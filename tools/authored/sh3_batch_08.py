from helpers import mcq, match, order, fill, multi, accepts


AUTHORED = {}

# ---------------------------------------------------------------- unit 91
AUTHORED["91"] = {
    "title": "कुष्ठलाङ्गलीमुलकल्कंवा",
    "question": "By unit 91, what paste is given, and with which liquid?",
    "rule": ("Another option (वा) in the run of drinks for the aparā (placenta) that does not come out: a paste (kalka) of "
             "kuṣṭha (costus) and the root of lāṅgalī (probably gloriosa lily), with either madya or urine (अन्यतरेण)."),
    "limits": ("Prose, no verb: the data carries पाययेत् (should give to drink) from unit 86. Printed मुल is probably "
               "मूल (flag). Whether the root is of lāṅgalī only or of both is open. Whose urine, and any dose, are not stated."),
    "explain_hi": ("यह गद्य-पंक्ति अपरा (जेर) न गिरने पर पिलाए जाने वाले योगों में एक और विकल्प है (‘वा’ = या)। "
                   "द्रव्य: कुष्ठ और लाङ्गली (सम्भवतः कलिहारी) की जड़ का कल्क, यानी पिसा हुआ गीला लेप। "
                   "इसे मद्य या मूत्र में से किसी एक (अन्यतरेण) के साथ देना है; किस पशु का मूत्र, यह नहीं कहा। "
                   "पंक्ति में क्रिया नहीं है; डेटा के अनुसार ‘पाययेत्’ (पिलाए) इकाई 86 से समझी जाती है। "
                   "‘मूल’ केवल लाङ्गली की जड़ है या दोनों की, यह खुला है।"),
    "hook": "कुष्ठ + लाङ्गली-मूल का कल्क; साथ में मद्य या मूत्र, दोनों में से एक।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 91, with what is the paste of kuṣṭha and lāṅgalī root taken?",
            ("With either madya or urine", "मद्यमूत्रान्यतरेण: with either one of the two, madya or urine."),
            [("With madya and urine mixed", "अन्यतरेण means one of the two, not both together."),
             ("With ghee and with honey", "Neither ghee nor honey is named in unit 91."),
             ("With pleasantly warm water", "Warm water is not named in unit 91.")],
            "The paste goes with one of two liquids: madya or urine.",
            "मद्य-मूत्र-अन्यतरेण = with either madya or urine."),
        order(1, "Put the members of unit 91 in the line's order.",
              ["कुष्ठ", "लाङ्गली", "मूल (छपा मुल)", "कल्क", "मद्य", "मूत्र"],
              "Kuṣṭha, lāṅgalī, root, paste; then the two liquids, madya and urine.",
              "कुष्ठ → लाङ्गली → मूल → कल्क → मद्य → मूत्र."),
        match(2, "Match each word of unit 91 to its meaning.",
              [["कुष्ठ", "costus"], ["लाङ्गली", "probably gloriosa lily"], ["मूल", "root"],
               ["कल्क", "paste"], ["अन्यतरेण", "with either one of two"]],
              "These words name the paste and how it is taken.",
              "कुष्ठ, लाङ्गली, मूल, कल्क, अन्यतर.", role="extend",
              teaches="अन्यतर = one of two: मद्यमूत्रान्यतरेण = with either madya or urine, not both."),
        mcq("discriminate", 3, "Which split of मद्यमूत्रान्यतरेण is right?",
            ("मद्यमूत्र + अन्यतरेण", "अ + अ → आ: मद्यमूत्र + अन्यतरेण = मद्यमूत्रान्यतरेण."),
            [("मद्यमूत्रा + न्यतरेण", "न्यतरेण is not a word; the word is अन्यतरेण."),
             ("मद्यमूत्रः + अन्यतरेण", "अः before अ would give मद्यमूत्रोऽन्यतरेण."),
             ("मद्यमूत्रम् + अन्यतरेण", "A final म् would give मद्यमूत्रमन्यतरेण.")],
            "मद्यमूत्र (madya, urine) + अन्यतरेण (with either one): अ + अ → आ.",
            "अ + अ → आ."),
        multi("apply", 4, "Which statements about unit 91 are right?",
              [("The animal giving the urine is named", "Not named: the data notes the urine is not specified."),
               ("Unit 91 states a dose of the paste", "No dose is printed."),
               ("Only one of the two liquids is used", "Right: अन्यतरेण, with either one."),
               ("Its verb is understood from unit 86", "Right: the data takes पाययेत् as carried from unit 86.")],
              [2, 3],
              "One of two liquids; the verb carried from unit 86; no animal and no dose named.",
              "अन्यतरेण = one of two; verb पाययेत् from unit 86."),
        mcq("transfer", 5, "Built like मद्यमूत्रान्यतरेण, what does a new example दुग्धजलान्यतरेण mean?",
            ("With either milk or water", "X-Y-अन्यतरेण = with one of the two, X or Y."),
            [("With milk and water mixed", "अन्यतर means one of two, not both together."),
             ("With milk boiled in water", "No boiling is said; अन्यतर picks one of two."),
             ("Without milk or water", "अन्यतरेण does not negate; it picks one.")],
            "दुग्ध + जल + अन्यतरेण = with either milk or water, as मद्य + मूत्र + अन्यतरेण.",
            "अन्यतरेण = with either one of the two named.",
            teaches="A dvandva followed by अन्यतर names two choices, of which one is used: दुग्धजलान्यतरेण = with milk or water."),
    ],
}

# ---------------------------------------------------------------- unit 92
AUTHORED["92"] = {
    "title": "वत्सकादिचूर्णं वा मद्येन",
    "question": "By unit 92, what powder is given, and with what?",
    "rule": ("Or the powder (चूर्ण) of the group beginning with vatsaka (probably the kuṭaja seed, Holarrhena), with "
             "madya (an intoxicating drink)."),
    "limits": ("Prose, no verb: the data takes it as carried from unit 86 (पाययेत्). The members of the vatsaka group are "
               "not listed here, and vatsaka = kuṭaja seed is probable only. No dose."),
    "explain_hi": ("अपरा-पातन के पान-योगों का यह अन्तिम विकल्प है: वत्सक आदि का चूर्ण, मद्य के साथ। "
                   "‘वत्सकादि’ = वत्सक से आरम्भ होने वाला द्रव्य-समूह; समूह के बाकी सदस्य यहाँ नहीं गिनाए गए। "
                   "वत्सक को सम्भवतः कुटज का बीज माना गया है (Holarrhena), यह पहचान निश्चित नहीं। "
                   "यहाँ औषध का रूप चूर्ण (सूखा पाउडर) है, इकाई 91 का कल्क (गीला लेप) नहीं। "
                   "क्रिया नहीं छपी; डेटा के अनुसार इकाई 86 से समझी जाती है।"),
    "hook": "वत्सक-आदि का चूर्ण + मद्य।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 92, with what is the vatsakādi powder taken?",
            ("With madya", "मद्येन: with madya, an intoxicating drink."),
            [("With urine", "Urine is an option of unit 91, not unit 92."),
             ("With ghee", "Ghee is not named in unit 92."),
             ("With warm water", "Water is not named in unit 92.")],
            "The powder is taken with madya.",
            "वत्सकादिचूर्णं वा मद्येन."),
        order(1, "Put the words of unit 92 in the line's order.",
              ["वत्सकादिचूर्णम्", "वा", "मद्येन"],
              "The powder of the vatsaka group, or, with madya.",
              "वत्सकादिचूर्णम् → वा → मद्येन."),
        match(2, "Match each word of unit 92 to its meaning.",
              [["वत्सक", "probably kuṭaja seed"], ["आदि", "beginning with"], ["चूर्ण", "powder"],
               ["मद्येन", "with madya"]],
              "Four words make the whole option.",
              "वत्सक, आदि, चूर्ण, मद्य.", role="extend",
              teaches="चूर्ण is a dry powder, a different form from the कल्क (wet paste) of unit 91."),
        mcq("discriminate", 3, "In unit 92, what does वत्सकादि mean?",
            ("The group beginning with vatsaka", "-आदि = beginning with: vatsaka heads a group not listed here."),
            [("Vatsaka alone, finely ground", "-आदि adds the rest of a group; it is not vatsaka alone."),
             ("Vatsaka together with its root", "No root is named; आदि means and the rest."),
             ("Every drug in the list except vatsaka", "-आदि includes vatsaka as the first member.")],
            "वत्सकादि = vatsaka and the rest of its group; the members are not named in this unit.",
            "X-आदि = the group beginning with X."),
        mcq("apply", 4, "Which split of वत्सकादि is right?",
            ("वत्सक + आदि", "अ + आ → आ: वत्सक + आदि = वत्सकादि."),
            [("वत्सका + दि", "दि is not a word; the word is आदि."),
             ("वत्सकः + आदि", "A visarga after अ drops before आ, giving वत्सक आदि."),
             ("वत्सकम् + आदि", "A final म् would give वत्सकमादि.")],
            "वत्सक + आदि: अ + आ → आ.",
            "अ + आ → आ."),
        mcq("transfer", 5, "Built like वत्सकादिचूर्णं वा मद्येन, what does a new example पिप्पल्यादिचूर्णं मधुना mean?",
            ("Powder of the pippalī group, with honey", "पिप्पली + आदि + चूर्णम्, and मधुना = with honey."),
            [("Powder of pippalī alone, with honey", "-आदि adds the rest of a group, not pippalī alone."),
             ("Pippalī with the powder of honey", "मधुना is the instrumental: with honey."),
             ("A paste of the pippalī group, with honey", "चूर्ण is a powder, not a paste (कल्क).")],
            "पिप्पल्यादिचूर्णम् = powder of the group beginning with pippalī; मधुना = with honey.",
            "X-आदि-चूर्णम् = powder of the X group; instrumental = with.",
            teaches="X-आदि-चूर्णम् + an instrumental: the powder of the group beginning with X, taken with that liquid."),
    ],
}

