from helpers import mcq, match, order, fill, multi, accepts


AUTHORED = {}

# ---------------------------------------------------------------- unit 14
AUTHORED["14"] = {
    "title": "वायवीयानि स्पर्शनं स्पर्शः",
    "question": "By unit 14, which parts and qualities of the body belong to wind (vāyu)?",
    "rule": ("Those of wind (वायवीयानि): the touch faculty (स्पर्शन, the skin sense), touch (स्पर्श), the movements "
             "beginning with the two breaths (प्रश्वास, उच्छ्वास) and lightness (लाघव)."),
    "limits": ("A prose list, parallel to unit 13 (space). Which of प्रश्वास and उच्छ्वास is the out-breath and which the "
               "in-breath is not fixed in the data: no question on it. आदि (and so on) leaves the movements open."),
    "explain_hi": ("यह गद्य-पंक्ति बताती है कि शरीर में कौन-से भाव वायु से सम्बन्धित हैं। "
                   "पहले स्पर्शन, यानी स्पर्श की इन्द्रिय (त्वचा), और उसका विषय स्पर्श आता है, जैसे इकाई १३ में श्रोत्र और शब्द आए थे। "
                   "फिर प्रश्वास और उच्छ्वास आदि के स्पन्दन, यानी साँस से आरम्भ होने वाली शरीर की गतियाँ। "
                   "अन्त में लाघव, यानी हल्कापन। "
                   "प्रश्वास और उच्छ्वास में कौन बाहर की साँस है और कौन भीतर की, यह डेटा तय नहीं करता।"),
    "hook": "वायु: छूना, साँस की हलचल, हल्कापन।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 14, which quality of the body belongs to wind (vāyu)?",
            ("Lightness (lāghava)", "लाघवं च: lightness closes the wind list."),
            [("Heaviness (gaurava)", "Heaviness belongs to earth (unit 17), not to wind."),
             ("Unctuousness (sneha)", "Unctuousness belongs to water (unit 16), not to wind."),
             ("Steadiness (dhairya)", "Steadiness belongs to earth (unit 17), not to wind.")],
            "Wind gives the body lightness (लाघव).",
            "वायवीयानि ... लाघवं च."),
        order(1, "Put the items of unit 14 in the line's order.",
              ["वायवीयानि", "स्पर्शनं", "स्पर्शः", "प्रश्वासोच्छ्वासादिपरिस्पंदनानि", "लाघवं च"],
              "Of wind: the touch faculty, touch, the movements beginning with the breaths, and lightness.",
              "वायवीयानि → स्पर्शनं → स्पर्शः → ...परिस्पंदनानि → लाघवं च."),
        match(2, "Match each word of unit 14 to its meaning.",
              [["वायवीय", "belonging to wind"], ["स्पर्शन", "organ of touch, skin sense"], ["स्पर्श", "touch"],
               ["परिस्पन्दन", "movement"], ["लाघव", "lightness"]],
              "Of wind: the touch faculty and touch, the movements of the body, and lightness.",
              "वायवीय, स्पर्शन, स्पर्श, परिस्पन्दन, लाघव.", role="extend",
              teaches="स्पर्शन is the faculty (the skin sense); स्पर्श is what it senses, touch."),
        mcq("discriminate", 3, "Which split of प्रश्वासोच्छ्वास in unit 14 is right?",
            ("प्रश्वास + उच्छ्वास", "अ + उ → ओ: प्रश्वास + उच्छ्वास → प्रश्वासोच्छ्वास."),
            [("प्रश्वा + सोच्छ्वास", "प्रश्वा and सोच्छ्वास are not the words; the words are प्रश्वास and उच्छ्वास."),
             ("प्रश्वास + ओच्छ्वास", "ओच्छ्वास is not a word, and अ + ओ would give औ, not ओ."),
             ("प्रश्वासः + उच्छ्वास", "A compound member has no visarga, and अः + उ would not join to ओ.")],
            "प्रश्वास + उच्छ्वास = प्रश्वासोच्छ्वास: the two breaths, joined by अ + उ → ओ.",
            "अ + उ → ओ."),
        multi("apply", 4, "Which of these does unit 14 assign to wind?",
              [("Touch (sparśa)", "Right: स्पर्शः is in the wind list."),
               ("Sound (śabda)", "Sound is born of space (unit 13)."),
               ("Movements such as breathing", "Right: प्रश्वासोच्छ्वासादिपरिस्पंदनानि."),
               ("Form (rūpa)", "Form belongs to fire (unit 15).")],
              [0, 2],
              "Wind: the touch faculty, touch, the movements beginning with the breaths, lightness.",
              "वायवीयानि स्पर्शनं स्पर्शः ...परिस्पंदनानि लाघवं च."),
        mcq("transfer", 5, "By the rule of प्रश्वास + उच्छ्वास, how are सूर्य + उदयः (sunrise) joined?",
            ("सूर्योदयः", "अ + उ → ओ, as प्रश्वास + उच्छ्वास → प्रश्वासोच्छ्वास."),
            [("सूर्यौदयः", "औ comes from अ + ओ or औ, not from अ + उ."),
             ("सूर्यादयः", "आ comes from अ + अ, not from अ + उ."),
             ("सूर्युदयः", "अ before उ is not dropped; the two join as ओ.")],
            "सूर्य + उदयः = सूर्योदयः, like प्रश्वास + उच्छ्वास = प्रश्वासोच्छ्वास.",
            "अ + उ → ओ.",
            teaches="A short अ followed by उ joins as ओ: प्रश्वास + उच्छ्वास → प्रश्वासोच्छ्वास."),
    ],
}

# ---------------------------------------------------------------- unit 15
AUTHORED["15"] = {
    "title": "आग्नेयानि दर्शनं रूपं",
    "question": "By unit 15, which parts and qualities of the body belong to fire (agni)?",
    "rule": ("Those of fire (आग्नेयानि): sight (दर्शन), form (रूप), Pitta, heat (ऊष्मा), digestion (पक्ति), burning heat "
             "(संताप), intelligence (मेधा), colour (वर्ण), radiance (भा), brilliance (तेजस्) and valour (शौर्य)."),
    "limits": ("A prose list. Pitta is the doṣa and is given no modern name. वर्ण = colour (it may also mean complexion). "
               "...ऊष्मापक्तिः is read ऊष्मा + पक्तिः (digestion), not अपक्ति, by the data. Valour and intelligence recur in "
               "later lists (units 21, 23), which follow other schemes."),
    "explain_hi": ("यह गद्य-पंक्ति अग्नि से सम्बन्धित भाव गिनाती है। "
                   "पहले दर्शन, यानी देखने की इन्द्रिय, और उसका विषय रूप; फिर पित्त, ऊष्मा (गर्मी), पक्ति (पाचन) और सन्ताप। "
                   "इसके बाद मेधा, वर्ण (रंग), भा (दीप्ति), तेज और शौर्य आते हैं। "
                   "पित्त यहाँ दोष है; इसका कोई आधुनिक नाम नहीं दिया गया। "
                   "डेटा के अनुसार ‘ऊष्मापक्तिः’ = ऊष्मा + पक्तिः है, ‘अपक्ति’ नहीं।"),
    "hook": "अग्नि: आँख, रूप, पित्त, गर्मी, पाचन, चमक, शौर्य।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 15, which sense faculty belongs to fire (agni)?",
            ("Sight (darśana)", "दर्शनं: the organ of sight opens the fire list."),
            [("Hearing (śrotra)", "The ear is born of space (unit 13)."),
             ("Smell (ghrāṇa)", "The nose belongs to earth (unit 17)."),
             ("Taste (rasana)", "The tongue belongs to water (unit 16).")],
            "Fire gives sight (दर्शन) and its object, form (रूप).",
            "आग्नेयानि दर्शनं रूपं."),
        order(1, "Put the items of unit 15 in the line's order.",
              ["दर्शनं", "रूपं", "पित्तमूष्मापक्तिः", "संतापो मेधा", "वर्णो भास्तेजः", "शौर्य्यं च"],
              "Sight, form, Pitta-heat-digestion, burning heat and intelligence, colour-radiance-brilliance, valour.",
              "दर्शनं → रूपं → पित्तमूष्मापक्तिः → संतापो मेधा → वर्णो भास्तेजः → शौर्य्यं च."),
        match(2, "Match each word of unit 15 to its meaning.",
              [["ऊष्मा", "heat"], ["पक्ति", "digestion, cooking"], ["संताप", "burning heat"], ["मेधा", "intelligence"],
               ["भा", "radiance"], ["शौर्य", "valour"]],
              "Fire gives heat, digestion, burning heat, intelligence, radiance and valour, among others.",
              "ऊष्मा, पक्ति, संताप, मेधा, भा, शौर्य.", role="extend",
              teaches="पक्ति (from √पच्, to cook) = digestion, cooking: a fire item."),
        mcq("discriminate", 3, "Which split of भास्तेजः in unit 15 is right?",
            ("भाः + तेजः", "A visarga before त becomes स्: भाः + तेजः → भास्तेजः."),
            [("भा + स्तेजः", "स्तेजः is not a word; the word is तेजः, brilliance."),
             ("भास्ते + जः", "भास्ते and जः are not the words of the list."),
             ("भाः + स्तेजः", "स्तेजः is not a word; the स् comes from the visarga.")],
            "भाः (radiance) + तेजः (brilliance) = भास्तेजः.",
            "Visarga + त → स्त."),
        mcq("apply", 4, "A student lists the fire items of unit 15. Which one does not belong?",
            ("Lightness (lāghava)", "Lightness belongs to wind (unit 14), not to fire."),
            [("Intelligence (medhā)", "Intelligence is in the fire list: मेधा."),
             ("Burning heat (saṃtāpa)", "Burning heat is in the fire list: संतापो."),
             ("Colour (varṇa)", "Colour is in the fire list: वर्णो.")],
            "Lightness is wind's (unit 14); intelligence, burning heat and colour are fire's.",
            "आग्नेयानि ... संतापो मेधा वर्णो ..."),
        mcq("transfer", 5, "By the rule of भाः + तेजः, how are देवाः + तत्र (the gods there) joined?",
            ("देवास्तत्र", "A visarga before त becomes स्, as भाः + तेजः → भास्तेजः."),
            [("देवा तत्र", "आः loses its visarga before a voiced sound; त is unvoiced."),
             ("देवार्तत्र", "र् comes after vowels other than अ/आ, before a voiced sound."),
             ("देवाश्तत्र", "श् comes before च, छ or श, not before त.")],
            "देवाः + तत्र = देवास्तत्र, like भाः + तेजः = भास्तेजः.",
            "Visarga + त → स्त.",
            teaches="A visarga before त becomes स्: भाः + तेजः → भास्तेजः."),
    ],
}

