from helpers import mcq, match, order, fill, multi, accepts


AUTHORED = {}

# ---------------------------------------------------------------- unit 69
AUTHORED["69"] = {
    "title": "सक्तून्वा तिलमाषबिल्वशलाटुयुक्तान् पयसा पाययेत्",
    "question": "By unit 69, what mixture is given to drink, and with what liquid?",
    "rule": ("Or (वा) one should make her drink saktu (flour of roasted grain) combined with sesame (तिल), black gram "
             "(माष), bilva (bael) and śalāṭu (unripe fruit), with milk (पयसा). It appears to continue the līna treatment "
             "of units 67-68."),
    "limits": ("The grain of the saktu is not stated (barley is usual, not said). The list may be read as four items or with "
               "bilva-śalāṭu as one (unripe bilva fruit): no question counts or splits the items. The woman is not named. "
               "A prose line."),
    "explain_hi": ("यह गद्य-पंक्ति सम्भवतः इकाई ६७-६८ के लीन गर्भ के उपचार को आगे बढ़ाती है और एक और विकल्प (वा) देती है। "
                   "सक्तु यानी भुने अन्न का आटा, तिल, माष (उड़द), बिल्व (बेल) और शलाटु (कच्चा फल) से युक्त करके, "
                   "दूध के साथ (पयसा) पिलाए (पाययेत्)। "
                   "सक्तु किस अन्न का है, यह नहीं कहा गया; जौ सामान्य है, पर पंक्ति में नहीं। "
                   "‘बिल्वशलाटु’ को एक वस्तु भी पढ़ा जा सकता है (बेल का कच्चा फल); शब्दशः पाठ चार वस्तुओं का है। "
                   "‘पाययेत्’ √पा का प्रेरणार्थक विधिलिङ् है: पिलाए, स्वयं पीना नहीं।"),
    "hook": "या फिर: तिल, उड़द, बेल, कच्चे फल वाला सत्तू, दूध के साथ।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 69, with what liquid is the saktu given?",
            ("Milk (पयस्)", "पयसा पाययेत्: one should make her drink it with milk."),
            [("Curd (दधि)", "Curd is not named in unit 69; the liquid is पयसा, with milk."),
             ("Ghee (घृत)", "Ghee goes with the broths and soups of unit 68, not with this saktu."),
             ("Honey (मधु)", "Honey is not named in unit 69.")],
            "The saktu mixture is given with milk.",
            "पयसा = with milk (instrumental)."),
        order(1, "Put the words of unit 69 in the line's order.",
              ["सक्तून्वा", "तिलमाषबिल्वशलाटुयुक्तान्", "पयसा", "पाययेत्"],
              "Or saktu, combined with sesame, black gram, bilva and śalāṭu, with milk, one should make her drink.",
              "सक्तून्वा → तिलमाषबिल्वशलाटुयुक्तान् → पयसा → पाययेत्."),
        match(2, "Match each word of unit 69 to its meaning.",
              [["सक्तु", "flour of roasted grain"], ["तिल", "sesame"], ["माष", "black gram"],
               ["पयस्", "milk"], ["पाययेत्", "should make (her) drink"]],
              "Saktu with sesame and black gram (and bilva, śalāṭu), given with milk.",
              "सक्तु, तिल, माष, पयस्, पाययेत्.", role="extend",
              teaches="पाययेत् is the causative optative of √पा (drink): 'should make (her) drink', not 'should drink'."),
        mcq("discriminate", 3, "By unit 69, from which grain is the saktu made?",
            ("The line does not say", "The data: the grain is not stated; barley is usual but not said."),
            [("Barley, as the line states", "Barley is usual, but unit 69 names no grain for the saktu."),
             ("Rice, as the line states", "No rice is named in unit 69; the grain is not stated."),
             ("Black gram, as the line states", "Black gram (माष) is mixed in; it is not named as the saktu's grain.")],
            "Unit 69 names saktu but not its grain.",
            "Say only what the line states: सक्तून्, with no grain named."),
        multi("apply", 4, "Which of these are printed in the compound joined to सक्तून् in unit 69?",
              [("माष (black gram)", "Right: तिल-माष-बिल्व-शलाटु-युक्तान्."),
               ("मूलक (radish)", "Radish soup is in unit 68, not in this compound."),
               ("तिल (sesame)", "Right: the compound begins with तिल."),
               ("मधुक (probably licorice)", "Madhuka is not named in unit 69."),
               ("बिल्व (bael)", "Right: बिल्व stands third in the compound.")],
              [0, 2, 4],
              "Sesame, black gram and bilva are printed in the compound; radish and madhuka are not.",
              "तिल-माष-बिल्व-शलाटु-युक्तान्."),
        mcq("transfer", 5, "Built like तिलमाष...युक्तान् सक्तून्, what does मधुयुक्तं पयः mean?",
            ("Milk combined with honey", "X-युक्त agrees with its noun: मधुयुक्तम् qualifies पयः, so milk combined with honey."),
            [("Honey given in place of milk", "युक्त means combined with, not in place of."),
             ("Milk kept apart from honey", "युक्त joins two things; it does not separate them."),
             ("Honey taken after the milk", "युक्त states a mixture, not an order of taking.")],
            "मधुयुक्तं पयः = milk combined with honey, as तिलमाष...युक्तान् सक्तून् = saktu combined with sesame and the rest.",
            "X-युक्त + noun = the noun combined with X.",
            teaches="A compound ending in -युक्त (combined with) agrees with its noun: ...युक्तान् (m. acc. pl.) with सक्तून्."),
    ],
}

# ---------------------------------------------------------------- unit 70
AUTHORED["70"] = {
    "title": "मेद्यमांसोपदंशं वा मार्द्दीकं",
    "question": "By unit 70, what further option is named, and what is its relish?",
    "rule": ("Or (वा) mārdvīka (grape wine; printed मार्द्दीकं), having meat, probably fatty (मेद्य), as its relish "
             "(उपदंश, a bite eaten with a drink). The line has no verb; it appears to continue unit 69."),
    "limits": ("मेद्य = fatty is probable (medhya also possible). मार्द्वीक corrects printed मार्द्दीकं (near-certain). "
               "The verb of unit 69 is carried. Questions use medya only as 'probable' and the correction only as "
               "near-certain; none asks what medya must mean. A prose line."),
    "explain_hi": ("यह छोटी गद्य-पंक्ति एक और विकल्प (वा) देती है: मार्द्वीक यानी अंगूर की मदिरा, जिसके साथ खाने की वस्तु "
                   "(उपदंश) मांस हो, सम्भवतः चर्बीयुक्त (मेद्य)। "
                   "पंक्ति में अपनी क्रिया नहीं है; इकाई ६९ की ‘पाययेत्’ (पिलाए) चली आती है, अनुवाद उसे जोड़ता नहीं। "
                   "छपा ‘मार्द्दीकं’ लगभग निश्चित रूप से ‘मार्द्वीकम्’ है (द्व का द्द पढ़ा जाना; इकाई ७६ में ‘मृद्वीकानां’ ठीक छपा है)। "
                   "‘मेद्य’ = चर्बीयुक्त सम्भावित है; ‘मेध्य’ (बुद्धिवर्धक) भी पढ़ा जा सकता है, पर मांस के साथ कम जँचता है।"),
    "hook": "या: साथ में मांस का कौर, और अंगूरी मदिरा।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 70, what is the relish (उपदंश) eaten with the drink?",
            ("Meat, probably fatty", "मेद्यमांसोपदंशम्: meat (probably fatty) as the relish."),
            [("Sesame and black gram", "Sesame and black gram go into the saktu of unit 69."),
             ("Red śāli rice", "Red śāli rice is the food of unit 68."),
             ("Radish soup with ghee", "Radish soup is an option of unit 68.")],
            "The relish (upadaṃśa) is meat, probably fatty.",
            "मेद्य-मांस-उपदंशम्: meat as the relish."),
        order(1, "Put these parts of unit 70 in the line's order.",
              ["मेद्य", "मांस", "उपदंशं", "वा", "मार्द्दीकं"],
              "Fatty (probable) meat as relish, or mārdvīka.",
              "मेद्य → मांस → उपदंशं → वा → मार्द्दीकं."),
        match(2, "Match each word of unit 70 to its meaning.",
              [["मेद्य", "fatty (probable)"], ["मांस", "meat"], ["उपदंश", "a relish eaten with a drink"], ["वा", "or"]],
              "Meat, probably fatty, as the relish: one more option.",
              "मेद्य, मांस, उपदंश, वा.", role="extend",
              teaches="A bahuvrīhi such as मांसोपदंशम् describes something else: 'having meat as its relish', here the drink."),
        mcq("discriminate", 3, "Which split of मांसोपदंशम् is right?",
            ("मांस + उपदंशम्", "अ + उ → ओ: मांस + उपदंशम् → मांसोपदंशम्."),
            [("मांसे + उपदंशम्", "ए before उ would give मांसयुपदंशम् or मांस उपदंशम्, not ओ."),
             ("मांसो + पदंशम्", "पदंशम् is not a word; the word is उपदंश, relish."),
             ("मांसः + उपदंशम्", "अः before उ drops the visarga and stays apart: मांस उपदंशम्.")],
            "मांस (meat) + उपदंशम् (relish): अ + उ → ओ.",
            "अ + उ → ओ."),
        multi("apply", 4, "Which statements about unit 70 are right by the card?",
              [("The line names honey as the relish", "The relish is meat, probably fatty; no honey is named."),
               ("The line has no verb of its own", "Right: the verb of unit 69 is carried, not printed."),
               ("Printed मार्द्दीकं is read as मार्द्वीकम्", "Right: a near-certain correction (द्व misread as द्द)."),
               ("The line names the kind of meat", "No animal is named; only meat, probably fatty.")],
              [1, 2],
              "The line has no verb, and its last word is a near-certain correction; medya is only probably 'fatty'.",
              "मेद्यमांसोपदंशं वा मार्द्दीकं (= मार्द्वीकम्): no verb."),
        mcq("transfer", 5, "By the rule of मांसोपदंशम्, how is हित + उपदेशः (good counsel) joined?",
            ("हितोपदेशः", "अ + उ → ओ, as मांस + उपदंशम् → मांसोपदंशम्."),
            [("हितौपदेशः", "औ comes from अ + ओ or अ + औ, not from अ + उ."),
             ("हितेपदेशः", "ए comes from अ + इ, not from अ + उ."),
             ("हितुपदेशः", "The अ does not simply vanish before उ.")],
            "हित + उपदेशः = हितोपदेशः, like मांस + उपदंशम् = मांसोपदंशम्.",
            "अ + उ → ओ.",
            teaches="A short अ followed by उ joins as ओ: मांस + उपदंशम् → मांसोपदंशम्."),
    ],
}

