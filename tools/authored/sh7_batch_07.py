from helpers import mcq, match, order, fill, multi, accepts


def T(q, teaches):
    q["teaches"] = teaches
    return q


AUTHORED = {}

# ---------------------------------------------------------------- unit 82
AUTHORED["82"] = {
    "title": "शेषाणि षट्पंचाशदंगुलदलप्रमाणानि",
    "question": "By unit 82, how many marmas remain, and of what measure are they?",
    "rule": ("The remaining ones (शेषाणि) are fifty-six (षट्पञ्चाशत्), of the measure of an aṅgula-dala: dala is "
             "probably 'half', so probably half a finger-breadth (aṅgula)."),
    "limits": ("Prose, no verb; 'marma' is understood, not printed. dala = half is only probable (also petal, part): no "
               "question takes 'half' as sure. The remaining marmas are not named; no total for units 79-82 is stated."),
    "explain_hi": ("यह इकाई माप के अनुसार मर्मों के पाँच भेदों की अन्तिम कड़ी है, जिनकी बात इकाई ७७ (‘पाँच प्रकार से बँटता है’) से चली। "
                   "शेष छप्पन मर्म ‘अंगुलदल’ के माप के हैं। "
                   "‘दल’ का अर्थ यहाँ सम्भवतः आधा है, यानी सम्भवतः आधा अंगुल; यह शब्द पत्ती या भाग भी होता है, इसलिए यह अर्थ पक्का नहीं। "
                   "पंक्ति में कोई क्रिया नहीं और ‘मर्म’ शब्द भी नहीं छपा; वह अध्याय के विषय से समझा जाता है। "
                   "इकाई ७९ से ८२ में छपी संख्याएँ १२, ६, ४, २९ और ५६ हैं; उनका जोड़ १०७ बैठता है, पर पाठ यहाँ यह जोड़ नहीं कहता। "
                   "‘षट्पंचाशदंगुल’ में पञ्चाशत् का त् स्वर अ से पहले द् बना है।"),
    "hook": "शेष छप्पन, अंगुलदल भर के।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 82, how many marmas are said to remain?",
            ("Fifty-six", "षट्पञ्चाशत् = six and fifty: fifty-six."),
            [("Twenty-nine", "Twenty-nine are the group measured by the palm (unit 81)."),
             ("Sixty-five", "षट् + पञ्चाशत् is six and fifty; sixty-five would be पञ्चषष्टिः."),
             ("Twelve", "Twelve are the group of one's own finger-breadth (unit 79).")],
            "शेषाणि षट्पञ्चाशत्: the remaining are fifty-six.",
            "षट् (six) + पञ्चाशत् (fifty) = 56."),
        order(1, "Put the printed parts of unit 82 in the line's order.",
              ["शेषाणि", "षट्पंचाशद्", "अंगुलदल", "प्रमाणानि"],
              "The remaining; fifty-six; of an aṅgula-dala; in measure.",
              "शेषाणि → षट्पंचाशद् → अंगुलदल → प्रमाणानि."),
        match(2, "Match each word of unit 82 to its meaning.",
              [["शेष", "remaining"], ["षट्", "six"], ["पञ्चाशत्", "fifty"], ["अङ्गुल", "finger-breadth"],
               ["प्रमाण", "measure"]],
              "शेषाणि = the remaining; षट्पञ्चाशत् = fifty-six; अङ्गुल-दल-प्रमाणानि = of an aṅgula-dala's measure.",
              "शेष, षट्, पञ्चाशत्, अङ्गुल, प्रमाण.", role="extend",
              teaches="In a number like षट्पञ्चाशत् the smaller number comes first: six + fifty = fifty-six."),
        mcq("discriminate", 3, "Which split of षट्पंचाशदंगुल in unit 82 is right?",
            ("षट्पञ्चाशत् + अङ्गुल", "त् before a vowel becomes द्: -शत् + अङ्गुल → -शदङ्गुल."),
            [("षट्पञ्चाशः + अङ्गुल", "A visarga before अ would not give द्; the numeral is पञ्चाशत्."),
             ("षट्पञ्च + आशदङ्गुल", "आशदङ्गुल is not a word; षट्पञ्चाशत् is one numeral."),
             ("षट्पञ्चाशत् + दङ्गुल", "दङ्गुल is not a word; the द् comes from the त् of पञ्चाशत्.")],
            "षट्पञ्चाशत् (fifty-six) + अङ्गुल (finger-breadth).",
            "त् + vowel → द् + vowel."),
        mcq("apply", 4, "What does the card say of दल in अंगुलदल, unit 82?",
            ("Probably 'half'; also petal or part", "The data takes dala as half (probable); the word also means petal or part."),
            [("Probably 'double'; also pair or twin", "Nothing in the data reads dala as double."),
             ("Probably 'palm'; also hand or fist", "The palm measure is pāṇitala (unit 81), not dala."),
             ("Probably 'tip'; also point or end", "Nothing in the data reads dala as a tip.")],
            "aṅgula-dala: probably half a finger-breadth; dala also means petal or part.",
            "दल = probably half (also petal, part)."),
        mcq("transfer", 5, "By the join of पञ्चाशत् + अङ्गुल, how is चत्वारिंशत् + अङ्गुलानि (forty aṅgulas) joined in a new example?",
            ("चत्वारिंशदङ्गुलानि", "त् before a vowel becomes द्, as पञ्चाशत् + अङ्गुल → पञ्चाशदङ्गुल."),
            [("चत्वारिंशतङ्गुलानि", "त् does not stay unvoiced before a vowel; it becomes द्."),
             ("चत्वारिंशच्छङ्गुलानि", "च्छ arises only from त् + श; here a vowel follows."),
             ("चत्वारिंशन्नङ्गुलानि", "न् may replace त् only before a nasal; अ is a vowel.")],
            "चत्वारिंशत् + अङ्गुलानि = चत्वारिंशदङ्गुलानि.",
            "त् + vowel → द् + vowel.",
            teaches="A final त् before a vowel becomes द्: पञ्चाशत् + अङ्गुल → पञ्चाशदङ्गुल, चत्वारिंशत् + अङ्गुलानि → चत्वारिंशदङ्गुलानि."),
    ],
}

# ---------------------------------------------------------------- unit 83
AUTHORED["83"] = {
    "title": "अन्ये पुनराहुः",
    "question": "What does the short formula of unit 83 say?",
    "rule": ("अन्ये पुनराहुः: 'others (अन्ये) again (पुनः) say (आहुः)'. A formula that brings in the view of other, unnamed "
             "authorities."),
    "limits": ("Prose formula of three words. Who the others are is not stated. That it brings in other views on the "
               "measures (units 84 and 85) is the data's reading ('appears to'); no question rests on what follows. "
               "आहुः is a perfect form, used as 'they say'."),
    "explain_hi": ("यह तीन शब्दों का छोटा गद्य-सूत्र है: ‘दूसरे फिर कहते हैं’। "
                   "‘अन्ये’ यानी दूसरे लोग; वे कौन हैं, यह नहीं बताया। "
                   "‘आहुः’ √अह् का परोक्ष भूत (लिट्), प्रथम पुरुष बहुवचन है, जिसका अर्थ ‘वे कहते हैं’ लिया जाता है। "
                   "डेटा के अनुसार यह आगे (इकाई ८४ और ८५) माप के बारे में दूसरों के मत खोलता दिखता है। "
                   "‘पुनराहुः’ में पुनर् का र् स्वर आ से पहले बना रहता है।"),
    "hook": "अन्ये पुनराहुः: अब दूसरों की बात।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "In unit 83, who are said to speak?",
            ("Others, whose names are not given", "अन्ये = others; the unit names nobody."),
            [("The author, speaking for himself", "अन्ये means others, not the author."),
             ("Ātreya and his pupils, by name", "No one is named in unit 83."),
             ("The kinsmen of the wounded man", "अन्ये are authorities who 'say'; no kinsmen are named.")],
            "अन्ये पुनराहुः: others again say.",
            "अन्ये = others (unnamed)."),
        order(1, "Put the words of unit 83 in the printed order.",
              ["अन्ये", "पुनर्", "आहुः"],
              "Others; again; say.",
              "अन्ये → पुनर् → आहुः."),
        match(2, "Match each word of unit 83 to its meaning.",
              [["अन्ये", "others"], ["पुनर्", "again"], ["आहुः", "they say"]],
              "अन्ये = others, पुनः = again, आहुः = they say.",
              "अन्ये, पुनर्, आहुः.", role="extend",
              teaches="आहुः is a perfect of √अह्, third person plural, used in the sense 'they say'."),
        mcq("discriminate", 3, "Which split of पुनराहुः in unit 83 is right?",
            ("पुनर् + आहुः", "पुनर् keeps its र् before the vowel आ: पुनर् + आहुः → पुनराहुः."),
            [("पुनरा + हुः", "Neither पुनरा nor हुः is a word."),
             ("पुन + राहुः", "पुन is not a word; the word is पुनर् (पुनः)."),
             ("पुनर् + अहुः", "र् + अ would give पुनरहुः, with a short अ.")],
            "पुनर् (again) + आहुः (they say).",
            "पुनर् + vowel: the र् stays."),
        mcq("apply", 4, "Which tense label does the data give to आहुः in unit 83?",
            ("Perfect, used as 'they say'", "The data: 3 pl. pf. √अह्, 'they say'."),
            [("Future, used as 'they will say'", "आहुः is not a future; the data labels it perfect."),
             ("Optative, used as 'they should say'", "आहुः is not an optative; the data labels it perfect."),
             ("Imperative, used as 'let them say'", "आहुः is not an imperative; the data labels it perfect.")],
            "आहुः: perfect, third person plural, in the sense 'they say'.",
            "आहुः = perfect of √अह्: they say."),
        mcq("transfer", 5, "Built like पुनराहुः, how is पुनर् + आगच्छति (comes again) joined in a new example?",
            ("पुनरागच्छति", "र् stays before a vowel, as पुनर् + आहुः → पुनराहुः."),
            [("पुनागच्छति", "The र् of पुनर् is not dropped before a vowel."),
             ("पुनोऽगच्छति", "ओऽ comes from अः + अ; पुनर् has र्, and आ follows."),
             ("पुनारागच्छति", "The अ of पुनर् is not lengthened before a vowel.")],
            "पुनर् + आगच्छति = पुनरागच्छति.",
            "पुनर् + vowel: the र् stays and joins the vowel.",
            teaches="पुनर् keeps its र् before a vowel: पुनर् + आहुः → पुनराहुः, पुनर् + आगच्छति → पुनरागच्छति."),
    ],
}

