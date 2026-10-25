from helpers import mcq, match, order, fill, multi, accepts


def T(q, teaches):
    q["teaches"] = teaches
    return q


AUTHORED = {}

# ---------------------------------------------------------------- unit 26
AUTHORED["26"] = {
    "title": "राजीचितः स्रवन्",
    "question": "By card 26, which complaints go with the swelling, and how do fever, diarrhoea and swelling follow one another?",
    "rule": ("Covered with streaks (राजीचितः), oozing (स्रवन्); the patient has vomiting, fever, breathlessness and diarrhoea. "
             "Fever and diarrhoea at the end of the swelling (शोफान्ते), or swelling when those two decline (तयोः क्षये)."),
    "limits": ("Verse, medium confidence. No verb here: the verb (जायन्ते) is in card 27. That the two nominatives describe "
               "card 25's swelling is an inference, and what the streaks are is not stated: no question on either. No outcome here."),
    "explain_hi": ("यह इकाई दो छपी पंक्तियाँ जोड़ती है और सूजन (शोफ) के मारक लक्षणों का वर्णन आगे बढ़ाती है। "
                   "पहली पंक्ति: रेखाओं से ढका, रिसता हुआ; और रोगी को वमन (छर्दि), ज्वर, श्वास (साँस फूलना) और अतिसार (दस्त)। "
                   "दूसरी पंक्ति एक उलटा क्रम बताती है: सूजन के अन्त में ज्वर और अतिसार, या उन दोनों के क्षीण होने पर सूजन। "
                   "क्रिया ‘जायन्ते’ (उत्पन्न होते हैं) डेटा के अनुसार कार्ड २७ में है; दोनों कार्ड सम्भवतः एक वाक्य हैं। "
                   "‘श्वयथुर्वा’ में श्वयथुः + वा की सन्धि है: उ के बाद विसर्ग घोष वर्ण व से पहले र् बनता है।"),
    "hook": "सूजन गई तो ज्वर-अतिसार आए; ज्वर-अतिसार घटे तो सूजन आई।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "In card 26, what does क्षये (in तयोः क्षये) mean?",
            ("When they decline", "क्षय = waning, decline: तयोः क्षये, when those two decline."),
            [("When they spread", "Spreading would be a word like प्रसर; क्षय is a decline."),
             ("When they begin", "A beginning would be आदि or आरम्भ; क्षय is a decline."),
             ("When they return", "A return would be a word like पुनरागम; क्षय is a decline.")],
            "क्षये = in the decline (locative): when those two decline.",
            "क्षय = waning, decline."),
        match(1, "Match each word of card 26 to its meaning.",
              [["राजीचितः", "covered with streaks"], ["छर्दि", "vomiting"], ["श्वास", "breathlessness"],
               ["अतिसार", "diarrhoea"], ["श्वयथुः", "swelling"]],
              "राजीचितः = covered with streaks, छर्दि = vomiting, श्वास = breathlessness, अतिसार = diarrhoea, श्वयथुः = swelling.",
              "राजीचितः, छर्दि, श्वास, अतिसार, श्वयथुः."),
        order(2, "Put the four complaints of the compound in line 1 of card 26 in the printed order.",
              ["छर्दि", "ज्वर", "श्वास", "अतिसार"],
              "छर्दि-ज्वर-श्वास-अतिसारिणम्: vomiting, fever, breathlessness, diarrhoea, in that order.",
              "छर्दि → ज्वर → श्वास → अतिसार.",
              role="extend",
              teaches="One compound joins four complaints; the ending -इन् (अतिसारिणम्) makes it 'the one having' them."),
        mcq("discriminate", 3, "By card 26, when does swelling (श्वयथुः) appear?",
            ("When fever and diarrhoea decline", "श्वयथुर्वा तयोः क्षये: or swelling when those two (fever and diarrhoea) decline."),
            [("When fever and diarrhoea first rise", "The card says swelling comes at their decline (क्षये), not at their rise."),
             ("When the vomiting has quite ended", "Swelling is tied to the decline of fever and diarrhoea, not of vomiting."),
             ("When the breathing becomes easy", "Nothing in card 26 ties the swelling to easier breathing.")],
            "Fever and diarrhoea at the end of the swelling; swelling at the decline of those two.",
            "शोफान्ते ज्वरातिसारौ ⇄ तयोः क्षये श्वयथुः."),
        mcq("apply", 4, "Which split of श्वयथुर्वा in card 26 is right?",
            ("श्वयथुः + वा", "After उ, ः before the voiced व → र्: श्वयथुः + वा → श्वयथुर्वा."),
            [("श्वयथु + र्वा", "र्वा is not a word; the र् comes from the visarga of श्वयथुः."),
             ("श्वयथुर् + आ", "आ is not the word here; the second word is वा (or)."),
             ("श्वयथुः + अवा", "That would print श्वयथुरवा, with रवा; the print has र्वा.")],
            "श्वयथुः (swelling) + वा (or).",
            "Visarga after a vowel other than अ/आ, before a voiced sound → र्."),
        mcq("transfer", 5, "By the pattern of शोफ + अन्ते → शोफान्ते, how is वर्ष + अन्ते (at the end of the year) joined in a new example?",
            ("वर्षान्ते", "अ + अ → आ: वर्ष + अन्ते → वर्षान्ते, like शोफ + अन्ते → शोफान्ते."),
            [("वर्षेन्ते", "ए comes from अ + इ, not from अ + अ."),
             ("वर्षोन्ते", "ओ comes from अ + उ, not from अ + अ."),
             ("वर्षैन्ते", "ऐ comes from अ + ए, not from अ + अ.")],
            "वर्ष + अन्ते = वर्षान्ते, like शोफ + अन्ते = शोफान्ते.",
            "अ + अ → आ.",
            teaches="Short अ + short अ merge into long आ: शोफ + अन्ते → शोफान्ते (printed शोफांते)."),
    ],
}

# ---------------------------------------------------------------- unit 27
AUTHORED["27"] = {
    "title": "दुर्बलस्य विशेषेण",
    "question": "By card 27, for whom do the complaints of card 26 arise for the end, and which new patient is begun?",
    "rule": ("They (the items of card 26) arise especially (विशेषेण) for the end (अन्ताय) of a weak embodied one (दुर्बलस्य "
             "देहिनः). New clause: he whose swelling is in the foot (पादस्थः) and whose two calves (पिण्डिके) ..."),
    "limits": ("Verse, medium confidence. परित्रस्ते is printed; 'slack' (परिस्रस्ते) is a conjecture: no question on the state "
               "of the calves. The stray anusvāra in जायंतेंऽताय is flagged. The यस्य clause continues in card 28. 'End' is of "
               "life only by context."),
    "explain_hi": ("पहली पंक्ति कार्ड २६ के लक्षणों को पूरा करती है: ये विशेष रूप से दुर्बल देहधारी के अन्त के लिए उत्पन्न होते हैं। "
                   "‘दुर्बलस्य’ और ‘देहिनः’ दोनों षष्ठी एकवचन हैं और साथ लिए गए: दुर्बल देही का। "
                   "दूसरी पंक्ति नया रोगी आरम्भ करती है: जिसकी सूजन पैर में स्थित है और जिसकी दोनों पिंडलियाँ (पिण्डिके) अनुमानित पाठ पर ढीली हैं। "
                   "छपा ‘परित्रस्ते’ (डरी हुई) पिंडलियों पर नहीं बैठता; ‘परिस्रस्ते’ (ढीली) अनुमान है, इसलिए उस पर प्रश्न नहीं। "
                   "यह वाक्य कार्ड २८ में पूरा होता है।"),
    "hook": "दुर्बल देही के अन्त के लिए; फिर पैर में सूजन वाला।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "In card 27, what does देहिनः mean?",
            ("Of an embodied one", "देहिन् = one who has a body, a living person; देहिनः is its genitive."),
            [("Of a skilled healer", "A healer would be भिषज् or वैद्य; देहिन् is an embodied one."),
             ("Of a newborn child", "A child would be बाल or शिशु; देहिन् is an embodied one."),
             ("Of a wandering monk", "A monk would be यति or भिक्षु; देहिन् is an embodied one.")],
            "देहिनः = of the embodied one (देह = body + -इन् = having).",
            "देहिन् = embodied being."),
        match(1, "Match each word of card 27 to its meaning.",
              [["दुर्बलस्य", "of the weak one"], ["विशेषेण", "especially"], ["अन्ताय", "for the end"],
               ["पादस्थः", "situated in the foot"], ["पिंडिके", "the two calves"]],
              "दुर्बलस्य = of the weak one, विशेषेण = especially, अन्ताय = for the end, पादस्थः = situated in the foot, पिंडिके = the two calves.",
              "दुर्बलस्य, विशेषेण, अन्ताय, पादस्थः, पिंडिके."),
        order(2, "Put these printed words of card 27 in the printed order.",
              ["दुर्बलस्य", "विशेषेण", "जायंतेंऽताय", "देहिनः", "श्वयथुर्यस्य", "पादस्थः"],
              "Line 1: of the weak, especially, they arise for the end, of the embodied one. Line 2: whose swelling, in the foot.",
              "दुर्बलस्य → विशेषेण → जायंतेंऽताय → देहिनः → श्वयथुर्यस्य → पादस्थः.",
              role="extend",
              teaches="The two genitives दुर्बलस्य ... देहिनः frame line 1; यस्य opens a new relative clause in line 2."),
        mcq("discriminate", 3, "By card 27, for whom do the complaints of card 26 arise, especially, for the end?",
            ("A weak embodied one", "दुर्बलस्य विशेषेण ... देहिनः: especially of a weak embodied one."),
            [("A strong young man", "The card says दुर्बल (weak), the opposite of strong."),
             ("A woman in labour", "The card names a weak embodied one, not a woman in labour."),
             ("A child at the breast", "The card names a weak embodied one, not a nursing child.")],
            "विशेषेण = especially; दुर्बलस्य देहिनः = of a weak embodied one.",
            "दुर्बल = weak; देहिन् = embodied one."),
        mcq("apply", 4, "In card 27, why are दुर्बलस्य and देहिनः read together as 'of a weak embodied one'?",
            ("Both are genitive singular", "दुर्बलस्य and देहिनः are both m. gen. sg.: so they go together."),
            [("Both are nominative plural", "-स्य and -इनः are genitive singular endings, not nominative plural."),
             ("Both are dative singular", "The dative of this card is अन्ताय; -स्य and -इनः are genitive."),
             ("Both are present verbs", "The verb is जायन्ते; दुर्बलस्य and देहिनः are nouns.")],
            "-अस्य (दुर्बलस्य) and -इनः (देहिनः) are genitive singular endings.",
            "Words in the same case, number and gender go together."),
        mcq("transfer", 5, "By the pattern of पादस्थः (situated in the foot), what does वृक्षस्थः mean in a new example?",
            ("Situated in a tree", "-स्थ = standing, situated in: वृक्ष (tree) + स्थः = situated in a tree."),
            [("Cutting down a tree", "Cutting would need a root like छिद्; -स्थ means situated in."),
             ("Far away from a tree", "Far from would need दूर; -स्थ means situated in."),
             ("Shaped much like a tree", "Like would be -वत् or इव; -स्थ means situated in.")],
            "वृक्षस्थः = situated in a tree, like पादस्थः = situated in the foot.",
            "X + -स्थ = situated in X.",
            teaches="The compound ending -स्थ (from √स्था, to stand) means 'situated in': पाद-स्थः = situated in the foot."),
    ],
}

