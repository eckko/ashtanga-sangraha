from helpers import mcq, match, order, fill, multi, accepts

AUTHORED = {}

# ---------------------------------------------------------------- unit 39
AUTHORED["39"] = {
    "title": "तौ षोढा दशधा चोक्तौ",
    "question": "How does verse 39 divide 'those two', and which dhātus does it name?",
    "rule": ("Those two are said to be sixfold and tenfold through variations such as excess; "
             "the dhātus are rasa, blood, flesh, fat, bone, marrow and semen, in this order."),
    "limits": ("'Those two' point back to the previous verse (the notes read them as saṃsarga and sannipāta); "
               "this verse does not name them. The number seven for the dhātus is not stated here, "
               "and the verse says nothing about what each dhātu does."),
    "explain_hi": ("पहली पंक्ति पिछले श्लोक की दो चीज़ों (‘तौ’ यानी वे दोनों) के बारे में है: उत्कर्ष (अधिकता) आदि के भेदों से उन्हें छह प्रकार का "
                   "और दस प्रकार का कहा गया है। दूसरी पंक्ति एक नई सूची शुरू करती है: रस, असृक् (रक्त), मांस, मेद, अस्थि, मज्जा और शुक्र, ये धातुएँ हैं। "
                   "सूची एक ही समास में है, इसलिए क्रम पक्का याद करने लायक है। ‘सात’ की गिनती इस श्लोक में नहीं, अगले श्लोक में आती है।"),
    "hook": "छह-दस के भेद उत्कर्ष आदि से; धातु: रस, असृक्, मांस, मेद, अस्थि, मज्जा, शुक्र।",
    "core": True,
    "questions": [
        mcq("pretest", 0,
            "Which dhātu does the second line of verse 39 name first?",
            ("रस", "The compound opens with रस."),
            [("मांस", "मांस is the third item, after रस and असृक्."),
             ("अस्थि", "अस्थि is the fifth item."),
             ("शुक्र", "शुक्र comes last in the list.")],
            "रसासृङ्मांसमेदोस्थिमज्जाशुक्राणि begins with रस and ends with शुक्र.",
            "The dhātus in order: रस, असृक्, मांस, मेद, अस्थि, मज्जा, शुक्र."),
        order(1, "Arrange the first six dhātus of the line in the verse's order.",
              ["रस", "असृक्", "मांस", "मेद", "अस्थि", "मज्जा"],
              "The verse names them in this order; शुक्र follows as the seventh.",
              "रस → असृक् → मांस → मेद → अस्थि → मज्जा → शुक्र."),
        match(2, "Match each dhātu word of the verse to its meaning.",
              [["असृक्", "blood"], ["मेद", "fat"], ["मज्जा", "marrow"], ["शुक्र", "semen"]],
              "These four words are glossed in the card as blood, fat, marrow and semen.",
              "असृक् = blood; मेद = fat; मज्जा = marrow; शुक्र = semen.", role="extend"),
        mcq("discriminate", 3, "Which is the right split of चोक्तावुत्कर्षादिविकल्पनात्?",
            ("च + उक्तौ + उत्कर्षादिविकल्पनात्",
             "च + उ gives चो; and उक्तौ before the vowel उ turns into उक्ताव्."),
            [("च + उक्ता + उत्कर्षादिविकल्पनात्", "The form is dual उक्तौ, agreeing with तौ; उक्ता would be feminine singular."),
             ("च + उक्तौ + त्कर्षादिविकल्पनात्", "The word is उत्कर्ष; its first उ belongs to it."),
             ("चो + उक्तौ + उत्कर्षादिविकल्पनात्", "चो is not a word; the ओ comes from the join of च and उ.")],
            "चोक्तावुत्कर्षादिविकल्पनात् = च + उक्तौ + उत्कर्ष-आदि-विकल्पनात्.",
            "अ + उ → ओ (च + उक्तौ → चोक्तौ); औ before a vowel → आव् (उक्तौ + उ → उक्ताव्-उ)."),
        mcq("apply", 4,
            "According to line 1, through what are the two called sixfold and tenfold?",
            ("Variations such as excess (उत्कर्ष)", "उत्कर्षादिविकल्पनात् gives this reason."),
            [("The seven dhātus of the next line", "The second line begins a separate list."),
             ("The number of foods taken", "The verse does not mention foods."),
             ("The season of the year", "The verse does not mention seasons.")],
            "उत्कर्षादिविकल्पनात् = from the variations (विकल्पन) by excess and the like.",
            "Sixfold and tenfold come from variations such as excess."),
        mcq("transfer", 5,
            "In a new line, भेदात् follows the pattern of विकल्पनात्. What does it mean?",
            ("From (through) the division", "-आत् is the ablative singular, like विकल्पनात् 'through the variation'."),
            [("Of the division", "Of would be the genitive, भेदस्य."),
             ("In the division", "In would be the locative, भेदे."),
             ("O division!", "A call would be the vocative, भेद.")],
            "भेदात् is the ablative singular of भेद, the same ending as विकल्पनात्.",
            "-आत् at the end of a masculine or neuter noun = ablative singular: from, through.",
            teaches="विकल्पनात् is the ablative singular; any a-stem noun takes the same -आत् ending for 'from' or 'through'."),
    ],
}

# ---------------------------------------------------------------- unit 40
AUTHORED["40"] = {
    "title": "सप्त दूष्या मलाः",
    "question": "What does line 1 of verse 40 name as dūṣyas and malas, and where do the diseases of line 2 arise?",
    "rule": ("Dūṣyas (what can be vitiated) and malas: urine, faeces, sweat and the like. "
             "Line 2 begins a clause: diseases that arise when the doṣas abide in rasa and the others."),
    "limits": ("'Sapta' is read as the seven dhātus of the previous verse, and the last pair "
               "is elliptical: the malas are also dūṣya, or malas in addition. The card does not rest on that choice. "
               "The clause of line 2 is completed in the next verse."),
    "explain_hi": ("पहली पंक्ति में ‘दूष्य’ यानी जो दूषित हो सकता है, और ‘मल’ आते हैं: मूत्र, शकृत् (मल) और स्वेद (पसीना) आदि। "
                   "‘सप्त’ को पिछले श्लोक की सात धातुओं से जोड़कर पढ़ा गया है, और अन्त की जोड़ी में दो पाठ संभव हैं। "
                   "दूसरी पंक्ति एक वाक्यांश है: जो रोग रस आदि में स्थित दोषों के होने पर उत्पन्न होते हैं। यह वाक्य पूरा अगले श्लोक में होता है, "
                   "इसलिए इस श्लोक के प्रश्न केवल इन्हीं दो पंक्तियों के शब्दों पर हैं।"),
    "hook": "दूष्य और मल: मूत्र, शकृत्, स्वेद; रोग वे जो रस आदि में टिके दोषों से उपजें।",
    "core": False,
    "questions": [
        mcq("pretest", 0,
            "Which wastes (malas) does line 1 of verse 40 name?",
            ("Urine, faeces and sweat", "मूत्र, शकृत् and स्वेद are named, with 'and the like'."),
            [("Blood, flesh and fat", "Those are dhātus of the previous verse."),
             ("Milk, bile and phlegm", "The verse names none of these."),
             ("Bone, marrow and semen", "Those are dhātus, not malas.")],
            "मूत्रशकृत्स्वेदादयः = urine, faeces, sweat and the like.",
            "Malas named: urine, faeces, sweat."),
        order(1, "Arrange the three malas in the order the verse names them.",
              ["मूत्र", "शकृत्", "स्वेद"],
              "The compound goes urine, faeces, sweat, then आदि ('and the like').",
              "मूत्र → शकृत् → स्वेद → आदि."),
        match(2, "Match each word of verse 40 to its meaning.",
              [["दूष्याः", "what can be vitiated"], ["मलाः", "wastes"],
               ["शकृत्", "faeces"], ["स्वेदः", "sweat"]],
              "Two category words and two named wastes.",
              "दूष्याः = dūṣyas; मलाः = wastes; शकृत् = faeces; स्वेद = sweat.", role="extend"),
        mcq("discriminate", 3, "Which is the right split of मूत्रशकृत्स्वेदादयोऽपि?",
            ("मूत्रशकृत्स्वेदादयः + अपि", "आदयः + अपि: visarga after अ before अ becomes ओ, and the lost अ is shown by ऽ."),
            [("मूत्रशकृत्स्वेदादयो + पि", "पि is not a word; the ऽ shows that अपि lost its अ."),
             ("मूत्रशकृत्स्वेदादय + अपि", "A bare अ + अ would give आ, not ओऽ."),
             ("मूत्रशकृत्स्वेदादयः + पि", "The word is अपि, not पि.")],
            "आदयोऽपि = आदयः + अपि. The ending -अः turns into -ओ before अ, and अपि's अ is marked by the avagraha ऽ.",
            "-अः + अ → -ोऽ."),
        mcq("apply", 4,
            "According to line 2, when do the diseases it speaks of arise?",
            ("When doṣas abide in rasa and the others", "रसादिस्थेषु दोषेषु: the doṣas are present in rasa and the rest."),
            [("When the malas are fully removed", "The verse says nothing about removing malas."),
             ("When no doṣa is present anywhere", "The clause needs doṣas: दोषेषु."),
             ("When the dhātus are named in order", "Naming has nothing to do with the arising of disease.")],
            "रसादिस्थेषु दोषेषु व्याधयः सम्भवन्ति ये: the diseases arise when doṣas abide in rasa and the others.",
            "Diseases arise in the case of doṣas abiding in rasa and the other dhātus."),
        mcq("transfer", 5,
            "A new line says धातुस्थेषु मलेषु. By the pattern of दोषेषु, what does मलेषु mean?",
            ("In the malas", "-एषु is the locative plural of a-stem masculine nouns, as in दोषेषु 'in the doṣas'."),
            [("By the malas", "By would need the ending -ऐः."),
             ("Of the malas", "Of would need -आनाम्."),
             ("The malas", "As subject it would be मलाः.")],
            "मलेषु is the locative plural of मल, 'in the malas', like दोषेषु.",
            "Masculine a-stem + -एषु = locative plural: in the ...",
            teaches="The ending -एषु means 'in the ...' for a plural a-stem noun, as in रसादिस्थेषु दोषेषु."),
    ],
}

