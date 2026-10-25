from helpers import mcq, match, order, fill, multi, accepts

AUTHORED = {}

# ---------------------------------------------------------------- unit 90
AUTHORED["90"] = {
    "title": "हरीतकीमपि त्रिवृद्विधानेन",
    "question": "How is harītakī to be prepared by verse 90, and which disorders is it said to remove especially?",
    "rule": ("Harītakī too is prepared by the same method as trivṛt. It is described as removing especially grahaṇī, "
             "pāṇḍu (anaemia), śoṣa (wasting), moha (bewilderment) and udara (the belly)."),
    "limits": ("The steps of 'the trivṛt method' are not repeated here. udara is rendered with its plain sense 'belly'; "
               "it may also name a belly disorder. grahaṇī = chronic bowel disorder and pāṇḍu = anaemia are probable "
               "identifications. No dose is given."),
    "explain_hi": ("पिछली पंक्तियों में त्रिवृत् आदि के योग आ चुके हैं; अब हरीतकी यानी हरड़ भी उसी त्रिवृत् की विधि से तैयार करने को कहा गया है। "
                   "‘अपि’ यानी ‘भी’ बताता है कि यह विधि पहले वाले द्रव्य से ली गई है; विधि के चरण यहाँ दोहराए नहीं गए। "
                   "दूसरी पंक्ति हरीतकी का विशेषण है: वह विशेष रूप से ग्रहणी यानी संग्रहणी, पाण्डु यानी रक्ताल्पता, शोष यानी सूखकर क्षीण होना, मोह और उदर को दूर करने वाली है। "
                   "‘अपहाम्’ स्त्रीलिङ्ग द्वितीया है, इसलिए यह ‘हरीतकीम्’ से मेल खाता है।"),
    "hook": "हरड़ भी निशोथ की तरह बनाओ; ग्रहणी, पाण्डु, शोष, मोह, उदर हटाए।",
    "core": True,
    "questions": [
        mcq("pretest", 0,
            "By verse 90, by whose method is harītakī to be prepared?",
            ("By the method of trivṛt", "त्रिवृद्विधानेन = by the method of trivṛt."),
            [("By the method of dantī", "dantī is not named in this verse; the verse says त्रिवृत्."),
             ("By the method of snuhī", "snuhī is not named in this verse; the verse says त्रिवृत्."),
             ("By the method of tilvaka", "tilvaka is not named in this verse; the verse says त्रिवृत्.")],
            "त्रिवृत्-विधान = the method (procedure) of trivṛt; अपि = also.",
            "हरीतकीम् अपि → त्रिवृद्विधानेन उपकल्पयेत्."),
        match(1, "Match each word of verse 90 to its meaning.",
              [["हरीतकी", "chebulic myrobalan"], ["विधान", "method"], ["उपकल्पयेत्", "should prepare"],
               ["विशेषात्", "especially"], ["अपहा", "removing"]],
              "The first line says how harītakī is prepared; the second says what it removes.",
              "हरीतकी = chebulic myrobalan; विधान = method; उपकल्पयेत् = should prepare; विशेषात् = especially; अपहा = removing."),
        order(2, "Put the disorders that verse 90's harītakī removes in the text's order.",
              ["ग्रहणी", "पाण्डु", "शोष", "मोह", "उदर"],
              "grahaṇī, pāṇḍu, śoṣa, moha, udara; the compound ends in -अपहाम्, 'removing'.",
              "ग्रहणी · पाण्डु · शोष · मोह · उदर · (अपहाम्).",
              role="extend",
              teaches="One compound lists five disorders and closes with -अपहा, 'removing' them."),
        mcq("discriminate", 3, "Which split of विधानेनोपकल्पयेत् is right?",
            ("विधानेन + उपकल्पयेत्", "अ + उ → ओ: विधानेन + उपकल्पयेत् → विधानेनोपकल्पयेत्."),
            [("विधानेन + अपकल्पयेत्", "अ + अ would give आ: विधानेनापकल्पयेत्."),
             ("विधानेनो + पकल्पयेत्", "There is no word पकल्पयेत्; the ओ comes from अ + उ."),
             ("विधानेनः + उपकल्पयेत्", "विधानेनः is not a form; the instrumental is विधानेन.")],
            "विधानेन = by the method (inst.); उपकल्पयेत् = should prepare.",
            "अ + उ → ओ."),
        multi("apply", 4, "Which of these does verse 90 say harītakī removes?",
              [("grahaṇī (bowel disorder)", "Right: ग्रहणी is the first member."),
               ("kaṇḍu (itching)", "No: itching is named in line 05.02.165, not in this verse."),
               ("śoṣa (wasting)", "Right: शोष is the third member."),
               ("moha (bewilderment)", "Right: मोह is the fourth member."),
               ("arśas (piles)", "No: piles are named in line 05.02.165, not in this verse.")],
              [0, 2, 3],
              "ग्रहणी, पाण्डु, शोष, मोह, उदर: these five are in verse 90.",
              "ग्रहणी · पाण्डु · शोष · मोह · उदर → अपहाम्."),
        mcq("transfer", 5,
            "Like ...अपहाम् qualifying हरीतकीम् (f. acc.), which form qualifies पथ्याम् (f. acc.) as कफ-अपहा, removing Kapha (invented)?",
            ("कफापहाम्", "Feminine accusative singular, like पथ्याम् and हरीतकीम्."),
            [("कफापहम्", "That is the masculine or neuter form; पथ्या is feminine."),
             ("कफापहः", "That is masculine nominative; पथ्याम् is accusative."),
             ("कफापहे", "That ending is locative or dual; पथ्याम् is singular accusative.")],
            "An adjective takes the gender, case and number of its noun: हरीतकीम् ... अपहाम्, पथ्याम् ... कफापहाम्.",
            "Adjective = noun's gender, case, number.",
            teaches="-अपहा 'removing' agrees with its noun: हरीतकीम् ... अपहाम्, पथ्याम् कफापहाम्."),
    ],
}

# ---------------------------------------------------------------- unit 91
AUTHORED["91"] = {
    "title": "पिबेत्पथ्यां ससिंधूत्थ",
    "question": "With which four drugs is pathyā drunk in verse 91, and with which liquids may harītakī be taken?",
    "rule": ("Pathyā (harītakī) is drunk together with rock salt, viḍaṅga, utpala and dried ginger; harītakī may also be "
             "taken with urine, or with a decoction of vatsaka (kuṭaja) and the rest."),
    "limits": ("utpala is disputed here (the usual meaning is blue lotus or water lily); its identity is left open. The "
               "animal source of the urine is not stated, nor the members of the vatsaka group. Whether the second line is "
               "a separate recipe is not explicit. No dose is given."),
    "explain_hi": ("पथ्या और हरीतकी एक ही द्रव्य, हरड़, के दो नाम हैं। "
                   "पहली पंक्ति में पथ्या को सिन्धूत्थ यानी सेंधा नमक, विडङ्ग यानी वायविडंग, उत्पल (पहचान विवादित) और नागर यानी सोंठ के साथ पीने को कहा है; ‘स-’ यानी ‘के साथ’। "
                   "दूसरी पंक्ति में हरीतकी लेने के दो द्रव बताए गए हैं: मूत्र, अथवा वत्सक यानी कुटज आदि का निर्यूह यानी काढ़ा। "
                   "मूत्र किस पशु का है और वत्सकादि गण में कौन द्रव्य हैं, यह यहाँ नहीं कहा।"),
    "hook": "हरड़ + सेंधा, वायविडंग, उत्पल, सोंठ; या मूत्र, या कुटज का काढ़ा।",
    "core": False,
    "questions": [
        mcq("pretest", 0,
            "In verse 91, what is sindhūttha?",
            ("Rock salt (saindhava)", "सिन्धूत्थ = rock salt, saindhava (standard)."),
            [("Dried ginger (nāgara)", "Dried ginger is नागर, the last drug of the compound."),
             ("A seed (viḍaṅga)", "viḍaṅga, Embelia ribes, is the next member, not sindhūttha."),
             ("Long pepper (pippalī)", "Long pepper is not named in this verse.")],
            "सिन्धूत्थ = 'risen from the Sindhu': rock salt (standard).",
            "सिन्धूत्थ · विडङ्ग · उत्पल · नागर."),
        match(1, "Match each drug word of verse 91 to its meaning on the card.",
              [["सिन्धूत्थ", "rock salt"], ["विडङ्ग", "Embelia ribes"], ["नागर", "dried ginger"],
               ["वत्सक", "kuṭaja"], ["निर्यूह", "decoction"]],
              "Three companions of pathyā from the first line; the vatsaka decoction from the second.",
              "सिन्धूत्थ = rock salt; विडङ्ग = Embelia ribes; नागर = dried ginger; वत्सक = kuṭaja; निर्यूह = decoction."),
        order(2, "Put the drugs drunk with pathyā in verse 91 in the text's order.",
              ["सिन्धूत्थ", "विडङ्ग", "उत्पल", "नागर"],
              "sindhūttha, viḍaṅga, utpala, nāgara: the compound begins with स- 'together with'.",
              "स- · सिन्धूत्थ · विडङ्ग · उत्पल · नागर.",
              role="extend",
              teaches="A compound beginning with स- means 'together with' the drugs it lists."),
        multi("discriminate", 3, "Which drugs does the first line of verse 91 add to pathyā?",
              [("sindhūttha (rock salt)", "Right: the first member of the स- compound."),
               ("viḍaṅga (Embelia ribes)", "Right: the second member."),
               ("vatsaka (kuṭaja)", "No: vatsaka is in the second line, as a decoction to drink it with."),
               ("nāgara (dried ginger)", "Right: the last member."),
               ("guḍa (jaggery)", "No: jaggery is not named in this verse.")],
              [0, 1, 3],
              "ससिन्धूत्थविडङ्गोत्पलनागराम् = with rock salt, viḍaṅga, utpala and dried ginger.",
              "पहली पंक्ति: सिन्धूत्थ · विडङ्ग · उत्पल · नागर; दूसरी: मूत्र · वत्सकादि-निर्यूह."),
        mcq("apply", 4, "Which rendering of मूत्रेण वत्सकादेर्वा निर्यूहेण is right?",
            ("with urine, or a decoction of vatsaka etc.", "मूत्रेण = with urine; वा = or; निर्यूहेण = with a decoction."),
            [("with urine, and a decoction of vatsaka etc.", "वा means 'or', not 'and'."),
             ("with milk, or a decoction of vatsaka etc.", "मूत्र means urine, not milk."),
             ("with urine, or a paste of vatsaka etc.", "निर्यूह is a decoction, not a paste.")],
            "मूत्रेण · वत्सकादेः · वा · निर्यूहेण: two ways, joined by 'or'.",
            "वा = or; निर्यूह = decoction."),
        mcq("transfer", 5,
            "Like ससिन्धूत्थ...नागराम् (together with rock salt and the rest), what does सघृतां पथ्याम् (invented) mean?",
            ("pathyā together with ghee", "स- + घृत = 'with ghee', agreeing with पथ्याम्."),
            [("pathyā without any ghee", "'Without ghee' would be निर्घृताम्; स- means 'with'."),
             ("ghee instead of pathyā", "स- adds a companion; it does not replace the noun."),
             ("pathyā cooked in ghee", "'Cooked in ghee' would need a word like सिद्ध; स- says only 'with'.")],
            "स- at the start of a compound adjective = 'together with'.",
            "स- + X = 'having X with it'.",
            teaches="A स- compound means 'together with': ससिन्धूत्थाम् पथ्याम्, सघृताम् पथ्याम् 'pathyā with ghee'."),
    ],
}

