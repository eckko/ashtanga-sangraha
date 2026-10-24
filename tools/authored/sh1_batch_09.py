from helpers import mcq, match, order, fill, multi, accepts


def T(q, teaches):
    q["teaches"] = teaches
    return q


AUTHORED = {}

# ---------------------------------------------------------------- unit 107
AUTHORED["107"] = {
    "title": "तत्रात्याशिता क्षुधिता",
    "question": "By unit 107, in which states does a woman not conceive, or conceive a defective foetus?",
    "rule": ("A woman who is over-fed, hungry, thirsty, frightened, dejected, grief-stricken, angry, very fat (probable sense), desiring "
             "another, or desiring no intercourse does not bear a foetus (garbha), or bears a defective (विगुण) one."),
    "limits": ("Prose, one printed line. अतिमेदुरा = very fat or very unctuous is a probable reading only, so no question "
               "rests on it. The printed वान is read वा न, and गर्भ possibly stands for गर्भम्. The text gives no reason "
               "for each state and no advice beyond the list."),
    "explain_hi": ("यह इकाई एक लम्बी सूची है: ऐसी स्त्री जो बहुत अधिक खा चुकी हो, भूखी, प्यासी, डरी हुई, उदास मन वाली, "
                   "शोक से पीड़ित, क्रोधित, अत्यन्त स्थूल (सम्भावित अर्थ), किसी दूसरे को चाहने वाली, या सहवास न चाहने वाली हो। "
                   "ऐसी स्त्री के दो परिणाम कहे गए हैं: वह गर्भ धारण नहीं करती, या विगुण (दोषयुक्त) गर्भ धारण करती है। "
                   "सारे विशेषण स्त्रीलिंग प्रथमा एकवचन हैं; क्रिया ‘धत्ते’ (धारण करती है) अन्त में है। "
                   "‘अत्याशिता’ में अति + आशिता है (इ + आ → या)।"),
    "hook": "दस अवस्थाएँ, दो परिणाम: न गर्भ धत्ते, विगुणं वा।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 107, what happens to a woman who is hungry, frightened or angry?",
            ("No foetus, or a defective foetus", "वा न गर्भ(ं) धत्ते विगुणं वा: the two stated outcomes (printed वान गर्भ)."),
            [("A foetus, but always a girl", "No child's sex is named in this unit."),
             ("Twins, or a child of short life", "Neither twins nor length of life is named here."),
             ("No monthly flow for a year", "The unit says nothing of the monthly flow.")],
            "The list ends with two outcomes: no foetus is borne, or a defective one.",
            "न गर्भं धत्ते विगुणं वा = does not bear a foetus, or bears a defective one."),
        match(1, "Match each word of unit 107 to its meaning.",
              [["क्षुधिता", "hungry"], ["पिपासिता", "thirsty"], ["भीता", "frightened"],
               ["शोकार्ता", "afflicted by grief"], ["अव्यवायकामा", "desiring no intercourse"]],
              "All are feminine nominative singulars describing the woman.",
              "क्षुधिता, पिपासिता, भीता, शोकार्ता, अव्यवायकामा."),
        T(order(2, "Put these states of the woman in unit 107 in the text's order.",
                ["अत्याशिता", "पिपासिता", "विमनाः", "क्रुद्धा", "अन्यकामा"],
                "Over-fed comes first, then thirsty, dejected, angry, and desiring another near the end.",
                "अत्याशिता → पिपासिता → विमनाः → क्रुद्धा → अन्यकामा.", role="extend"),
          "Unit 107 lists the states first and puts the verb धत्ते near the end with its two outcomes."),
        mcq("discriminate", 3, "Which split of अत्याशिता is right?",
            ("अति + आशिता", "इ + आ → या: अति + आशिता = अत्याशिता."),
            [("अत्य + आशिता", "अत्य is not a word; the prefix is अति."),
             ("अत्या + शिता", "शिता is not a word of the card."),
             ("अति + अशिता", "इ + short अ would give अत्यशिता, with a short अ.")],
            "अति (over) + आशिता (fed): इ before आ becomes य्.",
            "इ + आ → या."),
        multi("apply", 4, "Which statements about unit 107 are right?",
              [("Grief and anger are among the listed states", "Right: शोकार्ता and क्रुद्धा."),
               ("A defective foetus is one stated outcome", "Right: विगुणं वा."),
               ("A remedy for each state is given", "No remedy is given in this unit."),
               ("The states are said of the man", "The adjectives are feminine: the woman is meant.")],
              [0, 1],
              "The unit lists the woman's states and two outcomes; it gives no remedy.",
              "Feminine list + धत्ते: no foetus, or a defective one."),
        mcq("transfer", 5, "By the rule of अत्याशिता, how is अति + आदरः (excessive respect) written when joined?",
            ("अत्यादरः", "इ + आ → या, as in अति + आशिता."),
            [("अतिआदरः", "The two vowels are joined, not left side by side."),
             ("अत्यदरः", "The long आ of आदरः cannot turn short."),
             ("अतेदरः", "इ + आ does not give ए.")],
            "अति + आदरः = अत्यादरः, like अति + आशिता = अत्याशिता.",
            "इ + आ → या.",
            teaches="A final इ before a different vowel becomes य् and the vowel follows: अति + आ → अत्या."),
    ],
}

# ---------------------------------------------------------------- unit 108
AUTHORED["108"] = {
    "title": "तथा पुरुषोऽपि",
    "question": "By unit 108, what should the man not do, and what child does the text say results?",
    "rule": ("Line 2 is plain: for thus a male is born with a woman's behaviour (स्त्रीचेष्टः), or a female with a man's "
             "behaviour (पुंचेष्टा). Line 1 says the man should not stay below (अधः)."),
    "limits": ("Low confidence; two printed lines. The first clause has no verb; that the man too should avoid the states "
               "of unit 107 is conjecture, and no question rests on it. अधः = under the woman is probable. Line 2 gives "
               "the result (तथा हि)."),
    "explain_hi": ("पहली पंक्ति: ‘तथा पुरुषोऽपि’ (इसी प्रकार पुरुष भी) में क्रिया नहीं है; इसका आशय कि पुरुष भी इकाई 107 की "
                   "अवस्थाओं में न हो, केवल अनुमान है। फिर: ‘न चासावधस्तिष्ठेत्’ = और वह नीचे न रहे (सम्भवतः स्त्री के नीचे)। "
                   "दूसरी पंक्ति कारण देती है: ‘तथा हि’ (क्योंकि इस प्रकार) स्त्री की चेष्टा वाला पुरुष या पुरुष की चेष्टा वाली "
                   "स्त्री उत्पन्न होती है। ‘असौ’ पुंलिंग प्रथमा एकवचन है (वह), द्विवचन नहीं।"),
    "hook": "पुरुष नीचे न रहे: नहीं तो स्त्रीचेष्ट पुमान् या पुंचेष्टा स्त्री।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By line 2 of unit 108, what kind of child is born?",
            ("A male who behaves like a woman, or a female like a man", "स्त्रीचेष्टः पुमान् ... पुंचेष्टा वा स्त्री."),
            [("A male who behaves like a man, or a female like a woman", "That reverses the text: the behaviour is crossed."),
             ("A weak male, or a female with defective senses", "Weakness and senses are not named here."),
             ("No child at all, or one of very short life", "Line 2 says a child is born (जायते).")],
            "Line 2: a male with a woman's behaviour, or a female with a man's behaviour.",
            "स्त्रीचेष्टः पुमान्, पुंचेष्टा स्त्री."),
        match(1, "Match each word of unit 108 to its meaning.",
              [["अधः", "below"], ["तिष्ठेत्", "should stay"], ["स्त्रीचेष्टः", "with a woman's behaviour"],
               ["पुंचेष्टा", "with a man's behaviour"], ["जायते", "is born"]],
              "Two of these come from line 1, three from line 2.",
              "अधः, तिष्ठेत्, स्त्रीचेष्टः, पुंचेष्टा, जायते."),
        T(order(2, "Put the words of line 2 of unit 108 in the line's order.",
                ["तथा हि", "स्त्रीचेष्टः", "पुमान्", "जायते", "पुंचेष्टा वा स्त्री"],
                "For thus, with a woman's behaviour, a male, is born, or a female with a man's behaviour.",
                "तथा हि → स्त्रीचेष्टः → पुमान् → जायते → पुंचेष्टा वा स्त्री.", role="extend"),
          "तथा हि (for thus) gives the reason for the rule just before it."),
        mcq("discriminate", 3, "Which split of पुरुषोऽपि is right?",
            ("पुरुषः + अपि", "अः + अ → ओ, and the अ of अपि is dropped, marked ऽ."),
            [("पुरुष + उपि", "उपि is not a word of the card."),
             ("पुरुषौ + अपि", "A dual पुरुषौ would join as पुरुषावपि."),
             ("पुरुषः + पि", "पि is not a word; the dropped अ is marked by ऽ.")],
            "पुरुषः (man) + अपि (also): अः before अ becomes ओ and the अ is dropped.",
            "अः + अ → ओ + ऽ."),
        mcq("apply", 4, "What does the card give for असौ in न चासावधस्तिष्ठेत्?",
            ("Masculine nominative singular: that one", "The card labels असौ m. nom. sg., that (one)."),
            [("Masculine nominative dual: those two", "-औ here is not a dual ending; असौ is singular."),
             ("Feminine accusative singular: her", "Her would be ताम् or एनाम्."),
             ("Locative singular: in that place", "The card gives no locative here.")],
            "असौ = that one, the man, singular; its -औ is not a dual sign.",
            "असौ = m. nom. sg."),
        mcq("transfer", 5, "By the rule of अधस्तिष्ठेत् (अधः + तिष्ठेत्), how is वातः + तिष्ठति written when joined?",
            ("वातस्तिष्ठति", "Visarga before त becomes स्, as अधः + तिष्ठेत्."),
            [("वातोतिष्ठति", "ओ comes before a voiced sound; त is not voiced."),
             ("वातश्तिष्ठति", "श् comes before च, छ or श, not before त."),
             ("वाततिष्ठति", "The visarga is not simply dropped before त.")],
            "वातः + तिष्ठति = वातस्तिष्ठति, like अधः + तिष्ठेत् = अधस्तिष्ठेत्.",
            "Visarga + त → स्त.",
            teaches="A visarga before त or थ becomes स्: अधः + तिष्ठेत् → अधस्तिष्ठेत्."),
    ],
}

