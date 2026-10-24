from helpers import mcq, match, order, fill, multi, accepts

AUTHORED = {}

# ---------------------------------------------------------------- unit 79
AUTHORED["79"] = {
    "title": "उदुंबरशलाटूनि",
    "question": "Which drugs does verse 79 list for the ghee that is cooked in the next lines?",
    "rule": ("A list: unripe fruits (śalāṭu) of udumbara (cluster fig); the barks of jambū, āmra (mango) and udumbara; "
             "conch shell, sarjarasa (sal resin), lac and kattṛṇa, with a pala as the portion."),
    "limits": ("No verb: the list appears to run on into 05.06.156 (piṣṭvā ... pacet). The jambū member is flagged "
               "(printed jaṃbyā-, perhaps jaṃbvā-), so jambū (probably jamun) is not asked. Kattṛṇa is a grass, "
               "unidentified (an open point). Whether the pala goes with every item is not stated."),
    "explain_hi": ("यह श्लोक एक औषध-सूची है; इसमें क्रिया नहीं, बनाने की विधि 05.06.156 में आती लगती है। "
                   "पहली पंक्ति: उदुम्बर यानी गूलर (Ficus racemosa, मानक) के शलाटु यानी कच्चे फल, और जम्बू, आम्र यानी आम और उदुम्बर की छालें। "
                   "जम्बू का छपा रूप संदिग्ध है (सम्भवतः जामुन), इसलिए उस पर प्रश्न नहीं। "
                   "दूसरी पंक्ति: शंख, सर्जरस यानी साल का राल, लाक्षा यानी लाख, और कत्तृण नामक घास, जिसकी पहचान अज्ञात है। "
                   "अन्त में ‘पलांशिक’: पल (तौल की इकाई) जिसका अंश हो; यह हर द्रव्य पर लगे या नहीं, पाठ नहीं कहता।"),
    "hook": "गूलर के कच्चे फल, तीन पेड़ों की छाल, फिर शंख, राल, लाख, घास; अन्त में ‘पलांशिक’।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "Which part of the udumbara does line 1 of verse 79 name first?",
            ("Its unripe fruits (śalāṭu)",
             "उदुंबरशलाटूनि: the unripe fruits (śalāṭu) of the udumbara."),
            [("Its young sprouts (pallava)",
              "Sprouts of young udumbara come later, in 05.06.160."),
             ("Its ripe red fruits",
              "शलाटु means unripe fruit, not ripe fruit."),
             ("Its roots dug fresh",
              "No root is named in verse 79.")],
            "शलाटु = unripe fruit; the line opens with those of the udumbara (cluster fig).",
            "उदुम्बर-शलाटूनि = गूलर के कच्चे फल."),
        match(1, "Match each word of verse 79 to its meaning on the card.",
              [["उदुम्बर", "cluster fig"], ["शलाटु", "unripe fruit"], ["त्वच्", "bark"],
               ["शङ्ख", "conch shell"], ["लाक्षा", "lac"]],
              "Line 1 gives the tree parts; line 2 begins with conch shell and ends its items with lac and kattṛṇa.",
              "उदुम्बर = cluster fig; शलाटु = unripe fruit; त्वच् = bark; शङ्ख = conch shell; लाक्षा = lac."),
        order(2, "Put these words of line 2 of verse 79 in the verse's order.",
              ["शंखं", "सर्जरसं", "लाक्षां", "कत्तृणं च", "पलांशिकं"],
              "Conch shell, sal resin, lac, kattṛṇa, and last the measure: with a pala as the portion.",
              "शंखं · सर्जरसं · लाक्षां · कत्तृणं च · पलांशिकं.",
              role="extend",
              teaches="Line 2 of verse 79: conch shell, sarjarasa (sal resin), lac and kattṛṇa, with a pala as the portion."),
        mcq("discriminate", 3, "What is सर्जरस, by the card of verse 79?",
            ("The resin of the sal tree",
             "सर्ज (sal tree) + रस (here resin): sarjarasa, resin of the sal (standard)."),
            [("The bark of the sal tree",
              "The barks of line 1 are of jambū, āmra and udumbara, not sal."),
             ("Lac from the lac insect",
              "Lac is लाक्षा, a separate item in the same line."),
             ("Juice of unripe figs",
              "The unripe figs are the udumbara śalāṭu of line 1.")],
            "सर्जरस = resin (rasa) of the sarja (sal) tree; लाक्षा (lac) is listed next to it.",
            "सर्जरस = साल का राल."),
        multi("apply", 4, "A helper gathers the drugs of verse 79. Which of these does the verse name?",
              [("Conch shell (śaṅkha)", "Right: शंखं."),
               ("Lac (lākṣā)", "Right: लाक्षां."),
               ("Unripe udumbara fruits", "Right: उदुंबरशलाटूनि."),
               ("Dhātakī flowers", "Dhātakī flowers come in 05.06.161, not here."),
               ("Lentil (masūra)", "Masūra comes in 05.06.159 and 05.06.161, not here.")],
              [0, 1, 2],
              "Verse 79 names unripe udumbara fruits, three barks, conch shell, sarjarasa, lac and kattṛṇa.",
              "शलाटु · त्वचः · शंख · सर्जरस · लाक्षा · कत्तृण."),
        mcq("transfer", 5,
            "पलांशिकम् = with a pala as the portion. By that pattern, what does the new word कर्षांशिकम् mean?",
            ("With a karṣa as the portion",
             "कर्ष + अंशिक, like पल + अंशिक: the measure named is the portion."),
            [("Lacking any karṣa at all",
              "अंशिक means 'having a portion', not 'lacking' one."),
             ("Weighing four karṣa together",
              "No number is in the word; only the karṣa as the portion."),
             ("Less than one karṣa in weight",
              "Nothing says 'less'; the karṣa itself is the portion.")],
            "X-अंशिक = having X as the portion; अ + अ → आ joins them.",
            "पल + अंशिकम् → पलांशिकम्.",
            teaches="Verse 79: पलांशिकम् = पल + अंशिकम्, 'with a pala as the portion' (अ + अ → आ)."),
    ],
}