# ---------------------------------------------------------------- unit 92
AUTHORED["92"] = {
    "title": "पथ्यानागरचूर्णं वा",
    "question": "Which powder does verse 92 give, with what is it eaten, and what is drunk after it?",
    "rule": ("Or a powder of pathyā and nāgara (dried ginger), joined with kolinī fruit, is eaten with jaggery; "
             "lukewarm water is drunk afterwards."),
    "limits": ("Low confidence. The printed saṃyuktaṃkolinīphale runs two words together and its ending may be faulty "
               "(text flag): no question on it. kolinī is unidentified. No dose is given."),
    "explain_hi": ("यह हरीतकी वाला एक और विकल्प है (‘वा’ यानी अथवा)। "
                   "पथ्या यानी हरड़ और नागर यानी सोंठ का चूर्ण, कोलिनी के फल के साथ मिलाया हुआ (यह अंश छपाई में अस्पष्ट है), गुड़ के साथ खाया जाता है। "
                   "खाने के बाद (‘अनु’) गुनगुना जल पीना है। "
                   "कोलिनी कौन-सा पौधा है, यह पता नहीं; उस शब्द पर प्रश्न नहीं बना।"),
    "hook": "हरड़-सोंठ का चूर्ण, गुड़ के साथ; ऊपर से गुनगुना पानी।",
    "core": False,
    "questions": [
        mcq("pretest", 0,
            "By verse 92, with what is the powder eaten?",
            ("With jaggery (guḍa)", "गुडेन भक्षयेत् = one should eat it with jaggery."),
            [("With honey (madhu)", "No honey is named in this verse."),
             ("With ghee (ghṛta)", "No ghee is named in this verse."),
             ("With rock salt", "Rock salt belongs to line 05.02.169, not this verse.")],
            "गुड = jaggery; भक्षयेत् = should eat.",
            "चूर्णम् → गुडेन भक्षयेत्."),
        match(1, "Match each word of verse 92 to its meaning.",
              [["पथ्या", "chebulic myrobalan"], ["नागर", "dried ginger"], ["चूर्ण", "powder"],
               ["गुड", "jaggery"], ["कोष्ण", "lukewarm"]],
              "The powder of two drugs, eaten with jaggery, then lukewarm water.",
              "पथ्या = chebulic myrobalan; नागर = dried ginger; चूर्ण = powder; गुड = jaggery; कोष्ण = lukewarm."),
        order(2, "Put the steps of verse 92 in the text's order.",
              ["पथ्यानागरचूर्णम् (the powder)", "गुडेन भक्षयेत् (eat with jaggery)",
               "तोयं कोष्णं च पिबेदनु (then drink lukewarm water)"],
              "The powder is named, eaten with jaggery, and lukewarm water is drunk after.",
              "चूर्णम् · गुडेन भक्षयेत् · तोयं कोष्णं च पिबेदनु.",
              role="extend",
              teaches="अनु 'afterwards' puts the drink of lukewarm water after the eating."),
        mcq("discriminate", 3, "Which split of पिबेदनु is right?",
            ("पिबेत् + अनु", "त् before a vowel becomes द्: पिबेत् + अनु → पिबेदनु."),
            [("पिबेत् + नु", "त् before न becomes न्: that would be पिबेन्नु."),
             ("पिबे + दनु", "There is no word दनु here, and पिबे is not the verb form."),
             ("पिबेः + अनु", "पिबेः + अनु would give पिबेरनु, with र्.")],
            "पिबेत् = should drink; अनु = afterwards.",
            "त् + vowel → द् + vowel."),
        multi("apply", 4, "Which of these does verse 92 state?",
              [("The powder is of pathyā and nāgara", "Right: पथ्यानागरचूर्णम्."),
               ("It is eaten with jaggery", "Right: गुडेन भक्षयेत्."),
               ("Water is drunk before eating", "No: the water is drunk after (अनु)."),
               ("The water drunk is lukewarm", "Right: तोयं कोष्णम्."),
               ("The powder is mixed with honey", "No: no honey is named in this verse.")],
              [0, 1, 3],
              "Powder of pathyā and nāgara; eaten with jaggery; lukewarm water after.",
              "चूर्ण · गुड · कोष्ण तोय (अनु)."),
        mcq("transfer", 5,
            "Like पिबेत् + अनु → पिबेदनु, which is the joined form of भक्षयेत् + अपि (invented)?",
            ("भक्षयेदपि", "त् before a vowel becomes द्: भक्षयेत् + अपि → भक्षयेदपि."),
            [("भक्षयेतपि", "The त् is voiced to द् before a vowel; it does not stay त."),
             ("भक्षयेत्यपि", "No य् is inserted; त् simply becomes द्."),
             ("भक्षयेदापि", "The vowel of अपि stays short.")],
            "पिबेदनु, भक्षयेदपि: final त् becomes द् before a vowel.",
            "त् + vowel → द्.",
            teaches="A final त् becomes द् before a vowel: पिबेत् + अनु → पिबेदनु, भक्षयेत् + अपि → भक्षयेदपि."),
    ],
}

