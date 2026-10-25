from helpers import mcq, match, order, fill, multi, accepts


AUTHORED = {}

# ---------------------------------------------------------------- unit 64
AUTHORED["64"] = {
    "title": "तेषु प्रतिबद्धानि कोष्ठांगानि",
    "question": "By unit 64, which organs of the koṣṭha are bound in the seats?",
    "rule": ("In these (the seats, āśaya, of units 62-63) are bound the koṣṭhāṅgas, members of the koṣṭha (trunk): "
             "heart, liver, spleen, lung, unduka, kidney, intestine and so on."),
    "limits": ("Prose. The list ends in 'and so on' (आदि), so it is open. unduka = caecum is probable only (debated). "
               "The printed वक्क is possibly वृक्क (kidney), a flagged reading: no question on it. Which organ lies in "
               "which seat is not said."),
    "explain_hi": ("यह गद्य-पंक्ति बताती है कि उन आशयों में (इकाई ६२-६३) कोष्ठ के अंग बँधे हुए हैं। "
                   "कोष्ठ यानी धड़ या पेट का भीतरी भाग, और कोष्ठांग यानी उसके अंग। "
                   "सूची है: हृदय, यकृत् (जिगर), प्लीहा (तिल्ली), फुप्फुस (फेफड़ा), उण्डुक (सम्भवतः अन्धान्त्र), वक्क (सम्भवतः वृक्क, गुर्दा), "
                   "अन्त्र (आँत) आदि। "
                   "छपा ‘वक्क’ सम्भवतः ‘वृक्क’ है; यह सुधार सम्भावित ही है। "
                   "‘आदि’ से सूची खुली रहती है, और कौन-सा अंग किस आशय में है, यह नहीं कहा गया।"),
    "hook": "आशयों में बँधे कोष्ठांग: हृदय से अन्त्र तक।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 64, what are the organs bound in the seats called?",
            ("Members of the koṣṭha (koṣṭhāṅga)", "कोष्ठांगानि: the members of the koṣṭha, the trunk."),
            [("Organs of action (karmendriya)", "The organs of action are speech, anus, genital, hand and foot (unit 58)."),
             ("Seats of the sense-organs (adhiṣṭhāna)", "The seats of the senses are ears, skin, eyes, tongue, nostrils (unit 58)."),
             ("Membranes of the body (kalā)", "The seven kalās are another topic (from unit 46).")],
            "The organs bound in the seats are the koṣṭhāṅgas, members of the trunk.",
            "तेषु प्रतिबद्धानि कोष्ठांगानि."),
        order(1, "Put these organs of unit 64 in the line's order (the flagged वक्क is left out).",
              ["हृदय", "यकृत्", "प्लीह", "फुप्फुस", "उंदुक", "अंत्र"],
              "Heart, liver, spleen, lung, unduka, (kidney), intestine, and so on.",
              "हृदय → यकृत् → प्लीह → फुप्फुस → उंदुक → अंत्र."),
        match(2, "Match each organ of unit 64 to its meaning.",
              [["हृदय", "heart"], ["यकृत्", "liver"], ["प्लीहन्", "spleen"], ["फुप्फुस", "lung"], ["अन्त्र", "intestine"]],
              "Five of the koṣṭhāṅgas with their standard meanings.",
              "हृदय, यकृत्, प्लीहन्, फुप्फुस, अन्त्र.", role="extend",
              teaches="कोष्ठ = the trunk, belly; कोष्ठांग = a member (organ) of the koṣṭha."),
        mcq("discriminate", 3, "Which split of कोष्ठांगानि is right?",
            ("कोष्ठ + अङ्गानि", "अ + अ → आ: कोष्ठ + अङ्गानि → कोष्ठाङ्गानि (printed with ं)."),
            [("कोष्ठम् + अङ्गानि", "म् before a vowel stays: that would give कोष्ठमङ्गानि."),
             ("कोष्ठः + अङ्गानि", "अः + अ gives ओऽ: that would be कोष्ठोऽङ्गानि."),
             ("को + ष्ठाङ्गानि", "को and ष्ठाङ्गानि are not the words; the words are कोष्ठ, अङ्ग.")],
            "कोष्ठ (trunk) + अङ्गानि (members): अ + अ → आ.",
            "अ + अ → आ."),
        multi("apply", 4, "Which organs does unit 64 name among the koṣṭhāṅgas?",
              [("The tongue", "Not in this list; the tongue is a seat of a sense (unit 58)."),
               ("The heart", "Right: हृदय comes first."),
               ("The eye", "Not in this list; the eyes are a seat of a sense (unit 58)."),
               ("The spleen", "Right: प्लीह-."),
               ("The lung", "Right: फुप्फुस-.")],
              [1, 3, 4],
              "Heart, spleen and lung are named; tongue and eye are seats of the senses.",
              "हृदययकृत्प्लीहफुप्फुसोंदुकवक्कांत्रादीनि."),
        mcq("transfer", 5, "By the rule of फुप्फुस + उंदुक → फुप्फुसोंदुक, how is वसन्त + उत्सवः (spring festival) joined?",
            ("वसन्तोत्सवः", "अ + उ → ओ, as फुप्फुस + उंदुक → फुप्फुसोंदुक."),
            [("वसन्तुत्सवः", "The अ is not dropped; अ + उ merge as ओ."),
             ("वसन्तौत्सवः", "औ comes from अ + ओ or औ, not from अ + उ."),
             ("वसन्तवुत्सवः", "व् comes from उ before a vowel, not from अ + उ.")],
            "वसन्त + उत्सवः = वसन्तोत्सवः, like फुप्फुस + उंदुक = फुप्फुसोंदुक.",
            "अ + उ → ओ.",
            teaches="अ + उ → ओ: फुप्फुस + उंदुक → फुप्फुसोंदुक."),
    ],
}

# ---------------------------------------------------------------- unit 65
AUTHORED["65"] = {
    "title": "तत्र समानेनाध्मायमानस्य",
    "question": "By unit 65, from what blood do the liver and spleen arise?",
    "rule": ("There, from blood (शोणित) being inflated by samāna and being cooked by the body's heat (देहोष्मन्), "
             "the liver and spleen arise (जायते)."),
    "limits": ("Low confidence. The printed अच्छतः is unclear; 'from its clear part' is a conjecture: no question on it. "
               "samāna = the Vāyu so named is probable. The singular verb with two organs is as printed: no question on it."),
    "explain_hi": ("यह गद्य-पंक्ति कोष्ठांगों की उत्पत्ति का वर्णन शुरू करती है; इसका विश्वास निम्न है। "
                   "समान नाम का वायु (सम्भावित) शोणित यानी रक्त को फुलाता है, और देह की ऊष्मा उसे पकाती है। "
                   "ऐसे रक्त से यकृत् (जिगर) और प्लीहा (तिल्ली) उत्पन्न होते हैं (जायते)। "
                   "छपा शब्द ‘अच्छतः’ अस्पष्ट है; ‘उसके स्वच्छ भाग से’ केवल अनुमानित पाठ है। "
                   "आगे की छोटी इकाइयाँ (६६ से) इसी क्रिया ‘जायते’ को साथ लेकर चलती हैं।"),
    "hook": "समान फुलाए, ऊष्मा पकाए: रक्त से यकृत्-प्लीहा।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 65, which organs arise from the blood?",
            ("The liver and the spleen", "जायते यकृत्प्लीहा च: the liver and the spleen arise."),
            [("The bones and the joints", "No bone or joint is named in unit 65."),
             ("The eyes and the ears", "No eye or ear is named in unit 65."),
             ("The hair and the nails", "No hair or nail is named in unit 65.")],
            "From the blood, inflated and cooked, the liver and spleen arise.",
            "जायते यकृत्प्लीहा च."),
        order(1, "Put these phrases of unit 65 in the line's order (the unclear शोणितस्याच्छतो is left out).",
              ["तत्र", "समानेनाध्मायमानस्य", "देहोष्मणा पच्यमानस्य", "जायते", "यकृत्प्लीहा च"],
              "There, being inflated by samāna, being cooked by the body's heat, (of blood), arise the liver and spleen.",
              "तत्र → समानेनाध्मायमानस्य → देहोष्मणा पच्यमानस्य → जायते → यकृत्प्लीहा च."),
        match(2, "Match each word of unit 65 to its meaning.",
              [["समान", "samāna, the Vāyu so named (probable)"], ["आध्मायमान", "being inflated"],
               ["देहोष्मन्", "the body's heat"], ["पच्यमान", "being cooked"], ["जायते", "arises"]],
              "Blood inflated by samāna and cooked by the body's heat: the liver and spleen arise.",
              "समान, आध्मायमान, देहोष्मन्, पच्यमान, जायते.", role="extend",
              teaches="आध्मायमान = being inflated: the present passive participle of आ-√ध्मा."),
        mcq("discriminate", 3, "Which split of देहोष्मणा is right?",
            ("देह + ऊष्मणा", "अ + ऊ → ओ: देह + ऊष्मणा → देहोष्मणा."),
            [("देहः + ऊष्मणा", "अः before a vowel other than अ loses the visarga: देह ऊष्मणा, no ओ."),
             ("देहो + ऊष्मणा", "ओ before a vowel becomes अव्: that would give देहवूष्मणा."),
             ("दे + होष्मणा", "दे and होष्मणा are not the words; the words are देह, ऊष्मन्.")],
            "देह (body) + ऊष्मणा (by the heat): अ + ऊ → ओ.",
            "अ + ऊ → ओ."),
        mcq("apply", 4, "By unit 65, what does the body's heat do to the blood?",
            ("It cooks the blood", "पच्यमानस्य: being cooked by the body's heat."),
            [("It cools the blood", "Nothing cools it; the heat cooks it (पच्यमान)."),
             ("It dries the blood", "No drying is named; the heat cooks it."),
             ("It stops the blood", "No stopping is named; the heat cooks it.")],
            "Samāna inflates the blood; the body's heat cooks it.",
            "देहोष्मणा पच्यमानस्य."),
        mcq("transfer", 5, "By the rule of देह + ऊष्मणा → देहोष्मणा, how is जल + ऊर्मिः (a wave of water) joined?",
            ("जलोर्मिः", "अ + ऊ → ओ, as देह + ऊष्मणा → देहोष्मणा."),
            [("जलूर्मिः", "The अ is not dropped; अ + ऊ merge as ओ."),
             ("जलौर्मिः", "औ comes from अ + ओ or औ, not from अ + ऊ."),
             ("जलवूर्मिः", "व् comes from उ/ऊ before a vowel, not from अ + ऊ.")],
            "जल + ऊर्मिः = जलोर्मिः, like देह + ऊष्मणा = देहोष्मणा.",
            "अ + ऊ → ओ.",
            teaches="अ + ऊ → ओ: देह + ऊष्मणा → देहोष्मणा."),
    ],
}

