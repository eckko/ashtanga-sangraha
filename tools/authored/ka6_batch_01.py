from helpers import mcq, match, order, fill, multi, accepts

AUTHORED = {}

# ---------------------------------------------------------------- unit 1
AUTHORED["1"] = {
    "title": "अथातो बस्तिव्यापत्तिसिद्धिं",
    "question": "What does the opening formula of this Kalpa chapter announce as its subject?",
    "rule": ("The chapter opens: now, therefore, we shall explain the siddhi (success, "
             "accomplishment) of the mishaps (व्यापत्ति) of basti, the enema. "
             "व्याख्यास्यामः is first person plural future."),
    "limits": ("Only an announcement: no mishap, cause or remedy is named here. 'Successful "
               "treatment' for siddhi is an interpretive gloss of the data; the word itself "
               "means success or accomplishment."),
    "explain_hi": ("यह अध्याय का आरम्भ-सूत्र है: ‘अथ अतः’ यानी ‘अब, इसलिए’। विषय है ‘बस्ति-व्यापत्ति-सिद्धि’: "
                   "बस्ति (एनिमा) की व्यापत्तियों यानी गड़बड़ियों की सिद्धि, अर्थात् उनका सफल उपचार। "
                   "क्रिया ‘व्याख्यास्यामः’ उत्तम पुरुष बहुवचन भविष्यत् है: ‘हम व्याख्या करेंगे’। "
                   "इस इकाई में कोई व्यापत्ति या उपाय नहीं गिनाया गया, केवल विषय का नाम है।"),
    "hook": "अब बस्ति की गड़बड़ियाँ और उनकी सिद्धि: हम समझाएँगे।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "What subject does unit 1 announce for the chapter?",
            ("The mishaps of basti and their siddhi",
             "बस्ति-व्यापत्ति-सिद्धि: the accomplishment (treatment) of the mishaps of the enema."),
            [("The collecting and storing of emetic fruit",
              "That belongs to the emetic chapter; it is not named here."),
             ("The tastes of food in the cold season",
              "Seasons and tastes are not named in this formula."),
             ("The qualities of a good teacher of medicine",
              "No teacher is named; the subject is the basti's mishaps.")],
            "The formula names one subject: the siddhi of the vyāpatti (mishaps) of basti.",
            "अथातो बस्तिव्यापत्तिसिद्धिं व्याख्यास्यामः = now we shall explain the treatment of basti mishaps."),
        order(1, "Put the three parts of unit 1 in the text's order.",
              ["अथातः", "बस्तिव्यापत्तिसिद्धिम्", "व्याख्यास्यामः"],
              "Opening words, then the subject (object of the verb), then the verb.",
              "अथातः · बस्तिव्यापत्तिसिद्धिम् · व्याख्यास्यामः."),
        match(2, "Match each part of unit 1 to its meaning.",
              [["अथ", "now"], ["अतः", "therefore"], ["व्यापत्ति", "mishap, complication"],
               ["सिद्धि", "success, accomplishment"], ["व्याख्यास्यामः", "we shall explain"]],
              "The title compound is basti + vyāpatti + siddhi: the accomplishment of the enema's mishaps.",
              "व्यापत्ति = mishap; सिद्धि = success; व्याख्यास्यामः = we shall explain.",
              role="extend",
              teaches="The chapter title is a tat-puruṣa: the siddhi (success) of the vyāpatti (mishaps) of basti."),
        mcq("discriminate", 3, "Which split of अथातो is right?",
            ("अथ + अतः",
             "अ + अ gives आ; the visarga of अतः after अ turns into ओ before the voiced ब."),
            [("अथा + तः", "तः is not a word here; the long आ is two short अ joined."),
             ("अथ + आतः", "आतः is not the word; the card reads अतः, therefore."),
             ("अथो + अतः", "The ओ is the changed visarga at the end, not a vowel inside.")],
            "अथातो = अथ + अतः; the final ओ stands for -अः before a voiced sound.",
            "अ + अ → आ; -अः before a voiced consonant → -ओ."),
        mcq("apply", 4, "What does the verb form व्याख्यास्यामः tell about who speaks and when?",
            ("We, several speakers, will explain",
             "1 pl. future of vi-ā-√khyā: we shall explain."),
            [("He explained it in the past", "That would be third person singular, past."),
             ("You should explain it to us", "That would be a command to another person."),
             ("I am explaining it right now", "That would be first person singular, present.")],
            "The word split labels व्याख्यास्यामः as 1 pl. future.",
            "व्याख्यास्यामः = हम व्याख्या करेंगे (उत्तम पुरुष, बहुवचन, भविष्यत्)."),
        mcq("transfer", 5,
            "By the pattern of बस्ति-व्यापत्ति-सिद्धि, what would वमन-व्यापत्ति-सिद्धि (वमन, emesis) mean?",
            ("Treatment of the mishaps of emesis",
             "Same tat-puruṣa chain: the siddhi of the vyāpatti of vamana."),
            [("Emesis as the cure of basti mishaps", "Nothing in the compound names basti; the first member is वमन."),
             ("The success of emesis without mishaps", "व्यापत्ति is the mishap itself, not its absence."),
             ("A mishap caused by a successful cure", "The last member (सिद्धि) is the head; it is not a cause.")],
            "In X-व्यापत्ति-सिद्धि the first member names the procedure whose mishaps are treated.",
            "X-व्यापत्ति-सिद्धि = the successful treatment of the mishaps of X.",
            teaches="In a tat-puruṣa the last member is the head: X-vyāpatti-siddhi is the siddhi of the mishaps of X."),
    ],
}

# ---------------------------------------------------------------- unit 2
AUTHORED["2"] = {
    "title": "विबन्धगौरवाध्मान",
    "question": "Which mishaps of the basti does verse 2 list, and which of its names are obscure?",
    "rule": ("Line 1: obstruction (vibandha), heaviness, distension (ādhmāna), head-pain, vāhana, "
             "the upward-going. Line 2: belly-pain, aṅga-ruci, dhmā, heart-pain, cutting pain "
             "(kartana), flow (srava). The cause is in verse 3."),
    "limits": ("vāhana, aṅga-ruci and dhmā are obscure and only literally rendered; हत् is probably "
               "हृत् (heart), a possible misprint. Which six belong to non-application and which to "
               "over-application is not stated. Confidence low."),
    "explain_hi": ("यह श्लोक बिना क्रिया की एक सूची है; कारण (अयोग और अतियोग) अगले श्लोक में आता है। "
                   "पहली पंक्ति: विबन्ध यानी रुकावट (कब्ज़ या मल-वायु का रुकना, सम्भावित), गौरव यानी भारीपन, "
                   "आध्मान यानी पेट फूलना, शिरोरुज् यानी सिर-दर्द, ‘वाहन’ (अर्थ अस्पष्ट) और ऊपर जाने वाला। "
                   "दूसरी पंक्ति: कुक्षिशूल यानी पेट का शूल, ‘अंग-रुचि’ और ‘ध्मा’ (दोनों अस्पष्ट), हृदय की पीड़ा, "
                   "कर्तन यानी काटने जैसी पीड़ा और स्राव। अस्पष्ट नामों पर कोई प्रश्न नहीं है।"),
    "hook": "रुकावट, भार, फुलाव, सिर-दर्द ... पेट-शूल, कर्तन, स्राव: बस्ति की गड़बड़ियों की सूची।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "Which of these does verse 2 name among the mishaps of the basti?",
            ("Distension (आध्मान)", "आध्मान, distension or bloating, is the third name of line 1."),
            [("Fever (ज्वर)", "Fever is not named in verse 2."),
             ("Thirst (तृष्णा)", "Thirst is not named in verse 2."),
             ("Hiccup (हिक्का)", "Hiccup is not in this list.")],
            "Line 1 names vibandha, gaurava, ādhmāna, śiroruj, vāhana and the upward-going.",
            "आध्मान = distension; it is one of the listed mishaps."),
        match(1, "Match each clear mishap name of line 1 to its meaning.",
              [["विबन्ध", "obstruction, retention"], ["गौरव", "heaviness"],
               ["आध्मान", "distension, bloating"], ["शिरोरुज्", "head-pain"]],
              "These four names of line 1 are clear; vāhana is obscure and left out.",
              "विबन्ध = obstruction; गौरव = heaviness; आध्मान = distension; शिरोरुज् = head-pain."),
        order(2, "Put these mishap names in the order of verse 2.",
              ["विबन्ध", "आध्मान", "ऊर्ध्वग", "कुक्षिशूल", "कर्तन", "स्रव"],
              "Line 1 runs vibandha ... ādhmāna ... ūrdhvaga; line 2 runs kukṣiśūla ... kartana, srava.",
              "विबन्ध · आध्मान · ऊर्ध्वग ‖ कुक्षिशूल · कर्तन · स्रव.",
              role="extend",
              teaches="Line 1 ends with the upward-going (ऊर्ध्वग); line 2 starts with belly-pain and ends with flow (स्रव)."),
        mcq("discriminate", 3, "Which split of शिरोरुग् (in the first compound) is right?",
            ("शिरः + रुज्",
             "-अः before a voiced र becomes -ओ; final ज् becomes ग् before the voiced व that follows."),
            [("शिरो + रुग्", "शिरो is not the stem; the ओ is the changed visarga of शिरः."),
             ("शिर + ओरुज्", "ओरुज् is not a word; the word for pain is रुज्."),
             ("शिरः + उरुग्", "उरुग् is not a word; the visarga does not vanish before र here.")],
            "शिरः (head) + रुज् (pain) = head-pain.",
            "-अः + voiced consonant → -ओ: शिरः + रुज् → शिरोरुज्."),
        multi("apply", 4, "After a basti, a patient has heaviness and belly-pain. Which two of these does verse 2 name?",
              [("गौरव (heaviness)", "Right: the second name of line 1."),
               ("कुक्षिशूल (belly-pain)", "Right: the first name of line 2."),
               ("ज्वर (fever)", "Not named in verse 2."),
               ("तृष्णा (thirst)", "Not named in verse 2.")],
              [0, 1],
              "Heaviness (gaurava) is in line 1; belly-pain (kukṣiśūla) opens line 2.",
              "गौरव = heaviness (line 1); कुक्षिशूल = belly-pain (line 2)."),
        mcq("transfer", 5,
            "Like कुक्षि-शूल (belly-pain), what does पार्श्व-शूल mean (पार्श्व, side)?",
            ("Pain in the side",
             "The first member names the place, the last the pain: side-pain."),
            [("A side free from pain", "Nothing in the compound negates the pain."),
             ("Pain that moves from the belly", "The belly is not named in पार्श्वशूल."),
             ("Swelling of the side", "शूल is pain, not swelling.")],
            "कुक्षि-शूल = pain of the belly; पार्श्व-शूल = pain of the side.",
            "Place + शूल = pain in that place (tat-puruṣa).",
            teaches="Place + शूल is a tat-puruṣa: the pain of that place (kukṣiśūla = belly-pain)."),
    ],
}