# ---------------------------------------------------------------- unit 28
AUTHORED["28"] = {
    "title": "तं भिषक् परिवर्जयेत्",
    "question": "By card 28, what does the physician do with the patient of cards 27 and 28, and what does line 2 begin?",
    "rule": ("Line 1 ends the यस्य clause of card 27: and whose two thighs (सक्थिनी) sink, him (तम्) the physician (भिषक्) "
             "should avoid (परिवर्जयेत्). Line 2 begins a new sign: face (आननम्) and hands and feet (हस्तपादौ)."),
    "limits": ("Verse, LOW confidence. सीदतः may be a dual verb or a genitive participle; शुष्यतः likewise; विशेषायस्य is flagged "
               "(probably विशेषाद् यस्य); line 2 has no verb (in card 29): no question on any of these parses or on line 2's sense."),
    "explain_hi": ("पहली पंक्ति कार्ड २७ के ‘यस्य’ वाक्य को पूरा करती है: और जिसकी दोनों जाँघें (सक्थिनी) धँसती हैं, उसे वैद्य छोड़ दे (परिवर्जयेत्)। "
                   "‘तम्’ (उसे) पीछे के ‘यस्य’ को उठाता है। "
                   "डेटा ‘सीदतः’ को द्विवचन क्रिया लेता है, पर षष्ठी कृदन्त भी सम्भव है; इसलिए इस पर प्रश्न नहीं। "
                   "दूसरी पंक्ति नया लक्षण शुरू करती है: सूखते हुए जिसके मुख और हाथ-पैर विशेष रूप से ... ; इसकी क्रिया कार्ड २९ में है और अर्थ पक्का नहीं। "
                   "‘चैव’ में च + एव की सन्धि है (अ + ए → ऐ)।"),
    "hook": "पैर में सूजन, पिंडली, जाँघ धँसे: वैद्य छोड़ दे।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "In card 28, what does सक्थिनी mean?",
            ("The two thighs", "सक्थि = thigh; सक्थिनी is its neuter dual: the two thighs."),
            [("The two calves", "The two calves are पिंडिके (card 27); सक्थिनी are the thighs."),
             ("The two hands", "The hands are हस्त (in हस्तपादौ); सक्थिनी are the thighs."),
             ("The two cheeks", "Cheeks would be कपोल; सक्थिनी are the thighs.")],
            "सक्थिनी = the two thighs.",
            "सक्थि = thigh."),
        match(1, "Match each word of card 28 to its meaning.",
              [["सक्थिनी", "the two thighs"], ["भिषक्", "physician"], ["परिवर्जयेत्", "should avoid"],
               ["आननम्", "face"], ["हस्तपादौ", "hands and feet"]],
              "सक्थिनी = two thighs, भिषक् = physician, परिवर्जयेत् = should avoid, आननम् = face, हस्तपादौ = hands and feet.",
              "सक्थिनी, भिषक्, परिवर्जयेत्, आननम्, हस्तपादौ."),
        order(2, "Put the printed words of line 1 of card 28 in the printed order.",
              ["सीदतः", "सक्थिनी", "चैव", "तं", "भिषक्", "परिवर्जयेत्"],
              "सीदतः सक्थिनी चैव तं भिषक् परिवर्जयेत्: the thighs sink, and him the physician should avoid.",
              "सीदतः → सक्थिनी → चैव → तं → भिषक् → परिवर्जयेत्.",
              role="extend",
              teaches="तम् (him) picks up the यस्य (whose) clause begun in card 27: whose ..., him the physician should avoid."),
        mcq("discriminate", 3, "By card 28, who should avoid the patient whose thighs sink?",
            ("The physician", "तं भिषक् परिवर्जयेत्: the physician (भिषक्) should avoid him."),
            [("His own kin", "The card names the physician (भिषक्), not the kin."),
             ("The patient", "The patient is the one avoided (तम्), not the one who avoids."),
             ("The king", "No king is named in card 28; the subject is भिषक्.")],
            "भिषक् (nominative) is the subject; तम् (accusative) is the patient.",
            "भिषक् = physician; परिवर्जयेत् = should avoid."),
        mcq("apply", 4, "Which split of चैव in card 28 is right?",
            ("च + एव", "अ + ए → ऐ: च + एव → चैव (and indeed)."),
            [("च + इव", "अ + इ gives ए: that would print चेव."),
             ("च + ऐव", "ऐव is not a word; the ऐ comes from अ + ए."),
             ("चे + एव", "चे is not a word; the first word is च (and).")],
            "च (and) + एव (indeed): अ + ए → ऐ.",
            "अ + ए → ऐ."),
        mcq("transfer", 5, "By the pattern of च + एव → चैव, how is अद्य + एव (this very day) joined in a new example?",
            ("अद्यैव", "अ + ए → ऐ: अद्य + एव → अद्यैव, like च + एव → चैव."),
            [("अद्येव", "ए comes from अ + इ (अद्य + इव), not from अ + ए."),
             ("अद्यौव", "औ comes from अ + ओ or अ + औ, not from अ + ए."),
             ("अद्याव", "आ comes from अ + अ or अ + आ, not from अ + ए.")],
            "अद्य + एव = अद्यैव, like च + एव = चैव.",
            "अ + ए → ऐ.",
            teaches="अ before ए merges into ऐ: च + एव → चैव."),
    ],
}

# ---------------------------------------------------------------- unit 29
AUTHORED["29"] = {
    "title": "स मासाद्याति पञ्चताम्",
    "question": "By card 29, what outcome closes the sign begun in card 28, and what is said of the one with udara or swelling?",
    "rule": ("Line 1 closes card 28's sign: (they) swell, or swell apart from the body; he goes to pañcatā (पञ्चता, death) "
             "from a month (मासात्). Line 2: whoever has udara or swelling does not see his own penis (मेहनम्)."),
    "limits": ("Verse, medium confidence. मासात् is read 'within a month'; 'after a month' is possible: no question on which. "
               "The link to card 28 is an inference. Line 2 states no outcome or reason. Udara as ascites-type is probable only."),
    "explain_hi": ("पहली पंक्ति कार्ड २८ के लक्षण को पूरा करती है (सम्भवतः): सूजते हैं, या देह से अलग सूजते हैं; वह मास से पञ्चता यानी मृत्यु को पाता है। "
                   "‘पञ्चता’ (पाँच का भाव, पाँच भूतों में लौटना) मृत्यु का सामान्य मुहावरा है। "
                   "‘मासात्’ डेटा में ‘मास के भीतर’ लिया गया; ‘मास के बाद’ भी सम्भव, इसलिए इस पर प्रश्न नहीं। "
                   "दूसरी पंक्ति: जो उदरी (उदर रोग वाला, सम्भवतः जलोदर जैसा) या शोफी (सूजन वाला) है, वह अपना मेहन (लिङ्ग) नहीं देखता; इस इकाई में न फल कहा गया, न कारण। "
                   "‘मासाद्याति’ में मासात् + याति की सन्धि है: घोष य से पहले त् → द्।"),
    "hook": "मास से पञ्चता; उदरी या शोफी अपना मेहन न देखे।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "In card 29, what does पंचतां (पञ्चताम्) stand for?",
            ("Death", "पञ्चता, the state of five (return to the five elements), is the usual idiom for death."),
            [("Cure", "Cure would be a word like आरोग्य; पञ्चता is death."),
             ("Fever", "Fever is ज्वर; पञ्चता is the idiom for death."),
             ("Sleep", "Sleep is निद्रा; पञ्चता is the idiom for death.")],
            "याति पञ्चताम् = goes to the state of five: dies.",
            "पञ्चता = death (idiom)."),
        match(1, "Match each word of card 29 to its meaning.",
              [["पंचतां", "death (the state of five)"], ["याति", "goes, reaches"], ["उदरी", "one with udara (belly disease)"],
               ["शोफी", "one with swelling"], ["मेहनं", "penis"]],
              "पंचतां = death, याति = goes, उदरी = one with udara, शोफी = one with swelling, मेहनं = penis.",
              "पंचतां, याति, उदरी, शोफी, मेहनं."),
        order(2, "Put the printed words of line 2 of card 29 in the printed order.",
              ["उदरी", "यश्च", "शोफी वा", "स्वं", "न पश्यति", "मेहनं"],
              "उदरी यश्च शोफी वा स्वं न पश्यति मेहनं: whoever has udara or swelling does not see his own penis.",
              "उदरी → यश्च → शोफी वा → स्वं → न पश्यति → मेहनं.",
              role="extend",
              teaches="यः (who) ... न पश्यति: one relative clause covers both the उदरी and the शोफी, joined by वा (or)."),
        multi("discriminate", 3, "Which statements fit card 29 as printed?",
              [("Line 2 says why the penis is not seen", "No: the text gives no reason, and the data supplies none."),
               ("Line 2 speaks of one with udara or with swelling", "Right: उदरी ... शोफी वा."),
               ("पञ्चता here is the idiom for death", "Right: याति पञ्चताम्, goes to the state of five."),
               ("Line 2 itself states a death", "No: no outcome is stated in line 2 of this card.")],
              [1, 2],
              "Line 1 ends with पञ्चता (death); line 2 adds a sign of the उदरी or शोफी, with no outcome or reason.",
              "Signs and outcome: only what is printed."),
        mcq("apply", 4, "Which split of मासाद्याति in card 29 is right?",
            ("मासात् + याति", "त् before the voiced य → द्: मासात् + याति → मासाद्याति."),
            [("मासात् + आति", "आति is not a word; and त् + आ would print मासादाति."),
             ("मास + आद्याति", "आद्याति is not a word; the verb is याति (goes)."),
             ("मासम् + अद्याति", "अद्याति is not a word, and मासम् would not give मासा-.")],
            "मासात् (from a month) + याति (goes).",
            "त् before a voiced consonant → द्."),
        mcq("transfer", 5, "By the pattern of मासात् + याति → मासाद्याति, how is गृहात् + धावति (runs from the house) joined in a new example?",
            ("गृहाद्धावति", "त् before the voiced ध → द्: गृहात् + धावति → गृहाद्धावति."),
            [("गृहात्धावति", "त् does not stay voiceless before the voiced ध; it becomes द्."),
             ("गृहान्धावति", "न् is an optional form before a nasal; ध is not a nasal."),
             ("गृहाच्धावति", "च् comes before च, छ or श, not before ध.")],
            "गृहात् + धावति = गृहाद्धावति, like मासात् + याति = मासाद्याति.",
            "त् before a voiced consonant → द्.",
            teaches="A final त् becomes द् before a voiced consonant: मासात् + याति → मासाद्याति."),
    ],
}

# ---------------------------------------------------------------- unit 30
AUTHORED["30"] = {
    "title": "परिधानं न तिष्ठति; वीसर्पः",
    "question": "By card 30, what happens to the garment, and which complaints go with visarpa?",
    "rule": ("Or he whose garment (परिधानम्) does not stay in place (न तिष्ठति). Visarpa (spreading skin inflammation, "
             "erysipelas-type; probable) having cough, discolouration, fever, fainting and breaking pain in the limbs."),
    "limits": ("Verse, medium confidence. 'Because of the raised belly' rests on a conjecture (printed जठरोन्नातत्): no question on "
               "the cause. Visarpa's identification is probable. No outcome here; the verb may be हन्ति in card 32 (not fixed). "
               "The list continues in card 31."),
    "explain_hi": ("पहली पंक्ति: या जिसका परिधान (शरीर पर लपेटा निचला वस्त्र) नहीं टिकता; ‘पेट उभरा होने के कारण’ अनुमानित पाठ पर है (छपा ‘जठरोन्नातत्’ कोई शब्द नहीं), इसलिए कारण पर प्रश्न नहीं। "
                   "दूसरी पंक्ति नया रोग लेती है: विसर्प (सम्भवतः फैलने वाली त्वचा की सूजन), खाँसी (कास), विवर्णता, ज्वर, मूर्छा और अङ्गभङ्ग (अंगों के टूटने की पीड़ा) से युक्त। "
                   "‘-वान्’ (वाला) पूरे समास को विसर्प का विशेषण बनाता है। "
                   "सूची कार्ड ३१ में आगे चलती है; फल यहाँ नहीं, क्रिया सम्भवतः कार्ड ३२ में (तय नहीं)।"),
    "hook": "वस्त्र न टिके; विसर्प के साथ कास, विवर्णता, ज्वर, मूर्छा, अङ्गभङ्ग।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "In card 30, what is परिधानम्?",
            ("A garment worn round the body", "परिधान = the cloth worn round the body (lower cloth)."),
            [("A bed set out for the sick", "A bed would be शय्या; परिधान is a garment."),
             ("A bowl of food for the ill", "Food would be अन्न or आहार; परिधान is a garment."),
             ("A bandage tied over a wound", "A bandage would be बन्ध; परिधान is a garment.")],
            "परिधानम् = garment, lower cloth.",
            "परिधान = garment."),
        order(1, "Put the complaints joined to विसर्पः in card 30 in the printed order.",
              ["कास", "वैवर्ण्य", "ज्वर", "मूर्च्छा", "अंगभंग"],
              "कास-वैवर्ण्य-ज्वर-मूर्च्छा-अंगभंग-वान्: cough, discolouration, fever, fainting, breaking pain in the limbs.",
              "कास → वैवर्ण्य → ज्वर → मूर्च्छा → अंगभंग."),
        match(2, "Match each part of the compound in card 30 to its meaning.",
              [["कास", "cough"], ["वैवर्ण्य", "discolouration"], ["ज्वर", "fever"], ["मूर्च्छा", "fainting"],
               ["अंगभंग", "breaking pain in the limbs"]],
              "कास = cough, वैवर्ण्य = discolouration, ज्वर = fever, मूर्च्छा = fainting, अंगभंग = breaking pain in the limbs.",
              "कास, वैवर्ण्य, ज्वर, मूर्च्छा, अंगभंग.",
              role="extend",
              teaches="वैवर्ण्य is formed from वि-वर्ण (off-colour): the state of being discoloured."),
        mcq("discriminate", 3, "In card 30, which word does the masculine compound ending in -वान् (having) agree with?",
            ("विसर्पः", "-वान् is m. nom. sg., like विसर्पः: visarpa having cough, etc."),
            [("परिधानं", "परिधानम् is neuter; a masculine -वान् cannot agree with it."),
             ("तिष्ठति", "तिष्ठति is a verb; an adjective in -वान् agrees with a noun."),
             ("यस्य", "यस्य is genitive; -वान् is nominative.")],
            "विसर्पः (m. nom. sg.) ... -वान् (m. nom. sg.).",
            "An adjective agrees with its noun in gender, case and number."),
        mcq("apply", 4, "By card 30, what does न तिष्ठति say of the garment?",
            ("It does not stay in place", "परिधानं न तिष्ठति: the garment does not stay (remain) in place."),
            [("It is torn into shreds", "Nothing in card 30 says the garment is torn; it does not stay."),
             ("It is bound too tightly", "Nothing in card 30 says it is tight; it does not stay."),
             ("It is soaked with sweat", "Nothing in card 30 says it is soaked; it does not stay.")],
            "√स्था = stand, stay: न तिष्ठति = does not stay.",
            "तिष्ठति = stays, remains."),
        mcq("transfer", 5, "By the pattern of ...अंगभंगवान् (having breaking pain in the limbs), what does ज्ञानवान् mean in a new example?",
            ("Having knowledge", "-वत् (nom. -वान्) = having: ज्ञान (knowledge) + वान् = having knowledge."),
            [("Lacking knowledge", "Lacking would need अ- or निर्-; -वान् means having."),
             ("Giving knowledge", "Giving would be -द or दाता; -वान् means having."),
             ("Seeking knowledge", "Seeking would be जिज्ञासु; -वान् means having.")],
            "ज्ञानवान् = having knowledge, like ...अंगभंगवान् = having (those complaints).",
            "Noun + -वत् (m. nom. -वान्) = having that noun.",
            teaches="The suffix -वत् (masculine nominative -वान्) means 'having': कास...अंगभंगवान् = having cough ... limb-pain."),
    ],
}

