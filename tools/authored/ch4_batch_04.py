from helpers import mcq, match, order, fill, multi, accepts

AUTHORED = {}

# ---------------------------------------------------------------- unit 41
AUTHORED["41"] = {
    "title": "निर्गदांश्चासवारिष्ट",
    "question": "Which drinks does this unit list?",
    "rule": ("Line 1 names five drinks, āsava, ariṣṭa, sīdhu, mārdvīka and mādhava; "
             "line 2 gives three water drinks joined by 'or' (वा): water with musta and "
             "śuṇṭhī, sāra-water, honey-water."),
    "limits": ("The sentence is cut: it has no verb here and belongs with the neighbouring "
               "units. 'Harmless' (निर्गद) is a literal rendering. कथित may be a slip for "
               "क्वथित 'boiled' (a suggestion only), and 'sāra' has several senses. The unit "
               "does not say how or when any drink is taken."),
    "explain_hi": ("यह युग्म पेयों की सूची है; वाक्य अधूरा है और पड़ोसी श्लोकों से जुड़ता है। "
                   "पहली पंक्ति में पाँच पेयों के नाम हैं: आसव, अरिष्ट, सीधु, मार्द्वीक और माधव। "
                   "उन्हें ‘निर्गद’ (रोगरहित) कहा गया है। दूसरी पंक्ति में ‘वा’ (अथवा) से तीन जल "
                   "गिनाए हैं: मुस्त और शुंठी वाला जल, सार का जल, और शहद का जल। "
                   "आसव आदि पाँच नाम, तथा मुस्त, शुंठी और सार का अर्थ श्लोक नहीं बताता, इसलिए वे नाम ही रखे गए हैं।"),
    "hook": "पाँच नाम (आसव…माधव), फिर तीन जल — अंत में वा।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "Which of these is a drink named in line 1 of this unit?",
            ("सीधु", "Line 1 names आसव, अरिष्ट, सीधु, मार्द्वीक and माधव."),
            [("पानक", "पानक (a drink) is named in a later unit, not in this one."),
             ("शर्करा", "शर्करा (sugar) belongs to a later unit."),
             ("घृत", "घृत (ghee) belongs to a later unit.")],
            "The five names in line 1 are आसव, अरिष्ट, सीधु, मार्द्वीक and माधव.",
            "Line 1: आसव · अरिष्ट · सीधु · मार्द्वीक · माधव."),
        order(1, "Put the five drinks of line 1 in the order of the verse.",
              ["आसव", "अरिष्ट", "सीधु", "मार्द्वीक", "माधव"],
              "The line runs आसव, अरिष्ट, सीधु, मार्द्वीक, माधव.",
              "आसव · अरिष्ट · सीधु · मार्द्वीक · माधव.", role="warmup"),
        match(2, "Match each word of the unit to its meaning.",
              [["निर्गदान्", "free of ailment"], ["च", "and"], ["वा", "or"],
               ["क्षौद्रवारि", "honey-water"], ["सारांभः", "sāra-water"]],
              "These five words carry the sense of the two lines: the drinks, the 'and' of line 1 and the 'or' of line 2.",
              "च = and; वा = or; क्षौद्र = honey; वारि = water.",
              role="extend",
              teaches="च joins things together ('and') and वा offers alternatives ('or'); क्षौद्रवारि is 'honey-water', a compound of two nouns."),
        mcq("discriminate", 3, "Which is the right split of निर्गदांश्चासव-?",
            ("निर्गदान् + च + आसव",
             "-ान् before च becomes -ांश्च; च + आ gives चा."),
            [("निर्गदाः + च + आसव", "A visarga would give निर्गदाश्चासव, with no anusvara."),
             ("निर्गदां + श्च + आसव", "श्च is not a word; the श् comes from the joining."),
             ("निर्गद + अंश्च + आसव", "अंश्च is not a word here.")],
            "निर्गदान् (accusative plural) + च (and) + आसव: न् before च turns into ंश्.",
            "-ान् + च → -ांश्च."),
        mcq("apply", 4, "Which of these is NOT named in this unit?",
            ("coconut water", "Coconut water is named in a later unit, not here."),
            [("honey-water", "क्षौद्रवारि is in line 2."),
             ("sāra-water", "सारांभः is in line 2."),
             ("water with musta and śuṇṭhī", "This is the first water of line 2.")],
            "Line 2 names three waters: with musta and śuṇṭhī, sāra-water and honey-water. Coconut water is not among them.",
            "Line 2: three waters, joined by वा."),
        mcq("transfer", 5, "In the style of क्षौद्रवारि, which compound means sugar-water?",
            ("शर्करावारि", "X + वारि means the water of X, as क्षौद्रवारि is honey-water."),
            [("वारिशर्करा", "Here वारि comes first: the compound would read 'water-sugar'."),
             ("शर्करावारिता", "The ending -ता would make an abstract noun, not 'sugar-water'."),
             ("अशर्करावारि", "The prefix अ- would negate it: 'water without sugar'.")],
            "In क्षौद्रवारि the first part says which water: honey-water. शर्करावारि is built the same way.",
            "X-वारि = X-water.",
            teaches="A compound X-वारि (or X-अम्बु) names the water of X, with the first part telling which (क्षौद्रवारि = honey-water)."),
    ],
}

# ---------------------------------------------------------------- unit 42
AUTHORED["42"] = {
    "title": "गुरुशीतदिवास्वप्न",
    "question": "What does line 1 say to avoid, and how does line 2 describe summer?",
    "rule": ("Line 1: one should avoid (त्यजेत्) the heavy and cold, day-sleep, and the unctuous, "
             "sour and sweet. Line 2: in summer (ग्रीष्मे), sharp-rayed, like the atasī flower, "
             "kindled by forest fire."),
    "limits": ("Line 2 has no verb; its nominatives most naturally describe the sun, which the "
               "unit does not name. 'Kindled by forest fire' is literal. The sentence goes on in "
               "unit 43. The unit does not say the avoidance is for summer only."),
    "explain_hi": ("पहली पंक्ति में ‘त्यजेत्’ (छोड़े) का कर्म छह चीज़ें हैं: भारी और शीत, दिन की नींद, "
                   "तथा स्निग्ध, अम्ल और मधुर। दूसरी पंक्ति ग्रीष्म का वर्णन शुरू करती है: "
                   "अतसी के फूल जैसा, तीक्ष्ण किरणों वाला, दावानल से दीप्त। इसमें क्रिया नहीं है और "
                   "वर्णन सूर्य का माना गया है; वाक्य अगले श्लोक में चलता है। "
                   "श्लोक यह नहीं कहता कि ये त्याग केवल ग्रीष्म के लिए हैं।"),
    "hook": "भारी-शीत, दिन की नींद, स्निग्ध-अम्ल-मधुर छोड़े; ग्रीष्म में तीक्ष्ण किरणें।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "Which of these does line 1 say one should avoid?",
            ("daytime sleep", "दिवास्वप्न is in line 1."),
            [("exercise", "Exercise is avoided in a later unit, not in this one."),
             ("wine", "Wine is dealt with in a later unit."),
             ("bathing", "Bathing is not named here.")],
            "दिवास्वप्न (day-sleep) is the third item of the list.",
            "Avoid: गुरु, शीत, दिवास्वप्न, स्निग्ध, अम्ल, मधुर."),
        order(1, "Put the six things of line 1 in the order of the verse.",
              ["गुरु", "शीत", "दिवास्वप्न", "स्निग्ध", "अम्ल", "मधुर"],
              "The line runs heavy, cold, day-sleep, unctuous, sour, sweet.",
              "गुरु · शीत · दिवास्वप्न · स्निग्ध · अम्ल · मधुर.", role="warmup"),
        match(2, "Match each word of line 1 to its meaning.",
              [["गुरु", "heavy"], ["स्निग्ध", "unctuous"], ["अम्ल", "sour"],
               ["मधुर", "sweet"], ["दिवास्वप्न", "sleep by day"]],
              "These five words are five of the six things listed for avoiding.",
              "गुरु = heavy; स्निग्ध = unctuous; अम्ल = sour; मधुर = sweet; दिवा = by day.",
              role="extend",
              teaches="दिवास्वप्न is दिवा 'by day' + स्वप्न 'sleep': a compound of two words."),
        mcq("discriminate", 3, "Which is the right split of मधुरांस्त्यजेत्?",
            ("मधुरान् + त्यजेत्", "-ान् before त becomes -ांस्; त्यजेत् is the verb."),
            [("मधुराः + त्यजेत्", "A visarga before त would give मधुरास्त्यजेत्, with no anusvara."),
             ("मधुरां + स्त्यजेत्", "स्त्यजेत् is not a word; the स् comes from the joining."),
             ("मधुरान् + स्त्यजेत्", "There is no word स्त्यजेत्; the verb is त्यजेत्.")],
            "मधुरान् (sweet things, accusative plural) + त्यजेत् (should avoid).",
            "-ान् + त → -ांस्त."),
        mcq("apply", 4, "Which phrase does line 2 give together with 'in summer' (ग्रीष्मे)?",
            ("sharp-rayed", "तीक्ष्णांशुः means sharp-rayed."),
            [("cold-rayed", "The word is तीक्ष्ण (sharp), not cold."),
             ("veiled by cloud", "The line says kindled by forest fire, not veiled by cloud."),
             ("soft-rayed", "The word is तीक्ष्ण (sharp), the opposite of soft.")],
            "Line 2 describes summer with: like the atasī flower, sharp-rayed (तीक्ष्णांशुः), kindled by forest fire.",
            "ग्रीष्मे … तीक्ष्णांशुः."),
        mcq("transfer", 5, "In the style of त्यजेत्, what does शिष्यः आलस्यं त्यजेत् say?",
            ("A student should give up laziness", "-एत् is the 'should' form, as in त्यजेत्."),
            [("A student gave up laziness", "A past act would use a past form, not -एत्."),
             ("A student gives up laziness", "A plain present would be त्यजति."),
             ("A student has no laziness", "Nothing in the sentence says he has none.")],
            "त्यजेत् is the 'should' form of the verb त्यज् (give up); the invented sentence uses it the same way.",
            "-एत् = should.",
            teaches="The ending -एत् (त्यजेत्) says what one 'should' do; शिष्यः आलस्यं त्यजेत् = a student should give up laziness."),
    ],
}

