from helpers import mcq, match, order, fill, multi, accepts


def T(q, teaches):
    q["teaches"] = teaches
    return q


AUTHORED = {}

# ---------------------------------------------------------------- unit 75
AUTHORED["75"] = {
    "title": "दशांगुलंबस्तिशिरः",
    "question": "By unit 75, what measure does the text give for the basti-śiras (head of the bladder)?",
    "rule": ("The basti-śiras (बस्तिशिरः, 'head of the bladder'; basti = urinary bladder) is ten aṅgulas (दशाङ्गुलम्), "
             "counted in one's own finger-breadths (card 66)."),
    "limits": ("Prose, no verb (copula understood). Which part 'basti-śiras' means (the top of the bladder or the region "
               "above it) is not stated, nor which dimension the ten measures: no question on either."),
    "explain_hi": ("यह इकाई अंगुल-प्रमाण की सूची का एक छोटा अंश है: बस्तिशिर यानी मूत्राशय का शिर दस अंगुल का है। "
                   "बस्ति = मूत्राशय (मानक); ‘बस्तिशिर’ से ठीक कौन-सा भाग (मूत्राशय का ऊपरी भाग या उसके ऊपर का क्षेत्र) अभिप्रेत है, यह यहाँ नहीं कहा गया। "
                   "दस अंगुल लम्बाई है, चौड़ाई है या घेरा, यह भी नहीं बताया गया। "
                   "अंगुल अपनी ही अंगुलियों की चौड़ाई है (कार्ड ६६)। "
                   "‘दशांगुलं’ में दश + अङ्गुलम् (अ + अ → आ) है, और व्यंजन ब से पहले अन्तिम म् अनुस्वार लिखा गया।"),
    "hook": "दस अंगुल: बस्ति का शिर।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "In unit 75, what does बस्ति mean?",
            ("The urinary bladder", "बस्ति = urinary bladder (standard): बस्तिशिरः, head of the bladder."),
            [("The pair of kidneys", "Kidneys would be वृक्कौ; बस्ति is the bladder."),
             ("The end of the gut", "The end of the gut would be गुद; बस्ति is the bladder."),
             ("The tube of the neck", "The neck is ग्रीवा or शिरोधरा; बस्ति is the bladder.")],
            "बस्ति = urinary bladder; शिरः = head.",
            "बस्ति = urinary bladder."),
        order(1, "Put the word-parts of unit 75 in the printed order.",
              ["दश", "अङ्गुलम्", "बस्ति", "शिरः"],
              "Ten; aṅgulas; bladder; head: दशाङ्गुलं बस्तिशिरः.",
              "दश → अङ्गुलम् → बस्ति → शिरः."),
        match(2, "Match each word-part of unit 75 to its meaning.",
              [["दश", "ten"], ["अङ्गुल", "finger-breadth"], ["बस्ति", "bladder"], ["शिरस्", "head"]],
              "दश = ten, अङ्गुल = finger-breadth, बस्ति = bladder, शिरस् (printed शिरः) = head.",
              "दश, अङ्गुल, बस्ति, शिरस्.", role="extend",
              teaches=("दशाङ्गुलम् is a bahuvrīhi, 'having ten aṅgulas'; it is neuter because बस्तिशिरः (from शिरस्) "
                       "is neuter.")),
        mcq("discriminate", 3, "By unit 75, which statement is right?",
            ("The basti-śiras is ten aṅgulas", "दशाङ्गुलं बस्तिशिरः: the head of the bladder, ten aṅgulas."),
            [("The basti-śiras is twelve aṅgulas", "Twelve aṅgulas is the belly, in card 76."),
             ("The whole basti is ten aṅgulas long", "The measure is of the basti-śiras, and no length is named."),
             ("The basti holds ten measures of fluid", "The line gives a body measure, not a capacity.")],
            "Only the basti-śiras is measured, at ten aṅgulas.",
            "दशाङ्गुलम् goes with बस्तिशिरः."),
        multi("apply", 4, "Which statements fit unit 75?",
              [("The line gives the bladder's capacity", "No: it gives a measure in aṅgulas, not a capacity."),
               ("बस्ति here is the urinary bladder", "Right: basti = urinary bladder (standard)."),
               ("The word अङ्गुल is printed in this line", "Right: दशांगुलं prints it."),
               ("The ten is stated to be a length", "No: the line names no dimension.")],
              [1, 2],
              "The line prints aṅgula and names the bladder's head; it states no dimension and no capacity.",
              "दशाङ्गुलं बस्तिशिरः: ten aṅgulas, the head of the bladder."),
        mcq("transfer", 5, "By the pattern of दश + अङ्गुलम् → दशाङ्गुलम्, how is सप्त + अङ्गुलम् joined in a new example?",
            ("सप्ताङ्गुलम्", "अ + अ → आ: सप्त + अङ्गुलम् → सप्ताङ्गुलम्."),
            [("सप्तङ्गुलम्", "The two short अ merge into a long आ; they are not cut to one short अ."),
             ("सप्तेङ्गुलम्", "ए comes from अ + इ, not from अ + अ."),
             ("सप्तोङ्गुलम्", "ओ comes from अ + उ, not from अ + अ.")],
            "सप्त + अङ्गुलम् = सप्ताङ्गुलम्, like दश + अङ्गुलम् = दशाङ्गुलम्.",
            "अ + अ → आ.",
            teaches="Short अ + short अ → long आ: दश + अङ्गुलम् → दशाङ्गुलम्."),
    ],
}

# ---------------------------------------------------------------- unit 76
AUTHORED["76"] = {
    "title": "द्वादशांगुलमुदरं",
    "question": "By unit 76, how many aṅgulas is the belly (udara)?",
    "rule": "The belly (उदरम्) is twelve aṅgulas (द्वादशाङ्गुलम्).",
    "limits": ("Prose, no verb. The dimension (length, breadth or girth) is not stated: no question on it. Here udara is "
               "the belly as a body part, not the disease of that name (data's note)."),
    "explain_hi": ("उदर यानी पेट बारह अंगुल का है। "
                   "यहाँ उदर शरीर का अंग है, रोग नहीं (डेटा की टिप्पणी)। "
                   "बारह अंगुल लम्बाई है, चौड़ाई है या घेरा, यह नहीं कहा गया। "
                   "‘द्वादशांगुलमुदरं’ में द्वादश + अङ्गुलम् (अ + अ → आ) है, और फिर अङ्गुलम् + उदरम् में स्वर उ से पहले म् बना रहकर उससे जुड़ गया।"),
    "hook": "बारह अंगुल का पेट।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "In unit 76, what does द्वादश mean?",
            ("Twelve", "द्वादश = twelve (द्वा + दश, two and ten)."),
            [("Twenty", "Twenty would be विंशति."),
             ("Two", "Two would be द्वि; द्वादश is twelve."),
             ("Ten", "Ten would be दश; द्वादश is twelve.")],
            "द्वादश = twelve.",
            "द्वादश = twelve."),
        match(1, "Match each word of unit 76 to its meaning.",
              [["द्वादश", "twelve"], ["अङ्गुल", "finger-breadth"], ["उदर", "belly"]],
              "द्वादश = twelve, अङ्गुल = finger-breadth, उदर = belly.",
              "द्वादश, अङ्गुल, उदर."),
        fill(2, ("Unit 76: द्वादशाङ्गुलम् ____ (the belly is twelve aṅgulas). Type the missing word in Devanagari or in "
                 "English letters (e.g. dharma)."),
             accepts("उदरम्"),
             "उदरम् = the belly; printed joined: द्वादशांगुलमुदरं.",
             "उदरम् (belly) is the noun that द्वादशाङ्गुलम् describes; both are neuter.",
             "द्वादशाङ्गुलम् उदरम्: the belly, twelve aṅgulas."),
        mcq("discriminate", 3, "Which split of द्वादशांगुलमुदरं in unit 76 is right?",
            ("द्वादशाङ्गुलम् + उदरम्", "म् before the vowel उ stays म् and joins it: -लमुदरम्."),
            [("द्वादशाङ्गुल + मुदरम्", "मुदरम् is not a word; the म् ends द्वादशाङ्गुलम्."),
             ("द्वादशाङ्गुलमु + दरम्", "द्वादशाङ्गुलमु is not a form, and दरम् is not the noun here."),
             ("द्वादशाङ्गुलाम् + उदरम्", "That would give -लामुदरम्, with a long आ that is not printed.")],
            "द्वादशाङ्गुलम् (twelve aṅgulas) + उदरम् (belly).",
            "Final म् + vowel: म् joins the vowel."),
        multi("apply", 4, "Which statements fit unit 76?",
              [("उदर here is the belly, a body part", "Right: the data's note says it is not the disease here."),
               ("The line says the twelve is the girth", "No: the line names no dimension."),
               ("The word अङ्गुल is printed in this line", "Right: द्वादशांगुल- prints it."),
               ("The belly is eighteen aṅgulas", "No: twelve. Eighteen is the back's height (card 79).")],
              [0, 2],
              "The belly, a body part, is twelve aṅgulas; the dimension is not named.",
              "द्वादशाङ्गुलम् उदरम्."),
        mcq("transfer", 5, ("By the pattern of -अङ्गुलम् + उदरम् → -अङ्गुलमुदरम्, how is द्व्यङ्गुलम् + अन्तरम् (a gap of two "
                            "aṅgulas) joined in a new example?"),
            ("द्व्यङ्गुलमन्तरम्", "म् before the vowel अ stays म् and joins it."),
            [("द्व्यङ्गुलं अन्तरम्", "ं stands for म् only before a consonant; before a vowel म् joins the vowel."),
             ("द्व्यङ्गुलोऽन्तरम्", "ओऽ comes from अः + अ; here the word ends in म्, not in a visarga."),
             ("द्व्यङ्गुलमान्तरम्", "म् + अ does not lengthen the vowel; the अ of अन्तरम् stays short.")],
            "द्व्यङ्गुलम् + अन्तरम् = द्व्यङ्गुलमन्तरम्, like द्वादशाङ्गुलम् + उदरम्.",
            "Final म् + vowel: म् joins the vowel.",
            teaches="A final म् before a vowel is not turned into ं; it joins the vowel: -अङ्गुलम् + उदरम् → -अङ्गुलमुदरम्."),
    ],
}

