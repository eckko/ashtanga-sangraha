from helpers import mcq, match, order, fill, multi, accepts


AUTHORED = {}

# ---------------------------------------------------------------- unit 129
AUTHORED["129"] = {
    "title": "मंदस्तु सम्यगप्युपयुक्तम्",
    "question": "By unit 129, how does the manda (slow) agni deal with food, even food taken properly?",
    "rule": ("The manda agni, even with food properly taken (सम्यगप्युपयुक्तम्), first shows the signs of āma (आमलिङ्गानि: "
             "heaviness of the belly, distension, constipation and the like) and digests only after a long time (चिरात्पचति)."),
    "limits": ("Prose, one printed line; the fourth agni of unit 125. The list ends in ādi, so it is not complete. "
               "उदरगौरव is read as one item (heaviness of the belly), though it could be two; no question rests on that. "
               "āma = raw, undigested matter (standard). No cure is given."),
    "explain_hi": ("इकाई १२५ में अग्नि के चार भेद गिनाए गए; यह पंक्ति चौथे, मन्द अग्नि को बताती है। "
                   "मन्द अग्नि ठीक से खाए गए अन्न को भी तुरन्त नहीं पचाती: पहले आम (कच्चे, न पचे पदार्थ) के लक्षण दिखाती है, फिर देर से पचाती है। "
                   "छपे लक्षण: उदर का भारीपन, आध्मान (पेट फूलना), विबन्ध (मल रुकना), आटोप (गड़गड़ाहट), आन्त्रकूजन (आँतों की आवाज़), "
                   "मुख का सूखना, पायु (गुदा) की जकड़न, आदि। "
                   "‘आदि’ बताता है कि सूची पूरी नहीं है। "
                   "तुलना: सम अग्नि ठीक खाए को ठीक पचाती है (इकाई १२६), तीक्ष्ण जल्दी पचाती है (इकाई १२८)।"),
    "hook": "मन्द अग्नि: पहले आम के लक्षण, फिर देर से पाक।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 129, what does the manda (slow) agni do with food that was taken properly?",
            ("It shows signs of āma, then digests late", "आमलिङ्गानि दर्शयित्वा चिरात्पचति: shows the signs of āma, digests after a long time."),
            [("It digests it fast and turns into atyagni", "Growing into atyagni is said of the tīkṣṇa agni (unit 128)."),
             ("It digests it properly at the due time", "Proper digestion of properly taken food is the sama agni (unit 126)."),
             ("It leaves properly taken food undigested", "Not digesting properly taken food is said of the viṣama agni (unit 127).")],
            "Even properly taken food: signs of āma first, digestion after a long time.",
            "मन्दः ... आमलिङ्गानि दर्शयित्वा चिरात्पचति."),
        order(1, "Put these signs of āma in the order unit 129 prints them.",
              ["उदरगौरव", "आध्मान", "विबंध", "आटोप", "आंत्रकूजन", "मुखशोष"],
              "Heaviness of the belly, distension, constipation, gurgling, intestinal murmuring, dryness of the mouth (then stiffness of the anus and the like).",
              "उदरगौरव → आध्मान → विबंध → आटोप → आंत्रकूजन → मुखशोष."),
        match(2, "Match each sign of āma in unit 129 to its meaning.",
              [["आध्मान", "flatulent distension"], ["विबन्ध", "constipation"], ["आटोप", "gurgling"],
               ["मुखशोष", "dryness of the mouth"], ["पायुस्तम्भ", "stiffness of the anus"]],
              "आध्मान distension, विबन्ध constipation, आटोप gurgling, मुखशोष dry mouth, पायुस्तम्भ stiff anus.",
              "आध्मान, विबन्ध, आटोप, मुखशोष, पायुस्तम्भ.", role="extend",
              teaches="These are the printed signs (लिङ्ग) of āma, raw undigested matter, that the manda agni shows before it digests."),
        mcq("discriminate", 3, "Which split of सम्यगप्युपयुक्तम् in unit 129 is right?",
            ("सम्यक् + अपि + उपयुक्तम्", "क् before a vowel → ग्; इ before the unlike vowel उ → य्."),
            [("सम्यग् + अपि + युक्तम्", "That would give सम्यगपियुक्तम्; the print has -प्युप-."),
             ("सम्यक् + अप्यु + उपयुक्तम्", "अप्यु is not a word; the य् comes from the इ of अपि."),
             ("सम्यक् + अपे + उपयुक्तम्", "ए before उ would not give य्; the word is अपि, 'even'.")],
            "सम्यक् (properly) + अपि (even) + उपयुक्तम् (taken).",
            "क् + vowel → ग्; इ + unlike vowel → य्."),
        multi("apply", 4, "Which statements fit the manda agni of unit 129?",
              [("It digests improperly taken food quickly", "That is the tīkṣṇa agni (unit 128)."),
               ("Even properly taken food is digested after a long time", "Right: सम्यगप्युपयुक्तं ... चिरात्पचति."),
               ("It shows the signs of āma before digesting", "Right: आमलिङ्गानि दर्शयित्वा."),
               ("Increasing, it becomes atyagni", "Becoming atyagni is said of the tīkṣṇa agni (unit 128).")],
              [1, 2],
              "Manda: signs of āma, then late digestion, even of properly taken food.",
              "मन्दः: आमलिङ्गानि दर्शयित्वा चिरात्पचति."),
        mcq("transfer", 5, "By the rule of सम्यक् + अपि → सम्यगपि, how is वाक् + ईशः joined in a new example?",
            ("वागीशः", "क् before a vowel becomes ग्, as in सम्यक् + अपि → सम्यगपि."),
            [("वाकीशः", "क् does not stay क् before a vowel when words are joined."),
             ("वाङीशः", "ङ् comes from क् before a nasal, not before a vowel."),
             ("वागिशः", "The ग् is right, but the long ई of ईशः must stay long.")],
            "वाक् + ईशः = वागीशः, like सम्यक् + अपि = सम्यगपि.",
            "क् + vowel → ग्.",
            teaches="A final क् becomes ग् before a vowel: सम्यक् + अपि → सम्यगपि."),
    ],
}

# ---------------------------------------------------------------- unit 130
AUTHORED["130"] = {
    "title": "बाह्येनापि च ज्वालांगारात्मकेनाग्निना",
    "question": "By unit 130, why must the agni within be protected with effort?",
    "rule": ("Even with outer fire of flame and embers (ज्वालाङ्गारात्मक), cooking is not at all times of one form (नैकाकारः सर्वदा पाकः); "
             "how much more (किमुत) with what is lodged within (अन्तराश्रय; 'heat' is the data's conjecture ऊष्मणा). "
             "So guard it with effort (प्रयत्नतो रक्षेत्)."),
    "limits": ("Prose, one printed line. The printed ष्ममना is not a word; ऊष्मणा ('by heat') is the data's conjecture, so no "
               "question rests on that word. 'It' (तम्) is read as the agni. The line gives no method of protection here."),
    "explain_hi": ("यह पंक्ति एक तर्क देती है: ज्वाला और अंगारों वाली बाहरी अग्नि से भी पाक हर बार एक-सा नहीं होता। "
                   "तो भीतर आश्रित (अन्तराश्रय) ताप से, सम होने पर भी, कहना ही क्या (किमुत)। "
                   "इसलिए उसकी प्रयत्न से रक्षा करनी चाहिए। "
                   "छपा ‘ष्ममना’ कोई शब्द नहीं; ‘ऊष्मणा’ (ताप से) डेटा का अनुमानित पाठ है, इस पर कोई प्रश्न नहीं। "
                   "‘किमुत’ = ‘तो फिर कहना ही क्या’: छोटी बात से बड़ी बात सिद्ध करने का शब्द।"),
    "hook": "बाहर की आग भी एक-सी नहीं पकाती, तो भीतर वाली का क्या कहना!",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 130, what is said of cooking with outer fire of flame and embers?",
            ("It is not always of one form", "नैकाकारः सर्वदा पाकोभवति: the cooking is not always one-formed."),
            [("It is always even and steady", "The line denies this: न एकाकारः सर्वदा."),
             ("It is the same as inner heat", "The line sets outer fire against the heat within."),
             ("It cooks only raw grain well", "No grain or kind of food is named.")],
            "Even outer fire does not always cook in one way.",
            "नैकाकारः सर्वदा पाकः."),
        order(1, "Put these printed phrases of unit 130 in the line's order.",
              ["बाह्येनापि च", "ज्वालांगारात्मकेनाग्निना", "नैकाकारः सर्वदा पाकोभवति", "समेनापि", "तस्मात्तं प्रयत्नतो रक्षेत्"],
              "Even by outer fire of flame and embers, cooking is not always one-formed ... even when even ... so guard it with effort.",
              "बाह्येनापि च → ज्वालांगारात्मकेनाग्निना → नैकाकारः सर्वदा पाकोभवति → समेनापि → तस्मात्तं प्रयत्नतो रक्षेत्."),
        match(2, "Match each word of unit 130 to its meaning.",
              [["बाह्य", "external"], ["ज्वाला", "flame"], ["अङ्गार", "embers"], ["आकार", "form"],
               ["प्रयत्नतः", "with effort"]],
              "Outer fire of flame and embers; cooking not of one form; guard with effort.",
              "बाह्य, ज्वाला, अङ्गार, आकार, प्रयत्नतः.", role="extend",
              teaches="किमुत means 'how much more, what to say of': from the outer fire it argues to the heat within."),
        mcq("discriminate", 3, "Which split of नैकाकारः in unit 130 is right?",
            ("न + एकाकारः", "अ + ए → ऐ: न + एकाकारः → नैकाकारः, 'not of one form'."),
            [("न + इकाकारः", "अ + इ gives ए, not ऐ; and इकाकार is not a word."),
             ("नै + काकारः", "नै and काकार are not words here."),
             ("न + एकाकरः", "That would print नैकाकरः; the print has -कारः.")],
            "न (not) + एक (one) + आकारः (form).",
            "अ + ए → ऐ."),
        multi("apply", 4, "Which statements fit unit 130?",
              [("The outer fire is made of flame and embers", "Right: ज्वालाङ्गारात्मकेन अग्निना."),
               ("Outer fire always cooks in one way", "The line says the opposite: न एकाकारः सर्वदा."),
               ("It ends: guard it with effort", "Right: तस्मात्तं प्रयत्नतो रक्षेत्."),
               ("It says inner heat cooks faster than outer fire", "No such comparison of speed is printed.")],
              [0, 2],
              "Outer fire of flame and embers is uneven; so guard the inner one with effort.",
              "बाह्य ... नैकाकारः; तस्मात्तं प्रयत्नतो रक्षेत्."),
        mcq("transfer", 5, "By the use of किमुत in unit 130, what does बालोऽपि जानाति किमुत वृद्धः mean (a new example)?",
            ("Even a boy knows; how much more an elder", "किमुत argues from the lesser case to the greater, as in unit 130."),
            [("A boy knows it, but an elder does not", "किमुत does not deny; it argues to the greater case."),
             ("Neither the boy nor the elder knows", "जानाति is affirmative; nothing is denied."),
             ("The elder knows more slowly than a boy", "Nothing is said about speed of knowing.")],
            "बालोऽपि जानाति, किमुत वृद्धः = even a boy knows, what to say of an elder.",
            "X अपि ..., किमुत Y = even X ..., how much more Y.",
            teaches="किमुत (how much more): even outer fire is uneven, how much more the heat within."),
    ],
}

