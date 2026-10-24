from helpers import mcq, match, order, fill, multi, accepts


def T(q, teaches):
    q["teaches"] = teaches
    return q


AUTHORED = {}

# ---------------------------------------------------------------- unit 114
AUTHORED["114"] = {
    "title": "विवृतशया नक्तचारिणी",
    "question": "By unit 114, which two habits of the woman are named, and what does she produce?",
    "rule": ("She who sleeps uncovered (vivṛtaśayā) and she who roams at night (naktacāriṇī) produces a mad (unmatta) "
             "one. Its verb जनयति (produces) is carried on through units 115 to 125."),
    "limits": ("That the woman is pregnant is understood from the context, not printed. Whether one woman has both habits "
               "or either one is enough is left open by the wording (singular verb), so no question rests on it. विवृत may "
               "also mean 'in the open'. A prose line, not a verse."),
    "explain_hi": ("यह छोटी गद्य-पंक्ति माता के दो स्वभाव बताती है: बिना ढके सोना (विवृतशया) और रात में घूमना (नक्तचारिणी)। "
                   "परिणाम: वह उन्मत्त यानी पागल सन्तान को उत्पन्न करती है। "
                   "वह गर्भिणी है, यह प्रसंग से समझा जाता है; एक ही स्त्री में दोनों स्वभाव हों या एक भी काफ़ी है, यह पाठ खुला छोड़ता है। "
                   "यहाँ छपी क्रिया ‘जनयति’ आगे इकाई ११५ से १२५ तक की सब पंक्तियों में समझी जाती है। "
                   "‘चोन्मत्तम्’ में च + उन्मत्तम् की सन्धि है (अ + उ → ओ)।"),
    "hook": "बिना ढके सोना, रात में घूमना: उन्मत्त सन्तान।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 114, what is produced by she who sleeps uncovered and she who roams at night?",
            ("A mad one", "चोन्मत्तं जनयति: she produces a mad one."),
            [("An epileptic one", "Apasmāra (epilepsy) is the result in unit 115."),
             ("A blind-born one", "Blindness is not named in this line."),
             ("A short-lived one", "Short life is a result in unit 116.")],
            "The two habits lead to a mad (उन्मत्त) child.",
            "विवृतशया, नक्तचारिणी → उन्मत्त."),
        order(1, "Put the words of unit 114 in their printed order.",
              ["विवृतशया", "नक्तचारिणी", "चोन्मत्तं", "जनयति"],
              "Sleeping uncovered … roaming at night … and a mad one … produces.",
              "विवृतशया → नक्तचारिणी → चोन्मत्तं → जनयति."),
        match(2, "Match each word of unit 114 to its meaning on the card.",
              [["विवृत", "uncovered, exposed"], ["शया", "sleeping (she who sleeps)"], ["नक्त", "night"],
               ["चारिणी", "she who roams"], ["उन्मत्त", "mad"]],
              "The two compounds name the habits; उन्मत्त names the result.",
              "विवृत-शया, नक्त-चारिणी, उन्मत्त.", role="extend",
              teaches="नक्त + चारिणी: -चारिणी at the end of a compound = she who roams in X, here at night."),
        mcq("discriminate", 3, "Which split of चोन्मत्तं is right?",
            ("च + उन्मत्तम्", "अ + उ → ओ: च + उन्मत्तम् → चोन्मत्तम्."),
            [("चः + उन्मत्तम्", "अः before उ loses the visarga and leaves a gap: च उन्मत्तम्."),
             ("चो + न्मत्तम्", "न्मत्तम् is not a word; the card has उन्मत्त."),
             ("च + ओन्मत्तम्", "ओन्मत्त is not a word; the card has उन्मत्त.")],
            "च (and) + उन्मत्तम् (a mad one, acc.): अ + उ → ओ.",
            "अ + उ → ओ."),
        multi("apply", 4, "Which two are right about unit 114 by the card?",
              [("जनयति (produces) is printed in this unit", "Right: the verb is printed here and carried on to unit 125."),
               ("It says she must have both habits", "The wording leaves open whether both or either one is meant."),
               ("It is a prose line, not a verse", "Right: the unit is prose."),
               ("A word for pregnant is printed in it", "Pregnancy is understood from the context; no such word is printed.")],
              [0, 2],
              "A prose line whose verb जनयति serves the following units too.",
              "जनयति is printed here; the rest of the series borrows it."),
        mcq("transfer", 5, "By the join of चोन्मत्तम्, how is च + उदकम् (water) written when joined?",
            ("चोदकम्", "अ + उ → ओ, as in च + उन्मत्तम् → चोन्मत्तम्."),
            [("चौदकम्", "औ comes from अ + ओ or औ, not from अ + उ."),
             ("चुदकम्", "The अ does not vanish; it merges with उ into ओ."),
             ("च्वुदकम्", "व् replaces उ, not अ; here अ comes first.")],
            "च + उन्मत्तम् → चोन्मत्तम्; so च + उदकम् → चोदकम्.",
            "अ + उ → ओ.",
            teaches="A final अ and an initial उ merge into ओ: च + उन्मत्तम् → चोन्मत्तम्."),
    ],
}

# ---------------------------------------------------------------- unit 115
AUTHORED["115"] = {
    "title": "कलहशीलाऽपस्मारिणं",
    "question": "By unit 115, what does the quarrelsome woman produce?",
    "rule": ("She who is quarrelsome by nature (kalahaśīlā) produces one with apasmāra (epilepsy, standard). The verb "
             "जनयति is carried from unit 114."),
    "limits": ("The verb is not printed; it is carried from unit 114. The child's noun is unstated ('one'). Nothing is said "
               "on cure or prevention."),
    "explain_hi": ("यह एक ही छपा शब्द-समूह है: कलहशीला + अपस्मारिणम्। कलहशीला यानी झगड़ालू स्वभाव वाली माता (प्रथमा, कर्ता)। "
                   "अपस्मारिणम् यानी अपस्मार (मिर्गी, मानक) वाली सन्तान (द्वितीया, कर्म)। "
                   "क्रिया ‘जनयति’ इकाई ११४ से आती है, यहाँ छपी नहीं। "
                   "छपा ऽ दिखाता है कि आ + अ → आ में अ लुप्त हुआ; यह छपाई की आदत है।"),

    "hook": "झगड़े का स्वभाव: अपस्मार वाली सन्तान।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 115, what does a woman quarrelsome by nature produce?",
            ("One with apasmāra (epilepsy)", "कलहशीला अपस्मारिणम्: one with apasmāra."),
            [("A mad one", "The mad one is the result of unit 114."),
             ("A very stout (atisthūla) one", "Stoutness is a result in unit 122."),
             ("A jealous (īrṣyālu) one", "Jealousy is a result in unit 117.")],
            "Quarrelsome nature → a child with apasmāra.",
            "कलहशीला → अपस्मारिन्."),
        match(1, "Match each part of unit 115 to its meaning on the card.",
              [["कलह", "quarrel"], ["शील", "habit, disposition"], ["अपस्मार", "epilepsy (standard)"],
               ["जनयति", "produces (carried from unit 114)"]],
              "The habit, the disease, and the verb borrowed from unit 114.",
              "कलह = quarrel; शील = habit; अपस्मार = epilepsy."),
        fill(2, "The woman of unit 115 is ____-शीला, quarrelsome by nature. Type the first part in Devanagari or in English letters (e.g. dharma).",
             accepts("कलह"),
             "कलहशीला = कलह (quarrel) + शीला (having as habit).",
             "-शील at the end of a compound = having X as habit or nature: कलहशीला = quarrelsome by nature.",
             "कलह = quarrel."),
        mcq("discriminate", 3, "Which split of कलहशीलाऽपस्मारिणं is right?",
            ("कलहशीला + अपस्मारिणम्", "आ + अ → आ; the print marks the lost अ with ऽ."),
            [("कलहशीलः + अपस्मारिणम्", "अः + अ would give कलहशीलोऽपस्मारिणम्, with ओ."),
             ("कलहशीले + अपस्मारिणम्", "ए + अ would give कलहशीलेऽपस्मारिणम्, with ए."),
             ("कलहशीला + पस्मारिणम्", "पस्मारिन् is not a word; ऽ marks a lost अ.")],
            "कलहशीला (f. nom. sg.) + अपस्मारिणम् (acc. sg.).",
            "आ + अ → आ, shown by ऽ."),
        mcq("apply", 4, "By its case, who is कलहशीला in unit 115?",
            ("The woman, the subject (f. nom. sg.)", "Nominative: she is the one who produces."),
            [("The child, the object (acc. sg.)", "The child is अपस्मारिणम्, in the accusative."),
             ("A nurse who looks after the child", "No nurse is named in this line."),
             ("The father of the child to come", "No father is named; the form is feminine.")],
            "Nominative = the mother (subject); accusative = the child (object).",
            "f. nom. = she who produces; acc. = the one produced."),
        mcq("transfer", 5, "By the pattern of कलहशीला, what does an invented क्रोधशीला mean (क्रोध = anger)?",
            ("She who is angry by nature", "-शीला = having X as habit: anger as her nature."),
            [("She who is free of anger", "-शील means having the habit, not being free of it."),
             ("She who fears anger in others", "-शील names her own habit, not a fear."),
             ("She who is born out of anger", "-शील does not mean born of.")],
            "कलहशीला = quarrelsome by nature; क्रोधशीला = angry by nature.",
            "X-शीला = she who has X as habit.",
            teaches="-शील at the end of a compound = having X as one's habit or nature."),
    ],
}

