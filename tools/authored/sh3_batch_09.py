from helpers import mcq, match, order, fill, multi, accepts


AUTHORED = {}

# ---------------------------------------------------------------- unit 103
AUTHORED["103"] = {
    "title": "वरणादिं वा ... अथवा वीरतरादि",
    "question": "By unit 103, which two further preparations follow the yavakṣāra drink of unit 102?",
    "rule": ("Or (वा) the varaṇādi group with pañcakola and elā (probably cardamom) and an unclear atīvāpa; or else (अथवा) "
             "one with the vīratarādi and mūṣakādi groups as pratīvāpa (added substance). The verb (पिबेत्) is carried from unit 102."),
    "limits": ("Two printed lines; low confidence. अतीवाप is unclear (perhaps प्रतीवाप, not adopted); elā's role is unsure; "
               "whether one or both groups are the added substance is open; मूषक may be मुष्कक (not adopted). Group members "
               "are not given. No question rests on these."),
    "explain_hi": ("यह इकाई कार्ड १०२ के यवक्षार-पान के बाद मक्कल शूल के और विकल्प देती है; क्रिया ‘पिबेत्’ वहीं से आती है। "
                   "पहला विकल्प: वरणादि गण (वरण से आरम्भ होने वाला गण; वरण = Crateva nurvala, मानक) पञ्चकोल सहित, और एला "
                   "(सम्भवतः इलायची) तथा अस्पष्ट शब्द ‘अतीवाप’ के साथ। "
                   "पञ्चकोल = पीपर, पीपरामूल, चव्य, चित्रक और सोंठ (मानक)। "
                   "दूसरा विकल्प ‘अथवा’ से: वीरतरादि और मूषकादि गण प्रतीवाप यानी मिलाई जाने वाली वस्तु के रूप में; "
                   "समास खुला है, इसलिए कौन-सा गण प्रतीवाप है, यह तय नहीं। विश्वास निम्न है।"),
    "hook": "वा वरणादि + पञ्चकोल; अथवा वीरतरादि-मूषकादि प्रतीवाप।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "In unit 103, what does वरणादि name?",
            ("The group beginning with varaṇa", "-आदि = beginning with: varaṇa and the drugs that go with it."),
            [("Only varaṇa itself, as one single plant", "-आदि makes it a group, not one plant."),
             ("A decoction made of varaṇa", "No word for decoction stands in unit 103."),
             ("The five pungents (pañcakola)", "Pañcakola is named separately, with स-.")],
            "वरणादि = the group (gaṇa) beginning with varaṇa (Crateva nurvala; standard).",
            "X-आदि = the group beginning with X."),
        order(1, "Put the printed words of unit 103 in their order.",
              ["वरणादिं वा", "सपंचकोलमेलामतीवापं", "अथवा", "वीरतरादिमूषकादिप्रतीवापं"],
              "Line one: वरणादिं वा सपंचकोलमेलामतीवापं; line two: अथवा वीरतरादिमूषकादिप्रतीवापं.",
              "वरणादिं वा → सपंचकोल... → अथवा → वीरतरादि..."),
        match(2, "Match each word of unit 103 to its meaning.",
              [["वरणादि", "the group beginning with varaṇa"], ["पञ्चकोल", "the five pungents"],
               ["एला", "probably cardamom"], ["अथवा", "or else"], ["प्रतीवाप", "added substance"]],
              "These words carry the two alternatives of unit 103.",
              "वरणादि, पञ्चकोल, एला, अथवा, प्रतीवाप.", role="extend",
              teaches="A name + आदि at a compound's end means the whole group beginning with that drug: वरणादि, वीरतरादि, मूषकादि."),
        multi("discriminate", 3, "Which drugs make up pañcakola as the card lists it?",
              [("Black pepper (marica)", "Not in pañcakola; black pepper belongs to trikaṭu."),
               ("Long pepper (pippalī)", "Right: long pepper is the first of the five."),
               ("Cardamom (elā)", "Elā is named separately in the line, not inside pañcakola."),
               ("Citraka", "Right: citraka is one of the five."),
               ("Dry ginger", "Right: dry ginger is one of the five.")],
              [1, 3, 4],
              "Pañcakola = long pepper, its root, cavya, citraka and dry ginger (standard).",
              "पञ्चकोल: पीपर, पीपरामूल, चव्य, चित्रक, सोंठ."),
        mcq("apply", 4, "In unit 103, what does अथवा at the head of line two introduce?",
            ("A second, different preparation", "अथवा = or else: the vīratarādi/mūṣakādi preparation is another choice."),
            [("The reason for the makkala pain", "No cause is stated in unit 103."),
             ("The dose of the first preparation", "No dose is given in unit 103."),
             ("The time when it is to be drunk", "No time is named in unit 103.")],
            "वा and अथवा set out alternatives; the verb is the carried पिबेत्.",
            "अथवा = or else: a further alternative."),
        mcq("transfer", 5, "By the join in वरणादि (वरण + आदि), how do मरिच + आदि join in a new example?",
            ("मरिचादि", "अ + आ → आ, as वरण + आदि = वरणादि."),
            [("मरिचेदि", "ए comes from अ + इ, not from अ + आ."),
             ("मरिचौदि", "औ comes from अ + ओ or औ, not from अ + आ."),
             ("मरिच्यादि", "य् comes from इ before a vowel; मरिच ends in अ.")],
            "मरिच + आदि = मरिचादि, like वरण + आदि = वरणादि.",
            "अ + आ → आ.",
            teaches="A short अ followed by आ merges into one long आ: वरण + आदि → वरणादि."),
    ],
}

# ---------------------------------------------------------------- unit 104
AUTHORED["104"] = {
    "title": "लवणचूर्णं वावत्सकादिनिर्यूहेण",
    "question": "By unit 104, with what is salt powder taken?",
    "rule": ("Or salt powder (लवणचूर्ण) with a decoction (निर्यूह) of the vatsaka group (वत्सकादि). "
             "The verb is carried over from before."),
    "limits": ("Prose, medium confidence. Which salt is meant is not stated; vatsaka is not identified in this unit's data; "
               "no amount is given. वा is printed joined to the next word (वावत्सकादि). No question on the kind of salt."),
    "explain_hi": ("यह गद्य-पंक्ति एक और विकल्प देती है: लवण का चूर्ण, वत्सकादि गण के निर्यूह यानी क्वाथ के साथ। "
                   "क्रिया पहले से चली आ रही है, यहाँ छपी नहीं। "
                   "कौन-सा लवण, यह नहीं कहा गया; मात्रा भी नहीं दी गई। "
                   "‘वा’ अगले शब्द से जुड़ा छपा है (वावत्सकादि), इसे ‘वा वत्सकादि’ पढ़ा गया है। "
                   "‘निर्यूहेण’ में ण इसलिए है कि उसी शब्द में पहले र् आया है (णत्व नियम)।"),
    "hook": "नमक का चूर्ण + वत्सकादि का क्वाथ।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 104, what is taken with the vatsaka-group decoction?",
            ("Salt powder", "लवणचूर्णं: powder of salt."),
            [("Old jaggery", "Old jaggery is unit 108."),
             ("Yavakṣāra powder", "Yavakṣāra powder is unit 102."),
             ("Pepper paste", "A marica paste is unit 106.")],
            "Salt powder with a decoction of the vatsaka group.",
            "लवणचूर्ण = salt powder."),
        order(1, "Put the words of unit 104 in the line's order.",
              ["लवणचूर्णं", "वा", "वत्सकादि", "निर्यूहेण"],
              "Salt powder, or, of the vatsaka group, with the decoction.",
              "लवणचूर्णं → वा → वत्सकादि → निर्यूहेण."),
        match(2, "Match each word of unit 104 to its meaning.",
              [["लवण", "salt"], ["चूर्ण", "powder"], ["निर्यूह", "decoction"],
               ["वत्सकादि", "the group beginning with vatsaka"]],
              "Four words carry the whole line.",
              "लवण, चूर्ण, निर्यूह, वत्सकादि.", role="extend",
              teaches="निर्यूह is a decoction; निर्यूहेण, its instrumental, means with the decoction."),
        mcq("discriminate", 3, "Which case label does the card give निर्यूहेण?",
            ("Instrumental singular: with the decoction", "The data labels it inst. sg."),
            [("Locative singular: in the decoction", "The locative would be निर्यूहे."),
             ("Ablative singular: from the decoction", "The ablative would be निर्यूहात्."),
             ("Genitive singular: of the decoction", "The genitive would be निर्यूहस्य.")],
            "निर्यूहेण = with the decoction: the liquid the salt powder is taken with.",
            "-एण / -एन = instrumental singular of an अ-stem."),
        multi("apply", 4, "Which statements does unit 104 support?",
              [("The kind of salt is named", "Not stated: only लवण, salt."),
               ("The salt is taken as a powder", "Right: लवणचूर्णं."),
               ("A dose of the powder is given", "No amount is given."),
               ("The decoction is of the vatsaka group", "Right: वत्सकादिनिर्यूहेण.")],
              [1, 3],
              "Salt powder with the vatsaka-group decoction; no salt kind and no dose.",
              "लवणचूर्णं वा वत्सकादिनिर्यूहेण."),
        mcq("transfer", 5, "Built like निर्यूहेण, which instrumental is right for the new example मार्ग (path)?",
            ("मार्गेण", "र् earlier in the word, only ग between: न → ण, as in निर्यूहेण."),
            [("मार्गेन", "With र् before and nothing blocking, न must become ण."),
             ("मार्गाण", "The अ-stem instrumental ends in -एन/-एण, not -आण."),
             ("मार्गेणा", "The instrumental singular has a short final अ.")],
            "मार्ग → मार्गेण, like निर्यूह → निर्यूहेण.",
            "न → ण after र्, ऋ or ष् in the same word when only vowels, क-/प-वर्ग, य, व, ह stand between.",
            teaches="णत्व: after र्, ऋ or ष् in one word, न becomes ण unless a palatal, retroflex or dental (or ल, श, स) stands between: निर्यूहेण."),
    ],
}

