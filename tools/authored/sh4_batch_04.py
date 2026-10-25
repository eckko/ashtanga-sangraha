from helpers import mcq, match, order, fill, multi, accepts


AUTHORED = {}

# ---------------------------------------------------------------- unit 41
AUTHORED["41"] = {
    "title": "तत्र यस्याः ... तमुपविष्टकमित्याचक्षते",
    "question": "By unit 41, what signs mark the condition that is called upaviṣṭaka?",
    "rule": ("In her in whom the fetus constantly throbs (स्फुरति) and the belly (कुक्षि) does not grow (न विवर्धते), "
             "that they call upaviṣṭaka (उपविष्टक, literally 'sitting down'). The bleeding is described in a doubtful reading."),
    "limits": ("Low confidence. The bleeding clause (occasional, scanty ārtava and flow) rests on a corrected reading of "
               "printed परिस्रावादल्पौ, and प्रामात् is unclear and untranslated: no question rests on either. Whether "
               "तम् means the condition or the fetus is not stated. A prose line."),
    "explain_hi": ("यह गद्य-पंक्ति उपविष्टक नाम की दशा के लक्षण बताती है। "
                   "जिस स्त्री में गर्भ निरन्तर (सततम्) फड़कता है (स्फुरति) और कुक्षि यानी पेट नहीं बढ़ता (न च कुक्षिर्विवर्धते), "
                   "उसे उपविष्टक कहते हैं (आचक्षते)। "
                   "आर्तव और परिस्राव के कभी-कभी और अल्प दिखने वाला अंश सुधारे गए अनुमानित पाठ पर टिका है, और ‘प्रामात्’ शब्द "
                   "अस्पष्ट है; इसलिए इन पर कोई प्रश्न नहीं। "
                   "‘तम्’ पुंलिंग है; वह दशा को कहता है या गर्भ को, यह नहीं बताया गया।"),
    "hook": "गर्भ फड़के, पेट न बढ़े: उपविष्टक।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 41, what name do they give to this condition?",
            ("Upaviṣṭaka (उपविष्टक)", "तमुपविष्टकमित्याचक्षते: that they call upaviṣṭaka."),
            [("Āmagarbha (आमगर्भ)", "Āmagarbha, the unripe embryo, is a different topic of this chapter."),
             ("Mūḍhagarbha (मूढगर्भ)", "Mūḍhagarbha, the obstructed fetus, comes in a later section."),
             ("Raktapitta (रक्तपित्त)", "Raktapitta, a bleeding disorder, is named in unit 21, not here.")],
            "The line ends: that they call upaviṣṭaka.",
            "तम् उपविष्टकम् इति आचक्षते."),
        order(1, "Put these phrases of unit 41 in the line's order.",
              ["तत्र यस्याः", "सततं च गर्भः", "स्फुरति", "न च कुक्षिर्विवर्द्धते", "तमुपविष्टकमित्याचक्षते"],
              "Therein, in her in whom ... the fetus constantly ... throbs, and the belly does not grow: that they call upaviṣṭaka.",
              "तत्र यस्याः → सततं च गर्भः → स्फुरति → न च कुक्षिर्विवर्द्धते → तमुपविष्टकमित्याचक्षते."),
        match(2, "Match each word of unit 41 to its meaning.",
              [["सततम्", "constantly"], ["स्फुरति", "throbs, quivers"], ["कुक्षि", "belly"],
               ["विवर्धते", "grows"], ["आचक्षते", "they call"]],
              "The sure signs: the fetus constantly throbs, the belly does not grow; they call it upaviṣṭaka.",
              "सततम्, स्फुरति, कुक्षि, विवर्धते, आचक्षते.", role="extend",
              teaches="उपविष्टक is a name, literally 'sitting down', given to the fetus or condition that throbs but does not grow."),
        mcq("discriminate", 3, "Which split of इत्याचक्षते is right?",
            ("इति + आचक्षते", "इ before a different vowel becomes य्: इति + आचक्षते → इत्याचक्षते."),
            [("इत्य + आचक्षते", "इत्य is not a word; the particle is इति."),
             ("इति + अचक्षते", "इ + अ would give इत्यचक्षते, with a short अ, not या."),
             ("इत् + याचक्षते", "याचक्षते is not a verb; the verb is आचक्षते (they call).")],
            "इति (thus) + आचक्षते (they call): इ + आ → या.",
            "इ + a different vowel → य् + that vowel."),
        multi("apply", 4, "Which statements about unit 41 are right by the card?",
              [("The word प्रामात् has a sure meaning", "The data calls प्रामात् unclear and leaves it untranslated."),
               ("The fetus throbs constantly", "Right: सततं च गर्भः ... स्फुरति."),
               ("The belly grows and then shrinks", "Unit 41 says the belly does not grow at all: न च कुक्षिर्विवर्धते."),
               ("The belly does not grow", "Right: न च कुक्षिर्विवर्धते.")],
              [1, 3],
              "The sure signs are a constantly throbbing fetus and a belly that does not grow.",
              "सततं गर्भः स्फुरति, न च कुक्षिर्विवर्धते."),
        mcq("transfer", 5, "By the rule of कुक्षिर्विवर्धते, how is हरिः + वदति (Hari speaks) joined?",
            ("हरिर्वदति", "A visarga after इ before a voiced sound becomes र्, as कुक्षिः + विवर्धते."),
            [("हरी वदति", "The visarga drops with a long ई only before र्, not before व."),
             ("हरिश्वदति", "The visarga becomes श् before च, छ or श, not before व."),
             ("हरिः वदति", "Before a voiced sound the visarga after इ does not stay; it becomes र्.")],
            "हरिः + वदति = हरिर्वदति, like कुक्षिः + विवर्धते = कुक्षिर्विवर्धते.",
            "इः + voiced sound → इर्.",
            teaches="A visarga after a vowel other than अ/आ becomes र् before a voiced sound: कुक्षिः + विवर्धते → कुक्षिर्विवर्धते."),
    ],
}

# ---------------------------------------------------------------- unit 42
AUTHORED["42"] = {
    "title": "यदा तु प्रतिमासमार्तवं प्रत्यहं वा परिस्रवणं",
    "question": "By unit 42, what bleeding and what movement of the fetus mark the second picture?",
    "rule": ("When there is ārtava (menstrual blood) every month (प्रतिमासम्) or flow every day (प्रत्यहम्), not very scanty "
             "(नात्यल्पम्), and the fetus, wasting (परिहीयमाण), moves a little (किंचित् स्पन्दते) after a long time (चिरात्)."),
    "limits": ("The sentence appears to run on into unit 43, where the names come; this unit names no condition. The first clause has "
               "no verb. Printed गर्भाः (plural) is read as singular गर्भः; no question rests on the number. A prose line."),
    "explain_hi": ("यह गद्य-पंक्ति एक दूसरी अवस्था बताती है। "
                   "जब हर मास (प्रतिमासम्) आर्तव यानी रज, या हर दिन (प्रत्यहम्) परिस्रवण होता है, और वह बहुत थोड़ा नहीं होता "
                   "(नात्यल्पम्), और गर्भ घटता हुआ (परिहीयमाणः) देर से (चिरात्) थोड़ा-सा (किंचित्) हिलता है (स्पन्दते)। "
                   "वाक्य सम्भवतः अगली इकाई (४३) में पूरा होता है, जहाँ नाम दिए गए हैं; यहाँ किसी दशा का नाम नहीं है। "
                   "पहले खण्ड में क्रिया नहीं है।"),
    "hook": "हर मास रज, स्राव कम नहीं; गर्भ घटे, देर से थोड़ा हिले।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 42, how does the wasting fetus move?",
            ("A little, after a long time", "चिरात् किंचित् स्पन्दते: it moves a little after a long time."),
            [("Strongly, many times each day", "The unit says only a little (किंचित्), and late (चिरात्)."),
             ("Not at all, lying quite still", "It does move, though only a little: स्पन्दते."),
             ("Downward, turning head first", "Turning is not described in unit 42.")],
            "It moves a little, after a long time.",
            "चिरात् किंचित् स्पन्दते."),
        order(1, "Put these phrases of unit 42 in the line's order.",
              ["यदा तु", "प्रतिमासमार्तवं", "प्रत्यहं वा परिस्रवणं", "नात्यल्पं", "परिहीयमाणो", "चिरात्किंचित्स्पंदते"],
              "When, however, ārtava every month, or flow every day, not very scanty, wasting, (the fetus) moves a little after a long time.",
              "यदा तु → प्रतिमासमार्तवं → प्रत्यहं वा परिस्रवणं → नात्यल्पं → परिहीयमाणो → चिरात्किंचित्स्पंदते."),
        match(2, "Match each word of unit 42 to its meaning.",
              [["प्रतिमासम्", "every month"], ["प्रत्यहम्", "every day"], ["परिहीयमाण", "wasting, being diminished"],
               ["चिरात्", "after a long time"], ["किंचित्", "a little"]],
              "Monthly or daily flow, a wasting fetus that moves a little, late.",
              "प्रतिमासम्, प्रत्यहम्, परिहीयमाण, चिरात्, किंचित्.", role="extend",
              teaches="प्रति- with a time word means 'every': प्रतिमासम् = every month, प्रत्यहम् = every day."),
        mcq("discriminate", 3, "Which split of प्रत्यहम् is right?",
            ("प्रति + अहम्", "इ before a different vowel becomes य्: प्रति + अहम् → प्रत्यहम्."),
            [("प्रते + अहम्", "ए + अ would give प्रतेऽहम्, with ए kept and ऽ."),
             ("प्रत् + यहम्", "यहम् is not a word; the word is अहन् (day), here अहम्."),
             ("प्र + अत्यहम्", "अत्यहम् is not a word, and अ + अ would give आ.")],
            "प्रति (every) + अहम् (day): इ + अ → य.",
            "इ + a different vowel → य् + that vowel."),
        mcq("apply", 4, "By unit 42, how much is the flow?",
            ("Not very scanty", "नात्यल्पम् = न + अति + अल्पम्: not very scanty."),
            [("Very scanty, a few drops", "The unit says the opposite: नात्यल्पम्, not very scanty."),
             ("None at all, it has stopped", "There is ārtava every month or flow every day."),
             ("Heavy, mixed with many clots", "Clots and heaviness are not named in unit 42.")],
            "The flow is not very scanty.",
            "नात्यल्पम् = न अति अल्पम्."),
        mcq("transfer", 5, "By the rule of नात्यल्पम् (न + अति), how is अद्य + अपि (even today) joined?",
            ("अद्यापि", "अ + अ → आ, like न + अति → नाति."),
            [("अद्योपि", "अ + अ does not give ओ."),
             ("अद्यैपि", "अ + अ does not give ऐ."),
             ("अद्यपि", "The two अ merge into a long आ, not a short अ.")],
            "अद्य + अपि = अद्यापि, like न + अति = नाति in नात्यल्पम्.",
            "अ + अ → आ.",
            teaches="A short अ followed by a short अ joins as a long आ: न + अति → नाति; अद्य + अपि → अद्यापि."),
    ],
}

