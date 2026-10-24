from helpers import mcq, match, order, fill, multi, accepts

AUTHORED = {}

# ---------------------------------------------------------------- unit 55
AUTHORED["55"] = {
    "title": "धामार्गवो विशेषेण",
    "question": "In which ailments does unit 55 say dhāmārgava is especially used?",
    "rule": ("Dhāmārgava (a Luffa species, disputed), especially in gara, gulma, udara, kāsa and ailments from Kapha "
             "accumulation; in firm and heavy ones, in those in the seat of phlegm, and in Vāta-Kapha seated in the throat."),
    "limits": ("The unit has no verb; the use is understood. Whether -uttha-roga (arising ailments) covers every member or only "
               "Kapha accumulation is open. The identification of dhāmārgava is disputed (Luffa cylindrica or L. acutangula). "
               "The printed anusvāra in धांमार्गवो is a misprint and is not questioned. No dose is given."),
    "explain_hi": ("यहाँ से धामार्गव के वमन-योग शुरू होते हैं; धामार्गव तोरई-कुल (Luffa) का कोई पौधा है, पर कौन-सा, यह विवादित है। "
                   "पहली सूची: गर यानी बनाया हुआ विष, गुल्म यानी पेट की गाँठ, उदर यानी पेट का रोग, कास यानी खाँसी, और कफ के संचय से उठे रोग। "
                   "फिर रोगों के गुण: जो स्थिर और भारी हों, और जो कफ के आशय में बैठे हों। "
                   "अन्त में कण्ठ में आश्रय वाला वात-कफ। इकाई में क्रिया नहीं है; प्रयोग प्रसंग से समझा जाता है।"),
    "hook": "धामार्गव: जमा, भारी, कफ-स्थान का रोग, और गले में अटका वात-कफ।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "Which qualities of the ailments does unit 55 name for its drug?",
            ("Firm and heavy", "स्थिरेषु गुरुषु च = in those that are firm and heavy."),
            [("Light and mobile", "These are the opposites of स्थिर and गुरु."),
             ("Dry and rough", "Neither word stands in this unit."),
             ("Hot and sharp", "Hot and sharp are qualities of kṛtavedhana in line 05.01.65.")],
            "The drug is for ailments that are firm (स्थिर) and heavy (गुरु).",
            "स्थिर = firm; गुरु = heavy."),
        order(1, "Put the first members of the ailment compound of unit 55 in the order of the text.",
              ["गर", "गुल्म", "उदर", "कास", "कफसंचय"],
              "गरगुल्मोदरकासकफसंचयोत्थरोगेषु: concocted poison, abdominal lump, belly-ailment, cough, Kapha accumulation.",
              "गर · गुल्म · उदर · कास · कफसंचय."),
        match(2, "Match each word of unit 55 to its meaning.",
              [["गर", "concocted poison"], ["गुल्म", "abdominal lump"], ["कास", "cough"],
               ["श्लेष्माशय", "seat of phlegm"]],
              "Three ailments of the list and the place named after them.",
              "गर = concocted poison; गुल्म = abdominal lump; कास = cough; श्लेष्म-आशय = seat of phlegm.",
              role="extend",
              teaches="Unit 55: गर = concocted poison, गुल्म = abdominal lump, कास = cough, श्लेष्माशय = the seat of phlegm."),
        mcq("discriminate", 3, "Which is the right split of गुल्मोदर in unit 55?",
            ("गुल्म + उदर", "अ + उ → ओ: गुल्म + उदर → गुल्मोदर."),
            [("गुल्मम् + उदर", "Final म् before a vowel stays: that would give गुल्ममुदर."),
             ("गुल्मु + उदर", "उ + उ would give ऊ: गुल्मूदर."),
             ("गुल्मः + उदर", "अः before उ drops the visarga: गुल्म उदर, unjoined.")],
            "गुल्म (abdominal lump) + उदर (belly-ailment): अ + उ join as ओ.",
            "अ + उ → ओ (गुल्म + उदर → गुल्मोदर)."),
        mcq("apply", 4, "A patient has Vāta-Kapha lodged in the throat. Does unit 55 name its drug for him?",
            ("Yes: the last item names that state", "वातश्लेष्मणि च कण्ठाश्रये = and in Vāta-Kapha seated in the throat."),
            [("No: only belly ailments are named", "The list goes on to the seat of phlegm and the throat."),
             ("Only if it is light and mobile", "The unit names firm and heavy ailments, not light ones."),
             ("No: the throat comes in a later unit", "The throat is named in this very unit.")],
            "The unit closes with Vāta-Kapha whose seat is the throat.",
            "कण्ठ-आश्रय = having the throat as seat."),
        mcq("transfer", 5, "श्लेष्माशयस्थ means located in the seat of phlegm. What does a new word हृदयस्थ mean?",
            ("Located in the heart", "हृदय (heart) + स्थ (located in), as in श्लेष्माशय-स्थ."),
            [("Removing the heart's pain", "Removing would need -हर; -स्थ means located in."),
             ("Arising from the heart", "Arising would need -उत्थ, as in कफसंचयोत्थ."),
             ("Good for the heart", "Good for would need -हित or -हृद्य; -स्थ is located.")],
            "-स्थ after a place = located in it.",
            "X + स्थ = located in X; X + उत्थ = arising from X.",
            teaches="-स्थ = located in (श्लेष्माशयस्थ, हृदयस्थ); -उत्थ = arising from (कफसंचयोत्थ)."),
    ],
}

# ---------------------------------------------------------------- unit 56
AUTHORED["56"] = {
    "title": "जीवनीयान्यतमचूर्णसंयुक्तान् लेहान्",
    "question": "What lehas does unit 56 prescribe, and for which state of the doṣas?",
    "rule": ("Lehas (licked preparations) with the powder of any one of the jīvanīya group, with honey and sugar, made with "
             "their decoctions, are to be prescribed in the phlegm state in which Pitta is secondary."),
    "limits": ("Whose decoctions (तत्कषायैः) are meant is read as the drugs just named. The jīvanīya members are not listed "
               "here; an open note asks to keep jīvanīya as a group name only: no question on its effect. No dose is given."),
    "explain_hi": ("यह धामार्गव-खण्ड का एक लेह-योग है; लेह यानी चाटने की गाढ़ी औषध। "
                   "उसमें जीवनीय गण के किसी एक द्रव्य का चूर्ण, मधु और शर्करा मिलते हैं, और वह उन्हीं के काढ़ों से बनता है। "
                   "यह उस कफ की अवस्था में दिया जाए जिसमें पित्त गौण हो (पित्तोपसर्जन)। "
                   "उपसर्जन का अर्थ है ‘साथ चलने वाला, अप्रधान’: कफ प्रधान है, पित्त पीछे। "
                   "जीवनीय गण के सदस्य यहाँ नहीं गिनाए गए।"),
    "hook": "कफ आगे, पित्त पीछे: जीवनीय चूर्ण, शहद-शक्कर वाला लेह।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "What kind of preparation does unit 56 prescribe?",
            ("Lehas, preparations to be licked", "लेहान् = lehas (licked preparations), accusative plural."),
            [("Pills to be swallowed whole", "No pill (गुटिका) is named in this unit."),
             ("Oils to be put into the nose", "No oil or nasal use is named in this unit."),
             ("Pastes to be rubbed on skin", "No external paste is named in this unit.")],
            "The unit prepares lehas and prescribes them.",
            "लेह = a licked preparation; विदध्यात् = should prescribe."),
        order(1, "Put these parts of unit 56 in the order of the text.",
              ["प्रकल्प्य", "जीवनीयान्यतमचूर्णसंयुक्तान्", "समधुशर्करान्", "तत्कषायैः", "लेहान्", "पित्तोपसर्जने श्लेष्मणि"],
              "Having prepared, joined with jīvanīya powder, with honey and sugar, with their decoctions, lehas, in phlegm "
              "with Pitta secondary.",
              "प्रकल्प्य · …चूर्णसंयुक्तान् · समधुशर्करान् · तत्कषायैः · लेहान् · पित्तोपसर्जने श्लेष्मणि."),
        match(2, "Match each word of unit 56 to its meaning.",
              [["प्रकल्प्य", "having prepared"], ["अन्यतम", "any one (of several)"], ["शर्करा", "sugar"],
               ["उपसर्जन", "secondary, subordinate"]],
              "The action, the choice from the group, one added sweet, and the rank of Pitta.",
              "प्रकल्प्य = having prepared; अन्यतम = any one; शर्करा = sugar; उपसर्जन = secondary.",
              role="extend",
              teaches="Unit 56: प्रकल्प्य = having prepared, अन्यतम = any one of several, शर्करा = sugar, उपसर्जन = secondary."),
        mcq("discriminate", 3, "In पित्तोपसर्जने श्लेष्मणि, what is the place of Pitta?",
            ("Secondary to the phlegm", "पित्त-उपसर्जन (bahuvrīhi): the phlegm state in which Pitta is secondary."),
            [("Dominant over the phlegm", "उपसर्जन is subordinate, the opposite of dominant."),
             ("Wholly absent from it", "Absent would need a word like हीन; Pitta is present but secondary."),
             ("The only doṣa that is present", "श्लेष्मणि names phlegm as the main state.")],
            "Kapha is the main state; Pitta goes along with it as the lesser partner.",
            "उपसर्जन = accompanying, subordinate."),
        mcq("apply", 4, "Besides the jīvanīya powder, what two things go into the lehas of unit 56?",
            ("Honey and sugar", "समधुशर्करान् = with honey (मधु) and sugar (शर्करा)."),
            [("Ghee and rock salt", "Neither ghee nor salt is named in this unit."),
             ("Milk and jaggery", "Neither milk nor jaggery is named in this unit."),
             ("Oil and long pepper", "Neither is named in this unit.")],
            "The lehas are made with honey and sugar, and with the decoctions of the same drugs.",
            "स-मधु-शर्कर = with honey and sugar."),
        mcq("transfer", 5, "पित्तोपसर्जने means in which Pitta is secondary. What does a new word वातोपसर्जने mean?",
            ("In which Vāta is secondary", "Same bahuvrīhi: वात + उपसर्जन, with अ + उ → ओ."),
            [("In which Vāta is dominant", "उपसर्जन is secondary, not dominant."),
             ("In which Vāta is removed", "Removal would be -हर or -शमन, not उपसर्जन."),
             ("In which Pitta is secondary", "The new word names Vāta, not Pitta.")],
            "doṣa + उपसर्जन (bahuvrīhi) = the state in which that doṣa is secondary.",
            "X-उपसर्जन = with X secondary; अ + उ → ओ.",
            teaches="doṣa + उपसर्जन = in which that doṣa is secondary: पित्तोपसर्जन, वातोपसर्जन (अ + उ → ओ)."),
    ],
}

