from helpers import mcq, match, order, fill, multi, accepts

AUTHORED = {}

# ---------------------------------------------------------------- unit 26
AUTHORED["26"] = {
    "title": "फलमज्जाक्वाथं वा",
    "question": "Which decoction does unit 26 give, with which addition and mixture, and against what?",
    "rule": ("Or a decoction of the fruit kernel (majjā), with an addition of vatsaka and the rest, mixed with the decoction "
             "of either nimba or arka: it removes all Kapha ailments arising from satiation (saṃtarpaṇa)."),
    "limits": ("The unit has no verb; the giving is understood from the lines before. The vatsaka group is not listed here. "
               "IDs (standard, from the data): vatsaka = kuṭaja (Holarrhena), nimba = neem, arka = Calotropis. "
               "No dose or amount is given."),
    "explain_hi": ("एक और योग: फल यानी मैनफल की मज्जा (भीतरी गिरी) का क्वाथ। "
                   "उसमें वत्सक यानी कुटज (कुड़ा) आदि का प्रतिवाप, यानी ऊपर से डाला गया द्रव्य, मिलता है; उस समूह के सदस्य यहाँ नहीं गिनाए गए। "
                   "फिर उसे निम्ब यानी नीम या अर्क यानी आक, इन दो में से किसी एक के काढ़े से मिलाया जाता है। "
                   "फल: संतर्पण (अधिक पोषण, तृप्ति) से उपजे सब कफ-रोगों को हरता है। "
                   "‘अन्यतर’ का अर्थ है दो में से कोई एक।"),
    "hook": "गिरी का क्वाथ + वत्सक का प्रतिवाप + नीम या आक का काढ़ा = संतर्पण के कफ-रोग दूर।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "Which ailments does the decoction of unit 26 remove?",
            ("Kapha ailments from satiation", "सन्तर्पणोत्थ-सर्वश्लेष्मव्याधि-हरम् = removing all Kapha ailments arising from satiation."),
            [("Vāta ailments from fasting", "Vāta and fasting are not named; the text says Kapha (श्लेष्म) and satiation."),
             ("Pitta ailments from heat", "Pitta and heat are not named in this unit."),
             ("Blood ailments from injury", "Neither blood nor injury is named in this unit.")],
            "The decoction removes every Kapha ailment that arises from satiation (saṃtarpaṇa).",
            "सन्तर्पण + उत्थ = arising from satiation; श्लेष्मव्याधि = Kapha ailment; हर = removing."),
        order(1, "Put these parts of unit 26 in the order of the text.",
              ["फलमज्जाक्वाथम्", "वत्सकादिप्रतिवापम्", "निम्बार्कान्यतरकषायोपसर्जनम्", "सन्तर्पणोत्थसर्वश्लेष्मव्याधिहरम्"],
              "The base decoction, its addition, its mixture, and what it removes.",
              "फलमज्जाक्वाथं वा · वत्सकादिप्रतिवापं · निम्बार्कान्यतरकषायोपसर्जनं · सन्तर्पणोत्थसर्वश्लेष्मव्याधिहरम्."),
        match(2, "Match each drug of unit 26 to its identification in the card.",
              [["वत्सक", "kuṭaja, Holarrhena (standard)"], ["निम्ब", "neem (standard)"],
               ["अर्क", "Calotropis, madar (standard)"], ["फलमज्जा", "kernel of the (madana) fruit"]],
              "Vatsaka is the addition, nimba or arka gives the mixing decoction, and the kernel gives the base decoction.",
              "वत्सक = कुटज; निम्ब = नीम; अर्क = आक; फलमज्जा = fruit kernel.",
              role="extend",
              teaches="In unit 26, vatsaka (वत्सक) = kuṭaja (Holarrhena), nimba (निम्ब) = neem, arka (अर्क) = Calotropis (madar)."),
        mcq("discriminate", 3, "Which is the right split of सन्तर्पणोत्थ-?",
            ("सन्तर्पण + उत्थ", "अ + उ → ओ: सन्तर्पण + उत्थ → सन्तर्पणोत्थ."),
            [("सन्तर्पणा + ओत्थ", "There is no word ओत्थ; the second member is उत्थ (arising)."),
             ("सन्तर्पणः + उत्थ", "अः + उ would give अ उ with a gap (सन्तर्पण उत्थ), not ओ."),
             ("सन्तर्पणि + उत्थ", "इ + उ would give यु (सन्तर्पण्युत्थ), not ओ.")],
            "Inside the compound, सन्तर्पण (satiation) + उत्थ (arising): अ + उ → ओ.",
            "अ/आ + उ/ऊ → ओ."),
        mcq("apply", 4, "A helper has no nimba. With what may the kernel decoction of unit 26 still be mixed?",
            ("A decoction of arka", "निम्ब-अर्क-अन्यतर = either nimba or arka; one of the two is enough."),
            [("A decoction of paṭolī", "Paṭolī is named in line 05.01.38, not in this unit."),
             ("A decoction of triphalā", "Triphalā is not named in this unit."),
             ("A decoction of vatsaka", "Vatsaka is the addition (प्रतिवाप), not the mixing decoction.")],
            "अन्यतर = either of the two: nimba or arka.",
            "निम्बार्कान्यतरकषाय = the decoction of either nimba or arka."),
        mcq("transfer", 5, "निम्बार्कान्यतर means either of nimba and arka. What does a new phrase मधुघृतयोरन्यतरम् mean?",
            ("Either honey or ghee", "अन्यतर = one of two: either honey or ghee."),
            [("Both honey and ghee", "Both would be उभे, not अन्यतर."),
             ("Neither honey nor ghee", "'Neither' needs a negative; अन्यतर has none."),
             ("Any one of many drugs", "That is अन्यतम (one of many); अन्यतर is one of two.")],
            "अन्यतर picks one of two; अन्यतम picks one of three or more.",
            "अन्यतर = either of two; अन्यतम = any one of many.",
            teaches="अन्यतर means 'either of two' (निम्ब or अर्क; मधु or घृत); अन्यतम means 'any one of many'."),
    ],
}

# ---------------------------------------------------------------- unit 27
AUTHORED["27"] = {
    "title": "फलपिप्पलीनां वा फलादिनिर्यूहेण",
    "question": "How does unit 27 prepare the fruit-pippalīs so that a delicate patient vomits easily?",
    "rule": ("Steep the fruit-pippalīs twenty-one times in a decoction of phala and the rest, dust with a pollen-fine powder, "
             "keep (in a lotus) a night, powder again in the morning; the patient drinks to the neck, smelling, and vomits easily."),
    "limits": ("Low confidence. The placing in the lotus has no verb. The drink list (haridrā / kṛsarā, maybe one dish) "
               "is unclear and not questioned; nor are the misprints sāyānhe, bṛhata, krasarā. What is smelt is not stated. "
               "समुचितगन्धसम्पदुत्क्लिष्टकफपित्तः is read as one bahuvrīhi; it may be separate qualities."),
    "explain_hi": ("यह कोमल और दवा से घृणा करने वाले रोगी के लिए वमन की विधि है। "
                   "फल-पिप्पलियाँ फल आदि के काढ़े में इक्कीस बार भली-भाँति भावित की जाती हैं और फूल के पराग जैसे महीन चूर्ण से ढकी जाती हैं। "
                   "फिर वे सरोवर के बड़े कमल में रात भर रहती हैं (रखने की क्रिया पाठ में नहीं है), और प्रातः फिर चूर्ण लगाकर निकाली जाती हैं। "
                   "रोगी सेंधा नमक, गुड़ और फाणित यानी राब मिला एक पेय गले तक पीता है और सूँघता है। "
                   "लम्बे समास के एक पाठ के अनुसार उचित सुगन्ध से उसके कफ-पित्त उभर आते हैं (उसे अलग-अलग गुण भी पढ़ा जा सकता है), और वह सुख से वमन करता है।"),
    "hook": "इक्कीस बार भावित, कमल में रात भर, सुबह सूँघो: दवा से चिढ़ने वाला भी सुख से वमन करे।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "For which patient is the fragrant method of unit 27 meant?",
            ("A delicate one who hates medicine", "सुकुमारः … भेषजद्वेषी च = a delicate person who hates medicine."),
            [("A strong one with old fever", "Neither strength nor fever is named in this unit."),
             ("A child with a cough and cold", "No child, cough or cold is named in this unit."),
             ("An old man with weak digestion", "Old age and digestion are not named in this unit.")],
            "The method suits a delicate person who hates medicine: fragrance makes him vomit easily.",
            "सुकुमार = delicate; भेषजद्वेषी = one who hates medicine."),
        order(1, "Put these steps of unit 27 in the order of the text.",
              ["एकविंशतिकृत्वः सुभावितानाम्", "कुसुमरजःसदृशेन चूर्णेनावचूर्णयेत्", "तद्रात्रिमुषितम्",
               "प्रभाते पुनरुपचूर्णितमुद्धृत्य", "आकण्ठं पीतवानुपजिघ्रन्", "सुखेन छर्दयति"],
              "Steep, dust, keep a night, powder again and take out, drink to the neck while smelling, vomit easily.",
              "भावित → अवचूर्णयेत् → रात्रिमुषितम् → प्रभाते उद्धृत्य → पीतवान् उपजिघ्रन् → छर्दयति."),
        match(2, "Match each word of unit 27 to its meaning.",
              [["एकविंशतिकृत्वः", "twenty-one times"], ["कुसुमरजःसदृश", "like the pollen of flowers"],
               ["आकण्ठम्", "up to the neck"], ["उपजिघ्रन्", "smelling"]],
              "How often it is steeped, how fine the powder is, how much is drunk, and what the patient does.",
              "एकविंशतिकृत्वः = 21 times; कुसुमरजःसदृश = pollen-like; आकण्ठम् = to the neck; उपजिघ्रन् = smelling.",
              role="extend",
              teaches="Unit 27: steeped twenty-one times (एकविंशतिकृत्वः), a pollen-fine powder, drunk up to the neck (आकण्ठम्), while smelling (उपजिघ्रन्)."),
        multi("discriminate", 3, "Which two of these additions does unit 27 name for the drink?",
              [("Rock salt (सैन्धव)", "Right: सैन्धवगुडफाणितोपेतम् names rock salt."),
               ("Honey (मधु)", "Wrong: honey is not named in this unit."),
               ("Jaggery (गुड)", "Right: गुड is named, with phāṇita."),
               ("Ghee (घृत)", "Wrong: ghee is not named in this unit.")],
              [0, 2],
              "The drink comes with rock salt, jaggery and phāṇita (thick cane-juice syrup).",
              "सैन्धव-गुड-फाणित-उपेत = with rock salt, jaggery and phāṇita added."),
        mcq("apply", 4, "What is done with the steeped fruit-pippalīs in the morning, by unit 27?",
            ("Powdered again, then taken out", "प्रभाते पुनरुपचूर्णितमुद्धृत्य = in the morning, powdered again and taken out."),
            [("Boiled in milk and then strained", "No boiling or straining is named in this unit."),
             ("Dried in the sun and then ground", "No sun-drying is named; they are powdered again (पुनरुपचूर्णित)."),
             ("Burnt, and the ash kept aside", "No burning or ash is named in this unit.")],
            "In the morning (प्रभाते) the pippalīs are powdered again (पुनर् उपचूर्णित) and taken out (उद्धृत्य).",
            "प्रभाते पुनरुपचूर्णितमुद्धृत्य = in the morning, powdered again, taken out."),
        mcq("transfer", 5, "एकविंशतिकृत्वः means twenty-one times. What does a new word सप्तकृत्वः mean?",
            ("Seven times", "-कृत्वः after a number = so many times: सप्त + कृत्वः."),
            [("A seventh part", "A part would be सप्तम भाग, not -कृत्वः."),
             ("Seven kinds", "Kinds would be सप्तविध."),
             ("In the seventh", "The ordinal locative would be सप्तमे.")],
            "Number + -कृत्वः = that many times.",
            "-कृत्वः = 'times' after a number.",
            teaches="-कृत्वः after a number means 'so many times': एकविंशतिकृत्वः (21 times), सप्तकृत्वः (seven times)."),
    ],
}