# ---------------------------------------------------------------- unit 66
AUTHORED["66"] = {
    "title": "रक्तफेनात्फुप्फुसं",
    "question": "By unit 66, from what does the lung arise?",
    "rule": "From the froth (फेन) of blood, the lung (फुप्फुस). The verb 'arises' (जायते) is carried from unit 65.",
    "limits": ("Prose, two words with no verb: जायते of unit 65 is understood, not printed. The line gives only the "
               "source; how the froth forms the lung is not said. It is part of the account begun in unit 65."),
    "explain_hi": ("यह छोटी गद्य-पंक्ति कहती है: रक्त के फेन यानी झाग से फुप्फुस (फेफड़ा) बनता है। "
                   "पंक्ति में क्रिया नहीं है; इकाई ६५ की ‘जायते’ (उत्पन्न होता है) समझी जाती है। "
                   "‘रक्तफेनात्’ पंचमी विभक्ति है, यानी ‘से’। "
                   "यह इकाई ६५ से चल रहे अंगों की उत्पत्ति के वर्णन का भाग है। "
                   "झाग से फेफड़ा कैसे बनता है, यह पंक्ति नहीं बताती।"),
    "hook": "रक्त का झाग: उससे फेफड़ा।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 66, from what does the lung arise?",
            ("From the froth of blood", "रक्तफेनात्: from the froth of blood."),
            [("From the dregs of blood", "The dregs give the unduka (unit 67), not the lung."),
             ("From the essence of blood and fat", "Blood and fat give the kidneys (unit 68)."),
             ("From the essence of blood and flesh", "Blood and flesh give the intestines (unit 69).")],
            "The lung arises from the froth of blood.",
            "रक्तफेनात्फुप्फुसं."),
        match(1, "Match each word of unit 66 to its meaning.",
              [["रक्त", "blood"], ["फेन", "froth, foam"], ["फुप्फुस", "lung"]],
              "From the froth of blood, the lung.",
              "रक्त, फेन, फुप्फुस."),
        fill(2, "From the ____ of blood the lung arises (unit 66). Type the Sanskrit word for 'froth' in Devanagari "
                "or in English letters (e.g. dharma).",
             accepts("फेन", "phena"),
             "फेन = froth: रक्तफेनात् = from the froth of blood.",
             "फेन = froth, foam: रक्तफेन = the froth of blood.",
             "रक्त + फेन = the froth of blood."),
        mcq("discriminate", 3, "Which split of रक्तफेनात्फुप्फुसं is right?",
            ("रक्तफेनात् + फुप्फुसम्", "त् stays before the unvoiced फ; the final म् is printed ं."),
            [("रक्तफेना + त्फुप्फुसम्", "त्फुप्फुसम् is not a word; the ablative is रक्तफेनात्."),
             ("रक्तफेनः + फुप्फुसम्", "A visarga gives no त्: that would be रक्तफेनः फुप्फुसम्."),
             ("रक्तफेनम् + फुप्फुसम्", "म् before फ would be written ं: रक्तफेनं फुप्फुसम्.")],
            "रक्तफेनात् (from the froth of blood) + फुप्फुसम् (lung).",
            "त् stays before an unvoiced consonant such as क, प, फ, स (not before च, छ, श, ट, where it changes)."),
        mcq("apply", 4, "Unit 66 prints no verb. By the data, which verb is understood?",
            ("जायते, arises", "The verb of unit 65 is carried; it is not printed."),
            [("नश्यति, perishes", "Nothing perishes; the organs arise."),
             ("धारयति, holds", "No holding is named; the organs arise."),
             ("पच्यते, is cooked", "Unit 65 has the participle पच्यमान, not this verb; the carried verb is जायते.")],
            "जायते (arises) is carried from unit 65: from the froth of blood the lung arises.",
            "Elliptical line: the verb comes from unit 65."),
        mcq("transfer", 5, "By the -आत् of रक्तफेनात् (from the froth), what does वृक्षात् फलं पतति mean?",
            ("The fruit falls from the tree", "-आत् is the ablative: from the tree, as रक्तफेनात् = from the froth."),
            [("The fruit falls on the tree", "On the tree would be the locative वृक्षे."),
             ("The fruit of the tree falls", "Of the tree would be the genitive वृक्षस्य."),
             ("The tree falls with the fruit", "With would be the instrumental, and the tree is not the subject.")],
            "वृक्षात् = from the tree, as रक्तफेनात् = from the froth of blood.",
            "-आत् (a-stems) = ablative, from.",
            teaches="-आत् is the ablative ending (from) of a-stem nouns: रक्तफेनात् = from the froth of blood."),
    ],
}

# ---------------------------------------------------------------- unit 67
AUTHORED["67"] = {
    "title": "रक्तकिट्टादुंदुकः",
    "question": "By unit 67, from what does the unduka arise?",
    "rule": "From the dregs (किट्ट) of blood, the unduka (probably the caecum). The verb 'arises' is carried from unit 65.",
    "limits": ("Prose, no verb printed (जायते of unit 65 is understood). unduka = caecum is probable only; the line "
               "does not describe the organ."),
    "explain_hi": ("यह छोटी गद्य-पंक्ति कहती है: रक्त के किट्ट यानी तलछट या मैल से उण्डुक बनता है। "
                   "उण्डुक सम्भवतः अन्धान्त्र है; यह पहचान सम्भावित ही है। "
                   "क्रिया छपी नहीं; इकाई ६५ की ‘जायते’ समझी जाती है। "
                   "‘रक्तकिट्टात्’ का त् स्वर उ से पहले द् हो गया है: रक्तकिट्टादुंदुकः।"),
    "hook": "रक्त का तलछट: उससे उण्डुक।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 67, from what does the unduka arise?",
            ("From the dregs of blood", "रक्तकिट्टात्: from the dregs (kiṭṭa) of blood."),
            [("From the froth of blood", "The froth gives the lung (unit 66)."),
             ("From the essence of blood and fat", "Blood and fat give the kidneys (unit 68)."),
             ("From the essence of Kapha and blood", "Kapha and blood give the heart (unit 73).")],
            "The unduka arises from the dregs of blood.",
            "रक्तकिट्टादुंदुकः."),
        match(1, "Match each part of unit 67 to its meaning.",
              [["रक्त", "blood"], ["किट्ट", "dregs, sediment"], ["-आत् (किट्टात्)", "from (ablative)"]],
              "From the dregs of blood, the unduka.",
              "रक्त, किट्ट, -आत्."),
        mcq("extend", 2, "What does किट्ट in unit 67 mean?",
            ("Dregs, the sediment", "The data glosses किट्ट as dregs, sediment."),
            [("Froth on the surface", "Froth is फेन (unit 66)."),
             ("The clear essence", "The clear essence is प्रसाद (unit 68)."),
             ("Heat, warmth", "Heat is ऊष्मन् (unit 65).")],
            "किट्ट = dregs, sediment.",
            "रक्तकिट्ट = the dregs of blood.",
            teaches="किट्ट = dregs, sediment: रक्तकिट्ट = the dregs of blood."),
        mcq("discriminate", 3, "Which split of रक्तकिट्टादुंदुकः is right?",
            ("रक्तकिट्टात् + उंदुकः", "त् before a vowel becomes द्."),
            [("रक्तकिट्टा + दुंदुकः", "दुंदुकः is not the word; the organ is the उंदुक."),
             ("रक्तकिट्टः + उंदुकः", "अः + उ drops the visarga: that would be रक्तकिट्ट उंदुकः."),
             ("रक्तकिट्टम् + उंदुकः", "म् before a vowel stays: that would be रक्तकिट्टमुंदुकः.")],
            "रक्तकिट्टात् (from the dregs of blood) + उंदुकः: त् + vowel → द्.",
            "त् + vowel → द्."),
        multi("apply", 4, "Which statements fit unit 67?",
              [("किट्ट here means froth", "No: किट्ट is dregs; froth (फेन) is unit 66."),
               ("The unduka comes from the dregs of blood", "Right: रक्तकिट्टात् ... उंदुकः."),
               ("रक्तकिट्टात् is ablative: from the dregs", "Right: -आत्, from."),
               ("The line prints its own verb", "No: 'arises' is carried from unit 65.")],
              [1, 2],
              "From the dregs of blood, the unduka; the verb is carried from unit 65.",
              "रक्तकिट्टादुंदुकः."),
        mcq("transfer", 5, "By the rule of रक्तकिट्टात् + उंदुकः, how is तत् + उदकम् (that water) joined?",
            ("तदुदकम्", "त् before a vowel becomes द्."),
            [("ततुदकम्", "Before a vowel the त् does not stay; it becomes द्."),
             ("तद्दुदकम्", "The द् is not doubled."),
             ("तदूदकम्", "The short उ of उदकम् stays short.")],
            "तत् + उदकम् = तदुदकम्, like रक्तकिट्टात् + उंदुकः = रक्तकिट्टादुंदुकः.",
            "त् + vowel → द्.",
            teaches="A final त् becomes द् before a vowel: रक्तकिट्टात् + उंदुकः → रक्तकिट्टादुंदुकः."),
    ],
}

