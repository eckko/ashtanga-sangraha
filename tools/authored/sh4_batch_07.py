from helpers import mcq, match, order, fill, multi, accepts


AUTHORED = {}

# ---------------------------------------------------------------- unit 82
AUTHORED["82"] = {
    "title": "शूलमधिकमुपजायते ... मृतगर्भां विद्यान्",
    "question": "By unit 82, by what signs should one know a woman to be mṛtagarbhā, one with a dead fetus?",
    "rule": ("Excess pain arises, the fetus does not move (न स्पन्दते), the yoni does not flow; she is restless, weeps day "
             "and night, breathes with difficulty, wastes away (probable sense of क्षयति): know such a woman as mṛtagarbhā (मृतगर्भा)."),
    "limits": ("Low confidence. संस्येते (of the eyes) is not a known verb; 'sink in' is a conjecture. The noun of "
               "अन्यानि is not stated. स्वप्निति is read स्वपिति. 'Wastes away' (क्षयति) is probable. No question rests on "
               "these. Modern equivalent (probable): intrauterine fetal death. Prose."),
    "explain_hi": ("यह लम्बी गद्य-पंक्ति मृत गर्भ के लक्षण गिनाती है। "
                   "अत्यधिक शूल यानी पीड़ा होती है, गर्भ हिलता नहीं (न च स्पन्दते), और योनि से स्राव नहीं होता (न स्रवति)। "
                   "स्त्री भृश अरति यानी बहुत बेचैनी से घिरी कष्ट पाती है, अलग ढंग से चेष्टा करती है, निढाल होती और थकती है, "
                   "दिन-रात रोती है, हर श्वास पर कठिनाई से साँस लेती है और अत्यन्त कष्ट से जीती है। "
                   "ऐसी स्त्री को मृतगर्भा यानी मरे गर्भ वाली जाने (विद्यात्)। "
                   "आँखों वाली क्रिया ‘संस्येते’ अस्पष्ट है, और ‘अन्यानि’ (अन्य) की संज्ञा नहीं दी गई; इन पर कोई प्रश्न नहीं।"),
    "hook": "पीड़ा बढ़े, गर्भ न हिले, स्त्री बेचैन रोए: मृतगर्भा।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 82, what should one know a woman with these signs to be?",
            ("Mṛtagarbhā, with a dead fetus", "एवंविधां स्त्रियं मृतगर्भां विद्यात्: know such a woman as mṛtagarbhā."),
            [("Upaviṣṭaka, with a throbbing fetus", "Upaviṣṭaka, where the fetus throbs, is the name in unit 41."),
             ("Nāgodara, with a belly that shrinks", "Nāgodara is a name given in unit 43, not here."),
             ("Āpannagarbhā, a pregnant woman", "Āpannagarbhā (pregnant) is the word of unit 2; here the fetus is dead.")],
            "Such a woman one should know as mṛtagarbhā, one whose fetus is dead.",
            "एवंविधां स्त्रियं मृतगर्भां विद्यात्."),
        order(1, "Put these phrases of unit 82 in the line's order.",
              ["शूलमधिकमुपजायते", "न च स्पंदते गर्भः", "न स्रवति योनिः", "भृशमरतिपरीता व्यथते",
               "रोदित्यहर्निशं", "एवंविधां स्त्रियं मृतगर्भां"],
              "Pain arises in excess; the fetus does not move; the yoni does not flow; greatly restless she is distressed; "
              "she weeps day and night; such a woman (know as) mṛtagarbhā.",
              "शूल → न स्पन्दते → न स्रवति → अरति → रोदिति → मृतगर्भा."),
        match(2, "Match each word of unit 82 to its meaning.",
              [["शूल", "pain"], ["स्पन्दते", "moves, quivers"], ["अरति", "restlessness, discontent"],
               ["अहर्निशम्", "day and night"], ["कृच्छ्रात्", "with difficulty"]],
              "Pain, a fetus that does not move, restlessness, weeping day and night, breathing with difficulty.",
              "शूल, स्पन्दते, अरति, अहर्निशम्, कृच्छ्रात्.", role="extend",
              teaches="मृतगर्भा is a bahuvrīhi: she whose garbha (fetus) is मृत (dead)."),
        mcq("discriminate", 3, "Which split of कृच्छ्राच्छ्वसिति is right?",
            ("कृच्छ्रात् + श्वसिति", "त् before श becomes च्, and the श here becomes छ: त् + श → च्छ."),
            [("कृच्छ्रा + च्छ्वसिति", "च्छ्वसिति is not a word; the verb is श्वसिति (breathes)."),
             ("कृच्छ्राः + श्वसिति", "A visarga before श stays or becomes श्; it never gives च्छ."),
             ("कृच्छ्रम् + श्वसिति", "म् before श gives anusvāra (कृच्छ्रं श्वसिति), not च्छ.")],
            "कृच्छ्रात् (with difficulty) + श्वसिति (breathes): त् + श → च्छ.",
            "त् + श → च्छ (त् becomes च्, and the श usually becomes छ)."),
        multi("apply", 4, "Which of these are signs named in unit 82?",
              [("She feels no pain at all", "The unit says the opposite: शूलमधिकमुपजायते, pain arises in excess."),
               ("The fetus does not move", "Right: न च स्पन्दते गर्भः."),
               ("A heavy flow comes from the yoni", "The unit says the yoni does not flow: न स्रवति योनिः."),
               ("She weeps day and night", "Right: रोदित्यहर्निशम्."),
               ("She breathes with difficulty", "Right: कृच्छ्राच्छ्वसिति.")],
              [1, 3, 4],
              "A still fetus, weeping day and night and hard breathing are named; painlessness and a heavy flow are not.",
              "न स्पन्दते गर्भः, रोदित्यहर्निशम्, कृच्छ्राच्छ्वसिति."),
        mcq("transfer", 5, "By the rule of कृच्छ्रात् + श्वसिति, how is तत् + श्रुत्वा (having heard that) usually joined?",
            ("तच्छ्रुत्वा", "त् + श → च्छ, as कृच्छ्रात् + श्वसिति → कृच्छ्राच्छ्वसिति."),
            [("तद्श्रुत्वा", "त् becomes द् before a voiced sound; श is unvoiced."),
             ("तत्श्रुत्वा", "Before श the त् does not stay; it becomes च्."),
             ("तश्श्रुत्वा", "त् does not become श्; it becomes च्, and the श then usually छ.")],
            "तत् + श्रुत्वा = तच्छ्रुत्वा, like कृच्छ्रात् + श्वसिति = कृच्छ्राच्छ्वसिति.",
            "त् + श → च्छ.",
            teaches="A final त् before श becomes च्, and the श usually becomes छ: कृच्छ्रात् + श्वसिति → कृच्छ्राच्छ्वसिति."),
    ],
}

# ---------------------------------------------------------------- unit 83
AUTHORED["83"] = {
    "title": "तं तु गर्भं ... मूढगर्भमित्याहुः",
    "question": "By unit 83, what fetus do they call mūḍhagarbha?",
    "rule": ("The fetus that sometimes has entered the path of the offspring (अपत्यपथ, probably the birth passage) wrongly "
             "(असम्यक्) and in many ways (अनेकधा), afflicted and bewildered by deranged vāyu: they call it mūḍhagarbha (मूढगर्भ)."),
    "limits": ("'Birth passage' for अपत्यपथ is probable. Obstructed labour with a malpositioned fetus is a probable modern "
               "equivalent only. The many ways are not listed here. मूढ = bewildered, stuck. A prose line."),
    "explain_hi": ("यह गद्य-पंक्ति मूढगर्भ की परिभाषा देती है। "
                   "वह गर्भ, जो कभी-कभी (कदाचित्) गलत ढंग से (असम्यक्) और अनेक प्रकार से (अनेकधा) अपत्यपथ यानी सन्तान के "
                   "मार्ग में, सम्भवतः प्रसव-मार्ग में, पहुँचा हो (प्रतिपन्नम्), और बिगड़ी वायु से (विगुणेन वायुना) पीड़ित और मोहित हो, "
                   "उसे मूढगर्भ कहते हैं (इत्याहुः)। "
                   "मूढ = मोहित, अटका हुआ; यह तकनीकी नाम रखा गया है। "
                   "आधुनिक समतुल्य (सम्भावित): गर्भ की गलत स्थिति से अटका प्रसव।"),
    "hook": "गलत राह, बिगड़ी वायु, अटका गर्भ: मूढगर्भ।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 83, what afflicts and bewilders the fetus called mūḍhagarbha?",
            ("Deranged vāyu", "विगुणेन वायुना पीडितं मोहितं च: afflicted and bewildered by deranged wind."),
            [("Aggravated Pitta", "Pitta is not named in unit 83; the agent is वायुना, by wind."),
             ("Accumulated Kapha", "Kapha is not named in unit 83; the agent is वायुना, by wind."),
             ("Spoiled blood", "Blood is not named in unit 83; the agent is वायुना, by wind.")],
            "Deranged vāyu (wind) afflicts and bewilders it.",
            "विगुणेन वायुना पीडितं मोहितं च."),
        order(1, "Put these phrases of unit 83 in the line's order.",
              ["तं तु गर्भं", "कदाचिदसम्यगपत्यपथमनेकधा", "प्रतिपन्नं", "विगुणेन वायुना", "पीडितंमोहितं च",
               "मूढगर्भमित्याहुः"],
              "That fetus, however, sometimes wrongly into the path of the offspring in many ways having entered, by deranged "
              "wind afflicted and bewildered: they call it mūḍhagarbha.",
              "तं तु गर्भं → कदाचित्... → प्रतिपन्नं → विगुणेन वायुना → पीडितं मोहितं च → मूढगर्भमित्याहुः."),
        match(2, "Match each word of unit 83 to its meaning.",
              [["कदाचित्", "sometimes"], ["असम्यक्", "wrongly, not rightly"], ["अनेकधा", "in many ways"],
               ["विगुण", "faulty, deranged"], ["मोहित", "bewildered"]],
              "Sometimes, wrongly, in many ways; by deranged wind, afflicted and bewildered.",
              "कदाचित्, असम्यक्, अनेकधा, विगुण, मोहित.", role="extend",
              teaches="मूढ = bewildered, stuck: मूढगर्भ, the bewildered (stuck) fetus, is kept as a technical name."),
        mcq("discriminate", 3, "Which split of मूढगर्भमित्याहुः is right?",
            ("मूढगर्भम् + इति + आहुः", "म् joins the vowel; इ + आ → या: इति + आहुः → इत्याहुः."),
            [("मूढगर्भम् + इति + अहुः", "इ + अ would give इत्यहुः with a short अ; the verb is आहुः (they call)."),
             ("मूढगर्भः + इति + आहुः", "अः before इ loses the visarga (मूढगर्भ इति); no म् would appear."),
             ("मूढगर्भे + इति + आहुः", "ए before इ would give मूढगर्भ इति; no म् would appear.")],
            "मूढगर्भम् (accusative) + इति (thus) + आहुः (they call).",
            "म् + vowel joins; इ + आ → या."),
        mcq("apply", 4, "A healer must decide whether a fetus is mūḍhagarbha. Which finding fits unit 83?",
            ("It has entered the passage wrongly", "असम्यगपत्यपथम् ... प्रतिपन्नम्: it has entered the path wrongly."),
            [("It has entered the passage rightly", "The unit says the opposite: असम्यक्, wrongly."),
             ("It has never left its own place", "The unit says it has entered (प्रतिपन्नम्) the path of the offspring."),
             ("It moved in only one fixed way", "The unit says in many ways: अनेकधा.")],
            "The mūḍhagarbha has entered the path of the offspring wrongly and in many ways.",
            "असम्यक् ... अनेकधा प्रतिपन्नम्."),
        mcq("transfer", 5, "By the rule of असम्यक् + अपत्यपथम्, how is वाक् + ईशः (lord of speech) joined?",
            ("वागीशः", "A final क् before a vowel becomes ग्, as असम्यक् + अपत्य → असम्यगपत्य."),
            [("वाकीशः", "Before a vowel the final क् does not stay unvoiced; it becomes ग्."),
             ("वाङीशः", "क् may become ङ् before a nasal such as न or म, not before a vowel."),
             ("वाचीशः", "क् does not turn into च् here; before a vowel it becomes ग्.")],
            "वाक् + ईशः = वागीशः, like असम्यक् + अपत्यपथम् = असम्यगपत्यपथम्.",
            "क् + vowel → ग्.",
            teaches="A word-final क् becomes ग् before a vowel: असम्यक् + अपत्यपथम् → असम्यगपत्यपथम्."),
    ],
}