# ---------------------------------------------------------------- unit 77
AUTHORED["77"] = {
    "title": "दश विस्तारे द्वादशायामे पार्श्वे",
    "question": "By unit 77, what are the breadth and the length of the two flanks (pārśva)?",
    "rule": ("The two flanks (पार्श्वे) are ten in breadth (दश विस्तारे) and twelve in length (द्वादशायामे); "
             "the unit, aṅgula, is understood."),
    "limits": ("Prose, no verb; aṅgula is not printed here (understood). विस्तारे and -आयामे may be locatives ('in breadth', "
               "'in length') or dual forms agreeing with पार्श्वे; the sense is the same, so no question rests on their case."),
    "explain_hi": ("दोनों पार्श्व यानी धड़ के पसलियों वाले दोनों बगल चौड़ाई में दस और लम्बाई में बारह हैं। "
                   "यहाँ ‘अंगुल’ छपा नहीं, समझा जाता है। "
                   "विस्तार = चौड़ाई, आयाम = लम्बाई: एक ही अंग के दो माप एक पंक्ति में। "
                   "‘विस्तारे’ और ‘-आयामे’ सप्तमी (चौड़ाई में, लम्बाई में) भी हो सकते हैं और ‘पार्श्वे’ से मेल खाते द्विवचन भी; अर्थ एक ही रहता है। "
                   "‘द्वादशायामे’ में द्वादश + आयामे (अ + आ → आ) है।"),
    "hook": "बगल: दस चौड़े, बारह लम्बे।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "In unit 77, what does विस्तार mean?",
            ("Breadth", "विस्तार = breadth: दश विस्तारे, ten in breadth."),
            [("Height", "Height is उत्सेध (card 78); विस्तार is breadth."),
             ("Girth", "Girth is परिणाह (card 74); विस्तार is breadth."),
             ("Weight", "Weight would be भार; विस्तार is breadth.")],
            "विस्तार = breadth; आयाम = length.",
            "विस्तार = breadth."),
        order(1, "Put the words of unit 77 in the printed order.",
              ["दश", "विस्तारे", "द्वादशायामे", "पार्श्वे"],
              "Ten; in breadth; twelve in length; the two flanks.",
              "दश → विस्तारे → द्वादशायामे → पार्श्वे."),
        match(2, "Match each word of unit 77 to its meaning.",
              [["दश", "ten"], ["विस्तार", "breadth"], ["द्वादश", "twelve"], ["आयाम", "length"],
               ["पार्श्व", "flank"]],
              "दश = ten, विस्तार = breadth, द्वादश = twelve, आयाम = length, पार्श्व = flank.",
              "दश, विस्तार, द्वादश, आयाम, पार्श्व.", role="extend",
              teaches="One line can give two measures of one part: breadth (विस्तार) and length (आयाम)."),
        mcq("discriminate", 3, "By unit 77, which measures go with the two flanks?",
            ("Ten in breadth, twelve in length", "दश विस्तारे द्वादशायामे: ten with breadth, twelve with length."),
            [("Twelve in breadth, ten in length", "The numbers are swapped: दश goes with विस्तारे."),
             ("Ten in length, twelve in girth", "No girth is named, and ten goes with breadth."),
             ("Ten in height, twelve in length", "No height is named; ten goes with breadth.")],
            "दश with विस्तार, द्वादश with आयाम.",
            "दश विस्तारे · द्वादश आयामे."),
        mcq("apply", 4, "Which split of द्वादशायामे in unit 77 is right?",
            ("द्वादश + आयामे", "अ + आ → आ: द्वादश + आयामे → द्वादशायामे."),
            [("द्वादशा + यामे", "द्वादशा is not a form of twelve, and यामे is not the measure-word here."),
             ("द्वाद + शायामे", "द्वाद and शायामे are not words."),
             ("द्वा + दशायामे", "दशायामे is not a word; द्वादश (twelve) is one numeral.")],
            "द्वादश (twelve) + आयामे (in length).",
            "अ + आ → आ."),
        mcq("transfer", 5, "By the pattern of द्वादश + आयामे → द्वादशायामे, how is सप्त + आयामः joined in a new example?",
            ("सप्तायामः", "अ + आ → आ: सप्त + आयामः → सप्तायामः."),
            [("सप्तयामः", "अ + आ gives a long आ; it is not cut to a short अ."),
             ("सप्तेयामः", "ए comes from अ + इ, not from अ + आ."),
             ("सप्तोयामः", "ओ comes from अ + उ, not from अ + आ.")],
            "सप्त + आयामः = सप्तायामः, like द्वादश + आयामे = द्वादशायामे.",
            "अ + आ → आ.",
            teaches="Short अ + long आ → long आ: द्वादश + आयामे → द्वादशायामे."),
    ],
}

# ---------------------------------------------------------------- unit 78
AUTHORED["78"] = {
    "title": "द्वादशोत्सेधं त्रिकं",
    "question": "By unit 78, what is the height of the trika?",
    "rule": ("The trika (त्रिकम्, probably the sacral region of the lower back) is twelve in height (द्वादशोत्सेधम्); "
             "aṅgula is understood."),
    "limits": ("Prose, no verb; aṅgula is understood, not printed. Trika as the sacral region is the data's probable "
               "identification: no question rests on what the trika is."),
    "explain_hi": ("त्रिक, जो सम्भवतः पीठ के निचले भाग का त्रिकास्थि वाला स्थान है (सम्भावित पहचान), ऊँचाई में बारह है। "
                   "उत्सेध = ऊँचाई; अंगुल समझा जाता है, छपा नहीं। "
                   "‘द्वादशोत्सेधं’ में द्वादश + उत्सेधम् (अ + उ → ओ) है, और व्यंजन त से पहले अन्तिम म् अनुस्वार लिखा गया। "
                   "‘द्वादशोत्सेधम्’ बहुव्रीहि है, ‘जिसकी ऊँचाई बारह है’, और नपुंसक ‘त्रिकम्’ से मेल खाता है।"),
    "hook": "त्रिक: बारह ऊँचा।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "In unit 78, what does उत्सेध mean?",
            ("Height", "उत्सेध = height: द्वादशोत्सेधम्, twelve in height."),
            [("Girth", "Girth is परिणाह; उत्सेध is height."),
             ("Length", "Length is आयाम (card 77); उत्सेध is height."),
             ("Breadth", "Breadth is विस्तार (card 77); उत्सेध is height.")],
            "उत्सेध = height.",
            "उत्सेध = height."),
        order(1, "Put the word-parts of unit 78 in the printed order.",
              ["द्वादश", "उत्सेधम्", "त्रिकम्"],
              "Twelve; in height; the trika: द्वादशोत्सेधं त्रिकं.",
              "द्वादश → उत्सेधम् → त्रिकम्."),
        T(multi("extend", 2, "Which statements fit unit 78?",
                [("The word अङ्गुल is printed in this line", "No: only the numeral is printed; aṅgula is understood."),
                 ("The trika is eighteen in height", "No: twelve. Eighteen in height is the back (card 79)."),
                 ("उत्सेध here means height", "Right: द्वादशोत्सेधम्, twelve in height."),
                 ("द्वादशोत्सेधम् is a bahuvrīhi, 'twelve in height'", "Right: it describes त्रिकम्.")],
                [2, 3],
                "The trika is twelve in height; aṅgula is understood.",
                "द्वादशोत्सेधं त्रिकम्."),
          "A bahuvrīhi such as द्वादशोत्सेधम् ('having a height of twelve') describes the noun it stands with."),
        mcq("discriminate", 3, "Which split of द्वादशोत्सेधं in unit 78 is right?",
            ("द्वादश + उत्सेधम्", "अ + उ → ओ: द्वादश + उत्सेधम् → द्वादशोत्सेधम्."),
            [("द्वादशो + त्सेधम्", "द्वादशो and त्सेधम् are not words; the ओ comes from अ + उ."),
             ("द्वादश + ओत्सेधम्", "ओत्सेधम् is not a word, and अ + ओ would give औ."),
             ("द्वादशः + उत्सेधम्", "अः before उ loses its visarga and gives no ओ: द्वादश उत्सेधम्.")],
            "द्वादश (twelve) + उत्सेधम् (height).",
            "अ + उ → ओ."),
        mcq("apply", 4, "In unit 78, why does द्वादशोत्सेधम् end in -म्?",
            ("It agrees with the neuter त्रिकम्", "A bahuvrīhi takes the gender of its noun: त्रिकम् is neuter."),
            [("It is the object of a verb", "The line has no verb; the copula is understood."),
             ("It marks the plural of twelve", "-म् here is neuter singular, not a plural."),
             ("It is the masculine nominative", "The masculine would be -उत्सेधः, as in card 70.")],
            "द्वादशोत्सेधम् (n.) with त्रिकम् (n.).",
            "A bahuvrīhi agrees with its noun."),
        mcq("transfer", 5, "By the pattern of द्वादश + उत्सेधम् → द्वादशोत्सेधम्, how is दश + उत्सेधः joined in a new example?",
            ("दशोत्सेधः", "अ + उ → ओ: दश + उत्सेधः → दशोत्सेधः."),
            [("दशौत्सेधः", "औ comes from अ + ओ or औ, not from अ + उ."),
             ("दशूत्सेधः", "The अ does not drop to leave a long ऊ."),
             ("दशवुत्सेधः", "व् arises from उ before an unlike vowel, not from अ + उ.")],
            "दश + उत्सेधः = दशोत्सेधः, like द्वादश + उत्सेधम् = द्वादशोत्सेधम्.",
            "अ + उ → ओ.",
            teaches="Short अ + short उ → ओ: द्वादश + उत्सेधम् → द्वादशोत्सेधम्."),
    ],
}

