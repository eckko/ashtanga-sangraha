from helpers import mcq, match, order, fill, multi, accepts


AUTHORED = {}

# ---------------------------------------------------------------- unit 15
AUTHORED["15"] = {
    "title": "वृद्धिविदारीजीवंतीर्वापयसा",
    "question": "By unit 15, which three drugs are named, and with what are they given?",
    "rule": ("Or (वा) vṛddhi (identity disputed), vidārī (probably Pueraria tuberosa) and jīvantī (Leptadenia "
             "reticulata; standard), with milk (पयसा). The verb, to make her drink, is carried from unit 14."),
    "limits": ("Prose. Vṛddhi's identity is disputed and vidārī's only probable (it may also be Ipomoea digitata): no "
               "question rests on which plants they are. No verb is printed; पाययेत् is carried from unit 14. No amount "
               "is given."),
    "explain_hi": ("यह गद्य-पंक्ति इकाई १४ के बाद एक और विकल्प देती है: वृद्धि, विदारी और जीवन्ती, दूध के साथ (पयसा)। "
                   "क्रिया ‘पिलाए’ (पाययेत्) इकाई १४ से चली आती है, यहाँ छपी नहीं। "
                   "वृद्धि को प्रायः अष्टवर्ग की औषधि (Habenaria intermedia) माना जाता है, पर यह पहचान विवादित है; विदारी "
                   "सम्भवतः विदारीकन्द (Pueraria tuberosa) है; जीवन्ती यानी डोडी (Leptadenia reticulata) मानक पहचान है। "
                   "‘जीवंतीर्वा’ में जीवन्तीः + वा है: ई के बाद का विसर्ग घोष वर्ण व से पहले र् बनता है।"),
    "hook": "वृद्धि, विदारी, जीवन्ती: दूध के साथ।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 15, with what are vṛddhi, vidārī and jīvantī given?",
            ("With milk (पयसा)", "वा पयसा: with milk, the instrumental of पयस्."),
            [("With honey (क्षौद्र)", "Honey goes with the blood in unit 14; unit 15 prints पयसा, milk."),
             ("With rice-water (अम्बु)", "Rice-water is an option of unit 16, not of unit 15."),
             ("With ghee (सर्पिस्)", "No ghee is named in unit 15; the word is पयसा.")],
            "The three drugs are given with milk.",
            "वृद्धिविदारीजीवन्तीर्वा पयसा."),
        order(1, "Put the words of unit 15 in the line's order.",
              ["वृद्धि", "विदारी", "जीवन्तीः", "वा", "पयसा"],
              "Vṛddhi, vidārī, jīvantī, or, with milk.",
              "वृद्धि → विदारी → जीवन्तीः → वा → पयसा."),
        match(2, "Match each word of unit 15 to the data's identification.",
              [["वृद्धि", "identity disputed (perhaps Habenaria intermedia)"],
               ["विदारी", "probably Pueraria tuberosa"],
               ["जीवन्ती", "Leptadenia reticulata (standard)"],
               ["पयसा", "with milk"]],
              "Each drug keeps its label: vṛddhi disputed, vidārī probable, jīvantī standard.",
              "वृद्धि (disputed), विदारी (probable), जीवन्ती (standard), पयसा = with milk.", role="extend",
              teaches="The three drugs carry three different labels: disputed, probable, standard."),
        mcq("discriminate", 3, "Why is जीवन्तीः printed जीवंतीर् before वा in unit 15?",
            ("ईः before voiced व becomes ईर्", "After a vowel other than अ or आ, a visarga becomes र् before a voiced sound; व is voiced."),
            [("र् is part of the stem जीवन्ती", "The stem is जीवन्ती; the र् comes from the visarga of -ईः."),
             ("ः becomes र् before any consonant", "Before an unvoiced consonant (क, त, प ...) it does not become र्."),
             ("र् marks the dual of जीवन्ती", "The data reads f. acc. pl. (-ईः), not a dual.")],
            "जीवन्तीः + वा = जीवन्तीर्वा: व is a voiced sound.",
            "Visarga after a vowel other than अ/आ + voiced sound → र्."),
        multi("apply", 4, "Which statements fit unit 15 and its data?",
              [("Jīvantī is a standard identification", "Right: Leptadenia reticulata, labelled standard."),
               ("Vṛddhi is identified for certain", "The data labels vṛddhi's identity disputed."),
               ("The verb is carried from unit 14", "Right: पाययेत् is carried from unit 14 and not printed."),
               ("A dose of milk is stated", "No amount is given in unit 15.")],
              [0, 2],
              "Jīvantī is standard, vṛddhi disputed; the verb comes from unit 14.",
              "वृद्धि (disputed) ... जीवन्ती (standard); verb carried."),
        mcq("transfer", 5, "By the rule of जीवंतीर्वा, how is मुनिः + वदति (the sage speaks) joined?",
            ("मुनिर्वदति", "इः before the voiced व becomes इर्, as जीवन्तीः + वा."),
            [("मुनिः वदति", "After इ the visarga does not stay before a voiced sound."),
             ("मुनिश्वदति", "श् comes before च, छ or श, not before व."),
             ("मुनी वदति", "Dropping the visarga with a long vowel happens only before र.")],
            "मुनिः + वदति = मुनिर्वदति, like जीवन्तीः + वा = जीवन्तीर्वा.",
            "Visarga after a vowel other than अ/आ + voiced sound → र्.",
            teaches="After a vowel other than अ or आ, a visarga becomes र् before a voiced sound: जीवन्तीः + वा → जीवन्तीर्वा."),
    ],
}

# ---------------------------------------------------------------- unit 16
AUTHORED["16"] = {
    "title": "नीलोत्पलसिता... वा तंडुलांबु वा",
    "question": "By unit 16, which further options are listed, and which printed forms are unclear?",
    "rule": ("Options joined by वा (or): nīlotpala (blue water lily), sitā (crystal sugar, or 'white'), an unclear form, "
             "sandalwood and the like (चन्दनादि); or rice-water (तण्डुलाम्बु); or an unclear form."),
    "limits": ("Low confidence. पक्लोष्ट and सरसान्यसरेण are unclear printed forms (पक्व-लोष्ट is only a guess): no "
               "question rests on them. सिता may be sugar or 'white': no question on its sense. The verb, carried from "
               "unit 14, is not supplied; how these are used is not stated."),
    "explain_hi": ("यह गद्य-पंक्ति इकाई १५ की सूची को आगे बढ़ाती है और ‘वा’ (अथवा) से विकल्प जोड़ती है: नीलोत्पल (नीला कमल), "
                   "सिता (मिश्री), चन्दन आदि; अथवा तण्डुलाम्बु यानी चावल का पानी। "
                   "दो छपे रूप, ‘पक्लोष्ट’ और ‘सरसान्यसरेण’, अस्पष्ट हैं; इनका अर्थ नहीं बनता, इसलिए इन पर कुछ नहीं बनाया गया। "
                   "‘सिता’ मिश्री मानी गई है, पर उसका अर्थ ‘श्वेत’ भी हो सकता है। "
                   "क्रिया इकाई १४ से चली आती है और यहाँ जोड़ी नहीं गई। इस इकाई का विश्वास निम्न है।"),
    "hook": "नीला कमल, चन्दन आदि, या चावल का पानी।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 16, which liquid is offered as one option?",
            ("Rice-water (तण्डुलाम्बु)", "तण्डुल (rice grain) + अम्बु (water)."),
            [("Goat's milk (आज पयस्)", "Goat's milk is the vehicle of unit 17, not of unit 16."),
             ("Onion juice (पलाण्डुरस)", "Onion juice comes in unit 27."),
             ("Sour gruel (काञ्जिक)", "No sour gruel is named in unit 16.")],
            "One option of unit 16 is rice-water.",
            "वा तण्डुलाम्बु वा."),
        order(1, "Put these sure words of unit 16 in the line's order.",
              ["नीलोत्पल", "सिता", "चन्दनादि", "तण्डुलाम्बु"],
              "Blue water lily, sitā, sandalwood and the like; or rice-water.",
              "नीलोत्पल → सिता → चन्दनादि → तण्डुलाम्बु."),
        match(2, "Match each word of unit 16 to its meaning.",
              [["नीलोत्पल", "blue water lily"], ["चन्दन", "sandalwood (standard)"], ["आदि", "and so on"],
               ["तण्डुल", "rice grain"], ["अम्बु", "water"]],
              "चन्दनादि = sandalwood and the like; तण्डुलाम्बु = rice-water.",
              "नीलोत्पल, चन्दन, आदि, तण्डुल, अम्बु.", role="extend",
              teaches="चन्दनादि = sandalwood and the like; तण्डुलाम्बु = rice (तण्डुल) water (अम्बु)."),
        mcq("discriminate", 3, "Which split of तंडुलांबु is right?",
            ("तण्डुल + अम्बु", "अ + अ → आ: तण्डुल + अम्बु = तण्डुलाम्बु."),
            [("तण्डुलः + अम्बु", "A compound member has no visarga; अः + अ would give तण्डुलोऽम्बु."),
             ("तण्डुलम् + अम्बु", "Final म् before a vowel stays: it would give तण्डुलमम्बु."),
             ("तण्डुला + म्बु", "म्बु is not a word; the word is अम्बु (water).")],
            "तण्डुल (rice grain) + अम्बु (water): अ + अ → आ.",
            "अ + अ → आ."),
        multi("apply", 4, "Which statements fit unit 16 and its data?",
              [("Its confidence is high", "The data marks unit 16 low confidence."),
               ("पक्लोष्ट is an unclear printed form", "Right: the note says it is not restorable."),
               ("The verb is printed in this line", "The verb is carried from unit 14 and not supplied."),
               ("Its options are joined by वा", "Right: वा (or) stands twice in the line.")],
              [1, 3],
              "Low confidence; two unclear forms; options joined by वा; no verb printed.",
              "... वा तण्डुलाम्बु वा ..."),
        mcq("transfer", 5, "By the rule of नीलोत्पल, how is सूर्य + उदयः (sunrise) joined?",
            ("सूर्योदयः", "अ + उ → ओ, as नील + उत्पल."),
            [("सूर्यौदयः", "अ + उ does not give औ; औ comes from अ + ओ or अ + औ."),
             ("सूर्युदयः", "The अ is not dropped before उ."),
             ("सूर्येदयः", "ए comes from अ + इ, not from अ + उ.")],
            "सूर्य + उदयः = सूर्योदयः, like नील + उत्पल = नीलोत्पल.",
            "अ + उ → ओ.",
            teaches="A short अ followed by उ joins as ओ: नील + उत्पल → नीलोत्पल."),
    ],
}