# ---------------------------------------------------------------- unit 116
AUTHORED["116"] = {
    "title": "व्यवायशीला दुर्वपुषम्",
    "question": "By unit 116, what may a woman given to intercourse, and one given to grief, produce?",
    "rule": ("Given to sexual intercourse (vyavāya): an ill-shaped, (conjecturally) shameless or womanish (straiṇa) one. "
             "Constantly given to grief (śoka): a timid, wasted or short-lived one. वा = or."),
    "limits": ("अह्रीकम् (shameless) is a conjecture for the printed अन्हीकं: no question rests on it. शोक- corrects a stray "
               "sign in printed शॉक- (near certain). स्त्रैण may also mean fond of women, अपचित also honoured; the card "
               "keeps womanish and wasted. Verb from unit 114."),
    "explain_hi": ("यह इकाई दो छपी गद्य-पंक्तियाँ जोड़ती है, हर पंक्ति में माता का एक स्वभाव और सन्तान के तीन विकल्प, अन्त में ‘वा’ (या)। "
                   "व्यवाय यानी मैथुन में लगी रहने वाली माता से: बुरे शरीर वाली, अनुमानित पाठ पर निर्लज्ज, या स्त्रैण सन्तान। "
                   "निरन्तर शोक में रहने वाली से: डरपोक, क्षीण या अल्पायु सन्तान। "
                   "छपा ‘अन्हीकं’ कोई ज्ञात शब्द नहीं; ‘अह्रीकम्’ केवल अनुमान है। "
                   "क्रिया ‘जनयति’ इकाई ११४ से आती है।"),

    "hook": "व्यवाय से बुरा शरीर; शोक से डर और छोटी आयु।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 116, which result may a woman given to intercourse (vyavāya) produce?",
            ("An ill-shaped one", "व्यवायशीला दुर्वपुषम्: an ill-shaped one."),
            [("A mad one", "The mad one is the result of unit 114."),
             ("An epileptic one", "Apasmāra is the result of unit 115."),
             ("A red-eyed one", "Red eyes are a result in unit 121.")],
            "Vyavāya as habit → an ill-shaped, (conjecturally) shameless or womanish one.",
            "व्यवायशीला → दुर्वपुस् …"),
        match(1, "Match each word of unit 116 to its meaning on the card.",
              [["व्यवाय", "sexual intercourse"], ["दुर्वपुस्", "ill-shaped (bad body)"], ["स्त्रैण", "womanish"],
               ["भीरु", "timid"], ["अल्पायुस्", "short-lived"]],
              "One habit word and four result words of the two lines.",
              "व्यवाय, दुर्वपुस्, स्त्रैण, भीरु, अल्पायुस्."),
        order(2, "Put these words of unit 116 in their printed order.",
              ["व्यवायशीला", "दुर्वपुषम्", "स्त्रैणं वा", "भीरुम्", "अपचितम्", "अल्पायुषं वा"],
              "Line 1: the habit, then its results closed by वा; line 2 (after शॉकनित्या): timid, wasted, short-lived, वा.",
              "व्यवायशीला → दुर्वपुषम् → स्त्रैणं वा → भीरुम् → अपचितम् → अल्पायुषं वा.", role="extend",
              teaches="Each line gives the habit first (nominative), then its results (accusative), and वा (or) closes the list."),
        mcq("discriminate", 3, "Which split of अल्पायुषं is right?",
            ("अल्प + आयुषम्", "अ + आ → आ: अल्प + आयुषम् → अल्पायुषम्."),
            [("अल्पम् + आयुषम्", "म् before आ would give अल्पमायुषम्."),
             ("अल्पः + आयुषम्", "अः before आ would leave a gap: अल्प आयुषम्."),
             ("अल्पा + युषम्", "युषम् is not a word; the card has आयुस्.")],
            "अल्प (short) + आयुषम् (life): a short-lived one.",
            "अ + आ → आ."),
        mcq("apply", 4, "Which English of भीरुमपचितमल्पायुषं वा is right?",
            ("A timid, wasted or short-lived (one)", "भीरु = timid; अपचित = wasted; अल्पायुस् = short-lived."),
            [("A timid, wasted or long-lived (one)", "अल्प means little, short: short-lived."),
             ("A brave, wasted or short-lived (one)", "भीरु means timid, not brave."),
             ("A timid, well-fed or short-lived (one)", "अपचित is wasted here, not well-fed.")],
            "Three results, joined by वा: timid, wasted, short-lived.",
            "भीरु, अपचित, अल्पायुस्."),
        mcq("transfer", 5, "By the pattern of दुर्वपुस् (दुः + वपुस्, body), what does दुर्बुद्धि mean (बुद्धि = mind)?",
            ("Of bad mind, foolish", "दुः- = bad, ill: a bad mind."),
            [("Of great mind, wise", "दुः- means bad, not great."),
             ("Of two minds, doubtful", "दुः- is not द्वि (two)."),
             ("Of a quick mind, sharp", "दुः- does not mean quick.")],
            "दुः + वपुस् → दुर्वपुस् (ill-shaped); दुः + बुद्धि → दुर्बुद्धि (of bad mind).",
            "दुः- (दुर्-) = bad, ill.",
            teaches="दुः- before a word means bad or ill; before a voiced sound its visarga becomes र्: दुर्वपुस्."),
    ],
}

# ---------------------------------------------------------------- unit 117
AUTHORED["117"] = {
    "title": "अभिध्यायिनी परोपतापनम्",
    "question": "By unit 117, what may a covetous woman produce, and what a thieving one?",
    "rule": ("Covetous (abhidhyāyinī): one who torments others, a jealous or a womanish one. A thief (stenā, probable "
             "split): one abounding in toil, hostile, or given to inaction."),
    "limits": ("The split स्तेना तु आयासबहुलम् … of line 2 is probable, not certain, so no question rests on स्तेना or तु. "
               "अकर्मशील may also mean given to wrong action; the card keeps inaction. The verb comes from unit 114. "
               "Two printed lines."),
    "explain_hi": ("पहली छपी पंक्ति: लोभ करने वाली (अभिध्यायिनी, दूसरे की वस्तु की लालसा) माता से दूसरों को सन्ताप देने वाली, ईर्ष्यालु "
                   "या स्त्रैण सन्तान। दूसरी पंक्ति एक लम्बा जुड़ा शब्द है; उसका विभाजन ‘स्तेना तु …’ (चोर स्त्री तो) सम्भावित है, पक्का नहीं। "
                   "उसके परिणाम: परिश्रम से भरी, द्रोही या अकर्मशील सन्तान। "
                   "‘परोपतापन’ में पर + उपतापन की सन्धि है (अ + उ → ओ)। क्रिया ‘जनयति’ इकाई ११४ से आती है।"),

    "hook": "लोभ से ईर्ष्या, चोरी से द्रोह।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 117, which result may a covetous (abhidhyāyinī) woman produce?",
            ("A jealous (īrṣyālu) one", "अभिध्यायिनी … ईर्ष्यालुम्: a jealous one."),
            [("A bald (khalatika) one", "Baldness is a result in unit 123."),
             ("A timid (bhīru) one", "The timid one is a result in unit 116."),
             ("A drowsy (nidrālu) one", "Drowsiness is a result in unit 119.")],
            "Covetous → one who torments others, a jealous or a womanish one.",
            "अभिध्यायिनी → परोपतापन, ईर्ष्यालु, स्त्रैण."),
        order(1, "Put the words of line 1 of unit 117 in their printed order.",
              ["अभिध्यायिनी", "परोपतापनम्", "ईर्ष्यालुम्", "स्त्रैणं वा"],
              "The covetous one … tormenting others … jealous … or womanish.",
              "अभिध्यायिनी → परोपतापनम् → ईर्ष्यालुम् → स्त्रैणं वा."),
        match(2, "Match each word of unit 117 to its meaning on the card.",
              [["अभिध्या", "coveting another's possession"], ["परोपतापन", "tormenting others"],
               ["ईर्ष्यालु", "jealous"], ["अभिद्रोहिन्", "hostile, malicious"], ["आयासबहुल", "abounding in toil"]],
              "The habit word of line 1 and four result words of both lines.",
              "अभिध्या, परोपतापन, ईर्ष्यालु, अभिद्रोहिन्, आयासबहुल.", role="extend",
              teaches="पर (others) + उपतापन (tormenting) = परोपतापन, one who torments others."),
        mcq("discriminate", 3, "Which English of परोपतापनमीर्ष्यालुं स्त्रैणं वा is right?",
            ("One who torments others, a jealous or womanish (one)", "पर = others; उपतापन = tormenting; ईर्ष्यालु = jealous."),
            [("One who comforts others, a jealous or womanish (one)", "उपतापन is tormenting, not comforting."),
             ("One who torments himself, a jealous or womanish (one)", "पर means others, not oneself."),
             ("One who torments others, a generous or womanish (one)", "ईर्ष्यालु means jealous, not generous.")],
            "Three results, closed by वा: tormenting others, jealous, womanish.",
            "परोपतापन, ईर्ष्यालु, स्त्रैण."),
        multi("apply", 4, "Which two are right about unit 117 by the card?",
              [("The split स्तेना तु … of line 2 is certain", "The card calls the split probable, not certain."),
               ("अभिध्यायिनी is the woman, the subject (f. nom. sg.)", "Right: the habit word is nominative."),
               ("The verb जनयति is printed in this unit", "It is carried from unit 114, not printed here."),
               ("ईर्ष्यालुम् is accusative: it describes the one produced", "Right: results stand in the accusative.")],
              [1, 3],
              "Habit in the nominative, results in the accusative; the line-2 split is only probable.",
              "f. nom. = the woman; acc. = the one produced."),
        mcq("transfer", 5, "By the join of परोपतापन, how is पर + उपकार (help) written as one word?",
            ("परोपकार", "अ + उ → ओ, as in पर + उपतापन → परोपतापन."),
            [("परौपकार", "औ comes from अ + ओ or औ, not from अ + उ."),
             ("परुपकार", "The अ does not vanish; it merges with उ into ओ."),
             ("परूपकार", "अ + उ gives ओ, not a long ऊ.")],
            "पर + उपतापन → परोपतापन; so पर + उपकार → परोपकार (helping others).",
            "अ + उ → ओ.",
            teaches="अ + उ merge into ओ inside a compound: पर + उपतापन → परोपतापन."),
    ],
}