# ---------------------------------------------------------------- unit 31
AUTHORED["31"] = {
    "title": "भ्रमास्यशोफ; कुष्ठं विशीर्यमाणाङ्गम्",
    "question": "By card 31, which further complaints close the visarpa list, and what is said of the kuṣṭha patient?",
    "rule": ("Visarpa's list goes on: giddiness, swelling of the mouth (आस्य), nausea (हृल्लास), bodily exhaustion and diarrhoea. "
             "Kuṣṭha (leprosy; a group of skin diseases; standard): the one whose limbs crumble, with red eyes and a lost voice."),
    "limits": ("Verse, high confidence, two printed lines joined. आस्य may also mean face; 'mouth' is the data's reading. The verb "
               "(हन्ति) is in card 32; no outcome here. No question on what the visarpa list leads to."),
    "explain_hi": ("पहली पंक्ति कार्ड ३० की विसर्प-सूची को आगे बढ़ाती है: भ्रम (चक्कर), मुख की सूजन, हृल्लास (मितली), देह-साद (थकावट) और अतिसार (दस्त) वाला। "
                   "दूसरी पंक्ति कुष्ठ (कोढ़; त्वचा-रोगों का समूह) लेती है: जिसके अंग बिखर रहे हों, आँखें लाल हों और स्वर नष्ट हो। "
                   "‘विशीर्यमाणाङ्गम्’, ‘रक्तनेत्रम्’, ‘हतस्वरम्’ बहुव्रीहि हैं: ‘जिसका ... ऐसा हो’, यानी रोगी का वर्णन। "
                   "क्रिया ‘हन्ति’ (मारता है) कार्ड ३२ में है। "
                   "‘भ्रमास्य’ में भ्रम + आस्य की सन्धि है (अ + आ → आ)।"),
    "hook": "विसर्प: भ्रम, मुख-शोथ, मितली, थकान, दस्त; कुष्ठ: अंग बिखरें, आँख लाल, स्वर गया।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "In card 31, what does हृल्लास mean?",
            ("Nausea", "हृल्लास = nausea."),
            [("Laughter", "Laughter would be हास; हृल्लास is nausea."),
             ("Heartbeat", "A heartbeat would be a word like स्पन्दन; हृल्लास is nausea."),
             ("Hiccup", "Hiccup is हिध्मा or हिक्का; हृल्लास is nausea.")],
            "हृल्लास = nausea.",
            "हृल्लास = nausea."),
        order(1, "Put the complaints of the compound in line 1 of card 31 in the printed order.",
              ["भ्रम", "आस्यशोफ", "हृल्लास", "देहसाद", "अतिसार"],
              "भ्रम-आस्यशोफ-हृल्लास-देहसाद-अतिसार-वान्: giddiness, swelling of the mouth, nausea, bodily exhaustion, diarrhoea.",
              "भ्रम → आस्यशोफ → हृल्लास → देहसाद → अतिसार."),
        match(2, "Match each word of card 31 to its meaning.",
              [["भ्रम", "giddiness"], ["देहसाद", "bodily exhaustion"], ["विशीर्यमाणांग", "whose limbs crumble"],
               ["रक्तनेत्र", "with red eyes"], ["हतस्वर", "whose voice is lost"]],
              "भ्रम = giddiness, देहसाद = exhaustion of the body, विशीर्यमाणांग = whose limbs crumble, रक्तनेत्र = red-eyed, हतस्वर = whose voice is lost.",
              "भ्रम, देहसाद, विशीर्यमाणांग, रक्तनेत्र, हतस्वर.",
              role="extend",
              teaches="रक्तनेत्र, हतस्वर, विशीर्यमाणाङ्ग are bahuvrīhis: 'one whose eyes are red', and so on."),
        mcq("discriminate", 3, "By card 31, which sign is stated of the kuṣṭha patient?",
            ("Red eyes", "रक्तनेत्रम्: with red eyes."),
            [("Yellow nails", "Yellow eyes and nails are said in card 24 (pāṇḍu), not of kuṣṭha."),
             ("Swollen feet", "Swelling in the foot is card 27's patient, not kuṣṭha."),
             ("Hard lump", "A hard lump (aṣṭhīlā) is card 37, not kuṣṭha.")],
            "Kuṣṭha patient: limbs crumbling, red eyes, lost voice.",
            "कुष्ठम् ... रक्तनेत्रम्."),
        mcq("apply", 4, "In card 31, why does रक्तनेत्रम् name a person with red eyes, not the red eyes themselves?",
            ("It is a bahuvrīhi for a person", "रक्त-नेत्र as bahuvrīhi: one whose eyes are red; it describes the patient."),
            [("It is a dvandva of two nouns", "A dvandva would mean 'red and eye'; this names a person."),
             ("It is a verb in the present", "It has no verb ending; -अम् is accusative singular."),
             ("It is a locative of the place", "A locative would end in -ए; this is -अम्.")],
            "रक्त (red) + नेत्र (eye) = रक्तनेत्र, 'whose eyes are red' (bahuvrīhi).",
            "A bahuvrīhi describes something outside itself: 'whose X is Y'."),
        mcq("transfer", 5, "By the pattern of हतस्वरम् (one whose voice is lost), what does नष्टनिद्रः mean in a new example?",
            ("One whose sleep is lost", "नष्ट (lost) + निद्रा (sleep), bahuvrīhi: one whose sleep is lost."),
            [("The sleep that is lost", "निद्रा is feminine; masculine नष्टनिद्रः names a person, not the sleep."),
             ("One who brings on sleep", "Bringing sleep would be निद्राकर; नष्ट means lost."),
             ("One who sleeps too long", "Long sleep would be अतिनिद्र; नष्ट means lost.")],
            "नष्टनिद्रः = one whose sleep is lost, like हतस्वरः = one whose voice is lost.",
            "Bahuvrīhi: participle + noun = 'one whose noun is so'.",
            teaches="A participle + noun can form a bahuvrīhi naming a person: हत-स्वर = one whose voice is lost."),
    ],
}

# ---------------------------------------------------------------- unit 32
AUTHORED["32"] = {
    "title": "मन्दाग्निं जन्तुभिर्जुष्टम्",
    "question": "By card 32, whom does kuṣṭha kill, and how is the vāyu patient described?",
    "rule": ("(Kuṣṭha) kills (हन्ति) one with weak digestive fire, infested by creatures (जन्तु), with thirst and diarrhoea. "
             "Vāyu: one with numb skin, bent, afflicted with tremor, swelling and pain."),
    "limits": ("Verse, medium confidence. Kuṣṭha as subject is taken from card 31. jantu = creatures (worms or vermin is the usual "
               "sense; the text does not specify). Line 2 has no verb; whether घ्नन्ति of card 34 governs it is not fixed: no "
               "question on line 2's verb or outcome."),
    "explain_hi": ("पहली पंक्ति कार्ड ३१ के कुष्ठ का वाक्य पूरा करती है: कुष्ठ मारता है उस रोगी को जिसकी अग्नि मन्द हो, जो जन्तुओं (सम्भवतः कीड़ों) से घिरा हो, और तृष्णा व अतिसार वाला हो। "
                   "दूसरी पंक्ति वायु (शरीर का वात) लेती है: सुन्न त्वचा वाला, झुका हुआ, कम्प, सूजन और पीड़ा से पीड़ित। "
                   "दूसरी पंक्ति में क्रिया नहीं; कार्ड ३४ की ‘घ्नन्ति’ इसे भी लेती है या नहीं, तय नहीं। "
                   "‘जन्तुभिर्जुष्टम्’ में जन्तुभिः + जुष्टम् की सन्धि है: इ के बाद विसर्ग घोष ज से पहले र्।"),
    "hook": "कुष्ठ: मन्द अग्नि, जन्तु, तृष्णा, अतिसार; वायु: सुन्न त्वचा, झुका, कम्प।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "In card 32, what does मंदाग्निं describe?",
            ("Weak digestive fire", "मन्द (weak) + अग्नि (digestive fire): one whose digestive fire is weak."),
            [("A very high fever", "Fever is ज्वर; मन्दाग्नि is weak digestive fire."),
             ("A burning on the skin", "Burning would be दाह; मन्दाग्नि is weak digestive fire."),
             ("A quick, hard pulse", "Pulse is not named; मन्दाग्नि is weak digestive fire.")],
            "मन्दाग्निम् = (one) with weak digestive fire (agni).",
            "मन्द = weak; अग्नि = digestive fire."),
        match(1, "Match each word of card 32 to its meaning.",
              [["मंदाग्निं", "with weak digestive fire"], ["जुष्टं", "infested"], ["सुप्तत्वचं", "with numb skin"],
               ["भुग्नं", "bent"], ["कंप", "tremor"], ["रुजा", "pain"]],
              "मंदाग्निं = weak digestive fire, जुष्टं = infested, सुप्तत्वचं = numb-skinned, भुग्नं = bent, कंप = tremor, रुजा = pain.",
              "मंदाग्निं, जुष्टं, सुप्तत्वचं, भुग्नं, कंप, रुजा."),
        order(2, "Put these printed words of card 32 in the printed order.",
              ["मंदाग्निं", "जंतुभिर्जुष्टं", "हंति", "तृष्णातिसारिणं", "वायुः", "सुप्तत्वचं"],
              "Line 1: weak fire, infested by creatures, kills, with thirst and diarrhoea. Line 2 opens: vāyu, numb skin.",
              "मंदाग्निं → जंतुभिर्जुष्टं → हंति → तृष्णातिसारिणं → वायुः → सुप्तत्वचं.",
              role="extend",
              teaches="The verb हन्ति stands inside line 1; its subject, kuṣṭha, is in card 31."),
        mcq("discriminate", 3, "By card 32, which sign belongs to the vāyu patient of line 2, not to line 1's patient?",
            ("Numb skin", "सुप्तत्वचम्, numb-skinned, is in line 2, with वायुः."),
            [("Thirst", "Thirst (तृष्णा) is line 1's patient, under kuṣṭha."),
             ("Weak fire", "Weak fire (मन्दाग्नि) is line 1's patient."),
             ("Infestation", "Being infested by creatures is line 1's patient.")],
            "Line 1 (kuṣṭha): weak fire, creatures, thirst, diarrhoea. Line 2 (vāyu): numb skin, bent, tremor, swelling, pain.",
            "वायुः opens line 2."),
        mcq("apply", 4, "Which split of जंतुभिर्जुष्टं in card 32 is right?",
            ("जन्तुभिः + जुष्टम्", "After इ, ः before the voiced ज → र्: जन्तुभिः + जुष्टम्."),
            [("जन्तुभिः + उष्टम्", "That would print जन्तुभिरुष्टं; the print has र्जु."),
             ("जन्तु + भिर्जुष्टम्", "भिर्जुष्टम् is not a word; -भिः is the ending of जन्तुभिः."),
             ("जन्तुभि + र्जुष्टम्", "र्जुष्टम् is not a word; the र् comes from the visarga.")],
            "जन्तुभिः (by creatures) + जुष्टम् (infested).",
            "Visarga after a vowel other than अ/आ, before a voiced sound → र्."),
        mcq("transfer", 5, "By the pattern of जन्तुभिः + जुष्टम्, how is मुनिः + गायति (the sage sings) joined in a new example?",
            ("मुनिर्गायति", "After इ, ः before the voiced ग → र्: मुनिः + गायति → मुनिर्गायति."),
            [("मुनि गायति", "After इ the visarga is not dropped before a voiced sound; it gives र्."),
             ("मुनिस्गायति", "स् comes from a visarga before त or थ, not before ग."),
             ("मुनिश्गायति", "श् comes from a visarga before च, छ or श, not before ग.")],
            "मुनिः + गायति = मुनिर्गायति, like जन्तुभिः + जुष्टम् = जन्तुभिर्जुष्टम्.",
            "इः before a voiced sound → इर्.",
            teaches="A visarga after इ (any vowel other than अ/आ) becomes र् before a voiced sound: जन्तुभिर्जुष्टम्."),
    ],
}

