from helpers import mcq, match, order, fill, multi, accepts


AUTHORED = {}

# ---------------------------------------------------------------- unit 39
AUTHORED["39"] = {
    "title": "एष विभागः · स्थिता ह्येवं",
    "question": "By unit 39, where else is 'this division' found, and what do the doṣas do when they stay thus?",
    "rule": ("This division (एष विभागः) is also (अपि) in Pitta, śleṣman (Kapha) and pure blood; the doṣas, remaining "
             "thus (स्थिताः ... एवम्), support (अनुगृह्णन्ति) the body."),
    "limits": ("Two printed lines, prose. Line 1 appears to complete the 175 of unit 38 (grouping note). The share of "
               "each kind is not stated (a quarter each is only suggested): no question on it. एवम् (thus) points to a "
               "state not described here."),
    "explain_hi": ("पहली छपी पंक्ति कहती है कि यही विभाग पित्त, श्लेष्मा यानी कफ और शुद्ध रक्त में भी है। "
                   "यह इकाई ३८ के ‘चौथे अंश के विभाग’ और १७५ को पूरा करती दिखती है; पर हर एक का अंश कितना है, यह यहाँ नहीं कहा गया। "
                   "दूसरी पंक्ति: इस प्रकार स्थित रहते हुए दोष शरीर पर अनुग्रह करते हैं, यानी उसे सहारा देते हैं। "
                   "‘एवम्’ (इस प्रकार) किस अवस्था की ओर संकेत करता है, वह इस इकाई में वर्णित नहीं है। "
                   "‘रक्तेष्वपि’ में रक्तेषु + अपि, उ के बाद भिन्न स्वर आने से व् बना।"),
    "hook": "यही बँटवारा पित्त, कफ, शुद्ध रक्त में भी; इस प्रकार टिके दोष शरीर को सहारा देते हैं।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 39, in what else is 'this division' (vibhāga) also found?",
            ("In Pitta, śleṣman and pure blood", "पित्तश्लेष्मशुद्धरक्तेष्वपि: also in Pitta, śleṣman (Kapha) and pure blood."),
            [("In rasa, flesh and the bones", "Rasa, flesh and bones are not named in unit 39."),
             ("In sweat, urine and the stool", "Sweat, urine and stool are not named in unit 39."),
             ("In the limbs, joints and head", "Limbs, joints and head are not named in unit 39.")],
            "This division is also in Pitta, śleṣman (Kapha) and pure blood.",
            "एष विभागः पित्तश्लेष्मशुद्धरक्तेष्वपि."),
        order(1, "Put the words of the second line of unit 39 in the line's order.",
              ["स्थिताः", "हि", "एवम्", "देहम्", "अनुगृह्णन्ति", "दोषाः"],
              "Remaining, indeed, thus, the body, they support, the doṣas.",
              "स्थिता ह्येवं देहमनुगृह्णंति दोषाः."),
        match(2, "Match each word of unit 39 to its meaning.",
              [["एषः", "this"], ["विभागः", "division"], ["अपि", "also"], ["देहम्", "the body"],
               ["अनुगृह्णन्ति", "support, favour"], ["दोषाः", "the doṣas"]],
              "This division is also (in ...); the doṣas, remaining thus, support the body.",
              "एषः, विभागः, अपि, देहम्, अनुगृह्णन्ति, दोषाः.", role="extend",
              teaches="देहम् is the object (accusative) of अनुगृह्णन्ति; दोषाः is the subject (nominative plural)."),
        mcq("discriminate", 3, "Which split of रक्तेष्वपि in unit 39 is right?",
            ("रक्तेषु + अपि", "उ before a different vowel becomes व्: रक्तेषु + अपि → रक्तेष्वपि."),
            [("रक्तेषौ + अपि", "औ before a vowel becomes आव्: that would give रक्तेषावपि."),
             ("रक्ते + ष्वपि", "ष्वपि is not a word; the ष्व comes from -षु + अ."),
             ("रक्तेष्व + अपि", "अ + अ would give a long आ: रक्तेष्वापि.")],
            "रक्तेषु (in the bloods) + अपि (also): उ + अ → व.",
            "उ + a different vowel → व् + that vowel."),
        multi("apply", 4, "Which statements fit unit 39 and its data?",
              [("The unit states the exact share of each kind", "Not stated; one quarter each is only suggested by the arithmetic."),
               ("The doṣas, remaining thus, support the body", "Right: स्थिता ह्येवं देहमनुगृह्णंति दोषाः."),
               ("śleṣman here is Kapha", "Right: śleṣman = Kapha (standard)."),
               ("The unit describes the state that 'thus' points to", "It does not; एवम् points to a statement outside this unit.")],
              [1, 2],
              "The division is also in Pitta, śleṣman (Kapha) and pure blood; the doṣas, remaining thus, support the body.",
              "एष विभागः ... अपि; स्थिता ह्येवं देहमनुगृह्णंति दोषाः."),
        mcq("transfer", 5, "By the rule of रक्तेषु + अपि → रक्तेष्वपि, how is मधु + अत्र (honey here) joined in a new example?",
            ("मध्वत्र", "उ before a different vowel becomes व्, as रक्तेषु + अपि → रक्तेष्वपि."),
            [("मधोत्र", "ओ comes from अ + उ, not from उ + अ."),
             ("मधूत्र", "ऊ comes from उ + उ; here उ meets अ."),
             ("मधवत्र", "अव् comes from ओ before a vowel; मधु ends in उ.")],
            "मधु + अत्र = मध्वत्र, like रक्तेषु + अपि = रक्तेष्वपि.",
            "उ + अ → व.",
            teaches="उ before a different vowel becomes व्: रक्तेषु + अपि → रक्तेष्वपि."),
    ],
}

# ---------------------------------------------------------------- unit 40
AUTHORED["40"] = {
    "title": "व्यत्ययेन तु पीडयंति",
    "question": "By unit 40, what do they do by reversal (vyatyaya)?",
    "rule": ("But (तु) by reversal (व्यत्ययेन), the contrary of the state of unit 39, they afflict (पीडयन्ति)."),
    "limits": ("Prose, three words; elliptical. The subject (the doṣas of unit 39) is carried over and not printed; no "
               "object is stated. The unit does not say what the reversal consists of."),
    "explain_hi": ("यह तीन शब्दों की गद्य-पंक्ति है: किन्तु व्यत्यय से (उलटे होने पर) पीड़ा देते हैं। "
                   "कर्ता छपा नहीं; डेटा के अनुसार वे इकाई ३९ के दोष हैं, जो इस प्रकार स्थित रहकर शरीर को सहारा देते हैं। "
                   "‘व्यत्यय’ का अर्थ है उलट, विपरीत; यानी इकाई ३९ वाली अवस्था का उलटा। "
                   "किसे पीड़ा देते हैं, यह भी नहीं कहा गया। "
                   "‘तु’ (किन्तु) इस पंक्ति को पिछली बात के विरोध में रखता है।"),
    "hook": "उलटे हुए तो वही दोष पीड़ा देते हैं।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 40, what do they do by reversal (vyatyaya)?",
            ("They afflict", "व्यत्ययेन तु पीडयंति: but by reversal they afflict."),
            [("They support", "Supporting the body is said of the doṣas remaining thus (unit 39), not by reversal."),
             ("They carry Vāta", "Carrying is not said in unit 40."),
             ("They grow threefold", "Becoming threefold is not said in unit 40.")],
            "But by reversal they afflict.",
            "व्यत्ययेन तु पीडयंति."),
        match(1, "Match each word of unit 40 to its meaning.",
              [["व्यत्ययेन", "by reversal, by the contrary"], ["तु", "but"], ["पीडयन्ति", "they afflict"]],
              "But by reversal they afflict.",
              "व्यत्ययेन, तु, पीडयन्ति."),
        mcq("extend", 2, "In unit 40 no subject is printed. By the data, who are 'they'?",
            ("The doṣas of unit 39", "Data note: the subject, the doṣas of unit 39, is carried over."),
            [("The dhamanīs of unit 44", "The dhamanīs come later; the subject is carried over from unit 39."),
             ("The prāṇas of unit 47", "The prāṇas come later; the subject is carried over from unit 39."),
             ("The knife-forbidden ones of unit 37", "Unit 37 speaks of ones not to be dealt with by the knife; the subject here is carried over from unit 39.")],
            "They = the doṣas of unit 39, carried over.",
            "Subject carried over: the doṣas (unit 39).",
            teaches="An elliptical line can take its subject from the line before: here the doṣas of unit 39."),
        mcq("discriminate", 3, "What does तु do in unit 40?",
            ("It means 'but'", "तु marks a contrast: but by reversal they afflict."),
            [("It means 'also'", "'Also' is अपि (unit 39), not तु."),
             ("It means 'thus'", "'Thus' is एवम् (unit 39), not तु."),
             ("It means 'for'", "'Indeed, for' is हि (unit 39), not तु.")],
            "तु = but: it sets unit 40 against unit 39.",
            "तु = but (contrast)."),
        fill(4, "In unit 40 'they afflict' is ____ (type it in Devanagari or in English letters, e.g. dharma).",
             accepts("पीडयन्ति", None, "pidayanti", "peedayanti"),
             "पीडयन्ति = they afflict (printed पीडयंति).",
             "पीडयन्ति = they afflict, 3rd person plural present.",
             "व्यत्ययेन तु पीडयन्ति.", role="apply"),
        mcq("transfer", 5, "By the pattern of व्यत्यय → व्यत्ययेन (by reversal), how is हस्त (hand) put in the instrumental singular?",
            ("हस्तेन", "An अ-stem takes -एन in the instrumental singular, as व्यत्यय → व्यत्ययेन."),
            [("हस्ताय", "हस्ताय is the dative singular: for the hand."),
             ("हस्तात्", "हस्तात् is the ablative singular: from the hand."),
             ("हस्ते", "हस्ते is the locative singular: in the hand.")],
            "हस्तेन = by the hand, like व्यत्ययेन = by reversal.",
            "अ-stem, instrumental singular: -एन.",
            teaches="-एन marks the instrumental singular of अ-stems: व्यत्यय → व्यत्ययेन (by, through)."),
    ],
}

