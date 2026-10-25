from helpers import mcq, match, order, fill, multi, accepts


def T(q, teaches):
    q["teaches"] = teaches
    return q


AUTHORED = {}

# ---------------------------------------------------------------- unit 39
AUTHORED["39"] = {
    "title": "नाभीगुदांतरं गत्वा",
    "question": "By card 39, where does the strong one (taken as vāyu, Vāta) go, settle and take hold?",
    "rule": ("Having gone to the space between navel and anus (नाभीगुदांतरं गत्वा), or settling in the two groins "
             "(वंक्षणौ समाश्रयन्), having seized the anus and the heart (पायुहृदये), the strong one (बली)."),
    "limits": ("No main verb: the data says cards 39 to 42 (to card 42, line 1) appear to form one run, verb मुष्णाति "
               "(card 42), subject vāyu (Vāta). बली as vāyu is an inference; how क्षीणदेहस्य वा attaches is unclear: "
               "no question on these or on the case of पायुहृदये."),
    "explain_hi": ("यह इकाई एक लम्बी शृंखला का आरम्भ है: डेटा के नोट्स के अनुसार कार्ड ३९ से कार्ड ४२ की पहली पंक्ति तक एक ही वाक्य प्रतीत होता है, जिसकी क्रिया "
                   "‘मुष्णाति’ (हर लेता है) कार्ड ४२ में है और कर्ता वायु (मारुत) है। "
                   "यहाँ तीन बातें गिनाई गई हैं: नाभि और गुदा के बीच के स्थान में जाना, या दोनों वंक्षण (जाँघ और पेट के जोड़) में आश्रय लेना, "
                   "और गुदा (पायु) तथा हृदय को पकड़ना। "
                   "‘बली’ (बलवान) को वायु मानना डेटा का अनुमान है, और ‘क्षीणदेहस्य वा’ (या क्षीण देह वाले का) किससे जुड़ता है, यह स्पष्ट नहीं; "
                   "इन पर प्रश्न नहीं। गुदा के लिए यहाँ दो शब्द हैं: गुद और पायु।"),
    "hook": "नाभि-गुदा के बीच, या दोनों वंक्षण, फिर पायु और हृदय: शृंखला का पहला पड़ाव।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "In card 39, what does वंक्षणौ mean?",
            ("The two groins", "वङ्क्षणौ = the two groins (m. acc. dual)."),
            [("The two calves", "The calves are पिण्डिके; वंक्षणौ are the groins."),
             ("The two temples", "The temples are शङ्खौ; वंक्षणौ are the groins."),
             ("The two shoulders", "The shoulders would be अंसौ; वंक्षणौ are the groins.")],
            "वंक्षणौ = the two groins, where the strong one may settle.",
            "वङ्क्षण = groin."),
        order(1, "Put the words of card 39, line 1, in the printed order.",
              ["नाभीगुदांतरं", "गत्वा", "वंक्षणौ", "वा", "समाश्रयन्"],
              "Having gone to the space between navel and anus, or settling in the two groins.",
              "नाभीगुदांतरं → गत्वा → वंक्षणौ → वा → समाश्रयन्."),
        match(2, "Match each word of card 39 to its meaning.",
              [["गत्वा", "having gone"], ["समाश्रयन्", "settling in"], ["गृहीत्वा", "having seized"],
               ["क्षीण", "wasted"], ["बली", "strong"]],
              "गत्वा = having gone, समाश्रयन् = settling in, गृहीत्वा = having seized, क्षीण = wasted, बली = strong.",
              "गत्वा, समाश्रयन्, गृहीत्वा, क्षीण, बली.", role="extend",
              teaches=("गत्वा and गृहीत्वा end in -त्वा: actions done before the main verb, which the data finds only in "
                       "card 42 (मुष्णाति).")),
        mcq("discriminate", 3, "Which split of -गुदांतरं in card 39 is right?",
            ("गुद + अन्तरम्", "अ + अ → आ: गुद + अन्तरम् → गुदान्तरम्; final म् before ग is written ं."),
            [("गुदान् + तरम्", "तरम् is not the word here; the आ comes from अ + अ."),
             ("गुदे + अन्तरम्", "ए + अ would print गुदेऽन्तरम्, not गुदान्तरम्."),
             ("गुदम् + अन्तरम्", "म् + अ would print गुदमन्तरम्, with म.")],
            "गुद (anus) + अन्तरम् (space between): अ + अ → आ.",
            "अ + अ → आ."),
        mcq("apply", 4, "Card 39 names the anus with two different words. Which pair is it?",
            ("गुद and पायु", "नाभीगुदांतरं has गुद, and पायुहृदये has पायु: both mean the anus."),
            [("नाभि and पायु", "नाभि is the navel; only पायु is the anus."),
             ("वंक्षण and गुद", "वंक्षण is the groin; only गुद is the anus."),
             ("हृदय and पायु", "हृदय is the heart; only पायु is the anus.")],
            "गुद (line 1) and पायु (line 2) both name the anus.",
            "गुद = पायु = anus."),
        mcq("transfer", 5, "By the pattern of गत्वा (from √गम्), what does नत्वा (from √नम्, to bow) mean in a new example?",
            ("Having bowed", "-त्वा = having done: नत्वा = having bowed, as गत्वा = having gone."),
            [("He bows", "He bows would be नमति; -त्वा marks a finished action."),
             ("In order to bow", "That would be the infinitive नन्तुम्; -त्वा means having done."),
             ("Bowed down", "A past participle would be नत; नत्वा is the absolutive.")],
            "नत्वा = having bowed, like गत्वा = having gone.",
            "Root without prefix + -त्वा = having done.",
            teaches="-त्वा on a root without a prefix means 'having done': √गम् → गत्वा, √ग्रह् → गृहीत्वा."),
    ],
}

# ---------------------------------------------------------------- unit 40
AUTHORED["40"] = {
    "title": "मलान्बस्तिशिरोनाभि विबद्ध्य",
    "question": "By card 40, what is obstructed, and which effects follow?",
    "rule": ("Having obstructed the waste products (मलान्) at the head of the bladder (probable) and the navel, producing pain "
             "(रुजम्), causing pain in the two groins (वंक्षणयोः शूलम्), thirst (तृष्णाम्) and the state of broken "
             "(probably loose) stool (भिन्नपुरीषताम्)."),
    "limits": ("No main verb: the run of cards 39 to 42 ends in मुष्णाति (card 42). बस्तिशिरोनाभि is read 'head of the "
               "bladder (probable) and navel'; three items (bladder, head, navel) are also possible, and its case is not shown: "
               "no question on it. 'Loose' for भिन्न is only probable."),
    "explain_hi": ("कार्ड ३९ की शृंखला आगे चलती है (कर्ता डेटा के अनुसार वायु)। "
                   "पहले मलों (अपशिष्टों) को बस्ति के शिर यानी सम्भवतः मूत्राशय के ऊपरी भाग और नाभि पर रोकना, फिर पीड़ा (रुजा) उत्पन्न करना, "
                   "दोनों वंक्षण में शूल, तृष्णा और भिन्नपुरीषता यानी टूटे हुए, सम्भवतः पतले मल की अवस्था। "
                   "‘बस्तिशिरोनाभि’ को तीन वस्तुएँ (बस्ति, सिर, नाभि) भी पढ़ा जा सकता है और इसकी विभक्ति छपी नहीं; इस पर प्रश्न नहीं। "
                   "‘विबद्ध्य’ (लिखित रूप विबध्य) उपसर्ग वि- के कारण -त्वा नहीं, -य से बना है।"),
    "hook": "मल रुके, फिर पीड़ा, वंक्षण में शूल, तृष्णा, पतला (सम्भवतः) मल: क्रम याद रखो।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "In card 40, what does तृष्णाम् mean?",
            ("Thirst", "तृष्णा = thirst (f. acc. sg. here)."),
            [("Hunger", "Hunger would be क्षुधा; तृष्णा is thirst."),
             ("Sleep", "Sleep would be निद्रा; तृष्णा is thirst."),
             ("Itch", "Itch would be कण्डू; तृष्णा is thirst.")],
            "तृष्णा = thirst, one of the effects listed.",
            "तृष्णा = thirst."),
        order(1, "Put these parts of card 40 in the printed order.",
              ["मलान्", "विबद्ध्य", "जनयन् रुजं", "कुर्वन् वंक्षणयोः शूलं", "तृष्णां", "भिन्नपुरीषतां"],
              "Waste obstructed; pain produced; pain in the two groins; thirst; broken (probably loose) stool.",
              "मलान् → विबद्ध्य → जनयन् रुजं → कुर्वन् वंक्षणयोः शूलं → तृष्णां → भिन्नपुरीषतां."),
        match(2, "Match each word of card 40 to its meaning.",
              [["मलान्", "waste products"], ["विबद्ध्य", "having obstructed"], ["वंक्षणयोः", "in the two groins"],
               ["तृष्णाम्", "thirst"], ["भिन्नपुरीषताम्", "state of broken (probably loose) stool"]],
              "मलान् = waste products, विबद्ध्य = having obstructed, वंक्षणयोः = in the two groins, तृष्णाम् = thirst, "
              "भिन्नपुरीषताम् = state of broken (probably loose) stool.",
              "मलान्, विबद्ध्य, वंक्षणयोः, तृष्णाम्, भिन्नपुरीषताम्.", role="extend",
              teaches="भिन्नपुरीषता = भिन्न-पुरीष (broken stool) + -ता (state of): an abstract noun of a state."),
        mcq("discriminate", 3, "By card 40, where is the pain called शूलम् caused?",
            ("In the two groins", "कुर्वन् वंक्षणयोः शूलम्: causing pain in the two groins."),
            [("In the two eyes", "The eyes are not named in card 40."),
             ("In the two ears", "The ears are not named in card 40."),
             ("In the two shoulders", "The shoulders are not named in card 40.")],
            "शूलम् is placed in the two groins (वंक्षणयोः).",
            "वंक्षणयोः शूलम् = pain in the two groins."),
        mcq("apply", 4, "Why does विबद्ध्य (written विबध्य) end in -य and not in -त्वा?",
            ("The root has the prefix वि-", "With a prefix the absolutive takes -य: वि + √बन्ध् → विबध्य, having obstructed."),
            [("The root ends in a vowel", "√बन्ध् ends in a consonant; the -य comes from the prefix."),
             ("It is a passive verb", "विबध्य is an absolutive, not a finite passive verb."),
             ("-य marks the plural", "-य marks no number; it is the absolutive after a prefix.")],
            "Prefix + root → absolutive in -य: विबध्य.",
            "Absolutive: -त्वा without a prefix, -य with one."),
        mcq("transfer", 5, "By the pattern of विबध्य (वि + √बन्ध्), what does आरुह्य (आ + √रुह्, climb) mean in a new example?",
            ("Having climbed", "Prefix + root + -य = having done: आरुह्य = having climbed."),
            [("He climbs", "He climbs would be आरोहति; -य after a prefix marks a finished action."),
             ("In order to climb", "That would be the infinitive आरोढुम्; आरुह्य is the absolutive."),
             ("He climbed", "A past finite verb would be आरोहत्; आरुह्य is the absolutive.")],
            "आरुह्य = having climbed, like विबध्य = having obstructed.",
            "Prefix + root + -य = having done.",
            teaches="After a prefix the absolutive ends in -य, not -त्वा: वि + √बन्ध् → विबध्य, having obstructed."),
    ],
}

