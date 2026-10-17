# Brief: independent review of authored cards and questions (read-only)

You review a batch of authored units (module `<book>/tools/authored/<module>.py`, built bank at the path you are given). You did not write it.
Check, per unit, against the unit's own data and standard grammar: (1) every card claim (explain_hi, hook, aids, notes, rule, limits); (2) every
aid: diagram/chunks reproduce the verse's words in order, seesaw is a real pair in THIS verse, sandhi rules stated exactly, pegs/puns labelled as the
author's; (3) every picture spec: items and counts match the verse, alt text accurate, labels Devanagari, nothing added beyond the verse, legible
(render with `render_images.py` and look); (4) every question: the keyed answer undeniably right, distractors undeniably wrong from the card alone,
multi answer indexes, match pairs, order items in the verse's order, fill `accept` lists (Devanagari, IAST, plain-letter spellings), stems <=25 words and
one "?", quoted terms defined on the card, no question resting on an `uncertain` line or an ambiguous split, transfer examples valid Sanskrit with
agreeing case/number/gender, mix of kinds follows the owner's preferences (order and match favoured, at most one fill, >=3 kinds, right mcq option not
usually the longest); (5) medical/health wording: only what the verse says, no dose, no effect, no advice.
Output JSON (no file edits): {"units":[{"n","verdict":"ok|fix","issues":[{"field","where":"question id or aid","problem","fix":"exact replacement","severity":"error|minor"}]}],"summary"}.
Reviews found 13 to 18 real problems per 10 units in earlier chapters; be adversarial and concrete.