# ---------------------------------------------------------------- unit 41
AUTHORED["41"] = {
    "title": "श्यावारुणाः ... वातरक्तं वहंति",
    "question": "By unit 41, what marks the ones that carry Vāta-blood?",
    "rule": ("There (तत्र), the dusky-brown and reddish (श्यावारुणाः), throbbing (प्रस्पन्दिन्यः), fine (सूक्ष्माः), "
             "momentarily full and empty (क्षणपूर्णरिक्ताः) ones carry Vāta-blood (वातरक्तम्)."),
    "limits": ("Prose. The adjectives are feminine plural for an unstated noun (dhamanī or sirā); none is supplied. "
               "Vāta-blood is read as blood of the Vāta type, probably not the disease vātarakta (probable): no "
               "question on the disease. This unit opens the five-fold list of units 41-43."),
    "explain_hi": ("यह गद्य-पंक्ति रक्त के पाँच प्रकारों की सूची (इकाई ४१-४३) शुरू करती है। "
                   "वहाँ श्याव यानी साँवली-भूरी और अरुण यानी लाल, फड़कने वाली, सूक्ष्म, और क्षण में भरी क्षण में खाली: ये वात-रक्त का वहन करती हैं। "
                   "सब विशेषण स्त्रीलिंग बहुवचन हैं; जिस संज्ञा के हैं वह छपी नहीं (धमनी और सिरा दोनों स्त्रीलिंग हैं)। "
                   "‘वातरक्त’ को यहाँ वात-प्रकार का रक्त पढ़ा गया है, सम्भवतः वातरक्त रोग नहीं (सम्भावित)। "
                   "सन्धि: श्याव + अरुणाः → श्यावारुणाः (अ + अ → आ)।"),
    "hook": "साँवली-लाल, फड़कती, पतली, पल में भरी पल में खाली: वात-रक्त।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 41, what do the dusky-brown, reddish, throbbing ones carry?",
            ("Vāta-blood (vāta-rakta)", "...वातरक्तं वहंति: they carry Vāta-blood."),
            [("Pitta-blood (pitta-rakta)", "Pitta-blood goes with blue, yellow, warm ones (unit 42)."),
             ("Kapha-blood (kapha-rakta)", "Kapha-blood goes with fair, cold, itching ones (unit 42)."),
             ("Pure blood (śuddha-rakta)", "Pure blood goes with even, hidden ones (unit 43).")],
            "The dusky-brown, reddish, throbbing, fine, momentarily full and empty ones carry Vāta-blood.",
            "श्यावारुणाः ... वातरक्तं वहंति."),
        order(1, "Put these words of unit 41 in the line's order.",
              ["श्यावारुणाः", "प्रस्पन्दिन्यः", "सूक्ष्माः", "क्षणपूर्णरिक्ताः", "वातरक्तं वहन्ति"],
              "Dusky-brown and reddish, throbbing, fine, momentarily full and empty: they carry Vāta-blood.",
              "श्यावारुणाः → प्रस्पंदिन्यः → सूक्ष्माः → क्षणपूर्णरिक्ता → वातरक्तं वहंति."),
        match(2, "Match each word of unit 41 to its meaning.",
              [["श्याव", "dusky brown"], ["अरुण", "reddish"], ["प्रस्पन्दिन्", "throbbing"], ["सूक्ष्म", "fine, thin"],
               ["क्षणपूर्णरिक्त", "momentarily full and empty"]],
              "Five marks of the ones that carry Vāta-blood.",
              "श्याव, अरुण, प्रस्पन्दिन्, सूक्ष्म, क्षणपूर्णरिक्त.", role="extend",
              teaches="क्षण-पूर्ण-रिक्त: for a moment full, (for a moment) empty: filling and emptying by turns."),
        mcq("discriminate", 3, "Which sign is NOT given in unit 41 for the ones that carry Vāta-blood?",
            ("Warm to the touch", "Warm to the touch (स्पर्शोष्ण) marks the Pitta-blood ones of unit 42."),
            [("Throbbing", "Right in unit 41: प्रस्पन्दिन्यः."),
             ("Fine, thin", "Right in unit 41: सूक्ष्माः."),
             ("Full and empty by turns", "Right in unit 41: क्षणपूर्णरिक्ताः.")],
            "Unit 41: dusky-brown and reddish, throbbing, fine, momentarily full and empty; warmth is unit 42.",
            "श्यावारुणाः प्रस्पंदिन्यः सूक्ष्माः क्षणपूर्णरिक्ताः."),
        multi("apply", 4, "Which statements fit unit 41 and its data?",
              [("The noun these adjectives describe is printed", "It is not printed; none is supplied."),
               ("The adjectives are feminine plural", "Right: e.g. प्रस्पन्दिन्यः, f. nom. pl."),
               ("Vāta-blood here is certainly the disease vātarakta", "The data reads it as blood of the Vāta type, probably not the disease."),
               ("They are momentarily full and momentarily empty", "Right: क्षणपूर्णरिक्ताः.")],
              [1, 3],
              "Feminine plural adjectives for an unstated noun; momentarily full and empty; Vāta-blood, probably not the disease.",
              "श्यावारुणाः प्रस्पंदिन्यः सूक्ष्माः क्षणपूर्णरिक्ता वातरक्तं वहंति."),
        mcq("transfer", 5, "By the rule of श्याव + अरुणाः → श्यावारुणाः, how is न + अस्ति (is not) joined in a new example?",
            ("नास्ति", "अ + अ → आ, as श्याव + अरुणाः → श्यावारुणाः."),
            [("नेस्ति", "ए comes from अ + इ, not from अ + अ."),
             ("नोस्ति", "ओ comes from अ + उ, not from अ + अ."),
             ("नस्ति", "The two अ merge into a long आ; neither simply drops.")],
            "न + अस्ति = नास्ति, like श्याव + अरुणाः = श्यावारुणाः.",
            "अ + अ → आ.",
            teaches="Two short अ merge into long आ: श्याव + अरुणाः → श्यावारुणाः."),
    ],
}

# ---------------------------------------------------------------- unit 42
AUTHORED["42"] = {
    "title": "पित्तरक्तं · कफरक्तं",
    "question": "By unit 42, what marks the Pitta-blood ones, and what marks the Kapha-blood ones?",
    "rule": ("Blue, yellow and dark, warm to the touch, quickly discharging: Pitta-blood. Fair, unctuous (स्निग्ध), "
             "steady, cold, itching: Kapha-blood."),
    "limits": ("Two printed lines, prose; elliptical: the verb 'carry' (वहन्ति) is carried from unit 41, and the noun is "
               "unstated ('ones'). What is discharged and whose itching is meant are not stated."),
    "explain_hi": ("इस इकाई की दो छपी पंक्तियाँ रक्त के दो और प्रकार देती हैं; ‘वहन करती हैं’ क्रिया इकाई ४१ से समझी जाती है। "
                   "पहली: नीली, पीली और काली (असित), स्पर्श में उष्ण, शीघ्र स्रवित होने वाली: पित्त-रक्त। "
                   "दूसरी: गोरी, स्निग्ध यानी चिकनी, स्थिर, ठण्डी, खुजली वाली: कफ-रक्त। "
                   "क्या स्रवित होता है और खुजली किसकी, यह नहीं कहा गया। "
                   "सन्धि: स्पर्श + उष्णाः → स्पर्शोष्णाः (अ + उ → ओ)।"),
    "hook": "पित्त: रंगीन, गरम, जल्दी बहे; कफ: गोरी, चिकनी, स्थिर, ठण्डी, खुजली।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 42, which signs go with the Pitta-blood ones?",
            ("Warm to the touch, quickly discharging", "स्पर्शोष्णाः क्षिप्रस्राविण्यः पित्तरक्तं."),
            [("Cold to the touch, steady and itching", "Cold, steady, itching mark the Kapha-blood ones."),
             ("Throbbing, fine, momentarily full and empty", "These mark the Vāta-blood ones of unit 41."),
             ("Even, hidden and unctuous, rohiṇī", "These mark the pure-blood ones of unit 43.")],
            "Blue, yellow and dark, warm to the touch, quickly discharging: Pitta-blood.",
            "नीलपीतासिताः स्पर्शोष्णाः क्षिप्रस्राविण्यः पित्तरक्तं."),
        order(1, "Put the signs of the Kapha-blood ones in the order of unit 42.",
              ["गौर्यः", "स्निग्धाः", "स्थिराः", "शीताः", "कण्डूमत्यः"],
              "Fair, unctuous, steady, cold, itching: Kapha-blood.",
              "गौर्यः → स्निग्धाः → स्थिराः → शीताः → कंडूमत्यः."),
        match(2, "Match each word of the Pitta-blood line of unit 42 to its meaning.",
              [["नील", "blue"], ["पीत", "yellow"], ["असित", "dark, black"], ["स्पर्श", "touch"], ["उष्ण", "warm"],
               ["क्षिप्रस्राविन्", "quickly discharging"]],
              "Blue, yellow and dark, warm to the touch, quickly discharging.",
              "नील, पीत, असित, स्पर्श, उष्ण, क्षिप्रस्राविन्.", role="extend",
              teaches="स्पर्शोष्ण = warm (उष्ण) to the touch (स्पर्श): the first member says in what respect."),
        mcq("discriminate", 3, "Which split of स्पर्शोष्णाः in unit 42 is right?",
            ("स्पर्श + उष्णाः", "अ + उ → ओ: स्पर्श + उष्णाः → स्पर्शोष्णाः."),
            [("स्पर्शः + उष्णाः", "अः before a vowel other than अ gives अ with no join: स्पर्श उष्णाः."),
             ("स्पर्शे + उष्णाः", "ए before उ becomes अय् (or अ), never ओ."),
             ("स्पर्शो + ष्णाः", "ष्णाः is not a word; the ओ comes from अ + उ.")],
            "स्पर्श (touch) + उष्णाः (warm): अ + उ → ओ.",
            "अ + उ → ओ."),
        mcq("apply", 4, "By unit 42, the ones that are cold, steady and itching carry what?",
            ("Kapha-blood (kapha-rakta)", "गौर्यः स्निग्धाः स्थिराः शीताः कंडूमत्यः कफरक्तं."),
            [("Pitta-blood (pitta-rakta)", "Pitta-blood ones are warm, not cold."),
             ("Vāta-blood (vāta-rakta)", "Vāta-blood ones are throbbing and fine (unit 41)."),
             ("Pure blood (śuddha-rakta)", "Pure-blood ones are even and hidden (unit 43).")],
            "Fair, unctuous, steady, cold, itching: Kapha-blood.",
            "...शीताः कंडूमत्यः कफरक्तं."),
        mcq("transfer", 5, "By the pattern of गौर्यः (fair ones, from गौरी), what is the nominative plural of नदी (river) in a new example?",
            ("नद्यः", "A feminine ई-stem takes -यः in the nominative plural, as गौरी → गौर्यः."),
            [("नदीः", "नदीः is the accusative plural."),
             ("नद्यौ", "नद्यौ is a dual: two rivers."),
             ("नद्याः", "नद्याः is the genitive or ablative singular.")],
            "नद्यः = rivers, like गौर्यः = fair ones.",
            "Feminine ई-stem, nominative plural: -यः.",
            teaches="Feminine ई-stems take -यः in the nominative plural: गौरी → गौर्यः, कण्डूमती → कण्डूमत्यः."),
    ],
}