# ---------------------------------------------------------------- unit 68
AUTHORED["68"] = {
    "title": "रक्तमेदःप्रसादाद्वृक्कौ",
    "question": "By unit 68, from what do the two kidneys arise?",
    "rule": ("From the clear essence (प्रसाद) of blood and fat (मेदस्), the two kidneys (वृक्कौ, dual). "
             "'Arise' is carried from unit 65."),
    "limits": "Prose, no verb printed. The line names only the source; it does not describe the kidneys or where they lie.",
    "explain_hi": ("यह छोटी गद्य-पंक्ति कहती है: रक्त और मेद (चर्बी) के प्रसाद यानी स्वच्छ सार से दोनों वृक्क (गुर्दे) बनते हैं। "
                   "‘वृक्कौ’ द्विवचन है: दो गुर्दे। "
                   "क्रिया इकाई ६५ से समझी जाती है। "
                   "‘प्रसादात्’ का त् घोष व्यंजन व से पहले द् हुआ है: प्रसादाद्वृक्कौ। "
                   "प्रसाद शब्द इकाई ६९, ७३, ७५ और ७६ में भी इसी अर्थ में आता है।"),
    "hook": "रक्त और मेद का सार: उससे दो गुर्दे।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 68, from what do the two kidneys arise?",
            ("From the essence of blood and fat", "रक्तमेदःप्रसादात्: from the clear essence of blood and fat."),
            [("From the essence of blood and flesh", "Blood and flesh give the intestines (unit 69)."),
             ("From the essence of Kapha and blood", "Kapha and blood give the heart (unit 73)."),
             ("From the froth of blood", "The froth gives the lung (unit 66).")],
            "The kidneys arise from the clear essence of blood and fat.",
            "रक्तमेदःप्रसादाद्वृक्कौ."),
        match(1, "Match each part of unit 68 to its meaning.",
              [["रक्त", "blood"], ["मेदस्", "fat"], ["प्रसाद", "clear essence"], ["वृक्क", "kidney"]],
              "From the clear essence of blood and fat, the two kidneys.",
              "रक्त, मेदस्, प्रसाद, वृक्क."),
        mcq("extend", 2, "Why is वृक्कौ in unit 68 read as 'the two kidneys'?",
            ("-औ of an a-stem noun is the dual", "The data labels वृक्कौ m. nom. dual: the two kidneys."),
            [("-औ of an a-stem noun is the plural", "The a-stem plural is वृक्काः."),
             ("-औ here is a locative, 'in the kidney'", "For an a-stem the locative is वृक्के; -औ is locative only for i/u-stems (कुक्षौ)."),
             ("-औ here is a genitive, 'of the kidney'", "The genitive is वृक्कस्य.")],
            "वृक्कौ = the two kidneys: masculine, nominative, dual.",
            "a-stem masculine -औ = nominative/accusative dual.",
            teaches="वृक्कौ is a masculine dual: the two kidneys."),
        mcq("discriminate", 3, "Which split of प्रसादाद्वृक्कौ is right?",
            ("प्रसादात् + वृक्कौ", "त् before the voiced व becomes द्."),
            [("प्रसादा + द्वृक्कौ", "द्वृक्कौ is not a word; the word is वृक्कौ."),
             ("प्रसादम् + वृक्कौ", "म् before व would be written ं: प्रसादं वृक्कौ."),
             ("प्रसादः + वृक्कौ", "अः before a voiced consonant gives ओ: प्रसादो वृक्कौ.")],
            "प्रसादात् (from the clear essence) + वृक्कौ: त् + voiced consonant → द्.",
            "त् + voiced consonant → द्."),
        multi("apply", 4, "Which sources does unit 68 name for the kidneys?",
              [("Kapha", "Kapha goes with blood for the heart (unit 73), not here."),
               ("Blood", "Right: रक्त-."),
               ("Flesh", "Flesh goes with blood for the intestines (unit 69), not here."),
               ("Fat", "Right: मेदः-.")],
              [1, 3],
              "The clear essence of blood and fat: रक्तमेदःप्रसादात्.",
              "रक्त + मेदस् + प्रसाद."),
        mcq("transfer", 5, "By the rule of प्रसादात् + वृक्कौ, how is जगत् + गुरुः (teacher of the world) joined?",
            ("जगद्गुरुः", "त् before the voiced ग becomes द्."),
            [("जगत्गुरुः", "Before a voiced consonant the त् does not stay."),
             ("जगन्गुरुः", "त् becomes न् (optionally) only before a nasal, not before ग."),
             ("जगद्दुरुः", "The ग of गुरुः stays ग.")],
            "जगत् + गुरुः = जगद्गुरुः, like प्रसादात् + वृक्कौ = प्रसादाद्वृक्कौ.",
            "त् + voiced consonant → द्.",
            teaches="A final त् becomes द् before a voiced consonant: प्रसादात् + वृक्कौ → प्रसादाद्वृक्कौ."),
    ],
}

# ---------------------------------------------------------------- unit 69
AUTHORED["69"] = {
    "title": "रक्तमांसप्रसादादंत्राणि",
    "question": "By unit 69, from what do the intestines arise?",
    "rule": ("From the clear essence (प्रसाद) of blood and flesh (मांस), the intestines (अन्त्राणि, plural). "
             "'Arise' is carried from unit 65."),
    "limits": "Prose, no verb printed. This line gives only the source of the intestines; it does not describe them.",
    "explain_hi": ("यह छोटी गद्य-पंक्ति कहती है: रक्त और मांस के प्रसाद यानी स्वच्छ सार से अन्त्र (आँतें) बनती हैं। "
                   "‘अन्त्राणि’ नपुंसक बहुवचन है। "
                   "क्रिया इकाई ६५ से समझी जाती है। "
                   "‘प्रसादात्’ का त् स्वर अ से पहले द् हुआ है: प्रसादादंत्राणि।"),
    "hook": "रक्त और मांस का सार: उससे आँतें।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 69, from what do the intestines arise?",
            ("From the essence of blood and flesh", "रक्तमांसप्रसादात्: from the clear essence of blood and flesh."),
            [("From the essence of blood and fat", "Blood and fat give the kidneys (unit 68)."),
             ("From the essence of Kapha and blood", "Kapha and blood give the heart (unit 73)."),
             ("From the dregs of blood", "The dregs give the unduka (unit 67).")],
            "The intestines arise from the clear essence of blood and flesh.",
            "रक्तमांसप्रसादादंत्राणि."),
        order(1, "Put the parts of unit 69 in the line's order.",
              ["रक्त", "मांस", "प्रसादात्", "अंत्राणि"],
              "Blood, flesh, from the clear essence, the intestines.",
              "रक्त → मांस → प्रसादात् → अंत्राणि."),
        match(2, "Match each part of unit 69 to its meaning.",
              [["रक्त", "blood"], ["मांस", "flesh"], ["प्रसाद", "clear essence"], ["अन्त्र", "intestine"]],
              "From the clear essence of blood and flesh, the intestines.",
              "रक्त, मांस, प्रसाद, अन्त्र.", role="extend",
              teaches="मांस = flesh: रक्तमांसप्रसाद = the clear essence of blood and flesh."),
        mcq("discriminate", 3, "Which split of प्रसादादंत्राणि is right?",
            ("प्रसादात् + अन्त्राणि", "त् before a vowel becomes द्."),
            [("प्रसादात् + आन्त्राणि", "A long आ would stay long: प्रसादादान्त्राणि."),
             ("प्रसादः + अन्त्राणि", "अः + अ gives ओऽ: प्रसादोऽन्त्राणि."),
             ("प्रसादा + दन्त्राणि", "दन्त्राणि is not a word; the word is अन्त्राणि.")],
            "प्रसादात् (from the clear essence) + अन्त्राणि (intestines): त् + vowel → द्.",
            "त् + vowel → द्."),
        mcq("apply", 4, "What does the ending of अन्त्राणि in unit 69 show?",
            ("Plural: the intestines, many", "The data labels it n. nom. pl."),
            [("Dual: the two intestines", "A neuter dual would be अन्त्रे."),
             ("Singular: one intestine", "The singular would be अन्त्रम्."),
             ("Instrumental: by the intestines", "That would be अन्त्रैः.")],
            "अन्त्राणि is neuter nominative plural: the intestines.",
            "Neuter a-stem -आणि/-आनि = nominative/accusative plural."),
        mcq("transfer", 5, "By the pattern of रक्तमांस (blood and flesh), what does मातापितरौ mean?",
            ("Mother and father", "A dvandva: both members joined by 'and', like रक्त and मांस."),
            [("The mother's father", "That would be a tatpuruṣa (मातुः पिता); the dual -औ marks two persons."),
             ("A father like a mother", "Nothing here means 'like'."),
             ("Mother without father", "Nothing here means 'without'.")],
            "मातापितरौ = mother and father, as रक्तमांस = blood and flesh.",
            "Dvandva = X and Y.",
            teaches="A dvandva joins its members with 'and': रक्तमांस = blood and flesh."),
    ],
}

# ---------------------------------------------------------------- unit 70
AUTHORED["70"] = {
    "title": "तानि सार्द्धत्रिव्यामानि पुंसां",
    "question": "By unit 70, how long are the intestines in men?",
    "rule": ("Those (तानि, the intestines of unit 69) are three and a half vyāmas in men (पुंसाम्). "
             "A vyāma is the span of the outstretched arms."),
    "limits": ("Prose. The count is as printed. The line gives no other measure and does not say whose arm-span is "
               "meant. The verb 'are' is understood."),
    "explain_hi": ("यह गद्य-पंक्ति अन्त्र की लम्बाई बताती है। "
                   "‘तानि’ (वे) इकाई ६९ के अन्त्रों की ओर संकेत करता है। "
                   "पुरुषों में वे साढ़े तीन व्याम के होते हैं। "
                   "व्याम यानी फैलाई हुई दोनों बाँहों की लम्बाई। "
                   "छपा ‘सार्द्ध’ = सार्ध (र के बाद द्वित्व, छपाई की आदत)।"),
    "hook": "पुरुष में आँतें: साढ़े तीन व्याम।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 70, how long are the intestines in men?",
            ("Three and a half vyāmas", "सार्द्धत्रिव्यामानि: three and a half vyāmas."),
            [("Seven and a half vyāmas", "The line has त्रि (three), not seven."),
             ("Three vyāmas", "Three vyāmas is the women's length (unit 71)."),
             ("Eight and a half vyāmas", "The line has त्रि (three), not eight.")],
            "In men the intestines are three and a half vyāmas.",
            "तानि सार्द्धत्रिव्यामानि पुंसां."),
        order(1, "Put the words of unit 70 in the line's order.",
              ["तानि", "सार्द्धत्रिव्यामानि", "पुंसां"],
              "Those (are) three and a half vyāmas, of men.",
              "तानि → सार्द्धत्रिव्यामानि → पुंसां."),
        match(2, "Match each part of unit 70 to its meaning.",
              [["तानि", "those (the intestines)"], ["सार्ध", "with a half"], ["त्रि", "three"],
               ["व्याम", "arm-span, fathom"], ["पुंसाम्", "of men"]],
              "Those intestines are three and a half arm-spans in men.",
              "तानि, सार्ध, त्रि, व्याम, पुंसाम्.", role="extend",
              teaches="व्याम = the span of the outstretched arms, a measure of length."),
        mcq("discriminate", 3, "In unit 70, to what does तानि (those, neuter plural) point?",
            ("The intestines of unit 69", "अन्त्राणि is neuter plural, like तानि; the data names it the antecedent."),
            [("The two kidneys of unit 68", "वृक्कौ is masculine dual; it would need तौ."),
             ("The heart of unit 73", "हृदयम् is singular and comes later."),
             ("The lung of unit 66", "फुप्फुसम् is singular; it would need तत्.")],
            "तानि = those intestines (अन्त्राणि, unit 69).",
            "A pronoun agrees in gender and number with what it points to."),
        mcq("apply", 4, "A student renders unit 70 as: Those are three and a half vyāmas in women. Which word is wrong?",
            ("women", "पुंसाम् is of men; women come in unit 71."),
            [("three", "त्रि is three: right."),
             ("half", "सार्ध, with a half: right."),
             ("Those", "तानि, those: right.")],
            "Those (intestines) are three and a half vyāmas in men.",
            "पुंसाम् = of men."),
        mcq("transfer", 5, "By सार्द्धत्रि (three and a half), what does सार्धद्वि mean?",
            ("Two and a half", "सार्ध + द्वि: two with a half more."),
            [("One and a half", "द्वि is two, so the whole is two and a half."),
             ("Half of two", "सार्ध means with a half, not half of."),
             ("Two halves", "सार्ध adds a half to two.")],
            "सार्धद्वि = two and a half, as सार्धत्रि = three and a half.",
            "सार्ध + number = that number and a half.",
            teaches="सार्ध (with a half) before a number adds a half: सार्धत्रि = three and a half."),
    ],
}