# ---------------------------------------------------------------- unit 79
AUTHORED["79"] = {
    "title": "अष्टादशोत्सेधं पृष्ठं",
    "question": "By unit 79, what is the height of the back (pṛṣṭha)?",
    "rule": "The back (पृष्ठम्) is eighteen in height (अष्टादशोत्सेधम्); aṅgula is understood.",
    "limits": "Prose, no verb; aṅgula is understood, not printed. Only the height is given: nothing on breadth or girth.",
    "explain_hi": ("पृष्ठ यानी पीठ ऊँचाई में अठारह है; अंगुल समझा जाता है। "
                   "यह ‘अंगुल-प्रमाण: पैर से पीठ तक’ खण्ड की अन्तिम इकाई है। "
                   "इकाई ७८ की तरह यहाँ भी ‘-उत्सेधम्’ है: अष्टादश + उत्सेधम् (अ + उ → ओ)। "
                   "बहुव्रीहि ‘अष्टादशोत्सेधम्’ नपुंसक ‘पृष्ठम्’ से मेल खाता है; पीठ की चौड़ाई या घेरा यहाँ नहीं दिया गया।"),
    "hook": "पीठ अठारह ऊँची।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "In unit 79, what does पृष्ठ mean?",
            ("The back", "पृष्ठ = back: अष्टादशोत्सेधं पृष्ठम्."),
            [("The belly", "The belly is उदर (card 76)."),
             ("The chest", "The chest is उरस् (card 82)."),
             ("The neck", "The neck is शिरोधरा (card 90).")],
            "पृष्ठ = the back.",
            "पृष्ठ = back."),
        order(1, "Put the word-parts of unit 79 in the printed order.",
              ["अष्टादश", "उत्सेधम्", "पृष्ठम्"],
              "Eighteen; in height; the back: अष्टादशोत्सेधं पृष्ठं.",
              "अष्टादश → उत्सेधम् → पृष्ठम्."),
        match(2, "Match each word of unit 79 to its meaning.",
              [["अष्टादश", "eighteen"], ["उत्सेध", "height"], ["पृष्ठ", "back"]],
              "अष्टादश = eighteen, उत्सेध = height, पृष्ठ = back.",
              "अष्टादश, उत्सेध, पृष्ठ.", role="extend",
              teaches="अष्टादश (eighteen) is built from 'eight' and 'ten' (अष्टा- + दश)."),
        mcq("discriminate", 3, "By unit 79, which statement is right?",
            ("The back is eighteen in height", "अष्टादशोत्सेधं पृष्ठम्: eighteen, in height."),
            [("The back is twelve in height", "Twelve in height is the trika (card 78)."),
             ("The back is eighteen in girth", "उत्सेध is height, not girth."),
             ("The back is eighteen in breadth", "उत्सेध is height, not breadth.")],
            "Eighteen, and the dimension is height.",
            "अष्टादश + उत्सेध: eighteen in height."),
        fill(4, ("Unit 79: अष्टादशोत्सेधं ____ (the back is eighteen in height). Type the missing word in Devanagari or "
                 "in English letters (e.g. dharma)."),
             accepts("पृष्ठम्"),
             "पृष्ठम् = the back; printed पृष्ठं at the line's end.",
             "पृष्ठम् (back) is the neuter noun that अष्टादशोत्सेधम् describes.",
             "अष्टादशोत्सेधं पृष्ठम्.", role="apply"),
        mcq("transfer", 5, ("By the pattern of अष्टादशोत्सेधं पृष्ठम्, how would 'a tree (वृक्षः, m.) eighteen in height' "
                            "read in a new example?"),
            ("अष्टादशोत्सेधो वृक्षः", "Masculine -उत्सेधः agrees with वृक्षः; अः before the voiced consonant व → ओ."),
            [("अष्टादशोत्सेधं वृक्षः", "-उत्सेधम् is neuter; वृक्षः is masculine."),
             ("अष्टादशोत्सेधा वृक्षः", "-उत्सेधा is feminine; वृक्षः is masculine."),
             ("अष्टादशोत्सेधे वृक्षः", "-उत्सेधे is not a masculine nominative singular.")],
            "The bahuvrīhi takes the noun's gender: masculine -उत्सेधः, joined as -उत्सेधो before व.",
            "A bahuvrīhi agrees with its noun; अः + voiced consonant → ओ.",
            teaches=("A measure-bahuvrīhi takes the gender of its noun: अष्टादशोत्सेधं पृष्ठम् (n.), but "
                     "चतुरङ्गुलोत्सेधः पादः (m., card 70).")),
    ],
}

# ---------------------------------------------------------------- unit 80
AUTHORED["80"] = {
    "title": "द्वादशकं स्तनांतरं",
    "question": "By unit 80, what measure is given for the interval between the breasts?",
    "rule": ("The interval between the breasts (स्तनान्तरम्) is a set of twelve (द्वादशकम्), that is, twelve with "
             "aṅgula understood."),
    "limits": ("Prose, no verb; aṅgula is understood, not printed, and no dimension is named. द्वादशक = a group of twelve "
               "(data's note)."),
    "explain_hi": ("दोनों स्तनों के बीच का अन्तर (स्तनान्तर) बारह का है; अंगुल समझा जाता है। "
                   "‘द्वादशक’ यानी बारह का समूह: संख्या द्वादश पर -क प्रत्यय। "
                   "यह ‘अंगुल-प्रमाण: वक्ष, कंधे और हाथ’ खण्ड की पहली इकाई है। "
                   "‘स्तनांतरं’ में स्तन + अन्तरम् (अ + अ → आ) है; छपा ‘अंतर’ अनुस्वार के साथ है, त से पहले यह न् है: अन्तर।"),
    "hook": "स्तनों के बीच: बारह।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "In स्तनान्तर of unit 80, what does अन्तर mean?",
            ("Interval between", "अन्तर = interval: स्तनान्तर, the interval between the breasts."),
            [("The tip or point", "A tip would be अग्र; अन्तर is the interval."),
             ("The lower base", "A base would be मूल; अन्तर is the interval."),
             ("The outer edge", "An edge or limit is पर्यन्त (card 81); अन्तर is the interval.")],
            "स्तन (breast) + अन्तर (interval between).",
            "अन्तर = interval."),
        order(1, "Put the word-parts of unit 80 in the printed order.",
              ["द्वादशकम्", "स्तन", "अन्तरम्"],
              "A set of twelve; breasts; interval: द्वादशकं स्तनांतरं.",
              "द्वादशकम् → स्तन → अन्तरम्."),
        match(2, "Match each word of unit 80 to its meaning.",
              [["द्वादशक", "a set of twelve"], ["स्तन", "breast"], ["अन्तर", "interval"]],
              "द्वादशक = a set of twelve, स्तन = breast, अन्तर = interval.",
              "द्वादशक, स्तन, अन्तर.", role="extend",
              teaches="-क added to a numeral can make a group noun: द्वादश (twelve) → द्वादशक (a set of twelve)."),
        mcq("discriminate", 3, "Which split of स्तनांतरं in unit 80 is right?",
            ("स्तन + अन्तरम्", "अ + अ → आ: स्तन + अन्तरम् → स्तनान्तरम्."),
            [("स्तना + अन्तरम्", "स्तना is not a form of स्तन here; the stem is स्तन."),
             ("स्त + नान्तरम्", "स्त and नान्तरम् are not words."),
             ("स्तनान् + तरम्", "स्तनान् + तरम् would give स्तनांस्तरम्, not the printed form.")],
            "स्तन (breast) + अन्तरम् (interval).",
            "अ + अ → आ."),
        mcq("apply", 4, "By unit 80, which part's measure is a set of twelve?",
            ("The space between the breasts", "द्वादशकं स्तनान्तरम्: the interval between the breasts."),
            [("The limit of each breast", "The limit of the breast is two aṅgulas (card 81)."),
             ("The full breadth of the chest", "The chest is twenty-four aṅgulas broad (card 82)."),
             ("The heart within the chest", "The heart is two aṅgulas (card 83).")],
            "Twelve goes with स्तनान्तरम्.",
            "द्वादशकम् with स्तनान्तरम्."),
        mcq("transfer", 5, "By the pattern of द्वादश → द्वादशक (a set of twelve), what does सप्तक mean in a new example?",
            ("A set of seven", "सप्त (seven) + -क: a group of seven, like द्वादशक."),
            [("Seventeen", "Seventeen would be सप्तदश."),
             ("Seventy", "Seventy would be सप्तति."),
             ("Seven times", "Seven times would be सप्तकृत्वः.")],
            "सप्तक = a set of seven, as द्वादशक = a set of twelve.",
            "Numeral + -क → a group of that number.",
            teaches="-क after a numeral makes a group noun: द्वादशक = a set of twelve."),
    ],
}

