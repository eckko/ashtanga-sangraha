from helpers import mcq, match, order, fill, multi, accepts


AUTHORED = {}

# ---------------------------------------------------------------- unit 41
AUTHORED["41"] = {
    "title": "भ्रुवोर्मध्ये स्थपनी",
    "question": "By unit 41, where is the sthapanī marma, and what is said of injury to it?",
    "rule": ("Between the two brows (भ्रुवोर्मध्ये) is the sthapanī; there it is 'as with the utkṣepa' (तत्रोत्क्षेपवत्): "
             "the outcome stated for the two utkṣepas in unit 40 holds here too."),
    "limits": ("Prose and elliptical: no verb is printed and none is supplied; injury is understood. The outcome is not "
               "restated here: उत्क्षेपवत् points back to unit 40 (one with the dart still in, or whose dart fell out "
               "through suppuration, may live; not one whose dart was pulled out)."),
    "explain_hi": ("यह छोटी गद्य-पंक्ति कहती है: दोनों भौंहों के बीच स्थपनी नामक मर्म है। "
                   "‘तत्रोत्क्षेपवत्’ = वहाँ उत्क्षेप के समान: आघात का जो फल इकाई ४० में दोनों उत्क्षेपों के लिए कहा गया, वही यहाँ भी। "
                   "इकाई ४० में कहा गया: शल्य भीतर रहे, या पक कर अपने-आप गिर जाए, तो रोगी जी सकता है; शल्य निकाल दिया जाए तो नहीं। "
                   "‘-वत्’ प्रत्यय का अर्थ है ‘के समान’। "
                   "कोई क्रिया छपी नहीं है, और आघात समझा जाता है।"),
    "hook": "भौंहों के बीच स्थपनी: फल उत्क्षेप जैसा।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 41, where is the sthapanī marma?",
            ("Between the two brows", "भ्रुवोर्मध्ये: in the middle of the two brows."),
            [("Below the tail-ends of the brows", "That is the place of the two apāṅgas (unit 38)."),
             ("Above the two śaṅkhas", "That is the place of the two utkṣepas (unit 40)."),
             ("In the hollows above the brows", "That is the place of the two āvartas (unit 39).")],
            "भ्रुवोर्मध्ये स्थपनी: the sthapanī is between the two brows.",
            "भ्रुवोः मध्ये = in the middle of the two brows."),
        order(1, "Put the printed phrases of unit 41 in the line's order.",
              ["भ्रुवोर्मध्ये", "स्थपनी", "तत्रोत्क्षेपवत्"],
              "Between the brows; the sthapanī; there, as with the utkṣepa.",
              "भ्रुवोर्मध्ये → स्थपनी → तत्रोत्क्षेपवत्."),
        match(2, "Match each word of unit 41 to its meaning.",
              [["भ्रुवोः", "of the two brows"], ["मध्ये", "in the middle"], ["स्थपनी", "name of a marma (a support)"],
               ["तत्र", "there"], ["उत्क्षेपवत्", "as with the utkṣepa"]],
              "भ्रुवोः मध्ये = between the two brows; स्थपनी = the marma; तत्र उत्क्षेपवत् = there, as with the utkṣepa.",
              "भ्रुवोः, मध्ये, स्थपनी, तत्र, उत्क्षेपवत्.", role="extend",
              teaches="The suffix -वत् means 'like, as with': उत्क्षेपवत् carries over what was said of the utkṣepas."),
        mcq("discriminate", 3, "Which split of तत्रोत्क्षेपवत् in unit 41 is right?",
            ("तत्र + उत्क्षेपवत्", "अ + उ → ओ: तत्र + उत्क्षेपवत् → तत्रोत्क्षेपवत्."),
            [("तत्रो + उत्क्षेपवत्", "तत्रो is not a word; the ओ comes from अ + उ."),
             ("तत्रः + उत्क्षेपवत्", "तत्रः is not a word; तत्र (there) is an indeclinable."),
             ("तत्र + ओत्क्षेपवत्", "ओत्क्षेप is not a word, and अ + ओ would give औ.")],
            "तत्र (there) + उत्क्षेपवत् (as with the utkṣepa): अ + उ → ओ.",
            "अ + उ → ओ."),
        mcq("apply", 4, "Why is भ्रुवोः printed भ्रुवोर् before मध्ये in unit 41?",
            ("After ओ, a visarga before a voiced sound becomes र्", "म is voiced: भ्रुवोः + मध्ये → भ्रुवोर्मध्ये."),
            [("After ओ, a visarga before any consonant becomes र्", "Not before any consonant: before त it becomes स्, before च श्."),
             ("The dual genitive ending itself is -ओर्, not -ओः", "The ending is -ओः; the र् comes only from sandhi."),
             ("मध्ये begins with a vowel, so the visarga turns to र्", "मध्ये begins with the consonant म, not a vowel.")],
            "भ्रुवोः + मध्ये: visarga after ओ, before the voiced म → र्.",
            "Visarga after a vowel other than अ/आ, before a voiced sound → र्."),
        mcq("transfer", 5, "By the rule of तत्रोत्क्षेपवत्, how is सूर्य + उदयः (sunrise) joined in a new example?",
            ("सूर्योदयः", "अ + उ → ओ, as तत्र + उत्क्षेपवत् → तत्रोत्क्षेपवत्."),
            [("सूर्यौदयः", "औ comes from अ + ओ or औ, not from अ + उ."),
             ("सूर्युदयः", "The अ cannot simply drop before उ."),
             ("सूर्यवुदयः", "व् comes from उ before a vowel, not from अ.")],
            "सूर्य + उदयः = सूर्योदयः, like तत्र + उत्क्षेपवत्.",
            "अ + उ → ओ.",
            teaches="अ (or आ) + उ (or ऊ) → ओ: तत्र + उत्क्षेपवत् → तत्रोत्क्षेपवत्."),
    ],
}

# ---------------------------------------------------------------- unit 42
AUTHORED["42"] = {
    "title": "पंच संधयः सीमंता नाम",
    "question": "By unit 42, what are the sīmantas, and what follows injury to them?",
    "rule": ("Five joints (सन्धयः) on the head, transverse and upward, are called sīmanta; in them, death by way of "
             "insanity (उन्माद), giddiness (भ्रम) and loss of mind (चित्तनाश)."),
    "limits": ("Prose; injury is understood. The five joints as the skull sutures: probable, not stated. तिर्यक् and "
               "ऊर्ध्वम् as the joints' direction is the plainest reading; no question rests on it. -नाशैः is read "
               "'by way of'."),
    "explain_hi": ("सिर पर पाँच सन्धियाँ हैं, तिरछी और ऊपर की ओर; इनका नाम सीमन्त है। "
                   "‘सीमन्त’ शब्द का अर्थ है बालों की माँग; यहाँ यह मर्म का नाम है। "
                   "इन पर आघात (समझा जाता है) होने पर उन्माद, चक्कर (भ्रम) और चित्त के नाश के द्वारा मरण होता है। "
                   "ये पाँच सन्धियाँ सम्भवतः खोपड़ी की सीवनें हैं; पंक्ति यह नहीं कहती। "
                   "‘सीमंता नाम’ में आ के बाद का विसर्ग घोष न से पहले लुप्त हुआ है।"),
    "hook": "सिर की पाँच सन्धियाँ सीमन्त: उन्माद, भ्रम, चित्त-नाश, फिर मरण।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 42, how many joints (sandhi) on the head are called sīmanta?",
            ("Five", "पञ्च सन्धयः ... सीमन्ता नाम: five joints."),
            [("Four", "Four is the count of the śṛṅgāṭaka mouths (unit 43), not of the sīmantas."),
             ("Two", "Unit 42 prints पंच (five), not two."),
             ("Eight", "Unit 42 prints पंच (five), not eight.")],
            "Five joints on the head are called sīmanta.",
            "पञ्च सन्धयः शिरसि."),
        order(1, "Put the printed phrases of unit 42 in the line's order.",
              ["पंच संधयः", "शिरसितिर्यगूर्ध्वं च", "सीमंता नाम", "तेषून्मादभ्रमचित्तनाशैर्मरणं"],
              "Five joints; on the head, transverse and upward; called sīmanta; in those, death by insanity, giddiness, loss of mind.",
              "पंच संधयः → शिरसितिर्यगूर्ध्वं च → सीमंता नाम → तेषून्मादभ्रमचित्तनाशैर्मरणं."),
        match(2, "Match each word of unit 42 to its meaning.",
              [["उन्माद", "insanity"], ["भ्रम", "giddiness"], ["चित्तनाश", "loss of mind"], ["मरण", "death"],
               ["सीमन्त", "parting of the hair (as a word)"]],
              "Death comes by way of unmāda, bhrama and citta-nāśa; sīmanta as a word means the parting of the hair.",
              "उन्माद, भ्रम, चित्तनाश, मरण, सीमन्त.", role="extend",
              teaches="उन्माद-भ्रम-चित्तनाशैः is a dvandva in the instrumental plural: 'by way of insanity, giddiness and loss of mind'."),
        mcq("discriminate", 3, "In सीमंता नाम (unit 42), why has the visarga of सीमन्ताः gone?",
            ("After आ, a visarga drops before a voiced sound", "न is voiced: सीमन्ताः + नाम → सीमन्ता नाम."),
            [("After अ, a visarga becomes ओ before the न", "The vowel is आ (-न्ताः); अः would have given सीमन्तो."),
             ("The word is a singular that has no visarga", "सीमन्ताः is masculine nominative plural; it ends in -आः."),
             ("A visarga always drops before any consonant", "Not always: before त it becomes स्, before च श्.")],
            "सीमन्ताः + नाम: आः before the voiced न loses its visarga.",
            "आः + voiced sound → आ (visarga drops)."),
        multi("apply", 4, "Which statements fit unit 42?",
              [("The sīmantas are five joints on the head", "Right: पञ्च सन्धयः शिरसि ... सीमन्ता नाम."),
               ("The line itself names them the skull sutures", "Not printed: the sutures are only a probable reading."),
               ("Insanity and giddiness are named before death", "Right: उन्माद-भ्रम-चित्तनाशैः मरणम्."),
               ("Blindness follows injury to them", "Blindness belongs to the apāṅgas and āvartas (units 38-39).")],
              [0, 2],
              "Five head-joints called sīmanta; death by way of insanity, giddiness and loss of mind.",
              "पञ्च सन्धयः ... सीमन्ता नाम तेषु उन्माद-भ्रम-चित्तनाशैः मरणम्."),
        mcq("transfer", 5, "By the rule of तेषून्माद, how is साधु + उक्तम् (well said) joined in a new example?",
            ("साधूक्तम्", "उ + उ → ऊ, as तेषु + उन्माद → तेषून्माद."),
            [("साध्वुक्तम्", "उ → व् only before a different vowel; before उ the two merge."),
             ("साधोक्तम्", "ओ comes from अ + उ, not from उ + उ."),
             ("साधुक्तम्", "The two उ merge into a long ऊ, not a short उ.")],
            "साधु + उक्तम् = साधूक्तम्, like तेषु + उन्माद = तेषून्माद.",
            "उ + उ → ऊ.",
            teaches="Two like vowels merge into the long one: तेषु + उन्माद → तेषून्माद (उ + उ → ऊ)."),
    ],
}