# ---------------------------------------------------------------- unit 71
AUTHORED["71"] = {
    "title": "त्रिव्यामानि स्त्रीणां",
    "question": "By unit 71, how long are the intestines in women?",
    "rule": "In women (स्त्रीणाम्), three vyāmas. The intestines (तानि) and 'are' are carried from unit 70.",
    "limits": "Prose, two words; the noun and the verb are understood from unit 70, not printed. The count is as printed.",
    "explain_hi": ("यह दो शब्दों की गद्य-पंक्ति है: स्त्रियों में तीन व्याम। "
                   "क्या मापा जा रहा है, यह यहाँ छपा नहीं; ‘तानि’ (वे अन्त्र) इकाई ७० से समझा जाता है। "
                   "‘स्त्रीणाम्’ षष्ठी बहुवचन है: स्त्रियों का, यानी स्त्रियों में। "
                   "संख्या जैसी छपी है वैसी ही ली गई है।"),
    "hook": "स्त्री में आँतें: तीन व्याम।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 71, how long are the intestines in women?",
            ("Three vyāmas", "त्रिव्यामानि: three vyāmas."),
            [("Three and a half vyāmas", "That is the men's length (unit 70)."),
             ("Four vyāmas", "The line has त्रि, three."),
             ("Two vyāmas", "The line has त्रि, three.")],
            "In women the intestines are three vyāmas.",
            "त्रिव्यामानि स्त्रीणां."),
        match(1, "Match each part of unit 71 to its meaning.",
              [["त्रि", "three"], ["व्याम", "arm-span, fathom"], ["स्त्रीणाम्", "of women"]],
              "Three vyāmas, in women.",
              "त्रि, व्याम, स्त्रीणाम्."),
        mcq("extend", 2, "Unit 71 prints no noun. By the data, what does it measure?",
            ("The intestines, from unit 70", "तानि (the intestines) is carried from unit 70."),
            [("The kidneys, from unit 68", "The kidneys get no length; तानि of unit 70 is carried."),
             ("The sense-organs, from unit 75", "Unit 75 comes later and gives no length."),
             ("The heart, from unit 73", "The heart comes later and gives no length.")],
            "The intestines (तानि of unit 70) are understood.",
            "Elliptical line: the noun comes from unit 70.",
            teaches="An elliptical line carries its noun and verb from the line before: तानि of unit 70."),
        mcq("discriminate", 3, "What does the ending of स्त्रीणाम् in unit 71 show?",
            ("Genitive plural: of women", "The data labels it f. gen. pl."),
            [("Genitive singular: of a woman", "That would be स्त्रियाः."),
             ("Instrumental plural: by women", "That would be स्त्रीभिः."),
             ("Nominative plural: the women", "That would be स्त्रियः.")],
            "स्त्रीणाम् = of women: genitive plural.",
            "-णाम्/-नाम् = genitive plural."),
        multi("apply", 4, "Which statements fit unit 71?",
              [("The women's length is three and a half vyāmas", "No: सार्ध is not in this line; that is the men's length (unit 70)."),
               ("The noun measured is printed in this line", "No: तानि (the intestines) is carried from unit 70."),
               ("The women's length is three vyāmas", "Right: त्रिव्यामानि."),
               ("स्त्रीणाम् means of women", "Right: f. gen. pl.")],
              [2, 3],
              "In women, three vyāmas; the noun is carried from unit 70.",
              "त्रिव्यामानि स्त्रीणां."),
        mcq("transfer", 5, "By त्रिव्यामानि, where त्रि counts the vyāmas, what does पञ्च वर्षाणि mean?",
            ("Five years", "पञ्च counts the years, as त्रि counts the vyāmas."),
            [("The fifth year", "The fifth would be पञ्चमम्."),
             ("Five each year", "Nothing here means each."),
             ("Years of five men", "No men are named; पञ्च counts the years.")],
            "पञ्च वर्षाणि = five years, as त्रिव्यामानि = three vyāmas.",
            "A number before a noun counts it.",
            teaches="A number before a noun counts it: त्रिव्यामानि = three vyāmas."),
    ],
}

# ---------------------------------------------------------------- unit 72
AUTHORED["72"] = {
    "title": "रक्तस्यानिलयोगात्कोलीयं",
    "question": "By unit 72, with what does the blood join, and what is left unclear?",
    "rule": "From the union (योग) of blood (रक्त) with Vāyu (अनिल), the unclear कोलीयम्. 'Arises' is carried from unit 65.",
    "limits": ("Low confidence. कोलीयम् is not a known word here; what it names cannot be recovered (kola = jujube is "
               "only a guess): no question on it. The line does not say what arises."),
    "explain_hi": ("यह गद्य-पंक्ति कहती है: रक्त के अनिल यानी वायु से योग से ‘कोलीयम्’। "
                   "इसका विश्वास निम्न है। "
                   "‘कोलीयम्’ यहाँ ज्ञात शब्द नहीं; यह सम्भवतः किसी अंग का नाम है, पर कौन-सा, यह तय नहीं हो सकता "
                   "(कोल = बेर केवल अनुमान है)। "
                   "इसलिए यह इकाई नहीं बताती कि क्या उत्पन्न होता है। "
                   "क्रिया इकाई ६५ से समझी जाती है।"),
    "hook": "रक्त और वायु का योग: पर क्या बना, अस्पष्ट।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 72, with what is the blood joined?",
            ("With anila", "अनिलयोगात्: from union with anila, the doṣa Vāta."),
            [("With cool water", "No water is named in unit 72."),
             ("With milk and honey", "No milk or honey is named in unit 72."),
             ("With the mother's food", "No food is named in unit 72.")],
            "The blood is joined with anila (Vāta).",
            "रक्तस्य अनिलयोगात्."),
        match(1, "Match each part of unit 72 to its meaning.",
              [["रक्त", "blood"], ["अनिल", "anila (Vāta)"], ["योग", "union, joining"]],
              "From the union of blood with anila (Vāta).",
              "रक्त, अनिल, योग."),
        mcq("extend", 2, "What does अनिल in unit 72 mean?",
            ("Vāta, the doṣa", "The data glosses अनिल as anila (Vāta, a doṣa)."),
            [("The heat of the body", "That is देहोष्मन् (unit 65)."),
             ("Water, fluid", "Water is जल or उदक."),
             ("Earth, ground", "Earth is पृथ्वी.")],
            "अनिल = anila, the doṣa Vāta.",
            "अनिलयोग = union with anila (Vāta).",
            teaches="अनिल = Vāta (a doṣa): अनिलयोग = union with anila."),
        mcq("discriminate", 3, "Which split of रक्तस्यानिल is right?",
            ("रक्तस्य + अनिल", "अ + अ → आ: रक्तस्य + अनिल → रक्तस्यानिल."),
            [("रक्तस्य + निल", "निल is not a word, and no long आ would come."),
             ("रक्तस्ये + अनिल", "ए + अ would give रक्तस्येऽनिल."),
             ("रक्त + स्यानिल", "स्यानिल is not a word; the genitive is रक्तस्य.")],
            "रक्तस्य (of blood) + अनिल (Vāyu): अ + अ → आ.",
            "अ + अ → आ."),
        multi("apply", 4, "Which statements fit unit 72?",
              [("Blood is joined with Vāyu", "Right: रक्तस्य अनिलयोगात्."),
               ("The line prints its own verb", "No: 'arises' is carried from unit 65."),
               ("The blood is joined with Kapha", "No: अनिल is Vāyu, not Kapha (कफ)."),
               ("योगात् is ablative: from union", "Right: -आत्, from.")],
              [0, 3],
              "From the union of blood with Vāyu; the last word is unclear and the verb is carried.",
              "रक्तस्यानिलयोगात् (sure) + कोलीयं (unclear)."),
        mcq("transfer", 5, "By the rule of रक्तस्य + अनिल, how is सूर्य + अस्तः (sunset) joined?",
            ("सूर्यास्तः", "अ + अ → आ, as रक्तस्य + अनिल → रक्तस्यानिल."),
            [("सूर्येस्तः", "ए comes from अ + इ, not from अ + अ."),
             ("सूर्योस्तः", "ओ comes from अ + उ, not from अ + अ."),
             ("सूर्यऽस्तः", "The avagraha marks an अ dropped after ए or ओ.")],
            "सूर्य + अस्तः = सूर्यास्तः, like रक्तस्य + अनिल = रक्तस्यानिल.",
            "अ + अ → आ.",
            teaches="A short अ followed by a short अ joins as आ: रक्तस्य + अनिल → रक्तस्यानिल."),
    ],
}

