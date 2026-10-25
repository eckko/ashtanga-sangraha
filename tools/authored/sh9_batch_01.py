from helpers import mcq, match, order, fill, multi, accepts


def T(q, teaches):
    q["teaches"] = teaches
    return q


AUTHORED = {}

# ---------------------------------------------------------------- unit 1
AUTHORED["1"] = {
    "title": "अथातो विकृतांगविज्ञानीयमध्यायं",
    "question": "By card 1, which chapter does the text now begin, and with what formula?",
    "rule": ("Now, therefore (अथ अतः), we shall expound (व्याख्यास्यामः) the chapter (अध्यायम्) on the knowledge of "
             "abnormal body parts (विकृताङ्गविज्ञानीयम्)."),
    "limits": ("Prose, the standard chapter-opening formula. The title only names the topic; what counts as 'abnormal' "
               "comes in the cards that follow."),
    "explain_hi": ("यह अध्याय-आरम्भ का मानक सूत्र है: ‘अब इसलिए हम विकृताङ्गविज्ञानीय अध्याय की व्याख्या करेंगे’। "
                   "विकृत = बिगड़ा हुआ, अङ्ग = शरीर का भाग, विज्ञान = ज्ञान; यानी शरीर के विकृत अंगों के ज्ञान वाला अध्याय। "
                   "‘व्याख्यास्यामः’ भविष्यत् काल, उत्तम पुरुष बहुवचन है: ‘हम व्याख्या करेंगे’। "
                   "‘अथातो’ में अथ + अतः (अ + अ → आ) और अतः + वि- (घोष व्यंजन से पहले अः → ओ) की सन्धियाँ हैं।"),
    "hook": "अथातो ... व्याख्यास्यामः: नया अध्याय, विकृत अंगों का ज्ञान।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "In the chapter title of card 1, what does विकृत mean?",
            ("Abnormal, changed", "विकृत = changed from the natural state, abnormal."),
            [("Healthy, natural", "That would be प्रकृतिस्थ or स्वस्थ; विकृत is its opposite."),
             ("Hidden, inner", "Hidden would be गूढ; विकृत means changed, abnormal."),
             ("Newly formed", "Newly formed would be नव; विकृत means changed, abnormal.")],
            "विकृत-अङ्ग-विज्ञानीय = on the knowledge of abnormal body parts.",
            "विकृत = abnormal."),
        order(1, "Put the words of card 1 in the printed order.",
              ["अथ", "अतः", "विकृताङ्गविज्ञानीयम्", "अध्यायम्", "व्याख्यास्यामः"],
              "Now; therefore; on the knowledge of abnormal body parts; the chapter; we shall expound.",
              "अथ → अतः → विकृताङ्गविज्ञानीयम् → अध्यायम् → व्याख्यास्यामः."),
        match(2, "Match each word of card 1 to its meaning.",
              [["अथ", "now"], ["अतः", "therefore"], ["अङ्ग", "limb, body part"], ["विज्ञान", "knowledge"],
               ["अध्याय", "chapter"]],
              "अथ = now, अतः = therefore, अङ्ग = body part, विज्ञान = knowledge, अध्याय = chapter.",
              "अथ, अतः, अङ्ग, विज्ञान, अध्याय.", role="extend",
              teaches="A chapter title ending in -ईय means 'concerning ...': विकृताङ्गविज्ञानीय = concerning the knowledge of abnormal body parts."),
        mcq("discriminate", 3, "Which split of अथातो in card 1 is right?",
            ("अथ + अतः", "अ + अ → आ: अथ + अतः → अथातः; then अः → ओ before the voiced व."),
            [("अथा + तः", "अथा and तः are not the words here; the adverbs are अथ and अतः."),
             ("अथ + आतो", "आतो is not a word; the second word is अतः."),
             ("अथात् + ओ", "अथात् is not a word; ओ comes from the visarga of अतः.")],
            "अथ (now) + अतः (therefore).",
            "अ + अ → आ."),
        mcq("apply", 4, "Why is अध्यायम् printed अध्यायं before व्याख्यास्यामः in card 1?",
            ("Final म् before a consonant is written ं", "Inside a sentence a final म् before a consonant becomes anusvāra."),
            [("ं marks the plural of अध्याय", "The form is accusative singular; ं comes only from sandhi."),
             ("म् is dropped before every व", "It is not dropped; it is written as the anusvāra ं."),
             ("ं is the stem's own last letter", "The stem is अध्याय; the ं stands for the ending म्.")],
            "अध्यायम् + व्याख्यास्यामः → अध्यायं व्याख्यास्यामः.",
            "Final म् + consonant → ं."),
        mcq("transfer", 5, "By the pattern of व्याख्यास्यामः (we shall expound), what does वक्ष्यामः mean in a new example?",
            ("We shall speak", "-स्यामः / -ष्यामः is the future, first person plural: वच् → वक्ष्यामः, we shall speak."),
            [("We have spoken", "A past would need another form; -ष्यामः is the future."),
             ("They will speak", "'They will speak' would be वक्ष्यन्ति; -आमः is 'we'."),
             ("We are speaking", "The present would be वदामः; -ष्यामः is the future.")],
            "वक्ष्यामः = we shall speak, like व्याख्यास्यामः = we shall expound.",
            "-स्यामः / -ष्यामः = we shall ...",
            teaches="The ending -स्यामः (after some roots -ष्यामः) makes the future, 'we shall': व्याख्यास्यामः = we shall expound."),
    ],
}

# ---------------------------------------------------------------- unit 2
AUTHORED["2"] = {
    "title": "दोषा घनाघना इव",
    "question": "By card 2, what do the doṣas that are beyond medicine do, and what are they compared to?",
    "rule": ("Doṣas gone beyond the range of medicine and pervading the whole body, in men desiring another body, "
             "indicate the decay of life as clouds indicate rain, and suddenly produce a reversal of the natural state."),
    "limits": ("Prose, medium confidence. Printed स्वस्थनाम् is read स्वस्थानाम् (of the healthy) as a possible correction: "
               "no question rests on it. 'Desiring another body' is literal; the text does not say 'dying'. The simile "
               "borrows सूचयन्तः from the next phrase."),
    "explain_hi": ("यह इकाई रिष्ट का आधार बताती है: औषध की पहुँच से परे गए और पूरे शरीर में फैले दोष, दूसरे शरीर की इच्छा करने वाले पुरुषों में, अचानक स्वभाव का विपर्यास (उलटापन) उत्पन्न करते हैं। "
                   "जैसे बादल (घनाघनाः) वर्षा को सूचित करते हैं, वैसे ये दोष आयु के क्षय को सूचित करते हैं। "
                   "उपमा अधूरी है: ‘घनाघना इव वर्षम्’ अपना कृदन्त ‘सूचयन्तः’ अगले अंश से लेता है। "
                   "‘देहान्तराभिलाषिणाम्’ का शब्दार्थ है ‘दूसरे शरीर की इच्छा करने वाले’; पाठ ‘मरते हुए’ नहीं कहता। "
                   "छपा ‘स्वस्थनाम्’ सम्भवतः ‘स्वस्थानाम्’ (स्वस्थों का) है; यह सुधार अनुमान है, इसलिए उस पर प्रश्न नहीं।"),
    "hook": "बादल वर्षा बताते हैं, बेकाबू दोष आयु का क्षय।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "In card 2, what are the doṣas compared to?",
            ("Clouds foretelling rain", "घनाघना इव वर्षम्: like clouds (indicating) rain."),
            [("Rivers rising in flood", "No river is named; the simile is of clouds and rain."),
             ("Fires spreading in a wood", "No fire is named; the simile is of clouds and rain."),
             ("Winds drying up a lake", "No wind or lake is named; the simile is of clouds and rain.")],
            "Clouds indicate rain; these doṣas indicate the decay of life.",
            "घनाघन = cloud; वर्ष = rain."),
        order(1, "Put these parts of card 2 in the printed order.",
              ["पुरुषाणाम्", "देहान्तराभिलाषिणाम्", "औषधविषयम् अतीताः", "सकलशरीरव्यापिनः दोषाः", "घनाघनाः इव वर्षम्",
               "स्वभावविपर्यासं जनयन्ति"],
              "Of men; desiring another body; gone beyond the range of medicine; the doṣas pervading the whole body; like "
              "clouds rain; produce a reversal of the natural state.",
              "पुरुषाणाम् → देहान्तराभिलाषिणाम् → औषधविषयम् अतीताः → ... दोषाः → घनाघनाः इव → ... जनयन्ति."),
        match(2, "Match each word of card 2 to its meaning.",
              [["घनाघन", "cloud"], ["वर्ष", "rain"], ["आयुस्", "life"], ["क्षय", "decay"], ["अकस्मात्", "suddenly"],
               ["विपर्यास", "reversal"]],
              "घनाघन = cloud, वर्ष = rain, आयुस् = life, क्षय = decay, अकस्मात् = suddenly, विपर्यास = reversal.",
              "घनाघन, वर्ष, आयुस्, क्षय, अकस्मात्, विपर्यास.", role="extend",
              teaches="An elliptical simile borrows its verb from the next phrase: घनाघना इव वर्षम् (सूचयन्तः), like clouds (indicating) rain."),
        mcq("discriminate", 3, "In card 2, what do the doṣas indicate, as clouds indicate rain?",
            ("The decay of life", "आयुषः क्षयं सूचयन्तः: indicating the decay of life."),
            [("The coming of rain", "Rain is what the clouds indicate, in the simile; the doṣas indicate decay of life."),
             ("A return to health", "These doṣas are beyond medicine; nothing says health returns."),
             ("The change of season", "No season is named; the doṣas indicate decay of life.")],
            "Clouds → rain; these doṣas → decay of life.",
            "आयुषः क्षयम् = the decay of life."),
        multi("apply", 4, "Which statements fit card 2?",
              [("The doṣas pervade the whole body", "Yes: सकलशरीरव्यापिनः."),
               ("The text itself calls the men dying", "No: it says 'desiring another body'; 'dying' is not printed."),
               ("The reversal comes suddenly", "Yes: अकस्मात्, suddenly, without cause."),
               ("These doṣas still yield to medicine", "No: they have gone beyond its range (औषधविषयम् अतीताः).")],
              [0, 2],
              "Pervading the whole body, beyond medicine, suddenly reversing the natural state.",
              "सकलशरीरव्यापिनः; अकस्मात्; औषधविषयम् अतीताः."),
        mcq("transfer", 5, "By the pattern of सूचयन्तः + अकस्मात् → सूचयन्तोऽकस्मात्, how is रामः + अपि joined in a new example?",
            ("रामोऽपि", "अः + अ → ओ, and the अ is dropped (marked ऽ): रामः + अपि → रामोऽपि."),
            [("रामापि", "अ + अ → आ holds for a final अ; here the word ends in अः."),
             ("रामरपि", "र् comes from a visarga after a vowel other than अ/आ; here the vowel is अ."),
             ("राम अपि", "अः → अ only before vowels other than अ; before अ it is ओऽ.")],
            "रामः + अपि = रामोऽपि, like सूचयन्तः + अकस्मात् = सूचयन्तोऽकस्मात्.",
            "अः + अ → ओऽ.",
            teaches="अः before अ becomes ओ and the following अ is dropped, marked by ऽ: सूचयन्तः + अकस्मात् → सूचयन्तोऽकस्मात्."),
    ],
}

