from helpers import mcq, match, order, fill, multi, accepts


AUTHORED = {}

# ---------------------------------------------------------------- unit 28
AUTHORED["28"] = {
    "title": "पृष्ठवंशमुभयतः कुकुंदरौ",
    "question": "By unit 28, where are the two kukundara marmas, and what follows injury to them?",
    "rule": ("On the two sides, in the outer part of the jaghana (probably the hip region), on both sides of the spine "
             "(पृष्ठवंशम् उभयतः): the two kukundaras. In those two: loss of movement (चेष्टानाशः), and a touch-word whose "
             "reading is conjectural."),
    "limits": ("Prose; no verb is printed and the injury is understood. Printed स्पर्शज्ञानम् ('knowledge of touch') is "
               "read by conjecture as स्पर्शाज्ञानम् ('no perception of touch'), or a word for 'loss' has dropped; no question "
               "rests on this word. Jaghana = hip region is probable only."),
    "explain_hi": ("यह गद्य-पंक्ति दो कुकुन्दर मर्मों का स्थान और उनके आघात का फल बताती है। "
                   "स्थान: दोनों पार्श्वों में, जघन यानी सम्भवतः कूल्हे के क्षेत्र के बाहरी भाग में, रीढ़ के दोनों ओर। "
                   "फल (पक्का भाग): चेष्टा यानी हिलने-डुलने का नाश। "
                   "छपा ‘स्पर्शज्ञानम्’ (स्पर्श का ज्ञान) हानियों की सूची में ठीक नहीं बैठता; अनुमानित पाठ ‘स्पर्शाज्ञानम्’ (स्पर्श का अनुभव न होना) है, इसलिए इस शब्द पर कोई प्रश्न नहीं। "
                   "आघात शब्द छपा नहीं, समझा जाता है।"),
    "hook": "रीढ़ के दोनों ओर कुकुन्दर: चोट लगे तो चेष्टा का नाश।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 28, what sure loss follows injury (understood) to the two kukundaras?",
            ("Loss of movement", "चेष्टानाशश्च: and loss of movement."),
            [("Loss of hearing", "Deafness belongs to the vidhuras (card 36), not to the kukundaras."),
             ("Loss of smell", "Loss of smell belongs to the phaṇas (card 37), not to the kukundaras."),
             ("Stiffness of the arms", "Stiff arms belong to the aṃsas (card 33), not to the kukundaras.")],
            "The sure result printed for the kukundaras is loss of movement (चेष्टानाश).",
            "तयोः ... चेष्टानाशश्च."),
        order(1, "Put these printed parts of unit 28 in the line's order.",
              ["पार्श्वयोर्जघनबहिर्भागे", "पृष्ठवंशमुभयतः", "कुकुंदरौ", "तयोः", "चेष्टानाशश्च"],
              "Place (sides, outer part of the jaghana), place (both sides of the spine), name, 'in those two', result.",
              "पार्श्वयोर्जघनबहिर्भागे → पृष्ठवंशमुभयतः → कुकुंदरौ → तयोः → चेष्टानाशश्च."),
        match(2, "Match each word of unit 28 to its meaning.",
              [["पार्श्व", "side"], ["पृष्ठवंश", "spine"], ["उभयतः", "on both sides"], ["चेष्टा", "movement"],
               ["नाश", "loss"]],
              "पार्श्वयोः = on the two sides; पृष्ठवंशम् उभयतः = on both sides of the spine; चेष्टानाशः = loss of movement.",
              "पार्श्व, पृष्ठवंश, उभयतः, चेष्टा, नाश.", role="extend",
              teaches="उभयतः ('on both sides') takes an accusative: पृष्ठवंशम् उभयतः = on both sides of the spine."),
        mcq("discriminate", 3, "Which split of पार्श्वयोर्जघनबहिर्भागे in unit 28 is right?",
            ("पार्श्वयोः + जघन + बहिः + भागे", "ओः and इः before the voiced ज and भ show र्: -योर्ज-, -हिर्भा-."),
            [("पार्श्वयः + जघन + बहिः + भागे", "अः before the voiced ज would give ओ with no र् (पार्श्वयो जघन)."),
             ("पार्श्वयोः + जघन + बहि + भागे", "बहि is no word; the र् of -हिर्भा- comes from the visarga of बहिः."),
             ("पार्श्वयोः + जघन + बहिः + अभागे", "बहिः + अभागे would give बहिरभागे; the print has -हिर्भागे.")],
            "पार्श्वयोः (on the two sides) + जघन + बहिः (outside) + भागे (in the part).",
            "After a vowel other than अ/आ, a visarga before a voiced sound → र्."),
        multi("apply", 4, "Which statements fit unit 28?",
              [("The line says death comes at once", "No death is printed for the kukundaras in unit 28."),
               ("The kukundaras lie on both sides of the spine", "Right: पृष्ठवंशमुभयतः कुकुंदरौ."),
               ("Injury brings stiffness of the arms", "Stiff arms are the result for the aṃsas (card 33)."),
               ("Injury (understood) brings loss of movement", "Right: चेष्टानाशश्च.")],
              [1, 3],
              "Both sides of the spine; loss of movement.",
              "पृष्ठवंशमुभयतः कुकुंदरौ तयोः ... चेष्टानाशश्च."),
        mcq("transfer", 5, "By the rule of बहिर्भागे (बहिः + भागे), how is अग्निः + ज्वलति (fire burns) joined in a new example?",
            ("अग्निर्ज्वलति", "After इ a visarga before the voiced ज → र्, as बहिः + भागे → बहिर्भागे."),
            [("अग्निस्ज्वलति", "स् comes before त or थ, not before ज."),
             ("अग्नि ज्वलति", "The visarga drops before a voiced sound after आ, not after इ."),
             ("अग्नो ज्वलति", "ओ comes from अः before a voiced consonant; here the vowel is इ.")],
            "अग्निः + ज्वलति = अग्निर्ज्वलति, like बहिः + भागे = बहिर्भागे.",
            "इः / उः + voiced sound → इर् / उर्.",
            teaches="After इ or उ a visarga becomes र् before a voiced sound: बहिः + भागे → बहिर्भागे."),
    ],
}

# ---------------------------------------------------------------- unit 29
AUTHORED["29"] = {
    "title": "शोफो दौर्बल्यं मरणं च",
    "question": "By unit 29, where are the two nitamba marmas, and which three results are printed for them?",
    "rule": ("Above the two śroṇīkarṇas, covering the āśaya (an unnamed receptacle) and bound to the interior of the sides: "
             "the two nitambas. In those two: swelling (शोफः) and weakness (दौर्बल्यम्) in the lower body, and death (मरणम्)."),
    "limits": ("Prose; the injury is understood. 'āśaya' is not named as an organ. Printed पार्श्वन्तर may stand for "
               "पार्श्वान्तर (long ā dropped), and the sense of 'antara' is not firm; the full stop in अध. stands for the visarga. "
               "No question rests on those two words."),
    "explain_hi": ("यह गद्य-पंक्ति दो नितम्ब मर्मों का स्थान और फल बताती है। "
                   "स्थान: दोनों श्रोणिकर्णों के ऊपर; ये आशय (भीतर का कोई स्थान, जिसका नाम नहीं दिया गया) को ढकते हैं और पार्श्वों के भीतरी भाग से बँधे हैं। "
                   "फल: निचले शरीर में शोफ यानी सूजन, दुर्बलता, और मृत्यु। "
                   "‘पार्श्वन्तर’ में दीर्घ आ छूटा लगता है (पार्श्वान्तर), और ‘अध.’ में बिन्दु विसर्ग के स्थान पर है; इन पर कोई प्रश्न नहीं। "
                   "‘शोफो दौर्बल्यं’ में अः घोष व्यंजन द से पहले ओ बना है।"),
    "hook": "नितम्ब पर चोट: सूजन, कमज़ोरी और मृत्यु।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 29, which results follow injury (understood) to the two nitambas?",
            ("Swelling, weakness and death", "शोफो दौर्बल्यं मरणं च: swelling, weakness and death."),
            [("Lameness, pain and numbness", "None of these three is printed in unit 29."),
             ("Deafness, blindness and dumbness", "These belong to head and neck marmas (cards 34-39)."),
             ("Cough, śvāsa and death", "Cough (kāsa) and śvāsa (probably breathlessness) go with the apastambhas (card 25).")],
            "Three results: swelling (शोफ), weakness (दौर्बल्य) and death (मरण).",
            "शोफो दौर्बल्यं मरणं च."),
        order(1, "Put these printed parts of unit 29 in the line's order.",
              ["श्रोणीकर्णयोरुपर्याशयाच्छादनौ", "नितंबौ", "तयोः", "शोफो", "दौर्बल्यं", "मरणं च"],
              "Place and covering, name, 'in those two', then swelling, weakness and death.",
              "श्रोणीकर्णयोरुपर्याशयाच्छादनौ → नितंबौ → तयोः → शोफो → दौर्बल्यं → मरणं च."),
        match(2, "Match each word of unit 29 to its meaning.",
              [["उपरि", "above"], ["आच्छादन", "covering"], ["शोफ", "swelling"], ["दौर्बल्य", "weakness"],
               ["मरण", "death"]],
              "उपरि = above; आशयाच्छादनौ = covering the āśaya; शोफ, दौर्बल्य, मरण = swelling, weakness, death.",
              "उपरि, आच्छादन, शोफ, दौर्बल्य, मरण.", role="extend",
              teaches="दौर्बल्य is the abstract noun of दुर्बल (weak), made with vṛddhi (उ → औ) and -य: 'weakness'."),
        mcq("discriminate", 3, "Which split of उपर्याशयाच्छादनौ in unit 29 is right?",
            ("उपरि + आशय + आच्छादनौ", "इ + आ → या (उपर्याशय); अ + आ → आ (आशयाच्छादनौ)."),
            [("उपरि + अशय + आच्छादनौ", "इ + अ would give a short -र्य- (उपर्यशय); the print has the long -र्या-."),
             ("उपर + याशय + आच्छादनौ", "उपर and याशय are not words here; the य् comes from the इ of उपरि."),
             ("उपरि + आशय + च्छादनौ", "च्छादनौ is not a word; the word is आच्छादन, covering.")],
            "उपरि (above) + आशय (receptacle) + आच्छादनौ (the two covering).",
            "इ + आ → या; अ + आ → आ."),
        mcq("apply", 4, "In शोफो दौर्बल्यं of unit 29, why is शोफः printed शोफो?",
            ("अः before the voiced द → ओ", "द is a voiced consonant: शोफः + दौर्बल्यम् → शोफो दौर्बल्यम्."),
            [("अः before any consonant → ओ", "Not any consonant: before त it becomes स्, before च श्."),
             ("ओ is the ending of शोफ here", "शोफः is m. nom. sg.; ओ here comes only from sandhi."),
             ("दौर्बल्यं begins with a vowel", "दौर्बल्यम् begins with the consonant द.")],
            "शोफः + दौर्बल्यम्: अः before the voiced consonant द → ओ.",
            "अः + voiced consonant → ओ."),
        mcq("transfer", 5, "By the rule of उपर्याशय (उपरि + आशय), how is इति + आह (thus he said) joined in a new example?",
            ("इत्याह", "इ before आ becomes य्, as उपरि + आशय → उपर्याशय."),
            [("इताह", "The इ does not simply drop before आ."),
             ("इतीह", "ई would come from इ + इ, not from इ + आ."),
             ("इत्यह", "The आ of आह stays long: -त्या-.")],
            "इति + आह = इत्याह, like उपरि + आशय = उपर्याशय.",
            "इ + आ → या.",
            teaches="इ before a different vowel becomes य्: उपरि + आशय → उपर्याशय."),
    ],
}

