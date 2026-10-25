from helpers import mcq, match, order, fill, multi, accepts

# Kalpasthāna chapter 4 (Bastikalpa), units 12-24.
# Sections (sections_kalpa.py KA4): 12-17 madhuyaṣṭī-milk basti (burning); 18-20 kośātakyādi nirūha (Kapha);
# 21-24 punarnavādi nirūha (the list starts in line 05.04.39 of unit 20; verb in line 05.04.46).

AUTHORED = {}

# ---------------------------------------------------------------- unit 12
AUTHORED["12"] = {
    "title": "चतुष्पले तैल घृतस्य",
    "question": "What can be read with confidence in the damaged verse 12, a sour liquid made from goat?",
    "rule": ("On a conjectural reading: from goat fried in four palas of oil and ghee, made sour with śatāhvā, curd and "
             "pomegranate, a liquid (rasa) with things to be ground, good for strength, complexion, flesh, semen and digestive fire."),
    "limits": ("Both lines are damaged (तैल, the word with भृष्टः, and हितैः, मिर्ष, शिरोरुजी), so the translation is conjectural; "
               "questions keep to clear words. चतुष्पले is a locative dvigu, 'in four palas'. The use of the liquid is not stated."),
    "explain_hi": ("यह श्लोक छपाई में बहुत बिगड़ा है, इसलिए इसका पूरा अर्थ अनुमान पर टिका है। "
                   "पहली पंक्ति में लगता है कि चार पल तेल और घी में भुने बकरे से, शताह्वा यानी सम्भवतः सोआ, दही और दाड़िम यानी अनार से खट्टा किया रस बनता है। "
                   "दूसरी पंक्ति में यह रस ‘सपेष्य’ (स- = साथ, पेष्य = पीसने योग्य) यानी पीसने योग्य द्रव्यों के साथ है, और अनुमान से बल, वर्ण, मांस, रेतस् यानी वीर्य और अग्नि यानी पाचन-अग्नि के लिए हितकर कहा गया है। "
                   "‘मिर्ष’ पढ़ा नहीं जाता; अन्त का भाग सम्भवतः सिर के दर्द वाले के लिए ‘इष्ट’ बताता है। "
                   "‘चतुष्पले’ द्विगु समास, सप्तमी है: चार पल के माप में।"),
    "hook": "चार पल तेल-घी, बकरा, दही-अनार की खटास: बल-वर्ण-मांस-रेतस्-अग्नि का रस (पाठ अनुमानित)।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "Which measure does चतुष्पले in verse 12 name?",
            ("Four palas",
             "चतुष्पले: in a measure of four palas (catuḥ + pala)."),
            [("Eight palas", "चतुष् means four, not eight."),
             ("Half a tulā", "No tulā is named in verse 12."),
             ("Two āḍhakas", "No āḍhaka is named in verse 12.")],
            "चतुष्पले तैल घृतस्य: in four palas of oil and of ghee.",
            "चतुष्पले = in four palas."),
        match(1, "Match each clear word of verse 12 to its meaning.",
              [["चतुष्पले", "in four palas"], ["घृतस्य", "of ghee"], ["रसः", "liquid (rasa)"],
               ["सपेष्यः", "with what is to be ground"], ["बलवर्ण", "strength and complexion"]],
              "These words are clear even though the verse around them is damaged.",
              "चतुष्पले = in four palas; घृतस्य = of ghee; रसः = liquid; सपेष्यः = with things to grind; बलवर्ण = strength and complexion."),
        order(2, "Put these clear words of verse 12 in the printed order.",
              ["चतुष्पले", "घृतस्य", "रसः", "सपेष्यो", "बलवर्ण"],
              "The clear words run: in four palas, of ghee, the liquid, with things to grind, strength-complexion.",
              "चतुष्पले · घृतस्य · रसः · सपेष्यो · बलवर्ण.",
              role="extend",
              teaches="Verse 12's clear words: the measure (चतुष्पले) and ghee in line 1; रसः सपेष्यः and बलवर्ण open line 2."),
        mcq("discriminate", 3, "Why does सपेष्यो in verse 12 end in -ओ?",
            ("-अः before voiced ब → -ओ",
             "सपेष्यः + बलवर्ण: -अः before a voiced consonant becomes -ओ."),
            [("It is the neuter singular ending", "सपेष्य agrees with masculine रसः; -ओ is not a neuter ending."),
             ("It is a dual ending, like -औ", "-ओ is not a dual ending; रसः is singular."),
             ("It is a vocative of address", "No one is addressed; the word qualifies रसः.")],
            "सपेष्यः (m. nom. sg.) before the voiced ब of बलवर्ण is written सपेष्यो.",
            "-अः + voiced consonant → -ओ."),
        mcq("apply", 4, "In सपेष्यः of verse 12, what does the prefix स- add?",
            ("together with",
             "स- = with: सपेष्यः, together with what is to be ground."),
            [("without, lacking", "That would be निः- or अ-, not स-."),
             ("very, well", "That is सु-, as in सुशीत."),
             ("not at all", "That is न or अ-, not स-.")],
            "स-पेष्यः: the liquid together with what is to be ground.",
            "स- (prefix) = together with."),
        mcq("transfer", 5, "Like चतुष्पले 'in four palas', which invented form means in a measure of two palas?",
            ("द्विपले",
             "द्वि + पल as a dvigu compound, locative singular -ए, like चतुष्पले."),
            [("द्विपलेन", "Instrumental: 'with two palas', not 'in'."),
             ("द्विपलात्", "Ablative: 'from two palas'."),
             ("द्विपलस्य", "Genitive: 'of two palas'.")],
            "Number + पल forms a dvigu; the locative -ए gives 'in a measure of ... palas'.",
            "Dvigu + locative -ए = 'in a measure of N palas'.",
            teaches="A number joined with पल makes a dvigu compound; in the locative (-ए) it means 'in a measure of N palas' (चतुष्पले, द्विपले)."),
    ],
}

# ---------------------------------------------------------------- unit 13
AUTHORED["13"] = {
    "title": "यष्ट्याह्वयस्याष्टपलेन सिद्धं पयः",
    "question": "What milk preparation does verse 13 describe, and in which diseases is the nirūha beneficial?",
    "rule": ("Milk cooked with eight palas of liquorice (yaṣṭyāhvaya), with śatāhvā fruit and pippalī, joined with ghee and honey: "
             "a nirūha beneficial in vātarakta (gout-type), visarpa (erysipelas) and vaisvarya (hoarseness)."),
    "limits": ("शताह्वाफलपिप्पलीभिः may be three items or 'śatāhvā fruit and pippalī', and its print is flagged; no question rests on it. "
               "Śatāhvā is probably dill. Only the liquorice has a measure. युक्तं (neuter) agrees with the milk, not with the masculine निरूहः."),
    "explain_hi": ("यह नया नुस्खा है: आठ पल यष्ट्याह्वय यानी मुलेठी के साथ दूध पकाया जाता है, साथ में शताह्वा यानी सम्भवतः सोआ का फल और पिप्पली यानी पीपर। "
                   "यह दूध घी और शहद से युक्त किया जाता है। "
                   "ऐसा निरूह यानी काढ़े की बस्ति वातरक्त यानी गठिया जैसे रोग, विसर्प यानी फैलने वाले त्वचा-संक्रमण और वैस्वर्य यानी स्वर बिगड़ने में हितकर है। "
                   "‘युक्तं’ नपुंसक है, इसलिए वह ‘पयः’ (दूध) से मेल खाता है, पुल्लिंग ‘निरूहः’ से नहीं।"),
    "hook": "आठ पल मुलेठी में दूध, घी-शहद मिलाओ: गठिया, विसर्प, बैठा गला।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "What is cooked with eight palas of liquorice in verse 13?",
            ("Milk (पयः)",
             "सिद्धं पयः: milk cooked with eight palas of yaṣṭyāhvaya."),
            [("Water (जल)", "No water is named in verse 13."),
             ("Oil (तैल)", "No oil is named in verse 13."),
             ("Goat broth", "No meat is named in verse 13.")],
            "यष्ट्याह्वयस्याष्टपलेन सिद्धं पयः: milk cooked with eight palas of liquorice.",
            "पयः = milk; सिद्ध = cooked."),
        match(1, "Match each word of verse 13 to its meaning as the card gives it.",
              [["वातरक्त", "gout-type disease"], ["विसर्प", "erysipelas"], ["वैस्वर्य", "hoarseness"],
               ["यष्ट्याह्वय", "liquorice"], ["ससर्पिर्मधु", "with ghee and honey"]],
              "The three disease names are standard renderings in the data; yaṣṭyāhvaya is 'the one named yaṣṭi', liquorice.",
              "वातरक्त = gout-type; विसर्प = erysipelas; वैस्वर्य = hoarseness; यष्ट्याह्वय = liquorice."),
        order(2, "Put these phrases of verse 13 in the verse's order.",
              ["यष्ट्याह्वयस्याष्टपलेन", "सिद्धं पयः", "युक्तं ससर्पिर्मधु", "वातरक्तविसर्पवैस्वर्यहितो", "निरूहः"],
              "Measure and drug, the cooked milk, its additions, the diseases, and last the name nirūha.",
              "यष्ट्याह्वयस्याष्टपलेन · सिद्धं पयः · युक्तं ससर्पिर्मधु · …हितो · निरूहः.",
              role="extend",
              teaches="Verse 13 runs: liquorice measure, cooked milk, joined with ghee and honey, beneficial in three diseases, nirūha."),
        mcq("discriminate", 3, "Which is the right split of यष्ट्याह्वयस्याष्टपलेन in verse 13?",
            ("यष्ट्याह्वयस्य + अष्टपलेन",
             "अ + अ → आ: …स्य + अष्ट… = …स्याष्ट…."),
            [("यष्ट्याह्वयस्याः + अष्टपलेन", "-आः before a vowel drops the visarga and does not join."),
             ("यष्ट्याह्वयस्यम् + अष्टपलेन", "म् before a vowel stays: it would read …स्यमष्ट…."),
             ("यष्ट्याह्वयः + स्याष्टपलेन", "स्याष्टपल is no word; the measure is अष्टपल, eight palas.")],
            "Genitive यष्ट्याह्वयस्य (of liquorice) + अष्टपलेन (with eight palas).",
            "अ + अ → आ."),
        mcq("apply", 4, "In verse 13, which word does युक्तं (joined) agree with?",
            ("पयः, the milk",
             "युक्तं is neuter nominative, like पयः."),
            [("निरूहः, the enema", "निरूहः is masculine; युक्तं is neuter."),
             ("पिप्पलीभिः, the long peppers", "That is feminine instrumental plural."),
             ("अष्टपलेन, eight palas", "That is instrumental; युक्तं is nominative.")],
            "The milk is cooked and then joined with ghee and honey; the joined thing is the milk.",
            "An adjective agrees with its noun in gender, case and number."),
        mcq("transfer", 5, "Like …हितो निरूहः, which invented phrase says milk (पयः, neuter) is beneficial in visarpa?",
            ("विसर्पहितं पयः",
             "पयः is neuter, so the -हित compound takes -म् (written ं)."),
            [("विसर्पहितः पयः", "-अः is masculine, as with निरूहः, not neuter."),
             ("विसर्पहिता पयः", "-आ is feminine."),
             ("विसर्पहितान् पयः", "-आन् is masculine accusative plural.")],
            "A compound ending in -हित agrees with its noun: हितो (हितः) निरूहः, हितं पयः.",
            "-हित agrees with its noun's gender.",
            teaches="A compound ending in -हित ('beneficial in') agrees with its noun: masculine निरूहः → -हितः; neuter पयः → -हितम्."),
    ],
}