# ---------------------------------------------------------------- unit 28
AUTHORED["28"] = {
    "title": "एतेन सर्वमाल्यगन्धप्रावरणपटाः",
    "question": "What does unit 28 say is explained by the method just given?",
    "rule": "By this, all garlands, perfumes, wraps and cloths are explained.",
    "limits": ("'This' is the fragrance method of line 05.01.28 by the order of the text; the line itself does not name it "
               "and gives no steps. प्रावरणपट may be one item (cloth wraps) or two; no question counts the items."),
    "explain_hi": ("यह छोटी पंक्ति पिछली सुगन्ध-विधि को आगे फैलाती है। "
                   "‘एतेन व्याख्याताः’ का अर्थ है: इसी से (इसी विधि से) ये भी समझा दिए गए। "
                   "सूची है: सब माल्य यानी मालाएँ, गन्ध यानी सुगन्धित द्रव्य, प्रावरण यानी ओढ़ने के वस्त्र और पट यानी कपड़े। "
                   "‘प्रावरणपट’ एक वस्तु (ओढ़ने का कपड़ा) भी हो सकती है और दो भी; यहाँ दो पढ़ा गया है।"),
    "hook": "कमल की तरह माला, गन्ध, ओढ़नी और कपड़ा भी: एतेन व्याख्याताः।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "What does unit 28 say about garlands and perfumes?",
            ("They are explained by this", "एतेन … व्याख्याताः = by this they are explained."),
            [("They must never be used", "No ban is stated; व्याख्याताः means 'explained'."),
             ("They are given to drink", "No drinking is named in this unit."),
             ("They are burnt on fire", "No burning is named in this unit.")],
            "The unit extends the method just given to garlands, perfumes, wraps and cloths.",
            "एतेन = by this; व्याख्याताः = are explained."),
        order(1, "Put the items of unit 28 in the order of the text.",
              ["माल्य (माला)", "गन्ध", "प्रावरण", "पट"],
              "Garlands, perfumes, wraps, cloths: सर्वमाल्यगन्धप्रावरणपटाः.",
              "माल्य · गन्ध · प्रावरण · पट."),
        match(2, "Match each member of unit 28's compound to its meaning.",
              [["माल्य", "garland"], ["गन्ध", "perfume"], ["प्रावरण", "wrap"], ["पट", "cloth"]],
              "The four members of सर्वमाल्यगन्धप्रावरणपटाः, as the card renders them.",
              "माल्य = garland; गन्ध = perfume; प्रावरण = wrap; पट = cloth.",
              role="extend",
              teaches="माल्य = garland, गन्ध = perfume, प्रावरण = wrap, पट = cloth: all 'explained by this' in unit 28."),
        mcq("discriminate", 3, "Which English rendering of unit 28 has one wrong word?",
            ("By this, all garlands and perfumes are forbidden", "Wrong: व्याख्याताः is 'explained', not 'forbidden'."),
            [("By this, all garlands and perfumes are explained", "Correct: this is the card's rendering."),
             ("Through this, all garlands and perfumes are explained", "Correct: एतेन can be 'through this'."),
             ("By this, every garland and perfume is explained", "Correct: सर्व = all, every.")],
            "व्याख्याताः (vi-ā-√khyā, past participle) = explained.",
            "व्याख्यात = explained."),
        mcq("apply", 4, "By the order of the text, what does एतेन (by this) in unit 28 point back to?",
            ("The fragrant lotus method of line 05.01.28", "That method uses fragrance; garlands and perfumes are carriers of fragrance."),
            [("The ghee cooked as before of line 05.01.42", "That line comes after, not before, unit 28."),
             ("The surā with decoction of line 05.01.36", "That line comes after unit 28."),
             ("The jīmūtaka powder of line 05.01.39", "That line comes after unit 28.")],
            "एतेन takes up what was just said: the fragrance method of line 05.01.28.",
            "एतेन = by this (the preceding method)."),
        mcq("transfer", 5, "In unit 28, व्याख्याताः agrees with the masculine plural noun. Which new sentence agrees correctly?",
            ("एतेन तैलानि व्याख्यातानि", "तैलानि is neuter plural, so the participle is व्याख्यातानि."),
            [("एतेन तैलानि व्याख्याताः", "व्याख्याताः is masculine plural; तैलानि is neuter."),
             ("एतेन तैलानि व्याख्याता", "व्याख्याता is feminine singular."),
             ("एतेन तैलानि व्याख्यातम्", "व्याख्यातम् is singular; तैलानि is plural.")],
            "The past participle takes the gender and number of its noun.",
            "Participle agrees with its noun: पटाः व्याख्याताः, तैलानि व्याख्यातानि.",
            teaches="A past participle agrees with its noun: पटाः व्याख्याताः (m. pl.), तैलानि व्याख्यातानि (n. pl.)."),
    ],
}

# ---------------------------------------------------------------- unit 29
AUTHORED["29"] = {
    "title": "एवमेव च फलाभावे",
    "question": "What does unit 29 prepare when the madana fruit is not to be had?",
    "rule": "In just this way, in the absence of fruit, one should prepare madana flowers and unripe fruits (śalāṭu).",
    "limits": ("'In this way' means by the same procedures as the fruit; no new step is given. "
               "शलाटु is taken as unripe fruit. Madana = emetic nut, मैनफल (standard in this chapter)."),
    "explain_hi": ("यह इकाई विकल्प देती है: जब फल न मिले (फलाभावे), तब मदन यानी मैनफल के पुष्प और शलाटु यानी कच्चे फल लिए जाएँ। "
                   "उन्हें ‘एवमेव’ यानी इसी प्रकार, अर्थात् फल की ही विधियों से तैयार करे। "
                   "‘फलाभावे’ = फल + अभावे, यानी फल के न होने पर। "
                   "क्रिया ‘कल्पयेत्’ है: तैयार करे।"),
    "hook": "फल नहीं? तो मैनफल के फूल और कच्चे फल, उसी विधि से।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "What does unit 29 use when the fruit is not available?",
            ("Madana flowers and unripe fruits", "मदनपुष्पाणि शलाटूनि च = madana flowers and unripe fruits."),
            [("Madana roots and bark", "Roots and bark are not named in this unit."),
             ("Neem leaves and seeds", "Neem is not named in this unit."),
             ("Pippalī and ginger", "Neither is named in this unit.")],
            "In the absence of fruit, the flowers and the unripe fruits of madana are prepared.",
            "फलाभावे = in the absence of fruit; पुष्प = flower; शलाटु = unripe fruit."),
        match(1, "Match each word of unit 29 to its meaning.",
              [["फलाभावे", "in the absence of fruit"], ["मदनपुष्प", "madana flower"], ["शलाटु", "unripe fruit"],
               ["कल्पयेत्", "one should prepare"]],
              "The condition, the two substitutes and the verb.",
              "फलाभावे = when fruit is lacking; मदनपुष्प = madana flower; शलाटु = unripe fruit; कल्पयेत् = should prepare."),
        fill(2, "The word of unit 29 for unripe fruit is ____ (type it in Devanagari or in English letters, e.g. dharma).",
             accepts("शलाटु"),
             "शलाटु (here शलाटूनि, n. acc. pl.) = unripe fruit.",
             "शलाटु = unripe fruit: in the absence of ripe fruit, madana's unripe fruits are prepared the same way.",
             "शलाटु = unripe fruit."),
        mcq("discriminate", 3, "Which is the right split of फलाभावे?",
            ("फल + अभावे", "अ + अ → आ: फल + अभावे → फलाभावे."),
            [("फल + भावे", "भावे (in being) would give फलभावे, with no आ."),
             ("फले + आभावे", "There is no word आभाव; and ए + आ does not give आ."),
             ("फलः + अभावे", "अः + अ would give ओऽ (फलोऽभावे).")],
            "फल + अभाव (absence): अ + अ → आ; the sense is 'in the absence of fruit'.",
            "अ + अ → आ."),
        mcq("apply", 4, "Having madana flowers but no fruit, how should they be prepared by unit 29?",
            ("By the same procedures as the fruit", "एवमेव = in just this way: as the fruit was prepared."),
            [("Only as a smoke for the nose", "No smoke is named; एवमेव points to the same procedures."),
             ("Only as an oil for the skin", "No oil is named; एवमेव points to the same procedures."),
             ("By a new method given here", "No new method is given: एवमेव refers back.")],
            "एवमेव (in just this way) means the procedures already given for the fruit.",
            "एवम् + एव = in just this way."),
        mcq("transfer", 5, "फलाभावे means in the absence of fruit. What does a new phrase जलाभावे mean?",
            ("In the absence of water", "जल + अभावे: X-अभावे = when X is lacking."),
            [("In the presence of water", "अभाव is absence, not presence."),
             ("Instead of the fruit", "Fruit is not named in जलाभावे."),
             ("In the water itself", "That would be जले, without अभाव.")],
            "X-अभावे (locative) = in the absence of X.",
            "X + अभावे = when X is not available.",
            teaches="X-अभावे means 'in the absence of X': फलाभावे (of fruit), जलाभावे (of water)."),
    ],
}