# ---------------------------------------------------------------- unit 30
AUTHORED["30"] = {
    "title": "तिर्यगूर्ध्वं च पार्श्वसंधी",
    "question": "By unit 30, where are the two pārśvasandhis, and how does injury to them lead to death?",
    "rule": ("Bound to the lower interior of the sides, between the jaghana (probably the hip region) and the side, slanting "
             "and upward: the two pārśvasandhis (side-joints). In those two: death through the koṣṭha being full of blood "
             "(शोणितपूर्णकोष्ठतया)."),
    "limits": ("Prose; injury understood. Printed पार्श्वन्तर may stand for पार्श्वान्तर (long ā dropped, as in unit 29), and the "
               "sense of 'antara' is not firm; no question rests on that word. तिर्यगूर्ध्वं च is read as the direction, not a "
               "separate marma."),
    "explain_hi": ("यह गद्य-पंक्ति दो पार्श्वसन्धि मर्मों का स्थान और फल बताती है। "
                   "स्थान: पार्श्वों के निचले भीतरी भाग से बँधे, जघन (सम्भवतः कूल्हे का क्षेत्र) और पार्श्व के बीच, तिरछे और ऊपर की ओर। "
                   "फल: कोष्ठ के रक्त से भर जाने के कारण मृत्यु। "
                   "‘तिर्यगूर्ध्वं च’ दिशा बताता है, कोई अलग मर्म नहीं (डेटा का पाठ)। "
                   "‘तिर्यगूर्ध्वं’ में तिर्यक् का क् स्वर ऊ से पहले ग् बना है।"),
    "hook": "पार्श्वसन्धि पर चोट: कोष्ठ रक्त से भरे, मृत्यु।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 30, how does injury (understood) to the two pārśvasandhis cause death?",
            ("Koṣṭha filling with blood", "शोणितपूर्णकोष्ठतया: by the koṣṭha being full of blood."),
            [("Kapha filling the koṣṭha", "A koṣṭha full of Kapha is said of the stanamūlas (card 23)."),
             ("Blood turning into pus", "Blood turned to pus is said of the apālāpas (card 26)."),
             ("Through ākṣepaka (spasm?)", "Ākṣepaka (probably a convulsive spasm) is said of kṣipra (card 5).")],
            "Death comes through the koṣṭha being full of blood.",
            "तयोः शोणितपूर्णकोष्ठतया मरणं."),
        order(1, "Put these printed parts of unit 30 in the line's order.",
              ["जघनपार्श्वमध्ये", "तिर्यगूर्ध्वं च", "पार्श्वसंधी", "तयोः", "शोणितपूर्णकोष्ठतया", "मरणं"],
              "Place (between jaghana and side), direction, name, 'in those two', cause, death.",
              "जघनपार्श्वमध्ये → तिर्यगूर्ध्वं च → पार्श्वसंधी → तयोः → शोणितपूर्णकोष्ठतया → मरणं."),
        match(2, "Match each word of unit 30 to its meaning.",
              [["मध्ये", "in the middle"], ["तिर्यक्", "slantwise"], ["ऊर्ध्वम्", "upward"], ["शोणित", "blood"],
               ["पूर्ण", "full"]],
              "मध्ये = in the middle; तिर्यगूर्ध्वम् = slanting and upward; शोणितपूर्ण = full of blood.",
              "मध्ये, तिर्यक्, ऊर्ध्वम्, शोणित, पूर्ण.", role="extend",
              teaches="-तया (instrumental of an abstract in -ता) gives the cause: शोणितपूर्णकोष्ठतया = through the koṣṭha being full of blood."),
        mcq("discriminate", 3, "Which split of तिर्यगूर्ध्वं in unit 30 is right?",
            ("तिर्यक् + ऊर्ध्वम्", "A final क् before a vowel becomes ग्: तिर्यगूर्ध्वम्."),
            [("तिर्य + गूर्ध्वम्", "Neither तिर्य nor गूर्ध्वम् is a word; the ग् is the क् of तिर्यक्."),
             ("तिर्यक् + गूर्ध्वम्", "गूर्ध्वम् is not a word; the word is ऊर्ध्वम्, upward."),
             ("तिर्यक् + उर्ध्वम्", "A short उ would give -गु-; the print has -गू-, from ऊर्ध्वम्.")],
            "तिर्यक् (slantwise) + ऊर्ध्वम् (upward).",
            "क् + vowel → ग् + vowel."),
        mcq("apply", 4, "In तिर्यगूर्ध्वं of unit 30, why is the क् of तिर्यक् written ग्?",
            ("It stands before a vowel", "Before a vowel (a voiced sound) a final क् becomes ग्."),
            [("It stands before any sound", "Before a voiceless consonant (e.g. त) क् stays क्."),
             ("ग् is a case ending here", "तिर्यगूर्ध्वम् is an indeclinable (gram: ind.); ग् comes from sandhi."),
             ("ऊ is a voiceless sound", "Every vowel is voiced; that is why क् becomes ग्.")],
            "तिर्यक् + ऊर्ध्वम् → तिर्यगूर्ध्वम्: क् before a vowel → ग्.",
            "A final क् before a vowel → ग्."),
        mcq("transfer", 5, "By the rule of तिर्यगूर्ध्वम्, how is वाक् + ईशः (lord of speech) joined in a new example?",
            ("वागीशः", "क् before a vowel becomes ग्, as तिर्यक् + ऊर्ध्वम् → तिर्यगूर्ध्वम्."),
            [("वाकीशः", "क् stays क् only before a voiceless consonant, not before a vowel."),
             ("वाङीशः", "ङ् comes before a nasal (e.g. म), not before a vowel."),
             ("वागिशः", "The ई of ईशः stays long: -गी-.")],
            "वाक् + ईशः = वागीशः, like तिर्यक् + ऊर्ध्वम् = तिर्यगूर्ध्वम्.",
            "क् + vowel → ग्.",
            teaches="A final क् becomes ग् before a vowel: तिर्यक् + ऊर्ध्वम् → तिर्यगूर्ध्वम्."),
    ],
}

# ---------------------------------------------------------------- unit 31
AUTHORED["31"] = {
    "title": "पृष्ठवंशं बृहत्यौ",
    "question": "By unit 31, where are the two bṛhatī marmas, and through what does injury to them kill?",
    "rule": ("In a straight line with the two stanamūlas (breast-roots), on both sides of the spine: the two bṛhatīs. In those "
             "two: death through complications (उपद्रव) caused by an excessive flow of blood (शोणितातिप्रवृत्ति)."),
    "limits": ("Prose; injury understood. Bṛhatī here is a marma name, not the plant. Literally 'by straightness' (आर्जवेन) from "
               "the stanamūlas; 'in a straight line with' is the plain sense. The complications are not named."),
    "explain_hi": ("यह गद्य-पंक्ति दो बृहती मर्मों का स्थान और फल बताती है; यहाँ बृहती मर्म का नाम है, पौधा नहीं। "
                   "स्थान: दोनों स्तनमूलों से सीधी रेखा में, रीढ़ के दोनों ओर। "
                   "फल: रक्त के अतिप्रवाह से उत्पन्न उपद्रवों यानी जटिलताओं से मृत्यु; उपद्रव कौन-से हैं, यह नहीं बताया गया। "
                   "छपा ‘आर्ज्जव’ (दोहरा ज्ज) छपाई की आदत है, शब्द आर्जव है। "
                   "‘आर्जवेनोभयतः’ में अ + उ → ओ हुआ है।"),
    "hook": "स्तनमूल की सीध में, पीठ पर बृहती: रक्त बहे, उपद्रव, मृत्यु।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 31, what causes the complications through which injury to the bṛhatīs kills?",
            ("Excessive flow of blood", "शोणितातिप्रवृत्तिनिमित्तैः: caused by excessive flow of blood."),
            [("Kapha filling the koṣṭha", "Kapha filling the koṣṭha is said of the stanamūlas (card 23)."),
             ("Blood turning into pus", "Blood turned to pus is said of the apālāpas (card 26)."),
             ("Wind blocked at the dart", "Vāyu blocked at the dart is said of the utkṣepas (cards 62-63).")],
            "The complications are caused by an excessive flow of blood.",
            "शोणितातिप्रवृत्तिनिमित्तैरुपद्रवैर्मरणं."),
        order(1, "Put these printed parts of unit 31 in the line's order.",
              ["स्तनमूलयोरार्ज्जवेनोभयतः", "पृष्ठवंशं", "बृहत्यौ", "तयोः", "शोणितातिप्रवृत्तिनिमित्तैरुपद्रवैर्मरणं"],
              "In line with the breast-roots on both sides, of the spine, the bṛhatīs; in those two, death by complications.",
              "स्तनमूलयोरार्ज्जवेनोभयतः → पृष्ठवंशं → बृहत्यौ → तयोः → शोणितातिप्रवृत्तिनिमित्तैरुपद्रवैर्मरणं."),
        match(2, "Match each word of unit 31 to its meaning.",
              [["स्तनमूल", "breast-root"], ["आर्जव", "straightness"], ["अतिप्रवृत्ति", "excessive flow"],
               ["निमित्त", "cause"], ["उपद्रव", "complication"]],
              "आर्जवेन = in a straight line; शोणितातिप्रवृत्तिनिमित्त = caused by excessive flow of blood; उपद्रव = complication.",
              "स्तनमूल, आर्जव, अतिप्रवृत्ति, निमित्त, उपद्रव.", role="extend",
              teaches="आर्जव is the abstract noun of ऋजु (straight), made with vṛddhi (ऋ → आर्): 'straightness'."),
        mcq("discriminate", 3, "Which split of आर्ज्जवेनोभयतः in unit 31 is right?",
            ("आर्जवेन + उभयतः", "अ + उ → ओ: आर्जवेन + उभयतः → आर्जवेनोभयतः."),
            [("आर्जवे + नोभयतः", "नोभयतः is not a word; the न belongs to आर्जवेन."),
             ("आर्जवेनः + उभयतः", "आर्जवेनः is no form; and अः before उ would give अ, not ओ."),
             ("आर्जवेनो + भयतः", "आर्जवेनो is no form; the word is उभयतः, on both sides.")],
            "आर्जवेन (in a straight line) + उभयतः (on both sides).",
            "अ + उ → ओ."),
        multi("apply", 4, "Which statements fit unit 31?",
              [("Injury brings numbness of the arm", "Numbness of the arm is said of the aṃsaphalakas (card 32)."),
               ("Bṛhatī here names a marma, not the plant", "Right: the data reads बृहत्यौ as the marma name."),
               ("The two bṛhatīs lie on both sides of the spine", "Right: उभयतः पृष्ठवंशं बृहत्यौ."),
               ("Death comes through complications (upadrava)", "Right: उपद्रवैर्मरणं.")],
              [1, 2, 3],
              "Two marmas beside the spine, in line with the breast-roots; death by complications of excess bleeding.",
              "उभयतः पृष्ठवंशं बृहत्यौ ... उपद्रवैर्मरणं."),
        mcq("transfer", 5, "By the rule of आर्जवेनोभयतः, how is सूर्य + उदयः (sunrise) joined in a new example?",
            ("सूर्योदयः", "अ + उ → ओ, as आर्जवेन + उभयतः → आर्जवेनोभयतः."),
            [("सूर्यौदयः", "औ comes from अ + ओ or औ, not from अ + उ."),
             ("सूर्युदयः", "The अ does not drop before उ; the two merge into ओ."),
             ("सूर्यादयः", "आ comes from अ + अ, not from अ + उ.")],
            "सूर्य + उदयः = सूर्योदयः, like आर्जवेन + उभयतः.",
            "अ + उ → ओ.",
            teaches="अ followed by उ merges into ओ: आर्जवेन + उभयतः → आर्जवेनोभयतः."),
    ],
}

