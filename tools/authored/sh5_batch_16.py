from helpers import mcq, match, order, fill, multi, accepts


AUTHORED = {}

# ---------------------------------------------------------------- unit 191
AUTHORED["191"] = {
    "title": "नाभ्यामेका",
    "question": "By unit 191, what number is given for the navel (nābhi)?",
    "rule": ("One (एका, feminine) in the navel (नाभ्याम्, locative singular of नाभि). Printed as one word: "
             "नाभ्याम् + एका → नाभ्यामेका (the final म् simply joins the vowel)."),
    "limits": ("Prose, one printed word; no verb and no counted noun are printed. That peśī (muscles) are counted is carried "
               "from unit 175, where this count begins; the line itself does not name them."),
    "explain_hi": ("यह एक छपे शब्द की गद्य-पंक्ति है: नाभि में एक। "
                   "‘नाभ्याम्’ नाभि (मानक) का सप्तमी एकवचन है, यानी ‘नाभि में’; ‘एका’ स्त्रीलिंग ‘एक’ है। "
                   "गिनी जा रही वस्तु, पेशी, इकाई १७५ से चली आ रही है; यहाँ न वह छपी है, न क्रिया। "
                   "छपाई में दोनों शब्द जुड़े हैं: नाभ्याम् + एका → नाभ्यामेका।"),
    "hook": "नाभि में एक: नाभ्याम् एका।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 191, what number is given for the navel?",
            ("One", "नाभ्यामेका: one in the navel."),
            [("Two", "एका is one, not two."),
             ("Four", "एका is one, not four."),
             ("Six", "एका is one, not six.")],
            "One in the navel.",
            "एका = one; नाभ्याम् = in the navel."),
        match(1, "Match each part of unit 191 to its meaning.",
              [["नाभि", "navel"], ["नाभ्याम्", "in the navel"], ["एका", "one (feminine)"],
               ["नाभ्यामेका", "one in the navel"]],
              "नाभ्याम् + एका = नाभ्यामेका: one in the navel.",
              "नाभि, नाभ्याम्, एका, नाभ्यामेका."),
        fill(2, "In unit 191 'in the navel' is printed as ____ (type it in Devanagari or in English letters, e.g. dharma).",
             accepts("नाभ्याम्", "nābhyām", "nabhyam"),
             "नाभ्याम् = in the navel, the locative singular of the feminine नाभि.",
             "नाभ्याम् is the locative singular of नाभि: a feminine इ-stem can take -याम् for 'in'.",
             "नाभ्याम् + एका → नाभ्यामेका."),
        mcq("discriminate", 3, "Which split of नाभ्यामेका in unit 191 is right?",
            ("नाभ्याम् + एका", "The final म् of नाभ्याम् joins the vowel of एका in writing."),
            [("नाभ्या + मेका", "मेका is not a word; the number is एका (one)."),
             ("नाभ्याम + एका", "अ + ए would give ऐ (नाभ्यामैका), not मे."),
             ("नाभि + आमेका", "आमेका is not a word; the words are नाभ्याम् and एका.")],
            "नाभ्याम् (in the navel) + एका (one): म् + ए is written मे.",
            "Final म् before a vowel joins it in writing."),
        mcq("apply", 4, "In unit 191, what does the ending -याम् of नाभ्याम् show?",
            ("In: the locative singular", "The data: नाभ्याम् is f. loc. sg., 'in the navel'."),
            [("By: the instrumental singular", "The instrumental singular of नाभि is नाभ्या, not नाभ्याम्."),
             ("Of: the genitive plural", "The genitive plural of नाभि is नाभीनाम्, not नाभ्याम्."),
             ("To: the dative singular", "The dative singular of नाभि is नाभ्यै or नाभये, not नाभ्याम्.")],
            "नाभ्याम् = in the navel (locative singular).",
            "Feminine इ-stem + -याम् = locative singular, 'in'."),
        mcq("transfer", 5, "By the pattern of नाभ्याम् (in the navel, from नाभि), how is in the intellect said from the feminine बुद्धि?",
            ("बुद्ध्याम्", "A feminine इ-stem can take -याम् for 'in', as नाभि → नाभ्याम्."),
            [("बुद्ध्या", "बुद्ध्या is the instrumental, 'by the intellect'."),
             ("बुद्धेः", "बुद्धेः is the genitive or ablative, 'of' or 'from the intellect'."),
             ("बुद्धिम्", "बुद्धिम् is the accusative, not 'in the intellect'.")],
            "बुद्ध्याम् = in the intellect, like नाभ्याम् = in the navel (बुद्धौ is the other valid locative).",
            "Feminine इ-stem: locative singular -याम् (or -औ).",
            teaches="नाभ्याम् is the locative singular of the feminine नाभि: -याम् means 'in'."),
    ],
}

# ---------------------------------------------------------------- unit 192
AUTHORED["192"] = {
    "title": "द्वे हृदि आमाशयेच",
    "question": "By unit 192, which places share the number two?",
    "rule": ("Two (द्वे) in the heart (हृदि, standard) and in the āmāśaya (probably the stomach): both places stand in the "
             "locative singular, linked by च (and)."),
    "limits": ("Prose; no verb and no counted noun are printed (peśī carried from unit 175). Whether the two are for each place "
               "or in all is not stated: questions only ask that it is left open. Āmāśaya = stomach is probable only. "
               "Printed आमाशयेच = आमाशये च."),
    "explain_hi": ("यह गद्य-पंक्ति कहती है: दो, हृदय में और आमाशय में। "
                   "‘हृदि’ हृद् (हृदय, मानक) का सप्तमी एकवचन है; ‘आमाशये’ आमाशय (सम्भवतः जठर) का सप्तमी एकवचन। "
                   "दो पेशियाँ हर स्थान में हैं या दोनों में मिलाकर, यह पंक्ति नहीं बताती। "
                   "छपाई में ‘आमाशयेच’ जुड़ा है, यानी आमाशये च। "
                   "गिनी गई वस्तु (पेशी) इकाई १७५ से चली आ रही है।"),
    "hook": "हृदय और आमाशय: दो।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 192, what number is given for the heart and the āmāśaya?",
            ("Two", "द्वे हृदि आमाशये च: two in the heart and the āmāśaya."),
            [("Six", "द्वे is two, not six."),
             ("Ten", "द्वे is two, not ten."),
             ("Five", "द्वे is two, not five.")],
            "Two in the heart and the āmāśaya.",
            "द्वे = two."),
        order(1, "Put the words of unit 192 in the line's order.",
              ["द्वे", "हृदि", "आमाशये", "च"],
              "Two, in the heart and in the āmāśaya.",
              "द्वे → हृदि → आमाशये → च."),
        match(2, "Match each word of unit 192 to its meaning.",
              [["द्वे", "two"], ["हृद्", "heart"], ["हृदि", "in the heart"], ["आमाशय", "stomach (probable)"],
               ["च", "and"]],
              "Two in the heart and in the āmāśaya (probably the stomach).",
              "द्वे, हृद्, हृदि, आमाशय, च.", role="extend",
              teaches="हृदि is the locative singular of हृद् (heart): -इ on a consonant stem means 'in'."),
        mcq("discriminate", 3, "What does unit 192 leave open about its 'two'?",
            ("Whether two are in each place or in all", "The note: for each site or in all is not stated."),
            [("Whether the number printed is two", "The number is printed: द्वे, two."),
             ("Whether the heart is one of the places", "The heart is printed: हृदि, in the heart."),
             ("Whether the word च joins the places", "च is printed, in आमाशयेच = आमाशये च.")],
            "The number and the places are printed; per place or in all is not.",
            "द्वे हृदि आमाशये च: per place or in all is not said."),
        multi("apply", 4, "Which statements fit unit 192?",
              [("It names the heart (हृदि)", "Right: हृदि = in the heart."),
               ("It gives four in the āmāśaya", "The line gives two (द्वे), not four."),
               ("Its printed आमाशयेच is two words", "Right: आमाशये च, run together in print."),
               ("It prints the counted noun peśī", "No counted noun is printed; peśī is carried from unit 175.")],
              [0, 2],
              "The heart is named, and आमाशयेच is आमाशये च.",
              "द्वे हृदि आमाशये च."),
        mcq("transfer", 5, "By the pattern of हृदि (in the heart, from हृद्), how is in speech said from वाच्?",
            ("वाचि", "A consonant stem takes -इ for 'in', as हृद् → हृदि."),
            [("वाचा", "वाचा is the instrumental, 'by speech'."),
             ("वाचः", "वाचः is the genitive or ablative singular (or a plural), not 'in speech'."),
             ("वाचम्", "वाचम् is the accusative, not 'in speech'.")],
            "वाचि = in speech, like हृदि = in the heart.",
            "Consonant stem + -इ = locative singular, 'in'.",
            teaches="हृदि is the locative singular of हृद्: -इ on a consonant stem means 'in'."),
    ],
}

