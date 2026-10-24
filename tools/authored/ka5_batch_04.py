from helpers import mcq, match, order, fill, multi, accepts

# Kalpasthana chapter 5 (Siddhabastikalpa), units 47-61 (lines 05.05.92-121).
# 47-55: anuvasana oils and ghees against Vata and Pitta:
#   47-50 dashamula oil with the jivaniya paste (verb vipacya / pacet in 05.05.96-97),
#   51 shatahva oil and a heated preparation, 52-54 oil and ghee in milk, 55 the Pitta ghee.
# 56-61: anuvasana and niruha against Kapha:
#   56-59 one list whose oil is named in 05.05.115 and whose uses follow in 05.05.116-117,
#   60 pancamula / bilvadi oil, 61 fruit-and-sour anvasana and the niruha for pain and distension.

AUTHORED = {}

# ---------------------------------------------------------------- unit 47
AUTHORED["47"] = {
    "title": "दशमूलं वरां रास्नाम्",
    "question": "Which drugs does verse 47 list at the start of the new anuvāsana oil?",
    "rule": ("Verse 47 opens a drug list in the accusative: daśamūla (the ten roots), varā, rāsnā, "
             "aśvagandhā and punarnavā; then guḍūcī, eraṇḍa, bhūtīka, bhārgī, vṛṣaka and śirīṣa. "
             "Its verb comes later (verse 49)."),
    "limits": ("Low confidence. In the damaged compound of line 2, eraṇḍa and śirīṣa rest on suggested "
               "readings: no question uses them. bhūtīka is unidentified, rāsnā disputed. The ten roots "
               "of daśamūla are not named (open point). No verb here."),
    "explain_hi": ("यहाँ से वात-पित्तहर अनुवासन तेलों का नया प्रकरण शुरू होता है, और यह श्लोक पहले तेल के द्रव्य गिनाता है। "
                   "पहली पंक्ति: दशमूल यानी दस जड़ों का समूह, वरा यानी सम्भवतः त्रिफला, रास्ना (पहचान विवादित), अश्वगन्धा यानी असगन्ध और पुनर्नवा। "
                   "दूसरी पंक्ति एक लम्बा समास है: गुडूची यानी गिलोय, एरण्ड यानी अरंडी, भूतीक, भार्गी यानी भारंगी, वृषक यानी सम्भवतः अडूसा और शिरीष। "
                   "सब नाम द्वितीया विभक्ति में हैं: ये किसी आने वाली क्रिया के कर्म हैं, जो श्लोक ४९ में (‘विपाच्य’) आती है। "
                   "दूसरी पंक्ति की छपाई बिगड़ी है, इसलिए एरण्ड और शिरीष अनुमानित पाठ पर टिके हैं।"),
    "hook": "दशमूल से शुरू, वरा-रास्ना-असगन्ध-पुनर्नवा, फिर गिलोय-भारंगी-अडूसा।",
    "core": False,
    "questions": [
        mcq("pretest", 0,
            "What is दशमूल, the first item of verse 47, by the card?",
            ("A group of ten roots", "दश (ten) + मूल (root): the traditional group of ten roots."),
            [("One root boiled ten times", "Nothing is boiled ten times; दश counts the roots."),
             ("Ten pala of a single root", "No pala is given in verse 47; दश counts roots."),
             ("The root of a ten-leaved herb", "The card reads it as a group of ten roots, not one plant.")],
            "दशमूल names a group: ten roots taken together.",
            "दशमूल = दस जड़ों का समूह."),
        match(1, "Match each drug of verse 47 to its identification on the card.",
              [["वरा", "probably triphalā"], ["अश्वगन्धा", "ashwagandha (Withania somnifera)"],
               ["पुनर्नवा", "Boerhavia diffusa"], ["गुडूची", "giloy (Tinospora cordifolia)"]],
              "Four clear names of the list with the identifications the data gives.",
              "वरा = probably triphalā; अश्वगन्धा = Withania; पुनर्नवा = Boerhavia; गुडूची = giloy."),
        order(2, "Put the drugs of line 1 of verse 47 in their order.",
              ["दशमूल", "वरा", "रास्ना", "अश्वगन्धा", "पुनर्नवा"],
              "Line 1 runs daśamūla, varā, rāsnā, aśvagandhā, punarnavā.",
              "दशमूलं · वरां · रास्नाम् · अश्वगंधां · पुनर्नवां.",
              role="extend",
              teaches="Line 1 of verse 47: daśamūla, varā, rāsnā, aśvagandhā, punarnavā, all in the accusative."),
        multi("discriminate", 3, "Which of these does verse 47 name?",
              [("पुनर्नवा", "Named at the end of line 1."),
               ("भार्गी", "Named inside the compound of line 2."),
               ("गुडूची", "Opens the compound of line 2."),
               ("शतावरी", "Śatāvarī comes in verse 48, not 47."),
               ("जीवन्ती", "Jīvantī comes in verse 52, not 47.")],
              [0, 1, 2],
              "Only names printed in verse 47 count; śatāvarī and jīvantī belong to later verses.",
              "Count as listed only what the verse names."),
        mcq("apply", 4, "Why do the drug names of verse 47 stand in the accusative?",
            ("They are objects of a later verb", "The card: no verb here; the list is the object of vipācya in verse 49."),
            [("They are subjects of the sentence", "A subject would be nominative; these end in -आम्, -म्."),
             ("They name the diseases treated", "These are drug names, not diseases."),
             ("They are persons being addressed", "Address uses the vocative; these are drugs.")],
            "An accusative list waits for its verb; here the verb comes two verses later.",
            "द्वितीया = कर्म: verb vipācya (05.05.96)."),
        mcq("transfer", 5,
            "Like रास्नाम् + अश्वगन्धाम् → रास्नामश्वगन्धाम्, how do invented वचाम् + अभयाम् join?",
            ("वचामभयाम्", "Final म् before a vowel stays म् and joins it: वचाम् + अभयाम्."),
            [("वचांभयाम्", "Anusvāra replaces म् only before a consonant, not before अ."),
             ("वचाभयाम्", "The म् cannot simply drop before a vowel."),
             ("वचामाभयाम्", "No long आ arises; अ stays short after म्.")],
            "म् + vowel → म joined to the vowel, as in रास्नामश्वगन्धाम्.",
            "म् + स्वर → म-युक्त स्वर.",
            teaches="A final म् before a vowel joins it: रास्नाम् + अश्वगन्धाम् → रास्नामश्वगन्धाम्; वचाम् + अभयाम् → वचामभयाम्."),
    ],
}

# ---------------------------------------------------------------- unit 48
AUTHORED["48"] = {
    "title": "शतावरीं सहचरं काकनासाम्",
    "question": "Which drugs and grains does verse 48 add, and with which measures?",
    "rule": ("Verse 48 adds śatāvarī, sahacara and kākanāsā, with palāṃśika (having a pala as share), "
             "then barley (yava), black gram (māṣa), flax (atasī), kola and horse gram (kulattha), "
             "measured by the prasṛta."),
    "limits": ("The noun qualified by palāṃśika is not stated, and 'each' is not in the Sanskrit. "
               "kākanāsā is disputed, sahacara and kola probable. The measures are left unconverted. "
               "The list continues verse 47; its verb is most probably vipācya in verse 49."),
    "explain_hi": ("यह श्लोक श्लोक ४७ की द्रव्य-सूची आगे बढ़ाता है। "
                   "पहली पंक्ति: शतावरी, सहचर यानी सम्भवतः कटसरैया और काकनासा (पहचान विवादित), और ‘पलांशिक’ यानी जिसका भाग एक पल है। "
                   "दूसरी पंक्ति पाँच अन्न और फल: यव, माष यानी उड़द, अतसी यानी अलसी, कोल यानी सम्भवतः बेर और कुलत्थ यानी कुलथी; ये प्रसृत से मापे जाते हैं। "
                   "प्रसृत अंजलि-भर का मान है; ‘प्रत्येक’ शब्द संस्कृत में नहीं है। "
                   "क्रिया अभी नहीं आई: ये सब श्लोक ४९ के ‘विपाच्य’ के कर्म लगते हैं।"),
    "hook": "शतावरी-सहचर-काकनासा पल-भर; यव-माष-अतसी-कोल-कुलत्थ प्रसृत-भर।",
    "core": False,
    "questions": [
        mcq("pretest", 0,
            "By verse 48, with which measure are yava, māṣa and the other grains measured?",
            ("With the prasṛta", "प्रसृतोन्मितान् = measured by prasṛta, the cupped-palm measure."),
            [("With the pala", "Pala goes with the three drugs of line 1 (palāṃśika)."),
             ("With the droṇa", "Droṇa is the remainder of the boiling in verse 49."),
             ("With the āḍhaka (a volume)", "Āḍhaka measures the oil in verse 49.")],
            "The measure word is joined to the grains in one compound: prasṛta-unmita.",
            "प्रसृत-उन्मित = प्रसृत से मापा हुआ."),
        match(1, "Match each grain of verse 48 to its meaning on the card.",
              [["यव", "barley"], ["माष", "black gram"], ["अतसी", "flax, linseed"], ["कुलत्थ", "horse gram"]],
              "Four items of line 2 with their ordinary names.",
              "यव = barley; माष = black gram; अतसी = flax; कुलत्थ = horse gram."),
        order(2, "Put the items of line 2 of verse 48 in their order.",
              ["यव", "माष", "अतसी", "कोल", "कुलत्थ"],
              "The compound runs yava, māṣa, atasī, kola, kulattha.",
              "यव · माष · अतसी · कोल · कुलत्थ (प्रसृत-मापे).",
              role="extend",
              teaches="Line 2 of verse 48: yava, māṣa, atasī, kola, kulattha, measured by the prasṛta."),
        mcq("discriminate", 3, "What does पलांशिक (printed पळांशिकं) mean on the card?",
            ("Having a pala as share", "पल (a weight) + अंशिक (having as share)."),
            [("Measured by a prasṛta", "That is said of the grains in line 2."),
             ("One quarter of a pala", "No quarter is named; अंश here is share, not quarter."),
             ("Cut into pala-sized bits", "Cutting is not in the word; it names the share.")],
            "अंश = share; पलांशिक = one whose share is a pala.",
            "पल + अंशिक = जिसका भाग एक पल."),
        mcq("apply", 4, "A student writes a pala of each drug for verse 48. Is each in the Sanskrit?",
            ("No; each is not in the Sanskrit", "The card: the noun is not stated and 'each' is not in the text."),
            [("Yes; palāṃśika means each", "Palāṃśika means having a pala as share, nothing about each."),
             ("Yes; prasṛta means each one", "Prasṛta is a measure, the cupped palm."),
             ("No; the verse gives no measures at all", "It gives two: pala and prasṛta.")],
            "Do not supply 'each': the verse gives the measure, not its distribution.",
            "‘प्रत्येक’ पाठ में नहीं."),
        mcq("transfer", 5,
            "Like माष + अतसी → माषातसी, how do invented तिल + अतसी join in a compound?",
            ("तिलातसी", "अ + अ → आ: तिल + अतसी = तिलातसी, as माष + अतसी = माषातसी."),
            [("तिलेतसी", "ए comes from अ + इ, not from अ + अ."),
             ("तिलोतसी", "ओ comes from अ + उ, not from अ + अ."),
             ("तिलअतसी", "Inside a compound the two अ must merge.")],
            "Two short अ merge into one long आ.",
            "अ + अ → आ.",
            teaches="अ + अ → आ: माष + अतसी = माषातसी; तिल + अतसी = तिलातसी."),
    ],
}

