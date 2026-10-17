# Aṣṭāṅga Saṅgraha: raw extracted source bank

Stage 1 (extraction) of a pipeline: verify, review, fix, proofread come next. This folder holds the raw text, not a finished edition. Nothing here has been proofread.

Each chapter has two line-aligned files: the plain text (`text/chPP.CC.md`) and its sandhi-split twin (`text/chPP.CC-sandhi.md`). 6 parts, 150 chapters, 21,858 lines per version.

Read, in order: FORMAT.md (file and line format, plus the sandhi addition), toc.md (structure), STATUS.md (what is done), sources.md (where text came from), ISSUES.md (known doubts).

Rules for anyone editing here:
- Text lines come only from sources listed in sources.md; never from memory.
- Do not rename files or change line IDs of finished chapters.
- Record every doubt in ISSUES.md; fix text only in a later, explicit proofreading stage.
- Run `python3 reference/tools/check_extraction.py reference/ashtanga-sangraha` before every commit (the local copy treats Latin letters on lines listed as `ocr` in ISSUES.md as warnings).
- Branch pattern: `docs/YYYY-MM-DD/version-N`; push new branches only; the owner merges.

Rebuild from the uploads: `python3 -I tools/build_text.py <uploads dir> .` then `python3 -I tools/gen_docs.py .` (needs the six part files and their sandhi twins named as in tools/build_text.py).

How to continue: open STATUS.md, take the first chapter not marked extracted (none left), then start the proofreading stage; or follow the skill `/extract-vedic-book-web` for translations.