# ---------------------------------------------------------------- unit 73
AUTHORED["73"] = {
    "title": "हृदयं पुनः श्लेष्मरक्तप्रसादात्संभवति",
    "question": "By unit 73, from what does the heart arise, and what is it like?",
    "rule": ("The heart arises (संभवति) from the clear essence of Kapha (श्लेष्मन्) and blood; it resembles a lotus bud "
             "(पद्मकोश), is hollow (सुषिर) and has its face downward (अधोमुख)."),
    "limits": ("Prose. Lotus = Nelumbo nucifera (standard); कोश also means sheath or calyx, and the plain sense 'bud' is "
               "kept. 'Face downward' is not explained further in the line."),
    "explain_hi": ("यह गद्य-पंक्ति हृदय की उत्पत्ति और आकार बताती है। "
                   "हृदय कफ (श्लेष्मा) और रक्त के प्रसाद यानी स्वच्छ सार से उत्पन्न होता है (संभवति)। "
                   "वह पद्मकोश यानी कमल की कली के समान है, सुषिर यानी खोखला है, और अधोमुख है, यानी उसका मुख नीचे की ओर है। "
                   "कमल की पहचान मानक है; ‘कोश’ का अर्थ पुटक भी होता है, पर यहाँ सरल अर्थ ‘कली’ रखा गया है। "
                   "‘अधोमुख’ का आगे कोई अर्थ-विस्तार पंक्ति में नहीं है।"),
    "hook": "कफ-रक्त का सार: कमल-कली-सा, खोखला, मुँह नीचे।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 73, from what does the heart arise?",
            ("From the essence of Kapha and blood", "श्लेष्मरक्तप्रसादात्: from the clear essence of Kapha and blood."),
            [("From the essence of blood and fat", "Blood and fat give the kidneys (unit 68)."),
             ("From the essence of blood and flesh", "Blood and flesh give the intestines (unit 69)."),
             ("From the dregs of blood", "The dregs give the unduka (unit 67).")],
            "The heart arises from the clear essence of Kapha and blood.",
            "हृदयं पुनः श्लेष्मरक्तप्रसादात्संभवति."),
        order(1, "Put these phrases of unit 73 in the line's order.",
              ["हृदयं पुनः", "श्लेष्मरक्तप्रसादात्संभवति", "पद्मकोशसंकाशं", "सुषिरम्", "अधोमुखं"],
              "The heart, moreover, arises from the clear essence of Kapha and blood; like a lotus bud, hollow, face downward.",
              "हृदयं पुनः → ...संभवति → पद्मकोशसंकाशं → सुषिरम् → अधोमुखं."),
        match(2, "Match each word of unit 73 to its meaning.",
              [["पद्मकोश", "lotus bud"], ["संकाश", "resembling"], ["सुषिर", "hollow"], ["अधोमुख", "face downward"],
               ["संभवति", "arises"]],
              "The heart arises; it is like a lotus bud, hollow, with its face downward.",
              "पद्मकोश, संकाश, सुषिर, अधोमुख, संभवति.", role="extend",
              teaches="पद्मकोशसंकाश = resembling a lotus bud (lotus, Nelumbo nucifera: standard)."),
        mcq("discriminate", 3, "Which split of अधोमुखं is right?",
            ("अधः + मुखम्", "अः + a voiced consonant (म) → ओ."),
            [("अधः + उमुखम्", "अः + उ drops the visarga (अध उमुखम्), and उमुख is not a word."),
             ("अधम् + मुखम्", "म् before म would be written ं or म्म्: अधंमुखम्."),
             ("अधो + ओमुखम्", "ओमुख is not a word, and ओ + ओ would give अवो.")],
            "अधः (downward) + मुखम् (face): अः + voiced consonant → ओ.",
            "अः + voiced consonant → ओ (अः + अ → ओऽ)."),
        multi("apply", 4, "Which describe the heart in unit 73?",
              [("Hollow", "Right: सुषिरम्."),
               ("Solid all through", "The heart is hollow (सुषिर)."),
               ("Like a lotus bud", "Right: पद्मकोशसंकाशम्."),
               ("With its face downward", "Right: अधोमुखम्."),
               ("With its face upward", "अधोमुख: downward, not upward.")],
              [0, 2, 3],
              "Like a lotus bud, hollow, face downward.",
              "पद्मकोशसंकाशं सुषिरमधोमुखं."),
        mcq("transfer", 5, "By the rule of अधः + मुखम् → अधोमुखम्, how is मनः + रथः (wish) joined?",
            ("मनोरथः", "अः + a voiced consonant (र) → ओ."),
            [("मनरथः", "After अ the visarga is not simply dropped before र."),
             ("मनोऽरथः", "The avagraha marks a dropped अ; रथः begins with र."),
             ("मनारथः", "आ does not come from अः before र.")],
            "मनः + रथः = मनोरथः, like अधः + मुखम् = अधोमुखम्.",
            "अः + voiced consonant → ओ.",
            teaches="अः before a voiced consonant becomes ओ: अधः + मुखम् → अधोमुखम्."),
    ],
}

# ---------------------------------------------------------------- unit 74
AUTHORED["74"] = {
    "title": "तद्विशेषेण चेतनायाः स्थानं",
    "question": "By unit 74, of what is the heart the seat, and which organs lie on its left and right?",
    "rule": ("The heart is especially the seat of consciousness (चेतना) and of all states that follow it. On its left: "
             "spleen and lung; on the right: liver and kloman."),
    "limits": ("Prose, two printed lines. The kloman's identity is disputed (pancreas, lung or trachea region are "
               "proposed): no question on what it is. भाव 'states' may also mean things, conditions. The placement is as printed."),
    "explain_hi": ("पहली पंक्ति: वह (हृदय, इकाई ७३) विशेष रूप से चेतना का स्थान है, और चेतना के अनुगामी सब भावों का भी। "
                   "‘भाव’ का अर्थ अवस्थाएँ है; ‘वस्तुएँ, दशाएँ’ भी हो सकता है। "
                   "दूसरी पंक्ति: हृदय के बाएँ पार्श्व में प्लीहा (तिल्ली) और फुप्फुस (फेफड़ा) हैं, दाहिनी ओर यकृत् (जिगर) और क्लोम। "
                   "क्लोम की पहचान विवादित है (अग्न्याशय, फेफड़ा या श्वासनली-क्षेत्र कहे गए), इसलिए उसे संस्कृत नाम से ही रखा गया है। "
                   "अंगों की स्थिति जैसी छपी है वैसी ही अनूदित है।"),
    "hook": "हृदय चेतना का घर: बाएँ तिल्ली-फेफड़ा, दाएँ जिगर-क्लोम।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 74, the heart is especially the seat of what?",
            ("Of consciousness", "चेतनायाः स्थानम्: the seat of consciousness."),
            [("Of the bones", "No bone is named; it is the seat of cetanā."),
             ("Of hunger and thirst", "No hunger or thirst is named in unit 74."),
             ("Of the urine", "No urine is named in unit 74; the heart is the seat of cetanā.")],
            "The heart is especially the seat of consciousness.",
            "तद्विशेषेण चेतनायाः स्थानं."),
        order(1, "Put these phrases of unit 74 in the printed order.",
              ["तद्विशेषेण चेतनायाः स्थानं", "सर्वभावानां च चेतनानुगानां", "तस्य वामपार्श्वे", "प्लीहा फुप्फुसश्च",
               "दक्षिणतो", "यकृत्क्लोमंच"],
              "Seat of consciousness and of the states that follow it; on its left spleen and lung; on the right liver and kloman.",
              "...स्थानं → ...चेतनानुगानां → तस्य वामपार्श्वे → प्लीहा फुप्फुसश्च → दक्षिणतो → यकृत्क्लोमंच."),
        match(2, "Match each word of unit 74 to its meaning.",
              [["चेतना", "consciousness"], ["स्थान", "seat, place"], ["अनुग", "following"], ["वाम", "left"],
               ["दक्षिणतः", "on the right"]],
              "The seat of consciousness; organs on the left and on the right.",
              "चेतना, स्थान, अनुग, वाम, दक्षिणतः.", role="extend",
              teaches="वाम = left; दक्षिणतः = on the right: the two sides of the heart."),
        mcq("discriminate", 3, "Why is दक्षिणतः printed दक्षिणतो before यकृत् in unit 74?",
            ("अः becomes ओ before a voiced consonant", "य is voiced: दक्षिणतः + यकृत् → दक्षिणतो यकृत्."),
            [("अः becomes ओ before every consonant", "Not before an unvoiced one: फुप्फुसः + च → फुप्फुसश्च, here."),
             ("दक्षिणतो is a new word, 'of the south'", "The data reads दक्षिणतः, on the right."),
             ("After अ the visarga drops before य", "After अ, before a voiced consonant, it gives ओ; it is not just dropped.")],
            "दक्षिणतः + यकृत् = दक्षिणतो यकृत्: अः + voiced consonant → ओ.",
            "अः + voiced consonant → ओ."),
        mcq("apply", 4, "Picture the heart. By unit 74, which pair lies on its right side?",
            ("The liver and the kloman", "दक्षिणतो यकृत्क्लोमं च: on the right, the liver and the kloman."),
            [("The spleen and the lung", "They are on the left (वामपार्श्वे)."),
             ("The spleen and the kloman", "The spleen is on the left."),
             ("The lung and the liver", "The lung is on the left.")],
            "Left: spleen and lung. Right: liver and kloman.",
            "तस्य वामपार्श्वे प्लीहा फुप्फुसश्च दक्षिणतो यकृत्क्लोमंच."),
        mcq("transfer", 5, "By the rule of फुप्फुसः + च → फुप्फुसश्च, how is सर्पः + च (and the snake) joined?",
            ("सर्पश्च", "A visarga before च becomes श्."),
            [("सर्पो च", "ओ comes before a voiced consonant; च is unvoiced."),
             ("सर्प च", "The visarga is not dropped before च."),
             ("सर्पस्च", "Before च the visarga becomes श्, not स्.")],
            "सर्पः + च = सर्पश्च, like फुप्फुसः + च = फुप्फुसश्च.",
            "Visarga + च → श्च.",
            teaches="A visarga before च becomes श्: फुप्फुसः + च → फुप्फुसश्च."),
    ],
}

