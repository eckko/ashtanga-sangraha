from helpers import mcq, match, order, fill, multi, accepts


AUTHORED = {}

# ---------------------------------------------------------------- unit 1
AUTHORED["1"] = {
    "title": "अथातः सिराविभागं शारीरं",
    "question": "What does the opening line of Śārīrasthāna chapter 6 announce?",
    "rule": ("अथातः ... व्याख्यास्यामः: 'Now, therefore, we shall explain' the bodily (शारीरम्) division of the sirās "
             "(सिराविभागम्), the vessels."),
    "limits": ("Prose, one printed line: an opening formula. सिरा is kept as a Sanskrit term (vessel; veins and other "
               "blood-carrying vessels, probable). The line gives no number and names no vessel yet."),
    "explain_hi": ("यह अध्याय की आरम्भिक गद्य-पंक्ति है: अब इसलिए हम शरीर सम्बन्धी सिरा-विभाग की व्याख्या करेंगे। "
                   "‘सिरा’ यानी वाहिनी; इस परम्परा में शिराएँ और दूसरी रक्त ले जाने वाली वाहिनियाँ (सम्भावित); संस्कृत शब्द ही रखा गया है। "
                   "‘शारीरम्’ (शरीर सम्बन्धी) विभाग के साथ लिया गया है। "
                   "‘व्याख्यास्यामः’ भविष्यत्काल, उत्तम पुरुष बहुवचन है: हम व्याख्या करेंगे। "
                   "सन्धि: अथ + अतः में अ + अ मिलकर आ बना।"),
    "hook": "अथातः: अब सिराओं का बँटवारा।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 1, what will chapter 6 explain?",
            ("The division of the sirās", "सिराविभागं ... व्याख्यास्यामः: we shall explain the division of the sirās."),
            [("The division of the bones", "Bones are not named in unit 1; the line names सिरा (vessel)."),
             ("The division of marmas", "Marmas are not named in unit 1; the line names सिरा (vessel)."),
             ("The kinds of constitution", "Constitution is not named in unit 1; the line names सिरा.")],
            "Now, therefore, we shall explain the bodily division of the sirās.",
            "अथातः सिराविभागं शारीरं व्याख्यास्यामः."),
        order(1, "Put the words of unit 1 in the line's order.",
              ["अथातः", "सिराविभागं", "शारीरं", "व्याख्यास्यामः"],
              "Now therefore, the division of the sirās, bodily, we shall explain.",
              "अथातः → सिराविभागं → शारीरं → व्याख्यास्यामः."),
        match(2, "Match each word of unit 1 to its meaning.",
              [["अथ", "now"], ["अतः", "therefore"], ["सिराविभागम्", "the division of the sirās (vessels)"],
               ["शारीरम्", "bodily, of the body"], ["व्याख्यास्यामः", "we shall explain"]],
              "Now, therefore, we shall explain the bodily division of the sirās.",
              "अथ, अतः, सिराविभागम्, शारीरम्, व्याख्यास्यामः.", role="extend",
              teaches="सिरा = vessel (veins and other blood-carrying vessels, probable); the term is kept in Sanskrit."),
        mcq("discriminate", 3, "Which split of अथातः in unit 1 is right?",
            ("अथ + अतः", "अ + अ → आ: अथ + अतः → अथातः."),
            [("अथः + अतः", "अः before अ would give अथोऽतः, with ओ and avagraha."),
             ("अथ + तः", "No vowel would merge: अथ + तः would stay अथतः."),
             ("अथे + अतः", "ए before अ would give अथेऽतः, with ए kept.")],
            "अथ (now) + अतः (therefore): अ + अ → आ.",
            "अ + अ → आ."),
        mcq("apply", 4, "In unit 1, what form is व्याख्यास्यामः?",
            ("Future, first person plural: we shall explain", "The data labels it 1 pl. fut. of vi-ā-√khyā."),
            [("Past, third person plural: they explained", "The data labels it future, first person: we shall explain."),
             ("Command, second person: you must explain", "The data labels it future, first person: we shall explain."),
             ("Future, third person singular: he will explain", "The ending -आमः is first person plural: we.")],
            "व्याख्यास्यामः = we shall explain (1 pl. future).",
            "-स्यामः = we shall (future, 1st person plural)."),
        mcq("transfer", 5, "By the rule of अथातः, how is न + अस्ति (is not) joined in a new example?",
            ("नास्ति", "अ + अ → आ, as अथ + अतः → अथातः."),
            [("नेस्ति", "ए comes from अ + इ, not from अ + अ."),
             ("नोस्ति", "ओ comes from अ + उ, not from अ + अ."),
             ("नस्ति", "The two vowels merge into आ; neither simply drops.")],
            "न + अस्ति = नास्ति, like अथ + अतः = अथातः.",
            "अ + अ → आ.",
            teaches="Two short अ vowels merge into long आ: अथ + अतः → अथातः."),
    ],
}

# ---------------------------------------------------------------- unit 2
AUTHORED["2"] = {
    "title": "दश मूलसिरा हृदयप्रतिबद्धाः",
    "question": "By unit 2, how many root-sirās are there, to what are they bound, and what do they carry?",
    "rule": ("Ten root-sirās (मूलसिराः), bound to the heart (हृदयप्रतिबद्धाः), carry (नयन्ति) ojas (vital essence) to "
             "all the limbs and sub-limbs (सर्वाङ्गप्रत्यङ्गानि)."),
    "limits": ("Prose. ओजस् is a doctrinal term (vital essence) with no modern equivalent; it is kept. The printed "
               "joined word सर्वांगप्रत्यंगान्याोजो seems to have a stray आ (flag: possible): no question rests on its sandhi."),
    "explain_hi": ("यह गद्य-पंक्ति कहती है: हृदय से बँधी दस मूलसिराएँ सब अंगों और प्रत्यंगों तक ओज ले जाती हैं। "
                   "‘ओज’ शास्त्र का शब्द है (जीवन-सार); इसका कोई आधुनिक नाम नहीं, इसलिए संस्कृत शब्द ही रखा गया। "
                   "‘नयन्ति’ के साथ दो कर्म हैं: ओज वह है जो ले जाया जाता है, और अंग-प्रत्यंग वह जहाँ तक ले जाया जाता है। "
                   "‘मूलसिरा’ में आः का विसर्ग घोष ध्वनि ह से पहले लुप्त हुआ है; यह नियमित है। "
                   "छपे ‘...न्याोजो’ में आ अधिक लगता है, इसलिए डेटा ने इसे सम्भावित भूल माना है।"),
    "hook": "हृदय से बँधी दस जड़ें, अंग-अंग तक ओज।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 2, how many root-sirās (mūlasirā) are there?",
            ("Ten", "दश मूलसिरा: ten root-sirās."),
            [("Seven", "दश is ten; seven hundred is the count of the branches (unit 4)."),
             ("Four", "दश is ten, not four."),
             ("Sixteen", "Sixteen is the count of unit 6, not of the root-sirās.")],
            "There are ten root-sirās, bound to the heart.",
            "दश मूलसिरा हृदयप्रतिबद्धाः."),
        order(1, "Put the words of unit 2 in the line's order.",
              ["दश", "मूलसिरा", "हृदयप्रतिबद्धाः", "सर्वांगप्रत्यंगान्याोजो", "नयंति"],
              "Ten, root-sirās, bound to the heart, to all limbs and sub-limbs ojas, carry.",
              "दश → मूलसिरा → हृदयप्रतिबद्धाः → सर्वांगप्रत्यंगान्याोजो → नयंति."),
        match(2, "Match each word of unit 2 to its meaning.",
              [["दश", "ten"], ["मूलसिराः", "root-sirās"], ["हृदयप्रतिबद्धाः", "bound to the heart"],
               ["ओजः", "ojas (vital essence)"], ["नयन्ति", "they carry"]],
              "Ten root-sirās, bound to the heart, carry ojas to all the limbs and sub-limbs.",
              "दश, मूलसिराः, हृदयप्रतिबद्धाः, ओजः, नयन्ति.", role="extend",
              teaches="ओजस् is a doctrinal term (vital essence) kept in Sanskrit; नयन्ति takes both what is carried and where."),
        mcq("discriminate", 3, "By unit 2, to what are the ten root-sirās bound?",
            ("To the heart (hṛdaya)", "हृदयप्रतिबद्धाः: bound to the heart."),
            [("To the head (śiras)", "The head is not named in unit 2; हृदय is the heart."),
             ("To the back (pṛṣṭha)", "The back is not named in unit 2; हृदय is the heart."),
             ("To the thighs (sakthi)", "The thighs are not named in unit 2; हृदय is the heart.")],
            "The root-sirās are bound to the heart.",
            "हृदय-प्रतिबद्धाः = bound to the heart."),
        multi("apply", 4, "Which statements fit unit 2 and its data?",
              [("The data translates ojas as 'blood'", "Ojas is kept as a doctrinal term (vital essence), not blood."),
               ("The root-sirās carry ojas", "Right: ...ओजो नयन्ति: they carry ojas."),
               ("Ojas goes to all the limbs and sub-limbs", "Right: सर्वाङ्गप्रत्यङ्गानि are where it is carried."),
               ("Unit 2 says the sirās number seven hundred", "Seven hundred is the count of unit 4, not unit 2.")],
              [1, 2],
              "Ten root-sirās, bound to the heart, carry ojas to all the limbs and sub-limbs.",
              "दश मूलसिरा हृदयप्रतिबद्धाः सर्वांगप्रत्यंगान्याोजो नयंति."),
        mcq("transfer", 5, "By the rule of मूलसिरा before ह, how is बालाः + हसन्ति (the boys laugh) joined in a new example?",
            ("बाला हसन्ति", "After आ, a visarga drops before a voiced sound such as ह, as मूलसिराः → मूलसिरा."),
            [("बालो हसन्ति", "ओ comes from अः before a voiced consonant, not from आः."),
             ("बालार्हसन्ति", "र् comes from a visarga after vowels other than अ and आ."),
             ("बालास्हसन्ति", "स् comes from a visarga before त or थ, not before ह.")],
            "बालाः + हसन्ति = बाला हसन्ति, like मूलसिराः + हृदय... = मूलसिरा हृदय...",
            "आः before a voiced sound: the visarga drops.",
            teaches="After आ, the visarga drops before a voiced sound: मूलसिराः हृदय... → मूलसिरा हृदय..."),
    ],
}