# ---------------------------------------------------------------- unit 3
AUTHORED["3"] = {
    "title": "अयोगादतियोगाच्च",
    "question": "From which two faults of the basti do its mishaps arise, and to what kind of patient is it applied?",
    "rule": ("From non-application (ayoga) and over-application (atiyoga) of the basti there are "
             "six and six mishaps. Line 2 begins: applied to one whose body is not oiled and not "
             "sweated, and whose koṣṭha is heavy."),
    "limits": ("The verse does not say which six of verse 2 go with which fault. Line 2 is part of a "
               "sentence that ends in verse 5 (karoti). 'Neither oiled nor sweated' is the natural "
               "reading; 'not oiled, but sweated' is possible."),
    "explain_hi": ("यह श्लोक पिछली सूची का कारण बताता है: बस्ति के अयोग (ठीक से प्रयोग न होना) और अतियोग (अधिक प्रयोग) से "
                   "छह और छह आपत्तियाँ होती हैं। कौन-सी छह किसकी हैं, यह नहीं कहा गया। दूसरी पंक्ति एक नया वाक्य शुरू करती है "
                   "जो श्लोक ५ की क्रिया ‘करोति’ पर पूरा होता है: जिसका शरीर स्निग्ध और स्वेदित नहीं है और जिसका कोष्ठ भारी है, "
                   "उसमें दी गई बस्ति। ‘बस्ति’ शब्द इस वाक्य में आगे श्लोक ४ में आता है।"),
    "hook": "अयोग से छह, अतियोग से छह; बिना स्नेहन-स्वेदन, भारी कोष्ठ वाले में दी गई बस्ति ...",
    "core": True,
    "questions": [
        mcq("pretest", 0, "From what does verse 3 say the mishaps of the basti come?",
            ("From non-application and over-application",
             "अयोगात् अतियोगात् च: from non-application and from over-application."),
            [("From cold weather and from hot weather", "No season is named in verse 3."),
             ("From a wrong drug and from a wrong time", "Neither drug nor time is named as the cause."),
             ("From a weak patient and a strong one", "Strength of the patient is not named here.")],
            "The two causes are ayoga (non-application) and atiyoga (over-application).",
            "अयोग + अतियोग → बस्ति की आपत्तियाँ."),
        match(1, "Match each word of verse 3 to its meaning.",
              [["अयोग", "non-application"], ["अतियोग", "over-application"],
               ["आपदः", "mishaps"], ["योजितः", "applied"]],
              "Two faults, the mishaps they cause, and the word for the basti being applied.",
              "अयोग = non-application; अतियोग = over-application; आपदः = mishaps; योजितः = applied."),
        order(2, "Put these words of line 1 in the order of the verse.",
              ["अयोगात्", "अतियोगात्", "बस्तेः", "स्युः", "षट्षडापदः"],
              "First the two causes, then 'of the basti', the verb, and the six-and-six mishaps.",
              "अयोगात् · अतियोगात् · बस्तेः · स्युः · षट्षडापदः.",
              role="extend",
              teaches="Line 1 says: from ayoga and atiyoga of the basti there are six and six mishaps (āpadaḥ)."),
        mcq("discriminate", 3, "Which split of षट्षडापदः is right?",
            ("षट् + षट् + आपदः",
             "Final ट् becomes ड् before a vowel: षट् + आपदः → षडापदः."),
            [("षट्ष + डापदः", "डापदः is not a word; the ड is the changed ट्."),
             ("षट् + षडा + पदः", "पदः (feet) does not fit; the word is आपदः, mishaps."),
             ("षष् + टषड् + आपदः", "These pieces are not words.")],
            "Six (षट्), six (षट्), mishaps (आपदः).",
            "ट् → ड् before a vowel: षट् + आपदः → षडापदः."),
        mcq("apply", 4, "What does line 2 say about the koṣṭha (belly) of the patient?",
            ("It is heavy (गुरु)", "गुरुकोष्ठस्य: of one whose koṣṭha is heavy."),
            [("It is light and empty", "The word is गुरु, heavy, not light."),
             ("It is soft and oiled", "Oiling is denied of the body, and the koṣṭha is called heavy."),
             ("It is hot and burning", "Heat of the koṣṭha is not named in verse 3.")],
            "The patient of line 2: body not oiled, not sweated; koṣṭha heavy.",
            "गुरुकोष्ठ = heavy koṣṭha (storehouse, belly)."),
        mcq("transfer", 5,
            "By the pattern of अयोगात् and अतियोगात्, which form means from over-eating (भोजन, eating)?",
            ("अतिभोजनात्", "अति- gives excess and -आत् gives from: from over-eating."),
            [("अभोजनात्", "अ- negates: from not eating."),
             ("अतिभोजनम्", "This is over-eating itself, not 'from'."),
             ("भोजनस्य", "This is 'of eating', a genitive.")],
            "अ- = not, अति- = over; -आत् = from (ablative).",
            "अ- (not) · अति- (excess) + -आत् (from).",
            teaches="Prefix अ- negates and अति- marks excess; the ablative -आत् gives the cause (from ...)."),
    ],
}

# ---------------------------------------------------------------- unit 4
AUTHORED["4"] = {
    "title": "शीतोऽल्पस्नेहलवण",
    "question": "Which faulty kinds of basti does verse 4 name, and what does such a basti do to the doṣa?",
    "rule": ("A basti that is cold, or has little oil, salt, drug and quantity, or is even thick, "
             "agitates that doṣa and, because of weakness, does not expel it. The sentence "
             "continues to the verb in verse 5."),
    "limits": ("Whose weakness (durbalatva) is meant is not stated; the basti is the natural reading, "
               "the patient is possible. Whether 'little' covers all four of oil, salt, drug and "
               "quantity is not fixed. The effects come in verse 5."),
    "explain_hi": ("यह श्लोक बताता है कि बस्ति कैसी हो तो गड़बड़ होती है: ठंडी, या जिसमें स्नेह, लवण, द्रव्य और मात्रा "
                   "अल्प हो, अथवा गाढ़ी। ऐसी बस्ति उस दोष को क्षुब्ध तो करती है, पर दुर्बलता के कारण उसे बाहर नहीं निकालती। "
                   "दुर्बलता किसकी है (बस्ति की या रोगी की), यह स्पष्ट नहीं; सहज अर्थ बस्ति का है। "
                   "वाक्य की क्रिया ‘करोति’ अगले श्लोक में है।"),
    "hook": "ठंडी, कम-स्नेह, गाढ़ी बस्ति: दोष को हिलाए, निकाल न पाए।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "What does the faulty basti of verse 4 do with the doṣa?",
            ("Agitates it but does not expel it",
             "संक्षोभ्य ... अनिर्हरन्: having agitated it, not expelling it."),
            [("Expels it fully at once", "अनिर्हरन् means not expelling."),
             ("Leaves it untouched and calm", "संक्षोभ्य says the doṣa is agitated."),
             ("Turns it into another doṣa", "No change of doṣa is named.")],
            "The basti stirs up the doṣa and, through weakness, does not carry it out.",
            "संक्षोभ्य = having agitated; अनिर्हरन् = not expelling."),
        match(1, "Match each word of verse 4 to its meaning.",
              [["शीतः", "cold"], ["घनः", "thick"], ["संक्षोभ्य", "having agitated"],
               ["अनिर्हरन्", "not expelling"]],
              "Two faults of the basti and two words for what it does.",
              "शीतः = cold; घनः = thick; संक्षोभ्य = having agitated; अनिर्हरन् = not expelling."),
        order(2, "Put these words of line 2 in the order of the verse.",
              ["बस्तिः", "संक्षोभ्य", "तं दोषम्", "दुर्बलत्वात्", "अनिर्हरन्"],
              "The basti, having agitated that doṣa, because of weakness, not expelling (it).",
              "बस्तिः · संक्षोभ्य · तं दोषम् · दुर्बलत्वात् · अनिर्हरन्.",
              role="extend",
              teaches="Line 2 is a chain: the basti agitates the doṣa, and because of weakness does not expel it."),
        mcq("discriminate", 3, "Which split of the printed शीतोल्प... is right?",
            ("शीतः + अल्प...",
             "-अः + अ- gives -ओऽ-: शीतोऽल्प; the print drops the avagraha."),
            [("शीत + ओल्प...", "ओल्प is not a word; the ओ is the changed visarga."),
             ("शीतो + लप...", "लप is not the word; the word is अल्प, little."),
             ("शीतः + उल्प...", "अः + उ would not give this form, and उल्प is not a word.")],
            "Two words: शीतः (cold) and अल्प- (little), the first member of the next compound.",
            "-अः + अ → -ओऽ (avagraha): शीतः + अल्प → शीतोऽल्प."),
        mcq("apply", 4, "A physician gives a thick basti. Does verse 4 count it among the faulty ones?",
            ("Yes, thick (घन) is named",
             "घनोऽपि वा: or even thick."),
            [("No, only a cold basti is named", "Cold is one fault; thick is also named."),
             ("No, only lack of oil is named", "Little oil is one fault; thick is also named."),
             ("Only if salt is lacking too", "The verse names thick as a fault on its own, with वा (or).")],
            "Line 1 lists three alternatives: cold, or little oil/salt/drug/quantity, or even thick.",
            "शीत · अल्प-स्नेह-लवण-द्रव्य-मात्र · घन: तीनों विकल्प (वा)."),
        mcq("transfer", 5,
            "Like अनिर्हरन् (not expelling), which form means not seeing (पश्यन्, seeing)?",
            ("अपश्यन्", "Negative अ- before a consonant: अ + पश्यन् = अपश्यन्."),
            [("अनपश्यन्", "अन्- is used before a vowel, not before प."),
             ("अतिपश्यन्", "अति- means over or excess, not not."),
             ("पश्यन्नः", "This is not a negative form.")],
            "अ + निर्हरन् = अनिर्हरन्; in the same way अ + पश्यन् = अपश्यन्.",
            "Negative prefix: अ- before a consonant, अन्- before a vowel.",
            teaches="The negative prefix is अ- before a consonant (अनिर्हरन्, अपश्यन्) and अन्- before a vowel."),
    ],
}

# ---------------------------------------------------------------- unit 5
AUTHORED["5"] = {
    "title": "करोति वातविण्मूत्रविबन्धम्",
    "question": "What does the faulty basti of verses 3-4 cause, according to verse 5?",
    "rule": ("It causes an extremely severe obstruction of wind, stool and urine; pain in the "
             "basti (bladder, lower belly) and navel; ānāha; hṛllepa; and swelling in the anus."),
    "limits": ("Here basti is the organ, not the enema. Vāta is read as passing wind; the humour is "
               "not excluded. hṛllepa (coating at the heart) is a probable modern sense. Itching and "
               "the rest follow in verse 6."),
    "explain_hi": ("यहाँ श्लोक ३ से चला वाक्य अपनी क्रिया ‘करोति’ (करती है) पाता है। अयोग वाली बस्ति वायु, मल और मूत्र का "
                   "अत्यन्त भयंकर विबन्ध करती है। फिर बस्ति (यहाँ अंग: मूत्राशय या निचला पेट) और नाभि में पीड़ा, "
                   "आनाह (रुकावट के साथ पेट का फूलना), हृल्लेप (हृदय पर लेप-सा लगना, सम्भावित अर्थ) और गुदा में सूजन। "
                   "सूची अगले श्लोक में आगे चलती है।"),
    "hook": "वायु-मल-मूत्र रुके; बस्ति-नाभि में दर्द, आनाह, हृल्लेप, गुदा में सूजन।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "Which three does verse 5 say are obstructed?",
            ("Wind, stool and urine", "वात-विट्-मूत्र-विबन्ध: obstruction of wind, stool and urine."),
            [("Sweat, tears and urine", "Sweat and tears are not named."),
             ("Blood, bile and phlegm", "These are not named in verse 5."),
             ("Breath, speech and sleep", "None of these is named.")],
            "विण्मूत्र = विट् (stool) + मूत्र (urine), after वात (wind).",
            "वात · विट् · मूत्र: तीनों का विबन्ध."),
        order(1, "Put these effects in the order of verse 5.",
              ["विबन्ध", "बस्ति-नाभि-रुजा", "आनाह", "हृल्लेप", "गुदे श्वयथु"],
              "First the obstruction, then pain in basti and navel, ānāha, hṛllepa, swelling in the anus.",
              "विबन्ध · बस्ति-नाभि-रुजा · आनाह · हृल्लेप · गुदे श्वयथु."),
        match(2, "Match each effect named in verse 5 to its meaning.",
              [["विबन्ध", "obstruction, retention"], ["आनाह", "distension with retention"],
               ["हृल्लेप", "a coating felt at the heart"], ["श्वयथु", "swelling"]],
              "Four of the effects of the faulty basti.",
              "विबन्ध = obstruction; आनाह = distension with retention; हृल्लेप = heart-coating; श्वयथु = swelling.",
              role="extend",
              teaches="Verse 5 names obstruction, pain, ānāha, hṛllepa and swelling of the anus as effects."),
        mcq("discriminate", 3, "In बस्तिनाभिरुजा of verse 5, what does बस्ति mean?",
            ("The bladder or lower belly, an organ",
             "Beside नाभि (navel) and रुज् (pain), basti names a part of the body."),
            [("The enema given to the patient", "That is the sense in verses 3-4, not in this compound."),
             ("The doṣa stirred by the enema", "बस्ति is not a name of a doṣa."),
             ("The fluid of the decoction", "The compound is about places of pain.")],
            "The same word basti can mean the enema or the organ; here it is the organ.",
            "बस्ति-नाभि-रुजा = pain in the bladder (lower belly) and navel."),
        mcq("apply", 4, "Where does verse 5 place the swelling (श्वयथु)?",
            ("In the anus (गुदे)", "श्वयथुं गुदे: swelling in the anus."),
            [("In the navel", "The navel is named with pain, not swelling."),
             ("In the heart", "The heart is named with hṛllepa, not swelling."),
             ("In the feet", "The feet are not named in verse 5.")],
            "गुदे is locative singular: in the anus.",
            "श्वयथुं गुदे = गुदा में सूजन."),
        mcq("transfer", 5, "Like हृद् + लेपम् → हृल्लेपम्, how is तद् + लोकः (that world) joined?",
            ("तल्लोकः", "द् before ल becomes ल्: तद् + लोकः → तल्लोकः."),
            [("तद्लोकः", "The द् is not left unchanged before ल."),
             ("तंलोकः", "An anusvara is not made from द्."),
             ("तत्लोकः", "द् does not turn into त् before ल; it turns into ल्.")],
            "हृद् + लेप → हृल्लेप; in the same way तद् + लोक → तल्लोक.",
            "त्/द् + ल → ल्ल.",
            teaches="A final त्/द् before ल becomes ल् (हृद् + लेप = हृल्लेप; तद् + लोक = तल्लोक)."),
    ],
}