# ---------------------------------------------------------------- unit 71
AUTHORED["71"] = {
    "title": "तैलेन चाभीक्ष्णमुदरवंक्षणोरुकटीपार्श्वपृष्ठान्यभ्यंज्यात्",
    "question": "By unit 71, which parts of the body are anointed with oil, and how often?",
    "rule": ("And one should repeatedly (अभीक्ष्णम्) anoint with oil (तैलेन) the belly (उदर), groin (वंक्षण), thighs "
             "(ऊरु), waist (कटी), flanks (पार्श्व) and back (पृष्ठ). It appears to continue the treatment of units 67-70."),
    "limits": ("The kind of oil is not stated, nor who is anointed (the woman is understood). No count per day or duration "
               "is given. A prose line."),
    "explain_hi": ("यह गद्य-पंक्ति सम्भवतः इकाई ६७-७० के उपचार को आगे बढ़ाती है। "
                   "तेल से (तैलेन) बार-बार (अभीक्ष्णम्) छह अंगों का अभ्यंग करे (अभ्यञ्ज्यात्): पेट (उदर), वंक्षण यानी जाँघ का जोड़, "
                   "ऊरु यानी जाँघें, कमर (कटी), पार्श्व यानी बगल और पीठ (पृष्ठ)। "
                   "तेल किस प्रकार का हो, यह नहीं कहा गया, और दिन में कितनी बार, यह भी नहीं। "
                   "छह अंग एक द्वन्द्व समास में हैं, इसलिए अन्त में नपुंसक बहुवचन ‘पृष्ठानि’ है।"),
    "hook": "तेल बार-बार: पेट, वंक्षण, जाँघ, कमर, बगल, पीठ।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 71, with what does one anoint the belly and back?",
            ("With oil (तैल)", "तैलेन ... अभ्यञ्ज्यात्: with oil."),
            [("With ghee (घृत)", "Ghee is not named in unit 71; the line says तैलेन."),
             ("With milk (पयस्)", "Milk is the liquid of unit 69, not an unguent here."),
             ("With a paste (कल्क)", "A paste (kalka) belongs to the enema of unit 76.")],
            "The anointing is done with oil.",
            "तैलेन = with oil."),
        order(1, "Put the body parts of unit 71 in the line's order.",
              ["उदर", "वंक्षण", "ऊरु", "कटी", "पार्श्व", "पृष्ठ"],
              "Belly, groin, thighs, waist, flanks, back.",
              "उदर → वंक्षण → ऊरु → कटी → पार्श्व → पृष्ठ."),
        match(2, "Match each body part of unit 71 to its meaning.",
              [["उदर", "belly"], ["वंक्षण", "groin"], ["ऊरु", "thigh"], ["कटी", "waist"], ["पार्श्व", "flank"],
               ["पृष्ठ", "back"]],
              "The six parts anointed with oil.",
              "उदर, वंक्षण, ऊरु, कटी, पार्श्व, पृष्ठ.", role="extend",
              teaches="अभ्यञ्ज्यात् (abhi-√añj) = should anoint, rub with oil; अभीक्ष्णम् = repeatedly."),
        mcq("discriminate", 3, "Which split of वंक्षणोरु is right?",
            ("वंक्षण + ऊरु", "अ + ऊ → ओ: वंक्षण (groin) + ऊरु (thigh)."),
            [("वंक्षणे + उरु", "ए before उ would give वंक्षणयुरु or वंक्षण उरु, not ओ."),
             ("वंक्षणो + रु", "रु is not a word; the word is ऊरु, thigh."),
             ("वंक्षणः + ऊरु", "अः before ऊ drops the visarga and stays apart: वंक्षण ऊरु.")],
            "वंक्षण (groin) + ऊरु (thigh): अ + ऊ → ओ.",
            "अ + उ/ऊ → ओ."),
        mcq("apply", 4, "A helper asks how often to anoint, and with which oil. What does unit 71 say?",
            ("Repeatedly; the kind of oil is not stated", "अभीक्ष्णम् = repeatedly; तैलेन names no kind of oil."),
            [("Once a day; with sesame oil, as stated", "No count per day and no kind of oil are given."),
             ("Only once; with madhuraka-cooked oil", "Madhuraka oil is for the enema of unit 75; here the anointing is repeated."),
             ("Twice a month; with mustard oil, as stated", "No such count or oil is in unit 71.")],
            "Repeatedly, with oil of a kind not stated.",
            "तैलेन अभीक्ष्णम् अभ्यञ्ज्यात्."),
        mcq("transfer", 5, "By the rule of पृष्ठान्यभ्यंज्यात्, how is दधि + अत्र (curd here) joined?",
            ("दध्यत्र", "इ before a different vowel becomes य्, as पृष्ठानि + अभ्यञ्ज्यात्."),
            [("दधीत्र", "ई comes from इ + इ, not from इ + अ."),
             ("दधेत्र", "ए comes from अ + इ, not from इ + अ."),
             ("दध्यात्र", "या would need इ + आ; अत्र begins with a short अ.")],
            "दधि + अत्र = दध्यत्र, like पृष्ठानि + अभ्यञ्ज्यात् = पृष्ठान्यभ्यञ्ज्यात्.",
            "इ + a different vowel → य् + that vowel.",
            teaches="इ before a different vowel becomes य्: पृष्ठानि + अभ्यञ्ज्यात् → पृष्ठान्यभ्यञ्ज्यात्."),
    ],
}

# ---------------------------------------------------------------- unit 72
AUTHORED["72"] = {
    "title": "मुहुर्मुहुश्चैनां हर्षयेत्",
    "question": "By unit 72, what should one do for her, and how often?",
    "rule": ("And (च) one should gladden (हर्षयेत्) her (एनाम्) again and again (मुहुर्मुहुः). It appears to continue "
             "the treatment of unit 71."),
    "limits": ("How she is to be gladdened is not stated; हर्षयेत् keeps its plainest sense, 'gladden, cheer'. A prose line."),
    "explain_hi": ("यह छोटी गद्य-पंक्ति कहती है: और इसे (एनाम्) बार-बार (मुहुर्मुहुः) हर्षित करे (हर्षयेत्)। "
                   "यह सम्भवतः इकाई ७१ के अभ्यंग के साथ चलते उपचार का अगला अंग है। "
                   "किस उपाय से प्रसन्न करे, यह नहीं बताया गया। "
                   "‘हर्षयेत्’ √हृष् का प्रेरणार्थक विधिलिङ् है: प्रसन्न करे, हर्षित करे।"),
    "hook": "तन पर तेल, मन में हर्ष: बार-बार प्रसन्न करे।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 72, how often should one gladden her?",
            ("Again and again (मुहुर्मुहुः)", "मुहुर्मुहुश्चैनां हर्षयेत्: again and again."),
            [("Only once (सकृत्)", "The line says मुहुर्मुहुः, again and again."),
             ("Only at night (रात्रौ)", "No time of day is named in unit 72."),
             ("Only after meals (भोजनात् परम्)", "Meals are not named in unit 72.")],
            "One should gladden her again and again.",
            "मुहुर्मुहुः = again and again."),
        order(1, "Put the words of unit 72 in the line's order.",
              ["मुहुर्मुहुः", "च", "एनाम्", "हर्षयेत्"],
              "Again and again, and, her, one should gladden.",
              "मुहुर्मुहुः → च → एनाम् → हर्षयेत्."),
        match(2, "Match each word of unit 72 to its meaning.",
              [["मुहुर्मुहुः", "again and again"], ["च", "and"], ["एनाम्", "her"], ["हर्षयेत्", "should gladden"]],
              "And one should gladden her again and again.",
              "मुहुर्मुहुः, च, एनाम्, हर्षयेत्.", role="extend",
              teaches="हर्षयेत् is the causative optative of √हृष् (be glad): 'should make glad, should gladden'."),
        mcq("discriminate", 3, "Which split of मुहुश्चैनाम् is right?",
            ("मुहुः + च + एनाम्", "Visarga before च → श्; अ + ए → ऐ."),
            [("मुहुः + च + इनाम्", "अ + इ would give चेनाम्, with ए, not ऐ."),
             ("मुहुः + चा + इनाम्", "आ + इ would also give ए (चेनाम्), not ऐ."),
             ("मुहुश् + चै + नाम्", "चै and नाम् do not give 'and her'; the words are च and एनाम्.")],
            "मुहुः (again) + च (and) + एनाम् (her): विसर्ग + च → श्च; अ + ए → ऐ.",
            "Visarga + च → श्च; अ + ए → ऐ."),
        mcq("apply", 4, "A carer has done the oil anointing of unit 71. What does unit 72 add?",
            ("Gladden her, again and again", "मुहुर्मुहुश्चैनां हर्षयेत्."),
            [("Keep her silent and quite alone", "Unit 72 asks to gladden her, not to keep her alone."),
             ("Make her fast until the evening", "No fasting is named in unit 72."),
             ("Let her sleep through the day", "Sleep is not named in unit 72.")],
            "Unit 72 adds: gladden her again and again.",
            "हर्षयेत् = should gladden."),
        mcq("transfer", 5, "By the rule of चैनाम् (च + एनाम्), how is च + एव joined?",
            ("चैव", "अ + ए → ऐ, as च + एनाम् → चैनाम्."),
            [("चेव", "ए would come from अ + इ, not from अ + ए."),
             ("च्येव", "य् comes from इ before a vowel; च ends in अ."),
             ("चाव", "आ would come from अ + अ; एव begins with ए.")],
            "च + एव = चैव, like च + एनाम् = चैनाम्.",
            "अ + ए → ऐ.",
            teaches="A short अ followed by ए joins as ऐ: च + एनाम् → चैनाम्."),
    ],
}

# ---------------------------------------------------------------- unit 73
AUTHORED["73"] = {
    "title": "पूर्वोक्तं चेक्षेत",
    "question": "By unit 73, to what should one look?",
    "rule": ("And (च) one should look to (ईक्षेत) what was said before (पूर्वोक्तम्). It appears to close the līna "
             "treatment of units 67-72."),
    "limits": ("The line does not say what 'said before' refers to (the earlier regimen is likely, not stated): no question "
               "names it. A prose line."),
    "explain_hi": ("यह बहुत छोटी गद्य-पंक्ति सम्भवतः इकाई ६७-७२ के लीन गर्भ के उपचार को समाप्त करती है। "
                   "और पहले कहे हुए (पूर्वोक्तम्) पर दृष्टि रखे (ईक्षेत)। "
                   "‘पूर्वोक्त’ किसे कहता है, पंक्ति नहीं बताती; पहले कहा गया उपचार-क्रम सम्भव है, पर लिखा नहीं। "
                   "‘ईक्षेत’ √ईक्ष् का आत्मनेपद विधिलिङ् है: देखे, ध्यान रखे।"),
    "hook": "जो पहले कहा गया, उस पर नज़र रखे।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 73, to what should one look?",
            ("What was said before", "पूर्वोक्तं चेक्षेत: look to what was said before."),
            [("The signs of a dead fetus", "Those signs come in unit 82, not here."),
             ("The movement of the stars", "No stars are named in unit 73."),
             ("The colour of her urine", "Urine colour is not named in unit 73.")],
            "One should look to what was said before.",
            "पूर्वोक्तम् = what was said before."),
        order(1, "Put the parts of unit 73 in the line's order.",
              ["पूर्व", "उक्तं", "च", "ईक्षेत"],
              "Before, said, and, one should look to.",
              "पूर्व → उक्तं → च → ईक्षेत."),
        match(2, "Match each part of unit 73 to its meaning.",
              [["पूर्व", "before, earlier"], ["उक्त", "said"], ["च", "and"], ["ईक्षेत", "should look to, observe"]],
              "And one should look to what was said before.",
              "पूर्व, उक्त, च, ईक्षेत.", role="extend",
              teaches="उक्त is the past passive participle of √वच् (speak): 'said'; पूर्वोक्त = said before."),
        mcq("discriminate", 3, "Which split of चेक्षेत is right?",
            ("च + ईक्षेत", "अ + ई → ए: च + ईक्षेत → चेक्षेत."),
            [("च + एक्षेत", "अ + ए would give ऐ: चैक्षेत."),
             ("चे + क्षेत", "क्षेत is not a verb; the verb is ईक्षेत."),
             ("च् + ईक्षेत", "च् is not the particle; the particle is च, ending in अ.")],
            "च (and) + ईक्षेत (should look to): अ + ई → ए.",
            "अ + इ/ई → ए."),
        multi("apply", 4, "Which statements about unit 73 are right by the card?",
              [("The line names the regimen it means", "The data: what पूर्वोक्तम् refers to is not stated."),
               ("ईक्षेत is an optative: should look to", "Right: 3 sg. opt. mid. √ईक्ष्."),
               ("ईक्षेत is a future: will look", "The gram label is optative, not future."),
               ("What पूर्वोक्तम् refers to is not stated", "Right: the earlier regimen is likely, but not stated.")],
              [1, 3],
              "ईक्षेत is an optative, and the line does not say what was said before.",
              "पूर्वोक्तं चेक्षेत: referent not stated."),
        mcq("transfer", 5, "By the rule of चेक्षेत, how is गण + ईशः (lord of the troop) joined?",
            ("गणेशः", "अ + ई → ए, as च + ईक्षेत → चेक्षेत."),
            [("गणैशः", "ऐ comes from अ + ए or अ + ऐ, not from अ + ई."),
             ("गणीशः", "The अ does not simply vanish before ई."),
             ("गणोशः", "ओ comes from अ + उ, not from अ + ई.")],
            "गण + ईशः = गणेशः, like च + ईक्षेत = चेक्षेत.",
            "अ + ई → ए.",
            teaches="A short अ followed by ई joins as ए: च + ईक्षेत → चेक्षेत."),
    ],
}