# ---------------------------------------------------------------- unit 118
AUTHORED["118"] = {
    "title": "अमर्षणा चंडम्",
    "question": "By unit 118, what may an intolerant woman produce?",
    "rule": ("She who is intolerant (amarṣaṇā, impatient of offence) produces a fierce (caṇḍa) or a probably deceitful "
             "(aupadhika) one. वा = or."),
    "limits": ("औपधिक = deceitful is probable only (the word has other senses, e.g. additional): no question rests on its "
               "meaning. The print joins वा to the word before (a spacing slip). The verb comes from unit 114."),
    "explain_hi": ("यह छोटी गद्य-पंक्ति है: असहनशील (अमर्षणा) माता उग्र (चण्ड) या सम्भवतः कपटी (औपधिक) सन्तान को उत्पन्न करती है। "
                   "‘औपधिक’ का ‘कपटी’ अर्थ (उपधि = छल से) सम्भावित है, पक्का नहीं। "
                   "छपा ‘चंड’ = चण्ड: ड से पहले अनुस्वार ण् के स्थान पर लिखा गया है। "
                   "छपाई में ‘वा’ पिछले शब्द से जुड़ा है (औपधिकंवा); यह केवल दूरी की भूल है। क्रिया इकाई ११४ से।"),
    "hook": "असहनशील माता: उग्र सन्तान।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 118, which sure result may an intolerant (amarṣaṇā) woman produce?",
            ("A fierce (caṇḍa) one", "अमर्षणा चण्डम्: a fierce one."),
            [("A mute (mūka) one", "The mute one is a result in unit 122."),
             ("A short-lived one", "Short life is a result in unit 116."),
             ("One with urinary stone", "Aśmarī is a result in unit 120.")],
            "Intolerant → a fierce or a probably deceitful one.",
            "अमर्षणा → चण्ड …"),
        match(1, "Match each word of unit 118 to its meaning on the card.",
              [["अमर्षणा", "intolerant (she)"], ["चण्ड", "fierce, violent"], ["वा", "or"],
               ["जनयति", "produces (carried from unit 114)"]],
              "Habit, sure result, the closing particle, and the borrowed verb.",
              "अमर्षणा, चण्ड, वा, जनयति."),
        order(2, "Put the parts of unit 118 in their printed order.",
              ["अमर्षणा", "चंडम्", "औपधिकम्", "वा"],
              "Intolerant … fierce … (probably) deceitful … or.",
              "अमर्षणा → चंडम् → औपधिकम् → वा.", role="extend",
              teaches="As in the whole series, the habit (nominative) comes first, then the results (accusative), then वा."),
        mcq("discriminate", 3, "Which split of चंडमौपधिकंवा is right?",
            ("चण्डम् + औपधिकम् + वा", "म् joins the next vowel औ; वा is printed joined by a spacing slip."),
            [("चण्ड + औपधिकम् + वा", "अ + औ would give चण्डौपधिकम्, with no म."),
             ("चण्डमौ + पधिकम् + वा", "पधिक is not a word of the card."),
             ("चण्डम् + औपधिकंवा (one word)", "वा (or) is a separate word; the print only runs it on.")],
            "चण्डम् (fierce, acc.) + औपधिकम् (acc.) + वा (or).",
            "Final म् + vowel: म joins the vowel."),
        mcq("apply", 4, "In unit 118, which word describes the one produced?",
            ("चंडम्, in the accusative", "The results stand in the accusative: a fierce one."),
            [("अमर्षणा, in the nominative", "The nominative names the woman, not the child."),
             ("वा, the closing particle", "वा only means or."),
             ("जनयति, the printed verb", "The verb is not printed here; it is carried from unit 114.")],
            "Nominative = the woman; accusative = the one produced.",
            "acc. = the one produced."),
        mcq("transfer", 5, "By the print habit of चंडम् (read चण्डम्), how is a printed दंड read?",
            ("दण्ड", "Anusvāra before ड stands for ण्, the nasal of its class."),
            [("दन्ड", "न् is the nasal of त-class, not of ड."),
             ("दम्ड", "म् is the nasal of प-class, not of ड."),
             ("दङ्ड", "ङ् is the nasal of क-class, not of ड.")],
            "चंड = चण्ड; so दंड = दण्ड.",
            "ं before ट-class = ण्.",
            teaches="Before a stop, the printed anusvāra stands for that stop's own nasal: ं before ड = ण्."),
    ],
}

# ---------------------------------------------------------------- unit 119
AUTHORED["119"] = {
    "title": "स्वप्नशीला निद्रालुम्",
    "question": "By unit 119, what may a woman given to sleep, and one given to madya, produce?",
    "rule": ("Given to sleep (svapnaśīlā): a drowsy, foolish, or weak-digestion (alpāgni) one. Constantly given to madya "
             "(an intoxicating drink): one prone to thirst, of poor memory, or unsteady."),
    "limits": ("स्वप्न is taken as sleep (it can also mean dream), and तृष्णालु as prone to thirst (it can also mean craving); "
               "no question rests on these alternatives. The verb comes from unit 114. Two printed lines."),
    "explain_hi": ("यह इकाई दो छपी पंक्तियाँ जोड़ती है। सोने के स्वभाव वाली (स्वप्नशीला) माता से: उनींदी, नासमझ, या अल्प अग्नि यानी मन्द पाचन "
                   "वाली सन्तान। मद्य यानी मादक पेय में नित्य लगी रहने वाली से: प्यास की प्रवृत्ति वाली, अल्प स्मृति वाली या अस्थिर सन्तान। "
                   "‘अल्पाग्नि’ में अल्प + अग्नि (अ + अ → आ), ‘अनवस्थित’ में अन् + अवस्थित (स्थिर नहीं) है। "
                   "क्रिया ‘जनयति’ इकाई ११४ से आती है।"),

    "hook": "नींद से उनींदापन; मद्य से स्मृति कम।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 119, which result may a woman given to sleep (svapnaśīlā) produce?",
            ("A drowsy one", "स्वप्नशीला निद्रालुम्: a drowsy one."),
            [("A hostile one", "The hostile one is a result in unit 117."),
             ("A fierce one", "The fierce one is the result of unit 118."),
             ("A bald one", "Baldness is a result in unit 123.")],
            "Given to sleep → drowsy, foolish, or weak in digestion.",
            "स्वप्नशीला → निद्रालु, अबुध, अल्पाग्नि."),
        match(1, "Match each word of unit 119 to its meaning on the card.",
              [["निद्रालु", "drowsy, sleepy"], ["अबुध", "foolish"], ["अल्पाग्नि", "weak digestive fire"],
               ["अल्पस्मृति", "of poor memory"], ["अनवस्थित", "unsteady"]],
              "Three results of line 1 and two of line 2.",
              "निद्रालु, अबुध, अल्पाग्नि; अल्पस्मृति, अनवस्थित."),
        order(2, "Put the words of line 2 of unit 119 in their printed order.",
              ["मद्यनित्या", "तृष्णालुम्", "अल्पस्मृतिम्", "अनवस्थितं वा"],
              "Given to madya … prone to thirst … of poor memory … or unsteady.",
              "मद्यनित्या → तृष्णालुम् → अल्पस्मृतिम् → अनवस्थितं वा.", role="extend",
              teaches="-नित्या at the end of a compound = constant in, given to: मद्यनित्या = constantly given to madya."),
        mcq("discriminate", 3, "Which split of अल्पाग्निं is right?",
            ("अल्प + अग्निम्", "अ + अ → आ: अल्प + अग्निम् → अल्पाग्निम्."),
            [("अल्पम् + अग्निम्", "म् before अ would give अल्पमग्निम्."),
             ("अल्पः + अग्निम्", "अः before अ would give अल्पोऽग्निम्."),
             ("अल्पा + ग्निम्", "ग्निम् is not a word; the card has अग्नि.")],
            "अल्प (small) + अग्निम् (fire): one with weak digestive fire.",
            "अ + अ → आ."),
        mcq("apply", 4, "In unit 119, which result belongs to the woman given to madya, not to the one given to sleep?",
            ("Poor memory (alpasmṛti)", "अल्पस्मृतिम् stands in line 2, after मद्यनित्या."),
            [("Drowsiness (nidrālu)", "निद्रालुम् is in line 1, after स्वप्नशीला."),
             ("Foolishness (abudha)", "अबुधम् is in line 1, after स्वप्नशीला."),
             ("Weak digestion (alpāgni)", "अल्पाग्निम् is in line 1, after स्वप्नशीला.")],
            "Each result belongs to the habit printed just before it.",
            "Results follow their own habit word."),
        mcq("transfer", 5, "By the pattern of अनवस्थित (अन् + अवस्थित), how is the negative of आदि (beginning) formed?",
            ("अनादि", "Before a vowel the negative is अन्-: अन् + आदि → अनादि."),
            [("अआदि", "Before a vowel अ- takes the form अन्-."),
             ("नादि", "The negative prefix keeps its अ."),
             ("अनेदि", "अन् + आ gives ना, not ने.")],
            "अन् + अवस्थित → अनवस्थित (unsteady); अन् + आदि → अनादि (without beginning).",
            "Negative prefix before a vowel = अन्-.",
            teaches="Before a vowel the negative prefix is अन्-: अन् + अवस्थित → अनवस्थित, not steady."),
    ],
}