# ---------------------------------------------------------------- unit 57
AUTHORED["57"] = {
    "title": "धामार्गवकल्कं तुम्बरुधान्ययूषेण",
    "question": "With what broth is the dhāmārgava paste of unit 57 taken?",
    "rule": ("Dhāmārgava paste (कल्क) with a broth (यूष) of tumbaru (Zanthoxylum armatum, probable) and dhānya, in "
             "poisons (on a corrected reading)."),
    "limits": ("The printed विषेधु is not a word; the data reads विषेषु (in poisons): the use is not questioned. dhānya is "
               "literally grain; some lists read dhānyaka, coriander (disputed). No verb and no dose are given."),
    "explain_hi": ("धामार्गव का कल्क, यानी पीसी हुई लुगदी, एक यूष के साथ लिया जाता है। "
                   "यूष तुम्बरु और धान्य का है: तुम्बरु सम्भवतः तेजबल या तिमूर (Zanthoxylum armatum) है; धान्य का शाब्दिक अर्थ अनाज है, "
                   "कुछ सूचियाँ इसे धान्यक यानी धनिया पढ़ती हैं (विवादित)। "
                   "छपा ‘विषेधु’ कोई शब्द नहीं; डेटा इसे ‘विषेषु’ यानी विषों में पढ़ता है। "
                   "इकाई में क्रिया नहीं है।"),
    "hook": "धामार्गव की लुगदी, तुम्बरु-धान्य के यूष में।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "In what form is dhāmārgava taken in unit 57?",
            ("As a paste (कल्क)", "धामार्गवकल्कम् = dhāmārgava paste."),
            [("As a powder (चूर्ण)", "No powder is named in this unit."),
             ("As a juice (स्वरस)", "No juice is named in this unit."),
             ("As a ghee (सर्पिः)", "Ghee comes in line 05.01.64.")],
            "The drug is taken as kalka, a ground paste.",
            "कल्क = paste (ground wet)."),
        order(1, "Put the words of unit 57 in the order of the text (leave out the last word).",
              ["धामार्गव", "कल्कम्", "तुम्बरु", "धान्य", "यूषेण"],
              "Dhāmārgava paste, with the broth of tumbaru and dhānya.",
              "धामार्गव · कल्कम् · तुम्बरु · धान्य · यूषेण."),
        match(2, "Match each word of unit 57 to its meaning.",
              [["कल्क", "paste"], ["यूष", "broth"], ["तुम्बरु", "tumbaru (Zanthoxylum armatum, probable)"],
               ["धान्य", "dhānya (literally grain)"]],
              "The form of the drug, the liquid, and the two things the broth is made of.",
              "कल्क = paste; यूष = broth; तुम्बरु = Zanthoxylum armatum (probable); धान्य = literally grain.",
              role="extend",
              teaches="Unit 57: कल्क = paste, यूष = broth, तुम्बरु = tumbaru (Zanthoxylum armatum, probable), धान्य = literally grain."),
        mcq("discriminate", 3, "In तुम्बरुधान्ययूषेण, which member is the head that the others describe?",
            ("यूष (broth)", "The last member of a tatpuruṣa is its head: a broth of tumbaru and dhānya."),
            [("तुम्बरु (tumbaru)", "तुम्बरु names what the broth is made of."),
             ("धान्य (dhānya)", "धान्य names what the broth is made of."),
             ("No head: three equal items", "Only तुम्बरु and धान्य are paired; यूष is the head.")],
            "तुम्बरु-धान्य (a pair) + यूष (head): the broth of tumbaru and dhānya.",
            "Tatpuruṣa: the last member is the head."),
        mcq("apply", 4, "A student meets तुम्बरु in unit 57. What identification does the card give?",
            ("Zanthoxylum armatum (probable)", "The data: tumbaru = Zanthoxylum armatum (Hindi tejbal, timur), probable."),
            [("Coriander (disputed)", "Coriander is the disputed reading of dhānya, not of tumbaru."),
             ("Sponge gourd (disputed)", "Sponge gourd is one candidate for dhāmārgava."),
             ("Turmeric (standard)", "Turmeric (haridrā) is named in line 05.01.63.")],
            "Tumbaru is probably Zanthoxylum armatum, tejbal or timur in Hindi.",
            "तुम्बरु = Zanthoxylum armatum (probable)."),
        mcq("transfer", 5, "यूषेण (with broth) has ण because ष comes before it. Which new form means with milk (क्षीर)?",
            ("क्षीरेण", "र before the ending also turns न into ण: क्षीर + इन → क्षीरेण."),
            [("क्षीरेन", "After ष or र in the same word, the न of the ending becomes ण."),
             ("क्षीराय", "क्षीराय is dative: for milk."),
             ("क्षीरात्", "क्षीरात् is ablative: from milk.")],
            "Instrumental singular of an अ-stem ends in -एन, written -एण after ऋ, र or ष in the word.",
            "-एन → -एण after र/ष: यूषेण, क्षीरेण.",
            teaches="The instrumental -एन becomes -एण after र or ष in the word: यूष → यूषेण, क्षीर → क्षीरेण."),
    ],
}

# ---------------------------------------------------------------- unit 58
AUTHORED["58"] = {
    "title": "सुमनःसौमनस्यायवानी… मनोविकारेषु",
    "question": "With the decoction of which drugs, and in which disorders, does unit 58 use dhāmārgava?",
    "rule": ("With the decoction of any one of a long list (yavānī, haridrā, punarnavā, kāsamarda and others), or one or "
             "two dhāmārgava, in disorders of the mind."),
    "limits": ("Low confidence. The split of the long compound is doubtful (arbī unknown; saumanasyā as a name). Only "
               "yavānī, haridrā, punarnavā (standard) and kāsamarda (disputed) are identified. What one or two dhāmārgava "
               "counts, and its syntax, are open."),
    "explain_hi": ("यह मन के विकारों के लिए धामार्गव का योग है। "
                   "एक लम्बे समास में कई द्रव्य हैं; उनमें से किसी एक (अन्यतम) का काढ़ा लिया जाता है। "
                   "साफ़ पहचाने गए नाम: यवानी यानी अजवायन, हरिद्रा यानी हल्दी, पुनर्नवा यानी साँठी (मानक), और कासमर्द यानी कसौंदी (विवादित)। "
                   "बाकी नाम (सुमनः, सौमनस्या, चोरक, हैमवती, महासहा, क्षुद्रसहा, वृश्चीव, अर्बी) पहचाने नहीं गए, क्योंकि समास का विभाजन ही सन्दिग्ध है। "
                   "‘एक या दो धामार्गव’ में क्या गिना गया, यह पाठ नहीं कहता।"),
    "hook": "मन के विकार: किसी एक द्रव्य का काढ़ा, साथ में धामार्गव।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "For which disorders is the preparation of unit 58 used?",
            ("Disorders of the mind", "मनोविकारेषु = in disorders of the mind."),
            [("Disorders of the eye", "The eye is not named in this unit."),
             ("Disorders of the skin", "Skin diseases are named in line 05.01.66, not here."),
             ("Disorders of the belly", "Belly-ailments are named in line 05.01.60, not here.")],
            "The unit ends with मनोविकारेषु: in disorders of the mind.",
            "मनः (mind) + विकार (disorder)."),
        order(1, "Put these four clearer names of unit 58 in the order of the text.",
              ["यवानी", "हरिद्रा", "पुनर्नवा", "कासमर्द"],
              "In the long compound, yavānī and haridrā stand early, punarnavā and kāsamarda near its end.",
              "… यवानी · हरिद्रा · … · पुनर्नवा · कासमर्द …"),
        match(2, "Match each word of unit 58 to its meaning.",
              [["यवानी", "ajwain (standard)"], ["हरिद्रा", "turmeric (standard)"],
               ["पुनर्नवा", "spreading hogweed (standard)"], ["अन्यतम", "any one (of the list)"]],
              "Three identified drugs and the word that says how many are used.",
              "यवानी = ajwain; हरिद्रा = turmeric; पुनर्नवा = spreading hogweed; अन्यतम = any one.",
              role="extend",
              teaches="Unit 58: यवानी = ajwain, हरिद्रा = turmeric, पुनर्नवा = spreading hogweed (all standard); अन्यतम = any one."),
        mcq("discriminate", 3, "Which is the right split of मनोविकारेषु?",
            ("मनः + विकारेषु", "The stem मनस् ends in -अः; अः → ओ before a voiced sound (व)."),
            [("मन + ओविकारेषु", "There is no word ओविकार; the ओ comes from मनः."),
             ("मनु + विकारेषु", "मनु is a different word; उ would not become ओ here."),
             ("मना + विकारेषु", "आ before व stays आ: that would give मनाविकारेषु.")],
            "मनः (mind) + विकारेषु (in disorders): अः → ओ before व.",
            "अः + voiced consonant → ओ (मनः + विकार → मनोविकार)."),
        mcq("apply", 4, "A physician follows unit 58. How many drugs of the long list go into one decoction?",
            ("Any one of them", "अन्यतमकषायेण = with the decoction of any one of them."),
            [("All of them together", "अन्यतम means any one, not all."),
             ("Only the first two", "The text says any one, without naming which."),
             ("Haridrā, and it alone", "Haridrā is one choice among many, not the only one.")],
            "अन्यतम: one drug chosen from the list makes the decoction.",
            "अन्यतम = any one of several."),
        mcq("transfer", 5, "मनोविकार is a disorder of the mind. What does a new word नेत्रविकारेषु mean?",
            ("In disorders of the eye", "Same tatpuruṣa: नेत्र (eye) + विकार (disorder), locative plural."),
            [("In remedies for the eye", "A remedy would need a word like औषध; विकार is a disorder."),
             ("In the eyes of the mind", "मनस् is not in the new word."),
             ("In changes of the face", "नेत्र is the eye, not the face.")],
            "X-विकार = a disorder of X; -एषु = in (locative plural).",
            "Tatpuruṣa: मनो-विकार, नेत्र-विकार = disorder of the mind / eye.",
            teaches="X-विकार (tatpuruṣa) = disorder of X: मनोविकार (of the mind), नेत्रविकार (of the eye)."),
    ],
}

