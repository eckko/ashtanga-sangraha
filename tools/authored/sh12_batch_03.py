from helpers import mcq, match, order, fill, multi, accepts


def T(q, teaches):
    q["teaches"] = teaches
    return q


AUTHORED = {}

# ---------------------------------------------------------------- unit 27
AUTHORED["27"] = {
    "title": "यस्य शिरसि",
    "question": "By card 27, what two outcomes does the main clause name for the person 'on whose head' something is?",
    "rule": ("He on whose head (यस्य शिरसि) ... : he (सः) by a disease of the head (शिरोरोगेण) or (वा) by the cutting off "
             "of the head (शिरश्छेदनेन). What is on the head, and any verb, are not printed."),
    "limits": ("Prose; low confidence. What appears or grows on the head is missing in the print (perhaps a dropped word, as in "
               "cards 26 and 28); the data supplies nothing: no question asks what it is. No verb is printed in either clause."),
    "explain_hi": ("‘जिसके सिर पर …, वह सिर के रोग से अथवा सिर कटने से।’ "
                   "सिर पर क्या दिखता या उगता है, यह छपा नहीं; सम्भवतः एक शब्द छूट गया है, जैसे पड़ोसी कार्ड २६ और २८ में शरीर पर पौधे उगते हैं। "
                   "डेटा कुछ नहीं जोड़ता, इसलिए उस पर प्रश्न नहीं। "
                   "मुख्य वाक्य में दो फल ‘वा’ (अथवा) से जुड़े हैं: शिरोरोग और शिरश्छेदन। कोई क्रिया नहीं छपी। "
                   "सन्धि: शिरस् + रोगेण → शिरोरोगेण (अस् घोष व्यंजन से पहले → ओ), शिरः + छेदनेन → शिरश्छेदनेन (छ से पहले विसर्ग → श्)।"),
    "hook": "सिर पर (शब्द छपा नहीं) … तो सिर का रोग या सिर कटना।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "In card 27, what does शिरोरोगेण mean?",
            ("By a disease of the head", "शिरः (head) + रोगेण (by disease): by a disease of the head."),
            [("By a pain in the eyes", "Eyes would be नेत्र; शिरस् is the head."),
             ("By a wound in the chest", "Chest would be उरस्; शिरस् is the head."),
             ("By a fever in the whole body", "Fever would be ज्वर; रोग is disease, शिरस् the head.")],
            "शिरोरोगेण = by a disease of the head (instrumental).",
            "शिरस् = head, रोग = disease."),
        match(1, "Match each word of card 27 to its meaning.",
              [["यस्य", "of whom"], ["शिरसि", "on the head"], ["शिरोरोगेण", "by a disease of the head"],
               ["वा", "or"], ["शिरश्छेदनेन", "by the cutting off of the head"]],
              "यस्य = of whom, शिरसि = on the head, शिरोरोगेण = by a disease of the head, वा = or, शिरश्छेदनेन = by the cutting off of the head.",
              "यस्य, शिरसि, शिरोरोगेण, वा, शिरश्छेदनेन."),
        order(2, "Put the words of card 27 in the printed order.",
              ["यस्य", "शिरसि", "स", "शिरोरोगेण", "वा", "शिरश्छेदनेन"],
              "Of whom; on the head; he; by a disease of the head; or; by the cutting off of the head.",
              "यस्य → शिरसि → स → शिरोरोगेण → वा → शिरश्छेदनेन.",
              role="extend",
              teaches="यस्य (of whom) opens the relative clause; स (he) picks it up, and two instrumentals joined by वा name the outcome."),
        mcq("discriminate", 3, "Which split of शिरश्छेदनेन in card 27 is right?",
            ("शिरः + छेदनेन", "Visarga before छ → श्: शिरः + छेदनेन → शिरश्छेदनेन."),
            [("शिरा + छेदनेन", "शिरा + छेदनेन would print शिराछेदनेन or शिराच्छेदनेन, with no श्."),
             ("शिरः + अच्छेदनेन", "Before अ the visarga of शिरः gives ओऽ: शिरोऽच्छेदनेन."),
             ("शिरश्छे + दनेन", "शिरश्छे and दनेन are not words; छेदन (cutting) is one word.")],
            "शिरः (head) + छेदनेन (by cutting off): visarga before छ → श्.",
            "Visarga before च or छ → श्."),
        mcq("apply", 4, "By card 27, which two outcomes does वा ('or') join?",
            ("Head disease, or the head cut off", "शिरोरोगेण वा शिरश्छेदनेन: by a disease of the head or by the cutting off of the head."),
            [("Eye disease, or the eyes destroyed", "Eye disease and destruction of the eyes are cards 31 and 32, not card 27."),
             ("Fever, or a wasting of the body", "Card 27 names no fever and no wasting; both its outcomes concern the head."),
             ("Skin disease, or a fit of epilepsy", "Skin disease (कुष्ठ) is card 28 and epilepsy (अपस्मार) card 30.")],
            "Both outcomes in card 27 concern the head: शिरोरोग and शिरश्छेदन.",
            "वा joins शिरोरोगेण and शिरश्छेदनेन."),
        mcq("transfer", 5, "By the pattern of शिरः + छेदनेन → शिरश्छेदनेन, how is वृक्षः + छिद्यते (the tree is cut) joined in a new example?",
            ("वृक्षश्छिद्यते", "Visarga before छ → श्: वृक्षः + छिद्यते → वृक्षश्छिद्यते."),
            [("वृक्षो छिद्यते", "ओ comes from अः before a voiced consonant; छ is not voiced."),
             ("वृक्षस्छिद्यते", "स् comes from a visarga before त or थ (optionally before स), not before छ."),
             ("वृक्षर्छिद्यते", "र् comes from a visarga after a vowel other than अ/आ before a voiced sound.")],
            "वृक्षः + छिद्यते = वृक्षश्छिद्यते, like शिरः + छेदनेन = शिरश्छेदनेन.",
            "Visarga before च or छ → श्.",
            teaches="A visarga before च or छ becomes श्: शिरः + छेदनेन → शिरश्छेदनेन."),
    ],
}

# ---------------------------------------------------------------- unit 28
AUTHORED["28"] = {
    "title": "जायंते पद्मान्युरसि",
    "question": "By card 28, in what state is the person, what grows on his chest, and which disease is named?",
    "rule": ("He of whom, naked (नग्नस्य), sprinkled with ghee (आज्यावसिक्तस्य), offering into a flameless fire (अग्निम् अनर्चिषम् "
             "जुह्वतः), lotuses grow on the chest (पद्मानि उरसि): he by kuṣṭha (skin disease, leprosy group; standard)."),
    "limits": ("Prose; medium confidence. The verb of स कुष्ठेन is understood, not printed. The first long token is printed without "
               "spaces (a print slip). The card names the disease only: no course, time or treatment."),
    "explain_hi": ("जिसके नंगे, घी से सींचे हुए, ज्वाला-रहित अग्नि में आहुति देते हुए, छाती पर कमल उगते हैं, वह कुष्ठ से। "
                   "कुष्ठ = त्वचा के दीर्घ रोगों का समूह, जिसमें कोढ़ भी है (डेटा: standard)। "
                   "‘यस्य नग्नस्य … जुह्वतः’ षष्ठी रूपों की एक माला है जो उसी व्यक्ति का वर्णन करती है। "
                   "‘स कुष्ठेन’ की क्रिया छपी नहीं, समझी जाती है। "
                   "सन्धि: पद्मानि + उरसि → पद्मान्युरसि (इ + उ → यु), जुह्वतः + जायन्ते → जुह्वतो जायन्ते (अः घोष व्यंजन से पहले → ओ)।"),
    "hook": "नग्न, घी से सिक्त, बिना लौ की आग में आहुति, छाती पर कमल: कुष्ठ।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By card 28, what grows on the person's chest?",
            ("Lotuses", "पद्मानि उरसि जायन्ते: lotuses grow on the chest."),
            [("Mushrooms", "No mushrooms are named; पद्म is the lotus."),
             ("Feathers", "No feathers are named; पद्म is the lotus."),
             ("Grasses", "No grass grows on the chest in card 28; पद्म is the lotus.")],
            "पद्मानि = lotuses; उरसि = on the chest.",
            "पद्म = lotus."),
        order(1, "Put these parts of card 28 in the printed order.",
              ["नग्नस्य", "आज्यावसिक्तस्य", "अग्निमनर्चिषं", "जुह्वतो", "पद्मान्युरसि", "स कुष्ठेन"],
              "Naked; sprinkled with ghee; a flameless fire; offering; lotuses on the chest; he by kuṣṭha.",
              "नग्नस्य → आज्यावसिक्तस्य → अग्निमनर्चिषं → जुह्वतो → पद्मान्युरसि → स कुष्ठेन."),
        match(2, "Match each word of card 28 to its meaning.",
              [["नग्न", "naked"], ["आज्य", "ghee"], ["अनर्चिषम्", "flameless"], ["जुह्वतः", "offering an oblation"],
               ["उरसि", "on the chest"], ["पद्मानि", "lotuses"]],
              "नग्न = naked, आज्य = ghee, अनर्चिषम् = flameless, जुह्वतः = offering, उरसि = on the chest, पद्मानि = lotuses.",
              "नग्न, आज्य, अनर्चिषम्, जुह्वतः, उरसि, पद्मानि.",
              role="extend",
              teaches="A row of genitives (नग्नस्य, आज्यावसिक्तस्य, जुह्वतः) all describe the one person of यस्य."),
        mcq("discriminate", 3, "Which split of पद्मान्युरसि in card 28 is right?",
            ("पद्मानि + उरसि", "इ before the unlike vowel उ → य्: पद्मानि + उरसि → पद्मान्युरसि."),
            [("पद्मान् + युरसि", "युरसि is not a word; the य् comes from the इ of पद्मानि."),
             ("पद्माना + उरसि", "आ + उ gives ओ: that would print पद्मानोरसि."),
             ("पद्मे + उरसि", "ए before उ does not give यु; पद्मे is also not the plural.")],
            "पद्मानि (lotuses) + उरसि (on the chest): इ + उ → यु.",
            "इ + unlike vowel → य् + that vowel."),
        mcq("apply", 4, "A person is naked, sprinkled with ghee, offering into a flameless fire, and lotuses grow on his chest. Which disease does card 28 name?",
            ("कुष्ठ", "स कुष्ठेन: he by kuṣṭha, a skin disease (leprosy group; standard)."),
            [("प्रमेह", "प्रमेह follows drinking sneha with caṇḍālas (card 29)."),
             ("उन्माद", "उन्माद follows sinking in water while dancing with demons (card 29)."),
             ("अपस्मार", "अपस्मार is named for the one who is matta (card 30).")],
            "Lotuses on the chest → कुष्ठ.",
            "पद्मानि उरसि → स कुष्ठेन."),
        mcq("transfer", 5, "By the pattern of पद्मानि + उरसि → पद्मान्युरसि, how is फलानि + उद्याने (fruits in the garden) joined in a new example?",
            ("फलान्युद्याने", "इ before the unlike vowel उ → य्: फलानि + उद्याने → फलान्युद्याने."),
            [("फलानीद्याने", "इ + उ does not merge into ई; the इ becomes य्."),
             ("फलानेद्याने", "ए comes from अ + इ, not from इ + उ."),
             ("फलानियुद्याने", "The इ is replaced by य्; it does not stay beside it.")],
            "फलानि + उद्याने = फलान्युद्याने, like पद्मानि + उरसि = पद्मान्युरसि.",
            "इ + unlike vowel → य् + that vowel.",
            teaches="A final इ before an unlike vowel becomes य्: पद्मानि + उरसि → पद्मान्युरसि."),
    ],
}