# ---------------------------------------------------------------- unit 93
AUTHORED["93"] = {
    "title": "शतपुष्पाकुष्ठमदनहिङ्गुसिद्धस्यच तैलस्य पिचुं ग्राहयेत्",
    "question": "By unit 93, what is the picu made of, and what is done with it?",
    "rule": ("One should make (her) hold a picu (cotton wad) of oil cooked with śatapuṣpā (probably dill), kuṣṭha (costus), "
             "madana (probably emetic nut) and hiṅgu (asafoetida)."),
    "limits": ("Low confidence. The place where the picu is held is not stated (probably the vagina, not in the text); "
               "soaked is not in the text. Śatapuṣpā = dill and madana = emetic nut are probable only. Printed "
               "सिद्धस्यच = सिद्धस्य च (spacing flag). No dose, no duration."),
    "explain_hi": ("यहाँ से अपरा निकालने के बस्ति और हाथ वाले उपायों का भाग शुरू होता है। "
                   "शतपुष्पा (सम्भवतः सोआ या सौंफ), कुष्ठ, मदन (सम्भवतः मैनफल) और हींग के साथ तेल पकाया जाए; उस तेल का "
                   "पिचु यानी रुई का फाहा पकड़वाना चाहिए। "
                   "‘ग्राहयेत्’ प्रेरणार्थक है: ‘पकड़वाए, धारण कराए’। "
                   "पिचु कहाँ रखा जाए, यह पंक्ति नहीं कहती; ‘भिगोया’ शब्द भी ग्रन्थ में नहीं है। "
                   "‘च’ इस पंक्ति को पिछले विकल्पों से जोड़ता है।"),
    "hook": "चार द्रव्यों में पका तेल → उसका पिचु → धारण कराए।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 93, what should the woman be made to hold?",
            ("A cotton wad of the cooked oil", "तैलस्य पिचुं ग्राहयेत्: a picu of the oil, made to be held."),
            [("A pill made of asafoetida", "Hiṅgu is cooked into the oil; no pill is named."),
             ("A cup of the cooked decoction to drink", "The line speaks of oil and a picu, not a decoction."),
             ("A garland of the four herbs", "No garland is named in unit 93.")],
            "A picu (cotton wad) of the cooked oil is to be held.",
            "तैलस्य पिचुं ग्राहयेत्."),
        order(1, "Put the four substances cooked into the oil of unit 93 in the line's order.",
              ["शतपुष्पा", "कुष्ठ", "मदन", "हिङ्गु"],
              "Śatapuṣpā, kuṣṭha, madana, hiṅgu: then siddhasya, cooked (with them).",
              "शतपुष्पा → कुष्ठ → मदन → हिङ्गु → सिद्धस्य."),
        match(2, "Match each word of unit 93 to its meaning.",
              [["शतपुष्पा", "probably dill"], ["मदन", "probably emetic nut"], ["हिङ्गु", "asafoetida"],
               ["पिचु", "cotton wad"], ["ग्राहयेत्", "should cause to hold"]],
              "The substances, the picu, and the verb.",
              "शतपुष्पा, मदन, हिङ्गु, पिचु, ग्राहयेत्.", role="extend",
              teaches="ग्राहयेत् is a causative optative of √ग्रह्: should cause (her) to hold."),
        mcq("discriminate", 3, "In unit 93, what does सिद्धस्य तैलस्य mean?",
            ("Of oil cooked with them", "सिद्ध = cooked; the four substances are cooked into the oil."),
            [("Of raw oil mixed with them", "सिद्ध says cooked, not raw mixing."),
             ("Of oil pressed from them", "The oil is cooked with them, not pressed from them."),
             ("Of oil soaked overnight", "No soaking or night is in the text.")],
            "-सिद्ध at the end of a list = cooked with those things.",
            "X-सिद्धस्य तैलस्य = of oil cooked with X."),
        multi("apply", 4, "Which statements about unit 93 are right?",
              [("The picu is to be soaked for a night", "No soaking or time is in the text."),
               ("The place where the picu is held is not stated", "Right: the data notes the place is not stated."),
               ("Śatapuṣpā is identified as dill for certain", "Dill is probable only; fennel is also proposed."),
               ("The oil is cooked with śatapuṣpā, kuṣṭha, madana and hiṅgu", "Right: these four are named.")],
              [1, 3],
              "Four named substances; the place of the picu is not stated; śatapuṣpā = dill is only probable.",
              "शतपुष्पा-कुष्ठ-मदन-हिङ्गु-सिद्ध तैल; स्थान अलिखित."),
        mcq("transfer", 5, "Built like ग्राहयेत् (should cause to hold), what does a new example भोजयेत् mean?",
            ("Should feed (cause to eat)", "भोजयेत् is the causative optative of √भुज्, as ग्राहयेत् of √ग्रह्."),
            [("Should eat, by oneself alone", "That would be the plain optative भुञ्जीत, not the causative."),
             ("Has eaten already", "-एत् here is an optative, not a past form."),
             ("Will eat tomorrow", "No future is formed; it is an optative.")],
            "भोजयेत् = should make (someone) eat, like ग्राहयेत् = should make (her) hold.",
            "Causative -अय- + optative -एत् = should cause to ...",
            teaches="A causative stem in -अय- with the optative -एत् means should cause to: ग्राहयेत्, भोजयेत्."),
    ],
}

# ---------------------------------------------------------------- unit 94
AUTHORED["94"] = {
    "title": "ततश्चैनामनुवासनकालेऽनुवासयेत्",
    "question": "By unit 94, what is given next, and when?",
    "rule": ("ततः च: and then, at the time of anuvāsana, one should give her (एनाम्) an anuvāsana (oil enema)."),
    "limits": ("Prose, medium confidence. एनाम् (her) points to the woman of the earlier units; she is not named here. "
               "What the anuvāsana time is, and which oil, are not stated in this unit."),
    "explain_hi": ("पिचु के बाद (ततः = फिर) अगला कदम: अनुवासन के समय उसे अनुवासन, यानी तेल की बस्ति, देनी चाहिए। "
                   "‘एनाम्’ (इसे, उसे) स्त्रीलिंग द्वितीया है; पिछली इकाइयों की स्त्री की ओर संकेत, यहाँ नाम नहीं। "
                   "अनुवासन का समय क्या है और कौन-सा तेल, यह पंक्ति नहीं बताती। "
                   "सन्धि: ततः + च → ततश्च, च + एनाम् → चैनाम् (अ + ए → ऐ), काले + अनुवासयेत् → कालेऽनुवासयेत्।"),
    "hook": "ततः → अनुवासन के समय → अनुवासन।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 94, what is given at the time of anuvāsana?",
            ("An anuvāsana, the oil enema", "अनुवासनकाले अनुवासयेत्: at its time, give an anuvāsana."),
            [("An āsthāpana, a decoction enema", "The verb is अनुवासयेत्, not आस्थापयेत्."),
             ("A picu held in place", "The picu was unit 93; here the verb is अनुवासयेत्."),
             ("A drink of madya with powder", "No drink is named in unit 94.")],
            "Then, at the anuvāsana time, an anuvāsana (oil enema).",
            "अनुवासयेत् = should give an oil enema."),
        order(1, "Put the words of unit 94 in the line's order.",
              ["ततः", "च", "एनाम्", "अनुवासनकाले", "अनुवासयेत्"],
              "And then, her, at the time of anuvāsana, one should give an anuvāsana.",
              "ततः → च → एनाम् → अनुवासनकाले → अनुवासयेत्."),
        match(2, "Match each word of unit 94 to its meaning.",
              [["ततः", "then"], ["एनाम्", "her"], ["अनुवासनकाले", "at the time of anuvāsana"],
               ["अनुवासयेत्", "should give an oil enema"]],
              "Four words carry the whole line.",
              "ततः, एनाम्, अनुवासनकाले, अनुवासयेत्.", role="extend",
              teaches="एनाम् is the feminine accusative singular her; it points back to the woman of the earlier units."),
        mcq("discriminate", 3, "Which split of ततश्चैनाम् is right?",
            ("ततः + च + एनाम्", "Visarga before च → श्; अ + ए → ऐ: ततश्चैनाम्."),
            [("ततः + चै + नाम्", "चै and नाम् are not the words; they are च and एनाम्."),
             ("ततः + च + इनाम्", "अ + इ gives ए: it would read ततश्चेनाम्."),
             ("तत् + च + एनाम्", "त् before च would give तच्च, not तश्च.")],
            "ततः (then) + च (and) + एनाम् (her).",
            "ः + च → श्च; अ + ए → ऐ."),
        mcq("apply", 4, "Why is अनुवासनकाले + अनुवासयेत् written कालेऽनुवासयेत्?",
            ("ए stays, and the next अ drops (ऽ)", "Final ए before अ stays; the अ is dropped and marked by ऽ."),
            [("ए and अ fuse into the vowel ऐ", "ए + अ does not give ऐ; ऐ comes from अ + ए."),
             ("The ऽ marks a dropped visarga here", "No visarga stands here; ऽ marks the dropped अ."),
             ("ए turns into य् before the अ", "य् comes from इ or ई before a vowel, not from ए.")],
            "काले + अनुवासयेत् = कालेऽनुवासयेत्: ए kept, अ elided, ऽ written.",
            "ए + अ → एऽ."),
        mcq("transfer", 5, "By the rule of कालेऽनुवासयेत्, how is वने + अस्ति (it is in the forest) joined?",
            ("वनेऽस्ति", "ए before अ stays and the अ drops: वनेऽस्ति, like कालेऽनुवासयेत्."),
            [("वनास्ति", "आ would come from अ + अ; here the first word ends in ए."),
             ("वनैस्ति", "ऐ comes from अ + ए, not from ए + अ."),
             ("वन्यस्ति", "य् comes from इ or ई before a vowel.")],
            "वने + अस्ति = वनेऽस्ति, as काले + अनुवासयेत् = कालेऽनुवासयेत्.",
            "ए + अ → एऽ.",
            teaches="A final ए before अ stays and the अ is dropped, marked ऽ: काले + अनुवासयेत् → कालेऽनुवासयेत्."),
    ],
}

