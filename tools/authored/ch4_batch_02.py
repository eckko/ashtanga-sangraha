from helpers import mcq, match, order, fill, multi, accepts

AUTHORED = {}

# ---------------------------------------------------------------- unit 14
AUTHORED["14"] = {
    "title": "तैर्मार्गशीर्षादिभिः",
    "question": "How do the six seasons come about, and in what order are they named?",
    "rule": ("Taking the months that begin with Mārgaśīrṣa two by two, in order, "
             "there come to be six seasons: Hemanta, Śiśira, Vasanta, Grīṣma, "
             "Varṣā, Śarad."),
    "limits": ("Only the first month, Mārgaśīrṣa, is named; the verse gives no "
               "other month names and no dates. The print 'taimār-' may have lost "
               "an r (tair mār-); the meaning stays the same."),
    "explain_hi": ("यह गद्य-वाक्य ऋतुओं की गिनती देता है। मार्गशीर्ष से शुरू होने वाले "
                   "महीनों को दो-दो की संख्या में क्रम से लेने पर छह ऋतुएँ बनती हैं। "
                   "उनके नाम इसी क्रम में हैं: हेमन्त, शिशिर, वसन्त, ग्रीष्म, वर्षा, शरद। "
                   "‘द्विसंख्यैः’ का अर्थ ‘दो की संख्या वाले’ है और ‘क्रमात्’ का ‘क्रम से’। "
                   "केवल पहले महीने का नाम दिया गया है, बाकी महीनों के नाम यहाँ नहीं हैं।"),
    "hook": "मार्गशीर्ष से दो-दो मास: हेमन्त, शिशिर, वसन्त, ग्रीष्म, वर्षा, शरद।",
    "core": True,
    "questions": [
        mcq("pretest", 0,
            "How are the months beginning with Mārgaśīrṣa taken to make the six seasons?",
            ("Two by two, in order",
             "द्विसंख्यैः क्रमात्: two in number, in order."),
            [("One by one, in order", "द्विसंख्यैः says two in number, not one."),
             ("Three by three, in order", "The compound says two, not three."),
             ("Two by two, in any order", "क्रमात् says in order.")],
            "द्विसंख्यैः means two in number, and क्रमात् means in order.",
            "Months from Mārgaśīrṣa, two by two, in order, make the seasons."),
        match(1, "Match each word of the sentence to its meaning.",
              [["द्विसंख्यैः", "two in number"], ["क्रमात्", "in order"],
               ["आख्याः", "named"], ["षट्", "six"]],
              "These four words carry how the seasons are counted and named.",
              "द्विसंख्यैः = two in number; क्रमात् = in order; आख्याः = named; षट् = six."),
        fill(2, "The word for 'in order' is ____ (type it in Devanagari or in English letters, e.g. dharma).",
             accepts("क्रमात्"),
             "क्रमात् means in order; it is used here like an adverb.",
             "क्रमात् is the ablative of क्रम (order) used as 'in order, one after another'.",
             "क्रमात् = in order."),
        mcq("discriminate", 3, "Which is the right split of षडृतवो भवंति?",
            ("षट् + ऋतवः + भवन्ति",
             "ट् becomes ड् before a vowel; the visarga of ऋतवः becomes ओ before the voiced भ."),
            [("षष् + ऋतवः + भवन्ति", "षष् is not a form of the word for six."),
             ("षट् + ऋतुः + भवन्ति", "A singular ऋतुः would not give ऋतवो."),
             ("षट् + ऋतवः + भवति", "भवंति is plural, 'they are', not the singular भवति.")],
            "षट् (six) + ऋतवः (seasons) + भवन्ति (they are).",
            "Final ट् before a vowel → ड्; विसर्ग after अ before a voiced sound → ओ."),
        order(4, "Put the six seasons in the order of the sentence.",
              ["हेमन्त", "शिशिर", "वसन्त", "ग्रीष्म", "वर्षा", "शरद"],
              "The sentence names them as Hemanta, Śiśira, Vasanta, Grīṣma, Varṣā, Śarad.",
              "हेमन्त · शिशिर · वसन्त · ग्रीष्म · वर्षा · शरद.",
              role="apply"),
        mcq("transfer", 5,
            "What does the invented phrase ग्रीष्मादिभिः मासैः mean, built like मार्गशीर्षादिभिः?",
            ("By the months beginning with Grīṣma",
             "X-आदि means beginning with X; the ending -भिः is 'by', plural."),
            [("By the months ending with Grīṣma", "आदि means beginning, not ending."),
             ("By Grīṣma, the only month", "आदि means 'and the rest', so there is more than one."),
             ("Of the months beginning with Grīṣma", "-भिः is the 'by' ending, not 'of'.")],
            "ग्रीष्म + आदि + भिः: beginning with Grīṣma, by those (months).",
            "X-आदि = beginning with X.",
            teaches="A compound ending in -आदि means 'beginning with X' (मार्गशीर्षादि); the ending -भिः on it means 'by' in the plural."),
    ],
}

# ---------------------------------------------------------------- unit 15
AUTHORED["15"] = {
    "title": "तेषु शिशिरादयस्त्रयः",
    "question": "Which three seasons go with the sun's northward course, and which with the southward?",
    "rule": ("Among the six, the three beginning with Śiśira are the sun's northward "
             "course and ādāna (taking-in); the remaining three are the southward "
             "course and visarga (release)."),
    "limits": ("ādāna and visarga are kept as terms, glossed literally as taking-in "
               "and release; the verse does not explain them here. It does not name "
               "the three seasons in each half; they follow from the order of the "
               "previous unit."),
    "explain_hi": ("पिछले वाक्य के छह ऋतुओं में से शिशिर से शुरू होने वाली तीन ऋतुएँ सूर्य का "
                   "उत्तरायण (उदगयन) और आदान हैं। शेष तीन दक्षिणायन और विसर्ग हैं। "
                   "‘रवेः’ (सूर्य का) दोनों गतियों के साथ पढ़ा गया है। आदान का शाब्दिक अर्थ "
                   "‘लेना’ और विसर्ग का ‘छोड़ना, देना’ है; इस वाक्य में इनकी व्याख्या नहीं है। "
                   "‘शेषा’ में विसर्ग घोष व्यंजन से पहले छूटा है (शेषाः)।"),
    "hook": "शिशिर से तीन: उत्तरायण-आदान; शेष तीन: दक्षिणायन-विसर्ग।",
    "core": True,
    "questions": [
        mcq("pretest", 0,
            "Which course of the sun goes with the three seasons beginning with Śiśira?",
            ("The northward course (उदगयन)",
             "शिशिरादयः त्रयः are the sun's northward course and ādāna."),
            [("The southward course (दक्षिणायन)", "That goes with the remaining three."),
             ("Both courses together", "Each course gets its own three seasons."),
             ("No course is named", "Both courses are named in the sentence.")],
            "The three beginning with Śiśira are the northward course; the rest are the southward.",
            "Śiśira and two more: उदगयन + आदान; the other three: दक्षिणायन + विसर्ग."),
        match(1, "Match each word of the sentence to its meaning.",
              [["उदगयनम्", "northward course"], ["दक्षिणायनम्", "southward course"],
               ["आदानम्", "taking-in"], ["विसर्गः", "release"]],
              "These four terms are the two halves of the year in the sentence.",
              "उदगयनम् = northward course; दक्षिणायनम् = southward course; आदानम् = taking-in; विसर्गः = release."),
        fill(2, "The word for 'of the sun' is ____ (type it in Devanagari or in English letters, e.g. dharma).",
             accepts("रवेः"),
             "रवेः is the genitive singular of रवि, the sun.",
             "रवि (sun) is an -इ word; its 'of' form (genitive singular) is रवेः.",
             "रवेः = of the sun."),
        mcq("discriminate", 3, "Which is the right split of रवेरुदगयनम्?",
            ("रवेः + उदगयनम्",
             "A visarga after ए turns into र् before a vowel."),
            [("रवे + उदगयनम्", "Without the visarga there is no र् to explain the joined form."),
             ("रविः + उदगयनम्", "That would give रविरुदगयनम्, not रवेरुदगयनम्."),
             ("रवः + उदगयनम्", "रवः is not the word for sun and would give रव उदगयनम्.")],
            "रवेः (of the sun) + उदगयनम् (northward course).",
            "Visarga after a vowel other than अ/आ, before a vowel → र्."),
        order(4, "Put these phrases of the sentence in the order of the verse.",
              ["शिशिरादयः त्रयः", "रवेरुदगयनम्", "आदानं च", "शेषाः",
               "दक्षिणायनम्", "विसर्गश्च"],
              "The sentence first gives the three, their course and ādāna; then the remaining ones, their course and visarga.",
              "शिशिरादयः त्रयः · रवेरुदगयनम् · आदानं च · शेषाः · दक्षिणायनम् · विसर्गश्च.",
              role="apply"),
        mcq("transfer", 5,
            "In the invented line पञ्च जनाः; तेषु द्वौ गायकौ शेषा वादकाः, who are the वादकाः?",
            ("The three of the five who are not the two singers",
             "तेषु picks the group of five; शेषाः means the remaining ones."),
            [("The two singers themselves", "द्वौ गायकौ are the two singers; शेषाः are the others."),
             ("All five people together", "शेषाः leaves out the ones already named."),
             ("Some people outside the five", "तेषु means among them, so the group is the five.")],
            "तेषु (among them) fixes the group; शेषाः (the remaining) are those not yet named.",
            "तेषु + named part + शेषाः = the rest of that group.",
            teaches="तेषु (among them) takes a group already named; शेषाः means all the remaining members of that group, as in the sentence 'the remaining three'."),
    ],
}

