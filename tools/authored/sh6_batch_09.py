from helpers import mcq, match, order, fill, multi, accepts


AUTHORED = {}

# ---------------------------------------------------------------- unit 104
AUTHORED["104"] = {
    "title": "ताभ्यां च सारमलाभ्यां",
    "question": "By unit 104, what do the essence and the waste fill, and how?",
    "rule": ("By those two, the essence and the waste (सारमलाभ्याम्), the srotas of the dhātus, which have just that nature, "
             "are filled each according to its own (यथास्वम्), in succession, in an unbroken stream."),
    "limits": ("Prose. ताभ्याम् takes up the essence and waste of unit 103. Printed धातुवाख्यानां is read as "
               "धात्वाख्यानाम् (possible): no question on it. 'Bodily qualities' loosely means the dhātus; how the essence "
               "relates to each dhātu is not stated."),
    "explain_hi": ("यह गद्य-पंक्ति इकाई १०३ के सार (रस) और मल (किट्ट) को ‘ताभ्याम्’ यानी ‘उन दोनों से’ कहकर आगे ले जाती है। "
                   "उन्हीं के स्वरूप वाले (तदात्मक) शारीरिक गुणों, जिन्हें धातु कहते हैं, के स्रोतस् अपने-अपने अनुसार (यथास्वम्) भरे जाते हैं। "
                   "यह भरना क्रम से (पारम्पर्येण) और अटूट प्रवाह में (अव्यवच्छिन्नसन्तानम्) होता है। "
                   "‘शारीरगुण’ यहाँ धातुओं के लिए ढीला शब्द है; सार का हर धातु से ठीक सम्बन्ध यहाँ नहीं खोला गया। "
                   "छपा ‘धातुवाख्यानां’ सम्भवतः ‘धात्वाख्यानाम्’ है।"),
    "hook": "सार और मल से धातुओं के स्रोतस् क्रम से, बिना टूटे भरते हैं।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 104, what is filled by the essence and the waste?",
            ("The srotas of the dhātus", "स्रोतांसि ... आपूर्यन्ते: the srotas of the dhātus are filled."),
            [("The pores of the skin only", "The skin pores are not named in unit 104."),
             ("The hollow of the stomach", "Unit 104 speaks of the srotas of the dhātus, not the stomach."),
             ("The large bowel and bladder", "Neither is named in unit 104.")],
            "By the essence and the waste the srotas of the dhātus are filled.",
            "ताभ्यां च सारमलाभ्यां ... स्रोतांसि ... आपूर्यंते."),
        order(1, "Put these parts of unit 104 in the line's order.",
              ["ताभ्यां च सारमलाभ्यां", "तदात्मकानामेव", "शारीरगुणानां", "यथास्वं", "स्रोतांसि",
               "पारंपर्येणाव्यवच्छिन्नसंतानमापूर्यंते"],
              "By those two, of the same nature, of the bodily qualities, each its own, the srotas are filled in succession, unbroken.",
              "ताभ्यां च सारमलाभ्यां → तदात्मकानामेव → शारीरगुणानां → यथास्वं → स्रोतांसि → पारंपर्येणाव्यवच्छिन्नसंतानमापूर्यंते."),
        match(2, "Match each word of unit 104 to its meaning.",
              [["सार", "essence"], ["मल", "waste"], ["पारम्पर्येण", "in succession"], ["अव्यवच्छिन्न", "unbroken"],
               ["आपूर्यन्ते", "are filled"]],
              "Essence and waste fill the srotas in succession, unbroken.",
              "सार, मल, पारम्पर्येण, अव्यवच्छिन्न, आपूर्यन्ते.", role="extend",
              teaches="अ- negates: व्यवच्छिन्न 'cut off' → अव्यवच्छिन्न 'unbroken'; the stream of filling is never cut."),
        mcq("discriminate", 3, "By unit 104, how are the srotas filled?",
            ("In succession, in an unbroken stream", "पारम्पर्येणाव्यवच्छिन्नसन्तानम्: in succession, unbroken."),
            [("All at once, in one single flood", "पारम्पर्येण says in succession, not all at once."),
             ("In breaks, the stream being cut off", "अव्यवच्छिन्न means unbroken, not cut off."),
             ("Only during sleep, at night, in a trickle", "No time of day is named in unit 104.")],
            "The filling goes in succession and in an unbroken stream.",
            "पारंपर्येणाव्यवच्छिन्नसंतानमापूर्यंते."),
        multi("apply", 4, "Which statements fit unit 104?",
              [("ताभ्याम्, by those two, takes up the essence and the waste", "Right: ताभ्यां च सारमलाभ्यां."),
               ("The srotas are filled by the waste alone", "Both the essence and the waste are named (सारमलाभ्याम्)."),
               ("The filling goes each according to its own, यथास्वम्", "Right: यथास्वं स्रोतांसि."),
               ("The unit names each dhātu one by one", "No dhātu is named one by one here; the lists come in units 109-114.")],
              [0, 2],
              "By essence and waste together the srotas are filled, each according to its own.",
              "ताभ्यां च सारमलाभ्यां ... यथास्वं स्रोतांसि ... आपूर्यंते."),
        mcq("transfer", 5, "By the rule of तत् + आत्मक → तदात्मक, how is सत् + आचार (good conduct) joined in a new example?",
            ("सदाचार", "A final त् before a vowel becomes द्, as तत् + आत्मक → तदात्मक."),
            [("सताचार", "Before a vowel the त् does not stay; it becomes द्."),
             ("सदचार", "The आ of आचार is kept long; nothing shortens it."),
             ("सन्नाचार", "त् may become न् (optionally) only before a nasal, not before a vowel.")],
            "सत् + आचार = सदाचार, like तत् + आत्मक = तदात्मक.",
            "Final त् before a vowel → द्.",
            teaches="A word-final त् becomes द् before a vowel: तत् + आत्मक → तदात्मक."),
    ],
}

# ---------------------------------------------------------------- unit 105
AUTHORED["105"] = {
    "title": "स्त्रोतोभ्यश्च यथाविभागं",
    "question": "By unit 105, from what and how are the dhātus nourished?",
    "rule": ("From the srotas (स्रोतोभ्यः), according to division (यथाविभागम्) and, on a possible reading, according to need, "
             "the dhātus (धातवः) are nourished (पुष्यन्ति)."),
    "limits": ("Prose. Printed यथाथमेव is not a word; 'according to need' rests on the possible reading यथार्थमेव: no question "
               "on that word. Printed स्त्रोतो- is read as स्रोतो-. The unit does not say what the 'division' is."),
    "explain_hi": ("इकाई १०४ में धातुओं के स्रोतस् भरे गए; यहाँ कहा गया है कि स्रोतसों से धातु पुष्ट होते हैं। "
                   "पोषण ‘यथाविभागम्’ यानी विभाग के अनुसार होता है; यह विभाग क्या है, पंक्ति नहीं बताती। "
                   "छपा ‘यथाथमेव’ कोई शब्द नहीं; ‘यथार्थमेव’ (आवश्यकता के अनुसार ही) सम्भावित पाठ है, र् छपाई में छूटा माना गया। "
                   "‘पुष्यन्ति’ (पुष्ट होते हैं) √पुष् का वर्तमान बहुवचन है और ‘धातवः’ से मेल खाता है। "
                   "सन्धि: स्रोतोभ्यः + च → स्रोतोभ्यश्च।"),
    "hook": "भरे स्रोतसों से धातु पलते हैं, विभाग के अनुसार।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 105, what are nourished from the srotas?",
            ("The dhātus (धातवः)", "धातवः पुष्यन्ति: the dhātus are nourished."),
            [("The senses (इन्द्रियाणि)", "The senses are not named in unit 105."),
             ("The mind (मनः)", "The mind is not named in unit 105."),
             ("The winds (वायवः)", "No wind is named in unit 105.")],
            "From the srotas the dhātus are nourished.",
            "स्त्रोतोभ्यश्च ... धातवः पुष्यंति."),
        order(1, "Put these words of unit 105 in the line's order.",
              ["स्त्रोतोभ्यश्च", "यथाविभागं", "धातवः", "पुष्यंति"],
              "From the srotas, according to division, the dhātus are nourished.",
              "स्त्रोतोभ्यश्च → यथाविभागं → धातवः → पुष्यंति."),
        match(2, "Match each word of unit 105 to its meaning.",
              [["स्रोतोभ्यः", "from the srotas"], ["यथाविभागम्", "according to division"], ["धातवः", "the dhātus"],
               ["पुष्यन्ति", "are nourished, thrive"]],
              "From the srotas, according to division, the dhātus thrive.",
              "स्रोतोभ्यः, यथाविभागम्, धातवः, पुष्यन्ति.", role="extend",
              teaches="पुष्यन्ति is a 3rd plural present of √पुष् (to thrive); its subject is the plural धातवः."),
        mcq("discriminate", 3, "Which split of स्त्रोतोभ्यश्च (printed for स्रोतोभ्यश्च) in unit 105 is right?",
            ("स्रोतोभ्यः + च", "A visarga before च becomes श्: स्रोतोभ्यः + च → स्रोतोभ्यश्च."),
            [("स्रोतोभ्य + अश्च", "अश्च is not a word here; and अ + अ would give आ."),
             ("स्रोतः + भ्यश्च", "भ्यश्च is not a word; -भ्यः is the case ending of स्रोतस्."),
             ("स्रोतोभ्याम् + च", "म् before च would be written ं: स्रोतोभ्यां च.")],
            "स्रोतोभ्यः (from the srotas) + च (and): visarga before च → श्.",
            "Visarga before च → श्."),
        multi("apply", 4, "Which statements fit unit 105?",
              [("The srotas are nourished from the dhātus", "The other way round: the dhātus from the srotas."),
               ("The dhātus are nourished from the srotas", "Right: स्रोतोभ्यश्च ... धातवः पुष्यन्ति."),
               ("The unit explains what the division is", "The division is not explained in unit 105."),
               ("पुष्यन्ति is plural, agreeing with धातवः", "Right: both are plural.")],
              [1, 3],
              "From the srotas the dhātus (plural) are nourished; the division is not explained.",
              "स्त्रोतोभ्यश्च यथाविभागं ... धातवः पुष्यंति."),
        mcq("transfer", 5, "By the rule of स्रोतोभ्यश्च, how is देवाः + च (and the gods) joined in a new example?",
            ("देवाश्च", "A visarga before च becomes श्, as स्रोतोभ्यः + च → स्रोतोभ्यश्च."),
            [("देवास्च", "स् is the form before त/थ, not before च."),
             ("देवा च", "After आ the visarga drops before a voiced sound or a vowel; च is not voiced."),
             ("देवोच", "ओ comes from अः before a voiced consonant, not from आः.")],
            "देवाः + च = देवाश्च, like स्रोतोभ्यः + च = स्रोतोभ्यश्च.",
            "Visarga + च → श्च.",
            teaches="A visarga before च becomes श्: स्रोतोभ्यः + च → स्रोतोभ्यश्च."),
    ],
}