# ---------------------------------------------------------------- unit 17
AUTHORED["17"] = {
    "title": "गंधप्रियंग्वसितोत्पल... वाऽऽजेन पयसा",
    "question": "By unit 17, which drugs are listed, and in what milk?",
    "rule": ("One long compound: gandha, priyaṅgu (probably Callicarpa macrophylla), dark utpala, śālūka (probably a "
             "water-lily rhizome), the unripe fruit of udumbara (cluster fig; standard), shoots; or (वा) with goat's "
             "milk (आजेन पयसा)."),
    "limits": ("Groupings are uncertain (gandha-priyaṅgu, asita-utpala, udumbara-śalāḍu). न्यग्रोध rests on a possible "
               "correction of the printed 'ungrodha': no question on the banyan or its shoots. Gandha is unspecific. "
               "The verb is carried, not printed; no amount is given."),
    "explain_hi": ("यह पंक्ति एक लम्बा समास है, और फिर ‘वाऽऽजेन पयसा’ यानी अथवा बकरी के दूध से। "
                   "सूची में गन्ध (कोई सुगन्धित द्रव्य, अनिर्दिष्ट), प्रियंगु (सम्भवतः फूलप्रियंगु), काला उत्पल, शालूक "
                   "(सम्भवतः जलकमल का कन्द), उदुम्बर यानी गूलर (मानक) के कच्चे फल (शलाडु) और अंकुर (शृंग) हैं। "
                   "छपा ‘शलादुन्ग्रोध’ अर्थहीन है; इसे ‘शलाडु-न्यग्रोध’ (बरगद) पढ़ना केवल सम्भावित सुधार है, इसलिए बरगद पर "
                   "कोई प्रश्न नहीं। समूह बनाना भी अनिश्चित है: गन्ध-प्रियंगु एक नाम हो सकता है। "
                   "क्रिया पिछली इकाइयों से चली आती है।"),
    "hook": "प्रियंगु, उत्पल, शालूक, गूलर: बकरी के दूध से।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 17, which milk is named as the vehicle?",
            ("Goat's milk (आज)", "आजेन पयसा: with milk from the goat."),
            [("Sheep's milk (आविक)", "No sheep's milk is named in unit 17; आज = of the goat."),
             ("Buffalo milk (माहिष)", "No buffalo milk is named; the adjective is आज."),
             ("Camel's milk (औष्ट्र)", "No camel's milk is named; the adjective is आज.")],
            "The vehicle of unit 17 is goat's milk.",
            "वाऽऽजेन पयसा = or with goat's milk."),
        order(1, "Put these words of unit 17 in the line's order.",
              ["प्रियंगु", "असितोत्पल", "शालूक", "उडुंबर", "आजेन पयसा"],
              "Priyaṅgu, dark utpala, śālūka, udumbara, ... with goat's milk.",
              "प्रियंगु → असितोत्पल → शालूक → उडुंबर → आजेन पयसा."),
        match(2, "Match each word of unit 17 to the data's meaning.",
              [["प्रियङ्गु", "probably Callicarpa macrophylla"], ["शालूक", "probably a water-lily rhizome"],
               ["उडुम्बर", "cluster fig (standard)"], ["शलाडु", "unripe fruit"], ["आज", "of the goat"]],
              "Priyaṅgu and śālūka are probable; udumbara is standard; आजेन पयसा = with goat's milk.",
              "प्रियङ्गु, शालूक, उडुम्बर, शलाडु, आज.", role="extend",
              teaches="आज = 'of the goat' (from अज, goat): आजेन पयसा = with goat's milk."),
        mcq("discriminate", 3, "Which split of प्रियंग्वसित is right?",
            ("प्रियङ्गु + असित", "उ before a different vowel becomes व्: प्रियङ्गु + असित → प्रियङ्ग्वसित."),
            [("प्रियङ्गो + असित", "ओ + अ would give प्रियङ्गोऽसित, with ओ kept."),
             ("प्रियङ्गु + वसित", "This would give प्रियङ्गुवसित, keeping the उ."),
             ("प्रियङ्ग्व + सित", "प्रियङ्ग्व is not a word; the drug is प्रियङ्गु.")],
            "प्रियङ्गु (the drug) + असित (dark): उ + अ → व.",
            "उ + a different vowel → व् + that vowel."),
        multi("apply", 4, "Which statements fit unit 17 and its data?",
              [("The vehicle is goat's milk", "Right: वाऽऽजेन पयसा."),
               ("Gandha names one exact drug", "The data: gandha is unspecific."),
               ("The groupings in the compound are certain", "The note: groupings are uncertain."),
               ("Udumbara is the cluster fig", "Right: Ficus racemosa, labelled standard.")],
              [0, 3],
              "Goat's milk is the vehicle; udumbara is standard; gandha and the groupings stay open.",
              "उडुम्बर (standard) ... वाऽऽजेन पयसा."),
        mcq("transfer", 5, "By the rule of प्रियंग्वसित, how is मधु + अरिः (the enemy of Madhu) joined?",
            ("मध्वरिः", "उ + अ → व, as प्रियङ्गु + असित."),
            [("मधुरिः", "The अ is not dropped after उ."),
             ("मधवरिः", "उ becomes व् alone; अव् comes from ओ before a vowel."),
             ("मधारिः", "उ + अ does not give आ.")],
            "मधु + अरिः = मध्वरिः, like प्रियङ्गु + असित = प्रियङ्ग्वसित.",
            "उ + a different vowel → व् + that vowel.",
            teaches="उ before a different vowel becomes व्: प्रियङ्गु + असित → प्रियङ्ग्वसित."),
    ],
}

# ---------------------------------------------------------------- unit 18
AUTHORED["18"] = {
    "title": "कसेरुकमृणालशृंगाटक... शर्करामधुमधुरेण",
    "question": "By unit 18, which drugs make the liquid, and how is it sweetened?",
    "rule": ("Or with a liquid (read as a decoction, क्वाथ) of kaseruka, lotus stalk, śṛṅgāṭaka, kāśmarya, parūṣaka, "
             "drākṣā, sārivā and further drugs, made sweet with sugar and honey (शर्करामधुमधुरेण)."),
    "limits": ("Printed काथेन is read क्वाथेन (decoction) only as a possible correction; प्रोंडरीक = पुण्डरीक is "
               "conjectural and the syllable म is unclear: no question rests on these. Ananta is disputed; whether "
               "kanda-bīja (tuber, seed) belongs to utpala and puṇḍarīka only is uncertain."),
    "explain_hi": ("यह पंक्ति एक लम्बी सूची देती है: कसेरुक (सम्भवतः कसेरू), मृणाल (कमलनाल), शृंगाटक (सिंघाड़ा, मानक), काश्मर्य "
                   "(गम्भारी, मानक), परूषक (फालसा, मानक), द्राक्षा (अंगूर या मुनक्का, मानक), सारिवा (अनन्तमूल, मानक) और आगे "
                   "के द्रव्य; इनका द्रव शर्करा और शहद से मीठा किया जाए। "
                   "छपा ‘काथेन’ सम्भवतः ‘क्वाथेन’ (काढ़े से) है, पर यह सुधार निश्चित नहीं। "
                   "‘सारिवा’ के बाद का अक्षर ‘म’ अस्पष्ट है, और ‘प्रोंडरीक’ को पुण्डरीक (सम्भवतः श्वेत कमल) पढ़ना अनुमान है। "
                   "अनन्त की पहचान विवादित है; ‘कन्द-बीज’ किन-किन पर लागू है, यह भी तय नहीं।"),
    "hook": "लम्बी शीतल सूची, शर्करा और शहद से मीठी।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 18, what makes the liquid sweet?",
            ("Sugar and honey", "शर्करामधुमधुरेण: sweet with sugar (शर्करा) and honey (मधु)."),
            [("Jaggery and milk", "Neither is named in unit 18; the sweeteners are शर्करा and मधु."),
             ("Licorice and ghee", "Neither is in unit 18; licorice (madhuka) comes in unit 23."),
             ("Dates and raisins", "No dates are named; drākṣā is a list drug, the sweeteners are शर्करा and मधु.")],
            "The liquid is made sweet with sugar and honey.",
            "शर्करा + मधु + मधुर = sweet with sugar and honey."),
        order(1, "Put the first six drugs of unit 18 in the line's order.",
              ["कसेरुक", "मृणाल", "शृंगाटक", "काश्मर्य", "परूषक", "द्राक्षा"],
              "Kaseruka, lotus stalk, water chestnut, kāśmarya, phalsa, grape.",
              "कसेरुक → मृणाल → शृंगाटक → काश्मर्य → परूषक → द्राक्षा."),
        match(2, "Match each drug of unit 18 to the data's identification.",
              [["शृङ्गाटक", "water chestnut (standard)"], ["काश्मर्य", "Gmelina arborea (standard)"],
               ["परूषक", "phalsa, Grewia asiatica (standard)"], ["द्राक्षा", "grape or raisin (standard)"],
               ["सारिवा", "Hemidesmus indicus (standard)"], ["मृणाल", "lotus stalk"]],
              "Five drugs carry the label standard; मृणाल is the lotus stalk.",
              "शृङ्गाटक, काश्मर्य, परूषक, द्राक्षा, सारिवा, मृणाल.", role="extend",
              teaches="मृणाल = lotus stalk; śṛṅgāṭaka, kāśmarya, parūṣaka, drākṣā and sārivā are standard identifications."),
        mcq("discriminate", 3, "In unit 18, which drug's identity does the data label disputed?",
            ("अनन्त", "The data: ananta, perhaps the drug anantā; identity disputed."),
            [("काश्मर्य", "Kāśmarya is Gmelina arborea, labelled standard."),
             ("सारिवा", "Sārivā is Hemidesmus indicus, labelled standard."),
             ("परूषक", "Parūṣaka is phalsa, labelled standard.")],
            "Ananta may be a name of sārivā or a separate drug: disputed.",
            "अनन्त: identity disputed."),
        mcq("apply", 4, "Why does शर्करामधुमधुरेण end in -एण while काथेन ends in -एन?",
            ("An earlier र् turns न into ण", "After र in the same word (मधुर), with only a vowel between, the न of -एन becomes ण."),
            [("-एण marks the feminine instrumental", "Both are instr. sg.; a feminine one would end -या, as शर्करया."),
             ("-एण is the instrumental plural", "Both are singular; the a-stem instr. pl. ends -ऐः."),
             ("ण follows any long compound", "Length plays no part; the र before the ending does.")],
            "मधुर + एन → मधुरेण: र in the same word, only ए between.",
            "र ... (vowel) न → ण in the same word."),
        mcq("transfer", 5, "By the rule of मधुरेण, what is the instrumental singular of नर (man)?",
            ("नरेण", "र with only ए between: the न of -एन becomes ण, as मधुरेण."),
            [("नरेन", "After र in the same word, with only a vowel between, न does not stay."),
             ("नराण", "The a-stem instr. sg. ends -एन/-एण, not -आण."),
             ("नरेणा", "The instr. sg. of an a-stem has no long आ at the end.")],
            "नर + एन = नरेण, like मधुर + एन = मधुरेण.",
            "र ... (vowel) न → ण in the same word.",
            teaches="After र, ऋ or ष in the same word, with only a vowel between, न becomes ण: मधुर + एन → मधुरेण."),
    ],
}