# ---------------------------------------------------------------- unit 109
AUTHORED["109"] = {
    "title": "न च न्युब्जां पार्श्वगतां वा",
    "question": "By unit 109, in which two positions should the woman not be approached?",
    "rule": ("न च न्युब्जां पार्श्वगतां वा सेवेत: and one should not resort to (have union with) a woman lying face down "
             "or lying on her side. सेवेत is an optative: should (not) resort to."),
    "limits": ("The subject is not stated; the man is probably meant. Units 110 to 112 go on to say what happens in each position "
               "(read here as the reasons); this unit gives none."),
    "explain_hi": ("यह इकाई दो स्थितियाँ मना करती है: ‘न्युब्जा’ (औंधी, पेट के बल लेटी) और ‘पार्श्वगता’ (करवट पर लेटी)। "
                   "दोनों स्त्रीलिंग द्वितीया एकवचन हैं, क्योंकि स्त्री ‘सेवेत’ (सेवन करे) का कर्म है। "
                   "‘सेवेत’ विधिलिङ् आत्मनेपद है; ‘न’ के साथ अर्थ है ‘सेवन न करे’। कर्ता नहीं छपा; सम्भवतः पुरुष। "
                   "कारण अगली तीन इकाइयों में दिए गए हैं।"),
    "hook": "न औंधी, न करवट: न्युब्जां पार्श्वगतां वा न सेवेत।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 109, in which positions should the woman not be approached?",
            ("Lying face down, or lying on her side", "न्युब्जाम् and पार्श्वगताम् are both forbidden."),
            [("Lying on her back, or seated upright", "Lying on the back is advised in unit 113."),
             ("Standing, or lying face down only", "Standing is not named in this unit."),
             ("Lying on her side, or on her back", "Lying on the back is not forbidden here.")],
            "Face down (न्युब्जा) and on the side (पार्श्वगता) are the two positions named.",
            "न न्युब्जां पार्श्वगतां वा सेवेत."),
        match(1, "Match each word of unit 109 to its meaning.",
              [["न्युब्जाम्", "lying face down"], ["पार्श्वगताम्", "lying on the side"],
               ["सेवेत", "should resort to"], ["वा", "or"], ["न", "not"]],
              "Two positions, joined by वा, are the object of सेवेत, negated by न.",
              "न्युब्जाम्, पार्श्वगताम्, सेवेत, वा, न."),
        T(order(2, "Put the words of unit 109 in the line's order.",
                ["न च", "न्युब्जाम्", "पार्श्वगताम्", "वा", "सेवेत"],
                "And not, face down, on the side, or, should resort to.",
                "न च → न्युब्जाम् → पार्श्वगताम् → वा → सेवेत.", role="extend"),
          "The verb सेवेत comes last; the negation न च stands at the head of the line."),
        mcq("discriminate", 3, "What form does the card give सेवेत?",
            ("Third singular optative: should resort to", "The card labels it 3 sg. opt. ātm."),
            [("Third singular present: resorts to", "The present would be सेवते."),
             ("First singular present: I resort to", "That would be सेवे."),
             ("Third plural optative: they should resort", "That would be सेवेरन्.")],
            "सेवेत = he should resort to: an optative of rule, here negated by न.",
            "सेवेत = 3 sg. opt. ātm."),
        mcq("apply", 4, "Why are न्युब्जाम् and पार्श्वगताम् in the accusative?",
            ("They describe the woman, the object of सेवेत", "The card gives both as f. acc. sg., the object."),
            [("They describe the man, the subject of सेवेत", "A subject would be nominative, not accusative."),
             ("They name the place where union happens", "A place would be in the locative."),
             ("They give the reason why it is forbidden", "They name positions; the reasons come in units 110 to 112.")],
            "The woman is the object of सेवेत, so her descriptions are feminine accusatives.",
            "Object of the verb → accusative: न्युब्जाम्, पार्श्वगताम्."),
        mcq("transfer", 5, "Built like न्युब्जाम्, which form says a woman lying on her back as the object of सेवेत?",
            ("उत्तानाम्", "Feminine -आ stem, accusative singular -आम्, like न्युब्जाम्."),
            [("उत्ताना", "That is the nominative, used for a subject."),
             ("उत्तानायाम्", "That is the locative, in her."),
             ("उत्तानायाः", "That is the genitive or ablative.")],
            "उत्ताना → उत्तानाम्, as न्युब्जा → न्युब्जाम्.",
            "Feminine -आ stem, acc. sg.: -आम्.",
            teaches="A feminine -आ stem makes its accusative singular in -आम्: न्युब्जा → न्युब्जाम्."),
    ],
}

# ---------------------------------------------------------------- unit 110
AUTHORED["110"] = {
    "title": "न्युब्जायां वातो बलवान्",
    "question": "By unit 110, what happens in a woman lying face down?",
    "rule": ("In one lying face down Vāta is strong; it presses (afflicts) the yoni. This is the reason for the first "
             "forbidden position of unit 109."),
    "limits": ("Vāta is one of the three doṣas and is kept without a modern equivalent. yoni = the female genital passage "
               "or womb is a probable sense. The unit gives no remedy."),
    "explain_hi": ("इकाई 109 की पहली वर्जित स्थिति का कारण: औंधी लेटी स्त्री में वात बलवान होता है, और वह योनि को पीड़ित करता है। "
                   "‘न्युब्जायाम्’ सप्तमी है (औंधी लेटी में), जबकि इकाई 109 में ‘न्युब्जाम्’ द्वितीया थी। "
                   "पहले वाक्य में ‘है’ क्रिया समझी जाती है। ‘स’ (वह) वात की ओर संकेत करता है। "
                   "वात तीन दोषों में से एक है; उसका आधुनिक नाम नहीं दिया गया।"),
    "hook": "औंधी → वात बलवान् → योनि-पीडा।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 110, which doṣa is strong in a woman lying face down?",
            ("Vāta", "न्युब्जायां वातो बलवान्."),
            [("Pitta", "Pitta is named for the left side in unit 112."),
             ("Kapha", "Kapha (श्लेष्मा) is named for the right side in unit 111."),
             ("No doṣa at all", "The unit names Vāta as strong.")],
            "Face down: Vāta is strong and presses the yoni.",
            "न्युब्जा → वात."),
        match(1, "Match each word of unit 110 to its meaning.",
              [["न्युब्जायाम्", "in one lying face down"], ["वातः", "Vāta"], ["बलवान्", "strong"],
               ["योनिम्", "the yoni"], ["पीडयति", "presses, afflicts"]],
              "Position, doṣa, its strength, its target and its action.",
              "न्युब्जायाम्, वातः, बलवान्, योनिम्, पीडयति."),
        T(order(2, "Put the words of unit 110 in the line's order.",
                ["न्युब्जायाम्", "वातः", "बलवान्", "सः", "योनिम्", "पीडयति"],
                "In one face down, Vāta, strong; it, the yoni, presses.",
                "न्युब्जायाम् → वातः → बलवान् → सः → योनिम् → पीडयति.", role="extend"),
          "The unit is a small chain: position, then the doṣa made strong, then what it does."),
        mcq("discriminate", 3, "Which split explains वातो बलवान्?",
            ("वातः + बलवान्", "अः before a voiced consonant (ब) becomes ओ."),
            [("वातौ + बलवान्", "A dual वातौ would stay वातौ; the card gives वातः, singular."),
             ("वातम् + बलवान्", "An accusative would be written वातं before ब."),
             ("वात + ओबलवान्", "ओबलवान् is not a word.")],
            "वातः (Vāta) + बलवान् (strong): अः → ओ before the voiced ब.",
            "अः + voiced consonant → ओ."),
        mcq("apply", 4, "How does न्युब्जायाम् of unit 110 differ from न्युब्जाम् of unit 109?",
            ("It is locative, in her; न्युब्जाम् is accusative", "The card gives न्युब्जायाम् as f. loc. sg."),
            [("It is plural, while न्युब्जाम् is singular", "Both are singular."),
             ("It is masculine, while न्युब्जाम् is feminine", "Both are feminine."),
             ("It is a verb, while न्युब्जाम् is a noun", "Neither is a verb.")],
            "Unit 109: the woman as object (-आम्); unit 110: in her (-आयाम्), where Vāta grows strong.",
            "न्युब्जाम् = acc.; न्युब्जायाम् = loc."),
        mcq("transfer", 5, "By the rule of वातो बलवान्, how is रोगः + बलवान् written when joined?",
            ("रोगो बलवान्", "अः before a voiced consonant becomes ओ, as in वातो बलवान्."),
            [("रोगर्बलवान्", "र् comes after vowels other than अ/आ, not after अः."),
             ("रोगस्बलवान्", "स् comes only before त or थ."),
             ("रोगा बलवान्", "The अ does not lengthen; अः gives ओ.")],
            "रोगः + बलवान् = रोगो बलवान्, like वातः + बलवान् = वातो बलवान्.",
            "अः + voiced consonant → ओ.",
            teaches="After अ, a visarga before a voiced consonant joins as ओ: वातः + बलवान् → वातो बलवान्."),
    ],
}

