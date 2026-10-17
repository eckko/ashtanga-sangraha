# Brief: independent review of a drafted chunk (read-only)

You review ONE drafted chunk of a Sanskrit text: the word split, glosses, grammar labels, Hindi and English translations, text flags,
notes and confidence. You did not write it. Be adversarial and concrete: past reviews found real errors in almost every chunk
(unsupported additions in translations, wrong case labels or roots, invented Sanskrit, contested counts used as fact, split words that do
not match the printed text). Do not search the web; work from the Sanskrit and standard grammar.

## Input (read-only)
- `chunkK_in.json` (the Sanskrit as printed in `lines_iast`/`lines_deva`, the book's own layers as hints, `uncertain` lines),
- `chunkK_out.json` (the draft). Do not edit either file.

## What to check, per unit
1. Tokens: every printed token is present and unchanged (the checker already enforces this, but look for tokens whose split makes no
   sense). Each split word is a real Sanskrit word in dictionary-style inflected form; sandhi is undone correctly; compound members are right.
2. `gloss` and `gram`: case, number, gender, tense, root, compound type. Common errors: wrong case label, wrong root, enclitic `me` taken as
   ablative, `-au` assumed dual, kṛdanta forms mislabelled, `-tvā` vs `-ya`.
3. Hindi and English: faithful. Nothing added (interpretation, emphasis, "fifth", "thus ends"), nothing dropped; no Latin letters or bracketed
   glosses in the Hindi; English consistent with the brief's fixed renderings; names and numbers exact.
4. `text_flags` and `notes`: suspected typos are real and the suggestion is right; no invented variants; GROUPING notes are sensible.
5. `confidence` is honest. Lines listed in `uncertain` must not be given a firm reading.

## Output (write `chunkK_review.json`, no other file edits)
```
{"units":[{"n":"3","verdict":"ok|fix","issues":[
  {"field":"english|hindi|notes|gram|gloss|split|text_flags|confidence","where":"word or sentence","problem":"...","fix":"exact replacement text",
   "severity":"error|minor",
   "patch": {"n":"3","op":"set|replace|word|append_note", ...}   // machine-applicable form, see below; omit when it needs a human
  }]}],
 "summary":"..."}
```
`patch` formats: {"n","op":"set","field":"hindi","value":"<full new text>"}; {"n","op":"replace","field":"english","old":"<exact old substring>","new":"..."};
{"n","op":"word","match_w":"<the exact `w` of the word>","field":"gloss|gram|w","value":"..."}; {"n","op":"append_note","text":"..."}.
Give a patch only when you are sure; a `replace` `old` string must occur exactly once in that field. Reply with the counts of issues by severity
and whether you suggest regrouping any unit.