# ---------------------------------------------------------------- unit 84
AUTHORED["84"] = {
    "title": "व्रीहिप्रमाणानि क्षिप्राणि",
    "question": "What measure does unit 84 give, and how is the line built?",
    "rule": ("Of the measure of a vrīhi (rice grain; Oryza sativa, standard): क्षिप्राणि, read by the data as the "
             "marma kṣipra. व्रीहिप्रमाण is a bahuvrīhi: 'having a rice grain's measure'."),
    "limits": ("Prose, no verb. क्षिप्राणि is read by the data as the marma name kṣipra (neuter plural); the plain adjective "
               "'quick' is the alternative, so no question asks which marma is meant. That this is one of the views of the "
               "'others' of unit 83 is the data's reading ('appears to')."),
    "explain_hi": ("‘व्रीहिप्रमाणानि’ यानी व्रीहि (धान का दाना; मानक पहचान) के माप वाले। "
                   "‘क्षिप्राणि’ को डेटा क्षिप्र नामक मर्म (नपुंसक बहुवचन) पढ़ता है; यह साधारण विशेषण ‘शीघ्र’ भी हो सकता है, इसलिए किस मर्म की बात है, इस पर प्रश्न नहीं। "
                   "पंक्ति में कोई क्रिया नहीं। "
                   "‘व्रीहिप्रमाण’ बहुव्रीहि समास है: जिसका माप व्रीहि जितना हो; यह मापे जाने वाले के साथ नपुंसक बहुवचन में है। "
                   "डेटा के अनुसार यह इकाई ८३ के ‘दूसरों के मत’ में आती दिखती है और इकाई ८५ में आगे चलती है।"),
    "hook": "व्रीहि भर का माप: धान के दाने जितना।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "In unit 84, what is a vrīhi?",
            ("A rice grain", "व्रीहि = rice grain (Oryza sativa, standard)."),
            [("A barley grain", "Barley is yava; व्रीहि is rice."),
             ("A mustard seed", "Mustard is sarṣapa; व्रीहि is rice."),
             ("A finger-breadth", "A finger-breadth is aṅgula; व्रीहि is rice.")],
            "व्रीहिप्रमाणानि: of the measure of a rice grain.",
            "व्रीहि = rice grain."),
        match(1, "Match each word of unit 84 to its meaning.",
              [["व्रीहि", "rice grain"], ["प्रमाण", "measure"], ["क्षिप्र", "literally 'quick'"]],
              "व्रीहि = rice grain, प्रमाण = measure, क्षिप्र = 'quick' (the data reads it as the marma's name).",
              "व्रीहि, प्रमाण, क्षिप्र."),
        mcq("extend", 2, "What kind of compound is व्रीहिप्रमाणानि, as the data reads it?",
            ("Bahuvrīhi: having a rice grain's measure", "The data: bahuvrīhi, nom. pl.: 'of the measure of a rice grain'."),
            [("Dvandva: rice grains and measures", "A dvandva would list two things; the data reads a bahuvrīhi."),
             ("Avyayībhāva: according to the grain", "An avyayībhāva is indeclinable; this word has a plural ending."),
             ("Tatpuruṣa: the grain's own measure", "The data reads a bahuvrīhi, describing what has that measure.")],
            "व्रीहि-प्रमाणानि: (things) having the measure of a rice grain.",
            "X-प्रमाण (bahuvrīhi) = having the measure of X.",
            teaches="X-प्रमाण read as a bahuvrīhi means 'having the measure of X' and agrees with what is measured (here neuter plural)."),
        multi("discriminate", 3, "Which statements fit unit 84 as printed?",
              [("The line names who the 'others' are", "No speaker is named in unit 84."),
               ("The line has no verb", "Right: a nominal statement with no verb."),
               ("The line gives a count of marmas", "No number is printed in unit 84."),
               ("A rice grain serves as the measure", "Right: व्रीहि-प्रमाणानि, of a rice grain's measure.")],
              [1, 3],
              "No verb, no number, no speaker; a rice grain is the measure.",
              "व्रीहिप्रमाणानि क्षिप्राणि: measure + what is measured."),
        mcq("apply", 4, "Why does the card ask nothing about which marma क्षिप्राणि names?",
            ("It may also be the adjective 'quick'", "The data reads a marma name but keeps the plain adjective as the alternative."),
            [("It is damaged and unreadable in print", "The word is printed clearly; its reading, not its print, is open."),
             ("It is printed twice in the same line", "It is printed once, at the end of the line."),
             ("It is a verb without any subject", "The data reads it as a neuter plural noun or adjective.")],
            "क्षिप्राणि: the name kṣipra (data's reading) or the adjective 'quick'.",
            "Two readings → no question on the referent."),
        mcq("transfer", 5, "Built like व्रीहिप्रमाणानि, what does अङ्गुष्ठप्रमाणः (said of a man) mean in a new example?",
            ("Of the measure of a thumb", "X-प्रमाण (bahuvrīhi) = having X's measure: having a thumb's measure."),
            [("Measuring with his thumb", "The compound describes size, not an action of measuring."),
             ("A thumb and a measure", "That would be a dvandva listing two things."),
             ("Larger than any thumb", "Nothing in the compound says larger.")],
            "अङ्गुष्ठप्रमाणः = of a thumb's measure, like व्रीहिप्रमाणानि = of a rice grain's measure.",
            "X-प्रमाण = having the measure of X.",
            teaches="X-प्रमाण (bahuvrīhi) = having the measure of X: व्रीहिप्रमाण = of a rice grain's measure, अङ्गुष्ठप्रमाण = of a thumb's measure."),
    ],
}

# ---------------------------------------------------------------- unit 85
AUTHORED["85"] = {
    "title": "कलायप्रमाणानि स्तनरोहितोत्क्षेपाः",
    "question": "By unit 85, which marmas have a kalāya's measure, and what do others accept?",
    "rule": ("Of a kalāya's measure (probably the pea): stanarohita and utkṣepa. Likewise (तथा) others (अन्ये) accept "
             "(इच्छन्ति) marmas even (अपि) of a tila's measure (sesame seed; Sesamum indicum, standard)."),
    "limits": ("Prose; line 1 has no verb. kalāya = pea is probable (the grass pea is a possible alternative). The tila-sized "
               "marmas are not named. इच्छन्ति is literally 'they wish for'; 'accept' is the natural sense. The view appears "
               "to continue units 83-84 (data's reading)."),
    "explain_hi": ("पहली पंक्ति: कलाय (सम्भवतः मटर; खेसारी जैसी दूसरी दाल भी सम्भव) के माप के हैं स्तनरोहित और उत्क्षेप, जिन्हें डेटा द्वन्द्व में दो मर्म-नाम पढ़ता है। "
                   "दूसरी पंक्ति: वैसे ही दूसरे लोग तिल (मानक पहचान) के माप के भी मर्म मानते हैं; वे कौन से मर्म हैं, यह नहीं बताया। "
                   "‘इच्छन्ति’ का शाब्दिक अर्थ ‘चाहते हैं’ है; यहाँ ‘मानते हैं’ स्वाभाविक अर्थ है। "
                   "सन्धियाँ: स्तनरोहित + उत्क्षेपाः (अ + उ → ओ), तिलप्रमाणानि + अपि (इ + अ → य), मर्माणि + इच्छन्ति (इ + इ → ई)। "
                   "डेटा के अनुसार यह इकाई ८३-८४ के मत को आगे बढ़ाती दिखती है।"),
    "hook": "कलाय भर के दो, और कुछ के मत में तिल भर के भी।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 85, which two marmas have the measure of a kalāya (probably the pea)?",
            ("Stanarohita and utkṣepa", "स्तनरोहितोत्क्षेपाः: the data reads two marma names, stanarohita and utkṣepa."),
            [("Kṣipra and the talahṛdaya", "Neither is named in unit 85."),
             ("Gulpha and the maṇibandha", "These are of two finger-breadths (unit 80)."),
             ("Jānu and also the kūrpara", "These are of three finger-breadths (unit 80).")],
            "कलायप्रमाणानि स्तनरोहितोत्क्षेपाः: stanarohita and utkṣepa.",
            "कलाय-measure → स्तनरोहित, उत्क्षेप."),
        order(1, "Put the printed parts of unit 85 in the line's order.",
              ["कलायप्रमाणानि", "स्तनरोहितोत्क्षेपाः", "तथाऽन्ये", "तिलप्रमाणान्यपि", "मर्माणीच्छंति"],
              "Of a kalāya's measure; stanarohita and utkṣepa; likewise others; even of a tila's measure; accept marmas.",
              "कलायप्रमाणानि → स्तनरोहितोत्क्षेपाः → तथाऽन्ये → तिलप्रमाणान्यपि → मर्माणीच्छंति."),
        match(2, "Match each word of unit 85 to its meaning.",
              [["कलाय", "probably the pea"], ["तिल", "sesame seed"], ["इच्छन्ति", "they accept (literally wish for)"],
               ["अन्ये", "others"], ["अपि", "even"]],
              "कलाय = probably the pea; तिल = sesame seed (standard); अन्ये इच्छन्ति = others accept; अपि = even.",
              "कलाय, तिल, इच्छन्ति, अन्ये, अपि.", role="extend",
              teaches="इच्छन्ति (√इष्) literally means 'they wish for'; with मर्माणि it is read 'they accept (marmas)'."),
        mcq("discriminate", 3, "Which split of मर्माणीच्छंति in unit 85 is right?",
            ("मर्माणि + इच्छन्ति", "इ + इ → ई: मर्माणि + इच्छन्ति → मर्माणीच्छन्ति."),
            [("मर्माणी + च्छन्ति", "च्छन्ति is not a word; the verb is इच्छन्ति."),
             ("मर्माण + ईच्छन्ति", "Neither मर्माण nor ईच्छन्ति is a word."),
             ("मर्माणः + इच्छन्ति", "मर्माणः is no form of मर्मन्; the neuter plural is मर्माणि.")],
            "मर्माणि (marmas) + इच्छन्ति (they accept): इ + इ → ई.",
            "इ + इ → ई."),
        mcq("apply", 4, "By line 2 of unit 85, what do others accept?",
            ("Marmas even of a sesame seed's size", "तिलप्रमाणान्यपि मर्माणि: marmas even of a tila's measure."),
            [("No marma smaller than a whole palm", "The line speaks of marmas as small as a sesame seed."),
             ("Marmas only of a finger's width each", "The line says even (अपि) of a sesame seed's measure."),
             ("Marmas of the size of a barley grain", "Barley (yava) is not named; the line names tila.")],
            "तथाऽन्ये तिलप्रमाणान्यपि मर्माणीच्छन्ति: others accept marmas even of a sesame seed's measure.",
            "अन्ये + तिलप्रमाण + अपि: others, even sesame-sized."),
        mcq("transfer", 5, "By the join of स्तनरोहित + उत्क्षेपाः, how is सूर्य + उदयः (sunrise) joined in a new example?",
            ("सूर्योदयः", "अ + उ → ओ, as स्तनरोहित + उत्क्षेपाः → स्तनरोहितोत्क्षेपाः."),
            [("सूर्यौदयः", "अ + उ gives ओ; औ comes from अ + ओ or अ + औ."),
             ("सूर्युदयः", "The अ does not vanish before उ; the two merge into ओ."),
             ("सूर्यवुदयः", "व् arises from उ before a vowel, not from अ + उ.")],
            "सूर्य + उदयः = सूर्योदयः.",
            "अ + उ → ओ.",
            teaches="अ + उ → ओ: स्तनरोहित + उत्क्षेपाः → स्तनरोहितोत्क्षेपाः, सूर्य + उदयः → सूर्योदयः."),
    ],
}

