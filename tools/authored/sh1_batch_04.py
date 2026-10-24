from helpers import mcq, match, order, fill, multi, accepts


def T(q, teaches):
    q["teaches"] = teaches
    return q


AUTHORED = {}

# ---------------------------------------------------------------- unit 41
AUTHORED["41"] = {
    "title": "गुह्यप्रतिषेधेन चोभयानपि",
    "question": "What does unit 41 add to the treatment of unit 40, and with which verb is it read?",
    "rule": ("And with the remedy for the private parts (guhya-pratiṣedha), also both: the card reads this short line as "
             "continuing unit 40, whose verb साधयेत् (one should treat) is carried over."),
    "limits": ("The line has no verb of its own; that it continues unit 40 is the data's reading ('appears to'). "
               "उभयान् (both) is not explained: the two kinds of faults, of śukra and of ārtava, are a presumption only. "
               "No remedy for the private parts is named here."),
    "explain_hi": ("यह बहुत छोटी गद्य-पंक्ति है और इसकी अपनी कोई क्रिया नहीं है। कार्ड इसे इकाई ४० का आगे का भाग पढ़ता है, "
                   "जहाँ ‘साधयेत्’ (चिकित्सा करे) आया है। अर्थ: और गुह्य (गुप्तांग) के प्रतिषेध यानी उपचार से, दोनों को भी। "
                   "‘उभयान्’ (दोनों को) किनके लिए है, पंक्ति नहीं बताती; सम्भवतः शुक्र और आर्तव के दोष, पर यह कहा नहीं गया। "
                   "‘गुह्यप्रतिषेधेन’ तृतीया है: ‘उपचार से’।"),
    "hook": "इकाई ४० की ‘साधयेत्’ यहाँ भी: गुह्य के उपचार से, दोनों को भी।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 41, with what further means is the treatment done?",
            ("The remedy for the private parts", "गुह्यप्रतिषेधेन: with the remedy (प्रतिषेध) for the private parts (गुह्य)."),
            [("A decoction enema of bilva", "Bilva in an āsthāpana comes in unit 43, not here."),
             ("A drink of ghee with rock salt", "The ghee drink with saindhava is unit 42."),
             ("Purgation with trivṛt powder", "Trivṛt powder with ghee is the purgation of unit 46.")],
            "Unit 41 adds: and with the remedy for the private parts, also both.",
            "गुह्य = private parts; प्रतिषेध = remedy."),
        order(1, "Put the words of unit 41 in their printed order.",
              ["गुह्यप्रतिषेधेन", "च", "उभयान्", "अपि च"],
              "With the remedy for the private parts, and, both, also and.",
              "गुह्यप्रतिषेधेन → च → उभयान् → अपि च."),
        T(match(2, "Match each word of unit 41 to its meaning on the card.",
                [["गुह्य", "the private parts"], ["प्रतिषेध", "remedy"], ["उभयान्", "both"], ["अपि", "also"]],
                "Four words carry the line: the remedy for the private parts, also both.",
                "गुह्य, प्रतिषेध, उभयान्, अपि.", role="extend"),
          "उभयान् is masculine accusative plural: both (the object of the carried-over verb)."),
        mcq("discriminate", 3, "Which split of चोभयानपि is right?",
            ("च + उभयान् + अपि", "अ + उ → ओ gives चो; उभयान् + अपि simply join."),
            [("चो + भयान् + अपि", "चो is not a word, and भयान् is not the card's word."),
             ("च + ओभयान् + अपि", "ओभयान् is not a word; the card has उभयान्."),
             ("च + उभयान + पि", "पि is not a word; अपि keeps its अ after उभयान्.")],
            "च (and) + उभयान् (both) + अपि (also).",
            "अ + उ → ओ."),
        mcq("apply", 4, "On the card's reading, which verb completes unit 41?",
            ("साधयेत्, from unit 40", "The data reads the line as continuing unit 40, whose verb is साधयेत्."),
            [("ईक्षेत, from unit 14", "ईक्षेत (look to) belongs to the gulma advice of unit 14."),
             ("पिबेत्, from unit 55", "Unit 41 is read with the line before it, not a later one."),
             ("A verb printed in unit 41", "Unit 41 has no verb of its own.")],
            "Unit 41 has no verb; the verb साधयेत् (one should treat) is carried over from unit 40.",
            "Elliptical line: the verb comes from unit 40."),
        T(mcq("transfer", 5, "By the rule of चोभयानपि, how is च + उदकम् written when joined?",
              ("चोदकम्", "अ + उ → ओ, as in च + उभयान् → चोभयान्."),
              [("चौदकम्", "अ + उ gives ओ, not औ."),
               ("चादकम्", "अ + उ does not give आ."),
               ("चवुदकम्", "No व् is put between अ and उ.")],
              "च + उभयान् → चोभयान्; so च + उदकम् → चोदकम्.",
              "अ + उ → ओ."),
          "A final अ before उ merges with it into ओ."),
    ],
}

# ---------------------------------------------------------------- unit 42
AUTHORED["42"] = {
    "title": "वातिके शुक्रदोषे",
    "question": "What drink does unit 42 give for the Vāta-type fault of śukra, and how is it prepared?",
    "rule": ("In the Vāta-type fault (doṣa) of śukra: drinking of ghee cooked with sukta (a sour fermented liquid), saindhava "
             "(rock salt) and sour fruit, with yava-kṣāra (kṣāra of barley) as the addition (prativāpa)."),
    "limits": ("सुक्तसैंधवफलाम्ल is read as three items (sukta, saindhava, sour fruit); फलाम्ल could also be one sour fruit, "
               "so no question counts its items. No dose, stage or time is given. doṣa here is the fault of the semen."),
    "explain_hi": ("यहाँ से शुक्र और आर्तव के दोषों की चिकित्सा की सूची शुरू होती है। वातिक शुक्रदोष में घी का पान बताया है। "
                   "यह घी सुक्त (खट्टा किण्वित द्रव), सैन्धव यानी सेंधा नमक (मानक) और खट्टे फल के साथ पकाया जाता है। "
                   "उसमें यवक्षार, यानी यव (जौ, मानक) का क्षार, प्रतिवाप के रूप में डाला जाता है; प्रतिवाप = बाद में मिलाई जाने वाली वस्तु। "
                   "‘सिद्धम्’ का सम्बन्ध अन्तिम शब्द ‘सर्पिः’ (घी) से है। मात्रा या समय नहीं बताया गया।"),
    "hook": "वात का शुक्रदोष: खट्टा-नमकीन पका घी, ऊपर से यवक्षार।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 42, what is drunk in the Vāta-type fault of śukra?",
            ("Ghee (सर्पिः)", "सर्पिःपानम्: the drinking of ghee."),
            [("Milk (क्षीरम्)", "Milk is not drunk in this unit."),
             ("Oil (तैलम्)", "Oil comes in the enemas of unit 43."),
             ("Honey (मधु)", "Honey is not named in this unit.")],
            "The line ends with सर्पिःपानम्, the drinking of ghee.",
            "सर्पिः = ghee; पान = drinking."),
        order(1, "Put these words of unit 42 in their printed order.",
              ["वातिके", "शुक्रदोषे", "सुक्तसैंधवफलाम्लसिद्धं", "यवक्षारप्रतिवापं", "सर्पिःपानं"],
              "The case (Vāta-type śukra fault), then what the ghee is cooked with, the addition, and last the ghee drink.",
              "वातिके → शुक्रदोषे → …सिद्धं → यवक्षारप्रतिवापं → सर्पिःपानं."),
        T(match(2, "Match each word of unit 42 to its meaning on the card.",
                [["सुक्त", "a sour fermented liquid"], ["सैंधव", "rock salt"], ["यवक्षार", "kṣāra of barley"],
                 ["प्रतिवाप", "a substance added"], ["सर्पिः", "ghee"]],
                "These five words carry the preparation: what it is cooked with, what is added, and what is drunk.",
                "सुक्त, सैंधव, यवक्षार, प्रतिवाप, सर्पिः.", role="extend"),
          "प्रतिवाप = a substance added to the preparation; here it is यवक्षार."),
        mcq("discriminate", 3, "In unit 42, what is cooked (सिद्धम्) with sukta, saindhava and sour fruit?",
            ("The ghee that is drunk", "सिद्धम् agrees with सर्पिः, named only in the last word."),
            [("The barley kṣāra itself", "यवक्षार is the addition, not what is cooked."),
             ("An oil for the enema", "No oil or enema is in this unit."),
             ("The semen with the fault", "शुक्रदोषे names the case, not the thing cooked.")],
            "The ghee (सर्पिः) is cooked with them; यवक्षार is then added to it.",
            "सिद्धम् … सर्पिः: the ghee is cooked."),
        multi("apply", 4, "Which does unit 42 name for the Vāta-type fault of śukra?",
              [("Sukta", "Right: सुक्त is the first of the cooking items."),
               ("Saindhava (rock salt)", "Right: सैंधव."),
               ("Yava-kṣāra as the addition", "Right: यवक्षारप्रतिवापम्."),
               ("Bilva (bael)", "Bilva comes in unit 43's āsthāpana."),
               ("Trivṛt powder", "Trivṛt is the purgation of unit 46.")],
              [0, 1, 2],
              "The ghee is cooked with sukta, saindhava and sour fruit, with yava-kṣāra added.",
              "सुक्त, सैंधव, फलाम्ल; यवक्षार प्रतिवाप."),
        T(mcq("transfer", 5, "Built like वातिके शुक्रदोषे, what does the invented पैत्तिके ज्वरे mean?",
              ("In the Pitta-type fever", "Adjective and noun both in the locative: in the Pitta-type fever."),
              [("From the Pitta-type fever", "'From' would need the ablative, not the locative -ए."),
               ("The fever causes Pitta", "There is no verb; both words are locative."),
               ("For the Pitta-type fever", "'For' would need the dative, not the locative -ए.")],
              "वातिके शुक्रदोषे = in the Vāta-type fault of śukra; पैत्तिके ज्वरे = in the Pitta-type fever.",
              "Adjective + noun in the locative = 'in (the case of) …'."),
          "A locative pair like वातिके शुक्रदोषे names the case in which a treatment is used."),
    ],
}

