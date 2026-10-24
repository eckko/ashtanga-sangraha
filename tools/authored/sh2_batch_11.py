from helpers import mcq, match, order, fill, multi, accepts


def T(q, teaches):
    q["teaches"] = teaches
    return q


AUTHORED = {}

# ---------------------------------------------------------------- unit 126
AUTHORED["126"] = {
    "title": "यच्च यच्च यस्य व्याधेर्निदानम्",
    "question": "What does prose unit 126 say a pregnant woman's habits do to the offspring she bears?",
    "rule": ("Whatever is the cause (nidāna) of whatever disease: the pregnant woman (antarvatnī) who indulges in each "
             "of those produces offspring abounding in the corresponding disorders."),
    "limits": ("Medium confidence. The printed आसेवमानांऽतर्वत्नी is read as आसेवमाना अन्तर्वत्नी; the anusvara may be a "
               "print slip, so no question rests on that form. No disease, cause or remedy is named; the line gives the "
               "general rule only."),
    "explain_hi": ("यह गद्य-पंक्ति एक सामान्य सिद्धान्त देती है: जिस-जिस रोग का जो-जो निदान (कारण) है, उस-उसका सेवन करती हुई "
                   "अन्तर्वत्नी (गर्भवती) स्त्री उन-उन विकारों से भरपूर सन्तान को जन्म देती है। "
                   "‘यच्च यच्च … तत्तत्’ की दोहराई ‘जो-जो … वह-वह’ का जोड़ा बनाती है। "
                   "यहाँ कोई रोग, कारण या उपचार नाम से नहीं गिनाया गया; केवल सिद्धान्त है। "
                   "छपे ‘आसेवमानांऽतर्वत्नी’ में अनुस्वार सम्भवतः छपाई की भूल है; अर्थ ‘सेवन करती हुई गर्भवती’ लिया गया है।"),
    "hook": "जिस रोग का कारण माँ सेवे, वही विकार सन्तान में भरपूर।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 126, what offspring does a pregnant woman bear who indulges in the cause of a disease?",
            ("Offspring full of those same disorders", "तत्तद्विकारबहुलम् अपत्यम्: offspring full of the corresponding disorders."),
            [("Offspring free of every disorder", "The line says the opposite: abounding in disorders."),
             ("Offspring that dies soon after birth", "Death is not named in this line."),
             ("Offspring of the opposite sex only", "Sex of the child is not named in this line.")],
            "Each cause she indulges in brings the corresponding disorders in the offspring.",
            "निदान सेवन → तत्तद्विकारबहुल अपत्य."),
        order(1, "Put these printed parts of unit 126 in their order.",
              ["यच्च यच्च", "यस्य व्याधेर्निदानं", "तत्तदासेवमानांऽतर्वत्नी स्त्री", "तत्तद्विकारबहुलमपत्यं", "जनयति"],
              "Whatever, of whichever disease the cause, each of those indulging, the pregnant woman, offspring abounding "
              "in each such disorder, produces.",
              "यच्च यच्च → यस्य व्याधेर्निदानं → तत्तदासेवमाना… → तत्तद्विकारबहुलमपत्यं → जनयति."),
        T(match(2, "Match each word of unit 126 to its meaning on the card.",
                [["निदान", "cause (of disease)"], ["अन्तर्वत्नी", "pregnant woman"], ["व्याधि", "disease"],
                 ["बहुल", "abounding in"], ["अपत्य", "offspring"]],
                "These five words carry the rule: the cause of a disease, the pregnant woman, and offspring abounding in disorders.",
                "निदान, अन्तर्वत्नी, व्याधि, बहुल, अपत्य.", role="extend"),
          "अन्तर्वत्नी is a word for the pregnant woman; निदान is the cause of a disease."),
        mcq("discriminate", 3, "Which split of व्याधेर्निदानम् is right?",
            ("व्याधेः + निदानम्", "एः before the voiced न becomes एर्: व्याधेर्निदानम्."),
            [("व्याधिः + निदानम्", "That would join as व्याधिर्निदानम्, with इ."),
             ("व्याधेः + अनिदानम्", "That would join as व्याधेरनिदानम्, with an अ."),
             ("व्याधे + र्निदानम्", "र्निदानम् is not a word.")],
            "व्याधेः (of the disease, gen. sg.) + निदानम् (cause).",
            "Visarga after a vowel other than अ/आ becomes र् before a voiced sound."),
        mcq("apply", 4, "A pregnant woman keeps taking what is the cause of disease X. By unit 126, what follows?",
            ("Her offspring abounds in disorder X", "Each cause she indulges in gives the corresponding disorder in the offspring."),
            [("She is cured of disorder X herself", "The line speaks of the offspring, not a cure."),
             ("Her offspring is protected from X", "The line says the offspring abounds in it."),
             ("Only the father's line is affected", "The father is not named in this line.")],
            "Cause indulged in by the mother → that disorder abounds in the offspring.",
            "तत्तद् आसेवमाना → तत्तद्विकारबहुलम् अपत्यम्."),
        T(mcq("transfer", 5, "By the rule of यत् + च → यच्च, how is तत् + च written when joined?",
              ("तच्च", "त् before च becomes च्: तत् + च → तच्च."),
              [("तद्च", "त् becomes द् before a vowel or voiced sound, not before च."),
               ("तज्च", "ज् does not come from त् before च."),
               ("तश्च", "श् comes from a visarga before च, not from त्.")],
              "यत् + च → यच्च; so तत् + च → तच्च.",
              "त् + च → च्च."),
          "A final त् before च is assimilated to च्: यच्च, तच्च."),
    ],
}

# ---------------------------------------------------------------- unit 127
AUTHORED["127"] = {
    "title": "एतेन पितृजा अपिशुक्रदोषा व्याख्याताः",
    "question": "What does unit 127 say is also explained by this, and what should the two wishing for good offspring do?",
    "rule": ("By this the faults of śukra (semen) born of the father are also explained. Therefore the two, wishing for "
             "success of offspring (prajā-sampad), should look after themselves well."),
    "limits": ("Prose of two printed lines. एतेन (by this) points back to the account of the mother's habits. दोष here "
               "means fault, not the humour. The dual subject is 'the two' (in context the couple); the line does not "
               "name them. No particular fault of śukra is listed."),
    "explain_hi": ("पहली पंक्ति कहती है: इसी (माता के आचरण के वर्णन) से पिता से उत्पन्न शुक्र के दोष भी समझा दिए गए हैं। "
                   "यहाँ ‘दोष’ का अर्थ त्रुटि है, वात-पित्त-कफ वाला दोष नहीं। "
                   "दूसरी पंक्ति: इसलिए सन्तान की सम्पन्नता (प्रजासम्पद्) चाहने वाले दोनों अपनी भली-भाँति देखभाल करें। "
                   "‘इच्छन्तौ’ और ‘उपाचरेताम्’ द्विवचन हैं: दो जन; प्रसंग से दम्पती, पर पंक्ति नाम नहीं लेती।"),
    "hook": "माँ के दोषों से पिता के शुक्र-दोष भी समझो; इसलिए दोनों अपना ध्यान रखें।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 127, what is also explained by this (एतेन)?",
            ("The faults of śukra born of the father", "पितृजा अपि शुक्रदोषा व्याख्याताः."),
            [("The diet of the newborn after birth", "The newborn's diet is not named in this unit."),
             ("The signs of a male embryo in the womb", "No signs of sex are named in this unit."),
             ("The causes of a hard labour at term", "Labour is not named in this unit.")],
            "The faults of śukra that come from the father are explained by the same account.",
            "पितृज शुक्रदोष = faults of semen born of the father."),
        order(1, "Put the words of unit 127, line 2, in their printed order.",
              ["तस्मात्", "प्रजासंपदम्", "इच्छंतौ", "साधु", "आत्मानम्", "उपाचरेताम्"],
              "Therefore, success of offspring, wishing, well, self, should look after.",
              "तस्मात् → प्रजासंपदम् → इच्छंतौ → साधु → आत्मानम् → उपाचरेताम्."),
        T(match(2, "Match each word of unit 127 to its meaning on the card.",
                [["पितृज", "born of the father"], ["दोष", "fault (here, not the humour)"], ["व्याख्यात", "explained"],
                 ["प्रजासम्पद्", "success of offspring"], ["साधु", "well"]],
                "Line 1 gives what is explained; line 2 gives what the two should do.",
                "पितृज, दोष, व्याख्यात, प्रजासम्पद्, साधु.", role="extend"),
          "दोष can mean a fault as well as a humour; here the card reads fault."),
        mcq("discriminate", 3, "Why is पितृजाः printed as पितृजा before अपि?",
            ("Visarga after आ drops before a vowel", "पितृजाः + अपि → पितृजा अपि: regular sandhi."),
            [("Visarga becomes र् before a vowel", "र् comes after vowels other than अ/आ, not after आ."),
             ("Visarga with आ turns into ओ", "ओ comes from अः, not from आः."),
             ("A letter is lost in the print", "The note calls it regular visarga loss, not a print loss.")],
            "आः before a vowel or a voiced consonant loses its visarga.",
            "आः + vowel → आ (the visarga drops)."),
        mcq("apply", 4, "By the card, who should look after themselves in line 2 of unit 127?",
            ("The two (dual), in context the couple", "इच्छन्तौ and उपाचरेताम् are dual: two persons."),
            [("The physician alone (singular)", "The forms are dual, not singular."),
             ("The child after its birth, alone", "The child is the wished-for result, not the subject."),
             ("All the relatives (plural form)", "The forms are dual, not plural.")],
            "Both the participle and the verb are dual: the two wishing for success of offspring.",
            "-अन्तौ, -एताम् = dual."),
        T(mcq("transfer", 5, "Built like इच्छन्तौ (two wishing), which invented form means two going?",
              ("गच्छन्तौ", "Present participle stem गच्छत् + -औ: two going."),
              [("गच्छन्", "That is one going (singular)."),
               ("गच्छन्तः", "That is many going (plural)."),
               ("गच्छतः", "As a verb it means the two go; as a participle it is gen./abl. sg. or acc. pl., not nom. dual.")],
              "इच्छन्तौ = two wishing; गच्छन्तौ = two going.",
              "-न्तौ = nom. dual of a masculine present participle."),
          "A masculine present participle of the अ-class (इच्छति, गच्छति) ends in -न्तौ in the nominative dual: इच्छन्तौ, गच्छन्तौ."),
    ],
}