# ---------------------------------------------------------------- unit 30
AUTHORED["30"] = {
    "title": "इति फलविधानमुक्तम्",
    "question": "What does unit 30 close?",
    "rule": "Thus the procedure for the fruit (phala-vidhāna) has been stated: the section on the madana fruit ends here.",
    "limits": "A closing formula only: no drug, step or use is named. The next lines turn to jīmūtaka.",
    "explain_hi": ("यह समापन-वाक्य है: ‘इस प्रकार फल की विधि कही गई’। "
                   "‘फल’ यहाँ मदनफल यानी मैनफल है, जिसकी विधियाँ इससे पहले की पंक्तियों में आईं। "
                   "‘उक्तम्’ √वच् (कहना) का भूतकालिक कृदन्त है: कहा गया। "
                   "इसके बाद पाठ जीमूतक के योगों पर जाता है।"),
    "hook": "इति फलविधानमुक्तम्: मैनफल का अध्याय-खण्ड यहाँ पूरा।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "What does unit 30 say has been stated?",
            ("The procedure for the fruit", "फलविधानम् उक्तम् = the procedure for the fruit has been stated."),
            [("The list of all diseases", "No disease is named in this unit."),
             ("The rules for purging", "Purging is not named in this unit."),
             ("The signs of good vomiting", "No signs are named in this unit.")],
            "इति फलविधानमुक्तम् closes the procedures for the (madana) fruit.",
            "फलविधान = procedure for the fruit; उक्तम् = stated."),
        match(1, "Match each word of unit 30 to its meaning.",
              [["इति", "thus"], ["फलविधानम्", "procedure for the fruit"], ["उक्तम्", "has been stated"]],
              "A closing word, the topic, and the participle.",
              "इति = thus; फलविधानम् = procedure for the fruit; उक्तम् = stated."),
        fill(2, "In unit 30, the word meaning has been stated is ____ (type it in Devanagari or in English letters, e.g. dharma).",
             accepts("उक्तम्"),
             "उक्तम् is the past participle of √वच् (to speak): stated, said.",
             "उक्तम् (√वच्, past participle) = has been stated.",
             "उक्तम् = stated."),
        mcq("discriminate", 3, "Which is the right split of फलविधानमुक्तम्?",
            ("फलविधानम् + उक्तम्", "Final म् before a vowel is written joined: …नम् + उ… → …नमु…"),
            [("फलविधानः + उक्तम्", "अः + उ would give अ उ with a gap (फलविधान उक्तम्)."),
             ("फलविधाने + उक्तम्", "ए + उ would give अयु (फलविधानयुक्तम्)."),
             ("फलविधान + मुक्तम्", "मुक्तम् means 'released'; the verb here is उक्तम्, stated.")],
            "The म् of फलविधानम् joins the vowel of उक्तम् in writing; the words do not change.",
            "म् + vowel → written together (no sound change)."),
        mcq("apply", 4, "By the order of the text, which drug do the procedures closed in unit 30 concern?",
            ("Madana, the emetic nut", "The fruit (फल) of these lines is madana; its procedures end here."),
            [("Jīmūtaka, the bitter luffa", "Jīmūtaka starts after this close, in line 05.01.32."),
             ("Ikṣvāku, the bottle gourd", "Ikṣvāku comes later in the chapter."),
             ("Kuṭaja, the Holarrhena tree", "Kuṭaja's fruit comes later in the chapter.")],
            "फलविधान = the madana-fruit procedures; jīmūtaka follows next.",
            "फल = madana in this section."),
        mcq("transfer", 5, "उक्तम् is the past participle of √वच्. Which new sentence means Thus the procedure for the flower has been stated?",
            ("इति पुष्पविधानमुक्तम्", "पुष्प + विधानम् + उक्तम्, built like unit 30."),
            [("इति पुष्पविधानं वक्ष्यते", "वक्ष्यते is future: 'will be stated'."),
             ("इति पुष्पविधानं वदति", "वदति is present active: 'he says'."),
             ("इति पुष्पविधानं वदेत्", "वदेत् is optative: 'he should say'.")],
            "उक्तम् = has been stated (done); future, present and optative change the meaning.",
            "इति X-विधानम् उक्तम् = thus the procedure of X has been stated.",
            teaches="इति … उक्तम् closes a topic: 'thus … has been stated'; उक्तम् is the past participle of √वच्."),
    ],
}

# ---------------------------------------------------------------- unit 31
AUTHORED["31"] = {
    "title": "एवं च जीमूतकादीनपि कल्पयेत्",
    "question": "What does verse 31 say about jīmūtaka and the rest, and where is jīmūta especially used?",
    "rule": ("In this way one should also prepare jīmūtaka and the rest; but especially in fever, śvāsa (breathlessness), "
             "hiccup (hikkā) and the like, jīmūta."),
    "limits": ("The second line has no verb (elliptical). जीमूत is taken as short for जीमूतक. 'The rest' are not listed. "
               "Jīmūtaka = bitter luffa (probable, by the data of line 05.01.37)."),
    "explain_hi": ("मैनफल की विधि पूरी होने के बाद यह श्लोक कहता है कि इसी प्रकार जीमूतक आदि को भी तैयार करे। "
                   "जीमूतक को सम्भावित रूप से देवदाली (बिटर लूफ़ा) माना गया है। "
                   "दूसरी पंक्ति विशेष प्रयोग बताती है: ज्वर, श्वास यानी दमा, हिक्का यानी हिचकी आदि में जीमूत। "
                   "‘जीमूत’ को ‘जीमूतक’ का छोटा रूप माना गया है; दूसरी पंक्ति में क्रिया नहीं है।"),
    "hook": "मैनफल की ही विधि से जीमूतक; ज्वर, दमा, हिचकी में खास।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "In which conditions does verse 31 say jīmūta is used especially?",
            ("Fever, śvāsa, hiccup and the like", "ज्वर-श्वास-हिक्का-आदिषु = in fever, breathlessness, hiccup and the like."),
            [("Cough, poison and vomiting", "These belong to ikṣvāku in line 05.01.43, not to jīmūta."),
             ("Wasting, anaemia and cough", "These are named for surā in line 05.01.36."),
             ("Gulma, abscess and coryza", "These are named in line 05.01.13.")],
            "जीमूत is especially for fever, śvāsa and hiccup and the like.",
            "ज्वर · श्वास · हिक्का."),
        order(1, "Put the conditions of verse 31 in the order of the text.",
              ["ज्वर", "श्वास", "हिक्का"],
              "Fever, breathlessness, hiccup: ज्वरश्वासहिक्कादिषु.",
              "ज्वर · श्वास · हिक्का (· आदि)."),
        match(2, "Match each word of verse 31 to its meaning.",
              [["ज्वर", "fever"], ["श्वास", "breathlessness, asthma"], ["हिक्का", "hiccup"], ["विशेषतः", "especially"]],
              "Three conditions and the word that marks them as the special use.",
              "ज्वर = fever; श्वास = breathlessness; हिक्का = hiccup; विशेषतः = especially.",
              role="extend",
              teaches="ज्वर = fever, श्वास = breathlessness (asthma), हिक्का = hiccup: jīmūta is used especially in these."),
        mcq("discriminate", 3, "Which is the right split of जीमूतकादीनपि?",
            ("जीमूतक + आदीन् + अपि", "अ + आ → आ; final न् joins the vowel of अपि in writing."),
            [("जीमूतक + आदि + नपि", "There is no word नपि; the न् ends आदीन् (acc. pl.)."),
             ("जीमूतकः + आदीन् + अपि", "अः + आ would give अ आ with a gap, not आ."),
             ("जीमूतके + आदीन् + अपि", "ए + आ would give अया (जीमूतकयादीन्).")],
            "जीमूतक-आदीन् (jīmūtaka and the rest, acc. pl.) + अपि (also).",
            "अ + आ → आ; न् + vowel written together."),
        mcq("apply", 4, "How does verse 31 tell the physician to prepare jīmūtaka?",
            ("In the same way as the fruit", "एवं च … कल्पयेत् = and in this way one should prepare."),
            [("Only as a fresh juice", "No juice is named; एवम् points to the earlier procedures."),
             ("Only burnt to ash first", "No burning is named in this verse."),
             ("By a new list given here", "No list follows; एवम् refers back.")],
            "एवम् (in this way) points back to the madana procedures just closed.",
            "एवं कल्पयेत् = prepare in the same way."),
        mcq("transfer", 5, "ज्वरश्वासहिक्कादिषु means in fever, śvāsa, hiccup and the like. What does a new word कासादिषु mean?",
            ("In cough and the like", "कास + आदिषु: X-आदिषु = in X and the like."),
            [("In cough alone", "-आदि adds 'and the like'; 'alone' would be केवल."),
             ("From cough and the rest", "'From' needs the ablative (कासादिभ्यः)."),
             ("Of cough and the rest", "'Of' needs the genitive (कासादीनाम्).")],
            "-आदिषु is the locative plural of -आदि: in X and the like.",
            "X-आदिषु = in X and the like.",
            teaches="X-आदिषु (locative plural) means 'in X and the like': ज्वरश्वासहिक्कादिषु, कासादिषु."),
    ],
}

# ---------------------------------------------------------------- unit 32
AUTHORED["32"] = {
    "title": "तत्र पुष्पेषु क्षीरम्",
    "question": "Which liquid does unit 32 pair with the flowers and with each kind of fruit?",
    "rule": ("There: in flowers, milk; in fruits, a thin gruel (peyā) and the film on milk (santānikā) by their kind; "
             "in the hairless ones, curd or the upper part of curd."),
    "limits": ("Low confidence. No verb. Which fruits take peyā or santānikā is unclear (Hindi and English parse it "
               "differently); no question pairs them, nor rests on the flagged लोमलोमवत्सु, निर्लोमसु. Jīmūtaka's parts, by text order."),
    "explain_hi": ("यह इकाई बताती है कि (सम्भवतः जीमूतक के) किस भाग के साथ कौन-सा द्रव पड़ता है। "
                   "पुष्पों के साथ दूध। "
                   "फलों के साथ पेया यानी पतली लपसी और सन्तानिका यानी दूध पर जमी मलाई; कौन-से फल किसके साथ, यह छपे पाठ से साफ़ नहीं। "
                   "रोम-रहित फलों के साथ दही या दही का ऊपरी भाग। "
                   "इकाई में क्रिया नहीं है।"),
    "hook": "फूल को दूध, फल को पेया या मलाई, चिकने फल को दही।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "Which liquid does unit 32 pair with the flowers?",
            ("Milk (क्षीर)", "पुष्पेषु क्षीरम् = in the flowers, milk."),
            [("Curd (दधि)", "Curd goes with the hairless fruits, not the flowers."),
             ("Gruel (पेया)", "Peyā goes with fruits, not the flowers."),
             ("Honey (मधु)", "Honey is not named in this unit.")],
            "The unit opens: पुष्पेषु क्षीरम्, in the flowers, milk.",
            "पुष्पेषु क्षीरम् = flowers → milk."),
        order(1, "Put the liquids of unit 32 in the order of the text.",
              ["क्षीर (दूध)", "पेया", "सन्तानिका", "दधि", "दध्युत्तरक"],
              "Milk, thin gruel, milk-film, curd, upper part of curd.",
              "क्षीरम् · पेयाम् · सन्तानिकाम् · दधि · दध्युत्तरकम्."),
        match(2, "Match each liquid of unit 32 to its meaning.",
              [["क्षीर", "milk"], ["पेया", "thin gruel"], ["सन्तानिका", "film on milk"], ["दध्युत्तरक", "upper part of curd"]],
              "Four of the five liquids, as the card renders them.",
              "क्षीर = milk; पेया = thin gruel; सन्तानिका = milk-film; दध्युत्तरक = upper part of curd.",
              role="extend",
              teaches="In unit 32, पेया = thin gruel, सन्तानिका = the film on milk, दध्युत्तरक = the upper part of curd."),
        mcq("discriminate", 3, "Which is the right split of दध्युत्तरकम्?",
            ("दधि + उत्तरकम्", "इ + उ → यु: दधि + उत्तरकम् → दध्युत्तरकम्."),
            [("दध्य + उत्तरकम्", "अ + उ would give ओ (दध्योत्तरकम्)."),
             ("दधे + उत्तरकम्", "ए + उ would give अयु (दधयुत्तरकम्)."),
             ("दधः + उत्तरकम्", "अः + उ would give अ उ with a gap.")],
            "दधि (curd) + उत्तरक (upper part): इ before a different vowel becomes य्.",
            "इ + unlike vowel → य् + vowel."),
        mcq("apply", 4, "Which point of unit 32 is clear from the print, by the card?",
            ("Flowers take milk", "पुष्पेषु क्षीरम् is plain; the fruit pairings are the unclear part."),
            [("Hairy fruits take only curd", "Curd is not paired with hairy fruits; this pairing is not stated."),
             ("Flowers take the milk-film", "Santānikā is paired with fruits, not flowers."),
             ("All fruits take plain milk", "Not in this unit: here milk is paired with the flowers, the fruits with other liquids.")],
            "The flower → milk pairing is certain; which fruits take peyā or santānikā is not.",
            "पुष्प → क्षीर (clear); फल → पेया / सन्तानिका (unclear pairing)."),
        mcq("transfer", 5, "पुष्पेषु (n. -अ stem) means in the flowers. Which new form means in the leaves, from पत्र?",
            ("पत्रेषु", "-अ stems take -एषु in the locative plural."),
            [("पत्राणि", "This is nominative/accusative plural: 'leaves'."),
             ("पत्रैः", "This is instrumental plural: 'with leaves'."),
             ("पत्रस्य", "This is genitive singular: 'of a leaf'.")],
            "पुष्प → पुष्पेषु; पत्र → पत्रेषु: locative plural of -अ stems.",
            "Locative plural of -अ stems = -एषु.",
            teaches="The locative plural of -अ stems ends in -एषु: पुष्पेषु (in the flowers), फलेषु, पत्रेषु (in the leaves)."),
    ],
}