# ---------------------------------------------------------------- unit 14
AUTHORED["14"] = {
    "title": "शृतं पयः … सुशीतं पित्तामयान् हंति",
    "question": "What is the milk of verse 14 boiled with, how is it given, and what does it destroy?",
    "rule": ("Milk boiled with liquorice, rodhra, candana, lotus and blue water lily, with sugar, honey and ghee, well cooled, "
             "destroys the ailments of Pitta, together with the jīvanīya group."),
    "limits": ("रोघ्र is probably a misprint for रोध्र (lodhra); आमय as a drug name is unclear; अर्घ्यं ('valuable') is doubtful. No questions on these. "
               "Jīvanīya is the name of a standard group of ten herbs, named only, not listed. Plant parts are not stated."),
    "explain_hi": ("यहाँ दूध को यष्ट्याह्व यानी मुलेठी, रोध्र यानी लोध्र (छपा ‘रोघ्र’), एक अस्पष्ट ‘आमय’ और चन्दन के साथ, फिर कमल और उत्पल यानी सम्भवतः नीलकमल के साथ उबाला जाता है। "
                   "उसमें शर्करा, शहद और घी मिलाकर उसे भली-भाँति ठण्डा किया जाता है। "
                   "ऐसा दूध पित्त के आमयों यानी रोगों को नष्ट करता है, और ‘सजीवनीयं’ से जीवनीय गण भी साथ जुड़ता है। "
                   "जीवनीय दस जड़ी-बूटियों के एक प्रसिद्ध गण का नाम है; श्लोक उसके सदस्य नहीं गिनाता। ‘अर्घ्यं’ का अर्थ यहाँ संदिग्ध है।"),
    "hook": "मुलेठी-चन्दन-कमल-उत्पल में दूध उबालो, शर्करा-शहद-घी, खूब ठण्डा: पित्त के रोग भागें।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "What does the milk of verse 14 destroy?",
            ("The ailments of Pitta",
             "पित्तामयान् हंति: it destroys the ailments of Pitta."),
            [("The ailments of Kapha", "Kapha is not named in verse 14."),
             ("The ailments of Vāta", "Vāta is not named in verse 14."),
             ("Pain in the head only", "No head pain is named in verse 14.")],
            "पित्त + आमयान् = the ailments of Pitta, object of हंति (destroys).",
            "पित्तामय = ailment of Pitta."),
        match(1, "Match each word of verse 14 to its meaning as the card gives it.",
              [["कमल", "lotus"], ["उत्पल", "blue water lily"], ["शर्करा", "sugar"],
               ["क्षौद्र", "honey"], ["सुशीत", "well cooled"]],
              "Kamala is standard (lotus); utpala is probably the blue water lily.",
              "कमल = lotus; उत्पल = blue water lily; शर्करा = sugar; क्षौद्र = honey; सुशीत = well cooled."),
        order(2, "Put these words of verse 14 in the verse's order.",
              ["शृतं", "कमलोत्पलैश्च", "सशर्कराक्षौद्रघृतं", "सुशीतं", "पित्तामयान् हंति", "सजीवनीयं"],
              "Boiled, with lotus and lily; with sugar, honey, ghee; well cooled; destroys Pitta ailments; with jīvanīya.",
              "शृतं · कमलोत्पलैश्च · सशर्कराक्षौद्रघृतं · सुशीतं · पित्तामयान् हंति · सजीवनीयं.",
              role="extend",
              teaches="Verse 14 moves from boiling (शृतं) through the additions and cooling (सुशीतं) to its effect (पित्तामयान् हंति)."),
        mcq("discriminate", 3, "What does सजीवनीयं add to the milk of verse 14?",
            ("The jīvanīya herb group",
             "जीवनीय is the name of a standard group of ten herbs; it is named, not listed."),
            [("One plant called jīvanī", "The card treats jīvanīya as a group name, not one plant."),
             ("A patient who is living", "It names a drug group joined (स-) to the milk, not a patient."),
             ("A measure of the milk", "No measure is given in verse 14.")],
            "स-जीवनीयम्: together with the jīvanīya (group).",
            "जीवनीय = a group name (ten herbs), not listed here."),
        multi("apply", 4, "Which of these does verse 14 join with the boiled milk?",
              [("Sugar (शर्करा)", "Right: सशर्कराक्षौद्रघृतं names sugar."),
               ("Honey (क्षौद्र)", "Right: क्षौद्र is in the same compound."),
               ("Ghee (घृत)", "Right: घृत closes that compound."),
               ("Salt (लवण)", "Salt is not named in verse 14."),
               ("Oil (तैल)", "Oil is not named in verse 14.")],
              [0, 1, 2],
              "स-शर्करा-क्षौद्र-घृतम्: with sugar, honey and ghee.",
              "Additions of verse 14: शर्करा, क्षौद्र, घृत."),
        mcq("transfer", 5, "Join invented कफ + आमयान्, like पित्तामयान्. Which is right?",
            ("कफामयान्",
             "अ + आ → आ, as in पित्त + आमयान् = पित्तामयान्."),
            [("कफोमयान्", "ओ comes from अ + उ, not from अ + आ."),
             ("कफेमयान्", "ए comes from अ + इ, not from अ + आ."),
             ("कफमयान्", "The vowels merge into आ; they are not dropped.")],
            "Same rule as पित्त + आमयान् → पित्तामयान्.",
            "अ + आ → आ.",
            teaches="A short अ and a long आ merge into आ (पित्त + आमयान् = पित्तामयान्; कफ + आमयान् = कफामयान्)."),
    ],
}

# ---------------------------------------------------------------- unit 15
AUTHORED["15"] = {
    "title": "… पयः शृतं … मधुयष्टिकल्कैः",
    "question": "Which ingredients can be read in the damaged verse 15, and what is boiled?",
    "rule": ("On a conjectural reading: with candana, drākṣā (grape), madhuka and others (honey and kāśmarya rest on a guessed split), milk is boiled; "
             "with śrāvaṇī, mudgaparṇī and balā, and with pastes (kalka) of guptā and madhuyaṣṭi (liquorice). शृतं = boiled."),
    "limits": ("मोपांगना, शीतपाकी and सैंन्यैः are unclear; the split क्षौद्र + काश्मर्य is a guess; बलाखं is probably बलाख्यं; "
               "guptā and madhuka are disputed. No questions on these. The sentence runs on into the next lines (युक्तं, line 05.04.30), "
               "so this verse gives no use or verb."),
    "explain_hi": ("यह श्लोक बहुत बिगड़ा है; पहली पंक्ति के कई शब्द (मोपांगना, शीतपाकी, सैंन्यैः) पढ़े नहीं जाते। "
                   "पढ़े जाने वाले द्रव्य हैं: चन्दन, द्राक्षा यानी मुनक्का या अंगूर, और मधुक यानी सम्भवतः मुलेठी (विवादित); ‘क्षौद्रिकाश्मर्य’ को शहद और काश्मर्य यानी सम्भवतः गम्भारी पढ़ना केवल अनुमान है। "
                   "दूसरी पंक्ति में ‘पयः शृतं’ यानी उबाला हुआ दूध है, अनुमान से श्रावणी यानी सम्भवतः मुण्डी, मुद्गपर्णी यानी जंगली मूँग और बला के साथ, "
                   "और गुप्ता (पहचान विवादित) तथा मधुयष्टि यानी मुलेठी के कल्कों यानी लुगदी के साथ। "
                   "वाक्य अगली पंक्तियों में ‘युक्तं’ के साथ आगे चलता है।"),
    "hook": "चन्दन-द्राक्षा-मुलेठी ... दूध उबालो, मुलेठी का कल्क: वाक्य आगे चलता है।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "What is boiled in verse 15?",
            ("Milk (पयः)",
             "पयः शृतं: boiled milk."),
            [("Ghee (घृत)", "Ghee is not named in verse 15."),
             ("Oil (तैल)", "Oil is not named in verse 15."),
             ("Water (जल)", "No water is named in verse 15.")],
            "Line 2 opens with पयः शृतं, boiled milk.",
            "पयः = milk; शृत = boiled."),
        match(1, "Match each clear word of verse 15 to its meaning.",
              [["पयः", "milk"], ["शृतं", "boiled"], ["कल्कैः", "with pastes"],
               ["मधुयष्टि", "liquorice"], ["द्राक्षा", "grape or raisin"]],
              "These words are clear in the damaged verse; drākṣā and madhuyaṣṭi have standard identifications.",
              "पयः = milk; शृतं = boiled; कल्कैः = with pastes; मधुयष्टि = liquorice; द्राक्षा = grape/raisin."),
        order(2, "Put these clear items of verse 15 in the printed order.",
              ["चंदन", "द्राक्षा", "मधुक", "पयः शृतं", "मधुयष्टिकल्कैः"],
              "Line 1 names candana, drākṣā, madhuka; line 2 the boiled milk and the liquorice pastes.",
              "चंदन · द्राक्षा · मधुक · पयः शृतं · मधुयष्टिकल्कैः.",
              role="extend",
              teaches="Verse 15 lists drugs in line 1 and gives 'boiled milk' and the pastes in line 2."),
        mcq("discriminate", 3, "Which meaning fits शृतं in verse 15?",
            ("boiled",
             "शृत = boiled (√श्रा)."),
            [("cooled", "'Cooled' is शीत, as in सुशीत."),
             ("strained", "'Strained' is पूत."),
             ("ground", "'Ground' is पिष्ट; the pastes are कल्क.")],
            "पयः शृतं = boiled milk.",
            "शृत = boiled."),
        mcq("apply", 4, "What does the card say about the sentence of verse 15?",
            ("It runs on into the next lines",
             "युक्तं follows in line 05.04.30; no verb or use is in verse 15."),
            [("Its main verb stands in line 2", "Line 2 has no finite verb; शृतं is a participle."),
             ("It closes the recipe of verse 14", "Verse 14 ends with its own verb हंति; this is a new list."),
             ("It begins a new chapter", "The chapter continues; no new formula appears.")],
            "Verse 15 is a list of ingredients and the boiled milk; the sentence goes on.",
            "A sentence may run across units; keep each question to the unit."),
        mcq("transfer", 5, "Like पयः शृतं 'boiled milk', which invented phrase means boiled water, with जल (neuter)?",
            ("जलं शृतम्",
             "जल is neuter like पयः, so the participle is neuter -म्."),
            [("जलं शृतः", "-अः is masculine."),
             ("जलं शृता", "-आ is feminine."),
             ("जलं शृतान्", "-आन् is masculine accusative plural.")],
            "A past participle agrees with its noun: पयः शृतम्, जलं शृतम्.",
            "Participle agrees with its neuter noun: -म्.",
            teaches="A past participle like शृत agrees with its noun; with a neuter noun (पयः, जलम्) it takes -म्."),
    ],
}

# ---------------------------------------------------------------- unit 16
AUTHORED["16"] = {
    "title": "गोधूमचूर्णैश्च पिचुप्रमाणैः",
    "question": "What further ingredients, measure and state does verse 16 add to the boiled milk?",
    "rule": ("Wheat powders of the measure of a picu, the juice of sugarcane and vidārī, oil prepared with liquorice (yaṣṭīmadhu), "
             "sugar candy, honey and ghee are added; it is cooled. इक्षोः is the genitive of इक्षु."),
    "limits": ("The verse continues the boiled milk of line 05.04.29 and names the basti only in line 05.04.32. The kind of oil is not stated; "
               "रसेन is singular but is taken for both juices. Vidārī is probably Indian kudzu; sitopalā probably sugar candy."),
    "explain_hi": ("पिछली पंक्तियों का उबला दूध यहाँ और द्रव्यों से युक्त होता है: पिचु के माप के गेहूँ के चूर्ण, और इक्षु यानी ईख तथा विदारी यानी सम्भवतः विदारीकन्द का रस। "
                   "फिर यष्टीमधु यानी मुलेठी से तैयार किया तेल, और सितोपला यानी सम्भवतः मिश्री, शहद और घी। अन्त में वह ठण्डा (‘शीतः’) होता है। "
                   "‘इक्षोः’ उकारान्त पुल्लिंग ‘इक्षु’ की षष्ठी है: ईख का। "
                   "बस्ति का नाम अगले श्लोक की पहली पंक्ति में आता है।"),
    "hook": "पिचु भर गेहूँ, ईख-विदारी का रस, मुलेठी का तेल, मिश्री-शहद-घी: ठण्डा करो।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "What measure is given for the wheat powders in verse 16?",
            ("A picu",
             "पिचुप्रमाणैः: of the measure of a picu."),
            [("A pala", "No pala is named in verse 16."),
             ("A prasṛta", "No prasṛta is named in verse 16."),
             ("An āḍhaka", "No āḍhaka is named in verse 16.")],
            "गोधूमचूर्णैश्च पिचुप्रमाणैः: wheat powders of a picu's measure.",
            "पिचु = a small measure."),
        match(1, "Match each drug of verse 16 to its identity as the card gives it.",
              [["गोधूम", "wheat"], ["इक्षु", "sugarcane"], ["विदारी", "probably Indian kudzu"],
               ["सितोपला", "sugar candy"], ["यष्टीमधु", "liquorice"]],
              "Wheat and sugarcane are standard; vidārī and sitopalā are probable.",
              "गोधूम = wheat; इक्षु = sugarcane; विदारी = Indian kudzu (probable); सितोपला = sugar candy; यष्टीमधु = liquorice."),
        order(2, "Put these phrases of verse 16 in the verse's order.",
              ["गोधूमचूर्णैश्च", "पिचुप्रमाणैः", "इक्षोर्विदार्याश्च रसेन", "तैलेन यष्टीमधुसाधितेन", "सितोपलाक्षौद्रघृतैश्च", "शीतः"],
              "Wheat powders and their measure, the juices, the oil, sugar candy-honey-ghee, and last 'cooled'.",
              "गोधूमचूर्णैश्च · पिचुप्रमाणैः · इक्षोर्विदार्याश्च रसेन · तैलेन … · सितोपला… · शीतः.",
              role="extend",
              teaches="Verse 16 adds solids (wheat), juices, a medicated oil and sweet additions, and ends with शीतः (cooled)."),
        mcq("discriminate", 3, "Which is the right split of इक्षोर्विदार्याश्च in verse 16?",
            ("इक्षोः + विदार्याः + च",
             "-ओः before voiced व → -ओर्; -आः before च → -आश्च."),
            [("इक्षु + विदार्याः + च", "That would join as the compound इक्षुविदार्याश्च, without -ओर्."),
             ("इक्षोः + विदार्या + च", "विदार्या + च gives विदार्या च, with no श्."),
             ("इक्षो + र्विदार्याः + च", "र्विदार्या is no word; the र् belongs to इक्षोः.")],
            "इक्षोः (of sugarcane) + विदार्याः (of vidārī) + च (and), both genitives of रसेन.",
            "-ओः/-ऐः before a voiced sound → -ओर्/-ऐर्; -ः before च → -श्."),
        mcq("apply", 4, "With what is the oil of verse 16 prepared?",
            ("With yaṣṭīmadhu (liquorice)",
             "तैलेन यष्टीमधुसाधितेन: with oil prepared with liquorice."),
            [("With the juice of sugarcane", "The sugarcane juice is a separate addition."),
             ("With powder of wheat grain", "The wheat powders are a separate addition."),
             ("With the juice of vidārī", "The vidārī juice is a separate addition.")],
            "यष्टीमधु-साधित = prepared with liquorice; the oil's own kind is not stated.",
            "साधित = prepared."),
        mcq("transfer", 5, "Like इक्षोः 'of sugarcane' from इक्षु, which form means of the wind, from masculine वायु?",
            ("वायोः",
             "Masculine -उ stems take -ओः in the genitive singular, like इक्षोः."),
            [("वायुः", "Nominative singular: 'the wind'."),
             ("वायवः", "Nominative plural: 'winds'."),
             ("वायुना", "Instrumental: 'by the wind'.")],
            "इक्षु → इक्षोः; वायु → वायोः.",
            "Masculine -उ stem, genitive singular -ओः.",
            teaches="A masculine -उ stem takes -ओः in the genitive singular (इक्षु → इक्षोः, वायु → वायोः)."),
    ],
}