# ---------------------------------------------------------------- unit 106
AUTHORED["106"] = {
    "title": "उत्तरोत्तरानुप्रवेशेऽपि",
    "question": "By unit 106, what does not happen to the earlier srotas, and how are they kept up?",
    "rule": ("Even with the entry of each later one (उत्तरोत्तरानुप्रवेशे अपि), there is no wasting (न अपचयः) of the earlier "
             "srotas, which are nourished in due time (यथाकालम्) by the proper use of food, with transformation."),
    "limits": ("Prose. What 'the entry of each later one' means exactly is not stated; the data reads it loosely as the later "
               "stages drawing on the earlier: no question on that process. 'With transformation' is kept literal."),
    "explain_hi": ("यह गद्य-पंक्ति कहती है: बाद-बाद वाले के प्रवेश करने पर भी पहले वाले स्रोतसों का क्षय (अपचय) नहीं होता। "
                   "वे समय पर (यथाकालम्) आहार के ठीक सेवन (सम्यगाहारोपयोगेन) से परिणाम के साथ पोषित होते रहते हैं (आप्यायमानानाम्)। "
                   "‘अपि’ (भी) बताता है कि प्रवेश होने पर भी क्षय नहीं होता। "
                   "‘उत्तरोत्तरानुप्रवेश’ का ठीक अर्थ पंक्ति नहीं खोलती; डेटा इसे ढीले रूप में बाद के चरणों का पहले वालों से लेना पढ़ता है। "
                   "सन्धि: न + अपचयः → नापचयः, और भवति से पहले अपचयो।"),
    "hook": "बाद वाले लें, फिर भी पहले वाले न घटें: समय पर ठीक आहार से वे भरते रहते हैं।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 106, what is denied (न ... भवति) for the earlier srotas?",
            ("Wasting away", "नापचयो भवति: there is no wasting (apacaya)."),
            [("Being nourished", "They are nourished (आप्यायमानानाम्); that is affirmed."),
             ("Being transformed", "Only wasting (अपचय) is denied: नापचयो भवति. Nothing else is denied."),
             ("Receiving food", "They are kept up by the proper use of food; that is affirmed.")],
            "There is no wasting of the earlier srotas.",
            "पूर्वेषां स्रोतसां ... नापचयो भवति."),
        order(1, "Put these parts of unit 106 in the line's order.",
              ["उत्तरोत्तरानुप्रवेशेऽपि च", "पूर्वेषां स्रोतसां", "यथाकालं", "सम्यगाहारोपयोगेन",
               "परिणामवताप्यायमानानां", "नापचयो भवति"],
              "Even with the later ones entering, of the earlier srotas, in due time, by proper food, nourished, no wasting.",
              "उत्तरोत्तरानुप्रवेशेऽपि च → पूर्वेषां स्रोतसां → यथाकालं → सम्यगाहारोपयोगेन → परिणामवताप्यायमानानां → नापचयो भवति."),
        match(2, "Match each word of unit 106 to its meaning.",
              [["पूर्वेषाम्", "of the earlier"], ["यथाकालम्", "in due time"], ["सम्यक्", "properly"],
               ["अपचयः", "wasting, diminution"], ["आप्यायमानानाम्", "being nourished"]],
              "Of the earlier ones, nourished properly in due time, there is no wasting.",
              "पूर्वेषाम्, यथाकालम्, सम्यक्, अपचयः, आप्यायमानानाम्.", role="extend",
              teaches="उत्तर 'later' and पूर्व 'earlier' are this unit's pair: the later ones enter, yet the earlier do not waste."),
        mcq("discriminate", 3, "Which split of नापचयो in unit 106 is right?",
            ("न + अपचयः", "अ + अ → आ; अपचयः before the voiced भ of भवति becomes अपचयो."),
            [("ना + पचयः", "पचयः is not the word here; the word is अपचयः (wasting)."),
             ("न + उपचयः", "अ + उ would give ओ: नोपचयो; उपचय means growth, the opposite."),
             ("नः + अपचयः", "अः before अ would give नोऽपचयो, not नापचयो.")],
            "न (not) + अपचयः (wasting): अ + अ → आ.",
            "अ + अ → आ."),
        mcq("apply", 4, "By unit 106, by what are the earlier srotas nourished?",
            ("By the proper use of food, in due time", "यथाकालं सम्यगाहारोपयोगेन: in due time, by the proper use of food."),
            [("By fasting, at long and irregular intervals", "Fasting is not named; proper use of food is."),
             ("By medicines, taken only at night", "No medicine is named in unit 106."),
             ("By sleep and the rest of the body", "Sleep is not named in unit 106.")],
            "They are nourished in due time by the proper use of food.",
            "यथाकालं सम्यगाहारोपयोगेन ... आप्यायमानानां."),
        mcq("transfer", 5, "By the rule of नापचयो, how is न + अस्ति (is not) joined in a new example?",
            ("नास्ति", "अ + अ → आ, as न + अपचयः → नापचयः."),
            [("नेस्ति", "ए comes from अ + इ, not from अ + अ."),
             ("नोस्ति", "ओ comes from अ + उ, not from अ + अ."),
             ("नस्ति", "Two अ merge into a long आ, not a short अ.")],
            "न + अस्ति = नास्ति, like न + अपचयः = नापचयः.",
            "अ + अ → आ.",
            teaches="Two short अ merge into long आ: न + अपचयः → नापचयः."),
    ],
}

# ---------------------------------------------------------------- unit 107
AUTHORED["107"] = {
    "title": "ततश्चधात्वाख्याः प्रसादमलाः",
    "question": "By unit 107, what measure do the clear essences and the wastes follow?",
    "rule": ("Then the clear essences and wastes (प्रसादमलाः) called dhātus each follow only their own measure "
             "(स्वं स्वम् एव मानम्), according to age and body (यथावयःशरीरम्)."),
    "limits": ("Prose. 'Called dhātus' for the essences and wastes is a loose reading (data). No figure is given for any "
               "measure; the measures are not listed here."),
    "explain_hi": ("यह गद्य-पंक्ति कहती है: तब धातु कहलाने वाले प्रसाद (निर्मल सार) और मल अपना-अपना ही मान (माप) अपनाते हैं। "
                   "यह मान ‘यथावयःशरीरम्’ यानी आयु और शरीर के अनुसार है। "
                   "कोई संख्या या माप यहाँ नहीं दिया गया। "
                   "‘स्वं स्वम्’ की पुनरुक्ति ‘हर एक अपना’ का भाव देती है। "
                   "सन्धि: ततः + च → ततश्च; मानम् + अनुवर्तन्ते → मानमनुवर्तन्ते (स्वर से पहले म् रहता है)।"),
    "hook": "हर धातु अपना माप रखे: आयु और शरीर के हिसाब से।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 107, the measure of the essences and wastes goes according to what?",
            ("Age and body", "यथावयःशरीरम्: according to age and body."),
            [("Season and land", "Season and land are not named in unit 107."),
             ("Food and drink", "Food and drink are not named in unit 107."),
             ("Day and night", "Day and night are not named in unit 107.")],
            "They follow their own measure according to age and body.",
            "स्वंस्वमेव मानमनुवर्तंते यथावयःशरीरं."),
        order(1, "Put these words of unit 107 in the line's order.",
              ["ततश्च", "धात्वाख्याः", "प्रसादमलाः", "स्वंस्वमेव", "मानमनुवर्तंते", "यथावयःशरीरं"],
              "And then, called dhātus, the essences and wastes, each its own, follow the measure, by age and body.",
              "ततश्च → धात्वाख्याः → प्रसादमलाः → स्वंस्वमेव → मानमनुवर्तंते → यथावयःशरीरं."),
        match(2, "Match each word of unit 107 to its meaning.",
              [["प्रसाद", "clear essence"], ["मल", "waste"], ["मानम्", "measure"], ["अनुवर्तन्ते", "follow"],
               ["वयः", "age"], ["शरीर", "body"]],
              "The clear essences and wastes follow their measure by age and body.",
              "प्रसाद, मल, मानम्, अनुवर्तन्ते, वयः, शरीर.", role="extend",
              teaches="यथा + a noun makes 'according to': यथावयःशरीरम् = according to age and body."),
        mcq("discriminate", 3, "In unit 107, what does the repeated स्वं स्वम् (एव) mean?",
            ("Each its own measure only", "स्वं स्वम् एव: each its own, only."),
            [("One shared measure for all", "The repetition gives 'each its own', not one shared."),
             ("A measure doubled in size", "The repetition is distributive, not a doubling."),
             ("No fixed measure at all", "Each follows its own measure; a measure is affirmed.")],
            "स्वं स्वम् = each its own: every essence and waste keeps its own measure.",
            "स्वंस्वमेव मानमनुवर्तंते."),
        multi("apply", 4, "Which statements fit unit 107?",
              [("The unit gives a figure for each measure", "No figure is printed in unit 107."),
               ("The measure goes by age and body", "Right: यथावयःशरीरम्."),
               ("ततश्च = ततः + च, 'and then'", "Right: visarga before च → श्."),
               ("Only the essences follow a measure, not the wastes", "Both are named: प्रसादमलाः.")],
              [1, 2],
              "Essences and wastes each follow their own measure, by age and body; no figures are given.",
              "ततश्चधात्वाख्याः प्रसादमलाः स्वंस्वमेव मानमनुवर्तंते यथावयःशरीरं."),
        mcq("transfer", 5, "By the pattern of यथावयःशरीरम् (according to age and body), what does यथाशक्ति mean in a new example?",
            ("According to one's strength", "यथा + शक्ति = according to strength, as यथा + वयःशरीर."),
            [("Against one's strength", "यथा means according to, not against."),
             ("Without any strength", "यथा does not negate."),
             ("Beyond the limit of one's strength", "यथा keeps within, it does not exceed.")],
            "यथाशक्ति = according to one's strength, like यथावयःशरीरम् = according to age and body.",
            "यथा + noun = according to that noun.",
            teaches="यथा- + a noun gives an indeclinable 'according to X': यथावयःशरीरम्, यथाकालम्, यथास्वम्."),
    ],
}