# ---------------------------------------------------------------- unit 3
AUTHORED["3"] = {
    "title": "तत्समासतो रिष्टमित्याहुः",
    "question": "By card 3, what is the name given, in brief, to that sudden reversal?",
    "rule": "In brief (समासतः), they call that (तत्) riṣṭa (रिष्टम्), a sign foretelling death.",
    "limits": ("Prose. riṣṭa is a doctrinal term; 'sign foretelling death' is the data's plain explanation, not a modern "
               "equivalent. The line does not say who 'they' are."),
    "explain_hi": ("संक्षेप में उसे ‘रिष्ट’ कहते हैं। रिष्ट यानी मृत्यु के निकट आने का सूचक लक्षण, अनिष्ट-सूचक चिह्न। "
                   "यह परिभाषा पिछली इकाई के स्वभाव-विपर्यास से जुड़ती है। "
                   "‘इति आहुः’ यानी ‘ऐसा कहते हैं’; ‘इति’ नाम या उद्धरण को चिह्नित करता है। "
                   "सन्धियाँ: समासतः + रि- → समासतो (घोष र से पहले अः → ओ), रिष्टम् + इति → रिष्टमिति, इति + आहुः → इत्याहुः (इ + भिन्न स्वर → य्)।"),
    "hook": "स्वभाव उलटा, नाम पड़ा रिष्ट।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By card 3, what is riṣṭa?",
            ("A sign foretelling death", "रिष्ट = an ill-omen, a sign of approaching death."),
            [("A medicine for the doṣas", "No medicine is named; riṣṭa is a sign of approaching death."),
             ("A healthy body colour", "The natural colours come in card 4; riṣṭa is a sign of death."),
             ("A season of heavy rain", "Rain is only the simile of card 2; riṣṭa is a sign of death.")],
            "रिष्टम् इति आहुः: they call it riṣṭa, a sign foretelling death.",
            "रिष्ट = sign of approaching death."),
        order(1, "Put the words of card 3 in the printed order.",
              ["तत्", "समासतः", "रिष्टम्", "इति", "आहुः"],
              "That; in brief; riṣṭa; thus; they say.",
              "तत् → समासतः → रिष्टम् → इति → आहुः."),
        match(2, "Match each word of card 3 to its meaning.",
              [["तत्", "that"], ["समासतः", "in brief"], ["रिष्ट", "sign foretelling death"], ["इति", "thus (marks the name)"],
               ["आहुः", "they say"]],
              "तत् = that, समासतः = in brief, रिष्ट = sign foretelling death, इति = thus, आहुः = they say.",
              "तत्, समासतः, रिष्ट, इति, आहुः.", role="extend",
              teaches="X इति आहुः = 'they call it X': इति marks the name that is given."),
        mcq("discriminate", 3, "Which split of रिष्टमित्याहुः in card 3 is right?",
            ("रिष्टम् + इति + आहुः", "म् joins the next vowel; इ before आ → य्: इति + आहुः → इत्याहुः."),
            [("रिष्टम् + इत्य + आहुः", "इत्य is not a word; the य् comes from the इ of इति."),
             ("रिष्टमि + त्याहुः", "Neither part is a word; the words are रिष्टम्, इति, आहुः."),
             ("रिष्टम् + इति + याहुः", "याहुः is not a word; the verb is आहुः.")],
            "रिष्टम् (riṣṭa) + इति (thus) + आहुः (they say).",
            "इ + unlike vowel → य्."),
        mcq("apply", 4, "Why does इति appear as इत्य् before आहुः in card 3?",
            ("इ before a different vowel → य्", "इति + आहुः: the final इ meets आ and becomes य्."),
            [("इ before any vowel → य्", "Not any: इ + इ gives ई, not य्."),
             ("इ before a consonant → य्", "Before a consonant इ stays; य् arises only before a vowel."),
             ("य् is part of the word इत्य", "The particle is इति; the य् comes only from sandhi.")],
            "इति + आहुः → इत्याहुः.",
            "इ + unlike vowel → य्."),
        mcq("transfer", 5, "By the pattern of इति + आहुः → इत्याहुः, how is दधि + अत्र (curd here) joined in a new example?",
            ("दध्यत्र", "इ before a different vowel → य्: दधि + अत्र → दध्यत्र."),
            [("दधेत्र", "ए comes from अ + इ, not from इ + अ."),
             ("दधीत्र", "ई comes from इ + इ; here the second vowel is अ."),
             ("दधयत्र", "अय् comes from ए before a vowel; here the vowel is इ.")],
            "दधि + अत्र = दध्यत्र, like इति + आहुः = इत्याहुः.",
            "इ + unlike vowel → य्.",
            teaches="इ, उ, ऋ before a different vowel become य्, व्, र्: इति + आहुः → इत्याहुः."),
    ],
}

# ---------------------------------------------------------------- unit 4
AUTHORED["4"] = {
    "title": "गौरोऽगौरः श्यामो ऽश्यामः",
    "question": "By card 4, which colours belong to the body's natural state?",
    "rule": ("Fair or not fair (गौरः अगौरः), dusky or not dusky (श्यामः अश्यामः), black or not black (कृष्णः अकृष्णः): "
             "these are the colours of the body's natural state (देहप्रकृतिवर्णाः)."),
    "limits": ("'Not fair' etc. is the literal sense of the अ- forms; a sense 'slightly fair' is possible but not stated: "
               "no question rests on it. 'Or' is supplied; the text has none."),
    "explain_hi": ("उनमें देह की प्रकृति के वर्ण छह शब्दों में, तीन जोड़ों में बताए गए हैं: गौर-अगौर, श्याम-अश्याम, कृष्ण-अकृष्ण। "
                   "‘अ-’ वाले रूपों का शब्दार्थ ‘जो गौर नहीं’ आदि है; ‘थोड़ा गौर’ अर्थ सम्भव है पर छपा नहीं। "
                   "‘या’ शब्द पाठ में नहीं, जोड़े दिखाने के लिए जोड़ा गया है। "
                   "सन्धि: गौरः + अगौरः → गौरोऽगौरः (अः + अ → ओ, अ का लोप ऽ से)। "
                   "‘ऽकृष्णइति’ में अकृष्णः + इति है: अ के अलावा किसी स्वर से पहले अः → अ, इसलिए अकृष्ण इति; केवल रिक्त स्थान छूटा है।"),
    "hook": "गौर, श्याम, कृष्ण: हर एक का ‘अ-’ जोड़ीदार भी प्राकृत।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By card 4, what are गौर, श्याम, कृष्ण and their अ- forms?",
            ("Natural colours of the body", "देहप्रकृतिवर्णाः: the colours of the body's natural state."),
            [("Abnormal colours of illness", "The abnormal colours (विकृतयः) come in card 6; these are natural."),
             ("Signs foretelling death", "These are natural colours, not riṣṭa signs."),
             ("Shades of the five elements", "The shades (छाया) by element come from card 8 on; these are colours.")],
            "गौर, श्याम, कृष्ण and their अ- forms: the body's natural colours.",
            "देहप्रकृतिवर्ण = colour of the body's natural state."),
        order(1, "Put the six colour words of card 4 in the printed order.",
              ["गौरः", "अगौरः", "श्यामः", "अश्यामः", "कृष्णः", "अकृष्णः"],
              "Fair, not fair; dusky, not dusky; black, not black.",
              "गौर → अगौर → श्याम → अश्याम → कृष्ण → अकृष्ण."),
        match(2, "Match each word of card 4 to its meaning.",
              [["गौर", "fair"], ["श्याम", "dusky"], ["कृष्ण", "black"], ["अ-", "not"],
               ["देहप्रकृतिवर्ण", "natural colour of the body"]],
              "गौर = fair, श्याम = dusky, कृष्ण = black, अ- = not, देहप्रकृतिवर्ण = natural colour of the body.",
              "गौर, श्याम, कृष्ण, अ-, देहप्रकृतिवर्ण.", role="extend",
              teaches="The prefix अ- negates a word: गौर (fair) → अगौर (not fair), the data's literal reading."),
        mcq("discriminate", 3, "Which English rendering of card 4's colour list is right?",
            ("Fair or not, dusky or not, black or not", "गौरोऽगौरः श्यामो ऽश्यामः कृष्णो ऽकृष्णः."),
            [("Fair or not, dusky or not, red or not", "The third pair is कृष्ण (black), not red."),
             ("Fair or not, white or not, black or not", "The second pair is श्याम (dusky), not white."),
             ("Pale or not, dusky or not, black or not", "The first pair is गौर (fair), not pale.")],
            "Three pairs: गौर, श्याम, कृष्ण, each with its अ- form.",
            "गौर = fair, श्याम = dusky, कृष्ण = black."),
        mcq("apply", 4, "How does अकृष्णः + इति join in card 4?",
            ("अकृष्ण इति", "अः before a vowel other than अ → अ; the two vowels then stay apart."),
            [("अकृष्णो इति", "ओ arises before अ or a voiced consonant; here the next sound is इ."),
             ("अकृष्णेति", "After अः → अ the vowels do not join again; ए would need a plain final अ."),
             ("अकृष्णरिति", "र् comes from a visarga after a vowel other than अ/आ; here the vowel is अ.")],
            "अकृष्णः + इति → अकृष्ण इति (printed without the space).",
            "अः + vowel other than अ → अ."),
        mcq("transfer", 5, "By the pattern of गौर → अगौर (not fair), what does अश्वेत mean in a new example?",
            ("Not white", "अ- negates: श्वेत (white) → अश्वेत, not white."),
            [("Very white", "'Very' would need a prefix such as सु- or अति-; अ- negates."),
             ("Whitened", "'Whitened' would be a participle such as श्वेतित; अ- negates."),
             ("White as milk", "A comparison would need a word such as इव; अ- negates.")],
            "अश्वेत = not white, like अगौर = not fair.",
            "अ- + word = not ...",
            teaches="The negative prefix अ- before a consonant: गौर → अगौर, श्याम → अश्याम, कृष्ण → अकृष्ण."),
    ],
}