# ---------------------------------------------------------------- unit 33
AUTHORED["33"] = {
    "title": "हरितपाण्डुषु क्षीरम्",
    "question": "Which liquids does unit 33 give for the green and pale ones?",
    "rule": "In the green and pale (pāṇḍu) ones: milk or sour curd.",
    "limits": ("No verb, and the noun is unstated: 'ones' are probably the fruits of line 05.01.34. "
               "दध्यम्लम् may be 'sour curd' or 'sourness of curd'; sour curd is chosen. Pāṇḍu: the data says pale-yellow; "
               "the glossary prefers 'pale' (open)."),
    "explain_hi": ("पिछली इकाई की तरह यहाँ भी द्रव बताया गया है, अब हरे और पाण्डु (फीके) रंग वालों के लिए। "
                   "संज्ञा नहीं दी गई; सम्भवतः ये पिछली पंक्ति के फल हैं। "
                   "द्रव: दूध या खट्टा दही। "
                   "‘दध्यम्लम्’ = दधि + अम्लम् (इ + अ → य), जिसे खट्टा दही पढ़ा गया है।"),
    "hook": "हरे और फीके को: दूध या खट्टा दही।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "Which two liquids does unit 33 give as choices?",
            ("Milk or sour curd", "क्षीरं दध्यम्लं वा = milk or sour curd."),
            [("Ghee or oil", "Neither ghee nor oil is named in this unit."),
             ("Honey or water", "Neither is named in this unit."),
             ("Gruel or wine", "Neither is named in this unit.")],
            "For the green and pale ones: milk, or sour curd (वा = or).",
            "क्षीरम् · दध्यम्लम् · वा."),
        match(1, "Match each word of unit 33 to its meaning.",
              [["हरित", "green"], ["पाण्डु", "pale"], ["क्षीर", "milk"], ["अम्ल", "sour"]],
              "Two colours and the two parts of the liquids.",
              "हरित = green; पाण्डु = pale; क्षीर = milk; अम्ल = sour."),
        order(2, "Put the words of unit 33 in the order of the text.",
              ["हरितपाण्डुषु", "क्षीरम्", "दध्यम्लम्", "वा"],
              "In which ones, then the two liquids, then 'or'.",
              "हरितपाण्डुषु · क्षीरं · दध्यम्लं · वा.",
              role="extend",
              teaches="Unit 33 reads हरितपाण्डुषु क्षीरं दध्यम्लं वा: in the green and pale ones, milk or sour curd."),
        mcq("discriminate", 3, "Which is the right split of दध्यम्लम्?",
            ("दधि + अम्लम्", "इ + अ → य: दधि + अम्लम् → दध्यम्लम्."),
            [("दधे + अम्लम्", "ए + अ would give एऽ (दधेऽम्लम्)."),
             ("दधु + अम्लम्", "उ + अ would give व (दध्वम्लम्)."),
             ("दधः + अम्लम्", "अः + अ would give ओऽ (दधोऽम्लम्).")],
            "दधि (curd) + अम्ल (sour): इ before a different vowel becomes य्.",
            "इ + unlike vowel → य् + vowel."),
        mcq("apply", 4, "For which ones does unit 33 give milk or sour curd?",
            ("The green and pale ones", "हरितपाण्डुषु = in the green and pale ones."),
            [("The ripe and dried ones", "Ripe and dried fruits come in line 05.01.37."),
             ("The flowers and sprouts", "Flowers take milk in line 05.01.34; sprouts are not named here."),
             ("The fresh and old roots", "Roots are not named in this unit.")],
            "Colour words, green (हरित) and pale (पाण्डु), mark the ones meant.",
            "हरितपाण्डुषु → क्षीरं दध्यम्लं वा."),
        mcq("transfer", 5, "हरितपाण्डुषु is a dvandva in the locative plural. What does a new phrase रक्तश्वेतेषु mean?",
            ("In the red and white ones", "रक्त + श्वेत, dvandva, -एषु: in the red and white ones."),
            [("In the reddish-white one", "-एषु is plural, and a dvandva names both kinds."),
             ("From the red and white", "'From' would need the ablative (-एभ्यः)."),
             ("The red ones are white", "There is no verb 'are'; it is one locative compound.")],
            "Two colour words joined as a dvandva, then the locative plural: in the X and Y ones.",
            "Dvandva + locative plural = in the X and Y ones.",
            teaches="A dvandva of two colours in the locative plural means 'in the X and Y ones': हरितपाण्डुषु, रक्तश्वेतेषु."),
    ],
}

# ---------------------------------------------------------------- unit 34
AUTHORED["34"] = {
    "title": "तत्कषायसंसृष्टां वा सुराम्",
    "question": "Which drink does unit 34 give, and for which conditions?",
    "rule": ("Or one should use surā (grain liquor) mixed with its decoction in Kapha, arocaka (loss of relish), "
             "cough, pāṇḍu disease (anaemia) and yakṣman (consumption)."),
    "limits": ("'Its' (तत्) is not named; by the order of the text it is the jīmūtaka of these lines. "
               "Yakṣman = consumption, including what is now called tuberculosis (data). No amount is given."),
    "explain_hi": ("इस इकाई में एक मदिरा-योग है: सुरा यानी अनाज की मदिरा, ‘उसके’ (सम्भवतः जीमूतक के) काढ़े से मिली हुई। "
                   "क्रिया ‘प्रयुञ्जीत’ है: प्रयोग करे। "
                   "दशाएँ क्रम से: कफ, अरोचक यानी अरुचि, कास यानी खाँसी, पाण्डुरोग यानी रक्ताल्पता, और यक्ष्मन् यानी क्षय, जिसमें आज का तपेदिक भी आता है। "
                   "‘संसृष्ट’ का अर्थ है मिलाया हुआ।"),
    "hook": "काढ़ा मिली सुरा: कफ, अरुचि, खाँसी, पाण्डु, क्षय।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "What is mixed with its decoction in unit 34?",
            ("Surā, a grain liquor", "तत्कषायसंसृष्टां सुराम् = surā mixed with its decoction."),
            [("Milk, freshly drawn", "Milk is not named in this unit."),
             ("Ghee, cooked as before", "Ghee comes in line 05.01.42."),
             ("Curd, made sour", "Sour curd comes in line 05.01.35.")],
            "सुरा (grain liquor) is mixed (संसृष्ट) with its decoction (तत्कषाय).",
            "तत्कषायसंसृष्टा सुरा = surā mixed with its decoction."),
        order(1, "Put the conditions of unit 34 in the order of the text.",
              ["कफ", "अरोचक", "कास", "पाण्डुरोग", "यक्ष्मन्"],
              "Kapha, loss of relish, cough, pāṇḍu disease, consumption.",
              "कफ · अरोचक · कास · पाण्डुरोग · यक्ष्मन्."),
        match(2, "Match each condition of unit 34 to its meaning.",
              [["अरोचक", "loss of relish for food"], ["कास", "cough"], ["पाण्डुरोग", "anaemia"],
               ["यक्ष्मन्", "consumption (incl. tuberculosis)"]],
              "Four of the five conditions, with the modern names the data gives.",
              "अरोचक = loss of relish; कास = cough; पाण्डुरोग = anaemia; यक्ष्मन् = consumption.",
              role="extend",
              teaches="अरोचक = loss of relish, कास = cough, पाण्डुरोग = anaemia, यक्ष्मन् = consumption (includes tuberculosis)."),
        mcq("discriminate", 3, "Which is the right split of कफारोचक-?",
            ("कफ + अरोचक", "अ + अ → आ: कफ + अरोचक → कफारोचक."),
            [("कफ + रोचक", "रोचक (relish) would give कफरोचक, with no आ; the illness is अरोचक."),
             ("कफा + रोचक", "There is no stem कफा; and रोचक is the opposite sense."),
             ("कफः + अरोचक", "अः + अ would give ओऽ (कफोऽरोचक).")],
            "अरोचक = loss of relish (अ- + रोचक); कफ + अरोचक → कफारोचक.",
            "अ + अ → आ."),
        multi("apply", 4, "Which two of these patients fit the surā drink of unit 34?",
              [("One with a lasting cough (कास)", "Right: कास is named."),
               ("One with hiccup (हिक्का)", "Wrong: hiccup is named for jīmūta in line 05.01.33."),
               ("One with pāṇḍu disease, anaemia", "Right: पाण्डुरोग is named."),
               ("One with fever of Pitta and Kapha", "Wrong: that fever is in line 05.01.38.")],
              [0, 2],
              "Unit 34 names Kapha, arocaka, cough, pāṇḍu disease and yakṣman.",
              "कास and पाण्डुरोग are in unit 34's list."),
        mcq("transfer", 5, "तत्कषायसंसृष्टा सुरा is surā mixed with its decoction. What does a new phrase मधुसंसृष्टं पयः mean?",
            ("Milk mixed with honey", "X-संसृष्ट = mixed with X; the head पयः is milk."),
            [("Honey mixed with milk", "The head is पयः (milk); the first member is what is mixed in."),
             ("Milk free of honey", "संसृष्ट means mixed, not free of."),
             ("Honey taken after milk", "No sequence is stated; संसृष्ट is a mixture.")],
            "In X-संसृष्ट the first member names what is mixed into the head noun.",
            "X-संसृष्टम् Y = Y mixed with X.",
            teaches="X-संसृष्ट means 'mixed with X': तत्कषायसंसृष्टा सुरा (surā mixed with its decoction), मधुसंसृष्टं पयः (milk mixed with honey)."),
    ],
}