# ---------------------------------------------------------------- unit 29
AUTHORED["29"] = {
    "title": "यश्चंडालैः सह स्नेहं पिबति",
    "question": "By card 29, which two scenes are linked to prameha and to unmāda?",
    "rule": ("Who drinks sneha (oil or fat) with caṇḍālas (चण्डालैः सह): he by prameha (urinary disorder, probably diabetes-type). "
             "Who, dancing with demons (रक्षोभिः सह), sinks in the waters (अप्सु मज्जति): he by unmāda (insanity)."),
    "limits": ("Prose; two printed lines joined. The verbs of स प्रमेहेण and स उन्मादेन are understood, not printed. "
               "prameha as diabetes-type is only probable (data's label)."),
    "explain_hi": ("पहली पंक्ति: जो चाण्डालों के साथ स्नेह (तेल या वसा) पीता है, वह प्रमेह से; प्रमेह मूत्र-सम्बन्धी रोगों का समूह है, सम्भवतः मधुमेह जैसा (डेटा: probable)। "
                   "दूसरी पंक्ति: जो राक्षसों के साथ नाचता हुआ जल में डूबता है, वह उन्माद (पागलपन) से। "
                   "दोनों में ‘सह’ (साथ) तृतीया के साथ आता है: चण्डालैः सह, रक्षोभिः सह। "
                   "‘स प्रमेहेण’ और ‘स उन्मादेन’ की क्रिया छपी नहीं। "
                   "सन्धि: यः + चण्डालैः → यश्चण्डालैः, नृत्यन् + अप्सु → नृत्यन्नप्सु (ह्रस्व स्वर के बाद न् स्वर से पहले दुगना)।"),
    "hook": "चाण्डालों संग स्नेह: प्रमेह; राक्षसों संग नाचकर डूबना: उन्माद।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By card 29, with whom does the person drink sneha?",
            ("With caṇḍālas", "चण्डालैः सह स्नेहं पिबति: he drinks sneha with caṇḍālas."),
            [("With physicians", "No physicians are named; the companions are caṇḍālas."),
             ("With his teacher", "No teacher is named; the companions are caṇḍālas."),
             ("With the kings", "No kings appear in card 29; the companions are caṇḍālas.")],
            "चण्डालैः सह = with caṇḍālas.",
            "सह + instrumental = with."),
        match(1, "Match each word of card 29 to its meaning.",
              [["स्नेहम्", "oil or fat"], ["पिबति", "drinks"], ["रक्षोभिः", "with demons"], ["नृत्यन्", "dancing"],
               ["अप्सु", "in the waters"], ["मज्जति", "sinks"]],
              "स्नेहम् = oil or fat, पिबति = drinks, रक्षोभिः = with demons, नृत्यन् = dancing, अप्सु = in the waters, मज्जति = sinks.",
              "स्नेहम्, पिबति, रक्षोभिः, नृत्यन्, अप्सु, मज्जति."),
        order(2, "Put the words of card 29, line 2, in the printed order.",
              ["यो", "रक्षोभिः", "सह", "नृत्यन्नप्सु", "मज्जति", "स उन्मादेन"],
              "Who; demons; with; dancing, in the waters; sinks; he by unmāda.",
              "यो → रक्षोभिः → सह → नृत्यन्नप्सु → मज्जति → स उन्मादेन.",
              role="extend",
              teaches="सह (with) takes the instrumental: रक्षोभिः सह, like चण्डालैः सह in line 1."),
        mcq("discriminate", 3, "By card 29, which disease follows sinking in the waters while dancing with demons?",
            ("उन्माद (insanity)", "रक्षोभिः सह नृत्यन्नप्सु मज्जति स उन्मादेन: he by unmāda."),
            [("प्रमेह (urinary disorder)", "प्रमेह is for drinking sneha with caṇḍālas, line 1."),
             ("कुष्ठ (skin disease)", "कुष्ठ is for lotuses on the chest, card 28."),
             ("अपस्मार (epilepsy)", "अपस्मार is for the one who is matta, card 30.")],
            "Line 2: dancing with demons, sinking in water → उन्माद.",
            "रक्षोभिः सह नृत्यन् मज्जति → उन्माद."),
        mcq("apply", 4, "Why is नृत्यन् printed नृत्यन्न- before अप्सु in card 29?",
            ("After a short vowel, न् doubles before a vowel", "नृत्यन् ends in न् after short अ, and अप्सु begins with a vowel: न् → न्न्."),
            [("Every final न् doubles before any following vowel", "Not every: only after a short vowel; after a long vowel it stays single."),
             ("The stem of the participle ends in न्न्", "The stem is नृत्यत्; its nominative is नृत्यन्; the second न् is sandhi."),
             ("अप्सु begins with न् in the full form", "अप्सु (in the waters) begins with अ; the extra न् comes from sandhi.")],
            "नृत्यन् + अप्सु → नृत्यन्नप्सु.",
            "Short vowel + final न् + vowel → न्न्."),
        mcq("transfer", 5, "By the pattern of नृत्यन् + अप्सु → नृत्यन्नप्सु, how is पठन् + आस्ते (sits reading) joined in a new example?",
            ("पठन्नास्ते", "न् after the short अ of पठन्, before the vowel आ, doubles: पठन्नास्ते."),
            [("पठनास्ते", "After a short vowel the final न् must double before a vowel."),
             ("पठन्तास्ते", "No त् appears; only the न् doubles."),
             ("पठमास्ते", "न् does not turn into म् before a vowel.")],
            "पठन् + आस्ते = पठन्नास्ते, like नृत्यन् + अप्सु = नृत्यन्नप्सु.",
            "Short vowel + final न् + vowel → न्न्.",
            teaches="A final न् after a short vowel doubles before a vowel: नृत्यन् + अप्सु → नृत्यन्नप्सु."),
    ],
}

# ---------------------------------------------------------------- unit 30
AUTHORED["30"] = {
    "title": "सोऽपस्मारेण",
    "question": "By card 30, which disease is named for the one who is matta?",
    "rule": "He who is matta (intoxicated or frenzied; यो मत्तः): he by apasmāra (epilepsy; standard), सोऽपस्मारेण.",
    "limits": ("Prose; medium confidence. Printed मत्त: has a colon for the visarga (print habit). मत्त can be intoxicated or "
               "frenzied: no question picks one. No verb is printed."),
    "explain_hi": ("जो मत्त है, वह अपस्मार (मिर्गी; डेटा: standard) से। "
                   "‘मत्त’ का अर्थ नशे में या उन्मत्त दोनों हो सकता है; डेटा दोनों रखता है। "
                   "छपाई में ‘मत्त:’ में विसर्ग की जगह कोलन है, यह छपाई की आदत है। "
                   "सन्धि: सः + अपस्मारेण → सोऽपस्मारेण (अः + अ → ओ, और अगला अ लुप्त, जिसे ऽ दिखाता है); यः + मत्तः → यो मत्तः (अः घोष व्यंजन से पहले → ओ)।"),
    "hook": "मत्त हो तो अपस्मार।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "In card 30, what does अपस्मार name?",
            ("Epilepsy", "अपस्मार = epilepsy (standard)."),
            [("Insanity", "Insanity is उन्माद (card 29), a different word."),
             ("Fever", "Fever is ज्वर; अपस्मार is epilepsy."),
             ("Leprosy", "The leprosy group is कुष्ठ (card 28); अपस्मार is epilepsy.")],
            "अपस्मार = epilepsy.",
            "अपस्मार = epilepsy."),
        match(1, "Match each word of card 30 to its meaning.",
              [["यः", "who"], ["मत्तः", "intoxicated or frenzied"], ["सः", "he"], ["अपस्मारेण", "by epilepsy"]],
              "यः = who, मत्तः = intoxicated or frenzied, सः = he, अपस्मारेण = by epilepsy.",
              "यः, मत्तः, सः, अपस्मारेण."),
        fill(2, "The word for 'epilepsy' in card 30 is ____ (type it in Devanagari or in English letters, e.g. dharma).",
             accepts("अपस्मार", "apasmāra", "अपस्मारेण", "apasmara"),
             "अपस्मार = epilepsy; card 30 has it in the instrumental, अपस्मारेण.",
             "अपस्मार names epilepsy (standard); the instrumental अपस्मारेण says 'by epilepsy'.",
             "अपस्मार = epilepsy."),
        mcq("discriminate", 3, "Which split of सोऽपस्मारेण in card 30 is right?",
            ("सः + अपस्मारेण", "अः + अ → ओ, and the अ is elided (ऽ): सः + अपस्मारेण → सोऽपस्मारेण."),
            [("सो + अपस्मारेण", "सो is not a word; the ओ comes from the visarga of सः."),
             ("सः + पस्मारेण", "पस्मार is not a word; the ऽ marks an elided अ."),
             ("सा + अपस्मारेण", "सा + अ gives आ: that would print सापस्मारेण.")],
            "सः (he) + अपस्मारेण (by epilepsy): अः + अ → ओऽ.",
            "अः + अ → ओ + ऽ (अ elided)."),
        mcq("apply", 4, "Which English rendering of card 30 is right?",
            ("He who is intoxicated or frenzied, he by epilepsy", "यो मत्तः सोऽपस्मारेण: he who is intoxicated or frenzied, he by apasmāra."),
            [("He who is intoxicated or frenzied, he by a fever", "अपस्मार is epilepsy, not fever."),
             ("She who is intoxicated or frenzied, she by epilepsy", "यः and सः are masculine: he, not she."),
             ("He who is fast asleep and calm, he by epilepsy", "मत्त is intoxicated or frenzied, not asleep.")],
            "यः मत्तः = he who is intoxicated or frenzied; सः अपस्मारेण = he by epilepsy.",
            "मत्त = intoxicated/frenzied; अपस्मार = epilepsy."),
        mcq("transfer", 5, "By the pattern of सः + अपस्मारेण → सोऽपस्मारेण, how is मेषः + अत्र (the ram here) joined in a new example?",
            ("मेषोऽत्र", "अः + अ → ओ, and the अ is elided (ऽ): मेषोऽत्र."),
            [("मेष अत्र", "The gap form is for अः before vowels other than अ; before अ it gives ओऽ."),
             ("मेषरत्र", "र् comes from a visarga after a vowel other than अ/आ."),
             ("मेषात्र", "अः + अ does not merge into आ; it gives ओऽ.")],
            "मेषः + अत्र = मेषोऽत्र, like सः + अपस्मारेण = सोऽपस्मारेण.",
            "अः + अ → ओ + ऽ.",
            teaches="अः before अ becomes ओ and the अ is elided (ऽ): सः + अपस्मारेण → सोऽपस्मारेण."),
    ],
}

# ---------------------------------------------------------------- unit 31
AUTHORED["31"] = {
    "title": "यश्चंद्रसूर्ययोरुपरागं पश्यति",
    "question": "By card 31, what does seeing an eclipse of the moon and the sun bring?",
    "rule": ("He who sees (पश्यति) an eclipse (उपरागम्) of the moon and the sun (चन्द्रसूर्ययोः): in him a disease of the eyes "
             "(नेत्ररोगः) arises (उपजायते)."),
    "limits": "Prose; high confidence. It names a disease of the eyes in general: no particular eye disease, no time.",
    "explain_hi": ("जो चन्द्रमा और सूर्य का ग्रहण (उपराग) देखता है, उसे आँख का रोग उत्पन्न होता है। "
                   "‘चन्द्रसूर्ययोः’ द्वन्द्व समास का षष्ठी द्विवचन है: चन्द्रमा और सूर्य का। "
                   "‘नेत्ररोग’ सामान्य नाम है; कौन-सा रोग, यह नहीं कहा। "
                   "सन्धि: सूर्ययोः + उपरागम् → सूर्ययोरुपरागम् (ओ के बाद विसर्ग घोष वर्ण से पहले → र्); "
                   "नेत्ररोगः + उपजायते → नेत्ररोग उपजायते (अः, अ से भिन्न स्वर से पहले → अ, बीच में अन्तर)।"),
    "hook": "ग्रहण देखा तो नेत्ररोग।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "In card 31, what does उपराग mean?",
            ("Eclipse", "उपराग = eclipse: चन्द्रसूर्ययोरुपरागम्, an eclipse of the moon and the sun."),
            [("Sunrise", "Sunrise would be सूर्योदय; उपराग is an eclipse."),
             ("Rainbow", "Rainbow would be इन्द्रधनुस्; उपराग is an eclipse."),
             ("Moonlight", "Moonlight would be ज्योत्स्ना; उपराग is an eclipse.")],
            "उपराग = eclipse.",
            "उपराग = eclipse."),
        order(1, "Put the parts of card 31 in the printed order.",
              ["यः", "चंद्रसूर्ययोः", "उपरागं", "पश्यति", "तस्य", "नेत्ररोग उपजायते"],
              "Who; of the moon and the sun; an eclipse; sees; in him; a disease of the eyes arises.",
              "यः → चंद्रसूर्ययोः → उपरागं → पश्यति → तस्य → नेत्ररोग उपजायते."),
        match(2, "Match each word of card 31 to its meaning.",
              [["चन्द्रसूर्ययोः", "of the moon and the sun"], ["उपरागम्", "eclipse"], ["पश्यति", "sees"],
               ["नेत्ररोगः", "disease of the eyes"], ["उपजायते", "arises"]],
              "चन्द्रसूर्ययोः = of the moon and the sun, उपरागम् = eclipse, पश्यति = sees, नेत्ररोगः = eye disease, उपजायते = arises.",
              "चन्द्रसूर्ययोः, उपरागम्, पश्यति, नेत्ररोगः, उपजायते.",
              role="extend",
              teaches="चन्द्रसूर्ययोः is a dvandva (moon and sun) in the genitive dual: of the moon and the sun."),
        mcq("discriminate", 3, "Which split of सूर्ययोरुपरागं in card 31 is right?",
            ("सूर्ययोः + उपरागम्", "Visarga after ओ before a voiced sound (उ) → र्: सूर्ययोरुपरागम्."),
            [("सूर्ययोः + अपरागम्", "With अपरागम् it would print सूर्ययोरपरागं, with रप."),
             ("सूर्यया + उपरागम्", "आ + उ gives ओ: that would print सूर्ययोपरागं, with no र्."),
             ("सूर्ययो + रुपरागम्", "रुपराग is not a word; the र् comes from the visarga.")],
            "सूर्ययोः (of the sun, in the dvandva) + उपरागम् (eclipse).",
            "ओः + voiced sound → ओर्."),
        mcq("apply", 4, "Why does नेत्ररोगः lose its visarga before उपजायते in card 31 and stay unjoined?",
            ("अः before a vowel other than अ → अ, with a gap", "The visarga after अ drops before उ, and no further join is made."),
            [("अः before every vowel → अ, with a gap", "Not before अ: there अः + अ → ओऽ (सोऽपस्मारेण, card 30)."),
             ("अः before the vowel उ → ओ, with no gap", "ओ comes from अः before a voiced consonant (or before अ, as ओऽ), not before उ."),
             ("अः before the vowel उ → अर्, joined to it as one", "र् comes from a visarga after a vowel other than अ/आ.")],
            "नेत्ररोगः + उपजायते → नेत्ररोग उपजायते.",
            "अः + vowel other than अ → अ (gap)."),
        mcq("transfer", 5, "By the pattern of नेत्ररोगः + उपजायते → नेत्ररोग उपजायते, how is बालः + इच्छति (the boy wishes) written in a new example?",
            ("बाल इच्छति", "अः before a vowel other than अ → अ, with a gap: बाल इच्छति."),
            [("बालो इच्छति", "ओ comes from अः before a voiced consonant (or before अ, as ओऽ), not before इ."),
             ("बालरिच्छति", "र् comes from a visarga after a vowel other than अ/आ."),
             ("बालेच्छति", "Once the visarga drops, the vowels are not joined again.")],
            "बालः + इच्छति = बाल इच्छति, like नेत्ररोगः + उपजायते = नेत्ररोग उपजायते.",
            "अः + vowel other than अ → अ (gap).",
            teaches="अः before a vowel other than अ becomes अ and the words stay apart: नेत्ररोग उपजायते."),
    ],
}