# ---------------------------------------------------------------- unit 3
AUTHORED["3"] = {
    "title": "तत्प्रतिबद्धा हि शारीरचेष्टाः",
    "question": "By unit 3, what is bound to the root-sirās?",
    "rule": ("For (हि) the activities of the body (शारीरचेष्टाः) are bound to those (तत्प्रतिबद्धाः): तत् is understood "
             "as the ten root-sirās of unit 2."),
    "limits": ("Prose, three words; it appears to continue unit 2 (grouping note), and तत् is understood, not named. "
               "The line does not list the activities or say how they depend on the vessels."),
    "explain_hi": ("यह छोटी गद्य-पंक्ति इकाई २ की बात आगे बढ़ाती दिखती है: क्योंकि शरीर की चेष्टाएँ उनसे बँधी हैं। "
                   "‘तत्’ (वे) से डेटा इकाई २ की दस मूलसिराओं को समझता है; यह नाम यहाँ छपा नहीं। "
                   "‘हि’ का अर्थ है ‘क्योंकि’: यह पिछली बात का कारण देता है। "
                   "कौन-सी चेष्टाएँ, और वे कैसे बँधी हैं, यह पंक्ति नहीं बताती। "
                   "‘तत्प्रतिबद्धा’ में भी आः का विसर्ग ह से पहले लुप्त हुआ है।"),
    "hook": "शरीर की हर हलचल उन्हीं मूल-सिराओं से बँधी।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 3, what is bound to those (the root-sirās)?",
            ("The activities of the body", "शारीरचेष्टाः: the activities (चेष्टा) of the body."),
            [("The bones of the body", "Bones are not named in unit 3; चेष्टाः are activities."),
             ("The joints of the body", "Joints are not named in unit 3; चेष्टाः are activities."),
             ("The hairs of the body", "Hairs are not named in unit 3; चेष्टाः are activities.")],
            "For the activities of the body are bound to those.",
            "तत्प्रतिबद्धा हि शारीरचेष्टाः."),
        order(1, "Put the words of unit 3 in the line's order.",
              ["तत्प्रतिबद्धा", "हि", "शारीरचेष्टाः"],
              "Bound to those, for, the activities of the body.",
              "तत्प्रतिबद्धा → हि → शारीरचेष्टाः."),
        match(2, "Match each word part of unit 3 to its meaning.",
              [["तत्", "those (the root-sirās)"], ["प्रतिबद्धाः", "bound to"], ["हि", "for"],
               ["शारीर", "of the body"], ["चेष्टाः", "activities"]],
              "For the activities of the body are bound to those.",
              "तत्, प्रतिबद्धाः, हि, शारीर, चेष्टाः.", role="extend",
              teaches="तत् is understood as the ten root-sirās of unit 2; the referent is not printed in unit 3."),
        mcq("discriminate", 3, "What does हि add to unit 3?",
            ("It gives a reason: 'for'", "The data glosses हि as 'for': the line gives a reason."),
            [("It negates the line: 'not'", "'Not' is न, which does not occur in unit 3."),
             ("It adds 'also' to the line", "'Also' is अपि, which does not occur in unit 3."),
             ("It means 'among those'", "'Among those' is तत्र, which does not occur in unit 3.")],
            "हि = for: the activities of the body are bound to them.",
            "हि = for (giving a reason)."),
        mcq("apply", 4, "Why is तत्प्रतिबद्धा printed without a visarga in unit 3?",
            ("After आ, a visarga drops before a voiced sound like ह", "Data note: tatpratibaddhāḥ before h-, regular sandhi."),
            [("The word is singular, so it ends without a visarga", "The data labels it f. nom. pl., like चेष्टाः."),
             ("Before ह any visarga drops, whatever vowel is before it", "अः before a voiced consonant becomes ओ; it does not just drop."),
             ("The visarga has moved onto हि as its first sound", "हि has no visarga; the visarga simply drops after आ.")],
            "तत्प्रतिबद्धाः + हि → तत्प्रतिबद्धा हि: आः before a voiced sound loses its visarga.",
            "आः before a voiced sound: the visarga drops."),
        mcq("transfer", 5, "By the join in तत्प्रतिबद्धा, how is तत् + पुत्रः (his son) joined in a new example?",
            ("तत्पुत्रः", "त् stays त् before प, as तत् + प्रतिबद्धाः → तत्प्रतिबद्धाः."),
            [("तद्पुत्रः", "त् becomes द् before a voiced sound; प is not voiced."),
             ("तच्पुत्रः", "त् becomes च् before च or छ (and च्छ with श), not before प."),
             ("तन्पुत्रः", "त् becomes न् before a nasal such as म or न, not before प.")],
            "तत् + पुत्रः = तत्पुत्रः, like तत् + प्रतिबद्धाः = तत्प्रतिबद्धाः.",
            "त् before an unvoiced stop like प: no change.",
            teaches="त् before an unvoiced consonant such as प stays त्: तत् + प्रतिबद्धाः → तत्प्रतिबद्धाः."),
    ],
}

# ---------------------------------------------------------------- unit 4
AUTHORED["4"] = {
    "title": "तास्तु ... सप्त शतानि भवंति",
    "question": "By unit 4, through which measures do the sirās go, and how many do they become?",
    "rule": ("Going two aṅgulas, one aṅgula, half an aṅgula, a yava and half a yava (गत्वा), and spreading out like "
             "the sevanī of a tree's leaf (sense uncertain), the sirās become seven hundred (सप्त शतानि भवन्ति)."),
    "limits": ("Prose; confidence medium. The leaf simile is not firm: सेवनी's sense is uncertain, and printed "
               "विधम्यमानाः (dispersed) may be a misreading of विभज्यमानाः (divided; flag: possible): no question on either. "
               "The measures are not converted, and the line does not say whether they are length or thickness."),
    "explain_hi": ("यह गद्य-पंक्ति बताती है कि दस मूलसिराएँ (इकाई २) शाखाएँ बनकर सात सौ हो जाती हैं। "
                   "वे क्रम से दो अङ्गुल, एक अङ्गुल, आधा अङ्गुल, एक यव और आधा यव जाती हैं; अङ्गुल (अँगुली की चौड़ाई) और यव (जौ का दाना) माप हैं, इन्हें आधुनिक माप में नहीं बदला गया। "
                   "डेटा इन मापों को शाखा बनने के क्रमिक चरण पढ़ता है; पंक्ति यह नहीं कहती कि ये लम्बाई हैं या मोटाई। "
                   "उपमा वृक्ष के पत्ते की ‘सेवनी’ के फैलाव की है, पर सेवनी का अर्थ यहाँ अनिश्चित है। "
                   "छपा ‘विधम्यमानाः’ (बिखरती हुई) ‘विभज्यमानाः’ (बँटती हुई) का गलत पाठ हो सकता है (पाठ-चिह्न: सम्भावित); दोनों अर्थ ‘फैलना’ से मेल खाते हैं।"),
    "hook": "दो अङ्गुल से आधे यव तक बँटते-बँटते दस से सात सौ।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 4, how many do the sirās become as they branch?",
            ("Seven hundred", "सप्त शतानि भवन्ति: they become seven hundred."),
            [("Four hundred", "Four hundred is the share of the limbs (unit 5)."),
             ("One hundred", "सप्त शतानि is seven hundreds, not one."),
             ("Seventy only", "शतानि are hundreds: seven hundred, not seventy.")],
            "Branching out, the sirās become seven hundred.",
            "सप्त शतानि भवंति."),
        order(1, "Put the measures of unit 4 in the line's order.",
              ["द्व्यंगुलम् (two aṅgulas)", "अंगुलम् (an aṅgula)", "अर्द्धंगुलं (half an aṅgula)", "यवं (a yava)",
               "यवार्द्धं (half a yava)"],
              "Two aṅgulas, an aṅgula, half an aṅgula, a yava, half a yava: the line's order.",
              "द्व्यंगुलम् → अंगुलम् → अर्द्धंगुलं → यवं → यवार्द्धं."),
        match(2, "Match each word of unit 4 to its meaning.",
              [["अङ्गुल", "finger-breadth (a measure)"], ["यव", "barley-grain (a measure)"], ["गत्वा", "having gone"],
               ["सप्त शतानि", "seven hundred"], ["भवन्ति", "they become"]],
              "Having gone two aṅgulas ... half a yava, they become seven hundred.",
              "अङ्गुल, यव, गत्वा, सप्त शतानि, भवन्ति.", role="extend",
              teaches="अङ्गुल (finger-breadth) and यव (barley-grain) are measures; the data does not convert them."),
        mcq("discriminate", 3, "Which split of तास्तु in unit 4 is right?",
            ("ताः + तु", "A visarga before त becomes स्: ताः + तु → तास्तु."),
            [("तात् + तु", "त् + त would give तात्तु, with no स्."),
             ("ते + अस्तु", "ए before अ would give तेऽस्तु, with ए kept."),
             ("ताः + स्तु", "स्तु is not a word here; the स् comes from the visarga.")],
            "ताः (those) + तु (but): visarga before त → स्.",
            "Visarga before त → स्."),
        multi("apply", 4, "Which statements fit unit 4 and its data?",
              [("Two aṅgulas comes first among the measures", "Right: द्व्यङ्गुलम् opens the list."),
               ("The data converts the aṅgula into centimetres", "The measures are not converted."),
               ("The line says the measures are thicknesses", "The line does not say whether length or thickness."),
               ("Half a yava is the last measure named", "Right: यवार्द्धं च closes the list.")],
              [0, 3],
              "Two aṅgulas, an aṅgula, half an aṅgula, a yava, half a yava; the measures are not converted.",
              "द्व्यङ्गुलम् ... यवार्द्धं च गत्वा."),
        mcq("transfer", 5, "By the pattern of गत्वा (having gone, from √गम्), which form of √कृ means having done?",
            ("कृत्वा", "-त्वा forms the absolutive, 'having ...ed', as √गम् → गत्वा."),
            [("करोति", "करोति is a present verb: he does."),
             ("कृतम्", "कृतम् is a past participle: done."),
             ("कर्तुम्", "कर्तुम् is an infinitive: to do.")],
            "√कृ → कृत्वा (having done), like √गम् → गत्वा (having gone).",
            "-त्वा = having ...ed (absolutive).",
            teaches="-त्वा forms the absolutive: an action finished before the main verb (गत्वा ... भवन्ति)."),
    ],
}