# ---------------------------------------------------------------- unit 49
AUTHORED["49"] = {
    "title": "वहे विपाच्य तोयस्य",
    "question": "How does verse 49 make the decoction and then cook the oil?",
    "rule": ("Having boiled (the drugs) in a vaha of water until a droṇa remains, one should cook an "
             "āḍhaka of oil with that (liquid), together with the jīvanīya drugs, to be ground and "
             "measured by a pala."),
    "limits": ("vahe is read as the measure vaha (doubtful). The sizes of vaha and droṇa are not worked "
               "out (an open point), and the object of vipācya is not stated (most probably the list of "
               "verses 47-48). The ten jīvanīya drugs are not listed in the line."),
    "explain_hi": ("यह श्लोक विधि बताता है। "
                   "पहले (श्लोक ४७-४८ के द्रव्यों को) एक ‘वह’ जल में पकाकर इतना उबालें कि एक द्रोण शेष रहे। "
                   "फिर ‘तेन’ यानी उसी शेष क्वाथ से एक आढक तेल पकाएँ। "
                   "साथ में जीवनीय द्रव्य हों, पीसने योग्य और पल से मापे हुए। "
                   "वह, द्रोण, आढक और पल मान हैं; उनके आकार यहाँ तय नहीं किए गए।"),
    "hook": "वह-भर जल, द्रोण बचे; उससे आढक तेल, जीवनीय पल-भर पीसकर।",
    "core": False,
    "questions": [
        mcq("pretest", 0,
            "In verse 49, until how much water is left is the boiling continued?",
            ("Until a droṇa remains", "द्रोणशेषेण = with a droṇa as remainder."),
            [("Until a vaha remains", "The vaha is the water one starts with."),
             ("Until an āḍhaka is left", "The āḍhaka measures the oil, not the remainder."),
             ("Until a pala remains", "The pala measures the jīvanīya drugs.")],
            "शेष (remainder) is joined to droṇa: boil down to a droṇa.",
            "द्रोणशेष = एक द्रोण शेष."),
        order(1, "Put the phrases of verse 49 in their order.",
              ["वहे विपाच्य तोयस्य", "द्रोणशेषेण तेन च", "पचेत्तैलाढकं", "पेष्यैर्जीवनीयैः पलोन्मितैः"],
              "Boil, keep the remainder, cook the oil, with the jīvanīya paste.",
              "वह जल में उबालकर · द्रोण शेष, उससे · तेल पकाए · जीवनीय पल-भर."),
        match(2, "Match each measure of verse 49 to what it measures.",
              [["वह", "the water boiled"], ["द्रोण", "what remains"], ["आढक", "the oil"],
               ["पल", "the jīvanīya drugs"]],
              "Four measures, four quantities: water, remainder, oil, paste.",
              "वह = जल; द्रोण = शेष; आढक = तेल; पल = जीवनीय.",
              role="extend",
              teaches="In verse 49 the vaha measures the water, the droṇa the remainder, the āḍhaka the oil, the pala the jīvanīya drugs."),
        mcq("discriminate", 3, "To what does तेन (with that) refer in verse 49, by the card?",
            ("The liquid left after boiling", "The card: tena refers to the resulting liquid (the decoction)."),
            [("The āḍhaka of oil itself", "The oil is what is cooked with it, not 'that'."),
             ("The jīvanīya drugs ground", "Those are added in the instrumental of line 2."),
             ("The vaha vessel of water", "The card reads vaha as a measure, not a vessel.")],
            "First the decoction is made; then the oil is cooked with it.",
            "तेन = उस (शेष क्वाथ) से."),
        mcq("apply", 4, "Which split of पेष्यैर्जीवनीयैः is right?",
            ("पेष्यैः + जीवनीयैः", "ऐः before a voiced sound (ज) becomes ऐर्."),
            [("पेष्ये + ऐर्जीवनीयैः", "ऐर्जीवनीय is no word; the noun is जीवनीय."),
             ("पेष्यैः + अजीवनीयैः", "That would give पेष्यैरजीवनीयैः, which is not printed."),
             ("पेष्य + एर्जीवनीयैः", "एर्जीवनीय is no word; पेष्यैः is instrumental plural.")],
            "Visarga after ऐ turns into र् before ज: पेष्यैः जीवनीयैः → पेष्यैर्जीवनीयैः.",
            "ऐः + सघोष व्यञ्जन → ऐर्."),
        mcq("transfer", 5,
            "Like विपाच्य (वि- + √पच् + -य), which invented form means having ground, from प्र + √पिष्?",
            ("प्रपिष्य", "With a prefix the absolutive takes -य: प्र + पिष् + य = प्रपिष्य."),
            [("प्रपिष्ट्वा", "-त्वा is used without a prefix; with प्र- it becomes -य."),
             ("प्रपिनष्टि", "This is a present verb, 'grinds', not 'having ground'."),
             ("प्रपिष्टम्", "This is a past participle, 'ground', not 'having ground'.")],
            "Prefix + root takes -य (विपाच्य, प्रपिष्य); a bare root takes -त्वा.",
            "उपसर्ग + धातु → -य (ल्यप्).",
            teaches="With a prefix the absolutive ends in -य: वि + पच् → विपाच्य, प्र + पिष् → प्रपिष्य."),
    ],
}

# ---------------------------------------------------------------- unit 50
AUTHORED["50"] = {
    "title": "अनुवासनमित्येतत्",
    "question": "What does verse 50 call this oil, what does it dispel, and what is prepared in the same way?",
    "rule": ("This (oil) is called anuvāsana and dispels all disorders of Vāta. The fat (vasā) of the "
             "marsh-dwelling (ones) is likewise prepared with the jīvanīya (drugs)."),
    "limits": ("Line 2 has no verb, and the noun 'animals' is not stated (ānūpa = of marshy ground). "
               "tadvat refers to the preparation of the previous units. What the vasā is for is not said "
               "beyond 'similarly'."),
    "explain_hi": ("श्लोक ४७-४९ में बने तेल का नाम यहाँ दिया गया है: ‘अनुवासन’ यानी कुछ समय रोका जाने वाला स्नेह-बस्ति। "
                   "यह सब वात-विकारों को दूर करता है: ‘सर्ववातविकारनुत्’। "
                   "दूसरी पंक्ति एक और द्रव्य जोड़ती है: आनूप यानी दलदली भूमि के (प्राणियों) की वसा, जो ‘तद्वत्’ यानी उसी प्रकार जीवनीयों से तैयार की जाए। "
                   "‘प्राणी’ शब्द पाठ में नहीं है, और दूसरी पंक्ति में क्रिया भी नहीं।"),
    "hook": "दशमूल-तेल = अनुवासन, सब वातरोग दूर; अनूप-वसा भी वैसे ही।",
    "core": True,
    "questions": [
        mcq("pretest", 0,
            "What does verse 50 say this anuvāsana dispels?",
            ("All disorders of Vāta", "सर्ववातविकारनुत् = dispelling all Vāta disorders."),
            [("All disorders of Kapha", "Kapha oils come only from verse 56 on."),
             ("Only disorders of Pitta", "Pitta is not named in verse 50."),
             ("Ailments of semen alone", "Semen ailments are named in verse 54, not here.")],
            "The compound names the doṣa: sarva-vāta-vikāra-nud.",
            "सर्व-वात-विकार-नुद् = सब वातविकारों को दूर करने वाला."),
        match(1, "Match each word of verse 50 to its meaning on the card.",
              [["अनुवासन", "unctuous retention enema"], ["विकार", "disorder"],
               ["आनूप", "of marshy ground"], ["वसा", "fat"]],
              "The name, the disorder word, and the two words of line 2.",
              "अनुवासन = oil enema; विकार = disorder; आनूप = marsh-dwelling; वसा = fat."),
        order(2, "Put the phrases of verse 50 in their order.",
              ["अनुवासनमित्येतत्", "सर्ववातविकारनुत्", "आनूपानां वसा", "तद्वज्जीवनीयोपसाधिता"],
              "Name, action, then the second item and how it is made.",
              "नाम · वात-नाशक · आनूप-वसा · उसी प्रकार जीवनीय से.",
              role="extend",
              teaches="Verse 50 first names the oil (anuvāsana, against all Vāta disorders), then adds marsh-animal fat prepared the same way."),
        mcq("discriminate", 3, "Whose fat (vasā) does verse 50 name?",
            ("That of the marsh-dwelling ones", "आनूपानाम् = of the (ones) of marshy ground."),
            [("That of the desert-dwelling ones", "Desert animals are not named; ānūpa means marshy."),
             ("That of the village-kept ones", "Domestic animals are not named in verse 50."),
             ("That of the tree-dwelling birds", "No birds are named; ānūpa is marshy ground.")],
            "आनूप comes from अनूप, marshy (watery) country.",
            "आनूप = दलदली भूमि का."),
        mcq("apply", 4, "To what does तद्वत् (similarly) in verse 50 point, by the card?",
            ("The preparation described before", "The card: tadvat refers to the preparation of the previous units."),
            [("The Pitta ghee of verse 55", "A later verse cannot be meant by 'similarly' here."),
             ("A preparation without drugs", "The line itself names the jīvanīya drugs."),
             ("The way the enema is given", "Giving the enema is not described in these verses.")],
            "Like the oil of verses 47-49, the vasā is cooked with the jīvanīya drugs.",
            "तद्वत् = उसी प्रकार (पिछली विधि से)."),
        mcq("transfer", 5,
            "Like सर्ववातविकारनुत् (stem -नुद्), how does an invented compound for dispelling Kapha disorders end in the nominative?",
            ("कफविकारनुत्", "A final द् becomes त् at the end of a word: -नुद् → -नुत्."),
            [("कफविकारनुद्", "A final voiced द् is not kept at the end of a word."),
             ("कफविकारनुदः", "-नुदः is another case or the plural, not this nominative singular."),
             ("कफविकारनोदः", "नोद is a different noun, 'dispelling', not the -नुद् agent.")],
            "-नुद् at the end of a compound, final position: -नुत्.",
            "पदान्त द् → त्.",
            teaches="The agent ending -नुद् (dispelling) is written -नुत् at the end of a word: सर्ववातविकारनुत्, कफविकारनुत्."),
    ],
}

# ---------------------------------------------------------------- unit 51
AUTHORED["51"] = {
    "title": "शताह्वायवबिल्वाम्लैः",
    "question": "Which oil does verse 51 give for wind (Vāta), and how is its second preparation heated?",
    "rule": ("Oil cooked with śatāhvā (dill), yava, bilva (bael) and sour (ones) is given in samīraṇa "
             "(wind, Vāta). A second preparation, heated with fire-coloured (red-hot) rock salt, "
             "conquers Vāta; it is ghee only on a conjectural reading."),
    "limits": ("samīraṇe is literally 'in wind'; 'for wind' is interpretation (open point). The printed "
               "-ddhṛtaṃ is read as ghṛtam (ghee) by conjecture (open point): no question uses it. amla may "
               "be one sour drug. How the salt is used beyond 'heated with' is not said."),
    "explain_hi": ("यह श्लोक वात के लिए दो योग देता है। "
                   "पहला: शताह्वा यानी सोआ, यव, बिल्व यानी बेल और खट्टे (द्रव्यों) से सिद्ध तेल, ‘समीरणे’ यानी वायु (वात) में। "
                   "दूसरा: अग्नि के रंग का, यानी तपकर लाल हुआ सेंधा नमक, उससे तपाया गया और ‘अनिलजित्’ यानी वात को जीतने वाला द्रव्य। "
                   "छपा शब्द ‘धृत’ है; उसे ‘घृत’ यानी घी पढ़ना अनुमान है। "
                   "‘समीरणे’ शाब्दिक रूप से ‘वायु में’ है; ‘वायु के लिए’ अर्थ व्याख्या है।"),
    "hook": "सोआ-यव-बेल-खट्टा तेल वात में; लाल-तपे सेंधे से तपा, वात-जित्।",
    "core": False,
    "questions": [
        mcq("pretest", 0,
            "With which drugs is the oil of verse 51 cooked?",
            ("Śatāhvā, yava, bilva and sour ones", "शताह्वा-यव-बिल्व-अम्लैः = with these four."),
            [("Daśamūla, varā, rāsnā and punarnavā", "That list belongs to verse 47."),
             ("Jīvantī, madana, medā and balā", "Those drugs are listed in verse 52."),
             ("Saindhava, madana, kuṣṭha and vacā", "That list opens verse 56, the Kapha oil.")],
            "One instrumental compound names all four: śatāhvā, yava, bilva, amla.",
            "शताह्वा + यव + बिल्व + अम्ल → तैलं सिद्धम्."),
        match(1, "Match each word of verse 51 to its meaning on the card.",
              [["शताह्वा", "dill (Anethum sowa)"], ["बिल्व", "bael (Aegle marmelos)"],
               ["समीरण", "wind, a name of Vāta"], ["सैन्धव", "rock salt"]],
              "Two drugs, the name of the doṣa, and the salt.",
              "शताह्वा = सोआ; बिल्व = बेल; समीरण = वात; सैन्धव = सेंधा नमक."),
        order(2, "Put the phrases of verse 51 in their order.",
              ["शताव्हायवबिल्वाम्लैः", "तैलं सिद्धं समीरणे", "सैंधवेनाग्निवर्णेन", "तप्तं"],
              "First the oil and its drugs, then the salt and the heating.",
              "द्रव्य · तेल सिद्ध, वात में · लाल-तपे सेंधे से · तपाया.",
              role="extend",
              teaches="Verse 51 gives first the śatāhvā-yava-bilva-amla oil for Vāta, then a preparation heated with red-hot rock salt."),
        mcq("discriminate", 3, "What does अग्निवर्णेन describe in verse 51?",
            ("The rock salt, red-hot", "सैन्धवेन अग्निवर्णेन = with rock salt of fire colour."),
            [("The oil, turned dark red", "अग्निवर्णेन agrees with सैन्धवेन, the salt."),
             ("A fire lit under the pot", "No fire under a pot is named; the salt is fire-coloured."),
             ("The patient's flushed skin", "The patient is not described in verse 51.")],
            "Both words are instrumental singular: the salt is fire-coloured.",
            "अग्निवर्ण = आग के रंग का, तपकर लाल."),
        mcq("apply", 4, "Which split of सैंधवेनाग्निवर्णेन is right?",
            ("सैन्धवेन + अग्निवर्णेन", "अ + अ → आ: सैन्धवेन + अग्निवर्णेन."),
            [("सैन्धवे + नाग्निवर्णेन", "नाग्निवर्ण is no word; the instrumental is सैन्धवेन."),
             ("सैन्धवेन + नाग्निवर्णेन", "That would give सैन्धवेननाग्नि-, with an extra न."),
             ("सैन्धवेनः + अग्निवर्णेन", "A visarga before अ would give -नोऽग्नि-, not -नाग्नि-.")],
            "The long आ after न comes from -एन + अ-.",
            "अ + अ → आ."),
        mcq("transfer", 5,
            "Like अनिलजित् (conquering anila, Vāta), what does an invented कफजित् mean?",
            ("Conquering Kapha", "-जित् at the end of a compound = conquering X."),
            [("Born of Kapha", "'Born of' would be -ज (कफज), not -जित्."),
             ("Conquered by Kapha", "-जित् is active: it conquers, it is not conquered."),
             ("Increasing Kapha", "'Increasing' would be -वर्धन, not -जित्.")],
            "-जित् (from √जि) names the conqueror: anila-jit, kapha-jit.",
            "X-जित् = X को जीतने वाला.",
            teaches="-जित् at the end of a compound means conquering: अनिलजित् = conquering Vāta, कफजित् = conquering Kapha."),
    ],
}

