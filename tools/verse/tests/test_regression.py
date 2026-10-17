#!/usr/bin/env python3
"""Regression: the generic toolkit must rebuild the Charaka Samhita bank.

    python3 tests/test_regression.py [CHARAKA_DIR]

Copies CHARAKA_DIR (default /home/claude/charaka-samhita) to a temp dir,
adds a verse_book.json that reproduces its settings (authored modules are
the repo's own tools/*.py), runs ../make_bank.py and compares the result
with the repo's questions.json: same bank fields, concepts, ids, blocks,
questions. Key order and whitespace are ignored. Exit code 1 on any
difference.
"""
import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

TOOLS = Path(__file__).resolve().parent.parent
SOURCE = Path(sys.argv[1] if len(sys.argv) > 1
              else "/home/claude/charaka-samhita")

CONFIG = {
    "bank_id": "caraka-sutra",
    "title": "चरकसंहिता — सूत्रस्थान",
    "genre": "चरकसंहिता",
    "summary": ("The Charaka Samhita, Sūtrasthāna chapters 1 to 4: how "
                "Āyurveda came down from Brahmā to the sages, the drugs and "
                "gruels of the five cleansing treatments, the pastes applied "
                "to the skin, and the fifty groups of ten drugs."),
    "scroll_buttons": True,
    "labels": {"unit": "Chapter", "units": "chapters", "topic": "Verse",
               "whole": "Whole chapter"},
    "data_pattern": "data/sutrasthana{N}_verses.json",
    "authored_dir": "tools",
    "ref_template": "चरकसंहिता · सूत्रस्थान · अध्याय {chapter} · {kind} {unit}।",
    "source_disclaimer": ("पाठ: SARIT (एक ही स्रोत)। हिन्दी और English: "
                          "AI-रचित, AI-समीक्षित; विद्वान् से जाँच शेष।"),
    "gram_overrides": {
        "स्म": "अव्यय (निपात); ‘ह स्म’ कथन-शैली में, यहाँ लिट् ‘आह’ के साथ",
        "यथा-प्रोक्तम्": ("पु. द्वितीया ए.व. (‘आयुर्वेदम्’ का विशेषण); "
                          "यथा + प्रोक्तम्, क्रियाविशेषण रूप में भी पढ़ा जा "
                          "सकता है")},
    "chapters": [
        {"number": 1, "title": "दीर्घञ्जीवितीय", "prefix": "su1",
         "authored": ["ch1_authored.py", "ch1_aids.py", "batch_*.py"],
         "sections": "tools/sections.py:RANGES", "metre": "anustubh",
         "summary": ("How Āyurveda passed from Brahmā to Indra, why the sages "
                     "gathered on the Himālaya, and who they were.")},
        {"number": 2, "title": "अपामार्गतण्डुलीय", "prefix": "su2",
         "sections": "tools/sections.py:RANGES_2", "metre": "anustubh",
         "summary": ("The drug groups for the five treatments, the "
                     "twenty-eight gruels, and the physician who can use "
                     "them.")},
        {"number": 3, "title": "आरग्वधीय", "prefix": "su3",
         "sections": "tools/sections.py:RANGES_3", "metre": "upajati",
         "summary": ("The thirty-two medicinal pastes (pradeha) and the "
                     "conditions of the skin and body they are used for.")},
        {"number": 4, "title": "षड्विरेचनशताश्रितीय", "prefix": "su4",
         "sections": "tools/sections.py:RANGES_4", "metre": "anustubh",
         "summary": ("The six hundred purgative formulas, the five kinds of "
                     "preparation, and the fifty groups of ten drugs each.")},
    ],
}


def main():
    with tempfile.TemporaryDirectory() as tmp:
        book = Path(tmp) / "charaka"
        shutil.copytree(SOURCE, book, ignore=shutil.ignore_patterns(
            ".git", "__pycache__"))
        (book / "verse_book.json").write_text(
            json.dumps(CONFIG, ensure_ascii=False, indent=1), encoding="utf8")
        out = Path(tmp) / "bank.json"
        run = subprocess.run(
            [sys.executable, str(TOOLS / "make_bank.py"), str(book),
             "--out", str(out)], capture_output=True, text=True)
        print(run.stdout.strip())
        if run.returncode:
            print(run.stderr)
            return 1
        new = json.loads(out.read_text(encoding="utf8"))
        pictures = check_pictures(book, SOURCE)
    old = json.loads((SOURCE / "questions.json").read_text(encoding="utf8"))
    problems = compare(old, new) + pictures
    nq = len(new["questions"])
    print(f"generated {len(new['concepts'])} concepts, {nq} questions; "
          f"repo has {len(old['concepts'])} / {len(old['questions'])}")
    if problems:
        print(f"{len(problems)} DIFFERENCES")
        for p in problems[:40]:
            print(" -", p)
        return 1
    print("IDENTICAL (concepts, ids, block keys, questions, bank fields)")
    return 0