# ---------------------------------------------------------------- unit 41
AUTHORED["41"] = {
    "title": "श्वासं वा जनयन् वायुः",
    "question": "By card 41, what does vāyu (Vāta) produce, and what does it seize?",
    "rule": ("Or producing breathlessness (श्वासम्), vāyu (वायुः, Vāta), having seized the anus and the groins (गुदवंक्षणौ), "
             "having spread out (वितत्य), having seized the tips of the ribs and the chest (उरः), māruta (मारुतः, Vāta)."),
    "limits": ("Typed prose: no metre question. No main verb: the run (cards 39 to 42) ends in मुष्णाति. "
               "पर्शुक अग्राणि is one compound split by a printed space (flagged): no question on the space or the stem "
               "पर्शुक/पर्शुका (अग्राणि = tips is sure), nor on the number of गुदवंक्षणौ."),
    "explain_hi": ("शृंखला का तीसरा भाग। यहाँ कर्ता दो बार नाम से आता है: पहली पंक्ति में ‘वायुः’, दूसरी में ‘मारुतः’; दोनों एक ही वायु। "
                   "बताए गए कार्य: श्वास (साँस की कठिनाई) उत्पन्न करना, गुदा और वंक्षण को पकड़ना, फैलना, पसलियों के अग्र भागों और वक्ष (उरः) को पकड़ना। "
                   "‘पर्शुक अग्राणि’ के बीच छपा रिक्त स्थान एक समास को तोड़ता है (पाठ-चिह्न); उस पर प्रश्न नहीं। "
                   "‘वायुर्गृहीत्वा’ में उ के बाद का विसर्ग घोष ग से पहले र् बना है।"),
    "hook": "वायु और मारुत: एक ही वायु के दो नाम, बीच में श्वास, गुदा-वंक्षण, पसलियाँ, वक्ष।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "In card 41, what does श्वासम् mean?",
            ("Breathlessness", "श्वास here = breathlessness, difficult breathing."),
            [("Persistent cough", "Cough would be कास; श्वास here is breathlessness."),
             ("Repeated hiccup", "Hiccup would be हिक्का; श्वास here is breathlessness."),
             ("Bouts of vomiting", "Vomiting would be छर्दि; श्वास here is breathlessness.")],
            "श्वासम् = breathlessness, which vāyu may produce.",
            "श्वास = breathlessness."),
        match(1, "Match each word of card 41 to its meaning.",
              [["श्वासम्", "breathlessness"], ["वितत्य", "having spread out"], ["अग्राणि", "tips"],
               ["उरः", "chest"], ["मारुतः", "another name for vāyu (Vāta)"]],
              "श्वासम् = breathlessness, वितत्य = having spread out, अग्राणि = tips, उरः = chest, मारुतः = another name for vāyu (Vāta).",
              "श्वासम्, वितत्य, अग्राणि, उरः, मारुतः."),
        order(2, "Put these parts of card 41 in the printed order.",
              ["श्वासं वा जनयन्", "वायुर्गृहीत्वा", "गुदवंक्षणौ", "वितत्य", "गृहीत्वोरश्च", "मारुतः"],
              "Producing breathlessness, vāyu, having seized anus and groins, having spread out, having seized the chest, māruta.",
              "श्वासं वा जनयन् → वायुर्गृहीत्वा → गुदवंक्षणौ → वितत्य → गृहीत्वोरश्च → मारुतः.",
              role="extend",
              teaches="The subject is named twice, वायुः in line 1 and मारुतः at the end of line 2: two words for the one vāyu (Vāta)."),
        mcq("discriminate", 3, "Card 41 names vāyu (Vāta) with two words. Which pair is it?",
            ("वायुः and मारुतः", "वायुः (line 1) and मारुतः (line 2) both name vāyu (Vāta)."),
            [("श्वासः and मारुतः", "श्वास is breathlessness; only मारुतः names Vāta."),
             ("वायुः and उरः", "उरः is the chest; only वायुः names Vāta."),
             ("वितत्य and वायुः", "वितत्य means having spread out; only वायुः names Vāta.")],
            "वायुः and मारुतः: one subject, two names.",
            "वायु = मारुत = Vāta."),
        mcq("apply", 4, "Which split of गृहीत्वोरश्च in card 41 is right?",
            ("गृहीत्वा + उरः + च", "आ + उ → ओ; ः before च → श्: गृहीत्वोरश्च."),
            [("गृहीत्वा + अरः + च", "आ + अ would print गृहीत्वारश्च, with आ."),
             ("गृहीत्वा + ओरः + च", "आ + ओ would give औ: गृहीत्वौरश्च."),
             ("गृहीत्वो + रः + च", "गृहीत्वो and रः are no words; ओ comes from आ + उ.")],
            "गृहीत्वा (having seized) + उरः (chest) + च (and).",
            "आ + उ → ओ; ः + च → श्च."),
        mcq("transfer", 5, "By the pattern of वायुः + गृहीत्वा → वायुर्गृहीत्वा, how is धेनुः + धावति (the cow runs) joined in a new example?",
            ("धेनुर्धावति", "After उ, a visarga before a voiced sound → र्: धेनुः + धावति → धेनुर्धावति."),
            [("धेनो धावति", "ओ arises from अः before a voiced consonant, not from उः."),
             ("धेनुस्धावति", "स् arises from a visarga before त or थ, not before ध."),
             ("धेनु धावति", "After उ the visarga is not dropped before a voiced sound; it becomes र्.")],
            "धेनुः + धावति = धेनुर्धावति, like वायुः + गृहीत्वा = वायुर्गृहीत्वा.",
            "Visarga after a vowel other than अ/आ, before a voiced sound → र्.",
            teaches="A visarga after a vowel other than अ or आ becomes र् before a voiced sound: वायुः + गृहीत्वा → वायुर्गृहीत्वा."),
    ],
}

# ---------------------------------------------------------------- unit 42
AUTHORED["42"] = {
    "title": "सद्यो मुष्णाति जीवितं",
    "question": "What does card 42 say vāyu (Vāta) does at once, and which signs does line 2 list?",
    "rule": ("सद्यो मुष्णाति जीवितम्: (vāyu) at once steals life; the data takes this verb as closing the run of cards "
             "39 to 42. Line 2: suddenly the burning heat of fever, thirst, fainting and loss of strength."),
    "limits": ("Medium confidence. Printed आन्नत- for उन्नत- (raised eyes) and the missing space before सद्यो are flagged, and "
               "स्तिमित may mean still or moist: no question on either. Line 2 has no verb; the data's notes join it with card 43 "
               "(उपजायते)."),
    "explain_hi": ("यह पंक्ति कार्ड ३९ से चली शृंखला की क्रिया देती है: (वायु) तुरन्त जीवन हर लेता है (सद्यो मुष्णाति जीवितम्)। "
                   "‘स्तिमित’ का अर्थ निश्चल लिया गया, ‘गीला’ भी सम्भव है; ‘उठी आँखों वाला’ अनुमानित पाठ (छपा आन्नत) पर टिका है। इन पर प्रश्न नहीं। "
                   "दूसरी पंक्ति नई सूची आरम्भ करती है: अचानक ज्वर का सन्ताप, तृष्णा, मूर्छा और बल का क्षय; इसकी क्रिया कार्ड ४३ में है। "
                   "‘सद्यो’ में अः घोष व्यंजन म से पहले ओ बना है, और ‘ज्वरसंतापस्तृष्णा’ में विसर्ग त से पहले स् बना है।"),
    "hook": "सद्यो मुष्णाति: शृंखला यहाँ पूरी; फिर ज्वर-सन्ताप, तृष्णा, मूर्छा, बलक्षय।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "In card 42, what does मुष्णाति mean?",
            ("Steals, takes away", "मुष्णाति (√मुष्) = steals: सद्यो मुष्णाति जीवितम्, at once steals life."),
            [("Gives, hands over", "Gives would be ददाति; मुष्णाति means steals."),
             ("Guards, keeps safe", "Guards would be रक्षति; मुष्णाति means steals."),
             ("Grows, swells up", "Grows would be वर्धते; मुष्णाति means steals.")],
            "मुष्णाति = steals, takes away.",
            "√मुष् = steal."),
        order(1, "Put the words of card 42, line 2, in the printed order.",
              ["सहसा", "ज्वरसंतापः", "तृष्णा", "मूर्च्छा", "बलक्षयः"],
              "Suddenly: burning heat of fever, thirst, fainting, loss of strength.",
              "सहसा → ज्वरसंतापः → तृष्णा → मूर्च्छा → बलक्षयः."),
        match(2, "Match each word of card 42 to its meaning.",
              [["सद्यः", "at once"], ["जीवितम्", "life"], ["ज्वरसन्तापः", "burning heat of fever"],
               ["मूर्च्छा", "fainting"], ["बलक्षयः", "loss of strength"]],
              "सद्यः = at once, जीवितम् = life, ज्वरसन्तापः = burning heat of fever, मूर्च्छा = fainting, बलक्षयः = loss of strength.",
              "सद्यः, जीवितम्, ज्वरसन्तापः, मूर्च्छा, बलक्षयः.", role="extend",
              teaches="बलक्षयः = बल (strength) + क्षय (loss): a tatpuruṣa, 'loss of strength'."),
        mcq("discriminate", 3, "Why is सद्यः printed सद्यो before मुष्णाति in card 42?",
            ("अः before a voiced consonant → ओ", "म is a voiced consonant: सद्यः + मुष्णाति → सद्यो मुष्णाति."),
            [("Every ः before a consonant → ओ", "Not every: before त it becomes स्, as in ज्वरसंतापस्तृष्णा (line 2)."),
             ("सद्यो is the word's own form", "The word is सद्यः; the ओ comes from the visarga by sandhi."),
             ("अः before any vowel → ओ", "मुष्णाति begins with a consonant; before vowels other than अ, अः becomes अ.")],
            "सद्यः + मुष्णाति → सद्यो मुष्णाति.",
            "अः before a voiced consonant → ओ."),
        mcq("apply", 4, "Which split of ज्वरसंतापस्तृष्णा in card 42 is right?",
            ("ज्वरसन्तापः + तृष्णा", "ः before त → स्: ज्वरसन्तापः + तृष्णा → ज्वरसन्तापस्तृष्णा."),
            [("ज्वरसन्ताप + स्तृष्णा", "स्तृष्णा is no word; the स् comes from the visarga."),
             ("ज्वरसन्तापाः + तृष्णा", "आः + त would print -तापास्तृष्णा, with आ."),
             ("ज्वरसन्तापे + तृष्णा", "ए + त would print ज्वरसन्तापे तृष्णा, with no स्.")],
            "ज्वरसन्तापः (fever-heat) + तृष्णा (thirst).",
            "ः before त → स्."),
        mcq("transfer", 5, "By the pattern of सद्यः + मुष्णाति → सद्यो मुष्णाति, how is देवः + ददाति (the god gives) joined in a new example?",
            ("देवो ददाति", "अः before the voiced consonant द → ओ: देवो ददाति."),
            [("देवर्ददाति", "र् comes from a visarga after vowels other than अ/आ; after अ it is ओ."),
             ("देव ददाति", "अः loses only its visarga before vowels other than अ; before a voiced consonant it is ओ."),
             ("देवस्ददाति", "स् comes from a visarga before त or थ, not before द.")],
            "देवः + ददाति = देवो ददाति, like सद्यः + मुष्णाति = सद्यो मुष्णाति.",
            "अः before a voiced consonant → ओ.",
            teaches="अः before a voiced consonant becomes ओ: सद्यः + मुष्णाति → सद्यो मुष्णाति."),
    ],
}