# ---------------------------------------------------------------- unit 75
AUTHORED["75"] = {
    "title": "तथा कफरक्तवाहिनां स्रोतसां",
    "question": "By unit 75, from what do the sense-organs arise?",
    "rule": ("Likewise, from the clear essence (प्रसाद) of the channels (स्रोतस्) that carry Kapha and blood, and of the "
             "great elements (महाभूत), the sense-organs (इन्द्रियाणि) arise."),
    "limits": ("Prose; no verb printed ('arise', as in unit 73, is understood). Which sense-organ comes from which element "
               "is not said. srotas and mahābhūta are kept as terms."),
    "explain_hi": ("यह गद्य-पंक्ति इन्द्रियों की उत्पत्ति बताती है। "
                   "इसी प्रकार (तथा), कफ और रक्त को वहन करने वाले स्रोतसों के और महाभूतों के प्रसाद यानी स्वच्छ सार से इन्द्रियाँ बनती हैं। "
                   "स्रोतस् यानी शरीर के मार्ग, नालियाँ; महाभूत यानी महान् भूत (तत्त्व)। "
                   "क्रिया छपी नहीं; ‘उत्पन्न होती हैं’ समझा जाता है। "
                   "कौन-सी इन्द्रिय किस भूत से बनती है, यह यहाँ नहीं कहा गया।"),
    "hook": "स्रोतस् और महाभूतों का सार: उससे इन्द्रियाँ।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 75, from what do the sense-organs arise?",
            ("The essence of channels and great elements", "स्रोतसां महाभूतानां च प्रसादात्: from their clear essence."),
            [("The froth and the dregs of the blood", "Froth and dregs give the lung and the unduka (units 66-67)."),
             ("The essence of the blood and the fat alone", "Blood and fat give the kidneys (unit 68)."),
             ("The essence of the blood and the flesh alone", "Blood and flesh give the intestines (unit 69).")],
            "The sense-organs arise from the clear essence of the channels and the great elements.",
            "...स्रोतसां महाभूतानां च प्रसादादिंद्रियाणि."),
        order(1, "Put these words of unit 75 in the line's order.",
              ["तथा", "कफरक्तवाहिनां", "स्रोतसां", "महाभूतानां च", "प्रसादात्", "इंद्रियाणि"],
              "Likewise, of the channels carrying Kapha and blood, and of the great elements, from the clear essence, the sense-organs.",
              "तथा → कफरक्तवाहिनां → स्रोतसां → महाभूतानां च → प्रसादात् → इंद्रियाणि."),
        match(2, "Match each word of unit 75 to its meaning.",
              [["स्रोतस्", "channel"], ["वाहिन्", "carrying"], ["महाभूत", "great element"], ["प्रसाद", "clear essence"],
               ["इन्द्रिय", "sense-organ"]],
              "From the clear essence of the channels and the great elements, the sense-organs.",
              "स्रोतस्, वाहिन्, महाभूत, प्रसाद, इन्द्रिय.", role="extend",
              teaches="स्रोतस् = channel; कफरक्तवाहिन् = carrying Kapha and blood."),
        mcq("discriminate", 3, "By unit 75, what do the channels named there carry?",
            ("Kapha and blood", "कफरक्तवाहिनाम्: carrying Kapha and blood."),
            [("Vāyu and Pitta", "Neither Vāyu nor Pitta is named in unit 75."),
             ("Urine and stool", "Neither is named in unit 75."),
             ("Food and water", "Neither is named in unit 75.")],
            "The channels of unit 75 carry Kapha and blood.",
            "कफरक्तवाहिनां स्रोतसाम्."),
        multi("apply", 4, "Which sources does unit 75 name for the sense-organs?",
              [("Channels carrying Kapha and blood", "Right: कफरक्तवाहिनां स्रोतसाम्."),
               ("The mind (manas)", "The mind is not named in unit 75."),
               ("The great elements", "Right: महाभूतानाम्."),
               ("The bones", "No bone is named in unit 75.")],
              [0, 2],
              "Two sources: the channels carrying Kapha and blood, and the great elements.",
              "स्रोतसां महाभूतानां च प्रसादात्."),
        mcq("transfer", 5, "By the pattern of कफरक्तवाहिन् (carrying Kapha and blood), what does जलवाहिनी नदी mean?",
            ("A river that carries water", "-वाहिन्/-वाहिनी = carrying; the first member is what is carried."),
            [("A river carried by the water", "The first member is what is carried, not the carrier."),
             ("Water that carries a river", "नदी is the noun described; जलवाहिनी describes it."),
             ("A river without any water", "Nothing here means without.")],
            "जलवाहिनी नदी = a river carrying water, as कफरक्तवाहिन् = carrying Kapha and blood.",
            "X-वाहिन् = carrying X.",
            teaches="-वाहिन् (carrying) after a noun names what is carried: कफरक्तवाहिन् = carrying Kapha and blood."),
    ],
}

# ---------------------------------------------------------------- unit 76
AUTHORED["76"] = {
    "title": "तेष्वपि च नेत्रेश्लेष्मणः प्रसादात्",
    "question": "By unit 76, from what does the white circle of the eye arise, and from which parent is it born?",
    "rule": ("Among these too, in the eye, from the clear essence of Kapha (श्लेष्मन्), the white circle (शुक्लमण्डल, "
             "probably the white of the eye); that is born from the father (पितृज)."),
    "limits": ("Medium confidence. नेत्रेश्लेष्मणः may be read 'in the eye, of Kapha' or 'of the Kapha of the eye' "
               "(nearly the same sense): no question on the split. White of the eye (sclera) is probable. पितृज is not "
               "explained further."),
    "explain_hi": ("यह गद्य-पंक्ति नेत्र के भागों की उत्पत्ति शुरू करती है। "
                   "उनमें भी (तेष्वपि), आँख में श्लेष्मा यानी कफ के प्रसाद यानी स्वच्छ सार से शुक्लमण्डल बनता है; "
                   "यह सम्भवतः आँख का सफेद भाग है। "
                   "वह पितृज है, यानी पिता से उत्पन्न। "
                   "‘नेत्रेश्लेष्मणः’ को ‘नेत्रे + श्लेष्मणः’ (आँख में, कफ का) पढ़ा गया; ‘नेत्रश्लेष्मणः’ (आँख के कफ का) भी "
                   "लगभग वही अर्थ देता है। "
                   "‘पितृज’ का आगे कोई विस्तार यहाँ नहीं है।"),
    "hook": "आँख का सफेद घेरा: कफ के सार से, पिता से।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 76, from what does the white circle of the eye arise?",
            ("From the clear essence of Kapha", "श्लेष्मणः प्रसादात्: from the clear essence of Kapha."),
            [("From the blood alone", "The black circle comes from blood (unit 77), not the white."),
             ("From the froth of the blood", "The froth gives the lung (unit 66)."),
             ("From the clear essence of the flesh", "Flesh with blood gives the intestines (unit 69).")],
            "The white circle arises from the clear essence of Kapha.",
            "श्लेष्मणः प्रसादाच्छुक्लमंडलं."),
        order(1, "Put these words of unit 76 in the line's order.",
              ["तेष्वपि च", "नेत्रेश्लेष्मणः", "प्रसादाच्छुक्लमंडलं", "तत्पितृजं"],
              "Among these too, in the eye, of Kapha, from the clear essence, the white circle; that is father-born.",
              "तेष्वपि च → नेत्रेश्लेष्मणः → प्रसादाच्छुक्लमंडलं → तत्पितृजं."),
        match(2, "Match each word of unit 76 to its meaning.",
              [["शुक्ल", "white"], ["मण्डल", "circle"], ["श्लेष्मन्", "Kapha"], ["पितृज", "born from the father"]],
              "From the clear essence of Kapha, the white circle; it is born from the father.",
              "शुक्ल, मण्डल, श्लेष्मन्, पितृज.", role="extend",
              teaches="पितृज = पितृ (father) + ज (born): born from the father."),
        mcq("discriminate", 3, "Which split of प्रसादाच्छुक्लमंडलं is right?",
            ("प्रसादात् + शुक्लमण्डलम्", "त् + श → च्श, optionally च्छ before a vowel or semivowel (the print has च्छ)."),
            [("प्रसादा + च्छुक्लमण्डलम्", "च्छुक्ल is not a word; the ablative is प्रसादात्."),
             ("प्रसादात् + छुक्लमण्डलम्", "छुक्ल is not a word; the word is शुक्ल, white."),
             ("प्रसादः + शुक्लमण्डलम्", "A visarga gives no च्छ: that would be प्रसादः शुक्ल...")],
            "प्रसादात् (from the clear essence) + शुक्लमण्डलम् (white circle).",
            "त् + श → च्छ when श is followed by a vowel or semivowel (optional; च्श also correct)."),
        mcq("apply", 4, "By unit 76, from which parent is the white circle born?",
            ("From the father", "तत्पितृजम्: that is born from the father."),
            [("From the mother", "The black circle is the mother-born one (unit 77)."),
             ("From both parents", "The circle of sight has the nature of both (unit 77)."),
             ("From neither parent", "पितृज: it is born from the father.")],
            "The white circle is pitṛja, born from the father.",
            "तत्पितृजं."),
        mcq("transfer", 5, "By the rule of तेषु + अपि → तेष्वपि, how is मधु + अरिः (foe of Madhu) joined?",
            ("मध्वरिः", "उ before a different vowel becomes व्: मधु + अरिः → मध्वरिः."),
            [("मधोरिः", "ओ does not come from उ + अ."),
             ("मधुवरिः", "The उ itself becomes व्; it does not stay."),
             ("मध्वारिः", "The short अ of अरिः stays short.")],
            "मधु + अरिः = मध्वरिः, like तेषु + अपि = तेष्वपि.",
            "उ + a different vowel → व्.",
            teaches="उ before a different vowel becomes व्: तेषु + अपि → तेष्वपि."),
    ],
}


