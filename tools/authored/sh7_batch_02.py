from helpers import mcq, match, order, fill, multi, accepts


AUTHORED = {}

# ---------------------------------------------------------------- unit 14
AUTHORED["14"] = {
    "title": "वंक्षणवृषणमध्ये विटपं",
    "question": "By unit 14, where is the marma viṭapa, and what may follow its piercing?",
    "rule": ("Between the groin (वंक्षण) and the testes (वृषण) lies viṭapa (विटपम्); there, ṣāṇḍhya (probably "
             "impotence) or (वा) scantiness of śukra (semen), on the near-certain reading अल्पशुक्रता."),
    "limits": ("Prose, no verb. The printed अल्पशुकृता is not a word; the data reads अल्पशुक्रता (near certain), so no "
               "question rests on that word's form. ṣāṇḍhya = impotence is only the probable sense. वृषण can also mean "
               "the scrotum."),
    "explain_hi": ("यह गद्य-पंक्ति पैर के मर्मों की सूची का अन्तिम मर्म बताती है: वंक्षण यानी जाँघ और पेड़ू के जोड़ तथा वृषण यानी अण्डकोष के बीच विटप। "
                   "वहाँ आघात होने पर षाण्ढ्य, यानी सम्भवतः नपुंसकता, अथवा शुक्र यानी वीर्य की अल्पता होती है। "
                   "छपा ‘अल्पशुकृता’ कोई शब्द नहीं; डेटा इसे लगभग निश्चित रूप से ‘अल्पशुक्रता’ पढ़ता है। "
                   "‘वा’ (अथवा) दोनों फलों को विकल्प के रूप में रखता है। "
                   "‘विटपं तत्र’ में विटपम् का अन्तिम म् व्यंजन से पहले अनुस्वार (ं) लिखा गया है।"),
    "hook": "वंक्षण और वृषण के बीच विटप: षाण्ढ्य या अल्प शुक्र।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 14, where does the marma viṭapa lie?",
            ("Between the groin and the testes", "वंक्षणवृषणमध्ये: in the middle of the groin and the testes."),
            [("In the middle of the thigh", "The middle of the thigh is the place of urvī (unit 12), not viṭapa."),
             ("Three aṅgulas above the knee", "That is the place of āṇi (unit 11), not viṭapa."),
             ("At the joining of foot and shank", "That is the gulpha, the ankle (unit 8), not viṭapa.")],
            "Viṭapa lies between the groin (vaṅkṣaṇa) and the testes (vṛṣaṇa).",
            "वंक्षणवृषणमध्ये विटपम्."),
        order(1, "Put the printed words of unit 14 in the line's order.",
              ["वंक्षणवृषणमध्ये", "विटपं", "तत्र", "षांढ्यमल्पशुकृता", "वा"],
              "Between groin and testes; viṭapa; there; ṣāṇḍhya and scanty śukra (printed अल्पशुकृता); or.",
              "वंक्षणवृषणमध्ये → विटपं → तत्र → षांढ्यमल्पशुकृता → वा."),
        match(2, "Match each word of unit 14 to its meaning.",
              [["वंक्षण", "groin"], ["वृषण", "testes"], ["मध्ये", "in the middle, between"], ["तत्र", "there"],
               ["वा", "or"]],
              "वंक्षण-वृषण-मध्ये = between the groin and the testes; तत्र = there; वा = or.",
              "वंक्षण, वृषण, मध्ये, तत्र, वा.", role="extend",
              teaches="Two places joined in one compound and closed by मध्ये mean 'between them': वंक्षणवृषणमध्ये."),
        mcq("discriminate", 3, "Why is विटपम् printed विटपं before तत्र in unit 14?",
            ("Final म् before a consonant is written ं", "Inside a sentence a final म् before a consonant is written as anusvāra."),
            [("The ं marks a dual ending of विटप", "विटपम् is nominative singular (gram: n. nom. sg.), not dual."),
             ("The ं stands for a lost final visarga", "There is no visarga here; the word ends in म्."),
             ("Final म् before a vowel is written ं", "Before a vowel म् joins it (षाण्ढ्यमल्प); तत्र begins with त.")],
            "विटपम् + तत्र → विटपं तत्र: final म् before the consonant त is written ं.",
            "Final म् + consonant (inside a sentence) → ं."),
        multi("apply", 4, "Which statements fit unit 14?",
              [("The line names death as the result", "No death is named; the results are ṣāṇḍhya or scanty śukra."),
               ("Viṭapa lies between the groin and the testes", "Right: वंक्षणवृषणमध्ये विटपम्."),
               ("Piercing there may bring ṣāṇḍhya (probably impotence)", "Right: तत्र षाण्ढ्यम्; impotence is the probable sense."),
               ("The two results are joined by 'and' (च)", "They are joined by वा, 'or'.")],
              [1, 2],
              "Viṭapa: between groin and testes; there ṣāṇḍhya or scanty śukra (वा = or).",
              "वंक्षणवृषणमध्ये विटपं तत्र षाण्ढ्यम् ... वा."),
        mcq("transfer", 5, "By the rule of षाण्ढ्यमल्प (षाण्ढ्यम् + अल्प), how is जलम् + अस्ति joined in a new example?",
            ("जलमस्ति", "A final म् joins a following vowel, as षाण्ढ्यम् + अल्प → षाण्ढ्यमल्प."),
            [("जलोऽस्ति", "ओऽ comes from अः + अ, not from अम् + अ."),
             ("जलास्ति", "The म् does not drop; it joins the vowel."),
             ("जलंस्ति", "ं stands before a consonant, and the vowel अ cannot vanish.")],
            "जलम् + अस्ति = जलमस्ति, like षाण्ढ्यम् + अल्प = षाण्ढ्यमल्प.",
            "Final म् + vowel → म joined to the vowel.",
            teaches="A final म् before a vowel joins it: षाण्ढ्यम् + अल्प → षाण्ढ्यमल्प."),
    ],
}

# ---------------------------------------------------------------- unit 15
AUTHORED["15"] = {
    "title": "सक्थिवद्बाह्वोः",
    "question": "What does unit 15 say about the marmas of the two arms (bāhu)?",
    "rule": ("In the two arms (बाह्वोः, locative dual) it is as in the sakthi, the lower limb (सक्थिवत्): the plain "
             "sense is that the arms have marmas answering to those of the leg."),
    "limits": ("Prose, one printed word, elliptical: no verb and no marma is named, and the data supplies none. "
               "The sentence appears to be continued by units 16 and 17, which give the differences for the arms."),
    "explain_hi": ("यह एक शब्द की गद्य-पंक्ति भुजा के मर्मों का खण्ड आरम्भ करती है: ‘सक्थि के समान, दोनों भुजाओं में’। "
                   "सीधा अर्थ यह है कि भुजाओं के मर्म पैर (सक्थि) के मर्मों के अनुरूप हैं; पर पंक्ति न क्रिया देती है, न किसी मर्म का नाम। "
                   "‘-वत्’ का अर्थ है ‘के समान’। "
                   "‘बाह्वोः’ बाहु का सप्तमी द्विवचन है: दोनों भुजाओं में। "
                   "डेटा के अनुसार इकाई १६ और १७ इसे आगे बढ़ाती प्रतीत होती हैं, जहाँ भुजा के विशेष भेद आते हैं।"),
    "hook": "जैसा पैर में, वैसा भुजाओं में: सक्थिवत्।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 15, the two arms (bāhu) are said to be like what?",
            ("The sakthi (lower limb)", "सक्थिवत् = like the sakthi, the lower limb."),
            [("The trunk (antarādhi)", "The trunk is not named in unit 15."),
             ("The head (mūrdhan)", "The head is not named in unit 15."),
             ("The neck and head (grīvā-śiras)", "Neither neck nor head is named in unit 15.")],
            "सक्थिवद्बाह्वोः: in the two arms, as in the lower limb.",
            "सक्थि + वत् = like the lower limb."),
        match(1, "Match each part of unit 15 to its meaning.",
              [["सक्थि", "lower limb"], ["वत्", "like"], ["बाहु", "arm"], ["बाह्वोः", "in the two arms"]],
              "सक्थि-वत् = like the lower limb; बाह्वोः = in the two arms.",
              "सक्थि, वत्, बाहु, बाह्वोः."),
        fill(2, "Unit 15: सक्थिवत् ____ (in the two arms). Type it in Devanagari or in English letters (e.g. dharma).",
             accepts("बाह्वोः", None, "bahvoh", "bahvo"),
             "बाह्वोः (in the two arms): सक्थिवद्बाह्वोः.",
             "बाह्वोः is the locative dual of the u-stem बाहु: 'in the two arms'.",
             "सक्थिवत् बाह्वोः."),
        mcq("discriminate", 3, "Which split of सक्थिवद्बाह्वोः in unit 15 is right?",
            ("सक्थिवत् + बाह्वोः", "त् before the voiced ब is written द्: सक्थिवद्बाह्वोः."),
            [("सक्थि + वद्बाह्वोः", "वद्बाह्वोः is not a word; the द् belongs to -वत्."),
             ("सक्थिवः + बाह्वोः", "अः before the voiced ब would give ओ (सक्थिवो), not द्."),
             ("सक्थिवत् + आह्वोः", "आह्वोः is not a word; the word is बाह्वोः, 'in the two arms'.")],
            "सक्थिवत् (like the lower limb) + बाह्वोः (in the two arms).",
            "त् + voiced consonant → द्."),
        mcq("apply", 4, "By the plain sense of unit 15, what does सक्थिवत् tell about the arms?",
            ("Their marmas answer to the leg's", "The data's plain sense: the arms have marmas like those of the sakthi."),
            [("They are longer than the legs", "No length is compared in unit 15."),
             ("They have no marmas at all", "सक्थिवत् points to marmas like the leg's, not to none."),
             ("They heal sooner than the legs", "Healing is not spoken of in unit 15.")],
            "In the arms it is as in the lower limb: their marmas correspond to the leg's (plain sense; none is named).",
            "सक्थिवत् = as in the lower limb."),
        mcq("transfer", 5, "By the pattern of सक्थिवत्, which word means 'like a lion' (सिंह) in a new example?",
            ("सिंहवत्", "-वत् added to a noun means 'like it', as सक्थि → सक्थिवत्."),
            [("सिंहतः", "-तः means 'from' or 'on the side of', not 'like'."),
             ("सिंहेन", "सिंहेन is the instrumental: by the lion."),
             ("सिंहस्य", "सिंहस्य is the genitive: of the lion.")],
            "सिंह + वत् = सिंहवत्, like सक्थि + वत् = सक्थिवत्.",
            "noun + -वत् = 'like that noun'.",
            teaches="-वत् after a noun makes an indeclinable 'like ...': सक्थिवत्, like the lower limb."),
    ],
}

# ---------------------------------------------------------------- unit 16
AUTHORED["16"] = {
    "title": "विशेषस्तु गुल्फो मणिबंधः",
    "question": "By unit 16, what is the special point (viśeṣa) for the arms' marmas?",
    "rule": ("The special point (विशेषः): the data reads gulpha (ankle) as maṇibandha (wrist) and jānu (knee) as kūrpara "
             "(elbow) in the arm; in the piercing of those two, kuṇita, being bent or crooked."),
    "limits": ("Prose, no copula: the line only sets the names side by side; 'what is gulpha in the leg is maṇibandha "
               "in the arm' is the data's reading. The printed कुणित may stand for कुणित्वम् (possible); the sense is "
               "the same, so no question rests on the form. Appears to continue unit 15."),
    "explain_hi": ("यह पंक्ति भुजा का विशेष बताती है और इकाई १५ को आगे बढ़ाती प्रतीत होती है। "
                   "डेटा इसे मेल के रूप में पढ़ता है: पैर में जो गुल्फ है वह भुजा में मणिबन्ध यानी कलाई, और जो जानु है वह कूर्पर यानी कोहनी। "
                   "पंक्ति स्वयं केवल नाम साथ रखती है, ‘है’ नहीं कहती। "
                   "उन दोनों के बिंधने पर ‘कुणित’ यानी मुड़ा या टेढ़ा होना; छपा ‘कुणित’ शायद ‘कुणित्वं’ के लिए है, अर्थ वही। "
                   "‘विशेषस्तु’ और ‘मणिबंधस्तथा’ में विसर्ग त से पहले स् बना है।"),
    "hook": "पैर का गुल्फ, भुजा की कलाई; पैर का घुटना, भुजा की कोहनी: बिंधे तो टेढ़ापन।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "As the data reads unit 16, what in the arm answers to the gulpha (ankle) of the leg?",
            ("The maṇibandha (wrist)", "गुल्फो मणिबन्धः: the ankle's counterpart is the wrist (data's reading)."),
            [("The kūrpara (elbow)", "The elbow is set beside the jānu (knee), not the gulpha."),
             ("The aṃsa (shoulder)", "The shoulder is not named in unit 16."),
             ("The kakṣādhāra (armpit)", "Kakṣādhāra comes in unit 17, named like viṭapa, not like the gulpha.")],
            "gulpha → maṇibandha; jānu → kūrpara (the data's reading of the juxtaposed names).",
            "गुल्फो मणिबन्धस्तथा जानु कूर्परम्."),
        order(1, "Put the printed parts of unit 16 in the line's order.",
              ["विशेषस्तु", "गुल्फो", "मणिबंधस्तथा", "जानुकूर्परं", "तयोर्व्यधे कुणित"],
              "The special point; gulpha; maṇibandha, likewise; jānu, kūrpara; in the piercing of those two, kuṇita.",
              "विशेषस्तु → गुल्फो → मणिबंधस्तथा → जानुकूर्परं → तयोर्व्यधे कुणित."),
        match(2, "Match each word of unit 16 to its meaning.",
              [["गुल्फ", "ankle"], ["मणिबन्ध", "wrist"], ["जानु", "knee"], ["कूर्पर", "elbow"], ["व्यध", "piercing"]],
              "गुल्फ = ankle, मणिबन्ध = wrist, जानु = knee, कूर्पर = elbow, व्यध = piercing.",
              "गुल्फ, मणिबन्ध, जानु, कूर्पर, व्यध.", role="extend",
              teaches="The leg-name comes first and the arm-name after it: गुल्फो मणिबन्धः, जानु कूर्परम् (data's reading)."),
        mcq("discriminate", 3, "Why is विशेषः printed विशेषस् before तु in unit 16?",
            ("Visarga before त becomes स्", "विशेषः + तु → विशेषस्तु; likewise मणिबन्धः + तथा → मणिबन्धस्तथा."),
            [("Visarga before any consonant becomes स्", "Not any: before the voiced म, गुल्फः became गुल्फो."),
             ("Visarga before a vowel becomes स्", "तु begins with the consonant त, not a vowel."),
             ("Visarga before a voiced sound becomes स्", "त is not voiced; before a voiced sound अः gives ओ.")],
            "विशेषः + तु: visarga before त → स्.",
            "Visarga + त → स्त."),
        mcq("apply", 4, "By unit 16, what follows the piercing (vyadha) of those two?",
            ("Crookedness (kuṇita)", "तयोर्व्यधे कुणित: in their piercing, bentness or crookedness."),
            [("Blindness (āndhya)", "Blindness is the result for the apāṅga (unit 38), not here."),
             ("Deafness (bādhirya)", "Deafness is the result for the vidhura (unit 36), not here."),
             ("Loss of the voice (svara)", "Voice changes belong to the neck vessels (unit 34), not here.")],
            "In the piercing of those two: kuṇita, being bent or crooked.",
            "तयोर्व्यधे कुणित."),
        mcq("transfer", 5, "By the rule of विशेषस्तु, how is रामः + तत्र (Rāma there) joined in a new example?",
            ("रामस्तत्र", "Visarga before त becomes स्, as विशेषः + तु → विशेषस्तु."),
            [("रामो तत्र", "ओ comes from अः only before a voiced sound; त is not voiced."),
             ("रामश्तत्र", "श् comes before च, छ or श, not before त."),
             ("रामर्तत्र", "र् comes after vowels other than अ/आ before a voiced sound.")],
            "रामः + तत्र = रामस्तत्र, like विशेषः + तु = विशेषस्तु.",
            "Visarga + त → स्त.",
            teaches="A visarga before त becomes स्: विशेषः + तु → विशेषस्तु, मणिबन्धः + तथा → मणिबन्धस्तथा."),
    ],
}