# ---------------------------------------------------------------- unit 43
AUTHORED["43"] = {
    "title": "तालुनि सन्निपातः शृंगाटकसंज्ञानि",
    "question": "By unit 43, what are the śṛṅgāṭakas, and what follows injury to them?",
    "rule": ("The vessels (sirā) that satiate (तर्पणी) the tongue, nose, eye and ear meet in the palate (तालुनि "
             "सन्निपातः); their four mouths are named śṛṅgāṭaka; in them, death at once (सद्यो मरणम्)."),
    "limits": ("Prose, verbless; injury is understood. No single modern vessel is named for sirā. शृङ्गाटक is kept as the "
               "marma name (as a word: a triangle or junction). The print spells जिव्हा for जिह्वा (accepted variant)."),
    "explain_hi": ("जीभ, नाक, आँख और कान को तृप्त करने वाली सिराएँ तालु में आकर मिलती हैं। "
                   "उनके चार मुख हैं, जिनका नाम शृङ्गाटक है; इन पर आघात (समझा जाता है) से तत्काल मरण होता है। "
                   "‘शृङ्गाटक’ शब्द का अर्थ है त्रिकोण या संगम; यहाँ यह मर्म का नाम है। "
                   "छपा ‘जिव्हा’ जिह्वा का मान्य वर्तनी-भेद है। "
                   "‘सद्यो मरणं’ में अः घोष व्यंजन म से पहले ओ बना है।"),
    "hook": "चार इन्द्रियों की सिराएँ तालु में मिलें: चार मुख शृङ्गाटक, तुरन्त मरण।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 43, where do the vessels serving the tongue, nose, eye and ear meet?",
            ("In the palate (tālu)", "तालुनि सन्निपातः: the meeting is in the palate."),
            [("In the forehead (lalāṭa)", "The forehead is the place of the śaṅkhas (unit 39), not this meeting."),
             ("In the neck (grīvā)", "Unit 43 names the palate, not the neck."),
             ("Between the brows (bhrū)", "Between the brows is the sthapanī (unit 41).")],
            "The four senses' vessels meet in the palate.",
            "तालुनि सन्निपातः."),
        order(1, "Put the printed phrases of unit 43 in the line's order.",
              ["जिव्हाघ्राणाक्षिश्रोत्रतर्पणीनां सिराणां", "तालुनि सन्निपातः", "तासां मुखानि चत्वारि",
               "शृंगाटकसंज्ञानि", "तेषु सद्यो मरणं"],
              "Of the vessels satiating tongue, nose, eye, ear; meeting in the palate; their four mouths; named śṛṅgāṭaka; in those, death at once.",
              "सिराणाम् → तालुनि सन्निपातः → मुखानि चत्वारि → शृंगाटकसंज्ञानि → सद्यो मरणम्."),
        match(2, "Match each member of the compound in unit 43 to its meaning.",
              [["जिह्वा", "tongue"], ["घ्राण", "nose"], ["अक्षि", "eye"], ["श्रोत्र", "ear"], ["तर्पणी", "satiating"],
               ["तालु", "palate"]],
              "जिह्वा-घ्राण-अक्षि-श्रोत्र-तर्पणी: satiating tongue, nose, eye and ear; तालु = palate.",
              "जिह्वा, घ्राण, अक्षि, श्रोत्र, तर्पणी, तालु.", role="extend",
              teaches="A dvandva of four sense organs ends in तर्पणी (satiating): the vessels that satiate those four."),
        mcq("discriminate", 3, "Which split of घ्राणाक्षि inside the compound of unit 43 is right?",
            ("घ्राण + अक्षि", "अ + अ → आ: घ्राण + अक्षि → घ्राणाक्षि."),
            [("घ्राणा + क्षि", "क्षि is not a word here; the eye is अक्षि."),
             ("घ्राण + आक्षि", "आक्षि is not a word; the eye is अक्षि."),
             ("घ्राणाः + अक्षि", "Compound members carry no case ending such as -आः.")],
            "घ्राण (nose) + अक्षि (eye): अ + अ → आ.",
            "अ + अ → आ."),
        mcq("apply", 4, "By unit 43, what follows injury (understood) to the śṛṅgāṭakas?",
            ("Death at once", "तेषु सद्यो मरणम्: in those, death at once."),
            [("Blindness or damage to sight", "That is said of the āvartas (unit 39)."),
             ("Loss of the sense of smell", "That is said of the phaṇas (unit 37)."),
             ("Death by way of insanity", "That is said of the sīmantas (unit 42).")],
            "In the śṛṅgāṭakas, death at once.",
            "तेषु सद्यो मरणम्."),
        mcq("transfer", 5, "By the rule of सद्यो मरणं, how is रामः + गच्छति (Rāma goes) joined in a new example?",
            ("रामो गच्छति", "अः before the voiced ग → ओ, as सद्यः + मरणम् → सद्यो मरणम्."),
            [("रामा गच्छति", "The visarga drops after आ; here the vowel is अ, so it becomes ओ."),
             ("रामर्गच्छति", "र् comes after vowels other than अ/आ, not after अ."),
             ("रामस्गच्छति", "स् comes before त or थ, not before ग.")],
            "रामः + गच्छति = रामो गच्छति, like सद्यः + मरणम्.",
            "अः + voiced consonant → ओ.",
            teaches="अः before a voiced consonant becomes ओ: सद्यः + मरणम् → सद्यो मरणम्."),
    ],
}

# ---------------------------------------------------------------- unit 44
AUTHORED["44"] = {
    "title": "रोमावर्तः सोऽधिपतिर्नाम",
    "question": "By unit 44, what is the adhipati, and what follows injury to it?",
    "rule": ("Inside the head, above, the meeting of vessels (शिरा) and joints (सन्धि), a whorl of hair (रोमावर्तः): that "
             "is called adhipati (सोऽधिपतिर्नाम); there too, death occurs at once."),
    "limits": ("Prose; injury is understood. The print joins मस्तकाभ्यंतरं and उपरिष्टात् without a space (a spacing slip). "
               "रोमावर्त is read as describing the spot. The closing इति marks the end of the passage and is not translated."),
    "explain_hi": ("सिर के भीतर, ऊपर की ओर, सिराओं और सन्धियों का मिलन-स्थान है, जहाँ बालों का भँवर होता है। "
                   "उसका नाम अधिपति है; ‘अधिपति’ शब्द का अर्थ है स्वामी। "
                   "वहाँ भी तत्काल मरण होता है (‘अपि’ = भी)। "
                   "अन्त का ‘इति’ इस अंश की समाप्ति दिखाता है और अनूदित नहीं किया गया। "
                   "‘सोऽधिपतिः’ में सः + अधिपतिः: अः के बाद अ आए तो ओ बनता है और अ का लोप अवग्रह (ऽ) से दिखाया जाता है।"),
    "hook": "सिर के ऊपर बालों का भँवर: अधिपति, वहाँ भी तुरन्त मरण।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 44, what follows injury (understood) to the adhipati?",
            ("Death at once", "तत्रापि सद्यो मरणं भवति: there too, death at once."),
            [("Blindness alone", "Blindness is said of the apāṅgas (unit 38), not the adhipati."),
             ("Insanity alone", "Insanity is named for the sīmantas (unit 42), with death."),
             ("Loss of smell", "Loss of smell is said of the phaṇas (unit 37).")],
            "At the adhipati too, death at once.",
            "तत्रापि सद्यो मरणं भवति."),
        order(1, "Put the printed phrases of unit 44 in the line's order.",
              ["मस्तकाभ्यंतरंउपरिष्टाच्छिरासंधिसन्निपातो", "रोमावर्तः", "सोऽधिपतिर्नाम", "तत्रापि सद्यो मरणं भवतीति"],
              "Inside the head, above, the meeting of vessels and joints; a hair-whorl; that is called adhipati; there too death at once.",
              "सन्निपातो → रोमावर्तः → सोऽधिपतिर्नाम → तत्रापि सद्यो मरणम्."),
        fill(2, "Unit 44: 'a whorl of hair' is रोम + ____ (whorl). Type it in Devanagari or in English letters (e.g. dharma).",
             accepts("आवर्तः", None, "आवर्त", "avartah", "avarta"),
             "रोम + आवर्तः → रोमावर्तः, a whorl of hair (अ + आ → आ).",
             "आवर्त means a whorl or eddy; रोम-आवर्त is a hair-whorl.",
             "रोम + आवर्तः = रोमावर्तः."),
        mcq("discriminate", 3, "Which split of सोऽधिपतिर्नाम in unit 44 is right?",
            ("सः + अधिपतिः + नाम", "अः + अ → ओऽ; इः before the voiced न → इर्."),
            [("सो + अधिपतिः + नाम", "सो is not a word on its own; ओऽ comes from सः before अ."),
             ("सः + धिपतिः + नाम", "The avagraha marks a lost अ; the word is अधिपति."),
             ("सः + अधिपतिम् + नाम", "म् before न would be written ं or न्, never र्.")],
            "सः (that) + अधिपतिः (adhipati) + नाम (called).",
            "अः + अ → ओऽ; इः + voiced sound → इर्."),
        mcq("apply", 4, "In उपरिष्टाच्छिरा (unit 44), what does the च्छ come from?",
            ("त् + श (उपरिष्टात् + शिरा)", "त् + श → च्श, or optionally च्छ before a vowel or semivowel (here इ), as printed."),
            [("त् + स (उपरिष्टात् + सिरा)", "त् + स gives त्स, not च्छ."),
             ("च् + श (उपरिष्टाच् + शिरा)", "उपरिष्टाच् is not a word; the word is उपरिष्टात्."),
             ("त् + छ (उपरिष्टात् + छिरा)", "छिरा is not a word; the vessel is शिरा/सिरा.")],
            "उपरिष्टात् (above) + शिरा (vessel): त् + श → च्श, or optionally च्छ when a vowel or semivowel follows the श (here इ).",
            "त् + श → च्श; optionally च्छ when a vowel or semivowel follows the श."),
        mcq("transfer", 5, "By the rule of सोऽधिपतिः, how is सः + अपि (he too) joined in a new example?",
            ("सोऽपि", "सः before अ → सो, and the अ is dropped (ऽ), as in सोऽधिपतिः."),
            [("स अपि", "स with a gap comes before vowels other than अ, not before अ."),
             ("सरपि", "र् comes after vowels other than अ/आ."),
             ("सौपि", "औ comes from अ + ओ or औ, not from अः + अ.")],
            "सः + अपि = सोऽपि, like सः + अधिपतिः = सोऽधिपतिः.",
            "अः + अ → ओऽ.",
            teaches="अः before अ becomes ओ and the following अ is dropped, marked by ऽ: सः + अधिपतिः → सोऽधिपतिः."),
    ],
}