# ---------------------------------------------------------------- unit 86
AUTHORED["86"] = {
    "title": "भवंति चात्र",
    "question": "What does the formula of unit 86 say, and how is it joined?",
    "rule": ("भवन्ति चात्र: 'and here there are'. A formula introducing verses; the noun (verses) is not printed. "
             "च + अत्र → चात्र (अ + अ → आ)."),
    "limits": ("Prose formula of two words. The noun (verses) is not stated; the data names it as the sense of the formula. "
               "No question rests on what follows."),
    "explain_hi": ("यह दो शब्दों का गद्य-सूत्र है: ‘और यहाँ हैं’। "
                   "किस चीज़ के होने की बात है, वह संज्ञा (श्लोक) छपी नहीं; डेटा इसे आगे के श्लोकों को खोलने वाला सूत्र मानता है। "
                   "‘भवन्ति’ √भू का वर्तमान काल, प्रथम पुरुष बहुवचन है: वे हैं। "
                   "‘चात्र’ में च + अत्र की सन्धि है (अ + अ → आ)।"),
    "hook": "भवन्ति चात्र: अब यहाँ श्लोक आते हैं।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "What does भवंति चात्र in unit 86 mean?",
            ("And here there are", "भवन्ति = there are, च = and, अत्र = here."),
            [("And there they were", "भवन्ति is present, and अत्र is here, not there."),
             ("And now they all say", "No verb of saying is printed; भवन्ति = there are."),
             ("And here it is not", "No negation (न) is printed.")],
            "भवन्ति चात्र: and here there are.",
            "भवन्ति = there are; अत्र = here."),
        match(1, "Match each word of unit 86 to its meaning.",
              [["भवन्ति", "there are"], ["च", "and"], ["अत्र", "here"]],
              "भवन्ति = there are; च = and; अत्र = here.",
              "भवन्ति, च, अत्र."),
        mcq("extend", 2, "What is the verb form भवन्ति in unit 86?",
            ("Present, third person plural, √भू", "The data: 3 pl. pres. √भू: there are."),
            [("Future, third person plural, √भू", "The future would be भविष्यन्ति."),
             ("Present, first person plural, √भू", "The first person plural would be भवामः."),
             ("Optative, third person singular, √भू", "The optative singular would be भवेत्.")],
            "भवन्ति: present, third person plural of √भू.",
            "-अन्ति = present, 3rd plural.",
            teaches="भवन्ति is the present, third person plural, of √भू: there are, they are."),
        mcq("discriminate", 3, "Which split of चात्र in unit 86 is right?",
            ("च + अत्र", "अ + अ → आ: च + अत्र → चात्र."),
            [("चा + त्र", "Neither चा nor त्र is a word here."),
             ("चः + अत्र", "च has no visarga; and अः + अ would give चोऽत्र."),
             ("च + तत्र", "तत्र would stay तत्र: च तत्र.")],
            "च (and) + अत्र (here): अ + अ → आ.",
            "अ + अ → आ."),
        multi("apply", 4, "Which statements fit unit 86?",
              [("The noun 'verses' is printed in it", "The noun is not printed; it is understood."),
               ("Its verb is a present form", "Right: भवन्ति, present, third person plural."),
               ("It joins च with अत्र", "Right: च + अत्र → चात्र."),
               ("It names the author of the verses", "No author is named.")],
              [1, 2],
              "Present verb भवन्ति; च + अत्र joined; the noun and any author are not printed.",
              "भवन्ति चात्र: verb + and + here."),
        mcq("transfer", 5, "Built like भवन्ति (there are, √भू), which form of √पठ् means they read, in a new example?",
            ("पठन्ति", "-अन्ति is the present, third person plural, as भवन्ति."),
            [("पठति", "पठति is singular: he reads."),
             ("पठामः", "पठामः is first person: we read."),
             ("पठिष्यन्ति", "पठिष्यन्ति is future: they will read.")],
            "पठन्ति = they read, like भवन्ति = they are.",
            "Present, 3rd plural: -अन्ति.",
            teaches="The present third person plural ends in -अन्ति: भवन्ति (they are), पठन्ति (they read)."),
    ],
}

# ---------------------------------------------------------------- unit 87
AUTHORED["87"] = {
    "title": "देहेऽस्मिन्नायुर्मर्माणि रक्षति",
    "question": "What can be said surely of unit 87, whose two lines are obscure?",
    "rule": ("As read by the data: in this body (देहे अस्मिन्) life (आयुः) guards (रक्षति) the marmas; therefore (तस्मात्) "
             "the discerning man (विचक्षणः) should always (सदा) attend to (सेवेत) what pervades life (आयुर्व्यापि)."),
    "limits": ("Verse, low confidence. मर्मव्यामे is unclear (a conjecture is not used). Who guards whom can be read two "
               "ways (or as a compound): no question asks it. The object of सेवेत and the case of आयुर्व्यापि are "
               "uncertain: no question on them."),
    "explain_hi": ("ये दो पंक्तियाँ अस्पष्ट हैं, विश्वास कम है; इकाई ८६ के सूत्र के बाद पहला श्लोक दिखती हैं। "
                   "पहला शब्द ‘मर्मव्यामे’ स्पष्ट नहीं; एक अनुमान (मर्मव्याप्ते) है, पर अपनाया नहीं गया। "
                   "डेटा का पाठ: इस शरीर में आयु मर्मों की रक्षा करती है; पर उलटा अर्थ (मर्म आयु की रक्षा करते हैं) या ‘आयुर्मर्माणि’ समास भी सम्भव है। "
                   "दूसरी पंक्ति: इसलिए (तस्मात्) विचक्षण यानी समझदार व्यक्ति को सदा ‘आयु में व्याप्त’ का ही सेवन करना चाहिए; किसका, यह नहीं बताया। "
                   "पक्के भाग केवल शब्दों के अर्थ और सन्धियाँ हैं: देहे + अस्मिन् → देहेऽस्मिन्, तस्मात् + विचक्षणः → तस्माद्विचक्षणः।"),
    "hook": "तस्मात्... सदा सेवेत: समझदार सदा ध्यान रखे; बाकी पाठ धुँधला।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "In line 2 of unit 87, who should attend (सेवेत)?",
            ("The discerning man", "विचक्षणः: the discerning (man), m. nom. sg., the subject of सेवेत."),
            [("The physician's pupil", "No pupil is named; the subject is विचक्षणः."),
             ("The patient's kinsmen", "No kinsmen are named in unit 87."),
             ("The king's own servant", "No king or servant is named in unit 87.")],
            "सेवेत सदा तस्माद्विचक्षणः: therefore the discerning man should always attend.",
            "विचक्षणः = the discerning man."),
        order(1, "Put the printed words of line 2 of unit 87 in order.",
              ["आयुर्व्याप्येव", "सेवेत", "सदा", "तस्माद्विचक्षणः"],
              "Only the life-pervading; should attend; always; therefore the discerning man.",
              "आयुर्व्याप्येव → सेवेत → सदा → तस्माद्विचक्षणः."),
        match(2, "Match each sure word of unit 87 to its meaning.",
              [["देहे", "in the body"], ["रक्षति", "guards"], ["सदा", "always"], ["तस्मात्", "therefore"],
               ["विचक्षणः", "the discerning man"]],
              "देहे = in the body; रक्षति = guards; सदा = always; तस्मात् = therefore; विचक्षणः = the discerning man.",
              "देहे, रक्षति, सदा, तस्मात्, विचक्षणः.", role="extend",
              teaches="तस्मात् (therefore) draws a 'should' from what came before: here line 2 follows from line 1."),
        mcq("discriminate", 3, "Which split of देहेऽस्मिन् in unit 87 is right?",
            ("देहे + अस्मिन्", "ए + अ → ए, the अ dropped and shown by ऽ: देहेऽस्मिन्."),
            [("देहः + अस्मिन्", "अः + अ would give देहोऽस्मिन्."),
             ("देहे + स्मिन्", "स्मिन् is not a word; the pronoun is अस्मिन्."),
             ("देहा + अस्मिन्", "आ + अ would give देहास्मिन्.")],
            "देहे (in the body) + अस्मिन् (this): ए + अ → एऽ.",
            "ए + अ → एऽ."),
        mcq("apply", 4, "Why is तस्मात् printed तस्माद् before विचक्षणः in unit 87?",
            ("त् before a voiced sound becomes द्", "व is voiced: तस्मात् + विचक्षणः → तस्माद्विचक्षणः."),
            [("त् before any consonant becomes द्", "Not before a voiceless one: तस्मात् + कृते stays तस्मात्कृते."),
             ("त् at a word's end always becomes द्", "At a pause त् stays: तस्मात्."),
             ("The द् belongs to the word विचक्षणः", "The word begins with वि; the द् comes from तस्मात्.")],
            "तस्मात् + विचक्षणः: त् before the voiced व → द्.",
            "त् + voiced sound → द्."),
        mcq("transfer", 5, "By the rule of तस्माद्विचक्षणः, how is तस्मात् + गच्छति (therefore he goes) joined in a new example?",
            ("तस्माद्गच्छति", "त् before the voiced ग becomes द्, as before व."),
            [("तस्मात्गच्छति", "त् cannot stay unvoiced before the voiced ग."),
             ("तस्माग्गच्छति", "त् does not turn into ग् before ग."),
             ("तस्मान्गच्छति", "न् may replace त् only before a nasal; ग is not one.")],
            "तस्मात् + गच्छति = तस्माद्गच्छति.",
            "त् + voiced sound → द्.",
            teaches="A final त् before a voiced sound becomes द्: तस्मात् + विचक्षणः → तस्माद्विचक्षणः, तस्मात् + गच्छति → तस्माद्गच्छति."),
    ],
}

# ---------------------------------------------------------------- unit 88
AUTHORED["88"] = {
    "title": "मर्माभिघातः स्वल्पोऽपि",
    "question": "What does line 1 of unit 88 say of even a slight blow on a marma?",
    "rule": ("A blow on a marma (मर्माभिघातः), even a slight one (स्वल्पः अपि), generally (प्रायशः) afflicts exceedingly "
             "(बाधते तराम्). Line 2: diseases seated in a marma (रोगा मर्माश्रयाः) are likewise (तद्वत्); its sense is obscure."),
    "limits": ("Verse, low confidence. Whom the blow afflicts is not stated. Line 2 has no predicate, and प्रक्रान्ताः (begun, "
               "set about) may mean 'treatment undertaken' or 'set in': not clear. No question rests on the sense of line 2 "
               "beyond the plain words मर्माश्रय and रोगाः."),
    "explain_hi": ("पहली पंक्ति: मर्म पर थोड़ी भी चोट प्रायः बहुत अधिक पीड़ा देती है; किसे, यह नहीं कहा। "
                   "‘स्वल्पोऽपिप्रायशो’ छपाई में सटा है; यह स्वल्पः अपि प्रायशः है (रिक्त स्थान की भूल)। "
                   "दूसरी पंक्ति अस्पष्ट है: मर्म में आश्रय वाले रोग ‘वैसे ही’, ‘प्रयत्न से भी आरम्भ किए हुए’; इसका कोई विधेय नहीं, और ‘प्रक्रान्त’ का अर्थ (चिकित्सा आरम्भ हुई, या रोग जम गया) स्पष्ट नहीं। "
                   "सन्धियाँ: सु + अल्प → स्वल्प (उ + अ → व); रोगाः + मर्म → रोगा मर्म (आः का विसर्ग घोष से पहले लुप्त)।"),
    "hook": "छोटी-सी चोट भी, मर्म पर हो तो बहुत भारी।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 88, how does even a slight blow on a marma generally afflict?",
            ("Exceedingly", "बाधते तराम्: it afflicts exceedingly."),
            [("Not at all", "The line says it afflicts (बाधते), and exceedingly."),
             ("Only slightly", "स्वल्प describes the blow; the affliction is तराम्, exceedingly."),
             ("Only after a day", "No time is stated in unit 88.")],
            "मर्माभिघातः स्वल्पोऽपि प्रायशो बाधते तराम्.",
            "स्वल्प blow → तराम् affliction."),
        order(1, "Put these words of line 1 of unit 88 in the verse's order.",
              ["मर्माभिघातः", "स्वल्पोऽपि", "प्रायशो", "बाधते", "तरां"],
              "A blow on a marma; even slight; generally; afflicts; exceedingly.",
              "मर्माभिघातः → स्वल्पोऽपि → प्रायशो → बाधते → तरां."),
        match(2, "Match each word of unit 88 to its meaning.",
              [["अभिघात", "blow, injury"], ["स्वल्प", "very little, slight"], ["प्रायशः", "generally"],
               ["तराम्", "exceedingly"], ["आश्रय", "seat"]],
              "मर्म-अभिघातः = a blow on a marma; स्वल्पः = slight; प्रायशः = generally; तराम् = exceedingly; मर्म-आश्रयाः = seated in a marma.",
              "अभिघात, स्वल्प, प्रायशः, तराम्, आश्रय.", role="extend",
              teaches="मर्म-आश्रय (bahuvrīhi) = having a marma as its seat: रोगा मर्माश्रयाः, diseases seated in a marma."),
        mcq("discriminate", 3, "Which split of स्वल्प in unit 88 is right?",
            ("सु + अल्प", "उ + अ → व: सु + अल्प → स्वल्प."),
            [("स्व + अल्प", "अ + अ would give स्वाल्प, with a long आ."),
             ("स्वा + अल्प", "आ + अ would give स्वाल्प as well."),
             ("सो + अल्प", "ओ + अ would give सोऽल्प.")],
            "सु (very) + अल्प (little): उ + अ → व.",
            "उ + vowel (not उ) → व + vowel."),
        mcq("apply", 4, "Why is रोगाः printed रोगा before मर्माश्रया in unit 88?",
            ("आः drops its visarga before a voiced sound", "म is voiced, and the vowel before the visarga is आ."),
            [("Every visarga, after any vowel, drops before a voiced sound", "Not every one: अः → ओ, इः → इर् before a voiced consonant."),
             ("A visarga always drops at a line's middle", "Visarga changes depend on the sounds, not the place in the line."),
             ("रोगा is a feminine form without visarga", "The data: रोगाः, m. nom. pl.; only the visarga dropped.")],
            "रोगाः + मर्म-: आः before the voiced म → आ.",
            "आः + voiced sound → आ."),
        mcq("transfer", 5, "By the rule of रोगा मर्माश्रयाः, how is वृक्षाः + वर्धन्ते (trees grow) written in a new example?",
            ("वृक्षा वर्धन्ते", "आः drops its visarga before the voiced व, as रोगाः + मर्म- → रोगा मर्म-."),
            [("वृक्षो वर्धन्ते", "ओ comes only from short अः; here the vowel is आ."),
             ("वृक्षार्वर्धन्ते", "र् comes from a visarga after vowels other than अ/आ."),
             ("वृक्षास्वर्धन्ते", "स् stands before त or थ, not before व.")],
            "वृक्षाः + वर्धन्ते = वृक्षा वर्धन्ते.",
            "आः + voiced sound → आ.",
            teaches="After आ the visarga drops before a voiced sound: रोगाः + मर्माश्रयाः → रोगा मर्माश्रयाः, वृक्षाः + वर्धन्ते → वृक्षा वर्धन्ते."),
    ],
}