# ---------------------------------------------------------------- unit 105
AUTHORED["105"] = {
    "title": "वत्सकादिं वा मदिरया",
    "question": "By unit 105, with what drink is the vatsaka group taken?",
    "rule": "Or the vatsaka group (वत्सकादि) with madirā (मदिरा, an intoxicating drink). The verb is carried over.",
    "limits": ("Three words of prose, medium confidence. The verb is not printed. The kind of madirā, the members of the "
               "vatsaka group and any amount are not stated."),
    "explain_hi": ("तीन शब्दों की यह गद्य-पंक्ति एक और विकल्प है: वत्सकादि गण को मदिरा (एक मादक पेय) के साथ। "
                   "क्रिया पहले से चली आ रही है, यहाँ नहीं छपी। "
                   "‘वत्सकादिं’ द्वितीया है, यानी जो लिया जाए; ‘मदिरया’ तृतीया है, यानी किसके साथ। "
                   "मदिरा का प्रकार, गण के सदस्य और मात्रा नहीं बताए गए।"),
    "hook": "वत्सकादि + मदिरा: तीन शब्द, एक विकल्प।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 105, with what is the vatsaka group taken?",
            ("With madirā", "मदिरया = with madirā, an intoxicating drink."),
            [("With ghee", "Ghee is a vehicle in unit 102, not here."),
             ("With honey and water", "No honey is named in unit 105."),
             ("With milk", "No milk is named in unit 105.")],
            "वत्सकादिं वा मदिरया: the vatsaka group with madirā.",
            "मदिरया = with madirā."),
        order(1, "Put the words of unit 105 in the line's order.",
              ["वत्सकादिं", "वा", "मदिरया"],
              "The vatsaka group, or, with madirā.",
              "वत्सकादिं → वा → मदिरया."),
        fill(2, "Or the vatsaka group with madirā: वत्सकादिं वा ____ (type it in Devanagari or in English letters, e.g. dharma).",
             accepts("मदिरया", None, "madiraya"),
             "The line is वत्सकादिं वा मदिरया.",
             "मदिरया is the instrumental of मदिरा: with madirā.",
             "मदिरया = with madirā (instrumental)."),
        mcq("discriminate", 3, "Which case is मदिरया, and what does it show here?",
            ("Instrumental: with madirā", "-अया is the instrumental singular of an आ-stem like मदिरा."),
            [("Genitive: of madirā", "The genitive would be मदिरायाः."),
             ("Locative: in madirā", "The locative would be मदिरायाम्."),
             ("Dative: for madirā", "The dative would be मदिरायै.")],
            "मदिरया = with madirā: the drink with which the group is taken.",
            "आ-stem instrumental singular: -अया."),
        mcq("apply", 4, "In unit 105, which word names what is taken and which the drink it is taken with?",
            ("वत्सकादिं taken; मदिरया the drink", "Accusative = what is taken; instrumental = with what."),
            [("मदिरया taken; वत्सकादिं the drink", "Reversed: मदिरया is the instrumental, with madirā."),
             ("Both are taken; वा joins them", "वा marks this line as another option, not a pair."),
             ("वा taken; मदिरया the drink", "वा is the particle or, not a drug.")],
            "वत्सकादिं (acc.) is taken, मदिरया (inst.) is the drink.",
            "Accusative = what is taken; instrumental = the vehicle."),
        mcq("transfer", 5, "Built like मदिरया from मदिरा, what is the instrumental singular of माला (garland)?",
            ("मालया", "आ-stem instrumental: -अया, as मदिरा → मदिरया."),
            [("मालेन", "-एन is the ending of an अ-stem, not of माला."),
             ("मालायाः", "मालायाः is genitive or ablative singular."),
             ("मालायाम्", "मालायाम् is the locative singular.")],
            "माला → मालया, like मदिरा → मदिरया.",
            "आ-stem feminine, instrumental singular: -अया.",
            teaches="A feminine आ-stem takes -अया in the instrumental singular: मदिरा → मदिरया (with madirā)."),
    ],
}

# ---------------------------------------------------------------- unit 106
AUTHORED["106"] = {
    "title": "अंशुमतीद्वयकषायेनवा मरिचभद्रदारुकल्कं",
    "question": "By unit 106, which decoction and which paste are named?",
    "rule": ("Two things are named: a decoction (कषाय) of the aṃśumatī pair (द्वय), and a paste (कल्क) of marica "
             "(black pepper) and bhadradāru (deodar; probable). The main substance and the verb are carried from unit 102."),
    "limits": ("Low confidence. With वा after कषायेन, the decoction may be a separate option or the paste's vehicle: open. "
               "The pair (probably śālaparṇī and pṛśniparṇī) is disputed. No question on how "
               "the two parts relate; questions ask only the data's label for the pair, never which plants it is."),
    "explain_hi": ("इस गद्य-पंक्ति में दो चीज़ें हैं: अंशुमती-द्वय का कषाय (काढ़ा), और मरिच तथा भद्रदारु का कल्क। "
                   "अंशुमती-द्वय यानी सम्भवतः शालपर्णी और पृश्निपर्णी; यह पहचान व्याख्या है और विवादित है। "
                   "भद्रदारु = देवदारु (सम्भावित)। "
                   "‘वा’ कषायेन से जुड़ा छपा है; इसलिए दो अर्थ खुले हैं: काढ़ा अलग विकल्प, या कल्क को काढ़े के साथ लेना। "
                   "मुख्य द्रव्य और क्रिया कार्ड १०२ से चले आते हैं।"),
    "hook": "अंशुमती-जोड़ी का काढ़ा; मरिच-भद्रदारु का कल्क।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "In unit 106, what is made of marica and bhadradāru?",
            ("A paste (कल्क)", "मरिचभद्रदारुकल्कं: the compound ends in कल्क, paste."),
            [("A decoction (कषाय)", "कषाय is of the aṃśumatī pair."),
             ("An oil (तैल)", "No oil is named in unit 106."),
             ("A powder (चूर्ण)", "No powder is named in unit 106.")],
            "Marica and bhadradāru make a paste (kalka).",
            "...कल्कं = paste."),
        order(1, "Put the words of unit 106 in the line's order.",
              ["अंशुमतीद्वय", "कषायेन", "वा", "मरिचभद्रदारु", "कल्कं"],
              "Of the aṃśumatī pair, with the decoction, or, of marica and bhadradāru, the paste.",
              "अंशुमतीद्वय → कषायेन → वा → मरिचभद्रदारु → कल्कं."),
        match(2, "Match each word of unit 106 to its meaning.",
              [["कषाय", "decoction"], ["कल्क", "paste"], ["द्वय", "pair"],
               ["मरिच", "black pepper"], ["भद्रदारु", "deodar (probable)"]],
              "Five words name the two forms and their drugs.",
              "कषाय, कल्क, द्वय, मरिच, भद्रदारु.", role="extend",
              teaches="द्वय at a compound's end means a pair: अंशुमतीद्वय = the aṃśumatī pair, two plants."),
        mcq("discriminate", 3, "What label does the data give the identity of the aṃśumatī pair?",
            ("Disputed: probably śālaparṇī and pṛśniparṇī", "The data calls the pair an interpretation, disputed."),
            [("Standard: śālaparṇī and pṛśniparṇī", "The text does not name them; the data does not call it standard."),
             ("Unidentified: no guess offered at all", "The data does offer a probable pair."),
             ("Probable: two kinds of black pepper", "Marica is named apart; the pair is not pepper.")],
            "Aṃśumatī pair: probably śālaparṇī and pṛśniparṇī; identity disputed.",
            "अंशुमतीद्वय: पहचान विवादित."),
        multi("apply", 4, "Which statements about unit 106 are right?",
              [("bhadradāru = deodar is labelled probable", "Right: the data labels it probable."),
               ("The text itself names śālaparṇī", "No: the pair's plants are an interpretation."),
               ("वा is printed joined to कषायेन", "Right: printed कषायेनवा."),
               ("A dose of the paste is stated", "No amount is stated.")],
              [0, 2],
              "Deodar is probable; the pair's plants are an interpretation; वा is printed joined.",
              "Keep the data's labels: probable, disputed."),
        mcq("transfer", 5, "Built like मरिचभद्रदारुकल्क, what does the new example शुण्ठीमरिचचूर्ण mean?",
            ("A powder of dry ginger and black pepper", "The last member names the form; the earlier ones the drugs."),
            [("A paste of dry ginger and black pepper", "चूर्ण is powder; कल्क would be paste."),
             ("A decoction of dry ginger and pepper", "चूर्ण is powder; कषाय would be decoction."),
             ("Dry ginger and pepper cooked in oil", "No oil (तैल) stands in the compound.")],
            "शुण्ठी + मरिच + चूर्ण: a powder of dry ginger and black pepper, like marica + bhadradāru + kalka.",
            "Drug names + कल्क / चूर्ण / कषाय: the last word names the form.",
            teaches="In drug compounds like मरिचभद्रदारुकल्क, the final member names the preparation and the earlier members its drugs."),
    ],
}