# ---------------------------------------------------------------- unit 93
AUTHORED["93"] = {
    "title": "पथ्यात्रिवृद्भ्यां गुलिकाः",
    "question": "From what are the pills of verse 93 made, of what size are they, and who takes them?",
    "rule": ("Pills are to be made from pathyā and trivṛt, with honey (kṣaudra) and juice; they are of the measure of a "
             "māṣa and dry, and one with yakṣman (a wasting disease) takes them."),
    "limits": ("Text flags: pathyātrivṛddhāṃ has a faulty ending (read as a dual), and lihmāddhṛtadrutāḥ is only "
               "conjectured as 'should lick, melted in ghee': no question on how the pills are taken. kṣaudrarasa may be "
               "one term. yakṣman = tuberculosis is probable. māṣa is not converted."),
    "explain_hi": ("इस श्लोक में पथ्या यानी हरड़ और त्रिवृत् यानी निशोथ से गोलियाँ बनाने को कहा है, जो क्षौद्र यानी शहद और रस से युक्त हों। "
                   "गोलियाँ माष के परिमाण की और सूखी हों; माष एक छोटा माप है। "
                   "इन्हें यक्ष्मी यानी यक्ष्मन् (क्षय रोग, सम्भावित पहचान) से ग्रस्त व्यक्ति लेता है। "
                   "अन्तिम छपा शब्द बिगड़ा है; अनुमान से इसे ‘घी में द्रवित करके चाटे’ पढ़ा गया है, इसलिए उस पर प्रश्न नहीं बना।"),
    "hook": "हरड़ + निशोथ की माष भर सूखी गोलियाँ, शहद-रस के साथ, यक्ष्मा रोगी के लिए।",
    "core": False,
    "questions": [
        mcq("pretest", 0,
            "By verse 93, what size are the pills?",
            ("The measure of a māṣa", "माषप्रमाणाः = of the measure of a māṣa."),
            [("The size of a kola seed", "The kola-seed size belongs to line 05.02.177."),
             ("The measure of a karṣa", "No karṣa is named in this verse."),
             ("The size of a palmful", "No palmful is named in this verse.")],
            "माष = a small measure; प्रमाण = measure, size.",
            "गुलिकाः → माषप्रमाणाः · शुष्काः."),
        match(1, "Match each word of verse 93 to its meaning.",
              [["गुलिका", "pill"], ["कार्य", "to be made"], ["क्षौद्र", "honey"],
               ["शुष्क", "dry"], ["यक्ष्मी", "one with yakṣman"]],
              "Pills to be made, with honey; dry; for one with yakṣman.",
              "गुलिका = pill; कार्य = to be made; क्षौद्र = honey; शुष्क = dry; यक्ष्मी = one with yakṣman."),
        order(2, "Put these words of verse 93 in the text's order.",
              ["गुलिकाः", "कार्याः", "क्षौद्ररसान्विताः", "माषप्रमाणाः", "शुष्काः", "यक्ष्मी"],
              "Pills, to be made, with honey and juice; of māṣa measure, dry; one with yakṣman.",
              "गुलिकाः · कार्याः · क्षौद्ररसान्विताः · माषप्रमाणाः · शुष्काः · यक्ष्मी.",
              role="extend",
              teaches="The pills are described first (made, with honey), then their size and dryness, then who takes them."),
        multi("discriminate", 3, "Which of these does verse 93 state about the pills?",
              [("They are made from pathyā and trivṛt", "Right: पथ्या and त्रिवृत् are the two drugs named."),
               ("They are of the measure of a māṣa", "Right: माषप्रमाणाः."),
               ("They are dry", "Right: शुष्काः."),
               ("They are of the size of a kola seed", "No: that size is in line 05.02.177."),
               ("They are cooked in milk", "No: no milk is named in this verse.")],
              [0, 1, 2],
              "Pathyā and trivṛt pills, with honey and juice, māṣa-sized and dry.",
              "पथ्या + त्रिवृत् → गुलिकाः · माषप्रमाणाः · शुष्काः."),
        mcq("apply", 4, "Which split of माषप्रमाणास्ताः is right?",
            ("माषप्रमाणाः + ताः", "आः before त becomes आस्: माषप्रमाणाः + ताः → माषप्रमाणास्ताः."),
            [("माषप्रमाणः + ताः", "That would give माषप्रमाणस्ताः, with a short अ."),
             ("माषप्रमाणाम् + ताः", "Final म् before त gives ं: माषप्रमाणांताः."),
             ("माषप्रमाणाः + स्ताः", "There is no word स्ताः; the स् comes from the visarga.")],
            "माषप्रमाणाः (of māṣa measure, f. pl.) + ताः (those, f. pl.).",
            "ः + त → स्त."),
        mcq("transfer", 5,
            "Like माषप्रमाणाः + ताः → माषप्रमाणास्ताः, which is the joined form of शुष्काः + तत्र (invented)?",
            ("शुष्कास्तत्र", "ः before त becomes स्: शुष्काः + तत्र → शुष्कास्तत्र."),
            [("शुष्काश्तत्र", "श् comes before च, छ; before त the visarga becomes स्."),
             ("शुष्कातत्र", "The visarga is not dropped before त; it becomes स्."),
             ("शुष्कोस्तत्र", "आः keeps its आ; ओ comes only from अः before voiced sounds.")],
            "माषप्रमाणास्ताः, शुष्कास्तत्र: visarga before त → स्.",
            "ः + त/थ → स्.",
            teaches="Visarga before त becomes स्: माषप्रमाणाः + ताः → माषप्रमाणास्ताः, शुष्काः + तत्र → शुष्कास्तत्र."),
    ],
}

# ---------------------------------------------------------------- unit 94
AUTHORED["94"] = {
    "title": "सर्वत्रेष्टं विरेचनं",
    "question": "Which purgative does verse 94 call desired everywhere, and how are the modaka balls made?",
    "rule": ("Pathyā, trivṛt, kaṭu and hot water make a purgative desired everywhere. When pathyā powder has been "
             "steeped in snuk-milk (the milky sap of snuk, a spurge), one should make balls (modaka) of it."),
    "limits": ("The printed kaṭuṣṇāṃbu can be read as 'kaṭu and hot water', 'pungent hot water', or trikaṭu with a lost "
               "syllable: no question on kaṭu. snuk = Euphorbia neriifolia is probable (other spurges share the name). "
               "No dose or size of the balls is given here; it comes in line 05.02.177."),
    "explain_hi": ("पहली पंक्ति एक सरल विरेचन बताती है: पथ्या यानी हरड़, त्रिवृत् यानी निशोथ, कटु और गरम जल; यह ‘सर्वत्र इष्ट’ यानी हर जगह चाहा गया विरेचन है। "
                   "‘कटुष्णाम्बु’ का अर्थ दो-तीन तरह पढ़ा जा सकता है, इसलिए कटु का ठीक अर्थ खुला रखा गया है। "
                   "दूसरी पंक्ति नया योग आरम्भ करती है: पथ्या का चूर्ण स्नुक् यानी थूहर के क्षीर (पौधे का दूधिया रस) से भावित हो जाने पर उसके मोदक यानी लड्डू जैसी गोलियाँ बनाए। "
                   "मोदकों का माप और उनका सेवन अगली पंक्ति ०५.०२.१७७ में है।"),
    "hook": "हरड़-निशोथ-गरम पानी: हर जगह चलने वाला जुलाब; थूहर-दूध में भिगोया हरड़-चूर्ण: मोदक।",
    "core": True,
    "questions": [
        mcq("pretest", 0,
            "By verse 94, how is the purgative of pathyā, trivṛt and hot water described?",
            ("Desired everywhere", "सर्वत्र इष्टं विरेचनम् = a purgative desired everywhere."),
            [("Only for the strong", "Strength is not mentioned in this verse."),
             ("Only in the rains", "No season is named in this verse."),
             ("Harsh and risky", "The verse calls it desired (इष्ट), not harsh.")],
            "सर्वत्र = everywhere; इष्ट = desired; विरेचन = purgative.",
            "पथ्या · त्रिवृत् · ... उष्णाम्बु → सर्वत्रेष्टं विरेचनम्."),
        match(1, "Match each word of verse 94 to its meaning.",
              [["सर्वत्र", "everywhere"], ["इष्ट", "desired"], ["स्नुक्", "snuk (a spurge)"],
               ["भावित", "steeped, soaked"], ["मोदक", "ball (modaka)"]],
              "The first line praises the purgative; the second line makes balls of steeped pathyā powder.",
              "सर्वत्र = everywhere; इष्ट = desired; स्नुक् = a spurge; भावित = steeped; मोदक = ball."),
        order(2, "Put the words of the second line of verse 94 in the text's order.",
              ["स्नुक्क्षीरभाविते (steeped in snuk-milk)", "पथ्याचूर्णे (in the pathyā powder)", "कुर्वीत (should make)", "मोदकान् (balls)"],
              "When the pathyā powder has been steeped in snuk-milk, one should make balls: the steeping is named first.",
              "स्नुक्क्षीरभाविते · पथ्याचूर्णे · कुर्वीत · मोदकान्.",
              role="extend",
              teaches="A locative phrase (स्नुक्क्षीरभाविते पथ्याचूर्णे) says 'when the powder has been steeped'; the making of balls follows it."),
        mcq("discriminate", 3, "Which split of सर्वत्रेष्टं is right?",
            ("सर्वत्र + इष्टम्", "अ + इ → ए: सर्वत्र + इष्टम् → सर्वत्रेष्टम्."),
            [("सर्वत्र + अष्टम्", "अ + अ would give आ: सर्वत्राष्टम्."),
             ("सर्वत्रे + इष्टम्", "There is no form सर्वत्रे; the adverb is सर्वत्र."),
             ("सर्वत्र + एष्टम्", "There is no word एष्टम्; ए comes from अ + इ.")],
            "सर्वत्र = everywhere; इष्टम् = desired.",
            "अ + इ → ए."),
        mcq("apply", 4, "In verse 94, what is snuk-kṣīra, in which the powder is steeped?",
            ("The milky sap of the snuk spurge", "स्नुक्क्षीर = the milk (milky sap) of snuk, a spurge."),
            [("Cow's milk boiled with snuk", "No cow's milk is named; the 'milk' is the plant's own sap."),
             ("The juice of the pathyā fruit", "pathyā is the powder being steeped, not the liquid."),
             ("Milk mixed with some trivṛt", "trivṛt belongs to the first line's purgative.")],
            "स्नुक् = snuhī, a spurge (probable: Euphorbia neriifolia); क्षीर = its milky sap.",
            "स्नुक्क्षीरभाविते पथ्याचूर्णे → मोदकान् कुर्वीत."),
        mcq("transfer", 5,
            "Like सर्वत्र + इष्टम् → सर्वत्रेष्टम्, which is the joined form of अत्र + इष्टम् (invented)?",
            ("अत्रेष्टम्", "अ + इ → ए: अत्र + इष्टम् → अत्रेष्टम्."),
            [("अत्रिष्टम्", "The अ is not lost; it merges with इ into ए."),
             ("अत्रैष्टम्", "ऐ comes from अ + ए, not from अ + इ."),
             ("अत्रयिष्टम्", "No य् is inserted between अ and इ.")],
            "सर्वत्रेष्टम्, अत्रेष्टम्: अ + इ → ए.",
            "अ/आ + इ/ई → ए.",
            teaches="अ before इ merges into ए: सर्वत्र + इष्टम् → सर्वत्रेष्टम्, अत्र + इष्टम् → अत्रेष्टम्."),
    ],
}