# ---------------------------------------------------------------- unit 84
AUTHORED["84"] = {
    "title": "विगुणानिलप्रतिपीडनैवैचित्र्यादसंसंख्यगातिं च",
    "question": "By unit 84, the variety of whose pressing is named as a cause?",
    "rule": ("Owing to (-आत्) the variety (वैचित्र्य) of the pressing (प्रतिपीडन) by deranged (विगुण) wind (अनिल), "
             "(the fetus is one) of countless courses, on a conjectural reading. It appears to continue unit 83."),
    "limits": ("पीडनैवैचित्र्याद् is damaged (an extra ऐ, or a dropped व: पीडनैव वैचित्र्यात्; same sense). "
               "असंसंख्यगातिं is read असङ्ख्यगतिम् ('of countless courses') only on a conjecture. No question rests on "
               "either. No verb; '(one)' is not stated. Prose."),
    "explain_hi": ("यह छोटी, क्षतिग्रस्त गद्य-पंक्ति सम्भवतः इकाई ८३ का वाक्य आगे बढ़ाती है। "
                   "बिगड़ी वायु (विगुण अनिल) के दबाव (प्रतिपीडन) की विविधता (वैचित्र्य) से, अनुमानित पाठ पर, (वह गर्भ) असंख्य "
                   "गतियों वाला होता है। "
                   "छपा शब्द बिगड़ा है: बीच में या तो एक मात्रा अधिक है या एक ‘व’ छूटा है (अर्थ दोनों में एक), और ‘असंसंख्यगातिं’ को अनुमान से ‘असङ्ख्यगतिम्’ पढ़ा गया; "
                   "इसलिए ‘असंख्य गतियों’ पर कोई प्रश्न नहीं। "
                   "‘वैचित्र्यात्’ की पंचमी विभक्ति कारण बताती है: विविधता के कारण।"),
    "hook": "बिगड़ी वायु का दबाव तरह-तरह का (आगे अनुमानित पाठ: असंख्य गतियाँ)।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 84, whose pressing is named as the cause?",
            ("Deranged wind", "विगुणानिलप्रतिपीडन: the pressing by deranged (विगुण) wind (अनिल)."),
            [("The mother's hands", "No hands are named in unit 84; the pressing is by अनिल, wind."),
             ("A heavy meal", "Food is not named in unit 84; the pressing is by अनिल, wind."),
             ("Spoiled blood", "Blood is not named in unit 84; the pressing is by अनिल, wind.")],
            "The pressing is by deranged wind (विगुण अनिल).",
            "विगुण + अनिल + प्रतिपीडन."),
        order(1, "Put these parts of unit 84's long compound in the printed order.",
              ["विगुण", "अनिल", "प्रतिपीडन", "वैचित्र्यात्"],
              "Deranged, wind, pressing, owing to the variety: owing to the variety of the pressing by deranged wind.",
              "विगुण → अनिल → प्रतिपीडन → वैचित्र्यात्."),
        match(2, "Match each part of unit 84's compound to its meaning.",
              [["विगुण", "faulty, deranged"], ["अनिल", "wind"], ["प्रतिपीडन", "pressing"], ["वैचित्र्य", "variety"]],
              "Owing to the variety of the pressing by deranged wind.",
              "विगुण, अनिल, प्रतिपीडन, वैचित्र्य.", role="extend",
              teaches="वैचित्र्य is the abstract noun of विचित्र (varied): 'variety, manifoldness'."),
        mcq("discriminate", 3, "Which split of विगुणानिल is right?",
            ("विगुण + अनिल", "अ + अ → आ: विगुण + अनिल → विगुणानिल."),
            [("विगुणा + निल", "निल is not a word; the word is अनिल (wind)."),
             ("विगुणः + अनिल", "No visarga stands inside a compound, and अः + अ would give ओऽ."),
             ("विगुणे + अनिल", "ए + अ would give विगुणेऽनिल, with ए kept.")],
            "विगुण (deranged) + अनिल (wind): अ + अ → आ.",
            "अ + अ → आ."),
        mcq("apply", 4, "What does the ending -आत् of वैचित्र्यात् express in unit 84?",
            ("Cause: owing to, from", "The data labels it ablative: 'variety, from', that is, owing to the variety."),
            [("Place: in, among them", "Place would be the locative, वैचित्र्ये."),
             ("Means: by, with the help of", "Means would be the instrumental, वैचित्र्येण."),
             ("Purpose: for the sake of", "Purpose would be the dative, वैचित्र्याय.")],
            "वैचित्र्यात् is ablative: owing to the variety.",
            "-आत् (ablative) = from, owing to."),
        mcq("transfer", 5, "By the rule of विगुण + अनिल, how is हिम + अचलः (snow mountain) joined?",
            ("हिमाचलः", "अ + अ → आ, as विगुण + अनिल → विगुणानिल."),
            [("हिमचलः", "The two अ merge into a long आ; neither is simply lost."),
             ("हिमेचलः", "ए comes from अ + इ, not from अ + अ."),
             ("हिमोचलः", "ओ comes from अ + उ, not from अ + अ.")],
            "हिम + अचलः = हिमाचलः, like विगुण + अनिल = विगुणानिल.",
            "अ + अ → आ.",
            teaches="A short अ followed by a short अ joins as a long आ: विगुण + अनिल → विगुणानिल."),
    ],
}

# ---------------------------------------------------------------- unit 85
AUTHORED["85"] = {
    "title": "समासतस्तु त्रिविधा गतिः",
    "question": "By unit 85, into how many kinds is the course (gati) grouped in brief, and which are they?",
    "rule": ("In brief (समासतः), however, the course (गति) is of three kinds (त्रिविधा): upward (ऊर्ध्वा), transverse "
             "(तिर्यक्) and face-down (न्युब्जा). The copula is understood."),
    "limits": ("'Upward' rests on a near-certain correction (printed गतिरूध्र्वा read गतिरूर्ध्वा): no question asks for it. "
               "The exact bodily position of न्युब्जा is not described. Whose course it is, the line does not say. "
               "Printed तिर्यङ्ङ्युब्जा = तिर्यङ् न्युब्जा. A prose line."),
    "explain_hi": ("यह गद्य-पंक्ति गति को संक्षेप में (समासतः) तीन प्रकार की (त्रिविधा) बताती है: ऊर्ध्वा यानी ऊपर की ओर, "
                   "तिर्यक् यानी तिरछी, और न्युब्जा यानी औंधी, झुकी हुई। "
                   "छपे ‘गतिरूध्र्वा’ में ध और र उलट गए हैं; लगभग निश्चित पाठ ‘गतिरूर्ध्वा’ है। "
                   "न्युब्जा में शरीर की ठीक स्थिति क्या है, यह यहाँ नहीं बताया। "
                   "क्रिया ‘है’ समझी जाती है, और किसकी गति है, पंक्ति स्वयं नहीं कहती।"),
    "hook": "संक्षेप में तीन गति: ऊपर, तिरछी, औंधी।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 85, of how many kinds is the course (gati), in brief?",
            ("Of three kinds", "त्रिविधा गतिः: the course is of three kinds."),
            [("Of two kinds", "The unit says त्रिविधा, of three kinds."),
             ("Of eight kinds", "Eight is the number of saṃsthānas (positions) in unit 86, not of courses."),
             ("Of five kinds", "The unit says त्रिविधा, of three kinds.")],
            "In brief the course is of three kinds.",
            "समासतस्तु त्रिविधा गतिः."),
        order(1, "Put these printed words of unit 85 in the line's order.",
              ["समासतस्तु", "त्रिविधा", "गतिरूध्र्वा", "तिर्यङ्ङ्युब्जा च"],
              "In brief, however, of three kinds is the course: upward, transverse and face-down.",
              "समासतस्तु → त्रिविधा → गतिरूध्र्वा → तिर्यङ्ङ्युब्जा च."),
        match(2, "Match each word of unit 85 to its meaning.",
              [["समासतः", "in brief"], ["त्रिविधा", "of three kinds"], ["गति", "course"],
               ["तिर्यक्", "transverse, sideways"], ["न्युब्जा", "face-down, bent over"]],
              "In brief, the course is of three kinds; two of them are transverse and face-down.",
              "समासतः, त्रिविधा, गति, तिर्यक्, न्युब्जा.", role="extend",
              teaches="समासतः = in brief: the -तः ending makes an adverb, 'by way of a summary'."),
        mcq("discriminate", 3, "Which split of समासतस्तु is right?",
            ("समासतः + तु", "A visarga before त becomes स्: समासतः + तु → समासतस्तु."),
            [("समासतम् + तु", "म् before त would give anusvāra: समासतं तु."),
             ("समासते + तु", "ए before त stays ए: समासते तु."),
             ("समासतः + अस्तु", "अः + अ would give ओऽ: समासतोऽस्तु.")],
            "समासतः (in brief) + तु (however): visarga + त → स्त.",
            "Visarga before त/थ → स्."),
        mcq("apply", 4, "A course runs across, sideways. By unit 85, which of the three names fits it?",
            ("Tiryak, transverse", "तिर्यक् = transverse, sideways."),
            [("Nyubjā, face-down", "न्युब्जा = face-down, bent over, not sideways."),
             ("Ūrdhvā, upward", "ऊर्ध्वा = upward, not sideways."),
             ("Saṃsthāna, position", "Saṃsthāna is the word of unit 86, not one of the three courses.")],
            "Sideways is tiryak, the transverse course.",
            "तिर्यक् = transverse."),
        mcq("transfer", 5, "By the pattern of त्रिविधा (of three kinds), what does द्विविधा mean?",
            ("Of two kinds", "-विधा = of ... kinds: द्वि (two) + विधा = of two kinds."),
            [("Of many kinds", "Of many kinds would be बहुविधा."),
             ("Of ten kinds", "Of ten kinds would be दशविधा."),
             ("Twice as large", "-विधा means 'of ... kinds', not size.")],
            "द्विविधा = of two kinds, as त्रिविधा = of three kinds.",
            "number + -विध = of so many kinds.",
            teaches="-विध after a number means 'of so many kinds': त्रिविधा गतिः = the course is of three kinds."),
    ],
}

