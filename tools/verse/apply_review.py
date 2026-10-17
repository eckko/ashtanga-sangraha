#!/usr/bin/env python3
"""Apply an independent reviewer's machine-readable fixes to a drafted chunk.

    python3 apply_review.py DIR [--chunks 1,2,5] [--add-source]

For every chunk K found in DIR (or only those given) it reads
    chunkK_out.json      the draft (never modified)
    chunkK_review.json   {"units": [{"n", "verdict", "issues": [...]}]}
and writes
    chunkK_final.json    the draft with every patch applied
    changes_K.json       log: [{"n", "field", "old", "new", "why"}, ...]
Issues without a "patch" are printed as MANUAL items; nothing is applied
for them. The exit code is 1 if any patch could not be applied.

An issue may carry "patch": one object or a list of objects:
    {"n": "3", "op": "set", "field": "english", "value": "..."}
    {"n": "3", "op": "replace", "field": "hindi", "old": "...", "new": "..."}
    {"n": "3", "op": "word", "match_w": "me", "field": "gloss|gram|w",
     "value": "...", "occurrence": 1 | "all"}
    {"n": "3", "op": "append_note", "text": "..."}
"n" defaults to the unit of the issue; "why" defaults to the issue's
"problem". `field` of set/replace is a top-level field of the unit, or a
dotted path into it ("text_flags.0.why"). `word` finds words by their exact
`w` in all lines (and the lead-in); without "occurrence" the first match is
patched and a warning is printed when there are more.

--add-source  also copies type, line_ids, lines_deva, lines_iast, variants,
              src_flags, uncertain from chunkK_in.json into the final
              records (where they are missing), so the final file is a
              complete verse file ready to merge into data/.
"""
import argparse
import copy
import json
import re
import sys
from pathlib import Path

SOURCE_FIELDS = ["type", "line_ids", "lines_deva", "lines_iast", "variants",
                 "src_flags", "uncertain"]


class PatchError(Exception):
    pass


def get_path(rec, field):
    """(container, key) for a dotted path inside rec."""
    parts = field.split(".")
    cur = rec
    for p in parts[:-1]:
        cur = cur[int(p)] if isinstance(cur, list) else cur[p]
    last = parts[-1]
    return cur, (int(last) if isinstance(cur, list) else last)


def read(rec, field):
    try:
        box, key = get_path(rec, field)
        return box[key]
    except (KeyError, IndexError, ValueError, TypeError):
        raise PatchError(f"field {field!r} not found")


def write(rec, field, value):
    box, key = get_path(rec, field)
    box[key] = value


def all_words(rec):
    groups = list(rec.get("lead_in_tokens", []))
    for line in rec.get("lines", []):
        groups += line.get("tokens", [])
    return [w for t in groups for w in t.get("words", [])]


def apply_patch(rec, patch, why, log):
    n = rec["n"]
    op = patch.get("op")
    if op == "set":
        field = patch["field"]
        if field == "n":
            raise PatchError("the unit number cannot be changed")
        try:
            old = read(rec, field)
        except PatchError:
            old = None
        write(rec, field, patch["value"])
        log.append({"n": n, "field": field, "old": old,
                    "new": patch["value"], "why": why})
    elif op == "replace":
        field = patch["field"]
        old = read(rec, field)
        if not isinstance(old, str) or patch["old"] not in old:
            raise PatchError(f"{patch['old']!r} not found in {field}: "
                             f"{str(old)[:80]!r}")
        new = old.replace(patch["old"], patch["new"], 1)
        write(rec, field, new)
        log.append({"n": n, "field": field, "old": old, "new": new,
                    "why": why})
    elif op == "word":
        field = patch["field"]
        if field not in ("gloss", "gram", "w"):
            raise PatchError("word patches change gloss, gram or w")
        hits = [w for w in all_words(rec) if w.get("w") == patch["match_w"]]
        if not hits:
            raise PatchError(f"no word {patch['match_w']!r}")
        occ = patch.get("occurrence", 1)
        if occ == "all":
            chosen = hits
        else:
            if len(hits) > 1 and "occurrence" not in patch:
                print(f"  warning: unit {n}: {len(hits)} words "
                      f"{patch['match_w']!r}; patched the first "
                      "(use occurrence)")
            if not 1 <= occ <= len(hits):
                raise PatchError(f"occurrence {occ} of {len(hits)}")
            chosen = [hits[occ - 1]]
        for w in chosen:
            log.append({"n": n, "field": "word." + field, "word": w["w"],
                        "old": w.get(field), "new": patch["value"],
                        "why": why})
            w[field] = patch["value"]
    elif op == "append_note":
        old = rec.get("notes", "")
        new = (old + " " + patch["text"]).strip()
        rec["notes"] = new
        log.append({"n": n, "field": "notes", "old": old, "new": new,
                    "why": why})
    else:
        raise PatchError(f"unknown op {op!r}")