# ---------------------------------------------------------------- unit 43
AUTHORED["43"] = {
    "title": "कुक्षिश्च वृद्धोऽपि ... तदुपशुष्ककं नागोदरं च",
    "question": "By unit 43, what happens to the belly, and what names are given?",
    "rule": ("And the belly (कुक्षि), though grown (वृद्धोऽपि), diminishes: that is upaśuṣkaka (उपशुष्कक, literally "
             "'dried up') and nāgodara (नागोदर). It appears to complete the sentence begun in unit 42."),
    "limits": ("'Diminishes' rests on a near-certain correction (printed चरिहीयते read परिहीयते). Whether upaśuṣkaka and "
               "nāgodara are one condition or two is not settled, and nāga may be serpent or elephant: no question asks which (one only asks that both are "
               "left open). The copula is understood. A prose line."),
    "explain_hi": ("यह गद्य-पंक्ति सम्भवतः इकाई ४२ का वाक्य पूरा करती है। "
                   "कुक्षि यानी पेट बढ़ा हुआ होकर भी (वृद्धोऽपि) घटता है; उसे उपशुष्कक (शब्दार्थ: सूखा हुआ) और नागोदर कहा गया है। "
                   "छपा ‘चरिहीयते’ लगभग निश्चित रूप से ‘परिहीयते’ (घटता है) पढ़ा गया है। "
                   "उपशुष्कक और नागोदर एक ही दशा के दो नाम हैं या दो दशाएँ, शब्दों से तय नहीं; ‘नाग’ साँप भी हो सकता है और हाथी भी। "
                   "क्रिया ‘है’ समझी जाती है।"),
    "hook": "पेट बढ़कर भी घटे: उपशुष्कक, नागोदर।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 43, which two names are given?",
            ("Upaśuṣkaka and nāgodara", "तदुपशुष्ककं नागोदरं च."),
            [("Āmagarbha and mūḍhagarbha", "Neither name occurs in unit 43."),
             ("Pratiśyāya and śuṣkakāsa", "These are signs (catarrh, dry cough) in unit 45."),
             ("Raktapitta and mūrcchā", "Raktapitta is unit 21; mūrcchā, fainting, is a sign in unit 46.")],
            "The line ends: that is upaśuṣkaka, and nāgodara.",
            "तत् उपशुष्ककम् नागोदरम् च."),
        order(1, "Put these phrases of unit 43 in the line's order.",
              ["कुक्षिश्च", "वृद्धोऽपि", "तदुपशुष्ककं", "नागोदरं च"],
              "And the belly, though grown, (diminishes); that is upaśuṣkaka, and nāgodara.",
              "कुक्षिश्च → वृद्धोऽपि → तदुपशुष्ककं → नागोदरं च."),
        match(2, "Match each word of unit 43 to its meaning.",
              [["कुक्षि", "belly"], ["वृद्ध", "grown"], ["अपि", "even, though"],
               ["उपशुष्कक", "a name, literally 'dried up'"], ["उदर", "belly (in नागोदर)"]],
              "The belly, though grown, diminishes; the names are upaśuṣkaka and nāgodara.",
              "कुक्षि, वृद्ध, अपि, उपशुष्कक, उदर.", role="extend",
              teaches="नागोदर = नाग + उदर: the data keeps it as a name, literally 'nāga-belly'."),
        mcq("discriminate", 3, "Which split of वृद्धोऽपि is right?",
            ("वृद्धः + अपि", "अः + अ → ओऽ: the अ of अपि is dropped and marked ऽ."),
            [("वृद्ध + अपि", "अ + अ would give वृद्धापि, with आ and no ऽ."),
             ("वृद्धे + अपि", "ए + अ would give वृद्धेऽपि, with ए kept."),
             ("वृद्धो + पि", "पि is not a word; the word is अपि (though).")],
            "वृद्धः (grown) + अपि (though): अः + अ → ओऽ.",
            "अः + अ → ओऽ."),
        multi("apply", 4, "Which statements about unit 43 are right by the card?",
              [("The text explains what nāgodara means", "The data says the text does not explain it."),
               ("It is not settled whether the two names are one condition or two", "Right: the note leaves it open."),
               ("Printed चरिहीयते is kept as a real verb", "It is read as परिहीयते, a near-certain correction (c for p)."),
               ("नाग may mean serpent or elephant", "Right: the note gives both senses.")],
              [1, 3],
              "The card leaves open both the sense of nāga and whether the names are one condition or two.",
              "तदुपशुष्ककं नागोदरं च: names, not explained."),
        mcq("transfer", 5, "By the rule of तदुपशुष्ककम्, how is तत् + अन्नम् (that food) joined?",
            ("तदन्नम्", "A final त् before a vowel becomes द्, as तत् + उपशुष्ककम्."),
            [("ततन्नम्", "Before a vowel the final त् does not stay unvoiced; it becomes द्."),
             ("तन्नन्नम्", "त् may become न् before a nasal such as न or म, not before a vowel."),
             ("तच्छन्नम्", "त् + श gives च्श or च्छ; here no श follows.")],
            "तत् + अन्नम् = तदन्नम्, like तत् + उपशुष्ककम् = तदुपशुष्ककम्.",
            "त् + vowel → द्.",
            teaches="A word-final त् becomes द् before a vowel: तत् + उपशुष्ककम् → तदुपशुष्ककम्."),
    ],
}

# ---------------------------------------------------------------- unit 44
AUTHORED["44"] = {
    "title": "तौ तु मातुराहारतेजसाऽल्पेनाप्यायमानौ",
    "question": "By unit 44, what happens to those two when they become well nourished?",
    "rule": ("Those two (तौ), nourished by the slight tejas (vigour) of the mother's food, when they become well nourished "
             "(पुष्टौ), then even after groups of years (वर्षगणैरपि) the woman (प्रमदा) gives birth indeed (प्रसूयत एव)."),
    "limits": ("The line does not name the two (तौ); the data reads them as the two kinds just described. Tejas may also mean "
               "essence. No number of years is stated. No question rests on who the two are. A prose line."),
    "explain_hi": ("यह गद्य-पंक्ति आशा की बात कहती है। "
                   "वे दोनों (तौ) माता के आहार के अल्प तेज यानी बल से पोषण पाते हुए (आप्यायमानौ) जब पुष्ट हो जाएँ, "
                   "तब वर्षों के समूहों के बाद भी (वर्षगणैरपि) स्त्री (प्रमदा) प्रसव करती ही है (प्रसूयत एव)। "
                   "‘तौ’ किन दो को कहता है, पंक्ति में नाम नहीं; डेटा उन्हें अभी कहे गए दो प्रकार मानता है। "
                   "‘तेज’ को सार भी पढ़ा जा सकता है, और वर्षों की कोई संख्या नहीं दी गई।"),
    "hook": "थोड़ा पोषण, धीरे पुष्टि: बरसों बाद भी प्रसव होता ही है।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 44, what does the woman do in the end, even after groups of years?",
            ("She gives birth", "वर्षगणैरपि प्रमदा प्रसूयत एव: she gives birth indeed."),
            [("She loses the pregnancy", "The unit says the opposite: she gives birth indeed (एव)."),
             ("She bleeds every month", "Monthly ārtava is unit 42; unit 44 speaks of birth."),
             ("She can never conceive again", "The unit says she does give birth, even after years.")],
            "Even after groups of years, she gives birth.",
            "प्रमदा प्रसूयत एव."),
        order(1, "Put these phrases of unit 44 in the line's order.",
              ["तौ तु", "मातुराहारतेजसाऽल्पेन", "आप्यायमानौ", "यदा पुष्टौ स्यातां", "तदा वर्षगणैरपि",
               "प्रमदा प्रसूयत एव"],
              "Those two, by the slight tejas of the mother's food, being nourished, when they become well nourished, then even after groups of years the woman gives birth.",
              "तौ तु → मातुराहारतेजसाऽल्पेन → आप्यायमानौ → यदा पुष्टौ स्यातां → तदा वर्षगणैरपि → प्रमदा प्रसूयत एव."),
        match(2, "Match each word of unit 44 to its meaning.",
              [["आप्यायमान", "being nourished"], ["पुष्ट", "well nourished"], ["वर्षगण", "groups of years"],
               ["प्रमदा", "woman"], ["प्रसूयते", "gives birth"]],
              "Slow nourishment, then birth even after a long time.",
              "आप्यायमान, पुष्ट, वर्षगण, प्रमदा, प्रसूयते.", role="extend",
              teaches="यदा ... तदा = when ... then: यदा पुष्टौ स्यातां तदा ... प्रसूयते."),
        mcq("discriminate", 3, "Which split of मातुराहार is right?",
            ("मातुः + आहार", "उः before a vowel becomes उर्: मातुः (of the mother) + आहार."),
            [("माता + आहार", "आ + आ would give माताहार, with no र्."),
             ("मातृ + आहार", "ऋ + आ would give मात्राहार, not मातुर्."),
             ("मातुरा + हार", "मातुरा is not a form of माता; the genitive is मातुः.")],
            "मातुः (of the mother) + आहार (food): the visarga after उ becomes र् before आ.",
            "उः + vowel → उर्."),
        mcq("apply", 4, "A woman in this state has not delivered for years. What does unit 44 say?",
            ("Once they are well nourished, she gives birth", "यदा पुष्टौ स्यातां तदा ... प्रसूयत एव."),
            [("She must deliver within twelve years", "No number of years is stated; the text says groups of years."),
             ("Only the father's food can nourish the two of them", "They are nourished by the tejas of the mother's food."),
             ("They grow strong on rich, abundant food", "The tejas is slight (अल्पेन), not abundant.")],
            "When they become well nourished, she gives birth, even after groups of years.",
            "यदा ... तदा ... प्रसूयत एव."),
        mcq("transfer", 5, "By the rule of वर्षगणैरपि, how is देवैः + अपि (even by the gods) joined?",
            ("देवैरपि", "A visarga after ऐ before a vowel becomes र्, as गणैः + अपि."),
            [("देवैऽपि", "The avagraha marks a dropped अ after ए or ओ, not after ऐः."),
             ("देवायपि", "The word ends in a visarga, so ऐ does not meet the vowel and become आय्."),
             ("देवोऽपि", "ओऽ comes from अः + अ (देवः + अपि), a different word.")],
            "देवैः + अपि = देवैरपि, like वर्षगणैः + अपि = वर्षगणैरपि.",
            "ऐः + vowel → ऐर्.",
            teaches="A visarga after a vowel other than अ/आ becomes र् before a vowel: वर्षगणैः + अपि → वर्षगणैरपि."),
    ],
}

# ---------------------------------------------------------------- unit 45
AUTHORED["45"] = {
    "title": "तत्र वातेनोपविष्टकोपशुष्ककयोः",
    "question": "By unit 45, what signs does Vāta produce in upaviṣṭaka and upaśuṣkaka?",
    "rule": ("By Vāta: vāyu obstructed; stool passed noisy, frothy, broken; urine held back; pain in waist, back and heart; "
             "yawning; loss of sleep; catarrh; dry cough; lassitude; five 'as it were' sensations (the fifth, entering darkness, of open sense); hard digestion; daily decline; rough, cracked skin."),
    "limits": ("The construction 'by Vāta, in these two' is loose. Whether abhīkṣṇam (repeatedly) goes with sleep-loss or "
               "catarrh, and the sense of 'entering darkness', are open: no question rests on them. The ants sense (crawling) is "
               "probable. The woman is not named. A prose line."),
    "explain_hi": ("यह लम्बी गद्य-पंक्ति उपविष्टक और उपशुष्कक में वात के लक्षण गिनाती है। "
                   "वायु रुकता है; मल शब्द सहित, झागदार और टूटा हुआ निकलता है; मूत्र रुकता है; कमर, पीठ और हृदय में पीड़ा, "
                   "जम्हाई, नींद का नाश, प्रतिश्याय यानी जुकाम, सूखी खाँसी और साद यानी थकावट होती है। "
                   "पाँच ‘इव’ (मानो) वाले अनुभव हैं: कान मानो भनभनाते हैं, कनपटियाँ मानो चुभती हैं, शरीर मानो चींटियों से जुड़ा है, "
                   "वायु मानो काटता हुआ पेट में घूमता है, और मानो अन्धकार में प्रवेश कराया जाता है। "
                   "अन्न कठिनाई से पचता है, दिन-प्रतिदिन हानि होती है, और त्वचा फटी, विवर्ण और रूखी होती है। "
                   "‘अभीक्ष्णम्’ किससे जुड़ता है और ‘तम इव प्रवेश्यते’ का ठीक अर्थ, ये खुले हैं।"),
    "hook": "वात: झागदार टूटा मल, रुका मूत्र, सूखी खाँसी, रूखी फटी त्वचा।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 45, how is the stool passed under Vāta?",
            ("Noisy, frothy and broken", "सशब्दं फेनिलं विच्छिन्नं शकृदुपवेश्यते."),
            [("Smooth, silent and soft", "The unit says the opposite: with sound (सशब्दम्), broken."),
             ("Mixed with blood and pus", "Blood and pus are not named in unit 45."),
             ("Not at all; it is held", "It is urine that is held back (उपरुध्यते); stool is passed.")],
            "Stool is passed noisy, frothy and broken.",
            "सशब्दं फेनिलं विच्छिन्नं शकृत्."),
        order(1, "Put these signs of unit 45 in the line's order.",
              ["सशब्दं फेनिलं विच्छिन्नं शकृत्", "मूत्रमुपरुध्यते", "कटीपृष्ठहृदयेषु वेदना", "निद्रानाशः",
               "शुष्ककासः", "दुःखेनान्नस्य जरणम्"],
              "Noisy, frothy, broken stool; urine held back; pain in waist, back and heart; loss of sleep; dry cough; hard digestion.",
              "शकृत् → मूत्र → वेदना → निद्रानाश → शुष्ककास → दुःखेन जरण."),
        match(2, "Match each 'as it were' (इव) sign of unit 45 to what it says.",
              [["कर्णौ", "the two ears, as it were, hum"], ["शंखौ", "the two temples, as it were, are pricked"],
               ["शरीरम्", "the body, as it were, is joined with ants"],
               ["वायुः", "as if cutting, it wanders in the belly"]],
              "Four of the line's similes, each marked by इव (as it were).",
              "क्ष्वेलेते इव कर्णौ, तुद्येते इव शंखौ, पिपीलिकाभिरिव संसृज्यते शरीरम्, परिकृन्तन्निव वायुर्भ्रमति.",
              role="extend",
              teaches="इव = as it were, like: it marks a sensation described by a comparison."),
        mcq("discriminate", 3, "Which split of निद्रानाशोऽभीक्ष्णम् is right?",
            ("निद्रानाशः + अभीक्ष्णम्", "अः + अ → ओऽ: the अ of अभीक्ष्णम् is dropped and marked ऽ."),
            [("निद्रानाश + अभीक्ष्णम्", "अ + अ would give निद्रानाशाभीक्ष्णम्, with आ."),
             ("निद्रानाशे + अभीक्ष्णम्", "ए + अ would give निद्रानाशेऽभीक्ष्णम्, with ए."),
             ("निद्रानाशो + भीक्ष्णम्", "भीक्ष्णम् is not a word; the word is अभीक्ष्णम्.")],
            "निद्रानाशः (loss of sleep) + अभीक्ष्णम् (repeatedly): अः + अ → ओऽ.",
            "अः + अ → ओऽ."),
        multi("apply", 4, "Which of these are Vāta signs named in unit 45?",
              [("Dry cough", "Right: शुष्ककासः."),
               ("Burning in the belly and heart", "Burning (दाह) is a Pitta sign, unit 46."),
               ("Cracked, discoloured, rough skin", "Right: स्फुटितविवर्णपरुषत्वक्त्वम्."),
               ("A sweet taste in the mouth", "A sweet mouth is a Kapha sign, unit 47."),
               ("Loss of sleep", "Right: निद्रानाशः.")],
              [0, 2, 4],
              "Dry cough, loss of sleep and rough, cracked skin are Vāta signs; burning and a sweet mouth are not.",
              "Vāta: शुष्ककास, निद्रानाश, स्फुटित-विवर्ण-परुष त्वक्."),
        mcq("transfer", 5, "By the rule of वातेनोपविष्टक, how is देव + उत्सवः (a festival of the gods) joined?",
            ("देवोत्सवः", "अ + उ → ओ, as in वातेन + उपविष्टक."),
            [("देवौत्सवः", "अ + उ gives ओ, not औ."),
             ("देवेत्सवः", "अ + उ does not give ए."),
             ("देवुत्सवः", "The अ does not vanish; it merges into ओ.")],
            "देव + उत्सवः = देवोत्सवः, like वातेन + उपविष्टक = वातेनोपविष्टक.",
            "अ + उ → ओ.",
            teaches="A short अ followed by उ joins as ओ: वातेन + उपविष्टक → वातेनोपविष्टक; देव + उत्सवः → देवोत्सवः."),
    ],
}