# ---------------------------------------------------------------- unit 32
AUTHORED["32"] = {
    "title": "बाहुमूलसंबद्धे अंसफलके",
    "question": "By unit 32, where are the two aṃsaphalakas, and what follows injury to them?",
    "rule": ("On both sides of the spine, joined to the roots of the arms (बाहुमूलसंबद्धे): the two aṃsaphalakas "
             "(shoulder-plates, probably the shoulder-blades). In those two: numbness (स्वाप) and wasting (शोष) of the arm."),
    "limits": ("Prose with no verb; injury understood. Aṃsaphalaka = shoulder-blade is probable only. स्वाप here is numbness "
               "(the word can also mean sleep). बाहु stands once in the last compound and is read with both numbness and "
               "wasting."),
    "explain_hi": ("यह गद्य-पंक्ति दो अंसफलक मर्मों का स्थान और फल बताती है। "
                   "स्थान: रीढ़ के दोनों ओर, बाहु के मूल से जुड़े; अंसफलक यानी कन्धे की फलकें, सम्भवतः स्कन्धास्थियाँ। "
                   "फल: भुजा का स्वाप (सुन्न होना) और शोष (सूखकर क्षीण होना)। "
                   "‘संबद्धे अंसफलके’ में सन्धि नहीं हुई, क्योंकि संबद्धे द्विवचन है और ए पर समाप्त द्विवचन के बाद स्वर-सन्धि नहीं होती। "
                   "‘उभयतो बाहु’ में अः घोष व्यंजन ब से पहले ओ बना है।"),
    "hook": "कन्धे की फलकों पर चोट: भुजा सुन्न और सूखी।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 32, what follows injury (understood) to the two aṃsaphalakas?",
            ("Numbness, wasting of the arm", "बाहुस्वापशोषौ: numbness (स्वाप) and wasting (शोष) of the arm."),
            [("Stiffness of both the arms", "Stiff arms are said of the aṃsas (card 33), not the aṃsaphalakas."),
             ("Bentness of the arm (kuṇita)", "Kuṇita is said of wrist and elbow (card 16)."),
             ("Lameness of the leg", "Lameness (khañjatā) is said of the knee (card 10).")],
            "Two results: numbness and wasting of the arm.",
            "तयोर्बाहुस्वापशोषौ."),
        order(1, "Put the printed words of unit 32 in the line's order.",
              ["पृष्ठवंशमुभयतो", "बाहुमूलसंबद्धे", "अंसफलके", "तयोर्बाहुस्वापशोषौ"],
              "On both sides of the spine, joined to the arm-roots, the aṃsaphalakas; in those two, numbness and wasting of the arm.",
              "पृष्ठवंशमुभयतो → बाहुमूलसंबद्धे → अंसफलके → तयोर्बाहुस्वापशोषौ."),
        match(2, "Match each word of unit 32 to its meaning.",
              [["पृष्ठवंश", "spine"], ["बाहु", "arm"], ["मूल", "root"], ["संबद्ध", "joined"], ["शोष", "wasting"]],
              "बाहुमूलसंबद्धे = joined to the arm-roots; शोष = wasting.",
              "पृष्ठवंश, बाहु, मूल, संबद्ध, शोष.", role="extend",
              teaches="बाहुस्वापशोषौ is a dvandva in the dual: two results, numbness and wasting, both of the arm."),
        mcq("discriminate", 3, "Why is संबद्धे not joined with अंसफलके in unit 32?",
            ("Dual -ए stays apart before a vowel", "संबद्धे is n. nom. du.; a dual in -ए stays as it is before a vowel."),
            [("ए never joins with a following अ", "It does elsewhere: ते + अपि → तेऽपि; only the dual -ए is exempt."),
             ("अंसफलके begins with a consonant", "अंसफलके begins with the vowel अ."),
             ("संबद्धे is a locative singular form", "The data reads संबद्धे as n. nom. du., agreeing with अंसफलके.")],
            "Dual endings in ई, ऊ, ए are left unjoined before a vowel: संबद्धे अंसफलके.",
            "Dual -ई/-ऊ/-ए: no sandhi before a vowel."),
        mcq("apply", 4, "By unit 32, what are the two aṃsaphalakas joined to?",
            ("The roots of the two arms", "बाहुमूलसंबद्धे: joined to the arm-roots."),
            [("The roots of the breasts", "The breast-roots are named in unit 31 for the bṛhatīs, not here."),
             ("The hip 'ears' (śroṇīkarṇa)", "The śroṇīkarṇas belong to unit 29, the nitambas."),
             ("The junction of head and neck", "That junction is the place of the kṛkāṭikās (card 36).")],
            "They lie on both sides of the spine, joined to the roots of the arms.",
            "पृष्ठवंशमुभयतो बाहुमूलसंबद्धे अंसफलके."),
        mcq("transfer", 5, "By the rule of संबद्धे अंसफलके, how is द्वे + अत्र (two here) written in a new example?",
            ("द्वे अत्र", "द्वे is a dual in -ए, so it stays unjoined before a vowel."),
            [("द्वेऽत्र", "ए + अ → एऽ holds for other -ए words, not for a dual."),
             ("द्वयत्र", "ए → अय् before a vowel does not apply to a dual."),
             ("द्वात्र", "No rule turns ए + अ into आ.")],
            "द्वे अत्र stays apart, like संबद्धे अंसफलके.",
            "Dual -ए + vowel: no sandhi.",
            teaches="A dual ending in ई, ऊ or ए is not joined with a following vowel: संबद्धे अंसफलके."),
    ],
}

# ---------------------------------------------------------------- unit 33
AUTHORED["33"] = {
    "title": "तयोः स्तब्धबाहुता",
    "question": "By unit 33, where are the two aṃsa marmas, and what follows injury to them?",
    "rule": ("In the middle of neck, arm and head (ग्रीवाबाहुशिरोमध्ये), binding the aṃsapīṭha (printed असपीठ; reading possible) and the skandha: the two aṃsas "
             "(shoulders). In those two: stiffness of the arms (स्तब्धबाहुता)."),
    "limits": ("Prose; injury understood. The printed असपीठ is not a word; aṃsapīṭha (anusvara dropped) is a possible reading, "
               "and the sense of the pair aṃsapīṭha / skandha is not firm, so no question rests on असपीठ or on that pair; only the "
               "sure join बन्धनौ + अंसौ is asked."),
    "explain_hi": ("यह गद्य-पंक्ति दो अंस यानी कन्धे के मर्मों का स्थान और फल बताती है। "
                   "स्थान: ग्रीवा, बाहु और शिर के बीच; ये अंसपीठ और स्कन्ध को बाँधते हैं। "
                   "छपा ‘असपीठ’ कोई शब्द नहीं; ‘अंसपीठ’ (अनुस्वार छूटा) सम्भावित पाठ है, और अंसपीठ/स्कन्ध का अर्थ-भेद पक्का नहीं; इस पर कोई प्रश्न नहीं। "
                   "फल: भुजाओं की अकड़न (स्तब्धबाहुता)। "
                   "‘बंधनावंसौ’ में औ स्वर से पहले आव् बना है।"),
    "hook": "गर्दन, बाँह, सिर के बीच अंस: चोट लगे तो बाँह अकड़े।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 33, what follows injury (understood) to the two aṃsas?",
            ("Stiffness of the arms", "स्तब्धबाहुता: the state of having stiff arms."),
            [("Numbness of the whole arm", "Numbness of the arm is said of the aṃsaphalakas (card 32)."),
             ("An unsteady head", "An unsteady head is said of the kṛkāṭikās (card 36)."),
             ("Loss of speech", "Dumbness is said of the four dhamanīs of the throat (card 34).")],
            "In those two: stiffness of the arms.",
            "तयोः स्तब्धबाहुता."),
        order(1, "Put the parts named in ग्रीवाबाहुशिरोमध्ये (unit 33) in the printed order.",
              ["ग्रीवा", "बाहु", "शिरः", "मध्ये"],
              "Neck, arm, head, then 'in the middle': ग्रीवाबाहुशिरोमध्ये.",
              "ग्रीवा → बाहु → शिरः → मध्ये."),
        match(2, "Match each word of unit 33 to its meaning.",
              [["ग्रीवा", "neck"], ["बाहु", "arm"], ["शिरः", "head"], ["स्तब्ध", "stiff"], ["मध्ये", "in the middle"]],
              "ग्रीवाबाहुशिरोमध्ये = in the middle of neck, arm and head; स्तब्धबाहुता = stiff-armedness.",
              "ग्रीवा, बाहु, शिरः, स्तब्ध, मध्ये.", role="extend",
              teaches="स्तब्धबाहुता = स्तब्ध (stiff) + बाहु (arm) + -ता (-ness): the state of having stiff arms."),
        mcq("discriminate", 3, "Which split of बंधनावंसौ in unit 33 is right?",
            ("बन्धनौ + अंसौ", "औ before a vowel → आव्: बन्धनौ + अंसौ → बन्धनावंसौ."),
            [("बन्धने + अंसौ", "ए before अ gives -नेऽंसौ (or, for a dual -ए, stays apart); never -नावंसौ."),
             ("बन्धनाः + अंसौ", "आः before a vowel drops the visarga: बन्धना अंसौ."),
             ("बन्धना + वंसौ", "वंसौ is not a word; the व् comes from the औ of बन्धनौ.")],
            "बन्धनौ (the two binding) + अंसौ (the two aṃsas).",
            "औ + vowel → आव् + vowel."),
        multi("apply", 4, "Which statements fit unit 33?",
              [("Injury (understood) brings deafness", "Deafness is said of the vidhuras (card 36)."),
               ("The line says injury kills at once", "No death is printed for the aṃsas in unit 33."),
               ("The aṃsas lie amid neck, arm and head", "Right: ग्रीवाबाहुशिरोमध्ये ... अंसौ."),
               ("Injury (understood) brings stiff arms", "Right: तयोः स्तब्धबाहुता.")],
              [2, 3],
              "Place: amid neck, arm and head; result: stiffness of the arms.",
              "ग्रीवाबाहुशिरोमध्ये ... अंसौ तयोः स्तब्धबाहुता."),
        mcq("transfer", 5, "By the rule of बंधनावंसौ, how is बालौ + अत्र (the two boys, here) joined in a new example?",
            ("बालावत्र", "औ before a vowel becomes आव्, as बन्धनौ + अंसौ → बन्धनावंसौ."),
            [("बालवत्र", "आव् keeps the long आ: -ला-."),
             ("बालायत्र", "आय् comes from ऐ, not from औ."),
             ("बालोऽत्र", "ओऽ comes from अः + अ, not from औ + अ.")],
            "बालौ + अत्र = बालावत्र, like बन्धनौ + अंसौ = बन्धनावंसौ.",
            "औ + vowel → आव्.",
            teaches="A final औ becomes आव् before a vowel: बन्धनौ + अंसौ → बन्धनावंसौ."),
    ],
}

# ---------------------------------------------------------------- unit 34
AUTHORED["34"] = {
    "title": "कंठनाडीमुभयतश्चतस्त्रो धमन्यः",
    "question": "By unit 34, which four vessels lie beside the throat-tube, and what may injury to them cause?",
    "rule": ("On both sides of the kaṇṭha-nāḍī (probably the windpipe): four dhamanīs (vessels); of these two nīlā, two manyā (taken as names; not firm). "
             "In those: dumbness, alteration of voice, or not perceiving taste (वा: alternatives) occurs."),
    "limits": ("Prose; injury understood. Dhamanī is kept as 'vessel', not 'artery'. That nīlā and manyā are names is not firm "
               "(नीले could be 'blue'), so no question asks about them. The three results are alternatives, not all at once."),
    "explain_hi": ("यह गद्य-पंक्ति गर्दन और सिर के मर्मों का भाग आरम्भ करती है। "
                   "कण्ठनाड़ी (सम्भवतः श्वासनली) के दोनों ओर चार धमनियाँ यानी वाहिकाएँ हैं; उनमें दो नीला और दो मन्या कहलाती हैं; ये नाम पक्के नहीं, ‘नीले’ का अर्थ ‘नीली’ भी हो सकता है। "
                   "फल: मूकता (गूँगापन), स्वर का विकार, या रस (स्वाद) का ग्रहण न होना; ‘वा’ और एकवचन ‘भवति’ से ये तीन विकल्प हैं। "
                   "‘उभयतश्च’ में विसर्ग च से पहले श् बना है।"),
    "hook": "गले की चार धमनियाँ: चोट से गूँगापन, स्वर-विकार या स्वाद-हानि।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 34, what may follow injury (understood) to the four vessels beside the throat-tube?",
            ("Dumbness, altered voice or no taste", "मूकता स्वरवैकृत्यं रसाग्राहिता वा: these three, as alternatives."),
            [("Deafness, blindness or loss of smell", "These are said of vidhura, apāṅga and phaṇa (cards 36-38)."),
             ("Swelling, weakness and death", "These are said of the nitambas (unit 29)."),
             ("Numb, wasted and stiff arms", "Arm results are said of the aṃsaphalakas and aṃsas (cards 32, 33).")],
            "Dumbness, alteration of the voice, or inability to perceive taste.",
            "तासु मूकता स्वरवैकृत्यं रसाग्राहिता वा भवति."),
        order(1, "Put these printed parts of unit 34 in the line's order.",
              ["कंठनाडीमुभयतश्चतस्त्रो धमन्यः", "तासां द्वे नीले द्वे मन्ये", "तासु मूकता", "स्वरवैकृत्यं",
               "रसाग्राहिता वा भवति"],
              "Four vessels beside the throat-tube; their names; then dumbness, altered voice, or no taste.",
              "कंठनाडीमुभयतश्चतस्त्रो धमन्यः → तासां द्वे नीले द्वे मन्ये → तासु मूकता → स्वरवैकृत्यं → रसाग्राहिता वा भवति."),
        match(2, "Match each word of unit 34 to its meaning.",
              [["मूकता", "dumbness"], ["स्वर", "voice"], ["वैकृत्य", "alteration"], ["अग्राहिता", "not grasping"],
               ["भवति", "occurs"]],
              "मूकता = dumbness; स्वरवैकृत्य = alteration of voice; रसाग्राहिता = not grasping taste; भवति = occurs.",
              "मूकता, स्वर, वैकृत्य, अग्राहिता, भवति.", role="extend",
              teaches="रसाग्राहिता = रस + अ-ग्राहिन् + -ता: the state of not grasping taste (अ + अ → आ in रसा-)."),
        mcq("discriminate", 3, "By unit 34, how do the three results stand to one another?",
            ("As alternatives: any one may occur", "वा (or) with the singular भवति: one or another occurs."),
            [("As three stages, one after another", "No sequence is printed; वा marks alternatives."),
             ("As three that must all occur together", "वा means 'or', not 'and'."),
             ("As results of the throat-tube itself", "तासु (in those) refers to the four vessels, not to the kaṇṭhanāḍī.")],
            "The three are alternatives: dumbness, or altered voice, or not perceiving taste.",
            "मूकता स्वरवैकृत्यं रसाग्राहिता वा भवति."),
        mcq("apply", 4, "In कंठनाडीमुभयतश्चतस्त्रो of unit 34, why does उभयतः show श्?",
            ("A visarga before च becomes श्", "उभयतः + चतस्रः: visarga before च → श्."),
            [("A visarga before any consonant → श्", "Not any: before त it becomes स् (मातृकास्तासु, card 35)."),
             ("उभयतश् is the word's own form", "The word is उभयतः (ind.); श् comes from sandhi."),
             ("Visarga before a voiced sound → श्", "च is not voiced; before a voiced consonant अः gives ओ.")],
            "उभयतः + चतस्रः → उभयतश्चतस्रः: visarga before च → श्.",
            "Visarga + च/छ → श्."),
        mcq("transfer", 5, "By the rule of उभयतश्च-, how is नराः + चरन्ति (men move) joined in a new example?",
            ("नराश्चरन्ति", "Visarga before च becomes श्, as उभयतः + चतस्रः → उभयतश्चतस्रः."),
            [("नरास्चरन्ति", "स् comes before त or थ, not before च."),
             ("नरा चरन्ति", "आः drops its visarga before a voiced sound; च is not voiced."),
             ("नरोश्चरन्ति", "ओ comes from अः before a voiced consonant; here it is आः.")],
            "नराः + चरन्ति = नराश्चरन्ति, like उभयतः + चतस्रः.",
            "Visarga + च → श्च.",
            teaches="A visarga before च becomes श्: उभयतः + चतस्रः → उभयतश्चतस्रः."),
    ],
}