# ---------------------------------------------------------------- unit 16
AUTHORED["16"] = {
    "title": "तावादानविसर्गौ वर्षम्",
    "question": "What do ādāna and visarga together make?",
    "rule": "Those two, ādāna and visarga, make a year (varṣa).",
    "limits": ("The print has varṣa without the final -m (varṣam would be the "
               "neuter nominative); the meaning is the same. The unit says only "
               "that the two together are the year."),
    "explain_hi": ("यह छोटा वाक्य पिछली इकाई की दो अवस्थाओं को जोड़ता है: वे दोनों, आदान और "
                   "विसर्ग, मिलकर एक वर्ष हैं। ‘तौ’ का अर्थ ‘वे दोनों’ है और ‘आदानविसर्गौ’ "
                   "द्विवचन का द्वन्द्व है। छपाई में ‘वर्ष’ के अंत का म् छूटा लगता है (वर्षम्)। "
                   "इस वाक्य में आदान या विसर्ग की और कोई व्याख्या नहीं है।"),
    "hook": "आदान + विसर्ग = एक वर्ष।",
    "core": False,
    "questions": [
        mcq("pretest", 0,
            "What do ādāna and visarga together make, according to the unit?",
            ("A year (varṣa)", "तौ आदानविसर्गौ वर्षम्: the two make a year."),
            [("A single season", "The two together span the six seasons, a year."),
             ("A month", "The unit names no month."),
             ("A day and a night", "Nothing of days and nights is said here.")],
            "The two together are called the year.",
            "ādāna + visarga = वर्ष, a year."),
        match(1, "Match each word of the sentence to its meaning.",
              [["तौ", "those two"], ["आदान", "taking-in"],
               ["विसर्ग", "release"], ["वर्ष", "year"]],
              "These four words are the whole sentence.",
              "तौ = those two; आदान = taking-in; विसर्ग = release; वर्ष = year."),
        fill(2, "The word for 'year' (the print has वर्ष) is ____ (type it in Devanagari or in English letters, e.g. dharma).",
             accepts("वर्षम्", "वर्ष"),
             "वर्ष is the year; the print leaves off the final म्.",
             "वर्ष (neuter) names the year; the full nominative is वर्षम्, and the print's वर्ष is accepted.",
             "वर्ष(म्) = year."),
        mcq("discriminate", 3, "Which is the right split of तावादानविसर्गौ?",
            ("तौ + आदानविसर्गौ",
             "औ before a vowel becomes आव्: तौ + आ- gives ताव्-आ-."),
            [("ताव + आदानविसर्गौ", "ताव is not a word."),
             ("तु + आदानविसर्गौ", "तु would give त्वादान-, not तावादान-."),
             ("ताः + आदानविसर्गौ", "ताः would give ता आदान- or ता रादान-, not तावादान-.")],
            "तौ (those two) + आदानविसर्गौ (ādāna and visarga).",
            "औ + a vowel → आव् + vowel."),
        order(4, "Put the parts of the sentence in the order of the verse.",
              ["तौ", "आदान", "विसर्गौ", "वर्ष"],
              "The sentence runs: those two, ādāna and visarga, a year.",
              "तौ · आदान · विसर्गौ · वर्ष.",
              role="apply"),
        mcq("transfer", 5,
            "What does the invented dual compound मातापितरौ mean, built like आदानविसर्गौ?",
            ("Mother and father, the two",
             "A dual in -औ joins two things: both are named."),
            [("The mother's father", "A genitive link would not end in -औ."),
             ("Mothers and fathers, many", "-औ marks two, not many."),
             ("A father like a mother", "Nothing in the form says 'like'.")],
            "आदानविसर्गौ names two things together; मातापितरौ does the same for mother and father.",
            "Dvandva in dual -औ = the two named, together.",
            teaches="A dvandva in the dual (-औ) names two things together, as आदानविसर्गौ does; मातापितरौ names mother and father."),
    ],
}

# ---------------------------------------------------------------- unit 17
AUTHORED["17"] = {
    "title": "तयोरादानमाग्नेयम्",
    "question": "Which of the two, ādāna or visarga, is called āgneya?",
    "rule": "Of those two, ādāna is āgneya (fiery, belonging to Agni).",
    "limits": ("The verse only gives the label āgneya to ādāna; it does not say "
               "here why. The other half, visarga, is described in the next unit."),
    "explain_hi": ("पिछली इकाई में आदान और विसर्ग मिलकर वर्ष थे। यहाँ कहा गया है कि उन दोनों में "
                   "आदान ‘आग्नेय’ है, यानी अग्नि से संबंधित, उष्ण स्वभाव वाला। "
                   "‘तयोः’ का अर्थ ‘उन दोनों में’ है। ‘आदानम्’ और ‘आग्नेयम्’ दोनों नपुंसक हैं, "
                   "इसलिए विशेषण संज्ञा के लिंग में चलता है। इस वाक्य में आदान के कारण की "
                   "कोई व्याख्या नहीं है।"),
    "hook": "उन दोनों में आदान = आग्नेय।",
    "core": False,
    "questions": [
        mcq("pretest", 0,
            "Of ādāna and visarga, which is called āgneya in this unit?",
            ("ādāna", "तयोः आदानम् आग्नेयम्: of the two, ādāna is āgneya."),
            [("visarga", "Visarga is not named in this unit."),
             ("both of them", "Only ādāna gets the label here."),
             ("neither of them", "The label is given to ādāna.")],
            "आदानम् is the subject and आग्नेयम् says what it is.",
            "तयोः आदानम् आग्नेयम् = of the two, ādāna is āgneya."),
        match(1, "Match each word of the sentence to its meaning.",
              [["तयोः", "of those two"], ["आदानम्", "ādāna (taking-in)"],
               ["आग्नेयम्", "fiery, belonging to Agni"]],
              "These three words are the whole sentence.",
              "तयोः = of those two; आदानम् = ādāna; आग्नेयम् = fiery, belonging to Agni."),
        fill(2, "The word for 'fiery, belonging to Agni' is ____ (type it in Devanagari or in English letters, e.g. dharma).",
             accepts("आग्नेयम्"),
             "आग्नेयम् is the neuter form agreeing with आदानम्.",
             "आग्नेय is made from अग्नि; in the sentence it is neuter, like आदानम्.",
             "आग्नेयम् = fiery (of Agni)."),
        mcq("discriminate", 3, "Which is the right split of तयोरादानमाग्नेयम्?",
            ("तयोः + आदानम् + आग्नेयम्",
             "A visarga after ओ turns into र् before a vowel."),
            [("तयोः + दानम् + आग्नेयम्", "That would be written तयोर्दानम्, without the long आ."),
             ("तयोर + आदानम् + आग्नेयम्", "Dropping the visarga leaves no र् to join the words."),
             ("तयोः + आदानम् + अग्नेयम्", "अग्नेयम् is not the word; the word is आग्नेयम्.")],
            "तयोः (of those two) + आदानम् + आग्नेयम्.",
            "Visarga after a vowel other than अ/आ, before a vowel → र्."),
        order(4, "Put the words of the sentence in the order of the verse.",
              ["तयोः", "आदानम्", "आग्नेयम्"],
              "The sentence runs: of those two, ādāna, fiery.",
              "तयोः · आदानम् · आग्नेयम्.",
              role="apply"),
        mcq("transfer", 5,
            "Which word completes the invented line तयोः जलं ____ ('of the two, the water is cool'), agreeing like आग्नेयम्?",
            ("शीतलम्", "जलम् is neuter, so the describing word is neuter: -म्."),
            [("शीतलः", "This is masculine; जलम् is neuter."),
             ("शीतला", "This is feminine; जलम् is neuter."),
             ("शीतलाः", "This is masculine plural; जलम् is singular neuter.")],
            "A describing word agrees with its noun: neuter आदानम् → neuter आग्नेयम्; neuter जलम् → neuter शीतलम्.",
            "Describing word agrees with its noun in gender, number and case.",
            teaches="A word that says what something is (आग्नेयम्) takes the gender and number of its noun (आदानम्, neuter singular)."),
    ],
}

# ---------------------------------------------------------------- unit 18
AUTHORED["18"] = {
    "title": "तस्मिन् खलु कालस्वभावमार्ग",
    "question": "What do the sun and the winds do in ādāna, according to this sentence?",
    "rule": ("In ādāna the sun and the winds, sharp and dry, dry up the quality "
             "born of Soma, take the world's moisture, greatly strengthen the "
             "dry tastes (bitter, astringent, pungent) and bring weakness to men."),
    "limits": ("The compound 'kāla-svabhāva-mārga-parigṛhītaḥ' can be read as "
               "seized or governed by the nature and course of time; no question "
               "rests on it. The verse says what happens, not what to do about "
               "it, and gives no remedy."),
    "explain_hi": ("‘तस्मिन्’ का अर्थ आदान में है (इकाई १७)। यह एक लंबा वाक्य है जिसके दो कर्ता "
                   "हैं: सूर्य और उसके संपर्क से तीव्र और रूखी वायुएँ। श्लोक कहता है कि वे सोम से "
                   "उत्पन्न गुण को सुखाती हैं, संसार की स्निग्धता को लेती हैं, ऋतुओं के क्रम से "
                   "आए रूखेपन के कारण रूखे रसों, यानी तिक्त, कषाय और कटु को अत्यंत प्रबल करती हैं, "
                   "और मनुष्यों में दुर्बलता लाती हैं। यहाँ केवल यही कहा गया है; कोई उपाय या सलाह "
                   "इस वाक्य में नहीं है।"),
    "hook": "आदान में सूर्य और रूखी वायु: स्निग्धता घटती, तिक्त-कषाय-कटु बढ़ते, दुर्बलता आती।",
    "core": True,
    "questions": [
        mcq("pretest", 0,
            "According to this sentence, what do the sun and the winds bring to men in ādāna?",
            ("Weakness (दौर्बल्य)",
             "नृणां दौर्बल्यमावहन्ति: they bring weakness to men."),
            [("Strength (बल)", "Strength being built up is said of visarga, in the later unit."),
             ("Sleep (निद्रा)", "Sleep is not mentioned in this sentence."),
             ("Hunger (क्षुधा)", "Hunger is not mentioned in this sentence.")],
            "The last clause says they bring weakness to men.",
            "आदान: the sun and the winds bring दौर्बल्य to men."),
        match(1, "Match each word of the sentence to its meaning.",
              [["तिक्त", "bitter"], ["कषाय", "astringent"], ["कटु", "pungent"],
               ["स्नेह", "moisture, unctuousness"]],
              "The sentence names three tastes that are strengthened and one thing that is taken away.",
              "तिक्त = bitter; कषाय = astringent; कटु = pungent; स्नेह = moisture."),
        fill(2, "The word for 'sun' in this sentence is ____ (type it in Devanagari or in English letters, e.g. dharma).",
             accepts("अर्कः", "अर्क"),
             "अर्कः is the sun, the first subject of the sentence.",
             "अर्क is one of the words for the sun; here it is the subject with the winds (वायवः).",
             "अर्कः = sun."),
        mcq("discriminate", 3, "Which is the right split of अत्यर्थोष्ण-?",
            ("अत्यर्थ + उष्ण",
             "अ + उ joins as ओ: अत्यर्थ + उष्ण = अत्यर्थोष्ण."),
            [("अत्यर्थ + ओष्ण", "That would join as अत्यर्थौष्ण, and ओष्ण is not a word here."),
             ("अत्यर्थ + अष्ण", "अष्ण is not a word, and the उ would be lost."),
             ("अत्यर्थे + उष्ण", "ए + उ would give अत्यर्थ्युष्ण, not अत्यर्थोष्ण.")],
            "अत्यर्थ (very) + उष्ण (hot): very hot.",
            "अ/आ + उ/ऊ → ओ.",
            ),
        order(4, "Put these parts of the sentence in the order of the verse.",
              ["अर्कः", "तत्संपर्काद्वायवः", "सोमजं गुणमुपशोषयंतः",
               "जगतः स्नेहमाददानाः", "रसानभिप्रबलयंतः", "दौर्बल्यमावहंति"],
              "The two subjects come first, then the three things they do as participles, then the main verb: they bring weakness.",
              "अर्कः · तत्संपर्काद्वायवः · सोमजं गुणमुपशोषयंतः · जगतः स्नेहमाददानाः · रसानभिप्रबलयंतः · दौर्बल्यमावहंति.",
              role="apply"),
        mcq("transfer", 5,
            "In the invented line बालाः गायन्तः गच्छन्ति, what does गायन्तः say, like उपशोषयन्तः?",
            ("The boys go while singing",
             "A -न्तः present participle says what the subject does at the same time."),
            [("One boy sang yesterday", "गायन्तः is plural and present, not past."),
             ("The place the boys go to", "A participle in -न्तः is not a place word."),
             ("The boys will sing later", "It is a present participle, not a future.")],
            "उपशोषयन्तः (drying up) goes with the plural subjects and says what they do while the main verb happens.",
            "Present participle masculine plural in -न्तः = 'doing X' with a plural subject.",
            teaches="A present participle in -न्तः (masculine plural) describes what the plural subject is doing at the same time as the main verb, as in उपशोषयन्तः."),
    ],
}