# ---------------------------------------------------------------- unit 193
AUTHORED["193"] = {
    "title": "षट् यकृत्प्लीहोंदुकेषु",
    "question": "By unit 193, what number is given for the liver, the spleen and the uṇḍuka?",
    "rule": ("Six (षट्) in the liver (यकृत्, standard), the spleen (प्लीहा, standard) and the uṇḍuka (probably the caecum): "
             "one dvandva compound in the locative plural (-एषु); प्लीह + उण्डुक → प्लीहोण्डुक (अ + उ → ओ)."),
    "limits": ("Prose; no verb or counted noun (peśī carried from unit 175). The print has ंद where the standard word has ण्ड "
               "(उण्डुक): no question on that spelling. Uṇḍuka = caecum is probable only. How the six are shared among the "
               "three places is not stated."),
    "explain_hi": ("यह गद्य-पंक्ति कहती है: छह, यकृत् (जिगर), प्लीहा (तिल्ली) और उण्डुक (सम्भवतः अन्धान्त्र) में। "
                   "तीनों स्थान एक द्वन्द्व समास में हैं, जिसका अन्त सप्तमी बहुवचन ‘-एषु’ (में) है। "
                   "प्लीह + उण्डुक में अ + उ → ओ हुआ है: प्लीहोण्डुक। "
                   "छपाई में ‘ण्ड’ की जगह ‘ंद’ है; मानक शब्द उण्डुक है। "
                   "छह पेशियाँ तीनों में कैसे बँटी हैं, यह पंक्ति नहीं बताती।"),
    "hook": "जिगर, तिल्ली, उण्डुक: मिलाकर छह।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 193, what number is given for the liver, spleen and uṇḍuka?",
            ("Six", "षट् यकृत्प्लीहोण्डुकेषु: six in the liver, spleen and uṇḍuka."),
            [("Two", "षट् is six, not two."),
             ("Ten", "षट् is six, not ten."),
             ("Three", "षट् is six, not three.")],
            "Six in the three places.",
            "षट् = six."),
        order(1, "Put the places of unit 193 in the line's order.",
              ["liver (यकृत्)", "spleen (प्लीहा)", "uṇḍuka (probably caecum)"],
              "Liver, spleen, uṇḍuka: यकृत्-प्लीह-उण्डुक.",
              "यकृत् → प्लीहा → उण्डुक."),
        match(2, "Match each sure word of unit 193 to its meaning.",
              [["षट्", "six"], ["यकृत्", "liver"], ["प्लीहा", "spleen"], ["-एषु", "in (locative plural)"]],
              "Six in the liver, the spleen and the uṇḍuka.",
              "षट्, यकृत्, प्लीहा, -एषु.", role="extend",
              teaches="-एषु at the end of a dvandva puts all its members in the locative plural: 'in the liver, spleen and uṇḍuka'."),
        mcq("discriminate", 3, "In the printed प्लीहों... of unit 193, which two vowels joined to give the ओ?",
            ("अ + उ", "प्लीह + उण्डुक: अ + उ → ओ."),
            [("अ + इ", "अ + इ gives ए, not ओ."),
             ("अ + ओ", "अ + ओ gives औ, not ओ."),
             ("इ + उ", "इ + उ gives यु, not ओ.")],
            "प्लीह + उण्डुक → प्लीहोण्डुक: अ + उ → ओ.",
            "अ + उ → ओ."),
        mcq("apply", 4, "Why does the compound of unit 193 end in the plural -एषु?",
            ("It joins three places in one dvandva", "A dvandva of three or more members takes the plural."),
            [("It is a genitive ending, 'of the liver'", "-एषु is the locative plural; it means 'in'."),
             ("It joins two places, so it is dual", "Three places are named, and -एषु is plural, not dual."),
             ("It agrees with the number षट् as an adjective", "The data reads -एषु as the locative of the dvandva itself.")],
            "Liver, spleen and uṇḍuka: three members, so the locative plural -एषु.",
            "Dvandva of three or more → plural ending."),
        mcq("transfer", 5, "By the join in प्लीह + उण्डुक, how is सूर्य + उदयः (sunrise) written in a new example?",
            ("सूर्योदयः", "अ + उ → ओ, as प्लीह + उण्डुक → प्लीहोण्डुक."),
            [("सूर्यौदयः", "औ comes from अ + ओ or अ + औ, not from अ + उ."),
             ("सूर्युदयः", "अ + उ does not drop the अ; the two merge as ओ."),
             ("सूर्यवुदयः", "अव् comes from ओ before a vowel, not from अ + उ.")],
            "सूर्य + उदयः = सूर्योदयः, like प्लीह + उण्डुक = प्लीहोण्डुक.",
            "अ + उ → ओ.",
            teaches="Short अ before उ merges into ओ: प्लीह + उण्डुक → प्लीहोण्डुक."),
    ],
}

# ---------------------------------------------------------------- unit 194
AUTHORED["194"] = {
    "title": "पृष्ठे पंचोर्ध्वसनिविष्टाः",
    "question": "By unit 194, what number is given for the back, and how are they set?",
    "rule": ("Five (पञ्च) in the back (पृष्ठे), set upward (ऊर्ध्व-सन्निविष्टाः). पञ्च + ऊर्ध्व → पञ्चोर्ध्व "
             "(अ + ऊ → ओ)."),
    "limits": ("Prose; no verb; the counted noun is carried (peśī, unit 175). The print has सनिविष्टाः without the doubled न् "
               "(सन्निविष्टाः, as in unit 181): no question on that form. ऊर्ध्व may mean 'upward' (running up) or 'above': "
               "no question on which."),
    "explain_hi": ("यह गद्य-पंक्ति कहती है: पीठ में पाँच, ऊपर की ओर स्थित। "
                   "‘पृष्ठे’ पृष्ठ (पीठ) का सप्तमी एकवचन है। "
                   "पञ्च + ऊर्ध्व में अ + ऊ → ओ हुआ है: पञ्चोर्ध्व। "
                   "छपा ‘सनिविष्टाः’ सम्भवतः ‘सन्निविष्टाः’ है (सम्-नि-विष्ट, दोहरा न्); इकाई १८१ में यही शब्द ठीक छपा है। "
                   "‘ऊर्ध्व’ का अर्थ ‘ऊपर की ओर जाती’ भी हो सकता है और ‘ऊपर स्थित’ भी।"),
    "hook": "पीठ में पाँच, ऊपर की ओर।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 194, what number is given for the back?",
            ("Five", "पृष्ठे पञ्च: five in the back."),
            [("Ten", "पञ्च is five, not ten."),
             ("Three", "पञ्च is five, not three."),
             ("Eight", "पञ्च is five, not eight.")],
            "Five in the back.",
            "पञ्च = five; पृष्ठे = in the back."),
        match(1, "Match each sure part of unit 194 to its meaning.",
              [["पृष्ठ", "back"], ["पृष्ठे", "in the back"], ["पञ्च", "five"]],
              "पृष्ठे पञ्च: five in the back.",
              "पृष्ठ, पृष्ठे, पञ्च."),
        fill(2, "In unit 194 the number 'five' is ____ (type it in Devanagari or in English letters, e.g. dharma).",
             accepts("पञ्च", "pañca", "पंच", "panca", "pancha"),
             "पञ्च = five (printed पंच); five in the back.",
             "पञ्च = five; before ऊर्ध्व it joins as पञ्चोर्ध्व.",
             "पृष्ठे पञ्च."),
        mcq("discriminate", 3, "Which split of पंचोर्ध्व... in unit 194 is right?",
            ("पञ्च + ऊर्ध्व", "अ + ऊ → ओ: पञ्च + ऊर्ध्व → पञ्चोर्ध्व."),
            [("पञ्च + ओर्ध्व", "अ + ओ would give औ (पञ्चौर्ध्व), not ओ."),
             ("पञ्चो + ऊर्ध्व", "पञ्चो is not a word; the number is पञ्च."),
             ("पञ्चम् + ऊर्ध्व", "म् before a vowel would give पञ्चमूर्ध्व, not पञ्चोर्ध्व.")],
            "पञ्च (five) + ऊर्ध्व (upward): अ + ऊ → ओ.",
            "अ + ऊ → ओ."),
        multi("apply", 4, "Which statements fit unit 194?",
              [("It gives five in the back", "Right: पृष्ठे पञ्च."),
               ("It prints the counted noun peśī", "No counted noun is printed; peśī is carried from unit 175."),
               ("It gives ten in the back", "The line gives five (पञ्च), not ten."),
               ("Its पृष्ठे is a locative, 'in the back'", "Right: the data reads पृष्ठे as loc. sg.")],
              [0, 3],
              "Five in the back; पृष्ठे = in the back.",
              "पृष्ठे पञ्च."),
        mcq("transfer", 5, "By the join in पञ्च + ऊर्ध्व, how is जल + ऊर्मिः (a wave of water) written in a new example?",
            ("जलोर्मिः", "अ + ऊ → ओ, as पञ्च + ऊर्ध्व → पञ्चोर्ध्व."),
            [("जलौर्मिः", "औ comes from अ + ओ or अ + औ, not from अ + ऊ."),
             ("जलूर्मिः", "अ + ऊ does not drop the अ; the two merge as ओ."),
             ("जलवूर्मिः", "अव् comes from ओ before a vowel, not from अ + ऊ.")],
            "जल + ऊर्मिः = जलोर्मिः, like पञ्च + ऊर्ध्व = पञ्चोर्ध्व.",
            "अ + ऊ → ओ.",
            teaches="Short अ before ऊ merges into ओ: पञ्च + ऊर्ध्व → पञ्चोर्ध्व."),
    ],
}

