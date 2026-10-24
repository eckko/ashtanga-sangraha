from helpers import mcq, match, order, fill, multi, accepts


def T(q, teaches):
    q["teaches"] = teaches
    return q


AUTHORED = {}

# ---------------------------------------------------------------- unit 81
AUTHORED["81"] = {
    "title": "ततः पुष्पदर्शने",
    "question": "What does unit 81 say a woman should keep to for three nights from the first day of menstruation?",
    "rule": ("From the first day the flower (puṣpa: the menstrual flow) is seen, she should remain chaste (brahmacāriṇī), "
             "without bathing and ornaments, sleeping on a spread of darbha grass, for three nights."),
    "limits": ("The woman is not named in the line; she is understood from the context. Darbha is a sacred grass, usually "
               "taken as kuśa (Desmostachya bipinnata), but some sources give Imperata cylindrica: the identity is disputed, "
               "so no question rests on it. The unit gives no reason for these rules."),
    "explain_hi": ("यहाँ से रजस्वला की चर्या आरम्भ होती है। ‘पुष्प’ (फूल) मासिक स्राव का सामान्य शब्द है, और ‘पुष्पदर्शन’ यानी "
                   "रजोदर्शन, स्राव का पहली बार दिखना (मानक अर्थ)। उस पहले दिन से वह तीन रात तक ब्रह्मचारिणी रहे, "
                   "स्नान और अलंकार न करे, और दर्भ के बिछौने पर सोए। दर्भ एक पवित्र घास है, प्रायः कुश मानी जाती है, "
                   "पर उसकी पहचान विवादित है। स्त्री का नाम पंक्ति में नहीं है, वह प्रसंग से समझी जाती है।"),
    "hook": "पुष्प दिखा: तीन रात ब्रह्मचर्य, न स्नान न अलंकार, दर्भ पर शयन।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 81, for how long does she keep these rules?",
            ("For three nights", "त्रिरात्रम् आसीत: she should remain so for three nights."),
            [("For seven nights", "Seven nights (सप्तरात्रम्) are named in unit 86, not here."),
             ("For one full day", "The unit counts three nights from the first day."),
             ("For a whole month", "No month is named in this unit.")],
            "From the first day the flower is seen, she remains so for three nights (त्रिरात्रम्).",
            "त्रिरात्र = three nights."),
        order(1, "Put these phrases of unit 81 in their printed order.",
              ["ततः पुष्पदर्शने", "प्रथमदिवसात्प्रभृति", "ब्रह्मचारिणी", "स्नानालंकाररहिता", "दर्भसंस्तरशायिनी",
               "त्रिरात्रमासीत"],
              "When the flower is seen, from the first day on, chaste, without bath and ornament, sleeping on darbha, "
              "she should remain so for three nights.",
              "When → from when → three marks of her conduct → how long.", role="warmup"),
        match(2, "Match each word of unit 81 to its meaning on the card.",
              [["पुष्पदर्शन", "the sight of the flower (onset of menses)"], ["ब्रह्मचारिणी", "a woman keeping chastity"],
               ["रहिता", "without"], ["संस्तर", "a spread (to lie on)"], ["आसीत", "should remain"]],
              "These five words carry the time, the conduct and the verb of the unit.",
              "पुष्पदर्शन, ब्रह्मचारिणी, रहिता, संस्तर, आसीत.", role="extend",
              teaches="In this chapter पुष्प (flower) is the usual word for the menstrual flow; पुष्पदर्शन is its first sight."),
        mcq("discriminate", 3, "Which split of स्नानालंकाररहिता is right?",
            ("स्नान + अलंकार + रहिता", "अ + अ → आ: स्नान + अलंकार gives स्नानालंकार."),
            [("स्नानाल + कार + रहिता", "स्नानाल and कार are not words of the card."),
             ("स्नानम् + अलंकार + रहिता", "म् before a vowel would give स्नानमलंकार."),
             ("स्नाने + अलंकार + रहिता", "ए + अ would give स्नानेऽलंकार, not स्नानालंकार.")],
            "स्नान (bathing) + अलंकार (ornament) + रहिता (without).",
            "अ + अ → आ."),
        multi("apply", 4, "Which belong to the three-night rule of unit 81?",
              [("Bathing in cold water", "The cold-water bath comes on the fourth day, in unit 84."),
               ("Sleeping on a spread of darbha grass", "Right: दर्भसंस्तरशायिनी."),
               ("Wearing white garlands", "White garlands belong to the fourth day, in unit 84."),
               ("Going without bath and ornaments", "Right: स्नानालंकाररहिता.")],
              [1, 3],
              "For three nights she is chaste, without bath and ornaments, and sleeps on darbha.",
              "ब्रह्मचारिणी, स्नानालंकाररहिता, दर्भसंस्तरशायिनी."),
        T(mcq("transfer", 5, "Built like त्रिरात्रम् आसीत (remains for three nights), what does an invented मासम् अधीते say?",
              ("He studies for a month", "The accusative मासम् gives the length of time, like त्रिरात्रम्."),
              [("He studies from the month on", "'From' would need the ablative, like दिवसात्."),
               ("He studies in the month's end", "No end is named; मासम् gives a span of time."),
               ("He studies the month's lesson", "No lesson is named; मासम् gives a span of time.")],
              "त्रिरात्रम् = for three nights; मासम् = for a month.",
              "Time word in the accusative = for how long."),
          "A time word in the accusative (त्रिरात्रम्, मासम्) tells for how long something goes on."),
    ],
}

# ---------------------------------------------------------------- unit 82
AUTHORED["82"] = {
    "title": "पर्णशरावकरतलान्यतमे",
    "question": "What does unit 82 say she should eat, from what, and for what purpose?",
    "rule": ("In one of the two, a leaf-bowl or the palm of the hand, she should eat a little yāvaka (probably a barley "
             "preparation) cooked with milk, for thinning (karśana)."),
    "limits": ("Yāvaka as a preparation of yava (barley) is probable; the word can also mean lac, which does not suit "
               "eating. The woman is understood from unit 81. The printed यावकंपयसा is two words printed without a space. "
               "No amount beyond 'a little' is given."),
    "explain_hi": ("यह रजस्वला-चर्या का अगला नियम है; स्त्री इकाई ८१ से समझी जाती है। वह पत्ते के दोने या हथेली, इन दोनों में से "
                   "किसी एक में, दूध के साथ पकाया हुआ थोड़ा यावक खाए। यावक सम्भवतः यव (जौ) से बनी वस्तु है; यह पहचान "
                   "सम्भावित है। उद्देश्य ‘कर्शन’ है, यानी शरीर को कृश (दुबला) करना। मात्रा केवल ‘अल्प’ कही गई है।"),
    "hook": "पत्ते या हथेली में, दूध-पका थोड़ा यावक: कृश करने के लिए।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 82, what is she to eat?",
            ("A little yāvaka cooked with milk", "यावकं पयसा सिद्धम् अल्पम्."),
            [("Much rice cooked with ghee", "Neither rice nor ghee is named; the amount is a little."),
             ("Meat broth with sour fruit", "Neither is named in this unit."),
             ("Fresh fruit mixed with honey", "Neither is named in this unit.")],
            "She eats a little yāvaka (probably a barley preparation) cooked with milk.",
            "पयसा सिद्धम् = cooked with milk; अल्पम् = a little."),
        order(1, "Put these words of unit 82 in their printed order.",
              ["पर्णशरावकरतलान्यतमे", "यावकम्", "पयसा सिद्धम्", "अल्पम्", "कर्शनार्थम्", "अश्नीयात्"],
              "In a leaf-bowl or palm, yāvaka, cooked with milk, a little, for thinning, she should eat.",
              "Vessel → food → cooked with milk → amount → purpose → verb.", role="warmup"),
        match(2, "Match each word of unit 82 to its meaning on the card.",
              [["पर्णशराव", "leaf-bowl"], ["करतल", "palm of the hand"], ["पयस्", "milk"], ["अल्प", "a little"],
               ["कर्शन", "thinning, making lean"]],
              "Two words give the vessel, one the liquid, one the amount and one the aim.",
              "पर्णशराव, करतल, पयस्, अल्प, कर्शन.", role="extend",
              teaches="कर्शन (making lean, thinning) names the aim of this food."),
        mcq("discriminate", 3, "Which split of करतलान्यतमे is right?",
            ("करतल + अन्यतमे", "अ + अ → आ: करतल + अन्यतमे gives करतलान्यतमे."),
            [("करतला + न्यतमे", "न्यतमे is not a word of the card."),
             ("करतलम् + अन्यतमे", "म् before a vowel would give करतलमन्यतमे."),
             ("करतले + अन्यतमे", "ए + अ would give करतलेऽन्यतमे.")],
            "करतल (palm of the hand) + अन्यतमे (in one of them).",
            "अ + अ → आ."),
        multi("apply", 4, "By unit 82, in what may she eat it?",
              [("A bronze dish", "No metal vessel is named in this unit."),
               ("A leaf-bowl", "Right: पर्णशराव."),
               ("A clay pot", "No pot is named; the two are a leaf-bowl and the palm."),
               ("The palm of the hand", "Right: करतल.")],
              [1, 3],
              "अन्यतमे: in either one of the two, a leaf-bowl or the palm of the hand.",
              "पर्णशराव or करतल."),
        T(mcq("transfer", 5, "Built like कर्शनार्थम् (for thinning), what does an invented धनार्थं गच्छति say?",
              ("He goes for the sake of wealth", "-अर्थम् at the end = for the sake of, as in कर्शनार्थम्."),
              [("He goes along with his wealth", "'With' would need an instrumental, धनेन."),
               ("He goes away from his wealth", "'From' would need the ablative, धनात्."),
               ("He goes and gives his wealth", "No giving is named; -अर्थम् means for the sake of.")],
              "कर्शनार्थम् = for the purpose of thinning; धनार्थम् = for the sake of wealth.",
              "X + अर्थम् = for the sake of X."),
          "X + अर्थम् at the end of a compound means for the sake of X, for the purpose of X."),
    ],
}