# ---------------------------------------------------------------- unit 43
AUTHORED["43"] = {
    "title": "बिल्वविदारीक्षीरयुक्तमास्थापनम्",
    "question": "Which two enemas does unit 43 describe, and what goes into each?",
    "rule": ("Āsthāpana (decoction enema) joined with bilva (bael), vidārī and milk; and oil cooked with madhuka and "
             "bhadradāru as anuvāsana (oil enema)."),
    "limits": ("Two printed lines joined; no verb of giving is stated. Vidārī (Pueraria tuberosa), madhuka (licorice) and "
               "bhadradāru (deodar) are probable identifications; bilva = Aegle marmelos is standard. The printed आस्थपनं "
               "(short a) is possibly आस्थापनम्. Read in sequence with the Vāta-type list."),
    "explain_hi": ("इस इकाई में दो छपी पंक्तियाँ जुड़ी हैं और दोनों में क्रिया नहीं है। पहली: बिल्व यानी बेल (मानक), विदारी (सम्भवतः विदारीकन्द) "
                   "और दूध से युक्त आस्थापन, यानी काढ़े की बस्ति (एनिमा)। दूसरी: मधुक (सम्भवतः मुलेठी) और भद्रदारु (सम्भवतः देवदारु) "
                   "के साथ पकाया तेल, अनुवासन यानी तेल की बस्ति। यहाँ ‘बस्ति’ एनिमा है, मूत्राशय नहीं। "
                   "छपा ‘आस्थपनं’ सम्भवतः ‘आस्थापनं’ है।"),
    "hook": "काढ़े की बस्ति में बेल-विदारी-दूध; तेल की बस्ति में मधुक-भद्रदारु।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 43, as what is the oil cooked with madhuka and bhadradāru used?",
            ("As anuvāsana (oil enema)", "तैलम् अनुवासनम्: the oil, as anuvāsana."),
            [("As a drink with rock salt", "The ghee drink with saindhava is unit 42."),
             ("As a purgation (vireka)", "Purgation is not named in this unit."),
             ("As uttarabasti (injection)", "Uttarabasti comes in unit 44, not here.")],
            "Oil cooked with madhuka and bhadradāru, as anuvāsana (oil enema).",
            "अनुवासन = oil enema."),
        order(1, "Put these words of unit 43 in their printed order.",
              ["बिल्वविदारीक्षीरयुक्तम्", "आस्थापनम्", "मधुकभद्रदारुसिद्धम्", "तैलम्", "अनुवासनम्"],
              "Line 1: what the āsthāpana is joined with, then आस्थापनम्. Line 2: what the oil is cooked with, the oil, its use.",
              "…युक्तम् आस्थापनम् | …सिद्धम् तैलम् अनुवासनम्."),
        T(match(2, "Match each word of unit 43 to its meaning on the card.",
                [["बिल्व", "bael"], ["क्षीर", "milk"], ["आस्थापन", "decoction enema"], ["तैल", "oil"],
                 ["अनुवासन", "oil enema"]],
                "The two enemas and what goes into them.",
                "बिल्व, क्षीर, आस्थापन, तैल, अनुवासन.", role="extend"),
          "Āsthāpana is the decoction enema; anuvāsana is the oil enema."),
        mcq("discriminate", 3, "Which split of तैलमनुवासनम् is right?",
            ("तैलम् + अनुवासनम्", "म् + a vowel simply join: तैलम् + अनुवासनम् → तैलमनुवासनम्."),
            [("तैल + मनुवासनम्", "मनुवासनम् is not a word of the card."),
             ("तैलम + अनुवासनम्", "अ + अ would give आ: तैलमानुवासनम्."),
             ("तैलमनु + वासनम्", "तैलमनु is not a word; तैलम् is oil.")],
            "तैलम् (oil) + अनुवासनम् (oil enema).",
            "Final म् before a vowel joins it in writing."),
        mcq("apply", 4, "In unit 43, which preparation is joined with milk?",
            ("The āsthāpana (decoction enema)", "बिल्वविदारीक्षीरयुक्तम् आस्थापनम्."),
            [("The oil of the anuvāsana", "The oil is cooked with madhuka and bhadradāru, not milk."),
             ("The ghee drink of unit 42", "That ghee is cooked with sukta and rock salt."),
             ("The madhuka and bhadradāru", "These go into the oil; milk is not named with them.")],
            "Milk joins bilva and vidārī in the āsthāpana; the oil is cooked with madhuka and bhadradāru.",
            "क्षीरयुक्त … आस्थापनम्."),
        T(mcq("transfer", 5, "Built like क्षीरयुक्तम् आस्थापनम्, what does the invented घृतयुक्तम् अन्नम् mean?",
              ("Food joined with ghee", "-युक्त = joined with: घृतयुक्त = joined with ghee."),
              [("Ghee taken from food", "-युक्त means joined with, not taken from."),
               ("Food that has no ghee", "That would need a negative such as घृतहीन."),
               ("Ghee cooked into food", "Cooked would be -सिद्ध, not -युक्त.")],
              "क्षीरयुक्त = joined with milk; घृतयुक्त = joined with ghee.",
              "X-युक्त = joined with X."),
          "X-युक्त means joined with X; X-सिद्ध means cooked with X."),
    ],
}

# ---------------------------------------------------------------- unit 44
AUTHORED["44"] = {
    "title": "क्षीरकुलीररससिद्धं तैलम्",
    "question": "What oil does unit 44 give as uttarabasti?",
    "rule": ("Oil cooked with milk and the juice (rasa) of kulīra (probably crab), as uttarabasti (an injection through the "
             "urinary or genital passage)."),
    "limits": ("The printed रसरस is possibly a doubled रस (print doubling); the sense is not changed. Kulīra as crab is not "
               "certain (it can be a plant name). The route of the uttarabasti is not stated here. No verb."),
    "explain_hi": ("दूध और कुलीर (सम्भवतः केकड़ा) के रस से पकाया हुआ तेल उत्तरबस्ति के रूप में बताया गया है। "
                   "उत्तरबस्ति मूत्रमार्ग (पुरुष में) या योनिमार्ग (स्त्री में) से दी जाने वाली बस्ति है; यहाँ मार्ग नहीं बताया। "
                   "छपा ‘रसरस’ सम्भवतः ‘रस’ का दोहराव है। कुलीर कुछ सूचियों में पौधे का नाम भी है, इसलिए ‘केकड़ा’ निश्चित नहीं।"),
    "hook": "दूध और कुलीर-रस में पका तेल: उत्तरबस्ति।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 44, as what is the oil cooked with milk and kulīra juice used?",
            ("As uttarabasti", "तैलम् उत्तरबस्तिः: the oil, as uttarabasti."),
            [("As anuvāsana", "Anuvāsana is the oil of unit 43."),
             ("As a drink", "No drinking is named in unit 44."),
             ("As āsthāpana", "Āsthāpana is a decoction enema, in unit 43.")],
            "Oil cooked with milk and kulīra juice, as uttarabasti.",
            "उत्तरबस्ति = injection through the urinary or genital passage."),
        order(1, "Put the steps of unit 44 in the card's order.",
              ["दूध और कुलीर का रस", "उनसे पकाया तेल", "उत्तरबस्ति के रूप में"],
              "Milk and kulīra juice, the oil cooked with them, its use as uttarabasti.",
              "क्षीर-कुलीररस → सिद्ध तैल → उत्तरबस्तिः."),
        T(match(2, "Match each word of unit 44 to its meaning on the card.",
                [["क्षीर", "milk"], ["कुलीर", "probably crab"], ["रस", "juice"], ["तैल", "oil"],
                 ["उत्तरबस्ति", "injection through the urinary or genital passage"]],
                "Five words make the line: what the oil is cooked with, and its use.",
                "क्षीर, कुलीर, रस, तैल, उत्तरबस्ति.", role="extend"),
          "Uttarabasti is given through the urinary passage (man) or the genital passage (woman)."),
        mcq("discriminate", 3, "Which split of तैलमुत्तरबस्तिः is right?",
            ("तैलम् + उत्तरबस्तिः", "म् + the vowel उ join in writing: तैलमुत्तरबस्तिः."),
            [("तैल + मुत्तरबस्तिः", "मुत्तरबस्तिः is not a word of the card."),
             ("तैलमुत् + तरबस्तिः", "तरबस्तिः is not a word; the term is उत्तरबस्तिः."),
             ("तैलमु + उत्तरबस्तिः", "तैलमु is not a word; the word is तैलम्.")],
            "तैलम् (oil) + उत्तरबस्तिः (uttarabasti).",
            "Final म् before a vowel joins it in writing."),
        mcq("apply", 4, "Does unit 44 say by which passage this uttarabasti is given?",
            ("No, it gives no route here", "The note: the text gives no route in this line."),
            [("Yes, through the urinary passage", "The line names no passage."),
             ("Yes, through the genital passage", "The line names no passage."),
             ("Yes, through the mouth", "Uttarabasti is never given by mouth; nor does the line say so.")],
            "Uttarabasti can go through the urinary or the genital passage, but unit 44 does not say which.",
            "No route is stated in unit 44."),
        T(mcq("transfer", 5, "Built like क्षीर…सिद्धं तैलम्, what does the invented क्षीरसिद्धं घृतम् mean?",
              ("Ghee cooked with milk", "-सिद्ध = cooked with: क्षीरसिद्ध = cooked with milk."),
              [("Milk cooked with ghee", "The compound क्षीरसिद्ध describes घृतम्, so ghee is cooked."),
               ("Ghee mixed after milk", "-सिद्ध means cooked with, not mixed after."),
               ("Milk turned into ghee", "-सिद्ध does not mean turned into.")],
              "क्षीरकुलीररससिद्धं तैलम् = oil cooked with milk and kulīra juice; क्षीरसिद्धं घृतम् = ghee cooked with milk.",
              "X-सिद्धम् Y = Y cooked with X."),
          "X-सिद्ध before a noun means that noun is cooked with X."),
    ],
}

