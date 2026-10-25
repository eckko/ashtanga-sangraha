# Book notes: Aṣṭāṅga Saṅgraha, Kalpasthāna (Part 5), quiz chapters 501-508
- Source units: `data/chapter50N_verses.json`, built by grouping the reviewed per-line Hindi/English layer drafts
  (`reference/ashtanga-sangraha/layers-work/p05/chNN/chunk*_final.json`, Sonnet drafts, each independently reviewed and patched)
  into the edition's two-line pairs (build_units.py rule). Line ids are the study text's own (`05.CC.L`).
  `data/part5_layer_unit_map.json` maps every layer line to its quiz unit.
- Notes beginning `OPEN (05.CC.L)` are reviewer observations or proofread proposals that were never resolved: build no
  question on the point they raise.
- OWNER POLICY (overrides the "never identify a plant" line of ashtanga-notes.md for this part): exact translation,
  comprehension first; modern names and plant identifications are used as the unit data gives them, with the data's
  confidence word (standard / probable / disputed / unidentified). Never add an effect, dose or identification the data lacks.
- Fixed renderings: `reference/ashtanga-sangraha/layers-work/GLOSSARY.md` (kaṣāya taste = कसैला, preparation = काढ़ा; kṣāra stays kṣāra; ...).
- Kalpasthāna is largely prose (procedures, drug lists, measures). Prose units stand alone; `order` questions follow the steps
  or the list order of the text; `match` pairs drug -> use, complication -> remedy, as the text states them.
- Card ids: prefix ka1..ka8 (concepts `ka1-001`...). Batch modules: `tools/authored/ka{C}_batch_NN.py`. Sections: `tools/authored/sections_kalpa.py`.