# ---------------------------------------------------------------- unit 43
AUTHORED["43"] = {
    "title": "विश्लेषणं च संधीनां",
    "question": "By card 43, what arises in one about to die, and what is said of sweat at daybreak?",
    "rule": ("And loosening of the joints (सन्धीनां विश्लेषणम्) arises (उपजायते) in one about to die (मुमूर्षोः), with the "
             "signs of card 42, line 2. Line 2: he from whose face sweat drips profusely (भृशम्) at daybreak (गोसर्गे)."),
    "limits": ("High confidence. Line 1 appears (data's grouping) to complete the statement begun in card 42, line 2. Line 2 has no main clause here: the data "
               "takes 'तस्य जीवितम्' of card 44 as its end. वदन is taken as the face (it can also mean the mouth)."),
    "explain_hi": ("पहली पंक्ति कार्ड ४२ की दूसरी पंक्ति की सूची पूरी करती है: ज्वर-सन्ताप, तृष्णा, मूर्छा, बलक्षय और सन्धियों का ढीला होना "
                   "मुमूर्षु (मरणासन्न) में उत्पन्न होते हैं (उपजायते)। ‘उपजायते’ -यते पर समाप्त होता है, पर कर्मवाच्य नहीं; √जन् का यही रूप ‘उत्पन्न होता है’ है। "
                   "दूसरी पंक्ति नया वाक्य खोलती है: जिसके मुख से गोसर्ग (प्रभात; शब्दशः गायों के छूटने का समय) में बहुत पसीना टपकता है; "
                   "डेटा के अनुसार वाक्य कार्ड ४४ (‘तस्य जीवितम्’) में पूरा होता है।"),
    "hook": "सन्धियाँ ढीली, और गोसर्ग में मुख से भृश स्वेद।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "In card 43, what does गोसर्गे mean?",
            ("At daybreak", "गोसर्ग, literally 'release of the cows', is the early-morning time: at daybreak."),
            [("At midnight", "Midnight would be अर्धरात्रे; गोसर्ग is daybreak."),
             ("At sunset", "Sunset would be सायम्; गोसर्ग is daybreak."),
             ("At midday", "Midday would be मध्याह्ने; गोसर्ग is daybreak.")],
            "गोसर्गे = at daybreak (standard sense).",
            "गोसर्ग = daybreak."),
        match(1, "Match each word of card 43 to its meaning.",
              [["विश्लेषणम्", "loosening"], ["सन्धीनाम्", "of the joints"], ["मुमूर्षोः", "of one about to die"],
               ["स्वेदः", "sweat"], ["भृशम्", "profusely"]],
              "विश्लेषणम् = loosening, सन्धीनाम् = of the joints, मुमूर्षोः = of one about to die, स्वेदः = sweat, भृशम् = profusely.",
              "विश्लेषणम्, सन्धीनाम्, मुमूर्षोः, स्वेदः, भृशम्."),
        fill(2, "In card 43, the word for 'sweat' is ____ (type it in Devanagari or in English letters, e.g. dharma).",
             accepts("स्वेदः", "svedaḥ", "स्वेद", "svedah"),
             "स्वेदः = sweat: स्वेदः प्रच्यवते भृशम्, sweat drips profusely.",
             "स्वेद means sweat; स्वेदः is its nominative singular, the subject of प्रच्यवते.",
             "स्वेदः = sweat."),
        mcq("discriminate", 3, "Which split of वदनाद्यस्य in card 43 is right?",
            ("वदनात् + यस्य", "त् before the voiced य → द्: वदनात् + यस्य → वदनाद्यस्य."),
            [("वदनात् + अस्य", "That would print वदनादस्य, without य."),
             ("वदना + द्यस्य", "द्यस्य is no word; the द् comes from त्."),
             ("वदने + अद्यस्य", "ए + अ would print वदनेऽद्यस्य, with ए.")],
            "वदनात् (from the face) + यस्य (of whom).",
            "त् before a voiced sound → द्."),
        mcq("apply", 4, "What kind of form is उपजायते in card 43?",
            ("Present: it arises", "उप + √जन्, 3 sg. present: arises. It ends in -यते but is not a passive."),
            [("Optative: it should arise", "The optative would be उपजायेत; उपजायते is present."),
             ("Past: it arose", "A past form would be उपाजायत; उपजायते is present."),
             ("Future: it will arise", "The future would be उपजनिष्यते; उपजायते is present.")],
            "उपजायते = arises (present); जायते is not passive though it ends in -यते.",
            "-यते is not always passive (जायते, मन्यते)."),
        mcq("transfer", 5, "By the pattern of मुमूर्षोः + उपजायते → मुमूर्षोरुपजायते, how is भानोः + उदयः (the sun's rising) joined in a new example?",
            ("भानोरुदयः", "After ओ, a visarga before a vowel → र्: भानोः + उदयः → भानोरुदयः."),
            [("भानवुदयः", "अव् comes from ओ with no visarga; ओः before a vowel gives ओर्."),
             ("भानो उदयः", "After ओ the visarga is not dropped before a vowel; it becomes र्."),
             ("भानोदयः", "The उ of उदयः does not vanish; the visarga becomes र्.")],
            "भानोः + उदयः = भानोरुदयः, like मुमूर्षोः + उपजायते = मुमूर्षोरुपजायते.",
            "Visarga after ओ before a vowel or voiced consonant → र्.",
            teaches="A visarga after ओ becomes र् before a vowel: मुमूर्षोः + उपजायते → मुमूर्षोरुपजायते."),
    ],
}

# ---------------------------------------------------------------- unit 44
AUTHORED["44"] = {
    "title": "दुर्लभं तस्य जीवितं",
    "question": "What does card 44 say of the life of the one in card 43, and how does line 2 describe the masūrikā?",
    "rule": ("दुर्लभं तस्य जीवितम्: his life is hard to obtain; तस्य picks up the यस्य of card 43 (the data's grouping). Line 2: "
             "he on whose body (गात्रे) there are masūrikā (lentil-like eruptions, probably a pox-type disease) looking like "
             "coral pellets."),
    "limits": ("Medium confidence. In लेपज्वरोपतनस्य the reading 'upatapta' (afflicted) is a conjecture, and what lepa-jvara is, is "
               "disputed: no question on either. Line 2 has no verb; the data says it goes on in card 45. प्रबाल is printed for "
               "प्रवाल (coral). That masūrikā is a pox-type disease is only probable."),
    "explain_hi": ("पहली पंक्ति कार्ड ४३ के वाक्य को पूरा करती है: उसका जीवन दुर्लभ है (दुर्लभं तस्य जीवितम्); ‘तस्य’ कार्ड ४३ के ‘यस्य’ का उत्तर है। "
                   "‘लेपज्वरोपतनस्य’ में ‘उपतप्त’ (पीड़ित) अनुमानित पाठ है और लेपज्वर की पहचान विवादित है; इन पर प्रश्न नहीं। "
                   "दूसरी पंक्ति नया वाक्य खोलती है: जिसके शरीर पर प्रवाल (मूँगे) की गोलियों जैसी दिखने वाली मसूरिकाएँ हों। "
                   "मसूरिका = मसूर के दाने जैसी फुंसियाँ, सम्भवतः चेचक जैसा रोग (सम्भावित, डेटा का लेबल)। वाक्य कार्ड ४५ में आगे चलता है।"),
    "hook": "दुर्लभं जीवितम्; फिर मूँगे की गोलियों जैसी मसूरिकाएँ।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "In card 44, what does दुर्लभम् mean?",
            ("Hard to obtain", "दुर्-लभ = hard to obtain: दुर्लभं तस्य जीवितम्."),
            [("Easy to come by", "Easy to come by would be सुलभ; दुर्- means hard."),
             ("Already lost", "Lost would be नष्ट; दुर्लभ means hard to obtain."),
             ("Quite certain", "Certain would be निश्चित; दुर्लभ means hard to obtain.")],
            "दुर्लभम् = hard to obtain.",
            "दुर्- = hard, लभ = obtaining."),
        match(1, "Match each word of card 44 to its meaning.",
              [["दुर्लभम्", "hard to obtain"], ["जीवितम्", "life"], ["गात्रे", "on the body"],
               ["गुलिका", "pellet, small ball"], ["प्रबाल", "coral (printed for प्रवाल)"]],
              "दुर्लभम् = hard to obtain, जीवितम् = life, गात्रे = on the body, गुलिका = pellet, प्रबाल = coral.",
              "दुर्लभम्, जीवितम्, गात्रे, गुलिका, प्रबाल."),
        order(2, "Put these sure parts of card 44 in the printed order.",
              ["दुर्लभं", "तस्य", "जीवितं", "प्रबालगुलिकाभासा", "यस्य गात्रे", "मसूरिकाः"],
              "His life is hard to obtain; he on whose body there are masūrikā looking like coral pellets.",
              "दुर्लभं → तस्य → जीवितं → प्रबालगुलिकाभासा → यस्य गात्रे → मसूरिकाः.",
              role="extend",
              teaches="तस्य (his) answers the यस्य (whose) of card 43; the यस्य of line 2 opens a new relative clause."),
        mcq("discriminate", 3, "Why is -आभासाः printed -आभासा before यस्य in card 44?",
            ("After आ, ः drops before a voiced sound", "य is voiced: -आभासाः + यस्य → -आभासा यस्य."),
            [("Every ः drops before a consonant", "Not every: स्वेदः प्रच्यवते (card 43) keeps it before प."),
             ("After आ, ः before य becomes र्", "र् comes after vowels other than अ/आ; after आ the visarga drops."),
             ("आः before a voiced sound gives ओ", "ओ comes from अः, not from आः.")],
            "आः before a voiced sound loses its visarga.",
            "आः + voiced sound → आ."),
        mcq("apply", 4, "By the data of card 44, what does the name masūrikā point to?",
            ("Lentil-like eruptions", "masūra = lentil: masūrikā are lentil-like eruptions, probably a pox-type disease."),
            [("Cracks of the lips", "No lips are named in card 44."),
             ("Swellings of the eyes", "No eyes are named in card 44."),
             ("Pellets of coral", "Coral pellets give their look (प्रबालगुलिकाभासा), not the name.")],
            "मसूरिका = lentil-like eruptions (probably pox-type).",
            "मसूर = lentil → मसूरिका."),
        mcq("transfer", 5, "By the pattern of गुलिका + आभासाः → गुलिकाभासाः, how is विद्या + आलयः (a school) joined in a new example?",
            ("विद्यालयः", "आ + आ → आ: विद्या + आलयः → विद्यालयः."),
            [("विद्येलयः", "ए comes from आ + इ, not from आ + आ."),
             ("विद्यौलयः", "औ comes from आ + ओ or औ, not from आ + आ."),
             ("विद्यलयः", "The two long आs merge into one आ; it cannot become short.")],
            "विद्या + आलयः = विद्यालयः, like गुलिका + आभासाः = गुलिकाभासाः.",
            "आ + आ → आ.",
            teaches="आ + आ merge into one आ: गुलिका + आभासाः → गुलिकाभासाः."),
    ],
}