# ---------------------------------------------------------------- unit 80
AUTHORED["80"] = {
    "title": "पिष्ट्वा तैः सर्पिषः प्रस्थं",
    "question": "How is the ghee of verse 80 made, and in which disorders is it drunk?",
    "rule": ("Having ground (the drugs of 05.06.154-155), one should cook with them a prastha of ghee, doubled with milk. "
             "In all atisāras (diarrhoeas) this is to be drunk according to strength."),
    "limits": ("The drugs are those of the list before (it appears to complete 05.06.154-155). 'Doubled with milk' does not "
               "state the ratio exactly; no question uses a number for it. Whose strength (yathābalam) is not said; "
               "the patient's is the natural sense."),
    "explain_hi": ("यह पिछली सूची (05.06.154-155) की विधि पूरी करता लगता है। "
                   "उन द्रव्यों को पीसकर (पिष्ट्वा), उनके साथ घी का एक प्रस्थ पकाया जाए, जो दूध से दुगुना किया गया हो। "
                   "‘दुगुना’ का ठीक अनुपात पाठ नहीं बताता; एक पठन में दूध घी का दुगुना है। "
                   "दूसरी पंक्ति: सब अतिसारों यानी दस्तों में यह घी बल के अनुसार (यथाबलम्) पीना चाहिए। "
                   "किसका बल, यह नहीं कहा; रोगी का बल स्वाभाविक अर्थ है।"),
    "hook": "पीसो, घी का प्रस्थ दूध के साथ पकाओ, और हर दस्त में ताक़त देखकर पिलाओ।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "In which disorders is the ghee to be drunk, by verse 80?",
            ("In all atisāras (diarrhoeas)",
             "अतिसारेषु सर्वेषु: in all atisāras."),
            [("In fevers (jvara) only",
              "Fever is not named in verse 80."),
             ("In heart-pain and cutting",
              "Heart-pain and cutting are other mishaps of this chapter, not named here."),
             ("Only in a mild atisāra",
              "The verse says सर्वेषु, all, not only a mild one.")],
            "अतिसारेषु सर्वेषु = in all diarrhoeas: the locative names where the ghee is used.",
            "सर्व अतिसार → यह घी."),
        order(1, "Put these words of line 1 of verse 80 in the verse's order.",
              ["पिष्ट्वा", "तैः", "सर्पिषः प्रस्थं", "क्षीरद्विगुणितं", "पचेत्"],
              "Having ground, with these, a prastha of ghee, doubled with milk, one should cook.",
              "पिष्ट्वा · तैः · सर्पिषः प्रस्थं · क्षीरद्विगुणितं · पचेत्."),
        match(2, "Match each word of verse 80 to its meaning.",
              [["पिष्ट्वा", "having ground"], ["सर्पिस्", "ghee"], ["प्रस्थ", "a measure"],
               ["क्षीर", "milk"], ["पेय", "to be drunk"], ["यथाबलम्", "according to strength"]],
              "Line 1 gives the making, line 2 the use.",
              "पिष्ट्वा = having ground; सर्पिस् = ghee; प्रस्थ = a measure; क्षीर = milk; पेय = to be drunk; यथाबलम् = according to strength.",
              role="extend",
              teaches="Verse 80: having ground the drugs, cook a prastha of ghee doubled with milk; drink it in all atisāras according to strength."),
        mcq("discriminate", 3, "Which split of पेयमेतद्यथाबलं is right?",
            ("पेयम् + एतत् + यथाबलम्",
             "म् + ए → मे; त् → द् before the voiced य: पेयमेतद्यथाबलम्."),
            [("पेय + मेतत् + यथाबलम्",
              "मेतत् is not a word; the म् belongs to पेयम्."),
             ("पेयम् + एत + द्यथाबलम्",
              "Neither एत nor द्यथाबलम् fits; the pronoun is एतत्."),
             ("पेयमे + तत् + यथाबलम्",
              "पेयमे is not a form; the word is पेयम्.")],
            "पेयम् (to be drunk) + एतत् (this) + यथाबलम् (according to strength).",
            "-त् + य- → -द्य-."),
        mcq("apply", 4, "A physician gives this ghee to a patient. How, by verse 80, is it to be drunk?",
            ("According to strength (yathābalam)",
             "पेयमेतद्यथाबलम्: this is to be drunk according to strength."),
            [("One prastha drunk at once",
              "The prastha is the ghee cooked, not the dose drunk."),
             ("Twice the milk taken daily",
              "Milk goes into the cooking; no daily dose is given."),
             ("A fixed pala every morning",
              "No pala or time of day is named in verse 80.")],
            "यथा-बलम् = according to strength; the verse gives no fixed dose.",
            "यथाबलम् = बल के अनुसार."),
        mcq("transfer", 5,
            "Like पिष्ट्वा (having ground), what does the new form पीत्वा mean?",
            ("Having drunk",
             "-त्वा forms the absolutive: पीत्वा = having drunk (√पा), like पिष्ट्वा from √पिष्."),
            [("To be drunk",
              "'To be drunk' is the gerundive पेय, as in line 2."),
             ("One should drink",
              "'One should drink' would be an optative like पिबेत्."),
             ("He drinks now",
              "That is a present tense, पिबति; -त्वा is not a tense.")],
            "-त्वा = having done (an action finished before the main verb).",
            "√पिष् → पिष्ट्वा; √पा → पीत्वा.",
            teaches="In verse 80 पिष्ट्वा is an absolutive in -त्वा: 'having ground', done before पचेत् (one should cook)."),
    ],
}