def chunk_numbers(d, wanted):
    if wanted:
        return [int(k) for k in wanted.split(",")]
    found = set()
    for f in d.glob("chunk*_review.json"):
        m = re.fullmatch(r"chunk(\d+)_review\.json", f.name)
        if m and (d / f"chunk{m.group(1)}_out.json").exists():
            found.add(int(m.group(1)))
    return sorted(found)


def process(d, k, add_source):
    out_path = d / f"chunk{k}_out.json"
    rev_path = d / f"chunk{k}_review.json"
    draft = json.loads(out_path.read_text(encoding="utf8"))
    review = json.loads(rev_path.read_text(encoding="utf8"))
    units = review.get("units", []) if isinstance(review, dict) else review
    final = copy.deepcopy(draft)  # the draft file is never touched
    by_n = {r["n"]: r for r in final}
    log, manual, failed, applied = [], [], [], 0
    for u in units:
        for issue in u.get("issues", []):
            patch = issue.get("patch")
            if not patch:
                manual.append((u["n"], issue))
                continue
            patches = patch if isinstance(patch, list) else [patch]
            for p in patches:
                n = str(p.get("n", u["n"]))
                why = p.get("why") or "reviewer ({}): {}".format(
                    issue.get("severity", "?"), issue.get("problem", ""))
                try:
                    if n not in by_n:
                        raise PatchError(f"unit {n} not in chunk {k}")
                    apply_patch(by_n[n], p, why, log)
                    applied += 1
                except (PatchError, KeyError) as err:
                    failed.append((n, p, str(err)))
    if add_source:
        in_path = d / f"chunk{k}_in.json"
        if in_path.exists():
            src = {r["n"]: r for r in json.loads(
                in_path.read_text(encoding="utf8"))}
            for r in final:
                for f in SOURCE_FIELDS:
                    if f in src.get(r["n"], {}) and f not in r:
                        r[f] = src[r["n"]][f]
        else:
            print(f"  --add-source: {in_path.name} not found")
    (d / f"chunk{k}_final.json").write_text(
        json.dumps(final, ensure_ascii=False, indent=1), encoding="utf8")
    (d / f"changes_{k}.json").write_text(
        json.dumps(log, ensure_ascii=False, indent=1), encoding="utf8")
    print(f"chunk {k}: {len(final)} units, {applied} patches applied "
          f"({len(log)} changes logged), {len(manual)} issues without "
          f"patch, {len(failed)} patches failed")
    for n, issue in manual:
        print("  MANUAL unit {} [{}] {} / {}: {}".format(
            n, issue.get("severity", "?"), issue.get("field", "?"),
            issue.get("where", ""), issue.get("problem", "")))
        if issue.get("fix"):
            print("         suggested fix:", issue["fix"])
    for n, p, err in failed:
        print(f"  FAILED unit {n} {p.get('op')}: {err}")
    return len(failed)


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("dir", help="folder with chunkK_out/review.json")
    ap.add_argument("--chunks", help="chunk numbers, e.g. 1,2 (default all)")
    ap.add_argument("--add-source", action="store_true")
    a = ap.parse_args()
    d = Path(a.dir)
    ks = chunk_numbers(d, a.chunks)
    if not ks:
        sys.exit("no chunkK_out.json + chunkK_review.json pairs in " + str(d))
    failures = sum(process(d, k, a.add_source) for k in ks)
    sys.exit(1 if failures else 0)


if __name__ == "__main__":
    main()