# ---------------------------------------------------------------- unit 108
AUTHORED["108"] = {
    "title": "तत्राहाररसो व्यानविक्षिप्तो",
    "question": "By unit 108, where is the food-rasa cooked, and what does it nourish?",
    "rule": ("The food-rasa (आहाररसः), scattered by vyāna, is cooked in order (क्रमात्) in the dhātu-fires (धात्वग्निषु); "
             "having invigorated the body, it nourishes the dhātus and the wastes of the dhātus."),
    "limits": ("Prose, low confidence: damaged print. प्राम्रक्तादि is unclear (rasa-rakta-ādi is only a guess, not adopted) "
               "and समस्तु is uncertain; the parse of the long chain is provisional. No question on those words or on how "
               "the participles hang together."),
    "explain_hi": ("छपाई क्षतिग्रस्त है, इसलिए विश्वास कम है। "
                   "जो पक्का पढ़ा जाता है: आहार-रस, व्यान वायु से बिखेरा हुआ, धातुओं की अग्नियों (धात्वग्निषु) में क्रम से पकता है। "
                   "फिर वह शरीर को ऊर्जा देकर (देहमूर्जयित्वा) धातुओं और धातु-मलों को पुष्ट करता है (पुष्णाति)। "
                   "‘प्राम्रक्तादि’ अस्पष्ट है; ‘रस-रक्त-आदि’ केवल अनुमान है, अपनाया नहीं गया। "
                   "‘समस्तु’ का पाठ और अर्थ भी अनिश्चित है।"),
    "hook": "व्यान बिखेरे, धातु-अग्नियाँ पकाएँ, रस धातुओं को पाले।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 108, by which wind is the food-rasa scattered?",
            ("Vyāna", "व्यानविक्षिप्तः: scattered by vyāna."),
            [("Prāṇa", "Unit 108 names vyāna as the scatterer, not prāṇa."),
             ("Samāna", "Unit 108 names vyāna as the scatterer, not samāna."),
             ("Apāna", "Apāna is not named in unit 108.")],
            "The food-rasa is scattered by vyāna.",
            "तत्राहाररसो व्यानविक्षिप्तो."),
        match(1, "Match each word of unit 108 to its meaning.",
              [["आहाररसः", "food-rasa"], ["व्यान", "vyāna, a wind"], ["धात्वग्निषु", "in the dhātu-fires"],
               ["पच्यमानः", "being cooked"], ["पुष्णाति", "nourishes"]],
              "The food-rasa, scattered by vyāna, cooked in the dhātu-fires, nourishes.",
              "आहाररसः, व्यान, धात्वग्निषु, पच्यमानः, पुष्णाति."),
        order(2, "Put these printed words of unit 108 in the line's order.",
              ["तत्राहाररसो", "व्यानविक्षिप्तो", "धात्वग्निषु", "क्रमात्पच्यमानः", "देहमूर्जयित्वा", "धातून्धातुमलांश्च पुष्णाति"],
              "The rasa, scattered by vyāna, in the dhātu-fires, cooked in order, having invigorated the body, nourishes.",
              "तत्राहाररसो → व्यानविक्षिप्तो → धात्वग्निषु → क्रमात्पच्यमानः → देहमूर्जयित्वा → धातून्धातुमलांश्च पुष्णाति.",
              role="extend",
              teaches="The line moves from the rasa, to its cooking in the dhātu-fires, to what it nourishes."),
        mcq("discriminate", 3, "By unit 108, what does the food-rasa nourish?",
            ("The dhātus and the dhātu-wastes", "धातून्धातुमलांश्च पुष्णाति: the dhātus and the wastes of the dhātus."),
            [("The dhātus only, not their wastes", "The wastes of the dhātus are named too (धातुमलान्)."),
             ("The wastes only, not the dhātus", "The dhātus are named first (धातून्)."),
             ("The doṣas only, not the dhātus", "The doṣas are not named in unit 108.")],
            "It nourishes both the dhātus and the dhātu-wastes.",
            "धातून्धातुमलांश्च पुष्णाति."),
        mcq("apply", 4, "Which split of धात्वग्निषु in unit 108 is right?",
            ("धातु + अग्निषु", "उ before a different vowel becomes व्: धातु + अग्निषु → धात्वग्निषु."),
            [("धात्व + अग्निषु", "धात्व is not a stem; the stem is धातु."),
             ("धातौ + अग्निषु", "औ before a vowel becomes आव्: धाताव् अग्निषु."),
             ("धातु + वग्निषु", "वग्निषु is not a word; the व् comes from the उ.")],
            "धातु (dhātu) + अग्निषु (in the fires): उ + अ → व.",
            "उ + a different vowel → व् + that vowel."),
        mcq("transfer", 5, "By the rule of धात्वग्निषु, how is सु + अस्ति joined in a new example?",
            ("स्वस्ति", "उ before a different vowel becomes व्, as धातु + अग्निषु → धात्वग्निषु."),
            [("सोस्ति", "ओ comes from अ + उ, not from उ + अ."),
             ("सूस्ति", "ऊ comes from उ + उ; here उ meets अ."),
             ("सवस्ति", "अव् comes from ओ before a vowel; here the उ simply becomes व्.")],
            "सु + अस्ति = स्वस्ति, like धातु + अग्निषु = धात्वग्निषु.",
            "उ + अ → व.",
            teaches="उ before a different vowel becomes व्: धातु + अग्निषु → धात्वग्निषु."),
    ],
}

# ---------------------------------------------------------------- unit 109
AUTHORED["109"] = {
    "title": "अथान्नकिट्टमच्छं · रसस्य सारो रक्तं",
    "question": "By unit 109, what is the refuse of food, and what are the essence and the waste of rasa?",
    "rule": ("The refuse of food (अन्नकिट्टम्) is clear urine and thick dung (शकृत्). Of rasa the essence is blood (रक्त); "
             "the waste is Kapha and lasīkā (probably lymph or tissue fluid)."),
    "limits": ("Two printed lines, prose; the copula is understood. Lasīkā as lymph or tissue fluid is probable, not certain: "
               "no question on its identity. Printed कफ़ो is कफः (print habit)."),
    "explain_hi": ("पहली पंक्ति अन्न का किट्ट (अपशिष्ट) बताती है: स्वच्छ (अच्छ) मूत्र और घना (घन) शकृत् यानी विष्ठा। "
                   "दूसरी पंक्ति से धातुओं के सार और मल की सूची आरम्भ होती है: रस का सार रक्त है, और मल कफ तथा लसीका। "
                   "लसीका का अर्थ लसिका या ऊतक-द्रव सम्भावित है, निश्चित नहीं। "
                   "दोनों पंक्तियों में ‘है’ क्रिया समझी जाती है। "
                   "छपा ‘कफ़ो’ = कफः, छपाई की आदत।"),
    "hook": "अन्न का कचरा: मूत्र और विष्ठा; रस का सार रक्त, मल कफ।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 109, what is the essence (सार) of rasa?",
            ("Blood (rakta)", "रसस्य सारो रक्तम्: the essence of rasa is blood."),
            [("Flesh (māṃsa)", "Flesh is the essence of blood (unit 110)."),
             ("Fat (medas)", "Fat is the essence of flesh (unit 111)."),
             ("Marrow (majjā)", "Marrow is the essence of bone (unit 112).")],
            "Of rasa the essence is blood.",
            "रसस्य सारो रक्तं."),
        match(1, "Match each word of the first line of unit 109 to its meaning.",
              [["अच्छम्", "clear"], ["मूत्रम्", "urine"], ["घनम्", "thick"], ["शकृत्", "dung, stool"],
               ["किट्टम्", "refuse"]],
              "The refuse of food: clear urine, thick dung.",
              "अच्छम्, मूत्रम्, घनम्, शकृत्, किट्टम्."),
        order(2, "Put the words of the second line of unit 109 in the line's order.",
              ["रसस्य", "सारो", "रक्तं", "मलः", "कफ़ो", "लसीका च"],
              "Of rasa, the essence, blood; the waste, Kapha and lasīkā.",
              "रसस्य → सारो → रक्तं → मलः → कफ़ो → लसीका च.", role="extend",
              teaches="Each statement runs: the dhātu in the genitive, सारः and its essence, then मलः and its waste."),
        mcq("discriminate", 3, "By unit 109, which is clear and which is thick in the refuse of food?",
            ("Urine is clear; dung is thick", "अच्छं मूत्रं घनं शकृत्: clear urine, thick dung."),
            [("Urine is thick; dung is clear", "The other way round: अच्छं goes with मूत्रं."),
             ("Both urine and dung are clear", "घनं (thick) goes with शकृत्."),
             ("Both urine and dung are thick", "अच्छं (clear) goes with मूत्रं.")],
            "Clear urine and thick dung.",
            "अच्छं मूत्रं घनं शकृत्."),
        multi("apply", 4, "Which statements fit unit 109?",
              [("Kapha is named as a waste of rasa", "Right: मलः कफो लसीका च."),
               ("Blood is named as the waste of rasa", "Blood is the essence of rasa, not its waste."),
               ("Lasīkā is named as the essence of rasa", "Lasīkā is named with Kapha as the waste."),
               ("Urine and dung are the refuse of food", "Right: अन्नकिट्टम् ... मूत्रं ... शकृत्.")],
              [0, 3],
              "Food refuse: urine and dung; rasa: essence blood, waste Kapha and lasīkā.",
              "अथान्नकिट्टमच्छं मूत्रं घनं शकृत् · रसस्य सारो रक्तं मलः कफो लसीका च."),
        mcq("transfer", 5, "By the rule of सारः + रक्तम् → सारो रक्तम्, how is नरः + गच्छति joined in a new example?",
            ("नरो गच्छति", "अः before a voiced consonant becomes ओ, as सारः + रक्तम् → सारो रक्तम्."),
            [("नर गच्छति", "अः drops to अ before vowels other than अ, not before a consonant."),
             ("नरर्गच्छति", "र् comes from a visarga after vowels other than अ and आ."),
             ("नरस्गच्छति", "स् is the form before त or थ, not before ग.")],
            "नरः + गच्छति = नरो गच्छति, like सारः + रक्तम् = सारो रक्तम्.",
            "अः before a voiced consonant → ओ.",
            teaches="अः before a voiced consonant becomes ओ: सारः + रक्तम् → सारो रक्तम्."),
    ],
}

