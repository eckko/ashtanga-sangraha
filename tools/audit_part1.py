#!/usr/bin/env python3
"""Read-only audit of Part 1 (Sutrasthana) source text.

Checks the txt layers (source, sandhi split, hindi, eng) and the md tables,
assigns each row to a chapter via the md ids, and writes a per-chapter suspect
report. It never edits the source.

Usage: python3 tools/audit_part1.py [--out audit/part1-suspects]
"""
import re, sys, json, unicodedata, collections, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
REF = ROOT / "reference"
OUT = ROOT / "audit" / "part1-suspects"
if "--out" in sys.argv:
    OUT = pathlib.Path(sys.argv[sys.argv.index("--out") + 1])

DEV = re.compile(r"[ऀ-ॿ]")
LATIN = re.compile(r"[A-Za-z]")
# characters allowed in a Sanskrit source / split line
SKT_OK = re.compile(r"^[ऀ-ॿ‌‍\s\d\-\.,;:!?'\"()\[\]/‘’“”]*$")
ODD_SCRIPT = re.compile(r"[ঀ-৿਀-෿　-鿿＀-￯]")
DOUBLE_MATRA = re.compile(r"([ा-ौंः])\1")
MATRA_AFTER_MATRA = re.compile(r"[ा-ौ][ा-ौ]")
VIRAMA_BAD = re.compile(r"्[ऀ-ःा-ौ]")
LEADING_MATRA = re.compile(r"(^|\s)[ा-्ँ-ः]")
# known OCR confusions (suspect substring -> hint)
KNOWN = {"विष्य": "विधि?", "विष्यध्याय": "विधि?", "ााय": "doubled aa-matra",
         "। ।": "split danda", "॥॥": "doubled danda"}


def norm(s):
    s = unicodedata.normalize("NFC", s)
    s = s.replace("‌", "").replace("‍", "")
    return re.sub(r"[\s।॥|.,;:!?\-'\"()\d]+", "", s)


def read_txt(name):
    p = REF / "txt" / name
    return p.read_text(encoding="utf-8").split("\n")


def parse_md():
    rows = []
    for n in range(1, 41):
        p = REF / "md" / f"ch01.{n:02d}.md"
        if not p.exists():
            rows.append(("MISSING", n, None))
            continue
        for ln in p.read_text(encoding="utf-8").split("\n"):
            m = re.match(r"^\|\s*(1\.\d+\._\d+_)\s*\|\s*(.*?)\s*\|\s*(.*?)\s*\|\s*$", ln)
            if not m:
                continue
            rid, skt, hin = m.groups()
            sm = re.match(r"^\*\*(.*?)\*\*$", skt)
            skt_body = sm.group(1) if sm else skt
            sp = skt_body.split("<br/><br/>")
            src = sp[0].strip()
            split = re.sub(r"^_|_$", "", sp[1].strip()) if len(sp) > 1 else ""
            hp = hin.split("<br/><br/>")
            h = hp[0].strip()
            e = re.sub(r"^_|_$", "", hp[1].strip()) if len(hp) > 1 else ""
            rows.append((rid, n, (src, split, h, e)))
    return rows