# ---------------------------------------------------------------- unit 83
AUTHORED["83"] = {
    "title": "तीक्ष्णोष्णाम्ललवणानि वर्जयेत्",
    "question": "Which four kinds of things does unit 83 tell her to avoid?",
    "rule": "She should avoid sharp (pungent), hot, sour and salty (things).",
    "limits": ("The noun (food) and the woman (of unit 81) are understood, not printed. The unit gives no reason and no "
               "length of time; it names only these four."),
    "explain_hi": ("चर्या का तीसरा नियम एक छोटी गद्य-पंक्ति है: तीखे, गरम, खट्टे और नमकीन को त्याग दे। "
                   "ये चार गुण एक द्वन्द्व समास में हैं: तीक्ष्ण, उष्ण, अम्ल, लवण। कौन-सी वस्तुएँ, यह नहीं छपा; आहार समझा जाता है। "
                   "स्त्री इकाई ८१ की ही है। कारण या अवधि यहाँ नहीं बताए गए।"),
    "hook": "तीखा, गरम, खट्टा, नमकीन: चारों छोड़ो।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 83, what should she avoid?",
            ("Sharp, hot, sour and salty things", "तीक्ष्ण-उष्ण-अम्ल-लवणानि वर्जयेत्."),
            [("Sweet, cold, bitter and oily things", "None of these four is named in this unit."),
             ("Milk, ghee, honey and barley food", "None is named here; yāvaka with milk is to be eaten (unit 82)."),
             ("Baths, ornaments and soft beds", "Those belong to the three-night rule of unit 81.")],
            "She should avoid sharp, hot, sour and salty (things).",
            "वर्जयेत् = should avoid."),
        order(1, "Put the four qualities of unit 83 in their printed order.",
              ["तीक्ष्ण", "उष्ण", "अम्ल", "लवण"],
              "The compound runs: sharp, hot, sour, salty.",
              "तीक्ष्ण → उष्ण → अम्ल → लवण.", role="warmup"),
        match(2, "Match each word of unit 83 to its meaning on the card.",
              [["तीक्ष्ण", "sharp, pungent"], ["उष्ण", "hot"], ["अम्ल", "sour"], ["लवण", "salty"],
               ["वर्जयेत्", "should avoid"]],
              "Four qualities and one verb make the whole unit.",
              "तीक्ष्ण, उष्ण, अम्ल, लवण, वर्जयेत्.", role="extend",
              teaches="The four are joined in one dvandva compound, तीक्ष्णोष्णाम्ललवणानि: sharp, hot, sour and salty (ones)."),
        mcq("discriminate", 3, "Which split of तीक्ष्णोष्णाम्ल is right?",
            ("तीक्ष्ण + उष्ण + अम्ल", "अ + उ → ओ (तीक्ष्णोष्ण); अ + अ → आ (उष्णाम्ल)."),
            [("तीक्ष्णो + ष्ण + अम्ल", "ष्ण is not a word."),
             ("तीक्ष्णम् + उष्ण + अम्ल", "म् before a vowel would give तीक्ष्णमुष्ण."),
             ("तीक्ष्ण + ओष्ण + अम्ल", "ओष्ण is not a word of the card; the word is उष्ण.")],
            "तीक्ष्ण (sharp) + उष्ण (hot) + अम्ल (sour).",
            "अ + उ → ओ; अ + अ → आ."),
        mcq("apply", 4, "Which of these does unit 83 tell her to avoid?",
            ("Something sour (अम्ल)", "अम्ल is the third of the four."),
            [("Something sweet (मधुर)", "मधुर is not in the list."),
             ("Something bitter (तिक्त)", "तिक्त is not in the list."),
             ("Something cold (शीत)", "शीत is not in the list; hot (उष्ण) is.")],
            "Only sharp, hot, sour and salty are named.",
            "The list: तीक्ष्ण, उष्ण, अम्ल, लवण."),
        T(mcq("transfer", 5, "By the rule of तीक्ष्णोष्ण, how is शीत + उष्ण written when joined?",
              ("शीतोष्ण", "अ + उ → ओ, as in तीक्ष्ण + उष्ण."),
              [("शीतौष्ण", "अ + उ gives ओ, not औ."),
               ("शीतुष्ण", "The अ cannot simply vanish."),
               ("शीतवुष्ण", "No व् is put in after अ.")],
              "तीक्ष्ण + उष्ण → तीक्ष्णोष्ण; so शीत + उष्ण → शीतोष्ण (cold and hot).",
              "अ + उ → ओ."),
          "अ or आ before उ or ऊ merges into ओ."),
    ],
}

# ---------------------------------------------------------------- unit 84
AUTHORED["84"] = {
    "title": "चतुर्थेऽहन्युद्वर्तिता",
    "question": "How does unit 84 say she is prepared on the fourth day, and with what mind does she look upon her husband?",
    "rule": ("On the fourth day, rubbed with powder, bathed in cold water, anointed, adorned, in white garlands and garments, "
             "with auspicious rites done, her mind on no other, she should look upon a husband of this kind."),
    "limits": ("'Of just this kind' (evaṃvidha) points back to a description that is not in this unit, so the card states no "
               "quality of the husband. Udvartitā as 'rubbed with unguent powder' is the probable sense. The printed "
               "कृतमंगलस्वस्त्ययनैवंविधमेव is three words printed together (no letter wrong)."),
    "explain_hi": ("चौथे दिन चर्या बदल जाती है। स्त्री उबटन लगाई हुई (उद्वर्तन, सम्भावित अर्थ), ठण्डे जल से नहाई, लेप लगाई, "
                   "अलंकृत, श्वेत माला और वस्त्र वाली, मंगल और स्वस्त्ययन कर चुकी हो। उसका मन किसी अन्य पर न हो "
                   "(अनन्यमनाः), और वह ठीक इसी प्रकार के पति को देखे। ‘एवंविध’ किसी ऐसे वर्णन की ओर संकेत है जो इस इकाई में "
                   "नहीं है, इसलिए पति के गुण यहाँ नहीं कहे गए। इकाई ८१ में स्नान और अलंकार वर्जित थे; अब चौथे दिन दोनों हैं।"),
    "hook": "चौथा दिन: उबटन, ठण्डा स्नान, लेप, अलंकार, श्वेत माला-वस्त्र; मन केवल पति पर।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 84, on which day is she bathed and adorned?",
            ("On the fourth day", "चतुर्थे अहनि: on the fourth day."),
            [("On the first day", "From the first day she goes without bath (unit 81)."),
             ("On the seventh day", "No seventh day is named in this unit."),
             ("On the twelfth day", "No twelfth day is named in this unit.")],
            "On the fourth day she is rubbed, bathed, anointed and adorned.",
            "चतुर्थ = fourth; अहन् = day."),
        order(1, "Put these marks of her preparation in unit 84 in their printed order.",
              ["उद्वर्तिता", "शीतसलिलस्नाता", "अनुलिप्ता", "अलंकृता", "शुक्लमाल्यांबरा"],
              "Rubbed with powder, bathed in cold water, anointed, adorned, in white garlands and garments.",
              "उद्वर्तिता → स्नाता → अनुलिप्ता → अलंकृता → शुक्लमाल्याम्बरा.", role="warmup"),
        match(2, "Match each word of unit 84 to its meaning on the card.",
              [["उद्वर्तिता", "rubbed with unguent powder"], ["शीतसलिल", "cold water"], ["अनुलिप्ता", "anointed"],
               ["शुक्लमाल्याम्बरा", "with white garlands and garments"], ["अनन्यमनाः", "with the mind on no other"]],
              "Four words describe her preparation; the last describes her mind.",
              "उद्वर्तिता, शीतसलिल, अनुलिप्ता, शुक्लमाल्याम्बरा, अनन्यमनाः.", role="extend",
              teaches="अनन्यमनाः = अन् + अन्य + मनस्: one whose mind is on no other."),
        mcq("discriminate", 3, "Which split of चतुर्थेऽहन्युद्वर्तिता is right?",
            ("चतुर्थे + अहनि + उद्वर्तिता", "ए + अ → एऽ (the अ drops); इ + उ → यु."),
            [("चतुर्थः + अहनि + उद्वर्तिता", "अः + अ would give चतुर्थोऽहनि, with ओ."),
             ("चतुर्थे + हनि + उद्वर्तिता", "हनि is not a word; ऽ marks a dropped अ."),
             ("चतुर्थे + अहन्यु + द्वर्तिता", "द्वर्तिता is not a word of the card.")],
            "चतुर्थे (fourth) + अहनि (on the day) + उद्वर्तिता (rubbed with powder).",
            "ए + अ → एऽ; इ + a different vowel → य् + that vowel."),
        multi("apply", 4, "Which are part of her fourth-day preparation in unit 84?",
              [("Sleeping on a spread of darbha grass", "That is the three-night rule of unit 81."),
               ("White garlands and garments", "Right: शुक्लमाल्याम्बरा."),
               ("Eating a little yāvaka with milk", "That is the food rule of unit 82."),
               ("Auspicious rites and benedictions done", "Right: कृतमंगलस्वस्त्ययना.")],
              [1, 3],
              "On the fourth day she wears white garlands and garments and has the auspicious rites done.",
              "शुक्लमाल्याम्बरा; कृतमंगलस्वस्त्ययना."),
        T(mcq("transfer", 5, "By the rule of पश्येदनन्यमनाः, how is भवेत् + अत्र written when joined?",
              ("भवेदत्र", "त् before a vowel becomes द्."),
              [("भवेत्त्र", "The vowel अ of अत्र cannot vanish."),
               ("भवेतत्र", "Before a vowel the त् becomes द्, not त."),
               ("भवेन्नत्र", "त् becomes न् only before a nasal.")],
              "पश्येत् + अनन्यमनाः → पश्येदनन्यमनाः; so भवेत् + अत्र → भवेदत्र.",
              "Final त् + vowel → द् + vowel."),
          "A final त् before a vowel (or a voiced sound) becomes द्."),
    ],
}