# ---------------------------------------------------------------- unit 111
AUTHORED["111"] = {
    "title": "दक्षिणपार्श्वगायाः श्लेष्मा",
    "question": "By unit 111, what does Kapha do in a woman lying on her right side?",
    "rule": ("In one lying on the right side, Kapha (श्लेष्मा), pressed and displaced, closes the womb (गर्भाशय)."),
    "limits": ("अपिदधाति can mean covers or closes up; the data uses closes. श्लेष्मा = Kapha and गर्भाशय = womb are "
               "standard. The unit gives no remedy and nothing on the left side."),
    "explain_hi": ("इकाई 109 की दूसरी वर्जित स्थिति (करवट) का एक पक्ष: दाहिनी करवट पर लेटी स्त्री का श्लेष्मा, यानी कफ, "
                   "दबकर (पीडितः) और अपने स्थान से हटकर (च्युतः) गर्भाशय को बन्द कर देता है (अपिदधाति)। "
                   "‘दक्षिणपार्श्वगायाः’ षष्ठी एकवचन है: दाहिनी करवट वाली का। "
                   "‘पीडितश्च्युतो’ में दो सन्धियाँ हैं: विसर्ग च से पहले श् बनता है, और अः + अ → ओ (अ का लोप, ऽ)।"),
    "hook": "दाहिनी करवट → कफ दबकर हटे → गर्भाशय बन्द।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 111, what does Kapha do in a woman lying on her right side?",
            ("Pressed and displaced, it closes the womb", "श्लेष्मा पीडितश्च्युतोऽपिदधाति गर्भाशयम्."),
            [("Grown strong, it presses the yoni", "That is Vāta in one lying face down, unit 110."),
             ("Grown dry, it shrinks the womb", "Dryness and shrinking are not named here."),
             ("Displaced, it pushes the foetus left", "The unit says nothing of moving a foetus.")],
            "Right side: Kapha, pressed and displaced, closes the womb.",
            "दक्षिणपार्श्व → श्लेष्मा → गर्भाशय बन्द."),
        match(1, "Match each word of unit 111 to its meaning.",
              [["दक्षिणपार्श्वगायाः", "of one lying on the right side"], ["श्लेष्मा", "Kapha"],
               ["पीडितः", "pressed"], ["च्युतः", "displaced"], ["गर्भाशयम्", "the womb"]],
              "Position, doṣa, two states of the doṣa and the organ affected.",
              "दक्षिणपार्श्वगायाः, श्लेष्मा, पीडितः, च्युतः, गर्भाशयम्."),
        T(order(2, "Put the words of unit 111 in the line's order.",
                ["दक्षिणपार्श्वगायाः", "श्लेष्मा", "पीडितः", "च्युतः", "अपिदधाति", "गर्भाशयम्"],
                "Of one on the right side, Kapha, pressed, displaced, closes, the womb.",
                "दक्षिणपार्श्वगायाः → श्लेष्मा → पीडितः → च्युतः → अपिदधाति → गर्भाशयम्.", role="extend"),
          "Two participles (पीडितः, च्युतः) describe Kapha before its verb अपिदधाति."),
        mcq("discriminate", 3, "Which split of पीडितश्च्युतो is right?",
            ("पीडितः + च्युतः", "Visarga before च becomes श्; च्युतः then becomes ओ before अ."),
            [("पीडितम् + च्युतः", "An -म् ending would be written पीडितं, not पीडितश्."),
             ("पीडित + श्च्युतः", "श्च्युतः is not a word."),
             ("पीडितौ + च्युतः", "A dual पीडितौ would not turn into पीडितश्.")],
            "पीडितः (pressed) + च्युतः (displaced): visarga → श् before च.",
            "Visarga + च → श्च."),
        mcq("apply", 4, "In the print च्युतो ऽपिदधाति, what does the sign ऽ mark?",
            ("The अ of अपिदधाति, dropped after ओ", "च्युतः + अपिदधाति: अः + अ → ओ, and the अ drops (ऽ)."),
            [("A pause at the end of the sentence", "The sentence end is not marked by ऽ."),
             ("A long vowel in the following word", "ऽ does not lengthen a vowel."),
             ("A missing visarga on अपिदधाति", "A verb ending -ति has no visarga to lose.")],
            "ऽ (avagraha) shows where an initial अ was dropped after ओ.",
            "अः + अ → ओ ऽ."),
        mcq("transfer", 5, "By the rule of पीडितश्च्युतः, how is वातः + च written when joined?",
            ("वातश्च", "Visarga before च becomes श्, as in पीडितः + च्युतः."),
            [("वातो च", "ओ comes before a voiced sound; च is not voiced."),
             ("वातस्च", "स् comes before त or थ, not before च."),
             ("वातच", "The visarga is not simply dropped before च.")],
            "वातः + च = वातश्च, like पीडितः + च्युतः = पीडितश्च्युतः.",
            "Visarga + च → श्च.",
            teaches="A visarga before च or छ becomes श्: पीडितः + च्युतः → पीडितश्च्युतः."),
    ],
}

# ---------------------------------------------------------------- unit 112
AUTHORED["112"] = {
    "title": "वामपार्श्वगायास्तद्वत्पित्तम्",
    "question": "By unit 112, which doṣa acts in a woman lying on her left side, and how is it linked to units 110 and 111?",
    "rule": ("In one lying on the left side, similarly (तद्वत्), Pitta burns (विदहति). तद्वत् ties it to the Vāta and Kapha "
             "of units 110 and 111."),
    "limits": ("The object is printed रक्तशुके, not a word; रक्तशुक्रे (blood and semen) is a possible correction, so no question "
               "rests on what Pitta burns. Pitta is a doṣa, kept without a modern equivalent."),
    "explain_hi": ("बायीं करवट पर लेटी स्त्री में ‘तद्वत्’, यानी पिछली दो इकाइयों की तरह, पित्त ‘विदहति’ (जलाता है)। "
                   "छपा ‘रक्तशुके’ कोई शब्द नहीं है; ‘रक्तशुक्रे’ (रक्त और शुक्र, द्विवचन) सम्भावित सुधार है, इसलिए वस्तु पर प्रश्न नहीं। "
                   "इस तरह तीन स्थितियाँ और तीन दोष: औंधी में वात, दाहिनी करवट में कफ, बायीं करवट में पित्त। "
                   "‘वामपार्श्वगायाः’ षष्ठी एकवचन है; विसर्ग त से पहले स् बनता है।"),
    "hook": "औंधी-वात, दाहिनी-कफ, बायीं-पित्त।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 112, which doṣa acts in a woman lying on her left side?",
            ("Pitta", "वामपार्श्वगायास्तद्वत्पित्तम्."),
            [("Vāta", "Vāta is named for lying face down, unit 110."),
             ("Kapha", "Kapha is named for the right side, unit 111."),
             ("None; the left side is advised", "The position advised is lying on the back, unit 113.")],
            "Left side: Pitta, acting similarly to the doṣas of units 110 and 111.",
            "वामपार्श्व → पित्त."),
        order(1, "Put these words of unit 112 in the line's order.",
              ["वामपार्श्वगायाः", "तद्वत्", "पित्तम्", "विदहति"],
              "Of one on the left side, similarly, Pitta, burns; the doubtful object रक्तशुके follows and is left out.",
              "वामपार्श्वगायाः → तद्वत् → पित्तम् → विदहति."),
        mcq("extend", 2, "What does तद्वत् tell the reader in unit 112?",
            ("Pitta acts like the doṣas of units 110 and 111", "The data takes तद्वत् as similarly to units 110 and 111."),
            [("Pitta acts unlike the doṣas of units 110 and 111", "तद्वत् means similarly, not unlike."),
             ("Pitta comes only after twelve nights have passed", "No time is named in this unit."),
             ("Pitta is to be removed by the same remedy", "No remedy is named in this unit.")],
            "तद्वत् = similarly: one more position, one more doṣa, in the same pattern.",
            "तद्वत् = in that way, similarly.",
            teaches="तद्वत् (in that way) carries the pattern of the previous units onto a new case."),
        mcq("discriminate", 3, "Which split of वामपार्श्वगायास्तद्वत् is right?",
            ("वामपार्श्वगायाः + तद्वत्", "Visarga before त becomes स्."),
            [("वामपार्श्वगायाम् + तद्वत्", "A locative -आम् would be written -आं before त."),
             ("वामपार्श्वगाया + स्तद्वत्", "स्तद्वत् is not a word."),
             ("वामपार्श्वगायै + तद्वत्", "A dative -ऐ would stay -ऐ, not turn into -आस्.")],
            "वामपार्श्वगायाः (of one on the left side) + तद्वत् (similarly): visarga → स् before त.",
            "Visarga + त → स्त."),
        match(4, "Match each position of units 110 to 112 to the doṣa named for it.",
              [["न्युब्जा (face down)", "वात"], ["दक्षिणपार्श्वगा (right side)", "श्लेष्मा (कफ)"],
               ["वामपार्श्वगा (left side)", "पित्त"]],
              "Three positions, three doṣas: face down Vāta, right side Kapha, left side Pitta.",
              "न्युब्जा-वात, दक्षिण-कफ, वाम-पित्त.", role="apply"),
        mcq("transfer", 5, "Built like वामपार्श्वगायाः, which form of पार्श्वगता means of one lying on the side?",
            ("पार्श्वगतायाः", "Feminine -आ stem, genitive singular -आयाः, like वामपार्श्वगायाः."),
            [("पार्श्वगताम्", "That is the accusative, as in unit 109."),
             ("पार्श्वगतया", "That is the instrumental, by her."),
             ("पार्श्वगतायाम्", "That is the locative, in her.")],
            "पार्श्वगता → पार्श्वगतायाः, as वामपार्श्वगा → वामपार्श्वगायाः.",
            "Feminine -आ stem, gen. sg.: -आयाः.",
            teaches="A feminine -आ stem makes its genitive singular in -आयाः: वामपार्श्वगा → वामपार्श्वगायाः."),
    ],
}