# ---------------------------------------------------------------- unit 59
AUTHORED["59"] = {
    "title": "धामार्गवमूलसिद्धक्षीरसंभवं सर्पिः",
    "question": "How is the ghee of unit 59 made, and for which disorders?",
    "rule": ("Ghee produced from milk cooked with dhāmārgava root, or ghee cooked with the six beginning with phala, in "
             "disorders of the mind."),
    "limits": ("The six beginning with phala (फलादि-षट्) are not listed here; phala may be madanaphala, but the text does "
               "not say: not questioned. How the ghee is drawn from the milk, and the dose, are not stated."),
    "explain_hi": ("मन के विकारों के लिए दो घृत-योग। "
                   "पहला: धामार्गव की जड़ से दूध पकाया जाता है (सिद्ध), और उसी दूध से घी बनता है (सम्भव)। "
                   "दूसरा: फल आदि छह द्रव्यों से पकाया घी; ये छह यहाँ नहीं गिनाए गए। "
                   "दूध से घी कैसे निकले, और कितना लें, यह पाठ नहीं कहता।"),
    "hook": "जड़ से दूध, दूध से घी: मन के विकारों में।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "What does unit 59 prepare for disorders of the mind?",
            ("Ghee (सर्पिः)", "सर्पिः = ghee, the main word of the unit."),
            [("A leha (लेह)", "Lehas come in line 05.01.61."),
             ("A paste (कल्क)", "The paste comes in line 05.01.62."),
             ("A broth (यूष)", "A broth comes in line 05.01.62.")],
            "Both options of the unit are ghees.",
            "सर्पिः = ghee."),
        order(1, "Put the words of unit 59 in the order of the text.",
              ["धामार्गवमूलसिद्धक्षीरसंभवम्", "सर्पिः", "फलादिषट्सिद्धम्", "वा", "मनोविकारेषु"],
              "Produced from milk cooked with dhāmārgava root, ghee, or cooked with the six from phala, in disorders of the mind.",
              "…क्षीरसंभवम् · सर्पिः · फलादिषट्सिद्धम् · वा · मनोविकारेषु."),
        match(2, "Match each word of unit 59 to its meaning.",
              [["मूल", "root"], ["सिद्ध", "cooked"], ["क्षीर", "milk"], ["संभव", "produced from"]],
              "The part of the drug, the process, the liquid and how the ghee comes from it.",
              "मूल = root; सिद्ध = cooked; क्षीर = milk; संभव = produced (from).",
              role="extend",
              teaches="Unit 59: मूल = root, सिद्ध = cooked, क्षीर = milk, संभव = produced from: ghee from milk cooked with the root."),
        mcq("discriminate", 3, "Which is the right split of फलादि in unit 59?",
            ("फल + आदि", "अ + आ → आ: फल + आदि → फलादि."),
            [("फलम् + आदि", "Final म् before a vowel stays: that would give फलमादि."),
             ("फलः + आदि", "अः before आ drops the visarga: फल आदि, unjoined."),
             ("फले + आदि", "ए before आ becomes अय्: फलयादि, or फल आदि.")],
            "फल + आदि (beginning with): two अ-sounds join as आ.",
            "अ + आ → आ (फल + आदि → फलादि)."),
        fill(4, "In unit 59 the milk is cooked with dhāmārgava ____ (root). Type it in Devanagari or in English letters (e.g. dharma).",
             accepts("मूल", "मूलम्", "mula"),
             "धामार्गवमूलसिद्धक्षीर = milk cooked with the root (मूल) of dhāmārgava.",
             "In unit 59 the root (मूल) of dhāmārgava is cooked in milk, and ghee is produced from that milk.",
             "मूल = root.", role="apply"),
        mcq("transfer", 5, "फलादि means the group beginning with phala. What does a new word पिप्पल्यादि mean?",
            ("The group beginning with pippalī", "पिप्पली + आदि (इ + आ → या): beginning with pippalī."),
            [("Pippalī without the others", "-आदि adds the others; it does not leave them out."),
             ("The end of the pippalī group", "-आदि marks the first member, not the last."),
             ("Six pieces of pippalī fruit", "No number is in the new word; षट् is not there.")],
            "X-आदि = (the items) beginning with X.",
            "X + आदि = beginning with X: फलादि, पिप्पल्यादि.",
            teaches="X-आदि = the group beginning with X: फलादि (from phala), पिप्पल्यादि (from pippalī, ई + आ → या)."),
    ],
}

# ---------------------------------------------------------------- unit 60
AUTHORED["60"] = {
    "title": "कृतवेधनमत्यर्थकटुतीक्ष्णोष्णम्",
    "question": "What qualities does unit 60 give kṛtavedhana, and in which ailments is it to be prepared?",
    "rule": ("Kṛtavedhana (probably ridged gourd), exceedingly pungent, sharp and hot, is to be prepared all the more in gara, "
             "udara, gulma, plīha (spleen), pāṇḍu-roga (anaemia) and śvayathu (swelling)."),
    "limits": ("The identification (Luffa acutangula, ridged gourd) is probable. The unit names no part, form or dose. "
               "Udara here is an ailment term (belly-ailment)."),
    "explain_hi": ("अब कृतवेधन, यानी सम्भवतः तोरई (Luffa acutangula)। "
                   "उसके गुण: अत्यन्त कटु, तीक्ष्ण और उष्ण। "
                   "इसलिए वह विशेष रूप से (सुतराम्) इन रोगों में तैयार किया जाए: गर यानी बनाया हुआ विष, उदर यानी पेट का रोग, गुल्म यानी पेट की गाँठ, "
                   "प्लीहा यानी तिल्ली का बढ़ना, पाण्डु-रोग यानी रक्ताल्पता और श्वयथु यानी सूजन। "
                   "कौन-सा अंग, किस रूप में और कितना, यह पाठ नहीं कहता।"),
    "hook": "बहुत कड़वा-तीखा-गरम कृतवेधन: तिल्ली, पाण्डु और सूजन पर।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "Which qualities does unit 60 give kṛtavedhana?",
            ("Pungent, sharp and hot", "अत्यर्थकटुतीक्ष्णोष्णम् = exceedingly pungent, sharp and hot."),
            [("Sweet, cold and heavy", "These are the opposites; none of them is named here."),
             ("Bitter, soft and cold", "Soft and cold are not named; कटु is pungent."),
             ("Salty, oily and moist", "None of these is named in this unit.")],
            "Kṛtavedhana is exceedingly (अत्यर्थ) pungent, sharp and hot.",
            "कटु = pungent; तीक्ष्ण = sharp; उष्ण = hot."),
        order(1, "Put the ailments of unit 60 in the order of the text.",
              ["गर", "उदर", "गुल्म", "प्लीह", "पाण्डुरोग", "श्वयथु"],
              "गरोदरगुल्मप्लीहपाण्डुरोगश्वयथुषु: concocted poison, belly-ailment, abdominal lump, spleen, pale-ailment, swelling.",
              "गर · उदर · गुल्म · प्लीह · पाण्डुरोग · श्वयथु."),
        match(2, "Match each ailment of unit 60 to its meaning.",
              [["प्लीह", "spleen (splenic enlargement)"], ["पाण्डुरोग", "pale-ailment (anaemia)"],
               ["श्वयथु", "swelling (oedema)"], ["गर", "concocted poison"]],
              "Four members of the ailment list with the equivalents of the card.",
              "प्लीह = spleen; पाण्डुरोग = anaemia; श्वयथु = swelling; गर = concocted poison.",
              role="extend",
              teaches="Unit 60: प्लीह = spleen (splenic enlargement), पाण्डुरोग = pale-ailment (anaemia), श्वयथु = swelling (oedema), गर = concocted poison."),
        mcq("discriminate", 3, "Which is the right split of तीक्ष्णोष्ण in unit 60?",
            ("तीक्ष्ण + उष्ण", "अ + उ → ओ: तीक्ष्ण + उष्ण → तीक्ष्णोष्ण."),
            [("तीक्ष्णम् + उष्ण", "Final म् before a vowel stays: that would give तीक्ष्णमुष्ण."),
             ("तीक्ष्णो + ष्ण", "There is no word ष्ण; the ओ comes from अ + उ."),
             ("तीक्ष्णे + उष्ण", "ए before उ becomes अय् or अ: तीक्ष्णयुष्ण or तीक्ष्ण उष्ण.")],
            "तीक्ष्ण (sharp) + उष्ण (hot): अ + उ join as ओ.",
            "अ + उ → ओ (तीक्ष्ण + उष्ण → तीक्ष्णोष्ण)."),
        multi("apply", 4, "Which two of these ailments does unit 60 name for kṛtavedhana?",
              [("Plīha (spleen)", "Right: प्लीह stands in the list."),
               ("Kāsa (cough)", "Wrong: cough is named for dhāmārgava in line 05.01.60, not here."),
               ("Jvara (fever)", "Wrong: fever is not named in this unit."),
               ("Śvayathu (swelling)", "Right: श्वयथु closes the list.")],
              [0, 3],
              "Plīha and śvayathu are in the list; cough and fever are not.",
              "गर, उदर, गुल्म, प्लीह, पाण्डुरोग, श्वयथु."),
        mcq("transfer", 5, "अत्यर्थकटु means exceedingly pungent. What does a new word अत्यर्थशीत mean?",
            ("Exceedingly cold", "अत्यर्थ (exceedingly) + शीत (cold)."),
            [("Slightly cold", "अत्यर्थ is beyond measure, not slightly."),
             ("Not cold at all", "अत्यर्थ intensifies; it does not deny."),
             ("Cold, then hot", "Only one quality, शीत, is in the new word.")],
            "अत्यर्थ before a quality = that quality to an extreme degree.",
            "अत्यर्थ + quality = exceedingly so: अत्यर्थकटु, अत्यर्थशीत.",
            teaches="अत्यर्थ before a quality means 'exceedingly': अत्यर्थकटु (exceedingly pungent), अत्यर्थशीत (exceedingly cold)."),
    ],
}