# ---------------------------------------------------------------- unit 19
AUTHORED["19"] = {
    "title": "शालिपिष्टं जीवनीयशृतं वा क्षीरं",
    "question": "By unit 19, what two preparations are named?",
    "rule": ("Ground śāli (rice) flour (शालिपिष्ट); or milk (क्षीर) boiled (शृत) with the jīvanīya ('life-promoting') "
             "group. This is the literal two-item reading; the verb is carried from earlier units."),
    "limits": ("Ambiguous: the three neuter words may form one item (milk made with śāli flour or boiled with jīvanīya): "
               "no question on whether there are one or two items. The jīvanīya members are not named in this line. "
               "No verb, amount or time is printed."),
    "explain_hi": ("यह छोटी गद्य-पंक्ति दो विकल्प देती है: शालि चावल का पिसा चूर्ण (शालिपिष्ट), अथवा जीवनीय गण के साथ उबाला "
                   "हुआ (शृत) दूध (क्षीर)। "
                   "तीनों शब्द ‘पिष्टं’, ‘शृतं’ और ‘क्षीरं’ नपुंसकलिंग में मेल खाते हैं, इसलिए इसे एक ही वस्तु भी पढ़ा जा सकता है: "
                   "शालिचूर्ण से बना या जीवनीय से उबला दूध; यहाँ शाब्दिक दो-वस्तु पाठ लिया गया है। "
                   "जीवनीय एक औषधि-गण का मानक नाम है; उसके सदस्य इस पंक्ति में नहीं गिनाए गए। "
                   "क्रिया पिछली इकाइयों से चली आती है।"),
    "hook": "शालि का चूर्ण, या जीवनीय से उबला दूध।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 19, with what is the milk boiled?",
            ("The jīvanīya group", "जीवनीयशृतं क्षीरम्: milk boiled with the jīvanīya (life-promoting) group."),
            [("Juice of the onion", "Onion juice comes in unit 27, not in unit 19."),
             ("Bark of the banyan", "No bark is named in unit 19."),
             ("Neem leaves (निम्ब)", "No neem is named in unit 19.")],
            "The milk of unit 19 is boiled with the jīvanīya group.",
            "जीवनीय + शृत = boiled with the jīvanīya."),
        order(1, "Put the words of unit 19 in the line's order.",
              ["शालिपिष्टं", "जीवनीयशृतं", "वा", "क्षीरं"],
              "Śāli flour, boiled with jīvanīya, or, milk.",
              "शालिपिष्टं → जीवनीयशृतं → वा → क्षीरं."),
        match(2, "Match each word of unit 19 to its meaning.",
              [["शालि", "winter rice (standard)"], ["पिष्ट", "flour, ground paste"],
               ["जीवनीय", "the life-promoting drug group"], ["शृत", "boiled"], ["क्षीर", "milk"]],
              "शालिपिष्ट = śāli flour; जीवनीयशृत क्षीर = milk boiled with the jīvanīya.",
              "शालि, पिष्ट, जीवनीय, शृत, क्षीर.", role="extend",
              teaches="शृत = boiled: जीवनीयशृत = boiled with the jīvanīya."),
        mcq("discriminate", 3, "By unit 19 and its data, what is jīvanīya?",
            ("A drug group not listed here", "The note: the standard name of a drug group; its members are not named in this line."),
            [("The plant jīvantī of unit 15", "Jīvantī is one plant; jīvanīya is the name of a group."),
             ("A kind of red rice", "The rice of unit 19 is śāli; jīvanīya is a drug group."),
             ("The sweetener of the milk", "No sweetener is named in unit 19.")],
            "Jīvanīya is a group name; unit 19 does not list its members.",
            "जीवनीय = a drug group (members not named here)."),
        mcq("apply", 4, "Why do पिष्टं, शृतं and क्षीरं share the ending ं in unit 19?",
            ("All are neuter nom./acc. sg.", "The data: they agree (neuter); final -म् is printed ं."),
            [("All are optative verbs", "None is a verb; the verb is carried from earlier units."),
             ("All are feminine plurals", "They are neuter singular; a feminine plural ends -आः."),
             ("All are in the instrumental", "An a-stem instr. sg. ends -एन; these end -म्.")],
            "The three words agree as neuter singular.",
            "-म् (ं) = n. nom./acc. sg. here."),
        mcq("transfer", 5, "By the sense of जीवनीयशृतं क्षीरं, what does a new example मधुकशृतं क्षीरम् mean?",
            ("Milk boiled with madhuka", "X-शृत = boiled with X, as जीवनीयशृत."),
            [("Madhuka boiled in water", "The thing boiled is क्षीरम्, milk; madhuka is what it is boiled with."),
             ("Milk poured over madhuka", "शृत means boiled, not poured."),
             ("Madhuka taken after milk", "शृत names boiling, not an order of taking.")],
            "मधुकशृतं क्षीरम् = milk boiled with madhuka, like जीवनीयशृतं क्षीरम्.",
            "X-शृतं क्षीरम् = milk boiled with X.",
            teaches="शृत (boiled): X-शृतं क्षीरम् = milk boiled with X, as जीवनीयशृतं क्षीरम्."),
    ],
}

# ---------------------------------------------------------------- unit 20
AUTHORED["20"] = {
    "title": "बलाऽतिबला... रक्तशाल्योदनं सुशीतं भोजयेत्",
    "question": "By unit 20, what is she fed, and with what?",
    "rule": ("One should feed (भोजयेत्) very cool red śāli rice-meal (रक्तशाल्योदन) with milk prepared with balā, "
             "atibalā, śāli, ṣaṣṭika and kākolī, with honey and sugar; or with broth of jāṅgala game, cool in potency."),
    "limits": ("Printed केशु and भृतेन are read इक्षु (sugarcane) and शृतेन (boiled) only on a conjecture: no question on "
               "sugarcane root or on 'boiled'. Kākolī is disputed, atibalā only probable. No amount or time is given."),
    "explain_hi": ("इस पंक्ति की क्रिया ‘भोजयेत्’ (खिलाए) है, और भोजन है बहुत ठण्डा (सुशीत) लाल शालि चावल का भात (रक्तशाल्योदन)। "
                   "साथ में दूध, जो बला (बरियार, मानक), अतिबला (सम्भवतः कंघी), शालि, षष्टिक (साठी चावल) और काकोली (पहचान "
                   "विवादित) से तैयार हो, शहद और शर्करा के साथ। "
                   "अथवा भात शीतवीर्य जाङ्गल रस से खिलाए, यानी शुष्क प्रदेश के वन्य पशुओं का ऐसा रस जिसकी शक्ति (वीर्य) शीतल हो। "
                   "छपे ‘केशु’ को इक्षु (ईख) और ‘भृतेन’ को शृतेन (उबाला) पढ़ना अनुमान है, इसलिए इन पर प्रश्न नहीं।"),
    "hook": "ठण्डा लाल शालि-भात: औषध-दूध और शहद-शर्करा, या शीत जाङ्गल रस के साथ।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 20, what is she to be fed?",
            ("Very cool red śāli rice-meal", "रक्तशाल्योदनं सुशीतं भोजयेत्."),
            [("Warm barley gruel, lightly salted", "No barley or salt is named; the food is cool rice-meal."),
             ("Hot wheat bread with ghee", "No wheat is named; the food is सुशीत, very cool."),
             ("Raw fruit with sour curd", "No fruit or curd is named; the food is odana.")],
            "She is fed red śāli rice-meal, very cool.",
            "रक्तशाल्योदनं सुशीतं भोजयेत्."),
        order(1, "Put these phrases of unit 20 in the line's order.",
              ["पयसा समधुशर्करेण", "रक्तशाल्योदनं", "सुशीतं", "भोजयेत्", "शीतवीर्यजांगलरसेन वा"],
              "With milk, with honey and sugar, red śāli rice-meal, very cool, one should feed; or with cool jāṅgala broth.",
              "पयसा समधुशर्करेण → रक्तशाल्योदनं → सुशीतं → भोजयेत् → शीतवीर्यजांगलरसेन वा."),
        match(2, "Match each word of unit 20 to the data's meaning.",
              [["बला", "Sida cordifolia (standard)"], ["अतिबला", "probably Abutilon indicum"],
               ["षष्टिक", "rice ripening in sixty days"], ["काकोली", "identity disputed"],
               ["जाङ्गल", "dry-land game"]],
              "Balā is standard, atibalā probable, kākolī disputed; jāṅgala is game of arid country.",
              "बला, अतिबला, षष्टिक, काकोली, जाङ्गल.", role="extend",
              teaches="जाङ्गल = animals of arid country; their broth (रस) is meant."),
        mcq("discriminate", 3, "Which split of भोजयेच्छीत is right?",
            ("भोजयेत् + शीत", "त् + श → च्छ: भोजयेत् + शीत = भोजयेच्छीत."),
            [("भोजये + च्छीत", "च्छीत is not a word; the word is शीत (cool)."),
             ("भोजयेत् + छीत", "छीत is not a word; the छ comes from श after त्."),
             ("भोजयेः + शीत", "The data reads भोजयेत्, 3 sg. opt.; ः + श would not give च्छ.")],
            "भोजयेत् (should feed) + शीत (cool): त् + श → च्छ.",
            "त् + श → च्छ."),
        mcq("apply", 4, "By unit 20, what is the alternative broth like?",
            ("Cool in potency (शीतवीर्य)", "शीतवीर्यजाङ्गलरसेन: broth of dry-land game, cool in vīrya."),
            [("Hot in potency (उष्णवीर्य)", "The compound says शीत, cool, not उष्ण."),
             ("Sour in taste (अम्लरस)", "No taste of the broth is named."),
             ("From water animals (जलज)", "The broth is जाङ्गल, from dry-land game.")],
            "The broth is of dry-land game and cool in potency.",
            "शीतवीर्य जाङ्गलरस."),
        mcq("transfer", 5, "By the rule of भोजयेच्छीत, how is तत् + शरीरम् (that body) joined?",
            ("तच्छरीरम्", "त् + श → च्छ, as भोजयेत् + शीत."),
            [("तत्शरीरम्", "Before श, त् does not stay त्."),
             ("तद्शरीरम्", "त् becomes द् before voiced sounds; श is unvoiced."),
             ("तज्शरीरम्", "ज् would come before a voiced palatal (ज, झ), not before श.")],
            "तत् + शरीरम् = तच्छरीरम्, like भोजयेत् + शीत = भोजयेच्छीत.",
            "त् + श → च्छ.",
            teaches="त् before श: त् → च् and श → छ, written च्छ: भोजयेत् + शीत → भोजयेच्छीत."),
    ],
}

