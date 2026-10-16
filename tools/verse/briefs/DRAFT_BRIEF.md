# Brief: draft the word split, Hindi and English for one chunk of a Sanskrit text

You are drafting study material for ONE chunk of a Sanskrit text. The reader wants to (1) see dense verses broken into
individual words (sandhi viccheda, plus compound splitting) so they can understand and remember them, and (2) have a faithful
Hindi and English translation, so errors can be spotted. Correctness matters far more than elegance. Do not search the web;
work from the Sanskrit given and your own knowledge of grammar.

## Input: `chunkK_in.json`
A list of unit records, in order. Fields:
- `n` unit number (string). `type` "verse" or "prose". `line_ids` the book's own line numbers for the unit.
- `lines_iast`: the Sanskrit as printed (transliterated to IAST from the Devanagari), one string per printed line. It is a single
  noisy witness (the source was digitised from a poor scan): it contains typos. DO NOT silently fix them.
- `lines_deva`: the same lines in the printed Devanagari (for your reference; you do not write it).
- `book_split`, `book_hindi`, `book_english`: the study text's own layers for the same lines (a proofread word split with sandhi
  resolved, and modern Hindi and English study aids with bracketed glosses). Use them as HINTS, never as authority: they can be wrong,
  and the Hindi/English contain bracketed glosses and Latin letters that must NOT be copied into your output.
- `uncertain`: lines the editors flagged as damaged (with their note). Treat those words as doubtful: keep the printed token, say so in
  `text_flags`/`notes`, lower `confidence`, and never build a firm reading on them.
- A unit is usually one verse of two printed half-verse lines. Sometimes the grouping is wrong (a verse split across two units, or two
  unrelated lines joined): say so in `notes` with the words "GROUPING:" and what the right grouping looks like.

## Output: `chunkK_out.json`
A JSON list, one object per input record, same order, same `n`:
```
{
 "n": "3",
 "lines": [                         // one entry per input line, in order
   { "tokens": [                    // one entry per whitespace-separated token of that input line
       { "src": "athāto",           // EXACTLY the input token, character for character (even if you think it is a typo)
         "words": [                 // the token with sandhi undone, original forms restored; compound members joined by "-"
           {"w":"atha", "gloss":"now", "gram":"ind."},
           {"w":"ataḥ", "gloss":"therefore", "gram":"ind."} ] },
       ... ] } ],
 "hindi":   "...",                  // Hindi (Devanagari) translation of the whole unit, faithful, clear, standard Hindi
 "english": "...",                  // English translation of the whole unit, faithful
 "text_flags": [ {"src":"...", "suggest":"...", "why":"..."} ],   // suspected errors in the Sanskrit as given; [] if none
 "notes": "...",                    // ambiguity, alternative readings, where commentators differ, GROUPING issues; "" if none
 "confidence": "high|medium|low"
}
```
## Rules for the split (sandhi viccheda)
1. Undo sandhi and restore each word to its dictionary-style inflected form ("bharadvāja upāgamat" -> `bharadvājaḥ`, `upāgamat`;
   "athāto" -> `atha`, `ataḥ`; "'sitaḥ" -> `asitaḥ`).
2. Split compounds (samāsa) into members joined by hyphen: `brahma-jñānasya`. For a long compound give every member. Put the compound's
   type in `gram` when it helps ("tat-puruṣa", "dvandva", "bahuvrīhi").
3. IAST throughout, ṃ for anusvāra, ḥ for visarga, ' only for avagraha in `src`.
4. `gloss`: a short English meaning IN THIS CONTEXT (1 to 5 words). `gram`: a short grammatical tag: "m. nom. sg.", "n. acc. sg.", "f. inst. sg.",
   "gen. pl.", "ind.", "3 sg. pf. √gṛh", "abs. √budh", "pres. part. √icch", ... Keep it brief and use these forms. If unsure about case or root,
   say so in `notes` rather than guessing.
5. Every input token must appear in `tokens`, in order. The joined `src` values of a line must equal the input line exactly (the checker
   verifies this). Never merge, drop, reorder or "correct" input tokens.
6. If you believe the input has a typo, keep `src` as given, use the CORRECTED form in `words`, and add an entry to `text_flags` (with `why`).
   Use the metre (16 syllables a half-verse line, or 22 for an upajāti line), the sense, the book's own split and parallels in the chunk as
   evidence. If the typo is only suspected, say "possible" in `why`.
7. Technical medical words: give the plain literal sense in `gloss` (e.g. vāta "wind-humour (vāta)"), never a modern diagnosis. Plant, drug and
   preparation names: keep the name; gloss "drug name" unless the name is transparent; never identify a plant, never state an effect.

## Rules for translation
- Translate what the Sanskrit says; do not import later knowledge, commentary or modern interpretation. Where a word is ambiguous give the
  most literal natural rendering and mention the alternative in `notes`.
- Translate the whole unit as one flowing statement (a verse is often one sentence over two lines). Do not translate word by word. Where the
  sentence continues into the next unit, translate what the unit contains and end naturally.
- Hindi: standard literary Hindi in Devanagari, understandable to a modern reader. NO Latin letters in `hindi` and no bracketed glosses. Keep
  proper names and technical terms in Devanagari (वात, पित्त, कफ, दोष, धातु, रस ...).
- English: plain accurate English. Technical terms may stay in IAST with a short gloss the first time they are needed in the chunk. In English
  prose use IAST for Sanskrit terms (doṣa, vāta).
- Use "the text states" style only in `notes`, never inside a translation. Add nothing the Sanskrit does not say; drop nothing it does.
- Consistent renderings across chunks: āyurveda = Āyurveda (the science of life); ṛṣi = sage; vāta, pitta, kapha = Vāta, Pitta, Kapha;
  doṣa = doṣa; dhātu = dhātu; rasa = taste (of the six tastes) or rasa; vipāka, vīrya, prabhāva: keep the Sanskrit with a gloss; bhiṣak/vaidya =
  physician; proper names transliterated.

## Quality bar
An independent reviewer will check your work word by word, seeing only the Sanskrit and your output. Prefer a plain correct answer over a
clever one. Mark real uncertainty with `confidence` and `notes`.

## Self-check before finishing
Run: `python3 -I <TOOLS>/check_chunk.py chunkK_in.json chunkK_out.json` and fix every ERROR; read the WARNINGs and fix real mistakes.
Reply with: units done, number of text_flags, number of low-confidence units, GROUPING notes, and anything you could not resolve (short).