# ---------------------------------------------------------------- unit 89
AUTHORED["89"] = {
    "title": "विक्षिप्यते भृशं सीदन्",
    "question": "What signs does unit 89 list for the (unnamed) sufferer?",
    "rule": ("He is greatly tossed about (विक्षिप्यते भृशम्), sinking (सीदन्), empty (शून्यः); he reels (भ्रमति), trembles "
             "(वेपते), breathes upward with difficulty (ऊर्ध्वं श्वसिति कृच्छ्रेण), with slack limbs (स्रस्तगात्रः), again and "
             "again (मुहुर्मुहुः)."),
    "limits": ("Verse. The sufferer is not named; 'he' comes from the verbs. Unit 90 sums these up as the signs of marma "
               "injury. Printed श्वािसति is read as श्वसिति (near certain): no question rests on it. शून्य is kept literal "
               "(empty), perhaps a dazed state."),
    "explain_hi": ("यह श्लोक मर्माघात के लक्षणों की सूची है; पीड़ित का नाम नहीं, ‘वह’ क्रियाओं से समझा जाता है। "
                   "वह बहुत इधर-उधर फेंका जाता है (विक्षिप्यते), डूबता-सा (सीदन्), शून्य (सम्भवतः सुध-बुध खोया), घूमता है, काँपता है। "
                   "वह कठिनाई से ऊपर की ओर साँस लेता है, उसके अंग ढीले पड़ते हैं, बार-बार। "
                   "छपा ‘श्वािसति’ भटकी मात्राओं वाली छपाई है; ‘श्वसिति’ लगभग निश्चित पाठ है, फिर भी उस पर प्रश्न नहीं। "
                   "ये लक्षण इकाई ९० में ‘इन लक्षणों से’ कहकर समेटे जाते हैं; ‘मुहुर्मुहुः’ में उ के बाद विसर्ग घोष म से पहले र् बना है।"),
    "hook": "फेंका जाए, डूबे, घूमे, काँपे, ढीले अंग: बार-बार।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "In unit 89, what is said of the sufferer's limbs?",
            ("They are slack", "स्रस्तगात्रः: with slack, drooping limbs."),
            [("They are stiff", "Stiff would be स्तब्ध; the word is स्रस्त, slack."),
             ("They are swollen", "No swelling is named in unit 89."),
             ("They are burnt", "Burning is said of the heart in unit 90, not the limbs here.")],
            "स्रस्तगात्रो मुहुर्मुहुः: with slack limbs, again and again.",
            "स्रस्त-गात्र = slack-limbed."),
        order(1, "Put these signs of unit 89 in the verse's order.",
              ["विक्षिप्यते", "सीदन्", "भ्रमति", "वेपते", "स्रस्तगात्रो"],
              "Tossed about; sinking; reels; trembles; slack-limbed.",
              "विक्षिप्यते → सीदन् → भ्रमति → वेपते → स्रस्तगात्रो."),
        match(2, "Match each word of unit 89 to its meaning.",
              [["विक्षिप्यते", "is tossed about"], ["सीदन्", "sinking"], ["भ्रमति", "reels"], ["वेपते", "trembles"],
               ["स्रस्तगात्रः", "with slack limbs"]],
              "विक्षिप्यते = is tossed about; सीदन् = sinking; भ्रमति = reels; वेपते = trembles; स्रस्तगात्रः = with slack limbs.",
              "विक्षिप्यते, सीदन्, भ्रमति, वेपते, स्रस्तगात्रः.", role="extend",
              teaches="The data labels विक्षिप्यते a passive of vi-√क्षिप् ('is tossed about') and सीदन् a present participle of √सद् ('sinking')."),
        mcq("discriminate", 3, "Which English line has one wrong word for शून्यो भ्रमति वेपते in unit 89?",
            ("empty, he reels, he sleeps", "Wrong word: वेपते = he trembles, not he sleeps."),
            [("empty, he reels, he trembles", "No error: शून्यः = empty, भ्रमति = reels, वेपते = trembles."),
             ("empty, he wanders, he trembles", "No error: भ्रमति may be rendered reels or wanders."),
             ("empty, he reels, and trembles", "No error: the same three words, joined by 'and'.")],
            "शून्यो भ्रमति वेपते = empty, he reels, he trembles.",
            "वेपते = trembles."),
        mcq("apply", 4, "What does मुहुर्मुहुः add at the end of unit 89?",
            ("Again and again", "मुहुः मुहुः = again and again (a repeated indeclinable)."),
            [("Slowly and gently", "मुहुः means again, not slowly."),
             ("Only once, at last", "मुहुर्मुहुः means repeatedly, not once."),
             ("Upward, to the head", "Upward is ऊर्ध्वम्, a different word of the verse.")],
            "स्रस्तगात्रो मुहुर्मुहुः: with slack limbs, again and again.",
            "मुहुर्मुहुः = again and again."),
        mcq("transfer", 5, "By the pattern of सीदन् (sinking, √सद्), which form of √गम् means going (said of the subject), in a new example?",
            ("गच्छन्", "-अन् is the present participle, masc. nom. sg., as सीदन्."),
            [("गच्छति", "गच्छति is a finite verb: he goes."),
             ("गत्वा", "गत्वा is the absolutive: having gone."),
             ("गन्तुम्", "गन्तुम् is the infinitive: to go.")],
            "गच्छन् = going, like सीदन् = sinking.",
            "Present participle, masc. nom. sg.: -अन्.",
            teaches="A present participle in -अन् (masc. nom. sg.) describes the subject while acting: सीदन् = sinking, गच्छन् = going."),
    ],
}

# ---------------------------------------------------------------- unit 90
AUTHORED["90"] = {
    "title": "हृदयं दह्यते चास्य",
    "question": "By unit 90, what happens to his heart, and how does he reach death?",
    "rule": ("His heart (hṛdaya) burns (दह्यते) and does not stay in one place (नैकस्थानेऽवतिष्ठते). From injury to a marma "
             "(मर्मोपघातात्) he reaches death (मरणं समश्नुते) with these signs (एतैर्लिङ्गैः)."),
    "limits": ("Verse. The subject of 'does not stay' is taken as the heart; it could also be the man, so no question asks "
               "which. 'He' is not printed. 'These signs' refers back to the signs of unit 89 and of line 1 here (data's "
               "reading)."),
    "explain_hi": ("पहली पंक्ति: उसका हृदय जलता है और एक स्थान पर नहीं टिकता; ‘नहीं टिकता’ का कर्ता हृदय माना गया है, पर वह व्यक्ति भी हो सकता है। "
                   "दूसरी पंक्ति: मर्म पर आघात से वह इन लक्षणों के साथ मृत्यु को प्राप्त होता है। "
                   "‘इन लक्षणों’ से इकाई ८९ और इस पंक्ति १ के लक्षण अभिप्रेत हैं (डेटा का पाठ)। "
                   "सन्धियाँ: च + अस्य → चास्य, न + एक → नैक (अ + ए → ऐ), स्थाने + अवतिष्ठते → स्थानेऽवतिष्ठते, और "
                   "उपघातात् + मरणम् → उपघातान्मरणम् (अनुनासिक से पहले त् → न्, वैकल्पिक; द् भी सही)।"),
    "hook": "हृदय जले, ठिकाना न रहे: मर्माघात का अन्त।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 90, what happens to his heart (hṛdaya)?",
            ("It burns", "हृदयं दह्यते: his heart burns."),
            [("It stops", "The verse says the heart burns, not that it stops."),
             ("It swells", "No swelling is named in unit 90."),
             ("It grows cold", "The verse says it burns, the opposite of cold.")],
            "हृदयं दह्यते चास्य: and his heart burns.",
            "दह्यते = burns."),
        order(1, "Put the printed parts of unit 90 in the verse's order.",
              ["हृदयं दह्यते चास्य", "नैकस्थानेऽवतिष्ठते", "मर्मोपघातान्मरणम्", "एतैर्लिंगैः", "समश्नुते"],
              "His heart burns; does not stay in one place; from marma injury, death; with these signs; he reaches.",
              "Heart → not in one place → from marma injury death → with these signs → reaches."),
        match(2, "Match each word of unit 90 to its meaning.",
              [["दह्यते", "burns"], ["अवतिष्ठते", "stays"], ["उपघात", "injury"], ["लिङ्ग", "sign"],
               ["समश्नुते", "reaches"]],
              "दह्यते = burns; अवतिष्ठते = stays; मर्म-उपघात = injury to a marma; लिङ्ग = sign; समश्नुते = reaches.",
              "दह्यते, अवतिष्ठते, उपघात, लिङ्ग, समश्नुते.", role="extend",
              teaches="समश्नुते (sam-√अश्) = reaches, attains: मरणं समश्नुते, he reaches death."),
        mcq("discriminate", 3, "Which split of नैकस्थाने in unit 90 is right?",
            ("न + एकस्थाने", "अ + ए → ऐ: न + एक → नैक."),
            [("ना + इकस्थाने", "Neither ना nor इकस्थाने is a word here."),
             ("नै + कस्थाने", "Neither नै nor कस्थाने is a word."),
             ("न + इकस्थाने", "अ + इ would give ए: नेक-.")],
            "न (not) + एकस्थाने (in one place): अ + ए → ऐ.",
            "अ + ए → ऐ."),
        mcq("apply", 4, "Why is मर्मोपघातात् printed मर्मोपघातान् before मरणम् in unit 90?",
            ("Before a nasal, त् may become न्; द् is also valid", "म is a nasal: -घातात् + मरणम् → -घातान्मरणम्; the द् form is also correct."),
            [("Before any consonant whatever, त् turns into न् too", "Not before every consonant: before व it becomes द्, as in तस्माद्विचक्षणः."),
             ("न् is the ablative ending of the word here", "The ablative ending is -आत्; only its त् changed."),
             ("The न् belongs to the next word, मरणम्", "मरणम् begins with म; the न् comes from the त्.")],
            "मर्मोपघातात् + मरणम्: त् before the nasal म may become न्.",
            "त् + nasal → न् (optional; द् also correct)."),
        mcq("transfer", 5, "By the join of मर्मोपघातान्मरणम्, which is a correct join of तत् + मात्रम् (only that) in a new example?",
            ("तन्मात्रम्", "त् before a nasal may become न् (optional; तद्मात्रम् is also correct)."),
            [("तच्मात्रम्", "च् arises from त् before च or श, not before म."),
             ("तत्मात्रम्", "त् cannot stay unvoiced before the voiced nasal म."),
             ("तल्मात्रम्", "ल् arises from त् only before ल.")],
            "तत् + मात्रम् = तन्मात्रम् (or तद्मात्रम्).",
            "त् + nasal → न् (optional; द् also correct).",
            teaches="Before a nasal, त् may become न् (optional; द् is also correct): मर्मोपघातात् + मरणम् → मर्मोपघातान्मरणम्, तत् + मात्रम् → तन्मात्रम्."),
    ],
}