# ---------------------------------------------------------------- unit 107
AUTHORED["107"] = {
    "title": "भाईींनागरदेवदारुकल्कं वोष्णाम्भसा",
    "question": "By unit 107, which paste is taken, and with what?",
    "rule": ("Or a paste (कल्क) of an unclear first drug (printed भाईीं), nāgara (dry ginger) and devadāru (deodar), "
             "taken with warm water (उष्णाम्भसा). The verb is carried over."),
    "limits": ("Low confidence. भाईीं is not a word and cannot be restored; bhārṅgī is only a guess, not adopted. No "
               "question rests on the first drug. No amount is given."),
    "explain_hi": ("यह गद्य-पंक्ति एक और विकल्प देती है: भाईीं (अस्पष्ट शब्द), नागर यानी सोंठ और देवदारु का कल्क, गरम पानी के साथ। "
                   "पहला शब्द ‘भाईीं’ कोई शब्द नहीं; ‘भार्ङ्गी’ होना केवल अनुमान है, अपनाया नहीं गया। "
                   "क्रिया पहले से चली आ रही है। "
                   "सन्धि: वा + उष्ण → वोष्ण (आ + उ → ओ), उष्ण + अम्भसा → उष्णाम्भसा (अ + अ → आ)।"),
    "hook": "सोंठ-देवदारु का कल्क, गरम पानी से।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 107, with what is the paste taken?",
            ("With warm water", "उष्णाम्भसा = with warm water."),
            [("With madirā", "Madirā is the vehicle of unit 105."),
             ("With boiled cow milk", "No milk is named in unit 107."),
             ("With old ghee", "No ghee is named in unit 107.")],
            "The paste is taken with warm water.",
            "उष्ण + अम्भस् = warm water."),
        order(1, "Put these words of unit 107 in the line's order.",
              ["नागर", "देवदारु", "कल्कं", "वा", "उष्णाम्भसा"],
              "Nāgara, devadāru, paste, or, with warm water (after the unclear first word).",
              "नागर → देवदारु → कल्कं → वा → उष्णाम्भसा."),
        match(2, "Match each word of unit 107 to its meaning.",
              [["नागर", "dry ginger"], ["देवदारु", "deodar"], ["कल्क", "paste"],
               ["उष्ण", "warm"], ["अम्भस्", "water"]],
              "The sure words of unit 107.",
              "नागर, देवदारु, कल्क, उष्ण, अम्भस्.", role="extend",
              teaches="उष्णाम्भसा = उष्ण (warm) + अम्भसा (with water), instrumental: with warm water."),
        mcq("discriminate", 3, "Which split of वोष्णाम्भसा is right?",
            ("वा + उष्ण + अम्भसा", "आ + उ → ओ; अ + अ → आ."),
            [("वः + उष्ण + अम्भसा", "अः before उ loses its visarga: व उष्ण..., no ओ."),
             ("वो + उष्ण + अम्भसा", "ओ + उ would give अवु, not ओ."),
             ("वा + ओष्ण + अम्भसा", "आ + ओ would give औ, and ओष्ण is no word.")],
            "वा (or) + उष्ण (warm) + अम्भसा (with water).",
            "आ + उ → ओ; अ + अ → आ."),
        mcq("apply", 4, "In unit 107, which word tells the form in which the drugs are given?",
            ("कल्कं: as a paste", "कल्क = paste; the drug names stand before it."),
            [("नागर: as dry ginger", "नागर is one of the drugs, not the form."),
             ("उष्णाम्भसा: as warm water", "Warm water is the vehicle, not the form."),
             ("देवदारु: as deodar", "देवदारु is one of the drugs, not the form.")],
            "The drugs are given as a kalka (paste) with warm water.",
            "कल्क = the form; उष्णाम्भसा = the vehicle."),
        mcq("transfer", 5, "By the join वा + उष्ण → वोष्ण, how do वा + उदकेन (or with water) join in a new example?",
            ("वोदकेन", "आ + उ → ओ, as वा + उष्ण = वोष्ण."),
            [("वादकेन", "आ + उ does not drop the उ."),
             ("वौदकेन", "औ comes from आ + ओ or औ, not from आ + उ."),
             ("वूदकेन", "ऊ comes from उ + उ, not from आ + उ.")],
            "वा + उदकेन = वोदकेन, like वा + उष्णाम्भसा = वोष्णाम्भसा.",
            "आ + उ → ओ.",
            teaches="अ or आ followed by उ or ऊ joins as ओ: वा + उष्ण → वोष्ण."),
    ],
}

# ---------------------------------------------------------------- unit 108
AUTHORED["108"] = {
    "title": "पुराणगुडं वा ... भक्षयेत्",
    "question": "By unit 108, what should one eat, and mixed with what?",
    "rule": ("Or one should eat (भक्षयेत्) old jaggery (पुराणगुड) mixed with one powder of trikaṭu, trijātaka and dhanikā "
             "(probably coriander)."),
    "limits": ("Medium confidence. trikaṭu = dry ginger, black pepper, long pepper (standard); trijātaka = cinnamon bark, "
               "cardamom, bay leaf (standard); dhanikā is probably coriander (usual spelling dhānyaka). How old 'old' is, and "
               "any amount, are not stated."),
    "explain_hi": ("इस विकल्प की अपनी क्रिया है: ‘भक्षयेत्’ यानी खाना चाहिए। "
                   "पुराना गुड़ त्रिकटु, त्रिजातक और धनिका के चूर्ण में मिलाकर खाया जाए; तीनों का एक ही चूर्ण पढ़ा गया है। "
                   "त्रिकटु = सोंठ, मरिच, पीपर (मानक); त्रिजातक = दालचीनी, इलायची, तेजपात (मानक); धनिका = सम्भवतः धनिया। "
                   "गुड़ कितना पुराना हो और मात्रा कितनी, यह नहीं कहा गया।"),
    "hook": "पुराना गुड़ + तीन कटु + तीन सुगन्धि + धनिका (सम्भवतः धनिया): खाओ।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 108, what is eaten?",
            ("Old jaggery", "पुराणगुडं: old jaggery."),
            [("Fresh jaggery", "पुराण means old, not fresh."),
             ("Salt powder", "Salt powder is unit 104."),
             ("Yavakṣāra powder", "Yavakṣāra powder is unit 102.")],
            "Old jaggery, mixed with a powder, is eaten.",
            "पुराणगुड = old jaggery."),
        order(1, "Put these parts of unit 108 in the line's order.",
              ["पुराणगुडं वा", "त्रिकटु", "त्रिजातक", "धनिका", "चूर्णसंसृष्टं भक्षयेत्"],
              "Old jaggery, or; trikaṭu, trijātaka, dhanikā; mixed with the powder, one should eat.",
              "पुराणगुडं वा → त्रिकटु → त्रिजातक → धनिका → चूर्णसंसृष्टं भक्षयेत्."),
        match(2, "Match each name in unit 108 to what the data says it is.",
              [["त्रिकटु", "dry ginger, black pepper, long pepper"],
               ["त्रिजातक", "cinnamon bark, cardamom, bay leaf"],
               ["धनिका", "probably coriander"], ["पुराणगुड", "old jaggery"]],
              "Two standard groups of three, one probable plant, and the base.",
              "त्रिकटु, त्रिजातक, धनिका, पुराणगुड.", role="extend",
              teaches="त्रि- names a set of three: त्रिकटु the three pungents, त्रिजातक the three aromatics."),
        multi("discriminate", 3, "Which belong to trijātaka as the data gives it?",
              [("Cinnamon bark", "Right: one of the three aromatics."),
               ("Dry ginger", "Dry ginger is in trikaṭu, not trijātaka."),
               ("Bay leaf", "Right: one of the three aromatics."),
               ("Cardamom", "Right: one of the three aromatics."),
               ("Black pepper", "Black pepper is in trikaṭu, not trijātaka.")],
              [0, 2, 3],
              "Trijātaka = cinnamon bark, cardamom, bay leaf (standard).",
              "त्रिजातक: दालचीनी, इलायची, तेजपात."),
        mcq("apply", 4, "Which verb does unit 108 itself print?",
            ("भक्षयेत्: one should eat", "The line ends with its own verb, भक्षयेत्."),
            [("पिबेत्: one should drink", "A drinking verb (printed पिबेत) is in unit 102, not here."),
             ("दद्यात्: one should give", "दद्यात् is not printed in unit 108."),
             ("पाययेत्: should make drink", "पाययेत् is not printed in unit 108.")],
            "Unit 108 prints भक्षयेत्, should eat: the jaggery is eaten, not drunk.",
            "भक्षयेत् = should eat (optative)."),
        mcq("transfer", 5, "Built like पुराणगुड (old jaggery), what does the new example पुराणतैल mean?",
            ("Old oil", "पुराण qualifies the next word: old + oil, as old + jaggery."),
            [("Fresh oil", "पुराण means old, not fresh."),
             ("Oil with jaggery", "No गुड stands in पुराणतैल."),
             ("Oil cooked twice", "पुराण says old, not cooked twice.")],
            "पुराण + तैल = old oil, like पुराण + गुड = old jaggery.",
            "Adjective + noun in one compound (karmadhāraya): पुराणगुड.",
            teaches="In a karmadhāraya the first member describes the second: पुराणगुड = old jaggery."),
    ],
}