# ---------------------------------------------------------------- unit 81
AUTHORED["81"] = {
    "title": "द्व्यंगुलः स्तनपर्यंतः",
    "question": "By unit 81, how many aṅgulas is the limit (paryanta) of the breast?",
    "rule": "The limit of the breast (स्तनपर्यन्तः) is two aṅgulas (द्व्यङ्गुलः).",
    "limits": ("Prose, no verb. पर्यन्त = boundary, extremity; whether it means the breast's own extent or an edge region "
               "is not stated: no question on that."),
    "explain_hi": ("स्तन का पर्यन्त यानी छोर दो अंगुल का है। "
                   "पर्यन्त = सीमा, छोर; इसका अर्थ स्तन का अपना विस्तार है या किनारे का क्षेत्र, यह पाठ नहीं बताता। "
                   "‘द्व्यंगुलः’ में द्वि + अङ्गुलः है: इ के बाद भिन्न स्वर आए तो इ → य् (द्व्य)। "
                   "‘द्व्यङ्गुलः’ पुल्लिंग है, क्योंकि ‘पर्यन्तः’ पुल्लिंग है।"),
    "hook": "स्तन का छोर: दो अंगुल।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "In unit 81, what does पर्यन्त mean?",
            ("Limit, extremity", "पर्यन्त = boundary, extremity: स्तनपर्यन्तः, the limit of the breast."),
            [("Middle, centre", "The middle would be मध्य; पर्यन्त is the limit."),
             ("Swelling, bulk", "Bulk would be उपचय; पर्यन्त is the limit."),
             ("Colour, tint", "Colour would be वर्ण; पर्यन्त is the limit.")],
            "पर्यन्त = limit, extremity.",
            "पर्यन्त = limit."),
        order(1, "Put the word-parts of unit 81 in the printed order.",
              ["द्वि", "अङ्गुलः", "स्तन", "पर्यन्तः"],
              "Two; aṅgulas; breast; limit: द्व्यंगुलः स्तनपर्यंतः.",
              "द्वि → अङ्गुलः → स्तन → पर्यन्तः."),
        match(2, "Match each word-part of unit 81 to its meaning.",
              [["द्वि", "two"], ["अङ्गुल", "finger-breadth"], ["स्तन", "breast"], ["पर्यन्त", "limit"]],
              "द्वि = two, अङ्गुल = finger-breadth, स्तन = breast, पर्यन्त = limit.",
              "द्वि, अङ्गुल, स्तन, पर्यन्त.", role="extend",
              teaches="द्व्यङ्गुलः is masculine to agree with the masculine पर्यन्तः."),
        mcq("discriminate", 3, "Which split of द्व्यंगुलः in unit 81 is right?",
            ("द्वि + अङ्गुलः", "इ before the unlike vowel अ → य्: द्वि + अङ्गुलः → द्व्यङ्गुलः."),
            [("द्व + यङ्गुलः", "द्व and यङ्गुलः are not words; the य् comes from इ."),
             ("द्वे + अङ्गुलः", "ए + अ would give द्वेऽङ्गुलः, not द्व्य-."),
             ("द्व्य + अङ्गुलः", "That would give द्व्याङ्गुलः, with a long आ that is not printed.")],
            "द्वि (two) + अङ्गुलः (aṅgulas).",
            "इ + unlike vowel → य्."),
        mcq("apply", 4, "Why is द्वि + अङ्गुलः printed द्व्यंगुलः in unit 81?",
            ("इ before an unlike vowel → य्", "अ is unlike इ, so इ becomes य्: द्व्यङ्गुलः."),
            [("इ before any consonant → य्", "Before a consonant इ stays इ; the change is before a vowel."),
             ("इ + अ always gives ए", "ए comes from अ + इ (अ first), not from इ + अ."),
             ("इ + अ always gives ई", "ई comes from इ + इ, a like vowel, not from इ + अ.")],
            "द्वि + अङ्गुलः: इ before अ → य्.",
            "इ + unlike vowel → य्."),
        mcq("transfer", 5, "By the pattern of द्वि + अङ्गुलः → द्व्यङ्गुलः, how is प्रति + अङ्गम् joined in a new example?",
            ("प्रत्यङ्गम्", "इ before the unlike vowel अ → य्: प्रति + अङ्गम् → प्रत्यङ्गम्."),
            [("प्रतीङ्गम्", "ई comes from इ + इ, not from इ + अ."),
             ("प्रतेङ्गम्", "ए comes from अ + इ, not from इ + अ."),
             ("प्रतियङ्गम्", "The इ is replaced by य्; it is not kept beside it.")],
            "प्रति + अङ्गम् = प्रत्यङ्गम्, like द्वि + अङ्गुलः = द्व्यङ्गुलः.",
            "इ + unlike vowel → य्.",
            teaches="इ before an unlike vowel becomes य्: द्वि + अङ्गुलः → द्व्यङ्गुलः."),
    ],
}

# ---------------------------------------------------------------- unit 82
AUTHORED["82"] = {
    "title": "चतुर्विंशत्यंगुलविशालं द्वादशोत्सेधमुरः",
    "question": "By unit 82, what are the breadth and the height of the chest (uras)?",
    "rule": ("The chest (उरः) is twenty-four aṅgulas broad (चतुर्विंशत्यङ्गुलविशालम्) and twelve in height "
             "(द्वादशोत्सेधम्)."),
    "limits": ("Prose, no verb. No girth is given. The second measure prints only the numeral; aṅgula is understood "
               "there."),
    "explain_hi": ("उरस् यानी छाती चौबीस अंगुल चौड़ी और ऊँचाई में बारह है। "
                   "विशाल = चौड़ा, उत्सेध = ऊँचाई: एक अंग के दो माप; दूसरे माप में अंगुल समझा जाता है। "
                   "‘चतुर्विंशत्यंगुल’ में चतुर्विंशति + अङ्गुल है (इ के बाद भिन्न स्वर: इ → य्)। "
                   "‘द्वादशोत्सेधमुरः’ में द्वादश + उत्सेधम् (अ + उ → ओ) है, और फिर स्वर उ से पहले म् जुड़ गया। "
                   "‘उरः’ नपुंसक (उरस्) है, इसलिए दोनों विशेषण नपुंसक -म् में हैं।"),
    "hook": "छाती: चौबीस चौड़ी, बारह ऊँची।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "In unit 82, what does उरस् (printed उरः) mean?",
            ("The chest", "उरस् = chest: द्वादशोत्सेधमुरः."),
            [("The thigh", "The thigh is ऊरु (card 73), a different word."),
             ("The belly", "The belly is उदर (card 76)."),
             ("The shoulder", "The shoulder is स्कन्ध (card 84).")],
            "उरस् = chest.",
            "उरस् = chest."),
        order(1, "Put the word-parts of unit 82 in the printed order.",
              ["चतुर्विंशति", "अङ्गुल", "विशालम्", "द्वादश", "उत्सेधम्", "उरः"],
              "Twenty-four; aṅgulas; broad; twelve; in height; the chest.",
              "चतुर्विंशति → अङ्गुल → विशालम् → द्वादश → उत्सेधम् → उरः."),
        match(2, "Match each word of unit 82 to its meaning.",
              [["चतुर्विंशति", "twenty-four"], ["विशाल", "broad"], ["द्वादश", "twelve"], ["उत्सेध", "height"],
               ["उरस्", "chest"]],
              "चतुर्विंशति = twenty-four, विशाल = broad, द्वादश = twelve, उत्सेध = height, उरस् = chest.",
              "चतुर्विंशति, विशाल, द्वादश, उत्सेध, उरस्.", role="extend",
              teaches="A part can carry two measure-words: विशाल (broad) and उत्सेध (height)."),
        mcq("discriminate", 3, "By unit 82, which pair of measures belongs to the chest?",
            ("24 broad and 12 in height", "चतुर्विंशत्यङ्गुलविशालं द्वादशोत्सेधम्: 24 broad, 12 high."),
            [("12 broad and 24 in height", "The numbers are swapped: twenty-four goes with विशाल."),
             ("24 in girth and 12 broad", "No girth is named; twelve goes with height."),
             ("24 broad and 18 in height", "The height is twelve (द्वादश), not eighteen.")],
            "Twenty-four with breadth, twelve with height.",
            "चतुर्विंशति + विशाल · द्वादश + उत्सेध."),
        mcq("apply", 4, "Which split of चतुर्विंशत्यंगुल in unit 82 is right?",
            ("चतुर्विंशति + अङ्गुल", "इ before the unlike vowel अ → य्: -विंशति + अङ्गुल → -विंशत्यङ्गुल."),
            [("चतुर्विंशत् + यङ्गुल", "यङ्गुल is not a word; the य् comes from the इ of विंशति."),
             ("चतुर्विंशत्य + अङ्गुल", "That would give -त्याङ्गुल, with a long आ that is not printed."),
             ("चतुर्विंशते + अङ्गुल", "ए + अ would give -तेऽङ्गुल, not -त्यङ्गुल.")],
            "चतुर्विंशति (twenty-four) + अङ्गुल.",
            "इ + unlike vowel → य्."),
        mcq("transfer", 5, ("By the pattern of unit 82, what does षडङ्गुलविशालं द्वादशोत्सेधं फलकम् mean in a new "
                            "example?"),
            ("A board six broad and twelve high", "विशाल = broad, उत्सेध = height: six aṅgulas broad, twelve high."),
            [("A board twelve broad and six high", "The numbers are swapped: षट् goes with विशाल."),
             ("A board six long and twelve broad", "विशाल is breadth, not length; उत्सेध is height."),
             ("A board six high and twelve round", "उत्सेध is height, not girth; six goes with breadth.")],
            "षडङ्गुलविशालम् = six aṅgulas broad; द्वादशोत्सेधम् = twelve in height.",
            "Numeral + विशाल = breadth; numeral + उत्सेध = height.",
            teaches="Each measure-word follows its numeral: चतुर्विंशत्यङ्गुलविशालम् (24 broad), द्वादशोत्सेधम् (12 high)."),
    ],
}