# ---------------------------------------------------------------- unit 128
AUTHORED["128"] = {
    "title": "विशेषेण नारी",
    "question": "Whom does the two-word prose unit 128 single out?",
    "rule": "Especially the woman (nārī).",
    "limits": ("Two words only. No verb is printed; the data takes the verb of unit 127 (उपाचरेताम्, should look after) "
               "or a similar one as understood and does not supply it. No question asks whether it continues unit 127."),
    "explain_hi": ("यह केवल दो शब्दों की गद्य-पंक्ति है: विशेषेण नारी, यानी विशेष रूप से स्त्री। "
                   "कोई क्रिया छपी नहीं; इकाई १२७ की ‘उपाचरेताम्’ (देखभाल करें) जैसी क्रिया समझी जाती है, जोड़ी नहीं गई। "
                   "‘विशेषेण’ तृतीया एकवचन है, पर अव्यय की तरह ‘विशेष रूप से’ के अर्थ में आया है। "
                   "‘नारी’ स्त्रीलिंग प्रथमा एकवचन है।"),
    "hook": "दोनों ध्यान रखें, पर विशेषेण नारी।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "Whom does unit 128 single out?",
            ("The woman", "विशेषेण नारी: especially the woman."),
            [("The father of the child", "No father is named in this unit."),
             ("The attending physician", "No physician is named in this unit."),
             ("The newborn child", "No child is named in this unit.")],
            "The unit says: especially the woman.",
            "नारी = woman."),
        mcq("warmup", 1, "Which English of विशेषेण नारी is right?",
            ("Especially the woman", "विशेषेण = especially; नारी = woman."),
            [("Never the woman", "No negation is printed."),
             ("Only the man", "नारी is the woman, not the man."),
             ("The woman alone, never others", "विशेषेण means especially, not only.")],
            "Two words: especially (विशेषेण), the woman (नारी).",
            "विशेषेण = especially."),
        fill(2, "In unit 128 the word for woman is ____ (type it in Devanagari or in English letters, e.g. dharma).",
             accepts("नारी", None, "nari"),
             "नारी = woman (f. nom. sg.).",
             "नारी is a word for woman; here it stands in the nominative.",
             "नारी = woman."),
        mcq("discriminate", 3, "What is विशेषेण on the card?",
            ("An instrumental used as an adverb", "m. inst. sg. used as ind.: especially."),
            [("A verb: she should single out", "No verb is printed in this unit."),
             ("A nominative noun: the distinction", "The ending -एण is instrumental, not nominative."),
             ("A locative: in the special one", "A locative would end in -ए, as विशेषे.")],
            "विशेषेण is an instrumental singular that works as the adverb 'especially'.",
            "-एन / -एण = inst. sg. of an अ-stem."),
        multi("apply", 4, "Which two are right about unit 128 by the card?",
              [("It names the father as the one meant", "नारी is the woman; no father is named."),
               ("It is a prose line", "Right: the unit is prose."),
               ("नारी is the object, in the accusative", "The card gives नारी as f. nom. sg."),
               ("No verb is printed in it", "Right: the verb is only understood.")],
              [1, 3],
              "Unit 128 is a two-word prose line with no printed verb.",
              "Prose; no verb; नारी nom. sg."),
        T(mcq("transfer", 5, "Built like विशेषेण, which invented form is the instrumental singular of सुख (ease)?",
              ("सुखेन", "अ-stem + -एन = inst. sg.: with ease."),
              [("सुखस्य", "That is the genitive: of ease."),
               ("सुखे", "That is the locative: in ease."),
               ("सुखानि", "That is a plural nominative or accusative.")],
              "विशेष → विशेषेण; सुख → सुखेन.",
              "अ-stem inst. sg. = -एन (-एण after ष/र)."),
          "The instrumental singular of an अ-stem ends in -एन, or -एण after ष or र: सुखेन, विशेषेण."),
    ],
}

# ---------------------------------------------------------------- unit 129
AUTHORED["129"] = {
    "title": "व्याधींश्चास्या",
    "question": "With what kind of means does unit 129 say her diseases should be treated?",
    "rule": ("One should treat her diseases with mild, sweet, cool and pleasant medicines (auṣadha), foods (āhāra) and "
             "regimens (vihāra)."),
    "limits": ("The four qualities are read as qualifying all three means (the data's reading). No medicine, food or "
               "regimen is named and no dose is given. The printed ऊ of 'रूपाचरेत्' is a certain print slip for उ."),
    "explain_hi": ("यह पंक्ति गर्भिणी के रोगों के उपचार का ढंग बताती है: मृदु, मधुर, शिशिर (शीतल) और सुखकर "
                   "औषध, आहार और विहार से उपचार करे। "
                   "विहार का अर्थ है दिनचर्या या आचरण। चारों गुण तीनों साधनों पर लागू माने गए हैं। "
                   "कोई विशेष औषध या मात्रा नहीं बताई गई। ‘व्याधींश्च’ में व्याधीन् + च की सन्धि है।"),
    "hook": "चार गुण (मृदु, मधुर, शिशिर, सुख) × तीन साधन (औषध, आहार, विहार)।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 129, what kind of means should treat her diseases?",
            ("Mild, sweet, cool and pleasant", "मृदुमधुरशिशिरसुखैः: the four qualities of the means."),
            [("Sharp, hot, bitter and strong", "These are the opposite of the qualities named."),
             ("Heavy, sour, hot and dry", "None of these is named in the line."),
             ("Pungent, light, warm and quick", "None of these is named in the line.")],
            "Her diseases are treated with mild, sweet, cool and pleasant medicines, foods and regimens.",
            "मृदु, मधुर, शिशिर, सुख."),
        order(1, "Put the four qualities of unit 129 in their printed order.",
              ["मृदु", "मधुर", "शिशिर", "सुख"],
              "The compound reads मृदुमधुरशिशिरसुखैः: mild, sweet, cool, pleasant.",
              "मृदु → मधुर → शिशिर → सुख."),
        T(match(2, "Match each word of unit 129 to its meaning on the card.",
                [["औषध", "medicine"], ["आहार", "food"], ["विहार", "regimen, conduct"], ["शिशिर", "cool"],
                 ["मृदु", "mild"]],
                "Three words name the means, two name qualities of the means.",
                "औषध, आहार, विहार; शिशिर, मृदु.", role="extend"),
          "विहार here is regimen or conduct, the daily activities, beside medicine and food."),
        mcq("discriminate", 3, "Which split of व्याधींश्च is right?",
            ("व्याधीन् + च", "न् before च becomes ंश्: व्याधीन् + च → व्याधींश्च."),
            [("व्याधीः + च", "Visarga before च gives श् only: व्याधीश्च, with no anusvara."),
             ("व्याधिम् + च", "That would be written व्याधिं च, with no श्."),
             ("व्याधीं + श्च", "श्च is not a word.")],
            "व्याधीन् (diseases, acc. pl.) + च (and).",
            "Final न् + च → ंश्च."),
        multi("apply", 4, "Which three does unit 129 name as the means of treatment?",
              [("Foods (आहार)", "Right: आहार is one of the three means."),
               ("Emesis (वमन)", "Emesis is not named here; the next unit forbids it."),
               ("Medicines (औषध)", "Right: औषध is one of the three means."),
               ("Regimens (विहार)", "Right: विहार is one of the three means.")],
              [0, 2, 3],
              "The three means are medicines, foods and regimens.",
              "औषध, आहार, विहार."),
        T(mcq("transfer", 5, "Built like उपाचरेत् (one should treat), which invented form means one should read?",
              ("पठेत्", "Root पठ् + -एत्: one should read (optative, 3rd sg.)."),
              [("पठति", "That means he reads, a present."),
               ("पठितुम्", "That means to read, an infinitive."),
               ("पठित्वा", "That means having read.")],
              "उपाचरेत् = one should treat; पठेत् = one should read.",
              "-एत् = optative 3rd sg.: should."),
          "The ending -एत् gives the optative, one should do: उपाचरेत्, पठेत्."),
    ],
}

# ---------------------------------------------------------------- unit 130
AUTHORED["130"] = {
    "title": "न चास्या वमनादीनि प्रयोजयेत्",
    "question": "What does unit 130 forbid for her?",
    "rule": "And one should not apply to her emesis (vamana) and the rest.",
    "limits": ("आदि (and the rest) means the other cleansing procedures; they are not listed in this line. The genitive "
               "अस्याः is taken as to/for her."),
    "explain_hi": ("यह छोटी गद्य-पंक्ति निषेध करती है: इस (गर्भिणी) के लिए वमन आदि का प्रयोग न करे। "
                   "वमन का अर्थ है चिकित्सा के लिए उल्टी कराना। ‘आदि’ से बाकी शोधन-कर्म समझे जाते हैं, पर यहाँ उनके नाम नहीं हैं। "
                   "‘अस्याः’ षष्ठी है, ‘इसके लिए’ के अर्थ में लिया गया। ‘चास्या’ में च + अस्याः की सन्धि है।"),
    "hook": "गर्भिणी को वमन आदि नहीं।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 130, what should not be applied to her?",
            ("Emesis and the rest", "न … वमनादीनि प्रयोजयेत्."),
            [("Mild and sweet foods", "These are recommended in unit 129, not forbidden here."),
             ("Cool and pleasant regimens", "These are recommended in unit 129, not forbidden here."),
             ("Pleasant medicines", "These are recommended in unit 129, not forbidden here.")],
            "Emesis and the rest are not to be applied to her.",
            "न + प्रयोजयेत् = should not apply."),
        order(1, "Put the printed words of unit 130 in their order.",
              ["न", "चास्या", "वमनादीनि", "प्रयोजयेत्"],
              "Not, and for her, emesis and the rest, one should apply.",
              "न → चास्या → वमनादीनि → प्रयोजयेत्."),
        T(match(2, "Match each word of unit 130 to its meaning on the card.",
                [["न", "not"], ["अस्याः", "for her"], ["वमन", "emesis"], ["आदि", "and the rest"],
                 ["प्रयोजयेत्", "one should apply"]],
                "Five words make the whole prohibition.",
                "न, अस्याः, वमन, आदि, प्रयोजयेत्.", role="extend"),
          "वमन is therapeutic emesis; -आदि adds the rest of the group without naming them."),
        mcq("discriminate", 3, "What does आदि in वमनादीनि tell, by the card?",
            ("Other procedures follow, not named here", "आदि = and the rest: the other cleansing procedures."),
            [("Only emesis is meant, nothing else", "आदि adds others to emesis."),
             ("Emesis is to be given first of all", "आदि means and the rest, not first."),
             ("The full list is printed in this line", "The others are not listed here.")],
            "वमन-आदि = emesis and the rest; the rest are not listed in this line.",
            "X-आदि = X and the rest."),
        mcq("apply", 4, "Which English of न चास्या वमनादीनि प्रयोजयेत् is right?",
            ("And one should not apply emesis and the rest to her",
             "न = not; अस्याः = for her (f.); वमनादीनि = emesis and the rest."),
            [("And one should apply emesis and the rest to her", "This drops न, the not."),
             ("And one should not apply emesis and the rest to him", "अस्याः is feminine: her."),
             ("And one should not apply emesis alone to her", "आदि means and the rest, not alone.")],
            "Each wrong English changes one word: न, the gender of अस्याः, or आदि.",
            "न … प्रयोजयेत् = should not apply."),
        T(mcq("transfer", 5, "Built like वमनादीनि, what does an invented स्नानादीनि mean?",
              ("Bathing and the rest", "स्नान + आदि: bathing and the others of its group."),
              [("Bathing only, no other", "आदि adds others; it is not only."),
               ("The very first bath", "आदि does not mean first here."),
               ("After the bath is over", "आदि does not mean after.")],
              "वमन + आदि → वमनादीनि; स्नान + आदि → स्नानादीनि.",
              "X-आदि = X and the rest."),
          "-आदि at the end of a compound means X and the rest: वमनादीनि, स्नानादीनि."),
    ],
}