# ---------------------------------------------------------------- unit 5
AUTHORED["5"] = {
    "title": "तासां चतुःशती शाखासु",
    "question": "By unit 5, how many of the sirās are in the limbs (śākhā)?",
    "rule": ("Of them (तासाम्, the seven hundred), four hundred (चतुःशती) are in the limbs (शाखासु: the arms and legs)."),
    "limits": ("Prose; the copula is understood. The line appears to continue unit 4 (grouping note). It does not say "
               "how the four hundred are shared among the limbs."),
    "explain_hi": ("यह गद्य-पंक्ति सात सौ (इकाई ४) का पहला भाग बताती है: उनमें से चार सौ शाखाओं में हैं। "
                   "‘शाखा’ का शाब्दिक अर्थ डाल है; शरीर के इस बँटवारे में यह चारों हाथ-पैर हैं (मानक)। "
                   "‘चतुःशती’ एक समूह-संख्या (द्विगु) है: चार सौ का समूह। "
                   "‘हैं’ क्रिया छपी नहीं, समझी जाती है। "
                   "‘शाखासु’ में -आसु आकारान्त स्त्रीलिंग का सप्तमी बहुवचन है: शाखाओं में।"),
    "hook": "सात सौ में चार सौ हाथ-पैरों में।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 5, how many sirās are in the limbs (śākhā)?",
            ("Four hundred", "चतुःशती शाखासु: four hundred in the limbs."),
            [("Seven hundred", "Seven hundred is the whole count (unit 4)."),
             ("Forty in all", "चतुःशती is a set of four hundreds, not forty."),
             ("Ten in all", "Ten is the count of the root-sirās (unit 2).")],
            "Of the seven hundred, four hundred are in the limbs.",
            "तासां चतुःशती शाखासु."),
        order(1, "Put the words of unit 5 in the line's order.",
              ["तासां", "चतुःशती", "शाखासु"],
              "Of them, four hundred, in the limbs.",
              "तासां → चतुःशती → शाखासु."),
        match(2, "Match each word part of unit 5 to its meaning.",
              [["तासाम्", "of them"], ["चतुः", "four"], ["शती", "a hundred (a set of hundred)"],
               ["शाखासु", "in the limbs (arms and legs)"]],
              "Of them, four hundred are in the limbs.",
              "तासाम्, चतुः, शती, शाखासु.", role="extend",
              teaches="शाखा, literally 'branch', means the four limbs (arms and legs) in this body-division (standard)."),
        mcq("discriminate", 3, "What does the ending of शाखासु in unit 5 show?",
            ("In the limbs (locative plural)", "-आसु is the locative plural of an आ-stem: in the limbs."),
            [("Of the limbs (genitive plural)", "Of the limbs would be शाखानाम्."),
             ("By the limbs (instrumental plural)", "By the limbs would be शाखाभिः."),
             ("In the limb (locative singular)", "In the limb would be शाखायाम्.")],
            "शाखासु = in the limbs.",
            "आ-stem, locative plural: -आसु."),
        mcq("apply", 4, "By units 4 and 5, how many of the seven hundred are outside the limbs?",
            ("Three hundred", "700 − 400 = 300; the data later splits them as 136 + 164."),
            [("Four hundred", "Four hundred are in the limbs, not outside them."),
             ("Eleven hundred", "The four hundred are part of the seven hundred, not added to it."),
             ("Thirty in all", "700 − 400 is three hundred, not thirty.")],
            "Seven hundred in all, four hundred in the limbs: three hundred remain.",
            "700 − 400 = 300."),
        mcq("transfer", 5, "By the pattern of शाखासु, how is लता (creeper) put in the locative plural in a new example?",
            ("लतासु", "An आ-stem takes -आसु in the locative plural, as शाखा → शाखासु."),
            [("लताभिः", "लताभिः is the instrumental plural: by the creepers."),
             ("लतानाम्", "लतानाम् is the genitive plural: of the creepers."),
             ("लतायाम्", "लतायाम् is singular: in the creeper.")],
            "लता → लतासु (in the creepers), like शाखा → शाखासु.",
            "आ-stem, locative plural: -आसु.",
            teaches="-आसु marks the locative plural of feminine आ-stems: शाखा → शाखासु."),
    ],
}

# ---------------------------------------------------------------- unit 6
AUTHORED["6"] = {
    "title": "तत्र षोडशाव्यधनीयाः",
    "question": "By unit 6, what is said of sixteen of the limb sirās?",
    "rule": ("Among those (तत्र: the four hundred of the limbs, by the data's reading), sixteen (षोडश) are not to be "
             "pierced (अव्यधनीयाः)."),
    "limits": ("Prose; the copula is understood. 'Among those' as the four hundred of unit 5 is the data's reading. "
               "'Pierce' (√व्यध्) probably means venepuncture or bloodletting in practice (probable); the literal sense "
               "is kept. The sixteen are not named here."),
    "explain_hi": ("यह गद्य-पंक्ति कहती है: उनमें सोलह बेधने योग्य नहीं हैं। "
                   "‘तत्र’ (उनमें) को डेटा इकाई ५ की चार सौ शाखा-सिराओं से जोड़ता है। "
                   "‘अव्यधनीयाः’ = अ (नहीं) + व्यधनीय (बेधने योग्य); √व्यध् का अर्थ बेधना है, व्यवहार में सम्भवतः शिरा-वेध या रक्त निकालना (सम्भावित), पर शाब्दिक अर्थ रखा गया है। "
                   "सोलह कौन-सी हैं, यह यहाँ नहीं बताया गया। "
                   "सन्धि: षोडश + अव्यधनीयाः में अ + अ मिलकर आ बना।"),
    "hook": "चार सौ में सोलह: इन्हें मत बेधो।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 6, what is said of the sixteen?",
            ("They are not to be pierced", "षोडशाव्यधनीयाः: sixteen not to be pierced."),
            [("They are to be pierced first", "The अ- of अव्यधनीयाः negates: not to be pierced."),
             ("They are bound to the heart", "Binding to the heart is said of the root-sirās (unit 2)."),
             ("They are the root vessels", "The root-sirās are ten (unit 2); unit 6 does not name them.")],
            "Among those, sixteen are not to be pierced.",
            "तत्र षोडशाव्यधनीयाः."),
        match(1, "Match each word part of unit 6 to its meaning.",
              [["तत्र", "there, among those"], ["षोडश", "sixteen"], ["अ-", "not"], ["व्यधनीयाः", "to be pierced"]],
              "Among those, sixteen are not to be pierced.",
              "तत्र, षोडश, अ-, व्यधनीयाः."),
        mcq("extend", 2, "By the data's reading, among which group are the sixteen of unit 6?",
            ("The 400 of the limbs (unit 5)", "Data note: tatra is read as among those, the four hundred of unit 5."),
            [("The 10 root-sirās (unit 2)", "The root-sirās are ten; sixteen cannot be among them."),
             ("The 136 of the trunk (unit 7)", "The trunk's count comes after unit 6, in unit 7."),
             ("The 32 of the hip (unit 11)", "The hip's count comes later, in unit 11.")],
            "तत्र = among those: the four hundred in the limbs (data's reading).",
            "तत्र (among those) takes up the count just given.",
            teaches="तत्र after a count names a subset of it: among those four hundred, sixteen (data's reading)."),
        mcq("discriminate", 3, "Which split of षोडशाव्यधनीयाः in unit 6 is right?",
            ("षोडश + अव्यधनीयाः", "अ + अ → आ: षोडश + अव्यधनीयाः → षोडशाव्यधनीयाः."),
            [("षोडश + व्यधनीयाः", "No vowel would merge: it would stay षोडशव्यधनीयाः, without आ."),
             ("षोडशः + अव्यधनीयाः", "अः before अ would give षोडशोऽव्यधनीयाः."),
             ("षोडशे + अव्यधनीयाः", "ए before अ would give षोडशेऽव्यधनीयाः.")],
            "षोडश (sixteen) + अव्यधनीयाः (not to be pierced): अ + अ → आ.",
            "अ + अ → आ."),
        fill(4, "Unit 6: षोडश, then ____ (not to be pierced). Type it in Devanagari or in English letters (e.g. dharma).",
             accepts("अव्यधनीयाः", None, "अव्यधनीय", "avyadhaniyah", "avyadhaniya"),
             "षोडश + अव्यधनीयाः → षोडशाव्यधनीयाः.",
             "अ- (not) + व्यधनीय (to be pierced): अव्यधनीय.",
             "अव्यधनीयाः = not to be pierced.", role="apply"),
        mcq("transfer", 5, "By the pattern of अव्यधनीयाः, what does अकरणीयम् mean in a new example?",
            ("Not to be done", "अ- negates, -अनीय = to be ...ed: not to be done."),
            [("To be done", "The अ- at the front negates it: not to be done."),
             ("Having done it", "'Having done' is कृत्वा, an absolutive."),
             ("The one who does", "'The one who does' is कर्ता, an agent noun.")],
            "अ + करणीय = not to be done, like अ + व्यधनीय = not to be pierced.",
            "अ- + -अनीय = not to be ...ed.",
            teaches="-अनीय forms 'to be ...ed' (gerundive); अ- in front negates it: अव्यधनीय = not to be pierced."),
    ],
}

# ---------------------------------------------------------------- unit 7
AUTHORED["7"] = {
    "title": "षट्त्रिंशं शतमंतराधौ",
    "question": "By unit 7, how many (sirās, understood) are in the antarādhi (trunk, probable)?",
    "rule": ("A hundred with thirty-six added (षट्त्रिंशं शतम्) = 136 are in the antarādhi (अन्तराधौ: the trunk, between "
             "limbs and head; probable)."),
    "limits": ("Prose; confidence medium; the copula is understood. 'Trunk' for अन्तराधि is probable. The line appears "
               "to continue unit 5 (grouping note). 400 + 136 + 164 = 700 is the data's arithmetic, not printed here."),
    "explain_hi": ("यह गद्य-पंक्ति सात सौ का दूसरा भाग बताती है: अन्तराधि यानी धड़ में एक सौ छत्तीस। "
                   "‘षट्त्रिंशं शतम्’ को डेटा ‘सौ, छत्तीस और’ = १३६ पढ़ता है। "
                   "अन्तराधि हाथ-पैरों और सिर के बीच का भाग, यानी धड़ है (सम्भावित)। "
                   "डेटा का जोड़: ४०० (इकाई ५) + १३६ + १६४ (इकाई ९) = ७०० (इकाई ४)। "
                   "‘शतमंतराधौ’ में शतम् का म् स्वर से पहले अगले शब्द से जुड़ गया है।"),
    "hook": "धड़ में सौ और छत्तीस।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 7, how many (sirās, understood) are in the antarādhi (trunk, probable)?",
            ("One hundred and thirty-six", "षट्त्रिंशं शतम् = 136."),
            [("One hundred and sixty-four", "164 is the count above, unit 9."),
             ("Thirty-six with no hundred", "शतम् adds a hundred: 136, not 36."),
             ("Three thousand six hundred", "The thirty-six is added to the hundred, not multiplied.")],
            "136 are in the antarādhi.",
            "षट्त्रिंशं शतमंतराधौ."),
        match(1, "Match each word part of unit 7 to its meaning.",
              [["षट्", "six"], ["त्रिंशत्", "thirty"], ["शतम्", "a hundred"], ["अन्तराधौ", "in the antarādhi (trunk, probable)"]],
              "Thirty-six, a hundred: 136 in the trunk.",
              "षट्, त्रिंशत्, शतम्, अन्तराधौ."),
        mcq("extend", 2, "How does the data read षट्त्रिंशं शतम्?",
            ("A hundred with thirty-six added: 136", "Data note: a hundred with thirty-six added = 136."),
            [("Thirty-six hundreds, that is 3,600", "The thirty-six is added, not multiplied."),
             ("A hundred less thirty-six, that is 64", "Nothing is taken away; thirty-six is added."),
             ("Thirty-six and six more: 42", "षट् is part of षट्त्रिंशम्, thirty-six.")],
            "षट्त्रिंशं शतम् = 100 + 36 = 136.",
            "X-त्रिंशं शतम् = 100 + X-thirty.",
            teaches="An ordinal-like number in -म् with शतम् names a hundred plus that number: षट्त्रिंशं शतम् = 136."),
        mcq("discriminate", 3, "Which split of शतमंतराधौ in unit 7 is right?",
            ("शतम् + अन्तराधौ", "म् before a vowel stays म् and joins it: शतमन्तराधौ."),
            [("शत + मन्तराधौ", "मन्तराधौ is not a word; the म् belongs to शतम्."),
             ("शतम + अन्तराधौ", "अ + अ would give शतमान्तराधौ, with आ."),
             ("शतः + अन्तराधौ", "अः before अ would give शतोऽन्तराधौ.")],
            "शतम् (a hundred) + अन्तराधौ (in the trunk): म् joins the vowel.",
            "Final म् before a vowel: written joined, no change."),
        multi("apply", 4, "Which statements fit unit 7 and its data?",
              [("400 + 136 + 164 make the 700 of unit 4", "Right: the data's arithmetic (units 5, 7, 9)."),
               ("Unit 7 itself prints the total of 700", "The total is in unit 4; unit 7 prints only 136."),
               ("'Trunk' for antarādhi is a probable reading", "Right: the data labels it probable."),
               ("The thirty-six is multiplied by the hundred", "It is added: 100 + 36 = 136.")],
              [0, 2],
              "136 in the antarādhi (trunk, probable); with 400 and 164 they make 700.",
              "Limbs 400 + trunk 136 + above 164 = 700."),
        mcq("transfer", 5, "By the pattern of षट्त्रिंशं शतम्, what does द्वात्रिंशं शतम् mean in a new example?",
            ("132", "शतम् = 100; द्वात्रिंशम् adds thirty-two: 132."),
            [("32", "शतम् adds a hundred: 132, not 32."),
             ("3,200", "The number is added to the hundred, not multiplied."),
             ("68", "Nothing is taken away; 100 + 32 = 132.")],
            "द्वात्रिंशं शतम् = 100 + 32 = 132, as षट्त्रिंशं शतम् = 136.",
            "X-त्रिंशं शतम् = 100 + X-thirty.",
            teaches="A number in -म् joined with शतम् means a hundred plus that number: षट्त्रिंशं शतम् = 136."),
    ],
}