# ---------------------------------------------------------------- unit 17
AUTHORED["17"] = {
    "title": "बस्तिः प्रशस्तः स समस्तदेहदाहे",
    "question": "In which conditions does verse 17 recommend this basti?",
    "rule": ("That basti is recommended in burning of the whole body, with pain or seated in a part; in gulma, atisāra, bhrama, "
             "mūtrakṛcchra and the wasted (kṣīṇa); in injury and in the wasting of ojas and strength. Conditions stand in the locative (-ए)."),
    "limits": ("'That basti' is the milk preparation of lines 05.04.28-31. Line 1 may be read as three kinds of burning or two; no question on the count. "
               "The last compound has a stray syllable (ओजोज) and is not questioned. Ojas = vital essence."),
    "explain_hi": ("पिछली पंक्तियों में बनी दूध की बस्ति यहाँ ‘प्रशस्त’ यानी अनुशंसित कही गई है। "
                   "पहली पंक्ति: पूरे शरीर की दाह यानी जलन में, जो पीड़ा सहित हो या किसी अवयव में टिकी हो। "
                   "दूसरी पंक्ति: गुल्म यानी पेट की गाँठ, अतिसार यानी दस्त, भ्रम यानी चक्कर, मूत्रकृच्छ्र यानी कठिनाई से पेशाब, और क्षीण यानी दुर्बल व्यक्ति में; "
                   "क्षत यानी चोट में, और ओजस् यानी जीवन-सार तथा बल के क्षय में। "
                   "सब स्थितियाँ सप्तमी (-ए) में हैं: ‘दाहे’ = जलन में।"),
    "hook": "दाह, गुल्म, दस्त, चक्कर, कष्ट से पेशाब, क्षीण, चोट, ओज-क्षय: यह दूध-बस्ति।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "What is the first condition named in verse 17 for this basti?",
            ("Burning of the whole body",
             "समस्तदेहदाहे: in burning of the whole body."),
            [("Swelling of the whole body", "Swelling is not named in verse 17."),
             ("Hoarseness of the voice", "Hoarseness is not named in verse 17."),
             ("Aversion to food", "Aversion to food is not named in verse 17.")],
            "समस्त-देह-दाहे opens the list of conditions.",
            "दाह = burning."),
        match(1, "Match each condition of verse 17 to its meaning.",
              [["गुल्म", "abdominal lump"], ["अतिसार", "diarrhoea"], ["भ्रम", "giddiness"],
               ["मूत्रकृच्छ्र", "difficult urination"], ["क्षीण", "the wasted"]],
              "These five make up the compound of line 2.",
              "गुल्म = abdominal lump; अतिसार = diarrhoea; भ्रम = giddiness; मूत्रकृच्छ्र = dysuria; क्षीण = wasted."),
        order(2, "Put these conditions of verse 17, line 2, in the verse's order.",
              ["गुल्म", "अतिसार", "भ्रम", "मूत्रकृच्छ्र", "क्षीण"],
              "The compound runs gulma, atisāra, bhrama, mūtrakṛcchra, kṣīṇa.",
              "गुल्म · अतिसार · भ्रम · मूत्रकृच्छ्र · क्षीण.",
              role="extend",
              teaches="Line 2 of verse 17 lists gulma, atisāra, bhrama, mūtrakṛcchra and kṣīṇa in one compound in the locative."),
        mcq("discriminate", 3, "Which is the right split of गुल्मातिसार in verse 17?",
            ("गुल्म + अतिसार",
             "अ + अ → आ: गुल्म + अतिसार = गुल्मातिसार."),
            [("गुल्मा + तिसार", "Neither गुल्मा nor तिसार is the word."),
             ("गुल्मः + अतिसार", "-अः before अ becomes -ओऽ: it would read गुल्मोऽतिसार."),
             ("गुल्मम् + अतिसार", "म् before a vowel stays: it would read गुल्ममतिसार.")],
            "गुल्म (abdominal lump) + अतिसार (diarrhoea).",
            "अ + अ → आ."),
        mcq("apply", 4, "Which pair of conditions is named in verse 17?",
            ("Diarrhoea and giddiness",
             "अतिसार and भ्रम both stand in line 2."),
            [("Diarrhoea and hoarseness", "Hoarseness is not named in verse 17."),
             ("Giddiness and erysipelas", "Erysipelas is not named in verse 17."),
             ("Gulma and aversion to food", "Aversion to food is not named in verse 17.")],
            "Line 2 names gulma, atisāra, bhrama, mūtrakṛcchra, kṣīṇa; then kṣata and the wasting of ojas and strength.",
            "Only what verse 17 names belongs to its list."),
        mcq("transfer", 5, "Like दाहे 'in burning', which invented form means in fever, from ज्वर?",
            ("ज्वरे",
             "Locative singular -ए of an -अ stem, like दाहे."),
            [("ज्वरः", "Nominative: 'fever' as subject."),
             ("ज्वरेण", "Instrumental: 'by fever'."),
             ("ज्वरात्", "Ablative: 'from fever'.")],
            "The condition in which a basti is recommended stands in the locative: दाहे, ज्वरे.",
            "Locative -ए = 'in (the condition)'.",
            teaches="Conditions in which a remedy is recommended stand in the locative singular -ए (दाहे 'in burning', ज्वरे 'in fever')."),
    ],
}

# ---------------------------------------------------------------- unit 18
AUTHORED["18"] = {
    "title": "कोशातकारग्वधदेवदारु",
    "question": "Which drugs does verse 18 list, what is cooked in water, and how much liquid is kept?",
    "rule": ("Kośātaka, āragvadha, devadāru, mūrvā, aśvadaṃṣṭrā, kuṭaja, arka and pāṭhā; having cooked (पक्त्वा) kulattha and bṛhatī in water, "
             "there should be ten prasṛtas of that liquid."),
    "limits": ("Line 1 is a list with no verb: the text does not say these drugs are cooked with kulattha and bṛhatī, though it is likely. "
               "Plant parts are not stated; mūrvā is only probable. The recipe continues in line 05.04.36. A prasṛta is a handful-measure."),
    "explain_hi": ("यहाँ एक नए निरूह का नुस्खा शुरू होता है (इसे किसे देना है, यह इकाई २० में आता है)। पहली पंक्ति में आठ द्रव्य हैं: कोशातक यानी सम्भवतः तोरई, आरग्वध यानी अमलतास, देवदारु यानी देवदार, "
                   "मूर्वा (सम्भावित पहचान), अश्वदंष्ट्रा यानी सम्भवतः गोखरू, कुटज यानी कुड़ा, अर्क यानी आक और पाठा। इस पंक्ति में कोई क्रिया नहीं है। "
                   "दूसरी पंक्ति: कुलत्थ यानी कुलथी और बृहती यानी सम्भवतः बड़ी कटेरी को जल में ‘पक्त्वा’ यानी पकाकर, उस रस के दस प्रसृत हों। "
                   "प्रसृत अंजलि-भर का एक माप है।"),
    "hook": "तोरई से पाठा तक आठ, कुलथी-कटेरी जल में पकाओ: दस प्रसृत रस।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "How much of the liquid should there be in verse 18?",
            ("Ten prasṛtas",
             "रसस्य तस्य प्रसृता दश स्युः: ten prasṛtas of that liquid."),
            [("Eight prasṛtas", "Eight is the count of drugs in line 1, not the measure."),
             ("Two āḍhakas", "No āḍhaka is named in verse 18."),
             ("One prastha", "No prastha is named in verse 18.")],
            "प्रसृताः दश = ten prasṛtas.",
            "दश = ten; प्रसृत = handful-measure."),
        match(1, "Match each drug of verse 18 to its identity as the card gives it.",
              [["आरग्वध", "Indian laburnum"], ["देवदारु", "deodar"], ["कुटज", "kurchi"],
               ["अर्क", "giant milkweed"], ["कुलत्थ", "horse gram"]],
              "These five identifications are standard in the data.",
              "आरग्वध = Indian laburnum; देवदारु = deodar; कुटज = kurchi; अर्क = giant milkweed; कुलत्थ = horse gram."),
        order(2, "Put these drugs of verse 18, line 1, in the verse's order (from āragvadha).",
              ["आरग्वध", "देवदारु", "मूर्वा", "अश्वदंष्ट्रा", "कुटज", "अर्क"],
              "After kośātaka the compound runs āragvadha, devadāru, mūrvā, aśvadaṃṣṭrā, kuṭaja, arka, then pāṭhā.",
              "आरग्वध · देवदारु · मूर्वा · अश्वदंष्ट्रा · कुटज · अर्क.",
              role="extend",
              teaches="Line 1 of verse 18 lists eight drugs from kośātaka to pāṭhā in one compound with no verb."),
        mcq("discriminate", 3, "Which reading of प्रसृता दश in verse 18 is right?",
            ("प्रसृताः + दश",
             "-आः before a voiced consonant drops the visarga: प्रसृता दश."),
            [("प्रसृतः + दश", "-अः before a voiced consonant gives -ओ: प्रसृतो दश."),
             ("प्रसृतम् + दश", "It would be written प्रसृतं दश."),
             ("प्रसृतौ + दश", "-औ stays unchanged before a consonant.")],
            "प्रसृताः (m. nom. pl.) agrees with दश, ten.",
            "-आः + voiced consonant → -आ."),
        mcq("apply", 4, "According to line 2 of verse 18, what is cooked in water?",
            ("Kulattha and bṛhatī",
             "पक्त्वा कुलत्थान् बृहतीं च तोये: having cooked kulattha and bṛhatī in water."),
            [("Arka and pāṭhā only", "They are in line 1, which has no verb."),
             ("Only the drugs of line 1", "Line 2 names only kulattha and bṛhatī as cooked."),
             ("Kulattha and goat meat", "No meat is named in verse 18.")],
            "Only kulattha and bṛhatī are named as cooked; the link with line 1 is not stated.",
            "Keep to what the verse says: line 1 has no verb."),
        mcq("transfer", 5, "Like पक्त्वा 'having cooked' from √पच्, which form means having eaten, from √भुज्?",
            ("भुक्त्वा",
             "-त्वा forms the absolutive; ज् becomes क् before त्, as च् does in पक्त्वा."),
            [("भुक्तः", "Past participle: 'eaten', not 'having eaten'."),
             ("भुङ्क्ते", "Present tense: 'he eats'."),
             ("भोक्तुम्", "Infinitive: 'to eat'.")],
            "√पच् → पक्त्वा; √भुज् → भुक्त्वा.",
            "-त्वा = 'having done'.",
            teaches="The absolutive in -त्वा means 'having done' (√पच् → पक्त्वा 'having cooked', √भुज् → भुक्त्वा 'having eaten')."),
    ],
}

