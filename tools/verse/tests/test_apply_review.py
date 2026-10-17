#!/usr/bin/env python3
"""apply_review.py on a tiny synthetic chunk: every patch op, a failing
patch, an issue without patch, and the promise that the draft is untouched.

    python3 tests/test_apply_review.py
"""
import hashlib
import json
import subprocess
import sys
import tempfile
from pathlib import Path

TOOLS = Path(__file__).resolve().parent.parent


def unit(n, me_count=1):
    words = [{"w": "me", "gloss": "to me", "gram": "abl. sg."}] * me_count
    return {"n": n, "english": "Thus he said that fifth thing.",
            "hindi": "उसने कहा", "notes": "base",
            "lines": [{"tokens": [{"src": "me", "words": [
                dict(w) for w in words] + [
                {"w": "ca", "gloss": "and", "gram": "ind."}]}]}],
            "text_flags": [{"src": "x", "suggest": "y", "why": "z"}]}


def main():
    with tempfile.TemporaryDirectory() as tmp:
        d = Path(tmp)
        draft = [unit("1"), unit("2", 2)]
        (d / "chunk1_out.json").write_text(json.dumps(draft))
        (d / "chunk1_in.json").write_text(json.dumps([
            {"n": "1", "type": "verse", "lines_deva": ["मे च"]},
            {"n": "2", "type": "prose", "lines_deva": ["मे मे च"]}]))
        review = {"units": [
            {"n": "1", "verdict": "fix", "issues": [
                {"field": "english", "problem": "'Thus' added",
                 "severity": "minor", "fix": "He said that fifth thing.",
                 "patch": {"op": "replace", "field": "english",
                           "old": "Thus he", "new": "He"}},
                {"field": "hindi", "problem": "meaning", "severity": "error",
                 "patch": [{"op": "set", "field": "hindi",
                            "value": "उन्होंने कहा"},
                           {"op": "append_note", "text": "Reviewed."}]},
                {"field": "gram", "problem": "me is never ablative",
                 "severity": "error",
                 "patch": {"op": "word", "match_w": "me", "field": "gram",
                           "value": "gen. sg. pron. (encl.)"}},
                {"field": "text_flags", "problem": "why too thin",
                 "patch": {"op": "set", "field": "text_flags.0.why",
                           "value": "better reason"}},
                {"field": "gloss", "problem": "no such word",
                 "patch": {"op": "word", "match_w": "zzz", "field": "gloss",
                           "value": "q"}},
                {"field": "notes", "problem": "check Cakrapani",
                 "severity": "minor", "fix": "see commentary"}]},
            {"n": "2", "verdict": "fix", "issues": [
                {"field": "gram", "problem": "both me",
                 "patch": {"n": "2", "op": "word", "match_w": "me",
                           "field": "gloss", "value": "of me",
                           "occurrence": "all"}}]}]}
        (d / "chunk1_review.json").write_text(json.dumps(review))
        before = hashlib.sha256(
            (d / "chunk1_out.json").read_bytes()).hexdigest()
        run = subprocess.run(
            [sys.executable, str(TOOLS / "apply_review.py"), str(d),
             "--add-source"], capture_output=True, text=True)
        print(run.stdout)
        errors = []
        if run.returncode != 1:
            errors.append(f"exit code {run.returncode}, expected 1 "
                          "(one patch must fail)")
        if hashlib.sha256((d / "chunk1_out.json").read_bytes()).hexdigest() \
                != before:
            errors.append("the draft was modified")
        final = json.loads((d / "chunk1_final.json").read_text())
        log = json.loads((d / "changes_1.json").read_text())
        u1, u2 = final
        w = u1["lines"][0]["tokens"][0]["words"][0]
        checks = [
            (u1["english"] == "He said that fifth thing.", "replace"),
            (u1["hindi"] == "उन्होंने कहा", "set"),
            (u1["notes"] == "base Reviewed.", "append_note"),
            (w["gram"] == "gen. sg. pron. (encl.)", "word gram"),
            (u1["text_flags"][0]["why"] == "better reason", "dotted set"),
            (all(x["gloss"] == "of me" for x in
                 u2["lines"][0]["tokens"][0]["words"][:2]), "occurrence all"),
            (u1["type"] == "verse" and u2["lines_deva"] == ["मे मे च"],
             "--add-source"),
            (len(log) == 7 and {"n", "field", "old", "new", "why"}
             <= set(log[0]), "log"),
            ("MANUAL unit 1" in run.stdout, "manual item printed"),
            ("FAILED unit 1 word" in run.stdout, "failed patch printed"),
        ]
        for ok, name in checks:
            print(("ok   " if ok else "FAIL ") + name)
            if not ok:
                errors.append(name)
        print("PASS" if not errors else "FAIL: " + "; ".join(errors))
        return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