# ---------------------------------------------------------------- unit 19
AUTHORED["19"] = {
    "title": "विसर्गस्तु सौम्यः",
    "question": "What is visarga called here, in contrast to ādāna?",
    "rule": "Visarga, however (तु), is saumya (gentle, of the nature of Soma, the moon).",
    "limits": ("The verse only gives the label saumya to visarga and does not "
               "explain it here. The word saumya can be gentle or 'of Soma'; both "
               "are kept."),
    "explain_hi": ("पिछली इकाई में आदान को आग्नेय कहा गया था। यहाँ ‘तु’ (किन्तु) के साथ बताया "
                   "गया है कि विसर्ग सौम्य है, यानी सौम्य, सोम से संबंधित। यह एक छोटा "
                   "वाक्य है। ‘विसर्गस्तु’ में विसर्गः का विसर्ग त से पहले स् बन गया है। "
                   "अगली इकाई इसी विसर्ग का वर्णन करती है।"),
    "hook": "आदान आग्नेय, विसर्ग तो सौम्य।",
    "core": False,
    "questions": [
        mcq("pretest", 0,
            "Which of the two, ādāna or visarga, is called saumya here?",
            ("visarga", "विसर्गः तु सौम्यः: visarga, however, is saumya."),
            [("ādāna", "Ādāna was called āgneya in unit 17."),
             ("both of them", "Only visarga gets the label in this sentence."),
             ("neither of them", "Visarga is called saumya.")],
            "विसर्गः is the subject and सौम्यः tells what it is.",
            "विसर्गः तु सौम्यः = visarga, however, is saumya."),
        match(1, "Match each word of the sentence to its meaning.",
              [["विसर्गः", "release"], ["तु", "but, however"],
               ["सौम्यः", "gentle, of Soma"]],
              "These three words are the whole sentence.",
              "विसर्गः = release; तु = but, however; सौम्यः = gentle, of Soma."),
        fill(2, "The word for 'but, however' is ____ (type it in Devanagari or in English letters, e.g. dharma).",
             accepts("तु"),
             "तु sets this sentence against the one before it.",
             "तु is a small word meaning but or however; it comes after the first word of its clause.",
             "तु = but, however."),
        mcq("discriminate", 3, "Which is the right split of विसर्गस्तु?",
            ("विसर्गः + तु",
             "A visarga before त turns into स्."),
            [("विसर्गो + तु", "ओ appears before a voiced sound; त is not voiced."),
             ("विसर्गः + च", "च would give विसर्गश्च; the word here is तु."),
             ("विसर्गात् + तु", "That would be written विसर्गात्तु, with त्, not स्.")],
            "विसर्गः (visarga) + तु (but).",
            "Visarga before त → स्."),
        order(4, "Put the words of the sentence in the order of the verse.",
              ["विसर्गः", "तु", "सौम्यः"],
              "The sentence runs: visarga, however, saumya.",
              "विसर्गः · तु · सौम्यः.",
              role="apply"),
        mcq("transfer", 5,
            "In the invented pair दिनं उष्णम्; रात्रिः तु शीतला, what does तु signal?",
            ("A contrast with the sentence before",
             "तु marks 'but, however': the second sentence is set against the first."),
            [("The same thing said again", "तु marks a contrast, not a repetition."),
             ("A question about the night", "तु does not make a question."),
             ("Something that happened earlier", "तु says nothing about time.")],
            "तु sets रात्रिः against दिनम्, as विसर्गः तु is set against आदान.",
            "तु = but, however: contrast with what came before.",
            teaches="तु, after the first word of a sentence, sets that sentence against the one before it (विसर्गस्तु after आदानम् आग्नेयम्)."),
    ],
}

# ---------------------------------------------------------------- unit 20
AUTHORED["20"] = {
    "title": "तस्मिन्नपि कालमार्गमेघ",
    "question": "What increases in visarga, and what is built up in men?",
    "rule": ("In visarga, when the sun's power is struck down and the moon is "
             "unimpeded, the non-dry tastes (sour, salty, sweet) increase in "
             "due order and men's strength is built up."),
    "limits": ("The verse describes what happens in visarga; it gives no advice. "
               "'Mahendra's water' is kept literal. 'Due order' (यथाक्रमम्) is "
               "placed with both the tastes and the strength."),
    "explain_hi": ("‘तस्मिन्’ यहाँ विसर्ग के लिए है (इकाई १९)। एक लंबा वाक्य पहले स्थितियाँ बताता है: "
                   "सूर्य दक्षिणायन में है और काल-मार्ग, मेघ, वायु और वर्षा से उसका प्रभाव दब गया है; "
                   "चंद्रमा का बल अबाधित है; जगत् शीतल किरणों से निरंतर तृप्त हो रहा है और "
                   "महेन्द्र के जल से उसका ताप शांत है। तब अरूखे रस, यानी अम्ल, लवण और मधुर, "
                   "क्रम से बढ़ते हैं और मनुष्यों का बल संचित होता है। इसका आदान वाले वाक्य "
                   "(इकाई १८) से उलटा चित्र है, पर श्लोक कोई सलाह नहीं देता।"),
    "hook": "विसर्ग में सूर्य दबा, चंद्र प्रबल: अम्ल-लवण-मधुर बढ़ते और बल संचित होता।",
    "core": True,
    "questions": [
        mcq("pretest", 0,
            "What does the sentence say happens to men's strength in visarga?",
            ("It is built up (उपचीयते)",
             "बलं चोपचीयते नृणाम्: the strength of men is built up."),
            [("It is lost (क्षीयते)", "Weakness is the word of the ādāna sentence (unit 18)."),
             ("It stays as before", "The sentence says it is built up."),
             ("It is turned into heat", "Nothing like this is said.")],
            "The last clause says men's strength is built up.",
            "visarga: non-dry tastes increase; strength is built up."),
        match(1, "Match each word of the sentence to its meaning.",
              [["अम्ल", "sour"], ["लवण", "salty"], ["मधुर", "sweet"],
               ["अरूक्षाः", "not dry"]],
              "The sentence names three tastes and calls them not dry.",
              "अम्ल = sour; लवण = salty; मधुर = sweet; अरूक्षाः = not dry."),
        fill(2, "The word for 'strength' is ____ (type it in Devanagari or in English letters, e.g. dharma).",
             accepts("बलम्"),
             "बलम् is strength, the second thing that increases.",
             "बल is strength; in the sentence it is the subject of उपचीयते (is built up).",
             "बलम् = strength."),
        multi("discriminate", 3,
              "Which tastes does this sentence say increase in visarga? Select all.",
              [("अम्ल (sour)", "Right: it is the first of the three."),
               ("लवण (salty)", "Right: it is the second of the three."),
               ("मधुर (sweet)", "Right: it is the third of the three."),
               ("तिक्त (bitter)", "Bitter is one of the dry tastes of the ādāna sentence (unit 18)."),
               ("कषाय (astringent)", "Astringent is a dry taste of the ādāna sentence (unit 18)."),
               ("कटु (pungent)", "Pungent is a dry taste of the ādāna sentence (unit 18).")],
              [0, 1, 2],
              "Visarga: sour, salty and sweet increase; bitter, astringent and pungent are the ādāna tastes.",
              "Visarga: अम्ल, लवण, मधुर. Ādāna: तिक्त, कषाय, कटु."),
        order(4, "Put these phrases of the sentence in the order of the verse.",
              ["दक्षिणायनगेऽर्के", "शशिनि चाव्याहतबले",
               "शिशिराभिर्भाभिः शश्वदाप्यायमाने", "अरूक्षा रसाः प्रवर्द्धंते",
               "बलं चोपचीयते"],
              "The sentence gives the sun, the moon and the refreshed world first, then the tastes increase and strength is built up.",
              "दक्षिणायनगेऽर्के · शशिनि चाव्याहतबले · शिशिराभिर्भाभिः शश्वदाप्यायमाने · अरूक्षा रसाः प्रवर्द्धंते · बलं चोपचीयते.",
              role="apply"),
        mcq("transfer", 5,
            "What does the invented line मेघे गर्जति मयूराः नृत्यन्ति mean, with a locative phrase like अर्के?",
            ("When the cloud thunders, peacocks dance",
             "मेघे गर्जति (locative) sets the circumstance, as अर्के … does."),
            [("In the cloud, peacocks dance", "मेघे गर्जति is a phrase with its own verb form, not just a place."),
             ("The cloud thunders for the peacocks", "Nothing marks the peacocks as the aim."),
             ("After the peacocks dance, it thunders", "The locative phrase is the circumstance, not a later event.")],
            "In the verse, locative phrases like अर्के, शशिनि, जगति give the circumstances, then the main clause follows.",
            "Locative noun + locative participle = 'when X is so'.",
            teaches="A noun with a participle, both in the locative (सूर्य दक्षिणायनगे), sets the circumstance 'when X is so' before the main clause."),
    ],
}