# ---------------------------------------------------------------- unit 81
AUTHORED["81"] = {
    "title": "कच्छुराधातकीबिल्व",
    "question": "With which drugs, boiled in what, is the yavāgū (gruel) of verse 81 made?",
    "rule": ("With kacchurā, dhātakī (woodfordia), bilva (bael), samaṅgā and raktamūlin, and with masūra (lentil) "
             "and aśvattha (sacred fig) tips, boiled in water, there should be a yavāgū (gruel)."),
    "limits": ("Kacchurā is disputed and raktamūlin unidentified (open points: not asked). Samaṅgā is disputed (often "
               "Mimosa pudica). 'Masūra-aśvattha-śṛṅga' may also be three items; which items are boiled is not exact. "
               "The text does not say here what the gruel is for."),
    "explain_hi": ("दोनों पंक्तियाँ एक कथन लगती हैं: इन द्रव्यों से, जल में उबालकर, यवागू यानी गाढ़ी लपसी बने। "
                   "पहली पंक्ति: कच्छुरा (पहचान विवादित), धातकी यानी धाय (मानक), बिल्व यानी बेल (मानक), समंगा (विवादित, अक्सर लाजवन्ती), और रक्तमूली (अज्ञात)। "
                   "दूसरी पंक्ति: मसूर (मानक) और अश्वत्थ यानी पीपल (मानक) के शृंग यानी अग्रभाग। "
                   "‘मसूर-अश्वत्थ-शृंग’ को तीन अलग द्रव्य भी पढ़ा जा सकता है। "
                   "यह यवागू किस रोग के लिए है, यह श्लोक स्वयं नहीं कहता।"),
    "hook": "धाय, बेल, मसूर, पीपल की कोंपल: पानी में उबालो, लपसी तैयार।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "What preparation do the drugs of verse 81 make?",
            ("A yavāgū (gruel)",
             "यवागूः स्यात्: there should be a yavāgū (gruel)."),
            [("A ghee with milk",
              "The ghee cooked with milk is in 05.06.156."),
             ("A basti (enema)",
              "No basti is named in verse 81."),
             ("A paste (kalka)",
              "No kalka is named; the items are boiled in water.")],
            "The predicate is यवागूः स्यात्: a gruel should be (made).",
            "यवागू = गाढ़ी लपसी."),
        order(1, "Put these drugs of line 1 of verse 81 in the verse's order.",
              ["कच्छुरा", "धातकी", "बिल्व", "समंगा", "रक्तमूलिभिः"],
              "The compound of line 1 runs kacchurā, dhātakī, bilva, samaṅgā, raktamūlin.",
              "कच्छुरा · धातकी · बिल्व · समंगा · रक्तमूलिभिः."),
        match(2, "Match each word of verse 81 to its meaning on the card.",
              [["धातकी", "woodfordia"], ["बिल्व", "bael"], ["मसूर", "lentil"],
               ["अश्वत्थ", "sacred fig"], ["जल", "water"]],
              "Four drugs with standard names, and the water they are boiled in.",
              "धातकी = woodfordia; बिल्व = bael; मसूर = lentil; अश्वत्थ = sacred fig; जल = water.",
              role="extend",
              teaches="Verse 81: dhātakī, bilva, masūra and aśvattha tips, among others, boiled in water, make a yavāgū."),
        mcq("discriminate", 3, "Which split of स्याज्जले is right?",
            ("स्यात् + जले",
             "त् + ज → ज्ज: स्यात् (there should be) + जले (in water)."),
            [("स्याः + जले",
              "A visarga after आ drops before ज; it gives no ज्ज."),
             ("स्याम् + जले",
              "म् before ज becomes anusvāra or ञ्, not ज्ज."),
             ("स्याद् + ज्जले",
              "ज्जले is not a word; the ज्ज comes from the join.")],
            "स्यात् + जले: final त् takes the form of the following ज.",
            "-त् + ज- → -ज्ज-."),
        mcq("apply", 4, "A cook makes this gruel. In what are the drugs boiled, by verse 81?",
            ("In water (jale)",
             "जले शृतैः: boiled in water."),
            [("In fresh milk (kṣīra)",
              "Milk goes with the ghee of 05.06.156, not the gruel."),
             ("In melted ghee",
              "Ghee is not named in verse 81."),
             ("In sour fruit juice",
              "No sour liquid is named in verse 81.")],
            "जले (locative) = in water; शृतैः = boiled.",
            "जले शृत = जल में उबाले."),
        mcq("transfer", 5,
            "Like स्यात् + जले → स्याज्जले, how do the invented words भवेत् + जलम् join?",
            ("भवेज्जलम्",
             "Same rule: त् + ज → ज्ज."),
            [("भवेद्जलम्",
              "Before ज the त् does not stop at द्; it becomes ज्."),
             ("भवेञ्जलम्",
              "ञ् would come from a nasal, not from त्."),
             ("भवेच्जलम्",
              "च् stands before च or छ; before ज it is ज्.")],
            "Final त् before ज becomes ज्.",
            "-त् + ज- → -ज्ज-.",
            teaches="त् + ज → ज्ज: स्यात् + जले = स्याज्जले in verse 81."),
    ],
}