# ---------------------------------------------------------------- unit 74
AUTHORED["74"] = {
    "title": "यस्याः पुनरुदावर्त्तविबंधः स्यात्",
    "question": "By unit 74, how is a woman with udāvarta and vibandha treated?",
    "rule": ("If she has udāvarta (Vāta running upward in reverse) and vibandha (constipation) (read as two disorders; "
             "'constipation of the udāvarta kind' is also possible), one should treat her (उपाचरेत्) with foods and drinks "
             "that remove Vāta (वातहर) and are unctuous (स्निग्ध). A new topic appears to begin here."),
    "limits": ("उदावर्तविबन्धः may be two disorders or 'constipation of the udāvarta kind': no question decides which (one "
               "asks only that it is open). No food or drug is named. A prose line."),
    "explain_hi": ("यहाँ सम्भवतः नया विषय आरम्भ होता है। "
                   "जिस स्त्री को (यस्याः) उदावर्त यानी वात का उलटा ऊपर चढ़ना और विबन्ध यानी कब्ज हो (स्यात्), उसका (ताम्) "
                   "वात हरने वाले (वातहर), चिकने (स्निग्ध) अन्न और पानों से उपचार करे (उपाचरेत्)। "
                   "‘उदावर्तविबन्धः’ को दो रोग (द्वन्द्व) भी पढ़ा जा सकता है और ‘उदावर्त प्रकार का विबन्ध’ भी; डेटा पहला पाठ लेता है, "
                   "पर दूसरा खुला है। "
                   "कोई विशेष अन्न या औषध नाम से नहीं दिया गया। छपा ‘उदावर्त्त’ (र्त्त) छपाई की आदत है।"),
    "hook": "उलटा वात, रुका पेट: वात हरने वाला, चिकना अन्न-पान।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 74, with what is she treated?",
            ("Vāta-removing, unctuous food and drink", "वातहरस्निग्धान्नपानैरुपाचरेत्."),
            [("Cold, dry food and a long fast", "The line says unctuous (स्निग्ध), not dry, and names no fast."),
             ("Sharp purgatives and strong emetics at once", "No purgative or emetic is named in unit 74."),
             ("Bloodletting and a light, dry diet", "Neither is named; the food is unctuous.")],
            "She is treated with Vāta-removing, unctuous foods and drinks.",
            "वातहर-स्निग्ध-अन्न-पानैः उपाचरेत्."),
        order(1, "Put these parts of unit 74 in the line's order.",
              ["यस्याः पुनः", "उदावर्त्तविबंधः स्यात्", "तां", "वातहरस्निग्धान्नपानैः", "उपाचरेत्"],
              "Of her, however, who may have udāvarta and vibandha, her, with Vāta-removing unctuous foods and drinks, one should treat.",
              "यस्याः पुनः → उदावर्त्तविबंधः स्यात् → तां → वातहरस्निग्धान्नपानैः → उपाचरेत्."),
        match(2, "Match each word of unit 74 to its meaning.",
              [["उदावर्त", "Vāta running upward in reverse"], ["विबन्ध", "constipation"], ["स्निग्ध", "unctuous"],
               ["अन्नपान", "food and drink"], ["उपाचरेत्", "should treat"]],
              "The two complaints, and the unctuous foods and drinks that treat them.",
              "उदावर्त, विबन्ध, स्निग्ध, अन्नपान, उपाचरेत्.", role="extend",
              teaches="उप-आ-√चर् = to attend, to treat: उपाचरेत् = one should treat."),
        mcq("discriminate", 3, "Which split of स्निग्धान्न is right?",
            ("स्निग्ध + अन्न", "अ + अ → आ: स्निग्ध (unctuous) + अन्न (food)."),
            [("स्निग्धे + अन्न", "ए + अ would give स्निग्धेऽन्न, with ए kept and ऽ."),
             ("स्निग्धः + अन्न", "अः + अ would give स्निग्धोऽन्न, with ओऽ."),
             ("स्निग्धान् + न", "न here is not a word for food; the word is अन्न.")],
            "स्निग्ध (unctuous) + अन्न (food): अ + अ → आ.",
            "अ + अ → आ."),
        multi("apply", 4, "Which statements about unit 74 are right by the card?",
              [("The foods and drinks are unctuous", "Right: स्निग्ध."),
               ("The line names a particular drug", "No drug or food is named; only their qualities."),
               ("उदावर्तविबन्धः may be read as two disorders or one", "Right: the data leaves both readings open."),
               ("The text settles that it is one disorder", "It is not settled; the data reads two, with one possible.")],
              [0, 2],
              "The foods are unctuous and remove Vāta; whether udāvarta-vibandha is one disorder or two is open.",
              "वातहर-स्निग्ध अन्नपान; उदावर्तविबन्धः two-way."),
        mcq("transfer", 5, "Built like वातहर (removing Vāta), what does पित्तहर mean?",
            ("Removing Pitta", "-हर = removing, as in वातहर."),
            [("Caused by Pitta", "That would be पित्तज; -हर removes."),
             ("Increasing Pitta", "-हर takes away; it does not increase."),
             ("Seated in Pitta", "-हर does not mean seated in.")],
            "पित्तहर = removing Pitta, like वातहर = removing Vāta.",
            "X-हर = removing X.",
            teaches="-हर at the end of a compound = removing: वातहर = what removes Vāta."),
    ],
}

# ---------------------------------------------------------------- unit 75
AUTHORED["75"] = {
    "title": "अष्टमे तु मासे मधुरकसिद्धेन तैलेनानुवासयेत्",
    "question": "By unit 75, what is given in the eighth month, and with what oil?",
    "rule": ("In the eighth month (अष्टमे मासे), however, one should give an anuvāsana (unctuous enema) with oil cooked "
             "with madhuraka (probably a group of sweet drugs). It appears to continue unit 74."),
    "limits": ("'Of pregnancy' is understood; the line says only 'the eighth month'. Madhuraka as a group of sweet drugs is "
               "probable, not certain, and its members are not listed: no question names them. A prose line."),
    "explain_hi": ("यह गद्य-पंक्ति सम्भवतः इकाई ७४ के उदावर्त-विबन्ध के उपचार को आगे बढ़ाती है। "
                   "आठवें मास में तो (अष्टमे तु मासे) मधुरक से पकाए (मधुरकसिद्धेन) तेल से अनुवासन यानी चिकनाई वाली बस्ति दे "
                   "(अनुवासयेत्)। "
                   "‘गर्भ का आठवाँ मास’ समझा जाता है; पंक्ति केवल ‘आठवाँ मास’ कहती है। "
                   "मधुरक सम्भवतः मधुर औषधों का समूह है, पर यह निश्चित नहीं (विवादित), और उसके सदस्य यहाँ नहीं गिनाए गए।"),
    "hook": "आठवाँ मास: मधुरक-तेल से अनुवासन।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 75, in which month is the anuvāsana given?",
            ("The eighth (अष्टम)", "अष्टमे तु मासे: in the eighth month."),
            [("The seventh (सप्तम)", "The line says अष्टमे, the eighth."),
             ("The ninth (नवम)", "The line says अष्टमे, the eighth."),
             ("The fifth (पञ्चम)", "The line says अष्टमे, the eighth.")],
            "The anuvāsana is given in the eighth month.",
            "अष्टमे मासे = in the eighth month."),
        order(1, "Put these parts of unit 75 in the line's order.",
              ["अष्टमे तु", "मासे", "मधुरकसिद्धेन", "तैलेन", "अनुवासयेत्"],
              "In the eighth, however, month, cooked with madhuraka, with oil, one should give an anuvāsana.",
              "अष्टमे तु → मासे → मधुरकसिद्धेन → तैलेन → अनुवासयेत्."),
        match(2, "Match each word of unit 75 to its meaning.",
              [["अष्टम", "eighth"], ["मास", "month"], ["सिद्ध", "cooked"], ["तैल", "oil"],
               ["अनुवासयेत्", "should give an unctuous enema"]],
              "In the eighth month, an anuvāsana with oil cooked with madhuraka.",
              "अष्टम, मास, सिद्ध, तैल, अनुवासयेत्.", role="extend",
              teaches="X-सिद्ध = cooked with X: मधुरकसिद्धेन तैलेन = with oil cooked with madhuraka."),
        mcq("discriminate", 3, "Which split of तैलेनानुवासयेत् is right?",
            ("तैलेन + अनुवासयेत्", "अ + अ → आ: तैलेन (with oil) + अनुवासयेत्."),
            [("तैलेने + अनुवासयेत्", "ए + अ would give तैलेनेऽनुवासयेत्, with ए and ऽ."),
             ("तैलेनः + अनुवासयेत्", "अः + अ would give तैलेनोऽनुवासयेत्, with ओऽ."),
             ("तैलेना + नुवासयेत्", "नुवासयेत् is not a verb; the verb is अनुवासयेत्.")],
            "तैलेन + अनुवासयेत्: अ + अ → आ.",
            "अ + अ → आ."),
        mcq("apply", 4, "Which statement about madhuraka is right by the card?",
            ("Probably a group of sweet drugs; none listed", "The data: probable, not certain, and the members are not listed here."),
            [("Licorice alone, which the line names as madhuraka", "No single drug is named; madhuraka is probably a group."),
             ("A set of four sweet drugs, listed in this very line", "No members are listed in unit 75."),
             ("Honey boiled into the oil, as the line itself states", "Honey is not named; the oil is cooked with madhuraka.")],
            "Madhuraka is probably a group of sweet drugs; its members are not listed.",
            "मधुरक: probable group, members not listed."),
        mcq("transfer", 5, "Built like अष्टमे मासे (in the eighth month), what does सप्तमे दिवसे mean?",
            ("On the seventh day", "The locative of a time word gives 'on/in' that time."),
            [("For seven whole days", "A span of time would need another case; सप्तमे is the seventh, one day."),
             ("Seven times in a day", "सप्तम is an ordinal, the seventh, not a count of times."),
             ("After seven months", "दिवस is a day, not a month, and the locative gives 'on', not 'after'.")],
            "सप्तमे दिवसे = on the seventh day, like अष्टमे मासे = in the eighth month.",
            "Ordinal + time word in the locative = in/on that time.",
            teaches="The locative of a time word gives 'in/on' that time: अष्टमे मासे = in the eighth month."),
    ],
}