# ---------------------------------------------------------------- unit 43
AUTHORED["43"] = {
    "title": "लक्षणसंकरे · शुद्धरक्तमिति",
    "question": "By unit 43, which blood goes with mixed signs, and what marks the pure-blood ones?",
    "rule": ("In a mixture of the signs (लक्षणसङ्करे): blood of saṃsarga and sannipāta. Even, hidden, unctuous, rohiṇī "
             "ones: pure blood (शुद्धरक्तम्). इति closes the five-fold list of units 41-43."),
    "limits": ("Two printed lines, prose; the verb 'carry' is carried from unit 41. The line does not count the doṣas in "
               "saṃsarga and sannipāta. The sense of rohiṇī here is uncertain: no question on it."),
    "explain_hi": ("पहली छपी पंक्ति: लक्षणों के मिश्रण में संसर्ग और सन्निपात का रक्त। "
                   "संसर्ग सामान्यतः दो दोषों का और सन्निपात तीनों का मेल माना जाता है, पर यह पंक्ति दोषों की गिनती नहीं करती। "
                   "दूसरी पंक्ति: समान, गूढ़ यानी छिपी हुई, स्निग्ध और रोहिणी: शुद्ध रक्त; ‘रोहिणी’ का यहाँ अर्थ अनिश्चित है। "
                   "अन्त का ‘इति’ इकाई ४१-४३ की पाँच प्रकार की सूची पूरी करता है: वात, पित्त, कफ, संसर्ग-सन्निपात और शुद्ध रक्त। "
                   "छपे ‘समागूढाः’ में समाः + गूढाः हैं; घोष व्यंजन से पहले आः का विसर्ग लुप्त हुआ।"),
    "hook": "लक्षण मिले तो संसर्ग-सन्निपात; समान, गूढ़, चिकनी तो शुद्ध रक्त।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 43, which blood goes with a mixture of the signs (lakṣaṇa-saṅkara)?",
            ("Saṃsarga and sannipāta blood", "लक्षणसंकरे संसर्गसन्निपातरक्तं."),
            [("Pure blood, even and hidden", "Pure blood has its own signs; it is not the mixture."),
             ("Kapha blood, cold and itching", "Kapha-blood has its own signs (unit 42)."),
             ("Vāta blood, throbbing and fine", "Vāta-blood has its own signs (unit 41).")],
            "In a mixture of the signs: blood of saṃsarga and sannipāta.",
            "लक्षणसंकरे संसर्गसन्निपातरक्तं."),
        order(1, "Put the five kinds of blood in the order of units 41-43.",
              ["वातरक्त", "पित्तरक्त", "कफरक्त", "संसर्गसन्निपातरक्त", "शुद्धरक्त"],
              "Vāta, Pitta, Kapha, the mixed (saṃsarga, sannipāta), then pure blood; iti closes the list.",
              "वात → पित्त → कफ → संसर्ग-सन्निपात → शुद्ध."),
        match(2, "Match each word of unit 43 to its meaning.",
              [["लक्षण", "sign, mark"], ["सङ्कर", "mixture"], ["संसर्ग", "combination"],
               ["सन्निपात", "union"], ["शुद्ध", "pure"], ["गूढ", "hidden"]],
              "In a mixture of signs: saṃsarga and sannipāta blood; even, hidden ... ones: pure blood.",
              "लक्षण, सङ्कर, संसर्ग, सन्निपात, शुद्ध, गूढ.", role="extend",
              teaches="लक्षणसङ्करे is a locative of circumstance: 'when the signs are mixed'."),
        mcq("discriminate", 3, "Which sign is shared by the Kapha-blood ones (unit 42) and the pure-blood ones (unit 43)?",
            ("Unctuous (snigdha)", "स्निग्धाः is in both lists."),
            [("Even (sama)", "समाः is only in the pure-blood list."),
             ("Itching (kaṇḍūmat)", "कण्डूमत्यः is only in the Kapha-blood list."),
             ("Cold (śīta)", "शीताः is only in the Kapha-blood list.")],
            "स्निग्ध (unctuous) marks both the Kapha-blood and the pure-blood ones.",
            "कफ: गौर्यः स्निग्धाः ...; शुद्ध: समा गूढाः स्निग्धा ...."),
        multi("apply", 4, "Which statements fit unit 43 and its data?",
              [("The closing इति ends the five-fold list", "Right: iti closes the list of units 41-43."),
               ("The verb 'carry' is printed in unit 43", "It is not printed; it is carried from unit 41."),
               ("The line counts the doṣas in saṃsarga", "The line does not count the doṣas."),
               ("Pure blood is the last kind named", "Right: शुद्धरक्तमिति ends the list.")],
              [0, 3],
              "Mixed signs: saṃsarga and sannipāta blood; pure blood last; iti closes the list.",
              "लक्षणसंकरे ...; ... शुद्धरक्तमिति."),
        mcq("transfer", 5, "By the rule of समाः + गूढाः → समा गूढाः, how is देवाः + गच्छन्ति (the gods go) joined in a new example?",
            ("देवा गच्छन्ति", "आः before a voiced consonant drops its visarga, as समाः + गूढाः → समा गूढाः."),
            [("देवो गच्छन्ति", "ओ comes from अः before a voiced consonant, not from आः."),
             ("देवार्गच्छन्ति", "र् comes from a visarga after vowels other than अ and आ."),
             ("देवाश्गच्छन्ति", "श् comes from a visarga before च, छ or श, not before ग.")],
            "देवाः + गच्छन्ति = देवा गच्छन्ति, like समाः + गूढाः = समा गूढाः.",
            "आः + voiced sound → आ (visarga drops).",
            teaches="आः drops its visarga before a voiced sound: समाः गूढाः → समा गूढाः, स्निग्धाः रोहिण्यः → स्निग्धा रोहिण्यः."),
    ],
}

# ---------------------------------------------------------------- unit 44
AUTHORED["44"] = {
    "title": "धमन्यस्तु चतुर्विंशतिः",
    "question": "By unit 44, how many dhamanīs are there?",
    "rule": ("The dhamanīs (धमन्यः: vessels, channels; probably blood vessels, probable), however (तु), are twenty-four "
             "(चतुर्विंशतिः)."),
    "limits": ("Prose, two words; the copula is understood. 'Blood vessel' for dhamanī is probable; whether arteries in "
               "particular are meant is disputed: no question on it. The count is as printed."),
    "explain_hi": ("यह दो शब्दों की गद्य-पंक्ति धमनियों का प्रकरण शुरू करती है: धमनियाँ तो चौबीस हैं। "
                   "‘तु’ (तो) इसे पहले की बात से अलग करता है। "
                   "धमनी का अर्थ नली या वाहिका है; रक्तवाहिका सम्भावित पहचान है, और क्या विशेष रूप से धमनी (आर्टरी) अभिप्रेत है, यह विवादित है। "
                   "‘चतुर्विंशति’ = चतुर् (चार) + विंशति (बीस)। "
                   "सन्धि: धमन्यः + तु → धमन्यस्तु, त से पहले विसर्ग स् बना।"),
    "hook": "धमनियाँ: चौबीस।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 44, how many dhamanīs are there?",
            ("Twenty-four", "धमन्यस्तु चतुर्विंशतिः: the dhamanīs are twenty-four."),
            [("Seven hundred", "Seven hundred is the count of the sirās (unit 4), not of the dhamanīs."),
             ("Forty-two", "चतुर्विंशति is four and twenty, not forty-two."),
             ("Fourteen", "Fourteen would be चतुर्दश.")],
            "The dhamanīs, however, are twenty-four.",
            "धमन्यस्तु चतुर्विंशतिः."),
        match(1, "Match each word part of unit 44 to its meaning.",
              [["धमन्यः", "dhamanīs, vessels"], ["तु", "however"], ["चतुर्", "four"], ["विंशति", "twenty"]],
              "The dhamanīs, however, are four-and-twenty.",
              "धमन्यः, तु, चतुर्, विंशति."),
        fill(2, "By unit 44 the vessels counted as twenty-four are the ____ (type it in Devanagari or in English letters, e.g. dharma).",
             accepts("धमन्यः", None, "धमनी", "dhamanyah", "dhamani"),
             "धमन्यः (dhamanīs), nominative plural of धमनी.",
             "धमनी = vessel, channel (probably a blood vessel, probable); 24 of them.",
             "धमन्यस्तु चतुर्विंशतिः."),
        mcq("discriminate", 3, "Which split of धमन्यस्तु in unit 44 is right?",
            ("धमन्यः + तु", "Visarga before त becomes स्: धमन्यः + तु → धमन्यस्तु."),
            [("धमन्याः + तु", "That would give धमन्यास्तु, with a long आ."),
             ("धमन्यौ + तु", "औ stays before a consonant: धमन्यौ तु."),
             ("धमन्य + स्तु", "स्तु is not a word here; the स् comes from the visarga.")],
            "धमन्यः (dhamanīs) + तु (however): visarga before त → स्.",
            "Visarga before त → स्."),
        mcq("apply", 4, "By unit 44 and its data, what is a dhamanī?",
            ("A vessel, probably a blood vessel", "Data: dhamanī = vessel or channel; blood vessel is probable."),
            [("A bone that forms a joint", "Bones and joints are not meant; dhamanī is a vessel."),
             ("A sense organ of the head", "No sense organ is meant; dhamanī is a vessel."),
             ("A part of the large intestine", "No organ is meant; dhamanī is a vessel.")],
            "धमनी = a vessel or channel, probably a blood vessel (probable).",
            "धमन्यः = vessels (probable: blood vessels)."),
        mcq("transfer", 5, "By the pattern of चतुर्विंशतिः (four + twenty), what does पञ्चविंशतिः mean in a new example?",
            ("Twenty-five", "पञ्च (five) + विंशति (twenty) = 25, as चतुर् + विंशति = 24."),
            [("Fifteen", "Fifteen is पञ्चदश; विंशति is twenty."),
             ("Fifty-two", "The unit number comes first and is added to twenty."),
             ("Five twenties", "The parts are added, not multiplied.")],
            "पञ्चविंशतिः = 25, as चतुर्विंशतिः = 24.",
            "unit number + विंशति = that number plus twenty.",
            teaches="A unit number before विंशति is added to twenty: चतुर्विंशतिः = 4 + 20 = 24."),
    ],
}

# ---------------------------------------------------------------- unit 45
AUTHORED["45"] = {
    "title": "आराम इव · केदार इव",
    "question": "By unit 45, how do the dhamanīs act on the body, and with what two similes?",
    "rule": ("By them (ताभिः, the dhamanīs) this body (कायोऽयम्) is moistened (उपस्निह्यति), like a garden (आराम) by "
             "water-carrying ones and like a field (केदार) by canals (कुल्या)."),
    "limits": ("Prose. 'Water-carrying ones' (जलहारिणीभिः) qualifies an unstated feminine noun. The unit compares; it does "
               "not say how far the dhamanīs reach or what they carry besides moisture."),
    "explain_hi": ("यह गद्य-पंक्ति धमनियों का काम एक उपमा से समझाती है। "
                   "उनसे (ताभिः, इकाई ४४ की धमनियों से) यह शरीर आर्द्र होता है, जैसे जल ले जाने वालियों से उद्यान, और जैसे कुल्याओं यानी नहरों से खेत। "
                   "यानी शरीर उद्यान या खेत की जगह है और धमनियाँ नहरों की जगह। "
                   "‘उपस्निह्यति’ कर्तृवाच्य रूप है (आर्द्र होता है); हिन्दी-अंग्रेज़ी में ‘सींचा जाता है’ जैसा भाव स्वाभाविक है। "
                   "सन्धि: कायः + अयम् → कायोऽयम् (अः + अ → ओ, अवग्रह); आरामः + इव → आराम इव।"),
    "hook": "नहरें खेत को, धमनियाँ शरीर को सींचती हैं।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "In the simile of unit 45, by what is a field (kedāra) moistened?",
            ("By canals (kulyā)", "केदार इव कुल्याभिः: like a field by canals."),
            [("By clouds (megha)", "No clouds are named; the field is moistened by canals."),
             ("By wells (kūpa)", "No wells are named; the field is moistened by canals."),
             ("By rivers (nadī)", "No rivers are named; the field is moistened by canals.")],
            "Like a field by canals (kulyā).",
            "केदार इव कुल्याभिः."),
        order(1, "Put these phrases of unit 45 in the line's order.",
              ["ताभिः", "कायोऽयम्", "आराम इव जलहारिणीभिः", "केदार इव कुल्याभिः", "उपस्निह्यति"],
              "By them this body, like a garden by water-carrying ones, like a field by canals, is moistened.",
              "ताभिः → कायोऽयम् → आराम इव जलहारिणीभिः → केदार इव कुल्याभिः → उपस्निह्यति."),
        match(2, "Match each word of unit 45 to its meaning.",
              [["कायः", "body"], ["आरामः", "garden"], ["जलहारिणी", "water-carrying (one)"], ["केदारः", "field"],
               ["कुल्या", "canal"], ["उपस्निह्यति", "becomes moist"]],
              "By them the body is moistened, like a garden by water-carriers, like a field by canals.",
              "कायः, आरामः, जलहारिणी, केदारः, कुल्या, उपस्निह्यति.", role="extend",
              teaches="इव (like) follows the thing compared: आराम इव = like a garden; the instrumentals say by what."),
        mcq("discriminate", 3, "Which split of कायोऽयम् in unit 45 is right?",
            ("कायः + अयम्", "अः before अ becomes ओ and the अ is marked ऽ: कायः + अयम् → कायोऽयम्."),
            [("काया + यम्", "यम् is not the word here; the word is अयम् (this)."),
             ("कायो + अयम्", "कायो is not a word; the ओ comes from the visarga of कायः."),
             ("कायम् + अयम्", "म् before a vowel would give कायमयम्.")],
            "कायः (body) + अयम् (this): अः + अ → ओऽ.",
            "अः + अ → ओऽ."),
        mcq("apply", 4, "In the simile of unit 45, what is to the body as the canals are to the field?",
            ("The dhamanīs (ताभिः, by them)", "ताभिः = by them, the dhamanīs of unit 44: they moisten the body."),
            [("The garden (आरामः) itself", "The garden is another thing moistened, like the body."),
             ("The field (केदारः) itself", "The field is moistened by the canals; it is not the means."),
             ("This body (कायः) itself", "The body is what is moistened, not the means.")],
            "Canals : field = dhamanīs : body.",
            "ताभिः कायोऽयम् ... उपस्निह्यति."),
        mcq("transfer", 5, "By the rule of कायः + अयम् → कायोऽयम्, how is रामः + अयम् (this Rāma) joined in a new example?",
            ("रामोऽयम्", "अः before अ becomes ओ and the अ is marked ऽ, as कायः + अयम् → कायोऽयम्."),
            [("राम अयम्", "The gap comes before vowels other than अ; before अ it is ओऽ."),
             ("रामायम्", "No long आ arises; the visarga gives ओ."),
             ("रामरयम्", "र् comes from a visarga after vowels other than अ and आ.")],
            "रामः + अयम् = रामोऽयम्, like कायः + अयम् = कायोऽयम्.",
            "अः + अ → ओऽ.",
            teaches="अः before अ gives ओ, and the अ is dropped and marked with ऽ: कायः + अयम् → कायोऽयम्."),
    ],
}