# ---------------------------------------------------------------- unit 61
AUTHORED["61"] = {
    "title": "कुटजफलं पुनः सुकुमारेषु",
    "question": "For whom and in which ailments does unit 61 apply kuṭaja fruit?",
    "rule": ("Kuṭaja (kuṛā, Holarrhena pubescens) fruit, on the other hand, is to be applied in delicate persons, in those "
             "with prominent blood, Pitta and Kapha, and in vātaśoṇita, visarpa, jvara, kuṣṭha and the rest."),
    "limits": ("Whether the middle compound means blood, Pitta and Kapha, or raktapitta and Kapha, is an open point: not "
               "questioned. The disease equivalents (vātaśoṇita = gout-type disease, visarpa = erysipelas-type infection) "
               "are standard in the data. No dose is given."),
    "explain_hi": ("अब कुटज यानी कुड़ा (Holarrhena pubescens, मानक) का फल; उसके बीज इन्द्रयव कहलाते हैं। "
                   "‘पुनः’ यहाँ ‘दूसरी ओर’ है: पिछली पंक्ति का कृतवेधन अत्यन्त तीक्ष्ण था, कुटज-फल सुकुमार यानी कोमल व्यक्तियों में दिया जाए। "
                   "फिर उन रोगियों में जिनमें रक्त, पित्त और कफ प्रबल हों (या रक्तपित्त और कफ: यह खुला प्रश्न है)। "
                   "और वातशोणित यानी वातरक्त (गठिया जैसा रोग), विसर्प यानी फैलने वाला त्वचा-संक्रमण, ज्वर यानी बुखार, कुष्ठ यानी कोढ़ समेत त्वचा-रोग आदि में।"),
    "hook": "तीखे कृतवेधन के बाद कोमल लोगों के लिए कुटज-फल।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "For what kind of persons does unit 61 name kuṭaja fruit?",
            ("Delicate persons (सुकुमार)", "सुकुमारेषु = in delicate persons."),
            [("Strong persons (बलवान्)", "Strength is not named in this unit."),
             ("Aged persons (वृद्ध)", "Age is not named in this unit."),
             ("Fat persons (स्थूल)", "Body size is not named in this unit.")],
            "Kuṭaja fruit is for the delicate, after the exceedingly sharp kṛtavedhana.",
            "सुकुमार = delicate, tender."),
        order(1, "Put these ailments of unit 61 in the order of the text.",
              ["वातशोणित", "विसर्प", "ज्वर", "कुष्ठ"],
              "वातशोणितविसर्पज्वरकुष्ठादिषु: vātaśoṇita, visarpa, fever, kuṣṭha and the rest.",
              "वातशोणित · विसर्प · ज्वर · कुष्ठ · आदि."),
        match(2, "Match each ailment of unit 61 to its meaning.",
              [["वातशोणित", "gout-type disease (vātarakta)"], ["विसर्प", "erysipelas-type spreading skin infection"],
               ["ज्वर", "fever"], ["कुष्ठ", "skin diseases, including leprosy"]],
              "The four named ailments with the standard equivalents of the card.",
              "वातशोणित = vātarakta; विसर्प = erysipelas; ज्वर = fever; कुष्ठ = skin diseases.",
              role="extend",
              teaches="Unit 61: वातशोणित = vātarakta (gout-type), विसर्प = erysipelas-type infection, ज्वर = fever, कुष्ठ = skin diseases incl. leprosy."),
        mcq("discriminate", 3, "Which is the right split of सुकुमारेषूल्बण in unit 61?",
            ("सुकुमारेषु + उल्बण", "उ + उ → ऊ: सुकुमारेषु + उल्बण → सुकुमारेषूल्बण."),
            [("सुकुमारेषः + उल्बण", "There is no form सुकुमारेषः; the locative plural is -एषु."),
             ("सुकुमारेषो + उल्बण", "ओ before उ becomes अव्: सुकुमारेषवुल्बण."),
             ("सुकुमारे + षूल्बण", "There is no word षूल्बण; ष belongs to -एषु.")],
            "सुकुमारेषु (in delicate persons) + उल्बण (prominent): two उ join as ऊ.",
            "उ + उ → ऊ (सुकुमारेषु + उल्बण → सुकुमारेषूल्बण)."),
        mcq("apply", 4, "A delicate patient has visarpa. Which drug does the text name for him?",
            ("Kuṭaja fruit", "कुटजफलं पुनः सुकुमारेषु … विसर्प…: kuṭaja fruit, for the delicate, in visarpa."),
            [("Kṛtavedhana", "Kṛtavedhana is exceedingly sharp, and visarpa is not in its list."),
             ("Dhāmārgava root", "Dhāmārgava root is for disorders of the mind (05.01.64)."),
             ("Tumbaru broth", "Tumbaru broth goes with dhāmārgava paste (05.01.62).")],
            "The delicate person and visarpa both point to kuṭaja fruit.",
            "कुटजफल: सुकुमार · वातशोणित, विसर्प, ज्वर, कुष्ठ."),
        mcq("transfer", 5, "कुष्ठादिषु means in kuṣṭha and the rest. What does a new word कासादिषु mean?",
            ("In cough and the rest", "कास (cough) + आदि (and the rest), locative plural."),
            [("In cough only", "-आदि adds the rest; it does not limit to one."),
             ("Before the cough begins", "-आदिषु is a locative of the list, not of time."),
             ("From cough and others", "From would be the ablative -आदिभ्यः.")],
            "X-आदिषु = in X and the rest (locative plural).",
            "X + आदि = X and the rest: कुष्ठादि, कासादि (अ + आ → आ).",
            teaches="X-आदिषु = in X and the rest: कुष्ठादिषु, कासादिषु (अ + आ → आ)."),
    ],
}