# ---------------------------------------------------------------- unit 110
AUTHORED["110"] = {
    "title": "रक्तस्य सारो मांसं",
    "question": "By unit 110, what are the essence and the waste of blood?",
    "rule": ("Of blood (रक्त) the essence is flesh (मांस); kaṇḍarās (probably large tendons) and sirās (vessels) are named "
             "too; the waste (मल) is Pitta."),
    "limits": ("Prose; the copula is understood. Whether kaṇḍarā and sirā are part of the essence or a separate product is not "
               "stated: no question on it. Kaṇḍarā as large tendons is probable."),
    "explain_hi": ("यह गद्य-पंक्ति रक्त का सार और मल बताती है: सार मांस है; मल पित्त है। "
                   "बीच में कण्डराएँ (सम्भवतः बड़े टेंडन) और सिराएँ आती हैं; ये सार का भाग हैं या अलग उत्पाद, यह पंक्ति नहीं कहती। "
                   "ढाँचा इकाई १०९ जैसा है: षष्ठी (रक्तस्य), फिर सार, फिर मल। "
                   "सन्धि: सारः + मांसम् → सारो मांसम्; सिराः + च → सिराश्च।"),
    "hook": "रक्त से मांस बने, मल में पित्त।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 110, what is the waste (मल) of blood?",
            ("Pitta", "मलः पित्तम्: the waste of blood is Pitta."),
            [("Kapha", "Kapha is a waste of rasa (unit 109)."),
             ("Sweat", "Sweat is the waste of fat (unit 112)."),
             ("Urine", "Urine is the refuse of food (unit 109).")],
            "The waste of blood is Pitta.",
            "रक्तस्य ... मलः पित्तं."),
        order(1, "Put the words of unit 110 in the line's order.",
              ["रक्तस्य", "सारो", "मांसं", "कंडराः", "सिराश्च", "मलः पित्तं"],
              "Of blood, the essence, flesh; kaṇḍarās and sirās; the waste, Pitta.",
              "रक्तस्य → सारो → मांसं → कंडराः → सिराश्च → मलः पित्तं."),
        match(2, "Match each word of unit 110 to its meaning.",
              [["रक्तस्य", "of blood"], ["सारः", "essence"], ["मांसम्", "flesh"], ["मलः", "waste"], ["पित्तम्", "Pitta"]],
              "Of blood the essence is flesh; the waste is Pitta.",
              "रक्तस्य, सारः, मांसम्, मलः, पित्तम्.", role="extend",
              teaches="The genitive -स्य names the dhātu whose essence and waste follow: रक्तस्य = of blood."),
        mcq("discriminate", 3, "By unit 110, which is the essence (सार) of blood?",
            ("Flesh (māṃsa)", "रक्तस्य सारो मांसम्: the essence of blood is flesh."),
            [("Blood (rakta)", "Blood is the essence of rasa (unit 109), not of itself."),
             ("Pitta (a doṣa)", "Pitta is the waste of blood, not its essence."),
             ("Fat (medas)", "Fat is the essence of flesh (unit 111).")],
            "Of blood the essence is flesh.",
            "रक्तस्य सारो मांसं."),
        multi("apply", 4, "Which statements fit unit 110?",
              [("Kapha is the waste of blood", "Kapha is a waste of rasa (unit 109); blood's waste is Pitta."),
               ("Pitta is the waste of blood", "Right: मलः पित्तम्."),
               ("Blood is the essence of flesh", "The other way round: flesh is the essence of blood."),
               ("Flesh is the essence of blood", "Right: रक्तस्य सारो मांसम्.")],
              [1, 3],
              "Of blood: essence flesh, waste Pitta.",
              "रक्तस्य सारो मांसं ... मलः पित्तं."),
        mcq("transfer", 5, "By the pattern of रक्त → रक्तस्य (of blood), which form of वृक्ष (tree) means of the tree in a new example?",
            ("वृक्षस्य", "An अ-stem takes -स्य in the genitive singular, as रक्त → रक्तस्य."),
            [("वृक्षाय", "वृक्षाय is the dative: for the tree."),
             ("वृक्षेण", "वृक्षेण is the instrumental: by the tree."),
             ("वृक्षात्", "वृक्षात् is the ablative: from the tree.")],
            "वृक्षस्य = of the tree, like रक्तस्य = of blood.",
            "अ-stem, genitive singular: -स्य.",
            teaches="An अ-stem forms its genitive singular in -स्य: रक्त → रक्तस्य, रस → रसस्य."),
    ],
}

# ---------------------------------------------------------------- unit 111
AUTHORED["111"] = {
    "title": "मांसस्यसारो मेदस्त्वचो वसा च",
    "question": "By unit 111, what are the essence and the refuse of flesh?",
    "rule": ("Of flesh (मांस) the essence is fat (मेदस्), the skins (त्वचः) and vasā (muscle fat); the refuse (किट्ट) is the "
             "wastes of the ear, eye, nose, mouth, hair-pores and genital organ."),
    "limits": ("Prose; the copula is understood. त्वचः is taken as a plural (layers of skin). The print leaves a space before "
               "मलाः though it closes one compound. The unit does not describe these wastes."),
    "explain_hi": ("मांस का सार तीन नाम लेता है: मेद (चर्बी), त्वचाएँ और वसा (मांस की चर्बी)। "
                   "मांस का किट्ट छह स्थानों के मल हैं: कान, आँख, नाक, मुख, रोमकूप और प्रजनन (जननेन्द्रिय)। "
                   "ये छह एक द्वन्द्व समास में हैं जो ‘मलाः’ पर पूरा होता है; छपाई में ‘मलाः’ से पहले जगह छूटी है। "
                   "‘त्वचः’ को बहुवचन (त्वचा की परतें) पढ़ा गया है। "
                   "सन्धि: मेदः + त्वचः → मेदस्त्वचः; कर्ण + अक्षि → कर्णाक्षि; नासिका + आस्य → नासिकास्य।"),
    "hook": "मांस से मेद, त्वचा, वसा; मल छह छिद्रों में।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 111, which is an essence of flesh?",
            ("Fat (medas)", "मांसस्य सारो मेदः: fat is an essence of flesh."),
            [("Bone (asthi)", "Bone is not named in unit 111; it first comes in unit 112."),
             ("Blood (rakta)", "Blood is the essence of rasa (unit 109)."),
             ("Marrow (majjā)", "Marrow is the essence of bone (unit 112).")],
            "Of flesh the essence is fat, the skins and vasā.",
            "मांसस्यसारो मेदस्त्वचो वसा च."),
        order(1, "Put the places of the wastes of flesh in the order of unit 111.",
              ["कर्ण", "अक्षि", "नासिका", "आस्य", "रोमकूप", "प्रजनन"],
              "Ear, eye, nose, mouth, hair-pores, genital organ.",
              "कर्ण → अक्षि → नासिका → आस्य → रोमकूप → प्रजनन."),
        match(2, "Match each word of unit 111 to its meaning.",
              [["मेदः", "fat"], ["त्वचः", "skins"], ["वसा", "vasā, muscle fat"], ["आस्य", "mouth"],
               ["रोमकूप", "hair-pore"], ["प्रजनन", "genital organ"]],
              "Essence: fat, skins, vasā; refuse: wastes of the mouth, hair-pores, genital organ and others.",
              "मेदः, त्वचः, वसा; आस्य, रोमकूप, प्रजनन.", role="extend",
              teaches="किट्ट (refuse) here is a list of six places in one compound that ends in मलाः (wastes)."),
        mcq("discriminate", 3, "Which split of मेदस्त्वचो in unit 111 is right?",
            ("मेदः + त्वचः", "Visarga before त → स्; त्वचः before the voiced व of वसा becomes त्वचो."),
            [("मेद + स्त्वचः", "स्त्वचः is not a word; the स् is the visarga of मेदः."),
             ("मेदम् + त्वचः", "म् before त would be written ं: मेदं त्वचः."),
             ("मेदत् + त्वचः", "त् + त would give त्त: मेदत्त्वचः.")],
            "मेदः (fat) + त्वचः (skins): visarga before त → स्.",
            "Visarga before त → स्."),
        multi("apply", 4, "Which statements fit unit 111?",
              [("The wastes of the eye are part of the refuse of flesh", "Right: अक्षि is in the compound before मलाः."),
               ("Sweat is named as the refuse of flesh", "Sweat is the refuse of fat (unit 112)."),
               ("Fat is named as the refuse of flesh", "Fat is the essence of flesh, not its refuse."),
               ("The wastes of the hair-pores are named", "Right: रोमकूप is in the compound.")],
              [0, 3],
              "Refuse of flesh: the wastes of ear, eye, nose, mouth, hair-pores, genital organ.",
              "किट्टं कर्णाक्षिनासिकास्यरोमकूपप्रजनन मलाः."),
        mcq("transfer", 5, "By the rule of नासिका + आस्य → नासिकास्य, how is विद्या + आलय (house of learning) joined in a new example?",
            ("विद्यालय", "आ + आ → आ, as नासिका + आस्य → नासिकास्य."),
            [("विद्येलय", "ए comes from अ/आ + इ, not from आ + आ."),
             ("विद्यालाय", "The two आ merge into one आ; they are not both kept."),
             ("विद्योलय", "ओ comes from अ/आ + उ, not from आ + आ.")],
            "विद्या + आलय = विद्यालय, like नासिका + आस्य = नासिकास्य.",
            "आ + आ → आ.",
            teaches="Two like vowels merge into one long vowel: नासिका + आस्य → नासिकास्य."),
    ],
}