# ---------------------------------------------------------------- unit 35
AUTHORED["35"] = {
    "title": "सिरा मातृकास्तासु सद्यो मरणं",
    "question": "By unit 35, what are the neck vessels printed 'on both sides, four' called, and what follows injury to them?",
    "rule": ("In the neck, on both sides, four (as printed; no total is given) sirās (vessels), the mātṛkās. In those: immediate death (सद्यो मरणम्)."),
    "limits": ("Prose, nominal sentence; injury understood. Sirā = 'vessel' (not forced to 'vein'). "
               "The line says 'on both sides, four'; four in all or four on each side is not said (the data's "
               "unit 59 count has eight), so the card gives no total."),
    "explain_hi": ("यह छोटी गद्य-पंक्ति कहती है: ग्रीवा में दोनों ओर चार सिराएँ हैं, जिनका नाम मातृका है; उनमें आघात से तुरन्त मृत्यु। "
                   "चार कुल हैं या हर ओर चार, पंक्ति नहीं कहती (डेटा की गिनती इकाई ५९ में आठ मातृकाएँ मानती है); इसलिए कुल संख्या नहीं दी गई। "
                   "सिरा को यहाँ ‘वाहिका’ ही कहा गया है, किसी आधुनिक नाम से नहीं जोड़ा गया। "
                   "‘सिरा मातृकाः’ में आ के बाद का विसर्ग घोष व्यंजन म से पहले लुप्त हुआ है। "
                   "‘मातृकास्तासु’ में विसर्ग त से पहले स् बना, और ‘सद्यो मरणं’ में अः घोष व्यंजन म से पहले ओ बना। "
                   "एक ही पंक्ति में विसर्ग के तीन रूप दिखते हैं।"),
    "hook": "गर्दन के दोनों ओर मातृका सिराएँ: चोट लगे तो तुरन्त मृत्यु।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 35, what follows injury (understood) to the mātṛkā vessels of the neck?",
            ("Immediate death", "तासु सद्यो मरणं: in those, immediate death."),
            [("Loss of smell", "Loss of smell is said of the phaṇas (card 37)."),
             ("Dumbness or a changed voice", "These are said of the four dhamanīs (card 34)."),
             ("Deafness in both ears", "Deafness is said of the vidhuras (card 36).")],
            "In those: immediate death.",
            "तासु सद्यो मरणं."),
        match(1, "Match each word of unit 35 to its meaning.",
              [["ग्रीवा", "neck"], ["उभयतः", "on both sides"], ["सिरा", "vessel"], ["सद्यः", "immediately"],
               ["मरण", "death"]],
              "ग्रीवायाम् उभयतः = in the neck on both sides; सिराः = vessels; सद्यो मरणम् = immediate death.",
              "ग्रीवा, उभयतः, सिरा, सद्यः, मरण."),
        fill(2, "Unit 35: ग्रीवायामुभयतश्चतस्त्रः सिरा ____ (their name). Type it in Devanagari or in English letters (e.g. dharma).",
             accepts("मातृकाः", None, "matrika", "matrikah", "maatrikaa"),
             "मातृकाः, the name of these neck sirās: सिरा मातृकास्तासु.",
             "मातृका (f., plural here) is the name of these neck vessels; the word literally means 'mothers'.",
             "सिराः मातृकाः."),
        mcq("discriminate", 3, "Why is सिराः printed सिरा before मातृकाः in unit 35?",
            ("After आ, visarga drops before a voiced sound", "म is voiced: सिराः + मातृकाः → सिरा मातृकाः."),
            [("After आ, visarga drops before any sound at all", "Not before त: मातृकाः + तासु → मातृकास्तासु in the same line."),
             ("The print lost the visarga by mistake", "The data calls it the regular loss before a voiced consonant."),
             ("सिरा is a singular form in this line", "The data reads सिराः, f. nom. pl., agreeing with चतस्रः.")],
            "आः + voiced consonant: the visarga drops (सिरा मातृकाः).",
            "आः + voiced sound → आ."),
        mcq("apply", 4, "In मातृकास्तासु of unit 35, what does the visarga of मातृकाः become before त?",
            ("स्", "Visarga before त → स्: मातृकाः + तासु → मातृकास्तासु."),
            [("श्", "श् comes before च or छ, not before त."),
             ("र्", "र् comes after vowels other than अ/आ before a voiced sound."),
             ("ओ", "ओ comes from अः before a voiced consonant; here आः stands before त.")],
            "मातृकाः + तासु → मातृकास्तासु: visarga before त → स्.",
            "Visarga + त/थ → स्."),
        mcq("transfer", 5, "By the rule of सिरा मातृकाः, how is देवाः + गच्छन्ति (the gods go) joined in a new example?",
            ("देवा गच्छन्ति", "After आ the visarga drops before a voiced sound, as सिराः + मातृकाः → सिरा मातृकाः."),
            [("देवो गच्छन्ति", "ओ comes from अः, not from आः."),
             ("देवार्गच्छन्ति", "र् comes after vowels other than अ/आ."),
             ("देवास्गच्छन्ति", "स् comes before त or थ, not before ग.")],
            "देवाः + गच्छन्ति = देवा गच्छन्ति, like सिराः + मातृकाः.",
            "आः + voiced sound → आ.",
            teaches="After आ a visarga drops before a voiced sound: सिराः + मातृकाः → सिरा मातृकाः."),
    ],
}

# ---------------------------------------------------------------- unit 36
AUTHORED["36"] = {
    "title": "शिरोग्रीवयोः संधाने कृकाटिके",
    "question": "By card 36, which two pairs of marmas are placed, and what follows injury to each?",
    "rule": ("Two printed lines. At the junction of head and neck: the two kṛkāṭikās; in those, an unsteady head "
             "(चलमूर्धता). Below the backs of the two ears: the two vidhuras; of those, deafness (बाधिर्य)."),
    "limits": ("Prose, two printed lines joined in one card; no verb, injury understood. Kṛkāṭikā = the nape joints is "
               "probable only. The print joins संश्रिते and विधुरे without a space."),
    "explain_hi": ("यह कार्ड दो छपी पंक्तियाँ जोड़ता है, और दो मर्म-युग्म बताता है। "
                   "पहली: शिर और ग्रीवा के जोड़ पर दो कृकाटिका (सम्भवतः गर्दन के पीछे के जोड़); उनमें आघात से शिर का डगमगाना (चलमूर्धता)। "
                   "दूसरी: कानों के पीछे के भाग के नीचे स्थित दो विधुर; उनमें आघात से बहरापन। "
                   "दोनों में क्रिया छपी नहीं, आघात समझा जाता है। "
                   "‘तयोश्चल’ में विसर्ग च से पहले श्, और ‘तयोर्बाधिर्यं’ में घोष ब से पहले र् बना है।"),
    "hook": "गर्दन-सिर के जोड़ पर कृकाटिका: सिर डगमगाए; कान के पीछे विधुर: बहरापन।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By card 36, what follows injury (understood) to the two vidhuras below the backs of the ears?",
            ("Deafness", "तयोर्बाधिर्यं: of those two, deafness."),
            [("Blindness", "Blindness is said of the apāṅgas (card 38) and āvartas (card 39)."),
             ("Loss of smell", "Loss of smell is said of the phaṇas (card 37)."),
             ("Unsteady head", "An unsteady head goes with the kṛkāṭikās, the first pair of card 36.")],
            "The vidhuras: deafness (बाधिर्य).",
            "कर्णपृष्ठयोरधःसंश्रितेविधुरे तयोर्बाधिर्यं."),
        order(1, "Put these printed parts of card 36 in the order of its two lines.",
              ["शिरोग्रीवयोः संधाने", "कृकाटिके", "तयोश्चलमूर्द्धता", "कर्णपृष्ठयोरधःसंश्रितेविधुरे", "तयोर्बाधिर्यं"],
              "Line 1: place, kṛkāṭikā, unsteady head; line 2: place and vidhura, deafness.",
              "शिरोग्रीवयोः संधाने → कृकाटिके → तयोश्चलमूर्द्धता → कर्णपृष्ठयोरधःसंश्रितेविधुरे → तयोर्बाधिर्यं."),
        match(2, "Match each word of card 36 to its meaning.",
              [["सन्धान", "junction"], ["चल", "unsteady"], ["मूर्धन्", "head"], ["अधः", "below"],
               ["बाधिर्य", "deafness"]],
              "शिरोग्रीवयोः सन्धाने = at the junction of head and neck; चलमूर्धता = an unsteady head; बाधिर्य = deafness.",
              "सन्धान, चल, मूर्धन्, अधः, बाधिर्य.", role="extend",
              teaches="चलमूर्धता is a bahuvrīhi (चल + मूर्धन्: 'having an unsteady head') made abstract with -ता."),
        mcq("discriminate", 3, "By card 36, which result goes with which marma?",
            ("Kṛkāṭikā: unsteady head; vidhura: deafness", "तयोश्चलमूर्द्धता for the kṛkāṭikās; तयोर्बाधिर्यं for the vidhuras."),
            [("Kṛkāṭikā: deafness; vidhura: unsteady head", "This swaps the two results of the card."),
             ("Kṛkāṭikā: stiff arms; vidhura: deafness", "Stiff arms are said of the aṃsas (card 33)."),
             ("Kṛkāṭikā: unsteady head; vidhura: blindness", "Blindness is not said of the vidhuras.")],
            "Each pair has its own result: unsteady head, then deafness.",
            "कृकाटिके तयोश्चलमूर्द्धता; विधुरे तयोर्बाधिर्यं."),
        mcq("apply", 4, "Why is तयोः printed तयोश्- and तयोर्- in the two lines of card 36?",
            ("श् before च; र् before the voiced ब", "Visarga + च → श्; after ओ, visarga + voiced sound → र्."),
            [("श् before ब; र् before च", "This reverses the rules: च takes श्, the voiced ब takes र्."),
             ("Both are slips of the 1888 print", "Both are regular sandhi; the data flags neither."),
             ("They are two different case endings", "Both are तयोः (gen. du.); only sandhi differs.")],
            "तयोः + चल → तयोश्चल; तयोः + बाधिर्यम् → तयोर्बाधिर्यम्.",
            "Visarga + च → श्; ओः + voiced sound → ओर्."),
        mcq("transfer", 5, "By the rule of तयोर्बाधिर्यं, how is साधोः + भवनम् (the saint's house) joined in a new example?",
            ("साधोर्भवनम्", "After ओ, a visarga before the voiced भ → र्, as तयोः + बाधिर्यम्."),
            [("साधोश्भवनम्", "श् comes before च or छ, not before भ."),
             ("साधो भवनम्", "After ओ the visarga does not drop before a voiced sound; it becomes र्."),
             ("साधोस्भवनम्", "स् comes before त or थ, not before भ.")],
            "साधोः + भवनम् = साधोर्भवनम्, like तयोः + बाधिर्यम्.",
            "ओः + voiced sound → ओर्.",
            teaches="After ओ a visarga becomes र् before a voiced sound: तयोः + बाधिर्यम् → तयोर्बाधिर्यम्."),
    ],
}

