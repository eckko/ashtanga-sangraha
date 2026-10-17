#!/usr/bin/env python3
"""Build text/chPP.CC.md (plain, S1) and text/chPP.CC-sandhi.md (sandhi-split, S2)
from the six part files and their sandhi-split counterparts.

Usage: build_text.py RAW_DIR OUT_BOOK_DIR
RAW_DIR holds the user's uploads (see PARTS below). Nothing is typed by hand:
every character comes from those files. Only mechanical changes are made:
NFC, trimmed/collapsed spaces, blank lines dropped, trailing verse number
(॥ १ ॥ -> ॥) removed (logged in tools/stripped-numbers.tsv).
"""
import re, sys, unicodedata, json
from pathlib import Path

PARTS = {  # part: (plain file, sandhi file)
    1: ("e72a6405-ch01.txt", "d86a13a8-ch01-sandhi.txt"),
    2: ("10a931f2-ch02.txt", "2d76add6-ch02-sandhi.txt"),
    3: ("a9dc7020-ch03.txt", "664c4428-ch03-sandhi.txt"),
    4: ("2b4d3e82-ch04.txt", "46971ff8-ch04-sandhi.txt"),
    5: ("e7799f70-ch05.txt", "540f9bcc-ch05-sandhi.txt"),
    6: ("67104a21-ch06.txt", "185c4547-ch06-sandhi.txt"),
}
EXPECTED = {1: 40, 2: 12, 3: 16, 4: 24, 5: 8, 6: 50}
# The plain file of part 3 has two verse-lines joined by '।' on one line (raw line 1294);
# the sandhi file has them as two lines (1294, 1295). Join the two sandhi lines so both
# files keep the same line IDs. (1-based line numbers of the *sandhi* file.)
SANDHI_JOINS = {3: [(1294, 1295, "।शतारुः")]}
NUM_TAIL = re.compile(r"\s*॥\s*[०-९0-9]+\s*(?:॥)?\s*$")
OPENER_MAX = 160


def norm(line):
    return re.sub(r"[ \t ]+", " ", unicodedata.normalize("NFC", line)).strip()


def is_opener(line):
    s = line.strip().lstrip("॥").strip()
    return s.startswith("अथ") and "याख्यास्याम" in s and len(s) < OPENER_MAX


def main(raw_dir, out_dir):
    raw_dir, out_dir = Path(raw_dir), Path(out_dir)
    (out_dir / "text").mkdir(parents=True, exist_ok=True)
    report = {"chapters": [], "stripped": [], "joins": [], "blank_dropped": {}}
    stripped_rows = []
    for part, (pf, sf) in PARTS.items():
        plain = (raw_dir / pf).read_text(encoding="utf-8").split("\n")
        sandhi = (raw_dir / sf).read_text(encoding="utf-8").split("\n")
        for a, b, marker in SANDHI_JOINS.get(part, []):
            assert marker in plain[a - 1], (part, a, "marker not in plain line")
            sandhi[a - 1] = sandhi[a - 1].rstrip() + " " + sandhi[b - 1].lstrip()
            del sandhi[b - 1]
            report["joins"].append({"part": part, "sandhi_lines": [a, b], "plain_line": a})
        assert len(plain) == len(sandhi), (part, len(plain), len(sandhi))
        for i, (x, y) in enumerate(zip(plain, sandhi)):
            assert bool(x.strip()) == bool(y.strip()), (part, i + 1, "blank mismatch")
        openers = [i for i, l in enumerate(plain) if is_opener(l)]
        assert len(openers) == EXPECTED[part] - (1 if part == 4 else 0) + (1 if part == 4 else 0), (part, len(openers))
        assert len(openers) == EXPECTED[part], (part, len(openers))
        starts = [0]  # chapter 1 also owns the title/invocation lines before it
        for o in openers[1:]:
            j = o  # non-blank lines directly above an opener (after the blank gap) belong to it
            while j > 0 and plain[j - 1].strip():
                j -= 1
            starts.append(j if j > starts[-1] and o - j <= 3 else o)
        ends = starts[1:] + [len(plain)]
        # a chapter k>1 may own non-blank lines just above its opener (none expected): report
        for k, (s, e) in enumerate(zip(starts, ends), start=1):
            if k > 1 and s != openers[k - 1]:
                report.setdefault("preamble_above_opener", []).append((part, k, openers[k - 1] - s))
            chunk = [(i, plain[i], sandhi[i]) for i in range(s, e) if plain[i].strip()]
            blanks = sum(1 for i in range(s, e) if not plain[i].strip())
            report["blank_dropped"][f"{part:02d}.{k:02d}"] = blanks
            rows_p, rows_s = [], []
            for n, (i, lp, ls) in enumerate(chunk, start=1):
                lid = f"{part:02d}.{k:02d}.{n}"
                tp, ts = norm(lp), norm(ls)
                mp, ms = NUM_TAIL.search(tp), NUM_TAIL.search(ts)
                if mp or ms:
                    stripped_rows.append((lid, i + 1, mp.group(0).strip() if mp else "", ms.group(0).strip() if ms else ""))
                    if mp:
                        tp = NUM_TAIL.sub(" ॥", tp).strip()
                    if ms:
                        ts = NUM_TAIL.sub(" ॥", ts).strip()
                rows_p.append(f"{lid} | {tp}")
                rows_s.append(f"{lid} | {ts}")
            (out_dir / "text" / f"ch{part:02d}.{k:02d}.md").write_text("\n".join(rows_p) + "\n", encoding="utf-8")
            (out_dir / "text" / f"ch{part:02d}.{k:02d}-sandhi.md").write_text("\n".join(rows_s) + "\n", encoding="utf-8")
            report["chapters"].append({"part": part, "chapter": k, "lines": len(chunk),
                                       "source_first_line": chunk[0][0] + 1, "source_last_line": chunk[-1][0] + 1})
    with (out_dir / "tools" / "stripped-numbers.tsv").open("w", encoding="utf-8") as f:
        f.write("line_id\tsource_line\tplain_stripped\tsandhi_stripped\n")
        for r in stripped_rows:
            f.write("\t".join(map(str, r)) + "\n")
    (out_dir / "tools" / "build-report.json").write_text(json.dumps(report, ensure_ascii=False, indent=1), encoding="utf-8")
    print(sum(c["lines"] for c in report["chapters"]), "lines in", len(report["chapters"]), "chapters;",
          len(stripped_rows), "trailing numbers stripped; joins", report["joins"],
          "; preamble_above_opener", report.get("preamble_above_opener"))


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