# ---------------------------------------------------------------- unit 16
AUTHORED["16"] = {
    "title": "आंभसानि रसनं रसः",
    "question": "By unit 16, which parts and qualities of the body belong to water (ambhas)?",
    "rule": ("Those of water (आम्भसानि): the tongue (रसन), taste (रस), the mass of fluids (sweat, moisture, vasā, rasa, "
             "blood, semen, urine and so on), looseness (शैथिल्य) and unctuousness (स्नेह)."),
    "limits": ("A prose list. रस occurs twice: first taste, then, inside the compound, the rasa dhātu, the nutritive fluid "
               "(often equated with plasma or chyle: probable). वसा = muscle-fat is probable. The missing space after रसः is a print slip."),
    "explain_hi": ("यह गद्य-पंक्ति जल से सम्बन्धित भाव गिनाती है। "
                   "पहले रसन (जिह्वा) और उसका विषय रस (स्वाद)। "
                   "फिर द्रवों का समूह: स्वेद (पसीना), क्लेद (गीलापन), वसा (सम्भवतः मांसगत चर्बी), रस (पोषक द्रव), असृक् (रक्त), "
                   "शुक्र (वीर्य), मूत्र आदि। "
                   "अन्त में शैथिल्य (ढीलापन) और स्नेह (चिकनाई)। "
                   "ध्यान दें: पहला ‘रस’ स्वाद है और समास के भीतर का ‘रस’ पहली धातु, पोषक द्रव।"),
    "hook": "जल: जीभ, स्वाद, सारे द्रव, ढीलापन, चिकनाई।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 16, which quality does water (ambhas) give the body?",
            ("Unctuousness (sneha)", "स्नेहश्च: unctuousness closes the water list."),
            [("Steadiness (dhairya)", "Steadiness belongs to earth (unit 17)."),
             ("Heaviness (gaurava)", "Heaviness belongs to earth (unit 17)."),
             ("Brilliance (tejas)", "Brilliance belongs to fire (unit 15).")],
            "Water gives looseness (शैथिल्य) and unctuousness (स्नेह).",
            "... शैथिल्यं स्नेहश्च."),
        order(1, "Put the items of unit 16 in the line's order.",
              ["आंभसानि", "रसनं", "रसः", "...द्रवसमूहः", "शैथिल्यं", "स्नेहश्च"],
              "Of water: the tongue, taste, the mass of fluids, looseness, unctuousness.",
              "आंभसानि → रसनं → रसः → ...द्रवसमूहः → शैथिल्यं → स्नेहश्च."),
        match(2, "Match each fluid or quality of unit 16 to its meaning.",
              [["स्वेद", "sweat"], ["क्लेद", "moisture"], ["वसा", "muscle-fat (probable)"], ["असृज्", "blood (standard)"],
               ["शुक्र", "semen (standard)"], ["शैथिल्य", "looseness"]],
              "The mass of fluids and the qualities of water.",
              "स्वेद, क्लेद, वसा, असृज्, शुक्र, शैथिल्य.", role="extend",
              teaches="असृज् (असृक् before a consonant) = blood: असृक्शुक्र = blood and semen."),
        mcq("discriminate", 3, "In unit 16, what is the second रस, inside ...वसारसासृक्...?",
            ("The nutritive fluid, a dhātu", "The data: the second rasa is the rasa dhātu, the nutritive fluid."),
            [("Taste, like the first रसः", "The first रसः is taste; the second sits among the body's fluids."),
             ("Mercury of the alchemists", "Nothing in the unit speaks of mercury; it is a body fluid."),
             ("Juice pressed out of a fresh plant", "No plant is named; the compound lists the body's fluids.")],
            "रसः (taste) stands alone; the रस inside the fluid compound is the nutritive fluid.",
            "रसः = taste; ...वसारसासृक्... = vasā, rasa (nutritive fluid), blood."),
        multi("apply", 4, "Which of these does unit 16 name in its mass of fluids?",
              [("Bile (pitta)", "Pitta belongs to fire (unit 15)."),
               ("Sweat (sveda)", "Right: स्वेद opens the fluid compound."),
               ("Marrow (majjā)", "Marrow is listed as mother-born (unit 18), not here."),
               ("Urine (mūtra)", "Right: ...मूत्रादिद्रवसमूहः.")],
              [1, 3],
              "Sweat, moisture, vasā, rasa, blood, semen, urine and so on: the mass of fluids.",
              "स्वेदक्लेदवसारसासृक्शुक्रमूत्रादिद्रवसमूहः."),
        mcq("transfer", 5, "By the rule of स्नेहः + च, how are रामः + च (and Rāma) joined?",
            ("रामश्च", "A visarga before च becomes श्, as स्नेहः + च → स्नेहश्च."),
            [("रामो च", "अः becomes ओ only before a voiced sound; च is unvoiced."),
             ("रामस्च", "स् comes before त or थ, not before च."),
             ("रामर्च", "र् comes after vowels other than अ/आ, before a voiced sound.")],
            "रामः + च = रामश्च, like स्नेहः + च = स्नेहश्च.",
            "Visarga + च → श्च.",
            teaches="A visarga before च becomes श्: स्नेहः + च → स्नेहश्च."),
    ],
}

# ---------------------------------------------------------------- unit 17
AUTHORED["17"] = {
    "title": "पार्थिवानि घ्राणं गंधः",
    "question": "By unit 17, which parts and qualities of the body belong to earth (pṛthivī)?",
    "rule": ("Those of earth (पार्थिवानि): the nose (घ्राण), smell (गन्ध), the mass of solid forms (मूर्ति) beginning with "
             "hair, nails and bones, steadiness (धैर्य) and heaviness (गौरव)."),
    "limits": ("A prose list. धैर्य is taken as steadiness, firmness; fortitude is a possible alternative: no question rests "
               "on the choice. Hair, nails and bones are also called father-born in unit 19: another scheme."),
    "explain_hi": ("यह गद्य-पंक्ति पृथ्वी से सम्बन्धित भाव बताती है। "
                   "पहले घ्राण (नाक) और उसका विषय गन्ध। "
                   "फिर केश, नख, अस्थि आदि मूर्तियों, यानी ठोस रूपों, का समूह। "
                   "अन्त में धैर्य (स्थिरता) और गौरव (भारीपन)। "
                   "इस प्रकार इकाई १३ से १७ तक पाँचों भूतों के भाव पूरे होते हैं: आकाश, वायु, अग्नि, जल, पृथ्वी।"),
    "hook": "पृथ्वी: नाक, गन्ध, ठोस अंग, स्थिरता, भारीपन।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 17, which quality of the body belongs to earth?",
            ("Heaviness (gaurava)", "गौरवं च: heaviness closes the earth list."),
            [("Lightness (lāghava)", "Lightness belongs to wind (unit 14)."),
             ("Looseness (śaithilya)", "Looseness belongs to water (unit 16)."),
             ("Radiance (bhā)", "Radiance belongs to fire (unit 15).")],
            "Earth gives steadiness (धैर्य) and heaviness (गौरव).",
            "... धैर्य्यं गौरवं च."),
        order(1, "Put the items of unit 17 in the line's order.",
              ["पार्थिवानि", "घ्राणं", "गंधः", "केशनखास्थ्यादिमूर्त्तिसमूहो", "धैर्य्यं", "गौरवं च"],
              "Of earth: the nose, smell, the mass of solid forms, steadiness, heaviness.",
              "पार्थिवानि → घ्राणं → गंधः → ...मूर्त्तिसमूहो → धैर्य्यं → गौरवं च."),
        fill(2, "Unit 17: earth gives the nose (घ्राण) and its object, ____ (smell). Type it in Devanagari or in English letters (e.g. dharma).",
             accepts("गन्धः", None, "गन्ध"),
             "पार्थिवानि घ्राणं गंधः: the nose and smell (गन्धः, printed गंधः).",
             "गन्ध = smell, the object of the nose (घ्राण), as शब्द is of the ear and स्पर्श of the skin sense.",
             "घ्राणम् → गन्धः."),
        mcq("discriminate", 3, "Which split of अस्थ्यादि in unit 17 is right?",
            ("अस्थि + आदि", "इ + आ → या: अस्थि + आदि → अस्थ्यादि."),
            [("अस्थ्य + आदि", "अस्थ्य is not the word; the word is अस्थि, bone."),
             ("अस्थ + यादि", "अस्थ and यादि are not words; the य् comes from इ."),
             ("अस्थे + आदि", "अस्थे is not the word, and ए + आ would not give या.")],
            "अस्थि (bone) + आदि (and so on) = अस्थ्यादि.",
            "इ + आ → या."),
        mcq("apply", 4, "Which of these does unit 17 count in earth's mass of solid forms?",
            ("Nails (nakha)", "केशनखास्थ्यादि...: hair, nails, bones and so on."),
            [("Sweat (sveda)", "Sweat is a fluid of water (unit 16)."),
             ("Heat (ūṣman)", "Heat belongs to fire (unit 15)."),
             ("Breath (śvāsa)", "The breaths are movements of wind (unit 14).")],
            "Hair, nails and bones head earth's solid forms.",
            "केशनखास्थ्यादिमूर्त्तिसमूहः."),
        mcq("transfer", 5, "By the rule of अस्थि + आदि, how are इति + आदि (and so on) joined?",
            ("इत्यादि", "इ + आ → या, as अस्थि + आदि → अस्थ्यादि."),
            [("इत्यदि", "Short य comes from इ + short अ; here the vowel is long आ."),
             ("इतादि", "The इ is not dropped; it becomes य्."),
             ("इतेदि", "ए comes from अ + इ, not from इ + आ.")],
            "इति + आदि = इत्यादि, like अस्थि + आदि = अस्थ्यादि.",
            "इ + आ → या.",
            teaches="इ before a different vowel becomes य्: अस्थि + आदि → अस्थ्यादि."),
    ],
}

# ---------------------------------------------------------------- unit 18
AUTHORED["18"] = {
    "title": "तेषु मातृजानि मृदूनि",
    "question": "By unit 18, which parts of the body are born of the mother, and what quality do they share?",
    "rule": ("Among these, the mother-born (मातृज) parts are soft (मृदु): skin, blood, flesh, fat, marrow, navel, heart, "
             "stomach, uterus, liver, spleen, kloma (identity disputed), intestines, rectum and so on."),
    "limits": ("A prose list. Heart, stomach (āmāśaya), uterus, liver, spleen, intestines and rectum are standard "
               "identifications; kloma is disputed (pancreas, lungs or another structure proposed): no question on its identity. "
               "आदि (and so on) leaves the list open."),
    "explain_hi": ("यहाँ से भावों का दूसरा वर्गीकरण आरम्भ होता है: माता से उत्पन्न, पिता से उत्पन्न आदि। "
                   "माता से उत्पन्न भाव मृदु, यानी कोमल, हैं। "
                   "सूची: त्वचा, रक्त, मांस, मेद (चर्बी), मज्जा, नाभि, हृदय, आमाशय (पेट), गर्भाशय, यकृत् (जिगर), प्लीहा (तिल्ली), "
                   "क्लोम, आन्त्र (आँत) और गुद (मलद्वार) आदि। "
                   "हृदय, आमाशय, गर्भाशय, यकृत्, प्लीहा, आन्त्र और गुद की पहचान मानक है; क्लोम की पहचान विवादित है।"),
    "hook": "माता से कोमल: त्वचा, रक्त, मांस और भीतर के अंग।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 18, what quality do the mother-born parts share?",
            ("They are soft", "मृदूनि: they are soft."),
            [("They are firm", "Firm (स्थिर) is said of the father-born parts (unit 19)."),
             ("They are hot", "No heat is named; the word is मृदूनि, soft."),
             ("They are cold", "No cold is named; the word is मृदूनि, soft.")],
            "मातृजानि मृदूनि: the mother-born parts are soft.",
            "मातृज → मृदु."),
        order(1, "Put these organs of unit 18 in the line's order.",
              ["हृदय", "आमाशय", "गर्भाशय", "यकृत्", "प्लीहा", "आन्त्र"],
              "Heart, stomach, uterus, liver, spleen, (kloma,) intestines.",
              "...हृदयामाशयगर्भाशययकृत्प्लीहक्लोमांत्र..."),
        match(2, "Match each mother-born part of unit 18 to its modern name.",
              [["आमाशय", "stomach (standard)"], ["यकृत्", "liver (standard)"], ["प्लीहा", "spleen (standard)"],
               ["गर्भाशय", "uterus (standard)"], ["गुद", "rectum, anus (standard)"], ["मज्जा", "marrow"]],
              "These organs of the mother-born list have standard identifications.",
              "आमाशय, यकृत्, प्लीहा, गर्भाशय, गुद, मज्जा.", role="extend",
              teaches="आमाशय (stomach) and गर्भाशय (uterus) both end in आशय, a receptacle."),
        mcq("discriminate", 3, "Which split of मेदोमज्ज in unit 18 is right?",
            ("मेदस् + मज्जा", "A final अस् becomes ओ before a voiced sound: मेदस् + मज्जा → मेदोमज्ज."),
            [("मेद + ओमज्जा", "ओमज्जा is not a word; the word is मज्जा, marrow."),
             ("मेदा + उमज्जा", "मेदा and उमज्जा are not the words of the list."),
             ("मेदु + अमज्जा", "मेदु and अमज्जा are not words; the words are मेदस्, मज्जा.")],
            "मेदस् (fat) + मज्जा (marrow) = मेदोमज्ज...",
            "अस् + voiced sound → ओ."),
        mcq("apply", 4, "Which of these is not among the mother-born parts of unit 18?",
            ("Bones (asthi)", "Bones are father-born (unit 19), not mother-born."),
            [("Liver (yakṛt)", "Liver is in the mother-born list: यकृत्."),
             ("Spleen (plīhan)", "Spleen is in the mother-born list: प्लीह."),
             ("Navel (nābhi)", "Navel is in the mother-born list: नाभि.")],
            "Liver, spleen and navel are mother-born; bones are father-born.",
            "मातृजानि ... नाभि ... यकृत्प्लीह..."),
        mcq("transfer", 5, "By the rule of त्वच् + रक्त → त्वग्रक्त, how are वाच् + दानम् (giving of one's word) joined?",
            ("वाग्दानम्", "A final च् becomes ग् before a voiced sound, as त्वच् + रक्त → त्वग्रक्त."),
            [("वाक्दानम्", "Before the voiced द the unvoiced क् is not kept; it becomes ग्."),
             ("वाच्दानम्", "A final च् does not stay; it turns to the क्/ग् row."),
             ("वाज्दानम्", "A final च् goes to ग्, not to ज्.")],
            "वाच् + दानम् = वाग्दानम्, like त्वच् + रक्त = त्वग्रक्त.",
            "Final च् + voiced sound → ग्.",
            teaches="A final च् becomes ग् before a voiced sound: त्वच् + रक्त → त्वग्रक्त."),
    ],
}