# ---------------------------------------------------------------- unit 76
AUTHORED["76"] = {
    "title": "तदसिद्धौ ... निरूहयेत्",
    "question": "By unit 76, what enema is given if the anuvāsana does not succeed, and how is it made?",
    "rule": ("If that does not succeed (तदसिद्धौ), extract with milk and half water the rasa of two groups of drugs, add a "
             "paste (कल्क) of piyāla and bibhītaka kernels and sesame, and give it slightly salty and warm as a nirūha "
             "(decoction enema)."),
    "limits": ("'That' (the anuvāsana) is taken from context. Ananta rests on a conjectural reading; ikṣuvālikā and vetasa "
               "are disputed; parivyādha and bhūtikā are unidentified; whether the second group is roots is not settled. "
               "No question rests on these. A prose line."),
    "explain_hi": ("यह लम्बी गद्य-पंक्ति निरूह यानी काढ़े की बस्ति का विधान देती है। "
                   "उसके (सम्भवतः इकाई ७५ के अनुवासन के) सिद्ध न होने पर (तदसिद्धौ), दो समूहों का रस दूध और आधे जल से "
                   "(पयसाऽर्धोदकेन) निकाले (उद्धृत्य)। "
                   "पहला समूह जड़ों (मूल) का है: वीरण (सम्भवतः खस), शालि (धान), कुश, काश (काँस), इक्षुवालिका (विवादित), "
                   "वेतस (विवादित), परिव्याध (अज्ञात)। "
                   "दूसरा समूह: भूतिका (अज्ञात), अनन्त (अनुमानित पाठ; सम्भवतः सारिवा), काश्मर्य (गम्भारी), परूषक (फालसा), "
                   "मधुक (सम्भवतः मुलेठी), मृद्वीका (अंगूर); ये जड़ें हैं या पूरी औषधि, तय नहीं। "
                   "उस रस में पियाल (सम्भवतः चिरौंजी) और बिभीतक (बहेड़ा) की गिरी (मज्जा) तथा तिल का कल्क मिलाकर, "
                   "थोड़ा नमकीन और गरम करके निरूह दे (निरूहयेत्)।"),
    "hook": "अनुवासन न चले तो निरूह: दूध-जल में रस, गिरी-तिल का कल्क, थोड़ा नमक, गरम।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 76, what kind of enema is given if that does not succeed?",
            ("A nirūha (decoction enema)", "निरूहयेत्: one should give a nirūha."),
            [("A milk enema with rock salt", "That milk enema (kṣīrabasti) is unit 52; unit 76 ends with निरूहयेत्."),
             ("A nasal dose of oil (nasya)", "No nasal dose is named; the verb is निरूहयेत्."),
             ("An anuvāsana with ghee alone", "Unit 76 gives a nirūha, not an anuvāsana.")],
            "If that does not succeed, a nirūha (decoction enema) is given.",
            "तदसिद्धौ ... निरूहयेत्."),
        order(1, "Put these parts of unit 76 in the line's order.",
              ["तदसिद्धौ", "वीरणशालिकुशकाश...मूलानां", "भूतिका...मृद्वीकानां च", "पयसाऽर्द्धोदकेनोद्धृत्य रसं",
               "तेन पियालबिभीतकमज्जतिलकल्कयुक्तेन", "ईषल्लवणोष्णेन निरूहयेत्"],
              "If that fails; of the roots of vīraṇa ...; and of bhūtikā ... mṛdvīkā; with milk and half water, having "
              "extracted the rasa; with that, combined with a paste of kernels and sesame; slightly salty and warm, give a nirūha.",
              "तदसिद्धौ → ...मूलानां → ...मृद्वीकानां च → पयसाऽर्द्धोदकेनोद्धृत्य रसं → तेन ...कल्कयुक्तेन → ईषल्लवणोष्णेन निरूहयेत्."),
        match(2, "Match each drug name of unit 76 to the data's identification.",
              [["कुश", "Desmostachya bipinnata (standard)"], ["काश", "Saccharum spontaneum (standard)"],
               ["काश्मर्य", "Gmelina arborea (standard)"], ["परूषक", "Grewia asiatica, phalsa (standard)"],
               ["बिभीतक", "Terminalia bellirica (standard)"], ["पियाल", "Buchanania lanzan (probable)"]],
              "Six names of unit 76 with the data's identifications and labels.",
              "कुश, काश, काश्मर्य, परूषक, बिभीतक (standard); पियाल (probable).", role="extend",
              teaches="निरूह = a decoction enema; here the extracted rasa, with a paste (कल्क) mixed in, is its liquid."),
        mcq("discriminate", 3, "By unit 76, what is mixed into the extract before the enema?",
            ("A paste of piyāla and bibhītaka kernels and sesame", "पियालबिभीतकमज्जतिलकल्कयुक्तेन."),
            [("Honey, rock salt and a little ghee in equal parts", "Honey and ghee are not named; the salt is only slight (ईषत्)."),
             ("Oil cooked with madhuraka, the oil of the last unit", "That oil is the anuvāsana of unit 75; here a paste is added."),
             ("A powder of the first group's roots, dried and sifted", "The roots give the extract itself; the paste is of kernels and sesame.")],
            "The extract is combined with a paste of piyāla and bibhītaka kernels and sesame.",
            "तेन ...मज्जतिलकल्कयुक्तेन."),
        multi("apply", 4, "Which describe the nirūha of unit 76?",
              [("Given cold and strongly salted", "The line says slightly salty and warm: ईषल्लवणोष्णेन."),
               ("Given slightly salty and warm", "Right: ईषत्-लवण-उष्णेन."),
               ("Extracted with milk and half water", "Right: पयसाऽर्धोदकेन."),
               ("Boiled down in ghee alone", "No ghee is named; the extract is made with milk and water."),
               ("Given if the earlier step did not succeed", "Right: तदसिद्धौ, if that does not succeed.")],
              [1, 2, 4],
              "Extracted with milk and half water, slightly salty and warm, given if that does not succeed.",
              "तदसिद्धौ ... पयसाऽर्धोदकेन ... ईषल्लवणोष्णेन निरूहयेत्."),
        mcq("transfer", 5, "By the rule of ईषल्लवण (ईषत् + लवण), how is उत् + लासः (joy) joined?",
            ("उल्लासः", "त् before ल becomes ल्, as ईषत् + लवण → ईषल्लवण."),
            [("उद्लासः", "द् does not stay before ल; it becomes ल्."),
             ("उत्लासः", "त् does not stay before ल; it becomes ल्."),
             ("उच्छासः", "च्छ comes (optionally) from त् + श, not from त् + ल.")],
            "उत् + लासः = उल्लासः, like ईषत् + लवण = ईषल्लवण.",
            "त् + ल → ल्ल.",
            teaches="A final त् before ल becomes ल्: ईषत् + लवण → ईषल्लवण."),
    ],
}

# ---------------------------------------------------------------- unit 77
AUTHORED["77"] = {
    "title": "विगतविबंधां च ... गर्भिणीमतिपातयेत्",
    "question": "By unit 77, when is the second anuvāsana given, and why must udāvarta not be neglected?",
    "rule": ("When her constipation has gone and she has bathed and eaten, give an anuvāsana in the evening (सायम्) with "
             "that very oil. Udāvarta, if neglected (समुपेक्षित), would suddenly (सहसा) destroy the pregnant woman together "
             "with her fetus."),
    "limits": ("Two printed lines. 'Bathed' rests on a near-certain correction (printed स्त्राता for स्नाता). That the oil is "
               "the madhuraka oil of unit 75 follows from context, not from the words. अतिपातयेत् = destroy is the plain "
               "sense; 'cause to miscarry' is a narrower possible reading: no question picks between them."),
    "explain_hi": ("दो छपी पंक्तियाँ। "
                   "पहली: जिसका विबन्ध यानी कब्ज दूर हो गया हो (विगतविबन्धाम्), जो नहा चुकी (सुधारा पाठ: स्नाता) और खा चुकी हो "
                   "(अशिताम्), उसे सायंकाल (सायम्) उसी तेल से (तेनैव तैलेन) अनुवासन दे। "
                   "‘उसी तेल’ सम्भवतः इकाई ७५ का मधुरक-तेल है, पर शब्दों में नहीं कहा। "
                   "दूसरी पंक्ति (हि = निश्चय ही): उदावर्त यदि उपेक्षित हो (समुपेक्षितः), तो अचानक (सहसा) गर्भ सहित (सगर्भाम्) "
                   "गर्भवती को नष्ट कर दे (अतिपातयेत्)। "
                   "‘अतिपातयेत्’ का सरल अर्थ नष्ट करना है; ‘गर्भपात कराना’ एक संकरा सम्भव अर्थ है।"),
    "hook": "कब्ज गया, नहाई-खाई: सायं अनुवासन; उदावर्त की उपेक्षा घातक।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 77, at what time is this anuvāsana given?",
            ("In the evening (सायम्)", "सायं तेनैव तैलेनानुवासयेत्."),
            [("At dawn (प्रातः)", "The line says सायम्, in the evening."),
             ("At midday (मध्याह्ने)", "The line says सायम्, in the evening."),
             ("At midnight (अर्धरात्रे)", "The line says सायम्, in the evening.")],
            "The anuvāsana is given in the evening.",
            "सायम् = in the evening."),
        order(1, "Put these parts of unit 77 in the order of its two lines.",
              ["विगतविबंधां च", "स्त्राताशितां", "सायं", "तेनैव तैलेनानुवासयेत्", "उदावर्त्तोहि समुपेक्षितः",
               "सहसा सगर्भां गर्भिणीमतिपातयेत्"],
              "Her whose constipation has gone, bathed and fed, in the evening, with that very oil, give an anuvāsana. "
              "Udāvarta indeed, neglected, would suddenly destroy the pregnant woman with her fetus.",
              "विगतविबंधां च → स्त्राताशितां → सायं → तेनैव तैलेनानुवासयेत् → उदावर्त्तोहि समुपेक्षितः → सहसा सगर्भां गर्भिणीमतिपातयेत्."),
        match(2, "Match each word of unit 77 to its meaning.",
              [["विगतविबन्धा", "whose constipation has gone"], ["अशिता", "having eaten"], ["सायम्", "in the evening"],
               ["समुपेक्षित", "neglected"], ["सहसा", "suddenly"]],
              "The conditions for the evening anuvāsana, and the warning about neglect.",
              "विगतविबन्धा, अशिता, सायम्, समुपेक्षित, सहसा.", role="extend",
              teaches="स- at the start of a bahuvrīhi = with: सगर्भा = (a woman) with her fetus."),
        mcq("discriminate", 3, "By unit 77, what would neglected udāvarta do?",
            ("Would suddenly destroy her along with her fetus", "उदावर्तो हि समुपेक्षितः सहसा सगर्भां गर्भिणीमतिपातयेत्."),
            [("Would clear up on its own once the child is born", "The line warns of sudden harm, not a cure."),
             ("Would cause only a mild pain that passes in a day", "The line speaks of destruction, not mild pain."),
             ("Would slowly delay the labour by about a month", "The line says सहसा, suddenly, and names no delay.")],
            "Neglected udāvarta would suddenly destroy the pregnant woman together with her fetus.",
            "समुपेक्षितः ... सहसा ... अतिपातयेत्."),
        multi("apply", 4, "Before the evening anuvāsana, which must be true of her by unit 77?",
              [("Her constipation has gone", "Right: विगतविबन्धाम्."),
               ("She has fasted the whole day", "अशिताम् = having eaten, the opposite."),
               ("She had a nirūha that morning", "No morning nirūha is named in unit 77."),
               ("She has eaten", "Right: अशिताम्, having eaten.")],
              [0, 3],
              "Her constipation has gone and she has eaten (and bathed, on a near-certain reading).",
              "विगतविबन्धाम् ... अशिताम्."),
        mcq("transfer", 5, "By the rule of उदावर्त्तो हि, how is रामः + हसति (Rāma laughs) joined?",
            ("रामो हसति", "अः before a voiced sound (here ह) becomes ओ, as उदावर्तः + हि → उदावर्तो हि."),
            [("रामा हसति", "Dropping the visarga after आ is for आः, not अः."),
             ("रामर्हसति", "र् replaces a visarga after vowels other than अ/आ."),
             ("रामश्हसति", "Visarga becomes श् before च, छ or (optionally) श, not before ह.")],
            "रामः + हसति = रामो हसति, like उदावर्तः + हि = उदावर्तो हि.",
            "अः + voiced consonant → ओ.",
            teaches="अः before a voiced consonant becomes ओ: उदावर्तः + हि → उदावर्तो हि."),
    ],
}