# ---------------------------------------------------------------- unit 85
AUTHORED["85"] = {
    "title": "तदाहि यादृशमेव पश्यति",
    "question": "What does the first line of unit 85 say a woman bears, and why is its second line left open?",
    "rule": ("For then, whatever kind she sees or thinks of, of that kind she bears (a child). The second line's reading is "
             "conjectural and is not used for questions."),
    "limits": ("Low confidence. Line 2 is conjectural: स्नातांत् may be स्नातात् (after the bath) or स्नाताम् (the bathed "
               "woman), and उपेक्षेत may mean 'let pass' or 'abstain from'; undecided, so no question uses line 2. "
               "Line 1 leaves its objects unstated. The sentence seems to run on into units 86-87."),
    "explain_hi": ("पहली पंक्ति कारण बताती है: ‘हि’ यानी क्योंकि, उस समय स्त्री जिस प्रकार के को देखती या सोचती है, वैसे को ही "
                   "जन्म देती है। यादृश और तादृश एक जोड़ा है: जैसा, वैसा। दूसरी पंक्ति का पाठ अनुमानित है: ‘स्नातांत्’ को "
                   "‘स्नातात्’ (स्नान के बाद) या ‘स्नाताम्’ (नहाई हुई स्त्री को) पढ़ा जा सकता है, और ‘उपेक्षेत’ का अर्थ "
                   "‘बीतने दे’ या ‘दूर रहे’ हो सकता है; यह तय नहीं। एक अनुमानित पाठ पर: फिर स्नान के बाद, गुणवान् पुत्र "
                   "चाहने वाला चार रात बीतने दे। यह वाक्य सम्भवतः इकाई ८६-८७ में आगे चलता है।"),
    "hook": "जैसा देखे या सोचे, वैसा ही जने: यादृश, तादृश।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By line 1 of unit 85, what kind does she bear?",
            ("The kind she sees or thinks of", "यादृशम् … पश्यति चिन्तयति वा, तादृशं प्रसूते."),
            [("The kind her mother once was", "No mother is named in the line."),
             ("The kind the physician wishes", "No physician is named in the line."),
             ("The kind that the stars decide", "No stars are named in the line.")],
            "Whatever kind she then sees or thinks of, of that kind she bears.",
            "यादृश … तादृश = of which kind … of that kind."),
        order(1, "Put these words of line 1 of unit 85 in their printed order.",
              ["तदाहि", "यादृशमेव", "पश्यति", "चिंतयति वा", "तादृशं", "प्रसूत इति"],
              "For then, whatever kind, she sees, or thinks of, of that kind, she bears.",
              "तदा हि → यादृशम् एव → पश्यति → चिन्तयति वा → तादृशम् → प्रसूते इति.", role="warmup"),
        match(2, "Match each word of line 1 of unit 85 to its meaning on the card.",
              [["यादृश", "of which kind"], ["तादृश", "of that kind"], ["पश्यति", "she sees"],
               ["चिन्तयति", "she thinks of"], ["प्रसूते", "she bears"]],
              "The pair यादृश … तादृश frames the line; three verbs say what she does.",
              "यादृश, तादृश, पश्यति, चिन्तयति, प्रसूते.", role="extend",
              teaches="यादृश … तादृश is a pair: of which kind … of that kind (as the one, so the other)."),
        mcq("discriminate", 3, "The card reads the printed प्रसूत इति as a verb plus इति. Which joining gives it?",
            ("प्रसूते + इति", "ए before a vowel becomes अय्; the य् drops, leaving प्रसूत इति."),
            [("प्रसूत + इति", "अ + इ would merge into ए: प्रसूतेति."),
             ("प्रसूतम् + इति", "म् before a vowel would give प्रसूतमिति."),
             ("प्रसूता + इति", "आ + इ would merge into ए: प्रसूतेति.")],
            "प्रसूते (she bears) + इति (closing word) → प्रसूत इति.",
            "ए + a vowel → अ(य्) + vowel; the य् is usually dropped."),
        mcq("apply", 4, "By line 1 of unit 85, she then keeps thinking of a strong person. What kind does she bear?",
            ("One of that strong kind", "Whatever kind she thinks of, of that kind (तादृशम्) she bears."),
            [("One of the opposite, weak kind", "The rule is likeness (तादृश), not the opposite."),
             ("One of no fixed kind at all", "The line ties the kind to what she sees or thinks of."),
             ("One like her own father", "No father is named in the line.")],
            "The line ties the kind of child to the kind she sees or thinks of then.",
            "यादृशम् पश्यति चिन्तयति वा, तादृशं प्रसूते."),
        T(mcq("transfer", 5, "An invented line reads यादृशं बीजं तादृशं फलम्. What does it say?",
              ("As the seed is, so is the fruit", "यादृश … तादृश: of which kind … of that kind."),
              [("The seed is better than the fruit", "No better or worse is said."),
               ("The fruit grows without a seed", "The line pairs seed and fruit; it denies neither."),
               ("Seed and fruit differ in kind", "तादृश says of that same kind.")],
              "As यादृशं … तादृशं प्रसूते in unit 85, यादृशं बीजं तादृशं फलम् = as the seed, so the fruit.",
              "यादृश X तादृश Y = Y is of the same kind as X."),
          "यादृश … तादृश pairs two things of the same kind: as the one, so the other."),
    ],
}

# ---------------------------------------------------------------- unit 86
AUTHORED["86"] = {
    "title": "पुष्पेदिनात्सप्तरात्रं",
    "question": "What span does the fragment of unit 86 name, and why is it read with care?",
    "rule": "From the day of the flower (menstruation), seven nights: a fragment without a verb, on a conjectural reading.",
    "limits": ("Low confidence. No verb is printed or supplied. The printed पुष्पे- may be the compound पुष्पदिनात् or "
               "two words, पुष्पे दिनात्; undecided, so no question rests on that form. It seems to go with unit 85 and lead "
               "into unit 87; the purpose of the seven nights is not said."),
    "explain_hi": ("यह छोटा, क्रियाहीन टुकड़ा है: पुष्प (मासिक स्राव) के दिन से सात रात। छपा ‘पुष्पेदिनात्’ या तो समास "
                   "‘पुष्पदिनात्’ है या दो शब्द ‘पुष्पे दिनात्’; यह तय नहीं। ‘दिनात्’ पंचमी है: दिन से। यह टुकड़ा इकाई ८५ की "
                   "बीतने वाली रातों के साथ जुड़ा लगता है और इकाई ८७ की ओर ले जाता है; पर सात रातें किसलिए, यह यहाँ नहीं कहा गया।"),
    "hook": "पुष्प के दिन से सात रात: क्रिया नहीं, केवल गिनती।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "What span of time does unit 86 name?",
            ("Seven nights", "सप्तरात्रम् = seven nights."),
            [("Three nights", "Three nights (त्रिरात्रम्) are named in unit 81."),
             ("Twelve nights", "Twelve is not named in this unit."),
             ("A fortnight", "No fortnight is named in this unit.")],
            "The fragment names seven nights (सप्तरात्रम्), counted from a day (दिनात्).",
            "सप्त = seven; रात्र = night."),
        match(1, "Match each part of unit 86 to its meaning on the card.",
              [["सप्त", "seven"], ["रात्र", "night"], ["दिन", "day"], ["पुष्प", "flower (menstruation)"]],
              "The fragment is made of these four members.",
              "सप्त, रात्र, दिन, पुष्प.", role="warmup"),
        T(mcq("extend", 2, "What does unit 86 lack, as the card reads it?",
              ("A verb: none is printed or supplied", "The note calls it a fragment without a verb."),
              [("A number: no count is given", "सप्त, seven, is a number."),
               ("A time word: none is named", "दिन and रात्र are time words."),
               ("A noun: it has only verbs", "It has no verb; दिन and रात्र are nouns.")],
              "Unit 86 is a fragment with no verb; the card supplies none.",
              "No verb: read the fragment with the units around it."),
          "A fragment without a verb is read with the units around it; the card adds no verb of its own."),
        mcq("discriminate", 3, "Which split of दिनात्सप्तरात्रं is right?",
            ("दिनात् + सप्तरात्रम्", "त् stays त् before the unvoiced स."),
            [("दिना + त्सप्तरात्रम्", "त्सप्तरात्रम् is not a word."),
             ("दिनम् + सप्तरात्रम्", "म् before स would show as an anusvara: दिनं सप्त."),
             ("दिनात्स + अप्तरात्रम्", "Neither part is a word of the card.")],
            "दिनात् (from the day) + सप्तरात्रम् (seven nights).",
            "Final त् stays before an unvoiced consonant such as स."),
        multi("apply", 4, "Which are true of unit 86 as the card reads it?",
              [("It names the eighth night for a son", "That is unit 87."),
               ("It counts seven nights", "Right: सप्तरात्रम्."),
               ("It counts from a day (दिनात्)", "Right: दिनात् is ablative, from the day."),
               ("It tells her to bathe on that day", "No bath is named in this fragment.")],
              [1, 2],
              "The fragment counts seven nights from the day (of the flower).",
              "दिनात् = from the day; सप्तरात्रम् = seven nights."),
        T(mcq("transfer", 5, "Built like दिनात् (from the day), what does an invented ग्रामात् आगच्छति mean?",
              ("He comes from the village", "The ablative -आत् means from, as in दिनात्."),
              [("He comes to the village", "'To' would be an accusative, ग्रामम्."),
               ("He comes in the village", "'In' would be a locative, ग्रामे."),
               ("He comes with the village", "'With' would be an instrumental, ग्रामेण.")],
              "दिनात् = from the day; ग्रामात् = from the village.",
              "-आत् (ablative) = from."),
          "The ablative ending -आत् (दिनात्, ग्रामात्) means from."),
    ],
}