# ---------------------------------------------------------------- unit 21
AUTHORED["21"] = {
    "title": "रक्तपित्तक्रियाश्च शोधनवर्ज्याः प्रयुंजीत",
    "question": "By unit 21, which treatments are applied, and which are left out?",
    "rule": ("One should apply (प्रयुञ्जीत) the treatments (क्रियाः) of raktapitta, a bleeding disorder, excluding "
             "(वर्ज्याः) the cleansing (शोधन) ones, such as emesis and purgation."),
    "limits": ("Which raktapitta treatments are meant is not listed here. Raktapitta = a haemorrhagic (bleeding) disorder "
               "is a probable modern near-equivalent. Emesis and purgation are the data's examples of śodhana; the line "
               "itself names none."),
    "explain_hi": ("यह पंक्ति कहती है कि रक्तपित्त की चिकित्सा-क्रियाएँ (रक्तपित्तक्रियाः) प्रयोग करे (प्रयुञ्जीत), पर शोधन वाली "
                   "क्रियाओं को छोड़कर (शोधनवर्ज्याः)। "
                   "रक्तपित्त वह रोग है जिसमें शरीर के द्वारों से रक्त बहता है; आधुनिक निकट-समकक्ष रक्तस्राव का विकार सम्भावित है। "
                   "शोधन यानी शरीर-शोधन की क्रियाएँ, जैसे वमन और विरेचन। "
                   "कौन-कौन सी क्रियाएँ ली जाएँ, यह यहाँ नहीं गिनाया गया। ‘प्रयुञ्जीत’ आत्मनेपद विधिलिङ् है: प्रयोग करे।"),
    "hook": "रक्तपित्त की क्रियाएँ हाँ, शोधन नहीं।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 21, whose treatments are to be applied?",
            ("Those of raktapitta", "रक्तपित्तक्रियाः: the treatments of raktapitta, a bleeding disorder."),
            [("Those of fever (ज्वर)", "No fever is named; the compound is रक्तपित्त."),
             ("Those of cough (कास)", "Cough is not named in unit 21."),
             ("Those of diarrhoea", "No diarrhoea is named in unit 21.")],
            "The treatments of raktapitta are applied.",
            "रक्तपित्तक्रियाः प्रयुञ्जीत."),
        order(1, "Put the words of unit 21 in the line's order.",
              ["रक्तपित्तक्रियाः", "च", "शोधनवर्ज्याः", "प्रयुञ्जीत"],
              "The treatments of raktapitta, and, excluding cleansing, one should apply.",
              "रक्तपित्तक्रियाः → च → शोधनवर्ज्याः → प्रयुञ्जीत."),
        match(2, "Match each word of unit 21 to its meaning.",
              [["रक्तपित्त", "a bleeding disorder"], ["क्रिया", "treatment"], ["शोधन", "cleansing"],
               ["वर्ज्य", "to be excluded"], ["प्रयुञ्जीत", "should apply"]],
              "Apply the raktapitta treatments, with the cleansing ones excluded.",
              "रक्तपित्त, क्रिया, शोधन, वर्ज्य, प्रयुञ्जीत.", role="extend",
              teaches="वर्ज्य = to be excluded: शोधनवर्ज्याः = with the cleansing ones left out."),
        mcq("discriminate", 3, "Why is क्रियाः printed क्रियाश् before च in unit 21?",
            ("ः before च becomes श्", "A visarga before च or छ becomes श्."),
            [("ः before च becomes र्", "र् comes after vowels other than अ/आ, before voiced sounds; च is unvoiced."),
             ("ः before च becomes ओ", "ओ comes from अः before a voiced sound; here the vowel is आ and च is unvoiced."),
             ("ः before च is dropped", "The visarga is not dropped; it is written श्.")],
            "क्रियाः + च = क्रियाश्च.",
            "Visarga + च/छ → श्."),
        mcq("apply", 4, "By unit 21, which raktapitta treatments are left out?",
            ("Cleansing (शोधन)", "शोधनवर्ज्याः: the cleansing ones, such as emesis and purgation, are excluded."),
            [("Cooling (शीतल)", "No cooling measure is excluded; only शोधन is."),
             ("Soothing talk (कथा)", "Gentle talks are added in unit 22, not excluded."),
             ("Milk drinks (क्षीर)", "Milk is not excluded; only शोधन is.")],
            "Only the cleansing (śodhana) measures are excluded.",
            "शोधनवर्ज्याः = excluding śodhana."),
        mcq("transfer", 5, "By the rule of क्रियाश्च, how is बालाः + च (and the boys) joined?",
            ("बालाश्च", "The visarga before च becomes श्, as क्रियाः + च."),
            [("बाला च", "After आ the visarga drops only before voiced sounds; च is unvoiced."),
             ("बालार्च", "र् comes after vowels other than अ/आ, before voiced sounds."),
             ("बालास्च", "स् comes before त or थ; before च it is श्.")],
            "बालाः + च = बालाश्च, like क्रियाः + च = क्रियाश्च.",
            "Visarga + च/छ → श्.",
            teaches="A visarga before च or छ becomes श्: क्रियाः + च → क्रियाश्च."),
    ],
}

# ---------------------------------------------------------------- unit 22
AUTHORED["22"] = {
    "title": "सौम्याश्च मनोऽनुकूलाः कथाः",
    "question": "By unit 22, what kind of talks are also to be used?",
    "rule": ("And gentle (सौम्य) talks (कथाः), agreeable to the mind (मनोऽनुकूलाः). The verb प्रयुञ्जीत (should use) "
             "is carried from unit 21."),
    "limits": ("No verb is printed; the carried प्रयुञ्जीत is not supplied in the data. What the talks are about is not "
               "said. सौम्य also means 'cooling' (of the moon); the line does not choose between the senses."),
    "explain_hi": ("यह पंक्ति इकाई २१ की क्रिया ‘प्रयुञ्जीत’ से जुड़ती है: और सौम्य, मन के अनुकूल कथाएँ (भी प्रयोग करे)। "
                   "क्रिया यहाँ छपी नहीं, इकाई २१ से समझी जाती है। "
                   "‘सौम्य’ का अर्थ कोमल, शान्त है; चन्द्रमा से जुड़ा अर्थ ‘शीतल’ भी हो सकता है। "
                   "कथाएँ किस विषय की हों, यह नहीं बताया गया। "
                   "‘मनोऽनुकूलाः’ में मनः + अनुकूलाः है: अः + अ → ओऽ।"),
    "hook": "रक्तपित्त-क्रिया के साथ: सौम्य, मन भाती कथाएँ।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 22, what kind of talks are named?",
            ("Gentle, agreeable to the mind", "सौम्याः मनोऽनुकूलाः कथाः."),
            [("Stern, to warn her of risks", "Nothing stern is named; the talks are सौम्य, gentle."),
             ("Learned, about the scriptures", "No topic is named; only gentle and pleasing."),
             ("Loud, to keep her awake", "Nothing loud is named; the talks are सौम्य.")],
            "The talks are gentle and agreeable to the mind.",
            "सौम्याः मनोऽनुकूलाः कथाः."),
        order(1, "Put the words of unit 22 in the line's order.",
              ["सौम्याः", "च", "मनोऽनुकूलाः", "कथाः"],
              "Gentle, and, agreeable to the mind, talks.",
              "सौम्याः → च → मनोऽनुकूलाः → कथाः."),
        match(2, "Match each word of unit 22 to its meaning.",
              [["सौम्य", "gentle (also cooling)"], ["मनस्", "mind"], ["अनुकूल", "agreeable"], ["कथा", "talk, tale"]],
              "Gentle talks that are agreeable to the mind.",
              "सौम्य, मनस्, अनुकूल, कथा.", role="extend",
              teaches="अनुकूल = agreeable: मनोऽनुकूल = agreeable to the mind."),
        mcq("discriminate", 3, "Which split of मनोऽनुकूलाः is right?",
            ("मनः + अनुकूलाः", "अः + अ → ओऽ: the अ of अनुकूलाः is dropped, marked ऽ."),
            [("मन + अनुकूलाः", "अ + अ would give मनानुकूलाः, with आ."),
             ("मनो + नुकूलाः", "नुकूलाः is not a word; the word is अनुकूलाः."),
             ("मने + अनुकूलाः", "ए + अ would give मनेऽनुकूलाः, with ए.")],
            "मनः (mind) + अनुकूलाः (agreeable): अः + अ → ओऽ.",
            "अः + अ → ओऽ."),
        multi("apply", 4, "Which statements fit unit 22 and its data?",
              [("A new verb is printed in it", "No verb is printed; प्रयुञ्जीत is carried from unit 21."),
               ("सौम्य can also mean cooling", "Right: the note gives 'gentle', also 'cooling' (of the moon)."),
               ("The talks are agreeable to the mind", "Right: मनोऽनुकूलाः."),
               ("The topics of the talks are listed", "No topic is named in unit 22.")],
              [1, 2],
              "Gentle, pleasing talks; the verb comes from unit 21; no topics are given.",
              "सौम्याश्च मनोऽनुकूलाः कथाः."),
        mcq("transfer", 5, "By the rule of मनोऽनुकूलाः, how is बालः + अयम् (this boy) joined?",
            ("बालोऽयम्", "अः + अ → ओऽ, as मनः + अनुकूलाः."),
            [("बालायम्", "अः does not become आ before अ."),
             ("बाल अयम्", "Dropping the visarga and leaving a gap happens before vowels other than अ."),
             ("बालरयम्", "र् comes after vowels other than अ/आ.")],
            "बालः + अयम् = बालोऽयम्, like मनः + अनुकूलाः = मनोऽनुकूलाः.",
            "अः + अ → ओऽ.",
            teaches="अः before अ: अः → ओ and the अ is dropped, marked ऽ: मनः + अनुकूलाः → मनोऽनुकूलाः."),
    ],
}

# ---------------------------------------------------------------- unit 23
AUTHORED["23"] = {
    "title": "अदृष्टशोणितां तु ... पयः पाययेत्",
    "question": "By unit 23, what is given to her in whom no blood has been seen?",
    "rule": ("But (तु) for her in whom blood has not been seen (अदृष्टशोणिता), one should make her drink (पाययेत्) milk "
             "cooked (सिद्ध) with madhuka (licorice), payasyā (disputed) and asura-dāru (unidentified)."),
    "limits": ("Payasyā's identity is disputed; asura-dāru is unidentified and must not be equated with devadāru: no "
               "question on which plants they are, nor on how the last member splits (dāru may stand apart). No amount "
               "or timing is given."),
    "explain_hi": ("‘तु’ (परन्तु) से नया प्रसंग आरम्भ होता है: जिसमें रक्त दिखाई न दिया हो (अदृष्टशोणिता), यानी पीड़ा हो पर "
                   "स्राव न दिखे। "
                   "उसे मधुक (मुलेठी), पयस्या (पहचान विवादित) और असुरदारु (अज्ञात द्रव्य) के साथ पकाया हुआ (सिद्ध) दूध पिलाए "
                   "(पाययेत्)। "
                   "असुरदारु को देवदारु मानना ठीक नहीं; उसकी पहचान नहीं हुई। "
                   "‘अदृष्टशोणिता’ बहुव्रीहि है: वह स्त्री जिसका रक्त देखा नहीं गया।"),
    "hook": "रक्त न दिखे: मधुक-पयस्या से सिद्ध दूध।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 23, for whom is the cooked milk meant?",
            ("For her in whom no blood is seen", "अदृष्टशोणिताम्: her in whom blood has not been seen."),
            [("For her whose blood flows too much", "Too much flow is unit 10; unit 23 opens a new case with तु."),
             ("For her who has recently delivered", "No delivery is named in unit 23."),
             ("For her whose third month is over", "Months come up in unit 28 (not complete), not here.")],
            "The milk is for her in whom no blood has been seen.",
            "अदृष्टशोणितां तु ... पाययेत्."),
        order(1, "Put the words of unit 23 in the line's order.",
              ["अदृष्टशोणितां", "तु", "मधुकपयस्यासुरदारुभिः", "सिद्धं", "पयः", "पाययेत्"],
              "Her in whom blood is not seen, but, with madhuka, payasyā and asura-dāru, cooked, milk, one should make drink.",
              "अदृष्टशोणितां → तु → मधुकपयस्यासुरदारुभिः → सिद्धं → पयः → पाययेत्."),
        match(2, "Match each word of unit 23 to its meaning.",
              [["अदृष्ट", "not seen"], ["शोणित", "blood"], ["सिद्ध", "cooked"], ["पयस्", "milk"],
               ["पाययेत्", "should make (her) drink"]],
              "Milk cooked with three drugs, for her in whom blood is not seen.",
              "अदृष्ट, शोणित, सिद्ध, पयस्, पाययेत्.", role="extend",
              teaches="पाययेत् is the causative optative of √पा: should make (her) drink."),
        mcq("discriminate", 3, "Which reading of अदृष्टशोणिताम् fits unit 23?",
            ("She in whom blood is not seen", "A bahuvrīhi, f. acc. sg.: the woman in whom blood has not been seen."),
            [("The unseen blood itself", "शोणित is neuter; the f. acc. sg. -आम् names her, not the blood."),
             ("She in whom blood is seen", "The अ- negates: अदृष्ट = not seen."),
             ("Blood that she has not lost", "दृष्ट means seen, not lost.")],
            "अ + दृष्ट + शोणित, a bahuvrīhi: she whose blood has not been seen.",
            "अदृष्टशोणिता = she in whom blood is not seen."),
        multi("apply", 4, "Which statements fit unit 23 and its data?",
              [("Asura-dāru is the same as devadāru", "The note: do not equate it with devadāru; it is unidentified."),
               ("The line names a dose of milk", "No amount is given in unit 23."),
               ("The milk is cooked with madhuka", "Right: मधुक... सिद्धं पयः."),
               ("Payasyā's identity is disputed", "Right: the data labels payasyā disputed.")],
              [2, 3],
              "Milk cooked with madhuka and others; payasyā disputed, asura-dāru unidentified.",
              "मधुकपयस्यासुरदारुभिः सिद्धं पयः."),
        mcq("transfer", 5, "By the sense of पाययेत्, what does a new example बालं क्षीरं पाययेत् mean?",
            ("One should make the child drink milk", "पाययेत् is causative: should make (someone) drink."),
            [("The child should drink milk alone", "'Should drink' would be पिबेत्; पाययेत् is causative."),
             ("One should boil the milk for a child", "पाययेत् means make drink, not boil."),
             ("One should give the child no milk", "No negation (न) is in the sentence.")],
            "बालं क्षीरं पाययेत् = one should make the child drink milk, as पयः पाययेत्.",
            "पाययेत् (causative of √पा) = should make (someone) drink.",
            teaches="पाययेत् (causative optative of √पा) = should make (someone) drink; पिबेत् = should drink."),
    ],
}