# ---------------------------------------------------------------- unit 78
AUTHORED["78"] = {
    "title": "यस्याः पुनरतिमात्रदोषोपचयात् ... कोष्ठसंक्षोभमापादयति",
    "question": "By unit 78, what releases the fetus from its bond, and what does the freed fetus then do?",
    "rule": ("Excess doṣas, vyavāya and the like, other diseases, or earlier action (karman) of mother and offspring release "
             "the fetus like a fruit from its stalk; it passes the garbhaśayyā, hangs among liver, spleen and intestines, "
             "and disturbs the koṣṭha (belly)."),
    "limits": ("The scope of 'as stated' is not firm; karman is not expanded; garbhaśayyā = womb is probable; 'in the "
               "gaps' is loose; printed मोच्यते may be a slip for मुच्यते. No question rests on these. Continues in unit 79."),
    "explain_hi": ("यह एक लम्बा वाक्य है; मुख्य वाक्य ‘सः’ से आरम्भ होता है। "
                   "जिस स्त्री का गर्भ दोषों के अत्यधिक संचय से, या कहे हुए व्यवाय यानी मैथुन आदि से, या अन्य रोगों से, या माता और "
                   "सन्तान के पहले संचित कर्म से बन्धन से छूट जाता है, जैसे फल डंठल से (फलमिव वृन्तात्)। "
                   "वह छूटा गर्भ गर्भशय्या (सम्भवतः गर्भाशय) को लाँघकर यकृत्, प्लीहा यानी तिल्ली और आँतों के छिद्रों में लटकता हुआ "
                   "कोष्ठ में क्षोभ उत्पन्न करता है। "
                   "‘यथोक्त’ (जैसा कहा) व्यवाय से जुड़ता है या रोगों से, यह पक्का नहीं; कर्म का सिद्धान्त यहाँ नहीं समझाया गया। "
                   "वृत्तान्त अगली इकाई (७९) में चलता है।"),
    "hook": "डंठल से फल-सा छूटा गर्भ: यकृत्-प्लीहा-आँतों में लटके, कोष्ठ हिलाए।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 78, what simile is used for the fetus released from its bond?",
            ("A fruit from its stalk", "फलमिव वृन्तात्: like a fruit from its stalk."),
            [("A leaf blown from a branch", "No leaf is named; the simile is a fruit from its stalk."),
             ("A stone dropped in water", "A stone image is used of the belly in unit 81, not here."),
             ("A lamp running out of oil", "No lamp is named in unit 78.")],
            "The fetus is released like a fruit from its stalk.",
            "फलम् इव वृन्तात्."),
        order(1, "Put these causes and words of unit 78 in the line's order.",
              ["अतिमात्रदोषोपचयात्", "यथोक्तैर्वा व्यवायादिभिः", "अन्यैर्वा व्याधिभिः",
               "पूर्वोपचितेन वा जनन्यपत्ययोः कर्मणा", "बंधनान्मोच्यते गर्भः", "फलमिव वृंतात्"],
              "From excess doṣas, or by vyavāya and the like, or by other diseases, or by earlier action of mother and "
              "offspring, the fetus is released from its bond, like a fruit from its stalk.",
              "अतिमात्रदोषोपचयात् → यथोक्तैर्वा व्यवायादिभिः → अन्यैर्वा व्याधिभिः → पूर्वोपचितेन वा ...कर्मणा → "
              "बंधनान्मोच्यते गर्भः → फलमिव वृंतात्."),
        match(2, "Match each word of unit 78 to its meaning.",
              [["यकृत्", "liver"], ["प्लीह", "spleen"], ["अन्त्र", "intestines"], ["वृन्त", "stalk"],
               ["कोष्ठ", "storehouse, belly"]],
              "Where the freed fetus hangs, the simile's stalk, and what it disturbs.",
              "यकृत्, प्लीह, अन्त्र, वृन्त, कोष्ठ.", role="extend",
              teaches="कोष्ठ = the 'storehouse', the belly: कोष्ठसंक्षोभ = disturbance of the belly."),
        mcq("discriminate", 3, "By unit 78, what does the freed fetus bring about?",
            ("A disturbance of the koṣṭha, the belly", "कोष्ठसंक्षोभमापादयति."),
            [("A quick and easy birth on that day", "No birth is described; the fetus disturbs the koṣṭha."),
             ("A fever with a strong thirst at night", "Fever and thirst are not named in unit 78."),
             ("A bleeding from the nose and mouth", "No such bleeding is named in unit 78.")],
            "The freed fetus brings about a disturbance of the koṣṭha.",
            "कोष्ठसंक्षोभम् आपादयति."),
        multi("apply", 4, "Which does unit 78 name as causes of the release?",
              [("Excessive accumulation of doṣas", "Right: अतिमात्रदोषोपचयात्."),
               ("Cold baths in winter", "No bath or season is named in unit 78."),
               ("Other diseases", "Right: अन्यैर्वा व्याधिभिः."),
               ("Earlier accumulated action of mother and offspring", "Right: पूर्वोपचितेन वा जनन्यपत्ययोः कर्मणा."),
               ("Long fasting", "Fasting is not named in unit 78.")],
              [0, 2, 3],
              "Excess doṣas, other diseases and earlier action of mother and offspring are named (with vyavāya and the like).",
              "दोषोपचय, व्यवायादि, अन्य व्याधि, पूर्वोपचित कर्म."),
        mcq("transfer", 5, "Built like व्यवायादिभिः (by vyavāya and the like), what does स्नानादिभिः mean?",
            ("By bathing and the like", "X-आदि = X and the like, as व्यवाय + आदिभिः."),
            [("By bathing alone, nothing else", "आदि adds 'and the like'; it does not mean alone."),
             ("Without any bathing at all", "आदि does not negate; it widens."),
             ("After the first bath only", "आदि here is 'and the like', not 'first'.")],
            "स्नानादिभिः = by bathing and the like, like व्यवायादिभिः = by vyavāya and the like.",
            "X-आदि = X and the like.",
            teaches="X-आदि = X and the like: व्यवायादिभिः = by vyavāya and the like (अ + आ → आ)."),
    ],
}

# ---------------------------------------------------------------- unit 79
AUTHORED["79"] = {
    "title": "ततः कोष्ठसंक्षोभाद्वायुरपानो ... शोणितभावेन",
    "question": "By unit 79, how does the disturbance of the koṣṭha lead to the loss of the young fetus?",
    "rule": ("Then, from the disturbance of the koṣṭha, the Apāna wind repeatedly brings about pain (in kukṣi, basti (probably the bladder), "
             "sides, belly, yoni), distension (आनाह) and retention of stool and urine, and makes the young (तरुण) fetus fall in "
             "the form of blood."),
    "limits": ("The reach of 'pain' over the five places is a reading, not certain; basti = bladder is probable (basti also "
               "names the enema device). 'In the form of blood' renders शोणितभावेन, literally 'by the state of blood'. "
               "It continues unit 78. A prose line."),
    "explain_hi": ("यह गद्य-पंक्ति इकाई ७८ का वृत्तान्त आगे बढ़ाती है। "
                   "तब (ततः) कोष्ठ के क्षोभ से अपान वायु बार-बार (मुहुः) कुक्षि, बस्ति (सम्भवतः मूत्राशय), पार्श्व, उदर और योनि में "
                   "पीड़ा (शूल), आनाह यानी पेट फूलना, और मल-मूत्र का रुकना (सङ्ग) उत्पन्न करके (आपाद्य) कोमल (तरुण) गर्भ को "
                   "रक्त के रूप में (शोणितभावेन) गिरा देती है (च्यावयति)। "
                   "‘शूल’ पाँचों स्थानों पर लागू होता है, यह एक पाठ है, निश्चित नहीं। "
                   "‘बस्ति’ बस्ति-यन्त्र का नाम भी है; यहाँ मूत्राशय सम्भावित अर्थ है।"),
    "hook": "क्षोभ, फिर अपान: पीड़ा, आनाह, रुकावट; कोमल गर्भ रक्त के रूप में गिरे।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 79, which wind makes the young fetus fall?",
            ("Apāna (अपान)", "वायुरपानः ... गर्भं च्यावयति."),
            [("Prāṇa (प्राण)", "The line names अपान, not prāṇa."),
             ("Udāna (उदान)", "The line names अपान, not udāna."),
             ("Vyāna (व्यान)", "The line names अपान, not vyāna.")],
            "The Apāna wind makes the young fetus fall.",
            "वायुः अपानः."),
        order(1, "Put these parts of unit 79 in the line's order.",
              ["ततः", "कोष्ठसंक्षोभाद्वायुरपानो", "मुहुः", "कुक्षिबस्ति...संगानापाद्य", "गर्भं च्यावयति", "तरुणं शोणितभावेन"],
              "Then, from the disturbance of the koṣṭha, the Apāna wind, repeatedly, having brought about pains and "
              "retentions, makes the fetus fall, young, in the form of blood.",
              "ततः → कोष्ठसंक्षोभाद्वायुरपानो → मुहुः → कुक्षिबस्ति...संगानापाद्य → गर्भं च्यावयति → तरुणं शोणितभावेन."),
        match(2, "Match each word of unit 79 to its meaning.",
              [["आनाह", "distension (standard)"], ["विट् (विण्)", "stool"], ["मूत्र", "urine"], ["सङ्ग", "retention"],
               ["तरुण", "young, tender"], ["शोणित", "blood"]],
              "The signs Apāna brings about, and how the young fetus falls.",
              "आनाह, विट्, मूत्र, सङ्ग, तरुण, शोणित.", role="extend",
              teaches="च्यावयति is the causative of √च्यु (fall away): 'causes to fall'."),
        mcq("discriminate", 3, "Which split of संक्षोभाद्वायुः is right?",
            ("संक्षोभात् + वायुः", "त् before a voiced sound becomes द्."),
            [("संक्षोभाः + वायुः", "आः before a voiced sound drops the visarga: संक्षोभा वायुः."),
             ("संक्षोभम् + वायुः", "म् before a consonant is written ं: संक्षोभं वायुः."),
             ("संक्षोभा + द्वायुः", "द्वायुः is not a word; the word is वायुः.")],
            "संक्षोभात् (from the disturbance) + वायुः (wind): त् + voiced sound → द्.",
            "त् + voiced sound → द्."),
        mcq("apply", 4, "By unit 79, in what form does the young fetus fall?",
            ("In the form of blood", "तरुणं शोणितभावेन: the young fetus, in the form of blood."),
            [("As a fully formed body", "The fetus is called तरुण, young; the line says in the form of blood."),
             ("As a hard, stone-like mass", "A stone image is used of the belly in unit 81, not of the fetus here."),
             ("As clear water only", "The line says शोणित, blood, not water.")],
            "The young fetus falls in the form of blood.",
            "शोणितभावेन = in the form (state) of blood."),
        mcq("transfer", 5, "By the rule of वायुरपानः, how is गुरुः + आगच्छति (the teacher comes) joined?",
            ("गुरुरागच्छति", "उः before a vowel becomes उर्, as वायुः + अपानः → वायुरपानः."),
            [("गुरु आगच्छति", "After उ the visarga does not drop; it becomes र्."),
             ("गुर्वागच्छति", "व् comes from a plain उ before a vowel; here a visarga follows उ."),
             ("गुरोऽगच्छति", "ओऽ comes from अः + अ, and आगच्छति begins with आ.")],
            "गुरुः + आगच्छति = गुरुरागच्छति, like वायुः + अपानः = वायुरपानः.",
            "उः + vowel → उर्.",
            teaches="A visarga after उ becomes र् before a vowel: वायुः + अपानः → वायुरपानः."),
    ],
}

# ---------------------------------------------------------------- unit 80
AUTHORED["80"] = {
    "title": "सोऽभिहितः प्राक्",
    "question": "By unit 80, what does the line say about सः (that)?",
    "rule": ("That (सः) has been stated (अभिहितः) before (प्राक्). The line does not name what सः is."),
    "limits": ("The referent of सः (masculine) is not named; it may be the abortion (garbhasrāva) or the wind, but the text "
               "does not say: no question names it. A prose line."),
    "explain_hi": ("यह बहुत छोटी गद्य-पंक्ति कहती है: वह (सः) पहले (प्राक्) कहा जा चुका है (अभिहितः)। "
                   "‘सः’ पुंलिंग है, पर किसको कहता है, पंक्ति नाम नहीं देती; गर्भस्राव या वायु सम्भव है, पर यह लिखा नहीं। "
                   "यह सम्भवतः इकाई ७९ के वृत्तान्त के बाद की टिप्पणी है। "
                   "‘अभिहित’ अभि-√धा का भूत कृदन्त (क्त) है: कहा गया।"),
    "hook": "सोऽभिहितः प्राक्: बात पहले ही कही जा चुकी।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 80, when has सः (that) been stated?",
            ("Before, earlier (प्राक्)", "सोऽभिहितः प्राक्: it has been stated before."),
            [("Later, further on (पश्चात्)", "The line says प्राक्, before."),
             ("Nowhere at all (न क्वापि)", "The line says it has been stated (अभिहितः)."),
             ("In this very line (अत्र)", "The line says प्राक्, earlier, not here.")],
            "That has been stated before.",
            "प्राक् = before, earlier."),
        order(1, "Put the words of unit 80 in the line's order.",
              ["सः", "अभिहितः", "प्राक्"],
              "That, has been stated, before.",
              "सः → अभिहितः → प्राक्."),
        match(2, "Match each word of unit 80 to its meaning.",
              [["सः", "that (m. nom. sg.)"], ["अभिहित", "stated"], ["प्राक्", "before, earlier"]],
              "That has been stated before.",
              "सः, अभिहित, प्राक्.", role="extend",
              teaches="अभिहित is the past passive participle of अभि-√धा: 'stated, said'."),
        mcq("discriminate", 3, "Which split of सोऽभिहितः is right?",
            ("सः + अभिहितः", "अः + अ → ओऽ: the अ of अभिहितः is dropped and marked ऽ."),
            [("स + अभिहितः", "अ + अ would give साभिहितः, with आ."),
             ("से + अभिहितः", "ए + अ would give सेऽभिहितः, with ए kept."),
             ("सो + भिहितः", "भिहितः is not a word; the word is अभिहितः.")],
            "सः (that) + अभिहितः (stated): अः + अ → ओऽ.",
            "अः + अ → ओऽ."),
        multi("apply", 4, "Which statements about unit 80 are right by the card?",
              [("The line names what सः refers to", "The data: the referent is not named."),
               ("प्राक् means later", "प्राक् means before, earlier."),
               ("अभिहित is a past passive participle: stated", "Right: ppp of अभि-√धा."),
               ("सः is masculine, but its referent is not named", "Right: the text does not say what has been stated.")],
              [2, 3],
              "अभिहित is a past participle, and what सः means is not named.",
              "सोऽभिहितः प्राक्: referent not named."),
        mcq("transfer", 5, "By the rule of सोऽभिहितः, how is देवः + अयम् (this god) joined?",
            ("देवोऽयम्", "अः + अ → ओऽ, as सः + अभिहितः → सोऽभिहितः."),
            [("देवायम्", "आ would come from अ + अ without a visarga."),
             ("देव अयम्", "अः drops to अ before other vowels; before अ it becomes ओऽ."),
             ("देवेऽयम्", "एऽ comes from ए + अ, not from अः + अ.")],
            "देवः + अयम् = देवोऽयम्, like सः + अभिहितः = सोऽभिहितः.",
            "अः + अ → ओऽ.",
            teaches="अः followed by अ becomes ओ and the अ is dropped (ऽ): सः + अभिहितः → सोऽभिहितः."),
    ],
}