# ---------------------------------------------------------------- unit 82
AUTHORED["82"] = {
    "title": "बालोदुंबरकट्वंग",
    "question": "With which sprouts, flowers and drugs is the second preparation of verse 82 made?",
    "rule": ("With the sprouts (pallava) of young udumbara, kaṭvaṅga, samaṅgā and plakṣa, and with masūra, dhātakī "
             "flowers and balā (country mallow), it should be likewise."),
    "limits": ("'It' is not named: it appears to be the yavāgū of 05.06.159. Whether 'young' goes only with udumbara is "
               "not clear. Kaṭvaṅga is disputed (often Oroxylum indicum), plakṣa probable (Ficus virens): not asked. "
               "Masūra, dhātakī and samaṅgā recur from 05.06.158-159."),
    "explain_hi": ("यह 05.06.158-159 की यवागू जैसा दूसरा योग लगता है; ‘तथा भवेत्’ यानी उसी प्रकार हो। "
                   "पहली पंक्ति: कोमल उदुम्बर यानी गूलर, कट्वंग (विवादित, अक्सर सोनापाठा), समंगा और प्लक्ष (सम्भवतः पाकड़) के पल्लव यानी कोंपलें। "
                   "दूसरी पंक्ति: मसूर, धातकी यानी धाय के फूल, और बला यानी खरैटी (मानक)। "
                   "मसूर, धातकी और समंगा पिछले श्लोक (05.06.158-159) में भी थे। "
                   "‘बाल’ (कोमल) केवल गूलर पर लगे या सब पर, यह स्पष्ट नहीं।"),
    "hook": "कोंपलें चार पौधों की, फूल धाय के, साथ मसूर और बला: वैसी ही लपसी।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "Which part of the plants does line 1 of verse 82 use?",
            ("Their sprouts (pallava)",
             "…प्लक्षपल्लवैः: with the sprouts (pallava)."),
            [("Their barks (tvac)",
              "Barks are in the list of 05.06.154."),
             ("Their unripe fruits",
              "Unripe udumbara fruits are in 05.06.154."),
             ("Their roots",
              "No root is named in verse 82.")],
            "पल्लव closes the compound of line 1: sprouts.",
            "पल्लव = कोंपल."),
        order(1, "Put these members of the line 1 compound of verse 82 in the verse's order.",
              ["उदुम्बर", "कट्वङ्ग", "समङ्गा", "प्लक्ष", "पल्लवैः"],
              "बाल-उदुम्बर-कट्वङ्ग-समङ्गा-प्लक्ष-पल्लवैः: the four plants, then the sprouts.",
              "उदुम्बर · कट्वङ्ग · समङ्गा · प्लक्ष · पल्लवैः."),
        match(2, "Match each word of verse 82 to its meaning.",
              [["बाल", "young"], ["पल्लव", "sprout"], ["पुष्प", "flower"],
               ["बला", "country mallow"], ["तथा", "likewise"]],
              "बाल and पल्लव from line 1; पुष्प, बला and तथा from line 2.",
              "बाल = young; पल्लव = sprout; पुष्प = flower; बला = country mallow; तथा = likewise.",
              role="extend",
              teaches="Verse 82: sprouts of young udumbara and others, with masūra, dhātakī flowers and balā: it should be likewise."),
        mcq("discriminate", 3, "Which split of बालोदुंबर is right?",
            ("बाल + उदुम्बर",
             "अ + उ → ओ: बाल + उदुम्बर → बालोदुम्बर."),
            [("बालः + उदुम्बर",
              "Inside a compound there is no visarga; and -अः before उ would not give ओ."),
             ("बाल + ओदुम्बर",
              "अ + ओ gives औ, so this would print बालौदुम्बर."),
             ("बालि + उदुम्बर",
              "इ + उ gives यु, so this would print बाल्युदुम्बर.")],
            "बाल (young) + उदुम्बर (cluster fig): अ and उ merge into ओ.",
            "अ + उ → ओ."),
        multi("apply", 4, "Which items of verse 82 were already named in verse 81?",
              [("Masūra (lentil)", "Right: masūra is in 05.06.159 too."),
               ("Dhātakī", "Right: dhātakī is in 05.06.158 too."),
               ("Samaṅgā", "Right: samaṅgā is in 05.06.158 too."),
               ("Plakṣa", "Plakṣa is new in verse 82."),
               ("Balā (country mallow)", "Balā is new in verse 82.")],
              [0, 1, 2],
              "The card: masūra, dhātakī and samaṅgā recur from 05.06.158-159.",
              "दोहराए: मसूर · धातकी · समंगा."),
        mcq("transfer", 5,
            "बलाभिः is the instrumental plural of the feminine बला. What is the instrumental plural of the new feminine word लता?",
            ("लताभिः",
             "Feminine -आ stems: -आभिः in the instrumental plural, like बलाभिः."),
            [("लतैः",
              "-ऐः is the instrumental plural of -अ stems (masculine or neuter)."),
             ("लताभ्यः",
              "-आभ्यः is the dative or ablative plural."),
             ("लतायाः",
              "-आयाः is the genitive or ablative singular.")],
            "Feminine -आ + -भिः → -आभिः (with ...).",
            "बला → बलाभिः; लता → लताभिः.",
            teaches="बलाभिः in verse 82 = 'with balā': feminine -आ stems take -आभिः in the instrumental plural."),
    ],
}