# ---------------------------------------------------------------- unit 62
AUTHORED["62"] = {
    "title": "कुटजफलचूर्णान्यर्कक्षीरेण सप्ताहं भावयित्वा",
    "question": "In which liquids is kuṭaja fruit powder made ready for emesis in unit 62?",
    "rule": ("Kuṭaja fruit powders soaked seven days in arka milk (latex), or in the decoction of madanaphala, jīmūtaka, "
             "ikṣvāku, jīvantī or jīvaka, or in water of mustard, mahua or salt, or with kṛśarā, are prepared for emesis."),
    "limits": ("Low confidence. Three printed words are flagged (the anusvāras in चूर्णांनि and मुलांन्यतम, and क्रूशरया for "
               "कृशरया): not questioned. Whether mūla (root) governs the whole second list or only jīvaka, and what each "
               "alternative is joined to, are open. No dose is given."),
    "explain_hi": ("कुटज-फल के चूर्ण से वमन-योग बनाने के कई विकल्प। "
                   "पहला: चूर्ण को अर्क यानी आक के दूध (उसका दूधिया रस) में सात दिन भिगोना (भावयित्वा)। "
                   "या मदनफल यानी मैनफल, जीमूतक, इक्ष्वाकु, जीवन्ती, जीवक में से किसी एक के काढ़े से; "
                   "या सर्षप यानी सरसों, मधूक यानी महुआ और लवण में से किसी एक के जल से; या चूर्ण को कृशरा के साथ। "
                   "सबका उद्देश्य एक: वमनाय, यानी वमन के लिए। ‘मूल’ पूरी सूची पर लगे या केवल जीवक पर, यह सन्दिग्ध है।"),
    "hook": "आक के दूध में सात दिन: कुटज-चूर्ण वमन के लिए तैयार।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "In what are the kuṭaja fruit powders of unit 62 first soaked?",
            ("Arka milk (latex)", "अर्कक्षीरेण = with the milk of arka (Calotropis), its latex."),
            [("She-goat's milk", "Goat's milk belongs to line 05.01.48."),
             ("Cow's urine", "Cow's urine is not named in this unit."),
             ("Plain honey", "Honey is not named in this unit.")],
            "The powders are soaked for seven days in the milk (latex) of arka.",
            "अर्क = Calotropis (standard); क्षीर = milk, here latex."),
        order(1, "Put these parts of unit 62 in the order of the text.",
              ["अर्कक्षीरेण सप्ताहं भावयित्वा", "मदनफल… कषायेण वा", "सर्षपमधूकलवण… अम्भसा वा", "वमनाय कल्पयेत्"],
              "Soaked in arka milk for seven days, or with a decoction, or with water, then prepared for emesis.",
              "अर्कक्षीर · कषाय · अम्भस् · वमनाय कल्पयेत्."),
        match(2, "Match each drug of unit 62 to its identification.",
              [["अर्क", "Calotropis, milkweed (standard)"], ["मदनफल", "Randia dumetorum, emetic nut (standard)"],
               ["मधूक", "mahua, Madhuca longifolia (standard)"], ["सर्षप", "mustard, Brassica (probable)"]],
              "Four drugs of the unit with the identifications the data gives.",
              "अर्क = Calotropis; मदनफल = Randia dumetorum; मधूक = mahua; सर्षप = mustard.",
              role="extend",
              teaches="Unit 62: अर्क = Calotropis (आक), मदनफल = Randia dumetorum (मैनफल), मधूक = mahua (all standard); सर्षप = mustard (probable)."),
        mcq("discriminate", 3, "Which is the right split of सप्ताहम् (for seven days)?",
            ("सप्त + अहम्", "अ + अ → आ: सप्त (seven) + अह (day) → सप्ताह."),
            [("सप्तम् + अहम्", "Final म् before a vowel stays: that would give सप्तमहम्."),
             ("सप्ते + अहम्", "ए before अ swallows it: that would give सप्तेऽहम्."),
             ("सप्त + हम्", "There is no word हम्, and no आ would arise.")],
            "सप्त (seven) + अह (day): two short अ join as आ.",
            "अ + अ → आ (सप्त + अह → सप्ताह)."),
        multi("apply", 4, "Which of these give the water (अम्भस्) of unit 62, any one of them?",
              [("Sarṣapa (mustard)", "Right: सर्षप is the first of the three."),
               ("Haridrā (turmeric)", "Wrong: haridrā is named in line 05.01.63, not here."),
               ("Lavaṇa (salt)", "Right: लवण is the third of the three."),
               ("Jīvaka", "Wrong: jīvaka belongs to the decoction list, not the water.")],
              [0, 2],
              "सर्षपमधूकलवणान्यतमाम्भसा: with water of any one of mustard, mahua and salt.",
              "Water of: सर्षप · मधूक · लवण."),
        mcq("transfer", 5, "वमनाय means for emesis (dative of purpose). What does a new form विरेचनाय mean?",
            ("For purgation", "विरेचन (purgation) + -आय, the dative of purpose."),
            [("By purgation", "By would be the instrumental विरेचनेन."),
             ("From purgation", "From would be the ablative विरेचनात्."),
             ("Of purgation", "Of would be the genitive विरेचनस्य.")],
            "The dative -आय of an अ-stem states the purpose: for X.",
            "X + आय = for X: वमनाय, विरेचनाय.",
            teaches="The dative -आय states the purpose: वमनाय (for emesis), विरेचनाय (for purgation)."),
    ],
}

# ---------------------------------------------------------------- unit 63
AUTHORED["63"] = {
    "title": "भवति चात्र",
    "question": "What is the role of भवति चात्र before the closing verse of the chapter?",
    "rule": "And here there is (this): a lead-in formula; it turns from the prose drug-lists to the verse of lines 05.01.69-70.",
    "limits": "The unit names no drug or method. 'This' (the verse that follows) is understood, not stated.",
    "explain_hi": ("‘भवति चात्र’ एक परिचय-वाक्य है: ‘और इस विषय में यह (कहा गया) है’। "
                   "अब तक अध्याय गद्य में द्रव्यों की सूचियाँ दे रहा था; इसके बाद पंक्ति 05.01.69-70 का एक श्लोक आता है। "
                   "‘यह’ (आने वाला श्लोक) शब्दों में नहीं, समझा जाता है। "
                   "चात्र = च + अत्र।"),
    "hook": "भवति चात्र: गद्य रुका, अब श्लोक।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "What does अत्र mean in भवति चात्र?",
            ("Here, in this matter", "अत्र = here, in this matter."),
            [("There, in that place", "There would be तत्र."),
             ("Now, at this time", "Now would be अधुना or इदानीम्."),
             ("Therefore, for that", "Therefore would be अतः or तस्मात्.")],
            "भवति चात्र = and here (in this matter) there is (this).",
            "अत्र = here."),
        match(1, "Match each word of unit 63 to its meaning.",
              [["भवति", "there is"], ["च", "and"], ["अत्र", "here, in this matter"]],
              "The formula has three words: the verb, the joining word and the place word.",
              "भवति = there is; च = and; अत्र = here."),
        order(2, "Put the three words hidden in भवति चात्र in the order of the text.",
              ["भवति", "च", "अत्र"],
              "भवति, then च, then अत्र, the last two joined as चात्र.",
              "भवति · च · अत्र.",
              role="extend",
              teaches="भवति चात्र = भवति + च + अत्र: there is, and, here."),
        mcq("discriminate", 3, "Which is the right split of चात्र?",
            ("च + अत्र", "अ + अ → आ: च + अत्र → चात्र."),
            [("चः + अत्र", "अः before अ gives ओऽ: that would be चोऽत्र."),
             ("चे + अत्र", "ए before अ gives एऽ: that would be चेऽत्र."),
             ("च + त्र", "There is no word त्र, and no आ would arise.")],
            "च (and) + अत्र (here): two short अ join as आ.",
            "अ + अ → आ (च + अत्र → चात्र)."),
        mcq("apply", 4, "What follows the formula of unit 63 in the text?",
            ("A verse, in lines 05.01.69-70", "The note: the formula introduces the verse of lines 05.01.69 and 05.01.70."),
            [("The colophon, at once", "The colophon (05.01.71) comes after the verse."),
             ("A new list of kuṭaja drugs", "The kuṭaja prose ended with iti in line 05.01.67."),
             ("The opening of chapter two", "Chapter two begins only after the colophon.")],
            "भवति चात्र introduces verse after prose.",
            "भवति चात्र → श्लोक."),
        mcq("transfer", 5, "च + अत्र gives चात्र. Which is the joined form of a new pair तत्र + अपि (there also)?",
            ("तत्रापि", "अ + अ → आ, as in च + अत्र → चात्र."),
            [("तत्रपि", "Two अ do not shrink to one short अ; they give आ."),
             ("तत्रेपि", "ए would come from अ + इ."),
             ("तत्रोपि", "ओ would come from अ + उ.")],
            "Same rule as चात्र: short अ + short अ = आ.",
            "अ + अ → आ.",
            teaches="Short अ + short अ join as आ: च + अत्र = चात्र, तत्र + अपि = तत्रापि."),
    ],
}