# ---------------------------------------------------------------- unit 17
AUTHORED["17"] = {
    "title": "विटपवच्च कक्षाधारः",
    "question": "By unit 17, which arm marma is named like viṭapa, and what follows there?",
    "rule": ("And like viṭapa (विटपवत् च): kakṣādhāra (कक्षाधारः), in the middle of the armpit (कक्षा) and the akṣa "
             "(sense uncertain); there, kuṇitva (crookedness)."),
    "limits": ("Low confidence. अक्ष is not a known body part; the data leaves it untranslated and notes a possible "
               "reading 'between armpit and chest', not adopted; so no question asks where kakṣādhāra lies. 'Like "
               "viṭapa' is read as the arm's counterpart of unit 14; nothing more is stated. Appears to continue 15-16."),
    "explain_hi": ("यह पंक्ति भुजा के खण्ड का अन्तिम मर्म बताती है: ‘और विटप के समान’ कक्षाधार। "
                   "डेटा ‘विटप के समान’ को इकाई १४ के विटप का भुजा वाला प्रतिरूप पढ़ता है; पंक्ति इससे अधिक नहीं कहती। "
                   "स्थान ‘कक्षा (काँख) और अक्ष के बीच’ छपा है, पर अक्ष का अर्थ अनिश्चित है; ‘काँख और वक्ष के बीच’ एक सम्भावित पाठ है, अपनाया नहीं गया। "
                   "वहाँ आघात से कुणित्व यानी टेढ़ापन। "
                   "‘विटपवच्च’ में विटपवत् का त् च से पहले च् बना है।"),
    "hook": "विटप जैसा, भुजा में: कक्षाधार, फल टेढ़ापन।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 17, what follows at the kakṣādhāra?",
            ("Crookedness (kuṇitva)", "तत्र कुणित्वम्: there, crookedness."),
            [("Deafness (bādhirya)", "Deafness belongs to the vidhura (unit 36), not here."),
             ("Blindness (āndhya)", "Blindness belongs to the apāṅga (unit 38), not here."),
             ("Loss of smell (gandha)", "Loss of smell belongs to the phaṇa (unit 37), not here.")],
            "At kakṣādhāra: kuṇitva, crookedness.",
            "कक्षाधारः तत्र कुणित्वम्."),
        order(1, "Put the printed words of unit 17 in the line's order.",
              ["विटपवच्च", "कक्षाक्षमध्ये", "कक्षाधारः", "तत्र", "कुणित्वं"],
              "And like viṭapa; in the middle of armpit and akṣa (sense uncertain); kakṣādhāra; there; crookedness.",
              "विटपवच्च → कक्षाक्षमध्ये → कक्षाधारः → तत्र → कुणित्वं."),
        match(2, "Match each word of unit 17 to its meaning.",
              [["विटपवत्", "like viṭapa"], ["च", "and"], ["कक्षा", "armpit"], ["तत्र", "there"], ["कुणित्व", "crookedness"]],
              "विटपवत् च = and like viṭapa; कक्षा = armpit; तत्र कुणित्वम् = there, crookedness.",
              "विटपवत्, च, कक्षा, तत्र, कुणित्व.", role="extend",
              teaches="-त्व makes an abstract noun of state: कुणित्व = the state of being crooked."),
        mcq("discriminate", 3, "Which split of विटपवच्च in unit 17 is right?",
            ("विटपवत् + च", "त् before च is written च्: विटपवत् + च → विटपवच्च."),
            [("विटप + वच्च", "वच्च is not a word; the च् comes from the त् of -वत्."),
             ("विटपवः + च", "A visarga before च would give श्च (विटपवश्च), not च्च."),
             ("विटपवम् + च", "म् before च would be written ं (विटपवं च), not च्च.")],
            "विटपवत् (like viṭapa) + च (and).",
            "त् + च → च्च."),
        multi("apply", 4, "Which statements fit unit 17?",
              [("Death at once follows there", "No death is named; the result is crookedness."),
               ("Kakṣādhāra is named 'like viṭapa'", "Right: विटपवच्च ... कक्षाधारः."),
               ("Loss of blood is named there", "No loss of blood is named in unit 17."),
               ("Crookedness (kuṇitva) is named there", "Right: तत्र कुणित्वम्.")],
              [1, 3],
              "Like viṭapa: kakṣādhāra; there, crookedness.",
              "विटपवच्च ... कक्षाधारः तत्र कुणित्वम्."),
        mcq("transfer", 5, "By the rule of विटपवच्च, how is तत् + च (and that) joined in a new example?",
            ("तच्च", "त् before च becomes च्, as विटपवत् + च → विटपवच्च."),
            [("तश्च", "श्च comes from a visarga before च, not from त्."),
             ("तद्च", "द् comes before a voiced sound; च is not voiced."),
             ("तंच", "ं comes from a final म्, not from त्.")],
            "तत् + च = तच्च, like विटपवत् + च = विटपवच्च.",
            "त् + च → च्च.",
            teaches="A final त् before च becomes च्: विटपवत् + च → विटपवच्च."),
    ],
}

# ---------------------------------------------------------------- unit 18
AUTHORED["18"] = {
    "title": "वातवर्चोनिरसनस्थूलांत्रप्रतिबद्धो गुदः",
    "question": "By unit 18, how is the guda (anus) described, and what follows its injury?",
    "rule": ("The guda (anus), bound to the large intestine (स्थूलान्त्र), with the expelling (निरसन) of wind (वात) and "
             "stool (वर्चस्) in the compound; there, immediate death (सद्यो मरणम्)."),
    "limits": ("Prose, no verb. The compound does not settle whether 'expelling' qualifies the guda or the large "
               "intestine; the data keeps it with the intestine, and no question asks which. वात here is read as wind "
               "(flatus). Guda covers the anus and rectal end."),
    "explain_hi": ("यह पंक्ति उदर और वक्ष के मर्मों का खण्ड आरम्भ करती है। "
                   "गुद यानी गुदा स्थूलान्त्र यानी बड़ी आँत से बँधा है; लम्बे समास में वात (यहाँ वायु, यानी अधोवायु) और वर्चस् (मल) को बाहर निकालना भी आता है। "
                   "‘निरसन’ गुद का विशेषण है या स्थूलान्त्र का, यह समास से तय नहीं होता; डेटा इसे आँत के साथ रखता है। "
                   "वहाँ आघात से तुरन्त मृत्यु। "
                   "‘प्रतिबद्धो गुदः’ और ‘सद्यो मरणं’ में अः घोष व्यंजन से पहले ओ बना है।"),
    "hook": "बड़ी आँत से बँधा गुद: वहाँ तुरन्त मृत्यु।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 18, what follows an injury at the guda (anus)?",
            ("Immediate death", "तत्र सद्यो मरणम्: there, death at once."),
            [("Lameness of the leg", "Lameness is the result for the jānu (unit 10), not the guda."),
             ("Deafness of one ear", "Deafness belongs to the vidhura (unit 36), not the guda."),
             ("Crookedness of the arm", "Crookedness belongs to the arm marmas (units 16-17).")],
            "At the guda: immediate death.",
            "गुदः तत्र सद्यो मरणम्."),
        order(1, "Put the members of the long compound of unit 18 in their printed order.",
              ["वात", "वर्चस्", "निरसन", "स्थूलान्त्र", "प्रतिबद्ध"],
              "wind, stool, expelling, large intestine, bound to: वातवर्चोनिरसनस्थूलान्त्रप्रतिबद्धः.",
              "वात → वर्चस् → निरसन → स्थूलान्त्र → प्रतिबद्ध."),
        match(2, "Match each member of the compound of unit 18 to its meaning.",
              [["वात", "wind (flatus)"], ["वर्चस्", "stool"], ["निरसन", "expelling"], ["स्थूलान्त्र", "large intestine"],
               ["प्रतिबद्ध", "bound to"]],
              "वात-वर्चः-निरसन = expelling of wind and stool; स्थूलान्त्र = large intestine; प्रतिबद्ध = bound to.",
              "वात, वर्चस्, निरसन, स्थूलान्त्र, प्रतिबद्ध.", role="extend",
              teaches="प्रतिबद्ध (bound to) closes the compound and agrees with गुदः: the guda is bound to the large intestine."),
        mcq("discriminate", 3, "Which split of वर्चोनिरसन (in the compound of unit 18) is right?",
            ("वर्चः + निरसन", "The as-stem वर्चस् ends in visarga; अः before the voiced न → ओ: वर्चोनिरसन."),
            [("वर्च + उनिरसन", "उनिरसन is not a word; the ओ comes from वर्चः."),
             ("वर्चम् + निरसन", "म् before न would be written ं or न्, never ओ."),
             ("वर्चा + निरसन", "आ before न stays आ (वर्चानिरसन); the print has ओ.")],
            "वर्चः (stool) + निरसन (expelling): अः before the voiced न → ओ.",
            "अः + voiced consonant → ओ (also inside a compound)."),
        multi("apply", 4, "Which statements fit unit 18?",
              [("The guda is bound to the large intestine", "Right: स्थूलान्त्रप्रतिबद्धो गुदः."),
               ("The guda is bound to the bladder (basti)", "The basti comes in unit 19; the guda is bound to the large intestine."),
               ("Death follows at once there", "Right: तत्र सद्यो मरणम्."),
               ("Piercing there makes the leg lame", "Lameness is not named in unit 18.")],
              [0, 2],
              "The guda, bound to the large intestine; there, immediate death.",
              "स्थूलान्त्रप्रतिबद्धो गुदः तत्र सद्यो मरणम्."),
        mcq("transfer", 5, "By the rule of सद्यो मरणं, how is रामः + गच्छति (Rāma goes) joined in a new example?",
            ("रामो गच्छति", "अः before a voiced consonant becomes ओ, as सद्यः + मरणम् → सद्यो मरणम्."),
            [("रामर्गच्छति", "र् comes after vowels other than अ/आ, not after अ."),
             ("रामस्गच्छति", "स् comes before त or थ, not before ग."),
             ("रामश्गच्छति", "श् comes before च, छ or श, not before ग.")],
            "रामः + गच्छति = रामो गच्छति, like सद्यः + मरणम् = सद्यो मरणम्.",
            "अः + voiced consonant → ओ.",
            teaches="अः before a voiced consonant becomes ओ: सद्यः + मरणम् → सद्यो मरणम्, प्रतिबद्धः + गुदः → प्रतिबद्धो गुदः."),
    ],
}