# ---------------------------------------------------------------- unit 83
AUTHORED["83"] = {
    "title": "नानाप्रकारा जायंते",
    "question": "What gives rise to the many basti mishaps, and how are they to be treated?",
    "rule": ("Mishaps (vyāpad) of various kinds arise from an error (vibhrama) in the basti. One should carry out their "
             "treatment (sādhana) according to the path and according to the condition."),
    "limits": ("'Yathāpatham' (according to the path) is obscure: the course of the mishap, or perhaps a misreading of "
               "yathāpathyam; it is an open point and is not asked. The verse names no single mishap or remedy here."),
    "explain_hi": ("अध्याय फिर अपने विषय पर लौटता है: बस्ति की व्यापदें यानी दुर्घटनाएँ। "
                   "बस्ति में विभ्रम यानी भूल से अनेक प्रकार की व्यापदें उत्पन्न होती हैं। "
                   "उनका साधन यानी उपचार ‘यथापथम्’ और ‘यथावस्थम्’ करना चाहिए: मार्ग के अनुसार और अवस्था के अनुसार। "
                   "‘यथापथम्’ का अर्थ अस्पष्ट है (व्यापद का मार्ग, या ‘यथापथ्यम्’ का बिगड़ा रूप); इस पर प्रश्न नहीं। "
                   "यहाँ कोई एक व्यापद या एक दवा नहीं बताई गई।"),
    "hook": "बस्ति में भूल: तरह-तरह की मुसीबत; इलाज हालत देखकर।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "From what do mishaps of various kinds arise, by verse 83?",
            ("From an error in the basti",
             "बस्तिविभ्रमात्: from an error (vibhrama) in the basti."),
            [("From the patient's old age",
              "Age is not named in verse 83."),
             ("From eating after the meal",
              "No meal is named in verse 83."),
             ("From cold water after it",
              "Water is not named in verse 83.")],
            "बस्ति-विभ्रमात् is ablative: the cause from which the mishaps arise.",
            "बस्ति-विभ्रम → व्यापद्."),
        match(1, "Match each word of verse 83 to its meaning.",
              [["नानाप्रकार", "of various kinds"], ["व्यापद्", "mishap"], ["विभ्रम", "error"],
               ["अवस्था", "condition"], ["साधन", "treatment"]],
              "Line 1 gives the mishaps and their cause; line 2 the treatment.",
              "नानाप्रकार = of various kinds; व्यापद् = mishap; विभ्रम = error; अवस्था = condition; साधन = treatment."),
        order(2, "Put these phrases of verse 83 in the verse's order.",
              ["नानाप्रकारा", "जायंते", "व्यापदो", "बस्तिविभ्रमात्", "तासां कुर्वीत साधनं"],
              "Of various kinds arise mishaps, from an error in the basti; of those one should do the treatment.",
              "नानाप्रकारा · जायंते · व्यापदो · बस्तिविभ्रमात् ‖ … तासां कुर्वीत साधनं.",
              role="extend",
              teaches="Verse 83: mishaps of various kinds arise from an error in the basti; one should carry out their treatment."),
        mcq("discriminate", 3, "Before बस्तिविभ्रमात्, the printed व्यापदो stands for which form?",
            ("व्यापदः",
             "-अः → -ओ before a voiced sound (ब): व्यापदः + बस्ति… → व्यापदो बस्ति…"),
            [("व्यापदा",
              "Final -आ stays -आ before ब; it does not become -ओ."),
             ("व्यापदम्",
              "Final म् before ब becomes anusvāra: व्यापदं."),
             ("व्यापदे",
              "Final -ए stays -ए before a consonant.")],
            "व्यापदः (mishaps, nom. pl.): -अः turns into -ओ before the voiced ब.",
            "-अः + घोष व्यंजन → -ओ."),
        mcq("apply", 4, "A basti has gone wrong and a mishap appears. How should it be treated, by verse 83?",
            ("According to the condition",
             "यथावस्थम्: according to the condition (avasthā)."),
            [("Always by one fixed remedy",
              "The verse ties the treatment to the condition, not one remedy."),
             ("By giving the same basti again",
              "No repeat of the basti is stated."),
             ("It is left without treatment",
              "तासां कुर्वीत साधनम्: their treatment should be done.")],
            "यथा-अवस्थम् = as the condition is; the treatment follows it.",
            "यथावस्थम् = अवस्था के अनुसार."),
        mcq("transfer", 5,
            "Like यथावस्थम् (according to the condition), what does the new word यथाकालम् mean?",
            ("According to the time",
             "यथा + X (adverb) = according to X; काल = time."),
            [("At the wrong time",
              "That would be अकाले; यथा- means 'according to'."),
             ("Before the time",
              "That would be कालात् पूर्वम्; यथा- means 'according to'."),
             ("For all time",
              "That would be सर्वकालम् or सदा.")],
            "यथा-X-म् = according to X (as in यथाबलम्, 05.06.157).",
            "यथा + अवस्थम् → यथावस्थम् (आ + अ → आ).",
            teaches="यथावस्थम् in verse 83 = यथा + अवस्था: 'according to the condition'."),
    ],
}

# ---------------------------------------------------------------- unit 84
AUTHORED["84"] = {
    "title": "इति बस्तिव्यापत्सिद्धिर्नाम",
    "question": "Which chapter does unit 84 close, and what is its number?",
    "rule": ("The colophon: thus the sixth chapter of Kalpasthāna, named Bastivyāpatsiddhi, the success (siddhi) "
             "concerning the mishaps (vyāpad) of basti."),
    "limits": ("A closing formula: no drug or method. The opening line 05.06.1 spells the name with vyāpatti "
               "(Bastivyāpattisiddhi); both words mean mishap. The printed 'nāmaṣaṣṭho' without a space is a print matter."),
    "explain_hi": ("यह छठे अध्याय की पुष्पिका यानी समाप्ति-पंक्ति है। "
                   "नाम ‘बस्तिव्यापत्सिद्धि’: बस्ति की व्यापदों यानी दुर्घटनाओं की सिद्धि यानी उनका सफल उपचार। "
                   "अध्याय के आरम्भ (05.06.1) में यही नाम ‘व्यापत्ति’ शब्द से आया है; अर्थ वही है। "
                   "‘षष्ठः’ बताता है कि यह कल्पस्थान का छठा अध्याय है। "
                   "षष्ठोऽध्यायः = षष्ठः + अध्यायः।"),
    "hook": "इति: बस्ति की भूलों का इलाज, छठा अध्याय पूरा।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "What is the name of the chapter closed by unit 84?",
            ("Bastivyāpatsiddhi",
             "बस्तिव्यापत्सिद्धिर्नाम: named Bastivyāpatsiddhi."),
            [("Bastikalpa",
              "Bastikalpa is the fourth chapter."),
             ("Siddhabastikalpa",
              "Siddhabastikalpa is the fifth chapter."),
             ("Snehavyāpatsiddhi",
              "Snehavyāpatsiddhi is the seventh chapter.")],
            "The colophon names the chapter: the success concerning the mishaps of basti.",
            "बस्ति + व्यापत् + सिद्धि."),
        order(1, "Put the words of unit 84 in the order of the text.",
              ["इति", "बस्तिव्यापत्सिद्धिः", "नाम", "षष्ठः", "अध्यायः"],
              "Thus, Bastivyāpatsiddhi, named, the sixth, chapter.",
              "इति · बस्तिव्यापत्सिद्धिः · नाम · षष्ठः · अध्यायः."),
        match(2, "Match each word of unit 84 to its meaning.",
              [["इति", "thus"], ["व्यापद्", "mishap"], ["सिद्धि", "success"],
               ["षष्ठ", "sixth"], ["अध्याय", "chapter"]],
              "The words of the colophon, with the two members of the chapter's name.",
              "इति = thus; व्यापद् = mishap; सिद्धि = success; षष्ठ = sixth; अध्याय = chapter.",
              role="extend",
              teaches="Unit 84: the sixth chapter, Bastivyāpatsiddhi = success concerning the mishaps (vyāpad) of basti."),
        mcq("discriminate", 3, "Which split of सिद्धिर्नाम is right?",
            ("सिद्धिः + नाम",
             "-इः → -इर् before a voiced sound (न): सिद्धिः + नाम → सिद्धिर्नाम."),
            [("सिद्धिम् + नाम",
              "म् before न becomes anusvāra: सिद्धिं नाम."),
             ("सिद्धी + नाम",
              "Long ई before न stays ई; no र् appears."),
             ("सिद्धि + र्नाम",
              "र्नाम is not a word; the र् comes from the visarga.")],
            "सिद्धिः (success) + नाम (named): a visarga after इ becomes र् before a voiced sound.",
            "-इः + घोष → -इर्."),
        fill(4, "The colophon calls this the ____ (sixth) chapter. Type it in Devanagari or in English letters (e.g. dharma).",
             accepts("षष्ठः", None, "षष्ठ", "shashtha", "shashthah", "sasthah"),
             "षष्ठोऽध्यायः = षष्ठः (sixth) + अध्यायः (chapter).",
             "Unit 84 names the chapter Bastivyāpatsiddhi and calls it the sixth (षष्ठ) chapter.",
             "षष्ठ = sixth.", role="apply"),
        mcq("transfer", 5, "षष्ठः + अध्यायः gives षष्ठोऽध्यायः. How do the new words अष्टमः + अध्यायः join?",
            ("अष्टमोऽध्यायः",
             "Same rule: -अः + अ- → -ओऽ-, the avagraha marking the lost अ."),
            [("अष्टम अध्यायः",
              "That gap is for -अः before a vowel other than अ."),
             ("अष्टमा अध्यायः",
              "-अः does not lengthen to -आ before अ."),
             ("अष्टमेऽध्यायः",
              "ए would belong to a locative अष्टमे, not to अष्टमः.")],
            "-अः before अ: ओ, and ऽ for the swallowed अ.",
            "-अः + अ- → -ओऽ-.",
            teaches="-अः + अ- → -ओऽ-: षष्ठः + अध्यायः = षष्ठोऽध्यायः in unit 84."),
    ],
}


