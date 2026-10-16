#!/usr/bin/env python3
"""helpers.py: the question helpers behave as in Charaka's ch1_authored.py
and accepts() builds sensible lists.   python3 tests/test_helpers.py"""
import sys
from pathlib import Path

TOOLS = Path(__file__).resolve().parent.parent
sys.dont_write_bytecode = True
sys.path.insert(0, str(TOOLS))
sys.path.insert(0, "/home/claude/charaka-samhita/tools")
sys.dont_write_bytecode = True
import helpers  # noqa: E402


def main():
    errors = []

    def check(ok, name):
        print(("ok   " if ok else "FAIL ") + name)
        if not ok:
            errors.append(name)

    # same output as the Charaka original (if that repo is present)
    try:
        import ch1_authored as old
    except ImportError:
        old = None
    if old:
        args = ("pretest", 0, "Q?", ("R", "why"),
                [("a", "x"), ("b", "y"), ("c", "z")], "e", "r")
        for i in range(5):
            helpers._turn[0] = old._turn[0] = i  # rotation counters in step
            check(helpers.mcq(*args) == old.mcq(*args), "mcq equals original")
        check(helpers.match(1, "q", [["a", "b"]], "e", "r")
              == old.match(1, "q", [["a", "b"]], "e", "r"), "match")
        check(helpers.order(1, "q", ["a", "b"], "e", "r")
              == old.order(1, "q", ["a", "b"], "e", "r"), "order")
        check(helpers.fill(2, "q ____", ["a"], "e", "t", "r")
              == old.fill(2, "q ____", ["a"], "e", "t", "r"), "fill")
        check(helpers.multi("apply", 4, "q", [("a", "x"), ("b", "y")], [0],
                            "e", "r")
              == old.multi("apply", 4, "q", [("a", "x"), ("b", "y")], [0],
                           "e", "r"), "multi")
    a = helpers.accepts("सङ्ख्या")
    check(a[0] == "सङ्ख्या" and "संख्या" in a and "saṅkhyā" in a
          and "sankhya" not in a, "nasal variants, IAST, template-folded "
          "Latin not repeated")
    a = helpers.accepts("साङ्ख्य")
    check(a[:2] == ["साङ्ख्य", "सांख्य"], "sāṅkhya / sāṃkhya (Latin "
          "forms are already covered by the template's fold)")
    a = helpers.accepts("ऋषिः")
    check(a[0] == "ऋषिः" and "rishi" in a and "rushi" in a, "ṛṣiḥ Hinglish")
    a = helpers.accepts("अध्यायम्", None, "अध्याय")
    check(a[:3] == ["अध्यायम्", "अध्यायं", "अध्याय"], "extra forms")
    check(len(a) == len(set(a)), "no duplicates")
    check(helpers.accepts("धर्म", latin=False) == ["धर्म", "dharma"],
          "latin=False")
    print("PASS" if not errors else "FAIL")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