# ---------------------------------------------------------------- unit 21
AUTHORED["21"] = {
    "title": "भवति चात्र",
    "question": "What does this short formula do?",
    "rule": "'And on this matter there is the following': a formula that introduces the verses from unit 22 onward.",
    "limits": ("The unit itself says nothing about seasons. It only introduces "
               "what follows. The introduction role is the convention noted by "
               "the data, not a statement of the verse."),
    "explain_hi": ("यह एक छोटा सूत्र-वाक्य है: ‘और इस विषय में यह है’। गद्य के बाद श्लोक "
                   "लाने से पहले यह पंक्ति आती है। इस इकाई में कोई नई बात नहीं कही गई। "
                   "‘चात्र’ में च और अत्र जुड़े हैं (अ + अ → आ)।"),
    "hook": "‘और इस विषय में यह है’: आगे के श्लोकों का द्वार।",
    "core": False,
    "questions": [
        mcq("pretest", 0,
            "What does भवति चात्र do in the text?",
            ("It introduces the verses that follow",
             "'And on this matter there is the following': then verses come."),
            [("It ends the chapter", "The chapter continues after this line."),
             ("It names a new season", "No season is named in this line."),
             ("It gives a list of foods", "No food is named in this line.")],
            "The line points ahead to what is said next.",
            "भवति चात्र = and on this there is (the following)."),
        match(1, "Match each word of the line to its meaning.",
              [["भवति", "there is"], ["च", "and"], ["अत्र", "here, on this"]],
              "These three words are the whole line.",
              "भवति = there is; च = and; अत्र = here, on this."),
        fill(2, "The word for 'here, on this' is ____ (type it in Devanagari or in English letters, e.g. dharma).",
             accepts("अत्र"),
             "अत्र means here or on this matter.",
             "अत्र is a small word of place: here; with a matter it means on this.",
             "अत्र = here, on this."),
        mcq("discriminate", 3, "Which is the right split of चात्र?",
            ("च + अत्र",
             "अ + अ joins as आ: च + अत्र = चात्र."),
            [("चा + अत्र", "चा is not a word."),
             ("च + आत्र", "आत्र is not a word."),
             ("चः + अत्र", "A visarga here would not give चात्र.")],
            "च (and) + अत्र (here).",
            "अ + अ → आ."),
        order(4, "Put the words of the line in the order of the verse.",
              ["भवति", "च", "अत्र"],
              "The line runs: there is, and, here.",
              "भवति · च · अत्र.",
              role="apply"),
        mcq("transfer", 5,
            "Which is the correct joining of तथा + अत्र?",
            ("तथात्र", "आ + अ joins as आ, like च + अत्र = चात्र."),
            [("तथत्र", "The long आ stays long; it is not shortened."),
             ("तथैत्र", "ऐ would come from आ + ए or ऐ, not from आ + अ."),
             ("तथोत्र", "ओ would come from आ + उ, not from आ + अ.")],
            "Same rule as चात्र: a or ā meeting a or ā gives ā.",
            "अ/आ + अ/आ → आ.",
            teaches="When अ or आ meets अ or आ, the two become one long आ (च + अत्र = चात्र; तथा + अत्र = तथात्र)."),
    ],
}

# ---------------------------------------------------------------- unit 22
AUTHORED["22"] = {
    "title": "हेमंते शिशिरे चाप्यं",
    "question": "In which pairs of seasons is the strength of visarga and ādāna middling, and in which low?",
    "rule": ("In Śarad and Vasanta the strength of visarga and ādāna is middling "
             "(मध्य); in Varṣā and Nidāgha (the hot season) it is low (हीन)."),
    "limits": ("The grade for Hemanta and Śiśira rests on the printed word "
               "'cāpyam', which would read 'and watery'; the series best / "
               "middling / low suggests 'cāgryam', but this is not certain, so "
               "no question rests on that grade. The editors call the Hindi and "
               "English layers loose."),
    "explain_hi": ("यह श्लोक ऋतु-जोड़ियों के साथ विसर्ग और आदान के बल का दर्जा बताता है। "
                   "शरद और वसन्त में बल मध्यम है; वर्षा और निदाघ (ग्रीष्म) में हीन। "
                   "पहली पंक्ति में छपा ‘चाप्यम्’ अस्पष्ट है (संभवतः ‘चाग्र्यम्’, सर्वोत्तम), "
                   "इसलिए उस जोड़ी पर प्रश्न नहीं बने। क्रिया नहीं है; ‘बलम्’ दूसरी पंक्ति में भी "
                   "समझा जाता है। श्लोक केवल जोड़ियाँ गिनाता है, कारण नहीं बताता।"),
    "hook": "हेमन्त-शिशिर (पाठ संदिग्ध) · शरद-वसन्त: मध्यम · वर्षा-निदाघ: हीन।",
    "core": True,
    "questions": [
        mcq("pretest", 0,
            "In Śarad and Vasanta, how is the strength of visarga and ādāna graded?",
            ("Middling (मध्यम्)",
             "शरद्वसन्तयोः मध्यम्: in Śarad and Vasanta, middling."),
            [("Low (हीनम्)", "Low is the grade of Varṣā and Nidāgha."),
             ("Absent altogether", "No season is said to have none."),
             ("The same as Varṣā", "Varṣā goes with Nidāgha and is low.")],
            "The second line gives Śarad and Vasanta as middling.",
            "Śarad, Vasanta: middling; Varṣā, Nidāgha: low."),
        match(1, "Match each word of the verse to its meaning.",
              [["मध्यम्", "middling"], ["हीनम्", "low, poor"],
               ["बलम्", "strength"], ["निदाघः", "hot season"]],
              "These words carry the grades and the names of the second line.",
              "मध्यम् = middling; हीनम् = low, poor; बलम् = strength; निदाघः = hot season."),
        fill(2, "The word for 'low, poor' is ____ (type it in Devanagari or in English letters, e.g. dharma).",
             accepts("हीनम्"),
             "हीनम् is the grade given to Varṣā and Nidāgha.",
             "हीन means lacking, low; it is neuter to agree with बलम्.",
             "हीनम् = low, poor."),
        mcq("discriminate", 3,
            "Which two seasons does the verse pair together with the grade 'low'?",
            ("Varṣā and Nidāgha", "वर्षा निदाघयोः are joined and given हीनम्."),
            [("Śarad and Vasanta", "That pair is middling, not low."),
             ("Vasanta and Varṣā", "The verse does not pair these two."),
             ("Śiśira and Śarad", "The verse does not pair these two.")],
            "The verse gives its pairs as: Hemanta-Śiśira, Śarad-Vasanta, Varṣā-Nidāgha.",
            "Pairs: हेमन्त-शिशिर · शरद-वसन्त · वर्षा-निदाघ."),
        order(4, "Put the three pairs of seasons in the order of the verse.",
              ["हेमंते शिशिरे च", "शरद्वसंतयोः", "वर्षा निदाघयोः"],
              "The verse takes Hemanta and Śiśira first, then Śarad and Vasanta, then Varṣā and Nidāgha.",
              "हेमंते शिशिरे च · शरद्वसंतयोः · वर्षा निदाघयोः.",
              role="apply"),
        mcq("transfer", 5,
            "What does the invented word ग्रीष्मवसन्तयोः mean, built like शरद्वसन्तयोः?",
            ("Of or in the two, Grīṣma and Vasanta",
             "A joined pair with the dual ending -योः names both together."),
            [("Of Grīṣma alone, called Vasanta", "A joined pair names two things, not one."),
             ("In the many seasons from Grīṣma", "-योः is dual, not many."),
             ("After Grīṣma and Vasanta", "The ending does not mean after.")],
            "शरद्वसन्तयोः = Śarad and Vasanta, the two; ग्रीष्मवसन्तयोः works the same way.",
            "Joined pair + -योः = the two named, together.",
            teaches="Two nouns joined into one word with the dual ending -योः name both together (शरद्वसन्तयोः, 'of or in Śarad and Vasanta')."),
    ],
}

# ---------------------------------------------------------------- unit 23
AUTHORED["23"] = {
    "title": "धूमधूम्रा रजोमंदाः",
    "question": "What does the north do because of the wind's coldness?",
    "rule": ("The directions and the suns are smoke-grey, dim with dust, with "
             "discs clouded by frost; and the north, because of the wind's "
             "coldness, makes the hair stand on end."),
    "limits": ("The unit does not name a season. The editors flag the odd "
               "plural 'ādityāḥ' and the reading of 'dig-ādityāḥ'; no question "
               "rests on it. 'uttaraḥ' may be the north direction or the north "
               "wind; 'north' is kept."),
    "explain_hi": ("यह श्लोक एक दृश्य का वर्णन है। पहली पंक्ति के विशेषण हैं: धुएँ जैसे धूसर, "
                   "धूल से मंद और पाले से धुँधले मंडलों वाले। दूसरी पंक्ति में इनका कर्ता "
                   "‘दिगादित्याः’ आता है (दिशाएँ और सूर्य; यह पाठ संदिग्ध है)। फिर कहा गया है कि "
                   "वायु की शीतलता के कारण उत्तर रोमांच उत्पन्न करता है। श्लोक में ऋतु का नाम "
                   "नहीं है, इसलिए केवल वही कहा गया है जो पाठ में है।"),
    "hook": "धूसर, धूल-मंद, पाले-धुँधले; शीतल वायु से उत्तर में रोमांच।",
    "core": False,
    "questions": [
        mcq("pretest", 0,
            "Because of the wind's coldness, what does the north do in this verse?",
            ("Makes the hair stand on end",
             "मरुच्छैत्यादुत्तरो रोमहर्षणः: from the wind's coldness the north causes horripilation."),
            [("Makes the rivers steam", "Steaming rivers are in a later verse."),
             ("Makes the plants flower", "Flowering plants are in the verse after this one."),
             ("Makes the sky clear", "The verse says the opposite: dim and clouded.")],
            "The second line ends with रोमहर्षणः, causing the hair to stand on end.",
            "उत्तरः + रोमहर्षणः: the north makes the hair stand on end."),
        match(1, "Match each word of the verse to its meaning.",
              [["धूमधूम्राः", "smoke-grey"], ["रजोमन्दाः", "dim with dust"],
               ["तुषाराविलमण्डलाः", "with discs clouded by frost"],
               ["रोमहर्षणः", "causing the hair to stand on end"]],
              "These four words describe what the verse shows.",
              "धूमधूम्राः = smoke-grey; रजोमन्दाः = dim with dust; तुषाराविलमण्डलाः = discs clouded by frost; रोमहर्षणः = hair-raising."),
        fill(2, "The word for 'frost' (as in तुषार-आविल) is ____ (type it in Devanagari or in English letters, e.g. dharma).",
             accepts("तुषार"),
             "तुषार is frost, the cause of the cloudy discs.",
             "तुषार names frost; in the compound it is the first member: clouded by frost.",
             "तुषार = frost."),
        mcq("discriminate", 3, "Which is the right split of मरुच्छैत्यादुत्तरो?",
            ("मरुत् + शैत्यात् + उत्तरः",
             "त् before श joins as च्छ; शैत्यात् + उत्तरः gives शैत्यादुत्तरः."),
            [("मरुः + शैत्यात् + उत्तरः", "A visarga before श would give मरुश्शैत्यात्."),
             ("मरुत् + सैत्यात् + उत्तरः", "सैत्यात् is not a word; the word is शैत्यात्."),
             ("मरुत् + चैत्यात् + उत्तरः", "त् + च gives च्च, not च्छ, and चैत्य is not coldness.")],
            "मरुत् (wind) + शैत्यात् (from coldness) + उत्तरः (north).",
            "त् + श → च्छ; त् before a vowel-led word → द्."),
        order(4, "Put these words of the verse in the order of the verse.",
              ["धूमधूम्राः", "रजोमन्दाः", "तुषाराविलमण्डलाः",
               "मरुच्छैत्यात्", "रोमहर्षणः"],
              "The verse gives the three descriptions first, then the cold wind and the hair-raising north.",
              "धूमधूम्राः · रजोमन्दाः · तुषाराविलमण्डलाः · मरुच्छैत्यात् · रोमहर्षणः.",
              role="apply"),
        mcq("transfer", 5,
            "Built like तुषाराविलमण्डलाः, what does the invented मेघावृतशिखराः describe?",
            ("Things whose peaks are covered by clouds",
             "First part says by what, then the state, then whose: मेघ + आवृत + शिखराः."),
            [("Things that cover peaks with clouds", "आवृत is passive: covered, not covering."),
             ("Clouds that have peaks", "The clouds are the covering, not the owners of the peaks."),
             ("Peaks that are made of cloud", "आवृत means covered, not made of.")],
            "तुषार-आविल-मण्डलाः = those with discs clouded by frost; मेघ-आवृत-शिखराः = those with peaks covered by clouds.",
            "By-what + state + whose, all in one word.",
            teaches="A compound can say 'by what, in what state, whose': तुषार (frost) + आविल (clouded) + मण्डल (disc) = those whose discs are clouded by frost."),
    ],
}