# ---------------------------------------------------------------- unit 91
AUTHORED["91"] = {
    "title": "अमर्मविद्धोऽपि नरः",
    "question": "By unit 91, when does even a man pierced at a non-marma give up life at once?",
    "rule": ("Even a man pierced at a non-marma (अमर्मविद्धः), afflicted by cutting, splitting and the rest "
             "(छेदभेदादिपीडितः), and with much blood flowed out (अतिनिस्रुतरक्तः), gives up life (जीवितम्) at once (सद्यः)."),
    "limits": ("Verse. अमर्मविद्ध may also be read 'not pierced at a marma'; the sense is the same. The printed सद्यस्यजति is "
               "read as सद्यस्त्यजति (near certain: a lost त); no question rests on that join. The unit does not say how "
               "much blood loss is too much."),
    "explain_hi": ("यह श्लोक बताता है कि मर्म के बाहर का घाव भी घातक हो सकता है। "
                   "अमर्म में बिंधा हुआ भी मनुष्य, यदि छेदन, भेदन आदि से पीड़ित हो और उसका रक्त बहुत बह गया हो, तो तुरन्त जीवन छोड़ देता है। "
                   "‘अमर्मविद्ध’ को ‘मर्म में न बिंधा हुआ’ भी पढ़ा जा सकता है; अर्थ वही रहता है। "
                   "छपा ‘सद्यस्यजति’ में त छूट गया लगता है: सद्यः + त्यजति → सद्यस्त्यजति (लगभग निश्चित पाठ); इस पर प्रश्न नहीं। "
                   "‘रक्तश्च’ में विसर्ग च से पहले श् बना है।"),
    "hook": "मर्म बचा, पर रक्त बहा: तब भी तुरन्त मृत्यु।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 91, what happens to a man pierced at a non-marma who has lost much blood?",
            ("He gives up life at once", "सद्यः ... जीवितम्: he gives up life at once."),
            [("He lives, but loses that limb", "Unit 91 speaks of death at once, not of a lost limb."),
             ("He lives on for many years", "Unit 91 says he dies at once."),
             ("He recovers after a long fast", "No fast or recovery is named in unit 91.")],
            "अमर्मविद्धोऽपि नरः ... अतिनिस्रुतरक्तश्च सद्यस्त्यजति जीवितम्.",
            "Non-marma wound + much blood lost → death at once."),
        order(1, "Put these words of unit 91 in the verse's order.",
              ["अमर्मविद्धोऽपि", "नरः", "छेदभेदादिपीडितः", "अतिनिस्रुतरक्तश्च", "जीवितं"],
              "Even pierced at a non-marma; a man; afflicted by cutting, splitting and the rest; with much blood flowed out; life.",
              "अमर्मविद्धोऽपि → नरः → छेदभेदादिपीडितः → अतिनिस्रुतरक्तश्च → जीवितं."),
        match(2, "Match each word of unit 91 to its meaning.",
              [["छेद", "cutting"], ["भेद", "splitting"], ["अतिनिस्रुत", "flowed out excessively"], ["रक्त", "blood"],
               ["जीवित", "life"]],
              "छेद-भेद-आदि = cutting, splitting and the rest; अति-निस्रुत-रक्तः = with blood flowed out excessively; जीवितम् = life.",
              "छेद, भेद, अतिनिस्रुत, रक्त, जीवित.", role="extend",
              teaches="आदि at a compound's end means 'and the rest': छेदभेदादि = cutting, splitting and the like."),
        mcq("discriminate", 3, "What does the अ- of अमर्मविद्धः do in unit 91?",
            ("It negates: not a marma", "अ-मर्म = a non-marma: pierced at a place that is not a marma."),
            [("It means 'up to', like आ-", "'Up to' is आ (long), as in आचरम; this is short अ-."),
             ("It marks a past verb (augment)", "विद्ध is a participle; the augment belongs to past finite verbs."),
             ("It means 'very', like अति-", "'Very' is अति-, as in अतिनिस्रुत; अ- negates.")],
            "अ-मर्म-विद्धः = pierced at a non-marma.",
            "अ- before a consonant = not."),
        mcq("apply", 4, "By unit 91, what besides cutting and splitting brings death at once?",
            ("Much blood having flowed out", "अतिनिस्रुतरक्तश्च: and with blood flowed out excessively."),
            [("A blow landing on the marma itself", "The man is pierced at a non-marma (अमर्मविद्धः)."),
             ("A fever after the wounding", "No fever is named in unit 91."),
             ("Wind entering the wound", "No wind is named in unit 91.")],
            "Non-marma wound + cutting, splitting + much blood lost → death at once.",
            "अतिनिस्रुतरक्त = much blood flowed out."),
        mcq("transfer", 5, "By the rule of अतिनिस्रुतरक्तश्च, how is रामः + च (and Rāma) joined in a new example?",
            ("रामश्च", "A visarga before च becomes श्, as -रक्तः + च → -रक्तश्च."),
            [("रामो च", "ओ comes from अः before a voiced consonant; च is voiceless."),
             ("रामच्च", "The visarga does not become च्."),
             ("रामा च", "Only after आ does the visarga drop; here it is अः before च.")],
            "रामः + च = रामश्च.",
            "Visarga + च → श्च.",
            teaches="A visarga before च becomes श्: अतिनिस्रुतरक्तः + च → अतिनिस्रुतरक्तश्च, रामः + च → रामश्च."),
    ],
}

# ---------------------------------------------------------------- unit 92
AUTHORED["92"] = {
    "title": "अतोऽन्यथा जीवति तु",
    "question": "What does line 1 of unit 92 say of one pierced otherwise?",
    "rule": ("Otherwise than this (अतः अन्यथा), however (तु), one pierced (विद्धः) even by hundreds of arrows (शरशतैरपि) "
             "lives (जीवति). Line 2 is damaged."),
    "limits": ("Verse, low confidence. 'Otherwise than this' refers back to the marma injury and blood loss of units 90-91 "
               "(data's reading). Line 2's first word is damaged; whether it says he lives or does not live is not certain. "
               "No question rests on line 2."),
    "explain_hi": ("पहली पंक्ति पक्की है: इससे अन्यथा, यानी मर्माघात और अधिक रक्त-स्राव (इकाई ९०-९१) के बिना, सैकड़ों बाणों से बिंधा हुआ भी जीता है। "
                   "दूसरी पंक्ति का पहला शब्द ‘पुण्यवाच्छ्वियतायुश्चन’ टूटा हुआ और अस्पष्ट है; शायद ‘पुण्यवान्’ (पुण्यात्मा) और आयु का कोई शब्द है, पर कोई पक्का पाठ नहीं बना। "
                   "पक्के शब्द ‘कथंचिन्न जीवति’ हैं, यानी ‘किसी प्रकार नहीं जीता’; अनुवाद का दोहरा निषेध (‘ऐसा नहीं कि न जिए’) अनुमान है, उलटा अर्थ भी सम्भव। "
                   "इसलिए प्रश्न केवल पहली पंक्ति पर हैं। "
                   "‘अतोऽन्यथा’ में अतः + अन्यथा है: अः + अ → ओ, और अ का लोप ऽ से दिखता है।"),
    "hook": "मर्म बचा तो सौ बाण भी झेल ले।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "In line 1 of unit 92, what does one pierced even by hundreds of arrows do?",
            ("He lives", "जीवति तु विद्धः शरशतैरपि: one pierced even by hundreds of arrows lives."),
            [("He dies", "Line 1 says जीवति, he lives."),
             ("He flees", "No flight is named in unit 92."),
             ("He falls", "Line 1 says he lives; no fall is named.")],
            "अतोऽन्यथा जीवति तु विद्धः शरशतैरपि.",
            "जीवति = lives."),
        order(1, "Put the words of line 1 of unit 92 in the verse's order.",
              ["अतोऽन्यथा", "जीवति", "तु", "विद्धः", "शरशतैरपि"],
              "Otherwise than this; lives; however; pierced; even by hundreds of arrows.",
              "अतोऽन्यथा → जीवति → तु → विद्धः → शरशतैरपि."),
        match(2, "Match each word of line 1 of unit 92 to its meaning.",
              [["अतः", "than this"], ["अन्यथा", "otherwise"], ["विद्ध", "pierced"], ["शर", "arrow"], ["शत", "hundred"]],
              "अतः अन्यथा = otherwise than this; विद्धः = pierced; शर-शतैः = by hundreds of arrows.",
              "अतः, अन्यथा, विद्ध, शर, शत.", role="extend",
              teaches="शरशतैः = by hundreds of arrows: -ऐः is the instrumental plural of a-stems."),
        mcq("discriminate", 3, "Which split of अतोऽन्यथा in unit 92 is right?",
            ("अतः + अन्यथा", "अः + अ → ओ, and the अ is dropped (shown by ऽ): अतोऽन्यथा."),
            [("अतो + न्यथा", "न्यथा is not a word; the word is अन्यथा."),
             ("अत + अन्यथा", "अ + अ would give अतान्यथा."),
             ("अति + अन्यथा", "इ + अ would give अत्यन्यथा.")],
            "अतः (than this) + अन्यथा (otherwise).",
            "अः + अ → ओऽ."),
        mcq("apply", 4, "Why does the card build no question on line 2 of unit 92?",
            ("Its first word is damaged and unclear", "पुण्यवाच्छ्वियतायुश्चन is damaged; even the polarity of the line is not sure."),
            [("It repeats line 1 word for word", "Line 2 has other words (कथंचिन्न जीवति)."),
             ("The data calls it a later addition to the text", "The data calls it damaged, not a later addition."),
             ("It has no Sanskrit words at all", "It has words; its first one is damaged.")],
            "Line 2's first word is damaged, so its sense is not certain.",
            "Damaged line → no question."),
        mcq("transfer", 5, "By the pattern of शरशतैः (by hundreds of arrows), which form of वृक्ष means by trees, in a new example?",
            ("वृक्षैः", "-ऐः is the instrumental plural of a-stems, as शरशतैः."),
            [("वृक्षेषु", "वृक्षेषु is locative plural: among trees."),
             ("वृक्षाणाम्", "वृक्षाणाम् is genitive plural: of trees."),
             ("वृक्षम्", "वृक्षम् is accusative singular: a tree (as object).")],
            "वृक्षैः = by trees, like शरशतैः = by hundreds of arrows.",
            "a-stem, instrumental plural: -ऐः.",
            teaches="a-stems form the instrumental plural in -ऐः: शरशत → शरशतैः (by hundreds of arrows), वृक्ष → वृक्षैः (by trees)."),
    ],
}