# ---------------------------------------------------------------- unit 46
AUTHORED["46"] = {
    "title": "पित्तेन ताम्रहरितमुपवेश्यते",
    "question": "By unit 46, what signs does Pitta produce?",
    "rule": ("By Pitta: a coppery-green (one) is passed; vomiting (छर्दि); fainting (मूर्च्छा); burning in belly and heart; "
             "eyes, urine and nails yellow, red, cow-urine-hued; and the woman becomes dark (काली), weak and constantly in pain."),
    "limits": ("The noun of ताम्रहरितम् is not stated (stool of unit 45 is likely, not supplied). धूमिक and अम्लक are of "
               "uncertain sense; the colour list may be read two ways. No question rests on these. A prose line."),
    "explain_hi": ("यह गद्य-पंक्ति पित्त के लक्षण बताती है। "
                   "पित्त से ताम्र-हरित (ताँबे जैसा हरा) निकलता है; किस वस्तु का रंग है, यह नहीं कहा (सम्भवतः इकाई ४५ का मल)। "
                   "धूमिक और अम्लक के अर्थ अनिश्चित हैं। "
                   "फिर वमन (छर्दि), मूर्च्छा, कुक्षि और हृदय में जलन, आँखों, मूत्र और नखों का पीला, लाल और गोमूत्र जैसी आभा वाला होना; "
                   "और स्त्री काली, दुर्बल और नित्य पीड़ा वाली हो जाती है। "
                   "‘-त्व’ प्रत्यय भाववाचक है: ‘...नखत्वम्’ = नखों आदि का वैसा होना।"),
    "hook": "पित्त: जलन, वमन, मूर्च्छा; स्त्री काली, दुर्बल, सदा पीड़ित।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 46, where is burning felt under Pitta?",
            ("In the belly and the heart", "कुक्षिहृदयदाहः: burning of the belly and heart."),
            [("In the hands and the feet", "Hands and feet are white in the Kapha picture, unit 47."),
             ("In the ears and the temples", "Ears hum and temples are pricked under Vāta, unit 45."),
             ("In the waist and the back", "Pain in waist and back is a Vāta sign, unit 45.")],
            "Burning is in the belly and the heart.",
            "कुक्षिहृदयदाहः."),
        order(1, "Put these signs of unit 46 in the line's order.",
              ["छर्दिः", "मूर्च्छा", "कुक्षिहृदयदाहः", "काली", "दुर्बला", "नित्यशूला"],
              "Vomiting, fainting, burning of belly and heart, (eyes, urine, nails coloured), dark, weak, constantly in pain.",
              "छर्दिः → मूर्च्छा → कुक्षिहृदयदाहः → काली → दुर्बला → नित्यशूला."),
        match(2, "Match each word of unit 46 to its meaning.",
              [["छर्दि", "vomiting"], ["मूर्च्छा", "fainting"], ["दाह", "burning"], ["दुर्बला", "weak"],
               ["नित्यशूला", "constantly in pain"]],
              "Five of the Pitta signs.",
              "छर्दि, मूर्च्छा, दाह, दुर्बला, नित्यशूला.", role="extend",
              teaches="नित्यशूला is a bahuvrīhi: she whose pain (शूल) is constant (नित्य)."),
        mcq("discriminate", 3, "Which split of छर्दिर्मूर्च्छा is right?",
            ("छर्दिः + मूर्च्छा", "A visarga after इ before a voiced sound becomes र्."),
            [("छर्दि + मूर्च्छा", "With no visarga, no र् would appear: छर्दिमूर्च्छा."),
             ("छर्दिम् + मूर्च्छा", "म् before म would give छर्दिम्मूर्च्छा or छर्दिं मूर्च्छा, not र्."),
             ("छर्दिर + मूर्च्छा", "छर्दिर is not a word; the word is छर्दि (vomiting).")],
            "छर्दिः (vomiting) + मूर्च्छा (fainting): इः + voiced म → इर्.",
            "इः + voiced sound → इर्."),
        mcq("apply", 4, "By unit 46, what does the woman become under Pitta?",
            ("Dark, weak, constantly in pain", "काली दुर्बला नित्यशूला च नारी भवति."),
            [("Pale, heavy and always sleepy", "None of these is said of her in unit 46."),
             ("White in her hands, feet, eyes", "White hands, feet and eyes are the Kapha picture, unit 47."),
             ("Plump, strong and free of pain", "The unit says weak (दुर्बला) and constantly in pain.")],
            "She becomes dark, weak and constantly in pain.",
            "काली दुर्बला नित्यशूला च नारी भवति."),
        mcq("transfer", 5, "By the abstract suffix of ...नखत्वम्, what does गुरुत्वम् mean?",
            ("Heaviness, being heavy", "-त्व makes an abstract noun: the state of being गुरु (heavy)."),
            [("A heavy man, one who is heavy", "That would be the adjective गुरुः used of a person."),
             ("Heavier, more heavy than others", "A comparative is made with -तर (गुरुतर), not -त्व."),
             ("Of the teacher, the guru's own", "That would be a genitive (गुरोः), not an -त्व noun.")],
            "गुरु + त्व = गुरुत्वम्, the state of being heavy, as ...नख + त्व = the state of the nails (being so coloured).",
            "-त्व → abstract noun (the state of).",
            teaches="The suffix -त्व makes an abstract neuter noun, 'the state of being X': ...नेत्रमूत्रनखत्वम्."),
    ],
}

# ---------------------------------------------------------------- unit 47
AUTHORED["47"] = {
    "title": "श्लेष्मणा मधुरास्यत्वम्",
    "question": "By unit 47, what signs does Śleṣman (Kapha) produce?",
    "rule": ("By Śleṣman (Kapha): a sweet mouth (मधुरास्यत्व), nausea (उत्क्लेश), bringing up phlegm (श्लेष्मोद्वमन), "
             "aversion to food (भक्तद्वेष), white hands, feet and eyes, cough (कास) and breathlessness (श्वास)."),
    "limits": ("No verb is printed; the list continues the Vāta and Pitta pictures of units 45-46. Śvāsa is kept as "
               "breathlessness; the data calls an asthma-type sense only probable. No cause or treatment is given here. A prose line."),
    "explain_hi": ("यह गद्य-पंक्ति कफ (श्लेष्मा) के लक्षण गिनाती है। "
                   "मुख का मीठा रहना (मधुरास्यत्व), उत्क्लेश यानी मिचली, कफ का उगलना (श्लेष्मोद्वमन), भोजन से द्वेष (भक्तद्वेष), "
                   "हाथ, पैर और आँखों का श्वेत होना, खाँसी (कास) और श्वास यानी साँस फूलना। "
                   "क्रिया नहीं है; यह सूची इकाई ४५-४६ के वात और पित्त के चित्रों के बाद आती है। "
                   "श्वास को दमा जैसा रोग मानना केवल सम्भावित है।"),
    "hook": "कफ: मीठा मुँह, मिचली, कफ-वमन, भोजन से अरुचि, श्वेतता, खाँसी, श्वास।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 47, what taste is in the mouth under Kapha?",
            ("Sweet (मधुर)", "मधुरास्यत्वम्: the state of a sweet mouth."),
            [("Bitter (तिक्त)", "Bitterness is not named in unit 47."),
             ("Salty (लवण)", "Saltiness is not named in unit 47."),
             ("Pungent (कटु)", "Pungency is not named in unit 47.")],
            "The mouth is sweet.",
            "मधुर + आस्य + त्व."),
        order(1, "Put these signs of unit 47 in the line's order.",
              ["मधुरास्यत्वम्", "उत्क्लेशः", "श्लेष्मोद्वमनं", "भक्तद्वेषः", "श्वेतहस्तपादनेत्रता", "कासः श्वासश्च"],
              "Sweet mouth, nausea, bringing up phlegm, aversion to food, white hands-feet-eyes, cough and breathlessness.",
              "मधुरास्यत्वम् → उत्क्लेशः → श्लेष्मोद्वमनं → भक्तद्वेषः → श्वेतहस्तपादनेत्रता → कासः श्वासश्च."),
        match(2, "Match each sign of unit 47 to its meaning.",
              [["उत्क्लेश", "nausea"], ["श्लेष्मोद्वमन", "bringing up phlegm"], ["भक्तद्वेष", "aversion to food"],
               ["श्वेतहस्तपादनेत्रता", "whiteness of hands, feet and eyes"], ["श्वास", "breathlessness"]],
              "Five of the seven Kapha signs.",
              "उत्क्लेश, श्लेष्मोद्वमन, भक्तद्वेष, श्वेतहस्तपादनेत्रता, श्वास.", role="extend",
              teaches="भक्त = food, meal; द्वेष = aversion: भक्तद्वेष = aversion to food."),
        mcq("discriminate", 3, "Which split of श्लेष्मोद्वमनम् is right?",
            ("श्लेष्म + उद्वमनम्", "अ + उ → ओ: श्लेष्म (phlegm, compound form) + उद्वमन (bringing up)."),
            [("श्लेष्मो + द्वमनम्", "द्वमन is not a word; the word is उद्वमन."),
             ("श्लेष्म + ओद्वमनम्", "ओद्वमन is not a word, and अ + ओ would give औ."),
             ("श्लेष्मे + उद्वमनम्", "ए before उ does not give ओ.")],
            "श्लेष्म + उद्वमनम्: अ + उ → ओ.",
            "अ + उ → ओ."),
        mcq("apply", 4, "By unit 47, what colour do the hands, feet and eyes take under Kapha?",
            ("White (श्वेत)", "श्वेतहस्तपादनेत्रता: whiteness of hands, feet and eyes."),
            [("Yellow (पीत)", "Yellow eyes, urine and nails belong to the Pitta picture, unit 46."),
             ("Coppery (ताम्र)", "Coppery-green is said of what is passed under Pitta, unit 46."),
             ("Dark (काल)", "The woman becomes dark (काली) under Pitta, unit 46.")],
            "Under Kapha the hands, feet and eyes are white.",
            "श्वेत + हस्त + पाद + नेत्र + ता."),
        mcq("transfer", 5, "By the rule of मधुरास्य (मधुर + आस्य), how is हिम + आलयः joined?",
            ("हिमालयः", "अ + आ → आ, as मधुर + आस्य → मधुरास्य."),
            [("हिमलयः", "The long आ is not lost; अ + आ gives आ."),
             ("हिमैलयः", "ऐ comes from अ + ए, not from अ + आ."),
             ("हिमोलयः", "ओ comes from अ + उ, not from अ + आ.")],
            "हिम + आलयः = हिमालयः, like मधुर + आस्य = मधुरास्य.",
            "अ + आ → आ.",
            teaches="A short अ followed by a long आ joins as आ: मधुर + आस्य → मधुरास्य."),
    ],
}