# ---------------------------------------------------------------- unit 41
AUTHORED["41"] = {
    "title": "तज्जानित्युपचारेण",
    "question": "Which items does the list in line 2 of verse 41 name?",
    "rule": ("Line 2 begins a list: प्रीणन (gratifying), जीवन (sustaining life), लेप (coating), "
             "स्नेह (unctuousness), धारण (supporting) and पूरण (filling). The list's heading comes in the next verse."),
    "limits": ("Line 1 is damaged: the simile वृतदाहवत् is a doubtful reading (गृहदाहवत् is only a suggestion), "
               "so no question rests on it; this unit has low confidence. The list in line 2 is completed in the next unit."),
    "explain_hi": ("पहली पंक्ति में उपचार (लाक्षणिक प्रयोग) की बात है, पर उसकी उपमा का पाठ अनिश्चित है, इसलिए उस पर कोई प्रश्न नहीं बना। "
                   "दूसरी पंक्ति एक सूची शुरू करती है: प्रीणन, जीवन, लेप, स्नेह, धारण और पूरण। अन्तिम दो शब्द ‘धारणपूरणे’ एक द्वन्द्व समास में हैं, "
                   "इसलिए रूप द्विवचन का -ए है। सूची का नाम (कर्माणि धातूनाम्) अगले श्लोक की पहली पंक्ति में आता है।"),
    "hook": "प्रीणन, जीवन, लेप, स्नेह, धारण, पूरण: छह शब्दों की सूची, नाम अगले श्लोक में।",
    "core": False,
    "questions": [
        mcq("pretest", 0,
            "Which item opens the list in line 2 of verse 41?",
            ("प्रीणनम्", "The line begins with प्रीणनम्."),
            [("जीवनम्", "जीवनम् is the second item."),
             ("लेपः", "लेपः is the third item."),
             ("पूरणम्", "पूरण is the last item.")],
            "प्रीणनं जीवनं लेपः स्नेहो धारणपूरणे: the list opens with प्रीणन.",
            "List order: प्रीणन, जीवन, लेप, स्नेह, धारण, पूरण."),
        order(1, "Arrange the six items of the list in the verse's order.",
              ["प्रीणन", "जीवन", "लेप", "स्नेह", "धारण", "पूरण"],
              "The verse gives them in exactly this order.",
              "प्रीणन → जीवन → लेप → स्नेह → धारण → पूरण."),
        match(2, "Match each word of the list to its meaning.",
              [["प्रीणनम्", "gratifying, nourishing"], ["जीवनम्", "sustaining life"],
               ["लेपः", "coating"], ["स्नेहः", "unctuousness"]],
              "These four words are glossed in the card as shown.",
              "प्रीणन = gratifying; जीवन = sustaining life; लेप = coating; स्नेह = unctuousness.", role="extend"),
        mcq("discriminate", 3, "Why does धारणपूरणे end in -ए?",
            ("It is a neuter dual: the two items धारण and पूरण", "A dvandva of two neuter nouns takes the dual ending -ए."),
            [("It is a feminine singular naming one act", "The compound joins two separate items, so it is not singular."),
             ("It is a masculine plural for many supporters", "Plural masculine would end in -आः, and only two items are joined."),
             ("It is a call addressed to both items", "Nothing in the line addresses anyone.")],
            "धारणपूरणे = धारण + पूरण, a dvandva in the neuter nominative dual.",
            "Neuter dvandva of two items, nominative: dual in -ए."),
        multi("apply", 4, "Which of these does line 2 of verse 41 name?",
              [("प्रीणन", "Right: it opens the list."),
               ("लेप", "Right: the third item."),
               ("धारण", "Right: the fifth item."),
               ("शोधन", "This word is not in the line."),
               ("छेदन", "This word is not in the line.")],
              [0, 1, 2],
              "The line names six items; शोधन and छेदन are not among them.",
              "Named: प्रीणन, जीवन, लेप, स्नेह, धारण, पूरण."),
        mcq("transfer", 5,
            "A new line has the dvandva पठनलेखने, ending in -ए. What does the ending tell you?",
            ("Two neuter items: reading and writing", "Like धारणपूरणे, a neuter dvandva of two items has the dual -ए."),
            [("One masculine item, singular", "A masculine singular would end in -ः."),
             ("Many items, plural", "The plural of a neuter noun would end in -आनि."),
             ("A single item in the locative", "Two joined items are meant, not one in the locative.")],
            "पठन + लेखन are two neuter nouns, so पठनलेखने is the nominative dual.",
            "Two neuter nouns in a dvandva: nominative dual in -ए.",
            teaches="The same dual -ए of धारणपूरणे appears on any dvandva of two neuter a-stems."),
    ],
}

# ---------------------------------------------------------------- unit 42
AUTHORED["42"] = {
    "title": "गर्भोत्पादश्च कर्माणि",
    "question": "What does verse 42 say about the functions of the dhātus, and what do dhātus and foods always do?",
    "rule": ("The generation of the embryo ends the list of the previous verse; these are known in order as the functions of the dhātus. "
             "Dhātus and foods sustain the body at all times."),
    "limits": ("Line 1 finishes a list begun in verse 41, so its earlier items are not on this card. "
               "'Kramaśaḥ' (in order) is not spelled out: the verse does not say which function goes with which dhātu."),
    "explain_hi": ("पहली पंक्ति पिछले श्लोक की सूची पूरी करती है: अन्तिम शब्द ‘गर्भोत्पाद’ (गर्भ की उत्पत्ति) है, और ये सब धातुओं के ‘कर्म’ "
                   "(कार्य) क्रम से जाने जाते हैं। कौन-सा कार्य किस धातु का है, यह श्लोक नहीं बताता। दूसरी पंक्ति कहती है कि ये धातु और आहार "
                   "सदा शरीर को धारण करते हैं। ‘धात्वाहाराः’ में धातु + आहाराः का उ, व् बन जाता है।"),
    "hook": "सूची का अन्त गर्भ की उत्पत्ति; धातु और आहार सदा शरीर को धारण करते हैं।",
    "core": False,
    "questions": [
        mcq("pretest", 0,
            "What does the second line of verse 42 say the dhātus and foods do?",
            ("Sustain the body", "शरीरं धारयन्ति: they support the body."),
            [("Provoke the doṣas", "The line does not say this."),
             ("Pass out as wastes", "The line says nothing of passing out."),
             ("Wait for the season", "No season is mentioned here.")],
            "शरीरं धारयन्त्येते धात्वाहाराश्च सर्वदा: they always sustain the body.",
            "Dhātus and foods sustain the body at all times."),
        order(1, "Arrange the phrases of the second line in the verse's order.",
              ["शरीरम्", "धारयन्ति", "एते", "धात्वाहाराः", "सर्वदा"],
              "The line runs: the body they sustain, these dhātus and foods, always.",
              "शरीरं धारयन्ति एते धात्वाहाराश्च सर्वदा."),
        match(2, "Match each word of verse 42 to its meaning.",
              [["कर्माणि", "functions"], ["क्रमशः", "in order"],
               ["विदुः", "they know"], ["गर्भोत्पादः", "generation of the embryo"]],
              "These four words carry the first line.",
              "कर्माणि = functions; क्रमशः = in order; विदुः = they know; गर्भोत्पादः = generation of the embryo.", role="extend"),
        mcq("discriminate", 3, "Which is the right split of धात्वाहाराश्च?",
            ("धातु + आहाराः + च", "उ before the vowel आ turns into व्, giving धात्वा-."),
            [("धात्व + आहाराः + च", "धात्व is not a word here; the व् comes from the उ of धातु."),
             ("धातु + वाहाराः + च", "वाहाराः is not a word; the व् is born of the sandhi."),
             ("धातवः + आहाराः + च", "धातवः + आ would give धातव आहाराः, not धात्वाहाराः.")],
            "धात्वाहाराश्च = धातु + आहाराः + च: the dhātus and foods.",
            "उ + dissimilar vowel → व् + that vowel (धातु + आ → धात्वा)."),
        fill(4, "The dhātus and foods sustain the body ____ (the Devanagari word for 'at all times'; type it in Devanagari or in English letters, e.g. sarvada).",
             accepts("सर्वदा", "sarvadā"),
             "The verse ends with सर्वदा, 'always'.",
             "सर्वदा = at all times, in the last words of the second line.",
             "सर्वदा = always.", role="apply"),
        mcq("transfer", 5,
            "By the pattern धातु + आहाराः → धात्वाहाराः, how does गुरु + आज्ञा join?",
            ("गुर्वाज्ञा", "उ becomes व् before the dissimilar vowel आ, as in धात्वाहाराः."),
            [("गुराज्ञा", "The उ does not disappear; it turns into व्."),
             ("गुरूआज्ञा", "No vowel is joined on without change here."),
             ("गुरौज्ञा", "The आ of आज्ञा is not lost.")],
            "गुरु + आज्ञा → गुर्वाज्ञा, the same change of उ to व् as in धात्वाहाराः.",
            "उ + a different vowel → व् + that vowel.",
            teaches="Final उ before a different vowel becomes व्: धातु + आहाराः → धात्वाहाराः, गुरु + आज्ञा → गुर्वाज्ञा."),
    ],
}