# ---------------------------------------------------------------- unit 45
AUTHORED["45"] = {
    "title": "पैत्तिके सर्पिःपानम्",
    "question": "What ghee drink does unit 45 give in the Pitta-type (fault of śukra)?",
    "rule": ("In the Pitta-type (fault of śukra, understood): drinking of ghee cooked with kāṇḍekṣu, śvadaṃṣṭrā (puncture vine) "
             "and guḍūcī, with mūrvā and madhuka as the addition (pratīvāpa)."),
    "limits": ("शुक्रदोषे is understood from unit 42. The printed कांडेंक्षु has an extra ं (possible correction काण्डेक्षु); "
               "kāṇḍekṣu (a cane) is not identified and mūrvā is disputed, so no question rests on them. "
               "Śvadaṃṣṭrā = Tribulus terrestris and guḍūcī = Tinospora cordifolia are standard."),
    "explain_hi": ("पैत्तिक (शुक्रदोष) में भी घी का पान है; ‘शुक्रदोषे’ इकाई ४२ से समझा जाता है। "
                   "घी काण्डेक्षु, श्वदंष्ट्रा यानी गोखरू (मानक) और गुडूची यानी गिलोय (मानक) के साथ पकाया जाता है। "
                   "उसमें मूर्वा और मधुक प्रतीवाप के रूप में मिलाए जाते हैं; ‘प्रतीवाप’ वही है जो इकाई ४२ का ‘प्रतिवाप’। "
                   "काण्डेक्षु की पहचान नहीं है और मूर्वा की पहचान विवादित है।"),
    "hook": "पित्त का शुक्रदोष: गोखरू-गिलोय में पका घी, ऊपर से मूर्वा-मधुक।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 45, which two are the addition (pratīvāpa) to the ghee?",
            ("Mūrvā and madhuka", "मूर्वामधुकप्रतीवापम्: mūrvā and madhuka are the addition."),
            [("Guḍūcī and śvadaṃṣṭrā", "These are cooked into the ghee, not added."),
             ("Yava-kṣāra and salt", "Yava-kṣāra is the addition of unit 42."),
             ("Pippalī and madhuka", "Pippalī with madhuka is the addition of unit 49.")],
            "The ghee is cooked with kāṇḍekṣu, śvadaṃṣṭrā and guḍūcī; mūrvā and madhuka are added.",
            "प्रतीवाप = the substance added."),
        order(1, "Put these words of unit 45 in their printed order.",
              ["पैत्तिके", "कांडेंक्षुश्वदंष्ट्रागुडूचीसिद्धं", "मूर्वामधुकप्रतीवापं", "सर्पिःपानं"],
              "The case, what the ghee is cooked with, what is added, the ghee drink.",
              "पैत्तिके → …सिद्धं → …प्रतीवापं → सर्पिःपानं."),
        T(match(2, "Match each word of unit 45 to its meaning on the card.",
                [["पैत्तिक", "Pitta-type"], ["श्वदंष्ट्रा", "puncture vine (Tribulus terrestris)"],
                 ["गुडूची", "Tinospora cordifolia"], ["प्रतीवाप", "addition"], ["सर्पिःपान", "drinking of ghee"]],
                "The sure words of the line: the case, two cooking herbs, the addition and the drink.",
                "पैत्तिक, श्वदंष्ट्रा, गुडूची, प्रतीवाप, सर्पिःपान.", role="extend"),
          "Śvadaṃṣṭrā (gokṣura) is Tribulus terrestris; guḍūcī is Tinospora cordifolia (both standard)."),
        mcq("discriminate", 3, "In unit 45, which is cooked into the ghee rather than added to it?",
            ("Guḍūcī", "गुडूची stands in the …सिद्धम् compound: the ghee is cooked with it."),
            [("Mūrvā", "मूर्वा stands in the …प्रतीवापम् compound: it is added."),
             ("Madhuka", "मधुक stands in the …प्रतीवापम् compound: it is added."),
             ("Yava-kṣāra", "Yava-kṣāra belongs to unit 42, not unit 45.")],
            "-सिद्धम् names what the ghee is cooked with; -प्रतीवापम् names what is added.",
            "…सिद्धम् = cooked with; …प्रतीवापम् = with … as the addition."),
        multi("apply", 4, "Which plants does unit 45 name?",
              [("Śvadaṃṣṭrā (puncture vine)", "Right: श्वदंष्ट्रा, cooked into the ghee."),
               ("Guḍūcī", "Right: गुडूची, cooked into the ghee."),
               ("Madhuka", "Right: मधुक, part of the addition."),
               ("Bilva (bael)", "Bilva is in unit 43's āsthāpana."),
               ("Āmalaka", "Āmalaka is in unit 49's decoction.")],
              [0, 1, 2],
              "Unit 45 names kāṇḍekṣu, śvadaṃṣṭrā, guḍūcī, mūrvā and madhuka.",
              "श्वदंष्ट्रा, गुडूची; मूर्वा, मधुक."),
        T(mcq("transfer", 5, "In the invented वातिके ज्वरे घृतम्, पैत्तिके क्षीरम्, with what is पैत्तिके understood?",
              ("With ज्वरे, from the first part", "As शुक्रदोषे is carried into unit 45, ज्वरे is carried to पैत्तिके."),
              [("With घृतम्, from the first part", "पैत्तिके is locative; घृतम् is not, so they cannot agree."),
               ("With क्षीरम्, which follows it", "क्षीरम् is what is given, not the case."),
               ("With nothing; it stands alone", "An adjective like पैत्तिके needs its noun, carried over.")],
              "पैत्तिके (in the Pitta-type) carries the noun of the first part: पैत्तिके (ज्वरे).",
              "A repeated noun is often left out and understood from before."),
          "In such lists the noun (शुक्रदोषे, ज्वरे) is said once and understood with the next adjective."),
    ],
}

# ---------------------------------------------------------------- unit 46
AUTHORED["46"] = {
    "title": "त्रिवृच्चूर्णः सघृतो विरेकः",
    "question": "What purgation does unit 46 give?",
    "rule": "Powder of trivṛt (turpeth, Operculina turpethum) with ghee is the purgation (vireka, virecana).",
    "limits": ("A nominal sentence: there is no verb; 'is' is only the natural English. The line does not name a doṣa; the card "
               "reads it in sequence after the Pitta-type ghee of unit 45. The printed ':' is read as visarga. No dose is given."),
    "explain_hi": ("त्रिवृत् यानी निशोथ (मानक) का चूर्ण, घी के साथ, विरेचन (विरेक) है। "
                   "वाक्य बिना क्रिया का है; ‘है’ केवल अनुवाद में आता है। "
                   "यह पंक्ति किसी दोष का नाम नहीं लेती; क्रम से इसे इकाई ४५ के पैत्तिक उपचार के बाद पढ़ा गया है। "
                   "छपाई में विसर्ग ‘:’ के रूप में छपा है।"),
    "hook": "निशोथ का चूर्ण, घी के साथ: विरेचन।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 46, what is the purgation (vireka)?",
            ("Trivṛt powder with ghee", "त्रिवृच्चूर्णः सघृतः: trivṛt powder with ghee."),
            [("Dantī powder with oil", "Dantī powder licked with oil is unit 51."),
             ("Madanaphala decoction", "That decoction is the emesis of unit 50."),
             ("Yava-kṣāra with ghee", "Yava-kṣāra is the addition of unit 42.")],
            "Powder of trivṛt with ghee is the purgation.",
            "विरेक = purgation."),
        order(1, "Put the words of unit 46 in their order (with त्रिवृच्चूर्णः split).",
              ["त्रिवृत्", "चूर्णः", "सघृतः", "विरेकः"],
              "Trivṛt, powder, with ghee, purgation.",
              "त्रिवृत् → चूर्णः → सघृतः → विरेकः."),
        T(fill(2, "The word of unit 46 for purgation is ____ (type it in Devanagari or in English letters, e.g. dharma).",
               accepts("विरेकः", None, "विरेक"),
               "विरेकः = purgation (virecana), the last word of the line.",
               "विरेक means purgation, the same as virecana.", "विरेक = purgation."), "विरेक is purgation (virecana)."),
        mcq("discriminate", 3, "Which split of त्रिवृच्चूर्णः is right?",
            ("त्रिवृत् + चूर्णः", "त् before च becomes च्: त्रिवृत् + चूर्णः → त्रिवृच्चूर्णः."),
            [("त्रिवृच् + चूर्णः", "त्रिवृच् is not the word; the drug is त्रिवृत्."),
             ("त्रिवृ + च्चूर्णः", "च्चूर्णः is not a word."),
             ("त्रिवृत् + च + ऊर्णः", "No च (and) stands here; चूर्णः is powder.")],
            "त्रिवृत् (turpeth) + चूर्णः (powder).",
            "त् + च → च्च."),
        mcq("apply", 4, "Why is सघृतः printed as सघृतो before विरेकः?",
            ("अः before a voiced sound becomes ओ", "व is voiced, so सघृतः + विरेकः → सघृतो विरेकः."),
            [("अः before any consonant becomes ओ", "Before a voiceless sound like त it becomes स्, not ओ."),
             ("The visarga is dropped by mistake", "The change is regular sandhi, not a misprint."),
             ("ओ marks the dual number", "सघृतः is singular; ओ here comes from sandhi.")],
            "Final अः before a voiced consonant (here व) becomes ओ.",
            "अः + voiced consonant → ओ."),
        T(mcq("transfer", 5, "By the rule of त्रिवृच्चूर्णः, how is तत् + च written when joined?",
              ("तच्च", "त् before च becomes च्, as in त्रिवृत् + चूर्णः."),
              [("तद्च", "त् before च does not become द्."),
               ("तत्च", "त् does not stay before च; it becomes च्."),
               ("तन्च", "त् becomes न् only before a nasal.")],
              "त्रिवृत् + चूर्णः → त्रिवृच्चूर्णः; so तत् + च → तच्च.",
              "त् + च → च्च."),
          "A final त् before च becomes च्."),
    ],
}