# ---------------------------------------------------------------- unit 64 (verse)
AUTHORED["64"] = {
    "title": "दिगित्येषा … बीजेनानेन मतिमान्",
    "question": "What does verse 64 say the emetic preparations of the chapter are, and what should the wise one do?",
    "rule": ("This is an indication (दिक्) of emetics, of the especially useful ones; with this seed (model), the wise one "
             "should devise others also."),
    "limits": ("Two printed words are flagged (वमनां for वमनानाम्, and the anusvāra in अन्यांनपि): not questioned. "
               "उपयोगिनाम् has no noun of its own; 'of the useful ones' is an inference. बीज is figurative: the model."),
    "explain_hi": ("अध्याय का समापन-श्लोक। "
                   "पहली पंक्ति: यह वमनों का, विशेष रूप से उपयोगी वमनों का, केवल एक दिशा-संकेत (दिक्) है, पूरी सूची नहीं। "
                   "दूसरी पंक्ति: इस बीज से, यानी इस नमूने से, बुद्धिमान (मतिमान्) दूसरे योग भी बनाए (विकल्पयेत्)। "
                   "यह पंक्ति 05.01.8 की बात से मेल खाता है, जहाँ कल्प को केवल उदाहरण बताया गया था।"),
    "hook": "सूची बीज है; पेड़ बुद्धिमान वैद्य उगाए।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "Who should devise further preparations, according to verse 64?",
            ("The wise one (मतिमान्)", "मतिमान् … विकल्पयेत् = the wise one should devise."),
            [("The patient (आतुर)", "The patient is not named in this verse."),
             ("The pupil (शिष्य)", "No pupil is named in this verse."),
             ("The nurse (परिचारक)", "No attendant is named in this verse.")],
            "The wise physician makes new preparations from the model given.",
            "मतिमान् = one possessing understanding."),
        order(1, "Put these words of verse 64 in the order of the text.",
              ["दिगित्येषा", "सुतरामुपयोगिनाम्", "बीजेनानेन", "मतिमान्", "विकल्पयेदिति"],
              "An indication, of the especially useful ones; with this seed the wise one should devise.",
              "दिगित्येषा · सुतरामुपयोगिनाम् · बीजेनानेन · मतिमान् · … विकल्पयेदिति."),
        match(2, "Match each word of verse 64 to its meaning.",
              [["दिक्", "indication, direction"], ["बीज", "seed (here: the model)"], ["मतिमान्", "the wise one"],
               ["विकल्पयेत्", "should vary, devise"]],
              "The two words for what the chapter is, and the two for what the reader does.",
              "दिक् = indication; बीज = seed, model; मतिमान् = wise; विकल्पयेत् = should devise.",
              role="extend",
              teaches="Verse 64: दिक् = indication, बीज = seed (the model), मतिमान् = the wise one, विकल्पयेत् = should vary, devise."),
        mcq("discriminate", 3, "Which is the right split of दिगित्येषा?",
            ("दिक् + इति + एषा", "क् → ग् before a vowel; इ + ए → ये: दिगित्येषा."),
            [("दिक् + इत्या + एषा", "आ + ए would give ऐ: दिगित्यैषा."),
             ("दिगि + त्येषा", "Neither दिगि nor त्येषा is a word."),
             ("दिशः + इति + एषा", "दिशः before इ would lose the visarga: दिश इत्येषा.")],
            "दिक् (indication) + इति (thus) + एषा (this): two sandhi joins.",
            "क् → ग् before a vowel; इ + ए → ये."),
        mcq("apply", 4, "In verse 64, what is बीज (seed) used to mean?",
            ("The model to build variations on", "The note: बीज is figurative, the model from which variations are made."),
            [("The tumbī seeds of line 05.01.56", "Those were a drug; here बीज is figurative."),
             ("A seed that is to be planted", "No sowing is meant; it is a figure of speech."),
             ("The kernel of the madana fruit", "Kernel is majjā; here बीज is the model.")],
            "As a seed grows into many plants, the given recipes grow into new ones.",
            "बीज (figurative) = the model, the starting point."),
        mcq("transfer", 5, "मतिमान् is one possessing mati (understanding). What does a new word बलवान् mean?",
            ("One possessing strength", "बल (strength) + -वान्, the same possessive suffix as -मान्."),
            [("One lacking strength", "Lacking would need -हीन; -वान् is possessing."),
             ("Strength itself", "बलम् is strength itself; -वान् names its possessor."),
             ("One who takes strength away", "Taking away would need -हर; -वान् is possessing.")],
            "-मान् / -वान् after a noun = one who possesses it.",
            "X + मान्/वान् = possessing X: मतिमान्, बलवान्.",
            teaches="-मान् / -वान् = one possessing: मतिमान् (understanding), बलवान् (strength)."),
    ],
}

# ---------------------------------------------------------------- unit 65
AUTHORED["65"] = {
    "title": "इति वमनकल्पो नाम प्रथमोऽध्यायः",
    "question": "Which chapter does unit 65 close, and what is its number?",
    "rule": "Thus the first chapter, named Vamanakalpa (preparations for emesis): the colophon of Kalpasthāna chapter 1.",
    "limits": "A closing formula: it adds no drug or method. The chapter's contents are those of lines 05.01.1-70.",
    "explain_hi": ("यह अध्याय की समाप्ति-पंक्ति (पुष्पिका) है। "
                   "इसका नाम ‘वमनकल्प’ है, यानी वमन के योग: मदनफल, जीमूतक, इक्ष्वाकु, तुम्बी, धामार्गव, कृतवेधन और कुटज के योग इसी में थे। "
                   "‘प्रथमः’ बताता है कि यह कल्पस्थान का पहला अध्याय है। "
                   "प्रथमोऽध्यायः = प्रथमः + अध्यायः।"),
    "hook": "इति: वमन के योगों का पहला अध्याय पूरा।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "What is the name of the chapter closed by unit 65?",
            ("Vamanakalpa", "वमनकल्पो नाम = named Vamanakalpa (preparations for emesis)."),
            [("Virecanakalpa", "Purgation is the subject of the next chapter, not this one."),
             ("Bastikalpa", "Enema is not the name given here."),
             ("Dinacaryā", "Dinacaryā is a Sūtrasthāna chapter.")],
            "The colophon names the chapter: Vamanakalpa.",
            "वमन = emesis; कल्प = preparations."),
        order(1, "Put the words of unit 65 in the order of the text.",
              ["इति", "वमनकल्पः", "नाम", "प्रथमः", "अध्यायः"],
              "Thus, Vamanakalpa, named, the first, chapter.",
              "इति · वमनकल्पः · नाम · प्रथमः · अध्यायः."),
        match(2, "Match each word of unit 65 to its meaning.",
              [["इति", "thus"], ["नाम", "named"], ["प्रथम", "first"], ["अध्याय", "chapter"]],
              "The four words around the chapter's name.",
              "इति = thus; नाम = named; प्रथम = first; अध्याय = chapter.",
              role="extend",
              teaches="Unit 65: इति = thus, नाम = named, प्रथम = first, अध्याय = chapter."),
        mcq("discriminate", 3, "Which is the right split of प्रथमोऽध्यायः?",
            ("प्रथमः + अध्यायः", "अः + अ → ओऽ: the अ of अध्यायः is swallowed (avagraha)."),
            [("प्रथम + अध्यायः", "अ + अ would give आ: प्रथमाध्यायः."),
             ("प्रथमो + ध्यायः", "There is no word ध्यायः; the ओ comes from प्रथमः."),
             ("प्रथमम् + अध्यायः", "Final म् before a vowel stays: प्रथमम् अध्यायः, or प्रथममध्यायः.")],
            "प्रथमः (first) + अध्यायः (chapter): अः before अ gives ओ, and ऽ marks the lost अ.",
            "अः + अ → ओऽ (प्रथमः + अध्यायः → प्रथमोऽध्यायः)."),
        fill(4, "The colophon calls this chapter the ____ (first) chapter. Type it in Devanagari or in English letters (e.g. dharma).",
             accepts("प्रथमः", "प्रथम", "prathama"),
             "प्रथमोऽध्यायः = प्रथमः (first) + अध्यायः (chapter).",
             "Unit 65 names the chapter Vamanakalpa and calls it the first (प्रथम) chapter.",
             "प्रथम = first.", role="apply"),
        mcq("transfer", 5, "प्रथमः + अध्यायः gives प्रथमोऽध्यायः. Which is the joined form of a new pair द्वितीयः + अध्यायः?",
            ("द्वितीयोऽध्यायः", "Same rule: अः + अ → ओऽ."),
            [("द्वितीयाध्यायः", "That joins द्वितीय + अध्याय without the visarga."),
             ("द्वितीयरध्यायः", "Visarga becomes र् only after a vowel other than अ or आ."),
             ("द्वितीयेऽध्यायः", "ए would belong to a locative द्वितीये; -अः before अ gives ओऽ.")],
            "-अः before अ: ओ, with avagraha for the lost अ.",
            "अः + अ → ओऽ.",
            teaches="-अः + अ- → -ओऽ-: प्रथमोऽध्यायः, द्वितीयोऽध्यायः."),
    ],
}