# ---------------------------------------------------------------- unit 95
AUTHORED["95"] = {
    "title": "बिल्वबिल्वजयूषाद्याप्लवनैश्च",
    "question": "By unit 95, with which dips is something done here?",
    "rule": ("And with the dips (āplavana) beginning with bilva, bilvaja and yūṣa (soup). The same dips were named in "
             "unit 88."),
    "limits": ("Prose, no verb. The data says it seems to go with the āsthāpana of unit 96 or the anuvāsana of unit 94; "
               "which is left open. Bilvaja is unclear (see unit 86). No question on either point."),
    "explain_hi": ("यह पंक्ति केवल एक तृतीया वाक्यांश है: ‘और बिल्व, बिल्वज, यूष आदि आप्लवनों से’। "
                   "इसकी अपनी क्रिया नहीं है; डेटा के अनुसार यह इकाई 96 के आस्थापन से जुड़ती लगती है, या इकाई 94 के अनुवासन से — तय नहीं। "
                   "यही आप्लवन इकाई 88 में भी आए थे (गधे या बैल के कान वाले योग में)। "
                   "बिल्वज का अर्थ अस्पष्ट है। "
                   "‘आदि’ से समूह के बाकी आप्लवन खुले छोड़े गए हैं।"),
    "hook": "बिल्व, बिल्वज, यूष … आप्लवनों से (क्रिया आगे या पीछे)।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 95, which items head the list of dips?",
            ("Bilva, bilvaja and yūṣa", "बिल्वबिल्वजयूषादि: beginning with bilva, bilvaja and yūṣa."),
            [("Kuṣṭha, lāṅgalī and madya", "These are from unit 91, not the dips."),
             ("Milk, ghee and honey", "None of these is named in unit 95."),
             ("Śigru, marica and ajājī", "These come in unit 99.")],
            "The dips begin with bilva, bilvaja and yūṣa (soup).",
            "बिल्व-बिल्वज-यूष-आदि-आप्लवनैः."),
        order(1, "Put the members of unit 95 in the line's order.",
              ["बिल्व", "बिल्वज", "यूष", "आदि", "आप्लवनैः", "च"],
              "Bilva, bilvaja, yūṣa, and the rest: with the dips, and.",
              "बिल्व → बिल्वज → यूष → आदि → आप्लवनैः → च."),
        match(2, "Match each word of unit 95 to its meaning.",
              [["यूष", "soup"], ["आदि", "beginning with"], ["आप्लवन", "dip"], ["च", "and"]],
              "The sure words of the line.",
              "यूष, आदि, आप्लवन, च.", role="extend",
              teaches="आप्लवनैः is the instrumental plural: with the dips."),
        mcq("discriminate", 3, "Which split of यूषाद्याप्लवनैः is right?",
            ("यूष + आदि + आप्लवनैः", "अ + आ → आ (यूषादि); इ + आ → या (आद्याप्लवनैः)."),
            [("यूष + आदि + प्लवनैः", "इ before प stays: it would read यूषादिप्लवनैः."),
             ("यूष + आदे + आप्लवनैः", "ए before आ does not give या."),
             ("यूषा + द्या + प्लवनैः", "द्या and प्लवनैः are not the words here.")],
            "यूष (soup) + आदि (beginning with) + आप्लवनैः (with the dips).",
            "अ + आ → आ; इ + आ → या."),
        mcq("apply", 4, "Why is आप्लवनैः written आप्लवनैश् before च?",
            ("A visarga becomes श् before च", "ः + च → श्च: आप्लवनैः + च = आप्लवनैश्च."),
            [("A visarga becomes र् before च", "र् comes before a voiced sound, not before च."),
             ("A visarga drops before च", "It is not dropped; it becomes श्."),
             ("A visarga becomes स् before च", "स् comes before त or थ, not before च.")],
            "Before च or छ a visarga becomes श्.",
            "ः + च → श्च."),
        mcq("transfer", 5, "By the rule of आप्लवनैश्च, how is रामः + च (and Rāma) joined?",
            ("रामश्च", "A visarga before च becomes श्: रामश्च, like आप्लवनैश्च."),
            [("रामो च", "ओ comes before a voiced sound; च is not voiced."),
             ("रामर्च", "र् is not used after अ, and not before च."),
             ("रामस्च", "स् comes before त or थ, not before च.")],
            "रामः + च = रामश्च, as आप्लवनैः + च = आप्लवनैश्च.",
            "ः + च → श्च.",
            teaches="A visarga before च becomes श्: आप्लवनैः + च → आप्लवनैश्च."),
    ],
}

# ---------------------------------------------------------------- unit 96
AUTHORED["96"] = {
    "title": "फलजीमूतकेक्ष्वाकु… आस्थापयेत्",
    "question": "By unit 96, what enema is given, and with what is the liquid furnished?",
    "rule": ("One should give an āsthāpana (decoction enema) with (liquids) furnished with phala, jīmūtaka (probably a "
             "Luffa gourd), ikṣvāku (probably bitter bottle gourd), dhāmārgava (disputed), kuṭaja, an unclear ākai, "
             "kṛtavedhana (probably ridge gourd) and hastiparṇī (unidentified)."),
    "limits": ("Low confidence. ākai is unclear (perhaps a damaged arka, only a guess); hastiparṇī is unidentified; "
               "dhāmārgava is disputed; phala is not firmly identified. The liquids themselves are not stated. No "
               "question rests on these. The data says the unit seems to continue from unit 95."),
    "explain_hi": ("यह आस्थापन (काढ़े की बस्ति) का विधान है: फल, जीमूतक (सम्भवतः देवदाली), इक्ष्वाकु (सम्भवतः कड़वी लौकी), "
                   "धामार्गव (पहचान विवादित), कुटज (मानक: Holarrhena), अस्पष्ट ‘आकै’, कृतवेधन (सम्भवतः तोरई) और हस्तिपर्णी "
                   "(अज्ञात) से युक्त किए हुए (द्रवों) से आस्थापन दे। "
                   "कौन-से द्रव युक्त किए जाएँ, नहीं कहा; डेटा के अनुसार इकाई 95 के आप्लवन इससे जुड़ते लगते हैं। "
                   "‘फल’ की पहचान निश्चित नहीं। "
                   "कई नाम लौकी-तोरई जैसी बेलों के हैं, पर पहचान में विद्वानों में मतभेद है।"),
    "hook": "फल, जीमूतक, इक्ष्वाकु, धामार्गव, कुटज … → आस्थापन।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 96, what kind of enema is given?",
            ("An āsthāpana, a decoction enema", "आस्थापयेत्: should give an āsthāpana."),
            [("An anuvāsana, an oil enema", "The verb here is आस्थापयेत्, not अनुवासयेत्."),
             ("An uttarabasti, an injection", "The uttarabasti comes in unit 98."),
             ("A picu, a wad of cotton to be held", "The picu was unit 93.")],
            "The line ends उपहितैरास्थापयेत्: an āsthāpana with the furnished liquids.",
            "आस्थापयेत् = should give an āsthāpana."),
        order(1, "Put the first five names of unit 96 in the line's order.",
              ["फल", "जीमूतक", "इक्ष्वाकु", "धामार्गव", "कुटज"],
              "Phala, jīmūtaka, ikṣvāku, dhāmārgava, kuṭaja; then the unclear part.",
              "फल → जीमूतक → इक्ष्वाकु → धामार्गव → कुटज."),
        match(2, "Match each name of unit 96 to the identification its data gives.",
              [["जीमूतक", "Luffa echinata, probable"], ["इक्ष्वाकु", "bitter bottle gourd, probable"],
               ["कुटज", "Holarrhena, standard"], ["कृतवेधन", "ridge gourd, probable"], ["उपहित", "furnished with"]],
              "Each name keeps the data's label.",
              "जीमूतक, इक्ष्वाकु, कुटज, कृतवेधन; उपहित.", role="extend",
              teaches="उपहितैः = furnished with (instrumental plural): the liquids are furnished with the listed drugs."),
        mcq("discriminate", 3, "Which split of हस्तिपर्ण्युपहितैः is right?",
            ("हस्तिपर्णी + उपहितैः", "ई + उ → यु: हस्तिपर्णी + उपहितैः = हस्तिपर्ण्युपहितैः."),
            [("हस्तिपर्ण्यु + पहितैः", "पहितैः is not a word; the word is उपहितैः."),
             ("हस्तिपर्णे + उपहितैः", "ए before उ does not give यु."),
             ("हस्तिपर्णी + अपहितैः", "ई + अ would give य: हस्तिपर्ण्यपहितैः.")],
            "हस्तिपर्णी + उपहितैः: ई before a different vowel becomes य्.",
            "ई + उ → यु."),
        mcq("apply", 4, "Why is उपहितैः written उपहितैर् before आस्थापयेत्?",
            ("After ऐ a visarga becomes र्", "After a vowel other than अ/आ, a visarga becomes र् before a vowel."),
            [("After ऐ a visarga becomes ओ", "ओ comes only from अः before a voiced sound."),
             ("After ऐ a visarga is dropped", "Dropping happens after आ, not after ऐ."),
             ("After ऐ a visarga becomes स्", "स् comes before त or थ, not before a vowel.")],
            "उपहितैः + आस्थापयेत् = उपहितैरास्थापयेत्.",
            "Vowel other than अ/आ + ः before a vowel → र्."),
        mcq("transfer", 5, "By the rule of उपहितैरास्थापयेत्, how is गुरुः + आगच्छति (the teacher comes) joined?",
            ("गुरुरागच्छति", "After उ a visarga becomes र् before a vowel, as उपहितैः + आस्थापयेत्."),
            [("गुरु आगच्छति", "The visarga drops after आ, not after उ."),
             ("गुर्वागच्छति", "उ becomes व् only when no visarga stands after it."),
             ("गुरुशागच्छति", "श् comes before च, छ or श, not before a vowel.")],
            "गुरुः + आगच्छति = गुरुरागच्छति.",
            "Vowel other than अ/आ + ः before a vowel → र्.",
            teaches="After a vowel other than अ or आ, a visarga becomes र् before a vowel: उपहितैः + आस्थापयेत् → उपहितैरास्थापयेत्."),
    ],
}