# ---------------------------------------------------------------- unit 24
AUTHORED["24"] = {
    "title": "रोधप्रियंगुपुन्नाग",
    "question": "What is said of the four plants, and what of the six animals?",
    "rule": ("Rodha, priyaṅgu, punnāga and lavalī (plant names) are bright with "
             "blossoms; elephants, goats, buffaloes, horses, crows and pigs are "
             "spirited."),
    "limits": ("The plants are names only and are not identified; 'rodha' may be "
               "a slip for 'rodhra', so no question rests on that spelling. The "
               "verse does not name a season and does not say 'forests'."),
    "explain_hi": ("इस श्लोक की पहली पंक्ति चार पौधों के नाम देती है, जो फूलों से दीप्त हैं। "
                   "दूसरी पंक्ति छह प्राणियों को ‘दृप्त’ (मदमस्त, उत्साही) कहती है: हाथी, बकरे, "
                   "भैंसे, घोड़े, कौए और सूअर। पौधों के नाम केवल नाम हैं, उनकी पहचान नहीं की गई। "
                   "श्लोक में कोई ऋतु नहीं बताई गई है। ‘दृप्ता’ में अंत का विसर्ग घोष व्यंजन से पहले "
                   "छूटा है (दृप्ताः)।"),
    "hook": "चार पौधे फूलों से दीप्त; हाथी, बकरे, भैंसे, घोड़े, कौए, सूअर दृप्त।",
    "core": False,
    "questions": [
        mcq("pretest", 0,
            "Which of these creatures does the verse name among the spirited (दृप्त) ones?",
            ("Crows (वायस)", "वायस is the fifth of the six animals named."),
            [("Cows (गो)", "Cows are not named in the verse."),
             ("Deer (मृग)", "Deer are not named in the verse."),
             ("Dogs (श्वन्)", "Dogs are not named in the verse.")],
            "The six are elephants, goats, buffaloes, horses, crows and pigs.",
            "दृप्त: गज, अज, महिष, वाजि, वायस, सूकर."),
        match(1, "Match each animal word of the verse to its meaning.",
              [["गज", "elephant"], ["अज", "goat"], ["महिष", "buffalo"],
               ["वायस", "crow"], ["सूकर", "pig"]],
              "These five of the six animal words are in the second line.",
              "गज = elephant; अज = goat; महिष = buffalo; वायस = crow; सूकर = pig."),
        fill(2, "The word for 'spirited, proud' (masculine plural) is ____ (type it in Devanagari or in English letters, e.g. dharma).",
             accepts("दृप्ताः"),
             "दृप्ताः says what the six animals are.",
             "दृप्त describes the animals in the plural; the print drops the final visarga before the voiced ग.",
             "दृप्ताः = spirited, proud."),
        mcq("discriminate", 3, "Which is the right split of कुसुमोज्ज्वलाः?",
            ("कुसुम + उज्ज्वलाः",
             "अ + उ joins as ओ: कुसुम + उज्ज्वलाः = कुसुमोज्ज्वलाः."),
            [("कुसुम + ओज्ज्वलाः", "That would join as कुसुमौज्ज्वलाः, with औ."),
             ("कुसुमः + उज्ज्वलाः", "That would be written कुसुम उज्ज्वलाः."),
             ("कुसुम + ज्वलाः", "The उ would be lost, and the word is उज्ज्वल.")],
            "कुसुम (blossom) + उज्ज्वलाः (bright): bright with blossoms.",
            "अ + उ → ओ."),
        order(4, "Put the six animals in the order of the verse.",
              ["गज", "अज", "महिष", "वाजि", "वायस", "सूकर"],
              "The second line runs: elephants, goats, buffaloes, horses, crows, pigs.",
              "गज · अज · महिष · वाजि · वायस · सूकर.",
              role="apply"),
        mcq("transfer", 5,
            "What does the invented word मृगसिंहव्याघ्राः mean, with one plural ending at the end, like गजाज…सूकराः?",
            ("Deer, lions and tigers",
             "In a dvandva list, the members are joined without 'and' and one ending closes them."),
            [("Deer like lions and tigers", "A dvandva joins separate kinds; it does not say 'like'."),
             ("The tiger of the lion's deer", "No link of 'of' joins the members."),
             ("One animal with three names", "The members are different kinds, not names of one.")],
            "गजाजमहिषवाजिवायससूकराः is a list of six kinds joined into one word; the new word lists three.",
            "Dvandva = members joined with 'and'; the ending sits on the last.",
            teaches="In a dvandva list the members are joined with no 'and' and the shared plural ending sits on the last word (गजाजमहिषवाजिवायससूकराः)."),
    ],
}

# ---------------------------------------------------------------- unit 25
AUTHORED["25"] = {
    "title": "हिमानीपटलच्छन्ना",
    "question": "What does the verse say of rivers and well waters at the coming of cold?",
    "rule": ("At the coming of the cold, the rivers, covered with sheets of "
             "snow, with fish and birds hidden away, are steaming and warm, "
             "and so are the waters of wells."),
    "limits": ("The first-line adjectives are read with 'rivers'; whether they "
               "also describe the well waters is not clear. 'līna' is read as "
               "hidden, but 'clinging' is also possible, so no question rests "
               "on it."),
    "explain_hi": ("यह श्लोक हिम के आने पर नदियों और कुओं के जल का वर्णन करता है। नदियाँ हिम की "
                   "परतों से ढकी हैं और उनमें मछलियाँ और पक्षी छिपे रहते हैं; वे भाप वाली और "
                   "उष्ण हैं, और कुओं का जल भी। पहली पंक्ति के विशेषण नदियों के साथ पढ़े गए हैं; "
                   "कुओं के साथ भी हैं या नहीं, यह साफ़ नहीं है। ‘सबाष्पाः’ और ‘सोष्माणः’ में "
                   "‘स-’ का अर्थ ‘वाला’ है।"),
    "hook": "हिम के आने पर नदियाँ भाप और ऊष्मा वाली, कुओं का जल भी।",
    "core": False,
    "questions": [
        mcq("pretest", 0,
            "At the coming of the cold, what is said of the rivers?",
            ("They are steaming and warm",
             "नद्यः सबाष्पाः सोष्माणः: the rivers have vapour and warmth."),
            [("They have dried up", "Nothing in the verse says the rivers dry up."),
             ("They are in flood", "Nothing in the verse speaks of flood."),
             ("They run cold and clear", "The verse says warm and steaming.")],
            "The second line says the rivers are with vapour and with warmth.",
            "हिमागमे नद्यः: steaming and warm."),
        match(1, "Match each word of the verse to its meaning.",
              [["मीन", "fish"], ["विहंगम", "bird"], ["नद्यः", "rivers"],
               ["कूप", "well"], ["आपः", "waters"]],
              "These five words name what the verse describes.",
              "मीन = fish; विहंगम = bird; नद्यः = rivers; कूप = well; आपः = waters."),
        fill(2, "The word for 'rivers' is ____ (type it in Devanagari or in English letters, e.g. dharma).",
             accepts("नद्यः"),
             "नद्यः is the plural of नदी, river.",
             "नदी (river) has the plural नद्यः, the subject of the second line.",
             "नद्यः = rivers."),
        mcq("discriminate", 3, "Which is the right split of कूपापश्च?",
            ("कूप + आपः + च",
             "अ + आ joins as आ, and a visarga before च turns into श्."),
            [("कूप + आप + श्च", "श्च is not a word; the श् comes from a visarga."),
             ("कूप + आपः + श्च", "श्च is not a word; the word is च."),
             ("कूपः + आपः + च", "That would be written कूप आपश्च, with the visarga lost.")],
            "कूप (well) + आपः (waters) + च (and).",
            "अ + आ → आ; visarga + च → श्च."),
        order(4, "Put these phrases of the verse in the order of the verse.",
              ["हिमानीपटलच्छन्नाः", "लीनमीनविहंगमाः", "नद्यः",
               "सबाष्पाः सोष्माणः", "कूपापश्च", "हिमागमे"],
              "The verse gives the two descriptions, then the rivers, steaming and warm, then the well waters and the time.",
              "हिमानीपटलच्छन्नाः · लीनमीनविहंगमाः · नद्यः · सबाष्पाः सोष्माणः · कूपापश्च · हिमागमे.",
              role="apply"),
        mcq("transfer", 5,
            "What does the invented word सजलाः mean, with the prefix स- as in सबाष्पाः?",
            ("Having water",
             "स- at the start of such a word means with, having."),
            [("Without water", "स- gives 'with'; 'without' would be निर्- or अ-."),
             ("Born of water", "'Born of' would end in -ज."),
             ("Like water", "'Like' would end in -वत् or -सम.")],
            "सबाष्पाः = with vapour; सजलाः = with water.",
            "स- + noun = with that noun.",
            teaches="स- at the start of a compound means 'with, having' what the next word names (सबाष्पाः 'with vapour', सोष्माणः 'with warmth')."),
    ],
}

