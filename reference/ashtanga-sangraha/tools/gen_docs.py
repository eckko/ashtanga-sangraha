#!/usr/bin/env python3
"""Generate toc.md, STATUS.md, ISSUES.md and the audit TSVs from text/ + raw/structure-md-user-upload.md.
Run after build_text.py. Usage: gen_docs.py BOOK_DIR"""
import re, sys, json, difflib, unicodedata
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from english_names import NAMES

book = Path(sys.argv[1])
text = book / "text"
PART_NAMES = {
    1: ("सूत्रस्थानम्", "Sūtrasthāna (Fundamentals)"), 2: ("शारीरस्थानम्", "Śārīrasthāna (Anatomy and embryology)"),
    3: ("निदानस्थानम्", "Nidānasthāna (Causes and diagnosis)"), 4: ("चिकित्सास्थानम्", "Cikitsāsthāna (Treatment)"),
    5: ("कल्पस्थानम्", "Kalpasthāna (Formulations)"), 6: ("उत्तरस्थानम्", "Uttarasthāna (Specialties and supplements)"),
}
# structure.md rows -> (Sanskrit name, Hindi gloss)
struct = {}
for line in (book / "raw" / "structure-md-user-upload.md").read_text(encoding="utf-8").splitlines():
    m = re.match(r"^\|\s*(\d)\._(\d+)_\s*\|\s*(.*?)\s*\|\s*(.*?)\s*\|\s*$", line)
    if m:
        name = re.sub(r"^\[(.*?)\]\(.*?\)$", r"\1", m.group(3))
        struct[(int(m.group(1)), int(m.group(2)))] = (name, m.group(4))
assert len(struct) == 150, len(struct)

def read(path):
    return [l.split(" | ", 1) for l in path.read_text(encoding="utf-8").splitlines()]

chapters = []
for p in range(1, 7):
    for c in range(1, {1: 41, 2: 13, 3: 17, 4: 25, 5: 9, 6: 51}[p]):
        chapters.append((p, c))
assert len(chapters) == 150

stray = []        # (id, file, char names)
lowsim = []       # (id, ratio)
colophon_issues = []
STRAY_OK = set(" ")
def strange(s, sandhi):
    out = []
    for ch in s:
        o = ord(ch)
        if 0x900 <= o <= 0x97F or ch == " ":
            if ch in "‌‍":
                out.append(ch)
            continue
        if ch == "-" and sandhi:
            continue
        out.append(ch)
    return out

def sim(a, b):
    n = lambda s: "".join(c for c in s if c not in " -‌‍")
    return difflib.SequenceMatcher(None, n(a), n(b), autojunk=False).ratio()

status_rows, toc_rows, totals = [], {}, 0
stripped = {}
for r in (book / "tools" / "stripped-numbers.tsv").read_text(encoding="utf-8").splitlines()[1:]:
    lid, src, a, b = r.split("\t")
    stripped[lid] = (a, b)

devnum = {c: i for i, c in enumerate("०१२३४५६७८९")}
def tonum(s):
    return int("".join(str(devnum.get(c, c)) for c in s)) if s else None

for p, c in chapters:
    rp = read(text / f"ch{p:02d}.{c:02d}.md")
    rs = read(text / f"ch{p:02d}.{c:02d}-sandhi.md")
    assert [i for i, _ in rp] == [i for i, _ in rs]
    totals += len(rp)
    nlow = 0
    for (lid, a), (_, b) in zip(rp, rs):
        for ch, sandhi, t in (("plain", False, a), ("sandhi", True, b)):
            bad = strange(t, sandhi)
            if bad:
                stray.append((lid, ch, "".join(bad), t[:60]))
        ratio = sim(a, b)
        if ratio < 0.6:
            nlow += 1
            lowsim.append((lid, round(ratio, 2)))
    # colophon check: last line (within the last 4) that starts with इति and mentions ध्याय
    col = None
    for lid, t in rp[-6:][::-1]:
        if t.lstrip("॥ ").startswith("इति") and "ध्याय" in t and lid in stripped:
            col = (lid, tonum(re.sub(r"[॥ ]", "", stripped[lid][0])))
            break
    if col is None:
        colophon_issues.append((f"{p:02d}.{c:02d}", "missing", "no chapter-end colophon with a number found in the last 6 lines"))
    elif col[1] != c:
        colophon_issues.append((col[0], "numbering", f"colophon number {col[1]} but chapter position is {c}"))
    name, gloss = struct[(p, c)]
    toc_rows.setdefault(p, []).append((c, name, NAMES[p][c - 1], gloss, len(rp), nlow))
    status_rows.append((p, c, len(rp), nlow))