# ---------------------------------------------------------------- unit 43
AUTHORED["43"] = {
    "title": "वृद्धिः समानैः सर्वेषाम्",
    "question": "What brings increase and what brings reversal, and which six rasas does verse 43 name?",
    "rule": ("Increase of all comes through what is alike (समानैः, by like things); reversal through opposites. "
             "The rasas (tastes) are sweet, sour, salty, bitter, pungent and astringent, in this order."),
    "limits": ("'Sarveṣām' (of all) is left general in the verse; the notes read doṣas and dhātus by context, but the verse does not name them. "
               "ऊषण is glossed 'pungent'."),
    "explain_hi": ("पहली पंक्ति एक सिद्धान्त देती है: सबकी वृद्धि समान से होती है और विपरीत से विपर्यय यानी उलटा। ‘सर्वेषाम्’ किनका है, यह श्लोक "
                   "नहीं कहता। दूसरी पंक्ति छह रस गिनाती है: स्वादु, अम्ल, लवण, तिक्त, ऊषण और कषाय। ‘विपरीतैर्विपर्ययः’ में विसर्ग "
                   "र् बन गया है, क्योंकि आगे घोष वर्ण व् है।"),
    "hook": "समान से वृद्धि, विपरीत से विपर्यय; छह रस: स्वादु, अम्ल, लवण, तिक्त, ऊषण, कषाय।",
    "core": True,
    "questions": [
        mcq("pretest", 0,
            "According to line 1 of verse 43, what brings increase?",
            ("What is alike (समान)", "वृद्धिः समानैः: increase comes through like things."),
            [("What is opposite (विपरीत)", "Opposites bring the reverse, विपर्यय."),
             ("What is sweet (स्वादु)", "Sweet is a rasa named in line 2, not the cause of increase."),
             ("What is excessive (अति)", "The verse does not link increase to excess.")],
            "वृद्धिः समानैः सर्वेषाम्: for all, increase comes through like things.",
            "Like → increase; opposite → reverse."),
        order(1, "Arrange the six rasas in the order the verse names them.",
              ["स्वादु", "अम्ल", "लवण", "तिक्त", "ऊषण", "कषाय"],
              "The compound lists them in this order.",
              "स्वादु → अम्ल → लवण → तिक्त → ऊषण → कषाय."),
        match(2, "Match each rasa word to its taste.",
              [["स्वादु", "sweet"], ["अम्ल", "sour"], ["ऊषण", "pungent"], ["कषाय", "astringent"]],
              "These are four of the six rasas of line 2.",
              "स्वादु = sweet; अम्ल = sour; ऊषण = pungent; कषाय = astringent.", role="extend"),
        mcq("discriminate", 3, "Which is the right split of विपरीतैर्विपर्ययः?",
            ("विपरीतैः + विपर्ययः", "-ऐः before a voiced sound (व) turns the visarga into र्."),
            [("विपरीतः + विपर्ययः", "The instrumental plural 'by opposites' ends in -ऐः, not -अः."),
             ("विपरीते + विपर्ययः", "The ending -ए would be a different case, and gives no र्."),
             ("विपरीतैः + पर्ययः", "The word is विपर्यय, whose व् is part of it.")],
            "विपरीतैर्विपर्ययः = विपरीतैः (by opposites) + विपर्ययः (reversal).",
            "Visarga after a vowel other than अ or आ, before a voiced sound → र्."),
        mcq("apply", 4, "Which pairing does line 1 of verse 43 state?",
            ("Like gives increase; opposites give reversal", "समानैः वृद्धिः, विपरीतैः विपर्ययः."),
            [("Like gives reversal; opposites give increase", "This swaps the two."),
             ("Like gives increase; opposites give increase", "Opposites give reversal, not increase."),
             ("Like gives reversal; opposites give reversal", "Like things give increase.")],
            "The verse says increase by like things and reversal by opposites.",
            "समान → वृद्धि; विपरीत → विपर्यय."),
        mcq("transfer", 5,
            "Following समानैः 'by like things', what does मधुरैः mean in a new line?",
            ("By sweet things", "-ऐः is the instrumental plural, as in समानैः and विपरीतैः."),
            [("Of sweet things", "Of would need -आणाम्, मधुराणाम्."),
             ("Sweet things (as subject)", "As subject it would be मधुराः."),
             ("In sweet things", "In would need -एषु, मधुरेषु.")],
            "मधुरैः is the instrumental plural: by (with) sweet things.",
            "a-stem + -ऐः = instrumental plural: by ...",
            teaches="The ending -ऐः, seen in समानैः and विपरीतैः, means 'by (through) ...' for plural a-stem words."),
    ],
}

# ---------------------------------------------------------------- unit 44
AUTHORED["44"] = {
    "title": "षड् द्रव्यमाश्रिताः",
    "question": "On what do the six rasas rest, and which of them act on wind (Māruta) and Kapha in verse 44?",
    "rule": ("The six rest in a substance (dravya) and bring strength in the order of precedence. "
             "The first (rasas) destroy Māruta; the three beginning with bitter destroy Kapha."),
    "limits": ("'Yathāpūrvam' is read 'in order of precedence'; the verse does not say 'more'. "
               "'Ādyāḥ' has no number; 'the first three' follows from 'trayaḥ' and the six rasas of the last verse. "
               "Pitta is not treated here but in the next verse."),
    "explain_hi": ("पहली पंक्ति: ये छह रस द्रव्य के आश्रित हैं और ‘यथापूर्वम्’ (पूर्व-पूर्व के क्रम से) बल देने वाले हैं। "
                   "दूसरी पंक्ति: उनमें आदि के रस मारुत (वायु) को नष्ट करते हैं, और तिक्त से आरंभ होने वाले तीन कफ को। "
                   "पित्त की बात अगले श्लोक में है। ‘षड्’ असल में षट् है, जो आगे द्रव्य के द् से पहले ड् बन गया है।"),
    "hook": "छह रस द्रव्य में टिके; आदि के वायु को, तिक्त से शुरू होने वाले तीन कफ को नष्ट करते हैं।",
    "core": False,
    "questions": [
        mcq("pretest", 0,
            "On what do the six rasas rest, according to line 1 of verse 44?",
            ("A substance (द्रव्य)", "षड् द्रव्यमाश्रिताः: the six depend on a dravya."),
            [("The body (शरीर)", "The body is not named in this verse."),
             ("A doṣa", "The doṣas are acted on, not the resting place."),
             ("The season", "No season is named.")],
            "द्रव्यमाश्रिताः = resting in, dependent on a substance.",
            "The six rasas rest in a dravya."),
        order(1, "Arrange the phrases of the second line in the verse's order.",
              ["तत्र आद्याः", "मारुतं घ्नन्ति", "त्रयः तिक्तादयः", "कफम्"],
              "The line names Māruta first, then Kapha.",
              "तत्राद्या मारुतं घ्नन्ति त्रयस्तिक्तादयः कफम्."),
        match(2, "Match each word of verse 44 to its meaning.",
              [["द्रव्यम्", "substance"], ["आश्रिताः", "resting in"],
               ["बलावहाः", "bringing strength"], ["घ्नन्ति", "they destroy"]],
              "These words carry the two lines.",
              "द्रव्यम् = substance; आश्रिताः = resting in; बलावहाः = bringing strength; घ्नन्ति = they destroy.", role="extend"),
        mcq("discriminate", 3, "Why does the verse print षड् and not षट् before द्रव्यम्?",
            ("A final voiceless ट् becomes voiced ड् before the voiced द", "षट् + द्रव्यम् → षड् द्रव्यम्."),
            [("ट् always becomes ड् at the end of a word", "At the end of a sentence it stays ट्; the change needs a voiced sound after it."),
             ("The number six is षड् in every position", "The word is षट्; षड् is a sandhi form."),
             ("It is a misprint for षष्", "There is no such form; the change is regular.")],
            "षड् is षट् changed before the voiced द of द्रव्यम्.",
            "Final voiceless stop + voiced sound → the voiced stop (ट् → ड्)."),
        mcq("apply", 4, "Which doṣa does line 2 say the three rasas beginning with bitter destroy?",
            ("Kapha (कफ)", "त्रयस्तिक्तादयः कफम्."),
            [("Māruta (wind)", "Māruta is destroyed by the first rasas, आद्याः."),
             ("Strength (बल)", "बल is what the six bring, not what is destroyed."),
             ("The substance (द्रव्य)", "The dravya is where the rasas rest, not what they destroy.")],
            "तिक्तादयः कफं घ्नन्ति: the three starting with bitter destroy Kapha.",
            "आद्याः → मारुत; त्रयस्तिक्तादयः → कफ."),
        mcq("transfer", 5,
            "By the pattern त्रयः + तिक्तादयः → त्रयस्तिक्तादयः, how does रसः + तिक्तः join?",
            ("रसस्तिक्तः", "-अः + त becomes -अस् त, as in त्रयस्तिक्तादयः."),
            [("रसोतिक्तः", "-ओ comes before a voiced sound, but त is voiceless."),
             ("रसश्तिक्तः", "श् comes before च or छ, not before त."),
             ("रसःतिक्तः", "The visarga does change before त; it is not left as it is.")],
            "रसः + तिक्तः → रसस्तिक्तः: the visarga becomes स् before the voiceless त.",
            "Visarga + voiceless त → स्.",
            teaches="A visarga before a voiceless त becomes स्, as in त्रयः + तिक्त- → त्रयस्तिक्त-."),
    ],
}