# ---------------------------------------------------------------- unit 87
AUTHORED["87"] = {
    "title": "अथाष्टम्यां दशम्यां द्वादश्यां वा",
    "question": "On which nights does unit 87 say one desiring a son should lie together?",
    "rule": "Then, on the eighth, tenth or twelfth night, one desiring a son (putrakāma) should lie together (saṃviśet).",
    "limits": ("रात्रौ is singular and understood with each ordinal. The object of संविशेत् is not stated. The unit itself "
               "gives no reason for these nights."),
    "explain_hi": ("अब रात्रियों का नियम: पुत्र की कामना वाला आठवीं, दसवीं अथवा बारहवीं रात में सहवास करे। ‘रात्रौ’ एकवचन है और "
                   "हर क्रम-संख्या के साथ समझा जाता है। ‘संविशेत्’ का कर्म नहीं छपा। ‘पुत्रकाम’ बहुव्रीहि है: जिसे पुत्र की "
                   "कामना है। यह इकाई स्वयं कोई कारण नहीं देती।"),
    "hook": "पुत्र चाहे तो: आठवीं, दसवीं, बारहवीं रात।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 87, on which nights should one desiring a son lie together?",
            ("The eighth, tenth or twelfth", "अष्टम्यां दशम्यां द्वादश्यां वा रात्रौ."),
            [("The fifth, seventh or ninth", "Those are for one desiring a daughter, unit 88."),
             ("The eleventh or thirteenth", "Those are not named in this unit."),
             ("The first, second or third", "Those fall in the three nights of unit 81.")],
            "On the eighth, tenth or twelfth night, one desiring a son should lie together.",
            "अष्टमी, दशमी, द्वादशी = eighth, tenth, twelfth."),
        order(1, "Put these words of unit 87 in their printed order.",
              ["अथ", "अष्टम्यां", "दशम्यां", "द्वादश्यां वा", "रात्रौ", "पुत्रकामः संविशेत्"],
              "Then, on the eighth, tenth or twelfth night, one desiring a son should lie together.",
              "अथ → अष्टम्याम् → दशम्याम् → द्वादश्याम् वा → रात्रौ → पुत्रकामः संविशेत्.", role="warmup"),
        match(2, "Match each word of unit 87 to its meaning on the card.",
              [["अष्टमी", "eighth"], ["दशमी", "tenth"], ["द्वादशी", "twelfth"], ["पुत्रकाम", "one desiring a son"],
               ["संविशेत्", "should lie together"]],
              "Three ordinals give the nights; two words give the person and the act.",
              "अष्टमी, दशमी, द्वादशी, पुत्रकाम, संविशेत्.", role="extend",
              teaches="The ordinals are feminine (अष्टम्याम्, दशम्याम्) because they go with रात्रि, night, a feminine noun."),
        mcq("discriminate", 3, "Which split of अथाष्टम्यां is right?",
            ("अथ + अष्टम्याम्", "अ + अ → आ: अथ + अष्टम्याम् gives अथाष्टम्याम्."),
            [("अथा + ष्टम्याम्", "ष्टम्याम् is not a word."),
             ("अथः + अष्टम्याम्", "अः + अ would give अथोऽष्टम्याम्."),
             ("अथम् + अष्टम्याम्", "म् before a vowel would give अथमष्टम्याम्.")],
            "अथ (then) + अष्टम्याम् (on the eighth).",
            "अ + अ → आ."),
        fill(4, "One desiring a son is called ____ in unit 87 (type it in Devanagari or in English letters, e.g. dharma).",
             accepts("पुत्रकामः", None, "पुत्रकाम"),
             "पुत्रकामः संविशेत्: one desiring a son should lie together.",
             "पुत्र (son) + काम (desire): one whose desire is a son.",
             "पुत्रकाम = one desiring a son.", role="apply"),
        T(mcq("transfer", 5, "In an invented phrase धनकामो वणिक् (a merchant), what does धनकामः say of him?",
              ("He desires wealth", "X-काम = one whose desire is X, like पुत्रकाम."),
              [("He has lost wealth", "काम is desire, not loss."),
               ("He gives wealth away", "काम is desire, not giving."),
               ("He is desired for wealth", "The compound names what he desires, not who desires him.")],
              "पुत्रकामः = one desiring a son; धनकामः = one desiring wealth.",
              "X-कामः = one who desires X."),
          "A bahuvrīhi in -काम (पुत्रकाम, धनकाम) describes a person: one whose desire is X."),
    ],
}

# ---------------------------------------------------------------- unit 88
AUTHORED["88"] = {
    "title": "पंचम्यां सप्तम्यां नवम्यां वा",
    "question": "Which nights does unit 88 give for one desiring a daughter?",
    "rule": "On the fifth, seventh or ninth (night), one desiring a daughter (duhitṛkāma); the verb and 'night' come from unit 87.",
    "limits": ("Elliptic: संविशेत् and रात्रौ are carried from unit 87 and are not printed here; no verb is supplied. "
               "The unit gives no reason. It continues unit 87."),
    "explain_hi": ("यह इकाई ८७ का ही आगे का भाग है: पाँचवीं, सातवीं या नवीं (रात) में, पुत्री की कामना वाला। क्रिया ‘संविशेत्’ "
                   "और ‘रात्रौ’ इकाई ८७ से लिए जाते हैं; यहाँ छपे नहीं। ‘दुहितृकाम’ = जिसे दुहिता (पुत्री) की कामना है। "
                   "पुत्र के लिए आठवीं, दसवीं, बारहवीं और पुत्री के लिए पाँचवीं, सातवीं, नवीं: इन दो इकाइयों को साथ याद करें।"),
    "hook": "पुत्री चाहे तो: पाँचवीं, सातवीं, नवीं रात।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 88, which nights are for one desiring a daughter?",
            ("The fifth, seventh or ninth", "पंचम्यां सप्तम्यां नवम्यां वा."),
            [("The eighth, tenth or twelfth", "Those are for one desiring a son, unit 87."),
             ("The fourth, sixth or eighth", "These are not named in this unit."),
             ("The eleventh or thirteenth", "These are not named in this unit.")],
            "On the fifth, seventh or ninth (night), one desiring a daughter.",
            "पञ्चमी, सप्तमी, नवमी = fifth, seventh, ninth."),
        order(1, "Put the words of unit 88 in their printed order.",
              ["पंचम्यां", "सप्तम्यां", "नवम्यां वा", "दुहितृकामः"],
              "Fifth, seventh, or ninth, one desiring a daughter.",
              "पञ्चम्याम् → सप्तम्याम् → नवम्याम् वा → दुहितृकामः.", role="warmup"),
        match(2, "Match each word of unit 88 to its meaning on the card.",
              [["पञ्चमी", "fifth"], ["सप्तमी", "seventh"], ["नवमी", "ninth"], ["दुहितृ", "daughter"], ["काम", "desire"]],
              "Three ordinals give the nights; दुहितृकाम names the person.",
              "पञ्चमी, सप्तमी, नवमी, दुहितृ, काम.", role="extend",
              teaches="दुहितृकाम = one whose desire is a daughter (दुहितृ)."),
        mcq("discriminate", 3, "Unit 88 prints no verb. Where does its verb come from?",
            ("From unit 87: संविशेत्", "The verb and रात्रौ are carried from unit 87."),
            [("From unit 89: भवति", "भवति belongs to the next statement, not to this one."),
             ("From unit 83: वर्जयेत्", "That is the avoidance rule, much earlier."),
             ("It is printed: नवम्यां", "नवम्याम् is an ordinal, not a verb.")],
            "The unit is elliptic: संविशेत् and रात्रौ come from unit 87.",
            "An elliptic line borrows its verb from the line before."),
        mcq("apply", 4, "By unit 88, which of these nights is named for one desiring a daughter?",
            ("The seventh", "सप्तम्याम्: the seventh is one of the three."),
            [("The eighth", "The eighth is a night for a son, unit 87."),
             ("The tenth", "The tenth is a night for a son, unit 87."),
             ("The sixth", "The sixth is not named.")],
            "Only the fifth, seventh and ninth are named for a daughter.",
            "Daughter: पञ्चमी, सप्तमी, नवमी."),
        T(mcq("transfer", 5, "Built like सप्तम्यां (on the seventh), what does an invented तृतीयायां रात्रौ mean?",
              ("On the third night", "Locative ordinal + रात्रौ = on the Nth night."),
              [("Of the third night", "'Of' would need a genitive."),
               ("For three nights long", "That would be त्रिरात्रम्, an accusative of time."),
               ("By three nights' work", "'By' would need an instrumental.")],
              "सप्तम्यां (रात्रौ) = on the seventh night; तृतीयायां रात्रौ = on the third night.",
              "Feminine ordinal in the locative + रात्रौ = on the Nth night."),
          "A feminine ordinal in the locative with रात्रौ (सप्तम्यां रात्रौ, तृतीयायां रात्रौ) means on the Nth night."),
    ],
}

# ---------------------------------------------------------------- unit 89
AUTHORED["89"] = {
    "title": "तासूत्तरोत्तरम्",
    "question": "What does unit 89 say the offspring gains in these nights, and how does it grow?",
    "rule": ("In these (nights), progressively (each later one more), the offspring has the endowment of life-span, "
             "health, lordship, good fortune, strength, complexion and the senses."),
    "limits": ("The unit does not repeat which nights 'these' are, nor whether the count runs over the son's and the "
               "daughter's nights together. Varṇa as complexion is probable (it can also mean colour or class). "
               "No amounts are given."),
    "explain_hi": ("‘तासु’ यानी उन (रातों) में। ‘उत्तरोत्तरम्’ = क्रम से आगे-आगे, हर बाद वाली में अधिक। सन्तान को सात चीज़ों की "
                   "सम्पदा मिलती है: आयु, आरोग्य, ऐश्वर्य, सौभाग्य, बल, वर्ण (त्वचा का रंग; सम्भावित अर्थ) और इन्द्रियाँ। "
                   "‘अपत्यस्य भवति’ = सन्तान की होती है, यानी सन्तान को मिलती है। कौन-सी रातें, और गिनती कैसे चलती है, "
                   "यह इकाई दोहराती नहीं।"),
    "hook": "इन रातों में जितनी आगे, सन्तान की सम्पदा उतनी अधिक: आयु से इन्द्रिय तक सात।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 89, how does the offspring's endowment go across these nights?",
            ("Each later night gives more", "उत्तरोत्तरम्: each later one more."),
            [("Each later night gives less", "Decrease (ह्रास) comes after these, in unit 90."),
             ("Every night gives the same", "उत्तरोत्तरम् says each later one is more."),
             ("The first night gives most", "The order runs upward: each later one more.")],
            "In these nights, progressively, the offspring has more of the endowment.",
            "उत्तरोत्तरम् = each later one more."),
        order(1, "Put these items of the endowment in unit 89 in their printed order.",
              ["आयुः", "आरोग्य", "ऐश्वर्य", "सौभाग्य", "बल", "वर्ण"],
              "Life-span, health, lordship, good fortune, strength, complexion (then the senses).",
              "आयु → आरोग्य → ऐश्वर्य → सौभाग्य → बल → वर्ण → इन्द्रिय.", role="warmup"),
        match(2, "Match each word of unit 89 to its meaning on the card.",
              [["आयुस्", "life-span"], ["आरोग्य", "health"], ["ऐश्वर्य", "lordship, prosperity"],
               ["सौभाग्य", "good fortune"], ["अपत्य", "offspring"]],
              "Four items of the list and the one who receives them.",
              "आयुस्, आरोग्य, ऐश्वर्य, सौभाग्य, अपत्य.", role="extend",
              teaches="अपत्यस्य भवति: (the endowment) is the offspring's; the genitive shows who has it."),
        mcq("discriminate", 3, "Which split of आयुरारोग्य is right?",
            ("आयुः + आरोग्य", "Visarga after उ becomes र् before a vowel."),
            [("आयु + रारोग्य", "रारोग्य is not a word."),
             ("आयुम् + आरोग्य", "म् before a vowel would give आयुमारोग्य."),
             ("आयू + आरोग्य", "ऊ + आ would give आय्वारोग्य, with व्.")],
            "आयुः (life-span) + आरोग्य (health).",
            "Visarga after a vowel other than अ/आ → र् before a vowel."),
        multi("apply", 4, "Which are named in the endowment of unit 89?",
              [("Wisdom (बुद्धि)", "बुद्धि is not named in the list."),
               ("Strength (बल)", "Right: बल is in the list."),
               ("Learning (विद्या)", "विद्या is not named in the list."),
               ("The sense faculties (इन्द्रिय)", "Right: इन्द्रिय closes the list.")],
              [1, 3],
              "The list: life-span, health, lordship, good fortune, strength, complexion, senses.",
              "आयुस्, आरोग्य, ऐश्वर्य, सौभाग्य, बल, वर्ण, इन्द्रिय."),
        T(mcq("transfer", 5, "By the rule of आयुरारोग्य, how is धनुः + आदाय written when joined?",
              ("धनुरादाय", "Visarga after उ → र् before the vowel आ."),
              [("धनुआदाय", "The visarga after उ does not simply drop before a vowel."),
               ("धनुसादाय", "Before a vowel the visarga after उ becomes र्, not स्."),
               ("धनोरादाय", "The उ does not change to ओ.")],
              "आयुः + आरोग्य → आयुरारोग्य; so धनुः + आदाय → धनुरादाय (taking the bow).",
              "उः + vowel → उर् + vowel."),
          "A visarga after उ (or any vowel but अ/आ) becomes र् before a vowel."),
    ],
}