# ---------------------------------------------------------------- unit 37
AUTHORED["37"] = {
    "title": "तयोर्गंधाज्ञानं",
    "question": "By card 37, which marmas lie beside the nose-passage, and what follows injury to them?",
    "rule": ("On both sides of the nose-passage (घ्राणमार्गम् उभयतः), on the inside: the two phaṇas; 'bound to the ear-passage' (श्रोत्रमार्गप्रतिबद्धम्) "
             "stands between, and what it describes is not settled. Of those two: non-perception of smell (गन्धाज्ञानम्)."),
    "limits": ("Prose, elliptical; no verb, injury understood. Printed singular प्रतिबद्धम् does not agree with dual फणौ; what is "
               "joined to the ear-passage is not settled, and whether उभयतः goes with the passage or the phaṇas is open. No "
               "question rests on these points."),
    "explain_hi": ("यह गद्य-पंक्ति (छपी पंक्ति ३८) दो फण मर्मों का फल बताती है। "
                   "स्थान: नाक के मार्ग के दोनों ओर, भीतर की ओर, कान के मार्ग से जुड़े। "
                   "छपा एकवचन ‘प्रतिबद्धम्’ द्विवचन ‘फणौ’ से मेल नहीं खाता; कान के मार्ग से कौन जुड़ा है, यह तय नहीं; इस पर कोई प्रश्न नहीं। "
                   "फल: गन्ध का ज्ञान न होना। "
                   "‘गंधाज्ञानं’ में गन्ध + अज्ञानम् में अ + अ → आ हुआ है।"),
    "hook": "नाक के दोनों ओर फण: चोट से गन्ध न आए।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By card 37, what follows injury (understood) to the two phaṇas?",
            ("No perception of smell", "तयोर्गंधाज्ञानं: of those two, non-perception of smell."),
            [("No perception of taste", "Not grasping taste is said of the throat's four dhamanīs (card 34)."),
             ("No perception of sound", "Deafness is said of the vidhuras (card 36)."),
             ("No sight in the eyes", "Blindness is said of the apāṅgas (card 38).")],
            "Of those two: non-perception of smell.",
            "तयोर्गंधाज्ञानं."),
        order(1, "Put the words of card 37 (split from the print) in the line's order.",
              ["घ्राणमार्गम्", "उभयतः", "श्रोत्रमार्गप्रतिबद्धम्", "अभ्यन्तरतः", "फणौ", "गन्धाज्ञानम्"],
              "Nose-passage, on both sides, joined to the ear-passage, inside, the phaṇas; (of those two) no smell.",
              "घ्राणमार्गम् → उभयतः → श्रोत्रमार्गप्रतिबद्धम् → अभ्यन्तरतः → फणौ → गन्धाज्ञानम्."),
        match(2, "Match each word of card 37 to its meaning.",
              [["घ्राण", "nose"], ["मार्ग", "passage"], ["श्रोत्र", "ear"], ["अभ्यन्तरतः", "on the inside"],
               ["गन्ध", "smell"]],
              "घ्राणमार्ग = nose-passage; श्रोत्रमार्ग = ear-passage; अभ्यन्तरतः = inside; गन्ध = smell.",
              "घ्राण, मार्ग, श्रोत्र, अभ्यन्तरतः, गन्ध.", role="extend",
              teaches="-तः makes adverbs of place: अभ्यन्तरतः = on the inside, उभयतः = on both sides."),
        mcq("discriminate", 3, "Which split of गंधाज्ञानं in card 37 is right?",
            ("गन्ध + अज्ञानम्", "अ + अ → आ: गन्धाज्ञानम्, non-perception of smell."),
            [("गन्ध + ज्ञानम्", "That would give गन्धज्ञानम् with a short -ध-; the print has -धा-."),
             ("गन्धः + अज्ञानम्", "अः + अ would give गन्धोऽज्ञानम्, with ओ and ऽ."),
             ("गन्धे + अज्ञानम्", "ए + अ would give गन्धेऽज्ञानम्, with ए and ऽ.")],
            "गन्ध (smell) + अज्ञानम् (non-perception).",
            "अ + अ → आ."),
        multi("apply", 4, "Which statements fit card 37?",
              [("Two phaṇa marmas are named", "Right: फणौ, dual."),
               ("Injury (understood) brings blindness", "Blindness is said of the apāṅgas (card 38)."),
               ("Injury (understood) brings loss of smell", "Right: गन्धाज्ञानम्."),
               ("A verb is printed in the line", "No verb is printed; the line is elliptical.")],
              [0, 2],
              "Two phaṇas; non-perception of smell; no verb printed.",
              "फणौ तयोर्गंधाज्ञानं."),
        mcq("transfer", 5, "By the rule of गन्धाज्ञानम् (अ + अ), how is हिम + अचलः (snow-mountain) joined in a new example?",
            ("हिमाचलः", "अ + अ → आ, as गन्ध + अज्ञानम् → गन्धाज्ञानम्."),
            [("हिमचलः", "The two अs merge into a long आ; neither simply drops."),
             ("हिमेचलः", "ए comes from अ + इ, not from अ + अ."),
             ("हिमोचलः", "ओ comes from अ + उ, not from अ + अ.")],
            "हिम + अचलः = हिमाचलः, like गन्ध + अज्ञानम् = गन्धाज्ञानम्.",
            "अ + अ → आ.",
            teaches="Two short अs merge into आ: गन्ध + अज्ञानम् → गन्धाज्ञानम्."),
    ],
}

# ---------------------------------------------------------------- unit 38
AUTHORED["38"] = {
    "title": "बाह्यतोऽपांगौ तयोरांध्यं",
    "question": "By card 38, where are the two apāṅgas, and what follows injury to them?",
    "rule": ("Below the tail-ends of the two brows (भ्रुवोः पुच्छान्तयोः अधः), on the outside of the two eyes: the two apāṅgas "
             "(probably the outer eye-corners). Of those two: blindness (आन्ध्य)."),
    "limits": ("Prose, elliptical; no verb, injury understood. Apāṅga = outer corner of the eye is probable (the ordinary sense "
               "of the word). The line names no other result."),
    "explain_hi": ("यह गद्य-पंक्ति (छपी पंक्ति ३९) दो अपाङ्ग मर्मों का स्थान और फल बताती है। "
                   "स्थान: दोनों भौंहों के पूँछ जैसे छोरों के नीचे, दोनों आँखों के बाहर की ओर; अपाङ्ग सम्भवतः आँख का बाहरी कोना। "
                   "फल: अन्धापन। "
                   "‘अधोऽक्ष्णोः’ और ‘बाह्यतोऽपांगौ’ में अः + अ → ओऽ हुआ है: अः ओ बनता है और अगला अ लुप्त होकर ऽ (अवग्रह) से दिखाया जाता है। "
                   "‘तयोरांध्यं’ में ओ के बाद का विसर्ग स्वर से पहले र् बना है।"),
    "hook": "भौंह के छोर के नीचे, आँख के बाहर अपाङ्ग: चोट से अन्धापन।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By card 38, what follows injury (understood) to the two apāṅgas?",
            ("Blindness", "तयोरांध्यं: of those two, blindness."),
            [("Deafness", "Deafness is said of the vidhuras (card 36)."),
             ("Loss of smell", "Loss of smell is said of the phaṇas (card 37)."),
             ("Death at once", "Death at once is said of the śaṅkhas (card 39).")],
            "Of those two: blindness (आन्ध्य).",
            "तयोरांध्यं."),
        order(1, "Put the words of card 38 (split from the print) in the line's order.",
              ["भ्रुवोः", "पुच्छान्तयोः", "अधः", "अक्ष्णोः", "बाह्यतः", "अपाङ्गौ"],
              "Of the brows, at the tail-ends, below; of the eyes, on the outside; the apāṅgas.",
              "भ्रुवोः → पुच्छान्तयोः → अधः → अक्ष्णोः → बाह्यतः → अपाङ्गौ."),
        match(2, "Match each word of card 38 to its meaning.",
              [["भ्रू", "brow"], ["पुच्छ", "tail"], ["अन्त", "end"], ["बाह्यतः", "on the outside"],
               ["आन्ध्य", "blindness"]],
              "भ्रुवोः पुच्छान्तयोः = at the tail-ends of the brows; बाह्यतः = outside; आन्ध्य = blindness.",
              "भ्रू, पुच्छ, अन्त, बाह्यतः, आन्ध्य.", role="extend",
              teaches="आन्ध्य is the abstract noun of अन्ध (blind), made with vṛddhi (अ → आ) and -य: 'blindness'."),
        mcq("discriminate", 3, "Which split of अधोऽक्ष्णोः in card 38 is right?",
            ("अधः + अक्ष्णोः", "अः + अ → ओऽ: the अ of अक्ष्णोः is dropped and shown by ऽ."),
            [("अधः + क्ष्णोः", "क्ष्णोः is not a word; ऽ marks the dropped अ of अक्ष्णोः."),
             ("अधे + अक्ष्णोः", "ए + अ would give अधेऽक्ष्णोः, with ए."),
             ("अधौ + अक्ष्णोः", "औ + अ would give अधावक्ष्णोः, with आव्.")],
            "अधः (below) + अक्ष्णोः (of the two eyes).",
            "अः + अ → ओऽ."),
        mcq("apply", 4, "In बाह्यतोऽपांगौ of card 38, what does the sign ऽ stand for?",
            ("The dropped अ of अपाङ्गौ", "बाह्यतः + अपाङ्गौ: अः + अ → ओऽ; ऽ marks the lost अ."),
            [("The dropped visarga of बाह्यतः", "The visarga is not dropped: अः has become ओ."),
             ("A pause between two phrases", "ऽ (avagraha) marks an elided अ, not a pause."),
             ("A lengthened vowel of बाह्यतः", "No vowel is lengthened; ऽ marks a dropped अ.")],
            "ऽ (avagraha) shows the अ of अपाङ्गौ dropped after ओ.",
            "अः + अ → ओऽ."),
        mcq("transfer", 5, "By the rule of बाह्यतोऽपांगौ, how is रामः + अपि (Rāma too) joined in a new example?",
            ("रामोऽपि", "अः + अ → ओऽ, as बाह्यतः + अपाङ्गौ → बाह्यतोऽपाङ्गौ."),
            [("रामापि", "आ would come from अ + अ with no visarga."),
             ("राम अपि", "अः gives अ before vowels other than अ; before अ it gives ओऽ."),
             ("रामरपि", "र् does not come from a visarga after अ.")],
            "रामः + अपि = रामोऽपि.",
            "अः + अ → ओऽ.",
            teaches="अः before अ becomes ओ and the अ drops (ऽ): बाह्यतः + अपाङ्गौ → बाह्यतोऽपाङ्गौ."),
    ],
}