# ---------------------------------------------------------------- unit 45
AUTHORED["45"] = {
    "title": "उत्पद्याशु विनश्यंति",
    "question": "By card 45, what happens to what has arisen, what is said of 'him', and what do the next words resemble?",
    "rule": ("Having arisen, (they) quickly vanish (उत्पद्याशु विनश्यन्ति); not after long, he perishes (न चिरात् स विनश्यति). "
             "Line 2: resembling split lentils (मसूरविदलप्रख्याः) and likewise resembling coral (विद्रुमसन्निभाः)."),
    "limits": ("The plural subject of विनश्यन्ति is not stated (probably the eruptions of card 44): no question names it. Line 2 "
               "describes nouns not in this unit; the data says they appear to be the blisters (विस्फोटाः) of card 46. Printed ळ "
               "in विदळ is a print habit (= विदल)."),
    "explain_hi": ("कार्ड ४४ का वाक्य यहाँ पूरा होता है: (वे) उत्पन्न होकर शीघ्र नष्ट हो जाते हैं, और वह (रोगी) देर से नहीं, थोड़े ही समय में नष्ट होता है। "
                   "‘विनश्यन्ति’ का बहुवचन कर्ता छपा नहीं; डेटा के अनुसार सम्भवतः कार्ड ४४ की मसूरिकाएँ। ‘न चिरात्’ = देर के बाद नहीं, यानी शीघ्र। "
                   "दूसरी पंक्ति में दो उपमाएँ हैं: मसूर की फाड़ी के समान और मूँगे (विद्रुम) के समान; डेटा के अनुसार ये कार्ड ४६ के विस्फोटों के विशेषण लगते हैं। "
                   "‘उत्पद्याशु’ में उत्पद्य + आशु की सन्धि है (अ + आ → आ)।"),
    "hook": "उठीं और शीघ्र मिटीं; वह भी न चिरात्। फिर मसूर-दल और विद्रुम जैसी।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "In card 45, what does आशु mean?",
            ("Quickly", "आशु = quickly: उत्पद्याशु विनश्यन्ति, having arisen they quickly vanish."),
            [("Slowly", "Slowly would be शनैः; आशु means quickly."),
             ("Rarely", "Rarely would be कदाचित्; आशु means quickly."),
             ("Repeatedly", "Repeatedly would be मुहुः; आशु means quickly.")],
            "आशु = quickly.",
            "आशु = quickly."),
        order(1, "Put the words of card 45, line 1, in the printed order.",
              ["उत्पद्य", "आशु", "विनश्यंति", "न चिरात्", "स विनश्यति"],
              "Having arisen, quickly they vanish; not after long he perishes.",
              "उत्पद्य → आशु → विनश्यंति → न चिरात् → स विनश्यति."),
        match(2, "Match each word of card 45 to its meaning.",
              [["उत्पद्य", "having arisen"], ["आशु", "quickly"], ["न चिरात्", "before long"],
               ["विदल", "split"], ["विद्रुम", "coral"], ["सन्निभ", "resembling"]],
              "उत्पद्य = having arisen, आशु = quickly, न चिरात् = before long, विदल = split, विद्रुम = coral, सन्निभ = resembling.",
              "उत्पद्य, आशु, न चिरात्, विदल, विद्रुम, सन्निभ.", role="extend",
              teaches="न चिरात् = 'not after a long time', i.e. soon: चिरात् is an ablative used as an adverb."),
        mcq("discriminate", 3, "In card 45, which word says that 'he' perishes?",
            ("विनश्यति", "3rd singular: स विनश्यति, he perishes."),
            [("विनश्यन्ति", "3rd plural: they vanish, said of what has arisen."),
             ("उत्पद्य", "An absolutive: having arisen."),
             ("चिरात्", "An adverb: after a long time.")],
            "विनश्यति (sg.) is said of him; विनश्यन्ति (pl.) of what has arisen.",
            "-ति = 3 sg.; -न्ति = 3 pl."),
        multi("apply", 4, "Which comparisons does line 2 of card 45 make?",
              [("Like grains of rice", "No: rice is not named in card 45."),
               ("Like split lentils", "Right: मसूरविदलप्रख्याः, resembling split lentils."),
               ("Like crushed pearls", "No: pearls are not named in card 45."),
               ("Like coral", "Right: विद्रुमसन्निभाः, resembling coral.")],
              [1, 3],
              "Line 2 compares to split lentils and to coral.",
              "मसूरविदल-प्रख्याः, विद्रुम-सन्निभाः."),
        mcq("transfer", 5, "By the pattern of उत्पद्य + आशु → उत्पद्याशु, how is सूर्य + आलोकः (sunlight) joined in a new example?",
            ("सूर्यालोकः", "अ + आ → आ: सूर्य + आलोकः → सूर्यालोकः."),
            [("सूर्यलोकः", "The long आ of आलोकः cannot vanish; अ + आ → आ."),
             ("सूर्येलोकः", "ए comes from अ + इ or ई, not from अ + आ."),
             ("सूर्यौलोकः", "औ comes from अ + ओ or औ, not from अ + आ.")],
            "सूर्य + आलोकः = सूर्यालोकः, like उत्पद्य + आशु = उत्पद्याशु.",
            "अ + आ → आ.",
            teaches="अ + आ merge into आ: उत्पद्य + आशु → उत्पद्याशु."),
    ],
}

# ---------------------------------------------------------------- unit 46
AUTHORED["46"] = {
    "title": "विस्फोटा देहनाशनाः",
    "question": "Which blisters does card 46 call body-destroying, and which signs of the eyes, face and temples follow?",
    "rule": ("Blisters (विस्फोटाः) with the mouth turned inward (अन्तर्वक्त्र) and looking like kiṇa (probably a scar or "
             "callus) are body-destroying (देहनाशनाः). Line 2: jaundice (कामला) in the two eyes, the face full (मुखं पूर्णम्), "
             "loss of flesh in the two temples (शङ्खयोः)."),
    "limits": ("What kiṇa is, is uncertain: no question on its sense (the sandhi किणाभाः + च is sure). Printed अंतर्वक्त्रा "
               "probably lacks a visarga (flagged): no question on it. Line 2 has no verb (completed in card 47, data). "
               "कामला अक्ष्णोः may be one compound; the case of अक्ष्णोः is open."),
    "explain_hi": ("पहली पंक्ति में देह का नाश करने वाले विस्फोट (फफोले) बताए गए: भीतर की ओर मुख वाले और किण के समान दिखने वाले; "
                   "किण सम्भवतः घट्टा या चोट का निशान है, पहचान अनिश्चित, इसलिए उस पर प्रश्न नहीं। "
                   "डेटा के अनुसार कार्ड ४५ की दूसरी पंक्ति की उपमाएँ भी इन्हीं विस्फोटों की लगती हैं। "
                   "दूसरी पंक्ति नए लक्षण देती है: दोनों आँखों में कामला (पीलिया, मानक), मुख भरा हुआ, और दोनों शंख (कनपटियों) में मांस छूट जाना; "
                   "डेटा के अनुसार यह वाक्य कार्ड ४७ (‘यस्य तं परिवर्जयेत्’) में पूरा होता है।"),
    "hook": "भीतर-मुखी विस्फोट; आँखें पीली, मुख भरा, कनपटियों का मांस छूटा।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "In card 46, what does कामला mean?",
            ("Jaundice", "कामला = jaundice (standard), here in the two eyes."),
            [("Swelling", "Swelling would be शोथ; कामला is jaundice."),
             ("Fainting", "Fainting is मूर्च्छा (card 42); कामला is jaundice."),
             ("Coughing", "Cough would be कास; कामला is jaundice.")],
            "कामला = jaundice.",
            "कामला = jaundice."),
        order(1, "Put these parts of card 46 in the printed order.",
              ["अंतर्वक्त्रा", "किणाभाश्च", "विस्फोटा देहनाशनाः", "कामलाऽक्ष्णोः", "मुखंपूर्णं", "शंखयोर्मुक्तमांसता"],
              "Inward-mouthed, kiṇa-like, body-destroying blisters; jaundice in the eyes; face full; loss of flesh in the temples.",
              "अंतर्वक्त्रा → किणाभाश्च → विस्फोटा देहनाशनाः → कामलाऽक्ष्णोः → मुखंपूर्णं → शंखयोर्मुक्तमांसता."),
        match(2, "Match each word of card 46 to its meaning.",
              [["विस्फोटाः", "blisters"], ["देहनाशनाः", "body-destroying"], ["कामला", "jaundice"],
               ["शङ्खयोः", "in the two temples"], ["मुक्तमांसता", "loss of flesh"]],
              "विस्फोटाः = blisters, देहनाशनाः = body-destroying, कामला = jaundice, शङ्खयोः = in the two temples, मुक्तमांसता = loss of flesh.",
              "विस्फोटाः, देहनाशनाः, कामला, शङ्खयोः, मुक्तमांसता.", role="extend",
              teaches="मुक्तमांसता = मुक्त-मांस (flesh shed) + -ता (state of): the state of having shed flesh."),
        mcq("discriminate", 3, "By card 46, where is the loss of flesh (मुक्तमांसता)?",
            ("In the two temples", "शङ्खयोर्मुक्तमांसता: loss of flesh in the two temples."),
            [("In the two eyes", "The two eyes have jaundice, not loss of flesh."),
             ("In the whole face", "The face is called full (मुखं पूर्णम्)."),
             ("In the two calves", "No calves are named in card 46.")],
            "Eyes: jaundice; face: full; temples: loss of flesh.",
            "शङ्खयोः मुक्तमांसता."),
        mcq("apply", 4, "Which split of शंखयोर्मुक्तमांसता in card 46 is right?",
            ("शङ्खयोः + मुक्तमांसता", "ओः before the voiced म → ओर्: शङ्खयोर्मुक्तमांसता."),
            [("शङ्खयोः + अमुक्तमांसता", "That would print -योरमुक्त-, with र and अ."),
             ("शङ्ख + योर्मुक्तमांसता", "योर्मुक्तमांसता is no word; -योः is the dual ending."),
             ("शङ्खयो + र्मुक्तमांसता", "र्मुक्तमांसता is no word; the र् comes from the visarga.")],
            "शङ्खयोः (in the two temples) + मुक्तमांसता (loss of flesh).",
            "ओः before a voiced sound → ओर्."),
        mcq("transfer", 5, "By the pattern of किणाभाः + च → किणाभाश्च, how is वृक्षाः + च (and trees) joined in a new example?",
            ("वृक्षाश्च", "ः before च → श्: वृक्षाः + च → वृक्षाश्च."),
            [("वृक्षास्च", "स् comes from a visarga before त or थ, not before च."),
             ("वृक्षा च", "आः drops its visarga only before a voiced sound; च is unvoiced."),
             ("वृक्षार्च", "र् comes after vowels other than अ/आ, and only before a voiced sound.")],
            "वृक्षाः + च = वृक्षाश्च, like किणाभाः + च = किणाभाश्च.",
            "ः before च or छ → श्.",
            teaches="A visarga before च becomes श्: किणाभाः + च → किणाभाश्च."),
    ],
}

# ---------------------------------------------------------------- unit 47
AUTHORED["47"] = {
    "title": "यस्य तं परिवर्जयेत्",
    "question": "By card 47, line 1, which further signs are named, and what does the text say of such a one?",
    "rule": ("He in whom there is fright (सन्त्रासः) and heat in the body (उष्णता अङ्गे), him one should avoid "
             "(तं परिवर्जयेत्): by the data's grouping this appears to complete the sentence of card 46, line 2. The sense of line 2 is doubtful."),
    "limits": ("Low confidence. Line 2 (अकस्मादनुधावच्च विघृष्टं त्वक्समाश्रयं) is given literally; its neuter forms do not agree "
               "with card 49's wounds (व्रणाः), which the list from here to card 49, line 1, appears to describe (unresolved in the data): no question on line 2. The agent of "
               "परिवर्जयेत् is unstated."),
    "explain_hi": ("पहली पंक्ति कार्ड ४६ की दूसरी पंक्ति का वाक्य पूरा करती है: जिसमें (उन लक्षणों के साथ) भय (सन्त्रास) और शरीर में उष्णता हो, "
                   "उसे त्याग देना चाहिए (तं परिवर्जयेत्)। त्यागने वाला कौन, यह छपा नहीं। "
                   "दूसरी पंक्ति का अर्थ सन्दिग्ध है: ‘अचानक, पीछे दौड़ता हुआ, रगड़ा हुआ, त्वचा में आश्रित’ शब्दशः दिया गया है, और इसके नपुंसक रूप "
                   "कार्ड ४९ के ‘व्रणाः’ से मेल नहीं खाते। इसलिए इस पंक्ति पर कोई प्रश्न नहीं। "
                   "‘उष्णतांगे’ में उष्णता + अङ्गे की सन्धि है (आ + अ → आ)।"),
    "hook": "भय और देह में ताप: तं परिवर्जयेत्।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "In card 47, what does सन्त्रासः mean?",
            ("Fright, terror", "सन्त्रासः = fright, terror."),
            [("Thirst, craving", "Thirst would be तृष्णा; सन्त्रास is fright."),
             ("Sweat, moisture", "Sweat would be स्वेद; सन्त्रास is fright."),
             ("Pain, aching", "Pain would be शूल or रुजा; सन्त्रास is fright.")],
            "सन्त्रासः = fright.",
            "सन्त्रास = fright."),
        order(1, "Put the words of card 47, line 1, in the printed order.",
              ["सन्त्रासः", "उष्णता", "अङ्गे", "यस्य", "तं परिवर्जयेत्"],
              "Fright, and heat in the body: of whom; him one should avoid.",
              "सन्त्रासः → उष्णता → अङ्गे → यस्य → तं परिवर्जयेत्."),
        match(2, "Match each word of card 47, line 1, to its meaning.",
              [["सन्त्रासः", "fright"], ["उष्णता", "heat"], ["अङ्गे", "in the body"], ["तम्", "him"],
               ["परिवर्जयेत्", "one should avoid"]],
              "सन्त्रासः = fright, उष्णता = heat, अङ्गे = in the body, तम् = him, परिवर्जयेत् = one should avoid.",
              "सन्त्रासः, उष्णता, अङ्गे, तम्, परिवर्जयेत्.", role="extend",
              teaches="उष्णता = उष्ण (hot) + -ता (state of): heat as a state."),
        mcq("discriminate", 3, "Which split of उष्णतांगे in card 47 is right?",
            ("उष्णता + अङ्गे", "आ + अ → आ: उष्णता + अङ्गे → उष्णताङ्गे, printed उष्णतांगे."),
            [("उष्णताम् + अङ्गे", "म् + अ would print उष्णतामङ्गे, with म."),
             ("उष्णते + अङ्गे", "ए + अ would print उष्णतेऽङ्गे, with ए."),
             ("उष्णतां + गे", "गे is no word; the ं stands for the ङ् of अङ्गे.")],
            "उष्णता (heat) + अङ्गे (in the body).",
            "आ + अ → आ."),
        mcq("apply", 4, "In card 47, what kind of form is परिवर्जयेत्?",
            ("Optative: one should avoid", "3 sg. optative of परि + √वृज् (10th class): one should avoid."),
            [("Past: one avoided", "A past form would need the augment अ- or a past participle."),
             ("Future: one will avoid", "The future would be परिवर्जयिष्यति."),
             ("Absolutive: having avoided", "The absolutive would be परिवर्ज्य.")],
            "परिवर्जयेत् = one should avoid (optative).",
            "-एत् here marks the optative (not every optative ends so, e.g. ब्रूयात्)."),
        mcq("transfer", 5, "By the pattern of परिवर्जयेत् (one should avoid), what does रक्षेत् mean in a new example?",
            ("One should protect", "-एत् on an अ-stem verb = optative: रक्षेत्, one should protect."),
            [("He protected", "A past form would be अरक्षत्; -एत् marks the optative."),
             ("Having protected", "That would be रक्षित्वा; -एत् marks the optative."),
             ("He will protect", "That would be रक्षिष्यति; -एत् marks the optative.")],
            "रक्षेत् = one should protect, like परिवर्जयेत् = one should avoid.",
            "-एत् on an अ-stem verb = optative 'one should'.",
            teaches="-एत् on a verb with an अ-stem marks the optative, 'one should': परिवर्जयेत्. Not every optative ends in -एत् (ब्रूयात्)."),
    ],
}