# ---------------------------------------------------------------- unit 35
AUTHORED["35"] = {
    "title": "पर्यागतानां वा जीर्णानां जीमूतकफलानाम्",
    "question": "Which powder does unit 35 give, from which fruits, and in which condition?",
    "rule": "The powder of the ripe, old or dried fruits of jīmūtaka (bitter luffa, probable), in vātapitta (Vāta and Pitta together).",
    "limits": ("No verb; 'one should use' (prayuñjīta, line 05.01.36) is understood. Jīmūtaka = Luffa echinata, bitter luffa, "
               "Hindi देवदाली (probable); the unit does not say which Luffa. No amount or vehicle is given."),
    "explain_hi": ("यहाँ जीमूतक यानी देवदाली (सम्भावित पहचान: बिटर लूफ़ा) के फलों का चूर्ण है। "
                   "फल तीन दशाओं में से किसी में हो सकते हैं: पर्यागत यानी पूरे पके, जीर्ण यानी पुराने, या शुष्क यानी सूखे। "
                   "दशा: वातपित्त, यानी वात और पित्त साथ में। "
                   "क्रिया नहीं दी गई; पिछली पंक्ति का ‘प्रयुञ्जीत’ (प्रयोग करे) समझा जाता है।"),
    "hook": "पका, पुराना या सूखा जीमूतक-फल पीसो: वात-पित्त में।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "In which condition does unit 35 give the jīmūtaka-fruit powder?",
            ("In vātapitta", "वातपित्ते = in Vāta and Pitta together."),
            [("In Kapha alone", "Kapha is not named in this unit."),
             ("In pitta-born fever", "Pitta-born is line 05.01.39 (Pitta-Kapha fever line 05.01.38); here it is vātapitta."),
             ("In hiccup and fever", "These are named in line 05.01.33.")],
            "The unit ends with वातपित्ते: the joint Vāta-Pitta condition.",
            "वातपित्ते = in Vāta and Pitta together."),
        match(1, "Match each word of unit 35 to its meaning.",
              [["पर्यागत", "fully ripe"], ["जीर्ण", "old"], ["शुष्क", "dried"], ["चूर्ण", "powder"]],
              "Three states of the fruit and the form it is given in.",
              "पर्यागत = fully ripe; जीर्ण = old; शुष्क = dried; चूर्ण = powder."),
        order(2, "Put these words of unit 35 in the order of the text.",
              ["पर्यागतानाम्", "जीर्णानाम्", "जीमूतकफलानाम्", "शुष्काणाम्", "चूर्णम्", "वातपित्ते"],
              "Ripe, old, (of) jīmūtaka fruits, dried, powder, in vātapitta.",
              "पर्यागतानां वा · जीर्णानां · जीमूतकफलानां · शुष्काणां वा · चूर्णं · वातपित्ते.",
              role="extend",
              teaches="Unit 35: powder of ripe (पर्यागत), old (जीर्ण) or dried (शुष्क) jīmūtaka fruits, in vātapitta."),
        multi("discriminate", 3, "Which two states of the jīmūtaka fruit does unit 35 name?",
              [("Old (जीर्ण)", "Right: जीर्णानाम् is named."),
               ("Unripe (शलाटु)", "Wrong: unripe fruits are named for madana in line 05.01.30."),
               ("Dried (शुष्क)", "Right: शुष्काणाम् is named."),
               ("Roasted (भृष्ट)", "Wrong: roasting is not named in this unit.")],
              [0, 2],
              "The unit names ripe, old and dried fruits; unripe and roasted are not among them.",
              "पर्यागत · जीर्ण · शुष्क."),
        mcq("apply", 4, "What is the probable identification of jīmūtaka on this card?",
            ("Bitter luffa, Luffa echinata", "The data gives Luffa echinata (bitter luffa, Hindi देवदाली) as probable."),
            [("Golden shower, Cassia fistula", "That is āragvadha, in line 05.01.38."),
             ("Pointed gourd, Trichosanthes", "That is paṭolī, in line 05.01.38."),
             ("Wild asparagus, A. racemosus", "That is śatāvarī, in line 05.01.41.")],
            "Jīmūtaka = Luffa echinata, bitter luffa (probable).",
            "जीमूतक = देवदाली, bitter luffa (probable)."),
        mcq("transfer", 5, "वातपित्ते means in Vāta and Pitta together. What does a new word वातकफे mean?",
            ("In Vāta and Kapha together", "वात + कफ, dvandva, locative singular: in the joint Vāta-Kapha state."),
            [("In Vāta caused by Kapha", "A dvandva joins both equally; no cause is stated."),
             ("In Vāta without Kapha", "'Without' would need a word like विना."),
             ("From Vāta and Kapha", "'From' would need the ablative (वातकफात्).")],
            "A dvandva of two doṣas in the locative singular names the joint state: in X and Y together.",
            "X-Y-e (dvandva, loc. sg.) = in X and Y together.",
            teaches="A dvandva of two doṣas in the locative singular names their joint state: वातपित्ते, वातकफे."),
    ],
}

# ---------------------------------------------------------------- unit 36
AUTHORED["36"] = {
    "title": "द्वित्राणि वा सम्पोथ्य",
    "question": "How does unit 36 prepare two or three (fruits), and in which fever is it given?",
    "rule": ("Two or three, crushed, steeped in the decoction of any one of the (fresh or nine) ones beginning with āragvadha, "
             "or of paṭolī, and churned: in fever born of Pitta and Kapha."),
    "limits": ("What is crushed is not named (probably jīmūtaka fruits, line 05.01.37). नवानाम् may be 'fresh' or 'nine' "
               "(open); आसुत (steeped) is unsure; द्वित्राणि is a flagged print form. None of these is questioned. "
               "The āragvadha group is not listed. IDs standard: āragvadha = amaltās; paṭolī = parwal."),
    "explain_hi": ("दो या तीन (सम्भवतः जीमूतक के फल) कूटे जाते हैं (सम्पोथ्य)। "
                   "फिर वे आरग्वध यानी अमलतास आदि में से किसी एक के, या पटोली यानी परवल के काढ़े में भिगोए जाते हैं (आसुत; ठीक भाव अनिश्चित)। "
                   "फिर मथे जाते हैं (मथित्वा)। "
                   "दशा: पित्त और कफ से उत्पन्न ज्वर। "
                   "‘नवानाम्’ का अर्थ ‘ताज़े’ भी हो सकता है और ‘नौ’ भी; यह खुला प्रश्न है।"),
    "hook": "कूटो, अमलतास या परवल के काढ़े में भिगोओ, मथो: पित्त-कफ ज्वर में।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "In which fever does unit 36 give its churned preparation?",
            ("Fever born of Pitta and Kapha", "पित्तश्लेष्मजे ज्वरे = in fever born of Pitta and phlegm."),
            [("Fever born of Vāta alone", "Vāta is not named in this unit."),
             ("Fever born of Pitta alone", "Pitta-born alone is line 05.01.39; here Kapha joins."),
             ("Fever born of Vāta and Kapha", "That pair is named in line 05.01.40.")],
            "पित्त + श्लेष्म + ज = born of Pitta and phlegm (Kapha).",
            "पित्तश्लेष्मज ज्वर = fever of Pitta and Kapha."),
        order(1, "Put the steps of unit 36 in the order of the text.",
              ["सम्पोथ्य (कूटकर)", "निर्यूहेणासुतानि", "मथित्वा (मथकर)", "पित्तश्लेष्मजे ज्वरे"],
              "Crush, (put) in the decoction (आसुत), churn; then the fever it is for.",
              "सम्पोथ्य → निर्यूहेणासुतानि → मथित्वा → पित्तश्लेष्मजे ज्वरे."),
        match(2, "Match each word of unit 36 to its meaning in the card.",
              [["आरग्वध", "golden shower tree (standard)"], ["पटोली", "pointed gourd (standard)"],
               ["सम्पोथ्य", "having crushed"], ["मथित्वा", "having churned"]],
              "Two sources of the steeping decoction and two steps of the work.",
              "आरग्वध = Cassia fistula (amaltās); पटोली = Trichosanthes dioica (parwal); सम्पोथ्य = crushing; मथित्वा = churning.",
              role="extend",
              teaches="In unit 36 the decoction is of one of the āragvadha (golden shower tree) group, or of paṭolī (pointed gourd)."),
        mcq("discriminate", 3, "Which is the right split of निर्यूहेणासुतानि?",
            ("निर्यूहेण + आसुतानि", "अ + आ → आ: …हेण + आसुतानि → …हेणासुतानि."),
            [("निर्यूहे + नासुतानि", "There is no word नासुत; the ण ends निर्यूहेण (instrumental)."),
             ("निर्यूहेणः + आसुतानि", "There is no form निर्यूहेणः; the instrumental is निर्यूहेण."),
             ("निर्यूहेणे + आसुतानि", "ए + आ would give अया, not आ.")],
            "निर्यूहेण (with the decoction, instr.) + आसुतानि (steeped; sense unsure): अ + आ → आ.",
            "अ + आ → आ."),
        mcq("apply", 4, "The helper has paṭolī but no āragvadha. What does unit 36 allow?",
            ("Use the decoction of paṭolī", "पटोल्या वा निर्यूहेण = or with the decoction of paṭolī."),
            [("Use plain cold water instead", "Plain water is not named in this unit."),
             ("Leave out the decoction", "A decoction is required; paṭolī's is the named alternative."),
             ("Use surā liquor instead", "Surā is named in line 05.01.36, not here.")],
            "वा (or) offers paṭolī's decoction in place of one of the āragvadha group.",
            "आरग्वधादि … पटोल्या वा = āragvadha group, or paṭolī."),
        mcq("transfer", 5, "सम्पोथ्य (with a prefix) ends in -य, मथित्वा (no prefix) in -त्वा. Which new form means having taken out, from उद् + √हृ?",
            ("उद्धृत्य", "With a prefix the absolutive takes -य (here -त्य after a short vowel)."),
            [("उद्धृत्वा", "-त्वा is used without a prefix; with उद् it becomes -य/-त्य."),
             ("उद्धर्तुम्", "This is the infinitive: 'to take out'."),
             ("उद्धृतम्", "This is the past participle: 'taken out'.")],
            "No prefix: -त्वा (मथित्वा); with a prefix: -य (सम्पोथ्य, उद्धृत्य).",
            "Absolutive: -त्वा without prefix, -य with prefix.",
            teaches="The absolutive 'having done' is -त्वा without a prefix (मथित्वा) and -य with one (सम्पोथ्य, उद्धृत्य)."),
    ],
}

