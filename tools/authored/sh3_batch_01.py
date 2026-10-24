from helpers import mcq, match, order, fill, multi, accepts


def T(q, teaches):
    q["teaches"] = teaches
    return q


AUTHORED = {}

# ---------------------------------------------------------------- unit 1
AUTHORED["1"] = {
    "title": "अथातो गर्भोपचरणीयं शारीरम्",
    "question": "What does the opening line of Śārīrasthāna chapter 3 announce?",
    "rule": ("अथ अतः गर्भोपचरणीयं शारीरं व्याख्यास्यामः: now, therefore, we shall expound the Śārīra named "
             "Garbhopacaraṇīya, what is to be attended to regarding the embryo."),
    "limits": ("A stock opening formula, prose. It names the chapter only; no regimen is given in this line. "
               "Garbhopacaraṇīya is taken as the chapter's name; its literal sense is 'what is to be attended to "
               "regarding the embryo'."),
    "explain_hi": ("यह तीसरे अध्याय का आरम्भ-सूत्र है: ‘अब, इसलिए, हम गर्भोपचरणीय नामक शारीर की व्याख्या करेंगे।’ "
                   "‘गर्भोपचरणीय’ = गर्भ + उपचरणीय, यानी गर्भ के विषय में जिसकी देखभाल करनी है; यही अध्याय का नाम है। "
                   "‘शारीर’ शरीर-विषयक खण्ड है। "
                   "‘व्याख्यास्यामः’ भविष्यत्-काल, उत्तम पुरुष बहुवचन है: ‘हम व्याख्या करेंगे’। "
                   "इस पंक्ति में अभी कोई चर्या नहीं बताई गई, केवल विषय का नाम है।"),
    "hook": "अथातो … व्याख्यास्यामः: अब गर्भ की देखभाल का अध्याय।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 1, what will the speakers expound in this chapter?",
            ("The Garbhopacaraṇīya, care of the embryo", "गर्भोपचरणीयं शारीरं व्याख्यास्यामः."),
            [("The Garbhāvakrānti Śārīra, the embryo's descent",
              "That title opened chapter 2; this line names Garbhopacaraṇīya."),
             ("The six tastes and the actions of each one",
              "The line names no such subject."),
             ("The signs that foretell the death of a patient",
              "The line names no such subject.")],
            "The line announces the Garbhopacaraṇīya Śārīra: what is to be attended to regarding the embryo.",
            "अथातो गर्भोपचरणीयं शारीरं व्याख्यास्यामः."),
        order(1, "Put the words of unit 1 in the line's order.",
              ["अथ", "अतः", "गर्भोपचरणीयम्", "शारीरम्", "व्याख्यास्यामः"],
              "Now, therefore, the Garbhopacaraṇīya, the Śārīra, we shall expound.",
              "अथ → अतः → गर्भोपचरणीयम् → शारीरम् → व्याख्यास्यामः."),
        match(2, "Match each word of unit 1 to its meaning.",
              [["अथ", "now"], ["अतः", "therefore"], ["गर्भ", "embryo"],
               ["उपचरणीय", "to be attended to, care"], ["शारीरम्", "(section) on the body"],
               ["व्याख्यास्यामः", "we shall expound"]],
              "These words make the whole opening formula.",
              "अथ, अतः, गर्भ, उपचरणीय, शारीरम्, व्याख्यास्यामः.", role="extend",
              teaches="गर्भोपचरणीय = गर्भ (embryo) + उपचरणीय (to be attended to): the chapter is on care regarding the embryo."),
        mcq("discriminate", 3, "Which split of गर्भोपचरणीयम् is right?",
            ("गर्भ + उपचरणीयम्", "अ + उ → ओ: गर्भ + उपचरणीयम् = गर्भोपचरणीयम्."),
            [("गर्भः + उपचरणीयम्", "A compound member has no visarga; अः before उ would lose the visarga and leave गर्भ उपचरणीयम्."),
             ("गर्भो + पचरणीयम्", "पचरणीयम् is not the word of the card; the word is उपचरणीयम्."),
             ("गर्भ + ओपचरणीयम्", "अ + ओ would give औ, and ओपचरणीयम् is not a word.")],
            "गर्भ (embryo) + उपचरणीयम् (to be attended to): अ + उ → ओ.",
            "अ + उ → ओ."),
        mcq("apply", 4, "By the card, what form is व्याख्यास्यामः?",
            ("Future, first person plural: we shall expound", "Labelled 1 pl. fut. of वि-आ-√ख्या."),
            [("Present, first person plural: we now expound", "The -स्य- marks the future, not the present."),
             ("Future, third person plural: they will expound", "Third person plural would end in -स्यन्ति."),
             ("Optative, third singular: one should expound", "The optative of this chapter looks like पिबेत्; -स्यामः is future.")],
            "व्याख्यास्यामः = we shall expound: future, first person plural.",
            "-स्यामः = future, we shall."),
        mcq("transfer", 5, "By the ending of व्याख्यास्यामः, which form says we shall do, from √कृ?",
            ("करिष्यामः", "-ष्यामः is future, first person plural, like -स्यामः in व्याख्यास्यामः."),
            [("करिष्यन्ति", "-ष्यन्ति is future third plural: they will do."),
             ("कुर्मः", "कुर्मः is present: we do."),
             ("अकुर्म", "अकुर्म is past (imperfect): we did.")],
            "करिष्यामः = we shall do, like व्याख्यास्यामः = we shall expound.",
            "-स्यामः / -ष्यामः = we shall.",
            teaches="The future first person plural ends in -स्यामः / -ष्यामः: व्याख्यास्यामः = we shall expound, करिष्यामः = we shall do."),
    ],
}

# ---------------------------------------------------------------- unit 2
AUTHORED["2"] = {
    "title": "प्रथमेमासि गर्भिणी क्षीरमुपसंस्कृतं … पिबेत्",
    "question": "By unit 2, what should the pregnant woman drink in the first month, and how?",
    "rule": ("In the first month (प्रथमे मासि) the pregnant woman should drink (पिबेत्) milk (क्षीर) that is prepared "
             "(उपसंस्कृत), in measure (मात्रावत्), cool (शीत), at the (due) time (काले)."),
    "limits": ("The line does not say how the milk is prepared, what the measure is, or which time काले means. "
               "प्रथमेमासि is two words printed together, not a sandhi. Prose, not a verse."),
    "explain_hi": ("पहले मास में गर्भिणी दूध पिए: संस्कार किया हुआ (उपसंस्कृत), मात्रा के अनुसार, ठण्डा, और समय पर। "
                   "‘पिबेत्’ विधिलिङ् है: ‘पिए’, यानी करने योग्य बात। "
                   "संस्कार कैसे किया जाए, मात्रा कितनी हो, और ‘काले’ कौन-सा समय है, यह पंक्ति नहीं बताती। "
                   "‘प्रथमेमासि’ दो शब्द हैं जो एक साथ छपे हैं (प्रथमे मासि), यह कोई सन्धि नहीं। "
                   "‘मात्रावच्छीतं’ में मात्रावत् + शीतम् है: यहाँ त् + श को च्छ लिखा गया।"),
    "hook": "पहला मास: संस्कारित दूध, नपा, ठण्डा, समय पर।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 2, what should the pregnant woman drink in the first month?",
            ("Milk (क्षीरम्), prepared and cool", "गर्भिणी क्षीरमुपसंस्कृतं … शीतं … पिबेत्."),
            [("Milk with ghee and honey", "Ghee and honey join the milk in unit 8, the third (month)."),
             ("Honey (मधु), mixed into water", "No honey is named in unit 2."),
             ("Butter (नवनीत), in a measure", "Fresh butter is named in unit 9, the fourth (month).")],
            "In the first month she drinks milk, prepared, in measure, cool, at the time.",
            "प्रथमे मासि गर्भिणी क्षीरं … पिबेत्."),
        order(1, "Put the printed words of unit 2 in the line's order.",
              ["प्रथमेमासि", "गर्भिणी", "क्षीरमुपसंस्कृतं", "मात्रावच्छीतं", "काले", "पिबेत्"],
              "In the first month, the pregnant woman, milk prepared, in measure cool, at the time, should drink.",
              "प्रथमेमासि → गर्भिणी → क्षीरमुपसंस्कृतं → मात्रावच्छीतं → काले → पिबेत्."),
        match(2, "Match each word of unit 2 to its meaning.",
              [["क्षीरम्", "milk"], ["उपसंस्कृतम्", "prepared, treated"], ["मात्रावत्", "in measure"],
               ["शीतम्", "cool"], ["काले", "at the (due) time"]],
              "Five words say what she drinks and how.",
              "क्षीरम्, उपसंस्कृतम्, मात्रावत्, शीतम्, काले.", role="extend",
              teaches="मात्रावत् = in measure: the milk is taken in a measured amount, which the line does not fix."),
        mcq("discriminate", 3, "Which split of मात्रावच्छीतं is right?",
            ("मात्रावत् + शीतम्", "त् before श becomes च्, and the श is written छ here: च्छ."),
            [("मात्रावत् + छीतम्", "छीतम् is not a word; the word is शीतम्, cool."),
             ("मात्रा + वच्छीतम्", "वच्छीतम् is not a word; -वत् belongs to मात्रा."),
             ("मात्रावच् + शीतम्", "वच् is not the ending; the ending is -वत्.")],
            "मात्रावत् (in measure) + शीतम् (cool): here त् + श is written च्छ.",
            "त् + श → च्छ (as printed here)."),
        multi("apply", 4, "Which points does unit 2 leave unstated?",
              [("That the milk should be cool", "Stated: शीतम्."),
               ("How the milk is to be prepared", "Right: the note says the preparation is not stated."),
               ("Who is to drink the milk", "Stated: गर्भिणी, the pregnant woman."),
               ("Which time काले refers to", "Right: the note says the text does not say which time.")],
              [1, 3],
              "Cool and the drinker are stated; the preparation and the time are not.",
              "उपसंस्कृतम्, काले: not further defined."),
        mcq("transfer", 5, "By पिबेत् of unit 2, which invented sentence says the child should drink water?",
            ("बालो जलं पिबेत्", "पिबेत् is optative: should drink."),
            [("बालो जलं पिबति", "पिबति is present: drinks, a statement, not should."),
             ("बालो जलमपिबत्", "अपिबत् is past: drank."),
             ("बालो जलं पास्यति", "पास्यति is future: will drink.")],
            "बालो जलं पिबेत् = the child should drink water, like गर्भिणी क्षीरं पिबेत्.",
            "पिबेत् = should drink (optative).",
            teaches="पिबेत् is the optative (3 sg.) of √पा: should drink, the form the text uses for what is to be done."),
    ],
}