# ---------------------------------------------------------------- unit 43
AUTHORED["43"] = {
    "title": "दिशोज्वलंति भूमिश्च",
    "question": "What does the unit say blazes, and what happens to creatures?",
    "rule": ("The directions and the earth blaze (ज्वलन्ति); the wind is not pleasant from any side; "
             "through wind, sun and sweating creatures are as if feverish (ज्वरिता इव)."),
    "limits": ("'Not pleasant from any side' (नैकतः) is read as 'from no side'. 'ज्वरित' is rendered "
               "'feverish' and इव makes it a comparison: the creatures are not said to have fever. "
               "The unit does not name the season; it follows the summer of unit 42."),
    "explain_hi": ("यह युग्म गर्मी का दृश्य रचता है। पहली पंक्ति: दिशाएँ जलती हैं, भूमि भी जलती है, और "
                   "वायु किसी ओर से सुखद नहीं। दूसरी पंक्ति: वायु, धूप और पसीने से प्राणी ‘ज्वरित इव’ "
                   "होते हैं, यानी मानो ज्वर से पीड़ित। ‘इव’ तुलना है, इसलिए श्लोक यह नहीं कहता कि "
                   "प्राणियों को सचमुच ज्वर होता है।"),
    "hook": "दिशाएँ-भूमि जलें, हवा कहीं से सुखद नहीं; प्राणी मानो ज्वर-पीड़ित।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "What does line 1 say of the directions (दिशः)?",
            ("They blaze", "दिशः ज्वलन्ति: the directions blaze."),
            [("They grow dark", "Nothing about darkness is said."),
             ("They fill with cloud", "No cloud is mentioned in the unit."),
             ("They grow cold", "The unit speaks of blazing heat.")],
            "The first words say दिशः ज्वलन्ति, and the earth too.",
            "दिशः ज्वलन्ति · भूमिः च."),
        order(1, "Put these parts of the unit in the order of the verse.",
              ["the directions blaze", "the earth too", "the wind is not pleasant from any side",
               "creatures are as if feverish"],
              "Line 1 gives directions, earth and wind; line 2 ends with the creatures.",
              "दिशः · भूमिः · मारुतः · जन्तवः.", role="warmup"),
        match(2, "Match each word of the unit to its meaning.",
              [["दिशः", "directions"], ["ज्वलन्ति", "blaze"], ["मारुतः", "wind"],
               ["जन्तवः", "creatures"], ["ज्वरिताः", "feverish"]],
              "These words name what burns, what blows and who is affected.",
              "दिशः = directions; ज्वलन्ति = blaze; मारुतः = wind; जन्तवः = creatures; ज्वरिताः = feverish.",
              role="extend",
              teaches="ज्वलन्ति ('they blaze') is a plural verb agreeing with the plural दिशः; भूमिः च is added to it."),
        mcq("discriminate", 3, "Which is the right split of नैकतः?",
            ("न + एकतः", "अ + ए joins as ऐ: न + एकतः = नैकतः."),
            [("न + ऐकतः", "ऐकतः is not a word; the word is एकतः (from one side)."),
             ("ना + एकतः", "The 'not' here is the short न, not ना."),
             ("नः + एकतः", "A visarga would not leave a bare न.")],
            "नैकतः is न (not) + एकतः (from one side), so 'not from one side'.",
            "अ + ए → ऐ."),
        mcq("apply", 4, "What does the unit say about the wind (मारुतः)?",
            ("It is not pleasant from any side", "मारुतो नैकतः सुखः."),
            [("It is pleasant from every side", "The line says it is not pleasant."),
             ("It brings the rain", "No rain is mentioned in this unit."),
             ("It is pleasant only from the north", "No direction is singled out.")],
            "Line 1 says the wind is not pleasant (सुखः) from one side, read as from no side.",
            "मारुतो नैकतः सुखः."),
        mcq("transfer", 5, "Which is the right joining of सदा + एव?",
            ("सदैव", "आ + ए joins as ऐ, as अ + ए does in नैकतः."),
            [("सदेव", "That would drop the ā without a reason."),
             ("सदौव", "ए does not become औ."),
             ("सदाएव", "Sandhi joins the two vowels; they do not stand side by side.")],
            "आ (and अ) before ए join as ऐ: सदा + एव = सदैव, like न + एकतः = नैकतः.",
            "अ/आ + ए → ऐ.",
            teaches="When a word ending in -अ or -आ meets ए, the two join as ऐ (न + एकतः = नैकतः; सदा + एव = सदैव)."),
    ],
}

# ---------------------------------------------------------------- unit 44
AUTHORED["44"] = {
    "title": "तापार्ततुंगमातंग",
    "question": "Who made the waters turbid, and what consumed them?",
    "rule": ("Made turbid (कलुषीकृताः) by tall elephants and buffaloes distressed by heat; "
             "and having their waters consumed (क्षपित) by a heap of embers that are the sun's rays."),
    "limits": ("Both feminine plural descriptions need a noun; it is 'nadyaḥ' (rivers) in unit 45, "
               "so this unit does not name what is made turbid. The English ends in '...'. "
               "The reading of तुंग (tall) as going with the elephants is the data's choice."),
    "explain_hi": ("यह युग्म किसी स्त्रीलिंग बहुवचन संज्ञा का वर्णन है, जो अगले श्लोक में आती है, इसलिए यहाँ "
                   "यह नाम नहीं है। पहली पंक्ति: ताप से पीड़ित ऊँचे हाथियों और भैंसों ने उन्हें "
                   "गँदला कर दिया। दूसरी पंक्ति: सूर्य की किरणरूपी अंगारों के समूह ने उनका जल "
                   "नष्ट कर दिया। ‘कलुषी-कृत’ का अर्थ है ‘गँदला किया हुआ’।"),
    "hook": "ताप-पीड़ित हाथी-भैंसे गँदला करें; किरण-अंगारे जल सोखें।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "Which animals does line 1 name?",
            ("elephants and buffaloes", "मातङ्ग and महिष are the two animals of line 1."),
            [("deer and birds", "Deer and birds belong to a later unit about food."),
             ("horses and cows", "Neither is named."),
             ("fish and frogs", "Neither is named.")],
            "Line 1 names tall elephants (तुङ्ग मातङ्ग) and buffaloes (महिष).",
            "तुङ्गमातङ्गमहिषैः."),
        order(1, "Put the parts of the compound in line 2 in the order of the verse.",
              ["दिवाकर", "कर", "अंगार", "निकर", "क्षपित", "अंभस्"],
              "The compound runs: sun, ray, ember, heap, consumed, waters.",
              "दिवाकर · कर · अंगार · निकर · क्षपित · अंभस्.", role="warmup"),
        match(2, "Match each word of the unit to its meaning.",
              [["तुंग", "tall"], ["मातंग", "elephant"], ["महिष", "buffalo"],
               ["अंगार", "ember"], ["निकर", "heap"]],
              "These five words carry the picture of the two lines: the animals and the burning heap.",
              "तुंग = tall; मातंग = elephant; महिष = buffalo; अंगार = ember; निकर = heap.",
              role="extend",
              teaches="In a compound like अंगारनिकर the parts follow one another: 'a heap of embers'."),
        mcq("discriminate", 3, "Which is the right split of तापार्त-?",
            ("ताप + आर्त", "अ + आ joins as आ: ताप + आर्त = तापार्त."),
            [("ताप + अर्त", "अर्त is not a word here."),
             ("तापा + आर्त", "ताप is the word, with a short final vowel."),
             ("तापः + आर्त", "A visarga would not vanish inside a compound.")],
            "तापार्त = ताप (heat) + आर्त (distressed): 'distressed by heat'.",
            "अ + आ → आ."),
        mcq("apply", 4, "What does line 2 say consumed the waters?",
            ("a heap of sun-ray embers", "दिवाकरकरांगारनिकर."),
            [("a heap of dry leaves", "Leaves are mentioned in unit 45, not here."),
             ("a stream of the wind", "The wind is not named in this line."),
             ("a swarm of thirsty animals", "The animals are in line 1 and only make the water turbid.")],
            "Line 2: the waters are consumed by a heap (निकर) of embers (अङ्गार) that are the sun's rays (दिवाकर-कर).",
            "दिवाकरकरांगारनिकर = heap of embers that are the sun's rays."),
        mcq("transfer", 5, "In the style of कलुषीकृत, which word means made dirty?",
            ("मलिनीकृत", "X-ई-कृत means made X: कलुषी-कृत is made turbid."),
            [("मलिनहीन", "-हीन means devoid of: 'devoid of dirt'."),
             ("मलिनस्थित", "-स्थित means standing or kept in it."),
             ("मलिनदीपित", "-दीपित means kindled.")],
            "The pattern X-ई-कृत turns a quality into 'made X'; मलिन (dirty) gives मलिनीकृत.",
            "X-ई-कृत = made X.",
            teaches="The form X-ई-कृत means 'made X' (कलुषीकृत = made turbid; मलिनीकृत = made dirty)."),
    ],
}

