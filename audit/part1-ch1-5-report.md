# Part 1 (Sūtrasthāna) chapters 1-5: proofreading report

Branch `audit/part1-sutrasthana`. Scope: chapters 1-5 only (698 rows). Chapters 6-40 have no Hindi/English
(both layers are copies of the Sanskrit) and were not touched.

## What was done
- Every row of chapters 1-5 was read (Sanskrit, word-split, Hindi, English) by chapter-wise review passes.
- 324 fixes applied to `reference/md/ch01.01-05.md` and the matching lines of `reference/txt/ch01*.txt`
  (kept in sync; row/line alignment re-verified: 5,706 md rows = 5,706 txt lines).
- By kind: ocr 155, split 49, translation 45, typo 37, gloss 35, align 3.
- Every fix is recorded with its reason in `audit/fixes/*.json` (old text, new text, note).

## Not fixed (needs a human with a second source)
About 85 items are listed in `audit/flags/*.md` with a suggested reading and confidence. Mostly garbled
Sanskrit where the correct word is uncertain (for example 1.1.29, 1.4.135, 1.3.201, 1.5.39/42/62).
Medium-confidence changes that were applied but should be re-checked if a second source appears:
1.4.127, 1.5.66, 1.5.85.

## Residual script flags
The remaining `split-diverges` flags in chapters 1-5 are legitimate sandhi resolutions that were reviewed.

## Caveat
No second Sanskrit source exists, so Sanskrit fixes rest on grammar, the word-split line and the
translations. This is cleaned text, not verified against the 1888 print.