# ---------------------------------------------------------------- unit 131
AUTHORED["131"] = {
    "title": "केवलं त्वष्टमं मासमुपादाय",
    "question": "From which month does unit 131 bring in āsthāpana and anuvāsana?",
    "rule": ("Not bloodletting; but only, beginning from the eighth month, āsthāpana (decoction enema) or anuvāsana "
             "(oil enema)."),
    "limits": ("Medium confidence. The printed रक्त्ता- has a doubled त (possibly a print slip): no question on it. "
               "No verb; प्रयोजयेत् of unit 130 is understood. Whether the enemas are an exception to the prohibition "
               "is left open; no question asks this. No dose or method."),
    "explain_hi": ("इस पंक्ति में पहले ‘न रक्त्तावसेचनम्’ है: रक्त निकालना नहीं (छपे ‘रक्त्ता’ का दोहरा त सम्भवतः छपाई की भूल)। "
                   "फिर: किन्तु केवल आठवें मास से आरम्भ करके आस्थापन (काढ़े की बस्ति) या अनुवासन (तेल की बस्ति)। "
                   "क्रिया छपी नहीं; इकाई १३० की ‘प्रयोजयेत्’ समझी जाती है। "
                   "पाठ यह तय नहीं करता कि बस्तियाँ निषेध का अपवाद हैं या निषेध में ही आती हैं; शाब्दिक क्रम ही रखा गया है।"),
    "hook": "आठवाँ मास: आस्थापन या अनुवासन (अपवाद है या नहीं, पाठ खुला)।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 131, from which month are āsthāpana and anuvāsana spoken of?",
            ("From the eighth month", "अष्टमं मासमुपादाय: beginning from the eighth month."),
            [("From the third month", "The word printed is अष्टमम्, eighth."),
             ("From the fifth month", "The word printed is अष्टमम्, eighth."),
             ("From the seventh month", "The word printed is अष्टमम्, eighth.")],
            "The line names the eighth month (अष्टम मास).",
            "अष्टम = eighth."),
        order(1, "Put these words of unit 131 in their order.",
              ["केवलं", "त्वष्टमं", "मासमुपादाय", "आस्थापनम्", "अनुवासनं वा"],
              "Only, but the eighth, month beginning from, āsthāpana, or anuvāsana.",
              "केवलं → त्वष्टमं → मासमुपादाय → आस्थापनम् → अनुवासनं वा."),
        T(match(2, "Match each word of unit 131 to its meaning on the card.",
                [["आस्थापन", "decoction enema (standard)"], ["अनुवासन", "oil enema (standard)"], ["अष्टम", "eighth"],
                 ["उपादाय", "beginning from"], ["केवलम्", "only"]],
                "Two enemas, the month, and the words that frame them.",
                "आस्थापन, अनुवासन, अष्टम, उपादाय, केवलम्.", role="extend"),
          "आस्थापन is a decoction enema and अनुवासन an oil enema (standard identifications)."),
        mcq("discriminate", 3, "Which split of त्वष्टमम् is right?",
            ("तु + अष्टमम्", "उ before a different vowel becomes व्: तु + अष्टमम् → त्वष्टमम्."),
            [("त्वा + अष्टमम्", "आ + अ would join as त्वाष्टमम्, with आ."),
             ("ते + अष्टमम्", "ए + अ would join as तेऽष्टमम्."),
             ("त्वम् + अष्टमम्", "That would join as त्वमष्टमम्.")],
            "तु (but) + अष्टमम् (eighth).",
            "उ + a different vowel → व् + that vowel."),
        multi("apply", 4, "Which two does unit 131 state plainly, by the card?",
              [("Both enemas are given together daily", "वा means or; no frequency is given."),
               ("The eighth month is named", "Right: अष्टमं मासम्."),
               ("The two enemas are joined by वा, or", "Right: आस्थापनम् अनुवासनं वा."),
               ("Emesis is named again in this line", "Emesis is in unit 130, not in this line.")],
              [1, 2],
              "Sure in the line: the eighth month, and two enemas with or between them.",
              "अष्टमं मासम्; आस्थापनम् अनुवासनं वा."),
        T(mcq("transfer", 5, "By the rule of तु + अष्टमम्, how is मधु + अस्ति written when joined?",
              ("मध्वस्ति", "उ + अ → व: मधु + अस्ति → मध्वस्ति."),
              [("मधोस्ति", "उ + अ does not give ओ."),
               ("मधूस्ति", "उ + अ does not give a long ऊ."),
               ("माध्वस्ति", "The first vowel does not change.")],
              "तु + अष्टमम् → त्वष्टमम्; so मधु + अस्ति → मध्वस्ति.",
              "उ + a different vowel → व्."),
          "A final उ before a different vowel becomes व् and the vowel follows: त्वष्टमम्, मध्वस्ति."),
    ],
}

# ---------------------------------------------------------------- unit 132
AUTHORED["132"] = {
    "title": "वमनादिसाध्येषु पुनर्विकारेषु",
    "question": "How does unit 132 say one should proceed in her disorders that are curable by emesis and the rest?",
    "rule": ("But in disorders curable by emesis (vamana) and the rest, one should proceed with mild (ones) or with "
             "those that accomplish the same purpose."),
    "limits": ("The means are not named: 'mild (ones)' and 'those that do the same work' are left general. No dose. "
               "upakrama = beginning of treatment."),
    "explain_hi": ("इकाई १३० में वमन आदि का निषेध था; यहाँ प्रश्न है कि जो विकार वमन आदि से ही साध्य हैं, उनमें क्या करें। "
                   "उत्तर: मृदु (साधनों) से, या उसी प्रयोजन को पूरा करने वालों (तदर्थकारी) से उपक्रम (उपचार का आरम्भ) करे। "
                   "साधनों के नाम नहीं दिए गए। "
                   "‘वोपक्रमेत्’ में वा + उपक्रमेत् की सन्धि है (आ + उ → ओ)।"),
    "hook": "वमन-साध्य रोग? मृदु से, या जो वही काम करे उससे।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "Which disorders does unit 132 speak of?",
            ("Those emesis and the rest would cure", "वमनादिसाध्येषु विकारेषु."),
            [("Those of the newborn after birth", "The newborn is not named in this line."),
             ("Those from the father's śukra", "That is unit 127, not this line."),
             ("Those that arise only at delivery", "Delivery is not named in this line.")],
            "The line speaks of disorders that emesis and the rest would cure.",
            "वमनादिसाध्य = curable by emesis and the rest."),
        order(1, "Put these words of unit 132 in their order.",
              ["वमनादिसाध्येषु", "विकारेषु", "मृदुभिः", "तदर्थकारिभिः", "उपक्रमेत्"],
              "In curable-by-emesis-etc., disorders, with mild (ones), with those doing that purpose, one should proceed.",
              "वमनादिसाध्येषु → विकारेषु → मृदुभिः → तदर्थकारिभिः → उपक्रमेत्."),
        T(match(2, "Match each word of unit 132 to its meaning on the card.",
                [["साध्य", "curable by"], ["विकार", "disorder"], ["मृदु", "mild"],
                 ["तदर्थकारिन्", "accomplishing that purpose"], ["उपक्रमेत्", "one should proceed (to treat)"]],
                "Where (disorders curable by emesis), with what (mild or same-purpose means), and the verb.",
                "साध्य, विकार, मृदु, तदर्थकारिन्, उपक्रमेत्.", role="extend"),
          "तद्-अर्थ-कारिन् = that-purpose-doing: a means that does the same work."),
        mcq("discriminate", 3, "Which split of वोपक्रमेत् is right?",
            ("वा + उपक्रमेत्", "आ + उ → ओ: वा + उपक्रमेत् → वोपक्रमेत्."),
            [("वा + अपक्रमेत्", "आ + अ would join as वापक्रमेत्."),
             ("वाः + उपक्रमेत्", "आः before a vowel loses its visarga and stays apart (वा उपक्रमेत्): no ओ. And वा here is the indeclinable, or."),
             ("वो + पक्रमेत्", "पक्रमेत् is not a word.")],
            "वा (or) + उपक्रमेत् (one should proceed).",
            "आ + उ → ओ."),
        mcq("apply", 4, "A pregnant woman has a disorder that emesis would usually cure. By unit 132, what is done?",
            ("Treat with mild or same-purpose means", "मृदुभिस्तदर्थकारिभिर्वा उपक्रमेत्."),
            [("Give emesis at full strength anyway", "The line turns to mild or same-purpose means instead."),
             ("Leave it untreated until delivery", "The line says one should proceed to treat."),
             ("Treat it with bloodletting instead", "No bloodletting is named in this line.")],
            "Mild means, or means that do the same work, are used.",
            "मृदु or तदर्थकारी साधन."),
        T(mcq("transfer", 5, "Built like विकारेषु (in disorders), which is the locative plural of व्याधि (disease)?",
              ("व्याधिषु", "इ-stem + -षु: in diseases."),
              [("व्याधीन्", "That is the accusative plural."),
               ("व्याधिभिः", "That is the instrumental plural."),
               ("व्याधेः", "That is the genitive or ablative singular.")],
              "विकार → विकारेषु; व्याधि → व्याधिषु.",
              "Locative plural ends in -सु / -षु."),
          "The locative plural ends in -सु, which becomes -षु after इ, उ, ए and similar sounds: विकारेषु, व्याधिषु."),
    ],
}