# ---------------------------------------------------------------- unit 32
AUTHORED["32"] = {
    "title": "यस्तयोः पतनं",
    "question": "By card 32, what follows the falling of 'those two'?",
    "rule": ("He who (sees) the falling (पतनम्) of those two (तयोः; by the data the moon and the sun): for him destruction of "
             "the eyes (नेत्रविनाशः)."),
    "limits": ("Prose; medium confidence. The verb 'sees' is carried from card 31, not printed. Printed तस्यनेत्रविनाशः lacks a "
               "space (a print slip). The card says nothing of what kind of destruction or when."),
    "explain_hi": ("जो उन दोनों का गिरना (देखता है), उसके लिए आँखों का नाश। "
                   "डेटा के अनुसार ‘वे दोनों’ चन्द्रमा और सूर्य हैं; ‘देखता है’ क्रिया कार्ड ३१ से आती है, यहाँ छपी नहीं। "
                   "कार्ड ३१ में ग्रहण देखने पर नेत्ररोग, यहाँ गिरना देखने पर नेत्र-विनाश। "
                   "सन्धि: यः + तयोः → यस्तयोः (त से पहले विसर्ग → स्)। ‘तस्यनेत्रविनाशः’ में रिक्त स्थान छूटा है।"),
    "hook": "चन्द्र-सूर्य का गिरना: नेत्र-विनाश।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "In card 32, what does पतनम् mean?",
            ("Falling", "पतनम् = falling (from √पत्, to fall)."),
            [("Rising", "Rising would be उदय; पतन is falling."),
             ("Shining", "Shining would be दीप्ति; पतन is falling."),
             ("Hiding", "Hiding would be गोपन; पतन is falling.")],
            "पतनम् = falling.",
            "पतन = falling."),
        match(1, "Match each word of card 32 to its meaning.",
              [["तयोः", "of those two"], ["पतनम्", "falling"], ["तस्य", "for him"], ["नेत्र", "eye"], ["विनाशः", "destruction"]],
              "तयोः = of those two, पतनम् = falling, तस्य = for him, नेत्र = eye, विनाशः = destruction.",
              "तयोः, पतनम्, तस्य, नेत्र, विनाशः."),
        mcq("extend", 2, "By card 32, what follows seeing the moon and the sun fall?",
            ("Destruction of the eyes", "तस्य नेत्रविनाशः: for him destruction of the eyes."),
            [("A disease of the eyes", "A disease of the eyes is for seeing their eclipse (card 31)."),
             ("A disease of the head", "Disease of the head is named in card 27, not here."),
             ("A fit of insanity", "Insanity (उन्माद) is named in card 29, not here.")],
            "Eclipse → disease of the eyes (card 31); falling → destruction of the eyes (card 32).",
            "पतनम् → नेत्रविनाशः.",
            teaches="Card 32 goes a step beyond card 31: eclipse gives eye disease (नेत्ररोग), falling gives eye destruction (नेत्रविनाश)."),
        mcq("discriminate", 3, "Which split of यस्तयोः in card 32 is right?",
            ("यः + तयोः", "Visarga before त → स्: यः + तयोः → यस्तयोः."),
            [("यः + स्तयोः", "स्तयोः is not a word; the स् comes from the visarga."),
             ("यः + अस्तयोः", "Before अ the visarga gives ओऽ: योऽस्तयोः."),
             ("या + तयोः", "या + तयोः would print या तयोः, with no स्.")],
            "यः (who) + तयोः (of those two): visarga before त → स्.",
            "Visarga before त or थ → स्."),
        order(4, "Put the words of card 32 in the printed order.",
              ["यः", "तयोः", "पतनं", "तस्य", "नेत्रविनाशः"],
              "Who; of those two (by the data the moon and the sun); the falling; for him; destruction of the eyes.",
              "यः → तयोः → पतनं → तस्य → नेत्रविनाशः.",
              role="apply"),
        mcq("transfer", 5, "By the pattern of यः + तयोः → यस्तयोः, how is सिंहः + तत्र (the lion there) joined in a new example?",
            ("सिंहस्तत्र", "Visarga before त → स्: सिंहः + तत्र → सिंहस्तत्र."),
            [("सिंहो तत्र", "ओ comes from अः before a voiced consonant; त is not voiced."),
             ("सिंहर्तत्र", "र् comes from a visarga after a vowel other than अ/आ before a voiced sound."),
             ("सिंहश्तत्र", "श् comes from a visarga before च or छ (optionally before श), not before त.")],
            "सिंहः + तत्र = सिंहस्तत्र, like यः + तयोः = यस्तयोः.",
            "Visarga before त or थ → स्.",
            teaches="A visarga before त or थ becomes स्: यः + तयोः → यस्तयोः."),
    ],
}

# ---------------------------------------------------------------- unit 33
AUTHORED["33"] = {
    "title": "यः शष्कुलीरपूपान्वाऽभ्यवहृत्य",
    "question": "What kinds of scenes does the long list of card 33 give, and what does it say of the sick who show them?",
    "rule": ("A long prose list of 'who …' clauses (eating cakes and vomiting on waking, creepers on the head, being swallowed by a "
             "fish, rebuked by angry forefathers, …) closes: they, being sick (व्याधिताः), attain pañcatā (death)."),
    "limits": ("Prose, one long printed line; medium. Open or conjectural: patati (printed patya), vakram (maybe vaktram), facing or "
               "toward the south, the reach of aśnāti, puṣpāḍhya: no question on these. Plant names keep the data's labels. "
               "The card states signs only, no advice."),
    "explain_hi": ("यह एक लम्बी गद्य पंक्ति है जिसमें ‘जो …’ वाले बहुत से उपवाक्य ‘वा’ और ‘च’ से जुड़े हैं: शष्कुली (सम्भवतः तली टिकिया) या अपूप खाकर जागने पर उलटी; "
                   "सिर पर लताएँ उगना और पक्षियों का बैठना; गिद्ध, उल्लू, कौए आदि से सेवा; नाचती स्त्री द्वारा खींचा जाना; नग्न होकर लाल माला; "
                   "कीचड़, कुओं, गँदले जल में डूबना; मछली द्वारा निगला जाना; क्रुद्ध पितरों की डाँट; चन्द्र, सूर्य, तारा, दीपक आदि में से किसी को नष्ट होते देखना; "
                   "हाथ में दण्ड और पाश लिए काले, लाल आँखों वाले पुरुष, और कालरात्रि के रूप वाली स्त्री। "
                   "अन्त में: ‘ते व्याधिताः पञ्चतामाप्नुवन्ति’, वे रोगी पंचता (मृत्यु) को प्राप्त होते हैं। स्वस्थों के विषय में कार्ड ३४ है।"),
    "hook": "लम्बी सूची के अन्त में: रोगी हो तो पंचता।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By card 33, what do the sick who show these signs attain?",
            ("पञ्चता, that is death", "ते व्याधिताः पञ्चतामाप्नुवन्ति: they, being sick, attain pañcatā (death)."),
            [("आरोग्य, that is health", "Health is not the outcome named; the sick attain pañcatā."),
             ("उन्माद, that is insanity", "उन्माद is named in card 29, not as the end of card 33."),
             ("प्रमेह, a urinary disorder", "प्रमेह is named in card 29, not as the end of card 33.")],
            "पञ्चता ('five-ness') = death.",
            "व्याधिताः पञ्चताम् आप्नुवन्ति."),
        order(1, "Put these sure parts of card 33 in the printed order.",
              ["शष्कुलीरपूपान्वाऽभ्यवहृत्य", "शिरसि लतादयो जायंते", "गृध्रोलूककाकाद्यैः", "मत्स्येन वा ग्रस्यते",
               "निर्भर्त्स्यते वा कुपितैःपितृभिः", "पंचतामाप्नुवंति"],
              "Eating cakes; creepers on the head; vultures, owls, crows; swallowed by a fish; rebuked by angry forefathers; they attain pañcatā.",
              "शष्कुली… → शिरसि लतादयो → गृध्रोलूक… → मत्स्येन ग्रस्यते → कुपितैःपितृभिः → पंचताम्."),
        match(2, "Match each sure word of card 33 to its meaning.",
              [["दिग्वासाः", "naked (sky-clothed)"], ["मत्स्येन", "by a fish"], ["पङ्कदिग्धः", "smeared with mud"],
               ["कुपितैः पितृभिः", "by angry forefathers"], ["शून्याटवीम्", "a deserted forest"], ["पञ्चताम्", "death (five-ness)"]],
              "दिग्वासाः = naked, मत्स्येन = by a fish, पङ्कदिग्धः = mud-smeared, कुपितैः पितृभिः = by angry forefathers, शून्याटवीम् = deserted forest, पञ्चताम् = death.",
              "दिग्वासाः, मत्स्येन, पङ्कदिग्धः, कुपितैः पितृभिः, शून्याटवीम्, पञ्चताम्.",
              role="extend",
              teaches="पञ्चता ('five-ness') is the text's word for death; दिग्वासाः ('sky-clothed') means naked."),
        mcq("discriminate", 3, "By card 33, who are said to attain pañcatā?",
            ("Those who are sick (व्याधिताः)", "ते व्याधिताः पञ्चतामाप्नुवन्ति: the sick ones attain pañcatā."),
            [("Those who are healthy (स्वस्थाः)", "For the healthy card 34 states 'a doubt about life', not pañcatā."),
             ("Only the very old (वृद्धाः)", "No old age is named; the closing word is व्याधिताः."),
             ("Only young boys (बालाः)", "No boys are named here; the closing word is व्याधिताः.")],
            "व्याधिताः = afflicted with disease, sick.",
            "ते व्याधिताः पञ्चताम् आप्नुवन्ति."),
        mcq("apply", 4, "Which split of पांशूपधानायां in card 33 is right?",
            ("पांशु + उपधानायाम्", "उ + उ → ऊ: पांशु + उपधानायाम् → पांशूपधानायाम्."),
            [("पांशू + पधानायाम्", "पधाना is not a word; the ऊ comes from उ + उ."),
             ("पांशु + अपधानायाम्", "उ + अ gives व: that would print पांश्वपधानायां."),
             ("पांशो + उपधानायाम्", "ओ + उ gives अवु: that would print पांशवुपधानायां.")],
            "पांशु (dust) + उपधानायाम् (with a pillow): ground that has dust for a pillow.",
            "उ + उ → ऊ."),
        mcq("transfer", 5, "By the pattern of पांशु + उपधाना → पांशूपधाना, how is भानु + उदयः (the rise of the sun) joined in a new example?",
            ("भानूदयः", "उ + उ → ऊ: भानु + उदयः → भानूदयः."),
            [("भान्वुदयः", "उ → व् happens before an unlike vowel; here the vowel is alike."),
             ("भानोदयः", "ओ comes from अ + उ, not from उ + उ."),
             ("भानुदयः", "Two उ merge into a long ऊ, not a short उ.")],
            "भानु + उदयः = भानूदयः, like पांशु + उपधाना = पांशूपधाना.",
            "उ + उ → ऊ.",
            teaches="Two like vowels merge into the long vowel: उ + उ → ऊ, as in पांशु + उपधाना → पांशूपधाना."),
    ],
}