# ---------------------------------------------------------------- unit 45
AUTHORED["45"] = {
    "title": "सामान्यलक्षणं पुनर्मर्मणां",
    "question": "By unit 45, what is the general sign of the marmas when one is pressed or injured?",
    "rule": ("Further, the general sign of the marmas (सामान्यलक्षणं मर्मणाम्): when pressed or injured (पीडिते), "
             "arising of pain (रुजोत्पत्तिः) and irregular throbbing (विषमं स्पन्दनम्)."),
    "limits": ("Prose, verbless. पीडिते is impersonal: the injured marma is understood. पुनर् is read 'further' (a new "
               "topic). The line does not say what throbs; no question rests on that."),
    "explain_hi": ("यहाँ से नया विषय आरम्भ होता है: मर्मों का सामान्य लक्षण। "
                   "किसी मर्म के पीड़ित (दबने या चोट लगने) पर दो बातें होती हैं: पीड़ा की उत्पत्ति और अनियमित स्पन्दन। "
                   "‘पीडिते’ सप्तमी है: ‘पीड़ित होने पर’; कौन-सा मर्म, यह समझा जाता है। "
                   "कोई क्रिया छपी नहीं। "
                   "‘रुजोत्पत्तिर्विषमं’ में इ के बाद का विसर्ग घोष व से पहले र् बना है।"),
    "hook": "मर्म दबे तो दो बातें: पीड़ा उठे, स्पन्दन बिगड़े।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 45, which two signs appear when a marma is pressed or injured?",
            ("Pain and irregular throbbing", "रुजोत्पत्तिः (arising of pain) and विषमं स्पन्दनम् (irregular throbbing)."),
            [("Swelling and redness of the spot", "Neither swelling nor redness is printed in unit 45."),
             ("Fever and a burning thirst", "Neither fever nor thirst is printed in unit 45."),
             ("Itching and a change of colour", "Neither itching nor colour change is printed in unit 45.")],
            "The general sign: pain arises and the throbbing is irregular.",
            "पीडिते रुजोत्पत्तिर्विषमं च स्पन्दनम्."),
        order(1, "Put the printed words of unit 45 in the line's order.",
              ["सामान्यलक्षणं", "पुनर्मर्मणां", "पीडिते", "रुजोत्पत्तिर्विषमं च", "स्पंदनं"],
              "The general sign; further, of the marmas; when pressed; arising of pain and irregular; throbbing.",
              "सामान्यलक्षणं → पुनर्मर्मणां → पीडिते → रुजोत्पत्तिर्विषमं च → स्पंदनं."),
        match(2, "Match each word part of unit 45 to its meaning.",
              [["सामान्य", "general"], ["लक्षण", "sign"], ["रुजा", "pain"], ["उत्पत्ति", "arising"],
               ["विषम", "irregular"], ["स्पन्दन", "throbbing"]],
              "सामान्य-लक्षण = general sign; रुजा-उत्पत्ति = arising of pain; विषमं स्पन्दनम् = irregular throbbing.",
              "सामान्य, लक्षण, रुजा, उत्पत्ति, विषम, स्पन्दन.", role="extend",
              teaches="रुजोत्पत्ति is a tat-puruṣa: रुजा (pain) + उत्पत्ति (arising), आ + उ → ओ = the arising of pain."),
        mcq("discriminate", 3, "Why is उत्पत्तिः printed -त्तिर् before विषमं in unit 45?",
            ("After इ, a visarga before a voiced sound becomes र्", "व is voiced: रुजोत्पत्तिः + विषमम् → रुजोत्पत्तिर्विषमम्."),
            [("After इ, a visarga before any consonant becomes र्", "Not before any consonant: before त it becomes स्, before च श्."),
             ("The word's own stem ends in -र्, not in a visarga", "The stem is उत्पत्ति (an इ-stem); the र् comes from sandhi."),
             ("विषमं begins with a vowel, so the visarga turns to र्", "विषमं begins with the consonant व, not a vowel.")],
            "रुजोत्पत्तिः + विषमम्: इः before the voiced व → इर्.",
            "इः / उः + voiced sound → इर् / उर्."),
        mcq("apply", 4, "In unit 45, what does the locative पीडिते express?",
            ("When (a marma) is pressed or injured", "Locative of the past participle: 'when pressed, when injured'."),
            [("Having pressed (a marma) with the hand", "That would be a gerund such as पीडयित्वा, not a locative."),
             ("In order to press (a marma) oneself", "That would be an infinitive or dative, not पीडिते."),
             ("By the one who presses (a marma)", "That would be an instrumental agent, not a locative.")],
            "पीडिते (loc. of the past participle) = when (a marma) is pressed or injured.",
            "A locative participle with an understood noun = 'when (it) is ...'."),
        mcq("transfer", 5, "By the rule of रुजोत्पत्तिर्विषमं, how is मतिः + मम (my thought) joined in a new example?",
            ("मतिर्मम", "इ + visarga before the voiced म → र्, as उत्पत्तिः + विषमम्."),
            [("मतिस्मम", "स् comes before त or थ, not before म."),
             ("मति मम", "The visarga drops before a voiced sound after आ, not after इ."),
             ("मतिश्मम", "श् comes before च or छ (optionally before श), not before म.")],
            "मतिः + मम = मतिर्मम, like रुजोत्पत्तिः + विषमम्.",
            "इः + voiced sound → इर्.",
            teaches="After इ or उ, a visarga becomes र् before a voiced sound: रुजोत्पत्तिः + विषमम् → रुजोत्पत्तिर्विषमम्."),
    ],
}

# ---------------------------------------------------------------- unit 46
AUTHORED["46"] = {
    "title": "सामान्येनैव च",
    "question": "What does the short unit 46 print, and what is certain about it?",
    "rule": "सामान्येनैव च: data reading 'and by the general (one) alone' (सामान्येन + एव); elliptical.",
    "limits": ("Elliptical prose: the noun (probably 'sign') is not printed or supplied. GROUPING (data): appears to "
               "continue unit 45 and introduce unit 47's list. The split सामान्येन + एव is the data's reading, not "
               "certain. No question rests on the link or the split."),
    "explain_hi": ("यह दो शब्दों की गद्य-पंक्ति है: ‘और सामान्य से ही’। "
                   "जिस संज्ञा से ‘सामान्येन’ जुड़ता है (सम्भवतः ‘लक्षण’), वह छपी नहीं, और डेटा उसे जोड़ता नहीं। "
                   "‘सामान्येन’ का अर्थ ‘सामान्य रूप से’ भी हो सकता है। "
                   "डेटा के अनुसार यह इकाई ४५ को आगे बढ़ाती और इकाई ४७ की सूची का परिचय देती दिखती है। "
                   "डेटा का विभाजन सामान्येन + एव (अ + ए → ऐ) है; यह निश्चित नहीं, इस पर कोई प्रश्न नहीं।"),
    "hook": "‘सामान्येनैव च’: क्रिया छपी नहीं।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 46, what does the separate word च mean?",
            ("and", "च = and."),
            [("or", "That would be वा."), ("but", "That would be तु."), ("not", "That would be न.")],
            "च = and.", "च = and."),
        match(1, "Match each particle to its meaning (च is the one printed in unit 46).",
              [["च", "and"], ["वा", "or"], ["तु", "but, however"], ["अपि", "also, too"]],
              "च = and; वा = or; तु = but; अपि = also.", "च, वा, तु, अपि."),
        mcq("extend", 2, "By the data, which is true of unit 46?",
            ("No verb is printed or supplied", "Data: elliptical, not enriched."),
            [("It is an anuṣṭubh verse line", "type: prose."),
             ("It names five kinds of marma", "No kind of marma is printed in unit 46."),
             ("Its verb भवति ends the line", "No verb is printed in unit 46.")],
            "Unit 46 is elliptical prose: no verb is printed and none is supplied.",
            "Elliptical line: nothing supplied.",
            teaches="An elliptical line: the data supplies no missing verb or noun."),
        mcq("discriminate", 3, "Why does च stand last in unit 46?",
            ("च follows the word it adds", "च is enclitic: it never opens a clause."),
            [("च always ends a chapter", "च is a particle; it does not mark chapter ends."),
             ("च is a verb, set last", "च is an indeclinable particle, not a verb."),
             ("च fills a gap in the print", "च is printed plainly; nothing is restored.")],
            "च comes after the word it adds.", "च is enclitic."),
        multi("apply", 4, "Which of these words are printed in unit 46?",
              [("च", "Right: च stands apart at the end."),
               ("अपि", "अपि is not printed in unit 46."),
               ("वा", "वा is not printed in unit 46."),
               ("सामान्येनैव", "Right: printed as one word."),
               ("तु", "तु is not printed in unit 46.")],
              [0, 3],
              "Unit 46 prints सामान्येनैव and च only.",
              "सामान्येनैव च."),
        mcq("transfer", 5, "By the use of च in unit 46, what does रामो लक्ष्मणश्च mean in a new example?",
            ("Rāma and Lakṣmaṇa", "च after the last word = and."),
            [("Rāma or Lakṣmaṇa", "'Or' would be वा."),
             ("Rāma, not Lakṣmaṇa", "No न is printed."),
             ("Rāma, but Lakṣmaṇa", "'But' would be तु.")],
            "रामो लक्ष्मणश्च = Rāma and Lakṣmaṇa (रामः + ल → रामो; लक्ष्मणः + च → लक्ष्मणश्च).",
            "X Y च = X and Y.",
            teaches="च follows the last word it joins: रामो लक्ष्मणश्च."),
    ],
}

# ---------------------------------------------------------------- unit 47
AUTHORED["47"] = {
    "title": "मर्मविद्धस्य लक्षणं",
    "question": "By unit 47, which signs mark one pierced in a marma?",
    "rule": ("Heaviness (गुरुता), bewilderment (संमोह), desire for cold (शीतकामिता), sweating (स्वेद), fainting (मूर्च्छा), "
             "vomiting (वमि) and laboured breathing (श्वास): the sign of one pierced in a marma (मर्मविद्धस्य लक्षणम्)."),
    "limits": ("Verse (anuṣṭubh), confidence low. The first printed word देहप्रमुसि is damaged or unknown: kept unsplit, "
               "untranslated, and no question rests on it or on any guess for it. श्वास is breathing trouble in general "
               "(dyspnoea is the usual modern sense: probable). Verbless list."),
    "explain_hi": ("यह दो पंक्तियों का श्लोक मर्म में बिंधे हुए व्यक्ति के लक्षण गिनाता है। "
                   "पहली पंक्ति का पहला शब्द ‘देहप्रमुसि’ क्षतिग्रस्त या अज्ञात है; वह अस्पष्ट है और अनूदित नहीं किया गया। "
                   "बाकी लक्षण: भारीपन, सम्मोह (भ्रम), शीत की इच्छा, पसीना, मूर्च्छा, वमन और श्वास का कष्ट। "
                   "अन्त में ‘मर्मविद्धस्य लक्षणम्’ = मर्म में बिंधे हुए का लक्षण; कोई क्रिया छपी नहीं। "
                   "‘स्वेदो’ और ‘श्वासो’ में अः घोष व्यंजन म से पहले ओ बना है।"),
    "hook": "मर्म-विद्ध: भारी, भ्रमित, ठंड चाहे, पसीना, मूर्च्छा, वमन, साँस फूले।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 47, which of these is named as a sign of one pierced in a marma?",
            ("Desire for cold (śīta-kāmitā)", "शीतकामिता: desire for cold."),
            [("Desire for heat (uṣṇa-kāmitā)", "The verse names desire for cold, not for heat."),
             ("Loss of hunger (aruci)", "Loss of hunger is not printed in unit 47."),
             ("Itching of the skin (kaṇḍū)", "Itching is not printed in unit 47.")],
            "Desire for cold is one of the signs.",
            "शीतकामिता = desire for cold."),
        order(1, "After the damaged first word, put the printed words of unit 47 in the verse's order.",
              ["गुरुता", "संमोहः", "शीतकामिता", "स्वेदोमूर्च्छा", "वमिः श्वासो", "मर्मविद्धस्य लक्षणं"],
              "Heaviness, bewilderment, desire for cold; sweating, fainting; vomiting, breathlessness; the sign of one pierced in a marma.",
              "गुरुता → संमोहः → शीतकामिता → स्वेदोमूर्च्छा → वमिः श्वासो → मर्मविद्धस्य लक्षणं."),
        match(2, "Match each sign named in unit 47 to its meaning.",
              [["गुरुता", "heaviness"], ["संमोह", "bewilderment"], ["शीतकामिता", "desire for cold"],
               ["स्वेद", "sweating"], ["मूर्च्छा", "fainting"], ["वमि", "vomiting"]],
              "Six of the sure signs: heaviness, bewilderment, desire for cold, sweating, fainting, vomiting.",
              "गुरुता, संमोह, शीतकामिता, स्वेद, मूर्च्छा, वमि.", role="extend",
              teaches="-ता makes an abstract noun: गुरु (heavy) → गुरुता (heaviness); कामिन् → कामिता (desire)."),
        mcq("discriminate", 3, "Why is स्वेदः printed स्वेदो before मूर्च्छा in unit 47?",
            ("अः before a voiced consonant becomes ओ", "म is a voiced consonant: स्वेदः + मूर्च्छा → स्वेदो मूर्च्छा."),
            [("अः before every consonant becomes ओ", "Not every consonant: before त the visarga becomes स्, before च श्."),
             ("ओ is the nominative ending of स्वेद", "The nominative is स्वेदः; ओ comes only from sandhi."),
             ("मूर्च्छा begins with a vowel, so अः → ओ", "मूर्च्छा begins with the consonant म.")],
            "स्वेदः + मूर्च्छा: अः before the voiced म → ओ.",
            "अः + voiced consonant → ओ."),
        multi("apply", 4, "Which are named in unit 47 as signs of one pierced in a marma?",
              [("Itching of the skin (kaṇḍū)", "Not printed in unit 47."),
               ("Vomiting (vami)", "Right: वमिः."),
               ("Sweating (sveda)", "Right: स्वेदो."),
               ("Desire for warmth", "The verse has desire for cold (शीतकामिता)."),
               ("Fainting (mūrcchā)", "Right: मूर्च्छा.")],
              [1, 2, 4],
              "Vomiting, sweating and fainting are named; itching and desire for warmth are not.",
              "स्वेदो मूर्च्छा वमिः श्वासो मर्मविद्धस्य लक्षणम्."),
        mcq("transfer", 5, "By the pattern of गुरु → गुरुता (heaviness), what does लघु → लघुता mean in a new example?",
            ("lightness", "-ता makes an abstract noun: लघु (light) → लघुता (lightness)."),
            [("light (an adjective)", "The adjective is लघु itself; -ता makes the abstract noun."),
             ("to make light", "-ता does not make a verb."),
             ("a light person", "-ता names the quality, not the one who has it.")],
            "लघु → लघुता = lightness, like गुरु → गुरुता = heaviness.",
            "Adjective + -ता → abstract noun (feminine).",
            teaches="-ता after an adjective makes a feminine abstract noun: गुरु → गुरुता (heaviness)."),
    ],
}