# ---------------------------------------------------------------- unit 112
AUTHORED["112"] = {
    "title": "मेदसः सारोऽस्थिस्नायुसंधयः · अस्थ्नः सारो मज्जा",
    "question": "By unit 112, what are the essence and the waste of fat, and of bone?",
    "rule": ("Of fat (मेदस्) the essence is bone, snāyu (ligaments) and joints, as the data reads it; the waste (किट्ट) is "
             "sweat (स्वेद). Of bone the essence is marrow (मज्जा); the waste is head hair, body hair and nails."),
    "limits": ("Two printed lines, prose; the copula is understood. अस्थिस्नायुसन्धयः is read as three items; 'joints of bone "
               "and ligament' is possible: no question rests on the three-item reading. Printed मज्जाकिट्टं is read as two "
               "words (मज्जा, किट्टम्)."),
    "explain_hi": ("पहली पंक्ति: मेद (चर्बी) का सार अस्थि, स्नायु और सन्धियाँ हैं, और किट्ट पसीना (स्वेद)। "
                   "‘अस्थिस्नायुसन्धयः’ को तीन वस्तुओं की सूची पढ़ा गया; ‘अस्थि और स्नायु की सन्धियाँ’ भी सम्भव है। "
                   "दूसरी पंक्ति: अस्थि का सार मज्जा (हड्डी के भीतर का गूदा), और किट्ट केश, रोम (शरीर के बाल) और नख। "
                   "छपे ‘मज्जाकिट्टं’ में दो शब्द जुड़े छपे हैं; अर्थ (सार, फिर मल) के अनुसार इन्हें अलग पढ़ा गया। "
                   "सन्धि: सारः + अस्थि → सारोऽस्थि (अः + अ → ओ, अ का लोप ऽ से)।"),
    "hook": "मेद का किट्ट पसीना; हड्डी का सार मज्जा, मल बाल और नख।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 112, what is the waste (किट्ट) of fat (medas)?",
            ("Sweat", "मेदसः ... किट्टं स्वेदः: the waste of fat is sweat."),
            [("Pitta", "Pitta is the waste of blood (unit 110)."),
             ("Urine", "Urine is the refuse of food (unit 109)."),
             ("Kapha", "Kapha is a waste of rasa (unit 109).")],
            "The waste of fat is sweat.",
            "मेदसः ... किट्टं स्वेदः."),
        match(1, "Match each word of unit 112 to its meaning.",
              [["स्वेदः", "sweat"], ["मज्जा", "marrow"], ["केश", "hair of the head"], ["लोमन्", "body hair"],
               ["नखाः", "nails"], ["किट्टम्", "waste"]],
              "Sweat; marrow; head hair, body hair, nails; waste.",
              "स्वेदः, मज्जा, केश, लोमन्, नखाः, किट्टम्."),
        order(2, "Put these words of unit 112 in their order over the two lines.",
              ["मेदसः", "स्वेदः", "अस्थ्नः", "मज्जा", "केशलोमानि", "नखाः"],
              "Of fat ... sweat; of bone ... marrow ... hair and body hair, nails.",
              "मेदसः → स्वेदः → अस्थ्नः → मज्जा → केशलोमानि → नखाः.", role="extend",
              teaches="Each line runs: the dhātu in the genitive (मेदसः, अस्थ्नः), its essence, then its waste."),
        mcq("discriminate", 3, "Which split of सारोऽस्थि in unit 112 is right?",
            ("सारः + अस्थि", "अः before अ → ओ, and the अ is dropped (ऽ): सारोऽस्थि."),
            [("सारः + स्थि", "स्थि is not a word; ऽ marks a dropped अ of अस्थि."),
             ("सार + अस्थि", "अ + अ would give आ: सारास्थि."),
             ("सारम् + अस्थि", "म् before a vowel stays: सारमस्थि.")],
            "सारः (essence) + अस्थि (bone): अः + अ → ओऽ.",
            "अः + अ → ओ + ऽ."),
        mcq("apply", 4, "By unit 112, whose essence is marrow (majjā)?",
            ("Of bone (asthi)", "अस्थ्नः सारो मज्जा: the essence of bone is marrow."),
            [("Of fat (medas)", "Marrow is named after अस्थ्नः (of bone), not after मेदसः (of fat)."),
             ("Of flesh (māṃsa)", "The essence of flesh is fat (unit 111)."),
             ("Of blood (rakta)", "The essence of blood is flesh (unit 110).")],
            "Of bone the essence is marrow.",
            "अस्थ्नः सारो मज्जा."),
        mcq("transfer", 5, "By the rule of सारोऽस्थि, how is रामः + अपि (Rāma too) joined in a new example?",
            ("रामोऽपि", "अः before अ → ओ, the अ dropped (ऽ), as सारः + अस्थि → सारोऽस्थि."),
            [("रामापि", "अ + अ → आ is for a bare अ; here the अ has a visarga."),
             ("रामरपि", "र् comes from a visarga after vowels other than अ and आ."),
             ("राम अपि", "अः drops to अ before vowels other than अ; before अ it gives ओऽ.")],
            "रामः + अपि = रामोऽपि, like सारः + अस्थि = सारोऽस्थि.",
            "अः + अ → ओऽ.",
            teaches="अः before अ becomes ओ and the अ is dropped (ऽ): सारः + अस्थि → सारोऽस्थि."),
    ],
}

# ---------------------------------------------------------------- unit 113
AUTHORED["113"] = {
    "title": "मज्ज्ञस्तु सारः शुक्रं",
    "question": "By unit 113, what are the essence and the waste of marrow?",
    "rule": ("Of marrow (मज्जन्), however, the essence is śukra (semen); the waste (मल) is eye-excrement (अक्षिविट्) and the "
             "oiliness (स्नेह) of the skins."),
    "limits": ("Prose; the copula is understood; no 'and' joins the two wastes. Printed मज्ज्ञः is read as the genitive of "
               "majjan (marrow)."),
    "explain_hi": ("मज्जा का तो सार शुक्र (वीर्य) है। "
                   "मल दो हैं: आँख का मल (अक्षिविट्) और त्वचाओं का स्नेह (चिकनाई)। "
                   "दोनों के बीच ‘च’ (और) नहीं छपा। "
                   "‘मज्ज्ञः’ को मज्जन् (मज्जा) का षष्ठी एकवचन पढ़ा गया है। "
                   "सन्धि: मज्ज्ञः + तु → मज्ज्ञस्तु; मलः + अक्षिविट् → मलोऽक्षिविट् (अः + अ → ओ, ऽ)।"),
    "hook": "मज्जा से शुक्र; मल: आँख का मैल, त्वचा की चिकनाई।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 113, what is the essence of marrow?",
            ("Śukra (semen)", "मज्ज्ञस्तु सारः शुक्रम्: the essence of marrow is śukra."),
            [("Ojas (vital essence)", "Ojas is the essence of śukra (unit 114)."),
             ("Bone (asthi)", "Bone is not named in unit 113; marrow is the essence of bone (unit 112)."),
             ("Fat (medas)", "Fat is an essence of flesh (unit 111).")],
            "Of marrow the essence is śukra.",
            "मज्ज्ञस्तु सारः शुक्रं."),
        match(1, "Match each word of unit 113 to its meaning.",
              [["मज्ज्ञः", "of marrow"], ["सारः", "essence"], ["शुक्रम्", "śukra, semen"], ["अक्षिविट्", "eye-excrement"],
               ["स्नेहः", "oiliness"]],
              "Of marrow the essence is śukra; the waste, eye-excrement and the oiliness of the skins.",
              "मज्ज्ञः, सारः, शुक्रम्, अक्षिविट्, स्नेहः."),
        order(2, "Put the words of unit 113 in the line's order.",
              ["मज्ज्ञस्तु", "सारः", "शुक्रं", "मलोऽक्षिविट्", "त्वचां", "स्नेहः"],
              "Of marrow, however, the essence, śukra; the waste, eye-excrement, of the skins the oiliness.",
              "मज्ज्ञस्तु → सारः → शुक्रं → मलोऽक्षिविट् → त्वचां → स्नेहः.", role="extend",
              teaches="तु (however) follows the first word: मज्ज्ञः + तु → मज्ज्ञस्तु."),
        mcq("discriminate", 3, "By unit 113, which is a waste of marrow, not its essence?",
            ("The oiliness of the skins", "त्वचां स्नेहः is named after मलः, as a waste."),
            [("Śukra, the semen itself", "Śukra is the essence of marrow, not its waste."),
             ("The ojas, vital essence", "Ojas is the essence of śukra (unit 114)."),
             ("Sweat of the whole body", "Sweat is the waste of fat (unit 112).")],
            "Wastes of marrow: eye-excrement and the oiliness of the skins.",
            "मलोऽक्षिविट् त्वचां स्नेहः."),
        fill(4, "By unit 113, the essence of marrow is ____ (semen). Type it in Devanagari or in English letters (e.g. dharma).",
             accepts("शुक्रम्", None, "शुक्र", "shukra", "sukra"),
             "शुक्रम् (śukra, semen): मज्ज्ञस्तु सारः शुक्रम्.",
             "शुक्र = semen: the essence of marrow.",
             "मज्ज्ञस्तु सारः शुक्रं.", role="apply"),
        mcq("transfer", 5, "By the rule of मज्ज्ञः + तु → मज्ज्ञस्तु, how is बालाः + तिष्ठन्ति joined in a new example?",
            ("बालास्तिष्ठन्ति", "A visarga before त becomes स्, as मज्ज्ञः + तु → मज्ज्ञस्तु."),
            [("बाला तिष्ठन्ति", "After आ the visarga drops before a voiced sound or a vowel; त is not voiced."),
             ("बालो तिष्ठन्ति", "ओ comes from अः before a voiced consonant, not from आः."),
             ("बालाश्तिष्ठन्ति", "श् is the form before च or छ; before त it is स्.")],
            "बालाः + तिष्ठन्ति = बालास्तिष्ठन्ति, like मज्ज्ञः + तु = मज्ज्ञस्तु.",
            "Visarga before त → स्.",
            teaches="A visarga before त becomes स्: मज्ज्ञः + तु → मज्ज्ञस्तु."),
    ],
}