# ---------------------------------------------------------------- unit 83
AUTHORED["83"] = {
    "title": "द्व्यंगुलं हृदयं",
    "question": "By unit 83, how many aṅgulas is the heart (hṛdaya)?",
    "rule": "The heart (हृदयम्) is of two aṅgulas (द्व्यङ्गुलम्).",
    "limits": "Prose, no verb. The dimension is not stated: no question on it.",
    "explain_hi": ("हृदय यानी दिल दो अंगुल का है। "
                   "कौन-सा माप (लम्बाई, चौड़ाई आदि) है, यह नहीं कहा गया। "
                   "इकाई ८१ की तरह ‘द्व्यंगुल’ में द्वि + अङ्गुल है (इ के बाद भिन्न स्वर → य्); पर यहाँ ‘द्व्यङ्गुलम्’ नपुंसक है, क्योंकि ‘हृदयम्’ नपुंसक है, "
                   "जबकि इकाई ८१ में पुल्लिंग ‘पर्यन्तः’ के साथ ‘द्व्यङ्गुलः’ है। "
                   "व्यंजन ह से पहले अन्तिम म् अनुस्वार लिखा गया।"),
    "hook": "दिल: दो अंगुल।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "In unit 83, what does हृदय mean?",
            ("The heart", "हृदय = heart (standard)."),
            [("The lung", "The lung would be फुफ्फुस."),
             ("The liver", "The liver would be यकृत्."),
             ("The spleen", "The spleen would be प्लीहा.")],
            "हृदय = heart.",
            "हृदय = heart."),
        order(1, "Put the word-parts of unit 83 in the printed order.",
              ["द्वि", "अङ्गुलम्", "हृदयम्"],
              "Two; aṅgulas; the heart: द्व्यंगुलं हृदयं.",
              "द्वि → अङ्गुलम् → हृदयम्."),
        match(2, "Match each word-part of unit 83 to its meaning.",
              [["द्वि", "two"], ["अङ्गुल", "finger-breadth"], ["हृदय", "heart"]],
              "द्वि = two, अङ्गुल = finger-breadth, हृदय = heart.",
              "द्वि, अङ्गुल, हृदय.", role="extend",
              teaches="द्व्यङ्गुलम् is neuter because हृदयम् is neuter; with the masculine पर्यन्तः (card 81) it is द्व्यङ्गुलः."),
        mcq("discriminate", 3, "By unit 83, which statement is right?",
            ("The heart is two aṅgulas", "द्व्यङ्गुलं हृदयम्: two aṅgulas."),
            [("The heart is twelve aṅgulas", "Twelve aṅgulas is the belly (card 76)."),
             ("The heart is two in girth", "The line names no dimension."),
             ("The heart is of eight", "Of eight are the shoulders (card 84).")],
            "Two aṅgulas; no dimension is named.",
            "द्व्यङ्गुलम् with हृदयम्."),
        mcq("apply", 4, "Why is द्व्यङ्गुलम् printed द्व्यंगुलं before हृदयं in unit 83?",
            ("Final म् before a consonant → ं", "ह is a consonant: inside a sentence the final म् is written ं."),
            [("Final म् before any sound → ं", "Not any: before a vowel म् joins it (द्वादशांगुलमुदरं, card 76)."),
             ("ं marks the neuter gender", "The neuter is shown by -म्; ं is only its sandhi form."),
             ("ं stands for a dropped visarga", "The word ends in म्, not in a visarga.")],
            "द्व्यङ्गुलम् + हृदयम्: final म् before ह → ं.",
            "Final म् + consonant → ं (in a sentence)."),
        mcq("transfer", 5, ("By the pattern of द्व्यङ्गुलं हृदयम्, how does 'a thread (सूत्रम्, n.) of ten aṅgulas' read in "
                            "a new example?"),
            ("दशाङ्गुलं सूत्रम्", "Neuter -म् agrees with सूत्रम्, written ं before the consonant स."),
            [("दशाङ्गुलः सूत्रम्", "-अङ्गुलः is masculine; सूत्रम् is neuter."),
             ("दशाङ्गुला सूत्रम्", "-अङ्गुला is feminine; सूत्रम् is neuter."),
             ("दशाङ्गुलौ सूत्रम्", "-अङ्गुलौ is dual; सूत्रम् is singular.")],
            "दशाङ्गुलं सूत्रम्: neuter singular, like द्व्यङ्गुलं हृदयम्.",
            "The measure-word agrees with its noun.",
            teaches="The measure-word takes its noun's gender and number: द्व्यङ्गुलं हृदयम् (n. sg.)."),
    ],
}

# ---------------------------------------------------------------- unit 84
AUTHORED["84"] = {
    "title": "अष्टकौ स्कंधौ कक्षे च",
    "question": "By unit 84, what measure do the two shoulders (skandha) have, and how are the armpits joined to it?",
    "rule": ("The two shoulders (स्कन्धौ) are of eight (अष्टकौ), and the two armpits (कक्षे च): by the data's reading "
             "the armpits share the eight through च."),
    "limits": ("Prose, no verb; aṅgula is understood and no dimension is named. अष्टकौ is masculine dual and agrees only "
               "with स्कन्धौ; that the armpits share the measure is understood from च (data's note), not printed. How "
               "skandha differs from aṃsa (card 85) is not stated."),
    "explain_hi": ("दोनों स्कन्ध यानी कंधे आठ के हैं, और दोनों कक्ष यानी काँख भी। "
                   "‘अष्टकौ’ पुल्लिंग द्विवचन है और रूप में केवल ‘स्कन्धौ’ से मेल खाता है; काँखों का भी वही माप है, यह ‘च’ से समझा जाता है (डेटा की व्याख्या)। "
                   "अंगुल समझा जाता है, और माप का प्रकार (लम्बाई, चौड़ाई आदि) नहीं कहा गया। "
                   "‘अष्टक’ = आठ का समूह, जैसे इकाई ८० में ‘द्वादशक’।"),
    "hook": "कंधे आठ के, और काँख भी।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "In unit 84, what does कक्ष (printed कक्षे) mean?",
            ("Armpit", "कक्ष = armpit (standard): कक्षे, the two armpits."),
            [("Elbow", "The elbow would be कूर्पर."),
             ("Wrist", "The wrist would be मणिबन्ध."),
             ("Collarbone", "The collar region would be जत्रु.")],
            "कक्ष = armpit.",
            "कक्ष = armpit."),
        order(1, "Put the words of unit 84 in the printed order.",
              ["अष्टकौ", "स्कन्धौ", "कक्षे", "च"],
              "Of eight; the two shoulders; the two armpits; and.",
              "अष्टकौ → स्कन्धौ → कक्षे → च."),
        match(2, "Match each word of unit 84 to its meaning.",
              [["अष्टक", "a set of eight"], ["स्कन्ध", "shoulder"], ["कक्ष", "armpit"], ["च", "and"]],
              "अष्टक = a set of eight, स्कन्ध = shoulder, कक्ष = armpit, च = and.",
              "अष्टक, स्कन्ध, कक्ष, च.", role="extend",
              teaches="अष्टकौ is a masculine dual: in form it agrees with स्कन्धौ."),
        mcq("discriminate", 3, "By the data's note on unit 84, with which word does अष्टकौ agree in form?",
            ("स्कन्धौ only", "अष्टकौ and स्कन्धौ are both masculine duals."),
            [("कक्षे only", "कक्षे is not a masculine dual; अष्टकौ does not match its form."),
             ("Both स्कन्धौ and कक्षे", "Only स्कन्धौ matches; the armpits come in through च."),
             ("Neither of the two", "It matches स्कन्धौ: masculine, dual.")],
            "Form agreement: अष्टकौ with स्कन्धौ; the armpits share the measure through च.",
            "अष्टकौ (m. du.) = स्कन्धौ (m. du.)."),
        multi("apply", 4, "Which statements fit unit 84?",
              [("The armpits' share of the eight is understood from च", "Right: the data reads it so; it is not printed."),
               ("अष्टकौ is a feminine dual", "No: it is a masculine dual."),
               ("The line prints the word अङ्गुल", "No: aṅgula is understood."),
               ("स्कन्धौ is a masculine dual", "Right: two shoulders.")],
              [0, 3],
              "Two shoulders of eight; the armpits join through च.",
              "अष्टकौ स्कन्धौ · कक्षे च."),
        mcq("transfer", 5, "By the pattern of अष्टकौ स्कन्धौ, how does 'two pots (घटौ) of eight' read in a new example?",
            ("अष्टकौ घटौ", "Masculine dual -औ agrees with the masculine dual घटौ."),
            [("अष्टकं घटौ", "अष्टकम् (written ं before घ) is neuter singular; घटौ is masculine dual."),
             ("अष्टके घटौ", "अष्टके is not a masculine dual; घटौ needs -औ."),
             ("अष्टको घटौ", "अष्टको is अष्टकः (m. sg.) before a voiced sound; घटौ is dual.")],
            "अष्टकौ घटौ: masculine dual with masculine dual.",
            "The measure-word agrees with its noun in gender and number.",
            teaches="A measure-word in -क agrees with its noun: अष्टकौ स्कन्धौ (m. du.)."),
    ],
}

# ---------------------------------------------------------------- unit 85
AUTHORED["85"] = {
    "title": "षड्डावंसौ",
    "question": "In unit 85 (षड्डावंसौ), which part is fairly sure and which part is doubtful?",
    "rule": ("On a conjectural reading, the two aṃsa (अंसौ, probably the shoulder-joints) are of six. अंसौ and the "
             "numeral six are fairly sure; the middle syllables of the print are not."),
    "limits": ("Low confidence. Printed षड्डा- is no regular form; a dual -क numeral (from the parallel forms in cards 84, "
               "86 and 87) is a possible reading only: no question rests on the re-reading. Aṃsa as shoulder-joint is "
               "probable; how it differs from skandha (card 84) is not stated."),
    "explain_hi": ("अनुमानित पाठ पर, दोनों अंस यानी सम्भवतः कंधे के जोड़ छः के हैं। "
                   "छपा ‘षड्डा’ कोई नियमित रूप नहीं; पास के कार्ड ८४, ८६, ८७ के द्विवचन -क रूप (अष्टकौ, षोडशकौ, पञ्चदशकौ) देखकर ‘षट्कौ अंसौ’ (= षट्कावंसौ) एक सम्भव पाठ है, केवल अनुमान। "
                   "‘छः’ और ‘अंसौ’ लगभग पक्के हैं, बीच के अक्षर नहीं। "
                   "अंस = कंधा या कंधे का जोड़ (सम्भावित); कार्ड ८४ का स्कन्ध भी कंधा कहा गया है, दोनों का भेद यहाँ नहीं बताया गया।"),
    "hook": "अंस: छः, पर बीच के अक्षर धुँधले।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "In unit 85, which probable meaning does the data give for अंस?",
            ("Shoulder-joint", "अंस = shoulder or shoulder-joint (probable, by the data)."),
            [("Knee-joint", "The knee is जानु (card 72); अंस is the shoulder region."),
             ("Hip-joint", "The hip region is कटी (card 74); अंस is the shoulder region."),
             ("Wrist-joint", "The wrist would be मणिबन्ध; अंस is the shoulder region.")],
            "अंस = shoulder or shoulder-joint (probable).",
            "अंस = shoulder-joint (probable)."),
        mcq("warmup", 1, "Why does the data doubt the printed षड्डा- of unit 85?",
            ("It is not a regular form", "The data's note: 'ṣaḍḍā' is not a form."),
            [("It repeats the line before", "The line before (card 84) is अष्टकौ स्कंधौ कक्षे च; nothing is repeated."),
             ("It has no numeral at all", "षड्- (six) is the fairly sure part, by the data."),
             ("It is a verb with no subject", "No verb is printed; the line is a measure.")],
            "षड्डा- is not a regular form, so the middle syllables are doubtful.",
            "Printed षड्डा- = not a regular form."),
        match(2, "The data's note on unit 85 cites three parallel dual forms. Match each to its meaning.",
              [["अष्टकौ", "of eight"], ["षोडशकौ", "of sixteen"], ["पञ्चदशकौ", "of fifteen"]],
              "अष्टकौ (card 84) = of eight, षोडशकौ (card 86) = of sixteen, पञ्चदशकौ (card 87) = of fifteen.",
              "अष्टकौ, षोडशकौ, पञ्चदशकौ.", role="extend",
              teaches="Dual numerals in -क stand in the lines around this one; they ground the guess, nothing more."),
        multi("discriminate", 3, "Which statements fit unit 85, by the data?",
              [("षट्कौ is the printed word", "No: the print has षड्डा-; षट्कौ is only a possible reading."),
               ("The numeral six is fairly sure", "Right: the data calls six and aṃsa fairly sure."),
               ("Aṃsa is given as the knee", "No: aṃsa is the shoulder or shoulder-joint (probable)."),
               ("How aṃsa differs from skandha is not stated", "Right: the data says so.")],
              [1, 3],
              "Six and aṃsa are fairly sure; the middle syllables are not.",
              "Sure: षड्- and अंसौ. Doubtful: the middle syllables."),
        mcq("apply", 4, "In unit 85, what number does अंसौ show, by its grammar label?",
            ("Dual: two aṃsa", "The label is m. nom. du.: the two aṃsa."),
            [("Singular: one aṃsa", "The singular would be अंसः."),
             ("Plural: many aṃsa", "The plural would be अंसाः."),
             ("Plural: six aṃsa", "Six is the measure, not the count; अंसौ is dual.")],
            "अंसौ = m. nom. dual: the two aṃsa.",
            "अंसौ: m. nom. du."),
        mcq("transfer", 5, ("By the rule -औ + vowel → -आव् (printed in card 74: -मेढ्रौ + अष्ट- → -मेढ्रावष्ट-), how is "
                            "बालौ + अत्र joined in a new example?"),
            ("बालावत्र", "-औ before the vowel अ → -आव्: बालौ + अत्र → बालावत्र."),
            [("बालोऽत्र", "ओऽ comes from अः + अ; here the word ends in -औ."),
             ("बालौत्र", "-औ does not swallow the अ; it becomes -आव् before a vowel."),
             ("बालायत्र", "-आय् comes from ऐ before a vowel, not from औ.")],
            "बालौ + अत्र = बालावत्र, like -मेढ्रौ + अष्ट- = -मेढ्रावष्ट-.",
            "औ + vowel → आव्.",
            teaches="A final -औ before a vowel becomes -आव्: -मेढ्रौ + अष्ट- → -मेढ्रावष्ट- (card 74)."),
    ],
}