# ---------------------------------------------------------------- unit 19
AUTHORED["19"] = {
    "title": "तान्सर्षपतैलामदनैः सकुष्ठैः",
    "question": "With what are the ten prasṛtas joined in verse 19, and which genitive list follows?",
    "rule": ("Those (the prasṛtas of liquid) are joined with mustard oil and madana, with kuṣṭha, with akṣa-measures and with prasṛtas. "
             "Line 2 lists in the genitive (-अस्य, 'of'): honey, oil, phalāhvaya, kṣāra, and mustard oil."),
    "limits": ("No verb: the sentence runs on. Which item the akṣa and prasṛta measures belong to is unclear; madana may be the emetic nut or beeswax; "
               "phalāhvaya ('fruit-named') is unidentified; तैला- may be a misprint, and सर्षप-तैल may be two items (mustard, oil). No questions on these points. Kṣāra stays kṣāra."),
    "explain_hi": ("श्लोक १८ के दस प्रसृत रस (‘तान्’ = उन्हें) यहाँ और द्रव्यों से युक्त होते हैं: सरसों का तेल और मदन यानी मैनफल या मोम (पहचान विवादित), "
                   "कुष्ठ यानी कूठ के साथ, अक्ष के माप और प्रसृतों के साथ। कौन-सा माप किस द्रव्य का है, यह स्पष्ट नहीं। "
                   "दूसरी पंक्ति षष्ठी (‘का’) की सूची है: शहद का, तेल का, फलाह्वय का (अपहचाना), क्षार का, और सार्षप यानी सरसों के तेल का। "
                   "‘सार्षपस्य’ अपने से ठीक पहले के ‘तैलस्य’ का विशेषण है। वाक्य आगे चलता है।"),
    "hook": "सरसों-तेल, मदन, कूठ, अक्ष-प्रसृत; फिर शहद-तेल-फलाह्वय-क्षार-सरसों-तेल का।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "Which unit of weight is named in verse 19?",
            ("Akṣa",
             "अक्षप्रमाणैः: with akṣa-measures (akṣa, a unit of weight)."),
            [("Tulā", "No tulā is named in verse 19."),
             ("Āḍhaka", "No āḍhaka is named in verse 19."),
             ("Prastha", "No prastha is named in verse 19.")],
            "Verse 19 names the akṣa and the prasṛta as measures.",
            "अक्ष = a unit of weight."),
        order(1, "Put these genitives of verse 19, line 2, in the verse's order.",
              ["क्षौद्रस्य", "तैलस्य", "फलाह्वयस्य", "क्षारस्य", "तैलस्य च सार्षपस्य"],
              "Honey, oil, phalāhvaya, kṣāra, and last mustard oil.",
              "क्षौद्रस्य · तैलस्य · फलाह्वयस्य · क्षारस्य · तैलस्य च सार्षपस्य."),
        match(2, "Match each word of verse 19 to its meaning as the card gives it.",
              [["कुष्ठ", "costus root"], ["अक्ष", "a unit of weight"], ["प्रसृत", "a handful-measure"],
               ["क्षौद्र", "honey"], ["सार्षप", "of mustard"]],
              "Kuṣṭha is costus root; akṣa and prasṛta are measures; sārṣapa qualifies the oil.",
              "कुष्ठ = costus; अक्ष = weight unit; प्रसृत = handful; क्षौद्र = honey; सार्षप = of mustard.",
              role="extend",
              teaches="Verse 19 mixes drugs (कुष्ठ, क्षौद्र) with measures (अक्ष, प्रसृत); सार्षप is an adjective 'of mustard'."),
        mcq("discriminate", 3, "In line 2 of verse 19, what does सार्षपस्य qualify?",
            ("The oil right before it",
             "तैलस्य च सार्षपस्य: of mustard oil."),
            [("The honey at the start", "क्षौद्रस्य stands first, far from सार्षपस्य."),
             ("The kṣāra named earlier", "Kṣāra is a separate item, not mustard."),
             ("The fruit-named drug", "फलाह्वय is a separate, unidentified item.")],
            "सार्षपस्य (adj., gen.) agrees with the second तैलस्य: of mustard oil.",
            "An adjective qualifies the noun it agrees with, here तैलस्य."),
        mcq("apply", 4, "Which is the right split of सकुष्ठैरक्षप्रमाणैः in verse 19?",
            ("सकुष्ठैः + अक्षप्रमाणैः",
             "-ऐः before a vowel → -ऐर्: सकुष्ठैर् + अक्ष…."),
            [("सकुष्ठै + रक्षप्रमाणैः", "रक्षप्रमाण is no word; the र् comes from the visarga of -ऐः."),
             ("सकुष्ठः + ऐरक्षप्रमाणैः", "ऐरक्षप्रमाण is no word; the measure is अक्षप्रमाण."),
             ("सकुष्ठम् + अक्षप्रमाणैः", "म् before a vowel stays: it would read सकुष्ठमक्ष….")],
            "सकुष्ठैः (with kuṣṭha) + अक्षप्रमाणैः (with akṣa-measures).",
            "-ऐः + vowel → -ऐर् + vowel."),
        mcq("transfer", 5, "Like क्षौद्रस्य 'of honey', which form means of milk, from क्षीर (neuter)?",
            ("क्षीरस्य",
             "Genitive singular -अस्य of an -अ stem, like क्षौद्रस्य."),
            [("क्षीरेण", "Instrumental: 'with milk'."),
             ("क्षीरात्", "Ablative: 'from milk'."),
             ("क्षीरे", "Locative: 'in milk'.")],
            "क्षौद्र → क्षौद्रस्य; क्षीर → क्षीरस्य.",
            "Genitive singular -अस्य = 'of'.",
            teaches="An -अ stem takes -अस्य in the genitive singular, 'of' (क्षौद्रस्य, तैलस्य, क्षीरस्य)."),
    ],
}

# ---------------------------------------------------------------- unit 20
AUTHORED["20"] = {
    "title": "दद्यान्निरूहं कफरोगिताय",
    "question": "To whom does verse 20 say the nirūha should be given, and which new list begins in line 2?",
    "rule": ("Give the nirūha to one with Kapha disease, to one with slow digestive fire (mandāgni) and to one with aversion to food: the recipients "
             "stand in the dative (-आय, -ए). Line 2 begins a new list: punarnavā, eraṇḍa, bṛhatī, aśmabheda, vṛścīva, bhūtīka, balā, palāśa."),
    "limits": ("Line 1 appears to complete the recipe of lines 05.04.34-37. कफरोगिताय is an irregular dative kept as printed. Line 2 is an accusative list "
               "whose verb comes in line 05.04.46; its print has a stray anusvāra, and vṛścīva and bhūtīka are unidentified. No questions on line 2."),
    "explain_hi": ("पहली पंक्ति पिछले नुस्खे (कफहर निरूह) को पूरा करती लगती है: यह निरूह कफ के रोगी को, मन्दाग्नि यानी कमज़ोर पाचन वाले को, "
                   "और भोजन से अरुचि (‘अशनविद्विष्’ = भोजन से द्वेष करने वाला) वाले को देना चाहिए। "
                   "तीनों पाने वाले चतुर्थी (‘को’) में हैं। "
                   "दूसरी पंक्ति से नया नुस्खा शुरू होता है: पुनर्नवा यानी गदहपूर्णा, एरण्ड यानी अरण्डी, बृहती यानी सम्भवतः बड़ी कटेरी, अश्मभेद यानी सम्भवतः पाषाणभेद, "
                   "वृश्चीव और भूतीक (अपहचाने), बला यानी बरियार और पलाश यानी ढाक। इसकी क्रिया पंक्ति ०५.०४.४६ में आती है।"),
    "hook": "कफ-रोगी, मन्दाग्नि, अन्न से अरुचि: इन्हें निरूह दो; फिर पुनर्नवा से पलाश तक नई सूची।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "In verse 20, who is named first to receive the nirūha?",
            ("One with Kapha disease",
             "कफरोगिताय: for one afflicted with Kapha disease."),
            [("One with Pitta disease", "Pitta is not named in verse 20."),
             ("One with burning pain", "Burning is not named in verse 20."),
             ("One with a gulma lump", "Gulma is not named in verse 20.")],
            "The list of recipients opens with कफरोगिताय.",
            "कफरोगी = one with Kapha disease."),
        match(1, "Match each word of verse 20, line 1, to its meaning.",
              [["कफरोगिताय", "to one with Kapha disease"], ["मंदाग्नये", "to one with slow digestive fire"],
               ["अशनविद्विषे", "to one with aversion to food"], ["निरूहं", "decoction enema"], ["दद्यात्", "should give"]],
              "Line 1 is one sentence: give the nirūha to these three.",
              "कफरोगिताय · मंदाग्नये · अशनविद्विषे = the three recipients; दद्यात् निरूहम् = should give the nirūha."),
        order(2, "Put these words of verse 20, line 1, in the verse's order.",
              ["दद्यान्निरूहं", "कफरोगिताय", "मंदाग्नये", "चाशनविद्विषे च"],
              "The verb and object first, then the three recipients.",
              "दद्यान्निरूहं · कफरोगिताय · मंदाग्नये · चाशनविद्विषे च.",
              role="extend",
              teaches="Line 1 of verse 20 puts 'should give the nirūha' first and then names three recipients in the dative."),
        mcq("discriminate", 3, "Which is the right split of मंदाग्नये in verse 20?",
            ("मंद + अग्नये",
             "अ + अ → आ: मंद + अग्नये = मंदाग्नये."),
            [("मंदा + ग्नये", "ग्नये is no word; the word is अग्नये."),
             ("मंदम् + अग्नये", "म् before a vowel stays: it would read मंदमग्नये."),
             ("मंदः + अग्नये", "-अः before अ becomes -ओऽ: it would read मंदोऽग्नये.")],
            "मंद (slow) + अग्नि (fire), dative मंदाग्नये: to one with slow fire.",
            "अ + अ → आ."),
        mcq("apply", 4, "Which case do the three recipients in verse 20 take?",
            ("Dative: 'to, for'",
             "-आय and -ए (कफरोगिताय, मंदाग्नये, अशनविद्विषे) are dative endings."),
            [("Genitive: 'of'", "The genitive would be -अस्य or -एः."),
             ("Locative: 'in'", "The locative is used for conditions (verse 17), not recipients."),
             ("Nominative: subject", "The subject is the giver; the recipients are not nominative.")],
            "With दद्यात् (should give), the receiver stands in the dative.",
            "Receiver of 'give' → dative."),
        mcq("transfer", 5, "Like मंदाग्नये, which invented form names the weak man (दुर्बल) as the one to whom a basti is given?",
            ("दुर्बलाय",
             "Dative singular -आय of an -अ stem (दुर्बल → दुर्बलाय)."),
            [("दुर्बलस्य", "Genitive: 'of the weak man'."),
             ("दुर्बलेन", "Instrumental: 'by the weak man'."),
             ("दुर्बलः", "Nominative: 'the weak man' as subject.")],
            "The receiver of दद्यात् stands in the dative: -आय for -अ stems, -अये for masculine -इ stems (मंदाग्नये).",
            "Receiver → dative (-आय / -अये).",
            teaches="The one to whom something is given stands in the dative: -आय for -अ stems (दुर्बलाय), -अये for masculine -इ stems (मंदाग्नये)."),
    ],
}