# ---------------------------------------------------------------- unit 19
AUTHORED["19"] = {
    "title": "अल्पमांसशोणितोऽभ्यंतरतः",
    "question": "By unit 19, how is the basti (urinary bladder) described, and what is the exception to death there?",
    "rule": ("The basti (bladder) has little flesh and blood, is bow-curved (धनुर्वक्र), has one opening (एकद्वार) and its "
             "mouth turned down (अधोमुख); there too, immediate death, except from the wound of aśmarī (urinary stone)."),
    "limits": ("Low confidence: the printed क्टचा is not a word (candidates कट्याः, त्वचा; none adopted), so the sentence "
               "stands on a conjectural reading and no question touches that word. That the aśmarī-wound is the one "
               "made to remove a stone is only the natural sense; the line does not say so. Continued by unit 20."),
    "explain_hi": ("यह पंक्ति बस्ति यानी मूत्राशय का रूप बताती है: अल्प मांस और रक्त वाली, धनुष के समान टेढ़ी, एक द्वार वाली और नीचे की ओर मुख वाली। "
                   "बीच का छपा शब्द ‘क्टचा’ अस्पष्ट है (कोई स्वर नहीं); ‘कट्याः’ या ‘त्वचा’ सम्भावित हैं, अपनाए नहीं गए, इसलिए वाक्य अनुमानित पाठ पर है। "
                   "वहाँ भी तुरन्त मृत्यु, अश्मरी यानी मूत्र की पथरी के व्रण को छोड़कर (‘ऋते’ पञ्चमी के साथ)। "
                   "यह व्रण पथरी निकालने के लिए किया गया घाव है, यह स्वाभाविक अर्थ है पर पंक्ति ऐसा नहीं कहती। "
                   "डेटा के अनुसार इकाई २० इसे आगे बढ़ाती है।"),
    "hook": "धनुष-सी टेढ़ी, एक द्वार, नीचे मुख: बस्ति; अश्मरी-व्रण को छोड़ तुरन्त मृत्यु।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 19, the basti (bladder) is curved like what?",
            ("A bow (dhanus)", "धनुर्वक्रः: curved like a bow."),
            [("A conch (śaṅkha)", "No conch is named in unit 19."),
             ("A snake (sarpa)", "No snake is named in unit 19."),
             ("A lotus (padma)", "No lotus is named in unit 19.")],
            "The basti is bow-curved (धनुर्वक्र).",
            "धनुः + वक्र = धनुर्वक्र."),
        order(1, "Put these printed features of unit 19 in the line's order.",
              ["अल्पमांसशोणितो", "धनुर्वक्र", "एकद्वारो", "अधोमुखो", "बस्तिः"],
              "Little flesh and blood; bow-curved; one opening; mouth downward; the basti.",
              "अल्पमांसशोणितो → धनुर्वक्र → एकद्वारो → अधोमुखो → बस्तिः."),
        match(2, "Match each word part of unit 19 to its meaning.",
              [["अल्प", "little"], ["धनुस्", "bow"], ["वक्र", "curved"], ["द्वार", "opening"], ["अधोमुख", "mouth turned downward"]],
              "अल्प-मांस-शोणित = with little flesh and blood; धनुर्वक्र = bow-curved; एकद्वार = with one opening; अधोमुख = mouth downward.",
              "अल्प, धनुस्, वक्र, द्वार, अधोमुख.", role="extend",
              teaches="Each feature is a bahuvrīhi in the masculine nominative agreeing with बस्तिः: एकद्वारः = 'having one opening'."),
        mcq("discriminate", 3, "Which split of एकद्वारोऽधोमुखो in unit 19 is right?",
            ("एकद्वारः + अधोमुखः", "अः + अ → ओऽ: एकद्वारोऽधो-; then अः before the voiced ब → ओ."),
            [("एकद्वारः + धोमुखः", "धोमुखः is not a word; the avagraha marks a lost अ of अधोमुखः."),
             ("एकद्वारा + अधोमुखः", "आ + अ → आ would give एकद्वाराधोमुखः, with no ओऽ."),
             ("एकद्वारम् + अधोमुखः", "म् + अ would give एकद्वारमधोमुखः.")],
            "एकद्वारः (with one opening) + अधोमुखः (mouth downward): अः + अ → ओऽ.",
            "अः + अ → ओऽ (the ऽ marks the lost अ)."),
        mcq("apply", 4, "By unit 19, which wound at the basti is excepted (ṛte) from immediate death?",
            ("An aśmarī (stone) wound", "अश्मरीव्रणादृते: except from the wound of aśmarī (urinary stone)."),
            [("A kaṇṭaka (thorn) wound", "No thorn is named in unit 19."),
             ("A daṃśa (bite) wound", "No bite is named in unit 19."),
             ("A dagdha (burn) wound", "No burn is named in unit 19.")],
            "There too, immediate death, except from the aśmarī-wound.",
            "ऋते + ablative = except."),
        mcq("transfer", 5, "By the rule of व्रणादृते (व्रणात् + ऋते), how is जलात् + ऋते (except from water) joined in a new example?",
            ("जलादृते", "A final त् before a vowel becomes द्, as व्रणात् + ऋते → व्रणादृते."),
            [("जलातृते", "Before a vowel the त् is voiced to द्; it is not kept."),
             ("जलाऋते", "The final consonant does not drop before a vowel."),
             ("जलाद्रते", "ऋ is a vowel, not the consonant र; the ऋ stays.")],
            "जलात् + ऋते = जलादृते, like व्रणात् + ऋते = व्रणादृते.",
            "त् + vowel → द् + vowel.",
            teaches="A final त् before a vowel becomes द्: अश्मरीव्रणात् + ऋते → अश्मरीव्रणादृते."),
    ],
}

# ---------------------------------------------------------------- unit 20
AUTHORED["20"] = {
    "title": "तत्राप्युभयतो विद्धे न जीवति",
    "question": "By unit 20, what follows when (the basti, apparently) is pierced on both sides, and on one side?",
    "rule": ("Pierced on both sides (उभयतः विद्धे), one does not live (न जीवति); split on one side (एकतः भिन्ने), a wound "
             "discharging urine (मूत्रस्रावी व्रणः) results; that wound, treated with effort (यत्नेन उपक्रान्तः), heals (रोहति)."),
    "limits": ("Prose; the subject of जीवति is unstated (the person). 'There' apparently means the basti of unit 19 "
               "(the data: appears to continue it). The line names no particular treatment."),
    "explain_hi": ("यह पंक्ति इकाई १९ की बस्ति को आगे बढ़ाती प्रतीत होती है और दो स्थितियों में भेद करती है। "
                   "दोनों ओर बिंधने पर व्यक्ति जीवित नहीं रहता। "
                   "एक ओर फटने पर मूत्र बहाने वाला व्रण यानी घाव होता है; वह प्रयत्न से उपचारित किया जाए तो भर जाता है। "
                   "कौन सा उपचार, यह पंक्ति नहीं बताती। "
                   "‘यत्नेनोपक्रांतो’ में अ + उ → ओ हुआ है।"),
    "hook": "दोनों ओर बिंधे तो जीवन नहीं; एक ओर फटे तो मूत्र-स्रावी घाव, यत्न से भर जाता है।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 20, what follows when (the basti, apparently) is pierced on both sides?",
            ("One does not live", "उभयतो विद्धे न जीवति: pierced on both sides, one does not live."),
            [("A wound that heals", "The healing wound follows a split on one side, not both."),
             ("Lameness of the leg", "Lameness is not named in unit 20."),
             ("Loss of the smell", "Loss of smell is not named in unit 20.")],
            "Both sides: one does not live; one side: a urine-discharging wound that heals with effort.",
            "उभयतो विद्धे न जीवति."),
        order(1, "Put the phrases of unit 20 in the line's order.",
              ["तत्राप्युभयतो विद्धे", "न जीवति", "एकतो भिन्ने", "मूत्रस्रावी व्रणो भवति", "स तु यत्नेनोपक्रांतो रोहति"],
              "Pierced on both sides; does not live; split on one side; a urine-discharging wound results; that, treated with effort, heals.",
              "तत्राप्युभयतो विद्धे → न जीवति → एकतो भिन्ने → मूत्रस्रावी व्रणो भवति → स तु यत्नेनोपक्रांतो रोहति."),
        match(2, "Match each word of unit 20 to its meaning.",
              [["उभयतः", "on both sides"], ["एकतः", "on one side"], ["मूत्रस्रावी", "discharging urine"],
               ["उपक्रान्त", "treated"], ["रोहति", "heals"]],
              "उभयतः = on both sides; एकतः = on one side; मूत्रस्रावी = urine-discharging; उपक्रान्त = treated; रोहति = heals.",
              "उभयतः, एकतः, मूत्रस्रावी, उपक्रान्त, रोहति.", role="extend",
              teaches="-तः makes adverbs of side: उभयतः 'on both sides', एकतः 'on one side'."),
        mcq("discriminate", 3, "Which split of यत्नेनोपक्रांतो in unit 20 is right?",
            ("यत्नेन + उपक्रान्तः", "अ + उ → ओ: यत्नेनोप-; अः before the voiced र → ओ (उपक्रान्तो रोहति)."),
            [("यत्नेन + ओपक्रान्तः", "ओपक्रान्तः is not a word; the ओ comes from अ + उ."),
             ("यत्नेनः + उपक्रान्तः", "अः before उ would drop to अ, leaving a gap (यत्नेन उप-), not ओ."),
             ("यत्नेनौ + पक्रान्तः", "Neither यत्नेनौ nor पक्रान्तः is a word.")],
            "यत्नेन (with effort) + उपक्रान्तः (treated): अ + उ → ओ.",
            "अ + उ → ओ."),
        multi("apply", 4, "Which statements fit unit 20?",
              [("Pierced on both sides, one does not live", "Right: उभयतो विद्धे न जीवति."),
               ("Split on one side, one dies at once", "A split on one side gives a wound that can heal, not death."),
               ("A one-side split gives a wound discharging urine", "Right: एकतो भिन्ने मूत्रस्रावी व्रणो भवति."),
               ("That wound, treated with effort, heals", "Right: स तु यत्नेनोपक्रान्तो रोहति.")],
              [0, 2, 3],
              "Both sides: no life; one side: a urine-discharging wound, which heals when treated with effort.",
              "उभयतो विद्धे न जीवति; एकतो भिन्ने मूत्रस्रावी व्रणो भवति; स तु यत्नेनोपक्रान्तो रोहति."),
        mcq("transfer", 5, "By the rule of यत्नेनोपक्रांतो (अ + उ), how is सूर्य + उदयः (sunrise) joined in a new example?",
            ("सूर्योदयः", "अ + उ → ओ, as यत्नेन + उपक्रान्तः → यत्नेनोपक्रान्तः."),
            [("सूर्यौदयः", "औ comes from अ + ओ or औ, not from अ + उ."),
             ("सूर्युदयः", "The अ does not simply drop before उ."),
             ("सूर्यवुदयः", "व् comes from उ before another vowel, not from अ.")],
            "सूर्य + उदयः = सूर्योदयः, like यत्नेन + उपक्रान्तः = यत्नेनोपक्रान्तः.",
            "अ + उ → ओ.",
            teaches="अ before उ merges into ओ: यत्नेन + उपक्रान्तः → यत्नेनोपक्रान्तः."),
    ],
}

# ---------------------------------------------------------------- unit 21
AUTHORED["21"] = {
    "title": "पक्कामाशयमध्ये नाभिः",
    "question": "By unit 21, where is the nābhi (navel) placed, and what follows its injury?",
    "rule": ("In the middle of the pakva (digested, standing for pakvāśaya, probably the lower gut) and the āmāśaya "
             "(probably the stomach) is the nābhi (navel); there too (तत्रापि), immediate death."),
    "limits": ("Prose, no verb. The printed पक्का- is a Prakrit-like form; the Sanskrit पक्व is a possible correction. That "
               "पक्व stands for pakvāśaya is the usual sense, but आशय is not printed after it, so no question rests on "
               "it. The data labels āmāśaya 'standard' in the word list and 'probably the stomach' in the translation."),
    "explain_hi": ("यह पंक्ति नाभि का स्थान बताती है: पक्व और आमाशय के बीच। "
                   "पक्व से यहाँ पक्वाशय (पचे हुए अन्न का आशय, सम्भवतः नीचे की आँत) समझा जाता है, पर ‘आशय’ शब्द पक्व के बाद छपा नहीं। "
                   "आमाशय कच्चे अन्न का आशय है, सम्भवतः जठर। "
                   "छपा ‘पक्का’ प्राकृत जैसा रूप है; संस्कृत ‘पक्व’ सम्भावित सुधार है। "
                   "वहाँ भी तुरन्त मृत्यु; ‘तत्रापि’ = तत्र + अपि।"),
    "hook": "पक्व और आम के बीच नाभि: वहाँ भी तुरन्त मृत्यु।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 21, which marma lies between the pakva and the āmāśaya?",
            ("The nābhi (navel)", "पक्वामाशयमध्ये नाभिः: the navel lies between them."),
            [("The basti (bladder)", "The basti is described in unit 19, not placed here."),
             ("The guda (anus)", "The guda is bound to the large intestine (unit 18)."),
             ("The aṃsa (shoulder)", "The aṃsa lie between neck, arm and head (unit 33).")],
            "Between the pakva and the āmāśaya: the nābhi.",
            "पक्कामाशयमध्ये नाभिः."),
        match(1, "Match each word of unit 21 to its meaning.",
              [["नाभि", "navel"], ["आमाशय", "probably the stomach"], ["मध्ये", "in the middle"], ["सद्यः", "immediately"],
               ["मरण", "death"]],
              "नाभि = navel; आमाशय = probably the stomach; मध्ये = in the middle; सद्यो मरणम् = immediate death.",
              "नाभि, आमाशय, मध्ये, सद्यः, मरण."),
        order(2, "Put the printed words of unit 21 in the line's order.",
              ["पक्कामाशयमध्ये", "नाभिः", "तत्रापि", "सद्यो", "मरणं"],
              "Between pakva and āmāśaya; the nābhi; there too; immediately; death.",
              "पक्कामाशयमध्ये → नाभिः → तत्रापि → सद्यो → मरणं.", role="extend",
              teaches="तत्रापि = तत्र + अपि, 'there too': it links this marma to the ones before that also kill at once."),
        mcq("discriminate", 3, "Which split of तत्रापि in unit 21 is right?",
            ("तत्र + अपि", "अ + अ → आ: तत्रापि, 'there too'."),
            [("तत्रा + पि", "Neither तत्रा nor पि is a word."),
             ("तत्रः + अपि", "अः + अ would give ओऽ (तत्रोऽपि), not आ."),
             ("तत्रम् + अपि", "म् + अ would give तत्रमपि.")],
            "तत्र (there) + अपि (also): अ + अ → आ.",
            "अ + अ → आ."),
        mcq("apply", 4, "By unit 21, what follows an injury at the nābhi?",
            ("Immediate death there too", "तत्रापि सद्यो मरणम्: there too, death at once."),
            [("Paleness and loss of colour", "Paleness and discolour come with the kaṭīkataruṇa (unit 27)."),
             ("Bentness of the elbow joint", "Bentness belongs to the arm marmas (unit 16)."),
             ("Lameness and a stiff thigh", "Lameness belongs to the jānu (unit 10).")],
            "At the nābhi: immediate death, as at the guda and the basti.",
            "तत्रापि सद्यो मरणम्."),
        mcq("transfer", 5, "By the rule of तत्रापि, how is अत्र + अस्ति (it is here) joined in a new example?",
            ("अत्रास्ति", "अ + अ → आ, as तत्र + अपि → तत्रापि."),
            [("अत्रस्ति", "Two अ do not merge into a short अ; they give आ."),
             ("अत्रेस्ति", "ए comes from अ + इ, not from अ + अ."),
             ("अत्रोस्ति", "ओ comes from अ + उ, not from अ + अ.")],
            "अत्र + अस्ति = अत्रास्ति, like तत्र + अपि = तत्रापि.",
            "अ + अ → आ.",
            teaches="Two short अ merge into आ: तत्र + अपि → तत्रापि."),
    ],
}