# ---------------------------------------------------------------- unit 33
AUTHORED["33"] = {
    "title": "वातस्रं ... ज्वरान्वितं",
    "question": "By card 33, which parts of this damaged list can be read, and what do they say?",
    "rule": ("Damaged prose. Readable: delusion (मोह) and fever (ज्वर-अन्वितम्, accompanied by fever); then contraction (संकोच), "
             "blisters (स्फोट) and putrefaction (कोथ), joined by -वत् (having)."),
    "limits": ("Prose, LOW confidence. वातास्र (probably vātarakta, a gout-type disease) is a conjectural reading of printed "
               "वातस्रं; the middle of line 1 and the start of line 2 are unreadable. No question on the disease's name or on "
               "the unclear stretches; no verb or outcome here."),
    "explain_hi": ("यह इकाई गद्य है और छपाई बहुत क्षतिग्रस्त है। "
                   "छपा ‘वातस्रं’ अनुमानित पाठ पर ‘वातास्र’ है, जो सम्भवतः वातरक्त (गठिया की श्रेणी का रोग) का नाम है; इस पर प्रश्न नहीं। "
                   "पढ़ा जा सकता है: मोह और ज्वर से युक्त (ज्वरान्वितम्); बीच का अंश अस्पष्ट है। "
                   "दूसरी पंक्ति का आरम्भ अस्पष्ट है; अन्त साफ़ है: संकोच (सिकुड़न), स्फोट (फफोले) और कोथ (सड़न) वाला (-वत्)। "
                   "वाक्य सम्भवतः कार्ड ३४ तक चलता है; यहाँ न क्रिया है, न फल।"),
    "hook": "धुंधली छपाई में पक्के: मोह, ज्वर; संकोच, स्फोट, कोथ।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "In card 33, what does अन्वितम् (in ज्वरान्वितं) mean?",
            ("Accompanied by", "अन्वित = joined with, accompanied by: ज्वरान्वितम्, accompanied by fever."),
            [("Freed from", "Freed from would be मुक्त; अन्वित = accompanied by."),
             ("Cured of", "Cured would be a word like शान्त; अन्वित = accompanied by."),
             ("Hidden by", "Hidden would be छन्न; अन्वित = accompanied by.")],
            "ज्वर + अन्वितम् = accompanied by fever.",
            "अन्वित = accompanied by."),
        match(1, "Match each readable word of card 33 to its meaning.",
              [["मोह", "delusion"], ["ज्वर", "fever"], ["संकोच", "contraction"], ["स्फोट", "blister"], ["कोथ", "putrefaction"]],
              "मोह = delusion, ज्वर = fever, संकोच = contraction, स्फोट = blister, कोथ = putrefaction.",
              "मोह, ज्वर, संकोच, स्फोट, कोथ."),
        order(2, "Put these readable parts of card 33 in the printed order.",
              ["मोह", "ज्वरान्वितं", "संकोच", "स्फोट", "कोथवत्"],
              "Line 1: delusion ... accompanied by fever. Line 2 (end): contraction, blisters, having putrefaction.",
              "मोह → ज्वरान्वितं → संकोच → स्फोट → कोथवत्.",
              role="extend",
              teaches="The -वत् at the very end turns the whole list संकोच-स्फोट-कोथ into 'having' them."),
        multi("discriminate", 3, "Which of these stretches of card 33 can be read?",
              [("संकोचस्फोटकोथवत्", "Right: the end of line 2 is a clear list."),
               ("सूर्च्छायमदास्वम", "No: this middle stretch of line 1 is unreadable."),
               ("शिरोपहारुचिश्वारस", "No: this opening stretch of line 2 is unreadable."),
               ("ज्वरान्वितं", "Right: 'accompanied by fever' is clear.")],
              [0, 3],
              "Clear: मोह, ज्वरान्वितम्, संकोच-स्फोट-कोथ-वत्. Unreadable: two stretches, left as 'unclear' in the data.",
              "Learn only the sure parts of a damaged line."),
        mcq("apply", 4, "In कोथवत् of card 33, what does the ending -वत् add, by the data?",
            ("Having", "-वत् here = having: संकोच-स्फोट-कोथ-वत्, having contraction, blisters and putrefaction."),
            [("Without", "Without would need a prefix like निर्-; -वत् here means having."),
             ("Removing", "Removing would need a word like हर; -वत् here means having."),
             ("Causing", "Causing would need a word like कर; -वत् here means having.")],
            "-वत् (possessive) = having.",
            "Noun + -वत् = having it."),
        mcq("transfer", 5, "By the pattern of ज्वरान्वितम् (accompanied by fever), what does भयान्वितः mean in a new example?",
            ("Accompanied by fear", "भय (fear) + अन्वित (accompanied by): accompanied by fear."),
            [("Rid of all fear", "Rid of fear would be निर्भय; अन्वित means accompanied by."),
             ("Causing great fear", "Causing fear would be भयंकर; अन्वित means accompanied by."),
             ("Fearing no one", "That would be a different sense; अन्वित means accompanied by.")],
            "भयान्वितः = accompanied by fear, like ज्वरान्वितम् = accompanied by fever.",
            "X + अन्वित = accompanied by X (अ + अ → आ).",
            teaches="-अन्वित (accompanied by) closes a compound: ज्वर + अन्वितम् → ज्वरान्वितम्."),
    ],
}

# ---------------------------------------------------------------- unit 34
AUTHORED["34"] = {
    "title": "घ्नन्ति सर्वामयाः",
    "question": "By card 34, whom do all diseases kill, and by which complaints?",
    "rule": ("By head disease, distaste for food, breathlessness, meha (urinary disorder, prameha group; probable), loose stool, "
             "thirst and giddiness, all diseases (सर्वामयाः) kill (घ्नन्ति) one whose voice, dhātus, strength and fire are wasted."),
    "limits": ("Prose, medium confidence. Line 2 is a complete clause; whether घ्नन्ति also closes cards 32 and 33 is not "
               "established. 'vidbhed' lacks a final a (flagged); anala as digestive fire and meha as prameha are probable. No "
               "question on these."),
    "explain_hi": ("पहली पंक्ति तृतीया की सूची है: शिरोरोग, अरुचि (भोजन में अरुचि), श्वास, मेह (सम्भवतः प्रमेह), विड्भेद (पतला दस्त), तृषा और भ्रम से। "
                   "दूसरी पंक्ति: सभी रोग (सर्वामयाः) उसे मारते हैं (घ्नन्ति) जिसका स्वर, धातु, बल और अनल (सम्भवतः पाचन अग्नि) क्षीण हो गए हों। "
                   "‘क्षीण’ बहुव्रीहि में चारों पर लगता है। "
                   "यह वाक्य अपने आप में पूरा है; ‘घ्नन्ति’ कार्ड ३२-३३ को भी लेती है या नहीं, तय नहीं (वहाँ कर्ता एकवचन हैं)। "
                   "‘शिरोरोग’ में शिरस् + रोग है: अस् घोष व्यंजन से पहले ओ बनता है।"),
    "hook": "स्वर, धातु, बल, अनल क्षीण: सब रोग मारक।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "In card 34, what does सर्वामयाः mean?",
            ("All diseases", "सर्व (all) + आमय (disease): all diseases."),
            [("All healers", "Healers would be भिषजः; आमय is disease."),
             ("All remedies", "Remedies would be औषधानि; आमय is disease."),
             ("All patients", "Patients would be आतुराः; आमय is disease.")],
            "सर्वामयाः = all diseases (nom. pl.), subject of घ्नन्ति.",
            "आमय = disease."),
        order(1, "Put these complaints of the list in line 1 of card 34 in the printed order.",
              ["शिरोरोग", "अरुचि", "श्वास", "मेह", "तृड्", "भ्रम"],
              "शिरोरोग-अरुचि-श्वास-मेह-विद्भेद्-तृड्-भ्रमैः: head disease, distaste, breathlessness, meha, (loose stool), thirst, giddiness.",
              "शिरोरोग → अरुचि → श्वास → मेह → तृड् → भ्रम."),
        match(2, "Match each part of क्षीणस्वरधातुबलानलं and line 1 of card 34 to its meaning.",
              [["स्वर", "voice"], ["धातु", "body-tissue"], ["बल", "strength"], ["अनल", "fire"], ["अरुचि", "distaste for food"]],
              "स्वर = voice, धातु = body-tissue, बल = strength, अनल = fire (probably the digestive fire), अरुचि = distaste for food.",
              "स्वर, धातु, बल, अनल, अरुचि.",
              role="extend",
              teaches="In the bahuvrīhi क्षीण-स्वर-धातु-बल-अनलम्, क्षीण (wasted) goes with all four nouns."),
        mcq("discriminate", 3, "By card 34, whom do all diseases kill?",
            ("One whose voice and strength are wasted", "क्षीण-स्वर-धातु-बल-अनलम्: voice, tissues, strength and fire wasted."),
            [("One whose voice and strength are rising", "The card says क्षीण (wasted), not rising."),
             ("Only one who has a slight headache", "The card names the wasted one, not a slight headache."),
             ("One whose fire burns very strongly", "The card says the fire (anala) is wasted, not strong.")],
            "घ्नन्ति सर्वामयाः क्षीण-स्वर-धातु-बल-अनलम्.",
            "क्षीण = wasted."),
        mcq("apply", 4, "Which split of शिरोरोग in card 34 is right?",
            ("शिरस् + रोग", "अस् before the voiced र → ओ: शिरस् + रोग → शिरोरोग (head disease)."),
            [("शिरा + रोग", "That would print शिरारोग, with रा; the print has रो."),
             ("शिरो + अरोग", "That would print शिरोऽरोग; and अरोग (healthy) does not fit."),
             ("शिर + उरोग", "उरोग is not a word; the second word is रोग.")],
            "शिरस् (head) + रोग (disease).",
            "अस् (or अः) before a voiced consonant → ओ."),
        mcq("transfer", 5, "By the pattern of शिरस् + रोग → शिरोरोग, how is यशस् + गान (song of fame) joined in a new example?",
            ("यशोगान", "अस् before the voiced ग → ओ: यशस् + गान → यशोगान."),
            [("यशस्गान", "स् does not stay before a voiced consonant after अ; it gives ओ."),
             ("यशर्गान", "र् comes after vowels other than अ/आ; here the vowel is अ."),
             ("यशागान", "आ is not the result; अस् before a voiced consonant gives ओ.")],
            "यशस् + गान = यशोगान, like शिरस् + रोग = शिरोरोग.",
            "अस् before a voiced consonant → ओ.",
            teaches="A final अस् (or अः) becomes ओ before a voiced consonant: शिरस् + रोग → शिरोरोग."),
    ],
}