# ---------------------------------------------------------------- unit 48
AUTHORED["48"] = {
    "title": "अपिच",
    "question": "What does the connective अपिच (unit 48) mean?",
    "rule": "अपि (also) + च (and): 'and further'; a connective formula that opens a new statement.",
    "limits": ("Prose, one printed word; the print writes अपि च without a space. GROUPING (data): it opens unit 49; no "
               "question rests on that link."),
    "explain_hi": ("यह एक शब्द की गद्य-पंक्ति है: ‘अपि च’ = और भी। "
                   "अपि = भी, च = और; दोनों अव्यय हैं। "
                   "यह जोड़ने वाला सूत्र-वाक्यांश अगले कथन को खोलता है; डेटा के अनुसार वह इकाई ४९ है। "
                   "छपाई में अपि और च बिना अन्तर के जुड़े हैं; कोई ध्वनि-परिवर्तन नहीं, क्योंकि व्यंजन से पहले इ नहीं बदलता।"),
    "hook": "‘अपि च’: और भी, आगे सुनो।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 48, what does अपिच mean?",
            ("And further", "अपि (also) + च (and) = and further."),
            [("But not at all", "No negation is printed; अपि च adds."),
             ("Or, on the other hand", "'Or' would be वा, not अपि च."),
             ("Only this much", "'Only' would be एव or मात्र, not अपि च.")],
            "अपि च = and further.",
            "अपि = also; च = and."),
        match(1, "Match each part of unit 48 to its meaning.",
              [["अपि", "also, too"], ["च", "and"], ["अपि च", "and further"]],
              "अपि = also; च = and; together, 'and further'.",
              "अपि, च, अपि च."),
        fill(2, "Unit 48: अपिच = ____ + च (also + and). Type it in Devanagari or in English letters (e.g. dharma).",
             accepts("अपि"),
             "अपि (also) + च (and) = अपि च, 'and further'.",
             "अपि is an indeclinable meaning 'also, too'; with च it forms the connective अपि च.",
             "अपि + च = अपिच."),
        mcq("discriminate", 3, "Which split of अपिच (unit 48) is right?",
            ("अपि + च", "अपि (also) + च (and), written without a space."),
            [("अप् + इच", "इच is not a word; the words are अपि and च."),
             ("अपी + च", "अपी is not a word; the particle is अपि."),
             ("अ + पिच", "पिच is not a word; the particle is अपि.")],
            "अपि + च.",
            "अपिच = अपि + च."),
        mcq("apply", 4, "In unit 48, why does अपि stay अपि before च, with no sound change?",
            ("A final इ does not change before a consonant", "Vowel sandhi works only between vowels; च is a consonant."),
            [("A final इ becomes य् before the consonant च", "इ → य् only before a vowel, not before च."),
             ("A final इ becomes ए before the consonant च", "इ does not become ए before a consonant."),
             ("A final इ is dropped before the consonant च", "The इ is not dropped: अपि is printed in full.")],
            "अपि + च: no change, because च is a consonant.",
            "A final vowel stays before a consonant."),
        mcq("transfer", 5, "By vowel sandhi, how is अपि + अहम् (I too) joined in a new example?",
            ("अप्यहम्", "इ before a different vowel becomes य्: अपि + अहम् → अप्यहम्."),
            [("अपहम्", "The इ cannot simply drop."),
             ("अपेहम्", "ए comes from अ + इ, not from इ + अ."),
             ("अपीहम्", "ई comes from इ + इ, not from इ + अ.")],
            "अपि + अहम् = अप्यहम्.",
            "इ + a different vowel → य्.",
            teaches="अपि stays unchanged before a consonant (अपि च) but before a different vowel its इ becomes य् (अप्यहम्)."),
    ],
}

# ---------------------------------------------------------------- unit 49
AUTHORED["49"] = {
    "title": "मरणकारित्वान्मर्म",
    "question": "By unit 49, why is a marma so called, and what is it a meeting of?",
    "rule": ("Because it causes death (मरणकारित्वात्), it is a marma; and it is the meeting (सन्निपात) of flesh (मांस), "
             "vessels (सिरा), sinews (स्नाव = स्नायु), bone (अस्थि) and joint (सन्धि)."),
    "limits": ("Prose, verbless. This is the text's own explanation of the word; no etymology is added. सन्धि is taken as "
               "the fifth member; whether it joins अस्थि as 'bone-joint' is not decided by the wording, so no question "
               "rests on it. Printed स्नाव = स्नायु (both forms occur)."),
    "explain_hi": ("यह पंक्ति मर्म की परिभाषा देती है: मरण कराने के कारण इसे मर्म कहते हैं। "
                   "और वह मांस, सिरा, स्नायु (छपा ‘स्नाव’), अस्थि और सन्धि का सन्निपात यानी मिलन-स्थान है। "
                   "‘मरणकारित्वात्’ पञ्चमी है और कारण बताती है: ‘मृत्यु कराने के कारण’। "
                   "‘सन्धि’ को पाँचवाँ सदस्य माना गया; ‘अस्थि-सन्धि’ (हड्डी का जोड़) भी हो सकता है, शब्दों से तय नहीं। "
                   "यह पाठ की अपनी व्याख्या है; कोई व्युत्पत्ति नहीं जोड़ी गई।"),
    "hook": "जो मारे वह मर्म: मांस, सिरा, स्नायु, अस्थि, सन्धि का संगम।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 49, why is a marma called marma?",
            ("Because it causes death", "मरणकारित्वात्: because of causing death."),
            [("Because it lies hidden deep", "No such reason is printed in unit 49."),
             ("Because it carries the breath", "No such reason is printed in unit 49."),
             ("Because it is soft to the touch", "No such reason is printed in unit 49.")],
            "Because of causing death (मरणकारित्वात्), it is a marma.",
            "मरणकारित्वान्मर्म."),
        order(1, "Put these members of the compound in unit 49 in the printed order.",
              ["मांस", "सिरा", "स्नाव", "अस्थि"],
              "मांस-सिरा-स्नाव-अस्थि-(सन्धि)-सन्निपात: flesh, vessel, sinew, bone.",
              "मांस → सिरा → स्नाव → अस्थि."),
        match(2, "Match each word of unit 49 to its meaning.",
              [["मरण", "death"], ["कारित्व", "causing"], ["मांस", "flesh"], ["स्नाव", "sinew (snāyu)"],
               ["सन्निपात", "meeting"]],
              "मरण-कारित्व = causing death; मांस = flesh; स्नाव = sinew; सन्निपात = meeting.",
              "मरण, कारित्व, मांस, स्नाव, सन्निपात.", role="extend",
              teaches="-त्व makes an abstract noun (कारित्व = the being a cause); its ablative -त्वात् gives the reason."),
        mcq("discriminate", 3, "In मरणकारित्वान्मर्म (unit 49), what case is -त्वात्, and what does it express?",
            ("Ablative: the cause, 'because of'", "gram: n. abl. sg.; the ablative here gives the reason."),
            [("Genitive: the owner, 'of the one'", "The genitive singular would be -त्वस्य, not -त्वात्."),
             ("Locative: the place, 'in the one'", "The locative singular would be -त्वे, not -त्वात्."),
             ("Instrumental: the means, 'with it'", "The instrumental singular would be -त्वेन, not -त्वात्.")],
            "-त्वात् is ablative: because of causing death.",
            "Ablative of an abstract noun in -त्व = 'because of being ...'."),
        multi("apply", 4, "Which are named in unit 49 as members of the meeting (sannipāta) that a marma is?",
              [("Flesh (māṃsa)", "Right: मांस."),
               ("Fat (medas)", "Fat is not printed in unit 49."),
               ("Bone (asthi)", "Right: अस्थि."),
               ("Skin (tvak)", "Skin is not printed in unit 49."),
               ("Sinew (snāva)", "Right: स्नाव (= स्नायु).")],
              [0, 2, 4],
              "Flesh, vessel, sinew and bone are named (with sandhi, read by the data as a fifth member); fat and skin are not.",
              "मांस-सिरा-स्नाव-अस्थि-सन्धि-सन्निपातः."),
        mcq("transfer", 5, "By the pattern of मरणकारित्वात् (because of causing death), what does रोगित्वात् mean in a new example?",
            ("because of being ill", "-त्वात् = ablative of -त्व: 'because of being ...'."),
            [("of the sick person", "That would be a genitive such as रोगिणः, not -त्वात्."),
             ("in the state of illness", "That would be the locative रोगित्वे, not -त्वात्."),
             ("with the illness", "That would be an instrumental, not -त्वात्.")],
            "रोगित्वात् = because of being ill, like मरणकारित्वात्.",
            "-त्वात् = because of being ...",
            teaches="The ablative of an abstract noun in -त्व gives a reason: मरणकारित्वात् = because of causing death."),
    ],
}