# ---------------------------------------------------------------- unit 34
AUTHORED["34"] = {
    "title": "स्वस्थास्तुजीवितसंदेहमिति",
    "question": "By card 34, what does the text state for the healthy?",
    "rule": ("But the healthy (स्वस्थाः तु): a doubt about life (जीवितसंदेहम्). इति (thus) closes the statement; the verb "
             "(आप्नुवन्ति, attain) is carried from card 33."),
    "limits": ("Prose, elliptical; medium. The verb is not printed. The card says only 'a doubt about life': nothing more on the "
               "outcome and no advice."),
    "explain_hi": ("किन्तु स्वस्थ (लोग) जीवन के सन्देह को (प्राप्त होते हैं)। "
                   "क्रिया ‘आप्नुवन्ति’ (प्राप्त होते हैं) कार्ड ३३ से आती है, यहाँ छपी नहीं। "
                   "कार्ड ३३ रोगियों के लिए पंचता कहता है, यह कार्ड स्वस्थों के लिए केवल ‘जीवित-सन्देह’ कहता है; इससे अधिक कुछ नहीं। "
                   "‘इति’ कथन को समाप्त करता है। "
                   "सन्धि: स्वस्थाः + तु → स्वस्थास्तु (त से पहले विसर्ग → स्), संदेहम् + इति → संदेहमिति (म् स्वर से जुड़ता है)।"),
    "hook": "स्वस्थ के लिए: जीवन का सन्देह।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By card 34, what does the text state for the healthy?",
            ("A doubt about life", "स्वस्थास्तु जीवितसंदेहम्: but the healthy, a doubt about life."),
            [("A death that is certain", "Pañcatā (death) is stated for the sick in card 33, not the healthy."),
             ("A long, sure life", "The card says 'doubt', not a long life."),
             ("A cure of illness", "No cure is named; the card states a doubt about life.")],
            "जीवितसंदेहम् = a doubt about life.",
            "स्वस्थाः → जीवितसंदेहम्."),
        match(1, "Match each word of card 34 to its meaning.",
              [["स्वस्थाः", "the healthy (ones)"], ["तु", "but"], ["जीवित", "life"], ["संदेहम्", "doubt"], ["इति", "thus (closing)"]],
              "स्वस्थाः = the healthy, तु = but, जीवित = life, संदेहम् = doubt, इति = thus.",
              "स्वस्थाः, तु, जीवित, संदेहम्, इति."),
        fill(2, "The word for 'doubt' in card 34 is ____ (type it in Devanagari or in English letters, e.g. dharma).",
             accepts("संदेह", "saṃdeha", "संदेहम्", "sandeha"),
             "संदेह = doubt; जीवितसंदेहम् = a doubt about life.",
             "संदेह means doubt; with जीवित (life) it forms the tatpuruṣa जीवितसंदेह, a doubt about life.",
             "संदेह = doubt."),
        mcq("discriminate", 3, "Which split of स्वस्थास्तु in card 34 is right?",
            ("स्वस्थाः + तु", "Visarga before त → स्: स्वस्थाः + तु → स्वस्थास्तु."),
            [("स्वस्थः + तु", "The singular would print स्वस्थस्तु, with short अ; the print has स्थास्."),
             ("स्वस्थे + तु", "स्वस्थे + तु would print स्वस्थे तु, with no स्."),
             ("स्वस्थान् + तु", "स्वस्थान् + तु would print स्वस्थांस्तु, with a nasal.")],
            "स्वस्थाः (the healthy, plural) + तु (but).",
            "Visarga before त → स्."),
        mcq("apply", 4, "Which English rendering of card 34 is right?",
            ("But the healthy: a doubt about life", "स्वस्थाः तु जीवितसंदेहम्: but the healthy, a doubt about life."),
            [("But the sick: a doubt about their life", "स्वस्थाः are the healthy, not the sick."),
             ("But the healthy: a long, happy life", "संदेह is doubt, not a long life."),
             ("And the healthy: a doubt about death", "जीवित is life, and तु is 'but'.")],
            "स्वस्थाः = the healthy; तु = but; जीवितसंदेहम् = a doubt about life.",
            "स्वस्थाः तु जीवितसंदेहम्."),
        mcq("transfer", 5, "By the pattern of संदेहम् + इति → संदेहमिति, how is धनम् + इति (wealth, thus) joined in a new example?",
            ("धनमिति", "Final म् before a vowel joins it: धनम् + इति → धनमिति."),
            [("धनं इति", "ं stands for म् only before a consonant; before a vowel म् joins."),
             ("धनेति", "म् is not dropped; it joins the following vowel."),
             ("धनमीति", "The इ of इति stays short.")],
            "धनम् + इति = धनमिति, like संदेहम् + इति = संदेहमिति.",
            "Final म् + vowel → म् joins the vowel.",
            teaches="A final म् before a vowel is not written as ं; it joins the vowel: संदेहम् + इति → संदेहमिति."),
    ],
}

# ---------------------------------------------------------------- unit 35
AUTHORED["35"] = {
    "title": "भवंति चात्र",
    "question": "What does the formula of card 35 announce?",
    "rule": ("भवन्ति च अत्र, 'and on this matter there are': a lead-in formula that, in this treatise, introduces the verses "
             "that follow (from card 36)."),
    "limits": "Prose formula; nothing is supplied after भवन्ति. The card itself states no topic.",
    "explain_hi": ("‘भवन्ति चात्र’ = और इस विषय में (ये) हैं। "
                   "डेटा के अनुसार यह सूत्र इस ग्रन्थ में आगे आने वाले श्लोकों का परिचय देता है, यहाँ कार्ड ३६ से। "
                   "भवन्ति के बाद कुछ नहीं जोड़ा गया। "
                   "सन्धि: च + अत्र → चात्र (अ + अ → आ)। छपा ‘भवंति’ = भवन्ति: त से पहले न् को अनुस्वार से लिखा गया।"),
    "hook": "भवन्ति चात्र: अब श्लोक आते हैं।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "In card 35, what does अत्र mean?",
            ("Here, on this matter", "अत्र = here, in this matter."),
            [("There, in that place far off", "There would be तत्र; अत्र is here."),
             ("Now, at once", "Now would be अधुना; अत्र is here."),
             ("Again, once more", "Again would be पुनः; अत्र is here.")],
            "अत्र = here.",
            "अत्र = here."),
        match(1, "Match each word of card 35 to its meaning.",
              [["भवन्ति", "there are"], ["च", "and"], ["अत्र", "here, on this matter"]],
              "भवन्ति = there are, च = and, अत्र = here.",
              "भवन्ति, च, अत्र."),
        mcq("extend", 2, "By the data, what does the formula भवन्ति चात्र do in this treatise?",
            ("It leads into the verses after it", "The data: it introduces the verses that follow, here from card 36."),
            [("It closes the whole chapter here", "The chapter goes on; the formula opens what follows."),
             ("It names a disease of the dreamer", "It names no disease; it is a lead-in formula."),
             ("It gives the name of the metre", "It names no metre; it introduces the verses.")],
            "भवन्ति चात्र = and on this matter there are (verses).",
            "भवन्ति चात्र introduces verses.",
            teaches="भवन्ति चात्र ('and here there are') is a formula that leads into verses; here card 36 onward."),
        mcq("discriminate", 3, "Which split of चात्र in card 35 is right?",
            ("च + अत्र", "अ + अ → आ: च + अत्र → चात्र."),
            [("च + त्र", "With त्र no vowel joins: it would print चत्र, short."),
             ("चे + अत्र", "ए + अ gives एऽ: that would print चेऽत्र."),
             ("चा + अत्र", "चा is not a word; च is the particle 'and'.")],
            "च (and) + अत्र (here): अ + अ → आ.",
            "अ + अ → आ."),
        fill(4, "The verb meaning 'there are' in card 35 is ____ (type it in Devanagari or in English letters, e.g. dharma).",
             accepts("भवन्ति", "bhavanti", "भवंति"),
             "भवन्ति = there are (present, third person plural of √भू); the print writes it भवंति, with ं for न् before त.",
             "भवन्ति is the present plural of √भू (to be); before त the nasal may be printed as anusvāra, so भवंति = भवन्ति.",
             "भवन्ति = there are.", role="apply"),
        mcq("transfer", 5, "By the pattern of च + अत्र → चात्र, how is सह + अनुजेन (with the younger brother) joined in a new example?",
            ("सहानुजेन", "अ + अ → आ: सह + अनुजेन → सहानुजेन."),
            [("सहनुजेन", "The two अ merge into long आ, not short अ."),
             ("सहोनुजेन", "ओ comes from अ + उ, not from अ + अ."),
             ("सहेनुजेन", "ए comes from अ + इ, not from अ + अ.")],
            "सह + अनुजेन = सहानुजेन, like च + अत्र = चात्र.",
            "अ + अ → आ.",
            teaches="अ + अ merge into आ: च + अत्र → चात्र."),
    ],
}