# ---------------------------------------------------------------- unit 21
AUTHORED["21"] = {
    "title": "द्विपंचमूलं च पलांशकानि",
    "question": "What does verse 21 add to the list, how are the items treated, and how are the fruits measured?",
    "rule": ("The ten-root group, with a pala as the share, crushed (क्षुण्ण), washed (धौत), and eight fruits; bilva, yava, aṅkola, kulattha "
             "and dhānya; the fruits should be measured by prasṛtas. The adjectives are neuter plural (-आनि)."),
    "limits": ("The eight fruits are not named; whether the adjectives cover the roots or the whole list is not settled; whether bilva to dhānya are also "
               "measured by prasṛta is not stated; dhānya ('grain') could be coriander (disputed). The verb comes in line 05.04.46."),
    "explain_hi": ("यह पुनर्नवादि सूची की अगली कड़ी है। पहली पंक्ति: द्विपञ्चमूल यानी दशमूल, ‘पलांशक’ यानी एक पल के भाग वाले, ‘क्षुण्ण’ यानी कुचले और ‘धौत’ यानी धोए हुए, और आठ फल (नाम नहीं दिए)। "
                   "दूसरी पंक्ति: बिल्व यानी बेल, यव, अंकोल यानी सम्भवतः ढेरा, कुलत्थ यानी कुलथी और धान्य (अनाज; धनिया भी पढ़ा जा सकता है)। "
                   "फल प्रसृत के माप से हों। "
                   "विशेषण नपुंसक बहुवचन (-आनि) हैं, पर किस पर लागू हैं, यह तय नहीं।"),
    "hook": "दशमूल पल-अंश, कुचला-धोया, आठ फल; बेल-यव-अंकोल-कुलथी-धान्य; फल प्रसृत से।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "Which two treatments are named in verse 21, line 1?",
            ("Crushed and washed",
             "क्षुण्णानि धौतानि: crushed, washed."),
            [("Ground and strained", "Neither grinding nor straining is named in verse 21."),
             ("Boiled and cooled", "Neither boiling nor cooling is named in verse 21."),
             ("Fried and soaked", "Neither frying nor soaking is named in verse 21.")],
            "क्षुण्ण = crushed (√क्षुद्); धौत = washed (√धाव्).",
            "क्षुण्ण = crushed; धौत = washed."),
        match(1, "Match each word of verse 21 to its meaning as the card gives it.",
              [["द्विपंचमूल", "the ten roots"], ["क्षुण्ण", "crushed"], ["धौत", "washed"],
               ["बिल्व", "bael"], ["कुलत्थ", "horse gram"]],
              "Dvipañcamūla is 'two fives of roots', the daśamūla group.",
              "द्विपंचमूल = ten roots; क्षुण्ण = crushed; धौत = washed; बिल्व = bael; कुलत्थ = horse gram."),
        order(2, "Put these items of verse 21, line 2, in the verse's order.",
              ["बिल्वं", "यव", "अंकोल", "कुलत्थ", "धान्य"],
              "Bilva, then the compound yava, aṅkola, kulattha, dhānya.",
              "बिल्वं · यव · अंकोल · कुलत्थ · धान्य.",
              role="extend",
              teaches="Line 2 of verse 21 lists bilva, yava, aṅkola, kulattha and dhānya, then gives the prasṛta measure for the fruits."),
        mcq("discriminate", 3, "In verse 21, which measure is given for the fruits?",
            ("The prasṛta",
             "फलानि च स्युः प्रसृतोन्मितानि: the fruits measured by prasṛtas."),
            [("The pala", "The pala is the share in line 1 (पलांशकानि), not the fruits' measure."),
             ("The akṣa", "No akṣa is named in verse 21."),
             ("The half tulā", "No tulā is named in verse 21.")],
            "Line 1 has पलांशकानि (a pala as share); line 2 measures the fruits by prasṛta.",
            "Keep pala (line 1) apart from prasṛta (line 2)."),
        mcq("apply", 4, "Which is the right split of प्रसृतोन्मितानि in verse 21?",
            ("प्रसृत + उन्मितानि",
             "अ + उ → ओ: प्रसृत + उन्मितानि = प्रसृतोन्मितानि."),
            [("प्रसृतो + न्मितानि", "न्मित is no word; the word is उन्मित, measured."),
             ("प्रसृतः + उन्मितानि", "-अः before a vowel drops the visarga and does not join."),
             ("प्रसृतम् + उन्मितानि", "म् before a vowel stays: it would read प्रसृतमुन्मितानि.")],
            "प्रसृत (handful-measure) + उन्मितानि (measured).",
            "अ + उ → ओ."),
        mcq("transfer", 5, "Like क्षुण्णानि धौतानि फलानि, which invented phrase means washed leaves, with पत्राणि (neuter plural)?",
            ("धौतानि पत्राणि",
             "Neuter plural noun, neuter plural participle -आनि, like धौतानि फलानि."),
            [("धौताः पत्राणि", "-आः is masculine plural."),
             ("धौतेभ्यः पत्राणि", "-एभ्यः is dative or ablative plural."),
             ("धौतम् पत्राणि", "-अम् is singular.")],
            "A participle agrees with its noun: धौतानि फलानि, धौतानि पत्राणि.",
            "Neuter plural agreement -आनि.",
            teaches="A participle used as an adjective agrees with a neuter plural noun in -आनि (क्षुण्णानि धौतानि फलानि; धौतानि पत्राणि)."),
    ],
}

# ---------------------------------------------------------------- unit 22
AUTHORED["22"] = {
    "title": "पयो जलद्व्याढकसाधितं",
    "question": "How is the milk of verse 22 prepared and cleaned, and whose pastes are listed next?",
    "rule": ("Milk prepared with two āḍhakas of water, that milk remaining, strained through a clean cloth. Line 2 lists in the genitive the paste drugs: "
             "vacā, śatāhvā, amaradāru, kuṣṭha, yaṣṭyāhva, siddhārthaka and pippalī."),
    "limits": ("पयस् means milk or water; here milk, since water (जल) is named apart and क्षीर remains. Boiling the water away is not spelled out. "
               "Line 2 has misprints (शताव्हा, a stray ऽ, siddhārtha / kapippalīnāṃ): no questions on line 2."),
    "explain_hi": ("दूध को दो आढक जल के साथ सिद्ध किया जाता है, जब तक वह दूध ही शेष रहे, और फिर उसे स्वच्छ वस्त्र से छाना जाता है। "
                   "‘पयः’ का अर्थ दूध भी हो सकता है और जल भी; यहाँ दूध है, क्योंकि जल अलग से कहा गया है और ‘तत्क्षीरावशिष्टं’ दूध के शेष रहने की बात करता है। "
                   "दूसरी पंक्ति में कल्क के द्रव्य षष्ठी में हैं: वचा यानी बच, शताह्वा यानी सम्भवतः सोआ, अमरदारु यानी देवदार, कुष्ठ यानी कूठ, यष्ट्याह्व यानी मुलेठी, "
                   "सिद्धार्थक यानी सम्भवतः सफेद सरसों और पिप्पली यानी पीपर। ‘कल्कैः’ शब्द अगले श्लोक में आता है।"),
    "hook": "दो आढक जल में दूध पकाओ, दूध ही बचे, साफ़ कपड़े से छानो; फिर सात कल्क-द्रव्य।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "How much water is the milk prepared with in verse 22?",
            ("Two āḍhakas",
             "जलद्व्याढकसाधितं: prepared with two āḍhakas of water."),
            [("Ten prasṛtas", "No prasṛta is named in verse 22."),
             ("Four palas", "No pala is named in verse 22."),
             ("Half a tulā", "No tulā is named in verse 22.")],
            "जल-द्वि-आढक-साधितम्: prepared with two āḍhakas of water.",
            "आढक = a large measure."),
        match(1, "Match each word of verse 22, line 1, to its meaning.",
              [["पयः", "milk"], ["जल", "water"], ["शुचि", "clean"], ["वस्त्र", "cloth"], ["पूत", "strained"]],
              "Line 1 describes preparing and straining the milk.",
              "पयः = milk; जल = water; शुचि = clean; वस्त्र = cloth; पूत = strained."),
        order(2, "Put these words of verse 22, line 1, in the verse's order.",
              ["पयो", "जलद्व्याढकसाधितं", "तत्क्षीरावशिष्टं", "शुचिवस्त्रपूतं"],
              "Milk, prepared with two āḍhakas of water, that milk remaining, strained through clean cloth.",
              "पयो · जलद्व्याढकसाधितं · तत्क्षीरावशिष्टं · शुचिवस्त्रपूतं.",
              role="extend",
              teaches="Line 1 of verse 22 gives the steps in order: prepare with water, keep the milk, strain through a clean cloth."),
        mcq("discriminate", 3, "Why is पयः in verse 22 read as milk, not water?",
            ("Water (जल) is named apart, and क्षीर remains",
             "जल is a separate word, and तत्क्षीरावशिष्टं says that milk remains."),
            [("Because पयः can only mean milk", "पयस् can mean milk or water; the card says so."),
             ("Because the next verse names cow milk", "No cow is named; the reason is in this line."),
             ("Because basti never uses plain water", "The card makes no such claim.")],
            "Context decides: water is named as जल, and the remainder is क्षीर, milk.",
            "पयस् = milk or water; context decides."),
        mcq("apply", 4, "Which is the right split of जलद्व्याढक in verse 22?",
            ("जल + द्वि + आढक",
             "इ + आ → या: द्वि + आढक = द्व्याढक."),
            [("जलद् + व्याढक", "जलद् and व्याढक are not the words here."),
             ("जल + द्वय + आढक", "द्वय + आढक would give द्वयाढक."),
             ("जल + द्व्या + ढक", "ढक is no word; the measure is आढक.")],
            "जल (water) + द्वि (two) + आढक (a measure).",
            "इ + different vowel → य् + vowel."),
        mcq("transfer", 5, "Join invented त्रि + आढक, like द्वि + आढक → द्व्याढक. Which is right?",
            ("त्र्याढक",
             "इ before a different vowel becomes य्: त्रि + आढक = त्र्याढक."),
            [("त्रियाढक", "The इ does not stay; it becomes य्."),
             ("त्राढक", "The इ is not dropped; it becomes य्."),
             ("त्रेढक", "ए comes from अ + इ, not from इ + आ.")],
            "Same rule as द्वि + आढक → द्व्याढक.",
            "इ + different vowel → य्.",
            teaches="Final इ before a different vowel becomes य् (द्वि + आढक = द्व्याढक; त्रि + आढक = त्र्याढक)."),
    ],
}

# ---------------------------------------------------------------- unit 23
AUTHORED["23"] = {
    "title": "कल्कैर्यवान्या मदनैश्च युक्तं",
    "question": "What is the milk of verse 23 joined with, at what temperature, and with which three liquids?",
    "rule": ("Joined with pastes, with yavānī and madana; neither too hot nor too cold; smeared with jaggery and rock salt; joined with a set of three "
             "prasṛtis of honey, of oil and of fresh ghee (नवस्य, agreeing in the genitive)."),
    "limits": ("Whether three prasṛtis are meant for each liquid or three in all is not stated. The neuter words agree with the milk (पयः) of line 05.04.42; "
               "the verb comes in line 05.04.46. The kind of oil is not stated."),
    "explain_hi": ("पिछले श्लोक का छना दूध यहाँ कल्कों से, यवानी यानी अजवायन से और मदन यानी मैनफल से युक्त होता है। "
                   "वह ‘नात्युष्णशीत’ यानी न अधिक गरम, न अधिक ठण्डा हो, और गुड़ तथा सैन्धव यानी सेंधा नमक से ‘आक्त’ यानी लिप्त हो। "
                   "फिर शहद, तेल और नए घी के तीन प्रसृतियों से युक्त हो; तीन प्रसृति हर एक की हैं या सबकी मिलाकर, यह नहीं कहा। "
                   "‘नवस्य’ षष्ठी में ‘सर्पिषः’ से मेल खाता है: नए घी का।"),
    "hook": "कल्क-अजवायन-मैनफल, न गरम न ठण्डा, गुड़-सेंधा; शहद-तेल-नया घी: तीन प्रसृति।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "In verse 23, how warm should the preparation be?",
            ("Neither too hot nor too cold",
             "नात्युष्णशीतं: not too hot, not too cold."),
            [("Hot, as it comes off the fire", "The verse says 'not too hot'."),
             ("Well cooled after boiling", "The verse says 'not too cold'."),
             ("Warmed in the sun first", "No sun is named in verse 23.")],
            "न-अति-उष्ण-शीतम्: neither too hot nor too cold.",
            "नात्युष्णशीत = moderate warmth."),
        match(1, "Match each word of verse 23 to its meaning as the card gives it.",
              [["यवानी", "ajwain"], ["मदन", "emetic nut"], ["गुड", "jaggery"],
               ["सैंधव", "rock salt"], ["नव", "fresh"]],
              "Yavānī and madana are standard identifications in the data.",
              "यवानी = ajwain; मदन = emetic nut; गुड = jaggery; सैंधव = rock salt; नव = fresh."),
        order(2, "Put these phrases of verse 23 in the verse's order.",
              ["कल्कैर्यवान्या", "मदनैश्च युक्तं", "नात्युष्णशीतं", "गुडसैंधवाक्तं", "क्षौद्रस्य तैलस्य च सर्पिषश्च नवस्य", "युक्तं प्रसृतित्रयेण"],
              "Pastes and yavānī, madana, the temperature, jaggery and salt, the three liquids, the triad of prasṛtis.",
              "कल्कैर्यवान्या · मदनैश्च युक्तं · नात्युष्णशीतं · गुडसैंधवाक्तं · क्षौद्रस्य… · युक्तं प्रसृतित्रयेण.",
              role="extend",
              teaches="Verse 23 adds pastes, sets the warmth, adds jaggery and rock salt, then honey, oil and fresh ghee by a triad of prasṛtis."),
        mcq("discriminate", 3, "Of which three substances is the set of three prasṛtis in verse 23?",
            ("Honey, oil and fresh ghee",
             "क्षौद्रस्य तैलस्य च सर्पिषश्च नवस्य: of honey, oil and fresh ghee."),
            [("Jaggery, rock salt and honey", "Jaggery and salt are 'smeared in' (आक्त), not measured by prasṛti."),
             ("Ajwain, madana and oil", "Ajwain and madana go with the pastes."),
             ("Milk, water and ghee", "Water is not named in verse 23.")],
            "The three genitives belong to प्रसृतित्रयेण.",
            "प्रसृतित्रय = a triad of prasṛtis."),
        mcq("apply", 4, "Which is the right split of गुडसैंधवाक्तं in verse 23?",
            ("गुड + सैंधव + आक्तम्",
             "अ + आ → आ: सैंधव + आक्तम् = सैंधवाक्तम्."),
            [("गुड + सैंधवा + क्तम्", "क्त is no word; the participle is आक्त, smeared."),
             ("गुड + सैंधवः + आक्तम्", "-अः before a vowel drops the visarga and does not join."),
             ("गुड + सैंधवम् + आक्तम्", "म् before a vowel stays: it would read सैंधवमाक्तम्.")],
            "गुड (jaggery) + सैंधव (rock salt) + आक्त (smeared).",
            "अ + आ → आ."),
        mcq("transfer", 5, "Like सर्पिषः … नवस्य 'of fresh ghee', which invented phrase means of fresh honey?",
            ("नवस्य क्षौद्रस्य",
             "The adjective takes the same genitive singular as its noun: नवस्य क्षौद्रस्य."),
            [("नवेन क्षौद्रस्य", "नवेन is instrumental; it does not agree with the genitive."),
             ("नवानां क्षौद्रस्य", "नवानाम् is genitive plural; क्षौद्रस्य is singular."),
             ("नवः क्षौद्रस्य", "नवः is nominative; it does not agree.")],
            "An adjective agrees with its noun in case and number: नवस्य सर्पिषः, नवस्य क्षौद्रस्य.",
            "Adjective agrees in case and number.",
            teaches="An adjective agrees with its noun in case and number: नवस्य सर्पिषः 'of fresh ghee', नवस्य क्षौद्रस्य 'of fresh honey'."),
    ],
}