# ---------------------------------------------------------------- unit 50
AUTHORED["50"] = {
    "title": "तस्मिन् पीड्यमाने प्राणाबाधः",
    "question": "By unit 50, what follows when 'that' is being pressed or injured?",
    "rule": ("Therefore (तेन), when that (तस्मिन्) is being pressed or injured (पीड्यमाने), there is especially "
             "(विशेषतः) affliction of the life-breath (प्राणाबाधः)."),
    "limits": ("Prose, verbless. तस्मिन् ('in that') apparently points back to unit 49, but its noun is not printed; the card does "
               "not decide which. प्राण is kept as 'life-breath'. तेन is glossed 'therefore, by that'."),
    "explain_hi": ("यह पंक्ति सम्भवतः इकाई ४९ की परिभाषा से निष्कर्ष निकालती है: इसलिए उसके पीड़ित होने पर विशेष रूप से प्राण को बाधा होती है। "
                   "‘तस्मिन् पीड्यमाने’ सप्तमी में है: ‘उसके पीड़ित किए जाते समय’। "
                   "‘पीड्यमान’ वर्तमान कर्मवाच्य कृदन्त है (दबाया जा रहा)। "
                   "‘तस्मिन्’ किस संज्ञा को बताता है, वह छपी नहीं। "
                   "सन्धि: प्राण + आबाधः → प्राणाबाधः (अ + आ → आ)।"),
    "hook": "‘वह’ दबता हो तो विशेषकर प्राण पर बाधा।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 50, what is especially afflicted when 'that' is being pressed?",
            ("The life-breath (prāṇa)", "प्राणाबाधः: affliction of the life-breath."),
            [("The digestive fire (agni)", "Agni is not named in unit 50."),
             ("The sense of sight (dṛṣṭi)", "Sight is not named in unit 50."),
             ("The blood (śoṇita)", "Blood is not named in unit 50.")],
            "Especially, affliction of the life-breath.",
            "विशेषतः प्राणाबाधः."),
        order(1, "Put the printed words of unit 50 in the line's order.",
              ["तेन", "तस्मिन्", "पीड्यमाने", "विशेषतः", "प्राणाबाधः"],
              "Therefore; in that; being pressed; especially; affliction of the life-breath.",
              "तेन → तस्मिन् → पीड्यमाने → विशेषतः → प्राणाबाधः."),
        match(2, "Match each word of unit 50 to its meaning.",
              [["तेन", "therefore"], ["पीड्यमान", "being pressed"], ["विशेषतः", "especially"], ["प्राण", "life-breath"],
               ["आबाध", "affliction"]],
              "तेन = therefore; पीड्यमाने = being pressed; विशेषतः = especially; प्राण-आबाध = affliction of the life-breath.",
              "तेन, पीड्यमान, विशेषतः, प्राण, आबाध.", role="extend",
              teaches="प्राणाबाध is a tat-puruṣa: प्राण (life-breath) + आबाध (affliction) = affliction of the life-breath."),
        mcq("discriminate", 3, "What form is पीड्यमाने in unit 50?",
            ("Present passive participle, locative", "gram: pres. pass. part., loc. sg.: 'while being pressed'."),
            [("Present active participle, locative", "The active would mean 'while pressing'; -यमान here is passive."),
             ("Optative verb, third person singular", "An optative is a finite verb; पीड्यमाने declines like a noun."),
             ("Past passive participle, nominative", "The past participle is पीडित; -माने is a locative.")],
            "पीड्यमाने: present passive participle, locative: while (that) is being pressed.",
            "Present passive participle in -यमान; locative -माने."),
        fill(4, "Unit 50: तस्मिन् पीड्यमाने विशेषतः ____ + आबाधः (affliction of the life-breath). Type it in Devanagari or in English letters (e.g. dharma).",
             accepts("प्राण", None, "prana"),
             "प्राण + आबाधः → प्राणाबाधः (अ + आ → आ).",
             "प्राण = life-breath; with आबाध it means affliction of the life-breath.",
             "प्राण + आबाधः = प्राणाबाधः.", role="apply"),
        mcq("transfer", 5, "By the pattern of तस्मिन् पीड्यमाने, what does ग्रामे दह्यमाने mean in a new example?",
            ("while the village is being burnt", "Locative + present passive participle = 'while X is being ...ed'."),
            [("after the village was burnt", "That would need the past participle (दग्धे), not -यमाने."),
             ("while burning the village", "That would be active; -यमान here is passive."),
             ("the village is burning now", "A finite statement would need a verb such as दह्यते.")],
            "ग्रामे दह्यमाने = while the village is being burnt, like तस्मिन् पीड्यमाने.",
            "Locative + -यमाने = while (it) is being ...ed.",
            teaches="A noun and a present passive participle both in the locative mean 'while X is being ...ed': तस्मिन् पीड्यमाने."),
    ],
}

# ---------------------------------------------------------------- unit 51
AUTHORED["51"] = {
    "title": "बाहुल्येन तु निर्देशः",
    "question": "What does unit 51 say about the designation (nirdeśa)?",
    "rule": "बाहुल्येन तु निर्देशः: 'but the designation is by preponderance (bāhulya)'.",
    "limits": ("Prose, verbless. The data's sense, that the name 'marma' is given by what predominates and not as an exact "
               "rule, is interpretation kept out of the translation; no question rests on it."),
    "explain_hi": ("यह तीन शब्दों की गद्य-पंक्ति है: ‘किन्तु निर्देश बाहुल्य से (होता है)’। "
                   "बाहुल्य = अधिकता, प्रधानता; निर्देश = नाम देना, बताना; तु = किन्तु। "
                   "‘बाहुल्येन’ तृतीया एकवचन है: ‘बाहुल्य से’। "
                   "डेटा की व्याख्या है कि ‘मर्म’ नाम जो प्रधान हो उसके अनुसार दिया जाता है, पर यह अनुवाद में नहीं है। "
                   "कोई क्रिया छपी नहीं।"),
    "hook": "बाहुल्येन तु निर्देशः: निर्देश बाहुल्य से।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 51, the designation (nirdeśa) is made by what?",
            ("By preponderance (bāhulya)", "बाहुल्येन = by preponderance, by abundance."),
            [("By exact count (saṅkhyā) alone", "No count is printed in unit 51."),
             ("By position (sthāna)", "Position is not named in unit 51."),
             ("By the teacher's word", "No teacher is named in unit 51.")],
            "The designation is by preponderance.",
            "बाहुल्येन तु निर्देशः."),
        order(1, "Put the printed words of unit 51 in the line's order.",
              ["बाहुल्येन", "तु", "निर्देशः"],
              "By preponderance; but; the designation.",
              "बाहुल्येन → तु → निर्देशः."),
        match(2, "Match each word part of unit 51 to its meaning.",
              [["बाहुल्य", "preponderance, abundance"], ["तु", "but, however"], ["निर्देश", "designation, naming"],
               ["-एन", "by (instrumental ending)"]],
              "बाहुल्य-एन = by preponderance; तु = but; निर्देशः = the designation.",
              "बाहुल्य, तु, निर्देश, -एन.", role="extend",
              teaches="बाहुल्य (abundance) is an abstract noun; its instrumental बाहुल्येन means 'by preponderance'."),
        mcq("discriminate", 3, "In unit 51, what case is बाहुल्येन?",
            ("Instrumental singular ('by')", "-एन is the instrumental singular of an अ-stem."),
            [("Genitive singular ('of')", "The genitive would be बाहुल्यस्य."),
             ("Locative singular ('in')", "The locative would be बाहुल्ये."),
             ("Ablative singular ('from')", "The ablative would be बाहुल्यात्.")],
            "बाहुल्येन: instrumental singular, 'by preponderance'.",
            "अ-stem instrumental singular: -एन."),
        mcq("apply", 4, "Which English rendering of unit 51 keeps to the data?",
            ("But the designation: by preponderance.", "बाहुल्येन तु निर्देशः, word for word."),
            [("But the designation: by exact rule.", "बाहुल्येन means 'by preponderance', not 'by exact rule'."),
             ("But the designation: by the teacher alone.", "No teacher is printed in unit 51."),
             ("But no designation is given here at all.", "No negation is printed in unit 51.")],
            "But the designation: by preponderance.",
            "बाहुल्येन तु निर्देशः."),
        mcq("transfer", 5, "By the pattern of बाहुल्य → बाहुल्येन (by preponderance), what is the instrumental of ज्ञान in a new example?",
            ("ज्ञानेन", "अ-stem instrumental singular -एन: ज्ञान → ज्ञानेन (by knowledge)."),
            [("ज्ञानस्य", "-अस्य is the genitive singular."),
             ("ज्ञाने", "-ए is the locative singular."),
             ("ज्ञानात्", "-आत् is the ablative singular.")],
            "ज्ञान → ज्ञानेन, like बाहुल्य → बाहुल्येन.",
            "अ-stem instrumental singular: -एन.",
            teaches="An अ-stem takes -एन in the instrumental singular: बाहुल्य → बाहुल्येन."),
    ],
}

# ---------------------------------------------------------------- unit 52
AUTHORED["52"] = {
    "title": "मर्माणि पंचधा भिद्यंते",
    "question": "By unit 52, in how many ways are the marmas divided?",
    "rule": ("Therefore (तस्मात्) the marmas are divided in five ways (मर्माणि पञ्चधा भिद्यन्ते); on a conjectural reading "
             "the basis is 'flesh and the rest' (मांसाद्याश्रयतः)."),
    "limits": ("Prose. The print 'तस्मान्मां साद्याश्रयतो' has a stray space; the reading मांसाद्याश्रयतः is conjectural "
               "(text flag), so no question rests on it. The five kinds are named in the following units (cards 54-58), "
               "not here."),
    "explain_hi": ("यह पंक्ति मर्मों के विभाजन की घोषणा करती है: इसलिए मर्म पाँच प्रकार से विभक्त होते हैं। "
                   "छपा ‘तस्मान्मां साद्याश्रयतो’ बीच में अन्तर से टूटा है; अनुमानित पाठ ‘मांसाद्याश्रयतः’ = मांस आदि के आश्रय के अनुसार। "
                   "यह पाठ अनुमानित है, इसलिए इस पर कोई प्रश्न नहीं। "
                   "‘भिद्यन्ते’ वर्तमान कर्मवाच्य प्रथम पुरुष बहुवचन है: ‘विभक्त किए जाते हैं’। "
                   "पाँच प्रकार आगे की इकाइयों (५४-५८) में गिनाए गए हैं।"),
    "hook": "मर्म पाँच प्रकार के: पञ्चधा।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 52, in how many ways are the marmas divided?",
            ("In five ways (pañcadhā)", "पञ्चधा = in five ways."),
            [("In three ways (tridhā)", "The line prints पंचधा (five), not three."),
             ("In seven ways (saptadhā)", "The line prints पंचधा (five), not seven."),
             ("In two ways (dvidhā)", "The line prints पंचधा (five), not two.")],
            "The marmas are divided in five ways.",
            "मर्माणि पञ्चधा भिद्यन्ते."),
        order(1, "Put the printed words of unit 52 in the line's order.",
              ["तस्मान्मां", "साद्याश्रयतो", "मर्माणि", "पंचधा", "भिद्यंते"],
              "Therefore; (flesh and the rest, conjectural); the marmas; in five ways; are divided.",
              "तस्मान्मां → साद्याश्रयतो → मर्माणि → पंचधा → भिद्यंते."),
        match(2, "Match each sure word of unit 52 to its meaning.",
              [["तस्मात्", "therefore"], ["मर्माणि", "marmas"], ["पञ्चधा", "in five ways"], ["भिद्यन्ते", "are divided"]],
              "तस्मात् मर्माणि पञ्चधा भिद्यन्ते: therefore the marmas are divided in five ways.",
              "तस्मात्, मर्माणि, पञ्चधा, भिद्यन्ते.", role="extend",
              teaches="The suffix -धा after a number means 'in so many ways': पञ्च → पञ्चधा."),
        mcq("discriminate", 3, "What form is भिद्यंते in unit 52?",
            ("Present passive, third plural: 'are divided'", "gram: 3 pl. pres. pass. √भिद्."),
            [("Present active, third plural: 'they divide'", "The data labels it passive; the marmas are what is divided."),
             ("Optative, third plural: 'they should divide'", "An optative would not take the present ending -न्ते."),
             ("Past participle, plural: 'divided ones'", "A participle declines like a noun; -न्ते is a verb ending.")],
            "भिद्यन्ते: present passive, third person plural.",
            "Here -यन्ते is passive (data gram); -यते alone does not always prove it."),
        mcq("apply", 4, "Which English rendering of मर्माणि पंचधा भिद्यंते (unit 52) is right?",
            ("The marmas are divided in five ways.", "मर्माणि (the marmas) पञ्चधा (in five ways) भिद्यन्ते (are divided)."),
            [("The marmas divide the body in five.", "भिद्यन्ते is passive: the marmas are divided."),
             ("Five marmas are divided in the body.", "पञ्चधा is 'in five ways', not 'five marmas'."),
             ("The marmas are divided into fifty.", "पञ्चधा is five-fold, not fifty.")],
            "The marmas are divided in five ways.",
            "मर्माणि पञ्चधा भिद्यन्ते."),
        mcq("transfer", 5, "By the pattern of पञ्च → पञ्चधा (in five ways), what does त्रिधा mean in a new example?",
            ("in three ways", "-धा after a number = in so many ways: त्रि → त्रिधा."),
            [("the third one", "'Third' would be तृतीय, not त्रिधा."),
             ("three each", "'Three each' would be त्रिशः, not -धा."),
             ("by three men", "'By three' would be an instrumental (त्रिभिः).")],
            "त्रिधा = in three ways, like पञ्चधा = in five ways.",
            "Number + -धा = in so many ways.",
            teaches="-धा after a number means 'in so many ways': पञ्च → पञ्चधा, त्रि → त्रिधा."),
    ],
}