# ---------------------------------------------------------------- unit 37
AUTHORED["37"] = {
    "title": "जीमूतकचूर्णं कल्कं वा",
    "question": "With what water does verse 37 give jīmūtaka powder or paste, and in which conditions?",
    "rule": ("Jīmūtaka powder or paste with cold water in what is born of Pitta; the same with warm (water) in what is born "
             "of Vāta and Kapha, or of Kapha."),
    "limits": ("The noun for 'what is born of' is not stated (probably fever, as in line 05.01.38). 'Water' in the second line "
               "is understood from the first. Jīmūtaka = bitter luffa (probable). No amount is given."),
    "explain_hi": ("यह श्लोक एक ही द्रव्य को दो तरह के जल से देता है। "
                   "जीमूतक यानी देवदाली का चूर्ण या कल्क (पिसी लुगदी) ठंडे जल से, पित्त से उत्पन्न (सम्भवतः ज्वर) में। "
                   "वही गरम जल से, वात-कफ से उत्पन्न में या केवल कफ से उत्पन्न में। "
                   "दूसरी पंक्ति में ‘जल’ शब्द नहीं है; वह पहली पंक्ति से समझा जाता है।"),
    "hook": "पित्त को ठंडा पानी, वात-कफ और कफ को गरम पानी: द्रव्य वही जीमूतक।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "With what does verse 37 give jīmūtaka in what is born of Pitta?",
            ("With cold water", "शीतेनाम्बुना पित्तजे = with cold water, in what is born of Pitta."),
            [("With warm water", "Warm water is for Vāta-Kapha and Kapha in the second line."),
             ("With fresh milk", "Milk is not named in this verse."),
             ("With honey", "Honey is not named in this verse.")],
            "Cold water for the Pitta-born; warm for the Vāta-Kapha-born or Kapha-born.",
            "शीत अम्बु → पित्तज."),
        match(1, "Match each word of verse 37 to its meaning.",
              [["कल्क", "paste"], ["शीत", "cold"], ["उष्ण", "warm"], ["अम्बु", "water"]],
              "The two forms of the drug and the two waters: cold for the Pitta-born, warm for the Vāta-Kapha-born or Kapha-born.",
              "कल्क = paste; शीत = cold; उष्ण = warm; अम्बु = water."),
        order(2, "Put these words of verse 37 in the order of the text.",
              ["जीमूतकचूर्णम्", "शीतेनाम्बुना", "पित्तजे", "तदेवोष्णेन", "वातकफजे", "कफजे"],
              "Drug, cold water, Pitta-born; the same with warm, Vāta-Kapha-born, Kapha-born.",
              "जीमूतकचूर्णं (कल्कं वा) · शीतेनाम्बुना · पित्तजे · तदेवोष्णेन · वातकफजे · कफजे वा.",
              role="extend",
              teaches="Verse 37: jīmūtaka powder or paste with cold water in the Pitta-born; the same with warm in the Vāta-Kapha-born or Kapha-born."),
        mcq("discriminate", 3, "Which is the right split of तदेवोष्णेन?",
            ("तत् + एव + उष्णेन", "त् → द् before a vowel; अ + उ → ओ: एव + उष्णेन → एवोष्णेन."),
            [("तत् + एवा + उष्णेन", "There is no word एवा; the particle is एव."),
             ("तद् + एवः + उष्णेन", "अः + उ would give अ उ with a gap, not ओ."),
             ("तत् + एवो + ष्णेन", "There is no word ष्णेन; the word is उष्णेन (with warm).")],
            "तत् (that) + एव (same) + उष्णेन (with warm): त् → द्, अ + उ → ओ.",
            "त् → द् before a vowel; अ + उ → ओ."),
        mcq("apply", 4, "A patient's condition is born of Kapha alone. Which way does verse 37 give jīmūtaka?",
            ("With warm water", "तदेवोष्णेन … कफजे वा = the same with warm (water), or in the Kapha-born."),
            [("With cold water", "Cold water is for what is born of Pitta."),
             ("Not at all", "Kapha-born is named: कफजे वा."),
             ("With surā", "Surā is in line 05.01.36, not here.")],
            "Kapha-born, like Vāta-Kapha-born, takes the warm vehicle.",
            "उष्ण → वातकफज, कफज."),
        mcq("transfer", 5, "पित्तज means born of Pitta (पित्त + ज). What does a new word वातज mean?",
            ("Born of Vāta", "-ज at the end of a compound = born of: वात + ज."),
            [("Removing Vāta", "Removing would be -हर (वातहर)."),
             ("Increasing Vāta", "Increasing would be -वर्धन or -कर."),
             ("Like Vāta", "'Like' would be -वत् (वातवत्).")],
            "-ज = born of; -हर = removing; -वत् = like.",
            "X-ज = born of X.",
            teaches="-ज at the end of a compound means 'born of': पित्तज, कफज, वातज (born of Vāta)."),
    ],
}

# ---------------------------------------------------------------- unit 38
AUTHORED["38"] = {
    "title": "जीवकर्षभकेक्षुशतावरीणाम्",
    "question": "With the juice of which drugs does unit 38 give its preparation in what is born of Pitta?",
    "rule": ("Or with the expressed juice (svarasa) of any one of jīvaka, ṛṣabhaka, ikṣu (sugarcane) and śatāvarī "
             "(wild asparagus), in what is born of Pitta."),
    "limits": ("The unit continues line 05.01.39; the drug given with the juice is not repeated. IDs: ikṣu, śatāvarī standard; "
               "jīvaka and ṛṣabhaka disputed (usually Malaxis orchids, rare, often replaced by substitutes)."),
    "explain_hi": ("यह इकाई पित्त से उत्पन्न दशा के लिए एक और वाहक देती है: स्वरस, यानी ताज़ा निचोड़ा रस। "
                   "रस इन चार में से किसी एक का हो: जीवक, ऋषभक, इक्षु यानी गन्ना, और शतावरी। "
                   "जीवक और ऋषभक की पहचान विवादित है (प्रायः दुर्लभ ऑर्किड, व्यवहार में विकल्प लिए जाते हैं)। "
                   "‘अन्यतमस्य’ का अर्थ है इनमें से किसी एक का।"),
    "hook": "जीवक, ऋषभक, गन्ना, शतावरी: किसी एक का रस, पित्त में।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "What vehicle does unit 38 name for what is born of Pitta?",
            ("Expressed juice of one drug", "स्वरसेन = with the expressed juice, of any one (अन्यतमस्य)."),
            [("Decoction of all four drugs", "Not all four together: अन्यतमस्य = of any one."),
             ("Cold water mixed with honey", "Honey is not named; cold water is line 05.01.39."),
             ("Warm water with rock salt", "Warm water is line 05.01.40; rock salt is not named.")],
            "The juice (स्वरस) of any one of four drugs, in what is born of Pitta.",
            "स्वरस = expressed juice; अन्यतम = any one."),
        order(1, "Put the drugs of unit 38 in the order of the text.",
              ["जीवक", "ऋषभक", "इक्षु", "शतावरी"],
              "Jīvaka, ṛṣabhaka, ikṣu, śatāvarī.",
              "जीवक · ऋषभक · इक्षु · शतावरी."),
        match(2, "Match each drug of unit 38 to its identification in the card.",
              [["इक्षु", "sugarcane (standard)"], ["शतावरी", "wild asparagus (standard)"],
               ["जीवक", "Malaxis orchid (disputed)"]],
              "Two standard identifications and one disputed one, as the data labels them.",
              "इक्षु = sugarcane; शतावरी = Asparagus racemosus; जीवक = Malaxis acuminata (disputed).",
              role="extend",
              teaches="In unit 38, इक्षु = sugarcane and शतावरी = wild asparagus (standard); जीवक and ऋषभक are disputed (Malaxis orchids)."),
        mcq("discriminate", 3, "Which is the right split of ऋषभकेक्षु-?",
            ("ऋषभक + इक्षु", "अ + इ → ए: ऋषभक + इक्षु → ऋषभकेक्षु."),
            [("ऋषभके + क्षु", "There is no word क्षु; the drug is इक्षु."),
             ("ऋषभकः + इक्षु", "अः + इ would give अ इ with a gap, not ए."),
             ("ऋषभकु + इक्षु", "उ + इ would give वि (ऋषभक्विक्षु).")],
            "ऋषभक + इक्षु (sugarcane): अ + इ → ए.",
            "अ + इ → ए."),
        mcq("apply", 4, "A helper has only fresh sugarcane. Can unit 38's vehicle be made?",
            ("Yes, its juice is enough", "अन्यतमस्य = any one of the four; इक्षु is one of them."),
            [("No, all four are needed", "अन्यतमस्य means any one, not all four."),
             ("No, only śatāvarī is allowed", "Śatāvarī is one of four; any one will do."),
             ("Yes, but as a decoction", "The text says स्वरस, the expressed juice.")],
            "Any one (अन्यतम) of jīvaka, ṛṣabhaka, ikṣu, śatāvarī gives the juice.",
            "जीवकर्षभकेक्षुशतावरीणामन्यतमस्य स्वरसेन."),
        mcq("transfer", 5, "Unit 38 uses अन्यतम (one of four); unit 26 uses अन्यतर (nimba or arka). Which fits a new list of five drugs?",
            ("पञ्चानामन्यतमस्य", "अन्यतम picks one of three or more: right for five."),
            [("पञ्चानामन्यतरस्य", "अन्यतर picks one of two only."),
             ("पञ्चानामुभयोः", "उभय means both (of two)."),
             ("पञ्चानां सर्वेषाम्", "सर्व means all, not any one.")],
            "अन्यतर = one of two; अन्यतम = one of many.",
            "अन्यतम for three or more; अन्यतर for two.",
            teaches="अन्यतम picks any one of three or more (जीवकर्षभकेक्षुशतावरीणामन्यतमस्य); अन्यतर picks one of two."),
    ],
}