# ---------------------------------------------------------------- unit 36
AUTHORED["36"] = {
    "title": "मनोवहानां पूर्णत्वात्स्रोतसां",
    "question": "By card 36, why are terrible dreams seen, and by whom?",
    "rule": ("Because the mind-carrying channels (मनोवहानां स्रोतसाम्) are full (पूर्णत्वात्) of powerful malas (प्रबलैः मलैः), "
             "terrible dreams (दारुणाः स्वप्नाः) are seen by those whose selves are turned toward destruction."),
    "limits": ("Verse, two printed lines (reason, then statement). Whether mala here means the doṣas is not stated: no question "
               "on it. The verse names no particular dream."),
    "explain_hi": ("मन को वहन करने वाले स्रोतस् (मार्ग) जब प्रबल मलों (अपशिष्ट) से भरे हों, तब विनाश की ओर उन्मुख आत्मा वाले लोग भयंकर स्वप्न देखते हैं। "
                   "पहली पंक्ति कारण देती है (पञ्चमी ‘पूर्णत्वात्’ = भरे होने के कारण), दूसरी पंक्ति कथन। "
                   "यहाँ ‘मल’ से दोष अभिप्रेत हैं या नहीं, यह नहीं कहा गया। "
                   "सन्धि: मनस् + वह → मनोवह (अस् घोष व्यंजन से पहले → ओ), प्रबलैः + मलैः → प्रबलैर्मलैः (ऐ के बाद विसर्ग घोष वर्ण से पहले → र्), "
                   "स्वप्नाः + विनाश- → स्वप्ना विनाश- (आः घोष वर्ण से पहले विसर्ग खोता है)।"),
    "hook": "मनोवह स्रोतस् मलों से भरे: दारुण स्वप्न।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By card 36, what fills the mind-carrying channels?",
            ("Powerful malas", "पूर्णत्वात् स्रोतसां प्रबलैर्मलैः: the channels are full of powerful malas."),
            [("Very clear water", "No water is named; the channels are full of malas."),
             ("Kindled fire", "No fire is named; the channels are full of malas."),
             ("Pure ghee", "No ghee is named; the channels are full of malas.")],
            "मल = waste matter, impurity.",
            "स्रोतांसि प्रबलैः मलैः पूर्णानि."),
        order(1, "Put the parts of card 36 in the printed order.",
              ["मनोवहानां", "पूर्णत्वात्स्रोतसां", "प्रबलैर्मलैः", "दृश्यंते", "दारुणाः स्वप्ना", "विनाशाभिमुखात्मभिः"],
              "Mind-carrying; because of the fullness of the channels; with powerful malas; are seen; terrible dreams; by those turned toward destruction.",
              "मनोवहानां → पूर्णत्वात्स्रोतसां → प्रबलैर्मलैः → दृश्यंते → दारुणाः स्वप्ना → विनाशाभिमुखात्मभिः."),
        match(2, "Match each word of card 36 to its meaning.",
              [["मनोवह", "mind-carrying"], ["स्रोतस्", "channel"], ["मल", "waste matter"], ["दारुण", "terrible"],
               ["स्वप्न", "dream"], ["विनाशाभिमुख", "turned toward destruction"]],
              "मनोवह = mind-carrying, स्रोतस् = channel, मल = waste matter, दारुण = terrible, स्वप्न = dream, विनाशाभिमुख = turned toward destruction.",
              "मनोवह, स्रोतस्, मल, दारुण, स्वप्न, विनाशाभिमुख.",
              role="extend",
              teaches="The ablative पूर्णत्वात् gives the reason (line 1); the main clause दृश्यन्ते दारुणाः स्वप्नाः follows (line 2)."),
        mcq("discriminate", 3, "In card 36, what does the ablative पूर्णत्वात् express?",
            ("The reason: because of fullness", "The ablative of an abstract noun gives the cause: because the channels are full."),
            [("The tool: by means of fullness", "'By means of' would be the instrumental पूर्णत्वेन."),
             ("The owner: belonging to fullness", "'Of, belonging to' would be the genitive पूर्णत्वस्य."),
             ("The place: inside the fullness", "'In' would be the locative पूर्णत्वे.")],
            "पूर्णत्वात् = because of the fullness.",
            "Ablative of -त्व = because of."),
        mcq("apply", 4, "Why is स्वप्नाः printed स्वप्ना before विनाश- in card 36?",
            ("आः drops its visarga before a voiced sound", "After आ the visarga drops before the voiced व: स्वप्ना विनाश-."),
            [("Every visarga drops before a consonant", "Not every: after ऐ it gives र् (प्रबलैर्मलैः, same card)."),
             ("आः before a voiced sound turns into ओ", "ओ comes from अः (short अ), not from आः."),
             ("The plural form itself ends in -आ", "The nominative plural is स्वप्नाः; the visarga drops only by sandhi.")],
            "स्वप्नाः + विनाशाभिमुख- → स्वप्ना विनाशाभिमुख-.",
            "आः + voiced sound → आ."),
        mcq("transfer", 5, "By the pattern of प्रबलैः + मलैः → प्रबलैर्मलैः, how is अश्वैः + गच्छति (goes with horses) joined in a new example?",
            ("अश्वैर्गच्छति", "Visarga after ऐ before the voiced ग → र्: अश्वैर्गच्छति."),
            [("अश्वै गच्छति", "The visarga drops before a voiced sound only after अ/आ; after ऐ it gives र्."),
             ("अश्वैस्गच्छति", "स् comes from a visarga before त or थ (optionally before स), not before ग."),
             ("अश्वैश्गच्छति", "श् comes from a visarga before च or छ (optionally before श), not before ग.")],
            "अश्वैः + गच्छति = अश्वैर्गच्छति, like प्रबलैः + मलैः = प्रबलैर्मलैः.",
            "Visarga after a vowel other than अ/आ, before a voiced sound → र्.",
            teaches="A visarga after a vowel other than अ/आ becomes र् before a voiced sound: प्रबलैः + मलैः → प्रबलैर्मलैः."),
    ],
}

# ---------------------------------------------------------------- unit 37
AUTHORED["37"] = {
    "title": "अकल्याणमपि स्वप्नं दृष्ट्वा",
    "question": "By card 37, what result follows when an inauspicious dream is followed by an auspicious one?",
    "rule": ("One who, having seen (दृष्ट्वा) even an inauspicious dream (अकल्याणम् अपि स्वप्नम्), right there (तत्रैव) again "
             "(पुनः) sees a gentle, auspicious one (सौम्यं शुभम्): for him the result would be auspicious indeed (शुभमेव फलम्)."),
    "limits": ("Verse; two printed lines, one sentence. तत्रैव is taken as 'right there' (that place or that same sleep); the "
               "text does not say which: no question on it. The noun of सौम्यं शुभं (the dream) is understood."),
    "explain_hi": ("अशुभ स्वप्न देखकर भी जो वहीं फिर से सौम्य और शुभ (स्वप्न) देखे, उसके लिए फल शुभ ही हो। "
                   "‘दृष्ट्वा’ (देखकर) पूर्वकालिक क्रिया है, ‘पश्येत्’ और ‘भवेत्’ विधिलिङ् (चाहिए/हो) रूप हैं। "
                   "‘तत्रैव’ = वहीं; उसी स्थान में या उसी नींद में, यह नहीं कहा गया। "
                   "सन्धि: तत्र + एव → तत्रैव (अ + ए → ऐ), शुभम् + एव → शुभमेव (म् स्वर से जुड़ता है)।"),
    "hook": "अशुभ के बाद वहीं शुभ स्वप्न: फल शुभ ही।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By card 37, what is the result if an auspicious dream follows an inauspicious one?",
            ("An auspicious result", "तस्य शुभमेव फलं भवेत्: for him the result would be auspicious indeed."),
            [("A harmful outcome", "The verse says the result is auspicious (शुभम्)."),
             ("No outcome of any kind", "A result (फलम्) is named: an auspicious one."),
             ("A mixed outcome", "The verse says auspicious indeed (शुभमेव), not mixed.")],
            "शुभमेव फलम् = an auspicious result indeed.",
            "अकल्याण → then शुभ → फल शुभ."),
        order(1, "Put the parts of card 37 in the printed order.",
              ["अकल्याणमपि स्वप्नं", "दृष्ट्वा तत्रैव", "यः पुनः", "पश्येत्सौम्यं शुभं", "तस्य शुभमेव", "फलं भवेत्"],
              "Even an inauspicious dream; having seen, right there; who again; should see a gentle, auspicious one; for him auspicious indeed; would the result be.",
              "अकल्याणमपि स्वप्नं → दृष्ट्वा तत्रैव → यः पुनः → पश्येत्सौम्यं शुभं → तस्य शुभमेव → फलं भवेत्."),
        match(2, "Match each word of card 37 to its meaning.",
              [["अकल्याणम्", "inauspicious"], ["दृष्ट्वा", "having seen"], ["पुनः", "again"], ["सौम्यम्", "gentle"],
               ["फलम्", "result"]],
              "अकल्याणम् = inauspicious, दृष्ट्वा = having seen, पुनः = again, सौम्यम् = gentle, फलम् = result.",
              "अकल्याणम्, दृष्ट्वा, पुनः, सौम्यम्, फलम्.",
              role="extend",
              teaches="दृष्ट्वा (having seen) is an absolutive: the first dream comes before the second seeing (पश्येत्)."),
        mcq("discriminate", 3, "Which split of तत्रैव in card 37 is right?",
            ("तत्र + एव", "अ + ए → ऐ: तत्र + एव → तत्रैव."),
            [("तत्र + इव", "अ + इ gives ए: that would print तत्रेव."),
             ("तत्र + ओव", "ओव is not a word; अ + ओ would give औ."),
             ("तत्रा + एव", "तत्रा is not a word; तत्र is 'there'.")],
            "तत्र (there) + एव (just): अ + ए → ऐ.",
            "अ + ए → ऐ."),
        mcq("apply", 4, "In card 37, what form is पश्येत्?",
            ("Optative: should see", "पश्येत् is the optative of √दृश् (stem पश्य-): should see."),
            [("Absolutive: having seen", "The absolutive is दृष्ट्वा, earlier in the same verse."),
             ("Past tense: he saw", "A past form would be अपश्यत्; पश्येत् is optative."),
             ("Future: he will see", "The future would be द्रक्ष्यति; पश्येत् is optative.")],
            "पश्येत् = should see (optative, third person singular).",
            "पश्येत्, भवेत्: optative."),
        mcq("transfer", 5, "By the pattern of तत्र + एव → तत्रैव, how is अद्य + एव (this very day) joined in a new example?",
            ("अद्यैव", "अ + ए → ऐ: अद्य + एव → अद्यैव."),
            [("अद्येव", "ए comes from अ + इ, not from अ + ए."),
             ("अद्यौव", "औ comes from अ + ओ or अ + औ, not from अ + ए."),
             ("अद्ययेव", "No य् is inserted; अ and ए merge into ऐ.")],
            "अद्य + एव = अद्यैव, like तत्र + एव = तत्रैव.",
            "अ + ए → ऐ.",
            teaches="अ before ए gives ऐ: तत्र + एव → तत्रैव."),
    ],
}

# ---------------------------------------------------------------- unit 38
AUTHORED["38"] = {
    "title": "देवान् द्विजान् गोवृषभान्",
    "question": "Which beings and things does the list of card 38 name?",
    "rule": ("A list of accusatives: gods, the twice-born, cows and bulls (or bulls), living friends, kings, good men, famous ones, a kindled "
             "fire, very clear water-bodies. By the data they are objects of पश्येत् (card 40), or continue card 37."),
    "limits": ("Verse; two printed lines; no verb in the card. गोवृषभान् may be 'cows and bulls' or 'bulls': no question on it. "
               "Printed वन्हिम् is read वह्निम् (letter reversal; the data calls it certain)."),
    "explain_hi": ("देवताओं को, द्विजों को, गायों और बैलों को, जीवित मित्रों को, राजाओं को, सज्जनों को, यशस्वियों को, प्रज्वलित अग्नि को और अत्यन्त स्वच्छ जलाशयों को। "
                   "इस कार्ड में क्रिया नहीं; डेटा के अनुसार ये कार्ड ४० के ‘पश्येत्’ (देखे) के कर्म हैं, या कार्ड ३७ से जुड़ते हैं। "
                   "‘गोवृषभान्’ को ‘गाय और बैल’ या केवल ‘बैल’ दोनों पढ़ा जा सकता है। "
                   "सन्धि: सुहृदः + नृपान् → सुहृदो नृपान्, यशस्विनः + वह्निम् → यशस्विनो वह्निम् (अः घोष व्यंजन से पहले → ओ); जल + आशय → जलाशय (अ + आ → आ)।"),
    "hook": "देव, द्विज, गो-वृषभ, मित्र, राजा, साधु, यशस्वी, जलती अग्नि, स्वच्छ जल।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "In card 38, what does जलाशयान् mean?",
            ("Water-bodies", "जल (water) + आशय (resting place): water-bodies, lakes and ponds."),
            [("Grain stores", "Grain would be धान्य; जल is water."),
             ("Cattle sheds", "Cattle sheds would be गोष्ठ; जल is water."),
             ("Shrine posts", "Posts would be यूप or स्तम्भ; जल is water.")],
            "जलाशयान् = water-bodies (accusative plural).",
            "जल + आशय = जलाशय."),
        match(1, "Match each word of card 38 to its meaning.",
              [["देवान्", "gods"], ["द्विजान्", "the twice-born"], ["सुहृदः", "friends"], ["नृपान्", "kings"],
               ["साधून्", "good men"], ["वह्निम्", "fire"]],
              "देवान् = gods, द्विजान् = twice-born, सुहृदः = friends, नृपान् = kings, साधून् = good men, वह्निम् = fire.",
              "देवान्, द्विजान्, सुहृदः, नृपान्, साधून्, वह्निम्."),
        order(2, "Put these items of card 38 in the printed order.",
              ["देवान्", "द्विजान्", "सुहृदो", "साधून्", "यशस्विनो", "जलाशयान्"],
              "Gods; twice-born; friends; good men; famous (ones); water-bodies.",
              "देवान् → द्विजान् → सुहृदो → साधून् → यशस्विनो → जलाशयान्.",
              role="extend",
              teaches="The card is a row of accusative plurals (-आन्, -ऊन्, -अः) with no verb; by the data the verb comes in card 40."),
        multi("discriminate", 3, "Which of these does card 38 list?",
              [("Turbid water", "No: turbid water (कलुषोदक) is in card 33; card 38 has very clear water-bodies."),
               ("A kindled fire", "Yes: वह्निम् इद्धम्, a kindled fire."),
               ("Living friends", "Yes: जीवतः सुहृदः, living friends."),
               ("Angry forefathers", "No: angry forefathers are in card 33."),
               ("Very clear water-bodies", "Yes: स्वच्छान् जलाशयान्."),
               ("Black, red-eyed men", "No: black, red-eyed men are in card 33.")],
              [1, 2, 4],
              "Card 38: gods, twice-born, cows and bulls (or bulls), living friends, kings, good men, famous ones, kindled fire, clear water-bodies.",
              "Card 38 has clear water and kindled fire; card 33 has turbid water."),
        mcq("apply", 4, "Why is सुहृदः printed सुहृदो before नृपान् in card 38?",
            ("अः before a voiced consonant → ओ", "न is a voiced consonant: सुहृदः + नृपान् → सुहृदो नृपान्."),
            [("अः before any consonant → ओ", "Not any: before त it gives स् (यस्तयोः, card 32)."),
             ("ओ is the last vowel of the stem itself", "The stem is सुहृद्; the ओ comes from the visarga by sandhi."),
             ("अः before a vowel → ओ, always", "Before vowels other than अ, अः gives अ (नेत्ररोग उपजायते, card 31).")],
            "सुहृदः + नृपान् → सुहृदो नृपान्.",
            "अः + voiced consonant → ओ."),
        mcq("transfer", 5, "By the pattern of सुहृदः + नृपान् → सुहृदो नृपान्, how is गजः + धावति (the elephant runs) written in a new example?",
            ("गजो धावति", "अः before the voiced consonant ध → ओ: गजो धावति."),
            [("गज धावति", "The gap form is for अः before a vowel other than अ, not before a consonant."),
             ("गजर्धावति", "र् comes from a visarga after a vowel other than अ/आ."),
             ("गजा धावति", "अः does not lengthen to आ; before a voiced consonant it gives ओ.")],
            "गजः + धावति = गजो धावति, like सुहृदः + नृपान् = सुहृदो नृपान्.",
            "अः + voiced consonant → ओ.",
            teaches="अः before a voiced consonant becomes ओ: सुहृदः + नृपान् → सुहृदो नृपान्."),
    ],
}