# ---------------------------------------------------------------- unit 19
AUTHORED["19"] = {
    "title": "पितृजानि स्थिराणि",
    "question": "By unit 19, which parts of the body are born of the father, and what quality do they share?",
    "rule": ("The father-born (पितृज) parts are firm (स्थिर): hair, nails, bones, semen (शुक्र), sirā (probably veins), "
             "dhamanī (probably arteries) and so on."),
    "limits": ("A prose list. sirā = veins and dhamanī = arteries are probable only (the terms are not used alike in every "
               "text): no question on which vessel carries what. Hair, nails and bones are also earth's solid forms (unit 17): another scheme."),
    "explain_hi": ("यह गद्य-पंक्ति पिता से उत्पन्न भाव बताती है; वे स्थिर, यानी दृढ़, हैं। "
                   "सूची: केश, नख, अस्थि, शुक्र (वीर्य), सिरा और धमनी आदि। "
                   "सिरा और धमनी शरीर की नलिकाएँ हैं; इन्हें शिरा (वेन) और धमनी (आर्टरी) मानना केवल सम्भावित है। "
                   "इकाई १८ के कोमल, माता से उत्पन्न भावों के बाद यहाँ दृढ़ भाव आते हैं। "
                   "केश, नख और अस्थि इकाई १७ में पृथ्वी के ठोस रूपों में भी आए थे; वह दूसरा वर्गीकरण है।"),
    "hook": "पिता से स्थिर: केश, नख, हड्डी, शुक्र, नलिकाएँ।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 19, which of these is born of the father?",
            ("Bones (asthi)", "केशनखास्थि...: bones are in the father-born list."),
            [("Liver (yakṛt)", "The liver is mother-born (unit 18)."),
             ("Blood (rakta)", "Blood is mother-born (unit 18)."),
             ("Heart (hṛdaya)", "The heart is mother-born (unit 18).")],
            "Hair, nails, bones, semen and the vessels are father-born.",
            "पितृजानि स्थिराणि केशनखास्थि..."),
        order(1, "Put the father-born parts of unit 19 in the line's order.",
              ["केश", "नख", "अस्थि", "शुक्र", "सिरा", "धमनी"],
              "Hair, nails, bones, semen, sirā, dhamanī.",
              "केश → नख → अस्थि → शुक्र → सिरा → धमनी."),
        match(2, "Match each word of unit 19 to its meaning.",
              [["पितृज", "born of the father"], ["स्थिर", "firm, stable"], ["सिरा", "a vessel, probably a vein"],
               ["धमनी", "a vessel, probably an artery"], ["शुक्र", "semen"], ["केश", "hair"]],
              "The father-born parts are firm: hair, semen, the vessels and the rest.",
              "पितृज, स्थिर, सिरा, धमनी, शुक्र, केश.", role="extend",
              teaches="सिरा and धमनी are both tubular vessels; vein and artery are only probable equivalents."),
        mcq("discriminate", 3, "Which split of धमन्यादीनि in unit 19 is right?",
            ("धमनी + आदीनि", "ई + आ → या: धमनी + आदीनि → धमन्यादीनि."),
            [("धमन्य + आदीनि", "धमन्य is not the word; the word is धमनी."),
             ("धमनी + यादीनि", "यादीनि is not a word; the य् comes from the ई."),
             ("धम + न्यादीनि", "धम and न्यादीनि are not the words of the list.")],
            "धमनी (vessel) + आदीनि (and so on) = धमन्यादीनि.",
            "ई + आ → या."),
        mcq("apply", 4, "Which rendering of पितृजानि स्थिराणि is right?",
            ("The father-born are firm", "पितृजानि = born of the father; स्थिराणि = firm."),
            [("The father-born are soft", "Soft (मृदु) is said of the mother-born (unit 18)."),
             ("The mother-born are firm", "पितृ means father, not mother (मातृ)."),
             ("The firm are born of space", "पितृज is born of the father, not of space.")],
            "पितृजानि स्थिराणि = the father-born (parts) are firm.",
            "पितृ (father) + ज (born); स्थिर = firm."),
        mcq("transfer", 5, "By the pattern of पितृज (born of the father), what does जलज literally mean?",
            ("Born of water", "जल (water) + ज (born): born of water, as पितृ + ज = born of the father."),
            [("Water that is born", "The last member ज names what is born; the first says from where."),
             ("Giver of the water", "ज means born, not giving."),
             ("Born of the father", "The first member is जल, water, not पितृ.")],
            "जलज = born of water, like पितृज = born of the father.",
            "X + ज = born of X.",
            teaches="A compound ending in -ज means 'born of' its first member: पितृज = born of the father."),
    ],
}

# ---------------------------------------------------------------- unit 20
AUTHORED["20"] = {
    "title": "आत्मजानि तासु तासु योनिषूत्पत्तिः",
    "question": "By unit 20, what in a being is born of the self (ātman)?",
    "rule": ("Self-born (आत्मज): birth in this or that womb (yoni), mind, consciousness, the senses, prāṇa and apāna, "
             "sustaining, distinct form, voice and colour, desire, anger, greed, fear, joy, memory, intellect, wish, aversion, "
             "effort, ego, pleasure, pain, lifespan and more."),
    "limits": ("Prose, confidence medium. The last compound may end in आत्मज्ञान (self-knowledge) or in two items, ātman "
               "and knowledges: no question on it. A stray space may sit in कामक्रोधलोभभय हर्षाः (sense unchanged). "
               "धारण (sustaining) is left general; prāṇa and apāna stay Sanskrit terms."),
    "explain_hi": ("यह लम्बी गद्य-पंक्ति आत्मा से उत्पन्न भाव गिनाती है। "
                   "पहले उन-उन योनियों में जन्म, फिर मन, चेतना, इन्द्रियाँ, प्राण और अपान, और धारण। "
                   "फिर आकृति, स्वर और वर्ण की विशेषताएँ, और काम, क्रोध, लोभ, भय, हर्ष। "
                   "अन्त में धर्म और अधर्म में प्रवृत्ति का स्वभाव, स्मृति, बुद्धि, इच्छा, द्वेष, प्रयत्न, अहंकार, सुख, दुःख, "
                   "आयु और आत्मज्ञान। "
                   "अन्तिम समास को ‘आत्म’ और ‘ज्ञान’ दो अलग भाव भी पढ़ा जा सकता है।"),
    "hook": "आत्मा से: जन्म, मन, इन्द्रियाँ, भावनाएँ, स्मृति, बुद्धि, आयु।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 20, which of these is born of the self (ātman)?",
            ("The mind (manas)", "मनः is in the self-born list."),
            [("The liver (yakṛt)", "The liver is mother-born (unit 18)."),
             ("The bones (asthi)", "The bones are father-born (unit 19)."),
             ("Heaviness (gaurava)", "Heaviness belongs to earth (unit 17).")],
            "Mind, consciousness and the senses are self-born.",
            "आत्मजानि ... मनश्चेतनेंद्रियाणि."),
        order(1, "Put the first self-born items of unit 20 in the line's order.",
              ["योनिषूत्पत्तिः", "मनः", "चेतना", "इन्द्रियाणि", "प्राणापानौ", "धारणम्"],
              "Birth in the wombs, mind, consciousness, the senses, prāṇa and apāna, sustaining.",
              "योनिषूत्पत्तिः → मनः → चेतना → इन्द्रियाणि → प्राणापानौ → धारणम्."),
        match(2, "Match each self-born item of unit 20 to its meaning.",
              [["काम", "desire"], ["क्रोध", "anger"], ["लोभ", "greed"], ["भय", "fear"], ["द्वेष", "aversion"],
               ["प्रयत्न", "effort"]],
              "Desire, anger, greed, fear, aversion and effort are self-born.",
              "काम, क्रोध, लोभ, भय, द्वेष, प्रयत्न.", role="extend",
              teaches="इच्छा (wish) and द्वेष (aversion) stand side by side: liking and disliking."),
        mcq("discriminate", 3, "Which split of योनिषूत्पत्तिः in unit 20 is right?",
            ("योनिषु + उत्पत्तिः", "उ + उ → ऊ: योनिषु + उत्पत्तिः → योनिषूत्पत्तिः."),
            [("योनिषू + त्पत्तिः", "त्पत्तिः is not a word; the word is उत्पत्तिः, birth."),
             ("योनि + षूत्पत्तिः", "षूत्पत्तिः is not a word; षु is the locative ending."),
             ("योनिषु + ऊत्पत्तिः", "ऊत्पत्तिः is not a word; the word has short उ.")],
            "योनिषु (in the wombs) + उत्पत्तिः (birth) = योनिषूत्पत्तिः.",
            "उ + उ → ऊ."),
        multi("apply", 4, "Which of these does unit 20 count as born of the self?",
              [("Skin (tvac)", "Skin is mother-born (unit 18)."),
               ("Memory (smṛti)", "Right: स्मृति is in the self-born list."),
               ("Semen (śukra)", "Semen is father-born (unit 19)."),
               ("Effort (prayatna)", "Right: प्रयत्न is in the self-born list."),
               ("Spleen (plīhan)", "The spleen is mother-born (unit 18)."),
               ("Ego (ahaṅkāra)", "Right: अहंकार is in the self-born list.")],
              [1, 3, 5],
              "Memory, effort and ego are self-born; skin and spleen are mother-born, semen father-born.",
              "...स्मृतिबुद्धीच्छाद्वेषप्रयत्नाहंकार..."),
        mcq("transfer", 5, "By the rule of चेतना + इन्द्रियाणि → चेतनेन्द्रियाणि, how are महा + इन्द्रः (great Indra) joined?",
            ("महेन्द्रः", "आ + इ → ए, as चेतना + इन्द्रियाणि → चेतनेन्द्रियाणि."),
            [("महैन्द्रः", "ऐ comes from अ/आ + ए or ऐ, not from आ + इ."),
             ("महीन्द्रः", "ई comes from इ + इ, not from आ + इ."),
             ("महान्द्रः", "The इ is not lost; आ + इ join as ए.")],
            "महा + इन्द्रः = महेन्द्रः, like चेतना + इन्द्रियाणि = चेतनेन्द्रियाणि.",
            "आ + इ → ए.",
            teaches="आ followed by इ joins as ए: चेतना + इन्द्रियाणि → चेतनेन्द्रियाणि (the data's split)."),
    ],
}