# ---------------------------------------------------------------- unit 52
AUTHORED["52"] = {
    "title": "जीवन्तीं मदनं मेदाम्",
    "question": "Which drugs does verse 52 list for the next oil-and-ghee anuvāsana?",
    "rule": ("Verse 52 lists, in the accusative: jīvantī, madana, medā, śrāvaṇī, madhuka and balā; "
             "then śatāhvā and ṛṣabhaka (a dual pair), kṛṣṇā, kākanāsā and śatāvarī. The verb follows in "
             "verse 53."),
    "limits": ("medā, ṛṣabhaka and kākanāsā are disputed; śrāvaṇī, madhuka and kṛṣṇā (pippalī) only "
               "probable. The verse has no verb; the list runs on into verse 53."),
    "explain_hi": ("यह श्लोक एक नए तेल-घी के द्रव्य गिनाता है, जो वात-पित्त नाशक है (श्लोक ५४)। "
                   "पहली पंक्ति: जीवन्ती यानी डोडी, मदन यानी मैनफल, मेदा नामक द्रव्य (विवादित), श्रावणी यानी सम्भवतः गोरखमुण्डी, मधुक यानी सम्भवतः मुलेठी और बला यानी बरियार। "
                   "दूसरी पंक्ति: शताह्वा और ऋषभक का द्वन्द्व (द्विवचन), कृष्णा यानी सम्भवतः पिप्पली, काकनासा और शतावरी। "
                   "क्रिया इस श्लोक में नहीं; सूची श्लोक ५३ में चलती है, जहाँ ‘पिष्ट्वा’ आता है।"),
    "hook": "जीवन्ती-मदन-मेदा-श्रावणी-मधुक-बला; सोआ-ऋषभक, कृष्णा, काकनासा, शतावरी।",
    "core": False,
    "questions": [
        mcq("pretest", 0,
            "What is मदन in verse 52, by the card?",
            ("Emetic nut (Randia dumetorum)", "मदन = madana, the emetic nut (standard)."),
            [("Liquorice root, the probable madhuka", "Liquorice is the probable madhuka, a separate item."),
             ("Long pepper (kṛṣṇā here)", "Long pepper is the probable kṛṣṇā of line 2."),
             ("Asparagus root (śatāvarī)", "Śatāvarī closes line 2; it is not madana.")],
            "Each drug has its own identification; madana is the emetic nut.",
            "मदन = मैनफल."),
        match(1, "Match each drug of verse 52 to its identification on the card.",
              [["जीवन्ती", "Leptadenia reticulata"], ["बला", "Sida cordifolia"],
               ["कृष्णा", "probably pippalī, long pepper"], ["शतावरी", "Asparagus racemosus"]],
              "Four names with the identifications (and confidence) the data gives.",
              "जीवन्ती = डोडी; बला = बरियार; कृष्णा = सम्भवतः पिप्पली; शतावरी = Asparagus."),
        order(2, "Put the drugs of line 1 of verse 52 in their order.",
              ["जीवन्ती", "मदन", "मेदा", "श्रावणी", "मधुक", "बला"],
              "Line 1 runs jīvantī, madana, medā, śrāvaṇī, madhuka, balā.",
              "जीवंतीं · मदनं · मेदां · श्रावणीं · मधुकं · बळां.",
              role="extend",
              teaches="Line 1 of verse 52: jīvantī, madana, medā, śrāvaṇī, madhuka, balā."),
        mcq("discriminate", 3, "Which split of शताह्वर्षभकौ (printed शताव्हर्षभकौ) is right?",
            ("शताह्व + ऋषभकौ", "अ + ऋ → अर्: शताह्व + ऋषभकौ = शताह्वर्षभकौ."),
            [("शताह्वा + ऋषभकौ", "आ + ऋ gives आर्: शताह्वार्षभकौ, not printed."),
             ("शताह्व + अर्षभकौ", "अ + अ gives आ: शताह्वार्षभकौ, not printed."),
             ("शताह्वर् + षभकौ", "षभक is no drug; the second member is ऋषभक.")],
            "The short अ before र्ष shows the join अ + ऋ.",
            "अ + ऋ → अर्."),
        mcq("apply", 4, "Why does शताह्वर्षभकौ end in -औ?",
            ("It is a dual: two drugs joined", "The card: a dual dvandva, śatāhvā and ṛṣabhaka."),
            [("It is a locative: in śatāhvā", "The gram label is nom./acc. dual, not locative."),
             ("It is one single drug named twice over", "A dvandva joins two different drugs."),
             ("It is a verb: they cook", "No verb stands in verse 52.")],
            "-औ here marks the dual of a dvandva of two items (check the gram label: -au is not always dual).",
            "द्वन्द्व, द्विवचन: शताह्वा और ऋषभक."),
        mcq("transfer", 5,
            "Like शताह्व + ऋषभक → शताह्वर्षभक, how do invented मधुक + ऋषभक join?",
            ("मधुकर्षभक", "अ + ऋ → अर्: मधुक + ऋषभक = मधुकर्षभक."),
            [("मधुकार्षभक", "आर् would need आ + ऋ or vṛddhi; here it is अ + ऋ."),
             ("मधुकृषभक", "The अ cannot vanish; it joins ऋ as अर्."),
             ("मधुकऋषभक", "Inside a compound अ and ऋ must join.")],
            "अ + ऋ → अर् is guṇa sandhi.",
            "अ + ऋ → अर्.",
            teaches="अ + ऋ → अर्: शताह्व + ऋषभक = शताह्वर्षभक; मधुक + ऋषभक = मधुकर्षभक."),
    ],
}

# ---------------------------------------------------------------- unit 53
AUTHORED["53"] = {
    "title": "स्वगुप्तां क्षीरकाकोलीम्",
    "question": "Which drugs close the list in verse 53, and how are oil and ghee then made?",
    "rule": ("Svaguptā, kṣīrakākolī, the (drug) named karkaṭa, śaṭhī and vacā close the list. Having "
             "ground (them), one should cook oil and ghee in milk, fourfold on the suggested reading."),
    "limits": ("caturguṇaiḥ does not agree with kṣīre (text flag; read caturguṇe), and a proofread pass "
               "questions sādhayeta: no question uses either. karkaṭākhyā only says 'named karkaṭa' "
               "(karkaṭaśṛṅgī is probable, not in the line). kṣīrakākolī is disputed. Fourfold of what is "
               "not stated."),
    "explain_hi": ("यह श्लोक श्लोक ५२ की सूची पूरी करता है: स्वगुप्ता यानी कौंच, क्षीरकाकोली (विवादित), ‘कर्कट नामक’ द्रव्य, शठी यानी सम्भवतः कपूरकचरी और वचा यानी बच। "
                   "‘कर्कटाख्या’ बस ‘कर्कट नाम वाली’ कहती है; प्रायः कर्कटशृंगी अभिप्रेत मानी जाती है, पर पंक्ति यह नहीं कहती। "
                   "फिर विधि: इन्हें पीसकर तेल और घी को दूध में पकाए। "
                   "‘चतुर्गुणैः’ का रूप ‘क्षीरे’ से मेल नहीं खाता; सुझाया पाठ ‘चतुर्गुणे’ है, यानी चौगुने दूध में।"),
    "hook": "कौंच-क्षीरकाकोली-कर्कट-शठी-बच पीसकर; तेल-घी दूध में।",
    "core": False,
    "questions": [
        mcq("pretest", 0,
            "What does verse 53 say is done to the drugs before the cooking?",
            ("They are ground (piṣṭvā)", "पिष्ट्वा = having ground."),
            [("They are burnt to ash", "No burning is named in verse 53."),
             ("They are soaked overnight", "No soaking is named in verse 53."),
             ("They are boiled to a droṇa", "Boiling to a droṇa belongs to verse 49.")],
            "The absolutive पिष्ट्वा comes before the main verb: grind, then cook.",
            "पिष्ट्वा = पीसकर."),
        match(1, "Match each drug of verse 53 to its meaning on the card.",
              [["स्वगुप्ता", "cowhage (Mucuna pruriens)"], ["वचा", "sweet flag (Acorus calamus)"],
               ["शठी", "probably Hedychium spicatum"], ["कर्कटाख्या", "the one named karkaṭa"]],
              "Three identifications and one name that the line leaves as a name.",
              "स्वगुप्ता = कौंच; वचा = बच; शठी = सम्भवतः कपूरकचरी; कर्कटाख्या = कर्कट नामक."),
        order(2, "Put the drugs of line 1 of verse 53 in their order.",
              ["स्वगुप्ता", "क्षीरकाकोली", "कर्कटाख्या", "शठी", "वचा"],
              "Line 1 runs svaguptā, kṣīrakākolī, karkaṭākhyā, śaṭhī, vacā.",
              "स्वगुप्तां · क्षीरकाकोलीं · कर्कटाख्यां · शठीं · वचां.",
              role="extend",
              teaches="Line 1 of verse 53: svaguptā, kṣīrakākolī, karkaṭākhyā, śaṭhī, vacā."),
        mcq("discriminate", 3, "What does कर्कटाख्याम् itself say, by the card?",
            ("Only: the one named karkaṭa", "The card: the line says only 'named karkaṭa'."),
            [("A real crab goes into it", "आख्या = name; it names a drug, not a crab."),
             ("It is another name of vacā", "Vacā is listed separately after śaṭhī."),
             ("It means with crab-like leaves", "Leaves are not in the word; आख्या is 'name'.")],
            "-आख्या = called, named; the identification karkaṭaśṛṅgī is outside the line.",
            "कर्कट + आख्या = कर्कट नामक."),
        mcq("apply", 4, "In what does verse 53 cook the oil and ghee?",
            ("In milk (kṣīre)", "क्षीरे = in milk (locative)."),
            [("In a vaha of water", "The vaha of water is in verse 49."),
             ("In the sour liquid", "The sour (amla) belongs to verses 51 and 61."),
             ("In cow's urine", "Urine is not named in verse 53.")],
            "The locative क्षीरे names the medium of cooking.",
            "क्षीरे = दूध में."),
        mcq("transfer", 5,
            "Like पिष्ट्वा (having ground, bare √पिष्), which is the absolutive of the bare root √पच्?",
            ("पक्त्वा", "Without a prefix the absolutive takes -त्वा: पच् → पक्त्वा."),
            [("पचेत्", "This is the optative 'should cook', a finite verb."),
             ("पक्वम्", "This is the participle 'cooked', not 'having cooked'."),
             ("पच्य", "-य is used only with a prefix, as in विपाच्य.")],
            "A bare root takes -त्वा (पिष्ट्वा, पक्त्वा); a prefixed one takes -य.",
            "धातु (उपसर्ग-रहित) → -त्वा.",
            teaches="Without a prefix the absolutive ends in -त्वा: √पिष् → पिष्ट्वा, √पच् → पक्त्वा."),
    ],
}