# ---------------------------------------------------------------- unit 6
AUTHORED["6"] = {
    "title": "कण्डूगण्डानि वैवर्ण्यम्",
    "question": "Which further effects does verse 6 add, and what does line 2 point to for one with atisāra?",
    "rule": ("Line 1 adds itching, gaṇḍa (lumps, swellings), discolouration, restlessness (arati) "
             "and softness of the fire (vahni). Line 2: the pair of decoctions prescribed earlier, "
             "in one with atisāra (diarrhoea)."),
    "limits": ("Softness of the fire probably points to weak digestion; the verse does not say so. "
               "The pair of decoctions is not identified. How madhyadoṣe should be read is an open "
               "reviewer question; no question rests on it."),
    "explain_hi": ("पहली पंक्ति पिछली सूची को पूरा करती है (क्रिया ‘करोति’ श्लोक ५ से): कण्डू यानी खुजली, गण्ड यानी गाँठें या सूजन, "
                   "वैवर्ण्य यानी रंग बिगड़ना, अरति यानी बेचैनी और वह्नि (अग्नि) की मृदुता। "
                   "दूसरी पंक्ति उपचार की ओर मुड़ती है: पहले बताए गए दो काढ़े (क्वाथ), अतिसार यानी दस्त वाले रोगी में। "
                   "कौन-से दो काढ़े, यह यहाँ नहीं कहा गया; उनमें से कौन पिया जाए, यह अगले श्लोक में है।"),
    "hook": "खुजली, गाँठ, रंग, बेचैनी, मन्द अग्नि; दस्त में पहले कहे दो काढ़े।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "Which of these is named in line 1 of verse 6?",
            ("Itching (कण्डू)", "कण्डू, itching, is the first word of the line."),
            [("Fainting (मूर्च्छा)", "Fainting is not named in verse 6."),
             ("Cough (कास)", "Cough is not named in verse 6."),
             ("Vomiting (छर्दि)", "Vomiting is not named in verse 6.")],
            "Line 1: kaṇḍū, gaṇḍa, vaivarṇya, arati, vahni-mārdava.",
            "कण्डू = खुजली."),
        match(1, "Match each word of line 1 to its meaning.",
              [["कण्डू", "itching"], ["गण्ड", "lump, swelling"],
               ["वैवर्ण्य", "discolouration"], ["अरति", "restlessness"]],
              "Four of the five effects of line 1.",
              "कण्डू = itching; गण्ड = lump; वैवर्ण्य = discolouration; अरति = restlessness."),
        order(2, "Put the effects of line 1 in the order of the verse.",
              ["कण्डू", "गण्ड", "वैवर्ण्य", "अरति", "वह्निमार्दव"],
              "Itching, lumps, discolouration, restlessness, softness of the fire.",
              "कण्डू · गण्ड · वैवर्ण्य · अरति · वह्निमार्दव.",
              role="extend",
              teaches="Line 1 ends the list of effects with softness of the fire (वह्निमार्दव)."),
        mcq("discriminate", 3, "What does वह्निमार्दव literally mean in verse 6?",
            ("Softness of the fire (vahni = agni)",
             "वह्नि is a name of the fire; मार्दव is softness."),
            [("Burning heat of the body", "That would be दाह; मार्दव is softness."),
             ("Softness of the skin", "The skin is not named; वह्नि is fire."),
             ("Hardness of the stool", "Neither stool nor hardness is named.")],
            "Literal: softness of the fire. Weak digestion is a probable sense the verse does not state.",
            "वह्नि = अग्नि; मार्दव = मृदुता."),
        mcq("apply", 4, "For a patient with atisāra (diarrhoea), what does line 2 point to?",
            ("The pair of decoctions prescribed earlier",
             "क्वाथद्वयं प्राग्विहितम्: the two decoctions prescribed before."),
            [("A new pair of oils named here", "The line names decoctions, and earlier ones."),
             ("A strong purgation at once", "Purgation comes in verse 7, with the right time known."),
             ("A cold milk basti", "No milk basti is named in verse 6.")],
            "Line 2 refers back to two decoctions; it does not list their drugs.",
            "क्वाथद्वय = दो काढ़े; प्राग्विहित = पहले बताए गए."),
        mcq("transfer", 5, "Like प्राक् + विहितम् → प्राग्विहितम्, how is वाक् + दानम् (word-giving) joined?",
            ("वाग्दानम्", "Final क् becomes ग् before the voiced द."),
            [("वाक्दानम्", "क् does not stay unvoiced before a voiced consonant."),
             ("वाङ्दानम्", "क् turns into the nasal only before a nasal."),
             ("वाचदानम्", "The final consonant does not return to च here.")],
            "प्राक् + विहित → प्राग्विहित; वाक् + दान → वाग्दान.",
            "Final unvoiced stop + voiced consonant → voiced stop (क् → ग्).",
            teaches="A final क् becomes ग् before a voiced consonant (प्राग्विहित, वाग्दान)."),
    ],
}

# ---------------------------------------------------------------- unit 7
AUTHORED["7"] = {
    "title": "उष्णस्य तस्मादेकस्य",
    "question": "Which of the two decoctions is to be drunk, and which further measures does verse 7 list?",
    "rule": ("Therefore, in that case, drinking of one, the hot one, is recommended. Also "
             "phalavartis (suppositories), likewise sweatings (sveda), and, having known the "
             "time, purgation (virecana)."),
    "limits": ("Whether hot means temperature or potency is not stated. Which time is meant for "
               "purgation is not stated. The verse gives no doses and no drugs for the "
               "suppositories."),
    "explain_hi": ("पिछले श्लोक के दो काढ़ों में से यहाँ चुनाव होता है: इसलिए वहाँ एक, उष्ण वाले का पान प्रशंसित है। "
                   "उष्ण से तापमान का अर्थ है या वीर्य का, यह नहीं कहा गया। फिर उपायों की सूची है: फलवर्ति (गुदा में रखी "
                   "जाने वाली बत्ती, शब्दार्थ ‘फल-बत्ती’), स्वेद, और समय जानकर विरेचन। "
                   "कौन-सा समय, यह श्लोक नहीं बताता।"),
    "hook": "दो में से गर्म काढ़ा पियो; फिर फलवर्ति, स्वेद, समय देखकर विरेचन।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "Which one of the pair of decoctions does verse 7 recommend drinking?",
            ("The hot one (उष्ण)", "उष्णस्य ... एकस्य पानं प्रशस्यते: drinking of the one, the hot one."),
            [("The cold one", "The verse says उष्ण, hot."),
             ("Both, one after the other", "The verse says one (एक), not both."),
             ("Neither; only a basti", "Drinking (पान) is recommended.")],
            "Of the two decoctions, the hot one is chosen.",
            "उष्णस्य एकस्य पानम् = गर्म वाले एक का पान."),
        order(1, "Put the measures of verse 7 in the order of the verse.",
              ["पानम्", "फलवर्तयः", "स्वेदाः", "विरेचनम्"],
              "Drinking (of the hot decoction), suppositories, sweatings, then purgation.",
              "पान · फलवर्ति · स्वेद · विरेचन."),
        match(2, "Match each word of verse 7 to its meaning.",
              [["पानम्", "drinking"], ["प्रशस्यते", "is recommended"],
               ["फलवर्ति", "suppository (fruit-wick)"], ["स्वेद", "sweating, fomentation"],
               ["विरेचन", "purgation"]],
              "One recommended drink and three more measures.",
              "पान = drinking; प्रशस्यते = is recommended; फलवर्ति = suppository; स्वेद = sweating; विरेचन = purgation.",
              role="extend",
              teaches="Besides the hot decoction, verse 7 names phalavarti, sveda and virecana."),
        mcq("discriminate", 3, "Which split of फलवर्त्यस्तथा is right?",
            ("फलवर्त्यः + तथा",
             "A visarga before त becomes स्: -यः + तथा → -यस्तथा."),
            [("फलवर्ति + अस्तथा", "अस्तथा is not a word."),
             ("फलवर्त्य + स्तथा", "स्तथा is not a word; the स् is the changed visarga."),
             ("फलवर्त्यः + स्तथा", "The स् is not an extra letter; it replaces the visarga.")],
            "फलवर्त्यः (suppositories, f. nom. pl.) + तथा (likewise).",
            "ः + त → स्त: फलवर्त्यः + तथा → फलवर्त्यस्तथा."),
        mcq("apply", 4, "When does verse 7 say purgation (विरेचन) is given?",
            ("Having known the time", "कालं ज्ञात्वा विरेचनम्: purgation, having known the time."),
            [("At once, before anything else", "The verse makes it wait on knowing the time."),
             ("Only at night", "Night is not named."),
             ("After seven days of fasting", "No fasting or number of days is named.")],
            "The verse asks the physician to know the time; it does not say which time.",
            "कालं ज्ञात्वा = समय जानकर."),
        mcq("transfer", 5, "Like ज्ञात्वा (having known, √ज्ञा), which form means having heard (√श्रु)?",
            ("श्रुत्वा", "An absolutive of a root without prefix ends in -त्वा."),
            [("श्रुतम्", "This is the past participle, heard."),
             ("शृणोति", "This is the present, hears."),
             ("श्रोतुम्", "This is the infinitive, to hear.")],
            "ज्ञात्वा and श्रुत्वा are absolutives: having done the action first.",
            "Root without prefix + -त्वा = having ...ed (with a prefix: -य).",
            teaches="An unprefixed root takes -त्वा for having ...ed (ज्ञात्वा, श्रुत्वा); a prefixed root takes -य (संक्षोभ्य)."),
    ],
}