# ---------------------------------------------------------------- unit 86
AUTHORED["86"] = {
    "title": "षोडशकौ प्रबाहू",
    "question": "By unit 86, what measure is given for the two prabāhu?",
    "rule": ("The two prabāhu (प्रबाहू, a segment of the arm; identity disputed) are of sixteen (षोडशकौ); aṅgula is "
             "understood."),
    "limits": ("Prose, no verb; aṅgula is understood and no dimension is named. Which segment of the arm prabāhu is "
               "(forearm or another part of the upper limb) is disputed: the Sanskrit term is kept and no question rests "
               "on its identity."),
    "explain_hi": ("दोनों प्रबाहु सोलह के हैं; अंगुल समझा जाता है। "
                   "प्रबाहु भुजा का कोई भाग है: कुछ कोश इसे अग्रबाहु कहते हैं, कुछ ऊपरी अंग का कोई और भाग; पहचान विवादित है, इसलिए संस्कृत शब्द ही रखा गया। "
                   "‘षोडशकौ’ = सोलह का समूह, पुल्लिंग द्विवचन, ‘प्रबाहू’ से मेल। "
                   "‘प्रबाहू’ उकारान्त पुल्लिंग (बाहु की तरह) का प्रथमा द्विवचन है: -उ → -ऊ।"),
    "hook": "प्रबाहु: सोलह (पहचान विवादित)।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "In unit 86, what does षोडश mean?",
            ("Sixteen", "षोडश = sixteen: षोडशकौ, of sixteen."),
            [("Sixty", "Sixty would be षष्टि."),
             ("Six", "Six would be षट्."),
             ("Fourteen", "Fourteen would be चतुर्दश.")],
            "षोडश = sixteen.",
            "षोडश = sixteen."),
        order(1, "Build षोडशकौ of unit 86: put its parts in order.",
              ["षोडश", "-क", "-औ"],
              "Numeral षोडश (sixteen) + -क (a set of) + -औ (masculine nominative dual).",
              "षोडश → -क → -औ."),
        fill(2, ("Unit 86: ____ प्रबाहू (the two prabāhu are of sixteen). Type the missing word in Devanagari or in "
                 "English letters (e.g. dharma)."),
             accepts("षोडशकौ"),
             "षोडशकौ = of sixteen, masculine dual like प्रबाहू.",
             "षोडशकौ (of sixteen) agrees with the masculine dual प्रबाहू.",
             "षोडशकौ प्रबाहू."),
        mcq("discriminate", 3, "In unit 86, why does षोडशक end in -औ (षोडशकौ)?",
            ("It agrees with the m. dual प्रबाहू", "Both are masculine nominative duals."),
            [("It agrees with a feminine noun", "प्रबाहू is masculine; a feminine would need -े."),
             ("It marks the plural number", "The plural would be षोडशकाः; -औ is dual here."),
             ("It is a locative of place", "The locative of an अ-stem is -े (षोडशके), not -औ.")],
            "षोडशकौ (m. du.) with प्रबाहू (m. du.).",
            "The measure-word agrees with its noun."),
        mcq("apply", 4, "In unit 86, why does प्रबाहु end in -ऊ (प्रबाहू)?",
            ("-ऊ is the m. u-stem nom. dual", "Masculine u-stem, like बाहु: nominative dual -ऊ."),
            [("-ऊ is the u-stem nom. plural", "The plural is -अवः (बाहवः); -ऊ is the dual."),
             ("-ऊ marks the feminine gender", "The label is masculine; -ऊ here is the dual."),
             ("-ऊ is the vocative singular", "The vocative singular would be -ओ (बाहो).")],
            "प्रबाहु → प्रबाहू: m. nom. dual.",
            "Masculine u-stem: nominative dual -ऊ."),
        mcq("transfer", 5, ("By the pattern of प्रबाहु → प्रबाहू (two), what is the nominative dual of गुरु (teacher) in "
                            "a new example?"),
            ("गुरू", "Masculine u-stem: nominative dual -ऊ, like प्रबाहू."),
            [("गुरवः", "गुरवः is the nominative plural."),
             ("गुरुः", "गुरुः is the nominative singular."),
             ("गुरौ", "गुरौ is the locative singular.")],
            "गुरु → गुरू (two teachers), like प्रबाहु → प्रबाहू.",
            "Masculine u-stem: nominative dual -ऊ.",
            teaches="A masculine u-stem forms its nominative dual in -ऊ: प्रबाहु → प्रबाहू."),
    ],
}

# ---------------------------------------------------------------- unit 87
AUTHORED["87"] = {
    "title": "पंचदशकौ प्रपाणी",
    "question": "By unit 87, what measure is given for the two prapāṇi?",
    "rule": ("The two prapāṇi (प्रपाणी, a part of the hand or arm; identity disputed) are of fifteen (पञ्चदशकौ); "
             "aṅgula is understood."),
    "limits": ("Prose, no verb; aṅgula is understood and no dimension is named. What prapāṇi is remains disputed (the "
               "data notes fifteen exceeds the hand's twelve in card 88, so a part of the arm is possible, not certain): "
               "no question rests on its identity."),
    "explain_hi": ("दोनों प्रपाणि पन्द्रह के हैं; अंगुल समझा जाता है। "
                   "प्रपाणि हाथ या बाँह का कोई भाग है, पहचान विवादित; डेटा बताता है कि पन्द्रह हाथ के बारह (कार्ड ८८) से अधिक है, इसलिए बाँह का भाग सम्भव है, पर निश्चित नहीं। "
                   "‘पञ्चदशकौ’ = पन्द्रह का समूह, पुल्लिंग द्विवचन। "
                   "‘प्रपाणी’ इकारान्त पुल्लिंग (पाणि की तरह) का प्रथमा द्विवचन है: -इ → -ई। "
                   "छपा ‘पंच’ अनुस्वार के साथ है; च से पहले यह ञ् है: पञ्च।"),
    "hook": "प्रपाणि: पन्द्रह (पहचान विवादित)।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "In unit 87, what does पञ्चदश mean?",
            ("Fifteen", "पञ्चदश = fifteen (पञ्च + दश, five and ten)."),
            [("Fifty", "Fifty is पञ्चाशत् (card 74)."),
             ("Five", "Five is पञ्च alone."),
             ("Twenty-five", "Twenty-five would be पञ्चविंशति.")],
            "पञ्चदश = fifteen.",
            "पञ्चदश = fifteen."),
        order(1, "Build पञ्चदशकौ of unit 87: put its parts in order.",
              ["पञ्च", "दश", "-क", "-औ"],
              "पञ्च (five) + दश (ten) = fifteen, + -क (a set of) + -औ (masculine nominative dual).",
              "पञ्च → दश → -क → -औ."),
        T(multi("extend", 2, "Which statements fit unit 87?",
                [("पञ्चदशकौ is a masculine dual", "Right: it agrees with प्रपाणी."),
                 ("प्रपाणी is the nominative dual of प्रपाणि", "Right: masculine i-stem, dual -ई."),
                 ("The line prints the word अङ्गुल", "No: aṅgula is understood."),
                 ("The line names fifteen as a length", "No: no dimension is named.")],
                [0, 1],
                "Two masculine duals; aṅgula and the dimension are not printed.",
                "पञ्चदशकौ प्रपाणी."),
          "A numeral in -क and its noun stand in the same gender and number: पञ्चदशकौ प्रपाणी (m. du.)."),
        mcq("discriminate", 3, "Why is the printed पंच read पञ्च in unit 87?",
            ("ं before च stands for ञ्", "Anusvāra before a palatal stands for the palatal nasal ञ्."),
            [("ं before च stands for न्", "न् is the nasal of the त-row, not of च."),
             ("ं before च stands for म्", "म् is the nasal of the प-row, not of च."),
             ("ं before च stands for ङ्", "ङ् is the nasal of the क-row, not of च.")],
            "पंच = पञ्च: ं before च = ञ्.",
            "ं = the nasal of the next consonant's row."),
        mcq("apply", 4, "In unit 87, why does प्रपाणि end in -ई (प्रपाणी)?",
            ("-ई is the m. i-stem nom. dual", "Masculine i-stem, like पाणि: nominative dual -ई."),
            [("-ई is the i-stem nom. plural", "The plural is -अयः (पाणयः); -ई is the dual."),
             ("-ई marks the feminine gender", "The label is masculine; -ई here is the dual."),
             ("-ई is the locative singular", "The locative singular would be -औ (पाणौ).")],
            "प्रपाणि → प्रपाणी: m. nom. dual.",
            "Masculine i-stem: nominative dual -ई."),
        mcq("transfer", 5, ("By the pattern of प्रपाणि → प्रपाणी (two), what is the nominative dual of मुनि (sage) in a "
                            "new example?"),
            ("मुनी", "Masculine i-stem: nominative dual -ई, like प्रपाणी."),
            [("मुनयः", "मुनयः is the nominative plural."),
             ("मुनिः", "मुनिः is the nominative singular."),
             ("मुनौ", "मुनौ is the locative singular.")],
            "मुनि → मुनी (two sages), like प्रपाणि → प्रपाणी.",
            "Masculine i-stem: nominative dual -ई.",
            teaches="A masculine i-stem forms its nominative dual in -ई: प्रपाणि → प्रपाणी."),
    ],
}