# ---------------------------------------------------------------- unit 133
AUTHORED["133"] = {
    "title": "पूर्णमिवतैलपात्रम्",
    "question": "With what simile does unit 133 say the pregnant woman should be attended to?",
    "rule": "Like a full vessel of oil, one should attend to the pregnant woman (garbhiṇī) without shaking (her).",
    "limits": ("The object of 'not shaking' is not printed (her, or by the simile the vessel). The printed द् before "
               "गर्भिणीम् may be a stray letter; no question rests on it. The closing इति ends the prose passage. "
               "No particular act of care is named."),
    "explain_hi": ("यह गद्य-पंक्ति एक उपमा देती है: जैसे तेल से भरे पात्र को बिना हिलाए सँभालते हैं, वैसे ही गर्भिणी की "
                   "बिना हिलाए (असंक्षोभयन्) सेवा करे। "
                   "‘असंक्षोभयन्’ में अ- निषेध है: न हिलाते हुए। किसे न हिलाए, यह छपा नहीं; ‘उसे’ केवल पढ़ने की सुविधा के लिए है। "
                   "अन्त का ‘इति’ गद्य-भाग को समाप्त करता है।"),
    "hook": "भरा तेल-पात्र: छलके नहीं; गर्भिणी: हिले नहीं।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "To what does unit 133 compare the pregnant woman?",
            ("A full vessel of oil", "पूर्णम् इव तैलपात्रम्."),
            [("An empty clay pot", "The vessel is full (पूर्ण), and of oil."),
             ("A lamp in the wind", "No lamp is named."),
             ("A full jar of water", "The vessel is of oil (तैल), not water.")],
            "Like a full vessel of oil, she is attended without shaking.",
            "पूर्ण तैलपात्र = full oil-vessel."),
        order(1, "Put the words of unit 133 in their order.",
              ["पूर्णम्", "इव", "तैलपात्रम्", "असंक्षोभयन्", "गर्भिणीम्", "उपाचरेत्"],
              "Full, like, oil-vessel, not shaking, the pregnant woman, one should attend to.",
              "पूर्णम् → इव → तैलपात्रम् → असंक्षोभयन् → गर्भिणीम् → उपाचरेत्."),
        T(match(2, "Match each word of unit 133 to its meaning on the card.",
                [["पूर्ण", "full"], ["तैल", "oil"], ["पात्र", "vessel"], ["असंक्षोभयन्", "not shaking"],
                 ["गर्भिणी", "pregnant woman"]],
                "Three words make the simile; two name the manner and the one cared for.",
                "पूर्ण, तैल, पात्र, असंक्षोभयन्, गर्भिणी.", role="extend"),
          "इव after a word makes a simile: पूर्णम् इव तैलपात्रम् = like a full vessel of oil."),
        mcq("discriminate", 3, "Which split of उपाचरेदिति is right?",
            ("उपाचरेत् + इति", "त् before a vowel becomes द्: उपाचरेदिति."),
            [("उपाचरेः + इति", "A visarga here would give उपाचरेरिति."),
             ("उपाचरेत् + ईति", "ईति would show a long ई: उपाचरेदीति."),
             ("उपाचरे + दिति", "दिति is not the card's word.")],
            "उपाचरेत् (one should attend to) + इति (thus, closing).",
            "Final त् + vowel → द्."),
        mcq("apply", 4, "A carer follows unit 133. Which manner of care fits it?",
            ("Steady care that does not shake her", "असंक्षोभयन्: without shaking, like a full oil-vessel."),
            [("Brisk care with strong jolting", "That is the shaking the line forbids."),
             ("Care given only after delivery", "The line is about the pregnant woman (गर्भिणी)."),
             ("Care that leaves her alone entirely", "उपाचरेत् says one should attend to her.")],
            "Attend to her, but without agitating, as one carries a full vessel of oil.",
            "असंक्षोभयन् + उपाचरेत्."),
        T(mcq("transfer", 5, "Built like पूर्णम् इव तैलपात्रम्, which invented phrase means like a lamp?",
              ("दीपम् इव", "इव after a noun: like that thing."),
              [("दीपम् विना", "विना means without."),
               ("दीपम् प्रति", "प्रति means towards."),
               ("दीपात् ऋते", "ऋते means except.")],
              "इव follows the thing compared: तैलपात्रम् इव, दीपम् इव.",
              "X इव = like X."),
          "इव placed after a word means like: the thing compared comes before इव."),
    ],
}

# ---------------------------------------------------------------- unit 134
AUTHORED["134"] = {
    "title": "भवंति चात्र",
    "question": "What does the short prose formula of unit 134 do?",
    "rule": "And on this matter there are these: a lead-in formula to what follows.",
    "limits": ("The noun (what there are) is not printed and is not supplied. The formula leads in to the verses that "
               "follow from unit 135; it states no teaching of its own."),
    "explain_hi": ("‘भवन्ति चात्र’ एक परिचित सूत्र-वाक्य है: और इस विषय में ये हैं। "
                   "क्या हैं, यह संज्ञा छपी नहीं; जोड़ी भी नहीं गई। "
                   "यह आगे आने वाले श्लोकों (इकाई १३५ से) की भूमिका है। "
                   "‘भवन्ति’ √भू का वर्तमान, प्रथम पुरुष बहुवचन है; ‘चात्र’ में च + अत्र की सन्धि है।"),
    "hook": "भवन्ति चात्र: आगे श्लोक आ रहे हैं।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "What does unit 134 do?",
            ("It leads in to what follows", "भवन्ति चात्र: and on this there are (these)."),
            [("It closes the whole chapter", "The colophon comes in unit 138."),
             ("It names a new disease", "No disease is named here."),
             ("It gives a remedy for her", "No remedy is named here.")],
            "A standard lead-in formula: and on this matter there are these.",
            "भवन्ति चात्र = lead-in formula."),
        match(1, "Match each word of unit 134 to its meaning on the card.",
              [["भवन्ति", "there are"], ["च", "and"], ["अत्र", "here, in this matter"]],
              "Three words: there are, and, in this matter.",
              "भवन्ति, च, अत्र."),
        fill(2, "In unit 134 the word for here, in this matter is ____ (type it in Devanagari or in English letters, e.g. dharma).",
             accepts("अत्र"),
             "चात्र = च + अत्र; अत्र = here, in this matter.",
             "अत्र means here; in a text it means in this matter.",
             "अत्र = here."),
        mcq("discriminate", 3, "Which split of चात्र is right?",
            ("च + अत्र", "अ + अ → आ: च + अत्र → चात्र."),
            [("च + त्र", "That would be written चत्र, with no आ."),
             ("चा + त्र", "Neither चा nor त्र is the card's word."),
             ("चे + अत्र", "ए + अ would give चेऽत्र.")],
            "च (and) + अत्र (here).",
            "अ + अ → आ."),
        mcq("apply", 4, "What is भवन्ति, by the card's grammar?",
            ("Present, 3rd plural: there are", "3 pl. pres. √भू."),
            [("Present, 3rd singular: there is", "That would be भवति."),
             ("Future, 3rd plural: there will be", "That would be भविष्यन्ति."),
             ("Optative, 3rd plural: there should be", "That would be भवेयुः.")],
            "भवन्ति is the present third plural of √भू.",
            "-अन्ति = 3rd pl. present."),
        T(mcq("transfer", 5, "By the rule of च + अत्र → चात्र, how is न + अस्ति written when joined?",
              ("नास्ति", "अ + अ → आ: न + अस्ति → नास्ति."),
              [("नस्ति", "The two अ do not lose a vowel; they merge into आ."),
               ("नेस्ति", "अ + अ does not give ए."),
               ("नोस्ति", "अ + अ does not give ओ.")],
              "च + अत्र → चात्र; so न + अस्ति → नास्ति.",
              "अ + अ → आ."),
          "A final अ and an initial अ merge into one long आ: चात्र, नास्ति."),
    ],
}