# ---------------------------------------------------------------- unit 90
AUTHORED["90"] = {
    "title": "अतः परं तूत्तरोत्तरमेव",
    "question": "What does unit 90 say happens after this to life-span and the rest?",
    "rule": "But after this there is, progressively, a decrease (hrāsa) of life-span and the rest (the list of unit 89).",
    "limits": ("The copula is understood. The unit does not say from which night exactly 'after this' begins, and gives no "
               "amount. 'And the rest' (ādi) points back to the list of unit 89, which this unit follows."),
    "explain_hi": ("यह इकाई ८९ के ठीक बाद आती है और उसका उलटा पक्ष बताती है। ‘अतः परम्’ = इसके आगे, ‘तु’ = किन्तु। "
                   "आगे उत्तरोत्तर (क्रम से हर बाद वाले में) आयु आदि का ह्रास, यानी घटना, होता है। ‘आदि’ से इकाई ८९ की "
                   "पूरी सूची समझी जाती है। इसके आगे ठीक किस रात से, यह नहीं कहा गया।"),
    "hook": "इन रातों तक बढ़त, उसके आगे घटत।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 90, what happens to life-span and the rest after this?",
            ("A progressive decrease", "उत्तरोत्तरम् एव … ह्रासः."),
            [("A progressive increase", "Increase is the rule of unit 89, before this."),
             ("No change at any point", "ह्रास, decrease, is stated."),
             ("A sudden end on one night", "The decrease is progressive, not sudden.")],
            "After this, life-span and the rest decrease, each later one more.",
            "ह्रास = decrease."),
        order(1, "Put the parts of unit 90 in their printed order.",
              ["अतः परं", "तूत्तरोत्तरमेव", "आयुरादीनां", "ह्रासः"],
              "After this, but progressively indeed, of life-span and the rest, decrease.",
              "अतः परम् → तु उत्तरोत्तरम् एव → आयुरादीनाम् → ह्रासः.", role="warmup"),
        match(2, "Match each word of unit 90 to its meaning on the card.",
              [["अतः परम्", "after this"], ["तु", "but"], ["आदि", "and the rest"], ["ह्रास", "decrease"]],
              "These words turn unit 89's growth into a decrease.",
              "अतः परम्, तु, आदि, ह्रास.", role="extend",
              teaches="आयुरादि = life-span and the rest: आदि stands for the remaining items of unit 89's list."),
        mcq("discriminate", 3, "Which split of तूत्तरोत्तरम् is right?",
            ("तु + उत्तरोत्तरम्", "उ + उ → ऊ."),
            [("तू + त्तरोत्तरम्", "त्तरोत्तरम् is not a word."),
             ("ते + उत्तरोत्तरम्", "ए + उ would not give ऊ."),
             ("तत् + उत्तरोत्तरम्", "त् before a vowel would give तदुत्तरोत्तरम्.")],
            "तु (but) + उत्तरोत्तरम् (progressively).",
            "उ + उ → ऊ."),
        mcq("apply", 4, "In unit 90, which word shows that the change comes step by step?",
            ("उत्तरोत्तरम्", "Progressively: each later one more."),
            [("ह्रासः", "It names the change, a decrease, not its steps."),
             ("परम्", "It means after."),
             ("आदीनाम्", "It means of the rest.")],
            "उत्तरोत्तरम् makes the decrease progressive.",
            "उत्तरोत्तरम् = progressively."),
        T(mcq("transfer", 5, "By the rule of तूत्तरोत्तरम्, how is साधु + उक्तम् written when joined?",
              ("साधूक्तम्", "उ + उ → ऊ."),
              [("साध्वुक्तम्", "उ becomes व् only before a different vowel."),
               ("साधोक्तम्", "उ + उ does not give ओ."),
               ("साधुउक्तम्", "Two like vowels merge; they are not left side by side.")],
              "तु + उत्तरोत्तरम् → तूत्तरोत्तरम्; so साधु + उक्तम् → साधूक्तम् (well said).",
              "उ + उ → ऊ."),
          "Two like vowels merge into the long one: उ + उ → ऊ."),
    ],
}

# ---------------------------------------------------------------- unit 91
AUTHORED["91"] = {
    "title": "तत्र युग्मासु रात्रिषु",
    "question": "What does unit 91 say happens to the ārtava in the even and in the odd nights?",
    "rule": "Among these, in the even (yugma) nights the ārtava (menstrual blood) becomes small; in the odd (ayugma) ones it increases.",
    "limits": ("रात्रिषु (nights) is understood with अयुग्मासु. The unit states the two facts only; it gives no reason. "
               "Ārtava = menstrual blood, the female generative fluid (standard)."),
    "explain_hi": ("‘तत्र’ = उनमें, यानी इन रात्रियों में। सम (युग्म) रात्रियों में आर्तव अल्प हो जाता है और विषम (अयुग्म) "
                   "रात्रियों में बढ़ता (आप्यायते) है। आर्तव यानी मासिक रक्त, स्त्री का प्रजनन-द्रव (मानक अर्थ)। "
                   "‘अयुग्म’ = अ + युग्म, जो युग्म (सम) नहीं, यानी विषम। इकाई कोई कारण नहीं देती; अगली इकाई ‘तस्मात्’ "
                   "(इसलिए) से आरम्भ होती है।"),
    "hook": "सम रात: आर्तव घटे; विषम रात: आर्तव बढ़े।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 91, what happens to the ārtava in the even nights?",
            ("It becomes small", "युग्मासु रात्रिषु अल्पीभवति."),
            [("It increases", "It increases in the odd nights (आप्यायते)."),
             ("It stops for good", "Not said; it becomes small."),
             ("It turns dark", "No colour is named here.")],
            "In the even nights the ārtava becomes small; in the odd ones it increases.",
            "युग्म = even; अल्पीभवति = becomes small."),
        order(1, "Put these words of unit 91 in their printed order.",
              ["तत्र", "युग्मासु", "रात्रिषु", "अल्पीभवति", "आर्तवम्", "अयुग्मासु आप्यायते"],
              "Among these, in the even nights, becomes small, the ārtava; in the odd, it increases.",
              "तत्र → युग्मासु → रात्रिषु → अल्पीभवति → आर्तवम् → अयुग्मासु आप्यायते.", role="warmup"),
        match(2, "Match each word of unit 91 to its meaning on the card.",
              [["युग्म", "even"], ["अयुग्म", "odd"], ["अल्पीभवति", "becomes small"], ["आप्यायते", "increases, swells"]],
              "Two kinds of night, and what the ārtava does in each.",
              "युग्म, अयुग्म, अल्पीभवति, आप्यायते.", role="extend",
              teaches="युग्म = even; with the negative अ- it becomes अयुग्म, odd."),
        mcq("discriminate", 3, "Which split of रात्रिष्वल्पीभवति is right?",
            ("रात्रिषु + अल्पीभवति", "उ before a different vowel becomes व्."),
            [("रात्रिष्व + अल्पीभवति", "रात्रिष्व is not a word, and अ + अ would give आ."),
             ("रात्रिः + अल्पीभवति", "A visarga after इ would give र्: रात्रिरल्पीभवति."),
             ("रात्रिषो + अल्पीभवति", "ओ + अ would give रात्रिषोऽल्पीभवति.")],
            "रात्रिषु (in the nights) + अल्पीभवति (becomes small).",
            "उ + a different vowel → व् + that vowel."),
        mcq("apply", 4, "By unit 91, what does the ārtava do on the ninth night?",
            ("It increases (आप्यायते)", "Nine is odd (अयुग्म): there it increases."),
            [("It becomes small", "That is in the even nights."),
             ("It stops altogether", "Nothing like this is said."),
             ("It neither grows nor shrinks", "The unit gives a change for both kinds of night.")],
            "The ninth night is odd, and in the odd nights the ārtava increases.",
            "अयुग्म (odd) → आप्यायते."),
        T(mcq("transfer", 5, "By the rule of रात्रिष्वल्पीभवति, how is मधु + अरिः written when joined?",
              ("मध्वरिः", "उ + अ → व् + अ."),
              [("मधोरिः", "उ + अ does not give ओ."),
               ("मधूरिः", "उ + अ does not give ऊ."),
               ("मधुवरिः", "The उ itself turns into व्; it does not stay.")],
              "रात्रिषु + अल्पीभवति → रात्रिष्वल्पीभवति; so मधु + अरिः → मध्वरिः.",
              "उ + a different vowel → व्."),
          "A final उ before a different vowel becomes व्."),
    ],
}