# ---------------------------------------------------------------- unit 109
AUTHORED["109"] = {
    "title": "तस्याश्चेत्स्वस्थानतो योनिर्भ्रश्येत्",
    "question": "What condition does unit 109 state?",
    "rule": ("If (चेत्) her yoni (female genital passage) should slip (भ्रश्येत्) from its own place (स्वस्थानतः). "
             "The line is an if-clause; its then-part follows in unit 110 (ततः)."),
    "limits": ("Prose, high confidence. The line gives only the condition, no treatment. Whether 'her' is the woman of "
               "units 101-108 is left open. The modern equivalent, prolapse of the genital passage or uterus, is probable "
               "and not stated in the text."),
    "explain_hi": ("यह गद्य-पंक्ति एक शर्त है: यदि उसकी योनि अपने स्थान से खिसक जाए। "
                   "‘चेत्’ = यदि; इसका ‘तब’ वाला भाग अगली इकाई ११० में ‘ततः’ से आता है। "
                   "‘उसकी’ से वही स्त्री अभिप्रेत है या नहीं, व्याकरण खुला छोड़ता है। "
                   "आधुनिक समकक्ष (योनि या गर्भाशय का बाहर खिसकना) सम्भावित है, ग्रन्थ में नहीं कहा गया। "
                   "सन्धि: तस्याः + चेत् → तस्याश्चेत्; स्वस्थानतः + योनिः → स्वस्थानतो योनिः; योनिः + भ्रश्येत् → योनिर्भ्रश्येत्।"),
    "hook": "चेत् = यदि: योनि अपने स्थान से खिसके तो...",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 109, what may slip from its own place?",
            ("The yoni", "योनिर्भ्रश्येत्: the yoni should slip."),
            [("The child", "No child is named in unit 109."),
             ("The aparā", "The aparā is not named in unit 109."),
             ("The belly", "No belly is named in unit 109.")],
            "The condition: her yoni slips from its own place.",
            "योनिः भ्रश्येत् = the yoni should slip."),
        order(1, "Put the words of unit 109 in the line's order.",
              ["तस्याः", "चेत्", "स्वस्थानतः", "योनिः", "भ्रश्येत्"],
              "Her, if, from its own place, the yoni, should slip.",
              "तस्याः → चेत् → स्वस्थानतः → योनिः → भ्रश्येत्."),
        match(2, "Match each word of unit 109 to its meaning.",
              [["तस्याः", "her"], ["चेत्", "if"], ["स्वस्थानतः", "from its own place"], ["भ्रश्येत्", "should slip"]],
              "These words make the whole condition.",
              "तस्याः, चेत्, स्वस्थानतः, भ्रश्येत्.", role="extend",
              teaches="-तः on a noun means from: स्वस्थानतः = from its own place."),
        mcq("discriminate", 3, "Which split of तस्याश्चेत् is right?",
            ("तस्याः + चेत्", "A visarga before च becomes श्: तस्याः + चेत् → तस्याश्चेत्."),
            [("तस्या + चेत्", "With no visarga, nothing would turn into श्."),
             ("तस्यै + चेत्", "ऐ before a consonant stays ऐ; it gives no आश्."),
             ("तस्याम् + चेत्", "म् before च becomes anusvāra or ञ्, not श्.")],
            "तस्याः (her) + चेत् (if): visarga → श् before च.",
            "Visarga before च / छ → श्."),
        mcq("apply", 4, "Why is स्वस्थानतः written स्वस्थानतो in unit 109?",
            ("अः before the voiced य becomes ओ", "स्वस्थानतः + योनिः → स्वस्थानतो योनिः."),
            [("A visarga becomes ओ before any sound", "Before a voiceless sound it does not become ओ."),
             ("आः before a voiced sound gives ओ", "After आ the visarga simply drops."),
             ("स्वस्थानतो is a separate word form", "The word is स्वस्थानतः; only the join changes it.")],
            "अः before a voiced consonant (here य) → ओ.",
            "अः + voiced consonant → ओ."),
        mcq("transfer", 5, "By the join योनिः + भ्रश्येत् → योनिर्भ्रश्येत्, how do अग्निः + दहति (fire burns) join?",
            ("अग्निर्दहति", "इः before a voiced sound → इर्, as योनिः → योनिर्."),
            [("अग्नि दहति", "Before a voiced sound a visarga drops only after आ (or after अ before a vowel other than अ)."),
             ("अग्नो दहति", "ओ comes from अः, not from इः."),
             ("अग्निश्दहति", "श् comes only before च, छ or श.")],
            "अग्निः + दहति = अग्निर्दहति, like योनिः + भ्रश्येत् = योनिर्भ्रश्येत्.",
            "Visarga after a vowel other than अ / आ → र् before a voiced sound.",
            teaches="A visarga after इ, उ (or any vowel but अ / आ) becomes र् before a voiced sound: योनिः + भ्रश्येत् → योनिर्भ्रश्येत्."),
    ],
}

# ---------------------------------------------------------------- unit 110
AUTHORED["110"] = {
    "title": "ततो यस्य कस्यचिच्छोणितेन",
    "question": "By unit 110, how is the slipped yoni put back?",
    "rule": ("Then (ततः), having anointed the yoni with the blood of anyone whatever (यस्य कस्यचित्), a skilled woman "
             "(कुशला स्त्री) should place it back in its proper place (यथास्थानम्)."),
    "limits": ("Prose, medium confidence. Whose blood (animal or person) is not stated: यस्य कस्यचित् is one indefinite "
               "expression, anyone whatever. No further method is given. The line is the then-part of unit 109."),
    "explain_hi": ("यह इकाई ११० पिछली शर्त का ‘तब’ है: तब किसी के भी रक्त से योनि को चुपड़कर कुशल स्त्री उसे यथास्थान बैठा दे। "
                   "‘यस्य कस्यचित्’ मिलकर एक अनिश्चय-वाचक अभिव्यक्ति है: जिस किसी का भी; किस पशु या व्यक्ति का, नहीं कहा। "
                   "‘अभ्यज्य’ पूर्वकालिक रूप है: चुपड़कर। "
                   "सन्धि: कस्यचित् + शोणितेन → कस्यचिच्छोणितेन (त् + श → च्छ); शोणितेन + अभ्यज्य → शोणितेनाभ्यज्य (अ + अ → आ)।"),
    "hook": "किसी का भी रक्त लगाकर, कुशल स्त्री यथास्थान बैठाए।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 110, who should place the yoni back?",
            ("A skilled woman", "कुशला स्त्री निवेशयेत्: a skilled woman should place it back."),
            [("The attending physician", "No physician is named in unit 110."),
             ("Her husband", "No husband is named in unit 110."),
             ("Any servant", "The line says skilled woman, not any servant.")],
            "कुशला स्त्री: a skilled woman does it.",
            "कुशला स्त्री = a skilled woman."),
        order(1, "Put the parts of unit 110 in the line's order.",
              ["ततो", "यस्य कस्यचिच्छोणितेन", "अभ्यज्य योनिं", "यथास्थानं", "कुशला स्त्री निवेशयेत्"],
              "Then, with the blood of anyone whatever, having anointed the yoni, in its proper place, a skilled woman should place it.",
              "ततो → यस्य कस्यचिच्छोणितेन → अभ्यज्य योनिं → यथास्थानं → कुशला स्त्री निवेशयेत्."),
        match(2, "Match each word of unit 110 to its meaning.",
              [["शोणित", "blood"], ["अभ्यज्य", "having anointed"], ["यथास्थानम्", "in its proper place"],
               ["कुशला", "skilled"], ["निवेशयेत्", "should place back"]],
              "Five words carry the procedure.",
              "शोणित, अभ्यज्य, यथास्थानम्, कुशला, निवेशयेत्.", role="extend",
              teaches="यथा + स्थानम् = यथास्थानम्, an indeclinable compound: according to (its) place."),
        mcq("discriminate", 3, "Which split of कस्यचिच्छोणितेन is right?",
            ("कस्यचित् + शोणितेन", "त् + श → च्श / च्छ (optional, before a vowel); the print has च्छ: कस्यचित् + शोणितेन → कस्यचिच्छोणितेन."),
            [("कस्यचित् + छोणितेन", "छोणित is no word; the word is शोणित, blood."),
             ("कस्यचि + च्छोणितेन", "कस्यचि is no form; the pronoun is कस्यचित्."),
             ("कस्यचिच्छ + ओणितेन", "ओणित is no word; the word is शोणित.")],
            "कस्यचित् (of anyone) + शोणितेन (with blood).",
            "त् + श → च्श, and optionally च्छ before a vowel or semivowel (as printed: च्छ)."),
        mcq("apply", 4, "In unit 110, what does यस्य कस्यचित् tell about the blood used?",
            ("Of anyone whatever: no source named", "One indefinite expression: of anyone at all."),
            [("Of the woman herself, only", "The line does not say her own blood."),
             ("Of a goat, freshly killed", "No animal is named in unit 110."),
             ("Of the child, at birth", "No child is named in unit 110.")],
            "The source of the blood is left open: anyone whatever.",
            "यस्य कस्यचित् = of anyone whatever."),
        mcq("transfer", 5, "Built like अभ्यज्य (prefix + root → -य), what is the absolutive of नि + विश् (having entered)?",
            ("निविश्य", "With a prefix, the absolutive ends in -य: नि + विश् → निविश्य."),
            [("निविष्ट्वा", "-त्वा is used without a prefix, not with नि."),
             ("निविशित्वा", "-त्वा is not used after a prefix like नि."),
             ("निविशय", "The ending is -य directly on the root: निविश्य.")],
            "नि + विश् → निविश्य, like अभि + अञ्ज् → अभ्यज्य.",
            "Prefix + root → absolutive in -य; plain root → -त्वा.",
            teaches="An absolutive with a prefix ends in -य (अभ्यज्य, having anointed); a plain root takes -त्वा."),
    ],
}