# ---------------------------------------------------------------- unit 24
AUTHORED["24"] = {
    "title": "दद्यान्निरूहं विधिना विधिज्ञः",
    "question": "Who should give the nirūha described in the preceding lines, how, and what does it destroy?",
    "rule": ("One who knows the rule (विधिज्ञ, -ज्ञ = knower) should give that nirūha by the rule; it destroys (-घ्न) ailments produced by "
             "the combination of all (सर्वसंसर्गकृतामयघ्न)."),
    "limits": ("'Combination of all' does not say of what; it may mean all the doṣas, but the text does not say so, and no question rests on it. "
               "The unit ends the sentence that began in line 05.04.39; तं is that nirūha."),
    "explain_hi": ("यह इकाई पंक्ति ०५.०४.३९ से चल रहे लम्बे वाक्य को पूरा करती है; ‘दद्यात्’ उसकी क्रिया है। "
                   "विधि को जानने वाला (‘विधिज्ञ’) उस निरूह को विधि से दे। "
                   "वह निरूह ‘सर्वसंसर्ग’ यानी सबके संसर्ग से उत्पन्न आमयों यानी रोगों का नाशक (‘-घ्न’) है। "
                   "‘सबके’ से किसका संसर्ग, यह पाठ नहीं बताता; सम्भवतः सब दोषों का, पर यह जोड़ा नहीं गया।"),
    "hook": "विधिज्ञ विधि से दे: सबके संसर्ग से जन्मे रोगों का नाशक निरूह।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "In unit 24, who should give the nirūha?",
            ("One who knows the rule",
             "विधिज्ञः: knower of the rule."),
            [("Any attendant at hand", "The text names the विधिज्ञ, not any attendant."),
             ("The patient himself", "No self-giving is stated."),
             ("One who knows the drugs", "-ज्ञ is joined to विधि, the rule, not to drugs.")],
            "दद्यान्निरूहं विधिना विधिज्ञः: the knower of the rule gives it by the rule.",
            "विधिज्ञ = one who knows the rule."),
        match(1, "Match each word of unit 24 to its meaning.",
              [["दद्यात्", "should give"], ["विधिना", "by the rule"], ["विधिज्ञः", "one who knows the rule"],
               ["आमय", "ailment"], ["घ्न", "destroying"]],
              "All five words stand in the unit's one line.",
              "दद्यात् = should give; विधिना = by the rule; विधिज्ञः = knower of the rule; आमय = ailment; घ्न = destroying."),
        order(2, "Put these words of unit 24 in the text's order.",
              ["दद्यान्निरूहं", "विधिना", "विधिज्ञः", "तं", "सर्वसंसर्गकृतामयघ्नं"],
              "Give the nirūha, by the rule, the knower of the rule, that (nirūha), destroyer of ailments.",
              "दद्यान्निरूहं · विधिना · विधिज्ञः · तं · सर्वसंसर्गकृतामयघ्नं.",
              role="extend",
              teaches="Unit 24 gives the verb and object (दद्यान्निरूहं), how (विधिना), who (विधिज्ञः) and what the nirūha does (…आमयघ्नं)."),
        mcq("discriminate", 3, "Which is the right split of दद्यान्निरूहं in unit 24?",
            ("दद्यात् + निरूहम्",
             "त् before न becomes न्: दद्यात् + निरूहम् = दद्यान्निरूहम्."),
            [("दद्या + न्निरूहम्", "दद्या and न्निरूह are not the words."),
             ("दद्याः + निरूहम्", "-आः before a voiced consonant would give दद्या निरूहम्."),
             ("दद्यम् + निरूहम्", "दद्यम् is no form of √दा here; the optative is दद्यात्.")],
            "दद्यात् (should give) + निरूहम् (the nirūha).",
            "त् + nasal → न् + nasal."),
        mcq("apply", 4, "In unit 24, what does तं (that) refer to?",
            ("The nirūha described before",
             "तं is the nirūha prepared in lines 05.04.39-45."),
            [("The physician who gives it", "The giver is विधिज्ञः, nominative; तं is accusative."),
             ("The patient receiving it", "No patient is named in unit 24."),
             ("The rule (विधि) itself", "विधि is in the instrumental विधिना; तं is masculine accusative like निरूहम्.")],
            "तं (m. acc. sg.) agrees with निरूहम्, the object of दद्यात्.",
            "A pronoun agrees with the noun it points to."),
        mcq("transfer", 5, "Like विधिज्ञः 'one who knows the rule' (nominative), which invented nominative means one who knows basti?",
            ("बस्तिज्ञः",
             "-ज्ञ = knower; nominative -अः, like विधिज्ञः."),
            [("बस्तिघ्नः", "-घ्न means destroying, as in आमयघ्न, not knowing."),
             ("बस्तिना", "Instrumental: 'by the basti'."),
             ("बस्तिज्ञम्", "-अम् is accusative; the giver is nominative.")],
            "X + ज्ञ = one who knows X: विधिज्ञः, बस्तिज्ञः.",
            "-ज्ञ = knower; -घ्न = destroyer.",
            teaches="A compound ending in -ज्ञ means 'one who knows' (विधिज्ञः, बस्तिज्ञः); one ending in -घ्न means 'destroying' (आमयघ्न)."),
    ],
}