# ---------------------------------------------------------------- unit 131
AUTHORED["131"] = {
    "title": "तत्र प्रवरेण सात्म्येन समं",
    "question": "By unit 131, how are 'the others' brought to equality and (it) then kept, and which remedies are named?",
    "rule": ("Gradually (क्रमशः) bringing the others to equality (साम्यमापाद्य) by the lesser (अवर), one keeps it by the best (प्रवर), "
             "with the Vāta-and-other remedies of the doṣa-treatment section and the medicine-and-exercise combinations prescribed for grahaṇī."),
    "limits": ("Prose; confidence low, elliptical. What प्रवर, अवर and इतरान् refer to is not stated; nothing is asked "
               "about their roles. दोषोपक्रमणीय is probably a chapter title (not verified); grahaṇī is probably a "
               "digestive disorder. No dose is given."),
    "explain_hi": ("यह गद्य-पंक्ति अग्नि की रक्षा का ढंग बताती है, पर वाक्य अधूरा-सा है (विश्वास निम्न)। "
                   "श्रेष्ठ (प्रवर) सात्म्य के साथ, अपने-अपने अनुसार निम्न (अवर) के द्वारा अन्यों को क्रमशः समता तक पहुँचाकर, श्रेष्ठ से उसकी रक्षा करे। "
                   "प्रवर, अवर और ‘अन्य’ किसके लिए हैं, यह नहीं कहा गया; इसलिए इन पर कोई प्रश्न नहीं। "
                   "साधन दो स्थानों से लिए जाते हैं: दोषोपक्रमणीय (सम्भवतः दोष-चिकित्सा का अध्याय) में कहे वात आदि के साधन, "
                   "और ग्रहणी रोग (सम्भवतः पाचन का विकार) में बताए औषध और व्यायाम के योग। "
                   "अन्त का ‘इति’ कथन को समाप्त करता है।"),
    "hook": "धीरे-धीरे समता, फिर श्रेष्ठ से रक्षा।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "In unit 131, what does क्रमशः साम्यमापाद्य mean?",
            ("Having gradually brought to equality", "क्रमशः = gradually; साम्यम् आपाद्य = having brought to equality."),
            [("Having suddenly broken the equality", "क्रमशः is gradual, and साम्य is reached, not broken."),
             ("Having first measured all the doṣas", "No measuring is printed."),
             ("Having given up every kind of food", "No giving up of food is printed.")],
            "Gradually bringing to equality, then keeping by the best.",
            "क्रमशः साम्यम् आपाद्य."),
        order(1, "Put these parts of unit 131 in the line's order.",
              ["तत्र प्रवरेण सात्म्येन समं", "यथास्वमवरेणेतरान्", "क्रमशः साम्यमापाद्य", "वातादिसाधनेन",
               "ग्रहणीरोगविहितैश्चौषधव्यायामयोगैरिति"],
              "With the best sātmya; by the lesser the others; gradually to equality; by the Vāta-and-other remedy; by medicine-exercise combinations.",
              "तत्र प्रवरेण सात्म्येन समं → यथास्वमवरेणेतरान् → क्रमशः साम्यमापाद्य → वातादिसाधनेन → ग्रहणीरोगविहितैश्चौषधव्यायामयोगैरिति."),
        match(2, "Match each word of unit 131 to its meaning.",
              [["प्रवर", "best"], ["अवर", "lesser"], ["सात्म्य", "what suits"], ["साम्य", "equality"],
               ["व्यायाम", "exercise"]],
              "प्रवर best, अवर lesser, सात्म्य what suits, साम्य equality, व्यायाम exercise.",
              "प्रवर, अवर, सात्म्य, साम्य, व्यायाम.", role="extend",
              teaches="प्रवर and अवर are a pair (best and lesser); this line does not say what each refers to."),
        mcq("discriminate", 3, "Which split of विहितैश्चौषध in unit 131 is right?",
            ("विहितैः + च + औषध", "ऐः before च → ऐश्; अ + औ → औ: विहितैश्चौषध."),
            [("विहिते + च + औषध", "ए before च stays ए: it would print विहिते च."),
             ("विहितैः + चः + औषध", "चः is not a word; the word is च, 'and'."),
             ("विहितैः + च + उषध", "अ + उ gives ओ, not औ; the print has चौ.")],
            "विहितैः (prescribed) + च (and) + औषध (medicine).",
            "Visarga + च → श्च; अ + औ → औ."),
        multi("apply", 4, "Which statements fit unit 131?",
              [("The line gives a dose for each medicine", "No dose is printed."),
               ("Remedies for Vāta and the like come from the doṣa-treatment section", "Right: दोषोपक्रमणीयोक्तेन वातादिसाधनेन (probably a chapter title)."),
               ("The line says what the lesser (avara) refers to", "What अवर refers to is not stated."),
               ("Medicine-and-exercise combinations are those prescribed in grahaṇī", "Right: ग्रहणीरोगविहितैः औषधव्यायामयोगैः (probably a digestive disorder).")],
              [1, 3],
              "Two named sources of means; no doses, and no referents for प्रवर / अवर.",
              "वातादिसाधनेन, ग्रहणीरोगविहितैः औषधव्यायामयोगैः."),
        mcq("transfer", 5, "By the rule of अवरेण + इतरान् → अवरेणेतरान्, how is रामेण + इति joined in a new example?",
            ("रामेणेति", "अ + इ → ए, as अवरेण + इतरान् → अवरेणेतरान्."),
            [("रामेणीति", "अ + इ does not give a long ई."),
             ("रामेणैति", "ऐ comes from अ + ए or ऐ, not from अ + इ."),
             ("रामेण्यति", "य् comes from इ before a different vowel, not from अ.")],
            "रामेण + इति = रामेणेति, like अवरेण + इतरान् = अवरेणेतरान्.",
            "अ + इ → ए.",
            teaches="A final अ and an initial इ join as ए: अवरेण + इतरान् → अवरेणेतरान्."),
    ],
}

# ---------------------------------------------------------------- unit 132
AUTHORED["132"] = {
    "title": "भवति चात्र",
    "question": "What is the job of the short formula in unit 132?",
    "rule": "भवति च अत्र, 'and on this matter there are': a lead-in formula; the verses after it (from unit 133) appear to be its content.",
    "limits": "Prose formula with no object of its own; it teaches nothing by itself. That the verses from unit 133 on are its content is the data's 'appears'.",
    "explain_hi": ("‘भवति चात्र’ = ‘और इस विषय में (ये) हैं’। "
                   "गद्य-भाग के बाद यह पंक्ति श्लोकों को लाती है; इकाई १३३ से आगे के श्लोक इसके विषय दिखते हैं। "
                   "इस पंक्ति का अपना कोई विषय-शब्द नहीं। "
                   "‘चात्र’ में च + अत्र जुड़े हैं (अ + अ → आ)।"),
    "hook": "‘भवति चात्र’: अब संग्रह-श्लोक।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "What does भवति चात्र (unit 132) do?",
            ("It leads in to the verses that follow", "A lead-in formula; the verses from unit 133 appear to be its content."),
            [("It closes the sixth chapter at this point", "The chapter's closing line is unit 141."),
             ("It names the four kinds of agni here", "The four kinds are named in unit 125."),
             ("It gives a cure for the manda agni", "No cure is printed in these two words.")],
            "A formula that brings in the verses after it.",
            "भवति चात्र = and on this there are (verses)."),
        match(1, "Match each word of unit 132 to its meaning.",
              [["भवति", "there is / are"], ["च", "and"], ["अत्र", "on this matter"]],
              "And on this matter there are (verses).",
              "भवति, च, अत्र."),
        fill(2, "In the lead-in formula of unit 132, the verb meaning there is / are is ____ (type it in Devanagari or in English letters, e.g. dharma).",
             accepts("भवति", None, "bhavati"),
             "भवति = there is / are (3 sg. present of √भू).",
             "भवति, from √भू (be), opens the lead-in formula.",
             "भवति = there is / are."),
        mcq("discriminate", 3, "Which split of चात्र in unit 132 is right?",
            ("च + अत्र", "अ + अ → आ: च + अत्र = चात्र."),
            [("चे + अत्र", "ए + अ would print चेऽत्र, not चात्र."),
             ("च + आत्र", "आत्र is not a word."),
             ("चा + त्र", "चा and त्र are not words here.")],
            "च (and) + अत्र (on this matter): अ + अ → आ.",
            "अ + अ → आ."),
        multi("apply", 4, "Which statements about unit 132 are right?",
              [("It contains the verb भवति", "Right: 3 sg. present of √भू, 'there is'."),
               ("It is itself a metrical verse", "It is a prose formula."),
               ("It states what the coming verses are about", "It has no stated object."),
               ("The verses from unit 133 appear to be its content", "Right: the data reads them so ('appear').")],
              [0, 3],
              "A prose lead-in with the verb भवति; the verses after it appear to be its content.",
              "भवति च अत्र."),
        mcq("transfer", 5, "By the rule of च + अत्र → चात्र, how is तत्र + अपि joined in a new example?",
            ("तत्रापि", "अ + अ → आ, as च + अत्र → चात्र."),
            [("तत्रपि", "Two short अ join as a long आ, not a short अ."),
             ("तत्रेपि", "ए comes from अ + इ, not from अ + अ."),
             ("तत्रोपि", "ओ comes from अ + उ, not from अ + अ.")],
            "तत्र + अपि = तत्रापि, like च + अत्र = चात्र.",
            "अ + अ → आ.",
            teaches="A final अ and an initial अ join as a long आ: च + अत्र → चात्र."),
    ],
}

# ---------------------------------------------------------------- unit 133
AUTHORED["133"] = {
    "title": "स्वधातुसमवर्णांनि",
    "question": "By the verse of unit 133, what are the srotas (channels) like in colour and form?",
    "rule": ("The srotas (स्रोतांसि) have the colour of their own dhātu (स्वधातुसमवर्ण), are round (वृत्त), thick (स्थूल) and fine (अणु), "
             "long in form (दीर्घाण्याकृत्या), and like tendrils (प्रतानसदृश, probable)."),
    "limits": ("One verse, two printed lines; स्रोतांसि is named in the second line, the copula understood. Which srotas "
               "are thick and which fine is not said. प्रतान = tendril is probable, so no question rests on it. "
               "Printed वर्णांनि = वर्णानि."),
    "explain_hi": ("यह संग्रह-श्लोक स्रोतस् (शरीर के मार्ग) का रूप बताता है। "
                   "वे अपने-अपने धातु के समान रंग वाले हैं; गोल, मोटे और बारीक; आकृति में लम्बे; और प्रतान के समान (सम्भवतः लता के तन्तु)। "
                   "पहली पंक्ति के विशेषणों का विशेष्य ‘स्रोतांसि’ दूसरी पंक्ति में आता है। "
                   "‘मोटे और बारीक’ साथ छपे हैं; कौन-से स्रोतस् कैसे हैं, यह नहीं कहा गया। "
                   "छपा ‘वर्णांनि’ = वर्णानि (न से पहले अनुस्वार की छपाई-भूल)।"),
    "hook": "स्रोतस्: धातु-रंग, गोल, मोटे-बारीक, लम्बे, लता-तन्तु जैसे।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 133, what colour are the srotas (channels)?",
            ("The colour of their own dhātu", "स्वधातुसमवर्णानि: equal in colour to their own dhātu."),
            [("Always red, like the blood", "No one colour is given; each has its own dhātu's colour."),
             ("White, like milk or foam", "No such colour is printed."),
             ("Dark, like smoke or soot", "No such colour is printed.")],
            "Each srotas has the colour of its own dhātu.",
            "स्व-धातु-सम-वर्ण."),
        order(1, "Put these printed parts of the verse of unit 133 in order.",
              ["स्वधातुसमवर्णांनि", "वृत्तस्थूलान्यणूनि च", "स्रोतांसि", "दीर्घाण्याकृत्या", "प्रतानसदृशानि च"],
              "Own-dhātu-coloured; round, thick and fine; the srotas; long in form; like tendrils.",
              "स्वधातुसमवर्णांनि → वृत्तस्थूलान्यणूनि च → स्रोतांसि → दीर्घाण्याकृत्या → प्रतानसदृशानि च."),
        match(2, "Match each word of unit 133 to its meaning.",
              [["वृत्त", "round"], ["स्थूल", "thick"], ["अणु", "fine, minute"], ["दीर्घ", "long"],
               ["आकृति", "form"]],
              "वृत्त round, स्थूल thick, अणु fine, दीर्घ long, आकृति form.",
              "वृत्त, स्थूल, अणु, दीर्घ, आकृति.", role="extend",
              teaches="स्रोतस् (neuter, plural स्रोतांसि) are the body's channels; the verse gives their colour and shape."),
        mcq("discriminate", 3, "Which pair of opposite words does unit 133 print side by side for the srotas?",
            ("स्थूल (thick) and अणु (fine)", "वृत्तस्थूलान्यणूनि: thick and fine are both printed."),
            [("दीर्घ (long) and ह्रस्व (short)", "दीर्घ is printed, but ह्रस्व is not."),
             ("वृत्त (round) and चतुरस्र (square)", "वृत्त is printed, but चतुरस्र is not."),
             ("शुक्ल (white) and कृष्ण (black)", "No colour words are printed; colour follows the dhātu.")],
            "Thick (स्थूल) and fine (अणु) stand together in the first line.",
            "वृत्त-स्थूलानि अणूनि च."),
        mcq("apply", 4, "Which split of वृत्तस्थूलान्यणूनि in unit 133 is right?",
            ("वृत्तस्थूलानि + अणूनि", "इ before the unlike vowel अ → य्: -लान्यणूनि."),
            [("वृत्तस्थूलान् + यणूनि", "यणूनि is not a word; the य् comes from the इ of -आनि."),
             ("वृत्तस्थूलाने + अणूनि", "ए + अ would print -लानेऽणूनि."),
             ("वृत्तस्थूलान्य + अणूनि", "अ + अ would give आ: -न्याणूनि.")],
            "वृत्तस्थूलानि (round, thick) + अणूनि (fine).",
            "इ + unlike vowel → य्."),
        mcq("transfer", 5, "By the rule of वृत्तस्थूलानि + अणूनि, how is फलानि + अत्र joined in a new example?",
            ("फलान्यत्र", "इ before the unlike vowel अ → य्, as in वृत्तस्थूलान्यणूनि."),
            [("फलानियत्र", "The इ does not stay and add a य्; it becomes य्."),
             ("फलानेऽत्र", "ए with ऽ comes from ए + अ, not from इ + अ."),
             ("फलानात्र", "आ comes from अ + अ, not from इ + अ.")],
            "फलानि + अत्र = फलान्यत्र, like वृत्तस्थूलानि + अणूनि = वृत्तस्थूलान्यणूनि.",
            "इ + अ → य.",
            teaches="A final इ before अ becomes य्: वृत्तस्थूलानि + अणूनि → वृत्तस्थूलान्यणूनि."),
    ],
}