# ---------------------------------------------------------------- unit 26
AUTHORED["26"] = {
    "title": "देहोष्माणो विशंतोंऽतः",
    "question": "What do the body's heats do in the cold, and what happens to the belly's fire?",
    "rule": ("In the cold, struck by the cold wind, the heats of the body enter "
             "inside, and in the belly they make the fire, its heat massed "
             "together, strong."),
    "limits": ("The verse says only this about the fire of the belly; it gives "
               "no advice. 'piṇḍita-ūṣmāṇam' is read as describing the fire. "
               "The print has an extra anusvāra in 'viśantoṃ'taḥ' (viśanto'ntaḥ)."),
    "explain_hi": ("श्लोक शीत में शरीर की ऊष्मा का वर्णन करता है। ठंडी वायु से आहत होकर शरीर "
                   "की ऊष्माएँ भीतर प्रवेश करती हैं, और पेट में अग्नि को, जिसकी ऊष्मा एकत्र हो "
                   "गई है, प्रबल कर देती हैं। ‘पिंडितोष्माणम्’ को ‘अनलम्’ का विशेषण पढ़ा गया है। "
                   "छपे ‘विशंतोंऽतः’ में एक अतिरिक्त अनुस्वार है (विशन्तोऽन्तः)। श्लोक "
                   "इसके आगे कुछ नहीं कहता।"),
    "hook": "शीतल वायु से ऊष्माएँ भीतर जातीं, पेट की अग्नि प्रबल होती।",
    "core": True,
    "questions": [
        mcq("pretest", 0,
            "In the cold, struck by cold wind, what do the heats of the body do?",
            ("They enter inside (विशन्तः अन्तः)",
             "देहोष्माणः विशन्तः अन्तः: the heats of the body enter inside."),
            [("They leave the body", "The verse says inside, not out."),
             ("They turn cold and sink", "Nothing of the kind is in the verse."),
             ("They stay on the skin", "The verse says they go inside.")],
            "The first line says the heats of the body enter inside.",
            "शीत + ठंडी वायु → देह की ऊष्माएँ भीतर."),
        match(1, "Match each word of the verse to its meaning.",
              [["देहोष्माणः", "heats of the body"], ["विशन्तः", "entering"],
               ["जठरे", "in the belly"], ["अनलम्", "fire"],
               ["प्रबलम्", "strong"]],
              "These five words carry the sequence of the verse.",
              "देहोष्माणः = heats of the body; विशन्तः = entering; जठरे = in the belly; अनलम् = fire; प्रबलम् = strong."),
        fill(2, "The word for 'fire' (accusative) in the second line is ____ (type it in Devanagari or in English letters, e.g. dharma).",
             accepts("अनलम्", "ऽनलम्"),
             "अनलम् is the fire made strong, the object of कुर्वते.",
             "अनल is a word for fire; in the print the अ is the avagraha after कुर्वते.",
             "अनलम् = fire."),
        mcq("discriminate", 3, "Which is the right split of पिंडितोष्माणं?",
            ("पिण्डित + ऊष्माणम्",
             "अ + ऊ joins as ओ: पिण्डित + ऊष्माणम् = पिण्डितोष्माणम्."),
            [("पिण्डित + ओष्माणम्", "That would join as पिण्डितौष्माणम्, with औ."),
             ("पिण्डितः + ऊष्माणम्", "That would be written पिण्डित ऊष्माणम्."),
             ("पिण्डित + ष्माणम्", "The ऊ would be lost, and the word is ऊष्माण.")],
            "पिण्डित (massed) + ऊष्माणम् (heat): with heat massed together.",
            "अ + ऊ → ओ."),
        order(4, "Put these phrases of the verse in the order of the verse.",
              ["देहोष्माणः", "विशंतः", "शीते शीतानिलाहताः", "जठरे",
               "पिंडितोष्माणं प्रबलं", "कुर्वते अनलम्"],
              "The verse goes from the heats of the body, entering, struck by cold wind, to the belly and the fire made strong.",
              "देहोष्माणः · विशंतः · शीते शीतानिलाहताः · जठरे · पिंडितोष्माणं प्रबलं · कुर्वते अनलम्.",
              role="apply"),
        mcq("transfer", 5,
            "Built like अनलं प्रबलं कुर्वते, which invented line means 'they make the water cool'?",
            ("जलं शीतलं कुर्वन्ति",
             "'Make X Y': both X and Y stand in the accusative, then the verb."),
            [("जलस्य शीतलं कुर्वन्ति", "जलस्य is 'of the water', not the thing made."),
             ("जलं शीतलेन कुर्वन्ति", "शीतलेन is 'by the cool one', not the result."),
             ("जले शीतलं कुर्वन्ति", "जले is 'in the water', not the thing made.")],
            "अनलम् and प्रबलम् both stand in the accusative with कुर्वते: make the fire strong.",
            "Make X Y: X and Y in the accusative + the verb of making.",
            teaches="With 'make' (कृ), the thing made and what it becomes both stand in the accusative: अनलं प्रबलं कुर्वते, 'they make the fire strong'."),
    ],
}

# ---------------------------------------------------------------- unit 27
AUTHORED["27"] = {
    "title": "विसर्गे बलिनां प्रायः",
    "question": "What is clear in this unit: the period, the people, and what is applied?",
    "rule": ("Line 1 speaks of the strong in visarga; line 2 says one should "
             "apply nourishing (bṛṃhaṇa) foods and drinks for the right use of "
             "that. Little more can be relied on."),
    "limits": ("Low confidence. The subject of 'kṣamam' is not stated, and line 1 "
               "is uncertain in the print: 'svabhāvādiguru' is read by the "
               "editors as 'svabhāvād atiguru' or 'svabhāvād guru'. What 'tasya' "
               "refers to is not clear. No question rests on those points."),
    "explain_hi": ("इस इकाई का आधार कमज़ोर है, इसलिए यहाँ केवल साफ़ बातें रखी गई हैं। पहली पंक्ति "
                   "‘विसर्ग में बलवानों के लिए प्रायः …’ कहती है; ‘स्वभावादिगुरु’ छपाई में संदिग्ध है "
                   "और ‘क्षमम्’ का कर्ता नहीं बताया गया। दूसरी पंक्ति कहती है कि ‘बृंहण’ (पोषक) "
                   "अन्न और पान का प्रयोग करे। ‘तस्य’ किसके लिए है, यह श्लोक में स्पष्ट नहीं है, "
                   "इसलिए उस पर कोई प्रश्न नहीं बना।"),
    "hook": "विसर्ग में बलवानों के लिए … ; बृंहण अन्न-पान का प्रयोग करे (पाठ अधूरा)।",
    "core": False,
    "questions": [
        mcq("pretest", 0,
            "Line 1 of this unit speaks of the strong in which period?",
            ("visarga", "विसर्गे बलिनाम्: in visarga, of the strong."),
            [("ādāna", "Ādāna is not named in this unit."),
             ("both ādāna and visarga", "Only visarga is named here."),
             ("no period is named", "विसर्गे names the period.")],
            "The first word of the unit, विसर्गे, names the period.",
            "विसर्गे बलिनाम् = in visarga, of the strong."),
        match(1, "Match each word of line 1 to its meaning.",
              [["विसर्गे", "in visarga"], ["बलिनाम्", "of the strong"],
               ["प्रायः", "generally"], ["क्षमम्", "capable, able to bear"]],
              "These four words are the clear ones in the first line.",
              "विसर्गे = in visarga; बलिनाम् = of the strong; प्रायः = generally; क्षमम् = capable."),
        fill(2, "The word for 'generally' is ____ (type it in Devanagari or in English letters, e.g. dharma).",
             accepts("प्रायः"),
             "प्रायः means generally, for the most part.",
             "प्रायः is a small word that softens a claim: generally, mostly.",
             "प्रायः = generally."),
        mcq("discriminate", 3, "Which is the right split of बृंहणान्यन्नपानानि?",
            ("बृंहणानि + अन्नपानानि",
             "इ before a different vowel becomes य्: णि + अ gives ण्य."),
            [("बृंहणाने + अन्नपानानि", "ए + अ would give ए with an avagraha, not ण्य."),
             ("बृंहणान्य + अन्नपानानि", "A word ending in -य does not join as -ण्य + अ."),
             ("बृंहण + न्यन्नपानानि", "न्यन्नपानानि is not a word.")],
            "बृंहणानि (nourishing) + अन्नपानानि (foods and drinks), both neuter plural.",
            "इ + a different vowel → य् + that vowel."),
        order(4, "Put the parts of line 2 in the order of the verse.",
              ["बृंहणानि", "अन्नपानानि", "योजयेत्", "तस्य युक्तये"],
              "The line runs: nourishing, foods and drinks, one should apply, for the right use of that.",
              "बृंहणानि · अन्नपानानि · योजयेत् · तस्य युक्तये.",
              role="apply"),
        mcq("transfer", 5,
            "Built like योजयेत्, 'one should apply', which invented form means 'one should go'?",
            ("गच्छेत्", "The ending -एत् marks 'one should' or 'may'."),
            [("गच्छति", "This is the plain present: he goes."),
             ("अगच्छत्", "This is a past form: he went."),
             ("गमिष्यति", "This is a future form: he will go.")],
            "योजयेत् ends in -एत्, the 'should' form; गच्छेत् ends the same way.",
            "-एत् = 'one should / may'.",
            teaches="The ending -एत् on a verb (योजयेत्, गच्छेत्) says 'one should' or 'may', for one person."),
    ],
}

