# VERIFY log: ashtanga-sangraha

Dated log of the verify stage (`/verify-vedic-book-reference`). Branch `docs/2026-10-17/version-1`. Tools: eckko/claude-memory branch `feat/2026-10-17/verify-vedic-book-reference`.

## 2026-10-17
- Inventory. Owner answers: (1) `reference/md` and `reference/txt` (older digitisation, AI Hindi/English, older proofread Part 1) are ignored; (2) the owner's `-sandhi` twin files are kept as the sandhi layer, not redrafted by AI; (3) layer pilot = Part 5 first.
- Second edition: not used ("second edition: not available, skipped"). The older `reference/txt/ch01.txt` was offered and declined.
- Completeness (structure_check.py): 6 parts, 150 chapters, 21,858 lines; no gaps, no truncated part, toc.md and text/ agree. `check_extraction.py`: 0 errors, 9 warnings (ISSUES.md ocr rows, zero-width characters).
- Word checker: 213 stray rows, 111 typo candidates, 5,519 metre rows (see checks/word_check.md). Compare texts: none.
- AI proofreading: deviation from the default pack: the metre list was cut from 5,519 to the 686 lines at 14 or 18 aksharas (the rest are prose, paired lines or headings in this edition). 1,142 items, 20 packs (60 per pack), 20 agents, all answered. Result: 427 proposals, sample error rate 19/138 = 13.8% on ordinary lines. Proposals only; `text/` unchanged. Not read by a person.
- Layer plan: `plan_work.py --parts 5` -> 26 chunks, 1,005 units, about 0.3 million draft tokens plus the same for review (layers-work/). No layer drafted yet.
- Open point before layers: the toolkit's draft/check/merge/write steps also produce a word split and `write_layers.py` writes `-sandhi.md`, which would overwrite the owner's twin files. The layer step needs a Hindi+English-only variant (or a different output name) before it runs.