# ---------------------------------------------------------------- unit 86
AUTHORED["86"] = {
    "title": "संस्थानानि पुनरष्टौ",
    "question": "By unit 86, how many saṃsthānas (positions) are there?",
    "rule": ("The positions (संस्थानानि), however (पुनः), are eight (अष्टौ); the copula is understood. पुनः has an "
             "original र्, so before a vowel it shows र्: पुनः + अष्टौ → पुनरष्टौ."),
    "limits": ("What is arranged is not stated in this line; unit 87 only says 'those will be told further on'. The eight "
               "are not listed here. अष्टौ is a nominative of 'eight', not a dual. A prose line."),
    "explain_hi": ("यह दो शब्दों की गद्य-पंक्ति कहती है: संस्थान फिर (पुनः) आठ (अष्टौ) हैं। "
                   "संस्थान = व्यवस्था, स्थिति; किसकी स्थिति, यह पंक्ति नहीं कहती, और आठों के नाम यहाँ नहीं दिए। "
                   "‘अष्टौ’ अष्टन् (आठ) का प्रथमा रूप है; इसका ‘-औ’ द्विवचन नहीं है। "
                   "‘पुनः’ का विसर्ग मूल र् से बना है, इसलिए स्वर से पहले र् लौट आता है: पुनरष्टौ। "
                   "क्रिया ‘हैं’ समझी जाती है।"),
    "hook": "गति तीन, पर संस्थान आठ।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 86, how many saṃsthānas (positions) are there?",
            ("Eight", "संस्थानानि पुनरष्टौ: the positions are eight."),
            [("Three", "Three is the number of courses (gati) in unit 85."),
             ("Seven", "The unit says अष्टौ, eight."),
             ("Ten", "The unit says अष्टौ, eight.")],
            "The positions are eight.",
            "संस्थानानि अष्टौ."),
        order(1, "Put the words of unit 86 in the line's order.",
              ["संस्थानानि", "पुनः", "अष्टौ"],
              "The positions, however, (are) eight.",
              "संस्थानानि → पुनः → अष्टौ."),
        match(2, "Match each word of unit 86 to its meaning.",
              [["संस्थान", "position, configuration"], ["पुनः", "again, however"], ["अष्टौ", "eight"]],
              "The positions, however, are eight.",
              "संस्थान, पुनः, अष्टौ.", role="extend",
              teaches="अष्टौ is the nominative of अष्टन् (eight): here -औ is not a dual ending."),
        mcq("discriminate", 3, "Which split of पुनरष्टौ is right?",
            ("पुनः + अष्टौ", "पुनः has an original र्; before a vowel the र् shows: पुनरष्टौ."),
            [("पुनर + अष्टौ", "A final अ + अ would give आ: पुनराष्टौ."),
             ("पुनः + रष्टौ", "रष्टौ is not a word; the word is अष्टौ (eight)."),
             ("पुने + अष्टौ", "ए + अ would give पुनेऽष्टौ, with ए kept.")],
            "पुनः (however) + अष्टौ (eight): the visarga of पुनः comes from र्, which returns before a vowel.",
            "पुनः + vowel → पुनर्."),
        mcq("apply", 4, "In unit 86, what does the ending -औ of अष्टौ show?",
            ("The nominative of 'eight'", "The data labels अष्टौ num. nom.: 'eight' as subject."),
            [("A dual form: 'the two eights'", "-औ is not a dual here; अष्टौ is the nominative of अष्टन्."),
             ("A locative: 'in the eight'", "A locative would end in -सु: अष्टसु (in eight)."),
             ("A verb: 'they become eight'", "अष्टौ is a numeral, not a verb; the copula is understood.")],
            "अष्टौ = eight, nominative; the -औ is not a dual.",
            "अष्टन् → nominative अष्टौ."),
        mcq("transfer", 5, "By the rule of पुनः + अष्टौ, how is पुनः + आगतः (come again) joined?",
            ("पुनरागतः", "पुनः has an original र्; before a vowel it shows र्, as in पुनरष्टौ."),
            [("पुन आगतः", "An ordinary -अः drops its visarga before आ, but पुनः keeps its र्."),
             ("पुनो आगतः", "ओ comes from अः before a voiced consonant, and not for पुनः."),
             ("पुनरगतः", "The long आ of आगतः is not shortened.")],
            "पुनः + आगतः = पुनरागतः, like पुनः + अष्टौ = पुनरष्टौ.",
            "पुनः + vowel → पुनर्.",
            teaches="पुनः ends in an original र्: before a vowel it shows र्: पुनः + अष्टौ → पुनरष्टौ."),
    ],
}

# ---------------------------------------------------------------- unit 87
AUTHORED["87"] = {
    "title": "तान्यत्रैवोत्तरत्र वक्ष्यंते",
    "question": "By unit 87, what does the text promise about 'those'?",
    "rule": ("Those (तानि, neuter plural) will be told (वक्ष्यन्ते, future of √वच् in passive sense) just here (अत्रैव), "
             "further on (उत्तरत्र). The unit does not name what 'those' are."),
    "limits": ("The referent of तानि is not named; unit 86 (the eight positions) comes just before, but no pairing is "
               "asserted, and no question asks what 'those' are. A prose line."),
    "explain_hi": ("यह छोटी गद्य-पंक्ति एक वचन देती है: वे (तानि) यहीं (अत्र एव) आगे (उत्तरत्र) कहे जाएँगे (वक्ष्यन्ते)। "
                   "‘तानि’ नपुंसक बहुवचन है; वे क्या हैं, पंक्ति नहीं बताती। "
                   "ठीक पहले इकाई ८६ में आठ संस्थान आए हैं, पर दोनों को जोड़ा नहीं गया। "
                   "‘वक्ष्यन्ते’ √वच् (कहना) का भविष्यत् रूप है, कर्मवाच्य अर्थ में: कहे जाएँगे।"),
    "hook": "अभी नहीं, यहीं आगे बताएँगे।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 87, when will 'those' be told?",
            ("Further on, here in this text", "अत्रैवोत्तरत्र: just here, further on."),
            [("Already, in an earlier chapter", "वक्ष्यन्ते is future: they will be told, not were told."),
             ("In another book, not this one", "अत्र एव: just here, in this work."),
             ("Never; they are left untold", "The unit promises they will be told: वक्ष्यन्ते.")],
            "They will be told just here, further on.",
            "तान्यत्रैवोत्तरत्र वक्ष्यन्ते."),
        order(1, "Put the words of unit 87 in the line's order.",
              ["तानि", "अत्र", "एव", "उत्तरत्र", "वक्ष्यन्ते"],
              "Those, here, just, further on, will be told.",
              "तानि → अत्र → एव → उत्तरत्र → वक्ष्यन्ते."),
        match(2, "Match each word of unit 87 to its meaning.",
              [["तानि", "those"], ["अत्र", "here"], ["एव", "just, only"], ["उत्तरत्र", "further on, later"],
               ["वक्ष्यन्ते", "will be told"]],
              "Those will be told just here, further on.",
              "तानि, अत्र, एव, उत्तरत्र, वक्ष्यन्ते.", role="extend",
              teaches="वक्ष्यन्ते is a future form of √वच् (speak) used in passive sense: 'will be told'."),
        mcq("discriminate", 3, "Which split of तान्यत्रैवोत्तरत्र is right?",
            ("तानि + अत्र + एव + उत्तरत्र", "इ + अ → य; अ + ए → ऐ; अ + उ → ओ."),
            [("तानि + अत्र + इव + उत्तरत्र", "अ + इ would give ए (अत्रेव), not ऐ."),
             ("ताने + अत्र + एव + उत्तरत्र", "ए + अ would give तानेऽत्र, with ए kept."),
             ("तानि + अत्र + एव + ओत्तरत्र", "अ + ओ would give औ (एवौत्तरत्र), not ओ.")],
            "तानि (those) + अत्र (here) + एव (just) + उत्तरत्र (further on).",
            "इ + अ → य; अ + ए → ऐ; अ + उ → ओ."),
        mcq("apply", 4, "What does the verb वक्ष्यन्ते of unit 87 express?",
            ("Will be told (future)", "The data labels it 3 pl. future, passive in sense."),
            [("Are told now (present)", "A present would be उच्यन्ते (are told)."),
             ("Were told (past)", "-स्य- marks the future, not a past form."),
             ("Should be told (optative)", "-स्य- marks the future; the unit states, it does not urge.")],
            "वक्ष्यन्ते = they will be told.",
            "-स्य- / -क्ष्य- = future."),
        mcq("transfer", 5, "By the rule of अत्र + एव → अत्रैव, how is तत्र + एव (only there) joined?",
            ("तत्रैव", "अ + ए → ऐ, as अत्र + एव → अत्रैव."),
            [("तत्रेव", "ए comes from अ + इ; here अ meets ए and gives ऐ."),
             ("तत्रौव", "औ comes from अ + ओ, not from अ + ए."),
             ("तत्रयेव", "No य् comes in after अ; अ + ए → ऐ.")],
            "तत्र + एव = तत्रैव, like अत्र + एव = अत्रैव.",
            "अ + ए → ऐ.",
            teaches="A short अ followed by ए joins as ऐ: अत्र + एव → अत्रैव."),
    ],
}

# ---------------------------------------------------------------- unit 88
AUTHORED["88"] = {
    "title": "तेषु सर्वेष्वपि ... वर्जयेत्",
    "question": "By unit 88, in all of those, which woman should one avoid?",
    "rule": ("In all of those too (तेषु सर्वेष्वपि), one should avoid (वर्जयेत्) the woman whose sense-objects are reversed, "
             "who is overtaken by convulsion (आक्षेप), slipping of the yoni, giddiness and other troubles, whose body is cold "
             "and who has foul belching."),
    "limits": ("Low confidence. संवरण and मक्कल are of unclear sense here (kept untranslated); श्वास may be plain breathing or "
               "breathing trouble; in what respect she is to be avoided is not stated; the woman (the mūḍhagarbha case) is "
               "understood from context. No question rests on these. A prose line."),
    "explain_hi": ("यह गद्य-पंक्ति बताती है कि उन सब में भी (तेषु सर्वेष्वपि) किस स्त्री को छोड़ दे (वर्जयेत्)। "
                   "जिसकी इन्द्रियों के विषय उलटे हो गए हों, जो आक्षेप यानी ऐंठन, योनि के खिसकने (योनिस्रंश), संवरण, मक्कल, "
                   "श्वास और भ्रम यानी चक्कर से ग्रस्त हो, जिसका शरीर ठण्डा हो (शीतगात्रा) और जिसकी डकारें दुर्गन्धित हों "
                   "(पूत्युद्गारा)। "
                   "संवरण और मक्कल के अर्थ यहाँ अस्पष्ट हैं, और ‘श्वास’ साँस की तकलीफ भी हो सकता है, केवल साँस भी। "
                   "किस बात में छोड़े, यह इकाई नहीं कहती; स्त्री मूढगर्भ के प्रसंग से समझी जाती है।"),
    "hook": "इन्द्रियाँ उलटी, शरीर ठण्डा, डकार दुर्गन्धित: वर्जयेत्।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 88, what should one do with the woman who shows these signs?",
            ("One should avoid her", "वर्जयेत् = one should avoid."),
            [("One should feed her", "Feeding is not named in unit 88; the verb is वर्जयेत्, avoid."),
             ("One should bathe her", "Bathing is not named in unit 88; the verb is वर्जयेत्, avoid."),
             ("One should anoint her", "Anointing is not named in unit 88; the verb is वर्जयेत्, avoid.")],
            "One should avoid (वर्जयेत्) such a woman.",
            "... शीतगात्रां पूत्युद्गारां च वर्जयेत्."),
        order(1, "Put these phrases of unit 88 in the line's order.",
              ["तेषु सर्वेष्वपि", "विपरीतेंद्रियार्थाम्", "आक्षेपयोनिस्रंश...भ्रमाभिपन्नां", "शीतगात्रां",
               "पूत्युद्गारां च", "वर्जयेत्"],
              "In all of those too: with sense-objects reversed, overtaken by convulsion, slipping of the yoni ... giddiness, "
              "with a cold body and foul belching, one should avoid.",
              "तेषु सर्वेष्वपि → विपरीतेन्द्रियार्थाम् → ...अभिपन्नाम् → शीतगात्राम् → पूत्युद्गाराम् → वर्जयेत्."),
        match(2, "Match each word of unit 88 to its meaning.",
              [["आक्षेप", "convulsion"], ["योनिस्रंश", "slipping of the yoni"], ["भ्रम", "giddiness"],
               ["शीतगात्र", "with a cold body"], ["पूत्युद्गार", "with foul belching"]],
              "Convulsion, slipping of the yoni, giddiness, a cold body, foul belching.",
              "आक्षेप, योनिस्रंश, भ्रम, शीतगात्र, पूत्युद्गार.", role="extend",
              teaches="शीतगात्रा is a bahuvrīhi: she whose limbs (गात्र) are cold (शीत)."),
        mcq("discriminate", 3, "Which split of पूत्युद्गाराम् is right?",
            ("पूति + उद्गाराम्", "इ before a different vowel becomes य्: पूति + उद्गाराम् → पूत्युद्गाराम्."),
            [("पूत् + युद्गाराम्", "युद्गार is not a word; the word is उद्गार (belching)."),
             ("पूते + उद्गाराम्", "ए + उ would give पूत उद्गाराम्, with a gap."),
             ("पूतु + उद्गाराम्", "उ + उ would give ऊ: पूतूद्गाराम्.")],
            "पूति (foul) + उद्गाराम् (belching): इ + उ → यु.",
            "इ + a different vowel → य् + that vowel."),
        multi("apply", 4, "Which of these signs are named in unit 88?",
              [("A cold body", "Right: शीतगात्राम्."),
               ("High fever", "Fever is not named in unit 88."),
               ("Foul belching", "Right: पूत्युद्गाराम्."),
               ("Clear, sharp senses", "The unit says the opposite: विपरीतेन्द्रियार्थाम्, sense-objects reversed."),
               ("Giddiness", "Right: भ्रम.")],
              [0, 2, 4],
              "A cold body, foul belching and giddiness are named; fever and sharp senses are not.",
              "शीतगात्रा, पूत्युद्गारा, भ्रम."),
        mcq("transfer", 5, "By the rule of सर्वेषु + अपि → सर्वेष्वपि, how is मधु + अत्र (honey here) joined?",
            ("मध्वत्र", "उ before a different vowel becomes व्, as सर्वेषु + अपि → सर्वेष्वपि."),
            [("मधूत्र", "ऊ comes from उ + उ, not from उ + अ."),
             ("मधवत्र", "अव् comes from ओ before a vowel, not from उ."),
             ("मधुत्र", "The अ of अत्र is not simply lost; उ becomes व्.")],
            "मधु + अत्र = मध्वत्र, like सर्वेषु + अपि = सर्वेष्वपि.",
            "उ + a different vowel → व् + that vowel.",
            teaches="A short उ before a different vowel becomes व्: सर्वेषु + अपि → सर्वेष्वपि."),
    ],
}