NOTES_HI = {
    "79": ("विश्वास: मध्यम। 05.06.154-155 एक सूची लगती है, क्रिया नहीं; विधि (पिष्ट्वा … पचेत्) 05.06.156 में। "
           "text_flags: छपा ‘जंब्याम्रो…’ में ‘ब्या’ सम्भवतः ‘ब्वा’ (जम्बु + आम्र → जम्ब्वाम्र) का छपाई-दोष; इसलिए जम्बू सदस्य और उसकी सन्धि पर प्रश्न नहीं; "
           "उदुम्बर और ‘त्वचः’ (छालें) स्पष्ट हैं। छालें तीनों पेड़ों की मानी गईं। "
           "खुला अवलोकन (05.06.155): कत्तृण की पहचान (शायद Cymbopogon जैसी सुगन्धित घास) अनिर्णीत; ‘अज्ञात’ रखा, इस पर प्रश्न नहीं। "
           "‘पलांशिकम्’ एकवचन है; हर द्रव्य एक-एक पल है या नहीं, पाठ नहीं कहता; ‘प्रत्येक’ नहीं जोड़ा। पल ग्राम में नहीं बदला। "
           "पहचान: उदुम्बर = गूलर, Ficus racemosa (मानक); आम्र = आम (मानक); जम्बू = सम्भवतः जामुन; शंख, सर्जरस (साल का राल), लाक्षा (लाख) मानक। "
           "संधि जाँची: आम्रोदुंबर = आम्र + उदुम्बर (अ + उ → ओ); पलांशिकं = पल + अंशिकम् (अ + अ → आ); छपे ‘उदुंबर’, ‘शंखं’ में अनुस्वार = वर्ग-नासिक्य।"),
    "80": ("विश्वास: मध्यम। 05.06.154-155 की सूची को पूरा करता लगता है; ‘तैः’ = उन्हीं द्रव्यों से, ‘एतत्’ = यही घी। "
           "‘क्षीरद्विगुणितम्’ = दूध से दुगुना किया हुआ (प्रस्थ से मेल खाता); अनुपात ठीक नहीं बताया, एक पठन में दूध घी का दुगुना; इस संख्या पर प्रश्न नहीं। "
           "‘यथाबलम्’ = बल के अनुसार; किसका बल, अनुक्त (रोगी का स्वाभाविक अर्थ)। प्रस्थ ग्राम में नहीं बदला। "
           "संधि जाँची: पेयमेतद्यथाबलं = पेयम् + एतत् + यथाबलम् (त् → द् सघोष य से पहले); पिष्ट्वा तैः में सन्धि नहीं। कोई text_flag नहीं।"),
    "81": ("विश्वास: मध्यम। 05.06.158-159 एक कथन लगते हैं (विधेय ‘यवागूः स्यात्’)। "
           "खुला अवलोकन (05.06.158): कच्छुरा (दुरालभा जैसा पौधा या कपिकच्छु, विवादित) और रक्तमूली (‘लाल जड़ वाला’ केवल शाब्दिक अनुमान, अज्ञात); इन पर प्रश्न नहीं। "
           "समंगा विवादित (अक्सर Mimosa pudica, लाजवन्ती)। ‘मसूरश्वत्थशृंगैः’ = मसूर + अश्वत्थ-शृंग पढ़ा; तीन अलग द्रव्य (मसूर, अश्वत्थ, शृंग) भी सम्भव; "
           "मसूर + अश्वत्थ से नियमतः ‘मसूराश्वत्थ’ बनता, छपा ह्रस्व ‘र’ है (data में चिह्न नहीं); इस सन्धि पर प्रश्न नहीं। कौन-कौन से द्रव्य उबाले जाएँ, ठीक नहीं कहा। "
           "पहचान: धातकी = धाय, Woodfordia fruticosa; बिल्व = बेल; मसूर = Lens culinaris; अश्वत्थ = पीपल, Ficus religiosa (सब मानक)। "
           "संधि जाँची: स्याज्जले = स्यात् + जले (त् + ज → ज्ज); शृंगैश्च = शृङ्गैः + च (ः → श् च से पहले)। ‘शृत’ = उबाला हुआ।"),
    "82": ("विश्वास: मध्यम। 05.06.160-161 एक कथन लगते हैं; ‘तथा भवेत्’ का कर्ता अनुक्त, सम्भवतः 05.06.159 की यवागू। "
           "‘बाल’ (कोमल) केवल उदुम्बर पर लगे या सब सदस्यों पर, स्पष्ट नहीं; सीधा पठन पहला; इस पर प्रश्न नहीं। "
           "‘मसूरधातकीपुष्पबलाभिः’ = मसूर + धातकी-पुष्प + बला; ‘धातकी के फूल’ सीधा पठन। "
           "पहचान: कट्वंग विवादित (अक्सर Oroxylum indicum, सोनापाठा; कुछ Ailanthus); प्लक्ष सम्भावित (Ficus virens, पाकड़); बला = खरैटी, Sida cordifolia (मानक); इन पहचानों पर प्रश्न नहीं। "
           "संधि जाँची: बालोदुंबर = बाल + उदुम्बर (अ + उ → ओ); समंगाप्लक्ष = समङ्गा + प्लक्ष; बलाभिश्च = बलाभिः + च (ः → श्)। छपे ‘कट्वंग’, ‘समंगा’ = कट्वङ्ग, समङ्गा।"),
    "83": ("विश्वास: मध्यम। अध्याय यहाँ अपने शीर्षक के विषय (बस्ति-व्यापद्) पर लौटता है। ‘विभ्रम’ = भूल, विचलन। "
           "खुला अवलोकन (05.06.163): ‘यथापथम्’ अस्पष्ट: व्यापद का मार्ग, या ‘यथापथ्यम्’ (जो हितकर हो) का गलत पाठ; कोई चिह्न नहीं लगाया गया; इस शब्द पर प्रश्न नहीं। "
           "संधि जाँची: नानाप्रकारा जायंते = नानाप्रकाराः + जायन्ते (-आः सघोष से पहले -आ, नियमित); व्यापदो बस्ति… = व्यापदः + बस्ति… (-अः → -ओ); "
           "यथावस्थं = यथा + अवस्थम् (आ + अ → आ)। ‘कुर्वीत’ आत्मनेपद विधिलिङ्।"),
    "84": ("विश्वास: उच्च। कल्पस्थान के छठे अध्याय की पुष्पिका; अन्त का ‘इति’ समाप्ति-चिह्न। "
           "05.06.1 में नाम ‘बस्तिव्यापत्तिसिद्धि’ (व्यापत्ति), यहाँ ‘बस्तिव्यापत्सिद्धि’ (व्यापद् का समास-रूप व्यापत्); अर्थ एक। "
           "छपा ‘नामषष्ठो’ बिना अन्तर के: छपाई की बात, इस पर प्रश्न नहीं। "
           "संधि जाँची: सिद्धिर्नाम = सिद्धिः + नाम (-इः → -इर् सघोष से पहले); षष्ठोऽध्यायः = षष्ठः + अध्यायः (-अः + अ → -ओऽ)।"),
}