# ---------------------------------------------------------------- unit 134
AUTHORED["134"] = {
    "title": "आहारश्च विहारश्च",
    "question": "By the verse of unit 134, which food and conduct defile the srotas?",
    "rule": ("Food (आहार) and conduct (विहार) which are equal to the doṣas in qualities (दोषगुणैः समः), and which are unlike the "
             "dhātus in quality (धातुभिर्विगुणः): that is the defiler of the srotas (स्रोतसां प्रदूषकः). Whether both must hold together is not said."),
    "limits": ("One verse over two printed lines, one sentence. यः is masculine singular for both nouns ('whichever'). विगुण is "
               "read as 'unlike in quality'; 'defective in quality' is another reading, so no question turns on that choice. "
               "No doṣa, food or habit is named."),
    "explain_hi": ("यह श्लोक स्रोतस् के दूषित होने का कारण बताता है। "
                   "जो आहार और विहार (आचरण, दिनचर्या) दोषों के गुणों के समान हो, और जो धातुओं से भिन्न गुण वाला हो, वह स्रोतसों को दूषित करता है (दोनों साथ चाहिए या कोई एक, यह नहीं कहा)। "
                   "‘यः ... सः’ (जो ... वह) से दोनों पंक्तियाँ एक वाक्य बनती हैं। "
                   "‘विगुण’ को ‘भिन्न गुण वाला’ पढ़ा गया; ‘दोषपूर्ण गुण वाला’ भी सम्भव। "
                   "कोई विशेष दोष, आहार या आदत नहीं गिनाई गई।"),
    "hook": "दोष जैसा, धातु से उलटा: वही स्रोतस् बिगाड़े।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 134, how does food or conduct that defiles the srotas stand to the doṣas?",
            ("It is equal to them in qualities", "दोषगुणैः समः: equal to the doṣas in qualities."),
            [("It is equal to the dhātus in qualities", "Toward the dhātus it is विगुण, not equal."),
             ("It is opposite to all of the doṣas", "The verse says equal (सम), not opposite."),
             ("It has no bearing on the doṣas at all", "The verse links it to the doṣas' qualities.")],
            "Equal to the doṣas in qualities, unlike the dhātus: that defiles the srotas.",
            "दोषगुणैः समः."),
        order(1, "Put the printed quarter-lines of unit 134 in order.",
              ["आहारश्च विहारश्च", "यः स्याद्दोषगुणैः समः", "धातुभिर्विगुणो यश्च", "स्रोतसां स प्रदूषकः"],
              "Food and conduct, which is equal to the doṣas in qualities, and which is unlike the dhātus: that defiles the srotas.",
              "आहारश्च विहारश्च → यः स्याद्दोषगुणैः समः → धातुभिर्विगुणो यश्च → स्रोतसां स प्रदूषकः."),
        match(2, "Match each word of unit 134 to its meaning.",
              [["आहार", "food"], ["विहार", "conduct, regimen"], ["गुण", "quality"], ["सम", "equal"],
               ["प्रदूषक", "defiler"]],
              "आहार food, विहार conduct, गुण quality, सम equal, प्रदूषक defiler.",
              "आहार, विहार, गुण, सम, प्रदूषक.", role="extend",
              teaches="यः ... सः (which ... that): a relative clause in the first lines, the main clause स प्रदूषकः at the end."),
        mcq("discriminate", 3, "In धातुभिर्विगुणो of unit 134, why is the visarga of धातुभिः written र्?",
            ("It follows इ and stands before the voiced व", "After a vowel other than अ/आ, visarga before a voiced sound → र्."),
            [("Every visarga becomes र् before a consonant", "Before त it becomes स्, before च श्; not every consonant."),
             ("It follows अ and stands before the voiced व", "The vowel before it is इ (-भिः); अः would give ओ."),
             ("र् is part of the stem of the word", "The stem is धातु; -भिः is the ending, and its visarga becomes र्.")],
            "धातुभिः + विगुणः: इः before the voiced व → इर्.",
            "इः / उः + voiced sound → इर् / उर्."),
        multi("apply", 4, "Which statements fit the verse of unit 134?",
              [("It names the doṣa that does the harm", "No single doṣa is named."),
               ("Both food and conduct can defile the srotas", "Right: आहारश्च विहारश्च."),
               ("Equality with the doṣas' qualities is named as a cause", "Right: दोषगुणैः समः."),
               ("Likeness to the dhātus defiles the srotas", "Toward the dhātus it is विगुण, not alike.")],
              [1, 2],
              "Food or conduct like the doṣas and unlike the dhātus defiles the srotas.",
              "दोषगुणैः समः, धातुभिर्विगुणः."),
        mcq("transfer", 5, "By the rule of विगुणः + यः → विगुणो यः, how is रामः + याति joined in a new example?",
            ("रामो याति", "अः before the voiced consonant य → ओ, as विगुणो यः."),
            [("रामर्याति", "र् comes from a visarga after vowels other than अ/आ."),
             ("रामा याति", "The vowel is not lengthened; अः before a voiced consonant gives ओ."),
             ("राम याति", "अः drops to अ only before vowels other than अ, not before य.")],
            "रामः + याति = रामो याति, like विगुणः + यः = विगुणो यः.",
            "अः + voiced consonant → ओ.",
            teaches="अः before a voiced consonant becomes ओ: विगुणः + यश्च → विगुणो यश्च."),
    ],
}

# ---------------------------------------------------------------- unit 135
AUTHORED["135"] = {
    "title": "अतिप्रवृत्तिः संगो वा",
    "question": "By the verse of unit 135, what are the signs of vitiated srotas?",
    "rule": ("Signs of vitiation (दुष्टिलक्षण) of the srotas: excessive flow (अतिप्रवृत्ति), obstruction (सङ्ग), knots (ग्रन्थि) of the "
             "sirās (probably veins), and a fourth item with a damaged word (विमार्गप्तो) and गमन, 'going'."),
    "limits": ("One verse over two printed lines; confidence low for the damaged word only. विमार्गप्तो is not a word as printed; "
               "'having reached a wrong path' or 'going by a wrong path' are only guesses, so no question touches the fourth "
               "item. No cause or cure is given."),
    "explain_hi": ("यह श्लोक स्रोतसों के दूषित होने (दुष्टि) के लक्षण गिनाता है। "
                   "पक्के छपे लक्षण तीन हैं: अतिप्रवृत्ति (अत्यधिक प्रवाह), सङ्ग (रुकावट), और सिराओं (सम्भवतः नसों) की ग्रन्थियाँ (गाँठें)। "
                   "चौथा लक्षण ‘विमार्गप्तो वा गमनं’ में छपा है; ‘विमार्गप्तो’ क्षतिग्रस्त, अस्पष्ट शब्द है (सम्भवतः ‘गलत मार्ग’ से जुड़ा), इस पर कोई प्रश्न नहीं। "
                   "हर लक्षण के बीच ‘वा’ (या) है: इनमें से कोई भी लक्षण हो सकता है। "
                   "कारण या चिकित्सा यहाँ नहीं दी गई।"),
    "hook": "स्रोतस् बिगड़े तो: बहुत बहना, रुकना, गाँठ पड़ना।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "Which of these does unit 135 print as a sign of vitiated srotas?",
            ("Excessive flow (atipravṛtti)", "अतिप्रवृत्तिः is the first printed sign."),
            [("A change in the colour of the skin", "Skin colour is not printed in unit 135."),
             ("Loss of sleep through the night", "Sleep is not printed in unit 135."),
             ("Swelling of every joint (sandhi)", "Joints are not printed in unit 135.")],
            "Excessive flow, obstruction, knots of the sirās ...: signs of vitiated srotas.",
            "अतिप्रवृत्तिः सङ्गो वा ... स्रोतसां दुष्टिलक्षणम्."),
        order(1, "Put these printed parts of unit 135 in order (the damaged phrase is left out).",
              ["अतिप्रवृत्तिः", "संगो वा", "सिराणांग्रंथयोऽपि वा", "स्रोतसां दुष्टिलक्षणं"],
              "Excessive flow, or obstruction, or also knots of the sirās, ... the sign of vitiated srotas.",
              "अतिप्रवृत्तिः → संगो वा → सिराणांग्रंथयोऽपि वा → स्रोतसां दुष्टिलक्षणं."),
        match(2, "Match each word of unit 135 to its meaning.",
              [["अतिप्रवृत्ति", "excessive flow"], ["सङ्ग", "obstruction"], ["ग्रन्थि", "knot"], ["दुष्टि", "vitiation"],
               ["लक्षण", "sign"]],
              "अतिप्रवृत्ति excessive flow, सङ्ग obstruction, ग्रन्थि knot, दुष्टि vitiation, लक्षण sign.",
              "अतिप्रवृत्ति, सङ्ग, ग्रन्थि, दुष्टि, लक्षण.", role="extend",
              teaches="वा ... वा (or ... or): each printed item alone is a sign of vitiated srotas."),
        mcq("discriminate", 3, "Which split of संगो वा in unit 135 is right?",
            ("सङ्गः + वा", "अः before the voiced व → ओ; ं in the print stands for ङ्."),
            [("सङ्गे + वा", "ए before व stays ए: it would print सङ्गे वा."),
             ("सङ्गम् + वा", "म् before व is written ं: it would print सङ्गं वा."),
             ("सङ्गा + वा", "आ before व stays आ: it would print सङ्गा वा.")],
            "सङ्गः (obstruction) + वा (or): अः + voiced consonant → ओ.",
            "अः + voiced consonant → ओ."),
        multi("apply", 4, "Which statements fit unit 135?",
              [("Obstruction (saṅga) is one of the signs", "Right: सङ्गो वा."),
               ("The verse says which doṣa causes each sign", "No doṣa is named."),
               ("The verse gives a cure for vitiated srotas", "No cure is printed."),
               ("Knots of the sirās are one of the signs", "Right: सिराणां ग्रन्थयोऽपि वा (sirā, probably veins).")],
              [0, 3],
              "Signs only: excessive flow, obstruction, knots of the sirās, and a damaged fourth item.",
              "अतिप्रवृत्तिः सङ्गो वा सिराणां ग्रन्थयोऽपि वा."),
        mcq("transfer", 5, "By the rule of ग्रन्थयः + अपि → ग्रन्थयोऽपि, how is बालः + अत्र joined in a new example?",
            ("बालोऽत्र", "अः + अ → ओ, and ऽ marks the lost अ, as in ग्रन्थयोऽपि."),
            [("बाल अत्र", "अः becomes अ only before vowels other than अ."),
             ("बाला अत्र", "आ with a gap comes from आः, not from अः."),
             ("बालरत्र", "र् comes from a visarga after vowels other than अ/आ.")],
            "बालः + अत्र = बालोऽत्र, like ग्रन्थयः + अपि = ग्रन्थयोऽपि.",
            "अः + अ → ओऽ.",
            teaches="अः before अ becomes ओ and the अ is marked ऽ: ग्रन्थयः + अपि → ग्रन्थयोऽपि."),
    ],
}