# ---------------------------------------------------------------- unit 21
AUTHORED["21"] = {
    "title": "सात्म्यज भाव",
    "question": "By unit 21, what is born of sātmya, what is habitually suited to a person?",
    "rule": ("Born of sātmya (what is habitually suited): lifespan, health (on a near-certain correction), absence of "
             "laziness and of greed, clear senses, voice, colour, bīja (probably semen) and ojas, abundant joy, intelligence and strength."),
    "limits": ("Prose, confidence low. Printed आयोग्य is read आरोग्य (health) on a near-certain correction; "
               "संपद्यशस्तनताः is garbled and left untranslated; बीजौजः may be two items or 'ojas of the seed'. "
               "No question on these."),
    "explain_hi": ("यह गद्य-पंक्ति सात्म्य से उत्पन्न भाव बताती है; सात्म्य = जो व्यक्ति को अभ्यास से अनुकूल हो। "
                   "सूची: आयु, आरोग्य (सुधारे पाठ पर; छपा ‘आयोग्य’), आलस्य का अभाव, लोभ का अभाव, इन्द्रियों की स्वच्छता, "
                   "स्वर, वर्ण, बीज (सम्भवतः वीर्य) और ओज। "
                   "फिर एक अस्पष्ट शब्द ‘संपद्यशस्तनताः’, जिसका अर्थ नहीं लिया गया। "
                   "अन्त में हर्ष की अधिकता, मेधा और बल। "
                   "पंक्ति का पाठ बिगड़ा हुआ है, इसलिए विश्वास निम्न है।"),
    "hook": "जो अनुकूल हो, उससे: आयु, फुर्ती, साफ इन्द्रियाँ, बल।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 21, what does sātmya, the source named here, mean?",
            ("What is habitually suited", "The data: sātmya = what is habitually suited or compatible."),
            [("What is born of the mother", "That is मातृज (unit 18), not sātmya."),
             ("What is pure sattva", "Pure sattva is the source of unit 23."),
             ("What is born of the father", "That is पितृज (unit 19), not sātmya.")],
            "सात्म्य = what suits a person by habit; unit 21 lists what is born of it.",
            "सात्म्यजानि = born of sātmya."),
        order(1, "Put these sure items of unit 21 in the line's order.",
              ["अनालस्यम्", "अलोलुपत्वम्", "इन्द्रियप्रसाद", "प्रहर्षभूयस्त्वम्", "मेधा", "बलम्"],
              "Absence of laziness, absence of greed, clear senses, abundant joy, intelligence, strength.",
              "अनालस्यम् → अलोलुपत्वम् → इन्द्रियप्रसाद... → प्रहर्षभूयस्त्वम् → मेधा → बलम्."),
        match(2, "Match each word of unit 21 to its meaning.",
              [["अनालस्य", "absence of laziness"], ["अलोलुपत्व", "absence of greed"],
               ["इन्द्रियप्रसाद", "clarity of the senses"], ["प्रहर्षभूयस्त्व", "abundance of joy"], ["बल", "strength"]],
              "Sātmya brings freedom from laziness and greed, clear senses, much joy and strength.",
              "अनालस्य, अलोलुपत्व, इन्द्रियप्रसाद, प्रहर्षभूयस्त्व, बल.", role="extend",
              teaches="अन्- (before a vowel) and अ- (before a consonant) negate: अनालस्य, अलोलुपत्व."),
        mcq("discriminate", 3, "Which split of अनालस्य in unit 21 is right?",
            ("अन् + आलस्य", "अन्- is the negative before a vowel: absence of laziness (आलस्य)."),
            [("अना + लस्य", "अना and लस्य are not the parts; आलस्य is laziness."),
             ("अनल + अस्य", "अनल + अस्य would join as अनलास्य, a different word."),
             ("अ + नालस्य", "नालस्य is not a word; before a vowel the negative is अन्-.")],
            "अन् (not) + आलस्य (laziness) = अनालस्य, absence of laziness.",
            "Negative अ- before a consonant, अन्- before a vowel."),
        mcq("apply", 4, "By unit 21, which of these is born of sātmya?",
            ("Strength (bala)", "बलं च closes the sātmya list."),
            [("Grief (śoka)", "Grief belongs to tamas (unit 25)."),
             ("Hypocrisy (dambha)", "Hypocrisy belongs to rajas (unit 24)."),
             ("Dejection (viṣāda)", "Dejection belongs to tamas (unit 25).")],
            "What suits a person by habit brings strength, intelligence and clear senses.",
            "सात्म्यजानि ... मेधा बलं च."),
        mcq("transfer", 5, "By the rule of बीज + ओजः → बीजौजः, how are जल + ओघः (flood of water) joined?",
            ("जलौघः", "अ + ओ → औ, as बीज + ओजः → बीजौजः."),
            [("जलोघः", "ओ comes from अ + उ, not from अ + ओ."),
             ("जलैघः", "ऐ comes from अ + ए, not from अ + ओ."),
             ("जलाघः", "आ comes from अ + अ, not from अ + ओ.")],
            "जल + ओघः = जलौघः, like बीज + ओजः = बीजौजः.",
            "अ + ओ → औ.",
            teaches="A short अ followed by ओ joins as औ: बीज + ओजः → बीजौजः."),
    ],
}

# ---------------------------------------------------------------- unit 22
AUTHORED["22"] = {
    "title": "रसजानि ... संभवो वृत्तिर्वृद्धिः",
    "question": "By unit 22, what does rasa, the nutritive fluid, give the whole body?",
    "rule": ("Born of rasa (the nutritive fluid), of the whole body: its coming into being (संभव), maintenance (वृत्ति), "
             "growth (वृद्धि), satisfaction (तृप्ति), nourishment (पुष्टि) and vigour (उत्साह)."),
    "limits": ("Prose, confidence low. Printed कृत्स्त्रस्य is read कृत्स्नस्य (whole) on a near-certain correction; "
               "औल्यं is unknown and left untranslated: no question on either. The genitive is taken with every item."),
    "explain_hi": ("यह गद्य-पंक्ति रस, यानी पहली धातु पोषक द्रव, से उत्पन्न भाव बताती है। "
                   "ये सम्पूर्ण शरीर के हैं: उत्पत्ति (संभव), वृत्ति (चलते रहना), वृद्धि, तृप्ति, पुष्टि और उत्साह। "
                   "बीच में एक अज्ञात शब्द ‘औल्यं’ है, जिसका अर्थ नहीं लिया गया। "
                   "छपा ‘कृत्स्त्रस्य’ लगभग निश्चित रूप से ‘कृत्स्नस्य’ (सम्पूर्ण) है। "
                   "इसके बाद इकाई २३ से सत्त्व, रजस् और तमस् के भाव आते हैं।"),
    "hook": "रस से पूरे शरीर का बनना, चलना, बढ़ना, पुष्ट होना।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 22, what does rasa give the body?",
            ("Growth and nourishment", "वृद्धिः and पुष्टिः are in the rasa list."),
            [("Hair, nails and the bones", "Hair, nails and bones are father-born (unit 19)."),
             ("The mind and the senses", "The mind and the senses are self-born (unit 20)."),
             ("Envy, pride and greed", "These are rajas traits (unit 24).")],
            "Rasa gives the whole body its origin, maintenance, growth, satisfaction, nourishment and vigour.",
            "रसजानि ... वृद्धिः ... पुष्टिः."),
        order(1, "Put the sure items of unit 22 in the line's order (the unclear औल्यं is left out).",
              ["संभवः", "वृत्तिः", "वृद्धिः", "तृप्तिः", "पुष्टिः", "उत्साहः"],
              "Coming into being, maintenance, growth, satisfaction, nourishment, vigour.",
              "संभवो → वृत्तिर् → वृद्धिस् → तृप्तिर् → (औल्यं) → पुष्टिर् → उत्साहश्च."),
        match(2, "Match each word of unit 22 to its meaning.",
              [["संभव", "coming into being"], ["वृत्ति", "maintenance"], ["वृद्धि", "growth"], ["तृप्ति", "satisfaction"],
               ["पुष्टि", "nourishment"], ["उत्साह", "vigour"]],
              "What rasa gives the whole body.",
              "संभव, वृत्ति, वृद्धि, तृप्ति, पुष्टि, उत्साह.", role="extend",
              teaches="रसज = born of rasa, here the nutritive fluid (the first dhātu), not taste."),
        mcq("discriminate", 3, "Which split of वृद्धिस्तृप्तिः in unit 22 is right?",
            ("वृद्धिः + तृप्तिः", "A visarga before त becomes स्: वृद्धिः + तृप्तिः → वृद्धिस्तृप्तिः."),
            [("वृद्धि + स्तृप्तिः", "स्तृप्तिः is not a word; the स् comes from the visarga."),
             ("वृद्धिः + स्तृप्तिः", "स्तृप्तिः is not a word; the word is तृप्तिः."),
             ("वृद्धिस्तृ + प्तिः", "वृद्धिस्तृ and प्तिः are not words.")],
            "वृद्धिः (growth) + तृप्तिः (satisfaction) = वृद्धिस्तृप्तिः.",
            "Visarga + त → स्त."),
        mcq("apply", 4, "A child grows and keeps nourished. Which source does unit 22 credit with this?",
            ("Rasa, the nutrient fluid", "रसजानि ... वृद्धिः ... पुष्टिः."),
            [("Space, the element ākāśa", "Space gives the ear, sound, the channels and separateness (unit 13)."),
             ("The self, ātman, alone", "The self-born list (unit 20) has no growth or nourishment."),
             ("The guṇa named tamas", "Tamas gives ignorance, sleep and the like (unit 25).")],
            "Growth (वृद्धि) and nourishment (पुष्टि) are born of rasa.",
            "रसजानि ... वृद्धिः ... पुष्टिः."),
        mcq("transfer", 5, "By the rule of पुष्टिः + उत्साहः → पुष्टिरुत्साहः, how are हरिः + अस्ति (Hari is) joined?",
            ("हरिरस्ति", "After इ, a visarga before a vowel becomes र्."),
            [("हरियस्ति", "य् comes from a vowel इ, not from इः."),
             ("हरोऽस्ति", "The इ of हरि does not change to ओ."),
             ("हरि अस्ति", "After इ the visarga becomes र्; it is not dropped.")],
            "हरिः + अस्ति = हरिरस्ति, like पुष्टिः + उत्साहः = पुष्टिरुत्साहः.",
            "इः + vowel → इर्.",
            teaches="A visarga after इ becomes र् before a vowel: पुष्टिः + उत्साहः → पुष्टिरुत्साहः."),
    ],
}