# ---------------------------------------------------------------- unit 46
AUTHORED["46"] = {
    "title": "ताभिश्च नाभिश्चक्रनाभि...",
    "question": "By unit 46, what is surrounded by the dhamanīs?",
    "rule": ("And by them (ताभिश्च, the dhamanīs) the navel (नाभिः) is surrounded (आवृता); the simile 'like the hub "
             "of a wheel (चक्रनाभिः) by its spokes' rests on a conjectural reading."),
    "limits": ("Low confidence. The printed 'āraikariva' is not a word; 'like by spokes' (अरैरिव) is a conjectural "
               "restoration: no question on it. The copula is understood. The line does not count the dhamanīs."),
    "explain_hi": ("इस गद्य-पंक्ति का निश्चित भाग है: और उनसे (धमनियों से) नाभि घिरी हुई है। "
                   "अनुमानित पाठ पर इसके साथ उपमा है: जैसे चक्र की नाभि (पहिये की धुरी) अरों से घिरी हो। "
                   "छपा ‘आरैकरिव’ कोई शब्द नहीं बनता; ‘अरैरिव’ (अरों से जैसे) अनुमानित पाठ है, जो पहिये की उपमा से मेल खाता है। "
                   "इसलिए इस इकाई का विश्वास कम है और उस भाग पर कोई प्रश्न नहीं। "
                   "‘आवृता’ स्त्रीलिंग है और स्त्रीलिंग ‘नाभिः’ से मेल खाता है। "
                   "सन्धि: ताभिः + च → ताभिश्च (च से पहले विसर्ग → श्)।"),
    "hook": "नाभि धमनियों से घिरी (पहिये की धुरी जैसी: अनुमानित पाठ)।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 46, what is surrounded by them (the dhamanīs)?",
            ("The navel (nābhi)", "ताभिश्च नाभिः ... आवृता: and by them the navel is surrounded."),
            [("The heart (hṛdaya)", "The heart is not named in unit 46."),
             ("The head (śiras)", "The head is not named in unit 46."),
             ("The breasts (stana)", "The breasts are not named in unit 46.")],
            "And by them the navel is surrounded.",
            "ताभिश्च नाभिः ... आवृता."),
        match(1, "Match each sure word of unit 46 to its meaning.",
              [["ताभिः", "by them"], ["च", "and"], ["नाभिः", "navel"], ["चक्रनाभिः", "hub of a wheel"],
               ["आवृता", "surrounded"]],
              "And by them the navel is surrounded; cakranābhi = hub of a wheel (the simile rests on a conjectural reading).",
              "ताभिः, च, नाभिः, चक्रनाभिः, आवृता."),
        fill(2, "By unit 46 the ____ (navel) is surrounded by the dhamanīs (type it in Devanagari or in English letters, e.g. dharma).",
             accepts("नाभिः", None, "नाभि", "nabhi"),
             "नाभिः = the navel (f. nom. sg.).",
             "नाभि = navel; चक्रनाभि = hub of a wheel.",
             "ताभिश्च नाभिः ... आवृता.", role="extend"),
        mcq("discriminate", 3, "Which split of ताभिश्च in unit 46 is right?",
            ("ताभिः + च", "A visarga before च becomes श्: ताभिः + च → ताभिश्च."),
            [("ताभ्यः + च", "That would give ताभ्यश्च."),
             ("ताभिर् + च", "A visarga before च becomes श्, not र्."),
             ("ताभि + श्च", "श्च is not a word; the श् comes from the visarga.")],
            "ताभिः (by them) + च (and): visarga before च → श्.",
            "Visarga before च → श्."),
        multi("apply", 4, "Which statements fit unit 46 and its data?",
              [("आवृता agrees with the feminine नाभिः", "Right: data note: āvṛtā agrees with nābhiḥ (feminine)."),
               ("The line says the navel is moistened", "Moistening is said of the body in unit 45, not here."),
               ("चक्रनाभि is the hub of a wheel", "Right: cakranābhi is taken as the hub of a wheel."),
               ("The line counts the dhamanīs", "No number is printed in unit 46.")],
              [0, 2],
              "By them the navel is surrounded (आवृता, f.); cakranābhi = hub of a wheel (the simile is a conjectural reading).",
              "ताभिश्च नाभिश्चक्रनाभि... आवृता."),
        mcq("transfer", 5, "By the rule of ताभिः + च → ताभिश्च, how is रामः + च (and Rāma) joined in a new example?",
            ("रामश्च", "A visarga before च becomes श्, as ताभिः + च → ताभिश्च."),
            [("रामो च", "ओ comes from अः before a voiced consonant; च is not voiced."),
             ("राम च", "The visarga does not drop before च; it becomes श्."),
             ("रामस्च", "स् comes before त or थ; before च it is श्.")],
            "रामः + च = रामश्च, like ताभिः + च = ताभिश्च.",
            "Visarga before च → श्.",
            teaches="A visarga before च or छ becomes श्: ताभिः + च → ताभिश्च, नाभिः + चक्र... → नाभिश्चक्र...."),
    ],
}

# ---------------------------------------------------------------- unit 47
AUTHORED["47"] = {
    "title": "तस्मान्नाभ्यां · दशाधश्चतस्रस्तिर्यक्",
    "question": "By unit 47, where are the prāṇas especially established, and how many dhamanīs go downward and crosswise?",
    "rule": ("Therefore the prāṇas (vital breaths) are established especially in the navel (नाभ्याम्). Of those dhamanīs, "
             "ten go downward (दशाधः) and four crosswise (चतस्रस्तिर्यक्); 'ten upward' rests on a conjectural reading."),
    "limits": ("Low confidence; two printed lines. Three readings are conjectural: सा अन्तर् ('it within'), दश ऊर्ध्वम् "
               "('ten upward', printed ddhaśaurdhvaṃ) and प्रसृताः ('spread', printed pramṛtā): no question on them. The "
               "'yataḥ' clause has no main clause here (grouping note)."),
    "explain_hi": ("पहली छपी पंक्ति का निश्चित भाग: इस कारण नाभि में विशेष रूप से प्राण स्थित हैं। "
                   "आगे ‘यतश्च’ (और क्योंकि) वाला वाक्य अधूरा है; ‘सा अन्तर् अपि अधिष्ठानम्’ (वह भीतर भी आधार है) अनुमानित पाठ है। "
                   "दूसरी पंक्ति: उन धमनियों में दस नीचे की ओर और चार तिरछी हैं; ‘दस ऊपर की ओर फैली’ छपे ‘द्धशौर्ध्वं प्रमृता’ का अनुमानित पाठ है। "
                   "यह अनुमान इकाई ४४ के कुल चौबीस से मेल खाता है: १० + १० + ४। "
                   "‘चतस्रः’ स्त्रीलिंग ‘चार’ है, क्योंकि धमनी स्त्रीलिंग है।"),
    "hook": "प्राण विशेषकर नाभि में; धमनियाँ: दस नीचे, चार तिरछी (ऊपर दस, अनुमानित पाठ)।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 47, where are the prāṇas (vital breaths) especially established?",
            ("In the navel (nābhi)", "तस्मान्नाभ्यां विशेषेण प्राणा व्यवस्थिताः."),
            [("In the joints (sandhi)", "The joints are not named in unit 47."),
             ("In the eyes (netra)", "The eyes are not named in unit 47."),
             ("In the feet (pāda)", "The feet are not named in unit 47.")],
            "Therefore the prāṇas are established especially in the navel.",
            "तस्मान्नाभ्यां विशेषेण प्राणा व्यवस्थिताः."),
        order(1, "Put the words of the first clause of unit 47 in the line's order.",
              ["तस्मात्", "नाभ्याम्", "विशेषेण", "प्राणाः", "व्यवस्थिताः"],
              "Therefore, in the navel, especially, the prāṇas, are established.",
              "तस्मात् → नाभ्याम् → विशेषेण → प्राणाः → व्यवस्थिताः."),
        match(2, "Match each sure word of unit 47 to its meaning.",
              [["नाभ्याम्", "in the navel"], ["विशेषेण", "especially"], ["प्राणाः", "vital breaths"],
               ["व्यवस्थिताः", "established, situated"], ["अधः", "downward"], ["तिर्यक्", "crosswise"]],
              "The prāṇas are established especially in the navel; ten go downward, four crosswise.",
              "नाभ्याम्, विशेषेण, प्राणाः, व्यवस्थिताः, अधः, तिर्यक्.", role="extend",
              teaches="नाभ्याम् is the locative singular of the feminine नाभि (in the navel)."),
        mcq("discriminate", 3, "By unit 47, how many of the dhamanīs run crosswise (tiryak)?",
            ("Four", "चतस्रस्तिर्यक्: four crosswise."),
            [("Ten", "Ten is the number going downward (दशाधः)."),
             ("Two", "चतस्रः is four, not two."),
             ("Twenty-four", "Twenty-four is the total of unit 44.")],
            "Ten downward, four crosswise.",
            "दशाधश्चतस्रस्तिर्यक्."),
        multi("apply", 4, "Which statements fit the sure parts of unit 47?",
              [("Ten go downward", "Right: दशाधः = दश + अधः."),
               ("The line names the heart", "The heart is not named in unit 47."),
               ("Four run crosswise", "Right: चतस्रस्तिर्यक्."),
               ("The prāṇas are especially in the navel", "Right: नाभ्यां विशेषेण प्राणा व्यवस्थिताः.")],
              [0, 2, 3],
              "Prāṇas especially in the navel; ten downward, four crosswise.",
              "तस्मान्नाभ्यां ...; ... दशाधश्चतस्रस्तिर्यक्."),
        mcq("transfer", 5, "By the pattern of चतस्रः (four, with the feminine dhamanīs), how are four rivers (नदी, f.) named in a new example?",
            ("चतस्रो नद्यः", "चतस्रः is the feminine 'four'; अः before the voiced न becomes ओ."),
            [("चत्वारो नद्यः", "चत्वारः is the masculine 'four'; नदी is feminine."),
             ("चत्वारि नद्यः", "चत्वारि is the neuter 'four'; नदी is feminine."),
             ("चतुरो नद्यः", "चतुरः is the masculine accusative 'four'.")],
            "चतस्रो नद्यः = four rivers, as चतस्रः (धमन्यः) = four (dhamanīs).",
            "'Four' agrees in gender: m. चत्वारः, f. चतस्रः, n. चत्वारि.",
            teaches="The numeral 'four' takes the gender of its noun: चतस्रः goes with the feminine dhamanīs."),
    ],
}