# ---------------------------------------------------------------- unit 120
AUTHORED["120"] = {
    "title": "गोधामांसनित्याऽश्मरिणं",
    "question": "By unit 120, what may a woman constantly given to godhā-flesh produce?",
    "rule": ("Constantly given to godhā-flesh (monitor lizard, standard): one with aśmarī (urinary stone, standard), or "
             "one who passes urine slowly (sense not firm)."),
    "limits": ("शनैर्मेहिन् as 'passing urine slowly' is not firm (मेहिन् may mean one with meha, a urinary disorder): no "
               "question rests on its sense. The species of godhā (Varanus bengalensis) is only probable; the card says "
               "monitor lizard. The verb comes from unit 114."),
    "explain_hi": ("गोधा यानी गोह (मानक; जाति Varanus bengalensis सम्भावित) के मांस में नित्य लगी रहने वाली माता से: अश्मरी यानी पथरी "
                   "(मानक) वाली सन्तान, या धीरे मूत्र करने वाली। ‘शनैर्मेहिन्’ का अर्थ पक्का नहीं; ‘मेहिन्’ मेह-रोग वाला भी हो सकता है। "
                   "छपा ऽ दिखाता है: नित्या + अश्मरिणम् (आ + अ → आ)। "
                   "‘शनैर्’ में विसर्ग घोष ‘म’ से पहले र् बना है (ऐ के बाद)। क्रिया इकाई ११४ से।"),

    "hook": "गोह का मांस: पथरी वाली सन्तान।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 120, which result may a woman constantly given to godhā-flesh produce?",
            ("One with aśmarī", "गोधामांसनित्याऽश्मरिणम्: one with aśmarī."),
            [("One with prameha", "Prameha is a result in unit 122."),
             ("A red-eyed one", "Red eyes are a result in unit 121."),
             ("A bald one", "Baldness is a result in unit 123.")],
            "Godhā-flesh → one with urinary stone, or one who (probably) passes urine slowly.",
            "गोधामांसनित्या → अश्मरिन् …"),
        match(1, "Match each word of unit 120 to its meaning on the card.",
              [["गोधा", "monitor lizard (standard)"], ["मांस", "flesh"], ["नित्या", "constant in, given to"],
               ["अश्मरी", "urinary stone (standard)"]],
              "The long first token: what she takes, how often, and the result.",
              "गोधा, मांस, नित्या, अश्मरी."),
        order(2, "Put the parts of unit 120 in their printed order.",
              ["गोधा", "मांस", "नित्या", "अश्मरिणम्", "शनैर्मेहिनं वा"],
              "Godhā … flesh … given to … one with aśmarī … or one who passes urine slowly.",
              "गोधा → मांस → नित्या → अश्मरिणम् → शनैर्मेहिनं वा.", role="extend",
              teaches="In an X-नित्या compound the thing she takes comes first: गोधामांस-नित्या = given to godhā-flesh."),
        mcq("discriminate", 3, "Why is शनैः printed as शनैर् before मेहिनम्?",
            ("Visarga after ऐ becomes र् before a voiced sound", "म is voiced, so शनैः + मेहिनम् → शनैर्मेहिनम्."),
            [("Visarga becomes स् before every म", "स् comes before त or थ, not before म."),
             ("Visarga drops before every म", "Before a voiced consonant such as म the visarga drops only after आ (after अ it gives ओ); here ऐ comes before it."),
             ("The र् belongs to the stem शनैर्", "The word is शनैः; र् comes only from the join.")],
            "After a vowel other than अ or आ, a visarga before a voiced sound becomes र्.",
            "ऐः + voiced sound → ऐर्."),
        multi("apply", 4, "Which two are right about unit 120 by the card?",
              [("The exact species of godhā is stated as certain", "The species is only probable."),
               ("godhā = monitor lizard (standard)", "Right: the card labels it standard."),
               ("aśmarī = urinary stone (standard)", "Right: the card labels it standard."),
               ("शनैर्मेहिन् has one firm sense", "Its sense is not firm: it may also mean one with meha.")],
              [1, 2],
              "Standard: godhā = monitor lizard, aśmarī = urinary stone; not firm: species, शनैर्मेहिन्.",
              "Keep the data's labels: standard, probable, not firm."),
        mcq("transfer", 5, "By the join of शनैर्मेहिनम्, how is शनैः + याति (goes) written when joined?",
            ("शनैर्याति", "ऐः before a voiced sound: visarga → र्."),
            [("शनैस्याति", "स् comes before त or थ, not before य."),
             ("शनैयाति", "After ऐ the visarga does not simply drop before य."),
             ("शनैश्याति", "श् comes before च or छ, not before य.")],
            "शनैः + मेहिनम् → शनैर्मेहिनम्; so शनैः + याति → शनैर्याति.",
            "ऐः + voiced sound → ऐर्.",
            teaches="After a vowel other than अ/आ, a visarga before a voiced sound becomes र्."),
    ],
}

# ---------------------------------------------------------------- unit 121
AUTHORED["121"] = {
    "title": "वराहमांसनित्या रक्ताक्षं",
    "question": "By unit 121, what may a woman constantly given to varāha-flesh produce?",
    "rule": ("Constantly given to varāha-flesh (wild boar or pig, standard): a red-eyed one, a krathana (sense uncertain), "
             "or one with very rough hair."),
    "limits": ("क्रथन is a rare word of uncertain sense, kept untranslated: no question rests on its meaning. The verb "
               "comes from unit 114."),
    "explain_hi": ("वराह यानी सूअर (मानक) के मांस में नित्य लगी रहने वाली माता से: लाल आँखों वाली, ‘क्रथन’, या अत्यन्त कठोर रोमों वाली सन्तान। "
                   "‘क्रथन’ दुर्लभ शब्द है, अर्थ अनिश्चित, इसलिए इसका अनुवाद नहीं किया गया। "
                   "‘रक्ताक्ष’ बहुव्रीहि है: जिसकी आँखें लाल हों। ‘अतिपरुषरोमाणम्’ भी बहुव्रीहि है: जिसके रोम अत्यन्त कठोर हों। "
                   "क्रिया इकाई ११४ से।"),

    "hook": "सूअर का मांस: लाल आँखें, कड़े रोम।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 121, which result may a woman constantly given to varāha-flesh produce?",
            ("A red-eyed (raktākṣa) one", "वराहमांसनित्या रक्ताक्षम्: a red-eyed one."),
            [("One with slow blinking", "Slow blinking is a result in unit 122."),
             ("An epileptic one", "Apasmāra is the result of unit 115."),
             ("A dusky (śyāma) one", "The dusky one is a result in unit 125.")],
            "Varāha-flesh → red-eyed, krathana (uncertain), or very rough-haired.",
            "वराहमांसनित्या → रक्ताक्ष …"),
        order(1, "Put the words of unit 121 in their printed order.",
              ["वराहमांसनित्या", "रक्ताक्षम्", "क्रथनम्", "अतिपरुषरोमाणं वा"],
              "Given to varāha-flesh … red-eyed … krathana … or very rough-haired.",
              "वराहमांसनित्या → रक्ताक्षम् → क्रथनम् → अतिपरुषरोमाणं वा."),
        match(2, "Match each word of unit 121 to its meaning on the card.",
              [["वराह", "wild boar or pig (standard)"], ["रक्त", "red"], ["अक्ष", "eye"], ["परुष", "rough"],
               ["रोमन्", "hair (of the body)"]],
              "The words of the habit and of the two clear results.",
              "वराह, रक्त, अक्ष, परुष, रोमन्.", role="extend",
              teaches="अति- before an adjective = very: अतिपरुष = very rough."),
        mcq("discriminate", 3, "Which English of अतिपरुषरोमाणम् is right?",
            ("One with very rough hair", "अति = very; परुष = rough; रोमन् = hair."),
            [("One with very soft hair", "परुष means rough, not soft."),
             ("One with very rough skin", "रोमन् means hair, not skin."),
             ("One with very little hair", "परुष means rough, not little.")],
            "A bahuvrīhi: one whose hair is very rough.",
            "अति + परुष + रोमन्."),
        mcq("apply", 4, "Which split of रक्ताक्षं is right?",
            ("रक्त + अक्षम्", "अ + अ → आ: रक्त + अक्षम् → रक्ताक्षम्."),
            [("रक्तः + अक्षम्", "अः before अ would give रक्तोऽक्षम्."),
             ("रक्तम् + अक्षम्", "म् before अ would give रक्तमक्षम्."),
             ("रक्ता + क्षम्", "क्षम् is not the card's word; it has अक्ष, eye.")],
            "रक्त (red) + अक्षम् (eye): one whose eyes are red.",
            "अ + अ → आ."),
        mcq("transfer", 5, "Built like रक्ताक्ष (one whose eyes are red), what does दीर्घबाहु mean (दीर्घ long, बाहु arm)?",
            ("One whose arms are long", "A bahuvrīhi names the one who has long arms."),
            [("A long arm, the limb itself", "A bahuvrīhi names the owner, not the limb."),
             ("Something long, and an arm", "The two words are one compound, not a list."),
             ("The arm of a tall man", "दीर्घ describes बाहु; no man is named.")],
            "रक्ताक्ष = one whose eyes are red; दीर्घबाहु = one whose arms are long.",
            "Bahuvrīhi X-Y = one whose Y is X.",
            teaches="A bahuvrīhi names the one who has the thing: रक्ताक्ष = one whose eyes are red."),
    ],
}

# ---------------------------------------------------------------- unit 122
AUTHORED["122"] = {
    "title": "मत्स्यमांसनित्या चिरनिमेषं",
    "question": "By unit 122, what may a woman given to fish-flesh, and one given to the sweet, produce?",
    "rule": ("Constantly given to fish-flesh: one with slow blinking, or a stiff-eyed one. Constantly given to the sweet "
             "(madhura): one with prameha (urinary disorders, diabetes-type probable), a mute, or a very stout one."),
    "limits": ("The printed मधुरा- is possibly a slip for मधुर-; the sense sweet is not in doubt. Prameha as diabetes-type is "
               "probable only. The verb comes from unit 114. Two printed lines; the series of tastes begins here and runs to "
               "unit 125."),
    "explain_hi": ("यह इकाई दो छपी पंक्तियाँ जोड़ती है। मछली के मांस में नित्य लगी रहने वाली माता से: देर से पलक झपकाने वाली (चिरनिमेष) या "
                   "जड़ आँखों वाली (स्तब्धाक्ष) सन्तान। मधुर यानी मीठे में नित्य लगी रहने वाली से: प्रमेह (मूत्र-व्याधियों का वर्ग, मधुमेह-प्रकार "
                   "सम्भावित) वाली, गूँगी या अत्यन्त स्थूल सन्तान। "
                   "छपा ‘मधुरा-’ सम्भवतः ‘मधुर-’ की छपाई-भूल है। यहीं से रसों की शृंखला शुरू होती है। क्रिया इकाई ११४ से।"),

    "hook": "मछली से जड़ आँखें; मीठे से प्रमेह और स्थूलता।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 122, which result may a woman constantly given to the sweet (madhura) produce?",
            ("A very stout one", "मधुरानित्या … अतिस्थूलम्: a very stout one."),
            [("A bald (khalatika) one", "Baldness belongs to the salty, in unit 123."),
             ("A weak one", "Weakness belongs to the bitter and pungent, in unit 124."),
             ("A dusky one", "The dusky one belongs to the astringent, in unit 125.")],
            "Sweet → one with prameha, a mute, or a very stout one.",
            "मधुरनित्या → प्रमेहिन्, मूक, अतिस्थूल."),
        match(1, "Match each word of unit 122 to its meaning on the card.",
              [["चिरनिमेष", "slow in blinking"], ["स्तब्धाक्ष", "stiff-eyed"],
               ["प्रमेह", "urinary disorders (diabetes-type probable)"], ["मूक", "mute"], ["अतिस्थूल", "very stout"]],
              "Two results of fish-flesh and three of the sweet.",
              "चिरनिमेष, स्तब्धाक्ष; प्रमेह, मूक, अतिस्थूल."),
        order(2, "Put the words of line 2 of unit 122 in their printed order.",
              ["मधुरानित्या", "प्रमेहिणम्", "मूकम्", "अतिस्थूलं वा"],
              "Given to the sweet … one with prameha … mute … or very stout.",
              "मधुरानित्या → प्रमेहिणम् → मूकम् → अतिस्थूलं वा.", role="extend",
              teaches="A taste can be the habit too: मधुर-नित्या = constantly given to the sweet taste."),
        mcq("discriminate", 3, "Which result in unit 122 belongs to fish-flesh, not to the sweet?",
            ("Stiff eyes (stabdhākṣa)", "स्तब्धाक्षम् stands in line 1, after मत्स्यमांसनित्या."),
            [("Prameha (pramehin)", "प्रमेहिणम् is in line 2, after मधुरानित्या."),
             ("Being mute (mūka)", "मूकम् is in line 2, after मधुरानित्या."),
             ("Being very stout", "अतिस्थूलम् is in line 2, after मधुरानित्या.")],
            "Fish-flesh → slow blinking or stiff eyes; sweet → prameha, mute, very stout.",
            "Results follow their own habit word."),
        multi("apply", 4, "Which two are right about unit 122 by the card?",
              [("चिरनिमेष = slow in blinking (literally long wink)", "Right: so the card explains it."),
               ("Prameha is certainly diabetes", "Diabetes-type is only probable; prameha is a group of urinary disorders."),
               ("Fish-flesh and the sweet have the same results", "Their results differ: eyes for fish, prameha etc. for sweet."),
               ("The printed मधुरा- may be a slip for मधुर-", "Right: the card flags the long आ as a possible print slip.")],
              [0, 3],
              "Slow blinking is literal; the मधुरा- spelling is a possible slip; prameha's modern name is probable.",
              "Keep the data's labels."),
        mcq("transfer", 5, "By the join of स्तब्धाक्षम् (स्तब्ध + अक्षम्), how is मृग + अक्षी (doe-eyed) written?",
            ("मृगाक्षी", "अ + अ → आ, as in स्तब्ध + अक्षम् → स्तब्धाक्षम्."),
            [("मृगक्षी", "The second अ cannot simply vanish; अ + अ gives आ."),
             ("मृगोक्षी", "अ + अ does not give ओ."),
             ("मृगैक्षी", "अ + अ does not give ऐ.")],
            "स्तब्ध + अक्षम् → स्तब्धाक्षम्; so मृग + अक्षी → मृगाक्षी.",
            "अ + अ → आ.",
            teaches="Two short अ across a join merge into one long आ: स्तब्ध + अक्ष → स्तब्धाक्ष."),
    ],
}