# ---------------------------------------------------------------- unit 23
AUTHORED["23"] = {
    "title": "शुद्धसत्वजानि शौचमास्तिकत्वं",
    "question": "By unit 23, which traits are born of pure sattva?",
    "rule": ("Born of pure sattva: purity (शौच), belief (आस्तिकत्व), gratitude, courtesy, resolve, valour, depth, intellect, "
             "intelligence, memory, liking for bright dharma, devotion, non-attachment and the contrary of the guṇa tamas."),
    "limits": ("Prose, confidence medium. Printed शुक्लधर्म्हरूचिः is read शुक्लधर्मरुचिः (liking for bright dharma) on a "
               "near-certain correction: no question on that word. आस्तिकत्व is kept as plain belief. Printed सत्व = सत्त्व."),
    "explain_hi": ("यहाँ से सत्त्व, रजस् और तमस् से उत्पन्न भावों का विभाग आरम्भ होता है। "
                   "शुद्ध सत्त्व से उत्पन्न भाव: शौच, आस्तिकता, कृतज्ञता, दाक्षिण्य (शिष्टता), व्यवसाय (निश्चय), शौर्य, गाम्भीर्य, "
                   "बुद्धि, मेधा और स्मृति। "
                   "फिर शुक्ल धर्म में रुचि (सुधारे पाठ पर), भक्ति, अनभिष्वङ्ग (अनासक्ति) और तमोगुण का विपर्यय, यानी उलटा भाव। "
                   "छपा ‘सत्व’ = सत्त्व, और ‘शौर्य्यं’ = शौर्यम् (छपाई की आदत)।"),
    "hook": "शुद्ध सत्त्व: शुचिता, कृतज्ञता, बुद्धि, स्मृति, अनासक्ति।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 23, which of these is born of pure sattva?",
            ("Courtesy (dākṣiṇya)", "दाक्षिण्यं is in the sattva list."),
            [("Envy (mātsarya)", "Envy belongs to rajas and tamas (units 24, 25)."),
             ("Hypocrisy (dambha)", "Hypocrisy belongs to rajas (unit 24)."),
             ("Heedlessness (pramāda)", "Heedlessness belongs to tamas (unit 25).")],
            "Pure sattva gives purity, belief, gratitude, courtesy and the like.",
            "शुद्धसत्वजानि ... दाक्षिण्यं ..."),
        order(1, "Put the first sattva items of unit 23 in the line's order.",
              ["शौचम्", "आस्तिकत्वम्", "कृतज्ञता", "दाक्षिण्यम्", "व्यवसायः", "शौर्यम्"],
              "Purity, belief, gratitude, courtesy, resolve, valour.",
              "शौचम् → आस्तिकत्वम् → कृतज्ञता → दाक्षिण्यम् → व्यवसायः → शौर्यम्."),
        match(2, "Match each sattva trait of unit 23 to its meaning.",
              [["शौच", "purity"], ["कृतज्ञता", "gratitude"], ["दाक्षिण्य", "courtesy, kindliness"],
               ["व्यवसाय", "resolve, determination"], ["गाम्भीर्य", "depth, gravity"], ["अनभिष्वङ्ग", "non-attachment"]],
              "Traits born of pure sattva.",
              "शौच, कृतज्ञता, दाक्षिण्य, व्यवसाय, गाम्भीर्य, अनभिष्वङ्ग.", role="extend",
              teaches="कृतज्ञ = one who knows (ज्ञ) what was done (कृत) for him: grateful; -ता makes the abstract noun."),
        mcq("discriminate", 3, "Which split of तमोगुण in unit 23 is right?",
            ("तमस् + गुण", "A final अस् becomes ओ before a voiced sound: तमस् + गुण → तमोगुण."),
            [("तम + ओगुण", "ओगुण is not a word; the word is गुण."),
             ("तमः + उगुण", "उगुण is not a word, and the ओ is not अ + उ here."),
             ("तमा + उगुण", "तमा and उगुण are not the words; they are तमस्, गुण.")],
            "तमस् (tamas) + गुण = तमोगुण; विपर्यय = its contrary.",
            "अस् + voiced sound → ओ."),
        multi("apply", 4, "Which of these does unit 23 count as born of pure sattva?",
              [("Memory (smṛti)", "Right: स्मृतिः is in the sattva list."),
               ("Grief (śoka)", "Grief belongs to tamas (unit 25)."),
               ("Greed (lolupatva)", "Greed belongs to rajas (unit 24)."),
               ("Devotion (bhakti)", "Right: भक्ति is in the sattva list.")],
              [0, 3],
              "Memory and devotion are sattva's; grief is tamas's, greed rajas's.",
              "...बुद्धिर्मेधा स्मृतिः ... भक्ति..."),
        mcq("transfer", 5, "By the rule of तमस् + गुण → तमोगुण, how are मनस् + बलम् (strength of mind) joined?",
            ("मनोबलम्", "A final अस् becomes ओ before the voiced ब, as तमस् + गुण → तमोगुण."),
            [("मनःबलम्", "Before a voiced sound the अस् does not stay as visarga; it becomes ओ."),
             ("मनर्बलम्", "र् comes after vowels other than अ/आ."),
             ("मनाबलम्", "आ does not come from अस्; before a voiced sound it is ओ.")],
            "मनस् + बलम् = मनोबलम्, like तमस् + गुण = तमोगुण.",
            "अस् + voiced sound → ओ.",
            teaches="A final अस् becomes ओ before a voiced sound: तमस् + गुण → तमोगुण."),
    ],
}

# ---------------------------------------------------------------- unit 24
AUTHORED["24"] = {
    "title": "राजस भाव",
    "question": "By unit 24, which traits belong to rajas?",
    "rule": ("Those of rajas (राजसानि): envy (मात्सर्य), unmeasured talk (अमितभाषित्व), egoism (अहंकार), greed (लोलुपत्व), "
             "hypocrisy (दम्भ), pride (मान), anger (क्रोध) and desire (काम); the opening word is garbled."),
    "limits": ("Prose, confidence low. दुरुपघारताशौर्य्यं is garbled and left untranslated. क्रोधाहर्षः is parsed as printed, "
               "anger + joylessness, but may stand for क्रोधो हर्षः, anger and joy: no question on that word or on अहर्ष/हर्ष. "
               "Envy recurs in unit 25 (tamas)."),
    "explain_hi": ("यह गद्य-पंक्ति रजस् से सम्बन्धित भाव बताती है। "
                   "पहला शब्द ‘दुरुपघारताशौर्य्यं’ बिगड़ा हुआ है और उसका अर्थ नहीं लिया गया। "
                   "फिर मात्सर्य (ईर्ष्या), अमितभाषित्व (बहुत बोलना), अहंकार, लोलुपत्व (लोभ), दम्भ, मान और क्रोध। "
                   "छपा ‘क्रोधाहर्षः’ = क्रोध + अहर्ष (हर्ष का अभाव) पढ़ा गया है, पर यह ‘क्रोधो हर्षः’ की छपाई-भूल भी हो सकता है। "
                   "अन्त में काम।"),
    "hook": "रजस्: ईर्ष्या, बकबक, अहंकार, लोभ, दम्भ, मान।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 24, which of these belongs to rajas?",
            ("Hypocrisy (dambha)", "दंभो is in the rajas list."),
            [("Gratitude (kṛtajñatā)", "Gratitude is born of pure sattva (unit 23)."),
             ("Courtesy (dākṣiṇya)", "Courtesy is born of pure sattva (unit 23)."),
             ("Purity (śauca)", "Purity is born of pure sattva (unit 23).")],
            "Rajas gives envy, egoism, greed, hypocrisy, pride and desire.",
            "राजसानि ... दंभो मानः ..."),
        order(1, "Put these rajas items of unit 24 in the line's order.",
              ["मात्सर्यम्", "अमितभाषित्वम्", "अहंकारः", "लोलुपत्वम्", "दम्भः", "मानः"],
              "Envy, unmeasured talk, egoism, greed, hypocrisy, pride.",
              "मात्सर्यम् → अमितभाषित्वम् → अहंकारः → लोलुपत्वम् → दम्भः → मानः."),
        match(2, "Match each rajas word of unit 24 to its meaning.",
              [["मात्सर्य", "envy"], ["अमितभाषित्व", "unmeasured talkativeness"], ["दम्भ", "hypocrisy, pretension"],
               ["मान", "pride"], ["लोलुपत्व", "greed"], ["काम", "desire"]],
              "Rajas traits: envy, much talk, hypocrisy, pride, greed, desire.",
              "मात्सर्य, अमितभाषित्व, दम्भ, मान, लोलुपत्व, काम.", role="extend",
              teaches="अमितभाषित्व: अमित (unmeasured) + भाषिन् (one who speaks) + -त्व (-ness)."),
        mcq("discriminate", 3, "Why is अहंकारः printed अहंकारो before लोलुपत्वं in unit 24?",
            ("अः becomes ओ before the voiced ल", "ल is voiced; अः before a voiced consonant gives ओ."),
            [("अः becomes ओ before any consonant", "Before unvoiced sounds the visarga stays or changes otherwise."),
             ("ओ marks a vocative form here", "The data reads अहंकारः, nominative: egoism."),
             ("The stem itself ends in ओ", "The stem is अहंकार; the ओ comes from sandhi.")],
            "अहंकारः + लोलुपत्वम् = अहंकारो लोलुपत्वं.",
            "अः + voiced consonant → ओ."),
        mcq("apply", 4, "A person talks without measure and is full of pride. By unit 24, these are products of what?",
            ("Rajas", "अमितभाषित्व and मान are in the rajas list."),
            [("Pure sattva", "Sattva gives purity, gratitude, depth and the like (unit 23)."),
             ("Sātmya, what suits", "Sātmya gives lifespan, strength and the like (unit 21)."),
             ("Rasa, the nutrient fluid", "Rasa gives growth, nourishment and the like (unit 22).")],
            "Unmeasured talk and pride are rājasa.",
            "राजसानि ... अमितभाषित्वम् ... मानः."),
        mcq("transfer", 5, "By the rule of दम्भः + मानः → दम्भो मानः, how are शिष्यः + वदति (the pupil speaks) joined?",
            ("शिष्यो वदति", "अः becomes ओ before the voiced व, as दम्भः + मानः → दम्भो मानः."),
            [("शिष्य वदति", "Before a voiced consonant अः gives ओ; it is not simply dropped."),
             ("शिष्यर्वदति", "र् comes after vowels other than अ/आ."),
             ("शिष्यश्वदति", "श् comes before च, छ or श, not before व.")],
            "शिष्यः + वदति = शिष्यो वदति, like दम्भः + मानः = दम्भो मानः.",
            "अः + voiced consonant → ओ.",
            teaches="अः before a voiced consonant becomes ओ: दम्भः + मानः → दम्भो मानः."),
    ],
}

# ---------------------------------------------------------------- unit 25
AUTHORED["25"] = {
    "title": "तामसान्यज्ञानं विषादः प्रमादो",
    "question": "By unit 25, which traits belong to tamas?",
    "rule": ("Those of tamas (तामसानि): ignorance, dejection (विषाद), heedlessness (प्रमाद), sleep, laziness, hunger and "
             "thirst, grief, envy, a wrong notion (विप्रतिपत्ति), scheming against others and the contrary of the guṇa sattva."),
    "limits": ("A prose list. विप्रतिपत्ति may also mean perplexity or contrary conduct; अभिसंधान may also mean deceiving: "
               "no question rests on the choice. The double avagraha of निद्राऽऽलस्यं is a print habit. Envy is also in the rajas list (unit 24)."),
    "explain_hi": ("यह गद्य-पंक्ति तमस् से सम्बन्धित भाव बताती है। "
                   "सूची: अज्ञान, विषाद (उदासी), प्रमाद (असावधानी), निद्रा, आलस्य, भूख-प्यास, शोक, मात्सर्य (ईर्ष्या)। "
                   "फिर विप्रतिपत्ति (विपरीत धारणा), पराभिसंधान (दूसरों के विरुद्ध षड्यन्त्र) और सत्त्व गुण का विपरीत भाव। "
                   "विप्रतिपत्ति के ‘भ्रम’ या ‘उलटा आचरण’ अर्थ भी सम्भव हैं। "
                   "‘निद्राऽऽलस्यं’ का दोहरा अवग्रह केवल छपाई की आदत है: निद्रा + आलस्यम्।"),
    "hook": "तमस्: अज्ञान, उदासी, नींद, आलस्य, शोक, छल।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 25, which of these belongs to tamas?",
            ("Grief (śoka)", "शोको is in the tamas list."),
            [("Gratitude (kṛtajñatā)", "Gratitude is born of pure sattva (unit 23)."),
             ("Devotion (bhakti)", "Devotion is born of pure sattva (unit 23)."),
             ("Pride (māna)", "Pride belongs to rajas (unit 24).")],
            "Tamas gives ignorance, dejection, sleep, laziness, grief and the like.",
            "तामसानि ... शोको ..."),
        order(1, "Put the first tamas items of unit 25 in the line's order.",
              ["अज्ञानम्", "विषादः", "प्रमादः", "निद्रा", "आलस्यम्", "क्षुत्तृष्णा"],
              "Ignorance, dejection, heedlessness, sleep, laziness, hunger and thirst.",
              "अज्ञानम् → विषादः → प्रमादः → निद्रा → आलस्यम् → क्षुत्तृष्णा."),
        match(2, "Match each tamas word of unit 25 to its meaning.",
              [["अज्ञान", "ignorance"], ["विषाद", "dejection"], ["प्रमाद", "heedlessness"], ["शोक", "grief"],
               ["क्षुत्तृष्णा", "hunger and thirst"], ["पराभिसंधान", "scheming against others"]],
              "Tamas traits: ignorance, dejection, heedlessness, grief, hunger and thirst, scheming.",
              "अज्ञान, विषाद, प्रमाद, शोक, क्षुत्तृष्णा, पराभिसंधान.", role="extend",
              teaches="पराभिसंधान: पर (others) + अभिसंधान (scheming), scheming against others."),
        mcq("discriminate", 3, "Which split of क्षुत्तृष्णा in unit 25 is right?",
            ("क्षुध् + तृष्णा", "A final ध् becomes त् before the unvoiced त: क्षुध् + तृष्णा → क्षुत्तृष्णा."),
            [("क्षु + त्तृष्णा", "त्तृष्णा is not a word; the word is तृष्णा, thirst."),
             ("क्षुत्त + ऋष्णा", "क्षुत्त and ऋष्णा are not the words of the pair."),
             ("क्षुता + तृष्णा", "क्षुता is not the word; hunger is क्षुध्.")],
            "क्षुध् (hunger) + तृष्णा (thirst) = क्षुत्तृष्णा.",
            "Final ध् + unvoiced sound → त्."),
        multi("apply", 4, "Which of these does unit 25 assign to tamas?",
              [("Sleep (nidrā)", "Right: निद्रा is in the tamas list."),
               ("Purity (śauca)", "Purity is born of pure sattva (unit 23)."),
               ("Envy (mātsarya)", "Right: मात्सर्य्यं is in the tamas list (it is in unit 24 too)."),
               ("Courtesy (dākṣiṇya)", "Courtesy is born of pure sattva (unit 23)."),
               ("Laziness (ālasya)", "Right: आलस्यं is in the tamas list.")],
              [0, 2, 4],
              "Sleep, envy and laziness are tāmasa; purity and courtesy are sattva's.",
              "तामसानि ... निद्राऽऽलस्यं ... मात्सर्य्यं ..."),
        mcq("transfer", 5, "By the rule of तामसानि + अज्ञानम् → तामसान्यज्ञानम्, how are यदि + अपि (even if) joined?",
            ("यद्यपि", "इ before अ becomes य्, as तामसानि + अज्ञानम् → तामसान्यज्ञानम्."),
            [("यदीपि", "ई comes from इ + इ, not from इ + अ."),
             ("यदेपि", "ए comes from अ + इ, not from इ + अ."),
             ("यदापि", "The इ is not dropped; it becomes य्.")],
            "यदि + अपि = यद्यपि, like तामसानि + अज्ञानम् = तामसान्यज्ञानम्.",
            "इ + अ → य.",
            teaches="इ before a different vowel becomes य्: तामसानि + अज्ञानम् → तामसान्यज्ञानम्."),
    ],
}