# ---------------------------------------------------------------- unit 97
AUTHORED["97"] = {
    "title": "सिद्धार्थककुष्ठलाङ्गली… विमर्दयेत्",
    "question": "By unit 97, what is pounded, and in what is it crushed?",
    "rule": ("With (a liquid) mixed with siddhārthaka (probably white mustard), kuṣṭha, lāṅgalī and the milky sap of "
             "mahāvṛkṣa (disputed), or with surā-maṇḍa; having pounded the stalks of śālmalī (silk-cotton tree), one "
             "should crush (them) in a decoction of the five roots (pañcamūla)."),
    "limits": ("Low confidence; the sentence is elliptical and its syntax uncertain: the noun of the first phrase is not "
               "stated, स्त्रिञ्चानि is unclear and the वा joining it is a guess. Which pañcamūla is not stated. "
               "Mahāvṛkṣa is disputed. No question on these points."),
    "explain_hi": ("यह कठिन, अधूरा-सा वाक्य है। पहला अंश: सिद्धार्थक (सफेद सरसों, पहचान सम्भावित), कुष्ठ, लाङ्गली और महावृक्ष "
                   "(पहचान विवादित) के क्षीर से मिले हुए (किसी द्रव) से, या सुरामण्ड से। "
                   "निश्चित अंश: शाल्मली के डण्ठलों को कूटकर (आपोथ्य) पञ्चमूल के काढ़े में मसलना (विमर्दयेत्) चाहिए। "
                   "‘स्त्रिञ्चानि’ अस्पष्ट शब्द है; उसे ‘वा’ से डण्ठलों के साथ जोड़ना अनुमान है। "
                   "पञ्चमूल बड़ा है या छोटा, नहीं कहा। डेटा के अनुसार यह इकाई 96 के बस्ति-योगों का ही आगे का भाग लगता है।"),
    "hook": "शाल्मली-डण्ठल कूटो → पञ्चमूल-काढ़े में मसलो।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 97, in what are the pounded stalks crushed?",
            ("In a pañcamūla decoction", "पञ्चमूलकषाये विमर्दयेत्: crush in a pañcamūla decoction."),
            [("In a cup of cow's urine", "Cow's urine is not named in unit 97."),
             ("In pleasantly warm water", "Water is not named in unit 97."),
             ("In a little melted ghee", "Ghee is not named in unit 97.")],
            "The stalks, pounded, are crushed in a decoction of the five roots.",
            "पञ्चमूलकषाये विमर्दयेत्."),
        order(1, "Put these words of unit 97 in the line's order (the unclear word is left out).",
              ["सिद्धार्थककुष्ठलाङ्गलीमहावृक्षक्षीरमिश्रेण", "सुरामण्डेन", "शाल्मलीवृन्तानि", "आपोथ्य",
               "पञ्चमूलकषाये", "विमर्दयेत्"],
              "The mixed liquid, or surā-maṇḍa; the śālmalī stalks, pounded, crushed in the pañcamūla decoction.",
              "…मिश्रेण → सुरामण्डेन → शाल्मलीवृन्तानि → आपोथ्य → पञ्चमूलकषाये → विमर्दयेत्."),
        match(2, "Match each word of unit 97 to its meaning.",
              [["सिद्धार्थक", "white mustard, probable"], ["शाल्मली", "silk-cotton tree"], ["वृन्त", "stalk"],
               ["आपोथ्य", "having pounded"], ["विमर्दयेत्", "should crush, rub"]],
              "The sure words of the procedure.",
              "सिद्धार्थक, शाल्मली, वृन्त, आपोथ्य, विमर्दयेत्.", role="extend",
              teaches="आपोथ्य is an absolutive: having pounded, done before the main verb विमर्दयेत्."),
        mcq("discriminate", 3, "Why does आपोथ्य end in -य and not in -त्वा?",
            ("A prefixed root takes -य", "With a prefix (आ-) the absolutive ends in -य, not -त्वा."),
            [("-य marks a future form", "आपोथ्य is an absolutive, not a future."),
             ("-य marks an optative verb", "The optative of this sentence is विमर्दयेत्."),
             ("-य marks a past participle", "A past participle ends in -त or -न, not -य.")],
            "आ + √पुथ् with a prefix → आपोथ्य, having pounded.",
            "Absolutive: -त्वा without a prefix, -य with a prefix."),
        mcq("apply", 4, "By unit 97, which pañcamūla (group of five roots) is meant?",
            ("Not stated in the text", "The data notes: greater or lesser five roots, not stated."),
            [("The greater five roots", "Not stated; the text only says pañcamūla."),
             ("The lesser five roots", "Not stated; the text only says pañcamūla."),
             ("Both groups, ten roots", "Ten roots are not named in unit 97.")],
            "The unit says only पञ्चमूल; which group is left open.",
            "पञ्चमूल = a group of five roots; here unspecified."),
        mcq("transfer", 5, "Built like आपोथ्य (आ + √पुथ्), which form means having brought, from आ + √नी?",
            ("आनीय", "With the prefix आ-, the absolutive takes -य: आनीय."),
            [("आनीत्वा", "-त्वा is not used with a prefixed root."),
             ("आनयति", "आनयति is a present tense: he brings."),
             ("आनीतः", "आनीतः is a past participle: brought.")],
            "आ + √नी + य = आनीय, like आ + √पुथ् → आपोथ्य.",
            "Prefix + root → absolutive in -य.",
            teaches="A root with a prefix forms its absolutive in -य: आपोथ्य, आनीय; without a prefix in -त्वा."),
    ],
}

# ---------------------------------------------------------------- unit 98
AUTHORED["98"] = {
    "title": "तेन च पूतेन … उत्तरबस्तिं दद्यात्",
    "question": "By unit 98, with what oil is the uttarabasti given?",
    "rule": ("With that, strained (पूत), oily, joined with phala and the rest, with kaṭutaila (pungent oil, probably "
             "mustard oil) cooked with the āsthāpana substances as stated, one should give an uttarabasti."),
    "limits": ("Low confidence. The adjectives may all describe the kaṭutaila or a separate liquid; the grammar allows "
               "both. Whether the uttarabasti goes through the urethra or the female passage is not stated. "
               "Kaṭutaila = mustard oil is probable. No question on these points."),
    "explain_hi": ("यह उत्तरबस्ति का विधान है: कटु तेल (सम्भवतः सरसों का तेल), जो यथोक्त आस्थापन-द्रव्यों से पकाया गया है, उससे उत्तरबस्ति दे। "
                   "बीच के विशेषण — छाना हुआ (पूत), स्नेह वाला, फल आदि से युक्त — कटु तेल के हैं या किसी अलग द्रव के, व्याकरण दोनों मानता है। "
                   "उत्तरबस्ति मूत्रमार्ग या स्त्री-मार्ग से दी जाने वाली बस्ति का मानक नाम है; यहाँ कौन-सा मार्ग, नहीं कहा। "
                   "‘यथोक्त’ = जैसा कहा गया; यानी इकाई 96 जैसे आस्थापन-द्रव्य।"),
    "hook": "आस्थापन-द्रव्यों में पका कटु तेल → उत्तरबस्ति।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 98, what is given with the cooked kaṭutaila?",
            ("An uttarabasti", "कटुतैलेनोत्तरबस्तिं दद्यात्: give an uttarabasti with the oil."),
            [("An āsthāpana", "The āsthāpana substances cook the oil; the act here is उत्तरबस्ति."),
             ("A nasal drop (nasya)", "No nasal drop is named in unit 98."),
             ("A cotton picu", "The picu was unit 93.")],
            "With the kaṭutaila, an uttarabasti is given.",
            "उत्तरबस्तिं दद्यात्."),
        order(1, "Put these words of unit 98 in the line's order.",
              ["तेन", "पूतेन", "स्नेहवता", "फलादियुक्तेन", "यथोक्तास्थापनद्रव्यसिद्धेन", "कटुतैलेन"],
              "With that, strained, oily, joined with phala and the rest, cooked with the stated āsthāpana substances, "
              "with kaṭutaila; then उत्तरबस्तिं दद्यात्.",
              "तेन → पूतेन → स्नेहवता → फलादियुक्तेन → …सिद्धेन → कटुतैलेन."),
        match(2, "Match each word of unit 98 to its meaning.",
              [["पूत", "strained"], ["स्नेहवत्", "having oil"], ["यथोक्त", "as stated"],
               ["कटुतैल", "pungent oil, probably mustard"], ["उत्तरबस्ति", "urethral or uterine injection"]],
              "The words that describe the oil and the act.",
              "पूत, स्नेहवत्, यथोक्त, कटुतैल, उत्तरबस्ति.", role="extend",
              teaches="यथोक्त = यथा + उक्त, as stated: the āsthāpana substances already named."),
        mcq("discriminate", 3, "Which split of कटुतैलेनोत्तरबस्तिम् is right?",
            ("कटुतैलेन + उत्तरबस्तिम्", "अ + उ → ओ: कटुतैलेन + उत्तरबस्तिम् = कटुतैलेनोत्तरबस्तिम्."),
            [("कटुतैलेनः + उत्तरबस्तिम्", "अः before उ drops the visarga, leaving कटुतैलेन उत्तर…"),
             ("कटुतैलेनो + उत्तरबस्तिम्", "ओ before उ would give अवु, not ओ."),
             ("कटुतैले + नोत्तरबस्तिम्", "नोत्तरबस्तिम् is not a word.")],
            "कटुतैलेन (with pungent oil) + उत्तरबस्तिम् (uttarabasti): अ + उ → ओ.",
            "अ + उ → ओ."),
        mcq("apply", 4, "By unit 98, through which passage is the uttarabasti given?",
            ("Not stated in the text", "The data: urethra or female passage, not stated here."),
            [("Through the urethra", "Possible in general, but not stated in unit 98."),
             ("Through the female passage", "Possible in general, but not stated in unit 98."),
             ("Through the rectum", "The rectal enemas are āsthāpana and anuvāsana.")],
            "Uttarabasti is the term for both routes; unit 98 does not say which.",
            "उत्तरबस्ति = urethral or uterine injection; route not stated here."),
        mcq("transfer", 5, "By the rule of यथोक्त (यथा + उक्त), how is सूर्य + उदयः (sunrise) joined?",
            ("सूर्योदयः", "अ + उ → ओ, as यथा + उक्त → यथोक्त."),
            [("सूर्यौदयः", "औ comes from अ + ओ or औ, not from अ + उ."),
             ("सूर्युदयः", "The अ does not vanish before उ."),
             ("सूर्यवुदयः", "अव् comes from ओ before a vowel, not from अ.")],
            "सूर्य + उदयः = सूर्योदयः.",
            "अ/आ + उ → ओ.",
            teaches="अ or आ before उ gives ओ: यथा + उक्त → यथोक्त, कटुतैलेन + उत्तरबस्तिम् → कटुतैलेनोत्तरबस्तिम्."),
    ],
}