# ---------------------------------------------------------------- unit 95
AUTHORED["95"] = {
    "title": "कोलास्थिमात्राञ् शुष्कांश्च",
    "question": "Of what size are the balls in verse 95, with what are they licked, and for whom?",
    "rule": ("The modaka balls, of the size of a kola (jujube) seed and dry, are given to lick with fresh butter, for one "
             "with gulma, udara, liver, spleen, pain, ānāha and vibandha (constipation)."),
    "limits": ("'modakān' is carried over from line 05.02.176. -vibandhinaḥ may be genitive singular or a plural; it is "
               "read as 'of one with ...', and the sentence may go on into line 05.02.179: no question on its case. kola = "
               "jujube is probable. lehayet is literally 'should make (him) lick'."),
    "explain_hi": ("यह पिछली पंक्ति के मोदकों का सेवन बताता है। "
                   "मोदक कोल यानी बेर की गुठली के माप के और सूखे हों, और उन्हें नवनीत यानी ताज़े मक्खन के साथ चटाया जाए (‘लेहयेत्’ = चटाए)। "
                   "दूसरी पंक्ति बताती है किसके लिए: गुल्म यानी पेट की गाँठ, उदर, यकृत् यानी जिगर, प्लीहा यानी तिल्ली, शूल यानी पीड़ा, आनाह यानी पेट का फूलना और मल-वायु का रुकना, और विबन्ध यानी मलावरोध वाले रोगी के लिए। "
                   "‘-विबन्धिनः’ का विभक्ति-रूप दो तरह पढ़ा जा सकता है।"),
    "hook": "बेर की गुठली भर सूखे मोदक, मक्खन के साथ चटाओ: गुल्म से विबन्ध तक।",
    "core": False,
    "questions": [
        mcq("pretest", 0,
            "By verse 95, with what are the balls given to lick?",
            ("With fresh butter", "नवनीतेन लेहयेत् = should make (him) lick with fresh butter."),
            [("With castor oil (eraṇḍa)", "Castor oil belongs to line 05.02.179, not this verse."),
             ("With jaggery (guḍa)", "Jaggery belongs to line 05.02.172, not this verse."),
             ("With honey and ghee", "Neither honey nor ghee is named in this verse.")],
            "नवनीत = fresh butter; लेहयेत् = should make lick.",
            "मोदकान् → नवनीतेन लेहयेत्."),
        match(1, "Match each word of verse 95 to its meaning on the card.",
              [["कोल", "jujube"], ["अस्थि", "seed, stone"], ["नवनीत", "fresh butter"],
               ["यकृत्", "liver"], ["प्लीहा", "spleen"]],
              "The size (kola seed), the vehicle (butter), and two organs from the list of disorders.",
              "कोल = jujube; अस्थि = seed; नवनीत = fresh butter; यकृत् = liver; प्लीहा = spleen."),
        order(2, "Put the first six members of the second line's compound (verse 95) in order.",
              ["गुल्म", "उदर", "यकृत्", "प्लीह", "शूल", "आनाह"],
              "gulma, udara, yakṛt, plīha, śūla, ānāha; vibandha closes the list.",
              "गुल्म · उदर · यकृत् · प्लीह · शूल · आनाह · (विबन्ध).",
              role="extend",
              teaches="The disorders are listed in one compound ending in -विबन्धिनः, 'one with ... constipation'."),
        mcq("discriminate", 3, "In verse 95, what is ānāha, as the card gives it?",
            ("Belly distension with retention", "आनाह = distension of the abdomen with retention of stool and wind."),
            [("A hard lump in the belly", "A lump in the abdomen is gulma, the first member."),
             ("Pain or colic in the belly", "Pain is śūla, the member before ānāha."),
             ("A swelling of the spleen", "plīha names the spleen, not ānāha.")],
            "आनाह = distension with retention of stool and wind (standard).",
            "गुल्म = lump; शूल = pain; आनाह = distension; विबन्ध = constipation."),
        mcq("apply", 4, "Which split of शुष्कांश्च is right?",
            ("शुष्कान् + च", "न् before च becomes ंश्: शुष्कान् + च → शुष्कांश्च."),
            [("शुष्काः + च", "Visarga before च gives श्: that would be शुष्काश्च."),
             ("शुष्काम् + च", "म् before च gives ं: that would be शुष्कां च."),
             ("शुष्कं + अश्च", "There is no word अश्च, and ं + अ would not give ांश्च.")],
            "शुष्कान् (dry, m. acc. pl., agreeing with the balls) + च (and).",
            "न् + च → ंश्च."),
        mcq("transfer", 5,
            "Like शुष्कान् + च → शुष्कांश्च, which is the joined form of मोदकान् + च (invented)?",
            ("मोदकांश्च", "न् before च becomes ंश्: मोदकान् + च → मोदकांश्च."),
            [("मोदकाश्च", "That is the form from मोदकाः (nominative), not मोदकान्."),
             ("मोदकान्च", "Final न् does not stay unchanged before च."),
             ("मोदकांच", "The श् sibilant is inserted before च: ंश्च.")],
            "शुष्कांश्च, मोदकांश्च: न् + च → ंश्च.",
            "न् + च/छ → ंश्.",
            teaches="Final न् before च becomes anusvara + श्: शुष्कान् + च → शुष्कांश्च, मोदकान् + च → मोदकांश्च."),
    ],
}

# ---------------------------------------------------------------- unit 96
AUTHORED["96"] = {
    "title": "लिह्यादेरंडतैलेन",
    "question": "With what oil and which drugs is the preparation of verse 96 licked, what is drunk after, and how is it called?",
    "rule": ("One should lick it, joined with kuṣṭha (costus root) and trikaṭuka (the three pungents), with eraṇḍa "
             "(castor) oil, and drink pleasant water after; this purgative is easy (sukha)."),
    "limits": ("The thing licked is not named; etat ('this') refers back to it. sukha-udaka is 'pleasant water' "
               "(perhaps comfortably warm, not stated). kuṣṭha here is the drug (costus), not the skin disease. No dose is given."),
    "explain_hi": ("इस श्लोक में एक और विरेचन है: कुष्ठ यानी कूठ और त्रिकटुक (सोंठ, पीपर, काली मिर्च) से युक्त योग को एरण्ड यानी अरंडी के तैल के साथ चाटे। "
                   "किस चीज़ को चाटना है, उसका नाम यहाँ नहीं लिया गया; ‘एतत्’ यानी ‘यह’ उसी की ओर संकेत करता है। "
                   "बाद में (‘अनु’) सुखोदक यानी सुखद जल पीए। "
                   "अन्त में कहा है कि यह विरेचन ‘सुख’ यानी आसान, कष्ट न देने वाला है। "
                   "यहाँ कुष्ठ एक द्रव्य है, त्वचा का रोग नहीं।"),
    "hook": "अरंडी तेल + कूठ + त्रिकटु चाटो, ऊपर से सुखद पानी: आसान जुलाब।",
    "core": False,
    "questions": [
        mcq("pretest", 0,
            "By verse 96, with which oil is the preparation licked?",
            ("Eraṇḍa (castor) oil", "एरण्डतैलेन = with eraṇḍa (castor) oil."),
            [("Tila (sesame) oil", "Sesame oil is not named in this verse."),
             ("Sarṣapa (mustard) oil", "Mustard oil is not named in this verse."),
             ("Fresh butter (navanīta)", "Fresh butter belongs to line 05.02.177.")],
            "एरण्ड = castor, Ricinus communis (standard); तैल = oil.",
            "लिह्यात् · एरण्डतैलेन."),
        match(1, "Match each word of verse 96 to its meaning on the card.",
              [["एरण्ड", "castor"], ["कुष्ठ", "costus root"], ["त्रिकटुक", "the three pungents"],
               ["सुखोदक", "pleasant water"], ["विरेचन", "purgative"]],
              "The oil, the two additions, the after-drink, and what the whole is called.",
              "एरण्ड = castor; कुष्ठ = costus; त्रिकटुक = three pungents; सुखोदक = pleasant water; विरेचन = purgative."),
        order(2, "Put the phrases of verse 96 in the text's order.",
              ["लिह्यात्", "एरण्डतैलेन", "कुष्ठत्रिकटुकान्वितम्", "सुखोदकं चानुपिबेत्", "सुखमेतद्विरेचनम्"],
              "Lick, with castor oil, joined with kuṣṭha and trikaṭuka; drink pleasant water after; this purgative is easy.",
              "लिह्यात् · एरण्डतैलेन · कुष्ठत्रिकटुकान्वितम् · सुखोदकं चानुपिबेत् · सुखमेतद्विरेचनम्.",
              role="extend",
              teaches="The verse gives the action (lick) first, then the vehicle and the additions, then the after-drink and a judgement."),
        mcq("discriminate", 3, "By verse 96, how is this purgative described?",
            ("As easy (sukha)", "सुखम् एतद् विरेचनम् = this purgative is easy."),
            [("As the strongest", "No comparison of strength is made in this verse."),
             ("As for the old only", "No patient group is named in this verse."),
             ("As desired everywhere", "'Desired everywhere' is said of the purgative in line 05.02.175.")],
            "सुख = easy, comfortable; एतत् = this.",
            "सुखम् एतत् विरेचनम्."),
        multi("apply", 4, "Which three drugs make up trikaṭuka, as the card gives them?",
              [("śuṇṭhī (dried ginger)", "Right: one of the three pungents."),
               ("kuṣṭha (costus root)", "No: kuṣṭha is named beside trikaṭuka, not inside it."),
               ("pippalī (long pepper)", "Right: one of the three pungents."),
               ("eraṇḍa (castor)", "No: castor gives the oil it is licked with."),
               ("marica (black pepper)", "Right: one of the three pungents.")],
              [0, 2, 4],
              "त्रिकटुक = śuṇṭhī, pippalī, marica (standard).",
              "त्रि = three; कटु = pungent."),
        mcq("transfer", 5,
            "Like च + अनुपिबेत् → चानुपिबेत्, which is the joined form of च + अपि (invented)?",
            ("चापि", "अ + अ → आ: च + अपि → चापि."),
            [("चोपि", "ओ comes from अ + उ, not from अ + अ."),
             ("चैपि", "ऐ comes from अ + ए, not from अ + अ."),
             ("चपि", "The two अ merge into a long आ; neither is simply lost.")],
            "चानुपिबेत्, चापि: अ + अ → आ.",
            "अ + अ → आ.",
            teaches="Two अ sounds merge into आ: च + अनुपिबेत् → चानुपिबेत्, च + अपि → चापि."),
    ],
}