# ---------------------------------------------------------------- unit 195
AUTHORED["195"] = {
    "title": "दश दीर्घाःपार्श्वयोः",
    "question": "By unit 195, what is given for the two sides (pārśva)?",
    "rule": ("Ten long ones (दश दीर्घाः) in the two sides (पार्श्वयोः, locative dual). दीर्घाः पार्श्वयोः are two words run "
             "together in print; before प the visarga stays."),
    "limits": ("Prose; no verb; the counted noun is carried (peśī, unit 175). The line gives one number for the two sides and "
               "does not divide it: no question on per side."),
    "explain_hi": ("यह गद्य-पंक्ति कहती है: दोनों पार्श्वों (बगलों) में दस लम्बी। "
                   "‘दीर्घाः’ (लम्बी) प्रथमा बहुवचन विशेषण है, जो गिनी गई दस पेशियों का वर्णन करता है। "
                   "‘पार्श्वयोः’ पार्श्व का सप्तमी द्विवचन है: दोनों बगलों में। "
                   "छपाई में ‘दीर्घाःपार्श्वयोः’ जुड़ा है, पर यह बिना सन्धि के दो शब्द हैं; प से पहले विसर्ग बना रहता है। "
                   "दस हर ओर हैं या मिलाकर, यह पंक्ति नहीं बताती।"),
    "hook": "दोनों बगलों में दस लम्बी।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 195, what number is given for the two sides (pārśva)?",
            ("Ten", "दश दीर्घाः पार्श्वयोः: ten long ones in the two sides."),
            [("Five", "दश is ten, not five."),
             ("Six", "दश is ten, not six."),
             ("Four", "दश is ten, not four.")],
            "Ten in the two sides.",
            "दश = ten."),
        order(1, "Put the words of unit 195 in the line's order.",
              ["दश", "दीर्घाः", "पार्श्वयोः"],
              "Ten long ones, in the two sides.",
              "दश → दीर्घाः → पार्श्वयोः."),
        match(2, "Match each word of unit 195 to its meaning.",
              [["दश", "ten"], ["दीर्घ", "long"], ["पार्श्व", "side"], ["पार्श्वयोः", "in the two sides"]],
              "Ten long ones in the two sides.",
              "दश, दीर्घ, पार्श्व, पार्श्वयोः.", role="extend",
              teaches="पार्श्वयोः is a locative dual: -योः on an अ-stem here means 'in the two'."),
        mcq("discriminate", 3, "Which word in unit 195 describes the ten of the sides?",
            ("Long (दीर्घाः)", "दीर्घाः = long; the data: adj. nom. pl."),
            [("Short (ह्रस्वाः)", "The line says दीर्घाः, long, not short."),
             ("Round (वृत्ताः)", "The line says दीर्घाः, long, not round."),
             ("Thin (तनवः)", "The line says दीर्घाः, long, not thin.")],
            "The ten in the sides are called long.",
            "दीर्घ = long."),
        mcq("apply", 4, "In unit 195, what form is दीर्घाः?",
            ("Nominative plural, describing the ten", "The data: adj. nom. pl.; it goes with the ten counted."),
            [("Locative plural, 'in the long ones'", "A locative plural would end in -एषु or -आसु, not -आः."),
             ("Nominative dual, describing two of them", "A dual would end in -औ or -ए, not -आः."),
             ("Genitive singular, 'of the long one'", "दीर्घाः is not a genitive here; the data reads nom. pl.")],
            "दीर्घाः = long (nominative plural), describing the ten.",
            "Adjective agrees with the counted items: nominative plural."),
        mcq("transfer", 5, "By दीर्घाः पार्श्वयोः (visarga kept before प), how are रामः + पठति joined in a new example?",
            ("रामः पठति", "Before प the visarga stays, as in दीर्घाः पार्श्वयोः."),
            [("रामो पठति", "अः → ओ only before a voiced consonant; प is unvoiced."),
             ("रामस्पठति", "Visarga → स् before त or थ, not before प."),
             ("रामर्पठति", "र् comes from the visarga of other vowels before a voiced sound, not from अः before प.")],
            "रामः पठति: the visarga stays before प, as दीर्घाः stays before पार्श्वयोः.",
            "Visarga before प or फ stays.",
            teaches="Before प the visarga does not change: दीर्घाः पार्श्वयोः."),
    ],
}

# ---------------------------------------------------------------- unit 196
AUTHORED["196"] = {
    "title": "दश वक्षसि",
    "question": "By unit 196, what number is given for the chest (vakṣas)?",
    "rule": ("Ten (दश) in the chest (वक्षसि, locative singular of the स्-stem वक्षस्). This closes the run that goes from the "
             "anus (unit 188) to the chest."),
    "limits": ("Prose, two words; no verb and no counted noun are printed (peśī carried from unit 175). The line does not say "
               "per side or in all."),
    "explain_hi": ("यह दो शब्दों की गद्य-पंक्ति है: छाती में दस। "
                   "‘वक्षसि’ वक्षस् (छाती, मानक) का सप्तमी एकवचन है; स्-अन्त शब्दों में ‘में’ के लिए -इ लगता है। "
                   "गिनी गई वस्तु (पेशी) और क्रिया छपी नहीं। "
                   "इकाई १८८ से यहाँ तक गुदा से छाती तक की पेशियाँ गिनी गई हैं।"),
    "hook": "छाती में दस: दश वक्षसि।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 196, what number is given for the chest (vakṣas)?",
            ("Ten", "दश वक्षसि: ten in the chest."),
            [("Five", "दश is ten, not five."),
             ("Four", "दश is ten, not four."),
             ("Six", "दश is ten, not six.")],
            "Ten in the chest.",
            "दश = ten; वक्षसि = in the chest."),
        match(1, "Match each part of unit 196 to its meaning.",
              [["दश", "ten"], ["वक्षस्", "chest"], ["वक्षसि", "in the chest"]],
              "दश वक्षसि = ten in the chest.",
              "दश, वक्षस्, वक्षसि."),
        fill(2, "In unit 196 'in the chest' is ____ (type it in Devanagari or in English letters, e.g. dharma).",
             accepts("वक्षसि", "vakṣasi"),
             "वक्षसि = in the chest, the locative singular of वक्षस्.",
             "वक्षसि is the locative singular of the स्-stem वक्षस्: -इ means 'in'.",
             "दश वक्षसि."),
        mcq("discriminate", 3, "In unit 196, what is the form वक्षसि?",
            ("Locative singular, 'in the chest'", "The data: n. loc. sg. of वक्षस्."),
            [("Nominative singular, 'the chest'", "The nominative singular is वक्षः, not वक्षसि."),
             ("Locative plural, 'in the chests'", "The locative plural is वक्षःसु, not वक्षसि."),
             ("Instrumental singular, 'by the chest'", "The instrumental singular is वक्षसा, not वक्षसि.")],
            "वक्षसि = in the chest.",
            "स्-stem + -इ = locative singular."),
        multi("apply", 4, "Which statements fit unit 196?",
              [("It prints the counted noun peśī", "No counted noun is printed; peśī is carried from unit 175."),
               ("It gives ten in the chest", "Right: दश वक्षसि."),
               ("Its वक्षसि means 'in the chest'", "Right: locative singular of वक्षस्."),
               ("It gives ten on each side of the chest", "The line names no side.")],
              [1, 2],
              "Ten in the chest; वक्षसि = in the chest.",
              "दश वक्षसि."),
        mcq("transfer", 5, "By the pattern of वक्षसि (in the chest, from वक्षस्), how is in the mind said from मनस्?",
            ("मनसि", "An स्-stem takes -इ for 'in', as वक्षस् → वक्षसि."),
            [("मनसा", "मनसा is the instrumental, 'by the mind'."),
             ("मनसः", "मनसः is the genitive or ablative, 'of' or 'from the mind'."),
             ("मनः", "मनः is the nominative or accusative, 'the mind'.")],
            "मनसि = in the mind, like वक्षसि = in the chest.",
            "स्-stem + -इ = locative singular, 'in'.",
            teaches="वक्षसि is the locative singular of वक्षस्: -इ on an स्-stem means 'in'."),
    ],
}