# ---------------------------------------------------------------- unit 136
AUTHORED["136"] = {
    "title": "बिसानामिव सूक्ष्माणि",
    "question": "By the verse of unit 136, what are the openings (dvāra) of the srotas like, and what do they do?",
    "rule": ("The openings (द्वाराणि) of the srotas in the body are fine like those of lotus stalks (बिस, Nelumbo nucifera, standard) "
             "and spread far (दूरं विप्रसृतानि); through them rasa is built up (रसो यैरुपचीयते)."),
    "limits": ("One verse over two printed lines; the noun described (द्वाराणि) comes in the second line, the copula is understood. "
               "बिस = lotus stalk or root fibre. The verse does not say how many openings there are or where."),
    "explain_hi": ("यह श्लोक स्रोतसों के द्वारों (मुखों) का वर्णन करता है। "
                   "वे बिस (कमलनाल या उसके तन्तु; Nelumbo nucifera, मानक) जैसे सूक्ष्म हैं और दूर तक फैले हैं। "
                   "इन्हीं द्वारों से देह में रस का उपचय (वृद्धि, पोषण) होता है। "
                   "पहली पंक्ति के विशेषणों का विशेष्य ‘द्वाराणि’ दूसरी पंक्ति में है। "
                   "‘उपचीयते’ कर्मवाच्य है: ‘बढ़ाया जाता है’।"),
    "hook": "कमलनाल-से बारीक द्वार, जिनसे रस बढ़ता है।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 136, what are the openings of the srotas compared to?",
            ("Lotus stalks, for their fineness", "बिसानामिव सूक्ष्माणि: fine like those of lotus stalks."),
            [("The hairs of the head, for number", "Hair is not named in unit 136."),
             ("Threads of a web, for their pattern", "No web is named in unit 136."),
             ("Grains of sand, for their dryness", "No sand is named in unit 136.")],
            "Fine like lotus stalks and spread far.",
            "बिसानामिव सूक्ष्माणि."),
        order(1, "Put the printed quarter-lines of unit 136 in order.",
              ["बिसानामिव सूक्ष्माणि", "दूरं विप्रसृतानि च", "द्वाराणि स्रोतसां देहे", "रसोयैरुपचीयते"],
              "Fine like lotus stalks, and spread far: the openings of the srotas in the body, through which rasa is built up.",
              "बिसानामिव सूक्ष्माणि → दूरं विप्रसृतानि च → द्वाराणि स्रोतसां देहे → रसोयैरुपचीयते."),
        match(2, "Match each word of unit 136 to its meaning.",
              [["बिस", "lotus stalk"], ["सूक्ष्म", "fine"], ["विप्रसृत", "spread out"], ["द्वार", "opening"],
               ["उपचीयते", "is built up"]],
              "बिस lotus stalk, सूक्ष्म fine, विप्रसृत spread out, द्वार opening, उपचीयते is built up.",
              "बिस, सूक्ष्म, विप्रसृत, द्वार, उपचीयते.", role="extend",
              teaches="इव (like) follows the thing compared: बिसानाम् इव = like (those) of lotus stalks."),
        mcq("discriminate", 3, "Which split of रसोयैरुपचीयते in unit 136 is right?",
            ("रसः + यैः + उपचीयते", "अः before the voiced य → ओ; ऐः before a vowel → ऐर्."),
            [("रसे + यैः + उपचीयते", "ए before य stays ए: it would print रसे यैः."),
             ("रसः + यैः + अपचीयते", "That would print यैरप-; the print has यैरुप-."),
             ("रसम् + यैः + उपचीयते", "म् before य is written ं: it would print रसं यैः.")],
            "रसः (rasa) + यैः (by which) + उपचीयते (is built up).",
            "अः + voiced consonant → ओ; ऐः + vowel → ऐर्."),
        multi("apply", 4, "Which statements fit the verse of unit 136?",
              [("The openings are fine like lotus stalks", "Right: बिसानामिव सूक्ष्माणि."),
               ("Through the openings rasa is built up", "Right: रसो यैरुपचीयते."),
               ("The verse gives the number of openings", "No number is printed."),
               ("The openings spread far", "Right: दूरं विप्रसृतानि.")],
              [0, 1, 3],
              "Fine, far-spread openings through which rasa is built up; no number is given.",
              "सूक्ष्माणि, दूरं विप्रसृतानि, रसो यैरुपचीयते."),
        mcq("transfer", 5, "उपचीयते in unit 136 is passive (is built up). What does अन्नं पच्यते mean (a new example)?",
            ("Food is being cooked", "पच्यते is the passive of √पच्, like उपचीयते of उप-√चि."),
            [("Food cooks something", "The passive does not take an object here."),
             ("Food will be cooked", "पच्यते is present, not future."),
             ("Food was cooked", "पच्यते is present, not past.")],
            "अन्नं पच्यते = food is (being) cooked; रसो यैरुपचीयते = by which rasa is built up.",
            "Passive present (as here): -यते with the doer, if any, in the instrumental; not every -यते is passive.",
            teaches="उपचीयते is the present passive (gram: pass.) of उप-√चि; not every -यते is passive, but this one is."),
    ],
}

# ---------------------------------------------------------------- unit 137
AUTHORED["137"] = {
    "title": "केचिदाहुरहोरात्रात्",
    "question": "By the verse of unit 137, what do the different views say about how long food takes to become śukra?",
    "rule": ("Views differ on how soon food (अन्न) reaches the state of śukra (शुक्रत्व) by the sequence of cooking (पाकक्रमात्): some "
             "(केचित्) say from a day and night, others (अपरे) from six days; a month (मासात्) is also printed."),
    "limits": ("One verse over two printed lines. The period of the third group (परे) is not stated; the month printed next may "
               "belong with it, so no question pairs परे with the month. The verse does not say which view is right; इति closes the views."),
    "explain_hi": ("यह श्लोक मतभेद बताता है: अन्न पाक के क्रम से कितने समय में शुक्रत्व (वीर्य की अवस्था) तक पहुँचता है। "
                   "कुछ (केचित्) कहते हैं अहोरात्र (एक दिन-रात) से, दूसरे (अपरे) षडह (छह दिन) से, और अन्य (परे)। "
                   "दूसरी पंक्ति में ‘मास से’ छपा है; यह तीसरे मत (परे) का हो सकता है, पर पंक्ति साफ़ नहीं कहती। "
                   "कौन-सा मत ठीक है, यह यहाँ नहीं कहा गया। "
                   "अन्त का ‘इति’ मतों को बन्द करता है।"),
    "hook": "अन्न से शुक्र: एक दिन? छह दिन? एक मास?",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 137, what do the different views disagree about?",
            ("How long food takes to become śukra", "प्रयाति शुक्रत्वमन्नं: when food reaches the state of śukra."),
            [("How many dhātus the body holds", "No count of dhātus is printed in unit 137."),
             ("Which season best suits a meal", "No season is printed in unit 137."),
             ("Whether food needs any cooking", "The verse takes the sequence of cooking for granted.")],
            "The views differ on the time food takes to reach the state of śukra.",
            "केचित् ... अपरे ... परे ... प्रयाति शुक्रत्वम् अन्नम्."),
        order(1, "Put the printed parts of the verse of unit 137 in order.",
              ["केचिदाहुरहोरात्रात्", "षडहादपरे", "परे", "मासात्प्रयातिशुक्रत्वमन्नं", "पाकक्रमादिति"],
              "Some say from a day and night, others from six days, others ...; from a month food reaches śukra, by the sequence of cooking.",
              "केचिदाहुरहोरात्रात् → षडहादपरे → परे → मासात्प्रयातिशुक्रत्वमन्नं → पाकक्रमादिति."),
        match(2, "Match each word of unit 137 to its meaning.",
              [["अहोरात्र", "a day and night"], ["षडह", "six days"], ["मास", "a month"], ["शुक्रत्व", "state of śukra"],
               ["पाकक्रम", "sequence of cooking"]],
              "अहोरात्र a day and night, षडह six days, मास a month, शुक्रत्व state of śukra, पाकक्रम sequence of cooking.",
              "अहोरात्र, षडह, मास, शुक्रत्व, पाकक्रम.", role="extend",
              teaches="केचित् ... अपरे ... परे (some ... others ... still others) is the frame for listing views."),
        mcq("discriminate", 3, "By unit 137, which period do the others (अपरे) give?",
            ("Six days", "षडहादपरे: others, from six days."),
            [("A day and night", "A day and night is the view of केचित्, 'some'."),
             ("A whole month", "The month is not printed with अपरे."),
             ("A fortnight", "No fortnight is printed in unit 137.")],
            "केचित्: a day and night; अपरे: six days.",
            "षडहात् अपरे."),
        multi("apply", 4, "Which statements fit the verse of unit 137?",
              [("A month (मास) is printed as a period", "Right: मासात् प्रयाति ... is printed."),
               ("The verse decides which view is right", "No view is chosen."),
               ("Food reaches śukra by the sequence of cooking", "Right: पाकक्रमात्."),
               ("The verse names three dhātus in the chain", "No dhātu besides śukra is named.")],
              [0, 2],
              "Several periods are reported; the change is by the sequence of cooking; no view is chosen.",
              "मासात् प्रयाति शुक्रत्वम् अन्नम् पाकक्रमात्."),
        mcq("transfer", 5, "By the rule of केचित् + आहुः → केचिदाहुः, how is कश्चित् + आगच्छति joined in a new example?",
            ("कश्चिदागच्छति", "त् before a vowel → द्, as केचित् + आहुः → केचिदाहुः."),
            [("कश्चितागच्छति", "त् does not stay त् before a vowel when words are joined."),
             ("कश्चिनागच्छति", "न् comes (optionally) from त् before a nasal, not before a vowel."),
             ("कश्चिच्चागच्छति", "च्च comes from त् before च, not before a vowel.")],
            "कश्चित् + आगच्छति = कश्चिदागच्छति, like केचित् + आहुः = केचिदाहुः.",
            "त् + vowel → द्.",
            teaches="A final त् becomes द् before a vowel: केचित् + आहुः → केचिदाहुः."),
    ],
}