# ---------------------------------------------------------------- unit 99
AUTHORED["99"] = {
    "title": "शिग्रुसुमुखमरिचाजाजिचित्रक… अनुवासयेत्",
    "question": "By unit 99, with what cooked oil is the anuvāsana given?",
    "rule": ("Or one should give an anuvāsana (oil enema) with kaṭutaila (probably mustard oil) cooked with the paste of "
             "śigru (drumstick), sumukha (probably a basil), marica (black pepper), ajājī (probably cumin) and citraka, "
             "with milk and with cow's urine."),
    "limits": ("Prose. The data takes the paste as of the first five drugs, then milk and cow's urine; no question on "
               "that parse. Sumukha, ajājī and kaṭutaila are probable identifications. The printed ना ऽ in "
               "कटुतैलेनाऽनुवासयेत् is the print's habit for अ + अ. No dose."),
    "explain_hi": ("यह अनुवासन का दूसरा विकल्प है: शिग्रु (सहजन), सुमुख (सम्भवतः एक तुलसी), मरिच (काली मिर्च), "
                   "अजाजी (सम्भवतः जीरा) और चित्रक (चीता) के कल्क, दूध और गोमूत्र से पकाए हुए कटु तेल "
                   "(सम्भवतः सरसों का तेल) से अनुवासन दे। "
                   "डेटा यह विभाग मानता है: कल्क पहले पाँच का, फिर दूध और गोमूत्र। "
                   "‘कटुतैलेनाऽनुवासयेत्’ में ‘ऽ’ छपाई की आदत है: कटुतैलेन + अनुवासयेत् (अ + अ → आ)। "
                   "पिछली इकाई में यही कटु तेल उत्तरबस्ति के लिए था; यहाँ अनुवासन के लिए।"),
    "hook": "सहजन, सुमुख, मरिच, अजाजी, चित्रक + दूध + गोमूत्र → कटु तेल → अनुवासन।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 99, which enema is given with the cooked kaṭutaila?",
            ("An anuvāsana, an oil enema", "कटुतैलेनाऽनुवासयेत्: give an anuvāsana with the oil."),
            [("An uttarabasti, an injection", "The uttarabasti is unit 98; here the verb is अनुवासयेत्."),
             ("An āsthāpana, a decoction one", "The āsthāpana was unit 96."),
             ("A picu of the oil to hold", "The picu was unit 93.")],
            "The oil of unit 99 is given as an anuvāsana.",
            "अनुवासयेत् = should give an oil enema."),
        order(1, "Put the five drugs of the paste in unit 99 in the line's order.",
              ["शिग्रु", "सुमुख", "मरिच", "अजाजी", "चित्रक"],
              "Śigru, sumukha, marica, ajājī, citraka; then paste, milk, cow's urine.",
              "शिग्रु → सुमुख → मरिच → अजाजी → चित्रक."),
        match(2, "Match each word of unit 99 to the meaning its data gives.",
              [["शिग्रु", "drumstick tree, standard"], ["मरिच", "black pepper"], ["अजाजी", "cumin, probable"],
               ["कल्क", "paste"], ["गोमूत्र", "cow's urine"]],
              "Each identification keeps the data's label.",
              "शिग्रु, मरिच, अजाजी, कल्क, गोमूत्र.", role="extend",
              teaches="-सिद्धेन at the end of the list: (the oil) cooked with all these."),
        multi("discriminate", 3, "Which of these are cooked into the oil of unit 99?",
              [("हिङ्गु (asafoetida)", "Hiṅgu belongs to the oil of unit 93."),
               ("शिग्रु (drumstick)", "Right: the first of the list."),
               ("लाङ्गली (probably gloriosa lily)", "Lāṅgalī is in units 91 and 97, not unit 99."),
               ("मरिच (black pepper)", "Right: the third of the list."),
               ("गोमूत्र (cow's urine)", "Right: named with milk at the end of the list.")],
              [1, 3, 4],
              "Śigru, marica and cow's urine are in the list; hiṅgu and lāṅgalī are not.",
              "शिग्रु-सुमुख-मरिच-अजाजी-चित्रक-कल्क-क्षीर-गोमूत्र-सिद्ध."),
        mcq("apply", 4, "What does the data of unit 99 say kaṭutaila is?",
            ("Pungent oil, probably mustard", "Literally pungent oil; mustard oil is probable."),
            [("Certainly sesame oil", "The data says probably mustard oil, not sesame."),
             ("Certainly mustard oil, as printed", "The print says only pungent oil; mustard is probable."),
             ("An oil pressed from pepper", "Marica is cooked in; the oil is kaṭutaila.")],
            "कटुतैल = pungent oil; the identification as mustard oil is probable.",
            "कटुतैल: probably mustard oil."),
        mcq("transfer", 5, "Built like शिग्रु…सिद्धेन कटुतैलेन, what does a new example मरिचहिङ्गुसिद्धेन घृतेन mean?",
            ("With ghee cooked with marica and hiṅgu", "X-Y-सिद्धेन घृतेन = with ghee cooked with X and Y."),
            [("With marica and hiṅgu fried in oil", "घृतेन is ghee; the drugs are cooked into it."),
             ("With raw ghee and some marica", "सिद्ध says cooked, not raw."),
             ("With hiṅgu that was cooked in marica juice", "Marica and hiṅgu are a pair (dvandva).")],
            "मरिच + हिङ्गु + सिद्धेन घृतेन = with ghee cooked with black pepper and asafoetida.",
            "A dvandva + सिद्धेन = cooked with those items.",
            teaches="A dvandva list ending in -सिद्ध describes a fat cooked with those items: मरिचहिङ्गुसिद्धेन घृतेन."),
    ],
}

# ---------------------------------------------------------------- unit 100
AUTHORED["100"] = {
    "title": "उमाशाल्मलीपिच्छया वा",
    "question": "By unit 100, what two hand-and-filling measures are given?",
    "rule": ("Either fill the yoni (female genital passage) with picchā of umā (probably flax) and śālmalī, with ghee, and "
             "shake; or, with an oiled hand whose nails are cut, remove, following the mālā (sense unclear)."),
    "limits": ("Two printed lines joined; low confidence. Picchā = gum of śālmalī and umā = flax are probable. The objects "
               "of shake and remove are not stated, and the sense of mālā is unclear: no question on them. The data "
               "marks the unit verse, but the lines read as prose instructions."),
    "explain_hi": ("दो विकल्प (‘वा … वा’) हैं। पहला: घी सहित उमा (सम्भवतः अलसी) और शाल्मली की पिच्छा "
                   "(सम्भवतः सेमल का गोंद) से योनि भरकर हिलाए। "
                   "दूसरा: स्निग्ध (तेल लगे), कटे नाखून वाले हाथ से ‘माला के अनुसार’ हटाए; ‘माला’ का अर्थ यहाँ अस्पष्ट है। "
                   "क्या हिलाना और क्या हटाना, यह पंक्ति नहीं कहती; यह भाग अपरा निकालने के उपायों में आता है। "
                   "‘कृत्तनख’ बहुव्रीहि है: जिसके नाखून कटे हों (वह हाथ)।"),
    "hook": "पिच्छा से भरो-हिलाओ, या तेल लगे, कटे-नाखून हाथ से हटाओ।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 100, with what is the yoni filled in the first option?",
            ("Umā-śālmalī picchā with ghee", "उमाशाल्मलीपिच्छया … सघृतया: picchā with ghee."),
            [("Kaṭutaila cooked with several drugs", "Kaṭutaila belongs to units 98 and 99."),
             ("A decoction of five roots", "The pañcamūla decoction was unit 97."),
             ("Cow's urine with milk", "Urine and milk were unit 99.")],
            "The filling is the picchā of umā and śālmalī, together with ghee.",
            "उमाशाल्मलीपिच्छया सघृतया योनिं पूरयित्वा."),
        order(1, "Put the phrases of unit 100 in the text's order.",
              ["उमाशाल्मलीपिच्छया वा सघृतया", "योनिं पूरयित्वा", "विधुनुयात्",
               "स्निग्धेन वा कृत्तनखेन पाणिना", "मालानुसारतोऽपहरेत्"],
              "Fill with the picchā and ghee, then shake; or with the oiled, nail-cut hand, remove.",
              "पिच्छा → पूरयित्वा → विधुनुयात् → पाणिना → अपहरेत्."),
        match(2, "Match each word of unit 100 to its meaning.",
              [["सघृत", "with ghee"], ["पूरयित्वा", "having filled"], ["विधुनुयात्", "should shake"],
               ["स्निग्ध", "oiled"], ["अपहरेत्", "should remove"]],
              "The sure words of both options.",
              "सघृत, पूरयित्वा, विधुनुयात्, स्निग्ध, अपहरेत्.", role="extend",
              teaches="पूरयित्वा is an absolutive (having filled): it comes before the main verb विधुनुयात्."),
        mcq("discriminate", 3, "In कृत्तनखेन पाणिना, what does कृत्तनख mean?",
            ("Whose nails are cut (the hand)", "A bahuvrīhi: it describes the hand, whose nails are cut."),
            [("The nails that cut the hand", "The nails are the ones cut, not the cutters."),
             ("A hand and the cut nails", "It is not a dvandva of two things."),
             ("Cutting that is done by the nails", "कृत्त is a past participle, cut.")],
            "कृत्त (cut) + नख (nail), describing पाणिना: with a hand whose nails are cut.",
            "बहुव्रीहि: कृत्तनख = whose nails are cut."),
        mcq("apply", 4, "By unit 100, what two things are said of the hand used for removing?",
            ("It is oiled, and its nails are cut", "स्निग्धेन … कृत्तनखेन पाणिना."),
            [("It is washed, and it is warm", "Neither washing nor warmth is named."),
             ("It is oiled, and it is wound with hair", "No hair is named in unit 100."),
             ("It holds a picu of cooked oil", "No picu is named in unit 100.")],
            "The hand is snigdha (oiled) and kṛtta-nakha (with nails cut).",
            "स्निग्धेन कृत्तनखेन पाणिना."),
        mcq("transfer", 5, "By the rule of मालानुसारतोऽपहरेत्, how is रामः + अपि (Rāma too) joined?",
            ("रामोऽपि", "अः before अ → ओ, and the अ drops (ऽ), as अनुसारतः + अपहरेत्."),
            [("रामापि", "Dropping the visarga to give आ is wrong after short अ."),
             ("रामरपि", "र् is used after vowels other than अ/आ."),
             ("राम अपि", "Before अ the visarga does not just drop; it gives ओऽ.")],
            "रामः + अपि = रामोऽपि, as मालानुसारतः + अपहरेत् = मालानुसारतोऽपहरेत्.",
            "अः + अ → ओऽ.",
            teaches="A visarga after अ before अ: अः + अ → ओऽ: मालानुसारतः + अपहरेत् → मालानुसारतोऽपहरेत्."),
    ],
}