# ---------------------------------------------------------------- unit 39
AUTHORED["39"] = {
    "title": "ललाटे शंखौ",
    "question": "By card 39, where are the śaṅkhas and the āvartas, and what follows injury to each pair?",
    "rule": ("Two printed lines. Above the tail-ends of the brows, toward the ear, on the forehead: the two śaṅkhas (probably the "
             "temples); of those, death at once. Above the brows, in the two hollows: the two āvartas; of those, blindness or "
             "damage to sight."),
    "limits": ("Prose, two printed lines joined in one card; no verb, injury understood. उत्कर्णम् = 'toward the ear' is probable, "
               "and śaṅkha = temple is probable; no question rests on either."),
    "explain_hi": ("यह कार्ड दो छपी पंक्तियाँ (४० और ४१) जोड़ता है। "
                   "पहली: भौंहों के पूँछ-छोरों के ऊपर, कान की ओर (सम्भावित अर्थ), माथे पर दो शङ्ख (सम्भवतः कनपटियाँ); उनमें आघात से तुरन्त मृत्यु। "
                   "दूसरी: भौंहों के ऊपर दो गड्ढों में दो आवर्त; उनमें आघात से अन्धापन या दृष्टि की हानि। "
                   "दोनों में क्रिया छपी नहीं। "
                   "‘उपर्युत्कर्णं’ और ‘दृष्ट्युपघातो’ दोनों में इ + उ → यु हुआ है।"),
    "hook": "माथे पर शङ्ख: तुरन्त मृत्यु; भौंह के ऊपर आवर्त: अन्धापन।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By card 39, what follows injury (understood) to the two śaṅkhas?",
            ("Death at once", "तयोः सद्यो मरणं: of those two, death at once."),
            [("Blindness or damaged sight", "That is the result of the āvartas, the second pair of card 39."),
             ("Deafness of both ears", "Deafness is said of the vidhuras (card 36)."),
             ("Stiffness of the arms", "Stiff arms are said of the aṃsas (card 33).")],
            "The śaṅkhas: death at once.",
            "ललाटे शंखौ तयोः सद्यो मरणं."),
        order(1, "Put these printed parts of card 39 in the order of its two lines.",
              ["भ्रुवोः पुच्छांतयोरुपर्युत्कर्णं", "ललाटे शंखौ", "तयोः सद्यो मरणं", "भ्रुवोरुपरि निम्नयोरावर्तौ",
               "तयोरांध्यं दृष्ट्युपघातो वा"],
              "Line 1: place, śaṅkhas, death at once; line 2: place and āvartas, blindness or damaged sight.",
              "भ्रुवोः पुच्छांतयोरुपर्युत्कर्णं → ललाटे शंखौ → तयोः सद्यो मरणं → भ्रुवोरुपरि निम्नयोरावर्तौ → तयोरांध्यं दृष्ट्युपघातो वा."),
        match(2, "Match each word of card 39 to its meaning.",
              [["ललाट", "forehead"], ["निम्न", "hollow"], ["सद्यः", "at once"], ["दृष्टि", "sight"],
               ["उपघात", "damage"]],
              "ललाटे = on the forehead; निम्नयोः = in the two hollows; सद्यः = at once; दृष्ट्युपघात = damage to sight.",
              "ललाट, निम्न, सद्यः, दृष्टि, उपघात.", role="extend",
              teaches="दृष्ट्युपघातः is a tat-puruṣa: दृष्टि (sight) + उपघात (damage) = damage to sight."),
        mcq("discriminate", 3, "By card 39, where are the two āvartas?",
            ("Above the brows, in two hollows", "भ्रुवोरुपरि निम्नयोरावर्तौ."),
            [("Below the brows, outside the eyes", "That is the place of the apāṅgas (card 38)."),
             ("Above the śaṅkhas, at hair-ends", "That is the place of the utkṣepas (card 40)."),
             ("Below the backs of the two ears", "That is the place of the vidhuras (card 36).")],
            "The āvartas lie above the brows, in the two hollows.",
            "भ्रुवोरुपरि निम्नयोरावर्तौ."),
        mcq("apply", 4, "Which split of दृष्ट्युपघातो in card 39 is right?",
            ("दृष्टि + उपघातः", "इ + उ → यु; अः before वा (voiced) → ओ."),
            [("दृष्टिः + उपघातः", "इः before a vowel would give दृष्टिरुपघातः, with र्."),
             ("दृष्टे + उपघातः", "ए before उ would give दृष्टयुपघातः or दृष्ट उपघातः, not -ष्ट्यु-."),
             ("दृष्ट + युपघातः", "युपघातः is not a word; the य् comes from the इ of दृष्टि.")],
            "दृष्टि (sight) + उपघातः (damage).",
            "इ + उ → यु."),
        mcq("transfer", 5, "By the rule of दृष्ट्युपघातः, how is प्रति + उत्तरम् (reply) joined in a new example?",
            ("प्रत्युत्तरम्", "इ before उ becomes य्, as दृष्टि + उपघातः → दृष्ट्युपघातः."),
            [("प्रत्यूत्तरम्", "The उ of उत्तरम् stays short: -त्यु-."),
             ("प्रत्योत्तरम्", "ओ comes from अ + उ, not from इ + उ."),
             ("प्रतुत्तरम्", "The इ does not simply drop; it becomes य्.")],
            "प्रति + उत्तरम् = प्रत्युत्तरम्.",
            "इ + उ → यु.",
            teaches="इ before a different vowel becomes य्: दृष्टि + उपघातः → दृष्ट्युपघातः, उपरि + उत्कर्णम् → उपर्युत्कर्णम्."),
    ],
}

# ---------------------------------------------------------------- unit 40
AUTHORED["40"] = {
    "title": "जीवेन्नोद्धृतशल्यः",
    "question": "By card 40, who may live after injury at the two utkṣepas, and who may not?",
    "rule": ("Above the two śaṅkhas, at the hair-ends: the two utkṣepas. Of those two: one with the dart (शल्य) still in, or "
             "one whose dart has fallen out through suppuration (पाक), may live (जीवेत्); not one whose dart was pulled out."),
    "limits": ("Prose; injury understood, and the subject 'one' is unstated. The printed join केशांतउत्क्षेपौ is irregular "
               "(the data reads केशान्तौ + उत्क्षेपौ); no question rests on its form. The line gives no reason here."),
    "explain_hi": ("यह गद्य-पंक्ति (छपी पंक्ति ४२) दो उत्क्षेप मर्मों के बारे में है: ये दोनों शङ्खों के ऊपर, केशों के छोर पर हैं। "
                   "उनमें शल्य (कोई भी चुभने वाली वस्तु) भीतर रहे, या पाक (पकने) से अपने-आप गिर जाए, तो व्यक्ति जी सकता है; जिसका शल्य निकाल दिया गया, वह नहीं (जी सकता)। "
                   "कारण यह पंक्ति नहीं बताती। "
                   "छपा ‘केशांतउत्क्षेपौ’ असामान्य जोड़ है (डेटा: केशान्तौ + उत्क्षेपौ), इस पर कोई प्रश्न नहीं। "
                   "‘जीवेन्नोद्धृत’ = जीवेत् + न + उद्धृत: छपाई में त् न से पहले न् बना (वैकल्पिक; द् भी सही), और अ + उ → ओ।"),
    "hook": "उत्क्षेप में शल्य: भीतर रहे या पाक से गिरे तो जी सकता है; निकाला गया तो नहीं।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By card 40, where are the two utkṣepas?",
            ("Above the śaṅkhas, at hair-ends", "शंखयोरुपरि केशान्तौ उत्क्षेपौ."),
            [("Above the brows, in two hollows", "That is the place of the āvartas (card 39)."),
             ("Below the backs of the two ears", "That is the place of the vidhuras (card 36)."),
             ("At the head and neck junction", "That is the place of the kṛkāṭikās (card 36).")],
            "The utkṣepas lie above the two śaṅkhas, at the hair-ends.",
            "शंखयोरुपरि केशांतउत्क्षेपौ."),
        order(1, "Put these printed parts of card 40 in the line's order.",
              ["शंखयोरुपरि", "केशांतउत्क्षेपौ", "तयोः", "सशल्यः", "पाकात्पतितशल्यो वा", "जीवेन्नोद्धृतशल्यः"],
              "Place, name, 'of those two', with dart in, or dart fallen by suppuration, may live; not with dart pulled out.",
              "शंखयोरुपरि → केशांतउत्क्षेपौ → तयोः → सशल्यः → पाकात्पतितशल्यो वा → जीवेन्नोद्धृतशल्यः."),
        match(2, "Match each word of card 40 to its meaning.",
              [["शल्य", "dart"], ["पाक", "suppuration"], ["पतित", "fallen"], ["उद्धृत", "pulled out"],
               ["जीवेत्", "may live"]],
              "सशल्यः = with the dart; पाकात् पतितशल्यः = dart fallen by suppuration; उद्धृतशल्यः = dart pulled out.",
              "शल्य, पाक, पतित, उद्धृत, जीवेत्.", role="extend",
              teaches="स-शल्य, पतित-शल्य, उद्धृत-शल्य are bahuvrīhis: 'one whose dart is (with him / fallen / pulled out)'."),
        mcq("discriminate", 3, "Which split of जीवेन्नोद्धृतशल्यः in card 40 is right?",
            ("जीवेत् + न + उद्धृतशल्यः", "The print writes त् as न् before न (optional; द् is also correct); अ + उ → ओ (नोद्धृत)."),
            [("जीवेत् + नः + उद्धृतशल्यः", "अः before उ would give न उद्धृत, with no ओ."),
             ("जीवेत् + ने + उद्धृतशल्यः", "ए before उ would not give नो-."),
             ("जीवे + नोद्धृतशल्यः", "नोद्धृतशल्यः is not a word; the न्न comes from जीवेत् + न.")],
            "जीवेत् (may live) + न (not) + उद्धृतशल्यः (one whose dart is pulled out).",
            "त् + न → न्न as printed (optional, द्न also correct); अ + उ → ओ."),
        multi("apply", 4, "By card 40, who may live after injury at the utkṣepas?",
              [("One whose dart has been pulled out", "Not he: न उद्धृतशल्यः."),
               ("One with the dart still in", "Right: सशल्यः ... जीवेत्."),
               ("One whose dart fell out through suppuration", "Right: पाकात्पतितशल्यो वा जीवेत्."),
               ("No one: all three die", "Two of the three may live (जीवेत्).")],
              [1, 2],
              "With the dart in, or with the dart fallen out by suppuration: may live; dart pulled out: not.",
              "सशल्यः पाकात्पतितशल्यो वा जीवेन्नोद्धृतशल्यः."),
        mcq("transfer", 5, "By the rule of पतितशल्यो वा, how is वृक्षः + वर्धते (the tree grows) joined in a new example?",
            ("वृक्षो वर्धते", "अः before the voiced व → ओ, as पतितशल्यः + वा → पतितशल्यो वा."),
            [("वृक्षा वर्धते", "The visarga drops this way only after आ, not after अ."),
             ("वृक्षर्वर्धते", "र् comes after vowels other than अ/आ."),
             ("वृक्षस्वर्धते", "स् comes before त or थ, not before व.")],
            "वृक्षः + वर्धते = वृक्षो वर्धते.",
            "अः + voiced consonant → ओ.",
            teaches="अः before a voiced consonant becomes ओ: पतितशल्यः + वा → पतितशल्यो वा."),
    ],
}


