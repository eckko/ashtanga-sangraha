#!/usr/bin/env python3
"""Join the reviewed chunks into the final verse file of one chapter.

    python3 merge_chunks.py DIR OUT_FILE
    e.g. merge_chunks.py work/ch1 data/chapter1_verses.json

Reads DIR/chunk1_final.json, chunk2_final.json, ... (made by
apply_review.py --add-source) in chunk order and checks what make_bank.py
needs: unique unit numbers, `type`, `lines_deva`, `lines`, `hindi`,
`english` on every record, one line of tokens per Devanagari line.
"""
import json
import re
import sys
from pathlib import Path

REQUIRED = ["n", "type", "lines_deva", "lines", "hindi", "english"]


def main():
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    d, out = Path(sys.argv[1]), Path(sys.argv[2])
    files = sorted(
        (int(re.fullmatch(r"chunk(\d+)_final\.json", f.name).group(1)), f)
        for f in d.glob("chunk*_final.json")
        if re.fullmatch(r"chunk(\d+)_final\.json", f.name))
    if not files:
        sys.exit(f"no chunkK_final.json in {d}")
    records, problems, seen = [], [], set()
    for k, f in files:
        for rec in json.loads(f.read_text(encoding="utf8")):
            n = rec.get("n")
            for key in REQUIRED:
                if key not in rec:
                    problems.append(f"chunk {k} unit {n}: missing {key}")
            if n in seen:
                problems.append(f"chunk {k}: unit {n} appears twice")
            seen.add(n)
            if "lines" in rec and "lines_deva" in rec and \
                    len(rec["lines"]) != len(rec["lines_deva"]):
                problems.append(f"unit {n}: {len(rec['lines'])} token lines "
                                f"for {len(rec['lines_deva'])} Sanskrit lines")
            records.append(rec)
    for p in problems:
        print("PROBLEM", p)
    if problems:
        sys.exit(f"{len(problems)} problem(s); nothing written")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(records, ensure_ascii=False, indent=1),
                   encoding="utf8")
    print(f"{len(records)} units from {len(files)} chunks -> {out}")


if __name__ == "__main__":
    main()