# ---------------------------------------------------------------- unit 97
AUTHORED["97"] = {
    "title": "अल्पस्यापि महार्थत्वं",
    "question": "What does verse 97 say a small and a large amount of a drug can be made to do, and by which five means?",
    "rule": ("Even a small amount can be given great purposefulness, and a large amount smallness of action, by "
             "combination, separation, time, processing and method (yukti)."),
    "limits": ("The subject (the physician) is not stated. The space after saṃśleṣa is read as one compound "
               "(an open reviewer point): no question on that spacing. How each means works is not explained here."),
    "explain_hi": ("यह श्लोक योग बनाने का एक सिद्धान्त बताता है। "
                   "थोड़ी मात्रा का भी बड़ा प्रयोजन (असर) और अधिक मात्रा का भी थोड़ा कर्म किया जा सकता है। "
                   "इसके पाँच साधन हैं: संश्लेष यानी मिलाना, विश्लेष यानी अलग करना, काल यानी समय, संस्कार यानी द्रव्य को संस्कारित करना, और युक्ति यानी उचित योजना। "
                   "कर्ता (वैद्य) का नाम नहीं लिया गया; ये पाँचों साधन कैसे काम करते हैं, यह भी यहाँ नहीं समझाया।"),
    "hook": "थोड़ा भी बहुत, बहुत भी थोड़ा: मिलाओ, अलग करो, समय, संस्कार, युक्ति।",
    "core": True,
    "questions": [
        mcq("pretest", 0,
            "By verse 97, what can even a small amount be given?",
            ("Great purposefulness", "अल्पस्यापि महार्थत्वम् = great purposefulness even of a small amount."),
            [("Smallness of action", "Smallness of action is what a large amount (प्रभूत) can be given."),
             ("A longer shelf life", "Keeping time is not mentioned in this verse."),
             ("A sweeter final taste", "Taste is not mentioned in this verse.")],
            "अल्प = small amount; महार्थत्व = great purposefulness.",
            "अल्प → महार्थत्व · प्रभूत → अल्पकर्मता."),
        match(1, "Match each word of verse 97 to its meaning.",
              [["अल्प", "small amount"], ["प्रभूत", "large amount"], ["संश्लेष", "combination"],
               ["विश्लेष", "separation"], ["संस्कार", "processing"]],
              "Two amounts in the first line; three of the five means in the second.",
              "अल्प = small; प्रभूत = large; संश्लेष = combination; विश्लेष = separation; संस्कार = processing."),
        order(2, "Put the five means of verse 97 in the text's order.",
              ["संश्लेष", "विश्लेष", "काल", "संस्कार", "युक्ति"],
              "Combination, separation, time, processing, method; the instrumental -भिः says 'by means of'.",
              "संश्लेष · विश्लेष · काल · संस्कार · युक्ति (-भिः).",
              role="extend",
              teaches="The five means are named in a row ending in the instrumental plural -भिः: '...युक्तिभिः', 'by ... method'."),
        mcq("discriminate", 3, "By verse 97, what can a large amount be given?",
            ("Smallness of action", "प्रभूतस्याल्पकर्मताम् = smallness of action of a large amount."),
            [("Great purposefulness", "Great purposefulness is what a small amount (अल्प) can be given."),
             ("A quicker digestion", "Digestion is not mentioned in this verse."),
             ("A pleasanter smell", "Smell is not mentioned in this verse.")],
            "प्रभूत = large amount; अल्पकर्मता = smallness of action.",
            "प्रभूत → अल्पकर्मता."),
        multi("apply", 4, "Which of these are means named in verse 97?",
              [("time (काल)", "Right: the third means."),
               ("dose (मात्रा)", "No: मात्रा is not named in this verse."),
               ("processing (संस्कार)", "Right: the fourth means."),
               ("place (देश)", "No: देश is not named in this verse."),
               ("method (युक्ति)", "Right: the fifth means.")],
              [0, 2, 4],
              "संश्लेष, विश्लेष, काल, संस्कार, युक्ति: the five means.",
              "संश्लेष · विश्लेष · काल · संस्कार · युक्ति."),
        mcq("transfer", 5,
            "Like अल्पकर्मता (smallness of action, abstract noun in -ता), which word means lightness, from लघु (invented)?",
            ("लघुता", "-ता makes an abstract noun: लघु 'light' → लघुता 'lightness'."),
            [("लघुतर", "-तर makes a comparative: 'lighter'."),
             ("लघुतम", "-तम makes a superlative: 'lightest'."),
             ("लघूकृत", "लघूकृत is a participle: 'made light'.")],
            "अल्पकर्मता, लघुता: -ता forms a feminine abstract noun ('-ness').",
            "X + -ता = 'X-ness'.",
            teaches="-ता (and -त्व) form abstract nouns: अल्पकर्मता 'smallness of action', महार्थत्व 'great purposefulness', लघुता 'lightness'."),
    ],
}

# ---------------------------------------------------------------- unit 98
AUTHORED["98"] = {
    "title": "मनोऽनुकूलैर्युक्तानि विरेचनानि",
    "question": "With which pleasant additions should purgatives be given, by verse 98?",
    "rule": ("Purgatives should be given mixed with tvak, kesara, āmrātaka, pomegranate, cardamom, rock sugar, mākṣika "
             "and citron, with madya (an intoxicating drink), and with the various things agreeable to the mind."),
    "limits": ("A flagged stray space splits the first word: no question on tvak, kesara, āmrātaka. kesara is disputed, "
               "mākṣika unresolved. elā = cardamom, sitopalā = rock sugar, āmrātaka = hog plum: probable; dāḍima = "
               "pomegranate, mātuluṅga = citron: standard. 'things' is supplied. No dose."),
    "explain_hi": ("यह श्लोक बताता है कि विरेचन रोगी को अच्छे लगने वाले द्रव्यों के साथ दिए जाएँ। "
                   "द्रव्य: त्वक् यानी छाल, केसर (पहचान विवादित), आम्रातक यानी अमड़ा, दाडिम यानी अनार, एला यानी इलायची, सितोपला यानी मिश्री, माक्षिक (पहचान अनिश्चित) और मातुलुङ्ग यानी बिजौरा नीबू। "
                   "साथ ही मद्य से और उन-उन मन के अनुकूल वस्तुओं से युक्त करके विरेचन देने चाहिए (‘देयानि’ = देने योग्य)। "
                   "पहले शब्द में छपाई की एक बीच की जगह है, इसलिए पहले तीन द्रव्यों पर प्रश्न नहीं बना।"),
    "hook": "जुलाब भी मन भाए: अनार, इलायची, मिश्री, बिजौरा, मद्य के साथ।",
    "core": False,
    "questions": [
        mcq("pretest", 0,
            "By verse 98, purgatives are given with things agreeable to what?",
            ("To the mind (मनः)", "मनोऽनुकूलैः = with (things) agreeable to the mind."),
            [("To the doṣa", "No doṣa is named in this verse."),
             ("To the season (ṛtu)", "No season is named in this verse."),
             ("To the belly", "The belly (koṣṭha) is not named in this verse.")],
            "मनः = mind; अनुकूल = agreeable.",
            "तैस्तैश्च मनोऽनुकूलैः युक्तानि."),
        match(1, "Match each word of verse 98 to its meaning on the card.",
              [["दाडिम", "pomegranate"], ["एला", "cardamom"], ["सितोपला", "rock sugar"],
               ["मातुलुङ्ग", "citron"], ["मद्य", "an intoxicating drink"]],
              "Four drugs from the first line and the madya of the second.",
              "दाडिम = pomegranate; एला = cardamom; सितोपला = rock sugar; मातुलुङ्ग = citron; मद्य = intoxicating drink."),
        order(2, "Put these members of the first line of verse 98 in the text's order.",
              ["दाडिम", "एला", "सितोपला", "माक्षिक", "मातुलुङ्ग"],
              "Pomegranate, cardamom, rock sugar, mākṣika, citron: the list ends in the instrumental -ऐः.",
              "दाडिम · एला · सितोपला · माक्षिक · मातुलुङ्ग (-ऐः).",
              role="extend",
              teaches="The pleasant additions stand in one instrumental compound: '... with pomegranate, cardamom ...'."),
        mcq("discriminate", 3, "Which split of मनोऽनुकूलैः is right?",
            ("मनः + अनुकूलैः", "अः + अ → ओऽ: मनः + अनुकूलैः → मनोऽनुकूलैः."),
            [("मन + अनुकूलैः", "अ + अ would give आ: मनानुकूलैः."),
             ("मनो + नुकूलैः", "There is no word नुकूलैः; the ऽ marks a lost अ."),
             ("मनस् + नुकूलैः", "स् before न would not give ओऽ, and नुकूलैः is no word.")],
            "मनः (mind) + अनुकूलैः (agreeable, inst. pl.).",
            "अः + अ → ओऽ."),
        mcq("apply", 4, "In verse 98, what does देयानि say about the purgatives?",
            ("They are to be given", "देयानि = to be given (gerundive of √दा)."),
            [("They have been given", "'Have been given' would be the past participle दत्तानि."),
             ("They are now being given", "The present would be a form like दीयन्ते."),
             ("They must not be given", "No negation (न) is in this verse.")],
            "देय = to be given; it agrees with विरेचनानि (n. nom. pl.).",
            "युक्तानि देयानि विरेचनानि."),
        mcq("transfer", 5,
            "Like देयानि विरेचनानि (to be given, from √दा), which form means to be drunk (√पा), with विरेचनानि (invented)?",
            ("पेयानि", "The gerundive in -य: √पा → पेय, neuter plural पेयानि."),
            [("पीतानि", "पीतानि is the past participle: 'drunk'."),
             ("पिबन्ति", "पिबन्ति is a present verb: 'they drink'."),
             ("पीत्वा", "पीत्वा is the absolutive: 'having drunk'.")],
            "देयानि, पेयानि: the gerundive 'is to be ...' agrees with its noun.",
            "√दा → देय; √पा → पेय.",
            teaches="The gerundive in -य says 'is to be done': √दा → देयानि 'to be given', √पा → पेयानि 'to be drunk'."),
    ],
}