# ---------------------------------------------------------------- unit 48
AUTHORED["48"] = {
    "title": "ततस्ताभिर्यथास्वं · तासामूर्ध्वगा",
    "question": "By unit 48, what do the dhamanīs do for the limbs, and what happens to the upward-going ones at the heart?",
    "rule": ("By them (ताभिः) the limbs and parts, each according to its own, are held (धार्यन्ते) and nourished "
             "(आप्याय्यन्ते). The upward-going ones (ऊर्ध्वगाः), having reached the heart (हृदयम्), each become threefold "
             "(त्रिधा जायन्ते)."),
    "limits": ("Two printed lines, prose. The three kinds are not named in this unit (unit 49 counts thirty). The "
               "printed अंगवयवा lacks the long आ of अङ्गावयवाः (flagged, possible); no question on that join."),
    "explain_hi": ("पहली छपी पंक्ति: तब उन धमनियों से अपने-अपने अनुसार अंग और अवयव धारण किए जाते हैं और पुष्ट किए जाते हैं। "
                   "‘धार्यन्ते’ और ‘आप्याय्यन्ते’ कर्मवाच्य रूप हैं (आप्याय्यन्ते णिजन्त कर्मवाच्य)। "
                   "दूसरी पंक्ति: उनमें से ऊपर जाने वाली हृदय तक पहुँचकर प्रत्येक तीन प्रकार की हो जाती हैं; ‘जायन्ते’ आत्मनेपद है, कर्मवाच्य नहीं। "
                   "तीन प्रकार यहाँ गिनाए नहीं गए; अगली इकाई तीस की गिनती देती है। "
                   "छपे ‘अंगवयवा’ में अङ्ग + अवयव का आ छूटा दिखता है (अङ्गावयवाः अपेक्षित)।"),
    "hook": "धमनियाँ अंगों को थामें और पोसें; ऊपर वाली हृदय पर तीन-तीन हो जाएँ।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 48, what do the upward-going ones reach?",
            ("The heart (hṛdaya)", "तासामूर्ध्वगा हृदयमभिप्रपन्नाः: the upward ones reach the heart."),
            [("The joints (sandhi)", "The joints are not named in unit 48."),
             ("The soles (pādatala)", "The soles are not named in unit 48."),
             ("The large intestine (sthūlāntra)", "The large intestine is not named in unit 48.")],
            "The upward-going ones, having reached the heart, each become threefold.",
            "तासामूर्ध्वगा हृदयमभिप्रपन्नाः."),
        order(1, "Put these words of the second line of unit 48 in the line's order.",
              ["ऊर्ध्वगाः", "हृदयम्", "अभिप्रपन्नाः", "प्रत्येकम्", "त्रिधा जायन्ते"],
              "The upward-going, the heart, having reached, each, become threefold.",
              "ऊर्ध्वगा → हृदयम् → अभिप्रपन्नाः → प्रत्येकं → त्रिधा जायंते."),
        match(2, "Match each word of the first line of unit 48 to its meaning.",
              [["धार्यन्ते", "are held, supported"], ["आप्याय्यन्ते", "are nourished"], ["अङ्ग", "limb"],
               ["अवयव", "part"], ["यथास्वम्", "each according to its own"]],
              "By them the limbs and parts, each according to its own, are held and nourished.",
              "धार्यन्ते, आप्याय्यन्ते, अङ्ग, अवयव, यथास्वम्.", role="extend",
              teaches="धार्यन्ते and आप्याय्यन्ते are passive: the limbs are held and nourished; ताभिः (by them) is the agent."),
        mcq("discriminate", 3, "Which verb of unit 48 is NOT passive?",
            ("जायन्ते (come to be)", "जायन्ते is a middle form of √जन्: an -यन्ते form that is not passive."),
            [("धार्यन्ते (are held)", "धार्यन्ते is passive (3 pl. pres. pass. √धृ)."),
             ("आप्याय्यन्ते (are nourished)", "आप्याय्यन्ते is passive (causative passive of आ-√प्याय्).")],
            "-यन्ते is not always passive: जायन्ते is middle; धार्यन्ते and आप्याय्यन्ते are passive.",
            "Check the grammar label: जायते is middle, not passive."),
        mcq("apply", 4, "By unit 48, what happens to each upward-going one after it reaches the heart?",
            ("It comes to be threefold", "प्रत्येकं त्रिधा जायंते: each becomes threefold."),
            [("It joins the others in one", "Nothing is said of joining; each becomes threefold."),
             ("It turns back to the navel", "Nothing is said of turning back; each becomes threefold."),
             ("It runs on, crosswise, alone", "Nothing is said of running crosswise; each becomes threefold.")],
            "Each upward-going one, having reached the heart, becomes threefold.",
            "प्रत्येकं त्रिधा जायंते."),
        mcq("transfer", 5, "By the pattern of त्रिधा (threefold), what does पञ्चधा mean in a new example?",
            ("Fivefold", "-धा on a number = in so many ways: त्रिधा threefold, पञ्चधा fivefold."),
            [("The fifth", "The fifth is पञ्चम."),
             ("Fifty", "Fifty is पञ्चाशत्."),
             ("Fifteen", "Fifteen is पञ्चदश.")],
            "पञ्चधा = fivefold, as त्रिधा = threefold.",
            "number + -धा = in so many ways, so-many-fold.",
            teaches="-धा added to a number means 'in so many ways': त्रिधा = threefold."),
    ],
}

# ---------------------------------------------------------------- unit 49
AUTHORED["49"] = {
    "title": "ततस्त्रिंशतो मध्ये द्वे द्वे",
    "question": "By unit 49, what do two and two of the thirty carry?",
    "rule": ("Then, among the thirty (त्रिंशतः मध्ये), two and two (द्वे द्वे) carry Vāta, Pitta, Kapha, blood and rasa "
             "(the nutrient fluid)."),
    "limits": ("Prose; no finite verb, only a participle. The printed वहंतः is masculine against the feminine द्वे द्वे "
               "(flagged; वहन्त्यः or वहतः are possible): no question on that form. 'Two each' over the five items is "
               "the data's reading. The list continues in units 50-51 (grouping note)."),
    "explain_hi": ("यह गद्य-पंक्ति ‘तीस’ गिनकर उनका बँटवारा शुरू करती है; इकाई ४८ में ऊपर जाने वाली धमनियाँ हृदय तक पहुँचकर प्रत्येक तीन प्रकार की होती हैं। "
                   "तीस में से दो-दो वात, पित्त, कफ, रक्त और रस का वहन करती हैं; डेटा ‘द्वे द्वे’ को पाँचों में दो-दो पढ़ता है, यानी दस। "
                   "यहाँ ‘रस’ पोषक द्रव (धातु) है, स्वाद नहीं। "
                   "छपा ‘वहंतः’ पुंलिंग है, जबकि ‘द्वे द्वे’ स्त्रीलिंग; इसलिए ‘वहन्त्यः’ या ‘वहतः’ सम्भावित सुधार बताए गए हैं। "
                   "सन्धि: त्रिंशतः + मध्ये → त्रिंशतो मध्ये (अः + घोष व्यंजन → ओ)।"),
    "hook": "तीस में से दो-दो: वात, पित्त, कफ, रक्त, रस।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 49, how many of the thirty carry each of Vāta, Pitta, Kapha, blood and rasa?",
            ("Two each", "द्वे द्वे: two and two, read as two for each item."),
            [("One each", "The numeral is द्वे (two), repeated."),
             ("Three each", "The numeral is द्वे (two), not three."),
             ("Ten each", "Ten is the sum of all five pairs, not each.")],
            "Two and two carry Vāta, Pitta, Kapha, blood and rasa.",
            "द्वे द्वे वातपित्तकफरक्तरसान्..."),
        order(1, "Put the five carried things in the order of unit 49.",
              ["वात", "पित्त", "कफ", "रक्त", "रस"],
              "Vāta, Pitta, Kapha, blood, rasa.",
              "वात → पित्त → कफ → रक्त → रस."),
        match(2, "Match each word of unit 49 to its meaning.",
              [["त्रिंशतः", "of the thirty"], ["मध्ये", "among"], ["द्वे द्वे", "two and two"],
               ["रक्त", "blood"], ["रस", "nutrient fluid (rasa)"]],
              "Then, among the thirty, two and two carry Vāta, Pitta, Kapha, blood and rasa.",
              "त्रिंशतः, मध्ये, द्वे द्वे, रक्त, रस.", role="extend",
              teaches="त्रिंशतः मध्ये: a genitive with मध्ये = among (the thirty)."),
        mcq("discriminate", 3, "In unit 49, what does रस mean?",
            ("The nutrient fluid, a dhātu", "Data: rasa here is the nutrient fluid (dhātu), not taste."),
            [("Taste, one of the sense-objects", "Rasa as taste is unit 50; here it is the nutrient fluid."),
             ("A juice pressed out of a plant", "No plant is meant; rasa here is the nutrient fluid."),
             ("The sweat that comes on the skin", "Sweat is not meant; rasa here is the nutrient fluid.")],
            "रस in unit 49 = the nutrient fluid (dhātu), not taste.",
            "रस with वात, पित्त, कफ, रक्त = the nutrient fluid."),
        mcq("apply", 4, "On the data's reading of द्वे द्वे, how many of the thirty go to these five things?",
            ("Ten", "Two for each of five items: 2 × 5 = 10 (data note: 10 + 8 + 8 + 4 = 30)."),
            [("Five", "Each item has two, not one."),
             ("Two", "द्वे द्वे is repeated: two for each item."),
             ("Thirty", "Thirty is the whole; the five pairs make ten of it.")],
            "Two each for five items = ten of the thirty.",
            "द्वे द्वे × 5 = 10."),
        mcq("transfer", 5, "By the rule of त्रिंशतः + मध्ये → त्रिंशतो मध्ये, how is नरः + गच्छति (the man goes) joined in a new example?",
            ("नरो गच्छति", "अः before a voiced consonant becomes ओ, as त्रिंशतः + मध्ये → त्रिंशतो मध्ये."),
            [("नर गच्छति", "The visarga after अ does not just drop before a voiced consonant; it gives ओ."),
             ("नरा गच्छति", "आ comes from आः losing its visarga; here it is अः."),
             ("नरर्गच्छति", "र् comes from a visarga after vowels other than अ and आ.")],
            "नरः + गच्छति = नरो गच्छति, like त्रिंशतः + मध्ये = त्रिंशतो मध्ये.",
            "अः + voiced consonant → ओ.",
            teaches="अः before a voiced consonant becomes ओ: त्रिंशतः + मध्ये → त्रिंशतो मध्ये."),
    ],
}