# ---------------------------------------------------------------- unit 5
AUTHORED["5"] = {
    "title": "तद्भेदाश्च पद्मगौरादयः",
    "question": "By card 5, which variety of colour is named first, and is the list closed?",
    "rule": "And its varieties (तद्भेदाः च) are lotus-fair (पद्मगौर) and the like (आदयः).",
    "limits": ("Prose, no verb ('are' understood). Only पद्मगौर is named; आदयः leaves the list open. padma = lotus, "
               "Nelumbo nucifera (standard)."),
    "explain_hi": ("और उनके भेद पद्मगौर आदि हैं: पद्मगौर यानी कमल के समान गौर। "
                   "पद्म = कमल (Nelumbo nucifera; मानक पहचान)। "
                   "‘आदयः’ (आदि) बताता है कि सूची खुली है; केवल पहला भेद नाम से दिया गया है। "
                   "सन्धि: तत् + भेदाः → तद्भेदाः (घोष भ से पहले त् → द्), भेदाः + च → भेदाश्च (च से पहले विसर्ग → श्)।"),
    "hook": "पद्मगौर आदि: कमल-सा गौर, और ऐसे ही भेद।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "In card 5, what does पद्मगौर mean?",
            ("Fair like a lotus", "पद्म (lotus, Nelumbo nucifera; standard) + गौर (fair)."),
            [("Fair like the moon", "The moon would be चन्द्र; पद्म is the lotus."),
             ("Red like blood", "गौर is fair, and पद्म is the lotus, not blood."),
             ("Dark like a cloud", "गौर is fair, not dark; पद्म is the lotus.")],
            "पद्मगौर = fair like a lotus.",
            "पद्म = lotus; गौर = fair."),
        order(1, "Put the parts of card 5 in the printed order.",
              ["तद्भेदाः", "च", "पद्मगौर", "आदयः"],
              "Its varieties; and; lotus-fair; and the like.",
              "तद्भेदाः → च → पद्मगौर → आदयः."),
        match(2, "Match each part of card 5 to its meaning.",
              [["तत्", "its, of that"], ["भेद", "variety"], ["च", "and"], ["पद्म", "lotus (Nelumbo nucifera; standard)"],
               ["आदि", "and the like"]],
              "तत् = its, भेद = variety, च = and, पद्म = lotus, आदि = and the like.",
              "तत्, भेद, च, पद्म, आदि.", role="extend",
              teaches="-आदयः (from आदि) at the end of a compound means 'X and the like': the list is left open."),
        mcq("discriminate", 3, "Which split of तद्भेदाश्च in card 5 is right?",
            ("तत् + भेदाः + च", "त् → द् before the voiced भ; visarga → श् before च."),
            [("तद् + भेदा + श्च", "श्च is not a word; the श् comes from the visarga of भेदाः."),
             ("तद्भे + दाः + च", "Neither तद्भे nor दाः is a word here."),
             ("तत् + भेद + आश्च", "आश्च is not a word; भेदाः is one plural word.")],
            "तत् (its) + भेदाः (varieties) + च (and).",
            "त् + voiced consonant → द्; ः + च → श्च."),
        mcq("apply", 4, "In card 5, what does आदयः tell the reader about the varieties?",
            ("More of the kind exist", "आदयः = 'and the like': पद्मगौर is only the first named."),
            [("The list is complete", "आदयः leaves the list open; it is not complete."),
             ("These colours are abnormal", "Nothing in card 5 calls them abnormal."),
             ("These signal death", "Nothing in card 5 links them with death.")],
            "पद्मगौरादयः = lotus-fair and the like.",
            "आदि = and the like (open list)."),
        mcq("transfer", 5, "By the pattern of तत् + भेदाः → तद्भेदाः, how is सत् + भावः (good disposition) joined in a new example?",
            ("सद्भावः", "त् before the voiced भ becomes द्: सत् + भावः → सद्भावः."),
            [("सत्भावः", "त् cannot stay before a voiced consonant; it becomes द्."),
             ("सन्भावः", "न् could come only before a nasal; भ is not a nasal."),
             ("सभ्भावः", "त् does not turn into भ्; before भ it becomes द्.")],
            "सत् + भावः = सद्भावः, like तत् + भेदाः = तद्भेदाः.",
            "त् + voiced consonant → द्.",
            teaches="A final त् before a voiced consonant such as भ becomes द्: तत् + भेदाः → तद्भेदाः."),
    ],
}

# ---------------------------------------------------------------- unit 6
AUTHORED["6"] = {
    "title": "शुक्लादयस्तु विकृतयः",
    "question": "By card 6, which colours are abnormal, and what is said to lead to death?",
    "rule": ("But blue, dusky, copper-coloured, turmeric-yellow, white and the like are abnormalities (विकृतयः). The "
             "natural and the abnormal colour (प्रकृतिविकृतिवर्णौ), in a damaged condition, are for death (मरणाय)."),
    "limits": ("Low confidence. युगपद्गंधेगैकदेशे is damaged and unclear; the guess 'at once, or in one part of the body' "
               "is only a conjecture: no question on when the two colours lead to death. श्यामत्ताम्र has an extra त्. "
               "haridrā = Curcuma longa (standard)."),
    "explain_hi": ("नील, श्याम, ताम्र (ताँबे जैसा), हारिद्र (हल्दी के रंग का) और शुक्ल आदि तो विकृतियाँ हैं, यानी विकृत वर्ण। "
                   "हारिद्र हरिद्रा (हल्दी, Curcuma longa; मानक पहचान) से बना है। "
                   "फिर कहा है कि प्रकृति का वर्ण और विकृति का वर्ण, किसी स्थिति में, मृत्यु के लिए (मरणाय) होते हैं। "
                   "वह स्थिति बताने वाला शब्द ‘युगपद्गंधेगैकदेशे’ छपाई में बिगड़ा और अस्पष्ट है; ‘एक साथ या शरीर के एक भाग में’ केवल अनुमान है, इसलिए उस पर प्रश्न नहीं। "
                   "छपे ‘श्यामत्ताम्र’ में एक त् अधिक है; पढ़ना श्याम-ताम्र।"),
    "hook": "नील, श्याम, ताम्र, हारिद्र, शुक्ल: विकृत वर्ण।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By card 6, what are नील, ताम्र, हारिद्र and the like?",
            ("Abnormal changes of colour", "नील... शुक्लादयस्तु विकृतयः: they are abnormalities."),
            [("The body's natural colours", "The natural colours are those of card 4; these are called विकृतयः."),
             ("Varieties of lotus-fair", "Lotus-fair and the like are the varieties of card 5."),
             ("Shades of the five elements", "The shades (छाया) by element come from card 8 on.")],
            "तु (but) sets this list against the natural colours: these are abnormal.",
            "विकृति = abnormality."),
        order(1, "Put the colours of card 6's list in the printed order.",
              ["नील", "श्याम", "ताम्र", "हारिद्र", "शुक्ल"],
              "Blue, dusky, copper-coloured, turmeric-yellow, white (and the like).",
              "नील → श्याम → ताम्र → हारिद्र → शुक्ल."),
        match(2, "Match each word of card 6 to its meaning.",
              [["नील", "blue"], ["ताम्र", "copper-coloured"], ["हारिद्र", "turmeric-yellow (Curcuma longa; standard)"],
               ["शुक्ल", "white"], ["विकृति", "abnormality"]],
              "नील = blue, ताम्र = copper-coloured, हारिद्र = turmeric-yellow, शुक्ल = white, विकृति = abnormality.",
              "नील, ताम्र, हारिद्र, शुक्ल, विकृति.", role="extend",
              teaches="हारिद्र is formed from हरिद्रा (turmeric, Curcuma longa; standard): 'turmeric-coloured'."),
        mcq("discriminate", 3, "Which split of शुक्लादयस्तु in card 6 is right?",
            ("शुक्ल + आदयः + तु", "अ + आ → आ; visarga before त → स्."),
            [("शुक्ला + दयः + तु", "दयः is not the word; the ending is -आदयः, 'and the like'."),
             ("शुक्ल + आदय + स्तु", "स्तु is not a word; the स् comes from the visarga of आदयः."),
             ("शुक्लाद् + अयः + तु", "शुक्लाद् is not a word; शुक्ल means white.")],
            "शुक्ल (white) + आदयः (and the like) + तु (but).",
            "अ + आ → आ; ः + त → स्त."),
        mcq("apply", 4, "In card 6, what does the dative मरणाय mean?",
            ("For death", "-आय is the dative singular: मरणाय, for death, leading to death."),
            [("From death", "'From death' would be the ablative मरणात्."),
             ("Of death", "'Of death' would be the genitive मरणस्य."),
             ("In death", "'In death' would be the locative मरणे.")],
            "मरणाय = for death.",
            "Dative -आय = for."),
        mcq("transfer", 5, "By the pattern of मरण → मरणाय (for death), which form of रक्षण (protection) is its dative, for protection, in a new example?",
            ("रक्षणाय", "Dative singular of an अ-stem: -आय, 'for': रक्षणाय."),
            [("रक्षणात्", "-आत् is the ablative, 'from protection'."),
             ("रक्षणस्य", "-अस्य is the genitive, 'of protection'."),
             ("रक्षणे", "-ए is the locative, 'in protection'.")],
            "रक्षणाय = for protection, like मरणाय = for death.",
            "अ-stem dative sg. = -आय.",
            teaches="The dative singular of an अ-stem ends in -आय and means 'for, leading to': मरणाय = for death."),
    ],
}

# ---------------------------------------------------------------- unit 7
AUTHORED["7"] = {
    "title": "अनिमित्ततोऽन्यथात्वमुक्तं भवति",
    "question": "By card 7, what is said to change without cause?",
    "rule": ("By this is stated the being otherwise without cause (अनिमित्ततः अन्यथात्वम्) of fading, grief, joy, "
             "dryness, unctuousness and the like, and of all the states fixed by the division of doṣas etc."),
    "limits": ("Medium confidence; the construction is loose. Printed उरचय is no word; उपचय (growth) is a conjecture: no "
               "question on it. प्रकृतिभेदीय is read as the passage on varieties of prakṛti; its identity is not stated: "
               "no question on it."),
    "explain_hi": ("‘इससे’ यह भी कहा गया समझो कि मुरझाना, शोक, हर्ष, रूखापन, स्निग्धता आदि, और दोष आदि के भाग से नियत सभी भाव, बिना कारण (अनिमित्ततः) अन्यथा हो जाएँ। "
                   "प्रकृतिभेदीय में कहे गए बड़े, उपचित, सूक्ष्म और दीर्घ भाव भी इसी में आते हैं; प्रकृतिभेदीय कौन-सा अंश है, यह पंक्ति नहीं बताती। "
                   "छपा ‘उरचय’ कोई शब्द नहीं; ‘उपचय’ (वृद्धि) अनुमानित पाठ है, इसलिए उस पर प्रश्न नहीं। "
                   "‘अन्यथात्व’ = अन्यथा (दूसरी तरह) + त्व: दूसरी तरह हो जाना। "
                   "वाक्य-रचना ढीली है; षष्ठी पदों को उन भावों के रूप में लिया गया है जिनका अन्यथात्व कहा गया।"),
    "hook": "बिना कारण बदलाव: नियत भाव का अन्यथा होना।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "In card 7, what does अनिमित्ततः mean?",
            ("Without a cause", "अ-निमित्त = no cause; -तः = by way of: without cause."),
            [("With a clear cause", "अ- negates निमित्त; it is without a cause."),
             ("At a fixed time", "No time is named; निमित्त means cause."),
             ("Because of food", "No food is named; अनिमित्ततः is without cause.")],
            "अनिमित्ततः अन्यथात्वम् = being otherwise without cause.",
            "निमित्त = cause; अ- = without."),
        order(1, "Put these sure items of card 7's first list in the printed order (the doubtful word is left out).",
              ["म्लानि", "शोक", "हर्ष", "रौक्ष्य", "स्नेह"],
              "Fading, grief, joy, dryness, unctuousness (and the like).",
              "म्लानि → शोक → हर्ष → रौक्ष्य → स्नेह."),
        match(2, "Match each word of card 7 to its meaning.",
              [["म्लानि", "fading"], ["शोक", "grief"], ["हर्ष", "joy"], ["रौक्ष्य", "dryness"], ["स्नेह", "unctuousness"],
               ["अन्यथात्व", "being otherwise"]],
              "म्लानि = fading, शोक = grief, हर्ष = joy, रौक्ष्य = dryness, स्नेह = unctuousness, अन्यथात्व = being otherwise.",
              "म्लानि, शोक, हर्ष, रौक्ष्य, स्नेह, अन्यथात्व.", role="extend",
              teaches="-त्व makes an abstract noun: अन्यथा (otherwise) + त्व → अन्यथात्व, 'being otherwise'."),
        mcq("discriminate", 3, "Which two items of card 7's list are opposite in meaning by their glosses?",
            ("शोक and हर्ष", "शोक = grief, हर्ष = joy: a true pair of opposites."),
            [("म्लानि and शोक", "Fading and grief are not opposites."),
             ("हर्ष and रौक्ष्य", "Joy and dryness are not opposites."),
             ("शोक and रौक्ष्य", "Grief and dryness are not opposites.")],
            "Grief ⇄ joy; also dryness ⇄ unctuousness in the same list.",
            "शोक ⇄ हर्ष; रौक्ष्य ⇄ स्नेह."),
        multi("apply", 4, "Which statements fit card 7?",
              [("It gives a remedy for each change", "No: no remedy is named."),
               ("The change comes without a cause", "Yes: अनिमित्ततः."),
               ("It says each change kills at once", "No: no time of death is given."),
               ("The states are fixed by doṣas etc.", "Yes: दोषादिभागेन प्रतिनियतानाम्.")],
              [1, 3],
              "Fixed states becoming otherwise without cause.",
              "दोषादिभागेन प्रतिनियतानां भावानाम् अनिमित्ततः अन्यथात्वम्."),
        mcq("transfer", 5, "By the pattern of महत् + उपचय → महदुपचय, how is जगत् + ईशः (lord of the world) joined in a new example?",
            ("जगदीशः", "A final त् before a vowel becomes द्: जगत् + ईशः → जगदीशः."),
            [("जगतीशः", "त् does not stay before a vowel; it becomes द्."),
             ("जगन्नीशः", "न् could come only before a nasal; ई is a vowel."),
             ("जगदेशः", "The vowel ई stays ई; it does not become ए.")],
            "जगत् + ईशः = जगदीशः, like महत् + उपचय = महदुपचय.",
            "त् + vowel → द्.",
            teaches="A final त् before a vowel becomes द्: महत् + उपचय → महदुपचय."),
    ],
}