# ===================================================================== NOTES_HI
NOTES_HI = {
    "64": ("गद्य-पंक्ति; विश्वास उच्च। पाठ-चिह्न: छपा ‘वक्क’ सम्भवतः ‘वृक्क’ (गुर्दा), जैसा इकाई ६८ में ‘वृक्कौ’; यह सुधार "
           "सम्भावित है, इस पर प्रश्न नहीं। ‘तेषु’ = उन आशयों में (इकाई ६२-६३)। उण्डुक = सम्भवतः अन्धान्त्र (पहचान पर मतभेद); "
           "फुप्फुस = फेफड़ा, वृक्क = गुर्दा (मानक)। क्रिया ‘हैं’ समझी जाती है। छपाई में ं = वर्ग का नासिक्य (कोष्ठांग = कोष्ठाङ्ग, "
           "अंत्र = अन्त्र)। सन्धि जाँची: कोष्ठ + अङ्गानि → कोष्ठाङ्गानि (अ + अ → आ); फुप्फुस + उंदुक → फुप्फुसोंदुक (अ + उ → ओ); "
           "वक्क + अंत्र → वक्कांत्र (अ + अ → आ); अंत्र + आदीनि → अंत्रादीनि (अ + आ → आ)।"),
    "65": ("गद्य-पंक्ति; विश्वास निम्न। पाठ-चिह्न: ‘शोणितस्याच्छतो’ = शोणितस्य + अच्छतः; ‘अच्छतः’ ज्ञात रूप नहीं; ‘अच्छ-तस्’ "
           "(स्वच्छ भाग से) केवल अनुमान है, इकाई ६८-६९ के ‘प्रसादात्’ से तुलना पर; इस पर प्रश्न नहीं। समान = इसी नाम का वायु "
           "(सम्भावित)। ‘आध्मायमानस्य’ आ-√ध्मा का वर्तमान कर्मणि कृदन्त (फुलाया जाता हुआ)। यकृत् और प्लीहा एक कर्ता की तरह "
           "एकवचन क्रिया ‘जायते’ के साथ हैं (जैसा छपा)। सन्धि जाँची: समानेन + आध्मायमानस्य → समानेनाध्मायमानस्य (अ + आ → आ); "
           "देह + ऊष्मणा → देहोष्मणा (अ + ऊ → ओ); अच्छतः + जायते → अच्छतो जायते (अः + घोष व्यंजन → ओ)।"),
    "66": ("गद्य-पंक्ति; विश्वास उच्च। क्रिया नहीं छपी: इकाई ६५ की ‘जायते’ समझी जाती है, जोड़ी नहीं गई। समूह: इकाई ६५-६९ "
           "अंगों की उत्पत्ति का एक चलता वर्णन लगती हैं। फुप्फुस = फेफड़ा (मानक); यहाँ नपुंसक ‘फुप्फुसम्’, इकाई ७४ में पुंलिंग "
           "‘फुप्फुसः’। सन्धि जाँची: रक्तफेनात् + फुप्फुसम् → रक्तफेनात्फुप्फुसम् (त् अघोष फ से पहले बना रहता है); पद-अन्त म् छपाई में ं।"),
    "67": ("गद्य-पंक्ति; विश्वास उच्च। क्रिया नहीं छपी: इकाई ६५ से समझी जाती है। उण्डुक = सम्भवतः अन्धान्त्र (सम्भावित पहचान)। "
           "डेटा का शब्द-रूप ‘unduka’ (दन्त्य न) है, हिन्दी ‘उण्डुक’ (मूर्धन्य ण) लिखती है; छपा ‘उंदुक’ अनुस्वार से। "
           "सन्धि जाँची: रक्तकिट्टात् + उंदुकः → रक्तकिट्टादुंदुकः (त् + स्वर → द्)।"),
    "68": ("गद्य-पंक्ति; विश्वास उच्च। क्रिया इकाई ६५ से समझी जाती है। प्रसाद = स्वच्छ, शुद्ध सार; यही अर्थ इकाई ६९, ७३, ७५, ७६ "
           "में। वृक्क = गुर्दा (मानक); ‘वृक्कौ’ पुंलिंग प्रथमा द्विवचन। सन्धि जाँची: मेदस् + प्रसाद → मेदःप्रसाद (स् → विसर्ग, प से "
           "पहले); प्रसादात् + वृक्कौ → प्रसादाद्वृक्कौ (त् + घोष व्यंजन → द्)।"),
    "69": ("गद्य-पंक्ति; विश्वास उच्च। क्रिया इकाई ६५ से समझी जाती है, जोड़ी नहीं गई। ‘अन्त्राणि’ नपुंसक प्रथमा बहुवचन; र के बाद "
           "न → ण (अन्त्राणि)। सन्धि जाँची: प्रसादात् + अन्त्राणि → प्रसादादन्त्राणि (त् + स्वर → द्); छपा ‘अंत्राणि’ में ं = न्।"),
    "70": ("गद्य-पंक्ति; विश्वास उच्च। संख्या जैसी छपी वैसी अनूदित। व्याम = फैलाई हुई दोनों बाँहों की लम्बाई। ‘तानि’ इकाई ६९ के "
           "‘अन्त्राणि’ की ओर संकेत करता है। क्रिया ‘हैं’ समझी जाती है। छपा ‘सार्द्ध’ = सार्ध (र के बाद द्वित्व, छपाई की आदत)। "
           "डेटा ‘सार्धत्रिव्यामानि’ को बहुव्रीहि कहता है, जबकि इकाई ७१ का ‘त्रिव्यामानि’ द्विगु कहा गया; समास-भेद पर प्रश्न नहीं। "
           "छपा ‘पुंसां’ = पुंसाम् (पद-अन्त म् → ं)।"),
    "71": ("गद्य-पंक्ति; विश्वास उच्च। ‘तानि’ (अन्त्र) और क्रिया इकाई ७० से समझे जाते हैं, जोड़े नहीं गए। संख्या जैसी छपी। "
           "‘स्त्रीणाम्’ स्त्रीलिंग षष्ठी बहुवचन (अर्थ में ‘स्त्रियों में’)। समास-भेद (द्विगु या बहुव्रीहि) पर प्रश्न नहीं। "
           "छपा ‘स्त्रीणां’ = स्त्रीणाम्।"),
    "72": ("गद्य-पंक्ति; विश्वास निम्न। पाठ-चिह्न: ‘कोलीयम्’ यहाँ ज्ञात शब्द नहीं; सम्भवतः रक्त और वायु से बने किसी अंग का नाम, पर "
           "पहचान सम्भव नहीं (कोल = बेर केवल धातु का अनुमान); कोई पाठ अपनाया नहीं गया, इस पर प्रश्न नहीं। क्रिया इकाई ६५ से समझी "
           "जाती है। समूह: इकाई ६५-७२ अंगों की उत्पत्ति का चलता वर्णन लगती हैं; यह इकाई नहीं बताती कि क्या उत्पन्न होता है। "
           "सन्धि जाँची: रक्तस्य + अनिल → रक्तस्यानिल (अ + अ → आ); योगात् + कोलीयम् → योगात्कोलीयम् (त् अघोष क से पहले बना रहता है)।"),
    "73": ("गद्य-पंक्ति; विश्वास उच्च। पद्मकोश = कमल की कली (कमल: पहचान मानक); कोश का अर्थ म्यान, पुटक भी है, पर सरल अर्थ "
           "‘कली’ रखा गया। अधोमुख = मुख (छिद्र या नोक) नीचे की ओर; आगे व्याख्या नहीं। ‘पुनः’ = और, दूसरी ओर। सन्धि जाँची: "
           "हृदयम् + पुनः → हृदयं पुनः (म् → ं); प्रसादात् + संभवति → प्रसादात्संभवति (त् अघोष स से पहले बना रहता है); "
           "सुषिरम् + अधोमुखम् → सुषिरमधोमुखम् (म् + स्वर); अधः + मुखम् → अधोमुखम् (अः + घोष व्यंजन → ओ)।"),
    "74": ("दो छपी पंक्तियाँ जुड़ी हैं ([02.05.80], [02.05.81]); गद्य; विश्वास उच्च। ‘तत्’ और ‘तस्य’ = हृदय (इकाई ७३)। भाव = "
           "अवस्थाएँ; ‘वस्तुएँ, दशाएँ’ भी हो सकता है। क्लोम की पहचान विवादित (अग्न्याशय, फेफड़ा या श्वासनली-क्षेत्र कहे गए); कोई एक "
           "पहचान नहीं अपनाई, इस पर प्रश्न नहीं। अंगों की स्थिति जैसी छपी वैसी अनूदित। फुप्फुस यहाँ पुंलिंग (फुप्फुसः), इकाई ६६ में "
           "नपुंसक। छपा ‘क्लोमं’ अ-कारान्त रूप जैसा है; ‘क्लोमन्’ का प्रथमा एकवचन ‘क्लोम’ या ‘क्लोमा’ होता; छपा रूप रखा। "
           "सन्धि जाँची: तत् + विशेषेण → तद्विशेषेण (त् + घोष व्यंजन → द्); चेतना + अनुगानाम् → चेतनानुगानाम् (आ + अ → आ); "
           "फुप्फुसः + च → फुप्फुसश्च (विसर्ग + च → श्); दक्षिणतः + यकृत् → दक्षिणतो यकृत् (अः + घोष व्यंजन → ओ); "
           "क्लोमम् + च → क्लोमं च (छपा ‘क्लोमंच’ जुड़ा)।"),
    "75": ("गद्य-पंक्ति; विश्वास उच्च। क्रिया नहीं छपी; ‘उत्पन्न होना’ (इकाई ७३ जैसा) समझा जाता है। स्रोतस् और महाभूत शास्त्रीय "
           "शब्द रखे गए। ‘वाहिनाम्’ ‘स्रोतसाम्’ से मेल खाता है (नपुंसक षष्ठी बहुवचन)। सन्धि जाँची: प्रसादात् + इन्द्रियाणि → "
           "प्रसादादिन्द्रियाणि (त् + स्वर → द्; छपा ‘इंद्रियाणि’); वाहिनाम्, स्रोतसाम्, महाभूतानाम् → छपे ‘…ं’ (पद-अन्त म् → ं)।"),
    "76": ("गद्य-पंक्ति; विश्वास मध्यम। ‘नेत्रेश्लेष्मणः’ = नेत्रे + श्लेष्मणः (आँख में, कफ का) पढ़ा गया; ‘नेत्रश्लेष्मणः’ (आँख के "
           "कफ का) भी लगभग वही अर्थ देता है; विभाजन पर प्रश्न नहीं। शुक्लमण्डल = श्वेत मण्डल, सम्भवतः आँख का सफेद भाग (सम्भावित)। "
           "पितृज = पिता से उत्पन्न, जैसा छपा; व्याख्या नहीं। ‘तेषु’ किनकी ओर संकेत करता है, डेटा स्पष्ट नहीं कहता। सन्धि जाँची: "
           "तेषु + अपि → तेष्वपि (उ + अ → व); प्रसादात् + शुक्ल → प्रसादाच्छुक्ल, नियम: त् + श → च्श, विकल्प से च्छ (श के बाद स्वर या य/व/र हो तो; छपा च्छ); "
           "तत् + पितृजम् → तत्पितृजम् (त् अघोष प से पहले बना रहता है)।"),
}