# ---------------------------------------------------------------- unit 111
AUTHORED["111"] = {
    "title": "निविष्टां चाशोकरोहिणी...तैलेन",
    "question": "By unit 111, what is done once the yoni is placed back?",
    "rule": ("The placed yoni (निविष्टाम्) is fomented many times (बहुशः स्वेदयेत्) and filled (पूरयेत्), with oil well "
             "cooked (विपक्व) with a paste of aśoka, rohiṇī, barhiṣa, uśīra, priyaṅgu and devadāru."),
    "limits": ("Medium confidence. rohiṇī is disputed; barhiṣa is unidentified and the division of बर्हिषोशीर may go another "
               "way; priyaṅgu is probably Callicarpa macrophylla (disputed). What is filled is not stated, and the oil may go "
               "with filling rather than, or as well as, fomenting. No question rests on these points."),
    "explain_hi": ("स्थापित की गई योनि (निविष्टाम्, स्त्रीलिंग, योनि से मेल) को तेल से बार-बार स्वेदन करना और भरना चाहिए। "
                   "तेल अशोक (मानक), रोहिणी (विवादित), बर्हिष (अज्ञात), उशीर यानी खस (मानक), प्रियङ्गु (सम्भवतः फूलप्रियंगु, विवादित) "
                   "और देवदारु के कल्क से भली प्रकार पकाया गया है। "
                   "क्या भरना है, यह नहीं कहा; तेल केवल भरने के साथ भी जा सकता है। "
                   "‘बर्हिषोशीर’ का विभाग दूसरी तरह भी हो सकता है, इसलिए उस पर प्रश्न नहीं।"),
    "hook": "द्रव्यों के कल्क से पका तेल: बार-बार स्वेदन और भरना।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 111, what is cooked with the paste of the listed drugs?",
            ("Oil (तैल)", "...कल्कविपक्वेन तैलेन: oil well cooked with the paste."),
            [("Ghee (घृत)", "No ghee is named in unit 111."),
             ("Milk (क्षीर)", "No milk is named in unit 111."),
             ("Madirā", "Madirā belongs to unit 105.")],
            "The paste of the listed drugs is cooked into oil.",
            "कल्कविपक्व तैल = oil cooked with a paste."),
        order(1, "Put these drugs of unit 111 in the line's order.",
              ["अशोक", "रोहिणी", "उशीर", "प्रियङ्गु", "देवदारु"],
              "Aśoka, rohiṇī, (barhiṣa), uśīra, priyaṅgu, devadāru.",
              "अशोक → रोहिणी → उशीर → प्रियङ्गु → देवदारु."),
        match(2, "Match each drug of unit 111 to the label its data gives.",
              [["अशोक", "Saraca asoca (standard)"], ["उशीर", "vetiver (standard)"],
               ["रोहिणी", "identity disputed"], ["प्रियङ्गु", "probably Callicarpa macrophylla (disputed)"]],
              "Two standard, two disputed identifications.",
              "अशोक, उशीर: standard; रोहिणी, प्रियङ्गु: disputed.", role="extend",
              teaches="Keep each plant's label: standard (aśoka, uśīra), disputed (rohiṇī, priyaṅgu), unidentified (barhiṣa)."),
        mcq("discriminate", 3, "Which split of चाशोक is right?",
            ("च + अशोक", "अ + अ → आ: च + अशोक → चाशोक."),
            [("चा + शोक", "चा is no word; the particle is च."),
             ("चे + अशोक", "ए + अ keeps ए and marks ऽ: चेऽशोक."),
             ("चः + अशोक", "अः + अ gives ओऽ: चोऽशोक, not चाशोक.")],
            "च (and) + अशोक (aśoka): अ + अ → आ.",
            "अ + अ → आ."),
        multi("apply", 4, "Which statements does unit 111 support?",
              [("Rohiṇī is firmly identified", "No: its identity is disputed."),
               ("The fomenting is done many times", "Right: बहुशः, many times."),
               ("The material for filling is named", "No: the object of पूरयेत् is not stated."),
               ("The oil is well cooked with a paste", "Right: कल्कविपक्वेन तैलेन.")],
              [1, 3],
              "Many times; oil cooked with a paste; what is filled is not said; rohiṇī disputed.",
              "बहुशः = many times; विपक्व = well cooked."),
        mcq("transfer", 5, "Built like निविष्टां (agreeing with योनि), which form fits ____ नारीम् (the seated woman, accusative)?",
            ("उपविष्टाम्", "Feminine accusative singular, like निविष्टाम् with योनिम्."),
            [("उपविष्टम्", "-अम् is masculine or neuter; नारी is feminine."),
             ("उपविष्टा", "उपविष्टा is nominative; नारीम् is accusative."),
             ("उपविष्टाः", "उपविष्टाः is plural; नारीम् is singular.")],
            "उपविष्टाम् नारीम्, like निविष्टाम् (योनिम्): same gender, case and number.",
            "A participle agrees with its noun in gender, case and number.",
            teaches="A past participle in -त agrees with its noun: नि + विश् + त → निविष्ट, and निविष्टाम् is feminine accusative singular, like योनिम्."),
    ],
}

# ---------------------------------------------------------------- unit 112
AUTHORED["112"] = {
    "title": "ब्रूयाच्च गच्छ सुभगे स्वस्थानमिति",
    "question": "By unit 112, what words should be said?",
    "rule": ("And one should say (ब्रूयात्): 'Go, O fortunate one (सुभगे), to your own place (स्वस्थानम्)'. "
             "इति closes the quotation."),
    "limits": ("Prose, high confidence. Neither the speaker nor the one addressed is stated (the addressee is probably the "
               "yoni, not stated). No question on who speaks or who is addressed."),
    "explain_hi": ("और कहना चाहिए: ‘हे सुभगे, अपने स्थान को जाओ।’ "
                   "‘इति’ उद्धरण का अन्त दिखाता है। "
                   "कौन कहे और किससे कहे, यह नहीं बताया गया; सम्बोधन सम्भवतः योनि से है, पर लिखा नहीं। "
                   "सन्धि: ब्रूयात् + च → ब्रूयाच्च (त् + च → च्च); स्वस्थानम् + इति → स्वस्थानमिति।"),
    "hook": "‘गच्छ सुभगे स्वस्थानम्’: अपनी जगह जाओ।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 112, what do the spoken words tell the one addressed?",
            ("To go to your own place", "गच्छ ... स्वस्थानम्: go to your own place."),
            [("To stay quite still", "No word for staying still is spoken."),
             ("To come out of the body quickly", "The words say go to your own place."),
             ("To grow strong again", "No word for strength is spoken.")],
            "The words: Go, O fortunate one, to your own place.",
            "गच्छ स्वस्थानम् = go to your own place."),
        order(1, "Put the words of unit 112 in the line's order.",
              ["ब्रूयात्", "च", "गच्छ", "सुभगे", "स्वस्थानम्", "इति"],
              "One should say, and: go, O fortunate one, to your own place, (end of quote).",
              "ब्रूयात् → च → गच्छ → सुभगे → स्वस्थानम् → इति."),
        match(2, "Match each word of unit 112 to its meaning.",
              [["ब्रूयात्", "should say"], ["गच्छ", "go"], ["सुभगे", "O fortunate one"],
               ["स्वस्थानम्", "to your own place"], ["इति", "closes the quotation"]],
              "Five words: the saying and the words said.",
              "ब्रूयात्, गच्छ, सुभगे, स्वस्थानम्, इति.", role="extend",
              teaches="इति after spoken words closes the quotation: ... स्वस्थानम् इति."),
        mcq("discriminate", 3, "Which split of ब्रूयाच्च is right?",
            ("ब्रूयात् + च", "त् + च → च्च: ब्रूयात् + च → ब्रूयाच्च."),
            [("ब्रूयाः + च", "A visarga before च gives श्च: ब्रूयाश्च."),
             ("ब्रूया + च्च", "च्च is no word; the particle is च."),
             ("ब्रूयाम् + च", "म् before च gives anusvāra: ब्रूयां च.")],
            "ब्रूयात् (should say) + च (and): त् + च → च्च.",
            "त् + च → च्च."),
        mcq("apply", 4, "In unit 112, what does इति do?",
            ("Marks the end of the quoted words", "इति closes the quotation गच्छ सुभगे स्वस्थानम्."),
            [("It is the verb meaning go", "The verb go is गच्छ."),
             ("It names who does the speaking", "The speaker is not named."),
             ("It means also, like the word च", "च means and; इति closes a quote.")],
            "इति marks where the spoken words end.",
            "इति = end of a quotation."),
        mcq("transfer", 5, "By the join ब्रूयात् + च → ब्रूयाच्च, how do तत् + च (and that) join?",
            ("तच्च", "त् + च → च्च, as ब्रूयात् + च = ब्रूयाच्च."),
            [("तद्च", "त् → द् happens before voiced sounds; च is voiceless."),
             ("तञ्च", "ञ्च would need a nasal, and तत् has none."),
             ("तश्च", "श्च comes from a visarga before च, not from त्.")],
            "तत् + च = तच्च, like ब्रूयात् + च = ब्रूयाच्च.",
            "त् + च → च्च.",
            teaches="A final त् becomes च् before च: ब्रूयात् + च → ब्रूयाच्च."),
    ],
}

# ---------------------------------------------------------------- unit 113
AUTHORED["113"] = {
    "title": "तद्वच्चान्यतमा स्त्रीजातमात्रमेव बालं",
    "question": "By unit 113, who is to deal with the just-born child, and in what way?",
    "rule": ("In the same way (तद्वत्), any one woman (अन्यतमा स्त्री) deals with the child just born (जातमात्रं बालम्) by "
             "the procedure for the care of a child (बालोपचरणीय). The verb is damaged."),
    "limits": ("Low confidence. The printed verb विथिनोप्पादयेत् is read conjecturally as विधिना उत्पादयेत् (should bring forth); "
               "उपचरेत् or similar is also possible. स्त्रीजातमात्रम् may also read born of a woman only. No question on the "
               "verb, on विधिना, or on how स्त्री and जातमात्र are divided."),
    "explain_hi": ("उसी प्रकार (तद्वत्) कोई एक स्त्री (अन्यतमा) अभी जन्मे बालक के साथ बालक के उपचार की विधि से काम करे। "
                   "छपी क्रिया ‘विथिनोप्पादयेत्’ क्षतिग्रस्त है; ‘विधिना उत्पादयेत्’ (उत्पन्न करे) अनुमानित पाठ है, "
                   "‘उपचरेत्’ जैसा पाठ भी सम्भव। "
                   "‘अन्यतमा’ = कई में से कोई एक, ‘दूसरी’ नहीं। "
                   "‘स्त्रीजातमात्रम्’ को स्त्री + जातमात्रम् पढ़ा गया; ‘केवल स्त्री से जन्मा’ भी सम्भव है।"),
    "hook": "कोई एक स्त्री, नवजात बालक, बाल-उपचार की विधि।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "In unit 113, what does अन्यतमा mean?",
            ("Any one of several", "अन्यतम = one of several; feminine अन्यतमा: any one (woman)."),
            [("Another, a different one", "The data says अन्यतम is not other here."),
             ("The eldest of them all", "No age is in the word अन्यतमा."),
             ("All of them together", "अन्यतमा is singular: any one.")],
            "अन्यतमा = any one (of several women).",
            "अन्यतम = one of several, not other."),
        order(1, "Put the printed words of unit 113 in their order.",
              ["तद्वच्चान्यतमा", "स्त्रीजातमात्रमेव", "बालं", "बालोपचरणीयेन", "विथिनोप्पादयेत्"],
              "In the same way any one | woman, the just-born (child) only | the child | for the care of a child | (damaged verb).",
              "तद्वच्चान्यतमा → स्त्रीजातमात्रमेव → बालं → बालोपचरणीयेन → विथिनोप्पादयेत्."),
        match(2, "Match each word of unit 113 to its meaning.",
              [["तद्वत्", "in the same way"], ["अन्यतमा", "any one (of several)"],
               ["बालम्", "the child"], ["बालोपचरणीय", "for the care of a child"]],
              "The sure words of unit 113.",
              "तद्वत्, अन्यतमा, बालम्, बालोपचरणीय.", role="extend",
              teaches="-वत् means like, in the manner of: तत् + वत् = तद्वत्, in the same way."),
        mcq("discriminate", 3, "Which split of बालोपचरणीयेन is right?",
            ("बाल + उपचरणीयेन", "अ + उ → ओ: बाल + उपचरणीयेन → बालोपचरणीयेन."),
            [("बालो + पचरणीयेन", "पचरणीय is no word; the word is उपचरणीय."),
             ("बालः + उपचरणीयेन", "अः before उ loses its visarga: बाल उपचरणीयेन, two words."),
             ("बाले + उपचरणीयेन", "ए before उ gives अय् or अ; it gives no ओ.")],
            "बाल (child) + उपचरणीयेन (for the care): अ + उ → ओ.",
            "अ + उ → ओ."),
        mcq("apply", 4, "In unit 113, what case is बालं, and what is its role?",
            ("Accusative: the child is the object", "बालम्, m. acc. sg.: the one dealt with."),
            [("Nominative: the child is the doer", "The nominative would be बालः."),
             ("Instrumental: together with the child", "The instrumental would be बालेन."),
             ("Genitive: of the child", "The genitive would be बालस्य.")],
            "बालम् = the child, object of the (damaged) verb.",
            "अ-stem masculine accusative singular: -अम्."),
        mcq("transfer", 5, "Built like तद्वत् (like that), what does the new example पूर्ववत् mean?",
            ("As before", "पूर्व (former) + वत् (like): like the former, as before."),
            [("After that", "वत् means like, not after."),
             ("Not as before", "वत् carries no not."),
             ("Before birth", "No word for birth stands in पूर्ववत्.")],
            "पूर्व + वत् = as before, like तत् + वत् = in the same way.",
            "-वत् = like, in the manner of.",
            teaches="-वत् added to a word means like it: तद्वत् = like that, in the same way."),
    ],
}