# ---------------------------------------------------------------- unit 3
AUTHORED["3"] = {
    "title": "तस्मिन्नपि चाद्यं द्वादशरात्रं क्षीरोद्भवं सर्पिः … पिबेत्",
    "question": "By unit 3, what does she drink for the first twelve nights, and with what after-drink?",
    "rule": ("In that (month), for the first twelve nights, she should drink ghee (सर्पिः) arising from milk, boiled (शृत) "
             "with śāliparṇī and palāśa, with cool water (शीतोदक) prepared with gold and silver as after-drink (अनुपान)."),
    "limits": ("Medium confidence. Printed कथित is read conjecturally as क्वथित (boiled), so how the water is prepared with "
               "gold and silver is not sure; no question rests on it. Palāśa = Butea monosperma is probable (palāśa may also "
               "mean leaf). Śāliparṇī = Desmodium gangeticum (standard). No dose is given."),
    "explain_hi": ("उसी (पहले) मास में, पहली बारह रातों तक, गर्भिणी दूध से उत्पन्न घी पिए, जो शालिपर्णी (Desmodium gangeticum, मानक) "
                   "और पलाश (Butea monosperma, सम्भावित) के साथ उबाला गया हो। "
                   "इसका अनुपान, यानी बाद में पीने का द्रव, सोने और चाँदी के साथ तैयार किया ठण्डा जल है। "
                   "छपा ‘कथित’ (कहा हुआ) यहाँ ठीक नहीं बैठता; ‘क्वथित’ (उबाला हुआ) केवल अनुमानित पाठ है, इसलिए जल की तैयारी पर कोई प्रश्न नहीं। "
                   "‘पलाश’ का अर्थ ‘पत्ता’ भी हो सकता है; तब ‘शालिपर्णी के पत्तों के साथ’ भी सम्भव है। "
                   "मात्रा नहीं बताई गई।"),
    "hook": "बारह रातें: दूध का घी, शालिपर्णी-पलाश से उबला; अनुपान ठण्डा जल।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 3, what does she drink for the first twelve nights?",
            ("Ghee arising from milk, boiled with herbs", "क्षीरोद्भवं सर्पिः … शृतं … पिबेत्."),
            [("Milk cooked with sweet medicines alone", "That is unit 7, the second (month)."),
             ("Milk joined with fresh butter in a measure", "That is unit 9, the fourth (month)."),
             ("Cool water by itself, with no ghee at all", "Cool water is the after-drink; the drink itself is ghee.")],
            "For the first twelve nights: ghee from milk, boiled with śāliparṇī and palāśa.",
            "आद्यं द्वादशरात्रं क्षीरोद्भवं सर्पिः … पिबेत्."),
        order(1, "Put these printed words of unit 3 in the line's order.",
              ["द्वादशरात्रं", "क्षीरोद्भवं", "सर्पिः", "शालिपर्णीपलाशाभ्यां", "शृतं", "पिबेत्"],
              "Twelve nights, arising from milk, ghee, with śāliparṇī and palāśa, boiled, should drink.",
              "द्वादशरात्रं → क्षीरोद्भवं → सर्पिः → शालिपर्णीपलाशाभ्यां → शृतं → पिबेत्."),
        match(2, "Match each word of unit 3 to its meaning.",
              [["द्वादशरात्रम्", "twelve nights"], ["क्षीरोद्भवम्", "arising from milk"], ["सर्पिः", "ghee"],
               ["शृतम्", "boiled"], ["अनुपानम्", "after-drink"]],
              "These words say for how long, what, how prepared, and what follows.",
              "द्वादशरात्रम्, क्षीरोद्भवम्, सर्पिः, शृतम्, अनुपानम्.", role="extend",
              teaches="अनुपान = after-drink: what is drunk after the main preparation; here cool water."),
        mcq("discriminate", 3, "Which statement keeps the card's identification and label right?",
            ("Śāliparṇī is Desmodium gangeticum (standard)", "The data: śāliparṇī = Desmodium gangeticum, standard."),
            [("Palāśa is Butea monosperma (standard)", "Palāśa = Butea monosperma is labelled probable, not standard."),
             ("Śāliparṇī is Butea monosperma (probable)", "Butea monosperma is given for palāśa, not śāliparṇī."),
             ("Palāśa is Desmodium gangeticum (standard)", "Desmodium gangeticum is given for śāliparṇī, not palāśa.")],
            "Śāliparṇī = Desmodium gangeticum (standard); palāśa = Butea monosperma (probable).",
            "Keep each plant with its own name and label."),
        mcq("apply", 4, "Which split of तस्मिन्नपि is right?",
            ("तस्मिन् + अपि", "After a short vowel a final न् is doubled before a vowel: न्न."),
            [("तस्मिन्न + अपि", "There is no word तस्मिन्न; the word is तस्मिन्, in that."),
             ("तस्मि + न्नपि", "Neither piece is a word."),
             ("तस्मिन् + नपि", "नपि is not a word; the word is अपि, also.")],
            "तस्मिन् (in that) + अपि (also): न् after short इ doubles before a vowel.",
            "short vowel + न् + vowel → न्न."),
        mcq("transfer", 5, "By the rule of तस्मिन्नपि, how is कस्मिन् + अपि (in any) written when joined?",
            ("कस्मिन्नपि", "न् after the short इ doubles before अ, as in तस्मिन्नपि."),
            [("कस्मिनपि", "After a short vowel the न् is doubled, not kept single."),
             ("कस्मिन्नेपि", "अ does not change to ए here."),
             ("कस्मिंपि", "The न् does not become anusvara before a vowel.")],
            "कस्मिन् + अपि = कस्मिन्नपि, like तस्मिन् + अपि = तस्मिन्नपि.",
            "short vowel + न् + vowel → न्न.",
            teaches="A final न् after a short vowel is doubled before a vowel: तस्मिन् + अपि → तस्मिन्नपि."),
    ],
}

# ---------------------------------------------------------------- unit 4
AUTHORED["4"] = {
    "title": "खादुशीतं द्रवप्रायं सात्म्यं च सायं प्रातराहारयेत्",
    "question": "By unit 4, what kind of food is given, and at what times of day?",
    "rule": ("Food mostly liquid (द्रवप्राय) and suitable (सात्म्य), and, on a conjectural reading, sweet and cool, is to be "
             "given in the evening and in the morning (सायं प्रातः). आहारयेत् = should have (her) take as food."),
    "limits": ("Printed खादु is not a word; स्वादु (sweet) is a conjecture, so no question rests on खादुशीतं. Which foods are "
               "meant, and who gives them (the subject of आहारयेत्), are not stated. सात्म्य = agreeable to her, not further defined."),
    "explain_hi": ("इस पंक्ति के अनुसार ऐसा आहार कराया जाए जो अधिकतर तरल (द्रवप्राय) और अनुकूल (सात्म्य) हो, और अनुमानित पाठ पर मीठा व ठण्डा भी। "
                   "समय: सायं और प्रातः। "
                   "छपा ‘खादु’ कोई शब्द नहीं; ‘स्वादु’ (मीठा) केवल अनुमान है, इसलिए उस पर प्रश्न नहीं। "
                   "कौन-से खाद्य, और कौन खिलाए, यह नहीं बताया गया। "
                   "‘आहारयेत्’ णिजन्त (प्रेरणार्थक) विधिलिङ् है: ‘आहार कराए’।"),
    "hook": "सायं-प्रातः: पतला, अनुकूल आहार।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 4, at what times is the food to be given?",
            ("Evening and morning", "सायं प्रातराहारयेत्: evening and morning."),
            [("At midday and at midnight", "The line names सायं and प्रातः, not midday or midnight."),
             ("Only once a day, at noon", "Two times are named, evening and morning."),
             ("Only at night, after sleep", "The line names evening and morning.")],
            "The two times are सायम् (evening) and प्रातर् (morning).",
            "सायं प्रातः = evening and morning."),
        order(1, "Put the printed words of unit 4 in the line's order.",
              ["खादुशीतं", "द्रवप्रायं", "सात्म्यं", "च", "सायं", "प्रातराहारयेत्"],
              "(Sweet?) and cool, mostly liquid, suitable, and, in the evening, in the morning one should have her take.",
              "खादुशीतं → द्रवप्रायं → सात्म्यं → च → सायं → प्रातराहारयेत्."),
        match(2, "Match each sure word of unit 4 to its meaning.",
              [["द्रवप्रायम्", "mostly liquid"], ["सात्म्यम्", "suitable, agreeable"], ["सायम्", "in the evening"],
               ["प्रातर्", "in the morning"], ["आहारयेत्", "should have (her) take as food"]],
              "These sure words say what kind of food and when.",
              "द्रवप्रायम्, सात्म्यम्, सायम्, प्रातर्, आहारयेत्.", role="extend",
              teaches="-प्राय at the end of a compound = mostly: द्रवप्राय = mostly liquid."),
        mcq("discriminate", 3, "Which printed word of unit 4 does the card mark as doubtful?",
            ("खादुशीतं", "खादु is not a word; स्वादु is only a conjecture."),
            [("द्रवप्रायं", "A sure word: mostly liquid."),
             ("सात्म्यं", "A sure word: suitable, agreeable."),
             ("सायं", "A sure word: in the evening.")],
            "Only खादुशीतं carries the doubtful खादु.",
            "खादु → (conjecture) स्वादु."),
        mcq("apply", 4, "Which split of प्रातराहारयेत् is right?",
            ("प्रातर् + आहारयेत्", "र् stays before a vowel and joins it."),
            [("प्रातः + राहारयेत्", "राहारयेत् is not a word; the verb is आहारयेत्."),
             ("प्रात + आहारयेत्", "अ + आ → आ would give प्राताहारयेत्, with no र्."),
             ("प्रातरा + हारयेत्", "प्रातरा is not a word; the verb is आहारयेत्, from आ-√हृ.")],
            "प्रातर् (in the morning) + आहारयेत् (should have her take as food).",
            "र् + vowel: र् stays."),
        mcq("transfer", 5, "By -प्राय in द्रवप्रायम्, what does जलप्रायम् (of a dish, a new example) mean?",
            ("Mostly water", "-प्राय = mostly, as द्रवप्राय = mostly liquid."),
            [("Without any water", "Without would need a word like निर्-; -प्राय means mostly."),
             ("With a little water", "-प्राय does not mean a little."),
             ("Made for drinking water", "-प्राय does not mean made for.")],
            "जलप्राय = mostly water, like द्रवप्राय = mostly liquid.",
            "-प्राय = mostly.",
            teaches="-प्राय at the end of a compound means mostly: द्रवप्राय = mostly liquid, जलप्राय = mostly water."),
    ],
}