# ---------------------------------------------------------------- unit 50
AUTHORED["50"] = {
    "title": "अष्टाभिः शब्दरूपरसगंधा गृह्यंते",
    "question": "By unit 50, what is grasped by eight?",
    "rule": ("By eight (अष्टाभिः) sound, form, taste and smell (शब्दरूपरसगन्धाः) are grasped, perceived (गृह्यन्ते)."),
    "limits": ("Prose. Only four sense-objects are listed; touch is not named in this line. The unit does not say how "
               "the eight are shared among the objects. The line continues the count of unit 49 (grouping note)."),
    "explain_hi": ("यह गद्य-पंक्ति तीस की गिनती आगे बढ़ाती है: आठ से शब्द, रूप, रस यानी स्वाद और गन्ध ग्रहण किए जाते हैं। "
                   "यहाँ ‘रस’ स्वाद है, इकाई ४९ वाला पोषक द्रव नहीं। "
                   "केवल चार विषय गिनाए गए हैं; स्पर्श इस पंक्ति में नहीं है। "
                   "‘गृह्यन्ते’ कर्मवाच्य है: ग्रहण किए जाते हैं। "
                   "सन्धि: गन्धाः + गृह्यन्ते → गन्धा गृह्यन्ते (घोष व्यंजन से पहले आः का विसर्ग लुप्त)।"),
    "hook": "आठ से चार विषय: शब्द, रूप, रस, गन्ध (स्पर्श नहीं)।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 50, what is grasped by eight?",
            ("Sound, form, taste and smell", "अष्टाभिः शब्दरूपरसगंधा गृह्यंते."),
            [("Sound, touch, form and smell", "Touch is not named in unit 50."),
             ("Taste, smell, sleep and speech", "Sleep and speech are not in unit 50."),
             ("Tears, milk, form and taste", "Tears and milk are not in unit 50.")],
            "By eight, sound, form, taste and smell are grasped.",
            "अष्टाभिः शब्दरूपरसगंधा गृह्यंते."),
        order(1, "Put the sense-objects in the order of unit 50.",
              ["शब्द", "रूप", "रस", "गन्ध"],
              "Sound, form, taste, smell.",
              "शब्द → रूप → रस → गन्ध."),
        match(2, "Match each word of unit 50 to its meaning.",
              [["शब्द", "sound"], ["रूप", "form, visible appearance"], ["रस", "taste"], ["गन्ध", "smell"],
               ["गृह्यन्ते", "are grasped, perceived"]],
              "By eight, sound, form, taste and smell are grasped.",
              "शब्द, रूप, रस, गन्ध, गृह्यन्ते.", role="extend",
              teaches="गृह्यन्ते is passive of √ग्रह्: the objects are grasped; अष्टाभिः (by eight) is the agent."),
        mcq("discriminate", 3, "Which sense-object is NOT named in unit 50?",
            ("Touch (sparśa)", "Data note: touch is not named in this line."),
            [("Sound (śabda)", "शब्द is the first item of the list."),
             ("Form (rūpa)", "रूप is the second item of the list."),
             ("Smell (gandha)", "गन्ध is the last item of the list.")],
            "Sound, form, taste, smell are named; touch is not.",
            "शब्दरूपरसगन्धाः: four objects, no स्पर्श."),
        fill(4, "In unit 50 'smell' is ____ (type it in Devanagari or in English letters, e.g. dharma).",
             accepts("गन्ध", None, "गन्धाः", "gandha"),
             "गन्ध = smell, the last member of शब्दरूपरसगन्धाः.",
             "गन्ध = smell.",
             "शब्द, रूप, रस, गन्ध.", role="apply"),
        mcq("transfer", 5, "By the pattern of गृह्यन्ते (are grasped, passive), what does दृश्यन्ते mean in a new example?",
            ("They are seen", "दृश्यन्ते is the passive of √दृश्, as गृह्यन्ते of √ग्रह्."),
            [("They see", "'They see' is पश्यन्ति, an active form."),
             ("Having seen", "'Having seen' is दृष्ट्वा."),
             ("They will see", "'They will see' is द्रक्ष्यन्ति.")],
            "दृश्यन्ते = they are seen, like गृह्यन्ते = they are grasped.",
            "-यन्ते on these roots = passive 'are ...-ed'.",
            teaches="गृह्यन्ते is a passive (3 pl. pres.): are grasped, perceived."),
    ],
}

# ---------------------------------------------------------------- unit 51
AUTHORED["51"] = {
    "title": "द्वाभ्यां द्वाभ्यां · स्तनाश्रिते",
    "question": "By unit 51, what is done by two and two, and what do the last two pairs carry?",
    "rule": ("By two and two (द्वाभ्यां द्वाभ्याम्) one speaks, makes a sound (घोष), sleeps and wakes. Two carry tears "
             "(अश्रु); and two, resting on the breasts: a woman's milk (stanya), a man's semen (śukra)."),
    "limits": ("Two printed lines, prose. Two for each act (eight) is the data's reading of the repeated द्वाभ्याम्; "
               "which pair serves which act, and the subject, are unstated. The sense of ghoṣa beside 'speaks' is not "
               "fixed. For the breast pair 'carry' is understood."),
    "explain_hi": ("पहली छपी पंक्ति: दो-दो से बोलता है, घोष यानी ध्वनि करता है, सोता है और जागता है; डेटा इसे चार कामों में दो-दो, यानी आठ, पढ़ता है। "
                   "कौन-सी जोड़ी किस काम की है, और कर्ता कौन है, यह नहीं कहा गया। "
                   "दूसरी पंक्ति: दो आँसू वहन करती हैं; और स्तनों पर आश्रित दो: नारी का स्तन्य (दूध) और नर का शुक्र (वीर्य)। "
                   "डेटा के अनुसार ये अन्तिम चार हैं, और तीस पूरे होते हैं: १० + ८ + ८ + ४। "
                   "सन्धि: च + अश्रु → चाश्रु (अ + अ → आ)।"),
    "hook": "दो-दो से बोलना, ध्वनि, सोना, जागना; दो आँसू, दो स्तन पर: दूध या शुक्र।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 51, what do the two resting on the breasts carry?",
            ("A woman's milk; a man's semen", "नार्याः स्तन्यं नरस्य शुक्रं."),
            [("Tears in both woman and man", "Tears are carried by another two (द्वे चाश्रु वहतः)."),
             ("Food and water for the gut", "Food and water are not in unit 51."),
             ("Sweat and urine of the body", "Sweat and urine are not in unit 51.")],
            "Two, resting on the breasts: a woman's milk (stanya), a man's semen (śukra).",
            "द्वे च स्तनाश्रिते नार्याः स्तन्यं नरस्य शुक्रं."),
        order(1, "Put the four acts of the first line of unit 51 in the line's order.",
              ["भाषते", "घोषं करोति", "स्वपिति", "प्रतिबुध्यते"],
              "Speaks, makes a sound, sleeps, wakes.",
              "भाषते → घोषं करोति → स्वपिति → प्रतिबुध्यते."),
        match(2, "Match each word of unit 51 to its meaning.",
              [["भाषते", "speaks"], ["घोषम्", "sound, cry"], ["स्वपिति", "sleeps"], ["प्रतिबुध्यते", "wakes"],
               ["अश्रु", "tears"], ["स्तन्य", "breast-milk"]],
              "Speaks, makes a sound, sleeps, wakes; tears; breast-milk.",
              "भाषते, घोषम्, स्वपिति, प्रतिबुध्यते, अश्रु, स्तन्य.", role="extend",
              teaches="भाषते and प्रतिबुध्यते are middle (ātmanepada) present forms: speaks, wakes."),
        mcq("discriminate", 3, "Which split of चाश्रु in unit 51 is right?",
            ("च + अश्रु", "अ + अ → आ: च + अश्रु → चाश्रु."),
            [("चा + श्रु", "श्रु is not the word here; the word is अश्रु (tears)."),
             ("चे + अश्रु", "ए + अ would give चेऽश्रु, with ए kept."),
             ("च + श्रु", "With no vowel added, च + श्रु would give चश्रु, not चाश्रु.")],
            "च (and) + अश्रु (tears): अ + अ → आ.",
            "अ + अ → आ."),
        mcq("apply", 4, "On the data's reading of the repeated द्वाभ्याम्, how many serve speaking, sounding, sleeping and waking?",
            ("Eight, two for each act", "Data note: distributive, two for each of the four acts = eight."),
            [("Four, one for each act", "द्वाभ्याम् is 'by two', not 'by one'."),
             ("Ten, as for the doṣas", "Ten is the count of unit 49, not of these four acts."),
             ("Six, two for three acts", "Four acts are named: speaks, sounds, sleeps, wakes.")],
            "Two for each of the four acts = eight.",
            "द्वाभ्यां द्वाभ्याम् × 4 acts = 8 (data's reading)."),
        mcq("transfer", 5, "By the pattern of वहतः (the two carry), what form of √वद् means the two speak, in a new example?",
            ("वदतः", "-अतः marks the 3rd person dual present, as वहतः (the two carry)."),
            [("वदन्ति", "वदन्ति is plural: they (all) speak."),
             ("वदति", "वदति is singular: he speaks."),
             ("वदथः", "वदथः is 2nd person dual: you two speak.")],
            "वदतः = the two speak, like वहतः = the two carry.",
            "3rd person dual present: -अतः.",
            teaches="वहतः is 3rd person dual present: the two carry; so वद् → वदतः."),
    ],
}