# ---------------------------------------------------------------- unit 89
AUTHORED["89"] = {
    "title": "न तु क्षणमप्युपेक्षेत गर्भशल्यं",
    "question": "By unit 89, why must the garbhaśalya not be neglected even for a moment?",
    "rule": ("One should not neglect (न उपेक्षेत) the garbhaśalya (गर्भशल्य, the fetus as a lodged dart) even for a moment "
             "(क्षणमपि), for (हि) it, having made (her) breathless (निरुच्छ्वासीकृत्य), would quickly kill the mother (जननीम्)."),
    "limits": ("'Her' of 'made her breathless' is not in the Sanskrit; the mother is the natural object. आशु (quickly) may "
               "go with the making breathless or with the killing: no question asks which. 'The fetus as a śalya' is the "
               "data's reading of the compound. Two printed lines, prose."),
    "explain_hi": ("यह गद्य-वाक्य चेतावनी देता है: गर्भशल्य की क्षण भर भी (क्षणमपि) उपेक्षा न करे (न उपेक्षेत)। "
                   "शल्य = काँटा, बाण, या शरीर में अटकी बाहरी वस्तु; गर्भशल्य = शल्य की तरह अटका गर्भ। "
                   "क्योंकि (हि) वह दम घोंटकर (निरुच्छ्वासीकृत्य) शीघ्र (आशु) माता (जननीम्) को मार देगा (हन्यात्)। "
                   "‘उसे’ संस्कृत में नहीं है; माता स्वाभाविक कर्म है। "
                   "‘आशु’ दम घोंटने से जुड़ता है या मारने से, दोनों सम्भव हैं।"),
    "hook": "अटका गर्भ काँटे जैसा: क्षण भर भी देर नहीं।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 89, whom would the neglected garbhaśalya kill?",
            ("The mother", "जननीं हन्यात्: it would kill the mother (जननी)."),
            [("Only the fetus", "The unit names the mother: जननीम्."),
             ("The attendant", "No attendant is named; the object is जननीम्, the mother."),
             ("No one at all", "The unit says it would kill the mother: हन्यात्.")],
            "It would quickly kill the mother.",
            "तद्धि ... आशु जननीं हन्यात्."),
        order(1, "Put these words of unit 89 in the printed order.",
              ["न तु क्षणमप्युपेक्षेत", "गर्भशल्यं", "तद्धि", "निरुच्छ्वासीकृत्य", "आशु", "जननीं हन्यात्"],
              "One should not neglect even for a moment the garbhaśalya; for it, having made (her) breathless, quickly "
              "would kill the mother.",
              "न उपेक्षेत → गर्भशल्यम् → तद्धि → निरुच्छ्वासीकृत्य → आशु → जननीं हन्यात्."),
        match(2, "Match each word of unit 89 to its meaning.",
              [["क्षणम्", "for a moment"], ["उपेक्षेत", "should neglect"], ["शल्य", "dart, thorn, lodged foreign body"],
               ["जननी", "mother"], ["हन्यात्", "would kill"]],
              "Not even for a moment should one neglect the garbhaśalya; it would kill the mother.",
              "क्षणम्, उपेक्षेत, शल्य, जननी, हन्यात्.", role="extend",
              teaches="गर्भशल्य: the fetus (garbha) acting as a śalya, a dart or foreign body lodged in the body."),
        mcq("discriminate", 3, "Which split of तद्धि is right?",
            ("तत् + हि", "त् becomes द् before ह, and the ह after it may become ध: तत् + हि → तद्धि."),
            [("तद् + धि", "धि is not a word here; the particle is हि (for)."),
             ("तम् + हि", "म् before ह would give anusvāra: तं हि."),
             ("तदा + हि", "आ before ह stays: तदा हि.")],
            "तत् (that) + हि (for): त् + ह → द्ध.",
            "त् + ह → द्ध (त् → द्, and ह usually → ध)."),
        mcq("apply", 4, "A fetus is stuck as a garbhaśalya. By unit 89, what is the healer told?",
            ("Not to neglect it even a moment", "न तु क्षणमप्युपेक्षेत: not even for a moment."),
            [("To wait some days and watch it", "The unit says not even for a moment."),
             ("To leave it, as it will come out", "The unit warns it would kill the mother."),
             ("To wait until the mother sleeps", "The unit allows no delay at all: क्षणमपि.")],
            "Not to neglect the garbhaśalya even for a moment, for it would kill the mother.",
            "न क्षणमपि उपेक्षेत."),
        mcq("transfer", 5, "By the form हन्यात् (would kill, from √हन्), what does कुर्यात् (from √कृ) mean?",
            ("One would do, one should do", "Like हन्यात्, कुर्यात् is an optative in -यात्."),
            [("One did it once, long ago", "A past form would be e.g. अकरोत्, not कुर्यात्."),
             ("One will do it later", "The future is करिष्यति, not कुर्यात्."),
             ("Having done it, then", "'Having done' is कृत्वा, not कुर्यात्.")],
            "कुर्यात् = one would / should do, like हन्यात् = would kill.",
            "Optative 3 sg. of some verbs ends in -यात्.",
            teaches="Some verbs form the optative in -यात्, not in -एत्: हन्यात् (would kill), कुर्यात् (would do)."),
    ],
}

# ---------------------------------------------------------------- unit 90
AUTHORED["90"] = {
    "title": "सचेतनश्च गर्भः शस्त्रेण विदार्यमाणो",
    "question": "By unit 90, what may a fetus with consciousness do while being split open with a śastra?",
    "rule": ("And a fetus with consciousness (सचेतन), while being split open (विदार्यमाण) with a śastra (cutting instrument), "
             "may throw its limbs (अङ्गानि) about unevenly (विषमम्)."),
    "limits": ("How consciousness is known is not stated. विषमम् is read as an adverb (unevenly); it could also go with "
               "the limbs (uneven limbs): no question rests on which. The unit states what may happen; it gives no "
               "instruction. A prose line."),
    "explain_hi": ("यह गद्य-पंक्ति बताती है कि क्या हो सकता है। "
                   "चेतना वाला (सचेतन) गर्भ, जब शस्त्र से चीरा जा रहा हो (विदार्यमाणः), अंगों (अङ्गानि) को विषम रूप से "
                   "इधर-उधर फेंक सकता है (विक्षिपेत्)। "
                   "चेतना कैसे जानी जाए, यह इकाई नहीं कहती। "
                   "‘विषमम्’ क्रियाविशेषण माना गया है; ‘विषम अंगों को’ भी पढ़ा जा सकता है। "
                   "‘विदार्यमाण’ वर्तमान कर्मवाच्य कृदन्त है: चीरा जाता हुआ।"),
    "hook": "जीवित गर्भ, चलता शस्त्र, फेंकते अंग।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 90, what may a living fetus do while it is being cut with a śastra?",
            ("Throw its limbs about", "विषममङ्गानि विक्षिपेत्: may throw its limbs about unevenly."),
            [("Lie perfectly still", "The unit says it may throw its limbs about."),
             ("Turn itself head first", "Turning is not named in unit 90."),
             ("Slip back up into the womb", "Slipping back is not named in unit 90.")],
            "It may throw its limbs about unevenly.",
            "विषममङ्गानि विक्षिपेत्."),
        order(1, "Put the words of unit 90 in the line's order.",
              ["सचेतनश्च", "गर्भः", "शस्त्रेण", "विदार्यमाणो", "विषममंगानि", "विक्षिपेत्"],
              "And with consciousness, the fetus, with the śastra, being split open, unevenly the limbs, may throw about.",
              "सचेतनश्च → गर्भः → शस्त्रेण → विदार्यमाणो → विषममंगानि → विक्षिपेत्."),
        match(2, "Match each word of unit 90 to its meaning.",
              [["सचेतन", "with consciousness, alive"], ["शस्त्र", "cutting instrument, knife"],
               ["विदार्यमाण", "being split open"], ["अङ्ग", "limb"], ["विक्षिपेत्", "may throw about"]],
              "A living fetus, being split open with a knife, may throw its limbs about.",
              "सचेतन, शस्त्र, विदार्यमाण, अङ्ग, विक्षिपेत्.", role="extend",
              teaches="सचेतन is a bahuvrīhi: स- (with) + चेतन (consciousness): having consciousness, alive."),
        mcq("discriminate", 3, "Which split of विदार्यमाणो विषमम् is right?",
            ("विदार्यमाणः + विषमम्", "अः before a voiced consonant (here व) becomes ओ."),
            [("विदार्यमाणे + विषमम्", "ए before व stays ए: विदार्यमाणे विषमम्."),
             ("विदार्यमाणम् + विषमम्", "म् before व would give anusvāra: विदार्यमाणं विषमम्."),
             ("विदार्यमाणा + विषमम्", "आ before व stays आ: विदार्यमाणा विषमम्.")],
            "विदार्यमाणः (being split) + विषमम् (unevenly): अः + voiced consonant → ओ.",
            "अः + voiced consonant → ओ."),
        mcq("apply", 4, "Why does विदार्यमाण mean 'while being split open'?",
            ("-यमाण marks a present passive participle", "Present passive participle of वि-√दॄ: being split."),
            [("-यमाण marks a past passive participle", "A past participle would be e.g. विदारित or विदीर्ण."),
             ("-यमाण marks a future active participle", "A future participle would carry -स्य- (e.g. -ष्यत्)."),
             ("-यमाण marks an optative verb of wishing", "It is a participle, not a finite verb; the optative here is विक्षिपेत्.")],
            "-यमाण: present passive participle, 'being ...-ed'.",
            "-यमान/-यमाण = present passive participle."),
        mcq("transfer", 5, "By the rule of सचेतनः + च → सचेतनश्च, how is बालः + च (and the boy) joined?",
            ("बालश्च", "A visarga before च becomes श्, as सचेतनः + च → सचेतनश्च."),
            [("बालो च", "ओ comes from अः before a voiced sound; च is unvoiced."),
             ("बालस्च", "स् comes before त or थ, not before च."),
             ("बालष्च", "ष् comes before ट or ठ, not before च.")],
            "बालः + च = बालश्च, like सचेतनः + च = सचेतनश्च.",
            "Visarga before च/छ → श्.",
            teaches="A visarga before च or छ becomes श्: सचेतनः + च → सचेतनश्च."),
    ],
}