# ---------------------------------------------------------------- unit 5
AUTHORED["5"] = {
    "title": "न चाभ्यंगोद्वर्तनानि सेवेत",
    "question": "By unit 5, what should the pregnant woman not resort to?",
    "rule": ("She should not resort to (न … सेवेत) oil massage (अभ्यङ्ग) and rubbing with powders (उद्वर्तन). "
             "न with an optative verb forbids."),
    "limits": ("The line gives no reason and no time limit. The subject, the pregnant woman, is understood from unit 2, "
               "not printed. Printed अभ्यंग = अभ्यङ्ग."),
    "explain_hi": ("गर्भिणी अभ्यंग (तेल की मालिश) और उद्वर्तन (उबटन, चूर्ण से मलना) का सेवन न करे। "
                   "‘न … सेवेत’ निषेध है: ‘सेवन न करे’। "
                   "कर्ता (गर्भिणी) इकाई 2 से समझा जाता है, यहाँ छपा नहीं। "
                   "कारण और अवधि यह पंक्ति नहीं बताती। "
                   "‘अभ्यंगोद्वर्तनानि’ में अभ्यङ्ग + उद्वर्तनानि है (अ + उ → ओ)।"),
    "hook": "न मालिश, न उबटन।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 5, which two things should she not resort to?",
            ("Oil massage and powder rubs", "न चाभ्यंगोद्वर्तनानि सेवेत."),
            [("Milk and ghee taken cool", "Milk and ghee are prescribed in units 2 and 3, not forbidden."),
             ("Bathing and sleeping by day", "Neither is named in unit 5."),
             ("Honey and fresh butter", "These are added in later months (units 8, 9), not forbidden here.")],
            "She should avoid अभ्यङ्ग (oil massage) and उद्वर्तन (rubbing with powders).",
            "न अभ्यङ्गोद्वर्तनानि सेवेत."),
        match(1, "Match each word of unit 5 to its meaning.",
              [["न", "not"], ["च", "and"], ["अभ्यङ्ग", "oil massage"], ["उद्वर्तन", "rubbing with powders"],
               ["सेवेत", "she should resort to"]],
              "Five words make the whole line.",
              "न, च, अभ्यङ्ग, उद्वर्तन, सेवेत."),
        T(fill(2, "In unit 5, oil massage is ____ (type it in Devanagari or in English letters, e.g. dharma).",
               accepts("अभ्यङ्ग", None, "abhyanga"),
               "अभ्यङ्ग = oil massage; printed अभ्यंग.",
               "अभ्यङ्ग = oil massage.",
               "अभ्यङ्ग = oil massage."),
          "अभ्यङ्ग = oil massage; अभ्यंग and अभ्यङ्ग are two spellings of one word."),
        mcq("discriminate", 3, "Which split of अभ्यंगोद्वर्तनानि is right?",
            ("अभ्यङ्ग + उद्वर्तनानि", "अ + उ → ओ: अभ्यङ्ग + उद्वर्तनानि."),
            [("अभ्यङ्गः + उद्वर्तनानि", "A compound member has no visarga; अः before उ would leave अभ्यङ्ग उद्वर्तनानि."),
             ("अभ्यङ्गो + द्वर्तनानि", "द्वर्तनानि is not a word; the word is उद्वर्तनानि."),
             ("अभ्यङ्ग + ओद्वर्तनानि", "अ + ओ would give औ, and ओद्वर्तनानि is not a word.")],
            "अभ्यङ्ग (oil massage) + उद्वर्तनानि (rubbings with powder): अ + उ → ओ.",
            "अ + उ → ओ."),
        mcq("apply", 4, "In unit 5, what makes the sentence a prohibition?",
            ("न with the optative सेवेत", "न + optative = she should not resort to."),
            [("The plural ending of the compound", "A noun ending does not forbid; न does."),
             ("The particle च, read as not", "च means and; न means not."),
             ("A future verb: she will not resort", "सेवेत is optative, not future.")],
            "न + सेवेत = she should not resort to.",
            "न + optative = should not."),
        mcq("transfer", 5, "By न … सेवेत, which invented sentence says and she should not go to the village?",
            ("न च ग्रामं गच्छेत्", "न + optative गच्छेत् = should not go."),
            [("न च ग्रामं गच्छति", "गच्छति is present: does not go, a statement."),
             ("च ग्रामं गच्छेत्", "Without न it says she should go."),
             ("न च ग्रामं गमिष्यति", "गमिष्यति is future: will not go.")],
            "न च ग्रामं गच्छेत् = and she should not go to the village, like न च … सेवेत.",
            "न + optative = should not.",
            teaches="न with an optative verb forbids: न … सेवेत = she should not resort to; न … गच्छेत् = she should not go."),
    ],
}

# ---------------------------------------------------------------- unit 6
AUTHORED["6"] = {
    "title": "यथोक्तानि च दोषकराणि परिहरेत्",
    "question": "By the sure words of unit 6, what should she avoid?",
    "rule": ("She should avoid (परिहरेत्) the doṣa-causing (दोषकर) things as stated (यथोक्त). A time limit follows in a "
             "damaged word; 'up to the fifth month' is only a conjecture."),
    "limits": ("Low confidence. Printed आर्पचमान् is not a word; 'up to the fifth month' (आपञ्चमात्) is a guess, so no "
               "question rests on the month. What was stated earlier (यथोक्त) is not in this unit, and the doṣa-causing "
               "things are not listed."),
    "explain_hi": ("निश्चित भाग: ‘जैसा कहा गया है, वैसे दोष करने वाले (पदार्थों या कार्यों) को त्याग दे’। "
                   "इसके बाद एक बिगड़ा हुआ छपा शब्द ‘आर्पचमान्’ है; ‘आपञ्चमात् मासात्’ (पाँचवें मास तक) केवल अनुमान है। "
                   "इसलिए अवधि पर कोई प्रश्न नहीं; केवल इतना पक्का है कि कोई समय-सीमा कही गई है। "
                   "‘यथोक्त’ पहले कही गई बात की ओर संकेत करता है, जो इस अंश में नहीं है। "
                   "दोषकर = दोष (दोषों का विकार) उत्पन्न करने वाले।"),
    "hook": "जो कहे गए दोषकर, उन्हें त्यागे; अवधि का शब्द संदिग्ध।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By the sure words of unit 6, what should she avoid?",
            ("The doṣa-causing things, as stated", "यथोक्तानि च दोषकराणि परिहरेत्."),
            [("Milk that is prepared and cool", "Milk is prescribed in unit 2, not avoided."),
             ("Ghee that arises from milk", "Ghee is prescribed in unit 3, not avoided."),
             ("Food that is mostly liquid", "Such food is given in unit 4, not avoided.")],
            "She avoids the doṣa-causing things, as stated before.",
            "दोषकराणि परिहरेत्."),
        order(1, "Put the sure words of unit 6 in the line's order.",
              ["यथोक्तानि", "च", "दोषकराणि", "परिहरेत्"],
              "As stated, and, the doṣa-causing, she should avoid.",
              "यथोक्तानि → च → दोषकराणि → परिहरेत्."),
        match(2, "Match each sure word of unit 6 to its meaning.",
              [["यथोक्तानि", "as stated"], ["दोषकराणि", "causing doṣa"], ["परिहरेत्", "should avoid"],
               ["च", "and"]],
              "These four words are the sure part of the line.",
              "यथोक्तानि, दोषकराणि, परिहरेत्, च.", role="extend",
              teaches="-कर at the end of a compound = causing, making: दोषकर = causing doṣa (disturbance of the humours)."),
        mcq("discriminate", 3, "Which part of unit 6 does the card call only a conjecture?",
            ("The fifth-month limit", "आर्पचमान् is not a word; आपञ्चमात् is a guess."),
            [("That something is to be avoided", "Sure: परिहरेत्, should avoid."),
             ("That the things cause doṣa", "Sure: दोषकराणि."),
             ("That they were stated before", "Sure: यथोक्तानि, as stated.")],
            "Only the month limit rests on a guessed reading.",
            "आर्पचमान् → (guess) आपञ्चमात्."),
        mcq("apply", 4, "Which split of यथोक्तानि is right?",
            ("यथा + उक्तानि", "आ + उ → ओ: यथा + उक्तानि."),
            [("यथो + क्तानि", "Neither piece is a word."),
             ("यथा + ओक्तानि", "आ + ओ would give औ, and ओक्तानि is not a word."),
             ("यथः + उक्तानि", "There is no word यथः; the word is यथा, as.")],
            "यथा (as) + उक्तानि (stated): आ + उ → ओ.",
            "आ + उ → ओ."),
        mcq("transfer", 5, "By the rule of यथोक्तानि, how is महा + उत्सवः (a great festival) written when joined?",
            ("महोत्सवः", "आ + उ → ओ, as यथा + उक्तानि."),
            [("महौत्सवः", "आ + उ does not give औ."),
             ("महात्सवः", "The उ is not dropped after आ."),
             ("महुत्सवः", "The आ is not dropped before उ.")],
            "महा + उत्सवः = महोत्सवः, like यथा + उक्तानि = यथोक्तानि.",
            "आ + उ → ओ.",
            teaches="आ (or अ) followed by उ joins as ओ: यथा + उक्तानि → यथोक्तानि."),
    ],
}