# ---------------------------------------------------------------- unit 24
AUTHORED["24"] = {
    "title": "ताम्रवल्ल्यश्मंतकशतावरीपयस्याभिर्वा",
    "question": "By unit 24, with which drugs is the milk understood to be cooked?",
    "rule": ("Or (वा) with tāmravallī (unidentified), aśmantaka (disputed; usually Bauhinia racemosa), śatāvarī "
             "(Asparagus racemosus; standard) and payasyā (disputed). Milk cooked with these, as in unit 23, is understood."),
    "limits": ("Elliptical: the milk and the verb are understood from unit 23, not printed. Tāmravallī is unidentified, "
               "aśmantaka and payasyā disputed: no question on which plants they are. No amount is given."),
    "explain_hi": ("यह इकाई २३ का एक और विकल्प है: अथवा ताम्रवल्ली, अश्मन्तक, शतावरी और पयस्या के साथ। "
                   "दूध और ‘पिलाए’ क्रिया इकाई २३ से समझे जाते हैं, यहाँ छपे नहीं। "
                   "शतावरी (Asparagus racemosus) की पहचान मानक है; अश्मन्तक को प्रायः आपटा (Bauhinia racemosa) माना जाता है, "
                   "पर यह विवादित है; पयस्या भी विवादित है; ताम्रवल्ली (ताम्र-रंग की लता) पहचानी नहीं गई। "
                   "तृतीया बहुवचन ‘-भिः’ समास के अन्त में एक ही बार लगा है (पयस्याभिः)।"),
    "hook": "ताम्रवल्ली, अश्मन्तक, शतावरी, पयस्या: वही सिद्ध दूध।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 24, which drug of the list has a standard identification?",
            ("Śatāvarī (Asparagus racemosus)", "The data labels śatāvarī standard."),
            [("Tāmravallī (a copper-hued creeper)", "The data: tāmravallī is unidentified."),
             ("Aśmantaka (Bauhinia racemosa)", "The data: usually Bauhinia racemosa, but disputed."),
             ("Payasyā (kṣīravidārī)", "The data labels payasyā disputed.")],
            "Only śatāvarī is a standard identification in unit 24.",
            "शतावरी (standard)."),
        order(1, "Put the words of unit 24 in the line's order.",
              ["ताम्रवल्ली", "अश्मन्तक", "शतावरी", "पयस्याभिः", "वा"],
              "Tāmravallī, aśmantaka, śatāvarī, with payasyās, or.",
              "ताम्रवल्ली → अश्मन्तक → शतावरी → पयस्याभिः → वा."),
        match(2, "Match each part of unit 24 to its meaning.",
              [["ताम्र", "copper(-coloured)"], ["वल्ली", "creeper"], ["शतावरी", "Asparagus racemosus (standard)"],
               ["-भिः", "with (instr. pl.)"], ["वा", "or"]],
              "ताम्रवल्ली = copper-coloured creeper (unidentified); -भिः closes the list.",
              "ताम्र, वल्ली, शतावरी, -भिः, वा.", role="extend",
              teaches="-भिः is the instr. pl. ending; at the end of the compound it serves the whole list."),
        mcq("discriminate", 3, "Which split of ताम्रवल्ल्यश्मंतक is right?",
            ("ताम्रवल्ली + अश्मन्तक", "ई before a different vowel becomes य्: वल्ली + अ → वल्ल्य."),
            [("ताम्रवल्ले + अश्मन्तक", "ए + अ would give ताम्रवल्लेऽश्मन्तक."),
             ("ताम्रवल्लू + अश्मन्तक", "ऊ + अ would give व्, not य्."),
             ("ताम्रवल्ल्य + श्मन्तक", "श्मन्तक is not a word; the drug is अश्मन्तक.")],
            "ताम्रवल्ली + अश्मन्तक: ई + अ → य.",
            "ई + a different vowel → य् + that vowel."),
        mcq("apply", 4, "In unit 24, what is understood but not printed?",
            ("Milk cooked with these", "As in unit 23, the cooked milk is understood."),
            [("Ghee cooked in onion juice", "Onion juice belongs to unit 27, not here."),
             ("A powder licked with honey", "Licking with honey is unit 12."),
             ("Rice-meal served very cool", "Cool rice-meal is unit 20.")],
            "Unit 24 only lists drugs; the milk and the verb come from unit 23.",
            "... पयस्याभिर्वा (सिद्धं पयः, understood)."),
        mcq("transfer", 5, "By the rule of ताम्रवल्ल्यश्मंतक, how is नदी + अत्र (the river here) joined?",
            ("नद्यत्र", "ई + अ → य, as ताम्रवल्ली + अश्मन्तक."),
            [("नदीत्र", "The अ is not dropped after ई."),
             ("नद्यात्र", "या would come from ई + आ, not from ई + अ."),
             ("नदेत्र", "ए comes from अ + इ, not from ई + अ.")],
            "नदी + अत्र = नद्यत्र, like ताम्रवल्ली + अश्मन्तक = ताम्रवल्ल्यश्मन्तक.",
            "ई + a different vowel → य् + that vowel.",
            teaches="ई before a different vowel becomes य्: ताम्रवल्ली + अश्मन्तक → ताम्रवल्ल्यश्मन्तक."),
    ],
}

# ---------------------------------------------------------------- unit 25
AUTHORED["25"] = {
    "title": "विदार्यादिगणेन वा",
    "question": "By unit 25, what further option is named?",
    "rule": ("Or (वा) with the group (गण) beginning with vidārī (probably Pueraria tuberosa). Milk cooked with the group, "
             "as in unit 23, is understood."),
    "limits": ("Elliptical: the milk and the verb are understood, not printed. The members of the group are not named "
               "here. Vidārī's identification is only probable."),
    "explain_hi": ("तीन शब्दों की यह पंक्ति एक और विकल्प देती है: अथवा विदारी आदि गण से। "
                   "‘विदार्यादिगण’ यानी वह औषधि-समूह जो विदारी से आरम्भ होता है; उसके सदस्य यहाँ नहीं गिनाए गए। "
                   "इकाई २३ की तरह, इस गण के साथ पकाया दूध समझा जाता है, पर छपा नहीं। "
                   "विदारी सम्भवतः विदारीकन्द (Pueraria tuberosa) है। "
                   "‘विदार्यादि’ में विदारी + आदि है: ई + आ → या।"),
    "hook": "विदारी से आरम्भ होने वाला गण।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 25, which group is named?",
            ("The group beginning with vidārī", "विदार्यादिगणेन: with the vidārī-and-others group."),
            [("The group beginning with nyagrodha", "Nyagrodha and the others come in units 8 and 13."),
             ("The group of the three fruits", "No three fruits are named in unit 25."),
             ("The group of the five barks", "No barks are named in unit 25.")],
            "Unit 25 names the group that begins with vidārī.",
            "विदारी + आदि + गण."),
        order(1, "Put the parts of unit 25 in the line's order.",
              ["विदारी", "आदि", "गणेन", "वा"],
              "Vidārī, and the others, with the group, or.",
              "विदारी → आदि → गणेन → वा."),
        match(2, "Match each part of unit 25 to its meaning.",
              [["विदारी", "probably Pueraria tuberosa"], ["आदि", "and so on (beginning with)"], ["गण", "group"],
               ["वा", "or"]],
              "विदार्यादिगण = the group beginning with vidārī.",
              "विदारी, आदि, गण, वा.", role="extend",
              teaches="X-आदि-गण = the group beginning with X."),
        mcq("discriminate", 3, "Which split of विदार्यादि is right?",
            ("विदारी + आदि", "ई + आ → या: विदारी + आदि = विदार्यादि."),
            [("विदारा + आदि", "आ + आ would give विदारादि, with no य."),
             ("विदारु + आदि", "उ + आ would give विदार्वादि, with व."),
             ("विदारी + यादि", "यादि is not a word; the word is आदि.")],
            "विदारी (the drug) + आदि (and so on): ई + आ → या.",
            "ई + आ → या."),
        multi("apply", 4, "Which statements fit unit 25 and its data?",
              [("Milk cooked with the group is understood", "Right: as in unit 23, understood and not printed."),
               ("No verb is printed in the line", "Right: the line has no verb."),
               ("The group's members are named here", "The note: the members are not named here."),
               ("Vidārī is a certain identification", "Vidārī is probable (Pueraria tuberosa), not certain.")],
              [0, 1],
              "A verbless option: milk cooked with the vidārī group is understood.",
              "विदार्यादिगणेन वा."),
        mcq("transfer", 5, "By the rule of विदार्यादि, how is नदी + आगता (the river has come) joined?",
            ("नद्यागता", "ई + आ → या, as विदारी + आदि."),
            [("नदीगता", "The आ is not dropped after ई."),
             ("नद्यगता", "The आ stays long: ई + आ gives या, not य."),
             ("नदेगता", "ए comes from अ + इ, not from ई + आ.")],
            "नदी + आगता = नद्यागता, like विदारी + आदि = विदार्यादि.",
            "ई + आ → या.",
            teaches="ई before आ becomes य्, giving या: विदारी + आदि → विदार्यादि."),
    ],
}