# ---------------------------------------------------------------- unit 8
AUTHORED["8"] = {
    "title": "बिल्वमूल त्रिवृद्दारु",
    "question": "Which drugs and liquids does the basti of verse 8 contain?",
    "rule": ("A basti having bilva root, trivṛt, dāru, yava, kola and kulattha, and having surā "
             "and the others and urine. The rest of line 2 is damaged."),
    "limits": ("सप्राकूपेष्यः is damaged; 'should bring it' (तम् आनयेत्) is only conjectural. dāru "
               "(probably devadāru) and kola (probably jujube) are probable identifications. "
               "Whether बिल्वमूल belongs inside the compound is unfixed. Confidence low."),
    "explain_hi": ("यह एक बस्ति का द्रव्य-योग है: बिल्व यानी बेल की जड़, त्रिवृत् यानी निशोथ, दारु (सम्भवतः देवदारु), "
                   "यव, कोल (सम्भवतः बेर) और कुलत्थ यानी कुलथी वाली। दूसरी पंक्ति में बस्ति में सुरा आदि और मूत्र भी है। "
                   "उसके बाद का शब्द ‘सप्राकूपेष्यः’ छपाई में बिगड़ा है, इसलिए ‘उसे लाए’ केवल अनुमानित पाठ है और उस पर "
                   "कोई प्रश्न नहीं बना। ‘-वान्’ का अर्थ है ‘वाला’, जो बस्ति का विशेषण है।"),
    "hook": "बेल-जड़, निशोथ, दारु, यव, बेर, कुलथी; साथ में सुरा आदि और मूत्र।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "Which of these drugs is named in verse 8?",
            ("Kulattha (horse gram)", "कुलत्थ is the last drug of line 1."),
            [("Pippalī (long pepper)", "Pippalī is named in verse 11, not here."),
             ("Vacā (sweet flag)", "Vacā is named in verse 12, not here."),
             ("Citraka (leadwort)", "Citraka is named in verse 13, not here.")],
            "Line 1: bilva root, trivṛt, dāru, yava, kola, kulattha.",
            "कुलत्थ = कुलथी (horse gram, standard)."),
        match(1, "Match each drug of verse 8 to its identification.",
              [["बिल्व", "bael (Aegle marmelos)"], ["त्रिवृत्", "turpeth"],
               ["यव", "barley"], ["कुलत्थ", "horse gram"]],
              "These four identifications are marked standard in the data; dāru and kola are only probable.",
              "बिल्व = bael; त्रिवृत् = turpeth (निशोथ); यव = barley; कुलत्थ = horse gram."),
        order(2, "Put these drugs in the order of verse 8.",
              ["बिल्वमूल", "त्रिवृत्", "दारु", "यव", "कोल", "कुलत्थ"],
              "Bilva root first, then trivṛt, dāru, yava, kola, kulattha.",
              "बिल्वमूल · त्रिवृत् · दारु · यव · कोल · कुलत्थ.",
              role="extend",
              teaches="Line 1 lists six drugs from bilva root to kulattha, all qualifying the basti (-वान्, having)."),
        mcq("discriminate", 3, "What does the ending -वान् in कुलत्थवान् and मूत्रवान् mean?",
            ("Having, containing", "-वान् (matup) makes having X: the basti having these drugs."),
            [("Without, free from", "Without would need a word like विना or a negative."),
             ("Made from the root of", "Root is मूल, a separate member of the list."),
             ("Given after", "No sequence in time is expressed by -वान्.")],
            "-वान् qualifies the basti: it has the drugs, surā and the rest, and urine.",
            "X-वान् = X वाला (having X)."),
        mcq("apply", 4, "Which liquids does line 2 put into the basti?",
            ("Surā and the others, and urine",
             "सुरादिमूत्रवान्: having surā and the others, and urine."),
            [("Milk and ghee", "Neither milk nor ghee is named."),
             ("Honey and water", "Neither honey nor water is named."),
             ("Oil alone", "Oil is not named in verse 8.")],
            "सुरा-आदि = surā and the others (a fermented liquor and the rest); मूत्र = urine.",
            "सुरादि + मूत्र: द्रव भाग."),
        mcq("transfer", 5, "Like त्रिवृत् + दारु → त्रिवृद्दारु, how is मरुत् + गणः (the troop of winds) joined?",
            ("मरुद्गणः", "Final त् becomes द् before the voiced ग."),
            [("मरुत्गणः", "त् does not stay unvoiced before a voiced consonant."),
             ("मरुन्गणः", "त् turns into न् only before a nasal."),
             ("मरुग्गणः", "त् does not take the place of the next consonant before ग.")],
            "त्रिवृत् + दारु → त्रिवृद्दारु; मरुत् + गण → मरुद्गण.",
            "Final त् + voiced consonant → द्.",
            teaches="A final त् becomes द् before a voiced consonant (त्रिवृद्दारु, मरुद्गण)."),
    ],
}

# ---------------------------------------------------------------- unit 9
AUTHORED["9"] = {
    "title": "संशेषामे निरूहेण मृदुना",
    "question": "What does verse 9 say a mild nirūha, given with āma remaining, leads to?",
    "rule": ("With āma (undigested matter) remaining, by a mild nirūha (decoction enema), stirred "
             "by the doṣas, it stupefies the wind, obstructs the path and harms the fire (agni). "
             "The list of effects continues in verse 10."),
    "limits": ("The reading saṃśeṣa-āma is not secure, and the subject (taken as the basti) is not "
               "named; the remaining āma is a possible subject. Which path is meant is not stated. "
               "Confidence low."),
    "explain_hi": ("यहाँ नया प्रसंग शुरू होता है: आम (अपक्व, बिना पचा पदार्थ) शेष रहते हुए मृदु निरूह (काढ़े की बस्ति) "
                   "दिया जाए। दोषों से प्रेरित होकर वह वायु को मूर्च्छित (स्तब्ध) करता है, मार्ग को रोकता है और अग्नि को "
                   "हानि पहुँचाता है। कर्ता का नाम नहीं है; बस्ति माना गया है, पर शेष आम भी हो सकता है। "
                   "‘संशेषामे’ का पाठ भी पक्का नहीं, इसलिए प्रश्न केवल तीन क्रियाओं और स्पष्ट शब्दों पर हैं।"),
    "hook": "आम बचा हो और निरूह मृदु: वायु स्तब्ध, मार्ग बन्द, अग्नि को हानि।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "What kind of nirūha does verse 9 speak of?",
            ("A mild one (मृदुना)", "निरूहेण मृदुना: by a mild nirūha."),
            [("A sharp, strong one", "The verse says मृदु, mild."),
             ("A cold, thick one", "Cold and thick were faults in verse 4, not named here."),
             ("An oily one", "Oil is not named in verse 9.")],
            "The trouble arises from a mild nirūha given while āma remains.",
            "मृदु निरूह = हल्की काढ़े की बस्ति."),
        match(1, "Match what line 2 names to what happens to it.",
              [["अनिलम् (the wind)", "is stupefied"], ["मार्गम् (the path)", "is obstructed"],
               ["अग्निम् (the fire)", "is harmed"]],
              "Three objects, three verbs: मूर्च्छयति, रुणद्धि, हिनस्ति.",
              "वायु → मूर्च्छयति; मार्ग → रुणद्धि; अग्नि → हिनस्ति."),
        order(2, "Put these words of line 2 in the order of the verse.",
              ["मूर्च्छयति", "अनिलम्", "मार्गम्", "रुणद्धि", "अग्निम्", "हिनस्ति"],
              "Stupefies the wind; the path, obstructs; the fire, harms.",
              "मूर्च्छयति · अनिलम् · मार्गम् · रुणद्धि · अग्निम् · हिनस्ति.",
              role="extend",
              teaches="Line 2 has three verbs: मूर्च्छयति (stupefies), रुणद्धि (obstructs), हिनस्ति (harms)."),
        mcq("discriminate", 3, "Which split of दोषैरीरितः is right?",
            ("दोषैः + ईरितः",
             "A visarga after ऐ becomes र् before a vowel: दोषैः + ईरितः → दोषैरीरितः."),
            [("दोषै + रीरितः", "रीरितः is not a word; the र् is the changed visarga."),
             ("दोषः + ईरितः", "दोषः is singular; दोषैः, by the doṣas, is the plural."),
             ("दोषैर् + इरितः", "The vowel is long ई: ईरितः, stirred.")],
            "दोषैः (by the doṣas, inst. pl.) + ईरितः (stirred).",
            "ः after a vowel other than अ/आ + vowel → र्."),
        multi("apply", 4, "Which of these does line 2 of verse 9 state as effects?",
              [("The wind is stupefied", "Right: मूर्च्छयत्यनिलम्."),
               ("The path is obstructed", "Right: मार्गं रुणद्धि."),
               ("The fire is kindled", "The verse says the fire is harmed (हिनस्ति), not kindled."),
               ("The doṣa is expelled", "Expelling is not named; the doṣas stir it.")],
              [0, 1],
              "Line 2: stupefies the wind, obstructs the path, harms the fire.",
              "मूर्च्छयति · रुणद्धि · हिनस्ति."),
        mcq("transfer", 5, "Like रुणद्धि + अग्निम् → रुणद्ध्यग्निम्, how is यदि + अपि (even if) joined?",
            ("यद्यपि", "इ before a different vowel becomes य्."),
            [("यदीपि", "इ + अ does not give a long ई."),
             ("यदेपि", "इ + अ does not give ए."),
             ("यदिपि", "The vowels do not simply drop.")],
            "रुणद्धि + अग्निम् → रुणद्ध्यग्निम्; यदि + अपि → यद्यपि.",
            "इ/ई + different vowel → य् + vowel.",
            teaches="A final इ before a different vowel becomes य् (रुणद्ध्यग्निम्, मूर्च्छयत्यनिलम्, यद्यपि)."),
    ],
}

# ---------------------------------------------------------------- unit 10
AUTHORED["10"] = {
    "title": "गौरवक्लमहृच्छूल",
    "question": "Which further effects does verse 10 list, and with what is the patient treated?",
    "rule": ("Effects: heaviness, fatigue (klama), heart-pain, burning, bewilderment (saṃmoha) and "
             "twisting pain (veṣṭana). Then one should treat him with drying (rūkṣa), sweating "
             "(sveda) and digestive (pācana) means."),
    "limits": ("कुर्यात् has no object and may be a misprint; no question uses it. No noun stands "
               "with the instrumentals. rūkṣa-sveda may also be read as one item, dry fomentation. "
               "The treatment continues in verses 11-13. Confidence low."),
    "explain_hi": ("पहली पंक्ति श्लोक ९ की सूची को आगे बढ़ाती है: गौरव (भारीपन), क्लम (थकान), हृच्छूल (हृदय में शूल), "
                   "दाह (जलन), संमोह (मोह, घबराहट) और वेष्टन (ऐंठन)। दूसरी पंक्ति उपचार शुरू करती है: उसका रूक्ष, "
                   "स्वेद और पाचन से उपचार करे। ‘कुर्यात्’ बिना कर्म के है और अधिक लगता है; ‘रूक्ष-स्वेद’ को रूखा स्वेद "
                   "भी पढ़ा जा सकता है। उपचार अगले श्लोकों में चलता है।"),
    "hook": "भार, थकान, हृदय-शूल, जलन, मोह, ऐंठन; इलाज: रूक्ष, स्वेद, पाचन।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "With what does verse 10 say the patient should be treated?",
            ("Drying, sweating and digestive means",
             "रूक्षस्वेदपाचनैः: with drying, sweating and digestive (ones)."),
            [("Oiling, cooling and fasting", "These are not named; the verse says drying and sweating."),
             ("Bloodletting and cold baths", "Neither is named in verse 10."),
             ("Milk, ghee and honey", "No food or drink is named in verse 10.")],
            "The treatment of line 2: rūkṣa, sveda, pācana.",
            "रूक्ष · स्वेद · पाचन से उपचार."),
        order(1, "Put the effects of line 1 in the order of the verse.",
              ["गौरव", "क्लम", "हृच्छूल", "दाह", "संमोह", "वेष्टन"],
              "Heaviness, fatigue, heart-pain, burning, bewilderment, twisting pain.",
              "गौरव · क्लम · हृच्छूल · दाह · संमोह · वेष्टन."),
        match(2, "Match each effect of line 1 to its meaning.",
              [["क्लम", "fatigue"], ["दाह", "burning"], ["संमोह", "bewilderment"],
               ["वेष्टन", "twisting, cramping pain"]],
              "Four of the six effects of line 1.",
              "क्लम = fatigue; दाह = burning; संमोह = bewilderment; वेष्टन = twisting pain.",
              role="extend",
              teaches="Line 1 adds fatigue, burning, bewilderment and twisting pain to heaviness and heart-pain."),
        mcq("discriminate", 3, "Which split of हृच्छूल is right?",
            ("हृद् + शूल", "द् + श gives च्छ: हृद् + शूल → हृच्छूल."),
            [("हृत् + छूल", "छूल is not a word; the word is शूल, pain."),
             ("हृच् + शूल", "हृच् is not the stem; the heart is हृद्."),
             ("हृ + च्छूल", "These pieces are not words.")],
            "हृद् (heart) + शूल (pain) = heart-pain.",
            "त्/द् + श → च्छ."),
        mcq("apply", 4, "Which of these is NOT among the means of treatment named in verse 10?",
            ("Oiling (स्नेहन)", "Oiling is not named; the verse names drying, the opposite."),
            [("Drying (रूक्ष)", "Named: the first member of रूक्षस्वेदपाचनैः."),
             ("Sweating (स्वेद)", "Named: the second member."),
             ("Digestive means (पाचन)", "Named: the third member.")],
            "Named: rūkṣa, sveda, pācana. Oiling is not among them.",
            "रूक्ष · स्वेद · पाचन (स्नेहन नहीं)."),
        mcq("transfer", 5, "Like उपचरेत् (should treat), which form means one should go (√गम्, गच्छति)?",
            ("गच्छेत्", "A thematic verb takes -एत् in the 3 sg optative: गच्छ + एत्."),
            [("गच्छति", "This is the present, goes."),
             ("गतः", "This is the past participle, gone."),
             ("गन्तुम्", "This is the infinitive, to go.")],
            "उपचरेत् = upa-√car + -एत्, should treat; in the same way गच्छेत्, should go.",
            "3 sg optative of a thematic verb = stem + -एत् (should ...).",
            teaches="The 3 sg optative of a thematic verb ends in -एत् and gives should (उपचरेत्, गच्छेत्)."),
    ],
}