# ================================================================ NOTES_HI
NOTES_HI = {
    "75": ("गद्य; विश्वास मध्यम; कोई पाठ-चिह्न नहीं। क्रिया (है) समझी जाती है। बस्ति = मूत्राशय (मानक); ‘बस्तिशिर’ शब्दशः रखा गया, ठीक "
           "कौन-सा भाग (मूत्राशय का ऊपरी भाग या उसके ऊपर का क्षेत्र) यह नहीं कहा गया। माप का प्रकार नहीं बताया। छपाई में "
           "‘दशांगुलंबस्तिशिरः’ बिना जगह है। सन्धि जाँची: दश + अङ्गुलम् → दशाङ्गुलम् (अ + अ → आ); व्यंजन ब से पहले अन्तिम म् → ं "
           "(दशांगुलं)। छपा ‘अंगुल’ = अङ्गुल (ग से पहले ं = ङ्)।"),
    "76": ("गद्य; विश्वास उच्च; कोई पाठ-चिह्न नहीं। यहाँ उदर शरीर का अंग (पेट) है, रोग नहीं (डेटा की टिप्पणी)। माप का प्रकार नहीं "
           "बताया। सन्धि जाँची: द्वादश + अङ्गुलम् → द्वादशाङ्गुलम् (अ + अ → आ); द्वादशाङ्गुलम् + उदरम् → द्वादशाङ्गुलमुदरम् (स्वर से पहले म् "
           "जुड़ता है)। पंक्ति के अन्त का ‘उदरं’ अनुस्वार छपाई की आदत है, शब्द उदरम्।"),
    "77": ("गद्य; विश्वास मध्यम; कोई पाठ-चिह्न नहीं। ‘अंगुल’ छपा नहीं, समझा जाता है। ‘विस्तारे’ और ‘-आयामे’ सप्तमी (चौड़ाई में, "
           "लम्बाई में) भी हो सकते हैं और ‘पार्श्वे’ से मेल खाते द्विवचन भी; अर्थ एक ही है, इसलिए विभक्ति पर प्रश्न नहीं। पार्श्व = धड़ "
           "का बगल (मानक)। सन्धि जाँची: द्वादश + आयामे → द्वादशायामे (अ + आ → आ)।"),
    "78": ("गद्य; विश्वास मध्यम; कोई पाठ-चिह्न नहीं। त्रिक = पीठ का निचला भाग जहाँ रीढ़ श्रोणि से मिलती है, त्रिकास्थि (सम्भावित); "
           "इसकी पहचान पर प्रश्न नहीं। ‘अंगुल’ समझा जाता है। सन्धि जाँची: द्वादश + उत्सेधम् → द्वादशोत्सेधम् (अ + उ → ओ); व्यंजन त से "
           "पहले अन्तिम म् → ं (द्वादशोत्सेधं)। पंक्ति के अन्त का ‘त्रिकं’ अनुस्वार छपाई की आदत है।"),
    "79": ("गद्य; विश्वास उच्च; कोई पाठ-चिह्न नहीं। ‘अंगुल’ समझा जाता है; केवल ऊँचाई दी गई। सन्धि जाँची: अष्टादश + उत्सेधम् → "
           "अष्टादशोत्सेधम् (अ + उ → ओ); व्यंजन प से पहले अन्तिम म् → ं (अष्टादशोत्सेधं)। पंक्ति के अन्त का ‘पृष्ठं’ अनुस्वार छपाई की आदत है।"),
    "80": ("गद्य; विश्वास मध्यम; कोई पाठ-चिह्न नहीं। ‘द्वादशक’ = बारह का समूह (डेटा की टिप्पणी); ‘अंगुल’ समझा जाता है, माप का प्रकार "
           "नहीं कहा। सन्धि जाँची: स्तन + अन्तरम् → स्तनान्तरम् (अ + अ → आ); व्यंजन स से पहले अन्तिम म् → ं (द्वादशकं)। छपा ‘अंतर’ = "
           "अन्तर (त से पहले ं = न्)। अंग्रेज़ी अनुवाद ‘is a set of twelve’ शब्दशः है।"),
    "81": ("गद्य; विश्वास मध्यम; कोई पाठ-चिह्न नहीं। पर्यन्त = सीमा, छोर; स्तन का अपना विस्तार या किनारे का क्षेत्र, यह पाठ नहीं "
           "बताता, इसलिए इस पर प्रश्न नहीं। सन्धि जाँची: द्वि + अङ्गुलः → द्व्यङ्गुलः (इ + भिन्न स्वर → य्)। छपा ‘पर्यंतः’ = पर्यन्तः।"),
    "82": ("गद्य; विश्वास उच्च; कोई पाठ-चिह्न नहीं। दूसरे माप (द्वादशोत्सेधम्) में ‘अंगुल’ समझा जाता है; घेरा नहीं दिया। सन्धि जाँची: "
           "चतुर्विंशति + अङ्गुल → चतुर्विंशत्यङ्गुल (इ + भिन्न स्वर → य्); द्वादश + उत्सेधम् → द्वादशोत्सेधम् (अ + उ → ओ); द्वादशोत्सेधम् + "
           "उरः → द्वादशोत्सेधमुरः (स्वर से पहले म् जुड़ता है); व्यंजन द से पहले अन्तिम म् → ं (-विशालं)। उरः = उरस्, नपुंसक।"),
    "83": ("गद्य; विश्वास उच्च; कोई पाठ-चिह्न नहीं। हृदय = दिल (मानक); माप का प्रकार नहीं बताया। सन्धि जाँची: द्वि + अङ्गुलम् → "
           "द्व्यङ्गुलम् (इ + भिन्न स्वर → य्); व्यंजन ह से पहले अन्तिम म् → ं (द्व्यंगुलं)। पंक्ति के अन्त का ‘हृदयं’ अनुस्वार छपाई की आदत है।"),
    "84": ("गद्य; विश्वास मध्यम; कोई पाठ-चिह्न नहीं। ‘अष्टकौ’ पुल्लिंग द्विवचन है और केवल ‘स्कन्धौ’ से मेल खाता है; काँखों का वही माप "
           "‘च’ से समझा जाता है (डेटा की टिप्पणी)। कक्ष = काँख (मानक)। व्याकरण-लेबल में ‘कक्षे’ का लिंग नहीं दिया गया; पुल्लिंग कक्ष का "
           "द्विवचन ‘कक्षौ’ होता, इसलिए ‘कक्षे’ स्त्रीलिंग (कक्षा) या नपुंसक द्विवचन है। कोई सन्धि नहीं (औ + व्यंजन अपरिवर्तित)। "
           "छपा ‘स्कंधौ’ = स्कन्धौ।"),
    "85": ("गद्य; विश्वास कम। पाठ-चिह्न (सम्भव): छपा ‘षड्डावंसौ’ नियमित रूप नहीं; कार्ड ८४, ८६, ८७ (छपी पंक्ति ९८, १००, १०१) के "
           "द्विवचन -क रूपों के आधार पर ‘षट्कौ अंसौ’ = ‘षट्कावंसौ’ (स्कैन में ट्क/ड्ड की भूल) केवल अनुमान है; इस पर प्रश्न नहीं। ‘छः’ "
           "और ‘अंसौ’ लगभग पक्के, बीच के अक्षर नहीं। अंस = कंधा या कंधे का जोड़ (सम्भावित); स्कन्ध (कार्ड ८४) से भेद नहीं बताया। "
           "औ + स्वर → आव् का नियम कार्ड ७४ के छपे ‘मुष्कमेंढ्रावष्ट-’ में दिखता है।"),
    "86": ("गद्य; विश्वास मध्यम; कोई पाठ-चिह्न नहीं। प्रबाहु: कुछ कोश ‘अग्रबाहु’, कुछ ऊपरी अंग का भाग देते हैं; पहचान विवादित, "
           "संस्कृत शब्द रखा गया, इस पर प्रश्न नहीं। ‘अंगुल’ समझा जाता है। ‘प्रबाहू’ = उकारान्त पुल्लिंग प्रथमा द्विवचन; कोई सन्धि नहीं।"),
    "87": ("गद्य; विश्वास मध्यम; कोई पाठ-चिह्न नहीं। प्रपाणि अस्पष्ट: डेटा के अनुसार पन्द्रह हाथ के बारह (कार्ड ८८, छपी पंक्ति १०२) "
           "से अधिक है, इसलिए बाँह का भाग सम्भव, पर निश्चित नहीं; पहचान विवादित, इस पर प्रश्न नहीं। ‘अंगुल’ समझा जाता है। छपा ‘पंच’ "
           "= पञ्च (च से पहले ं = ञ्)। ‘प्रपाणी’ = इकारान्त पुल्लिंग प्रथमा द्विवचन।"),
}