# ================================================================== NOTES_HI
NOTES_HI = {
    "28": ("गद्य; विश्वास मध्यम। पाठ-चिह्न (सम्भावित): छपा ‘स्पर्शज्ञानम्’ (स्पर्श का ज्ञान) हानियों की सूची में नहीं बैठता; अनुमानित पाठ "
           "‘स्पर्शाज्ञानम्’ (दीर्घ आ: स्पर्श का अज्ञान), या ‘ज्ञान’ के बाद ‘नाश’ जैसा शब्द छूटा; अर्थ वही; इस शब्द पर कोई प्रश्न नहीं। "
           "जघन = कूल्हे का क्षेत्र (सम्भावित)। छपा कुकुंदरौ = कुकुन्दरौ (ं = न्)। सन्धि जाँची: पार्श्वयोः + जघन → पार्श्वयोर्जघन; बहिः + "
           "भागे → बहिर्भागे (अ/आ से भिन्न स्वर के बाद विसर्ग + घोष → र्); पृष्ठवंशम् + उभयतः → पृष्ठवंशमुभयतः; चेष्टानाशः + च → "
           "चेष्टानाशश्च (च से पहले विसर्ग → श्)।"),
    "29": ("गद्य; विश्वास मध्यम। पाठ-चिह्न: (१) छपा ‘पार्श्वन्तर’; पार्श्व + अन्तर से ‘पार्श्वान्तर’ (दीर्घ आ) बनना चाहिए, दीर्घ-चिह्न छूटा "
           "लगता है (सम्भावित; इकाई ३० में भी); ‘अन्तर’ का अर्थ (भीतरी भाग) पक्का नहीं। (२) छपा ‘अध.’: बिन्दु विसर्ग के स्थान पर (लगभग "
           "निश्चित) = अधःकाये। इन पर कोई प्रश्न नहीं। आशय = कोई भीतरी स्थान, नाम नहीं दिया गया। सन्धि जाँची: श्रोणीकर्णयोः + उपरि → "
           "श्रोणीकर्णयोरुपरि (ओ के बाद विसर्ग + स्वर → र्); उपरि + आशय → उपर्याशय (इ + आ → या); आशय + आच्छादनौ → आशयाच्छादनौ "
           "(अ + आ → आ); शोफः + दौर्बल्यम् → शोफो दौर्बल्यम् (अः + घोष व्यंजन → ओ); छपा नितंबौ = नितम्बौ।"),
    "30": ("गद्य; विश्वास मध्यम। पाठ-चिह्न (सम्भावित): छपा ‘अधःपार्श्वन्तर’; दीर्घ आ छूटा लगता है (पार्श्वान्तर), जैसे इकाई २९ में; "
           "‘अन्तर’ का अर्थ पक्का नहीं; इस पर कोई प्रश्न नहीं। ‘तिर्यगूर्ध्वं च’ दिशा के रूप में पढ़ा गया, अलग मर्म नहीं (डेटा)। जघन = "
           "कूल्हे का क्षेत्र (सम्भावित)। पार्श्वसंधी = द्विवचन (ई पर समाप्त)। सन्धि जाँची: तिर्यक् + ऊर्ध्वम् → तिर्यगूर्ध्वम् (स्वर से पहले "
           "क् → ग्); छपा संधी = सन्धी।"),
    "31": ("गद्य; विश्वास मध्यम; कोई पाठ-चिह्न नहीं। छपा ‘आर्ज्जव’ (दोहरा ज्ज) छपाई की आदत, शब्द आर्जव। बृहती यहाँ मर्म-नाम है, पौधा "
           "नहीं। ‘आर्जवेन’ का शाब्दिक अर्थ ‘सीधेपन से’, सरल अर्थ ‘सीधी रेखा में’। सन्धि जाँची: स्तनमूलयोः + आर्जवेन → "
           "स्तनमूलयोरार्जवेन; आर्जवेन + उभयतः → आर्जवेनोभयतः (अ + उ → ओ); शोणित + अति → शोणिताति (अ + अ → आ); निमित्तैः + "
           "उपद्रवैः → निमित्तैरुपद्रवैः; उपद्रवैः + मरणम् → उपद्रवैर्मरणम् (ऐ के बाद विसर्ग + स्वर/घोष → र्)।"),
    "32": ("गद्य; विश्वास मध्यम; कोई पाठ-चिह्न नहीं; क्रिया नहीं। अंसफलक = स्कन्धास्थि (सम्भावित)। स्वाप = सुन्नपन (शब्द का दूसरा अर्थ "
           "नींद भी)। ‘बाहु’ अन्तिम समास में एक बार है और स्वाप तथा शोष दोनों से जुड़ता है। सन्धि जाँची: पृष्ठवंशम् + उभयतः → "
           "पृष्ठवंशमुभयतः; उभयतः + बाहु → उभयतो बाहु (अः + घोष व्यंजन → ओ); संबद्धे अंसफलके अलग (ए पर समाप्त द्विवचन के बाद "
           "स्वर-सन्धि नहीं); तयोः + बाहु → तयोर्बाहु।"),
    "33": ("गद्य; विश्वास मध्यम। पाठ-चिह्न (सम्भावित): छपा ‘असपीठ’ कोई शब्द नहीं; ‘अंसपीठ’ (अनुस्वार छूटा) सम्भावित पाठ; अंसपीठ और "
           "स्कन्ध के अर्थ का भेद पक्का नहीं; इस समास पर कोई प्रश्न नहीं। अवग्रह के बाद का समास ‘अंसपीठ और स्कन्ध को बाँधने वाले’ पढ़ा "
           "गया। सन्धि जाँची: शिरः + मध्ये → शिरोमध्ये (समास में शिरस् → शिरो); मध्ये + अ- → मध्येऽ- (ए + अ → एऽ); बन्धनौ + अंसौ → "
           "बन्धनावंसौ (औ + स्वर → आव्)।"),
    "34": ("गद्य; विश्वास मध्यम; कोई पाठ-चिह्न नहीं। धमनी = वाहिका (‘artery’ नहीं ठहराया गया)। नीला और मन्या नाम माने गए, पर यह पक्का "
           "नहीं: ‘नीले’ विशेषण ‘नीली’ भी हो सकता है; इन पर कोई प्रश्न नहीं। तीनों फल विकल्प हैं (वा, एकवचन भवति)। कण्ठनाड़ी = "
           "श्वासनली (सम्भावित)। छपा ‘चतस्त्रो’ (अतिरिक्त त्), शब्द-सूची में चतस्रः। ‘धमन्यः तासां’ में छपाई ने त से पहले विसर्ग को स् "
           "नहीं किया (विराम)। सन्धि जाँची: कण्ठनाडीम् + उभयतः → कण्ठनाडीमुभयतः; उभयतः + चतस्रः → उभयतश्चतस्रः (च से पहले "
           "विसर्ग → श्); चतस्रः + धमन्यः → चतस्रो धमन्यः (अः + घोष व्यंजन → ओ); रस + अग्राहिता → रसाग्राहिता।"),
    "35": ("गद्य; विश्वास उच्च; कोई पाठ-चिह्न नहीं; नामवाक्य। ‘दोनों ओर चार’: कुल चार या हर ओर चार, पंक्ति नहीं कहती; डेटा की गिनती (इकाई ५९ की टिप्पणी) आठ मातृकाएँ मानती है; कार्ड कुल संख्या नहीं देता। सिरा = वाहिका (प्रायः ‘शिरा/vein’, यहाँ ठहराया नहीं गया)। छपा ‘चतस्त्रः’ "
           "(अतिरिक्त त्), शब्द चतस्रः। सन्धि जाँची: ग्रीवायाम् + उभयतः → ग्रीवायामुभयतः; सिराः + मातृकाः → सिरा मातृकाः (आ के बाद "
           "विसर्ग घोष से पहले लुप्त, नियमित); मातृकाः + तासु → मातृकास्तासु (त से पहले विसर्ग → स्); सद्यः + मरणम् → सद्यो मरणम् "
           "(अः + घोष व्यंजन → ओ)।"),
    "36": ("गद्य; विश्वास उच्च; कोई पाठ-चिह्न नहीं। यह कार्ड दो छपी पंक्तियाँ (३६ और ३७) जोड़ता है। छपा ‘मूर्द्ध’ (दोहरा द्ध) = मूर्ध। "
           "कृकाटिका = गर्दन और खोपड़ी का जोड़ (सम्भावित)। दूसरी पंक्ति अधूरी: क्रिया नहीं, आघात समझा जाता है। छपाई ‘संश्रितेविधुरे’ में "
           "दो शब्द बिना अन्तर के जुड़े। सन्धि जाँची: तयोः + चल → तयोश्चल (च से पहले विसर्ग → श्); कर्णपृष्ठयोः + अधः → "
           "कर्णपृष्ठयोरधः; तयोः + बाधिर्यम् → तयोर्बाधिर्यम् (ओ के बाद विसर्ग + घोष → र्)।"),
    "37": ("गद्य; विश्वास मध्यम; कोई पाठ-चिह्न नहीं; छपी पंक्ति ३८। अधूरा वाक्य, क्रिया नहीं। छपाई ने अभ्यन्तरतः और फणौ बिना अन्तर के "
           "जोड़े। ‘उभयतः’ नासा-मार्ग से जुड़ता है या फणों से, तय नहीं। छपा एकवचन ‘प्रतिबद्धम्’ द्विवचन ‘फणौ’ से मेल नहीं खाता: यह "
           "घ्राणमार्ग से जुड़ सकता है, या द्विवचन की भूल हो सकती है; अनुवाद सरलतम अर्थ रखता है; इन पर कोई प्रश्न नहीं। सन्धि जाँची: "
           "घ्राणमार्गम् + उभयतः → घ्राणमार्गमुभयतः; प्रतिबद्धम् + अभ्यन्तरतः → प्रतिबद्धमभ्यन्तरतः; तयोः + गन्ध → तयोर्गन्ध; गन्ध + "
           "अज्ञानम् → गन्धाज्ञानम् (अ + अ → आ)।"),
    "38": ("गद्य; विश्वास उच्च; कोई पाठ-चिह्न नहीं; छपी पंक्ति ३९। अधूरा वाक्य, क्रिया नहीं। अपाङ्ग = आँख का बाहरी कोना (सम्भावित; "
           "शब्द का सामान्य अर्थ यही)। पुच्छान्त = भौंह का पतला छोर। सन्धि जाँची: पुच्छान्तयोः + अधः → पुच्छान्तयोरधः; अधः + अक्ष्णोः "
           "→ अधोऽक्ष्णोः (अः + अ → ओऽ); अक्ष्णोः + बाह्यतः → अक्ष्णोर्बाह्यतः; बाह्यतः + अपाङ्गौ → बाह्यतोऽपाङ्गौ (अः + अ → ओऽ); "
           "तयोः + आन्ध्यम् → तयोरान्ध्यम्।"),
    "39": ("गद्य; विश्वास मध्यम; कोई पाठ-चिह्न नहीं। यह कार्ड दो छपी पंक्तियाँ (४० और ४१) जोड़ता है; दोनों अधूरी, क्रिया नहीं। ‘उत्कर्णम्’ "
           "= कान की ओर (सम्भावित, निश्चित नहीं)। शङ्ख = कनपटी (सम्भावित; शब्द का सामान्य अर्थ शंख)। ‘निम्नयोः’ (सप्तमी द्विवचन) आवर्तों "
           "के साथ पढ़ा गया। सन्धि जाँची: उपरि + उत्कर्णम् → उपर्युत्कर्णम् (इ + उ → यु); सद्यः + मरणम् → सद्यो मरणम्; भ्रुवोः + उपरि → "
           "भ्रुवोरुपरि; निम्नयोः + आवर्तौ → निम्नयोरावर्तौ; दृष्टि + उपघातः → दृष्ट्युपघातः; उपघातः + वा → उपघातो वा (अः + घोष "
           "व्यंजन → ओ)।"),
    "40": ("गद्य; विश्वास उच्च; छपी पंक्ति ४२। डेटा में कोई पाठ-चिह्न नहीं, पर छपा ‘केशांतउत्क्षेपौ’ असामान्य जोड़ है: डेटा केशान्तौ + "
           "उत्क्षेपौ पढ़ता है, जिसकी नियमित सन्धि ‘केशान्तावुत्क्षेपौ’ (या ‘केशान्ता उत्क्षेपौ’) होती; इसके रूप पर कोई प्रश्न नहीं। शल्य = "
           "कोई भी चुभने वाली वस्तु; पाक = पकना। अज्ञात कर्ता ‘कोई व्यक्ति’ समझा गया। जीवेत् = विधिलिङ् प्रथम पुरुष एकवचन। सन्धि "
           "जाँची: शङ्खयोः + उपरि → शङ्खयोरुपरि; पाकात् + पतित → पाकात्पतित (अघोष प से पहले त् वैसा ही); पतितशल्यः + वा → "
           "पतितशल्यो वा; जीवेत् + न → जीवेन्न (न से पहले त् → न्, छपे अनुसार; यह वैकल्पिक है, द् भी सही); न + उद्धृत → नोद्धृत (अ + उ → ओ)।"),
}