# ---------------------------------------------------------------- unit 48
AUTHORED["48"] = {
    "title": "तयोर्जीवनीयबृंहणीयमधुरौषधसिद्धानां सर्पिषामुपयोगः",
    "question": "By unit 48, what is used for those two conditions?",
    "rule": ("For those two (तयोः): the use (उपयोग) of ghees (सर्पिस्, plural) cooked (सिद्ध) with life-promoting "
             "(जीवनीय), nourishing (बृंहणीय) and sweet (मधुर) medicines (औषध). This appears to begin the treatment."),
    "limits": ("No verb is printed ('is to be made' is understood). तयोः is read as upaviṣṭaka and upaśuṣkaka. The "
               "members of the jīvanīya and bṛṃhaṇīya classes are not listed here, and no dose is given. A prose line."),
    "explain_hi": ("यह गद्य-पंक्ति सम्भवतः उपविष्टक और उपशुष्कक की चिकित्सा आरम्भ करती है। "
                   "उन दोनों के लिए (तयोः) ऐसे घृतों (सर्पिषाम्, बहुवचन) का उपयोग कहा गया है जो जीवनीय यानी जीवन देने वाले, "
                   "बृंहणीय यानी पुष्ट करने वाले और मधुर औषधों से पकाए गए (सिद्ध) हों। "
                   "जीवनीय और बृंहणीय औषधों के वर्ग हैं; उनके सदस्य यहाँ नहीं गिनाए गए, और मात्रा भी नहीं दी गई। "
                   "क्रिया नहीं है; ‘करना चाहिए’ समझा जाता है।"),
    "hook": "दोनों के लिए: जीवनीय, बृंहणीय, मधुर औषधों से पके घी।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 48, what is to be used for those two?",
            ("Medicated ghees", "सर्पिषामुपयोगः: the use of ghees cooked with medicines."),
            [("Bloodletting with leeches", "Bloodletting is not named in unit 48."),
             ("Oil dropped into the ears", "Ear drops are not named in unit 48."),
             ("Cold water on the head", "Cold water on the head is not named in unit 48.")],
            "Ghees cooked with life-promoting, nourishing and sweet medicines.",
            "सर्पिषाम् उपयोगः."),
        order(1, "Put the words of unit 48 in the line's order.",
              ["तयोः", "जीवनीय", "बृंहणीय", "मधुरौषधसिद्धानां", "सर्पिषाम्", "उपयोगः"],
              "For those two, life-promoting, nourishing, cooked with sweet medicines, of ghees, the use.",
              "तयोः → जीवनीय → बृंहणीय → मधुरौषधसिद्धानां → सर्पिषाम् → उपयोगः."),
        match(2, "Match each word of unit 48 to its meaning.",
              [["जीवनीय", "life-promoting"], ["बृंहणीय", "nourishing"], ["औषध", "medicine"],
               ["सिद्ध", "cooked, prepared"], ["सर्पिस्", "ghee"]],
              "Ghees cooked with three kinds of medicine.",
              "जीवनीय, बृंहणीय, औषध, सिद्ध, सर्पिस्.", role="extend",
              teaches="सिद्ध after a list of drugs = cooked with them: ...औषधसिद्ध = cooked with the medicines."),
        mcq("discriminate", 3, "Which split of मधुरौषध is right?",
            ("मधुर + औषध", "अ + औ → औ: मधुर (sweet) + औषध (medicine)."),
            [("मधुर + उषध", "अ + उ would give ओ (मधुरोषध), not औ."),
             ("मधुरे + औषध", "ए before औ would not give औ."),
             ("मधुरौ + षध", "षध is not a word; the word is औषध.")],
            "मधुर + औषध: अ + औ → औ.",
            "अ + औ → औ."),
        multi("apply", 4, "Which statements about unit 48 are right by the card?",
              [("It lists the members of the jīvanīya class", "The members are not listed here."),
               ("सर्पिषाम् is plural: more than one ghee", "Right: the note says plural."),
               ("It gives the dose of each ghee", "No dose is given."),
               ("No verb is printed in the line", "Right: the use 'is to be made' is understood.")],
              [1, 3],
              "Plural ghees, no verb, no list of class members and no dose.",
              "तयोः ... सर्पिषाम् उपयोगः."),
        mcq("transfer", 5, "By the rule of तयोर्जीवनीय, how is गुरोः + वचनम् (the teacher's word) joined?",
            ("गुरोर्वचनम्", "A visarga after ओ before a voiced sound becomes र्, as तयोः + जीवनीय."),
            [("गुरो वचनम्", "The visarga after ओ is not simply dropped before व."),
             ("गुरोश्वचनम्", "The visarga becomes श् before च, छ or श, not before व."),
             ("गुरोऽवचनम्", "ऽ marks a dropped अ; no अ follows here.")],
            "गुरोः + वचनम् = गुरोर्वचनम्, like तयोः + जीवनीय = तयोर्जीवनीय.",
            "ओः + voiced sound → ओर्.",
            teaches="A visarga after a vowel other than अ/आ becomes र् before a voiced sound: तयोः + जीवनीय → तयोर्जीवनीय."),
    ],
}

# ---------------------------------------------------------------- unit 49
AUTHORED["49"] = {
    "title": "तथा पयसां रसानामामगर्भाणां च",
    "question": "By unit 49, what further things are used likewise?",
    "rule": ("Likewise (तथा), the use of milks (पयस्), rasas (juices or broths) and āmagarbhas (literally 'raw fetuses'), "
             "promoting the growth of the fetus (गर्भवृद्धिकर). The masculine करः agrees with उपयोगः of unit 48."),
    "limits": ("'Growth' rests on a near-certain correction (printed गर्भविद्धिकरः). The sense of rasa is not settled, and "
               "āmagarbha is kept as printed, sense uncertain, whose not said: no question asks what they are. No verb; a prose line."),
    "explain_hi": ("यह गद्य-पंक्ति इकाई ४८ के ‘उपयोगः’ को आगे बढ़ाती है: वैसे ही (तथा) दूधों (पयसाम्), रसों (रसानाम्) और "
                   "आमगर्भों (आमगर्भाणाम्) का उपयोग, जो गर्भ की वृद्धि करने वाला है। "
                   "छपा ‘गर्भविद्धिकरः’ लगभग निश्चित रूप से ‘गर्भवृद्धिकरः’ पढ़ा गया है। "
                   "‘रस’ का अर्थ यहाँ मांस-रस या अन्य रस, तय नहीं; ‘आमगर्भ’ (शब्दार्थ: कच्चा गर्भ) छपे रूप में रखा गया है, अर्थ अनिश्चित है। "
                   "पुंलिंग ‘करः’ इकाई ४८ के ‘उपयोगः’ से मेल खाता है।"),
    "hook": "तथा: दूध, रस, आमगर्भ; गर्भ-वृद्धि के लिए।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 49, which of these is named, likewise, for use?",
            ("Milks (पयस्)", "पयसाम्: of milks."),
            [("Wines (मद्य)", "Madya is named in unit 33, for another case, not here."),
             ("Sesame oils (तैल)", "Oil is not named in unit 49."),
             ("Honey (मधु)", "Honey is not named in unit 49.")],
            "Milks, rasas and āmagarbhas are named.",
            "पयसां रसानाम् आमगर्भाणां च."),
        order(1, "Put the words of unit 49 in the line's order.",
              ["तथा", "पयसां", "रसानाम्", "आमगर्भाणां", "च"],
              "Likewise, of milks, of rasas, of āmagarbhas, and.",
              "तथा → पयसां → रसानाम् → आमगर्भाणां → च."),
        match(2, "Match each word of unit 49 to its meaning.",
              [["तथा", "likewise"], ["पयस्", "milk"], ["आम", "raw, unripe"], ["वृद्धि", "growth"],
               ["कर", "making, promoting"]],
              "Likewise, milks and the others, promoting growth.",
              "तथा, पयस्, आम, वृद्धि, कर.", role="extend",
              teaches="-कर at the end of a compound = making: गर्भवृद्धिकर = making the growth of the fetus."),
        mcq("discriminate", 3, "By the data, why is करः (making) masculine in unit 49?",
            ("It agrees with उपयोगः of unit 48", "The note: masculine करः agrees with the understood उपयोगः."),
            [("It agrees with the word पयसाम्", "पयस् is neuter, and पयसाम् is a genitive plural."),
             ("It agrees with the word गर्भ alone", "गर्भ is the first member of the compound, not the noun it qualifies."),
             ("It is a verb in the third person", "करः is a noun-form ending (nom. sg.), not a verb.")],
            "करः qualifies the understood उपयोगः (use) of unit 48.",
            "उपयोगः (m.) ... गर्भवृद्धिकरः (m.)."),
        multi("apply", 4, "Which statements about unit 49 are right by the card?",
              [("Rasa here certainly means meat broth", "The note: meat broth or other juices, not settled."),
               ("The sense of rasa is not settled", "Right: the note leaves it open."),
               ("āmagarbha is kept as printed, sense uncertain", "Right: kept as printed, not enriched."),
               ("The text says whose āmagarbha is meant", "The note: the text does not say whose.")],
              [1, 2],
              "Rasa and āmagarbha are kept open, as the data leaves them.",
              "रसानाम्, आमगर्भाणाम्: sense not settled."),
        mcq("transfer", 5, "By the rule of रसानामामगर्भाणाम्, how is फलानाम् + आम्राणाम् written joined?",
            ("फलानामाम्राणाम्", "A final म् before a vowel stays म् and joins it, as रसानाम् + आमगर्भाणाम्."),
            [("फलानांआम्राणाम्", "The anusvāra stands before a consonant, not before a vowel."),
             ("फलानाम्राणाम्", "The म् is not lost; it stays and the vowel follows it."),
             ("फलानोम्राणाम्", "म् + आ does not make an ओ.")],
            "फलानाम् + आम्राणाम् = फलानामाम्राणाम्, like रसानाम् + आमगर्भाणाम्.",
            "म् + vowel → म् joined to the vowel.",
            teaches="A word-final म् before a vowel stays म् and is written joined to it: रसानाम् + आमगर्भाणाम् → रसानामामगर्भाणाम्."),
    ],
}

# ---------------------------------------------------------------- unit 50
AUTHORED["50"] = {
    "title": "तथा संभोजनमेतैरेव च घृतादिभिः",
    "question": "By unit 50, with what is the feeding done?",
    "rule": ("Likewise (तथा), feeding (संभोजन) with these very ones (एतैरेव), with ghee and the others (घृतादिभिः). "
             "No verb is printed."),
    "limits": ("The nouns of एतैः are not stated; 'these very ones' is read as ghee and the like. Who is fed is not stated "
               "(the woman is the natural reading): no question rests on it. No amount is given. A prose line."),
    "explain_hi": ("यह छोटी गद्य-पंक्ति कहती है: वैसे ही (तथा) इन्हीं (एतैरेव) घृत आदि (घृतादिभिः) के साथ भोजन कराना (संभोजन)। "
                   "‘एतैः’ किन वस्तुओं को कहता है, नाम नहीं दिए; घृत और वैसी ही वस्तुएँ पढ़ा गया है। "
                   "भोजन किसे कराया जाए, यह नहीं कहा; स्त्री स्वाभाविक अर्थ है। "
                   "क्रिया नहीं है, और मात्रा नहीं दी गई।"),
    "hook": "तथा: इन्हीं घृत आदि के साथ भोजन।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 50, with what is the feeding done?",
            ("With ghee and the others", "एतैरेव च घृतादिभिः: with these very ones, ghee and the others."),
            [("With birds' meat alone", "Meat is not named in unit 50."),
             ("With cold water alone", "Water is not named in unit 50."),
             ("With nothing; she fasts", "Unit 50 names feeding (संभोजन), not fasting.")],
            "With these very ones, ghee and the others.",
            "संभोजनम् एतैः एव च घृतादिभिः."),
        order(1, "Put the words of unit 50 in the line's order.",
              ["तथा", "संभोजनम्", "एतैरेव", "च", "घृतादिभिः"],
              "Likewise, feeding, with these very ones, and, with ghee and the others.",
              "तथा → संभोजनम् → एतैरेव → च → घृतादिभिः."),
        match(2, "Match each word of unit 50 to its meaning.",
              [["संभोजन", "feeding"], ["एतैः", "with these"], ["एव", "very, just"], ["घृत", "ghee"],
               ["आदि", "and the others"]],
              "Feeding with these very ones, ghee and the like.",
              "संभोजन, एतैः, एव, घृत, आदि.", role="extend",
              teaches="एव after a pronoun stresses it: एतैरेव = with these very ones."),
        mcq("discriminate", 3, "Which split of एतैरेव is right?",
            ("एतैः + एव", "A visarga after ऐ before a vowel becomes र्: एतैः + एव → एतैरेव."),
            [("एतै + रेव", "रेव is not a word; the word is एव (very)."),
             ("एते + एव", "ए + ए would give एत एव, with no र्."),
             ("एतैर + एव", "एतैर is not a form; the instrumental is एतैः.")],
            "एतैः (with these) + एव (very): ऐः + vowel → ऐर्.",
            "ऐः + vowel → ऐर्."),
        multi("apply", 4, "Which statements about unit 50 are right by the card?",
              [("It names a new drug not met before", "It refers back: these very ones, ghee and the like."),
               ("It gives the amount of ghee", "No amount is given."),
               ("The nouns of एतैः are not stated", "Right: the note says they are not stated."),
               ("No verb is printed in the line", "Right: the line is elliptical.")],
              [2, 3],
              "A verbless line that points back to ghee and the like.",
              "तथा संभोजनम् एतैः एव."),
        mcq("transfer", 5, "By the sense of घृतादिभिः, what does फलादिभिः mean?",
            ("With fruits and the like", "आदि closing a compound = and the others: फल + आदि."),
            [("Without any of the fruits", "आदि does not negate; 'without' would need a word like विना."),
             ("From one single fruit", "-भिः is plural (with), and आदि adds others."),
             ("For the fruits alone", "आदि adds others; it does not restrict.")],
            "फल + आदि + भिः = with fruits and the like, as घृत + आदि + भिः = with ghee and the others.",
            "X-आदि = X and the others.",
            teaches="आदि at the end of a compound means 'and the others': घृतादिभिः = with ghee and the others."),
    ],
}