# ---------------------------------------------------------------- unit 22
AUTHORED["22"] = {
    "title": "कोष्ठवक्षसोः स्तनयोश्च मध्ये हृदयं",
    "question": "By unit 22, where is the hṛdaya (heart), what is it called, and what follows its injury?",
    "rule": ("In the middle of the koṣṭha (belly) and the chest, and of the two breasts, is the hṛdaya (heart): the seat "
             "(अधिष्ठान) of sattva, rajas and tamas, the gate (द्वार) of the āmāśaya (probably the stomach); there too, "
             "immediate death."),
    "limits": ("Prose, no verb. The print runs मध्ये into the next word and drops the avagraha of तमोऽधिष्ठानम्; no "
               "question rests on those forms. 'Between belly and chest' reads कोष्ठवक्षसोः as a dvandva (data). The three "
               "guṇas are named, not explained."),
    "explain_hi": ("यह पंक्ति हृदय का स्थान और स्वरूप बताती है: कोष्ठ (पेट) और वक्ष के बीच तथा दोनों स्तनों के बीच। "
                   "हृदय सत्त्व, रज और तम, इन तीन गुणों का अधिष्ठान यानी आधार है, और आमाशय (सम्भवतः जठर) का द्वार है। "
                   "वहाँ भी तुरन्त मृत्यु। "
                   "छपाई में ‘मध्ये’ अगले शब्द से जुड़ गया है और ‘तमोऽधिष्ठानम्’ का अवग्रह छूट गया है; ‘सत्व’ = सत्त्व। "
                   "‘स्तनयोश्च’ में विसर्ग च से पहले श् बना है।"),
    "hook": "स्तनों के बीच हृदय: तीन गुणों का आधार, आमाशय का द्वार; वहाँ भी तुरन्त मृत्यु।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 22, the hṛdaya (heart) is called the seat (adhiṣṭhāna) of what?",
            ("Sattva, rajas and tamas", "सत्त्वरजस्तमोऽधिष्ठानम्: the seat of the three guṇas."),
            [("Urine, stool and sweat", "These are not named in unit 22."),
             ("Hair, nails and teeth", "These are not named in unit 22."),
             ("Bones, sinews and joints", "These are not named in unit 22.")],
            "The heart is the seat of sattva, rajas and tamas.",
            "सत्वरजस्तमोधिष्ठानम् (printed)."),
        order(1, "Put the printed parts of unit 22 in the line's order.",
              ["कोष्ठवक्षसोः स्तनयोश्च", "मध्ये", "सत्वरजस्तमोधिष्ठानम्", "आमाशयद्वारं", "हृदयं", "तत्रापि सद्यो मरणं"],
              "Of belly and chest and the two breasts; in the middle; seat of the three guṇas; gate of the āmāśaya; the heart; there too immediate death.",
              "कोष्ठवक्षसोः स्तनयोश्च → मध्ये → सत्वरजस्तमोधिष्ठानम् → आमाशयद्वारं → हृदयं → तत्रापि सद्यो मरणं."),
        match(2, "Match each word of unit 22 to its meaning.",
              [["कोष्ठ", "belly, trunk cavity"], ["वक्षस्", "chest"], ["स्तन", "breast"], ["अधिष्ठान", "seat"], ["द्वार", "gate"]],
              "कोष्ठ = belly; वक्षस् = chest; स्तन = breast; अधिष्ठान = seat; द्वार = gate.",
              "कोष्ठ, वक्षस्, स्तन, अधिष्ठान, द्वार.", role="extend",
              teaches="आमाशयद्वारम् is a tat-puruṣa: the gate (द्वार) of the āmāśaya."),
        mcq("discriminate", 3, "Why is स्तनयोः printed स्तनयोश् before च in unit 22?",
            ("Visarga before च becomes श्", "स्तनयोः + च → स्तनयोश्च."),
            [("Visarga before any consonant becomes श्", "Not any: in रजस्तमः the visarga before त became स्."),
             ("श् is part of a dual case ending", "The dual ending is -योः; the श् comes from sandhi."),
             ("Visarga before a voiced sound becomes श्", "च is not voiced; after ओ a visarga before a voiced sound gives र्.")],
            "स्तनयोः + च: visarga before च → श्.",
            "Visarga + च → श्च."),
        multi("apply", 4, "Which statements fit unit 22?",
              [("The heart lies below the two breasts", "It lies in the middle of the two breasts, not below them."),
               ("The heart lies between the two breasts", "Right: स्तनयोश्च मध्ये."),
               ("The heart is called the gate of the āmāśaya", "Right: आमाशयद्वारम्."),
               ("There too, death follows at once", "Right: तत्रापि सद्यो मरणम्.")],
              [1, 2, 3],
              "Between the breasts; seat of the three guṇas; gate of the āmāśaya; immediate death.",
              "स्तनयोश्च मध्ये ... आमाशयद्वारं हृदयं तत्रापि सद्यो मरणम्."),
        mcq("transfer", 5, "By the rule of स्तनयोश्च, how is नराः + च (and the men) joined in a new example?",
            ("नराश्च", "Visarga before च becomes श्, as स्तनयोः + च → स्तनयोश्च."),
            [("नरास्च", "स् comes before त or थ, not before च."),
             ("नरा च", "After आ the visarga drops before a voiced sound; च is not voiced."),
             ("नरो च", "ओ comes from अः before a voiced consonant, not from आः.")],
            "नराः + च = नराश्च, like स्तनयोः + च = स्तनयोश्च.",
            "Visarga + च → श्च.",
            teaches="A visarga before च becomes श्: स्तनयोः + च → स्तनयोश्च."),
    ],
}

# ---------------------------------------------------------------- unit 23
AUTHORED["23"] = {
    "title": "स्तनयोरधस्तात् द्व्यंगुलमुभयतः स्तनमूले",
    "question": "By unit 23, where are the two stanamūla, and whose death is stated there?",
    "rule": ("Two aṅgulas (द्व्यङ्गुलम्) below the two breasts, on both sides, are the two stanamūla (breast-roots); in "
             "those two, death of one whose koṣṭha (belly) is full of Kapha (कफपूर्णकोष्ठस्य)."),
    "limits": ("Prose, no verb. 'In those two' is read as 'when pierced'. Death is tied to the state 'koṣṭha full of "
               "Kapha'; the text says no more about it."),
    "explain_hi": ("यह पंक्ति दो स्तनमूल मर्म बताती है: दोनों स्तनों के नीचे दो अंगुल, दोनों ओर। "
                   "‘स्तनमूले’ द्विवचन है: दो मर्म, एक-एक ओर। "
                   "उन दोनों में आघात से उस व्यक्ति की मृत्यु कही गई है जिसका कोष्ठ कफ से भरा हो; पंक्ति इससे अधिक नहीं बताती। "
                   "‘द्व्यंगुलम्’ में द्वि + अङ्गुल से इ + अ → य हुआ है। "
                   "‘स्तनयोरधस्तात्’ में ओ के बाद का विसर्ग स्वर से पहले र् बना है।"),
    "hook": "स्तनों के नीचे दो अंगुल: स्तनमूल; कफ-भरे कोष्ठ वाले की मृत्यु।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 23, where are the two stanamūla?",
            ("Two aṅgulas below the breasts", "स्तनयोरधस्तात् द्व्यङ्गुलम्: two aṅgulas below the two breasts."),
            [("Two aṅgulas above the nipples", "That is the place of the stanarohita (unit 24)."),
             ("In the middle of the breasts", "The middle of the breasts is the heart's place (unit 22)."),
             ("Below the two shoulder-tops", "That is the place of the apālāpa (unit 26).")],
            "Two aṅgulas below the breasts, on both sides: the stanamūla.",
            "स्तनयोरधस्तात् द्व्यंगुलमुभयतः स्तनमूले."),
        order(1, "Put the printed words of unit 23 in the line's order.",
              ["स्तनयोरधस्तात्", "द्व्यंगुलमुभयतः", "स्तनमूले", "तयोः", "कफपूर्णकोष्ठस्य", "मरणं"],
              "Below the breasts; two aṅgulas on both sides; the stanamūla; in those two; of one with koṣṭha full of Kapha; death.",
              "स्तनयोरधस्तात् → द्व्यंगुलमुभयतः → स्तनमूले → तयोः → कफपूर्णकोष्ठस्य → मरणं."),
        match(2, "Match each word of unit 23 to its meaning.",
              [["अधस्तात्", "below"], ["द्व्यङ्गुल", "two finger-breadths"], ["उभयतः", "on both sides"], ["मूल", "root"],
               ["पूर्ण", "full"]],
              "अधस्तात् = below; द्व्यङ्गुल = two aṅgulas; उभयतः = on both sides; मूल = root; पूर्ण = full.",
              "अधस्तात्, द्व्यङ्गुल, उभयतः, मूल, पूर्ण.", role="extend",
              teaches="कफपूर्णकोष्ठस्य is a bahuvrīhi in the genitive: 'of one whose koṣṭha is full of Kapha'."),
        mcq("discriminate", 3, "Which split of द्व्यंगुलमुभयतः in unit 23 is right?",
            ("द्वि + अङ्गुलम् + उभयतः", "इ + अ → य: द्व्यङ्गुल-; म् + उ → मु: -लमुभयतः."),
            [("द्व + यङ्गुलम् + उभयतः", "Neither द्व nor यङ्गुलम् is a word; the य् comes from द्वि."),
             ("द्वि + अङ्गुलः + उभयतः", "अः before उ would drop to अ (अङ्गुल उभयतः), with no म्."),
             ("द्वे + अङ्गुलम् + उभयतः", "ए + अ would give एऽ (द्वेऽङ्गुलम्), not य.")],
            "द्वि (two) + अङ्गुलम् (finger-breadth) + उभयतः (on both sides).",
            "इ + अ → य; म् + vowel → joined."),
        mcq("apply", 4, "By unit 23, whose death is stated for the stanamūla?",
            ("One whose koṣṭha is full of Kapha", "कफपूर्णकोष्ठस्य मरणम्."),
            [("One whose koṣṭha is full of blood", "Blood-full koṣṭha is stated for other marmas (units 24, 25), not here."),
             ("One whose koṣṭha is full of pus", "Pus is not named in unit 23."),
             ("One whose koṣṭha is full of wind", "Wind is not named in unit 23.")],
            "At the stanamūla: death of one whose koṣṭha is full of Kapha.",
            "तयोः कफपूर्णकोष्ठस्य मरणम्."),
        mcq("transfer", 5, "By the rule of द्व्यंगुलम् (द्वि + अङ्गुलम्), how is इति + अत्र joined in a new example?",
            ("इत्यत्र", "इ before a different vowel becomes य्, as द्वि + अङ्गुलम् → द्व्यङ्गुलम्."),
            [("इतात्र", "इ does not turn into आ before अ."),
             ("इत्यात्र", "य् + आ would come from इ + आ, not इ + अ."),
             ("इतीत्र", "ई would come from इ + इ, not इ + अ.")],
            "इति + अत्र = इत्यत्र, like द्वि + अङ्गुलम् = द्व्यङ्गुलम्.",
            "इ + अ → य.",
            teaches="इ before a different vowel becomes य्: द्वि + अङ्गुलम् → द्व्यङ्गुलम्."),
    ],
}