# ---------------------------------------------------------------- unit 45
AUTHORED["45"] = {
    "title": "कषायतिक्तमधुराः पित्तम्",
    "question": "Which rasas act on Pitta in verse 45, and how is a substance divided?",
    "rule": ("Astringent, bitter and sweet destroy Pitta (the verb carries over), but the others make Pitta. "
             "A substance is threefold: pacifying, provoking, and good for the healthy."),
    "limits": ("The verb 'destroy' of the first clause is carried from verse 44. 'Kurvate' is literally 'make', read as 'produce, provoke'. "
               "The verse speaks of the rasas only; it says nothing more about the 'others' than that they make Pitta."),
    "explain_hi": ("पहली पंक्ति में कषाय, तिक्त और मधुर रस पित्त को नष्ट करते हैं (क्रिया ‘घ्नन्ति’ पिछले श्लोक से चली आती है), "
                   "परंतु ‘अन्ये’ यानी दूसरे रस पित्त को उत्पन्न करते हैं। दूसरी पंक्ति द्रव्य को तीन प्रकार का बताती है: शमन (शान्त करने वाला), "
                   "कोपन (कुपित करने वाला) और स्वस्थ के लिए हितकर। ‘स्वस्थहितम्’ का अर्थ है ‘स्वस्थ के लिए हित’।"),
    "hook": "कषाय, तिक्त, मधुर पित्त-नाशक; द्रव्य तीन तरह का: शमन, कोपन, स्वस्थहित।",
    "core": True,
    "questions": [
        mcq("pretest", 0,
            "How does line 2 of verse 45 divide a substance (द्रव्य)?",
            ("Pacifying, provoking, good for the healthy", "शमनं कोपनं स्वस्थहितं द्रव्यमिति त्रिधा."),
            [("Sweet, sour, salty", "Those are rasas, not the three kinds of dravya."),
             ("Hot, cold, neutral", "Hot and cold belong to the next verse's vīrya."),
             ("Light, heavy, soft", "The verse does not divide dravya by these.")],
            "The verse says a substance is threefold: शमन, कोपन and स्वस्थहित.",
            "द्रव्य is threefold: शमन, कोपन, स्वस्थहित."),
        order(1, "Arrange the three kinds of substance in the verse's order.",
              ["शमन", "कोपन", "स्वस्थहित"],
              "The verse gives pacifying, provoking, then good for the healthy.",
              "शमनं कोपनं स्वस्थहितं."),
        match(2, "Match each word of verse 45 to its meaning.",
              [["शमनम्", "pacifying"], ["कोपनम्", "provoking"],
               ["स्वस्थहितम्", "good for the healthy"], ["कुर्वते", "they make"]],
              "These words carry the second line and the verb of the first.",
              "शमनम् = pacifying; कोपनम् = provoking; स्वस्थहितम् = good for the healthy; कुर्वते = they make.", role="extend"),
        mcq("discriminate", 3, "Which is the right split of द्रव्यमिति?",
            ("द्रव्यम् + इति", "A final म् stays before a vowel and joins it: द्रव्य-म्-इति."),
            [("द्रव्य + मिति", "मिति is not a word; the म् belongs to द्रव्यम्."),
             ("द्रव्यः + इति", "The word द्रव्यम् is neuter and ends in म्, not visarga."),
             ("द्रव्ये + इति", "The ending is -म्, not -ए; the join would not give द्रव्यमिति.")],
            "द्रव्यमिति = द्रव्यम् + इति ('a substance, thus').",
            "Final म् + vowel: the म् is written with the vowel."),
        multi("apply", 4, "Line 1 of verse 45 names tastes that destroy Pitta. Which are they?",
              [("कषाय (astringent)", "Right: named first."),
               ("तिक्त (bitter)", "Right: named second."),
               ("मधुर (sweet)", "Right: named third."),
               ("अम्ल (sour)", "Not named in this line; it is among the 'others'."),
               ("लवण (salty)", "Not named in this line; it is among the 'others'.")],
              [0, 1, 2],
              "The first line names astringent, bitter and sweet; the others make Pitta.",
              "कषाय-तिक्त-मधुराः destroy Pitta; अन्ये make it."),
        mcq("transfer", 5,
            "By the pattern स्वस्थहितम् 'good for the healthy', what does रोगिहितम् mean?",
            ("Good for the sick", "The first member names for whom it is good; रोगिन् means 'sick'."),
            [("Made by the sick", "The compound says 'good for', not 'made by'."),
             ("Harming the sick", "हित means good, the opposite of harm."),
             ("The sick one who is good", "The compound is not a description of the sick person.")],
            "X-हितम् means good for X, so रोगिहितम् is good for the sick.",
            "X-हित = good for X.",
            teaches="In स्वस्थहितम् the first member names the one for whom it is good; any X-हितम् is read the same way."),
    ],
}

# ---------------------------------------------------------------- unit 46
AUTHORED["46"] = {
    "title": "उष्णशीतगुणोत्कर्षात्",
    "question": "How many kinds of vīrya and vipāka does verse 46 give, and on what does vīrya depend?",
    "rule": ("Among these, vīrya (potency) is held to be twofold from the predominance of the hot or cold quality. "
             "The vipāka (ripening, final transformation) of a substance is threefold."),
    "limits": ("The third kind of vipāka is printed स्वाद्वम्लकदुकात्मकः; 'kaduka' is probably a slip for 'kaṭuka', so this card builds no question on the three names. "
               "The verse does not say which substance has which vīrya or vipāka."),
    "explain_hi": ("पहली पंक्ति: उष्ण और शीत गुण की प्रधानता (उत्कर्ष) से वीर्य दो प्रकार का माना गया है। "
                   "दूसरी पंक्ति: द्रव्य का विपाक तीन प्रकार का है। तीन नामों में अन्तिम शब्द ‘कदुक’ छपा है, जो शायद ‘कटुक’ की भूल है, "
                   "इसलिए यहाँ केवल गिनती और आधार पर प्रश्न हैं। ‘द्विधा’, ‘त्रिधा’ में -धा का अर्थ ‘प्रकार का’ है।"),
    "hook": "वीर्य दो प्रकार का (उष्ण/शीत की प्रधानता से); विपाक तीन प्रकार का।",
    "core": False,
    "questions": [
        mcq("pretest", 0,
            "In verse 46, from what does the twofold vīrya come?",
            ("The predominance of the hot or cold quality", "उष्णशीतगुणोत्कर्षात्: from the excess of the hot or cold quality."),
            [("The sweet or sour taste of a substance", "Taste is not given as the basis in this verse."),
             ("The first or last ripening", "Ripening belongs to vipāka, not to the basis of vīrya."),
             ("The strong or weak digestion", "Digestion is not mentioned.")],
            "उष्ण-शीत-गुण-उत्कर्षात् = from the predominance of the hot or cold quality.",
            "वीर्य: twofold, by the predominance of hot or cold."),
        order(1, "Arrange the phrases of the first line in the verse's order.",
              ["उष्णशीतगुणोत्कर्षात्", "तत्र", "वीर्यम्", "द्विधा", "स्मृतम्"],
              "The line gives the reason first, then 'among these', vīrya, twofold, 'held'.",
              "उष्णशीतगुणोत्कर्षात्तत्र वीर्यं द्विधा स्मृतम्."),
        match(2, "Match each word of verse 46 to its meaning.",
              [["वीर्यम्", "potency"], ["विपाकः", "ripening, final transformation"],
               ["द्विधा", "twofold"], ["त्रिधा", "threefold"]],
              "Two technical terms and two number words.",
              "वीर्यम् = potency; विपाकः = ripening; द्विधा = twofold; त्रिधा = threefold.", role="extend"),
        mcq("discriminate", 3, "Which is the right split of गुणोत्कर्षात्?",
            ("गुण + उत्कर्षात्", "अ + उ gives ओ, so गुण + उत्कर्षात् is written गुणोत्कर्षात्."),
            [("गुणा + उत्कर्षात्", "आ + उ would give आ-उ, not ओ."),
             ("गुण + त्कर्षात्", "The word is उत्कर्षात्, with its उ."),
             ("गुणो + उत्कर्षात्", "गुणो is not a word; the ओ is produced by the join.")],
            "गुणोत्कर्षात् = गुण + उत्कर्षात् ('from the excess of the quality').",
            "अ + उ → ओ."),
        mcq("apply", 4, "Which pairing of counts does verse 46 give?",
            ("Vīrya twofold, vipāka threefold", "वीर्यं द्विधा, विपाकः त्रिधा."),
            [("Vīrya threefold, vipāka twofold", "This swaps the two."),
             ("Vīrya twofold, vipāka twofold", "Vipāka is threefold (त्रिधा)."),
             ("Vīrya threefold, vipāka threefold", "Vīrya is twofold (द्विधा).")],
            "The first line says vīrya is द्विधा, the second says vipāka is त्रिधा.",
            "वीर्य: 2 kinds; विपाक: 3 kinds."),
        mcq("transfer", 5,
            "By the pattern द्विधा and त्रिधा, what does a new word चतुर्धा mean?",
            ("Fourfold", "-धा makes 'in ... ways'; चतुर् is four."),
            [("Fourth", "An ordinal would be चतुर्थ."),
             ("Four times", "'Times' would be चतुः, as in the number adverbs."),
             ("Of four", "'Of' would be a genitive ending, not -धा.")],
            "द्वि + धा = twofold, त्रि + धा = threefold, so चतुर् + धा = fourfold.",
            "number + धा = in so many kinds.",
            teaches="The suffix -धा after a number gives 'so many-fold': द्विधा, त्रिधा, and the same pattern in षोढा, दशधा of verse 39."),
    ],
}