# ---------------------------------------------------------------- unit 92
AUTHORED["92"] = {
    "title": "तस्मात्तासु क्रमात्",
    "question": "What does unit 92 conclude about the birth of a son and of a daughter?",
    "rule": "Therefore, in these (nights), in order, there is the birth of a son and of a daughter.",
    "limits": ("The copula is understood. This unit does not spell out which nights go with the son and which with the "
               "daughter; kramāt is read as the order of the nights. The nights are listed in unit 87 (son) and unit 88 "
               "(daughter)."),
    "explain_hi": ("‘तस्मात्’ = इसलिए। उन रात्रियों में क्रम से पुत्र और पुत्री का जन्म होता है। ‘क्रमात्’ यानी रात्रियों के "
                   "(सम-विषम) क्रम से; पर कौन-सा किस रात से, यह इस इकाई में स्पष्ट नहीं लिखा। रातें इकाई ८७ (पुत्र: आठवीं, "
                   "दसवीं, बारहवीं) और ८८ (पुत्री: पाँचवीं, सातवीं, नवीं) में दी गई हैं। ‘तासु’ पिछली इकाइयों की रातों की ओर संकेत करता है।"),
    "hook": "इसलिए उन रातों में क्रम से: पुत्र और पुत्री का जन्म।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 92, what follows in these nights, in order?",
            ("The birth of a son and of a daughter", "क्रमात् पुत्रस्य दुहितुश्च जन्म."),
            [("The growth and fall of life-span", "That is units 89 and 90."),
             ("The bath and the adorning of the wife", "That is unit 84."),
             ("Chastity and sleep on darbha grass", "Both belong to the three nights of unit 81.")],
            "Therefore in these (nights), in order, there is the birth of a son and of a daughter.",
            "पुत्रस्य दुहितुः च जन्म = birth of a son and of a daughter."),
        order(1, "Put the words of unit 92 in their printed order.",
              ["तस्मात्", "तासु", "क्रमात्", "पुत्रस्य", "दुहितुश्च", "जन्म"],
              "Therefore, in these, in order, of a son, and of a daughter, birth.",
              "तस्मात् → तासु → क्रमात् → पुत्रस्य → दुहितुः च → जन्म.", role="warmup"),
        match(2, "Match each word of unit 92 to its meaning on the card.",
              [["तस्मात्", "therefore"], ["तासु", "in these"], ["क्रमात्", "in order"], ["दुहितुः", "of a daughter"],
               ["जन्म", "birth"]],
              "These words make the whole conclusion.",
              "तस्मात्, तासु, क्रमात्, दुहितुः, जन्म.", role="extend",
              teaches="क्रमात् is an ablative used as an adverb: in order, in turn."),
        mcq("discriminate", 3, "Which split of दुहितुश्च is right?",
            ("दुहितुः + च", "A visarga before च becomes श्."),
            [("दुहितृ + श्च", "श्च is not a word."),
             ("दुहिते + च", "ए before च stays: दुहिते च; no श् comes in."),
             ("दुहितुम् + च", "म् before च would show as an anusvara: दुहितुं च.")],
            "दुहितुः (of a daughter) + च (and).",
            "Visarga + च → श्च."),
        mcq("apply", 4, "What does the card say about the pairing of nights in unit 92?",
            ("This unit itself does not spell it out", "The pairing is not spelled out here; units 87-88 give the nights."),
            [("It names the even nights for a daughter", "No nights are named in this unit."),
             ("It names the odd nights for a son", "No nights are named in this unit."),
             ("It says the order is left to chance", "क्रमात् means in order, not by chance.")],
            "Unit 92 says only 'in order'; the nights are listed in units 87 and 88.",
            "क्रमात् = in order; the nights: units 87-88."),
        T(mcq("transfer", 5, "By the rule of दुहितुश्च, how is रामः + च written when joined?",
              ("रामश्च", "A visarga before च becomes श्."),
              [("रामो च", "अः becomes ओ only before a voiced sound; च is unvoiced."),
               ("रामस्च", "Before च the visarga becomes श्, not स्."),
               ("रामर्च", "अः does not become र्.")],
              "दुहितुः + च → दुहितुश्च; so रामः + च → रामश्च.",
              "Visarga + च → श्च."),
          "A visarga before च or छ becomes श्."),
    ],
}

# ---------------------------------------------------------------- unit 93
AUTHORED["93"] = {
    "title": "अतएव चानुपरतार्तवदर्शनाम्",
    "question": "Whom does unit 93 say one desiring a son should not approach, even on odd days?",
    "rule": ("For this very reason, one desiring a son should not approach a woman in whom the sight of the ārtava has not "
             "ceased, even on odd days."),
    "limits": ("This unit speaks of days (अहस्सु), the earlier ones of nights; the text is followed as printed. It does not "
               "say why odd days are named, nor does it restate the reason it points back to. अहस्सु is a printed variant "
               "of अहःसु."),
    "explain_hi": ("‘अतएव’ = इसीलिए। पुत्र की इच्छा वाला उस स्त्री के पास न जाए जिसका आर्तव-दर्शन (मासिक स्राव का दिखना) अभी "
                   "रुका नहीं है, विषम दिनों में भी नहीं। ‘अनुपरतार्तवदर्शना’ बहुव्रीहि है: जिसका आर्तव दिखना बन्द नहीं हुआ। "
                   "यहाँ ‘दिन’ (अहस्सु) कहा गया है, पहले की इकाइयों में ‘रात्रि’; पाठ जैसा छपा है वैसा रखा गया। "
                   "विषम दिनों का उल्लेख क्यों है, यह इकाई नहीं बताती।"),
    "hook": "स्राव अभी रुका नहीं? पुत्रार्थी पास न जाए, विषम दिन में भी।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 93, whom should one desiring a son not approach?",
            ("A woman whose ārtava has not ceased", "अनुपरतार्तवदर्शनाम्: one in whom the sight of ārtava has not ceased."),
            [("A woman who has bathed", "No bath is named in this unit."),
             ("A woman who is already pregnant", "Pregnancy is not named in this unit."),
             ("A woman who is past fifty years", "Age is not named in this unit.")],
            "He should not approach a woman whose ārtava is still seen.",
            "अनुपरत = not ceased."),
        order(1, "Put the words of unit 93 in their printed order.",
              ["अतएव", "चानुपरतार्तवदर्शनां", "पुत्रार्थी", "विषमेष्वप्यहस्सु", "नोपेयात्"],
              "For this very reason, and the woman whose ārtava has not ceased, one desiring a son, even on odd days, should not approach.",
              "अतएव → अनुपरतार्तवदर्शनाम् → पुत्रार्थी → विषमेषु अपि अहस्सु → न उपेयात्.", role="warmup"),
        match(2, "Match each word of unit 93 to its meaning on the card.",
              [["अनुपरत", "not ceased"], ["आर्तवदर्शन", "sight of the ārtava"], ["पुत्रार्थी", "one desiring a son"],
               ["विषम", "odd"], ["उपेयात्", "should approach"]],
              "Five words carry the person, the woman, the days and the act.",
              "अनुपरत, आर्तवदर्शन, पुत्रार्थी, विषम, उपेयात्.", role="extend",
              teaches="अनुपरत = अन् + उपरत: not ceased; अन् is the negative before a vowel."),
        mcq("discriminate", 3, "Which split of नोपेयात् is right?",
            ("न + उपेयात्", "अ + उ → ओ."),
            [("नो + पेयात्", "पेयात् is not the card's word."),
             ("नः + उपेयात्", "A visarga after अ drops before उ, giving न उपेयात्."),
             ("नु + पेयात्", "Neither part is the card's word.")],
            "न (not) + उपेयात् (should approach).",
            "अ + उ → ओ."),
        mcq("apply", 4, "By unit 93, which days does it name with अपि (also, even)?",
            ("The odd days (विषम)", "विषमेषु अपि अहस्सु: even on odd days."),
            [("The even days (युग्म)", "युग्म is unit 91's word; this unit says विषम."),
             ("The fourth day only", "The fourth day belongs to unit 84."),
             ("The days of the bath", "No bath is named in this unit.")],
            "The rule holds even on the odd days.",
            "विषम = odd; अपि = also, even."),
        T(mcq("transfer", 5, "By the rule of अनुपरत, which word means without beginning?",
              ("अनादि", "अन् + आदि: the negative is अन् before a vowel."),
              [("अआदि", "Before a vowel the negative is अन्, not अ."),
               ("अवादि", "The negative never takes व्."),
               ("अनदि", "आदि keeps its long आ.")],
              "अन् + उपरत → अनुपरत; so अन् + आदि → अनादि.",
              "Negative अ- before a consonant, अन्- before a vowel."),
          "The negative prefix is अ- before a consonant and अन्- before a vowel (अनुपरत, अनादि)."),
    ],
}