# ---------------------------------------------------------------- unit 8
AUTHORED["8"] = {
    "title": "छायास्तु शरीरे पंच",
    "question": "By card 8, how many chāyās are there in the body?",
    "rule": "As for the chāyās (छायाः तु), the shades or lustres, there are five (पञ्च) in the body (शरीरे).",
    "limits": ("Prose, no verb. chāyā is a technical term (shade, lustre, reflection of the body); the five are described "
               "by element in the next cards, not here."),
    "explain_hi": ("शरीर में छायाएँ पाँच हैं। छाया एक पारिभाषिक शब्द है: शरीर की छाया, कान्ति या प्रतिबिम्ब। "
                   "अगली इकाइयाँ इन पाँचों को महाभूतों के अनुसार बताती हैं; यहाँ केवल संख्या है। "
                   "‘तु’ नया विषय शुरू करता है: ‘जहाँ तक छायाओं की बात है’। "
                   "सन्धि: छायाः + तु → छायास्तु (त से पहले विसर्ग → स्)।"),
    "hook": "छायाएँ पाँच, प्रभाएँ (आगे) सात।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By card 8, how many chāyās are there in the body?",
            ("Five", "छायास्तु शरीरे पञ्च: five."),
            [("Seven", "Seven is the number of the prabhās (card 12), not of the chāyās."),
             ("Three", "The line says पञ्च, five."),
             ("Four", "The line says पञ्च, five.")],
            "पञ्च = five chāyās.",
            "छाया: पाँच."),
        order(1, "Put the words of card 8 in the printed order.",
              ["छायाः", "तु", "शरीरे", "पञ्च"],
              "The chāyās; as for; in the body; five.",
              "छायाः → तु → शरीरे → पञ्च."),
        match(2, "Match each word of card 8 to its meaning.",
              [["छाया", "shade, lustre"], ["तु", "as for, but"], ["शरीर", "body"], ["पञ्च", "five"]],
              "छाया = shade, lustre; तु = as for; शरीर = body; पञ्च = five.",
              "छाया, तु, शरीर, पञ्च.", role="extend",
              teaches="छाया in this chapter is a technical term: the shade or lustre of the body, of which there are five."),
        mcq("discriminate", 3, "Which split of छायास्तु in card 8 is right?",
            ("छायाः + तु", "Visarga before त → स्: छायाः + तु → छायास्तु."),
            [("छाया + स्तु", "स्तु is not a word; the स् comes from the visarga."),
             ("छायस् + तु", "The stem is छाया with a long आ; छायस् is not a form."),
             ("छायास् + अतु", "अतु is not a word; the particle is तु.")],
            "छायाः (the chāyās) + तु (as for).",
            "ः + त → स्त."),
        mcq("apply", 4, "In card 8, what does the particle तु do?",
            ("It opens a new topic", "तु = as for, but: it turns to a new subject, the chāyās."),
            [("It asks a question", "A question would need किम्; तु opens a new topic."),
             ("It negates the line", "A negation would need न; तु opens a new topic."),
             ("It marks a strong wish", "A wish would need an optative; तु opens a new topic.")],
            "छायास्तु: as for the chāyās ...",
            "तु = as for, but."),
        mcq("transfer", 5, "By the pattern of छायाः + तु → छायास्तु, how is देवाः + तु joined in a new example?",
            ("देवास्तु", "Visarga before त → स्: देवाः + तु → देवास्तु."),
            [("देवा तु", "आः drops its visarga only before a voiced sound; त is voiceless."),
             ("देवाश्तु", "श् comes before च, छ or श, not before त."),
             ("देवोस्तु", "ओ never arises from आः; the vowel stays आ.")],
            "देवाः + तु = देवास्तु, like छायाः + तु = छायास्तु.",
            "ः + त → स्त.",
            teaches="A visarga before त or थ becomes स्: छायाः + तु → छायास्तु."),
    ],
}

# ---------------------------------------------------------------- unit 9
AUTHORED["9"] = {
    "title": "वातात्पांशुभस्मरूक्षा",
    "question": "By card 9, what is the chāyā from wind (vāta) like?",
    "rule": ("From wind (वातात्): dry as dust and ash, reddish with dust, dark brown, lacking lustre, smelling of "
             "sweat-waste. The first line, of another chāyā, is unctuous and as if with lustre."),
    "limits": ("Low confidence for line 1: its long word खादम्लखङ्गाकाशनीलनिर्मला is damaged; the element ether is read "
               "from the pattern: no question on it. The noun छाया is understood from card 8, not printed. Line 2 is clear."),
    "explain_hi": ("दो छपी पंक्तियाँ जोड़ी गई हैं। पहली पंक्ति का लम्बा शब्द बिगड़ा हुआ है; अगली इकाइयों के क्रम से वह आकाश की छाया मानी जाती है, जो स्निग्ध और मानो प्रभा वाली (सप्रभेव) है। "
                   "दूसरी पंक्ति स्पष्ट है: वात (वायु) से आने वाली छाया धूल और राख जैसी रूखी, धूल से लाल, श्याव (गहरी भूरी), प्रभाहीन और स्वेदमल (पसीने रूपी मल) की गन्ध वाली होती है। "
                   "संज्ञा ‘छाया’ इकाई ८ से समझी जाती है; विशेषण स्त्रीलिंग एकवचन हैं। "
                   "सन्धियाँ: सप्रभा + इव → सप्रभेव (आ + इ → ए), रजः + अरुणा → रजोऽरुणा (अः + अ → ओऽ)।"),
    "hook": "वायु की छाया: रूखी, धूल-सी लाल, बिना चमक, पसीने की गन्ध।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By card 9, line 2, which element's chāyā is dry as dust and ash?",
            ("Wind", "वातात् पांशुभस्मरूक्षा: from wind, dry as dust and ash."),
            [("Water", "The water chāyā (card 11) is very unctuous, not dry."),
             ("Earth", "The earth chāyā (card 11) is unctuous and of pleasing lustre."),
             ("Fire", "The fire chāyā comes in card 10; line 2 names वात.")],
            "वातात् = from wind (vāta).",
            "वात → रूक्ष छाया."),
        order(1, "Put the words of card 9, line 2, after वातात् in the printed order.",
              ["पांशुभस्मरूक्षा", "रजोऽरुणा", "श्यावा", "निष्प्रभा", "स्वेदमलगंधिः"],
              "Dry as dust and ash; reddish with dust; dark brown; lacking lustre; smelling of sweat-waste.",
              "पांशुभस्मरूक्षा → रजोऽरुणा → श्यावा → निष्प्रभा → स्वेदमलगंधिः."),
        match(2, "Match each word of card 9, line 2, to its meaning.",
              [["रूक्ष", "dry"], ["अरुण", "reddish"], ["श्याव", "dark brown"], ["निष्प्रभ", "lacking lustre"],
               ["स्वेदमल", "sweat-waste"]],
              "रूक्ष = dry, अरुण = reddish, श्याव = dark brown, निष्प्रभ = lacking lustre, स्वेदमल = sweat-waste.",
              "रूक्ष, अरुण, श्याव, निष्प्रभ, स्वेदमल.", role="extend",
              teaches="-गन्धि at the end of a compound means 'smelling of': स्वेदमलगन्धिः = smelling of sweat-waste."),
        mcq("discriminate", 3, "Which split of सप्रभेव in card 9, line 1, is right?",
            ("सप्रभा + इव", "आ + इ → ए: सप्रभा + इव → सप्रभेव, as if with lustre."),
            [("सप्रभ + एव", "अ + ए would give ऐ (सप्रभैव), not ए."),
             ("सप्रभे + इव", "ए before इ would give अ इ or अयि, not ए."),
             ("सप्रभा + एव", "आ + ए would give ऐ (सप्रभैव), not ए.")],
            "सप्रभा (with lustre) + इव (as if).",
            "अ/आ + इ → ए."),
        multi("apply", 4, "Which statements fit the wind chāyā of card 9?",
              [("It lacks lustre", "Yes: निष्प्रभा."),
               ("It is very unctuous", "No: it is dry (रूक्षा); unctuous fits other chāyās."),
               ("It shines like fire", "No: it lacks lustre."),
               ("It smells of sweat-waste", "Yes: स्वेदमलगन्धिः.")],
              [0, 3],
              "Dry, dust-reddish, dark brown, lustreless, smelling of sweat-waste.",
              "वातात्: रूक्षा, अरुणा, श्यावा, निष्प्रभा, स्वेदमलगन्धिः."),
        mcq("transfer", 5, "By the pattern of वात → वातात् (from wind), which form of जल (water) is its ablative, from water, in a new example?",
            ("जलात्", "Ablative singular of an अ-stem: -आत्, 'from': जलात्."),
            [("जलस्य", "-अस्य is the genitive, 'of water'."),
             ("जलाय", "-आय is the dative, 'for water'."),
             ("जले", "-ए is the locative, 'in water'.")],
            "जलात् = from water, like वातात् = from wind.",
            "अ-stem ablative sg. = -आत्.",
            teaches="The ablative singular of an अ-stem ends in -आत् and means 'from': वातात् = from wind."),
    ],
}