# ---------------------------------------------------------------- unit 51
AUTHORED["51"] = {
    "title": "सुभिक्षाया अभीक्ष्णं यानवाहनादिभिः",
    "question": "By unit 51, by what means is the 'bringing about' (upapādana) done, repeatedly?",
    "rule": ("Of one well provided with food (सुभिक्षा), repeatedly (अभीक्ष्णम्), the bringing about (उपपादन) by carriages, "
             "vehicles and the like (यानवाहनादिभिः), and by shaking (क्षोभण), rubbing (मार्जन) and yawning (जृम्भण) (means or result: open). Sense not firm."),
    "limits": ("Low confidence: the sense is not firm. The object of उपपादन is not stated, and whether shaking, rubbing and "
               "yawning are means or what is brought about is open: no question rests on either. मार्जन may be wiping; जृम्भण stretching."),
    "explain_hi": ("इस गद्य-पंक्ति का अर्थ पक्का नहीं है (विश्वास निम्न)। "
                   "शब्दों से: भली-भाँति भोजन पाने वाली (सुभिक्षा) स्त्री का, बार-बार (अभीक्ष्णम्), यान, वाहन आदि से, और क्षोभण "
                   "(हिलाना), मार्जन (रगड़ना या पोंछना) और जृम्भण (जम्हाई या अँगड़ाई) से उपपादन (कराना, सम्पन्न करना)। "
                   "उपपादन किस वस्तु का है, यह नहीं कहा; और क्षोभण आदि साधन हैं या फल, यह खुला है। "
                   "क्रिया नहीं है।"),
    "hook": "बार-बार यान-वाहन, हिलाना, रगड़ना, जम्हाई (अर्थ पक्का नहीं)।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 51, how often is the 'bringing about' (upapādana) done?",
            ("Repeatedly (अभीक्ष्णम्)", "अभीक्ष्णम् = repeatedly."),
            [("Once only (सकृत्)", "The unit says अभीक्ष्णम्, repeatedly."),
             ("Every third day", "No interval is named in unit 51."),
             ("Only at night", "No time of day is named in unit 51.")],
            "It is done repeatedly.",
            "अभीक्ष्णम् = repeatedly."),
        order(1, "Put the words of unit 51 in the line's order.",
              ["सुभिक्षाया", "अभीक्ष्णं", "यानवाहनादिभिः", "क्षोभणमार्जनजृंभणैः", "उपपादनं"],
              "Of one well fed, repeatedly, by carriages, vehicles and the like, by shaking, rubbing and yawning, the bringing about.",
              "सुभिक्षाया → अभीक्ष्णं → यानवाहनादिभिः → क्षोभणमार्जनजृंभणैः → उपपादनं."),
        match(2, "Match each word of unit 51 to its meaning.",
              [["यान", "carriage, riding"], ["वाहन", "vehicle, conveyance"], ["क्षोभण", "shaking, jolting"],
               ["मार्जन", "rubbing or wiping"], ["जृम्भण", "yawning or stretching"]],
              "The words of the line; मार्जन and जृम्भण each have two senses in the data.",
              "यान, वाहन, क्षोभण, मार्जन, जृम्भण.", role="extend",
              teaches="उपपादन = bringing about, arranging; its object is not stated in unit 51."),
        mcq("discriminate", 3, "Which split of सुभिक्षाया अभीक्ष्णम् is right?",
            ("सुभिक्षायाः + अभीक्ष्णम्", "आः before a vowel drops its visarga, and the words stay apart."),
            [("सुभिक्षाया + अभीक्ष्णम्", "आ + अ would merge into सुभिक्षायाभीक्ष्णम्, one word."),
             ("सुभिक्षायाम् + अभीक्ष्णम्", "म् would stay and join: सुभिक्षायामभीक्ष्णम्."),
             ("सुभिक्षायः + अभीक्ष्णम्", "अः + अ would give सुभिक्षायोऽभीक्ष्णम्, with ओऽ.")],
            "सुभिक्षायाः (of her well fed) + अभीक्ष्णम्: the visarga after आ drops before a vowel; no further joining.",
            "आः + vowel → आ (visarga dropped, gap kept)."),
        multi("apply", 4, "Which statements about unit 51 are right by the card?",
              [("The object of उपपादन is not stated", "Right: the note says it is not stated."),
               ("The sense of the line is firm", "The data says the sense is not firm (low confidence)."),
               ("It names one particular vehicle", "Only यान, वाहन and the like (आदि) are named, in general."),
               ("Means or result: the instrumentals are open", "Right: the note leaves this open.")],
              [0, 3],
              "The line's sense is not firm: the object and the role of the instrumentals are open.",
              "सुभिक्षाया अभीक्ष्णं ... उपपादनम्: sense not firm."),
        mcq("transfer", 5, "By the rule of सुभिक्षाया अभीक्ष्णम्, how is बालाः + आगच्छन्ति (the boys come) joined?",
            ("बाला आगच्छन्ति", "After आ the visarga drops before a vowel, and the gap stays."),
            [("बालागच्छन्ति", "After the visarga drops, the two vowels are not merged again."),
             ("बालो आगच्छन्ति", "ओ comes from a visarga after short अ, not after आ."),
             ("बालार् आगच्छन्ति", "र् comes after vowels other than अ and आ.")],
            "बालाः + आगच्छन्ति = बाला आगच्छन्ति, like सुभिक्षायाः + अभीक्ष्णम् = सुभिक्षाया अभीक्ष्णम्.",
            "आः + vowel → आ (visarga dropped, no further sandhi).",
            teaches="A visarga after आ is dropped before a vowel, and the vowels do not merge: सुभिक्षायाः + अभीक्ष्णम् → सुभिक्षाया अभीक्ष्णम्."),
    ],
}

# ---------------------------------------------------------------- unit 52
AUTHORED["52"] = {
    "title": "अथ विशेषेण वाते ... शाल्योदनं भोजयेत्",
    "question": "By unit 52, what is done first in the Vāta case, and what is she fed?",
    "rule": ("Especially in Vāta (विशेषेण वाते): first (पूर्वमेव) give a milk-basti (क्षीरबस्ति, milk enema) with saindhava "
             "(rock salt); then feed her, bathed in cold water, soft boiled śāli rice (मृदु शाल्योदन)."),
    "limits": ("'Bathed' rests on a near-certain correction (printed स्त्रातां read स्नाताम्); printed दत्वा is read दत्त्वा. No "
               "question rests on the bath. No amounts are given. Rock salt and śāli as a winter rice are standard. A prose line."),
    "explain_hi": ("यह गद्य-पंक्ति वात की विशेष चिकित्सा का क्रम बताती है। "
                   "पहले ही (पूर्वमेव) सैन्धव यानी सेंधा नमक से युक्त क्षीरबस्ति (दूध की एनिमा) देकर (दत्वा), "
                   "ठंडे जल से नहाई हुई स्त्री को मृदु शालि-ओदन यानी नरम पका शालि चावल खिलाए (भोजयेत्)। "
                   "छपा ‘स्त्रातां’ लगभग निश्चित रूप से ‘स्नाताम्’ (नहाई हुई) पढ़ा गया है, और ‘दत्वा’ का शुद्ध रूप ‘दत्त्वा’ है। "
                   "‘भोजयेत्’ प्रेरणार्थक विधिलिङ् है: खिलाए।"),
    "hook": "वात: पहले नमक वाली दूध-बस्ति, फिर नरम शालि-भात।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 52, what is given first, especially in Vāta?",
            ("A milk enema with rock salt", "सैंधवोपहितं क्षीरबस्तिं दत्वा: a milk-basti with saindhava."),
            [("A purge with sharp drugs", "No purge is named in unit 52."),
             ("Oil poured on the head", "Oil on the head is not named in unit 52."),
             ("A fast of three whole days", "No fast is named in unit 52.")],
            "First a milk-basti provided with rock salt.",
            "पूर्वमेव सैंधवोपहितं क्षीरबस्तिं दत्वा."),
        order(1, "Put these phrases of unit 52 in the line's order.",
              ["अथ विशेषेण वाते", "पूर्वमेव", "सैंधवोपहितं क्षीरबस्तिं", "दत्वा", "मृदु शाल्योदनं", "भोजयेत्"],
              "Then especially in Vāta, first, a milk-basti with rock salt, having given, soft śāli rice, one should feed.",
              "अथ विशेषेण वाते → पूर्वमेव → सैंधवोपहितं क्षीरबस्तिं → दत्वा → मृदु शाल्योदनं → भोजयेत्."),
        match(2, "Match each word of unit 52 to its meaning.",
              [["सैन्धव", "rock salt"], ["क्षीरबस्ति", "milk enema"], ["मृदु", "soft"],
               ["ओदन", "boiled rice"], ["भोजयेत्", "one should feed"]],
              "Rock salt in the milk enema first; then soft boiled rice.",
              "सैन्धव, क्षीरबस्ति, मृदु, ओदन, भोजयेत्.", role="extend",
              teaches="उपहित = provided with: सैन्धवोपहित = provided with rock salt."),
        mcq("discriminate", 3, "Which split of शाल्योदनम् is right?",
            ("शालि + ओदनम्", "इ before a different vowel becomes य्: शालि + ओदनम् → शाल्योदनम्."),
            [("शाल्य + ओदनम्", "अ + ओ would give औ (शाल्यौदनम्), not यो."),
             ("शाले + ओदनम्", "ए before ओ does not give यो."),
             ("शाल् + योदनम्", "योदन is not a word; the word is ओदन (boiled rice).")],
            "शालि (śāli rice) + ओदनम् (boiled rice): इ + ओ → यो.",
            "इ + a different vowel → य् + that vowel."),
        mcq("apply", 4, "By unit 52, what kind of rice is she fed?",
            ("Soft boiled śāli rice", "मृदु शाल्योदनं भोजयेत्."),
            [("Hard, parched barley grains", "Barley is not named in unit 52; the rice is soft (मृदु)."),
             ("Rice gruel made sour", "No gruel and no sour taste are named in unit 52."),
             ("Raw, unboiled grains", "ओदन is boiled rice, and it is soft.")],
            "Soft śāli rice, boiled (ओदन).",
            "मृदु शाल्योदनम्."),
        mcq("transfer", 5, "By the rule of शाल्योदनम्, how is दधि + ओदनम् (curd-rice) joined?",
            ("दध्योदनम्", "इ before ओ becomes य्, as शालि + ओदनम्."),
            [("दधोदनम्", "The इ does not vanish; it becomes य्."),
             ("दध्यौदनम्", "इ + ओ gives यो, not यौ."),
             ("दधेदनम्", "इ + ओ does not give ए.")],
            "दधि + ओदनम् = दध्योदनम्, like शालि + ओदनम् = शाल्योदनम्.",
            "इ + ओ → यो.",
            teaches="A final इ before a different vowel becomes य्: शालि + ओदनम् → शाल्योदनम्."),
    ],
}

