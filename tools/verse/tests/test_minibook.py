#!/usr/bin/env python3
"""End to end on a tiny invented book: config -> make_bank.py (authored
module written with `from helpers import ...`) -> render_images.py with a
mermaid spec -> template validator (0 errors, 0 warnings).

    python3 tests/test_minibook.py [TEMPLATE_DIR]
"""
import json
import subprocess
import sys
import tempfile
from pathlib import Path

TOOLS = Path(__file__).resolve().parent.parent
TEMPLATE = Path(sys.argv[1] if len(sys.argv) > 1
                else "/home/claude/recall-quiz-site-template-2.2.1")
CHARAKA = Path("/home/claude/charaka-samhita")

MODULE = '''from helpers import mcq, match, order, fill, multi, accepts

AUTHORED = {"1": {
    "title": "दीर्घं जीवितम्",
    "question": "Whom did Bharadvāja approach, seeking a long life?",
    "rule": "इन्द्रम् ends in -म्: accusative, the person approached.",
    "limits": "The verse does not say why Indra was chosen.",
    "explain_hi": "भरद्वाज दीर्घ जीवन चाहते हुए इन्द्र के पास गए।",
    "hook": "भरद्वाज → इन्द्र",
    "core": False,
    "questions": [
        mcq("pretest", 0, "Seeking long life, to whom did Bharadvāja go?",
            ("Indra", "The verse says he approached Indra."),
            [("Brahmā", "Brahmā is not named in this verse."),
             ("Ātreya", "Ātreya is not named in this verse."),
             ("Agniveśa", "Agniveśa is not named in this verse.")],
            "इन्द्रम् is the object.", "इन्द्रम् = Indra (accusative)."),
        match(1, "Match each word to its meaning.",
              [["जीवितम्", "life"], ["इन्द्रम्", "Indra"],
               ["अमरेश्वरम्", "lord of the immortals"]],
              "Three words of the verse.", "Accusatives."),
        fill(2, "Bharadvāja approached ____ (type it in Devanagari).",
             accepts("इन्द्रम्"), "The verse names him.", "-म् = accusative.",
             "इन्द्रम् = Indra."),
        multi("discriminate", 3, "Which words are accusative?",
              [("इन्द्रम्", "accusative"), ("भरद्वाजः", "nominative"),
               ("जीवितम्", "accusative"), ("बुद्ध्वा", "absolutive")],
              [0, 2], "Two accusatives.", "-म् marks the accusative."),
        order(4, "Put the actions in order.",
              ["wishing for long life", "approaching Indra",
               "knowing him fit to give refuge"],
              "The verse gives these in this order.", "Order of the verse.",
              role="apply"),
        mcq("transfer", 5, "In ‘रामम् पश्यति’, what is रामम्?",
            ("The object", "-म् marks the accusative: the one seen."),
            [("The subject", "The subject would be रामः."),
             ("The verb", "पश्यति is the verb."),
             ("A place", "Nothing marks a place.")],
            "रामम् is accusative.", "-म् = object.",
            teaches="Accusative -म् marks the object."),
    ]}}
NOTES_HI = {"1": "‘उग्रतपाः’ का विसर्ग ‘बुद्ध्वा’ से पहले लुप्त है।"}
AIDS = {"1": {"frame": "कौन: भरद्वाज · किसके पास: इन्द्र · क्यों: दीर्घ जीवन",
              "diagram": "भरद्वाज → इन्द्र"}}
IMAGE_SPECS = {("1", "diagram"): {
    "file": "mini-1.svg", "alt": "Bharadvaja goes to Indra", "type": "mermaid",
    "code": 'flowchart LR\\n  A["भरद्वाज"] --> B["इन्द्र"]'}}
'''


def main():
    with tempfile.TemporaryDirectory() as tmp:
        book = Path(tmp)
        (book / "data").mkdir()
        unit = json.loads((CHARAKA / "data" / "sutrasthana1_verses.json")
                          .read_text(encoding="utf8"))[2]
        unit["n"] = "1"
        (book / "data" / "chapter1_verses.json").write_text(
            json.dumps([unit], ensure_ascii=False), encoding="utf8")
        (book / "tools" / "authored").mkdir(parents=True)
        (book / "tools" / "authored" / "ch1_batch_01.py").write_text(
            MODULE, encoding="utf8")
        (book / "verse_book.json").write_text(json.dumps({
            "bank_id": "mini", "title": "Mini", "genre": "mini",
            "summary": "A tiny test book.",
            "ref_template": "मिनी · अध्याय {chapter} · {kind} {unit}।",
            "chapters": [{"number": 1, "title": "एक", "prefix": "mb1",
                          "summary": "One verse.", "metre": "anustubh"}]},
            ensure_ascii=False), encoding="utf8")
        steps = [
            [sys.executable, str(TOOLS / "make_bank.py"), str(book)],
            [sys.executable, str(TOOLS / "render_images.py"), str(book)]]
        for cmd in steps:
            run = subprocess.run(cmd, capture_output=True, text=True)
            print(run.stdout.strip() or run.stderr.strip())
            if run.returncode:
                print("FAIL:", " ".join(cmd[1:]))
                return 1
        bank = json.loads((book / "questions.json").read_text(encoding="utf8"))
        card = bank["concepts"][0]["card"]["blocks"]
        aids = [b for b in card if b["key"] == "aids"][0]["aids"]
        kinds = [a["aid"] for a in aids]
        ok = (kinds == ["frame", "diagram", "metre"]
              and aids[1]["image"]["src"] == "images/aids/mini-1.svg"
              and (book / "images" / "aids" / "mini-1.svg").exists()
              and bank["concepts"][0]["id"] == "mb1-001"
              and len(bank["questions"]) == 6)
        print("aids:", kinds, "-> ok" if ok else "-> UNEXPECTED")
        validator = TEMPLATE / "tools" / "validate_bank.py"
        if validator.exists():
            run = subprocess.run([sys.executable, str(validator),
                                  str(book / "questions.json")],
                                 capture_output=True, text=True)
            print(run.stdout.strip()[-600:])
            ok = ok and run.returncode == 0 and "0 error(s), 0 warning(s)" in run.stdout
        else:
            print("template validator not found; skipped")
        print("PASS" if ok else "FAIL")
        return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