# ===================================================================== NOTES_HI
NOTES_HI = {
    "14": ("गद्य-पंक्ति; विश्वास उच्च; पाठ-चिह्न नहीं। प्रश्वास और उच्छ्वास में कौन बाहर की और कौन भीतर की साँस है, डेटा तय नहीं "
           "करता; इस पर प्रश्न नहीं। स्पर्शन इकाई १३ के श्रोत्र के समान इन्द्रिय (त्वचा) है। छपा ‘परिस्पंदनानि’ = परिस्पन्दनानि "
           "(अनुस्वार-वर्तनी)। सन्धि जाँची: स्पर्शनम् + स्पर्शः → स्पर्शनं स्पर्शः (व्यंजन से पहले म् → ं); प्रश्वास + उच्छ्वास → "
           "प्रश्वासोच्छ्वास (अ + उ → ओ); उत् + श्वास → उच्छ्वास (त् + श → च्छ); उच्छ्वास + आदि → उच्छ्वासादि (अ + आ → आ); "
           "लाघवम् + च → लाघवं च।"),
    "15": ("गद्य-पंक्ति; विश्वास उच्च; पाठ-चिह्न नहीं। छपा ‘शौर्य्यं’ = शौर्यम् (य्य दुहराना छपाई की आदत)। डेटा: "
           "‘पित्तमूष्मापक्तिः’ = पित्तम् + ऊष्मा + पक्तिः, ‘अपक्ति’ नहीं; ऊष्मा और पक्तिः बिना जगह के छपे हैं, सन्धि नहीं। पित्त "
           "नपुंसक है और दोष के रूप में रखा गया। वर्ण = रंग (त्वचा का रंग भी हो सकता है)। सन्धि जाँची: पित्तम् + ऊष्मा → "
           "पित्तमूष्मा; संतापः + मेधा → संतापो मेधा (अः + घोष → ओ); वर्णः + भाः → वर्णो भाः; भाः + तेजः → भास्तेजः (विसर्ग + त → "
           "स्); शौर्यम् + च → शौर्यं च।"),
    "16": ("गद्य-पंक्ति; विश्वास उच्च; पाठ-चिह्न नहीं। ‘रसः’ के बाद जगह न होना केवल छपाई की चूक है। पहला रस = स्वाद; समास के "
           "भीतर का रस = पोषक द्रव (पहली धातु; प्लाज़्मा या काइल मानना सम्भावित)। वसा = मांसगत चर्बी (सम्भावित); असृक् = रक्त, "
           "शुक्र = वीर्य (मानक)। छपा ‘आंभसानि’ = आम्भसानि। सन्धि जाँची: रस + असृज् → रसासृज् (अ + अ → आ); असृज् + शुक्र → "
           "असृक्शुक्र (अघोष श से पहले ज् → क्); मूत्र + आदि → मूत्रादि; शैथिल्यम् + स्नेहः → शैथिल्यं स्नेहः; स्नेहः + च → स्नेहश्च "
           "(विसर्ग + च → श्)।"),
    "17": ("गद्य-पंक्ति; विश्वास उच्च; पाठ-चिह्न नहीं। धैर्य = स्थिरता, दृढ़ता (सूची पार्थिव गुणों की है); ‘धीरज’ भी सम्भव; "
           "इस चुनाव पर प्रश्न नहीं। छपा ‘गंधः’ = गन्धः, ‘मूर्त्ति’ = मूर्ति, ‘धैर्य्यं’ = धैर्यम् (छपाई की आदत)। सन्धि जाँची: "
           "घ्राणम् + गन्धः → घ्राणं गंधः; नख + अस्थि → नखास्थि (अ + अ → आ); अस्थि + आदि → अस्थ्यादि (इ + आ → या); समूहः + "
           "धैर्यम् → समूहो धैर्यम् (अः + घोष → ओ); गौरवम् + च → गौरवं च।"),
    "18": ("गद्य-पंक्ति; विश्वास उच्च; पाठ-चिह्न नहीं। पहचान: हृदय, आमाशय (पेट), गर्भाशय, यकृत्, प्लीहा, आन्त्र, गुद मानक; "
           "क्लोम विवादित (अग्न्याशय, फेफड़े या फुफ्फुसावरण जैसी रचना: अलग-अलग मत), इसलिए ‘क्लोम’ ही रखा; इस पर प्रश्न नहीं। "
           "छपा ‘क्लोमांत्र’ = क्लोमान्त्र (अनुस्वार-वर्तनी)। सन्धि जाँची: त्वच् + रक्त → त्वग्रक्त (घोष से पहले च् → ग्); मेदस् + "
           "मज्जा → मेदोमज्ज (घोष से पहले अस् → ओ); हृदय + आमाशय → हृदयामाशय (अ + आ → आ); क्लोम + आन्त्र → क्लोमान्त्र; गुद "
           "+ आदीनि → गुदादीनि।"),
    "19": ("गद्य-पंक्ति; विश्वास उच्च; पाठ-चिह्न नहीं। सिरा = सम्भवतः शिरा (वेन), धमनी = सम्भवतः धमनी (आर्टरी); दोनों शब्द हर "
           "ग्रन्थ में एक जैसे प्रयुक्त नहीं, इसलिए केवल सम्भावित। कौन-सी नली क्या ले जाती है, इस पर प्रश्न नहीं। सन्धि जाँची: "
           "नख + अस्थि → नखास्थि (अ + अ → आ); धमनी + आदीनि → धमन्यादीनि (ई + आ → या)।"),
    "20": ("गद्य-पंक्ति; विश्वास मध्यम। पाठ-चिह्न: ‘कामक्रोधलोभभय हर्षाः’ में जगह सम्भवतः छपाई की भूल (कामक्रोधलोभभयहर्षाः); "
           "अर्थ नहीं बदलता। अन्तिम समास ‘...आयुरात्मज्ञानानि’ एक द्वन्द्व माना गया जिसका अन्तिम भाव आत्मज्ञान है; ‘आत्मा’ और "
           "‘ज्ञान’ दो भाव भी पढ़े जा सकते हैं। इस पर प्रश्न नहीं। छपा ‘धर्म्म’ = धर्म। सन्धि जाँची: योनिषु + उत्पत्तिः → "
           "योनिषूत्पत्तिः (उ + उ → ऊ); उत्पत्तिः + मनः → उत्पत्तिर्मनः (इः + घोष → इर्); मनः + चेतना → मनश्चेतना (विसर्ग + च → "
           "श्); चेतना + इन्द्रियाणि → चेतनेन्द्रियाणि (आ + इ → ए); प्राण + अपानौ → प्राणापानौ; धारणम् + आकृति → धारणमाकृति; "
           "बुद्धि + इच्छा → बुद्धीच्छा (इ + इ → ई); प्रयत्न + अहंकार → प्रयत्नाहंकार; आयुस् + आत्म → आयुरात्म (स्वर से पहले स् → र्)।"),
    "21": ("गद्य-पंक्ति; विश्वास निम्न। पाठ-चिह्न: (१) छपा ‘आयुरायोग्यम्’ → ‘आयुरारोग्यम्’ (लगभग निश्चित: ‘आयोग्य’ = अयोग्यता "
           "अच्छे फलों की सूची से मेल नहीं खाता; रो → यो छपाई-भूल); (२) ‘संपद्यशस्तनताः’ बिगड़ा शब्द, न विभाजित, न अनुवादित "
           "(‘संपत् प्रशस्ततनुताः’ केवल सम्भव, अपनाया नहीं)। ‘बीजौजः’ = बीज + ओजः दो भाव माने गए; ‘बीज का ओज’ भी सम्भव। इन "
           "पर प्रश्न नहीं। सन्धि जाँची: सात्म्यजानि + आयुः → सात्म्यजान्यायुः (इ + आ → या); अनालस्यम् + अलोलुपत्वम् → "
           "अनालस्यमलोलुपत्वम्; अलोलुपत्वम् + इन्द्रिय → अलोलुपत्वमिंद्रिय; बीज + ओजः → बीजौजः (अ + ओ → औ); छपा "
           "‘प्रहर्षभूयस्त्वंमेधा’ में जगह नहीं (प्रहर्षभूयस्त्वं मेधा); बलम् + च → बलं च।"),
    "22": ("गद्य-पंक्ति; विश्वास निम्न। पाठ-चिह्न: (१) छपा ‘कृत्स्त्रस्य’ → ‘कृत्स्नस्य’ (लगभग निश्चित; ‘त्स्त्र’ = ‘त्स्न’ की "
           "छपाई-भूल); (२) ‘औल्यं’ अज्ञात शब्द, अनुवाद नहीं (‘औज्ज्वल्यं’ केवल अनुमान, अपनाया नहीं)। इन पर प्रश्न नहीं। षष्ठी "
           "‘सम्पूर्ण शरीर का’ सूची के सब भावों से जोड़ी गई। रस = पोषक द्रव (पहली धातु)। सन्धि जाँची: संभवः + वृत्तिः → संभवो "
           "वृत्तिः (अः + घोष → ओ); वृत्तिः + वृद्धिः → वृत्तिर्वृद्धिः (इः + घोष → इर्); वृद्धिः + तृप्तिः → वृद्धिस्तृप्तिः (विसर्ग + त "
           "→ स्); तृप्तिः + औल्यम् → तृप्तिरौल्यम्; पुष्टिः + उत्साहः → पुष्टिरुत्साहः; उत्साहः + च → उत्साहश्च।"),
    "23": ("गद्य-पंक्ति; विश्वास मध्यम। पाठ-चिह्न: छपा ‘शुक्लधर्म्हरूचिः’ → ‘शुक्लधर्मरुचिः’ (लगभग निश्चित; फालतू ‘ह’ और "
           "दीर्घ ऊ छपाई-भूल); इस शब्द पर प्रश्न नहीं। शुक्ल धर्म = उज्ज्वल या शुद्ध धर्म; आस्तिकत्व का सीधा अर्थ ‘आस्था’ रखा। "
           "छपा ‘सत्व’ = सत्त्व; ‘शौर्य्यं गांभीर्य्यं विपर्य्यय’ में य्य दुहराना छपाई की आदत। सन्धि जाँची: शौचम् + आस्तिकत्वम् → "
           "शौचमास्तिकत्वम्; बुद्धिः + मेधा → बुद्धिर्मेधा (इः + घोष → इर्); रुचिः + भक्तिः → रुचिर्भक्तिः; भक्तिः + अनभिष्वङ्गः → "
           "भक्तिरनभिष्वङ्गः; अनभिष्वङ्गः + तमो... → अनभिष्वङ्गस्तमो... (विसर्ग + त → स्); तमस् + गुण → तमोगुण; विपर्ययः + च → "
           "विपर्ययश्च।"),
    "24": ("गद्य-पंक्ति; विश्वास निम्न। पाठ-चिह्न: (१) ‘दुरुपघारताशौर्य्यं’ बिगड़ा शब्द, न विभाजित, न अनुवादित "
           "(‘दुरुपघाततता-अशौर्य’ केवल अनुमान); (२) छपा ‘क्रोधाहर्षः’ = क्रोध + अहर्ष (हर्ष का अभाव) पढ़ा, पर ‘क्रोधो हर्षः’ "
           "(क्रोध और हर्ष) की एक-मात्रा छपाई-भूल भी हो सकता है। इन पर प्रश्न नहीं। मात्सर्य इकाई २५ (तमस्) में भी है। सन्धि "
           "जाँची: मात्सर्यम् + अमित → मात्सर्यममित; अमितभाषित्वम् + अहंकारः → अमितभाषित्वमहंकारः; अहंकारः + लोलुपत्वम् → "
           "अहंकारो लोलुपत्वम् (अः + घोष → ओ); दम्भः + मानः → दम्भो मानः; मानः + क्रोध... (क से पहले विसर्ग रहता है); कामः + च → "
           "कामश्च।"),
    "25": ("गद्य-पंक्ति; विश्वास उच्च; पाठ-चिह्न नहीं। ‘निद्राऽऽलस्यं’ का दोहरा अवग्रह छपाई की आदत (निद्रा + आलस्यम्, आ + आ → "
           "आ)। विप्रतिपत्ति = विपरीत धारणा (‘भ्रम’, ‘उलटा आचरण’ भी सम्भव); अभिसंधान = षड्यन्त्र (‘छल’ भी सम्भव)। ‘क्षुत्तृष्णा’ "
           "जोड़ा: भूख और प्यास। छपा ‘सत्वगुणवैपरीत्यंच’ = सत्त्वगुणवैपरीत्यं च। सन्धि जाँची: तामसानि + अज्ञानम् → "
           "तामसान्यज्ञानम् (इ + अ → य); प्रमादः + निद्रा → प्रमादो निद्रा (अः + घोष → ओ); क्षुध् + तृष्णा → क्षुत्तृष्णा (अघोष से "
           "पहले ध् → त्); शोकः + मात्सर्यम् → शोको मात्सर्यम्; पर + अभिसंधानम् → पराभिसंधानम् (अ + अ → आ)।"),
}