# ---------------------------------------------------------------- unit 81
AUTHORED["81"] = {
    "title": "विवृद्धे तु गर्भेस्तब्धं ... उदरमाभाति",
    "question": "By unit 81, how does the belly appear when the fetus has grown?",
    "rule": ("But when the fetus has grown (विवृद्धे गर्भे), the belly (उदर) appears (आभाति) stiff (स्तब्ध), still "
             "(स्तिमित), cold (शीत), as if it had a stone inside (अश्मगर्भम् इव)."),
    "limits": ("The unit does not say which case it describes (the dead fetus of unit 82 is likely, not stated): no question "
               "links them. स्तिमित may also mean 'wet' (not chosen): no question rests on it. Printed गर्भेस्तब्धं joins two "
               "words by a spacing slip. A prose line."),
    "explain_hi": ("यह गद्य-पंक्ति पेट का रूप बताती है। "
                   "पर (तु) गर्भ के बढ़ जाने पर (विवृद्धे गर्भे) पेट (उदरम्) कठोर (स्तब्धम्), स्थिर (स्तिमितम्), ठण्डा (शीतम्) और "
                   "मानो भीतर पत्थर वाला (अश्मगर्भम् इव) दिखाई देता है (आभाति)। "
                   "‘विवृद्धे गर्भे’ सति-सप्तमी है: गर्भ के बढ़ जाने पर। "
                   "यह किस अवस्था की बात है, यहाँ नहीं कहा; अगली इकाई (८२) का मृत गर्भ सम्भव है, पर लिखा नहीं। "
                   "‘स्तिमित’ का अर्थ ‘गीला’ भी हो सकता है; यहाँ ‘स्थिर’ लिया गया।"),
    "hook": "बढ़ा गर्भ, पेट पत्थर-सा: कठोर, स्थिर, ठण्डा।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 81, the belly appears as if it had what inside?",
            ("A stone (अश्म)", "अश्मगर्भमिव: as if with a stone inside."),
            [("Water (उदक)", "No water is named; the simile is a stone."),
             ("A flame (अग्नि)", "No fire is named; the belly is cold (शीत)."),
             ("A wind (वायु)", "No wind is named in unit 81; the simile is a stone.")],
            "The belly appears as if it had a stone inside.",
            "अश्म-गर्भम् इव = as if stone-interiored."),
        order(1, "Put these parts of unit 81 in the line's order.",
              ["विवृद्धे तु गर्भे", "स्तब्धं", "स्तिमितं", "शीतम्", "अश्मगर्भमिव", "उदरमाभाति"],
              "When the fetus has grown, stiff, still, cold, as if with a stone inside, the belly appears.",
              "विवृद्धे तु गर्भे → स्तब्धं → स्तिमितं → शीतम् → अश्मगर्भमिव → उदरमाभाति."),
        match(2, "Match each word of unit 81 to its meaning.",
              [["विवृद्ध", "grown"], ["स्तब्ध", "stiff, rigid"], ["शीत", "cold"], ["अश्म", "stone"], ["आभाति", "appears"]],
              "The grown fetus, and the stiff, cold, stone-like belly.",
              "विवृद्ध, स्तब्ध, शीत, अश्म, आभाति.", role="extend",
              teaches="A locative absolute: विवृद्धे गर्भे (both locative) = when the fetus has grown."),
        mcq("discriminate", 3, "Which split of इवोदरम् is right?",
            ("इव + उदरम्", "अ + उ → ओ: इव (as if) + उदरम् (belly)."),
            [("इवः + उदरम्", "इव has no visarga, and अः before उ would stay apart: इव उदरम्."),
             ("इवो + दरम्", "दरम् is not the word here; the word is उदरम्, belly."),
             ("इवे + उदरम्", "ए before उ would give इवयुदरम् or इव उदरम्, not ओ.")],
            "इव (as if) + उदरम् (belly): अ + उ → ओ.",
            "अ + उ → ओ."),
        mcq("apply", 4, "A belly is stiff, still and cold, as if with a stone inside. By unit 81, when does it look so?",
            ("When the fetus has grown", "विवृद्धे तु गर्भे: when the fetus has grown."),
            [("Right after conception", "The line says when the fetus has grown, not at conception."),
             ("After the fetus is delivered", "The line speaks of a grown fetus still inside."),
             ("Only in the first month", "No month is named; the fetus has grown.")],
            "The belly looks so when the fetus has grown.",
            "विवृद्धे गर्भे = when the fetus has grown."),
        mcq("transfer", 5, "Built like विवृद्धे गर्भे (when the fetus has grown), what does उदिते सूर्ये mean?",
            ("When the sun has risen", "Noun and participle both in the locative: 'when the sun has risen'."),
            [("Before the sun rises", "उदिते is a past participle: has risen, not before rising."),
             ("Because of the sun", "A locative absolute gives 'when', not 'because of'."),
             ("Facing the eastern sun", "No direction is in उदिते सूर्ये.")],
            "उदिते सूर्ये = when the sun has risen, like विवृद्धे गर्भे = when the fetus has grown.",
            "Locative noun + locative participle = when X has ...",
            teaches="A locative absolute (noun and participle both locative) gives 'when X has ...': विवृद्धे गर्भे."),
    ],
}