# ---------------------------------------------------------------- unit 26
AUTHORED["26"] = {
    "title": "श्वदंष्ट्रास्वरसक्षीरसिद्धं वासर्पिः",
    "question": "By unit 26, what is cooked, and in what?",
    "rule": ("Or (वा) ghee (सर्पिः) cooked (सिद्ध) in the svarasa (expressed fresh juice) of śvadaṃṣṭrā (gokṣura, "
             "Tribulus terrestris; standard) and milk (क्षीर)."),
    "limits": ("The grouping (juice of śvadaṃṣṭrā and milk, or juice and milk of ...) is not decided; the plain reading "
               "is used: no question rests on it. No verb, amount or use is printed."),
    "explain_hi": ("यह पंक्ति एक नया योग देती है: श्वदंष्ट्रा यानी गोखरू (मानक पहचान) के स्वरस (निचोड़ा हुआ ताज़ा रस) और दूध "
                   "(क्षीर) में पकाया (सिद्ध) घी (सर्पिः)। "
                   "छपाई में ‘वा’ और ‘सर्पिः’ जुड़े हुए हैं (वासर्पिः)। "
                   "समास का समूह तय नहीं: ‘श्वदंष्ट्रा का रस और दूध’ या ‘श्वदंष्ट्रा का रस और उसी का दूध’; यहाँ सीधा पाठ लिया गया। "
                   "घी कितना और कैसे दिया जाए, यह नहीं बताया गया।"),
    "hook": "गोखरू का रस और दूध: इनमें सिद्ध घी।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 26, what is cooked in the juice and milk?",
            ("Ghee (सर्पिः)", "सिद्धं वा सर्पिः: ghee cooked in them."),
            [("Oil (तैल)", "No oil is named; the word is सर्पिः, ghee."),
             ("Gruel (यवागू)", "No gruel is named in unit 26."),
             ("Rice (ओदन)", "Rice-meal is unit 20, not 26.")],
            "Ghee is cooked in śvadaṃṣṭrā juice and milk.",
            "... क्षीरसिद्धं वा सर्पिः."),
        order(1, "Put the parts of unit 26 in the line's order.",
              ["श्वदंष्ट्रा", "स्वरस", "क्षीर", "सिद्धं", "वा", "सर्पिः"],
              "Śvadaṃṣṭrā, fresh juice, milk, cooked, or, ghee.",
              "श्वदंष्ट्रा → स्वरस → क्षीर → सिद्धं → वा → सर्पिः."),
        match(2, "Match each part of unit 26 to its meaning.",
              [["श्वदंष्ट्रा", "Tribulus terrestris, gokṣura (standard)"], ["स्वरस", "expressed fresh juice"],
               ["क्षीर", "milk"], ["सिद्ध", "cooked"], ["सर्पिस्", "ghee"]],
              "Ghee cooked in the fresh juice of śvadaṃṣṭrā and milk.",
              "श्वदंष्ट्रा, स्वरस, क्षीर, सिद्ध, सर्पिस्.", role="extend",
              teaches="स्वरस = expressed fresh juice."),
        mcq("discriminate", 3, "What does स्वरस mean in unit 26?",
            ("Fresh pressed juice", "The data: svarasa, expressed fresh juice."),
            [("A boiled decoction", "A decoction is क्वाथ; स्वरस is juice pressed out fresh."),
             ("A paste of the herb", "A paste is कल्क; स्वरस is juice."),
             ("A fine dry powder", "A powder is चूर्ण; स्वरस is juice.")],
            "स्वरस is the juice pressed out of the fresh plant.",
            "स्वरस = expressed fresh juice."),
        multi("apply", 4, "Which statements fit unit 26 and its data?",
              [("The data settles the grouping", "The note: the grouping is not decided."),
               ("The ghee is cooked in juice and milk", "Right: स्वरस-क्षीर-सिद्धं सर्पिः, the plain reading."),
               ("Śvadaṃṣṭrā is usually gokṣura", "Right: Tribulus terrestris, labelled standard."),
               ("वा and सर्पिः are run together in print", "Right: the print reads वासर्पिः.")],
              [1, 2, 3],
              "Ghee cooked in śvadaṃṣṭrā juice and milk; the grouping stays open.",
              "श्वदंष्ट्रास्वरसक्षीरसिद्धं वा सर्पिः."),
        mcq("transfer", 5, "By the sense of स्वरस, what is a new example आमलकस्वरसः?",
            ("Fresh juice of āmalaka", "आमलक + स्वरस: the expressed fresh juice of āmalaka."),
            [("A decoction of āmalaka", "A decoction is क्वाथ, not स्वरस."),
             ("Ghee cooked with āmalaka", "Cooked ghee would be आमलकसिद्धं सर्पिः."),
             ("Dry powder of āmalaka", "A powder is चूर्ण, not स्वरस.")],
            "आमलकस्वरसः = the fresh juice of āmalaka, like श्वदंष्ट्रास्वरस.",
            "X-स्वरस = the expressed fresh juice of X.",
            teaches="स्वरस = expressed fresh juice: X-स्वरस = the fresh juice of X."),
    ],
}

# ---------------------------------------------------------------- unit 27
AUTHORED["27"] = {
    "title": "पलांडुरससिद्धं वा सक्षौद्रं",
    "question": "By unit 27, in what juice is it cooked, and with what is it taken?",
    "rule": ("Or (वा) (that) cooked (सिद्ध) in the juice (रस) of palāṇḍu (onion, Allium cepa; standard), with honey "
             "(सक्षौद्र)."),
    "limits": ("Elliptical: what is cooked is not printed (the data notes the ghee of unit 26, but no noun is supplied). "
               "No amount or use is given; when the honey is added is not said."),
    "explain_hi": ("यह पंक्ति इकाई २६ के बाद एक और विकल्प देती है: अथवा पलाण्डु यानी प्याज (मानक पहचान) के रस में पकाया हुआ, "
                   "शहद के साथ (सक्षौद्र)। "
                   "क्या पकाया जाए, यह संज्ञा यहाँ छपी नहीं; डेटा का नोट इकाई २६ के घी की ओर संकेत करता है, पर कोई शब्द जोड़ता नहीं। "
                   "‘सक्षौद्रम्’ बहुव्रीहि है: स (सहित) + क्षौद्र (शहद), यानी शहद सहित। "
                   "मात्रा या प्रयोग-विधि नहीं दी गई।"),
    "hook": "प्याज के रस में सिद्ध, शहद के साथ।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 27, in whose juice is it cooked?",
            ("Onion (पलाण्डु)", "पलाण्डुरससिद्धम्: cooked in the juice of palāṇḍu, onion."),
            [("Garlic (लशुन)", "Garlic is not named; the word is पलाण्डु."),
             ("Lemon (जम्बीर)", "No lemon is named in unit 27."),
             ("Śvadaṃṣṭrā (गोक्षुर)", "Śvadaṃṣṭrā juice is unit 26, not 27.")],
            "It is cooked in onion juice.",
            "पलाण्डु + रस + सिद्ध."),
        order(1, "Put the parts of unit 27 in the line's order.",
              ["पलाण्डु", "रस", "सिद्धं", "वा", "सक्षौद्रं"],
              "Onion, juice, cooked, or, with honey.",
              "पलाण्डु → रस → सिद्धं → वा → सक्षौद्रं."),
        match(2, "Match each part of unit 27 to its meaning.",
              [["पलाण्डु", "onion (standard)"], ["रस", "juice"], ["सिद्ध", "cooked"], ["स-", "with"],
               ["क्षौद्र", "honey"]],
              "Cooked in onion juice, with honey.",
              "पलाण्डु, रस, सिद्ध, स-, क्षौद्र.", role="extend",
              teaches="स- = with: सक्षौद्र = with honey."),
        mcq("discriminate", 3, "What does स- add in सक्षौद्रं?",
            ("With, along with", "स + क्षौद्र, a bahuvrīhi: with honey."),
            [("Without, lacking", "'Without' would be निः- or अ-, not स-."),
             ("Very, too much", "'Very' would be अति-, not स-."),
             ("Good, well made", "'Good' would be सु-, not स-.")],
            "स- = with: सक्षौद्रम् = with honey.",
            "स- (bahuvrīhi) = with."),
        mcq("apply", 4, "Which noun does unit 27 itself print as the thing cooked?",
            ("None: no noun is printed", "The note: what is cooked is not stated; no noun is supplied."),
            [("Ghee, printed in the line", "Ghee is pointed to from unit 26; it is not printed here."),
             ("Milk, printed in the line", "No milk is printed in unit 27."),
             ("Oil, printed in the line", "No oil is printed in unit 27.")],
            "Unit 27 prints no noun for what is cooked.",
            "पलाण्डुरससिद्धं (noun not printed)."),
        mcq("transfer", 5, "By the rule of सक्षौद्रं, what does a new example सलवणं भोजनम् mean?",
            ("Food with salt", "स + लवण: with salt, as स + क्षौद्र."),
            [("Food without salt", "Without salt would be अलवण or निर्लवण."),
             ("Food that is very salty", "Very salty would need अति-, not स-."),
             ("Salt instead of food", "स- adds 'with'; it does not replace.")],
            "सलवणं भोजनम् = food with salt, like सक्षौद्रम् = with honey.",
            "स- (bahuvrīhi) = with.",
            teaches="स- in a bahuvrīhi means 'with': स + क्षौद्र → सक्षौद्र, with honey."),
    ],
}