# ---------------------------------------------------------------- unit 93
AUTHORED["93"] = {
    "title": "चिकित्सेदेव यत्नतः",
    "question": "By unit 93, how should one treat, and what is said of the physician in line 2?",
    "rule": ("Therefore (तस्मात्) one should indeed treat (चिकित्सेत् एव) with effort (यत्नतः), up to (आ) the last (चरम) "
             "breath. Line 2: the physician (भिषक्), approved by good kinsmen and friends, having refused (प्रत्याख्याय) "
             "the patient (आतुरम्)."),
    "limits": ("Verse. Printed उच्छासात् is read as उच्छ्वासात् (breath; near certain): no question rests on it. Line 2 "
               "has no main verb; what the physician does after refusing is not stated (no 'to treat' in the Sanskrit). "
               "सत् may qualify only बन्धु."),
    "explain_hi": ("पहली पंक्ति: इसलिए अन्तिम श्वास तक प्रयत्नपूर्वक चिकित्सा करनी ही चाहिए; कर्ता (वैद्य) छपा नहीं। "
                   "छपा ‘उच्छासात्’ कोई ज्ञात शब्द नहीं; ‘उच्छ्वासात्’ (श्वास से) लगभग निश्चित पाठ है, फिर भी उस शब्द पर प्रश्न नहीं। "
                   "‘आचरम’ में आ + चरम है: आ (पञ्चमी के साथ) = ‘तक’, चरम = अन्तिम। "
                   "दूसरी पंक्ति: सज्जन बन्धुओं और मित्रों से अनुमत वैद्य, रोगी को अस्वीकार करके; इस इकाई में मुख्य क्रिया नहीं, और ‘चिकित्सा के लिए’ जैसा कुछ संस्कृत में नहीं। "
                   "‘सद्वंधु’ में छपा व, ब के स्थान पर है (इस छपाई का व/ब का अदल-बदल)।"),
    "hook": "अन्तिम साँस तक इलाज: हार न मानो।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 93, how should one treat (चिकित्सेत्)?",
            ("With effort", "चिकित्सेदेव यत्नतः: one should indeed treat with effort."),
            [("With haste", "The line says यत्नतः, with effort, not haste."),
             ("With fasting", "No fasting is named in unit 93."),
             ("With silence", "No silence is named in unit 93.")],
            "चिकित्सेदेव यत्नतः: one should indeed treat, with effort.",
            "यत्नतः = with effort."),
        order(1, "Put the printed parts of unit 93 in the verse's order.",
              ["तस्मादाचरमोच्छासाच्चिकित्सेदेव", "यत्नतः", "सद्वंधुमित्रानुमतः", "प्रत्याख्यायातुरं", "भिषक्"],
              "Therefore up to the last breath one should indeed treat; with effort; approved by good kinsmen and friends; having refused the patient; the physician.",
              "तस्माद्... → यत्नतः → सद्वंधुमित्रानुमतः → प्रत्याख्यायातुरं → भिषक्."),
        match(2, "Match each word of unit 93 to its meaning.",
              [["चिकित्सेत्", "one should treat"], ["यत्नतः", "with effort"], ["अनुमत", "approved"], ["आतुर", "patient"],
               ["भिषक्", "physician"]],
              "चिकित्सेत् = one should treat; यत्नतः = with effort; अनुमत = approved; आतुरम् = the patient; भिषक् = the physician.",
              "चिकित्सेत्, यत्नतः, अनुमत, आतुर, भिषक्.", role="extend",
              teaches="चिकित्सेत् is an optative (the data: 3 sg. opt.): 'one should treat'."),
        mcq("discriminate", 3, "Which split of प्रत्याख्यायातुरं in unit 93 is right?",
            ("प्रत्याख्याय + आतुरम्", "अ + आ → आ: प्रत्याख्याय + आतुरम् → प्रत्याख्यायातुरम्."),
            [("प्रत्याख्या + यातुरम्", "यातुरम् is not a word; the noun is आतुरम्."),
             ("प्रत्याख्यायः + आतुरम्", "अः before आ drops its visarga and leaves a gap: प्रत्याख्याय आतुरम्."),
             ("प्रत्याख्यायि + आतुरम्", "इ + आ would give या: प्रत्याख्याय्यातुरम्.")],
            "प्रत्याख्याय (having refused) + आतुरम् (the patient).",
            "अ + आ → आ."),
        mcq("apply", 4, "In line 2 of unit 93, what has the physician done to the patient (प्रत्याख्याय)?",
            ("Refused or rejected him", "प्रत्याख्याय = having refused, rejected (absolutive of prati-ā-√ख्या)."),
            [("Bathed and anointed him", "प्रत्याख्याय means having refused, not bathing."),
             ("Fed and then rested him", "प्रत्याख्याय means having refused, not feeding."),
             ("Bled and bandaged him", "प्रत्याख्याय means having refused, not bleeding.")],
            "प्रत्याख्यायातुरं भिषक्: the physician, having refused the patient.",
            "प्रत्याख्याय = having refused."),
        mcq("transfer", 5, "Built like आचरम (आ + चरम, 'up to the last'), what does आमरणात् mean in a new example?",
            ("Up to death", "आ with the ablative = up to: आ + मरणात् = up to death."),
            [("Away from death", "आ with the ablative means up to, not away from."),
             ("Without death", "Without would be विना or a negative अ-; आ means up to."),
             ("After death", "After would be ऊर्ध्वम् or पश्चात्; आ means up to.")],
            "आमरणात् = up to death, like आचरम = up to the last.",
            "आ + ablative = up to.",
            teaches="आ with the ablative means 'up to': आ + चरम (up to the last), आमरणात् (up to death)."),
    ],
}

# ---------------------------------------------------------------- unit 94
AUTHORED["94"] = {
    "title": "इति मर्मविभागो नाम सप्तमोऽध्यायः",
    "question": "What does the colophon of unit 94 name?",
    "rule": ("Thus (इति) the seventh (सप्तमः) chapter (अध्यायः), named (नाम) Marmavibhāga, the division of the marmas."),
    "limits": ("Prose colophon, no verb. It names only the chapter and its number; it states nothing about the marmas "
               "themselves."),
    "explain_hi": ("यह अध्याय की समाप्ति-पंक्ति (पुष्पिका) है: ‘इस प्रकार मर्मविभाग नामक सातवाँ अध्याय’। "
                   "मर्मविभाग यानी मर्मों का विभाग, जो इकाई १ में घोषित विषय था। "
                   "‘सप्तम’ क्रमवाचक संख्या है: सातवाँ। "
                   "सन्धियाँ: मर्मविभागः + नाम → मर्मविभागो नाम (अः + घोष व्यंजन → ओ), सप्तमः + अध्यायः → सप्तमोऽध्यायः (अः + अ → ओऽ)। "
                   "छपाई में ‘नामसप्तमोऽध्यायः’ सटा हुआ है।"),
    "hook": "इति... सप्तमोऽध्यायः: मर्मविभाग पूरा।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 94, which chapter ends here?",
            ("The seventh, the Marmavibhāga", "सप्तमोऽध्यायः, named मर्मविभाग."),
            [("The sixth, the Marmavibhāga", "सप्तम is seventh, not sixth (षष्ठ)."),
             ("The eighth, the Marmavibhāga", "सप्तम is seventh, not eighth (अष्टम)."),
             ("The seventh, the Doṣavibhāga", "The chapter is named मर्मविभाग.")],
            "इति मर्मविभागो नाम सप्तमोऽध्यायः.",
            "सप्तम = seventh."),
        order(1, "Put the words of unit 94 in the printed order.",
              ["इति", "मर्मविभागो", "नाम", "सप्तमो", "अध्यायः"],
              "Thus; Marmavibhāga; named; seventh; chapter.",
              "इति → मर्मविभागो → नाम → सप्तमो → अध्यायः."),
        match(2, "Match each word of unit 94 to its meaning.",
              [["इति", "thus"], ["विभाग", "division"], ["नाम", "named"], ["सप्तम", "seventh"], ["अध्याय", "chapter"]],
              "इति = thus; मर्म-विभाग = division of the marmas; नाम = named; सप्तमः अध्यायः = the seventh chapter.",
              "इति, विभाग, नाम, सप्तम, अध्याय.", role="extend",
              teaches="सप्तम (seventh) is the ordinal of सप्त (seven); it agrees with अध्यायः (m. nom. sg.)."),
        mcq("discriminate", 3, "Which split of सप्तमोऽध्यायः in unit 94 is right?",
            ("सप्तमः + अध्यायः", "अः + अ → ओ, the अ dropped (ऽ): सप्तमोऽध्यायः."),
            [("सप्तमो + ध्यायः", "ध्यायः is not the word; it is अध्यायः."),
             ("सप्तम + अध्यायः", "अ + अ would give सप्तमाध्यायः."),
             ("सप्तमे + अध्यायः", "ए + अ would give सप्तमेऽध्यायः.")],
            "सप्तमः (seventh) + अध्यायः (chapter): अः + अ → ओऽ.",
            "अः + अ → ओऽ."),
        mcq("apply", 4, "Why is मर्मविभागः printed मर्मविभागो before नाम in unit 94?",
            ("अः before a voiced consonant gives ओ", "न is a voiced consonant: मर्मविभागः + नाम → मर्मविभागो नाम."),
            [("Any visarga before न gives ओ", "Not any: इः before न gives इर्, आः drops to आ."),
             ("ओ is the vocative ending here", "The data: मर्मविभागः, m. nom. sg.; ओ comes from sandhi."),
             ("The visarga drops before न", "It drops only after आ; after अ it becomes ओ.")],
            "मर्मविभागः + नाम: अः before the voiced न → ओ.",
            "अः + voiced consonant → ओ."),
        mcq("transfer", 5, "By the pattern of सप्तमोऽध्यायः, how is अष्टमः + अध्यायः (the eighth chapter) joined in a new example?",
            ("अष्टमोऽध्यायः", "अः + अ → ओ, the अ dropped (ऽ), as सप्तमः + अध्यायः."),
            [("अष्टमरध्यायः", "र् comes from a visarga after vowels other than अ/आ."),
             ("अष्टमौऽध्यायः", "अः + अ gives ओ, not औ."),
             ("अष्टम अध्यायः", "अः drops to अ only before vowels other than अ; before अ it gives ओऽ.")],
            "अष्टमः + अध्यायः = अष्टमोऽध्यायः.",
            "अः + अ → ओऽ.",
            teaches="अः before अ becomes ओ and the अ is dropped (ऽ): सप्तमः + अध्यायः → सप्तमोऽध्यायः, अष्टमः + अध्यायः → अष्टमोऽध्यायः."),
    ],
}