# ---------------------------------------------------------------- unit 47
AUTHORED["47"] = {
    "title": "पयस्याश्रीपर्णीसिद्धम्",
    "question": "What āsthāpana does unit 47 give?",
    "rule": "Āsthāpana (decoction enema) cooked with payasyā and śrīparṇī (probably gambhārī, Gmelina arborea), joined with milk.",
    "limits": ("Payasyā's identity is disputed, so no question rests on it; śrīparṇī as Gmelina arborea is probable. No verb is "
               "stated. The line does not name a doṣa; it is read in sequence with the Pitta-type list."),
    "explain_hi": ("इस पंक्ति में फिर आस्थापन यानी काढ़े की बस्ति है। वह पयस्या और श्रीपर्णी (सम्भवतः गम्भारी) के साथ पकाई जाती है और दूध से युक्त होती है। "
                   "‘सिद्धम्’ और ‘युक्तम्’ दोनों आस्थापन के विशेषण हैं। पयस्या की पहचान विवादित है। "
                   "पंक्ति दोष का नाम नहीं लेती; क्रम से पैत्तिक सूची में पढ़ी गई है।"),
    "hook": "पयस्या-श्रीपर्णी में पकी, दूध मिली: काढ़े की बस्ति।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 47, with what is the āsthāpana joined?",
            ("With milk", "क्षीरयुक्तम् आस्थापनम्: the āsthāpana joined with milk."),
            [("With oil", "Oil is not named in unit 47."),
             ("With honey", "Honey is not named in unit 47."),
             ("With rock salt", "Rock salt belongs to unit 42.")],
            "Āsthāpana cooked with payasyā and śrīparṇī, joined with milk.",
            "क्षीरयुक्त = joined with milk."),
        order(1, "Put the parts of unit 47 in their printed order.",
              ["पयस्या", "श्रीपर्णी", "सिद्धम्", "क्षीरयुक्तम्", "आस्थापनम्"],
              "Two drugs, cooked, joined with milk, āsthāpana.",
              "पयस्या → श्रीपर्णी → सिद्धम् → क्षीरयुक्तम् → आस्थापनम्."),
        T(match(2, "Match each word of unit 47 to its meaning on the card.",
                [["श्रीपर्णी", "probably gambhārī (Gmelina arborea)"], ["सिद्ध", "cooked"], ["क्षीर", "milk"],
                 ["युक्त", "joined with"], ["आस्थापन", "decoction enema"]],
                "Five words carry the line; payasyā is left out because its identity is disputed.",
                "श्रीपर्णी, सिद्ध, क्षीर, युक्त, आस्थापन.", role="extend"),
          "Both सिद्धम् (cooked) and युक्तम् (joined) describe the āsthāpana."),
        mcq("discriminate", 3, "Which split of क्षीरयुक्तमास्थापनम् is right?",
            ("क्षीरयुक्तम् + आस्थापनम्", "म् + आ join in writing: क्षीरयुक्तमास्थापनम्."),
            [("क्षीरयुक्त + मास्थापनम्", "मास्थापनम् is not a word of the card."),
             ("क्षीरयुक्तमा + स्थापनम्", "क्षीरयुक्तमा is not a word."),
             ("क्षीरयुक्त + आस्थापनम्", "अ + आ would give आ with no म्: क्षीरयुक्तास्थापनम्.")],
            "क्षीरयुक्तम् (joined with milk) + आस्थापनम् (decoction enema).",
            "Final म् before a vowel joins it in writing."),
        mcq("apply", 4, "In unit 47, what do सिद्धम् and युक्तम् both describe?",
            ("The āsthāpana", "Both are neuter and qualify आस्थापनम्."),
            [("The milk alone", "Milk is inside the compound क्षीरयुक्तम्; it is not described."),
             ("The payasyā plant", "Payasyā is a member of the compound, not the thing described."),
             ("An oil enema", "No oil is named in unit 47.")],
            "The āsthāpana is cooked (सिद्धम्) with the two drugs and joined (युक्तम्) with milk.",
            "सिद्धम्, युक्तम् → आस्थापनम्."),
        T(mcq("transfer", 5, "Built like पयस्याश्रीपर्णीसिद्धम्, what does the invented दधिमधुयुक्तम् अन्नम् mean?",
              ("Food joined with curd and honey", "दधि + मधु is a pair (and), then -युक्त = joined with."),
              [("Curd joined with honey food", "अन्नम् is the thing described; दधिमधु is what it is joined with."),
               ("Food cooked from curd only", "Both दधि and मधु are named, and -युक्त is not cooked."),
               ("Honey joined with curd food", "The noun described is अन्नम्, food.")],
              "पयस्या + श्रीपर्णी are the pair with -सिद्ध; दधि + मधु are the pair with -युक्त.",
              "X-Y-युक्तम् Z = Z joined with X and Y."),
          "A pair of names inside a compound before -सिद्ध or -युक्त means 'with X and Y'."),
    ],
}

# ---------------------------------------------------------------- unit 48
AUTHORED["48"] = {
    "title": "मधुकमुद्गपर्णीसिद्धं तैलम्",
    "question": "What oil does unit 48 give, and in which two ways is it used?",
    "rule": "Oil cooked with madhuka and mudgaparṇī (probably Phaseolus trilobus), as anuvāsana (oil enema) and as uttarabasti.",
    "limits": ("No verb is stated. Mudgaparṇī as Phaseolus trilobus (Vigna trilobata) is probable. The line does not name a doṣa; "
               "it is read in sequence with the Pitta-type list. No route or dose is given."),
    "explain_hi": ("मधुक और मुद्गपर्णी (सम्भवतः मुँगवन) के साथ पकाया हुआ तेल दो तरह काम आता है: अनुवासन यानी तेल की बस्ति, "
                   "और उत्तरबस्ति। ‘च’ (और) दोनों उपयोगों को जोड़ता है। "
                   "पंक्ति में क्रिया नहीं है और दोष का नाम भी नहीं; क्रम से पैत्तिक सूची में पढ़ी गई है।"),
    "hook": "एक तेल, दो काम: अनुवासन भी, उत्तरबस्ति भी।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 48, in which two ways is the oil used?",
            ("As anuvāsana and uttarabasti", "तैलम् अनुवासनम् उत्तरबस्तिः च."),
            [("As a drink and as purgation", "Neither drinking nor purgation is named here."),
             ("As āsthāpana and emesis", "Āsthāpana is a decoction enema; emesis is unit 50."),
             ("As a wash and as a paste", "No wash or paste is named in unit 48.")],
            "The oil cooked with madhuka and mudgaparṇī is both anuvāsana and uttarabasti.",
            "अनुवासनम् … उत्तरबस्तिः च."),
        order(1, "Put these words of unit 48 in their order.",
              ["मधुकमुद्गपर्णीसिद्धम्", "तैलम्", "अनुवासनम्", "उत्तरबस्तिः", "च"],
              "What the oil is cooked with, the oil, its two uses, and च (and).",
              "…सिद्धम् → तैलम् → अनुवासनम् → उत्तरबस्तिः → च."),
        T(match(2, "Match each word of unit 48 to its meaning on the card.",
                [["मुद्गपर्णी", "probably Phaseolus trilobus"], ["सिद्ध", "cooked"], ["अनुवासन", "oil enema"],
                 ["उत्तरबस्ति", "injection through the urinary or genital passage"], ["च", "and"]],
                "Five words carry the oil, how it is made and its two uses.",
                "मुद्गपर्णी, सिद्ध, अनुवासन, उत्तरबस्ति, च.", role="extend"),
          "One oil serves two uses here, joined by च."),
        mcq("discriminate", 3, "Which split of उत्तरबस्तिश्च is right?",
            ("उत्तरबस्तिः + च", "Visarga before च becomes श्: उत्तरबस्तिश्च."),
            [("उत्तरबस्ति + श्च", "श्च is not a word."),
             ("उत्तरबस्तिश् + च", "उत्तरबस्तिश् is not the word; the form is उत्तरबस्तिः."),
             ("उत्तरबस्तिस् + च", "That is not the word form; the श् comes from the visarga.")],
            "उत्तरबस्तिः (uttarabasti) + च (and).",
            "Visarga + च → श्च."),
        multi("apply", 4, "Which does unit 48 state?",
              [("The oil is cooked with madhuka and mudgaparṇī", "Right: मधुकमुद्गपर्णीसिद्धम्."),
               ("The oil is used as anuvāsana", "Right: तैलम् अनुवासनम्."),
               ("The oil is used as uttarabasti", "Right: उत्तरबस्तिः च."),
               ("The oil is joined with milk", "Milk joins the āsthāpana of unit 47, not this oil."),
               ("The oil is drunk with rock salt", "No drinking is named in unit 48.")],
              [0, 1, 2],
              "Oil cooked with madhuka and mudgaparṇī, as anuvāsana and uttarabasti.",
              "…सिद्धं तैलम् अनुवासनम् उत्तरबस्तिः च."),
        T(mcq("transfer", 5, "By the rule of उत्तरबस्तिश्च, how is रामः + च written when joined?",
              ("रामश्च", "Visarga before च becomes श्."),
              [("रामो च", "Visarga becomes ओ only before a voiced sound; च is voiceless."),
               ("रामस्च", "Before च the visarga becomes श्, not स्."),
               ("रामर्च", "Visarga after अ does not become र्.")],
              "उत्तरबस्तिः + च → उत्तरबस्तिश्च; so रामः + च → रामश्च.",
              "Visarga + च/छ → श्."),
          "A visarga before च becomes श्."),
    ],
}