# ---------------------------------------------------------------- unit 39
AUTHORED["39"] = {
    "title": "कन्यां कुमारकान् गौरान्",
    "question": "Which figures does the list of card 39 add?",
    "rule": ("The list goes on: a maiden, boys, fair ones, white-clothed ones, very radiant ones; a man-eating one, a blazing-bodied "
             "one, sprinkled with blood all around. By the data the verb is पश्येत् in card 40."),
    "limits": ("Verse; medium. गौरान्, शुक्लवस्त्रान्, सुतेजसः may describe the boys or stand alone; line 2 may be one figure or "
               "three; नराशन names no particular being: no question on these. No verb in the card."),
    "explain_hi": ("कन्या को, कुमारों को, गोरों को, श्वेत वस्त्र वालों को, अत्यन्त तेजस्वियों को; नरभक्षी को, दीप्त शरीर वाले को, चारों ओर से रक्त से सींचे हुए को। "
                   "‘गौरान्, शुक्लवस्त्रान्, सुतेजसः’ कुमारों के विशेषण भी हो सकते हैं; दूसरी पंक्ति के तीन शब्द एक आकृति के हैं या तीन के, यह नहीं कहा। "
                   "‘नराशन’ शब्दशः नरभक्षी; किसी विशेष प्राणी का नाम नहीं। क्रिया कार्ड ४० में (डेटा)। "
                   "सन्धि: समन्तात् + रुधिर- → समन्ताद्रुधिर- (त् घोष व्यंजन से पहले → द्), रुधिर + उक्षितम् → रुधिरोक्षितम् (अ + उ → ओ)।"),
    "hook": "कन्या, कुमार, श्वेत वस्त्र, तेजस्वी; दीप्त शरीर, रक्त से सिक्त।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "In card 39, what does कन्याम् mean?",
            ("A maiden", "कन्याम् = a maiden, a girl (accusative singular)."),
            [("A mother", "Mother would be जननी or माता; कन्या is a maiden."),
             ("A widow", "Widow would be विधवा; कन्या is a maiden."),
             ("A queen", "Queen would be राज्ञी; कन्या is a maiden.")],
            "कन्या = maiden.",
            "कन्या = maiden."),
        match(1, "Match each word of card 39 to its meaning.",
              [["कन्याम्", "a maiden"], ["कुमारकान्", "boys"], ["शुक्लवस्त्रान्", "white-clothed"], ["दीप्ततनुम्", "blazing-bodied"],
               ["रुधिरोक्षितम्", "sprinkled with blood"]],
              "कन्याम् = a maiden, कुमारकान् = boys, शुक्लवस्त्रान् = white-clothed, दीप्ततनुम् = blazing-bodied, रुधिरोक्षितम् = sprinkled with blood.",
              "कन्याम्, कुमारकान्, शुक्लवस्त्रान्, दीप्ततनुम्, रुधिरोक्षितम्."),
        order(2, "Put these words of card 39 in the printed order.",
              ["कन्यां", "कुमारकान्", "शुक्लवस्त्रान्", "नराशनं", "दीप्ततनुं", "समंताद्रुधिरोक्षितं"],
              "A maiden; boys; white-clothed; man-eating; blazing-bodied; sprinkled with blood all around.",
              "कन्यां → कुमारकान् → शुक्लवस्त्रान् → नराशनं → दीप्ततनुं → समंताद्रुधिरोक्षितं.",
              role="extend",
              teaches="Bahuvrīhis such as शुक्लवस्त्र (whose cloth is white) and दीप्ततनु (whose body blazes) describe a person by a feature."),
        mcq("discriminate", 3, "Which split of रुधिरोक्षितं in card 39 is right?",
            ("रुधिर + उक्षितम्", "अ + उ → ओ: रुधिर + उक्षितम् → रुधिरोक्षितम्."),
            [("रुधिरः + उक्षितम्", "अः before उ gives अ with a gap: रुधिर उक्षितम्."),
             ("रुधिर + अक्षितम्", "अ + अ gives आ: that would print रुधिराक्षितं."),
             ("रुधिर + ओक्षितम्", "ओक्षित is not a word; अ + ओ would give औ.")],
            "रुधिर (blood) + उक्षितम् (sprinkled): अ + उ → ओ.",
            "अ + उ → ओ."),
        mcq("apply", 4, "Why is समन्तात् printed समंताद् before रुधिर- in card 39?",
            ("त् before a voiced consonant → द्", "र is voiced: समन्तात् + रुधिर- → समन्ताद्रुधिर-."),
            [("त् before any consonant → द्", "Not before a voiceless one: पूर्णत्वात्स्रोतसां (card 36) keeps त्."),
             ("द् is the word's own last letter", "The word is समन्तात्; the द् comes from sandhi."),
             ("त् before र is dropped", "The त् is not dropped; it becomes द्.")],
            "समन्तात् + रुधिरोक्षितम् → समन्ताद्रुधिरोक्षितम्.",
            "त् + voiced consonant → द् (before a nasal, न् is also possible)."),
        mcq("transfer", 5, "By the pattern of समन्तात् + रुधिर- → समन्ताद्रुधिर-, how is दूरात् + वदति (speaks from afar) joined in a new example?",
            ("दूराद्वदति", "त् before the voiced व → द्: दूरात् + वदति → दूराद्वदति."),
            [("दूरात्वदति", "त् stays only before a voiceless sound; व is voiced."),
             ("दूरान्वदति", "न् is a possible form only before a nasal; व is not a nasal."),
             ("दूराव्वदति", "त् does not turn into व्; before a voiced sound it gives द्.")],
            "दूरात् + वदति = दूराद्वदति, like समन्तात् + रुधिर- = समन्ताद्रुधिर-.",
            "त् + voiced consonant → द्.",
            teaches="A final त् before a voiced consonant becomes द्: समन्तात् + रुधिरोक्षितम् → समन्ताद्रुधिरोक्षितम्."),
    ],
}