# ---------------------------------------------------------------- unit 135
AUTHORED["135"] = {
    "title": "इत्यनात्ययिके व्याधौ",
    "question": "How does verse 135 set the rule for a non-critical disease against that for a very severe one?",
    "rule": ("Thus the rule in a non-critical (anātyayika) disease; but in a very severe one, even with sharp "
             "applications of treatment (kriyāyoga), one should carefully protect the woman."),
    "limits": ("No copula is printed after विधिः and none is supplied. इति (thus) closes what was said before; the verse "
               "does not restate it. The sharp treatments are not named, and no dose or advice is added. The two lines appear to pair as one verse (not stated by "
               "the print)."),
    "explain_hi": ("यह श्लोक दो स्थितियों को अलग करता है। अनात्ययिक (जो गम्भीर या आपात न हो) रोग में ‘इति विधिः’: यही विधि है, "
                   "जो अब तक कही गई। किन्तु अत्यधिक (बहुत बढ़े) रोग में तीक्ष्ण क्रियायोगों (तेज़ उपचार-प्रयोगों) से भी "
                   "स्त्री की यत्न से रक्षा करे। तीक्ष्ण उपचारों के नाम नहीं दिए गए। "
                   "‘अनात्ययिक’ में अन्- निषेध है, जो स्वर से पहले आता है।"),
    "hook": "साधारण रोग: वही विधि · बहुत बढ़ा रोग: तीक्ष्ण भी, पर स्त्री की यत्न से रक्षा।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By verse 135, what may be used in a very severe (अत्यधिक) disease?",
            ("Even sharp applications of treatment", "तीक्ष्णैरपि क्रियायोगैः."),
            [("Only mild and sweet foods", "For a very severe disease the verse names even sharp means."),
             ("Nothing; the disease is left alone", "The verse says to protect her even with sharp means."),
             ("Only fasting for some days at home", "Fasting is not named in this verse.")],
            "In a very severe disease even sharp treatments are used, protecting the woman with care.",
            "अत्यधिके … तीक्ष्णैरपि क्रियायोगैः."),
        order(1, "Put the four printed quarters of verse 135 in their order.",
              ["इत्यनात्ययिके व्याधौ", "विधिरत्यधिके पुनः", "तीक्ष्णैरपि क्रियायोगैः", "स्त्रियंयत्नेन पालयेत्"],
              "Thus in a non-critical disease, the rule; in a very severe one again, even with sharp treatments, "
              "protect the woman with care.",
              "इत्यनात्ययिके → विधिरत्यधिके → तीक्ष्णैरपि → स्त्रियंयत्नेन."),
        T(match(2, "Match each word of verse 135 to its meaning on the card.",
                [["अनात्ययिक", "non-critical"], ["अत्यधिक", "very severe"], ["तीक्ष्ण", "sharp, strong"],
                 ["क्रियायोग", "application of treatment"], ["यत्नेन", "with care"], ["पालयेत्", "should protect"]],
                "Two words name the two kinds of disease; the rest give the treatment and the care.",
                "अनात्ययिक, अत्यधिक, तीक्ष्ण, क्रियायोग, यत्नेन, पालयेत्.", role="extend"),
          "अनात्ययिक (non-critical) and अत्यधिक (very severe) are the two cases the verse sets apart."),
        mcq("discriminate", 3, "Which split of विधिरत्यधिके is right?",
            ("विधिः + अत्यधिके", "इः before a vowel becomes इर्: विधिरत्यधिके."),
            [("विधी + अत्यधिके", "ई + अ would join as विध्यत्यधिके."),
             ("विधिम् + अत्यधिके", "That would join as विधिमत्यधिके."),
             ("विधि + रत्यधिके", "रत्यधिके is not a word.")],
            "विधिः (rule, nom. sg.) + अत्यधिके (in a very severe one).",
            "Visarga after इ becomes र् before a vowel."),
        mcq("apply", 4, "Which pairing is right by verse 135?",
            ("Non-critical: the rule given; very severe: even sharp means",
             "इति अनात्ययिके विधिः; अत्यधिके पुनः तीक्ष्णैरपि."),
            [("Non-critical: even sharp means; very severe: the rule given", "This swaps the two cases."),
             ("Both cases: only sharp means at once", "The non-critical case keeps the rule given."),
             ("Both cases: no treatment, only waiting", "Treatment is named for both cases.")],
            "The verse sets the non-critical case (the rule already given) against the very severe case (even sharp means).",
            "अनात्ययिक ↔ अत्यधिक."),
        T(mcq("transfer", 5, "Built like अनात्ययिक (अन् + आत्ययिक), which invented word means without end?",
              ("अनन्त", "अन् + अन्त: before a vowel the negative is अन्-."),
              [("अअन्त", "Before a vowel the negative is अन्-, not अ-."),
               ("नन्त", "The negative prefix keeps its अ."),
               ("अन्त", "That is end itself, with no negation.")],
              "अन् + आत्ययिक → अनात्ययिक; अन् + अन्त → अनन्त.",
              "Negative अ- before a consonant, अन्- before a vowel."),
          "The negative prefix is अ- before a consonant and अन्- before a vowel: अनात्ययिक, अनन्त."),
    ],
}

# ---------------------------------------------------------------- unit 136
AUTHORED["136"] = {
    "title": "स्त्री हि मूलमपत्यानाम्",
    "question": "What does verse 136 say of woman, and what of the householder's state?",
    "rule": ("For woman is the root of offspring; for woman, when protected, protects. Of all the āśramas (stages of "
             "life), the householder's state is first and blameless."),
    "limits": ("The object of रक्षति (protects) is not printed and is not supplied. प्रथमम् may also be read as an "
               "adverb; the sense stays the same. Line 2 is not further explained here. The two lines appear to pair as "
               "one verse (not stated by the print)."),
    "explain_hi": ("‘हि’ (क्योंकि) से यह श्लोक पहले कही बात का कारण देता प्रतीत होता है: स्त्री ही सन्तानों की जड़ है; स्त्री ही, रक्षित होने पर, रक्षा करती है। "
                   "किसकी रक्षा करती है, यह छपा नहीं। "
                   "दूसरी पंक्ति कहती है: सब आश्रमों में गृहस्थपन प्रथम और अनिन्दित (निन्दारहित) है; इसे यहाँ आगे नहीं समझाया गया। "
                   "‘हि’ का अर्थ है ‘क्योंकि, ही’।"),
    "hook": "स्त्री: सन्तान की जड़ · रक्षित हो तो रक्षक · गृहस्थ: पहला, अनिन्दित।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By verse 136, of what is woman the root (मूल)?",
            ("Of offspring", "मूलम् अपत्यानाम्: root of offspring."),
            [("Of all disease", "The verse says offspring, not disease."),
             ("Of the wealth", "Wealth is not named."),
             ("Of the doṣas", "The doṣas are not named.")],
            "Woman is the root of offspring.",
            "अपत्य = offspring."),
        order(1, "Put the four printed quarters of verse 136 in their order.",
              ["स्त्री हि मूलमपत्यानां", "स्त्री हि रक्षति रक्षिता", "सर्वाश्रमाणां प्रथमं", "गृहस्थत्वमनिंदितं"],
              "Root of offspring; protected, she protects; of all āśramas, first; the householder's state, blameless.",
              "मूलमपत्यानां → रक्षति रक्षिता → सर्वाश्रमाणां प्रथमं → गृहस्थत्वमनिंदितं."),
        T(match(2, "Match each word of verse 136 to its meaning on the card.",
                [["मूल", "root"], ["अपत्य", "offspring"], ["रक्षिता", "protected"], ["आश्रम", "stage of life"],
                 ["गृहस्थत्व", "householder's state"], ["अनिन्दित", "blameless"]],
                "Line 1 is about woman; line 2 about the āśramas and the householder.",
                "मूल, अपत्य, रक्षिता, आश्रम, गृहस्थत्व, अनिन्दित.", role="extend"),
          "अनिन्दित = अ (not) + निन्दित (blamed): blameless."),
        mcq("discriminate", 3, "Which split of गृहस्थत्वमनिंदितम् is right?",
            ("गृहस्थत्वम् + अनिन्दितम्", "म् joins the next vowel अ: blameless."),
            [("गृहस्थत्वम् + निन्दितम्", "Before न the म् would be an anusvara, गृहस्थत्वं निन्दितम्: no मनि."),
             ("गृहस्थत्वा + अनिन्दितम्", "आ + अ would join as गृहस्थत्वानिन्दितम्."),
             ("गृहस्थत्व + मनिन्दितम्", "मनिन्दितम् is not a word.")],
            "गृहस्थत्वम् (householder's state) + अनिन्दितम् (blameless).",
            "Final म् + vowel → म joins the vowel."),
        multi("apply", 4, "Which three does verse 136 state?",
              [("Woman is the root of disease", "The verse says root of offspring."),
               ("Woman is the root of offspring", "Right: स्त्री हि मूलमपत्यानाम्."),
               ("Woman, when protected, protects", "Right: स्त्री हि रक्षति रक्षिता."),
               ("The householder's state is first and blameless", "Right: प्रथमं गृहस्थत्वमनिन्दितम्.")],
              [1, 2, 3],
              "Root of offspring; protected, she protects; the householder's state first and blameless.",
              "मूलम् अपत्यानाम्; रक्षति रक्षिता; गृहस्थत्वम् अनिन्दितम्."),
        T(mcq("transfer", 5, "Built like अपत्यानाम् (of offspring), which is the genitive plural of फल (fruit)?",
              ("फलानाम्", "अ-stem + -आनाम्: of the fruits."),
              [("फलानि", "That is the nominative or accusative plural."),
               ("फलैः", "That is the instrumental plural."),
               ("फलेषु", "That is the locative plural.")],
              "अपत्य → अपत्यानाम्; फल → फलानाम्.",
              "अ-stem gen. pl. = -आनाम्."),
          "The genitive plural of an अ-stem ends in -आनाम् (-आणाम् after र or ष): अपत्यानाम्, आश्रमाणाम्."),
    ],
}