# ---------------------------------------------------------------- unit 45
AUTHORED["45"] = {
    "title": "प्रवृद्धरोधसो नद्यः",
    "question": "What are the rivers and the trees like?",
    "rule": ("Rivers with banks grown high (प्रवृद्धरोधसः); trees devoid of shade (छायाहीनाः), with "
             "fallen and old leaves, marked by dry bark and creepers."),
    "limits": ("The units 44 and 45 are one sentence: unit 44 describes these rivers. That the banks "
               "stand high because the water has shrunk is a probable reading, not stated. "
               "The unit gives only descriptions; there is no verb."),
    "explain_hi": ("यह युग्म पिछले श्लोक की स्त्रीलिंग संज्ञा ‘नद्यः’ को पूरा करता है। नदियों के तट ऊँचे "
                   "उठे दिखते हैं (प्रवृद्धरोधसः)। वृक्ष छाया से रहित हैं, उनके पत्ते झड़े हुए और पुराने हैं, और "
                   "वे सूखी छाल और लताओं से चिह्नित हैं। तट ऊँचे क्यों हैं, यह श्लोक नहीं बताता; "
                   "पिछले श्लोक को देखकर अनुमान ही किया जा सकता है।"),
    "hook": "ऊँचे तट वाली नदियाँ; छाया-रहित वृक्ष, झड़े-पुराने पत्ते, सूखी छाल-लताएँ।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "What does line 1 say the trees (महीरुहाः) are devoid of?",
            ("shade", "छायाहीनाः: devoid of shade."),
            [("fruit", "Fruit is not mentioned."),
             ("birds", "Birds are not mentioned."),
             ("roots", "Roots are not mentioned.")],
            "छाया-हीनाः means devoid of shade.",
            "छायाहीनाः महीरुहाः."),
        order(1, "Put these descriptions in the order of the verse.",
              ["rivers with high banks", "trees devoid of shade", "with fallen and old leaves",
               "marked by dry bark and creepers"],
              "Line 1 gives the rivers and the shadeless trees; line 2 gives the leaves and the dry bark.",
              "प्रवृद्धरोधसः · छायाहीनाः · विशीर्णजीर्णपर्णाः · शुष्कवल्कललताङ्किताः.", role="warmup"),
        match(2, "Match each word of the unit to its meaning.",
              [["नद्यः", "rivers"], ["महीरुहाः", "trees"], ["पर्ण", "leaf"],
               ["वल्कल", "bark"], ["लता", "creeper"]],
              "These five words are the things the two lines describe.",
              "नद्यः = rivers; महीरुहाः = trees; पर्ण = leaf; वल्कल = bark; लता = creeper.",
              role="extend",
              teaches="In a compound the first part tells the kind: पर्ण 'leaf', वल्कल 'bark' and लता 'creeper' appear as parts of the compounds विशीर्णजीर्णपर्णाः and शुष्कवल्कललताङ्किताः."),
        mcq("discriminate", 3, "Which is the right split of नद्यश्छाया-?",
            ("नद्यः + छाया", "A visarga before छ becomes श्: नद्यः + छाया = नद्यश्छाया."),
            [("नद्यो + छाया", "ओ is made only before a voiced sound; छ is unvoiced."),
             ("नद्या + छाया", "नद्या would be a different case, not the plural subject."),
             ("नद्यः + श्छाया", "श्छाया is not a word; the श् comes from the joining.")],
            "नद्यः (rivers) + छाया... : the visarga changes to श् before the छ of छाया.",
            "ः + छ → श्छ."),
        mcq("apply", 4, "What kind of leaves does line 2 give the trees?",
            ("fallen and old", "विशीर्णजीर्णपर्णाः."),
            [("fresh and green", "The line says fallen and old."),
             ("wet and heavy", "Nothing says wet or heavy."),
             ("flowering and young", "The line says fallen and old.")],
            "विशीर्ण (fallen) and जीर्ण (old) both describe the leaves (पर्ण).",
            "विशीर्णजीर्णपर्णाः."),
        mcq("transfer", 5, "Which phrase means trees devoid of fruit, in the style of छायाहीनाः महीरुहाः?",
            ("फलहीनाः वृक्षाः", "X-हीन means devoid of X."),
            [("फलयुक्ताः वृक्षाः", "-युक्त means joined with: 'with fruit'."),
             ("छायाहीनाः वृक्षाः", "This is 'devoid of shade', not of fruit."),
             ("फलहीनं वृक्षम्", "This is singular and in the wrong case.")],
            "फल (fruit) + हीन (devoid) gives फलहीन; it agrees with the plural trees: फलहीनाः वृक्षाः.",
            "X-हीन = devoid of X.",
            teaches="A compound ending in -हीन means 'devoid of' the first part, and it agrees with the noun it describes."),
    ],
}

# ---------------------------------------------------------------- unit 46
AUTHORED["46"] = {
    "title": "आदत्ते जगतः स्नेहं",
    "question": "Why does the verse say to avoid certain things?",
    "rule": ("Because (यतः) the sun at that time strongly draws away the world's moisture (स्नेह), "
             "therefore (अतः) one should avoid exercise, sun, and the pungent, sour, salty and hot."),
    "limits": ("स्नेह means oil, unctuousness or moisture; the card keeps 'moisture (sneha)'. "
               "'At that time' points back to the summer of the earlier units. "
               "The verse gives the reason and the list, not a dose or a method."),
    "explain_hi": ("यह युग्म कारण और निष्कर्ष है। पहली पंक्ति कारण देती है: ‘यतः’ उस समय सूर्य जगत् के स्नेह "
                   "(नमी, चिकनाई) को अत्यंत खींच लेता है। दूसरी पंक्ति ‘अतः’ से निष्कर्ष कहती है: "
                   "व्यायाम, धूप तथा कटु, अम्ल, लवण और उष्ण का त्याग करे। यहाँ ‘यतः’ कारण का और "
                   "‘अतः’ परिणाम का शब्द है। श्लोक इससे अधिक कोई मात्रा या उपाय नहीं बताता।"),
    "hook": "यतः सूर्य स्नेह खींचे, अतः व्यायाम-धूप-कटु-अम्ल-लवण-उष्ण त्यागे।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "What does the sun do in line 1, according to the unit?",
            ("It draws away the world's moisture", "आदत्ते जगतः स्नेहं भृशम्."),
            [("It gives back the world's moisture", "The verb आदत्ते means draws away, not gives."),
             ("It dries only the rivers", "The verse says the world's moisture, not only rivers."),
             ("It hides behind the clouds", "No cloud is mentioned.")],
            "Line 1: the sun strongly (भृशम्) draws away (आदत्ते) the moisture (स्नेहम्) of the world (जगतः).",
            "आदत्ते जगतः स्नेहं भृशम् — the sun draws away moisture." ),
        order(1, "Put the six things of line 2 in the order of the verse.",
              ["व्यायाम", "आतप", "कटु", "अम्ल", "लवण", "उष्ण"],
              "The line runs exercise, sun, pungent, sour, salty, hot.",
              "व्यायाम · आतप · कटु · अम्ल · लवण · उष्ण.", role="warmup"),
        fill(2, "The word for 'therefore' in line 2 is ____ (type it in Devanagari or in English letters, e.g. dharma).",
             accepts("अतः"),
             "अतः means therefore: it brings the result of the reason given in line 1.",
             "अतः ('from this, therefore') begins the result; यतः ('because') begins the reason.",
             "अतः = therefore.", role="extend"),
        mcq("discriminate", 3, "Which is the right split of त्यजेदतः?",
            ("त्यजेत् + अतः", "A final त् becomes द् before a vowel: त्यजेत् + अतः = त्यजेदतः."),
            [("त्यजेद् + तः", "तः is not a word here."),
             ("त्यजे + दतः", "दतः is not the word; the 'therefore' is अतः."),
             ("त्यजेः + अतः", "त्यजेः is a different person of the verb.")],
            "त्यजेत् (should avoid) + अतः (therefore).",
            "त् + vowel → द् + vowel."),
        mcq("apply", 4, "Which reason does the unit give for the avoidance?",
            ("the sun draws away the world's moisture", "यतः … आदित्यो भृशम्."),
            [("the wind blows pleasantly from every side", "Unit 43 says the wind is not pleasant."),
             ("the rivers have banks grown high", "That is in unit 45; it is not the stated reason here."),
             ("the earth is cold and still", "The units speak of blazing heat.")],
            "The word यतः (because) introduces the sun's drawing away moisture; अतः (therefore) leads to the avoiding.",
            "यतः = because (reason); अतः = therefore (result)."),
        mcq("transfer", 5,
            "In यतः मेघो गर्जति, अतः जनाः गृहं विशेयुः, which word introduces the result?",
            ("अतः", "अतः means therefore: it begins the result."),
            [("यतः", "यतः means because: it begins the reason."),
             ("जनाः", "जनाः is the subject, 'the people'."),
             ("गृहम्", "गृहम् is 'the house', the thing entered.")],
            "As in the verse, यतः gives the reason (the cloud thunders) and अतः the result (the people should enter the house).",
            "यतः … अतः = because … therefore.",
            teaches="यतः ('because') opens the reason and अतः ('therefore') opens the result that follows from it."),
    ],
}

# ---------------------------------------------------------------- unit 47
AUTHORED["47"] = {
    "title": "मद्यं न सेव्यं",
    "question": "What does the unit say about wine, and what follows otherwise?",
    "rule": ("Line 1: wine is not to be used (न सेव्यम्), or it is to be used little, or with much water. "
             "Line 2: otherwise (अन्यथा) it brings about śoṣa, slackness, burning and bewilderment."),
    "limits": ("The first line can be read as three options (not at all, little, with much water) or as "
               "'little wine' and 'wine with much water'; no question depends on that. शोष is drying-up "
               "or wasting and मोह bewilderment. The verse gives no amount."),
    "explain_hi": ("पहली पंक्ति मद्य के बारे में है: मद्य ‘न सेव्य’ है, अथवा थोड़ा, या बहुत जल मिलाकर "
                   "सेवन किया जाए। पंक्ति को दो ढंग से पढ़ा जा सकता है (तीन विकल्प, या ‘थोड़ा’ और "
                   "‘बहुत जल वाला’), पर सामग्री वही रहती है। दूसरी पंक्ति ‘अन्यथा’ (नहीं तो) कहकर "
                   "चार परिणाम गिनाती है: शोष, शिथिलता, दाह और मोह। कोई मात्रा नहीं बताई गई।"),
    "hook": "मद्य: न सेव्य, या थोड़ा, या बहुत जल के साथ; अन्यथा शोष-शिथिलता-दाह-मोह।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "Which of these does line 1 give as a way to use wine?",
            ("with much water", "सुबहुवारि is in line 1."),
            [("with much honey", "Honey is not named in line 1."),
             ("heated over a fire", "Heating is not mentioned."),
             ("only at night", "No time of day is named.")],
            "The line allows wine in small amount, or with much water (सुबहुवारि).",
            "मद्यं न सेव्यं, स्वल्पं वा, सुबहुवारि वा."),
        order(1, "Put the four results named in line 2 in the order of the verse.",
              ["शोष", "शैथिल्य", "दाह", "मोह"],
              "The line runs śoṣa, slackness, burning, bewilderment.",
              "शोष · शैथिल्य · दाह · मोह.", role="warmup"),
        match(2, "Match each word of line 2 to its meaning.",
              [["शोष", "drying-up"], ["शैथिल्य", "slackness"], ["दाह", "burning"],
               ["मोह", "bewilderment"], ["अन्यथा", "otherwise"]],
              "The four results and the word that introduces them.",
              "शोष = drying-up; शैथिल्य = slackness; दाह = burning; मोह = bewilderment; अन्यथा = otherwise.",
              role="extend",
              teaches="अन्यथा ('otherwise') says what happens if the condition just given is not kept."),
        mcq("discriminate", 3, "What does अन्यथा do in line 2?",
            ("it begins the results", "अन्यथा means otherwise."),
            [("it adds a further allowed use of wine", "It does not allow anything; it begins the results."),
             ("it gives the reason for line 1", "A reason would be introduced by यतः."),
             ("it names the amount of wine", "No amount is given in the unit.")],
            "अन्यथा (otherwise) turns from the conditions of line 1 to what follows if they are not kept.",
            "अन्यथा = otherwise."),
        mcq("apply", 4, "Which of these is NOT named in line 2 as a result?",
            ("swelling", "Swelling is not named in the unit."),
            [("burning", "दाह is the third result."),
             ("drying-up", "शोष is the first result."),
             ("bewilderment", "मोह is the fourth result.")],
            "Line 2 names four: śoṣa, slackness, burning, bewilderment. Swelling is not among them.",
            "Four results: शोष, शैथिल्य, दाह, मोह."),
        mcq("transfer", 5, "In the style of सेव्यम्, what does वन्द्यः गुरुः mean?",
            ("a teacher to be honoured", "-य after a verb root says 'to be done': वन्द्य = to be honoured."),
            [("a teacher who honoured", "That would be a past form."),
             ("a teacher who is honouring", "That would be a present participle."),
             ("a teacher honouring no one", "Nothing says this.")],
            "सेव्य is 'to be used', from √सेव्. In the same way वन्द्य is 'to be honoured', from √वन्द्.",
            "-य (gerundive) = to be done.",
            teaches="A word in -य made from a verb root (सेव्य, वन्द्य) means 'to be done': it says what should be used or honoured."),
    ],
}