NOTES_HI = {
    "14": "विश्वास: उच्च। छपा ‘तैमार्गशीर्ष…’ में शायद ‘र्’ छूटा है (तैः + मार्ग → तैर्मार्ग…, पाठ-झंडा); अर्थ वही रहता है। ‘हेमंतशिशिर’ और ‘वसंतग्रीष्मवर्षाशरदाख्याः’ एक ही समास है जो छपाई के अंतराल से टूटा दिखता है। संधि जाँची: षडृतवो भवंति = षट् + ऋतवः + भवंति (ट् → ड् स्वर से पहले; ऋतवः का विसर्ग घोष भ से पहले ओ)। केवल पहले महीने (मार्गशीर्ष) का नाम दिया है।",
    "15": "विश्वास: उच्च। ‘रवेः’ दोनों गतियों के साथ पढ़ा गया है। ‘आदान’ और ‘विसर्ग’ शब्द के रूप में रखे गए हैं (लेना और छोड़ना)। संधि जाँची: शिशिरादयस्त्रयो = शिशिर + आदयः + त्रयः (अ + आ → आ; आदयः + त्र → स्त्र; त्रयः + र → त्रयो र); रवेरुदगयनम् = रवेः + उदगयनम् (ए के बाद विसर्ग स्वर से पहले र्); शेषा = शेषाः (घोष द से पहले विसर्ग छूटा, वर्तनी-टिप्पणी देखें)। कोई पाठभेद नहीं।",
    "16": "विश्वास: उच्च। छपा ‘वर्ष’ में अंत का म् छूटा लगता है (वर्षम्, पाठ-झंडा)। संधि जाँची: तावादानविसर्गौ = तौ + आदानविसर्गौ (औ + आ → आव् + आ); आदानविसर्गौ द्विवचन का द्वन्द्व है। दोनों का मिलकर वर्ष होना ही कहा गया है।",
    "17": "विश्वास: उच्च। ‘आग्नेयम्’ अग्नि से बना विशेषण है (अग्नि-संबंधी); कारण इस वाक्य में नहीं दिया। संधि जाँची: तयोरादानमाग्नेयम् = तयोः + आदानम् + आग्नेयम् (ओ के बाद विसर्ग स्वर से पहले र्)। कोई पाठभेद नहीं।",
    "18": "विश्वास: मध्यम। एक ही वाक्य में दो कर्ता (अर्क और वायवः) और बहुवचन कृदंत हैं। ‘कालस्वभावमार्गपरिगृहीतः’ दो तरह पढ़ा जा सकता है (काल के स्वभाव और मार्ग से ग्रहण किया हुआ); शाब्दिक अर्थ रखा गया है, उस पर प्रश्न नहीं। ‘सोमजं गुणम्’ = सोम (चंद्र) से उत्पन्न गुण, जैसा पाठ कहता है। ‘तस्मिन्’ = आदान (इकाई १७)। संधि जाँची: अत्यर्थोष्ण = अत्यर्थ + उष्ण (अ + उ → ओ); ऋतुक्रमेणोपजनित = ऋतुक्रमेण + उपजनित (अ + उ → ओ); रसांस्तिक्त = रसान् + तिक्त; तत्संपर्काद्वायवः = तत्संपर्कात् + वायवः (त् → द्)। पाठ-झंडे नहीं।",
    "19": "विश्वास: उच्च। ‘सौम्य’ का अर्थ सौम्य और ‘सोम का’ दोनों हो सकता है (डेटा में दोनों रखे हैं)। संधि जाँची: विसर्गस्तु = विसर्गः + तु (विसर्ग त से पहले स्)। यह वाक्य इकाई १७ (आदान आग्नेय) के सामने रखा गया है। कोई पाठभेद नहीं।",
    "20": "विश्वास: उच्च। ‘तस्मिन्’ = विसर्ग (इकाई १९)। लंबा सप्तमी-समूह (सूर्य, चंद्र, जगत्) है और उसके बाद मुख्य वाक्य। ‘माहेंद्रसलिल’ = महेन्द्र का जल, शाब्दिक। ‘यथाक्रमम्’ रसों और बल दोनों के साथ लिया गया। ‘इति’ अंत में है। छपा ‘आप्यायमानेमाहेंद्र…’ जुड़ा हुआ छपा है (ए + म, संधि नहीं)। संधि जाँची: चाव्याहतबले = च + अव्याहत (अ + अ → आ); जगत्यरूक्षा = जगति + अरूक्षाः (इ + अ → य; अरूक्षा = अरूक्षाः, घोष र से पहले विसर्ग छूटा); प्रवर्द्धंतेऽम्ल = प्रवर्धंते + अम्ल; चोपचीयते = च + उपचीयते (अ + उ → ओ)।",
    "21": "विश्वास: उच्च। यह परंपरागत परिचय-वाक्य है, जो आगे के श्लोकों (इकाई २२ से) से पहले आता है। संधि जाँची: चात्र = च + अत्र (अ + अ → आ)। कोई पाठभेद नहीं।",
    "22": "विश्वास: मध्यम। छपा ‘चाप्यं’ (= च + आप्यम्, ‘और जल-संबंधी’) का सुझाव ‘चाग्र्यं’ (च + अग्र्यम्, ‘और श्रेष्ठ’) है, क्योंकि श्रेष्ठ / मध्य / हीन का क्रम बनता है; यह संभव है, निश्चित नहीं (पाठ-झंडा और संपादकों की टिप्पणी)। इसलिए हेमन्त-शिशिर के दर्जे पर कोई प्रश्न नहीं बना। निदाघ = ग्रीष्म। क्रिया नहीं है; ‘बलम्’ दूसरी पंक्ति में भी समझा जाता है। संधि जाँची: शरद्वसंतयोः = शरत् + वसंतयोः (त् → द् घोष व से पहले); विसर्गादानयोः = विसर्ग + आदानयोः।",
    "23": "विश्वास: मध्यम। ‘दिगादित्याः’ = दिक् + आदित्याः (क् → ग् स्वर से पहले) पढ़ा गया है, पर बहुवचन ‘आदित्याः’ अटपटा है और संपादकों ने अनुवाद को ढीला कहा है, इसलिए उस पर कोई प्रश्न नहीं। ‘उत्तरः’ दिशा या वायु हो सकता है; ‘उत्तर’ रखा गया। श्लोक ऋतु का नाम नहीं देता। संधि जाँची: रजोमंदाः = रजः + मंदाः (विसर्ग → ओ घोष म से पहले); मरुच्छैत्यात् = मरुत् + शैत्यात् (त् + श → च्छ); शैत्यादुत्तरो = शैत्यात् + उत्तरः (त् → द्); उत्तरो रोमहर्षणः = उत्तरः + रोमहर्षणः।",
    "24": "विश्वास: मध्यम। पौधों के नाम केवल नाम हैं, पहचान नहीं की गई। छपा ‘रोध’ संभवतः ‘रोध्र’ है (लोध्र; पाठ-झंडा); इसलिए वर्तनी पर कोई प्रश्न नहीं। श्लोक में ऋतु या ‘वन’ शब्द नहीं है। ‘दृप्त’ = मदमस्त, उत्साही (गर्वित)। संधि जाँची: कुसुमोज्ज्वलाः = कुसुम + उज्ज्वलाः (अ + उ → ओ); दृप्ता = दृप्ताः (घोष ग से पहले विसर्ग छूटा, वर्तनी-टिप्पणी देखें); लवल्यः = लवली का बहुवचन।",
    "25": "विश्वास: मध्यम। पहली पंक्ति के विशेषण ‘नद्यः’ (पंक्ति २) के साथ पढ़े गए हैं; कुओं के जल के साथ भी हैं या नहीं, साफ़ नहीं। ‘लीन’ को ‘छिपा हुआ’ पढ़ा गया है (‘चिपका हुआ’ भी संभव), इसलिए उस पर प्रश्न नहीं। ‘हिमानी’ = हिम/पाले का ढेर। ‘हिमागमे’ = हिम (शीत) के आने पर। संधि जाँची: कूपापश्च = कूप + आपः + च (अ + आ → आ; विसर्ग + च → श्च); सोष्माणः = स + ऊष्माणः (अ + ऊ → ओ); ‘हिमानीपटलच्छन्नाः’ में पटल + छन्न → च्छ (स्वर के बाद छ का द्वित्व)।",
    "26": "विश्वास: मध्यम। छपा ‘विशंतोंऽतः’ में ‘तो’ के बाद अतिरिक्त अनुस्वार है (विशन्तः + अन्तः → विशन्तोऽन्तः; पाठ-झंडा)। ‘पिण्डित-ऊष्माणम्’ को ‘अनलम्’ का विशेषण पढ़ा गया है। ‘शीते’ = शीत ऋतु में (सप्तमी)। ‘कुर्वते’ आत्मनेपद, ‘ऽनलम्’ का अवग्रह अलग टुकड़े में छपा है। संधि जाँची: देहोष्माणः = देह + ऊष्माणः (अ + ऊ → ओ); पिंडितोष्माणं = पिण्डित + ऊष्माणम्; कुर्वतेऽनलम् = कुर्वते + अनलम्।",
    "27": "विश्वास: कम। पहली पंक्ति का ‘स्वभावादिगुरु’ संदिग्ध है (संपादकों का सुझाव ‘स्वभावादतिगुरु’; दूसरा विकल्प ‘स्वभावाद्गुरु’, जिसमें मात्राएँ १६ रहती हैं)। ‘क्षमम्’ नपुंसक है पर उसका कर्ता नहीं बताया; डेटा उसे पिछली इकाई का ‘अनल’ मानता है, यह केवल अनुमान है। ‘तस्य’ भी इसी पर टिका है। पुस्तक का हिन्दी ‘संतुष्ट करने के लिए’ जैसा पढ़ता है, पर ‘युक्तये’ का शाब्दिक अर्थ ‘उचित प्रयोग के लिए’ है। इसलिए कोई प्रश्न पहली पंक्ति के संदिग्ध अंश या ‘तस्य’ पर नहीं बना। संधि जाँची: बृंहणान्यन्नपानानि = बृंहणानि + अन्नपानानि (इ + अ → य)।",
}

