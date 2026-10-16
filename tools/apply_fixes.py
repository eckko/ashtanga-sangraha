#!/usr/bin/env python3
"""Apply row-id keyed fixes to BOTH reference/md and reference/txt (Part 1).

Fix file: JSON list of
  {"id": "1.2._14_", "field": "src|split|hindi|eng", "old": "exact substring" ,
   "new": "replacement", "kind": "ocr|gloss|align|translation|typo", "note": "why"}
If "old" is missing/empty the whole field is replaced by "new".
"old" must occur exactly once in the field, else the fix is rejected.

Usage:
  python3 tools/apply_fixes.py --check audit/fixes/ch01.json [...]   # dry run
  python3 tools/apply_fixes.py audit/fixes/ch01.json [...]           # apply
"""
import re, sys, json, pathlib, collections

ROOT = pathlib.Path(__file__).resolve().parent.parent
REF = ROOT / "reference"
ROW = re.compile(r"^\|\s*(1\.(\d+)\._(\d+)_)\s*\|\s*(.*?)\s*\|\s*(.*?)\s*\|\s*$")
FIELDS = ("src", "split", "hindi", "eng")


def split_row(skt, hin):
    sm = re.match(r"^\*\*(.*)\*\*$", skt, re.S)
    body = sm.group(1) if sm else skt
    sp = body.split("<br/><br/>")
    src = sp[0]
    split = re.sub(r"^_|_$", "", sp[1]) if len(sp) > 1 else ""
    hp = hin.split("<br/><br/>")
    h = hp[0]
    e = re.sub(r"^_|_$", "", hp[1]) if len(hp) > 1 else ""
    return {"src": src, "split": split, "hindi": h, "eng": e}


def join_row(f):
    return f"**{f['src']}<br/><br/>_{f['split']}_**", f"{f['hindi']}<br/><br/>_{f['eng']}_"


def apply(fix, cur):
    old, new = fix.get("old") or "", fix["new"]
    if fix["field"] not in FIELDS:
        return None, "bad field"
    v = cur[fix["field"]]
    if not old:
        return new, None
    c = v.count(old)
    if c != 1:
        return None, f"old occurs {c}x in {fix['field']}"
    return v.replace(old, new), None


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    check = "--check" in sys.argv
    fixes = []
    for a in args:
        fixes += json.loads(pathlib.Path(a).read_text(encoding="utf-8"))
    by_id = collections.defaultdict(list)
    for f in fixes:
        by_id[f["id"]].append(f)

    # md files
    done = rejected = 0
    msgs = []
    md_state = {}
    rowfields = {}  # id -> fields after md edit (for locating txt line)
    order = []  # (id) in global order, from md
    for n in range(1, 6):
        p = REF / "md" / f"ch01.{n:02d}.md"
        lines = p.read_text(encoding="utf-8").split("\n")
        for i, ln in enumerate(lines):
            m = ROW.match(ln)
            if not m:
                continue
            rid = m.group(1)
            order.append(rid)
            flds = split_row(m.group(4), m.group(5))
            orig = dict(flds)
            for fx in by_id.get(rid, []):
                nv, err = apply(fx, flds)
                if err:
                    rejected += 1
                    msgs.append(f"REJECT {rid} {fx['field']}: {err}")
                else:
                    flds[fx["field"]] = nv
                    done += 1
            rowfields[rid] = (orig, flds)
            if flds != orig:
                a, b = join_row(flds)
                lines[i] = f"| {rid} | {a} | {b} |"
        md_state[p] = lines

    unknown = [i for i in by_id if i not in rowfields]
    for u in unknown:
        msgs.append(f"UNKNOWN id {u}")

    # txt layers: nth non-blank source line == nth md row (verified by audit_part1.py)
    files = {"src": "ch01.txt", "split": "ch01-sandhi.txt", "hindi": "ch01-hindi.txt", "eng": "ch01-eng.txt"}
    txt = {k: (REF / "txt" / v).read_text(encoding="utf-8").split("\n") for k, v in files.items()}
    allorder = []
    for p in sorted((REF / "md").glob("ch01.*.md")):
        for ln in p.read_text(encoding="utf-8").split("\n"):
            m = ROW.match(ln)
            if m:
                allorder.append(m.group(1))
    nb = [i for i, s in enumerate(txt["src"]) if s.strip()]
    idx = {rid: nb[k] for k, rid in enumerate(allorder)}
    txt_miss = 0
    for rid, (orig, flds) in rowfields.items():
        for fld in FIELDS:
            if orig[fld] == flds[fld]:
                continue
            li = idx[rid]
            line = txt[fld][li]
            if line.strip() == orig[fld].strip():
                txt[fld][li] = flds[fld]
            elif orig[fld] and orig[fld] in line and line.count(orig[fld]) == 1:
                txt[fld][li] = line.replace(orig[fld], flds[fld])
            else:
                # fall back: re-apply each fix on the txt line itself
                ok = False
                for fx in by_id[rid]:
                    if fx["field"] != fld or not fx.get("old"):
                        continue
                    if line.count(fx["old"]) == 1:
                        txt[fld][li] = txt[fld][li].replace(fx["old"], fx["new"])
                        ok = True
                if not ok:
                    txt_miss += 1
                    msgs.append(f"TXT-DIFFERS {rid} {fld}: md and txt lines differ; txt left unchanged (needs manual look)")

    print(f"applied={done} rejected={rejected} unknown={len(unknown)} txt_unsynced={txt_miss}")
    for m in msgs:
        print(m)
    if check or rejected or unknown:
        if not check:
            print("Nothing written because of rejected/unknown fixes." if (rejected or unknown) else "")
        return 1 if (rejected or unknown) else 0
    for p, lines in md_state.items():
        p.write_text("\n".join(lines), encoding="utf-8")
    for k, v in files.items():
        (REF / "txt" / v).write_text("\n".join(txt[k]), encoding="utf-8")
    return 0


if __name__ == "__main__":
    sys.exit(main())