# ---------------------------------------------------------------- unit 48
AUTHORED["48"] = {
    "title": "पानकानि समंथानि",
    "question": "What do the three describing words of line 2 say about the drinks?",
    "rule": ("Line 2 names drinks (पानकानि) that are with mantha (समन्थानि), rich in sugar "
             "(सिताढ्यानि) and cold (हिमानि). The four words all end in the neuter plural."),
    "limits": ("Line 1 is damaged in the print: तद्व्यानि is not a word and तोयानि (waters) is "
               "only a guess, so the card draws nothing from it. The verb is in unit 51. "
               "The questions use only the words of line 2 and their grammar."),
    "explain_hi": ("इस युग्म की पहली पंक्ति छपाई में बिगड़ी है (‘तद्व्यानि’ शब्द नहीं है, ‘तोयानि’ केवल "
                   "अनुमान है), इसलिए उस पर कुछ नहीं टिकाया गया। दूसरी पंक्ति साफ़ है: पानक, "
                   "मंथ से युक्त, शर्करा से भरपूर और शीतल। चारों शब्द नपुंसक बहुवचन हैं। क्रिया "
                   "(‘निषेवेत’) यहाँ नहीं, श्लोक ५१ में है, इसलिए पूरे वाक्य का अर्थ यहाँ से नहीं निकलता।"),
    "hook": "पानक: समंथ, सिताढ्य, हिम — चारों नपुंसक बहुवचन।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "In line 2, which word means 'cold'?",
            ("हिमानि", "हिम means cold."),
            [("सिताढ्यानि", "This means rich in sugar."),
             ("समन्थानि", "This means with mantha."),
             ("पानकानि", "This means drinks.")],
            "हिमानि is the word for cold; it stands at the end of line 2.",
            "हिमानि = cold."),
        match(1, "Match each word of line 2 to its meaning.",
              [["पानकानि", "drinks"], ["समन्थानि", "with mantha"],
               ["सिताढ्यानि", "rich in sugar"], ["हिमानि", "cold"], ["च", "and"]],
              "These are the five words of line 2.",
              "पानक = drink; समन्थ = with mantha; सिताढ्य = rich in sugar; हिम = cold.",
              role="warmup"),
        order(2, "Put the words of line 2 in the order of the verse.",
              ["पानकानि", "समन्थानि", "सिताढ्यानि", "हिमानि", "च"],
              "The line runs पानकानि, समन्थानि, सिताढ्यानि, हिमानि, च.",
              "पानकानि · समन्थानि · सिताढ्यानि · हिमानि · च.", role="extend",
              teaches="A line can be learned as a row of describing words after its noun: पानकानि first, then the three that describe it."),
        mcq("discriminate", 3, "Which is the right split of समन्थानि?",
            ("स + मन्थानि", "स- 'with' + मन्थानि: with mantha."),
            [("सम + न्थानि", "न्थानि is not a word."),
             ("समन् + थानि", "थानि is not a word."),
             ("सा + मन्थानि", "सा + म would stay long: सामन्थानि.")],
            "स (with) + मन्थानि: with mantha.",
            "स- = with."),
        mcq("apply", 4, "What gender and number do पानकानि, समन्थानि, सिताढ्यानि and हिमानि share?",
            ("neuter plural", "The data marks all four as neuter nominative plural."),
            [("masculine singular", "A masculine singular would not end in -आनि."),
             ("feminine plural", "A feminine plural would end differently, as in -आः."),
             ("neuter singular", "A neuter singular would end in -म्, as पानकम्.")],
            "All four end in -नि, the neuter plural, so they belong together.",
            "-आनि: neuter plural."),
        mcq("transfer", 5, "Which phrase means sweet fruits? फल is neuter.",
            ("मधुराणि फलानि", "Neuter plural describing word and noun, like हिमानि पानकानि."),
            [("मधुरः फलानि", "मधुरः is masculine singular; it does not agree."),
             ("मधुराणि फलम्", "The noun फलम् is singular here."),
             ("मधुराः फलानि", "मधुराः is masculine plural; it does not agree with a neuter noun.")],
            "A neuter plural noun (फलानि) takes neuter plural describing words (मधुराणि), as पानकानि takes हिमानि.",
            "Describing word and noun agree in gender and number.",
            teaches="A describing word agrees with its noun: a neuter plural noun takes a neuter plural describing word (-आणि/-आनि)."),
    ],
}

# ---------------------------------------------------------------- unit 49
AUTHORED["49"] = {
    "title": "स्वादुशीतं द्रवं चान्नं",
    "question": "What foods and drinks does this unit list?",
    "rule": ("Line 1: sweet, cold and liquid food, and dry-land (जाङ्गल) animals and birds. Line 2 "
             "lists six: śāli rice, milk, ghee, grapes, coconut water, sugar."),
    "limits": ("The verb that governs the list is निषेवेत, two units on (unit 51); this unit only lists. "
               "The unit names the animals and birds, not their flesh, which context implies. "
               "No amount, time or method is given."),
    "explain_hi": ("यह युग्म सूची है, क्रिया दो श्लोक आगे (‘निषेवेत’, श्लोक ५१) आती है। पहली पंक्ति: मधुर, शीत और "
                   "द्रव अन्न, तथा जांगल (शुष्क भूमि के) मृग और पक्षी। दूसरी पंक्ति में छह चीज़ें "
                   "हैं: शालि, दूध, घी, द्राक्षा, नारियल का जल और शर्करा। श्लोक में पशु-पक्षियों का नाम "
                   "है, ‘मांस’ शब्द नहीं; वह प्रसंग से समझा जाता है।"),
    "hook": "मधुर-शीत-द्रव अन्न, जांगल पशु-पक्षी; शालि, क्षीर, घृत, द्राक्षा, नारिकेरांबु, शर्करा।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "Which of these is named in line 2?",
            ("coconut water", "नारिकेरांबु is in line 2."),
            [("honey-water", "Honey-water is in unit 41, not here."),
             ("sugarcane juice", "Not named; the unit names sugar (शर्करा), not juice."),
             ("barley-water", "Not named; the grain is śāli rice.")],
            "Line 2 names śāli, milk, ghee, grapes, coconut water and sugar.",
            "शालि · क्षीर · घृत · द्राक्षा · नारिकेराम्बु · शर्करा."),
        order(1, "Put the six items of line 2 in the order of the verse.",
              ["शालि", "क्षीर", "घृत", "द्राक्षा", "नारिकेराम्बु", "शर्करा"],
              "The line runs śāli, milk, ghee, grapes, coconut water, sugar.",
              "शालि · क्षीर · घृत · द्राक्षा · नारिकेराम्बु · शर्करा.", role="warmup"),
        match(2, "Match each item of line 2 to its meaning.",
              [["क्षीर", "milk"], ["घृत", "ghee"], ["द्राक्षा", "grapes"],
               ["नारिकेराम्बु", "coconut water"], ["शर्करा", "sugar"]],
              "Five of the six items of line 2.",
              "क्षीर = milk; घृत = ghee; द्राक्षा = grapes; नारिकेर = coconut; अम्बु = water; शर्करा = sugar.",
              role="extend",
              teaches="नारिकेराम्बु is नारिकेर 'coconut' + अम्बु 'water': the first part says which water."),
        mcq("discriminate", 3, "Which is the right split of नारिकेरांबु?",
            ("नारिकेर + अम्बु", "अ + अ joins as आ: नारिकेर + अम्बु = नारिकेराम्बु."),
            [("नारिकेरा + आम्बु", "आम्बु is not a word."),
             ("नारिके + रांबु", "रांबु is not a word."),
             ("नारिकेरः + अम्बु", "A visarga would change into ओ before अ, not vanish.")],
            "नारिकेर (coconut) + अम्बु (water).",
            "अ + अ → आ."),
        mcq("apply", 4, "Which animals and birds does line 1 name?",
            ("dry-land (जाङ्गल) ones", "जाङ्गलान् मृगपक्षिणः."),
            [("water-dwelling ones", "The line says dry-land, not water-dwelling."),
             ("marsh-dwelling ones", "The line says dry-land, not marsh."),
             ("forest-dwelling ones", "The line says dry-land (जाङ्गल)." )],
            "Line 1 says जाङ्गल animals and birds, with the data's gloss 'dry-land'.",
            "जाङ्गल = dry-land."),
        mcq("transfer", 5, "Which is the right joining of द्राक्षा + अम्बु, grape-water?",
            ("द्राक्षाम्बु", "आ + अ joins as आ, like अ + अ in नारिकेराम्बु."),
            [("द्राक्षअम्बु", "The two vowels do not stand side by side."),
             ("द्राक्षोम्बु", "आ + अ does not become ओ."),
             ("द्राक्षैम्बु", "आ + अ does not become ऐ.")],
            "When a word ending in -आ meets अ, the two join as one long आ: द्राक्षा + अम्बु = द्राक्षाम्बु.",
            "अ/आ + अ → आ.",
            teaches="A word ending in -अ or -आ before अ joins into one long आ (नारिकेर + अम्बु; द्राक्षा + अम्बु = द्राक्षाम्बु)."),
    ],
}