# ---------------------------------------------------------------- unit 197
AUTHORED["197"] = {
    "title": "तिस्रोऽसाक्षकोपरितः",
    "question": "By unit 197, what number opens the line, and which parts of it are sure?",
    "rule": ("Three (तिस्रः, feminine) above (उपरितः) a place printed असाक्षक, read on a conjecture as अंस + अक्षक "
             "(shoulders and collar-bones, probable). तिस्रः before अ becomes तिस्रोऽ (अः + अ → ओ, the अ marked ऽ)."),
    "limits": ("Conjectural place word: printed असाक्षक has no sense; अंसाक्षक is the data's conjecture (anusvāra lost in "
               "print), and akṣaka = collar-bone is probable only. No question on the place. Sure: the number, the join "
               "तिस्रोऽ, and उपरितः (above). Counted noun carried (peśī, unit 175)."),
    "explain_hi": ("यह गद्य-पंक्ति कहती है: तीन, ... के ऊपर। "
                   "‘तिस्रः’ स्त्रीलिंग ‘तीन’ है; अ से पहले अः का ओ होता है और वह अ लुप्त होकर ऽ (अवग्रह) से दिखाया जाता है: तिस्रोऽ। "
                   "स्थान-शब्द छपाई में ‘असाक्षक’ है, जिसका कोई अर्थ नहीं बनता; अनुमानित पाठ ‘अंसाक्षक’ है, यानी कन्धे और अक्षक (सम्भवतः हँसली)। "
                   "‘उपरितः’ का अर्थ है ‘ऊपर’। "
                   "यह इकाई कन्धे से सिर तक की पेशियों की गिनती आरम्भ करती है।"),
    "hook": "तीन, ऊपर: तिस्रः उपरितः (स्थान अनुमानित)।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 197, what number opens the line?",
            ("Three", "तिस्रः = three (feminine)."),
            [("Two", "तिस्रः is three, not two."),
             ("Ten", "तिस्रः is three, not ten."),
             ("Five", "तिस्रः is three, not five.")],
            "The line opens with three.",
            "तिस्रः = three."),
        match(1, "Match each sure part of unit 197 to its meaning.",
              [["तिस्रः", "three (feminine)"], ["उपरितः", "above"], ["ऽ (avagraha)", "marks a dropped अ"]],
              "तिस्रः = three; उपरितः = above; ऽ marks the अ lost after ओ.",
              "तिस्रः, उपरितः, ऽ."),
        mcq("extend", 2, "In unit 197, how did तिस्रः become तिस्रोऽ before अ?",
            ("अः before अ becomes ओ; the अ is marked ऽ", "तिस्रः + अ... → तिस्रोऽ...: अः + अ → ओऽ."),
            [("अः before any vowel becomes ओ, unmarked", "Before vowels other than अ, अः becomes अ; only before अ is it ओऽ."),
             ("The visarga becomes र् before the अ", "र् comes from the visarga of other vowels (इः, उः ...), not from अः."),
             ("The visarga drops and the अ stays as it is", "That happens before vowels other than अ; before अ it is ओऽ.")],
            "तिस्रः + अ → तिस्रोऽ: अः before अ gives ओ, and the अ is shown by ऽ.",
            "अः + अ → ओऽ.",
            teaches="Visarga after अ before अ: अः + अ → ओऽ (avagraha marks the lost अ)."),
        multi("discriminate", 3, "Which parts of unit 197 are sure, not conjectural?",
              [("The place word (read as अंसाक्षक)", "The data: printed असाक्षक has no sense; अंसाक्षक is a conjecture."),
               ("The number three (तिस्रः)", "Right: तिस्रः is printed clearly."),
               ("The collar-bone sense (अक्षक)", "That identity is probable only, and the word itself rests on the conjecture."),
               ("The word above (उपरितः)", "Right: उपरितः is printed; only the place word is conjectural.")],
              [1, 3],
              "Sure: the number and उपरितः; conjectural: the place word and with it akṣaka.",
              "असाक्षक → अंसाक्षक: conjecture; तिस्रः, उपरितः: sure."),
        mcq("apply", 4, "In unit 197, what form is the number तिस्रः?",
            ("Feminine nominative plural", "The data: num. f. nom. pl.; the masculine would be त्रयः."),
            [("Masculine nominative plural", "The masculine nominative plural of three is त्रयः, not तिस्रः."),
             ("Neuter nominative plural", "The neuter nominative plural of three is त्रीणि, not तिस्रः."),
             ("Feminine nominative dual", "Three has no dual; तिस्रः is plural.")],
            "तिस्रः = three, feminine nominative plural.",
            "त्रि: m. त्रयः, n. त्रीणि, f. तिस्रः."),
        mcq("transfer", 5, "By the rule of तिस्रोऽ, how are रामः + अपि joined in a new example?",
            ("रामोऽपि", "अः + अ → ओऽ, as तिस्रः + अ... → तिस्रोऽ..."),
            [("रामापि", "Only आः drops its visarga; अः before अ becomes ओ with ऽ."),
             ("रामरपि", "र् comes from the visarga of other vowels, not from अः."),
             ("राम अपि", "अः becomes अ only before vowels other than अ; before अ it is ओऽ.")],
            "रामः + अपि = रामोऽपि, like तिस्रः + अ... = तिस्रोऽ...",
            "अः + अ → ओऽ.",
            teaches="अः before अ becomes ओ and the अ is marked ऽ: तिस्रः + अ → तिस्रोऽ."),
    ],
}

# ---------------------------------------------------------------- unit 198
AUTHORED["198"] = {
    "title": "दश ग्रीवायां",
    "question": "By unit 198, what number is given for the neck (grīvā)?",
    "rule": ("Ten (दश) in the neck (ग्रीवायाम्, locative singular of the feminine आ-stem ग्रीवा, printed ग्रीवायां)."),
    "limits": ("Prose, two words; no verb and no counted noun are printed (peśī carried from unit 175)."),
    "explain_hi": ("यह दो शब्दों की गद्य-पंक्ति है: गर्दन में दस। "
                   "‘ग्रीवायाम्’ ग्रीवा (गर्दन) का सप्तमी एकवचन है; आ-अन्त स्त्रीलिंग शब्दों में ‘में’ के लिए -आयाम् लगता है। "
                   "छपाई में अन्त का म् अनुस्वार (ं) से लिखा है: ग्रीवायां। "
                   "गिनी गई वस्तु (पेशी) और क्रिया छपी नहीं।"),
    "hook": "गर्दन में दस।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 198, what number is given for the neck?",
            ("Ten", "दश ग्रीवायाम्: ten in the neck."),
            [("Eight", "दश is ten, not eight."),
             ("Four", "दश is ten, not four."),
             ("Six", "दश is ten, not six.")],
            "Ten in the neck.",
            "दश = ten; ग्रीवायाम् = in the neck."),
        match(1, "Match each part of unit 198 to its meaning.",
              [["दश", "ten"], ["ग्रीवा", "neck"], ["ग्रीवायाम्", "in the neck"]],
              "दश ग्रीवायाम् = ten in the neck.",
              "दश, ग्रीवा, ग्रीवायाम्."),
        fill(2, "In unit 198 the word for 'neck' (without the ending) is ____ (type it in Devanagari or in English letters, e.g. dharma).",
             accepts("ग्रीवा", "grīvā", "griva"),
             "ग्रीवा = neck; ग्रीवायाम् = in the neck.",
             "ग्रीवा = neck, a feminine आ-stem.",
             "दश ग्रीवायाम्."),
        mcq("discriminate", 3, "In unit 198, what is the form ग्रीवायाम्?",
            ("Locative singular, 'in the neck'", "The data: f. loc. sg."),
            [("Genitive singular, 'of the neck'", "The genitive singular is ग्रीवायाः, not ग्रीवायाम्."),
             ("Instrumental singular, 'by the neck'", "The instrumental singular is ग्रीवया, not ग्रीवायाम्."),
             ("Accusative singular, 'the neck'", "The accusative singular is ग्रीवाम्, not ग्रीवायाम्.")],
            "ग्रीवायाम् = in the neck.",
            "Feminine आ-stem + -आयाम् = locative singular."),
        multi("apply", 4, "Which statements fit unit 198?",
              [("It gives eight in the neck", "The line gives ten (दश), not eight."),
               ("It gives ten in the neck", "Right: दश ग्रीवायाम्."),
               ("It prints a verb", "No verb is printed."),
               ("Its ग्रीवायाम् is a locative, 'in the neck'", "Right: f. loc. sg.")],
              [1, 3],
              "Ten in the neck; ग्रीवायाम् = in the neck.",
              "दश ग्रीवायाम्."),
        mcq("transfer", 5, "By the pattern of ग्रीवायाम् (in the neck, from ग्रीवा), how is in the hall said from शाला?",
            ("शालायाम्", "A feminine आ-stem takes -आयाम् for 'in', as ग्रीवा → ग्रीवायाम्."),
            [("शालया", "शालया is the instrumental, 'by the hall'."),
             ("शालायाः", "शालायाः is the genitive or ablative, 'of' or 'from the hall'."),
             ("शालाम्", "शालाम् is the accusative, not 'in the hall'.")],
            "शालायाम् = in the hall, like ग्रीवायाम् = in the neck.",
            "Feminine आ-stem + -आयाम् = locative singular.",
            teaches="ग्रीवायाम् is the locative singular of ग्रीवा: -आयाम् on a feminine आ-stem means 'in'."),
    ],
}