# ---------------------------------------------------------------- unit 8
AUTHORED["8"] = {
    "title": "तत्र द्वाविंशत्",
    "question": "What does unit 8 print, and why does the data flag its number?",
    "rule": ("'Among those, twenty-two' (तत्र द्वाविंशत्), as printed. The data reads तत्र as in units 6 and 9: a subset "
             "of the 136 of the trunk."),
    "limits": ("Prose; confidence low; the copula is understood. The data flags द्वाविंशत् (22): the trunk sirās named for "
               "guarding in units 12-21 add up to 32, so द्वात्रिंशत् is possible; the translation keeps 22. No question "
               "asks which number is right. The subset reading of तत्र is an inference, not stated."),
    "explain_hi": ("यह दो शब्दों की गद्य-पंक्ति है: उनमें बाईस। संख्या छपे अनुसार अनूदित है, बदली नहीं गई। "
                   "‘तत्र’ को डेटा इकाई ६ और ९ की तरह पढ़ता है: इकाई ७ के धड़ वाले १३६ में से एक उप-समूह, सम्भवतः न बेधने योग्य; यह अनुमान है, छपा नहीं। "
                   "आगे इकाई १२-२१ में धड़ की जिन सिराओं की रक्षा कही गई, उनका जोड़ ८ + २ + ४ + ४ + १४ = ३२ है। "
                   "इसलिए डेटा ‘द्वाविंशत्’ (२२) को सम्भवतः ‘द्वात्रिंशत्’ (३२) का गलत पाठ मानता है; दोनों में एक अक्षर का अन्तर है। "
                   "‘हैं’ क्रिया समझी जाती है।"),
    "hook": "धड़ में ‘उनमें बाईस’: पर जोड़ बत्तीस कहता है।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "In unit 8, what does तत्र mean, as in unit 6?",
            ("Among those", "The data glosses तत्र as 'there, among those'."),
            [("Not at all", "'Not' is न, which does not occur in unit 8."),
             ("Also, too", "'Also' is अपि, which does not occur in unit 8."),
             ("In each one", "'In each' is एकैकस्मिन्, used in unit 9.")],
            "तत्र = among those, as in unit 6.",
            "तत्र = there, among those."),
        order(1, "Put these printed phrases of units 5 to 8 in the text's order.",
              ["चतुःशती शाखासु", "तत्र षोडशाव्यधनीयाः", "षट्त्रिंशं शतमंतराधौ", "तत्र द्वाविंशत्"],
              "Four hundred in the limbs; among those sixteen; 136 in the trunk; among those twenty-two (as printed).",
              "Count, then तत्र: 400 → 16; 136 → 22 (as printed; the subset reading is the data's inference)."),
        mcq("extend", 2, "Why does the data flag the printed number of unit 8?",
            ("The guarded trunk sirās of units 12-21 total 32", "8 + 2 + 4 + 4 + 14 = 32 (units 12, 14, 16, 21)."),
            [("द्वाविंशत् is not a Sanskrit number word", "द्वाविंशत् is a number word: twenty-two."),
             ("Twenty-two is more than the trunk's count of 136", "Twenty-two is less than 136; there is no clash."),
             ("The line is too damaged to be read at all in the scan", "The line is read; it is printed as तत्र द्वाविंशत्.")],
            "The trunk sirās named for guarding later add up to 32, so the printed 22 may be a misreading of 32.",
            "A total that disagrees with its parts: flag, keep the print.",
            teaches="When the parts named later disagree with a printed count, the data flags the count and translates the print."),
        mcq("discriminate", 3, "Which word printed in unit 8 also opens unit 6?",
            ("तत्र", "Units 6 and 8 both open with तत्र (there, among those)."),
            [("अपि", "अपि comes in unit 9 (तत्रापि), not in unit 8."),
             ("षोडश", "षोडश (sixteen) is printed in unit 6 only."),
             ("न", "न (not) comes in unit 9, not in unit 8.")],
            "तत्र opens units 6 and 8: तत्र षोडशाव्यधनीयाः, तत्र द्वाविंशत्.",
            "तत्र = there, among those."),
        multi("apply", 4, "Which statements fit unit 8 and its data?",
              [("The translation keeps the printed twenty-two", "Right: the number is translated as printed."),
               ("The data changes the number to thirty-two", "Thirty-two is only a possible reading; it is not applied."),
               ("No verb is printed; 'are' is understood", "Right: the copula is understood."),
               ("Unit 8 names the place of these sirās", "No place is printed; the trunk comes from unit 7.")],
              [0, 2],
              "Twenty-two is kept as printed; 32 is a flagged possibility; the copula is understood.",
              "तत्र द्वाविंशत्."),
        mcq("transfer", 5, "A new example: सप्त छात्राः। तत्र द्वौ कुशलौ। What does तत्र mean here?",
            ("Among those (the seven)", "तत्र after a count names a subset, as in unit 6 (and, by the data's inference, unit 8)."),
            [("Therefore (for that reason)", "'Therefore' is अतः, not तत्र."),
             ("Also (the seven too)", "'Also' is अपि, not तत्र."),
             ("Not (none of them)", "'Not' is न, not तत्र.")],
            "Seven students; among those, two are skilled.",
            "Count + तत्र + number = a subset of that count.",
            teaches="After a count, तत्र (among those) introduces a subset of it: तत्र षोडश, तत्र द्वाविंशत्."),
    ],
}

# ---------------------------------------------------------------- unit 9
AUTHORED["9"] = {
    "title": "चतुःषष्ट्यधिकं शतमूर्ध्वं",
    "question": "By unit 9, how many (sirās, understood) are above, and what should one not pierce?",
    "rule": ("A hundred with sixty-four in excess (164) are above (ऊर्ध्वम्); among those also fifty. A hundred in each "
             "sakthi (thigh). Among those one should not pierce (न विध्येत्) the jāladharā."),
    "limits": ("Two printed lines, prose; confidence medium. What the fifty are is not stated. Printed सक्थि is not the "
               "usual locative (सक्थ्नि; flag: possible). जालधरा is apparently a vessel's name, 'net-bearing' is uncertain: "
               "no question on its sense. The sentence appears to continue in unit 10."),
    "explain_hi": ("पहली पंक्ति सात सौ का तीसरा भाग देती है: एक सौ चौंसठ ऊपर (ऊर्ध्वम्, शरीर का ऊपरी भाग); उनमें भी पचास। पचास क्या हैं, यह नहीं कहा गया। "
                   "डेटा की जाँच: ४०० + १३६ + १६४ = ७००। "
                   "दूसरी पंक्ति: उनमें प्रत्येक सक्थि (जाँघ) में सौ; उनमें जालधरा को न बेधे। "
                   "जालधरा सम्भवतः किसी सिरा का नाम है; शाब्दिक अर्थ ‘जाल धारण करने वाली’ अनिश्चित है। "
                   "छपा ‘सक्थि’ सामान्य सप्तमी ‘सक्थ्नि’ नहीं है, सम्भवतः न छूट गया; डेटा ने इसे ‘जाँघ’ ही रखा है, चारों शाखाएँ नहीं।"),
    "hook": "ऊपर एक सौ चौंसठ; हर जाँघ में सौ; जालधरा को मत बेधो।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 9, how many (sirās, understood) are above (ūrdhvam)?",
            ("One hundred and sixty-four", "चतुःषष्ट्यधिकं शतम् ऊर्ध्वम्: 164 above."),
            [("One hundred and thirty-six", "136 is the trunk's count (unit 7)."),
             ("Sixty-four with no hundred", "शतम् with अधिकम्: a hundred plus sixty-four."),
             ("Four hundred in the limbs", "Four hundred is the limbs' count (unit 5).")],
            "164 are above; among those also fifty.",
            "चतुःषष्ट्यधिकं शतमूर्ध्वं."),
        order(1, "Put the phrases of unit 9 in the text's order.",
              ["चतुःषष्ट्यधिकं शतमूर्ध्वं", "तत्रापि पंचाशत्", "तासामेकैकस्मिन्सक्थि शतं", "तत्र न विध्येज्जालधरां"],
              "164 above; among those also fifty; a hundred in each thigh; one should not pierce the jāladharā.",
              "चतुःषष्ट्यधिकं → तत्रापि → तासामेकैकस्मिन् → तत्र न विध्येत्."),
        match(2, "Match each word of unit 9 to its meaning.",
              [["चतुःषष्टि", "sixty-four"], ["अधिकम्", "in excess"], ["ऊर्ध्वम्", "above"],
               ["एकैकस्मिन्", "in each"], ["विध्येत्", "one should pierce"]],
              "A hundred, sixty-four in excess, above; in each thigh a hundred; one should not pierce ...",
              "चतुःषष्टि, अधिकम्, ऊर्ध्वम्, एकैकस्मिन्, विध्येत्.", role="extend",
              teaches="X-अधिकं शतम् = a hundred with X in excess: चतुःषष्ट्यधिकं शतम् = 164."),
        mcq("discriminate", 3, "Which split of विध्येज्जालधरां in unit 9 is right?",
            ("विध्येत् + जालधराम्", "त् before ज becomes ज्: विध्येत् + जालधराम् → विध्येज्जालधराम्."),
            [("विध्ये + जालधराम्", "With no final त् there would be one ज: विध्येजालधराम्."),
             ("विध्येम् + जालधराम्", "म् before ज would give ं (ञ्), not ज्ज."),
             ("विध्येः + जालधराम्", "A visarga after ए before a voiced sound would give र्.")],
            "विध्येत् (one should pierce) + जालधराम्: त् + ज → ज्ज.",
            "त् before ज → ज्."),
        mcq("apply", 4, "By unit 9, what does न विध्येत् say one should not do?",
            ("Pierce it", "न विध्येज्जालधराम्: one should not pierce the jāladharā."),
            [("Bind it", "No binding is named; the verb is विध्येत्, pierce."),
             ("Rub it", "No rubbing is named; the verb is विध्येत्, pierce."),
             ("Heat it", "No heating is named; the verb is विध्येत्, pierce.")],
            "न विध्येत् = one should not pierce.",
            "न + optative = one should not."),
        mcq("transfer", 5, "By the pattern of न विध्येत्, what does न गच्छेत् mean in a new example?",
            ("One should not go", "न + optative = one should not, as न विध्येत् = one should not pierce."),
            [("One did not go", "A past form is not optative; गच्छेत् is optative."),
             ("One is not going", "A present form would be न गच्छति."),
             ("Having not gone", "An absolutive would end in -त्वा or -य.")],
            "न गच्छेत् = one should not go, like न विध्येत् = one should not pierce.",
            "न + optative = 'one should not'.",
            teaches="The optative (here -एत्) gives a rule, 'one should'; with न it forbids: न विध्येत्."),
    ],
}