# ===================================================================== NOTES_HI
NOTES_HI = {
    "69": ("गद्य; विश्वास उच्च; कोई पाठ-चिह्न नहीं। वाक्य सम्भवतः इकाई ६७-६८ (लीन गर्भ) का क्रम आगे बढ़ाता है। "
           "‘बिल्वशलाटु’ को एक वस्तु (बेल का कच्चा फल) भी पढ़ा जा सकता है; चार-वस्तु पाठ शब्दशः है; संख्या पर प्रश्न नहीं। "
           "सक्तु का अन्न नहीं कहा (जौ सामान्य, पर लिखा नहीं)। ‘पाययेत्’ = पिलाए (प्रेरणार्थक)। "
           "सन्धि जाँची: सक्तून् + वा → सक्तून्वा (कोई परिवर्तन नहीं, केवल जुड़ा लिखा); "
           "तिल-माष-बिल्व-शलाटु-युक्तान् समास में स्वर-सन्धि नहीं; युक्तान् + पयसा → युक्तान् पयसा।"),
    "70": ("गद्य; विश्वास मध्यम। पाठ-चिह्न: छपा ‘मार्द्दीकं’ → ‘मार्द्वीकं’ (लगभग निश्चित; द्व का द्द पढ़ा जाना; इकाई ७६ में "
           "‘मृद्वीकानां’ ठीक छपा है)। ‘मेद्य’ = चर्बीयुक्त (सम्भावित); ‘मेध्य’ (बुद्धिवर्धक) भी सम्भव, पर मांस के साथ कम उचित। "
           "पंक्ति में क्रिया नहीं; इकाई ६९ की ‘पाययेत्’ चली आती है। प्रश्नों में ‘मेद्य’ केवल ‘सम्भावित’ लेबल के साथ और सुधार केवल ‘लगभग निश्चित’ के रूप में आते हैं; ‘मेद्य’ का निश्चित अर्थ कोई प्रश्न नहीं पूछता। "
           "सन्धि जाँची: मांस + उपदंशम् → मांसोपदंशम् (अ + उ → ओ); उपदंशम् + वा → उपदंशं वा (व्यंजन से पहले म् → अनुस्वार)।"),
    "71": ("गद्य; विश्वास उच्च; कोई पाठ-चिह्न नहीं। सम्भवतः इकाई ६७-७० के उपचार का क्रम। तेल का प्रकार नहीं कहा। "
           "छपा ‘वंक्षण’ = वङ्क्षण, ‘अभ्यंज्यात्’ = अभ्यञ्ज्यात् (अनुस्वार वर्तनी)। "
           "सन्धि जाँची: च + अभीक्ष्णम् → चाभीक्ष्णम् (अ + अ → आ); अभीक्ष्णम् + उदर → अभीक्ष्णमुदर (म् स्वर से जुड़ता है); "
           "वङ्क्षण + ऊरु → वङ्क्षणोरु (अ + ऊ → ओ); पृष्ठानि + अभ्यञ्ज्यात् → पृष्ठान्यभ्यञ्ज्यात् (इ + अ → य)।"),
    "72": ("गद्य; विश्वास उच्च; कोई पाठ-चिह्न नहीं। सम्भवतः इकाई ७१ के बाद का अंग। किस उपाय से हर्षित करे, नहीं कहा; "
           "‘हर्षयेत्’ का सरल अर्थ (प्रसन्न करे) रखा। "
           "सन्धि जाँची: मुहुः + मुहुः → मुहुर्मुहुः (उः + घोष → उर्); मुहुः + च → मुहुश्च (विसर्ग + च → श्); "
           "च + एनाम् → चैनाम् (अ + ए → ऐ); एनाम् + हर्षयेत् → एनां हर्षयेत् (व्यंजन से पहले म् → अनुस्वार)।"),
    "73": ("गद्य; विश्वास मध्यम; कोई पाठ-चिह्न नहीं। सम्भवतः इकाई ६७-७२ के लीन-उपचार को समाप्त करती है। "
           "‘पूर्वोक्त’ किसे कहता है, पंक्ति में नहीं; इस पर प्रश्न नहीं। "
           "सन्धि जाँची: पूर्व + उक्तम् → पूर्वोक्तम् (अ + उ → ओ); पूर्वोक्तम् + च → पूर्वोक्तं च (व्यंजन से पहले अनुस्वार); "
           "च + ईक्षेत → चेक्षेत (अ + ई → ए)।"),
    "74": ("गद्य; विश्वास उच्च; कोई पाठ-चिह्न नहीं। सम्भवतः नया विषय। ‘उदावर्तविबन्धः’ दो प्रकार से पढ़ा जा सकता है: दो रोग "
           "(द्वन्द्व) या ‘उदावर्त प्रकार का विबन्ध’; डेटा पहला लेता है; किसी पाठ को चुनने वाला प्रश्न नहीं। ‘वातहर’ और ‘स्निग्ध’ "
           "दोनों अन्न-पान के विशेषण। छपा ‘उदावर्त्त’ (र्त्त) छपाई की सामान्य वर्तनी। "
           "सन्धि जाँची: पुनर् + उदावर्त → पुनरुदावर्त (पुनर् का र् स्वर से जुड़ता है); स्यात् + ताम् → स्यात्ताम्; "
           "ताम् + वात → तां वात (अनुस्वार); स्निग्ध + अन्न → स्निग्धान्न (अ + अ → आ); पानैः + उपाचरेत् → पानैरुपाचरेत् "
           "(ऐः + स्वर → ऐर्); उप + आचरेत् → उपाचरेत् (अ + आ → आ)।"),
    "75": ("गद्य; विश्वास मध्यम; कोई पाठ-चिह्न नहीं। सम्भवतः इकाई ७४ का क्रम। ‘आठवाँ मास’ गर्भ का समझा जाता है, पंक्ति में नहीं "
           "कहा। मधुरक: सम्भवतः मधुर औषधों का समूह (निश्चित नहीं, विवादित); सदस्य यहाँ नहीं गिनाए; इन पर प्रश्न नहीं। "
           "सन्धि जाँची: तैलेन + अनुवासयेत् → तैलेनानुवासयेत् (अ + अ → आ)। अष्टमे तु मासे में कोई सन्धि नहीं।"),
    "76": ("गद्य; विश्वास मध्यम। पाठ-चिह्न: (१) छपा ‘इक्षुबालिकावेेतस’ → ‘इक्षुवालिकावेतस’ (वेतस के लिए लगभग निश्चित, फालतू "
           "ए; ब/व की अदला-बदली इस छपाई में सामान्य); (२) छपा ‘भूतिकांनंत’ → ‘भूतिकानन्त’ (सम्भावित: फालतू अनुस्वार; ‘अनन्त’ "
           "अनुमानित पाठ)। पहचान: वीरण सम्भावित (खस की घास); शालि, कुश, काश, काश्मर्य, परूषक, मृद्वीका, बिभीतक मानक; मधुक "
           "सम्भवतः मुलेठी; पियाल सम्भावित; अनन्त सम्भावित (सारिवा) पर पाठ अनुमानित; इक्षुवालिका, वेतस विवादित; परिव्याध, भूतिका "
           "अज्ञात। ‘मूलानाम्’ पहले समूह से जुड़ा; दूसरा समूह जड़ें हैं या पूरी औषधि, तय नहीं। ‘तदसिद्धौ’ का ‘तत्’ = अनुवासन, "
           "प्रसंग से। इन पर प्रश्न नहीं। "
           "सन्धि जाँची: तत् + असिद्धौ → तदसिद्धौ (त् + स्वर → द्); भूतिका + अनन्त → भूतिकानन्त (आ + अ → आ); "
           "पयसा + अर्ध → पयसार्ध (आ + अ → आ; छपा ‘पयसाऽर्द्ध’ में ऽ केवल लिपि-चिह्न); अर्ध + उदकेन → अर्धोदकेन (अ + उ → ओ); "
           "उदकेन + उद्धृत्य → उदकेनोद्धृत्य (अ + उ → ओ); युक्तेन + ईषत् → युक्तेनेषत् (अ + ई → ए); ईषत् + लवण → ईषल्लवण "
           "(त् + ल → ल्ल); लवण + उष्णेन → लवणोष्णेन (अ + उ → ओ)।"),
    "77": ("दो छपी पंक्तियाँ (02.04.80, 02.04.81); विश्वास मध्यम। पाठ-चिह्न: छपा ‘स्त्राताशितां’ → ‘स्नाताशितां’ (लगभग निश्चित; "
           "‘स्त्रात’ शब्द नहीं; जैसे इकाई ५२ में)। ‘तेनैव तैलेन’ = इकाई ७५ का मधुरक-तेल, यह प्रसंग से, शब्दों में नहीं। "
           "‘अतिपातयेत्’ = नष्ट करे (सरल अर्थ); ‘गर्भपात कराए’ संकरा सम्भव अर्थ; इनमें चुनने वाला प्रश्न नहीं। छपा ‘उदावर्त्तो’ "
           "(र्त्त) सामान्य वर्तनी। "
           "सन्धि जाँची: विगतविबन्धाम् + च → विगतविबन्धां च (अनुस्वार); स्नात + अशिताम् → स्नाताशिताम् (अ + अ → आ); "
           "सायम् + तेन → सायं तेन; तेन + एव → तेनैव (अ + ए → ऐ); तैलेन + अनुवासयेत् → तैलेनानुवासयेत्; "
           "उदावर्तः + हि → उदावर्तो हि (अः + घोष → ओ); गर्भिणीम् + अतिपातयेत् → गर्भिणीमतिपातयेत्।"),
    "78": ("गद्य; विश्वास मध्यम। पाठ-चिह्न: छपा ‘मोच्यते’ → सम्भवतः ‘मुच्यते’ (√मुच् का कर्मवाच्य; गुण वाला रूप छपाई की भूल "
           "या पुराना पाठान्तर)। ‘यथोक्तैः’ व्यवाय से जुड़ता है या रोगों से, पक्का नहीं। गर्भशय्या = सम्भवतः गर्भाशय। ‘विवरैः’ "
           "का ‘छिद्रों में’ अनुवाद ढीला है। कर्म का सिद्धान्त नहीं खोला गया। इन पर प्रश्न नहीं। वाक्य इकाई ७९ में चलता है। "
           "सन्धि जाँची: पुनर् + अतिमात्र → पुनरतिमात्र; उपचयात् + यथा → उपचयाद्यथा (त् + घोष → द्); यथा + उक्तैः → यथोक्तैः "
           "(आ + उ → ओ); उक्तैः + वा → उक्तैर्वा (ऐः + घोष → ऐर्); व्यवाय + आदिभिः → व्यवायादिभिः (अ + आ → आ); "
           "आदिभिः + अन्यैः → आदिभिरन्यैः (इः + स्वर → इर्); पूर्व + उपचितेन → पूर्वोपचितेन (अ + उ → ओ); जननी + अपत्ययोः → "
           "जनन्यपत्ययोः (ई + अ → य); बन्धनात् + मुच्यते → बन्धनान्मुच्यते (यहाँ अनुनासिक से पहले त् का न् लिखा; विकल्प से, द् भी शुद्ध); फलम् + इव → "
           "फलमिव; सः + मुक्त → स मुक्त (व्यंजन से पहले सः का विसर्ग लोप); मुक्तबन्धनः + गर्भ → मुक्तबन्धनो गर्भ (अः + घोष → ओ); "
           "प्लीह + अन्त्र → प्लीहान्त्र (अ + अ → आ); विवरैः + वा → विवरैर्वा; वा + अवलम्बमानः → वावलम्बमानः (आ + अ → आ)।"),
    "79": ("गद्य; विश्वास मध्यम; कोई पाठ-चिह्न नहीं। इकाई ७८ का क्रम। ‘शूल’ पाँचों स्थानों (कुक्षि, बस्ति, पार्श्व, उदर, योनि) पर "
           "लागू होता है, यह एक पाठ है, निश्चित नहीं। बस्ति = मूत्राशय सम्भावित (बस्ति-यन्त्र का नाम भी)। आनाह = पेट फूलना, मल व "
           "वायु का रुकना (मानक)। ‘शोणितभावेन’ शब्दशः ‘रक्त की अवस्था से’। "
           "सन्धि जाँची: संक्षोभात् + वायुः → संक्षोभाद्वायुः (त् + घोष → द्); वायुः + अपानः → वायुरपानः (उः + स्वर → उर्); "
           "अपानः + मुहुः → अपानो मुहुः (अः + घोष → ओ); पार्श्व + उदर → पार्श्वोदर (अ + उ → ओ); शूल + आनाह → शूलानाह (अ + आ → आ); "
           "विट् + मूत्र → विण्मूत्र (यहाँ अनुनासिक से पहले ट् का ण् लिखा); सङ्गान् + आपाद्य → सङ्गानापाद्य।"),
    "80": ("गद्य; विश्वास मध्यम; कोई पाठ-चिह्न नहीं। ‘सः’ (पुंलिंग) किसे कहता है, पंक्ति में नाम नहीं (गर्भस्राव या वायु सम्भव, "
           "लिखा नहीं); इस पर प्रश्न नहीं। सम्भवतः इकाई ७९ के बाद। "
           "सन्धि जाँची: सः + अभिहितः → सोऽभिहितः (अः + अ → ओऽ)।"),
    "81": ("गद्य; विश्वास मध्यम; कोई पाठ-चिह्न नहीं। छपा ‘गर्भेस्तब्धं’ = गर्भे + स्तब्धम् (केवल रिक्त स्थान छूटा)। "
           "‘स्तिमित’ = स्थिर लिया; ‘गीला’ भी अर्थ हो सकता है। यह इकाई किस अवस्था की है, यहाँ नहीं कहा (इकाई ८२ का मृत गर्भ सम्भव); "
           "इन पर प्रश्न नहीं। "
           "सन्धि जाँची: शीतम् + अश्म → शीतमश्म; अश्मगर्भम् + इव → अश्मगर्भमिव; इव + उदरम् → इवोदरम् (अ + उ → ओ); "
           "उदरम् + आभाति → उदरमाभाति (म् स्वर से जुड़ता है)।"),
}