# ===================================================================== AIDS
AIDS = {
    "28": {
        "frame": "कहाँ: पार्श्वयोः, जघन का बाहरी भाग, रीढ़ के दोनों ओर → कौन: कुकुन्दरौ (दो) → फल: चेष्टानाश (स्पर्श-शब्द का पाठ अनुमानित)।",
        "chunks": "पार्श्वयोर्जघनबहिर्भागे | पृष्ठवंशमुभयतः | कुकुंदरौ | तयोः | स्पर्शज्ञानमधःकाये | चेष्टानाशश्च",
        "sandhi": ("अ/आ से भिन्न स्वर के बाद विसर्ग + घोष → र्: बहिः + भागे → बहिर्भागे, पार्श्वयोः + जघन → पार्श्वयोर्जघन · "
                   "च से पहले विसर्ग → श्: चेष्टानाशः + च → चेष्टानाशश्च।"),
    },
    "29": {
        "chain": {"steps": ["श्रोणीकर्णों के ऊपर", "आशय को ढकने वाले", "नितम्ब (दो)", "फल: शोफ, दौर्बल्य और मरण"]},
        "chunks": "श्रोणीकर्णयोरुपर्याशयाच्छादनौ | पार्श्वन्तरप्रतिबद्धौ | नितंबौ | तयोरध.काये | शोफो दौर्बल्यं मरणं च",
        "sandhi": ("इ + आ → या: उपरि + आशय → उपर्याशय · अ + आ → आ: आशय + आच्छादनौ → आशयाच्छादनौ · "
                   "अः + घोष व्यंजन → ओ: शोफः + दौर्बल्यम् → शोफो दौर्बल्यम्।"),
    },
    "30": {
        "chain": {"steps": ["जघन और पार्श्व के बीच", "तिरछे और ऊपर की ओर", "पार्श्वसन्धि (दो)", "कोष्ठ रक्त से भरा",
                            "मरण"]},
        "chunks": "अधःपार्श्वन्तरप्रतिबद्धौ | जघनपार्श्वमध्ये | तिर्यगूर्ध्वं च | पार्श्वसंधी | तयोः | शोणितपूर्णकोष्ठतया मरणं",
        "sandhi": "स्वर से पहले अन्तिम क् → ग्: तिर्यक् + ऊर्ध्वम् → तिर्यगूर्ध्वम्।",
    },
    "31": {
        "chain": {"steps": ["बृहती पर आघात (समझा जाता है)", "रक्त का अतिप्रवाह", "उससे उपद्रव", "मरण"]},
        "chunks": "स्तनमूलयोरार्ज्जवेनोभयतः | पृष्ठवंशं | बृहत्यौ | तयोः | शोणितातिप्रवृत्तिनिमित्तैरुपद्रवैर्मरणं",
        "sandhi": ("अ + उ → ओ: आर्जवेन + उभयतः → आर्जवेनोभयतः · अ + अ → आ: शोणित + अति → शोणिताति · "
                   "ऐ के बाद विसर्ग + स्वर/घोष → र्: निमित्तैः + उपद्रवैः → निमित्तैरुपद्रवैः।"),
    },
    "32": {
        "frame": "कहाँ: रीढ़ के दोनों ओर, बाहु-मूल से जुड़े → कौन: अंसफलक (दो; सम्भवतः स्कन्धास्थियाँ) → फल: भुजा का स्वाप और शोष।",
        "chunks": "पृष्ठवंशमुभयतो | बाहुमूलसंबद्धे | अंसफलके | तयोर्बाहुस्वापशोषौ",
        "sandhi": ("ए पर समाप्त द्विवचन के बाद स्वर-सन्धि नहीं: संबद्धे अंसफलके · "
                   "अः + घोष व्यंजन → ओ: उभयतः + बाहु → उभयतो बाहु।"),
    },
    "33": {
        "frame": "कहाँ: ग्रीवा, बाहु और शिर के बीच → कौन: अंस (दो कन्धे) → फल: स्तब्धबाहुता (भुजाओं की अकड़न)।",
        "chunks": "ग्रीवाबाहुशिरोमध्येऽसपीठस्कंधबंधनावंसौ | तयोः | स्तब्धबाहुता",
        "sandhi": "औ + स्वर → आव्: बन्धनौ + अंसौ → बन्धनावंसौ · ए + अ → एऽ: मध्ये + अ- → मध्येऽ-।",
    },
    "34": {
        "diagram": {"groups": [
            {"label": "कण्ठनाड़ी के दोनों ओर ४ धमनियाँ", "items": ["२ नीला (नाम-पाठ पक्का नहीं)", "२ मन्या (नाम-पाठ पक्का नहीं)"]},
            {"label": "उनमें आघात से (वा: कोई एक)", "items": ["१ मूकता", "२ स्वर-वैकृत्य", "३ रस का अग्रहण"]}]},
        "chunks": "कंठनाडीमुभयतश्चतस्त्रो धमन्यः | तासां द्वे नीले द्वे मन्ये | तासु मूकता | स्वरवैकृत्यं | रसाग्राहिता वा भवति",
        "sandhi": ("च से पहले विसर्ग → श्: उभयतः + चतस्रः → उभयतश्चतस्रः · "
                   "अः + घोष व्यंजन → ओ: चतस्रः + धमन्यः → चतस्रो धमन्यः।"),
    },
    "35": {
        "frame": "कहाँ: ग्रीवायाम् उभयतः → कितनी: चतस्रः (४; कुल या हर ओर, पंक्ति नहीं कहती) सिराएँ → नाम: मातृकाः → फल: सद्यो मरणम्।",
        "chunks": "ग्रीवायामुभयतश्चतस्त्रः | सिरा | मातृकास्तासु | सद्यो मरणं",
        "sandhi": ("एक पंक्ति, विसर्ग के तीन रूप: आः + घोष → आ (सिरा मातृकाः) · त से पहले विसर्ग → स् (मातृकास्तासु) · "
                   "अः + घोष व्यंजन → ओ (सद्यो मरणम्)।"),
    },
    "36": {
        "diagram": {"groups": [
            {"label": "पंक्ति १", "items": ["कहाँ: शिर-ग्रीवा का जोड़", "कौन: कृकाटिका (दो)", "फल: चलमूर्धता"]},
            {"label": "पंक्ति २", "items": ["कहाँ: कानों के पीछे, नीचे", "कौन: विधुर (दो)", "फल: बाधिर्य"]}]},
        "chunks": "शिरोग्रीवयोः संधाने | कृकाटिके | तयोश्चलमूर्द्धता || कर्णपृष्ठयोरधःसंश्रितेविधुरे | तयोर्बाधिर्यं",
        "sandhi": "च से पहले विसर्ग → श्: तयोः + चल → तयोश्चल · ओ के बाद विसर्ग + घोष → र्: तयोः + बाधिर्यम् → तयोर्बाधिर्यम्।",
    },
    "37": {
        "frame": "कहाँ: घ्राणमार्ग के दोनों ओर, भीतर की ओर → कौन: फण (दो) → फल: गन्धाज्ञान (गन्ध न आना)।",
        "chunks": "घ्राणमार्गमुभयतः | श्रोत्रमार्गप्रतिबद्धमभ्यंतरतःफणौ | तयोर्गंधाज्ञानं",
        "sandhi": "अ + अ → आ: गन्ध + अज्ञानम् → गन्धाज्ञानम् · स्वर से पहले म् जुड़ता है: घ्राणमार्गम् + उभयतः → घ्राणमार्गमुभयतः।",
    },
    "38": {
        "frame": "कहाँ: भौंहों के पूँछ-छोरों के नीचे, आँखों के बाहर → कौन: अपाङ्ग (दो; सम्भवतः आँख का बाहरी कोना) → फल: आन्ध्य।",
        "chunks": "भ्रुवोः | पुच्छांतयोरधोऽक्ष्णोर्बाह्यतोऽपांगौ | तयोरांध्यं",
        "sandhi": ("अः + अ → ओऽ (अ लुप्त, ऽ से दिखाया): अधः + अक्ष्णोः → अधोऽक्ष्णोः, बाह्यतः + अपाङ्गौ → बाह्यतोऽपाङ्गौ · "
                   "ओ के बाद विसर्ग + स्वर → र्: तयोः + आन्ध्यम् → तयोरान्ध्यम्।"),
    },
    "39": {
        "contrast": {"groups": [
            {"label": "शङ्ख (दो; सम्भवतः कनपटियाँ)", "items": ["भौंह-छोरों के ऊपर, कान की ओर (सम्भावित)", "ललाट पर",
                                                          "फल: सद्यो मरण"]},
            {"label": "आवर्त (दो)", "items": ["भौंहों के ऊपर", "दो गड्ढों में", "फल: आन्ध्य या दृष्टि-उपघात"]}]},
        "chunks": "भ्रुवोः पुच्छांतयोरुपर्युत्कर्णं | ललाटे शंखौ | तयोः सद्यो मरणं || भ्रुवोरुपरि निम्नयोरावर्तौ | तयोरांध्यं दृष्ट्युपघातो वा",
        "sandhi": "इ + उ → यु: उपरि + उत्कर्णम् → उपर्युत्कर्णम्, दृष्टि + उपघातः → दृष्ट्युपघातः · अः + घोष व्यंजन → ओ: उपघातः + वा → उपघातो वा।",
    },
    "40": {
        "seesaw": "सशल्य (शल्य भीतर ही) ⇄ उद्धृतशल्य (शल्य निकाला गया): दोनों इसी पंक्ति में; पहला जी सकता है, दूसरा नहीं।",
        "chunks": "शंखयोरुपरि | केशांतउत्क्षेपौ | तयोः | सशल्यः | पाकात्पतितशल्यो वा | जीवेन्नोद्धृतशल्यः",
        "sandhi": ("न से पहले त् → न् (छपे अनुसार; वैकल्पिक, द् भी सही): जीवेत् + न → जीवेन्न · अ + उ → ओ: न + उद्धृत → नोद्धृत · "
                   "अः + घोष व्यंजन → ओ: पतितशल्यः + वा → पतितशल्यो वा।"),
        "pegs": "मेरा बनाया चित्र: काँटा चुभा है और उसी ने छेद को बन्द कर रखा है; खींचो तो छेद खुल जाए। (केवल याद की सहायता, पंक्ति का दावा नहीं)",
    },
}


# ============================================================== IMAGE_SPECS
IMAGE_SPECS = {
    ("29", "chain"): {
        "file": "sh7-nitamba-29.svg",
        "alt": ("Chain of unit 29 in line order: above the two śroṇīkarṇas, covering the āśaya, the two nitambas; results "
                "(listed together): swelling, weakness and death."),
        "type": "chain",
        "title": "इकाई २९: नितम्ब",
        "steps": ["श्रोणीकर्णों के ऊपर", "आशय को ढकने वाले", "नितम्ब (दो)", "फल: शोफ, दौर्बल्य और मरण"],
    },
    ("31", "chain"): {
        "file": "sh7-brihati-31.svg",
        "alt": ("Flowchart of unit 31: injury to the bṛhatī (understood) leads to excessive flow of blood, which causes "
                "complications, which lead to death."),
        "type": "mermaid",
        "code": ("flowchart TD\n"
                 "  A[\"बृहती पर आघात\"] --> B[\"रक्त का अतिप्रवाह\"]\n"
                 "  B --> C[\"उससे उपद्रव\"]\n"
                 "  C --> D[\"मरण\"]\n"),
    },
    ("34", "diagram"): {
        "file": "sh7-kantha-dhamani-34.svg",
        "alt": ("Flowchart of unit 34: four dhamanīs beside the throat-tube; two nīlā and two manyā (names not firm); in "
                "those, dumbness, or alteration of voice, or not perceiving taste (alternatives)."),
        "type": "mermaid",
        "code": ("flowchart TD\n"
                 "  A[\"कण्ठनाड़ी के दोनों ओर\"] --> B[\"चार धमनियाँ\"]\n"
                 "  B --> C[\"२ नीला (नाम अनिश्चित)\"]\n"
                 "  B --> D[\"२ मन्या (नाम अनिश्चित)\"]\n"
                 "  C --> E[\"आघात: कोई एक फल\"]\n"
                 "  D --> E\n"
                 "  E --> F[\"१ मूकता\"]\n"
                 "  E --> G[\"२ स्वर-वैकृत्य\"]\n"
                 "  E --> H[\"३ रस का अग्रहण\"]\n"),
    },
    ("36", "diagram"): {
        "file": "sh7-krikatika-vidhura-36.svg",
        "alt": ("Table of card 36 (two printed lines): kṛkāṭikā at the junction of head and neck, result an unsteady head; "
                "vidhura below the backs of the ears, result deafness."),
        "type": "table",
        "title": "कार्ड ३६: दो मर्म-युग्म",
        "heads": ["मर्म और स्थान", "फल"],
        "rows": [["कृकाटिका: शिर-ग्रीवा का जोड़", "चलमूर्धता: सिर डगमगाना"],
                 ["विधुर: कानों के पीछे, नीचे", "बाधिर्य: बहरापन"]],
    },
    ("39", "contrast"): {
        "file": "sh7-shankha-avarta-39.svg",
        "alt": ("Split of card 39: śaṅkha (probably the temples), above the brows' tail-ends, on the "
                "forehead, death at once; āvarta, above the brows in two hollows, blindness or damage to sight."),
        "type": "split",
        "title": "कार्ड ३९: शङ्ख और आवर्त",
        "cols": [["शङ्ख (सम्भवतः कनपटियाँ)", ["भौंह-छोरों के ऊपर", "ललाट पर", "फल: सद्यो मरण"]],
                 ["आवर्त", ["भौंहों के ऊपर", "दो गड्ढों में", "फल: अन्धापन या दृष्टि-हानि"]]],
    },
    ("40", "seesaw"): {
        "file": "sh7-utkshepa-shalya-40.svg",
        "alt": ("Split of card 40: may live, one with the dart still in, or one whose dart fell out through suppuration; "
                "may not live, one whose dart was pulled out."),
        "type": "split",
        "title": "कार्ड ४०: उत्क्षेप में शल्य",
        "cols": [["जी सकता है", ["सशल्य: शल्य भीतर", "पाक से शल्य गिरा"]],
                 ["नहीं जी सकता", ["उद्धृतशल्य: शल्य निकाला"]]],
    },
}