# ---------------------------------------------------------------- unit 137
AUTHORED["137"] = {
    "title": "जरायुणा मुखे छन्ने",
    "question": "Why, by verse 137, does the one in the womb not cry out?",
    "rule": ("When the mouth is covered by the jarāyu (fetal membrane) and the throat is wrapped in Kapha, and because "
             "the path of vāyu (wind) is obstructed, the one in the womb (garbhastha) does not cry out."),
    "limits": ("जरायु is the membrane enclosing the fetus; which membrane exactly is not said. वायु is read as wind or "
               "air, though the humour Vāta is not excluded; no question rests on that. The two lines appear to form "
               "one sentence (not stated by the print)."),
    "explain_hi": ("यह श्लोक बताता है कि गर्भ में रहने वाला (गर्भस्थ) क्यों नहीं रोता। तीन कारण हैं: "
                   "जरायु (गर्भ को ढकने वाली झिल्ली) से मुख ढका रहता है, कण्ठ कफ से लिपटा रहता है, और वायु का मार्ग रुका रहता है। "
                   "पहले दो सति-सप्तमी (‘… होने पर’) हैं, तीसरा पंचमी ‘निरोधात्’ (रुकने से)। "
                   "जरायु कौन-सी झिल्ली है, यह नहीं बताया; ‘वायु’ यहाँ हवा माना गया है।"),
    "hook": "मुख पर जरायु, कण्ठ में कफ, वायु-मार्ग बन्द: गर्भस्थ नहीं रोता।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By verse 137, what does the one in the womb not do?",
            ("It does not cry out", "न गर्भस्थः प्ररोदिति."),
            [("It does not move", "Movement is not spoken of here."),
             ("It does not grow", "Growth is not spoken of here."),
             ("It does not take food", "Food is not spoken of here.")],
            "The one in the womb does not cry out.",
            "प्ररोदिति = cries out."),
        order(1, "Put the four printed quarters of verse 137 in their order.",
              ["जरायुणा मुखे छन्ने", "कंठे चकफवेष्टिते", "वायोर्मार्गनिरोधाच्च", "न गर्भस्थः प्ररोदिति"],
              "Mouth covered by the jarāyu; throat wrapped in Kapha; path of vāyu blocked; so it does not cry.",
              "मुख → कण्ठ → वायु का मार्ग → न प्ररोदिति."),
        T(match(2, "Match each word of verse 137 to its meaning on the card.",
                [["जरायु", "fetal membrane (standard)"], ["छन्न", "covered"], ["वेष्टित", "wrapped, enveloped"],
                 ["निरोध", "obstruction"], ["गर्भस्थ", "the one in the womb"]],
                "Each of the three causes has a word for what is done: covered, wrapped, obstructed.",
                "जरायु, छन्न, वेष्टित, निरोध, गर्भस्थ.", role="extend"),
          "Three causes: mouth covered (छन्न), throat wrapped (वेष्टित), path obstructed (निरोध)."),
        mcq("discriminate", 3, "By verse 137, what covers the mouth?",
            ("The jarāyu (fetal membrane)", "जरायुणा मुखे छन्ने."),
            [("Kapha (the humour)", "Kapha wraps the throat, not the mouth."),
             ("Vāyu (wind or air)", "It is the path of vāyu that is blocked."),
             ("The mother's own abdomen", "No such covering is named.")],
            "The jarāyu covers the mouth; Kapha wraps the throat; the path of vāyu is blocked.",
            "मुख ← जरायु; कण्ठ ← कफ."),
        mcq("apply", 4, "Which English of कंठे चकफवेष्टिते is right?",
            ("And the throat being wrapped in Kapha", "कण्ठे (throat, loc.) च कफवेष्टिते."),
            [("And the mouth being wrapped in Kapha", "कण्ठ is the throat, not the mouth."),
             ("And the throat being free of Kapha", "वेष्टित means wrapped, not free."),
             ("And the throat being wrapped in jarāyu", "The throat is wrapped in Kapha, not the jarāyu.")],
            "Each wrong English changes one word: the organ, the state, or what wraps it.",
            "कण्ठ + कफवेष्टित."),
        T(mcq("transfer", 5, "By the rule of वायोः + मार्ग → वायोर्मार्ग, how is गुरोः + वचनम् written when joined?",
              ("गुरोर्वचनम्", "ओः before the voiced व becomes ओर्."),
              [("गुरो वचनम्", "Only अः and आः drop the visarga like this; after ओ it becomes र्."),
               ("गुरोस्वचनम्", "स् comes before त, not before व."),
               ("गुरोवचनम्", "The visarga does not simply vanish here.")],
              "वायोः + मार्ग → वायोर्मार्ग; so गुरोः + वचनम् → गुरोर्वचनम्.",
              "Visarga after a vowel other than अ/आ becomes र् before a voiced sound."),
          "A visarga after ओ (or any vowel but अ, आ) becomes र् before a voiced sound: वायोर्मार्ग, गुरोर्वचनम्."),
    ],
}

# ---------------------------------------------------------------- unit 138
AUTHORED["138"] = {
    "title": "इतिगर्भावक्रांतिर्नाम द्वितीयोऽध्यायः",
    "question": "What does the colophon in unit 138 name the chapter?",
    "rule": "Thus the second chapter, named Garbhāvakrānti (the descent of the embryo).",
    "limits": "A colophon: it names the chapter and its number, and teaches nothing else.",
    "explain_hi": ("यह अध्याय की समाप्ति-पंक्ति (पुष्पिका) है: इस प्रकार गर्भावक्रान्ति नाम का दूसरा अध्याय (पूरा हुआ)। "
                   "गर्भावक्रान्ति = गर्भ + अवक्रान्ति: गर्भ का अवतरण या प्रवेश। "
                   "छपे शब्द सन्धि से जुड़े हैं: गर्भावक्रान्तिः + नाम → गर्भावक्रान्तिर्नाम, द्वितीयः + अध्यायः → द्वितीयोऽध्यायः।"),
    "hook": "शारीर का दूसरा अध्याय: गर्भावक्रान्ति।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 138, what is chapter two named?",
            ("गर्भावक्रान्ति", "इति गर्भावक्रान्तिर्नाम द्वितीयोऽध्यायः."),
            [("दिनचर्याध्याय", "That name is not printed here."),
             ("ऋतुचर्याविधि", "That name is not printed here."),
             ("रोगनिदानविधि", "That name is not printed here.")],
            "The colophon names the chapter गर्भावक्रान्ति, the descent of the embryo.",
            "गर्भावक्रान्ति = descent of the embryo."),
        order(1, "Put the words of unit 138 in their order.",
              ["इति", "गर्भावक्रान्तिः", "नाम", "द्वितीयः", "अध्यायः"],
              "Thus, Garbhāvakrānti, named, second, chapter.",
              "इति → गर्भावक्रान्तिः → नाम → द्वितीयः → अध्यायः."),
        T(match(2, "Match each word of unit 138 to its meaning on the card.",
                [["इति", "thus (closing)"], ["नाम", "named"], ["द्वितीय", "second"], ["अध्याय", "chapter"],
                 ["अवक्रान्ति", "descent, entry"]],
                "A colophon: thus, the chapter named X, second.",
                "इति, नाम, द्वितीय, अध्याय, अवक्रान्ति.", role="extend"),
          "A colophon opens with इति and gives the chapter's name (X नाम) and number."),
        mcq("discriminate", 3, "Which split of द्वितीयोऽध्यायः is right?",
            ("द्वितीयः + अध्यायः", "अः before अ gives ओ and the अ is shown by ऽ."),
            [("द्वितीया + अध्यायः", "आ + अ would join as द्वितीयाध्यायः."),
             ("द्वितीये + अध्यायः", "ए + अ would give द्वितीयेऽध्यायः, with ए."),
             ("द्वितीयो + ध्यायः", "ध्यायः is not the card's word.")],
            "द्वितीयः (second) + अध्यायः (chapter): अः + अ → ओऽ.",
            "अः + अ → ओ + ऽ."),
        fill(4, "In unit 138 the word for chapter is ____ (type it in Devanagari or in English letters, e.g. dharma).",
             accepts("अध्यायः", None, "अध्याय", "adhyayah", "adhyaya"),
             "अध्यायः = chapter; with द्वितीयः it is printed द्वितीयोऽध्यायः.",
             "अध्याय means chapter; ऽ shows its lost अ after द्वितीयो.",
             "अध्याय = chapter.", role="apply"),
        T(mcq("transfer", 5, "By the rule of द्वितीयोऽध्यायः, how is रामः + अपि written when joined?",
              ("रामोऽपि", "अः + अ → ओऽ: रामोऽपि."),
              [("रामापि", "अः + अ does not give आ."),
               ("रामरपि", "र् does not come after अ here."),
               ("रामेऽपि", "अः + अ does not give ए.")],
              "द्वितीयः + अध्यायः → द्वितीयोऽध्यायः; so रामः + अपि → रामोऽपि.",
              "अः + अ → ओ + ऽ."),
          "अः before अ becomes ओ and the following अ is shown by ऽ: द्वितीयोऽध्यायः, रामोऽपि."),
    ],
}