# ---------------------------------------------------------------- unit 49
AUTHORED["49"] = {
    "title": "श्लैष्मिके सर्पिःपानम्",
    "question": "What ghee drink does unit 49 give in the Kapha-type (fault)?",
    "rule": ("In the Kapha-type (one): drinking of ghee cooked with a decoction (kvātha) of pāṣāṇabhedaka, aśmantaka and "
             "āmalaka, with powder of pippalī (long pepper) and madhuka as the addition."),
    "limits": ("Pāṣāṇabhedaka (Bergenia ligulata) is probable; aśmantaka is disputed, so no question rests on it; āmalaka "
               "(Phyllanthus emblica) and pippalī (Piper longum) are standard. शुक्रदोषे is understood. No dose."),
    "explain_hi": ("श्लैष्मिक यानी कफज (शुक्रदोष) में भी घी का पान है। घी पाषाणभेदक (सम्भवतः पखानभेद), अश्मन्तक (पहचान विवादित) "
                   "और आमलक यानी आँवला (मानक) के क्वाथ (काढ़े) में पकाया जाता है। "
                   "उसमें पिप्पली यानी पीपर (मानक) और मधुक का चूर्ण प्रतीवाप के रूप में मिलाया जाता है। "
                   "छपा ‘पाषाणभेदकाश्मंतक’ = पाषाणभेदक + अश्मन्तक (अ + अ → आ)।"),
    "hook": "कफ का शुक्रदोष: पत्थर-भेदक और आँवले के काढ़े में पका घी, ऊपर से पीपर-मधुक चूर्ण।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 49, in what is the ghee cooked?",
            ("A decoction of three drugs", "…आमलकक्वाथसिद्धम्: cooked with a decoction (क्वाथ)."),
            [("Milk with crab juice", "That is unit 44's oil."),
             ("Sukta with rock salt", "That is unit 42's ghee."),
             ("Oil with bhadradāru", "That is unit 43's anuvāsana.")],
            "The ghee is cooked with a decoction of pāṣāṇabhedaka, aśmantaka and āmalaka.",
            "क्वाथ = decoction."),
        order(1, "Put the names in the order of unit 49's decoction compound.",
              ["पाषाणभेदक", "अश्मन्तक", "आमलक", "क्वाथ"],
              "पाषाणभेदक, अश्मन्तक, आमलक, then क्वाथ (decoction) and सिद्धम्.",
              "पाषाणभेदक → अश्मन्तक → आमलक → क्वाथ."),
        T(match(2, "Match each word of unit 49 to its meaning on the card.",
                [["श्लैष्मिक", "Kapha-type"], ["आमलक", "emblic myrobalan"], ["पिप्पली", "long pepper"],
                 ["क्वाथ", "decoction"], ["चूर्ण", "powder"]],
                "The case, two standard drugs and the two forms of preparation.",
                "श्लैष्मिक, आमलक, पिप्पली, क्वाथ, चूर्ण.", role="extend"),
          "Āmalaka = Phyllanthus emblica; pippalī = Piper longum (both standard)."),
        mcq("discriminate", 3, "Which split of पाषाणभेदकाश्मन्तक is right?",
            ("पाषाणभेदक + अश्मन्तक", "अ + अ → आ: …भेदक + अश्मन्तक → …भेदकाश्मन्तक."),
            [("पाषाणभेदका + श्मन्तक", "श्मन्तक is not a word of the card."),
             ("पाषाणभेद + काश्मन्तक", "काश्मन्तक is not a word of the card."),
             ("पाषाणभेदक + श्मन्तक", "With श्मन्तक the long आ could not arise.")],
            "पाषाणभेदक (probably Bergenia ligulata) + अश्मन्तक (disputed).",
            "अ + अ → आ."),
        mcq("apply", 4, "In unit 49, what is put in as powder for the addition?",
            ("Pippalī and madhuka", "पिप्पलीमधुकचूर्णप्रतीवापम्."),
            [("Āmalaka and aśmantaka", "These are in the decoction the ghee is cooked with."),
             ("Mūrvā and madhuka", "Mūrvā with madhuka is the addition of unit 45."),
             ("Yava-kṣāra alone", "Yava-kṣāra is the addition of unit 42.")],
            "Powder of pippalī and madhuka is the addition (प्रतीवाप).",
            "…चूर्णप्रतीवापम् = with powder of … as the addition."),
        T(mcq("transfer", 5, "By the rule of पाषाणभेदकाश्मन्तक, how is हिम + अचलः written when joined?",
              ("हिमाचलः", "अ + अ → आ."),
              [("हिमचलः", "The second अ cannot simply vanish."),
               ("हिमेचलः", "अ + अ does not give ए."),
               ("हिमोचलः", "अ + अ does not give ओ.")],
              "पाषाणभेदक + अश्मन्तक → पाषाणभेदकाश्मन्तक; so हिम + अचलः → हिमाचलः.",
              "अ + अ → आ."),
          "Two short अ sounds meeting merge into a long आ."),
    ],
}

# ---------------------------------------------------------------- unit 50
AUTHORED["50"] = {
    "title": "मदनफलकषायो वमनम्",
    "question": "What emesis does unit 50 give?",
    "rule": "A decoction (kaṣāya) of madanaphala (Randia dumetorum) as vamana (emesis).",
    "limits": ("A nominal sentence: no verb. कषाय here means a decoction (the preparation), not the astringent taste. The line "
               "does not name a doṣa; it is read in sequence after the Kapha-type ghee of unit 49. No dose is given."),
    "explain_hi": ("मदनफल यानी मैनफल (मानक) का कषाय, यानी काढ़ा, वमन (उल्टी कराना) है। "
                   "यहाँ ‘कषाय’ बनाने की विधि (काढ़ा) के अर्थ में है, कसैले रस के अर्थ में नहीं। "
                   "वाक्य में क्रिया नहीं है। पंक्ति दोष का नाम नहीं लेती; क्रम से इसे इकाई ४९ के कफज उपचार के बाद पढ़ा गया है।"),
    "hook": "मैनफल का काढ़ा: वमन।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 50, what is used for vamana (emesis)?",
            ("A madanaphala decoction", "मदनफलकषायः वमनम्."),
            [("A trivṛt powder", "Trivṛt powder with ghee is the purgation of unit 46."),
             ("A bilva and milk enema", "That is unit 43's āsthāpana."),
             ("A pippalī powder", "Pippalī powder is the addition of unit 49.")],
            "A decoction of madanaphala as vamana.",
            "वमन = emesis."),
        match(1, "Match each word of unit 50 to its meaning on the card.",
              [["मदनफल", "Randia dumetorum"], ["कषाय", "decoction"], ["वमन", "emesis"]],
              "Three words make the whole line.",
              "मदनफल, कषाय, वमन."),
        T(fill(2, "The word of unit 50 for emesis is ____ (type it in Devanagari or in English letters, e.g. dharma).",
               accepts("वमनम्", None, "वमन"),
               "वमनम् = emesis, the last word of the line.",
               "वमन means emesis.", "वमन = emesis."), "वमन is emesis (making one vomit)."),
        mcq("discriminate", 3, "In unit 50, what does कषाय mean?",
            ("A decoction", "The note: kaṣāya here is the preparation, a decoction."),
            [("The astringent taste", "Here कषाय names the preparation, not the taste."),
             ("A dry powder", "Powder is चूर्ण, as in unit 46."),
             ("An oil enema", "An oil enema is अनुवासन.")],
            "कषाय is used here in its preparation sense: a decoction.",
            "कषाय (preparation) = decoction."),
        mcq("apply", 4, "Why is कषायः printed as कषायो before वमनम्?",
            ("अः before the voiced व becomes ओ", "व is voiced, so कषायः + वमनम् → कषायो वमनम्."),
            [("अः before a vowel becomes ओ", "Before a vowel other than अ the visarga drops; व is no vowel."),
             ("The visarga turns into र्", "After अ the visarga does not become र्."),
             ("ओ marks a dual noun", "कषायः is singular; ओ comes from sandhi.")],
            "Final अः before a voiced consonant (here व) becomes ओ.",
            "अः + voiced consonant → ओ."),
        T(mcq("transfer", 5, "Built like मदनफलकषायो वमनम्, what does the invented त्रिफलाकषायः पानम् mean?",
              ("A triphalā decoction as the drink", "X-कषायः = decoction of X; पानम् = drink."),
              [("A triphalā powder as the drink", "Powder would be चूर्ण, not कषाय."),
               ("A drink that tastes of triphalā", "कषाय here is the decoction, not a taste."),
               ("A triphalā oil as the drink", "Oil would be तैल, not कषाय.")],
              "मदनफलकषायः = decoction of madanaphala; त्रिफलाकषायः = decoction of triphalā.",
              "X-कषायः = decoction of X."),
          "X-कषाय in a list of preparations is a decoction of X."),
    ],
}

# ---------------------------------------------------------------- unit 51
AUTHORED["51"] = {
    "title": "दन्तीविडङ्गचूर्णस्तैललीढः",
    "question": "What purgation and what āsthāpana does unit 51 give?",
    "rule": ("Powder of dantī and viḍaṅga, licked with oil, is the purgation (vireka). Āsthāpana (decoction enema) strong or "
             "thick (pragāḍha) with a decoction of rājavṛkṣa (Cassia fistula) and madanaphala."),
    "limits": ("Two printed lines joined. Dantī (Baliospermum montanum) is probable; viḍaṅga (Embelia ribes) and rājavṛkṣa "
               "(Cassia fistula) are standard. Which part of rājavṛkṣa is not said, and whether फल goes with both names is undecided. "
               "No doṣa is named; read in the Kapha-type sequence."),
    "explain_hi": ("पहली पंक्ति: दन्ती (सम्भवतः दन्तीमूल) और विडङ्ग यानी वायविडंग (मानक) का चूर्ण, तेल से चाटा हुआ, विरेचन है। "
                   "दूसरी: राजवृक्ष यानी अमलतास (मानक) और मदनफल के काढ़े से प्रगाढ़ (गाढ़ा या तीव्र) आस्थापन। "
                   "राजवृक्ष का कौन-सा भाग, यह नहीं कहा; ‘फल’ दोनों नामों के साथ है या केवल मदन के, यह तय नहीं। "
                   "पंक्तियाँ दोष का नाम नहीं लेतीं; क्रम से कफज सूची में पढ़ी गई हैं।"),
    "hook": "तेल से चाटा दन्ती-विडंग: विरेचन; अमलतास-मैनफल का गाढ़ा काढ़ा: आस्थापन।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 51, how is the powder of dantī and viḍaṅga taken?",
            ("Licked with oil", "तैललीढः: licked with oil."),
            [("Drunk in milk", "No milk is named in unit 51."),
             ("Mixed with ghee", "Ghee goes with trivṛt powder in unit 46."),
             ("Boiled in water", "No boiling in water is named for the powder.")],
            "The powder of dantī and viḍaṅga, licked with oil, is the purgation.",
            "तैल-लीढ = licked with oil."),
        order(1, "Put these words of unit 51 in their printed order.",
              ["दन्तीविडङ्गचूर्णः", "तैललीढः", "विरेकः", "राजवृक्षमदनफलकषायप्रगाढम्", "आस्थापनम्"],
              "Line 1: the powder, licked with oil, the purgation. Line 2: strong with the decoction, the āsthāpana.",
              "चूर्णः → तैललीढः → विरेकः | …प्रगाढम् → आस्थापनम्."),
        T(match(2, "Match each word of unit 51 to its meaning on the card.",
                [["विडङ्ग", "Embelia ribes"], ["लीढ", "licked"], ["विरेक", "purgation"], ["राजवृक्ष", "Cassia fistula"],
                 ["प्रगाढ", "thick, strong"]],
                "Five words carry the two preparations of the unit.",
                "विडङ्ग, लीढ, विरेक, राजवृक्ष, प्रगाढ.", role="extend"),
          "प्रगाढ = thick or strong: the āsthāpana is made strong with the decoction."),
        mcq("discriminate", 3, "Which split of चूर्णस्तैललीढो is right?",
            ("चूर्णः + तैललीढः", "Visarga before त becomes स्: चूर्णस्तैल…."),
            [("चूर्णस् + तैललीढः", "चूर्णस् is not the word form; it is चूर्णः."),
             ("चूर्ण + स्तैललीढः", "स्तैललीढः is not a word."),
             ("चूर्णः + स्तैललीढः", "There is no स्त word; the स् comes from the visarga.")],
            "चूर्णः (powder) + तैललीढः (licked with oil); then तैललीढः + विरेकः → तैललीढो विरेकः.",
            "Visarga + त → स्त."),
        multi("apply", 4, "Which does unit 51 state?",
              [("The powder licked with oil is the purgation", "Right: …चूर्णः तैललीढः विरेकः."),
               ("The āsthāpana is strong with a decoction", "Right: …कषायप्रगाढम् आस्थापनम्."),
               ("It says which part of rājavṛkṣa is used", "The text does not say which part."),
               ("The decoction of madanaphala is the emesis", "That is unit 50; here madanaphala is in the āsthāpana.")],
              [0, 1],
              "Unit 51 gives a purgation (powder licked with oil) and an āsthāpana strong with a decoction.",
              "विरेकः; …प्रगाढम् आस्थापनम्."),
        T(mcq("transfer", 5, "By the rule of चूर्णस्तैल…, how is रामः + तत्र written when joined?",
              ("रामस्तत्र", "Visarga before त becomes स्."),
              [("रामो तत्र", "Visarga becomes ओ only before a voiced sound; त is voiceless."),
               ("रामश्तत्र", "Visarga becomes श् before च, not before त."),
               ("रामर्तत्र", "Visarga after अ does not become र्.")],
              "चूर्णः + तैल → चूर्णस्तैल; so रामः + तत्र → रामस्तत्र.",
              "Visarga + त/थ → स्."),
          "A visarga before त or थ becomes स्."),
    ],
}