# ---------------------------------------------------------------- unit 47
AUTHORED["47"] = {
    "title": "गुरुमन्दहिमस्निग्ध",
    "question": "Which qualities (guṇas) does verse 47 name, and how does it reach twenty?",
    "rule": ("Heavy, slow, cold, unctuous, smooth, dense, soft and stable; with subtle (सूक्ष्म) and clear (विशद) added, "
             "and with their opposites, the qualities are twenty."),
    "limits": ("The verse names only these ten qualities; it does not name their opposites. "
               "The ten is the sum of the eight listed and the two added, as the notes count."),
    "explain_hi": ("पहली पंक्ति आठ गुण गिनाती है: गुरु, मन्द, हिम, स्निग्ध, श्लक्ष्ण, सान्द्र, मृदु, स्थिर। दूसरी पंक्ति कहती है कि सूक्ष्म और विशद "
                   "को जोड़कर तथा ‘सविपर्यय’ यानी अपने विपरीतों के साथ ये बीस गुण हैं। विपरीतों के नाम श्लोक नहीं देता। "
                   "‘ससूक्ष्मविशदा’ के अन्त में विसर्ग नहीं लिखा, पर यह भूल नहीं है: आः के बाद घोष वर्ण व् आने पर विसर्ग लुप्त होता है।"),
    "hook": "आठ गुण + सूक्ष्म-विशद, सब अपने विपरीतों सहित = बीस गुण।",
    "core": True,
    "questions": [
        mcq("pretest", 0,
            "With the two added and the opposites, how many qualities does verse 47 say there are?",
            ("Twenty (विंशति)", "विंशतिः सविपर्ययाः: twenty with their opposites."),
            [("Eight", "Eight are the ones listed in line 1, before the additions."),
             ("Ten", "Ten leaves out the opposites; the verse says twenty with them."),
             ("Sixteen", "The verse does not give sixteen.")],
            "The verse ends with विंशतिः सविपर्ययाः: twenty, with their opposites.",
            "Twenty qualities, with their opposites."),
        order(1, "Arrange the first six qualities of line 1 in the verse's order.",
              ["गुरु", "मन्द", "हिम", "स्निग्ध", "श्लक्ष्ण", "सान्द्र"],
              "The line begins with these six; मृदु and स्थिर follow.",
              "गुरु → मन्द → हिम → स्निग्ध → श्लक्ष्ण → सान्द्र → मृदु → स्थिर."),
        match(2, "Match each quality word to its meaning.",
              [["गुरु", "heavy"], ["मन्द", "slow"], ["हिम", "cold"], ["सान्द्र", "dense"]],
              "Four of the eight listed qualities.",
              "गुरु = heavy; मन्द = slow; हिम = cold; सान्द्र = dense.", role="extend"),
        mcq("discriminate", 3,
            "ससूक्ष्मविशदा stands for ससूक्ष्मविशदाः. Why is the visarga not written?",
            ("After आः, before a voiced sound like व, the visarga drops", "The next word विंशतिः starts with the voiced व."),
            [("The visarga is always dropped at the end of a verse line", "It is dropped only before a voiced sound, not by line position."),
             ("It is a misprint that should be corrected", "It is regular sandhi, not a misprint."),
             ("The word is a singular that never has a visarga", "It is a plural, in -आः.")],
            "ससूक्ष्मविशदाः + विंशतिः → ससूक्ष्मविशदा विंशतिः.",
            "-आः + voiced sound → -आ."),
        mcq("apply", 4,
            "The verse names ten qualities. Why does it reach twenty?",
            ("Each is taken with its opposite (सविपर्ययाः)", "सविपर्ययाः means 'with their opposites'."),
            [("Each is repeated one more time", "The word says 'with opposites', not 'repeated'."),
             ("Ten more are listed in the next line", "No further list of ten follows in this verse."),
             ("Two are added to each quality", "The two added are सूक्ष्म and विशद, once only.")],
            "सविपर्ययाः = sa + viparyaya: together with their opposites.",
            "10 named + their opposites = 20."),
        mcq("transfer", 5,
            "By the pattern स + विपर्ययाः 'with their opposites', what does सपुष्पाः mean in a new line?",
            ("With flowers", "स- before a noun gives 'with', so स + पुष्प = with flowers."),
            [("Without flowers", "'Without' would be अ- or निः-."),
             ("Having many flowers", "स- only says 'with'; it does not say 'many'."),
             ("Of the flowers", "'Of' is a case ending; स- is a prefix.")],
            "स + पुष्प-आः = सपुष्पाः, 'with flowers', as सविपर्ययाः is 'with opposites'.",
            "स- + noun = together with that noun.",
            teaches="The prefix स- means 'with', as in सविपर्ययाः; the same works for any noun."),
    ],
}

# ---------------------------------------------------------------- unit 48
AUTHORED["48"] = {
    "title": "इन्द्रियार्था व्यवायी च",
    "question": "Which other qualities does verse 48 name, and what does the vyavāyin quality do?",
    "rule": ("The objects of the senses, vyavāyin and vikāsin (printed विकाषी) are the other qualities. "
             "The vyavāyin quality, having pervaded the whole body, is fit for pāka (ripening, cooking)."),
    "limits": ("The printed विकाषी may be विकासी or विकाशी; the spelling is open, so no question rests on it. "
               "'Pākāya kalpate' is literally 'is fit for ripening' and is left plain; vyavāyin and vikāsin are kept untranslated."),
    "explain_hi": ("पहली पंक्ति: इन्द्रियों के विषय (इन्द्रियार्थाः), व्यवायी और विकासी (छपा रूप ‘विकाषी’, वर्तनी अनिश्चित) ‘अपरे गुणाः’ यानी अन्य गुण हैं। "
                   "दूसरी पंक्ति: व्यवायी पूरे शरीर में फैलकर (व्याप्य) पाक के योग्य होता है। ‘व्याप्य’ ल्यप्-रूप है, यानी उपसर्ग वाली क्रिया "
                   "का ‘करके’ अर्थ वाला रूप। ‘चापरे’ = च + अपरे।"),
    "hook": "अन्य गुण: इन्द्रियार्थ, व्यवायी, विकासी; व्यवायी पूरे देह में फैलकर पाक के योग्य।",
    "core": False,
    "questions": [
        mcq("pretest", 0,
            "In line 2 of verse 48, what does the vyavāyin quality do?",
            ("Pervades the whole body and is fit for pāka", "व्यवायी देहमखिलं व्याप्य पाकाय कल्पते."),
            [("Stays in the head alone and is fit for pāka", "The verse says the whole body, अखिलं देहम्."),
             ("Pervades the whole body and is unfit for pāka", "It is fit for pāka, कल्पते."),
             ("Pervades the senses and is fit for pāka", "What it pervades is the body (देहम्).")],
            "It pervades the whole body and is fit for pāka (ripening, cooking).",
            "व्यवायी: pervades the whole body; fit for pāka."),
        order(1, "Arrange the phrases of line 2 in the verse's order.",
              ["व्यवायी", "देहमखिलम्", "व्याप्य", "पाकाय कल्पते"],
              "The line runs: vyavāyin, the whole body, having pervaded, fit for pāka.",
              "व्यवायी देहमखिलं व्याप्य पाकाय कल्पते."),
        match(2, "Match each word of verse 48 to its meaning.",
              [["इन्द्रियार्थाः", "objects of the senses"], ["अखिलम्", "whole"],
               ["व्याप्य", "having pervaded"], ["पाकाय", "for pāka (ripening)"]],
              "These words carry both lines.",
              "इन्द्रियार्थाः = objects of the senses; अखिलम् = whole; व्याप्य = having pervaded; पाकाय = for ripening.", role="extend"),
        mcq("discriminate", 3, "Which is the right split of चापरे?",
            ("च + अपरे", "अ + अ join into आ: च + अपरे → चापरे."),
            [("च + आपरे", "आपरे is not a word here."),
             ("चा + परे", "परे would mean 'other' only if the अ were not part of अपरे."),
             ("चो + अपरे", "चो is not a word; the join of अ and अ gives आ.")],
            "चापरे = च ('and') + अपरे ('other').",
            "अ + अ → आ."),
        multi("apply", 4, "Which of these does line 1 of verse 48 name as other qualities?",
              [("इन्द्रियार्थाः", "Right: objects of the senses."),
               ("व्यवायी", "Right: named in line 1."),
               ("विकाषी (as printed)", "Right: the third, vikāsin."),
               ("सत्त्व", "Not named in this line."),
               ("रजस्", "Not named in this line.")],
              [0, 1, 2],
              "Line 1 names three: the objects of the senses, vyavāyin and vikāsin.",
              "Other qualities: इन्द्रियार्थाः, व्यवायी, विकासी."),
        mcq("transfer", 5,
            "Like व्याप्य 'having pervaded', what does प्रविश्य, from a verb with a prefix, mean?",
            ("Having entered", "A prefixed verb takes -य for 'having done'; प्र + विश् means enter."),
            [("To enter", "'To enter' would be प्रवेष्टुम्."),
             ("Having been entered", "-य does not make a passive 'been'."),
             ("Let him enter", "A command would be प्रविशतु.")],
            "व्याप्य and प्रविश्य are both absolutives in -य of prefixed verbs.",
            "Prefix + root + -य = 'having done'.",
            teaches="After a prefix, 'having done' is -य, not -त्वा: व्याप्य 'having pervaded', प्रविश्य 'having entered'."),
    ],
}