# ---------------------------------------------------------------- unit 10
AUTHORED["10"] = {
    "title": "तिरश्चाभ्यंतरगाः",
    "question": "By unit 10 and its data, which further sirās is one not to pierce?",
    "rule": ("'And (ones) going across and within' (तिरः च अभ्यन्तरगाः): by the data, further objects of न विध्येत् "
             "(one should not pierce) of unit 9."),
    "limits": ("Prose, one joined word, with no verb of its own: it appears to complete unit 9 (grouping note). 'Across' "
               "may also mean 'oblique'. तिरः is taken as an adverb with -गाः; no question rests on the word's split."),
    "explain_hi": ("यह एक जुड़े हुए शब्द की गद्य-पंक्ति है: और आड़ी तथा भीतर जाने वाली (सिराएँ)। "
                   "इसकी अपनी क्रिया नहीं; डेटा के अनुसार ये इकाई ९ के ‘न विध्येत्’ (न बेधे) के और कर्म हैं, इसलिए इसे पूरे वाक्य के रूप में अनूदित नहीं किया गया। "
                   "‘तिरः’ (आड़ा) को -गाः के साथ क्रिया-विशेषण माना गया है; ‘आड़ा’ का अर्थ ‘तिरछा’ भी हो सकता है। "
                   "‘अभ्यन्तरगाः’ = अभ्यन्तर (भीतर) + गाः (जाने वाली)। "
                   "शब्द-विभाजन डेटा के अनुसार है; इस पर कोई सन्धि-प्रश्न नहीं बनाया गया।"),
    "hook": "आड़ी जाने वाली, भीतर जाने वाली: इन्हें भी मत बेधो।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "In unit 10, what does अभ्यन्तरगाः mean?",
            ("Going within", "अभ्यन्तर (inside, within) + -गाः (going)."),
            [("Going upward", "Upward would be ऊर्ध्वगाः; अभ्यन्तर is within."),
             ("Going outward", "अभ्यन्तर is inside, the opposite of outward."),
             ("Bound within", "-गाः is going; 'bound' is प्रतिबद्ध.")],
            "अभ्यन्तरगाः = (ones) going within.",
            "अभ्यन्तर-गाः = going within."),
        match(1, "Match each part of unit 10 to its meaning.",
              [["अभ्यन्तर", "inside, within"], ["-गाः", "(ones) going"], ["अभ्यन्तरगाः", "(ones) going within"]],
              "अभ्यन्तर (within) + -गाः (going) = (ones) going within.",
              "अभ्यन्तर, -गाः, अभ्यन्तरगाः."),
        mcq("extend", 2, "In the printed अभ्यंतर of unit 10, what does the dot ं stand for?",
            ("The nasal न् (अभ्यन्तर)", "Before त the print writes the nasal as ं: अभ्यंतर = अभ्यन्तर."),
            [("The nasal म् (अभ्यम्तर)", "The word is अभ्यन्तर, with न्; no म् is in it."),
             ("A long vowel (अभ्याअतर)", "ं marks a nasal, not a long vowel."),
             ("A plural mark (अभ्यतराः)", "Plural is shown by the ending -गाः, not by ं.")],
            "अभ्यंतर is printed for अभ्यन्तर: ं stands for न् before त.",
            "Printed ं before त = न्.",
            teaches="The print writes a nasal before a consonant as ं: अभ्यंतर = अभ्यन्तर, as नयंति = नयन्ति."),
        mcq("discriminate", 3, "In अभ्यन्तरगाः, what does -गाः add?",
            ("Going", "-गा = going: (ones) going within."),
            [("Bearing", "'Bearing' would be -धर / -धरा; -गाः is going."),
             ("Bound to", "'Bound to' is प्रतिबद्ध, as in unit 2."),
             ("Carrying", "'Carrying' is नयन्ति, as in unit 2.")],
            "-गाः = (ones) going.",
            "-ग / -गा at the end of a compound = going."),
        multi("apply", 4, "Which statements fit unit 10 and its data?",
              [("Unit 10 prints its own verb", "No verb is printed in unit 10."),
               ("अभ्यन्तर means inside, within", "Right: data gloss of abhyantara."),
               ("Unit 10 gives a number of sirās", "No number is printed in unit 10."),
               ("The data rates unit 10's confidence as medium", "Right: confidence medium.")],
              [1, 3],
              "No verb and no number are printed; अभ्यन्तर = inside, within; confidence is medium.",
              "तिरश्चाभ्यंतरगाः."),
        mcq("transfer", 5, "By the pattern of अभ्यन्तरगाः, what does वनगाः mean in a new example?",
            ("(Ones) going in the forest", "-गाः = going, as अभ्यन्तरगाः = going within."),
            [("(Ones) born in the forest", "'Born in' would be -जाः: वनजाः."),
             ("(Ones) guarding the forest", "'Guarding' would be -पाः or -रक्षकाः, not -गाः."),
             ("(Ones) leaving the forest", "-गाः is going in or to, not leaving.")],
            "वन + गाः = going in the forest, like अभ्यन्तर + गाः = going within.",
            "X-गाः = (ones) going in or to X.",
            teaches="-ग / -गा after a place word means 'going (in, to) that place': अभ्यन्तरगाः = going within."),
    ],
}

# ---------------------------------------------------------------- unit 11
AUTHORED["11"] = {
    "title": "द्वात्रिंशच्छ्रोण्यां",
    "question": "By unit 11, how many (sirās, understood) are in the śroṇi, and what is their seat?",
    "rule": ("Thirty-two (द्वात्रिंशत्) are in the śroṇi (श्रोण्याम्: hip region, pelvis), having the guda (anus) and "
             "meḍhra (penis) as their seat (गुदमेढ्राश्रयाः)."),
    "limits": ("Prose; the copula is understood. आश्रय = seat, support; the line does not say more about how they rest. "
               "मेंढ्र is printed with an anusvāra, a variant spelling of मेढ्र. Śroṇi, guda and meḍhra: standard."),
    "explain_hi": ("यह गद्य-पंक्ति धड़ की सिराओं का पहला स्थान देती है: श्रोणि यानी कटि-प्रदेश में बत्तीस। "
                   "उनका आश्रय गुद (मलद्वार) और मेढ्र (शिश्न) है; ‘गुदमेढ्राश्रयाः’ बहुव्रीहि है: जिनका आश्रय गुद और मेढ्र है। "
                   "आश्रय कैसा है, यह पंक्ति आगे नहीं बताती। "
                   "सन्धि: द्वात्रिंशत् + श्रोण्याम् → द्वात्रिंशच्छ्रोण्याम् (त् + श → च्छ)। "
                   "छपा ‘मेंढ्र’ अनुस्वार वाली वर्तनी है, शब्द मेढ्र ही है।"),
    "hook": "श्रोणि में बत्तीस, गुद और मेढ्र के आश्रय से।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 11, how many (sirās, understood) are in the śroṇi (hip region)?",
            ("Thirty-two", "द्वात्रिंशत् श्रोण्याम्: thirty-two in the śroṇi."),
            [("Twenty-four", "Twenty-four is the back's count (unit 13)."),
             ("Sixteen", "Sixteen is the count of the sides (unit 12)."),
             ("Twenty-two", "द्वात्रिंशत् is thirty-two, not twenty-two.")],
            "Thirty-two are in the śroṇi.",
            "द्वात्रिंशच्छ्रोण्यां."),
        order(1, "Put the word parts of unit 11 in the line's order.",
              ["द्वात्रिंशत्", "श्रोण्याम्", "गुद", "मेढ्र", "आश्रयाः"],
              "Thirty-two, in the śroṇi, guda, meḍhra, having as seat.",
              "द्वात्रिंशत् → श्रोण्याम् → गुद → मेढ्र → आश्रयाः."),
        match(2, "Match each word of unit 11 to its meaning.",
              [["द्वात्रिंशत्", "thirty-two"], ["श्रोणि", "hip region, pelvis"], ["गुद", "anus"],
               ["मेढ्र", "penis"], ["आश्रय", "seat, support"]],
              "Thirty-two in the hip region, having the anus and penis as their seat.",
              "द्वात्रिंशत्, श्रोणि, गुद, मेढ्र, आश्रय.", role="extend",
              teaches="गुदमेढ्राश्रयाः is a bahuvrīhi: 'having guda and meḍhra as seat', describing the 32 (sirās, understood)."),
        mcq("discriminate", 3, "Which split of द्वात्रिंशच्छ्रोण्यां in unit 11 is right?",
            ("द्वात्रिंशत् + श्रोण्याम्", "त् + श → च्छ: द्वात्रिंशत् + श्रोण्याम् → द्वात्रिंशच्छ्रोण्याम्."),
            [("द्वात्रिंशः + श्रोण्याम्", "A visarga before श stays or becomes श्; it never gives च्छ."),
             ("द्वात्रिंशत् + छ्रोण्याम्", "छ्रोण्याम् is not a word; the छ comes from श after त्."),
             ("द्वात्रिंशच् + श्रोण्याम्", "The number word ends in त्, not च्; च् comes from the join.")],
            "द्वात्रिंशत् (thirty-two) + श्रोण्याम् (in the śroṇi): त् + श → च्छ.",
            "त् + श → च्छ."),
        mcq("apply", 4, "By unit 11, what do the thirty-two (sirās, understood) have as their seat (āśraya)?",
            ("The guda and meḍhra", "गुदमेढ्राश्रयाः: having guda and meḍhra as seat."),
            [("The heart and chest", "Heart and chest are not named in unit 11."),
             ("The back and spine", "Back and spine are not named in unit 11."),
             ("The head and neck", "Head and neck are not named in unit 11.")],
            "Their seat is the guda (anus) and meḍhra (penis).",
            "गुद-मेढ्र-आश्रयाः = having guda and meḍhra as seat."),
        mcq("transfer", 5, "By the rule of द्वात्रिंशच्छ्रोण्यां, how is तत् + शरीरम् (that body) joined in a new example?",
            ("तच्छरीरम्", "त् + श → च्छ, as द्वात्रिंशत् + श्रोण्याम् → द्वात्रिंशच्छ्रोण्याम्."),
            [("तद्शरीरम्", "त् becomes द् before a voiced sound; श is not voiced."),
             ("तश्शरीरम्", "त् does not become श् before श; the join gives च्छ."),
             ("तन्शरीरम्", "त् becomes न् before a nasal such as म or न, not before श.")],
            "तत् + शरीरम् = तच्छरीरम्, like द्वात्रिंशत् + श्रोण्याम् = द्वात्रिंशच्छ्रोण्याम्.",
            "त् + श → च्छ.",
            teaches="त् before श gives च्छ (त् becomes च्, श becomes छ): द्वात्रिंशत् + श्रोण्याम् → द्वात्रिंशच्छ्रोण्याम्."),
    ],
}