# ---------------------------------------------------------------- unit 11
AUTHORED["11"] = {
    "title": "पिप्पलीकत्तृणोशीर",
    "question": "Which medicated water does verse 11 prescribe, and what does it say the water does?",
    "rule": ("One should drink water with pippalī, kattṛṇa, uśīra, dāru and sūrvā, mixed with "
             "sauvarcala (black salt); it is kindling (dīpana) and cleansing in the heart."),
    "limits": ("kattṛṇa is a disputed grass; sūrvā is unidentified; dāru is probably devadāru. "
               "Whether bhṛta (filled) should read śṛta (boiled) is an open reviewer question; no "
               "question rests on it. No quantity is given."),
    "explain_hi": ("उपचार आगे चलता है: पिप्पली यानी पीपर, कत्तृण (एक घास, पहचान विवादित), उशीर यानी खस, दारु (सम्भवतः देवदारु) "
                   "और सूर्वा (अज्ञात पहचान) से भरा जल। उसे सौवर्चल यानी काले नमक से मिलाकर पिए। "
                   "यह जल दीपन (अग्नि को प्रदीप्त करने वाला) और हृदय में शोधन करने वाला कहा गया है। "
                   "मात्रा या बनाने की विधि नहीं दी गई।"),
    "hook": "पीपर, घास, खस, दारु, सूर्वा का जल; काला नमक डालो; अग्नि जगाए, हृदय शुद्ध करे।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "What is the water of verse 11 mixed with before drinking?",
            ("Sauvarcala (black salt)", "सौवर्चलोन्मिश्रम्: mixed with sauvarcala."),
            [("Honey", "Honey is not named in verse 11."),
             ("Curd-maṇḍa", "Curd-maṇḍa is named in verse 12, not here."),
             ("Ghee", "Ghee is not named in verse 11.")],
            "The water is mixed with sauvarcala, a salt (black salt, standard).",
            "सौवर्चल = काला नमक."),
        match(1, "Match each word of verse 11 to its meaning.",
              [["पिप्पली", "long pepper"], ["उशीर", "vetiver"],
               ["सौवर्चल", "black salt"], ["दीपन", "kindling the digestive fire"]],
              "Two drugs of line 1, the salt and one quality of the water.",
              "पिप्पली = long pepper; उशीर = vetiver; सौवर्चल = black salt; दीपन = kindling."),
        order(2, "Put the drugs of line 1 in the order of the verse.",
              ["पिप्पली", "कत्तृण", "उशीर", "दारु", "सूर्वा"],
              "Pippalī, kattṛṇa, uśīra, dāru, sūrvā, then -भृतं जलम्.",
              "पिप्पली · कत्तृण · उशीर · दारु · सूर्वा.",
              role="extend",
              teaches="Line 1 names five drugs in one compound ending in -भृतम्, qualifying the water (जलम्)."),
        mcq("discriminate", 3, "Which drug of verse 11 does the data call unidentified?",
            ("Sūrvā", "Sūrvā is unidentified; possibly a variant of mūrvā, itself disputed."),
            [("Pippalī", "Pippalī is long pepper, a standard identification."),
             ("Uśīra", "Uśīra is vetiver, a standard identification."),
             ("Sauvarcala", "Sauvarcala is black salt, a standard identification.")],
            "Standard: pippalī, uśīra, sauvarcala. Probable: dāru. Disputed: kattṛṇa. Unidentified: sūrvā.",
            "सूर्वा = अज्ञात पहचान."),
        mcq("apply", 4, "What does line 2 say the water does?",
            ("Kindles and cleanses in the heart",
             "दीपनं हृदिशोधनम्: kindling, and cleansing in the heart."),
            [("Cools and calms the body", "Cooling is not named."),
             ("Purges the bowels downward", "Purging is not named in verse 11."),
             ("Stops the flow of urine", "Urine is not named in verse 11.")],
            "Two qualities: dīpana and hṛdi-śodhana.",
            "दीपन + हृदिशोधन."),
        mcq("transfer", 5, "Like सौवर्चल + उन्मिश्रम् → सौवर्चलोन्मिश्रम्, how is गङ्गा + उदकम् (Ganges water) joined?",
            ("गङ्गोदकम्", "अ/आ + उ gives ओ."),
            [("गङ्गौदकम्", "औ comes from अ/आ + ओ/औ, not + उ."),
             ("गङ्गुदकम्", "The आ does not simply drop."),
             ("गङ्गावुदकम्", "No व् is inserted between आ and उ.")],
            "सौवर्चल + उन्मिश्र → सौवर्चलोन्मिश्र; कत्तृण + उशीर → कत्तृणोशीर; गङ्गा + उदक → गङ्गोदक.",
            "अ/आ + उ/ऊ → ओ.",
            teaches="अ or आ followed by उ becomes ओ (कत्तृणोशीर, सौवर्चलोन्मिश्र, गङ्गोदक)."),
    ],
}

# ---------------------------------------------------------------- unit 12
AUTHORED["12"] = {
    "title": "वचानागरशठ्यो वा",
    "question": "Which drugs does verse 12 give as an alternative, and with which liquors are they drunk?",
    "rule": ("Or vacā, nāgara and śaṭhī, mixed with curd-maṇḍa, should be drunk with prasannā "
             "(a clear liquor), or with ariṣṭa, or with āsava (fermented liquors)."),
    "limits": ("śaṭhī is disputed (Hedychium spicatum or Curcuma zedoaria); no question asks its "
               "identity. मूर्च्छिताः as mixed is a conjecture; prepared is possible. No quantity "
               "or time is given."),
    "explain_hi": ("‘वा’ से विकल्प आता है: वचा यानी बच, नागर यानी सोंठ और शठी (पहचान विवादित), दही के मण्ड से मिश्रित। "
                   "इन्हें प्रसन्ना (साफ़ मदिरा), अरिष्ट या आसव (दोनों किण्वित मदिराएँ) के साथ पिया जाए। "
                   "‘मूर्च्छित’ का अर्थ यहाँ ‘मिश्रित’ अनुमान है। मात्रा नहीं दी गई।"),
    "hook": "बच, सोंठ, शठी दही-मण्ड में; पियो प्रसन्ना, अरिष्ट या आसव से।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "Which three drugs does verse 12 name?",
            ("Vacā, nāgara and śaṭhī", "वचा-नागर-शठ्यः: vacā, nāgara, śaṭhī."),
            [("Pippalī, uśīra and dāru", "These are in verse 11."),
             ("Pathyā, palāśa and citraka", "These are in verse 13."),
             ("Trivṛt, yava and kola", "These are in verse 8.")],
            "Verse 12 opens with vacā (sweet flag), nāgara (dry ginger) and śaṭhī.",
            "वचा · नागर · शठी."),
        match(1, "Match each word of verse 12 to its meaning.",
              [["वचा", "sweet flag"], ["नागर", "dry ginger"],
               ["दधिमण्ड", "the watery or creamy part of curd"], ["प्रसन्ना", "a clear liquor"]],
              "Two drugs with standard identifications, the mixing liquid and one drink.",
              "वचा = sweet flag (बच); नागर = dry ginger (सोंठ); दधिमण्ड = curd-maṇḍa; प्रसन्ना = clear liquor."),
        order(2, "Put these liquids in the order of verse 12.",
              ["दधिमण्डेन", "प्रसन्नया", "अरिष्टेन", "आसवेन"],
              "Mixed with curd-maṇḍa; drunk with prasannā, or ariṣṭa, or āsava.",
              "दधिमण्ड · प्रसन्ना · अरिष्ट · आसव.",
              role="extend",
              teaches="The drugs are first mixed with curd-maṇḍa, then drunk with one of three liquors."),
        mcq("discriminate", 3, "Which split of स्युररिष्टेनासवेन is right?",
            ("स्युः + अरिष्टेन + आसवेन",
             "-उः before a vowel becomes -उर्; अ + आ gives आ."),
            [("स्यु + ररिष्टेन + आसवेन", "ररिष्टेन is not a word; the र् is the changed visarga."),
             ("स्युः + अरिष्टे + नासवेन", "नासवेन is not a word; the word is आसवेन."),
             ("स्युर् + अरिष्टेन + असवेन", "The vowel is long: आसव, not असव.")],
            "स्युः (should be) + अरिष्टेन (with ariṣṭa) + आसवेन (with āsava).",
            "-उः + vowel → -उर्; अ + आ → आ."),
        multi("apply", 4, "Which drinks does line 2 name for taking these drugs?",
              [("प्रसन्ना (a clear liquor)", "Right: प्रसन्नया."),
               ("अरिष्ट (a fermented liquor)", "Right: अरिष्टेन."),
               ("आसव (a fermented liquor)", "Right: आसवेन."),
               ("Milk", "Milk is not named in verse 12."),
               ("Hot water", "Water is not named in verse 12.")],
              [0, 1, 2],
              "Three alternatives joined by वा: prasannā, ariṣṭa, āsava.",
              "प्रसन्ना वा अरिष्ट वा आसव."),
        mcq("transfer", 5, "Like पेयाः (to be drunk, agreeing with the drugs), which phrase means the water is to be drunk (जलम्, n.)?",
            ("जलं पेयम्", "A gerundive agrees with its noun: neuter singular -अम्."),
            [("जलं पेयाः", "-आः is plural; जलम् is singular."),
             ("जलं पेया", "-आ is feminine; जलम् is neuter."),
             ("जलं पीतम्", "पीत is drunk (already), not to be drunk.")],
            "पेयाः agrees with the feminine plural drugs; पेयम् agrees with neuter जलम्.",
            "Gerundive (-य) = to be ...ed; it agrees with its noun.",
            teaches="A gerundive like पेय (to be drunk) agrees with its noun in gender and number (शठ्यः पेयाः, जलं पेयम्)."),
    ],
}