# ===================================================================== AIDS
AIDS = {
    "14": {
        "chunks": "वायवीयानि | स्पर्शनं स्पर्शः | प्रश्वासोच्छ्वासादिपरिस्पंदनानि | लाघवं च",
        "sandhi": "अ + उ → ओ: प्रश्वास + उच्छ्वास → प्रश्वासोच्छ्वास · त् + श → च्छ: उत् + श्वास → उच्छ्वास · अ + आ → आ: "
                  "उच्छ्वास + आदि → उच्छ्वासादि।",
        "diagram": {"groups": [
            {"label": "वायु से सम्बन्धित (क्रम से)", "items": ["१ स्पर्शन (स्पर्श की इन्द्रिय)", "२ स्पर्श",
                                                          "३ श्वास आदि के स्पन्दन", "४ लाघव (हल्कापन)"]}]},
    },
    "15": {
        "chunks": "आग्नेयानि | दर्शनं रूपं | पित्तमूष्मापक्तिः | संतापो मेधा | वर्णो भास्तेजः | शौर्य्यं च",
        "sandhi": "अः + घोष → ओ: संतापः + मेधा → संतापो मेधा · विसर्ग + त → स्: भाः + तेजः → भास्तेजः · म् + स्वर: पित्तम् + "
                  "ऊष्मा → पित्तमूष्मा।",
        "diagram": {"groups": [
            {"label": "अग्नि से सम्बन्धित (क्रम से)", "items": ["दर्शन", "रूप", "पित्त", "ऊष्मा", "पक्ति", "संताप", "मेधा",
                                                           "वर्ण", "भा", "तेज", "शौर्य"]}]},
    },
    "16": {
        "chunks": "आंभसानि | रसनं रसः | स्वेदक्लेदवसारसासृक्शुक्रमूत्रादिद्रवसमूहः | शैथिल्यं स्नेहश्च",
        "sandhi": "अ + अ → आ: रस + असृज् → रसासृक् · अघोष से पहले ज् → क्: असृज् + शुक्र → असृक्शुक्र · विसर्ग + च → श्: "
                  "स्नेहः + च → स्नेहश्च।",
        "diagram": {"groups": [
            {"label": "जल से सम्बन्धित", "items": ["रसन (जिह्वा)", "रस (स्वाद)", "द्रवों का समूह", "शैथिल्य", "स्नेह"]},
            {"label": "द्रवों का समूह (क्रम से)", "items": ["स्वेद", "क्लेद", "वसा (सम्भावित: मांसगत चर्बी)",
                                                       "रस (पोषक द्रव)", "असृक् (रक्त)", "शुक्र", "मूत्र आदि"]}]},
        "contrast": "इसी पंक्ति में दो ‘रस’: पहला ‘रसः’ = स्वाद (रसन का विषय); समास के भीतर का ‘रस’ = पोषक द्रव (धातु)।",
    },
    "17": {
        "chunks": "पार्थिवानि | घ्राणं गंधः | केशनखास्थ्यादिमूर्त्तिसमूहो | धैर्य्यं गौरवं च",
        "sandhi": "इ + आ → या: अस्थि + आदि → अस्थ्यादि · अः + घोष → ओ: समूहः + धैर्यम् → समूहो धैर्यम्।",
        "anchors": ("याद-सूत्र (मेरी याद-पद्धति): हर भूत के साथ पहले इन्द्रिय, फिर उसका विषय: आकाश-श्रोत्र-शब्द, वायु-स्पर्शन-स्पर्श, "
                    "अग्नि-दर्शन-रूप, जल-रसन-रस, पृथ्वी-घ्राण-गन्ध (इकाई १३-१७)।"),
    },
    "18": {
        "chunks": "तेषु | मातृजानि मृदूनि | त्वग्रक्तमांसमेदोमज्ज | नाभिहृदयामाशयगर्भाशय | यकृत्प्लीहक्लोमांत्रगुदादीनि",
        "sandhi": "घोष से पहले च् → ग्: त्वच् + रक्त → त्वग्रक्त · घोष से पहले अस् → ओ: मेदस् + मज्जा → मेदोमज्ज · अ + आ → आ: "
                  "हृदय + आमाशय → हृदयामाशय।",
        "diagram": {"groups": [
            {"label": "माता से, कोमल (क्रम १-७)", "items": ["त्वचा", "रक्त", "मांस", "मेद", "मज्जा", "नाभि", "हृदय"]},
            {"label": "क्रम ८-१४", "items": ["आमाशय (पेट)", "गर्भाशय", "यकृत् (जिगर)", "प्लीहा (तिल्ली)",
                                         "क्लोम (पहचान विवादित)", "आन्त्र (आँत)", "गुद आदि"]}]},
    },
    "19": {
        "chunks": "पितृजानि | स्थिराणि | केशनखास्थिशुक्र | सिराधमन्यादीनि",
        "sandhi": "अ + अ → आ: नख + अस्थि → नखास्थि · ई + आ → या: धमनी + आदीनि → धमन्यादीनि।",
        "diagram": {"groups": [
            {"label": "पिता से, स्थिर (क्रम से)", "items": ["केश", "नख", "अस्थि", "शुक्र", "सिरा (सम्भवतः शिरा)",
                                                       "धमनी (सम्भवतः धमनी)"]}]},
    },
    "20": {
        "chunks": "आत्मजानि | तासु तासु योनिषूत्पत्तिः | मनश्चेतनेंद्रियाणि | प्राणापानौ धारणम् | आकृतिस्वरवर्णविशेषाः | "
                  "कामक्रोधलोभभय हर्षाः | धर्म्माधर्म्मशीलता | स्मृतिबुद्धीच्छाद्वेषप्रयत्नाहंकार | सुखदुःखायुरात्मज्ञानानि च",
        "sandhi": "उ + उ → ऊ: योनिषु + उत्पत्तिः → योनिषूत्पत्तिः · इः + घोष → इर्: उत्पत्तिः + मनः → उत्पत्तिर्मनः · विसर्ग + च → श्: "
                  "मनः + चेतना → मनश्चेतना · आ + इ → ए: चेतना + इन्द्रियाणि → चेतनेन्द्रियाणि · इ + इ → ई: बुद्धि + इच्छा → बुद्धीच्छा।",
        "diagram": {"groups": [
            {"label": "आत्मा से (पहला भाग, क्रम से)", "items": ["उन-उन योनियों में जन्म", "मन", "चेतना", "इन्द्रियाँ",
                                                             "प्राण और अपान", "धारण", "आकृति, स्वर, वर्ण की विशेषता",
                                                             "काम, क्रोध, लोभ, भय, हर्ष"]},
            {"label": "दूसरा भाग (क्रम से)", "items": ["धर्म-अधर्म का स्वभाव", "स्मृति, बुद्धि", "इच्छा, द्वेष", "प्रयत्न, अहंकार",
                                                    "सुख, दुःख", "आयु", "आत्मज्ञान (या आत्मा व ज्ञान)"]}]},
    },
    "21": {
        "chunks": "सात्म्यजान्यायुरायोग्यम् (= आरोग्यम्) | अनालस्यमलोलुपत्वम् | इंद्रियप्रसादस्वरवर्णबीजौजः | संपद्यशस्तनताः (?) | "
                  "प्रहर्षभूयस्त्वंमेधा | बलं च",
        "sandhi": "इ + आ → या: सात्म्यजानि + आयुः → सात्म्यजान्यायुः · अ + ओ → औ: बीज + ओजः → बीजौजः · अन्- (स्वर से पहले): "
                  "अन् + आलस्य → अनालस्य।",
        "frame": "स्रोत: सात्म्य (जो अभ्यास से अनुकूल हो) → फल: आयु, आरोग्य (सुधारा पाठ), आलस्य व लोभ का अभाव, साफ इन्द्रियाँ, "
                 "स्वर, वर्ण, बीज और ओज → (एक अस्पष्ट शब्द) → हर्ष की अधिकता, मेधा, बल।",
    },
    "22": {
        "chunks": "रसजानि | कृत्स्त्रस्य (= कृत्स्नस्य) देहस्य | संभवो वृत्तिर्वृद्धिस्तृप्तिरौल्यं (?) | पुष्टिरुत्साहश्च",
        "sandhi": "विसर्ग + त → स्: वृद्धिः + तृप्तिः → वृद्धिस्तृप्तिः · इः + स्वर → इर्: पुष्टिः + उत्साहः → पुष्टिरुत्साहः · "
                  "अः + घोष → ओ: संभवः + वृत्तिः → संभवो वृत्तिः।",
        "diagram": {"groups": [
            {"label": "रस से, पूरे शरीर के (क्रम से)", "items": ["संभव (उत्पत्ति)", "वृत्ति (चलते रहना)", "वृद्धि", "तृप्ति",
                                                            "औल्यं (अस्पष्ट)", "पुष्टि", "उत्साह"]}]},
    },
    "23": {
        "chunks": "शुद्धसत्वजानि | शौचमास्तिकत्वं कृतज्ञता दाक्षिण्यं | व्यवसायः शौर्य्यं गांभीर्य्यं | बुद्धिर्मेधा स्मृतिः | "
                  "शुक्लधर्म्हरूचिः (= शुक्लधर्मरुचिः) | भक्तिरनभिष्वंगः | तमोगुणविपर्य्ययश्च",
        "sandhi": "इः + घोष → इर्: बुद्धिः + मेधा → बुद्धिर्मेधा · विसर्ग + त → स्: अनभिष्वङ्गः + तमो... → अनभिष्वङ्गस्तमो... · "
                  "घोष से पहले अस् → ओ: तमस् + गुण → तमोगुण।",
        "diagram": {"groups": [
            {"label": "शुद्ध सत्त्व से (क्रम १-७)", "items": ["शौच", "आस्तिकत्व", "कृतज्ञता", "दाक्षिण्य", "व्यवसाय", "शौर्य",
                                                         "गाम्भीर्य"]},
            {"label": "क्रम ८-१४", "items": ["बुद्धि", "मेधा", "स्मृति", "शुक्ल धर्म में रुचि (सुधारा पाठ)", "भक्ति",
                                         "अनभिष्वङ्ग", "तमोगुण का विपर्यय"]}]},
    },
    "24": {
        "chunks": "राजसानि | दुरुपघारताशौर्य्यं (?) | मात्सर्य्यममितभाषित्वमहंकारो | लोलुपत्वं दंभो मानः | क्रोधाहर्षः (?) | कामश्च",
        "sandhi": "अः + घोष → ओ: अहंकारः + लोलुपत्वम् → अहंकारो लोलुपत्वम् · अः + घोष → ओ: दम्भः + मानः → दम्भो मानः · "
                  "विसर्ग + च → श्: कामः + च → कामश्च।",
        "frame": "स्रोत: रजस् → (एक अस्पष्ट शब्द) → मात्सर्य, अमितभाषित्व, अहंकार, लोलुपत्व, दम्भ, मान → क्रोध (और ‘अहर्ष’ या "
                 "‘हर्ष’: अनिश्चित) → काम।",
    },
    "25": {
        "chunks": "तामसान्यज्ञानं | विषादः प्रमादो | निद्राऽऽलस्यं | क्षुत्तृष्णा शोको | मात्सर्य्यं विप्रतिपत्तिः | पराभिसंधानं | "
                  "सत्वगुणवैपरीत्यंच",
        "sandhi": "इ + अ → य: तामसानि + अज्ञानम् → तामसान्यज्ञानम् · अघोष से पहले ध् → त्: क्षुध् + तृष्णा → क्षुत्तृष्णा · "
                  "अ + अ → आ: पर + अभिसंधानम् → पराभिसंधानम्।",
        "diagram": {"groups": [
            {"label": "तमस् से सम्बन्धित (क्रम से)", "items": ["अज्ञान", "विषाद", "प्रमाद", "निद्रा", "आलस्य", "भूख-प्यास",
                                                           "शोक", "मात्सर्य", "विप्रतिपत्ति", "पराभिसंधान",
                                                           "सत्त्व गुण का विपरीत भाव"]}]},
    },
}