# ---- TSVs
with (book / "tools" / "stray-characters.tsv").open("w", encoding="utf-8") as f:
    f.write("line_id\tfile\tstray_chars\ttext_start\n")
    for r in stray:
        f.write("\t".join(r) + "\n")
with (book / "tools" / "plain-vs-sandhi-low-similarity.tsv").open("w", encoding="utf-8") as f:
    f.write("line_id\tratio_after_removing_spaces_and_hyphens\n")
    for lid, r in lowsim:
        f.write(f"{lid}\t{r}\n")

# ---- toc.md
out = ["# Aṣṭāṅga Saṅgraha (अष्टाङ्गसंग्रह)", "",
       "- Author / compiler: Vāgbhaṭa (Siṃhagupta's son), Āyurveda, Ātreya tradition (colophon of Part 3 in the source: सिंहगुप्तसूनुश्रीमद्वाग्भटाचार्यविरचिते)",
       "- Subject and purpose of the book: a compendium of the eight branches of Āyurveda in six sthānas, 150 chapters (the source's own Part 1 chapter 1 says पञ्चाशदध्यायशतं षड्भिः स्थानैः)",
       "- Base edition: the 1888 Marathi-printed (Devanagari) edition as digitised by the owner from a poor scan; plain text = S1, sandhi-split counterpart = S2 (see sources.md)",
       "- Mapping: part = sthāna, chapter = adhyāya, verse = one source line (unit); the source has no verse numbers, so units are counted from 1 in each chapter",
       f"- Totals: 6 parts, 150 chapters, {totals} lines (units) extracted per version (traditional verse count: unknown; the edition's lines are pairs of pādas and prose paragraphs, so they are not verse numbers)",
       "- Chapter names and the one-line purposes below come from the owner's `structure.md` (Sanskrit title, Hindi gloss); English names are written by the extraction agent from the Sanskrit titles (inferred).",
       "- Layout: one file per chapter for every part (each part is over 1000 lines). Each chapter file `text/chPP.CC.md` has a line-aligned sandhi-split twin `text/chPP.CC-sandhi.md`.", ""]
for p in range(1, 7):
    sk, en = PART_NAMES[p]
    out += [f"## Part {p:02d}: {sk} ({en})", "",
            "| Part | Chapter | Sanskrit name | English name | Purpose | Verses (extracted) | Verses (traditional) | File | Status |",
            "|---|---|---|---|---|---|---|---|---|"]
    for c, name, eng, gloss, n, _ in toc_rows[p]:
        out.append(f"| {p:02d} | {c:02d} | {name} | {eng} | {gloss} | {n} | unknown | text/ch{p:02d}.{c:02d}.md | extracted |")
    out.append("")
(book / "toc.md").write_text("\n".join(out), encoding="utf-8")

# ---- STATUS.md
st = ["# Status: ashtanga-sangraha", "",
      "Updated: 2026-10-17 on branch docs/2026-10-17/version-1. Base source: S1 (plain), S2 (sandhi-split twin). All 150 chapters extracted; no translations (see sources.md).", "",
      "| Part | Chapter | Sanskrit lines | Source | Hindi | English | Check | Notes |", "|---|---|---|---|---|---|---|---|"]
for p, c, n, nlow in status_rows:
    note = f"{nlow} line(s) where sandhi twin differs a lot from plain (see tools/plain-vs-sandhi-low-similarity.tsv)" if nlow else ""
    st.append(f"| {p:02d} | {c:02d} | {n} | S1 + S2 | -- | -- | see README | {note} |")