# ===================================================================== NOTES_HI
NOTES_HI = {
    "39": ("गद्य; विश्वास मध्यम; दो छपी पंक्तियाँ (०२.०६.४१, ०२.०६.४२); कोई पाठ-चिह्न नहीं। पहली पंक्ति इकाई ३८ के १७५ के विभाग को "
           "पूरा करती दिखती है; हर प्रकार का अंश (चौथाई-चौथाई) केवल गणित से सुझता है, छपा नहीं। श्लेष्मन् = कफ (मानक)। ‘एवम्’ इस इकाई "
           "के बाहर के कथन की ओर संकेत करता है। सन्धि जाँची: एषः + विभागः → एष विभागः (एषः का विसर्ग व्यंजन से पहले लुप्त); रक्तेषु + "
           "अपि → रक्तेष्वपि (उ + अ → व); स्थिताः + हि → स्थिता हि (घोष से पहले आः का विसर्ग लुप्त); हि + एवम् → ह्येवम् (इ + ए → ये); "
           "देहम् + अनुगृह्णन्ति → देहमनुगृह्णन्ति।"),
    "40": ("गद्य; विश्वास मध्यम; कोई पाठ-चिह्न नहीं। अण्डाकार वाक्य: कर्ता (इकाई ३९ के दोष) और कर्म छपे नहीं, जोड़े नहीं गए। "
           "व्यत्यय = उलट, विपरीत (इकाई ३९ वाली अवस्था का)। छपा ‘पीडयंति’ = पीडयन्ति (अनुस्वार नासिक्य के स्थान पर)।"),
    "41": ("गद्य; विश्वास मध्यम; कोई पाठ-चिह्न नहीं। विशेषण स्त्रीलिंग बहुवचन हैं; संज्ञा (धमनी या सिरा) छपी नहीं, जोड़ी नहीं गई। "
           "‘वातरक्त’ = वात-प्रकार का रक्त, सम्भवतः रोग वातरक्त नहीं (सम्भावित)। सन्धि जाँची: श्याव + अरुणाः → श्यावारुणाः (अ + अ → आ); "
           "क्षणपूर्णरिक्ताः + वात... → क्षणपूर्णरिक्ता वात... (घोष से पहले आः का विसर्ग लुप्त)। डेटा का ‘क्षण-पूर्ण-रिक्त’ पर द्वन्द्व "
           "लेबल पूरी तरह सटीक नहीं लगता (क्षण क्रिया-विशेषण जैसा है); अर्थ पर प्रभाव नहीं।"),
    "42": ("गद्य; विश्वास मध्यम; दो छपी पंक्तियाँ (०२.०६.४५, ०२.०६.४६); कोई पाठ-चिह्न नहीं। ‘वहन्ति’ क्रिया इकाई ४१ से समझी जाती है; "
           "संज्ञा अनकही (‘वाली’)। असित = काला, साँवला; गौरी = गोरी (हल्की पीली-सफेद भी)। सन्धि जाँची: नील + पीत + असिताः → "
           "नीलपीतासिताः (अ + अ → आ); स्पर्श + उष्णाः → स्पर्शोष्णाः (अ + उ → ओ)। क्या स्रवित होता है, खुजली किसकी, यह नहीं कहा गया।"),
    "43": ("गद्य; विश्वास मध्यम; दो छपी पंक्तियाँ (०२.०६.४७, ०२.०६.४८); कोई पाठ-चिह्न नहीं। ‘वहन्ति’ इकाई ४१ से समझी जाती है। "
           "संसर्ग-सन्निपात को सामान्यतः दो और तीनों दोषों का मेल माना जाता है, पर पंक्ति गिनती नहीं करती। छपा ‘समागूढाः’ = समाः गूढाः "
           "(घोष से पहले आः का विसर्ग लुप्त; रिक्त स्थान छूटा); ‘स्निग्धा रोहिण्यः’ = स्निग्धाः रोहिण्यः। ‘रोहिणी’ का अर्थ यहाँ अनिश्चित, "
           "उस पर कोई प्रश्न नहीं। अन्त का ‘इति’ इकाई ४१-४३ की पाँच प्रकार की सूची पूरी करता है।"),
    "44": ("गद्य; विश्वास उच्च; कोई पाठ-चिह्न नहीं। क्रिया समझी जाती है। धमनी = नली, वाहिका; रक्तवाहिका सम्भावित, ‘आर्टरी’ विशेष रूप "
           "से अभिप्रेत है या नहीं, विवादित। संख्या २४ छपे अनुसार; इकाई ४७ के १० + १० + ४ से मेल (वहाँ ‘दस ऊपर’ अनुमानित पाठ है)। "
           "सन्धि जाँची: धमन्यः + तु → धमन्यस्तु (त से पहले विसर्ग → स्)।"),
    "45": ("गद्य; विश्वास उच्च; कोई पाठ-चिह्न नहीं। ‘ताभिः’ इकाई ४४ की धमनियों की ओर; ‘जलहारिणीभिः’ स्त्रीलिंग, संज्ञा अनकही। "
           "छपा ‘ताभिःकायो’ रिक्त स्थान की चूक है। सन्धि जाँची: कायः + अयम् → कायोऽयम् (अः + अ → ओऽ); अयम् + आरामः → अयमारामः; "
           "आरामः + इव → आराम इव, केदारः + इव → केदार इव (अः के बाद अ से भिन्न स्वर: विसर्ग लुप्त, अन्तर बना रहता है); कुल्याभिः + उप... → "
           "कुल्याभिरुप... (इ के बाद विसर्ग + स्वर → र्)। ‘उपस्निह्यति’ कर्तृवाच्य (आर्द्र होता है)।"),
    "46": ("गद्य; विश्वास कम। पाठ-चिह्न (सम्भावित): छपा ‘नाभिश्चक्रनाभिरारैकरिवावृता’ में ‘आरैकरिव’ शब्द नहीं बनता; ‘अरैरिव’ (अरों से "
           "जैसे) अनुमानित पाठ है, बीच का ‘क’ और दीर्घ आ छपाई की चूक लगते हैं; इस पर कोई प्रश्न नहीं। ‘आवृता’ स्त्रीलिंग ‘नाभिः’ से "
           "मेल खाता है। सन्धि जाँची: ताभिः + च → ताभिश्च, नाभिः + चक्र... → नाभिश्चक्र... (च से पहले विसर्ग → श्)।"),
    "47": ("गद्य; विश्वास कम; दो छपी पंक्तियाँ (०२.०६.५२, ०२.०६.५३)। तीन पाठ-चिह्न (सम्भावित): ‘सांऽतरप्यधिष्ठानं’ → सा अन्तर् अपि "
           "अधिष्ठानम् (अनुस्वार चूक लगता है; ‘सा’ = नाभि, अनुमान); ‘द्धशौर्ध्वं’ → दश ऊर्ध्वम्; ‘प्रमृता’ → प्रसृताः (प्रमृत = मरा हुआ, "
           "अर्थ नहीं बनता)। इन पर कोई प्रश्न नहीं। ‘यतः’ वाले उपवाक्य का मुख्य वाक्य इस इकाई में नहीं। छपा ‘विशेषेणप्राणा’ = विशेषेण "
           "प्राणाः (रिक्त स्थान की चूक)। सन्धि जाँची: तस्मात् + नाभ्याम् → तस्मान्नाभ्याम् (नासिक्य से पहले त् → न्); दश + अधः → दशाधः "
           "(अ + अ → आ); अधः + चतस्रः → अधश्चतस्रः (च से पहले विसर्ग → श्); चतस्रः + तिर्यक् → चतस्रस्तिर्यक् (त से पहले विसर्ग → स्)। "
           "डेटा के अंग्रेज़ी अनुवाद में दोनों वाक्यों के बीच पूर्ण-विराम छूटा है।"),
    "48": ("गद्य; विश्वास उच्च; दो छपी पंक्तियाँ (०२.०६.५४, ०२.०६.५५)। पाठ-चिह्न (सम्भावित): छपे ‘अंगवयवा’ में अङ्ग + अवयव का दीर्घ आ "
           "छूटा (अङ्गावयवाः अपेक्षित)। ‘ततः’ = तब, वहाँ से (‘इसलिए’ भी पढ़ा जा सकता है)। धार्यन्ते कर्मवाच्य, आप्याय्यन्ते णिजन्त "
           "कर्मवाच्य, जायन्ते आत्मनेपद (कर्मवाच्य नहीं)। सन्धि जाँची: ततः + ताभिः → ततस्ताभिः; ताभिः + यथास्वम् → ताभिर्यथास्वम् (इ के "
           "बाद विसर्ग + घोष → र्); अवयवाः + धार्यन्ते → अवयवा धार्यन्ते, ऊर्ध्वगाः + हृदयम् → ऊर्ध्वगा हृदयम् (आः का विसर्ग लुप्त)। "
           "तीन प्रकार इस इकाई में गिनाए नहीं गए।"),
    "49": ("गद्य; विश्वास मध्यम। पाठ-चिह्न (सम्भावित): छपा ‘वहंतः’ पुंलिंग है, स्त्रीलिंग ‘द्वे द्वे’ से मेल नहीं; ‘वहन्त्यः’ सुझाया गया, "
           "और ‘वहतः’ (द्विवचन क्रिया) भी सम्भव; इस पर कोई प्रश्न नहीं। ‘द्वे द्वे’ को पाँचों में दो-दो पढ़ा गया (१०)। रस = पोषक द्रव "
           "(धातु), स्वाद नहीं। सन्धि जाँची: ततः + त्रिंशतः → ततस्त्रिंशतः; त्रिंशतः + मध्ये → त्रिंशतो मध्ये (अः + घोष व्यंजन "
           "→ ओ)। सूची इकाई ५०-५१ में चलती है।"),
    "50": ("गद्य; विश्वास उच्च; कोई पाठ-चिह्न नहीं। केवल चार विषय; स्पर्श नहीं गिनाया गया। रूप = दिखने वाला रूप; रस = स्वाद। "
           "गृह्यन्ते कर्मवाच्य। सन्धि जाँची: गन्धाः + गृह्यन्ते → गन्धा गृह्यन्ते (घोष से पहले आः का विसर्ग लुप्त)। इकाई ४९ की गिनती आगे।"),
    "51": ("गद्य; विश्वास मध्यम; दो छपी पंक्तियाँ (०२.०६.५८, ०२.०६.५९); कोई पाठ-चिह्न नहीं। दोहराया ‘द्वाभ्याम्’ वितरणात्मक पढ़ा गया "
           "(चार कामों में दो-दो = आठ); कौन-सी जोड़ी किस काम की, और कर्ता कौन, नहीं कहा गया। घोष का ‘बोलता है’ के साथ ठीक अर्थ तय "
           "नहीं। दूसरी जोड़ी के लिए ‘वहतः’ समझा जाता है। छपा ‘नार्याःस्तन्यं’ = नार्याः स्तन्यम् (रिक्त स्थान की चूक)। सन्धि जाँची: च + "
           "अश्रु → चाश्रु (अ + अ → आ); स्तन + आश्रिते → स्तनाश्रिते (अ + आ → आ)।"),
}