# ---------------------------------------------------------------- unit 50
AUTHORED["50"] = {
    "title": "तालवृंतानिलान् हारान्",
    "question": "What things and persons does this unit list?",
    "rule": ("Line 1: breezes of palm-leaf fans, necklaces, garlands with lotuses and water-lilies. "
             "Line 2: slender beloved women (कान्ताः) with lotus-stalk bracelets, smeared with sandal."),
    "limits": ("The verb is निषेवेत, in unit 51. 'Slender' (तन्वी) could go with the women or the "
               "bracelets; the card reads it with the women. ‘स्रजः’ (garlands) is printed ‘स्त्रजः’, "
               "a slip. The unit only lists."),
    "explain_hi": ("यह भी सूची है, जिसकी क्रिया श्लोक ५१ में आती है। पहली पंक्ति: ताल के पंखों की हवाएँ, "
                   "हार, और कमल-उत्पल सहित मालाएँ। दूसरी पंक्ति: कमलनाल के कंगनों वाली, कृश, चंदन से "
                   "लिप्त प्रियतमाएँ। ‘तन्वी’ स्त्रियों का विशेषण पढ़ा गया है, पर वह कंगनों का भी हो सकता है। "
                   "छपा ‘स्त्रजः’ असल में ‘स्रजः’ है।"),
    "hook": "पंखे की हवा, हार, कमल-माला; कमलनाल-कंगन और चंदन वाली प्रियतमाएँ।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "With what are the garlands of line 1 said to come?",
            ("lotuses and water-lilies", "स्रजः सकमलोत्पलाः."),
            [("jasmine and champak", "Neither is named."),
             ("gold and pearls", "Neither is named; the necklaces are a separate item."),
             ("sandal and camphor", "Sandal is in line 2, applied to the women.")],
            "The garlands come with (स) lotuses (कमल) and water-lilies (उत्पल).",
            "सकमलोत्पलाः = with lotuses and water-lilies."),
        order(1, "Put the four listed things in the order of the verse.",
              ["breezes of palm-leaf fans", "necklaces", "garlands", "beloved women"],
              "Line 1 gives fan-breezes, necklaces and garlands; line 2 gives the women.",
              "तालवृन्तानिलाः · हाराः · स्रजः · कान्ताः.", role="warmup"),
        match(2, "Match each word of the unit to its meaning.",
              [["तालवृन्त", "palm-leaf fan"], ["हार", "necklace"], ["स्रज्", "garland"],
               ["मृणाल", "lotus-stalk"], ["कान्ता", "beloved woman"]],
              "Five of the things named in the two lines.",
              "तालवृन्त = palm-leaf fan; हार = necklace; स्रज् = garland; मृणाल = lotus-stalk.",
              role="extend",
              teaches="कान्ता is a woman who is loved (a beloved); it is feminine, and the plural is कान्ताः."),
        mcq("discriminate", 3, "Which is the right split of सकमलोत्पलाः?",
            ("स + कमल + उत्पलाः", "अ + उ joins as ओ: कमल + उत्पल = कमलोत्पल."),
            [("स + कमला + उत्पलाः", "कमला is not the word here; the lotus is कमल."),
             ("स + कमल + ओत्पलाः", "ओत्पल is not a word."),
             ("सः + कमल + उत्पलाः", "A visarga would not show here.")],
            "सकमलोत्पलाः = स (with) + कमल (lotus) + उत्पल (water-lily).",
            "अ + उ → ओ."),
        mcq("apply", 4, "How does line 2 describe the beloved women?",
            ("lotus-stalk bracelets, smeared with sandal", "मृणालवलयाः, चन्दनरूषिताः."),
            [("with gold bracelets, smeared with camphor paste", "The line says lotus-stalk and sandal."),
             ("with lotus garlands, smeared with musk", "The line says lotus-stalk bracelets and sandal."),
             ("with pearl bracelets, strewn with petals", "The line says lotus-stalk and sandal.")],
            "Line 2: slender, with lotus-stalk (मृणाल) bracelets (वलय), beloved, smeared with sandal (चन्दन).",
            "कान्ताः मृणालवलयाः चन्दनरूषिताः."),
        mcq("transfer", 5, "What does रत्नवलयाः कान्ताः mean, in the style of मृणालवलयाः?",
            ("women with bracelets of jewels", "A compound like X-वलयाः describes those who have X-bracelets."),
            [("women who are bracelets of jewels", "The compound describes the women; they are not bracelets."),
             ("jewels that are the bracelets of women", "The jewels are not the described subject."),
             ("women without bracelets", "Nothing in the compound negates the bracelets.")],
            "The compound रत्नवलयाः says 'having bracelets of jewels' and describes the women, as मृणालवलयाः does.",
            "X-वलय (describing) = having X-bracelets.",
            teaches="A compound like मृणालवलयाः describes a person as 'having lotus-stalk bracelets'; it agrees with the noun it describes (कान्ताः)."),
    ],
}

# ---------------------------------------------------------------- unit 51
AUTHORED["51"] = {
    "title": "सरांसि वापीः सरितः",
    "question": "What should one resort to, according to this unit?",
    "rule": ("One should resort to (निषेवेत) lakes, tanks, rivers and groves, cold and fragrant ones, and "
             "to very light garments (सुलघूनि वासांसि)."),
    "limits": ("हिमानि and सुरभीणि are neuter and could describe the water-places, the garments, or "
               "both; the card claims none of these. This is the verb that governs the list of "
               "units 48 to 50 as well. It gives no time or amount."),
    "explain_hi": ("यहाँ पिछले तीन श्लोकों की सूची की क्रिया आती है: ‘निषेवेत’ (सेवन करे)। पहली पंक्ति में सरोवर, "
                   "बावड़ियाँ, नदियाँ, वन और ‘हिमानि’ (शीतल) हैं; दूसरी पंक्ति में ‘सुरभीणि’ (सुगंधित), "
                   "क्रिया ‘निषेवेत’ और अत्यंत हल्के वस्त्र हैं। ‘हिमानि’ और ‘सुरभीणि’ किससे जुड़ते हैं, यह साफ़ नहीं: "
                   "जलस्थानों से, वस्त्रों से, या दोनों से।"),
    "hook": "सर, वापी, सरित्, कानन — शीतल-सुगंधित; और सुलघु वस्त्र: निषेवेत।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "Which of these does the unit say to resort to?",
            ("groves", "काननानि is in line 1."),
            [("mountains", "Mountains are not named."),
             ("deserts", "Deserts are not named."),
             ("markets", "Markets are not named.")],
            "Line 1 names lakes, tanks, rivers and groves.",
            "सरांसि · वापीः · सरितः · काननानि."),
        order(1, "Put the four places of line 1 in the order of the verse.",
              ["सरांसि", "वापीः", "सरितः", "काननानि"],
              "The line runs lakes, tanks, rivers, groves.",
              "सरांसि · वापीः · सरितः · काननानि.", role="warmup"),
        match(2, "Match each word of the unit to its meaning.",
              [["सरांसि", "lakes"], ["वापीः", "tanks"], ["सरितः", "rivers"],
               ["काननानि", "groves"], ["वासांसि", "garments"]],
              "Five things the unit names.",
              "सरांसि = lakes; वापीः = tanks; सरितः = rivers; काननानि = groves; वासांसि = garments.",
              role="extend",
              teaches="Nouns in the accusative plural name the things resorted to; the verb निषेवेत tells what is done to them."),
        fill(3, "The verb 'should resort to' in line 2 is ____ (type it in Devanagari or in English letters, e.g. dharma).",
             accepts("निषेवेत"),
             "निषेवेत is the 3rd person singular optative of नि-सेव्: 'should resort to'.",
             "निषेवेत: the 'should' form (-एत) of ni-sev, in the middle voice.",
             "निषेवेत = should resort to.", role="discriminate"),
        multi("apply", 4, "Which two words are feminine plural (accusative) in line 1?",
              [("वापीः", "Right: tanks, feminine accusative plural."),
               ("सरितः", "Right: rivers, feminine accusative plural."),
               ("सरांसि", "This is neuter plural."),
               ("काननानि", "This is neuter plural."),
               ("वासांसि", "This is neuter plural, and it stands in line 2.")],
              [0, 1],
              "The data marks वापीः and सरितः as feminine accusative plural; सरांसि and काननानि are neuter.",
              "वापीः, सरितः: feminine plural."),
        mcq("transfer", 5, "Which sentence means a student should serve the teacher?",
            ("शिष्यो गुरुं सेवेत", "-एत is the 'should' form, as in निषेवेत."),
            [("शिष्यो गुरुं सेवते", "सेवते is a plain present: 'serves'."),
             ("शिष्यो गुरुमसेवत", "असेवत is a past form: 'served'."),
             ("शिष्यो गुरुं सेविष्यते", "सेविष्यते is a future form: 'will serve'.")],
            "सेवेत has the same -एत ending as निषेवेत, so it says 'should serve'.",
            "-एत = should.",
            teaches="The ending -एत (निषेवेत, सेवेत) says what one 'should' do; the plain present, past and future have other endings."),
    ],
}