# ---------------------------------------------------------------- unit 53
AUTHORED["53"] = {
    "title": "ततो विदार्यादिगणसाधितेन सर्पिषाऽनुवासयेत्",
    "question": "By unit 53, what enema is given next, and with what?",
    "rule": ("Then (ततः) one should give an anuvāsana (अनुवासन, unctuous enema) with ghee (सर्पिस्) prepared (साधित) with "
             "the vidārī-and-others group (विदार्यादिगण; vidārī probably Pueraria tuberosa). It appears to continue unit 52."),
    "limits": ("Vidārī = Pueraria tuberosa is probable only. The members of the vidārī group are not listed here, and no "
               "amount is given. A prose line, appearing to continue the Vāta treatment of unit 52."),
    "explain_hi": ("यह गद्य-पंक्ति सम्भवतः इकाई ५२ के वात-उपचार को आगे बढ़ाती है। "
                   "फिर (ततः) विदारी आदि के गण से तैयार (साधित) घी (सर्पिस्) से अनुवासन दे (अनुवासयेत्), यानी घी या तेल की "
                   "चिकनाई वाली बस्ति। "
                   "विदारी की पहचान सम्भवतः विदारीकन्द (Pueraria tuberosa) है; यह सम्भावित है, निश्चित नहीं। "
                   "विदारी-आदि गण के सदस्य यहाँ नहीं गिनाए गए।"),
    "hook": "फिर: विदारी-गण के घी से अनुवासन।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 53, what kind of enema is given then?",
            ("An anuvāsana with ghee", "सर्पिषाऽनुवासयेत्: give an anuvāsana (unctuous enema) with ghee."),
            [("A milk enema with rock salt", "That is given first, in unit 52; unit 53 comes after it."),
             ("A cold water enema", "Cold water is not used for an enema in unit 53."),
             ("A honey enema, warm", "Honey is not named in unit 53.")],
            "Then an anuvāsana with ghee.",
            "सर्पिषा अनुवासयेत्."),
        order(1, "Put the words of unit 53 in the line's order.",
              ["ततः", "विदार्यादिगणसाधितेन", "सर्पिषा", "अनुवासयेत्"],
              "Then, prepared with the vidārī group, with ghee, one should give an anuvāsana.",
              "ततः → विदार्यादिगणसाधितेन → सर्पिषा → अनुवासयेत्."),
        match(2, "Match each word of unit 53 to its meaning.",
              [["विदारी", "probably Pueraria tuberosa (Indian kudzu)"], ["गण", "group"], ["साधित", "prepared"],
               ["सर्पिस्", "ghee"], ["अनुवासन", "unctuous (oil or ghee) enema"]],
              "Ghee prepared with the vidārī group, used for an anuvāsana.",
              "विदारी, गण, साधित, सर्पिस्, अनुवासन.", role="extend",
              teaches="अनुवासन = an oil or ghee enema; अनुवासयेत् = one should give it."),
        mcq("discriminate", 3, "Which split of विदार्यादि is right?",
            ("विदारी + आदि", "ई before a different vowel becomes य्: विदारी + आदि → विदार्यादि."),
            [("विदारा + आदि", "आ + आ would give विदारादि, with no य्."),
             ("विदारे + आदि", "ए before आ does not give या."),
             ("विदारि + यादि", "यादि is not a word; the word is आदि (and the others).")],
            "विदारी + आदि: ई + आ → या.",
            "ई + a different vowel → य् + that vowel."),
        multi("apply", 4, "Which statements about unit 53 are right by the card?",
              [("The ghee is prepared with the vidārī group", "Right: विदार्यादिगणसाधितेन सर्पिषा."),
               ("It lists all members of the vidārī group", "The members are not listed here."),
               ("The enema given here is of milk", "Here it is an anuvāsana with ghee; the milk enema is unit 52."),
               ("Vidārī is probably Pueraria tuberosa", "Right: the data labels it probable.")],
              [0, 3],
              "Ghee prepared with the vidārī group (vidārī probably Pueraria tuberosa) is used for an anuvāsana.",
              "विदार्यादिगणसाधितेन सर्पिषा अनुवासयेत्."),
        mcq("transfer", 5, "By the rule of ततो विदार्यादि, how is नरः + वदति (the man speaks) joined?",
            ("नरो वदति", "अः before a voiced sound becomes ओ, as ततः + विदारी."),
            [("नरर्वदति", "र् comes after vowels other than अ and आ."),
             ("नरा वदति", "The visarga after short अ does not leave a long आ."),
             ("नरः वदति", "Before a voiced sound the visarga after अ does not stay.")],
            "नरः + वदति = नरो वदति, like ततः + विदार्यादि = ततो विदार्यादि.",
            "अः + voiced consonant → ओ.",
            teaches="A visarga after अ becomes ओ before a voiced consonant: ततः + विदार्यादि → ततो विदार्यादि."),
    ],
}

# ---------------------------------------------------------------- unit 54
AUTHORED["54"] = {
    "title": "निवातं च सेवेत",
    "question": "By unit 54, what should one resort to?",
    "rule": ("And one should resort to (सेवेत) a wind-sheltered place or state (निवात). सेवेत is the optative middle of "
             "√सेव्: one should resort to. It appears to continue units 52-53."),
    "limits": ("Three words. Who resorts (the woman is the natural reading) and for how long are not stated. निवात is "
               "kept as the data glosses it, a wind-sheltered state or place; not enriched. A prose line."),
    "explain_hi": ("तीन शब्दों की यह गद्य-पंक्ति इकाई ५२-५३ के वात-उपचार में सम्भवतः जोड़ती है: और निवात यानी वायु से बचे स्थान या अवस्था "
                   "का सेवन करे (सेवेत)। "
                   "‘सेवेत’ आत्मनेपद विधिलिङ् है: सेवन करना चाहिए। "
                   "कौन और कितने समय तक, यह नहीं कहा। "
                   "छपे ‘निवातं च’ में म् व्यंजन से पहले अनुस्वार हो गया है।"),
    "hook": "वात में: हवा से बचो, निवात में रहो।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 54, what should one resort to?",
            ("Shelter from the wind", "निवातं च सेवेत: resort to a wind-sheltered place."),
            [("Open and breezy places", "The unit says the opposite: निवात, shelter from the wind."),
             ("Bathing in a cold river", "Bathing is not named in unit 54."),
             ("Sleeping on the open roof", "The unit names shelter from the wind, not open air.")],
            "Shelter from the wind (निवात).",
            "निवातं सेवेत."),
        order(1, "Put the words of unit 54 in the line's order.",
              ["निवातं", "च", "सेवेत"],
              "Shelter from the wind, and, one should resort to.",
              "निवातं → च → सेवेत."),
        match(2, "Match each word of unit 54 to its meaning.",
              [["निवात", "shelter from the wind"], ["च", "and"], ["सेवेत", "one should resort to"]],
              "Three words: and one should resort to shelter from the wind.",
              "निवात, च, सेवेत.", role="extend",
              teaches="सेवेत = optative middle of √सेव्: one should resort to, attend to."),
        mcq("discriminate", 3, "Which form of √सेव् means 'one should resort to'?",
            ("सेवेत", "Optative middle, 3 sg.: one should resort to."),
            [("सेवते", "Present middle: one resorts to (a fact, not 'should')."),
             ("सेवितः", "Past participle: resorted to, served."),
             ("सेविष्यते", "Future: one will resort to.")],
            "सेवेत is the optative: 'one should'.",
            "सेवते (present) → सेवेत (optative)."),
        mcq("apply", 4, "Why is निवातम् printed निवातं before च in unit 54?",
            ("म् before a consonant is written ं", "A final म् before a consonant becomes anusvāra (or the nasal of that consonant)."),
            [("The ं marks a dual ending of the word", "निवातम् is accusative singular in the data, not dual."),
             ("म् is always ं in every place", "Before a vowel म् stays: निवातम् + एव → निवातमेव."),
             ("The ं is a later printer's error", "It is regular sandhi, not an error.")],
            "निवातम् + च → निवातं च: म् before a consonant → ं.",
            "म् + consonant → ं."),
        mcq("transfer", 5, "By the form सेवेत (from सेवते), what does लभेत (from लभते, obtains) mean?",
            ("One should obtain", "Like सेवेत, लभेत is the optative middle: one should obtain."),
            [("One obtains now", "That is the present, लभते."),
             ("One obtained it", "A past form would be e.g. अलभत, not लभेत."),
             ("One will obtain", "The future is लप्स्यते, not लभेत.")],
            "लभते → लभेत (one should obtain), like सेवते → सेवेत (one should resort to).",
            "Thematic middle present -अते → optative -एत.",
            teaches="For a thematic middle verb like सेवते, the optative 3 sg. ends in -एत: सेवेत = one should resort to."),
    ],
}