# ---------------------------------------------------------------- unit 199
AUTHORED["199"] = {
    "title": "अष्टौ गंडयोः",
    "question": "By unit 199, what number is given for the two cheeks (gaṇḍa)?",
    "rule": ("Eight (अष्टौ) in the two cheeks (गण्डयोः, locative dual of गण्ड). Printed गंड = गण्ड: the anusvāra stands "
             "for ण् before ड."),
    "limits": ("Prose, two words; no verb and no counted noun are printed (peśī carried from unit 175). The line gives one "
               "number for the two cheeks and does not divide it."),
    "explain_hi": ("यह दो शब्दों की गद्य-पंक्ति है: दोनों गालों में आठ। "
                   "‘गण्डयोः’ गण्ड (गाल, मानक) का सप्तमी द्विवचन है: दोनों गालों में। "
                   "छपा ‘गंड’ = गण्ड; ड से पहले अनुस्वार ण् का काम करता है। "
                   "गिनी गई वस्तु (पेशी) और क्रिया छपी नहीं।"),
    "hook": "दोनों गालों में आठ।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 199, what number is given for the two cheeks?",
            ("Eight", "अष्टौ गण्डयोः: eight in the two cheeks."),
            [("Ten", "अष्टौ is eight, not ten."),
             ("Two", "अष्टौ is eight, not two."),
             ("Four", "अष्टौ is eight, not four.")],
            "Eight in the two cheeks.",
            "अष्टौ = eight."),
        match(1, "Match each part of unit 199 to its meaning.",
              [["अष्टौ", "eight"], ["गण्ड", "cheek"], ["गण्डयोः", "in the two cheeks"]],
              "अष्टौ गण्डयोः = eight in the two cheeks.",
              "अष्टौ, गण्ड, गण्डयोः."),
        mcq("extend", 2, "In unit 199, what does the ending -योः of गण्डयोः show?",
            ("Locative dual: in the two cheeks", "The data: m. loc. du."),
            [("Locative plural: in the many cheeks", "The locative plural would be गण्डेषु."),
             ("Nominative dual: the two cheeks", "The nominative dual would be गण्डौ."),
             ("Instrumental plural: by the cheeks", "The instrumental plural would be गण्डैः.")],
            "गण्डयोः = in the two cheeks (locative dual).",
            "अ-stem + -योः = locative dual here.",
            teaches="-योः on an अ-stem is the locative dual: गण्डयोः = in the two cheeks."),
        mcq("discriminate", 3, "In the printed गंड of unit 199, which nasal does the anusvāra stand for?",
            ("ण्, the nasal of the ड class", "Before ड the class nasal is ण्: गंड = गण्ड."),
            [("न्, the nasal of the द class", "न् goes before त थ द ध; before ड it is ण्."),
             ("म्, the nasal of the ब class", "म् goes before प फ ब भ; before ड it is ण्."),
             ("ङ्, the nasal of the ग class", "ङ् goes before क ख ग घ; before ड it is ण्.")],
            "गंड = गण्ड: the anusvāra before ड is read as ण्.",
            "Anusvāra before a stop = that class's nasal."),
        multi("apply", 4, "Which statements fit unit 199?",
              [("It prints the counted noun peśī", "No counted noun is printed; peśī is carried from unit 175."),
               ("It gives ten in the cheeks", "The line gives eight (अष्टौ), not ten."),
               ("It gives eight", "Right: अष्टौ."),
               ("Its गण्डयोः names two cheeks", "Right: locative dual, in the two cheeks.")],
              [2, 3],
              "Eight in the two cheeks.",
              "अष्टौ गण्डयोः."),
        mcq("transfer", 5, "By the pattern of गण्डयोः (in the two cheeks), how is in the two feet said from पाद?",
            ("पादयोः", "An अ-stem takes -योः for the locative dual, as गण्ड → गण्डयोः."),
            [("पादेषु", "-एषु is the locative plural, in three or more."),
             ("पादौ", "पादौ is the nominative or accusative dual, 'the two feet'."),
             ("पादस्य", "पादस्य is the genitive singular, 'of the foot'.")],
            "पादयोः = in the two feet, like गण्डयोः = in the two cheeks.",
            "अ-stem + -योः = locative dual.",
            teaches="गण्डयोः is a locative dual: -योः on an अ-stem means 'in the two'."),
    ],
}

# ---------------------------------------------------------------- unit 200
AUTHORED["200"] = {
    "title": "अष्टौ हन्वोः",
    "question": "By unit 200, what number is given for the two jaws (hanu)?",
    "rule": ("Eight (अष्टौ) in the two jaws (हन्वोः, locative dual of the feminine उ-stem हनु: हनु + ओः → हन्वोः, "
             "उ before ओ becomes व्)."),
    "limits": ("Prose, two words; no verb and no counted noun are printed (peśī carried from unit 175). The line gives one "
               "number for the two jaws and does not divide it."),
    "explain_hi": ("यह दो शब्दों की गद्य-पंक्ति है: दोनों जबड़ों में आठ। "
                   "‘हन्वोः’ हनु (जबड़ा) का सप्तमी द्विवचन है; हनु + ओः में उ का व् हुआ है। "
                   "गिनती इकाई १९९ (गाल) जैसी ही है: वहाँ भी आठ। "
                   "गिनी गई वस्तु (पेशी) और क्रिया छपी नहीं।"),
    "hook": "दोनों जबड़ों में आठ।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 200, what number is given for the two jaws?",
            ("Eight", "अष्टौ हन्वोः: eight in the two jaws."),
            [("Four", "अष्टौ is eight, not four."),
             ("Ten", "अष्टौ is eight, not ten."),
             ("Six", "अष्टौ is eight, not six.")],
            "Eight in the two jaws.",
            "अष्टौ = eight."),
        match(1, "Match each part of unit 200 to its meaning.",
              [["अष्टौ", "eight"], ["हनु", "jaw"], ["हन्वोः", "in the two jaws"]],
              "अष्टौ हन्वोः = eight in the two jaws.",
              "अष्टौ, हनु, हन्वोः."),
        mcq("extend", 2, "How is हन्वोः formed from हनु in unit 200?",
            ("हनु + ओः: उ before ओ becomes व्", "उ before an unlike vowel becomes व्: हनु + ओः → हन्वोः."),
            [("हनु + वोः: वोः is the ending", "The dual ending is -ओः; the व् comes from the उ of हनु."),
             ("हनो + ओः: ओ before ओ becomes व्", "ओ before a vowel becomes अव्, not व्; the stem is हनु."),
             ("हन् + वोः: the stem is हन्", "The stem is हनु (jaw); its उ gives the व्.")],
            "हनु + ओः → हन्वोः: उ + ओ → वो.",
            "उ + unlike vowel → व् + that vowel.",
            teaches="उ before an unlike vowel becomes व्: हनु + ओः → हन्वोः."),
        mcq("discriminate", 3, "Which reading of हन्वोः fits unit 200?",
            ("Locative dual, 'in the two jaws'", "The data: f. loc. du."),
            [("Locative plural, 'in the jaws'", "The locative plural would be हनुषु."),
             ("Nominative dual, 'the two jaws'", "The nominative dual would be हनू."),
             ("Instrumental singular, 'by the jaw'", "The instrumental singular would be हन्वा.")],
            "हन्वोः = in the two jaws.",
            "उ-stem + -ओः (उ → व्) = locative dual here."),
        multi("apply", 4, "Which statements fit unit 200?",
              [("It gives eight in the jaws", "Right: अष्टौ हन्वोः."),
               ("It joins its two words in one printed word", "The two words are printed apart: अष्टौ हन्वोः."),
               ("Its हन्वोः has a व् from the उ of हनु", "Right: हनु + ओः → हन्वोः."),
               ("It prints the counted noun peśī", "No counted noun is printed; peśī is carried from unit 175.")],
              [0, 2],
              "Eight in the jaws; हन्वोः = हनु + ओः.",
              "अष्टौ हन्वोः."),
        mcq("transfer", 5, "By the pattern of हन्वोः (from the feminine हनु), how is in the two cows said from धेनु?",
            ("धेन्वोः", "उ before ओ becomes व्, as हनु + ओः → हन्वोः."),
            [("धेनुषु", "धेनुषु is the locative plural, in three or more."),
             ("धेनू", "धेनू is the nominative dual, 'the two cows'."),
             ("धेनवोः", "अव् comes from ओ before a vowel; the stem ends in उ, which gives व्.")],
            "धेन्वोः = in the two cows, like हन्वोः = in the two jaws.",
            "उ-stem + -ओः → -वोः.",
            teaches="हन्वोः = हनु + ओः: उ before ओ becomes व्."),
    ],
}