NOTES_HI = {
    "12": ("विश्वास: निम्न। पंक्तियाँ ०५.०४.२२-२३, एक वाक्य (‘अम्लः’ पंक्ति २३ के ‘रसः’ का विशेषण है)। दोनों पंक्तियाँ बिगड़ी हैं; अनुवाद अनुमानित। "
           "text_flags: ‘तैल’ में विभक्ति नहीं (सम्भवतः ‘तैले’, या ‘तैलघृतस्य’ एक समास); ‘भृष्टःच्छागाच्छताव्हा…’ सम्भवतः ‘भृष्टाच्छागाच्छताह्वा…’ (विसर्ग सम्भवतः खोया आ; शताव्हा = शताह्वा)। "
           "खुला बिन्दु (OPEN ०५.०४.२३): ‘हितैः’ तृतीया बहुवचन ‘रसः’ से मेल नहीं खाता, ‘मिर्ष’ अज्ञात शब्द, ‘बलवर्ण’ विभक्ति-रहित; ‘शिरोरुजी इष्टः’ दो तरह पढ़ा जा सकता है। इन पर प्रश्न नहीं। "
           "‘मांस’ शब्द पंक्ति २२ में नहीं, केवल ‘छाग’ है। संधि जाँची: चतुष्पले = चतुः + पले; सपेष्यो = सपेष्यः + (ब) ; रेतोऽग्नि = रेतः + अग्नि।"),
    "13": ("विश्वास: मध्यम। पंक्तियाँ ०५.०४.२४-२५। ‘युक्तं’ नपुंसक है और ‘पयः’ से मेल खाता है, ‘निरूहः’ से नहीं; दूध दोबारा नहीं कहा गया। "
           "text_flag: छपा ‘शताव्हा’ = शताह्वा (व और ह उलटे)। ‘शताह्वाफलपिप्पलीभिः’ तीन द्रव्य (शताह्वा, फल, पिप्पली) भी हो सकते हैं; यहाँ ‘शताह्वा का फल और पिप्पली’ पढ़ा। "
           "‘यष्ट्याह्वय’ = ‘यष्टि नाम वाला’, यानी यष्टीमधु। संधि जाँची: यष्ट्याह्वय = यष्टि + आह्वय; …स्याष्टपलेन = …स्य + अष्टपलेन; ससर्पिर्मधु = स + सर्पिः + मधु; हितो निरूहः = हितः + निरूहः।"),
    "14": ("विश्वास: मध्यम। पंक्तियाँ ०५.०४.२६-२७; कर्ता ‘पयः’ (नपुंसक)। text_flag: छपा ‘रोघ्र’ ज्ञात शब्द नहीं, सम्भवतः ‘रोध्र’ (ध का घ छपा)। "
           "‘आमय’ द्रव्य-नाम के रूप में अस्पष्ट (शब्द का अर्थ ‘रोग’ है), सम्भवतः बिगड़ा। खुला बिन्दु (OPEN ०५.०४.२६): ‘अर्घ्यं’ (मूल्यवान) संदिग्ध है, text_flags में नहीं; इस पर प्रश्न नहीं। "
           "जीवनीय दस द्रव्यों का प्रसिद्ध गण है (जीवक, ऋषभक, मेदा, महामेदा, काकोली, क्षीरकाकोली, मुद्गपर्णी, माषपर्णी, जीवन्ती, मधुक), पाठ में सूची नहीं। "
           "संधि जाँची: पयोऽर्घ्यं = पयः + अर्घ्यम्; कमलोत्पलैश्च = कमल + उत्पलैः + च; पित्तामयान् = पित्त + आमयान्; हंति = हन्ति।"),
    "15": ("विश्वास: निम्न। पंक्तियाँ ०५.०४.२८-२९; वाक्य पंक्ति ०५.०४.३० (‘युक्तं’) में आगे चलता है। पहली पंक्ति का समास बहुत बिगड़ा है: ‘मोपांगना’, ‘शीतपाकी’, ‘सैंन्यैः’ अस्पष्ट, छपे रूप में रखे। "
           "खुला बिन्दु (OPEN ०५.०४.२८): ‘क्षौद्रिकाश्मर्य’ = क्षौद्र + काश्मर्य केवल अनुमान है (संधि से ‘क्षौद्रकाश्मर्य’ होता); पक्का न करें। "
           "text_flag: ‘बलाखं’ सम्भवतः ‘बलाख्यं’ (बला नाम वाला)। ‘गुप्ता’ पौधा (सम्भवतः कपिकच्छू, विवादित) या ‘रक्षित’ हो सकता है; ‘मधुक’ सम्भवतः मुलेठी, महुआ भी (विवादित)। "
           "तीन जड़ी-बूटियों का दूध से सम्बन्ध अनुमान है। इन पर प्रश्न नहीं।"),
    "16": ("विश्वास: मध्यम। पंक्तियाँ ०५.०४.३०-३१; पंक्ति ०५.०४.२९ का उबला दूध आगे चलता है, बस्ति का नाम पंक्ति ०५.०४.३२ में। कोई text_flag नहीं। "
           "‘पिचुप्रमाणैः’ गेहूँ के चूर्णों के साथ लिया; ‘रसेन’ एकवचन है पर ईख और विदारी दोनों का रस माना। विदारी सम्भवतः Pueraria tuberosa; Ipomoea digitata को भी विदारी कहते हैं। "
           "तेल का प्रकार नहीं दिया। संधि जाँची: गोधूमचूर्णैश्च = …चूर्णैः + च; पिचुप्रमाणैरिक्षोर्विदार्याश्च = पिचुप्रमाणैः + इक्षोः + विदार्याः + च; सितोपला = सित + उपला।"),
    "17": ("विश्वास: मध्यम। पंक्तियाँ ०५.०४.३२-३३; ‘सः बस्तिः’ पंक्तियाँ ०५.०४.२८-३१ की दूध की तैयारी है। "
           "पंक्ति ३२ का विभाजन अनिश्चित: दाह के तीन प्रकार (पूरा शरीर, पीड़ा सहित, अंग में टिका) या दो; संख्या पर प्रश्न नहीं। "
           "text_flag और खुला बिन्दु (OPEN ०५.०४.३३): ‘क्षतौजोजबल’ में ‘ज’ अतिरिक्त लगता है (उसके बिना २२ अक्षर); इस समास पर प्रश्न नहीं। ‘ओजोजबल’ = ‘ओज से जन्मा बल’ भी पढ़ा जा सकता है। "
           "संधि जाँची: सशूले ऽवयवाश्रिते = सशूले + अवयवाश्रिते (छपाई में अन्तर के साथ); गुल्मातिसार = गुल्म + अतिसार।"),
    "18": ("विश्वास: मध्यम। पंक्तियाँ ०५.०४.३४-३५; पंक्तियाँ ३४-३६ एक नुस्खा लगती हैं। पंक्ति ३४ प्रथमा बहुवचन की सूची है, क्रिया नहीं; उसके द्रव्य कुलत्थ-बृहती के साथ पकते हैं, यह पाठ नहीं कहता। "
           "छपा ‘मूर्व्वा’ (दोहरा व) = मूर्वा। खुला बिन्दु (OPEN ०५.०४.३४): मूर्वा की पहचान (Marsdenia tenacissima) सम्भावित ही है, अन्य पौधे भी सुझाए गए; इस पर प्रश्न नहीं। "
           "किस अंग का प्रयोग, यह नहीं कहा। संधि जाँची: कोशातकारग्वध = कोशातक + आरग्वध; मूर्वाश्वदंष्ट्रा = मूर्वा + अश्वदंष्ट्रा; कुटजार्क = कुटज + अर्क; प्रसृता दश = प्रसृताः + दश।"),
    "19": ("विश्वास: मध्यम। पंक्तियाँ ०५.०४.३६-३७; क्रिया नहीं, वाक्य आगे चलता है। ‘तान्’ पंक्ति ०५.०४.३५ के दस प्रसृत हैं। "
           "text_flag: ‘सर्षपतैला-’ का दीर्घ आ सम्भवतः छपाई की भूल (तैल + मदन); ‘सर्षप’ और ‘तैल’ दो द्रव्य भी हो सकते हैं। ‘अक्षप्रमाणैः’ और ‘प्रसृतैः’ किस द्रव्य के माप हैं, अस्पष्ट। "
           "मदन = मैनफल (Randia) या मोम, पाठ तय नहीं करता। ‘फलाह्वय’ = ‘फल नाम वाला’, अपहचाना। पंक्ति ३७ की षष्ठी-सूची का अगली पंक्ति से सम्बन्ध नहीं बताया। "
           "संधि जाँची: सकुष्ठैरक्ष = सकुष्ठैः + अक्ष; प्रसृतैश्च = प्रसृतैः + च।"),
    "20": ("विश्वास: मध्यम। पंक्तियाँ ०५.०४.३८-३९। पंक्ति ३८ पंक्तियाँ ३६-३७ के वाक्य को पूरा करती लगती है। ‘कफरोगिताय’ छपे रूप में रखा (कफरोगिन् की चतुर्थी ‘कफरोगिणे’ होती), छन्द के लिए खिंचा रूप लगता है। "
           "पंक्तियाँ ३९-४६ एक वाक्य लगती हैं; क्रिया ‘दद्यात् निरूहम्’ पंक्ति ४६ में। text_flag: ‘पुनर्नवैंरंड’ में ऐ के बाद अनुस्वार अतिरिक्त; ‘बृहत्त्य’ का दोहरा त केवल लिपि का रूप। "
           "अश्मभेद (सम्भवतः Bergenia ligulata) विवादित; वृश्चीव और भूतीक अपहचाने। संधि जाँची: दद्यान्निरूहं = दद्यात् + निरूहम्; मंदाग्नये = मंद + अग्नये; चाशन = च + अशन; बृहत्त्यश्म = बृहती + अश्मभेद।"),
    "21": ("विश्वास: मध्यम। पंक्तियाँ ०५.०४.४०-४१; पंक्ति ३९ का वाक्य आगे, क्रिया पंक्ति ४६ में। कोई text_flag नहीं। "
           "‘पलांशकानि, क्षुण्णानि, धौतानि’ नपुंसक बहुवचन हैं जबकि ‘द्विपंचमूलम्’ एकवचन; ये मूलों पर या पूरी सूची पर लागू हो सकते हैं, पाठ तय नहीं करता। आठ फलों के नाम नहीं। "
           "बिल्व से धान्य तक का माप भी प्रसृत है या नहीं, नहीं कहा। ‘धान्य’ = अनाज; ‘धान्यक’ (धनिया) दूसरा पाठ है, नहीं अपनाया। "
           "संधि जाँची: पलांशकानि = पल + अंशकानि; चाष्टौ = च + अष्टौ; यवांकोल = यव + अंकोल; प्रसृतोन्मितानि = प्रसृत + उन्मितानि।"),
    "22": ("विश्वास: मध्यम। पंक्तियाँ ०५.०४.४२-४३; पंक्ति ४१ का वाक्य आगे। ‘पयः’ दूध पढ़ा, क्योंकि ‘जल’ अलग है और ‘तत्क्षीरावशिष्टं’ दूध के शेष रहने की बात है। जल का उड़ जाना स्पष्ट नहीं कहा। "
           "text_flags: छपा ‘शताव्हा’ = शताह्वा; ‘हा’ के बाद का ऽ अतिरिक्त (आ + अ → आ); ‘सिद्धार्थ कपिप्पलीनां’ को सिद्धार्थक + पिप्पलीनाम् पढ़ा (छन्द दोनों में २२ अक्षर, निर्णायक नहीं); ‘कपि-पिप्पली’ (गजपिप्पली) भी सम्भव। "
           "दूसरी पंक्ति की षष्ठियाँ पंक्ति ४४ के ‘कल्कैः’ से जुड़ती हैं। संधि जाँची: पयो जल = पयः + जल; द्व्याढक = द्वि + आढक; तत्क्षीरावशिष्टं = तत् + क्षीर + अवशिष्टम्।"),
    "23": ("विश्वास: मध्यम। पंक्तियाँ ०५.०४.४४-४५; ‘युक्तं’, ‘आक्तं’ नपुंसक हैं और पंक्ति ४२ के ‘पयः’ से मेल खाते हैं; क्रिया पंक्ति ४६ में। कोई text_flag नहीं। "
           "तीन द्रव्य षष्ठी में और ‘प्रसृतित्रय’ तृतीया में: तीन प्रसृति हर एक की या कुल, नहीं कहा। ‘आक्त’ का शब्दार्थ ‘लिप्त’। प्रसृति = प्रसृत, एक ही माप। "
           "संधि जाँची: कल्कैर्यवान्या = कल्कैः + यवान्या; मदनैश्च = मदनैः + च; नात्युष्णशीतं = न + अति + उष्ण + शीतम्; गुडसैंधवाक्तं = गुड + सैंधव + आक्तम्; सर्पिषश्च = सर्पिषः + च।"),
    "24": ("विश्वास: मध्यम। गद्य, पंक्ति ०५.०४.४६; पंक्तियाँ ३९-४५ के वाक्य की क्रिया यहाँ है। कोई text_flag नहीं। "
           "‘सर्वसंसर्ग’ = सबका संसर्ग; किसका, यह नहीं कहा (सम्भवतः सब दोषों का), कुछ जोड़ा नहीं गया। ‘तं’ = यही निरूह। "
           "संधि जाँची: दद्यान्निरूहं = दद्यात् + निरूहम् (त् + न → न्न); विधिज्ञस्तं = विधिज्ञः + तम् (ः + त → स्त); कृतामयघ्नं = कृत + आमय + घ्नम्।"),
}