# ---------------------------------------------------------------- unit 13
AUTHORED["13"] = {
    "title": "पथ्यां पलाशं चित्रकं शठीम्",
    "question": "Which drugs does verse 13 grind, with what, and what else is drunk?",
    "rule": ("A damaged first word, then pathyā, palāśa, citraka and śaṭhī; having ground them and "
             "kuṣṭha with urine, one should drink; and the kindling (dīpana) kṣāras."),
    "limits": ("दारुत्रिकटुुकं is damaged and not translated; reading it as dāru + trikaṭuka is an "
               "open owner decision, so no question uses it. Whether the ground drugs or the "
               "kṣāras are drunk is not fully stated. Confidence low."),
    "explain_hi": ("पहला शब्द छपाई में बिगड़ा है (सम्भवतः दारु + त्रिकटुक, पर यह अपनाया नहीं गया)। फिर पथ्या यानी हरड़, "
                   "पलाश यानी ढाक, चित्रक यानी चीता और शठी (पहचान विवादित)। इन्हें और कुष्ठ यानी कूठ को मूत्र के साथ "
                   "पीसकर पिए; और दीपन क्षार भी। क्षार शब्द वैसा ही रखा गया है। प्रश्न केवल स्पष्ट शब्दों पर हैं।"),
    "hook": "हरड़, ढाक, चीता, शठी, कूठ: मूत्र में पीसो, पियो; दीपन क्षार भी।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "With what does verse 13 say the drugs are ground?",
            ("With urine (मूत्रेण)", "पिष्ट्वा ... मूत्रेण: having ground with urine."),
            [("With honey", "Honey is not named in verse 13."),
             ("With curd-maṇḍa", "Curd-maṇḍa belongs to verse 12."),
             ("With hot water", "Water is not named in verse 13.")],
            "मूत्रेण is instrumental: with urine.",
            "मूत्र के साथ पीसकर."),
        match(1, "Match each drug of verse 13 to its identification.",
              [["पथ्या", "chebulic myrobalan"], ["पलाश", "flame of the forest"],
               ["चित्रक", "leadwort"], ["कुष्ठ", "costus"]],
              "Four drugs with standard identifications in the data.",
              "पथ्या = हरड़; पलाश = ढाक; चित्रक = चीता; कुष्ठ = कूठ (costus)."),
        order(2, "Put these clear drug names of line 1 in the order of the verse.",
              ["पथ्याम्", "पलाशम्", "चित्रकम्", "शठीम्"],
              "After the damaged first word: pathyā, palāśa, citraka, śaṭhī.",
              "पथ्या · पलाश · चित्रक · शठी.",
              role="extend",
              teaches="Line 1 is a list of drug names in the accusative, objects of पिष्ट्वा (having ground)."),
        mcq("discriminate", 3, "What does पिष्ट्वा mean in verse 13?",
            ("Having ground", "Absolutive of √पिष्: having ground, before drinking."),
            [("Ground (as an adjective)", "That would be पिष्ट, a past participle."),
             ("To grind", "That would be an infinitive."),
             ("He grinds", "That would be a present verb.")],
            "पिष्ट्वा ... पिबेत्: having ground, one should drink.",
            "-त्वा = having ...ed."),
        mcq("apply", 4, "Besides the ground drugs, what else does line 2 say one should drink?",
            ("The kindling (dīpana) kṣāras", "पिबेत् क्षारांश्च दीपनान्: and the kindling kṣāras."),
            [("Fresh milk with sugar", "Neither is named in verse 13."),
             ("The hot decoction of verse 7", "That decoction is not mentioned again here."),
             ("Clear liquor (प्रसन्ना)", "Prasannā is named in verse 12, not here.")],
            "क्षारान् दीपनान्: kṣāras that kindle. kṣāra is kept as a term.",
            "क्षार (दीपन) भी पिए."),
        mcq("transfer", 5, "Like क्षारान् + च → क्षारांश्च, how is तान् + च (and them) joined?",
            ("तांश्च", "-न् before च becomes anusvara + श्: तांश्च."),
            [("तान्च", "न् does not stay unchanged before च here."),
             ("ताञ्च", "The rule inserts श्, not only a palatal nasal."),
             ("तानच", "No vowel is added after न्.")],
            "क्षारान् च → क्षारांश्च; तान् च → तांश्च.",
            "-न् + च/छ → -ंश्च.",
            teaches="A final न् before च becomes anusvara + श् (क्षारांश्च, तांश्च)."),
    ],
}

# ---------------------------------------------------------------- unit 14
AUTHORED["14"] = {
    "title": "बस्तिमस्य विदध्याच्च",
    "question": "Which basti does verse 14 prescribe, and in which patients is a basti of little potency applied?",
    "rule": ("One should administer to him a basti of the daśamūla (ten roots) with urine. Line 2 "
             "begins: applied with little potency, in one rich in doṣa, in a dry one, or in one "
             "with a harsh abode (āśaya)."),
    "limits": ("The ten roots are not listed. Line 2 starts a sentence whose verb (रुन्ध्यात्) is in "
               "verse 15. Harsh abode is kept literal. The print drops the avagraha in "
               "युक्तोल्पवीर्यो."),
    "explain_hi": ("पहली पंक्ति उपचार का अन्तिम अंग देती है: उसके लिए मूत्र सहित दशमूल (दस जड़ों का समूह) की बस्ति दे। "
                   "दस जड़ों के नाम यहाँ नहीं हैं। दूसरी पंक्ति नया वाक्य शुरू करती है: अल्प वीर्य (कम शक्ति) वाली बस्ति, "
                   "जब दोषों से भरे, रूक्ष या क्रूर आशय वाले रोगी में दी जाए; उसका परिणाम श्लोक १५ में ‘रुन्ध्यात्’ से आता है।"),
    "hook": "मूत्र के साथ दशमूल बस्ति; कम शक्ति की बस्ति, दोष-भरे, रूखे, क्रूर आशय वाले में ...",
    "core": True,
    "questions": [
        mcq("pretest", 0, "Which basti does line 1 of verse 14 prescribe?",
            ("A daśamūla basti with urine", "समूत्रं दाशमूलिकम्: of the ten roots, with urine."),
            [("An oil basti with milk", "Neither oil nor milk is named."),
             ("A basti of honey and salt", "Neither honey nor salt is named here."),
             ("A cold basti of curd", "Cold was a fault in verse 4; curd is not named.")],
            "दाशमूलिक = of the daśamūla (group of ten roots); स-मूत्र = with urine.",
            "मूत्र सहित दशमूल की बस्ति."),
        match(1, "Match each word of verse 14 to its meaning.",
              [["समूत्रम्", "with urine"], ["दाशमूलिकम्", "of the ten roots"],
               ["अल्पवीर्यः", "of little potency"], ["दोषाढ्ये", "in one rich in doṣa"]],
              "Two words for the prescribed basti, two for the faulty case of line 2.",
              "समूत्र = with urine; दाशमूलिक = of daśamūla; अल्पवीर्य = of little potency; दोषाढ्य = rich in doṣa."),
        order(2, "Put these words of line 2 in the order of the verse.",
              ["युक्तः", "अल्पवीर्यः", "दोषाढ्ये", "रूक्षे", "क्रूराशये"],
              "Applied, of little potency; in one rich in doṣa, in a dry one, in one with a harsh abode.",
              "युक्तः · अल्पवीर्यः · दोषाढ्ये · रूक्षे · क्रूराशये.",
              role="extend",
              teaches="Line 2 names a weak basti and three kinds of patient (locatives); its verb comes in verse 15."),
        mcq("discriminate", 3, "Which split of क्रूराशयेऽथवा is right?",
            ("क्रूराशये + अथवा", "ए + अ keeps ए and the अ drops, marked by the avagraha (ऽ)."),
            [("क्रूराशय + एथवा", "एथवा is not a word; the word is अथवा, or."),
             ("क्रूराशयः + अथवा", "-अः + अ would give -ओऽ, not -एऽ."),
             ("क्रूराशये + थवा", "थवा is not a word; the अ of अथवा is hidden in ऽ.")],
            "क्रूराशये (in one with a harsh abode, loc.) + अथवा (or).",
            "-ए + अ → -एऽ (avagraha)."),
        mcq("apply", 4, "Which patient is NOT among those named in line 2 of verse 14?",
            ("A well-oiled patient", "The verse names a dry (रूक्ष) one, not an oiled one."),
            [("One rich in doṣa", "Named: दोषाढ्ये."),
             ("A dry one", "Named: रूक्षे."),
             ("One with a harsh abode", "Named: क्रूराशये.")],
            "Three patients: rich in doṣa, dry, with a harsh abode (āśaya).",
            "दोषाढ्य · रूक्ष · क्रूराशय."),
        mcq("transfer", 5, "By the pattern of समूत्रम् (with urine), what does सक्षीरम् mean (क्षीर, milk)?",
            ("With milk", "स- + noun forms a bahuvrīhi: having X, with X."),
            [("Without milk", "Without would be निः- or अ-, not स-."),
             ("Milk alone", "स- adds a companion; it does not mean only."),
             ("For the sake of milk", "No purpose is expressed by स-.")],
            "स-मूत्र = with urine; स-क्षीर = with milk.",
            "स- + X = with X (bahuvrīhi).",
            teaches="The prefix स- makes a bahuvrīhi meaning with X (समूत्र, सक्षीर)."),
    ],
}