# ---------------------------------------------------------------- unit 48
AUTHORED["48"] = {
    "title": "गन्ध और प्रभा की सूची",
    "question": "By card 48, which smells and which lustres are listed?",
    "rule": ("Smelling of sandalwood (standard), uśīra (vetiver root, standard), madirā (an intoxicating drink), a corpse and a crow "
             "(-गन्धयः); having the lustre of śaivāla (water-moss; plant disputed), a cock's comb, kuṅkuma (saffron, standard), "
             "āla (probably orpiment) and ink (-प्रभाः)."),
    "limits": ("The noun is not here: by the data, the list from card 47, line 2, to card 49, line 1, appears to describe the wounds (व्रणाः) of card 49 (for card 47 the data leaves this unresolved). "
               "No question on āla (split open) or śaivāla (disputed)."),
    "explain_hi": ("यह इकाई दो लम्बे समासों की सूची है; जिसका वर्णन है वह यहाँ नहीं, डेटा के अनुसार सम्भवतः कार्ड ४९ के व्रण (घाव)। "
                   "पहली पंक्ति गन्ध बताती है: चन्दन (मानक), उशीर यानी खस (मानक), मदिरा (नशीला पेय), कुणप (शव) और ध्वाङ्क्ष (कौआ)। "
                   "दूसरी पंक्ति प्रभा (आभा) बताती है: शैवाल (जल की काई; पहचान विवादित), मुर्गे की कलगी, कुंकुम यानी केसर (मानक), "
                   "आल (सम्भवतः हरताल) और मषी (स्याही)। ‘कुंकुमाल’ को कुंकुम + अल भी पढ़ा जा सकता है, इसलिए आल पर प्रश्न नहीं। "
                   "‘चंदनोशीर’ में चन्दन + उशीर की सन्धि है (अ + उ → ओ)।"),
    "hook": "पहली पंक्ति: नाक से (गन्ध); दूसरी पंक्ति: आँख से (प्रभा)।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "In card 48, what does कुणप mean?",
            ("A corpse", "कुणप = corpse: one of the smells in line 1."),
            [("A crow", "A crow is ध्वाङ्क्ष, the next word; कुणप is a corpse."),
             ("A blue lotus", "A blue lotus would be उत्पल; कुणप is a corpse."),
             ("A flame", "A flame would be ज्वाला; कुणप is a corpse.")],
            "कुणप = corpse.",
            "कुणप = corpse."),
        order(1, "Put the smells of card 48, line 1, in the printed order.",
              ["चंदन", "उशीर", "मदिरा", "कुणप", "ध्वांक्ष"],
              "Sandalwood, uśīra, an intoxicating drink, a corpse, a crow: all closed by -गंधयः.",
              "चंदन → उशीर → मदिरा → कुणप → ध्वांक्ष."),
        match(2, "Match each word of card 48 to its meaning.",
              [["चन्दन", "sandalwood (standard)"], ["उशीर", "vetiver root (standard)"], ["कुणप", "corpse"],
               ["ध्वाङ्क्ष", "crow"], ["कुक्कुटशिखा", "cock's comb"], ["कुङ्कुम", "saffron (standard)"]],
              "चन्दन = sandalwood, उशीर = vetiver root, कुणप = corpse, ध्वाङ्क्ष = crow, कुक्कुटशिखा = cock's comb, कुङ्कुम = saffron.",
              "चन्दन, उशीर, कुणप, ध्वाङ्क्ष, कुक्कुटशिखा, कुङ्कुम.", role="extend",
              teaches="-गन्धयः closes the first list (smells) and -प्रभाः the second (lustres): one end-word governs a whole compound."),
        multi("discriminate", 3, "Which items of card 48 are named for their smell (-गन्धयः)?",
              [("मदिरा", "Right: line 1, closed by -गन्धयः."),
               ("मषी", "No: line 2, a lustre (-प्रभाः)."),
               ("कुणप", "Right: line 1, closed by -गन्धयः."),
               ("कुक्कुटशिखा", "No: line 2, a lustre (-प्रभाः)."),
               ("उशीर", "Right: line 1, closed by -गन्धयः."),
               ("कुंकुम", "No: line 2, a lustre (-प्रभाः).")],
              [0, 2, 4],
              "Line 1 (smells): candana, uśīra, madirā, kuṇapa, dhvāṅkṣa. Line 2 (lustres): śaivāla, cock's comb, kuṅkuma, āla, ink.",
              "-गन्धयः = smelling of; -प्रभाः = having the lustre of."),
        mcq("apply", 4, "Which split of चंदनोशीर in card 48 is right?",
            ("चन्दन + उशीर", "अ + उ → ओ: चन्दन + उशीर → चन्दनोशीर."),
            [("चन्दन + ओशीर", "अ + ओ would give औ: चन्दनौशीर."),
             ("चन्दनम् + उशीर", "म् + उ would print चन्दनमुशीर, with म."),
             ("चन्दनो + शीर", "चन्दनो and शीर are not the words; ओ comes from अ + उ.")],
            "चन्दन (sandalwood) + उशीर (vetiver root).",
            "अ + उ → ओ."),
        mcq("transfer", 5, "By the pattern of चन्दन + उशीर → चन्दनोशीर, how is हिम + उदकम् (cold water) joined in a new example?",
            ("हिमोदकम्", "अ + उ → ओ: हिम + उदकम् → हिमोदकम्."),
            [("हिमौदकम्", "औ comes from अ + ओ or औ, not from अ + उ."),
             ("हिमूदकम्", "अ does not vanish before उ; अ + उ → ओ."),
             ("हिम्वुदकम्", "व् comes from उ before a vowel, not from अ.")],
            "हिम + उदकम् = हिमोदकम्, like चन्दन + उशीर = चन्दनोशीर.",
            "अ + उ → ओ.",
            teaches="अ + उ merge into ओ: चन्दन + उशीर → चन्दनोशीर."),
    ],
}

# ---------------------------------------------------------------- unit 49
AUTHORED["49"] = {
    "title": "प्राणनाशकरा व्रणाः",
    "question": "Which wounds does card 49 call life-destroying, and what is said of the Vāta-born and the Pitta-born one?",
    "rule": ("Wounds (व्रणाः) with inner burning (अन्तर्दाहाः) and without heat (निरूष्माणः) cause the destruction of life "
             "(प्राणनाशकराः). Line 2: the Vāta-born (one) which would not be for pain (न शूलाय), and the Pitta-born which "
             "would not be for burning (न दाहाय)."),
    "limits": ("Line 1 appears to end the list begun in card 47, line 2 (data). Line 2's noun is unstated (probably a wound, see cards 49 and 51); "
               "the sentence goes on into card 50. 'Inner burning, no heat' is as printed; nothing is added about the outside."),
    "explain_hi": ("पहली पंक्ति सम्भवतः कार्ड ४७-४८ की सूची का अन्त है: भीतर दाह वाले, ऊष्मा से रहित, प्राणों का नाश करने वाले व्रण (घाव)। "
                   "बाहर के बारे में कुछ नहीं कहा गया; जैसा छपा है वैसा ही लिया गया। "
                   "दूसरी पंक्ति नया क्रम आरम्भ करती है: जो वातज हो और पीड़ा (शूल) के लिए न हो, और जो पित्तज हो और दाह के लिए न हो; "
                   "संज्ञा छपी नहीं (सम्भवतः व्रण), और वाक्य कार्ड ५० में आगे चलता है। "
                   "‘शूलाय’, ‘दाहाय’ चतुर्थी एकवचन हैं: ‘के लिए’ (प्रयोजन)।"),
    "hook": "भीतर दाह, ऊष्मा नहीं: प्राणनाशक व्रण। वातज बिना शूल, पित्तज बिना दाह।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "In card 49, what does व्रणाः mean?",
            ("Wounds, ulcers", "व्रणाः = wounds, ulcers (m. nom. pl.)."),
            [("Fevers, heats", "Fever would be ज्वर; व्रण is a wound."),
             ("Joints, limbs, parts", "A joint would be सन्धि; व्रण is a wound."),
             ("Signs, marks", "A sign would be लक्षण; व्रण is a wound.")],
            "व्रणाः = wounds.",
            "व्रण = wound, ulcer."),
        match(1, "Match each word of card 49 to its meaning.",
              [["अन्तर्दाहाः", "with inner burning"], ["निरूष्माणः", "without heat"],
               ["प्राणनाशकराः", "causing destruction of life"], ["वातजः", "Vāta-born"], ["पित्तजः", "Pitta-born"],
               ["दाहाय", "for burning"]],
              "अन्तर्दाहाः = with inner burning, निरूष्माणः = without heat, प्राणनाशकराः = causing destruction of life, "
              "वातजः = Vāta-born, पित्तजः = Pitta-born, दाहाय = for burning.",
              "अन्तर्दाहाः, निरूष्माणः, प्राणनाशकराः, वातजः, पित्तजः, दाहाय."),
        fill(2, "In card 49, the word for 'for pain' is ____ (type it in Devanagari or in English letters, e.g. dharma).",
             accepts("शूलाय", "śūlāya", "shulaya"),
             "शूलाय = for pain: यो वातजो न शूलाय, the Vāta-born which would not be for pain.",
             "-आय is the dative singular of an अ-stem: here it says 'for' (purpose).",
             "शूलाय = for pain."),
        mcq("discriminate", 3, "By card 49, what is said of the Pitta-born one?",
            ("It would not be for burning", "स्यान्न दाहाय पित्तजः: the Pitta-born one which would not be for burning."),
            [("It would not be for pain", "That is said of the Vāta-born one (न शूलाय)."),
             ("It would not be for swelling", "No swelling is named in card 49."),
             ("It would not be for pus", "Card 49 says nothing of pus for the Pitta-born one.")],
            "Vāta-born: not for pain; Pitta-born: not for burning.",
            "वातजः न शूलाय; पित्तजः न दाहाय."),
        mcq("apply", 4, "Which split of स्यान्नदाहाय in card 49 is right?",
            ("स्यात् + न + दाहाय", "त् before the nasal न may become न् (optional; स्याद् न is also correct)."),
            [("स्यात् + अन्नदाहाय", "That would print स्यादन्नदाहाय, with द and अ."),
             ("स्या + न्नदाहाय", "न्नदाहाय is no word; the first न् comes from त्."),
             ("स्यान्न + दाहाय", "स्यान्न is no word; it is स्यात् + न.")],
            "स्यात् (would be) + न (not) + दाहाय (for burning).",
            "त् before a nasal may become न् (optional; द् also correct)."),
        mcq("transfer", 5, "By the pattern of शूलाय (for pain), what does ज्ञानाय mean in a new example?",
            ("For knowledge", "-आय = dative singular: ज्ञानाय, for knowledge."),
            [("By knowledge", "By knowledge would be ज्ञानेन (instrumental)."),
             ("Of knowledge", "Of knowledge would be ज्ञानस्य (genitive)."),
             ("In knowledge", "In knowledge would be ज्ञाने (locative).")],
            "ज्ञानाय = for knowledge, like शूलाय = for pain.",
            "अ-stem + -आय = dative singular, 'for'.",
            teaches="-आय is the dative singular of an अ-stem noun, 'for (the sake of)': शूलाय, दाहाय."),
    ],
}