# ---------------------------------------------------------------- unit 113
AUTHORED["113"] = {
    "title": "उत्ताना बीजं गृह्णीयात्",
    "question": "By unit 113, in what position should the woman receive the seed?",
    "rule": ("Lying on her back (उत्ताना), she should receive the seed (बीज, probably semen). The woman is the subject: "
             "उत्ताना is feminine nominative."),
    "limits": ("The printed दस्मात् is not a word; तस्मात् (therefore) is the likely reading, so no question rests on it. "
               "बीज = semen is probable. The unit gives no further reason for the position."),
    "explain_hi": ("तीन वर्जित स्थितियों (औंधी, दाहिनी करवट, बायीं करवट) के बाद यह इकाई उचित स्थिति कहती है: "
                   "‘उत्ताना’ यानी चित (पीठ के बल) लेटी स्त्री ‘बीज’ (सम्भवतः शुक्र) को ‘गृह्णीयात्’ (ग्रहण करे)। "
                   "छपा ‘दस्मात्’ शब्द नहीं; ‘तस्मात्’ (इसलिए) सम्भावित पाठ है (त/द की भूल)। "
                   "‘गृह्णीयात्’ विधिलिङ् है; ‘बीजंगृह्णीयात्’ = बीजम् + गृह्णीयात् (म् → ं व्यंजन से पहले)।"),
    "hook": "न औंधी, न करवट: उत्ताना बीजं गृह्णीयात्।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 113, in what position should the woman receive the seed?",
            ("Lying on her back", "उत्ताना = lying on the back, supine."),
            [("Lying face down", "Face down is forbidden in unit 109."),
             ("On her right side", "The right side is linked to Kapha, unit 111."),
             ("On her left side", "The left side is linked to Pitta, unit 112.")],
            "Lying on her back (उत्ताना) she should receive the seed.",
            "उत्ताना बीजं गृह्णीयात्."),
        match(1, "Match each word of unit 113 to its meaning.",
              [["उत्ताना", "lying on the back"], ["बीजम्", "seed"], ["गृह्णीयात्", "should receive"]],
              "The doubtful first word दस्मात् is left out.",
              "उत्ताना, बीजम्, गृह्णीयात्."),
        fill(2, "Lying on her back, she should receive the seed: ____ बीजं गृह्णीयात् (type it in Devanagari or in English letters, e.g. dharma).",
             accepts("उत्ताना", None, "uttana"),
             "उत्ताना = lying on her back, feminine nominative: the woman is the subject.",
             "उत्ताना (supine) is the advised position, after three forbidden ones.",
             "उत्ताना = lying on the back."),
        mcq("discriminate", 3, "Which split of the printed बीजंगृह्णीयात् is right?",
            ("बीजम् + गृह्णीयात्", "म् before a consonant is written as anusvāra (ं)."),
            [("बीजः + गृह्णीयात्", "A visarga form would join as बीजो, not बीजं."),
             ("बीज + अंगृह्णीयात्", "अंगृह्णीयात् is not a word."),
             ("बीजन् + गृह्णीयात्", "The card gives बीजम्, n. acc. sg., not बीजन्.")],
            "बीजम् (seed) + गृह्णीयात् (should receive): final म् → ं before ग.",
            "म् + consonant → ं."),
        multi("apply", 4, "Which statements about unit 113 are right?",
              [("The woman is the subject of गृह्णीयात्", "Right: उत्ताना is feminine nominative."),
               ("गृह्णीयात् is an optative: should receive", "Right: the card labels it 3 sg. opt."),
               ("The man is told to lie on his back", "उत्ताना is feminine: the woman lies on her back."),
               ("The seed is said to be blood", "बीज is glossed seed, probably semen, not blood.")],
              [0, 1],
              "The woman, lying on her back, should receive the seed.",
              "उत्ताना (f. nom.) + गृह्णीयात् (opt.)."),
        mcq("transfer", 5, "By the rule of बीजं गृह्णीयात्, how is फलम् + खादेत् (should eat the fruit) written when joined?",
            ("फलं खादेत्", "म् before a consonant becomes anusvāra, as in बीजं गृह्णीयात्."),
            [("फलो खादेत्", "ओ comes from a visarga after अ, not from म्."),
             ("फलः खादेत्", "That changes the word into a visarga form."),
             ("फला खादेत्", "The म् does not become a long आ.")],
            "फलम् + खादेत् = फलं खादेत्, like बीजम् + गृह्णीयात् = बीजं गृह्णीयात्.",
            "म् + consonant → ं.",
            teaches="A final म् before a consonant is written as anusvāra: बीजम् + गृह्णीयात् → बीजं गृह्णीयात्."),
    ],
}

# ---------------------------------------------------------------- unit 114
AUTHORED["114"] = {
    "title": "यथास्थानमेव तिष्ठन्ति दोषाः",
    "question": "By unit 114, where do the doṣas remain?",
    "rule": ("So here the doṣas remain just in their own places (यथास्थानमेव). तिष्ठन्ति is present, third person plural: "
             "they remain."),
    "limits": ("The opening print तथािह is malformed; the data reads तथा + इह, where तथेह would be expected, so no question "
               "rests on it. तथा shows that the line continues an earlier statement; the data does not say which one. "
               "The doṣas are kept without a modern equivalent."),
    "explain_hi": ("यह छोटा वाक्य कहता है: ‘इस प्रकार यहाँ दोष अपने-अपने स्थान पर ही रहते हैं।’ "
                   "‘यथास्थानम्’ का अर्थ है स्थान के अनुसार, यानी हर एक अपने स्थान पर; ‘एव’ = ही। "
                   "‘तिष्ठन्ति’ धातु स्था का वर्तमान, प्रथम पुरुष बहुवचन है (छपा ‘तिष्ठंति’, अनुस्वार = न्)। "
                   "आरम्भ का ‘तथा’ बताता है कि यह किसी पहले कथन से जुड़ा है; डेटा यह नहीं बताता कि किससे। छपा ‘तथािह’ बिगड़ा रूप है।"),
    "hook": "दोष अपनी जगह: यथास्थानमेव तिष्ठन्ति।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 114, where do the doṣas remain?",
            ("In their own places", "यथास्थानमेव तिष्ठन्ति दोषाः."),
            [("Inside the womb only", "The womb is not named in this unit."),
             ("In the blood and semen", "Blood and semen are not named here."),
             ("Out of their own places", "The unit says the opposite: in their own places.")],
            "The doṣas remain just in their own places.",
            "यथास्थानम् एव = just in their own places."),
        match(1, "Match each part of unit 114 to its meaning.",
              [["यथास्थानम्", "each in its own place"], ["एव", "just, only"], ["तिष्ठन्ति", "they remain"],
               ["दोषाः", "the doṣas"]],
              "The doubtful opening तथा(इ)ह is left out.",
              "यथास्थानम्, एव, तिष्ठन्ति, दोषाः."),
        fill(2, "So here the doṣas remain in their own places: यथास्थानमेव ____ दोषाः (type it in Devanagari or in English letters, e.g. dharma).",
             accepts("तिष्ठन्ति", None, "तिष्ठंति"),
             "तिष्ठन्ति = they remain, printed तिष्ठंति with anusvāra.",
             "तिष्ठन्ति is the present third person plural of स्था, agreeing with दोषाः.",
             "तिष्ठन्ति = they remain."),
        mcq("discriminate", 3, "What does यथास्थानम् mean in unit 114?",
            ("Each in its own place", "यथा + स्थानम्: according to place, each in its own."),
            [("All in one shared place", "यथा- here means according to each one's place."),
             ("Away from their places", "No word for away occurs."),
             ("In the place of the foetus", "The foetus is not named in this unit.")],
            "यथास्थानम् = according to place: each doṣa in its own place.",
            "यथा + noun = according to that noun."),
        mcq("apply", 4, "The print reads तिष्ठंति. Which reading does the card give?",
            ("तिष्ठन्ति, with न् for the anusvāra", "Before त the anusvāra is read as the nasal न्."),
            [("तिष्ठति: the anusvāra is a misprint", "The plural subject दोषाः needs the plural तिष्ठन्ति."),
             ("तिष्ठामि: the verb is first person", "No first-person form is given; दोषाः needs the third person."),
             ("तिष्ठेत्: the verb is an optative", "The card labels it present, not optative.")],
            "तिष्ठंति = तिष्ठन्ति, they remain; the anusvāra before त stands for न्.",
            "Anusvāra before त = न्."),
        mcq("transfer", 5, "Invented line: दोषो यथास्थानमेव ____ (the doṣa remains in its place). Which verb fits?",
            ("तिष्ठति", "A singular subject takes the singular तिष्ठति."),
            [("तिष्ठन्ति", "That is plural, for दोषाः."),
             ("तिष्ठतः", "That is dual, for two subjects."),
             ("तिष्ठामि", "That is first person, I remain.")],
            "दोषः (one) + तिष्ठति; दोषाः (many) + तिष्ठन्ति.",
            "Present 3 sg. -ति, 3 pl. -न्ति.",
            teaches="The verb agrees in number with its subject: दोषः तिष्ठति, दोषाः तिष्ठन्ति."),
    ],
}