# ---------------------------------------------------------------- unit 7
AUTHORED["7"] = {
    "title": "विशेषेण द्वितीये मधुरौषधसिद्धं पयः पिबेत्",
    "question": "By unit 7, what should she drink, especially, in the second month?",
    "rule": ("Especially (विशेषेण) in the second (month), she should drink milk (पयस्) cooked (सिद्ध) with sweet medicines "
             "(मधुर-औषध). मधुर + औषध → मधुरौषध (अ + औ → औ)."),
    "limits": ("The word month is understood from unit 2, not printed. The sweet medicines are not listed here and none is "
               "identified. No dose is given."),
    "explain_hi": ("विशेष रूप से दूसरे (मास) में गर्भिणी मधुर औषधों से पकाया हुआ दूध (पयः) पिए। "
                   "‘मास’ शब्द यहाँ नहीं छपा, इकाई 2 से समझा जाता है। "
                   "मधुर औषध कौन-से हैं, यहाँ नहीं गिनाए गए; किसी की पहचान नहीं दी गई। "
                   "‘-सिद्ध’ समास के अन्त में = उससे पकाया हुआ। "
                   "‘मधुरौषध’ में मधुर + औषध है (अ + औ → औ)।"),
    "hook": "दूसरा मास: मधुर औषधों से सिद्ध दूध।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 7, what should she drink in the second (month)?",
            ("Milk cooked with sweet medicines", "मधुरौषधसिद्धं पयः पिबेत्."),
            [("Ghee boiled with śāliparṇī", "That is unit 3, the first month's twelve nights."),
             ("Milk with ghee and honey", "That is unit 8, the third (month)."),
             ("Milk with fresh butter", "That is unit 9, the fourth (month).")],
            "In the second, milk cooked with sweet medicines.",
            "द्वितीये मधुरौषधसिद्धं पयः पिबेत्."),
        order(1, "Put the words of unit 7 in the line's order.",
              ["विशेषेण", "द्वितीये", "मधुरौषधसिद्धम्", "पयः", "पिबेत्"],
              "Especially, in the second, cooked with sweet medicines, milk, she should drink.",
              "विशेषेण → द्वितीये → मधुरौषधसिद्धम् → पयः → पिबेत्."),
        match(2, "Match each word of unit 7 to its meaning.",
              [["विशेषेण", "especially"], ["द्वितीये", "in the second"], ["मधुर", "sweet"],
               ["औषध", "medicine"], ["सिद्धम्", "cooked"], ["पयः", "milk"]],
              "Six members carry the whole line.",
              "विशेषेण, द्वितीये, मधुर, औषध, सिद्धम्, पयः.", role="extend",
              teaches="-सिद्ध at the end of a compound = cooked with: मधुरौषधसिद्ध = cooked with sweet medicines."),
        mcq("discriminate", 3, "Which split of मधुरौषध is right?",
            ("मधुर + औषध", "अ + औ → औ: मधुर + औषध."),
            [("मधुरौ + षध", "षध is not a word; the word is औषध, medicine."),
             ("मधु + रौषध", "रौषध is not a word."),
             ("मधुरः + औषध", "A compound member has no visarga; अः before औ would leave मधुर औषध.")],
            "मधुर (sweet) + औषध (medicine): अ + औ → औ.",
            "अ + औ → औ."),
        multi("apply", 4, "Which statements does unit 7 make?",
              [("The milk is cooked with sweet medicines", "Right: मधुरौषधसिद्धं पयः."),
               ("The sweet medicines are named one by one", "None is listed here."),
               ("It is for the second (month)", "Right: द्वितीये."),
               ("The milk is taken with honey", "Honey comes in unit 8, the third.")],
              [0, 2],
              "Milk cooked with sweet medicines, in the second (month); none is named.",
              "द्वितीये मधुरौषधसिद्धं पयः."),
        mcq("transfer", 5, "By the rule of मधुरौषध, how is वन + औषधम् (a forest medicine) written when joined?",
            ("वनौषधम्", "अ + औ → औ, as मधुर + औषध."),
            [("वनोषधम्", "अ + औ does not give ओ."),
             ("वनेषधम्", "अ + औ does not give ए."),
             ("वनवौषधम्", "No व् is put between अ and औ.")],
            "वन + औषधम् = वनौषधम्, like मधुर + औषध = मधुरौषध.",
            "अ + औ → औ.",
            teaches="अ followed by औ joins as औ: मधुर + औषध → मधुरौषध."),
    ],
}

# ---------------------------------------------------------------- unit 8
AUTHORED["8"] = {
    "title": "तृतीये तदेव सर्पिर्मधुभ्यां",
    "question": "By unit 8, what is given in the third month?",
    "rule": ("In the third (month), the same (तदेव: the milk of unit 7) with ghee and honey (सर्पिर्मधुभ्याम्, instrumental "
             "dual: with the two). The verb पिबेत् is carried over, not printed."),
    "limits": ("No verb is printed; it is carried from unit 7. The amounts of ghee and honey are not stated. Medium confidence."),
    "explain_hi": ("तीसरे (मास) में वही (इकाई 7 का दूध), घी और मधु के साथ। "
                   "क्रिया ‘पिबेत्’ पिछली इकाई से चली आती है, यहाँ छपी नहीं। "
                   "‘सर्पिर्मधुभ्याम्’ तृतीया द्विवचन है: ‘(इन) दोनों के साथ’, घी और मधु। "
                   "घी और मधु की मात्रा नहीं बताई गई। "
                   "‘सर्पिर्मधु’ में सर्पिः + मधु है (इ के बाद विसर्ग → र् घोष ‘म’ से पहले)।"),
    "hook": "तीसरा मास: वही दूध, घी और मधु के साथ।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 8, with what is the same (milk) taken in the third (month)?",
            ("With ghee and honey", "तदेव सर्पिर्मधुभ्याम्."),
            [("With fresh butter", "Fresh butter is unit 9, the fourth."),
             ("With cool water", "Cool water is the after-drink of unit 3."),
             ("With rice gruel", "No gruel is named in unit 8.")],
            "The same milk, with ghee and honey.",
            "तृतीये तदेव सर्पिर्मधुभ्याम्."),
        match(1, "Match each word of unit 8 to its meaning.",
              [["तृतीये", "in the third"], ["तत्", "that"], ["एव", "same, very"], ["सर्पिः", "ghee"],
               ["मधु", "honey"]],
              "Five members make the whole line.",
              "तृतीये, तत्, एव, सर्पिः, मधु."),
        T(fill(2, "In unit 8, honey is ____ (type it in Devanagari or in English letters, e.g. dharma).",
               accepts("मधु"),
               "सर्पिर्मधुभ्याम् = with ghee (सर्पिः) and honey (मधु).",
               "मधु = honey.",
               "मधु = honey."),
          "मधु = honey; with सर्पिः (ghee) it makes the pair सर्पिर्मधु."),
        mcq("discriminate", 3, "By the card, what does the ending of सर्पिर्मधुभ्याम् show?",
            ("Instrumental dual: with the two", "Labelled inst. du., a dvandva of two members: ghee and honey."),
            [("Plural: with many kinds of ghee", "Two members, ghee and honey, take the dual."),
             ("Genitive: of ghee and of honey", "The genitive dual would end in -योः."),
             ("Nominative: the one who drinks", "The drinker is the pregnant woman; this word is instrumental.")],
            "-भ्याम् here = with the two: ghee and honey.",
            "सर्पिर्मधुभ्याम् = inst. du.: with ghee and honey."),
        mcq("apply", 4, "Which split of सर्पिर्मधु is right?",
            ("सर्पिः + मधु", "A visarga after इ becomes र् before the voiced म."),
            [("सर्प + इर्मधु", "इर्मधु is not a word; the word is मधु, honey."),
             ("सर्पी + रमधु", "Neither piece is a word of the card."),
             ("सर्पिम् + मधु", "A final म् would give सर्पिम्मधु, with no र्.")],
            "सर्पिः (ghee) + मधु (honey): इः → इर् before a voiced sound.",
            "इः + voiced sound → इर्."),
        mcq("transfer", 5, "By the rule of सर्पिर्मधु, how is धनुः + धरः (bow-holder) written when joined?",
            ("धनुर्धरः", "A visarga after उ becomes र् before the voiced ध."),
            [("धनुधरः", "The visarga is not simply dropped after उ."),
             ("धनुस्धरः", "स् stays only before त/थ, not before ध."),
             ("धनूधरः", "The उ is not lengthened; the visarga becomes र्.")],
            "धनुः + धरः = धनुर्धरः, like सर्पिः + मधु = सर्पिर्मधु.",
            "इः/उः + voiced sound → इर्/उर्.",
            teaches="A visarga after इ or उ becomes र् before a voiced sound: सर्पिः + मधु → सर्पिर्मधु."),
    ],
}