# ===================================================================== NOTES_HI
NOTES_HI = {
    "126": ("विश्वास मध्यम; गद्य, एक छपी पंक्ति (02.02.135)। पाठ-चिह्न (सम्भावित): छपा ‘तत्तदासेवमानांऽतर्वत्नी’; "
            "‘आसेवमानां’ (द्वितीया) प्रथमा ‘स्त्री/अन्तर्वत्नी’ से मेल नहीं खाता, अनुस्वार सम्भवतः छपाई की भूल है; "
            "अर्थ ‘आसेवमाना अन्तर्वत्नी’ लिया गया, अवग्रह ‘अ’ के स्थान पर छपा है। ‘निदान’ = रोग का कारण (मानक)। "
            "सन्धियाँ जाँचीं: यत् + च → यच्च (त् + च → च्च); व्याधेः + निदानम् → व्याधेर्निदानम्; "
            "तत्-तद्-विकार (त् → द् घोष व से पहले); बहुलम् + अपत्यम् → बहुलमपत्यम्।"),
    "127": ("विश्वास उच्च, कोई पाठ-चिह्न नहीं; गद्य, दो छपी पंक्तियाँ (02.02.136, 02.02.137)। ‘एतेन’ पिछले माता-आचरण के वर्णन की ओर है। "
            "‘दोष’ = त्रुटि, वात आदि दोष नहीं। द्विवचन कर्ता ‘दोनों’ (प्रसंग से दम्पती) छपा नहीं। ‘आत्मानम्’ एकवचन (प्रत्येक का अपना आप)। "
            "सन्धियाँ जाँचीं: पितृजाः + अपि → पितृजा अपि; शुक्रदोषाः + व्याख्याताः → शुक्रदोषा व्याख्याताः (आः के बाद विसर्ग-लोप); "
            "सम्पदम् + इच्छन्तौ → सम्पदमिच्छन्तौ; साधु + आत्मानम् → साध्वात्मानम् (उ + आ → वा); आत्मानम् + उपाचरेताम् → आत्मानमुपाचरेताम्।"),
    "128": ("विश्वास उच्च, कोई पाठ-चिह्न नहीं; गद्य (02.02.138)। अधूरा वाक्य: इकाई १२७ की ‘उपाचरेताम्’ या वैसी क्रिया समझी गई, जोड़ी नहीं गई। "
            "आँकड़ों के अनुसार यह इकाई १२७ से आगे चलती प्रतीत होती है। ‘विशेषेण’ तृतीया एकवचन, अव्यय की तरह (ष के बाद न → ण)।"),
    "129": ("विश्वास उच्च; गद्य (02.02.139)। पाठ-चिह्न (निश्चित): ‘विहारैरूपाचरेत्’ का दीर्घ ऊ छपाई की भूल है; उपसर्ग उप-आ-√चर्, "
            "पाठ ‘विहारैरुपाचरेत्’। चारों गुण तीनों साधनों के विशेषण माने गए। विहार = दिनचर्या, आचरण। "
            "सन्धियाँ जाँचीं: व्याधीन् + च → व्याधींश्च; च + अस्याः → चास्याः; अस्याः + मृदु → अस्या मृदु (आः के बाद विसर्ग-लोप); "
            "सुखैः + औषध → सुखैरौषध; औषध + आहार → औषधाहार।"),
    "130": ("विश्वास उच्च, कोई पाठ-चिह्न नहीं; गद्य (02.02.140)। वमन = चिकित्सा हेतु उल्टी कराना; ‘आदि’ के बाकी शोधन-कर्म यहाँ नहीं गिनाए। "
            "‘अस्याः’ षष्ठी, ‘इसके लिए’ अर्थ में। सन्धियाँ जाँचीं: च + अस्याः → चास्याः; अस्याः + वमन → अस्या वमन; वमन + आदीनि → वमनादीनि।"),
    "131": ("विश्वास मध्यम; गद्य (02.02.141)। पाठ-चिह्न (सम्भावित): छपा ‘रक्त्तावसेचनं’ का दोहरा त्त ‘रक्त-अवसेचन’ की वर्तनी नहीं; "
            "सम्भवतः ‘रक्तावसेचनं’ (छपाई की भूल)। क्रिया नहीं छपी; इकाई १३० की ‘प्रयोजयेत्’ समझी गई। "
            "पाठ यह तय नहीं करता कि बस्तियाँ निषेध का अपवाद हैं या निषेध ही जारी है; शाब्दिक क्रम रखा गया। "
            "आस्थापन = काढ़े की बस्ति, अनुवासन = तेल की बस्ति (मानक)। सन्धियाँ जाँचीं: तु + अष्टमम् → त्वष्टमम्; "
            "मासम् + उपादाय → मासमुपादाय; उपादाय + आस्थापनम् → उपादायास्थापनम्; आस्थापनम् + अनुवासनम् → आस्थापनमनुवासनम्।"),
    "132": ("विश्वास उच्च, कोई पाठ-चिह्न नहीं; गद्य (02.02.142)। साधनों के नाम नहीं दिए; ‘मृदु (साधनों)’ कोष्ठक में। "
            "उपक्रम = उपचार का आरम्भ। सन्धियाँ जाँचीं: पुनः + विकारेषु → पुनर्विकारेषु; मृदुभिः + तद् → मृदुभिस्तद्; "
            "तत् + अर्थ → तदर्थ; कारिभिः + वा → कारिभिर्वा; वा + उपक्रमेत् → वोपक्रमेत् (आ + उ → ओ)।"),
    "133": ("विश्वास उच्च; गद्य (02.02.143)। पाठ-चिह्न (सम्भावित): ‘असंक्षोभयन्द्गर्भिणीम्’ में ‘गर्भिणीम्’ से पहले छपा द् अतिरिक्त लगता है "
            "(असंक्षोभयन् + गर्भिणीम्)। ‘असंक्षोभयन्’ का कर्म छपा नहीं (उसे, या उपमा से पात्र)। अन्त का ‘इति’ गद्य-भाग समाप्त करता है। "
            "सन्धियाँ जाँचीं: पूर्णम् + इव → पूर्णमिव; तैलपात्रम् + असंक्षोभयन् → तैलपात्रमसंक्षोभयन्; गर्भिणीम् + उपाचरेत् → "
            "गर्भिणीमुपाचरेत्; उपाचरेत् + इति → उपाचरेदिति।"),
    "134": ("विश्वास उच्च, कोई पाठ-चिह्न नहीं; गद्य (02.02.144)। परिचित भूमिका-सूत्र; संज्ञा (क्या हैं) छपी नहीं, जोड़ी नहीं गई। "
            "आगे के श्लोकों (इकाई १३५ से) का परिचय। छपा ‘भवंति’ = भवन्ति (अनुस्वार न् के स्थान पर)। सन्धि जाँची: च + अत्र → चात्र।"),
    "135": ("विश्वास उच्च, कोई पाठ-चिह्न नहीं; श्लोक, दो पंक्तियाँ (02.02.145, 02.02.146), जो एक श्लोक लगती हैं (छपाई यह नहीं कहती)। "
            "‘विधिः’ के बाद क्रिया नहीं; ‘अत्यधिके’ के साथ ‘व्याधौ’ समझा गया। तीक्ष्ण = तेज़, तीव्र, कठोर। "
            "सन्धियाँ जाँचीं: इति + अनात्ययिके → इत्यनात्ययिके (इ + अ → य); विधिः + अत्यधिके → विधिरत्यधिके; "
            "तीक्ष्णैः + अपि → तीक्ष्णैरपि; स्त्रियम् + यत्नेन → स्त्रियं यत्नेन (छपाई में बिना दूरी ‘स्त्रियंयत्नेन’)।"),
    "136": ("विश्वास उच्च, कोई पाठ-चिह्न नहीं; श्लोक, दो पंक्तियाँ (02.02.147, 02.02.148), जो एक श्लोक लगती हैं (छपाई यह नहीं कहती)। "
            "‘रक्षति’ का कर्म छपा नहीं, जोड़ा नहीं। ‘प्रथमम्’ क्रियाविशेषण (पहले) भी हो सकता है; अर्थ वही रहता है। दूसरी पंक्ति यहाँ आगे नहीं समझाई गई। "
            "सन्धियाँ जाँचीं: मूलम् + अपत्यानाम् → मूलमपत्यानाम्; सर्व + आश्रमाणाम् → सर्वाश्रमाणाम्; गृहस्थत्वम् + अनिन्दितम् → गृहस्थत्वमनिन्दितम्।"),
    "137": ("विश्वास उच्च, कोई पाठ-चिह्न नहीं; श्लोक, दो पंक्तियाँ (02.02.149, 02.02.150), एक वाक्य (छपाई यह नहीं कहती)। "
            "दो सति-सप्तमी (मुखे छन्ने, कण्ठे कफवेष्टिते) और एक पंचमी (निरोधात्)। जरायु = गर्भ को घेरने वाली झिल्ली (मानक); "
            "कौन-सी (एम्नियन या कोरियन), यह नहीं कहा। ‘वायु’ = हवा माना, वात-दोष भी अस्वीकार नहीं। "
            "सन्धियाँ जाँचीं: कण्ठे + च (छपा ‘कंठे चकफवेष्टिते’, च और कफवेष्टिते बिना दूरी); वायोः + मार्ग → वायोर्मार्ग; "
            "निरोधात् + च → निरोधाच्च; गर्भस्थः + प्ररोदिति (प से पहले विसर्ग बना रहता है)।"),
    "138": ("विश्वास उच्च, कोई पाठ-चिह्न नहीं; गद्य, पुष्पिका (02.02.151)। "
            "सन्धियाँ जाँचीं: गर्भ + अवक्रान्ति → गर्भावक्रान्ति; गर्भावक्रान्तिः + नाम → गर्भावक्रान्तिर्नाम; "
            "द्वितीयः + अध्यायः → द्वितीयोऽध्यायः (अः + अ → ओऽ)। छपाई में ‘इति’ अगले शब्द से जुड़ा है।"),
}