# ---------------------------------------------------------------- unit 91
AUTHORED["91"] = {
    "title": "तस्मात्तत्संगे ... मंत्रौषधानि प्रयुंजीत",
    "question": "By unit 91, what is to be done 'in the obstruction of that' (तत्सङ्गे)?",
    "rule": ("Therefore (तस्मात्), in its obstruction (तत्सङ्गे), they should strive (प्रयतेरन्), and one should apply "
             "(प्रयुञ्जीत) the earlier-stated (पूर्वोक्त) mantras and medicines (मन्त्रौषध)."),
    "limits": ("Low confidence. Printed सूत्यः is unclear; 'for delivery' (सूत्यै) is a conjecture: no question rests on it. "
               "Who 'they' are and what 'that' (तत्) refers to are not stated; the earlier passage of the mantras is not "
               "named. A prose line."),
    "explain_hi": ("यह गद्य-पंक्ति कहती है कि इसलिए (तस्मात्) उसके अटकने पर (तत्सङ्गे) वे प्रयत्न करें (प्रयतेरन्), और पहले कहे "
                   "हुए (पूर्वोक्तानि) मन्त्र और औषध प्रयोग में लाए (प्रयुञ्जीत)। "
                   "छपा ‘सूत्यः’ व्याकरण में नहीं बैठता; ‘प्रसव के लिए’ (सूत्यै) केवल अनुमान है, इस पर कोई प्रश्न नहीं। "
                   "‘वे’ कौन हैं और ‘तत्’ किसे कहता है, नहीं बताया। "
                   "क्रिया बहुवचन ‘प्रयतेरन्’ से एकवचन ‘प्रयुञ्जीत’ में बदलती है।"),
    "hook": "अटके तो जुटो: पहले कहे मन्त्र और औषध लगाओ।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 91, what should one apply in the obstruction?",
            ("The earlier-stated mantras and medicines", "पूर्वोक्तानि च मन्त्रौषधानि प्रयुञ्जीत."),
            [("Cold water poured over the whole belly", "Water is not named in unit 91."),
             ("A new oil that is described only in this line", "The unit names things stated earlier, not a new oil."),
             ("Rest alone, with no medicine or mantra", "The unit names mantras and medicines.")],
            "One should apply the mantras and medicines stated earlier.",
            "पूर्वोक्तानि मन्त्रौषधानि प्रयुञ्जीत."),
        order(1, "Put these words of unit 91 in the line's order.",
              ["तस्मात्", "तत्संगे", "प्रयतेरन्", "पूर्वोक्तानि च", "मंत्रौषधानि", "प्रयुंजीत"],
              "Therefore, in its obstruction, ... they should strive, and the earlier-stated mantras and medicines one "
              "should apply.",
              "तस्मात् → तत्सङ्गे → प्रयतेरन् → पूर्वोक्तानि च → मन्त्रौषधानि → प्रयुञ्जीत."),
        match(2, "Match each word of unit 91 to its meaning.",
              [["तस्मात्", "therefore"], ["सङ्ग", "obstruction, sticking"], ["प्रयतेरन्", "they should strive"],
               ["पूर्वोक्त", "stated earlier"], ["प्रयुञ्जीत", "one should apply"]],
              "Therefore, in the obstruction, they should strive and apply the earlier-stated mantras and medicines.",
              "तस्मात्, सङ्ग, प्रयतेरन्, पूर्वोक्त, प्रयुञ्जीत.", role="extend",
              teaches="पूर्वोक्त = पूर्व (earlier) + उक्त (stated): 'stated earlier'."),
        mcq("discriminate", 3, "Which split of मन्त्रौषधानि is right?",
            ("मन्त्र + औषधानि", "अ + औ → औ: मन्त्र + औषधानि → मन्त्रौषधानि."),
            [("मन्त्रः + औषधानि", "No visarga stands inside a compound; अः before औ would leave a gap."),
             ("मन्त्रो + षधानि", "षधानि is not a word; the word is औषधानि (medicines)."),
             ("मन्त्रे + औषधानि", "ए before औ would give मन्त्र औषधानि, with a gap.")],
            "मन्त्र (mantra) + औषधानि (medicines): अ + औ → औ.",
            "अ + औ → औ."),
        mcq("apply", 4, "In unit 91 the verb shifts from प्रयतेरन् to प्रयुञ्जीत. What changes?",
            ("Plural 'they' to singular 'one'", "प्रयतेरन् is 3 pl.; प्रयुञ्जीत is 3 sg.; both are optatives."),
            [("Singular 'one' to plural 'they'", "It is the other way: प्रयतेरन् is plural, प्रयुञ्जीत singular."),
             ("Present tense to future tense", "Both are optatives ('should'), neither present nor future."),
             ("Optative mood to the past tense", "Both are optatives; neither is past.")],
            "The shift is from plural (they should strive) to singular (one should apply).",
            "प्रयतेरन् (3 pl. opt.) → प्रयुञ्जीत (3 sg. opt.)."),
        mcq("transfer", 5, "By the rule of पूर्व + उक्तानि → पूर्वोक्तानि, how is हित + उपदेशः (good advice) joined?",
            ("हितोपदेशः", "अ + उ → ओ, as पूर्व + उक्तानि → पूर्वोक्तानि."),
            [("हितौपदेशः", "औ comes from अ + ओ or अ + औ, not from अ + उ."),
             ("हितेपदेशः", "ए comes from अ + इ, not from अ + उ."),
             ("हितुपदेशः", "The अ does not simply vanish before उ.")],
            "हित + उपदेशः = हितोपदेशः, like पूर्व + उक्तानि = पूर्वोक्तानि.",
            "अ + उ → ओ.",
            teaches="A short अ followed by उ joins as ओ: पूर्व + उक्तानि → पूर्वोक्तानि."),
    ],
}

# ---------------------------------------------------------------- unit 92
AUTHORED["92"] = {
    "title": "त्रिविधस्तु संगो भवति",
    "question": "By unit 92, of how many kinds is saṅga (obstruction)?",
    "rule": ("The obstruction (सङ्ग, the sticking of the fetus) is of three kinds (त्रिविधः). त्रिविधः is masculine to "
             "agree with सङ्गः, as त्रिविधा in unit 85 agrees with feminine गतिः."),
    "limits": ("The kinds are not named in this line; unit 93 gives three places, but does not say they are 'the three "
               "kinds'. Whose sticking is understood from unit 91. A prose line."),
    "explain_hi": ("यह छोटी गद्य-पंक्ति कहती है: सङ्ग यानी गर्भ का अटकना तीन प्रकार का (त्रिविधः) होता है (भवति)। "
                   "प्रकार यहाँ गिनाए नहीं गए; इकाई ९३ तीन स्थान देती है, पर उन्हें ‘तीन प्रकार’ नहीं कहती। "
                   "‘त्रिविधः’ पुंलिंग है क्योंकि ‘सङ्गः’ पुंलिंग है; इकाई ८५ में ‘त्रिविधा’ स्त्रीलिंग ‘गतिः’ के साथ था। "
                   "सन्धि: त्रिविधः + तु → त्रिविधस्तु, सङ्गः + भवति → सङ्गो भवति।"),
    "hook": "सङ्ग भी तीन तरह का।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 92, of how many kinds is saṅga (obstruction)?",
            ("Of three kinds", "त्रिविधस्तु सङ्गो भवति: saṅga is of three kinds."),
            [("Of eight kinds", "Eight is the number of saṃsthānas (positions) in unit 86."),
             ("Of two kinds", "The unit says त्रिविधः, of three kinds."),
             ("Of four kinds", "The unit says त्रिविधः, of three kinds.")],
            "Saṅga is of three kinds.",
            "त्रिविधः सङ्गः."),
        order(1, "Put the words of unit 92 in the line's order.",
              ["त्रिविधः", "तु", "सङ्गः", "भवति"],
              "Of three kinds, however, the obstruction is.",
              "त्रिविधः → तु → सङ्गः → भवति."),
        match(2, "Match each word of unit 92 to its meaning.",
              [["त्रिविध", "of three kinds"], ["तु", "however"], ["सङ्ग", "obstruction, sticking"], ["भवति", "is"]],
              "The obstruction, however, is of three kinds.",
              "त्रिविध, तु, सङ्ग, भवति.", role="extend",
              teaches="सङ्ग here is the sticking (obstruction) of the fetus, taken up from unit 91."),
        mcq("discriminate", 3, "In unit 85 the course (गतिः, feminine) is त्रिविधा. Why is it त्रिविधः in unit 92?",
            ("It agrees with masculine सङ्गः", "An adjective takes the gender of its noun: त्रिविधः सङ्गः."),
            [("It is plural, and त्रिविधा singular", "Both are singular; they differ in gender."),
             ("त्रिविधा was a printing error", "त्रिविधा is right with feminine गतिः."),
             ("It means 'of three courses' here", "त्रिविध means 'of three kinds' in both lines.")],
            "त्रिविधः agrees with masculine सङ्गः; त्रिविधा agreed with feminine गतिः.",
            "An adjective agrees with its noun in gender."),
        mcq("apply", 4, "Which split of सङ्गो भवति is right?",
            ("सङ्गः + भवति", "अः before a voiced consonant (here भ) becomes ओ."),
            [("सङ्गे + भवति", "ए before भ stays ए: सङ्गे भवति."),
             ("सङ्गम् + भवति", "म् before भ would give anusvāra: सङ्गं भवति."),
             ("सङ्गा + भवति", "आ before भ stays आ: सङ्गा भवति.")],
            "सङ्गः (obstruction) + भवति (is): अः + voiced consonant → ओ.",
            "अः + voiced consonant → ओ."),
        mcq("transfer", 5, "By the agreement in त्रिविधः सङ्गः, which form of त्रिविध goes with neuter कर्म (procedure)?",
            ("त्रिविधं कर्म", "Neuter कर्म takes a neuter adjective: त्रिविधम्, written ं before क."),
            [("त्रिविधः कर्म", "-अः is masculine; कर्म is neuter."),
             ("त्रिविधा कर्म", "-आ is feminine; कर्म is neuter."),
             ("त्रिविधौ कर्म", "-औ is a dual; कर्म here is singular.")],
            "त्रिविधं कर्म, as त्रिविधः सङ्गः and त्रिविधा गतिः.",
            "The adjective takes its noun's gender: -अः m., -आ f., -अम् n.",
            teaches="त्रिविध takes the gender of its noun: त्रिविधः सङ्गः (m.), त्रिविधा गतिः (f.), त्रिविधं कर्म (n.)."),
    ],
}

# ---------------------------------------------------------------- unit 93
AUTHORED["93"] = {
    "title": "शिरस्यंसे जघने वा",
    "question": "By unit 93, which three places are named?",
    "rule": ("In the head (शिरसि), in the shoulder (अंसे), or in the jaghana (जघने, hip region): three locatives joined "
             "by वा (or). No verb."),
    "limits": ("No verb; it appears to continue unit 92, but the line does not say these are the three kinds of saṅga. "
               "Head, shoulder and breech obstruction is a probable obstetric reading only. The exact part meant by "
               "jaghana is not defined. A prose line."),
    "explain_hi": ("यह तीन शब्दों की गद्य-पंक्ति तीन स्थान बताती है: सिर में (शिरसि), कन्धे में (अंसे), या जघन यानी कूल्हे के "
                   "भाग में (जघने)। "
                   "क्रिया नहीं है; सम्भवतः यह इकाई ९२ के तीन प्रकार के सङ्ग को आगे बढ़ाती है, पर पंक्ति यह स्वयं नहीं कहती। "
                   "प्रसूति की सम्भावित व्याख्या (पाठ नहीं कहता): सिर, कन्धे और नितम्ब से अटकना। "
                   "तीनों शब्द सप्तमी (अधिकरण) एकवचन हैं।"),
    "hook": "सिर, कन्धा या कूल्हा: तीन जगह।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 93, which places are named?",
            ("Head, shoulder or hip region", "शिरस्यंसे जघने वा: in the head, the shoulder or the hip region."),
            [("Neck, chest or the knees", "None of these is named in unit 93."),
             ("Eyes, ears or the two nostrils", "None of these is named in unit 93."),
             ("Belly, back or the flanks", "None of these is named in unit 93.")],
            "The head, the shoulder or the jaghana (hip region).",
            "शिरसि, अंसे, जघने वा."),
        order(1, "Put the words of unit 93 in the line's order.",
              ["शिरसि", "अंसे", "जघने", "वा"],
              "In the head, in the shoulder, in the hip region, or.",
              "शिरसि → अंसे → जघने → वा."),
        match(2, "Match each word of unit 93 to its meaning.",
              [["शिरस्", "head"], ["अंस", "shoulder"], ["जघन", "hip region"], ["वा", "or"]],
              "Head, shoulder, hip region; वा = or.",
              "शिरस्, अंस, जघन, वा.", role="extend",
              teaches="Here -इ and -ए mark the locative singular: शिरसि = in the head, अंसे, जघने = in the shoulder, hip region."),
        mcq("discriminate", 3, "Which split of शिरस्यंसे is right?",
            ("शिरसि + अंसे", "इ before a different vowel becomes य्: शिरसि + अंसे → शिरस्यंसे."),
            [("शिरः + यंसे", "यंसे is not a word; the word is अंसे (in the shoulder)."),
             ("शिरसे + अंसे", "ए + अ would give शिरसेऽंसे, with ए kept."),
             ("शिरसा + अंसे", "आ + अ would give आ: शिरसांसे.")],
            "शिरसि (in the head) + अंसे (in the shoulder): इ + अ → य.",
            "इ + a different vowel → य् + that vowel."),
        mcq("apply", 4, "What case are शिरसि, अंसे and जघने in, by the data?",
            ("Locative (in)", "The data labels all three locative singular: in the head, shoulder, hip region."),
            [("Instrumental (with)", "The instrumental would be शिरसा, अंसेन, जघनेन."),
             ("Genitive (of)", "The genitive would be शिरसः, अंसस्य, जघनस्य."),
             ("Ablative (from)", "The ablative would be शिरसः, अंसात्, जघनात्.")],
            "All three are locatives: in the head, in the shoulder, in the hip region.",
            "-इ (शिरसि), -ए (अंसे, जघने) = locative singular."),
        mcq("transfer", 5, "By the rule of शिरसि + अंसे → शिरस्यंसे, how is दधि + अत्र (curd here) joined?",
            ("दध्यत्र", "इ before a different vowel becomes य्, as शिरसि + अंसे → शिरस्यंसे."),
            [("दधेत्र", "ए comes from अ + इ, not from इ + अ."),
             ("दधीत्र", "ई comes from इ + इ, not from इ + अ."),
             ("दधात्र", "The इ does not vanish; it becomes य्.")],
            "दधि + अत्र = दध्यत्र, like शिरसि + अंसे = शिरस्यंसे.",
            "इ + a different vowel → य् + that vowel.",
            teaches="A short इ before a different vowel becomes य्: शिरसि + अंसे → शिरस्यंसे."),
    ],
}