# ---------------------------------------------------------------- unit 101
AUTHORED["101"] = {
    "title": "प्रजातायां … शूलं मक्कलाख्यं स्यात्",
    "question": "By unit 101, what condition is named, and in whom?",
    "rule": ("If (चेत्), in a woman who has given birth (प्रजाता), there is a pain (शूल) called makkala in the basti "
             "(rendered bladder) and an unclear place. The remedy follows in unit 102 (तत्र)."),
    "limits": ("Low confidence; an if-clause only. मुद्धोदरेषु is unclear and unsplit; basti = bladder is not certain "
               "(perhaps the lower abdomen). Makkala is usually spelled makkalla (flag). What makkalla is like (a lump) is "
               "not in the text. No question on these points."),
    "explain_hi": ("यहाँ से प्रसूता के मक्कल शूल का भाग शुरू होता है। यह केवल शर्त-वाक्य है: ‘यदि (चेत्) प्रसूता "
                   "(जन्म दे चुकी स्त्री) में बस्ति आदि में मक्कल नाम की पीड़ा हो’। "
                   "उपाय अगली इकाई 102 (‘तत्र’) में है। "
                   "‘मुद्धोदरेषु’ अस्पष्ट है; ‘बस्ति’ को मूत्राशय माना गया, पर अर्थ (मूत्राशय या निचला पेट) निश्चित नहीं। "
                   "‘मक्कल’ का सामान्य रूप ‘मक्कल्ल’ है; उसका विवरण ग्रन्थ में यहाँ नहीं दिया गया।"),
    "hook": "प्रसूता + मक्कल शूल = चेत् (यदि); उपाय तत्र, अगली इकाई में।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 101, what is the pain called?",
            ("Makkala", "शूलं मक्कलाख्यम्: a pain called makkala."),
            [("Garbha-saṅga", "Garbha-saṅga (retention of the fetus) was unit 73."),
             ("Vidāha", "No vidāha is named in unit 101."),
             ("Ānāha", "No ānāha is named in unit 101.")],
            "The pain of the woman who has given birth is called makkala.",
            "मक्कलाख्यं शूलम् = the pain called makkala."),
        order(1, "Put these words of unit 101 in the line's order (the unclear word is left out).",
              ["प्रजातायाम्", "चेत्", "शूलम्", "मक्कलाख्यम्", "स्यात्"],
              "In one who has given birth, if, pain, called makkala, there should be.",
              "प्रजातायाम् → चेत् → शूलम् → मक्कलाख्यम् → स्यात्."),
        match(2, "Match each word of unit 101 to its meaning.",
              [["प्रजाता", "one who has given birth"], ["चेत्", "if"], ["शूल", "pain"],
               ["आख्य", "called"], ["स्यात्", "there should be"]],
              "These words make the sure frame of the if-clause.",
              "प्रजाता, चेत्, शूल, आख्य, स्यात्.", role="extend",
              teaches="चेत् with the optative स्यात् makes an if-clause: if there should be."),
        mcq("discriminate", 3, "Which split of मक्कलाख्यम् is right?",
            ("मक्कल + आख्यम्", "अ + आ → आ: मक्कल + आख्यम् = मक्कलाख्यम्."),
            [("मक्कला + ख्यम्", "ख्यम् is not a word; the word is आख्यम्."),
             ("मक्कलम् + आख्यम्", "A final म् would give मक्कलमाख्यम्."),
             ("मक्कलः + आख्यम्", "अः before आ drops the visarga: मक्कल आख्यम्.")],
            "मक्कल (makkala) + आख्यम् (called).",
            "अ + आ → आ."),
        mcq("apply", 4, "By unit 101, in whom does the makkala pain arise?",
            ("A woman who has given birth", "प्रजातायाम्: in one who has given birth."),
            [("A pregnant woman before labour", "प्रजाता means one who has already given birth."),
             ("A woman whose fetus is retained", "प्रजाता has already given birth; retention was unit 73."),
             ("A woman in her seventh month", "No month is named in unit 101.")],
            "प्रजाता = one who has given birth (feminine past participle).",
            "प्रजातायाम् = in one who has given birth."),
        mcq("transfer", 5, "Built like चेत् … स्यात् of unit 101, what does a new example ज्वरश्चेत् स्यात् mean?",
            ("If there should be fever", "चेत् = if; स्यात् = there should be."),
            [("Fever is there, therefore", "चेत् is if, not therefore."),
             ("Fever has already gone", "स्यात् means there should be, not gone."),
             ("Wherever fever may be", "चेत् is if, not wherever.")],
            "ज्वरः + चेत् → ज्वरश्चेत्; with स्यात्: if there should be fever.",
            "चेत् + optative = if ... should be.",
            teaches="चेत् with an optative makes a condition: ज्वरश्चेत् स्यात् = if there should be fever."),
    ],
}

# ---------------------------------------------------------------- unit 102
AUTHORED["102"] = {
    "title": "तत्र यवक्षारचूर्णं सर्पिषा",
    "question": "By unit 102, what is drunk for the makkala pain, and with what?",
    "rule": ("In that case (तत्र), one should drink the powder of yavakṣāra (kṣāra of barley; probably impure potassium "
             "carbonate) with ghee, or with pleasantly warm water."),
    "limits": ("High confidence. The yavakṣāra identification as impure potassium carbonate is probable. तत्र points back "
               "to the if-clause of unit 101. No dose or duration. पिबेत is the middle optative of √पा."),
    "explain_hi": ("यह इकाई 101 की शर्त का उत्तर है (‘तत्र’ = उस स्थिति में): यवक्षार का चूर्ण पिए। "
                   "साथ में दो विकल्प: घी (सर्पिषा) या सुखोष्ण, यानी सुखद गुनगुना, जल; ‘वा’ इन दोनों को जोड़ता है। "
                   "यवक्षार को यव के पौधे की राख से बना अशुद्ध पोटैशियम कार्बोनेट मानना सम्भावित है, निश्चित नहीं। "
                   "‘पिबेत’ √पा का आत्मनेपदी विधिलिङ् है। मात्रा नहीं दी गई।"),
    "hook": "मक्कल में: यवक्षार-चूर्ण, घी या गुनगुने जल से।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 102, what powder is drunk for the makkala pain?",
            ("The powder of yavakṣāra", "यवक्षारचूर्णं … पिबेत: drink the yavakṣāra powder."),
            [("The powder of vatsakādi", "The vatsakādi powder was unit 92."),
             ("The powder of pippalī", "Pippalī is not named in unit 102."),
             ("A powder of plain salt", "Salt is not named in unit 102.")],
            "For the makkala pain: yavakṣāra powder.",
            "तत्र यवक्षारचूर्णं पिबेत."),
        order(1, "Put the words of unit 102 in the line's order.",
              ["तत्र", "यवक्षारचूर्णम्", "सर्पिषा", "सुखोष्णोदकेन", "वा", "पिबेत"],
              "In that case, yavakṣāra powder, with ghee, with pleasantly warm water, or, one should drink.",
              "तत्र → यवक्षारचूर्णम् → सर्पिषा → सुखोष्णोदकेन → वा → पिबेत."),
        match(2, "Match each word of unit 102 to its meaning.",
              [["तत्र", "in that case"], ["यवक्षार", "kṣāra of barley"], ["सर्पिस्", "ghee"],
               ["सुखोष्ण", "pleasantly warm"], ["उदक", "water"]],
              "The remedy, its two vehicles, and the link back to unit 101.",
              "तत्र, यवक्षार, सर्पिस्, सुखोष्ण, उदक.", role="extend",
              teaches="तत्र here means in that case: it answers the if-clause (चेत्) of unit 101."),
        mcq("discriminate", 3, "Which split of सुखोष्णोदकेन is right?",
            ("सुख + उष्ण + उदकेन", "अ + उ → ओ twice: सुखोष्ण, उष्णोदक."),
            [("सुखो + ष्णो + दकेन", "These pieces are not words."),
             ("सुख + उष्णः + उदकेन", "अः before उ would drop the visarga, not give ओ."),
             ("सुखम् + उष्ण + उदकेन", "A final म् would give सुखमुष्ण….")],
            "सुख (pleasantly) + उष्ण (warm) + उदकेन (with water).",
            "अ + उ → ओ."),
        multi("apply", 4, "With which does unit 102 allow the powder to be drunk?",
              [("Ghee", "Right: सर्पिषा, with ghee."),
               ("Madya", "Madya is not named in unit 102."),
               ("Pleasantly warm water", "Right: सुखोष्णोदकेन, the other option."),
               ("Cow's urine", "Cow's urine is not named in unit 102.")],
              [0, 2],
              "Two vehicles, joined by वा: ghee or pleasantly warm water.",
              "सर्पिषा सुखोष्णोदकेन वा."),
        mcq("transfer", 5, "By सर्पिषा (with ghee, from सर्पिस्), what is the instrumental of मनस् (mind)?",
            ("मनसा", "An -स् stem takes -आ in the instrumental: मनसा, like सर्पिस् → सर्पिषा."),
            [("मनसेन", "-एन belongs to अ-stems, not to -स् stems."),
             ("मनसि", "मनसि is the locative: in the mind."),
             ("मनः", "मनः is the nominative: the mind.")],
            "मनस् + आ = मनसा (with the mind), like सर्पिस् + आ = सर्पिषा.",
            "-स् stems: instrumental singular in -आ.",
            teaches="Stems in -स् take -आ in the instrumental singular: सर्पिस् → सर्पिषा, मनस् → मनसा."),
    ],
}