# ---------------------------------------------------------------- unit 39
AUTHORED["39"] = {
    "title": "अथवा पूर्ववद्धृतं वा सिद्धम्",
    "question": "What further preparation does unit 39 add?",
    "rule": "Or ghee cooked as before (pūrvavat).",
    "limits": ("Which earlier preparation 'as before' means is not stated. The print reads पूर्ववद्धृतं; the data reads it as "
               "पूर्ववत् + घृतम् (ghee; द्ध probably printed for द्घ). A split पूर्ववत् + हृतम् is grammatically possible but "
               "not the data's reading. No drug or dose is named."),
    "explain_hi": ("यह छोटी इकाई एक और विकल्प जोड़ती है: पहले की भाँति सिद्ध किया (पकाया) हुआ घृत। "
                   "‘पूर्ववत्’ का अर्थ है पहले की तरह; कौन-सी पिछली विधि, यह यहाँ नहीं कहा गया। "
                   "‘सिद्ध’ का अर्थ है पकाया हुआ, तैयार। "
                   "छपा रूप ‘पूर्ववद्धृतं’ है; डेटा उसे पूर्ववत् + घृतम् पढ़ता है (सम्भवतः द्घ की जगह द्ध छपा)।"),
    "hook": "पहले जैसा पकाया घी: एक और रास्ता।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "What does unit 39 add as another option?",
            ("Ghee cooked as before", "पूर्ववत् … घृतं सिद्धम् = ghee cooked as before."),
            [("Oil cooked with salt", "Oil and salt are not named in this unit."),
             ("Milk boiled with jīmūtaka", "Milk is not named in this unit."),
             ("Curd churned with water", "Curd is not named in this unit.")],
            "The unit offers ghee, cooked in the earlier way.",
            "घृत = ghee; सिद्ध = cooked; पूर्ववत् = as before."),
        match(1, "Match each word of unit 39 to its meaning.",
              [["अथवा", "or else"], ["पूर्ववत्", "as before"], ["घृत", "ghee"], ["सिद्ध", "cooked"]],
              "The connective, the manner, the substance and its state.",
              "अथवा = or else; पूर्ववत् = as before; घृत = ghee; सिद्ध = cooked."),
        fill(2, "In unit 39, the word for cooked, prepared is ____ (type it in Devanagari or in English letters, e.g. dharma).",
             accepts("सिद्धम्"),
             "सिद्धम् (√सिध्, past participle, n. sg.) = cooked, prepared.",
             "सिद्ध = cooked (in the glossary: siddha = cooked, śṛta = boiled).",
             "सिद्धम् = cooked."),
        mcq("discriminate", 3, "What does unit 39 say about which earlier preparation as before means?",
            ("It does not name it", "पूर्ववत् refers back, but the unit names no earlier preparation."),
            [("It names the madana milk", "No milk or line is named in the unit."),
             ("It names the surā drink", "Surā is not named in this unit."),
             ("It names the lotus method", "The lotus method is not named in this unit.")],
            "The reference of पूर्ववत् is left open by the text.",
            "पूर्ववत् = as before (not specified)."),
        mcq("apply", 4, "Which English rendering of unit 39 has one wrong word?",
            ("Or ghee cooked as later", "Wrong: पूर्ववत् is 'as before', not 'as later'."),
            [("Or ghee cooked as before", "Correct: this is the card's rendering."),
             ("Or else ghee prepared as before", "Correct: सिद्ध can be 'prepared'."),
             ("Or ghee, cooked in the former way", "Correct: पूर्ववत् = in the former way.")],
            "पूर्व = former, earlier; पूर्ववत् = as before.",
            "पूर्ववत् = as before."),
        mcq("transfer", 5, "पूर्ववत् means as before (पूर्व + वत्). What does a new word मातृवत् mean?",
            ("Like a mother", "-वत् = like, in the manner of: मातृ + वत्."),
            [("A mother's own thing", "Possession would need the genitive (मातुः)."),
             ("Before the mother", "'Before' would be पूर्व, not -वत्."),
             ("For the mother", "'For' would need the dative (मात्रे).")],
            "Adverb -वत् = like X: पूर्ववत् (as before), मातृवत् (like a mother).",
            "X-वत् = like X.",
            teaches="The adverb -वत् means 'like, as': पूर्ववत् (as before), मातृवत् (like a mother)."),
    ],
}


NOTES_HI = {
    "26": ("विश्वास: मध्यम। इकाई में क्रिया नहीं; पिछली पंक्तियों की तरह अधूरा वाक्य। ‘हर’ (हरने वाला) छपे पाठ में ही है। "
           "वत्सक = कुटज (पंक्ति 05.01.4 वाला वृक्ष, मानक पहचान)। "
           "सन्धि जाँची: निम्बार्क = निम्ब + अर्क (अ + अ → आ); अन्यतरकषायोपसर्जन = …कषाय + उपसर्जन (अ + उ → ओ); सन्तर्पणोत्थ = सन्तर्पण + उत्थ। "
           "छपे रूप ‘निंब’, ‘संतर्पण’ में अनुस्वार है; ये निम्ब, सन्तर्पण के ही रूप हैं।"),
    "27": ("विश्वास: निम्न। लम्बी और कुछ अस्पष्ट इकाई। मुद्रण-दोष चिह्नित: ‘सायान्हे’ = सायाह्ने (संध्या), ‘बृहत’ = बृहत्, ‘क्रसरा’ = सम्भवतः कृसरा; इन पर प्रश्न नहीं बना। "
           "कमल में रखने की क्रिया पाठ में नहीं है। ‘हरिद्राकृसरा’ एक व्यंजन भी हो सकता है, तब हल्दी की पहचान लागू नहीं। "
           "खुले बिन्दु (05.01.28): अनुवादों में हल्दी और खिचड़ी बिना संकोच के लिखे गए हैं; और ‘उपजिघ्रन्’ का कर्म पाठ में नहीं है। "
           "‘समुचितगन्धसम्पदुत्क्लिष्टकफपित्तः’ एक बहुव्रीहि पढ़ा गया; अलग-अलग गुण भी हो सकते हैं। "
           "सन्धि जाँची: चूर्णेनावचूर्णयेत् = चूर्णेन + अवचूर्णयेत्; पुनरुपचूर्णितमुद्धृत्य = पुनर् + उपचूर्णितम् + उद्धृत्य।"),
    "28": ("विश्वास: मध्यम। ‘प्रावरणपट’ एक समास (ओढ़ने का कपड़ा) भी हो सकता है और दो वस्तुएँ भी; दो पढ़ा गया। "
           "‘एतेन’ पिछली सुगन्ध-विधि (पंक्ति 05.01.28) की ओर संकेत करता है, यह पाठ-क्रम से समझा गया। "
           "छपा ‘गंध’ = गन्ध (अनुस्वार)।"),
    "29": ("विश्वास: उच्च। ‘शलाटु’ = कच्चा फल। ‘एवमेव’ = एवम् + एव। "
           "सन्धि जाँची: फलाभावे = फल + अभावे (अ + अ → आ)। कोई मुद्रण-दोष चिह्नित नहीं।"),
    "30": ("विश्वास: उच्च। समापन-वाक्य। सन्धि: फलविधानमुक्तम् = फलविधानम् + उक्तम् (म् स्वर से जुड़कर लिखा जाता है)। "
           "छपे पाठ में अन्त का ‘मुक्तं’ अनुस्वार से है।"),
    "31": ("विश्वास: मध्यम। पंक्ति 05.01.32 में ‘एवंच’ एक शब्द-सा छपा है (एवं च); बिना सन्धि-परिवर्तन के अलग किया। "
           "पंक्ति 05.01.33 में क्रिया नहीं; ‘जीमूत’ को ‘जीमूतक’ का छोटा रूप माना गया। "
           "सन्धि जाँची: जीमूतकादीनपि = जीमूतक + आदीन् + अपि; विशेषतस्तु = विशेषतः + तु (विसर्ग → स्)।"),
    "32": ("विश्वास: निम्न। क्रिया नहीं। मुद्रण-चिह्न: ‘लोमलोमवत्सु’ में अक्षर दोहराया लगता है (सम्भवतः लोमवत्सु); ‘निर्लोमसु’ के लिए निर्लोमेषु सुझाया गया। "
           "(टिप्पणी: नकारान्त ‘निर्लोमन्’ मानें तो ‘निर्लोमसु’ स्वयं शुद्ध सप्तमी बहुवचन हो सकता है।) इन पर प्रश्न नहीं बना। "
           "दूसरा ‘फलेषु’ और ‘शेषेषु’ अनिश्चित हैं। खुला बिन्दु (05.01.34): हिन्दी दोनों ‘फलेषु’ रखती है, अंग्रेज़ी उन्हें एक कर देती है; पेया और सन्तानिका की जोड़ी पर प्रश्न नहीं बना।"),
    "33": ("विश्वास: मध्यम। क्रिया और संज्ञा दोनों नहीं। ‘दध्यम्लम्’ = दधि + अम्लम् (इ + अ → य); खट्टा दही या दही की खटास, पहला अर्थ लिया। "
           "शब्दावली के अनुसार पाण्डु = फीका (pale), ‘पीला’ नहीं; डेटा की हिन्दी में ‘पीले’ है (रिपोर्ट किया)। "
           "छपा ‘पांडुषु’ = पाण्डुषु।"),
    "34": ("विश्वास: मध्यम। ‘तत्’ (उसका) किसका है, यह नहीं कहा; पाठ-क्रम से जीमूतक। "
           "सन्धि जाँची: कफारोचक = कफ + अरोचक (अ + अ → आ)। छपा ‘प्रयुंजीत’ = प्रयुञ्जीत, ‘पांडु’ = पाण्डु। "
           "यक्ष्मन् = क्षय, जिसमें आज का तपेदिक आता है (डेटा)।"),
    "35": ("विश्वास: मध्यम। क्रिया नहीं; पंक्ति 05.01.36 का ‘प्रयुञ्जीत’ समझा जाता है। "
           "‘पर्यागत’ = पूरी तरह आया हुआ, यानी पका। जीमूतक = Luffa echinata (सम्भावित); कुछ सूचियों में अन्य लूफ़ा भी इस नाम से आते हैं। "
           "‘वातपित्त’ को वात-पित्त की संयुक्त दशा पढ़ा गया।"),
    "36": ("विश्वास: मध्यम। मुद्रण-चिह्न: ‘द्वित्राणि’ के लिए ‘द्वित्रीणि’ सुझाया गया (टिप्पणी: ‘द्वित्र’ अकारान्त विशेषण मानें तो ‘द्वित्राणि’ भी चलता है)। "
           "खुला बिन्दु (05.01.38): ‘नवानाम्’ = ताज़े या नौ, तय नहीं; इस पर प्रश्न नहीं बना। ‘आसुत’ का ठीक भाव अनिश्चित। "
           "क्या कूटा जाए, यह नहीं कहा (सम्भवतः जीमूतक के फल)। "
           "सन्धि जाँची: सम्पोथ्यारग्वधादीनाम् = सम्पोथ्य + आरग्वधादीनाम्; निर्यूहेणासुतानि = निर्यूहेण + आसुतानि।"),
    "37": ("विश्वास: उच्च। पंक्ति 05.01.39: ‘पित्तजे’ की संज्ञा (सम्भवतः ज्वर) नहीं दी। पंक्ति 05.01.40: ‘जल’ पहली पंक्ति से समझा जाता है। "
           "सन्धि जाँची: शीतेनाम्बुना = शीतेन + अम्बुना; तदेवोष्णेन = तत् + एव + उष्णेन (त् → द्, अ + उ → ओ)।"),
    "38": ("विश्वास: उच्च। षष्ठी बहुवचन के बाद षष्ठी एकवचन ‘अन्यतमस्य’ (इनमें से किसी एक का)। "
           "सन्धि जाँची: जीवकर्षभक = जीवक + ऋषभक (अ + ऋ → अर्); ऋषभकेक्षु = ऋषभक + इक्षु (अ + इ → ए); …शतावरीणामन्यतमस्य = …णाम् + अन्यतमस्य। "
           "जीवक, ऋषभक जीवनीय-गण में भी आते हैं (पंक्ति 05.01.61)।"),
    "39": ("विश्वास: उच्च (डेटा)। ‘पूर्ववत्’ किस पिछली विधि की ओर है, यह नहीं कहा। "
           "छपा ‘पूर्ववद्धृतं’ डेटा में पूर्ववत् + घृतम् पढ़ा गया (सम्भवतः द्घ की जगह द्ध छपा); नियम से द्ध त् + ह से भी बन सकता है (पूर्ववत् + हृतम्), "
           "पर डेटा का पाठ घृत है और प्रश्न उसी पर हैं। डेटा में इसका text_flag होना चाहिए (रिपोर्ट किया)।"),
}