# ---------------------------------------------------------------- unit 123
AUTHORED["123"] = {
    "title": "अम्लनित्या रक्तपित्तिनं",
    "question": "By unit 123, what may a woman given to the sour, and one given to the salty, produce?",
    "rule": ("Constantly given to the sour (amla): one with raktapitta (a bleeding disorder, probable) or with diseases of "
             "skin and eyes. Given to the salty (lavaṇa): one with early wrinkles (valī) and greying (palita), or a bald one."),
    "limits": ("raktapitta as a bleeding disorder is probable only. The printed बली is वली (wrinkle; v/b spelling). The verb "
               "comes from unit 114. Two printed lines."),
    "explain_hi": ("अम्ल यानी खट्टे में नित्य लगी रहने वाली माता से: रक्तपित्त (सम्भवतः रक्तस्राव की व्याधि) वाली, या त्वचा और आँखों के रोग वाली "
                   "सन्तान। लवण यानी नमकीन में नित्य लगी रहने वाली से: शीघ्र झुर्रियों (वली) और पलित (बाल पकना) वाली, या गंजी (खलतिक) सन्तान। "
                   "छपा ‘बली’ = वली (व/ब का अदल-बदल)। "
                   "‘त्वगक्षि’ में त्वक् + अक्षि: स्वर से पहले क् → ग्। क्रिया इकाई ११४ से।"),

    "hook": "खट्टे से रक्तपित्त; नमक से जल्दी झुर्री, सफ़ेदी, गंजापन।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 123, which result may a woman constantly given to the salty (lavaṇa) produce?",
            ("A bald one", "लवणनित्या … खलतिकम्: a bald one."),
            [("A mute one", "The mute one belongs to the sweet, in unit 122."),
             ("A dusky one", "The dusky one belongs to the astringent, in unit 125."),
             ("A short-lived one", "Short life belongs to grief, in unit 116.")],
            "Salty → early wrinkles and greying, or baldness.",
            "लवणनित्या → शीघ्रवलीपलित, खलतिक."),
        match(1, "Match each word of unit 123 to its meaning on the card.",
              [["अम्ल", "sour"], ["लवण", "salty"], ["त्वक्", "skin"], ["अक्षि", "eye"], ["पलित", "grey hair"],
               ["खलतिक", "bald"]],
              "The two tastes and four words of their results.",
              "अम्ल, लवण; त्वक्, अक्षि, पलित, खलतिक."),
        order(2, "Put these words of unit 123 in their printed order.",
              ["अम्लनित्या", "रक्तपित्तिनम्", "त्वगक्षिरोगिणं वा", "लवणनित्या", "शीघ्रबलीपलितम्", "खलतिकं वा"],
              "Sour … raktapitta … skin-and-eye disease, or; salty … early wrinkles and greying … bald, or.",
              "अम्लनित्या → रक्तपित्तिनम् → त्वगक्षिरोगिणं वा → लवणनित्या → शीघ्रबलीपलितम् → खलतिकं वा.", role="extend",
              teaches="Two taste-pairs: each taste (nominative) is followed by its own results (accusative), closed by वा."),
        mcq("discriminate", 3, "Which split of त्वगक्षिरोगिणं is right?",
            ("त्वक् + अक्षि + रोगिणम्", "क् becomes ग् before a vowel: त्वक् + अक्षि → त्वगक्षि."),
            [("त्वग + अक्षि + रोगिणम्", "अ + अ would give त्वगाक्षि, with a long आ."),
             ("त्वगः + अक्षि + रोगिणम्", "अः + अ would give त्वगोऽक्षि, with ओ."),
             ("त्वगा + क्षि + रोगिणम्", "क्षि is not a word; the card has अक्षि, eye.")],
            "त्वक् (skin) + अक्षि (eye) + रोगिणम् (one with disease).",
            "क् + vowel → ग् + vowel."),
        mcq("apply", 4, "Which English of शीघ्रबलीपलितं खलतिकं वा is right?",
            ("One with early wrinkles and greying, or a bald (one)", "शीघ्र = early; बली = वली, wrinkle; पलित = greying."),
            [("One with late wrinkles and greying, or a bald (one)", "शीघ्र means early, quick, not late."),
             ("One with early strength and greying, or a bald (one)", "बली here is वली, wrinkle, not बल, strength."),
             ("One with early wrinkles and greying, and long hair", "खलतिक means bald, not long-haired.")],
            "The salty taste: early wrinkles and greying, or baldness.",
            "शीघ्र-वली-पलित; खलतिक."),
        mcq("transfer", 5, "By the join of त्वगक्षि (त्वक् + अक्षि), how is वाक् + ईश (lord) written as one word?",
            ("वागीश", "क् becomes ग् before a vowel: वाक् + ईश → वागीश."),
            [("वाकीश", "Before a vowel क् becomes ग्; it does not stay क्."),
             ("वाङ्गीश", "No nasal is added in this join."),
             ("वागेश", "ग् + ई stays गी; ई does not turn into ए.")],
            "त्वक् + अक्षि → त्वगक्षि; so वाक् + ईश → वागीश.",
            "क् + vowel → ग्.",
            teaches="A final क् before a vowel becomes ग्: त्वक् + अक्षि → त्वगक्षि."),
    ],
}

# ---------------------------------------------------------------- unit 124
AUTHORED["124"] = {
    "title": "तिक्तनित्या शोषिणम्",
    "question": "By unit 124, what may a woman given to the bitter, and one given to the pungent, produce?",
    "rule": ("Constantly given to the bitter (tikta): one with śoṣa (a wasting disease, consumption-type probable), a weak or "
             "a wasted one. Given to the pungent (kaṭuka): a weak one, one with little śukra (semen), or one without offspring."),
    "limits": ("śoṣa as consumption-type is probable only. The printed दुर्वलम् is a spelling variant of दुर्बलम् (weak). "
               "The verb comes from unit 114. Two printed lines."),
    "explain_hi": ("तिक्त यानी कड़वे में नित्य लगी रहने वाली माता से: शोष (सूखने वाली व्याधि, क्षय-प्रकार सम्भावित) वाली, दुर्बल (अबल) या क्षीण "
                   "(अपचित, इकाई ११६ जैसा) सन्तान। कटुक यानी तीखे में नित्य लगी रहने वाली से: दुर्बल, अल्प शुक्र (वीर्य) वाली, या अनपत्य (सन्तानहीन) सन्तान। "
                   "दोनों रसों में ‘कमज़ोर’ आता है: पहले ‘अबलम्’, फिर ‘दुर्वलम्’ (= दुर्बलम्)। "
                   "‘अनपत्य’ में अन् + अपत्य है: जिसकी सन्तान न हो। क्रिया इकाई ११४ से।"),

    "hook": "कड़वे से शोष; तीखे से अल्प शुक्र, सन्तानहीनता।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 124, which result may a woman constantly given to the pungent (kaṭuka) produce?",
            ("One without offspring", "कटुकनित्या … अनपत्यम्: one without offspring."),
            [("One with very rough hair", "Very rough hair belongs to varāha-flesh, in unit 121."),
             ("A bald one", "Baldness belongs to the salty, in unit 123."),
             ("A mute one", "The mute one belongs to the sweet, in unit 122.")],
            "Pungent → a weak one, one with little śukra, or one without offspring.",
            "कटुकनित्या → दुर्बल, अल्पशुक्र, अनपत्य."),
        match(1, "Match each word of unit 124 to its meaning on the card.",
              [["तिक्त", "bitter"], ["कटुक", "pungent"], ["अबल", "weak"], ["अल्पशुक्र", "with little śukra (semen)"],
               ["अनपत्य", "without offspring"]],
              "Two tastes and three results.",
              "तिक्त, कटुक; अबल, अल्पशुक्र, अनपत्य."),
        order(2, "Put the words of line 1 of unit 124 in their printed order.",
              ["तिक्तनित्या", "शोषिणम्", "अबलम्", "अपचितं वा"],
              "Given to the bitter … one with śoṣa … weak … or wasted.",
              "तिक्तनित्या → शोषिणम् → अबलम् → अपचितं वा.", role="extend",
              teaches="-इन् after a disease name = one who has it: शोषिन् = one with śoṣa."),
        mcq("discriminate", 3, "Which result in unit 124 belongs to the bitter, not to the pungent?",
            ("Śoṣa, a wasting disease", "शोषिणम् stands in line 1, after तिक्तनित्या."),
            [("Little śukra (semen)", "अल्पशुक्रम् is in line 2, after कटुकनित्या."),
             ("Being without offspring", "अनपत्यम् is in line 2, after कटुकनित्या."),
             ("Being very stout", "Stoutness belongs to the sweet, in unit 122.")],
            "Bitter → śoṣa, weak, wasted; pungent → weak, little śukra, no offspring.",
            "Results follow their own habit word."),
        multi("apply", 4, "Both tastes of unit 124 lead to a weak one. Which two words say weak?",
              [("अनपत्यम्", "This means without offspring."),
               ("अल्पशुक्रम्", "This means with little śukra (semen)."),
               ("अबलम्", "Right: अ + बल, without strength, after the bitter."),
               ("दुर्वलम् (= दुर्बलम्)", "Right: weak, after the pungent; printed with व for ब.")],
              [2, 3],
              "अबलम् (bitter) and दुर्वलम् = दुर्बलम् (pungent) both mean weak.",
              "अबल and दुर्बल = weak."),
        mcq("transfer", 5, "By the pattern of अबल (अ + बल, strength), what does अभय mean (भय = fear)?",
            ("Without fear, fearless", "अ- before a consonant = without: अभय = fearless."),
            [("Full of fear", "अ- denies; it does not fill."),
             ("A great fear", "अ- does not mean great."),
             ("Fear of the weak", "अभय is one word: without fear.")],
            "अ + बल → अबल (without strength); अ + भय → अभय (without fear).",
            "अ- before a consonant = without, not.",
            teaches="अ- before a consonant negates: अबल = without strength, weak."),
    ],
}