AIDS = {
    "14": {
        "chain": {"steps": ["हेमन्त", "शिशिर", "वसन्त", "ग्रीष्म", "वर्षा", "शरद"]},
        "chunks": "तैर्मार्गशीर्षादिभिर्द्विसंख्यैः | क्रमाद्धेमंतशिशिरवसंतग्रीष्मवर्षाशरदाख्याः | षडृतवो भवंति।",
        "sandhi": "षट् + ऋतवः → षडृतवः (ट् → ड् स्वर से पहले)। ऋतवः + भवंति → ऋतवो भवंति (विसर्ग → ओ, घोष से पहले)।",
        "anchors": "ऋतु = मौसम · मार्गशीर्ष = पहला मास · द्विसंख्य = दो की संख्या वाला · क्रमात् = क्रम से · आख्या = नाम।",
    },
    "15": {
        "diagram": {"groups": [
            {"label": "शिशिर आदि तीन (रवि की गति)", "items": ["उदगयन (उत्तरायण)", "आदान"]},
            {"label": "शेष तीन", "items": ["दक्षिणायन", "विसर्ग"]}]},
        "chunks": "तेषु शिशिरादयस्त्रयो | रवेरुदगयनमादानं च ‖ शेषा दक्षिणायनं | विसर्गश्च।",
        "sandhi": "ए के बाद विसर्ग, स्वर से पहले → र्: रवेः + उदगयनम् → रवेरुदगयनम्। अ + आ → आ: शिशिर + आदयः → शिशिरादयः।",
        "contrast": "शिशिर से तीन: उत्तरायण · आदान ↔ शेष तीन: दक्षिणायन · विसर्ग।",
    },
    "16": {
        "chunks": "तावादानविसर्गौ | वर्ष(म्)।",
        "sandhi": "औ + आ → आव् + आ: तौ + आदानविसर्गौ → तावादानविसर्गौ।",
        "anchors": "तौ = वे दोनों · आदान = लेना · विसर्ग = छोड़ना, देना · वर्ष = साल।",
    },
    "17": {
        "chunks": "तयोरादानमाग्नेयं।",
        "sandhi": "ओ के बाद विसर्ग, स्वर से पहले → र्: तयोः + आदानम् → तयोरादानम्।",
        "anchors": "आग्नेय = अग्नि-संबंधी · तयोः = उन दोनों में · आदान (नपुंसक) → आग्नेय (नपुंसक)।",
    },
    "18": {
        "diagram": {"groups": [
            {"label": "कर्ता", "items": ["अर्क (सूर्य)", "वायवः (तीव्र, रूखी)"]},
            {"label": "करते हैं", "items": ["सोमज गुण सुखाना", "जगत् का स्नेह लेना", "तिक्त-कषाय-कटु प्रबल करना"]},
            {"label": "फल", "items": ["नरों में दौर्बल्य"]}]},
        "chunks": "तस्मिन् खलु … अर्कस्तत्संपर्काद्वायवश्च तीव्ररूक्षाः | सोमजं गुणमुपशोषयंतो | जगतः स्नेहमाददानाः | … रसांस्तिक्तकषायकटुकानभिप्रबलयंतो | नृणां दौर्बल्यमावहंति।",
        "sandhi": "अ + उ → ओ: अत्यर्थ + उष्ण → अत्यर्थोष्ण। न् + त → ंस्त: रसान् + तिक्त → रसांस्तिक्त।",
        "anchors": "अर्क = सूर्य · रूक्ष = रूखा · स्नेह = चिकनाई, नमी · तिक्त = कड़वा · कषाय = कसैला · कटु = तीखा · दौर्बल्य = कमज़ोरी।",
    },
    "19": {
        "chunks": "विसर्गस्तु | सौम्यः।",
        "sandhi": "विसर्ग + त → स्त: विसर्गः + तु → विसर्गस्तु।",
        "contrast": "आदान आग्नेय (इकाई १७) ↔ विसर्ग तो सौम्य। ‘तु’ दोनों को आमने-सामने रखता है।",
    },
    "20": {
        "diagram": {"groups": [
            {"label": "स्थितियाँ", "items": ["सूर्य दक्षिणायन में, प्रभाव दबा", "चंद्र का बल अबाधित", "जगत् शीतल किरणों से तृप्त"]},
            {"label": "तब", "items": ["अम्ल, लवण, मधुर बढ़ते", "नरों का बल संचित"]}]},
        "chunks": "तस्मिन्नपि … दक्षिणायनगेऽर्के | शशिनि चाव्याहतबले | शिशिराभिर्भाभिः शश्वदाप्यायमाने … जगत्यरूक्षा रसाः प्रवर्द्धंते | अम्ललवणमधुरा यथाक्रमं | बलं चोपचीयते नृणामिति।",
        "sandhi": "अ + उ → ओ: च + उपचीयते → चोपचीयते। अ + अ → आ: च + अव्याहत → चाव्याहत।",
        "contrast": "आदान (इकाई १८): रूखे रस तिक्त-कषाय-कटु बढ़ते, दौर्बल्य ↔ विसर्ग: अरूखे रस अम्ल-लवण-मधुर बढ़ते, बल संचित।",
    },
    "21": {
        "chunks": "भवति चात्र।",
        "sandhi": "अ + अ → आ: च + अत्र → चात्र।",
        "frame": "‘और इस विषय में यह है’: आगे श्लोक आते हैं (इकाई २२ से)।",
    },
    "22": {
        "diagram": {"groups": [
            {"label": "हेमन्त, शिशिर", "items": ["पाठ संदिग्ध (श्रेष्ठ?)"]},
            {"label": "शरद, वसन्त", "items": ["मध्यम"]},
            {"label": "वर्षा, निदाघ", "items": ["हीन"]}]},
        "chunks": "हेमंते शिशिरे चाप्यं | विसर्गादानयोर्बलं ‖ शरद्वसंतयोर्मध्यं | हीनं वर्षा निदाघयोः।",
        "anchors": "बल = ताक़त · मध्य = बीच का · हीन = कम · निदाघ = गर्मी का मौसम (ग्रीष्म)।",
    },
    "23": {
        "chunks": "धूमधूम्रा रजोमंदा- | स्तुषाराविलमंडलाः ‖ दिगादित्या मरुच्छैत्या- | दुत्तरो रोमहर्षणः।",
        "sandhi": "त् + श → च्छ: मरुत् + शैत्यात् → मरुच्छैत्यात्। विसर्ग → ओ घोष से पहले: रजः + मंदाः → रजोमंदाः।",
        "anchors": "धूम = धुआँ · धूम्र = धूसर · रजस् = धूल · तुषार = पाला · रोमहर्षण = रोंगटे खड़े करने वाला।",
    },
    "24": {
        "diagram": {"groups": [
            {"label": "फूलों से दीप्त", "items": ["रोध", "प्रियंगु", "पुन्नाग", "लवली"]},
            {"label": "दृप्त (मदमस्त)", "items": ["गज", "अज", "महिष", "वाजि", "वायस", "सूकर"]}]},
        "chunks": "रोधप्रियंगुपुन्नागलवल्यः | कुसुमोज्ज्वलाः ‖ दृप्ता | गजाजमहिषवाजिवायससूकराः।",
        "sandhi": "अ + उ → ओ: कुसुम + उज्ज्वलाः → कुसुमोज्ज्वलाः। अ + अ → आ: गज + अज → गजाज।",
        "anchors": "कुसुम = फूल · उज्ज्वल = चमकता · दृप्त = मदमस्त · गज = हाथी · अज = बकरा · महिष = भैंसा · वाजि = घोड़ा · वायस = कौआ · सूकर = सूअर।",
    },
    "25": {
        "chunks": "हिमानीपटलच्छन्ना | लीनमीनविहंगमाः ‖ नद्यः सबाष्पाः सोष्माणः | कूपापश्च हिमागमे।",
        "sandhi": "अ + आ → आ; विसर्ग + च → श्च: कूप + आपः + च → कूपापश्च। अ + ऊ → ओ: स + ऊष्माणः → सोष्माणः।",
        "anchors": "हिमानी = पाले/हिम का ढेर · पटल = परत · मीन = मछली · विहंगम = पक्षी · बाष्प = भाप · ऊष्मा = गर्मी · सबाष्प = भाप वाला।",
        "frame": "कब: हिम के आने पर · क्या: नदियाँ भाप-ऊष्मा वाली, कुओं का जल भी · ढकी हिम की परतों से, मछली-पक्षी छिपे (नदियों के लिए)।",
    },
    "26": {
        "chain": {"steps": ["शीत में ठंडी वायु का आघात", "देह की ऊष्माएँ भीतर प्रवेश करती हैं", "पेट में अग्नि प्रबल हो जाती है"]},
        "chunks": "देहोष्माणो विशंतोऽंतः | शीतेशीतानिलाहताः ‖ जठरे पिंडितोष्माणं | प्रबलं कुर्वतेऽनलं।",
        "sandhi": "अ + ऊ → ओ: देह + ऊष्माणः → देहोष्माणः। विसर्ग + अ → ओऽ: विशन्तः + अन्तः → विशन्तोऽन्तः।",
        "anchors": "ऊष्मा = गर्मी · जठर = पेट · पिंडित = इकट्ठा · प्रबल = मजबूत · अनल = अग्नि।",
    },
    "27": {
        "chunks": "विसर्गे बलिनां प्रायः | स्वभावादिगुरु (अनिश्चित) क्षमं ‖ बृंहणान्यन्नपानानि | योजयेत्तस्य युक्तये।",
        "sandhi": "इ + भिन्न स्वर → य्: बृंहणानि + अन्नपानानि → बृंहणान्यन्नपानानि।",
        "anchors": "बलिन् = बलवान् · प्रायः = आमतौर पर · क्षम = समर्थ · बृंहण = पोषक · योजयेत् = प्रयोग करे · युक्ति = उचित प्रयोग।",
    },
}

IMAGE_SPECS = {
    ("14", "chain"): {
        "file": "ch4b02-seasons-14.svg",
        "alt": "Chain of the six seasons in the order of the sentence: Hemanta, Śiśira, Vasanta, Grīṣma, Varṣā, Śarad",
        "type": "chain",
        "title": "वाक्य १४: छह ऋतुएँ क्रम से",
        "steps": ["हेमन्त", "शिशिर", "वसन्त", "ग्रीष्म", "वर्षा", "शरद"],
    },
    ("15", "diagram"): {
        "file": "ch4b02-courses-15.svg",
        "alt": "Two columns: the three seasons beginning with Śiśira are the northward course and ādāna; the remaining three are the southward course and visarga",
        "type": "split",
        "title": "वाक्य १५: दो गतियाँ, दो अवस्थाएँ",
        "cols": [["शिशिर आदि तीन", ["उदगयन (उत्तरायण)", "आदान"]],
                 ["शेष तीन", ["दक्षिणायन", "विसर्ग"]]],
    },
    ("18", "diagram"): {
        "file": "ch4b02-adana-18.svg",
        "alt": "Flowchart: the sun and the winds dry up the quality born of Soma, take the world's moisture and strengthen the bitter, astringent and pungent tastes; the result is weakness in men",
        "type": "mermaid",
        "code": ('flowchart TD\n'
                 '  A["अर्क और<br/>तीव्र रूखी वायुएँ"] --> B["सोमज गुण को सुखाना"]\n'
                 '  A --> C["जगत् का स्नेह लेना"]\n'
                 '  A --> D["तिक्त, कषाय, कटु<br/>अत्यंत प्रबल"]\n'
                 '  B --> E["नरों में दौर्बल्य"]\n'
                 '  C --> E\n'
                 '  D --> E\n'),
    },
    ("20", "diagram"): {
        "file": "ch4b02-visarga-20.svg",
        "alt": "Flowchart: sun in the southern course with its power struck down, moon unimpeded, world refreshed by cool rays; then sour, salty and sweet tastes increase and men's strength is built up",
        "type": "mermaid",
        "code": ('flowchart TD\n'
                 '  A["सूर्य दक्षिणायन में,<br/>प्रभाव दबा"] --> D["अम्ल, लवण, मधुर<br/>क्रम से बढ़ते"]\n'
                 '  B["चंद्र का बल अबाधित"] --> D\n'
                 '  C["जगत् शीतल किरणों<br/>से तृप्त"] --> D\n'
                 '  D --> E["नरों का बल संचित"]\n'),
    },
    ("22", "diagram"): {
        "file": "ch4b02-strength-22.svg",
        "alt": "Table: Hemanta and Śiśira, grade uncertain in the print; Śarad and Vasanta, middling; Varṣā and Nidāgha, low",
        "type": "table",
        "title": "श्लोक २२: ऋतु-जोड़ी और बल",
        "heads": ["ऋतुएँ", "विसर्ग-आदान का बल"],
        "rows": [["हेमन्त, शिशिर", "पाठ संदिग्ध"],
                 ["शरद, वसन्त", "मध्यम"],
                 ["वर्षा, निदाघ", "हीन"]],
    },
    ("24", "diagram"): {
        "file": "ch4b02-plants-animals-24.svg",
        "alt": "Two columns: four plants bright with blossoms (rodha, priyangu, punnaga, lavali) and six spirited animals (elephants, goats, buffaloes, horses, crows, pigs)",
        "type": "split",
        "title": "श्लोक २४: फूल और दृप्त प्राणी",
        "cols": [["फूलों से दीप्त", ["रोध", "प्रियंगु", "पुन्नाग", "लवली"]],
                 ["दृप्त", ["गज", "अज", "महिष", "वाजि", "वायस", "सूकर"]]],
    },
    ("26", "chain"): {
        "file": "ch4b02-heat-26.svg",
        "alt": "Chain: in the cold the cold wind strikes; the heats of the body enter inside; the fire in the belly is made strong",
        "type": "chain",
        "title": "श्लोक २६: शीत में देह की ऊष्मा",
        "steps": ["शीत में ठंडी वायु का आघात", "देह की ऊष्माएँ भीतर प्रवेश", "पेट की अग्नि प्रबल"],
    },
}