def check_pictures(book, source):
    """render_images.py on the copy must redraw the repo's own pictures
    (chain / table / split specs) byte for byte."""
    legacy = ["quote", "rope-vajra-umbrella", "baton", "stairs", "stone",
              "torch-slope", "ledges-8", "ledges-9", "ledges-10"]
    out = book / "fresh_aids"  # the 9 hand-drawn pictures are not specs
    out.mkdir()
    for name in legacy:
        shutil.copy(source / "images" / "aids" / f"{name}.svg", out)
    run = subprocess.run(
        [sys.executable, str(TOOLS / "render_images.py"), str(book),
         "--out", str(out)], capture_output=True, text=True)
    print(run.stdout.strip().splitlines()[-1] if run.stdout.strip()
          else run.stderr)
    problems = []
    if run.returncode:
        problems.append("render_images.py failed:\n" + run.stdout[-600:])
    same = 0
    for f in sorted(out.glob("*.svg")):
        ref = source / "images" / "aids" / f.name
        if not ref.exists():
            problems.append(f"picture {f.name} not in the repo")
        elif ref.read_text(encoding="utf8") != f.read_text(encoding="utf8"):
            problems.append(f"picture {f.name} differs from the repo's")
        else:
            same += 1
    print(f"{same} pictures identical to the repo's")
    return problems


def diff(a, b, path=""):
    """First few differing paths between two JSON values."""
    if type(a) is not type(b):
        return [f"{path}: type {type(a).__name__} vs {type(b).__name__}"]
    if isinstance(a, dict):
        out = []
        for k in sorted(set(a) | set(b)):
            if k not in a:
                out.append(f"{path}/{k}: only in generated")
            elif k not in b:
                out.append(f"{path}/{k}: only in repo")
            else:
                out += diff(a[k], b[k], f"{path}/{k}")
        return out
    if isinstance(a, list):
        if len(a) != len(b):
            return [f"{path}: length {len(a)} vs {len(b)}"]
        out = []
        for i, (x, y) in enumerate(zip(a, b)):
            out += diff(x, y, f"{path}[{i}]")
        return out
    return [] if a == b else [f"{path}: {a!r:.80} vs {b!r:.80}"]


def compare(old, new):
    problems = []
    for key in old:
        if key in ("concepts", "questions"):
            continue
        problems += [f"bank {d}" for d in diff(old[key], new.get(key),
                                               key)]
    for key in new:
        if key not in old:
            problems.append(f"bank field {key} only in generated")
    old_c = {c["id"]: c for c in old["concepts"]}
    new_c = {c["id"]: c for c in new["concepts"]}
    if [c["id"] for c in old["concepts"]] != [c["id"] for c in new["concepts"]]:
        problems.append("concept ids / order differ: "
                        f"{sorted(set(old_c) ^ set(new_c))[:10]}")
    for cid in old_c.keys() & new_c.keys():
        a, b = old_c[cid], new_c[cid]
        if [x["key"] for x in a["card"]["blocks"]] != \
                [x["key"] for x in b["card"]["blocks"]]:
            problems.append(f"{cid}: block keys differ")
        problems += diff(a, b, cid)
    old_q = {q["id"]: q for q in old["questions"]}
    new_q = {q["id"]: q for q in new["questions"]}
    if [q["id"] for q in old["questions"]] != [q["id"] for q in new["questions"]]:
        problems.append("question ids / order differ: "
                        f"{sorted(set(old_q) ^ set(new_q))[:10]}")
    for qid in old_q.keys() & new_q.keys():
        problems += diff(old_q[qid], new_q[qid], qid)
    return problems


if __name__ == "__main__":
    sys.exit(main())