AIDS = {
    "26": {
        "chain": {"steps": ["फल-मज्जा का क्वाथ", "वत्सक आदि का प्रतिवाप", "नीम या आक में से एक का काढ़ा मिलाकर",
                            "संतर्पण से उपजे सब कफ-रोग दूर"]},
        "contrast": "अन्यतर = दो में से एक (निम्ब या अर्क) · अन्यतम = कई में से एक।",
        "anchors": "मज्जा = भीतरी गिरी · प्रतिवाप = ऊपर से डाला द्रव्य · उपसर्जन = मिलाया हुआ · संतर्पण = अधिक पोषण · हर = हरने वाला।",
    },
    "27": {
        "chain": {"steps": ["फल के काढ़े में इक्कीस बार भावित", "पराग जैसे महीन चूर्ण से ढका", "कमल में रात भर",
                            "सुबह फिर चूर्ण लगाकर निकाला", "गले तक पीकर सूँघे", "सुख से वमन"]},
        "frame": "किसके लिए: सुकुमार और दवा से चिढ़ने वाला · कैसे: सुगन्ध से कफ-पित्त उभरें · फल: सुख से वमन।",
        "anchors": "एकविंशतिकृत्वः = इक्कीस बार · कुसुमरज = पराग · आकण्ठम् = गले तक · उपजिघ्रन् = सूँघता हुआ · भेषजद्वेषी = दवा से चिढ़ने वाला।",
    },
    "28": {
        "chunks": "एतेन | सर्वमाल्यगन्धप्रावरणपटाः | व्याख्याताः।",
        "anchors": "माल्य = माला · गन्ध = सुगन्धित द्रव्य · प्रावरण = ओढ़ना · पट = कपड़ा · व्याख्यात = समझाया हुआ।",
        "pegs": "मेरा बनाया चित्र: कमल की सुगन्ध की तरह माला, इत्र और कपड़ों में बसी सुगन्ध भी उसी तरह काम में ली जाए।",
    },
    "29": {
        "chunks": "एवमेव च | फलाभावे | मदनपुष्पाणि शलाटूनि च | कल्पयेत्।",
        "sandhi": "अ + अ → आ: फल + अभावे → फलाभावे; म् + स्वर: एवम् + एव → एवमेव।",
        "anchors": "अभाव = न होना · पुष्प = फूल · शलाटु = कच्चा फल · कल्पयेत् = तैयार करे।",
    },
    "30": {
        "chunks": "इति | फलविधानम् | उक्तम्।",
        "anchors": "इति = इस प्रकार · विधान = विधि · उक्त = कहा गया (√वच्)।",
    },
    "31": {
        "chunks": "एवं च जीमूतकादीनपि कल्पयेत् | विशेषतस्तु | ज्वरश्वासहिक्कादिषु जीमूतम्।",
        "frame": "क्या: जीमूतक आदि · कैसे: इसी प्रकार (मैनफल की विधि से) · विशेष रूप से कहाँ: ज्वर, श्वास, हिक्का आदि।",
        "anchors": "श्वास = दमा · हिक्का = हिचकी · विशेषतः = विशेष रूप से · अपि = भी।",
    },
    "32": {
        "diagram": {"groups": [{"label": "द्रव (पाठ-क्रम)", "items": ["क्षीर", "पेया", "सन्तानिका", "दधि", "दध्युत्तरक"]}]},
        "frame": "पुष्प → दूध (स्पष्ट) · फल → पेया / सन्तानिका (जोड़ी अस्पष्ट) · रोम-रहित फल → दही या दही का ऊपरी भाग।",
        "anchors": "पेया = पतली लपसी · सन्तानिका = दूध पर जमी मलाई · दध्युत्तरक = दही का ऊपरी भाग।",
    },
    "33": {
        "chunks": "हरितपाण्डुषु | क्षीरम् | दध्यम्लं वा।",
        "sandhi": "इ + अ → य: दधि + अम्लम् → दध्यम्लम्।",
        "contrast": "यहाँ पाण्डु = फीका रंग · पंक्ति 05.01.36 में पाण्डुरोग = रक्ताल्पता का रोग।",
    },
    "34": {
        "diagram": {"groups": [{"label": "दशाएँ (पाठ-क्रम)", "items": ["कफ", "अरोचक", "कास", "पाण्डुरोग", "यक्ष्मन्"]}]},
        "sandhi": "अ + अ → आ: कफ + अरोचक → कफारोचक।",
        "anchors": "संसृष्ट = मिलाया · सुरा = अनाज की मदिरा · अरोचक = अरुचि · कास = खाँसी · यक्ष्मन् = क्षय · प्रयुञ्जीत = प्रयोग करे।",
    },
    "35": {
        "chunks": "पर्यागतानां वा जीर्णानां | जीमूतकफलानां | शुष्काणां वा | चूर्णं | वातपित्ते।",
        "frame": "क्या: जीमूतक-फल का चूर्ण · कैसे फल: पके, पुराने या सूखे · कब: वात-पित्त में।",
        "anchors": "पर्यागत = पूरा पका · जीर्ण = पुराना · शुष्क = सूखा · चूर्ण = पाउडर।",
    },
    "36": {
        "chain": {"steps": ["दो-तीन को कूटे (सम्पोथ्य)", "आरग्वध आदि में से एक या पटोली के काढ़े में आसुत (भाव अनिश्चित)",
                            "मथे (मथित्वा)", "पित्त-कफ ज्वर में"]},
        "contrast": "उपसर्ग के बिना: मथित्वा (-त्वा) · उपसर्ग के साथ: सम्पोथ्य (-य)।",
        "anchors": "सम्पोथ्य = कूटकर · आसुत = भिगोया (अर्थ अनिश्चित) · मथित्वा = मथकर · आरग्वध = अमलतास · पटोली = परवल।",
    },
    "37": {
        "seesaw": "शीत (ठंडा जल) → पित्तज · उष्ण (गरम जल) → वात-कफज या कफज। द्रव्य वही, जल उलटा।",
        "diagram": {"groups": [{"label": "ठंडा जल", "items": ["पित्तज"]},
                               {"label": "गरम जल", "items": ["वातकफज", "कफज"]}]},
        "sandhi": "त् → द् और अ + उ → ओ: तत् + एव + उष्णेन → तदेवोष्णेन; अ + अ → आ: शीतेन + अम्बुना → शीतेनाम्बुना।",
    },
    "38": {
        "diagram": {"groups": [{"label": "स्वरस: इनमें से किसी एक का (पाठ-क्रम)",
                                "items": ["जीवक", "ऋषभक", "इक्षु", "शतावरी"]}]},
        "sandhi": "अ + ऋ → अर्: जीवक + ऋषभक → जीवकर्षभक; अ + इ → ए: ऋषभक + इक्षु → ऋषभकेक्षु।",
        "anchors": "स्वरस = ताज़ा निचोड़ा रस · इक्षु = गन्ना · शतावरी = शतावरी · अन्यतम = कई में से एक।",
    },
    "39": {
        "chunks": "अथवा | पूर्ववद्धृतं वा | सिद्धम्।",
        "anchors": "अथवा = या फिर · पूर्ववत् = पहले की तरह · घृत = घी · सिद्ध = पकाया हुआ।",
    },
}


IMAGE_SPECS = {
    ("26", "chain"): {
        "file": "ka1-kernel-decoction-26.svg",
        "alt": ("Flowchart of unit 26: decoction of the fruit kernel, with an addition of vatsaka and the rest, mixed with the "
                "decoction of either nimba or arka, removing all kapha ailments arising from satiation"),
        "type": "mermaid",
        "code": ('flowchart TD\n  A["फल-मज्जा का क्वाथ"] --> B["वत्सक आदि का प्रतिवाप"]\n'
                 '  B --> C["नीम या आक में से एक"]\n  C --> D["संतर्पण के कफ-रोग दूर"]\n'),
    },
    ("27", "chain"): {
        "file": "ka1-lotus-fragrance-27.svg",
        "alt": ("Chain of unit 27: fruit-pippalis steeped twenty-one times, dusted with a pollen-fine powder, kept a night in a lotus, "
                "powdered again and taken out in the morning, the patient drinks to the neck and smells, and vomits easily"),
        "type": "chain",
        "title": "इकाई २७: सुगन्ध से वमन",
        "steps": ["इक्कीस बार भावित", "पराग जैसा चूर्ण", "कमल में रात भर", "सुबह फिर चूर्ण, निकाले",
                  "गले तक पीकर सूँघे", "सुख से वमन"],
    },
    ("32", "diagram"): {
        "file": "ka1-part-liquid-32.svg",
        "alt": ("Table of unit 32: flowers take milk; fruits take peya or santanika, the pairing being unclear; hairless fruits "
                "take curd or the upper part of curd"),
        "type": "table",
        "title": "इकाई ३२: भाग और द्रव",
        "heads": ["भाग", "द्रव"],
        "rows": [["पुष्प", "दूध"], ["फल (जोड़ी अस्पष्ट)", "पेया, सन्तानिका"], ["रोम-रहित फल", "दही या ऊपरी भाग"]],
    },
    ("34", "diagram"): {
        "file": "ka1-sura-conditions-34.svg",
        "alt": ("Mind map of unit 34: sura mixed with its decoction, used in kapha, arocaka, kasa, pandu disease and yakshman"),
        "type": "mermaid",
        "code": ("mindmap\n  काढ़ा मिली सुरा\n    कफ\n    अरोचक\n    कास\n    पाण्डुरोग\n    यक्ष्मन्\n"),
    },
    ("36", "chain"): {
        "file": "ka1-crush-churn-36.svg",
        "alt": ("Flowchart of unit 36: two or three crushed, steeped in the decoction of one of the aragvadha group or of patoli, "
                "churned, and given in fever born of pitta and kapha"),
        "type": "mermaid",
        "code": ('flowchart TD\n  A["दो-तीन कूटे"] --> B["आरग्वध आदि में से एक"]\n'
                 '  A --> C["या पटोली का काढ़ा"]\n  B --> D["आसुत करके मथे"]\n  C --> D\n'
                 '  D --> E["पित्त-कफ ज्वर में"]\n'),
    },
    ("37", "seesaw"): {
        "file": "ka1-cold-warm-37.svg",
        "alt": ("Two columns for verse 37: jimutaka powder or paste with cold water in what is born of pitta; with warm water "
                "in what is born of vata and kapha, or of kapha"),
        "type": "split",
        "title": "श्लोक ३७: जीमूतक-चूर्ण या कल्क",
        "cols": [["ठंडा जल", ["पित्तज"]], ["गरम जल", ["वातकफज", "कफज"]]],
    },
    ("38", "diagram"): {
        "file": "ka1-four-juices-38.svg",
        "alt": ("Mind map of unit 38: the expressed juice of any one of jivaka, rishabhaka, ikshu (sugarcane) and shatavari"),
        "type": "mermaid",
        "code": ("mindmap\n  किसी एक का स्वरस\n    जीवक\n    ऋषभक\n    इक्षु यानी गन्ना\n    शतावरी\n"),
    },
}