# ---------------------------------------------------------------- unit 10
AUTHORED["10"] = {
    "title": "तेजस् की छाया: दृष्टिमुखा",
    "question": "By card 10, which element's chāyā is named, and what part of the line is clear?",
    "rule": ("From tejas, fire (तेजसः), comes a chāyā described in one damaged compound; it is called दृष्टिमुखा, "
             "'with eye and face'."),
    "limits": ("Low confidence. हुतहुताशविद्युतसतपनीयरक्ता is damaged; 'red like fire, lightning and gold' is only a "
               "guess: no question on it. दृष्टिमुखा is literal; the text does not say the colour shows in the eyes and "
               "face. तेजसः is read as ablative by the pattern of वातात्."),
    "explain_hi": ("तेजस् यानी अग्नि से आने वाली छाया का वर्णन एक लम्बे, बिगड़े हुए समास में है। "
                   "‘हुत-हुताश-विद्युत्-तपनीय-रक्ता’ (आहुति पाई अग्नि, बिजली और सोने जैसी लाल) केवल अनुमान है, इसलिए उस पर प्रश्न नहीं। "
                   "स्पष्ट शब्द ‘दृष्टिमुखा’ है: शब्दार्थ ‘दृष्टि और मुख वाली’; रंग आँखों और मुख में दिखता है, यह सम्भव है पर छपा नहीं। "
                   "‘तेजसः’ रूप में षष्ठी भी हो सकता है; वातात् के क्रम से यहाँ पंचमी (‘से’) पढ़ा गया है। "
                   "सन्धि: तेजसः + हुत- → तेजसो हुत- (घोष ह से पहले अः → ओ)।"),
    "hook": "अग्नि की छाया: दृष्टि और मुख वाली (बाकी अस्पष्ट)।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By card 10, from which element does this chāyā come?",
            ("Fire", "तेजसः: from tejas, the element fire."),
            [("Wind", "The wind chāyā is that of card 9 (वातात्)."),
             ("Water", "The water chāyā comes in card 11 (अम्भसः)."),
             ("Earth", "The earth chāyā comes in card 11 (भुवः).")],
            "तेजस् = fire.",
            "तेजस् → अग्नि की छाया."),
        match(1, "Match each sure word of card 10 to its meaning.",
              [["तेजस्", "fire (the element)"], ["दृष्टि", "eye, sight"], ["मुख", "face"]],
              "तेजस् = fire, दृष्टि = eye, मुख = face; दृष्टिमुखा = with eye and face.",
              "तेजस्, दृष्टि, मुख."),
        fill(2, "In card 10, the word meaning from fire (the element) is ____ (type it in Devanagari or in English letters, e.g. dharma).",
             accepts("तेजसः", "tejasaḥ", "तेजसो"),
             "तेजसः (printed तेजसो before ह) = from tejas, fire.",
             "तेजस् is an s-stem; तेजसः has the same form as the genitive, and the pattern of वातात् makes it 'from fire' here.",
             "तेजसः = from fire."),
        mcq("discriminate", 3, "Why is तेजसः printed तेजसो before हुत- in card 10?",
            ("अः before a voiced consonant → ओ", "ह is a voiced consonant: तेजसः + हुत- → तेजसो हुत-."),
            [("आः before a voiced consonant → ओ", "आः drops its visarga before a voiced sound; and here the vowel is अ."),
             ("Every visarga before ह → ओ", "Not every: after इ or उ the visarga gives र् before ह."),
             ("ओ is the stem's own ending", "The stem is तेजस्; ओ comes only from sandhi.")],
            "तेजसः + हुत-: अः before the voiced ह → ओ.",
            "अः + voiced consonant → ओ."),
        multi("apply", 4, "Which statements about card 10 are sure?",
              [("The long compound is clear in print", "No: it is damaged and unclear."),
               ("The text says the colour shows in the eyes", "No: that is probable, but not printed."),
               ("The element named is tejas, fire", "Yes: तेजसः."),
               ("दृष्टिमुखा means 'with eye and face'", "Yes: the data's literal reading.")],
              [2, 3],
              "Sure: the element (fire) and the word दृष्टिमुखा; the long compound is unclear.",
              "तेजसः ... दृष्टिमुखा."),
        mcq("transfer", 5, "By the pattern of तेजसः + हुत- → तेजसो हुत-, how is रामः + हसति (Rāma laughs) joined in a new example?",
            ("रामो हसति", "अः before the voiced consonant ह → ओ: रामो हसति."),
            [("रामा हसति", "अः does not lengthen to आ; before a voiced consonant it gives ओ."),
             ("रामर् हसति", "र् comes from a visarga after a vowel other than अ/आ; here the vowel is अ."),
             ("राम हसति", "अः → अ only before vowels other than अ; ह is a consonant.")],
            "रामः + हसति = रामो हसति, like तेजसः + हुत- = तेजसो हुत-.",
            "अः + voiced consonant → ओ.",
            teaches="अः before a voiced consonant (here ह) becomes ओ: तेजसः + हुत- → तेजसो हुत-."),
    ],
}

# ---------------------------------------------------------------- unit 11
AUTHORED["11"] = {
    "title": "अंभसो और भुवो: जल और पृथ्वी की छाया",
    "question": "By card 11, how do the chāyās from water and from earth differ, and what do they share?",
    "rule": ("From water (अम्भसः): clear as vaidūrya, dense, very unctuous. From earth (भुवः): of pleasing lustre, dense, "
             "steady, unctuous, dusky and white."),
    "limits": ("Medium confidence. vaidūrya = beryl or cat's-eye (disputed); इन्द्रनील (probably sapphire) is a conjectural "
               "reading of printed इंद्रील; स्निग्धाशुद्धा may be 'unctuous, pure' or 'unctuous, impure': no question on the "
               "gems or on शुद्धा. The noun छाया is understood from card 8."),
    "explain_hi": ("दो छपी पंक्तियाँ जोड़ी गई हैं। जल (अम्भस्) की छाया वैदूर्य के समान निर्मल, घनी और अत्यन्त स्निग्ध (सुस्निग्धा) होती है। "
                   "वैदूर्य की पहचान विवादित है (लहसुनिया या बेरिल); छपा ‘इंद्रील’ कोई शब्द नहीं, ‘इन्द्रनील’ (सम्भवतः नीलम) अनुमानित पाठ है। "
                   "पृथ्वी (भू) की छाया सुन्दर कान्ति वाली, घनी, स्थिर, स्निग्ध, श्याम और श्वेत होती है। "
                   "‘स्निग्धाशुद्धा’ को स्निग्धा शुद्धा (रिक्त स्थान छूटा) या स्निग्धा अशुद्धा, दोनों तरह पढ़ा जा सकता है; इसलिए उस पर प्रश्न नहीं। "
                   "दोनों छायाएँ घनी हैं।"),
    "hook": "जल की छाया: अति स्निग्ध; पृथ्वी की: स्थिर। दोनों घनी।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By card 11, which quality is said of the earth chāyā?",
            ("Steady", "भुवो ... स्थिरा: the earth chāyā is steady."),
            [("Dry as ash", "Dry as dust and ash is the wind chāyā of card 9."),
             ("Lacking lustre", "The earth chāyā is of pleasing lustre (रुचिराभा)."),
             ("Smelling of sweat", "That is said of the wind chāyā (card 9).")],
            "Earth: pleasing lustre, dense, steady, unctuous, dusky, white.",
            "भू की छाया: स्थिरा."),
        order(1, "Put these sure words of card 11's earth line in the printed order.",
              ["रुचिराभा", "घना", "स्थिरा", "स्निग्धा", "श्यामा", "श्वेता"],
              "Of pleasing lustre, dense, steady, unctuous, dusky, white.",
              "रुचिराभा → घना → स्थिरा → स्निग्धा → श्यामा → श्वेता."),
        match(2, "Match each word of card 11 to its meaning.",
              [["अम्भस्", "water"], ["भू", "earth"], ["घन", "dense"], ["सुस्निग्ध", "very unctuous"], ["स्थिर", "steady"],
               ["रुचिर", "pleasing"]],
              "अम्भस् = water, भू = earth, घन = dense, सुस्निग्ध = very unctuous, स्थिर = steady, रुचिर = pleasing.",
              "अम्भस्, भू, घन, सुस्निग्ध, स्थिर, रुचिर.", role="extend",
              teaches="The prefix सु- here means 'very, well': स्निग्धा (unctuous) → सुस्निग्धा (very unctuous)."),
        mcq("discriminate", 3, "By card 11, which quality do the water and the earth chāyā both have?",
            ("Dense", "घना stands in both lines."),
            [("Steady", "स्थिरा is said only of the earth chāyā."),
             ("White", "श्वेता is said only of the earth chāyā."),
             ("Of pleasing lustre", "रुचिराभा is said only of the earth chāyā.")],
            "Water: घना; earth: घना.",
            "घन = dense (both)."),
        mcq("apply", 4, "By card 11, which chāyā is called सुस्निग्धा, very unctuous?",
            ("The water one", "अम्भसो ... घना सुस्निग्धा."),
            [("The earth one", "The earth chāyā is called स्निग्धा, without सु-."),
             ("The wind one", "The wind chāyā is dry (रूक्षा), card 9."),
             ("The fire one", "The fire chāyā is that of card 10.")],
            "सुस्निग्धा belongs to the water line.",
            "अम्भस् → सुस्निग्धा."),
        mcq("transfer", 5, "By the pattern of स्निग्धा → सुस्निग्धा (very unctuous), what does सुशीतल mean in a new example?",
            ("Very cool", "सु- = very: शीतल (cool) → सुशीतल, very cool."),
            [("Not cool", "'Not' would need the prefix अ-: अशीतल."),
             ("Cooled again", "'Again' would need पुनः; सु- means very."),
             ("Like the cold", "A comparison would need इव; सु- means very.")],
            "सुशीतल = very cool, like सुस्निग्धा = very unctuous.",
            "सु- + adjective = very ...",
            teaches="The prefix सु- strengthens an adjective: स्निग्धा → सुस्निग्धा, very unctuous."),
    ],
}