# ---------------------------------------------------------------- unit 138
AUTHORED["138"] = {
    "title": "वृष्यादीनि प्रभावात्तु",
    "question": "By the verse of unit 138, how do vṛṣya (virility-promoting) things act on śukra?",
    "rule": ("But (तु) vṛṣya things and the like, through prabhāva (special potency, प्रभावात्), make śukra and the like at once "
             "(सद्यः). The second line (other medicine, from a day and night) is read with low confidence."),
    "limits": ("One verse over two printed lines; confidence low. The noun of वृष्यादीनि (drugs or foods) is not stated. In the "
               "second line the object of करोति is not stated, so no question rests on what other medicine does. No dose or "
               "named drug is given."),
    "explain_hi": ("इकाई १३७ में अन्न के धीरे-धीरे शुक्र बनने के मत थे; यह श्लोक ‘तु’ (परन्तु) से अलग बात कहता है। "
                   "वृष्य (शुक्र बढ़ाने वाले) आदि अपने प्रभाव (विशेष शक्ति) से तुरन्त (सद्यः) शुक्र आदि बना देते हैं। "
                   "‘वृष्यादीनि’ किसके लिए है (औषध या आहार), यह नहीं कहा गया। "
                   "दूसरी पंक्ति (‘प्रायः ... अहोरात्रात् ... भेषजम्’) का अर्थ अनिश्चित है: करोति का कर्म नहीं छपा; इस पर कोई प्रश्न नहीं। "
                   "कोई मात्रा या औषध का नाम नहीं दिया गया।"),
    "hook": "वृष्य: प्रभाव से तुरन्त शुक्र।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 138, how soon do vṛṣya things make śukra, and by what?",
            ("At once, through prabhāva", "प्रभावात्तु सद्यः शुक्रादि कुर्वन्ते."),
            [("After a month, by cooking", "A month and the sequence of cooking belong to food (unit 137)."),
             ("After six days, by taste", "Six days is a view about food (unit 137); taste is not named."),
             ("Never; they only weaken it", "The verse says they make śukra and the like.")],
            "Vṛṣya things make śukra and the like at once, by prabhāva.",
            "प्रभावात् ... सद्यः."),
        order(1, "Put these printed words of unit 138 in order (one long joined word is left out).",
              ["वृष्यादीनि", "प्रभावात्तु", "सद्यः", "शुक्रादिकुर्वंते", "प्रायः", "भेषजं"],
              "Vṛṣya and the like, but by prabhāva, at once make śukra and the like; generally ... medicine.",
              "वृष्यादीनि → प्रभावात्तु → सद्यः → शुक्रादिकुर्वंते → प्रायः → भेषजं."),
        match(2, "Match each word of unit 138 to its meaning.",
              [["वृष्य", "virility-promoting"], ["प्रभाव", "special potency"], ["सद्यः", "at once"],
               ["प्रायः", "generally"], ["भेषज", "medicine"]],
              "वृष्य virility-promoting, प्रभाव special potency, सद्यः at once, प्रायः generally, भेषज medicine.",
              "वृष्य, प्रभाव, सद्यः, प्रायः, भेषज.", role="extend",
              teaches="प्रभाव is a special potency whose action is not reasoned out from the other properties."),
        mcq("discriminate", 3, "Which split of प्रभावात्तु in unit 138 is right?",
            ("प्रभावात् + तु", "त् before त stays त्: प्रभावात् + तु = प्रभावात्तु."),
            [("प्रभावा + त्तु", "त्तु is not a word; the word is तु, 'but'."),
             ("प्रभावात्त + उ", "अ + उ would give ओ: -त्तो, not -त्तु."),
             ("प्रभावम् + तु", "म् before त is written ं: it would print प्रभावं तु.")],
            "प्रभावात् (through prabhāva) + तु (but).",
            "त् + त → त्त."),
        mcq("apply", 4, "Unit 137 has food reach śukra over time. Which word of unit 138 marks its contrast with that?",
            ("तु (but)", "प्रभावात्तु: तु, 'but', sets vṛṣya things against the food views of unit 137."),
            [("सद्यः (at once)", "सद्यः gives the time, not the contrast."),
             ("प्रायः (generally)", "प्रायः belongs to the second line, 'generally'."),
             ("अपि (also)", "अपि means 'also', not 'but'.")],
            "तु (but) marks the contrast: vṛṣya things act at once (सद्यः) by prabhāva.",
            "वृष्यादीनि प्रभावात्तु सद्यः."),
        mcq("transfer", 5, "By the rule of शुक्र + आदि → शुक्रादि, how is अन्न + आदि joined in a new example?",
            ("अन्नादि", "अ + आ → आ, as शुक्र + आदि → शुक्रादि."),
            [("अन्नदि", "अ + आ gives a long आ, not a short अ."),
             ("अन्नेदि", "ए comes from अ + इ, not from अ + आ."),
             ("अन्नैदि", "ऐ comes from अ + ए or ऐ, not from अ + आ.")],
            "अन्न + आदि = अन्नादि, like शुक्र + आदि = शुक्रादि.",
            "अ + आ → आ.",
            teaches="A final अ and an initial आ join as आ: शुक्र + आदि → शुक्रादि; वृष्य + आदीनि → वृष्यादीनि."),
    ],
}

# ---------------------------------------------------------------- unit 139
AUTHORED["139"] = {
    "title": "समः समाने स्थानस्थे",
    "question": "By the verse of unit 139, what makes the agni sama, viṣama, tīkṣṇa or manda?",
    "rule": ("Sama when Samāna (a wind) stands in its own place; viṣama when gone along a wrong path (विमार्गगे); tīkṣṇa when "
             "overcome by Pitta (पित्ताभिमूर्च्छिते); manda when this is afflicted by Kapha (कफपीडिते)."),
    "limits": ("One verse, two printed lines; the subject agni comes from unit 125. What goes the wrong path is not "
               "stated (the data reads Samāna), and what अस्मिन् refers to is open; no question rests on either. "
               "Printed अग्निं is possibly अग्निर्; not asked."),
    "explain_hi": ("यह श्लोक इकाई १२५ के चार अग्नियों का कारण बताता है। "
                   "सम: जब समान नामक वायु अपने स्थान में हो; विषम: जब (वह, सम्भवतः समान) गलत मार्ग में गया हो। "
                   "तीक्ष्ण: जब पित्त से आक्रान्त हो; मन्द: जब यह कफ से पीड़ित हो। "
                   "क्रम वही है जो इकाई १२५ में: सम, विषम, तीक्ष्ण, मन्द। "
                   "गलत मार्ग में कौन जाता है और ‘अस्मिन्’ किसके लिए है, यह छपा नहीं; इन पर कोई प्रश्न नहीं।"),
    "hook": "समान ठीक: सम; राह भटके: विषम; पित्त: तीक्ष्ण; कफ: मन्द।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 139, which doṣa is named in the condition for the manda (slow) agni?",
            ("Kapha", "मन्दोऽस्मिन्कफपीडिते: slow when afflicted by Kapha."),
            [("Pitta", "Being overcome by Pitta makes the agni tīkṣṇa (sharp)."),
             ("Rakta", "Rakta is not named in unit 139."),
             ("Vāta", "Vāta is not named for the manda agni; the verse names Kapha.")],
            "Kapha-afflicted: manda.",
            "मन्दः ... कफपीडिते."),
        match(1, "Match each state of agni to its cause in unit 139.",
              [["सम (even)", "Samāna in its own place"], ["विषम (uneven)", "gone along a wrong path"],
               ["तीक्ष्ण (sharp)", "overcome by Pitta"], ["मन्द (slow)", "afflicted by Kapha"]],
              "Sama: Samāna in place; viṣama: wrong path; tīkṣṇa: Pitta; manda: Kapha.",
              "सम, विषम, तीक्ष्ण, मन्द."),
        order(2, "Put the four states of agni in the order of the verse of unit 139.",
              ["समः समाने स्थानस्थे", "विषमोऽग्निंविमार्गगे", "पित्ताभिमूर्च्छिते तीक्ष्णो", "मंदोऽस्मिन्कफपीडिते"],
              "Sama, viṣama, tīkṣṇa, manda: the same order as the list of unit 125.",
              "समः → विषमः → तीक्ष्णः → मन्दः.", role="extend",
              teaches="The verse keeps the order of unit 125 (sama, viṣama, tīkṣṇa, manda) and gives each state its cause."),
        mcq("discriminate", 3, "Which split of पित्ताभिमूर्च्छिते in unit 139 is right?",
            ("पित्त + अभिमूर्च्छिते", "अ + अ → आ: पित्त + अभिमूर्च्छिते → पित्ताभिमूर्च्छिते."),
            [("पित्ते + अभिमूर्च्छिते", "ए + अ would print पित्तेऽभि-."),
             ("पित्तम् + अभिमूर्च्छिते", "म् would join the vowel: पित्तमभि-."),
             ("पित्ति + अभिमूर्च्छिते", "इ + अ would give य: पित्त्यभि-.")],
            "पित्त (Pitta) + अभिमूर्च्छिते (overcome).",
            "अ + अ → आ."),
        mcq("apply", 4, "Unit 128: the tīkṣṇa agni digests even improperly taken food quickly. By unit 139, which condition goes with it?",
            ("Overcome by Pitta", "पित्ताभिमूर्च्छिते तीक्ष्णः."),
            [("Afflicted by Kapha", "Kapha goes with manda, the slow one."),
             ("Samāna in its own place", "That goes with sama, the even one."),
             ("Gone along a wrong path", "A wrong path goes with viṣama, the uneven one.")],
            "Tīkṣṇa: overcome by Pitta.",
            "पित्ताभिमूर्च्छिते तीक्ष्णः."),
        mcq("transfer", 5, "कफपीडिते in unit 139 is a locative absolute (when afflicted by Kapha). What does गुरौ गते शिष्यः पठति mean?",
            ("When the teacher has gone, the pupil reads", "गुरौ गते: noun and participle in the locative = 'when ...'."),
            [("The pupil reads to the teacher who went", "गुरौ गते is not an object; it sets the time."),
             ("The teacher goes, and the pupil goes too", "शिष्यः पठति: the pupil reads, he does not go."),
             ("The pupil goes to the teacher to read", "गते is the teacher's going, in the locative.")],
            "गुरौ गते = when the teacher has gone, like कफपीडिते = when afflicted by Kapha.",
            "Locative noun + locative participle = 'when ...'.",
            teaches="A noun and a participle both in the locative give 'when ...': स्थानस्थे समाने, कफपीडिते."),
    ],
}

# ---------------------------------------------------------------- unit 140
AUTHORED["140"] = {
    "title": "शांतेऽग्नौ म्रियते",
    "question": "By the verse of unit 140, what follows when the agni is extinguished, well-ordered or abnormal?",
    "rule": ("Agni extinguished (शान्ते): one dies; well-ordered (युक्ते): one lives long, free from disease; abnormal (विकृते): one "
             "would be diseased. Therefore protect it with effort (प्रयत्नेन पालयेत्)."),
    "limits": ("One verse over two printed lines; the subject ('one') is not stated. It gives no method of protection. The close "
               "matches the advice at the end of unit 130 (there रक्षेत् and प्रयत्नतः, here पालयेत् and प्रयत्नेन)."),
    "explain_hi": ("यह श्लोक अग्नि का महत्त्व तीन अवस्थाओं से बताता है। "
                   "अग्नि शान्त (बुझ) जाए तो मनुष्य मरता है; ठीक (युक्त) रहे तो चिरकाल तक नीरोग जीता है; विकृत हो तो रोगी होता है। "
                   "इसलिए उसकी प्रयत्न से रक्षा करनी चाहिए। "
                   "यही सलाह इकाई १३० के अन्त में भी है (वहाँ ‘रक्षेत्’, यहाँ ‘पालयेत्’)। "
                   "रक्षा का उपाय यहाँ नहीं दिया गया।"),
    "hook": "अग्नि बुझी तो मृत्यु, ठीक तो दीर्घायु, बिगड़ी तो रोग।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 140, what follows when the agni is extinguished (śānta)?",
            ("One dies", "शान्तेऽग्नौ म्रियते: when the agni is extinguished, one dies."),
            [("One lives long", "Long life goes with the well-ordered (yukta) agni."),
             ("One falls ill", "Illness goes with the abnormal (vikṛta) agni."),
             ("One feels cold", "Cold is not named in unit 140.")],
            "Extinguished agni: death.",
            "शान्ते अग्नौ म्रियते."),
        order(1, "Put the printed parts of the verse of unit 140 in order.",
              ["शांतेऽग्नौ म्रियते", "युक्ते चिरं जीवत्यनामयः", "रोगीस्याद्विकृते", "तस्मात्तं प्रयत्नेन पालयेत्"],
              "Extinguished: dies; well-ordered: lives long, healthy; abnormal: diseased; so protect it with effort.",
              "शांतेऽग्नौ म्रियते → युक्ते चिरं जीवत्यनामयः → रोगीस्याद्विकृते → तस्मात्तं प्रयत्नेन पालयेत्."),
        match(2, "Match each word of unit 140 to its meaning.",
              [["शान्त", "extinguished"], ["युक्त", "well-ordered"], ["विकृत", "abnormal"], ["अनामय", "free from disease"],
               ["प्रयत्न", "effort"]],
              "शान्त extinguished, युक्त well-ordered, विकृत abnormal, अनामय free from disease, प्रयत्न effort.",
              "शान्त, युक्त, विकृत, अनामय, प्रयत्न.", role="extend",
              teaches="शान्ते, युक्ते, विकृते are locatives agreeing with अग्नौ: 'when the agni is ...'."),
        mcq("discriminate", 3, "Which split of शांतेऽग्नौ in unit 140 is right?",
            ("शान्ते + अग्नौ", "ए + अ: ए stays and the अ is marked ऽ."),
            [("शान्ता + अग्नौ", "आ + अ would give आ: शान्ताग्नौ."),
             ("शान्तः + अग्नौ", "अः + अ would give ओऽ: शान्तोऽग्नौ."),
             ("शान्तम् + अग्नौ", "म् would join the vowel: शान्तमग्नौ.")],
            "शान्ते (extinguished) + अग्नौ (when the agni): ए + अ → एऽ.",
            "ए + अ → एऽ."),
        mcq("apply", 4, "Units 130 and 140 both close with advice about the agni. What is it?",
            ("Protect it with effort", "तस्मात्तं प्रयत्नतो रक्षेत् (130); तस्मात्तं प्रयत्नेन पालयेत् (140)."),
            [("Feed it with outer fire", "No outer fire is advised; unit 130 only compares it."),
             ("Let Kapha settle on it", "Kapha makes it manda (unit 139); it is not advised."),
             ("Leave it alone to rest", "Both lines say to protect it with effort.")],
            "Both: therefore protect it with effort.",
            "तस्मात्तं प्रयत्नेन पालयेत्."),
        mcq("transfer", 5, "पालयेत् in unit 140 is an optative (one should protect). What does सत्यं वदेत् mean (a new example)?",
            ("One should speak the truth", "वदेत् is the optative of √वद्, like पालयेत्: 'should'."),
            [("One spoke the truth", "वदेत् is optative, not past."),
             ("One will speak the truth", "वदेत् is optative, not future."),
             ("One is speaking the truth", "वदेत् is optative, not present.")],
            "सत्यं वदेत् = one should speak the truth, like तं पालयेत् = one should protect it.",
            "Optative 3 sg. -एत् here: 'one should ...'.",
            teaches="पालयेत् is optative (gram: opt.): 'one should protect'; वदेत् is formed the same way."),
    ],
}