# ---------------------------------------------------------------- unit 9
AUTHORED["9"] = {
    "title": "चतुर्थेऽक्षमात्रनवनीतयुक्तं",
    "question": "By unit 9, what is joined (to the milk) in the fourth month, and in what measure?",
    "rule": ("In the fourth (month), (the milk) joined with fresh butter (नवनीत) in the measure of an akṣa (अक्ष, a measure "
             "of weight, a synonym of karṣa). चतुर्थे + अक्ष → चतुर्थेऽक्ष."),
    "limits": ("The verb and the substance (the milk of units 7, 8) are carried over; neither is printed. The card gives no "
               "modern weight for akṣa. Medium confidence."),
    "explain_hi": ("चौथे (मास) में (वही दूध) अक्ष-मात्रा नवनीत (ताज़ा मक्खन) से युक्त। "
                   "अक्ष तौल का एक माप है, कर्ष का पर्याय (शब्दकोश के अनुसार); आधुनिक तौल यहाँ नहीं दी गई। "
                   "क्रिया और द्रव्य (दूध) पिछली इकाइयों से चले आते हैं, यहाँ छपे नहीं। "
                   "‘चतुर्थेऽक्ष’ में चतुर्थे + अक्ष है: ए के बाद अ लुप्त होता है और ऽ (अवग्रह) से दिखाया जाता है।"),
    "hook": "चौथा मास: अक्ष-भर नवनीत।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 9, what is joined (to the milk) in the fourth (month)?",
            ("Fresh butter (नवनीत), an akṣa in measure", "अक्षमात्रनवनीतयुक्तम्."),
            [("Ghee and honey (सर्पिः, मधु), both together", "Ghee and honey are unit 8, the third."),
             ("Sweet medicines (मधुरौषध), cooked into it", "Sweet medicines are unit 7, the second."),
             ("Śāliparṇī and palāśa, boiled into ghee", "These are unit 3, the first month.")],
            "In the fourth: fresh butter in the measure of an akṣa.",
            "चतुर्थे अक्षमात्रनवनीतयुक्तम्."),
        order(1, "Put the members of unit 9's single printed word in order.",
              ["चतुर्थे", "अक्ष", "मात्र", "नवनीत", "युक्तम्"],
              "In the fourth, akṣa, measure, fresh butter, joined with.",
              "चतुर्थे → अक्ष → मात्र → नवनीत → युक्तम्."),
        match(2, "Match each member of unit 9 to its meaning.",
              [["चतुर्थे", "in the fourth"], ["अक्ष", "a measure of weight (= karṣa)"], ["मात्र", "measure"],
               ["नवनीत", "fresh butter"], ["युक्तम्", "joined with"]],
              "Five members make the one printed word.",
              "चतुर्थे, अक्ष, मात्र, नवनीत, युक्तम्.", role="extend",
              teaches="अक्ष here is a measure of weight, a synonym of karṣa; अक्षमात्र = in the measure of an akṣa."),
        mcq("discriminate", 3, "Which split of चतुर्थेऽक्ष is right?",
            ("चतुर्थे + अक्ष", "ए + अ: the अ is dropped and shown by ऽ."),
            [("चतुर्थः + अक्ष", "अः + अ would give चतुर्थोऽक्ष, with ओ."),
             ("चतुर्थ + एक्ष", "एक्ष is not a word; the word is अक्ष."),
             ("चतुर्थे + आक्ष", "आक्ष is not the card's word, and the avagraha marks a dropped short अ.")],
            "चतुर्थे (in the fourth) + अक्ष (a measure): ए + अ → एऽ.",
            "final ए + अ → एऽ."),
        mcq("apply", 4, "What does the sign ऽ in चतुर्थेऽक्ष show?",
            ("A short अ dropped after ए", "The avagraha marks the elided अ of अक्ष."),
            [("A long vowel to be sounded", "ऽ does not mark length."),
             ("A pause, like a comma", "ऽ is not punctuation."),
             ("A letter lost in the scan", "The note says the avagraha is printed correctly.")],
            "ऽ = a short अ dropped after ए (or ओ).",
            "ऽ = elided अ."),
        mcq("transfer", 5, "By the rule of चतुर्थेऽक्ष, how is वने + अस्मिन् (in this forest) written when joined?",
            ("वनेऽस्मिन्", "ए + अ: the अ drops and is shown by ऽ."),
            [("वनयस्मिन्", "ए + अ here does not give य."),
             ("वनास्मिन्", "ए + अ does not give आ."),
             ("वनोऽस्मिन्", "ओऽ comes from अः or ओ, not from ए.")],
            "वने + अस्मिन् = वनेऽस्मिन्, like चतुर्थे + अक्ष = चतुर्थेऽक्ष.",
            "final ए + अ → एऽ.",
            teaches="A word-final ए before a short अ drops the अ, shown by ऽ: चतुर्थे + अक्ष → चतुर्थेऽक्ष."),
    ],
}

# ---------------------------------------------------------------- unit 10
AUTHORED["10"] = {
    "title": "पंचमे क्षीरसर्पिः",
    "question": "By unit 10, what is named for the fifth month?",
    "rule": ("In the fifth (month), क्षीरसर्पिस्: milk-ghee, taken as ghee of milk. The verb is carried over. Printed पंचमे "
             "= पञ्चमे (anusvara before च stands for ञ्)."),
    "limits": ("The compound may also be read as milk and ghee; the card does not decide it, and no question rests on it. "
               "No verb or amount is printed. Medium confidence."),
    "explain_hi": ("पाँचवें (मास) में क्षीरसर्पिः, यानी दूध का घी (क्षीर से बना सर्पि)। "
                   "इस समास को ‘दूध और घी’ (द्वन्द्व) भी पढ़ा जा सकता है; डेटा सरल अर्थ ‘दूध का घी’ लेता है, तय नहीं। "
                   "क्रिया पिछली इकाइयों से चली आती है; मात्रा नहीं दी गई। "
                   "छपा ‘पंचमे’ = पञ्चमे: च से पहले अनुस्वार ञ् का ही दूसरा लेखन है।"),
    "hook": "पाँचवाँ मास: क्षीरसर्पि।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 10, what is named for the fifth (month)?",
            ("क्षीरसर्पिः, milk-ghee", "पंचमे क्षीरसर्पिः."),
            [("नवनीत, fresh butter", "Fresh butter is unit 9, the fourth."),
             ("मधु, honey, with milk", "Honey is unit 8, the third."),
             ("जल, cool water alone", "Cool water is the after-drink of unit 3.")],
            "The fifth (month) names क्षीरसर्पिः.",
            "पञ्चमे क्षीरसर्पिः."),
        match(1, "Match each member of unit 10 to its meaning.",
              [["पञ्चमे", "in the fifth"], ["क्षीर", "milk"], ["सर्पिः", "ghee"]],
              "Three members make the whole line.",
              "पञ्चमे, क्षीर, सर्पिः."),
        T(fill(2, "In unit 10, the word for ghee is ____ (type it in Devanagari or in English letters, e.g. dharma).",
               accepts("सर्पिः", None, "सर्पिस्"),
               "क्षीरसर्पिः = क्षीर (milk) + सर्पिः (ghee).",
               "सर्पिः = ghee.",
               "सर्पिः = ghee."),
          "सर्पिः (stem सर्पिस्) = ghee."),
        multi("discriminate", 3, "Which statements are true of unit 10?",
              [("It prints no verb", "Right: the verb is carried over."),
               ("It gives a measure in akṣa", "The akṣa measure is unit 9."),
               ("It names honey", "Honey is unit 8."),
               ("It names the fifth (month)", "Right: पंचमे, in the fifth.")],
              [0, 3],
              "A two-word line: the fifth (month) and milk-ghee, with no verb.",
              "पंचमे क्षीरसर्पिः (no verb)."),
        mcq("apply", 4, "Why is the printed पंचमे the same word as पञ्चमे?",
            ("Anusvara before च stands for ञ्", "An anusvara before a stop stands for that class's nasal."),
            [("पंचमे is a dual form of पञ्चमे", "The anusvara is spelling only; it changes no ending."),
             ("The anusvara marks a long vowel", "Anusvara is a nasal, not a length mark."),
             ("पंचमे is a misprint for पचमे", "There is no word पचमे; the nasal is real.")],
            "पंचमे = पञ्चमे: anusvara before च = ञ्.",
            "anusvara before a stop = that class's nasal."),
        mcq("transfer", 5, "By पंचमे = पञ्चमे, how is printed संकल्प written with the class nasal?",
            ("सङ्कल्प", "Before क (the क-class) the nasal is ङ्."),
            [("सञ्कल्प", "ञ् belongs before च-class letters, not before क."),
             ("सन्कल्प", "न् belongs before त-class letters, not before क."),
             ("सम्कल्प", "म् belongs before प-class letters, not before क.")],
            "संकल्प = सङ्कल्प, as पंचमे = पञ्चमे.",
            "anusvara before a stop = that class's nasal.",
            teaches="An anusvara before a stop may be written as that stop's class nasal: पंचमे = पञ्चमे, संकल्प = सङ्कल्प."),
    ],
}

# ---------------------------------------------------------------- unit 11
AUTHORED["11"] = {
    "title": "षष्ठे तदेव मधुरौषधसिद्धं",
    "question": "By unit 11, how is that same (drink) prepared in the sixth month?",
    "rule": ("In the sixth (month), that same (तदेव), cooked with sweet medicines (मधुरौषधसिद्धम्). The verb is carried over. "
             "तत् + एव → तदेव (त् → द् before a vowel)."),
    "limits": ("Whether तदेव means the milk-ghee of unit 10 or the milk of unit 7 is not stated; no question rests on it. "
               "The sweet medicines are not named. Medium confidence."),
    "explain_hi": ("छठे (मास) में वही, मधुर औषधों से पकाया हुआ। "
                   "‘तदेव’ (वही) इकाई 10 के क्षीरसर्पि की ओर है या इकाई 7 के दूध की ओर, यह नहीं बताया गया; इसलिए उस पर प्रश्न नहीं। "
                   "क्रिया पिछली इकाइयों से चली आती है। मधुर औषधों के नाम नहीं दिए गए। "
                   "‘तदेव’ में तत् + एव है: स्वर से पहले त् → द्।"),
    "hook": "छठा मास: वही, मधुर औषधों से सिद्ध।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 11, how is that same (drink) prepared in the sixth (month)?",
            ("Cooked with sweet medicines", "तदेव मधुरौषधसिद्धम्."),
            [("Joined with fresh butter", "Fresh butter is unit 9."),
             ("Taken with ghee and honey", "Ghee and honey are unit 8."),
             ("Boiled with śāliparṇī", "Śāliparṇī is unit 3.")],
            "In the sixth, that same, cooked with sweet medicines.",
            "षष्ठे तदेव मधुरौषधसिद्धम्."),
        order(1, "Put the words of unit 11 in the line's order.",
              ["षष्ठे", "तत्", "एव", "मधुरौषधसिद्धम्"],
              "In the sixth, that, same, cooked with sweet medicines.",
              "षष्ठे → तत् → एव → मधुरौषधसिद्धम्."),
        match(2, "Match each word of unit 11 to its meaning.",
              [["षष्ठे", "in the sixth"], ["तत्", "that"], ["एव", "same, very"], ["मधुर", "sweet"],
               ["सिद्धम्", "cooked"]],
              "Five members carry the whole line.",
              "षष्ठे, तत्, एव, मधुर, सिद्धम्.", role="extend",
              teaches="एव stresses the word before it: तत् एव = that very, the same."),
        mcq("discriminate", 3, "Which split of तदेव is right?",
            ("तत् + एव", "त् → द् before a vowel: तत् + एव = तदेव."),
            [("तद + एव", "अ + ए would give ऐ: तदैव, not तदेव."),
             ("तदे + एव", "There is no word तदे."),
             ("त + देव", "देव (god) is not the card's word; the words are तत् and एव.")],
            "तत् (that) + एव (same): त् → द् before a vowel.",
            "final त् + vowel → द्."),
        multi("apply", 4, "Which of these are printed in unit 11?",
              [("पिबेत्, should drink", "Not printed: the verb is carried over."),
               ("षष्ठे, in the sixth", "Right: printed."),
               ("मधुरौषधसिद्धं, cooked with sweet medicines", "Right: printed."),
               ("नवनीत, fresh butter", "Not printed: fresh butter is unit 9.")],
              [1, 2],
              "Printed: षष्ठे, तदेव, मधुरौषधसिद्धं; the verb is carried over.",
              "षष्ठे तदेव मधुरौषधसिद्धं."),
        mcq("transfer", 5, "By the rule of तदेव, how is जगत् + ईशः (lord of the world) written when joined?",
            ("जगदीशः", "त् → द् before a vowel, as तत् + एव."),
            [("जगतीशः", "A final त् before a vowel becomes द्, not त्."),
             ("जगदेशः", "The ई does not change to ए."),
             ("जगन्नीशः", "त् may become न् (optionally) only before a nasal.")],
            "जगत् + ईशः = जगदीशः, like तत् + एव = तदेव.",
            "final त् + vowel → द्.",
            teaches="A word-final त् becomes द् before a vowel: तत् + एव → तदेव."),
    ],
}