# ===================================================================== NOTES_HI
NOTES_HI = {
    "91": ("गद्य; विश्वास मध्यम। पाठ-चिह्न: छपा ‘मुल’ सम्भवतः ‘मूल’ (दीर्घ ऊ), और ‘कल्कंवा’ बिना अन्तराल = कल्कं वा। "
           "‘मूल’ केवल लाङ्गली का या दोनों का — दो तरह; डेटा ‘लाङ्गली की जड़’ पढ़ता है, इस पर प्रश्न नहीं। "
           "मूत्र किस पशु का, नहीं कहा। क्रिया (पाययेत्) इकाई 86 से समझी जाती है। "
           "सन्धि जाँची: मद्यमूत्र + अन्यतरेण → मद्यमूत्रान्यतरेण (अ + अ → आ); कल्कम् + वा → कल्कं वा (व्यंजन से पहले अनुस्वार)।"),
    "92": ("गद्य; विश्वास मध्यम; कोई पाठ-चिह्न नहीं। वत्सक = सम्भवतः कुटज का बीज (Holarrhena); समूह के सदस्य यहाँ नहीं गिनाए। "
           "क्रिया इकाई 86 से समझी जाती है। सन्धि जाँची: वत्सक + आदि → वत्सकादि (अ + आ → आ); चूर्णम् + वा → चूर्णं वा।"),
    "93": ("गद्य; विश्वास निम्न। पाठ-चिह्न: छपा ‘सिद्धस्यच’ = सिद्धस्य च (केवल अन्तराल)। पिचु कहाँ रखा जाए, नहीं कहा "
           "(सम्भवतः योनि, ग्रन्थ में नहीं); ‘भिगोया’ भी नहीं लिखा। शतपुष्पा = सम्भवतः सोआ (सौंफ भी प्रस्तावित); मदन = सम्भवतः मैनफल। "
           "सन्धि जाँची: पिचुम् + ग्राहयेत् → पिचुं ग्राहयेत् (व्यंजन से पहले अनुस्वार)।"),
    "94": ("गद्य; विश्वास मध्यम; कोई पाठ-चिह्न नहीं। ‘एनाम्’ पिछली इकाइयों की स्त्री की ओर संकेत; यहाँ नाम नहीं। "
           "सन्धि जाँची: ततः + च → ततश्च (विसर्ग → श् च से पहले); च + एनाम् → चैनाम् (अ + ए → ऐ); "
           "एनाम् + अनुवासन → एनामनुवासन; अनुवासनकाले + अनुवासयेत् → कालेऽनुवासयेत् (ए + अ → एऽ)।"),
    "95": ("गद्य; विश्वास मध्यम; कोई पाठ-चिह्न नहीं। वर्गीकरण: क्रिया नहीं छपी; डेटा के अनुसार यह इकाई 96 के ‘आस्थापयेत्’ से "
           "या इकाई 94 के अनुवासन से जुड़ती है — तय नहीं, इस पर प्रश्न नहीं। बिल्वज अस्पष्ट (देखें इकाई 86)। "
           "सन्धि जाँची: यूष + आदि → यूषादि (अ + आ → आ); आदि + आप्लवनैः → आद्याप्लवनैः (इ + आ → या); आप्लवनैः + च → आप्लवनैश्च।"),
    "96": ("गद्य; विश्वास निम्न। पाठ-चिह्न: ‘कुटजाकैकृतवेधन’ अस्पष्ट; ‘आकै’ शायद बिगड़ा ‘अर्क’ — केवल अनुमान, कोई पक्का सुधार नहीं; "
           "इस पर प्रश्न नहीं। हस्तिपर्णी अज्ञात, धामार्गव विवादित, ‘फल’ की पहचान निश्चित नहीं (परम्परा में प्रायः मदनफल, ग्रन्थ नहीं कहता)। "
           "कौन-से द्रव युक्त किए जाएँ, अलिखित। सन्धि जाँची: जीमूतक + इक्ष्वाकु → जीमूतकेक्ष्वाकु (अ + इ → ए); "
           "हस्तिपर्णी + उपहितैः → हस्तिपर्ण्युपहितैः (ई + उ → यु); उपहितैः + आस्थापयेत् → उपहितैरास्थापयेत् (ऐ के बाद विसर्ग → र्)।"),
    "97": ("गद्य; विश्वास निम्न; वाक्य अधूरा, वाक्य-रचना अनिश्चित। पाठ-चिह्न: ‘स्त्रिञ्चानि’ ज्ञात शब्द नहीं, छपाई बिगड़ी हो सकती है; "
           "अविभक्त, अस्पष्ट रखा गया; उसके बाद के ‘वा’ को ‘या’ पढ़ना अनुमान। पहले तृतीया-वाक्यांश का संज्ञा-शब्द (द्रव) अलिखित। "
           "पञ्चमूल बड़ा या छोटा, नहीं कहा। महावृक्ष विवादित (कभी Euphorbia)। सिद्धार्थक = सफेद सरसों सम्भावित "
           "(डेटा की हिन्दी में ‘सम्भवतः’ छूटा है)। सन्धि जाँची: महा + वृक्ष → महावृक्ष; छपा ‘आपोथ्यपञ्चमूल’ बिना अन्तराल।"),
    "98": ("गद्य; विश्वास निम्न; कोई पाठ-चिह्न नहीं। ‘तेन पूतेन स्नेहवता फलादियुक्तेन …’ सब कटुतैल के विशेषण हैं या किसी अलग द्रव के — "
           "व्याकरण दोनों मानता है; इस पर प्रश्न नहीं। कटुतैल = सम्भवतः सरसों का तेल। उत्तरबस्ति का मार्ग यहाँ नहीं कहा। "
           "सन्धि जाँची: फल + आदि → फलादि; यथा + उक्त → यथोक्त (आ + उ → ओ); उक्त + आस्थापन → उक्तास्थापन (अ + आ → आ); "
           "कटुतैलेन + उत्तरबस्तिम् → कटुतैलेनोत्तरबस्तिम् (अ + उ → ओ); बस्तिम् + दद्यात् → बस्तिं दद्यात्।"),
    "99": ("गद्य; विश्वास मध्यम; कोई पाठ-चिह्न नहीं। डेटा का विभाग: कल्क पहले पाँच द्रव्यों का, फिर क्षीर और गोमूत्र। सुमुख = सम्भवतः एक तुलसी "
           "(कुछ सूचियों में विवादित); अजाजी = सम्भवतः जीरा। सन्धि जाँची: मरिच + अजाजी → मरिचाजाजी (अ + अ → आ); "
           "कटुतैलेन + अनुवासयेत् → छपा ‘कटुतैलेनाऽनुवासयेत्’ (अ + अ → आ; ‘ऽ’ छपाई की आदत)।"),
    "100": ("डेटा में प्रकार ‘verse’, पर दोनों छपी पंक्तियाँ गद्य-निर्देश जैसी लगती हैं (रिपोर्ट किया); विश्वास निम्न; दो छपी पंक्तियाँ जोड़ी गईं। "
            "[02.03.107] पिच्छा = सम्भवतः शाल्मली का गोंद; उमा = सम्भवतः अलसी (उमा हल्दी आदि का भी नाम); ‘विधुनुयात्’ का कर्म अलिखित। "
            "[02.03.108] ‘माला’ = हार, पंक्ति — यहाँ अर्थ अस्पष्ट; ‘अपहरेत्’ का कर्म अलिखित; ‘स्निग्ध’ = तेल लगा (या स्नेहयुक्त)। "
            "इन पर प्रश्न नहीं। सन्धि जाँची: माला + अनुसारतः → मालानुसारतः (आ + अ → आ); मालानुसारतः + अपहरेत् → मालानुसारतोऽपहरेत् "
            "(अः + अ → ओऽ); योनिम् + पूरयित्वा → योनिं पूरयित्वा।"),
    "101": ("गद्य; विश्वास निम्न। पाठ-चिह्न: ‘मुद्धोदरेषु’ अस्पष्ट (शायद मूर्ध-उदरेषु जैसा कुछ), अविभक्त रखा; ‘मक्कलाख्यं’ का सामान्य रूप "
            "मक्कल्लाख्यं (दो ल)। वर्गीकरण: यह शर्त-वाक्य है; उत्तर इकाई 102 (‘तत्र’) में। बस्ति = मूत्राशय, पर अर्थ (मूत्राशय या निचला पेट) "
            "निश्चित नहीं। सन्धि जाँची: चेत् + बस्ति → चेद्बस्ति (त् → द् घोष से पहले; छपाई में ब के स्थान पर व); मक्कल + आख्यम् → मक्कलाख्यम्; "
            "शूलम् + मक्कलाख्यम् → शूलं मक्कलाख्यं।"),
    "102": ("गद्य; विश्वास उच्च; कोई पाठ-चिह्न नहीं। वर्गीकरण: इकाई 101 की शर्त का उत्तर (‘तत्र’)। यवक्षार = यव-पौधे की राख का अशुद्ध "
            "पोटैशियम कार्बोनेट — सम्भावित। ‘पिबेत’ √पा का आत्मनेपदी विधिलिङ्। सन्धि जाँची: सुख + उष्ण + उदकेन → सुखोष्णोदकेन "
            "(अ + उ → ओ, दो बार); चूर्णम् + सर्पिषा → चूर्णं सर्पिषा।"),
}