# ================================================================ AIDS
AIDS = {
    "75": {
        "chunks": "दशांगुलं | बस्तिशिरः",
        "sandhi": ("अ + अ → आ: दश + अङ्गुलम् → दशाङ्गुलम् · व्यंजन ब से पहले अन्तिम म् → ं: दशाङ्गुलम् + बस्ति- → "
                   "दशांगुलं बस्ति- (छपाई में बिना जगह)।"),
        "frame": "कौन: बस्तिशिरः (मूत्राशय का शिर) → कितना: दशाङ्गुलम् (दस अंगुल) → कौन-सा माप: नहीं कहा गया।",
        "pegs": "दस अंगुल = दोनों हाथों की दसों अंगुलियाँ, बस्ति के शिर पर रखी हुई। (मेरा बनाया स्मरण-चित्र)",
    },
    "76": {
        "frame": "कौन: उदरम् (पेट, अंग; रोग नहीं) → कितना: द्वादशाङ्गुलम् (बारह अंगुल) → कौन-सा माप: नहीं कहा गया।",
        "sandhi": ("अ + अ → आ: द्वादश + अङ्गुलम् → द्वादशाङ्गुलम् · स्वर से पहले म् जुड़ता है: द्वादशाङ्गुलम् + उदरम् → "
                   "द्वादशाङ्गुलमुदरम्।"),
        "pegs": "पेट पर घड़ी का गोल चेहरा, बारह अंकों वाला: बारह अंगुल का उदर। (मेरा बनाया स्मरण-चित्र)",
    },
    "77": {
        "chunks": "दश विस्तारे | द्वादशायामे | पार्श्वे",
        "diagram": {"groups": [
            {"label": "पार्श्वे (दोनों बगल)", "items": ["दश विस्तारे: चौड़ाई में दस", "द्वादशायामे: लम्बाई में बारह"]}]},
        "contrast": "विस्तार (चौड़ाई) दस ⇄ आयाम (लम्बाई) बारह: दोनों इसी इकाई में, एक ही अंग पार्श्व के।",
        "sandhi": "अ + आ → आ: द्वादश + आयामे → द्वादशायामे।",
    },
    "78": {
        "chunks": "द्वादशोत्सेधं | त्रिकं",
        "sandhi": "अ + उ → ओ: द्वादश + उत्सेधम् → द्वादशोत्सेधम् · व्यंजन त से पहले अन्तिम म् → ं: द्वादशोत्सेधं त्रिकं।",
        "pegs": "‘त्रिक’ में ‘त्रि’ (तीन): तीन को चार गुना करो, बारह। (मेरा बनाया स्मरण-सूत्र; पाठ ऐसा नहीं कहता)",
    },
    "79": {
        "chunks": "अष्टादशोत्सेधं | पृष्ठं",
        "frame": "कौन: पृष्ठम् (पीठ) → कौन-सा माप: उत्सेध (ऊँचाई) → कितना: अष्टादश (अठारह) → इकाई: अंगुल (समझा गया)।",
        "sandhi": "अ + उ → ओ: अष्टादश + उत्सेधम् → अष्टादशोत्सेधम् · व्यंजन प से पहले अन्तिम म् → ं: अष्टादशोत्सेधं पृष्ठं।",
        "pegs": "अष्टादश = आठ और दस: पीठ पर आठ और दस की दो पट्टियाँ। (मेरा बनाया स्मरण-चित्र)",
    },
    "80": {
        "chunks": "द्वादशकं | स्तनांतरं",
        "frame": "कौन: स्तनान्तरम् (स्तनों के बीच का अन्तर) → कितना: द्वादशकम् (बारह का समूह) → इकाई: अंगुल (समझा गया)।",
        "sandhi": "अ + अ → आ: स्तन + अन्तरम् → स्तनान्तरम् · व्यंजन स से पहले अन्तिम म् → ं: द्वादशकं स्तनांतरं।",
    },
    "81": {
        "chunks": "द्व्यंगुलः | स्तनपर्यंतः",
        "sandhi": "इ + भिन्न स्वर → य्: द्वि + अङ्गुलः → द्व्यङ्गुलः।",
        "frame": "कौन: स्तनपर्यन्तः (स्तन का छोर) → कितना: द्व्यङ्गुलः (दो अंगुल, पुल्लिंग)।",
        "pegs": "‘द्वि’ = दो: छोर पर दो अंगुलियाँ टिकी हुईं। (मेरा बनाया स्मरण-चित्र)",
    },
    "82": {
        "chunks": "चतुर्विंशत्यंगुलविशालं | द्वादशोत्सेधमुरः",
        "diagram": {"groups": [
            {"label": "उरः (छाती)", "items": ["चतुर्विंशत्यङ्गुलविशालम्: चौबीस अंगुल चौड़ी", "द्वादशोत्सेधम्: ऊँचाई में बारह"]}]},
        "contrast": "विशाल (चौड़ाई) चौबीस ⇄ उत्सेध (ऊँचाई) बारह: दोनों इसी इकाई में, एक ही अंग उरस् के।",
        "sandhi": ("इ + भिन्न स्वर → य्: चतुर्विंशति + अङ्गुल → चतुर्विंशत्यङ्गुल · अ + उ → ओ: द्वादश + उत्सेधम् → "
                   "द्वादशोत्सेधम् · स्वर से पहले म् जुड़ता है: द्वादशोत्सेधम् + उरः → द्वादशोत्सेधमुरः।"),
    },
    "83": {
        "chunks": "द्व्यंगुलं | हृदयं",
        "sandhi": "इ + भिन्न स्वर → य्: द्वि + अङ्गुलम् → द्व्यङ्गुलम् · व्यंजन ह से पहले अन्तिम म् → ं: द्व्यंगुलं हृदयं।",
        "anchors": "द्वि + अङ्गुल, लिंग अपने संज्ञा-शब्द से: पर्यन्तः (पुं.) के साथ द्व्यङ्गुलः, हृदयम् (नपुं.) के साथ द्व्यङ्गुलम्। (मेरी याद-पद्धति)",
    },
    "84": {
        "chunks": "अष्टकौ | स्कंधौ | कक्षे च",
        "frame": ("कितना: अष्टकौ (आठ का समूह, पुं. द्विवचन) → किसका: स्कन्धौ (दोनों कंधे) → और: कक्षे च (दोनों काँख; माप ‘च’ से "
                  "समझा गया)।"),
        "diagram": {"groups": [
            {"label": "अष्टकौ: आठ के", "items": ["स्कन्धौ: दोनों कंधे (रूप से मेल)", "कक्षे च: दोनों काँख (‘च’ से समझा गया)"]}]},
    },
    "85": {
        "contrast": "लगभग पक्का: अंसौ (दो अंस) और संख्या छः ⇄ अनिश्चित: छपे ‘षड्डा-’ के बीच के अक्षर। दोनों इसी इकाई में।",
        "anchors": "पक्का भाग याद रखो: छः, दो अंस। धुँधला भाग: बीच के अक्षर, उस पर कोई प्रश्न नहीं। (मेरी याद-पद्धति)",
        "sandhi": "औ + स्वर → आव्: -मेढ्रौ + अष्ट- → -मेढ्रावष्ट- (कार्ड ७४ में छपा)।",
    },
    "86": {
        "chunks": "षोडशकौ | प्रबाहू",
        "frame": "कितना: षोडशकौ (सोलह का समूह, पुं. द्विवचन) → किसका: प्रबाहू (भुजा का एक भाग, पहचान विवादित)।",
        "anchors": "बाहु → बाहू, प्रबाहु → प्रबाहू: उकारान्त पुल्लिंग, प्रथमा द्विवचन -ऊ। (मेरी याद-पद्धति)",
    },
    "87": {
        "chunks": "पंचदशकौ | प्रपाणी",
        "frame": "कितना: पञ्चदशकौ (पन्द्रह का समूह, पुं. द्विवचन) → किसका: प्रपाणी (हाथ या बाँह का एक भाग, पहचान विवादित)।",
        "anchors": "पाणि → पाणी, प्रपाणि → प्रपाणी: इकारान्त पुल्लिंग, प्रथमा द्विवचन -ई; छपा पंच = पञ्च। (मेरी याद-पद्धति)",
    },
}

# ================================================================ IMAGE_SPECS
IMAGE_SPECS = {
    ("77", "diagram"): {
        "file": "sh8-parshva-77.svg",
        "alt": "Table of card 77: the two flanks (pārśva), breadth ten and length twelve (aṅgula understood).",
        "type": "table",
        "title": "कार्ड ७७: दोनों पार्श्व",
        "heads": ["माप", "संख्या"],
        "rows": [["विस्तार: चौड़ाई", "दश (१०)"], ["आयाम: लम्बाई", "द्वादश (१२)"]],
    },
    ("82", "diagram"): {
        "file": "sh8-uras-82.svg",
        "alt": "Table of card 82: the chest (uras), breadth twenty-four aṅgulas and height twelve.",
        "type": "table",
        "title": "कार्ड ८२: उरस् (छाती)",
        "heads": ["माप", "संख्या"],
        "rows": [["विशाल: चौड़ाई", "चतुर्विंशति (२४)"], ["उत्सेध: ऊँचाई", "द्वादश (१२)"]],
    },
    ("84", "diagram"): {
        "file": "sh8-skandha-84.svg",
        "alt": ("Flowchart of card 84: of eight goes with the two shoulders (agreement in form); the two armpits share "
                "it through 'and' (understood)."),
        "type": "mermaid",
        "code": ("flowchart TD\n"
                 "  A[\"अष्टकौ: आठ के\"] --> B[\"स्कन्धौ: दोनों कंधे\"]\n"
                 "  A -. \"च से समझा गया\" .-> C[\"कक्षे: दोनों काँख\"]\n"),
    },
    ("85", "contrast"): {
        "file": "sh8-amsa-85.svg",
        "alt": ("Split of card 85: fairly sure, the two aṃsa (probably shoulder-joints) and the numeral six; uncertain, "
                "the middle syllables of the printed ṣaḍḍā-."),
        "type": "split",
        "title": "कार्ड ८५: पक्का और अनिश्चित",
        "cols": [["लगभग पक्का", ["अंसौ: दो अंस", "सम्भावित: कंधे के जोड़", "संख्या: छः"]],
                 ["अनिश्चित", ["छपा: षड्डावंसौ", "बीच के अक्षर", "कोई प्रश्न नहीं"]]],
    },
}