NOTES_HI = {
    "55": ("विश्वास: मध्यम। छपा ‘धांमार्गवो’ में अनुस्वार छपाई-दोष है (पंक्ति 05.01.62-64 में ‘धामार्गव’); इस शब्द पर प्रश्न नहीं बना। "
           "‘-उत्थरोग’ केवल कफसंचय पर लगे या सभी सदस्यों पर, यह दो-तरफ़ा है। स्थिर और गुरु रोगों के विशेषण माने गए। क्रिया नहीं। "
           "सन्धि जाँची: धामार्गवो विशेषेण = धामार्गवः + विशेषेण (अः → ओ घोष व से पहले); गुल्मोदर = गुल्म + उदर; कण्ठाश्रये = कण्ठ + आश्रये। छपा ‘कंठ’ = कण्ठ। "
           "पहचान (विवादित): धामार्गव = Luffa cylindrica या Luffa acutangula; कभी कृतवेधन/कोशातकी से भ्रम।"),
    "56": ("विश्वास: मध्यम। ‘तत्कषायैः’ = उन्हीं (अभी कहे द्रव्यों) के काढ़ों से, यह व्याख्या है। "
           "खुला बिन्दु (05.01.61): अंग्रेज़ी ‘life-promoting’ प्रभाव बताता है, केवल गण-नाम रखने का सुझाव; इस पर प्रश्न नहीं बना। "
           "जीवनीय गण (चरक की सूची, यहाँ जाँची नहीं): जीवक, ऋषभक, मेदा, महामेदा, काकोली, क्षीरकाकोली, मुद्गपर्णी, माषपर्णी, जीवन्ती, मधुक; कई विवादित। "
           "सन्धि जाँची: जीवनीयान्यतम = जीवनीय + अन्यतम; समधुशर्कराँस्तत्कषायैः = …शर्करान् + तत्… (न् → ंस् त से पहले); पित्तोपसर्जने = पित्त + उपसर्जने।"),
    "57": ("विश्वास: मध्यम। छपा ‘विषेधु’ कोई शब्द नहीं; डेटा ‘विषेषु’ (विषों में) पढ़ता है (षु/धु भ्रम); इस पर प्रश्न नहीं बना। "
           "धान्य शाब्दिक रूप से अनाज; कुछ सूचियाँ धान्यक यानी धनिया पढ़ती हैं (विवादित)। "
           "पहचान (सम्भावित): तुम्बरु = Zanthoxylum armatum, तेजबल/तिमूर। छपा ‘तुंबरु’ = तुम्बरु, ‘कल्कं’ में अन्त्य म् अनुस्वार। क्रिया नहीं।"),
    "58": ("विश्वास: निम्न। लम्बे समास का विभाजन सन्दिग्ध है, विशेषकर ‘वृश्चीवार्बीबीज’ (वृश्चीव + अर्बी + बीज, या वृश्ची + वार्बी…); अर्बी अज्ञात। "
           "खुला बिन्दु (05.01.63): अर्बी पर ‘सम्भावित’ चिह्न जोड़ने और अनुवाद को सन्दिग्ध रखने का सुझाव। ‘सौमनस्या’ द्रव्य-नाम है, यह भी सन्दिग्ध। "
           "‘एक या दो धामार्गव’ में गिनी गई वस्तु नहीं बताई; और धामार्गव मुख्य द्रव्य है या अलग विकल्प, यह दो-तरफ़ा। इन पर प्रश्न नहीं बने। "
           "पहचान: यवानी = अजवायन, हरिद्रा = हल्दी, पुनर्नवा = साँठी (मानक); कासमर्द = Senna occidentalis, कसौंदी (विवादित)। "
           "सन्धि जाँची: मनोविकारेषु = मनः + विकारेषु; धामार्गवमेकं = धामार्गवम् + एकम्।"),
    "59": ("विश्वास: मध्यम। ‘फलादिषट्’ = फल से शुरू होने वाले छह; यह गण यहाँ नहीं गिनाया गया, अनुवाद शाब्दिक है। ‘फल’ मदनफल हो सकता है, पर पाठ नहीं कहता। "
           "‘संभवम्’ = (दूध से) उत्पन्न; दूध से घी निकालने की विधि नहीं बताई। "
           "सन्धि जाँची: फलादि = फल + आदि; छपे ‘संभवं’, ‘सिद्धं’ में अन्त्य म् अनुस्वार। कोई छपाई-दोष चिह्नित नहीं।"),
    "60": ("विश्वास: मध्यम। ‘कल्पयेत्’ = तैयार करे, (प्रयोग के लिए) व्यवस्था करे। कटु = तीखा/चरपरा। "
           "डेटा ‘अत्यर्थकटुतीक्ष्णोष्ण’ को द्वन्द्व कहता है; ठीक-ठीक यह ‘अत्यर्थ’ से विशेषित गुणों का द्वन्द्व है। "
           "पहचान (सम्भावित): कृतवेधन = Luffa acutangula, तोरई। उदर यहाँ रोग-वाचक। "
           "सन्धि जाँची: कृतवेधनमत्यर्थ = कृतवेधनम् + अत्यर्थ; तीक्ष्णोष्ण = तीक्ष्ण + उष्ण; गरोदर = गर + उदर। छपा ‘पांडु’ = पाण्डु।"),
    "61": ("विश्वास: मध्यम। खुला बिन्दु (05.01.66): ‘उल्बणरक्तपित्तकफ’ को ‘रक्त, पित्त और कफ’ की जगह ‘रक्तपित्त और कफ’ पढ़ना अधिक सम्भव बताया गया; "
           "निर्णय मनुष्य पर छोड़ा गया, इसलिए इस पर प्रश्न नहीं बना। "
           "‘पुनः’ यहाँ ‘दूसरी ओर’ (पिछले कृतवेधन से विरोध)। "
           "पहचान (मानक): कुटज = Holarrhena pubescens, कुड़ा; बीज इन्द्रयव। वातशोणित = वातरक्त, विसर्प = फैलने वाला त्वचा-संक्रमण, कुष्ठ = कोढ़ समेत त्वचा-रोग। "
           "सन्धि जाँची: सुकुमारेषूल्बण = सुकुमारेषु + उल्बण (उ + उ → ऊ); कुष्ठादिषु = कुष्ठ + आदिषु।"),
    "62": ("विश्वास: निम्न। तीन छपाई-दोष चिह्नित: ‘चूर्णांन्यर्क’ (चूर्णान्यर्क, अतिरिक्त अनुस्वार), ‘मुलांन्यतम’ (मूलान्यतम), ‘क्रूशरया’ (कृशरया); "
           "खुला बिन्दु (05.01.67): चिह्नों का ‘src’ पूरा छपा शब्द हो, और ‘ञ/न से पहले अतिरिक्त अनुस्वार’ की आदत पूरी पुस्तक में है। इन पर प्रश्न नहीं बने। "
           "‘मूल’ पूरी दूसरी सूची पर लगे या केवल जीवक पर, यह सन्दिग्ध (मदनफल फल का नाम है)। विकल्पों का व्याकरण संक्षिप्त है। अन्तिम ‘इति’ खण्ड को बन्द करता है। "
           "पहचान: अर्क = आक, मदनफल = मैनफल, मधूक = महुआ (मानक); सर्षप = सरसों, जीवन्ती = Leptadenia reticulata, कृशरा = खिचड़ी जैसा पका व्यंजन (सम्भावित)। "
           "सन्धि जाँची: सप्ताहम् = सप्त + अहम्।"),
    "63": ("विश्वास: उच्च। परिचय-सूत्र; पंक्ति 05.01.68, 69, 70 एक साथ हैं (सूत्र, फिर दो अर्ध-पंक्तियों का एक श्लोक)। "
           "‘यह’ (आने वाला श्लोक) समझा जाता है। सन्धि जाँची: चात्र = च + अत्र (अ + अ → आ)। कोई छपाई-दोष नहीं।"),
    "64": ("विश्वास: मध्यम। छपा ‘वमनां’ = वमनानाम् (ना गिरा; अर्थ और आठ अक्षरों की पंक्ति के लिए आवश्यक); "
           "छपा ‘अन्यांनपि’ = अन्यानपि (अतिरिक्त अनुस्वार, सम्भवतः स्कैन-दोष)। इन दोनों पर प्रश्न नहीं बने। "
           "‘उपयोगिनाम्’ का अपना संज्ञा-शब्द नहीं; ‘उपयोगी (वमनों) का’ अनुमान है। ‘बीज’ लाक्षणिक: नमूना जिससे नए योग बनें। "
           "सन्धि जाँची: दिगित्येषा = दिक् + इति + एषा; सुतरामुपयोगिनाम् = सुतराम् + उपयोगिनाम्; बीजेनानेन = बीजेन + अनेन; विकल्पयेदिति = विकल्पयेत् + इति।"),
    "65": ("विश्वास: उच्च। अध्याय की पुष्पिका; आरम्भ का ‘॥’ दण्ड-चिह्न है। "
           "सन्धि जाँची: वमनकल्पो नाम = वमनकल्पः + नाम (अः → ओ घोष न से पहले); प्रथमोऽध्यायः = प्रथमः + अध्यायः (अः + अ → ओऽ)। कोई छपाई-दोष नहीं।"),
}