# ---------------------------------------------------------------- unit 125
AUTHORED["125"] = {
    "title": "कषायनित्या श्यामम्",
    "question": "By unit 125, what may a woman constantly given to the astringent produce?",
    "rule": ("Constantly given to the astringent (kaṣāya): a dusky one, one with ānāha (distension of the belly with "
             "retention, standard), or one with udāvarta (upward course of Vāta, standard)."),
    "limits": ("कषाय here is the taste (astringent), not a decoction. The verb comes from unit 114. Nothing is said on cure."),
    "explain_hi": ("कषाय यानी कसैले रस में नित्य लगी रहने वाली माता से: श्याम (साँवली) सन्तान, आनाह (पेट फूलना और मल-वात रुकना, मानक) वाली, "
                   "या उदावर्त (वात का उलटा, ऊपर की ओर चलना, मानक) वाली। "
                   "यहाँ ‘कषाय’ रस है, काढ़ा नहीं। "
                   "छपा जुड़ा शब्द = श्यामम् + आनाहिनम् + उदावर्तिनम्। ‘-इन्’ का अर्थ है: वह रोग जिसे हो। क्रिया इकाई ११४ से।"),

    "hook": "कसैले से साँवलापन, आनाह, उदावर्त।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 125, which result may a woman constantly given to the astringent (kaṣāya) produce?",
            ("One with udāvarta", "कषायनित्या … उदावर्तिनम्: one with udāvarta."),
            [("One with prameha", "Prameha belongs to the sweet, in unit 122."),
             ("One with raktapitta", "Raktapitta belongs to the sour, in unit 123."),
             ("One with aśmarī", "Aśmarī belongs to godhā-flesh, in unit 120.")],
            "Astringent → a dusky one, one with ānāha, or one with udāvarta.",
            "कषायनित्या → श्याम, आनाहिन्, उदावर्तिन्."),
        order(1, "Put the words of unit 125 in their printed order.",
              ["कषायनित्या", "श्यामम्", "आनाहिनम्", "उदावर्तिनं वा"],
              "Given to the astringent … dusky … one with ānāha … or one with udāvarta.",
              "कषायनित्या → श्यामम् → आनाहिनम् → उदावर्तिनं वा."),
        match(2, "Match each word of unit 125 to its meaning on the card.",
              [["कषाय", "astringent (the taste)"], ["श्याम", "dusky, dark"],
               ["आनाह", "belly distension with retention"], ["उदावर्त", "upward course of Vāta"]],
              "The taste and its three results.",
              "कषाय, श्याम, आनाह, उदावर्त.", role="extend",
              teaches="कषाय in a list of tastes = the astringent taste, not a decoction: कषायनित्या = constantly given to the astringent."),
        mcq("discriminate", 3, "In unit 125, what does कषाय mean?",
            ("The astringent taste", "The card says कषाय here is the taste."),
            [("A decoction to drink", "The card says it is the taste here, not a decoction."),
             ("The sweet taste", "The sweet (मधुर) is in unit 122."),
             ("The pungent taste", "The pungent (कटुक) is in unit 124.")],
            "कषायनित्या = constantly given to the astringent taste.",
            "कषाय = astringent (taste)."),
        mcq("apply", 4, "Which split of श्याममानाहिनम् is right?",
            ("श्यामम् + आनाहिनम्", "म् joins the next vowel आ: श्याममानाहिनम्."),
            [("श्याम + मानाहिनम्", "मानाहिन् is not a word; the card has आनाहिन्."),
             ("श्यामा + आनाहिनम्", "आ + आ would give श्यामानाहिनम्, with no second म."),
             ("श्यामम् + अनाहिनम्", "That would join as श्याममनाहिनम्, with a short अ.")],
            "श्यामम् (dusky, acc.) + आनाहिनम् (one with ānāha, acc.).",
            "Final म् + vowel: म joins the vowel."),
        mcq("transfer", 5, "By the pattern of आनाहिन् (one with ānāha), what does ज्वरिन् mean (ज्वर = fever)?",
            ("One who has fever", "-इन् = one who has X: one with fever."),
            [("Fever itself, the disease", "-इन् names the person who has it, not the disease."),
             ("One who cures fever", "-इन् means having, not curing."),
             ("One who is free of fever", "-इन् means having, not being free.")],
            "आनाहिन् = one with ānāha; ज्वरिन् = one with fever.",
            "X-इन् = one who has X.",
            teaches="-इन् after a disease name = one who has it: आनाहिन्, उदावर्तिन्."),
    ],
}