# ===================================================================== AIDS
AIDS = {
    "126": {
        "chain": {"steps": ["जिस-जिस रोग का जो निदान", "गर्भिणी उस-उसका सेवन करती", "सन्तान उन-उन विकारों से भरपूर"]},
        "frame": "यच्च यच्च … यस्य (जो-जो, जिसका) → तत्तत् (वह-वह) → तत्तद्विकारबहुलम् अपत्यम् जनयति।",
        "sandhi": ("त् + च → च्च: यत् + च → यच्च · एः + घोष → एर्: व्याधेः + निदानम् → व्याधेर्निदानम् · "
                   "त् + घोष व → द्व: तत् + विकार → तद्विकार।"),
        "chunks": "यच्च यच्च | यस्य व्याधेर्निदानं | तत्तदासेवमानांऽतर्वत्नी स्त्री | तत्तद्विकारबहुलमपत्यं | जनयति",
    },
    "127": {
        "frame": "एतेन (माता के वर्णन से) → पितृज शुक्रदोष भी व्याख्यात → तस्मात् (इसलिए) → दोनों साधु आत्मानम् उपाचरेताम्।",
        "sandhi": ("आः + स्वर/घोष → आ: पितृजाः + अपि → पितृजा अपि · उ + आ → वा: साधु + आत्मानम् → साध्वात्मानम् · "
                   "म् + स्वर: सम्पदम् + इच्छन्तौ → सम्पदमिच्छन्तौ।"),
        "anchors": "मेरी याद-पद्धति: ‘-औ, -एताम्’ = दो जन: इच्छन्तौ (दो चाहने वाले), उपाचरेताम् (दोनों देखभाल करें)।",
    },
    "128": {
        "frame": "विशेषेण (विशेष रूप से) → नारी (स्त्री) → (क्रिया इकाई १२७ जैसी, समझी गई)।",
        "puns": "मेरी बनाई, केवल सुनने की सहायता: ‘विशेष-एण’: दोनों में विशेष, नारी।",
        "anchors": "मेरी याद-पद्धति: १२७ में ‘दोनों’, १२८ में ‘विशेषकर नारी’।",
    },
    "129": {
        "diagram": {"groups": [
            {"label": "गुण (छपे क्रम में)", "items": ["मृदु", "मधुर", "शिशिर", "सुख"]},
            {"label": "साधन (छपे क्रम में)", "items": ["औषध", "आहार", "विहार"]}]},
        "sandhi": ("न् + च → ंश्च: व्याधीन् + च → व्याधींश्च · ऐः + स्वर → ऐर्: सुखैः + औषध → सुखैरौषध · "
                   "अ + आ → आ: औषध + आहार → औषधाहार।"),
        "letters": "गुणों के आदि-अक्षर, छपे क्रम में: मृ-म-शि-सु · साधनों के: औ-आ-वि।",
        "contrast": "इसी पंक्ति में: चार गुण (मृदु, मधुर, शिशिर, सुख) ↔ तीन साधन (औषध, आहार, विहार): गुण विशेषण हैं, साधन विशेष्य।",
    },
    "130": {
        "frame": "न (नहीं) → च अस्याः (और इसके लिए) → वमनादीनि (वमन आदि) → प्रयोजयेत् (प्रयोग करे)।",
        "sandhi": "अ + अ → आ: च + अस्याः → चास्याः · आः + घोष → आ: अस्याः + वमन → अस्या वमन · अ + आ → आ: वमन + आदीनि → वमनादीनि।",
        "anchors": "मेरी याद-पद्धति: १२९ ‘करो: मृदु उपचार’ → १३० ‘न करो: वमन आदि’।",
    },
    "131": {
        "frame": ("न रक्त्तावसेचनम् (रक्त निकालना नहीं; छपा पाठ संदिग्ध) → केवलं तु (किन्तु केवल) → अष्टमं मासमुपादाय "
                  "(आठवें मास से) → आस्थापनम् अनुवासनं वा (क्रिया इकाई १३० से समझी गई)।"),
        "sandhi": ("उ + अ → व: तु + अष्टमम् → त्वष्टमम् · आ + आ → आ: उपादाय + आस्थापनम् → उपादायास्थापनम् · "
                   "म् + स्वर: मासम् + उपादाय → मासमुपादाय।"),
        "chunks": "न रक्त्तावसेचनं | केवलं त्वष्टमं | मासमुपादाय | आस्थापनम् | अनुवासनं वा",
    },
    "132": {
        "chain": {"steps": ["वमन आदि से साध्य विकार", "मृदु (साधनों) से", "या तदर्थकारी (वही काम करने वालों) से", "उपक्रम करे"]},
        "sandhi": ("आ + उ → ओ: वा + उपक्रमेत् → वोपक्रमेत् · विसर्ग + त → स्त: मृदुभिः + तद् → मृदुभिस्तद् · "
                   "इः + घोष → इर्: कारिभिः + वा → कारिभिर्वा।"),
        "frame": "वमनादिसाध्येषु पुनः विकारेषु (पर वमन-साध्य रोगों में) → मृदुभिः तदर्थकारिभिः वा (मृदु या वही काम करने वालों से) → उपक्रमेत्।",
    },
    "133": {
        "diagram": {"groups": [
            {"label": "उपमा", "items": ["पूर्ण तैलपात्र"]},
            {"label": "विषय", "items": ["गर्भिणी"]},
            {"label": "ढंग", "items": ["असंक्षोभयन् (बिना हिलाए)"]},
            {"label": "क्रिया", "items": ["उपाचरेत् (सेवा करे)"]}]},
        "sandhi": "त् + स्वर → द्: उपाचरेत् + इति → उपाचरेदिति · म् + स्वर: पूर्णम् + इव → पूर्णमिव, गर्भिणीम् + उपाचरेत् → गर्भिणीमुपाचरेत्।",
        "story": "मेरा बनाया चित्र: कोई तेल से लबालब कटोरा लेकर चल रहा है, एक बूँद न छलके; वैसे ही गर्भिणी की सेवा, बिना झटके।",
    },
    "134": {
        "frame": "भवन्ति (हैं) → च (और) → अत्र (इस विषय में) → (क्या हैं, छपा नहीं; आगे श्लोक)।",
        "sandhi": "अ + अ → आ: च + अत्र → चात्र · छपा ‘भवंति’ = भवन्ति।",
    },
    "135": {
        "contrast": {"groups": [
            {"label": "अनात्ययिक रोग में", "items": ["इति विधिः: यही विधि (जो कही गई)"]},
            {"label": "अत्यधिक रोग में", "items": ["तीक्ष्ण क्रियायोग भी", "स्त्री की यत्न से रक्षा"]}]},
        "sandhi": ("इ + अ → य: इति + अनात्ययिके → इत्यनात्ययिके · इः + स्वर → इर्: विधिः + अत्यधिके → विधिरत्यधिके · "
                   "ऐः + स्वर → ऐर्: तीक्ष्णैः + अपि → तीक्ष्णैरपि।"),
        "seesaw": "अनात्ययिक (गम्भीर नहीं) ↔ अत्यधिक (बहुत बढ़ा): दोनों इसी श्लोक में, ‘पुनः’ से अलग।",
        "chunks": "इत्यनात्ययिके व्याधौ | विधिरत्यधिके पुनः | तीक्ष्णैरपि क्रियायोगैः | स्त्रियंयत्नेन पालयेत्",
    },
    "136": {
        "diagram": {"groups": [
            {"label": "पंक्ति १: स्त्री", "items": ["मूलम् अपत्यानाम् (सन्तान की जड़)", "रक्षति रक्षिता (रक्षित हो तो रक्षा करती)"]},
            {"label": "पंक्ति २: आश्रम", "items": ["सर्वाश्रमाणां प्रथमम् (सब आश्रमों में प्रथम)", "गृहस्थत्वम् अनिन्दितम् (गृहस्थपन निन्दारहित)"]}]},
        "sandhi": ("म् + स्वर: मूलम् + अपत्यानाम् → मूलमपत्यानाम्, गृहस्थत्वम् + अनिन्दितम् → गृहस्थत्वमनिन्दितम् · "
                   "अ + आ → आ: सर्व + आश्रमाणाम् → सर्वाश्रमाणाम्।"),
        "puns": "मेरी बनाई, केवल सुनने की सहायता: ‘रक्षति रक्षिता’: जो रक्षित, वही रक्षक।",
        "chunks": "स्त्री हि मूलमपत्यानां | स्त्री हि रक्षति रक्षिता | सर्वाश्रमाणां प्रथमं | गृहस्थत्वमनिंदितं",
    },
    "137": {
        "chain": {"steps": ["जरायु से मुख ढका", "कफ से कण्ठ लिपटा", "वायु का मार्ग रुका", "गर्भस्थ नहीं रोता"]},
        "sandhi": ("ओः + घोष → ओर्: वायोः + मार्ग → वायोर्मार्ग · त् + च → च्च: निरोधात् + च → निरोधाच्च।"),
        "letters": "तीन कारण, छपे क्रम में: मु-कं-वा (मुख, कण्ठ, वायु-मार्ग)।",
        "frame": "मुखे छन्ने, कण्ठे कफवेष्टिते (… होने पर) + मार्गनिरोधात् (रुकने से) → न प्ररोदिति।",
    },
    "138": {
        "frame": "इति (इस प्रकार) → गर्भावक्रान्तिः नाम (गर्भावक्रान्ति नामक) → द्वितीयः अध्यायः (दूसरा अध्याय)।",
        "sandhi": ("अः + अ → ओऽ: द्वितीयः + अध्यायः → द्वितीयोऽध्यायः · इः + घोष → इर्: गर्भावक्रान्तिः + नाम → "
                   "गर्भावक्रान्तिर्नाम · अ + अ → आ: गर्भ + अवक्रान्ति → गर्भावक्रान्ति।"),
    },
}

# ===================================================================== IMAGE_SPECS
IMAGE_SPECS = {
    ("126", "chain"): {
        "file": "sh2-nidana-santana-126.svg",
        "alt": ("Chain of unit 126 in three steps: whatever is the cause of whatever disease; the pregnant woman "
                "indulges in each of those; she bears offspring abounding in the corresponding disorders."),
        "type": "chain",
        "title": "इकाई १२६: निदान-सेवन से सन्तान में विकार",
        "steps": ["जिस-जिस रोग का जो निदान", "गर्भिणी उस-उसका सेवन करती", "सन्तान उन-उन विकारों से भरपूर"],
    },
    ("129", "diagram"): {
        "file": "sh2-mridu-upachara-129.svg",
        "alt": ("Two columns for unit 129 in printed order: four qualities (mild, sweet, cool, pleasant) and three means "
                "(medicines, foods, regimens) with which her diseases are treated."),
        "type": "split",
        "title": "गर्भिणी के रोगों का उपचार (इकाई १२९)",
        "cols": [["चार गुण", ["मृदु", "मधुर", "शिशिर (शीतल)", "सुख (सुखकर)"]],
                 ["तीन साधन", ["औषध", "आहार", "विहार (दिनचर्या)"]]],
    },
    ("133", "diagram"): {
        "file": "sh2-tailapatra-133.svg",
        "alt": ("Table of unit 133's simile: the compared thing is a full vessel of oil; the subject is the pregnant "
                "woman; the manner is without shaking; the act is to attend to her."),
        "type": "table",
        "title": "पूर्ण तैलपात्र की उपमा (इकाई १३३)",
        "heads": ["अंग", "छपा शब्द और अर्थ"],
        "rows": [["उपमा", "पूर्णम् इव तैलपात्रम्: भरे तेल-पात्र की तरह"], ["विषय", "गर्भिणीम्: गर्भिणी को"],
                 ["ढंग", "असंक्षोभयन्: बिना हिलाए"], ["क्रिया", "उपाचरेत्: सेवा करे"]],
    },
    ("135", "contrast"): {
        "file": "sh2-atyayika-135.svg",
        "alt": ("Two columns for verse 135: in a non-critical disease, the rule already given; in a very severe disease, "
                "even sharp applications of treatment, protecting the woman with care."),
        "type": "split",
        "title": "दो स्थितियाँ (श्लोक १३५)",
        "cols": [["अनात्ययिक रोग में", ["इति विधिः: यही विधि"]],
                 ["अत्यधिक रोग में", ["तीक्ष्ण क्रियायोग भी", "स्त्री की यत्न से रक्षा"]]],
    },
    ("136", "diagram"): {
        "file": "sh2-stri-mula-136.svg",
        "alt": ("Numbered table of verse 136's four quarters in printed order: woman the root of offspring; protected, "
                "she protects; of all stages of life, first; the householder's state, blameless."),
        "type": "table",
        "title": "श्लोक १३६: चारों चरण क्रम से",
        "heads": ["छपा चरण", "अर्थ"],
        "rows": [["१. स्त्री हि मूलमपत्यानां", "स्त्री ही सन्तान की जड़"], ["२. स्त्री हि रक्षति रक्षिता", "रक्षित हो तो रक्षा करती"],
                 ["३. सर्वाश्रमाणां प्रथमं", "सब आश्रमों में प्रथम"], ["४. गृहस्थत्वमनिंदितं", "गृहस्थपन निन्दारहित"]],
    },
    ("137", "chain"): {
        "file": "sh2-garbhastha-rodana-137.svg",
        "alt": ("Flowchart of verse 137: three causes (mouth covered by the jarayu, throat wrapped in Kapha, path of vayu "
                "obstructed) all lead to one result: the one in the womb does not cry out."),
        "type": "mermaid",
        "code": ("flowchart TD\n"
                 "  A[\"१. जरायु से मुख ढका\"] --> D[\"गर्भस्थ नहीं रोता\"]\n"
                 "  B[\"२. कफ से कण्ठ लिपटा\"] --> D\n"
                 "  C[\"३. वायु का मार्ग रुका\"] --> D\n"),
    },
}