# ---------------------------------------------------------------- unit 52
AUTHORED["52"] = {
    "title": "निष्पतद्यंत्रसलिले",
    "question": "Where should one sleep by day and where by night?",
    "rule": ("By day (दिवा) one should sleep (स्वप्यात्) in a shower-house where water falls from a "
             "contrivance; at night (रात्रौ) on an open-air roof strewn with fragrant flowers."),
    "limits": ("'Water falling from a contrivance' avoids saying fountain; ākāśa-talaka is read as an "
               "open roof or terrace, literally sky-surface. The English ends with the second place only; "
               "the sentence goes on in unit 53. The unit says where, not how long."),
    "explain_hi": ("यह युग्म सोने की जगहें बताता है। दिन में ‘धारागृह’ में सोए, जहाँ यंत्र से जल गिर रहा हो। "
                   "रात में खुले आकाशतल (छत) पर सोए, जो सुगंधित फूलों से बिछा हो। क्रिया ‘स्वप्यात्’ "
                   "(सोए) है, यानी ‘सोना चाहिए’ का रूप। श्लोक केवल स्थान बताता है, अवधि या उपाय नहीं।"),
    "hook": "दिन में धारागृह (गिरता जल), रात में आकाशतल (सुगंधित फूल)।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "Where does the unit say one should sleep by day (दिवा)?",
            ("in a shower-house", "धारागृहे: in a shower-house."),
            [("on an open roof", "The open roof is for the night."),
             ("in a closed cellar", "No cellar is named."),
             ("under a tree", "No tree is named here.")],
            "दिवा (by day) goes with the shower-house where water falls from a contrivance.",
            "दिवा … धारागृहे."),
        order(1, "Put these words of the unit in the order of the verse.",
              ["निष्पतद्यन्त्रसलिले", "स्वप्यात्", "धारागृहे", "दिवा", "रात्रौ", "आकाशतलके"],
              "The unit runs: where water falls from a contrivance, should sleep, in the shower-house, by day, at night, on the open roof.",
              "निष्पतद्यन्त्रसलिले · स्वप्यात् · धारागृहे · दिवा · रात्रौ · आकाशतलके.",
              role="warmup"),
        fill(2, "The word for 'by day' is ____ (type it in Devanagari or in English letters, e.g. dharma).",
             accepts("दिवा"),
             "दिवा means by day, and it is paired with रात्रौ, at night.",
             "दिवा 'by day' and रात्रौ 'at night' set the two times of the unit against each other.",
             "दिवा = by day.", role="extend"),
        mcq("discriminate", 3, "Which is the right split of स्वप्याद्धारागृहे?",
            ("स्वप्यात् + धारागृहे", "A final त् becomes द् before a voiced sound: स्वप्यात् + धारा- = स्वप्याद्धारा-."),
            [("स्वप्याद् + आरागृहे", "आरागृहे is not a word."),
             ("स्वप्या + द्धारागृहे", "द्धारागृहे is not a word."),
             ("स्वप्यात + धारागृहे", "The verb ends in त्, not in a vowel.")],
            "स्वप्यात् (should sleep) + धारागृहे (in the shower-house).",
            "त् + voiced → द्."),
        mcq("apply", 4, "What does the unit say of the night place?",
            ("an open roof strewn with flowers", "आकाशतलके सुगन्धिकुसुमास्तृते."),
            [("a shower-house with falling water", "This is the day place."),
             ("a closed room smeared with sandal", "No closed room is named."),
             ("a high river bank", "River banks are in unit 45, not here.")],
            "At night (रात्रौ) one sleeps on the open roof (आकाशतलक) strewn with fragrant flowers.",
            "रात्रौ … आकाशतलके सुगन्धिकुसुमास्तृते."),
        mcq("transfer", 5, "Which sentence means one should sleep in the garden?",
            ("उद्याने स्वप्यात्", "The locative -ए says 'in', as in धारागृहे."),
            [("उद्यानात् स्वप्यात्", "-आत् says 'from the garden'."),
             ("उद्यानस्य स्वप्यात्", "-स्य says 'of the garden'."),
             ("उद्यानं स्वप्यात्", "-म् makes the garden the thing slept, not the place.")],
            "A noun in the locative (धारागृहे, आकाशतलके) tells where; उद्याने is the locative of उद्यान.",
            "Locative -ए = in.",
            teaches="The locative ending -ए (धारागृहे, उद्याने) tells the place where something is done."),
    ],
}

# ---------------------------------------------------------------- unit 53
AUTHORED["53"] = {
    "title": "कर्पूरचंदनार्द्रांगो",
    "question": "What two descriptions does line 1 give, and what does line 2 say of the rains?",
    "rule": ("Line 1 gives two descriptions, no noun named: limbs moistened with camphor and sandal, and rare "
             "union with Anaṅga (love). Line 2: in the rains (वर्षासु) the wind is Vāruṇa, and all "
             "crops spring up."),
    "limits": ("The two descriptions in line 1 are nominative singular, name no one and have no verb here: the "
               "sentence began in unit 52. 'Vāruṇa' may be 'western' or 'of Varuṇa'; the card keeps "
               "it untranslated. 'Anaṅga' is love, and the card does not say more."),
    "explain_hi": ("पहली पंक्ति में दो वर्णन हैं, पर जिसका वर्णन है उसका नाम नहीं आता: कपूर और चंदन से भीगे अंगों वाला, और "
                   "विरल कामसंग वाला (‘अनंग’ = प्रेम या काम)। क्रिया पिछले श्लोक से चलती है। दूसरी पंक्ति नया "
                   "विषय खोलती है: वर्षा में वायु ‘वारुण’ है और सब धान्यों का उगना होता है। "
                   "‘वारुण’ का अर्थ ‘पश्चिमी’ या ‘वरुण-संबंधी’ दोनों हो सकता है, इसलिए उस पर प्रश्न नहीं बना।"),
    "hook": "कपूर-चंदन से भीगे अंग; वर्षा में वारुण वायु और सब धान्यों का उगना।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "With what are the limbs moistened, according to line 1?",
            ("camphor and sandal", "कर्पूरचन्दनार्द्राङ्गः."),
            [("musk and saffron", "Neither is named."),
             ("water and flowers", "Water and flowers are in the earlier unit, not here."),
             ("ghee and honey", "Neither is named.")],
            "आर्द्र (moist) अङ्ग (limbs) with camphor (कर्पूर) and sandal (चन्दन).",
            "कर्पूरचन्दनार्द्राङ्गः."),
        order(1, "Put these parts of the unit in the order of the verse.",
              ["limbs moistened with camphor and sandal", "rare union with Anaṅga",
               "in the rains", "the wind is Vāruṇa", "all crops spring up"],
              "Line 1 gives the two descriptions; line 2 gives the rains, the wind and the crops.",
              "कर्पूरचन्दनार्द्राङ्गः · विरलानङ्गसङ्गमः · वर्षासु · वारुणो वायुः · सर्वसस्यसमुद्गमः.",
              role="warmup"),
        match(2, "Match each word of line 2 to its meaning.",
              [["वर्षासु", "in the rains"], ["वायुः", "wind"], ["सर्व", "all"],
               ["सस्य", "crop"], ["समुद्गमः", "springing up"]],
              "Five words that carry the sense of line 2.",
              "वर्षासु = in the rains; वायुः = wind; सर्व = all; सस्य = crop; समुद्गम = springing up.",
              role="extend",
              teaches="वर्षासु is the locative plural of the feminine वर्षा, used for the rainy months: 'in the rains'."),
        mcq("discriminate", 3, "Which is the right split of वारुणो वायुः?",
            ("वारुणः + वायुः", "-अः before a voiced sound (व) becomes ओ."),
            [("वारुणाः + वायुः", "That would join as वारुणा वायुः, with a long vowel."),
             ("वारुणे + वायुः", "ए does not turn into ओ."),
             ("वारुणम् + वायुः", "-म् would stay as -म् or -ं, not become ओ.")],
            "वारुणः (Vāruṇa, kept untranslated) + वायुः (wind): the visarga becomes ओ before the voiced व.",
            "-अः + voiced → ओ."),
        mcq("apply", 4, "What does line 2 say springs up in the rains?",
            ("all crops", "सर्वसस्यसमुद्गमः."),
            [("only the grass", "The line says all crops."),
             ("only the lotuses", "Lotuses are named in unit 50; the line says all crops."),
             ("all the rivers", "The line does not speak of rivers.")],
            "Line 2: in the rains the wind is Vāruṇa, and all crops (सर्वसस्य) spring up (समुद्गम).",
            "सर्वसस्यसमुद्गमः = springing up of all crops."),
        mcq("transfer", 5, "Which means in the garlands? माला is feminine, like वर्षा.",
            ("मालासु", "-आसु is the locative plural of feminine -आ nouns, as वर्षासु."),
            [("मालायाम्", "This is the locative singular, 'in the garland'."),
             ("मालाभिः", "This is the instrumental plural, 'by the garlands'."),
             ("मालानाम्", "This is the genitive plural, 'of the garlands'.")],
            "वर्षा gives वर्षासु; माला is declined the same way, so 'in the garlands' is मालासु.",
            "Feminine -आ: loc. pl. -आसु.",
            teaches="Feminine nouns in -आ form the locative plural in -आसु (वर्षासु = in the rains; मालासु = in the garlands)."),
    ],
}