# ---------------------------------------------------------------- unit 141
AUTHORED["141"] = {
    "title": "इति सिराविभागो नामषष्ठोऽध्यायः",
    "question": "What does the closing line of unit 141 name the sixth chapter?",
    "rule": ("Thus the sixth chapter (षष्ठोऽध्यायः), named Sirāvibhāga, the division of the sirā (vessels). Printed नामषष्ठो = नाम "
             "षष्ठः, without a space."),
    "limits": "Prose closing line (colophon): it gives the chapter's name and number and teaches nothing else. No word for 'ends' is printed.",
    "explain_hi": ("यह छठे अध्याय की समाप्ति-पंक्ति (पुष्पिका) है: इस प्रकार सिराविभाग नाम का छठा अध्याय। "
                   "सिराविभाग = सिरा (वाहिनी) + विभाग (बँटवारा)। "
                   "अध्याय सिराओं से आरम्भ होकर धमनी, स्रोतस् और अग्नि तक गया। "
                   "छपाई में ‘नामषष्ठो’ बिना अन्तर के है = नाम षष्ठः। "
                   "सन्धि: सिराविभागः + नाम → सिराविभागो नाम; षष्ठः + अध्यायः → षष्ठोऽध्यायः।"),
    "hook": "छठा अध्याय: सिराओं का विभाग।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 141, what is the sixth chapter named?",
            ("सिराविभाग", "इति सिराविभागो नाम षष्ठोऽध्यायः."),
            [("अङ्गविभाग", "That is the name of chapter five."),
             ("मर्मविभाग", "That is the name of chapter seven."),
             ("गर्भव्यापत्", "That is the name of chapter four.")],
            "The sixth chapter is Sirāvibhāga, the division of the vessels.",
            "सिराविभाग = division of the sirās."),
        order(1, "Put the words of unit 141 (split out of sandhi) in their order.",
              ["इति", "सिराविभागः", "नाम", "षष्ठः", "अध्यायः"],
              "Thus, Sirāvibhāga, named, sixth, chapter.",
              "इति → सिराविभागः → नाम → षष्ठः → अध्यायः."),
        match(2, "Match each word of unit 141 to its meaning.",
              [["इति", "thus (closing)"], ["सिरा", "vessel"], ["विभाग", "division"], ["नाम", "named"],
               ["षष्ठ", "sixth"]],
              "Thus the sixth chapter, named division of the vessels.",
              "इति, सिरा, विभाग, नाम, षष्ठ.", role="extend",
              teaches="सिराविभाग = सिरा + विभाग: the division of the vessels, the theme with which the chapter began."),
        mcq("discriminate", 3, "Which split of षष्ठोऽध्यायः in unit 141 is right?",
            ("षष्ठः + अध्यायः", "अः + अ → ओ, and ऽ marks the lost अ."),
            [("षष्ठे + अध्यायः", "ए + अ would print षष्ठेऽध्यायः."),
             ("षष्ठा + अध्यायः", "आ + अ would give आ: षष्ठाध्यायः."),
             ("षष्ठम् + अध्यायः", "म् would join the vowel: षष्ठमध्यायः.")],
            "षष्ठः (sixth) + अध्यायः (chapter).",
            "अः + अ → ओऽ."),
        fill(4, "In unit 141 the word for 'sixth' is ____ (type it in Devanagari or in English letters, e.g. dharma).",
             accepts("षष्ठः", "ṣaṣṭhaḥ", "षष्ठ", "षष्ठो", "shashtha", "shashthah", "shashtho", "sashtha"),
             "षष्ठः = sixth; before अध्यायः it is printed षष्ठोऽध्यायः.",
             "षष्ठ = sixth (ordinal of षट्, six).",
             "षष्ठ = sixth.", role="apply"),
        mcq("transfer", 5, "By the pattern of षष्ठोऽध्यायः, what does सप्तमोऽध्यायः mean (a new example)?",
            ("The seventh chapter", "सप्तमः (seventh) + अध्यायः, joined like षष्ठः + अध्यायः."),
            [("Seven chapters", "सप्तम is the ordinal 'seventh', not the number 'seven'."),
             ("The sixth chapter", "Sixth is षष्ठ; सप्तम is seventh."),
             ("A chapter of seven parts", "Nothing about parts is said; सप्तम is 'seventh'.")],
            "सप्तमोऽध्यायः = the seventh chapter, like षष्ठोऽध्यायः = the sixth chapter.",
            "Ordinal + अध्यायः: अः + अ → ओऽ.",
            teaches="षष्ठ (sixth) and सप्तम (seventh) are ordinals; joined with अध्यायः they give षष्ठोऽध्यायः, सप्तमोऽध्यायः."),
    ],
}