# ---------------------------------------------------------------- unit 94
AUTHORED["94"] = {
    "title": "मूढगर्भस्य तु जरायुपातनसामान्यं कर्मेत्येके",
    "question": "By unit 94, what two opinions are given about the procedure for a mūḍhagarbha?",
    "rule": ("Some (एके) say: for a mūḍhagarbha the procedure (कर्म) is the same as causing the jarāyu (afterbirth) to fall. "
             "Some say: the procedure beginning with mantras (मन्त्रादि) is prescribed in the Atharvaveda."),
    "limits": ("These are opinions of 'some' (इत्येके); the text does not say which is held. सामान्य plainly means 'common "
               "to'. Printed कर्मार्थर्व has an extra र् (near-certain: कर्माथर्व); no question rests on the printed form. "
               "The steps after the mantras are not listed. Two printed lines, prose."),
    "explain_hi": ("ये दो गद्य-पंक्तियाँ मूढगर्भ के कर्म (उपचार) पर दो मत देती हैं। "
                   "कुछ लोग (एके) कहते हैं: मूढगर्भ का कर्म जरायु यानी जेर को गिराने (पातन) के समान है। "
                   "कुछ कहते हैं: मन्त्र आदि वाला कर्म अथर्ववेद में विहित (बताया गया) है। "
                   "‘इति एके’ मत बताता है, ग्रन्थ का अपना निर्णय नहीं; कौन-सा मत माना गया, यह नहीं कहा। "
                   "‘सामान्य’ का सीधा अर्थ ‘साझा’ है, और मन्त्र के बाद के कर्म यहाँ गिनाए नहीं गए।"),
    "hook": "मूढगर्भ पर मतभेद: कोई कहे जेर जैसा, कोई कहे अथर्ववेद के मन्त्र।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 94, who holds the views given here?",
            ("Some unnamed authorities", "इत्येके: thus some (say)."),
            [("All the teachers, in agreement", "एके means some, not all; the views differ."),
             ("The author, as his own rule", "The text does not say which view it holds."),
             ("The mother and her attendants", "एके refers to some authorities, not to the mother.")],
            "Each view is marked इत्येके: thus some (say).",
            "इति एके = thus some (say)."),
        order(1, "Put these printed phrases of unit 94 in order.",
              ["मूढगर्भस्य तु", "जरायुपातनसामान्यं", "कर्मेत्येके", "मंत्रादिकर्मार्थर्ववेदविहितम्", "इत्येके"],
              "For a mūḍhagarbha, however, the same as causing the afterbirth to fall is the procedure, some say; the "
              "procedure beginning with mantras is prescribed in the Atharvaveda, some say.",
              "मूढगर्भस्य तु → जरायुपातनसामान्यं → कर्मेत्येके → मंत्रादि...विहितम् → इत्येके."),
        match(2, "Match each word of unit 94 to its meaning.",
              [["जरायु", "afterbirth"], ["पातन", "causing to fall"], ["सामान्य", "common to, the same as"],
               ["एके", "some (people)"], ["विहित", "prescribed"]],
              "Some liken it to causing the afterbirth to fall; some point to the Atharvaveda.",
              "जरायु, पातन, सामान्य, एके, विहित.", role="extend",
              teaches="इति एके = 'thus some (say)': it marks an opinion, not the text's own ruling."),
        mcq("discriminate", 3, "Which split of कर्मेत्येके is right?",
            ("कर्म + इति + एके", "अ + इ → ए; इ + ए → ये."),
            [("कर्मे + इति + एके", "ए + इ would give कर्म इति, with a gap."),
             ("कर्म + इत्य + एके", "इत्य is not a word; the particle is इति."),
             ("कर्म + एति + एके", "अ + ए would give ऐ: कर्मैत्येके.")],
            "कर्म (procedure) + इति (thus) + एके (some): अ + इ → ए; इ + ए → ये.",
            "अ + इ → ए; इ + ए → ये."),
        multi("apply", 4, "Which statements about unit 94 are right by the card?",
              [("The text says which opinion is right", "It does not; both are views of 'some' (एके)."),
               ("One view likens it to causing the afterbirth to fall", "Right: जरायुपातनसामान्यं कर्म."),
               ("One view links the mantra procedure to the Atharvaveda", "Right: मन्त्रादिकर्म अथर्ववेदविहितम्."),
               ("The unit lists every step after the mantras", "आदि (beginning with) is all it says; no steps are listed.")],
              [1, 2],
              "Two views of 'some': like the falling of the afterbirth; mantras as in the Atharvaveda. Neither is ruled on.",
              "... इत्येके ... इत्येके."),
        mcq("transfer", 5, "By the rule of इति + एके → इत्येके, how is प्रति + एकम् (each one) joined?",
            ("प्रत्येकम्", "इ before a different vowel becomes य्, as इति + एके → इत्येके."),
            [("प्रतीकम्", "ई comes from इ + इ, not from इ + ए."),
             ("प्रत्यैकम्", "ऐ comes from अ + ए; here इ meets ए."),
             ("प्रतयेकम्", "अय् comes from ए before a vowel, not from इ.")],
            "प्रति + एकम् = प्रत्येकम्, like इति + एके = इत्येके.",
            "इ + ए → ये.",
            teaches="A short इ before ए becomes य्: इति + एके → इत्येके."),
    ],
}