AIDS = {
    "55": {
        "diagram": {"groups": [{"label": "धामार्गव विशेष रूप से (पाठ-क्रम)",
                                "items": ["गर", "गुल्म", "उदर", "कास", "कफसंचय से उठे रोग", "स्थिर और भारी रोग",
                                          "कफ के आशय में स्थित रोग", "कण्ठ में बैठा वात-कफ"]}]},
        "sandhi": "अ + उ → ओ: गुल्म + उदर → गुल्मोदर; अ + आ → आ: कण्ठ + आश्रये → कण्ठाश्रये।",
        "anchors": "गर = बनाया हुआ विष · गुल्म = पेट की गाँठ · कास = खाँसी · स्थिर = टिका हुआ · गुरु = भारी · आशय = स्थान।",
    },
    "56": {
        "chain": {"steps": ["जीवनीय गण के किसी एक का चूर्ण", "मधु और शर्करा मिलाएँ", "उन्हीं के काढ़ों से",
                            "लेह तैयार करें", "पित्त-गौण कफ में दें"]},
        "anchors": "प्रकल्प्य = तैयार करके · अन्यतम = कोई एक · शर्करा = शक्कर · उपसर्जन = गौण, साथ चलने वाला · विदध्यात् = विधान करे।",
        "sandhi": "अ + उ → ओ: पित्त + उपसर्जने → पित्तोपसर्जने; अ + अ → आ: जीवनीय + अन्यतम → जीवनीयान्यतम।",
    },
    "57": {
        "chunks": "धामार्गवकल्कं | तुम्बरुधान्ययूषेण | विषेधु (= विषेषु?)।",
        "anchors": "कल्क = पीसी लुगदी · यूष = यूष, पतला शोरबा · तुम्बरु = तेजबल (सम्भावित) · धान्य = अनाज (शाब्दिक)।",
        "frame": "क्या: धामार्गव की लुगदी · किसके साथ: तुम्बरु-धान्य का यूष · किसमें: विषों में (सुधारे पाठ पर)।",
    },
    "58": {
        "frame": "क्या: सूची के किसी एक द्रव्य का काढ़ा · या: एक या दो धामार्गव · किसमें: मन के विकार।",
        "anchors": "यवानी = अजवायन · हरिद्रा = हल्दी · पुनर्नवा = साँठी · अन्यतम = कोई एक · मनोविकार = मन का विकार।",
        "sandhi": "अः + घोष → ओ: मनः + विकारेषु → मनोविकारेषु; म् + स्वर: धामार्गवम् + एकम् → धामार्गवमेकम्।",
    },
    "59": {
        "chain": {"steps": ["धामार्गव की जड़", "उससे दूध पकाएँ", "उस दूध से घी", "मन के विकारों में"]},
        "anchors": "मूल = जड़ · सिद्ध = पकाया हुआ · क्षीर = दूध · सर्पिः = घी · संभव = उत्पन्न।",
        "contrast": "पहला घी: जड़ से पके दूध से बना · दूसरा घी: फल आदि छह से पकाया।",
    },
    "60": {
        "diagram": {"groups": [{"label": "कृतवेधन के गुण", "items": ["अत्यन्त कटु", "तीक्ष्ण", "उष्ण"]},
                               {"label": "रोग (पाठ-क्रम)", "items": ["गर", "उदर", "गुल्म", "प्लीहा", "पाण्डु-रोग", "श्वयथु"]}]},
        "sandhi": "अ + उ → ओ: तीक्ष्ण + उष्ण → तीक्ष्णोष्ण, गर + उदर → गरोदर।",
        "anchors": "कटु = तीखा · तीक्ष्ण = तेज़ · उष्ण = गरम · प्लीहा = तिल्ली · पाण्डु = रक्ताल्पता · श्वयथु = सूजन।",
    },
    "61": {
        "diagram": {"groups": [{"label": "किसमें", "items": ["सुकुमार व्यक्ति", "रक्त-पित्त-कफ प्रबल"]},
                               {"label": "रोग (पाठ-क्रम)", "items": ["वातशोणित", "विसर्प", "ज्वर", "कुष्ठ", "आदि"]}]},
        "contrast": "कृतवेधन (पंक्ति 05.01.65): अत्यन्त तीक्ष्ण, कठोर रोगों में · कुटज-फल (यहाँ): ‘पुनः’, सुकुमारों में।",
        "sandhi": "उ + उ → ऊ: सुकुमारेषु + उल्बण → सुकुमारेषूल्बण; अ + आ → आ: कुष्ठ + आदिषु → कुष्ठादिषु।",
    },
    "62": {
        "chain": {"steps": ["कुटज-फल के चूर्ण", "आक के दूध में सात दिन भिगोएँ",
                            "या मदनफल आदि के काढ़े से", "या सरसों, महुआ, नमक के जल से",
                            "या कृशरा के साथ", "वमन के लिए तैयार"]},
        "anchors": "अर्क = आक · भावयित्वा = भिगोकर · सप्ताह = सात दिन · अम्भस् = जल · वमनाय = वमन के लिए।",
        "sandhi": "अ + अ → आ: सप्त + अहम् → सप्ताहम्।",
    },
    "63": {
        "chunks": "भवति | च | अत्र।",
        "sandhi": "अ + अ → आ: च + अत्र → चात्र।",
        "frame": "पहले: गद्य में द्रव्यों की सूचियाँ · यह सूत्र · बाद में: पंक्ति 05.01.69-70 का श्लोक, फिर पुष्पिका।",
    },
    "64": {
        "chain": {"steps": ["यह वमनों की केवल दिशा है", "विशेष रूप से उपयोगी वमनों की", "इस बीज (नमूने) से",
                            "बुद्धिमान दूसरे योग भी बनाए"]},
        "sandhi": "क् → ग् स्वर से पहले, इ + ए → ये: दिक् + इति + एषा → दिगित्येषा; त् → द्: विकल्पयेत् + इति → विकल्पयेदिति।",
        "pegs": "मेरा बनाया चित्र: एक बीज बोया, उससे पूरा बाग़ उगा; इस अध्याय के योग बीज हैं, नए योग बाग़।",
    },
    "65": {
        "chunks": "इति | वमनकल्पो नाम | प्रथमोऽध्यायः।",
        "sandhi": "अः + घोष → ओ: वमनकल्पः + नाम → वमनकल्पो नाम; अः + अ → ओऽ: प्रथमः + अध्यायः → प्रथमोऽध्यायः।",
        "frame": "अध्याय १ वमनकल्प: मदनफल · जीमूतक · इक्ष्वाकु · तुम्बी · धामार्गव · कृतवेधन · कुटज।",
    },
}


IMAGE_SPECS = {
    ("55", "diagram"): {
        "file": "ka1-dhamargava-uses-55.svg",
        "alt": ("Mind map of unit 55: dhamargava especially in gara, gulma, udara, kasa and ailments from kapha "
                "accumulation, in firm and heavy ailments, in those in the seat of phlegm, and in vata-kapha seated in the throat"),
        "type": "mermaid",
        "code": ("mindmap\n  धामार्गव विशेष रूप से\n    गर यानी बनाया विष\n    गुल्म यानी पेट की गाँठ\n    उदर\n"
                 "    कास यानी खाँसी\n    कफ-संचय के रोग\n    स्थिर और भारी रोग\n    कफ-आशय के रोग\n    कण्ठ का वात-कफ\n"),
    },
    ("56", "chain"): {
        "file": "ka1-jivaniya-leha-56.svg",
        "alt": ("Flowchart of unit 56: powder of any one jivaniya drug, with honey and sugar, made with their decoctions, "
                "gives lehas, prescribed in phlegm with pitta secondary"),
        "type": "mermaid",
        "code": ('flowchart TD\n  A["जीवनीय गण के<br/>किसी एक का चूर्ण"] --> B["मधु और शर्करा सहित"]\n'
                 '  B --> C["उन्हीं के काढ़ों से"]\n  C --> D["लेह"]\n  D --> E["पित्त-गौण कफ में दें"]\n'),
    },
    ("59", "chain"): {
        "file": "ka1-root-ghee-59.svg",
        "alt": ("Flowchart of unit 59: dhamargava root cooks the milk, ghee is produced from that milk; or ghee cooked "
                "with the six beginning with phala; both for disorders of the mind"),
        "type": "mermaid",
        "code": ('flowchart TD\n  A["धामार्गव की जड़"] --> B["उससे पका दूध"]\n  B --> C["उस दूध से घी"]\n'
                 '  D["फल आदि छह"] --> E["उनसे पका घी"]\n  C --> F["मन के विकारों में"]\n  E --> F\n'),
    },
    ("60", "diagram"): {
        "file": "ka1-kritavedhana-60.svg",
        "alt": ("Mind map of unit 60: kritavedhana with three qualities (exceedingly pungent, sharp, hot) and six "
                "ailments in text order: gara, udara, gulma, pliha, pandu-roga, shvayathu"),
        "type": "mermaid",
        "code": ("mindmap\n  कृतवेधन\n    गुण\n      अत्यन्त कटु\n      तीक्ष्ण\n      उष्ण\n    रोग\n      गर\n"
                 "      उदर\n      गुल्म\n      प्लीहा यानी तिल्ली\n      पाण्डु यानी रक्ताल्पता\n      श्वयथु यानी सूजन\n"),
    },
    ("61", "diagram"): {
        "file": "ka1-kutaja-uses-61.svg",
        "alt": ("Mind map of unit 61: kutaja fruit for delicate persons and those with prominent rakta, pitta and "
                "kapha, and in vatashonita, visarpa, jvara, kushtha and the rest"),
        "type": "mermaid",
        "code": ("mindmap\n  कुटज का फल\n    किसमें\n      सुकुमार व्यक्ति\n      रक्त-पित्त-कफ प्रबल\n    रोग\n"
                 "      वातशोणित\n      विसर्प\n      ज्वर यानी बुखार\n      कुष्ठ आदि\n"),
    },
    ("62", "chain"): {
        "file": "ka1-kutaja-emesis-62.svg",
        "alt": ("Flowchart of unit 62: kutaja fruit powder made ready for emesis in four ways: soaked seven days in "
                "arka milk, with a decoction of madanaphala and others, with water of mustard, mahua or salt, or with krishara"),
        "type": "mermaid",
        "code": ('flowchart LR\n  A["कुटज-फल<br/>का चूर्ण"] --> B["आक के दूध में<br/>सात दिन भिगोए"]\n'
                 '  A --> C["मदनफल आदि में से<br/>एक का काढ़ा"]\n  A --> D["सरसों, महुआ, नमक<br/>में से एक का जल"]\n'
                 '  A --> E["कृशरा के साथ"]\n  B --> F["वमन के लिए"]\n  C --> F\n  D --> F\n  E --> F\n'),
    },
    ("64", "chain"): {
        "file": "ka1-seed-model-64.svg",
        "alt": ("Chain of verse 64: this is only an indication of the useful emetics; with this seed, the wise one "
                "should devise others also"),
        "type": "chain",
        "title": "श्लोक ६४: बीज से नए योग",
        "steps": ["वमनों की दिशा", "उपयोगी वमनों की", "इस बीज से", "बुद्धिमान अन्य योग बनाए"],
    },
}