# ===================================================================== NOTES_HI
NOTES_HI = {
    "129": ("गद्य (02.06.143); विश्वास मध्यम। पाठ-चिह्न: छपा ‘चिरात्पचति’ = चिरात् पचति (प से पहले त् नहीं बदलता; केवल अन्तर की कमी)। "
            "लम्बा समास सात मदों का द्वन्द्व + ‘आदि’ पढ़ा गया; ‘उदरगौरव’ = उदर का भारीपन (उदर रोग नहीं); उदर और गौरव दो मद भी हो सकते हैं, "
            "इस पर कोई प्रश्न नहीं। आम = कच्चा, न पचा पदार्थ (मानक)। छपे ं (मंद, विबंध, आंत्र, स्तंभ, लिंग) = न्/ङ्। सन्धि जाँची: मन्दः + तु → "
            "मन्दस्तु (त से पहले विसर्ग → स्); सम्यक् + अपि → सम्यगपि (स्वर से पहले क् → ग्); अपि + उपयुक्तम् → अप्युपयुक्तम् (इ + भिन्न स्वर → य्); "
            "उपयुक्तम् + उदर → उपयुक्तमुदर; गौरव + आध्मान → गौरवाध्मान (अ + आ → आ); आदीनि + आम → आदीन्याम।"),
    "130": ("गद्य (02.06.144); विश्वास मध्यम। पाठ-चिह्न (सम्भावित): छपा ‘किमुतांतराश्रयेणोष्ममना’; ‘ष्ममना’ कोई रूप नहीं; ‘ऊष्मणा’ (ताप से) "
            "डेटा का अनुमानित पाठ है (म का दोहराव); इस पर कोई प्रश्न नहीं। छपा ‘तस्मात्तं’ = तस्मात् तम् (त से पहले त् नहीं बदलता)। "
            "‘तम्’ = अग्नि (डेटा का पाठ)। ‘समेन’ ऊष्मन् से मेल खाता है। सन्धि जाँची: बाह्येन + अपि → बाह्येनापि (अ + अ → आ); "
            "ज्वाला + अङ्गार → ज्वालाङ्गार; आत्मकेन + अग्निना → आत्मकेनाग्निना; न + एक + आकारः → नैकाकारः (अ + ए → ऐ, अ + आ → आ); "
            "पाकः + भवति → पाको भवति (अः + घोष व्यंजन → ओ; छपा ‘पाकोभवति’ बिना अन्तर); प्रयत्नतः + रक्षेत् → प्रयत्नतो रक्षेत्।"),
    "131": ("गद्य (02.06.145); विश्वास निम्न: वाक्य अधूरा। ‘प्रवरेण सात्म्येन समम्’, ‘अवरेण इतरान्’ और दूसरा ‘प्रवरेण’ सब तृतीया हैं, पर "
            "किसके लिए (आहार-विहार का सात्म्य? बलवान-निर्बल अग्नियाँ?) यह नहीं कहा गया; कोई प्रश्न इन पर नहीं। ‘समम्’ = समान रूप से "
            "(या ‘साथ’)। दोषोपक्रमणीय सम्भवतः किसी अध्याय का नाम (जाँचा नहीं गया); ग्रहणी सम्भवतः पाचन का विकार। अन्त का ‘इति’ कथन बन्द करता है। "
            "सन्धि जाँची: अवरेण + इतरान् → अवरेणेतरान् (अ + इ → ए); परिपालयेत् + दोष → परिपालयेद्दोष (घोष से पहले त् → द्); दोष + उपक्रमणीय → "
            "दोषोपक्रमणीय (अ + उ → ओ); उपक्रमणीय + उक्तेन → उपक्रमणीयोक्तेन; विहितैः + च → विहितैश्च; च + औषध → चौषध (अ + औ → औ); "
            "योगैः + इति → योगैरिति (ऐः + स्वर → ऐर्)।"),
    "132": ("गद्य (02.06.146); विश्वास उच्च; कोई पाठ-चिह्न नहीं। श्लोक लाने का सूत्र; इकाई १३३ (छपी पंक्ति 147) से आगे के श्लोक इसके विषय "
            "दिखते हैं, कोई विराम नहीं माना गया। सन्धि जाँची: च + अत्र → चात्र (अ + अ → आ)।"),
    "133": ("श्लोक (02.06.147-148); विश्वास मध्यम। पाठ-चिह्न: छपा ‘स्वधातुसमवर्णांनि’ = स्वधातुसमवर्णानि (न से पहले अनुस्वार की छपाई)। "
            "पहली पंक्ति के विशेषणों का विशेष्य ‘स्रोतांसि’ दूसरी पंक्ति में (दोनों पंक्तियाँ इसी इकाई में)। ‘हैं’ क्रिया समझी जाती है। "
            "प्रतान = लता का तन्तु (सम्भावित); ‘फैलाव’ भी इसका अर्थ; इस पर कोई प्रश्न नहीं। सन्धि जाँची: वृत्तस्थूलानि + अणूनि → "
            "वृत्तस्थूलान्यणूनि (इ + अ → य); दीर्घाणि + आकृत्या → दीर्घाण्याकृत्या (इ + आ → या)।"),
    "134": ("श्लोक (02.06.149-150); विश्वास मध्यम; कोई पाठ-चिह्न नहीं। एक वाक्य दोनों पंक्तियों में। ‘यः’ पुंल्लिङ्ग एकवचन, दोनों संज्ञाओं "
            "के लिए (‘जो भी’)। विगुण = भिन्न गुण वाला (धातुभिः तृतीया के साथ); ‘दोषपूर्ण गुण वाला’ भी सम्भव। सन्धि जाँची: आहारः + च → आहारश्च "
            "(च से पहले विसर्ग → श्); स्यात् + दोष → स्याद्दोष (घोष से पहले त् → द्); धातुभिः + विगुणः → धातुभिर्विगुणः (इ के बाद विसर्ग + घोष → र्); "
            "विगुणः + यः → विगुणो यः (अः + घोष व्यंजन → ओ); यः + च → यश्च; सः + प्रदूषकः → स प्रदूषकः (सः का विसर्ग व्यंजन से पहले लुप्त)।"),
    "135": ("श्लोक (02.06.151-152); विश्वास निम्न, केवल क्षतिग्रस्त शब्द के कारण। पाठ-चिह्न (क्षतिग्रस्त): छपा ‘विमार्गप्तो’ कोई शब्द नहीं; "
            "सम्भवतः ‘विमार्गप्राप्तः’ (गलत मार्ग पर पहुँचा) या ‘विमार्गगमनम्’ का बिगड़ा रूप; अपठनीय मानकर बिना विभाजन छोड़ा गया, इस पर कोई प्रश्न नहीं। "
            "छपा ‘सिराणांग्रंथयोऽपि’ = सिराणां ग्रन्थयोऽपि (केवल अन्तर की कमी)। सिरा = सम्भवतः नसें। ‘संगो’ = सङ्गः (ं = ङ्)। सन्धि जाँची: "
            "सङ्गः + वा → सङ्गो वा (अः + घोष व्यंजन → ओ); ग्रन्थयः + अपि → ग्रन्थयोऽपि (अः + अ → ओऽ)।"),
    "136": ("श्लोक (02.06.153-154); विश्वास मध्यम; कोई पाठ-चिह्न नहीं। पहली पंक्ति के विशेषणों का विशेष्य ‘द्वाराणि’ दूसरी पंक्ति में। "
            "बिस = कमलनाल या उसकी जड़ के तन्तु (Nelumbo nucifera, मानक)। ‘बिसानामिव’ = कमलनालों के (तन्तुओं) जैसे। ‘हैं’ क्रिया समझी जाती है। "
            "उपचीयते = कर्मवाच्य वर्तमान। सन्धि जाँची: बिसानाम् + इव → बिसानामिव; दूरम् + विप्रसृतानि → दूरं विप्रसृतानि; रसः + यैः → रसो यैः "
            "(अः + घोष व्यंजन → ओ; छपा ‘रसोयैः’ बिना अन्तर); यैः + उपचीयते → यैरुपचीयते (ऐः + स्वर → ऐर्)।"),
    "137": ("श्लोक (02.06.155-156); विश्वास मध्यम। पाठ-चिह्न: छपा ‘मासात्प्रयातिशुक्रत्वमन्नं’ = मासात् प्रयाति शुक्रत्वम् अन्नम् (केवल अन्तर "
            "की कमी)। तीसरे मत (परे) की अवधि इस इकाई में नहीं कही गई; ‘मासात्’ उसका हो सकता है, निश्चित नहीं; इस पर कोई प्रश्न नहीं। "
            "अन्त का ‘इति’ मत को बन्द करता है, अनूदित नहीं। सन्धि जाँची: केचित् + आहुः → केचिदाहुः (स्वर से पहले त् → द्); आहुः + अहोरात्रात् → "
            "आहुरहोरात्रात् (उ के बाद विसर्ग + स्वर → र्); षट् + अह → षडह (ट् + स्वर → ड्); षडहात् + अपरे → षडहादपरे; पाकक्रमात् + इति → "
            "पाकक्रमादिति।"),
    "138": ("श्लोक (02.06.157-158); विश्वास निम्न। पाठ-चिह्न: छपे ‘प्रभावात्तु’ = प्रभावात् तु और ‘शुक्रादिकुर्वंते’ = शुक्रादि कुर्वन्ते (केवल अन्तर "
            "की कमी)। ‘वृष्यादीनि’ की संज्ञा (औषध या आहार) नहीं छपी। दूसरी पंक्ति में ‘करोति’ का कर्म नहीं कहा गया, जोड़ा नहीं गया; इस पंक्ति के "
            "अर्थ पर कोई प्रश्न नहीं। प्रभाव = विशेष शक्ति। सन्धि जाँची: वृष्य + आदीनि → वृष्यादीनि (अ + आ → आ); करोति + अहोरात्रात् → "
            "करोत्यहोरात्रात् (इ + अ → य); अहोरात्रात् + यत् → अहोरात्राद्यत् (घोष से पहले त् → द्); यत् + अन्यत् + अपि → यदन्यदपि।"),
    "139": ("श्लोक (02.06.159-160); विश्वास मध्यम। पाठ-चिह्न (सम्भावित): छपा ‘विषमोऽग्निंविमार्गगे’; ‘अग्निं’ सम्भवतः ‘अग्निर्’ (व से पहले र् की "
            "जगह ं) और अन्तर नहीं; इस पर कोई प्रश्न नहीं। छपा ‘मंदोऽस्मिन्कफपीडिते’ में केवल अन्तर की कमी। सम का विशेष्य अग्नि इकाई १२५ (छपी पंक्ति "
            "139) से। ‘विमार्गगे’ डेटा में समान से मेल खाता है, पर समान फिर नहीं छपा; ‘अस्मिन्’ (इसमें) किसके लिए (अग्नि या स्थान), नहीं कहा "
            "गया। समान = एक वायु। सन्धि जाँची: विषमः + अग्निः → विषमोऽग्निः (अः + अ → ओऽ); पित्त + अभिमूर्च्छिते → पित्ताभिमूर्च्छिते (अ + अ → आ); "
            "तीक्ष्णः + मन्दः → तीक्ष्णो मन्दः (अः + घोष व्यंजन → ओ); मन्दः + अस्मिन् → मन्दोऽस्मिन्।"),
    "140": ("श्लोक (02.06.161-162); विश्वास उच्च। पाठ-चिह्न: छपे ‘रोगीस्याद्विकृते’ = रोगी स्याद् विकृते और ‘तस्मात्तं’ = तस्मात् तम् (केवल "
            "अन्तर की कमी)। ‘म्रियते’ और ‘जीवति’ का कर्ता नहीं छपा (‘कोई’)। युक्ते, विकृते अग्नौ से मेल खाते हैं। ‘तम्’ = अग्नि। अन्त की "
            "सलाह इकाई १३० (छपी पंक्ति 144) जैसी है, पर शब्द थोड़े भिन्न (रक्षेत्/पालयेत्, प्रयत्नतः/प्रयत्नेन)। सन्धि जाँची: शान्ते + अग्नौ → "
            "शान्तेऽग्नौ (ए + अ → एऽ); जीवति + अनामयः → जीवत्यनामयः (इ + अ → य); स्यात् + विकृते → स्याद्विकृते (घोष से पहले त् → द्)।"),
    "141": ("पुष्पिका, गद्य (02.06.163); विश्वास उच्च। पाठ-चिह्न: छपा ‘नामषष्ठोऽध्यायः’ = नाम षष्ठोऽध्यायः (केवल अन्तर की कमी)। इनपुट में "
            "इसे श्लोक लिखा था, पर यह समाप्ति-पंक्ति है। ‘समाप्त’ शब्द छपा नहीं। सन्धि जाँची: सिराविभागः + नाम → सिराविभागो नाम (अः + घोष "
            "व्यंजन → ओ); षष्ठः + अध्यायः → षष्ठोऽध्यायः (अः + अ → ओऽ)।"),
}