NOTES_HI = {
    "41": "विश्वास: मध्यम। छपे ‘कथितमुस्तशुंठ्यंबु’ में ‘कथित’ शायद ‘क्वथित’ (उबाला) है; यह केवल सुझाव है। ‘सार’ के अनेक अर्थ हैं, इसलिए ‘सार-जल’ रखा गया। ‘निर्गद’ का अक्षरशः अर्थ ‘रोगरहित’ है। सन्धि: निर्गदान् + च + आसव → निर्गदांश्चासव; वारि का समास ‘क्षौद्र-वारि’। छपे युग्म में पिछला आधा श्लोक इस पंक्ति से जुड़ता है।",
    "42": "विश्वास: मध्यम। दूसरी पंक्ति में क्रिया नहीं है; विशेषण सूर्य के माने गए हैं। ‘दावदीपितः’ का अक्षरशः अर्थ ‘दावानल से जलाया गया’ है, शायद ‘दावानल जैसा दहकता’। सन्धि: मधुरान् + त्यजेत् → मधुरांस्त्यजेत्; ग्रीष्मे + अतसी → ग्रीष्मे ऽतसी (ए + अ → ए, अवग्रह छपा); तीक्ष्णांशुः = तीक्ष्ण + अंशुः (अ + अ → आ)।",
    "43": "विश्वास: उच्च। ‘नैकतः’ = न + एकतः (अ + ए → ऐ); अक्षरशः ‘एक ओर से नहीं’, यहाँ ‘किसी ओर से नहीं’ पढ़ा गया। सन्धि: दिशः + ज्वलन्ति → दिशो ज्वलन्ति; भूमिः + च → भूमिश्च; मारुतः + न → मारुतो न; जन्तवः + ज्वरिताः → जन्तवो ज्वरिता (छपे ‘ज्वरिता’ में अन्त का विसर्ग छूटा है, गलती नहीं)। ‘ज्वरित’ = ज्वर से प्रभावित।",
    "44": "विश्वास: उच्च। दोनों विशेषण स्त्रीलिंग बहुवचन हैं और संज्ञा ‘नद्यः’ अगले श्लोक में है। ‘तुंग’ को ‘मातंग’ के साथ, ‘तापार्त’ को दोनों पशुओं के साथ लिया गया है। सन्धि: ताप + आर्त → तापार्त; दिवाकर + कर + अंगार → दिवाकरकरांगार; क्षपित + अंभसः → क्षपितांभसः (अ + अ → आ)।",
    "45": "विश्वास: उच्च। ‘प्रवृद्धरोधसः’ का अर्थ ‘बढ़े हुए तट’ है; तट शायद जल घटने से ऊँचे दिखते हैं (पिछले श्लोक की तुलना), पर यह अनुमान है। सन्धि: नद्यः + छायाहीनाः → नद्यश्छायाहीनाः (छपे ‘छायाहीना’ में अन्त का विसर्ग छूटा है, गलती नहीं); विशीर्णजीर्णपर्णाः + च → ..पर्णाश्च; शुष्क + वल्कल + लता + अंकिताः → शुष्कवल्कलतांकिताः (आ + अ → आ)।",
    "46": "विश्वास: उच्च। ‘स्नेह’ = तेल/चिकनाई/नमी; ‘नमी (स्नेह)’ रखा गया। ‘तदा’ = उस समय (पिछले ग्रीष्म-वर्णन की ओर इशारा)। सन्धि: तदा + आदित्यः → तदादित्यः; व्यायाम + आतप → व्यायामातप; कटु + अम्ल → कट्वम्ल (उ + अ → व); लवण + उष्णम् → लवणोष्णम्; त्यजेत् + अतः → त्यजेदतः।",
    "47": "विश्वास: उच्च। पहली पंक्ति दो ढंग से पढ़ी जा सकती है: तीन विकल्प (न सेव्य / थोड़ा / बहुत जल के साथ), या ‘थोड़ा मद्य’ और ‘बहुत जल वाला मद्य’। ‘शोष’ = सूखना/क्षीणता; ‘मोह’ = भ्रम। सन्धि: मद्यं न सेव्यं (छपे ‘नसेव्यं’ में सिर्फ़ स्पेस छूटा है); शोष..मोहान् + करोति → ..मोहान्करोति; सेव्य + सुबहुवारि।",
    "48": "विश्वास: निम्न। पहली पंक्ति (४.७४) छपाई में बिगड़ी है: ‘तद्व्यानि’ शब्द नहीं है; सुझाव ‘तोयानि’ (जल) या ‘तद्द्रव्याणि’ केवल अनुमान हैं। इसलिए प्रश्न केवल दूसरी पंक्ति के साफ़ शब्दों और उनके व्याकरण पर बने हैं। ‘मंथ’ एक मथा हुआ पेय है, नाम ही रखा गया। सन्धि: सित/सिता + आढ्यानि → सिताढ्यानि (दोनों विभाजन सम्भव: अ + आ → आ या आ + आ → आ; सिता = शर्करा, सित = श्वेत); स + मन्थानि → समन्थानि।",
    "49": "विश्वास: उच्च। क्रिया ‘निषेवेत’ आगे के श्लोक में है। ‘जांगल’ = शुष्क भूमि का। मृग-पक्षिणः के साथ ‘मांस’ शब्द नहीं, वह प्रसंग से समझा जाता है। ‘शालि’ चावल की किस्म है, नाम रखा गया। सन्धि: जांगलान् + मृगपक्षिणः → जांगलान्मृगपक्षिणः; नारिकेर + अंबु → नारिकेरांबु; द्राक्षा + नारिकेर → द्राक्षानारिकेर।",
    "50": "विश्वास: उच्च। छपा ‘स्त्रजः’ सम्भवतः ‘स्रजः’ है (स्रज् में त नहीं)। ‘तन्वी’ स्त्रियों का विशेषण पढ़ा गया है; यह कंगनों का भी हो सकता है। सन्धि: ताल + वृन्त + अनिलान् → तालवृन्तानिलान्; स + कमल + उत्पलाः → सकमलोत्पलाः (अ + उ → ओ); कान्ताः + चन्दन → कान्ताश्चन्दन।",
    "51": "विश्वास: उच्च। ‘सुरभीणि’ जलस्थानों, वस्त्रों या दोनों से जुड़ सकता है। ‘वापी’ = बावड़ी/सरोवर। क्रिया ‘निषेवेत’ (आत्मनेपद, विधिलिङ्) पिछले तीन श्लोकों की सूचियों की भी है। सन्धि: सरितः + काननानि → सरितः काननानि (अलग छपे); निषेवेत + वासांसि।",
    "52": "विश्वास: उच्च। ‘यन्त्र’ = कोई उपकरण; ‘आकाशतलक’ का अक्षरशः अर्थ ‘आकाश का तल’, खुली छत पढ़ा गया। सन्धि: स्वप्यात् + धारागृहे → स्वप्याद्धारागृहे; रात्रौ + च + आकाशतलके → रात्रौ चाकाशतलके (अ + आ → आ); सुगन्धि + कुसुम + आस्तृते → सुगन्धिकुसुमास्तृते (अ + आ → आ)।",
    "53": "विश्वास: उच्च। ‘अनंग’ कामदेव/काम; ‘अनंगसंगम’ = कामसंग। ‘वारुण’ का अर्थ ‘पश्चिमी’ या ‘वरुण-संबंधी’, दोनों सम्भव। ‘वर्षासु’ बहुवचन है (वर्षा के महीने)। सन्धि: कर्पूर + चन्दन + आर्द्र + अङ्गः → कर्पूरचन्दनार्द्राङ्गः; विरल + अनङ्ग → विरलानङ्ग; वारुणः + वायुः → वारुणो वायुः।",
}