# ---------------------------------------------------------------- unit 99
AUTHORED["99"] = {
    "title": "इति विरेचनकल्पो नाम द्वितीयोऽध्यायः",
    "question": "Which chapter does unit 99 close, and what is its number?",
    "rule": "Thus the second chapter, named Virecanakalpa (the purgative preparations): the colophon of Kalpasthāna chapter 2.",
    "limits": "A closing formula: it adds no drug or method. The chapter's contents are those of lines 05.02.1-184.",
    "explain_hi": ("यह अध्याय की समाप्ति-पंक्ति (पुष्पिका) है। "
                   "इसका नाम ‘विरेचनकल्प’ है, यानी विरेचन के योग: त्रिवृत्, आरग्वध, तिल्वक, स्नुही, दन्ती, हरीतकी आदि के योग इसी अध्याय में थे। "
                   "‘द्वितीयः’ बताता है कि यह कल्पस्थान का दूसरा अध्याय है। "
                   "विरेचनकल्पो नाम = विरेचनकल्पः + नाम।"),
    "hook": "इति: विरेचन के योगों का दूसरा अध्याय पूरा।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 99, what is the name of the chapter that ends here?",
            ("Virecanakalpa", "विरेचनकल्पो नाम = named Virecanakalpa (the purgative preparations)."),
            [("Vamanakalpa", "Vamanakalpa (emesis) is the first chapter, closed at line 05.01.71."),
             ("Bastikalpa", "Enema is not the name given in this unit."),
             ("Ṛtucaryā", "Ṛtucaryā is a Sūtrasthāna chapter.")],
            "विरेचन = purgation; कल्प = preparations.",
            "इति · विरेचनकल्पः · नाम · द्वितीयः · अध्यायः."),
        order(1, "Put the words of unit 99 in the order of the text.",
              ["इति", "विरेचनकल्पः", "नाम", "द्वितीयः", "अध्यायः"],
              "Thus, Virecanakalpa, named, the second, chapter.",
              "इति · विरेचनकल्पः · नाम · द्वितीयः · अध्यायः."),
        match(2, "Match each word of unit 99 to its meaning.",
              [["इति", "thus"], ["विरेचन", "purgation"], ["कल्प", "preparations"],
               ["द्वितीय", "second"], ["अध्याय", "chapter"]],
              "The words of the colophon around the chapter's name and number.",
              "इति = thus; विरेचन = purgation; कल्प = preparations; द्वितीय = second; अध्याय = chapter.",
              role="extend",
              teaches="Unit 99: इति = thus, विरेचनकल्प = the purgative preparations, द्वितीय = second, अध्याय = chapter."),
        mcq("discriminate", 3, "Which split of विरेचनकल्पो नाम is right?",
            ("विरेचनकल्पः + नाम", "अः → ओ before a voiced consonant (न): विरेचनकल्पः नाम → विरेचनकल्पो नाम."),
            [("विरेचनकल्पम् + नाम", "म् before न would give ं: विरेचनकल्पं नाम."),
             ("विरेचनकल्पे + नाम", "A final ए stays ए before न."),
             ("विरेचनकल्पौ + नाम", "A final औ stays औ before न.")],
            "विरेचनकल्पः (m. nom. sg.) + नाम (named).",
            "अः + voiced consonant → ओ."),
        fill(4, "Unit 99 calls this chapter the ____ (second) chapter. Type it in Devanagari or in English letters (e.g. dharma).",
             accepts("द्वितीयः", "dvitīyaḥ", "द्वितीय", "dvitīya", "dvitiyah"),
             "द्वितीयोऽध्यायः = द्वितीयः (second) + अध्यायः (chapter).",
             "Unit 99 names the chapter Virecanakalpa and calls it the second (द्वितीय) chapter.",
             "द्वितीय = second.", role="apply"),
        mcq("transfer", 5,
            "Like विरेचनकल्पः + नाम → विरेचनकल्पो नाम, which is the joined form of योगः + भवति (invented)?",
            ("योगो भवति", "अः before a voiced consonant (भ) becomes ओ."),
            [("योगा भवति", "Dropping to आ happens only after a long आः."),
             ("योगर्भवति", "Visarga becomes र् only after vowels other than अ or आ."),
             ("योगस्भवति", "स् appears only before त or थ.")],
            "विरेचनकल्पो नाम, योगो भवति: अः → ओ before a voiced consonant.",
            "अः + voiced consonant → ओ.",
            teaches="-अः before a voiced consonant becomes -ओ: विरेचनकल्पो नाम, योगो भवति."),
    ],
}