# ===================================================================== NOTES_HI
NOTES_HI = {
    "15": ("गद्य-पंक्ति; विश्वास मध्यम; कोई पाठ-चिह्न नहीं। क्रिया (पाययेत्) इकाई १४ से चली आती है। वृद्धि की पहचान "
           "विवादित; विदारी सम्भावित (Ipomoea digitata भी कही जाती है)। छपा ‘जीवंती’ = जीवन्ती (अनुस्वार वर्ग-नासिक्य के स्थान पर)। "
           "सन्धि जाँची: जीवन्तीः + वा → जीवन्तीर्वा (ई के बाद विसर्ग, घोष वर्ण से पहले → र्); छपाई में ‘वापयसा’ जुड़ा है = वा पयसा।"),
    "16": ("विश्वास निम्न। दो छपे रूप अस्पष्ट (अपठनीय): ‘पक्लोष्ट’ (पाठ-चिह्न: पक्व-लोष्ट केवल अनुमान) और ‘सरसान्यसरेण’; "
           "इन पर कुछ नहीं बनाया गया। ‘सिता’ दो तरह: मिश्री या ‘श्वेत’; इस पर प्रश्न नहीं। क्रिया इकाई १४ से, जोड़ी नहीं गई। "
           "छपे ‘चंदन’, ‘तंडुलांबु’ = चन्दन, तण्डुलाम्बु। सन्धि जाँची: नील + उत्पल → नीलोत्पल (अ + उ → ओ); चन्दन + आदि → "
           "चन्दनादि (अ + आ → आ); तण्डुल + अम्बु → तण्डुलाम्बु (अ + अ → आ)।"),
    "17": ("विश्वास मध्यम। पाठ-चिह्न: ‘शलादुन्ग्रोध’ → सम्भवतः शलाडु-न्यग्रोध (न्य को ङ् पढ़ा गया; दन्त्य द भी छपाई-भूल); इसलिए "
           "बरगद पर प्रश्न नहीं। समूह अनिश्चित: गन्ध-प्रियंगु एक नाम हो सकता है; असित-उत्पल अलग भी; उदुम्बर-शलाडु मान लिया गया। "
           "छपा ‘उडुंबर’ = उदुम्बर/उडुम्बर, ‘शृंगानि’ = शृङ्गाणि (छपाई में दन्त्य न)। सन्धि जाँची: प्रियङ्गु + असित → प्रियङ्ग्वसित "
           "(उ + अ → व); असित + उत्पल → असितोत्पल; शालूक + उडुम्बर → शालूकोडुम्बर (अ + उ → ओ); वा + आजेन → वाऽऽजेन "
           "(आ + आ → आ; ‘ऽऽ’ छपाई का चिह्न)।"),
    "18": ("विश्वास मध्यम। पाठ-चिह्न: ‘काथेन’ → सम्भवतः क्वाथेन (व छूटा, जैसे इकाई ३२ में); ‘सारिवामप्रोंडरीक’ → सारिवा-पुण्डरीक, "
           "‘म’ अक्षर अस्पष्ट (प्रो = पु)। इन पर प्रश्न नहीं। अनन्त विवादित (सारिवा का नाम या अलग द्रव्य); ‘कन्द-बीज’ का विस्तार "
           "अनिश्चित। छपा ‘कसेरुक’ = कशेरुक। सन्धि जाँची: पुण्डरीक + अनन्त → पुण्डरीकानन्त (अ + अ → आ); अनन्त + उत्पल → "
           "अनन्तोत्पल (अ + उ → ओ); मधुर + एन → मधुरेण (र के बाद केवल स्वर, न → ण)।"),
    "19": ("विश्वास मध्यम; कोई पाठ-चिह्न नहीं। अर्थ दो तरह: तीनों नपुंसक शब्द एक ही वस्तु (शालिचूर्ण या जीवनीय से बना दूध) या दो "
           "अलग वस्तुएँ; शाब्दिक दो-वस्तु पाठ लिया गया, इस पर प्रश्न नहीं। जीवनीय गण का नाम मानक है; सदस्य इस पंक्ति में नहीं। "
           "क्रिया पिछली इकाइयों से। छपे ‘पिष्टं’, ‘शृतं’, ‘क्षीरं’ में अन्तिम म् अनुस्वार से लिखा है।"),
    "20": ("विश्वास मध्यम। पाठ-चिह्न: ‘केशु’ → इक्षु (षष्टिक + इक्षुमूल → षष्टिकेक्षुमूल; क्ष/श भ्रम), ‘भृतेन’ → शृतेन; दोनों अनुमान, "
           "इन पर प्रश्न नहीं (‘भृत’ = भरा/तैयार भी)। ‘इक्षु-मूल’ दो वस्तुएँ भी हो सकती हैं। सन्धि जाँची: बला + अतिबला → बलाऽतिबला "
           "(आ + अ → आ; ऽ छपाई का चिह्न); शालि + ओदनम् → शाल्योदनम् (इ + ओ → यो); भोजयेत् + शीत → भोजयेच्छीत (त् + श → च्छ)।"),
    "21": ("विश्वास मध्यम; कोई पाठ-चिह्न नहीं। छपाई में ‘शोधनवर्ज्याः’ और ‘प्रयुंजीत’ जुड़े हैं। रक्तपित्त = रक्तस्राव का विकार "
           "(सम्भावित आधुनिक समकक्ष)। ‘वर्ज्याः’ क्रियाः से मेल खाता है। सन्धि जाँची: क्रियाः + च → क्रियाश्च (विसर्ग, च से पहले → श्); "
           "वर्ज्याः + प्रयुञ्जीत: प से पहले विसर्ग बना रहता है।"),
    "22": ("विश्वास उच्च; कोई पाठ-चिह्न नहीं। क्रिया (प्रयुञ्जीत) इकाई २१ से समझी जाती है, जोड़ी नहीं गई। ‘सौम्य’ = कोमल, चन्द्र-सम्बन्धी "
           "‘शीतल’ भी। सन्धि जाँची: सौम्याः + च → सौम्याश्च (विसर्ग, च से पहले → श्); मनः + अनुकूलाः → मनोऽनुकूलाः (अः + अ → ओऽ)।"),
    "23": ("विश्वास मध्यम; कोई पाठ-चिह्न नहीं। पयस्या विवादित (प्रायः क्षीरविदारी); असुरदारु अज्ञात, देवदारु से न मिलाएँ; ‘अमरदारु’ "
           "अलग पाठ होगा, अपनाया नहीं गया; ‘दारु’ अलग शब्द भी हो सकता है। व्याकरण से ‘पयस्या + सुरदारु’ विच्छेद भी बनता है; डेटा इसे "
           "नहीं अपनाता, इसलिए इस समास के विच्छेद पर कोई प्रश्न नहीं। सन्धि जाँची: अदृष्टशोणिताम् + तु → अदृष्टशोणितां तु "
           "(व्यञ्जन से पहले म् → ं)।"),
    "24": ("विश्वास मध्यम; कोई पाठ-चिह्न नहीं। दूध और क्रिया इकाई २३ से समझे जाते हैं, छपे नहीं। ताम्रवल्ली अज्ञात; अश्मन्तक "
           "विवादित (प्रायः आपटा); पयस्या विवादित; शतावरी मानक। सन्धि जाँची: ताम्रवल्ली + अश्मन्तक → ताम्रवल्ल्यश्मन्तक "
           "(ई + अ → य); पयस्याभिः + वा → पयस्याभिर्वा (इ के बाद विसर्ग, घोष वर्ण से पहले → र्)।"),
    "25": ("विश्वास उच्च; कोई पाठ-चिह्न नहीं। इकाई २३ की तरह गण से पकाया दूध समझा जाता है, छपा नहीं। गण के सदस्य यहाँ नहीं "
           "गिनाए गए। विदारी सम्भावित। सन्धि जाँची: विदारी + आदि → विदार्यादि (ई + आ → या)।"),
    "26": ("विश्वास उच्च; कोई पाठ-चिह्न नहीं। छपाई में ‘वा’ और ‘सर्पिः’ जुड़े हैं (वासर्पिः)। समूह तय नहीं (श्वदंष्ट्रा का रस और "
           "दूध, या रस और उसी का दूध); सीधा पाठ लिया गया, इस पर प्रश्न नहीं। श्वदंष्ट्रा प्रायः गोक्षुर (मानक); यह नाम दूसरे पौधों "
           "के लिए भी आता है। छपा ‘श्वदंष्ट्रा’ में अनुस्वार। समास में सन्धि: श्वदंष्ट्रा + स्वरस, कोई स्वर-सन्धि नहीं।"),
    "27": ("विश्वास मध्यम; कोई पाठ-चिह्न नहीं। क्या पकाया जाए, यह छपा नहीं (नोट इकाई २६ के घी की ओर संकेत करता है), कोई संज्ञा जोड़ी "
           "नहीं गई। छपा ‘पलांडु’ = पलाण्डु। सन्धि जाँची: सिद्धम् + वा → सिद्धं वा (व्यञ्जन से पहले म् → ं); सक्षौद्रं अन्त में छपाई "
           "की आदत से अनुस्वार।"),
}


# ===================================================================== AIDS
AIDS = {
    "15": {
        "diagram": {"groups": [
            {"label": "द्रव्य (क्रम से)", "items": ["वृद्धि: पहचान विवादित", "विदारी: विदारीकन्द (सम्भावित)",
                                                 "जीवन्ती: डोडी (मानक)"]},
            {"label": "साथ में", "items": ["पयसा: दूध के साथ"]}]},
        "sandhi": "ई के बाद विसर्ग, घोष वर्ण से पहले → र्: जीवन्तीः + वा → जीवन्तीर्वा।",
        "frame": "क्या: वृद्धि-विदारी-जीवन्तीः (कर्म) → किसके साथ: पयसा (दूध) → क्रिया: इकाई १४ से (पाययेत्, पिलाए)।",
    },
    "16": {
        "chunks": "नीलोत्पलसितापक्लोष्टचंदनादि | वा तंडुलांबु | वा सरसान्यसरेण",
        "sandhi": "अ + उ → ओ: नील + उत्पल → नीलोत्पल · अ + आ → आ: चन्दन + आदि → चन्दनादि · अ + अ → आ: तण्डुल + अम्बु → तण्डुलाम्बु।",
        "frame": "विकल्प १: नीलोत्पल, सिता, (अस्पष्ट), चन्दन आदि → वा → विकल्प २: तण्डुलाम्बु (चावल का पानी) → वा → विकल्प ३: अस्पष्ट रूप।",
    },
    "17": {
        "diagram": {"groups": [
            {"label": "समास के द्रव्य (क्रम से)", "items": ["गन्ध: अनिर्दिष्ट सुगन्धित द्रव्य", "प्रियंगु (सम्भावित)",
                                                         "असित उत्पल: काला उत्पल", "शालूक: कमल-कन्द (सम्भावित)",
                                                         "उदुम्बर: गूलर (मानक) के कच्चे फल",
                                                         "शृंग: अंकुर (किसके, यह अनुमानित पाठ पर)"]},
            {"label": "अथवा", "items": ["आजेन पयसा: बकरी के दूध से"]}]},
        "sandhi": "उ + अ → व: प्रियङ्गु + असित → प्रियङ्ग्वसित · अ + उ → ओ: शालूक + उडुम्बर → शालूकोडुम्बर · आ + आ → आ: वा + आजेन → वाऽऽजेन।",
        "chunks": "गंधप्रियंग्वसितोत्पल | शालूकोडुंबरशलादु | न्ग्रोधशृंगानि | वाऽऽजेन पयसा",
    },
    "18": {
        "diagram": {"groups": [
            {"label": "द्रव्य (क्रम से)", "items": ["कसेरुक: कसेरू (सम्भावित)", "मृणाल: कमलनाल", "शृंगाटक: सिंघाड़ा (मानक)",
                                                 "काश्मर्य: गम्भारी (मानक)", "परूषक: फालसा (मानक)",
                                                 "द्राक्षा: अंगूर या मुनक्का (मानक)", "सारिवा: अनन्तमूल (मानक)",
                                                 "म: अस्पष्ट अक्षर", "पुण्डरीक: श्वेत कमल (सम्भावित, अनुमानित पाठ)",
                                                 "अनन्त: पहचान विवादित", "उत्पल, कन्द, बीज"]},
            {"label": "द्रव और मिठास", "items": ["क्वाथ: काढ़ा (सम्भावित सुधार)", "शर्करा और शहद से मीठा"]}]},
        "sandhi": "र के बाद केवल स्वर हो तो न → ण: मधुर + एन → मधुरेण · अ + उ → ओ: अनन्त + उत्पल → अनन्तोत्पल।",
        "letters": "पहले छह द्रव्यों के पहले अक्षर क्रम से: क-मृ-शृ-का-प-द्रा (कसेरुक, मृणाल, शृंगाटक, काश्मर्य, परूषक, द्राक्षा)। (मेरी याद-पद्धति)",
    },
    "19": {
        "chunks": "शालिपिष्टं | जीवनीयशृतं वा क्षीरं",
        "frame": "विकल्प १: शालिपिष्टम् (शालि का चूर्ण) → वा → विकल्प २: जीवनीयशृतं क्षीरम् (जीवनीय से उबला दूध); क्रिया पीछे से।",
        "anchors": "याद-सूत्र: ‘शृत’ = उबला; ‘X-शृत क्षीर’ = X से उबला दूध। (मेरी याद-पद्धति)",
    },
    "20": {
        "diagram": {"groups": [
            {"label": "दूध किनसे तैयार (क्रम से)", "items": ["बला (मानक)", "अतिबला (सम्भावित)", "शालि, षष्टिक",
                                                          "ईख-मूल (अनुमानित पाठ)", "काकोली (विवादित)"]},
            {"label": "भोजन", "items": ["दूध, शहद-शर्करा सहित", "सुशीत लाल शालि-भात खिलाए",
                                       "अथवा शीतवीर्य जाङ्गल रस के साथ"]}]},
        "sandhi": "त् + श → च्छ: भोजयेत् + शीत → भोजयेच्छीत · इ + ओ → यो: शालि + ओदनम् → शाल्योदनम्।",
        "chunks": "बलाऽतिबलाशालिषष्टिकेशुमूलकाकोलीभृतेन च पयसा | समधुशर्करेण | रक्तशाल्योदनं सुशीतं भोजयेत् | शीतवीर्यजांगलरसेन वा",
        "frame": "क्रिया: भोजयेत् (खिलाए) → क्या: रक्तशाल्योदनं सुशीतम् → किसके साथ: औषध-दूध और शहद-शर्करा, अथवा शीतवीर्य जाङ्गल रस।",
    },
    "21": {
        "frame": "कर्म: रक्तपित्तक्रियाः → विशेषण: शोधनवर्ज्याः (शोधन छोड़कर) → क्रिया: प्रयुञ्जीत (प्रयोग करे)।",
        "seesaw": "प्रयुञ्जीत (प्रयोग करे): रक्तपित्त की क्रियाएँ ↔ वर्ज्य (छोड़ दे): शोधन वाली क्रियाएँ।",
        "sandhi": "विसर्ग, च से पहले → श्: क्रियाः + च → क्रियाश्च।",
    },
    "22": {
        "chunks": "सौम्याश्च | मनोऽनुकूलाः | कथाः",
        "sandhi": "विसर्ग, च से पहले → श्: सौम्याः + च → सौम्याश्च · अः + अ → ओऽ: मनः + अनुकूलाः → मनोऽनुकूलाः।",
        "anchors": "याद-सूत्र: इकाई २१ की क्रिया ‘प्रयुञ्जीत’ यहाँ भी: दवा की क्रियाओं के साथ सौम्य, मन भाती कथाएँ। (मेरी याद-पद्धति)",
    },
    "23": {
        "chain": {"steps": ["अदृष्टशोणिता: जिसमें रक्त न दिखे", "मधुक, पयस्या (विवादित), असुरदारु (अज्ञात)",
                            "इनसे सिद्ध (पकाया) दूध", "पाययेत्: पिलाए"]},
        "sandhi": "व्यञ्जन से पहले म् → ं: अदृष्टशोणिताम् + तु → अदृष्टशोणितां तु, सिद्धम् + पयः → सिद्धं पयः। (पयस्यासुर... का विच्छेद दो तरह बन सकता है, इसलिए यहाँ नहीं।)",
        "frame": "किसके लिए: अदृष्टशोणिताम् (कर्म) → किनसे: मधुक-पयस्या-असुरदारुभिः → क्या: सिद्धं पयः → क्रिया: पाययेत्।",
    },
    "24": {
        "diagram": {"groups": [
            {"label": "द्रव्य (क्रम से)", "items": ["ताम्रवल्ली: अज्ञात", "अश्मन्तक: प्रायः आपटा (विवादित)",
                                                 "शतावरी (मानक)", "पयस्या: पहचान विवादित"]},
            {"label": "समझा गया", "items": ["इनसे सिद्ध दूध (इकाई २३ से)"]}]},
        "sandhi": "ई + अ → य: ताम्रवल्ली + अश्मन्तक → ताम्रवल्ल्यश्मन्तक · इ के बाद विसर्ग, घोष वर्ण से पहले → र्: पयस्याभिः + वा → पयस्याभिर्वा।",
        "chunks": "ताम्रवल्ल्यश्मंतक | शतावरीपयस्याभिर्वा",
    },
    "25": {
        "frame": "किससे: विदार्यादिगणेन (विदारी से आरम्भ होने वाले गण से) → वा → समझा गया: सिद्ध दूध (इकाई २३ से)।",
        "sandhi": "ई + आ → या: विदारी + आदि → विदार्यादि।",
        "anchors": "याद-सूत्र: ‘X-आदि-गण’ = X से आरम्भ होने वाला गण; सदस्य यहाँ नहीं गिनाए। (मेरी याद-पद्धति)",
    },
    "26": {
        "chain": {"steps": ["श्वदंष्ट्रा (गोखरू, मानक) का स्वरस", "और क्षीर (दूध)", "इनमें सिद्ध (पकाया)", "सर्पिः (घी)"]},
        "chunks": "श्वदंष्ट्रास्वरसक्षीरसिद्धं | वासर्पिः",
        "frame": "किसमें: श्वदंष्ट्रा-स्वरस और क्षीर → क्या: सिद्धं सर्पिः (पकाया घी) → वा (अथवा)।",
    },
    "27": {
        "chunks": "पलांडुरससिद्धं वा | सक्षौद्रं",
        "frame": "किसमें: पलाण्डु-रस (प्याज का रस) → सिद्धम् (पकाया; क्या, यह छपा नहीं) → सक्षौद्रम् (शहद सहित)।",
        "anchors": "याद-सूत्र: ‘स-’ = सहित: सक्षौद्र = शहद सहित, सघृत = घी सहित। (मेरी याद-पद्धति)",
    },
}