# ---------------------------------------------------------------- unit 54
AUTHORED["54"] = {
    "title": "बृंहणं वातपित्तघ्नम्",
    "question": "What does verse 54 say this oil-and-ghee anuvāsana does?",
    "rule": ("It is nourishing (bṛṃhaṇa), destroys Vāta and Pitta, increases strength, semen (śukra) and "
             "agni (the digestive fire), removes ailments of menstrual blood (rajas) and semen, and is "
             "the putrīya (son-related) anuvāsana."),
    "limits": ("No verb. That it describes the preparation of verses 52-53 is presumed from the sequence. "
               "agni = digestive fire, though the line says only 'fire'. How putrīya is meant is not said; "
               "it is kept literal."),
    "explain_hi": ("यह श्लोक श्लोक ५२-५३ में बने तेल-घी के गुण बताता है (क्रिया नहीं है, सम्बन्ध क्रम से माना गया)। "
                   "यह बृंहण यानी पोषण करने वाला है, वात और पित्त का नाश करता है, और बल, शुक्र तथा अग्नि यानी पाचन-शक्ति बढ़ाता है। "
                   "यह रज यानी आर्तव और शुक्र के रोग दूर करता है। "
                   "अन्त में इसे ‘पुत्रीय’ अनुवासन कहा गया, यानी पुत्र से सम्बन्धित; यह कैसे, पाठ नहीं बताता।"),
    "hook": "पोषे, वात-पित्त हरे, बल-शुक्र-अग्नि बढ़ाए, रज-शुक्र रोग हरे: पुत्रीय।",
    "core": True,
    "questions": [
        mcq("pretest", 0,
            "Which two doṣas does verse 54 say this anuvāsana destroys?",
            ("Vāta and Pitta", "वातपित्तघ्नम् = destroying Vāta and Pitta."),
            [("Vāta and Kapha", "Kapha is not named in verse 54."),
             ("Pitta and Kapha", "Kapha is not named; Vāta is."),
             ("All three doṣas", "Only two are named in the compound.")],
            "The compound vāta-pitta-ghna names exactly two doṣas.",
            "वात + पित्त + घ्न."),
        match(1, "Match each word of verse 54 to its meaning on the card.",
              [["बृंहण", "nourishing"], ["वर्धन", "increasing"], ["आमय", "ailment"], ["हर", "removing"]],
              "The four action words of the verse.",
              "बृंहण = पोषण; वर्धन = बढ़ाना; आमय = रोग; हर = हरना."),
        order(2, "Put the phrases of verse 54 in their order.",
              ["बृंहणं", "वातपित्तघ्नं", "बलशुक्राग्निवर्द्धनं", "रजःशुक्रामयहरं", "पुत्रीयं चानुवासनं"],
              "Nourishing, doṣa-destroying, increasing, removing, then the name.",
              "बृंहण · वात-पित्त-घ्न · बल-शुक्र-अग्नि-वर्धन · रज-शुक्र-आमय-हर · पुत्रीय अनुवासन.",
              role="extend",
              teaches="Verse 54 lists the effects in order: nourishing, against Vāta and Pitta, increasing strength-semen-fire, removing rajas-semen ailments, putrīya."),
        multi("discriminate", 3, "Which of these does verse 54 say the anuvāsana increases?",
              [("बल (strength)", "First member of bala-śukra-agni-vardhana."),
               ("शुक्र (semen)", "Second member of the same compound."),
               ("अग्नि (digestive fire)", "Third member of the same compound."),
               ("कफ (Kapha)", "Kapha is not named in verse 54."),
               ("मेदस् (body fat)", "Body fat is not named in verse 54.")],
              [0, 1, 2],
              "Only the three members before -वर्धन are increased.",
              "बल + शुक्र + अग्नि + वर्धन."),
        mcq("apply", 4, "In रजःशुक्रामयहरम्, what does रजस् mean here, by the card?",
            ("Menstrual blood", "The card: rajas is taken as menstrual blood in this setting."),
            [("Dust or dirt", "Dust is a common sense of rajas, but not the one here."),
             ("The mind's quality rajas", "That sense does not fit 'ailments of rajas and semen'."),
             ("Pollen of flowers", "Pollen is not meant; the pair is rajas and śukra.")],
            "Paired with śukra (semen), rajas is the female counterpart: menstrual blood.",
            "रजस् = आर्तव (यहाँ)."),
        mcq("transfer", 5,
            "Like बलशुक्राग्निवर्धनम् (increasing strength, semen, fire), what does an invented मेधावर्धनम् mean?",
            ("Increasing intelligence", "-वर्धन at the end of a compound = increasing X."),
            [("Destroying intelligence", "'Destroying' would be -घ्न, as in वातपित्तघ्न."),
             ("Removing ailments of it", "'Removing' would be -हर, as in आमयहर."),
             ("Born of intelligence", "'Born of' would be -ज, not -वर्धन.")],
            "-वर्धन increases, -घ्न destroys, -हर removes.",
            "X-वर्धन = X को बढ़ाने वाला.",
            teaches="At the end of a compound -वर्धन means increasing (बलवर्धन, मेधावर्धन), -घ्न destroying, -हर removing."),
    ],
}

# ---------------------------------------------------------------- unit 55
AUTHORED["55"] = {
    "title": "शिशिरस्पर्शवीर्यैः",
    "question": "How does verse 55 make the Pitta-destroying anuvāsana?",
    "rule": ("With ground (drugs) cold in touch and potency (vīrya), in fourfold milk, ghee having oil as "
             "a quarter (tailapāda) is cooked: an anuvāsana that destroys Pitta."),
    "limits": ("The drugs are not named, only described as cold. śiśira may go with both touch and "
               "potency or the phrase may be read 'having cold touch and potency' (two-way). A quarter of "
               "what, and fourfold of what, are not stated (understood: of the ghee). No verb."),
    "explain_hi": ("यह श्लोक पित्त के लिए अनुवासन बताता है। "
                   "द्रव्यों का नाम नहीं, केवल गुण: वे स्पर्श में और वीर्य यानी शक्ति में शीतल हों, और पिसे हुए हों। "
                   "इन्हें चौगुने दूध में डालकर ऐसा घी पकाया जाए जिसमें तेल एक चौथाई हो: ‘तैलपाद’। "
                   "यह अनुवासन पित्त का नाश करता है। "
                   "चौथाई और चौगुना किसके अनुपात में, पंक्ति नहीं कहती; घी का माना जाता है।"),
    "hook": "ठण्डे पिसे द्रव्य, चौगुना दूध, घी में चौथाई तेल: पित्त-घ्न।",
    "core": True,
    "questions": [
        mcq("pretest", 0,
            "Which doṣa does the anuvāsana of verse 55 destroy?",
            ("Pitta", "पित्तघ्नम् = destroying Pitta."),
            [("Vāta", "Vāta oils were verses 47-51; verse 55 names Pitta."),
             ("Kapha", "Kapha oils follow from verse 56."),
             ("Rakta", "Blood is not named in verse 55.")],
            "The last line says it plainly: pitta-ghnam anuvāsanam.",
            "पित्तघ्न = पित्त-नाशक."),
        match(1, "Match each word of verse 55 to its meaning on the card.",
              [["शिशिर", "cold"], ["स्पर्श", "touch"], ["वीर्य", "potency"], ["पाद", "a quarter"]],
              "The three words of the drug description and the share of oil.",
              "शिशिर = शीतल; स्पर्श = छूना; वीर्य = शक्ति; पाद = चौथाई."),
        order(2, "Put the phrases of verse 55 in their order.",
              ["शिशिरस्पर्शवीर्यैश्च", "पिष्टैः", "क्षीरे चतुर्गुणे", "तैलपादं घृतं सिद्धं", "पित्तघ्नमनुवासनं"],
              "Cold drugs, ground, in fourfold milk; the ghee; then its use.",
              "शीतल द्रव्य · पिसे · चौगुने दूध में · चौथाई-तेल घी · पित्त-घ्न अनुवासन.",
              role="extend",
              teaches="Verse 55: cold drugs, ground, in fourfold milk; ghee with a quarter of oil; a Pitta-destroying anuvāsana."),
        mcq("discriminate", 3, "What does तैलपादं घृतम् mean on the card?",
            ("Ghee with oil as a quarter", "तैल-पाद = having oil as a quarter; the noun is ghee."),
            [("Oil with ghee as a quarter", "The quarter is oil (तैल-पाद), the base is ghee."),
             ("Only a quarter of the oil", "The ghee is the main item; oil is its quarter."),
             ("Oil and ghee, equal parts", "पाद means a quarter, not an equal share.")],
            "In a bahuvrīhi तैलपाद the ghee has oil as its quarter.",
            "तैलपाद घृत = जिसमें तेल चौथाई हो, ऐसा घी."),
        mcq("apply", 4, "Which drugs does verse 55 itself name for this anuvāsana?",
            ("None by name; only cold ones", "The card: the drugs are unstated, described as cold in touch and potency."),
            [("Jīvantī, madana and medā", "Those are in verse 52, a different preparation."),
             ("Śatāhvā, yava and bilva", "Those cook the Vāta oil of verse 51."),
             ("The jīvanīya group of ten", "Jīvanīya is named in verses 49-50, not here.")],
            "Verse 55 chooses drugs by a property (cold), not by name.",
            "शिशिरस्पर्शवीर्य = गुण से चुने द्रव्य."),
        mcq("transfer", 5,
            "Like वीर्यैः + च → वीर्यैश्च, how do invented पिष्टैः + च join?",
            ("पिष्टैश्च", "Visarga before च becomes श्."),
            [("पिष्टैर्च", "र् comes before voiced sounds; च is unvoiced."),
             ("पिष्टैच", "The visarga does not drop before च."),
             ("पिष्टैस्च", "स् comes before त/थ; before च it is श्.")],
            "ः + च → श्च, as in शिशिरस्पर्शवीर्यैश्च.",
            "ः + च/छ → श्.",
            teaches="Visarga before च becomes श्: वीर्यैः + च = वीर्यैश्च; पिष्टैः + च = पिष्टैश्च."),
    ],
}

# ---------------------------------------------------------------- unit 56
AUTHORED["56"] = {
    "title": "सैन्धवं मदनं कुष्ठम्",
    "question": "Which drugs open the Kapha oil list in verse 56?",
    "rule": ("Verse 56 opens a list (nominative): rock salt (saindhava), madana, kuṣṭha (the drug costus), "
             "śatāhvā, nicula, vacā; then hrīvera, madhuka, bhārgī, devadāru, together with kaṭphala. "
             "The oil made with them is named in verse 58."),
    "limits": ("Printed nicalo is read nicula (doubtful, disputed drug) and hrībera as hrīvera: no question "
               "uses either. kuṣṭha here is the drug, not the skin disease. That these drugs feed the oil "
               "of verse 58 is presumed; this verse has no verb."),
    "explain_hi": ("यहाँ से कफहर अनुवासन का प्रकरण है, और यह श्लोक उसकी लम्बी सूची शुरू करता है (सूची श्लोक ५८ तक चलती है)। "
                   "पहली पंक्ति: सैन्धव यानी सेंधा नमक, मदन यानी मैनफल, कुष्ठ नामक औषध यानी कूठ, शताह्वा यानी सोआ, निचुल और वचा यानी बच। "
                   "दूसरी पंक्ति: ह्रीवेर यानी सुगन्धबाला, मधुक, भार्गी, देवदारु यानी देवदार, और कट्फल यानी कायफल ‘सहित’। "
                   "यहाँ ‘कुष्ठ’ त्वचा-रोग नहीं, औषध है। "
                   "छपा ‘निचलो’ निचुल पढ़ा गया, यह अनिश्चित है।"),
    "hook": "सेंधा-मैनफल-कूठ-सोआ-निचुल-बच; सुगन्धबाला-मधुक-भारंगी-देवदार-कायफल।",
    "core": False,
    "questions": [
        mcq("pretest", 0,
            "What is कुष्ठ in verse 56, by the card?",
            ("The drug costus", "Here kuṣṭha is the drug (Saussurea costus), not the disease."),
            [("The skin disease", "In a drug list kuṣṭha is the drug; the card says so."),
             ("A rock salt", "Rock salt is saindhava, the first item."),
             ("A weight measure", "No measure is given in verse 56.")],
            "In a list of drugs, kuṣṭha names the costus root.",
            "कुष्ठ (औषध) = कूठ."),
        match(1, "Match each drug of verse 56 to its meaning on the card.",
              [["सैन्धव", "rock salt"], ["देवदारु", "Himalayan cedar"], ["वचा", "sweet flag"],
               ["कट्फल", "box myrtle (Myrica esculenta)"]],
              "Four clear items of the list.",
              "सैन्धव = सेंधा नमक; देवदारु = देवदार; वचा = बच; कट्फल = कायफल."),
        order(2, "Put these drugs of line 1 of verse 56 in their order.",
              ["सैन्धव", "मदन", "कुष्ठ", "शताह्वा", "वचा"],
              "Line 1 runs saindhava, madana, kuṣṭha, śatāhvā, (nicula), vacā.",
              "सैंधवं · मदनं · कुष्ठं · शताव्हा · (निचुल) · वचा.",
              role="extend",
              teaches="Line 1 of verse 56: saindhava, madana, kuṣṭha, śatāhvā, nicula, vacā."),
        multi("discriminate", 3, "Which of these does verse 56 name?",
              [("देवदारु", "Named in line 2."),
               ("सैन्धव", "Opens line 1."),
               ("मधुक", "Named in line 2."),
               ("नागर", "Nāgara (dry ginger) opens verse 57."),
               ("दन्ती", "Dantī comes in verse 58.")],
              [0, 1, 2],
              "The list runs over three verses; count only what verse 56 prints.",
              "Count as listed only what the verse names."),
        mcq("apply", 4, "What does सकट्फलम् mean, by the card?",
            ("Together with kaṭphala", "स- = with: sa-kaṭphalam = with kaṭphala."),
            [("Without any kaṭphala", "'Without' would be निः- or अ-, not स-."),
             ("Only kaṭphala's fruit", "स- adds kaṭphala; it does not pick a part."),
             ("Kaṭphala as one quarter", "No quarter is named in verse 56.")],
            "The prefix स- in a bahuvrīhi means 'together with'.",
            "स- = सहित."),
        mcq("transfer", 5,
            "Like सकट्फलम् (together with kaṭphala), what does an invented ससैन्धवम् mean?",
            ("Together with rock salt", "स- + सैन्धव = with rock salt."),
            [("Without any rock salt", "स- adds; it does not take away."),
             ("Instead of rock salt", "स- does not mean 'instead of'."),
             ("Like rock salt in taste", "स- here is 'with', not 'like'.")],
            "स- at the head of a bahuvrīhi = together with X.",
            "स + X = X सहित.",
            teaches="स- at the start of a bahuvrīhi means together with: सकट्फलम् = with kaṭphala, ससैन्धवम् = with rock salt."),
    ],
}