# ---------------------------------------------------------------- unit 12
AUTHORED["12"] = {
    "title": "तासां द्वे द्वे वंक्षणयोः",
    "question": "By unit 12, how are eight (sirās, understood) of the hip placed, and how many are in the two sides?",
    "rule": ("Of them, two each in the two groins (वङ्क्षणयोः) and the two kaṭīkataruṇas: thus eight (इत्यष्टौ); one "
             "should guard them. Sixteen in the two sides (पार्श्वयोः); in each side one going upward, named pārśvasandhi."),
    "limits": ("Two printed lines, prose; confidence low. Printed शखतो is not a word; 'from the knife' (शस्त्रतः) is a "
               "conjectural reading: no question on what they are guarded from. Kaṭīkataruṇa and pārśvasandhi are marma "
               "names in this tradition (probable). The second line is elliptical: no verb is printed."),
    "explain_hi": ("पहली पंक्ति: उन (श्रोणि की बत्तीस) में दो-दो दोनों वंक्षणों (जाँघ के मूल) में और दोनों कटीकतरुणों में, इस प्रकार आठ; इनकी रक्षा करे। "
                   "छपा ‘शखतो’ कोई शब्द नहीं; ‘शस्त्रतः’ (शस्त्र से) अनुमानित पाठ है, इसलिए ‘किससे रक्षा’ पर कोई प्रश्न नहीं। "
                   "दूसरी पंक्ति: दोनों पार्श्वों (बगलों) में सोलह; उन दोनों में एक-एक ऊपर जाने वाली, जिसका नाम पार्श्वसन्धि है। इस पंक्ति में क्रिया छपी नहीं। "
                   "कटीकतरुण और पार्श्वसन्धि इस परम्परा में मर्म (प्राण-स्थान) के नाम हैं (सम्भावित)। "
                   "सन्धि: च + इति → चेति (अ + इ → ए); इति + अष्टौ → इत्यष्टौ (इ + भिन्न स्वर → य्)।"),
    "hook": "दो-दो, दो-दो: आठ की रक्षा; बगलों में सोलह, ऊपर एक-एक पार्श्वसन्धि।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 12, how many (sirās, understood) are in the two sides (pārśva)?",
            ("Sixteen", "षोडश पार्श्वयोः: sixteen in the two sides."),
            [("Eight", "Eight is the total of the groins and kaṭīkataruṇas."),
             ("Thirty-two", "Thirty-two is the śroṇi's count (unit 11)."),
             ("Twenty-four", "Twenty-four is the back's count (unit 13).")],
            "Sixteen are in the two sides.",
            "षोडश पार्श्वयोः."),
        order(1, "Put these phrases of unit 12 in the text's order.",
              ["द्वे द्वे वंक्षणयोः", "कटीकतरुणयोश्च", "इत्यष्टौ", "षोडश पार्श्वयोः", "पार्श्वसंधिसंज्ञां"],
              "Two each in the groins, and in the kaṭīkataruṇas, thus eight; sixteen in the sides; named pārśvasandhi.",
              "वंक्षणयोः → कटीकतरुणयोश्च → इत्यष्टौ → षोडश पार्श्वयोः → पार्श्वसंधिसंज्ञां."),
        mcq("extend", 2, "How does unit 12 reach eight (अष्टौ)?",
            ("Two each in both groins and both kaṭīkataruṇas", "द्वे द्वे वङ्क्षणयोः कटीकतरुणयोश्च: 2 + 2 + 2 + 2 = 8."),
            [("Four in the two groins and four in the two sides", "The sides are counted apart: sixteen."),
             ("Eight in each one of the two groins", "द्वे द्वे is two each, not eight each."),
             ("Two each in the two sides and in the back as well", "The back is not named in unit 12.")],
            "Two each in the two groins and in the two kaṭīkataruṇas: eight.",
            "द्वे द्वे ... इति अष्टौ.",
            teaches="इति closes a list and the total follows: द्वे द्वे ... इत्यष्टौ = thus eight."),
        mcq("discriminate", 3, "Which split of इत्यष्टौ in unit 12 is right?",
            ("इति + अष्टौ", "इ before a different vowel becomes य्: इति + अष्टौ → इत्यष्टौ."),
            [("इतः + अष्टौ", "अः before अ would give इतोऽष्टौ."),
             ("इते + अष्टौ", "ए before अ would give इतेऽष्टौ."),
             ("इत्य + अष्टौ", "अ + अ would give इत्याष्टौ, with आ.")],
            "इति (thus) + अष्टौ (eight): इ + अ → य.",
            "इ + a different vowel → य् + that vowel."),
        multi("apply", 4, "Which statements fit unit 12 and its data?",
              [("Printed शखतो is a clear Sanskrit word", "It is not a word; शस्त्रतः is only conjectural."),
               ("The second line prints its own verb", "It is elliptical: no verb is printed."),
               ("Sixteen are in the two sides", "Right: षोडश पार्श्वयोः."),
               ("In each side one goes upward, named pārśvasandhi", "Right: ऊर्ध्वगाम् एकैकां पार्श्वसंधिसंज्ञां.")],
              [2, 3],
              "Sixteen in the sides, one upward in each named pārśvasandhi; शखतो is unclear; no verb in line two.",
              "षोडश पार्श्वयोः तयोरूर्ध्वगामेकैकां पार्श्वसंधिसंज्ञां."),
        mcq("transfer", 5, "By the join in कटीकतरुणयोश्चेति, how is न + इति joined in a new example?",
            ("नेति", "अ + इ → ए, as च + इति → चेति."),
            [("नीति", "ई comes from इ + इ, not from अ + इ."),
             ("नैति", "ऐ comes from अ + ए, not from अ + इ."),
             ("न्यति", "य् comes from इ before a different vowel; here अ meets इ.")],
            "न + इति = नेति, like च + इति = चेति.",
            "अ + इ → ए.",
            teaches="अ + इ → ए: च + इति → चेति (in कटीकतरुणयोश्चेत्यष्टौ)."),
    ],
}

# ---------------------------------------------------------------- unit 13
AUTHORED["13"] = {
    "title": "चतुर्विंशतिः पृष्ठे",
    "question": "By unit 13, how many (sirās, understood) are in the back (pṛṣṭha)?",
    "rule": ("Twenty-four (चतुर्विंशतिः) are in the back (पृष्ठे)."),
    "limits": ("Prose, two words; the copula is understood. The line does not say where in the back they lie; the "
               "next line places four of them."),
    "explain_hi": ("यह दो शब्दों की गद्य-पंक्ति है: पीठ में चौबीस। "
                   "‘चतुर्विंशतिः’ = चतुर् (चार) + विंशति (बीस) = २४। "
                   "‘पृष्ठे’ नपुंसक पृष्ठ का सप्तमी एकवचन है: पीठ में। "
                   "‘हैं’ क्रिया छपी नहीं, समझी जाती है। "
                   "यह धड़ की सिराओं की गिनती का अगला स्थान है: श्रोणि (इकाई ११) और पार्श्व (इकाई १२) के बाद पीठ।"),
    "hook": "पीठ में चौबीस।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 13, how many (sirās, understood) are in the back?",
            ("Twenty-four", "चतुर्विंशतिः पृष्ठे: twenty-four in the back."),
            [("Thirty-two", "Thirty-two is the śroṇi's count (unit 11)."),
             ("Sixteen", "Sixteen is the count of the sides (unit 12)."),
             ("Forty-two", "चतुर्विंशति is four and twenty: twenty-four.")],
            "Twenty-four are in the back.",
            "चतुर्विंशतिः पृष्ठे."),
        match(1, "Match each word part of unit 13 to its meaning.",
              [["चतुर्", "four"], ["विंशतिः", "twenty"], ["चतुर्विंशतिः", "twenty-four"], ["पृष्ठे", "in the back"]],
              "Four + twenty = twenty-four, in the back.",
              "चतुर्, विंशतिः, चतुर्विंशतिः, पृष्ठे."),
        fill(2, "By unit 13, twenty-four are ____ (in the back). Type it in Devanagari or in English letters (e.g. dharma).",
             accepts("पृष्ठे", None, "पृष्ठ"),
             "पृष्ठे = in the back: चतुर्विंशतिः पृष्ठे.",
             "पृष्ठ (back) + -े (locative singular) = in the back.",
             "पृष्ठे = in the back."),
        mcq("discriminate", 3, "Which meaning fits the form पृष्ठे in unit 13?",
            ("In the back (locative)", "The data labels it n. loc. sg.: in the back."),
            [("Of the back (genitive)", "Of the back would be पृष्ठस्य."),
             ("By the back (instrumental)", "By the back would be पृष्ठेन."),
             ("The backs (nominative plural)", "The backs would be पृष्ठानि.")],
            "पृष्ठे = in the back.",
            "अ-stem, locative singular: -े."),
        mcq("apply", 4, "By units 11 to 13, which region has the most (sirās, understood)?",
            ("The hip region (śroṇi)", "Śroṇi 32 (unit 11) is more than back 24 or sides 16."),
            [("The back (pṛṣṭha)", "The back has 24 (unit 13), fewer than the śroṇi's 32."),
             ("The two sides (pārśva)", "The sides have 16 (unit 12), fewer than 32."),
             ("The two groins (vaṅkṣaṇa)", "The groins have two each (unit 12), fewer than 32.")],
            "Śroṇi 32, back 24, sides 16, groins 2 + 2.",
            "Compare: 32 > 24 > 16."),
        mcq("transfer", 5, "By the pattern of चतुर्विंशतिः (24), what does चतुस्त्रिंशत् mean in a new example?",
            ("34", "चतुर् (four) + त्रिंशत् (thirty) = 34, as चतुर् + विंशति = 24."),
            [("43", "The unit comes first in the word, but its value is added: 30 + 4."),
             ("120", "The parts are added, not multiplied: 30 + 4."),
             ("7", "त्रिंशत् is thirty, not three: 30 + 4.")],
            "चतुस्त्रिंशत् = 4 + 30 = 34, like चतुर्विंशतिः = 4 + 20.",
            "unit + tens = their sum.",
            teaches="A unit placed before a tens word is added to it: चतुर् + विंशति = 24."),
    ],
}