NOTES_HI = {
    "90": ("विश्वास: उच्च। ‘अपहाम्’ स्त्रीलिङ्ग द्वितीया एकवचन है और इसी श्लोक की ‘हरीतकीम्’ (पंक्ति ०५.०२.१६७) से मेल खाता है; डेटा का नोट इसे ‘पिछली इकाई’ की हरीतकी कहता है, पर हरीतकी इसी इकाई में है। "
           "‘उदर’ का सरल अर्थ पेट रखा गया; यह किसी उदर-रोग का नाम भी हो सकता है। "
           "‘त्रिवृत् की विधि’ के चरण यहाँ नहीं दोहराए गए। "
           "संधि जाँची: हरीतकीमपि = हरीतकीम् + अपि; त्रिवृद्विधानेन = त्रिवृत् + विधानेन (त् → द् घोष से पहले); विधानेनोपकल्पयेत् = विधानेन + उपकल्पयेत् (अ + उ → ओ); विशेषाद्ग्रहणी = विशेषात् + ग्रहणी; मोहोदर = मोह + उदर। छपा ‘पांडु’ = पाण्डु। "
           "पहचान (डेटा के अनुसार): हरीतकी = हरड़, Terminalia chebula; ग्रहणी = पुराना आँत-पाचन विकार (सम्भावित); पाण्डु = रक्ताल्पता (सम्भावित)।"),
    "91": ("विश्वास: उच्च। चारों साथी द्रव्य (सिन्धूत्थ, विडङ्ग, उत्पल, नागर) द्रव्य-नाम माने गए। "
           "खुला बिन्दु (०५.०२.१६९): उत्पल के लिए ‘Costus speciosus’ का प्रस्ताव पुष्ट नहीं है; सामान्य अर्थ नील कमल/कुमुदिनी, इस सूची में अर्थ अस्पष्ट; उत्पल की पहचान पर प्रश्न नहीं बना (क्रम-प्रश्न में केवल सूची में उसका स्थान है)। "
           "‘निर्यूह’ को काढ़ा (क्वाथ) पढ़ा गया; कषाय और क्वाथ से इसका भेद अभी खुला है। मूत्र किस पशु का, और वत्सकादि गण के सदस्य, नहीं बताए गए। "
           "संधि जाँची: पिबेत्पथ्यां = पिबेत् + पथ्याम्; विडङ्गोत्पल = विडङ्ग + उत्पल (अ + उ → ओ); वत्सकादेर्वा = वत्सकादेः + वा (ः → र् घोष से पहले)। छपा ‘सिंधू’, ‘विडंग’ = सिन्धू, विडङ्ग। "
           "पहचान: सिन्धूत्थ = सेंधा नमक (standard); विडङ्ग = Embelia ribes (standard); नागर = सोंठ (standard); वत्सक = कुटज, Holarrhena antidysenterica (standard)।"),
    "92": ("विश्वास: निम्न। छपा ‘संयुक्तंकोलिनीफले’ दो शब्द जुड़कर छपे हैं, और ‘-फले’ का विभक्ति-रूप भी गलत हो सकता है (फ़्लैग); इस शब्द और कोलिनी पर प्रश्न नहीं बना। "
           "सप्तमी ‘कोलिनीफले’ को अनुवाद में ‘के साथ’ पढ़ा गया। कोलिनी की पहचान नहीं हुई। "
           "संधि जाँची: भक्षयेत्तोयं = भक्षयेत् + तोयम्; पिबेदनु = पिबेत् + अनु (त् → द् स्वर से पहले)। ‘कोष्ण’ = थोड़ा गरम, गुनगुना।"),
    "93": ("विश्वास: मध्यम। दो फ़्लैग: (१) छपा ‘पथ्यात्रिवृद्धां’ का अन्त ‘-द्धां’ ठीक रूप नहीं; अर्थ से द्विवचन ‘पथ्यात्रिवृद्भ्याम्’ (पथ्या और त्रिवृत् से) पढ़ा गया। "
           "खुला बिन्दु (०५.०२.१७३): छन्द इस सुधार का प्रमाण नहीं (दोनों रूपों में १६ अक्षर), केवल अर्थ है। "
           "(२) छपा ‘लिह्माद्धृतद्रुताः’ अनुमान से ‘लिह्याद्घृतद्रुताः’ (घी में द्रवित करके चाटे) पढ़ा गया; सेवन-विधि पर प्रश्न नहीं बना। "
           "‘क्षौद्ररस’ को शहद और रस, या एक शब्द ‘मधु-रस’, दोनों तरह पढ़ा जा सकता है। ‘सूखी’ और ‘घी में द्रवित’ कैसे साथ चलते हैं, नहीं कहा। "
           "संधि जाँची: माषप्रमाणास्ताः = माषप्रमाणाः + ताः (ः → स् त से पहले)। माष एक छोटा माप है, रूपान्तर नहीं किया। यक्ष्मन् = क्षय रोग (सम्भावित; शब्द आधुनिक रोग से व्यापक)।"),
    "94": ("विश्वास: मध्यम। छपा ‘कटुष्णांबु’ तीन तरह पढ़ा जा सकता है: ‘कटु और उष्ण जल’, ‘कटु गरम जल’, या एक अक्षर छूटा ‘त्रिकटु’; यहाँ चार द्रव्यों वाला पाठ लिया गया; कटु पर प्रश्न नहीं बना। "
           "संधि जाँची: सर्वत्रेष्टं = सर्वत्र + इष्टम् (अ + इ → ए); कटुष्ण = कटु + उष्ण (उ + उ → ऊ होना चाहिए, छपा ‘कटुष्ण’ ह्रस्व है; इस पर प्रश्न नहीं); स्नुक्क्षीर = स्नुक् + क्षीर। "
           "‘भाविते’ सप्तमी: ‘भावित हो जाने पर’। स्नुक् = स्नुही, थूहर, Euphorbia neriifolia (सम्भावित); क्षीर = पौधे का दूधिया रस। मोदकों का माप पंक्ति ०५.०२.१७७ में है।"),
    "95": ("विश्वास: मध्यम। ‘मोदकान्’ पिछली पंक्ति ०५.०२.१७६ से लिया गया। ‘-विबन्धिनः’ षष्ठी एकवचन या बहुवचन (प्रथमा/द्वितीया) दोनों हो सकता है; ‘…वाले का’ पढ़ा गया; इस पर प्रश्न नहीं बना। "
           "‘लेहयेत्’ √लिह् का णिजन्त: शाब्दिक ‘चटाए’ (शब्दावली में यह अनुवाद अभी खुला है)। "
           "संधि जाँची: कोलास्थिमात्राञ् शुष्कांश्च = …मात्रान् + शुष्कान् + च (न् → ञ् श से पहले; न् + च → ंश्च); गुल्मोदर = गुल्म + उदर; शूलानाह = शूल + आनाह। छपा ‘विबंधिनः’ = विबन्धिनः। "
           "पहचान: कोल = बेर, Ziziphus jujuba (सम्भावित); आनाह = पेट का फूलना, मल-वायु रुकना (standard); विबन्ध = मलावरोध।"),
    "96": ("विश्वास: मध्यम। जिस वस्तु को चाटना है उसका नाम नहीं; ‘एतत्’ उसी की ओर लौटता है। ‘सुखोदक’ = सुखद जल (शायद सुहाता गरम; कहा नहीं)। "
           "यहाँ कुष्ठ द्रव्य है (कूठ, Saussurea lappa, standard), त्वचा-रोग नहीं। "
           "संधि जाँची: लिह्यादेरंड = लिह्यात् + एरण्ड (त् → द्); त्रिकटुकान्वितं = त्रिकटुक + अन्वितम् (अ + अ → आ); सुखोदकं = सुख + उदकम् (अ + उ → ओ); चानुपिबेत् = च + अनुपिबेत्; सुखमेतद्विरेचनं = सुखम् + एतत् + विरेचनम्। "
           "पहचान: एरण्ड = अरंडी, Ricinus communis (standard); त्रिकटुक = सोंठ, पीपर, काली मिर्च (standard)।"),
    "97": ("विश्वास: मध्यम। कर्ता नहीं बताया। ‘संश्लेष’ के बाद की जगह को एक ही समास का भाग माना गया: संश्लेष-विश्लेष-काल-संस्कार-युक्तिभिः। "
           "खुले बिन्दु (०५.०२.१८२): इस जगह पर फ़्लैग जोड़ने का सुझाव, और ‘संश्लेष’ का व्याकरण-चिह्न दो जगह आना; इन पर प्रश्न नहीं बना। "
           "संधि जाँची: अल्पस्यापि = अल्पस्य + अपि (अ + अ → आ); प्रभूतस्याल्प = प्रभूतस्य + अल्प; कुर्यात्संश्लेष = कुर्यात् + संश्लेष। ‘अर्थत्व’ = प्रयोजन, उपयोगिता।"),
    "98": ("विश्वास: मध्यम। उपजाति छन्द। छपा ‘त्वक्केसरा म्रातक…’ में बीच की जगह भूल है: ‘त्वक्केसराम्रातक…’ (त्वक्-केसर-आम्रातक) पढ़ा गया (फ़्लैग)। "
           "खुला बिन्दु (०५.०२.१८३): फ़्लैग का सुझाव ‘त्वक्केसराम्’ उसके अपने कारण से मेल नहीं खाता; ठीक सुझाव जगह हटाना है। इन तीन द्रव्यों पर प्रश्न नहीं बना। "
           "‘त्वक्-केसर’ एक द्रव्य है या दो, यह भी दो-तरफ़ा। केसर = सम्भवतः नागकेसर, Mesua ferrea (विवादित)। "
           "खुला बिन्दु (०५.०२.१८३): माक्षिक इस सूची में सम्भवतः शहद, खनिज अर्थ कम सम्भावित; निर्णय बाकी, इसलिए माक्षिक के अर्थ पर प्रश्न नहीं। "
           "संधि जाँची: दाडिमैला = दाडिम + एला (अ + ए → ऐ); सितोपला = सित + उपला; तैस्तैश्च = तैः + तैः + च; मनोऽनुकूलैर्युक्तानि = मनः + अनुकूलैः + युक्तानि। "
           "पहचान: दाडिम = अनार (standard); एला = इलायची (सम्भावित); सितोपला = मिश्री (सम्भावित); मातुलुङ्ग = बिजौरा, Citrus medica (standard); आम्रातक = अमड़ा (सम्भावित)।"),
    "99": ("विश्वास: उच्च। अध्याय की पुष्पिका, गद्य पंक्ति। आरम्भ का ‘॥’ छपाई का चिह्न है। "
           "संधि जाँची: विरेचनकल्पो नाम = विरेचनकल्पः + नाम (अः → ओ घोष न से पहले); द्वितीयोऽध्यायः = द्वितीयः + अध्यायः (अः + अ → ओऽ)।"),
}