# ---------------------------------------------------------------- unit 24
AUTHORED["24"] = {
    "title": "स्तनचूचुकयोरूर्ध्वं स्तनरोहिते",
    "question": "By unit 24, where are the two stanarohita, and whose death is stated there?",
    "rule": ("Two aṅgulas above the stanacūcuka (breast and nipple, read as a dvandva), on both sides, are the two "
             "stanarohita; death of one whose koṣṭha is full of blood (शोणितपूर्णकोष्ठस्य)."),
    "limits": ("Prose, no verb. The printed सद्यो before श is irregular (सद्यः or सद्यश् expected; possible flag); no "
               "question rests on it. Unlike units 23 and 25 there is no तयोः. The data's notes read स्तनचूचुक as a "
               "dvandva, while its translation says 'the two nipples'; no question rests on the parse."),
    "explain_hi": ("यह पंक्ति दो स्तनरोहित मर्म बताती है: स्तनचूचुक के ऊपर दो अंगुल, दोनों ओर। "
                   "डेटा की टिप्पणी ‘स्तनचूचुक’ को द्वन्द्व (स्तन और चूचुक) पढ़ती है, अनुवाद ‘दोनों स्तनाग्र’ कहता है। "
                   "वहाँ तुरन्त, रक्त से भरे कोष्ठ वाले व्यक्ति की मृत्यु कही गई है। "
                   "छपा ‘सद्यो’ श से पहले अनियमित है; ‘सद्यः’ या ‘सद्यश्’ अपेक्षित है। "
                   "इकाई २३ और २५ के विपरीत यहाँ ‘तयोः’ नहीं है।"),
    "hook": "चूचुक के ऊपर दो अंगुल: स्तनरोहित; रक्त-भरे कोष्ठ वाले की मृत्यु।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 24, how far from the stanacūcuka do the two stanarohita lie?",
            ("Two aṅgulas above", "स्तनचूचुकयोरूर्ध्वं द्व्यङ्गुलम्: two aṅgulas above."),
            [("Two aṅgulas below", "Below the breasts lie the stanamūla (unit 23), not the stanarohita."),
             ("Three aṅgulas above", "The line has द्वि (two), not three."),
             ("Twelve aṅgulas below", "Twelve aṅgulas is the measure for indrabasti (unit 9).")],
            "Two aṅgulas above the stanacūcuka, on both sides.",
            "ऊर्ध्वं द्व्यंगुलमुभयतः स्तनरोहिते."),
        order(1, "Put the printed words of unit 24 in the line's order.",
              ["स्तनचूचुकयोरूर्ध्वं", "द्व्यंगुलमुभयतः", "स्तनरोहिते", "सद्यो", "शोणितपूर्णकोष्ठस्य", "मरणं"],
              "Above the stanacūcuka; two aṅgulas on both sides; the stanarohita; at once; of one with koṣṭha full of blood; death.",
              "स्तनचूचुकयोरूर्ध्वं → द्व्यंगुलमुभयतः → स्तनरोहिते → सद्यो → शोणितपूर्णकोष्ठस्य → मरणं."),
        match(2, "Match each word of unit 24 to its meaning.",
              [["ऊर्ध्वम्", "above"], ["चूचुक", "nipple"], ["शोणित", "blood"], ["पूर्ण", "full"], ["मरण", "death"]],
              "ऊर्ध्वम् = above; चूचुक = nipple; शोणित-पूर्ण = full of blood; मरण = death.",
              "ऊर्ध्वम्, चूचुक, शोणित, पूर्ण, मरण.", role="extend",
              teaches="शोणितपूर्णकोष्ठस्य is a bahuvrīhi in the genitive: 'of one whose koṣṭha is full of blood'."),
        mcq("discriminate", 3, "Which split of स्तनचूचुकयोरूर्ध्वं in unit 24 is right?",
            ("स्तनचूचुकयोः + ऊर्ध्वम्", "ओ + visarga before a vowel → ओर्: -योरूर्ध्वम्."),
            [("स्तनचूचुकयो + रूर्ध्वम्", "रूर्ध्वम् is not a word; the र् comes from the visarga."),
             ("स्तनचूचुकयः + ऊर्ध्वम्", "अः before ऊ would drop to अ, with no र्."),
             ("स्तनचूचुकाः + ऊर्ध्वम्", "आः before a vowel drops its visarga, with no र्.")],
            "स्तनचूचुकयोः (of breast and nipple) + ऊर्ध्वम् (above).",
            "ओः + vowel → ओर्."),
        multi("apply", 4, "Which statements fit unit 24?",
              [("The stanarohita lie on both sides", "Right: उभयतः स्तनरोहिते."),
               ("The stanarohita lie below the breasts", "They lie above; below the breasts are the stanamūla (unit 23)."),
               ("The stated death is of one whose koṣṭha is full of Kapha", "Kapha is stated in unit 23; here it is blood."),
               ("The stated death is of one whose koṣṭha is full of blood", "Right: शोणितपूर्णकोष्ठस्य मरणम्.")],
              [0, 3],
              "Above, on both sides; death of one whose koṣṭha is full of blood.",
              "उभयतः स्तनरोहिते ... शोणितपूर्णकोष्ठस्य मरणम्."),
        mcq("transfer", 5, "By the rule of स्तनचूचुकयोरूर्ध्वं, how is हस्तयोः + उपरि (above the two hands) joined in a new example?",
            ("हस्तयोरुपरि", "ओ + visarga before a vowel → ओर्, as स्तनचूचुकयोः + ऊर्ध्वम्."),
            [("हस्तयो उपरि", "After ओ the visarga is not dropped before a vowel; it becomes र्."),
             ("हस्तयोस्उपरि", "स् comes from a visarga before त or थ, not before a vowel."),
             ("हस्तयवुपरि", "अव् comes from a bare ओ before a vowel; here the visarga gives र्.")],
            "हस्तयोः + उपरि = हस्तयोरुपरि, like स्तनचूचुकयोः + ऊर्ध्वम् = स्तनचूचुकयोरूर्ध्वम्.",
            "ओः + vowel → ओर्.",
            teaches="After ओ a visarga before a vowel becomes र्: स्तनचूचुकयोः + ऊर्ध्वम् → स्तनचूचुकयोरूर्ध्वम्."),
    ],
}

# ---------------------------------------------------------------- unit 25
AUTHORED["25"] = {
    "title": "उभयत्रोरसो नाड्यौ वातवहे अपस्तंभौ",
    "question": "By unit 25, what are the two apastambha, and how does death come there?",
    "rule": ("On both sides of the chest (उरसः), two channels (नाड्यौ) carrying vāta (wind): the two apastambha; in those "
             "two, death through the koṣṭha being full of blood, and through cough (कास) and śvāsa (probably breathlessness)."),
    "limits": ("Prose. वातवहे may also mean 'carrying Vāta' (the doṣa); the data keeps 'wind' and no question asks which. "
               "nāḍī is kept as 'channel, tube'; śvāsa = breathlessness is probable (also a disease name)."),
    "explain_hi": ("यह पंक्ति पार्श्व, पीठ और कंधे के मर्मों का खण्ड आरम्भ करती है: छाती के दोनों ओर दो नाड़ियाँ जो वात को ले जाती हैं, उनका नाम अपस्तम्भ। "
                   "‘वातवहे’ का अर्थ ‘वायु ले जाने वाली’ रखा गया है; ‘वात दोष ले जाने वाली’ भी सम्भव है। "
                   "उन दोनों में आघात से कोष्ठ रक्त से भर जाने के कारण, और कास (खाँसी) तथा श्वास (सम्भवतः साँस फूलना) से मृत्यु। "
                   "‘वातवहे अपस्तंभौ’ में ए पर समाप्त द्विवचन के बाद सन्धि नहीं होती, इसलिए पद अलग हैं। "
                   "‘उभयत्रोरसो’ में अ + उ → ओ हुआ है।"),
    "hook": "छाती की दो वात-वाही नाड़ियाँ: अपस्तम्भ; रक्त-भरा कोष्ठ, खाँसी, श्वास से मृत्यु।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 25, what are the two apastambha?",
            ("Two channels of the chest", "उभयत्रोरसो नाड्यौ: two channels (nāḍī) on both sides of the chest."),
            [("Two bones by the spine", "Two bones by the spine are the kaṭīkataruṇa (unit 27)."),
             ("Two joints of the flanks", "The side-joints are the pārśvasandhi (unit 30)."),
             ("Two plates of the shoulders", "The shoulder-plates are the aṃsaphalaka (unit 32).")],
            "The apastambha: two vāta-carrying channels on both sides of the chest.",
            "उभयत्रोरसो नाड्यौ वातवहे अपस्तंभौ."),
        order(1, "Put the printed parts of unit 25 in the line's order.",
              ["उभयत्रोरसो", "नाड्यौ वातवहे", "अपस्तंभौ", "तयोःशोणितपूर्णकोष्ठतया", "कासश्वासाभ्यां च", "मरणं"],
              "On both sides of the chest; two vāta-carrying channels; the apastambha; through blood-full koṣṭha; and through cough and śvāsa; death.",
              "उभयत्रोरसो → नाड्यौ वातवहे → अपस्तंभौ → तयोःशोणितपूर्णकोष्ठतया → कासश्वासाभ्यां च → मरणं."),
        match(2, "Match each word of unit 25 to its meaning.",
              [["उभयत्र", "on both sides"], ["उरस्", "chest"], ["नाडी", "channel, tube"], ["कास", "cough"],
               ["श्वास", "probably breathlessness"]],
              "उभयत्र = on both sides; उरस् = chest; नाडी = channel; कास = cough; श्वास = probably breathlessness.",
              "उभयत्र, उरस्, नाडी, कास, श्वास.", role="extend",
              teaches="कासश्वासाभ्याम् is a dvandva in the dual: cough and śvāsa together."),
        mcq("discriminate", 3, "Why does वातवहे stay unjoined before अपस्तंभौ in unit 25?",
            ("A dual ending in ए takes no vowel sandhi", "वातवहे is f. nom. dual; a dual in -ए stays as it is before a vowel."),
            [("ए before अ never changes in sandhi", "It usually does (ए + अ → एऽ); only the dual is exempt."),
             ("अपस्तंभौ begins with a consonant", "अपस्तंभौ begins with the vowel अ."),
             ("Names of marmas are never joined", "Marma names join freely (भागयोरपालापौ, unit 26).")],
            "वातवहे is a dual in -ए: such a dual is not joined with a following vowel.",
            "Dual -ई/-ऊ/-ए + vowel → no sandhi."),
        multi("apply", 4, "Which statements fit unit 25?",
              [("The two lie on both sides of the chest", "Right: उभयत्रोरसः."),
               ("Death comes through loss of blood", "Loss of blood is not stated; the koṣṭha is full of blood."),
               ("Death comes with cough and śvāsa", "Right: कासश्वासाभ्यां च मरणम्."),
               ("The two lie two aṅgulas below the breasts", "That is the place of the stanamūla (unit 23).")],
              [0, 2],
              "On both sides of the chest; death through blood-full koṣṭha and through cough and śvāsa.",
              "उभयत्रोरसो ... शोणितपूर्णकोष्ठतया कासश्वासाभ्यां च मरणम्."),
        mcq("transfer", 5, "By the rule of वातवहे अपस्तंभौ, how are बाले (two girls, nom. dual) + अत्र (here) written in a new example?",
            ("बाले अत्र", "A dual in -ए takes no sandhi before a vowel, as वातवहे अपस्तंभौ."),
            [("बालेऽत्र", "ए + अ → एऽ is for a word that is not a dual in -ए."),
             ("बालयत्र", "ए → अय् before a vowel is not used for a dual in -ए."),
             ("बाल्यत्र", "य् comes from इ before a vowel; बाले ends in ए.")],
            "बाले अत्र stays apart, like वातवहे अपस्तंभौ.",
            "Dual in -ए + vowel → no sandhi.",
            teaches="A dual ending in ई, ऊ or ए is not joined with a following vowel: वातवहे अपस्तंभौ."),
    ],
}