NOTES_HI = {
    "82": ("गद्य; विश्वास मध्यम; कोई पाठ-चिह्न नहीं। कोई क्रिया नहीं; ‘मर्म’ शब्द छपा नहीं। ‘दल’ = आधा सम्भावित अर्थ है (शब्द पत्ती, भाग भी)। "
           "सन्धि जाँची: षट् + पञ्चाशत् → षट्पञ्चाशत् (प से पहले ट् अघोष ही रहता है); पञ्चाशत् + अङ्गुल → पञ्चाशदङ्गुल (स्वर से पहले त् → द्)। "
           "इकाई ७९-८२ की छपी संख्याएँ १२, ६, ४, २९, ५६ का जोड़ १०७ है; पाठ यह जोड़ यहाँ नहीं कहता। छपाई में अनुस्वार (पंचाशद, अंगुल)।"),
    "83": ("गद्य; विश्वास उच्च; कोई पाठ-चिह्न नहीं। सन्धि जाँची: पुनर् + आहुः → पुनराहुः (स्वर से पहले र् बना रहता है)। आहुः = √अह्, लिट्, "
           "प्रथम पुरुष बहुवचन। समूह-टिप्पणी (डेटा): इकाई ८४-८५ के दूसरे मतों को खोलता दिखता है।"),
    "84": ("गद्य; विश्वास मध्यम; कोई पाठ-चिह्न नहीं। कोई क्रिया नहीं। ‘क्षिप्राणि’ दो तरह पढ़ा जा सकता है: क्षिप्र नामक मर्म (डेटा का पाठ) या "
           "साधारण विशेषण ‘शीघ्र’; इसलिए किस मर्म की बात है, इस पर प्रश्न नहीं। व्रीहि = धान का दाना (मानक पहचान)। कोई सन्धि-जोड़ नहीं। "
           "समूह-टिप्पणी (डेटा): इकाई ८३ के बाद आती और इकाई ८५ में आगे चलती दिखती है।"),
    "85": ("गद्य, दो छपी पंक्तियाँ; विश्वास मध्यम; कोई पाठ-चिह्न नहीं। कलाय = मटर (सम्भावित; खेसारी भी सम्भव); तिल = तिल का दाना (मानक)। "
           "स्तनरोहित और उत्क्षेप को द्वन्द्व में दो मर्म-नाम पढ़ा गया। सन्धि जाँची: स्तनरोहित + उत्क्षेपाः → स्तनरोहितोत्क्षेपाः (अ + उ → ओ); "
           "तथा + अन्ये → तथान्ये (आ + अ → आ; छपा अवग्रह ‘तथाऽन्ये’ छपाई की आदत); तिलप्रमाणानि + अपि → तिलप्रमाणान्यपि (इ + अ → य); "
           "मर्माणि + इच्छन्ति → मर्माणीच्छन्ति (इ + इ → ई)। ‘इच्छन्ति’ का शाब्दिक अर्थ ‘चाहते हैं’।"),
    "86": ("गद्य-सूत्र; विश्वास उच्च; कोई पाठ-चिह्न नहीं। संज्ञा (श्लोक) छपी नहीं। सन्धि जाँची: च + अत्र → चात्र (अ + अ → आ)। "
           "भवन्ति = √भू, वर्तमान, प्रथम पुरुष बहुवचन; छपा ‘भवंति’ अनुस्वार के साथ।"),
    "87": ("श्लोक (छपे रूप में प्रति पंक्ति १६ अक्षर); विश्वास कम। पाठ-चिह्न (सम्भव): ‘मर्मव्यामे’ के लिए अनुमान ‘मर्मव्याप्ते’ (प्त/म की भूल), "
           "पर अपनाया नहीं; शब्द अस्पष्ट छोड़ा गया। ‘आयुः’ और ‘मर्माणि’ दोनों प्रथमा/द्वितीया जैसे; कौन किसकी रक्षा करता है, दो तरह पढ़ा जा सकता है, "
           "या ‘आयुर्मर्माणि’ समास भी। ‘आयुर्व्यापि’ की विभक्ति अनिश्चित, ‘सेवेत’ का कर्म नहीं बताया; √सेव् = सेवा, अभ्यास, भोग भी। "
           "सन्धि जाँची: देहे + अस्मिन् → देहेऽस्मिन् (ए + अ → एऽ); अस्मिन् + आयुः → अस्मिन्नायुः (ह्रस्व स्वर के बाद अन्तिम न् स्वर से पहले दुगना); "
           "आयुः + मर्माणि → आयुर्मर्माणि (उ के बाद विसर्ग + घोष → र्); तस्मात् + विचक्षणः → तस्माद्विचक्षणः (घोष से पहले त् → द्)।"),
    "88": ("श्लोक; विश्वास कम; कोई पाठ-चिह्न नहीं। ‘स्वल्पोऽपिप्रायशो’ छपाई में सटा (स्वल्पः अपि प्रायशः; रिक्त स्थान की भूल)। ‘बाधते’ का कर्म नहीं बताया। "
           "दूसरी पंक्ति अस्पष्ट: विधेय नहीं; ‘प्रक्रान्त’ = आरम्भ किया हुआ, पर चिकित्सा आरम्भ या रोग का जमना, स्पष्ट नहीं। "
           "सन्धि जाँची: सु + अल्प → स्वल्प (उ + अ → व); स्वल्पः + अपि → स्वल्पोऽपि (अः + अ → ओऽ); रोगाः + मर्म → रोगा मर्म (आः, घोष से पहले विसर्ग लुप्त); "
           "मर्माश्रयाः + तद्वत् → मर्माश्रयास्तद्वत् (त से पहले विसर्ग → स्); तद्वत् + प्रक्रान्ताः → तद्वत्प्रक्रान्ताः।"),
    "89": ("श्लोक, प्रति पंक्ति १६ अक्षर; विश्वास मध्यम। पाठ-चिह्न (लगभग निश्चित): छपा ‘श्वािसति’ में भटकी मात्राएँ; पाठ ‘श्वसिति’ (√श्वस्, छन्द भी यही माँगता है); "
           "इस शब्द पर प्रश्न नहीं। कर्ता छपा नहीं; ‘वह’ क्रियाओं से। ‘शून्य’ शाब्दिक (खाली) रखा, सम्भवतः सुध-बुध खोई दशा। "
           "सन्धि जाँची: शून्यः + भ्रमति → शून्यो भ्रमति (अः + घोष व्यंजन → ओ); स्रस्तगात्रः + मुहुः → स्रस्तगात्रो मुहुः; मुहुः + मुहुः → मुहुर्मुहुः (उ के बाद विसर्ग + घोष → र्)।"),
    "90": ("श्लोक; विश्वास उच्च; कोई पाठ-चिह्न नहीं। ‘अवतिष्ठते’ का कर्ता हृदय माना गया; व्यक्ति भी हो सकता है। ‘एतैः लिङ्गैः’ = इकाई ८९ और इस इकाई "
           "की पंक्ति १ के लक्षण (डेटा का पाठ)। सन्धि जाँची: च + अस्य → चास्य (अ + अ → आ); न + एक → नैक (अ + ए → ऐ); स्थाने + अवतिष्ठते → स्थानेऽवतिष्ठते (ए + अ → एऽ); "
           "मर्म + उपघातात् → मर्मोपघातात् (अ + उ → ओ); उपघातात् + मरणम् → उपघातान्मरणम् (अनुनासिक से पहले त् → न्, वैकल्पिक; द् भी सही); "
           "मरणम् + एतैः → मरणमेतैः; एतैः + लिङ्गैः → एतैर्लिङ्गैः (ऐ के बाद विसर्ग + घोष → र्)।"),
    "91": ("श्लोक; विश्वास उच्च। पाठ-चिह्न (लगभग निश्चित): छपा ‘सद्यस्यजति’ में त छूटा; पाठ सद्यः + त्यजति → सद्यस्त्यजति (अक्षर-संख्या वही); इस पर प्रश्न नहीं। "
           "‘अमर्मविद्ध’ = अमर्म में बिंधा, या मर्म में न बिंधा; अर्थ वही। ‘अमर्मविद्धोऽपिनरः’ छपाई में सटा। "
           "सन्धि जाँची: अमर्मविद्धः + अपि → अमर्मविद्धोऽपि (अः + अ → ओऽ); नरः + छेद → नरश्छेद (छ से पहले विसर्ग → श्); भेद + आदि → भेदादि (अ + आ → आ); "
           "अतिनिस्रुतरक्तः + च → अतिनिस्रुतरक्तश्च (च से पहले विसर्ग → श्)।"),
    "92": ("श्लोक; विश्वास कम। पाठ-चिह्न (सम्भव): ‘पुण्यवाच्छ्वियतायुश्चन’ टूटा हुआ; ‘छ्वियता’ कोई ज्ञात शब्द नहीं; आरम्भ शायद पुण्यवान्, फिर आयु का कोई शब्द; "
           "कोई पक्का पाठ नहीं। पक्के शब्द ‘कथंचिन्न जीवति’ = किसी प्रकार नहीं जीता; अनुवाद का दोहरा निषेध अनुमान है, उलटा अर्थ भी सम्भव; पंक्ति २ पर प्रश्न नहीं। "
           "‘अतः अन्यथा’ इकाई ९०-९१ के मर्माघात और रक्त-स्राव की ओर संकेत (डेटा का पाठ)। "
           "सन्धि जाँची: अतः + अन्यथा → अतोऽन्यथा (अः + अ → ओऽ); शरशतैः + अपि → शरशतैरपि (ऐ के बाद विसर्ग + स्वर → र्); कथंचित् + न → कथंचिन्न (अनुनासिक से पहले त् → न्, वैकल्पिक)।"),
    "93": ("श्लोक; विश्वास मध्यम। पाठ-चिह्न (लगभग निश्चित): छपा ‘उच्छासात्’ ज्ञात शब्द नहीं; पाठ ‘उच्छ्वासात्’ (व छूटा, अक्षर-संख्या वही); इस शब्द पर प्रश्न नहीं। "
           "कर्ता (वैद्य) पंक्ति १ में छपा नहीं। पंक्ति २ में मुख्य क्रिया नहीं; ‘प्रत्याख्याय’ = अस्वीकार करके; ‘चिकित्सा के लिए’ संस्कृत में नहीं। ‘सत्’ केवल बन्धु का विशेषण भी हो सकता है। "
           "छपा ‘सद्वंधु’ में व, ब के स्थान पर (व/ब अदल-बदल)। सन्धि जाँची: तस्मात् + आ → तस्मादा (स्वर से पहले त् → द्); चरम + उच्छ्वासात् → चरमोच्छ्वासात् (अ + उ → ओ); "
           "उच्छ्वासात् + चिकित्सेत् → उच्छ्वासाच्चिकित्सेत् (च से पहले त् → च्); चिकित्सेत् + एव → चिकित्सेदेव; प्रत्याख्याय + आतुरम् → प्रत्याख्यायातुरम् (अ + आ → आ)।"),
    "94": ("गद्य, अध्याय की पुष्पिका; विश्वास उच्च; कोई पाठ-चिह्न नहीं। इनपुट में यह श्लोक-प्रकार में था; डेटा अब इसे गद्य मानता है (सही)। "
           "‘नामसप्तमोऽध्यायः’ छपाई में सटा। सन्धि जाँची: मर्मविभागः + नाम → मर्मविभागो नाम (अः + घोष व्यंजन → ओ); सप्तमः + अध्यायः → सप्तमोऽध्यायः (अः + अ → ओऽ)।"),
}