# ===================================================================== AIDS
AIDS = {
    "69": {
        "diagram": {"groups": [
            {"label": "सक्तु (भुने अन्न का आटा) से युक्त (बिल्व-शलाटु एक वस्तु भी पढ़ा जा सकता है)",
             "items": ["तिल", "माष (उड़द)", "बिल्व (बेल)", "शलाटु (कच्चा फल)"]},
            {"label": "कैसे दें", "items": ["दूध के साथ (पयसा)", "पिलाए (पाययेत्)"]}]},
        "chunks": "सक्तून्वा | तिलमाषबिल्वशलाटुयुक्तान् | पयसा | पाययेत्",
        "frame": "क्या: सक्तून् (भुने अन्न का आटा; अन्न नहीं कहा) → किससे युक्त: तिल, माष, बिल्व, शलाटु → किसके साथ: पयसा (दूध) "
                 "→ क्रिया: पाययेत् (पिलाए)।",
    },
    "70": {
        "chunks": "मेद्यमांसोपदंशं | वा | मार्द्दीकं (= मार्द्वीकम्)",
        "sandhi": "अ + उ → ओ: मांस + उपदंशम् → मांसोपदंशम् · व्यंजन से पहले म् → ं: उपदंशम् + वा → उपदंशं वा।",
        "frame": "विकल्प: वा → पेय: मार्द्वीक (अंगूर की मदिरा; सुधारा पाठ, लगभग निश्चित) → साथ खाने को (उपदंश): मांस, "
                 "सम्भवतः चर्बीयुक्त → क्रिया: इकाई ६९ की ‘पाययेत्’ चली आती है।",
    },
    "71": {
        "diagram": {"groups": [
            {"label": "तेल से बार-बार अभ्यंग (क्रम से)", "items": ["१ उदर (पेट)", "२ वंक्षण (जाँघ का जोड़)", "३ ऊरु (जाँघ)",
                                                                "४ कटी (कमर)", "५ पार्श्व (बगल)", "६ पृष्ठ (पीठ)"]}]},
        "chunks": "तैलेन | चाभीक्ष्णम् | उदरवंक्षणोरुकटीपार्श्वपृष्ठानि | अभ्यंज्यात्",
        "sandhi": "अ + अ → आ: च + अभीक्ष्णम् → चाभीक्ष्णम् · अ + ऊ → ओ: वंक्षण + ऊरु → वंक्षणोरु · इ + अ → य: "
                  "पृष्ठानि + अभ्यञ्ज्यात् → पृष्ठान्यभ्यञ्ज्यात्।",
    },
    "72": {
        "chunks": "मुहुर्मुहुश्चैनां | हर्षयेत्",
        "sandhi": "उः + घोष → उर्: मुहुः + मुहुः → मुहुर्मुहुः · विसर्ग + च → श्: मुहुः + च → मुहुश्च · अ + ए → ऐ: "
                  "च + एनाम् → चैनाम्।",
        "anchors": "याद-सूत्र: इकाई ७१ में तन पर तेल, इकाई ७२ में मन में हर्ष। (मेरी याद-पद्धति)",
    },
    "73": {
        "chunks": "पूर्वोक्तं | चेक्षेत",
        "sandhi": "अ + उ → ओ: पूर्व + उक्तम् → पूर्वोक्तम् · अ + ई → ए: च + ईक्षेत → चेक्षेत।",
        "anchors": "याद-सूत्र: ‘पूर्व + उक्त’ = पहले कहा; लीन-उपचार का समापन-वाक्य: जो पहले कहा, उसे देखते रहो। (मेरी याद-पद्धति; "
                   "‘पहले कहा’ किसे कहता है, पंक्ति नहीं बताती)",
    },
    "74": {
        "chunks": "यस्याः पुनरुदावर्त्तविबंधः स्यात् | तां | वातहरस्निग्धान्नपानैः | उपाचरेत्",
        "sandhi": "अ + अ → आ: स्निग्ध + अन्न → स्निग्धान्न · ऐः + स्वर → ऐर्: पानैः + उपाचरेत् → पानैरुपाचरेत् · "
                  "अ + आ → आ: उप + आचरेत् → उपाचरेत्।",
        "frame": "किसको: यस्याः ... स्यात् (जिसे उदावर्त और विबन्ध हो; एक रोग या दो, खुला) → किससे: अन्न-पान जो वात हरें और "
                 "चिकने हों → क्रिया: उपाचरेत् (उपचार करे)।",
    },
    "75": {
        "chunks": "अष्टमे तु मासे | मधुरकसिद्धेन | तैलेनानुवासयेत्",
        "sandhi": "अ + अ → आ: तैलेन + अनुवासयेत् → तैलेनानुवासयेत्।",
        "frame": "कब: अष्टमे मासे (आठवें मास में; गर्भ का, समझा जाता है) → किससे: मधुरक से पका तेल (मधुरक सम्भवतः मधुर औषधों का "
                 "समूह) → क्या: अनुवासन (चिकनाई वाली बस्ति)।",
    },
    "76": {
        "diagram": {"groups": [
            {"label": "पहला समूह: इनकी जड़ें", "items": ["वीरण (सम्भवतः खस)", "शालि (धान)", "कुश", "काश (काँस)",
                                                       "इक्षुवालिका (विवादित)", "वेतस (विवादित)", "परिव्याध (अज्ञात)"]},
            {"label": "दूसरा समूह (जड़ या पूरी, तय नहीं)", "items": ["भूतिका (अज्ञात)", "अनन्त (अनुमानित पाठ)",
                                                                  "काश्मर्य (गम्भारी)", "परूषक (फालसा)",
                                                                  "मधुक (सम्भवतः मुलेठी)", "मृद्वीका (अंगूर)"]}]},
        "chain": {"steps": ["उसके सिद्ध न होने पर (तदसिद्धौ)", "दोनों समूहों का रस दूध और आधे जल से निकाले",
                            "उसमें पियाल-बिभीतक की गिरी और तिल का कल्क मिलाए", "थोड़ा नमकीन और गरम",
                            "निरूह दे (निरूहयेत्)"]},
        "chunks": "तदसिद्धौ | वीरणशालिकुशकाशेक्षुबालिकावेेतसपरिव्याधमूलानां | भूतिकांनंतकाश्मर्यपरूषकमधुकमृद्वीकानां च | "
                  "पयसाऽर्द्धोदकेनोद्धृत्य रसं | तेन पियालबिभीतकमज्जतिलकल्कयुक्तेनेषल्लवणोष्णेन | निरूहयेत्",
        "sandhi": "त् + स्वर → द्: तत् + असिद्धौ → तदसिद्धौ · अ + उ → ओ: अर्ध + उदकेन → अर्धोदकेन · अ + ई → ए: "
                  "युक्तेन + ईषत् → युक्तेनेषत् · त् + ल → ल्ल: ईषत् + लवण → ईषल्लवण।",
    },
    "77": {
        "chain": {"steps": ["शर्तें: कब्ज दूर हो (विगतविबन्धा), नहा चुकी (सुधारा पाठ), खा चुकी", "सायंकाल",
                            "उसी तेल से अनुवासन"]},
        "chunks": "विगतविबंधां च | स्त्राताशितां (= स्नाताशिताम्) | सायं तेनैव तैलेनानुवासयेत् || उदावर्त्तोहि समुपेक्षितः | "
                  "सहसा सगर्भां गर्भिणीमतिपातयेत्",
        "sandhi": "अ + ए → ऐ: तेन + एव → तेनैव · अ + अ → आ: तैलेन + अनुवासयेत् → तैलेनानुवासयेत् · अः + घोष → ओ: "
                  "उदावर्तः + हि → उदावर्तो हि।",
    },
    "78": {
        "diagram": {"groups": [
            {"label": "कारण (कोई एक: वा)", "items": ["दोषों का अत्यधिक संचय", "कहे हुए व्यवाय आदि", "अन्य रोग",
                                                  "माता और सन्तान का पूर्व-संचित कर्म"]},
            {"label": "फिर (क्रम से)", "items": ["गर्भ बन्धन से छूटे, जैसे फल डंठल से", "गर्भशय्या (सम्भवतः गर्भाशय) को लाँघे",
                                               "यकृत्, प्लीहा, आँतों के बीच लटके", "कोष्ठ में क्षोभ"]}]},
        "chunks": "यस्याः पुनरतिमात्रदोषोपचयाद्यथोक्तैर्वा व्यवायादिभिरन्यैर्वा व्याधिभिः | पूर्वोपचितेन वा जनन्यपत्ययोः कर्मणा | "
                  "बंधनान्मोच्यते गर्भः फलमिववृंतात् | स मुक्तबंधनो गर्भशय्यामतिक्रम्य | यकृत्प्लीहान्त्रविवरैर्वावलंबमानः | "
                  "कोष्ठसंक्षोभमापादयति",
        "sandhi": "त् + घोष → द्: उपचयात् + यथा → उपचयाद्यथा · आ + उ → ओ: यथा + उक्तैः → यथोक्तैः · ई + अ → य: "
                  "जननी + अपत्ययोः → जनन्यपत्ययोः · म् + स्वर: फलम् + इव → फलमिव।",
    },
    "79": {
        "chain": {"steps": ["कोष्ठ में क्षोभ", "अपान वायु", "बार-बार शूल, आनाह, मल-मूत्र का रुकना", "कोमल गर्भ को गिराए",
                            "रक्त के रूप में"]},
        "chunks": "ततः कोष्ठसंक्षोभाद्वायुरपानो मुहुः | कुक्षिबस्तिपार्श्वोदरयोनिशूलानाहविण्मूत्रसंगानापाद्य | गर्भं च्यावयति | "
                  "तरुणं शोणितभावेन",
        "sandhi": "त् + घोष → द्: संक्षोभात् + वायुः → संक्षोभाद्वायुः · उः + स्वर → उर्: वायुः + अपानः → वायुरपानः · "
                  "अः + घोष → ओ: अपानः + मुहुः → अपानो मुहुः।",
    },
    "80": {
        "chunks": "सोऽभिहितः | प्राक्",
        "sandhi": "अः + अ → ओऽ: सः + अभिहितः → सोऽभिहितः।",
        "anchors": "याद-सूत्र: ‘प्राक्’ = पहले: जो बात पीछे कही जा चुकी, उसकी ओर इशारा; क्या कहा गया, पंक्ति नहीं बताती। (मेरी याद-पद्धति)",
    },
    "81": {
        "diagram": {"groups": [
            {"label": "गर्भ बढ़ जाने पर पेट", "items": ["स्तब्ध: कठोर", "स्तिमित: स्थिर", "शीत: ठण्डा",
                                                       "मानो भीतर पत्थर (अश्मगर्भम् इव)"]}]},
        "chunks": "विवृद्धे तु गर्भे | स्तब्धं स्तिमितं शीतम् | अश्मगर्भमिव | उदरमाभाति",
        "sandhi": "अ + उ → ओ: इव + उदरम् → इवोदरम् · म् + स्वर: अश्मगर्भम् + इव → अश्मगर्भमिव; उदरम् + आभाति → उदरमाभाति।",
    },
}


# ===================================================================== IMAGE_SPECS
IMAGE_SPECS = {
    ("69", "diagram"): {
        "file": "sh4-saktu-paya-69.svg",
        "alt": ("Flowchart of unit 69: saktu (flour of roasted grain) combined with sesame, black gram, bilva (bael) and "
                "śalāṭu (unripe fruit; bilva-śalāṭu may also be one item), given with milk to drink."),
        "type": "mermaid",
        "code": ("flowchart TD\n"
                 "  B[\"तिल\"] ---> A\n"
                 "  C[\"माष (उड़द)\"] ---> A\n"
                 "  D[\"बिल्व (बेल)\"] --> A\n"
                 "  E[\"शलाटु<br/>(कच्चा फल)\"] --> A\n"
                 "  B ~~~ D\n"
                 "  C ~~~ E\n"
                 "  A[\"सक्तु: भुने<br/>अन्न का आटा\"] --> F[\"दूध के साथ\"]\n"
                 "  F --> G[\"पिलाए\"]\n"
                 "  D -.- H[\"बिल्व-शलाटु:<br/>एक भी सम्भव\"]\n"
                 "  E -.- H\n"),
    },
    ("71", "diagram"): {
        "file": "sh4-abhyanga-anga-71.svg",
        "alt": ("Table of unit 71: the six body parts anointed repeatedly with oil, in line order: belly, groin, thigh, "
                "waist, flank, back."),
        "type": "table",
        "title": "इकाई ७१: तेल से बार-बार अभ्यंग",
        "heads": ["छपा शब्द", "अंग"],
        "rows": [["१ उदर", "पेट"], ["२ वंक्षण", "जाँघ का जोड़"], ["३ ऊरु", "जाँघ"], ["४ कटी", "कमर"],
                 ["५ पार्श्व", "बगल"], ["६ पृष्ठ", "पीठ"]],
    },
    ("76", "diagram"): {
        "file": "sh4-niruha-dravya-76.svg",
        "alt": ("Two columns of unit 76. Roots of: vīraṇa (probably vetiver), śāli (rice), kuśa, kāśa (kans grass), "
                "ikṣuvālikā (disputed), vetasa (disputed), parivyādha (unidentified). Second group, roots or whole not "
                "settled: bhūtikā (unidentified), ananta (conjectural reading), kāśmarya (gmelina), parūṣaka (phalsa), "
                "madhuka (probably licorice), mṛdvīkā (grape)."),
        "type": "split",
        "title": "इकाई ७६: निरूह के दो द्रव्य-समूह",
        "cols": [["पहला समूह: जड़ें", ["वीरण (सम्भवतः खस)", "शालि (धान)", "कुश", "काश (काँस)", "इक्षुवालिका (विवादित)",
                                        "वेतस (विवादित)", "परिव्याध (अज्ञात)"]],
                 ["दूसरा समूह (जड़ या पूरी?)", ["भूतिका (अज्ञात)", "अनन्त (अनुमानित पाठ)", "काश्मर्य (गम्भारी)",
                                                "परूषक (फालसा)", "मधुक (सम्भवतः मुलेठी)", "मृद्वीका (अंगूर)"]]],
    },
    ("77", "chain"): {
        "file": "sh4-sayam-anuvasana-77.svg",
        "alt": ("Chain of unit 77: conditions on her (constipation gone; bathed, a near-certain reading; eaten); in the "
                "evening; an anuvāsana with that very oil."),
        "type": "chain",
        "title": "इकाई ७७: सायंकाल अनुवासन",
        "steps": ["शर्तें: कब्ज दूर हो, नहा चुकी (सुधारा पाठ), खा चुकी", "सायंकाल", "उसी तेल से अनुवासन"],
    },
    ("78", "diagram"): {
        "file": "sh4-garbha-mukti-78.svg",
        "alt": ("Flowchart of unit 78: any one of four causes (excess doṣa accumulation; vyavāya and the like, as stated; "
                "other diseases; earlier action of mother and offspring) releases the fetus from its bond like a fruit from "
                "its stalk; it passes the garbhaśayyā (probably the womb), hangs among liver, spleen and intestines, and "
                "disturbs the koṣṭha."),
        "type": "mermaid",
        "code": ("flowchart TD\n"
                 "  A[\"दोषों का<br/>अत्यधिक संचय\"] ---> E\n"
                 "  B[\"कहे हुए<br/>व्यवाय आदि\"] ---> E\n"
                 "  C[\"अन्य रोग\"] --> E\n"
                 "  D[\"माता-सन्तान का<br/>पूर्व कर्म\"] --> E\n"
                 "  A ~~~ C\n"
                 "  B ~~~ D\n"
                 "  E[\"गर्भ बन्धन से छूटे\"] -.- F[\"जैसे फल<br/>डंठल से\"]\n"
                 "  E --> G[\"गर्भशय्या को लाँघे\"]\n"
                 "  G --> H[\"यकृत्, प्लीहा,<br/>आँतों में लटके\"]\n"
                 "  H --> I[\"कोष्ठ में क्षोभ\"]\n"),
    },
    ("79", "chain"): {
        "file": "sh4-apana-chyuti-79.svg",
        "alt": ("Chain of unit 79: disturbance of the koṣṭha; the Apāna wind; repeated pain, distension (ānāha) and "
                "retention of stool and urine; it makes the young fetus fall; in the form of blood."),
        "type": "chain",
        "title": "इकाई ७९: अपान से गर्भ-च्युति",
        "steps": ["कोष्ठ में क्षोभ", "अपान वायु", "बार-बार शूल, आनाह, मल-मूत्र रुके", "कोमल गर्भ को गिराए",
                  "रक्त के रूप में"],
    },
    ("81", "diagram"): {
        "file": "sh4-ashmagarbha-81.svg",
        "alt": ("Table of unit 81: when the fetus has grown, the belly appears stiff, still, cold, and as if it had a "
                "stone inside."),
        "type": "table",
        "title": "इकाई ८१: गर्भ बढ़ने पर पेट",
        "heads": ["छपा शब्द", "अर्थ"],
        "rows": [["स्तब्धं", "कठोर"], ["स्तिमितं", "स्थिर"], ["शीतम्", "ठण्डा"], ["अश्मगर्भमिव", "मानो भीतर पत्थर"]],
    },
}