# ===================================================================== NOTES_HI
NOTES_HI = {
    "82": ("गद्य-पंक्ति; विश्वास निम्न। पाठ-चिह्न: (१) ‘संस्येते’ ज्ञात क्रिया-रूप नहीं; द्विवचन कर्ता ‘अक्षिणी’ (दोनों आँखें) "
           "के लिए द्विवचन क्रिया चाहिए; ‘संसीदेते’ (धँसती हैं) या ‘स्रंसेते’ (लटकती हैं) सम्भावित, ‘संशीयेते’, ‘संस्यन्देते’ भी "
           "अनुमान मात्र; शब्द संदिग्ध, इस पर प्रश्न नहीं। (२) छपा ‘स्वप्निति’ सम्भवतः ‘स्वपिति’ (न अधिक छपा)। ‘अन्यानि’ की "
           "संज्ञा नहीं दी। ‘योनिः’ को ‘न स्रवति’ का कर्ता माना गया। ‘क्षयति’ = क्षीण होती है, सम्भावित; ‘ताम्यति’ का सूक्ष्म अर्थ "
           "पक्का नहीं। छपा अन्तिम ‘विद्यान्’ को डेटा ‘विद्यात्’ पढ़ता है (कोई पाठ-चिह्न नहीं)। आधुनिक समतुल्य (सम्भावित): "
           "गर्भ में भ्रूण की मृत्यु। सन्धि जाँची: गर्भः + अन्यानि → गर्भोऽन्यानि (अः + अ → ओऽ); योनिः + अक्षिणी → "
           "योनिरक्षिणी (इः + स्वर → इर्); च + अस्याः → चास्याः (अ + अ → आ); व्यथते + अन्यथा → व्यथतेऽन्यथा (ए + अ → एऽ); "
           "रोदिति + अहर्निशम् → रोदित्यहर्निशम् (इ + अ → य); प्रति + उच्छ्वासात् → प्रत्युच्छ्वासात् (इ + उ → यु); "
           "कृच्छ्रात् + श्वसिति → कृच्छ्राच्छ्वसिति (त् + श → च्छ); क्षयति + इति → क्षयतीति (इ + इ → ई); इति + एवम् → "
           "इत्येवम् (इ + ए → ये)।"),
    "83": ("गद्य-पंक्ति; विश्वास मध्यम; कोई पाठ-चिह्न नहीं। छपा ‘गर्भंकदाचिदसम्यगपत्यपथमनेकधा’ = गर्भम् कदाचित् असम्यक् "
           "अपत्य-पथम् अनेकधा; ‘पीडितंमोहितं’ में दो शब्द जुड़े छपे (अन्तर की भूल)। ‘अपत्यपथ’ = सन्तान का मार्ग, सम्भवतः "
           "प्रसव-मार्ग (सम्भावित)। मूढ = मोहित, अटका; मूढगर्भ तकनीकी नाम रखा गया। आधुनिक समतुल्य (सम्भावित): गर्भ की गलत "
           "स्थिति से अटका प्रसव। सन्धि जाँची: कदाचित् + असम्यक् → कदाचिदसम्यक् (त् + स्वर → द्); असम्यक् + अपत्य → "
           "असम्यगपत्य (क् + स्वर → ग्); अपत्यपथम् + अनेकधा → अपत्यपथमनेकधा; मूढगर्भम् + इति → मूढगर्भमिति; इति + आहुः → "
           "इत्याहुः (इ + आ → या)।"),
    "84": ("गद्य-पंक्ति; विश्वास मध्यम। पाठ-चिह्न (सम्भावित): छपे ‘...प्रतिपीडनैवैचित्र्याद...’ में एक ‘ऐ/इ’ अधिक, और "
           "‘असंसंख्यगातिं’ में ‘सं’ दोहरा और ‘गा’ दीर्घ; अनुमानित पाठ ‘प्रतिपीडनवैचित्र्याद् असङ्ख्यगतिम्’। दूसरा उतना ही सम्भव "
           "सुधार: ‘प्रतिपीडनैव वैचित्र्यात्’ (एक ‘व’ छूटा); ‘दबाव की विविधता से’ अर्थ दोनों में एक। ‘असंख्य गतियाँ’ अनुमानित "
           "पाठ पर; इस पर प्रश्न नहीं। क्रिया ‘कहते हैं’ इकाई ८३ से समझी जाती है, जोड़ी नहीं गई; संज्ञा ‘(वह)’ नहीं दी। "
           "सम्भवतः इकाई ८३ का वाक्य आगे बढ़ाती है; ‘असंख्य गतियाँ’ इकाई ८५ (गति तीन प्रकार की) से मेल खाता है। "
           "सन्धि जाँची: विगुण + अनिल → विगुणानिल (अ + अ → आ); वैचित्र्यात् + अ... → वैचित्र्याद... (त् + स्वर → द्)।"),
    "85": ("गद्य-पंक्ति; विश्वास मध्यम। पाठ-चिह्न (लगभग निश्चित): छपे ‘गतिरूध्र्वा’ में ध और र उलटे; पाठ ‘गतिरूर्ध्वा’ "
           "(ऊर्ध्वा = ऊपर की ओर); इस शब्द को उत्तर बनाकर कोई प्रश्न नहीं। छपा ‘तिर्यङ्ङ्युब्जा’ = तिर्यङ् न्युब्जा (ङ दोहरा "
           "छपा)। ‘न्युब्जा’ = औंधी, झुकी; शरीर की ठीक स्थिति यहाँ नहीं बताई। क्रिया ‘है’ समझी जाती है। सन्धि जाँची: "
           "समासतः + तु → समासतस्तु (विसर्ग + त → स्); गतिः + ऊर्ध्वा → गतिरूर्ध्वा (इः + स्वर → इर्); तिर्यक् + न्युब्जा → "
           "तिर्यङ् न्युब्जा (क् अनुनासिक से पहले विकल्प से ङ्; तिर्यग् न्युब्जा भी शुद्ध)।"),
    "86": ("गद्य-पंक्ति; विश्वास मध्यम; कोई पाठ-चिह्न नहीं। क्रिया ‘हैं’ समझी जाती है। संस्थान = व्यवस्था, स्थिति; किसकी, "
           "यहाँ नहीं कहा; इकाई ८७ केवल कहती है कि ‘वे’ आगे कहे जाएँगे। ‘अष्टौ’ = अष्टन् (आठ) का प्रथमा रूप; ‘-औ’ यहाँ "
           "द्विवचन नहीं। सन्धि जाँची: पुनः + अष्टौ → पुनरष्टौ (पुनः का विसर्ग मूल र् से है, इसलिए स्वर से पहले र् लौटता है)।"),
    "87": ("गद्य-पंक्ति; विश्वास उच्च; कोई पाठ-चिह्न नहीं। ‘तानि’ (नपुंसक बहुवचन) किसे कहता है, इकाई नहीं बताती; ठीक पहले "
           "इकाई ८६ (आठ संस्थान) है, पर जोड़ा नहीं गया। ‘वक्ष्यंते’ = वक्ष्यन्ते (√वच्, भविष्यत्, कर्मवाच्य अर्थ: कहे "
           "जाएँगे)। सन्धि जाँची: तानि + अत्र → तान्यत्र (इ + अ → य); अत्र + एव → अत्रैव (अ + ए → ऐ); एव + उत्तरत्र → "
           "एवोत्तरत्र (अ + उ → ओ)।"),
    "88": ("गद्य-पंक्ति; विश्वास निम्न; कोई पाठ-चिह्न नहीं। लम्बा समास ‘विपरीतेन्द्रियार्थाम्…अभिपन्नाम्’ स्त्री के विशेषणों की "
           "एक कड़ी माना गया। ‘संवरण’ (बन्द होना या ढकना; क्या बन्द होता है, नहीं कहा) और ‘मक्कल’ (दुर्लभ शब्द; अन्य ग्रन्थों में "
           "प्रसव के बाद की पीड़ा या जमा रक्त) यहाँ अस्पष्ट, अनुवाद नहीं किए; इन पर प्रश्न नहीं। ‘श्वास’ = साँस की तकलीफ, या "
           "केवल साँस। ‘वर्जयेत्’ = छोड़ दे; किस बात में (जैसे आगे की क्रियाएँ), इकाई नहीं कहती। स्त्री (मूढगर्भ वाली) प्रसंग "
           "से समझी जाती है। सन्धि जाँची: सर्वेषु + अपि → सर्वेष्वपि (उ + अ → व); विपरीत + इन्द्रिय → विपरीतेन्द्रिय (अ + इ → "
           "ए); इन्द्रिय + अर्थाम् → इन्द्रियार्थाम् (अ + अ → आ); भ्रम + अभिपन्नाम् → भ्रमाभिपन्नाम्; पूति + उद्गाराम् → "
           "पूत्युद्गाराम् (इ + उ → यु)।"),
    "89": ("दो छपी गद्य-पंक्तियाँ; विश्वास मध्यम; कोई पाठ-चिह्न नहीं। ‘गर्भशल्य’ तकनीकी शब्द रखा: शल्य = काँटा, बाण, या "
           "शरीर में अटकी बाहरी वस्तु; डेटा इसे ‘शल्य के रूप में गर्भ’ पढ़ता है। ‘तत्’ (नपुंसक) गर्भशल्य को कहता माना गया। "
           "‘आशु’ (शीघ्र) दम घोंटने से जुड़ता है या मारने से, दोनों सम्भव; इस पर प्रश्न नहीं। ‘(उसे)’ संस्कृत में नहीं; माता "
           "स्वाभाविक कर्म है। सन्धि जाँची: क्षणम् + अपि → क्षणमपि; अपि + उपेक्षेत → अप्युपेक्षेत (इ + उ → यु); तत् + हि → "
           "तद्धि (त् → द्, ह → ध); निरुच्छ्वासीकृत्य + आशु → निरुच्छ्वासीकृत्याशु (अ + आ → आ)।"),
    "90": ("गद्य-पंक्ति; विश्वास उच्च; कोई पाठ-चिह्न नहीं। सचेतन = चेतना वाला, जीवित; यह कैसे जाना जाए, इकाई नहीं कहती। "
           "‘विषमम्’ क्रियाविशेषण (विषम रूप से) माना गया; ‘विषम अंगों को’ भी पढ़ा जा सकता है; इस पर प्रश्न नहीं। "
           "‘विदार्यमाण’ = वि-√दॄ, वर्तमान कर्मवाच्य कृदन्त। सन्धि जाँची: सचेतनः + च → सचेतनश्च (विसर्ग + च → श्); "
           "विदार्यमाणः + विषमम् → विदार्यमाणो विषमम् (अः + घोष व्यंजन → ओ); विषमम् + अङ्गानि → विषममङ्गानि; छपे ‘अंगानि’ "
           "में ं = ङ्।"),
    "91": ("गद्य-पंक्ति; विश्वास निम्न। पाठ-चिह्न (सम्भावित): छपा ‘सूत्यः’ व्याकरण में नहीं बैठता; ‘सूत्यै’ (चतुर्थी: प्रसव "
           "के लिए) अनुमानित; इस पर प्रश्न नहीं। ‘प्रयतेरन्’ (वे प्रयत्न करें) का कर्ता नहीं दिया; बहुवचन ‘प्रयतेरन्’ से "
           "एकवचन ‘प्रयुञ्जीत’ में बदलाव है। ‘तत्सङ्गे’ में ‘तत्’ (गर्भ या उसका अटकना) नहीं बताया; सङ्ग इकाई ९२ में आगे "
           "लिया गया। ‘पूर्वोक्तानि’ मन्त्र और औषध दोनों से जुड़ा माना; पहले का कौन-सा प्रसंग, नहीं कहा। सन्धि जाँची: "
           "पूर्व + उक्तानि → पूर्वोक्तानि (अ + उ → ओ); मन्त्र + औषधानि → मन्त्रौषधानि (अ + औ → औ); छपे ‘संगे’, ‘मंत्र’, "
           "‘प्रयुंजीत’ में ं = ङ्, न्, ञ्।"),
    "92": ("गद्य-पंक्ति; विश्वास उच्च; कोई पाठ-चिह्न नहीं। सङ्ग = अटकना, रुकावट (गर्भ का, इकाई ९१ से समझा)। प्रकार यहाँ "
           "नहीं गिनाए। सन्धि जाँची: त्रिविधः + तु → त्रिविधस्तु (विसर्ग + त → स्); सङ्गः + भवति → सङ्गो भवति (अः + घोष "
           "व्यंजन → ओ)।"),
    "93": ("गद्य-पंक्ति; विश्वास मध्यम; कोई पाठ-चिह्न नहीं। क्रिया नहीं; सम्भवतः इकाई ९२ (तीन प्रकार का सङ्ग) को आगे बढ़ाती है, "
           "पर ये तीन ही ‘तीन प्रकार’ हैं, यह नहीं कहा। जघन = कूल्हे का भाग (कमर, नितम्ब); ठीक अंग परिभाषित नहीं। प्रसूति की "
           "सम्भावित व्याख्या (पाठ नहीं कहता): सिर, कन्धे और नितम्ब से अटकना। सन्धि जाँची: शिरसि + अंसे → शिरस्यंसे "
           "(इ + अ → य)।"),
    "94": ("दो छपी गद्य-पंक्तियाँ; विश्वास मध्यम। पाठ-चिह्न (लगभग निश्चित): छपे ‘कर्मार्थर्ववेद’ में एक र् अधिक; कर्म + अथर्व → "
           "कर्माथर्व। क्रिया ‘कहते हैं’ (आहुः) नहीं छपी; ‘इति एके’ = कुछ कहते हैं। जरायु = जेर, अपरा या झिल्लियाँ (मानक); "
           "इस अध्याय में पहले ‘अपरा’ शब्द आया है। ‘सामान्य’ का सीधा अर्थ ‘साझा’; ‘के समान’ अनुवाद है। यह इकाई ९४-९५ में "
           "दिए तीन मतों में से दो है; कौन-सा माना गया, नहीं कहा। ‘आदि’ = से आरम्भ; बाकी कर्म नहीं गिनाए। सन्धि जाँची: "
           "कर्म + इति → कर्मेति (अ + इ → ए); इति + एके → इत्येके (इ + ए → ये); मन्त्र + आदि → मन्त्रादि (अ + आ → आ); "
           "विहितम् + इति → विहितमिति।"),
}