# ===================================================================== NOTES_HI
NOTES_HI = {
    "81": ("विश्वास ऊँचा। गद्य इकाई; कर्ता (स्त्री) का नाम नहीं, प्रसंग से समझी जाती है। ‘पुष्प’ मासिक स्राव का सामान्य शब्द; "
           "पुष्पदर्शन = रजोदर्शन (मानक)। ‘आसीत’ = रहे। दर्भ: प्रायः कुश मानी जाती है, कुछ स्रोत दूसरी घास बताते हैं; पहचान विवादित। "
           "सन्धि: प्रथमदिवसात् + प्रभृति → प्रथमदिवसात्प्रभृति; स्नान + अलंकार → स्नानालंकार (अ + अ → आ); "
           "त्रिरात्रम् + आसीत → त्रिरात्रमासीत।"),
    "82": ("विश्वास मध्यम। छपा ‘यावकंपयसा’ = यावकं पयसा (दो शब्द बिना दूरी के छपे; कोई अक्षर नहीं बदला)। "
           "‘यावक’ सम्भवतः यव (जौ) से बनी वस्तु (सम्भावित); इसका अर्थ लाख भी होता है, पर वह खाने में नहीं बैठता। "
           "‘अन्यतमे’ = दोनों में से किसी एक में। स्त्री इकाई ८१ की। सन्धि: करतल + अन्यतमे → करतलान्यतमे; "
           "सिद्धम् + अल्पम् → सिद्धमल्पम्; कर्शन + अर्थम् → कर्शनार्थम्।"),
    "83": ("विश्वास ऊँचा। चार गुणों का द्वन्द्व; संज्ञा (आहार) और कर्ता (इकाई ८१ की स्त्री) समझे जाते हैं। ‘तीक्ष्ण’ = तीखा, चरपरा। "
           "सन्धि: तीक्ष्ण + उष्ण → तीक्ष्णोष्ण (अ + उ → ओ); उष्ण + अम्ल → उष्णाम्ल (अ + अ → आ)।"),
    "84": ("विश्वास मध्यम। छपा ‘कृतमंगलस्वस्त्ययनैवंविधमेव’ तीन शब्द जुड़े छपे: कृतमङ्गलस्वस्त्ययना + एवंविधम् + एव "
           "(आ + ए → ऐ; कोई अक्षर ग़लत नहीं)। ‘एवंविध’ ऐसे वर्णन की ओर संकेत है जो इस इकाई में नहीं; पति के गुण यहाँ नहीं। "
           "‘उद्वर्तिता’ उद्वर्तन (चूर्ण से मलना) से, सम्भावित अर्थ। छपे ‘स्नाताऽनुलिप्ताऽलंकृता’ में ऽ दिखाता है कि अगले शब्द का "
           "आरम्भिक अ पिछले आ में मिल गया (आ + अ → आ)। सन्धि: चतुर्थे + अहनि → चतुर्थेऽहनि; अहनि + उद्वर्तिता → अहन्युद्वर्तिता; "
           "स्वस्ति + अयन → स्वस्त्ययन; पश्येत् + अनन्यमनाः → पश्येदनन्यमनाः।"),
    "85": ("विश्वास कम। दो छपी पंक्तियाँ जुड़ी हैं। पंक्ति १: कर्म अनकहे, यादृश-तादृश विशेषण; छपा ‘प्रसूत इति’ = प्रसूते + इति "
           "(ए + स्वर → अय्, य् का लोप); अन्त का ‘इति’ कथन-समाप्ति, अनुवाद में नहीं। पंक्ति २ अनुमानित: ‘स्नातांत्’ का सुझाव "
           "‘स्नातात्’ (त से पहले अनुस्वार इस छपाई की आदत; पंचमी, ‘स्नान के बाद’, असामान्य रूप); विकल्प ‘स्नाताम्’ (नहाई स्त्री को), "
           "त् को भटका अक्षर मानकर; ‘उपेक्षेत’ = ‘बीतने दे’ (अनुमानित) या ‘दूर रहे, उपेक्षा करे’; तय नहीं, स्वामी के लिए खुला। "
           "‘चतूरात्रम्’ का सुझाव ‘चतुरात्रम्’; ध्यान दें कि र् + र् में पहला र् लुप्त होकर पूर्व स्वर दीर्घ होता है "
           "(निर् + रस → नीरस), इसलिए ‘चतूरात्रम्’ भी नियमित सन्धि-रूप हो सकता है। ‘पुत्रार्थी’ पुल्लिङ्ग, पर कर्ता नहीं कहा। "
           "सन्धि: यादृशम् + एव → यादृशमेव; पुनः + अपि → पुनरपि। यह वाक्य इकाई ८६-८७ के साथ चलता लगता है।"),
    "86": ("विश्वास कम। क्रियाहीन टुकड़ा; कोई क्रिया नहीं जोड़ी गई। छपा ‘पुष्पेदिनात्’: सुझाव समास ‘पुष्पदिनात्’ (समास के भीतर सप्तमी "
           "‘पुष्पे’ अटपटी है), विकल्प दो शब्द ‘पुष्पे दिनात्’; तय नहीं। सन्धि: दिनात् + सप्तरात्रम् → दिनात्सप्तरात्रम् (अघोष स से "
           "पहले त् वैसा ही)। इकाई ८५ (बीतने वाली रातें) के साथ जुड़ा लगता है और इकाई ८७ की ओर ले जाता है।"),
    "87": ("विश्वास ऊँचा। ‘रात्रौ’ एकवचन, हर क्रम-संख्या के साथ समझा जाता है। ‘संविशेत्’ का कर्म नहीं छपा। "
           "सन्धि: अथ + अष्टम्याम् → अथाष्टम्याम् (अ + अ → आ); व्यंजन से पहले म् → अनुस्वार (अष्टम्यां दशम्यां)।"),
    "88": ("विश्वास ऊँचा। क्रिया ‘संविशेत्’ और ‘रात्रौ’ इकाई ८७ से; अनुवाद में क्रिया नहीं जोड़ी गई। छपा ‘पंचम्यां’ = पञ्चम्याम् "
           "(अनुस्वार)। ‘दुहितृकाम’ बहुव्रीहि, पुल्लिङ्ग प्रथमा। यह इकाई ८७ को आगे बढ़ाती है।"),
    "89": ("विश्वास मध्यम। ‘अपत्यस्य भवति’ सम्बन्ध-षष्ठी (सन्तान की होती है)। ‘संपद्’ पूरी सूची वाले लम्बे समास का अन्तिम पद: "
           "सबकी सम्पदा। वर्ण = त्वचा का रंग (सम्भावित; रंग या वर्ग भी हो सकता है)। सन्धि: तासु + उत्तरोत्तरम् → तासूत्तरोत्तरम्; "
           "उत्तर + उत्तरम् → उत्तरोत्तरम्; आयुः + आरोग्य → आयुरारोग्य; आरोग्य + ऐश्वर्य → आरोग्यैश्वर्य; वर्ण + इन्द्रिय → वर्णेन्द्रिय; "
           "संपत् + अपत्यस्य → संपदपत्यस्य।"),
    "90": ("विश्वास ऊँचा। क्रिया (होता है) समझी जाती है। ‘आदि’ = इकाई ८९ की सूची; यह इकाई ८९ के बाद आती है। "
           "सन्धि: तु + उत्तरोत्तरम् → तूत्तरोत्तरम् (उ + उ → ऊ); उत्तरोत्तरम् + एव → उत्तरोत्तरमेव; एव + आयुः → एवायुः; "
           "आयुः + आदीनाम् → आयुरादीनाम्।"),
    "91": ("विश्वास ऊँचा। ‘रात्रिषु’ ‘अयुग्मासु’ के साथ भी समझा जाता है। आर्तव = मासिक रक्त, स्त्री का प्रजनन-द्रव (मानक)। "
           "‘आप्यायते’ का कर्ता वही आर्तव। सन्धि: रात्रिषु + अल्पीभवति → रात्रिष्वल्पीभवति; अल्पीभवति + आर्तवम् → अल्पीभवत्यार्तवम्; "
           "आर्तवम् + अयुग्मासु → आर्तवमयुग्मासु; अयुग्मासु + आप्यायते → अयुग्मास्वाप्यायते।"),
    "92": ("विश्वास ऊँचा। क्रिया समझी जाती है। ‘क्रमात्’ = रातों के (सम/विषम) क्रम से; पुत्र-सम, पुत्री-विषम का जोड़ा इस इकाई में "
           "स्पष्ट नहीं लिखा। ‘तासु’ इकाई ८७-९१ की रातों की ओर। सन्धि: तस्मात् + तासु → तस्मात्तासु; क्रमात् + पुत्रस्य → "
           "क्रमात्पुत्रस्य; दुहितुः + च → दुहितुश्च।"),
    "93": ("विश्वास मध्यम। ‘अनुपरतार्तवदर्शनाम्’ बहुव्रीहि, स्त्रीलिङ्ग द्वितीया: जिसका आर्तव-दर्शन रुका नहीं। ‘अहस्सु’ = ‘अहःसु’ का "
           "छपा विकल्प। यहाँ दिन, पहले की इकाइयों में रातें; पाठ जैसा छपा वैसा रखा। सन्धि: अतः + एव → अत एव (छपा ‘अतएव’); "
           "च + अनुपरत → चानुपरत; विषमेषु + अपि → विषमेष्वपि; अपि + अहस्सु → अप्यहस्सु; न + उपेयात् → नोपेयात्।"),
}