# ---------------------------------------------------------------- unit 26
AUTHORED["26"] = {
    "title": "अंसकूटयोरधः पार्श्वयोरुपरि अपालापौ",
    "question": "By unit 26, where are the two apālāpa, and how does death come there?",
    "rule": ("Below the two aṃsakūṭa (shoulder-tops), above the parts of the two sides (पार्श्व), are the two apālāpa; "
             "in those two, death by blood that has turned into pus (पूयत्वम् आपन्नेन रक्तेन)."),
    "limits": ("Prose, no verb. How भागयोः relates to the sides is not firm ('above the parts of the sides' or 'above, in "
               "the portions of the sides'), so no question rests on it. aṃsakūṭa = top of the shoulder; the acromion "
               "region is only probable."),
    "explain_hi": ("यह पंक्ति दो अपालाप मर्म बताती है: दोनों अंसकूट यानी कन्धे के शिखरों के नीचे, और दोनों पार्श्वों के भागों के ऊपर। "
                   "‘भागयोः’ का पार्श्वों से ठीक सम्बन्ध पक्का नहीं है। "
                   "उन दोनों में आघात से, पूय यानी मवाद बन चुके रक्त से मृत्यु। "
                   "‘आपन्नेन’ तृतीया है और ‘रक्तेन’ से मेल खाता है। "
                   "‘अंसकूटयोरधः’, ‘पार्श्वयोरुपरि’ और ‘भागयोरपालापौ’ में ओ के बाद का विसर्ग स्वर से पहले र् बना है।"),
    "hook": "कन्धे के शिखर के नीचे अपालाप: मवाद बने रक्त से मृत्यु।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 26, how does death come at the two apālāpa?",
            ("By blood turned into pus", "पूयत्वमापन्नेन रक्तेन मरणम्: by blood that has become pus."),
            [("By a mere loss of blood", "Loss of blood is the cause at the kaṭīkataruṇa (unit 27)."),
             ("By a koṣṭha full of Kapha", "That is stated for the stanamūla (unit 23)."),
             ("By pain and convulsions", "Neither pain nor convulsion is named in unit 26.")],
            "At the apālāpa: death by blood turned into pus.",
            "तयोः पूयत्वमापन्नेन रक्तेन मरणम्."),
        order(1, "Put the printed parts of unit 26 in the line's order.",
              ["अंसकूटयोरधः", "पार्श्वयोरुपरि", "भागयोरपालापौ", "तयोः", "पूयत्वमापन्नेन रक्तेन", "मरणं"],
              "Below the shoulder-tops; above the sides; of the parts, the apālāpa; in those two; by blood turned to pus; death.",
              "अंसकूटयोरधः → पार्श्वयोरुपरि → भागयोरपालापौ → तयोः → पूयत्वमापन्नेन रक्तेन → मरणं."),
        match(2, "Match each word of unit 26 to its meaning.",
              [["अंसकूट", "shoulder-top"], ["अधः", "below"], ["पार्श्व", "side, flank"], ["उपरि", "above"], ["पूय", "pus"]],
              "अंसकूट = shoulder-top; अधः = below; पार्श्व = side; उपरि = above; पूय = pus.",
              "अंसकूट, अधः, पार्श्व, उपरि, पूय.", role="extend",
              teaches="आपन्नेन (having turned into) agrees with रक्तेन in the instrumental: 'by blood that has become pus'."),
        mcq("discriminate", 3, "Which split of पूयत्वमापन्नेन in unit 26 is right?",
            ("पूयत्वम् + आपन्नेन", "म् joins the following vowel: पूयत्वमापन्नेन."),
            [("पूयत्व + मापन्नेन", "मापन्नेन is not a word; the म् ends पूयत्वम्."),
             ("पूयत्वा + आपन्नेन", "आ + आ would give पूयत्वापन्नेन, with no म्."),
             ("पूयत्वः + आपन्नेन", "अः before आ would drop to अ, with no म्.")],
            "पूयत्वम् (the state of pus) + आपन्नेन (having reached).",
            "Final म् + vowel → joined."),
        mcq("apply", 4, "By unit 26, the apālāpa lie below what?",
            ("The two shoulder-tops", "अंसकूटयोरधः: below the two aṃsakūṭa."),
            [("The two breasts", "Below the breasts lie the stanamūla (unit 23)."),
             ("The backs of the ears", "Below the backs of the ears lie the vidhura (unit 36)."),
             ("The ends of the brows", "Below the brow-ends lie the apāṅga (unit 38).")],
            "The apālāpa: below the shoulder-tops, above the parts of the sides.",
            "अंसकूटयोरधः पार्श्वयोरुपरि."),
        mcq("transfer", 5, "By the pattern of आपन्नेन रक्तेन, which form of उष्ण (hot) goes with जलेन (by water) in a new example?",
            ("उष्णेन", "An adjective takes the case of its noun: जलेन (instr.) → उष्णेन, as रक्तेन → आपन्नेन."),
            [("उष्णस्य", "उष्णस्य is genitive; it would not agree with जलेन."),
             ("उष्णम्", "उष्णम् is nominative or accusative, not instrumental."),
             ("उष्णात्", "उष्णात् is ablative, not instrumental.")],
            "उष्णेन जलेन = by hot water, like आपन्नेन रक्तेन = by blood that has turned.",
            "Adjective agrees with its noun in case: -एन with -एन.",
            teaches="An adjective or participle agrees with its noun in case, number and gender: आपन्नेन रक्तेन."),
    ],
}

# ---------------------------------------------------------------- unit 27
AUTHORED["27"] = {
    "title": "पृष्ठवंशमुभयतः कटीकतरुणे",
    "question": "By unit 27, where are the two kaṭīkataruṇa, and how does one die there?",
    "rule": ("On both sides of the spine (पृष्ठवंश), towards the two śroṇīkarṇa (hip-'ears'), two bones: the kaṭīkataruṇa; "
             "in those two, from loss of blood (शोणितक्षयात्), one dies pale, discoloured and of diminished appearance."),
    "limits": ("Prose. śroṇīkarṇa names a part of the pelvic region (again in unit 29); its exact structure is not firm, "
               "so no question asks what it is. 'prati' + accusative is read as 'towards'. The subject of म्रियते is "
               "unstated (the person)."),
    "explain_hi": ("यह पंक्ति दो कटीकतरुण मर्म बताती है: रीढ़ (पृष्ठवंश) के दोनों ओर, श्रोणीकर्णों की ओर, दो अस्थियाँ। "
                   "श्रोणीकर्ण श्रोणि-प्रदेश का एक भाग है; इसकी ठीक रचना पक्की नहीं (इकाई २९ में फिर आता है)। "
                   "उन दोनों में आघात से रक्त के क्षय के कारण व्यक्ति पाण्डु (फीका), विवर्ण (बदरंग) और क्षीण रूप वाला होकर मरता है। "
                   "‘म्रियते’ (मरता है) रूप में -यते है, पर इसका अर्थ कर्मवाच्य नहीं, ‘मरता है’ है। "
                   "‘श्रोणीकर्णावस्थिनी’ में औ स्वर से पहले आव् बना है।"),
    "hook": "रीढ़ के दोनों ओर दो अस्थियाँ: कटीकतरुण; रक्त-क्षय से फीका, बदरंग होकर मृत्यु।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 27, from what does one die at the kaṭīkataruṇa?",
            ("From loss of blood", "शोणितक्षयात्: from loss of blood (śoṇita)."),
            [("From blood turned to pus", "Blood turned to pus is the cause at the apālāpa (unit 26)."),
             ("From a koṣṭha full of Kapha", "That is stated for the stanamūla (unit 23)."),
             ("From cough and breathlessness", "Cough and śvāsa are named for the apastambha (unit 25).")],
            "At the kaṭīkataruṇa: from loss of blood one dies pale and discoloured.",
            "तयोः शोणितक्षयात् ... म्रियते."),
        order(1, "Put the printed parts of unit 27 in the line's order.",
              ["पृष्ठवंशमुभयतः", "प्रतिश्रोणीकर्णावस्थिनी", "कटीकतरुणे", "तयोः शोणितक्षयात्", "पांडुर्विवर्णो हीनरूपो म्रियते"],
              "On both sides of the spine; towards the hip-'ears', two bones; the kaṭīkataruṇa; in those, from loss of blood; pale, discoloured, diminished, dies.",
              "पृष्ठवंशमुभयतः → प्रतिश्रोणीकर्णावस्थिनी → कटीकतरुणे → तयोः शोणितक्षयात् → पांडुर्विवर्णो हीनरूपो म्रियते."),
        match(2, "Match each word of unit 27 to its meaning.",
              [["पृष्ठवंश", "spine"], ["क्षय", "loss"], ["पाण्डु", "pale"], ["विवर्ण", "discoloured"],
               ["हीनरूप", "of diminished appearance"]],
              "पृष्ठवंश = spine; शोणितक्षय = loss of blood; पाण्डु, विवर्ण, हीनरूप = pale, discoloured, diminished.",
              "पृष्ठवंश, क्षय, पाण्डु, विवर्ण, हीनरूप.", role="extend",
              teaches="पृष्ठवंश = पृष्ठ (back) + वंश (bamboo): the data's word for the spine (standard)."),
        mcq("discriminate", 3, "Which split of प्रतिश्रोणीकर्णावस्थिनी in unit 27 is right?",
            ("प्रति + श्रोणीकर्णौ + अस्थिनी", "औ before a vowel becomes आव्: -कर्णावस्थिनी."),
            [("प्रति + श्रोणीकर्णा + वस्थिनी", "वस्थिनी is not a word; the व् comes from औ."),
             ("प्रति + श्रोणीकर्णे + अस्थिनी", "A dual in -ए would stay apart (श्रोणीकर्णे अस्थिनी), with no व्."),
             ("प्रति + श्रोणीकर्णः + अस्थिनी", "अः + अ would give ओऽ (श्रोणीकर्णोऽस्थिनी).")],
            "प्रति (towards) + श्रोणीकर्णौ (the two hip-'ears') + अस्थिनी (two bones).",
            "औ + vowel → आव् + vowel."),
        fill(4, "Unit 27: पांडुर्विवर्णो हीनरूपो ____ (dies). Type it in Devanagari or in English letters (e.g. dharma).",
             accepts("म्रियते", None, "mriyate"),
             "म्रियते (dies): पाण्डुर्विवर्णो हीनरूपो म्रियते.",
             "म्रियते is the present, 3rd person singular (middle) of √मृ: 'dies'; -यते here is not a passive.",
             "हीनरूपः म्रियते.", role="apply"),
        mcq("transfer", 5, "By the rule of पांडुर्विवर्णो (पाण्डुः + विवर्णः), how is गुरुः + वदति (the teacher speaks) joined in a new example?",
            ("गुरुर्वदति", "उ + visarga before a voiced sound → र्, as पाण्डुः + विवर्णः → पाण्डुर्विवर्णः."),
            [("गुरो वदति", "ओ comes from अः before a voiced sound, not from उः."),
             ("गुरुस्वदति", "स् comes before त or थ, not before व."),
             ("गुरु वदति", "The visarga drops before a voiced sound after आ, not after उ.")],
            "गुरुः + वदति = गुरुर्वदति, like पाण्डुः + विवर्णः = पाण्डुर्विवर्णः.",
            "उः + voiced sound → उर्.",
            teaches="After इ or उ a visarga becomes र् before a voiced sound: पाण्डुः + विवर्णः → पाण्डुर्विवर्णः."),
    ],
}