# ---------------------------------------------------------------- unit 35
AUTHORED["35"] = {
    "title": "वातव्याधिरपस्मारी कुष्ठी",
    "question": "By card 35, which patients should be avoided, and when?",
    "rule": ("One with vātavyādhi, apasmāra (epilepsy), kuṣṭha, (raktī, uncertain), udara, kṣaya, gulma and meha: those, when "
             "wasted (क्षीणान्), one should avoid (वर्जयेत्) even in a slight disorder (विकारेऽल्पेऽपि)."),
    "limits": ("Verse, medium confidence. रत्त्युदरी is flagged: raktī (sense uncertain) is a conjecture: no question on it. Udara "
               "(probably ascites-type), kṣaya (probably tuberculosis) and meha (prameha group) are probable identifications. "
               "The agent of वर्जयेत् is not stated."),
    "explain_hi": ("यह श्लोक रोगियों की सूची देता है: वातव्याधि वाला, अपस्मारी (मिर्गी वाला), कुष्ठी, (अनुमानित पाठ पर रक्ती, अर्थ अनिश्चित), उदरी, क्षयी, गुल्मी (पेट की गाँठ वाला) और मेही। "
                   "इन्हें, जब वे क्षीण हों, थोड़े से विकार में भी छोड़ देना चाहिए (वर्जयेत्)। "
                   "उदर सम्भवतः जलोदर जैसा, क्षय सम्भवतः क्षयरोग (टीबी) और मेह सम्भवतः प्रमेह-समूह है (डेटा: सम्भावित)। "
                   "‘-ई’ में अन्त होने वाले नाम (-इन्) का अर्थ है ‘वह रोग वाला’। "
                   "छोड़ने वाला कौन, छपा नहीं।"),
    "hook": "क्षीण वातव्याधि, अपस्मारी, कुष्ठी, उदरी, क्षयी, गुल्मी, मेही: छोटे विकार में भी वर्ज्य।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "In card 35, what does अल्पे (in विकारेऽल्पेऽपि) mean?",
            ("Slight", "अल्प = small, slight: विकारे अल्पे अपि, even in a slight disorder."),
            [("Severe", "Severe would be तीव्र; अल्प = slight."),
             ("Sudden", "Sudden would be आकस्मिक; अल्प = slight."),
             ("Long", "Long-lasting would be दीर्घ; अल्प = slight.")],
            "अल्पे = in a slight (disorder).",
            "अल्प = slight."),
        order(1, "Put these sure patients of card 35 in the printed order.",
              ["वातव्याधिः", "अपस्मारी", "कुष्ठी", "क्षयी", "गुल्मी", "मेही"],
              "वातव्याधिः, अपस्मारी, कुष्ठी, (रत्त्युदरी), क्षयी, गुल्मी, मेही: the printed order, the flagged token left out.",
              "वातव्याधिः → अपस्मारी → कुष्ठी → क्षयी → गुल्मी → मेही."),
        match(2, "Match each patient of card 35 to his complaint.",
              [["अपस्मारी", "one with epilepsy (apasmāra)"], ["कुष्ठी", "one with kuṣṭha (skin disease)"],
               ["गुल्मी", "one with an abdominal lump (gulma)"], ["मेही", "one with meha (urinary disorder)"],
               ["क्षयी", "one with kṣaya (wasting)"]],
              "अपस्मारी = epilepsy, कुष्ठी = kuṣṭha, गुल्मी = gulma, मेही = meha, क्षयी = kṣaya (wasting).",
              "अपस्मारी, कुष्ठी, गुल्मी, मेही, क्षयी.",
              role="extend",
              teaches="A disease name + -इन् (nom. -ई) means 'one who has it': गुल्म → गुल्मी."),
        mcq("discriminate", 3, "By card 35, when should these patients be avoided even in a slight disorder?",
            ("When they are wasted", "तान् क्षीणान् ... वर्जयेत्: those, when wasted, should be avoided."),
            [("When they are young", "Age is not named; the condition is क्षीण (wasted)."),
             ("When they are rich", "Wealth is not named; the condition is क्षीण (wasted)."),
             ("When they are new", "A new illness is not named; the condition is क्षीण (wasted).")],
            "क्षीणान् = wasted (acc. pl.), with तान्.",
            "क्षीण = wasted."),
        mcq("apply", 4, "Which split of विकारेऽल्पेऽपि in card 35 is right?",
            ("विकारे + अल्पे + अपि", "ए + अ → एऽ (the अ drops, marked ऽ), twice: विकारेऽल्पेऽपि."),
            [("विकार + अल्पे + अपि", "अ + अ would give आ: that would print विकाराल्पे-."),
             ("विकारे + ल्पे + पि", "ल्पे and पि are not words; the ऽ marks a dropped अ."),
             ("विकारे + अल्पे + पि", "पि is not a word; the third word is अपि (even).")],
            "विकारे (in a disorder) + अल्पे (slight) + अपि (even).",
            "ए + अ → एऽ."),
        mcq("transfer", 5, "By the pattern of गुल्मी (one with gulma), what does ज्वरी mean in a new example?",
            ("One who has fever", "ज्वर + -इन् (nom. -ई) = one who has fever."),
            [("Fever as a disease", "The disease itself is ज्वर; -ई names the one who has it."),
             ("One freed from fever", "Freed would need a word like मुक्त; -ई means having."),
             ("A cure for the fever", "A cure would be ज्वरघ्न; -ई means having.")],
            "ज्वरी = one who has fever, like गुल्मी = one who has gulma.",
            "Disease + -इन् (nom. -ई) = one who has it.",
            teaches="The suffix -इन् (masculine nominative -ई) turns a disease into its patient: कुष्ठ → कुष्ठी."),
    ],
}

# ---------------------------------------------------------------- unit 36
AUTHORED["36"] = {
    "title": "बलमांसक्षयस्तीव्रः",
    "question": "By card 36, which signs are named, and how long does the text say the patient lives?",
    "rule": ("Severe loss of strength and flesh (बलमांसक्षयः तीव्रः), increase of disease (रोगवृद्धिः) and loss of appetite "
             "(अरोचकः): the patient in whom these are observed lives three fortnights (त्रीन् पक्षान्)."),
    "limits": ("Prose by the data's type, high confidence; two printed lines joined. The printed पक्षाञ्स (ñ) is a print habit, read "
               "पक्षान् स. The card states only the text's own span; nothing is added."),
    "explain_hi": ("यह इकाई तीन लक्षण गिनाती है: बल और मांस का तीव्र क्षय, रोग की वृद्धि, और अरोचक (भोजन में अरुचि)। "
                   "जिस रोगी (आतुर) में ये दिखाई दें (लक्ष्यन्ते), पाठ के अनुसार वह तीन पक्ष (तीन पखवाड़े) जीवित रहता है। "
                   "‘त्रीन् पक्षान्’ द्वितीया है: समय की अवधि बताने वाली द्वितीया। "
                   "छपा ‘पक्षाञ्स’ छपाई की आदत है, पढ़ें पक्षान् स। "
                   "‘क्षयस्तीव्रः’ में क्षयः + तीव्रः की सन्धि है: त से पहले विसर्ग → स्।"),
    "hook": "बल-मांस घटे, रोग बढ़े, अरुचि: तीन पक्ष।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "In card 36, what does आतुरस्य (in यस्यातुरस्य) mean?",
            ("Of the patient", "आतुर = sick person, patient: यस्य आतुरस्य, of which patient."),
            [("Of the healer", "A healer would be भिषज् or वैद्य; आतुर is the patient."),
             ("Of the envoy", "An envoy would be दूत; आतुर is the patient."),
             ("Of the kinsman", "A kinsman would be बन्धु; आतुर is the patient.")],
            "आतुरस्य = of the patient (m. gen. sg.).",
            "आतुर = patient."),
        match(1, "Match each word of card 36 to its meaning.",
              [["बल", "strength"], ["मांस", "flesh"], ["वृद्धि", "increase"], ["अरोचकः", "loss of appetite"],
               ["लक्ष्यंते", "are observed"]],
              "बल = strength, मांस = flesh, वृद्धि = increase, अरोचकः = loss of appetite, लक्ष्यंते = are observed.",
              "बल, मांस, वृद्धि, अरोचकः, लक्ष्यंते."),
        order(2, "Put the printed words of card 36 in the printed order.",
              ["बलमांसक्षयस्तीव्रो", "रोगवृद्धिररोचकः", "यस्यातुरस्य", "लक्ष्यंते", "त्रीन् पक्षाञ्स", "जीवति"],
              "Signs first (line 1), then: in which patient they are observed, three fortnights he lives (line 2).",
              "बलमांसक्षयस्तीव्रो → रोगवृद्धिररोचकः → यस्यातुरस्य → लक्ष्यंते → त्रीन् पक्षाञ्स → जीवति.",
              role="extend",
              teaches="यस्य आतुरस्य ... सः: the relative clause names the patient, सः picks him up for जीवति."),
        mcq("discriminate", 3, "By card 36, how long does the text say the patient with these signs lives?",
            ("Three fortnights", "त्रीन् पक्षान् स जीवति: he lives three fortnights."),
            [("Three months", "The card says पक्ष (fortnight), not मास (month)."),
             ("Seven days", "No span of days is named; the card says three fortnights."),
             ("One fortnight", "The number is त्रीन् (three), not one.")],
            "त्रीन् (three) पक्षान् (fortnights).",
            "Read the number and the unit as printed."),
        mcq("apply", 4, "Which split of रोगवृद्धिररोचकः in card 36 is right?",
            ("रोगवृद्धिः + अरोचकः", "After इ, ः before a vowel → र्: रोगवृद्धिः + अरोचकः → रोगवृद्धिररोचकः."),
            [("रोगवृद्धिः + रोचकः", "Before र the visarga after इ drops and इ lengthens: that would print -वृद्धी रोचकः."),
             ("रोगवृद्धि + अरोचकः", "Without a visarga, इ + अ gives य: that would print रोगवृद्ध्यरोचकः."),
             ("रोग + वृद्धिररोचकः", "वृद्धिररोचकः is not one word; र comes from the visarga.")],
            "रोगवृद्धिः (increase of disease) + अरोचकः (loss of appetite).",
            "Visarga after a vowel other than अ/आ, before a vowel → र्."),
        mcq("transfer", 5, "By the pattern of त्रीन् पक्षान् जीवति, what does द्वौ मासौ वसति mean in a new example?",
            ("He stays for two months", "The accusative of time gives the span: द्वौ मासौ, for two months."),
            [("He stays in month two", "'In the second month' would be द्वितीये मासे (locative)."),
             ("He stays after two months", "'After' would need a word like अनन्तरम्; the accusative gives the span."),
             ("He stays as two months pass", "That would need a different construction; the accusative gives the span.")],
            "द्वौ मासौ वसति = he stays for two months, like त्रीन् पक्षान् जीवति = he lives for three fortnights.",
            "Accusative of time = how long.",
            teaches="An accusative of time states the span of an action: त्रीन् पक्षान् जीवति = lives for three fortnights."),
    ],
}