# ---------------------------------------------------------------- unit 115
AUTHORED["115"] = {
    "title": "लब्धगर्भां चैनां विदित्वा",
    "question": "By unit 115, after knowing what, and in which lunar mansion, should the puṃsavana and the like be employed?",
    "rule": ("Having known that she has conceived (लब्धगर्भाम्), one should employ the puṃsavana (rite for obtaining a male "
             "child) and the like in Puṣya (the lunar mansion Puṣya)."),
    "limits": ("One token is damaged: प्रागव्यक्तीभावादृर्भस्य; before the foetus becomes manifest is a conjectural reading, "
               "so no question rests on it. The subject of प्रयुञ्जीत is not stated. The text names only puṃsavana and the like here; "
               "the steps come later."),
    "explain_hi": ("नया विषय पुंसवन: स्त्री को गर्भवती (लब्धगर्भा) जानकर, पुष्य नक्षत्र में पुंसवन आदि का प्रयोग करे। "
                   "पुंसवन पुत्र-प्राप्ति के लिए किया जाने वाला संस्कार है (मानक)। "
                   "बीच का छपा शब्द ‘प्रागव्यक्तीभावादृर्भस्य’ क्षतिग्रस्त है; ‘गर्भ के प्रकट होने से पहले’ अनुमानित अर्थ है। "
                   "‘विदित्वा’ क्त्वा-प्रत्ययान्त (जानकर) है और ‘प्रयुञ्जीत’ विधिलिङ् (प्रयोग करे); कर्ता नहीं छपा। "
                   "‘चैनाम्’ = च + एनाम् (अ + ए → ऐ)।"),
    "hook": "गर्भ जानकर, पुष्य में पुंसवनादि (प्रयुञ्जीत)।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 115, in which lunar mansion should the puṃsavana be employed?",
            ("Puṣya", "पुष्ये = in Puṣya."),
            [("Rohiṇī", "Rohiṇī is not named in this unit."),
             ("Maghā", "Maghā is not named in this unit."),
             ("Revatī", "Revatī is not named in this unit.")],
            "पुष्ये पुंसवनादि प्रयुञ्जीत: in Puṣya one should employ the puṃsavana and the like.",
            "पुष्ये = in the lunar mansion Puṣya."),
        match(1, "Match each word of unit 115 to its meaning.",
              [["लब्धगर्भाम्", "one who has conceived"], ["एनाम्", "her"], ["विदित्वा", "having known"],
               ["पुष्ये", "in Puṣya"], ["प्रयुञ्जीत", "should employ"]],
              "The damaged middle word is left out.",
              "लब्धगर्भाम्, एनाम्, विदित्वा, पुष्ये, प्रयुञ्जीत."),
        T(order(2, "Put these words of unit 115 in the line's order.",
                ["लब्धगर्भाम्", "विदित्वा", "पुष्ये", "पुंसवनादि", "प्रयुञ्जीत"],
                "Having known her to have conceived, in Puṣya, the puṃsavana and the like, one should employ.",
                "लब्धगर्भाम् → विदित्वा → पुष्ये → पुंसवनादि → प्रयुञ्जीत.", role="extend"),
          "First conception is known, then the rite is done in Puṣya: the absolutive comes before the main verb."),
        mcq("discriminate", 3, "Which split of चैनाम् is right?",
            ("च + एनाम्", "अ + ए → ऐ: च + एनाम् = चैनाम्."),
            [("च + इनाम्", "अ + इ would give ए: चेनाम्."),
             ("चै + नाम्", "चै is not a word of the card."),
             ("च + ऐनाम्", "ऐनाम् is not a word; the pronoun is एनाम्.")],
            "च (and) + एनाम् (her): अ before ए becomes ऐ.",
            "अ + ए → ऐ."),
        mcq("apply", 4, "What form is विदित्वा, and what does it show?",
            ("Absolutive: having known first", "The card labels it abs. √vid; -त्वा = having done."),
            [("Optative: one should know", "The optative of the line is प्रयुञ्जीत."),
             ("Present: one knows now", "A present form would end in -ति."),
             ("Infinitive: in order to know it", "An infinitive would end in -तुम्.")],
            "विदित्वा = having known: the knowing comes before employing the rite.",
            "-त्वा = absolutive, having done."),
        mcq("transfer", 5, "By the rule of चैनाम्, how is च + एव written when joined?",
            ("चैव", "अ + ए → ऐ, as in च + एनाम्."),
            [("चेव", "अ + ए gives ऐ, not ए."),
             ("चाएव", "The two vowels are joined, not left side by side."),
             ("चयेव", "No य् comes between अ and ए.")],
            "च + एव = चैव, like च + एनाम् = चैनाम्.",
            "अ + ए → ऐ.",
            teaches="A or आ before ए or ऐ joins into ऐ: च + एनाम् → चैनाम्."),
    ],
}

# ---------------------------------------------------------------- unit 116
AUTHORED["116"] = {
    "title": "द्वादशरात्रमित्यन्ये",
    "question": "What other opinion on the time of the rite does unit 116 report?",
    "rule": ("द्वादशरात्रम् इति अन्ये: 'a period of twelve nights', so others (hold). An elliptical line: the verb of saying "
             "is understood, not printed."),
    "limits": ("The line does not say from when the twelve nights are counted, nor who the others are. It is read as a further "
               "opinion on the time of the rite of unit 115; no verb is supplied."),
    "explain_hi": ("यह एक संक्षिप्त मत है: ‘बारह रात्रि का काल, ऐसा अन्य लोग (कहते हैं)।’ "
                   "‘कहते हैं’ क्रिया छपी नहीं, समझी जाती है। यह इकाई 115 के पुंसवन के समय पर दूसरा मत माना गया है। "
                   "बारह रातें कब से गिनी जाएँ और ‘अन्ये’ कौन हैं, पाठ नहीं बताता। "
                   "‘इत्यन्ये’ = इति + अन्ये (इ + अ → य)।"),
    "hook": "अन्ये: बारह रातें।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 116, what time do others give for the rite?",
            ("A period of twelve nights", "द्वादशरात्रम् इति अन्ये."),
            [("Every single day", "Every day is the view of unit 118."),
             ("Only on the paired days", "Paired days are the view of unit 117."),
             ("Only under Puṣya", "Puṣya is the statement of unit 115, not of the others.")],
            "Others say: twelve nights.",
            "द्वादशरात्रम् = a period of twelve nights."),
        match(1, "Match each word of unit 116 to its meaning.",
              [["द्वादश", "twelve"], ["रात्रम्", "nights (a period of)"], ["इति", "thus, so"], ["अन्ये", "others"]],
              "Number, period, quote-marker and the holders of the view.",
              "द्वादश, रात्रम्, इति, अन्ये."),
        T(order(2, "Put the words of unit 116 in the line's order.",
                ["द्वादशरात्रम्", "इति", "अन्ये"],
                "The view, then इति, then who holds it.",
                "द्वादशरात्रम् → इति → अन्ये.", role="extend"),
          "A view is quoted, closed by इति, and its holders are named after it; the verb of saying is understood."),
        mcq("discriminate", 3, "Which split of इत्यन्ये is right?",
            ("इति + अन्ये", "इ + अ → य: इति + अन्ये = इत्यन्ये."),
            [("इत्य + अन्ये", "इत्य is not a word; the particle is इति."),
             ("इति + यन्ये", "यन्ये is not a word."),
             ("इत् + यन्ये", "Neither इत् nor यन्ये is a word of the card.")],
            "इति (thus) + अन्ये (others): इ before अ becomes य्.",
            "इ + अ → य."),
        multi("apply", 4, "Which statements about unit 116 are right?",
              [("The verb of saying is understood, not printed", "Right: the line is elliptical."),
               ("It reports another view on the time of the rite", "Right: a further opinion on the rite of unit 115."),
               ("It says the nights are counted from conception", "The starting point is not stated."),
               ("It names the others as Ātreya's pupils", "The others are not named.")],
              [0, 1],
              "An elliptical line: one view, one group of holders, no verb.",
              "X इति अन्ये = X, so others (say)."),
        mcq("transfer", 5, "By the rule of इत्यन्ये, how is इति + आह (thus he said) written when joined?",
            ("इत्याह", "इ + आ → या, as इ + अ → य in इत्यन्ये."),
            [("इत्यह", "The long आ of आह cannot turn short."),
             ("इतेआह", "इ does not become ए here, and vowels are not left side by side."),
             ("इताह", "The इ is not simply dropped.")],
            "इति + आह = इत्याह, like इति + अन्ये = इत्यन्ये.",
            "इ + a different vowel → य् + vowel.",
            teaches="The final इ of इति becomes य् before a different vowel: इति + अन्ये → इत्यन्ये."),
    ],
}

# ---------------------------------------------------------------- unit 117
AUTHORED["117"] = {
    "title": "तत्रापि युग्मदिनेष्विति केचित्",
    "question": "What view do some hold in unit 117?",
    "rule": ("तत्र अपि युग्मदिनेषु इति केचित्: even in that, on the paired (even) days, so some (hold). Elliptical like "
             "unit 116."),
    "limits": ("Which days count as paired is not stated, and what तत्र (in that) points to is not spelled out. "
               "No verb is printed."),
    "explain_hi": ("एक और मत: ‘उसमें भी युग्म (सम) दिनों में, ऐसा कुछ लोग (कहते हैं)।’ "
                   "‘युग्म’ = जोड़ा, सम; कौन-से दिन, यह नहीं बताया गया। ‘तत्र’ (उसमें) किस ओर संकेत करता है, पाठ स्पष्ट नहीं कहता। "
                   "सन्धियाँ: तत्र + अपि → तत्रापि (अ + अ → आ); दिनेषु + इति → दिनेष्विति (उ + इ → वि)।"),
    "hook": "केचित्: युग्म दिन।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 117, on which days do some say the rite should be?",
            ("On even days", "युग्मदिनेषु = on paired days."),
            [("On every day", "Every day is the view of unit 118."),
             ("For twelve nights", "Twelve nights is the view of unit 116."),
             ("On the odd days alone", "Odd days are not named.")],
            "Some say: on the paired days.",
            "युग्मदिनेषु = on paired (even) days."),
        match(1, "Match each word of unit 117 to its meaning.",
              [["तत्र", "there, in that"], ["अपि", "even"], ["युग्मदिनेषु", "on paired (even) days"],
               ["केचित्", "some"]],
              "Place-word, particle, the view and its holders.",
              "तत्र, अपि, युग्मदिनेषु, केचित्."),
        T(order(2, "Put the words of unit 117 in the line's order.",
                ["तत्र", "अपि", "युग्मदिनेषु", "इति", "केचित्"],
                "Even in that, on paired days, so some.",
                "तत्र → अपि → युग्मदिनेषु → इति → केचित्.", role="extend"),
          "Same frame as unit 116: view, इति, then its holders."),
        mcq("discriminate", 3, "Which split of युग्मदिनेष्विति is right?",
            ("युग्मदिनेषु + इति", "उ + इ → वि: दिनेषु + इति = दिनेष्विति."),
            [("युग्मदिनेषि + इति", "इ + इ would give ई: दिनेषीति."),
             ("युग्मदिनेष्व + इति", "That would join as दिनेष्वेति."),
             ("युग्मदिनेषु + विति", "विति is not a word.")],
            "युग्मदिनेषु (on paired days) + इति (thus): उ before इ becomes व्.",
            "उ + इ → वि."),
        mcq("apply", 4, "Which days does unit 117 say the paired days are?",
            ("It does not say which days are meant", "The data: which days are meant is not stated."),
            [("The days of the new moon", "No new moon is named."),
             ("The days of the Puṣya mansion", "Puṣya is named in unit 115, not here."),
             ("The days after the twelve nights", "No such link is stated.")],
            "युग्म = paired, even; the unit gives no list of days.",
            "युग्मदिन = paired days, not listed."),
        mcq("transfer", 5, "By the rule of दिनेष्विति, how is मधु + इति written when joined?",
            ("मध्विति", "उ + इ → वि, as in दिनेषु + इति."),
            [("मधूति", "उ + इ does not give ऊ."),
             ("मधेति", "उ + इ does not give ए."),
             ("मधुयिति", "No य् comes between उ and इ.")],
            "मधु + इति = मध्विति, like दिनेषु + इति = दिनेष्विति.",
            "उ + a different vowel → व् + vowel.",
            teaches="A final उ before a different vowel becomes व्: दिनेषु + इति → दिनेष्विति."),
    ],
}