# ---------------------------------------------------------------- unit 53
AUTHORED["53"] = {
    "title": "तद्यथा",
    "question": "What does the formula तद्यथा (unit 53) mean, and how is it joined?",
    "rule": "तत् + यथा → तद्यथा, 'that is as follows': त् becomes द् before the voiced य.",
    "limits": ("Prose, one printed word, an introductory formula. GROUPING (data): the list begins in unit 54; no question "
               "rests on that link."),
    "explain_hi": ("यह एक शब्द की गद्य-पंक्ति है: ‘तद्यथा’ = वह इस प्रकार है। "
                   "यह परिचय देने वाला सूत्र-शब्द है; डेटा के अनुसार सूची इकाई ५४ से आरम्भ होती है। "
                   "सन्धि: तत् + यथा → तद्यथा; त् घोष य से पहले द् बन जाता है। "
                   "तत् = वह, यथा = जैसे, इस प्रकार।"),
    "hook": "‘तद्यथा’: वह इस प्रकार, त् बना द्।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 53, what does तद्यथा mean?",
            ("That is as follows", "तत् (that) + यथा (as follows)."),
            [("Therefore it is not so", "No negation is printed; तद्यथा introduces."),
             ("Thus the chapter is ended", "That would be an इति formula, not तद्यथा."),
             ("Wherever it may be", "That would be यत्र, not तद्यथा.")],
            "तद्यथा = that is as follows.",
            "तत् + यथा."),
        match(1, "Match each part of unit 53 to its meaning.",
              [["तत्", "that"], ["यथा", "as, as follows"], ["तद्यथा", "that is as follows"]],
              "तत् = that; यथा = as follows; तद्यथा = that is as follows.",
              "तत्, यथा, तद्यथा."),
        fill(2, "Unit 53: तद्यथा = तत् + ____ (as follows). Type it in Devanagari or in English letters (e.g. dharma).",
             accepts("यथा", None, "yatha"),
             "तत् + यथा → तद्यथा.",
             "यथा = as, as follows; त् becomes द् before the voiced य.",
             "तत् + यथा = तद्यथा."),
        mcq("discriminate", 3, "Why is तत् printed तद् in तद्यथा (unit 53)?",
            ("Before voiced य, त् becomes द्", "य is voiced: तत् + यथा → तद्यथा."),
            [("त् becomes द् before every sound", "Not before every sound: before क or प it stays त्."),
             ("य is unvoiced, so the त् softens", "य is voiced, not unvoiced."),
             ("य is a nasal, so the त् has to change", "य is not a nasal; it is a voiced semivowel.")],
            "तत् + यथा: त् before the voiced य → द्.",
            "त् + य (or a vowel, ग, द, ब, व) → द्य ...: तत् + यथा → तद्यथा."),
        mcq("apply", 4, "Which split of तद्यथा (unit 53) is right?",
            ("तत् + यथा", "त् → द् before the voiced य."),
            [("तत् + अथ", "तत् + अथ would give तदथ, with no य."),
             ("त + द्यथा", "द्यथा is not a word; the words are तत् and यथा."),
             ("तद्य + था", "तद्य and था are not the words here.")],
            "तत् (that) + यथा (as follows).",
            "तद्यथा = तत् + यथा."),
        mcq("transfer", 5, "By the rule of तद्यथा, how is जगत् + ईशः (lord of the world) joined in a new example?",
            ("जगदीशः", "त् → द् before a vowel (here ई), as before य in तत् + यथा → तद्यथा."),
            [("जगतीशः", "त् does not stay voiceless before a vowel."),
             ("जगन्नीशः", "न् comes (optionally) from त् before a nasal, not before ई."),
             ("जगच्छीशः", "च्छ comes from त् + श, not from त् + ई.")],
            "जगत् + ईशः = जगदीशः, like तत् + यथा = तद्यथा.",
            "Final त् + vowel → द्.",
            teaches="A final त् becomes द् before a vowel and before voiced consonants such as य, ग, द, ब, व (not before ज, ल or a nasal): तत् + यथा → तद्यथा."),
    ],
}

# ---------------------------------------------------------------- unit 54
AUTHORED["54"] = {
    "title": "एकादश मांसमर्माणि",
    "question": "By unit 54, which marmas are the eleven flesh-marmas (māṃsa-marma)?",
    "rule": ("Talahṛdaya, indrabasti, guda and stanarohita: eleven flesh-marmas (एकादश मांसमर्माणि), the first of the "
             "five kinds announced in unit 52."),
    "limits": ("Verbless prose list. guda = anus, rectum (standard); talahṛdaya and indrabasti regions are probable; "
               "stanarohita is one name (split probable). 'Eleven' counts sides and limbs (data's count check 4+4+1+2, "
               "cards 4, 9, 18, 24); no question rests on that."),
    "explain_hi": ("पाँच प्रकारों में पहला: मांस-मर्म। "
                   "तलहृदय, इन्द्रबस्ति, गुद और स्तनरोहित: ये ग्यारह मांस-मर्म हैं। "
                   "गुद = मलद्वार (मानक); तलहृदय (हथेली या तलवे का मध्य) और इन्द्रबस्ति (पिंडली या अग्रबाहु का मध्य) सम्भावित पहचान हैं; "
                   "स्तनरोहित को एक नाम माना गया (विभाजन सम्भावित)। "
                   "‘ग्यारह’ नामों की संख्या नहीं, हर ओर और हर अंग की गिनती है; डेटा का जोड़ ४ + ४ + १ + २ है (इकाइयाँ ४, ९, १८, २४)। "
                   "सन्धि: तलहृदय + इन्द्रबस्ति → तलहृदयेन्द्रबस्ति (अ + इ → ए)।"),
    "hook": "मांस-मर्म ग्यारह: तलहृदय, इन्द्रबस्ति, गुद, स्तनरोहित।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 54, how many flesh-marmas (māṃsa-marma) are counted?",
            ("Eleven (ekādaśa)", "एकादश मांसमर्माणि: eleven flesh-marmas."),
            [("Forty-one (ekacatvāriṃśat)", "Forty-one is the count of the vessel-marmas (unit 55)."),
             ("Twenty (viṃśati)", "Twenty is the count of the joint-marmas (unit 58)."),
             ("Eight (aṣṭau)", "Eight is the count of the bone-marmas (unit 57).")],
            "Eleven flesh-marmas.",
            "एकादश मांसमर्माणि."),
        order(1, "Put the marma names of unit 54 in the printed order.",
              ["तलहृदय", "इंद्रबस्ति", "गुद", "स्तनरोहित"],
              "Talahṛdaya, indrabasti, guda, stanarohita: eleven flesh-marmas.",
              "तलहृदय → इंद्रबस्ति → गुद → स्तनरोहित."),
        match(2, "Match each word of unit 54 to its meaning.",
              [["मांस", "flesh"], ["मर्म", "vital spot"], ["एकादश", "eleven"], ["गुद", "anus, rectum (standard)"],
               ["स्तन", "breast"]],
              "मांस-मर्म = flesh-marma; एकादश = eleven; गुद = anus, rectum; स्तन = breast (in stanarohita).",
              "मांस, मर्म, एकादश, गुद, स्तन.", role="extend",
              teaches="मांसमर्म is a tat-puruṣa: a marma of flesh, the first of the five kinds."),
        mcq("discriminate", 3, "Which split of तलहृदयेंद्रबस्ति in unit 54 is right?",
            ("तलहृदय + इन्द्रबस्ति", "अ + इ → ए: तलहृदय + इन्द्र → तलहृदयेन्द्र."),
            [("तलहृदय + एन्द्रबस्ति", "अ + ए would give ऐ (तलहृदयैन्द्र), not ए."),
             ("तलहृदये + इन्द्रबस्ति", "ए before इ would give अय्/अ, not ए; and compound members take no case ending."),
             ("तलहृदयी + इन्द्रबस्ति", "ई + इ would give ई, not ए.")],
            "तलहृदय + इन्द्रबस्ति: अ + इ → ए.",
            "अ + इ → ए."),
        multi("apply", 4, "Which are named in unit 54 among the eleven flesh-marmas?",
              [("Nābhi", "Nābhi is a vessel-marma (unit 55)."),
               ("Talahṛdaya", "Right: तलहृदय."),
               ("Mātṛkā", "Mātṛkā is a vessel-marma (unit 55)."),
               ("Guda", "Right: गुद."),
               ("Stanarohita", "Right: स्तनरोहित.")],
              [1, 3, 4],
              "Talahṛdaya, indrabasti, guda and stanarohita are flesh-marmas; nābhi and mātṛkā are vessel-marmas.",
              "तलहृदय-इन्द्रबस्ति-गुद-स्तनरोहितानि एकादश मांसमर्माणि."),
        mcq("transfer", 5, "By the rule of स्तनरोहितान्येकादश, how is वारि + एव (water alone) joined in a new example?",
            ("वार्येव", "इ before a different vowel becomes य्, as स्तनरोहितानि + एकादश → स्तनरोहितान्येकादश."),
            [("वारेव", "The इ cannot simply drop before ए."),
             ("वारैव", "ऐ comes from अ + ए, not from इ + ए."),
             ("वारयेव", "अय् comes from ए before a vowel, not from इ.")],
            "वारि + एव = वार्येव, like स्तनरोहितानि + एकादश.",
            "इ + a different vowel → य्.",
            teaches="इ before a different vowel becomes य्: स्तनरोहितानि + एकादश → स्तनरोहितान्येकादश."),
    ],
}