AIDS = {
    "79": {
        "diagram": {"groups": [{"label": "पंक्ति १", "items": ["उदुम्बर के शलाटु (कच्चे फल)", "जम्बू की छाल (फ़्लैग)",
                                                         "आम्र की छाल", "उदुम्बर की छाल"]},
                               {"label": "पंक्ति २", "items": ["शंख", "सर्जरस (साल का राल)", "लाक्षा (लाख)",
                                                         "कत्तृण (अज्ञात घास)", "पलांशिक"]}]},
        "chunks": "उदुंबरशलाटूनि | जंब्याम्रोदुंबरत्वचः (फ़्लैग) ‖ शंखं सर्जरसं लाक्षां | कत्तृणं च पलांशिकं",
        "frame": "कथन 05.06.154-157: यहाँ सूची (154-155) · फिर पीसकर घी पकाना (156) · सब अतिसारों में पीना (157)।",
        "anchors": "उदुम्बर = गूलर · शलाटु = कच्चा फल · त्वच् = छाल · शंख = शंख · सर्जरस = साल का राल · लाक्षा = लाख · पल = तौल।",
    },
    "80": {
        "chain": {"steps": ["सूची के द्रव्य पीसें", "उनके साथ घी का प्रस्थ", "दूध से दुगुना", "पकाएँ",
                            "सब अतिसारों में", "बल के अनुसार पिएँ"]},
        "chunks": "पिष्ट्वा तैः सर्पिषः प्रस्थं | क्षीरद्विगुणितं पचेत् ‖ अतिसारेषु सर्वेषु | पेयमेतद्यथाबलं",
        "sandhi": "त् → द् सघोष य से पहले: पेयम् + एतत् + यथाबलम् → पेयमेतद्यथाबलम्।",
        "anchors": "पिष्ट्वा = पीसकर · सर्पिस् = घी · प्रस्थ = एक मान · क्षीर = दूध · पेय = पीने योग्य · यथाबलम् = बल के अनुसार।",
    },
    "81": {
        "diagram": {"groups": [{"label": "पंक्ति १ (एक समास)", "items": ["कच्छुरा", "धातकी (धाय)", "बिल्व (बेल)",
                                                                    "समंगा", "रक्तमूली"]},
                               {"label": "पंक्ति २", "items": ["मसूर", "अश्वत्थ (पीपल) के शृंग", "= यवागू", "जल में उबले"]}]},
        "chunks": "कच्छुराधातकीबिल्व | समंगारक्तमूलिभिः ‖ मसूरश्वत्थशृंगैश्च | यवागूः स्याज्जले शृतैः",
        "sandhi": "त् + ज → ज्ज: स्यात् + जले → स्याज्जले; ः + च → श्च: शृङ्गैः + च → शृंगैश्च।",
        "anchors": "धातकी = धाय · बिल्व = बेल · मसूर = मसूर · अश्वत्थ = पीपल · शृंग = अग्रभाग · यवागू = गाढ़ी लपसी · शृत = उबाला।",
    },
    "82": {
        "contrast": {"groups": [{"label": "05.06.158-159 (यवागू)", "items": ["कच्छुरा", "धातकी", "बिल्व", "समंगा", "रक्तमूली", "मसूर", "अश्वत्थ-शृंग"]},
                                {"label": "05.06.160-161 (तथा)", "items": ["कोमल उदुम्बर", "कट्वंग", "समंगा", "प्लक्ष", "(इनके पल्लव)", "मसूर", "धातकी-पुष्प", "बला"]}]},
        "chunks": "बालोदुंबरकट्वंग | समंगाप्लक्षपल्लवैः ‖ मसूरधातकीपुष्प | बलाभिश्च तथा भवेत्",
        "sandhi": "अ + उ → ओ: बाल + उदुम्बर → बालोदुम्बर; ः + च → श्च: बलाभिः + च → बलाभिश्च।",
        "anchors": "बाल = कोमल · पल्लव = कोंपल · प्लक्ष = सम्भवतः पाकड़ · पुष्प = फूल · बला = खरैटी · तथा = उसी प्रकार।",
    },
    "83": {
        "chain": {"steps": ["बस्ति में विभ्रम (भूल)", "अनेक प्रकार की व्यापदें", "मार्ग के अनुसार (अस्पष्ट), अवस्था के अनुसार",
                            "उनका साधन (उपचार) करें"]},
        "chunks": "नानाप्रकारा जायंते | व्यापदो बस्तिविभ्रमात् ‖ यथापथं यथावस्थं | तासां कुर्वीत साधनं",
        "sandhi": "-अः → -ओ सघोष से पहले: व्यापदः + बस्ति… → व्यापदो बस्ति…; आ + अ → आ: यथा + अवस्थम् → यथावस्थम्।",
        "anchors": "नानाप्रकार = तरह-तरह के · व्यापद् = दुर्घटना · विभ्रम = भूल · अवस्था = हालत · साधन = उपचार।",
    },
    "84": {
        "frame": "अध्याय ६ का ढाँचा: 05.06.1 आरम्भ (बस्तिव्यापत्तिसिद्धि) · बस्ति की व्यापदें और उपचार · मल, वात, रक्त आदि के संसर्ग में बस्ति के रस · सब अतिसारों में घृत, फिर यवागू · व्यापदों का उपचार अवस्था के अनुसार · यहाँ पुष्पिका।",
        "sandhi": "-इः → -इर् सघोष से पहले: सिद्धिः + नाम → सिद्धिर्नाम; -अः + अ → -ओऽ: षष्ठः + अध्यायः → षष्ठोऽध्यायः।",
        "anchors": "इति = इस प्रकार · व्यापद् = दुर्घटना · सिद्धि = सफल उपचार · षष्ठ = छठा · अध्याय = अध्याय।",
    },
}