# ---------------------------------------------------------------- unit 50
AUTHORED["50"] = {
    "title": "कफजो न च पूयाय",
    "question": "By card 50, what would the Kapha-born and the marma-born one not be for, and how is something seen?",
    "rule": ("The Kapha-born (one) which would not be for pus (न पूयाय), and the marma-born (marma = a vital spot) which would not "
             "be for pain (रुजे न). Line 2: where one without powder (अचूर्णः) looks as if strewn with powder (चूर्णकीर्णाभः) "
             "and is suddenly seen (अकस्मात् दृश्यते)."),
    "limits": ("The noun and the verb of line 1 are carried from card 49 and not supplied. The noun of line 2 is not stated "
               "(probably a wound) and the data says it continues in card 51. Marma is a doctrinal term: no modern equivalent."),
    "explain_hi": ("कार्ड ४९ का क्रम पूरा होता है: जो कफज हो और पूय (पीब) के लिए न हो, और जो मर्मज हो (मर्म = जीवन-स्थल) और पीड़ा (रुजा) के लिए न हो। "
                   "संज्ञा और क्रिया कार्ड ४९ से आती हैं, यहाँ छपी नहीं। "
                   "दूसरी पंक्ति: जहाँ (कोई, सम्भवतः व्रण) चूर्ण से रहित होकर भी चूर्ण बिखरा हुआ-सा दिखे, और अचानक दिखाई दे; डेटा के अनुसार यह कार्ड ५१ में आगे चलता है। "
                   "‘यत्राकस्माच्च’ में यत्र + अकस्मात् (अ + अ → आ) और अकस्मात् + च (त् + च → च्च) की सन्धियाँ हैं।"),
    "hook": "कफज बिना पूय, मर्मज बिना रुजा; बिना चूर्ण के चूर्ण-सा दिखे।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "In card 50, what does पूयाय mean?",
            ("For pus", "पूयाय = for pus (m. dat. sg.)."),
            [("For blood", "Blood would be रक्त; पूय is pus."),
             ("For sweat", "Sweat would be स्वेद; पूय is pus."),
             ("For fever", "Fever would be ज्वर; पूय is pus.")],
            "पूयाय = for pus.",
            "पूय = pus."),
        order(1, "Put these parts of card 50 in the printed order.",
              ["कफजो", "न च पूयाय", "मर्मजश्च", "रुजे न यः", "अचूर्णश्चूर्णकीर्णाभो", "यत्राकस्माच्च दृश्यते"],
              "Kapha-born, not for pus; marma-born, not for pain; without powder, looking powder-strewn; where suddenly seen.",
              "कफजो → न च पूयाय → मर्मजश्च → रुजे न यः → अचूर्णश्चूर्णकीर्णाभो → यत्राकस्माच्च दृश्यते."),
        match(2, "Match each word of card 50 to its meaning.",
              [["कफजः", "Kapha-born"], ["पूयाय", "for pus"], ["मर्मजः", "born at a vital spot"],
               ["रुजे", "for pain"], ["अचूर्णः", "without powder"], ["दृश्यते", "is seen"]],
              "कफजः = Kapha-born, पूयाय = for pus, मर्मजः = born at a vital spot, रुजे = for pain, अचूर्णः = without powder, दृश्यते = is seen.",
              "कफजः, पूयाय, मर्मजः, रुजे, अचूर्णः, दृश्यते.", role="extend",
              teaches="रुजे is the dative singular of the feminine रुज् (pain): 'for pain', like शूलाय in card 49."),
        mcq("discriminate", 3, "By card 50, what would the marma-born one not be for?",
            ("Pain", "मर्मजश्च रुजे न यः: the marma-born which is not for pain."),
            [("Pus", "Not being for pus is said of the Kapha-born one."),
             ("Burning", "Not being for burning is said of the Pitta-born one (card 49)."),
             ("Swelling", "No swelling is named in card 50.")],
            "Kapha-born: not for pus; marma-born: not for pain.",
            "मर्मजः रुजे न."),
        mcq("apply", 4, "Which split of अकस्माच्च in card 50 is right?",
            ("अकस्मात् + च", "त् before च → च्: अकस्मात् + च → अकस्माच्च."),
            [("अकस्मा + च्च", "अकस्मा is no word; च्च is त् + च."),
             ("अकस्माः + च", "ः before च gives श्च: that would print अकस्माश्च."),
             ("अकस्मान् + च", "न् before च gives ंश्च: that would print अकस्मांश्च.")],
            "अकस्मात् (suddenly) + च (and).",
            "त् before च → च्."),
        mcq("transfer", 5, "By the pattern of यत्र + अकस्मात् → यत्राकस्मात्, how is वन + अन्तः (the forest's edge) joined in a new example?",
            ("वनान्तः", "अ + अ → आ: वन + अन्तः → वनान्तः."),
            [("वनन्तः", "The two अs merge into a long आ; neither is simply lost."),
             ("वनोन्तः", "ओ comes from अ + उ, not from अ + अ."),
             ("वनेन्तः", "ए comes from अ + इ, not from अ + अ.")],
            "वन + अन्तः = वनान्तः, like यत्र + अकस्मात् = यत्राकस्मात्.",
            "अ + अ → आ.",
            teaches="अ + अ merge into आ: यत्र + अकस्मात् → यत्राकस्मात्."),
    ],
}