# ================================================================= NOTES_HI
NOTES_HI = {
    "41": ("गद्य; विश्वास मध्यम; कोई पाठ-चिह्न नहीं। अधूरा वाक्य: क्रिया छपी नहीं, जोड़ी नहीं गई। ‘तत्रोत्क्षेपवत्’ = पिछली इकाई ४० में "
           "उत्क्षेपों के लिए कहे गए आघात-फल के समान; फल यहाँ दोहराया नहीं गया। सन्धि जाँची: भ्रुवोः + मध्ये → भ्रुवोर्मध्ये (ओ के बाद "
           "विसर्ग + घोष व्यंजन → र्); तत्र + उत्क्षेपवत् → तत्रोत्क्षेपवत् (अ + उ → ओ)।"),
    "42": ("गद्य; विश्वास उच्च; कोई पाठ-चिह्न नहीं। पाँच सन्धियाँ सम्भवतः खोपड़ी की सीवनें (सम्भावित, छपा नहीं)। तिर्यक्/ऊर्ध्वम् को सन्धियों "
           "की दिशा पढ़ना सबसे सीधा पाठ है। तृतीया ‘-नाशैः’ = ‘के द्वारा’। छपाई ‘शिरसितिर्यग्’ में शिरसि और तिर्यक् बिना अन्तर के; छपा "
           "पंच = पञ्च। सन्धि जाँची: सीमन्ताः + नाम → सीमन्ता नाम (आ के बाद विसर्ग घोष से पहले लुप्त); तिर्यक् + ऊर्ध्वम् → तिर्यगूर्ध्वम् "
           "(क् स्वर से पहले ग्); तेषु + उन्माद → तेषून्माद (उ + उ → ऊ); नाशैः + मरणम् → नाशैर्मरणम् (ऐ के बाद विसर्ग + घोष → र्)।"),
    "43": ("गद्य; विश्वास उच्च; कोई पाठ-चिह्न नहीं। छपा ‘जिव्हा’ = जिह्वा (मान्य वर्तनी-भेद)। तर्पण = तृप्ति। सिरा के लिए कोई एक आधुनिक "
           "वाहिका नहीं कही गई। शृङ्गाटक मर्म-नाम (शब्दार्थ: त्रिकोण या संगम)। क्रियाहीन वाक्य। सन्धि जाँची: घ्राण + अक्षि → घ्राणाक्षि "
           "(अ + अ → आ); सद्यः + मरणम् → सद्यो मरणम् (अः + घोष व्यंजन → ओ)। ‘सन्निपातः तासां’ छपाई में विसर्ग सहित छपा है।"),
    "44": ("गद्य; विश्वास मध्यम; कोई पाठ-चिह्न नहीं। छपाई ‘मस्तकाभ्यंतरंउपरिष्टात्’ में दोनों शब्द बिना अन्तर के (अन्तर की भूल)। ‘शिरा’ = "
           "सिरा (वर्तनी-भेद)। रोमावर्त = बालों का भँवर, स्थान का वर्णन। अन्तिम ‘इति’ अंश की समाप्ति, अनूदित नहीं। सन्धि जाँची: "
           "उपरिष्टात् + शिरा → उपरिष्टाच्छिरा (त् + श → च्श; स्वर या अन्तःस्थ से पहले विकल्प से च्छ, यहाँ श के बाद इ); सन्निपातः + रोमावर्तः → सन्निपातो रोमावर्तः (अः + घोष व्यंजन → ओ); "
           "सः + अधिपतिः → सोऽधिपतिः (अः + अ → ओऽ); अधिपतिः + नाम → अधिपतिर्नाम; तत्र + अपि → तत्रापि; भवति + इति → भवतीति (इ + इ → ई)।"),
    "45": ("गद्य; विश्वास उच्च; कोई पाठ-चिह्न नहीं। ‘पीडिते’ (सप्तमी, भूत कृदन्त) निर्वैयक्तिक: पीड़ित मर्म समझा जाता है। ‘पुनर्’ = आगे, "
           "नया विषय। क्रियाहीन वाक्य। सन्धि जाँची: रुजा + उत्पत्तिः → रुजोत्पत्तिः (आ + उ → ओ; डेटा का विभाजन ‘ruj-’ इस छपे ओ से मेल नहीं खाता); रुजोत्पत्तिः + विषमम् → रुजोत्पत्तिर्विषमम् (इ के बाद विसर्ग + "
           "घोष → र्); पुनर् + मर्मणाम् → पुनर्मर्मणाम्। छपे ‘स्पंदनं’ और ‘मर्मणां’ में ं।"),
    "46": ("गद्य; विश्वास मध्यम; कोई पाठ-चिह्न नहीं। अधूरा: संज्ञा (सम्भवतः ‘लक्षण’) छपी नहीं, जोड़ी नहीं गई; ‘सामान्येन’ = ‘सामान्य रूप "
           "से’ भी हो सकता है। समूह-टिप्पणी (डेटा): इकाई ४५ को आगे बढ़ाती और इकाई ४७ की सूची का परिचय देती दिखती है। डेटा का विभाजन: "
           "सामान्येन + एव → सामान्येनैव (अ + ए → ऐ); निश्चित नहीं, इस पर कोई प्रश्न नहीं।"),
    "47": ("श्लोक (अनुष्टुभ्), दो पंक्तियाँ; विश्वास निम्न। पाठ-चिह्न (सम्भावित): पहला शब्द ‘देहप्रमुसि’ ज्ञात शब्द नहीं, क्षतिग्रस्त; "
           "‘देहप्रसुप्ति’ जैसा कोई शरीर-लक्षण हो सकता है, पर कोई पुनर्स्थापन स्वीकार नहीं; अविभक्त, अस्पष्ट और अनूदित; इस पर कोई प्रश्न नहीं। "
           "‘वमिः’ मान्य रूप। श्वास = साँस का कष्ट (आधुनिक अर्थ dyspnoea सम्भावित)। सन्धि जाँची: स्वेदः + मूर्च्छा → स्वेदो मूर्च्छा "
           "(छपा ‘स्वेदोमूर्च्छा’, बिना अन्तर); श्वासः + मर्म → श्वासो मर्म (अः + घोष व्यंजन → ओ); देहप्रमुसिः + गुरुता → देहप्रमुसिर्गुरुता।"),
    "48": ("गद्य; विश्वास उच्च; कोई पाठ-चिह्न नहीं। अपि + च बिना अन्तर के छपे; कोई सन्धि-परिवर्तन नहीं (व्यंजन से पहले स्वर नहीं बदलता)। "
           "समूह-टिप्पणी (डेटा): अगली इकाई ४९ को खोलती है।"),
    "49": ("गद्य; विश्वास मध्यम; कोई पाठ-चिह्न नहीं। क्रियाहीन। छपा ‘स्नाव’ = स्नायु (दोनों रूप मिलते हैं)। ‘सन्धि’ पाँचवाँ सदस्य माना गया; "
           "‘अस्थि-सन्धि’ भी सम्भव, शब्दों से तय नहीं; इस पर कोई प्रश्न नहीं। पाठ की अपनी व्याख्या; कोई व्युत्पत्ति नहीं जोड़ी। सन्धि जाँची: "
           "मरणकारित्वात् + मर्म → मरणकारित्वान्मर्म (त् अनुनासिक म से पहले न्; यह परिवर्तन वैकल्पिक है); स्नाव + अस्थि → स्नावास्थि "
           "(अ + अ → आ); तत् + पुनर् → तत्पुनर्।"),
    "50": ("गद्य; विश्वास मध्यम; कोई पाठ-चिह्न नहीं। क्रियाहीन। ‘तस्मिन्’ की संज्ञा छपी नहीं। पीड्यमाने = वर्तमान कर्मवाच्य कृदन्त, सप्तमी "
           "एकवचन। प्राण = प्राण-वायु, जीवन (‘life-breath’)। सन्धि जाँची: प्राण + आबाधः → प्राणाबाधः (अ + आ → आ); ‘तस्मिन् पीड्यमाने’ "
           "अलग छपे।"),
    "51": ("गद्य; विश्वास मध्यम; कोई पाठ-चिह्न नहीं। क्रियाहीन। डेटा की व्याख्या (नाम प्रधानता से, ठीक नियम से नहीं) अनुवाद से बाहर रखी गई; "
           "इस पर कोई प्रश्न नहीं। कोई सन्धि-परिवर्तन नहीं।"),
    "52": ("गद्य; विश्वास मध्यम। पाठ-चिह्न (सम्भावित): छपा ‘तस्मान्मां साद्याश्रयतो’ में ‘मां सादि’ के बीच अनावश्यक अन्तर दिखता है; अनुमानित "
           "पाठ ‘मांसाद्याश्रयतः’ (मांस आदि के आश्रय से), जिसे आगे की इकाइयाँ ५४-५८ (मांस, सिरा, स्नायु, अस्थि, सन्धि मर्म) समर्थन देती हैं; "
           "इस पर कोई प्रश्न नहीं। भिद्यन्ते = वर्तमान कर्मवाच्य, प्रथम पुरुष बहुवचन। सन्धि जाँची: तस्मात् + मां(स) → तस्मान्मां (त् अनुनासिक "
           "से पहले न्, वैकल्पिक); आश्रयतः + मर्माणि → आश्रयतो मर्माणि (अः + घोष व्यंजन → ओ)।"),
    "53": ("गद्य; विश्वास उच्च; कोई पाठ-चिह्न नहीं। परिचय-सूत्र; डेटा के अनुसार सूची इकाई ५४ से। सन्धि जाँची: तत् + यथा → तद्यथा "
           "(त् घोष य से पहले द्)।"),
    "54": ("गद्य; विश्वास मध्यम; कोई पाठ-चिह्न नहीं। क्रियाहीन सूची; इकाई ५२ में घोषित पाँच भेदों में पहला (मांस-मर्म)। ‘स्तनरोहित’ एक नाम माना "
           "गया (विभाजन सम्भावित)। पहचान: गुद = मलद्वार (मानक); तलहृदय, इन्द्रबस्ति के क्षेत्र सम्भावित (टीका-परम्परा से, इस पंक्ति से नहीं)। "
           "डेटा का गणना-निरीक्षण: तलहृदय ४ + इन्द्रबस्ति ४ (इकाई ४, ९) + गुद १ (इकाई १८) + स्तनरोहित २ (इकाई २४) = ११; छपा नहीं। "
           "सन्धि जाँची: तलहृदय + इन्द्रबस्ति → तलहृदयेन्द्रबस्ति (अ + इ → ए); स्तनरोहितानि + एकादश → स्तनरोहितान्येकादश (इ + भिन्न स्वर → य्); "
           "छपा इंद्र = इन्द्र।"),
}