# ---------------------------------------------------------------- unit 57
AUTHORED["57"] = {
    "title": "नागरं पुष्करं मेदा",
    "question": "Which drugs does verse 57 add to the Kapha oil list?",
    "rule": ("Verse 57 continues the list: nāgara (dry ginger), puṣkara, medā, cavikā, citraka, śaṭhī; "
             "then viḍaṅga and ativiṣā (a dual pair), śyāmā, hareṇu, nīlinī (indigo) and sthirā."),
    "limits": ("medā, śyāmā and hareṇu are disputed; puṣkara, cavikā and sthirā only probable. No verb: "
               "the list runs on into verse 58."),
    "explain_hi": ("यह श्लोक कफहर तेल की सूची आगे बढ़ाता है। "
                   "पहली पंक्ति: नागर यानी सोंठ, पुष्कर यानी सम्भवतः पुष्करमूल, मेदा नामक द्रव्य, चविका यानी सम्भवतः चव्य, चित्रक यानी चीता और शठी। "
                   "दूसरी पंक्ति: विडंग और अतिविषा यानी अतीस (द्विवचन का जोड़ा), श्यामा, हरेणु, नीलिनी यानी नील और स्थिरा यानी सम्भवतः शालपर्णी। "
                   "श्यामा, हरेणु और मेदा की पहचान विवादित है। "
                   "क्रिया अभी नहीं आई; सूची श्लोक ५८ में पूरी होती है।"),
    "hook": "सोंठ-पुष्कर-मेदा-चव्य-चीता-शठी; विडंग-अतीस, श्यामा, हरेणु, नील, स्थिरा।",
    "core": False,
    "questions": [
        mcq("pretest", 0,
            "What is नागर in verse 57, by the card?",
            ("Dry ginger (śuṇṭhī)", "नागर = dry ginger (standard)."),
            [("Long pepper (kṛṣṇā)", "Long pepper is kṛṣṇā of verse 52."),
             ("The lotus (puṣkara)", "Lotus is a sense of puṣkara, the next item."),
             ("Indigo plant (nīlinī)", "Indigo is nīlinī, in line 2.")],
            "nāgara opens the line: dry ginger.",
            "नागर = सोंठ."),
        match(1, "Match each drug of verse 57 to its identification on the card.",
              [["चित्रक", "leadwort (Plumbago zeylanica)"], ["विडङ्ग", "Embelia ribes"],
               ["अतिविषा", "Aconitum heterophyllum"], ["नीलिनी", "indigo"]],
              "Four standard identifications of the verse.",
              "चित्रक = चीता; विडङ्ग = Embelia; अतिविषा = अतीस; नीलिनी = नील."),
        order(2, "Put the drugs of line 1 of verse 57 in their order.",
              ["नागर", "पुष्कर", "मेदा", "चविका", "चित्रक", "शठी"],
              "Line 1 runs nāgara, puṣkara, medā, cavikā, citraka, śaṭhī.",
              "नागरं · पुष्करं · मेदा · चविका · चित्रकः · शठी.",
              role="extend",
              teaches="Line 1 of verse 57: nāgara, puṣkara, medā, cavikā, citraka, śaṭhī."),
        mcq("discriminate", 3, "Which split of विडंगातिविषे is right?",
            ("विडङ्ग + अतिविषे", "अ + अ → आ: विडङ्ग + अतिविषे = विडङ्गातिविषे."),
            [("विडङ्ग + तिविषे", "No vowel would join: that gives विडङ्गतिविषे."),
             ("विडङ्गे + अतिविषे", "ए + अ gives एऽ: विडङ्गेऽतिविषे."),
             ("विडङ्ग + इतिविषे", "अ + इ gives ए: विडङ्गेतिविषे.")],
            "The long आ after ङ्ग shows अ + अ.",
            "अ + अ → आ."),
        mcq("apply", 4, "What is स्थिरा in verse 57, by the card?",
            ("Probably śālaparṇī, not certain", "The card tags sthirā = śālaparṇī as probable."),
            [("Certainly śālaparṇī, standard", "The data says probable, not standard."),
             ("Indigo (Indigofera tinctoria)", "Indigo is nīlinī, the item before it."),
             ("Leadwort (Plumbago zeylanica)", "Leadwort is citraka of line 1.")],
            "Keep the confidence word with the identification.",
            "स्थिरा = सम्भवतः शालपर्णी."),
        mcq("transfer", 5,
            "Like हरेणुः + नीलिनी → हरेणुर्नीलिनी, how do invented गुरुः + नमति join?",
            ("गुरुर्नमति", "उः before a voiced sound (न) becomes उर्."),
            [("गुरो नमति", "ओ arises from अः, not from उः."),
             ("गुरु नमति", "The visarga after उ is not dropped before न."),
             ("गुरुन्नमति", "No न् is doubled; the visarga becomes र्.")],
            "Visarga after a vowel other than अ/आ becomes र् before a voiced sound.",
            "इः/उः + सघोष → इर्/उर्.",
            teaches="After उ (or इ) a visarga before a voiced sound becomes र्: हरेणुः + नीलिनी = हरेणुर्नीलिनी; गुरुः + नमति = गुरुर्नमति."),
    ],
}

# ---------------------------------------------------------------- unit 58
AUTHORED["58"] = {
    "title": "बिल्वाजमोदे चपला",
    "question": "Which drugs close the Kapha list in verse 58, and which oil is prepared with them?",
    "rule": ("Bilva and ajamodā, capalā, dantī and rāsnā (close the list). With those, equal (ones), "
             "castor oil (airaṇḍa-taila) or (another) oil is to be prepared: it removes diseases of Kapha."),
    "limits": ("taiḥ samaiḥ is probably 'in equal parts', but 'parts' is not in the Sanskrit. capalā and "
               "rāsnā are disputed, ajamodā probable. That 'those' are the drugs of verses 56-58 is "
               "presumed."),
    "explain_hi": ("यह श्लोक कफहर सूची पूरी करता है: बिल्व और अजमोदा (द्विवचन का जोड़ा), चपला, दन्ती यानी जंगली जमालगोटा और रास्ना। "
                   "फिर ‘तैः समैः’ यानी उन समानों से, सम्भवतः बराबर भागों में (‘भाग’ शब्द पाठ में नहीं)। "
                   "उनसे एरण्ड-तेल यानी अरंडी का तेल, या कोई तेल, साधित किया जाए। "
                   "वह ‘कफरोगनुत्’ है, यानी कफ के रोग दूर करता है।"),
    "hook": "बेल-अजमोद-चपला-दन्ती-रास्ना बराबर; अरंडी या कोई तेल: कफ-रोग दूर।",
    "core": False,
    "questions": [
        mcq("pretest", 0,
            "Which diseases does the oil of verse 58 remove?",
            ("Diseases of Kapha", "कफरोगनुत् = removing diseases of Kapha."),
            [("Diseases of Pitta", "Pitta was the target of verse 55."),
             ("All Vāta disorders", "That was said of the oil in verse 50."),
             ("Ailments of semen", "Semen ailments were named in verse 54.")],
            "The last compound names the target: kapha-roga-nud.",
            "कफ-रोग-नुद् = कफ रोग दूर करने वाला."),
        match(1, "Match each word of verse 58 to its meaning on the card.",
              [["दन्ती", "Baliospermum montanum"], ["अजमोदा", "probably Trachyspermum roxburghianum"],
               ["एरण्डतैल", "castor oil"], ["समैः", "equal (ones)"]],
              "Two drugs, the oil, and the word for the proportion.",
              "दन्ती = जंगली जमालगोटा; अजमोदा = सम्भवतः अजमोद; एरण्डतैल = अरंडी का तेल; समैः = समान."),
        order(2, "Put the phrases of verse 58 in their order.",
              ["बिल्वाजमोदे चपला", "दंती रास्ना च तैः समैः", "साध्यमैरंडतैलं वा", "तैलं वा कफरोगनुत्"],
              "The last drugs, the equal share, the castor oil or oil, then its use.",
              "बिल्व-अजमोदा, चपला · दन्ती, रास्ना, समान · एरण्ड-तेल या · तेल, कफ-रोग-नाशक.",
              role="extend",
              teaches="Verse 58 ends the Kapha list and says: with those, equal, castor oil or oil is prepared; it removes Kapha diseases."),
        mcq("discriminate", 3, "What does तैः समैः mean, by the card?",
            ("With those, equal (ones)", "The card: with those, equal; probably 'in equal parts'."),
            [("With those, cooked twice", "No second cooking is named; समैः is 'equal'."),
             ("With those, half the oil", "No half is named; समैः is 'equal'."),
             ("Without those, oil alone", "तैः is instrumental 'with those', not 'without'.")],
            "सम = equal; 'parts' is understood, not printed.",
            "तैः समैः = उन समानों से."),
        mcq("apply", 4, "Which oil does verse 58 allow to be prepared?",
            ("Castor oil, or (another) oil", "साध्यम् एरण्डतैलं वा तैलं वा = castor oil or oil."),
            [("Only sesame oil, never castor", "Castor oil is named first; sesame is not named."),
             ("Ghee with a quarter of oil", "That is the Pitta anuvāsana of verse 55."),
             ("Fat of the marsh-dwellers", "Marsh-animal fat is in verse 50.")],
            "वा … वा offers two choices: castor oil or another oil.",
            "एरण्डतैलं वा तैलं वा."),
        mcq("transfer", 5,
            "Like एरण्डतैलं वा तैलं वा, what does an invented घृतं वा तैलं वा पिबेत् mean?",
            ("He may drink either ghee or oil", "वा … वा = either … or."),
            [("He should drink both together", "Both together would use च, not वा."),
             ("He should drink neither of them", "'Neither' would need न; वा offers a choice."),
             ("He drinks ghee, but never oil", "वा … वा keeps both open as choices.")],
            "Each वा follows one of the alternatives.",
            "X वा Y वा = X या Y.",
            teaches="वा … वा after two words means either … or: एरण्डतैलं वा तैलं वा (castor oil or oil); घृतं वा तैलं वा."),
    ],
}

# ---------------------------------------------------------------- unit 59
AUTHORED["59"] = {
    "title": "वर्ध्मोदावर्तगुल्मार्शः",
    "question": "Which disorders does verse 59 say that anuvāsana quickly destroys?",
    "rule": ("That anuvāsana would quickly destroy vardhma (probably scrotal swelling), udāvarta, gulma, "
             "arśas (haemorrhoids), splenic disorder and meha, together with wind (māruta), and also ānāha "
             "and aśmarī (urinary stone)."),
    "limits": ("The modern name for meha (the prameha group) is an open point: no question uses it. "
               "vardhma is probable (hernia or hydrocele). How exactly samārutān (with wind) is meant is "
               "not explained. 'That' anuvāsana is presumably the oil of verse 58."),
    "explain_hi": ("यह श्लोक कफहर तेल (श्लोक ५८) के अनुवासन का फल बताता है। "
                   "वह शीघ्र नष्ट करे: वर्ध्म यानी सम्भवतः अण्डवृद्धि, उदावर्त यानी वायु का उलटा चलना, गुल्म यानी पेट की गाँठ, अर्श यानी बवासीर, प्लीहा का रोग और मेह यानी मूत्र के रोग, वायु सहित। "
                   "साथ में आनाह यानी मल-वायु रुककर पेट फूलना और अश्मरी यानी पथरी। "
                   "‘हन्यात्’ विधिलिङ् है: नष्ट कर दे। "
                   "मेह का आधुनिक नाम अभी खुला प्रश्न है।"),
    "hook": "वर्ध्म-उदावर्त-गुल्म-अर्श-प्लीहा-मेह, आनाह-अश्मरी: शीघ्र नष्ट।",
    "core": True,
    "questions": [
        mcq("pretest", 0,
            "How fast does verse 59 say that anuvāsana destroys these disorders?",
            ("Quickly (āśu)", "चाशु = च + आशु, and quickly."),
            [("Slowly, in a month", "No month is named in verse 59."),
             ("After seven doses", "No number of doses is named."),
             ("Only after fasting", "No fasting is named in verse 59.")],
            "आशु = quickly; it qualifies हन्यात्.",
            "आशु हन्यात् = शीघ्र नष्ट करे."),
        match(1, "Match each disorder of verse 59 to its meaning on the card.",
              [["उदावर्त", "reversed movement of wind"], ["गुल्म", "abdominal lump"],
               ["अर्शस्", "haemorrhoids"], ["अश्मरी", "urinary stone"]],
              "Four disorders with the senses the data gives.",
              "उदावर्त = वायु उलटा; गुल्म = गाँठ; अर्शस् = बवासीर; अश्मरी = पथरी."),
        order(2, "Put these disorders in the order of verse 59.",
              ["वर्ध्म", "उदावर्त", "गुल्म", "अर्शस्", "आनाह", "अश्मरी"],
              "Line 1 runs vardhma, udāvarta, gulma, arśas (spleen, meha); line 2 ānāha, aśmarī.",
              "वर्ध्म · उदावर्त · गुल्म · अर्शः · (प्लीहा · मेह) ‖ आनाह · अश्मरी.",
              role="extend",
              teaches="The anuvāsana of verse 59 destroys vardhma, udāvarta, gulma, arśas, spleen disorder, meha, then ānāha and aśmarī."),
        multi("discriminate", 3, "Which of these does verse 59 name?",
              [("आनाह (distension)", "Named in line 2."),
               ("अश्मरी (urinary stone)", "Named in line 2."),
               ("गुल्म (abdominal lump)", "Named in the compound of line 1."),
               ("ज्वर (fever)", "Fever is not in verse 59."),
               ("कास (cough)", "Cough is not in verse 59.")],
              [0, 1, 2],
              "Only disorders printed in the verse count.",
              "Count as listed only what the verse names."),
        mcq("apply", 4, "Which split of हन्यात्तदनुवासनं is right?",
            ("हन्यात् + तत् + अनुवासनम्", "त् + त → त्त; तत् + अ → तद (voiced before a vowel)."),
            [("हन्या + तत् + अनुवासनम्", "That would give हन्यातद-, with a single त."),
             ("हन्यात् + तत + अनुवासनम्", "तत + अ would give ता: हन्यात्तता- is not printed."),
             ("हन्यात् + तद् + नुवासनम्", "तद् + न gives तन्न, and नुवासन is no word.")],
            "हन्यात् keeps its त् before त; तत् becomes तद् before the vowel अ.",
            "हन्यात् + तत् + अनुवासनम् = हन्यात्तदनुवासनम्."),
        mcq("transfer", 5,
            "Like हन्यात् (would destroy, optative of √हन्), which invented form means would go, from √गम्?",
            ("गच्छेत्", "The optative 3rd singular of √गम् is गच्छेत्."),
            [("गच्छति", "This is the present, 'goes'."),
             ("गमिष्यति", "This is the future, 'will go'."),
             ("गत्वा", "This is the absolutive, 'having gone'.")],
            "हन्यात्, गच्छेत्, पचेत्: optatives say what would or should happen.",
            "विधिलिङ् = चाहिए / कर दे.",
            teaches="The optative states what would or should happen: हन्यात् (would destroy), गच्छेत् (would go)."),
    ],
}