IMAGE_SPECS = {
    ("79", "diagram"): {
        "file": "ka6-ghrita-dravya-79.svg",
        "alt": ("Table of verse 79: unripe udumbara fruits, the barks of jambu (flagged), amra and udumbara, conch shell, "
                "sarjarasa (sal resin), lac and kattrina (unidentified grass), with a pala as the portion"),
        "type": "table",
        "title": "श्लोक ७९: घृत के द्रव्य",
        "heads": ["द्रव्य", "पहचान"],
        "rows": [["उदुम्बर के शलाटु", "गूलर के कच्चे फल (मानक)"], ["जम्बू की छाल", "सम्भवतः जामुन (फ़्लैग)"],
                 ["आम्र की छाल", "आम (मानक)"], ["उदुम्बर की छाल", "गूलर (मानक)"], ["शंख", "शंख (मानक)"],
                 ["सर्जरस", "साल का राल (मानक)"], ["लाक्षा", "लाख (मानक)"], ["कत्तृण", "एक घास (अज्ञात)"],
                 ["पलांशिक (मात्रा)", "पल जिसका अंश हो"]],
    },
    ("80", "chain"): {
        "file": "ka6-atisara-ghrita-80.svg",
        "alt": ("Flowchart of verse 80: grind the listed drugs, cook a prastha of ghee with them doubled with milk, "
                "drink it in all atisaras according to strength"),
        "type": "mermaid",
        "code": ('flowchart TD\n  A["सूची के द्रव्य पीसें"] --> B["उनके साथ घी का प्रस्थ"]\n'
                 '  B --> C["दूध से दुगुना, पकाएँ"]\n  C --> D["सब अतिसारों में"]\n'
                 '  D --> E["बल के अनुसार पिएँ"]\n'),
    },
    ("81", "diagram"): {
        "file": "ka6-yavagu-81.svg",
        "alt": ("Mind map of verse 81: the yavagu (gruel) made with kacchura, dhataki, bilva, samanga and raktamulin "
                "(line 1), and masura and ashvattha tips boiled in water (line 2)"),
        "type": "mermaid",
        "code": ('mindmap\n  यवागू\n    पंक्ति १\n      कच्छुरा\n      धातकी\n      बिल्व\n      समंगा\n      रक्तमूली\n'
                 '    पंक्ति २\n      मसूर\n      अश्वत्थ के शृंग\n      जल में उबले\n'),
    },
    ("83", "chain"): {
        "file": "ka6-vyapad-sadhana-83.svg",
        "alt": ("Flowchart of verse 83: an error in the basti gives mishaps of various kinds; their treatment is done "
                "according to the path (unclear) and according to the condition"),
        "type": "mermaid",
        "code": ('flowchart TD\n  A["बस्ति में विभ्रम"] --> B["अनेक प्रकार की व्यापदें"]\n'
                 '  B --> C["मार्ग के अनुसार<br/>(अस्पष्ट)"]\n  B --> D["अवस्था के अनुसार"]\n'
                 '  C --> E["उनका साधन करें"]\n  D --> E\n'),
    },
}