# ===================================================================== NOTES_HI
NOTES_HI = {
    "1": ("गद्य; विश्वास उच्च; कोई पाठ-चिह्न नहीं। अध्याय की आरम्भिक पंक्ति। सिरा = वाहिनी, शिराएँ और दूसरी रक्तवाहिनियाँ "
          "(सम्भावित); संस्कृत शब्द रखा गया। शारीरम् को विभाग के साथ लिया गया। सन्धि जाँची: अथ + अतः → अथातः (अ + अ → आ); "
          "व्यंजन से पहले छपे सिराविभागं, शारीरं में म् → ं।"),
    "2": ("गद्य; विश्वास उच्च। पाठ-चिह्न (सम्भावित): छपा ‘सर्वांगप्रत्यंगान्याोजो’ में -न्या- और -ओजो के बीच आ अधिक लगता है; "
          "-आनि + ओजः से ‘-आन्योजो’ बनता है; छपा रूप रखा गया, इस पर कोई प्रश्न नहीं। ओजस् = जीवन-सार, शास्त्रीय शब्द, आधुनिक नाम नहीं। "
          "सन्धि जाँची: मूलसिराः + ह... → मूलसिरा (आः का विसर्ग घोष ध्वनि से पहले लुप्त, नियमित); ओजः + न... → ओजो (अः + घोष व्यंजन → ओ); "
          "छपा नयंति = नयन्ति।"),
    "3": ("गद्य; विश्वास उच्च; कोई पाठ-चिह्न नहीं। समूह-टिप्पणी: इकाई २ को आगे बढ़ाती दिखती है; ‘तत्’ = इकाई २ की दस मूलसिराएँ "
          "(समझा गया, छपा नहीं)। सन्धि जाँची: तत्प्रतिबद्धाः + हि → तत्प्रतिबद्धा हि (आः + घोष ध्वनि, विसर्ग लुप्त); तत् + प्र... → "
          "तत्प्र... (प से पहले त् नहीं बदलता)।"),
    "4": ("गद्य; विश्वास मध्यम। पाठ-चिह्न (सम्भावित): छपा ‘विधम्यमानाः’ (बिखरती हुई) सम्भवतः ‘विभज्यमानाः’ (बँटती हुई); भ/ध और ज/म "
          "छपाई में मिलते-जुलते हैं; छपा शब्द रखा गया। सेवनी का अर्थ यहाँ अनिश्चित (अन्यत्र सिलाई, सीवन); उपमा पर कोई प्रश्न नहीं। "
          "अङ्गुल, यव माप हैं, बदले नहीं गए; लम्बाई या मोटाई, यह नहीं कहा। सन्धि जाँची: ताः + तु → तास्तु (त से पहले विसर्ग → स्); "
          "द्वि + अङ्गुलम् → द्व्यङ्गुलम् (इ + अ → य); यव + अर्धम् → यवार्धम् (अ + अ → आ)। छपा ‘अर्द्धंगुलं’ (अर्ध + अङ्गुलम्) में आ नहीं दिखता; "
          "इस पर कोई सन्धि-प्रश्न नहीं। छपाई में -र्द्ध- = -र्ध-।"),
    "5": ("गद्य; विश्वास उच्च; कोई पाठ-चिह्न नहीं। समूह-टिप्पणी: इकाई ४ के सात सौ का भाग। शाखा = हाथ-पैर (मानक)। चतुःशती द्विगु, "
          "स्त्रीलिंग एकवचन। क्रिया समझी जाती है। सन्धि जाँची: तासाम् व्यंजन से पहले तासां (ं)।"),
    "6": ("गद्य; विश्वास उच्च; कोई पाठ-चिह्न नहीं। ‘तत्र’ = उनमें, इकाई ५ के चार सौ (डेटा का पठन)। √व्यध् = बेधना; व्यवहार में "
          "सम्भवतः शिरा-वेध या रक्त-मोक्षण (सम्भावित), शाब्दिक अर्थ रखा गया। सन्धि जाँची: षोडश + अव्यधनीयाः → षोडशाव्यधनीयाः "
          "(अ + अ → आ)।"),
    "7": ("गद्य; विश्वास मध्यम; कोई पाठ-चिह्न नहीं। षट्त्रिंशं शतम् = सौ और छत्तीस = १३६ (डेटा का पठन)। अन्तराधि = धड़, अंगों और सिर "
          "के बीच का भाग (सम्भावित)। डेटा का जोड़: ४०० + १३६ + १६४ = ७००। सन्धि जाँची: शतम् + अन्तराधौ → शतमन्तराधौ (स्वर से पहले म्); "
          "छपा अंतराधौ = अन्तराधौ।"),
    "8": ("गद्य; विश्वास निम्न। पाठ-चिह्न (सम्भावित, और सम्भवतः ठीक): छपा ‘द्वाविंशत्’ (२२); धड़ की जिन सिराओं की रक्षा कही गई, "
          "उनका जोड़ ८ (इकाई १२, छपी पंक्ति १३) + २ (इकाई १२, पंक्ति १४) + ४ (इकाई १४) + ४ (इकाई १६) + १४ (इकाई २१) = ३२ = द्वात्रिंशत्; "
          "दोनों में एक अक्षर का अन्तर। सुधार लागू नहीं, छपा २२ अनूदित। कौन-सी संख्या ठीक है, इस पर कोई प्रश्न नहीं। ‘तत्र’ को इकाई ६ और ९ "
          "की तरह उप-समूह पढ़ना अनुमान है।"),
    "9": ("गद्य; विश्वास मध्यम; दो छपी पंक्तियाँ (०२.०६.९, ०२.०६.१०)। पाठ-चिह्न (सम्भावित): छपा ‘सक्थि’ सामान्य सप्तमी नहीं "
          "(सक्थ्नि या सक्थिनि), सम्भवतः न छूटा; अर्थ ‘जाँघ’ रखा गया, चारों शाखाओं तक नहीं बढ़ाया। पचास क्या हैं, नहीं कहा; डेटा की "
          "गणना (इकाई २४-३६ की सिराएँ = ५०) केवल संकेत है। जालधरा = सम्भवतः किसी सिरा का नाम, ‘जाल धारण करने वाली’ अर्थ अनिश्चित। "
          "पंक्ति के भीतर का ‘।’ पहला वाक्यांश समाप्त करता है। सन्धि जाँची: चतुःषष्टि + अधिकम् → चतुःषष्ट्यधिकम् (इ + अ → य); "
          "तत्र + अपि → तत्रापि (अ + अ → आ); विध्येत् + जालधराम् → विध्येज्जालधराम् (त् + ज → ज्ज)।"),
    "10": ("गद्य; विश्वास मध्यम; कोई पाठ-चिह्न नहीं। समूह-टिप्पणी: इकाई ९ के ‘न विध्येत्’ के और कर्म; अपनी क्रिया नहीं। तिरः को -गाः के "
           "साथ क्रिया-विशेषण लिया गया; ‘आड़ा’ = तिरछा भी हो सकता है। विभाजन डेटा के अनुसार (तिरः + च + अभ्यन्तरगाः); इस जुड़े शब्द पर "
           "कोई सन्धि-प्रश्न नहीं।"),
    "11": ("गद्य; विश्वास उच्च; कोई पाठ-चिह्न नहीं। श्रोणि = कटि-प्रदेश, गुद = मलद्वार, मेढ्र = शिश्न (सभी मानक)। छपा मेंढ्र अनुस्वार "
           "वाली वर्तनी है। गुदमेढ्राश्रयाः बहुव्रीहि। सन्धि जाँची: द्वात्रिंशत् + श्रोण्याम् → द्वात्रिंशच्छ्रोण्याम् (त् + श → च्छ); "
           "गुदमेढ्र + आश्रयाः → ...मेढ्राश्रयाः (अ + आ → आ)।"),
    "12": ("गद्य; विश्वास निम्न; दो छपी पंक्तियाँ (०२.०६.१३, ०२.०६.१४)। पाठ-चिह्न (सम्भावित): छपा ‘शखतो’ कोई शब्द नहीं; अनुमानित "
           "पाठ ‘शस्त्रतः’ (शस्त्र से), जैसे इकाई २४ (शस्त्रेण न स्पृशेत्) और इकाई ३६ (शस्त्रेण परिहरेत्) में; ख/स्त्र का भ्रम सम्भव। "
           "इस पर कोई प्रश्न नहीं। कटीकतरुण, पार्श्वसन्धि = इस परम्परा में मर्म-नाम (सम्भावित)। दूसरी पंक्ति में क्रिया नहीं (रक्षेत् जैसी "
           "क्रिया समझी जा सकती है, जोड़ी नहीं गई)। सन्धि जाँची: कटीकतरुणयोः + च → ...योश्च (च से पहले विसर्ग → श्); च + इति → चेति "
           "(अ + इ → ए); इति + अष्टौ → इत्यष्टौ; तयोः + ऊर्ध्व... → तयोरूर्ध्व... (ओ के बाद विसर्ग + स्वर → र्)।"),
    "13": ("गद्य; विश्वास उच्च; कोई पाठ-चिह्न नहीं। क्रिया समझी जाती है। चतुर्विंशतिः = २४; पृष्ठे नपुंसक सप्तमी एकवचन। कोई "
           "सन्धि-परिवर्तन नहीं (प से पहले विसर्ग छपा रहता है)।"),
}