# ===================================================================== NOTES_HI
NOTES_HI = {
    "114": ("विश्वास उच्च, कोई पाठ-चिह्न नहीं; गद्य, एक छपी पंक्ति (02.02.117)। कर्ता प्रथमा: विवृतशया, नक्तचारिणी; वे गर्भिणी हैं, यह प्रसंग से। "
            "एक स्त्री में दोनों स्वभाव या एक ही काफ़ी, यह शब्दों से तय नहीं (क्रिया एकवचन)। ‘विवृत’ = बिना ढके, या खुले में। "
            "उन्मत्त = उन्माद वाला (मानक)। ‘जनयति’ आगे इकाई ११५ से १२५ तक भी लगती है। "
            "सन्धियाँ जाँचीं: च + उन्मत्तम् → चोन्मत्तम् (अ + उ → ओ); उन्मत्तम् + जनयति → उन्मत्तं जनयति (अन्त्य म् → अनुस्वार)।"),
    "115": ("विश्वास उच्च, कोई पाठ-चिह्न नहीं; गद्य (02.02.118)। क्रिया ‘जनयति’ इकाई ११४ से, छपी नहीं; सन्तान का संज्ञा-शब्द अनकहा। "
            "अपस्मार = मिर्गी (मानक)। सन्धि जाँची: कलहशीला + अपस्मारिणम् → कलहशीलाऽपस्मारिणम् (आ + अ → आ); छपा ऽ छपाई की आदत है।"),
    "116": ("विश्वास मध्यम; गद्य, दो छपी पंक्तियाँ (02.02.119, 02.02.120)। पाठ-चिह्न: (१) छपा ‘अन्हीकं’ ज्ञात शब्द नहीं; ‘अह्रीकम्’ "
            "(निर्लज्ज) अनुमानित पाठ है, इस पर कोई प्रश्न नहीं। (२) छपा ‘शॉकनित्या’ में ॉ भटका चिह्न है; ‘शोकनित्या’ लगभग निश्चित। "
            "‘स्त्रैण’ = स्त्रैण, जनाना (स्त्री-प्रिय भी हो सकता है); ‘अपचित’ = क्षीण (‘सम्मानित’ भी अर्थ है; यही शब्द इकाई १२४ में)। "
            "क्रिया इकाई ११४ से। सन्धियाँ जाँचीं: भीरुम् + अपचितम् → भीरुमपचितम्; अपचितम् + अल्पायुषम् → अपचितमल्पायुषम्; "
            "अल्प + आयुषम् → अल्पायुषम् (अ + आ → आ); स्त्रैणम् + वा → स्त्रैणं वा।"),
    "117": ("विश्वास मध्यम, कोई पाठ-चिह्न नहीं; गद्य, दो छपी पंक्तियाँ (02.02.121, 02.02.122)। दूसरी पंक्ति एक लम्बा जुड़ा शब्द है; "
            "‘स्तेना तु आयासबहुलम् अभिद्रोहिणम् अकर्मशीलम्’ विभाजन सम्भावित है, पक्का नहीं (‘तु’ अटपटा तत्त्व है)। "
            "‘अकर्मशील’ = अकर्मण्य, या बुरे कर्म वाला भी हो सकता है। क्रिया इकाई ११४ से। "
            "सन्धियाँ जाँचीं: पर + उपतापनम् → परोपतापनम् (अ + उ → ओ); परोपतापनम् + ईर्ष्यालुम् → परोपतापनमीर्ष्यालुम्।"),
    "118": ("विश्वास मध्यम, कोई पाठ-चिह्न नहीं; गद्य (02.02.123)। ‘औपधिक’ = कपटी (उपधि = छल) सम्भावित; इसके दूसरे अर्थ भी हैं "
            "(जैसे अतिरिक्त)। छपाई में ‘वा’ पिछले शब्द से जुड़ा (औपधिकंवा): दूरी की भूल, बिना चिह्न के अलग किया। "
            "छपा ‘चंड’ = चण्ड (ड से पहले अनुस्वार = ण्)। सन्धि जाँची: चण्डम् + औपधिकम् → चण्डमौपधिकम्। क्रिया इकाई ११४ से।"),
    "119": ("विश्वास उच्च, कोई पाठ-चिह्न नहीं; गद्य, दो छपी पंक्तियाँ (02.02.124, 02.02.125)। ‘स्वप्न’ = नींद (स्वप्न भी हो सकता है); "
            "‘तृष्णालु’ = प्यास की प्रवृत्ति (तृष्णा, लालसा भी हो सकता है)। अल्पाग्नि = मन्द पाचन-अग्नि (मानक)। क्रिया इकाई ११४ से। "
            "सन्धियाँ जाँचीं: निद्रालुम् + अबुधम् → निद्रालुमबुधम्; अल्प + अग्निम् → अल्पाग्निम्; अल्पस्मृतिम् + अनवस्थितम् → "
            "अल्पस्मृतिमनवस्थितम्; अन् + अवस्थित → अनवस्थित।"),
    "120": ("विश्वास मध्यम, कोई पाठ-चिह्न नहीं; गद्य (02.02.126)। गोधा = गोह (मानक), जाति Varanus bengalensis सम्भावित। "
            "अश्मरी = मूत्र की पथरी (मानक)। ‘शनैर्मेहिन्’ = धीरे-धीरे मूत्र करने वाला, पर ‘मेहिन्’ = मेह-रोग वाला भी हो सकता है: अर्थ पक्का नहीं। "
            "सन्धियाँ जाँचीं: नित्या + अश्मरिणम् → नित्याऽश्मरिणम् (आ + अ → आ, ऽ छपा); शनैः + मेहिनम् → शनैर्मेहिनम् "
            "(ऐ के बाद विसर्ग घोष से पहले र्)। क्रिया इकाई ११४ से।"),
    "121": ("विश्वास मध्यम, कोई पाठ-चिह्न नहीं; गद्य (02.02.127)। ‘क्रथन’ दुर्लभ शब्द, अर्थ अनिश्चित (सम्भवतः √क्रथ् ‘चोट पहुँचाना’ से, "
            "या ध्वनि-शब्द); अनुवाद के बिना रखा गया, कोई प्रश्न नहीं। वराह = जंगली सूअर या सूअर (मानक)। अन्तिम शब्द ‘-रोमन्’ का बहुव्रीहि "
            "(द्वितीया: -रोमाणम्)। सन्धियाँ जाँचीं: रक्त + अक्षम् → रक्ताक्षम्; क्रथनम् + अतिपरुषरोमाणम् → क्रथनमतिपरुषरोमाणम्। क्रिया इकाई ११४ से।"),
    "122": ("विश्वास मध्यम; गद्य, दो छपी पंक्तियाँ (02.02.128, 02.02.129)। पाठ-चिह्न: छपा ‘मधुरानित्या’ का लम्बा आ सम्भवतः छपाई-भूल "
            "(आगे के अम्लनित्या, लवणनित्या आदि शुद्ध प्रातिपदिक रखते हैं)। छपाई में ‘मूकमतिस्थूलंवा’ में वा जुड़ा। "
            "प्रमेह = मूत्र-व्याधियों का वर्ग, मधुमेह-प्रकार सम्भावित। ‘चिरनिमेष’ = देर से पलक झपकाना (शाब्दिक: लम्बी झपक)। "
            "सन्धियाँ जाँचीं: स्तब्ध + अक्षम् → स्तब्धाक्षम्; मूकम् + अतिस्थूलम् → मूकमतिस्थूलम्। क्रिया इकाई ११४ से।"),
    "123": ("विश्वास उच्च, कोई पाठ-चिह्न नहीं; गद्य, दो छपी पंक्तियाँ (02.02.130, 02.02.131)। रक्तपित्त = शरीर के छिद्रों से रक्तस्राव, "
            "आधुनिक अर्थ सम्भावित। छपा ‘बली’ = वली (व/ब का अदल-बदल, सामान्य किया गया)। खलतिक = गंजा (मानक)। "
            "सन्धियाँ जाँचीं: त्वक् + अक्षि → त्वगक्षि (स्वर से पहले क् → ग्); रक्तपित्तिनम् + त्वगक्षिरोगिणम् → रक्तपित्तिनं त्वगक्षिरोगिणम्। "
            "क्रिया इकाई ११४ से।"),
    "124": ("विश्वास उच्च, कोई पाठ-चिह्न नहीं; गद्य, दो छपी पंक्तियाँ (02.02.132, 02.02.133)। शोष = सूखना, क्षीण होना; क्षय-प्रकार सम्भावित। "
            "‘अपचित’ इकाई ११६ जैसा (क्षीण)। छपा ‘दुर्वलम्’ = दुर्बलम् (मान्य वर्तनी-भेद, कोई चिह्न नहीं)। शुक्र = वीर्य (मानक)। "
            "सन्धियाँ जाँचीं: शोषिणम् + अबलम् → शोषिणमबलम्; अबलम् + अपचितम् → अबलमपचितम्; अल्पशुक्रम् + अनपत्यम् → "
            "अल्पशुक्रमनपत्यम्; अन् + अपत्य → अनपत्य। क्रिया इकाई ११४ से।"),
    "125": ("विश्वास उच्च, कोई पाठ-चिह्न नहीं; गद्य (02.02.134)। ‘कषाय’ यहाँ रस (कसैला) है, काढ़ा नहीं। आनाह = पेट फूलना और मल-वात का "
            "रुकना (मानक); उदावर्त = वात का उलटा, ऊपर चलना (मानक)। छपा जुड़ा शब्द = श्यामम् + आनाहिनम् + उदावर्तिनम्। "
            "सन्धियाँ जाँचीं: श्यामम् + आनाहिनम् → श्याममानाहिनम्; आनाहिनम् + उदावर्तिनम् → आनाहिनमुदावर्तिनम्। क्रिया इकाई ११४ से।"),
}