# ---------------------------------------------------------------- unit 12
AUTHORED["12"] = {
    "title": "तासां वायव्या विनाशाय",
    "question": "By card 12, which chāyā brings destruction, and what are the seven prabhās?",
    "rule": ("Of these chāyās, the one of vāyu is for destruction and very great affliction; the rest bring a rise of "
             "happiness. The prabhās are seven: red, yellow, pale, white, black, dark brown, green."),
    "limits": ("Prose. 'Very great' is taken with affliction; the noun is not repeated. असित is literally 'not white', "
               "rendered black; हरित may also be yellowish-green. No question on the dropped visargas of the list (हरिता च)."),
    "explain_hi": ("दो छपी पंक्तियाँ जोड़ी गई हैं। पाँच छायाओं में वायु वाली (वायव्या) विनाश और अत्यन्त बड़े क्लेश के लिए होती है; शेष छायाएँ सुख का उदय करने वाली (सुखोदयाः) हैं। "
                   "फिर प्रभाएँ सात बताई गई हैं: रक्त (लाल), पीत (पीली), पाण्डुर (फीकी), सित (सफेद), असित (काली), श्याव (गहरी भूरी) और हरित (हरी)। "
                   "असित का शब्दार्थ ‘जो सित नहीं’ है, इसे काली पढ़ा गया; हरित पीला-हरा भी हो सकता है। "
                   "सन्धियाँ: च + अतिमहते → चातिमहते (अ + अ → आ), शेषाः + तु → शेषास्तु (त से पहले विसर्ग → स्), सुख + उदयाः → सुखोदयाः (अ + उ → ओ)।"),
    "hook": "पाँच छाया: वायु की घातक, बाकी सुखद। प्रभा सात रंगों की।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By card 12, what is the chāyā of vāyu for?",
            ("For destruction and great affliction", "वायव्या विनाशाय क्लेशाय चातिमहते."),
            [("For happiness and a long healthy life", "A rise of happiness is said of the remaining chāyās, not vāyu's."),
             ("For strength of body and of mind", "No strength is named in card 12."),
             ("For lustre of the eyes and the face", "Card 12 names no eyes or face.")],
            "Vāyu's chāyā: destruction and very great affliction.",
            "वायव्या → विनाश, क्लेश."),
        order(1, "Put the first six prabhās of card 12 in the printed order.",
              ["रक्ता", "पीता", "पाण्डुरा", "सिता", "असिता", "श्यावा"],
              "Red, yellow, pale, white, black, dark brown (then green).",
              "रक्ता → पीता → पाण्डुरा → सिता → असिता → श्यावा (→ हरिता)."),
        match(2, "Match each prabhā of card 12 to its colour.",
              [["रक्त", "red"], ["पीत", "yellow"], ["पाण्डुर", "pale"], ["सित", "white"], ["असित", "black"],
               ["हरित", "green"]],
              "रक्त = red, पीत = yellow, पाण्डुर = pale, सित = white, असित = black, हरित = green.",
              "रक्त, पीत, पाण्डुर, सित, असित, हरित.", role="extend",
              teaches="असित = अ + सित, literally 'not white'; the data renders it black."),
        mcq("discriminate", 3, "By card 12, which chāyās bring a rise of happiness (सुखोदयाः)?",
            ("All but the vāyu one", "शेषास्तु सुखोदयाः: the remaining ones."),
            [("Only the vāyu one", "Vāyu's chāyā is for destruction and affliction."),
             ("All five, vāyu's too", "Vāyu's chāyā is set apart: it is for destruction."),
             ("None of the five", "The remaining ones (शेषाः) bring happiness.")],
            "वायव्या → destruction; शेषाः → happiness.",
            "शेष = the remaining ones."),
        multi("apply", 4, "Which statements fit card 12?",
              [("There are five prabhās", "No: the prabhās are seven (सप्त); the chāyās are five."),
               ("The vāyu chāyā is for destruction", "Yes: वायव्या विनाशाय."),
               ("हरित is one of the prabhās", "Yes: the last of the seven."),
               ("The other chāyās bring affliction", "No: they bring a rise of happiness.")],
              [1, 2],
              "Vāyu's chāyā destroys; the rest bring happiness; seven prabhās.",
              "वायव्या विनाशाय; शेषाः सुखोदयाः; सप्त प्रभाः."),
        mcq("transfer", 5, "By the pattern of च + अतिमहते → चातिमहते, how is न + अस्ति joined in a new example?",
            ("नास्ति", "अ + अ → आ: न + अस्ति → नास्ति."),
            [("नेस्ति", "ए comes from अ + इ; here the second vowel is अ."),
             ("नस्ति", "Two अ-vowels join into a long आ; one cannot simply vanish."),
             ("नोस्ति", "ओ comes from अ + उ or from अः; here it is plain अ + अ.")],
            "न + अस्ति = नास्ति, like च + अतिमहते = चातिमहते.",
            "अ + अ → आ.",
            teaches="Two short अ vowels join into long आ: च + अतिमहते → चातिमहते."),
    ],
}

# ---------------------------------------------------------------- unit 13
AUTHORED["13"] = {
    "title": "ताः स्निग्धा विकाशिन्योऽमलाः शुभाः",
    "question": "By card 13, which prabhās are auspicious and which are not?",
    "rule": ("Those prabhās (ताः) that are unctuous, spreading and stainless are auspicious (शुभाः); the opposite ones "
             "(विपरीताः) are inauspicious (अशुभाः)."),
    "limits": ("Prose. ताः refers to the prabhās of card 12 (data's note). विकाशिन् is rendered 'spreading, radiant'. "
               "The line does not say what the inauspicious prabhās foretell."),
    "explain_hi": ("वे प्रभाएँ (ताः) जो स्निग्ध, विकसित होने वाली (विकाशिन्यः) और निर्मल (अमलाः) हों, शुभ हैं; उनसे विपरीत अशुभ हैं। "
                   "‘ताः’ इकाई १२ की सात प्रभाओं की ओर संकेत करता है। "
                   "अशुभ प्रभाएँ क्या सूचित करती हैं, यह पंक्ति नहीं कहती। "
                   "सन्धियाँ: विकाशिन्यः + अमलाः → विकाशिन्योऽमलाः (अः + अ → ओऽ), विपरीताः + तु → विपरीतास्तु, तु + अशुभाः → त्वशुभाः (उ + भिन्न स्वर → व्)।"),
    "hook": "चिकनी, फैलती, निर्मल प्रभा शुभ; उलटी अशुभ।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By card 13, which prabhās are auspicious?",
            ("Unctuous, radiant, stainless", "ताः स्निग्धा विकाशिन्योऽमलाः शुभाः."),
            [("Dry, dark and without lustre", "Those are the opposite kind, called अशुभ."),
             ("Red, yellow and pale ones", "Card 13 picks no colours; it names qualities."),
             ("Dense, steady and white", "These words describe the earth chāyā (card 11).")],
            "स्निग्ध, विकाशिन्, अमल → शुभ.",
            "स्निग्ध + विकाशी + अमल = शुभ."),
        order(1, "Put the words of card 13's first clause in the printed order.",
              ["ताः", "स्निग्धाः", "विकाशिन्यः", "अमलाः", "शुभाः"],
              "Those; unctuous; spreading; stainless; auspicious.",
              "ताः → स्निग्धाः → विकाशिन्यः → अमलाः → शुभाः."),
        match(2, "Match each word of card 13 to its meaning.",
              [["स्निग्ध", "unctuous"], ["विकाशिन्", "spreading, radiant"], ["अमल", "stainless"], ["शुभ", "auspicious"],
               ["विपरीत", "opposite"]],
              "स्निग्ध = unctuous, विकाशिन् = spreading, अमल = stainless, शुभ = auspicious, विपरीत = opposite.",
              "स्निग्ध, विकाशिन्, अमल, शुभ, विपरीत.", role="extend",
              teaches="अ- negates here too: मल (stain) → अमल (stainless), शुभ → अशुभ (inauspicious)."),
        mcq("discriminate", 3, "Which split of विपरीतास्त्वशुभाः in card 13 is right?",
            ("विपरीताः + तु + अशुभाः", "ः + त → स्त; उ + अ → व्: तु + अशुभाः → त्वशुभाः."),
            [("विपरीताः + तु + शुभाः", "तु + शुभाः would stay तु शुभाः; the व् shows a vowel अ followed."),
             ("विपरीताः + त्व + शुभाः", "त्व is not a word here; the व् comes from the उ of तु."),
             ("विपरी + तास्तु + अशुभाः", "Neither विपरी nor तास्तु is a word here.")],
            "विपरीताः (the opposite) + तु (but) + अशुभाः (inauspicious).",
            "ः + त → स्त; उ + unlike vowel → व्."),
        mcq("apply", 4, "By card 13, what does the text call the opposite prabhās (विपरीताः)?",
            ("Inauspicious", "विपरीतास्त्वशुभाः: the opposite ones are inauspicious."),
            [("Auspicious", "Auspicious are the unctuous, spreading, stainless ones."),
             ("Very auspicious", "Auspicious are the unctuous, spreading, stainless ones, not the opposite."),
             ("Stainless", "Stainless is a mark of the auspicious ones.")],
            "विपरीताः → अशुभाः.",
            "विपरीत = अशुभ."),
        mcq("transfer", 5, "By the pattern of तु + अशुभाः → त्वशुभाः, how is वस्तु + अत्र (the thing here) joined in a new example?",
            ("वस्त्वत्र", "उ before a different vowel → व्: वस्तु + अत्र → वस्त्वत्र."),
            [("वस्तोत्र", "ओ comes from अ + उ, not from उ + अ."),
             ("वस्तूत्र", "ऊ comes from उ + उ; here the second vowel is अ."),
             ("वस्तवत्र", "अव् comes from ओ before a vowel; here the vowel is उ.")],
            "वस्तु + अत्र = वस्त्वत्र, like तु + अशुभाः = त्वशुभाः.",
            "उ + unlike vowel → व्.",
            teaches="उ before a different vowel becomes व्: तु + अशुभाः → त्वशुभाः."),
    ],
}

