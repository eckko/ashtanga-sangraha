# Issues: ashtanga-sangraha

Nothing in the text files was changed because of an issue.

| Line ID | Kind | What | Source(s) | Suggested check |
|---|---|---|---|---|
| 01.04.73 (sandhi) | ocr | Latin letters 'otherwise' inside the sandhi line (OCR noise or stray words); kept as in the source | S2 | check against the print edition |
| 03.15.41 (sandhi) | ocr | Latin letters 'resource' inside the sandhi line (OCR noise or stray words); kept as in the source | S2 | check against the print edition |
| 04.02.187 (sandhi) | ocr | Latin letters 'nakh' inside the sandhi line (OCR noise or stray words); kept as in the source | S2 | check against the print edition |
| 04.23.44 (sandhi) | ocr | Latin letters 'ye' inside the sandhi line (OCR noise or stray words); kept as in the source | S2 | check against the print edition |
| 06.02.117 | ocr | Latin letters 'rika' inside the plain line (OCR noise or stray words); kept as in the source | S1 | check against the print edition |
| 06.02.117 (sandhi) | ocr | Latin letters 'rika' inside the sandhi line (OCR noise or stray words); kept as in the source | S2 | check against the print edition |
| 06.08.81 | ocr | Latin letters 'current' inside the plain line (OCR noise or stray words); kept as in the source | S1 | check against the print edition |
| 06.08.81 (sandhi) | ocr | Latin letters 'current' inside the sandhi line (OCR noise or stray words); kept as in the source | S2 | check against the print edition |
| 06.29.12 | ocr | Latin letters 'state' inside the plain line (OCR noise or stray words); kept as in the source | S1 | check against the print edition |
| 06.29.12 (sandhi) | ocr | Latin letters 'state' inside the sandhi line (OCR noise or stray words); kept as in the source | S2 | check against the print edition |
| 06.35.119 | ocr | Latin letters 'alm' inside the plain line (OCR noise or stray words); kept as in the source | S1 | check against the print edition |
| 06.35.119 (sandhi) | ocr | Latin letters 'alm' inside the sandhi line (OCR noise or stray words); kept as in the source | S2 | check against the print edition |
| 06.49.332 | ocr | Latin letters 'Direct' inside the plain line (OCR noise or stray words); kept as in the source | S1 | check against the print edition |
| 06.49.332 (sandhi) | ocr | Latin letters 'Direct' inside the sandhi line (OCR noise or stray words); kept as in the source | S2 | check against the print edition |
| (many) | possible-typo | 351 lines contain non-Devanagari characters other than letters (':' used for visarga, '.', ',', '=', '/', '*', '·', '•', brackets, ZWJ/ZWNJ); kept as in the source. Full list: tools/stray-characters.tsv | S1, S2 | proofread: ':' is probably ः |
| 03.14.50 | other | In the plain Part 3 file one line holds two verse-lines joined by '।' (…बहुव्रणं।शतारुः…). The sandhi file has them as two lines; the two sandhi lines were joined with a space so both files keep identical line IDs. | S1, S2 | split into two lines at the proofreading stage (that adds an ID, so decide then) |
| 01.01 | missing | no chapter-end colophon with a number found in the last 6 lines | S1 | chapter end may be damaged or the chapter boundary may be wrong |
| 01.07 | missing | no chapter-end colophon with a number found in the last 6 lines | S1 | chapter end may be damaged or the chapter boundary may be wrong |
| 01.08 | missing | no chapter-end colophon with a number found in the last 6 lines | S1 | chapter end may be damaged or the chapter boundary may be wrong |
| 01.10 | missing | no chapter-end colophon with a number found in the last 6 lines | S1 | chapter end may be damaged or the chapter boundary may be wrong |
| 01.13 | missing | no chapter-end colophon with a number found in the last 6 lines | S1 | chapter end may be damaged or the chapter boundary may be wrong |
| 01.32 | missing | no chapter-end colophon with a number found in the last 6 lines | S1 | chapter end may be damaged or the chapter boundary may be wrong |
| 01.40 | missing | no chapter-end colophon with a number found in the last 6 lines | S1 | chapter end may be damaged or the chapter boundary may be wrong |
| 02.05 | missing | no chapter-end colophon with a number found in the last 6 lines | S1 | chapter end may be damaged or the chapter boundary may be wrong |
| 03.07 | missing | no chapter-end colophon with a number found in the last 6 lines | S1 | chapter end may be damaged or the chapter boundary may be wrong |
| 03.08 | missing | no chapter-end colophon with a number found in the last 6 lines | S1 | chapter end may be damaged or the chapter boundary may be wrong |
| 03.12 | missing | no chapter-end colophon with a number found in the last 6 lines | S1 | chapter end may be damaged or the chapter boundary may be wrong |
| 04.10 | missing | no chapter-end colophon with a number found in the last 6 lines | S1 | chapter end may be damaged or the chapter boundary may be wrong |
| 04.11 | missing | no chapter-end colophon with a number found in the last 6 lines | S1 | chapter end may be damaged or the chapter boundary may be wrong |
| 04.17 | missing | no chapter-end colophon with a number found in the last 6 lines | S1 | chapter end may be damaged or the chapter boundary may be wrong |
| 06.09 | missing | no chapter-end colophon with a number found in the last 6 lines | S1 | chapter end may be damaged or the chapter boundary may be wrong |
| 06.10 | missing | no chapter-end colophon with a number found in the last 6 lines | S1 | chapter end may be damaged or the chapter boundary may be wrong |
| 06.19 | missing | no chapter-end colophon with a number found in the last 6 lines | S1 | chapter end may be damaged or the chapter boundary may be wrong |
| 06.20 | missing | no chapter-end colophon with a number found in the last 6 lines | S1 | chapter end may be damaged or the chapter boundary may be wrong |
| (all) | variant | 1 lines where the plain line and its sandhi twin look very different (similarity < 0.6 after removing spaces/hyphens): possible misalignment or edits in S2. List: tools/plain-vs-sandhi-low-similarity.tsv | S1, S2 | review the listed lines |
| (all) | count | The source has no verse numbers: IDs count source lines from 1 per chapter. The edition pairs pādas on one line and mixes prose, so a source line is not always a verse; traditional verse counts are unknown here. | S1 | decide the final verse numbering at the verification stage |
| (all) | numbering | 167 trailing numbers like '॥ १ ॥' were removed from the text (verse/chapter numbers in the source) as FORMAT.md requires; they are recorded in tools/stripped-numbers.tsv | S1, S2 | none |
| (toc) | other | structure.md has typos in titles that were copied as they are: 1.8 'अन्नरक्षाविष्यध्यायः' and other 'विष्यध्यायः' (probably विधि…), 4.8 'छर्दित्ह्रद्रोगतृष्णा…', 6.34 'ग्रंथ्यर्बुदश्लीपदापचीनाडीवि०' (cut off), 6.40 starts with a Bengali letter ব in 'বিষप्रतिषेधाध्यायः' | structure.md | fix the titles in toc.md when the owner confirms |
| 01.* (plain) | variant | The repo's older reference/txt/ch01.txt differs from the uploaded Part 1 file in 254 lines (the repo copy looks proofread). This extraction uses the uploaded file as given. | S1 | decide which Part 1 text is the base |
| (checks) | other | Verify stage 2026-10-17: word checker flagged 213 stray/impossible sequences, 111 typo candidates (tier 1 and 2), 5,519 metre lines (not useful here: prose and paired lines). AI proofreading read 1,142 lines (all strays, all typo candidates, 686 metre lines at 14 or 18 aksharas, 138 sample lines): 427 proposals (error or unsure) in checks/proposals.tsv, summary in checks/PROOFREAD.md. Sample error rate 19 of 138 ordinary lines (13.8%, sample size 138). No text was changed. | S1 | check proposals against the printed edition before any correction |