# ===================================================================== AIDS
AIDS = {
    "64": {
        "diagram": {"groups": [
            {"label": "कोष्ठांग (पंक्ति के क्रम से)", "items": ["१ हृदय", "२ यकृत् (जिगर)", "३ प्लीहा (तिल्ली)",
                                                         "४ फुप्फुस (फेफड़ा)", "५ उण्डुक (सम्भवतः अन्धान्त्र)",
                                                         "६ वक्क (सम्भवतः वृक्क: गुर्दा)", "७ अन्त्र (आँत)",
                                                         "आदि: सूची खुली"]}]},
        "chunks": "तेषु | प्रतिबद्धानि | कोष्ठांगानि | हृदययकृत्प्लीहफुप्फुसोंदुकवक्कांत्रादीनि",
        "sandhi": "अ + अ → आ: कोष्ठ + अङ्गानि → कोष्ठाङ्गानि · अ + उ → ओ: फुप्फुस + उंदुक → फुप्फुसोंदुक · "
                  "अ + आ → आ: अंत्र + आदीनि → अंत्रादीनि।",
    },
    "65": {
        "diagram": {"groups": [
            {"label": "शोणित (रक्त) पर दो क्रियाएँ", "items": ["समान वायु (सम्भावित) से फुलाया जाता",
                                                          "देह की ऊष्मा से पकाया जाता"]},
            {"label": "उससे उत्पन्न", "items": ["यकृत् (जिगर)", "प्लीहा (तिल्ली)"]},
            {"label": "अस्पष्ट", "items": ["अच्छतः: शब्द अस्पष्ट (अनुमान: स्वच्छ भाग से)"]}]},
        "chunks": "तत्र | समानेनाध्मायमानस्य | देहोष्मणा पच्यमानस्य | शोणितस्याच्छतो (? अस्पष्ट) | जायते यकृत्प्लीहा च",
        "sandhi": "अ + आ → आ: समानेन + आध्मायमानस्य → समानेनाध्मायमानस्य · अ + ऊ → ओ: देह + ऊष्मणा → देहोष्मणा।",
    },
    "66": {
        "frame": "किससे: रक्त का फेन (झाग) → क्या: फुप्फुस (फेफड़ा) → क्रिया: जायते, इकाई ६५ से समझी।",
        "sandhi": "त् अघोष फ से पहले बना रहता है: रक्तफेनात् + फुप्फुसम् → रक्तफेनात्फुप्फुसम् · पद-अन्त म् → ं (छपा ‘फुप्फुसं’)।",
        "puns": "फेन और फुप्फुस: दोनों ‘फ’ से शुरू; ‘फ’ वाले झाग से ‘फ’ वाला फेफड़ा। (मेरी बनाई याद, केवल सुनने की सहायता)",
    },
    "67": {
        "frame": "किससे: रक्त का किट्ट (तलछट) → क्या: उण्डुक (सम्भवतः अन्धान्त्र) → क्रिया: जायते, इकाई ६५ से समझी।",
        "chunks": "रक्तकिट्टादुंदुकः (पढ़ा: रक्तकिट्टात् + उंदुकः)",
        "sandhi": "त् + स्वर → द्: रक्तकिट्टात् + उंदुकः → रक्तकिट्टादुंदुकः।",
    },
    "68": {
        "frame": "किससे: रक्त और मेद का प्रसाद (स्वच्छ सार) → क्या: वृक्कौ (दोनों गुर्दे) → क्रिया: इकाई ६५ से समझी।",
        "chunks": "रक्तमेदःप्रसादाद्वृक्कौ (पढ़ा: रक्त-मेदः-प्रसादात् + वृक्कौ)",
        "sandhi": "त् + घोष व्यंजन → द्: प्रसादात् + वृक्कौ → प्रसादाद्वृक्कौ · समास में स् → ः (प से पहले): मेदस् + प्रसाद → मेदःप्रसाद।",
    },
    "69": {
        "frame": "किससे: रक्त और मांस का प्रसाद (स्वच्छ सार) → क्या: अन्त्राणि (आँतें, बहुवचन) → क्रिया: इकाई ६५ से समझी।",
        "chunks": "रक्तमांसप्रसादादंत्राणि (पढ़ा: रक्त-मांस-प्रसादात् + अन्त्राणि)",
        "sandhi": "त् + स्वर → द्: प्रसादात् + अन्त्राणि → प्रसादादन्त्राणि (छपा ‘अंत्राणि’ में ं = न्)।",
    },
    "70": {
        "frame": "क्या: तानि (वे अन्त्र, इकाई ६९) → कितना: सार्ध + त्रि व्याम = साढ़े तीन व्याम → किनमें: पुंसाम् (पुरुषों में)।",
        "chunks": "तानि | सार्द्धत्रिव्यामानि | पुंसां",
        "anchors": "व्याम = फैलाई हुई दोनों बाँहों की लम्बाई; ‘सार्ध’ = आधा अधिक।",
    },
    "71": {
        "frame": "क्या: (अन्त्र, ‘तानि’ इकाई ७० से समझा) → कितना: त्रि व्याम = तीन व्याम → किनमें: स्त्रीणाम् (स्त्रियों में)।",
        "chunks": "त्रिव्यामानि | स्त्रीणां",
    },
    "72": {
        "frame": "किसका: रक्तस्य (रक्त का) → किससे: अनिलयोगात् (वायु से योग से) → क्या: कोलीयम् (अस्पष्ट शब्द; क्या बनता है, तय नहीं)।",
        "chunks": "रक्तस्यानिलयोगात् | कोलीयं (? अस्पष्ट)",
        "sandhi": "अ + अ → आ: रक्तस्य + अनिल → रक्तस्यानिल · त् अघोष क से पहले बना रहता है: योगात् + कोलीयम् → योगात्कोलीयम्।",
    },
    "73": {
        "diagram": {"groups": [
            {"label": "उत्पत्ति", "items": ["कफ (श्लेष्मा) और रक्त का प्रसाद"]},
            {"label": "हृदय कैसा (क्रम से)", "items": ["१ कमल की कली जैसा", "२ खोखला (सुषिर)", "३ मुख नीचे (अधोमुख)"]}]},
        "chunks": "हृदयं पुनः | श्लेष्मरक्तप्रसादात्संभवति | पद्मकोशसंकाशं | सुषिरमधोमुखं",
        "sandhi": "अः + घोष व्यंजन → ओ: अधः + मुखम् → अधोमुखम् · म् + स्वर: सुषिरम् + अधोमुखम् → सुषिरमधोमुखम् · "
                  "त् अघोष स से पहले बना रहता है: प्रसादात् + संभवति → प्रसादात्संभवति।",
    },
    "74": {
        "contrast": "बाएँ (वामपार्श्वे): प्लीहा, फुप्फुस ↔ दाएँ (दक्षिणतः): यकृत्, क्लोम (पहचान विवादित)।",
        "frame": "क्या: तत् (हृदय) → किसका स्थान: चेतना का, और चेतना के अनुगामी सब भावों का → उसके बाएँ: प्लीहा, फुप्फुस → "
                 "दाएँ: यकृत्, क्लोम।",
        "chunks": "तद्विशेषेण चेतनायाः स्थानं | सर्वभावानां च चेतनानुगानां | तस्य वामपार्श्वे | प्लीहा फुप्फुसश्च | दक्षिणतो | यकृत्क्लोमंच",
        "sandhi": "विसर्ग + च → श्: फुप्फुसः + च → फुप्फुसश्च · अः + घोष व्यंजन → ओ: दक्षिणतः + यकृत् → दक्षिणतो यकृत् · "
                  "आ + अ → आ: चेतना + अनुग → चेतनानुग · त् + घोष व्यंजन → द्: तत् + विशेषेण → तद्विशेषेण।",
    },
    "75": {
        "diagram": {"groups": [
            {"label": "किनका प्रसाद", "items": ["कफ और रक्त को वहन करने वाले स्रोतस्", "महाभूत"]},
            {"label": "उससे", "items": ["इन्द्रियाँ"]}]},
        "chunks": "तथा | कफरक्तवाहिनां स्रोतसां | महाभूतानां च | प्रसादादिंद्रियाणि",
        "sandhi": "त् + स्वर → द्: प्रसादात् + इन्द्रियाणि → प्रसादादिन्द्रियाणि (छपा ‘इंद्रियाणि’)।",
    },
    "76": {
        "chain": {"steps": ["उनमें भी: नेत्र में", "श्लेष्मा (कफ) का प्रसाद", "शुक्लमण्डल (सम्भवतः आँख का सफेद भाग)",
                            "वह पितृज: पिता से उत्पन्न"]},
        "chunks": "तेष्वपि च | नेत्रेश्लेष्मणः | प्रसादाच्छुक्लमंडलं | तत्पितृजं",
        "sandhi": "उ + अ → व: तेषु + अपि → तेष्वपि · त् + श → च्श, विकल्प से च्छ (श के बाद स्वर या य/व/र हो तो; छपा च्छ): प्रसादात् + शुक्ल → "
                  "प्रसादाच्छुक्ल · त् अघोष प से पहले बना रहता है: तत् + पितृजम् → तत्पितृजम्।",
    },
}


# ===================================================================== IMAGE_SPECS
IMAGE_SPECS = {
    ("64", "diagram"): {
        "file": "sh5-koshthanga-64.svg",
        "alt": ("Table of unit 64, the members of the koṣṭha in line order: heart; liver; spleen; lung; unduka (probably "
                "the caecum); vakka (possibly vṛkka, kidney; a flagged reading); intestine; and so on (the list is open)."),
        "type": "table",
        "title": "इकाई ६४: कोष्ठांग, पंक्ति के क्रम से",
        "heads": ["छपा शब्द", "अर्थ"],
        "rows": [["१ हृदय", "दिल"], ["२ यकृत्", "जिगर"], ["३ प्लीह", "तिल्ली"], ["४ फुप्फुस", "फेफड़ा"],
                 ["५ उंदुक", "सम्भवतः अन्धान्त्र"], ["६ वक्क", "सम्भवतः वृक्क: गुर्दा"], ["७ अंत्र", "आँत"],
                 ["आदि", "इत्यादि: सूची खुली"]],
    },
    ("65", "diagram"): {
        "file": "sh5-yakrt-pliha-65.svg",
        "alt": ("Flowchart of unit 65: samāna (probably the Vāyu) inflates the blood and the body's heat cooks it; from "
                "that blood the liver and the spleen arise. The word acchataḥ is unclear."),
        "type": "mermaid",
        "code": ("flowchart TD\n"
                 "  A[\"समान (सम्भवतः वायु)\"] -->|\"फुलाता\"| C[\"शोणित (रक्त)\"]\n"
                 "  B[\"देह की ऊष्मा\"] -->|\"पकाती\"| C\n"
                 "  C --> D[\"यकृत् और प्लीहा\"]\n"
                 "  C -.- E[\"अच्छतः: अस्पष्ट शब्द\"]\n"),
    },
    ("73", "diagram"): {
        "file": "sh5-hrdaya-73.svg",
        "alt": ("Flowchart of unit 73: from the clear essence of Kapha and blood the heart arises; it is 1 like a lotus "
                "bud, 2 hollow, 3 with its face downward."),
        "type": "mermaid",
        "code": ("flowchart TD\n"
                 "  A[\"कफ और रक्त का प्रसाद\"] --> B[\"हृदय\"]\n"
                 "  B --> C[\"१ कमल की<br/>कली जैसा\"]\n"
                 "  B --> D[\"२ खोखला\"]\n"
                 "  B --> E[\"३ मुख नीचे<br/>की ओर\"]\n"),
    },
    ("74", "contrast"): {
        "file": "sh5-hrdaya-parshva-74.svg",
        "alt": ("Two columns of unit 74, the organs beside the heart: on the left side the spleen and the lung; on the "
                "right the liver and the kloman (identity disputed)."),
        "type": "split",
        "title": "इकाई ७४: हृदय के दोनों ओर",
        "cols": [["बाएँ (वामपार्श्वे)", ["प्लीहा (तिल्ली)", "फुप्फुस (फेफड़ा)"]],
                 ["दाएँ (दक्षिणतः)", ["यकृत् (जिगर)", "क्लोम (पहचान विवादित)"]]],
    },
    ("75", "diagram"): {
        "file": "sh5-indriya-prasada-75.svg",
        "alt": ("Flowchart of unit 75: the clear essence of the channels that carry Kapha and blood, and of the great "
                "elements, gives the sense-organs."),
        "type": "mermaid",
        "code": ("flowchart TD\n"
                 "  A[\"कफ-रक्त वाही स्रोतस्\"] --> C[\"इनका प्रसाद\"]\n"
                 "  B[\"महाभूत\"] --> C\n"
                 "  C --> D[\"इन्द्रियाँ\"]\n"),
    },
    ("76", "chain"): {
        "file": "sh5-shukla-mandala-76.svg",
        "alt": ("Chain of unit 76: among these too, in the eye; the clear essence of Kapha; the white circle (probably the "
                "white of the eye); that is born from the father."),
        "type": "chain",
        "title": "इकाई ७६: शुक्लमण्डल",
        "steps": ["उनमें भी: नेत्र में", "श्लेष्मा (कफ) का प्रसाद", "शुक्लमण्डल (सम्भवतः आँख का सफेद भाग)",
                  "वह पितृज: पिता से उत्पन्न"],
    },
}