# ================================================================ NOTES_HI
NOTES_HI = {
    "1": ("गद्य; विश्वास उच्च; कोई पाठ-चिह्न नहीं। अध्याय-आरम्भ का मानक सूत्र; ‘विकृताङ्गविज्ञानीयम्’ विशेषण ‘अध्यायम्’ का है। "
          "सन्धि जाँची: अथ + अतः → अथातः (अ + अ → आ); अतः + विकृत- → अतो विकृत- (घोष व्यंजन से पहले अः → ओ); अध्यायम् + व्या- → "
          "अध्यायं (व्यंजन से पहले अन्तिम म् → ं)। छपा ‘विकृतांग’ अनुस्वार के साथ = विकृताङ्ग।"),
    "2": ("गद्य; विश्वास मध्यम। पाठ-चिह्न (सम्भव): छपा ‘स्वस्थनाम्’ षष्ठी बहुवचन के दीर्घ आ के बिना है; ‘स्वस्थानाम्’ पढ़ा गया, यह "
          "सुधार अनुमान है, इस पर प्रश्न नहीं। ‘विपर्य्यास’ (दोहरा य) को विपर्यास पढ़ा गया। उपमा अधूरी: ‘घनाघना इव वर्षम्’ कृदन्त "
          "‘सूचयन्तः’ अगले अंश से लेता है; घनाघन = बादल (घना, हाथी आदि अर्थ यहाँ उपयुक्त नहीं)। ‘देहान्तराभिलाषिणाम्’ = दूसरे शरीर "
          "की इच्छा करने वाले; ‘मरते हुए’ छपा नहीं। सन्धि जाँची: व्यापिनः + दोषाः → व्यापिनो दोषा (अः + घोष व्यंजन → ओ; आः घोष से पहले "
          "विसर्ग खोता है); घनाघनाः + इव → घनाघना इव; सूचयन्तः + अकस्मात् → सूचयन्तोऽकस्मात् (अः + अ → ओऽ)। ‘मतीताःसकल’ में "
          "रिक्त स्थान छूटा है।"),
    "3": ("गद्य; विश्वास उच्च; कोई पाठ-चिह्न नहीं। रिष्ट पारिभाषिक शब्द है (मृत्यु-सूचक लक्षण); आधुनिक पर्याय नहीं दिया गया। "
          "सन्धि जाँची: तत् + समासतः → तत्समासतः (स से पहले त् बना रहता है); समासतः + रि- → समासतो (अः + घोष र → ओ); रिष्टम् + इति → "
          "रिष्टमिति; इति + आहुः → इत्याहुः (इ + भिन्न स्वर → य्)।"),
    "4": ("गद्य; विश्वास मध्यम; कोई पाठ-चिह्न नहीं। ‘अ-’ रूपों का शब्दार्थ ‘जो ... नहीं’ लिया गया; ‘थोड़ा’ अर्थ सम्भव पर कथित नहीं। "
          "‘या’ जोड़ा गया है, पाठ में नहीं। प्रकृति = स्वाभाविक अवस्था। सन्धि जाँची: गौरः + अगौरः → गौरोऽगौरः, श्यामः + अश्यामः → "
          "श्यामोऽश्यामः, कृष्णः + अकृष्णः → कृष्णोऽकृष्णः (अः + अ → ओऽ); अकृष्णः + इति → अकृष्ण इति (अ के अलावा स्वर से पहले अः → अ)। "
          "समीक्षक के अनुसार छपा ‘ऽकृष्णइति’ में अलग स्वर इ है; केवल रिक्त स्थान छूटा, सन्धि-दोष नहीं।"),
    "5": ("गद्य; विश्वास उच्च; कोई पाठ-चिह्न नहीं। क्रिया (हैं) समझी जाती है। पद्म = कमल, Nelumbo nucifera (मानक); पद्मगौर = "
          "कमल जैसा गौर। सन्धि जाँची: तत् + भेदाः → तद्भेदाः (घोष भ से पहले त् → द्); भेदाः + च → भेदाश्च (च से पहले विसर्ग → श्); "
          "पद्मगौर + आदयः → पद्मगौरादयः (अ + आ → आ)।"),
    "6": ("गद्य; विश्वास कम। पाठ-चिह्न (सम्भव): ‘युगपद्गंधेगैकदेशे’ बिगड़ा है, बिना विभाजन रखा गया; ‘युगपद् गात्रैकदेशे’ (एक साथ, या "
          "शरीर के एक भाग में) केवल अनुमान है, अनुवाद में ‘अस्पष्ट’; इस पर प्रश्न नहीं। दूसरा चिह्न: ‘श्यामत्ताम्र’ में अधिक त्, "
          "पढ़ना श्याम-ताम्र। हारिद्र ← हरिद्रा (हल्दी, Curcuma longa; मानक)। ‘विकृतयःतत्र’ में रिक्त स्थान छूटा; नियमित सन्धि "
          "विकृतयस्तत्र होती (त से पहले विसर्ग → स्)। सन्धि जाँची: शुक्ल + आदयः + तु → शुक्लादयस्तु। मरणाय = चतुर्थी, मृत्यु के लिए।"),
    "7": ("गद्य; विश्वास मध्यम। पाठ-चिह्न (सम्भव): ‘उरचय’ कोई शब्द नहीं; ‘उपचय’ (वृद्धि; र/प की भूल) अनुमान है, इस पर प्रश्न नहीं; "
          "‘एतेनम्लानि’ में रिक्त स्थान छूटा। रचना ढीली: षष्ठी पद उन भावों के रूप में लिए गए जिनका अन्यथात्व कहा गया। "
          "‘प्रकृतिभेदीय’ = प्रकृति-भेदों वाला अंश; उसकी पहचान पंक्ति में नहीं। सन्धि जाँची: म्लानि + उ- → म्लान्यु- (इ + भिन्न स्वर → "
          "य्); महत् + उपचय → महदुपचय (स्वर से पहले त् → द्); अनिमित्ततः + अन्यथात्वम् → अनिमित्ततोऽन्यथात्वम् (अः + अ → ओऽ); "
          "प्रकृतिभेदीय + उक्तानाम् → प्रकृतिभेदीयोक्तानाम् (अ + उ → ओ)। ‘प्रतिनियतानांभावानाम्’ में रिक्त स्थान छूटा।"),
    "8": ("गद्य; विश्वास उच्च; कोई पाठ-चिह्न नहीं। छाया पारिभाषिक शब्द: शरीर की छाया, कान्ति या प्रतिबिम्ब; पाँचों का वर्णन अगली "
          "इकाइयों में महाभूतों के अनुसार है। सन्धि जाँची: छायाः + तु → छायास्तु (त से पहले विसर्ग → स्)। छपा ‘पंच’ = पञ्च।"),
    "9": ("गद्य; विश्वास कम; दो छपी पंक्तियाँ (०२.०९.९ और ०२.०९.१०) जोड़ी गईं। पाठ-चिह्न (सम्भव): ‘खादम्लखङ्गाकाशनीलनिर्मला’ "
          "बिगड़ा है, बिना विभाजन; ‘खात् अमल-खड्ग-आकाश-नील-निर्मला’ केवल अनुमान है (खङ्ग सम्भवतः खड्ग, ड/ङ की भूल); अनुवाद में "
          "‘अस्पष्ट’; इस पर प्रश्न नहीं। आकाश की छाया अगली चार पंक्तियों के क्रम (वातात्, तेजसः, अम्भसः, भुवः) से मानी गई। "
          "संज्ञा ‘छाया’ इकाई ८ से। सन्धि जाँची: सप्रभा + इव → सप्रभेव (आ + इ → ए); रजः + अरुणा → रजोऽरुणा (अः + अ → ओऽ); निः + प्रभा "
          "→ निष्प्रभा। ‘गन्धिः’ इ-अन्त विशेषण का स्त्रीलिंग रूप; मल = स्वेद रूपी मल, कोई रोग नहीं।"),
    "10": ("गद्य; विश्वास कम। पाठ-चिह्न (सम्भव): ‘हुतहुताशविद्युतसतपनीयरक्ता’ बिगड़ा है; ‘हुत-हुताश-विद्युत्-तपनीय-रक्ता’ (आहुति "
           "पाई अग्नि, बिजली और सोने जैसी लाल) अनुमान है, ‘असत’ अक्षरों का हिसाब नहीं बैठता; इस पर प्रश्न नहीं। ‘दृष्टिमुखा’ = दृष्टि "
           "और मुख वाली; रंग आँख-मुख में दिखता है, यह छपा नहीं। तेजस् = अग्नि महाभूत; ‘तेजसः’ को वातात् के क्रम से पंचमी पढ़ा गया। "
           "सन्धि जाँची: तेजसः + हुत- → तेजसो हुत- (अः + घोष ह → ओ); छपाई में रिक्त स्थान छूटा।"),
    "11": ("गद्य; विश्वास मध्यम; दो छपी पंक्तियाँ (०२.०९.१२ और ०२.०९.१३) जोड़ी गईं। पाठ-चिह्न (सम्भव): छपा ‘इंद्रील’ कोई शब्द "
           "नहीं; ‘इन्द्रनील’ (सम्भवतः नीलम) अनुमान है। वैदूर्य की पहचान विवादित (लहसुनिया या बेरिल)। दूसरा चिह्न: ‘स्निग्धाशुद्धा’ "
           "छपे रूप में नियमित सन्धि से स्निग्धा + अशुद्धा (अशुद्ध) भी है; ‘स्निग्धा शुद्धा’ (रिक्त स्थान छूटा) माना गया; इस पर प्रश्न "
           "नहीं। संज्ञा ‘छाया’ इकाई ८ से। सन्धि जाँची: अम्भसः + वै- → अम्भसो (अः + घोष व → ओ); वैदूर्य + इ- → वैदूर्ये- (अ + इ → ए); "
           "भुवः + रुचिराभा → भुवो रुचिराभा; रुचिर + आभा → रुचिराभा।"),
    "12": ("गद्य; विश्वास उच्च; दो छपी पंक्तियाँ (०२.०९.१४ और ०२.०९.१५) जोड़ी गईं। पाठ-चिह्न (सम्भव): ‘हरिता च’ में च से पहले "
           "विसर्ग श् होना चाहिए (हरिताश्च); रक्ता पीता, पीता पाण्डुरा, पाण्डुरा सिता में भी अघोष व्यंजन से पहले विसर्ग छूटा है "
           "(छपाई की आदत)। ‘अतिमहते’ को क्लेशाय के साथ लिया गया। असित = ‘जो सित नहीं’, काली पढ़ी गई; हरित पीला-हरा भी हो सकता है। "
           "छपा ‘ऽसिता’: डेटा इसे सिताः असिताः पढ़ता है (आः + स्वर → विसर्ग-लोप)। सन्धि जाँची: च + अतिमहते → चातिमहते (अ + अ → आ); "
           "शेषाः + तु → शेषास्तु; सुख + उदयाः → सुखोदयाः (अ + उ → ओ)।"),
    "13": ("गद्य; विश्वास उच्च; कोई पाठ-चिह्न नहीं। ‘ताः’ इकाई १२ की प्रभाओं की ओर। विकाशिन् = फैलने वाली, दीप्त। सन्धि जाँची: "
           "विकाशिन्यः + अमलाः → विकाशिन्योऽमलाः (अः + अ → ओऽ); विपरीताः + तु → विपरीतास्तु (त से पहले विसर्ग → स्); तु + अशुभाः → "
           "त्वशुभाः (उ + भिन्न स्वर → व्)। ‘ताः स्निग्धा’ और ‘अमलाः शुभाः’ में स/श से पहले विसर्ग बना रहना भी ठीक है (स्/श् वैकल्पिक)। "
           "छपा ‘शुभाः विपरीताः’ घोष व से पहले विसर्ग रखता है (सन्धि नहीं की गई; नियमित रूप शुभा विपरीताः)।"),
}