AIDS = {
    "12": {
        "chunks": "चतुष्पले तैल घृतस्य | भृष्टःच्छागाच्छताव्हादधिदाडिमाम्लः (बिगड़ा) ‖ रसः सपेष्यो | बलवर्ण मांसरेतोऽग्निहितैः | मिर्ष (अस्पष्ट) शिरोरुजीष्टः।",
        "anchors": "पल = तौल का माप · घृत = घी · छाग = बकरा · दधि = दही · दाडिम = अनार · अम्ल = खट्टा · रेतस् = वीर्य · अग्नि = पाचन-अग्नि।",
        "sandhi": "अः + घोष व्यंजन → ओ: सपेष्यः + बल → सपेष्यो बल; अः + अ → ओऽ: रेतः + अग्नि → रेतोऽग्नि; ः + प → ष्प: चतुः + पले → चतुष्पले।",
    },
    "13": {
        "diagram": {"groups": [{"label": "दूध पकाया", "items": ["आठ पल यष्ट्याह्वय", "शताह्वा-फल", "पिप्पली"]},
                               {"label": "युक्त", "items": ["सर्पिः (घी)", "मधु"]},
                               {"label": "निरूह हितकर", "items": ["वातरक्त", "विसर्प", "वैस्वर्य"]}]},
        "chunks": "यष्ट्याह्वयस्याष्टपलेन सिद्धं पयः | शताव्हाफलपिप्पलीभिः ‖ युक्तं ससर्पिर्मधु | वातरक्तविसर्पवैस्वर्यहितो निरूहः।",
        "sandhi": "इ + आ → या: यष्टि + आह्वय → यष्ट्याह्वय; अ + अ → आ: …स्य + अष्टपलेन → …स्याष्टपलेन; इः + म → इर्म: सर्पिः + मधु → सर्पिर्मधु।",
        "contrast": "‘युक्तं’ नपुंसक → ‘पयः’ (दूध) से मेल · ‘हितो’ पुल्लिंग → ‘निरूहः’ से मेल।",
    },
    "14": {
        "diagram": {"groups": [{"label": "दूध उबाला", "items": ["यष्ट्याह्व", "रोध्र (छपा रोघ्र)", "चन्दन", "कमल", "उत्पल"]},
                               {"label": "फिर", "items": ["शर्करा", "क्षौद्र", "घृत", "सुशीत"]},
                               {"label": "फल", "items": ["पित्त के आमय नाशे", "जीवनीय के साथ"]}]},
        "chunks": "यष्ट्याह्वरोघ्रामयचंदनैश्च | शृतं पयोऽर्घ्यं | कमलोत्पलैश्च ‖ सशर्कराक्षौद्रघृतं सुशीतं | पित्तामयान् हंति | सजीवनीयं।",
        "sandhi": "अ + उ → ओ: कमल + उत्पलैः → कमलोत्पलैः; अ + आ → आ: पित्त + आमयान् → पित्तामयान्; अः + अ → ओऽ: पयः + अर्घ्यम् → पयोऽर्घ्यं।",
        "frame": "क्या: उबला दूध · किसके साथ: मुलेठी, चन्दन, कमल, उत्पल · फिर: शर्करा-शहद-घी, खूब ठण्डा · फल: पित्त के रोग नाशे।",
    },
    "15": {
        "chunks": "मोपांगना (अस्पष्ट) चंदन शीतपाकी (अस्पष्ट) द्राक्षा क्षौद्रिकाश्मर्य मधुक सैंन्यैः (अस्पष्ट) ‖ पयः शृतं | श्रावणीमुद्गपर्णीबलाखं | गुप्तामधुयष्टिकल्कैः।",
        "anchors": "चन्दन = सम्भवतः संदल (सफ़ेद चन्दन) · द्राक्षा = मुनक्का या अंगूर · मधुक = सम्भवतः मुलेठी · शृत = उबाला हुआ · मुद्गपर्णी = जंगली मूँग · कल्क = लुगदी।",
        "frame": "पंक्ति १: द्रव्यों की सूची (कई शब्द अस्पष्ट) · पंक्ति २: उबला दूध, तीन जड़ी-बूटियाँ, मुलेठी के कल्क · क्रिया: आगे (युक्तं)।",
    },
    "16": {
        "chain": {"steps": ["उबला दूध (पिछली पंक्तियाँ)", "गेहूँ के चूर्ण, पिचु के माप", "ईख और विदारी का रस",
                            "मुलेठी से तैयार तेल", "मिश्री, शहद, घी", "ठण्डा (शीतः)"]},
        "chunks": "गोधूमचूर्णैश्च पिचुप्रमाणैः | इक्षोर्विदार्याश्च रसेन युक्तं ‖ तैलेन यष्टीमधुसाधितेन | सितोपलाक्षौद्रघृतैश्च शीतः।",
        "sandhi": "ऐः/ओः + स्वर/घोष → ऐर्/ओर्: पिचुप्रमाणैः + इक्षोः → पिचुप्रमाणैरिक्षोः, इक्षोः + विदार्याः → इक्षोर्विदार्याः; आः + च → आश्च: विदार्याः + च → विदार्याश्च।",
        "anchors": "गोधूम = गेहूँ · पिचु = छोटा माप · इक्षु = ईख · विदारी = सम्भवतः विदारीकन्द · सितोपला = सम्भवतः मिश्री · साधित = तैयार किया।",
    },
    "17": {
        "diagram": {"groups": [{"label": "पंक्ति १: दाह में", "items": ["पूरे शरीर की जलन", "पीड़ा सहित", "या अंग में टिकी"]},
                               {"label": "पंक्ति २", "items": ["गुल्म", "अतिसार", "भ्रम", "मूत्रकृच्छ्र", "क्षीण"]},
                               {"label": "पंक्ति २ (आगे)", "items": ["क्षत", "ओज और बल का क्षय"]}]},
        "chunks": "बस्तिः प्रशस्तः स | समस्तदेहदाहे सशूले ऽवयवाश्रिते वा ‖ गुल्मातिसारभ्रममूत्रकृच्छ्रक्षीणे | क्षतौजोजबलसंक्षये च।",
        "sandhi": "अ + अ → आ: गुल्म + अतिसार → गुल्मातिसार; ए + अ → एऽ: सशूले + अवयव → सशूले ऽवयव (छपाई में अन्तर के साथ)।",
        "anchors": "प्रशस्त = अनुशंसित · दाह = जलन · गुल्म = पेट की गाँठ · अतिसार = दस्त · भ्रम = चक्कर · मूत्रकृच्छ्र = कठिनाई से पेशाब · ओजस् = जीवन-सार।",
    },
    "18": {
        "diagram": {"groups": [{"label": "पंक्ति १: सूची, क्रिया नहीं", "items": ["कोशातक", "आरग्वध", "देवदारु", "मूर्वा", "अश्वदंष्ट्रा", "कुटज", "अर्क", "पाठा"]},
                               {"label": "पंक्ति २: जल में पकाकर", "items": ["कुलत्थ", "बृहती", "उस रस के दस प्रसृत"]}]},
        "chunks": "कोशातकारग्वधदेवदारुमूर्व्वाश्वदंष्ट्राकुटजार्कपाठाः ‖ पक्त्वा कुलत्थान् बृहतीं च तोये | रसस्य तस्य प्रसृता दश स्युः।",
        "sandhi": "अ + आ → आ: कोशातक + आरग्वध → कोशातकारग्वध; अ + अ → आ: कुटज + अर्क → कुटजार्क; आः + घोष → आ: प्रसृताः + दश → प्रसृता दश।",
        "anchors": "कोशातक = सम्भवतः तोरई · आरग्वध = अमलतास · अश्वदंष्ट्रा = सम्भवतः गोखरू · कुटज = कुड़ा · अर्क = आक · कुलत्थ = कुलथी · तोय = जल।",
    },
    "19": {
        "chunks": "तान्सर्षपतैलामदनैः | सकुष्ठैरक्षप्रमाणैः | प्रसृतैश्च युक्तान् ‖ क्षौद्रस्य तैलस्य फलाह्वयस्य | क्षारस्य तैलस्य च सार्षपस्य।",
        "sandhi": "ऐः + स्वर → ऐर्: सकुष्ठैः + अक्ष → सकुष्ठैरक्ष; ऐः + च → ऐश्च: प्रसृतैः + च → प्रसृतैश्च।",
        "frame": "किसे: उन (दस प्रसृत रस) को · किससे युक्त: सरसों-तेल, मदन, कुष्ठ, अक्ष और प्रसृत माप · फिर षष्ठी-सूची: शहद, तेल, फलाह्वय, क्षार, सरसों-तेल।",
        "anchors": "मदन = मैनफल या मोम (विवादित) · कुष्ठ = कूठ · अक्ष = तौल का माप · प्रसृत = अंजलि-भर · फलाह्वय = ‘फल नाम वाला’ (अपहचाना) · सार्षप = सरसों का।",
    },
    "20": {
        "chunks": "दद्यान्निरूहं | कफरोगिताय | मंदाग्नये | चाशनविद्विषे च ‖ पुनर्नवैंरंडबृहत्त्यश्मभेदवृश्चीवभूतीकबलापलाशान्।",
        "frame": "पंक्ति १: किसे दें (चतुर्थी): कफ-रोगी, मन्दाग्नि, अन्न से अरुचि · पंक्ति २: नई सूची (द्वितीया), क्रिया पंक्ति ०५.०४.४६ में।",
        "sandhi": "त् + न → न्न: दद्यात् + निरूहम् → दद्यान्निरूहम्; अ + अ → आ: मंद + अग्नये → मंदाग्नये; अ + अ → आ: च + अशन → चाशन।",
        "anchors": "निरूह = काढ़े की बस्ति · मन्दाग्नि = कमज़ोर पाचन · अशन = भोजन · विद्विष् = द्वेष करने वाला · पुनर्नवा = गदहपूर्णा · पलाश = ढाक।",
    },
    "21": {
        "diagram": {"groups": [{"label": "पंक्ति १", "items": ["द्विपंचमूल", "पल के अंश वाले", "कुचले", "धोए", "आठ फल"]},
                               {"label": "पंक्ति २", "items": ["बिल्व", "यव", "अंकोल", "कुलत्थ", "धान्य", "फल: प्रसृत के माप"]}]},
        "chunks": "द्विपंचमूलं च पलांशकानि | क्षुण्णानि धौतानि | फलानि चाष्टौ ‖ बिल्वं यवांकोलकुलत्थधान्यं | फलानि च स्युः प्रसृतोन्मितानि।",
        "sandhi": "अ + अ → आ: पल + अंशकानि → पलांशकानि, च + अष्टौ → चाष्टौ; अ + उ → ओ: प्रसृत + उन्मितानि → प्रसृतोन्मितानि।",
        "contrast": "पंक्ति १: ‘पलांशक’ (पल का भाग) · पंक्ति २: फल ‘प्रसृत’ से मापे।",
    },
    "22": {
        "chain": {"steps": ["दूध + दो आढक जल", "सिद्ध किया", "वही दूध शेष रहे", "स्वच्छ वस्त्र से छाना"]},
        "chunks": "पयो जलद्व्याढकसाधितं | तत्क्षीरावशिष्टं | शुचिवस्त्रपूतं ‖ वचाशताव्हाऽमरदारुकुष्ठयष्ट्याह्वसिद्धार्थ कपिप्पलीनां।",
        "sandhi": "इ + आ → या: द्वि + आढक → द्व्याढक; अ + अ → आ: क्षीर + अवशिष्टम् → क्षीरावशिष्टम्; अः + घोष → ओ: पयः + जल → पयो जल।",
        "anchors": "आढक = बड़ा माप · शुचि = स्वच्छ · वस्त्र = कपड़ा · पूत = छाना · वचा = बच · अमरदारु = देवदार · सिद्धार्थक = सम्भवतः सफेद सरसों।",
    },
    "23": {
        "diagram": {"groups": [{"label": "युक्त", "items": ["कल्क", "यवानी", "मदन"]},
                               {"label": "कैसा", "items": ["न अधिक गरम, न ठण्डा", "गुड़ और सैन्धव से आक्त"]},
                               {"label": "तीन प्रसृति", "items": ["क्षौद्र", "तैल", "नया सर्पिः"]}]},
        "chunks": "कल्कैर्यवान्या मदनैश्च युक्तं | नात्युष्णशीतं | गुडसैंधवाक्तं ‖ क्षौद्रस्य तैलस्य च सर्पिषश्च नवस्य | युक्तं प्रसृतित्रयेण।",
        "sandhi": "अ + अ → आ, इ + उ → यु: न + अति + उष्ण → नात्युष्ण; अ + आ → आ: सैंधव + आक्तम् → सैंधवाक्तम्; ः + य → र्य: कल्कैः + यवान्या → कल्कैर्यवान्या।",
        "anchors": "यवानी = अजवायन · मदन = मैनफल · गुड = गुड़ · सैन्धव = सेंधा नमक · आक्त = लिप्त · नव = नया · प्रसृति = प्रसृत, अंजलि-भर।",
    },
    "24": {
        "chunks": "दद्यान्निरूहं | विधिना | विधिज्ञस्तं | सर्वसंसर्गकृतामयघ्नं।",
        "frame": "कौन: विधिज्ञ · कैसे: विधि से · क्या: वह निरूह (पंक्तियाँ ०५.०४.३९-४५ का) · फल: सबके संसर्ग से उत्पन्न रोगों का नाशक।",
        "sandhi": "त् + न → न्न: दद्यात् + निरूहम् → दद्यान्निरूहम्; ः + त → स्त: विधिज्ञः + तम् → विधिज्ञस्तम्; अ + आ → आ: कृत + आमय → कृतामय।",
        "anchors": "विधि = नियम, विधि · -ज्ञ = जानने वाला · संसर्ग = मेल · आमय = रोग · -घ्न = नाश करने वाला।",
    },
}


IMAGE_SPECS = {
    ("13", "diagram"): {
        "file": "ka4-yashtiksira-13.svg",
        "alt": ("Flowchart of verse 13: milk cooked with eight palas of liquorice, shatahva fruit and pippali, joined with ghee and honey, "
                "gives a nirūha beneficial in three diseases: vatarakta, visarpa and vaisvarya"),
        "type": "mermaid",
        "code": ('flowchart TD\n'
                 '  A["आठ पल मुलेठी"] --> D["दूध पकाया"]\n'
                 '  B["शताह्वा-फल · पिप्पली"] --> D\n'
                 '  D --> E["घी और शहद से युक्त"]\n'
                 '  E --> F["निरूह हितकर"]\n'
                 '  F --> G["वातरक्त"]\n'
                 '  F --> H["विसर्प"]\n'
                 '  F --> I["वैस्वर्य"]\n'),
    },
    ("14", "diagram"): {
        "file": "ka4-pittahara-14.svg",
        "alt": ("Two columns for verse 14: milk boiled with liquorice, rodhra (printed roghra), amaya (unclear), sandalwood, lotus and blue water lily; "
                "then sugar, honey, ghee, well cooled, with the jivaniya group, destroying the ailments of Pitta"),
        "type": "split",
        "title": "श्लोक १४: शीतल दूध",
        "cols": [["दूध उबाला", ["यष्ट्याह्व (मुलेठी)", "रोध्र (छपा रोघ्र)", "आमय (अस्पष्ट)", "चन्दन", "कमल", "उत्पल"]],
                 ["फिर", ["शर्करा · शहद · घी", "भली-भाँति ठण्डा", "जीवनीय के साथ", "पित्त के रोग नाशे"]]],
    },
    ("17", "diagram"): {
        "file": "ka4-daha-17.svg",
        "alt": ("Two columns for verse 17: burning of the whole body, with pain or seated in a part; then gulma, atisara, bhrama, "
                "mutrakricchra, the wasted, injury, and wasting of ojas and strength"),
        "type": "split",
        "title": "श्लोक १७: यह बस्ति कहाँ प्रशस्त",
        "cols": [["पंक्ति १: दाह", ["पूरे शरीर की जलन", "पीड़ा सहित", "या अंग में टिकी"]],
                 ["पंक्ति २", ["गुल्म", "अतिसार", "भ्रम", "मूत्रकृच्छ्र", "क्षीण", "क्षत", "ओज और बल का क्षय"]]],
    },
    ("18", "diagram"): {
        "file": "ka4-koshataka-18.svg",
        "alt": ("Two columns for verse 18: line 1 lists eight drugs with no verb (koshataka, aragvadha, devadaru, murva, ashvadamshtra, "
                "kutaja, arka, patha); line 2 cooks kulattha and brihati in water, giving ten prasritas of liquid"),
        "type": "split",
        "title": "श्लोक १८: कोशातकादि",
        "cols": [["पंक्ति १: सूची (क्रिया नहीं)", ["कोशातक", "आरग्वध", "देवदारु", "मूर्वा", "अश्वदंष्ट्रा", "कुटज", "अर्क", "पाठा"]],
                 ["पंक्ति २: जल में पकाकर", ["कुलत्थ", "बृहती", "उस रस के दस प्रसृत"]]],
    },
    ("21", "diagram"): {
        "file": "ka4-dashamula-21.svg",
        "alt": ("Two columns for verse 21: line 1 the ten roots with a pala as share, crushed, washed, and eight fruits; "
                "line 2 bilva, yava, ankola, kulattha, dhanya, and the fruits measured by prasrita"),
        "type": "split",
        "title": "श्लोक २१: पुनर्नवादि सूची आगे",
        "cols": [["पंक्ति १", ["द्विपंचमूल", "पल के अंश वाले", "कुचले, धोए", "आठ फल"]],
                 ["पंक्ति २", ["बिल्व", "यव", "अंकोल", "कुलत्थ", "धान्य", "फल: प्रसृत के माप"]]],
    },
    ("22", "chain"): {
        "file": "ka4-ksirapaka-22.svg",
        "alt": ("Chain of four steps for verse 22: milk with two adhakas of water; prepared; that milk remaining; strained through a clean cloth"),
        "type": "chain",
        "title": "श्लोक २२: दूध की तैयारी",
        "steps": ["दूध + दो आढक जल", "सिद्ध किया", "वही दूध शेष रहे", "स्वच्छ वस्त्र से छाना"],
    },
    ("23", "diagram"): {
        "file": "ka4-prasriti-23.svg",
        "alt": ("Flowchart of verse 23: joined with pastes, ajwain and madana; neither too hot nor too cold; smeared with jaggery "
                "and rock salt; honey, oil and fresh ghee; joined by a set of three prasritis"),
        "type": "mermaid",
        "code": ('flowchart TD\n'
                 '  A["कल्क · यवानी · मदन से युक्त"] --> B["न अधिक गरम, न ठण्डा"]\n'
                 '  B --> C["गुड़ और सैन्धव से लिप्त"]\n'
                 '  C --> D["शहद · तेल · नया घी"]\n'
                 '  D --> E["तीन प्रसृति से युक्त"]\n'),
    },
}