# ================================================================ NOTES_HI
NOTES_HI = {
    "27": ("गद्य; विश्वास निम्न; एक छपी पंक्ति (०२.१२.२८)। पाठ-चिह्न (सम्भव): ‘यस्य शिरसि’ के बाद वह संज्ञा या क्रिया नहीं छपी जो बताए कि सिर पर क्या "
           "दिखता या उगता है; पड़ोसी कार्ड २६ और २८ की तरह सम्भवतः एक शब्द छूटा है। डेटा कुछ नहीं जोड़ता, इसलिए उस पर प्रश्न नहीं। "
           "सन्धि जाँची: शिरस् + रोगेण → शिरोरोगेण (अस् घोष व्यंजन र से पहले → ओ); शिरः + छेदनेन → शिरश्छेदनेन (छ से पहले विसर्ग → श्)। "
           "सः व्यंजन से पहले ‘स’ छपा है।"),
    "28": ("गद्य; विश्वास मध्यम; एक छपी पंक्ति (०२.१२.२९)। पाठ-चिह्न (निश्चित): पहला लम्बा शब्द ‘यस्यनग्नस्या…’ बिना रिक्त स्थान के छपा; यस्य अलग शब्द है। "
           "डेटा इसे षष्ठी-निरपेक्ष (genitive absolute) कहता है; षष्ठी रूप ‘उरसि’ वाले व्यक्ति का वर्णन भी करते हैं। ‘स कुष्ठेन’ की क्रिया छपी नहीं। "
           "कुष्ठ = त्वचा रोगों का समूह, कोढ़ सहित (standard)। "
           "सन्धि जाँची: नग्नस्य + आज्य- → नग्नस्याज्य-; आज्य + अवसिक्त → आज्यावसिक्त (अ + अ → आ); अग्निम् + अनर्चिषम् → अग्निमनर्चिषम्; "
           "जुह्वतः + जायन्ते → जुह्वतो जायन्ते (अः घोष व्यंजन से पहले → ओ); पद्मानि + उरसि → पद्मान्युरसि (इ + उ → यु)। छपा ‘जायंते’ = जायन्ते।"),
    "29": ("गद्य; विश्वास उच्च; दो छपी पंक्तियाँ (०२.१२.३० और ०२.१२.३१) जोड़ी गईं; कोई पाठ-चिह्न नहीं। दोनों मुख्य वाक्यों की क्रिया छपी नहीं। "
           "प्रमेह = मूत्र रोगों का समूह, मधुमेह जैसा (probable); उन्माद = पागलपन (standard)। "
           "सन्धि जाँची: यः + चण्डालैः → यश्चण्डालैः (च से पहले विसर्ग → श्); यः + रक्षोभिः → यो रक्षोभिः (अः घोष व्यंजन से पहले → ओ); "
           "रक्षस् + भिः → रक्षोभिः; नृत्यन् + अप्सु → नृत्यन्नप्सु (ह्रस्व स्वर के बाद न् स्वर से पहले दुगना)। छपा ‘चंडालैः’ = चण्डालैः।"),
    "30": ("गद्य; विश्वास मध्यम; एक छपी पंक्ति (०२.१२.३२)। पाठ-चिह्न (सम्भव): छपा ‘मत्त:’ में विसर्ग की जगह कोलन है (छपाई की आदत)। "
           "‘मत्त’ = नशे में या उन्मत्त, दोनों सम्भव; किसी एक पर प्रश्न नहीं। अपस्मार = मिर्गी (standard)। "
           "सन्धि जाँची: यः + मत्तः → यो मत्तः; सः + अपस्मारेण → सोऽपस्मारेण (अः + अ → ओ, अ का लोप, ऽ)।"),
    "31": ("गद्य; विश्वास उच्च; एक छपी पंक्ति (०२.१२.३३); कोई पाठ-चिह्न नहीं। "
           "सन्धि जाँची: यः + चन्द्र- → यश्चन्द्र- (च से पहले विसर्ग → श्); सूर्ययोः + उपरागम् → सूर्ययोरुपरागम् (ओ के बाद विसर्ग, घोष वर्ण से पहले → र्); "
           "नेत्ररोगः + उपजायते → नेत्ररोग उपजायते (अः, अ से भिन्न स्वर से पहले → अ, अन्तर बना रहता है)। छपा ‘चंद्र’ = चन्द्र।"),
    "32": ("गद्य; विश्वास मध्यम; एक छपी पंक्ति (०२.१२.३४)। पाठ-चिह्न (निश्चित): ‘तस्यनेत्रविनाशः’ में रिक्त स्थान छूटा: तस्य नेत्रविनाशः। "
           "क्रिया ‘देखता है’ कार्ड ३१ (छपी पंक्ति ३३) से आती है, छपी नहीं; ‘वे दोनों’ डेटा के अनुसार चन्द्रमा और सूर्य। "
           "सन्धि जाँची: यः + तयोः → यस्तयोः (त से पहले विसर्ग → स्); पतनम् + तस्य → पतनं तस्य (व्यंजन से पहले म् → ं)।"),
    "33": ("गद्य; विश्वास मध्यम; एक लम्बी छपी पंक्ति (०२.१२.३५)। डेटा के अनुसार कार्ड ३३ और ३४ (छपी पंक्तियाँ ३५, ३६) सम्भवतः एक ही वाक्य हैं। "
           "पाठ-चिह्न: ‘पत्यारोहति’ में ‘पतति आरोहति’ अनुमानित पाठ है (छपा ‘पत्य’); ‘वक्रं’ की जगह ‘वक्त्रं’ (मुख) सम्भव पर अपनाया नहीं; "
           "‘आद्यै र्वा’ में छपा फालतू रिक्त स्थान; अनेक जगह रिक्त स्थान छूटे (भवतियो, स्वयंवा, परिष्वज्यतेनग्नो आदि)। "
           "दो तरफ़ा पाठ: दक्षिणाभिमुखम् (दक्षिण की ओर मुख किए या दक्षिण की ओर खींचा); अश्नाति केवल पक्वान्न लेता है या पूरी सूची; पुष्पाढ्य अलग सदस्य या "
           "आगे के वृक्षों का विशेषण; श्वभ्र-आयतन; स्रोतसा वा ह्रियते / वा आह्रियते। इन पर प्रश्न नहीं। "
           "पहचानें डेटा के लेबल के साथ: शाल्मली = सेमल, Bombax ceiba (standard); किंशुक = ढाक, Butea monosperma (standard); कोविदार = कचनार, "
           "Bauhinia variegata (probable); पारिभद्रक = Erythrina variegata (probable); वेत्र = बेंत (probable); वंश = बाँस (standard); कार्पास = कपास (standard); "
           "शष्कुली = तली टिकिया (probable)। छपाई की आदत: ब = व (बयांसि = वयांसि, प्रब्रजित = प्रव्रजित)। "
           "सन्धि जाँची: गृध्र + उलूक → गृध्रोलूक (अ + उ → ओ); पांशु + उपधाना → पांशूपधाना (उ + उ → ऊ); शून्य + अटवीम् → शून्याटवीम् (अ + अ → आ); "
           "कलुष + उदकेषु → कलुषोदकेषु; पञ्चताम् + आप्नुवन्ति → पञ्चतामाप्नुवन्ति।"),
    "34": ("गद्य; विश्वास मध्यम; एक छपी पंक्ति (०२.१२.३६), पूरी बिना रिक्त स्थान के छपी। डेटा के अनुसार यह कार्ड ३३ का वाक्य पूरा करती है; "
           "क्रिया ‘आप्नुवन्ति’ कार्ड ३३ से आती है, छपी नहीं। ‘स्वस्थाः’ बहुवचन, ‘जीवितसंदेहम्’ उस क्रिया का कर्म। "
           "सन्धि जाँची: स्वस्थाः + तु → स्वस्थास्तु (त से पहले विसर्ग → स्); संदेहम् + इति → संदेहमिति (म् + स्वर)। छपा ‘संदेह’ = सन्देह।"),
    "35": ("गद्य सूत्र; विश्वास उच्च; एक छपी पंक्ति (०२.१२.३७); कोई पाठ-चिह्न नहीं। डेटा के अनुसार यह आगे के श्लोकों (कार्ड ३६ से; छपी पंक्ति ३८ से) का परिचय है। "
           "सन्धि जाँची: च + अत्र → चात्र (अ + अ → आ)। छपा ‘भवंति’ = भवन्ति (त से पहले न् अनुस्वार से लिखा)।"),
    "36": ("श्लोक (अनुष्टुभ्); विश्वास उच्च; दो छपी पंक्तियाँ (०२.१२.३८ और ०२.१२.३९), एक वाक्य: पहली पंक्ति कारण, दूसरी कथन; कोई पाठ-चिह्न नहीं। "
           "‘मल’ से दोष अभिप्रेत हैं या नहीं, यह नहीं कहा; इस पर प्रश्न नहीं। "
           "सन्धि जाँची: मनस् + वहानाम् → मनोवहानाम्; पूर्णत्वात् + स्रोतसाम् → पूर्णत्वात्स्रोतसाम् (अघोष स से पहले त् रहता है); "
           "प्रबलैः + मलैः → प्रबलैर्मलैः (ऐ के बाद विसर्ग घोष वर्ण से पहले → र्); स्वप्नाः + विनाश- → स्वप्ना विनाश- (आः घोष वर्ण से पहले विसर्ग खोता है); "
           "विनाश + अभिमुख + आत्मभिः → विनाशाभिमुखात्मभिः।"),
    "37": ("श्लोक (अनुष्टुभ्); विश्वास उच्च; दो छपी पंक्तियाँ (०२.१२.४० और ०२.१२.४१), एक वाक्य (क्रिया ‘पश्येत्’ दूसरी पंक्ति में); कोई पाठ-चिह्न नहीं। "
           "‘तत्रैव’ = वहीं: उसी स्थान में या उसी नींद में, यह नहीं कहा। ‘सौम्यं शुभं’ की संज्ञा (स्वप्न) समझी जाती है। "
           "सन्धि जाँची: अकल्याणम् + अपि → अकल्याणमपि; तत्र + एव → तत्रैव (अ + ए → ऐ); पश्येत् + सौम्यम् → पश्येत्सौम्यम्; शुभम् + एव → शुभमेव।"),
    "38": ("श्लोक (अनुष्टुभ्); विश्वास उच्च; दो छपी पंक्तियाँ (०२.१२.४२ और ०२.१२.४३)। क्रिया नहीं: डेटा के अनुसार ये कार्ड ४० (छपी पंक्ति ४६) के ‘पश्येत्’ के कर्म हैं, "
           "या कार्ड ३७ (छपी पंक्ति ४१) से जुड़ते हैं। पाठ-चिह्न (निश्चित): छपा ‘वन्हिमिद्धं’ = वह्निम् इद्धम् (ह्न का उलटा लेखन)। "
           "‘गोवृषभान्’ = गाय और बैल, या केवल बैल। ‘सुहृदोनृपान्’ में रिक्त स्थान छूटा। "
           "सन्धि जाँची: सुहृदः + नृपान् → सुहृदो नृपान्; यशस्विनः + वह्निम् → यशस्विनो वह्निम् (अः घोष व्यंजन से पहले → ओ); वह्निम् + इद्धम् → वह्निमिद्धम्; जल + आशय → जलाशय।"),
    "39": ("श्लोक (अनुष्टुभ्); विश्वास मध्यम; दो छपी पंक्तियाँ (०२.१२.४४ और ०२.१२.४५); कोई पाठ-चिह्न नहीं। सूची कार्ड ३८ से चलती है; क्रिया कार्ड ४० (छपी पंक्ति ४६) में। "
           "‘गौरान्, शुक्लवस्त्रान्, सुतेजसः’ अलग सदस्य या कुमारों के विशेषण; दूसरी पंक्ति एक आकृति या तीन; ‘नराशन’ किसी विशेष प्राणी का नाम नहीं। "
           "सन्धि जाँची: शुक्लवस्त्रान् + सुतेजसः (कोई परिवर्तन नहीं); नर + अशनम् → नराशनम् (अ + अ → आ); समन्तात् + रुधिर- → समन्ताद्रुधिर- (त् घोष व्यंजन से पहले → द्); "
           "रुधिर + उक्षितम् → रुधिरोक्षितम् (अ + उ → ओ)।"),
}