# ---------------------------------------------------------------- unit 118
AUTHORED["118"] = {
    "title": "प्रत्यहमित्यपरे",
    "question": "What third view on the time does unit 118 report?",
    "rule": ("प्रत्यहम् इति अपरे: every day, so others (hold). प्रत्यहम् = प्रति + अहम्, an indeclinable: every day."),
    "limits": ("Elliptical like units 116 and 117: no verb printed, the others are not named, and the line does not say "
               "for how long."),
    "explain_hi": ("तीसरा मत: ‘प्रतिदिन, ऐसा दूसरे लोग (कहते हैं)।’ "
                   "‘प्रत्यहम्’ अव्ययीभाव है: प्रति + अहम् (इ + अ → य), अर्थ ‘हर दिन’। "
                   "तीन मत क्रम से: अन्ये = बारह रातें, केचित् = युग्म दिन, अपरे = प्रतिदिन। "
                   "‘इत्यपरे’ = इति + अपरे।"),
    "hook": "अन्ये बारह, केचित् युग्म, अपरे प्रतिदिन।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 118, how often do others say the rite should be?",
            ("Every day", "प्रत्यहम् = every day."),
            [("For twelve nights", "Twelve nights is the view of unit 116."),
             ("On paired days", "Paired days are the view of unit 117."),
             ("Once, under Puṣya", "Puṣya is the statement of unit 115.")],
            "Others say: every day.",
            "प्रत्यहम् = every day."),
        fill(1, "Every day, so others: ____ इत्यपरे (type it in Devanagari or in English letters, e.g. dharma).",
             accepts("प्रत्यहम्"),
             "प्रत्यहम् = every day, from प्रति + अहम्.",
             "प्रत्यहम् is an indeclinable: every day.",
             "प्रत्यहम् = every day.", role="warmup"),
        mcq("extend", 2, "What kind of word does the card call प्रत्यहम्?",
            ("An indeclinable meaning every day", "The card: ind. (avyayībhāva), every day."),
            [("A verb meaning he says daily", "No verb is printed in the line."),
             ("A plural noun meaning the others", "The others is अपरे."),
             ("A pronoun meaning that day", "No pronoun is in this line.")],
            "प्रति + अहम् makes the indeclinable प्रत्यहम्, every day.",
            "प्रत्यहम् = ind., every day.",
            teaches="प्रति + a noun of time can make an indeclinable of repetition: प्रत्यहम् = every day."),
        mcq("discriminate", 3, "Which split of प्रत्यहम् is right?",
            ("प्रति + अहम्", "इ + अ → य: प्रति + अहम् = प्रत्यहम्."),
            [("प्रत्य + अहम्", "प्रत्य is not a word; the prefix is प्रति."),
             ("प्रति + यहम्", "यहम् is not a word."),
             ("प्रत् + यहम्", "Neither प्रत् nor यहम् is a word.")],
            "प्रति (each) + अहम् (day): इ before अ becomes य्.",
            "इ + अ → य."),
        match(4, "Match each holder of a view in units 116 to 118 with the time they give.",
              [["अन्ये (others)", "द्वादशरात्रम्"], ["केचित् (some)", "युग्मदिनेषु"], ["अपरे (others)", "प्रत्यहम्"]],
              "Three views in a row: twelve nights, paired days, every day.",
              "अन्ये-द्वादशरात्रम्, केचित्-युग्मदिनेषु, अपरे-प्रत्यहम्.", role="apply"),
        mcq("transfer", 5, "By the rule of प्रत्यहम्, how is प्रति + एकम् (each one) written when joined?",
            ("प्रत्येकम्", "इ + ए → ये, as इ + अ → य in प्रत्यहम्."),
            [("प्रतेकम्", "इ + ए does not give ए alone."),
             ("प्रतीकम्", "इ + ए does not give ई."),
             ("प्रत्यैकम्", "ए stays ए; it does not become ऐ.")],
            "प्रति + एकम् = प्रत्येकम्, like प्रति + अहम् = प्रत्यहम्.",
            "इ + a different vowel → य् + vowel.",
            teaches="इ before a different vowel becomes य् and the vowel stays: प्रति + अहम् → प्रत्यहम्."),
    ],
}

# ---------------------------------------------------------------- unit 119
AUTHORED["119"] = {
    "title": "तद्यथा",
    "question": "What does the short line तद्यथा do in the text?",
    "rule": ("तद्यथा = तत् + यथा: that is as follows, namely. It introduces the procedure that the next units give."),
    "limits": ("Two words only; it states nothing itself. What follows is in the next units, not in this one."),
    "explain_hi": ("‘तद्यथा’ का अर्थ है ‘वह इस प्रकार है’, यानी आगे विधि बताई जाती है। "
                   "यह तत् (वह) + यथा (जैसे) से बना है; त् घोष वर्ण य से पहले द् हो जाता है। "
                   "इसमें कोई क्रिया नहीं और यह गद्य है। अगली इकाई (120) से विधि आरम्भ होती है।"),
    "hook": "तद्यथा = अब सुनो कैसे।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "What does unit 119 (तद्यथा) do in the text?",
            ("It leads into the procedure", "The data: it introduces the procedure of the next units."),
            [("It closes the chapter", "The chapter goes on after it."),
             ("It gives the time of the rite", "Times are given in units 115 to 118."),
             ("It reports another teacher's view", "No holder of a view is named.")],
            "तद्यथा = that is as follows: a lead-in to the steps.",
            "तद्यथा = namely, as follows."),
        mcq("warmup", 1, "What does तद्यथा mean?",
            ("That is as follows; namely", "तत् (that) + यथा (as)."),
            [("Therefore, for that reason", "Therefore would be अतः or तस्मात्."),
             ("Likewise, in that way", "In that way would be तद्वत् or तथा."),
             ("So say some others", "That pattern is इति केचित् or इति अपरे.")],
            "तद्यथा = that is as follows.",
            "तत् + यथा = namely."),
        fill(2, "That is as follows: तद्____ (type it in Devanagari or in English letters, e.g. dharma).",
             accepts("यथा", None, "yatha"),
             "तद्यथा = तत् + यथा.",
             "यथा = as; with तत् it means that is as follows.",
             "तत् + यथा = तद्यथा."),
        mcq("discriminate", 3, "Which split of तद्यथा is right?",
            ("तत् + यथा", "त् before the voiced य becomes द्."),
            [("तद + यथा", "There is no word तद with a final अ."),
             ("तत् + अथा", "That would join as तदथा, without य."),
             ("ता + द्यथा", "द्यथा is not a word.")],
            "तत् (that) + यथा (as): त् → द् before a voiced sound.",
            "त् + voiced sound → द्."),
        multi("apply", 4, "Which statements about unit 119 are right?",
              [("तत् is the neuter pronoun that", "Right: the card gives तत् n. nom. sg."),
               ("The procedure itself comes in the following units", "Right: it introduces what follows."),
               ("It is a metrical verse line", "The unit is prose."),
               ("It contains a verb of saying", "No verb occurs in it.")],
              [0, 1],
              "A two-word prose lead-in: that is as follows.",
              "तद्यथा = तत् + यथा, prose, no verb."),
        mcq("transfer", 5, "By the rule of तद्यथा, how is सत् + गुणः (good quality) written when joined?",
            ("सद्गुणः", "त् before the voiced ग becomes द्, as in तत् + यथा."),
            [("सत्गुणः", "त् is voiced to द् before a voiced consonant."),
             ("सन्गुणः", "न् comes before a nasal, not before ग."),
             ("सग्गुणः", "त् does not copy the next consonant here.")],
            "सत् + गुणः = सद्गुणः, like तत् + यथा = तद्यथा.",
            "त् + voiced consonant → द्.",
            teaches="A final त् before a voiced sound becomes द्: तत् + यथा → तद्यथा."),
    ],
}