# ---------------------------------------------------------------- unit 114
AUTHORED["114"] = {
    "title": "शुक्रस्य सारमोजः",
    "question": "By unit 114, what is the essence of śukra?",
    "rule": ("Of śukra (semen) the essence (सारम्) is ojas (ओजः, vital essence): the last link of the chain of essences "
             "named dhātu by dhātu in units 109-113."),
    "limits": ("Prose; the copula is understood. सारम् (सारः in the neighbouring units) is read as neuter nominative; it may "
               "be an accusative with a verb understood: no question on its case or gender. No waste of śukra is named here."),
    "explain_hi": ("यह छोटी गद्य-पंक्ति कहती है: शुक्र का सार ओजस् (जीवन-सार) है। "
                   "इकाई १०९ से चली सारों की कड़ी यहाँ ओजस् पर पहुँचती है: रस → रक्त → मांस → मेद → अस्थि (इकाई ११२ के पाठ के अनुसार) → मज्जा → शुक्र → ओजस्। "
                   "यहाँ ‘सारम्’ है, पास की इकाइयों में ‘सारः’; इसे नपुंसक प्रथमा पढ़ा गया, पर समझी गई क्रिया के साथ द्वितीया भी सम्भव है। "
                   "सन्धि: सारम् + ओजः → सारमोजः (स्वर से पहले म् रहता है)।"),
    "hook": "कड़ी का अन्त: शुक्र का सार ओज।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 114, what is the essence of śukra?",
            ("Ojas", "शुक्रस्य सारमोजः: the essence of śukra is ojas."),
            [("Marrow", "Marrow is the essence of bone (unit 112)."),
             ("Blood", "Blood is the essence of rasa (unit 109)."),
             ("Pitta", "Pitta is the waste of blood (unit 110).")],
            "Of śukra the essence is ojas.",
            "शुक्रस्य सारमोजः."),
        match(1, "Match each word of unit 114 to its meaning.",
              [["शुक्रस्य", "of śukra"], ["सारम्", "essence"], ["ओजः", "ojas, vital essence"]],
              "Of śukra the essence is ojas.",
              "शुक्रस्य, सारम्, ओजः."),
        order(2, "Put these in the order in which units 110-114 first name them.",
              ["मांस", "मेदस्", "अस्थि", "मज्जा", "शुक्र", "ओजस्"],
              "Flesh (110), fat (111), bone (112, as read: the essence of fat may instead be the joints), marrow (112), śukra (113), ojas (114).",
              "मांस → मेदस् → अस्थि → मज्जा → शुक्र → ओजस्.", role="extend",
              teaches="Units 110-114 go dhātu by dhātu: each line opens with a dhātu in the genitive, then its essence and waste."),
        mcq("discriminate", 3, "In unit 114, what is the relation of ojas to śukra?",
            ("Ojas is the essence of śukra", "शुक्रस्य सारम् ओजः: ojas is the essence of śukra."),
            [("Śukra is the essence of ojas", "The other way round: शुक्रस्य is the genitive."),
             ("Ojas is the waste of śukra", "सारम् is essence; no waste is named here."),
             ("Ojas is the source of śukra", "Ojas comes from śukra as its essence.")],
            "Ojas is the essence of śukra.",
            "शुक्रस्य सारमोजः."),
        multi("apply", 4, "Which statements fit unit 114?",
              [("Unit 114 names a waste of śukra", "No waste is named in unit 114."),
               ("Unit 114 has a printed verb", "No verb is printed; the copula is understood."),
               ("शुक्रस्य is a genitive, 'of śukra'", "Right: the genitive -स्य names whose essence ojas is."),
               ("ओजः is the essence named in this unit", "Right: शुक्रस्य सारमोजः.")],
              [2, 3],
              "Of śukra (genitive) the essence is ojas; no verb and no waste are printed.",
              "शुक्रस्य सारमोजः."),
        mcq("transfer", 5, "By the rule of सारम् + ओजः → सारमोजः, how is फलम् + अस्ति joined in a new example?",
            ("फलमस्ति", "A final म् before a vowel stays and joins it, as सारम् + ओजः → सारमोजः."),
            [("फलं अस्ति", "ं is written for म् before a consonant, not before a vowel."),
             ("फलोस्ति", "म् does not drop, and अ + अ would not give ओ."),
             ("फलास्ति", "म् does not drop before a vowel.")],
            "फलम् + अस्ति = फलमस्ति, like सारम् + ओजः = सारमोजः.",
            "Final म् before a vowel stays: म् + vowel.",
            teaches="A final म् before a vowel stays and joins it: सारम् + ओजः → सारमोजः."),
    ],
}

# ---------------------------------------------------------------- unit 115
AUTHORED["115"] = {
    "title": "अत्यंतशुद्धतया चास्मिन्मलाभावः",
    "question": "By unit 115, why is there no waste here, and what do others not accept?",
    "rule": ("Through extreme purity (अत्यन्तशुद्धतया) there is no waste (मलाभावः) in this; others, for this very reason "
             "(अत एव), do not accept its cooking (पाक)."),
    "limits": ("Two printed lines, prose. 'In this' (अस्मिन्) and 'of it' (तस्य) are not tied to a noun in the unit (the data "
               "reads them as the śukra/ojas of unit 114): no question on what they refer to. Literally नेच्छन्ति is 'do not "
               "wish'; 'do not accept' is the natural sense."),
    "explain_hi": ("पहली पंक्ति: अत्यन्त शुद्धता के कारण इसमें मल का अभाव है। "
                   "‘इसमें’ (अस्मिन्) किसके लिए है, पंक्ति में कोई संज्ञा नहीं; डेटा इसे इकाई ११४ का शुक्र/ओजस् पढ़ता है। "
                   "दूसरी पंक्ति एक अन्य मत देती है: दूसरे लोग इसी कारण (अत एव) उसका पाक (पकना) नहीं मानते। "
                   "‘नेच्छन्ति’ का शब्दार्थ ‘नहीं चाहते’ है; ‘स्वीकार नहीं करते’ स्वाभाविक अर्थ है। "
                   "सन्धि: न + इच्छन्ति → नेच्छन्ति (अ + इ → ए); पुनर् + अतः → पुनरतः; अतः + एव → अत एव।"),
    "hook": "इतना शुद्ध कि मल नहीं; इसीलिए कुछ कहते: पाक भी नहीं।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 115, why is there no waste (mala) in this?",
            ("Through extreme purity", "अत्यन्तशुद्धतया: through extreme purity."),
            [("Through great heat", "Heat is not named in unit 115."),
             ("Through long cooking", "Cooking is named only as what others deny."),
             ("Through the wind vyāna", "No wind is named in unit 115.")],
            "Through extreme purity there is no waste in this.",
            "अत्यंतशुद्धतया चास्मिन्मलाभावः."),
        match(1, "Match each word of unit 115 to its meaning.",
              [["अत्यन्त", "extreme"], ["शुद्धता", "purity"], ["मलाभावः", "absence of waste"], ["अन्ये", "others"],
               ["पाकम्", "cooking"]],
              "Extreme purity, absence of waste; others deny cooking.",
              "अत्यन्त, शुद्धता, मलाभावः, अन्ये, पाकम्."),
        order(2, "Put the printed words of unit 115 in their order over the two lines.",
              ["अत्यंतशुद्धतया", "चास्मिन्मलाभावः", "अन्येपुनरतएव", "तस्य", "नेच्छंति", "पाकं"],
              "Through extreme purity, and in this no waste; others for this very reason do not accept its cooking.",
              "अत्यंतशुद्धतया → चास्मिन्मलाभावः → अन्येपुनरतएव → तस्य → नेच्छंति → पाकं.", role="extend",
              teaches="The first line gives the fact and its reason; the second gives the others' view, on the same ground (अत एव)."),
        mcq("discriminate", 3, "By unit 115, what do the others (अन्ये) not accept?",
            ("Its cooking (pāka)", "तस्य नेच्छन्ति पाकम्: they do not accept its cooking."),
            [("Its purity (śuddhatā)", "Purity is the reason given, not what is denied."),
             ("Its place (sthāna)", "No place is named in unit 115."),
             ("Its strength (bala)", "Strength is not named in unit 115.")],
            "Others do not accept its cooking (pāka).",
            "अन्येपुनरतएव तस्य नेच्छंति पाकं."),
        mcq("apply", 4, "Which split of नेच्छंति in unit 115 is right?",
            ("न + इच्छन्ति", "अ + इ → ए: न + इच्छन्ति → नेच्छन्ति."),
            [("ने + च्छन्ति", "च्छन्ति is not a word; the verb is इच्छन्ति."),
             ("न + एच्छन्ति", "एच्छन्ति is not a word; and अ + ए would give ऐ."),
             ("नः + इच्छन्ति", "अः before इ drops its visarga with no join: न इच्छन्ति.")],
            "न (not) + इच्छन्ति (wish, accept): अ + इ → ए.",
            "अ + इ → ए."),
        mcq("transfer", 5, "By the rule of नेच्छन्ति, how is न + इति (not, thus) joined in a new example?",
            ("नेति", "अ + इ → ए, as न + इच्छन्ति → नेच्छन्ति."),
            [("नोति", "ओ comes from अ + उ, not from अ + इ."),
             ("नाति", "आ comes from अ + अ, not from अ + इ."),
             ("नयिति", "अय् comes from ए before a vowel; here there is no ए.")],
            "न + इति = नेति, like न + इच्छन्ति = नेच्छन्ति.",
            "अ + इ → ए.",
            teaches="अ + इ → ए: न + इच्छन्ति → नेच्छन्ति."),
    ],
}