# ===================================================================== NOTES_HI
NOTES_HI = {
    "41": ("गद्य-पंक्ति; विश्वास निम्न। पाठ-चिह्न: (१) छपा ‘कादाचित्कार्त्तवपरिस्रावादल्पौ’ में पंचमी ‘परिस्रावात्’ द्विवचन क्रिया "
           "‘दृश्येते’ और ‘अल्पौ’ से मेल नहीं खाती; सम्भावित सुधार ‘परिस्रावावल्पौ’ (औ + अ → आव्; व का द पढ़ा जाना); "
           "(२) ‘प्रामात्’ ज्ञात शब्द नहीं, अस्पष्ट छोड़ा गया (शायद बिगड़ा ‘प्रमाणात्’)। इन पर प्रश्न नहीं। ‘तम्’ पुंलिंग: दशा या गर्भ, नहीं "
           "बताया। छपा ‘अपरिहीयमान’ न सहित (सामान्य वर्तनी र के बाद ण, जैसे इकाई ४२ में); छपा रूप रखा। ‘विवर्द्धते’ = विवर्धते, "
           "‘र्त्त’ = र्त (छपाई की आदत)। सन्धि जाँची: कादाचित्क + आर्तव → कादाचित्कार्तव (अ + आ → आ); अपरिहीयमानः + एव → "
           "अपरिहीयमान एव (अः + अ से भिन्न स्वर → अ); कुक्षिः + विवर्धते → कुक्षिर्विवर्धते (इः + घोष → इर्); तम् + उपविष्टकम् → "
           "तमुपविष्टकम्; उपविष्टकम् + इति → उपविष्टकमिति; इति + आचक्षते → इत्याचक्षते (इ + आ → या)।"),
    "42": ("गद्य-पंक्ति; विश्वास मध्यम। पाठ-चिह्न: छपा ‘गर्भाः’ (बहुवचन) एकवचन क्रिया ‘स्पन्दते’ से मेल नहीं खाता; सम्भावित सुधार "
           "‘गर्भः’ (दीर्घ आ छपाई की भूल)। संख्या पर प्रश्न नहीं। छपा ‘चतथा’ = च तथा (और इसी प्रकार)। पहले खण्ड में क्रिया नहीं। "
           "वाक्य सम्भवतः इकाई ४३ में पूरा होता है (नाम वहीं)। ‘स्पंदते’ = स्पन्दते। सन्धि जाँची: प्रतिमासम् + आर्तवम् → प्रतिमासमार्तवम्; "
           "प्रति + अहम् → प्रत्यहम् (इ + अ → य); न + अति + अल्पम् → नात्यल्पम् (अ + अ → आ; इ + अ → य); परिहीयमाणः + गर्भः → "
           "परिहीयमाणो गर्भः (अः + घोष व्यंजन → ओ); चिरात् + किंचित् → चिरात्किंचित्।"),
    "43": ("गद्य-पंक्ति; विश्वास मध्यम। पाठ-चिह्न: छपा ‘चरिहीयते’ → ‘परिहीयते’ (लगभग निश्चित; प के स्थान पर च; धातु परि-√हा, जैसे "
           "इकाई ४१-४२ में)। उपशुष्कक और नागोदर एक दशा के दो नाम हैं या दो दशाएँ, शब्दों से तय नहीं; ‘नाग’ = साँप या हाथी; नागोदर "
           "नाम के रूप में रखा। इन पर प्रश्न नहीं। क्रिया ‘है’ समझी जाती है। सन्धि जाँची: कुक्षिः + च → कुक्षिश्च (विसर्ग + च → श्); "
           "वृद्धः + अपि → वृद्धोऽपि (अः + अ → ओऽ); तत् + उपशुष्ककम् → तदुपशुष्ककम् (त् + स्वर → द्); नाग + उदरम् → नागोदरम् "
           "(अ + उ → ओ)।"),
    "44": ("गद्य-पंक्ति; विश्वास मध्यम; कोई पाठ-चिह्न नहीं। ‘तौ’ (द्विवचन) का नाम पंक्ति में नहीं; डेटा उन्हें अभी कहे गए दो प्रकार "
           "(उपविष्टक, उपशुष्कक) पढ़ता है। ‘तेज’ = बल, सार भी पढ़ा जा सकता है। वर्षगण = वर्षों के समूह, संख्या नहीं। सन्धि जाँची: "
           "मातुः + आहार → मातुराहार (उः + स्वर → उर्); तेजसा + अल्पेन → तेजसाऽल्पेन (छपा रूप, ऽ के साथ); अल्पेन + आप्यायमानौ → "
           "अल्पेनाप्यायमानौ (अ + आ → आ); वर्षगणैः + अपि → वर्षगणैरपि (ऐः + स्वर → ऐर्); प्रसूयते + एव → प्रसूयत एव (ए + स्वर → "
           "अ, बीच में अन्तर)।"),
    "45": ("गद्य-पंक्ति; विश्वास मध्यम; कोई पाठ-चिह्न नहीं। ‘वातेन उपविष्टकोपशुष्ककयोः’ की रचना ढीली है (इन दोनों में, वात से)। "
           "‘अभीक्ष्णम्’ निद्रानाश या प्रतिश्याय से जुड़ सकता है (प्रतिश्याय के साथ रखा)। ‘तम इव प्रवेश्यते’ (छपा ‘तमइव’) = अन्धकार में "
           "प्रवेश जैसा (सम्भावित: चक्कर); अर्थ के दो रूप सम्भव। ‘पिपीलिकाभिरिव’ = रेंगने जैसा अनुभव (सम्भावित)। प्रतिश्याय = जुकाम "
           "(मानक); हृदय = हृदय (मानक)। ‘त्वक्त्त्वं’ में द्वित्व त् छपाई की आदत (त्वक्त्वम्)। सन्धि जाँची: वातेन + उपविष्टक → "
           "वातेनोपविष्टक (अ + उ → ओ); उपविष्टक + उपशुष्ककयोः → उपविष्टकोपशुष्ककयोः; शकृत् + उपवेश्यते → शकृदुपवेश्यते (त् + स्वर → द्); "
           "निद्रानाशः + अभीक्ष्णम् → निद्रानाशोऽभीक्ष्णम् (अः + अ → ओऽ); पिपीलिकाभिः + इव → पिपीलिकाभिरिव; परिकृन्तन् + इव → "
           "परिकृन्तन्निव (ह्रस्व स्वर के बाद न् का द्वित्व); दुःखेन + अन्नस्य → दुःखेनान्नस्य (अ + अ → आ)।"),
    "46": ("गद्य-पंक्ति; विश्वास मध्यम; कोई पाठ-चिह्न नहीं। ‘ताम्रहरितम्’ का संज्ञा-शब्द नहीं दिया (इकाई ४५ का शकृत् सम्भावित, जोड़ा "
           "नहीं)। ‘धूमिक’ और ‘अम्लक’ के अर्थ अनिश्चित (धुएँ जैसा, खट्टा); ‘पीतरक्तगोमूत्राभ’ को ‘पीला-लाल या गोमूत्र-आभा’ भी पढ़ा जा "
           "सकता है। इन पर प्रश्न नहीं। मूर्च्छा = बेहोशी (मानक)। ‘-त्व’ पूरी सूची (नेत्र, मूत्र, नख) पर भाववाचक। सन्धि जाँची: "
           "ताम्रहरितम् + उपवेश्यते → ताम्रहरितमुपवेश्यते; धूमिकः + अम्लकः → धूमिकोऽम्लकः (अः + अ → ओऽ); अम्लकः + छर्दिः → "
           "अम्लकश्छर्दिः (विसर्ग + छ → श्); छर्दिः + मूर्च्छा → छर्दिर्मूर्च्छा (इः + घोष → इर्); गोमूत्र + आभ → गोमूत्राभ।"),
    "47": ("गद्य-पंक्ति; विश्वास उच्च; कोई पाठ-चिह्न नहीं। क्रिया नहीं (इकाई ४६ जैसा)। उत्क्लेश = मिचली (मानक)। श्वास = साँस फूलना; "
           "दमा जैसा अर्थ केवल सम्भावित (शब्दार्थ में ‘मानक’ लिखा है, टिप्पणी में ‘सम्भावित’)। ‘श्लेष्मोद्वमन’ = कफ उगलना। सन्धि जाँची: "
           "मधुर + आस्य → मधुरास्य (अ + आ → आ); मधुरास्यत्वम् + उत्क्लेशः → मधुरास्यत्वमुत्क्लेशः; श्लेष्म + उद्वमनम् → श्लेष्मोद्वमनम् "
           "(अ + उ → ओ); श्वासः + च → श्वासश्च (विसर्ग + च → श्)।"),
    "48": ("गद्य-पंक्ति; विश्वास उच्च; कोई पाठ-चिह्न नहीं। क्रिया नहीं (‘करना चाहिए’ समझा जाता है)। ‘तयोः’ = उपविष्टक और उपशुष्कक। "
           "जीवनीय, बृंहणीय औषध-वर्ग हैं; सदस्य यहाँ नहीं। ‘सर्पिषाम्’ बहुवचन: एक से अधिक घी। छपा ‘सिद्धानांसर्पिषाम्’ बिना अन्तर। "
           "सन्धि जाँची: तयोः + जीवनीय → तयोर्जीवनीय (ओः + घोष → ओर्); मधुर + औषध → मधुरौषध (अ + औ → औ); सर्पिषाम् + उपयोगः → "
           "सर्पिषामुपयोगः।"),
    "49": ("गद्य-पंक्ति; विश्वास मध्यम। पाठ-चिह्न: छपा ‘गर्भविद्धिकरः’ → ‘गर्भवृद्धिकरः’ (लगभग निश्चित; ‘विद्धि’ = बेधना, यहाँ अर्थहीन; "
           "ऋ का इ पढ़ा जाना)। पुंलिंग ‘करः’ इकाई ४८ के ‘उपयोगः’ से मेल खाता है। ‘रस’ = मांस-रस या अन्य रस, तय नहीं; ‘आमगर्भ’ छपे रूप "
           "में, किसका, यह नहीं कहा, अर्थ अनिश्चित। इन पर प्रश्न नहीं। सन्धि जाँची: रसानाम् + आमगर्भाणाम् → रसानामामगर्भाणाम् "
           "(म् + स्वर); आम + गर्भ (सन्धि नहीं)।"),
    "50": ("गद्य-पंक्ति; विश्वास मध्यम; कोई पाठ-चिह्न नहीं। क्रिया नहीं। ‘एतैः’ की संज्ञाएँ नहीं दीं; घृत आदि पढ़ा गया। भोजन किसे, यह "
           "नहीं कहा (स्त्री स्वाभाविक अर्थ)। छपा ‘संभोजनम्’ = सम्भोजनम्। सन्धि जाँची: संभोजनम् + एतैः → संभोजनमेतैः; एतैः + एव → "
           "एतैरेव (ऐः + स्वर → ऐर्); घृत + आदिभिः → घृतादिभिः (अ + आ → आ)।"),
    "51": ("गद्य-पंक्ति; विश्वास निम्न; अर्थ पक्का नहीं। ‘सुभिक्षायाः’ स्त्री को समझकर पढ़ा गया; ‘उपपादनम्’ का कर्म नहीं दिया; "
           "‘क्षोभणमार्जनजृम्भणैः’ साधन हैं या फल, खुला है। मार्जन = पोंछना या रगड़ना; जृम्भण = जम्हाई या अँगड़ाई। इन पर प्रश्न नहीं। "
           "क्रिया नहीं। सन्धि जाँची: सुभिक्षायाः + अभीक्ष्णम् → सुभिक्षाया अभीक्ष्णम् (आः + स्वर → आ, विसर्ग लुप्त, आगे सन्धि नहीं); "
           "यान + वाहन + आदिभिः → यानवाहनादिभिः; जृम्भणैः + उपपादनम् → जृम्भणैरुपपादनम् (ऐः + स्वर → ऐर्)।"),
    "52": ("गद्य-पंक्ति; विश्वास उच्च। पाठ-चिह्न: (१) छपा ‘शीतोदकस्त्रातां’ → ‘शीतोदकस्नाताम्’ (लगभग निश्चित; ‘स्त्रात’ शब्द नहीं; "
           "यही इकाई ७७ में भी); (२) छपा ‘दत्वा’ → ‘दत्त्वा’ (सम्भावित; √दा का क्त्वा-रूप दत्त्वा)। स्नान पर प्रश्न नहीं। बस्ति = एनिमा "
           "(दूध की, नमक सहित)। सैन्धव = सेंधा नमक (मानक); शालि = जाड़े का धान (मानक); ओदन = पका भात। ‘मृदु’ भात के साथ पढ़ा गया। "
           "सन्धि जाँची: पूर्वम् + एव → पूर्वमेव; सैन्धव + उपहितम् → सैन्धवोपहितम् (अ + उ → ओ); शीत + उदक → शीतोदक; "
           "शालि + ओदनम् → शाल्योदनम् (इ + ओ → यो)।"),
    "53": ("गद्य-पंक्ति; विश्वास उच्च; कोई पाठ-चिह्न नहीं। इकाई ५२ (वात) का क्रम आगे। विदारी = विदारीकन्द, Pueraria tuberosa "
           "(सम्भावित); विदारी-आदि गण के सदस्य यहाँ नहीं। अनुवासन = तेल या घी की बस्ति (मानक)। साधित = तैयार किया। सन्धि जाँची: "
           "ततः + विदारी... → ततो विदारी... (अः + घोष → ओ); विदारी + आदि → विदार्यादि (ई + आ → या); सर्पिषा + अनुवासयेत् → "
           "सर्पिषाऽनुवासयेत् (छपा रूप, आ + अ → आ, ऽ के साथ)।"),
    "54": ("गद्य-पंक्ति; विश्वास उच्च; कोई पाठ-चिह्न नहीं। इकाई ५२-५३ का क्रम आगे। निवात (नपुं.) = वायु से बचा स्थान या अवस्था; "
           "अर्थ बढ़ाया नहीं। ‘सेवेत’ = √सेव् आत्मनेपद विधिलिङ्, प्रथम पुरुष एकवचन। सन्धि जाँची: निवातम् + च → निवातं च "
           "(व्यंजन से पहले म् → अनुस्वार)।"),
}