# ---------------------------------------------------------------- unit 201
AUTHORED["201"] = {
    "title": "एकैका गलकाकलजिव्हामूर्द्धसु",
    "question": "By unit 201, what number is given for the throat, kākala, tongue and head?",
    "rule": ("One each (एकैका, feminine) in the gala (throat), the kākala (identity disputed), the tongue (जिह्वा) and the "
             "head (मूर्धन्): one dvandva in the locative plural (-सु). एकैका = एक + एका (अ + ए → ऐ)."),
    "limits": ("Prose; counted noun carried (peśī, unit 175). Kākala = uvula or laryngeal prominence is disputed: no question on "
               "what it is. Printed जिव्हा and मूर्द्धसु are spelling variants of जिह्वा and मूर्धसु."),
    "explain_hi": ("यह गद्य-पंक्ति कहती है: एक-एक, गल (गला), काकल, जिह्वा (जीभ) और मूर्धा (सिर) में। "
                   "काकल की पहचान विवादित है: घण्टी (उवुला) या कण्ठमणि। "
                   "‘एकैका’ = एक + एका, अ + ए → ऐ; स्त्रीलिंग है। "
                   "चारों स्थान एक द्वन्द्व समास में हैं, जिसका अन्त सप्तमी बहुवचन ‘-सु’ (में) है। "
                   "छपा ‘जिव्हा’ जिह्वा का और ‘मूर्द्धसु’ मूर्धसु का वर्तनी-भेद है।"),
    "hook": "गला, काकल, जीभ, सिर: एक-एक।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 201, how many are given in each of its places?",
            ("One each", "एकैका: one each."),
            [("Two each", "एकैका is one each, not two each."),
             ("Five each", "एकैका is one each, not five each."),
             ("Four each", "एकैका is one each, not four each.")],
            "One in each of the four places.",
            "एकैका = one each."),
        order(1, "Put the places of unit 201 in the line's order.",
              ["गल (throat)", "काकल (disputed)", "जिव्हा (tongue)", "मूर्द्धसु (head)"],
              "Throat, kākala, tongue, head: गल-काकल-जिह्वा-मूर्धसु.",
              "गल → काकल → जिह्वा → मूर्धन्."),
        match(2, "Match each sure word of unit 201 to its meaning.",
              [["एकैका", "one each"], ["गल", "throat"], ["जिह्वा", "tongue"], ["मूर्धन्", "head"]],
              "One each in the throat, the kākala, the tongue and the head.",
              "एकैका, गल, जिह्वा, मूर्धन्.", role="extend",
              teaches="एकैका = one each: the number one repeated, one for every place named."),
        mcq("discriminate", 3, "Which split of एकैका in unit 201 is right?",
            ("एक + एका", "अ + ए → ऐ: एक + एका → एकैका."),
            [("एकै + का", "एकै and का are not the words; they are एक and एका."),
             ("एके + एका", "ए + ए would give एक एका, not एकैका."),
             ("एकि + एका", "इ + ए would give एक्येका, not एकैका.")],
            "एक + एका = एकैका: अ + ए → ऐ.",
            "अ + ए → ऐ."),
        mcq("apply", 4, "In unit 201, what does the printed जिव्हा stand for?",
            ("The tongue (जिह्वा), spelt व्ह for ह्व", "The data: jivhā is a variant spelling of jihvā."),
            [("The jaw (हनु), in a variant spelling", "जिव्हा is the tongue, not the jaw."),
             ("The palate (तालु), in a variant spelling", "जिव्हा is the tongue, not the palate."),
             ("The lip (ओष्ठ), in a variant spelling", "जिव्हा is the tongue, not the lip.")],
            "जिव्हा = जिह्वा, the tongue.",
            "Printed जिव्हा = जिह्वा (tongue)."),
        mcq("transfer", 5, "By the join in एक + एका, how is अत्र + एव (here indeed) written in a new example?",
            ("अत्रैव", "अ + ए → ऐ, as एक + एका → एकैका."),
            [("अत्रेव", "ए comes from अ + इ; अ + ए gives ऐ."),
             ("अत्रोव", "ओ comes from अ + उ, not from अ + ए."),
             ("अत्रयेव", "य् comes from इ before a vowel; अत्र ends in अ.")],
            "अत्र + एव = अत्रैव, like एक + एका = एकैका.",
            "अ + ए → ऐ.",
            teaches="Short अ before ए joins as ऐ: एक + एका → एकैका."),
    ],
}

# ---------------------------------------------------------------- unit 202
AUTHORED["202"] = {
    "title": "द्वे द्वे तालुललाटयोः",
    "question": "By unit 202, what is given for the palate and the forehead?",
    "rule": ("Two, two (द्वे द्वे), read by the data as a pair in each place, in the palate (तालु) and the forehead "
             "(ललाट): a dvandva of two places in the locative dual (-योः)."),
    "limits": ("Prose; the counted noun is not in the unit (peśī carried from unit 175, probable only). 'A pair in each place' "
               "is the data's reading of the doubled द्वे; no word 'each' is printed. Unit 203 is elliptical after this line."),
    "explain_hi": ("यह गद्य-पंक्ति कहती है: दो-दो, तालु और ललाट (माथा) में। "
                   "दोहराए ‘द्वे द्वे’ को डेटा ‘हर स्थान में एक जोड़ी’ पढ़ता है; ‘प्रत्येक’ जैसा कोई शब्द छपा नहीं। "
                   "‘तालुललाटयोः’ दो स्थानों का द्वन्द्व है, इसलिए सप्तमी द्विवचन (-योः) में है। "
                   "गिनी गई वस्तु, सम्भवतः पेशी, इकाई १७५ से चली आ रही है।"),
    "hook": "तालु में दो, माथे में दो।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 202, which number word is printed twice?",
            ("Two (द्वे)", "द्वे द्वे: two, two."),
            [("Eight (अष्टौ)", "अष्टौ is not in this line; द्वे is printed twice."),
             ("Ten (दश)", "दश is not in this line; द्वे is printed twice."),
             ("Six (षट्)", "षट् is not in this line; द्वे is printed twice.")],
            "द्वे is printed twice: two, two.",
            "द्वे द्वे = two, two."),
        match(1, "Match each part of unit 202 to its meaning.",
              [["द्वे", "two"], ["तालु", "palate"], ["ललाट", "forehead"], ["-योः", "in the two (locative dual)"]],
              "Two, two, in the palate and the forehead.",
              "द्वे, तालु, ललाट, -योः."),
        mcq("extend", 2, "How does the data read the doubled द्वे द्वे of unit 202?",
            ("Two, two: a pair in each place", "The note: 'two, two' (a pair in each place)."),
            [("Four in each place", "Nothing is added up; the reading is a pair in each place."),
             ("Two in all, printed twice by error", "No print error is noted; the doubling is read as a pair in each place."),
             ("Twenty-two in the two places", "द्वे द्वे is not a compound number; it is two, two.")],
            "द्वे द्वे = two, two: a pair in each place, as the data reads it.",
            "Doubled number = that number in each place (data's reading here).",
            teaches="A doubled number (द्वे द्वे) is read as 'two, two', a pair in each place named."),
        mcq("discriminate", 3, "Why does तालुललाटयोः in unit 202 end in the dual -योः?",
            ("It joins two places, palate and forehead", "A dvandva of two members takes the dual."),
            [("It joins three places, so it is dual", "A dvandva of three takes the plural; this one has two members."),
             ("-योः agrees with the number द्वे only", "The data reads -योः as the locative dual of the dvandva."),
             ("-योः is a plural ending in this line", "-योः is a dual ending (locative or genitive), not plural.")],
            "Palate + forehead: two members, so the locative dual -योः.",
            "Dvandva of two → dual ending."),
        multi("apply", 4, "Which statements fit unit 202?",
              [("It names the jaws and the cheeks", "Those are not in this line; it names the palate and forehead."),
               ("It prints the counted noun peśī", "No counted noun is printed; peśī is carried from unit 175."),
               ("It names the palate and the forehead", "Right: तालुललाटयोः."),
               ("Its number word द्वे is printed twice", "Right: द्वे द्वे.")],
              [2, 3],
              "Two, two, in the palate and the forehead.",
              "द्वे द्वे तालुललाटयोः."),
        mcq("transfer", 5, "By the dual of तालुललाटयोः (a two-member dvandva), which nominative form means Rāma and Lakṣmaṇa?",
            ("रामलक्ष्मणौ", "Two members, so the dual: nominative dual -औ."),
            [("रामलक्ष्मणाः", "-आः is the plural, for three or more."),
             ("रामलक्ष्मणः", "-अः is singular; two persons take the dual."),
             ("रामलक्ष्मणयोः", "-योः is the locative or genitive dual, not the nominative.")],
            "रामलक्ष्मणौ = Rāma and Lakṣmaṇa: a two-member dvandva in the dual.",
            "Dvandva of two members → dual.",
            teaches="A dvandva of two members takes a dual ending: तालुललाटयोः."),
    ],
}

# ---------------------------------------------------------------- unit 203
AUTHORED["203"] = {
    "title": "नासौष्ठकर्णेषु च",
    "question": "By unit 203, which places are named?",
    "rule": ("And in the nose (नासा), the lips (ओष्ठ) and the ears (कर्ण): a three-member dvandva in the locative plural "
             "(-एषु); नासा + ओष्ठ → नासौष्ठ (आ + ओ → औ). No number is printed."),
    "limits": ("Prose, elliptical: the line continues unit 202; no numeral, counted noun or verb is printed, and the data "
               "supplies none. No question on a number for these places."),
    "explain_hi": ("यह गद्य-पंक्ति कहती है: और नाक, ओठ और कानों में। "
                   "यह इकाई २०२ की पंक्ति को आगे बढ़ाती है; संख्या और गिनी गई वस्तु वहीं से चली आती है, यहाँ कुछ जोड़ा नहीं गया। "
                   "‘नासौष्ठ’ में नासा + ओष्ठ, आ + ओ → औ हुआ है। "
                   "तीन स्थानों का द्वन्द्व होने से अन्त सप्तमी बहुवचन ‘-एषु’ है। "
                   "यहीं कन्धे से सिर तक की पेशियों की गिनती पूरी होती है।"),
    "hook": "नाक, ओठ, कान: नासौष्ठकर्णेषु।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "Which places does unit 203 name?",
            ("Nose, lips and ears", "नासौष्ठकर्णेषु: in the nose, lips and ears."),
            [("Eyes, brows and teeth", "The line names nose (नासा), lips (ओष्ठ) and ears (कर्ण)."),
             ("Hands, feet and knees", "The line names nose (नासा), lips (ओष्ठ) and ears (कर्ण)."),
             ("Hair, nails and skin", "The line names nose (नासा), lips (ओष्ठ) and ears (कर्ण).")],
            "Nose, lips and ears.",
            "नासा, ओष्ठ, कर्ण."),
        order(1, "Put the parts of unit 203 in the line's order.",
              ["नासा", "ओष्ठ", "कर्णेषु", "च"],
              "In the nose, lips and ears, and.",
              "नासा → ओष्ठ → कर्णेषु → च."),
        match(2, "Match each word of unit 203 to its meaning.",
              [["नासा", "nose"], ["ओष्ठ", "lip"], ["कर्ण", "ear"], ["च", "and"]],
              "And in the nose, the lips and the ears.",
              "नासा, ओष्ठ, कर्ण, च.", role="extend",
              teaches="-एषु at the end of a three-member dvandva puts all three places in the locative plural."),
        mcq("discriminate", 3, "Which split of नासौष्ठ in unit 203 is right?",
            ("नासा + ओष्ठ", "आ + ओ → औ: नासा + ओष्ठ → नासौष्ठ."),
            [("नासौ + ष्ठ", "ष्ठ is not a word; the word is ओष्ठ (lip)."),
             ("नासा + उष्ठ", "आ + उ would give ओ (नासोष्ठ), not औ."),
             ("नासे + ओष्ठ", "ए before a vowel becomes अय्; it does not give औ.")],
            "नासा (nose) + ओष्ठ (lip): आ + ओ → औ.",
            "आ + ओ → औ."),
        multi("apply", 4, "Which of these are printed in unit 203?",
              [("A numeral for these places", "No numeral is printed; the count comes from unit 202."),
               ("The nose, lips and ears", "Right: नासौष्ठकर्णेषु."),
               ("The counted noun peśī", "No counted noun is printed."),
               ("The word च (and)", "Right: च closes the line.")],
              [1, 3],
              "Only the three places and च are printed.",
              "नासौष्ठकर्णेषु च."),
        mcq("transfer", 5, "By the join in नासा + ओष्ठ, how is गङ्गा + ओघः (the Gaṅgā's flood) written in a new example?",
            ("गङ्गौघः", "आ + ओ → औ, as नासा + ओष्ठ → नासौष्ठ."),
            [("गङ्गोघः", "ओ comes from अ/आ + उ, not from आ + ओ."),
             ("गङ्गैघः", "ऐ comes from अ/आ + ए, not from आ + ओ."),
             ("गङ्गावोघः", "आव् comes from औ before a vowel, not from आ + ओ.")],
            "गङ्गा + ओघः = गङ्गौघः, like नासा + ओष्ठ = नासौष्ठ.",
            "आ + ओ → औ.",
            teaches="आ before ओ joins as औ: नासा + ओष्ठ → नासौष्ठ."),
    ],
}