# ---------------------------------------------------------------- unit 49
AUTHORED["49"] = {
    "title": "विकाषी विकषन्नेव",
    "question": "What does the vikāsin quality do to the joints in line 1 of verse 49?",
    "rule": ("Line 1: the vikāsin quality (printed विकाषी), merely by expanding, loosens the bonds of the joints. "
             "Line 2 is damaged and is not used on this card."),
    "limits": ("Low confidence. Line 2 is damaged (सस्तीक्ष्णप्रकर्षौ, कैश्चित्सौ unresolved); the card gives only the plain sense 'some posit sharpness and excess' "
               "and builds no question on it. The spelling विकाषी / विकषन् may stand for विकासी / विकसन् or विकाशी / विकशन्; "
               "the sense 'expanding' stays the same."),
    "explain_hi": ("पहली पंक्ति स्पष्ट है: विकासी (छपा ‘विकाषी’) फैलते हुए ही संधियों के बन्धनों को ढीला कर देता है। ‘विकषन्नेव’ में न् दोहरा "
                   "हुआ है: विकषन् + एव। दूसरी पंक्ति में पाठ बिगड़ा है (‘सस्’, ‘सौ’ का अर्थ स्पष्ट नहीं); सादा अर्थ यही लगता है कि कुछ लोग तीक्ष्ण और प्रकर्ष की "
                   "कल्पना करते हैं, पर उस पर भरोसा न करें, इसलिए प्रश्न केवल पहली पंक्ति पर हैं।"),
    "hook": "विकासी फैलते हुए ही संधि-बन्धनों को ढीला करता है; दूसरी पंक्ति बिगड़ी है।",
    "core": False,
    "questions": [
        mcq("pretest", 0,
            "What does the quality in line 1 of verse 49 loosen?",
            ("The bonds of the joints (संधिबन्धान्)", "संधिबन्धान् विमुञ्चति: it looses the bonds of the joints."),
            [("The bonds of the doṣas", "The doṣas are not mentioned in line 1."),
             ("The skin of the body", "The skin is not mentioned."),
             ("The bones of the head", "Only the bonds of the joints are named.")],
            "विमुञ्चति = looses; संधिबन्धान् = the bonds of the joints.",
            "The quality loosens the bonds of the joints."),
        order(1, "Arrange the phrases of line 1 in the verse's order.",
              ["विकाषी", "विकषन्नेव", "संधिबन्धान्", "विमुञ्चति"],
              "The line names the quality, then 'merely by expanding', the bonds, the verb.",
              "विकाषी विकषन्नेव संधिबन्धान्विमुञ्चति."),
        match(2, "Match each word of line 1 to its meaning.",
              [["संधि", "joint"], ["बन्धान्", "bonds"], ["विमुञ्चति", "he looses"], ["एव", "merely, just"]],
              "These words are the safe, clear ones of the line.",
              "संधि = joint; बन्ध = bond; विमुञ्चति = looses; एव = merely.", role="extend"),
        mcq("discriminate", 3, "Which is the right split of विकषन्नेव?",
            ("विकषन् + एव", "A final न् after a short vowel is doubled before a vowel: विकषन् + एव → विकषन्नेव."),
            [("विकषन + नेव", "नेव is not a word."),
             ("विकषन्न + एव", "विकषन्न is not a form; the second न् comes from the join."),
             ("विकष + न्नेव", "न्नेव is not a word.")],
            "विकषन्नेव = विकषन् (expanding) + एव (merely).",
            "Final न् after a short vowel + vowel → न्न्."),
        mcq("apply", 4, "According to line 1, how does this quality loosen the bonds?",
            ("By expanding alone (विकषन्नेव)", "एव stresses that expanding alone is enough."),
            [("By pressing on them", "Nothing in the line speaks of pressing."),
             ("By drying them out", "Nothing in the line speaks of drying."),
             ("By cooling them", "Nothing in the line speaks of cooling.")],
            "विकषन्नेव = just by expanding; the bonds of the joints are loosened.",
            "Expanding is the means named."),
        mcq("transfer", 5,
            "By the pattern विकषन् + एव → विकषन्नेव, how does पठन् + एव join?",
            ("पठन्नेव", "Final न् after a short vowel doubles before a vowel."),
            [("पठनेव", "Without doubling, the join would be wrong."),
             ("पठेव", "The न् is not lost."),
             ("पठण्णेव", "ण् is not the nasal of this word.")],
            "पठन् + एव → पठन्नेव, the same doubling as in विकषन्नेव.",
            "Short vowel + final न् + vowel → न्न्.",
            teaches="A final न् after a short vowel is doubled before a vowel: विकषन्नेव, पठन्नेव."),
    ],
}

# ---------------------------------------------------------------- unit 50
AUTHORED["50"] = {
    "title": "सत्त्वं रजस्तमश्चेति",
    "question": "Which three are called the great qualities (mahāguṇa) in verse 50, and what three faults of conjunction does line 2 name?",
    "rule": ("Sattva, rajas and tamas are called the three great qualities. "
             "The conjunction of time, objects and actions may be deficient, wrong or excessive; the sentence continues in the next verse."),
    "limits": ("The second sentence has no verb in this unit; it is completed in the next verse, so the card does not say what the conjunction leads to. "
               "The printed सत्वं is a variant spelling of सत्त्वम्, not an error."),
    "explain_hi": ("पहली पंक्ति में तीन ‘महागुण’ कहे गए हैं: सत्त्व, रज और तम। दूसरी पंक्ति एक नया वाक्य शुरू करती है: काल, अर्थ और कर्मों का "
                   "योग तीन तरह का हो सकता है: हीन, मिथ्या या अतिमात्र। इसकी क्रिया इस श्लोक में नहीं है, वह अगले श्लोक में पूरी होती है। "
                   "छपा ‘सत्वं’ सत्त्वम् का दूसरा रूप है। ‘रजस्तमश्चेति’ में विसर्ग स्, श् बन गए हैं।"),
    "hook": "तीन महागुण: सत्त्व, रज, तम; काल-अर्थ-कर्म का योग: हीन, मिथ्या, अतिमात्र।",
    "core": False,
    "questions": [
        mcq("pretest", 0,
            "Which set does line 1 of verse 50 call the three great qualities?",
            ("Sattva, rajas and tamas", "सत्त्वं रजस्तमश्चेति त्रयः प्रोक्ता महागुणाः."),
            [("Vāta, pitta and kapha", "These three are not named in this verse."),
             ("Heavy, slow and cold", "These are qualities of verse 47, not the mahāguṇas."),
             ("Sweet, sour and salty", "These are rasas of verse 43.")],
            "The three great qualities are sattva, rajas and tamas.",
            "महागुण: सत्त्व, रजस्, तमस्."),
        order(1, "Arrange the three great qualities in the verse's order.",
              ["सत्त्व", "रजस्", "तमस्"],
              "The verse gives sattva, then rajas, then tamas.",
              "सत्त्वं रजस्तमः."),
        match(2, "Match each word of verse 50 to its meaning.",
              [["सत्त्वम्", "clarity"], ["रजस्", "activity"], ["तमस्", "inertia"], ["महागुणाः", "great qualities"]],
              "These are the glosses of the card for the four words of line 1.",
              "सत्त्व = clarity; रजस् = activity; तमस् = inertia; महागुण = great quality.", role="extend"),
        mcq("discriminate", 3, "Which is the right split of रजस्तमश्चेति?",
            ("रजः + तमः + च + इति", "The visarga becomes स् before त, श् before च, and च + इति gives चेति."),
            [("रज + स्तमः + च + इति", "स्तमः is not a word; the स् is the changed visarga of रजः."),
             ("रजः + तमः + चे + इति", "चे is not a word; the ए comes from the join of अ and इ."),
             ("रजः + तमः + च + एति", "The word is इति ('thus'); एति means 'goes'.")],
            "रजस्तमश्चेति = रजः + तमः + च + इति.",
            "Visarga + त → स्; visarga + च → श्; अ + इ → ए."),
        multi("apply", 4, "Which faults of the conjunction does line 2 of verse 50 name?",
              [("हीन (deficient)", "Right: the first."),
               ("मिथ्या (wrong)", "Right: the second."),
               ("अतिमात्र (excessive)", "Right: the third."),
               ("सम्यक् (right)", "Not named in this line."),
               ("मध्य (middling)", "Not named in this line.")],
              [0, 1, 2],
              "The compound हीनमिथ्यातिमात्रकः names deficient, wrong and excessive.",
              "योग: हीन, मिथ्या, अतिमात्र."),
        mcq("transfer", 5,
            "By the pattern कालार्थकर्मणाम् 'of time, objects and actions', what does गुणकर्मणाम् mean in a new line?",
            ("Of qualities and actions", "The ending -आम् at the end of the dvandva covers both members."),
            [("By qualities and actions", "By would need -ऐः or -भिः."),
             ("Qualities and actions (as subject)", "As subject it would end in -आनि or -आणि."),
             ("In qualities and actions", "In would need -सु.")],
            "गुण + कर्मन् in a dvandva: the genitive plural -आम् at the end belongs to both, 'of qualities and actions'.",
            "Dvandva + -आम् = of all the members.",
            teaches="In a dvandva, the case ending is written once, at the end, and covers every member: कालार्थकर्मणाम् = of time, objects and actions."),
    ],
}