# ===================================================================== AIDS
AIDS = {
    "41": {
        "chunks": "भ्रुवोर्मध्ये | स्थपनी | तत्रोत्क्षेपवत्",
        "frame": "कहाँ: भ्रुवोर्मध्ये (दोनों भौंहों के बीच) → कौन: स्थपनी → फल: उत्क्षेपवत् (इकाई ४० के उत्क्षेप जैसा)।",
        "sandhi": "ओ के बाद विसर्ग + घोष व्यंजन → र्: भ्रुवोः + मध्ये → भ्रुवोर्मध्ये · अ + उ → ओ: तत्र + उत्क्षेपवत् → तत्रोत्क्षेपवत्।",
    },
    "42": {
        "diagram": {"groups": [
            {"label": "सीमन्त: सिर पर पाँच सन्धियाँ", "items": ["तिरछी और ऊपर की ओर", "उन्माद", "भ्रम (चक्कर)",
                                                        "चित्त-नाश", "इनके द्वारा मरण"]}]},
        "chunks": "पंच संधयः | शिरसितिर्यगूर्ध्वं च | सीमंता नाम | तेषून्मादभ्रमचित्तनाशैर्मरणं",
        "sandhi": ("आ के बाद विसर्ग घोष से पहले लुप्त: सीमन्ताः + नाम → सीमन्ता नाम · उ + उ → ऊ: तेषु + उन्माद → तेषून्माद · "
                   "ऐ के बाद विसर्ग + घोष → र्: नाशैः + मरणम् → नाशैर्मरणम्।"),
    },
    "43": {
        "diagram": {"groups": [
            {"label": "शृङ्गाटक (इकाई ४३)", "items": ["जीभ, नाक, आँख, कान की तर्पणी सिराएँ", "तालु में सन्निपात",
                                                  "उनके चार मुख: शृङ्गाटक", "उनमें तत्काल मरण"]}]},
        "chunks": "जिव्हाघ्राणाक्षिश्रोत्रतर्पणीनां सिराणां | तालुनि सन्निपातः | तासां मुखानि चत्वारि | शृंगाटकसंज्ञानि | तेषु सद्यो मरणं",
        "sandhi": "अ + अ → आ: घ्राण + अक्षि → घ्राणाक्षि · अः + घोष व्यंजन → ओ: सद्यः + मरणम् → सद्यो मरणम्।",
    },
    "44": {
        "chain": {"steps": ["मस्तक के भीतर, ऊपर", "सिरा और सन्धि का सन्निपात", "रोमावर्त: बालों का भँवर",
                            "नाम: अधिपति", "वहाँ भी तत्काल मरण"]},
        "chunks": "मस्तकाभ्यंतरंउपरिष्टाच्छिरासंधिसन्निपातो | रोमावर्तः | सोऽधिपतिर्नाम | तत्रापि सद्यो मरणं भवतीति",
        "sandhi": ("अः + अ → ओऽ: सः + अधिपतिः → सोऽधिपतिः · त् + श → च्श, और स्वर या अन्तःस्थ से पहले विकल्प से च्छ (यहाँ श के बाद इ): उपरिष्टात् + शिरा → उपरिष्टाच्छिरा · "
                   "अ + अ → आ: तत्र + अपि → तत्रापि।"),
    },
    "45": {
        "diagram": {"groups": [
            {"label": "मर्मों का सामान्य लक्षण: पीडिते (दबने या चोट पर)", "items": ["रुजोत्पत्ति: पीड़ा उठना",
                                                                          "विषम स्पन्दन: अनियमित स्पन्दन (क्या, यह छपा नहीं)"]}]},
        "chunks": "सामान्यलक्षणं | पुनर्मर्मणां | पीडिते | रुजोत्पत्तिर्विषमं च | स्पंदनं",
        "sandhi": "इ के बाद विसर्ग + घोष व्यंजन → र्: रुजोत्पत्तिः + विषमम् → रुजोत्पत्तिर्विषमम्।",
    },
    "46": {
        "chunks": "सामान्येनैव | च",
        "sandhi": "डेटा का विभाजन (निश्चित नहीं): सामान्येन + एव → सामान्येनैव (अ + ए → ऐ)।",
        "frame": "किससे: सामान्येन (सामान्य से) → बल: एव (ही) → जोड़: च (और); संज्ञा छपी नहीं। (विभाजन डेटा का पाठ)",
    },
    "47": {
        "diagram": {"groups": [
            {"label": "मर्मविद्धस्य लक्षणम् (छपे क्रम में)", "items": ["देहप्रमुसि: अस्पष्ट, अनूदित नहीं", "गुरुता: भारीपन",
                                                               "संमोह: भ्रम", "शीतकामिता: ठंड की इच्छा",
                                                               "स्वेद: पसीना", "मूर्च्छा: बेहोशी", "वमि: उल्टी",
                                                               "श्वास: साँस का कष्ट"]}]},
        "chunks": "देहप्रमुसिर्गुरुता | संमोहः | शीतकामिता || स्वेदोमूर्च्छा | वमिः | श्वासो | मर्मविद्धस्य लक्षणं",
        "sandhi": "अः + घोष व्यंजन → ओ: स्वेदः + मूर्च्छा → स्वेदो मूर्च्छा; श्वासः + मर्म → श्वासो मर्म।",
        "anchors": "-ता से भाववाचक संज्ञा: गुरु → गुरुता (भारीपन), शीतकामिन् → शीतकामिता (ठंड की चाह)।",
    },
    "48": {
        "chunks": "अपि | च",
        "frame": "अपि (भी) + च (और) = और भी: अगला कथन खोलने वाला सूत्र।",
        "sandhi": "व्यंजन से पहले स्वर नहीं बदलता: अपि + च → अपि च (छपा ‘अपिच’); पर स्वर से पहले इ → य्: अपि + अहम् → अप्यहम्।",
    },
    "49": {
        "diagram": {"groups": [
            {"label": "मर्म: मरणकारित्वात् (मृत्यु कराने से)", "items": ["१ मांस", "२ सिरा", "३ स्नाव (स्नायु)", "४ अस्थि",
                                                                  "५ सन्धि (पाँचवाँ सदस्य, डेटा का पाठ)",
                                                                  "इनका सन्निपात = मर्म"]}]},
        "chunks": "मरणकारित्वान्मर्म | तत्पुनर्मांससिरास्नावस्थिसंधिसन्निपातः",
        "sandhi": ("त् अनुनासिक से पहले न् (वैकल्पिक): मरणकारित्वात् + मर्म → मरणकारित्वान्मर्म · अ + अ → आ: स्नाव + अस्थि → "
                   "स्नावास्थि।"),
        "anchors": "‘जो मारे वह मर्म’: मरण से मर्म याद रखें (मेरी याद-पद्धति, पाठ का दावा नहीं; पाठ केवल ‘मरणकारित्वात्’ कहता है)।",
    },
    "50": {
        "chain": {"steps": ["तेन: इसलिए", "तस्मिन् पीड्यमाने: उसके दबाए जाते समय", "विशेषतः: विशेष रूप से",
                            "प्राणाबाधः: प्राण को बाधा"]},
        "chunks": "तेन | तस्मिन् | पीड्यमाने | विशेषतः | प्राणाबाधः",
        "sandhi": "अ + आ → आ: प्राण + आबाधः → प्राणाबाधः।",
    },
    "51": {
        "chunks": "बाहुल्येन | तु | निर्देशः",
        "frame": "कैसे: बाहुल्येन (प्रधानता से) → जोड़: तु (किन्तु) → क्या: निर्देशः (नाम देना)।",
        "anchors": "अ-अन्त शब्द की तृतीया एकवचन -एन: बाहुल्य → बाहुल्येन, ज्ञान → ज्ञानेन।",
    },
    "52": {
        "chunks": "तस्मान्मां | साद्याश्रयतो | मर्माणि | पंचधा | भिद्यंते",
        "frame": "क्यों: तस्मात् (इसलिए) → किस आधार पर: मांसाद्याश्रयतः (अनुमानित पाठ) → क्या: मर्माणि → कैसे: पञ्चधा (पाँच प्रकार) → भिद्यन्ते।",
        "anchors": "संख्या + -धा = उतने प्रकार से: पञ्चधा (पाँच प्रकार), त्रिधा (तीन प्रकार)।",
    },
    "53": {
        "chunks": "तद्यथा",
        "sandhi": "त् स्वर और य, ग, द, ब, व जैसे घोष व्यंजनों से पहले द् (ज, ल, अनुनासिक से पहले नहीं): तत् + यथा → तद्यथा; जगत् + ईशः → जगदीशः।",
        "frame": "तत् (वह) + यथा (इस प्रकार) = वह इस प्रकार है: सूची का परिचय।",
    },
    "54": {
        "diagram": {"groups": [
            {"label": "एकादश मांसमर्माणि (छपे क्रम में)", "items": ["१ तलहृदय: हथेली/तलवे का मध्य (सम्भावित)",
                                                            "२ इन्द्रबस्ति: पिंडली/अग्रबाहु का मध्य (सम्भावित)",
                                                            "३ गुद: मलद्वार (मानक)", "४ स्तनरोहित: एक नाम (सम्भावित विभाजन)"]}]},
        "chunks": "तलहृदयेंद्रबस्तिगुदस्तनरोहितान्येकादश | मांसमर्माणि",
        "sandhi": ("अ + इ → ए: तलहृदय + इन्द्रबस्ति → तलहृदयेन्द्रबस्ति · इ + भिन्न स्वर → य्: स्तनरोहितानि + एकादश → "
                   "स्तनरोहितान्येकादश।"),
        "anchors": "डेटा का गणना-निरीक्षण (छपा नहीं): ४ + ४ + १ + २ = ११, हर ओर और हर अंग गिनकर।",
    },
}


# ============================================================== IMAGE_SPECS
IMAGE_SPECS = {
    ("42", "diagram"): {
        "file": "sh7-simanta-42.svg",
        "alt": ("Flowchart of unit 42: five joints on the head, transverse and upward, called sīmanta; in them, injury "
                "(understood) leads by way of insanity, giddiness and loss of mind to death."),
        "type": "mermaid",
        "code": ("flowchart TD\n"
                 "  A[\"सिर पर पाँच सन्धियाँ\"] --> B[\"तिरछी और ऊपर की ओर\"]\n"
                 "  B --> C[\"नाम: सीमन्त\"]\n"
                 "  C --> D[\"उन्माद\"]\n"
                 "  C --> E[\"भ्रम\"]\n"
                 "  C --> F[\"चित्त-नाश\"]\n"
                 "  D --> G[\"इनके द्वारा मरण\"]\n"
                 "  E --> G\n"
                 "  F --> G\n"),
    },
    ("43", "diagram"): {
        "file": "sh7-shringataka-43.svg",
        "alt": ("Flowchart of unit 43: the satiating vessels of tongue, nose, eye and ear meet in the palate; their four "
                "mouths are named śṛṅgāṭaka; in them, death at once."),
        "type": "mermaid",
        "code": ("flowchart TD\n"
                 "  A[\"जीभ, नाक, आँख, कान\"] --> B[\"इनकी तर्पणी सिराएँ\"]\n"
                 "  B --> C[\"तालु में सन्निपात\"]\n"
                 "  C --> D[\"उनके चार मुख\"]\n"
                 "  D --> E[\"नाम: शृङ्गाटक\"]\n"
                 "  E --> F[\"उनमें तत्काल मरण\"]\n"),
    },
    ("44", "chain"): {
        "file": "sh7-adhipati-44.svg",
        "alt": ("Chain of unit 44 in line order: inside the head, above; the meeting of vessels and joints; a whorl of "
                "hair; called adhipati; there too death at once."),
        "type": "chain",
        "title": "इकाई ४४: अधिपति",
        "steps": ["मस्तक के भीतर, ऊपर", "सिरा और सन्धि का सन्निपात", "रोमावर्त: बालों का भँवर", "नाम: अधिपति",
                  "वहाँ भी तत्काल मरण"],
    },
    ("45", "diagram"): {
        "file": "sh7-samanya-lakshana-45.svg",
        "alt": ("Flowchart of unit 45: when a marma is pressed or injured, two general signs: arising of pain and "
                "irregular throbbing."),
        "type": "mermaid",
        "code": ("flowchart TD\n"
                 "  A[\"मर्म पीडित होने पर\"] --> B[\"रुजोत्पत्ति: पीड़ा उठना\"]\n"
                 "  A --> C[\"विषम स्पन्दन\"]\n"),
    },
    ("47", "diagram"): {
        "file": "sh7-marmaviddha-47.svg",
        "alt": ("Table of unit 47 in printed order: dehapramusi (damaged, untranslated), heaviness, bewilderment, desire "
                "for cold, sweating, fainting, vomiting, laboured breathing: the sign of one pierced in a marma."),
        "type": "table",
        "title": "इकाई ४७: मर्मविद्धस्य लक्षणम्",
        "heads": ["छपा शब्द", "अर्थ"],
        "rows": [["१ देहप्रमुसि", "अस्पष्ट (क्षतिग्रस्त)"], ["२ गुरुता", "भारीपन"], ["३ संमोह", "भ्रम"],
                 ["४ शीतकामिता", "ठंड की इच्छा"], ["५ स्वेद", "पसीना"], ["६ मूर्च्छा", "बेहोशी"], ["७ वमि", "उल्टी"],
                 ["८ श्वास", "साँस का कष्ट"]],
    },
    ("49", "diagram"): {
        "file": "sh7-marma-sannipata-49.svg",
        "alt": ("Table of unit 49: a marma is so called because it causes death; it is the meeting of the members, "
                "numbered in printed order (five as the data reads it): flesh, vessel, sinew (snāva = snāyu), bone, joint (the fifth as the data reads it)."),
        "type": "table",
        "title": "इकाई ४९: मर्म = सन्निपात",
        "heads": ["छपा शब्द", "अर्थ"],
        "rows": [["मरणकारित्वात्", "मृत्यु कराने से: मर्म"], ["१ मांस", "मांस"], ["२ सिरा", "सिरा"],
                 ["३ स्नाव", "स्नायु"], ["४ अस्थि", "हड्डी"], ["५ सन्धि", "जोड़ (डेटा का पाठ)"]],
    },
    ("54", "diagram"): {
        "file": "sh7-mamsa-marma-54.svg",
        "alt": ("Table of unit 54 in printed order: talahṛdaya (centre of palm or sole, probable), indrabasti (mid-calf "
                "or mid-forearm, probable), guda (anus, standard), stanarohita (one name, split probable): eleven "
                "flesh-marmas."),
        "type": "table",
        "title": "इकाई ५४: एकादश मांसमर्माणि",
        "heads": ["छपा नाम", "क्षेत्र (डेटा का लेबल)"],
        "rows": [["१ तलहृदय", "हथेली/तलवे का मध्य (सम्भावित)"], ["२ इन्द्रबस्ति", "पिंडली/अग्रबाहु मध्य (सम्भावित)"],
                 ["३ गुद", "मलद्वार (मानक)"], ["४ स्तनरोहित", "एक नाम (सम्भावित विभाजन)"], ["कुल", "एकादश (११)"]],
    },
}