# ---------------------------------------------------------------- unit 114
AUTHORED["114"] = {
    "title": "तमुपदेक्ष्यते तूत्तरेषु",
    "question": "What does unit 114 say about 'that' (तम्)?",
    "rule": "But that (तम्) will be taught (उपदेक्ष्यते, future) in the later (ones, उत्तरेषु).",
    "limits": ("Prose, medium confidence. Which later ones (probably the later sthānas, especially Uttarasthāna) is an "
               "interpretation, not stated. तम् may mean the procedure or the child; the verb can be read active or passive. "
               "No question on what तम् refers to or on which section is meant."),
    "explain_hi": ("यह छोटी गद्य-पंक्ति कहती है: उसका उपदेश तो आगे वालों में किया जाएगा। "
                   "‘उपदेक्ष्यते’ भविष्यत् काल है। "
                   "‘उत्तरेषु’ से सम्भवतः आगे के स्थान, विशेषकर उत्तरस्थान, अभिप्रेत हैं; यह व्याख्या है, ग्रन्थ में नहीं कहा। "
                   "‘तम्’ विधि के लिए है या बालक के लिए, यह खुला है। "
                   "सन्धि: तम् + उपदेक्ष्यते → तमुपदेक्ष्यते; तु + उत्तरेषु → तूत्तरेषु (उ + उ → ऊ)।"),
    "hook": "विस्तार आगे: उत्तरेषु।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 114, when will that be taught?",
            ("Later, in the later ones", "उपदेक्ष्यते ... उत्तरेषु: will be taught in the later (ones)."),
            [("Here, in this same line", "The verb is future: it is not taught here."),
             ("It was already taught earlier on", "The verb is future, not past."),
             ("It will never be taught", "The line says it will be taught.")],
            "The teaching is postponed to the later (ones).",
            "उपदेक्ष्यते = will be taught (future)."),
        order(1, "Put the words of unit 114 in the line's order.",
              ["तम्", "उपदेक्ष्यते", "तु", "उत्तरेषु"],
              "That, will be taught, but, in the later (ones).",
              "तम् → उपदेक्ष्यते → तु → उत्तरेषु."),
        match(2, "Match each word of unit 114 to its meaning.",
              [["तम्", "that"], ["उपदेक्ष्यते", "will be taught"], ["तु", "but"], ["उत्तरेषु", "in the later (ones)"]],
              "Four words make the line.",
              "तम्, उपदेक्ष्यते, तु, उत्तरेषु.", role="extend",
              teaches="उत्तरेषु is locative plural of उत्तर, later: in the later (ones)."),
        mcq("discriminate", 3, "Which split of तूत्तरेषु is right?",
            ("तु + उत्तरेषु", "उ + उ → ऊ: तु + उत्तरेषु → तूत्तरेषु."),
            [("तू + त्तरेषु", "त्तरेषु is no word; the word is उत्तरेषु."),
             ("ते + उत्तरेषु", "ए + उ gives अय् or अ; it gives no ऊ."),
             ("तो + उत्तरेषु", "ओ + उ gives अव् or अ; it gives no ऊ.")],
            "तु (but) + उत्तरेषु (in the later ones): उ + उ → ऊ.",
            "उ + उ → ऊ."),
        mcq("apply", 4, "Which tense label does the data give उपदेक्ष्यते?",
            ("Future", "The data labels it 3 sg. fut. mid. of upa-√diś."),
            [("Present", "A present would be उपदिशति / उपदिश्यते."),
             ("Perfect", "A perfect would be उपदिदेश."),
             ("Optative", "An optative would be उपदिशेत्.")],
            "-स्य- marks the future: उपदेक्ष्यते, will be taught.",
            "उपदेक्ष्यते = future."),
        mcq("transfer", 5, "By the join तु + उत्तरेषु → तूत्तरेषु, how do मधु + उदकम् join in a new example?",
            ("मधूदकम्", "उ + उ → ऊ, as तु + उत्तरेषु = तूत्तरेषु."),
            [("मध्वुदकम्", "उ → व् only before a different vowel."),
             ("मधोदकम्", "ओ comes from अ + उ, not from उ + उ."),
             ("मधौदकम्", "औ comes from अ + ओ, not from उ + उ.")],
            "मधु + उदकम् = मधूदकम्, like तु + उत्तरेषु = तूत्तरेषु.",
            "उ + उ → ऊ.",
            teaches="Two like vowels merge into the long one: उ + उ → ऊ (तु + उत्तरेषु → तूत्तरेषु)."),
    ],
}

# ---------------------------------------------------------------- unit 115
AUTHORED["115"] = {
    "title": "अथ सूतिकां बलातैलेनाभ्यज्यात्",
    "question": "By unit 115, how is the sūtikā then cared for?",
    "rule": ("Then (अथ) one should anoint the sūtikā (woman who has recently given birth) with balā oil (बलातैल; balā "
             "probably country mallow, Sida cordifolia)."),
    "limits": ("Prose, medium confidence. balā = Sida cordifolia is probable (several plants are called balā). Who anoints, "
               "how often, and how the oil is made are not stated here."),
    "explain_hi": ("यहाँ से सूतिका-परिचर्या आरम्भ होती है: फिर प्रसूता यानी सूतिका को बलातैल से अभ्यंग करना चाहिए। "
                   "बला = सम्भवतः बरियार (Sida cordifolia); कई पौधे ‘बला’ कहलाते हैं, इसलिए पहचान सम्भावित है। "
                   "कौन अभ्यंग करे, कितनी बार, तेल कैसे बने, यह यहाँ नहीं कहा। "
                   "सन्धि: बलातैलेन + अभ्यज्यात् → बलातैलेनाभ्यज्यात् (अ + अ → आ)।"),
    "hook": "अथ: सूतिका को बलातैल से अभ्यंग।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 115, with what is the sūtikā anointed?",
            ("Balā oil", "बलातैलेन: with balā oil."),
            [("Plain ghee", "No ghee is named in unit 115."),
             ("Warm water", "Water is not named in unit 115."),
             ("Mustard oil", "The oil named is balā oil.")],
            "The sūtikā is anointed with balā oil.",
            "बलातैल = balā oil."),
        order(1, "Put the words of unit 115 in the line's order.",
              ["अथ", "सूतिकां", "बलातैलेन", "अभ्यज्यात्"],
              "Then, the sūtikā, with balā oil, one should anoint.",
              "अथ → सूतिकां → बलातैलेन → अभ्यज्यात्."),
        fill(2, "Then one should anoint the ____ (woman who has recently given birth) with balā oil (type it in Devanagari or in English letters, e.g. dharma).",
             accepts("सूतिकाम्", None, "सूतिका", "sutikam", "sutika"),
             "The line is अथ सूतिकां बलातैलेनाभ्यज्यात्.",
             "सूतिका = a woman who has recently given birth; सूतिकाम् is its accusative.",
             "सूतिकाम् = the sūtikā (object)."),
        mcq("discriminate", 3, "Which split of बलातैलेनाभ्यज्यात् is right?",
            ("बलातैलेन + अभ्यज्यात्", "अ + अ → आ: बलातैलेन + अभ्यज्यात्."),
            [("बलातैलेन + भ्यज्यात्", "भ्यज्यात् is no verb; the verb is अभ्यज्यात्."),
             ("बलातैलेने + अभ्यज्यात्", "ए + अ keeps ए with ऽ: ...तैलेनेऽभ्यज्यात्."),
             ("बलातैलेनः + अभ्यज्यात्", "अः + अ gives ओऽ, not आ.")],
            "बलातैलेन (with balā oil) + अभ्यज्यात् (should anoint).",
            "अ + अ → आ."),
        mcq("apply", 4, "Which label does the data give balā = country mallow here?",
            ("Probable", "Several plants are called balā, so Sida cordifolia is probable."),
            [("Standard", "The data does not call it standard here."),
             ("Disputed", "The data says probable, not disputed."),
             ("Unidentified", "The data does give an identification.")],
            "balā = Sida cordifolia: probable.",
            "बला: सम्भावित पहचान."),
        mcq("transfer", 5, "By the join बलातैलेन + अभ्यज्यात्, how do घृतेन + अभ्यज्य (having anointed with ghee) join?",
            ("घृतेनाभ्यज्य", "अ + अ → आ, as बलातैलेन + अभ्यज्यात्."),
            [("घृतेनोभ्यज्य", "ओ comes from अ + उ, not from अ + अ."),
             ("घृतेनेभ्यज्य", "ए comes from अ + इ, not from अ + अ."),
             ("घृतेनैभ्यज्य", "ऐ comes from अ + ए, not from अ + अ.")],
            "घृतेन + अभ्यज्य = घृतेनाभ्यज्य, like बलातैलेन + अभ्यज्यात् = बलातैलेनाभ्यज्यात्.",
            "अ + अ → आ.",
            teaches="A final अ and an initial अ merge into one long आ: बलातैलेन + अभ्यज्यात् → बलातैलेनाभ्यज्यात्."),
    ],
}