st += ["", "## Next", "- Proofreading/verification stage (the plain text is a raw OCR-like scan; see ISSUES.md).",
       "- Translations: none added here (see sources.md for what exists in the repo and why it was left out)."]
(book / "STATUS.md").write_text("\n".join(st) + "\n", encoding="utf-8")

# ---- ISSUES.md
rows = []
latin = [r for r in stray if re.search(r"[A-Za-z]", r[2])]
for lid, ch, chars, t in latin:
    rows.append((lid + (" (sandhi)" if ch == "sandhi" else ""), "ocr", f"Latin letters {chars!r} inside the {ch} line (OCR noise or stray words); kept as in the source", "S1" if ch == "plain" else "S2", "check against the print edition"))
others = [r for r in stray if not re.search(r"[A-Za-z]", r[2])]
rows.append(("(many)", "possible-typo", f"{len(others)} lines contain non-Devanagari characters other than letters (':' used for visarga, '.', ',', '=', '|', '*', '·', '•', brackets, ZWJ/ZWNJ); kept as in the source. Full list: tools/stray-characters.tsv", "S1, S2", "proofread: ':' is probably ः"))
rows.append(("03.14.50", "other", "In the plain Part 3 file one line holds two verse-lines joined by '।' (…बहुव्रणं।शतारुः…). The sandhi file has them as two lines; the two sandhi lines were joined with a space so both files keep identical line IDs.", "S1, S2", "split into two lines at the proofreading stage (that adds an ID, so decide then)"))
for cid, kind, what in colophon_issues:
    rows.append((cid, kind, what, "S1", "chapter end may be damaged or the chapter boundary may be wrong"))
rows.append(("(all)", "variant", f"{len(lowsim)} lines where the plain line and its sandhi twin look very different (similarity < 0.6 after removing spaces/hyphens): possible misalignment or edits in S2. List: tools/plain-vs-sandhi-low-similarity.tsv", "S1, S2", "review the listed lines"))
rows.append(("(all)", "count", "The source has no verse numbers: IDs count source lines from 1 per chapter. The edition pairs pādas on one line and mixes prose, so a source line is not always a verse; traditional verse counts are unknown here.", "S1", "decide the final verse numbering at the verification stage"))
rows.append(("(all)", "numbering", f"{len(stripped)} trailing numbers like '॥ १ ॥' were removed from the text (verse/chapter numbers in the source) as FORMAT.md requires; they are recorded in tools/stripped-numbers.tsv", "S1, S2", "none"))
rows.append(("(toc)", "other", "structure.md has typos in titles that were copied as they are: 1.8 'अन्नरक्षाविष्यध्यायः' and other 'विष्यध्यायः' (probably विधि…), 4.8 'छर्दित्ह्रद्रोगतृष्णा…', 6.34 'ग्रंथ्यर्बुदश्लीपदापचीनाडीवि०' (cut off), 6.40 starts with a Bengali letter ব in 'বিষप्रतिषेधाध्यायः'", "structure.md", "fix the titles in toc.md when the owner confirms"))
rows.append(("01.* (plain)", "variant", "The repo's older reference/txt/ch01.txt differs from the uploaded Part 1 file in 254 lines (the repo copy looks proofread). This extraction uses the uploaded file as given.", "S1", "decide which Part 1 text is the base"))
iss = ["# Issues: ashtanga-sangraha", "", "Nothing in the text files was changed because of an issue.", "",
       "| Line ID | Kind | What | Source(s) | Suggested check |", "|---|---|---|---|---|"]
for r in rows:
    iss.append("| " + " | ".join(x.replace("|", "/") for x in r) + " |")
(book / "ISSUES.md").write_text("\n".join(iss) + "\n", encoding="utf-8")
print("lines/version", totals, "| stray", len(stray), "latin", len(latin), "| lowsim", len(lowsim), "| colophon issues", len(colophon_issues))
for r in colophon_issues[:40]:
    print("  ", r)