# ===================================================================== NOTES_HI
NOTES_HI = {
    "107": "विश्वास मध्यम; गद्य, एक छपी पंक्ति। पाठ-चिह्न: छपा ‘गर्भ’ सम्भवतः ‘गर्भं’ है (अनुस्वार छूटा; ‘धत्ते’ का कर्म द्वितीया अपेक्षित)। छपा ‘वान’ = वा + न पढ़ा गया। ‘अतिमेदुरा’ = अत्यन्त स्थूल / अति स्निग्ध (सम्भावित; मेदुर = चिकना, मेदयुक्त), इसलिए इस पर प्रश्न नहीं। ‘अव्यवाय’ = सहवास का अभाव (व्यवाय = मैथुन, मानक); ‘विगुण’ = दोषयुक्त। दोनों ‘वा’ सूची और दोनों परिणामों को जोड़ते हैं। सन्धि जाँची: तत्र + अति + आशिता → तत्रात्याशिता (अ + अ → आ; इ + आ → या)। ‘क्रुद्धाऽतिमेदुरा’ आदि में छपा ऽ अगले शब्द के आरम्भिक अ (अतिमेदुरा, अन्यकामा, अव्यवायकामा) को दिखाता है, जो आ + अ → आ से मिल गया है।",
    "108": "विश्वास निम्न; दो छपी पंक्तियाँ (02.01.123, 02.01.124) जोड़ी गईं। पहली पंक्ति के पहले वाक्य ‘तथा पुरुषोऽपि’ में क्रिया नहीं; ‘पुरुष भी इकाई 107 की अवस्थाओं में न हो’ अनुमान मात्र है, कोई क्रिया जोड़ी नहीं गई। ‘अधः’ = नीचे, यानी स्त्री के नीचे (सम्भावित)। दूसरी पंक्ति (‘तथा हि’) पहली का परिणाम बताती है। सन्धि जाँची: पुरुषः + अपि → पुरुषोऽपि; न च असौ अधः तिष्ठेत् → नचासावधस्तिष्ठेत् (अ + अ → आ; औ + अ → आव; विसर्ग → स् त से पहले)। ‘असौ’ एकवचन है।",
    "109": "विश्वास उच्च, कोई पाठ-चिह्न नहीं। ‘न्युब्ज’ = औंधा, पेट के बल। ‘सेवेत’ = सेवन करे, समागम करे; स्त्री कर्म है (स्त्रीलिंग द्वितीया)। कर्ता नहीं छपा; सम्भवतः पुरुष।",
    "110": "विश्वास उच्च, कोई पाठ-चिह्न नहीं। वात तीन दोषों में से एक (कोई आधुनिक नाम नहीं)। ‘योनि’ = स्त्री का जनन-मार्ग / गर्भाशय (सम्भावित)। पहले वाक्य में ‘है’ समझा जाता है। सन्धि: वातः + बलवान् → वातो बलवान् (अः → ओ घोष व्यंजन से पहले); सः + योनिम् → स योनिम् (‘सः’ का विसर्ग व्यंजन से पहले लुप्त)।",
    "111": "विश्वास उच्च, कोई पाठ-चिह्न नहीं। ‘श्लेष्मन्’ = कफ (मानक पर्याय); ‘गर्भाशय’ = गर्भाशय, uterus (मानक)। ‘च्युत’ = अपने स्थान से हटा। ‘अपिदधाति’ = ढकता या बन्द करता है; सरल अर्थ ‘बन्द करता है’ लिया गया। सन्धि: पीडितः + च्युतः → पीडितश्च्युतः (विसर्ग → श् च से पहले); च्युतः + अपिदधाति → च्युतोऽपिदधाति (अः + अ → ओ, अ का लोप ऽ)।",
    "112": "विश्वास मध्यम। पाठ-चिह्न: छपा ‘रक्तशुके’ कोई शब्द नहीं; ‘रक्तशुक्रे’ (रक्त और शुक्र, नपुं. द्वितीया द्विवचन) सम्भावित सुधार — इसलिए ‘पित्त क्या जलाता है’ पर प्रश्न नहीं। ‘तद्वत्’ = इकाई 110-111 की तरह। पित्त दोष है (नाम रखा गया)। सन्धि: वामपार्श्वगायाः + तद्वत् → वामपार्श्वगायास्तद्वत् (विसर्ग → स् त से पहले); तद्वत् + पित्तम् → तद्वत्पित्तम्।",
    "113": "विश्वास मध्यम। पाठ-चिह्न: छपा ‘दस्मात्’ शब्द नहीं; ‘तस्मात्’ (इसलिए) सम्भावित (त/द भ्रम) — इस पर प्रश्न नहीं। ‘बीज’ = बीज, यहाँ सम्भवतः शुक्र। कर्ता स्त्री है (‘उत्ताना’ स्त्रीलिंग प्रथमा)। सन्धि: तस्मात् + उत्ताना → तस्मादुत्ताना (त् → द् स्वर से पहले); छपा ‘बीजंगृह्णीयात्’ = बीजम् + गृह्णीयात् (म् → ं)।",
    "114": "विश्वास मध्यम। पाठ-चिह्न: छपा ‘तथािह’ बिगड़ा देवनागरी रूप है; डेटा इसे तथा + इह रखता है, जबकि सन्धि से ‘तथेह’ अपेक्षित (आ + इ → ए) — सम्भवतः छपाई/OCR भूल; इस पर प्रश्न नहीं। ‘तथा’ से वाक्य किसी पहले कथन को आगे बढ़ाता है, पर डेटा यह नहीं बताता कि किसे। ‘यथास्थानम्’ = स्थान के अनुसार, हर एक अपने स्थान पर। छपा ‘तिष्ठंति’ = तिष्ठन्ति (अनुस्वार त से पहले न्)। दोष शब्द रखा गया।",
    "115": "विश्वास मध्यम। पाठ-चिह्न: छपा ‘प्रागव्यक्तीभावादृर्भस्य’ दो जगह क्षतिग्रस्त — ‘ऋर्भस्य’ शब्द नहीं (‘गर्भस्य’ अपेक्षित), और ‘अव्यक्ती-’ से ‘अप्रकट होने से पहले’ अर्थ नहीं बैठता; सुझाव ‘प्राग्व्यक्तीभावाद्गर्भस्य’ (गर्भ के प्रकट होने से पहले) अनुमानित है — इस पर कोई प्रश्न नहीं। ‘प्रयुञ्जीत’ का कर्ता नहीं छपा। पुंसवन = पुत्र-प्राप्ति हेतु संस्कार (मानक); यहाँ केवल ‘पुंसवन आदि’ कहा गया। पुष्य = नक्षत्र (मानक)। सन्धि: च + एनाम् → चैनाम् (अ + ए → ऐ); लब्धगर्भाम् → लब्धगर्भां (म् → ं)।",
    "116": "विश्वास मध्यम, कोई पाठ-चिह्न नहीं। संक्षिप्त वाक्य: ‘कहते हैं’ क्रिया समझी जाती है, जोड़ी नहीं गई। इकाई 115 के संस्कार के समय पर दूसरा मत माना गया। सन्धि: द्वादशरात्रम् + इति → द्वादशरात्रमिति; इति + अन्ये → इत्यन्ये (इ + अ → य)।",
    "117": "विश्वास मध्यम, कोई पाठ-चिह्न नहीं। इकाई 116 की तरह संक्षिप्त (कहने की क्रिया समझी जाती है)। ‘युग्म’ = जोड़ा, सम; कौन-से दिन, नहीं बताया। सन्धि: तत्र + अपि → तत्रापि (अ + अ → आ); युग्मदिनेषु + इति → युग्मदिनेष्विति (उ + इ → वि)।",
    "118": "विश्वास मध्यम, कोई पाठ-चिह्न नहीं। इकाई 116-117 की तरह संक्षिप्त। ‘प्रत्यहम्’ अव्ययीभाव (प्रति + अहम्, इ + अ → य); ‘इत्यपरे’ = इति + अपरे।",
    "119": "विश्वास उच्च, कोई पाठ-चिह्न नहीं। ‘तद्यथा’ = तत् + यथा (त् → द् घोष य से पहले); आगे की विधि (इकाई 120 से) का आरम्भ-सूचक।",
}