# ===================================================================== NOTES_HI
NOTES_HI = {
    "104": ("गद्य; विश्वास मध्यम; एक छपी पंक्ति (०२.०६.११५)। पाठ-चिह्न (सम्भावित): छपा ‘धातुवाख्यानां’ में उ अधिक लगता है; "
            "धातु + आख्यानाम् → धात्वाख्यानाम् (उ + आ → वा) पढ़ा गया; इस रूप पर कोई प्रश्न नहीं। ‘शारीरगुण’ धातुओं के लिए ढीला शब्द। "
            "सन्धि जाँची: तत् + आत्मक → तदात्मक (स्वर से पहले त् → द्); पारम्पर्येण + अव्यवच्छिन्न → पारम्पर्येणाव्यवच्छिन्न (अ + अ → आ); "
            "सन्तानम् + आपूर्यन्ते → सन्तानमापूर्यन्ते; छपे ‘पारंपर्ये’, ‘संतान’, ‘आपूर्यंते’ में ं = म्/न्।"),
    "105": ("गद्य; विश्वास मध्यम; एक छपी पंक्ति (०२.०६.११६)। छपा ‘स्त्रोतो’ = स्रोतो (वर्तनी)। पाठ-चिह्न (सम्भावित): छपा ‘यथाथमेव’ "
            "शब्द नहीं; ‘यथार्थमेव’ (आवश्यकता के अनुसार) सुझाया गया, र् छपाई में छूटा; इस पर कोई प्रश्न नहीं। "
            "सन्धि जाँची: स्रोतोभ्यः + च → स्रोतोभ्यश्च (च से पहले विसर्ग → श्); यथार्थम् + एव → यथार्थमेव।"),
    "106": ("गद्य; विश्वास मध्यम; एक छपी पंक्ति (०२.०६.११७); कोई पाठ-चिह्न नहीं। ‘उत्तरोत्तरानुप्रवेश’ का ठीक अर्थ अस्पष्ट, ढीला पढ़ा गया। "
            "डेटा ‘परिणामवताप्यायमानानां’ को परिणामवत् + आप्यायमानानाम् बाँटता है; पर त् स्वर से पहले द् बनता, इसलिए यह विभाजन सन्धि से नहीं "
            "बैठता (परिणामवता + आप्यायमानानाम् अधिक सम्भव); इस पर कोई प्रश्न नहीं। सन्धि जाँची: उत्तर + उत्तर → उत्तरोत्तर (अ + उ → ओ); "
            "अनुप्रवेशे + अपि → अनुप्रवेशेऽपि; सम्यक् + आहार → सम्यगाहार (स्वर से पहले क् → ग्); आहार + उपयोगेन → आहारोपयोगेन; "
            "न + अपचयः → नापचयः; अपचयः + भवति → अपचयो भवति (अः + घोष व्यंजन → ओ)।"),
    "107": ("गद्य; विश्वास मध्यम; एक छपी पंक्ति (०२.०६.११८); कोई पाठ-चिह्न नहीं। ‘धात्वाख्याः प्रसादमलाः’ का अर्थ ढीला (डेटा)। "
            "यथावयःशरीरम् = आयु और शरीर के अनुसार। सन्धि जाँची: ततः + च → ततश्च; धातु + आख्याः → धात्वाख्याः (उ + आ → वा); "
            "स्वम् + स्वम् → स्वंस्वम् (व्यंजन से पहले ं); मानम् + अनुवर्तन्ते → मानमनुवर्तन्ते।"),
    "108": ("गद्य; विश्वास कम; एक छपी पंक्ति (०२.०६.११९), छपाई क्षतिग्रस्त। पाठ-चिह्न: ‘प्राम्रक्तादि’ अस्पष्ट, ‘रसरक्तादि’ केवल अनुमान, "
            "अपनाया नहीं; ‘समस्तु’ = समः तु (अर्थ अनिश्चित) या समस्तः तु; लम्बी कृदन्त-शृंखला का विश्लेषण अस्थायी। इन पर कोई प्रश्न नहीं। "
            "सन्धि जाँची: तत्र + आहार → तत्राहार (अ + आ → आ); आहाररसः + व्यान → आहाररसो व्यान (अः + घोष व्यंजन → ओ); "
            "धातु + अग्निषु → धात्वग्निषु (उ + अ → व); धातुमलान् + च → धातुमलांश्च।"),
    "109": ("गद्य; विश्वास मध्यम; दो छपी पंक्तियाँ (०२.०६.१२०, ०२.०६.१२१); कोई पाठ-चिह्न नहीं। छपा ‘कफ़ो’ = कफः (फ़ छपाई की आदत)। "
            "लसीका = लसिका या ऊतक-द्रव (सम्भावित)। क्रिया समझी जाती है। सन्धि जाँची: अथ + अन्न → अथान्न (अ + अ → आ); "
            "अन्नकिट्टम् + अच्छम् → अन्नकिट्टमच्छम्; सारः + रक्तम् → सारो रक्तम् (अः + घोष व्यंजन → ओ)।"),
    "110": ("गद्य; विश्वास मध्यम; एक छपी पंक्ति (०२.०६.१२२); कोई पाठ-चिह्न नहीं। कण्डरा = बड़े टेंडन (सम्भावित); सिरा = वाहिनी। "
            "कण्डरा और सिरा सार का भाग हैं या अलग, यह अनिश्चित; इस पर कोई प्रश्न नहीं। छपा ‘कंडराः’ = कण्डराः। "
            "सन्धि जाँची: सारः + मांसम् → सारो मांसम्; सिराः + च → सिराश्च।"),
    "111": ("गद्य; विश्वास मध्यम; एक छपी पंक्ति (०२.०६.१२३); कोई पाठ-चिह्न नहीं। छपाई में ‘मलाः’ से पहले जगह है, पर एक ही समास। "
            "‘त्वचः’ बहुवचन (त्वचा की परतें) पढ़ा गया; ‘मांसस्यसारो’ छपाई में जुड़ा। सन्धि जाँची: मेदः + त्वचः → मेदस्त्वचः "
            "(त से पहले विसर्ग → स्); त्वचः + वसा → त्वचो वसा; कर्ण + अक्षि → कर्णाक्षि; नासिका + आस्य → नासिकास्य (आ + आ → आ)।"),
    "112": ("गद्य; विश्वास मध्यम; दो छपी पंक्तियाँ (०२.०६.१२४, ०२.०६.१२५)। ‘अस्थिस्नायुसन्धयः’ तीन वस्तुओं की सूची पढ़ी गई; "
            "‘अस्थि और स्नायु की सन्धियाँ’ भी सम्भव, इसलिए इस पर कोई प्रश्न नहीं। छपा ‘मज्जाकिट्टं’ दो शब्द (मज्जा, किट्टम्) पढ़ा गया, "
            "बीच में कोई सन्धि नहीं। सन्धि जाँची: सारः + अस्थि → सारोऽस्थि (अः + अ → ओ, ऽ); अस्थ्नः = अस्थि का षष्ठी एकवचन।"),
    "113": ("गद्य; विश्वास मध्यम; एक छपी पंक्ति (०२.०६.१२६); कोई पाठ-चिह्न नहीं। मज्ज्ञः = मज्जन् का षष्ठी एकवचन। दोनों मलों के बीच "
            "‘च’ नहीं छपा। सन्धि जाँची: मज्ज्ञः + तु → मज्ज्ञस्तु (त से पहले विसर्ग → स्); मलः + अक्षिविट् → मलोऽक्षिविट् (अः + अ → ओ, ऽ)।"),
    "114": ("गद्य; विश्वास उच्च; एक छपी पंक्ति (०२.०६.१२७); कोई पाठ-चिह्न नहीं। ‘सारम्’ यहाँ, पास की इकाइयों में ‘सारः’; "
            "नपुंसक प्रथमा पढ़ा गया, या (समझी गई क्रिया के साथ) द्वितीया, जिसमें पुंलिंग भी सम्भव; अर्थ एक; कारक या लिंग पर कोई प्रश्न नहीं। सन्धि जाँची: सारम् + ओजः → सारमोजः।"),
    "115": ("गद्य; विश्वास मध्यम; दो छपी पंक्तियाँ (०२.०६.१२८, ०२.०६.१२९)। छपाई में शब्द जुड़े: ‘चास्मिन्मलाभावः’ = च अस्मिन् "
            "मलाभावः, ‘अन्येपुनरतएव’ = अन्ये पुनर् अत एव (अन्ये और पुनर् के बीच कोई सन्धि नहीं)। ‘अस्मिन्’, ‘तस्य’ किसी संज्ञा से "
            "जुड़े नहीं; डेटा इन्हें इकाई ११४ का शुक्र/ओजस् पढ़ता है; इस पर कोई प्रश्न नहीं। सन्धि जाँची: च + अस्मिन् → चास्मिन्; "
            "मल + अभावः → मलाभावः; पुनर् + अतः → पुनरतः; अतः + एव → अत एव; न + इच्छन्ति → नेच्छन्ति (अ + इ → ए)।"),
}