# ===================================================================== AIDS
AIDS = {
    "82": {
        "diagram": {"groups": [
            {"label": "देह के लक्षण (क्रम से)", "items": ["शूल अधिक", "गर्भ न हिले", "अन्य (लक्षण) प्रकट; संज्ञा नहीं दी",
                                                     "योनि से स्राव नहीं", "आँखें: क्रिया अस्पष्ट (संस्येते)"]},
            {"label": "स्त्री की दशा (क्रम से)", "items": ["भृश अरति, व्यथा", "अलग ढंग की चेष्टा", "निढाल, थकी",
                                                     "दिन-रात रोए", "नींद नहीं (छपा: स्वप्निति)", "हर श्वास कठिन",
                                                     "अति कष्ट से जीए", "क्षीण हो (सम्भावित)"]},
            {"label": "नाम", "items": ["मृतगर्भा: मरे गर्भ वाली"]}]},
        "chunks": "शूलमधिकमुपजायते | न च स्पंदते गर्भो | ऽन्यानि प्रादुर्भवंति | न स्रवति योनिः | अक्षिणी चास्याः संस्येते (?) | "
                  "तथा भृशमरतिपरीता व्यथते | ऽन्यथा चेष्टते | ताम्यति श्राम्यति | रोदित्यहर्निशं | न स्वप्निति | "
                  "प्रत्युच्छ्वासात्कृच्छ्राच्छ्वसिति | अतिकष्टं प्राणिति | क्षयतीति | एवंविधां स्त्रियं मृतगर्भां विद्यान्",
        "sandhi": "त् + श → च्छ: कृच्छ्रात् + श्वसिति → कृच्छ्राच्छ्वसिति · अः + अ → ओऽ: गर्भः + अन्यानि → गर्भोऽन्यानि · "
                  "इ + अ → य: रोदिति + अहर्निशम् → रोदित्यहर्निशम्।",
    },
    "83": {
        "diagram": {"groups": [
            {"label": "गर्भ कैसे पहुँचा", "items": ["कभी-कभी (कदाचित्)", "गलत ढंग से (असम्यक्)",
                                                 "अपत्यपथ में (सम्भवतः प्रसव-मार्ग)", "अनेक प्रकार से (अनेकधा)"]},
            {"label": "किससे", "items": ["विगुण वायु से पीड़ित", "और मोहित"]},
            {"label": "नाम", "items": ["मूढगर्भ (मूढ = मोहित, अटका)"]}]},
        "chunks": "तं तु गर्भं | कदाचिदसम्यगपत्यपथमनेकधा | प्रतिपन्नं | विगुणेन वायुना | पीडितं मोहितं च | मूढगर्भमित्याहुः",
        "sandhi": "क् + स्वर → ग्: असम्यक् + अपत्य → असम्यगपत्य · त् + स्वर → द्: कदाचित् + असम्यक् → कदाचिदसम्यक् · "
                  "इ + आ → या: इति + आहुः → इत्याहुः।",
    },
    "84": {
        "chunks": "विगुण | अनिल | प्रतिपीडनै (?) | वैचित्र्याद् | असंसंख्यगातिं (= असङ्ख्यगतिम्?) | च",
        "sandhi": "अ + अ → आ: विगुण + अनिल → विगुणानिल · त् + स्वर → द्: वैचित्र्यात् + अ... → वैचित्र्याद...।",
        "frame": "कारण: विगुण अनिल (बिगड़ी वायु) → उसका प्रतिपीडन (दबाव) → उसकी विविधता (वैचित्र्यात्, पंचमी = कारण) → "
                 "फल: अनुमानित पाठ पर असंख्य गतियाँ। क्रिया इकाई ८३ से।",
    },
    "85": {
        "diagram": {"groups": [
            {"label": "संक्षेप में गति: त्रिविधा", "items": ["१ ऊर्ध्वा: ऊपर की ओर (सुधारा पाठ)", "२ तिर्यक्: तिरछी",
                                                       "३ न्युब्जा: औंधी, झुकी"]}]},
        "chunks": "समासतस्तु | त्रिविधा | गतिरूध्र्वा (= गतिरूर्ध्वा) | तिर्यङ्ङ्युब्जा (= तिर्यङ् न्युब्जा) च",
        "sandhi": "विसर्ग + त → स्: समासतः + तु → समासतस्तु · इः + स्वर → इर्: गतिः + ऊर्ध्वा → गतिरूर्ध्वा।",
        "pegs": "ऊपर, तिरछा, औंधा: तीन दिशाएँ जैसे हाथ से इशारा: ऊपर उँगली, फिर हथेली आड़ी, फिर हथेली उलटी। (लेखक की अपनी याद-युक्ति)",
    },
    "86": {
        "chunks": "संस्थानानि | पुनरष्टौ",
        "sandhi": "पुनः (मूल र्) + स्वर → पुनर्: पुनः + अष्टौ → पुनरष्टौ।",
        "anchors": "याद-सूत्र: गति तीन (इकाई ८५), संस्थान आठ (इकाई ८६), सङ्ग तीन (इकाई ९२)। (मेरी याद-पद्धति)",
    },
    "87": {
        "chunks": "तान्यत्रैवोत्तरत्र | वक्ष्यंते",
        "sandhi": "इ + अ → य: तानि + अत्र → तान्यत्र · अ + ए → ऐ: अत्र + एव → अत्रैव · अ + उ → ओ: एव + उत्तरत्र → एवोत्तरत्र।",
        "frame": "क्या: तानि (वे; नाम नहीं दिया) → कहाँ: अत्र एव (यहीं) → कब: उत्तरत्र (आगे) → क्रिया: वक्ष्यन्ते (कहे जाएँगे)।",
    },
    "88": {
        "diagram": {"groups": [
            {"label": "ऐसी स्त्री (क्रम से)", "items": ["इन्द्रियों के विषय उलटे", "आक्षेप (ऐंठन)", "योनि का खिसकना",
                                                  "संवरण (अर्थ अस्पष्ट)", "मक्कल (अर्थ अस्पष्ट)", "श्वास",
                                                  "भ्रम (चक्कर)", "शरीर ठण्डा", "डकार दुर्गन्धित"]},
            {"label": "निर्देश", "items": ["वर्जयेत्: छोड़ दे", "किस बात में: नहीं कहा"]}]},
        "chunks": "तेषु सर्वेष्वपि | विपरीतेंद्रियार्थाम् | आक्षेपयोनिस्रंशसंवरणमक्कलश्वासभ्रमाभिपन्नां | शीतगात्रां | "
                  "पूत्युद्गारां च | वर्जयेत्",
        "sandhi": "उ + अ → व: सर्वेषु + अपि → सर्वेष्वपि · इ + उ → यु: पूति + उद्गाराम् → पूत्युद्गाराम् · अ + इ → ए: "
                  "विपरीत + इन्द्रिय → विपरीतेन्द्रिय।",
    },
    "89": {
        "chain": {"steps": ["गर्भशल्य की उपेक्षा", "दम घुटना (निरुच्छ्वासीकृत्य)", "शीघ्र (आशु)", "माता की मृत्यु (हन्यात्)",
                            "इसलिए: क्षण भर भी उपेक्षा नहीं"]},
        "chunks": "न तु क्षणमप्युपेक्षेत | गर्भशल्यं | तद्धि | निरुच्छ्वासीकृत्याशु | जननीं हन्यात्",
        "sandhi": "इ + उ → यु: अपि + उपेक्षेत → अप्युपेक्षेत · त् + ह → द्ध: तत् + हि → तद्धि · अ + आ → आ: "
                  "निरुच्छ्वासीकृत्य + आशु → निरुच्छ्वासीकृत्याशु।",
    },
    "90": {
        "chunks": "सचेतनश्च गर्भः | शस्त्रेण विदार्यमाणो | विषममंगानि | विक्षिपेत्",
        "sandhi": "विसर्ग + च → श्: सचेतनः + च → सचेतनश्च · अः + घोष व्यंजन → ओ: विदार्यमाणः + विषमम् → विदार्यमाणो विषमम्।",
        "frame": "कौन: सचेतन गर्भ (जीवित) → कब: शस्त्र से चीरा जाते समय (विदार्यमाणः) → क्या कर सकता है: अंगों को विषम रूप से "
                 "फेंके (विक्षिपेत्)।",
    },
    "91": {
        "chunks": "तस्मात्तत्संगे | सूत्यः (?) प्रयतेरन् | पूर्वोक्तानि च | मंत्रौषधानि प्रयुंजीत",
        "sandhi": "अ + उ → ओ: पूर्व + उक्तानि → पूर्वोक्तानि · अ + औ → औ: मन्त्र + औषधानि → मन्त्रौषधानि।",
        "frame": "क्यों: तस्मात् (इसलिए) → कब: तत्सङ्गे (उसके अटकने पर) → वे: प्रयतेरन् (प्रयत्न करें) → एक: प्रयुञ्जीत "
                 "(प्रयोग करे) → क्या: पहले कहे मन्त्र और औषध।",
    },
    "92": {
        "chunks": "त्रिविधस्तु | संगो भवति",
        "sandhi": "विसर्ग + त → स्: त्रिविधः + तु → त्रिविधस्तु · अः + घोष व्यंजन → ओ: सङ्गः + भवति → सङ्गो भवति।",
        "anchors": "लिंग-मेल: त्रिविधः सङ्गः (पुं.), त्रिविधा गतिः (स्त्री., इकाई ८५), त्रिविधं कर्म (नपुं.)।",
    },
    "93": {
        "diagram": {"groups": [
            {"label": "तीन स्थान (वा = या)", "items": ["शिरसि: सिर में", "अंसे: कन्धे में", "जघने: कूल्हे के भाग में"]}]},
        "chunks": "शिरस्यंसे | जघने वा",
        "sandhi": "इ + अ → य: शिरसि + अंसे → शिरस्यंसे।",
    },
    "94": {
        "contrast": {"groups": [
            {"label": "कुछ (एके) का मत: १", "items": ["मूढगर्भ का कर्म", "जरायु (जेर) गिराने के समान"]},
            {"label": "कुछ (एके) का मत: २", "items": ["मन्त्र आदि वाला कर्म", "अथर्ववेद में विहित"]},
            {"label": "ग्रन्थ का निर्णय", "items": ["नहीं कहा"]}]},
        "chunks": "मूढगर्भस्य तु | जरायुपातनसामान्यं | कर्मेत्येके || मंत्रादिकर्मार्थर्ववेदविहितम् (= ...कर्माथर्ववेद...) | इत्येके",
        "sandhi": "अ + इ → ए: कर्म + इति → कर्मेति · इ + ए → ये: इति + एके → इत्येके · अ + आ → आ: मन्त्र + आदि → मन्त्रादि।",
    },
}


# ===================================================================== IMAGE_SPECS
IMAGE_SPECS = {
    ("82", "diagram"): {
        "file": "sh4-mritagarbha-82.svg",
        "alt": ("Two columns of unit 82, signs of a dead fetus in line order. Body: excess pain; fetus does not move; other "
                "(signs) appear; no flow from the yoni; the eyes' verb unclear. The woman: greatly restless and distressed; "
                "acts differently; languishes and tires; weeps day and night; no sleep (printed svapniti); each breath hard; "
                "lives in great distress; wastes away (probable). Name: mṛtagarbhā."),
        "type": "split",
        "title": "इकाई ८२: मृतगर्भा के लक्षण",
        "cols": [["देह (क्रम से)", ["१ शूल अधिक", "२ गर्भ न हिले", "३ अन्य प्रकट (संज्ञा नहीं)", "४ योनि से स्राव नहीं",
                                   "५ आँखें: क्रिया अस्पष्ट"]],
                 ["स्त्री (क्रम से)", ["६ भृश अरति, व्यथा", "७ अलग ढंग की चेष्टा", "८ निढाल, थकी", "९ दिन-रात रोए",
                                      "१० नींद नहीं", "११ हर श्वास कठिन", "१२ अति कष्ट से जीए", "१३ क्षीण (सम्भावित)",
                                      "नाम: मृतगर्भा"]]],
    },
    ("83", "diagram"): {
        "file": "sh4-mudhagarbha-83.svg",
        "alt": ("Flowchart of unit 83: the fetus has entered the path of the offspring (probably the birth passage) "
                "sometimes, wrongly and in many ways, and is afflicted and bewildered by deranged vāyu; both lead to the "
                "name mūḍhagarbha."),
        "type": "mermaid",
        "code": ("flowchart TD\n"
                 "  A[\"गर्भ\"] --> B[\"कभी-कभी, गलत ढंग से, अनेक प्रकार से अपत्यपथ में पहुँचा\"]\n"
                 "  A --> D[\"विगुण वायु से पीड़ित और मोहित\"]\n"
                 "  B --> F[\"नाम: मूढगर्भ\"]\n"
                 "  D --> F\n"),
    },
    ("85", "diagram"): {
        "file": "sh4-trividha-gati-85.svg",
        "alt": ("Table of unit 85, the three courses in brief, in line order: ūrdhvā, upward (printed ūdhrvā, a corrected "
                "reading); tiryak, transverse; nyubjā, face-down."),
        "type": "table",
        "title": "इकाई ८५: संक्षेप में तीन गति",
        "heads": ["शब्द", "अर्थ"],
        "rows": [["१ ऊर्ध्वा (छपा: ऊध्र्वा)", "ऊपर की ओर"], ["२ तिर्यक्", "तिरछी, आड़ी"], ["३ न्युब्जा", "औंधी, झुकी"]],
    },
    ("88", "diagram"): {
        "file": "sh4-varjya-88.svg",
        "alt": ("Two columns of unit 88. The woman, signs in line order: sense-objects reversed; convulsion; slipping of the "
                "yoni; saṃvaraṇa (sense unclear); makkala (sense unclear); śvāsa; giddiness; cold body; foul belching. "
                "Instruction: one should avoid her; in what respect is not stated."),
        "type": "split",
        "title": "इकाई ८८: किसे छोड़े",
        "cols": [["ऐसी स्त्री (क्रम से)", ["१ इन्द्रिय-विषय उलटे", "२ आक्षेप (ऐंठन)", "३ योनि का खिसकना",
                                          "४ संवरण (अर्थ अस्पष्ट)", "५ मक्कल (अर्थ अस्पष्ट)", "६ श्वास",
                                          "७ भ्रम (चक्कर)", "८ शरीर ठण्डा", "९ डकार दुर्गन्धित"]],
                 ["निर्देश", ["वर्जयेत्: छोड़ दे", "किस बात में: नहीं कहा"]]],
    },
    ("89", "chain"): {
        "file": "sh4-garbhashalya-89.svg",
        "alt": ("Chain of unit 89: neglect of the garbhaśalya; making breathless; quickly; death of the mother; therefore not "
                "even a moment's neglect."),
        "type": "chain",
        "title": "इकाई ८९: गर्भशल्य",
        "steps": ["गर्भशल्य की उपेक्षा", "दम घुटना", "शीघ्र (आशु)", "माता की मृत्यु", "इसलिए: क्षण भर भी देर नहीं"],
    },
    ("93", "diagram"): {
        "file": "sh4-sanga-sthana-93.svg",
        "alt": ("Table of unit 93, three places joined by 'or', in line order: in the head; in the shoulder; in the jaghana "
                "(hip region)."),
        "type": "table",
        "title": "इकाई ९३: तीन स्थान (वा = या)",
        "heads": ["शब्द", "अर्थ"],
        "rows": [["शिरसि", "सिर में"], ["अंसे", "कन्धे में"], ["जघने वा", "या कूल्हे के भाग में"]],
    },
    ("94", "contrast"): {
        "file": "sh4-matabheda-94.svg",
        "alt": ("Two columns of unit 94, two opinions of 'some'. First: the procedure for a mūḍhagarbha is the same as "
                "causing the afterbirth (jarāyu) to fall. Second: the procedure beginning with mantras is prescribed in "
                "the Atharvaveda. The text does not say which is held."),
        "type": "split",
        "title": "इकाई ९४: दो मत, निर्णय नहीं दिया",
        "cols": [["कुछ का मत: १", ["मूढगर्भ का कर्म", "जरायु (जेर) गिराने के समान"]],
                 ["कुछ का मत: २", ["मन्त्र आदि वाला कर्म", "अथर्ववेद में विहित"]]],
    },
}