# =================================================================== NOTES_HI
NOTES_HI = {
    "14": ("गद्य; विश्वास उच्च। पाठ-चिह्न (लगभग निश्चित): छपा ‘षांढ्यमल्पशुकृता’; ‘शुकृता’ शब्द नहीं, ‘अल्पशुक्रता’ (वीर्य की अल्पता) "
           "पढ़ा गया; र का ऋ छपाई की भूल; इस शब्द के रूप पर कोई प्रश्न नहीं। षाण्ढ्य = नपुंसकता (सम्भावित अर्थ); वृषण = अण्डकोष "
           "(थैली भी)। सन्धि जाँची: विटपम् + तत्र → विटपं तत्र (व्यंजन से पहले म् → ं); षाण्ढ्यम् + अल्प → षाण्ढ्यमल्प (स्वर से पहले म् जुड़ता है); "
           "छपा वंक्षण, षांढ्य (ं = ङ्/ण्)।"),
    "15": ("गद्य; विश्वास मध्यम; कोई पाठ-चिह्न नहीं। अधूरा वाक्य: न क्रिया, न मर्म का नाम; डेटा कुछ नहीं जोड़ता। समूह-टिप्पणी: इकाई १६ "
           "और १७ इसे आगे बढ़ाती प्रतीत होती हैं। सन्धि जाँची: सक्थिवत् + बाह्वोः → सक्थिवद्बाह्वोः (घोष ब से पहले त् → द्)। बाह्वोः = "
           "सप्तमी द्विवचन।"),
    "16": ("गद्य; विश्वास मध्यम। पाठ-चिह्न (सम्भावित): छपा ‘कुणित’ शायद ‘कुणित्वं’ (इकाई १७ में यही फल) के लिए; अर्थ नहीं बदलता। "
           "पंक्ति नाम केवल साथ रखती है; ‘गुल्फ = मणिबन्ध, जानु = कूर्पर’ डेटा का मेल-पाठ है। छपा ‘जानुकूर्परंतयोर्व्यधे’ एक पद में जुड़ा "
           "(जानु + कूर्परम् + तयोः + व्यधे)। समूह-टिप्पणी: इकाई १५ को आगे बढ़ाती प्रतीत होती है। सन्धि जाँची: विशेषः + तु → विशेषस्तु; "
           "मणिबन्धः + तथा → मणिबन्धस्तथा (त से पहले विसर्ग → स्); गुल्फः + मणि → गुल्फो (अः + घोष व्यंजन → ओ); तयोः + व्यधे → "
           "तयोर्व्यधे (ओ के बाद विसर्ग + घोष → र्)।"),
    "17": ("गद्य; विश्वास निम्न। पाठ-चिह्न (सम्भावित): छपा ‘कक्षाक्षमध्ये’; अक्ष ज्ञात अंग नहीं (अक्षक = हँसली होता); ‘कक्षावक्षसोर्मध्ये’ "
           "(काँख और छाती के बीच) सम्भावित पाठ, अपनाया नहीं; अक्ष का अर्थ अस्पष्ट छोड़ा गया; स्थान पर कोई प्रश्न नहीं। ‘विटप के "
           "समान’ = इकाई १४ के विटप का भुजा वाला प्रतिरूप (डेटा का पाठ)। छपा ‘कक्षाधारः’ (दीर्घ आ); इकाई ५६ और ६४ में ‘कक्षाधर’। "
           "सन्धि जाँची: विटपवत् + च → विटपवच्च (च से पहले त् → च्); छपाई में ‘कक्षाधारः तत्र’ विसर्ग बना रहा (सन्धि करने पर "
           "कक्षाधारस्तत्र)।"),
    "18": ("गद्य; विश्वास मध्यम; कोई पाठ-चिह्न नहीं। समास में ‘निरसन’ गुद का विशेषण है या स्थूलान्त्र का, तय नहीं; डेटा इसे आँत के साथ "
           "रखता है; इस पर कोई प्रश्न नहीं। वात = वायु (अधोवायु), दोष-अर्थ नहीं लिया। स्थूलान्त्र = बड़ी आँत (मानक); गुद = गुदा और "
           "मलाशय का अन्त। सन्धि जाँची: वर्चः + निरसन → वर्चोनिरसन (अः + घोष न → ओ); स्थूल + अन्त्र → स्थूलान्त्र (अ + अ → आ); "
           "प्रतिबद्धः + गुदः → प्रतिबद्धो गुदः; सद्यः + मरणम् → सद्यो मरणं (अः + घोष व्यंजन → ओ)।"),
    "19": ("गद्य; विश्वास निम्न। पाठ-चिह्न (सम्भावित): छपा ‘क्टचा’ शब्द नहीं (क के बाद स्वर नहीं); ‘कट्याः’ (कटि के भीतर) या ‘त्वचा’ "
           "सम्भावित, अपनाए नहीं; शब्द अविभाजित; वाक्य अनुमानित पाठ पर; इस शब्द पर कोई प्रश्न नहीं। अश्मरी = मूत्र की पथरी (मानक); "
           "बस्ति = मूत्राशय (मानक)। ‘अश्मरीव्रण’ = पथरी निकालने का घाव, यह स्वाभाविक अर्थ है, छपा नहीं। ऋते + पञ्चमी। समूह-टिप्पणी: "
           "इकाई २० इसे आगे बढ़ाती है। सन्धि जाँची: शोणितः + अभ्यन्तरतः → शोणितोऽभ्यन्तरतः; एकद्वारः + अधोमुखः → एकद्वारोऽधोमुखः "
           "(अः + अ → ओऽ); धनुः + वक्र → धनुर्वक्र (उ के बाद विसर्ग + घोष → र्); धनुर्वक्रः + एक → धनुर्वक्र एक (अः + अ से भिन्न स्वर → अ); "
           "अधोमुखः + बस्तिः → अधोमुखो बस्तिः; तत्र + अपि → तत्रापि; मरणम् + अश्मरी → मरणमश्मरी; व्रणात् + ऋते → व्रणादृते (स्वर से "
           "पहले त् → द्)।"),
    "20": ("गद्य; विश्वास उच्च; कोई पाठ-चिह्न नहीं। ‘जीवति’ का कर्ता (व्यक्ति) छपा नहीं; ‘सः’ = वह व्रण। उपक्रान्त = उपचारित; "
           "रोहति = भर जाता है। समूह-टिप्पणी: इकाई १९ (बस्ति) को आगे बढ़ाती प्रतीत होती है। सन्धि जाँची: तत्र + अपि + उभयतः → "
           "तत्राप्युभयतः (अ + अ → आ; इ + उ → यु); उभयतः + विद्धे → उभयतो विद्धे; एकतः + भिन्ने → एकतो भिन्ने; व्रणः + भवति → "
           "व्रणो भवति (अः + घोष व्यंजन → ओ); सः + तु → स तु (सः का विसर्ग व्यंजन से पहले लुप्त); यत्नेन + उपक्रान्तः → यत्नेनोपक्रान्तः "
           "(अ + उ → ओ); उपक्रान्तः + रोहति → उपक्रान्तो रोहति। छपाई में ‘जीवति एकतो’ अलग (सन्धि करने पर जीवत्येकतो)।"),
    "21": ("गद्य; विश्वास मध्यम। पाठ-चिह्न (सम्भावित): छपा ‘पक्का-’ प्राकृत जैसा रूप; संस्कृत ‘पक्व’; व/क की भ्रान्ति। ‘पक्व’ से "
           "पक्वाशय (सम्भवतः नीचे की आँत) समझा जाता है, पर ‘आशय’ पक्व के बाद छपा नहीं; इस पर कोई प्रश्न नहीं। आमाशय: डेटा की "
           "शब्द-सूची में ‘मानक’ (जठर), अनुवाद में ‘सम्भवतः जठर’; कार्ड ‘सम्भवतः’ रखता है। नाभि = नाभि (मानक)। सन्धि जाँची: पक्व + "
           "आमाशय → पक्वामाशय (अ + आ → आ); तत्र + अपि → तत्रापि (अ + अ → आ); सद्यः + मरणम् → सद्यो मरणं; छपाई में ‘नाभिः तत्रापि’ "
           "विसर्ग बना रहा।"),
    "22": ("गद्य; विश्वास मध्यम। पाठ-चिह्न: छपा ‘मध्येसत्वरजस्तमोधिष्ठान’; मध्ये अगले शब्द से जुड़ा, और तमः + अधिष्ठानम् → "
           "तमोऽधिष्ठानम् का अवग्रह छूटा; ‘सत्व’ = सत्त्व (वर्तनी)। कोष्ठ-वक्षसोः द्वन्द्व, षष्ठी द्विवचन (पेट और छाती के बीच), डेटा का "
           "पाठ। आमाशय = कच्चे अन्न का आशय (सम्भवतः जठर), आम (फल) नहीं। हृदय = हृदय (मानक)। सन्धि जाँची: स्तनयोः + च → स्तनयोश्च "
           "(च से पहले विसर्ग → श्); रजः + तमः → रजस्तमः (त से पहले विसर्ग → स्); अधिष्ठानम् + आमाशय → अधिष्ठानमामाशय; तत्र + अपि → "
           "तत्रापि।"),
    "23": ("गद्य; विश्वास मध्यम; कोई पाठ-चिह्न नहीं। ‘स्तनमूले’ द्विवचन (दो मर्म, दोनों ओर)। ‘तयोः’ = उन दोनों में (बिंधने पर)। मृत्यु "
           "‘कफ से भरे कोष्ठ वाले’ की कही गई; पंक्ति इससे अधिक नहीं कहती। सन्धि जाँची: स्तनयोः + अधस्तात् → स्तनयोरधस्तात् (ओ के बाद "
           "विसर्ग + स्वर → र्); द्वि + अङ्गुलम् → द्व्यङ्गुलम् (इ + अ → य); द्व्यङ्गुलम् + उभयतः → द्व्यङ्गुलमुभयतः; छपाई में ‘अधस्तात् "
           "द्व्यंगुलम्’ अलग (सन्धि करने पर अधस्ताद्द्व्यङ्गुलम्)।"),
    "24": ("गद्य; विश्वास मध्यम। पाठ-चिह्न (सम्भावित): छपा ‘सद्यो’ श से पहले अनियमित; ‘सद्यः’ या ‘सद्यश्’ अपेक्षित; इस पर कोई प्रश्न नहीं। "
           "डेटा की टिप्पणी ‘स्तनचूचुक’ को द्वन्द्व (स्तन और चूचुक) पढ़ती है, जबकि अनुवाद ‘दोनों चूचुक / स्तनाग्र’ कहता है; विग्रह पर कोई "
           "प्रश्न नहीं। इकाई २३ और २५ के विपरीत ‘तयोः’ नहीं। सन्धि जाँची: स्तनचूचुकयोः + ऊर्ध्वम् → स्तनचूचुकयोरूर्ध्वम् (ओ के बाद "
           "विसर्ग + स्वर → र्); द्वि + अङ्गुलम् → द्व्यङ्गुलम्।"),
    "25": ("गद्य; विश्वास मध्यम; कोई पाठ-चिह्न नहीं। ‘वातवहे’ = वायु ले जाने वाली (डेटा); ‘वात दोष ले जाने वाली’ भी सम्भव; इस पर कोई "
           "प्रश्न नहीं। नाडी = नली, नाड़ी (सिद्धान्त-शब्द)। श्वास = साँस फूलना (सम्भावित; रोग का नाम भी)। छपा ‘तयोःशोणित’ बिना अन्तर। "
           "सन्धि जाँची: उभयत्र + उरसः → उभयत्रोरसः (अ + उ → ओ); उरसः + नाड्यौ → उरसो नाड्यौ (अः + घोष न → ओ); वातवहे अपस्तंभौ "
           "अलग (ए पर समाप्त द्विवचन, प्रगृह्य: सन्धि नहीं); -आभ्याम् + च → -आभ्यां च।"),
    "26": ("गद्य; विश्वास मध्यम; कोई पाठ-चिह्न नहीं। ‘पार्श्वयोरुपरि भागयोः’ = पार्श्वों के भागों के ऊपर; ‘ऊपर, पार्श्वों के भागों में’ भी "
           "सम्भव; इस पर कोई प्रश्न नहीं। अंसकूट = कन्धे का शिखर (सम्भवतः एक्रोमियन प्रदेश)। इकाई ५५ में इसी मर्म का नाम ‘अलाप’ "
           "छपा है। सन्धि जाँची: अंसकूटयोः + अधः → अंसकूटयोरधः; पार्श्वयोः + उपरि → पार्श्वयोरुपरि; भागयोः + अपालापौ → "
           "भागयोरपालापौ (ओ के बाद विसर्ग + स्वर → र्); पूयत्वम् + आपन्नेन → पूयत्वमापन्नेन।"),
    "27": ("गद्य; विश्वास मध्यम; कोई पाठ-चिह्न नहीं। ‘प्रति’ + द्वितीया = की ओर। श्रोणीकर्ण श्रोणि-प्रदेश का एक भाग (इकाई २९ में फिर), "
           "ठीक रचना पक्की नहीं। ‘म्रियते’ वर्तमान, प्रथम पुरुष एकवचन, आत्मनेपद: ‘मरता है’ (कर्मवाच्य नहीं)। कर्ता (व्यक्ति) छपा नहीं। "
           "सन्धि जाँची: पृष्ठवंशम् + उभयतः → पृष्ठवंशमुभयतः; श्रोणीकर्णौ + अस्थिनी → श्रोणीकर्णावस्थिनी (औ + स्वर → आव्); पाण्डुः + "
           "विवर्णः → पाण्डुर्विवर्णः (उ के बाद विसर्ग + घोष → र्); विवर्णः + हीनरूपः → विवर्णो हीनरूपः; हीनरूपः + म्रियते → हीनरूपो म्रियते "
           "(अः + घोष व्यंजन → ओ)।"),
}