# ===================================================================== AIDS
AIDS = {
    "104": {
        "chain": {"steps": ["इकाई १०३: सार (रस) और मल (किट्ट)", "ताभ्याम्: उन दोनों से", "धातुओं के स्रोतस्",
                            "यथास्वम्: अपने-अपने अनुसार", "पारम्पर्येण: क्रम से", "अटूट प्रवाह में भरे जाते हैं"]},
        "chunks": "ताभ्यां च सारमलाभ्यां | तदात्मकानामेव | शारीरगुणानां धातुवाख्यानां | यथास्वं स्रोतांसि | पारंपर्येणाव्यवच्छिन्नसंतानमापूर्यंते",
        "sandhi": "स्वर से पहले त् → द्: तत् + आत्मक → तदात्मक · अ + अ → आ: पारम्पर्येण + अव्यवच्छिन्न → पारम्पर्येणाव्यवच्छिन्न · स्वर से पहले म्: सन्तानम् + आपूर्यन्ते → सन्तानमापूर्यन्ते।",
        "anchors": "नहर में पानी बिना रुके, एक के बाद एक खेत भरता है; वैसे ही स्रोतस् भरते हैं। (मेरी याद-पद्धति, पाठ की उपमा नहीं)",
    },
    "105": {
        "chunks": "स्त्रोतोभ्यश्च | यथाविभागं | यथाथमेव | धातवः पुष्यंति",
        "sandhi": "च से पहले विसर्ग → श्: स्रोतोभ्यः + च → स्रोतोभ्यश्च।",
        "frame": "कहाँ से: स्रोतोभ्यः → कैसे: यथाविभागम् (और सम्भावित पाठ यथार्थम्) → कौन: धातवः → क्या: पुष्यन्ति (पुष्ट होते हैं)।",
    },
    "106": {
        "chunks": "उत्तरोत्तरानुप्रवेशेऽपि च | पूर्वेषां स्रोतसां | यथाकालं | सम्यगाहारोपयोगेन | परिणामवताप्यायमानानां | नापचयो भवति",
        "seesaw": "उत्तर (बाद वाले) ⇄ पूर्व (पहले वाले): बाद वालों का प्रवेश होता है, फिर भी पहले वालों का अपचय नहीं।",
        "sandhi": "अ + उ → ओ: उत्तर + उत्तर → उत्तरोत्तर · स्वर से पहले क् → ग्: सम्यक् + आहार → सम्यगाहार · अ + अ → आ: न + अपचयः → नापचयः · अः + घोष व्यंजन → ओ: अपचयः + भवति → अपचयो भवति।",
        "frame": "भी होने पर: बाद वालों का प्रवेश → किनका: पूर्वेषां स्रोतसाम् → कैसे पोषित: यथाकालं, सम्यक् आहार से → फल: नापचयो भवति।",
    },
    "107": {
        "chunks": "ततश्चधात्वाख्याः | प्रसादमलाः | स्वंस्वमेव | मानमनुवर्तंते | यथावयःशरीरं",
        "sandhi": "च से पहले विसर्ग → श्: ततः + च → ततश्च · उ + आ → वा: धातु + आख्याः → धात्वाख्याः · स्वर से पहले म्: मानम् + अनुवर्तन्ते → मानमनुवर्तन्ते।",
        "frame": "कौन: प्रसादमलाः (धातु कहलाने वाले) → क्या करते: स्वं स्वं मानम् अनुवर्तन्ते → किसके अनुसार: वयः और शरीर।",
    },
    "108": {
        "chain": {"steps": ["आहार-रस", "व्यान वायु से बिखरा", "धातु-अग्नियों में क्रम से पकता", "शरीर को ऊर्जा देकर",
                            "धातुओं और धातु-मलों को पुष्ट करता"]},
        "chunks": "तत्राहाररसो | व्यानविक्षिप्तो | यथास्वं समस्तु | धात्वग्निषु | क्रमात्पच्यमानः | स्वात्मभावप्रच्युतिसमनंतरमेव | प्राम्रक्तादिधातुसंज्ञकः | कालवदस्खलितबलप्रमाणो | देहमूर्जयित्वा | धातून्धातुमलांश्च पुष्णाति",
        "sandhi": "अ + आ → आ: तत्र + आहार → तत्राहार · उ + अ → व: धातु + अग्निषु → धात्वग्निषु · अः + घोष व्यंजन → ओ: आहाररसः + व्यान → आहाररसो व्यान।",
        "frame": "कौन: आहाररसः → किससे बिखरा: व्यान → कहाँ पकता: धात्वग्निषु, क्रम से → क्या करता: देह को ऊर्जा देकर धातुओं और धातु-मलों को पुष्ट।",
    },
    "109": {
        "diagram": {"groups": [
            {"label": "अन्न का किट्ट", "items": ["मूत्र (स्वच्छ)", "शकृत् (घना)"]},
            {"label": "रस", "items": ["सार: रक्त", "मल: कफ", "मल: लसीका (सम्भावित: लसिका)"]}]},
        "chunks": "अथान्नकिट्टमच्छं | मूत्रं | घनं शकृत् || रसस्य सारो रक्तं | मलः कफ़ो लसीका च",
        "sandhi": "अ + अ → आ: अथ + अन्न → अथान्न · अः + घोष व्यंजन → ओ: सारः + रक्तम् → सारो रक्तम्।",
        "frame": "किसका: रसस्य → सार: रक्तम् → मल: कफः, लसीका।",
    },
    "110": {
        "chunks": "रक्तस्य | सारो मांसं | कंडराः सिराश्च | मलः पित्तं",
        "sandhi": "अः + घोष व्यंजन → ओ: सारः + मांसम् → सारो मांसम् · च से पहले विसर्ग → श्: सिराः + च → सिराश्च।",
        "frame": "किसका: रक्तस्य → सार: मांसम् → साथ में छपे: कण्डराः, सिराः → मल: पित्तम्।",
    },
    "111": {
        "diagram": {"groups": [
            {"label": "मांस का सार", "items": ["मेद (चर्बी)", "त्वचः (त्वचाएँ)", "वसा (मांस की चर्बी)"]},
            {"label": "मांस का किट्ट: इनके मल", "items": ["१ कर्ण (कान)", "२ अक्षि (आँख)", "३ नासिका (नाक)", "४ आस्य (मुख)",
                                                     "५ रोमकूप", "६ प्रजनन (जननेन्द्रिय)"]}]},
        "chunks": "मांसस्यसारो | मेदस्त्वचो वसा च | किट्टं | कर्णाक्षिनासिकास्यरोमकूपप्रजनन मलाः",
        "sandhi": "त से पहले विसर्ग → स्: मेदः + त्वचः → मेदस्त्वचः · अ + अ → आ: कर्ण + अक्षि → कर्णाक्षि · आ + आ → आ: नासिका + आस्य → नासिकास्य।",
        "letters": "छह स्थानों के पहले अक्षर क्रम से: क-अ-ना-आ-रो-प्र। (मेरी याद-पद्धति)",
    },
    "112": {
        "diagram": {"groups": [
            {"label": "मेद", "items": ["सार: अस्थि, स्नायु, सन्धि (पढ़े अनुसार)", "किट्ट: स्वेद (पसीना)"]},
            {"label": "अस्थि", "items": ["सार: मज्जा", "किट्ट: केश, रोम, नख"]}]},
        "chunks": "मेदसः | सारोऽस्थिस्नायुसंधयः | किट्टं स्वेदः || अस्थ्नः | सारो मज्जाकिट्टं | केशलोमानि नखाः",
        "sandhi": "अः + अ → ओ, अ का लोप (ऽ): सारः + अस्थि → सारोऽस्थि · अः + घोष व्यंजन → ओ: सारः + मज्जा → सारो मज्जा।",
        "frame": "किसका: मेदसः → सार: अस्थि-स्नायु-सन्धि → किट्ट: स्वेद || किसका: अस्थ्नः → सार: मज्जा → किट्ट: केश, लोम, नख।",
    },
    "113": {
        "chunks": "मज्ज्ञस्तु | सारः शुक्रं | मलोऽक्षिविट् | त्वचां स्नेहः",
        "sandhi": "त से पहले विसर्ग → स्: मज्ज्ञः + तु → मज्ज्ञस्तु · अः + अ → ओ, ऽ: मलः + अक्षिविट् → मलोऽक्षिविट्।",
        "frame": "किसका: मज्ज्ञः (मज्जा का) → सार: शुक्रम् → मल: अक्षिविट्, त्वचाओं का स्नेह।",
    },
    "114": {
        "chain": {"steps": ["रस", "रक्त (इकाई १०९)", "मांस (इकाई ११०)", "मेद (इकाई १११)", "अस्थि (इकाई ११२, पढ़े अनुसार)",
                            "मज्जा (इकाई ११२)", "शुक्र (इकाई ११३)", "ओजस् (इकाई ११४)"]},
        "chunks": "शुक्रस्य | सारमोजः",
        "sandhi": "स्वर से पहले म् रहता है: सारम् + ओजः → सारमोजः।",
        "letters": "सारों की कड़ी के पहले अक्षर: र-र-मां-मे-अ-म-शु-ओ (रस से ओजस् तक)। (मेरी याद-पद्धति)",
    },
    "115": {
        "chunks": "अत्यंतशुद्धतया | चास्मिन्मलाभावः || अन्येपुनरतएव | तस्य | नेच्छंति पाकं",
        "sandhi": "अ + इ → ए: न + इच्छन्ति → नेच्छन्ति · अ + अ → आ: च + अस्मिन् → चास्मिन्, मल + अभावः → मलाभावः · अ के सिवा किसी स्वर से पहले अः → अ: अतः + एव → अत एव।",
        "frame": "कारण: अत्यन्त शुद्धता → फल: मल का अभाव || अन्य मत: इसी कारण (अत एव) → उसका पाक नहीं मानते।",
    },
}


# ===================================================================== IMAGE_SPECS
IMAGE_SPECS = {
    ("104", "chain"): {
        "file": "sh6-saramala-104.svg",
        "alt": ("Chain of unit 104: the essence (rasa) and waste (kiṭṭa) of unit 103; by those two; the srotas of the dhātus; "
                "each according to its own; in succession; filled in an unbroken stream."),
        "type": "chain",
        "title": "इकाई १०४: सार और मल से स्रोतस् भरना",
        "steps": ["इकाई १०३: सार (रस) और मल (किट्ट)", "ताभ्याम्: उन दोनों से", "धातुओं के स्रोतस्",
                  "यथास्वम्: अपने-अपने अनुसार", "पारम्पर्येण: क्रम से", "अटूट प्रवाह में भरे जाते हैं"],
    },
    ("108", "chain"): {
        "file": "sh6-aharrasa-108.svg",
        "alt": ("Chain of the sure parts of unit 108: food-rasa; scattered by vyāna; cooked in order in the dhātu-fires; "
                "having invigorated the body; nourishes the dhātus and the dhātu-wastes. Unclear words are left out."),
        "type": "chain",
        "title": "इकाई १०८: आहार-रस (केवल पक्के अंश)",
        "steps": ["आहार-रस", "व्यान वायु से बिखरा", "धातु-अग्नियों में क्रम से पकता", "शरीर को ऊर्जा देकर",
                  "धातुओं और धातु-मलों को पुष्ट करता"],
    },
    ("109", "diagram"): {
        "file": "sh6-annakitta-109.svg",
        "alt": ("Two columns of unit 109. Refuse of food: urine (clear), dung (thick). Rasa: essence blood; waste Kapha; "
                "waste lasīkā (probably lymph)."),
        "type": "split",
        "title": "इकाई १०९: अन्न का किट्ट और रस",
        "cols": [["अन्न का किट्ट", ["मूत्र (स्वच्छ)", "शकृत् (घना)"]],
                 ["रस", ["सार: रक्त", "मल: कफ", "मल: लसीका (सम्भावित: लसिका)"]]],
    },
    ("111", "diagram"): {
        "file": "sh6-mamsa-kitta-111.svg",
        "alt": ("Two columns of unit 111. Essence of flesh: fat, skins, vasā (muscle fat). Refuse of flesh, the wastes of, "
                "numbered in printed order: 1 ear, 2 eye, 3 nose, 4 mouth, 5 hair-pores, 6 genital organ."),
        "type": "split",
        "title": "इकाई १११: मांस का सार और किट्ट",
        "cols": [["मांस का सार", ["मेद (चर्बी)", "त्वचः (त्वचाएँ)", "वसा (मांस की चर्बी)"]],
                 ["किट्ट: इनके मल", ["१ कर्ण (कान)", "२ अक्षि (आँख)", "३ नासिका (नाक)", "४ आस्य (मुख)", "५ रोमकूप",
                                    "६ प्रजनन (जननेन्द्रिय)"]]],
    },
    ("112", "diagram"): {
        "file": "sh6-medas-asthi-112.svg",
        "alt": ("Table of unit 112. Fat: essence bone, snāyu and joints (as read); waste sweat. Bone: essence marrow; "
                "waste head hair, body hair and nails."),
        "type": "table",
        "title": "इकाई ११२: मेद और अस्थि",
        "heads": ["धातु", "सार / किट्ट"],
        "rows": [["मेद", "सार: अस्थि, स्नायु, सन्धि (पढ़े अनुसार)"], ["मेद", "किट्ट: स्वेद (पसीना)"],
                 ["अस्थि", "सार: मज्जा"], ["अस्थि", "किट्ट: केश, रोम, नख"]],
    },
    ("114", "chain"): {
        "file": "sh6-sara-shrinkhala-114.svg",
        "alt": ("Chain of essences, units 109-114, each the essence of the one before: rasa, blood (109), flesh (110), "
                "fat (111), bone (112, as read: the essence of fat may instead be the joints), marrow (112), śukra (113), ojas (114)."),
        "type": "chain",
        "title": "इकाई १०९-११४: सारों की कड़ी (हर एक पिछले का सार)",
        "steps": ["रस", "रक्त (इकाई १०९)", "मांस (इकाई ११०)", "मेद (इकाई १११)", "अस्थि (इकाई ११२, पढ़े अनुसार)",
                  "मज्जा (इकाई ११२)", "शुक्र (इकाई ११३)", "ओजस् (इकाई ११४)"],
    },
}