# ===================================================================== AIDS
AIDS = {
    "41": {
        "chunks": "तत्र यस्याः | कादाचित्कार्त्तवपरिस्रावादल्पौ (?) च दृश्येते | सततं च गर्भः | प्रामात् (?) परिमाणादपरिहीयमानएव स्फुरति | "
                  "न च कुक्षिर्विवर्द्धते | तमुपविष्टकमित्याचक्षते",
        "sandhi": "इः + घोष → इर्: कुक्षिः + विवर्धते → कुक्षिर्विवर्धते · इ + आ → या: इति + आचक्षते → इत्याचक्षते।",
        "frame": "किसमें: तत्र यस्याः → पक्के लक्षण: गर्भ निरन्तर फड़के (सततं स्फुरति), पेट न बढ़े (न कुक्षिर्विवर्धते) → नाम: "
                 "तम् उपविष्टकम् इति आचक्षते। (रज-स्राव वाला अंश अनुमानित पाठ)",
    },
    "42": {
        "chunks": "यदा तु | प्रतिमासमार्तवं | प्रत्यहं वा परिस्रवणं | नात्यल्पं | चतथा परिहीयमाणो गर्भाश्चिरात् | किंचित्स्पंदते",
        "sandhi": "इ + अ → य: प्रति + अहम् → प्रत्यहम् · अ + अ → आ: न + अति → नाति (नात्यल्पम्) · अः + घोष व्यंजन → ओ: "
                  "परिहीयमाणः + गर्भः → परिहीयमाणो गर्भः।",
        "frame": "कब: यदा → स्राव: हर मास आर्तव या हर दिन परिस्रवण, बहुत कम नहीं → गर्भ: घटता हुआ, देर से थोड़ा हिलता → नाम: "
                 "सम्भवतः अगली इकाई (४३) में।",
    },
    "43": {
        "diagram": {"groups": [
            {"label": "कुक्षि (पेट)", "items": ["बढ़ा हुआ होकर भी (वृद्धोऽपि)", "घटता है (सुधारा पाठ: परिहीयते)"]},
            {"label": "नाम", "items": ["उपशुष्कक (शब्दार्थ: सूखा हुआ)", "नागोदर", "एक दशा या दो: तय नहीं"]}]},
        "chunks": "कुक्षिश्च | वृद्धोऽपि | चरिहीयते (= परिहीयते) | तदुपशुष्ककं | नागोदरं च",
        "sandhi": "अः + अ → ओऽ: वृद्धः + अपि → वृद्धोऽपि · त् + स्वर → द्: तत् + उपशुष्ककम् → तदुपशुष्ककम् · अ + उ → ओ: "
                  "नाग + उदरम् → नागोदरम्।",
    },
    "44": {
        "chain": {"steps": ["माता के आहार का अल्प तेज", "उससे पोषण (आप्यायमानौ)", "जब पुष्ट हो जाएँ (यदा पुष्टौ)",
                            "तब वर्षों बाद भी (तदा वर्षगणैरपि)", "स्त्री प्रसव करती ही है"]},
        "chunks": "तौ तु | मातुराहारतेजसाऽल्पेनाप्यायमानौ | यदा पुष्टौ स्यातां | तदा वर्षगणैरपि | प्रमदा प्रसूयत एव",
        "sandhi": "उः + स्वर → उर्: मातुः + आहार → मातुराहार · ऐः + स्वर → ऐर्: वर्षगणैः + अपि → वर्षगणैरपि · ए + स्वर → अ "
                  "(अन्तर रहता है): प्रसूयते + एव → प्रसूयत एव।",
    },
    "45": {
        "diagram": {"groups": [
            {"label": "लक्षण (क्रम से)", "items": ["वायु का रुकना", "मल: शब्द, झाग, टूटा", "मूत्र रुकना",
                                                 "कमर, पीठ, हृदय में पीड़ा; जम्हाई", "नींद का नाश", "प्रतिश्याय (जुकाम)",
                                                 "सूखी खाँसी", "साद (थकावट)", "अन्न कठिनाई से पचे", "दिन-प्रतिदिन हानि",
                                                 "त्वचा फटी, विवर्ण, रूखी"]},
            {"label": "‘इव’ (मानो) वाले अनुभव", "items": ["कान मानो भनभनाएँ", "कनपटियाँ मानो चुभें",
                                                       "शरीर मानो चींटियों से जुड़ा", "वायु मानो काटता हुआ पेट में घूमे",
                                                       "मानो अन्धकार में प्रवेश"]}]},
        "chunks": "तत्र वातेनोपविष्टकोपशुष्ककयोर्वायुः प्रतिहन्यते | सशब्दं फेनिलं विच्छिन्नं शकृदुपवेश्यते | मूत्रमुपरुध्यते | "
                  "कटीपृष्ठहृदयेषु वेदनाजृंभा | निद्रानाशोऽभीक्ष्णं प्रतिश्यायः शुष्ककासः सादः | क्ष्वेलेते इवकर्णौ तुद्येते इव शंखौ | "
                  "पिपीलिकाभिरिव संसृज्यते शरीरं | परिकृंतन्निव वायुर्भ्रमति कुक्षौ | तमइव प्रवेश्यते | दुःखेनान्नस्य जरणमहरहः परिहानिः | "
                  "स्फुटितविवर्णपरुषत्वक्त्त्वं च भवति",
        "sandhi": "अ + उ → ओ: वातेन + उपविष्टक → वातेनोपविष्टक · त् + स्वर → द्: शकृत् + उपवेश्यते → शकृदुपवेश्यते · "
                  "अः + अ → ओऽ: निद्रानाशः + अभीक्ष्णम् → निद्रानाशोऽभीक्ष्णम् · अ + अ → आ: दुःखेन + अन्नस्य → दुःखेनान्नस्य।",
    },
    "46": {
        "diagram": {"groups": [
            {"label": "पित्त के लक्षण (क्रम से)", "items": ["ताम्र-हरित निकलना (संज्ञा नहीं दी)", "धूमिक, अम्लक (अर्थ अनिश्चित)",
                                                         "छर्दि (वमन)", "मूर्च्छा", "कुक्षि और हृदय में दाह",
                                                         "आँख, मूत्र, नख: पीले, लाल, गोमूत्र-आभा",
                                                         "स्त्री: काली, दुर्बल, नित्य पीड़ित"]}]},
        "chunks": "पित्तेन ताम्रहरितमुपवेश्यते | धूमिकोऽम्लकश्छर्दिर्मूर्च्छा | कुक्षिहृदयदाहः | पीतरक्तगोमूत्राभनेत्रमूत्रनखत्वं | "
                  "काली दुर्बला नित्यशूला च नारी भवति",
        "sandhi": "विसर्ग + छ → श्: अम्लकः + छर्दिः → अम्लकश्छर्दिः · इः + घोष → इर्: छर्दिः + मूर्च्छा → छर्दिर्मूर्च्छा · "
                  "अ + आ → आ: गोमूत्र + आभ → गोमूत्राभ।",
    },
    "47": {
        "diagram": {"groups": [
            {"label": "कफ के लक्षण (क्रम से)", "items": ["मुख मीठा", "उत्क्लेश (मिचली)", "कफ उगलना", "भोजन से द्वेष",
                                                      "हाथ, पैर, आँख श्वेत", "कास (खाँसी)", "श्वास (साँस फूलना)"]}]},
        "chunks": "श्लेष्मणा | मधुरास्यत्वमुत्क्लेशः | श्लेष्मोद्वमनं भक्तद्वेषः | श्वेतहस्तपादनेत्रता | कासः श्वासश्च",
        "sandhi": "अ + आ → आ: मधुर + आस्य → मधुरास्य · अ + उ → ओ: श्लेष्म + उद्वमनम् → श्लेष्मोद्वमनम् · विसर्ग + च → श्: "
                  "श्वासः + च → श्वासश्च।",
        "letters": "सात लक्षणों के पहले अक्षर क्रम से: म-उ-श्ले-भ-श्वे-का-श्वा (मधुरास्य, उत्क्लेश, श्लेष्मोद्वमन, भक्तद्वेष, "
                   "श्वेतता, कास, श्वास)। (मेरी याद-पद्धति)",
    },
    "48": {
        "diagram": {"groups": [
            {"label": "किनके लिए", "items": ["तयोः: उन दोनों के लिए"]},
            {"label": "घृत किन औषधों से पके", "items": ["जीवनीय", "बृंहणीय", "मधुर"]}]},
        "chunks": "तयोर्जीवनीयबृंहणीय | मधुरौषधसिद्धानां | सर्पिषामुपयोगः",
        "sandhi": "ओः + घोष → ओर्: तयोः + जीवनीय → तयोर्जीवनीय · अ + औ → औ: मधुर + औषध → मधुरौषध।",
        "frame": "किनके लिए: तयोः → क्या: सर्पिषाम् (घृतों का, बहुवचन) → कैसे घृत: जीवनीय, बृंहणीय, मधुर औषधों से सिद्ध → "
                 "उपयोगः (क्रिया समझी जाती है)।",
    },
    "49": {
        "chunks": "तथा | पयसां रसानामामगर्भाणां च | गर्भविद्धिकरः (= गर्भवृद्धिकरः)",
        "sandhi": "म् + स्वर: रसानाम् + आमगर्भाणाम् → रसानामामगर्भाणाम्।",
        "frame": "तथा (वैसे ही) → किनका उपयोग: पयस् (दूध), रस (अर्थ खुला), आमगर्भ (अर्थ अनिश्चित) → फल: गर्भ-वृद्धि करने वाला "
                 "(सुधारा पाठ); ‘करः’ इकाई ४८ के ‘उपयोगः’ से मेल।",
    },
    "50": {
        "chunks": "तथा | संभोजनमेतैरेव च | घृतादिभिः",
        "sandhi": "ऐः + स्वर → ऐर्: एतैः + एव → एतैरेव · अ + आ → आ: घृत + आदिभिः → घृतादिभिः।",
        "anchors": "याद-सूत्र: ‘एतैरेव’ = इन्हीं से: नया द्रव्य नहीं, पहले कहे घृत आदि ही। (मेरी याद-पद्धति)",
    },
    "51": {
        "chunks": "सुभिक्षाया अभीक्ष्णं | यानवाहनादिभिः | क्षोभणमार्जनजृंभणैः | उपपादनं",
        "sandhi": "आः + स्वर → आ (आगे सन्धि नहीं): सुभिक्षायाः + अभीक्ष्णम् → सुभिक्षाया अभीक्ष्णम् · ऐः + स्वर → ऐर्: "
                  "जृम्भणैः + उपपादनम् → जृम्भणैरुपपादनम्।",
        "frame": "किसका: सुभिक्षायाः (भली-भाँति भोजन पाने वाली का) → कब: अभीक्ष्णम् (बार-बार) → किनसे: यान-वाहन आदि; क्षोभण, "
                 "मार्जन, जृम्भण (साधन या फल, खुला) → उपपादनम् (कर्म नहीं दिया)।",
    },
    "52": {
        "chain": {"steps": ["वात में, पहले ही", "सेंधा नमक वाली दूध-बस्ति देना", "ठंडे जल से नहाई (सुधारा पाठ)",
                            "नरम शालि-भात खिलाना"]},
        "chunks": "अथ विशेषेण वाते | पूर्वमेव सैंधवोपहितं क्षीरबस्तिं दत्वा | शीतोदकस्त्रातां (= स्नातां) | मृदु शाल्योदनं भोजयेत्",
        "sandhi": "अ + उ → ओ: सैन्धव + उपहितम् → सैन्धवोपहितम् · इ + ओ → यो: शालि + ओदनम् → शाल्योदनम्।",
    },
    "53": {
        "chunks": "ततो | विदार्यादिगणसाधितेन | सर्पिषा ऽनुवासयेत्",
        "sandhi": "अः + घोष → ओ: ततः + विदारी... → ततो विदारी... · ई + आ → या: विदारी + आदि → विदार्यादि।",
        "frame": "कब: ततः (क्षीरबस्ति के बाद) → किससे: सर्पिषा (घी से) → घी कैसा: विदारी आदि गण से साधित → क्रिया: अनुवासयेत् "
                 "(अनुवासन बस्ति दे)।",
    },
    "54": {
        "chunks": "निवातं च | सेवेत",
        "sandhi": "व्यंजन से पहले म् → अनुस्वार: निवातम् + च → निवातं च।",
        "anchors": "याद-सूत्र: वात का रोग, तो ‘नि-वात’ (हवा से बचाव); सम्भवतः वात-उपचार का अगला अंग: बस्ति, अनुवासन, फिर निवात। (मेरी याद-पद्धति)",
    },
}

# ===================================================================== IMAGE_SPECS
IMAGE_SPECS = {
    ("43", "diagram"): {
        "file": "sh4-upashushkaka-43.svg",
        "alt": ("Flowchart of unit 43: the belly, though grown, diminishes (a corrected reading); that is called "
                "upaśuṣkaka and nāgodara; whether these are one condition or two is not settled."),
        "type": "mermaid",
        "code": ("flowchart TD\n"
                 "  A[\"कुक्षि बढ़ी हुई होकर भी\"] --> B[\"घटती है (सुधारा पाठ)\"]\n"
                 "  B --> C[\"नाम: उपशुष्कक\"]\n"
                 "  B --> D[\"नाम: नागोदर\"]\n"
                 "  C -.- E[\"एक दशा या दो: तय नहीं\"]\n"
                 "  D -.- E\n"),
    },
    ("44", "chain"): {
        "file": "sh4-varshagana-44.svg",
        "alt": ("Chain of unit 44: the slight tejas of the mother's food; nourished by it; when they become well nourished; "
                "then even after groups of years; the woman gives birth indeed."),
        "type": "chain",
        "title": "इकाई ४४: बरसों बाद भी प्रसव",
        "steps": ["माता के आहार का अल्प तेज", "उससे पोषण", "जब पुष्ट हो जाएँ", "तब वर्षों बाद भी",
                  "स्त्री प्रसव करती ही है"],
    },
    ("45", "diagram"): {
        "file": "sh4-vata-lakshana-45.svg",
        "alt": ("Two columns of unit 45, Vāta signs in upaviṣṭaka and upaśuṣkaka. Signs in order: vāyu obstructed; stool "
                "noisy, frothy, broken; urine held back; pain in waist, back, heart, and yawning; loss of sleep; catarrh; dry "
                "cough; lassitude; hard digestion; daily decline; skin cracked, discoloured, rough. 'As it were' sensations: "
                "ears hum; temples pricked; body as if joined with ants; vāyu as if cutting wanders in the belly; as if entering darkness."),
        "type": "split",
        "title": "इकाई ४५: वात के लक्षण",
        "cols": [["लक्षण (क्रम से)", ["१ वायु रुके", "२ मल: शब्द, झाग, टूटा", "३ मूत्र रुके",
                                      "४ कमर, पीठ, हृदय में पीड़ा; जम्हाई", "५ नींद का नाश", "६ जुकाम",
                                      "७ सूखी खाँसी", "८ थकावट", "९ अन्न कठिनाई से पचे", "१० दिन-प्रतिदिन हानि",
                                      "११ त्वचा फटी, विवर्ण, रूखी"]],
                 ["‘इव’ (मानो) वाले", ["कान मानो भनभनाएँ", "कनपटियाँ मानो चुभें", "शरीर मानो चींटियों से जुड़ा",
                                        "वायु मानो काटता, पेट में घूमे", "मानो अन्धकार में प्रवेश"]]],
    },
    ("46", "diagram"): {
        "file": "sh4-pitta-lakshana-46.svg",
        "alt": ("Table of unit 46, Pitta signs in line order: a coppery-green (one) is passed (noun not stated); dhūmika and "
                "amlaka (sense uncertain); vomiting; fainting; burning in belly and heart; eyes, urine and nails yellow, red, "
                "cow-urine-hued; the woman dark, weak, constantly in pain."),
        "type": "table",
        "title": "इकाई ४६: पित्त के लक्षण",
        "heads": ["छपा शब्द", "अर्थ"],
        "rows": [["ताम्रहरितमुपवेश्यते", "ताम्र-हरित निकलता (संज्ञा नहीं दी)"],
                 ["धूमिकोऽम्लकः", "अर्थ अनिश्चित"],
                 ["छर्दिः", "वमन"], ["मूर्च्छा", "बेहोशी"],
                 ["कुक्षिहृदयदाहः", "पेट और हृदय में जलन"],
                 ["...नेत्रमूत्रनखत्वं", "आँख, मूत्र, नख पीले, लाल, गोमूत्र-आभा"],
                 ["काली दुर्बला नित्यशूला", "स्त्री काली, दुर्बल, सदा पीड़ित"]],
    },
    ("47", "diagram"): {
        "file": "sh4-kapha-lakshana-47.svg",
        "alt": ("Table of unit 47, Kapha signs in line order: sweet mouth; nausea; bringing up phlegm; aversion to food; "
                "white hands, feet and eyes; cough; breathlessness."),
        "type": "table",
        "title": "इकाई ४७: कफ के लक्षण",
        "heads": ["छपा शब्द", "अर्थ"],
        "rows": [["मधुरास्यत्वम्", "मुख मीठा"], ["उत्क्लेशः", "मिचली"], ["श्लेष्मोद्वमनं", "कफ उगलना"],
                 ["भक्तद्वेषः", "भोजन से द्वेष"], ["श्वेतहस्तपादनेत्रता", "हाथ, पैर, आँख श्वेत"],
                 ["कासः", "खाँसी"], ["श्वासः", "साँस फूलना"]],
    },
    ("48", "diagram"): {
        "file": "sh4-sarpis-upayoga-48.svg",
        "alt": ("Flowchart of unit 48: for those two, the use of ghees, cooked with three kinds of medicine: life-promoting "
                "(jīvanīya), nourishing (bṛṃhaṇīya) and sweet (madhura)."),
        "type": "mermaid",
        "code": ("flowchart TD\n"
                 "  A[\"उन दोनों के लिए\"] --> B[\"घृतों का उपयोग\"]\n"
                 "  B --> C[\"पके: इन औषधों से\"]\n"
                 "  C --> D[\"जीवनीय\"]\n"
                 "  C --> E[\"बृंहणीय\"]\n"
                 "  C --> F[\"मधुर\"]\n"),
    },
    ("52", "chain"): {
        "file": "sh4-kshira-basti-52.svg",
        "alt": ("Chain of unit 52, the Vāta case: first; give a milk enema with rock salt; she bathed in cold water (a corrected "
                "reading); feed her soft boiled śāli rice."),
        "type": "chain",
        "title": "इकाई ५२: वात में पहले क्षीरबस्ति",
        "steps": ["वात में, पहले ही", "सेंधा नमक वाली दूध-बस्ति", "ठंडे जल से नहाई (सुधारा पाठ)", "नरम शालि-भात खिलाना"],
    },
}