def main():
    src = read_txt("ch01.txt")
    spl = read_txt("ch01-sandhi.txt")
    hin = read_txt("ch01-hindi.txt")
    eng = read_txt("ch01-eng.txt")
    summary = {"txt_lines": [len(src), len(spl), len(hin), len(eng)]}
    flags = collections.defaultdict(list)  # chapter -> [(id, kind, detail)]

    # 1. layer alignment: same length and blanks at same positions
    n = min(len(src), len(spl), len(hin), len(eng))
    for i in range(n):
        blanks = [not x.strip() for x in (src[i], spl[i], hin[i], eng[i])]
        if len(set(blanks)) > 1:
            flags[0].append((f"txt:{i+1}", "layer-blank-mismatch", str(blanks)))

    # 2. md rows vs txt non-blank lines, in order
    md = parse_md()
    missing = [r[1] for r in md if r[0] == "MISSING"]
    md = [r for r in md if r[0] != "MISSING"]
    nb = [i for i in range(n) if src[i].strip()]
    summary["md_rows"] = len(md)
    summary["txt_nonblank"] = len(nb)
    summary["md_files_missing"] = missing
    ids_seen = collections.Counter(r[0] for r in md)
    for rid, c in ids_seen.items():
        if c > 1:
            flags[0].append((rid, "duplicate-id", str(c)))

    # walk both lists; resync greedily if a row disagrees (reports offsets)
    j = 0
    chap_rows = collections.Counter()
    for rid, ch, (s, sp, h, e) in md:
        chap_rows[ch] += 1
        while j < len(nb) and norm(src[nb[j]]) != norm(s):
            # try small lookahead before declaring mismatch
            look = [k for k in range(j, min(j + 4, len(nb))) if norm(src[nb[k]]) == norm(s)]
            if look:
                for k in range(j, look[0]):
                    flags[ch].append((f"txt:{nb[k]+1}", "txt-line-not-in-md", src[nb[k]][:60]))
                j = look[0]
                break
            flags[ch].append((rid, "md-vs-txt-source-differs",
                              f"md={s[:50]} | txt={src[nb[j]][:50]}"))
            break
        if j < len(nb):
            j += 1
        # per-row checks use the md row; txt line looked up by position
        chk(flags, ch, rid, s, sp, h, e)
    summary["txt_lines_after_last_md_row"] = len(nb) - j
    summary["rows_per_chapter"] = dict(sorted(chap_rows.items()))

    # 3. collapse untranslated chapters into one chapter-level flag
    for ch in list(flags):
        if ch == 0:
            continue
        hs = sum(1 for _, k, _ in flags[ch] if k == "hindi-equals-source")
        es = sum(1 for _, k, _ in flags[ch] if k == "english-is-devanagari")
        if hs > 0.5 * chap_rows[ch] or es > 0.5 * chap_rows[ch]:
            flags[ch] = [f for f in flags[ch] if f[1] not in ("hindi-equals-source", "english-is-devanagari")]
            flags[ch].insert(0, (f"ch{ch}", "UNTRANSLATED-CHAPTER",
                                 f"hindi==source in {hs}/{chap_rows[ch]} rows, english not English in {es}/{chap_rows[ch]}"))
    OUT.mkdir(parents=True, exist_ok=True)
    tot = collections.Counter()
    for ch in sorted(flags):
        by = collections.Counter(k for _, k, _ in flags[ch])
        tot.update(by)
        lines = [f"# Part 1 chapter {ch} suspects ({sum(by.values())})", ""]
        lines += [f"- {k}: {v}" for k, v in by.most_common()]
        lines += ["", "| id | kind | detail |", "|---|---|---|"]
        for rid, k, d in flags[ch]:
            lines.append(f"| {rid} | {k} | {d.replace('|', '/')} |")
        (OUT / f"ch{ch:02d}.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    summary["flags_by_kind"] = dict(tot.most_common())
    summary["flags_by_chapter"] = {c: len(v) for c, v in sorted(flags.items())}
    (OUT / "summary.json").write_text(json.dumps(summary, ensure_ascii=False, indent=1), encoding="utf-8")
    print(json.dumps(summary, ensure_ascii=False, indent=1))


def chk(flags, ch, rid, s, sp, h, e):
    F = lambda k, d: flags[ch].append((rid, k, d))
    # Sanskrit source
    if not DEV.search(s):
        F("src-no-devanagari", s[:50])
    if ODD_SCRIPT.search(s + sp):
        F("odd-script", s[:50])
    if LATIN.search(s):
        F("latin-in-source", "".join(LATIN.findall(s))[:30])
    if LATIN.search(sp):
        F("latin-in-split", " ".join(re.findall(r"[A-Za-z]+", sp))[:30])
    if not SKT_OK.match(s.replace("॥", "").replace("।", "")) and not LATIN.search(s) and not ODD_SCRIPT.search(s):
        F("odd-char-source", "".join(sorted(set(c for c in s if not SKT_OK.match(c))))[:20])
    if MATRA_AFTER_MATRA.search(s) or DOUBLE_MATRA.search(s) or VIRAMA_BAD.search(s):
        F("malformed-akshara-source", s[:60])
    if LEADING_MATRA.search(s):
        F("leading-matra-source", s[:60])
    for k, hint in KNOWN.items():
        if k in s:
            F("known-ocr", f"{k} {hint}")
    # split vs source
    if not sp:
        F("missing-split", s[:50])
    else:
        a, b = norm(s), norm(sp)
        if a != b:
            # sandhi-viccheda legitimately changes letters; flag only large divergence
            import difflib
            r = difflib.SequenceMatcher(None, a, b).ratio()
            if r < 0.80:
                F("split-diverges", f"ratio={r:.2f} src={s[:40]} split={sp[:40]}")
    # Hindi
    if not h:
        F("missing-hindi", "")
    else:
        if ODD_SCRIPT.search(h) or "。" in h:
            F("odd-script-hindi", h[:50])
        if norm(h) == norm(s) and len(s) > 12:
            F("hindi-equals-source", h[:40])
        if len(s) > 25 and not DEV.search(h):
            F("hindi-no-devanagari", h[:40])
    # English
    if not e:
        F("missing-english", "")
    else:
        if DEV.sub("", e).strip() == "" and len(e) > 3:
            F("english-is-devanagari", e[:40])
        if len(s) > 25 and len(e) < 0.2 * len(s):
            F("english-too-short", f"{len(e)} vs src {len(s)}")
        if len(e) > 12 * max(len(s), 20):
            F("english-too-long", f"{len(e)} vs src {len(s)}")
        # unbalanced parens in glosses
        if e.count("(") != e.count(")"):
            F("english-unbalanced-paren", e[:50])
    if h and h.count("(") != h.count(")"):
        F("hindi-unbalanced-paren", h[:50])
    # length ratio hindi vs english (misalignment sign)
    if h and e and len(h) > 40 and len(e) > 40:
        r = len(e) / len(h)
        if r < 0.25 or r > 4:
            F("hindi-english-length-skew", f"hin={len(h)} eng={len(e)}")


if __name__ == "__main__":
    main()