# ================================================================ NOTES_HI
NOTES_HI = {
    "39": ("पद्य; विश्वास मध्यम; दो छपी पंक्तियाँ (०२.११.७४ और ०२.११.७५) जोड़ी गईं; कोई पाठ-चिह्न नहीं। "
           "डेटा के अनुसार छपी पंक्तियाँ ७४ से ८० (कार्ड ३९ से ४२) एक शृंखला हैं, क्रिया ‘मुष्णाति’ (कार्ड ४२), कर्ता वायु/मारुत। "
           "‘क्षीणदेहस्य वा’ किससे जुड़ता है, स्पष्ट नहीं; ‘बली’ को वायु मानना अनुमान है। छपा ‘नाभी-’ (दीर्घ ई), शब्द-विभाग में ‘नाभि-’। "
           "सन्धि जाँची: गुद + अन्तरम् → गुदान्तरम् (अ + अ → आ); अन्तरम् + गत्वा → अन्तरं गत्वा (व्यंजन से पहले म् → ं)।"),
    "40": ("पद्य; विश्वास मध्यम; दो छपी पंक्तियाँ (०२.११.७६ और ०२.११.७७); कोई पाठ-चिह्न नहीं। ‘बस्तिशिरोनाभि’ को ‘बस्ति-शिर (सम्भावित) और नाभि’ लिया गया; "
           "तीन वस्तुएँ भी सम्भव, विभक्ति छपी नहीं। छपा ‘विबद्ध्य’ (दोहरा द) = विबध्य। ‘भिन्नपुरीषता’ में ‘पतला’ सम्भावित अर्थ है। "
           "सन्धि जाँची: मलान् + बस्ति- → मलान्बस्ति- (रिक्त स्थान के बिना छपा); तृष्णाम् + भिन्न- → तृष्णां भिन्न- (छपा ‘तृष्णांभिन्न’)। "
           "डेटा के अनुसार यह छपी पंक्तियों ७४-७६ (कार्ड ३९-४०) को आगे बढ़ाता है।"),
    "41": ("डेटा में प्रकार ‘गद्य’ है, यद्यपि पंक्तियाँ छन्द-जैसी दिखती हैं; प्रकार बदला नहीं गया और छन्द पर प्रश्न नहीं। विश्वास मध्यम; "
           "छपी पंक्तियाँ ०२.११.७८ और ०२.११.७९। पाठ-चिह्न (सम्भव): ‘पर्शुक अग्राणि’ के बीच रिक्त स्थान एक समास (पर्शुका-अग्राणि) को तोड़ता है। "
           "‘गुदवंक्षणौ’ का द्विवचन जैसा छपा वैसा रखा गया। "
           "सन्धि जाँची: वायुः + गृहीत्वा → वायुर्गृहीत्वा (उ के बाद विसर्ग, घोष ग से पहले → र्); गृहीत्वा + उरः → गृहीत्वोरः (आ + उ → ओ); "
           "उरः + च → उरश्च (च से पहले ः → श्)।"),
    "42": ("पद्य; विश्वास मध्यम; छपी पंक्तियाँ ०२.११.८० और ०२.११.८१। पाठ-चिह्न (सम्भव): छपा ‘स्तिमितस्यान्नताक्षस्यसद्यो’ में ‘आन्नत’ सम्भवतः ‘उन्नत’ (ओ/आ का भ्रम) "
           "और ‘सद्यो’ से पहले रिक्त स्थान छूटा। ‘स्तिमित’ = निश्चल, विकल्प ‘गीला’। छपा ‘मूर्च्छा’ (दोहरा), शब्द-विभाग में मूर्छा। "
           "डेटा: छपी पंक्ति ८० शृंखला ७४-८० की मुख्य क्रिया, कर्ता ‘मारुतः’ (कार्ड ४१); पंक्तियाँ ८१-८२ (कार्ड ४२-४३) एक कथन। "
           "सन्धि जाँची: सद्यः + मुष्णाति → सद्यो मुष्णाति (अः + घोष व्यंजन → ओ); ज्वरसन्तापः + तृष्णा → ज्वरसन्तापस्तृष्णा (त से पहले ः → स्)।"),
    "43": ("पद्य; विश्वास उच्च; छपी पंक्तियाँ ०२.११.८२ और ०२.११.८३; कोई पाठ-चिह्न नहीं। अनेक एकवचन कर्ताओं के बाद क्रिया एकवचन (निकटतम से मेल)। "
           "गोसर्ग = शब्दशः गायों का छूटना, प्रभात (मानक)। वदन = मुख या चेहरा; चेहरा लिया गया। डेटा: छपी पंक्ति ८३ का वाक्य पंक्ति ८४ (कार्ड ४४) में चलता है। "
           "सन्धि जाँची: मुमूर्षोः + उपजायते → मुमूर्षोरुपजायते (ओ के बाद विसर्ग, स्वर से पहले → र्); वदनात् + यस्य → वदनाद्यस्य (घोष य से पहले त् → द्); "
           "स्वेदः + प्रच्यवते → स्वेदः प्रच्यवते (प से पहले विसर्ग रहता है; रिक्त स्थान के बिना छपा)।"),
    "44": ("पद्य; विश्वास मध्यम; छपी पंक्तियाँ ०२.११.८४ और ०२.११.८५। पाठ-चिह्न (सम्भव): छपा ‘लेपज्वरोपतनस्य’ में ‘उपतन’ ज्ञात शब्द नहीं; "
           "‘उपतप्त’ (पीड़ित) अनुमानित पाठ है। लेपज्वर की पहचान विवादित (सम्भवतः चरक का ‘लेपक’ ज्वर, पर अनिश्चित)। छपा ‘प्रबाल’ = प्रवाल (व/ब का अदल-बदल)। "
           "मसूरिका = चेचक जैसा रोग: सम्भावित। डेटा: पंक्ति ८४ पंक्ति ८३ (कार्ड ४३) का वाक्य पूरा करती है, पंक्ति ८५ पंक्ति ८६ (कार्ड ४५) में चलती है। "
           "सन्धि जाँची: गुलिका + आभासाः → गुलिकाभासाः (आ + आ → आ); -आभासाः + यस्य → -आभासा यस्य (आः घोष से पहले विसर्ग खोता है)।"),
    "45": ("पद्य; विश्वास उच्च; छपी पंक्तियाँ ०२.११.८६ और ०२.११.८७; कोई पाठ-चिह्न नहीं। ‘विनश्यन्ति’ का बहुवचन कर्ता नहीं छपा (सम्भवतः कार्ड ४४ की मसूरिकाएँ), "
           "अनुवाद में जोड़ा नहीं गया। छपा ‘विदळ’ में ळ छपाई की आदत (= विदल)। पंक्ति ८७ के विशेषण डेटा के अनुसार पंक्ति ८८ (कार्ड ४६) के ‘विस्फोटाः’ के लगते हैं। "
           "छपा ‘विनश्यंतिन’ = विनश्यन्ति न (रिक्त स्थान छूटा)। सन्धि जाँची: उत्पद्य + आशु → उत्पद्याशु (अ + आ → आ); सः + विनश्यति → स विनश्यति (सः का विसर्ग व्यंजन से पहले लुप्त); ‘चिरात्स’ = चिरात् स (रिक्त स्थान के बिना छपा); "
           "-प्रख्याः + तथा → -प्रख्यास्तथा (त से पहले ः → स्)।"),
    "46": ("पद्य; विश्वास मध्यम; छपी पंक्तियाँ ०२.११.८८ और ०२.११.८९। पाठ-चिह्न (सम्भव): छपा ‘अंतर्वक्त्रा’ में बहुवचन का विसर्ग सम्भवतः छूटा (‘अन्तर्वक्त्राः’); अर्थ वही। "
           "किण = घट्टा, चोट का निशान या दाग: अनिश्चित। ‘कामला अक्ष्णोः’ को एक समास भी पढ़ा जा सकता है। ‘कामलाऽक्ष्णोः’ का ऽ छपाई की आदत। "
           "डेटा: पंक्ति ८९ का वाक्य पंक्ति ९० (कार्ड ४७) में पूरा। सन्धि जाँची: विस्फोटाः + देह- → विस्फोटा देह- (आः घोष से पहले विसर्ग खोता है); "
           "किणाभाः + च → किणाभाश्च (च से पहले ः → श्); शङ्खयोः + मुक्त- → शङ्खयोर्मुक्त- (ओ के बाद विसर्ग, घोष म से पहले → र्)।"),
    "47": ("पद्य; विश्वास कम; छपी पंक्तियाँ ०२.११.९० और ०२.११.९१; कोई पाठ-चिह्न नहीं, पर पंक्ति ९१ का अर्थ सन्दिग्ध: ‘अनुधावत्’ और ‘विघृष्ट’ शब्दशः दिए गए; "
           "इनके नपुंसक एकवचन रूप पंक्ति ९४ (कार्ड ४९) के ‘व्रणाः’ से मेल नहीं खाते; इकाई क्षतिग्रस्त हो सकती है। उस पंक्ति पर प्रश्न नहीं। "
           "‘परिवर्जयेत्’ का कर्ता छपा नहीं। सन्धि जाँची: सन्त्रासः + च → सन्त्रासश्च; च + उष्णता → चोष्णता (अ + उ → ओ); उष्णता + अङ्गे → उष्णताङ्गे (आ + अ → आ); "
           "अकस्मात् + अनुधावत् → अकस्मादनुधावत् (स्वर से पहले त् → द्); अनुधावत् + च → अनुधावच्च (च से पहले त् → च्)।"),
    "48": ("पद्य; विश्वास मध्यम; छपी पंक्तियाँ ०२.११.९२ और ०२.११.९३; कोई पाठ-चिह्न नहीं। वर्णित संज्ञा इस इकाई में नहीं (डेटा: सम्भवतः पंक्ति ९४, कार्ड ४९ के व्रण)। "
           "‘कुणपध्वांक्ष’ को दो गन्ध (शव, कौआ) लिया गया। पहचान: चन्दन = Santalum album, उशीर = खस की जड़ (Chrysopogon zizanioides), कुंकुम = केसर (Crocus sativus), "
           "तीनों मानक; शैवाल विवादित; आल सम्भवतः हरताल। ‘कुंकुमाल’ = कुंकुम + आल या कुंकुम + अल, दोनों सन्धि से सम्भव। "
           "सन्धि जाँची: चन्दन + उशीर → चन्दनोशीर (अ + उ → ओ); कुक्कुटशिखा + कुंकुम में सन्धि नहीं।"),
    "49": ("पद्य; विश्वास मध्यम; छपी पंक्तियाँ ०२.११.९४ और ०२.११.९५; कोई पाठ-चिह्न नहीं। पंक्ति ९४ सम्भवतः पंक्तियों ९१-९३ (कार्ड ४७-४८) की सूची का अन्त; "
           "पंक्ति ९५ की संज्ञा नहीं छपी (सम्भवतः व्रण, पंक्ति ९४ और ९८ देखें), वाक्य पंक्ति ९६ (कार्ड ५०) में चलता है। वात और पित्त दोष, नाम वैसे ही रखे। "
           "सन्धि जाँची: अन्तर्दाहाः + निरूष्माणः → अन्तर्दाहा निरूष्माणः (आः घोष न से पहले विसर्ग खोता है); यः + वातजः → यो वातजः (अः + घोष व्यंजन → ओ); "
           "स्यात् + न → स्यान्न (अनुनासिक से पहले त् → न् विकल्प से; स्याद् न भी शुद्ध)।"),
    "50": ("पद्य; विश्वास मध्यम; छपी पंक्तियाँ ०२.११.९६ और ०२.११.९७; कोई पाठ-चिह्न नहीं। पंक्ति ९६ की संज्ञा और क्रिया पंक्ति ९५ (कार्ड ४९) से आती हैं, जोड़ी नहीं गईं। "
           "मर्म = जीवन-स्थल (शास्त्रीय शब्द), कोई आधुनिक समानार्थी नहीं। पंक्ति ९७ की संज्ञा छपी नहीं (सम्भवतः व्रण); डेटा: पंक्ति ९८ (कार्ड ५१) में आगे। "
           "सन्धि जाँची: कफजः + न → कफजो न; मर्मजः + च → मर्मजश्च; अचूर्णः + चूर्ण- → अचूर्णश्चूर्ण- (च से पहले ः → श्); -आभः + यत्र → -आभो यत्र; "
           "यत्र + अकस्मात् → यत्राकस्मात् (अ + अ → आ); अकस्मात् + च → अकस्माच्च (च से पहले त् → च्)।"),
}