NOTES_HI = {
    "39": "‘चोक्तावुत्कर्षादिविकल्पनात्’ में दो सन्धियाँ जाँची गईं: च + उक्तौ → चोक्तौ, उक्तौ + उत्कर्ष → उक्ताव्-उत्कर्ष। ‘तौ’ पिछले श्लोक (३८) के दो पदार्थों के लिए है, "
          "जिन्हें स्रोत की टिप्पणी में संसर्ग और सन्निपात पढ़ा गया है; यह इसी श्लोक से सिद्ध नहीं होता। ‘असृक्’ का अर्थ रक्त है। सात की संख्या अगले श्लोक में है। पाठ-चिह्न नहीं हैं।",
    "40": "विश्वास: मध्यम। ‘सप्त’ को पिछले श्लोक की सात धातुओं से जोड़ा गया है, और अन्त की जोड़ी में दो अर्थ सम्भव हैं (मल भी दूष्य हैं, या मल अतिरिक्त हैं); "
          "कार्ड ने इस चुनाव पर प्रश्न नहीं बनाया। ‘मूत्रशकृत्स्वेदादयोऽपि’ = आदयः + अपि। पंक्ति २ का सम्बन्ध-सूचक ‘ये’ अगले श्लोक की पंक्ति १ (‘तान् आहुः’) में पूरा होता है; "
          "असल श्लोक की सीमा यहाँ की जोड़ी से अलग दिखती है।",
    "41": "विश्वास: निम्न। पंक्ति १ में ‘वृतदाहवत्’ का पाठ संदिग्ध है; ‘गृहदाहवत्’ केवल सुझाव है (टिप्पणी: सम्भव)। पुस्तक का हिन्दी ‘जलते लोहे का गोला’ और अंग्रेज़ी ‘ring of fire’ "
          "संस्कृत से सिद्ध नहीं होते। इसलिए पंक्ति १ पर कोई प्रश्न नहीं है। पंक्ति २ की सूची अगले श्लोक की पंक्ति १ (‘कर्माणि धातूनाम्’) में पूरी होती है। "
          "‘धारणपूरणे’ नपुंसक द्विवचन द्वन्द्व है।",
    "42": "विश्वास: मध्यम। पंक्ति १ पिछले श्लोक की सूची पूरी करती है; सूची की वस्तुएँ ‘कर्माणि’ की समानाधिकरण हैं। ‘क्रमशः’ का अर्थ क्रम से है, पर यह नहीं बताया गया कि कौन-सा कार्य किस धातु का है। "
          "‘धात्वाहाराश्च’ = धातु + आहाराः + च (उ → व्)।",
    "43": "‘विपरीतैर्विपर्ययः’ = विपरीतैः + विपर्ययः (विसर्ग → र् घोष व् से पहले)। ‘सर्वेषाम्’ अनिर्दिष्ट रखा गया है। ‘ऊषण’ को यहाँ ‘तीखा’ (pungent) पढ़ा गया है (आमतौर पर जिसे कटु रस कहते हैं)। पाठ-चिह्न नहीं।",
    "44": "विश्वास: मध्यम। छपा ‘षड्’ असल में ‘षट्’ है (द् से पहले ट् → ड्)। ‘यथापूर्वम्’ का अर्थ ‘क्रम-श्रेष्ठता से’ पढ़ा गया है; ‘अधिक’ संस्कृत में नहीं है। "
          "‘आद्याः’ में संख्या नहीं है; ‘आदि के तीन’ पिछले श्लोक के छह रस और ‘त्रयः’ से निकलता है। ‘घ्नन्ति’ का शाब्दिक अर्थ ‘मारते हैं’ है। "
          "‘द्रव्यमाश्रितास्तेच’ में ‘ते च’ का विराम छूटा है (ते च)।",
    "45": "विश्वास: मध्यम। पंक्ति १ की क्रिया ‘घ्नन्ति’ पिछले श्लोक की पंक्ति २ से ली गई है। ‘कुर्वते’ का शाब्दिक अर्थ ‘करते हैं’ है, यहाँ ‘उत्पन्न/कुपित करते हैं’ पढ़ा गया है। "
          "‘पित्तमन्ये’ = पित्तम् + अन्ये; ‘द्रव्यमिति’ = द्रव्यम् + इति। श्लोक केवल रसों की बात करता है।",
    "46": "विश्वास: मध्यम। पाठ-चिह्न: ‘स्वाद्वम्लकदुकात्मकः’ में ‘कदुक’ शब्द नहीं है; ‘कटुक’ सम्भावित है (देवनागरी में भी ट की जगह द दिखता है)। इसलिए तीन विपाक-नामों पर प्रश्न नहीं बना। "
          "‘गुणोत्कर्षात्’ = गुण + उत्कर्षात् (अ + उ → ओ)। वीर्य और विपाक संक्षिप्त अर्थ के साथ रखे गए हैं।",
    "47": "‘ससूक्ष्मविशदा’ ‘ससूक्ष्मविशदाः’ है; विसर्ग लिपि में लुप्त है (आः + व्, स्वीकृत वर्तनी, भूल नहीं)। गिनती: आठ सूचीबद्ध गुण + सूक्ष्म + विशद = दस; विपरीतों के साथ बीस। "
          "‘हिम’ (बर्फ़, ठंडा) को ‘शीत’ रूप में रखा गया है। गुणों के विपरीतों के नाम श्लोक में नहीं हैं।",
    "48": "विश्वास: मध्यम। पाठ-चिह्न: ‘विकाषी’ में ष् छपा है; ज्ञात गुण ‘विकासी’ (वि-√कस्) है, पर इस स्कैन में श् अक्सर ष् छपा मिलता है, इसलिए ‘विकाशी’ भी सम्भव है। "
          "यही वर्तनी श्लोक ४९ में लौटती है। ‘पाकाय कल्पते’ का शाब्दिक अर्थ ‘पाक के योग्य है’ है। ‘इन्द्रियार्था’ = इन्द्रियार्थाः (घोष व् से पहले विसर्ग लुप्त)। ‘चापरे’ = च + अपरे।",
    "49": "विश्वास: निम्न। पंक्ति १ की वर्तनी ‘विकाषी’ और ‘विकषन्’ (विकासी/विकाशी, विकसन्/विकशन्) सम्भावित पाठान्तर हैं; अर्थ ‘फैलना’ वही रहता है। पंक्ति २ बिगड़ी है (सम्पादकों का संकेत): "
          "‘सस्तीक्ष्णप्रकर्षौ’ में ‘सस्’ का अर्थ अनिश्चित है (सतीक्ष्ण… या तीक्ष्णप्रकर्षौ सुझाव), ‘कैश्चित्सौ’ में ‘सौ’ शायद ‘तौ’ हो, और छन्द-गणना भी स्थिर नहीं। केवल सादा अर्थ "
          "‘कुछ ने तीक्ष्ण और प्रकर्ष की कल्पना की’ दिया गया है; ‘अतिरिक्त गुणों के रूप में’ संदर्भ से जोड़ा गया है। इस पर भरोसा न करें।",
    "50": "विश्वास: मध्यम। छपा ‘सत्वं’ सत्त्वम् का रूपान्तर है (भूल नहीं)। ‘रजस्तमश्चेति’ = रजः + तमः + च + इति। दूसरा वाक्य (‘कालार्थकर्मणां योगः …’) इस इकाई में क्रिया-रहित है "
          "और अगले श्लोक में चलता है। ‘हीनमिथ्यातिमात्रकः’ द्वन्द्व है: हीन, मिथ्या, अतिमात्र।",
}