# ---------------------------------------------------------------- unit 12
AUTHORED["12"] = {
    "title": "सप्तमे च",
    "question": "What does unit 12 print for the seventh month?",
    "rule": ("Unit 12 prints only सप्तमे च: and in the seventh (month). सप्तमे is the locative singular of the ordinal "
             "सप्तम: in the seventh. No substance or verb is printed."),
    "limits": ("Incomplete as printed: nothing is given for the seventh month in this unit, and nothing is supplied. "
               "Whether content was lost or follows is not settled; no question rests on it."),
    "explain_hi": ("यह इकाई केवल ‘सप्तमे च’ छापती है: ‘और सातवें (मास) में’। "
                   "कोई द्रव्य या क्रिया यहाँ नहीं दी गई, और कुछ जोड़ा भी नहीं गया। "
                   "‘सप्तमे’ क्रमसंख्या ‘सप्तम’ की सप्तमी एकवचन है: ‘सातवें में’। "
                   "इकाई 2 से यहाँ तक मास-क्रम चलता है: प्रथमे, द्वितीये, तृतीये, चतुर्थे, पञ्चमे, षष्ठे, सप्तमे।"),
    "hook": "सप्तमे च: सातवाँ मास, पर यहाँ कुछ और नहीं।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 12, which month is named?",
            ("The seventh (सप्तमे)", "सप्तमे च: and in the seventh."),
            [("The sixth (षष्ठे)", "षष्ठे is unit 11."),
             ("The eighth (अष्टमे)", "No eighth is named here."),
             ("The fifth (पञ्चमे)", "पञ्चमे is unit 10.")],
            "Unit 12 names the seventh (month).",
            "सप्तमे = in the seventh."),
        order(1, "Put these ordinal words in counting order, ending with unit 12's word.",
              ["तृतीये", "चतुर्थे", "पञ्चमे", "षष्ठे", "सप्तमे"],
              "Third, fourth, fifth, sixth, seventh.",
              "तृतीये → चतुर्थे → पञ्चमे → षष्ठे → सप्तमे."),
        T(fill(2, "And in the seventh: ____ च (type it in Devanagari or in English letters, e.g. dharma).",
               accepts("सप्तमे"),
               "The line is सप्तमे च.",
               "सप्तमे = in the seventh.",
               "सप्तमे = in the seventh."),
          "सप्तमे = in the seventh: locative singular of the ordinal सप्तम."),
        mcq("discriminate", 3, "What does unit 12 print for the seventh (month)?",
            ("Only सप्तमे च, nothing more", "The note: no substance or verb is given."),
            [("Milk with ghee and honey", "That is unit 8, the third."),
             ("Fresh butter, an akṣa in measure", "That is unit 9, the fourth."),
             ("Milk cooked with sweet medicines", "That is unit 7, the second (month).")],
            "Unit 12 prints only सप्तमे च.",
            "सप्तमे च (nothing more)."),
        mcq("apply", 4, "By the card, what form is सप्तमे?",
            ("Locative singular: in the seventh", "Labelled loc. sg."),
            [("Nominative singular: the seventh one", "That would be सप्तमः."),
             ("Accusative singular: the seventh (object)", "That would be सप्तमम्."),
             ("Instrumental singular: by the seventh", "That would be सप्तमेन.")],
            "सप्तमे = in the seventh (locative).",
            "-ए (a-stem) = locative singular: in."),
        mcq("transfer", 5, "By सप्तमे, how is in the eighth (month), from अष्टम, said?",
            ("अष्टमे", "Locative singular -ए, as सप्तम → सप्तमे."),
            [("अष्टमः", "अष्टमः is nominative: the eighth."),
             ("अष्टमेन", "अष्टमेन is instrumental: by the eighth."),
             ("अष्टमम्", "अष्टमम् is accusative.")],
            "अष्टम → अष्टमे = in the eighth, like सप्तम → सप्तमे.",
            "a-stem locative singular = -ए.",
            teaches="The locative singular of an a-stem ordinal ends in -ए: सप्तम → सप्तमे (in the seventh), अष्टम → अष्टमे."),
    ],
}

# ---------------------------------------------------------------- unit 13
AUTHORED["13"] = {
    "title": "मातुर्विदाहो भवतीति स्त्रियो भाषंते",
    "question": "By unit 13, what do women say causes the mother's burning in that month, and what does Ātreya answer?",
    "rule": ("In that (seventh) month, women say the mother's burning (विदाह) comes through the arising of the embryo's "
             "hair (केशोत्पत्ति); the venerable Ātreya says not so (न इति)."),
    "limits": ("Ātreya's own reason is not given in this unit. विदाह = burning, probably a heartburn-like sensation; the text "
               "does not define it. The verb for Ātreya is not printed; says is supplied. Medium confidence."),
    "explain_hi": ("उस (सातवें) मास में स्त्रियाँ कहती हैं कि गर्भ के केशों की उत्पत्ति से माता को विदाह (जलन) होता है। "
                   "भगवान् आत्रेय कहते हैं: ‘ऐसा नहीं’ (नेति)। "
                   "आत्रेय के लिए क्रिया छपी नहीं, ‘भाषन्ते’ से समझी जाती है। "
                   "आत्रेय का अपना कारण इस इकाई में नहीं है। "
                   "विदाह = जलन, सम्भवतः छाती की जलन जैसी अनुभूति; ग्रन्थ इसकी परिभाषा नहीं देता।"),
    "hook": "स्त्रियाँ: केश उगने से जलन; आत्रेय: नहीं।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 13, what do the women say causes the mother's burning (विदाह)?",
            ("The arising of the embryo's hair", "गर्भस्य केशोत्पत्त्या मातुर्विदाहो भवति."),
            [("The mother's diet in that month", "The women name no food as the cause."),
             ("The turning of the embryo", "No turning is named in unit 13."),
             ("The ghee and honey she drinks", "Ghee and honey are unit 8, and no cause is tied to them.")],
            "The women's view: the embryo's hair arising causes the mother's burning.",
            "केशोत्पत्त्या … विदाहः."),
        order(1, "Put these printed parts of unit 13 in the line's order.",
              ["तस्मिंश्च", "गर्भस्यकेशोत्पत्त्या", "मातुर्विदाहो भवतीति", "स्त्रियो भाषंते", "नेति",
               "भगवान्आत्रेयः"],
              "And in that, by the arising of the embryo's hair, the mother's burning occurs, so women say; not so, Ātreya.",
              "तस्मिंश्च → गर्भस्यकेशोत्पत्त्या → मातुर्विदाहो भवतीति → स्त्रियो भाषंते → नेति → भगवान्आत्रेयः."),
        match(2, "Match each word of unit 13 to its meaning.",
              [["केश", "hair"], ["उत्पत्ति", "arising"], ["मातुः", "of the mother"], ["विदाह", "burning"],
               ["स्त्रियः", "women"], ["भाषन्ते", "say"]],
              "These words carry the women's claim.",
              "केश, उत्पत्ति, मातुः, विदाह, स्त्रियः, भाषन्ते.", role="extend",
              teaches="विदाह = burning, probably a heartburn-like sensation; the text gives no further definition."),
        mcq("discriminate", 3, "In unit 13, who holds which view?",
            ("Women: hair causes it; Ātreya: not so", "स्त्रियो भाषंते … नेति भगवानात्रेयः."),
            [("Ātreya: hair causes it; women: not so", "The roles are reversed: the women make the claim."),
             ("Women and Ātreya both: hair causes it", "Ātreya says नेति, not so."),
             ("Ātreya gives the true cause here", "His own reason is not in this unit.")],
            "The women claim; Ātreya denies.",
            "स्त्रियो भाषन्ते … नेति आत्रेयः."),
        multi("apply", 4, "Which sandhi joins from unit 13 are stated rightly?",
              [("न + इति → नैति (अ + इ → ऐ)", "Wrong: अ + इ → ए, giving नेति."),
               ("विदाहः + भवति → विदाहर्भवति", "Wrong: अः before a voiced sound → ओ: विदाहो भवति."),
               ("भवति + इति → भवतीति (इ + इ → ई)", "Right: two इ make ई."),
               ("मातुः + विदाहः → मातुर्विदाहः", "Right: उः before the voiced व → उर्.")],
              [2, 3],
              "भवतीति and मातुर्विदाहः are right; नेति and विदाहो are the true forms of the others.",
              "अ + इ → ए; अः + voiced → ओ; इ + इ → ई; उः + voiced → उर्."),
        mcq("transfer", 5, "By the rule of नेति, how is न + इच्छति (does not wish) written when joined?",
            ("नेच्छति", "अ + इ → ए, as न + इति → नेति."),
            [("नैच्छति", "ऐ comes from अ + ए/ऐ, not from अ + इ."),
             ("नीच्छति", "The अ is not dropped; अ + इ gives ए."),
             ("नयिच्छति", "No य् is put between अ and इ.")],
            "न + इच्छति = नेच्छति, like न + इति = नेति.",
            "अ + इ → ए.",
            teaches="अ followed by इ joins as ए: न + इति → नेति."),
    ],
}