# ---------------------------------------------------------------- unit 37
AUTHORED["37"] = {
    "title": "वाताष्ठीलाऽतिसंवृद्धा",
    "question": "By card 37, what does the vātāṣṭhīlā do, where is it, and in whom?",
    "rule": ("A vātāṣṭhīlā (a hard, round, stony lump due to Vāta), greatly enlarged, remaining dreadful in the heart (हृदि), "
             "at once (सद्यः) steals the life (मुष्णाति जीवितम्) of one beset by thirst."),
    "limits": ("Verse, medium confidence, two printed lines joined. aṣṭhīlā is a traditional term; no modern equivalent is asserted. "
               "The avagrahas after -ā are a print habit, not sandhi marks."),
    "explain_hi": ("वाताष्ठीला यानी वात से बनी कठोर, गोल, पथरीली गाँठ; बहुत बढ़ी हुई (अतिसंवृद्धा) और हृदय में भयंकर रूप से टिकी हुई (तिष्ठन्ती दारुणा हृदि)। "
                   "यह तृष्णा से घिरे हुए (तृष्णया अनुपरीतस्य) का जीवन तुरन्त (सद्यः) हर लेती है (मुष्णाति)। "
                   "अष्ठीला परम्परागत शब्द है; इसका कोई आधुनिक नाम नहीं दिया गया। "
                   "अतिसंवृद्धा, तिष्ठन्ती, दारुणा: तीनों स्त्रीलिङ्ग हैं क्योंकि वाताष्ठीला स्त्रीलिङ्ग है। "
                   "‘सद्यो मुष्णाति’ में सद्यः + मुष्णाति: अः घोष व्यंजन म से पहले ओ बनता है।"),
    "hook": "हृदय में बढ़ी वाताष्ठीला, साथ में तृष्णा: जीवन तुरन्त हर ले।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "In card 37, what does सद्यो (सद्यः) mean?",
            ("At once", "सद्यः = at once, immediately."),
            [("Slowly", "Slowly would be शनैः; सद्यः = at once."),
             ("Monthly", "Monthly would be a word like मासि मासि; सद्यः = at once."),
             ("Daily", "Daily would be प्रतिदिनम्; सद्यः = at once.")],
            "सद्यः = at once.",
            "सद्यः = at once."),
        match(1, "Match each word of card 37 to its meaning.",
              [["अतिसंवृद्धा", "greatly enlarged"], ["तिष्ठंती", "remaining"], ["हृदि", "in the heart"],
               ["तृष्णया", "by thirst"], ["मुष्णाति", "steals"], ["जीवितं", "life"]],
              "अतिसंवृद्धा = greatly enlarged, तिष्ठंती = remaining, हृदि = in the heart, तृष्णया = by thirst, मुष्णाति = steals, जीवितं = life.",
              "अतिसंवृद्धा, तिष्ठंती, हृदि, तृष्णया, मुष्णाति, जीवितं."),
        order(2, "Put the printed words of card 37 in the printed order.",
              ["वाताष्ठीलाऽतिसंवृद्धा", "तिष्ठंती", "दारुणा", "हृदि", "तृष्णयाऽनुपरीतस्य", "सद्यो मुष्णाति जीवितं"],
              "The lump and its state (line 1), then whose life it steals and how fast (line 2).",
              "वाताष्ठीलाऽतिसंवृद्धा → तिष्ठंती → दारुणा → हृदि → तृष्णयाऽनुपरीतस्य → सद्यो मुष्णाति जीवितं.",
              role="extend",
              teaches="Line 1 describes the subject (feminine); line 2 gives the person (genitive) and the verb."),
        mcq("discriminate", 3, "By card 37, where does the vātāṣṭhīlā remain?",
            ("In the heart", "तिष्ठन्ती दारुणा हृदि: remaining dreadful in the heart."),
            [("In the groins", "The groins (वंक्षणौ) are named in card 39, of the wind, not here."),
             ("In the calves", "The calves are named in cards 27 and 38, not as its place."),
             ("In the throat", "No throat is named in card 37; the place is हृदि.")],
            "हृदि = in the heart (locative of हृद्).",
            "हृदि = in the heart."),
        mcq("apply", 4, "In card 37, why are अतिसंवृद्धा, तिष्ठंती and दारुणा feminine?",
            ("They agree with वाताष्ठीला", "वाताष्ठीला is feminine, so its adjectives are feminine."),
            [("They agree with जीवितं", "जीवितम् is neuter; feminine forms cannot agree with it."),
             ("They agree with हृदि", "हृदि is a locative of a neuter noun; these are nominatives."),
             ("They agree with तृष्णया", "तृष्णया is instrumental; these three are nominative.")],
            "Adjectives agree with their noun: वाताष्ठीला (f. nom. sg.).",
            "Agreement in gender, case and number."),
        mcq("transfer", 5, "By the pattern of तिष्ठंती (remaining, feminine), what does गच्छन्ती mean in a new example?",
            ("She who is going", "-अन्ती is the feminine present participle: गच्छन्ती = (she who is) going."),
            [("She who has gone", "Having gone would be गता (past participle), not गच्छन्ती."),
             ("She who will go", "Will go would be the future गमिष्यन्ती, not गच्छन्ती."),
             ("In order to go", "In order to go is the infinitive गन्तुम्, not गच्छन्ती.")],
            "गच्छन्ती = going (f.), like तिष्ठन्ती = remaining (f.).",
            "Present stem + -अन्ती = feminine present participle.",
            teaches="The feminine present participle ends in -अन्ती: तिष्ठ- + अन्ती → तिष्ठन्ती (remaining)."),
    ],
}

# ---------------------------------------------------------------- unit 38
AUTHORED["38"] = {
    "title": "शैथिल्यं पिंडिके वायुः",
    "question": "By card 38, what does the wind do to the calves and to the manyā before it steals life?",
    "rule": ("The wind (वायुः), having brought (नीत्वा) the two calves to slackness (शैथिल्यम्) and the nose to crookedness "
             "(conjectural), or, of a wasted one, having drawn tight (आयम्य) the two manyā, at once steals life."),
    "limits": ("Verse, medium confidence. Printed जिह्रतां is no word; crookedness (जिह्मताम्) is a conjecture: no question on the "
               "nose. manyā as the side of the neck is probable. How वा joins the two actions is the data's reading."),
    "explain_hi": ("वायु दोनों पिंडलियों को शिथिलता में (शैथिल्यं पिण्डिके) और नाक को अनुमानित पाठ पर टेढ़ेपन में ले जाकर (नीत्वा), "
                   "या क्षीण हुए व्यक्ति की दोनों मन्या (सम्भवतः गर्दन के पार्श्व) को खींचकर (आयम्य), तुरन्त जीवन हर लेता है। "
                   "छपा ‘जिह्रतां’ कोई शब्द नहीं; ‘जिह्मताम्’ अनुमान है, इसलिए नाक पर प्रश्न नहीं। "
                   "‘नीत्वा’ बिना उपसर्ग का क्त्वा-रूप है, ‘आयम्य’ उपसर्ग आ- के कारण ल्यप् (-य) रूप; दोनों मुख्य क्रिया ‘मुष्णाति’ से पहले की क्रियाएँ हैं। "
                   "‘वायुर्नीत्वा’ में वायुः + नीत्वा: उ के बाद विसर्ग घोष न से पहले र्।"),
    "hook": "पिंडली ढीली या मन्या तनी: वायु तुरन्त जीवन हरे।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "In card 38, what does शैथिल्यं mean?",
            ("Slackness", "शैथिल्य (from शिथिल, loose) = slackness."),
            [("Stiffness", "Stiffness would be स्तम्भ; शैथिल्य is slackness."),
             ("Swelling", "Swelling is शोफ; शैथिल्य is slackness."),
             ("Burning", "Burning is दाह; शैथिल्य is slackness.")],
            "शैथिल्यम् = slackness, looseness.",
            "शैथिल्य = slackness."),
        match(1, "Match each word of card 38 to its meaning.",
              [["शैथिल्यं", "slackness"], ["पिंडिके", "the two calves"], ["नीत्वा", "having brought"],
               ["नासां", "nose"], ["आयम्य", "having drawn tight"]],
              "शैथिल्यं = slackness, पिंडिके = the two calves, नीत्वा = having brought, नासां = nose, आयम्य = having drawn tight.",
              "शैथिल्यं, पिंडिके, नीत्वा, नासां, आयम्य."),
        order(2, "Put these printed words of card 38 in the printed order.",
              ["शैथिल्यं", "पिंडिके", "वायुर्नीत्वा", "नासां च", "क्षीणस्यायम्य", "मन्ये वा"],
              "Line 1: slackness, the calves, the wind having brought, and the nose. Line 2: of the wasted one having drawn tight, the manyā, or.",
              "शैथिल्यं → पिंडिके → वायुर्नीत्वा → नासां च → क्षीणस्यायम्य → मन्ये वा.",
              role="extend",
              teaches="Two gerunds, नीत्वा and आयम्य, come before the one main verb मुष्णाति."),
        mcq("discriminate", 3, "In card 38, which word is the main (finite) verb whose subject is वायुः?",
            ("मुष्णाति", "मुष्णाति (steals) is 3rd sg. present: the main verb, subject वायुः."),
            [("नीत्वा", "नीत्वा is a gerund (having brought), not a finite verb."),
             ("आयम्य", "आयम्य is a gerund (having drawn tight), not a finite verb."),
             ("शैथिल्यं", "शैथिल्यम् is a noun (slackness), not a verb.")],
            "Gerunds नीत्वा, आयम्य → main verb मुष्णाति.",
            "A gerund needs a finite verb to finish the sentence."),
        mcq("apply", 4, "In card 38, why does आयम्य end in -य while नीत्वा ends in -त्वा?",
            ("आयम्य has the prefix आ-", "With a prefix the gerund takes -य (आ-√यम् → आयम्य); √नी alone takes -त्वा."),
            [("आयम्य is a future form", "Both are gerunds ('having ...'); neither is future."),
             ("नीत्वा is a passive form", "Both are gerunds; -त्वा does not mark the passive."),
             ("आयम्य is a feminine form", "Gerunds are indeclinable; they have no gender.")],
            "Gerund: -त्वा without a prefix, -य with a prefix.",
            "Prefix + root → gerund in -य; plain root → -त्वा."),
        mcq("transfer", 5, "By the pattern of आयम्य (आ- + √यम्), which gerund of प्र- + √विश् (having entered) is right in a new example?",
            ("प्रविश्य", "With the prefix प्र-, the gerund takes -य: प्र-√विश् → प्रविश्य."),
            [("प्रविष्ट्वा", "-त्वा is used without a prefix; with प्र- the ending is -य."),
             ("प्रविशत्वा", "No such form; with a prefix the gerund ends in -य."),
             ("प्रविशन्य", "No such form; the gerund is प्रविश्य.")],
            "प्रविश्य = having entered, like आयम्य = having drawn tight.",
            "Prefix + root → gerund in -य.",
            teaches="A verb with a prefix forms its gerund in -य, not -त्वा: आ-√यम् → आयम्य, beside √नी → नीत्वा."),
    ],
}