# ===================================================================== NOTES_HI
NOTES_HI = {
    "103": ("दो छपी पंक्तियाँ जुड़ी हैं [02.03.111, 02.03.112]; विश्वास निम्न। पाठ-चिह्न: ‘सपंचकोलमेलामतीवापं’ — ‘अतीवाप’ ज्ञात शब्द नहीं; "
            "छपी पंक्ति 112 (कार्ड 103) में ‘प्रतीवाप’ है, इसलिए ‘अति’ सम्भवतः ‘प्रति’ हो, पर अपनाया नहीं। ‘मेलाम्’ = पञ्चकोलम् + एलाम्; "
            "एला अलग द्रव्य है या जोड़, वाक्य-रचना अनिश्चित। दूसरी पंक्ति का समास खुला: एक या दोनों गण प्रतीवाप। "
            "‘मूषक’ सम्भवतः ‘मुष्कक’ का छापा-दोष (अपनाया नहीं)। गणों के सदस्य यहाँ नहीं दिए। क्रिया ‘पिबेत्’ कार्ड 102 से। "
            "सन्धि जाँची: वरण + आदिम् → वरणादिम् (अ + आ → आ)।"),
    "104": ("गद्य; विश्वास मध्यम। पाठ-चिह्न: ‘वावत्सकादिनिर्यूहेण’ — ‘वा’ बिना अन्तराल छपा, ‘वा वत्सकादि...’ पढ़ा गया। कौन-सा लवण, नहीं कहा। "
            "क्रिया अध्याहृत। व्याकरण: निर्यूहेण में र् के बाद न → ण (णत्व)। सन्धि जाँची: वत्सक + आदि → वत्सकादि।"),
    "105": ("गद्य; विश्वास मध्यम; कोई पाठ-चिह्न नहीं। क्रिया अध्याहृत। मदिरया = मदिरा की तृतीया एकवचन। "
            "सन्धि जाँची: वत्सक + आदिम् → वत्सकादिम्; छपा ‘वत्सकादिं’ (अनुस्वार)।"),
    "106": ("गद्य; विश्वास निम्न। पाठ-चिह्न: ‘कषायेनवा’ — कषायेन + वा, बिना अन्तराल। ‘वा’ कषायेन के बाद है, इसलिए दूसरा अर्थ भी सम्भव: "
            "मरिच-भद्रदारु कल्क, अंशुमती-द्वय के काढ़े के साथ; छपा क्रम रखा गया। अंशुमती-द्वय के दो पौधे (शालपर्णी, पृश्निपर्णी) व्याख्या हैं, "
            "विवादित। भद्रदारु = देवदारु सम्भावित। व्याकरण-टिप्पणी: णत्व-नियम से ‘कषायेण’ अपेक्षित है (ष के बाद); छपा ‘कषायेन’ — इस पर प्रश्न नहीं।"),
    "107": ("गद्य; विश्वास निम्न। पाठ-चिह्न: ‘भाईीं’ शब्द नहीं, अपुनर्स्थाप्य; ‘भार्ङ्गी’ केवल अनुमान, अपनाया नहीं। शेष समास सूची के रूप में अनूदित। "
            "क्रिया अध्याहृत। सन्धि जाँची: वा + उष्ण → वोष्ण (आ + उ → ओ); उष्ण + अम्भसा → उष्णाम्भसा (अ + अ → आ)।"),
    "108": ("गद्य; विश्वास मध्यम; कोई पाठ-चिह्न नहीं। ‘त्रिकटु-त्रिजातक-धनिका-चूर्ण’ = तीनों का द्वन्द्व, फिर एक चूर्ण। धनिका का सामान्य रूप धान्यक; "
            "धनिया सम्भावित। ‘संसृष्टम्’ पुराणगुडम् से मेल खाता है (पुं. द्वितीया)। अपनी क्रिया: भक्षयेत्।"),
    "109": ("गद्य; विश्वास उच्च; कोई पाठ-चिह्न नहीं। केवल शर्त (चेत्); फल कार्ड 110 में (ततः)। ‘तस्याः’ पिछली स्त्री है या नहीं, खुला। "
            "आधुनिक समकक्ष (योनि-भ्रंश / प्रोलैप्स) सम्भावित, ग्रन्थ में नहीं। सन्धि जाँची: तस्याः + चेत् → तस्याश्चेत्; "
            "स्वस्थानतः + योनिः → स्वस्थानतो योनिः (अः → ओ घोष से पहले); योनिः + भ्रश्येत् → योनिर्भ्रश्येत् (इः → इर्)।"),
    "110": ("गद्य; विश्वास मध्यम; कोई पाठ-चिह्न नहीं। ‘यस्य कस्यचित्’ एक अनिश्चय-वाचक अभिव्यक्ति; किसका रक्त, नहीं कहा। छपा ‘अभ्यज्ययोनिं’ जुड़ा। "
            "सन्धि जाँची: ततः + यस्य → ततो यस्य; कस्यचित् + शोणितेन → कस्यचिच्छोणितेन (त् + श → च्छ); शोणितेन + अभ्यज्य → शोणितेनाभ्यज्य।"),
    "111": ("गद्य; विश्वास मध्यम। पाठ-चिह्न: ‘स्वेदयेत्पूरयेत्’ बिना अन्तराल। ‘बर्हिषोशीर’ = बर्हिष + उशीर (अ + उ → ओ) छपे के अनुसार; "
            "दूसरा विभाग सम्भव, बर्हिष अज्ञात — प्रश्न नहीं। रोहिणी विवादित, प्रियङ्गु विवादित। पूरयेत् का कर्म नहीं कहा; ‘तैलेन’ पूरयेत् के साथ भी "
            "जा सकता है। सन्धि जाँची: च + अशोक → चाशोक (अ + अ → आ)। निविष्टाम् स्त्रीलिंग, योनि से मेल।"),
    "112": ("गद्य; विश्वास उच्च; कोई पाठ-चिह्न नहीं। वक्ता और सम्बोधित (सम्भवतः योनि) नहीं बताए। ‘इति’ उद्धरण-समाप्ति। "
            "सन्धि जाँची: ब्रूयात् + च → ब्रूयाच्च (त् + च → च्च); स्वस्थानम् + इति → स्वस्थानमिति।"),
    "113": ("गद्य; विश्वास निम्न। पाठ-चिह्न: ‘विथिनोप्पादयेत्’ — विधिना + उत्पादयेत् अनुमानित (थ → ध, प्प → त्प); ‘उपचरेत्’ जैसा भी सम्भव। "
            "‘स्त्रीजातमात्रमेव’ = स्त्री + जातमात्रम् + एव, या ‘केवल स्त्री से जन्मा’। अन्यतमा = कई में से एक। "
            "सन्धि जाँची: तद्वत् + च → तद्वच्च; च + अन्यतमा → चान्यतमा; बाल + उपचरणीय → बालोपचरणीय (अ + उ → ओ)।"),
    "114": ("गद्य; विश्वास मध्यम; कोई पाठ-चिह्न नहीं। ‘उत्तरेषु’ = आगे वालों में, सम्भवतः आगे के स्थान (उत्तरस्थान) — व्याख्या। ‘तम्’ विधि या बालक; "
            "कर्मवाच्य मानें तो द्वितीया ‘तम्’ असामान्य। सन्धि जाँची: तम् + उपदेक्ष्यते → तमुपदेक्ष्यते; तु + उत्तरेषु → तूत्तरेषु (उ + उ → ऊ)।"),
    "115": ("गद्य; विश्वास मध्यम; कोई पाठ-चिह्न नहीं। बला = Sida cordifolia सम्भावित। छपा ‘अभ्यज्यात्’ डेटा में √अञ्ज् का विधिलिङ् माना गया "
            "(नियमित रूप अभ्यञ्ज्यात् होता) — इस पर प्रश्न नहीं। सन्धि जाँची: बलातैलेन + अभ्यज्यात् → बलातैलेनाभ्यज्यात् (अ + अ → आ)।"),
}