# ---------------------------------------------------------------- unit 60
AUTHORED["60"] = {
    "title": "साधितं पञ्चमूलेन",
    "question": "Which further Kapha-removing anuvāsana does verse 60 offer?",
    "rule": ("Oil prepared with the five roots (pañcamūla), or with bilva and the rest (bilvādi), is an "
             "anuvāsana removing phlegm (śleṣman); or (one prepared) with substances that destroy Kapha."),
    "limits": ("The five roots and the members of bilvādi are not named. The verse is elliptical: "
               "'prepared' is read with both instruments, and no verb is given in line 2."),
    "explain_hi": ("यह श्लोक कफ के लिए और विकल्प देता है। "
                   "पञ्चमूल यानी पाँच जड़ों के समूह से साधित तेल, अथवा बिल्व यानी बेल आदि से साधित तेल। "
                   "यह अनुवासन श्लेष्म यानी कफ को हरता है। "
                   "या फिर कफ का नाश करने वाले किसी भी द्रव्य से बना अनुवासन। "
                   "पाँच जड़ें कौन सी हैं और ‘बिल्वादि’ में क्या-क्या है, यह श्लोक नहीं बताता।"),
    "hook": "पञ्चमूल या बेल-आदि से तेल; या कोई कफ-घाती द्रव्य: कफहर अनुवासन।",
    "core": True,
    "questions": [
        mcq("pretest", 0,
            "With what is the oil of verse 60 first prepared?",
            ("The five roots (pañcamūla)", "साधितं पञ्चमूलेन = prepared with the five roots."),
            [("The ten roots (daśamūla)", "Daśamūla opened the Vāta oil of verse 47."),
             ("Fruits in eightfold sour", "Fruits and sour are in verse 61."),
             ("Cold drugs in fourfold milk", "That was the Pitta ghee of verse 55.")],
            "pañca = five: a group of five roots, not ten.",
            "पञ्चमूल = पाँच जड़ों का समूह."),
        match(1, "Match each word of verse 60 to its meaning on the card.",
              [["पञ्चमूल", "a group of five roots"], ["बिल्वादि", "bilva and the rest"],
               ["श्लेष्मन्", "phlegm (Kapha)"], ["घातिन्", "destroying"]],
              "The two groups, the target and the action word.",
              "पञ्चमूल = पाँच जड़ें; बिल्वादि = बेल आदि; श्लेष्मन् = कफ; घातिन् = नाशक."),
        order(2, "Put the phrases of verse 60 in their order.",
              ["साधितं पंचमूलेन", "तैलं बिल्वादिना", "अनुवासनं श्लेष्महरं", "द्रव्यैर्वा कफघातिभिः"],
              "Five roots, or bilvādi; the anuvāsana's action; or other Kapha-destroying substances.",
              "पञ्चमूल से साधित · तेल, या बिल्वादि से · श्लेष्म-हर अनुवासन · या कफ-घाती द्रव्यों से.",
              role="extend",
              teaches="Verse 60: oil with pañcamūla or bilvādi is a phlegm-removing anuvāsana; or one with any Kapha-destroying substances."),
        mcq("discriminate", 3, "What does बिल्वादिना mean, by the card?",
            ("With bilva and the rest", "बिल्व + आदि = bilva and the rest (instrumental)."),
            [("With bilva alone, nothing else", "आदि adds 'and the rest'."),
             ("Before bilva is put in", "आदि here is 'and so on', not 'before'."),
             ("With the first part of bilva", "आदि is not a part of the fruit here.")],
            "-आदि closes an open group named by its first member.",
            "बिल्वादि = बेल आदि."),
        mcq("apply", 4, "A physician has neither pañcamūla nor bilvādi. What does verse 60 still allow?",
            ("Kapha-destroying substances", "द्रव्यैर्वा कफघातिभिः = or with Kapha-destroying substances."),
            [("Only a nirūha with urine", "Verse 60 offers an anuvāsana option, not only nirūha."),
             ("Ghee with a quarter of oil", "That is the Pitta anuvāsana of verse 55."),
             ("No anuvāsana at all", "The third option keeps the anuvāsana possible.")],
            "The last वा opens a general choice: any Kapha-destroying drug.",
            "द्रव्यैः वा कफघातिभिः."),
        mcq("transfer", 5,
            "Like कफघातिभिः (by Kapha-destroying ones), what does an invented विषघाती mean?",
            ("Destroying poison", "-घातिन् (nom. -घाती) = destroying X."),
            [("Born of poison", "'Born of' would be -ज, not -घातिन्."),
             ("Struck by poison", "-घातिन् is active: it strikes, it is not struck."),
             ("Increasing poison", "'Increasing' would be -वर्धन.")],
            "-घातिन् from √हन्, 'to strike, kill': the one who destroys.",
            "X-घातिन् = X का नाशक.",
            teaches="-घातिन् at the end of a compound means destroying: कफघातिन् = Kapha-destroying, विषघातिन् (nom. विषघाती) = poison-destroying."),
    ],
}

# ---------------------------------------------------------------- unit 61
AUTHORED["61"] = {
    "title": "फलैरष्टगुणे चाम्ले",
    "question": "What does verse 61 give for Kapha, and what for pain with distension?",
    "rule": ("In Kapha: an anvāsana (= anuvāsana, oil enema) cooked with fruits and in the eightfold sour "
             "(amla). In pain (śūla) and distension (ānāha): a nirūha (decoction enema) joined with that."),
    "limits": ("Low confidence. What is eightfold, and the noun of 'sour', are not stated. paiṭumūtravān "
               "is not a word: 'with salt (paṭu) and urine' is only a conjectural reading, so no question "
               "uses it. What tadyukta (joined with that) refers to is not certain. No main verb."),
    "explain_hi": ("यह श्लोक दो उपाय देता है। "
                   "कफ में: फलों के साथ और आठ गुने अम्ल यानी खट्टे में पकाया गया अन्वासन (अनुवासन का ही दूसरा रूप)। "
                   "शूल और आनाह यानी पेट फूलने में: ‘तद्युक्त’ यानी उससे युक्त निरूह। "
                   "छपा ‘पैटुमूत्रवान्’ कोई शब्द नहीं; अनुमानित पाठ के अनुसार यह सम्भवतः पटु यानी नमक और मूत्र वाला निरूह है। "
                   "किस वस्तु का आठ गुना, यह भी पंक्ति नहीं कहती।"),
    "hook": "कफ में फल-अम्ल का अन्वासन; शूल-आनाह में उससे युक्त निरूह।",
    "core": False,
    "questions": [
        mcq("pretest", 0,
            "In which condition does verse 61 use the anvāsana cooked with fruits?",
            ("In Kapha (kaphe)", "सिद्धमन्वासनं कफे = the cooked anvāsana, in Kapha."),
            [("In Pitta", "Pitta is not named in verse 61."),
             ("In fever", "Fever is not named in verse 61."),
             ("In pain and distension", "Those get the nirūha of line 2.")],
            "Each remedy has its locative: कफे for the anvāsana, शूलानाहे for the nirūha.",
            "कफे = कफ में."),
        match(1, "Match each word of verse 61 to its meaning on the card.",
              [["अन्वासन", "oil enema (= anuvāsana)"], ["निरूह", "decoction enema"],
               ["शूल", "pain"], ["आनाह", "distension"]],
              "Two enemas and the two troubles of line 2.",
              "अन्वासन = अनुवासन; निरूह = क्वाथ-बस्ति; शूल = पीड़ा; आनाह = पेट फूलना."),
        order(2, "Put the phrases of verse 61 in their order.",
              ["फलैरष्टगुणे चाम्ले", "सिद्धमन्वासनं कफे", "शूलानाहे तु", "तद्युक्तो निरूहः"],
              "First the anvāsana and its condition, then the nirūha and its condition.",
              "फल और अठगुना अम्ल · सिद्ध अन्वासन, कफ में · शूल-आनाह में · उससे युक्त निरूह.",
              role="extend",
              teaches="Verse 61: in Kapha an anvāsana cooked with fruits in eightfold sour; in pain and distension a nirūha joined with that."),
        mcq("discriminate", 3, "Which enema does verse 61 give for pain and distension?",
            ("A nirūha joined with that", "शूलानाहे तु तद्युक्तो निरूहः."),
            [("An anvāsana of fruits only", "The anvāsana is for Kapha, in line 1."),
             ("A sharp nirūha with milk", "Milk is not named in verse 61."),
             ("No enema, only a drink", "A nirūha, an enema, is named.")],
            "तु (but) turns to the second condition and its own remedy.",
            "शूल-आनाह → तद्युक्त निरूह."),
        mcq("apply", 4, "Does verse 61 say what is eightfold?",
            ("No; the noun is not stated", "The card: what is eightfold is not stated."),
            [("Yes; eight kinds of fruit", "अष्टगुणे is with अम्ले, not a count of fruits."),
             ("Yes; eight pala of oil", "No pala is named in verse 61."),
             ("Yes; eight parts of urine", "Urine rests on a conjectural reading, not this word.")],
            "अष्टगुणे अम्ले is literally 'in the eightfold sour'; the measure is left open.",
            "अष्टगुण = आठ गुना (किसका, अनुक्त)."),
        mcq("transfer", 5,
            "Like शूल + आनाहे → शूलानाहे, how do invented ज्वर + आनाहे join?",
            ("ज्वरानाहे", "अ + आ → आ: ज्वर + आनाहे = ज्वरानाहे."),
            [("ज्वरेनाहे", "ए comes from अ + इ, not from अ + आ."),
             ("ज्वरोनाहे", "ओ comes from अ + उ, not from अ + आ."),
             ("ज्वरआनाहे", "Inside a compound अ and आ must merge.")],
            "अ + आ merge into one long आ.",
            "अ + आ → आ.",
            teaches="अ + आ → आ: शूल + आनाहे = शूलानाहे; ज्वर + आनाहे = ज्वरानाहे."),
    ],
}