AIDS = {
    "82": {
        "diagram": {"groups": [
            {"label": "माप के अनुसार पाँच भेद (इकाई ७९-८२)", "items": [
                "स्वाङ्गुल: १२ (इकाई ७९)", "दो अंगुल: ६ (इकाई ८०)", "तीन अंगुल: ४ (इकाई ८०)",
                "पाणितल: २९ (इकाई ८१)", "अंगुलदल, सम्भवतः आधा अंगुल: ५६ (इकाई ८२)"]}]},
        "chunks": "शेषाणि | षट्पंचाशदंगुलदलप्रमाणानि",
        "sandhi": "स्वर से पहले त् → द्: पञ्चाशत् + अङ्गुल → पञ्चाशदङ्गुल · षट् + पञ्चाशत् → षट्पञ्चाशत् (प से पहले ट् वैसा ही)।",
    },
    "83": {
        "chunks": "अन्ये | पुनराहुः",
        "frame": "कौन: अन्ये (दूसरे, नाम नहीं) → कब: पुनः (फिर) → क्या करते हैं: आहुः (कहते हैं)।",
        "sandhi": "स्वर से पहले पुनर् का र् बना रहता है: पुनर् + आहुः → पुनराहुः।",
    },
    "84": {
        "frame": "माप: व्रीहि (धान का दाना) → किसका: क्षिप्राणि (डेटा: क्षिप्र मर्म; या विशेषण ‘शीघ्र’)।",
        "chunks": "व्रीहिप्रमाणानि | क्षिप्राणि",
        "anchors": "पक्का भाग: व्रीहि-प्रमाण = धान के दाने भर का माप। खुला भाग: ‘क्षिप्राणि’ नाम या विशेषण। (मेरी याद-पद्धति)",
    },
    "85": {
        "diagram": {"groups": [
            {"label": "कलाय (सम्भवतः मटर) के माप के", "items": ["स्तनरोहित", "उत्क्षेप"]},
            {"label": "अन्य मत: तिल के माप के भी", "items": ["मर्म (नाम नहीं बताए)"]}]},
        "chunks": "कलायप्रमाणानि | स्तनरोहितोत्क्षेपाः | तथाऽन्ये | तिलप्रमाणान्यपि | मर्माणीच्छंति",
        "sandhi": ("अ + उ → ओ: स्तनरोहित + उत्क्षेपाः → स्तनरोहितोत्क्षेपाः · इ + अ → य: तिलप्रमाणानि + अपि → तिलप्रमाणान्यपि · "
                   "इ + इ → ई: मर्माणि + इच्छन्ति → मर्माणीच्छन्ति।"),
    },
    "86": {
        "chunks": "भवंति | चात्र",
        "frame": "क्या: भवन्ति (हैं) → जोड़: च (और) → कहाँ: अत्र (यहाँ); संज्ञा (श्लोक) छपी नहीं।",
        "sandhi": "अ + अ → आ: च + अत्र → चात्र।",
    },
    "87": {
        "chunks": "मर्मव्यामेऽपि | देहेऽस्मिन्नायुर्मर्माणि | रक्षति | आयुर्व्याप्येव | सेवेत | सदा | तस्माद्विचक्षणः",
        "anchors": ("पक्के शब्द: देहे अस्मिन् (इस शरीर में), रक्षति (रक्षा करता है), सदा (सदा), तस्मात् (इसलिए), विचक्षणः (समझदार)। "
                    "धुँधले: मर्मव्यामे, कौन किसकी रक्षा, आयुर्व्यापि की विभक्ति। (मेरी याद-पद्धति)"),
        "sandhi": ("ए + अ → एऽ: देहे + अस्मिन् → देहेऽस्मिन् · ह्रस्व स्वर के बाद न् स्वर से पहले दुगना: अस्मिन् + आयुः → अस्मिन्नायुः · "
                   "घोष से पहले त् → द्: तस्मात् + विचक्षणः → तस्माद्विचक्षणः।"),
    },
    "88": {
        "chunks": "मर्माभिघातः | स्वल्पोऽपिप्रायशो | बाधते | तरां | रोगा | मर्माश्रयास्तद्वत्प्रक्रांता | यत्नतोऽपिच",
        "frame": "क्या: मर्माभिघातः (मर्म पर चोट) → कैसी: स्वल्पः अपि (थोड़ी भी) → कितनी बार: प्रायशः (प्रायः) → फल: बाधते तराम् (बहुत पीड़ा देती है)।",
        "sandhi": "उ + अ → व: सु + अल्प → स्वल्प · अः + अ → ओऽ: स्वल्पः + अपि → स्वल्पोऽपि · आः का विसर्ग घोष से पहले लुप्त: रोगाः + मर्म → रोगा मर्म।",
    },
    "89": {
        "chain": {"steps": ["बहुत फेंका जाता (विक्षिप्यते भृशम्)", "डूबता हुआ (सीदन्)", "खाली-सा (शून्यः)", "घूमता (भ्रमति)",
                            "काँपता (वेपते)", "ऊपर कठिन साँस", "ढीले अंग (स्रस्तगात्रः)", "बार-बार (मुहुर्मुहुः)"]},
        "chunks": "विक्षिप्यते | भृशं | सीदन् | शून्यो | भ्रमति | वेपते | ऊर्ध्वं | श्वािसति | कृच्छ्रेण | स्रस्तगात्रो | मुहुर्मुहुः",
        "sandhi": "अः + घोष व्यंजन → ओ: शून्यः + भ्रमति → शून्यो भ्रमति · उ के बाद विसर्ग + घोष → र्: मुहुः + मुहुः → मुहुर्मुहुः।",
    },
    "90": {
        "chain": {"steps": ["हृदय जलता है", "एक स्थान पर नहीं टिकता", "मर्म पर आघात से", "इन लक्षणों के साथ", "मृत्यु को प्राप्त"]},
        "chunks": "हृदयं | दह्यते | चास्य | नैकस्थानेऽवतिष्ठते | मर्मोपघातान्मरणमेतैर्लिंगैः | समश्नुते",
        "sandhi": ("अ + ए → ऐ: न + एक → नैक · ए + अ → एऽ: स्थाने + अवतिष्ठते → स्थानेऽवतिष्ठते · अनुनासिक से पहले त् → न् (वैकल्पिक; द् भी सही): "
                   "उपघातात् + मरणम् → उपघातान्मरणम्।"),
    },
    "91": {
        "chain": {"steps": ["अमर्म में बिंधा मनुष्य भी", "छेदन, भेदन आदि से पीड़ित", "और रक्त बहुत बह गया", "तुरन्त जीवन छोड़ता है"]},
        "chunks": "अमर्मविद्धोऽपिनरश्छेदभेदादिपीडितः | अतिनिस्रुतरक्तश्च | सद्यस्यजति | जीवितं",
        "sandhi": "अः + अ → ओऽ: अमर्मविद्धः + अपि → अमर्मविद्धोऽपि · च/छ से पहले विसर्ग → श्: नरः + छेद → नरश्छेद, रक्तः + च → रक्तश्च।",
    },
    "92": {
        "frame": "किससे अलग: अतः अन्यथा (इससे अन्यथा) → कौन: विद्धः (बिंधा हुआ) → किससे: शरशतैः अपि (सैकड़ों बाणों से भी) → फल: जीवति (जीता है)।",
        "chunks": "अतोऽन्यथा | जीवति | तु | विद्धः | शरशतैरपि | पुण्यवाच्छ्वियतायुश्चन | कथंचिन्न | जीवति",
        "sandhi": "अः + अ → ओऽ: अतः + अन्यथा → अतोऽन्यथा · ऐ के बाद विसर्ग + स्वर → र्: शरशतैः + अपि → शरशतैरपि।",
        "anchors": "पक्का: पंक्ति १ (सौ बाण, फिर भी जीवित)। टूटा: पंक्ति २ का पहला शब्द; अर्थ की दिशा भी अनिश्चित। (मेरी याद-पद्धति)",
    },
    "93": {
        "chain": {"steps": ["तस्मात्: इसलिए", "आचरम: अन्तिम (श्वास) तक", "यत्नतः: प्रयत्न से", "चिकित्सेत् एव: चिकित्सा करनी ही चाहिए"]},
        "chunks": "तस्मादाचरमोच्छासाच्चिकित्सेदेव | यत्नतः | सद्वंधुमित्रानुमतः | प्रत्याख्यायातुरं | भिषक्",
        "sandhi": ("स्वर से पहले त् → द्: चिकित्सेत् + एव → चिकित्सेदेव · च से पहले त् → च्: -सात् + चिकित्सेत् → -साच्चिकित्सेत् · "
                   "अ + आ → आ: प्रत्याख्याय + आतुरम् → प्रत्याख्यायातुरम्।"),
    },
    "94": {
        "chunks": "इति | मर्मविभागो | नामसप्तमोऽध्यायः",
        "frame": "इति (इस प्रकार) → नाम: मर्मविभाग → क्रम: सप्तमः (सातवाँ) → क्या: अध्यायः।",
        "sandhi": "अः + घोष व्यंजन → ओ: मर्मविभागः + नाम → मर्मविभागो नाम · अः + अ → ओऽ: सप्तमः + अध्यायः → सप्तमोऽध्यायः।",
    },
}


IMAGE_SPECS = {
    ("82", "diagram"): {
        "file": "sh7-parimana-82.svg",
        "alt": ("Table of the five groups of marmas by measure, units 79 to 82: own finger-breadth, twelve (79); two "
                "finger-breadths, six (80); three finger-breadths, four (80); the palm, twenty-nine (81); aṅgula-dala, "
                "probably half a finger-breadth, fifty-six (82)."),
        "type": "table",
        "title": "माप के अनुसार पाँच भेद (इकाई ७९-८२)",
        "heads": ["माप", "संख्या"],
        "rows": [["स्वाङ्गुल (अपना अंगुल)", "१२ (इकाई ७९)"], ["दो अंगुल", "६ (इकाई ८०)"], ["तीन अंगुल", "४ (इकाई ८०)"],
                 ["पाणितल (हथेली)", "२९ (इकाई ८१)"], ["अंगुलदल (सम्भवतः आधा अंगुल)", "५६ (इकाई ८२)"]],
    },
    ("85", "diagram"): {
        "file": "sh7-kalaya-tila-85.svg",
        "alt": ("Flowchart of unit 85: of a kalāya's measure (probably the pea), stanarohita and utkṣepa; likewise others "
                "accept marmas even of a tila's (sesame seed's) measure, not named."),
        "type": "mermaid",
        "code": ("flowchart TD\n"
                 "  A[\"कलाय-माप: सम्भवतः मटर\"] --> B[\"स्तनरोहित\"]\n"
                 "  A --> C[\"उत्क्षेप\"]\n"
                 "  D[\"तथा अन्ये: दूसरे मानते हैं\"] --> E[\"तिल-माप के भी मर्म\"]\n"),
    },
    ("89", "chain"): {
        "file": "sh7-marmaghata-lakshana-89.svg",
        "alt": ("Numbered flowchart of the signs of unit 89 in verse order: greatly tossed about; sinking; empty; reels; "
                "trembles; breathes upward with difficulty; slack limbs; again and again."),
        "type": "mermaid",
        "code": ("flowchart TD\n"
                 "  A[\"१ बहुत फेंका जाता\"] --> B[\"२ डूबता हुआ\"]\n"
                 "  B --> C[\"३ खाली-सा\"]\n"
                 "  C --> D[\"४ घूमता\"]\n"
                 "  D --> E[\"५ काँपता\"]\n"
                 "  E --> F[\"६ ऊपर कठिन साँस\"]\n"
                 "  F --> G[\"७ ढीले अंग\"]\n"
                 "  G --> H[\"८ बार-बार\"]\n"),
    },
    ("90", "chain"): {
        "file": "sh7-hridaya-daha-90.svg",
        "alt": ("Flowchart of unit 90: the heart burns; it does not stay in one place; from injury to a marma, with these "
                "signs, he reaches death."),
        "type": "mermaid",
        "code": ("flowchart TD\n"
                 "  A[\"१ हृदय जलता है\"] --> B[\"२ एक स्थान पर नहीं टिकता\"]\n"
                 "  B --> C[\"३ मर्म पर आघात से\"]\n"
                 "  C --> D[\"४ इन लक्षणों के साथ\"]\n"
                 "  D --> E[\"५ मृत्यु को प्राप्त\"]\n"),
    },
    ("91", "chain"): {
        "file": "sh7-amarma-rakta-91.svg",
        "alt": ("Chain of unit 91: even a man pierced at a non-marma; afflicted by cutting, splitting and the rest; with much "
                "blood flowed out; gives up life at once."),
        "type": "chain",
        "title": "इकाई ९१: अमर्म-घाव और रक्त-स्राव",
        "steps": ["अमर्म में बिंधा मनुष्य भी", "छेदन, भेदन आदि से पीड़ित", "और रक्त बहुत बह गया", "तुरन्त जीवन छोड़ता है"],
    },
    ("93", "chain"): {
        "file": "sh7-acarama-chikitsa-93.svg",
        "alt": ("Chain of line 1 of unit 93: therefore; up to the last (breath); with effort; one should indeed treat."),
        "type": "chain",
        "title": "इकाई ९३: अन्तिम (श्वास) तक चिकित्सा",
        "steps": ["तस्मात्: इसलिए", "आचरम: अन्तिम (श्वास) तक", "यत्नतः: प्रयत्न से", "चिकित्सेत् एव: चिकित्सा करनी ही चाहिए"],
    },
}