# ================================================================ AIDS
AIDS = {
    "27": {
        "frame": "किसके: यस्य → कहाँ: शिरसि (सिर पर) → क्या: छपा नहीं → फल: स शिरोरोगेण वा शिरश्छेदनेन।",
        "chunks": "यस्य शिरसि | स शिरोरोगेण | वा शिरश्छेदनेन",
        "sandhi": "अस् + घोष व्यंजन → ओ: शिरस् + रोगेण → शिरोरोगेण · छ से पहले विसर्ग → श्: शिरः + छेदनेन → शिरश्छेदनेन।",
    },
    "28": {
        "chain": {"steps": ["नग्नस्य: नंगा", "आज्यावसिक्तस्य: घी से सींचा", "अग्निमनर्चिषं जुह्वतः: बिना लौ की अग्नि में आहुति",
                            "पद्मानि उरसि जायन्ते: छाती पर कमल", "स कुष्ठेन: कुष्ठ से"]},
        "chunks": "यस्यनग्नस्याज्यावसिक्तस्याग्निमनर्चिषं | जुह्वतो | जायंते पद्मान्युरसि | स कुष्ठेन",
        "sandhi": "इ + उ → यु: पद्मानि + उरसि → पद्मान्युरसि · अः + घोष व्यंजन → ओ: जुह्वतः + जायन्ते → जुह्वतो जायन्ते · अ + अ → आ: आज्य + अवसिक्त → आज्यावसिक्त।",
    },
    "29": {
        "frame": "पंक्ति १: चण्डालैः सह स्नेहं पिबति → स प्रमेहेण · पंक्ति २: रक्षोभिः सह नृत्यन् अप्सु मज्जति → स उन्मादेन।",
        "chunks": "यश्चंडालैः सह | स्नेहं पिबति | स प्रमेहेण || यो रक्षोभिः सह | नृत्यन्नप्सु मज्जति | स उन्मादेन",
        "sandhi": "च से पहले विसर्ग → श्: यः + चण्डालैः → यश्चण्डालैः · ह्रस्व स्वर के बाद न् + स्वर → न्न्: नृत्यन् + अप्सु → नृत्यन्नप्सु।",
    },
    "30": {
        "chunks": "यो मत्त: | सोऽपस्मारेण",
        "sandhi": "अः + घोष व्यंजन → ओ: यः + मत्तः → यो मत्तः · अः + अ → ओऽ: सः + अपस्मारेण → सोऽपस्मारेण।",
        "anchors": "मत्त → अपस्मार; उन्माद (कार्ड २९) और अपस्मार (कार्ड ३०) दो अलग शब्द। (मेरी याद-पद्धति)",
    },
    "31": {
        "frame": "कौन: यः → क्या देखता: चन्द्रसूर्ययोः उपरागम् (ग्रहण) → फल: तस्य नेत्ररोगः उपजायते।",
        "chunks": "यश्चंद्रसूर्ययोरुपरागं | पश्यति | तस्य नेत्ररोग | उपजायते",
        "sandhi": "ओ के बाद विसर्ग + घोष वर्ण → र्: सूर्ययोः + उपरागम् → सूर्ययोरुपरागम् · अः + अ से भिन्न स्वर → अ (अन्तर): नेत्ररोगः + उपजायते → नेत्ररोग उपजायते।",
    },
    "32": {
        "diagram": {"groups": [
            {"label": "कार्ड २७-३२: चिह्न → रोग",
             "items": ["२७: सिर पर (शब्द छपा नहीं) → शिरोरोग या सिर कटना", "२८: छाती पर कमल → कुष्ठ",
                       "२९: चाण्डालों संग स्नेह → प्रमेह", "२९: राक्षसों संग नाचकर डूबना → उन्माद",
                       "३०: मत्त → अपस्मार", "३१: चन्द्र-सूर्य ग्रहण → नेत्ररोग", "३२: उनका गिरना → नेत्र-विनाश"]}]},
        "chunks": "यस्तयोः पतनं | तस्यनेत्रविनाशः",
        "sandhi": "त से पहले विसर्ग → स्: यः + तयोः → यस्तयोः · व्यंजन से पहले म् → ं: पतनम् + तस्य → पतनं तस्य।",
    },
    "33": {
        "diagram": {"groups": [
            {"label": "कार्ड ३३: कुछ पक्के चिह्न (छपे क्रम में)",
             "items": ["१ शष्कुली या अपूप खाकर जागने पर उलटी", "२ सिर पर लताएँ, पक्षी बैठें", "३ गिद्ध, उल्लू, कौए आदि सेवा करें",
                       "४ नाचती स्त्री खींचे", "५ नग्न होकर लाल माला", "६ कीचड़ से लिपटा हँसे या नाचे", "७ कीचड़, कुएँ, गँदले जल में डूबे",
                       "८ मछली निगले", "९ क्रुद्ध पितर डाँटें", "१० चन्द्र, सूर्य, तारा आदि नष्ट होते दिखें",
                       "११ दण्ड-पाश हाथ में लिए काले पुरुष", "१२ अन्त: ते व्याधिताः पंचताम् आप्नुवन्ति"]}]},
        "chunks": ("यः शष्कुलीरपूपान्वाऽभ्यवहृत्य प्रतिबुद्धश्छर्दयति | यस्य शिरसि लतादयो जायंते बयांसि च निलीयंते | "
                   "यो गृध्रोलूककाकाद्यैः … परिचर्यते | स्त्रिया नृत्यंत्या ऽऽकृष्यते | स्वयंवा दिग्वासा याति शून्याटवीं | "
                   "नग्नो वा रक्तां स्रजं धारयति | पंकदिग्धो हसति नृत्यति वा | पंककूपकलुषोदकेषु वा मज्जति | मत्स्येन वा ग्रस्यते | "
                   "निर्भर्त्स्यते वा कुपितैःपितृभिः | पुरुषान् वा नग्नान्कषायवाससोऽसौम्यान्दंडपाशहस्तान् | ते व्याधिताः पंचतामाप्नुवंति"),
        "sandhi": ("अ + उ → ओ: गृध्र + उलूक → गृध्रोलूक · उ + उ → ऊ: पांशु + उपधाना → पांशूपधाना · अ + अ → आ: शून्य + अटवीम् → शून्याटवीम् · "
                   "म् + स्वर: पञ्चताम् + आप्नुवन्ति → पञ्चतामाप्नुवन्ति।"),
    },
    "34": {
        "diagram": {"groups": [
            {"label": "कौन → क्या (कार्ड ३३-३४)",
             "items": ["व्याधिताः (रोगी, कार्ड ३३) → पंचता (मृत्यु)", "स्वस्थाः (स्वस्थ, कार्ड ३४) → जीवित-संदेह"]}]},
        "chunks": "स्वस्थास्तु | जीवितसंदेहम् | इति",
        "sandhi": "त से पहले विसर्ग → स्: स्वस्थाः + तु → स्वस्थास्तु · म् + स्वर: संदेहम् + इति → संदेहमिति।",
    },
    "35": {
        "chunks": "भवंति | चात्र",
        "sandhi": "अ + अ → आ: च + अत्र → चात्र।",
        "anchors": "भवन्ति चात्र = ‘और यहाँ (श्लोक) हैं’: गद्य से श्लोकों की ओर का द्वार। (मेरी याद-पद्धति)",
    },
    "36": {
        "chain": {"steps": ["मनोवह स्रोतस्", "प्रबल मलों से भरे (पूर्णत्वात्)", "दारुण स्वप्न दिखते हैं",
                            "किनको: विनाश की ओर उन्मुख आत्मा वालों को"]},
        "chunks": "मनोवहानां पूर्णत्वात्स्रोतसां प्रबलैर्मलैः | दृश्यंते दारुणाः स्वप्ना विनाशाभिमुखात्मभिः",
        "sandhi": ("अस् + घोष व्यंजन → ओ: मनस् + वह → मनोवह · ऐ के बाद विसर्ग + घोष वर्ण → र्: प्रबलैः + मलैः → प्रबलैर्मलैः · "
                   "आः + घोष वर्ण → आ: स्वप्नाः + विनाश- → स्वप्ना विनाश-।"),
    },
    "37": {
        "chain": {"steps": ["अकल्याणम् अपि स्वप्नं दृष्ट्वा: अशुभ स्वप्न देखकर भी", "तत्रैव पुनः: वहीं फिर",
                            "सौम्यं शुभं पश्येत्: सौम्य, शुभ देखे", "तस्य शुभमेव फलं भवेत्: फल शुभ ही"]},
        "seesaw": "अकल्याणम् (अशुभ) ⇄ शुभम् (शुभ): दोनों इसी श्लोक में।",
        "chunks": "अकल्याणमपि स्वप्नं दृष्ट्वा तत्रैव यः पुनः | पश्येत्सौम्यं शुभं तस्य शुभमेव फलं भवेत्",
        "sandhi": "अ + ए → ऐ: तत्र + एव → तत्रैव · म् + स्वर: शुभम् + एव → शुभमेव, अकल्याणम् + अपि → अकल्याणमपि।",
    },
    "38": {
        "diagram": {"groups": [
            {"label": "कार्ड ३८ की सूची (छपे क्रम में)",
             "items": ["१ देवान् = देवता", "२ द्विजान् = द्विज", "३ गोवृषभान् = गाय-बैल (या बैल)", "४ जीवतः सुहृदः = जीवित मित्र",
                       "५ नृपान् = राजा", "६ साधून् = सज्जन", "७ यशस्विनः = यशस्वी", "८ वह्निम् इद्धम् = जलती अग्नि",
                       "९ स्वच्छान् जलाशयान् = स्वच्छ जलाशय"]}]},
        "chunks": "देवान् द्विजान् गोवृषभान् जीवतः सुहृदोनृपान् | साधून् यशस्विनो वन्हिमिद्धं स्वच्छान् जलाशयान्",
        "sandhi": "अः + घोष व्यंजन → ओ: सुहृदः + नृपान् → सुहृदो नृपान्, यशस्विनः + वह्निम् → यशस्विनो वह्निम् · अ + आ → आ: जल + आशय → जलाशय।",
    },
    "39": {
        "diagram": {"groups": [
            {"label": "कार्ड ३९ की सूची (छपे क्रम में)",
             "items": ["१ कन्याम् = कन्या", "२ कुमारकान् = कुमार", "३ गौरान् = गोरे", "४ शुक्लवस्त्रान् = श्वेत वस्त्र वाले",
                       "५ सुतेजसः = अत्यन्त तेजस्वी", "६ नराशनम् = नरभक्षी", "७ दीप्ततनुम् = दीप्त शरीर वाला",
                       "८ समन्तात् रुधिरोक्षितम् = चारों ओर रक्त से सींचा"]}]},
        "chunks": "कन्यां कुमारकान् गौरान् शुक्लवस्त्रान्सुतेजसः | नराशनं दीप्ततनुं समंताद्रुधिरोक्षितं",
        "sandhi": "त् + घोष व्यंजन → द्: समन्तात् + रुधिर- → समन्ताद्रुधिर- · अ + उ → ओ: रुधिर + उक्षितम् → रुधिरोक्षितम् · अ + अ → आ: नर + अशनम् → नराशनम्।",
    },
}

# ================================================================ IMAGE_SPECS
IMAGE_SPECS = {
    ("28", "chain"): {
        "file": "sh12-padma-kushtha-28.svg",
        "alt": ("Chain of card 28 in printed order: naked, sprinkled with ghee, offering into a flameless fire, lotuses grow on "
                "the chest, then he by kuṣṭha (skin disease)."),
        "type": "chain",
        "title": "कार्ड २८: छपे क्रम में",
        "steps": ["नग्न", "घी से सींचा हुआ", "बिना लौ की अग्नि में आहुति", "छाती पर कमल उगते", "फल: कुष्ठ"],
    },
    ("32", "diagram"): {
        "file": "sh12-chihna-roga-32.svg",
        "alt": ("Table of cards 27 to 32: something on the head (word not printed) with head disease or the head cut off; lotuses "
                "on the chest with kuṣṭha; sneha with caṇḍālas with prameha; dancing with demons and sinking with unmāda; being "
                "matta with apasmāra; eclipse of moon and sun with eye disease; their falling with destruction of the eyes."),
        "type": "table",
        "title": "कार्ड २७-३२: चिह्न और रोग",
        "heads": ["कार्ड: चिह्न", "रोग"],
        "rows": [["२७: सिर पर (छपा नहीं)", "शिरोरोग या सिर कटना"], ["२८: छाती पर कमल", "कुष्ठ"],
                 ["२९: चाण्डाल संग स्नेह", "प्रमेह"], ["२९: राक्षस संग डूबना", "उन्माद"], ["३०: मत्त", "अपस्मार"],
                 ["३१: ग्रहण देखना", "नेत्ररोग"], ["३२: चन्द्र-सूर्य का गिरना", "नेत्र-विनाश"]],
    },
    ("33", "diagram"): {
        "file": "sh12-pancata-33.svg",
        "alt": ("Numbered table of twelve sure items of card 33 in printed order: vomiting after cakes, creepers and birds on "
                "the head, attended by vultures, owls, crows, dragged by a dancing woman, naked with a red garland, mud-smeared "
                "laughing or dancing, sinking in mud, wells or turbid water, swallowed by a fish, rebuked by angry forefathers, "
                "moon, sun, stars perishing, black men with staff and noose; at the end, the sick attain pañcatā (death)."),
        "type": "table",
        "title": "कार्ड ३३: कुछ पक्के चिह्न",
        "heads": ["क्रम", "चिह्न"],
        "rows": [["१", "शष्कुली या पुए खाकर, जागकर उलटी"], ["२", "सिर पर लताएँ, पक्षी"], ["३", "गिद्ध, उल्लू, कौए सेवा करें"],
                 ["४", "नाचती स्त्री खींचे"], ["५", "नग्न, लाल माला"], ["६", "कीचड़ लिपटा हँसे, नाचे"],
                 ["७", "कीचड़, कुएँ, गँदले जल में डूबे"], ["८", "मछली निगले"], ["९", "क्रुद्ध पितर डाँटें"],
                 ["१०", "चन्द्र, सूर्य, तारे नष्ट दिखें"], ["११", "दण्ड-पाश लिए काले पुरुष"], ["अन्त", "रोगी: पंचता (मृत्यु)"]],
    },
    ("34", "diagram"): {
        "file": "sh12-svastha-34.svg",
        "alt": ("Table of cards 33 and 34: the sick (card 33) attain pañcatā, death; the healthy (card 34) a doubt about life."),
        "type": "table",
        "title": "कार्ड ३३-३४: कौन, क्या",
        "heads": ["कौन", "क्या"],
        "rows": [["व्याधिताः = रोगी (३३)", "पंचता = मृत्यु"], ["स्वस्थाः = स्वस्थ (३४)", "जीवित-संदेह"]],
    },
    ("36", "chain"): {
        "file": "sh12-manovaha-36.svg",
        "alt": ("Flowchart of card 36: mind-carrying channels, full of powerful malas, so terrible dreams are seen, by those "
                "whose selves are turned toward destruction."),
        "type": "mermaid",
        "code": ("flowchart TD\n"
                 "  A[\"मनोवह स्रोतस्\"] --> B[\"प्रबल मलों से भरे\"]\n"
                 "  B --> C[\"दारुण स्वप्न दिखते\"]\n"
                 "  C --> D[\"किनको: विनाश-उन्मुख\"]\n"),
    },
    ("37", "chain"): {
        "file": "sh12-shubha-phala-37.svg",
        "alt": ("Chain of card 37: having seen even an inauspicious dream, right there again, should see a gentle auspicious one, "
                "the result is auspicious indeed."),
        "type": "chain",
        "title": "कार्ड ३७: अशुभ के बाद शुभ",
        "steps": ["अशुभ स्वप्न देखकर भी", "वहीं फिर", "सौम्य, शुभ देखे", "फल: शुभ ही"],
    },
    ("38", "diagram"): {
        "file": "sh12-deva-dvija-38.svg",
        "alt": ("Numbered table of card 38 in printed order: gods, twice-born, cows and bulls (or bulls), living friends, kings, "
                "good men, famous ones, a kindled fire, very clear water-bodies."),
        "type": "table",
        "title": "कार्ड ३८ की सूची",
        "heads": ["क्रम", "शब्द = अर्थ"],
        "rows": [["१", "देवान् = देवता"], ["२", "द्विजान् = द्विज"], ["३", "गोवृषभान् = गाय-बैल (या बैल)"], ["४", "जीवतः सुहृदः = जीवित मित्र"],
                 ["५", "नृपान् = राजा"], ["६", "साधून् = सज्जन"], ["७", "यशस्विनः = यशस्वी"], ["८", "वह्निम् इद्धम् = जलती अग्नि"],
                 ["९", "स्वच्छान् जलाशयान् = स्वच्छ जलाशय"]],
    },
    ("39", "diagram"): {
        "file": "sh12-kanya-39.svg",
        "alt": ("Numbered table of card 39 in printed order: a maiden, boys, fair ones, white-clothed ones, very radiant ones, "
                "a man-eating one, a blazing-bodied one, sprinkled with blood all around."),
        "type": "table",
        "title": "कार्ड ३९ की सूची",
        "heads": ["क्रम", "शब्द = अर्थ"],
        "rows": [["१", "कन्याम् = कन्या"], ["२", "कुमारकान् = कुमार"], ["३", "गौरान् = गोरे"], ["४", "शुक्लवस्त्रान् = श्वेत वस्त्र वाले"],
                 ["५", "सुतेजसः = अति तेजस्वी"], ["६", "नराशनम् = नरभक्षी"], ["७", "दीप्ततनुम् = दीप्त शरीर वाला"],
                 ["८", "रुधिरोक्षितम् = रक्त-सिक्त"]],
    },
}