# ===================================================================== AIDS
AIDS = {
    "91": {
        "diagram": {"groups": [
            {"label": "कल्क", "items": ["कुष्ठ", "लाङ्गली (सम्भवतः कलिहारी) की जड़"]},
            {"label": "साथ में (दोनों में से एक)", "items": ["मद्य", "मूत्र (किसका, नहीं कहा)"]}]},
        "chunks": "कुष्ठलाङ्गलीमुलकल्कंवा | मद्यमूत्रान्यतरेण",
        "sandhi": "अ + अ → आ: मद्यमूत्र + अन्यतरेण → मद्यमूत्रान्यतरेण · म् → अनुस्वार व्यंजन से पहले: कल्कम् + वा → कल्कं वा।",
        "frame": "द्रव्य (कल्क) + ‘वा’ (या, एक और विकल्प) + वाहन (तृतीया: अन्यतरेण); क्रिया पाययेत् इकाई 86 से।",
    },
    "92": {
        "chunks": "वत्सकादिचूर्णं | वा | मद्येन",
        "sandhi": "अ + आ → आ: वत्सक + आदि → वत्सकादि · म् → अनुस्वार: चूर्णम् + वा → चूर्णं वा।",
        "contrast": "इसी इकाई में रूप: चूर्ण = सूखा पाउडर (वत्सक आदि का); वाहन: मद्य।",
        "anchors": "याद-सूत्र: ‘आदि’ = समूह का पहला नाम, बाकी समूह साथ। (मेरी याद-पद्धति)",
    },
    "93": {
        "chain": {"steps": ["शतपुष्पा, कुष्ठ, मदन, हिङ्गु", "इनसे पकाया तेल", "उस तेल का पिचु (रुई का फाहा)",
                            "पकड़वाए (स्थान नहीं कहा)"]},
        "chunks": "शतपुष्पाकुष्ठमदनहिङ्गुसिद्धस्यच | तैलस्य | पिचुं | ग्राहयेत्",
        "frame": "क्या पकाया (द्रव्य-सूची + सिद्ध) → किसका (तैलस्य) → क्या (पिचुम्) → क्रिया (ग्राहयेत्, प्रेरणार्थक)।",
        "pegs": "मेरा बनाया चित्र: चार डिब्बे — सोआ, कुष्ठ, मैनफल, हींग — एक कड़ाही में; उसमें डूबा रुई का फाहा। (केवल याद के लिए)",
    },
    "94": {
        "chunks": "ततश्चैनाम् | अनुवासनकाले | अनुवासयेत्",
        "sandhi": "विसर्ग + च → श्च: ततः + च → ततश्च · अ + ए → ऐ: च + एनाम् → चैनाम् · ए + अ → एऽ: काले + अनुवासयेत् → कालेऽनुवासयेत्।",
        "frame": "कब (ततः, अनुवासनकाले) → किसे (एनाम्) → क्रिया (अनुवासयेत्)।",
    },
    "95": {
        "chunks": "बिल्व | बिल्वज | यूषादि | आप्लवनैश्च",
        "sandhi": "अ + आ → आ: यूष + आदि → यूषादि · इ + आ → या: आदि + आप्लवनैः → आद्याप्लवनैः · विसर्ग + च → श्च: आप्लवनैः + च → आप्लवनैश्च।",
        "frame": "केवल तृतीया-वाक्यांश (किससे: आप्लवनैः); क्रिया इस इकाई में नहीं।",
    },
    "96": {
        "diagram": {"groups": [
            {"label": "नाम (क्रम से) और डेटा की पहचान", "items": [
                "फल: पहचान निश्चित नहीं", "जीमूतक: सम्भवतः देवदाली", "इक्ष्वाकु: सम्भवतः कड़वी लौकी", "धामार्गव: विवादित",
                "कुटज: मानक", "आकै: अस्पष्ट", "कृतवेधन: सम्भवतः तोरई", "हस्तिपर्णी: अज्ञात"]}]},
        "chunks": "फल | जीमूतक | इक्ष्वाकु | धामार्गव | कुटज | आकै (?) | कृतवेधन | हस्तिपर्णी | उपहितैः | आस्थापयेत्",
        "sandhi": "अ + इ → ए: जीमूतक + इक्ष्वाकु → जीमूतकेक्ष्वाकु · ई + उ → यु: हस्तिपर्णी + उपहितैः → हस्तिपर्ण्युपहितैः · ऐ के बाद विसर्ग → र् स्वर से पहले: उपहितैः + आस्थापयेत् → उपहितैरास्थापयेत्।",
        "frame": "द्रव्य-सूची + ‘उपहितैः’ (से युक्त किए हुए, तृतीया बहुवचन) → क्रिया ‘आस्थापयेत्’।",
    },
    "97": {
        "chain": {"steps": ["१ शाल्मली के डण्ठल", "२ कूटकर (आपोथ्य)", "३ पञ्चमूल के काढ़े में", "४ मसले (विमर्दयेत्)"]},
        "chunks": ("सिद्धार्थककुष्ठलाङ्गलीमहावृक्षक्षीरमिश्रेण वा | सुरामण्डेन | शाल्मलीवृन्तानि वा | स्त्रिञ्चानि (?) | "
                   "आपोथ्य | पञ्चमूलकषाये | विमर्दयेत्"),
        "frame": "पहला अंश: तृतीया (किससे; संज्ञा अलिखित) · दूसरा अंश: कर्म (वृन्तानि) → पूर्वकालिक क्रिया (आपोथ्य) → स्थान (कषाये) → क्रिया (विमर्दयेत्)।",
        "anchors": "याद-सूत्र: आ + √पुथ् → आपोथ्य; उपसर्ग है तो -य, नहीं तो -त्वा। (मेरी याद-पद्धति)",
    },
    "98": {
        "chain": {"steps": ["यथोक्त आस्थापन-द्रव्य", "उनसे पका कटु तेल (सम्भवतः सरसों)", "छाना, स्नेहयुक्त, फल आदि सहित",
                            "उत्तरबस्ति दे"]},
        "chunks": "तेन च पूतेन | स्नेहवता | फलादियुक्तेन | यथोक्तास्थापनद्रव्यसिद्धेन | कटुतैलेनोत्तरबस्तिं | दद्यात्",
        "sandhi": "आ + उ → ओ: यथा + उक्त → यथोक्त · अ + आ → आ: उक्त + आस्थापन → उक्तास्थापन · अ + उ → ओ: कटुतैलेन + उत्तरबस्तिम् → कटुतैलेनोत्तरबस्तिम्।",
        "frame": "सब शब्द तृतीया में (तेन … कटुतैलेन: किससे) → कर्म (उत्तरबस्तिम्) → क्रिया (दद्यात्)।",
    },
    "99": {
        "diagram": {"groups": [
            {"label": "कल्क के द्रव्य (क्रम से)", "items": ["शिग्रु: सहजन", "सुमुख: सम्भवतः एक तुलसी", "मरिच: काली मिर्च",
                                                    "अजाजी: सम्भवतः जीरा", "चित्रक: चीता"]},
            {"label": "साथ में", "items": ["क्षीर (दूध)", "गोमूत्र"]},
            {"label": "परिणाम", "items": ["पका कटु तेल → अनुवासन"]}]},
        "chunks": "शिग्रु | सुमुख | मरिच | अजाजि | चित्रक | कल्क | क्षीर | गोमूत्र | सिद्धेन वा | कटुतैलेनाऽनुवासयेत्",
        "sandhi": "अ + अ → आ: मरिच + अजाजी → मरिचाजाजी; कटुतैलेन + अनुवासयेत् → कटुतैलेनानुवासयेत् (छपाई में ‘नाऽनु’)।",
        "anchors": "याद-सूत्र: ‘शि-सु-म-अ-चि’ — शिग्रु, सुमुख, मरिच, अजाजी, चित्रक। (मेरी याद-पद्धति, ग्रन्थ का शब्द नहीं)",
    },
    "100": {
        "diagram": {"groups": [
            {"label": "पहला विकल्प", "items": ["घी सहित उमा-शाल्मली पिच्छा", "योनि भरकर", "हिलाए (क्या, अलिखित)"]},
            {"label": "दूसरा विकल्प", "items": ["स्निग्ध, कटे नाखून वाला हाथ", "माला के अनुसार (अर्थ अस्पष्ट)", "हटाए (क्या, अलिखित)"]}]},
        "chunks": "उमाशाल्मलीपिच्छया वा सघृतया | योनिं पूरयित्वा | विधुनुयात् | स्निग्धेन वा कृत्तनखेन पाणिना | मालानुसारतोऽपहरेत्",
        "sandhi": "आ + अ → आ: माला + अनुसारतः → मालानुसारतः · अः + अ → ओऽ: मालानुसारतः + अपहरेत् → मालानुसारतोऽपहरेत्।",
        "frame": "वा … (पूरयित्वा → विधुनुयात्) · वा … (पाणिना → अपहरेत्): दो विकल्प।",
    },
    "101": {
        "chunks": "प्रजातायां | चेद्वस्तिमुद्धोदरेषु (?) | शूलं | मक्कलाख्यं | स्यात्",
        "sandhi": "अ + आ → आ: मक्कल + आख्यम् → मक्कलाख्यम् · त् → द् घोष से पहले: चेत् + बस्ति → चेद्बस्ति (छपा ‘चेद्वस्ति’)।",
        "frame": "शर्त (चेत् … स्यात्): किसमें (प्रजातायाम्) → क्या (शूलं मक्कलाख्यम्); उत्तर ‘तत्र’ इकाई 102 में।",
    },
    "102": {
        "chain": {"steps": ["यदि प्रसूता में मक्कल शूल (इकाई 101)", "तत्र: यवक्षार का चूर्ण पिए", "घी के साथ",
                            "या सुखोष्ण जल के साथ"]},
        "chunks": "तत्र | यवक्षारचूर्णं | सर्पिषा | सुखोष्णोदकेन वा | पिबेत",
        "sandhi": "अ + उ → ओ: सुख + उष्ण → सुखोष्ण; उष्ण + उदकेन → उष्णोदकेन · म् → अनुस्वार: चूर्णम् + सर्पिषा → चूर्णं सर्पिषा।",
        "frame": "तत्र (उस स्थिति में) → कर्म (यवक्षारचूर्णम्) → वाहन (सर्पिषा / सुखोष्णोदकेन वा) → क्रिया (पिबेत)।",
    },
}


# ===================================================================== IMAGE_SPECS
IMAGE_SPECS = {
    ("91", "diagram"): {
        "file": "sh3-kushtha-langali-91.svg",
        "alt": ("Two columns for unit 91: the paste is of kuṣṭha and the root of lāṅgalī (probably gloriosa lily); it is "
                "taken with one of two liquids, madya or urine (whose urine is not stated)."),
        "type": "split",
        "title": "इकाई ९१: कल्क और वाहन",
        "cols": [["कल्क", ["कुष्ठ", "लाङ्गली (सम्भवतः कलिहारी) की जड़"]],
                 ["दोनों में से एक", ["मद्य", "मूत्र (किसका, नहीं कहा)"]]],
    },
    ("93", "chain"): {
        "file": "sh3-picu-taila-93.svg",
        "alt": ("Flowchart of unit 93: śatapuṣpā, kuṣṭha, madana and hiṅgu; oil cooked with them; a picu (cotton wad) of "
                "that oil; made to be held, the place not stated."),
        "type": "mermaid",
        "code": ("flowchart TD\n"
                 "  A[\"शतपुष्पा, कुष्ठ, मदन, हिङ्गु\"] --> B[\"इनसे पकाया तेल\"]\n"
                 "  B --> C[\"उस तेल का पिचु\"]\n"
                 "  C --> D[\"पकड़वाए; स्थान नहीं कहा\"]\n"),
    },
    ("96", "diagram"): {
        "file": "sh3-asthapana-dravya-96.svg",
        "alt": ("Table of the eight names of unit 96 in order with the data's labels: phala not firm, jīmūtaka probable, "
                "ikṣvāku probably bitter bottle gourd, dhāmārgava disputed, kuṭaja standard, ākai unclear, kṛtavedhana "
                "probably ridge gourd, hastiparṇī unidentified."),
        "type": "table",
        "title": "इकाई ९६: आस्थापन के द्रव्य",
        "heads": ["नाम (क्रम से)", "डेटा की पहचान"],
        "rows": [["फल", "निश्चित नहीं"], ["जीमूतक", "सम्भवतः देवदाली"], ["इक्ष्वाकु", "सम्भवतः कड़वी लौकी"],
                 ["धामार्गव", "विवादित"], ["कुटज", "कुड़ा (मानक)"], ["आकै", "अस्पष्ट शब्द"],
                 ["कृतवेधन", "सम्भवतः तोरई"], ["हस्तिपर्णी", "अज्ञात"]],
    },
    ("97", "chain"): {
        "file": "sh3-shalmali-vrinta-97.svg",
        "alt": ("Numbered flowchart of the sure part of unit 97: 1 the stalks of śālmalī, 2 pounded, 3 in a decoction of the "
                "five roots, 4 crushed."),
        "type": "mermaid",
        "code": ("flowchart TD\n"
                 "  A[\"१ शाल्मली के डण्ठल\"] --> B[\"२ कूटकर (आपोथ्य)\"]\n"
                 "  B --> C[\"३ पञ्चमूल के काढ़े में\"]\n"
                 "  C --> D[\"४ मसले (विमर्दयेत्)\"]\n"),
    },
    ("99", "diagram"): {
        "file": "sh3-anuvasana-taila-99.svg",
        "alt": ("Table of unit 99 in order: śigru drumstick, sumukha probably a basil, marica black pepper, ajājī probably "
                "cumin, citraka leadwort, as paste; with milk and cow's urine; the kaṭutaila cooked with them is given "
                "as an anuvāsana."),
        "type": "table",
        "title": "इकाई ९९: अनुवासन का कटु तेल",
        "heads": ["द्रव्य (क्रम से)", "डेटा की पहचान"],
        "rows": [["शिग्रु", "सहजन"], ["सुमुख", "सम्भवतः एक तुलसी"], ["मरिच", "काली मिर्च"],
                 ["अजाजी", "सम्भवतः जीरा"], ["चित्रक", "चीता"], ["क्षीर, गोमूत्र", "दूध, गाय का मूत्र"],
                 ["कटु तेल", "सम्भवतः सरसों का तेल"]],
    },
    ("100", "diagram"): {
        "file": "sh3-do-vikalpa-100.svg",
        "alt": ("Flowchart of unit 100 with two options: fill the yoni with umā-śālmalī picchā and ghee, then shake; or, "
                "with an oiled hand with nails cut, remove following the mālā (sense unclear)."),
        "type": "mermaid",
        "code": ("flowchart TD\n"
                 "  R[\"दो विकल्प: वा … वा\"] --> A[\"घी सहित उमा-शाल्मली पिच्छा\"]\n"
                 "  A --> B[\"योनि भरकर हिलाए\"]\n"
                 "  R --> C[\"स्निग्ध, कटे नाखून का हाथ\"]\n"
                 "  C --> D[\"माला के अनुसार हटाए\"]\n"),
    },
    ("102", "chain"): {
        "file": "sh3-yavakshara-102.svg",
        "alt": ("Flowchart of units 101 and 102: if a woman who has given birth has the makkala pain, in that case she "
                "drinks yavakṣāra powder, with ghee or with pleasantly warm water."),
        "type": "mermaid",
        "code": ("flowchart TD\n"
                 "  A[\"यदि प्रसूता में मक्कल शूल\"] -->|\"तत्र\"| B[\"यवक्षार का चूर्ण पिए\"]\n"
                 "  B --> C[\"घी के साथ\"]\n"
                 "  B -->|\"वा\"| D[\"सुखोष्ण जल के साथ\"]\n"),
    },
}