# ===================================================================== NOTES_HI
NOTES_HI = {
    "1": ("गद्य-पंक्ति; विश्वास उच्च; कोई पाठ-चिह्न नहीं। अध्याय का आरम्भ-सूत्र। ‘गर्भोपचरणीय’ अध्याय का नाम माना गया। "
          "छपा ‘गर्भोपचरणीयं’, ‘शारीरं’ = -म् (व्यंजन से पहले अनुस्वार)। सन्धि जाँची: अथ + अतः → अथातः (अ + अ → आ); "
          "अतः + गर्भ… → अतो गर्भ… (घोष से पहले अः → ओ); गर्भ + उपचरणीयम् → गर्भोपचरणीयम् (अ + उ → ओ)।"),
    "2": ("गद्य-पंक्ति; विश्वास उच्च; कोई पाठ-चिह्न नहीं। ‘प्रथमेमासि’ दो शब्द एक साथ छपे हैं (प्रथमे मासि), सन्धि या दोष नहीं। "
          "संस्कार का प्रकार, मात्रा और ‘काले’ का समय नहीं बताया गया। सन्धि जाँची: क्षीरम् + उपसंस्कृतम् → क्षीरमुपसंस्कृतम्; "
          "मात्रावत् + शीतम् → मात्रावच्छीतम् (यहाँ त् + श → च्छ लिखा गया)।"),
    "3": ("विश्वास मध्यम। पाठ-चिह्न: ‘कथित’ (कहा हुआ) → सम्भवतः ‘क्वथित’ (उबाला हुआ), मुद्रण में व छूटा; ‘उबाला हुआ’ अनुवाद इसी अनुमान पर है। "
          "शालिपर्णी = Desmodium gangeticum (मानक); पलाश = Butea monosperma (सम्भावित; ‘पत्ता’ अर्थ भी सम्भव)। "
          "‘तस्मिन्’ = उस (मास) में; ‘आद्यं द्वादशरात्रम्’ अवधि का द्वितीया-प्रयोग माना गया। बहुव्रीहि ‘कनक…अनुपानम्’ घी का विशेषण। "
          "सन्धि जाँची: तस्मिन् + अपि → तस्मिन्नपि (ह्रस्व स्वर के बाद न् द्वित्व); च + आद्यम् → चाद्यम् (अ + आ → आ); "
          "क्षीर + उद्भवम् → क्षीरोद्भवम्; शीत + उदक → शीतोदक (अ + उ → ओ); उदक + अनुपानम् → उदकानुपानम् (अ + अ → आ)।"),
    "4": ("विश्वास मध्यम। पाठ-चिह्न: ‘खादु’ कोई शब्द नहीं → सम्भवतः ‘स्वादु’ (मीठा), ख/स्व का भ्रम; अनुवाद इसी अनुमान पर। "
          "वाक्य अधूरा-सा: खाद्य पदार्थों के नाम और ‘आहारयेत्’ का कर्ता नहीं दिए गए; विशेषणों की विभक्ति को आहार की मानकर पढ़ा गया। "
          "सात्म्य = उसके अनुकूल, आगे परिभाषित नहीं। सन्धि जाँची: प्रातर् + आहारयेत् → प्रातराहारयेत्।"),
    "5": ("गद्य-पंक्ति; विश्वास उच्च; कोई पाठ-चिह्न नहीं। कर्ता (गर्भिणी) इकाई 2 से समझा गया। छपा ‘अभ्यंग’ = अभ्यङ्ग (अनुस्वार = ङ्)। "
          "सन्धि जाँची: च + अभ्यङ्ग → चाभ्यङ्ग (अ + अ → आ); अभ्यङ्ग + उद्वर्तनानि → अभ्यङ्गोद्वर्तनानि (अ + उ → ओ)।"),
    "6": ("विश्वास निम्न। पाठ-चिह्न: ‘आर्पचमान्’ कोई शब्द नहीं; अक्षरों के आकार से ‘आपञ्चमात्’ (पाँचवें तक) का अनुमान है, पर यह केवल अनुमान; "
          "निश्चित केवल इतना कि कोई समय-सीमा है। ‘यथोक्त’ पहले कही बात की ओर है, जो इस अंश में नहीं। दोषकर = दोष उत्पन्न करने वाले। "
          "सन्धि जाँची: यथा + उक्तानि → यथोक्तानि (आ + उ → ओ); परिहरेत् + आ… → परिहरेदा… (स्वर से पहले त् → द्)। "
          "अवधि पर कोई प्रश्न नहीं।"),
    "7": ("गद्य-पंक्ति; विश्वास उच्च; कोई पाठ-चिह्न नहीं। ‘द्वितीये’ के बाद ‘मास’ इकाई 2 से समझा गया। मधुर औषध यहाँ गिनाए नहीं गए, "
          "कोई पहचान नहीं। सन्धि जाँची: मधुर + औषध → मधुरौषध (अ + औ → औ); छपा ‘सिद्धं’ = सिद्धम् (प से पहले अनुस्वार)।"),
    "8": ("विश्वास मध्यम; कोई पाठ-चिह्न नहीं। क्रिया ‘पिबेत्’ पिछली इकाई से; अनुवाद में भी नहीं जोड़ी गई। ‘तदेव’ = इकाई 7 का दूध (डेटा की टिप्पणी)। "
          "‘सर्पिर्मधुभ्याम्’ तृतीया द्विवचन, द्वन्द्व। छपा ‘मधुभ्यां’ = मधुभ्याम्। सन्धि जाँची: तत् + एव → तदेव (त् → द्); "
          "सर्पिः + मधु → सर्पिर्मधु (इ के बाद विसर्ग → र् घोष से पहले)।"),
    "9": ("विश्वास मध्यम; कोई पाठ-चिह्न नहीं। क्रिया और द्रव्य (इकाई 7, 8 का दूध) पिछली इकाइयों से; जोड़े नहीं गए। अवग्रह ठीक छपा है। "
          "अक्ष = तौल का माप, कर्ष का पर्याय (शब्दकोश)। सन्धि जाँची: चतुर्थे + अक्ष → चतुर्थेऽक्ष (ए के बाद अ लुप्त, ऽ से सूचित)।"),
    "10": ("विश्वास मध्यम; कोई पाठ-चिह्न नहीं। क्रिया पिछली इकाइयों से। ‘क्षीरसर्पिः’ दो प्रकार से पढ़ा जा सकता है: ‘दूध का घी’ (तत्पुरुष, लिया गया; "
           "तुलना: इकाई 3 का ‘क्षीरोद्भवं सर्पिः’) या ‘दूध और घी’ (द्वन्द्व); इस पर प्रश्न नहीं। छपा ‘पंचमे’ = पञ्चमे (अनुस्वार = ञ्)।"),
    "11": ("विश्वास मध्यम; कोई पाठ-चिह्न नहीं। क्रिया पिछली इकाइयों से। ‘तदेव’ इकाई 10 के क्षीरसर्पि की ओर है या इकाई 7 के दूध की ओर, "
           "डेटा खुला छोड़ता है; इस पर प्रश्न नहीं। सन्धि जाँची: तत् + एव → तदेव (त् → द्); मधुर + औषध → मधुरौषध (अ + औ → औ)।"),
    "12": ("विश्वास मध्यम; कोई पाठ-चिह्न नहीं। छपे रूप में अधूरा: सातवें मास के लिए न द्रव्य, न क्रिया; कुछ जोड़ा नहीं गया। "
           "डेटा की टिप्पणी (GROUPING): सम्भवतः अगली इकाई में चलता है या सामग्री छूट गई; तय नहीं, इस पर प्रश्न नहीं।"),
    "13": ("विश्वास मध्यम; कोई पाठ-चिह्न नहीं। ‘तस्मिन्’ = उस (सातवें, इकाई 12 का) मास में। आत्रेय के लिए ‘कहते हैं’ क्रिया ‘भाषन्ते’ से समझी गई। "
           "छपा ‘गर्भस्यकेशोत्पत्त्या’ = गर्भस्य केशोत्पत्त्या (केवल शब्द-विभाग); छपा ‘भगवान्आत्रेयः’ में हलन्त के बाद स्थान/जोड़ छूटा, "
           "पूरा रूप भगवानात्रेयः; ‘भाषंते’ = भाषन्ते। विदाह = जलन, सम्भवतः छाती की जलन जैसी। सन्धि जाँची: तस्मिन् + च → तस्मिंश्च; "
           "केश + उत्पत्त्या → केशोत्पत्त्या (अ + उ → ओ); मातुः + विदाहः → मातुर्विदाहः (उ के बाद विसर्ग → र्); विदाहः + भवति → "
           "विदाहो भवति (अः → ओ घोष से पहले); भवति + इति → भवतीति (इ + इ → ई); स्त्रियः + भाषन्ते → स्त्रियो भाषन्ते; न + इति → नेति (अ + इ → ए)।"),
}