# ===================================================================== AIDS
AIDS = {
    "107": {
        "diagram": {"groups": [
            {"label": "स्त्री की अवस्थाएँ (क्रम से)", "items": ["अत्याशिता", "क्षुधिता", "पिपासिता", "भीता", "विमनाः",
                                                         "शोकार्ता", "क्रुद्धा", "अतिमेदुरा (सम्भावित अर्थ)",
                                                         "अन्यकामा", "अव्यवायकामा"]},
            {"label": "परिणाम", "items": ["न गर्भं धत्ते", "विगुणं वा (धत्ते)"]}]},
        "chunks": "तत्रात्याशिता क्षुधिता पिपासिता | भीता विमनाः शोकार्ता | क्रुद्धाऽतिमेदुरा | ऽन्यकामाऽव्यवायकामा | वा न गर्भ(ं) धत्ते | विगुणं वा",
        "sandhi": "अ + अ → आ: तत्र + अति → तत्राति · इ + आ → या: अति + आशिता → अत्याशिता · छपा ‘वान’ = वा + न।",
        "frame": "पहले लम्बी सूची (सब स्त्रीलिंग प्रथमा), अन्त में क्रिया ‘धत्ते’ और दो विकल्प: न गर्भ, या विगुण गर्भ।",
    },
    "108": {
        "chain": {"steps": ["यदि पुरुष नीचे (अधः) रहे (जो वर्जित है)", "तथा हि (क्योंकि इस प्रकार)", "स्त्रीचेष्ट पुमान्", "या पुंचेष्टा स्त्री जन्मे"]},
        "sandhi": "अः + अ → ओ ऽ: पुरुषः + अपि → पुरुषोऽपि · अ + अ → आ: च + असौ → चासौ · औ + अ → आव: असौ + अधः → असावधः · विसर्ग → स् (त से पहले): अधः + तिष्ठेत् → अधस्तिष्ठेत्।",
        "contrast": "स्त्रीचेष्टः पुमान् (स्त्री जैसी चेष्टा वाला पुरुष) ↔ पुंचेष्टा स्त्री (पुरुष जैसी चेष्टा वाली स्त्री)।",
    },
    "109": {
        "chunks": "न च | न्युब्जां | पार्श्वगतां वा | सेवेत",
        "anchors": "याद-सूत्र: दो वर्जित स्थितियाँ — औंधी और करवट; कारण अगली तीन इकाइयों में। (मेरी याद-पद्धति)",
        "frame": "न + कर्म (स्त्रीलिंग द्वितीया: न्युब्जाम्, पार्श्वगताम्) + विधिलिङ् ‘सेवेत’ = ऐसी का सेवन न करे।",
    },
    "110": {
        "chain": {"steps": ["न्युब्जायाम् (औंधी में)", "वातः बलवान् (वात बलवान)", "स योनिं पीडयति (वह योनि को पीड़ा देता)"]},
        "sandhi": "अः → ओ (घोष व्यंजन से पहले): वातः + बलवान् → वातो बलवान् · ‘सः’ का विसर्ग व्यंजन से पहले लुप्त: सः + योनिम् → स योनिम्।",
        "contrast": "इकाई 109: न्युब्जाम् (द्वितीया, कर्म) ↔ इकाई 110: न्युब्जायाम् (सप्तमी, ‘उसमें’)।",
    },
    "111": {
        "chain": {"steps": ["दक्षिण करवट", "श्लेष्मा (कफ) दबा", "अपने स्थान से च्युत", "गर्भाशय बन्द"]},
        "sandhi": "विसर्ग → श् (च से पहले): पीडितः + च्युतः → पीडितश्च्युतः · अः + अ → ओ ऽ: च्युतः + अपिदधाति → च्युतोऽपिदधाति।",
        "chunks": "दक्षिणपार्श्वगायाः | श्लेष्मा | पीडितश्च्युतो | ऽपिदधाति | गर्भाशयं",
    },
    "112": {
        "contrast": {"groups": [
            {"label": "स्थिति", "items": ["न्युब्जा (औंधी)", "दक्षिणपार्श्वगा", "वामपार्श्वगा"]},
            {"label": "दोष और कार्य", "items": ["वात: योनि को पीड़ा", "कफ: गर्भाशय बन्द", "पित्त: जलाता है (वस्तु संदिग्ध)"]}]},
        "sandhi": "विसर्ग → स् (त से पहले): वामपार्श्वगायाः + तद्वत् → वामपार्श्वगायास्तद्वत्।",
        "anchors": "याद-सूत्र: औंधी-वात, दाहिनी-कफ, बायीं-पित्त — तीन स्थिति, तीन दोष। (मेरी याद-पद्धति)",
    },
    "113": {
        "contrast": "वर्जित: न्युब्जा, पार्श्वगता (इकाई 109) ↔ उचित: उत्ताना (इकाई 113)।",
        "sandhi": "म् → ं (व्यंजन से पहले): बीजम् + गृह्णीयात् → बीजं गृह्णीयात् · त् → द् (स्वर से पहले): तस्मात् + उत्ताना → तस्मादुत्ताना (छपा ‘दस्मा-’)।",
        "chunks": "दस्माद् (सम्भावित तस्माद्) | उत्ताना | बीजं | गृह्णीयात्",
    },
    "114": {
        "chunks": "तथा(इह) | यथास्थानमेव | तिष्ठन्ति | दोषाः",
        "frame": "कर्ता ‘दोषाः’ (बहुवचन) अन्त में, क्रिया ‘तिष्ठन्ति’ (बहुवचन) उससे पहले, और ‘यथास्थानमेव’ = कहाँ।",
        "sandhi": "म् + स्वर: यथास्थानम् + एव → यथास्थानमेव · छपा ‘तिष्ठंति’ = तिष्ठन्ति (अनुस्वार = न् त से पहले)।",
    },
    "115": {
        "chain": {"steps": ["लब्धगर्भा जानकर (विदित्वा)", "पुष्ये (पुष्य नक्षत्र में)", "पुंसवनादि", "प्रयुञ्जीत (प्रयोग करे)"]},
        "sandhi": "अ + ए → ऐ: च + एनाम् → चैनाम् · म् → ं: लब्धगर्भाम् + च → लब्धगर्भां च।",
        "chunks": "लब्धगर्भां चैनां विदित्वा | (क्षतिग्रस्त: प्रागव्यक्तीभावादृर्भस्य) | पुष्ये | पुंसवनादि प्रयुञ्जीत",
    },
    "116": {
        "frame": "मत + इति + मत रखने वाले: द्वादशरात्रम् इति अन्ये (‘कहते हैं’ समझा जाता है)।",
        "sandhi": "इ + अ → य: इति + अन्ये → इत्यन्ये · म् + स्वर: द्वादशरात्रम् + इति → द्वादशरात्रमिति।",
    },
    "117": {
        "frame": "वही ढाँचा: तत्रापि युग्मदिनेषु (मत) इति केचित् (कौन)।",
        "sandhi": "अ + अ → आ: तत्र + अपि → तत्रापि · उ + इ → वि: युग्मदिनेषु + इति → युग्मदिनेष्विति।",
    },
    "118": {
        "contrast": {"groups": [
            {"label": "कौन", "items": ["अन्ये (इकाई 116)", "केचित् (इकाई 117)", "अपरे (इकाई 118)"]},
            {"label": "क्या समय", "items": ["द्वादशरात्रम्", "युग्मदिनेषु", "प्रत्यहम्"]}]},
        "sandhi": "इ + अ → य: प्रति + अहम् → प्रत्यहम्; इति + अपरे → इत्यपरे।",
        "pegs": "मेरा बनाया चित्र: तीन लोग एक कैलेंडर के सामने — एक बारह रातों पर घेरा बनाता है, दूसरा जोड़े वाले दिनों पर, तीसरा हर दिन पर निशान लगाता है। (केवल याद के लिए)",
    },
    "119": {
        "sandhi": "त् → द् (घोष य से पहले): तत् + यथा → तद्यथा।",
        "frame": "तद्यथा = ‘वह इस प्रकार है’: आगे विधि आएगी (इकाई 120 से)।",
    },
}

# ===================================================================== IMAGE_SPECS
IMAGE_SPECS = {
    ("107", "diagram"): {
        "file": "sh1-garbha-varjya-107.svg",
        "alt": ("Two columns for unit 107: ten states of the woman in text order (over-fed, hungry, thirsty, frightened, "
                "dejected, grief-stricken, angry, very fat as a probable sense, desiring another, desiring no intercourse) "
                "and the two outcomes: she does not bear a foetus, or bears a defective one."),
        "type": "split",
        "title": "इकाई १०७: अवस्था और परिणाम",
        "cols": [["ऐसी स्त्री", ["अत्याशिता", "क्षुधिता", "पिपासिता", "भीता", "विमनाः", "शोकार्ता", "क्रुद्धा",
                                 "अतिमेदुरा (सम्भावित)", "अन्यकामा", "अव्यवायकामा"]],
                 ["परिणाम", ["गर्भ धारण नहीं", "या विगुण गर्भ"]]],
    },
    ("110", "chain"): {
        "file": "sh1-nyubja-vata-110.svg",
        "alt": ("Chain of unit 110: in a woman lying face down, Vata is strong, and it presses the yoni."),
        "type": "chain",
        "title": "औंधी स्थिति (इकाई ११०)",
        "steps": ["औंधी लेटी में", "वात बलवान", "वह योनि को पीड़ा देता"],
    },
    ("111", "chain"): {
        "file": "sh1-dakshina-kapha-111.svg",
        "alt": ("Chain of unit 111: lying on the right side, Kapha is pressed, is displaced from its place, and closes the womb."),
        "type": "chain",
        "title": "दाहिनी करवट (इकाई १११)",
        "steps": ["दाहिनी करवट", "कफ दबा", "स्थान से च्युत", "गर्भाशय बन्द"],
    },
    ("112", "contrast"): {
        "file": "sh1-parshva-dosha-112.svg",
        "alt": ("Table of units 110 to 112: lying face down, Vata presses the yoni; on the right side, Kapha closes the womb; "
                "on the left side, Pitta burns, its object being a doubtful reading."),
        "type": "table",
        "title": "तीन वर्जित स्थितियाँ (११०-११२)",
        "heads": ["स्थिति", "दोष और कार्य"],
        "rows": [["औंधी (न्युब्जा)", "वात: योनि को पीड़ा"],
                 ["दाहिनी करवट", "कफ: गर्भाशय बन्द"],
                 ["बायीं करवट", "पित्त: जलाता (वस्तु संदिग्ध)"]],
    },
    ("115", "chain"): {
        "file": "sh1-pumsavana-115.svg",
        "alt": ("Flowchart of the sure parts of unit 115: having known she has conceived, in the lunar mansion Pushya, "
                "one should employ the pumsavana and the like."),
        "type": "mermaid",
        "code": ("flowchart TD\n"
                 "  A[\"गर्भ प्राप्त जानकर\"] --> B[\"पुष्य नक्षत्र में\"]\n"
                 "  B --> C[\"पुंसवन आदि\"]\n"
                 "  C --> D[\"प्रयोग करे\"]\n"),
    },
    ("118", "contrast"): {
        "file": "sh1-trayo-mata-118.svg",
        "alt": ("Table of units 116 to 118, three views on the time: others say twelve nights; some say on paired days; "
                "others again say every day."),
        "type": "table",
        "title": "तीन मत (११६-११८)",
        "heads": ["कौन कहते", "समय"],
        "rows": [["अन्ये (अन्य लोग)", "बारह रातें"],
                 ["केचित् (कुछ लोग)", "युग्म दिनों में"],
                 ["अपरे (दूसरे लोग)", "प्रतिदिन"]],
    },
}