NOTES_HI = {
    "1": ("विश्वास: उच्च। अध्याय का आरम्भ-सूत्र। संधि जाँची: अथातो = अथ + अतः (अ + अ → आ; -अः + घोष व्यंजन → -ओ); "
          "बस्तिव्यापत्तिसिद्धिं = बस्ति-व्यापत्ति-सिद्धिम् (स्त्री. द्वितीया एकवचन, तत्पुरुष)। ‘सिद्धि’ = सफलता; "
          "‘सफल उपचार’ डेटा की व्याख्यात्मक व्याख्या है। पाठभेद या टेक्स्ट-फ़्लैग नहीं।"),
    "2": ("विश्वास: निम्न। दोनों पंक्तियाँ बिना क्रिया की सूची हैं; कारण श्लोक ३ में। ‘वाहन’, ‘अंगरुचि’ और ‘ध्मा’ अस्पष्ट हैं "
          "(सम्भव अनुमान: प्रवाहण, अरुचि, आध्मान/ध्मान; कोई अपनाया नहीं गया), इन पर प्रश्न नहीं। टेक्स्ट-फ़्लैग: छपा ‘हत्पीडा’ "
          "सम्भवतः ‘हृत्पीडा’ (ऋ-मात्रा छूटी)। संधि जाँची: शिरोरुग् = शिरः + रुज् (-अः → -ओ; ज् → ग्); "
          "वाहनोर्ध्वगाः = वाहन + ऊर्ध्वगाः (अ + ऊ → ओ)। कौन-सी छह अयोग की और कौन-सी अतियोग की, यह पाठ में नहीं।"),
    "3": ("विश्वास: मध्यम। संधि जाँची: षट्षडापदः = षट् + षट् + आपदः (ट् → ड् स्वर से पहले); अयोगादतियोगाच्च = अयोगात् + "
          "अतियोगात् + च (त् → द्; त् + च → च्च)। टेक्स्ट-फ़्लैग: ‘अंस्निग्ध’ में अनुस्वार अतिरिक्त, ‘अस्निग्ध’ होना चाहिए। "
          "निषेध ‘अ-’ दोनों (स्निग्ध, स्विन्न) पर माना गया; ‘स्निग्ध नहीं पर स्विन्न’ भी व्याकरण से सम्भव, इसलिए प्रश्न केवल "
          "‘गुरुकोष्ठ’ पर। पंक्ति २ का वाक्य श्लोक ५ (करोति) तक चलता है।"),
    "4": ("विश्वास: मध्यम। टेक्स्ट-फ़्लैग: छपा ‘शीतोल्प’ में अवग्रह छूटा है: शीतः + अल्प → शीतोऽल्प (वैसा ही श्लोक १४ में "
          "‘युक्तोल्प’)। ‘अल्प’ चारों (स्नेह, लवण, द्रव्य, मात्रा) पर लगे या नहीं, यह समास से तय नहीं। ‘दुर्बलत्व’ किसका है, "
          "नहीं कहा गया। संधि जाँची: घनोऽपि = घनः + अपि; दुर्बलत्वादनिर्हरन् = दुर्बलत्वात् + अनिर्हरन् (त् → द्)। "
          "क्रिया श्लोक ५ में।"),
    "5": ("विश्वास: मध्यम। क्रिया ‘करोति’ श्लोक ३-४ के वाक्य को पूरा करती है। ‘बस्ति’ यहाँ अंग (मूत्राशय/निचला पेट) है, "
          "एनिमा नहीं। ‘वात’ को अधोवायु पढ़ा गया; दोष का अर्थ बाहर नहीं किया गया। संधि जाँची: विण्मूत्र = विट् + मूत्र "
          "(ट् → ण् अनुनासिक से पहले); हृल्लेपं = हृद् + लेपम् (द् + ल → ल्ल); रुजानाहं = रुजा + आनाहम्। "
          "आनाह (मानक), हृल्लेप (सम्भावित), श्वयथु (मानक)।"),
    "6": ("विश्वास: मध्यम। टेक्स्ट-फ़्लैग: ‘वन्हि’ = वह्नि (वर्तनी); ‘काथद्वयं’ सम्भवतः ‘क्वाथद्वयं’ (व छूटा)। "
          "खुला प्रश्न (05.06.11): ‘मध्यदोषे’ को ‘मध्यम दोष में’ पढ़ें या बहुव्रीहि ‘मध्यम दोष वाले में’, यह स्वामी को तय करना है; "
          "इस पर कोई प्रश्न नहीं। दोनों काढ़े पहचाने नहीं गए। संधि जाँची: प्राग्विहितं = प्राक् + विहितम् (क् → ग्); "
          "मध्यदोषेऽतिसारिणि = मध्यदोषे + अतिसारिणि। ‘वह्निमार्दव’ से मन्द पाचन सम्भावित है, कहा नहीं गया।"),
    "7": ("विश्वास: मध्यम। श्लोक ६ के दो काढ़ों में से ‘उष्ण’ एक चुना गया; ‘तस्मात्’ = इसलिए (विकल्प: ‘उसमें से’)। "
          "उष्णता ताप की है या वीर्य की, नहीं कहा गया। संधि जाँची: तस्मादेकस्य = तस्मात् + एकस्य (त् → द्); "
          "फलवर्त्यस्तथा = फलवर्त्यः + तथा (ः → स् त से पहले)। ‘फलवर्ति’ = औषधीय बत्ती (मानक अर्थ)। समय कौन-सा, नहीं कहा गया।"),
    "8": ("विश्वास: निम्न। ‘सप्राकूपेष्यः’ छपाई में बिगड़ा/अबोध्य है; अर्ध-पंक्ति में १७ अक्षर (१६ अपेक्षित), इसलिए "
          "‘तम् आनयेत्’ भी अनुमानित है; इस पर प्रश्न नहीं। खुला प्रश्न (05.06.15): ‘उसे लाए’ में ‘तम्’ पुल्लिंग है "
          "(‘उसको/उस’), अंग्रेज़ी ‘it’ पर स्वामी का निर्णय शेष। ‘बिल्वमूल’ के बाद छपा स्थान अस्पष्ट। संधि जाँची: त्रिवृद्दारु = "
          "त्रिवृत् + दारु (त् → द्); सुरादि = सुरा + आदि। दारु = देवदारु (सम्भावित), कोल = बेर (सम्भावित), शेष मानक।"),
    "9": ("विश्वास: निम्न। ‘संशेषामे’ = संशेष-आमे (शेष आम में) का पाठ पक्का नहीं। ‘ईरितः’ पुल्लिंग प्रथमा है पर कर्ता का नाम नहीं; "
          "बस्ति माना गया। समीक्षक का सुझाव: यदि छपाई में ओ की जगह ए हो (‘संशेषामो’) तो शेष आम ही कर्ता होगा; अपनाया नहीं गया। "
          "संधि जाँची: दोषैरीरितः = दोषैः + ईरितः (ः → र्); मूर्च्छयत्यनिलं = मूर्च्छयति + अनिलम्; रुणद्ध्यग्निं = रुणद्धि + "
          "अग्निम् (इ → य्)। ‘मूर्च्छयति’ का शब्दार्थ ‘मूर्च्छित करना’, ‘गाढ़ा करना’ भी।"),
    "10": ("विश्वास: निम्न। ‘कुर्यात्’ बिना कर्म के है और ‘उपचरेत्’ के साथ अधिक लगता है (सम्भवतः छपाई-दोष, सुधारा नहीं गया)। "
           "‘रूक्ष-स्वेद-पाचन’ को ‘रूक्ष स्वेद (सूखा सेंक) + पाचन’ भी पढ़ा जा सकता है। संधि जाँची: हृच्छूल = हृद् + शूल "
           "(द् + श → च्छ); कुर्यादुपचरेत्तं = कुर्यात् + उपचरेत् + तम्। क्लम, संमोह (मानक), वेष्टन (सम्भावित)।"),
    "11": ("विश्वास: मध्यम। खुला प्रश्न (05.06.20): ‘भृतं’ (भरा) की जगह ‘शृतं’ (उबाला) सम्भव; स्वामी का निर्णय शेष, इस पर प्रश्न नहीं। "
           "पहचान: पिप्पली, उशीर, सौवर्चल मानक; दारु सम्भावित; कत्तृण विवादित (शायद रोहिष घास); सूर्वा अज्ञात (शायद मूर्वा)। "
           "संधि जाँची: कत्तृणोशीर = कत्तृण + उशीर (अ + उ → ओ); सौवर्चलोन्मिश्रं = सौवर्चल + उन्मिश्रम्; "
           "पिबेत्सौवर्चल… = पिबेत् + सौवर्चल…। ‘हृदिशोधन’ का विस्तार पाठ में नहीं।"),
    "12": ("विश्वास: मध्यम। ‘मूर्च्छिताः’ = मिश्रित (अनुमान; ‘तैयार’ भी सम्भव)। शठी विवादित (कपूरकचरी या कचूर)। "
           "संधि जाँची: वचानागरशठ्यो वा = …शठ्यः + वा (-अः + घोष → -ओ); स्युररिष्टेनासवेन = स्युः + अरिष्टेन + आसवेन "
           "(-उः → -उर्; अ + आ → आ)। प्रसन्ना = साफ़ मदिरा (सुरा का एक भेद, मानक); अरिष्ट, आसव शब्द ही रखे गए।"),
    "13": ("विश्वास: निम्न। पहला शब्द ‘दारुत्रिकटुुकं’ बिगड़ा है (दोहरी उ-मात्रा)। टेक्स्ट-फ़्लैग: ‘दारुत्रिकटुकं’ (दारु + त्रिकटुक) "
           "से अर्ध-पंक्ति १६ अक्षर की होती है; खुला प्रश्न (05.06.24): इसे अपनाना स्वामी तय करेंगे; इस पर प्रश्न नहीं। "
           "क्या पिया जाए (पिसी औषधियाँ या क्षार) पूरी तरह स्पष्ट नहीं। संधि जाँची: क्षारांश्च = क्षारान् + च (न् + च → ंश्च); "
           "पिबेत्क्षारान् = पिबेत् + क्षारान्।"),
    "14": ("विश्वास: मध्यम। दशमूल के दस नाम पाठ में नहीं। टेक्स्ट-फ़्लैग: ‘युक्तोल्पवीर्यो’ में अवग्रह छूटा (युक्तः + अल्पवीर्यः → "
           "युक्तोऽल्पवीर्यो), जैसे श्लोक ४ में। पंक्ति २ का वाक्य श्लोक १५ की क्रिया ‘रुन्ध्यात्’ तक चलता है। संधि जाँची: "
           "बस्तिमस्य = बस्तिम् + अस्य; विदध्याच्च = विदध्यात् + च; क्रूराशयेऽथवा = क्रूराशये + अथवा (ए + अ → एऽ)। "
           "‘विदध्यात्’ = दे/प्रयोग करे (शब्दावली में खुला)।"),
}