# ===================================================================== AIDS
AIDS = {
    "1": {
        "chunks": "अथातो | गर्भोपचरणीयं | शारीरं | व्याख्यास्यामः",
        "sandhi": "अ + अ → आ: अथ + अतः → अथातः · घोष से पहले अः → ओ: अतः + ग → अतो ग · अ + उ → ओ: गर्भ + उपचरणीयम् → गर्भोपचरणीयम्।",
        "frame": "कब: अथ अतः (अब, इसलिए) → क्या: गर्भोपचरणीयं शारीरम् (विषय) → क्रिया: व्याख्यास्यामः (हम व्याख्या करेंगे)।",
    },
    "2": {
        "diagram": {"groups": [{"label": "प्रथमे मासि गर्भिणी पिए: दूध (क्रम से)",
                                "items": ["उपसंस्कृत (संस्कार किया)", "मात्रावत् (मात्रा से)", "शीत (ठण्डा)", "काले (समय पर)"]}]},
        "chunks": "प्रथमेमासि | गर्भिणी | क्षीरमुपसंस्कृतं | मात्रावच्छीतं | काले | पिबेत्",
        "sandhi": "म् + स्वर: क्षीरम् + उपसंस्कृतम् → क्षीरमुपसंस्कृतम् · त् + श → च्छ (यहाँ ऐसे छपा): मात्रावत् + शीतम् → मात्रावच्छीतम्।",
        "anchors": "याद-सूत्र: ‘उ-मा-शी-का’ — उपसंस्कृत, मात्रावत्, शीत, काले: दूध के तीन गुण और पीने का समय, क्रम से। (मेरी याद-पद्धति)",
    },
    "3": {
        "chain": {"steps": ["उस (पहले) मास में, पहली बारह रातें", "दूध से उत्पन्न सर्पि (घी)",
                            "शालिपर्णी (मानक) और पलाश (सम्भावित) के साथ उबाला", "पिए",
                            "अनुपान: सोना-चाँदी वाला ठण्डा जल (तैयारी का शब्द संदिग्ध)"]},
        "chunks": "तस्मिन्नपि चाद्यं द्वादशरात्रं | क्षीरोद्भवं सर्पिः | शालिपर्णीपलाशाभ्यां शृतं | कनकरजतकथितशीतोदकानुपानं | पिबेत्",
        "sandhi": "ह्रस्व स्वर के बाद न् + स्वर → न्न: तस्मिन् + अपि → तस्मिन्नपि · अ + आ → आ: च + आद्यम् → चाद्यम् · अ + उ → ओ: क्षीर + उद्भवम् → क्षीरोद्भवम्।",
        "anchors": "याद-सूत्र: ‘बारह रातें, घी; बाद में ठण्डा जल’ — मुख्य पेय घी, अनुपान जल। (मेरी याद-पद्धति)",
    },
    "4": {
        "diagram": {"groups": [
            {"label": "आहार कैसा (क्रम से)", "items": ["खादुशीत (खादु संदिग्ध; अनुमान: स्वादु)", "द्रवप्राय (अधिकतर तरल)", "सात्म्य (अनुकूल)"]},
            {"label": "कब", "items": ["सायं", "प्रातः"]}]},
        "chunks": "खादुशीतं | द्रवप्रायं | सात्म्यं च | सायं | प्रातराहारयेत्",
        "sandhi": "र् स्वर से पहले बना रहता है: प्रातर् + आहारयेत् → प्रातराहारयेत्।",
    },
    "5": {
        "chunks": "न चाभ्यंगोद्वर्तनानि | सेवेत",
        "sandhi": "अ + अ → आ: च + अभ्यङ्ग → चाभ्यङ्ग · अ + उ → ओ: अभ्यङ्ग + उद्वर्तनानि → अभ्यङ्गोद्वर्तनानि।",
        "frame": "निषेध: न + विधिलिङ् (सेवेत) = सेवन न करे; कर्म: अभ्यङ्ग और उद्वर्तन; कर्ता (गर्भिणी) इकाई 2 से।",
    },
    "6": {
        "chunks": "यथोक्तानि च | दोषकराणि | परिहरेत् | आर्पचमान्मासात् (?)",
        "frame": "कर्म: यथोक्तानि दोषकराणि (कहे गए दोषकर) → क्रिया: परिहरेत् (त्यागे) → अवधि: संदिग्ध शब्द (अनुमान: पाँचवें मास तक)।",
        "sandhi": "आ + उ → ओ: यथा + उक्तानि → यथोक्तानि · स्वर से पहले त् → द्: परिहरेत् + आ… → परिहरेदा…।",
    },
    "7": {
        "chunks": "विशेषेण | द्वितीये | मधुरौषधसिद्धं | पयः | पिबेत्",
        "sandhi": "अ + औ → औ: मधुर + औषध → मधुरौषध।",
        "frame": "कब: विशेषेण द्वितीये (विशेषकर दूसरे में) → क्या: पयः (दूध) → कैसा: मधुरौषधसिद्धम् (मधुर औषधों से पका) → क्रिया: पिबेत्।",
    },
    "8": {
        "diagram": {"groups": [{"label": "तृतीये: तदेव (वही दूध)", "items": ["सर्पि (घी) के साथ", "मधु के साथ"]}]},
        "chunks": "तृतीये | तदेव | सर्पिर्मधुभ्यां",
        "sandhi": "स्वर से पहले त् → द्: तत् + एव → तदेव · इ के बाद विसर्ग → र् घोष से पहले: सर्पिः + मधु → सर्पिर्मधु।",
    },
    "9": {
        "chain": {"steps": ["चतुर्थे (चौथे में)", "अक्ष-मात्र (अक्ष भर)", "नवनीत (ताज़ा मक्खन)", "युक्त (मिला हुआ)"]},
        "chunks": "चतुर्थेऽक्ष | मात्र | नवनीत | युक्तं",
        "sandhi": "ए + अ → एऽ: चतुर्थे + अक्ष → चतुर्थेऽक्ष (अ लुप्त, ऽ से सूचित)।",
    },
    "10": {
        "chunks": "पंचमे | क्षीरसर्पिः",
        "sandhi": "अनुस्वार = वर्ग का नासिक्य: पंचमे = पञ्चमे (च से पहले ञ्)।",
        "anchors": "याद-सूत्र: ‘पाँचवें में क्षीर-सर्पि’ — पंचमे क्षीरसर्पिः। (मेरी याद-पद्धति, केवल याद के लिए)",
    },
    "11": {
        "chunks": "षष्ठे | तदेव | मधुरौषधसिद्धं",
        "sandhi": "स्वर से पहले त् → द्: तत् + एव → तदेव · अ + औ → औ: मधुर + औषध → मधुरौषध।",
        "frame": "कब: षष्ठे → क्या: तदेव (वही; कौन-सा, खुला) → कैसा: मधुरौषधसिद्धम्; क्रिया पिछली इकाइयों से।",
    },
    "12": {
        "chunks": "सप्तमे | च",
        "frame": "केवल समय: सप्तमे (सातवें में) + च (और); द्रव्य और क्रिया छपे नहीं।",
        "anchors": "याद-सूत्र: मास-क्रम प्रथमे → द्वितीये → तृतीये → चतुर्थे → पञ्चमे → षष्ठे → सप्तमे; सातवें पर यह इकाई रुक जाती है। (मेरी याद-पद्धति)",
    },
    "13": {
        "contrast": "स्त्रियों का मत: गर्भ के केशों की उत्पत्ति से माता को विदाह ↔ भगवान् आत्रेय: नेति (ऐसा नहीं)।",
        "chunks": "तस्मिंश्च | गर्भस्यकेशोत्पत्त्या | मातुर्विदाहो भवतीति | स्त्रियो भाषंते | नेति | भगवान्आत्रेयः",
        "sandhi": "न् + च → ंश्च: तस्मिन् + च → तस्मिंश्च · उः + घोष → उर्: मातुः + विदाहः → मातुर्विदाहः · अ + इ → ए: न + इति → नेति।",
        "frame": "मत (इति तक): केशोत्पत्त्या मातुर्विदाहो भवति → कहने वाले: स्त्रियः भाषन्ते → उत्तर: न इति → किसका: भगवान् आत्रेयः।",
    },
}

# ===================================================================== IMAGE_SPECS
IMAGE_SPECS = {
    ("2", "diagram"): {
        "file": "sh3-prathama-masa-kshira-2.svg",
        "alt": ("Table of unit 2 in line order: in the first month the pregnant woman drinks milk that is prepared, "
                "in measure, cool, at the (due) time."),
        "type": "table",
        "title": "प्रथमे मासि: दूध (इकाई २)",
        "heads": ["शब्द", "अर्थ"],
        "rows": [["क्षीरम्", "दूध"], ["उपसंस्कृतम्", "संस्कार किया हुआ"], ["मात्रावत्", "मात्रा के अनुसार"],
                 ["शीतम्", "ठण्डा"], ["काले", "समय पर"]],
    },
    ("3", "chain"): {
        "file": "sh3-dvadasha-ratra-sarpi-3.svg",
        "alt": ("Flowchart of unit 3: in the first month, for the first twelve nights, ghee arising from milk, boiled with "
                "śāliparṇī (standard identification) and palāśa (probable), is drunk; after-drink: cool water with gold and "
                "silver (the word for its preparation is doubtful)."),
        "type": "mermaid",
        "code": ("flowchart TD\n"
                 "  A[\"पहली बारह रातें\"] --> B[\"दूध से उत्पन्न घी\"]\n"
                 "  S[\"शालिपर्णी (मानक)\"] --> C[\"साथ उबाला घी\"]\n"
                 "  P[\"पलाश (सम्भावित)\"] --> C\n"
                 "  B --> C\n"
                 "  C --> D[\"पिए\"]\n"
                 "  D --> E[\"अनुपान: ठण्डा जल\"]\n"
                 "  E -.- F[\"सोना-चाँदी से तैयार (तैयारी का शब्द संदिग्ध)\"]\n"),
    },
    ("4", "diagram"): {
        "file": "sh3-saayam-praatah-4.svg",
        "alt": ("Two columns of unit 4: the food, in line order: (sweet, a doubtful reading) and cool, mostly liquid, "
                "suitable; the times: evening and morning."),
        "type": "split",
        "title": "इकाई ४: आहार और समय",
        "cols": [["आहार कैसा (क्रम से)", ["१ खादुशीत (खादु संदिग्ध)", "२ द्रवप्राय (अधिकतर तरल)", "३ सात्म्य (अनुकूल)"]],
                 ["कब", ["सायं", "प्रातः"]]],
    },
    ("8", "diagram"): {
        "file": "sh3-tritiya-sarpi-madhu-8.svg",
        "alt": ("Flowchart of unit 8: in the third (month), the same milk, with ghee and with honey."),
        "type": "mermaid",
        "code": ("flowchart TD\n"
                 "  A[\"तृतीये (तीसरे में)\"] --> B[\"तदेव (वही दूध)\"]\n"
                 "  B --> C[\"सर्पि (घी) के साथ\"]\n"
                 "  B --> D[\"मधु के साथ\"]\n"),
    },
    ("9", "chain"): {
        "file": "sh3-chaturtha-navanita-9.svg",
        "alt": ("Chain of unit 9 in word order: in the fourth (month); in the measure of an akṣa; fresh butter; joined with."),
        "type": "chain",
        "title": "इकाई ९: चतुर्थे",
        "steps": ["चतुर्थे (चौथे में)", "अक्ष-मात्र", "नवनीत (मक्खन)", "युक्त (मिला हुआ)"],
    },
    ("13", "contrast"): {
        "file": "sh3-vidaha-atreya-13.svg",
        "alt": ("Flowchart of unit 13: the women's view: the arising of the embryo's hair causes burning in the mother; "
                "the venerable Ātreya answers: not so."),
        "type": "mermaid",
        "code": ("flowchart TD\n"
                 "  A[\"स्त्रियों का मत\"] --> B[\"गर्भ के केशों की उत्पत्ति\"]\n"
                 "  B --> C[\"माता को विदाह (जलन)\"]\n"
                 "  C -.->|\"इस मत पर\"| D[\"भगवान् आत्रेय: नेति\"]\n"
                 "  D --> E[\"ऐसा नहीं\"]\n"),
    },
}