NOTES_HI = {
    "47": ("विश्वास: निम्न। दूसरी पंक्ति का लम्बा समास बिगड़ा है (text_flags): ‘गुडूच्यैंरंड’ में अतिरिक्त अनुस्वार, गुडूची + ऐरण्ड पढ़ा गया (गुडूची + एरण्ड से ‘-येरण्ड’ बनता, ‘-यैरण्ड’ नहीं); छपा ‘शेरिष’ ज्ञात द्रव्य नहीं, ‘शिरीष’ सुझाया गया। इन दो सदस्यों पर प्रश्न नहीं बना; गुडूची, भार्गी स्पष्ट हैं। "
           "भूतीक की पहचान विवादित, नहीं जोड़ी गई। रास्ना विवादित (Pluchea lanceolata, Alpinia galanga आदि)। "
           "खुला अवलोकन (05.05.92): दशमूल की दस जड़ों की सूची केवल notes में है, शब्दावली प्रविष्टि का सुझाव; इस पर प्रश्न नहीं। "
           "संधि जाँची: रास्नामश्वगंधां = रास्नाम् + अश्वगन्धाम्; पुनर्नवां में अन्त का ं = म्। क्रिया इस इकाई में नहीं; सम्भवतः 05.05.96 का ‘विपाच्य’।"),
    "48": ("विश्वास: मध्यम। छपा ‘पळांशिकं’ (ळ) = पलांशिकम् (वर्तनी सामान्यीकृत)। ‘पलांशिक’ किस संज्ञा का विशेषण है, नहीं कहा; पूरी सूची पर भी लग सकता है। ‘प्रत्येक’ पाठ में नहीं। "
           "पहचान: शतावरी, यव, माष, अतसी, कुलत्थ मानक; सहचर (कटसरैया) और कोल (बेर) सम्भावित; काकनासा विवादित। प्रसृत = अंजलि-भर का मान; ग्राम में नहीं बदला। "
           "05.05.92-95 के कर्म 05.05.96 के ‘विपाच्य’ के लगते हैं (वाक्य इकाइयों के पार)। "
           "संधि जाँची: यवमाषातसी = यव + माष + अतसी (अ + अ → आ); प्रसृतोन्मितान् = प्रसृत + उन्मितान् (अ + उ → ओ); पलांशिकं = पल + अंशिकम्।"),
    "49": ("विश्वास: मध्यम। ‘वहे’ का अर्थ संदिग्ध: ‘वह’ नामक मान माना गया, ‘तोयस्य’ के साथ। "
           "खुला अवलोकन (05.05.96): वह और द्रोण के आकार नहीं निकाले गए (द्रोण = ४ आढक मानक है, वह का आकार ग्रन्थों में भिन्न); इन संख्याओं पर प्रश्न नहीं। "
           "‘विपाच्य’ का कर्म अनुक्त, सम्भवतः 05.05.92-95 की सूची। ‘तेन’ = शेष क्वाथ। जीवनीय दस द्रव्यों का गण (मानक), पंक्ति उन्हें नहीं गिनाती। "
           "संधि जाँची: पचेत्तैलाढकं = पचेत् + तैल + आढकम्; पेष्यैर्जीवनीयैः = पेष्यैः + जीवनीयैः (ऐः → ऐर् सघोष से पहले); पलोन्मितैः = पल + उन्मितैः।"),
    "50": ("विश्वास: उच्च। नाम ‘अनुवासन’ पंक्ति में ही है। ‘-नुत्’ = ‘-नुद्’ का पदान्त रूप। "
           "‘आनूप’ = दलदली भूमि का; ‘प्राणी’ शब्द अनुक्त। ‘तद्वत्’ पिछली इकाई की विधि की ओर। दूसरी पंक्ति में क्रिया नहीं। "
           "संधि जाँची: अनुवासनमित्येतत् = अनुवासनम् + इति + एतत् (इ + ए → ये); तद्वज्जीवनीयोपसाधिता = तद्वत् + जीवनीय + उपसाधिता (त् + ज → ज्ज; अ + उ → ओ)।"),
    "51": ("विश्वास: मध्यम। छपा ‘शताव्हा’ = शताह्वा (छपाई की परिपाटी)। ‘अम्ल’ को ‘खट्टे (द्रव्य)’ पढ़ा; एक खट्टा द्रव्य भी हो सकता है। "
           "खुला अवलोकन (05.05.100): ‘समीरणे’ शाब्दिक ‘वायु में’, ‘वायु के लिए’ व्याख्या। खुला अवलोकन (05.05.101) और text_flags: छपा ‘-द्धृतं’ को ‘घृतम्’ पढ़ना अनुमान; इस पर प्रश्न नहीं बना, ‘च’ और ‘अनिलजित्’ स्पष्ट हैं। "
           "संधि जाँची: बिल्वाम्लैस्तैलं = बिल्व + अम्लैः + तैलम् (ः → स् त से पहले); सैंधवेनाग्निवर्णेन = सैन्धवेन + अग्निवर्णेन; चानिल = च + अनिल।"),
    "52": ("विश्वास: मध्यम। छपा ‘बळां’ (ळ) = बलाम्; ‘शताव्हर्षभकौ’ = शताह्व + ऋषभकौ (अ + ऋ → अर्), द्वन्द्व द्विवचन; समास में शताह्वा का अन्त्य ह्रस्व। "
           "पहचान: जीवन्ती, मदन, बला मानक; श्रावणी, मधुक (मुलेठी; महुआ भी मधुक कहलाता), कृष्णा (पिप्पली) सम्भावित; मेदा, ऋषभक, काकनासा विवादित। "
           "क्रिया नहीं; सूची 05.05.104-105 में चलती है।"),
    "53": ("विश्वास: मध्यम। text_flags: ‘चतुर्गुणैः’ (तृतीया बहुवचन) ‘क्षीरे’ (सप्तमी एकवचन) से मेल नहीं खाता; दो इकाई बाद के ‘क्षीरे चतुर्गुणे’ के आधार पर ‘चतुर्गुणे’ सुझाया गया। एक proofread टिप्पणी ‘साधयेत’ को अपूर्ण मानती है, पर यह आत्मनेपद विधिलिङ् का नियमित रूप है। दोनों शब्दों पर प्रश्न नहीं बना; पिष्ट्वा, तैलं, घृतं, क्षीरे स्पष्ट हैं। "
           "‘कर्कटाख्या’ = कर्कट नामक; कर्कटशृंगी सम्भावित, पंक्ति में नहीं। क्षीरकाकोली विवादित; स्वगुप्ता = आत्मगुप्ता, कौंच (मानक)। "
           "संधि जाँची: कर्कटाख्यां = कर्कट + आख्याम् (अ + आ → आ)।"),
    "54": ("विश्वास: मध्यम। दोनों पंक्तियों में क्रिया नहीं; श्लोक 05.05.102-105 की तैयारी का वर्णन माना गया। छपा ‘वर्द्धन’ = वर्धन। "
           "‘अग्नि’ = पाचन-अग्नि (ऐसी सूचियों में सामान्य), पंक्ति केवल ‘अग्नि’ कहती है। ‘रजस्’ = आर्तव (इस प्रसंग में मानक)। ‘पुत्रीय’ शाब्दिक रखा: कैसे, पाठ नहीं कहता। "
           "संधि जाँची: बलशुक्राग्नि = बल + शुक्र + अग्नि (अ + अ → आ); रजःशुक्रामयहरं = रजः + शुक्र + आमय + हरम्; चानुवासनं = च + अनुवासनम्।"),
    "55": ("विश्वास: मध्यम। द्रव्य अनुक्त, केवल गुण: ‘शिशिर-स्पर्श-वीर्य’; ‘शिशिर’ दोनों (स्पर्श और वीर्य) के साथ लिया गया, दूसरा पठन भी सम्भव। data के हिन्दी में केवल ‘वीर्य’ है; शब्दावली के अनुसार ‘वीर्य यानी शक्ति’ होना चाहिए। "
           "‘तैलपाद’ = जिसमें तेल चौथाई हो (घी का, ऐसा माना जाता है; पंक्ति नहीं कहती)। क्रिया नहीं। "
           "संधि जाँची: वीर्यैश्च = वीर्यैः + च (ः → श् च से पहले); पित्तघ्नमनुवासनं = पित्तघ्नम् + अनुवासनम्।"),
    "56": ("विश्वास: मध्यम। text_flags: छपा ‘निचलो’ (निश्चल) द्रव्य नहीं, ‘निचुलः’ सुझाया (Barringtonia या वेतस, विवादित); ‘ह्रीबेरं’ में ब/व का भेद, ह्रीवेर पढ़ा। खुला अवलोकन (05.05.110): कोई बदलाव नहीं। इन दो शब्दों पर प्रश्न नहीं बना। "
           "यहाँ ‘कुष्ठ’ औषध (कूठ) है, त्वचा-रोग नहीं। सूची प्रथमा में (नपुंसक प्रथमा = द्वितीया); उपयोग 05.05.115 में। "
           "संधि जाँची: निचलो वचा = निचलः + वचा (अः → ओ सघोष से पहले); सकट्फलं = स + कट्फलम्।"),
    "57": ("विश्वास: मध्यम। पहचान: नागर, चित्रक, विडंग, अतिविषा, नीलिनी मानक; पुष्कर (पुष्करमूल; कमल भी), चविका, स्थिरा सम्भावित; मेदा, श्यामा, हरेणु विवादित। "
           "‘विडंगातिविषे’ द्वन्द्व द्विवचन (स्त्रीलिङ्ग -ए)। शब्दावली का ‘विड’ (नमक) यहाँ नहीं। "
           "संधि जाँची: विडंगातिविषे = विडङ्ग + अतिविषे (अ + अ → आ); हरेणुर्नीलिनी = हरेणुः + नीलिनी (उः → उर् सघोष से पहले)।"),
    "58": ("विश्वास: मध्यम। ‘तैः समैः’ = उन समानों से; ‘बराबर भाग’ अर्थ सम्भावित, ‘भाग’ शब्द नहीं। ‘बिल्वाजमोदे’ द्वन्द्व द्विवचन। चपला विवादित (कुछ सूचियों में पिप्पली); अजमोदा सम्भावित; दन्ती मानक। "
           "किन द्रव्यों से तेल पके, पिछली इकाइयों (05.05.110-114) की सूची मानी गई। ‘-नुत्’ = ‘-नुद्’ का पदान्त रूप। "
           "संधि जाँची: बिल्वाजमोदे = बिल्व + अजमोदे; साध्यमैरंडतैलं = साध्यम् + ऐरण्डतैलम्।"),
    "59": ("विश्वास: मध्यम। छपा ‘उदावर्त्त’ = उदावर्त। पहली पंक्ति के द्वितीया कर्म ‘हन्यात्’ के हैं, जो इसी इकाई की दूसरी पंक्ति में है (data की पंक्ति-टिप्पणी ‘अगली इकाई’ कहती है, पर दोनों पंक्तियाँ इसी इकाई में हैं)। "
           "खुला अवलोकन (05.05.116): ‘मेह’ = प्रमेह गण; मधुमेह का आधुनिक नाम स्वामी तय करेंगे, इस पर प्रश्न नहीं। वर्ध्म = अण्डवृद्धि, हर्निया या हाइड्रोसील (सम्भावित)। ‘समारुतान्’ = वायु सहित। "
           "संधि जाँची: वर्ध्मोदावर्त = वर्ध्म + उदावर्त (अ + उ → ओ); गुल्मार्शः = गुल्म + अर्शः; आनाहमश्मरीं = आनाहम् + अश्मरीम्; चाशु = च + आशु; हन्यात्तदनुवासनं = हन्यात् + तत् + अनुवासनम्।"),
    "60": ("विश्वास: उच्च। ‘साधितम्’ दोनों करणों (पञ्चमूलेन, बिल्वादिना) के साथ। पाँच जड़ें और ‘बिल्वादि’ के सदस्य नामित नहीं। दूसरी पंक्ति में क्रिया नहीं। "
           "छपा ‘बिल्वादिना ऽथवा’ में अवग्रह से पहले रिक्त स्थान छपाई का है। "
           "संधि जाँची: बिल्वादिना ऽथवा = बिल्वादिना + अथवा (आ + अ → आ, अवग्रह चिह्न); द्रव्यैर्वा = द्रव्यैः + वा (ऐः → ऐर् सघोष से पहले)।"),
    "61": ("विश्वास: निम्न। text_flags: ‘पैटुमूत्रवान्’ कोई शब्द नहीं; ‘पटुमूत्रवान्’ (पटु = सम्भवतः नमक, और मूत्र) सुझाया गया; इस शब्द पर प्रश्न नहीं बना। "
           "‘अष्टगुणे अम्ले’ शाब्दिक ‘आठ गुने खट्टे में’; किसका आठ गुना और ‘अम्ल’ की संज्ञा अनुक्त। ‘अन्वासन’ = अनुवासन का दूसरा रूप। ‘तद्युक्त’ पिछले अन्वासन की ओर, निश्चित नहीं। मुख्य क्रिया नहीं। "
           "संधि जाँची: फलैरष्टगुणे = फलैः + अष्टगुणे; चाम्ले = च + अम्ले; सिद्धमन्वासनं = सिद्धम् + अन्वासनम्; शूलानाहे = शूल + आनाहे; तद्युक्तो निरूहः = तद्युक्तः + निरूहः (अः → ओ सघोष से पहले)।"),
}