# ===================================================================== IMAGE_SPECS
IMAGE_SPECS = {
    ("15", "diagram"): {
        "file": "sh4-vriddhi-vidari-15.svg",
        "alt": ("Table of unit 15 in line order with the data's labels: vṛddhi (identity disputed), vidārī (probably "
                "Indian kudzu), jīvantī (standard), then 'with milk'."),
        "type": "table",
        "title": "इकाई १५: तीन द्रव्य, दूध के साथ",
        "heads": ["छपा शब्द (क्रम से)", "पहचान / अर्थ"],
        "rows": [["वृद्धि", "पहचान विवादित"], ["विदारी", "विदारीकन्द (सम्भावित)"], ["जीवन्ती", "डोडी (मानक)"],
                 ["वा पयसा", "अथवा दूध के साथ"]],
    },
    ("17", "diagram"): {
        "file": "sh4-priyangu-aja-17.svg",
        "alt": ("Table of unit 17 in line order: gandha (unspecific fragrant substance), priyaṅgu (probable), dark utpala, "
                "śālūka water-lily rhizome (probable), unripe fruit of udumbara cluster fig (standard), shoots (whose, "
                "only on a conjectural reading), then 'or with goat's milk'."),
        "type": "table",
        "title": "इकाई १७: द्रव्य और बकरी का दूध",
        "heads": ["छपा शब्द (क्रम से)", "पहचान / अर्थ"],
        "rows": [["गंध", "अनिर्दिष्ट सुगन्धित द्रव्य"], ["प्रियंगु", "फूलप्रियंगु (सम्भावित)"],
                 ["असितोत्पल", "काला उत्पल"], ["शालूक", "कमल-कन्द (सम्भावित)"],
                 ["उडुंबर-शलादु", "गूलर (मानक) के कच्चे फल"], ["...शृंगानि", "अंकुर (अनुमानित पाठ पर)"],
                 ["वाऽऽजेन पयसा", "अथवा बकरी के दूध से"]],
    },
    ("18", "diagram"): {
        "file": "sh4-kaseruka-kvatha-18.svg",
        "alt": ("Table of unit 18 in line order with the data's labels: kaseruka (probable), lotus stalk, water chestnut "
                "(standard), kāśmarya (standard), phalsa (standard), grape or raisin (standard), sārivā (standard), an "
                "unclear syllable, puṇḍarīka (probable, conjectural reading), ananta (disputed), utpala, tuber and seed; "
                "decoction (possible correction), sweet with sugar and honey."),
        "type": "table",
        "title": "इकाई १८: क्वाथ के द्रव्य",
        "heads": ["द्रव्य (क्रम से)", "पहचान"],
        "rows": [["कसेरुक", "कसेरू (सम्भावित)"], ["मृणाल", "कमलनाल"], ["शृंगाटक", "सिंघाड़ा (मानक)"],
                 ["काश्मर्य", "गम्भारी (मानक)"], ["परूषक", "फालसा (मानक)"], ["द्राक्षा", "अंगूर या मुनक्का (मानक)"],
                 ["सारिवा", "अनन्तमूल (मानक)"], ["म", "अस्पष्ट अक्षर"], ["पुण्डरीक", "श्वेत कमल (सम्भावित, अनुमानित पाठ)"],
                 ["अनन्त", "पहचान विवादित"], ["उत्पल, कन्द, बीज", "उत्पल; कन्द; बीज"],
                 ["काथेन", "क्वाथ से (सम्भावित सुधार)"], ["शर्करामधुमधुरेण", "शर्करा और शहद से मीठा"]],
    },
    ("20", "diagram"): {
        "file": "sh4-raktashali-odana-20.svg",
        "alt": ("Flowchart of unit 20: balā (standard), atibalā (probable), śāli and ṣaṣṭika, sugarcane root (conjectural "
                "reading) and kākolī (disputed) prepare the milk; milk with honey and sugar, or broth of dry-land game "
                "cool in potency, go with the very cool red śāli rice-meal that one should feed."),
        "type": "mermaid",
        "code": ("flowchart TD\n"
                 "  L1[\"बला (मानक)\"] --> A\n"
                 "  L2[\"अतिबला (सम्भावित)\"] --> A\n"
                 "  L3[\"शालि, षष्टिक\"] --> A\n"
                 "  L4[\"ईख-मूल (अनुमानित पाठ)\"] --> A\n"
                 "  L5[\"काकोली (विवादित)\"] --> A\n"
                 "  A[\"इनसे तैयार दूध\"] --> M[\"शहद और शर्करा सहित\"]\n"
                 "  M -->|\"के साथ\"| F[\"सुशीत लाल शालि-भात खिलाए\"]\n"
                 "  B[\"अथवा शीतवीर्य जाङ्गल रस\"] -->|\"के साथ\"| F\n"),
    },
    ("23", "chain"): {
        "file": "sh4-adrishta-shonita-23.svg",
        "alt": ("Chain of unit 23: for her in whom blood is not seen; madhuka, payasyā (disputed) and asura-dāru "
                "(unidentified); milk cooked with these; make her drink it."),
        "type": "chain",
        "title": "इकाई २३: रक्त न दिखे तो सिद्ध दूध",
        "steps": ["जिसमें रक्त न दिखे", "मधुक, पयस्या (विवादित), असुरदारु (अज्ञात)", "इनसे सिद्ध (पकाया) दूध",
                  "पाययेत्: पिलाए"],
    },
    ("24", "diagram"): {
        "file": "sh4-tamravalli-shatavari-24.svg",
        "alt": ("Table of unit 24 in line order with the data's labels: tāmravallī (unidentified), aśmantaka (usually "
                "Bauhinia racemosa, disputed), śatāvarī (standard), payasyā (disputed); milk cooked with these is "
                "understood from unit 23."),
        "type": "table",
        "title": "इकाई २४: चार द्रव्य",
        "heads": ["द्रव्य (क्रम से)", "पहचान"],
        "rows": [["ताम्रवल्ली", "अज्ञात"], ["अश्मन्तक", "प्रायः आपटा (विवादित)"], ["शतावरी", "शतावरी (मानक)"],
                 ["पयस्या", "पहचान विवादित"], ["समझा गया", "इनसे सिद्ध दूध (इकाई २३ से)"]],
    },
    ("26", "chain"): {
        "file": "sh4-shvadamshtra-sarpis-26.svg",
        "alt": ("Chain of unit 26: the fresh juice of śvadaṃṣṭrā (gokṣura, standard) and milk; cooked in these; ghee."),
        "type": "chain",
        "title": "इकाई २६: गोखरू-रस और दूध में सिद्ध घी",
        "steps": ["श्वदंष्ट्रा (गोखरू, मानक) का स्वरस", "और क्षीर (दूध)", "इनमें सिद्ध (पकाया)", "सर्पिः (घी)"],
    },
}