# ---------------------------------------------------------------- unit 52
AUTHORED["52"] = {
    "title": "वातजेऽप्यार्तवदोषे",
    "question": "What two statements does unit 52 join, and which new subject begins in it?",
    "rule": ("Oil cooked with madhuka and pippalī, as anuvāsana and uttarabasti. In the Vāta-type fault of ārtava also: drinking "
             "of ghee cooked with bhārgī (Clerodendrum serratum) and bhadradāru (probably deodar)."),
    "limits": ("The data reads two statements here: the first appears to continue the Kapha-type list of units 49-51; the second "
               "begins the faults of ārtava. What अपि (also) compares with is not said. Bhadradāru as deodar is probable; bhārgī "
               "and pippalī are standard."),
    "explain_hi": ("इस पंक्ति में दो कथन जुड़े लगते हैं। पहला: मधुक और पिप्पली (पीपर, मानक) से पकाया तेल, अनुवासन और उत्तरबस्ति; "
                   "यह सम्भवतः इकाई ४९-५१ की कफज सूची का शेष है। दूसरा: वातज आर्तवदोष में भी भार्गी यानी भारंगी (मानक) "
                   "और भद्रदारु (सम्भवतः देवदारु) से पकाए घी का पान। यहीं से आर्तव के दोषों की चिकित्सा शुरू होती है। "
                   "‘अपि’ (भी) किससे तुलना करता है, यह नहीं कहा।"),
    "hook": "पहले कफ का तेल, फिर नया विषय: वातज आर्तव में भारंगी-देवदारु का घी।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "In unit 52, which new subject begins?",
            ("Faults of ārtava", "वातजे अपि आर्तवदोषे: the faults of ārtava begin."),
            [("Faults of the breast milk", "Breast milk is not named in unit 52."),
             ("Signs of pregnancy", "Signs of pregnancy belong to units 14-16."),
             ("Faults of the urine", "Urine is not named in unit 52.")],
            "After the oil of the Kapha-type list, the line turns to the Vāta-type fault of ārtava.",
            "आर्तवदोष = fault of ārtava."),
        order(1, "Put these phrases of unit 52 in their printed order.",
              ["मधुकपिप्पलीसिद्धं तैलम्", "अनुवासनमुत्तरबस्तिश्च", "वातजेऽप्यार्तवदोषे", "भार्गीभद्रदारुसिद्धम्", "सर्पिःपानम्"],
              "The oil and its two uses; then the new case and its ghee drink.",
              "तैलम् → अनुवासनम् उत्तरबस्तिः च → वातजे … आर्तवदोषे → …सिद्धम् → सर्पिःपानम्."),
        T(match(2, "Match each word of unit 52 to its meaning on the card.",
                [["पिप्पली", "long pepper"], ["वातज", "Vāta-type"], ["आर्तवदोष", "fault of ārtava"],
                 ["भार्गी", "Clerodendrum serratum"], ["भद्रदारु", "probably deodar"]],
                "Five words carry the second statement and the drug of the first.",
                "पिप्पली, वातज, आर्तवदोष, भार्गी, भद्रदारु.", role="extend"),
          "Bhārgī = Clerodendrum serratum (standard); bhadradāru = deodar (probable)."),
        mcq("discriminate", 3, "Which split of वातजेऽप्यार्तवदोषे is right?",
            ("वातजे + अपि + आर्तवदोषे", "ए + अ → ए with ऽ; इ + आ → या."),
            [("वातजे + अप्य + आर्तवदोषे", "अप्य is not a word; the word is अपि."),
             ("वातज + अपि + आर्तवदोषे", "वातज + अपि would give वातजापि (अ + अ → आ), not वातजेऽपि."),
             ("वातजेऽपि + यार्तवदोषे", "यार्तवदोषे is not a word; the य comes from इ.")],
            "वातजे (in the Vāta-type) + अपि (also) + आर्तवदोषे (in the fault of ārtava).",
            "ए + अ → एऽ; इ + आ → या."),
        mcq("apply", 4, "By unit 52, what is drunk in the Vāta-type fault of ārtava?",
            ("Ghee cooked with bhārgī and bhadradāru", "भार्गीभद्रदारुसिद्धं सर्पिःपानम्."),
            [("Oil cooked with madhuka and pippalī", "That oil is the anuvāsana of the first statement."),
             ("Ghee cooked with sukta and rock salt", "That is the Vāta-type fault of śukra, unit 42."),
             ("Milk cooked with kulīra juice", "Milk with kulīra juice cooks unit 44's oil.")],
            "In the Vāta-type fault of ārtava: drinking of ghee cooked with bhārgī and bhadradāru.",
            "वातजे आर्तवदोषे … सर्पिःपानम्."),
        T(mcq("transfer", 5, "By the rule of वातजेऽपि, how is वने + अपि written when joined?",
              ("वनेऽपि", "ए + अ → ए, and the lost अ is marked by ऽ."),
              [("वनयपि", "ए + अ here gives एऽ, not अय."),
               ("वनापि", "ए + अ does not give आ."),
               ("वनेपि", "The अ is marked by ऽ (avagraha) in this sandhi.")],
              "वातजे + अपि → वातजेऽपि; so वने + अपि → वनेऽपि.",
              "ए + अ → एऽ."),
          "A final ए before अ stays, and the अ is dropped and marked with ऽ."),
    ],
}

# ---------------------------------------------------------------- unit 53
AUTHORED["53"] = {
    "title": "वा क्षीरम्, पयःसर्पिः सहितम्",
    "question": "What can be read for sure in the damaged unit 53?",
    "rule": ("Line 1 (damaged): or milk, cooked with drugs whose names are partly unreadable. Line 2: in (or as) a paste "
             "(kalka) of madhuka and śṛgālavinnā, combined with milk and ghee."),
    "limits": ("Low confidence. The first word is damaged; काश्मर्य and क्षुद्रसहा are only a reading and 'सूि' is unclear, so "
               "no question rests on them. कल्के (locative) or कल्कम् is undecided. Śṛgālavinnā is disputed. Which fault this "
               "treats is not said."),
    "explain_hi": ("यह इकाई क्षतिग्रस्त है, विश्वास कम। पहली पंक्ति का पहला शब्द टूटा है: आरम्भ ‘काश्मर्य’ और ‘क्षुद्रसहा’ जैसा लगता है, "
                   "बीच का ‘सूि’ अस्पष्ट है; अनुमानित पाठ पर अर्थ: अथवा (उनसे) पकाया दूध। "
                   "दूसरी पंक्ति: मधुक और शृगालविन्ना (पहचान विवादित) के कल्क (लेप) में, दूध और घी के साथ संयुक्त। "
                   "छपा ‘कल्के’ सप्तमी है, पर ‘सहितम्’ के कारण ‘कल्कम्’ भी सम्भव; यह तय नहीं।"),
    "hook": "पहला शब्द टूटा; पक्का: ‘वा क्षीरम्’ और ‘पयःसर्पिः सहितम्’।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By the sure part of unit 53, which two make up the paste (kalka)?",
            ("Madhuka and śṛgālavinnā", "मधुकशृगालविन्नाकल्के: a paste of madhuka and śṛgālavinnā."),
            [("Bilva and vidārī", "Bilva and vidārī are in unit 43's āsthāpana."),
             ("Dantī and viḍaṅga", "Dantī and viḍaṅga are unit 51's powder."),
             ("Bhārgī and bhadradāru", "These cook unit 52's ghee.")],
            "Line 2 names a paste (kalka) of madhuka and śṛgālavinnā.",
            "कल्क = paste."),
        order(1, "Put these sure words of unit 53 in their printed order.",
              ["वा", "क्षीरम्", "मधुकशृगालविन्नाकल्के", "पयःसर्पिः", "सहितम्"],
              "Line 1 ends 'or milk'; line 2: the paste, milk and ghee, combined.",
              "वा → क्षीरम् | कल्के → पयःसर्पिः → सहितम्."),
        T(match(2, "Match each word of unit 53 to its meaning on the card.",
                [["वा", "or"], ["कल्क", "paste"], ["पयः", "milk"], ["सर्पिः", "ghee"], ["सहित", "combined, together with"]],
                "Five sure words of the damaged unit.",
                "वा, कल्क, पयः, सर्पिः, सहित.", role="extend"),
          "पयः and क्षीर both mean milk; सर्पिः is ghee."),
        mcq("discriminate", 3, "What does पयःसर्पिः mean in unit 53?",
            ("Milk and ghee", "A pair (dvandva): पयः (milk) and सर्पिः (ghee)."),
            [("Ghee made from milk", "The data reads a pair, 'milk; ghee', not a source."),
             ("Milk without ghee", "No word of 'without' is in it."),
             ("Water and oil", "पयः is milk and सर्पिः is ghee.")],
            "पयःसर्पिः is a pair compound: milk and ghee.",
            "पयः = milk; सर्पिः = ghee."),
        mcq("apply", 4, "What does the card say of the first word of unit 53 (काश्मर्य…सिद्धं)?",
            ("It is damaged; read by conjecture", "The middle (सूि) is unclear; only a conjectural reading is given."),
            [("It is clear and fully readable", "The data marks it damaged and keeps it unsplit."),
             ("It names one plant, kāśmarya", "It seems to hold more names, partly unreadable."),
             ("It is the verb of the line", "It ends in सिद्धं, cooked; it is not a verb.")],
            "The first word is damaged: kāśmarya and kṣudrasahā are only a reading, and 'सूि' is unclear.",
            "Damaged word: nothing is built on it."),
        T(mcq("transfer", 5, "Built like पयःसर्पिः, what does the invented मधुसर्पिः mean?",
              ("Honey and ghee", "A pair compound like पयःसर्पिः: मधु (honey) and सर्पिः (ghee)."),
              [("Ghee made of honey", "As a pair it names two things, not a source."),
               ("Honey without ghee", "No word of 'without' is in it."),
               ("Sweet-tasting ghee", "मधु here is the noun honey, one of the pair.")],
              "पयःसर्पिः = milk and ghee; मधुसर्पिः = honey and ghee.",
              "A pair (dvandva) compound = X and Y."),
          "A dvandva compound joins two names with the sense 'X and Y'."),
    ],
}