AIDS = {
    "41": {
        "diagram": {"groups": [
            {"label": "पहली पंक्ति: पाँच पेय",
             "items": ["आसव", "अरिष्ट", "सीधु", "मार्द्वीक", "माधव"]},
            {"label": "दूसरी पंक्ति: तीन जल (वा)",
             "items": ["मुस्त-शुंठी वाला जल", "सारांभः", "क्षौद्रवारि"]}]},
        "sandhi": "न् + च → ंश्च: निर्गदान् + च + आसव → निर्गदांश्चासव · च + आ → चा।",
        "chunks": "निर्गदांश्चासवारिष्टसीधुमार्द्वीकमाधवान् ‖ कथितमुस्तशुंठ्यंबु | सारांभः | क्षौद्रवारि वा।",
        "anchors": "पाँच नाम ‘आ-अ-सी-मा-मा’ (मेरा बनाया स्मरण-सूत्र): आसव, अरिष्ट, सीधु, मार्द्वीक, माधव · फिर तीन जल।",
    },
    "42": {
        "diagram": {"groups": [
            {"label": "छोड़े (त्यजेत्)",
             "items": ["गुरु", "शीत", "दिवास्वप्न", "स्निग्ध", "अम्ल", "मधुर"]},
            {"label": "ग्रीष्मे: वर्णन",
             "items": ["अतसीपुष्पनिभः", "तीक्ष्णांशुः", "दावदीपितः"]}]},
        "sandhi": "न् + त → ंस्त: मधुरान् + त्यजेत् → मधुरांस्त्यजेत् · ए + अ → ए ऽ: ग्रीष्मे + अतसी → ग्रीष्मे ऽतसी।",
        "chunks": "गुरुशीतदिवास्वप्नस्निग्धाम्लमधुरांस्त्यजेत् ‖ ग्रीष्मे ऽतसीपुष्पनिभः | तीक्ष्णांशुः | दावदीपितः।",
        "contrast": "छोड़ने की सूची में ‘स्निग्ध, अम्ल, मधुर’ साथ आते हैं, जबकि ‘गुरु-शीत’ पहले जोड़े में।",
    },
    "43": {
        "diagram": {"groups": [
            {"label": "पहली पंक्ति",
             "items": ["दिशः ज्वलन्ति", "भूमिः च", "मारुतः न एकतः सुखः"]},
            {"label": "दूसरी पंक्ति",
             "items": ["पवन-आतप-संस्वेदैः", "जन्तवः", "ज्वरिताः इव"]}]},
        "sandhi": "अः + ज → ओ ज: दिशः + ज्वलन्ति → दिशोज्वलन्ति · अ + ए → ऐ: न + एकतः → नैकतः।",
        "chunks": "दिशोज्वलन्ति भूमिश्च | मारुतो नैकतः सुखः ‖ पवनातपसंस्वेदैः | जन्तवो ज्वरिता इव।",
        "letters": "द-भू-मा: दिशः, भूमिः, मारुतः — पहली पंक्ति के तीन कर्ता (मेरा बनाया स्मरण-सूत्र)।",
    },
    "44": {
        "diagram": {"groups": [
            {"label": "पहली पंक्ति",
             "items": ["तापार्त", "तुंग", "मातंग", "महिषैः", "कलुषीकृताः"]},
            {"label": "दूसरी पंक्ति (एक समास)",
             "items": ["दिवाकर", "कर", "अंगार", "निकर", "क्षपित", "अंभसः"]}]},
        "sandhi": "अ + आ → आ: ताप + आर्त → तापार्त · अ + अ → आ: क्षपित + अंभसः → क्षपितांभसः।",
        "chunks": "तापार्ततुंगमातंगमहिषैः | कलुषीकृताः ‖ दिवाकरकरांगारनिकरक्षपितांभसः।",
    },
    "45": {
        "diagram": {"groups": [
            {"label": "पहली पंक्ति",
             "items": ["प्रवृद्धरोधसः नद्यः", "छायाहीनाः महीरुहाः"]},
            {"label": "दूसरी पंक्ति",
             "items": ["विशीर्णजीर्णपर्णाः", "शुष्कवल्कललताङ्किताः"]}]},
        "sandhi": "ः + छ → श्छ: नद्यः + छायाहीनाः → नद्यश्छायाहीनाः · ः + च → श्च: पर्णाः + च → पर्णाश्च।",
        "chunks": "प्रवृद्धरोधसो नद्यश्छायाहीना महीरुहाः ‖ विशीर्णजीर्णपर्णाश्च | शुष्कवल्कलतांकिताः।",
    },
    "46": {
        "diagram": {"groups": [
            {"label": "कारण (यतः)",
             "items": ["आदत्ते", "जगतः स्नेहम्", "आदित्यः", "भृशम्"]},
            {"label": "निष्कर्ष (अतः): त्यजेत्",
             "items": ["व्यायाम", "आतप", "कटु", "अम्ल", "लवण", "उष्ण"]}]},
        "frame": "क्योंकि सूर्य जगत् का स्नेह खींचता है, इसलिए ये छह छोड़े: व्यायाम, आतप, कटु, अम्ल, लवण, उष्ण।",
        "sandhi": "त् + अ → द् + अ: त्यजेत् + अतः → त्यजेदतः · आ + आ → आ: तदा + आदित्यः → तदादित्यः।",
        "chunks": "आदत्ते जगतः स्नेहं | तदादित्यो भृशं यतः ‖ व्यायामातपकट्वम्ललवणोष्णं | त्यजेदतः।",
    },
    "47": {
        "diagram": {"groups": [
            {"label": "पहली पंक्ति: मद्य",
             "items": ["न सेव्यम्", "स्वल्पम् वा", "सेव्यम् सुबहुवारि वा"]},
            {"label": "अन्यथा: चार परिणाम",
             "items": ["शोष", "शैथिल्य", "दाह", "मोह"]}]},
        "frame": "मद्य: न सेव्य / थोड़ा / बहुत जल के साथ; अन्यथा चार: शोष, शैथिल्य, दाह, मोह।",
        "chunks": "मद्यं न सेव्यं | स्वल्पं वा सेव्यं | सुबहुवारि वा ‖ अन्यथा | शोषशैथिल्यदाहमोहान्करोति तत्।",
        "sandhi": "छपे में मोहान्करोति और नसेव्यं जुड़े हैं (कोई संधि-परिवर्तन नहीं); शब्द हैं मोहान् + करोति, न + सेव्यम्।",
    },
    "48": {
        "diagram": {"groups": [
            {"label": "दूसरी पंक्ति के शब्द",
             "items": ["पानकानि", "समन्थानि", "सिताढ्यानि", "हिमानि", "च"]}]},
        "sandhi": "अ/आ + आ → आ: सित(ा) + आढ्यानि → सिताढ्यानि (सिता = शर्करा; सित = श्वेत)।",
        "chunks": "नवमृद्भाजनस्थानि तद्व्यानि (पाठ अस्पष्ट) सुरभीणि च ‖ पानकानि | समंथानि | सिताढ्यानि | हिमानि च।",
        "anchors": "चारों शब्द -नि पर समाप्त: नपुंसक बहुवचन — पानकानि के साथ जुड़े।",
    },
    "49": {
        "diagram": {"groups": [
            {"label": "पहली पंक्ति",
             "items": ["स्वादु शीतं द्रवं च अन्नम्", "जांगलान् मृगपक्षिणः"]},
            {"label": "दूसरी पंक्ति: छह",
             "items": ["शालि", "क्षीर", "घृत", "द्राक्षा", "नारिकेराम्बु", "शर्करा"]}]},
        "sandhi": "अ + अ → आ: नारिकेर + अम्बु → नारिकेराम्बु · जांगलान् + मृग: म से पहले न् ज्यों का त्यों रहता है, कोई परिवर्तन नहीं (छपा जांगलान्मृग)।",
        "chunks": "स्वादुशीतं द्रवं चान्नं | जांगलान्मृगपक्षिणः ‖ शालिक्षीरघृतद्राक्षानारिकेरांबुशर्कराः।",
        "anchors": "छह: शालि, क्षीर, घृत, द्राक्षा, नारियल-जल, शर्करा — पहला शब्द ‘शा’ से, अंतिम ‘श’ से (मेरा बनाया स्मरण-सूत्र)।",
    },
    "50": {
        "diagram": {"groups": [
            {"label": "पहली पंक्ति",
             "items": ["तालवृन्तानिलान्", "हारान्", "स्रजः सकमलोत्पलाः"]},
            {"label": "दूसरी पंक्ति",
             "items": ["तन्वी", "मृणालवलयाः", "कान्ताः", "चन्दनरूषिताः"]}]},
        "sandhi": "अ + उ → ओ: कमल + उत्पलाः → कमलोत्पलाः · अ + अ → आ: तालवृन्त + अनिलान् → तालवृन्तानिलान्।",
        "chunks": "तालवृंतानिलान् हारान् | स्त्रजः सकमलोत्पलाः ‖ तन्वीमृणालवलयाः | कांताश्चंदनरूषिताः।",
    },
    "51": {
        "diagram": {"groups": [
            {"label": "पहली पंक्ति",
             "items": ["सरांसि", "वापीः", "सरितः", "काननानि", "हिमानि च"]},
            {"label": "दूसरी पंक्ति",
             "items": ["सुरभीणि", "निषेवेत", "वासांसि", "सुलघूनि च"]}]},
        "frame": "क्रिया ‘निषेवेत’ (सेवन करे) के कर्म: सरोवर, बावड़ी, नदी, वन और हल्के वस्त्र।",
        "chunks": "सरांसि वापीः सरितः | काननानि हिमानि च ‖ सुरभीणि निषेवेत | वासांसि सुलघूनि च।",
        "anchors": "चार स्थान: सर · वापी · सरित् · कानन — ‘स-वा-स-का’। मेरा बनाया स्मरण-सूत्र।",
    },
    "52": {
        "diagram": {"groups": [
            {"label": "दिन में (दिवा)",
             "items": ["निष्पतद्यन्त्रसलिले", "स्वप्यात्", "धारागृहे"]},
            {"label": "रात में (रात्रौ)",
             "items": ["आकाशतलके", "सुगन्धिकुसुमास्तृते"]}]},
        "contrast": "दिन: धारागृह, यंत्र से गिरता जल ↔ रात: खुला आकाशतल, सुगंधित फूलों से बिछा।",
        "sandhi": "त् + ध → द्ध: स्वप्यात् + धारागृहे → स्वप्याद्धारागृहे · अ + आ → आ: च + आकाशतलके → चाकाशतलके।",
        "chunks": "निष्पतद्यंत्रसलिले | स्वप्याद्धारागृहे दिवा ‖ रात्रौ चाकाशतलके | सुगंधिकुसुमास्तृते।",
    },
    "53": {
        "diagram": {"groups": [
            {"label": "पहली पंक्ति",
             "items": ["कर्पूरचन्दनार्द्राङ्गः", "विरलानङ्गसङ्गमः"]},
            {"label": "दूसरी पंक्ति",
             "items": ["वर्षासु", "वारुणः वायुः", "सर्वसस्यसमुद्गमः"]}]},
        "sandhi": "अः + व → ओ व: वारुणः + वायुः → वारुणो वायुः · अ + आ → आ: चन्दन + आर्द्र → चन्दनार्द्र।",
        "chunks": "कर्पूरचंदनार्द्रांगो | विरलानंगसंगमः ‖ वर्षासु वारुणो वायुः | सर्वसस्यसमुद्गमः।",
    },
}

IMAGE_SPECS = {
    ("42", "diagram"): {
        "file": "ch4b04-42-avoid-list.svg",
        "alt": "Mind map of the line 1 list in verse 42: six things to avoid: heavy, cold, day-sleep, unctuous, sour, sweet (listed in the verse order; the picture's layout is not the verse order).",
        "type": "mermaid",
        "code": """mindmap
  त्यजेत्
    गुरु
    शीत
    दिवास्वप्न
    स्निग्ध
    अम्ल
    मधुर""",
    },
    ("46", "frame"): {
        "file": "ch4b04-46-reason-result.svg",
        "alt": "Flowchart of verse 46: because the sun strongly draws away the world's moisture, therefore one should avoid six things: exercise, sun, pungent, sour, salty, hot.",
        "type": "mermaid",
        "code": """flowchart TD
  A["यतः (कारण): सूर्य जगत् का<br/>स्नेह खींचता है"] --> B["अतः (निष्कर्ष): त्यजेत्"]
  B --> C["व्यायाम"]
  B --> D["आतप"]
  B --> E["कटु"]
  B --> F["अम्ल"]
  B --> G["लवण"]
  B --> H["उष्ण"]""",
    },
    ("47", "frame"): {
        "file": "ch4b04-47-madya.svg",
        "alt": "Flowchart of verse 47: for wine the verse says not to be used, or a little, or with much water; otherwise four results: drying-up, slackness, burning, bewilderment.",
        "type": "mermaid",
        "code": """flowchart TD
  A["मद्य: न सेव्य, या स्वल्प,<br/>या सुबहुवारि"] --> E["अन्यथा"]
  E --> F["शोष"]
  E --> G["शैथिल्य"]
  E --> H["दाह"]
  E --> I["मोह"]""",
    },
    ("49", "diagram"): {
        "file": "ch4b04-49-list.svg",
        "alt": "Mind map of verse 49: sweet cold liquid food, dry-land animals and birds, and the six items śāli rice, milk, ghee, grapes, coconut water, sugar (listed in the verse order; the picture's layout is not the verse order).",
        "type": "mermaid",
        "code": """mindmap
  सूची
    अन्न
      स्वादु शीत द्रव
    जांगल
      मृग और पक्षी
    छह वस्तुएँ
      शालि
      क्षीर
      घृत
      द्राक्षा
      नारिकेराम्बु
      शर्करा""",
    },
    ("51", "frame"): {
        "file": "ch4b04-51-resort.svg",
        "alt": "Mind map of verse 51: what one should resort to: lakes, tanks, rivers, groves, and very light garments (the picture's layout is not the verse order: lakes, tanks, rivers, groves, then garments).",
        "type": "mermaid",
        "code": """mindmap
  निषेवेत
    सरांसि
    वापीः
    सरितः
    काननानि
    सुलघु वासांसि""",
    },
    ("52", "contrast"): {
        "file": "ch4b04-52-day-night.svg",
        "alt": "Two columns for verse 52: by day, a shower-house where water falls from a contrivance; at night, an open roof strewn with fragrant flowers.",
        "type": "split",
        "title": "सोने के स्थान",
        "cols": [["दिन में", ["धारागृह", "यंत्र से गिरता जल"]],
                 ["रात में", ["खुला आकाशतल", "सुगंधित फूलों से बिछा"]]],
    },
}