# ================================================================ NOTES_HI
NOTES_HI = {
    "26": ("श्लोक; विश्वास मध्यम; कोई पाठ-चिह्न नहीं; दो छपी पंक्तियाँ (०२.११.४८ और ०२.११.४९) जोड़ी गईं। दोनों प्रथमा विशेषण (राजीचितः, "
           "स्रवन्) सम्भवतः कार्ड २५ के शोफ के हैं और द्वितीया समास रोगी का; यह अनुमान है। रेखाएँ किसकी, छपा नहीं। क्रिया नहीं; डेटा के अनुसार "
           "‘जायन्ते’ कार्ड २७ में है, दोनों कार्ड सम्भवतः एक वाक्य। ‘तयोः’ = ज्वर और अतिसार का। सन्धि जाँची: ज्वर + अतिसारौ → ज्वरातिसारौ "
           "और शोफ + अन्ते → शोफान्ते (अ + अ → आ; छपा ‘शोफांते’); श्वयथुः + वा → श्वयथुर्वा (उ के बाद विसर्ग, घोष से पहले → र्)।"),
    "27": ("श्लोक; विश्वास मध्यम; दो छपी पंक्तियाँ (०२.११.५० और ०२.११.५१)। पाठ-चिह्न (सम्भव): ‘जायंतेंऽताय’ में ‘ते’ के बाद अनुस्वार "
           "भटका हुआ लगता है; नियमित रूप जायन्तेऽन्ताय (ए + अ → एऽ)। ‘परित्रस्ते’ (डरी हुई) पिंडलियों पर नहीं बैठता; ‘परिस्रस्ते’ (ढीली) "
           "अनुमान है (त्र/स्र की छपाई-भूल; तुलना कार्ड ३८ का ‘शैथिल्यं पिंडिके’); इस पर प्रश्न नहीं। पहली पंक्ति के कर्ता कार्ड २६ के लक्षण "
           "हैं। ‘अन्ताय’ = अन्त के लिए (जीवन का, प्रसंग से)। वाक्य कार्ड २८ में आगे। सन्धि जाँची: श्वयथुः + यस्य → श्वयथुर्यस्य (उ के बाद "
           "विसर्ग, घोष य से पहले → र्)।"),
    "28": ("श्लोक; विश्वास कम; दो छपी पंक्तियाँ (०२.११.५२ और ०२.११.५३)। पाठ-चिह्न (सम्भव): ‘विशेषायस्य’ में द् छूटा लगता है, पाठ "
           "विशेषाद् यस्य। ‘सीदतः’ द्विवचन क्रिया (दोनों धँसती हैं) ली गई; षष्ठी कृदन्त ‘धँसते हुए का’ भी सम्भव। ‘शुष्यतः’ षष्ठी कृदन्त ली गई; "
           "द्विवचन क्रिया भी सम्भव; दूसरी पंक्ति की क्रिया ‘शूयन्ते’ कार्ड २९ में है, इसलिए अर्थ पक्का नहीं। इन पर प्रश्न नहीं। पहली पंक्ति "
           "कार्ड २७ के ‘यस्य’ को पूरा करती है। सन्धि जाँची: च + एव → चैव (अ + ए → ऐ); तम् + भिषक् → तं भिषक् (व्यंजन से पहले म् → ं)।"),
    "29": ("श्लोक; विश्वास मध्यम; दो छपी पंक्तियाँ (०२.११.५४ और ०२.११.५५)। पाठ-चिह्न (सम्भव): ‘शूंयंते’ में भटका अनुस्वार, पाठ शूयन्ते। "
           "पहली पंक्ति कार्ड २८ को पूरा करती है (सम्भवतः)। ‘मासात्’ पञ्चमी: ‘मास के भीतर’ लिया, ‘मास के बाद’ भी सम्भव। ‘पञ्चता’ मृत्यु का "
           "मुहावरा। उदर को जलोदर जैसा मानना सम्भावित है। दूसरी पंक्ति में कोई फल नहीं, और मेहन न दिखने का कारण न पाठ देता है न डेटा। "
           "सन्धि जाँची: देहात् + सः → देहात्स (स से पहले त् वैसा ही); सः व्यंजन से पहले विसर्ग खोता है; मासात् + याति → मासाद्याति (घोष "
           "से पहले त् → द्); यः + च → यश्च (च से पहले विसर्ग → श्)।"),
    "30": ("श्लोक; विश्वास मध्यम; दो छपी पंक्तियाँ (०२.११.५६ और ०२.११.५७)। पाठ-चिह्न (सम्भव): ‘जठरोन्नातत्परिधानं’ में ‘न्नातत्’ कोई "
           "शब्द नहीं; ‘जठरोन्नतात् परिधानं’ (पेट के उभार से) अनुमान; कारण पर प्रश्न नहीं। छपा ‘वीसर्पः’ (दीर्घ ई) = विसर्प; विसर्प की पहचान "
           "सम्भावित। ‘मूर्च्छा’ का दोहरा च्छ वर्तनी है। डेटा के अनुसार छपी पंक्तियाँ ५५-५६ (कार्ड २९/३०) और लक्षण जोड़ती हैं, फल नहीं। क्रिया "
           "‘हन्ति’ सम्भवतः छपी पंक्ति ६० (कार्ड ३२) में, तय नहीं। सन्धि जाँची: मूर्छा + अङ्ग → मूर्छाङ्ग (आ + अ → आ)।"),
    "31": ("श्लोक; विश्वास उच्च; कोई पाठ-चिह्न नहीं; दो छपी पंक्तियाँ (०२.११.५८ और ०२.११.५९)। पहली पंक्ति कार्ड ३० की सूची आगे बढ़ाती "
           "है। ‘आस्यशोफ’ = मुख की सूजन (आस्य = मुख भी, चेहरा भी); ‘देहसाद’ = देह की थकावट। क्रिया ‘हन्ति’ कार्ड ३२ में; दोनों कार्ड "
           "सम्भवतः एक कथन। कुष्ठ = कोढ़, त्वचा-रोगों का समूह (मानक)। सन्धि जाँची: भ्रम + आस्य → भ्रमास्य (अ + आ → आ); साद + अतिसार → "
           "सादातिसार (अ + अ → आ); विशीर्यमाण + अङ्गम् → विशीर्यमाणाङ्गम् (छपा ‘विशीर्यमाणांगं’, बिना जगह ‘रक्तनेत्रं’ से सटा)।"),
    "32": ("श्लोक; विश्वास मध्यम; कोई पाठ-चिह्न नहीं; दो छपी पंक्तियाँ (०२.११.६० और ०२.११.६१)। कर्ता ‘कुष्ठ’ कार्ड ३१ से। जन्तु = जीव; "
           "कीड़े या छोटे जीव सामान्य अर्थ, पाठ स्पष्ट नहीं करता। वायु यहाँ शरीर का वात है। दूसरी पंक्ति में क्रिया नहीं; डेटा के अनुसार "
           "कार्ड ३४ की ‘घ्नन्ति’ सम्भवतः, पर एकवचन कर्ता के साथ बहुवचन क्रिया नहीं बैठती, इसलिए तय नहीं। सन्धि जाँची: मन्द + अग्निम् → "
           "मन्दाग्निम्; जन्तुभिः + जुष्टम् → जन्तुभिर्जुष्टम् (इ के बाद विसर्ग, घोष से पहले → र्); तृष्णा + अतिसारिणम् → तृष्णातिसारिणम् "
           "(आ + अ → आ); रुजा + आतुरम् → रुजातुरम् (आ + आ → आ)।"),
    "33": ("डेटा में प्रकार गद्य (prose) है, यद्यपि पंक्तियाँ छन्द-जैसी लगती हैं; प्रकार वैसा ही रखा, छन्द पर कुछ नहीं कहा। विश्वास कम; दो "
           "छपी पंक्तियाँ (०२.११.६२ और ०२.११.६३)। पाठ-चिह्न (सम्भव): ‘वातस्रं’ में वात-अस्र का दीर्घ आ छूटा, पाठ वातास्र (सम्भवतः "
           "वातरक्त); पहली पंक्ति का बीच ‘सूर्च्छायमदास्वम’ अपठनीय (अनुमान: मूर्छा, आयाम, मद, अस्वप्न; अनुवाद में नहीं अपनाया); दूसरी पंक्ति "
           "का आरम्भ ‘शिरोपहारुचिश्वारस’ अपठनीय (अनुमान: शिरोरुजा, अरुचि, श्वास; तुलना कार्ड ३४ की सूची)। इन पर प्रश्न नहीं। कर्ता सम्भवतः "
           "वातास्र (अनुमान); वाक्य कार्ड ३४ तक चलता लगता है। सन्धि जाँची: ज्वर + अन्वितम् → ज्वरान्वितम् (अ + अ → आ)।"),
    "34": ("डेटा में प्रकार गद्य (prose) है, यद्यपि पंक्तियाँ छन्द-जैसी लगती हैं; प्रकार वैसा ही रखा, छन्द पर कुछ नहीं कहा। विश्वास मध्यम; "
           "दो छपी पंक्तियाँ (०२.११.६४ और ०२.११.६५)। पाठ-चिह्न (सम्भव): ‘विद्भेद्’ में भेद का अन्त्य अ छूटा (विड्भेद-तृड्); इस पर प्रश्न "
           "नहीं। ‘अनल’ बल के साथ सम्भवतः पाचन अग्नि; ‘मेह’ सम्भवतः प्रमेह-समूह। दूसरी पंक्ति अपने आप में पूरा वाक्य है; ‘घ्नन्ति’ कार्ड "
           "३२-३३ को भी समाप्त करती है या नहीं, स्थापित नहीं। सन्धि जाँची: शिरस् + रोग → शिरोरोग (अस् + घोष व्यंजन → ओ); रोग + अरुचि → "
           "रोगारुचि; तृट् + भ्रमैः → तृड्भ्रमैः (घोष से पहले ट् → ड्); सर्व + आमयाः → सर्वामयाः; बल + अनलम् → बलानलम्।"),
    "35": ("श्लोक; विश्वास मध्यम; दो छपी पंक्तियाँ (०२.११.६६ और ०२.११.६७)। पाठ-चिह्न (सम्भव): ‘रत्त्युदरी’ में ‘रत्त-’ सम्भवतः ‘रक्त-’ "
           "(क/त भूल): रक्ती उदरी; ‘रक्ती’ का अर्थ अनिश्चित (रक्तपित्त भी हो सकता है, अपनाया नहीं); इस पर प्रश्न नहीं। उदर, क्षय, मेह की "
           "पहचान सम्भावित। ‘तान्’ पहले गिनाए रोगियों को लेता है; ‘वर्जयेत्’ का कर्ता छपा नहीं (कार्ड २८ में भिषक् है)। सन्धि जाँची: "
           "वातव्याधिः + अपस्मारी → वातव्याधिरपस्मारी (इ के बाद विसर्ग, स्वर से पहले → र्); विकारे + अल्पे + अपि → विकारेऽल्पेऽपि (ए + अ → "
           "एऽ, दो बार)।"),
    "36": ("डेटा में प्रकार गद्य (prose) है, यद्यपि पंक्तियाँ छन्द-जैसी लगती हैं; प्रकार वैसा ही रखा, छन्द पर कुछ नहीं कहा। विश्वास उच्च; "
           "कोई पाठ-चिह्न नहीं; दो छपी पंक्तियाँ (०२.११.६८ और ०२.११.६९), एक कथन। छपा ‘पक्षाञ्स’ में ञ् छपाई की आदत; सामान्य सन्धि "
           "पक्षांस्स (या पक्षान् स); पढ़ा पक्षान् स। सन्धि जाँची: क्षयः + तीव्रः → क्षयस्तीव्रः (त से पहले विसर्ग → स्); तीव्रः + रोग- → "
           "तीव्रो रोग- (अः + घोष व्यंजन → ओ); रोगवृद्धिः + अरोचकः → रोगवृद्धिररोचकः (इ के बाद विसर्ग, स्वर से पहले → र्); यस्य + आतुरस्य → "
           "यस्यातुरस्य (अ + आ → आ)।"),
    "37": ("श्लोक; विश्वास मध्यम; कोई पाठ-चिह्न नहीं; दो छपी पंक्तियाँ (०२.११.७० और ०२.११.७१)। ‘वाताष्ठीलाऽति’ और ‘तृष्णयाऽनु’ में "
           "आ के बाद छपा अवग्रह छपाई की आदत है (आ + अ → आ)। अष्ठीला परम्परागत शब्द, कोई आधुनिक नाम नहीं। कर्ता स्त्रीलिङ्ग वाताष्ठीला। "
           "सन्धि जाँची: वात + अष्ठीला → वाताष्ठीला (अ + अ → आ); सद्यः + मुष्णाति → सद्यो मुष्णाति (अः + घोष व्यंजन → ओ)।"),
    "38": ("श्लोक; विश्वास मध्यम; दो छपी पंक्तियाँ (०२.११.७२ और ०२.११.७३)। पाठ-चिह्न (सम्भव): ‘जिह्रतां’ कोई शब्द नहीं; ‘जिह्मतां’ "
           "(टेढ़ापन) अनुमान (म/र भूल); नाक पर प्रश्न नहीं। ‘पिण्डिके’ और ‘नासाम्’ दोनों ‘नीत्वा’ के कर्म, दूसरी द्वितीया अवस्था बताती है। "
           "‘वा’ दोनों क्रियाओं को जोड़ता है (डेटा का पाठ)। मन्या = सम्भवतः गर्दन का पार्श्व। कर्ता वायु पहली पंक्ति से। सन्धि जाँची: वायुः + "
           "नीत्वा → वायुर्नीत्वा (उ के बाद विसर्ग, घोष से पहले → र्); क्षीणस्य + आयम्य → क्षीणस्यायम्य (अ + आ → आ); सद्यः + मुष्णाति → "
           "सद्यो मुष्णाति (अः + घोष व्यंजन → ओ)।"),
}