# ================================================================= NOTES_HI
NOTES_HI = {
    "41": ("पंक्ति में अपनी क्रिया नहीं; डेटा इसे इकाई ४० (छपी पंक्ति ०२.०१.४२) का शेष मानता है, जहाँ ‘साधयेत्’ है ("
           "डेटा के नोट में ‘unit 42’ छपी पंक्ति की संख्या है)। ‘उभयान्’ (पुं. द्वितीया बहु.) किनके लिए, नहीं कहा; शुक्र-आर्तव दोष केवल अनुमान। "
           "सन्धि: च + उभयान् → चोभयान् (अ + उ → ओ); उभयान् + अपि → उभयानपि।"),
    "42": ("‘सैंधव’ में अनुस्वार छपाई की शैली है (सैन्धव)। ‘सुक्तसैंधवफलाम्ल’ को तीन वस्तुएँ (सुक्त, सैन्धव, खट्टा फल) पढ़ा गया है; "
           "‘फलाम्ल’ एक खट्टा फल भी हो सकता है। ‘सिद्धम्’ अन्तिम शब्द ‘सर्पिः’ से जुड़ता है। सैन्धव = सेंधा नमक, यव = जौ (दोनों मानक)।"),
    "43": ("दो छपी पंक्तियाँ (०२.०१.४५-४६) जुड़ी हैं; क्रिया नहीं। छपा ‘आस्थपनं’ (ह्रस्व अ) सम्भवतः ‘आस्थापनं’ है। "
           "सन्धि: …युक्तम् + आस्थापनम् → …युक्तमास्थापनम्; तैलम् + अनुवासनम् → तैलमनुवासनम्। "
           "विदारी, मधुक (मुलेठी; नाम महुआ के लिए भी) और भद्रदारु की पहचान सम्भावित।"),
    "44": ("छपा ‘रसरस’ सम्भवतः ‘रस’ का दोहराव (छपाई की भूल) है; दोनों रहें तो भी अर्थ नहीं बदलता। "
           "कुलीर = केकड़ा, पर कुछ सूचियों में पौधे का नाम भी, इसलिए निश्चित नहीं। सन्धि: तैलम् + उत्तरबस्तिः → तैलमुत्तरबस्तिः।"),
    "45": ("‘शुक्रदोषे’ इकाई ४२ से समझा जाता है। छपा ‘कांडेंक्षु’ में ए के बाद का ं अनावश्यक लगता है: सम्भावित पाठ काण्ड + इक्षु → काण्डेक्षु (अ + इ → ए)। "
           "‘मूर्वामधुकप्रतीवापंसर्पिःपानं’ छपाई में जुड़ा है। ‘प्रतीवाप’ (दीर्घ ई, जैसा छपा) = प्रतिवाप। काण्डेक्षु अज्ञात, मूर्वा विवादित।"),
    "46": ("छपाई में विसर्ग ‘:’ से दिखाया गया: ‘त्रिवृच्चूर्ण:’ = त्रिवृच्चूर्णः। "
           "सन्धि: त्रिवृत् + चूर्णः → त्रिवृच्चूर्णः (त् + च → च्च); सघृतः + विरेकः → सघृतो विरेकः (अः + घोष व्यंजन → ओ)। विरेक पुंलिंग।"),
    "47": ("पयस्या की पहचान विवादित; श्रीपर्णी = गम्भारी सम्भावित। ‘सिद्धम्’ और ‘युक्तम्’ दोनों ‘आस्थापनम्’ के विशेषण। "
           "सन्धि: क्षीरयुक्तम् + आस्थापनम् → क्षीरयुक्तमास्थापनम्।"),
    "48": ("मुद्गपर्णी = Phaseolus trilobus (Vigna trilobata), सम्भावित। "
           "सन्धि: तैलम् + अनुवासनम् + उत्तरबस्तिः + च → तैलमनुवासनमुत्तरबस्तिश्च (विसर्ग + च → श्च)।"),
    "49": ("छपा ‘पाषाणभेदकाश्मंतक’ = पाषाणभेदक + अश्मन्तक (अ + अ → आ); अश्मन्तक + आमलक → …काश्मन्तकामलक (अ + आ → आ)। "
           "अश्मन्तक की पहचान विवादित; पाषाणभेदक सम्भावित (दूसरे पौधे भी पाषाणभेद कहलाते हैं)। डेटा के नोट में हिन्दी ‘कफज’ कहा है, अनुवाद में ‘श्लैष्मिक’ ही रखा है।"),
    "50": ("बिना क्रिया का वाक्य। ‘कषाय’ = काढ़ा (विधि के अर्थ में)। "
           "सन्धि: मदनफलकषायः + वमनम् → मदनफलकषायो वमनम् (अः + घोष व्यंजन → ओ)। मदनफल = मैनफल, मानक।"),
    "51": ("दो छपी पंक्तियाँ (०२.०१.५४-५५) जुड़ी हैं। सन्धि: चूर्णः + तैल → चूर्णस्तैल (विसर्ग + त → स्त); तैललीढः + विरेकः → तैललीढो विरेकः। "
           "‘फल’ दोनों नामों (राजवृक्ष, मदन) के साथ या केवल मदन के साथ, तय नहीं। राजवृक्ष का भाग नहीं कहा।"),
    "52": ("दो कथन जुड़े लगते हैं: पहला कफज सूची का शेष (सम्भवतः), दूसरा आर्तवदोष का आरम्भ। "
           "छपाई में ‘आर्तवदोषेभार्गी’ जुड़ा है: आर्तवदोषे + भार्गी। "
           "सन्धि: वातजे + अपि → वातजेऽपि (ए + अ → एऽ); अपि + आर्तव → अप्यार्तव (इ + आ → या)। ‘अपि’ की तुलना किससे, नहीं कहा।"),
    "53": ("विश्वास कम। ‘काश्मर्यक्षुद्रसहासूिसिद्धं’ क्षतिग्रस्त है: ‘सूि’ कोई शब्द नहीं, बीच का भाग अपुनर्स्थाप्य; काश्मर्य और क्षुद्रसहा केवल पाठ-अनुमान, "
           "शब्द बिना विभाजन रखा गया। ‘कल्के’ (सप्तमी, जैसा छपा) बनाम ‘कल्कम्’ (‘सहितम्’ से मेल): दोनों सम्भव, अनुवाद छपे रूप पर। "
           "शृगालविन्ना की पहचान विवादित।"),
}