# ===================================================================== AIDS
AIDS = {
    "1": {
        "chunks": "अथातः | सिराविभागं शारीरं | व्याख्यास्यामः",
        "sandhi": "अ + अ → आ: अथ + अतः → अथातः।",
        "frame": "कब: अथ (अब) → क्यों: अतः (इसलिए) → क्या: सिराविभाग (सिराओं का बँटवारा) → कौन: हम व्याख्या करेंगे।",
    },
    "2": {
        "chain": {"steps": ["हृदय", "उससे बँधी दस मूलसिराएँ", "ओज ले जाती हैं", "सब अंगों और प्रत्यंगों तक"]},
        "chunks": "दश मूलसिरा | हृदयप्रतिबद्धाः | सर्वांगप्रत्यंगान्याोजो | नयंति",
        "sandhi": "आः का विसर्ग घोष ध्वनि से पहले लुप्त: मूलसिराः + ह... → मूलसिरा ह...।",
        "pegs": "मेरा बनाया चित्र: हृदय एक पेड़ का तना, दस मोटी जड़ें, जो हर डाल तक रस पहुँचाती हैं। (केवल याद की सहायता)",
    },
    "3": {
        "chunks": "तत्प्रतिबद्धा | हि | शारीरचेष्टाः",
        "frame": "किससे बँधी: तत् (वे मूलसिराएँ, समझा गया) → क्यों: हि (क्योंकि) → क्या: शारीरचेष्टाः (शरीर की चेष्टाएँ)।",
        "sandhi": "प से पहले त् नहीं बदलता: तत् + प्रतिबद्धाः → तत्प्रतिबद्धाः।",
    },
    "4": {
        "chain": {"steps": ["द्वि + अङ्गुल (दो अङ्गुल)", "अङ्गुल", "अर्ध अङ्गुल", "यव (जौ)", "अर्ध यव",
                            "सप्त शतानि: सात सौ हो जाती हैं"]},
        "chunks": "तास्तु | द्व्यंगुलमंगुलमर्द्धंगुलं | यवं यवार्द्धं च गत्वा | द्रुमपत्रसेवनीप्रतानवद्विधम्यमानाः | सप्त शतानि भवंति",
        "sandhi": "त से पहले विसर्ग → स्: ताः + तु → तास्तु · इ + अ → य: द्वि + अङ्गुलम् → द्व्यङ्गुलम्।",
        "letters": "माप का क्रम: दो-एक-आधा अङ्गुल, फिर एक-आधा यव। (मेरी याद-पद्धति)",
    },
    "5": {
        "chunks": "तासां | चतुःशती | शाखासु",
        "frame": "किनमें से: तासाम् (उन सात सौ में से) → कितनी: चतुःशती (४००) → कहाँ: शाखासु (हाथ-पैरों में)।",
        "anchors": "शाखा = पेड़ की डाल; शरीर की डालें = हाथ-पैर। (मेरी याद-पद्धति)",
    },
    "6": {
        "chunks": "तत्र | षोडशाव्यधनीयाः",
        "sandhi": "अ + अ → आ: षोडश + अव्यधनीयाः → षोडशाव्यधनीयाः।",
        "frame": "किनमें: तत्र (उन चार सौ में, डेटा का पठन) → कितनी: षोडश (१६) → क्या: अव्यधनीयाः (न बेधने योग्य)।",
    },
    "7": {
        "chunks": "षट्त्रिंशं | शतमंतराधौ",
        "frame": "कितनी: शतम् (१००) + षट्त्रिंशम् (३६) = १३६ → कहाँ: अन्तराधौ (धड़ में, सम्भावित)।",
        "sandhi": "स्वर से पहले म् जुड़ता है: शतम् + अन्तराधौ → शतमन्तराधौ।",
    },
    "8": {
        "chain": {"steps": ["इकाई ५: ४०० शाखाओं में", "इकाई ६: तत्र १६ न बेधने योग्य", "इकाई ७: १३६ अन्तराधि में",
                            "इकाई ८: तत्र २२ (छपा; सम्भावित ३२)", "इकाई ९: १६४ ऊपर; तत्रापि ५०"]},
        "chunks": "तत्र | द्वाविंशत्",
        "frame": "किनमें: तत्र (उन १३६ में, डेटा का अनुमान) → कितनी: द्वाविंशत् (२२, छपे अनुसार; सम्भावित पाठ ३२)।",
    },
    "9": {
        "diagram": {"groups": [
            {"label": "७०० का बँटवारा (कहाँ: संख्या)", "items": ["शाखाएँ (इकाई ५): ४००", "अन्तराधि, धड़ (इकाई ७): १३६",
                                                           "ऊर्ध्व, ऊपर (इकाई ९): १६४", "कुल (इकाई ४): ७००"]}]},
        "chunks": "चतुःषष्ट्यधिकं शतमूर्ध्वं | तत्रापि पंचाशत् || तासामेकैकस्मिन्सक्थि शतं। | तत्र न विध्येज्जालधरां",
        "sandhi": "त् + ज → ज्ज: विध्येत् + जालधराम् → विध्येज्जालधराम् · इ + अ → य: चतुःषष्टि + अधिकम् → चतुःषष्ट्यधिकम्।",
        "frame": "भाग १: ऊपर १६४, उनमें भी ५० → भाग २: हर सक्थि (जाँघ) में १०० → निषेध: जालधरा को न बेधे।",
    },
    "10": {
        "chunks": "तिरश्चाभ्यंतरगाः",
        "frame": "किस क्रिया के कर्म: इकाई ९ का ‘न विध्येत्’ (डेटा) → कौन-सी: तिरः (आड़ी, या तिरछी) च अभ्यन्तरगाः (भीतर जाने वाली)।",
        "anchors": "-ग = जाने वाला: जैसे हिन्दी ‘खग’ (आकाश में जाने वाला, पक्षी)। (मेरी याद-पद्धति, शब्द-साम्य पर)",
    },
    "11": {
        "chunks": "द्वात्रिंशच्छ्रोण्यां | गुदमेंढ्राश्रयाः",
        "sandhi": "त् + श → च्छ: द्वात्रिंशत् + श्रोण्याम् → द्वात्रिंशच्छ्रोण्याम्।",
        "frame": "कितनी: द्वात्रिंशत् (३२) → कहाँ: श्रोण्याम् (कटि-प्रदेश में) → किसके आश्रय से: गुद और मेढ्र।",
    },
    "12": {
        "diagram": {"groups": [
            {"label": "पहली पंक्ति: आठ (इति अष्टौ)", "items": ["दोनों वंक्षणों में: दो-दो", "दोनों कटीकतरुणों में: दो-दो",
                                                         "जोड़: आठ; रक्षा करे"]},
            {"label": "दूसरी पंक्ति: पार्श्व", "items": ["दोनों पार्श्वों में: सोलह",
                                                   "हर पार्श्व में ऊपर जाने वाली: एक (पार्श्वसन्धि नाम)"]}]},
        "chunks": "तासां द्वे द्वे वंक्षणयोः | कटीकतरुणयोश्चेत्यष्टौशखतो | रक्षेत् || षोडश पार्श्वयोः | तयोरूर्ध्वगामेकैकां | पार्श्वसंधिसंज्ञां",
        "sandhi": "अ + इ → ए: च + इति → चेति · इ + अ → य: इति + अष्टौ → इत्यष्टौ · ओ के बाद विसर्ग + स्वर → र्: तयोः + ऊर्ध्व... → तयोरूर्ध्व...।",
    },
    "13": {
        "chunks": "चतुर्विंशतिः | पृष्ठे",
        "frame": "कितनी: चतुर् (४) + विंशति (२०) = २४ → कहाँ: पृष्ठे (पीठ में)।",
    },
}


# ===================================================================== IMAGE_SPECS
IMAGE_SPECS = {
    ("2", "chain"): {
        "file": "sh6-mulasira-2.svg",
        "alt": ("Flowchart of unit 2: the heart; the ten root-sirās bound to it; they carry ojas; to all the limbs "
                "and sub-limbs."),
        "type": "mermaid",
        "code": ('flowchart TD\n'
                 '  A["हृदय"] -->|"बँधी"| B["दस मूलसिराएँ"]\n'
                 '  B -->|"ले जाती हैं"| C["ओज"]\n'
                 '  C -->|"तक"| D["सब अंग और प्रत्यंग"]\n'),
    },
    ("4", "chain"): {
        "file": "sh6-sapta-shata-4.svg",
        "alt": ("Chain of unit 4 in the line's order: two aṅgulas, one aṅgula, half an aṅgula, a yava, half a yava; "
                "then the sirās become seven hundred."),
        "type": "chain",
        "title": "इकाई ४: बँटते-बँटते सात सौ",
        "steps": ["द्वि + अङ्गुल (दो अङ्गुल)", "अङ्गुल", "अर्ध अङ्गुल", "यव (जौ)", "अर्ध यव", "सप्त शतानि: सात सौ हो जाती हैं"],
    },
    ("8", "chain"): {
        "file": "sh6-tatra-8.svg",
        "alt": ("Chain of units 5 to 9 in text order: 400 in the limbs; among those 16 not to be pierced; 136 in the "
                "trunk; among those 22 as printed (32 possible); 164 above, among those also 50."),
        "type": "chain",
        "title": "इकाई ५-९: गिनती और ‘तत्र’",
        "steps": ["इकाई ५: ४०० शाखाओं में", "इकाई ६: तत्र १६ न बेधने योग्य", "इकाई ७: १३६ अन्तराधि में",
                  "इकाई ८: तत्र २२ (छपा; सम्भावित ३२)", "इकाई ९: १६४ ऊपर; तत्रापि ५०"],
    },
    ("9", "diagram"): {
        "file": "sh6-saptashati-split-9.svg",
        "alt": ("Table of the split of the seven hundred sirās: limbs 400 (unit 5), trunk 136 (unit 7), above 164 "
                "(unit 9), total 700 (unit 4)."),
        "type": "table",
        "title": "इकाई ४-९: ७०० सिराओं का बँटवारा",
        "heads": ["कहाँ (इकाई)", "संख्या"],
        "rows": [["शाखाएँ (५)", "४००"], ["अन्तराधि, धड़ (७)", "१३६"], ["ऊर्ध्व, ऊपर (९)", "१६४"], ["कुल (४)", "७००"]],
    },
    ("12", "diagram"): {
        "file": "sh6-vankshana-parshva-12.svg",
        "alt": ("Table of unit 12: two each in the two groins and the two kaṭīkataruṇas, thus eight, to be guarded; "
                "sixteen in the two sides; one going upward in each side, named pārśvasandhi."),
        "type": "table",
        "title": "इकाई १२: वंक्षण, कटीकतरुण, पार्श्व",
        "heads": ["कहाँ", "संख्या"],
        "rows": [["दोनों वंक्षणों में", "दो-दो"], ["दोनों कटीकतरुणों में", "दो-दो"], ["इति अष्टौ: रक्षा करे", "आठ"],
                 ["दोनों पार्श्वों में", "सोलह"], ["हर पार्श्व में ऊपर जाने वाली", "एक (पार्श्वसन्धि)"]],
    },
}