# ===================================================================== NOTES_HI
NOTES_HI = {
    "191": ("गद्य; विश्वास उच्च; कोई पाठ-चिह्न नहीं। लोप: न संज्ञा छपी, न क्रिया; गिनी गई वस्तु (पेशी) इकाई १७५ से चली आ रही है। "
            "सन्धि जाँची: नाभ्याम् + एका → नाभ्यामेका (म् स्वर से जुड़ता है)। नाभ्याम् = नाभि का सप्तमी एकवचन (नाभौ भी मान्य रूप है)।"),
    "192": ("गद्य; विश्वास उच्च; कोई पाठ-चिह्न नहीं। लोप: पेशी इकाई १७५ से। छपा ‘आमाशयेच’ = आमाशये च (जुड़ा छपा)। "
            "दो हर स्थान में हैं या कुल, यह नहीं कहा गया। आमाशय = जठर, सम्भावित। छपे पाठ में ‘हृदि आमाशये’ बिना सन्धि है "
            "(सन्धि होती तो इ + आ → या)।"),
    "193": ("गद्य; विश्वास मध्यम। पाठ-चिह्न (सम्भावित): छपा ‘प्लीहोंदुकेषु’ में ‘ंद’ है, मानक शब्द उण्डुक (ण्ड) है; शब्द-विभाग में सुधारा गया। "
            "इस वर्तनी पर कोई प्रश्न नहीं। उण्डुक = अन्धान्त्र, सम्भावित ही। सन्धि जाँची: प्लीह + उण्डुक → प्लीहोण्डुक (अ + उ → ओ)। "
            "लोप: पेशी इकाई १७५ से।"),
    "194": ("गद्य; विश्वास मध्यम। पाठ-चिह्न (सम्भावित): छपा ‘सनिविष्टाः’ में दोहरा न् नहीं; सम्-नि-विष्ट से ‘सन्निविष्टाः’ बनता है "
            "(इकाई १८१ में ठीक छपा)। इस रूप पर कोई प्रश्न नहीं। ‘ऊर्ध्व’ = ऊपर की ओर या ऊपर: दोनों अर्थ सम्भव। "
            "सन्धि जाँची: पञ्च + ऊर्ध्व → पञ्चोर्ध्व (अ + ऊ → ओ); छपा पंच = पञ्च। लोप: पेशी इकाई १७५ से।"),
    "195": ("गद्य; विश्वास उच्च; कोई पाठ-चिह्न नहीं। छपा ‘दीर्घाःपार्श्वयोः’ दो शब्द हैं, जुड़े छपे (कोई सन्धि नहीं; प से पहले विसर्ग बना रहता है)। "
            "लोप: पेशी इकाई १७५ से। दस हर ओर हैं या कुल, यह नहीं कहा गया।"),
    "196": ("गद्य; विश्वास उच्च; कोई पाठ-चिह्न नहीं। लोप: पेशी इकाई १७५ से; क्रिया नहीं। वक्षसि = वक्षस् (छाती, मानक) का सप्तमी एकवचन।"),
    "197": ("गद्य; विश्वास मध्यम। पाठ-चिह्न (सम्भावित, अनुमान): छपा ‘असाक्षक’ अर्थहीन है; ‘अंसाक्षक’ (कन्धे और हँसलियाँ) अनुमानित पाठ है, "
            "छपाई में अनुस्वार छूटा माना गया। अक्षक = हँसली, सम्भावित (इकाई १६० में दोनों अक्षकों में चार स्नायु गिने गए हैं)। "
            "स्थान-शब्द पर कोई प्रश्न नहीं। सन्धि जाँची: तिस्रः + अ... → तिस्रोऽ... (अः + अ → ओ, अ का लोप ऽ से); "
            "...क + उपरितः → ...कोपरितः (अ + उ → ओ)। लोप: पेशी इकाई १७५ से।"),
    "198": ("गद्य; विश्वास उच्च; कोई पाठ-चिह्न नहीं। छपा ‘ग्रीवायां’ = ग्रीवायाम् (अन्त का म् अनुस्वार से छपा)। लोप: पेशी इकाई १७५ से।"),
    "199": ("गद्य; विश्वास उच्च; कोई पाठ-चिह्न नहीं। छपा ‘गंडयोः’ = गण्डयोः (ड से पहले अनुस्वार = ण्)। गण्ड = गाल, मानक। "
            "लोप: पेशी इकाई १७५ से।"),
    "200": ("गद्य; विश्वास उच्च; कोई पाठ-चिह्न नहीं। हन्वोः = हनु (स्त्रीलिंग) का सप्तमी द्विवचन; हनु + ओः → हन्वोः (उ + ओ → वो)। "
            "लोप: पेशी इकाई १७५ से।"),
    "201": ("गद्य; विश्वास मध्यम; कोई पाठ-चिह्न नहीं। काकल की पहचान विवादित (घण्टी या कण्ठमणि); उस पर कोई प्रश्न नहीं। "
            "छपा ‘जिव्हा’ = जिह्वा (वर्तनी-भेद, इकाई १६६ में भी), ‘मूर्द्धसु’ = मूर्धसु (दोहरा द्)। "
            "सन्धि जाँची: एक + एका → एकैका (अ + ए → ऐ)। लोप: पेशी इकाई १७५ से।"),
    "202": ("गद्य; विश्वास मध्यम; कोई पाठ-चिह्न नहीं। समूह-टिप्पणी: गिनी गई संज्ञा इस इकाई में नहीं; पेशी इकाई १७५ से, सम्भावित ही। "
            "दोहराया ‘द्वे द्वे’ = दो, दो (हर स्थान में एक जोड़ी); ‘प्रत्येक’ जोड़ा नहीं गया। दोनों संख्या-शब्द द्विवचन रूप हैं।"),
    "203": ("गद्य; विश्वास मध्यम; कोई पाठ-चिह्न नहीं। लोप: इकाई २०२ को आगे बढ़ाती है; संख्या और संज्ञा वहीं से, यहाँ कुछ जोड़ा नहीं गया। "
            "‘च’ तीनों स्थानों को जोड़ता है। सन्धि जाँची: नासा + ओष्ठ → नासौष्ठ (आ + ओ → औ)।"),
}