# ===================================================================== AIDS
AIDS = {
    "114": {
        "diagram": {"groups": [
            {"label": "माता के स्वभाव (प्रथमा)", "items": ["विवृतशया (बिना ढके सोने वाली)", "नक्तचारिणी (रात में घूमने वाली)"]},
            {"label": "सन्तान (द्वितीया)", "items": ["उन्मत्तम् (पागल)"]},
            {"label": "क्रिया", "items": ["जनयति (उत्पन्न करती है; आगे १२५ तक)"]}]},
        "sandhi": "अ + उ → ओ: च + उन्मत्तम् → चोन्मत्तम् · अन्त्य म् → अनुस्वार: उन्मत्तम् + जनयति → उन्मत्तं जनयति।",
        "frame": "स्वभाव (प्रथमा, माता) → परिणाम (द्वितीया, सन्तान) → जनयति। यही ढाँचा इकाई १२५ तक चलता है।",
        "chunks": "विवृतशया | नक्तचारिणी | चोन्मत्तं | जनयति",
    },
    "115": {
        "frame": "कलहशीला (झगड़ालू माता) → अपस्मारिणम् (अपस्मार वाली सन्तान) → (जनयति, इकाई ११४ से)।",
        "sandhi": "आ + अ → आ, छपा ऽ: कलहशीला + अपस्मारिणम् → कलहशीलाऽपस्मारिणम्।",
        "puns": "मेरी बनाई, केवल सुनने की सहायता: ‘कलह’ की कड़क से ‘अपस्मार’ का झटका याद रखें।",
    },
    "116": {
        "diagram": {"groups": [
            {"label": "व्यवायशीला", "items": ["दुर्वपुष (बुरे शरीर वाला)", "अह्रीक (निर्लज्ज, अनुमानित पाठ)", "स्त्रैण"]},
            {"label": "शोकनित्या (छपा शॉक-)", "items": ["भीरु (डरपोक)", "अपचित (क्षीण)", "अल्पायु"]}]},
        "sandhi": "अ + आ → आ: अल्प + आयुषम् → अल्पायुषम् · विसर्ग → र् (उ के बाद, घोष से पहले): दुः + वपुषम् → दुर्वपुषम्।",
        "contrast": "इसी इकाई के दो स्वभाव: व्यवाय (मैथुन) → बुरा शरीर, स्त्रैणता (और अनुमानित पाठ पर निर्लज्जता) · शोक → डर, क्षीणता, छोटी आयु।",
        "chunks": "व्यवायशीला | दुर्वपुषम् [अन्हीकं: अनुमानित अह्रीकम्] | स्त्रैणं वा || शॉकनित्या | भीरुम् | अपचितम् | अल्पायुषं वा",
    },
    "117": {
        "diagram": {"groups": [
            {"label": "अभिध्यायिनी (लोभ करने वाली)", "items": ["परोपतापन", "ईर्ष्यालु", "स्त्रैण"]},
            {"label": "स्तेना (चोर स्त्री; विभाजन सम्भावित)", "items": ["आयासबहुल", "अभिद्रोही", "अकर्मशील"]}]},
        "sandhi": "अ + उ → ओ: पर + उपतापनम् → परोपतापनम् · म् + स्वर: परोपतापनम् + ईर्ष्यालुम् → परोपतापनमीर्ष्यालुम्।",
        "chunks": "अभिध्यायिनी | परोपतापनम् | ईर्ष्यालुम् | स्त्रैणं वा || स्तेना तु (सम्भावित) | आयासबहुलम् | अभिद्रोहिणम् | अकर्मशीलं वा",
    },
    "118": {
        "frame": "अमर्षणा (असहनशील माता) → चण्डम् (उग्र) या औपधिकम् (सम्भवतः कपटी) → (जनयति, इकाई ११४ से)।",
        "sandhi": "म् + स्वर: चण्डम् + औपधिकम् → चण्डमौपधिकम् · छपा अनुस्वार: चंड = चण्ड (ड से पहले ण्)।",
        "puns": "मेरी बनाई, केवल सुनने की सहायता: ‘अमर्ष’ (सहन नहीं) से ‘चण्ड’ (प्रचण्ड) सन्तान।",
    },
    "119": {
        "diagram": {"groups": [
            {"label": "स्वप्नशीला (सोने के स्वभाव वाली)", "items": ["निद्रालु (उनींदा)", "अबुध (नासमझ)", "अल्पाग्नि (मन्द पाचन)"]},
            {"label": "मद्यनित्या (मद्य में नित्य)", "items": ["तृष्णालु (प्यास वाला)", "अल्पस्मृति", "अनवस्थित (अस्थिर)"]}]},
        "sandhi": "अ + अ → आ: अल्प + अग्निम् → अल्पाग्निम् · अन् + अ: अन् + अवस्थित → अनवस्थित।",
        "chunks": "स्वप्नशीला | निद्रालुम् | अबुधम् | अल्पाग्निं वा || मद्यनित्या | तृष्णालुम् | अल्पस्मृतिम् | अनवस्थितं वा",
        "pegs": "मेरी बनाई याद-जोड़ी: नींद → नींद ही (उनींदा); मद्य → स्मृति कम।",
    },
    "120": {
        "frame": "गोधा-मांस-नित्या (गोह के मांस में नित्य) → अश्मरिणम् (पथरी वाला) या शनैर्मेहिनम् (धीरे मूत्र करने वाला, अर्थ पक्का नहीं)।",
        "sandhi": "आ + अ → आ, छपा ऽ: नित्या + अश्मरिणम् → नित्याऽश्मरिणम् · ऐः + घोष → ऐर्: शनैः + मेहिनम् → शनैर्मेहिनम्।",
        "chunks": "गोधा | मांस | नित्या | अश्मरिणम् | शनैर्मेहिनं वा",
    },
    "121": {
        "frame": "वराह-मांस-नित्या → रक्ताक्षम् (लाल आँखों वाला), क्रथनम् (अर्थ अनिश्चित), या अतिपरुषरोमाणम् (अत्यन्त कठोर रोमों वाला)।",
        "sandhi": "अ + अ → आ: रक्त + अक्षम् → रक्ताक्षम् · म् + स्वर: क्रथनम् + अति… → क्रथनमति…",
        "chunks": "वराहमांसनित्या | रक्ताक्षम् | क्रथनम् [अर्थ अनिश्चित] | अतिपरुषरोमाणं वा",
    },
    "122": {
        "diagram": {"groups": [
            {"label": "मत्स्यमांसनित्या", "items": ["चिरनिमेष (देर से पलक झपकाना)", "स्तब्धाक्ष (जड़ आँखें)"]},
            {"label": "मधुरानित्या (सम्भवतः मधुरनित्या)", "items": ["प्रमेही (मधुमेह-प्रकार सम्भावित)", "मूक (गूँगा)", "अतिस्थूल"]}]},
        "sandhi": "अ + अ → आ: स्तब्ध + अक्षम् → स्तब्धाक्षम् · म् + स्वर: मूकम् + अतिस्थूलम् → मूकमतिस्थूलम्।",
        "anchors": "मेरी याद-पद्धति: छह रस क्रम से: मधुर (१२२) → अम्ल, लवण (१२३) → तिक्त, कटुक (१२४) → कषाय (१२५)।",
        "chunks": "मत्स्यमांसनित्या | चिरनिमेषम् | स्तब्धाक्षं वा || मधुरानित्या | प्रमेहिणम् | मूकम् | अतिस्थूलं वा",
    },
    "123": {
        "frame": "अम्लनित्या → रक्तपित्ती या त्वक्-अक्षि-रोगी · लवणनित्या → शीघ्र वली-पलित या खलतिक (गंजा)।",
        "sandhi": "क् + स्वर → ग्: त्वक् + अक्षि → त्वगक्षि · छपा ‘बली’ = वली (व/ब)।",
        "contrast": "इसी इकाई के दो रस: अम्ल (खट्टा) → रक्त, त्वचा, आँख · लवण (नमकीन) → झुर्री, बाल पकना, गंजापन।",
        "chunks": "अम्लनित्या | रक्तपित्तिनम् | त्वगक्षिरोगिणं वा || लवणनित्या | शीघ्रबलीपलितम् | खलतिकं वा",
    },
    "124": {
        "diagram": {"groups": [
            {"label": "तिक्तनित्या (कड़वा)", "items": ["शोषी (क्षय-प्रकार सम्भावित)", "अबल (दुर्बल)", "अपचित (क्षीण)"]},
            {"label": "कटुकनित्या (तीखा)", "items": ["दुर्बल (छपा दुर्वल)", "अल्पशुक्र", "अनपत्य (सन्तानहीन)"]}]},
        "sandhi": "म् + स्वर: शोषिणम् + अबलम् → शोषिणमबलम् · अन् + अ: अन् + अपत्य → अनपत्य · अ + ब: अ + बल → अबल।",
        "letters": "दोनों रसों में ‘कमज़ोर’: तिक्त में अ-बल, कटुक में दुर्-बल।",
        "chunks": "तिक्तनित्या | शोषिणम् | अबलम् | अपचितं वा || कटुकनित्या | दुर्वलम् | अल्पशुक्रम् | अनपत्यं वा",
    },
    "125": {
        "diagram": {"groups": [
            {"label": "कषायनित्या (कसैले में नित्य)", "items": ["१ श्यामम् (साँवला)", "२ आनाहिनम् (आनाह वाला)", "३ उदावर्तिनं वा (उदावर्त वाला)"]}]},
        "sandhi": "म् + स्वर: श्यामम् + आनाहिनम् → श्याममानाहिनम् · आनाहिनम् + उदावर्तिनम् → आनाहिनमुदावर्तिनम्।",
        "anchors": "मेरी याद-पद्धति: छह रसों की शृंखला यहाँ पूरी होती है: मधुर, अम्ल, लवण, तिक्त, कटुक, कषाय (इकाई १२२ से १२५)।",
    },
}

# ===================================================================== IMAGE_SPECS
IMAGE_SPECS = {
    ("114", "diagram"): {
        "file": "sh2-unmatta-114.svg",
        "alt": ("Flowchart of unit 114: she who sleeps uncovered (vivritashaya) and she who roams at night (naktacharini) "
                "produce (janayati) a mad (unmatta) child."),
        "type": "mermaid",
        "code": ("flowchart TD\n"
                 "  A[\"विवृतशया: बिना ढके सोने वाली\"] --> D[\"जनयति: उत्पन्न करती है\"]\n"
                 "  B[\"नक्तचारिणी: रात में घूमने वाली\"] --> D\n"
                 "  D --> C[\"उन्मत्त सन्तान\"]\n"),
    },
    ("116", "diagram"): {
        "file": "sh2-vyavaya-shoka-116.svg",
        "alt": ("Two columns for unit 116: given to intercourse (vyavaya): ill-shaped, shameless (conjectural reading), "
                "womanish; given to grief (shoka, printed with a stray sign): timid, wasted, short-lived."),
        "type": "split",
        "title": "इकाई ११६: दो स्वभाव, तीन-तीन परिणाम",
        "cols": [["व्यवायशीला", ["दुर्वपुष: बुरा शरीर", "अह्रीक (अनुमानित पाठ)", "स्त्रैण"]],
                 ["शोकनित्या (छपा शॉक-)", ["भीरु: डरपोक", "अपचित: क्षीण", "अल्पायु"]]],
    },
    ("117", "diagram"): {
        "file": "sh2-abhidhya-stena-117.svg",
        "alt": ("Two columns for unit 117: covetous (abhidhyayini): tormenting others, jealous, womanish; thief (stena, "
                "probable split): abounding in toil, hostile, given to inaction."),
        "type": "split",
        "title": "इकाई ११७: लोभ और चोरी",
        "cols": [["अभिध्यायिनी", ["परोपतापन", "ईर्ष्यालु", "स्त्रैण"]],
                 ["स्तेना (विभाजन सम्भावित)", ["आयासबहुल", "अभिद्रोही", "अकर्मशील"]]],
    },
    ("119", "diagram"): {
        "file": "sh2-svapna-madya-119.svg",
        "alt": ("Two columns for unit 119: given to sleep (svapnashila): drowsy, foolish, weak digestion; given to madya: "
                "prone to thirst, poor memory, unsteady."),
        "type": "split",
        "title": "इकाई ११९: नींद और मद्य",
        "cols": [["स्वप्नशीला", ["निद्रालु: उनींदा", "अबुध: नासमझ", "अल्पाग्नि: मन्द पाचन"]],
                 ["मद्यनित्या", ["तृष्णालु: प्यास वाला", "अल्पस्मृति", "अनवस्थित: अस्थिर"]]],
    },
    ("122", "diagram"): {
        "file": "sh2-matsya-madhura-122.svg",
        "alt": ("Two columns for unit 122: given to fish-flesh: slow blinking, stiff eyes; given to the sweet (madhura): "
                "prameha (diabetes-type probable), mute, very stout."),
        "type": "split",
        "title": "इकाई १२२: मछली और मधुर",
        "cols": [["मत्स्यमांसनित्या", ["चिरनिमेष: देर से झपक", "स्तब्धाक्ष: जड़ आँखें"]],
                 ["मधुरानित्या (सम्भवतः मधुरनित्या)", ["प्रमेही (मधुमेह-प्रकार सम्भावित)", "मूक: गूँगा", "अतिस्थूल"]]],
    },
    ("124", "diagram"): {
        "file": "sh2-tikta-katuka-124.svg",
        "alt": ("Two columns for unit 124 in printed order: bitter (tikta): shosha (consumption-type probable), weak, wasted; "
                "pungent (katuka): weak (printed durvala), little shukra, without offspring."),
        "type": "split",
        "title": "इकाई १२४: तिक्त और कटुक",
        "cols": [["तिक्तनित्या (कड़वा)", ["शोषी (क्षय-प्रकार सम्भावित)", "अबल: दुर्बल", "अपचित: क्षीण"]],
                 ["कटुकनित्या (तीखा)", ["दुर्बल (छपा दुर्वल)", "अल्पशुक्र: कम वीर्य", "अनपत्य: सन्तानहीन"]]],
    },
    ("125", "diagram"): {
        "file": "sh2-kashaya-125.svg",
        "alt": ("Flowchart of unit 125: constantly given to the astringent (kashaya) leads to one of three alternatives, "
                "numbered in printed order: 1 a dusky one; 2 one with anaha; 3 one with udavarta."),
        "type": "mermaid",
        "code": ("flowchart TD\n"
                 "  A[\"कषायनित्या: कसैले में नित्य\"] -->|\"या\"| B[\"१ श्याम: साँवला\"]\n"
                 "  A -->|\"या\"| C[\"२ आनाही: आनाह वाला\"]\n"
                 "  A -->|\"या\"| D[\"३ उदावर्ती: उदावर्त वाला\"]\n"),
    },
}