# ================================================================ AIDS
AIDS = {
    "1": {
        "chunks": "अथातो | विकृतांगविज्ञानीयमध्यायं | व्याख्यास्यामः",
        "frame": "कब: अथ (अब) → क्यों: अतः (इसलिए) → क्या: विकृताङ्गविज्ञानीय अध्याय → क्या करेंगे: व्याख्यास्यामः (व्याख्या करेंगे)।",
        "sandhi": ("अ + अ → आ: अथ + अतः → अथातः · अः + घोष व्यंजन → ओ: अतः + विकृत- → अतो विकृत- · व्यंजन से पहले अन्तिम म् → ं: "
                   "अध्यायम् + व्याख्यास्यामः → अध्यायं व्याख्यास्यामः।"),
    },
    "2": {
        "diagram": {"groups": [
            {"label": "उपमान", "items": ["घनाघनाः: बादल", "वर्षम्: वर्षा को सूचित करते हैं"]},
            {"label": "उपमेय", "items": ["दोषाः: औषध से परे, पूरे शरीर में फैले", "आयुषः क्षयम्: आयु के क्षय को सूचित करते हैं",
                                         "अकस्मात् स्वभावविपर्यासं जनयन्ति"]}]},
        "chunks": ("स्वस्थनामातुराणां वा पुरुषाणां | देहांतराभिलाषिणामौषधविषयमतीताःसकलशरीरव्यापिनो दोषा | घनाघना इव वर्षम् | "
                   "आयुषः क्षयं सूचयंतो | ऽकस्मात्स्वभावविपर्य्यासं जनयंति"),
        "sandhi": ("अः + घोष व्यंजन → ओ: व्यापिनः + दोषाः → व्यापिनो दोषा · आः घोष ध्वनि से पहले विसर्ग खोता है: दोषाः + घनाघनाः → "
                   "दोषा घनाघना, घनाघनाः + इव → घनाघना इव · अः + अ → ओऽ: सूचयन्तः + अकस्मात् → सूचयन्तोऽकस्मात्।"),
    },
    "3": {
        "chain": {"steps": ["इकाई २: दोष अचानक स्वभाव उलट देते हैं", "तत्: वह (विपर्यास)", "समासतः: संक्षेप में",
                            "रिष्टम् इति आहुः: उसे रिष्ट कहते हैं"]},
        "chunks": "तत्समासतो | रिष्टमित्याहुः",
        "sandhi": "अः + घोष र → ओ: समासतः + रिष्टम् → समासतो रिष्टम् · इ + भिन्न स्वर → य्: इति + आहुः → इत्याहुः।",
    },
    "4": {
        "diagram": {"groups": [
            {"label": "देहप्रकृतिवर्णाः (छपे क्रम में)", "items": ["१ गौरः", "२ अगौरः", "३ श्यामः", "४ अश्यामः", "५ कृष्णः",
                                                              "६ अकृष्णः"]}]},
        "seesaw": "गौर ⇄ अगौर, श्याम ⇄ अश्याम, कृष्ण ⇄ अकृष्ण: तीनों जोड़े इसी इकाई में; दोनों पलड़े प्राकृत वर्ण।",
        "sandhi": "अः + अ → ओऽ: गौरः + अगौरः → गौरोऽगौरः · अ के अलावा स्वर से पहले अः → अ: अकृष्णः + इति → अकृष्ण इति।",
    },
    "5": {
        "chunks": "तद्भेदाश्च | पद्मगौरादयः",
        "sandhi": "घोष भ से पहले त् → द्: तत् + भेदाः → तद्भेदाः · च से पहले विसर्ग → श्: भेदाः + च → भेदाश्च · अ + आ → आ: पद्मगौर + आदयः → पद्मगौरादयः।",
        "anchors": "पक्का: पहला भेद पद्मगौर (कमल-सा गौर), ‘आदयः’ से सूची खुली। (मेरी याद-पद्धति)",
    },
    "6": {
        "diagram": {"groups": [
            {"label": "विकृतयः (छपे क्रम में)", "items": ["१ नील", "२ श्याम", "३ ताम्र", "४ हारिद्र", "५ शुक्ल", "आदि"]}]},
        "chunks": "नीलश्यामत्ताम्रहारिद्रशुक्लादयस्तु | विकृतयःतत्र | प्रकृतिविकृतिवर्णौ | युगपद्गंधेगैकदेशे वा | मरणाय",
        "anchors": "पक्का: पाँच विकृत वर्ण; ‘मरणाय’ = मृत्यु के लिए। अस्पष्ट: ‘युगपद्गंधेगैकदेशे’ वाली स्थिति। (मेरी याद-पद्धति)",
    },
    "7": {
        "seesaw": "शोक ⇄ हर्ष, रौक्ष्य ⇄ स्नेह: दोनों जोड़े इसी इकाई की सूची में; दोनों का बिना कारण बदलना कहा गया।",
        "chunks": ("एतेनम्लान्युरचयशोकहर्षरौक्ष्यस्नेहादयस्तथा | प्रकृतिभेदीयोक्तानां | महदुपचयसूक्ष्मदीर्घाणां | सर्वेषां च | "
                   "दोषादिभागेन | प्रतिनियतानांभावानामनिमित्ततोऽन्यथात्वमुक्तं भवति"),
        "sandhi": "स्वर से पहले त् → द्: महत् + उपचय → महदुपचय · अः + अ → ओऽ: अनिमित्ततः + अन्यथात्वम् → अनिमित्ततोऽन्यथात्वम्।",
    },
    "8": {
        "chunks": "छायास्तु | शरीरे | पंच",
        "sandhi": "त से पहले विसर्ग → स्: छायाः + तु → छायास्तु।",
        "pegs": "‘छाया पाँच, प्रभा सात’: पाँच उँगलियों की छाया, सात रंगों की प्रभा। (मेरा बनाया स्मरण-चित्र)",
    },
    "9": {
        "chain": {"steps": ["वातात्: वायु से", "१ पांशुभस्मरूक्षा: धूल-राख-सी रूखी", "२ रजोऽरुणा: धूल से लाल",
                            "३ श्यावा: गहरी भूरी", "४ निष्प्रभा: प्रभाहीन", "५ स्वेदमलगंधिः: पसीने-मल की गन्ध"]},
        "chunks": "तत्र खादम्लखङ्गाकाशनीलनिर्मला | सस्नेहा सप्रभेव || वातात्पांशुभस्मरूक्षा | रजोऽरुणा | श्यावा | निष्प्रभा | स्वेदमलगंधिः",
        "sandhi": "आ + इ → ए: सप्रभा + इव → सप्रभेव · अः + अ → ओऽ: रजः + अरुणा → रजोऽरुणा।",
    },
    "10": {
        "chunks": "तेजसोहुतहुताशविद्युतसतपनीयरक्ता | दृष्टिमुखा",
        "anchors": "पक्का: तेजस् (अग्नि) की छाया, ‘दृष्टिमुखा’। अस्पष्ट: बीच का लम्बा समास। (मेरी याद-पद्धति)",
        "sandhi": "अः + घोष ह → ओ: तेजसः + हुत- → तेजसो हुत-।",
    },
    "11": {
        "contrast": "अम्भस् (जल): वैदूर्य-सी निर्मल, घनी, अति स्निग्ध ⇄ भू (पृथ्वी): सुन्दर कान्ति, घनी, स्थिर, स्निग्ध, श्याम, श्वेत: दोनों इसी इकाई में।",
        "chunks": "अंभसो | वैदूर्येंद्रीलविमला | घना सुस्निग्धा || भुवो | रुचिराभा | घना स्थिरा | स्निग्धाशुद्धा | श्यामा श्वेता च",
        "sandhi": "अः + घोष व्यंजन → ओ: अम्भसः + वै- → अम्भसो, भुवः + रुचिराभा → भुवो रुचिराभा · अ + आ → आ: रुचिर + आभा → रुचिराभा।",
    },
    "12": {
        "seesaw": "वायव्या → विनाश और अति बड़ा क्लेश ⇄ शेषाः → सुखोदय: दोनों पलड़े इसी इकाई में।",
        "diagram": {"groups": [
            {"label": "सप्त प्रभाः (छपे क्रम में)", "items": ["१ रक्ता", "२ पीता", "३ पाण्डुरा", "४ सिता", "५ असिता", "६ श्यावा",
                                                         "७ हरिता"]}]},
        "sandhi": "अ + अ → आ: च + अतिमहते → चातिमहते · त से पहले विसर्ग → स्: शेषाः + तु → शेषास्तु · अ + उ → ओ: सुख + उदयाः → सुखोदयाः।",
    },
    "13": {
        "contrast": "स्निग्ध, विकाशी, अमल → शुभ ⇄ विपरीत → अशुभ: दोनों इसी इकाई में।",
        "chunks": "ताः स्निग्धा | विकाशिन्योऽमलाः | शुभाः | विपरीतास्त्वशुभाः",
        "sandhi": ("अः + अ → ओऽ: विकाशिन्यः + अमलाः → विकाशिन्योऽमलाः · त से पहले विसर्ग → स्: विपरीताः + तु → विपरीतास्तु · "
                   "उ + भिन्न स्वर → व्: तु + अशुभाः → त्वशुभाः।"),
    },
}

# ================================================================ IMAGE_SPECS
IMAGE_SPECS = {
    ("2", "diagram"): {
        "file": "sh9-ghanaghana-2.svg",
        "alt": ("Flowchart of card 2: clouds indicate rain; likewise doṣas beyond medicine indicate the decay of life and "
                "suddenly produce a reversal of the natural state."),
        "type": "mermaid",
        "code": ("flowchart LR\n"
                 "  A[\"घनाघनाः: बादल\"] --> B[\"वर्षा की सूचना\"]\n"
                 "  C[\"दोष: औषध से परे\"] --> D[\"आयु-क्षय की सूचना\"]\n"
                 "  C --> E[\"अचानक स्वभाव-विपर्यास\"]\n"),
    },
    ("4", "diagram"): {
        "file": "sh9-prakriti-varna-4.svg",
        "alt": ("Table of card 4: the three pairs of natural body colours in printed order: fair and not fair, dusky and "
                "not dusky, black and not black."),
        "type": "table",
        "title": "कार्ड ४: देह के प्राकृत वर्ण",
        "heads": ["वर्ण", "अ- रूप"],
        "rows": [["१ गौर: गोरा", "२ अगौर: जो गौर नहीं"], ["३ श्याम: साँवला", "४ अश्याम: जो श्याम नहीं"],
                 ["५ कृष्ण: काला", "६ अकृष्ण: जो कृष्ण नहीं"]],
    },
    ("6", "diagram"): {
        "file": "sh9-vikriti-varna-6.svg",
        "alt": ("Table of card 6 in printed order: the abnormal colours blue, dusky, copper-coloured, turmeric-yellow "
                "(standard identification) and white, and the like."),
        "type": "table",
        "title": "कार्ड ६: विकृत वर्ण (छपे क्रम में)",
        "heads": ["क्रम", "वर्ण"],
        "rows": [["१", "नील: नीला"], ["२", "श्याम: साँवला"], ["३", "ताम्र: ताँबे जैसा"],
                 ["४", "हारिद्र: हल्दी के रंग का (मानक)"], ["५", "शुक्ल: सफेद"], ["…", "आदि"]],
    },
    ("9", "chain"): {
        "file": "sh9-vata-chaya-9.svg",
        "alt": ("Chain of card 9, line 2, in printed order: the chāyā from wind is dry as dust and ash, reddish with dust, "
                "dark brown, lacking lustre, smelling of sweat-waste."),
        "type": "chain",
        "title": "कार्ड ९: वायु की छाया",
        "steps": ["वातात्: वायु से", "१ धूल-राख-सी रूखी", "२ धूल से लाल", "३ गहरी भूरी", "४ प्रभाहीन",
                  "५ पसीने-मल की गन्ध"],
    },
    ("11", "contrast"): {
        "file": "sh9-ambhas-bhu-11.svg",
        "alt": ("Split of card 11: the water chāyā is clear as vaidūrya (identity disputed), dense, very unctuous; the earth "
                "chāyā is of pleasing lustre, dense, steady, unctuous, dusky and white."),
        "type": "split",
        "title": "कार्ड ११: जल और पृथ्वी की छाया",
        "cols": [["अम्भस्: जल", ["वैदूर्य-सी निर्मल (विवादित पहचान)", "घनी", "अत्यन्त स्निग्ध"]],
                 ["भू: पृथ्वी", ["सुन्दर कान्ति", "घनी", "स्थिर", "स्निग्ध", "श्याम", "श्वेत"]]],
    },
    ("12", "seesaw"): {
        "file": "sh9-vayavya-12.svg",
        "alt": ("Flowchart of card 12: of the chāyās, the one of vāyu leads to destruction and very great affliction; the "
                "remaining ones lead to a rise of happiness."),
        "type": "mermaid",
        "code": ("flowchart TD\n"
                 "  A[\"पाँच छायाएँ\"] --> B[\"वायव्या: वायु की\"]\n"
                 "  A --> C[\"शेषाः: बाकी\"]\n"
                 "  B --> D[\"विनाश\"]\n"
                 "  B --> E[\"अति बड़ा क्लेश\"]\n"
                 "  C --> F[\"सुख का उदय\"]\n"),
    },
    ("12", "diagram"): {
        "file": "sh9-sapta-prabha-12.svg",
        "alt": ("Table of card 12 in printed order: the seven prabhās red, yellow, pale, white, black (literally not white), "
                "dark brown, green."),
        "type": "table",
        "title": "कार्ड १२: सात प्रभाएँ (छपे क्रम में)",
        "heads": ["क्रम", "प्रभा"],
        "rows": [["१", "रक्ता: लाल"], ["२", "पीता: पीली"], ["३", "पाण्डुरा: फीकी"], ["४", "सिता: सफेद"],
                 ["५", "असिता: काली (जो सित नहीं)"], ["६", "श्यावा: गहरी भूरी"], ["७", "हरिता: हरी"]],
    },
    ("13", "contrast"): {
        "file": "sh9-shubha-prabha-13.svg",
        "alt": ("Split of card 13: auspicious prabhās are unctuous, spreading and stainless; the opposite ones are "
                "inauspicious."),
        "type": "split",
        "title": "कार्ड १३: शुभ और अशुभ प्रभा",
        "cols": [["शुभ", ["स्निग्ध", "विकाशी: फैलने वाली", "अमल: निर्मल"]],
                 ["अशुभ", ["इनसे विपरीत"]]],
    },
}