# ===================================================================== IMAGE_SPECS
IMAGE_SPECS = {
    ("14", "diagram"): {
        "file": "sh5-vayaviya-14.svg",
        "alt": ("Flowchart of unit 14: from 'belonging to wind' four numbered items in line order: the touch faculty, touch, "
                "the movements beginning with the breaths, lightness."),
        "type": "mermaid",
        "code": ("flowchart LR\n"
                 "  A[\"वायु से सम्बन्धित\"] --> B[\"१ स्पर्शन (इन्द्रिय)\"]\n"
                 "  A --> C[\"२ स्पर्श\"]\n"
                 "  A --> D[\"३ श्वास आदि के स्पन्दन\"]\n"
                 "  A --> E[\"४ लाघव (हल्कापन)\"]\n"),
    },
    ("15", "diagram"): {
        "file": "sh5-agneya-15.svg",
        "alt": ("Table of unit 15, the eleven fire items in line order with meanings: darśana (sight), rūpa (form), Pitta, "
                "ūṣman (heat), pakti (digestion), saṃtāpa (burning heat), medhā (intelligence), varṇa (colour), bhā "
                "(radiance), tejas (brilliance), śaurya (valour)."),
        "type": "table",
        "title": "इकाई १५: अग्नि से सम्बन्धित",
        "heads": ["शब्द", "अर्थ"],
        "rows": [["दर्शन", "देखने की इन्द्रिय"], ["रूप", "रूप"], ["पित्त", "दोष"], ["ऊष्मा", "गर्मी"], ["पक्ति", "पाचन"],
                 ["संताप", "तीव्र गर्मी"], ["मेधा", "बुद्धि-शक्ति"], ["वर्ण", "रंग"], ["भा", "दीप्ति"], ["तेज", "तेज"],
                 ["शौर्य", "वीरता"]],
    },
    ("16", "diagram"): {
        "file": "sh5-ambhasa-16.svg",
        "alt": ("Two columns of unit 16. Of water: tongue (rasana), taste (rasa), the mass of fluids, looseness, unctuousness. "
                "The mass of fluids in order: sweat, moisture, vasā (probably muscle-fat), rasa (the nutritive fluid), "
                "blood, semen, urine and so on."),
        "type": "split",
        "title": "इकाई १६: जल से सम्बन्धित",
        "cols": [["जल से (क्रम से)", ["१ रसन (जिह्वा)", "२ रस (स्वाद)", "३ द्रवों का समूह", "४ शैथिल्य (ढीलापन)",
                                     "५ स्नेह (चिकनाई)"]],
                 ["द्रवों का समूह", ["स्वेद (पसीना)", "क्लेद (गीलापन)", "वसा (सम्भावित: चर्बी)", "रस (पोषक द्रव)",
                                    "असृक् (रक्त)", "शुक्र (वीर्य)", "मूत्र आदि"]]],
    },
    ("18", "diagram"): {
        "file": "sh5-matrja-18.svg",
        "alt": ("Table of unit 18, the mother-born soft parts in line order: skin, blood, flesh, fat, marrow, navel, heart, "
                "stomach, uterus, liver, spleen (all organ names standard), kloma (identity disputed), intestines, rectum and so on."),
        "type": "table",
        "title": "इकाई १८: माता से उत्पन्न, कोमल",
        "heads": ["शब्द", "अर्थ"],
        "rows": [["त्वक्", "त्वचा"], ["रक्त", "रक्त"], ["मांस", "मांस"], ["मेदस्", "चर्बी"], ["मज्जा", "मज्जा"],
                 ["नाभि", "नाभि"], ["हृदय", "हृदय (मानक)"], ["आमाशय", "पेट (मानक)"], ["गर्भाशय", "गर्भाशय (मानक)"],
                 ["यकृत्", "जिगर (मानक)"], ["प्लीहा", "तिल्ली (मानक)"], ["क्लोम", "पहचान विवादित"],
                 ["आन्त्र", "आँत (मानक)"], ["गुद आदि", "मलद्वार (मानक)"]],
    },
    ("19", "diagram"): {
        "file": "sh5-pitrja-19.svg",
        "alt": ("Flowchart of unit 19: father-born, firm; six numbered items in line order: hair, nails, bones, semen, sirā "
                "(probably veins), dhamanī (probably arteries)."),
        "type": "mermaid",
        "code": ("flowchart LR\n"
                 "  A[\"पिता से उत्पन्न: स्थिर\"] --> B[\"१ केश\"]\n"
                 "  A --> C[\"२ नख\"]\n"
                 "  A --> D[\"३ अस्थि\"]\n"
                 "  A --> E[\"४ शुक्र\"]\n"
                 "  A --> F[\"५ सिरा (सम्भवतः शिरा)\"]\n"
                 "  A --> G[\"६ धमनी (सम्भावित)\"]\n"),
    },
    ("20", "diagram"): {
        "file": "sh5-atmaja-20.svg",
        "alt": ("Table of unit 20, the self-born items grouped by printed compound in line order: birth in this and that "
                "womb; mind, consciousness, senses; prāṇa and apāna; sustaining; distinct form, voice, colour; desire, anger, "
                "greed, fear, joy; disposition to dharma and adharma; memory, intellect, wish, aversion, effort, ego; "
                "pleasure, pain, lifespan; self-knowledge (or self and knowledge)."),
        "type": "table",
        "title": "इकाई २०: आत्मा से उत्पन्न",
        "heads": ["अंश", "अर्थ"],
        "rows": [["तासु तासु योनिषूत्पत्तिः", "उन-उन योनियों में जन्म"], ["मनश्चेतनेंद्रियाणि", "मन, चेतना, इन्द्रियाँ"],
                 ["प्राणापानौ", "प्राण और अपान"], ["धारणम्", "धारण"],
                 ["आकृतिस्वरवर्णविशेषाः", "आकृति, स्वर, वर्ण की विशेषता"],
                 ["कामक्रोधलोभभय हर्षाः", "काम, क्रोध, लोभ, भय, हर्ष"], ["धर्म्माधर्म्मशीलता", "धर्म-अधर्म का स्वभाव"],
                 ["स्मृतिबुद्धीच्छाद्वेष", "स्मृति, बुद्धि, इच्छा, द्वेष"], ["प्रयत्नाहंकार", "प्रयत्न, अहंकार"],
                 ["सुखदुःखायुः", "सुख, दुःख, आयु"], ["आत्मज्ञानानि", "आत्मज्ञान (या आत्मा व ज्ञान)"]],
    },
    ("22", "diagram"): {
        "file": "sh5-rasaja-22.svg",
        "alt": ("Flowchart of unit 22: born of rasa, of the whole body; seven numbered items in line order: coming into being, "
                "maintenance, growth, satisfaction, an unclear word (aulya), nourishment, vigour."),
        "type": "mermaid",
        "code": ("flowchart LR\n"
                 "  A[\"रस से: पूरे शरीर के\"] --> B[\"१ संभव (उत्पत्ति)\"]\n"
                 "  A --> C[\"२ वृत्ति\"]\n"
                 "  A --> D[\"३ वृद्धि\"]\n"
                 "  A --> E[\"४ तृप्ति\"]\n"
                 "  A --> F[\"५ औल्यं (अस्पष्ट)\"]\n"
                 "  A --> G[\"६ पुष्टि\"]\n"
                 "  A --> H[\"७ उत्साह\"]\n"),
    },
    ("23", "diagram"): {
        "file": "sh5-sattvaja-23.svg",
        "alt": ("Table of unit 23, the fourteen traits born of pure sattva in line order: purity, belief, gratitude, courtesy, "
                "resolve, valour, depth, intellect, intelligence, memory, liking for bright dharma (corrected reading), "
                "devotion, non-attachment, the contrary of tamas."),
        "type": "table",
        "title": "इकाई २३: शुद्ध सत्त्व से उत्पन्न",
        "heads": ["शब्द", "अर्थ"],
        "rows": [["शौच", "शुचिता"], ["आस्तिकत्व", "आस्था"], ["कृतज्ञता", "किए उपकार को मानना"], ["दाक्षिण्य", "शिष्टता"],
                 ["व्यवसाय", "निश्चय"], ["शौर्य", "वीरता"], ["गाम्भीर्य", "गहराई"], ["बुद्धि", "बुद्धि"], ["मेधा", "बुद्धि-शक्ति"],
                 ["स्मृति", "स्मरण"], ["शुक्लधर्मरुचि", "शुद्ध धर्म में रुचि (सुधारा पाठ)"], ["भक्ति", "भक्ति"],
                 ["अनभिष्वङ्ग", "अनासक्ति"], ["तमोगुणविपर्यय", "तमोगुण का उलटा"]],
    },
    ("25", "diagram"): {
        "file": "sh5-tamasa-25.svg",
        "alt": ("Table of unit 25, the tamas traits in line order: ignorance, dejection, heedlessness, sleep, laziness, hunger "
                "and thirst, grief, envy, wrong notion, scheming against others, the contrary of sattva."),
        "type": "table",
        "title": "इकाई २५: तमस् से सम्बन्धित",
        "heads": ["शब्द", "अर्थ"],
        "rows": [["अज्ञान", "अज्ञान"], ["विषाद", "उदासी"], ["प्रमाद", "असावधानी"], ["निद्रा", "नींद"], ["आलस्य", "आलस्य"],
                 ["क्षुत्तृष्णा", "भूख और प्यास"], ["शोक", "शोक"], ["मात्सर्य", "ईर्ष्या"], ["विप्रतिपत्ति", "विपरीत धारणा"],
                 ["पराभिसंधान", "दूसरों के विरुद्ध षड्यन्त्र"], ["सत्त्वगुणवैपरीत्य", "सत्त्व गुण का उलटा"]],
    },
}
