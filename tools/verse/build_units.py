#!/usr/bin/env python3
"""Turn a four-layer study text into verse units for the verse-study pipeline.

    python3 build_units.py OUT_DIR PART_FILE [PART_FILE ...]
            [--chapter-numbers 1,2,3,4,5] [--uncertain UNCERTAIN_PART_FILE]

A study text (the format the user's Sanskrit EPUBs use) has, per numbered
line "C.L" (chapter C, line L), four layers in this order:
  Sanskrit as printed (Devanagari) / word-split (sandhi resolved) /
  Hindi / English.
Each PART_FILE is one chapter as written by tools/extract_book.py
(a "## Chapter N" heading, then blocks of five lines: "C.L" + 4 layers).
UNCERTAIN_PART_FILE (optional) is the appendix listing damaged lines
("C.L [tags] note").

Output: OUT_DIR/chapterN_units.json, a list of unit records in text order:
  n          unit number in the chapter, as a string ("1", "2", ...)
  type       "verse" or "prose"
  line_ids   the book's own line numbers, e.g. ["5.2", "5.3"]
  lines_deva the Sanskrit as printed, one string per line
  lines_iast the same, IAST, one string per line (tokens as printed)
  book_split / book_hindi / book_english   the book's other layers (reference
             only; the draft agents write the final Hindi and English)
  uncertain  [{"line": "5.14", "note": "..."}] damaged lines inside the unit

Grouping rule (mechanical; reviewers may ask for overrides):
  * a line starting with the formula "अथात" stands alone (prose);
  * the closing "iti ... adhyāyaḥ" line stands alone (prose);
  * a line is verse-like when it has 13 to 24 aksharas (an anuṣṭubh half
    verse is 16, an upajāti line 22);
  * a run of consecutive verse-like lines of the same length class (about
    16 or about 22) is cut into pairs (one printed verse = two half-verse
    lines); an odd last line stands alone;
  * every other line is a prose unit by itself.
Overrides: OUT_DIR/grouping_overrides.json, {"3": [["3.5"], ["3.6","3.7"]]}
maps a chapter to the exact list of line-id groups to use instead.
"""
import argparse
import json
import re
import sys
import unicodedata
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from metre import syllable_ends  # noqa: E402
from indic_transliteration import sanscript as S  # noqa: E402

LINE_ID = re.compile(r"^(\d+)\.(\d+)$")
FORMULA = "अथात"


def read_blocks(path):
    """[(line_id, deva, split, hindi, english)] from one chapter part file."""
    rows = []
    lines = Path(path).read_text(encoding="utf-8").split("\n")
    i = 0
    while i < len(lines):
        if LINE_ID.match(lines[i].strip()) and i + 4 < len(lines) + 0:
            block = [x.strip() for x in lines[i + 1:i + 5]]
            if len(block) == 4:
                rows.append((lines[i].strip(), *block))
                i += 5
                continue
        i += 1
    return rows


def verse_like(deva):
    n = len(syllable_ends(deva))
    return 13 <= n <= 24


def metre_class(deva):
    """22 for upajāti-length lines, 16 for anuṣṭubh-length ones."""
    return 22 if len(syllable_ends(deva)) >= 20 else 16


def colophon(deva):
    """The closing line "iti ... nāma ... adhyāyaḥ" is its own unit."""
    return deva.startswith("इति") and "ध्याय" in deva


def group(rows):
    """List of lists of rows."""
    groups, run = [], []

    def flush():
        for k in range(0, len(run), 2):
            groups.append(run[k:k + 2])
        run.clear()

    for row in rows:
        deva = row[1]
        if deva.startswith(FORMULA) or colophon(deva) or not verse_like(deva):
            flush()
            groups.append([row])
        else:
            if run and metre_class(run[-1][1]) != metre_class(deva):
                flush()
            run.append(row)
    flush()
    return groups


def uncertain_lines(path):
    out = {}
    if not path:
        return out
    for text in Path(path).read_text(encoding="utf-8").split("\n"):
        m = re.match(r"^(\d+\.\d+)\s+(.*)$", text.strip())
        if m:
            out[m.group(1)] = m.group(2)
    return out


def to_iast(text):
    return S.transliterate(unicodedata.normalize("NFC", text), S.DEVANAGARI,
                           S.IAST)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("out_dir")
    ap.add_argument("parts", nargs="+")
    ap.add_argument("--chapter-numbers")
    ap.add_argument("--uncertain")
    a = ap.parse_args()
    out = Path(a.out_dir)
    out.mkdir(parents=True, exist_ok=True)
    over_path = out / "grouping_overrides.json"
    overrides = json.loads(over_path.read_text()) if over_path.exists() else {}
    unc = uncertain_lines(a.uncertain)
    numbers = a.chapter_numbers.split(",") if a.chapter_numbers else None
    for k, part in enumerate(a.parts):
        rows = read_blocks(part)
        if not rows:
            print("no lines in", part)
            continue
        ch = numbers[k] if numbers else rows[0][0].split(".")[0]
        by_id = {r[0]: r for r in rows}
        if ch in overrides:
            groups = [[by_id[x] for x in g] for g in overrides[ch]]
        else:
            groups = group(rows)
        units = []
        for n, g in enumerate(groups, 1):
            deva = [r[1] for r in g]
            is_verse = all(verse_like(d) for d in deva) \
                and not deva[0].startswith(FORMULA) and not colophon(deva[0])
            units.append({
                "n": str(n), "type": "verse" if is_verse else "prose",
                "line_ids": [r[0] for r in g],
                "lines_deva": deva,
                "lines_iast": [to_iast(d) for d in deva],
                "book_split": [r[2] for r in g],
                "book_hindi": [r[3] for r in g],
                "book_english": [r[4] for r in g],
                "uncertain": [{"line": r[0], "note": unc[r[0]]}
                              for r in g if r[0] in unc],
            })
        target = out / f"chapter{ch}_units.json"
        target.write_text(json.dumps(units, ensure_ascii=False, indent=1),
                          encoding="utf-8")
        print(f"chapter {ch}: {len(rows)} lines -> {len(units)} units "
              f"({sum(u['type'] == 'verse' for u in units)} verse, "
              f"{sum(u['type'] == 'prose' for u in units)} prose, "
              f"{sum(bool(u['uncertain']) for u in units)} with uncertain lines)")


if __name__ == "__main__":
    main()