# ================================================================ AIDS
AIDS = {
    "39": {
        "chain": {"steps": ["नाभीगुदांतरं गत्वा: नाभि-गुदा के बीच जाकर", "वंक्षणौ वा समाश्रयन्: या दोनों वंक्षण में टिककर",
                            "गृहीत्वा पायुहृदये: गुदा और हृदय पकड़कर", "बली: बलवान (डेटा का अनुमान: वायु)"]},
        "chunks": "नाभीगुदांतरं गत्वा | वंक्षणौ वा समाश्रयन् || गृहीत्वा पायुहृदये | क्षीणदेहस्य वा | बली",
        "sandhi": "अ + अ → आ: गुद + अन्तरम् → गुदान्तरम् · व्यंजन से पहले म् → ं: अन्तरम् + गत्वा → अन्तरं गत्वा।",
        "anchors": "गुद = पायु: एक ही अंग के दो नाम, एक पहली पंक्ति में, एक दूसरी में। (मेरी याद-पद्धति)",
    },
    "40": {
        "diagram": {"groups": [{"label": "कार्ड ४० (छपे क्रम में)",
                                "items": ["१ मलान् विबद्ध्य: मल रोककर", "२ जनयन् रुजं: पीड़ा उत्पन्न", "३ वंक्षणयोः शूलं: वंक्षण में शूल",
                                          "४ तृष्णां: तृष्णा", "५ भिन्नपुरीषतां: टूटा (सम्भवतः पतला) मल"]}]},
        "chunks": "मलान्बस्तिशिरोनाभि | विबद्ध्य | जनयन् रुजं || कुर्वन् वंक्षणयोः शूलं | तृष्णांभिन्नपुरीषतां",
        "sandhi": "व्यंजन से पहले म् → ं: तृष्णाम् + भिन्न- → तृष्णां भिन्न- · उपसर्ग के साथ -त्वा नहीं, -य: वि + √बन्ध् → विबध्य।",
        "frame": "क्या रुका: मल · कहाँ: बस्ति-शिर (सम्भावित) और नाभि · फल: रुजा, वंक्षण में शूल, तृष्णा, भिन्नपुरीषता · क्रिया: कार्ड ४२ में।",
    },
    "41": {
        "frame": "कर्ता: वायुः ... मारुतः (एक ही) · क्या उत्पन्न: श्वास · क्या पकड़ा: गुदा-वंक्षण, पसलियों के अग्र, वक्ष · क्रिया: कार्ड ४२ में।",
        "chunks": "श्वासं वा जनयन् | वायुर्गृहीत्वा | गुदवंक्षणौ || वितत्यपर्शुक अग्राणि | गृहीत्वोरश्च | मारुतः",
        "sandhi": ("उ के बाद विसर्ग, घोष से पहले → र्: वायुः + गृहीत्वा → वायुर्गृहीत्वा · आ + उ → ओ: गृहीत्वा + उरः → गृहीत्वोरः · "
                   "च से पहले ः → श्: उरः + च → उरश्च।"),
        "anchors": "पहली पंक्ति में वायुः, दूसरी के अन्त में मारुतः: एक ही कर्ता के दो नाम। (मेरी याद-पद्धति)",
    },
    "42": {
        "diagram": {"groups": [{"label": "डेटा के अनुसार एक शृंखला (कार्ड ३९-४२)",
                                "items": ["कार्ड ३९: नाभि-गुदा, वंक्षण, पायु-हृदय", "कार्ड ४०: मल रोक, शूल, तृष्णा",
                                          "कार्ड ४१: श्वास, पसलियाँ, वक्ष", "कार्ड ४२: सद्यो मुष्णाति जीवितम्"]}]},
        "chunks": "स्तिमितस्यान्नताक्षस्य | सद्यो मुष्णाति जीवितं || सहसा | ज्वरसंतापस्तृष्णामूर्च्छाबलक्षयः",
        "sandhi": "अः + घोष व्यंजन → ओ: सद्यः + मुष्णाति → सद्यो मुष्णाति · त से पहले ः → स्: ज्वरसन्तापः + तृष्णा → ज्वरसन्तापस्तृष्णा।",
        "pegs": "ज्वर, तृष्णा, मूर्छा, बल: ‘ज-तृ-मू-ब’ चार पड़ाव। (मेरा बनाया स्मरण-सूत्र)",
    },
    "43": {
        "frame": "पंक्ति १: क्या: सन्धियों का विश्लेषण (और कार्ड ४२ की सूची) · किसमें: मुमूर्षु · क्रिया: उपजायते || पंक्ति २: कब: गोसर्ग · कहाँ से: मुख · क्या: भृश स्वेद · अन्त: कार्ड ४४।",
        "chunks": "विश्लेषणं च संधीनां | मुमूर्षोरुपजायते || गोसर्गे | वदनाद्यस्य | स्वेदःप्रच्यवते | भृशं",
        "sandhi": ("ओ के बाद विसर्ग, स्वर से पहले → र्: मुमूर्षोः + उपजायते → मुमूर्षोरुपजायते · घोष य से पहले त् → द्: वदनात् + यस्य → वदनाद्यस्य।"),
        "anchors": "उपजायते: -यते वाला पर कर्मवाच्य नहीं, ‘उत्पन्न होता है’। (मेरी याद-पद्धति)",
    },
    "44": {
        "frame": "पंक्ति १: किसका: तस्य (कार्ड ४३ का यस्य) · क्या: जीवितम् · कैसा: दुर्लभम् || पंक्ति २: जिसके: गात्रे · क्या: मसूरिकाः · कैसी: प्रवाल-गुलिका जैसी।",
        "chunks": "लेपज्वरोपतनस्य | दुर्लभं तस्य जीवितं || प्रबालगुलिकाभासा | यस्य गात्रे | मसूरिकाः",
        "sandhi": "आ + आ → आ: गुलिका + आभासाः → गुलिकाभासाः · आः घोष से पहले विसर्ग खोता है: -आभासाः + यस्य → -आभासा यस्य।",
    },
    "45": {
        "chain": {"steps": ["उत्पद्य: उत्पन्न होकर", "आशु विनश्यन्ति: शीघ्र नष्ट (कर्ता छपा नहीं)", "न चिरात्: देर से नहीं",
                            "स विनश्यति: वह नष्ट होता है"]},
        "chunks": "उत्पद्याशु विनश्यंति | न चिरात्स विनश्यति || मसूरविदळप्रख्यास्तथा | विद्रुमसन्निभाः",
        "sandhi": ("अ + आ → आ: उत्पद्य + आशु → उत्पद्याशु · त से पहले ः → स्: -प्रख्याः + तथा → -प्रख्यास्तथा · "
                   "सः व्यंजन से पहले विसर्ग खोता है: सः + विनश्यति → स विनश्यति।"),
    },
    "46": {
        "diagram": {"groups": [{"label": "कार्ड ४६ (छपे क्रम में)",
                                "items": ["१ अंतर्वक्त्रा = भीतर-मुखी", "२ किणाभाः = किण जैसे (किण अनिश्चित)", "३ विस्फोटा देहनाशनाः = देह-नाशक फफोले",
                                          "४ कामला अक्ष्णोः = आँखों में पीलिया", "५ मुखं पूर्णं = मुख भरा", "६ शंखयोः मुक्तमांसता"]}]},
        "chunks": "अंतर्वक्त्रा | किणाभाश्च | विस्फोटा देहनाशनाः || कामलाऽक्ष्णोर्मुखंपूर्णं | शंखयोर्मुक्तमांसता",
        "sandhi": ("च से पहले ः → श्: किणाभाः + च → किणाभाश्च · आः घोष से पहले विसर्ग खोता है: विस्फोटाः + देह- → विस्फोटा देह- · "
                   "ओ के बाद विसर्ग, घोष से पहले → र्: शङ्खयोः + मुक्त- → शङ्खयोर्मुक्त-।"),
        "anchors": "छपे क्रम में: आँखें (कामला), मुख (पूर्ण), कनपटी (मांस छूटा)। (मेरी याद-पद्धति)",
    },
    "47": {
        "frame": "किसमें: यस्य · क्या: सन्त्रास और अङ्ग में उष्णता · पाठ का कथन: तं परिवर्जयेत् · पंक्ति २: अर्थ सन्दिग्ध।",
        "chunks": "संत्रासश्चोष्णतांगे च | यस्य | तं परिवर्जयेत् || अकस्मादनुधावच्च | विघृष्टं | त्वक्समाश्रयं",
        "sandhi": ("च से पहले ः → श्: सन्त्रासः + च → सन्त्रासश्च · अ + उ → ओ: च + उष्णता → चोष्णता · आ + अ → आ: उष्णता + अङ्गे → उष्णताङ्गे · "
                   "च से पहले त् → च्: अनुधावत् + च → अनुधावच्च।"),
    },
    "48": {
        "diagram": {"groups": [{"label": "गन्ध (-गंधयः)", "items": ["चन्दन (मानक)", "उशीर (खस, मानक)", "मदिरा", "कुणप (शव)", "ध्वाङ्क्ष (कौआ)"]},
                               {"label": "प्रभा (-प्रभाः)", "items": ["शैवाल (विवादित)", "कुक्कुटशिखा", "कुंकुम (केसर, मानक)",
                                                                    "आल (सम्भवतः हरताल)", "मषी (स्याही)"]}]},
        "chunks": "चंदनोशीरमदिराकुणपध्वांक्षगंधयः || शैवालकुक्कुटशिखाकुंकुमालमषीप्रभाः",
        "sandhi": "अ + उ → ओ: चन्दन + उशीर → चन्दनोशीर · ‘कुंकुमाल’ = कुंकुम + आल या + अल (दोनों सम्भव, प्रश्न नहीं)।",
        "anchors": "पहली पंक्ति नाक के लिए, दूसरी आँख के लिए। (मेरी याद-पद्धति)",
    },
    "49": {
        "frame": "पंक्ति १: व्रण: अन्तर्दाह, निरूष्मा, प्राणनाशकर || पंक्ति २: वातज → न शूलाय · पित्तज → न दाहाय · आगे: कार्ड ५०।",
        "chunks": "अंतर्दाहानिरूष्माणः | प्राणनाशकरा व्रणाः || यो वातजो न शूलाय | स्यान्नदाहाय पित्तजः",
        "sandhi": ("आः घोष से पहले विसर्ग खोता है: अन्तर्दाहाः + निरूष्माणः → अन्तर्दाहा निरूष्माणः · अः + घोष व्यंजन → ओ: यः + वातजः → यो वातजः · "
                   "अनुनासिक से पहले त् → न् (विकल्प; स्याद् न भी शुद्ध): स्यात् + न → स्यान्न।"),
        "pegs": "वातज-शूल, पित्तज-दाह: ‘व-श’, ‘प-द’ के जोड़े, दोनों के आगे ‘न’। (मेरा बनाया स्मरण-सूत्र)",
    },
    "50": {
        "diagram": {"groups": [{"label": "कार्ड ४९-५०: जो इसके लिए न हो",
                                "items": ["कार्ड ४९: वातज → न शूलाय", "कार्ड ४९: पित्तज → न दाहाय", "कार्ड ५०: कफज → न पूयाय",
                                          "कार्ड ५०: मर्मज → न रुजे"]}]},
        "chunks": "कफजो न च पूयाय | मर्मजश्च रुजे न यः || अचूर्णश्चूर्णकीर्णाभो | यत्राकस्माच्च दृश्यते",
        "contrast": "अचूर्णः (चूर्ण से रहित) ⇄ चूर्णकीर्णाभः (चूर्ण बिखरा-सा दिखे): दोनों इसी इकाई में।",
        "sandhi": ("च से पहले ः → श्: अचूर्णः + चूर्ण- → अचूर्णश्चूर्ण- · अ + अ → आ: यत्र + अकस्मात् → यत्राकस्मात् · "
                   "च से पहले त् → च्: अकस्मात् + च → अकस्माच्च।"),
    },
}

# ================================================================ IMAGE_SPECS
IMAGE_SPECS = {
    ("39", "chain"): {
        "file": "sh11-nabhi-guda-39.svg",
        "alt": ("Chain of card 39 in printed order: having gone to the space between navel and anus, or settling in the two "
                "groins, having seized the anus and the heart, the strong one (the data takes it as vāyu, Vāta)."),
        "type": "chain",
        "title": "कार्ड ३९: बली कहाँ जाता है",
        "steps": ["नाभि और गुदा के बीच जाकर", "या दोनों वंक्षण में टिककर", "गुदा (पायु) और हृदय पकड़कर",
                  "बली: बलवान (डेटा का अनुमान: वायु)"],
    },
    ("40", "diagram"): {
        "file": "sh11-mala-40.svg",
        "alt": ("Table of card 40 in printed order: waste products obstructed, pain produced, pain in the two groins, thirst, "
                "and broken (probably loose) stool."),
        "type": "table",
        "title": "कार्ड ४०: रुकावट और उसके फल",
        "heads": ["क्रम", "छपा शब्द: अर्थ"],
        "rows": [["१", "मलान् विबद्ध्य: मल रोककर"], ["२", "जनयन् रुजं: पीड़ा"], ["३", "वंक्षणयोः शूलं: वंक्षण में शूल"],
                 ["४", "तृष्णां: तृष्णा"], ["५", "भिन्नपुरीषतां: टूटा (सम्भवतः पतला) मल"]],
    },
    ("42", "diagram"): {
        "file": "sh11-mushnati-42.svg",
        "alt": ("Table of cards 39 to 42, which the data takes as one run: navel-anus, groins, anus and heart; obstruction, "
                "pain, thirst; breathlessness, ribs, chest; and the verb in card 42, at once steals life."),
        "type": "table",
        "title": "कार्ड ३९-४२: एक शृंखला (डेटा)",
        "heads": ["कार्ड", "क्या"],
        "rows": [["३९", "नाभि-गुदा, वंक्षण, पायु-हृदय"], ["४०", "मल रोक, शूल, तृष्णा"], ["४१", "श्वास, पसलियाँ, वक्ष"],
                 ["४२", "क्रिया: सद्यो मुष्णाति जीवितम्"]],
    },
    ("46", "diagram"): {
        "file": "sh11-visphota-46.svg",
        "alt": ("Table of card 46 in printed order: blisters inward-mouthed, looking like kiṇa (uncertain), body-destroying; "
                "jaundice in the two eyes; face full; loss of flesh in the two temples."),
        "type": "table",
        "title": "कार्ड ४६: लक्षण",
        "heads": ["क्रम", "छपा शब्द = अर्थ"],
        "rows": [["१", "अंतर्वक्त्रा = भीतर-मुखी"], ["२", "किणाभाः = किण जैसे (अनिश्चित)"], ["३", "विस्फोटा देहनाशनाः = देह-नाशक फफोले"],
                 ["४", "कामला अक्ष्णोः = आँखों में पीलिया"], ["५", "मुखं पूर्णं = मुख भरा"], ["६", "शंखयोः = मांस छूटा"]],
    },
    ("48", "diagram"): {
        "file": "sh11-gandha-prabha-48.svg",
        "alt": ("Split of card 48: smells of sandalwood (standard), uśīra (vetiver, standard), an intoxicating drink, a corpse and a crow; lustres "
                "of śaivāla (disputed), cock's comb, saffron (standard), āla (probably orpiment) and ink."),
        "type": "split",
        "title": "कार्ड ४८: गन्ध और प्रभा",
        "cols": [["गन्ध", ["चन्दन (मानक)", "उशीर (खस, मानक)", "मदिरा", "कुणप (शव)", "ध्वाङ्क्ष (कौआ)"]],
                 ["प्रभा", ["शैवाल (विवादित)", "मुर्गे की कलगी", "कुंकुम (केसर, मानक)", "आल (सम्भवतः हरताल)", "मषी (स्याही)"]]],
    },
    ("50", "diagram"): {
        "file": "sh11-dosha-vrana-50.svg",
        "alt": ("Table of cards 49 and 50: the Vāta-born one not for pain, the Pitta-born not for burning, the Kapha-born "
                "not for pus, the marma-born not for pain."),
        "type": "table",
        "title": "कार्ड ४९-५०: जो इसके लिए न हो",
        "heads": ["कौन", "किसके लिए नहीं"],
        "rows": [["वातज (४९)", "शूल"], ["पित्तज (४९)", "दाह"], ["कफज (५०)", "पूय"], ["मर्मज (५०)", "रुजा"]],
    },
}