# ===================================================================== AIDS
AIDS = {
    "103": {
        "diagram": {"groups": [
            {"label": "पहला विकल्प (वा)", "items": ["वरणादि गण", "पञ्चकोल सहित", "एला (सम्भवतः इलायची)", "अतीवाप (अस्पष्ट)"]},
            {"label": "दूसरा विकल्प (अथवा)", "items": ["वीरतरादि गण", "मूषकादि गण", "प्रतीवाप रूप में (समास खुला)"]}]},
        "chunks": "वरणादिं वा | सपंचकोलमेलामतीवापं (?) | अथवा | वीरतरादिमूषकादिप्रतीवापं",
        "frame": "क्रिया ‘पिबेत्’ कार्ड १०२ से; ‘वा … अथवा’ दो विकल्प खोलते हैं।",
    },
    "104": {
        "chunks": "लवणचूर्णं | वा | वत्सकादिनिर्यूहेण",
        "frame": "क्या (लवणचूर्णम्, द्वितीया) + किसके साथ (वत्सकादिनिर्यूहेण, तृतीया); क्रिया अध्याहृत।",
        "anchors": "याद-सूत्र: र् ने न को ण बनाया — नि-र्-यूहेण। (मेरी याद-पद्धति)",
    },
    "105": {
        "chunks": "वत्सकादिं | वा | मदिरया",
        "frame": "क्या (वत्सकादिम्, द्वितीया) + किसके साथ (मदिरया, तृतीया); क्रिया अध्याहृत।",
    },
    "106": {
        "chunks": "अंशुमतीद्वयकषायेन | वा | मरिचभद्रदारुकल्कं",
        "frame": "दो भाग: कषाय (अंशुमती-द्वय का) और कल्क (मरिच-भद्रदारु का); ‘वा’ के स्थान से दोनों का सम्बन्ध खुला।",
        "anchors": "याद-सूत्र: समास का अन्तिम शब्द रूप बताता है — कषाय = काढ़ा, कल्क = पीसा लेप। (मेरी याद-पद्धति)",
    },
    "107": {
        "diagram": {"groups": [
            {"label": "कल्क के द्रव्य (क्रम से)", "items": ["भाईीं (अस्पष्ट)", "नागर (सोंठ)", "देवदारु"]},
            {"label": "किसके साथ", "items": ["उष्ण अम्भस् (गरम पानी)"]}]},
        "chunks": "भाईीं (?) | नागरदेवदारुकल्कं | वोष्णाम्भसा",
        "sandhi": "आ + उ → ओ: वा + उष्ण → वोष्ण · अ + अ → आ: उष्ण + अम्भसा → उष्णाम्भसा।",
    },
    "108": {
        "diagram": {"groups": [
            {"label": "आधार", "items": ["पुराना गुड़"]},
            {"label": "एक चूर्ण (क्रम से)", "items": ["त्रिकटु: सोंठ, मरिच, पीपर", "त्रिजातक: दालचीनी, इलायची, तेजपात",
                                                 "धनिका: सम्भवतः धनिया"]},
            {"label": "क्रिया", "items": ["भक्षयेत् (खाए)"]}]},
        "chunks": "पुराणगुडं वा | त्रिकटुत्रिजातकधनिकाचूर्णसंसृष्टं | भक्षयेत्",
        "pegs": "मेरा बनाया चित्र: ‘तीन-तीन’ की दो थालियाँ — एक में तीन तीखे (सोंठ, मरिच, पीपर), एक में तीन सुगन्धित (दालचीनी, इलायची, तेजपात) — और बीच में धनिया; सब पुराने गुड़ पर। (केवल याद के लिए, ग्रन्थ का दावा नहीं)",
    },
    "109": {
        "chunks": "तस्याश्चेत् | स्वस्थानतो | योनिर्भ्रश्येत्",
        "sandhi": "विसर्ग + च → श्च: तस्याः + चेत् → तस्याश्चेत् · अः → ओ घोष से पहले: स्वस्थानतः + योनिः → स्वस्थानतो योनिः · इः → इर् घोष से पहले: योनिः + भ्रश्येत् → योनिर्भ्रश्येत्।",
        "frame": "चेत् (यदि) … भ्रश्येत् → फल अगली इकाई ११० में ‘ततः’ से।",
    },
    "110": {
        "chain": {"steps": ["ततः (तब)", "किसी के भी रक्त से योनि चुपड़ना", "कुशल स्त्री यथास्थान बैठाए (निवेशयेत्)"]},
        "chunks": "ततो | यस्य कस्यचिच्छोणितेन | अभ्यज्य योनिं | यथास्थानं | कुशला स्त्री निवेशयेत्",
        "sandhi": "अः → ओ घोष से पहले: ततः + यस्य → ततो यस्य · त् + श → च्छ: कस्यचित् + शोणितेन → कस्यचिच्छोणितेन · अ + अ → आ: शोणितेन + अभ्यज्य → शोणितेनाभ्यज्य।",
    },
    "111": {
        "diagram": {"groups": [
            {"label": "कल्क के द्रव्य (क्रम से)", "items": ["१ अशोक (मानक)", "२ रोहिणी (विवादित)", "३ बर्हिष (अज्ञात)",
                                                     "४ उशीर, खस (मानक)", "५ प्रियङ्गु (सम्भवतः, विवादित)", "६ देवदारु"]},
            {"label": "कर्म", "items": ["कल्क से पका तेल", "बार-बार स्वेदन", "भरना (क्या, नहीं कहा)"]}]},
        "chunks": "निविष्टां च | अशोकरोहिणीबर्हिषोशीरप्रियंगुदेवदारुकल्कविपक्वेन | तैलेन | बहुशः | स्वेदयेत् | पूरयेत्",
        "sandhi": "अ + अ → आ: च + अशोक → चाशोक · छपे के अनुसार अ + उ → ओ: बर्हिष + उशीर → बर्हिषोशीर (दूसरा विभाग भी सम्भव)।",
    },
    "112": {
        "chunks": "ब्रूयाच्च | गच्छ सुभगे | स्वस्थानम् | इति",
        "sandhi": "त् + च → च्च: ब्रूयात् + च → ब्रूयाच्च · म् + स्वर: स्वस्थानम् + इति → स्वस्थानमिति।",
        "frame": "ब्रूयात् (कहे) → उद्धरण ‘गच्छ सुभगे स्वस्थानम्’ → इति (उद्धरण समाप्त)।",
    },
    "113": {
        "chunks": "तद्वच्चान्यतमा | स्त्रीजातमात्रमेव | बालं | बालोपचरणीयेन | विथिनोप्पादयेत् (?)",
        "sandhi": "त् + च → च्च: तद्वत् + च → तद्वच्च · अ + अ → आ: च + अन्यतमा → चान्यतमा · अ + उ → ओ: बाल + उपचरणीय → बालोपचरणीय।",
        "frame": "कौन (अन्यतमा स्त्री) → किसे (जातमात्रं बालम्) → कैसे (बालोपचरणीय विधि से) → क्रिया क्षतिग्रस्त (अनुमानित)।",
    },
    "114": {
        "chunks": "तमुपदेक्ष्यते | तूत्तरेषु",
        "sandhi": "म् + स्वर: तम् + उपदेक्ष्यते → तमुपदेक्ष्यते · उ + उ → ऊ: तु + उत्तरेषु → तूत्तरेषु।",
    },
    "115": {
        "chunks": "अथ | सूतिकां | बलातैलेनाभ्यज्यात्",
        "sandhi": "अ + अ → आ: बलातैलेन + अभ्यज्यात् → बलातैलेनाभ्यज्यात्।",
        "frame": "अथ (फिर) → किसे (सूतिकाम्) → किससे (बलातैलेन) → क्रिया (अभ्यज्यात्)।",
    },
}

# ===================================================================== IMAGE_SPECS
IMAGE_SPECS = {
    ("103", "diagram"): {
        "file": "sh3-varanadi-vikalpa-103.svg",
        "alt": ("Two columns of unit 103. First option (vā): the varaṇādi group, with pañcakola, elā (probably cardamom) "
                "and atīvāpa (unclear). Second option (athavā): the vīratarādi and mūṣakādi groups as pratīvāpa, added "
                "substance (the compound is open)."),
        "type": "split",
        "title": "इकाई १०३: दो विकल्प",
        "cols": [["पहला विकल्प (वा)", ["वरणादि गण", "पञ्चकोल सहित", "एला (सम्भवतः इलायची)", "अतीवाप (अस्पष्ट)"]],
                 ["दूसरा विकल्प (अथवा)", ["वीरतरादि गण", "मूषकादि गण", "प्रतीवाप रूप में (समास खुला)"]]],
    },
    ("107", "diagram"): {
        "file": "sh3-nagara-kalka-107.svg",
        "alt": ("Table of unit 107: a paste of bhāīīṃ (unclear word), nāgara (dry ginger) and devadāru (deodar), "
                "taken with warm water."),
        "type": "table",
        "title": "इकाई १०७: कल्क और वाहन",
        "heads": ["छपा शब्द", "अर्थ"],
        "rows": [["भाईीं", "अस्पष्ट शब्द"], ["नागर", "सोंठ"], ["देवदारु", "देवदार (वृक्ष)"],
                 ["कल्कं", "कल्क (पीसा लेप)"], ["उष्णाम्भसा", "गरम पानी के साथ"]],
    },
    ("108", "diagram"): {
        "file": "sh3-purana-guda-108.svg",
        "alt": ("Table of unit 108: old jaggery is eaten mixed with one powder of trikaṭu (dry ginger, black pepper, "
                "long pepper; standard), trijātaka (cinnamon bark, cardamom, bay leaf; standard) and dhanikā "
                "(probably coriander)."),
        "type": "table",
        "title": "इकाई १०८: पुराना गुड़ और चूर्ण",
        "heads": ["द्रव्य", "घटक / पहचान"],
        "rows": [["पुराना गुड़", "आधार, खाया जाए"], ["त्रिकटु", "सोंठ, मरिच, पीपर (मानक)"],
                 ["त्रिजातक", "दालचीनी, इलायची, तेजपात (मानक)"], ["धनिका", "सम्भवतः धनिया"]],
    },
    ("110", "chain"): {
        "file": "sh3-yoni-niveshana-110.svg",
        "alt": ("Flowchart of unit 110: then, the yoni is anointed with the blood of anyone whatever, and a skilled "
                "woman places it back in its proper place."),
        "type": "mermaid",
        "code": ("flowchart TD\n"
                 "  A[\"ततः (तब)\"] --> B[\"किसी के भी रक्त से चुपड़ना\"]\n"
                 "  B --> C[\"कुशल स्त्री यथास्थान बैठाए\"]\n"),
    },
    ("111", "diagram"): {
        "file": "sh3-ashoka-taila-111.svg",
        "alt": ("Table of unit 111, the six drugs of the paste in line order with the data's labels: aśoka (standard), "
                "rohiṇī (disputed), barhiṣa (unidentified), uśīra vetiver (standard), priyaṅgu (probable, disputed), "
                "devadāru; the oil cooked with them is used for repeated fomenting and filling."),
        "type": "table",
        "title": "इकाई १११: कल्क से पका तेल",
        "heads": ["द्रव्य (क्रम से)", "पहचान"],
        "rows": [["१ अशोक", "मानक"], ["२ रोहिणी", "विवादित"], ["३ बर्हिष", "अज्ञात"],
                 ["४ उशीर", "खस (मानक)"], ["५ प्रियङ्गु", "सम्भवतः फूलप्रियंगु, विवादित"], ["६ देवदारु", "देवदारु"],
                 ["उपयोग", "बार-बार स्वेदन, और भरना"]],
    },
}