AIDS = {
    "1": {
        "chunks": "अथातो | बस्तिव्यापत्तिसिद्धिं | व्याख्यास्यामः",
        "sandhi": "अ + अ → आ, और -अः घोष व्यंजन से पहले -ओ: अथ + अतः → अथातो।",
        "frame": "कब: अब (अथ) · क्यों: इसलिए (अतः) · क्या: बस्ति की गड़बड़ियों की सिद्धि · कौन: हम समझाएँगे।",
    },
    "2": {
        "diagram": {"groups": [{"label": "पंक्ति १", "items": ["विबन्ध", "गौरव", "आध्मान", "शिरोरुज्", "वाहन (अस्पष्ट)", "ऊर्ध्वग"]},
                               {"label": "पंक्ति २", "items": ["कुक्षिशूल", "अंगरुचि (अस्पष्ट)", "ध्मा (अस्पष्ट)", "हृत्पीडा", "कर्तन", "स्रव"]}]},
        "chunks": "विबन्धगौरवाध्मान | शिरोरुग्वाहनोर्ध्वगाः ‖ कुक्षिशूलाङ्गरुचिध्मा | हृत्पीडाकर्तनस्रवाः",
        "sandhi": "-अः घोष से पहले -ओ: शिरः + रुज् → शिरोरुज्; अ + ऊ → ओ: वाहन + ऊर्ध्वगाः → वाहनोर्ध्वगाः।",
        "anchors": "विबन्ध = रुकावट · गौरव = भारीपन · आध्मान = पेट फूलना · कुक्षि = पेट · कर्तन = काटने जैसी पीड़ा · स्रव = स्राव।",
    },
    "3": {
        "chain": {"steps": ["बस्ति का अयोग या अतियोग", "छह और छह आपत्तियाँ (श्लोक २ की सूची)"]},
        "chunks": "अयोगादतियोगाच्च | बस्तेः स्युः षट्षडापदः ‖ अस्निग्धस्विन्नदेहस्य | गुरुकोष्ठस्य योजितः",
        "sandhi": "ट् → ड् स्वर से पहले: षट् + आपदः → षडापदः; त् + च → च्च: अतियोगात् + च → अतियोगाच्च।",
        "contrast": "अयोग = बस्ति ठीक से न लगना · अतियोग = अधिक लगना; दोनों से छह-छह आपत्तियाँ।",
        "frame": "पंक्ति २ का रोगी: शरीर स्निग्ध नहीं, स्वेदित नहीं · कोष्ठ भारी · वाक्य श्लोक ५ तक।",
    },
    "4": {
        "chain": {"steps": ["ठंडी, कम स्नेह-लवण-द्रव्य-मात्रा वाली, या गाढ़ी बस्ति", "दोष को क्षुब्ध करती है",
                            "दुर्बलता से उसे बाहर नहीं निकालती", "(परिणाम श्लोक ५ में)"]},
        "chunks": "शीतोऽल्पस्नेहलवण | द्रव्यमात्रो घनोऽपि वा ‖ बस्तिः संक्षोभ्य तं दोषं | दुर्बलत्वादनिर्हरन्",
        "sandhi": "-अः + अ → -ओऽ: शीतः + अल्प → शीतोऽल्प; घनः + अपि → घनोऽपि।",
        "anchors": "शीत = ठंडा · घन = गाढ़ा · संक्षोभ्य = हिलाकर, क्षुब्ध करके · अनिर्हरन् = न निकालता हुआ।",
    },
    "5": {
        "diagram": {"groups": [{"label": "विबन्ध", "items": ["वात", "विट् (मल)", "मूत्र"]},
                               {"label": "पीड़ा और अन्य", "items": ["बस्ति-नाभि में पीड़ा", "आनाह", "हृल्लेप", "गुदा में श्वयथु"]}]},
        "chunks": "करोति वातविण्मूत्र | विबन्धमतिदारुणम् ‖ बस्तिनाभिरुजानाहं | हृल्लेपं श्वयथुं गुदे",
        "sandhi": "ट् → ण् अनुनासिक से पहले: विट् + मूत्र → विण्मूत्र; द् + ल → ल्ल: हृद् + लेप → हृल्लेप।",
        "anchors": "विट् = मल · आनाह = रुकावट से पेट फूलना · हृल्लेप = हृदय पर लेप-सा · श्वयथु = सूजन · गुद = गुदा।",
    },
    "6": {
        "chunks": "कण्डूगण्डानि वैवर्ण्य | मरतिं वह्निमार्दवम् ‖ क्वाथद्वयं प्राग्विहितं | मध्यदोषेऽतिसारिणि",
        "sandhi": "क् → ग् घोष से पहले: प्राक् + विहितम् → प्राग्विहितम्।",
        "anchors": "कण्डू = खुजली · गण्ड = गाँठ · वैवर्ण्य = रंग बिगड़ना · अरति = बेचैनी · वह्नि = अग्नि · मार्दव = मृदुता।",
        "frame": "पंक्ति १: लक्षण (क्रिया श्लोक ५ से) · पंक्ति २: अतिसार वाले में पहले कहे दो काढ़े।",
    },
    "7": {
        "chain": {"steps": ["दो काढ़ों में से उष्ण एक का पान", "फलवर्ति", "स्वेद", "समय जानकर विरेचन"]},
        "chunks": "उष्णस्य तस्मादेकस्य | तत्र पानं प्रशस्यते ‖ फलवर्त्यस्तथा स्वेदाः | कालं ज्ञात्वा विरेचनम्",
        "sandhi": "ः + त → स्त: फलवर्त्यः + तथा → फलवर्त्यस्तथा; त् → द् स्वर से पहले: तस्मात् + एकस्य → तस्मादेकस्य।",
        "anchors": "प्रशस्यते = प्रशंसित है · फलवर्ति = औषधीय बत्ती · स्वेद = सेंक · विरेचन = दस्त कराना।",
    },
    "8": {
        "diagram": {"groups": [{"label": "द्रव्य (पंक्ति १)", "items": ["बिल्वमूल", "त्रिवृत्", "दारु", "यव", "कोल", "कुलत्थ"]},
                               {"label": "द्रव (पंक्ति २)", "items": ["सुरा आदि", "मूत्र"]}]},
        "chunks": "बिल्वमूल त्रिवृद्दारु | यवकोलकुलत्थवान् ‖ सुरादिमूत्रवान्बस्तिः | सप्राकूपेष्यः (बिगड़ा) …",
        "sandhi": "त् → द् घोष से पहले: त्रिवृत् + दारु → त्रिवृद्दारु; आ + आ → आ: सुरा + आदि → सुरादि।",
        "pegs": "मेरा बनाया चित्र: एक बेल का पेड़ जिसकी जड़ के पास निशोथ की बेल, देवदारु का लट्ठा, जौ की बाली, बेर और कुलथी का ढेर रखा है।",
    },
    "9": {
        "chain": {"steps": ["आम शेष रहते मृदु निरूह", "दोषों से प्रेरित", "वायु मूर्च्छित", "मार्ग रुका", "अग्नि को हानि"]},
        "chunks": "संशेषामे निरूहेण | मृदुना दोषैरीरितः ‖ मूर्च्छयत्यनिलं मार्गं | रुणद्ध्यग्निं हिनस्ति च",
        "sandhi": "ः → र् स्वर से पहले (ऐ के बाद): दोषैः + ईरितः → दोषैरीरितः; इ → य्: रुणद्धि + अग्निम् → रुणद्ध्यग्निम्।",
        "anchors": "मृदु = हल्का · निरूह = काढ़े की बस्ति · ईरित = प्रेरित · अनिल = वायु · हिनस्ति = हानि करता है।",
    },
    "10": {
        "contrast": {"groups": [{"label": "लक्षण (पंक्ति १)", "items": ["गौरव", "क्लम", "हृच्छूल", "दाह", "संमोह", "वेष्टन"]},
                                {"label": "उपचार (पंक्ति २)", "items": ["रूक्ष", "स्वेद", "पाचन"]}]},
        "chunks": "गौरवक्लमहृच्छूल | दाहसंमोहवेष्टनम् ‖ ततः कुर्यादुपचरेत्तं | रूक्षस्वेदपाचनैः",
        "sandhi": "द् + श → च्छ: हृद् + शूल → हृच्छूल; त् + त: उपचरेत् + तम् → उपचरेत्तम्।",
        "anchors": "क्लम = थकान · दाह = जलन · संमोह = घबराहट, मोह · वेष्टन = ऐंठन · पाचन = पचाने वाला।",
    },
    "11": {
        "diagram": {"groups": [{"label": "जल में", "items": ["पिप्पली", "कत्तृण", "उशीर", "दारु", "सूर्वा"]},
                               {"label": "मिलाओ", "items": ["सौवर्चल"]},
                               {"label": "गुण", "items": ["दीपन", "हृदि-शोधन"]}]},
        "chunks": "पिप्पलीकत्तृणोशीर | दारुसूर्वाभृतं जलम् ‖ पिबेत्सौवर्चलोन्मिश्रं | दीपनं हृदिशोधनम्",
        "sandhi": "अ + उ → ओ: कत्तृण + उशीर → कत्तृणोशीर; सौवर्चल + उन्मिश्रम् → सौवर्चलोन्मिश्रम्।",
        "anchors": "पिप्पली = पीपर · उशीर = खस · सौवर्चल = काला नमक · दीपन = अग्नि जगाने वाला · शोधन = शुद्ध करना।",
    },
    "12": {
        "frame": "क्या: बच, सोंठ, शठी · किसमें मिलाकर: दही का मण्ड · किसके साथ पिएँ: प्रसन्ना, या अरिष्ट, या आसव।",
        "chunks": "वचानागरशठ्यो वा | दधिमण्डेन मूर्च्छिताः ‖ पेयाः प्रसन्नया वा स्यु | ररिष्टेनासवेन वा",
        "sandhi": "-उः स्वर से पहले -उर्: स्युः + अरिष्टेन → स्युररिष्टेन; अ + आ → आ: अरिष्टेन + आसवेन → अरिष्टेनासवेन।",
        "anchors": "वचा = बच · नागर = सोंठ · मण्ड = ऊपर का पतला भाग · प्रसन्ना = साफ़ मदिरा · पेय = पीने योग्य।",
    },
    "13": {
        "chunks": "दारुत्रिकटुुकं (बिगड़ा) पथ्यां | पलाशं चित्रकं शठीम् ‖ पिष्ट्वा कुष्ठं च मूत्रेण | पिबेत्क्षारांश्च दीपनान्",
        "sandhi": "न् + च → ंश्च: क्षारान् + च → क्षारांश्च।",
        "anchors": "पथ्या = हरड़ · पलाश = ढाक · चित्रक = चीता · कुष्ठ = कूठ · पिष्ट्वा = पीसकर · दीपन = अग्नि जगाने वाला।",
        "frame": "क्या पीसें: पथ्या, पलाश, चित्रक, शठी, कुष्ठ · किसमें: मूत्र · फिर: पिए · और: दीपन क्षार।",
    },
    "14": {
        "contrast": {"groups": [{"label": "पंक्ति १: दी जाने वाली बस्ति", "items": ["दाशमूलिक", "समूत्र"]},
                                {"label": "पंक्ति २: अल्पवीर्य बस्ति, इनमें", "items": ["दोषाढ्य", "रूक्ष", "क्रूराशय"]}]},
        "chunks": "बस्तिमस्य विदध्याच्च | समूत्रं दाशमूलिकम् ‖ युक्तोऽल्पवीर्यो दोषाढ्ये | रूक्षे क्रूराशयेऽथवा",
        "sandhi": "ए + अ → एऽ: क्रूराशये + अथवा → क्रूराशयेऽथवा; -अः + अ → -ओऽ: युक्तः + अल्प → युक्तोऽल्प।",
        "anchors": "समूत्र = मूत्र सहित · दाशमूलिक = दशमूल का · अल्पवीर्य = कम शक्ति वाला · आढ्य = भरा · आशय = स्थान।",
    },
}

IMAGE_SPECS = {
    ("2", "diagram"): {
        "file": "ka6-vyapad-list-2.svg",
        "alt": "Two columns of the mishap names in verse 2: line 1 vibandha, gaurava, adhmana, shiroruj, vahana (obscure), urdhvaga; line 2 kukshishula, angaruci (obscure), dhma (obscure), hritpida, kartana, srava",
        "type": "split",
        "title": "श्लोक २: बस्ति की आपत्तियाँ",
        "cols": [["पंक्ति १", ["विबन्ध", "गौरव", "आध्मान", "शिरोरुज्", "वाहन (अस्पष्ट)", "ऊर्ध्वग"]],
                 ["पंक्ति २", ["कुक्षिशूल", "अंगरुचि (अस्पष्ट)", "ध्मा (अस्पष्ट)", "हृत्पीडा", "कर्तन", "स्रव"]]],
    },
    ("3", "chain"): {
        "file": "ka6-ayoga-atiyoga-3.svg",
        "alt": "Flowchart: non-application and over-application of the basti both lead to six and six mishaps",
        "type": "mermaid",
        "code": ('flowchart TD\n  A["अयोग"] --> C["छह और छह आपत्तियाँ"]\n'
                 '  B["अतियोग"] --> C\n'),
    },
    ("4", "chain"): {
        "file": "ka6-durbala-basti-4.svg",
        "alt": "Chain of four steps: a cold, low-oil or thick basti; it agitates the dosha; through weakness it does not expel it; the result follows in verse 5",
        "type": "chain",
        "title": "श्लोक ४: दुर्बल बस्ति",
        "steps": ["ठंडी, कम स्नेह वाली या गाढ़ी बस्ति", "दोष को क्षुब्ध करती है",
                  "दुर्बलता से उसे नहीं निकालती", "परिणाम: श्लोक ५"],
    },
    ("5", "diagram"): {
        "file": "ka6-vibandha-effects-5.svg",
        "alt": "Mind map of verse 5: obstruction of wind, stool and urine; pain in bladder and navel; anaha; hrillepa; swelling in the anus",
        "type": "mermaid",
        "code": ('mindmap\n  अयोग का परिणाम\n    अत्यन्त विबन्ध\n      वायु\n      मल\n      मूत्र\n'
                 '    बस्ति और नाभि में पीड़ा\n    आनाह\n    हृल्लेप\n    गुदा में सूजन\n'),
    },
    ("8", "diagram"): {
        "file": "ka6-basti-dravya-8.svg",
        "alt": "Table of the six drugs of verse 8 with identifications: bilva root (bael), trivrit (turpeth), daru (probably deodar), yava (barley), kola (probably jujube), kulattha (horse gram)",
        "type": "table",
        "title": "श्लोक ८: बस्ति के द्रव्य",
        "heads": ["द्रव्य", "पहचान"],
        "rows": [["बिल्वमूल", "बेल की जड़"], ["त्रिवृत्", "निशोथ"], ["दारु", "सम्भवतः देवदारु"],
                 ["यव", "यव (एक अन्न)"], ["कोल", "सम्भवतः बेर"], ["कुलत्थ", "कुलथी"]],
    },
    ("9", "chain"): {
        "file": "ka6-ama-niruha-9.svg",
        "alt": "Flowchart: a mild nirūha with ama remaining, stirred by the doshas, stupefies the wind, obstructs the path and harms the fire",
        "type": "mermaid",
        "code": ('flowchart TD\n  A["आम शेष, मृदु निरूह"] --> B["दोषों से प्रेरित"]\n'
                 '  B --> C["वायु मूर्च्छित"]\n  B --> D["मार्ग रुका"]\n  B --> E["अग्नि को हानि"]\n'),
    },
    ("10", "contrast"): {
        "file": "ka6-lakshana-upachara-10.svg",
        "alt": "Two columns: six effects of verse 10 (heaviness, fatigue, heart-pain, burning, bewilderment, twisting pain) and three means of treatment (drying, sweating, digestives)",
        "type": "split",
        "title": "श्लोक १०: लक्षण और उपचार",
        "cols": [["लक्षण", ["गौरव", "क्लम", "हृच्छूल", "दाह", "संमोह", "वेष्टन"]],
                 ["उपचार", ["रूक्ष", "स्वेद", "पाचन"]]],
    },
    ("11", "diagram"): {
        "file": "ka6-dipana-jala-11.svg",
        "alt": "Flowchart: water with five drugs (pippali, kattrina, ushira, daru, surva), mixed with black salt, is kindling and cleansing in the heart",
        "type": "mermaid",
        "code": ('flowchart TD\n  A["पिप्पली, कत्तृण, उशीर"] --> C["जल"]\n  B["दारु, सूर्वा"] --> C\n'
                 '  C --> D["सौवर्चल मिलाकर पिए"]\n  D --> E["दीपन"]\n  D --> F["हृदय में शोधन"]\n'),
    },
}