# ===================================================================== AIDS
AIDS = {
    "41": {
        "frame": "इकाई ४०: …साधयेत् → इकाई ४१: गुह्यप्रतिषेधेन च, उभयान् अपि च (क्रिया वही, ‘साधयेत्’)।",
        "sandhi": "अ + उ → ओ: च + उभयान् → चोभयान् · न् + स्वर: उभयान् + अपि → उभयानपि।",
        "chunks": "गुह्यप्रतिषेधेन | चोभयानपि | च",
    },
    "42": {
        "diagram": {"groups": [
            {"label": "दशा", "items": ["वातिक शुक्रदोष"]},
            {"label": "जिनके साथ पका", "items": ["सुक्त", "सैन्धव", "फल-अम्ल"]},
            {"label": "प्रतिवाप", "items": ["यवक्षार"]},
            {"label": "उपचार", "items": ["सर्पिःपान (घी पीना)"]}]},
        "chunks": "वातिके शुक्रदोषे | सुक्तसैंधवफलाम्लसिद्धं | यवक्षारप्रतिवापं | सर्पिःपानं",
        "frame": "ढाँचा: दशा (सप्तमी) → …सिद्धम् (किसके साथ पका) → …प्रतिवापम् (क्या मिलाया) → सर्पिःपानम्। यही ढाँचा इकाई ४५ और ४९ में दोहराया गया है।",
        "pegs": "मेरा बनाया चित्र: खट्टा-नमकीन घी का प्याला, ऊपर जौ की बाली से छिड़का क्षार (केवल याद के लिए)।",
    },
    "43": {
        "contrast": "आस्थापन: बिल्व, विदारी, क्षीर (काढ़े की बस्ति) ↔ अनुवासन: तैल, मधुक और भद्रदारु के साथ पका (तेल की बस्ति)।",
        "chunks": "बिल्वविदारीक्षीरयुक्तम् | आस्थापनम् || मधुकभद्रदारुसिद्धं | तैलम् | अनुवासनम्",
        "sandhi": "म् + स्वर: …युक्तम् + आस्थापनम् → …युक्तमास्थापनम् · तैलम् + अनुवासनम् → तैलमनुवासनम्।",
    },
    "44": {
        "chain": {"steps": ["दूध", "कुलीर (सम्भवतः केकड़ा) का रस", "उनसे पकाया तेल", "उत्तरबस्ति"]},
        "sandhi": "म् + स्वर: तैलम् + उत्तरबस्तिः → तैलमुत्तरबस्तिः।",
        "anchors": "उत्तरबस्ति = मूत्रमार्ग (पुरुष) या योनिमार्ग (स्त्री) से दी जाने वाली बस्ति; इस पंक्ति में मार्ग नहीं कहा।",
    },
    "45": {
        "diagram": {"groups": [
            {"label": "दशा", "items": ["पैत्तिक (शुक्रदोष)"]},
            {"label": "जिनके साथ पका", "items": ["काण्डेक्षु (पाठ सम्भावित)", "श्वदंष्ट्रा (गोखरू)", "गुडूची (गिलोय)"]},
            {"label": "प्रतीवाप", "items": ["मूर्वा", "मधुक"]},
            {"label": "उपचार", "items": ["सर्पिःपान"]}]},
        "contrast": "…सिद्धम्: घी इनके साथ पकता है (काण्डेक्षु, श्वदंष्ट्रा, गुडूची) ↔ …प्रतीवापम्: बाद में मिलाए जाते हैं (मूर्वा, मधुक)।",
        "sandhi": "अ + इ → ए: काण्ड + इक्षु → काण्डेक्षु (छपा ‘कांडेंक्षु’, सम्भावित सुधार)।",
        "frame": "इकाई ४२ का ढाँचा, नई दशा: पैत्तिके (शुक्रदोषे समझा जाता है)।",
    },
    "46": {
        "sandhi": "त् + च → च्च: त्रिवृत् + चूर्णः → त्रिवृच्चूर्णः · अः + व → ओ व: सघृतः + विरेकः → सघृतो विरेकः।",
        "chunks": "त्रिवृच्चूर्णः | सघृतो | विरेकः",
        "frame": "क्या (त्रिवृत् चूर्ण) + किसके साथ (घृत) = कौन-सा शोधन (विरेक)।",
    },
    "47": {
        "chunks": "पयस्याश्रीपर्णीसिद्धं | क्षीरयुक्तम् | आस्थापनं",
        "sandhi": "म् + आ: क्षीरयुक्तम् + आस्थापनम् → क्षीरयुक्तमास्थापनम्।",
        "frame": "दो विशेषण, एक संज्ञा: …सिद्धम् (पका) + क्षीरयुक्तम् (दूध से युक्त) → आस्थापनम्।",
    },
    "48": {
        "chunks": "मधुकमुद्गपर्णीसिद्धं | तैलम् | अनुवासनम् | उत्तरबस्तिश्च",
        "sandhi": "विसर्ग + च → श्च: उत्तरबस्तिः + च → उत्तरबस्तिश्च · म् + स्वर: तैलम् + अनुवासनम् → तैलमनुवासनम्।",
        "frame": "एक तेल, दो उपयोग: अनुवासन और उत्तरबस्ति (‘च’ से जुड़े)।",
    },
    "49": {
        "diagram": {"groups": [
            {"label": "दशा", "items": ["श्लैष्मिक (कफज)"]},
            {"label": "क्वाथ जिसमें पका", "items": ["पाषाणभेदक", "अश्मन्तक", "आमलक"]},
            {"label": "चूर्ण-प्रतीवाप", "items": ["पिप्पली", "मधुक"]},
            {"label": "उपचार", "items": ["सर्पिःपान"]}]},
        "sandhi": "अ + अ → आ: पाषाणभेदक + अश्मन्तक → पाषाणभेदकाश्मन्तक · अ + आ → आ: अश्मन्तक + आमलक → अश्मन्तकामलक।",
        "contrast": "क्वाथ (काढ़ा) में पकाना: पाषाणभेदक, अश्मन्तक, आमलक ↔ चूर्ण के रूप में मिलाना: पिप्पली, मधुक।",
        "frame": "इकाई ४२ और ४५ का ढाँचा, तीसरी दशा: श्लैष्मिके। नया: घी काढ़े में पकता है, प्रतीवाप चूर्ण है।",
    },
    "50": {
        "sandhi": "अः + व → ओ व: मदनफलकषायः + वमनम् → मदनफलकषायो वमनम्।",
        "anchors": "कषाय यहाँ = काढ़ा (विधि), कसैला रस नहीं। वमन = उल्टी कराना।",
        "puns": "मेरी बनाई, केवल सुनने की सहायता: ‘मदन-फल’ से ‘मैन-फल’, और मैनफल से वमन।",
    },
    "51": {
        "contrast": "विरेक: दन्ती-विडङ्ग चूर्ण, तेल से चाटा ↔ आस्थापन: राजवृक्ष-मदनफल के काढ़े से प्रगाढ़।",
        "sandhi": "विसर्ग + त → स्त: चूर्णः + तैल → चूर्णस्तैल · अः + व → ओ व: तैललीढः + विरेकः → तैललीढो विरेकः।",
        "chunks": "दंतीविडंगचूर्णः | तैललीढो | विरेकः || राजवृक्षमदनफलकषायप्रगाढम् | आस्थापनं",
    },
    "52": {
        "contrast": "पहला कथन (सम्भवतः कफज का शेष): मधुक-पिप्पली तैल, अनुवासन और उत्तरबस्ति ↔ दूसरा (नया विषय): वातज आर्तवदोष में भार्गी-भद्रदारु घृत का पान।",
        "sandhi": "ए + अ → एऽ: वातजे + अपि → वातजेऽपि · इ + आ → या: अपि + आर्तव → अप्यार्तव।",
        "chunks": "मधुकपिप्पलीसिद्धं तैलम् | अनुवासनमुत्तरबस्तिश्च || वातजेऽप्यार्तवदोषे | भार्गीभद्रदारुसिद्धं | सर्पिःपानं",
        "frame": "शुक्रदोष (इकाई ४२-५२ का पहला भाग) → आर्तवदोष (इकाई ५२ का दूसरा भाग से)।",
    },
    "53": {
        "frame": "पंक्ति १: [टूटा शब्द …सिद्धं] वा क्षीरं · पंक्ति २: मधुकशृगालविन्नाकल्के पयःसर्पिः सहितं। प्रश्न केवल पक्के शब्दों पर।",
        "chunks": "काश्मर्यक्षुद्रसहासूिसिद्धं (क्षतिग्रस्त) | वा क्षीरं || मधुकशृगालविन्नाकल्के | पयःसर्पिः | सहितं",
        "anchors": "पयः = दूध, सर्पिः = घी: ‘पयःसर्पिः’ = दूध और घी।",
    },
}

# ============================================================== IMAGE_SPECS
IMAGE_SPECS = {
    ("42", "diagram"): {
        "file": "sh1-vatika-shukra-42.svg",
        "alt": ("Flowchart of unit 42: in the Vata-type fault of shukra, ghee is cooked with sukta, saindhava (rock salt) and "
                "sour fruit, yava-kshara is added, and the ghee is drunk."),
        "type": "mermaid",
        "code": ("flowchart TD\n"
                 "  A[\"वातिक शुक्रदोष\"] --> E[\"सर्पिःपान\"]\n"
                 "  B[\"सुक्त, सैन्धव,<br/>खट्टा फल\"] -->|\"साथ पका\"| E\n"
                 "  C[\"यवक्षार\"] -->|\"प्रतिवाप\"| E\n"),
    },
    ("43", "contrast"): {
        "file": "sh1-asthapana-anuvasana-43.svg",
        "alt": ("Split of unit 43: asthapana (decoction enema) with bilva, vidari (probable) and milk; anuvasana (oil enema) "
                "of oil cooked with madhuka (probable) and bhadradaru (probable)."),
        "type": "split",
        "title": "दो बस्तियाँ (इकाई ४३)",
        "cols": [["आस्थापन (काढ़े की बस्ति)", ["बिल्व (बेल)", "विदारी (सम्भावित)", "क्षीर (दूध)"]],
                 ["अनुवासन (तेल की बस्ति)", ["तैल, पका हुआ:", "मधुक (सम्भावित)", "भद्रदारु (सम्भावित)"]]],
    },
    ("44", "chain"): {
        "file": "sh1-uttarabasti-44.svg",
        "alt": ("Chain of unit 44: milk and the juice of kulira (probably crab) cook an oil, which is given as uttarabasti."),
        "type": "chain",
        "title": "उत्तरबस्ति का तेल (इकाई ४४)",
        "steps": ["दूध", "कुलीर (सम्भवतः केकड़ा) का रस", "उनसे पकाया तेल", "उत्तरबस्ति"],
    },
    ("45", "diagram"): {
        "file": "sh1-paittika-shukra-45.svg",
        "alt": ("Mind map of unit 45: in the Pitta-type (fault of shukra), ghee drink cooked with kandekshu (possible reading), shvadamshtra and "
                "guduchi, with murva and madhuka as the addition."),
        "type": "mermaid",
        "code": ("mindmap\n"
                 "  पैत्तिक: सर्पिःपान\n"
                 "    साथ पका\n"
                 "      काण्डेक्षु, पाठ सम्भावित\n"
                 "      श्वदंष्ट्रा\n"
                 "      गुडूची\n"
                 "    प्रतीवाप\n"
                 "      मूर्वा\n"
                 "      मधुक\n"),
    },
    ("49", "diagram"): {
        "file": "sh1-shlaishmika-shukra-49.svg",
        "alt": ("Mind map of unit 49: in the Kapha-type, ghee drink cooked with a decoction of pashanabhedaka, ashmantaka and "
                "amalaka, with powder of pippali and madhuka as the addition."),
        "type": "mermaid",
        "code": ("mindmap\n"
                 "  श्लैष्मिक: सर्पिःपान\n"
                 "    क्वाथ में पका\n"
                 "      पाषाणभेदक\n"
                 "      अश्मन्तक\n"
                 "      आमलक\n"
                 "    चूर्ण-प्रतीवाप\n"
                 "      पिप्पली\n"
                 "      मधुक\n"),
    },
    ("51", "contrast"): {
        "file": "sh1-vireka-asthapana-51.svg",
        "alt": ("Split of unit 51: purgation is the powder of danti (probable) and vidanga licked with oil; asthapana is made "
                "strong with a decoction of rajavriksha and madanaphala."),
        "type": "split",
        "title": "इकाई ५१: दो शोधन",
        "cols": [["विरेक (विरेचन)", ["दन्ती (सम्भावित)", "विडङ्ग", "चूर्ण, तेल से चाटा"]],
                 ["आस्थापन", ["राजवृक्ष (अमलतास)", "मदनफल", "काढ़े से प्रगाढ़"]]],
    },
    ("52", "contrast"): {
        "file": "sh1-artavadosha-52.svg",
        "alt": ("Split of unit 52: first statement (probably the end of the Kapha-type list): oil with madhuka and pippali as "
                "anuvasana and uttarabasti; second (new subject): in the Vata-type fault of artava, ghee cooked with bhargi "
                "and bhadradaru is drunk."),
        "type": "split",
        "title": "इकाई ५२: दो कथन",
        "cols": [["पहला (सम्भवतः कफज का शेष)", ["मधुक-पिप्पली से पका तेल", "अनुवासन", "उत्तरबस्ति"]],
                 ["दूसरा: वातज आर्तवदोष", ["भार्गी", "भद्रदारु (सम्भावित)", "उनसे पका घी पीना"]]],
    },
}