# ===================================================================== AIDS
AIDS = {
    "39": {
        "frame": "भाग १: एष विभागः (यही बँटवारा) → कहाँ भी: पित्त, श्लेष्मा (कफ), शुद्ध रक्त में · भाग २: दोषाः (दोष) → स्थिताः एवम् (इस प्रकार टिके) → देहम् अनुगृह्णन्ति (शरीर को सहारा देते हैं)।",
        "chunks": "एष विभागः | पित्तश्लेष्मशुद्धरक्तेष्वपि || स्थिता ह्येवं | देहमनुगृह्णंति | दोषाः",
        "sandhi": "उ + भिन्न स्वर → व्: रक्तेषु + अपि → रक्तेष्वपि · इ + ए → ये: हि + एवम् → ह्येवम् · एषः का विसर्ग व्यंजन से पहले लुप्त: एष विभागः।",
    },
    "40": {
        "frame": "कब: व्यत्ययेन (उलटे होने पर) → तु (किन्तु) → क्या करते हैं: पीडयन्ति (पीड़ा देते हैं); कर्ता इकाई ३९ के दोष, छपे नहीं।",
        "chunks": "व्यत्ययेन | तु | पीडयंति",
        "anchors": "व्यत्यय ~ ‘उलट-पलट’: जो दोष इस प्रकार टिककर सहारा देते हैं, वही उलटे होकर पीड़ा देते हैं। (मेरी याद-पद्धति)",
    },
    "41": {
        "chunks": "तत्र | श्यावारुणाः | प्रस्पंदिन्यः | सूक्ष्माः | क्षणपूर्णरिक्ता | वातरक्तं वहंति",
        "sandhi": "अ + अ → आ: श्याव + अरुणाः → श्यावारुणाः · घोष से पहले आः का विसर्ग लुप्त: क्षणपूर्णरिक्ताः + वात... → क्षणपूर्णरिक्ता वात...।",
        "pegs": "मेरा बनाया चित्र: हवा से हिलती पतली नली, कभी भरी कभी खाली, रंग साँवला-लाल: वात-रक्त। (केवल याद की सहायता)",
    },
    "42": {
        "contrast": {"groups": [
            {"label": "पित्त-रक्त (पंक्ति १)", "items": ["नील, पीत, असित (नीली, पीली, काली)", "स्पर्शोष्ण (छूने में गरम)",
                                                    "क्षिप्रस्राविणी (जल्दी स्रवित)"]},
            {"label": "कफ-रक्त (पंक्ति २)", "items": ["गौरी (गोरी)", "स्निग्ध (चिकनी)", "स्थिर", "शीत (ठण्डी)",
                                                  "कण्डूमती (खुजली वाली)"]}]},
        "chunks": "नीलपीतासिताः | स्पर्शोष्णाः | क्षिप्रस्राविण्यः | पित्तरक्तं || गौर्यः | स्निग्धाः | स्थिराः | शीताः | कंडूमत्यः | कफरक्तं",
        "sandhi": "अ + उ → ओ: स्पर्श + उष्णाः → स्पर्शोष्णाः · अ + अ → आ: पीत + असिताः → पीतासिताः।",
    },
    "43": {
        "diagram": {"groups": [
            {"label": "रक्त के पाँच प्रकार, इकाई ४१-४३ (प्रकार: लक्षण)", "items": [
                "१ वात-रक्त (४१): श्याव-अरुण, फड़कती, सूक्ष्म, क्षण में भरी-खाली",
                "२ पित्त-रक्त (४२): नीली-पीली-काली, छूने में गरम, जल्दी स्रवित",
                "३ कफ-रक्त (४२): गोरी, चिकनी, स्थिर, ठण्डी, खुजली",
                "४ संसर्ग-सन्निपात-रक्त (४३): लक्षणों का मिश्रण",
                "५ शुद्ध रक्त (४३): समान, गूढ़, चिकनी, रोहिणी (अर्थ अनिश्चित)"]}]},
        "chunks": "लक्षणसंकरे | संसर्गसन्निपातरक्तं || समागूढाः | स्निग्धा | रोहिण्यः | शुद्धरक्तमिति",
        "sandhi": "घोष से पहले आः का विसर्ग लुप्त: समाः + गूढाः → समा गूढाः, स्निग्धाः + रोहिण्यः → स्निग्धा रोहिण्यः · म् + स्वर: शुद्धरक्तम् + इति → शुद्धरक्तमिति।",
    },
    "44": {
        "chunks": "धमन्यस्तु | चतुर्विंशतिः",
        "sandhi": "त से पहले विसर्ग → स्: धमन्यः + तु → धमन्यस्तु।",
        "frame": "कौन: धमन्यः (धमनियाँ, सम्भवतः रक्तवाहिकाएँ) → तु (तो) → कितनी: चतुर्-विंशति (४ + २० = २४)।",
    },
    "45": {
        "diagram": {"groups": [
            {"label": "उपमा: किससे → क्या आर्द्र होता है", "items": ["ताभिः (धमनियों से) → कायोऽयम् (यह शरीर)",
                                                              "जलहारिणीभिः (जल ले जाने वालियों से) → आराम (उद्यान)",
                                                              "कुल्याभिः (नहरों से) → केदार (खेत)"]}]},
        "chunks": "ताभिःकायोऽयमाराम इव | जलहारिणीभिः | केदार इव | कुल्याभिरुपस्निह्यति",
        "sandhi": "अः + अ → ओऽ: कायः + अयम् → कायोऽयम् · अः + अ से भिन्न स्वर → अ (अन्तर): आरामः + इव → आराम इव · इ के बाद विसर्ग + स्वर → र्: कुल्याभिः + उप... → कुल्याभिरुप...।",
    },
    "46": {
        "chunks": "ताभिश्च | नाभिश्चक्रनाभिरारैकरिवावृता",
        "sandhi": "च से पहले विसर्ग → श्: ताभिः + च → ताभिश्च, नाभिः + चक्र... → नाभिश्चक्र...।",
        "pegs": "मेरा बनाया चित्र: पहिये की धुरी, चारों ओर से घिरी; वैसे ही नाभि धमनियों से घिरी। पूरी उपमा अनुमानित पाठ पर है। (केवल याद की सहायता)",
    },
    "47": {
        "diagram": {"groups": [
            {"label": "धमनियों की दिशाएँ (इकाई ४७)", "items": ["ऊर्ध्व, ऊपर: दस (अनुमानित पाठ)", "अधः, नीचे: दस",
                                                       "तिर्यक्, तिरछी: चार", "कुल (इकाई ४४): चौबीस"]}]},
        "chunks": "तस्मान्नाभ्यां | विशेषेणप्राणा | व्यवस्थिताः || तासां खलु धमनीनां | द्धशौर्ध्वं प्रमृता | दशाधश्चतस्रस्तिर्यक्",
        "sandhi": "नासिक्य से पहले त् → न्: तस्मात् + नाभ्याम् → तस्मान्नाभ्याम् · अ + अ → आ: दश + अधः → दशाधः · च से पहले विसर्ग → श्: अधः + चतस्रः → अधश्चतस्रः · त से पहले विसर्ग → स्: चतस्रः + तिर्यक् → चतस्रस्तिर्यक्।",
    },
    "48": {
        "chain": {"steps": ["ताभिः: धमनियों से", "अङ्ग-अवयव धारण और पुष्ट होते हैं", "ऊर्ध्वगाः: ऊपर जाने वाली",
                            "हृदयम् अभिप्रपन्नाः: हृदय तक पहुँचकर", "प्रत्येकं त्रिधा: हर एक तीन प्रकार की"]},
        "chunks": "ततस्ताभिर्यथास्वमंगवयवा | धार्यंते | आप्याय्यंते च || तासामूर्ध्वगा | हृदयमभिप्रपन्नाः | प्रत्येकं | त्रिधाजायंते",
        "frame": "भाग १: ताभिः (उनसे) → अङ्गावयवाः (अंग-अवयव) → धार्यन्ते, आप्याय्यन्ते (थामे, पोसे जाते हैं) · भाग २: ऊर्ध्वगाः → हृदय तक → प्रत्येक त्रिधा।",
    },
    "49": {
        "diagram": {"groups": [
            {"label": "तीस में से दो-दो (डेटा का पाठ)", "items": ["वात: २", "पित्त: २", "कफ: २", "रक्त: २",
                                                          "रस (पोषक द्रव): २", "मिलाकर: १०"]}]},
        "chunks": "ततस्त्रिंशतो मध्ये | द्वे द्वे | वातपित्तकफरक्तरसान्वहंतः",
        "sandhi": "अः + घोष व्यंजन → ओ: त्रिंशतः + मध्ये → त्रिंशतो मध्ये · त से पहले विसर्ग → स्: ततः + त्रिंशतः → ततस्त्रिंशतः।",
    },
    "50": {
        "chunks": "अष्टाभिः | शब्दरूपरसगंधा | गृह्यंते",
        "frame": "किससे: अष्टाभिः (आठ से) → क्या: शब्द, रूप, रस, गन्ध (चार विषय, स्पर्श नहीं) → गृह्यन्ते (ग्रहण किए जाते हैं)।",
        "letters": "क्रम के पहले अक्षर: श-रू-र-ग (शब्द, रूप, रस, गन्ध)। (मेरी याद-पद्धति)",
    },
    "51": {
        "diagram": {"groups": [
            {"label": "तीस का बँटवारा, इकाई ४९-५१ (डेटा का पाठ)", "items": [
                "इकाई ४९: वात, पित्त, कफ, रक्त, रस: दो-दो = १०",
                "इकाई ५०: शब्द, रूप, रस, गन्ध: आठ",
                "इकाई ५१: बोलना, घोष, सोना, जागना: दो-दो = ८",
                "इकाई ५१: आँसू २, स्तनों पर २ = ४",
                "कुल: ३०"]}]},
        "chunks": "द्वाभ्यां द्वाभ्यां | भाषते | घोषं करोति | स्वपिति | प्रतिबुध्यते च || द्वे चाश्रु वहतः | द्वे च स्तनाश्रिते | नार्याःस्तन्यं | नरस्य शुक्रं",
        "sandhi": "अ + अ → आ: च + अश्रु → चाश्रु · अ + आ → आ: स्तन + आश्रिते → स्तनाश्रिते।",
    },
}


# ===================================================================== IMAGE_SPECS
IMAGE_SPECS = {
    ("42", "contrast"): {
        "file": "sh6-pitta-kapha-rakta-42.svg",
        "alt": ("Two columns of unit 42. Pitta-blood: blue, yellow and dark; warm to the touch; quickly discharging. "
                "Kapha-blood: fair; unctuous; steady; cold; itching."),
        "type": "split",
        "title": "इकाई ४२: पित्त-रक्त और कफ-रक्त",
        "cols": [["पित्त-रक्त", ["नीली, पीली, काली", "छूने में गरम", "जल्दी स्रवित"]],
                 ["कफ-रक्त", ["गोरी", "चिकनी (स्निग्ध)", "स्थिर", "ठण्डी", "खुजली वाली"]]],
    },
    ("43", "diagram"): {
        "file": "sh6-pancha-rakta-43.svg",
        "alt": ("Table of the five kinds of blood of units 41-43, in order: 1 Vāta-blood (dusky-brown and reddish, throbbing, "
                "fine, momentarily full and empty), 2 Pitta-blood (blue, yellow, dark, warm, quickly discharging), "
                "3 Kapha-blood (fair, unctuous, steady, cold, itching), 4 saṃsarga-sannipāta blood (signs mixed), "
                "5 pure blood (even, hidden, unctuous, rohiṇī, sense uncertain)."),
        "type": "table",
        "title": "इकाई ४१-४३: रक्त के पाँच प्रकार",
        "heads": ["प्रकार (इकाई)", "लक्षण"],
        "rows": [["१ वात-रक्त (४१)", "साँवली-लाल, फड़कती, सूक्ष्म, क्षण में भरी-खाली"],
                 ["२ पित्त-रक्त (४२)", "नीली-पीली-काली, छूने में गरम, जल्दी स्रवित"],
                 ["३ कफ-रक्त (४२)", "गोरी, चिकनी, स्थिर, ठण्डी, खुजली वाली"],
                 ["४ संसर्ग-सन्निपात (४३)", "लक्षणों का मिश्रण"],
                 ["५ शुद्ध रक्त (४३)", "समान, गूढ़, चिकनी, रोहिणी (अर्थ अनिश्चित)"]],
    },
    ("45", "diagram"): {
        "file": "sh6-kulya-upama-45.svg",
        "alt": ("Flowchart of the simile of unit 45: the dhamanīs moisten this body, as water-carrying ones a garden and "
                "canals a field."),
        "type": "mermaid",
        "code": ('flowchart TD\n'
                 '  A["धमनियाँ, ताभिः"] --> B["यह शरीर, कायः (आर्द्र होता है)"]\n'
                 '  C["जल ले जाने वालियाँ"] --> D["उद्यान, आरामः (जैसे)"]\n'
                 '  E["नहरें, कुल्याः"] --> F["खेत, केदारः (जैसे)"]\n'),
    },
    ("47", "diagram"): {
        "file": "sh6-dhamani-disha-47.svg",
        "alt": ("Table of the directions of the dhamanīs in unit 47: upward ten (conjectural reading), downward ten, "
                "crosswise four; total twenty-four (unit 44)."),
        "type": "table",
        "title": "इकाई ४७: धमनियों की दिशाएँ",
        "heads": ["दिशा", "संख्या"],
        "rows": [["ऊर्ध्व, ऊपर", "दस (अनुमानित पाठ)"], ["अधः, नीचे", "दस"], ["तिर्यक्, तिरछी", "चार"],
                 ["कुल (इकाई ४४)", "चौबीस"]],
    },
    ("48", "chain"): {
        "file": "sh6-urdhvaga-48.svg",
        "alt": ("Chain of unit 48: by the dhamanīs the limbs and parts are held and nourished; the upward-going ones reach "
                "the heart; each becomes threefold."),
        "type": "chain",
        "title": "इकाई ४८: ऊपर जाने वाली धमनियाँ",
        "steps": ["धमनियों से अंग-अवयव थामे और पोसे जाते हैं", "ऊपर जाने वाली धमनियाँ", "हृदय तक पहुँचकर",
                  "हर एक तीन प्रकार की"],
    },
    ("49", "diagram"): {
        "file": "sh6-dve-dve-49.svg",
        "alt": ("Table of unit 49 on the data's reading: two each of the thirty carry Vāta, Pitta, Kapha, blood and rasa "
                "(nutrient fluid); ten in all."),
        "type": "table",
        "title": "इकाई ४९: तीस में से दो-दो",
        "heads": ["क्या वहन करती हैं", "कितनी"],
        "rows": [["वात", "२"], ["पित्त", "२"], ["कफ", "२"], ["रक्त", "२"], ["रस, पोषक द्रव", "२"], ["मिलाकर", "१०"]],
    },
    ("51", "diagram"): {
        "file": "sh6-trimshat-51.svg",
        "alt": ("Table of the thirty on the data's reading, units 49-51: 10 for Vāta, Pitta, Kapha, blood, "
                "rasa; 8 for sound, form, taste, smell; 8 for speaking, sound, sleep, waking; 4 for tears and the breasts; "
                "total 30."),
        "type": "table",
        "title": "इकाई ४९-५१: तीस का बँटवारा (डेटा का पाठ)",
        "heads": ["काम (इकाई)", "संख्या"],
        "rows": [["वात, पित्त, कफ, रक्त, रस (४९)", "१०"], ["शब्द, रूप, रस, गन्ध (५०)", "८"],
                 ["बोलना, घोष, सोना, जागना (५१)", "८"], ["आँसू, स्तन (५१)", "४"], ["कुल", "३०"]],
    },
}