# ===================================================================== AIDS
AIDS = {
    "14": {
        "diagram": {"groups": [
            {"label": "विटप (इकाई १४)", "items": ["स्थान: वंक्षण और वृषण के बीच", "फल: षाण्ढ्य (सम्भवतः नपुंसकता)",
                                               "वा: या अल्पशुकृता (छपा; पाठ अल्पशुक्रता, वीर्य की कमी)"]}]},
        "chunks": "वंक्षणवृषणमध्ये | विटपं | तत्र | षांढ्यमल्पशुकृता | वा",
        "sandhi": ("व्यंजन से पहले अन्तिम म् → ं: विटपम् + तत्र → विटपं तत्र · स्वर से पहले म् जुड़ता है: षाण्ढ्यम् + अल्प → "
                   "षाण्ढ्यमल्प।"),
        "frame": "कहाँ: वंक्षणवृषणमध्ये → नाम: विटपम् → फल: षाण्ढ्यम् वा अल्पशुक्रता (वा = अथवा)।",
    },
    "15": {
        "frame": "किसके समान: सक्थिवत् (पैर के समान) → कहाँ: बाह्वोः (दोनों भुजाओं में) → क्रिया और मर्म-नाम: छपे नहीं।",
        "sandhi": "घोष व्यंजन से पहले त् → द्: सक्थिवत् + बाह्वोः → सक्थिवद्बाह्वोः।",
        "anchors": "‘-वत्’ = ‘के समान’: सक्थिवत्, विटपवत् (इकाई १७)। (मेरी याद-पद्धति)",
    },
    "16": {
        "diagram": {"groups": [
            {"label": "सक्थि (पैर) → बाहु (भुजा), डेटा का मेल-पाठ", "items": ["गुल्फ → मणिबन्ध (कलाई)", "जानु → कूर्पर (कोहनी)",
                                                                       "उन दोनों के व्यध पर: कुणित (टेढ़ापन)"]}]},
        "chunks": "विशेषस्तु | गुल्फो | मणिबंधस्तथा | जानुकूर्परं | तयोर्व्यधे | कुणित",
        "sandhi": ("त से पहले विसर्ग → स्: विशेषः + तु → विशेषस्तु, मणिबन्धः + तथा → मणिबन्धस्तथा · अः + घोष व्यंजन → ओ: "
                   "गुल्फः + मणि → गुल्फो मणि · ओ के बाद विसर्ग + घोष → र्: तयोः + व्यधे → तयोर्व्यधे।"),
        "anchors": "टखना ↔ कलाई, घुटना ↔ कोहनी: शरीर के दोनों ओर के जोड़ों की जोड़ी। (मेरी याद-पद्धति, डेटा के मेल-पाठ पर)",
    },
    "17": {
        "chunks": "विटपवच्च | कक्षाक्षमध्ये | कक्षाधारः | तत्र | कुणित्वं",
        "frame": "किसके समान: विटपवत् (इकाई १४ का विटप) → कहाँ: कक्षा और ‘अक्ष’ (अर्थ अनिश्चित) के बीच → नाम: कक्षाधारः → फल: कुणित्वम्।",
        "sandhi": "च से पहले त् → च्: विटपवत् + च → विटपवच्च।",
    },
    "18": {
        "chain": {"steps": ["वात और वर्चस् (मल) का निरसन", "स्थूलान्त्र (बड़ी आँत) से प्रतिबद्ध", "गुद (गुदा)",
                            "तत्र सद्यो मरणम्: तुरन्त मृत्यु"]},
        "chunks": "वातवर्चोनिरसनस्थूलांत्रप्रतिबद्धो | गुदः | तत्र | सद्यो मरणं",
        "sandhi": ("अः + घोष व्यंजन → ओ: वर्चः + निरसन → वर्चोनिरसन, प्रतिबद्धः + गुदः → प्रतिबद्धो गुदः, सद्यः + मरणम् → सद्यो मरणम्।"),
    },
    "19": {
        "diagram": {"groups": [
            {"label": "बस्ति (मूत्राशय) के छपे लक्षण, पंक्ति-क्रम में", "items": ["१ अल्पमांसशोणित: कम मांस-रक्त",
                                                                         "२ अभ्यंतरतः क्टचा: अस्पष्ट शब्द",
                                                                         "३ धनुर्वक्र: धनुष-सी टेढ़ी", "४ एकद्वार: एक द्वार",
                                                                         "५ अधोमुख: नीचे की ओर मुख",
                                                                         "फल: सद्यो मरण, अश्मरी-व्रण को छोड़कर"]}]},
        "chunks": "अल्पमांसशोणितोऽभ्यंतरतः | क्टचा | धनुर्वक्र | एकद्वारोऽधोमुखो | बस्तिः | तत्रापि सद्यो मरणमश्मरीव्रणादृते",
        "sandhi": ("अः + अ → ओऽ: एकद्वारः + अधोमुखः → एकद्वारोऽधोमुखः · उ के बाद विसर्ग + घोष → र्: धनुः + वक्र → धनुर्वक्र · "
                   "स्वर से पहले त् → द्: व्रणात् + ऋते → व्रणादृते।"),
        "pegs": "धनुष (वक्र) + एक द्वार + नीचे मुख: उलटे धनुष-सी थैली। (मेरा बनाया चित्र, केवल याद के लिए)",
    },
    "20": {
        "diagram": {"groups": [
            {"label": "वहाँ भी (सम्भवतः बस्ति, इकाई १९)", "items": ["उभयतः विद्धे: दोनों ओर बिंधे → न जीवति",
                                                                 "एकतः भिन्ने: एक ओर फटे → मूत्रस्रावी व्रण",
                                                                 "यत्न से उपक्रान्त → रोहति (भर जाता है)"]}]},
        "seesaw": "उभयतः (दोनों ओर) ⇄ एकतः (एक ओर): दोनों इसी पंक्ति में; पहले से मृत्यु, दूसरे से भरने वाला घाव।",
        "chunks": "तत्राप्युभयतो विद्धे | न जीवति | एकतो भिन्ने | मूत्रस्रावी व्रणो भवति | स तु यत्नेनोपक्रांतो रोहति",
        "sandhi": "अ + उ → ओ: यत्नेन + उपक्रान्तः → यत्नेनोपक्रान्तः · अः + घोष व्यंजन → ओ: व्रणः + भवति → व्रणो भवति।",
    },
    "21": {
        "frame": "कहाँ: पक्व और आमाशय (सम्भवतः जठर) के बीच → नाम: नाभिः → फल: तत्रापि सद्यो मरणम् (वहाँ भी तुरन्त मृत्यु)।",
        "chunks": "पक्कामाशयमध्ये | नाभिः | तत्रापि | सद्यो मरणं",
        "sandhi": "अ + अ → आ: तत्र + अपि → तत्रापि · अ + आ → आ: पक्व + आमाशय → पक्वामाशय।",
    },
    "22": {
        "diagram": {"groups": [
            {"label": "हृदय (इकाई २२)", "items": ["स्थान: कोष्ठ-वक्ष और दोनों स्तनों के बीच", "सत्त्व, रज, तम का अधिष्ठान",
                                               "आमाशय (सम्भवतः जठर) का द्वार", "फल: वहाँ भी सद्यो मरण"]}]},
        "chunks": "कोष्ठवक्षसोः | स्तनयोश्च | मध्येसत्वरजस्तमोधिष्ठानमामाशयद्वारं | हृदयं | तत्रापि सद्यो मरणं",
        "sandhi": "च से पहले विसर्ग → श्: स्तनयोः + च → स्तनयोश्च · त से पहले विसर्ग → स्: रजः + तमः → रजस्तमः।",
    },
    "23": {
        "frame": "कहाँ: स्तनों के नीचे दो अंगुल, दोनों ओर → नाम: स्तनमूले (दो) → फल: कफपूर्णकोष्ठ वाले की मृत्यु।",
        "chunks": "स्तनयोरधस्तात् | द्व्यंगुलमुभयतः | स्तनमूले | तयोः | कफपूर्णकोष्ठस्य | मरणं",
        "sandhi": "इ + अ → य: द्वि + अङ्गुलम् → द्व्यङ्गुलम् · ओ के बाद विसर्ग + स्वर → र्: स्तनयोः + अधस्तात् → स्तनयोरधस्तात्।",
    },
    "24": {
        "frame": "कहाँ: स्तनचूचुक के ऊपर दो अंगुल, दोनों ओर → नाम: स्तनरोहिते (दो) → फल: शोणितपूर्णकोष्ठ वाले की मृत्यु।",
        "chunks": "स्तनचूचुकयोरूर्ध्वं | द्व्यंगुलमुभयतः | स्तनरोहिते | सद्यो | शोणितपूर्णकोष्ठस्य | मरणं",
        "sandhi": "ओ के बाद विसर्ग + स्वर → र्: स्तनचूचुकयोः + ऊर्ध्वम् → स्तनचूचुकयोरूर्ध्वम् (छपा ‘सद्यो’ श से पहले अनियमित)।",
    },
    "25": {
        "chain": {"steps": ["उभयत्र उरसः: छाती के दोनों ओर", "दो नाड़ियाँ, वातवह", "नाम: अपस्तम्भ",
                            "शोणितपूर्णकोष्ठता से", "और कास-श्वास से: मरण"]},
        "chunks": "उभयत्रोरसो | नाड्यौ वातवहे | अपस्तंभौ | तयोःशोणितपूर्णकोष्ठतया | कासश्वासाभ्यां च | मरणं",
        "sandhi": ("ए पर समाप्त द्विवचन के बाद सन्धि नहीं: वातवहे अपस्तंभौ · अ + उ → ओ: उभयत्र + उरसः → उभयत्रोरसः · अः + घोष "
                   "व्यंजन → ओ: उरसः + नाड्यौ → उरसो नाड्यौ।"),
    },
    "26": {
        "frame": "कहाँ: अंसकूटों के नीचे, पार्श्वों के भागों के ऊपर → नाम: अपालापौ (दो) → फल: पूय बने रक्त से मृत्यु।",
        "chunks": "अंसकूटयोरधः | पार्श्वयोरुपरि | भागयोरपालापौ | तयोः | पूयत्वमापन्नेन रक्तेन | मरणं",
        "sandhi": ("ओ के बाद विसर्ग + स्वर → र्: अंसकूटयोः + अधः → अंसकूटयोरधः, पार्श्वयोः + उपरि → पार्श्वयोरुपरि · स्वर से पहले "
                   "म् जुड़ता है: पूयत्वम् + आपन्नेन → पूयत्वमापन्नेन।"),
    },
    "27": {
        "diagram": {"groups": [
            {"label": "कटीकतरुण (इकाई २७)", "items": ["पृष्ठवंश के दोनों ओर", "श्रोणीकर्णों की ओर दो अस्थियाँ",
                                                    "शोणितक्षय से", "पाण्डु, विवर्ण, हीनरूप", "म्रियते: मरता है"]}]},
        "chunks": "पृष्ठवंशमुभयतः | प्रतिश्रोणीकर्णावस्थिनी | कटीकतरुणे | तयोः शोणितक्षयात् | पांडुर्विवर्णो हीनरूपो म्रियते",
        "sandhi": ("औ + स्वर → आव्: श्रोणीकर्णौ + अस्थिनी → श्रोणीकर्णावस्थिनी · उ के बाद विसर्ग + घोष → र्: पाण्डुः + विवर्णः → "
                   "पाण्डुर्विवर्णः · अः + घोष व्यंजन → ओ: हीनरूपः + म्रियते → हीनरूपो म्रियते।"),
    },
}


# ============================================================== IMAGE_SPECS
IMAGE_SPECS = {
    ("14", "diagram"): {
        "file": "sh7-vitapa-14.svg",
        "alt": ("Table of unit 14: place, between the groin and the testes; name, viṭapa; result, ṣāṇḍhya (probably "
                "impotence) or scanty śukra (printed alpaśukṛtā, read alpaśukratā)."),
        "type": "table",
        "title": "इकाई १४: विटप",
        "heads": ["क्या", "पंक्ति में"],
        "rows": [["स्थान", "वंक्षण और वृषण के बीच"], ["नाम", "विटपम्"], ["फल", "षाण्ढ्य (सम्भवतः नपुंसकता)"],
                 ["वा (या)", "अल्पशुकृता (छपा): वीर्य की कमी"]],
    },
    ("16", "diagram"): {
        "file": "sh7-gulpha-manibandha-16.svg",
        "alt": ("Table of unit 16 as the data reads it: gulpha (ankle) in the leg, maṇibandha (wrist) in the arm; jānu "
                "(knee) in the leg, kūrpara (elbow) in the arm; piercing of those two gives kuṇita, crookedness."),
        "type": "table",
        "title": "इकाई १६: विशेष (डेटा का मेल-पाठ)",
        "heads": ["सक्थि (पैर) में", "बाहु (भुजा) में"],
        "rows": [["गुल्फ (टखना)", "मणिबन्ध (कलाई)"], ["जानु (घुटना)", "कूर्पर (कोहनी)"],
                 ["उन दोनों का व्यध", "कुणित: टेढ़ापन"]],
    },
    ("19", "diagram"): {
        "file": "sh7-basti-19.svg",
        "alt": ("Table of unit 19 in line order: little flesh and blood; inside, kṭacā (unclear word); bow-curved; one "
                "opening; mouth downward; result: immediate death except from the aśmarī (urinary stone) wound."),
        "type": "table",
        "title": "इकाई १९: बस्ति (मूत्राशय)",
        "heads": ["छपा शब्द", "अर्थ"],
        "rows": [["१ अल्पमांसशोणित", "कम मांस और रक्त"], ["२ अभ्यंतरतः क्टचा", "अस्पष्ट शब्द"],
                 ["३ धनुर्वक्र", "धनुष-सी टेढ़ी"], ["४ एकद्वार", "एक द्वार"], ["५ अधोमुख", "नीचे की ओर मुख"],
                 ["फल", "सद्यो मरण, अश्मरी-व्रण को छोड़"]],
    },
    ("20", "diagram"): {
        "file": "sh7-basti-vyadha-20.svg",
        "alt": ("Flowchart of unit 20: there too (apparently the basti); pierced on both sides, one does not live; split "
                "on one side, a urine-discharging wound, which treated with effort heals."),
        "type": "mermaid",
        "code": ("flowchart TD\n"
                 "  A[\"वहाँ भी: सम्भवतः बस्ति\"] --> B[\"उभयतः विद्धे: दोनों ओर\"]\n"
                 "  A --> C[\"एकतः भिन्ने: एक ओर\"]\n"
                 "  B --> D[\"न जीवति\"]\n"
                 "  C --> E[\"मूत्रस्रावी व्रण\"]\n"
                 "  E --> F[\"यत्न से उपक्रान्त\"]\n"
                 "  F --> G[\"रोहति: भर जाता है\"]\n"),
    },
    ("22", "diagram"): {
        "file": "sh7-hridaya-22.svg",
        "alt": ("Table of unit 22: the hṛdaya (heart) lies between belly and chest and between the two breasts; seat of "
                "sattva, rajas and tamas; gate of the āmāśaya (probably the stomach); there too immediate death."),
        "type": "table",
        "title": "इकाई २२: हृदय",
        "heads": ["क्या", "पंक्ति में"],
        "rows": [["स्थान", "कोष्ठ-वक्ष, दोनों स्तनों के बीच"], ["अधिष्ठान", "सत्त्व, रज, तम"],
                 ["द्वार", "आमाशय का (सम्भवतः जठर)"], ["फल", "वहाँ भी सद्यो मरण"]],
    },
    ("25", "chain"): {
        "file": "sh7-apastambha-25.svg",
        "alt": ("Chain of unit 25 in line order: on both sides of the chest; two vāta-carrying channels; named "
                "apastambha; through the koṣṭha full of blood; and through cough and śvāsa, death."),
        "type": "chain",
        "title": "इकाई २५: अपस्तम्भ",
        "steps": ["उभयत्र उरसः: छाती के दोनों ओर", "दो नाड़ियाँ, वातवह", "नाम: अपस्तम्भ",
                  "शोणितपूर्णकोष्ठता से", "और कास-श्वास से: मरण"],
    },
    ("27", "diagram"): {
        "file": "sh7-katikataruna-27.svg",
        "alt": ("Flowchart of unit 27: on both sides of the spine, two bones towards the hip-'ears', the kaṭīkataruṇa; "
                "from loss of blood one becomes pale, discoloured and diminished, and dies."),
        "type": "mermaid",
        "code": ("flowchart TD\n"
                 "  A[\"पृष्ठवंश के दोनों ओर\"] --> B[\"श्रोणीकर्णों की ओर दो अस्थि\"]\n"
                 "  B --> C[\"कटीकतरुण\"]\n"
                 "  C --> D[\"शोणितक्षय से\"]\n"
                 "  D --> E[\"पाण्डु, विवर्ण, हीनरूप\"]\n"
                 "  E --> F[\"म्रियते: मरता है\"]\n"),
    },
}