# ===================================================================== AIDS
AIDS = {
    "129": {
        "diagram": {"groups": [
            {"label": "मन्द अग्नि: ठीक खाए अन्न पर भी, आम के लक्षण (छपे क्रम में)",
             "items": ["१ उदरगौरव: पेट का भारीपन", "२ आध्मान: पेट फूलना", "३ विबंध: मल रुकना", "४ आटोप: गड़गड़ाहट",
                       "५ आंत्रकूजन: आँतों की आवाज़", "६ मुखशोष: मुँह सूखना", "७ पायुस्तंभ: गुदा की जकड़न", "आदि → चिरात्पचति"]}]},
        "frame": "कौन: मन्द अग्नि (इकाई १२५ का चौथा भेद) → किस पर: सम्यक् उपयुक्त अन्न पर भी → पहले: आम के लक्षण दिखाकर → फिर: चिरात् पचति (देर से पचाती)।",
        "chunks": "मंदस्तु | सम्यगप्युपयुक्तम् | उदरगौरवाध्मानविबंधाटोपांत्रकूजनमुखशोषपायुस्तंभादीन्यामलिंगानि | दर्शयित्वा | चिरात्पचति",
        "sandhi": ("स्वर से पहले क् → ग्: सम्यक् + अपि → सम्यगपि · इ + भिन्न स्वर → य्: अपि + उपयुक्तम् → अप्युपयुक्तम् · "
                   "त से पहले विसर्ग → स्: मन्दः + तु → मन्दस्तु।"),
    },
    "130": {
        "seesaw": "बाह्य (बाहरी) अग्नि ⇄ अन्तराश्रय (भीतर आश्रित; ‘ताप’ अनुमानित पाठ): दोनों इसी पंक्ति में; बाहरी भी एक-सी नहीं, तो भीतर वाली का क्या कहना।",
        "frame": "छोटा उदाहरण: बाह्य अग्नि का पाक एक-सा नहीं → किमुत (तो क्या कहना) भीतर का ताप → निष्कर्ष: तस्मात्तं प्रयत्नतो रक्षेत्।",
        "chunks": "बाह्येनापि च | ज्वालांगारात्मकेनाग्निना | नैकाकारः सर्वदा पाकोभवति | किमुतांतराश्रयेणोष्ममना | समेनापि | तस्मात्तं प्रयत्नतो रक्षेत्",
        "sandhi": "अ + ए → ऐ: न + एकाकारः → नैकाकारः · अः + घोष व्यंजन → ओ: पाकः + भवति → पाको भवति · अ + अ → आ: बाह्येन + अपि → बाह्येनापि।",
    },
    "131": {
        "frame": ("पहले: अवर (निम्न) से अन्यों को क्रमशः साम्य तक → फिर: प्रवर (श्रेष्ठ) से रक्षा → साधन: वात आदि के साधन (दोषोपक्रमणीय में कहे) "
                  "और औषध-व्यायाम के योग (ग्रहणी रोग में बताए)।"),
        "seesaw": "प्रवर (श्रेष्ठ) ⇄ अवर (निम्न): दोनों इसी पंक्ति में; किसके लिए हैं, यह छपा नहीं।",
        "chunks": "तत्र प्रवरेण सात्म्येन समं | यथास्वमवरेणेतरान् | क्रमशः साम्यमापाद्य | प्रवरेण परिपालयेद्दोषोपक्रमणीयोक्तेन च | वातादिसाधनेन | ग्रहणीरोगविहितैश्चौषधव्यायामयोगैरिति",
        "sandhi": "अ + इ → ए: अवरेण + इतरान् → अवरेणेतरान् · अ + उ → ओ: दोष + उपक्रमणीय → दोषोपक्रमणीय · अ + औ → औ: च + औषध → चौषध।",
    },
    "132": {
        "frame": "सूत्र-वाक्य: भवति (है/हैं) + च (और) + अत्र (इस विषय में) → आगे संग्रह-श्लोक (इकाई १३३ से, ऐसा दिखता है)।",
        "sandhi": "अ + अ → आ: च + अत्र → चात्र।",
        "anchors": "‘भवति चात्र’ दिखे तो समझें: गद्य समाप्त, अब श्लोक। (मेरी याद-पद्धति)",
    },
    "133": {
        "diagram": {"groups": [
            {"label": "स्रोतांसि (छपे क्रम में)", "items": ["१ स्वधातुसमवर्ण: अपने धातु के रंग के", "२ वृत्त: गोल", "३ स्थूल: मोटे",
                                                     "४ अणु: बारीक", "५ दीर्घ आकृति: लम्बे", "६ प्रतानसदृश: लता-तन्तु जैसे (सम्भावित)"]}]},
        "seesaw": "स्थूल (मोटे) ⇄ अणु (बारीक): दोनों इसी श्लोक की पहली पंक्ति में।",
        "chunks": "स्वधातुसमवर्णांनि | वृत्तस्थूलान्यणूनि च | स्रोतांसि दीर्घाण्याकृत्या | प्रतानसदृशानि च",
        "sandhi": "इ + अ → य: वृत्तस्थूलानि + अणूनि → वृत्तस्थूलान्यणूनि · इ + आ → या: दीर्घाणि + आकृत्या → दीर्घाण्याकृत्या।",
    },
    "134": {
        "diagram": {"groups": [
            {"label": "स्रोतसां प्रदूषकः", "items": ["आहार और विहार", "दोषगुणैः समः: दोषों के गुणों के समान",
                                               "धातुभिर्विगुणः: धातुओं से भिन्न गुण", "→ स्रोतसों को दूषित करता"]}]},
        "contrast": "दोषों से: सम (समान) · धातुओं से: विगुण (भिन्न गुण)। दोनों शर्तें इसी श्लोक में।",
        "chunks": "आहारश्च विहारश्च | यः स्याद्दोषगुणैः समः | धातुभिर्विगुणो यश्च | स्रोतसां स प्रदूषकः",
        "sandhi": ("इ के बाद विसर्ग + घोष → र्: धातुभिः + विगुणः → धातुभिर्विगुणः · अः + घोष व्यंजन → ओ: विगुणः + यः → विगुणो यः · "
                   "च से पहले विसर्ग → श्: आहारः + च → आहारश्च।"),
    },
    "135": {
        "chain": {"steps": ["१ अतिप्रवृत्ति: अत्यधिक प्रवाह", "२ सङ्ग: रुकावट", "३ सिराओं की ग्रन्थियाँ: गाँठें",
                            "४ विमार्गप्तो वा गमनं: अस्पष्ट शब्द", "= स्रोतसां दुष्टिलक्षणम्"]},
        "chunks": "अतिप्रवृत्तिः | संगो वा | सिराणांग्रंथयोऽपि वा | विमार्गप्तो वा गमनं | स्रोतसां दुष्टिलक्षणं",
        "sandhi": "अः + घोष व्यंजन → ओ: सङ्गः + वा → सङ्गो वा · अः + अ → ओऽ: ग्रन्थयः + अपि → ग्रन्थयोऽपि।",
        "anchors": "तीन पक्के लक्षण: ‘बहुत बहना, रुकना, गाँठ’। (मेरी याद-पद्धति)",
    },
    "136": {
        "frame": "क्या: द्वाराणि स्रोतसाम् (स्रोतसों के द्वार) → कैसे: बिस जैसे सूक्ष्म, दूर तक फैले → कहाँ: देहे → काम: रसो यैरुपचीयते (इनसे रस बढ़ता)।",
        "chunks": "बिसानामिव सूक्ष्माणि | दूरं विप्रसृतानि च | द्वाराणि स्रोतसां देहे | रसोयैरुपचीयते",
        "sandhi": "अः + घोष व्यंजन → ओ: रसः + यैः → रसो यैः · ऐः + स्वर → ऐर्: यैः + उपचीयते → यैरुपचीयते · स्वर से पहले म्: बिसानाम् + इव → बिसानामिव।",
        "pegs": "मेरा बनाया चित्र: कमलनाल तोड़ें तो महीन तन्तु दूर तक खिंचते हैं; वैसे ही बारीक, फैले द्वार।",
    },
    "137": {
        "diagram": {"groups": [
            {"label": "अन्न → शुक्रत्व: कितने समय में? (पाकक्रमात्)",
             "items": ["केचित् (कुछ): अहोरात्र से", "अपरे (दूसरे): षडह से", "परे (अन्य): अवधि इस इकाई में स्पष्ट नहीं",
                       "छपा: मासात् (मास से), सम्भव है परे का हो"]}]},
        "chunks": "केचिदाहुरहोरात्रात् | षडहादपरे | परे | मासात्प्रयातिशुक्रत्वमन्नं | पाकक्रमादिति",
        "sandhi": "स्वर से पहले त् → द्: केचित् + आहुः → केचिदाहुः · उ के बाद विसर्ग + स्वर → र्: आहुः + अहोरात्रात् → आहुरहोरात्रात्।",
    },
    "138": {
        "contrast": "इसी श्लोक में: वृष्य आदि → सद्यः (तुरन्त), प्रभाव से · अन्य भेषज → प्रायः, अहोरात्रात् (अर्थ अनिश्चित)।",
        "chunks": "वृष्यादीनि | प्रभावात्तु | सद्यः | शुक्रादिकुर्वंते | प्रायः करोत्यहोरात्राद्यदन्यदपि भेषजं",
        "sandhi": "अ + आ → आ: वृष्य + आदीनि → वृष्यादीनि · त् + त → त्त: प्रभावात् + तु → प्रभावात्तु · इ + अ → य: करोति + अहोरात्रात् → करोत्यहोरात्रात्।",
    },
    "139": {
        "diagram": {"groups": [
            {"label": "अग्नि की चार अवस्थाएँ (इकाई १२५ का क्रम)",
             "items": ["सम: समान वायु अपने स्थान में", "विषम: गलत मार्ग में गया", "तीक्ष्ण: पित्त से आक्रान्त",
                       "मन्द: कफ से पीड़ित"]}]},
        "chunks": "समः समाने स्थानस्थे | विषमोऽग्निंविमार्गगे | पित्ताभिमूर्च्छिते तीक्ष्णो | मंदोऽस्मिन्कफपीडिते",
        "sandhi": "अः + अ → ओऽ: विषमः + अग्निः → विषमोऽग्निः; मन्दः + अस्मिन् → मन्दोऽस्मिन् · अ + अ → आ: पित्त + अभिमूर्च्छिते → पित्ताभिमूर्च्छिते।",
        "anchors": "क्रम याद रखें: ‘स-वि-ती-म’ (सम, विषम, तीक्ष्ण, मन्द)। (मेरी याद-पद्धति)",
    },
    "140": {
        "chain": {"steps": ["शान्ते अग्नौ: म्रियते (मृत्यु)", "युक्ते: चिरं जीवत्यनामयः (दीर्घ, नीरोग जीवन)",
                            "विकृते: रोगी स्यात् (रोग)", "तस्मात्तं प्रयत्नेन पालयेत् (रक्षा करे)"]},
        "chunks": "शांतेऽग्नौ म्रियते | युक्ते चिरं जीवत्यनामयः | रोगीस्याद्विकृते | तस्मात्तं प्रयत्नेन पालयेत्",
        "sandhi": "ए + अ → एऽ: शान्ते + अग्नौ → शान्तेऽग्नौ · इ + अ → य: जीवति + अनामयः → जीवत्यनामयः · घोष से पहले त् → द्: स्यात् + विकृते → स्याद्विकृते।",
        "frame": "अग्नि की तीन दशाएँ, तीन फल; फिर ‘तस्मात्’ से निष्कर्ष: रक्षा करे।",
    },
    "141": {
        "frame": "इति (इस प्रकार) → सिराविभागः (सिराओं का विभाग) → नाम → षष्ठः (छठा) → अध्यायः।",
        "sandhi": "अः + घोष व्यंजन → ओ: सिराविभागः + नाम → सिराविभागो नाम · अः + अ → ओऽ: षष्ठः + अध्यायः → षष्ठोऽध्यायः।",
        "anchors": "अध्याय ५ अङ्गविभाग, ६ सिराविभाग, ७ मर्मविभाग: तीन ‘विभाग’ एक के बाद एक। (मेरी याद-पद्धति)",
    },
}


# ============================================================== IMAGE_SPECS
IMAGE_SPECS = {
    ("129", "diagram"): {
        "file": "sh6-manda-ama-129.svg",
        "alt": ("Table of unit 129: the seven printed signs of āma that the manda agni shows, numbered in printed order, "
                "followed by 'and the like' and late digestion."),
        "type": "table",
        "title": "मन्द अग्नि: आम के लक्षण (इकाई १२९)",
        "heads": ["छपा शब्द", "अर्थ"],
        "rows": [["१ उदरगौरव", "पेट का भारीपन"], ["२ आध्मान", "पेट फूलना"], ["३ विबंध", "मल रुकना"],
                 ["४ आटोप", "गड़गड़ाहट"], ["५ आंत्रकूजन", "आँतों की आवाज़"], ["६ मुखशोष", "मुँह सूखना"],
                 ["७ पायुस्तंभ", "गुदा की जकड़न"], ["आदि → चिरात्पचति", "आदि; फिर देर से पाक"]],
    },
    ("133", "diagram"): {
        "file": "sh6-srotas-rupa-133.svg",
        "alt": ("Flowchart of unit 133: the srotas, with six numbered features in printed order: own-dhātu colour, round, "
                "thick, fine, long in form, like tendrils (probable)."),
        "type": "mermaid",
        "code": ("flowchart TD\n"
                 "  S[\"स्रोतांसि\"] --> A[\"१ अपने धातु के रंग के\"]\n"
                 "  A --> B[\"२ वृत्त: गोल\"]\n"
                 "  B --> C[\"३ स्थूल: मोटे\"]\n"
                 "  C --> D[\"४ अणु: बारीक\"]\n"
                 "  D --> E[\"५ दीर्घ: लम्बे\"]\n"
                 "  E --> F[\"६ प्रतान जैसे (सम्भावित)\"]\n"),
    },
    ("134", "diagram"): {
        "file": "sh6-pradushaka-134.svg",
        "alt": ("Flowchart of unit 134: food and conduct, with two conditions side by side (equal to the doṣas in qualities, "
                "unlike the dhātus in quality), lead to the defiler of the srotas."),
        "type": "mermaid",
        "code": ("flowchart TD\n"
                 "  A[\"आहार और विहार\"] --> C[\"दोषों के गुणों के समान\"]\n"
                 "  A --> D[\"धातुओं से भिन्न गुण\"]\n"
                 "  C --> E[\"स्रोतसों का प्रदूषक\"]\n"
                 "  D --> E\n"),
    },
    ("137", "diagram"): {
        "file": "sh6-paka-kala-137.svg",
        "alt": ("Table of unit 137: views on how long food takes to become śukra: some, a day and night; others, six days; "
                "still others, period not clear; a month is printed and may belong to them."),
        "type": "table",
        "title": "अन्न से शुक्रत्व: मत (इकाई १३७)",
        "heads": ["कौन", "कितने समय में"],
        "rows": [["केचित् (कुछ)", "अहोरात्र से"], ["अपरे (दूसरे)", "षडह (छह दिन) से"],
                 ["परे (अन्य)", "स्पष्ट नहीं"], ["छपा: मासात्", "मास से; परे का हो सकता है"]],
    },
    ("139", "diagram"): {
        "file": "sh6-agni-avastha-139.svg",
        "alt": ("Table of unit 139: the four states of agni and their causes: sama, Samāna in its own place; viṣama, gone "
                "along a wrong path; tīkṣṇa, overcome by Pitta; manda, afflicted by Kapha."),
        "type": "table",
        "title": "अग्नि की चार अवस्थाएँ (इकाई १३९)",
        "heads": ["अग्नि", "कब"],
        "rows": [["सम", "समान वायु अपने स्थान में"], ["विषम", "गलत मार्ग में गया"],
                 ["तीक्ष्ण", "पित्त से आक्रान्त"], ["मन्द", "कफ से पीड़ित"]],
    },
    ("140", "chain"): {
        "file": "sh6-agni-phala-140.svg",
        "alt": ("Flowchart of unit 140: agni extinguished leads to death, well-ordered to long disease-free life, abnormal "
                "to disease; therefore protect it with effort."),
        "type": "mermaid",
        "code": ("flowchart TD\n"
                 "  A[\"अग्नि\"] --> B[\"शान्त: मृत्यु\"]\n"
                 "  A --> C[\"युक्त: दीर्घ नीरोग जीवन\"]\n"
                 "  A --> D[\"विकृत: रोग\"]\n"
                 "  B --> E[\"इसलिए प्रयत्न से रक्षा\"]\n"
                 "  C --> E\n"
                 "  D --> E\n"),
    },
}