AIDS = {
    "47": {
        "diagram": {"groups": [{"label": "पंक्ति १", "items": ["दशमूल", "वरा", "रास्ना", "अश्वगन्धा", "पुनर्नवा"]},
                               {"label": "पंक्ति २ (बिगड़ा समास)", "items": ["गुडूची", "एरण्ड (अनुमानित)", "भूतीक", "भार्गी", "वृषक", "शिरीष (अनुमानित)"]}]},
        "sandhi": "म् + स्वर: रास्नाम् + अश्वगन्धाम् → रास्नामश्वगन्धाम्; ई + ऐ → यै: गुडूची + ऐरण्ड → गुडूच्यैरण्ड (छपा ‘गुडूच्यैंरंड’)।",
        "anchors": "दशमूल = दस जड़ें · वरा = सम्भवतः त्रिफला · अश्वगन्धा = असगन्ध · गुडूची = गिलोय · भार्गी = भारंगी · वृषक = सम्भवतः अडूसा।",
    },
    "48": {
        "frame": "पंक्ति १: शतावरी, सहचर, काकनासा · मान: पलांशिक (पल-भर भाग) · पंक्ति २: यव, माष, अतसी, कोल, कुलत्थ · मान: प्रसृत।",
        "sandhi": "अ + अ → आ: माष + अतसी → माषातसी; अ + उ → ओ: प्रसृत + उन्मितान् → प्रसृतोन्मितान्।",
        "anchors": "यव = जौ-अन्न (यव) · माष = उड़द · अतसी = अलसी · कुलत्थ = कुलथी · प्रसृत = अंजलि-भर · अंश = भाग।",
    },
    "49": {
        "chain": {"steps": ["द्रव्य (श्लोक ४७-४८)", "एक वह जल में उबाले", "एक द्रोण शेष रहे", "उससे एक आढक तेल पकाए", "साथ: जीवनीय, पिसे, पल-भर"]},
        "sandhi": "ऐः → ऐर् सघोष से पहले: पेष्यैः + जीवनीयैः → पेष्यैर्जीवनीयैः; त् + त → त्त: पचेत् + तैल → पचेत्तैल।",
        "anchors": "विपाच्य = उबालकर · तोय = जल · शेष = बचा हुआ · पचेत् = पकाए · पेष्य = पीसने योग्य · उन्मित = मापा हुआ।",
    },
    "50": {
        "frame": "नाम: अनुवासन · काम: सब वात-विकार दूर · दूसरा द्रव्य: आनूप (दलदली भूमि के) प्राणियों की वसा · विधि: उसी प्रकार, जीवनीय से।",
        "sandhi": "इ + ए → ये: इति + एतत् → इत्येतत्; त् + ज → ज्ज: तद्वत् + जीवनीय → तद्वज्जीवनीय; अ + उ → ओ: जीवनीय + उपसाधिता → जीवनीयोपसाधिता।",
        "anchors": "अनुवासन = रोकी जाने वाली स्नेह-बस्ति · विकार = रोग · नुद् = दूर करने वाला · आनूप = दलदली · वसा = चर्बी · तद्वत् = वैसे ही।",
    },
    "51": {
        "contrast": "पहला योग: शताह्वा-यव-बिल्व-अम्ल से सिद्ध तेल, वायु में ↔ दूसरा योग: लाल-तपे सेंधे नमक से तपाया, वात-जित् (घी, अनुमानित पाठ)।",
        "sandhi": "ः → स् त से पहले: अम्लैः + तैलम् → अम्लैस्तैलम्; अ + अ → आ: सैन्धवेन + अग्निवर्णेन → सैन्धवेनाग्निवर्णेन।",
        "anchors": "शताह्वा = सोआ · बिल्व = बेल · अम्ल = खट्टा · समीरण = वायु (वात) · अग्निवर्ण = आग के रंग का · जित् = जीतने वाला।",
    },
    "52": {
        "chunks": "जीवंतीं मदनं मेदां | श्रावणीं मधुकं बळां ‖ शताव्हर्षभकौ कृष्णां | काकनासां शतावरीं।",
        "sandhi": "अ + ऋ → अर्: शताह्व + ऋषभकौ → शताह्वर्षभकौ (द्वन्द्व, द्विवचन)।",
        "anchors": "जीवन्ती = डोडी · मदन = मैनफल · मधुक = सम्भवतः मुलेठी · बला = बरियार · कृष्णा = सम्भवतः पिप्पली · शतावरी = शतावरी।",
    },
    "53": {
        "frame": "सूची का अन्त: स्वगुप्ता, क्षीरकाकोली, कर्कट-नामक, शठी, वचा · विधि: पीसकर · पकाना: तेल और घी, दूध में (चौगुना, सुझाया पाठ)।",
        "contrast": "पिष्ट्वा ↔ विपाच्य: बिना उपसर्ग -त्वा (पिष् → पिष्ट्वा); उपसर्ग के साथ -य (वि + पच् → विपाच्य, श्लोक ४९)।",
        "anchors": "स्वगुप्ता = कौंच · कर्कटाख्या = कर्कट नामक · शठी = सम्भवतः कपूरकचरी · वचा = बच · पिष्ट्वा = पीसकर · क्षीर = दूध।",
    },
    "54": {
        "diagram": {"groups": [{"label": "गुण और नाम", "items": ["बृंहण", "पुत्रीय अनुवासन"]},
                               {"label": "नाश करे", "items": ["वात", "पित्त"]},
                               {"label": "बढ़ाए", "items": ["बल", "शुक्र", "अग्नि"]},
                               {"label": "रोग हरे", "items": ["रज", "शुक्र"]}]},
        "contrast": "-घ्न ↔ -वर्धन: वातपित्तघ्न = वात-पित्त का नाश; बलशुक्राग्निवर्धन = बल, शुक्र, अग्नि की वृद्धि।",
        "anchors": "बृंहण = पोषण · घ्न = नाशक · वर्धन = बढ़ाने वाला · रजस् = आर्तव · आमय = रोग · पुत्रीय = पुत्र से सम्बन्धित।",
    },
    "55": {
        "chain": {"steps": ["स्पर्श और वीर्य में शीतल द्रव्य", "पीसे", "चौगुने दूध में", "घी, जिसमें तेल चौथाई", "पकाया: पित्तघ्न अनुवासन"]},
        "sandhi": "ः → श् च से पहले: वीर्यैः + च → वीर्यैश्च; म् + स्वर: पित्तघ्नम् + अनुवासनम् → पित्तघ्नमनुवासनम्।",
        "anchors": "शिशिर = शीतल · स्पर्श = छूना · वीर्य = वीर्य यानी शक्ति · पिष्ट = पिसा · चतुर्गुण = चौगुना · पाद = चौथाई।",
    },
    "56": {
        "chunks": "सैंधवं मदनं कुष्ठं | शताव्हा निचलो वचा ‖ ह्रीबेरं मधुकं भार्गी | देवदारु सकट्फलं।",
        "contrast": "कुष्ठ (औषध) ↔ कुष्ठ (रोग): यहाँ द्रव्यों की सूची में कुष्ठ = कूठ नामक औषध, त्वचा-रोग नहीं।",
        "anchors": "सैन्धव = सेंधा नमक · कुष्ठ = कूठ · वचा = बच · ह्रीवेर = सुगन्धबाला · देवदारु = देवदार · कट्फल = कायफल · स- = सहित।",
    },
    "57": {
        "chunks": "नागरं पुष्करं मेदा | चविका चित्रकः शठी ‖ विडंगातिविषे श्यामा | हरेणुर्नीलिनी स्थिरा।",
        "sandhi": "अ + अ → आ: विडङ्ग + अतिविषे → विडङ्गातिविषे; उः → उर् सघोष से पहले: हरेणुः + नीलिनी → हरेणुर्नीलिनी।",
        "pegs": "मेरा बनाया क्रम-सूत्र (श्लोक का दावा नहीं): ‘ना-पु-मे-च-चि-श’ यानी नागर, पुष्कर, मेदा, चविका, चित्रक, शठी; फिर ‘वि-अ-श्या-ह-नी-स्थि’।",
        "anchors": "नागर = सोंठ · चित्रक = चीता · विडङ्ग = वायविडंग · अतिविषा = अतीस · नीलिनी = नील · स्थिरा = सम्भवतः शालपर्णी।",
    },
    "58": {
        "chain": {"steps": ["बिल्व, अजमोदा, चपला, दन्ती, रास्ना", "उन समान (द्रव्यों) से", "एरण्ड-तेल या कोई तेल साधित", "कफ-रोग दूर"]},
        "sandhi": "अ + अ → आ: बिल्व + अजमोदे → बिल्वाजमोदे; म् + स्वर: साध्यम् + ऐरण्डतैलम् → साध्यमैरण्डतैलम्।",
        "anchors": "अजमोदा = सम्भवतः अजमोद · दन्ती = जंगली जमालगोटा · सम = बराबर · साध्य = साधने योग्य · एरण्डतैल = अरंडी का तेल · वा … वा = या … या।",
    },
    "59": {
        "diagram": {"groups": [{"label": "पंक्ति १ (वायु सहित)", "items": ["वर्ध्म", "उदावर्त", "गुल्म", "अर्श", "प्लीहा-रोग", "मेह"]},
                               {"label": "पंक्ति २", "items": ["आनाह", "अश्मरी"]},
                               {"label": "कौन नष्ट करे", "items": ["वह अनुवासन, शीघ्र"]}]},
        "sandhi": "अ + उ → ओ: वर्ध्म + उदावर्त → वर्ध्मोदावर्त; अ + आ → आ: च + आशु → चाशु; त् + त → त्त: हन्यात् + तत् → हन्यात्तत्।",
        "anchors": "वर्ध्म = सम्भवतः अण्डवृद्धि · उदावर्त = वायु उलटा · गुल्म = गाँठ · अर्श = बवासीर · अश्मरी = पथरी · आशु = शीघ्र।",
    },
    "60": {
        "frame": "विकल्प १: पञ्चमूल से साधित तेल · विकल्प २: बिल्व आदि से · विकल्प ३: कोई भी कफ-घाती द्रव्य · काम: श्लेष्म-हर अनुवासन।",
        "contrast": "पञ्चमूल ↔ दशमूल: यहाँ (कफ) पाँच जड़ों का समूह; श्लोक ४७ (वात) में दस जड़ों का समूह।",
        "anchors": "पञ्च = पाँच · मूल = जड़ · आदि = इत्यादि · श्लेष्मन् = कफ · हर = हरने वाला · घातिन् = नाशक।",
    },
    "61": {
        "contrast": "कफ में: फल और आठ गुने अम्ल से सिद्ध अन्वासन ↔ शूल-आनाह में: उससे युक्त निरूह (पटु-मूत्र वाला, अनुमानित)।",
        "sandhi": "ऐः → ऐर् स्वर से पहले: फलैः + अष्टगुणे → फलैरष्टगुणे; अ + आ → आ: शूल + आनाहे → शूलानाहे; अः → ओ: तद्युक्तः + निरूहः → तद्युक्तो निरूहः।",
        "anchors": "अष्टगुण = आठ गुना · अम्ल = खट्टा · अन्वासन = अनुवासन · शूल = पीड़ा · आनाह = पेट फूलना · निरूह = क्वाथ-बस्ति।",
    },
}


IMAGE_SPECS = {
    ("47", "diagram"): {
        "file": "ka5-dashamula-taila-47.svg",
        "alt": ("Table of verse 47: line 1 has five drugs (dashamula, vara, rasna, ashvagandha, punarnava); "
                "line 2, a damaged compound, has six (guduci, eranda conjectural, bhutika, bhargi, vrishaka, shirisha conjectural)"),
        "type": "table",
        "title": "श्लोक ४७: अनुवासन तैल के द्रव्य",
        "heads": ["पंक्ति", "द्रव्य"],
        "rows": [["पंक्ति १", "दशमूल, वरा, रास्ना"], ["पंक्ति १", "अश्वगन्धा, पुनर्नवा"],
                 ["पंक्ति २", "गुडूची, एरण्ड (अनुमानित)"], ["पंक्ति २", "भूतीक, भार्गी, वृषक"],
                 ["पंक्ति २", "शिरीष (अनुमानित)"]],
    },
    ("49", "chain"): {
        "file": "ka5-vaha-drona-49.svg",
        "alt": ("Flowchart of verse 49: the drugs of verses 47-48 are boiled in a vaha of water until a drona remains; "
                "with that an adhaka of oil is cooked, together with the jivaniya drugs ground and measured by a pala"),
        "type": "mermaid",
        "code": ('flowchart TD\n  A["द्रव्य, श्लोक ४७-४८"] --> B["एक वह जल में उबाले"]\n'
                 '  B --> C["एक द्रोण शेष रहे"]\n  C --> D["उससे एक आढक<br/>तेल पकाए"]\n'
                 '  E["जीवनीय, पिसे,<br/>पल-भर"] --> D\n'),
    },
    ("51", "contrast"): {
        "file": "ka5-shatahva-saindhava-51.svg",
        "alt": ("Split picture of verse 51: first, oil cooked with shatahva, yava, bilva and sour ones, given in wind (Vata); "
                "second, a preparation heated with red-hot rock salt that conquers Vata (ghee on a conjectural reading)"),
        "type": "split",
        "title": "श्लोक ५१: वात के दो योग",
        "cols": [["तेल, वायु में", ["शताह्वा", "यव", "बिल्व", "अम्ल"]],
                 ["वात-जित् योग", ["अग्निवर्ण सैन्धव", "से तपाया", "घी: अनुमानित पाठ"]]],
    },
    ("54", "diagram"): {
        "file": "ka5-putriya-anuvasana-54.svg",
        "alt": ("Mind map of verse 54: the anuvasana is nourishing; destroys Vata and Pitta; increases strength, semen and agni; "
                "removes ailments of menstrual blood and semen; and is called putriya"),
        "type": "mermaid",
        "code": ('mindmap\n  पुत्रीय अनुवासन\n    बृंहण\n    नाश करे\n      वात\n      पित्त\n'
                 '    बढ़ाए\n      बल\n      शुक्र\n      अग्नि\n    रोग हरे\n      रज\n      शुक्र\n'),
    },
    ("55", "chain"): {
        "file": "ka5-pittaghna-ghrita-55.svg",
        "alt": ("Flowchart of verse 55: drugs cold in touch and potency are ground, put in fourfold milk, and ghee with oil "
                "as a quarter is cooked: a Pitta-destroying anuvasana"),
        "type": "mermaid",
        "code": ('flowchart TD\n  A["स्पर्श, वीर्य में<br/>शीतल द्रव्य"] --> B["पीसे"]\n'
                 '  B --> C["चौगुने दूध में"]\n  C --> D["घी, जिसमें<br/>तेल चौथाई"]\n'
                 '  D --> E["पित्तघ्न अनुवासन"]\n'),
    },
    ("58", "chain"): {
        "file": "ka5-kapharoga-taila-58.svg",
        "alt": ("Chain of verse 58: bilva, ajamoda, capala, danti and rasna; with those, equal; castor oil or another oil "
                "is prepared; it removes diseases of Kapha"),
        "type": "chain",
        "title": "श्लोक ५८: कफ-रोग नाशक तेल",
        "steps": ["बिल्व, अजमोदा, चपला, दन्ती, रास्ना", "उन समान द्रव्यों से", "एरण्ड-तेल या कोई तेल साधित", "कफ-रोग दूर"],
    },
    ("59", "diagram"): {
        "file": "ka5-anuvasana-roga-59.svg",
        "alt": ("Mind map of verse 59: that anuvasana quickly destroys, in line 1, vardhma, udavarta, gulma, piles, "
                "spleen disorder and meha (with wind), and in line 2 anaha and urinary stone"),
        "type": "mermaid",
        "code": ('mindmap\n  अनुवासन शीघ्र नष्ट करे\n    पंक्ति एक, वायु सहित\n      वर्ध्म\n      उदावर्त\n      गुल्म\n'
                 '      अर्श\n      प्लीहा-रोग\n      मेह\n    पंक्ति दो\n      आनाह\n      अश्मरी\n'),
    },
    ("61", "contrast"): {
        "file": "ka5-kapha-shula-61.svg",
        "alt": ("Split picture of verse 61: in Kapha, an anvasana cooked with fruits and the eightfold sour; "
                "in pain and distension, a niruha joined with that"),
        "type": "split",
        "title": "श्लोक ६१: दो स्थितियाँ, दो बस्तियाँ",
        "cols": [["कफ में", ["अन्वासन", "फलों से", "आठ गुने अम्ल में"]],
                 ["शूल, आनाह में", ["निरूह", "उससे युक्त"]]],
    },
}