# ================================================================ AIDS
AIDS = {
    "26": {
        "chunks": "राजीचितः | स्रवंछर्द्दिज्वरश्वासातिसारिणं || ज्वरातिसारौ | शोफांते | श्वयथुर्वा | तयोः क्षये",
        "seesaw": "शोफ के अन्त में → ज्वर और अतिसार ⇄ ज्वर-अतिसार के क्षय में → श्वयथु (सूजन)। दोनों क्रम इसी इकाई में।",
        "sandhi": ("अ + अ → आ: ज्वर + अतिसारौ → ज्वरातिसारौ, शोफ + अन्ते → शोफान्ते · उ के बाद विसर्ग, घोष से पहले → र्: "
                   "श्वयथुः + वा → श्वयथुर्वा।"),
        "anchors": "चार शिकायतें क्रम से: छर्दि, ज्वर, श्वास, अतिसार (‘छ-ज-श-अ’)। (मेरी याद-पद्धति)",
    },
    "27": {
        "chunks": "दुर्बलस्य | विशेषेण | जायंतेंऽताय | देहिनः || श्वयथुर्यस्य | पादस्थः | परित्रस्ते च | पिंडिके",
        "frame": "किसके लिए: दुर्बलस्य देहिनः → कैसे: विशेषेण → क्या: जायन्ते अन्ताय (कार्ड २६ के लक्षण) → नया रोगी: यस्य श्वयथुः पादस्थः ...",
        "sandhi": "उ के बाद विसर्ग, घोष य से पहले → र्: श्वयथुः + यस्य → श्वयथुर्यस्य · ए + अ → एऽ: जायन्ते + अन्ताय → जायन्तेऽन्ताय (छपा अनुस्वार भटका)।",
    },
    "28": {
        "chunks": "सीदतः | सक्थिनी चैव | तं भिषक् परिवर्जयेत् || आननं | हस्तपादौ च | विशेषायस्य | शुष्यतः",
        "chain": {"steps": ["यस्य श्वयथुः पादस्थः (कार्ड २७)", "पिण्डिके ... (कार्ड २७)", "सक्थिनी सीदतः", "तं भिषक् परिवर्जयेत्"]},
        "sandhi": "अ + ए → ऐ: च + एव → चैव · व्यंजन से पहले म् → ं: तम् + भिषक् → तं भिषक्।",
    },
    "29": {
        "chunks": "शूंयंते वा | विना देहात् | स मासाद्याति पंचतां || उदरी यश्च | शोफी वा | स्वं न पश्यति मेहनं",
        "sandhi": ("घोष से पहले त् → द्: मासात् + याति → मासाद्याति · सः व्यंजन से पहले विसर्ग खोता है: सः + मासात् → स मासात् · "
                   "च से पहले विसर्ग → श्: यः + च → यश्च।"),
        "anchors": "पञ्चता = पाँच का भाव: शरीर पाँच भूतों में लौटा, यानी मृत्यु। (केवल याद की सहायता)",
    },
    "30": {
        "chunks": "यस्य वा | जठरोन्नातत्परिधानं | न तिष्ठति || वीसर्पः | कासवैवर्ण्यज्वरमूर्च्छांगभंगवान्",
        "chain": {"steps": ["१ कास (खाँसी)", "२ वैवर्ण्य (रंग बिगड़ना)", "३ ज्वर", "४ मूर्च्छा", "५ अङ्गभङ्ग (अंगों की टूटन)"]},
        "anchors": "पक्का: परिधान न टिके; विसर्प की पाँच शिकायतें। अनुमान: ‘पेट के उभार से’। (मेरी याद-पद्धति)",
    },
    "31": {
        "chunks": "भ्रमास्यशोफहृल्लासदेहसादातिसारवान् || कुष्ठं | विशीर्यमाणांगं | रक्तनेत्रं | हतस्वरं",
        "contrast": ("विसर्प की सूची (कार्ड ३० से आगे): भ्रम, आस्यशोफ, हृल्लास, देहसाद, अतिसार ⇄ कुष्ठ का रोगी: अंग बिखरते, लाल आँखें, "
                     "स्वर नष्ट। दोनों इसी इकाई में।"),
        "sandhi": "अ + आ → आ: भ्रम + आस्य → भ्रमास्य · अ + अ → आ: साद + अतिसार → सादातिसार, विशीर्यमाण + अङ्गम् → विशीर्यमाणाङ्गम्।",
    },
    "32": {
        "chunks": "मंदाग्निं | जंतुभिर्जुष्टं | हंति | तृष्णातिसारिणं || वायुः | सुप्तत्वचं | भुग्नं | कंपशोफरुजातुरं",
        "contrast": ("कुष्ठ (हन्ति): मन्दाग्नि, जन्तुओं से घिरा, तृष्णा, अतिसार ⇄ वायु (क्रिया इस कार्ड में नहीं): सुन्न त्वचा, झुका, कम्प, "
                     "सूजन, पीड़ा। दोनों इसी इकाई में।"),
        "sandhi": ("अ + अ → आ: मन्द + अग्निम् → मन्दाग्निम् · इ के बाद विसर्ग, घोष से पहले → र्: जन्तुभिः + जुष्टम् → जन्तुभिर्जुष्टम् · "
                   "आ + आ → आ: रुजा + आतुरम् → रुजातुरम्।"),
    },
    "33": {
        "chunks": "वातस्रं | मोहसूर्च्छायमदास्वमज्वरान्वितं || शिरोपहारुचिश्वारससंकोचस्फोटकोथवत्",
        "anchors": "पक्के: मोह, ज्वरान्वित; संकोच, स्फोट, कोथ (-वत्)। अपठनीय: दो बीच के अंश। अनुमान: वातास्र। (मेरी याद-पद्धति)",
        "frame": "रोग (अनुमानित: वातास्र) → साथ: मोह ... ज्वर (अन्वितम्) → और: ... संकोच, स्फोट, कोथ (-वत्) → क्रिया: यहाँ नहीं।",
    },
    "34": {
        "chunks": "शिरोरोगारुचिश्वासमेहविद्भेद्तृड्भ्रमैः || घ्नंति | सर्वामयाः | क्षीणस्वरधातुबलानलं",
        "diagram": {"groups": [
            {"label": "किनसे (तृतीया, छपे क्रम में)",
             "items": ["१ शिरोरोग", "२ अरुचि", "३ श्वास", "४ मेह", "५ विद्भेद्", "६ तृड्", "७ भ्रम"]},
            {"label": "किसे: क्षीण ...", "items": ["स्वर", "धातु", "बल", "अनल"]}]},
        "sandhi": ("अस् + घोष व्यंजन → ओ: शिरस् + रोग → शिरोरोग · घोष से पहले ट् → ड्: तृट् + भ्रमैः → तृड्भ्रमैः · अ + आ → आ: "
                   "सर्व + आमयाः → सर्वामयाः।"),
    },
    "35": {
        "chunks": "वातव्याधिरपस्मारी | कुष्ठी | रत्त्युदरी | क्षयी || गुल्मी | मेही च | तान् क्षीणान् | विकारेऽल्पेऽपि | वर्जयेत्",
        "diagram": {"groups": [
            {"label": "रोगी (छपे क्रम में)",
             "items": ["१ वातव्याधि", "२ अपस्मारी", "३ कुष्ठी", "४ रत्त्युदरी (अनिश्चित)", "५ क्षयी", "६ गुल्मी", "७ मेही"]},
            {"label": "कब वर्ज्य", "items": ["क्षीण हों तो", "थोड़े विकार में भी"]}]},
        "sandhi": ("इ के बाद विसर्ग, स्वर से पहले → र्: वातव्याधिः + अपस्मारी → वातव्याधिरपस्मारी · ए + अ → एऽ: विकारे + अल्पे + अपि → "
                   "विकारेऽल्पेऽपि।"),
        "pegs": "‘-ई’ वाले सब रोगी: अपस्मारी, कुष्ठी, उदरी, क्षयी, गुल्मी, मेही; पहला ‘वातव्याधि’ अकेला बिना -ई। (मेरा बनाया स्मरण-सूत्र)",
    },
    "36": {
        "chunks": "बलमांसक्षयस्तीव्रो | रोगवृद्धिररोचकः || यस्यातुरस्य | लक्ष्यंते | त्रीन् पक्षाञ्स जीवति",
        "chain": {"steps": ["बल-मांस का तीव्र क्षय", "रोग की वृद्धि", "अरोचक", "जिस रोगी में दिखें", "वह तीन पक्ष जीता है (पाठ)"]},
        "sandhi": ("त से पहले विसर्ग → स्: क्षयः + तीव्रः → क्षयस्तीव्रः · अः + घोष व्यंजन → ओ: तीव्रः + रोग- → तीव्रो रोग- · इ के बाद "
                   "विसर्ग, स्वर से पहले → र्: रोगवृद्धिः + अरोचकः → रोगवृद्धिररोचकः।"),
    },
    "37": {
        "chunks": "वाताष्ठीलाऽतिसंवृद्धा | तिष्ठंती | दारुणा | हृदि || तृष्णयाऽनुपरीतस्य | सद्यो मुष्णाति जीवितं",
        "frame": "कौन: वाताष्ठीला (बहुत बढ़ी) → कहाँ: हृदि (भयंकर टिकी) → किसका: तृष्णा से घिरे का → क्या: सद्यः जीवन हरे।",
        "sandhi": "अ + अ → आ: वात + अष्ठीला → वाताष्ठीला · अः + घोष व्यंजन → ओ: सद्यः + मुष्णाति → सद्यो मुष्णाति · आ के बाद ऽ छपाई की आदत।",
    },
    "38": {
        "chunks": "शैथिल्यं पिंडिके | वायुर्नीत्वा | नासां च जिह्रतां || क्षीणस्यायम्य मन्ये वा | सद्यो मुष्णाति जीवितं",
        "seesaw": "शैथिल्य (पिंडलियाँ ढीली, नीत्वा) ⇄ आयम्य (मन्या खिंची, तनी): ढीला ⇄ तना, दोनों इसी इकाई में; दोनों के बाद ‘सद्यो मुष्णाति जीवितं’।",
        "sandhi": ("उ के बाद विसर्ग, घोष से पहले → र्: वायुः + नीत्वा → वायुर्नीत्वा · अ + आ → आ: क्षीणस्य + आयम्य → क्षीणस्यायम्य · "
                   "अः + घोष व्यंजन → ओ: सद्यः + मुष्णाति → सद्यो मुष्णाति।"),
    },
}

# ================================================================ IMAGE_SPECS
IMAGE_SPECS = {
    ("26", "seesaw"): {
        "file": "sh11-shopha-26.svg",
        "alt": ("Split of card 26: at the end of the swelling, fever and diarrhoea; when fever and diarrhoea decline, "
                "swelling."),
        "type": "split",
        "title": "कार्ड २६: दो उलटे क्रम",
        "cols": [["शोफान्ते", ["सूजन का अन्त", "तब ज्वर, अतिसार"]],
                 ["तयोः क्षये", ["ज्वर-अतिसार घटें", "तब श्वयथु (सूजन)"]]],
    },
    ("30", "chain"): {
        "file": "sh11-visarpa-30.svg",
        "alt": ("Chain of card 30: the five complaints joined to visarpa in printed order: cough, discolouration, fever, "
                "fainting, breaking pain in the limbs."),
        "type": "chain",
        "title": "कार्ड ३०: विसर्प (सम्भावित) के साथ, क्रम से",
        "steps": ["१ कास (खाँसी)", "२ वैवर्ण्य (रंग बिगड़ना)", "३ ज्वर", "४ मूर्च्छा", "५ अङ्गभङ्ग (अंगों की टूटन)"],
    },
    ("32", "contrast"): {
        "file": "sh11-kushtha-vayu-32.svg",
        "alt": ("Split of card 32: kuṣṭha kills one with weak digestive fire, infested by creatures, with thirst and "
                "diarrhoea; vāyu: one with numb skin, bent, with tremor, swelling and pain (no verb in the card)."),
        "type": "split",
        "title": "कार्ड ३२: दो पंक्तियाँ, दो रोगी",
        "cols": [["कुष्ठ (हन्ति)", ["मन्द अग्नि", "जन्तुओं से घिरा", "तृष्णा, अतिसार"]],
                 ["वायु (क्रिया नहीं)", ["सुन्न त्वचा", "झुका हुआ", "कम्प, सूजन, पीड़ा"]]],
    },
    ("34", "diagram"): {
        "file": "sh11-sarvamaya-34.svg",
        "alt": ("Chain of card 34: all diseases kill one whose voice, body-tissues, strength and fire are wasted, by "
                "head disease, distaste for food, breathlessness, meha, loose stool, thirst and giddiness."),
        "type": "chain",
        "title": "कार्ड ३४: किनसे, कौन, किसे",
        "steps": ["किनसे (क्रम से): १ शिरोरोग २ अरुचि ३ श्वास ४ मेह", "५ विद्भेद् ६ तृड् ७ भ्रम", "सर्वामयाः घ्नन्ति: सभी रोग मारते हैं",
                  "किसे: जिसके स्वर, धातु, बल, अनल क्षीण"],
    },
    ("35", "diagram"): {
        "file": "sh11-varjya-35.svg",
        "alt": ("Table of card 35: the patients in printed order (vātavyādhi, apasmāra, kuṣṭha, the uncertain raktī-udarī, "
                "kṣaya, gulma, meha), to be avoided when wasted, even in a slight disorder."),
        "type": "table",
        "title": "कार्ड ३५: क्षीण हों तो थोड़े विकार में भी वर्ज्य",
        "heads": ["क्रम", "रोगी"],
        "rows": [["१", "वातव्याधि वाला"], ["२", "अपस्मारी (मिर्गी)"], ["३", "कुष्ठी"],
                 ["४", "रत्त्युदरी (पाठ अनिश्चित)"], ["५", "क्षयी"], ["६", "गुल्मी"], ["७", "मेही"]],
    },
    ("36", "chain"): {
        "file": "sh11-paksha-36.svg",
        "alt": ("Chain of card 36: severe loss of strength and flesh, increase of disease, loss of appetite; the patient in "
                "whom they are observed lives three fortnights, as the text states."),
        "type": "chain",
        "title": "कार्ड ३६: तीन लक्षण, पाठ की अवधि",
        "steps": ["बल-मांस का तीव्र क्षय", "रोग की वृद्धि", "अरोचक (अरुचि)", "जिस रोगी में दिखें", "वह तीन पक्ष जीता है (पाठ)"],
    },
    ("38", "seesaw"): {
        "file": "sh11-shaithilya-38.svg",
        "alt": ("Split of card 38: the wind brings the two calves to slackness, or draws the two manyā tight (side of the "
                "neck, probable); either way it at once steals life."),
        "type": "split",
        "title": "कार्ड ३८: ढीला या तना",
        "cols": [["नीत्वा", ["दोनों पिंडलियाँ", "शैथिल्य (ढीली)", "सद्यो मुष्णाति जीवितम्"]],
                 ["आयम्य", ["दोनों मन्या (सम्भावित)", "खिंची, तनी", "सद्यो मुष्णाति जीवितम्"]]],
    },
}