# ===================================================================== AIDS
AIDS = {
    "191": {
        "chunks": "नाभ्यामेका",
        "sandhi": "म् + स्वर: नाभ्याम् + एका → नाभ्यामेका (म् आगे के स्वर से जुड़ता है)।",
        "frame": "स्थान: नाभ्याम् (नाभि में) → संख्या: एका (एक, स्त्रीलिंग) → वस्तु और क्रिया: छपी नहीं।",
    },
    "192": {
        "diagram": {"groups": [
            {"label": "द्वे (दो): हर स्थान में या कुल, अनकहा", "items": ["हृदि: हृदय में", "आमाशये: आमाशय (सम्भवतः जठर) में"]}]},
        "chunks": "द्वे | हृदि | आमाशयेच",
        "frame": "संख्या: द्वे (दो) → स्थान: हृदि, आमाशये → जोड़: च।",
    },
    "193": {
        "diagram": {"groups": [
            {"label": "षट् (छह), तीन स्थानों में मिलाकर", "items": ["यकृत् (जिगर, मानक)", "प्लीहा (तिल्ली, मानक)",
                                                          "उण्डुक (सम्भवतः अन्धान्त्र)"]}]},
        "chunks": "षट् | यकृत्प्लीहोंदुकेषु",
        "sandhi": "अ + उ → ओ: प्लीह + उण्डुक → प्लीहोण्डुक।",
        "letters": "स्थानों के पहले अक्षर क्रम से: य-प्ली-उ (यकृत्, प्लीहा, उण्डुक)। (मेरी याद-पद्धति)",
    },
    "194": {
        "chunks": "पृष्ठे | पंचोर्ध्वसनिविष्टाः",
        "sandhi": "अ + ऊ → ओ: पञ्च + ऊर्ध्व → पञ्चोर्ध्व।",
        "frame": "स्थान: पृष्ठे (पीठ में) → संख्या: पञ्च (पाँच) → कैसी: ऊर्ध्व-सन्निविष्टाः (ऊपर की ओर स्थित)।",
    },
    "195": {
        "chunks": "दश | दीर्घाःपार्श्वयोः",
        "frame": "संख्या: दश (दस) → कैसी: दीर्घाः (लम्बी) → स्थान: पार्श्वयोः (दोनों बगलों में)।",
        "pegs": "बगल लम्बी होती है, इसलिए वहाँ की दस पेशियाँ भी ‘लम्बी’। (मेरी याद-पद्धति, केवल याद की सहायता)",
    },
    "196": {
        "chain": {"steps": ["१९१ नाभि: एक", "१९२ हृदय, आमाशय: दो", "१९३ यकृत्, प्लीहा, उण्डुक: छह",
                            "१९४ पीठ: पाँच", "१९५ दोनों पार्श्व: दस लम्बी", "१९६ वक्ष: दस"]},
        "chunks": "दश | वक्षसि",
        "frame": "संख्या: दश (दस) → स्थान: वक्षसि (छाती में) → वस्तु: छपी नहीं (पेशी, इकाई १७५ से)।",
    },
    "197": {
        "chunks": "तिस्रोऽसाक्षकोपरितः",
        "sandhi": "अः + अ → ओऽ: तिस्रः + अ... → तिस्रोऽ... · अ + उ → ओ: ...क + उपरितः → ...कोपरितः।",
        "frame": "संख्या: तिस्रः (तीन, स्त्रीलिंग) → स्थान: अनुमानित पाठ पर अंस-अक्षक (छपा असाक्षक) → उपरितः (ऊपर)।",
    },
    "198": {
        "chunks": "दश | ग्रीवायां",
        "frame": "संख्या: दश (दस) → स्थान: ग्रीवायाम् (गर्दन में)।",
        "pegs": "गर्दन में दस, जैसे छाती (इकाई १९६) में दस: दस से दस। (मेरी याद-पद्धति)",
    },
    "199": {
        "chunks": "अष्टौ | गंडयोः",
        "frame": "संख्या: अष्टौ (आठ) → स्थान: गण्डयोः (दोनों गालों में)।",
        "anchors": "गाल और जबड़ा पास-पास, दोनों में आठ (इकाई १९९, २००)। (मेरी याद-पद्धति)",
    },
    "200": {
        "chunks": "अष्टौ | हन्वोः",
        "sandhi": "उ + ओ → वो: हनु + ओः → हन्वोः।",
        "frame": "संख्या: अष्टौ (आठ) → स्थान: हन्वोः (दोनों जबड़ों में)।",
    },
    "201": {
        "diagram": {"groups": [
            {"label": "एकैका (एक-एक), क्रम से", "items": ["गल (गला)", "काकल (पहचान विवादित)", "जिह्वा (जीभ; छपा जिव्हा)",
                                                    "मूर्धा (सिर)"]}]},
        "chunks": "एकैका | गलकाकलजिव्हामूर्द्धसु",
        "sandhi": "अ + ए → ऐ: एक + एका → एकैका।",
        "letters": "स्थानों के पहले अक्षर क्रम से: ग-का-जि-मू। (मेरी याद-पद्धति)",
    },
    "202": {
        "diagram": {"groups": [
            {"label": "द्वे द्वे: हर स्थान में एक जोड़ी (डेटा का पाठ)", "items": ["तालु: दो", "ललाट (माथा): दो"]}]},
        "chunks": "द्वे द्वे | तालुललाटयोः",
        "frame": "संख्या: द्वे द्वे (दो, दो) → स्थान: तालु, ललाट → रूप: द्वन्द्व, सप्तमी द्विवचन।",
    },
    "203": {
        "chain": {"steps": ["१९७ अंस-अक्षक के ऊपर (अनुमानित पाठ): तीन", "१९८ ग्रीवा: दस", "१९९ दोनों गाल: आठ",
                            "२०० दोनों हनु: आठ", "२०१ गल, काकल, जिह्वा, सिर: एक-एक", "२०२ तालु, ललाट: दो-दो",
                            "२०३ नासा, ओष्ठ, कर्ण (संख्या २०२ से)"]},
        "chunks": "नासौष्ठकर्णेषु च",
        "sandhi": "आ + ओ → औ: नासा + ओष्ठ → नासौष्ठ।",
    },
}


# ===================================================================== IMAGE_SPECS
IMAGE_SPECS = {
    ("192", "diagram"): {
        "file": "sh5-hrdaya-amashaya-192.svg",
        "alt": ("Table of unit 192: two (dve), in the heart (hṛd, standard) and in the āmāśaya (probably the stomach); whether "
                "two in each place or in all is not stated."),
        "type": "table",
        "title": "इकाई १९२: द्वे (दो)",
        "heads": ["छपा शब्द", "अर्थ"],
        "rows": [["हृदि", "हृदय में"], ["आमाशये", "आमाशय (सम्भवतः जठर) में"], ["द्वे", "हर स्थान में या कुल: अनकहा"]],
    },
    ("193", "diagram"): {
        "file": "sh5-yakrt-pliha-193.svg",
        "alt": ("Table of unit 193: six (ṣaṭ) together in three places, in line order: liver (yakṛt, standard), spleen "
                "(plīhā, standard), uṇḍuka (probably the caecum)."),
        "type": "table",
        "title": "इकाई १९३: षट् (छह), तीन स्थानों में",
        "heads": ["स्थान (क्रम से)", "पहचान"],
        "rows": [["यकृत्", "जिगर (मानक)"], ["प्लीहा", "तिल्ली (मानक)"], ["उण्डुक", "सम्भवतः अन्धान्त्र"]],
    },
    ("196", "chain"): {
        "file": "sh5-peshi-nabhi-vaksha-196.svg",
        "alt": ("Chain of the muscle counts of units 191 to 196 in order: navel one; heart and āmāśaya two; liver, spleen and "
                "uṇḍuka six; back five; two sides ten long; chest ten."),
        "type": "chain",
        "title": "पेशियाँ: नाभि से वक्ष तक",
        "steps": ["१९१ नाभि: एक", "१९२ हृदय, आमाशय: दो", "१९३ यकृत्, प्लीहा, उण्डुक: छह",
                  "१९४ पीठ: पाँच", "१९५ दोनों पार्श्व: दस लम्बी", "१९६ वक्ष: दस"],
    },
    ("201", "diagram"): {
        "file": "sh5-gala-kakala-201.svg",
        "alt": ("Table of unit 201: one each, in line order, in the throat (gala), the kākala (identity disputed), the tongue "
                "(jihvā, printed jivhā) and the head (mūrdhan)."),
        "type": "table",
        "title": "इकाई २०१: एकैका (एक-एक)",
        "heads": ["स्थान (क्रम से)", "अर्थ"],
        "rows": [["गल", "गला"], ["काकल", "पहचान विवादित"], ["जिह्वा (छपा जिव्हा)", "जीभ"], ["मूर्धा", "सिर"]],
    },
    ("202", "diagram"): {
        "file": "sh5-talu-lalata-202.svg",
        "alt": ("Table of unit 202: 'two, two' (dve dve), read by the data as a pair in each place: palate (tālu) two, "
                "forehead (lalāṭa) two."),
        "type": "table",
        "title": "इकाई २०२: द्वे द्वे (दो, दो)",
        "heads": ["स्थान", "संख्या (डेटा का पाठ)"],
        "rows": [["तालु", "दो"], ["ललाट (माथा)", "दो"]],
    },
    ("203", "chain"): {
        "file": "sh5-peshi-ansa-nasa-203.svg",
        "alt": ("Chain of the muscle counts of units 197 to 203 in order: above the shoulders and akṣaka (conjectural reading) "
                "three; neck ten; two cheeks eight; two jaws eight; throat, kākala, tongue, head one each; palate and forehead "
                "two, two; nose, lips, ears (number carried from unit 202)."),
        "type": "chain",
        "title": "पेशियाँ: कन्धे से सिर तक",
        "steps": ["१९७ अंस-अक्षक के ऊपर (अनुमानित पाठ): तीन", "१९८ ग्रीवा: दस", "१९९ दोनों गाल: आठ",
                  "२०० दोनों हनु: आठ", "२०१ गल, काकल, जिह्वा, सिर: एक-एक", "२०२ तालु, ललाट: दो-दो",
                  "२०३ नासा, ओष्ठ, कर्ण (संख्या २०२ से)"],
    },
}