AIDS = {
    "39": {
        "diagram": {"groups": [
            {"label": "पहली पंक्ति", "items": ["तौ", "षोढा", "दशधा", "च उक्तौ", "उत्कर्षादिविकल्पनात्"]},
            {"label": "दूसरी पंक्ति: धातु",
             "items": ["रस", "असृक्", "मांस", "मेद", "अस्थि", "मज्जा", "शुक्र"]}]},
        "letters": "मेरा बनाया सूत्र: र-अ-मां-मे-अ-म-शु (रस, असृक्, मांस, मेद, अस्थि, मज्जा, शुक्र के पहले अक्षर)।",
        "pegs": "मेरा बनाया चित्र: सात मंज़िल की इमारत, सबसे नीचे रस का कुआँ और सबसे ऊपर शुक्र का शिखर; बीच में क्रम से असृक्, मांस, मेद, अस्थि, मज्जा। "
                "केवल याद के लिए, श्लोक का दावा नहीं।",
        "sandhi": "अ + उ → ओ: च + उक्तौ → चोक्तौ; औ + स्वर → आव्: उक्तौ + उत्कर्ष → उक्ताव्-उत्कर्ष।",
        "chunks": "तौ षोढा दशधा च उक्तौ | उत्कर्ष-आदि-विकल्पनात् ‖ रस-असृक्-मांस-मेद-अस्थि-मज्जा-शुक्राणि | धातवः।",
    },
    "40": {
        "diagram": {"groups": [
            {"label": "पहली पंक्ति", "items": ["सप्त दूष्याः", "मलाः", "मूत्र", "शकृत्", "स्वेद", "आदयः अपि च"]},
            {"label": "दूसरी पंक्ति", "items": ["रसादिस्थेषु दोषेषु", "व्याधयः", "सम्भवन्ति", "ये"]}]},
        "chunks": "सप्त दूष्याः | मलाः मूत्र-शकृत्-स्वेद-आदयः अपि च ‖ रसादिस्थेषु दोषेषु | व्याधयः सम्भवन्ति ये।",
        "sandhi": "आदयः + अपि → आदयोऽपि: अः + अ → ओऽ (लुप्त अ का चिह्न ऽ)।",
        "anchors": "दूष्य = जो दूषित हो सके · मल = मैल, अपशिष्ट · मूत्र-शकृत्-स्वेद की तीन छोटी कड़ियाँ।",
    },
    "41": {
        "diagram": {"groups": [
            {"label": "पंक्ति २ की सूची",
             "items": ["प्रीणनम्", "जीवनम्", "लेपः", "स्नेहः", "धारणम्", "पूरणम्"]}]},
        "letters": "मेरा बनाया सूत्र: प्री-जी-ले-स्ने-धा-पू (छह शब्दों के पहले अक्षर)।",
        "chunks": "प्रीणनं | जीवनं | लेपः | स्नेहः | धारण-पूरणे।",
        "anchors": "जीवन = जीना, जीव · लेप = लेप लगाना · स्नेह = चिकनाई · धारण = धारण करना।",
    },
    "42": {
        "diagram": {"groups": [
            {"label": "पंक्ति १", "items": ["गर्भोत्पादः च", "कर्माणि धातूनाम्", "क्रमशः", "विदुः"]},
            {"label": "पंक्ति २", "items": ["शरीरम्", "धारयन्ति", "एते", "धात्वाहाराः च", "सर्वदा"]}]},
        "chunks": "गर्भोत्पादः च | कर्माणि धातूनां | क्रमशः विदुः ‖ शरीरं धारयन्ति | एते धात्वाहाराः च | सर्वदा।",
        "sandhi": "धातु + आहाराः → धात्वाहाराः (उ → व् + आ); उसी तरह गुरु + आज्ञा → गुर्वाज्ञा।",
        "anchors": "सर्वदा = सर्व + दा (हर समय) · धारयन्ति ← धारण (श्लोक ४१) एक ही धातु।",
    },
    "43": {
        "diagram": {"groups": [
            {"label": "पंक्ति १", "items": ["वृद्धिः समानैः", "विपरीतैः विपर्ययः"]},
            {"label": "छह रस", "items": ["स्वादु", "अम्ल", "लवण", "तिक्त", "ऊषण", "कषाय"]}]},
        "seesaw": "समान → वृद्धि ⇄ विपरीत → विपर्यय: एक ही पंक्ति में समान और विपरीत आमने-सामने हैं।",
        "letters": "मेरा बनाया सूत्र: स्वा-अ-ल-ति-ऊ-क (स्वादु, अम्ल, लवण, तिक्त, ऊषण, कषाय के पहले अक्षर)।",
        "chunks": "वृद्धिः समानैः सर्वेषां | विपरीतैः विपर्ययः ‖ रसाः | स्वादु-अम्ल-लवण-तिक्त-ऊषण-कषायकाः।",
        "sandhi": "विपरीतैः + विपर्ययः → विपरीतैर्विपर्ययः: विसर्ग घोष वर्ण से पहले र् बना।",
    },
    "44": {
        "diagram": {"groups": [
            {"label": "पंक्ति १", "items": ["षड् रस", "द्रव्य के आश्रित", "यथापूर्वं बलावहाः"]},
            {"label": "पंक्ति २", "items": ["आद्याः: मारुत को नष्ट करते हैं", "तिक्तादि तीन: कफ को नष्ट करते हैं"]}]},
        "chunks": "षड् द्रव्यम् आश्रिताः ते च | यथापूर्वं बलावहाः ‖ तत्र आद्याः मारुतं घ्नन्ति | त्रयः तिक्तादयः कफम्।",
        "sandhi": "षट् + द्रव्यम् → षड् द्रव्यम्; त्रयः + तिक्त- → त्रयस्तिक्त-: विसर्ग त से पहले स्।",
        "anchors": "आश्रित = आश्रय पाया हुआ · बलावह = बल + आवह (बल लाने वाला) · घ्नन्ति = हनन से, मारते हैं।",
    },
    "45": {
        "diagram": {"groups": [
            {"label": "पंक्ति १", "items": ["कषाय", "तिक्त", "मधुर", "पित्त (नाश)", "अन्ये तु पित्तं कुर्वते"]},
            {"label": "पंक्ति २", "items": ["शमनम्", "कोपनम्", "स्वस्थहितम्", "द्रव्यम् त्रिधा"]}]},
        "contrast": {"groups": [
            {"label": "तीन रस पित्त को", "items": ["कषाय", "तिक्त", "मधुर"]},
            {"label": "अन्य रस पित्त को", "items": ["उत्पन्न करते हैं (कुर्वते)"]}]},
        "chunks": "कषाय-तिक्त-मधुराः पित्तम् | अन्ये तु कुर्वते ‖ शमनं कोपनं स्वस्थहितं | द्रव्यम् इति त्रिधा।",
        "sandhi": "पित्तम् + अन्ये → पित्तमन्ये; द्रव्यम् + इति → द्रव्यमिति: म् स्वर के साथ लिखा जाता है।",
        "pegs": "मेरा बनाया चित्र: तीन दरवाज़े: शान्त करने वाला (शमन), भड़काने वाला (कोपन), और स्वस्थ के लिए अच्छा (स्वस्थहित)। केवल याद के लिए।",
    },
    "46": {
        "diagram": {"groups": [
            {"label": "पंक्ति १: वीर्य", "items": ["उष्ण-शीत गुण की प्रधानता", "वीर्य द्विधा"]},
            {"label": "पंक्ति २: विपाक", "items": ["द्रव्य का विपाक", "त्रिधा"]}]},
        "chunks": "उष्णशीतगुणोत्कर्षात् | तत्र वीर्यं द्विधा स्मृतं ‖ त्रिधा विपाकः द्रव्यस्य।",
        "sandhi": "गुण + उत्कर्षात् → गुणोत्कर्षात् (अ + उ → ओ); उत्कर्षात् + तत्र → उत्कर्षात्तत्र।",
        "anchors": "द्वि + धा = द्विधा (दो प्रकार) · त्रि + धा = त्रिधा (तीन प्रकार) · षोढा, दशधा (श्लोक ३९) भी इसी तरह के रूप।",
        "pegs": "मेरा बनाया चित्र: एक तराज़ू के दो पलड़े: उष्ण और शीत; जो पलड़ा भारी, वही वीर्य। केवल याद के लिए, श्लोक में तराज़ू नहीं है।",
    },
    "47": {
        "diagram": {"groups": [
            {"label": "आठ गुण (पंक्ति १)",
             "items": ["गुरु", "मन्द", "हिम", "स्निग्ध", "श्लक्ष्ण", "सान्द्र", "मृदु", "स्थिर"]},
            {"label": "पंक्ति २", "items": ["सूक्ष्म और विशद के साथ", "विपरीतों के साथ", "कुल बीस"]}]},
        "letters": "मेरा बनाया सूत्र: गु-म-हि-स्नि-श्ल-सा-मृ-स्थि (आठ गुणों के पहले अक्षर)।",
        "chunks": "गुरु-मन्द-हिम-स्निग्ध-श्लक्ष्ण-सान्द्र-मृदु-स्थिराः ‖ गुणाः स-सूक्ष्म-विशदाः | विंशतिः स-विपर्ययाः।",
        "sandhi": "ससूक्ष्मविशदाः + विंशतिः → ससूक्ष्मविशदा विंशतिः: आः के बाद घोष व् से पहले विसर्ग लुप्त।",
        "anchors": "स + विपर्यय = विपरीतों के साथ · विंशति = बीस · हिम = बर्फ़ (ठंडा)।",
    },
    "48": {
        "diagram": {"groups": [
            {"label": "पंक्ति १: अन्य गुण", "items": ["इन्द्रियार्थाः", "व्यवायी", "विकाषी (छपा रूप)"]},
            {"label": "पंक्ति २: व्यवायी", "items": ["पूरे देह में फैलकर", "पाक के योग्य"]}]},
        "chunks": "इन्द्रियार्थाः व्यवायी च | विकाषी च अपरे गुणाः ‖ व्यवायी देहम् अखिलं व्याप्य | पाकाय कल्पते।",
        "sandhi": "च + अपरे → चापरे (अ + अ → आ); इन्द्रियार्थाः + व्यवायी → इन्द्रियार्था व्यवायी: आः के बाद घोष व् से पहले विसर्ग लुप्त।",
        "anchors": "व्याप्य = वि + आप् + य (फैलकर) · अखिल = पूरा · पाक = पकना।",
    },
    "49": {
        "diagram": {"groups": [
            {"label": "पंक्ति १", "items": ["विकाषी", "विकषन् एव (फैलते ही)", "संधिबन्धान्", "विमुञ्चति"]}]},
        "chunks": "विकाषी विकषन् एव | संधिबन्धान् विमुञ्चति।",
        "sandhi": "विकषन् + एव → विकषन्नेव: ह्रस्व स्वर के बाद अन्त का न् स्वर से पहले दोहरा होता है।",
        "anchors": "संधि = जोड़ · बन्ध = बन्धन · विमुञ्चति = वि + मुच् (छोड़ना, ढीला करना)।",
    },
    "50": {
        "diagram": {"groups": [
            {"label": "पंक्ति १: महागुण", "items": ["सत्त्वम्", "रजः", "तमः"]},
            {"label": "पंक्ति २: योग तीन तरह का", "items": ["काल", "अर्थ", "कर्म", "हीन", "मिथ्या", "अतिमात्र"]}]},
        "letters": "मेरा बनाया सूत्र: स-र-त (सत्त्व, रज, तम) और ही-मि-अ (हीन, मिथ्या, अतिमात्र)।",
        "chunks": "सत्त्वं रजः तमः च इति | त्रयः प्रोक्ताः महागुणाः ‖ काल-अर्थ-कर्मणां योगः | हीन-मिथ्या-अतिमात्रकः।",
        "sandhi": "रजः + तमः + च + इति → रजस्तमश्चेति: विसर्ग त से पहले स्, च से पहले श्; अ + इ → ए।",
        "pegs": "मेरा बनाया चित्र: तीन बत्तियाँ (सत्त्व उजली, रज चलती, तम ठहरी) और तीन फिसलनें (हीन, मिथ्या, अति)। केवल याद के लिए।",
    },
}

IMAGE_SPECS = {
    ("39", "diagram"): {
        "file": "ch1b04-dhatus-39.svg",
        "alt": "Mind map with the head dhatu and the seven dhatus of verse 39 in order: rasa, blood, flesh, fat, bone, marrow, semen",
        "type": "mermaid",
        "code": """mindmap
  धातु
    रस
    असृक्
    मांस
    मेद
    अस्थि
    मज्जा
    शुक्र
""",
    },
    ("43", "diagram"): {
        "file": "ch1b04-rasas-43.svg",
        "alt": "Mind map with the head rasa and the six tastes of verse 43 in order: sweet, sour, salty, bitter, pungent, astringent",
        "type": "mermaid",
        "code": """mindmap
  रस
    स्वादु
    अम्ल
    लवण
    तिक्त
    ऊषण
    कषाय
""",
    },
    ("44", "diagram"): {
        "file": "ch1b04-rasas-act-44.svg",
        "alt": "Flowchart of verse 44: the six rasas rest in a substance; the first rasas destroy Maruta (wind); the three beginning with bitter destroy Kapha",
        "type": "mermaid",
        "code": """flowchart TD
  A["षड् रस"] --> B["द्रव्य के आश्रित"]
  A --> C["आद्याः (आदि के रस)"]
  A --> D["तिक्तादि तीन"]
  C --> E["मारुत को नष्ट करते हैं"]
  D --> F["कफ को नष्ट करते हैं"]
""",
    },
    ("47", "diagram"): {
        "file": "ch1b04-gunas-47.svg",
        "alt": "Two columns for verse 47: the eight listed qualities (heavy, slow, cold, unctuous, smooth, dense, soft, stable) and the two added (subtle, clear), twenty with their opposites",
        "type": "split",
        "title": "श्लोक ४७: गुण (विपरीतों सहित बीस)",
        "cols": [["श्लोक में गिनाए आठ", ["गुरु", "मन्द", "हिम", "स्निग्ध", "श्लक्ष्ण", "सान्द्र", "मृदु", "स्थिर"]],
                 ["साथ जुड़े दो", ["सूक्ष्म", "विशद"]]],
    },
    ("50", "diagram"): {
        "file": "ch1b04-mahagunas-50.svg",
        "alt": "Flowchart of verse 50: the conjunction of time, objects and actions may be deficient, wrong or excessive",
        "type": "mermaid",
        "code": """flowchart TD
  A["काल, अर्थ, कर्म का योग"] --> B["हीन"]
  A --> C["मिथ्या"]
  A --> D["अतिमात्र"]
""",
    },
}


for _u in AUTHORED.values():
    _q = _u["questions"][2]
    _q.setdefault("teaches", _q["rule"])