AIDS = {
    "90": {
        "frame": "पहली पंक्ति: हरीतकी भी त्रिवृत् की विधि से तैयार करे · दूसरी पंक्ति: वह विशेष रूप से पाँच विकार दूर करने वाली।",
        "diagram": {"groups": [{"label": "हरीतकी दूर करे", "items": ["ग्रहणी", "पाण्डु", "शोष", "मोह", "उदर"]}]},
        "chunks": "हरीतकीमपि | त्रिवृद्विधानेनोपकल्पयेत् || विशेषाद्ग्रहणीपांडु | शोषमोहोदरापहाम्",
        "sandhi": "अ + उ → ओ: विधानेन + उपकल्पयेत् → विधानेनोपकल्पयेत्; त् → द् घोष से पहले: त्रिवृत् + विधानेन → त्रिवृद्विधानेन।",
        "anchors": "हरीतकी = हरड़ · विधान = विधि · उपकल्पयेत् = तैयार करे · विशेषात् = विशेष रूप से · अपहा = दूर करने वाली।",
    },
    "91": {
        "diagram": {"groups": [{"label": "पथ्या के साथ (पहली पंक्ति)", "items": ["सिन्धूत्थ", "विडङ्ग", "उत्पल", "नागर"]},
                               {"label": "हरीतकी किससे (दूसरी पंक्ति)", "items": ["मूत्र", "या वत्सक आदि का काढ़ा"]}]},
        "chunks": "पिबेत्पथ्यां ससिंधूत्थ | विडंगोत्पलनागराम् || मूत्रेण वत्सकादेर्वा | निर्यूहेण हरीतकीं",
        "anchors": "पथ्या = हरड़ · सिन्धूत्थ = सेंधा नमक · विडङ्ग = वायविडंग · नागर = सोंठ · वत्सक = कुटज · निर्यूह = काढ़ा।",
        "pegs": "मेरा बनाया स्मृति-सूत्र: ‘सि-वि-उ-ना’ (सिन्धूत्थ, विडङ्ग, उत्पल, नागर) - सेंधा, वायविडंग, उत्पल, सोंठ।",
    },
    "92": {
        "chain": {"steps": ["पथ्या और नागर का चूर्ण", "कोलिनी फल के साथ (पाठ अस्पष्ट)", "गुड़ के साथ खाना", "बाद में गुनगुना जल पीना"]},
        "chunks": "पथ्यानागरचूर्णं वा | संयुक्तंकोलिनीफले || गुडेन भक्षयेत्तोयं | कोष्णं च पिबेदनु",
        "anchors": "पथ्या = हरड़ · नागर = सोंठ · चूर्ण = पाउडर · गुड = गुड़ · तोय = जल · कोष्ण = गुनगुना · अनु = बाद में।",
    },
    "93": {
        "frame": "किससे: पथ्या और त्रिवृत् · किसके साथ: शहद और रस · माप: माष भर, सूखी · किसके लिए: यक्ष्मी (सेवन-विधि का शब्द बिगड़ा)।",
        "chunks": "पथ्यात्रिवृद्धां गुलिकाः | कार्याः क्षौद्ररसान्विताः || माषप्रमाणास्ताः शुष्का | यक्ष्मी लिह्माद्धृतद्रुताः",
        "sandhi": "ः + त → स्त: माषप्रमाणाः + ताः → माषप्रमाणास्ताः।",
        "anchors": "गुलिका = गोली · कार्य = बनानी चाहिए · क्षौद्र = शहद · माष = छोटा माप · शुष्क = सूखी · यक्ष्मी = क्षय रोगी।",
    },
    "94": {
        "contrast": "पहली पंक्ति: पथ्या, त्रिवृत्, कटु, गरम जल = सर्वत्र इष्ट विरेचन · दूसरी पंक्ति: थूहर के दूध से भावित पथ्या-चूर्ण के मोदक।",
        "chain": {"steps": ["पथ्या का चूर्ण", "स्नुक् के क्षीर से भावित", "मोदक बनाना"]},
        "chunks": "पथ्यात्रिवृत्कटुष्णांबु | सर्वत्रेष्टं विरेचनं || स्नुक्क्षीरभाविते पथ्या | चूर्णे कुर्वीत मोदकान्",
        "sandhi": "अ + इ → ए: सर्वत्र + इष्टम् → सर्वत्रेष्टम्।",
        "anchors": "सर्वत्र = हर जगह · इष्ट = चाहा गया · स्नुक् = थूहर · क्षीर = दूधिया रस · भावित = भिगोया हुआ · मोदक = गोला।",
    },
    "95": {
        "frame": "क्या: पिछली पंक्ति के मोदक · माप: बेर की गुठली भर, सूखे · किसके साथ: नवनीत (ताज़ा मक्खन) · किसके लिए: गुल्म से विबन्ध तक के रोगी।",
        "diagram": {"groups": [{"label": "किसके लिए", "items": ["गुल्म", "उदर", "यकृत्", "प्लीहा", "शूल", "आनाह", "विबन्ध"]}]},
        "chunks": "कोलास्थिमात्राञ् शुष्कांश्च | नवनीतेन लेहयेत् || गुल्मोदरयकृत्प्लीह | शूलानाहविबंधिनः",
        "sandhi": "न् + च → ंश्च: शुष्कान् + च → शुष्कांश्च।",
        "anchors": "कोल = बेर · अस्थि = गुठली · नवनीत = मक्खन · लेहयेत् = चटाए · यकृत् = जिगर · प्लीहा = तिल्ली · आनाह = पेट फूलना।",
    },
    "96": {
        "chain": {"steps": ["कुष्ठ और त्रिकटुक मिला योग", "एरण्ड तैल के साथ चाटना", "बाद में सुखद जल पीना", "यह सुख विरेचन"]},
        "chunks": "लिह्यादेरंडतैलेन | कुष्ठत्रिकटुकान्वितं || सुखोदकं चानुपिबेत् | सुखमेतद्विरेचनं",
        "sandhi": "अ + उ → ओ: सुख + उदकम् → सुखोदकम्; अ + अ → आ: च + अनुपिबेत् → चानुपिबेत्।",
        "anchors": "एरण्ड = अरंडी · कुष्ठ = कूठ · त्रिकटुक = सोंठ, पीपर, काली मिर्च · सुखोदक = सुखद जल · सुख = आसान।",
    },
    "97": {
        "seesaw": "अल्प (थोड़ी मात्रा) → महार्थत्व (बड़ा प्रयोजन) · प्रभूत (अधिक मात्रा) → अल्पकर्मता (थोड़ा कर्म)।",
        "diagram": {"groups": [{"label": "पाँच उपाय", "items": ["संश्लेष", "विश्लेष", "काल", "संस्कार", "युक्ति"]}]},
        "chunks": "अल्पस्यापि महार्थत्वं | प्रभूतस्याल्पकर्मतां || कुर्यात्संश्लेष विश्लेष | कालसंस्कारयुक्तिभिः",
        "anchors": "अल्प = थोड़ा · प्रभूत = बहुत · संश्लेष = मिलाना · विश्लेष = अलग करना · काल = समय · संस्कार = संस्कारित करना · युक्ति = उचित योजना।",
    },
    "98": {
        "diagram": {"groups": [{"label": "द्रव्य", "items": ["त्वक्", "केसर", "आम्रातक", "दाडिम", "एला", "सितोपला", "माक्षिक", "मातुलुङ्ग"]},
                               {"label": "और", "items": ["मद्य", "मन के अनुकूल वस्तुएँ"]}]},
        "chunks": "त्वक्केसरा म्रातकदाडिमैला | सितोपलामाक्षिकमातुलुंगैः || मद्येन तैस्तैश्च मनोऽनुकूलै | र्युक्तानि देयानि विरेचनानि",
        "sandhi": "अः + अ → ओऽ: मनः + अनुकूलैः → मनोऽनुकूलैः; अ + ए → ऐ: दाडिम + एला → दाडिमैला।",
        "anchors": "दाडिम = अनार · एला = इलायची · सितोपला = मिश्री · मातुलुङ्ग = बिजौरा · मद्य = मादक पेय · अनुकूल = भाने वाला · देय = देने योग्य।",
    },
    "99": {
        "frame": "इति = इस प्रकार · विरेचनकल्प = विरेचन के योग · नाम = नामक · द्वितीय अध्याय = दूसरा अध्याय (कल्पस्थान)।",
        "sandhi": "अः → ओ घोष से पहले: विरेचनकल्पः + नाम → विरेचनकल्पो नाम; अः + अ → ओऽ: द्वितीयः + अध्यायः → द्वितीयोऽध्यायः।",
        "anchors": "इति = इस प्रकार · विरेचन = दस्त से शोधन · कल्प = योग · द्वितीय = दूसरा · अध्याय = अध्याय।",
    },
}

IMAGE_SPECS = {
    ("90", "diagram"): {
        "file": "ka2-haritaki-roga-90.svg",
        "alt": "Mind map of verse 90: the head 'haritaki removes' with five branches: grahani, pandu, shosha, moha and udara",
        "type": "mermaid",
        "code": ('mindmap\n  हरीतकी दूर करे\n    ग्रहणी\n    पाण्डु\n    शोष\n    मोह\n    उदर\n'),
    },
    ("91", "diagram"): {
        "file": "ka2-pathya-yoga-91.svg",
        "alt": "Two-column picture of verse 91: pathya drunk with rock salt, vidanga, utpala and dried ginger; haritaki taken with urine or a decoction of vatsaka and the rest",
        "type": "split",
        "title": "श्लोक ९१: हरड़ के दो योग",
        "cols": [["पथ्या के साथ", ["सिन्धूत्थ (सेंधा नमक)", "विडङ्ग", "उत्पल", "नागर (सोंठ)"]],
                 ["हरीतकी किससे", ["मूत्र", "या वत्सक आदि का काढ़ा"]]],
    },
    ("94", "chain"): {
        "file": "ka2-snuk-modaka-94.svg",
        "alt": "Flowchart of verse 94, second line: pathya powder is steeped in snuk milk, then balls (modaka) are made",
        "type": "mermaid",
        "code": ('flowchart TD\n  A["पथ्या का चूर्ण"] --> B["स्नुक् के क्षीर<br/>से भावित"]\n'
                 '  B --> C["मोदक बनाना"]\n'),
    },
    ("95", "diagram"): {
        "file": "ka2-modaka-roga-95.svg",
        "alt": "Mind map of verse 95: balls (modaka) with fresh butter at the centre, for gulma, udara, liver, spleen, pain, anaha and vibandha",
        "type": "mermaid",
        "code": ('mindmap\n  मक्खन के साथ मोदक\n    गुल्म\n    उदर\n    यकृत्\n    प्लीहा\n    शूल\n    आनाह\n    विबन्ध\n'),
    },
    ("97", "seesaw"): {
        "file": "ka2-yukti-matra-97.svg",
        "alt": "Flowchart of verse 97: five means (combination, separation, time, processing, method) give a small amount great purposefulness and a large amount small action",
        "type": "mermaid",
        "code": ('flowchart TD\n  U["संश्लेष · विश्लेष · काल<br/>संस्कार · युक्ति"] --> X["अल्प: महार्थत्व<br/>थोड़े का बड़ा प्रयोजन"]\n'
                 '  U --> Y["प्रभूत: अल्पकर्मता<br/>बहुत का थोड़ा कर्म"]\n'),
    },
    ("98", "diagram"): {
        "file": "ka2-manonukula-98.svg",
        "alt": "Two-column picture of verse 98: purgatives given with tvak, kesara, amrataka, pomegranate, cardamom, rock sugar, makshika, citron; and with madya and things agreeable to the mind",
        "type": "split",
        "title": "श्लोक ९८: विरेचन के साथ",
        "cols": [["द्रव्य", ["त्वक्", "केसर", "आम्रातक", "दाडिम", "एला", "सितोपला", "माक्षिक", "मातुलुङ्ग"]],
                 ["और", ["मद्य", "मन के अनुकूल वस्तुएँ"]]],
    },
}