# ===================================================================== AIDS
AIDS = {
    "81": {
        "chain": {"steps": ["पुष्पदर्शन: पहला दिन", "ब्रह्मचारिणी", "स्नान-अलंकार से रहित", "दर्भ के बिछौने पर शयन",
                            "तीन रात तक"]},
        "frame": "कब: पुष्पदर्शने, प्रथमदिवसात् प्रभृति · कैसे: ब्रह्मचारिणी, स्नानालंकाररहिता, दर्भसंस्तरशायिनी · कितना: त्रिरात्रम्।",
        "sandhi": ("त् + प → त्प: प्रथमदिवसात् + प्रभृति → प्रथमदिवसात्प्रभृति · अ + अ → आ: स्नान + अलंकार → स्नानालंकार · "
                   "म् + स्वर: त्रिरात्रम् + आसीत → त्रिरात्रमासीत।"),
        "anchors": "मेरी याद-पद्धति: तीन रात, तीन संयम: ब्रह्मचर्य, न स्नान-अलंकार, दर्भ पर शयन।",
    },
    "82": {
        "diagram": {"groups": [
            {"label": "किसमें", "items": ["पर्णशराव (पत्ते का दोना)", "या करतल (हथेली)"]},
            {"label": "क्या", "items": ["यावक (सम्भवतः जौ से बना)", "दूध में पका"]},
            {"label": "कितना", "items": ["अल्प"]},
            {"label": "क्यों", "items": ["कर्शनार्थम् (कृश करने को)"]}]},
        "sandhi": ("अ + अ → आ: करतल + अन्यतमे → करतलान्यतमे; कर्शन + अर्थम् → कर्शनार्थम् · "
                   "म् + स्वर: सिद्धम् + अल्पम् → सिद्धमल्पम्; कर्शनार्थम् + अश्नीयात् → कर्शनार्थमश्नीयात्।"),
        "pegs": "मेरा बनाया चित्र: हथेली पर दूध में पके जौ का छोटा कौर, पास में पत्ते का दोना। (केवल याद के लिए)",
    },
    "83": {
        "frame": "स्त्री (इकाई ८१ की) · वर्जयेत् · तीक्ष्ण, उष्ण, अम्ल, लवण (आहार समझा जाता है)।",
        "sandhi": "अ + उ → ओ: तीक्ष्ण + उष्ण → तीक्ष्णोष्ण · अ + अ → आ: उष्ण + अम्ल → उष्णाम्ल।",
        "letters": "चार वर्ज्य: ती-उ-अ-ल (तीक्ष्ण, उष्ण, अम्ल, लवण)।",
    },
    "84": {
        "chain": {"steps": ["चौथा दिन", "उद्वर्तिता (उबटन)", "ठण्डे जल से स्नाता", "अनुलिप्ता (लेप)", "अलंकृता",
                            "श्वेत माला और वस्त्र", "मंगल-स्वस्त्ययन किए", "अनन्यमना: ऐसे पति को देखे"]},
        "sandhi": ("ए + अ → एऽ: चतुर्थे + अहनि → चतुर्थेऽहनि · इ + उ → यु: अहनि + उद्वर्तिता → अहन्युद्वर्तिता · "
                   "आ + ए → ऐ: स्वस्त्ययना + एवंविधम् → स्वस्त्ययनैवंविधम् · त् + स्वर → द्: पश्येत् + अनन्यमनाः → पश्येदनन्यमनाः।"),
        "contrast": "इकाई ८१ (तीन रात): स्नान और अलंकार से रहित, दर्भ पर शयन ↔ इकाई ८४ (चौथा दिन): ठण्डे जल से स्नान, अलंकार, श्वेत माला-वस्त्र।",
    },
    "85": {
        "frame": "पंक्ति १: तदा हि (क्योंकि तब) → यादृशम् पश्यति चिन्तयति वा → तादृशं प्रसूते। पंक्ति २: पाठ अनुमानित।",
        "sandhi": "ए + इ → अ इ: प्रसूते + इति → प्रसूत इति (ए → अय्, य् का लोप) · म् + स्वर: यादृशम् + एव → यादृशमेव।",
        "anchors": "मेरी याद-पद्धति: या-दृश = जैसा, ता-दृश = वैसा; ‘य’ वाला सम्बन्ध जोड़ता है (जो/जैसा), ‘त’ वाला उसे पूरा करता है (वह/वैसा)।",
    },
    "86": {
        "frame": "पुष्प (स्राव) के दिन से → सात रात (क्रिया नहीं; इकाई ८५ और ८७ के साथ पढ़ें)।",
        "sandhi": "त् + स → त्स: दिनात् + सप्तरात्रम् → दिनात्सप्तरात्रम् · पाठ: ‘पुष्पे’ या ‘पुष्प-’ (तय नहीं)।",
        "chunks": "पुष्पेदिनात् | सप्तरात्रं",
    },
    "87": {
        "frame": "अथ → अष्टम्यां, दशम्यां, द्वादश्यां वा (रात्रौ) → पुत्रकामः संविशेत्।",
        "sandhi": "अ + अ → आ: अथ + अष्टम्याम् → अथाष्टम्याम् · म् → अनुस्वार व्यंजन से पहले: अष्टम्याम् दशम्याम् → अष्टम्यां दशम्यां।",
        "anchors": "पुत्र: ८, १०, १२ (तीनों सम अंक)।",
    },
    "88": {
        "contrast": "इकाई ८७: पुत्रकाम → आठवीं, दसवीं, बारहवीं ↔ इकाई ८८: दुहितृकाम → पाँचवीं, सातवीं, नवीं।",
        "frame": "क्रिया ‘संविशेत्’ और ‘रात्रौ’ इकाई ८७ से आते हैं; इकाई ८८ में केवल रातें और व्यक्ति।",
        "anchors": "पुत्री: ५, ७, ९ (विषम अंक) · पुत्र: ८, १०, १२ (सम अंक)।",
    },
    "89": {
        "diagram": {"groups": [
            {"label": "सन्तान की सम्पदा (उत्तरोत्तर)",
             "items": ["आयु", "आरोग्य", "ऐश्वर्य", "सौभाग्य", "बल", "वर्ण", "इन्द्रिय"]}]},
        "sandhi": ("उ + उ → ऊ: तासु + उत्तरोत्तरम् → तासूत्तरोत्तरम् · उः + स्वर → उर्: आयुः + आरोग्य → आयुरारोग्य · "
                   "अ + ऐ → ऐ: आरोग्य + ऐश्वर्य → आरोग्यैश्वर्य · अ + इ → ए: वर्ण + इन्द्रिय → वर्णेन्द्रिय।"),
        "letters": "सात की सूची: आ-आ-ऐ-सौ-ब-व-इ (आयु, आरोग्य, ऐश्वर्य, सौभाग्य, बल, वर्ण, इन्द्रिय)।",
        "contrast": "इकाई ८९: इन रातों में उत्तरोत्तर सम्पदा ↔ इकाई ९०: इसके आगे उत्तरोत्तर ह्रास।",
    },
    "90": {
        "contrast": "इकाई ८९: इन रातों में उत्तरोत्तर सम्पदा (आयु, आरोग्य, बल आदि) ↔ इकाई ९०: इसके आगे उत्तरोत्तर ह्रास।",
        "frame": "अतः परम् (इसके आगे) + तु (किन्तु) → उत्तरोत्तरम् एव → आयु आदि का ह्रास।",
        "sandhi": ("उ + उ → ऊ: तु + उत्तरोत्तरम् → तूत्तरोत्तरम् · अ + आ → आ: एव + आयुः → एवायुः · "
                   "उः + आ → उरा: आयुः + आदीनाम् → आयुरादीनाम्।"),
    },
    "91": {
        "seesaw": "युग्म (सम) रातें: आर्तव अल्पीभवति (घटता) ↔ अयुग्म (विषम) रातें: आर्तव आप्यायते (बढ़ता)।",
        "sandhi": ("उ + अ → व: रात्रिषु + अल्पीभवति → रात्रिष्वल्पीभवति · इ + आ → या: अल्पीभवति + आर्तवम् → अल्पीभवत्यार्तवम् · "
                   "म् + स्वर: आर्तवम् + अयुग्मासु → आर्तवमयुग्मासु · उ + आ → वा: अयुग्मासु + आप्यायते → अयुग्मास्वाप्यायते।"),
        "chunks": "तत्र युग्मासु | रात्रिष्वल्पीभवत्यार्तवम् | अयुग्मास्वाप्यायते",
    },
    "92": {
        "frame": "तस्मात् (इसलिए) → तासु (उन रातों में) → क्रमात् (क्रम से) → पुत्र और दुहिता का जन्म।",
        "sandhi": ("त् + त → त्त: तस्मात् + तासु → तस्मात्तासु · त् + प → त्प: क्रमात् + पुत्रस्य → क्रमात्पुत्रस्य · "
                   "ः + च → श्च: दुहितुः + च → दुहितुश्च।"),
        "chunks": "तस्मात्तासु | क्रमात् | पुत्रस्य दुहितुश्च | जन्म",
    },
    "93": {
        "frame": "अतएव (इसीलिए) → पुत्रार्थी → अनुपरतार्तवदर्शनाम् (जिसका स्राव नहीं रुका) → विषमेषु अपि अहस्सु → न उपेयात्।",
        "sandhi": ("अ + अ → आ: च + अनुपरत → चानुपरत · उ + अ → व: विषमेषु + अपि → विषमेष्वपि · इ + अ → य: अपि + अहस्सु → अप्यहस्सु · "
                   "अ + उ → ओ: न + उपेयात् → नोपेयात्।"),
        "chunks": "अतएव | चानुपरतार्तवदर्शनां | पुत्रार्थी | विषमेष्वप्यहस्सु | नोपेयात्",
    },
}

# ===================================================================== IMAGE_SPECS
IMAGE_SPECS = {
    ("81", "chain"): {
        "file": "sh1-rajasvala-81.svg",
        "alt": ("Chain of unit 81: from the first day the menses are seen, she keeps chastity, goes without bath and "
                "ornaments, sleeps on a spread of darbha grass, for three nights."),
        "type": "chain",
        "title": "रजस्वला-चर्या (इकाई ८१)",
        "steps": ["पुष्पदर्शन: पहला दिन", "ब्रह्मचारिणी", "स्नान-अलंकार से रहित", "दर्भ के बिछौने पर शयन", "तीन रात तक"],
    },
    ("82", "diagram"): {
        "file": "sh1-yavaka-82.svg",
        "alt": ("Table of unit 82: in a leaf-bowl or the palm of the hand; yavaka (probably a barley preparation) cooked "
                "with milk; a little; for thinning."),
        "type": "table",
        "title": "आहार-नियम (इकाई ८२)",
        "heads": ["प्रश्न", "इकाई ८२"],
        "rows": [["किसमें", "पत्ते का दोना या हथेली"],
                 ["क्या", "यावक (सम्भवतः जौ), दूध में पका"],
                 ["कितना", "अल्प"],
                 ["क्यों", "कर्शन: कृश करने को"]],
    },
    ("84", "chain"): {
        "file": "sh1-chaturtha-dina-84.svg",
        "alt": ("Chain of unit 84 in printed order: fourth day; rubbed with powder; bathed in cold water; anointed; adorned; "
                "white garlands and garments; auspicious rites done; with mind on no other she looks upon such a husband."),
        "type": "chain",
        "title": "चौथा दिन (इकाई ८४)",
        "steps": ["चौथा दिन", "उद्वर्तिता (उबटन)", "ठण्डे जल से स्नाता", "अनुलिप्ता (लेप)", "अलंकृता",
                  "श्वेत माला और वस्त्र", "मंगल-स्वस्त्ययन किए", "अनन्यमना: ऐसे पति को देखे"],
    },
    ("88", "contrast"): {
        "file": "sh1-ratri-88.svg",
        "alt": ("Table joining units 87 and 88: one desiring a son, the eighth, tenth or twelfth night; one desiring a "
                "daughter, the fifth, seventh or ninth."),
        "type": "table",
        "title": "रातें (इकाई ८७-८८)",
        "heads": ["पुत्रकाम (इकाई ८७)", "दुहितृकाम (इकाई ८८)"],
        "rows": [["आठवीं रात", "पाँचवीं रात"],
                 ["दसवीं रात", "सातवीं रात"],
                 ["बारहवीं रात", "नवीं रात"]],
    },
    ("89", "diagram"): {
        "file": "sh1-sampad-89.svg",
        "alt": ("Chain of unit 89 in printed order: the offspring's endowment, growing progressively in these nights: "
                "life-span, health, lordship, good fortune, strength, complexion, the senses."),
        "type": "chain",
        "title": "सन्तान की सम्पदा (इकाई ८९)",
        "steps": ["आयु", "आरोग्य", "ऐश्वर्य", "सौभाग्य", "बल", "वर्ण", "इन्द्रिय"],
    },
    ("90", "contrast"): {
        "file": "sh1-hrasa-90.svg",
        "alt": ("Split of units 89 and 90: in these nights the endowment grows progressively; after this, life-span and "
                "the rest decrease progressively."),
        "type": "split",
        "title": "बढ़त और ह्रास (इकाई ८९-९०)",
        "cols": [["इन रातों में (इकाई ८९)", ["उत्तरोत्तर सम्पदा", "आयु, आरोग्य, बल आदि"]],
                 ["इसके आगे (इकाई ९०)", ["उत्तरोत्तर ह्रास", "आयु आदि का"]]],
    },
    ("91", "seesaw"): {
        "file": "sh1-yugma-91.svg",
        "alt": "Split of unit 91: in the even nights the artava becomes small; in the odd nights it increases.",
        "type": "split",
        "title": "आर्तव: सम और विषम रातें (इकाई ९१)",
        "cols": [["युग्म (सम) रातें", ["आर्तव अल्प होता है"]],
                 ["अयुग्म (विषम) रातें", ["आर्तव बढ़ता है"]]],
    },
}
