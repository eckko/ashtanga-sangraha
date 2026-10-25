from helpers import mcq, match, order, fill, multi, accepts


def T(q, teaches):
    q["teaches"] = teaches
    return q


AUTHORED = {}

# ---------------------------------------------------------------- unit 1
AUTHORED["1"] = {
    "title": "अथातो गर्भावक्रान्तिशारीरम्",
    "question": "What does the opening line of Śārīrasthāna chapter 2 announce that the speakers will explain?",
    "rule": ("अथ अतः गर्भावक्रान्तिशारीरम् व्याख्यास्यामः: now, therefore, we shall explain the Śārīra called "
             "Garbhāvakrānti, the descent (entry) of the embryo."),
    "limits": ("A stock opening formula. Garbhāvakrānti is the chapter's title; 'descent, entry of the embryo' is its "
               "literal sense. The line itself says nothing yet about how the embryo forms. The printed -क्रांति- "
               "with anusvara is only spelling for -क्रान्ति-."),
    "explain_hi": ("यह दूसरे अध्याय का आरम्भ-सूत्र है: ‘अब, इसलिए, हम गर्भावक्रान्ति शारीर की व्याख्या करेंगे।’ "
                   "‘गर्भावक्रान्ति’ = गर्भ + अवक्रान्ति, यानी गर्भ का उतरना या प्रवेश; यह अध्याय का नाम है। "
                   "‘व्याख्यास्यामः’ भविष्यत्-काल, उत्तम पुरुष बहुवचन है: ‘हम व्याख्या करेंगे’। "
                   "‘अथातो’ में दो सन्धियाँ हैं: अथ + अतः → अथातः (अ + अ → आ), और घोष ‘ग’ से पहले अतः → अतो।"),
    "hook": "अथातो … व्याख्यास्यामः: अब गर्भ के उतरने की बात।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "What does the opening line of chapter 2 say the speakers will explain?",
            ("The Garbhāvakrānti Śārīra, the descent of the embryo", "गर्भावक्रान्तिशारीरं व्याख्यास्यामः."),
            [("The Putrakāmīya Śārīra, on desiring a son", "That was chapter 1; this line names Garbhāvakrānti."),
             ("The signs of approaching death and decay", "The line names no such subject."),
             ("The daily care of the newborn child here", "The line names no such subject.")],
            "The line announces the Garbhāvakrānti Śārīra: the descent (entry) of the embryo.",
            "अथातो गर्भावक्रान्तिशारीरं व्याख्यास्यामः."),
        order(1, "Put the words of unit 1 in the line's order.",
              ["अथ", "अतः", "गर्भावक्रान्तिशारीरम्", "व्याख्यास्यामः"],
              "Now, therefore, the Garbhāvakrānti Śārīra, we shall explain.",
              "अथ → अतः → गर्भावक्रान्तिशारीरम् → व्याख्यास्यामः."),
        match(2, "Match each word of unit 1 to its meaning.",
              [["अथ", "now"], ["अतः", "therefore"], ["गर्भ", "embryo"],
               ["अवक्रान्ति", "descent, entry"], ["व्याख्यास्यामः", "we shall explain"]],
              "These words make the whole opening formula.",
              "अथ, अतः, गर्भ, अवक्रान्ति, व्याख्यास्यामः.", role="extend",
              teaches="गर्भावक्रान्ति = गर्भ (embryo) + अवक्रान्ति (descent, entry), joined by अ + अ → आ."),
        mcq("discriminate", 3, "Which split of अथातो is right?",
            ("अथ + अतः", "अ + अ → आ gives अथातः; before the voiced ग, अतः is written अतो."),
            [("अथा + तः", "तः alone is not a word of the card."),
             ("अथः + अतः", "There is no word अथः; the particle is अथ."),
             ("अथ + आतः", "आतः is not a word of the card; the word is अतः, therefore.")],
            "अथ (now) + अतः (therefore): अ + अ → आ.",
            "अ + अ → आ."),
        mcq("apply", 4, "Why is अतः written अतो in अथातो गर्भावक्रान्ति…?",
            ("-अः becomes -ओ before a voiced consonant such as ग", "ग is voiced, so -अः → -ओ."),
            [("-अः becomes -ओ before every consonant", "Before a voiceless consonant -अः does not become -ओ."),
             ("The ओ shows that अतः is a dual form here", "अतः is an indeclinable; it has no dual."),
             ("The ओ is a misprint that the data corrects", "The data marks no misprint here; it is regular sandhi.")],
            "अतः + गर्भ… → अतो गर्भ…: -अः → -ओ before a voiced consonant.",
            "-अः → -ओ before a voiced consonant."),
        mcq("transfer", 5, "By the rule of अथ + अतः, how is तत्र + अपि (even there) written when joined?",
            ("तत्रापि", "अ + अ → आ, as in अथ + अतः → अथातः."),
            [("तत्रेपि", "अ + अ does not give ए."),
             ("तत्रोपि", "अ + अ does not give ओ."),
             ("तत्रपि", "One अ is not simply dropped; the two make long आ.")],
            "तत्र + अपि = तत्रापि, like अथ + अतः = अथातः.",
            "Short अ + short अ → long आ.",
            teaches="Two short अ sounds meeting at a word joint become one long आ: अथ + अतः → अथातः."),
    ],
}

# ---------------------------------------------------------------- unit 2
AUTHORED["2"] = {
    "title": "गते पुराणे रजसि नवेऽवस्थिते",
    "question": "By unit 2, under what conditions, and joined with what, does the śukra reach the womb?",
    "rule": ("When old rajas has gone, new rajas is established, and womb and passage are clean, unaltered śukra, "
             "impelled by unaltered vāyu, followed by the other great elements, mingled with ārtava and joined with "
             "the jīva, goes to the womb."),
    "limits": ("One long prose sentence. अन्वक्षम् is unclear (probably 'at once'); no question uses it. The jīva "
               "(living soul) is a doctrinal term with no modern equivalent. The line does not say what the other great "
               "elements do beyond following. The print's वशांनुवर्तिना has a possibly needless anusvara (वशानुवर्तिना)."),
    "explain_hi": ("यह एक लम्बा गद्य-वाक्य है। पहले सप्तमी में शर्तें आती हैं: पुराना रज चला गया हो, नया रज स्थित हो, "
                   "गर्भाशय (आशय) और मार्ग शुद्ध हों। फिर कर्ता ‘शुक्रम्’ (वीर्य) अपने विशेषणों के साथ: बीज-रूप, अविकृत, "
                   "अविकृत वायु से प्रेरित, अन्य महाभूतों से अनुगत, आर्तव (स्त्री का रज) से मिला हुआ। "
                   "वह जीव से संयुक्त होता है; जीव राग आदि क्लेशों के वश चलने वाला, अपने कर्म से प्रेरित और मन के समान वेग वाला है। "
                   "अन्त में क्रिया: ‘गर्भाशयम् उपयाति’, गर्भाशय में पहुँचता है। "
                   "‘अन्वक्षम्’ का अर्थ अनिश्चित है (सम्भवतः ‘तुरन्त’)।"),
    "hook": "शर्तें पहले, फिर शुक्र + वायु + महाभूत + आर्तव + जीव → गर्भाशय।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 2, where does the śukra finally go?",
            ("To the womb (garbhāśaya)", "गर्भाशयम् उपयाति = goes to the womb."),
            [("Out of the body again", "The verb उपयाति says it goes to, reaches."),
             ("Into the heart (hṛdaya)", "The heart is not named in this unit."),
             ("Into the channels of rajas", "No channels are named in this unit.")],
            "The sentence ends गर्भाशयमुपयाति: it goes to the womb.",
            "शुक्रम् … गर्भाशयम् उपयाति."),
        order(1, "Put these phrases about the śukra in unit 2 in the text's order.",
              ["बीजात्मना शुक्रम् अविकृतम्", "अविकृतेन वायुना प्रेरितम्", "अन्यैः महाभूतैः अनुगतम्",
               "आर्तवेन अभिमूर्च्छितम्", "जीवेन अभिसंसृष्टम्", "गर्भाशयम् उपयाति"],
              "Seed-form unaltered śukra, impelled by wind, followed by the elements, mingled with ārtava, joined with the jīva, goes to the womb.",
              "शुक्र → वायु → महाभूत → आर्तव → जीव → गर्भाशय."),
        match(2, "Match each participle of unit 2 to its meaning.",
              [["प्रेरितम्", "impelled"], ["अनुगतम्", "followed"], ["अभिमूर्च्छितम्", "mingled, combined"],
               ["अभिसंसृष्टम्", "joined, united"], ["उपयाति", "goes to, reaches"]],
              "Four past participles describe the śukra; उपयाति is the main verb.",
              "प्रेरित, अनुगत, अभिमूर्च्छित, अभिसंसृष्ट; उपयाति.", role="extend",
              teaches="Each participle takes its agent or partner in the instrumental: वायुना प्रेरितम् = impelled by wind (agent), आर्तवेन अभिमूर्च्छितम् = mingled with ārtava (partner)."),
        mcq("discriminate", 3, "Which phrase of unit 2 describes the jīva, not the śukra?",
            ("मनोजवेन: swift as the mind", "मनोजवेन is instrumental, like जीवेन; the data calls it a qualifier of the jīva."),
            [("बीजात्मना: in the form of seed", "This describes the śukra (बीजात्मना शुक्रम्)."),
             ("आर्तवेन अभिमूर्च्छितम्: mingled with ārtava", "अभिमूर्च्छितम् is neuter nominative, agreeing with शुक्रम्."),
             ("अन्यैः महाभूतैः अनुगतम्: followed by the elements", "अनुगतम् is neuter nominative, agreeing with शुक्रम्.")],
            "The jīva's qualifiers are instrumentals: रागादिक्लेशवशानुवर्तिना, स्वकर्मचोदितेन, मनोजवेन.",
            "jīva: swift as mind, impelled by own karma, under the sway of passion and the other afflictions."),
        multi("apply", 4, "Which conditions does unit 2 state before the śukra goes to the womb?",
              [("The old rajas has gone", "Right: गते पुराणे (रजसि)."),
               ("The woman has fasted beforehand", "No fasting is named in this unit."),
               ("The passage (मार्ग) is blocked", "The text says the passage is clean (शुद्धे … मार्गे)."),
               ("The new rajas is established", "Right: नवे अवस्थिते.")],
              [0, 3],
              "Old rajas gone, new rajas established, womb and passage clean: these are the conditions.",
              "गते पुराणे रजसि नवेऽवस्थिते शुद्धे गर्भस्याशये मार्गे च."),
        mcq("transfer", 5, "By the rule of महाभूतैरनुगतम्, how is देवैः + अर्चितम् (worshipped by the gods) written?",
            ("देवैरर्चितम्", "Visarga after ऐ becomes र् before a vowel, as महाभूतैः + अनुगतम्."),
            [("देवैशर्चितम्", "श् stands for visarga only before च, छ, श."),
             ("देवैर्चितम्", "The अ of अर्चितम् cannot be lost."),
             ("देवोऽर्चितम्", "ओऽ comes only from -अः, not from -ऐः.")],
            "देवैः + अर्चितम् = देवैरर्चितम्, like महाभूतैः + अनुगतम् = महाभूतैरनुगतम्.",
            "Visarga after a vowel other than अ/आ → र् before a vowel.",
            teaches="Visarga after a vowel other than अ or आ becomes र् before a vowel: महाभूतैः + अनुगतम् → महाभूतैरनुगतम्."),
    ],
}

# ---------------------------------------------------------------- unit 3
AUTHORED["3"] = {
    "title": "कार्याणां च कारणानुविधायित्वात्",
    "question": "By unit 3, why does the embryo take on the nature of its cause?",
    "rule": ("कार्याणां च कारणानुविधायित्वात् तत्स्वभावतां प्रतिपद्यते: and because effects follow their causes, it "
             "attains the nature of that (cause). The subject, the embryo, is carried from unit 2."),
    "limits": ("The line names neither the subject nor the cause; 'it' (the embryo) is understood from unit 2. The print "
               "runs त्त्त्स्वभावतां together; -त्वात् + तत्स्वभावताम् is a correction the sense requires (possible). "
               "No question uses the printed form."),
    "explain_hi": ("यह एक सामान्य सिद्धान्त है: कार्य अपने कारण का अनुसरण करते हैं, इसलिए वह उसी (कारण) के स्वभाव को प्राप्त होता है। "
                   "कर्ता लिखा नहीं गया; पिछली इकाई से ‘गर्भ’ समझा जाता है। "
                   "‘कारणानुविधायित्वात्’ में -त्व से भाववाचक संज्ञा बनी और ‘-त्वात्’ पंचमी है, जो कारण बताती है: ‘अनुसरण करने के कारण’। "
                   "छपे पाठ में तीन ‘त्’ एक साथ हैं; ‘तत्’ का ‘अ’ छूटा लगता है; अर्थ के आधार पर ‘-त्वात् तत्स्वभावताम्’ पढ़ना सम्भावित सुधार है।"),
    "hook": "जैसा कारण, वैसा कार्य: गर्भ कारण का स्वभाव पाता है।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 3, whose nature does the embryo attain?",
            ("The nature of its cause", "तत्स्वभावताम्: the nature of that (cause)."),
            [("The nature of the mother alone", "The line names no mother."),
             ("The nature of the season", "The line names no season."),
             ("A nature opposite to its cause", "Effects follow their causes; nothing opposite is said.")],
            "Because effects follow causes, it attains the nature of that cause.",
            "कार्य कारण का अनुसरण करते हैं."),
        match(1, "Match each word of unit 3 to its meaning.",
              [["कार्याणाम्", "of effects"], ["कारण", "cause"], ["अनुविधायित्वात्", "from conformity, following"],
               ["स्वभावताम्", "the having of the nature"], ["प्रतिपद्यते", "attains"]],
              "Effects follow causes, so it attains that nature.",
              "कार्य, कारण, अनुविधायित्व, स्वभावता, प्रतिपद्यते."),
        order(2, "Put the words of unit 3 in the line's order, as corrected.",
              ["कार्याणाम्", "च", "कारणानुविधायित्वात्", "तत्स्वभावताम्", "प्रतिपद्यते"],
              "Of effects, and, because of following the cause, the nature of that, attains.",
              "कार्याणाम् → च → कारणानुविधायित्वात् → तत्स्वभावताम् → प्रतिपद्यते.", role="extend",
              teaches="-त्वात् is the ablative of a -त्व abstract noun and gives the reason: because of following the cause."),
        mcq("discriminate", 3, "What does the ending -त्वात् in कारणानुविधायित्वात् express?",
            ("A reason: because of following the cause", "The card labels it an ablative; here it gives the reason."),
            [("A place: in the following of the cause", "That would need a locative, -त्वे."),
             ("An owner: of the following of the cause", "That would need a genitive, -त्वस्य."),
             ("A goal: for the following of the cause", "That would need a dative, -त्वाय.")],
            "-त्वात् = ablative: because of.",
            "Ablative -आत् of an abstract can give the reason."),
        mcq("apply", 4, "Which split of कारणानुविधायित्वात् is right?",
            ("कारण + अनुविधायित्वात्", "अ + अ → आ: कारण + अनु… = कारणानु…."),
            [("कारणा + नुविधायित्वात्", "नुविधायित्व is not a word."),
             ("कारणम् + अनुविधायित्वात्", "Then the म् would show: कारणमनु…."),
             ("कारणे + अनुविधायित्वात्", "ए + अ would give कारणेऽनु…, not कारणानु….")],
            "कारण (cause) + अनुविधायित्वात् (because of following).",
            "अ + अ → आ."),
        mcq("transfer", 5, "In the invented sentence शिला गुरुत्वाज्जले मज्जति (गुरुत्वात् + जले) (the stone sinks in water), what does गुरुत्वात् mean?",
            ("Because of its heaviness", "-त्वात् gives the reason, as कारणानुविधायित्वात्."),
            [("In its heaviness", "A locative would be गुरुत्वे."),
             ("Of its heaviness", "A genitive would be गुरुत्वस्य."),
             ("For its heaviness", "A dative would be गुरुत्वाय.")],
            "गुरु (heavy) + -त्व (-ness), ablative -त्वात्: because of heaviness.",
            "-त्वात् = because of being X.",
            teaches="-त्व makes an abstract noun (being X); its ablative -त्वात् gives the reason: because of being X."),
    ],
}

# ---------------------------------------------------------------- unit 4
AUTHORED["4"] = {
    "title": "शुक्रस्य बाहुल्यात् पुमान्",
    "question": "By unit 4, what decides whether the offspring is male, female or napuṃsaka?",
    "rule": ("Abundance of śukra gives a male, abundance of ārtava a female, and equality of the two a napuṃsaka "
             "(neither male nor female). ततः एव, for that very reason, ties it to unit 3."),
    "limits": ("No verb is printed; 'arises' is only understood. napuṃsaka is kept as the text's third category; no single "
               "modern equivalent is asserted. The line gives no measure of abundance and no advice."),
    "explain_hi": ("इसी कारण (कार्य कारण का अनुसरण करता है) तीन परिणाम बताए गए हैं: शुक्र की अधिकता से पुरुष, "
                   "आर्तव की अधिकता से स्त्री, और दोनों की समता से नपुंसक। "
                   "‘बाहुल्यात्’ पंचमी है (अधिकता से) और ‘साम्येन’ तृतीया (समता से); दोनों कारण बताते हैं। "
                   "वाक्य में क्रिया नहीं है। ‘नपुंसक’ शब्दशः ‘न पुरुष’ है; इसका कोई एक आधुनिक पर्याय नहीं दिया गया। "
                   "‘ततएव’ छपा है: ततः + एव → तत एव (अ के बाद विसर्ग स्वर से पहले लुप्त, बीच का अन्तर रहता है)।"),
    "hook": "शुक्र अधिक → पुरुष, आर्तव अधिक → स्त्री, बराबर → नपुंसक।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 4, what follows from the abundance of ārtava?",
            ("A female offspring", "आर्तवस्य बाहुल्यात् स्त्री."),
            [("A male offspring", "A male comes from the abundance of śukra."),
             ("A napuṃsaka", "A napuṃsaka comes from the equality of the two."),
             ("A miscarriage", "No miscarriage is named in this unit.")],
            "Abundance of ārtava gives a female.",
            "आर्तवस्य बाहुल्यात् स्त्री."),
        match(1, "Match each cause in unit 4 to its result.",
              [["शुक्रस्य बाहुल्यात्", "a male"], ["आर्तवस्य बाहुल्यात्", "a female"],
               ["तयोः साम्येन", "a napuṃsaka"]],
              "Three causes, three results, in this order.",
              "शुक्र → पुमान्, आर्तव → स्त्री, साम्य → नपुंसकम्."),
        order(2, "Put the phrases of unit 4 in the line's order.",
              ["ततः एव च", "शुक्रस्य बाहुल्यात् पुमान्", "आर्तवस्य बाहुल्यात् स्त्री", "तयोः साम्येन नपुंसकम्"],
              "For that very reason: male, then female, then napuṃsaka.",
              "ततः एव → पुमान् → स्त्री → नपुंसकम्.", role="extend",
              teaches="बाहुल्यात् (ablative, from abundance) and साम्येन (instrumental, by equality) both give the cause."),
        mcq("discriminate", 3, "In unit 4, what does तयोः (of the two) refer to?",
            ("Śukra and ārtava", "The two just named: शुक्रस्य … आर्तवस्य."),
            [("The male and female offspring", "They are the results, not the two whose equality is meant."),
             ("Vāyu and the great elements", "Neither is named in this unit."),
             ("The old and the new rajas", "Rajas is not named in this unit.")],
            "तयोः साम्येन = by the equality of the two, śukra and ārtava.",
            "तयोः = of the two (śukra, ārtava)."),
        mcq("apply", 4, "The print has ततएव. Which split is right?",
            ("ततः + एव", "After -अ, visarga drops before a vowel other than अ: तत एव."),
            [("तत् + एव", "That would give तदेव."),
             ("तत + एव", "अ + ए would join into ऐ: ततैव."),
             ("ततम् + एव", "That would give ततमेव.")],
            "ततः (from that) + एव (indeed) → तत एव.",
            "-अः + vowel other than अ → -अ, with a gap."),
        mcq("transfer", 5, "By the rule of ततः + एव, how is रामः + इति written?",
            ("राम इति", "-अः drops its visarga before इ and the gap stays, as तत एव."),
            [("रामो इति", "-अः → -ओ only before a voiced consonant, or before अ as ओऽ."),
             ("रामेति", "Once the visarga drops, the vowels do not join again."),
             ("रामरिति", "र् replaces visarga only after vowels other than अ/आ.")],
            "रामः + इति = राम इति, like ततः + एव = तत एव.",
            "-अः + vowel other than अ → -अ + gap.",
            teaches="After अ, a visarga is dropped before any vowel except अ, and the vowels then stay apart: ततः + एव → तत एव."),
    ],
}

# ---------------------------------------------------------------- unit 5
AUTHORED["5"] = {
    "title": "शुक्रार्तवेऽनिलेन खण्डशो भिन्ने",
    "question": "By unit 5, what happens when anila (Vāta) splits śukra and ārtava into pieces?",
    "rule": ("When śukra and ārtava are split into pieces by anila (Vāta), offspring come into being according "
             "to the divisions (यथाविभागम्)."),
    "limits": ("The line gives no number of offspring; 'offspring' is plural only, and twins are not named. No verb "
               "is printed: उत्पत्तिः stands as a nominal sentence. Unit 6 appears to continue this line."),
    "explain_hi": ("जब शुक्र और आर्तव वायु (अनिल) द्वारा टुकड़ों में बँट जाते हैं, तब विभाग के अनुसार सन्तानों की उत्पत्ति होती है। "
                   "‘शुक्रार्तवे … भिन्ने’ सप्तमी है: ‘बँट जाने पर’। ‘यथाविभागम्’ अव्ययीभाव है: ‘विभाग के अनुसार’। "
                   "‘अपत्यानाम्’ बहुवचन है, पर कितनी सन्तानें, यह नहीं कहा गया। "
                   "छपे वाक्य में क्रिया नहीं; हिन्दी का ‘होती है’ समझा हुआ है। अगली इकाई इसी को आगे बढ़ाती दिखती है।"),
    "hook": "वायु ने बाँटा, जितने भाग उतनी सन्तानें: यथाविभागम्।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 5, what splits śukra and ārtava into pieces?",
            ("Anila (Vāta)", "अनिलेन = by anila (Vāta)."),
            [("The jīva", "The jīva is named in unit 2, not here."),
             ("The mother's food", "No food is named in this unit."),
             ("The great elements", "The elements are named in unit 2, not here.")],
            "शुक्रार्तवेऽनिलेन खण्डशो भिन्ने: split into pieces by anila (Vāta).",
            "अनिलेन = by anila (Vāta)."),
        order(1, "Put the words of unit 5 in the line's order.",
              ["शुक्रार्तवे", "अनिलेन", "खण्डशः", "भिन्ने", "यथाविभागम्", "अपत्यानाम् उत्पत्तिः"],
              "Śukra-ārtava, by anila, in pieces, split: according to division, the origin of offspring.",
              "शुक्रार्तवे → अनिलेन → खण्डशः → भिन्ने → यथाविभागम् → अपत्यानाम् उत्पत्तिः."),
        match(2, "Match each word of unit 5 to its meaning.",
              [["अनिलेन", "by anila (Vāta)"], ["खण्डशः", "in pieces"], ["भिन्ने", "split, divided"],
               ["यथाविभागम्", "according to the division"], ["अपत्यानाम्", "of offspring"]],
              "Split by anila (Vāta) into pieces, offspring arise according to the divisions.",
              "अनिल, खण्डशः, भिन्न, यथाविभागम्, अपत्य.", role="extend",
              teaches="अनिल (unit 5) is a name of the doṣa Vāta, as the data glosses it."),
        mcq("discriminate", 3, "Which split of शुक्रार्तवेऽनिलेन is right?",
            ("शुक्रार्तवे + अनिलेन", "ए + अ → एऽ: the ऽ marks the lost अ of अनिलेन."),
            [("शुक्रार्तवे + निलेन", "निलेन is not a word; the ऽ shows an अ was lost."),
             ("शुक्रार्तवः + अनिलेन", "-अः + अ would give शुक्रार्तवोऽनिलेन."),
             ("शुक्रार्तवम् + अनिलेन", "Then the म् would show: शुक्रार्तवमनिलेन.")],
            "शुक्रार्तवे (locative) + अनिलेन (by anila): ए + अ → एऽ.",
            "ए + अ → एऽ."),
        multi("apply", 4, "Which does unit 5 state?",
              [("Exactly two offspring arise", "No number is given; अपत्यानाम् is only plural."),
               ("Śukra and ārtava are split into pieces", "Right: खण्डशो भिन्ने."),
               ("The splitting is done by the jīva", "The agent is अनिल, Vāta."),
               ("The splitting is done by anila (Vāta)", "Right: अनिलेन.")],
              [1, 3],
              "Split into pieces by anila (Vāta); offspring arise according to the divisions, no number stated.",
              "शुक्रार्तवेऽनिलेन खण्डशो भिन्ने यथाविभागमपत्यानामुत्पत्तिः."),
        mcq("transfer", 5, "By the pattern of यथाविभागम्, what does यथाशक्ति mean?",
            ("According to one's strength", "यथा + noun = according to X, like यथाविभागम्."),
            [("Without any strength", "That would need a negative, not यथा."),
             ("Beyond one's strength", "यथा does not mean beyond."),
             ("Because of one's strength", "यथा does not give a reason.")],
            "यथा + शक्ति = according to (one's) strength, as यथा + विभाग = according to the division.",
            "यथा- compound (avyayībhāva) = according to X.",
            teaches="यथा + a noun makes an indeclinable compound meaning according to X: यथाविभागम्, according to the division."),
    ],
}

# ---------------------------------------------------------------- unit 6
AUTHORED["6"] = {
    "title": "विकृते वियोन्याकृतीनाम्",
    "question": "What does unit 6 add about the case when (the factors) are vitiated?",
    "rule": ("विकृते वियोन्याकृतीनाम्: when vitiated, (the origin) of those with the forms of other wombs. It appears to "
             "continue unit 5, carrying over उत्पत्तिः (origin)."),
    "limits": ("Two words only, no verb. What is vitiated (śukra-ārtava of unit 5, or anila, Vāta) is not stated. Whether "
               "'forms of other wombs' means animal-like shapes is not said. The link to unit 5 is the data's grouping "
               "('appears to')."),
    "explain_hi": ("इस इकाई में केवल दो शब्द हैं: ‘विकृते’ (विकृत होने पर) और ‘वियोन्याकृतीनाम्’ (अन्य योनि के आकारों वालों की)। "
                   "डेटा के अनुसार यह इकाई ५ को आगे बढ़ाती दिखती है, यानी ‘उत्पत्तिः’ वहीं से समझा जाता है: "
                   "विकृत होने पर अन्य योनि के आकार वालों की उत्पत्ति। "
                   "क्या विकृत होता है (शुक्र-आर्तव या वायु), यह नहीं कहा गया; ‘अन्य योनि’ का अर्थ पशु-आकार है या नहीं, यह भी नहीं। "
                   "सन्धि: वियोनि + आकृतीनाम् → वियोन्याकृतीनाम् (इ + आ → या)।"),
    "hook": "विकृत हुआ तो आकार भी अन्य योनि जैसा: विकृते वियोन्याकृतीनाम्।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "Unit 6 opens with विकृते. What does it mean?",
            ("When vitiated", "The card glosses विकृते as when vitiated."),
            [("When healthy", "विकृत is the opposite of unaltered (अविकृत)."),
             ("When divided in pieces", "That is भिन्ने in unit 5."),
             ("When established", "That is अवस्थिते in unit 2.")],
            "विकृते = when vitiated (locative of the participle विकृत).",
            "विकृते = when vitiated."),
        match(1, "Match each part of unit 6 to its meaning.",
              [["विकृते", "when vitiated"], ["वि-", "different, other"], ["योनि", "womb"], ["आकृति", "form, shape"]],
              "When vitiated: of the forms of other wombs.",
              "विकृते; वि- + योनि + आकृति."),
        T(mcq("extend", 2, "Which split of वियोन्याकृतीनाम् is right?",
              ("वियोनि + आकृतीनाम्", "इ before a different vowel becomes य्: इ + आ → या."),
              [("वियोनि + अकृतीनाम्", "इ + अ would give वियोन्यकृतीनाम्, with short य."),
               ("वियोनिः + आकृतीनाम्", "Visarga after इ would become र्: वियोनिराकृतीनाम्."),
               ("वियोन + याकृतीनाम्", "Neither part is a word.")],
              "वियोनि (other womb) + आकृतीनाम् (of forms).",
              "इ + आ → या."),
          "इ before a different vowel becomes य्: वियोनि + आकृतीनाम् → वियोन्याकृतीनाम्."),
        mcq("discriminate", 3, "In unit 6, what case is वियोन्याकृतीनाम्?",
            ("Genitive plural: of the forms", "-ईनाम् is the genitive plural; the card glosses it of forms."),
            [("Nominative plural: the forms", "That would be -आकृतयः."),
             ("Locative singular: in the form", "That would be -आकृतौ."),
             ("Instrumental plural: by the forms", "That would be -आकृतिभिः.")],
            "वियोन्याकृतीनाम् = of the forms of other wombs: genitive plural.",
            "-ईनाम् = genitive plural."),
        multi("apply", 4, "Which are true of unit 6, by the card?",
              [("विकृते is a locative: when vitiated", "Right: locative of the participle विकृत."),
               ("It names what is vitiated", "What is vitiated is not stated."),
               ("वियोन्याकृतीनाम् is genitive plural: of the forms", "Right: -ईनाम्, genitive plural."),
               ("It says the forms are animal forms", "That is not stated and is not added.")],
              [0, 2],
              "विकृते = when vitiated; वियोन्याकृतीनाम् = of the forms of other wombs. What is vitiated, and what the forms are, is not said.",
              "विकृते वियोन्याकृतीनाम्."),
        mcq("transfer", 5, "By the rule of वियोन्याकृतीनाम्, how is इति + आह (he said thus) written?",
            ("इत्याह", "इ + आ → या, as वियोनि + आकृतीनाम्."),
            [("इताह", "The इ is not dropped; it becomes य्."),
             ("इत्येह", "इ + आ does not give ये."),
             ("इतेह", "इ + आ does not give ए.")],
            "इति + आह = इत्याह, like वियोनि + आकृतीनाम् = वियोन्याकृतीनाम्.",
            "इ + unlike vowel → य् + vowel.",
            teaches="इ before an unlike vowel becomes य्: इति + आह → इत्याह."),
    ],
}

# ---------------------------------------------------------------- unit 7
AUTHORED["7"] = {
    "title": "सद्योगृहीतगर्भायाः लिङ्गम्",
    "question": "By unit 7, what are the signs of a woman who has just conceived?",
    "rule": ("Signs of a woman who has just conceived: taking in of the seed by the yoni, satisfaction, heaviness, "
             "throbbing, and continued connection (अनुबन्ध) of śukra and ārtava."),
    "limits": ("योन्या is read as instrumental, by the yoni; a genitive, of the yoni, is possible and the sense changes "
               "little. The line lists signs only; it gives no test, timing or advice. अथनार्याः = अथ नार्याः (spacing, certain)."),
    "explain_hi": ("‘अब सद्यः गर्भ धारण की हुई स्त्री का लक्षण’: योनि द्वारा बीज का ग्रहण, तृप्ति, भारीपन (गुरिमा), "
                   "फड़कना (स्फुरण) और शुक्र-आर्तव का अनुबन्ध (लगातार जुड़ाव)। "
                   "‘सद्योगृहीतगर्भा’ बहुव्रीहि है: सद्यः (अभी) + गृहीत (ग्रहण किया) + गर्भा = जिसने अभी गर्भ धारण किया है। "
                   "‘योन्या’ तृतीया मानी गई; षष्ठी पठन भी सम्भव है, अर्थ लगभग वही रहता है। "
                   "आगे इकाई ९ प्रकट गर्भ के लक्षण देती है।"),
    "hook": "अभी गर्भ: बीज-ग्रहण, तृप्ति, गुरिमा, स्फुरण, अनुबन्ध।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "Whose signs does unit 7 list?",
            ("A woman who has newly conceived", "सद्योगृहीतगर्भायाः = of her who has just now conceived."),
            [("A woman whose pregnancy is manifest", "That is unit 9 (व्यक्तगर्भायाः)."),
             ("A woman in her monthly flow", "No flow is named in this unit."),
             ("A woman near her delivery", "No delivery is named in this unit.")],
            "The signs are of the woman who has just conceived.",
            "सद्योगृहीतगर्भा = she who has just conceived."),
        order(1, "Put the signs of unit 7 in the text's order.",
              ["योन्या बीजग्रहणम्", "तृप्तिः", "गुरिमा", "स्फुरणम्", "शुक्रार्तवयोः अनुबन्धः"],
              "Seed taken in, satisfaction, heaviness, throbbing, continued connection.",
              "बीजग्रहण → तृप्ति → गुरिमा → स्फुरण → अनुबन्ध."),
        match(2, "Match each sign of unit 7 to its meaning.",
              [["बीजग्रहणम्", "taking in of the seed"], ["तृप्तिः", "satisfaction"], ["गुरिमा", "heaviness"],
               ["स्फुरणम्", "throbbing, quivering"], ["अनुबन्धः", "continued connection"]],
              "Five signs of a woman who has just conceived.",
              "बीजग्रहण, तृप्ति, गुरिमा, स्फुरण, अनुबन्ध.", role="extend",
              teaches="सद्योगृहीतगर्भा = सद्यः (just now) + गृहीत (taken) + गर्भ: a bahuvrīhi, she who has just conceived."),
        mcq("discriminate", 3, "What does सद्यः in सद्योगृहीतगर्भा mean?",
            ("A moment ago, newly", "The card glosses सद्यः as just now."),
            [("Gradually", "Gradually is क्रमेण, in unit 9."),
             ("Long ago", "सद्यः is the opposite: just now."),
             ("With difficulty", "No such word is in the compound.")],
            "सद्यः = just now; with गृहीतगर्भा, she who has just conceived.",
            "सद्यः = just now."),
        multi("apply", 4, "Which are signs named in unit 7?",
              [("Swelling of the feet (पादशोथ)", "That is named in unit 9, not here."),
               ("Craving for the sour (अम्लकामिता)", "That is named in unit 9, not here."),
               ("Heaviness (गुरिमा)", "Right: गुरिमा is in the list."),
               ("Throbbing (स्फुरणम्)", "Right: स्फुरणम् is in the list.")],
              [2, 3],
              "Unit 7: seed taken in, satisfaction, heaviness, throbbing, connection.",
              "Unit 7 = just conceived; unit 9 = manifest pregnancy."),
        mcq("transfer", 5, "By the rule of तृप्तिर्गुरिमा, how is मतिः + गता (the mind has gone) written?",
            ("मतिर्गता", "Visarga after इ becomes र् before a voiced sound, as तृप्तिः + गुरिमा."),
            [("मतिस्गता", "स् stands for visarga only before त, थ."),
             ("मतिश्गता", "श् stands for visarga only before च, छ, श."),
             ("मतिगता", "After इ the visarga is not simply dropped.")],
            "मतिः + गता = मतिर्गता, like तृप्तिः + गुरिमा = तृप्तिर्गुरिमा.",
            "-इः → -इर् before a voiced sound.",
            teaches="Visarga after इ (or another vowel than अ/आ) becomes र् before a voiced sound: तृप्तिः + गुरिमा → तृप्तिर्गुरिमा."),
    ],
}

# ---------------------------------------------------------------- unit 8
AUTHORED["8"] = {
    "title": "तंद्राऽंगसादः प्रसेको",
    "question": "Which further signs does unit 8 add, and which of its words are doubtful?",
    "rule": ("Likewise (तथा) further signs: on a conjectural reading joy and nausea, then drowsiness, limb-weariness, "
             "flow (praseka), heart-distress (conjectural), exhaustion and thirst."),
    "limits": ("Confidence low. Three printed words are doubtful: महर्षो (perhaps प्रहर्ष or महाहर्ष, joy), हृल्लाभ "
               "(probably हृल्लास, nausea) and हृदयन्पथा (probably हृदयव्यथा). No question uses them. प्रसेक is kept as "
               "'flow, trickling'; what flows is not said."),
    "explain_hi": ("‘तथा’ से पिछली इकाई के लक्षणों की सूची आगे बढ़ती है। निश्चित शब्द: तन्द्रा (ऊँघ), अङ्गसाद (अंगों की शिथिलता), "
                   "प्रसेक (बहाव), ग्लानि (थकावट) और पिपासा (प्यास)। "
                   "तीन छपे शब्द संदिग्ध हैं: ‘महर्षो’ (सम्भवतः हर्ष), ‘हृल्लाभ’ (सम्भवतः हृल्लास, जी मिचलाना) और "
                   "‘हृदयन्पथा’ (सम्भवतः हृदयव्यथा, हृदय की पीड़ा)। इनका अनुवाद ‘अनुमानित पाठ पर’ है, इसलिए इन पर कोई प्रश्न नहीं। "
                   "‘प्रसेक’ का अर्थ केवल बहाव है; किसका बहाव, यह नहीं कहा गया।"),
    "hook": "तन्द्रा, अङ्गसाद, प्रसेक … ग्लानि, पिपासा।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "Which word in unit 8 means thirst?",
            ("पिपासा", "The card glosses पिपासा as thirst."),
            [("ग्लानिः", "ग्लानिः is exhaustion."),
             ("तन्द्रा", "तन्द्रा is drowsiness."),
             ("प्रसेकः", "प्रसेकः is flow, trickling.")],
            "पिपासा = thirst, near the end of the list.",
            "पिपासा = thirst."),
        match(1, "Match each sure word of unit 8 to its meaning.",
              [["तन्द्रा", "drowsiness"], ["अङ्गसादः", "weariness of the limbs"], ["प्रसेकः", "flow, trickling"],
               ["ग्लानिः", "exhaustion"], ["पिपासा", "thirst"]],
              "These five words are sure; the doubtful ones are left out.",
              "तन्द्रा, अङ्गसाद, प्रसेक, ग्लानि, पिपासा."),
        order(2, "Put these sure words of unit 8 in the text's order.",
              ["तन्द्रा", "अङ्गसादः", "प्रसेकः", "ग्लानिः", "पिपासा"],
              "Drowsiness, limb-weariness, flow, exhaustion, thirst (doubtful words left out).",
              "तन्द्रा → अङ्गसाद → प्रसेक → ग्लानि → पिपासा.", role="extend",
              teaches="अङ्गसाद = अङ्ग (limb) + साद (weariness, slackness): weariness of the limbs."),
        mcq("discriminate", 3, "What does तथा, the first word of unit 8, mean?",
            ("Likewise", "The card glosses तथा as likewise: the list of signs goes on."),
            [("Therefore", "That is तस्मात्, in unit 11."),
             ("Gradually", "That is क्रमेण, in unit 9."),
             ("Not", "That is न.")],
            "तथा = likewise.",
            "तथा = likewise."),
        mcq("apply", 4, "Why is प्रसेकः printed प्रसेको before हृदय…?",
            ("-अः becomes -ओ before the voiced ह", "ह is voiced, so -अः → -ओ."),
            [("-अः becomes -ओ before every consonant", "अङ्गसादः keeps its visarga before प्रसेकः."),
             ("The ओ marks a vocative form", "प्रसेकः is labelled nominative."),
             ("The word's stem is प्रसेको", "The stem is प्रसेक; ओ is sandhi.")],
            "प्रसेकः + ह… → प्रसेको ह…: -अः → -ओ before a voiced consonant.",
            "-अः → -ओ before a voiced consonant."),
        mcq("transfer", 5, "By the rule of प्रसेको हृदय…, how is बालः + हसति (the child laughs) written?",
            ("बालो हसति", "-अः → -ओ before the voiced ह."),
            [("बालर्हसति", "र् replaces visarga only after vowels other than अ/आ."),
             ("बालस् हसति", "स् stands for visarga only before त, थ."),
             ("बाला हसति", "-अः does not become -आ.")],
            "बालः + हसति = बालो हसति, like प्रसेकः + हृदय… = प्रसेको हृदय….",
            "-अः → -ओ before a voiced consonant.",
            teaches="-अः becomes -ओ before a voiced consonant (ग, द, ब, ह …): प्रसेकः + हृदय… → प्रसेको हृदय…."),
    ],
}

# ---------------------------------------------------------------- unit 9
AUTHORED["9"] = {
    "title": "क्रमेण तु व्यक्तगर्भायाः",
    "question": "By unit 9, which signs appear gradually once the pregnancy has become manifest?",
    "rule": ("Gradually (क्रमेण), in a woman whose pregnancy is manifest: sleep, yawning, fainting, vomiting, distaste "
             "for food, swelling of the feet, craving for the sour, and other signs of less sure reading."),
    "limits": ("Confidence low. कुक्षिमात्रगौरवम् (heaviness of the belly alone) is a possible correction of the print; "
               "अक्षिरोमसंतुलनम् has no clear sense; the sense of -ता in क्षामनेत्रस्वरता is not secure. No question uses "
               "these. 'In those various states' is translated literally; no advice is given."),
    "explain_hi": ("‘किन्तु क्रम से, जिसका गर्भ प्रकट हो चुका है उसमें’ ये लक्षण आते हैं: निद्रा, जम्हाई, मूर्च्छा, छर्दि (उलटी), "
                   "अरुचि (भोजन में अरुचि), पैरों की सूजन (पादशोफ) और खट्टे की अभिलाषा। "
                   "सूची के आरम्भ में कुछ पद संदिग्ध हैं: ‘कुक्षिमात्रगौरव’ (छपाई में अतिरिक्त ‘औ’), ‘क्षामनेत्रस्वरता’ और "
                   "‘अक्षिरोमसंतुलन’ (अर्थ अस्पष्ट); इन पर प्रश्न नहीं है। "
                   "इकाई ७ ‘सद्योगृहीतगर्भा’ (अभी गर्भ धारण की हुई) के लक्षण देती है, यह इकाई ‘व्यक्तगर्भा’ (प्रकट गर्भ वाली) के। "
                   "सन्धि: पादशोफः + अम्ले → पादशोफोऽम्ले (अः + अ → ओऽ)।"),
    "hook": "प्रकट गर्भ: नींद, जम्हाई, मूर्च्छा, उलटी, अरुचि, पैर सूजे, खट्टे की चाह।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 9, what does the woman crave once her pregnancy is manifest?",
            ("The sour", "अम्लेऽभिलाषः = craving for the sour."),
            [("The sweet", "Sweet is not named in this unit."),
             ("The salty", "Salty is not named in this unit."),
             ("Cold water", "Water is not named in this unit.")],
            "अम्ले अभिलाषः: craving for the sour.",
            "अम्ले अभिलाषः = craving for the sour."),
        order(1, "Put these signs of unit 9 in the text's order.",
              ["निद्रा", "जृम्भणम्", "मूर्च्छा", "छर्दिः", "अरुचिः", "पादशोफः"],
              "Sleep, yawning, fainting, vomiting, distaste for food, swelling of the feet.",
              "निद्रा → जृम्भण → मूर्च्छा → छर्दि → अरुचि → पादशोफ."),
        match(2, "Match each sign of unit 9 to its meaning.",
              [["निद्रा", "sleep"], ["जृम्भणम्", "yawning"], ["छर्दिः", "vomiting"],
               ["अरुचिः", "distaste for food"], ["पादशोफः", "swelling of the feet"]],
              "Sure signs of manifest pregnancy in unit 9.",
              "निद्रा, जृम्भण, छर्दि, अरुचि, पादशोफ.", role="extend",
              teaches="पादशोफ = पाद (foot) + शोफ (swelling, oedema; standard): swelling of the feet."),
        mcq("discriminate", 3, "What does क्रमेण, the first word of unit 9, mean?",
            ("Gradually, in order", "The card glosses क्रमेण as gradually, in order."),
            [("Suddenly, at once", "That is not क्रमेण; unit 7 has सद्यः, just now."),
             ("Never", "क्रमेण is not a negative."),
             ("At night", "No time of day is named.")],
            "क्रमेण तु व्यक्तगर्भायाः: gradually, in her whose pregnancy is manifest.",
            "क्रमेण = gradually."),
        mcq("apply", 4, "Which split of पादशोफोऽम्ले is right?",
            ("पादशोफः + अम्ले", "-अः + अ → -ओऽ: पादशोफोऽम्ले."),
            [("पादशोफो + म्ले", "म्ले is not a word; the ऽ marks a lost अ."),
             ("पादशोफे + अम्ले", "ए + अ would give पादशोफेऽम्ले."),
             ("पादशोफम् + अम्ले", "Then the म् would show: पादशोफमम्ले.")],
            "पादशोफः (swelling of the feet) + अम्ले (for the sour).",
            "-अः + अ → -ओऽ."),
        mcq("transfer", 5, "By the rule of पादशोफोऽम्ले, how is वेदः + अयम् (this is the Veda) written?",
            ("वेदोऽयम्", "-अः + अ → -ओऽ, as पादशोफः + अम्ले."),
            [("वेद अयम्", "Before अ the visarga does not just drop; -अः + अ → -ओऽ."),
             ("वेदरयम्", "र् replaces visarga only after vowels other than अ/आ."),
             ("वेदायम्", "-अः + अ does not give आ.")],
            "वेदः + अयम् = वेदोऽयम्, like पादशोफः + अम्ले = पादशोफोऽम्ले.",
            "-अः + अ → -ओऽ.",
            teaches="-अः before अ becomes -ओ and the अ is dropped, marked by ऽ: पादशोफः + अम्ले → पादशोफोऽम्ले."),
    ],
}

# ---------------------------------------------------------------- unit 10
AUTHORED["10"] = {
    "title": "स्रोतसां वर्त्मान्युपरुध्यन्ते गर्भेण",
    "question": "By unit 10, what does the embryo do to the channels that carry rajas?",
    "rule": ("The paths of her srotas (bodily channels) that carry rajas (menstrual blood) are blocked by the embryo. "
             "उपरुध्यन्ते is passive (are blocked); the doer, गर्भेण, is instrumental."),
    "limits": ("srotas is kept as 'bodily channels'; no single modern structure is named. The printed रजोवाहिनीं lacks नां: "
               "रजोवाहिनीनाम् is a possible correction, and no question uses its form. The line does not say when the "
               "blocking starts."),
    "explain_hi": ("‘और उसके रज को वहन करने वाले स्रोतसों (शरीर की वाहिनियों) के मार्ग गर्भ द्वारा रुक जाते हैं।’ "
                   "‘उपरुध्यन्ते’ कर्मवाच्य, प्रथम पुरुष बहुवचन है: ‘रोके जाते हैं’; रोकने वाला ‘गर्भेण’ तृतीया में है। "
                   "छपा ‘रजोवाहिनीं’ स्रोतसाम् से मेल नहीं खाता; ‘रजोवाहिनीनाम्’ सम्भावित सुधार है। "
                   "‘स्रोतस्’ शास्त्रीय शब्द है, किसी एक आधुनिक संरचना से नहीं जोड़ा गया। अगली इकाई इसका फल बताती है।"),
    "hook": "गर्भ ने रज के मार्ग रोके: वर्त्मानि उपरुध्यन्ते गर्भेण।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 10, what blocks the paths of the rajas-carrying channels?",
            ("The embryo (garbha)", "गर्भेण = by the embryo."),
            [("Vāyu (Vāta)", "Vāyu is not named in this unit."),
             ("The old rajas", "Old rajas is named in unit 2, not here."),
             ("The ārtava itself", "Ārtava is not named in this unit.")],
            "वर्त्मानि उपरुध्यन्ते गर्भेण: the paths are blocked by the embryo.",
            "गर्भेण = by the embryo."),
        match(1, "Match each word of unit 10 to its meaning.",
              [["तस्याः", "of her"], ["स्रोतसाम्", "of the channels"], ["वर्त्मानि", "paths"],
               ["उपरुध्यन्ते", "are blocked"], ["गर्भेण", "by the embryo"]],
              "The paths of her rajas-carrying channels are blocked by the embryo.",
              "तस्याः, स्रोतसाम्, वर्त्मानि, उपरुध्यन्ते, गर्भेण."),
        order(2, "Put these words of unit 10 in the line's order.",
              ["तस्याश्च", "स्रोतसाम्", "वर्त्मानि", "उपरुध्यन्ते", "गर्भेण"],
              "Of her, of the channels, the paths, are blocked, by the embryo.",
              "तस्याश्च → स्रोतसाम् → वर्त्मानि → उपरुध्यन्ते → गर्भेण.", role="extend",
              teaches="In a passive sentence the doer stands in the instrumental: गर्भेण उपरुध्यन्ते = are blocked by the embryo."),
        mcq("discriminate", 3, "What does उपरुध्यन्ते say about the paths?",
            ("They are blocked", "The card labels it 3 pl. present passive."),
            [("They block something else", "That would be active; the form is passive."),
             ("They will be blocked later", "The form is present, not future."),
             ("They were opened by the embryo", "उप-√रुध् means block, not open.")],
            "उपरुध्यन्ते = are blocked; वर्त्मानि is its plural subject.",
            "-यन्ते = passive, they are (being) X-ed."),
        mcq("apply", 4, "Which split of वर्त्मान्युपरुध्यन्ते is right?",
            ("वर्त्मानि + उपरुध्यन्ते", "इ before उ becomes य्: नि + उ → न्यु."),
            [("वर्त्मान् + युपरुध्यन्ते", "युपरुध्यन्ते is not a word."),
             ("वर्त्मानम् + उपरुध्यन्ते", "Then the म् would show: वर्त्मानमुप…."),
             ("वर्त्मानः + उपरुध्यन्ते", "-अः + उ would drop the visarga: वर्त्मान उप….")],
            "वर्त्मानि (paths) + उपरुध्यन्ते (are blocked).",
            "इ + unlike vowel → य् + vowel."),
        mcq("transfer", 5, "In the invented sentence जलेन मार्गा उपरुध्यन्ते, what blocks the paths?",
            ("The water", "जलेन is instrumental: the doer of the passive."),
            [("The paths themselves", "मार्गाः is the subject that is blocked."),
             ("Nothing; the paths block the water", "The verb is passive: the paths are blocked."),
             ("A traveller on the paths", "No traveller is named.")],
            "जलेन मार्गा(ः) उपरुध्यन्ते = the paths are blocked by water, like वर्त्मानि गर्भेण उपरुध्यन्ते.",
            "Passive verb + instrumental doer.",
            teaches="With a passive verb, the thing acted on is nominative and the doer instrumental: वर्त्मानि … गर्भेण उपरुध्यन्ते."),
    ],
}

# ---------------------------------------------------------------- unit 11
AUTHORED["11"] = {
    "title": "तस्मात् ततः परम् आर्तवं न दृश्यते",
    "question": "By unit 11, what follows from the blocking of the channels in unit 10?",
    "rule": ("Therefore (तस्मात्), from then on (ततः परम्), the ārtava (menstrual fluid) is not seen. तस्मात् points "
             "back to the blocking of the channels in unit 10."),
    "limits": ("The line says only that ārtava is not seen; it does not say for how long, nor give any test or advice. "
               "The link to unit 10 follows the data's note."),
    "explain_hi": ("‘इसलिए उसके बाद आर्तव (स्त्री का रज) दिखाई नहीं देता।’ "
                   "‘तस्मात्’ (इसलिए) पिछली इकाई की बात की ओर संकेत करता है: गर्भ ने रजोवाही स्रोतसों के मार्ग रोक दिए। "
                   "‘ततः परम्’ एक मुहावरा है: ‘उसके बाद से’। "
                   "‘दृश्यते’ कर्मवाच्य, प्रथम पुरुष एकवचन है: ‘दिखाई देता है’; ‘न’ के साथ ‘नहीं दिखता’। "
                   "छपाई में ‘तस्मात्ततःपरमार्तवं’ एक साथ लिखा है।"),
    "hook": "मार्ग रुके, इसलिए आर्तव न दृश्यते।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 11, what is no longer seen after conception?",
            ("The ārtava", "आर्तवं न दृश्यते."),
            [("The śukra", "Śukra is not named in this unit."),
             ("The embryo's throbbing", "No throbbing is named in this unit."),
             ("Swelling of the feet", "That is a sign in unit 9, not named here.")],
            "आर्तवं न दृश्यते: the ārtava is not seen.",
            "ततः परम् आर्तवं न दृश्यते."),
        order(1, "Put the words of unit 11 in the line's order.",
              ["तस्मात्", "ततः", "परम्", "आर्तवम्", "न", "दृश्यते"],
              "Therefore, from then on, the ārtava is not seen.",
              "तस्मात् → ततः → परम् → आर्तवम् → न → दृश्यते."),
        match(2, "Match each word of unit 11 to its meaning.",
              [["तस्मात्", "therefore"], ["ततः परम्", "from then on"], ["आर्तवम्", "ārtava (menstrual fluid)"],
               ["न", "not"], ["दृश्यते", "is seen"]],
              "Therefore, from then on, ārtava is not seen.",
              "तस्मात्, ततः परम्, आर्तवम्, न, दृश्यते.", role="extend",
              teaches="ततः परम् is an idiom: after that, from then on."),
        mcq("discriminate", 3, "By the card, what does तस्मात् (therefore) point back to?",
            ("The blocking of the channels in unit 10", "The data links unit 11 to unit 10."),
            [("The splitting by anila in unit 5", "That explains offspring, not the stopping of ārtava."),
             ("The signs of unit 7", "Unit 7 lists signs; it gives no cause."),
             ("The clean womb of unit 2", "That is a condition for conception, not this cause.")],
            "The paths are blocked by the embryo (unit 10); therefore ārtava is not seen (unit 11).",
            "Unit 10 cause → unit 11 result."),
        mcq("apply", 4, "What form is दृश्यते in unit 11?",
            ("Passive, 3rd singular present: is seen", "The card labels it 3 sg. pres. pass. of √दृश्."),
            [("Active, 3rd singular: sees", "The form is passive, not active."),
             ("Passive, 3rd plural: are seen", "The plural would be दृश्यन्ते."),
             ("Passive, future: will be seen", "The form is present, not future.")],
            "दृश्यते = is seen; with न, is not seen.",
            "दृश्यते = is seen."),
        mcq("transfer", 5, "In the invented line चन्द्रो न दृश्यते, what is said?",
            ("The moon is not seen", "दृश्यते is passive singular: is seen; न = not."),
            [("The moon does not see", "That would need an active verb, पश्यति."),
             ("The moon will not be seen", "दृश्यते is present, not future."),
             ("The moons are not seen", "चन्द्रः and दृश्यते are singular.")],
            "चन्द्रो न दृश्यते = the moon is not seen, like आर्तवं न दृश्यते.",
            "न दृश्यते = is not seen.",
            teaches="दृश्यते is the present passive of √दृश्: is seen; न दृश्यते = is not seen."),
    ],
}

# ---------------------------------------------------------------- unit 12
AUTHORED["12"] = {
    "title": "अपरेत्याहुः",
    "question": "What name does unit 12 give to what is checked below and increases of itself?",
    "rule": ("Then that, checked below and increasing of itself, they call aparā (probably the afterbirth, placenta). "
             "आहुः = they say."),
    "limits": ("Confidence low; grammar not secure. तत् is taken as the fluid of earlier units (not stated). The doubled "
               "अपरम् may be a repetition. aparā = placenta is probable. Who 'they' are is not said. No question uses "
               "these points."),
    "explain_hi": ("‘तब वह, नीचे रुका हुआ, अपने आप बढ़ता हुआ, उसे अपरा (सम्भवतः आँवल) कहते हैं।’ "
                   "पंक्ति कठिन है और व्याकरण पक्का नहीं। ‘तत्’ को पिछली इकाइयों का रक्त/रज माना गया है, जो यहाँ लिखा नहीं। "
                   "दोहरा ‘अपरम् अपरम्’ छपाई की पुनरुक्ति भी हो सकता है, या ‘एक और, एक और’ का अर्थ। "
                   "‘स्वोपचीयमान’ = स्व + उपचीयमान (अपने आप बढ़ता हुआ)। ‘आहुः’ = कहते हैं; कौन कहते हैं, नहीं बताया। "
                   "अगली इकाई में दूसरे इसका नाम ‘जरायु’ बताते हैं।"),
    "hook": "नीचे रुका, अपने आप बढ़ा: अपरा इति आहुः।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 12, what name is given to what is checked below and increases of itself?",
            ("अपरा (aparā)", "अपरेत्याहुः = they call it aparā."),
            [("जरायु (jarāyu)", "जरायु is the name others give, in unit 13."),
             ("आर्तव (ārtava)", "Ārtava is not the name given here."),
             ("गर्भाशय (garbhāśaya)", "The womb is not the name given here.")],
            "They call it aparā, probably the afterbirth (placenta).",
            "अपरा इति आहुः."),
        match(1, "Match each word of unit 12 to its meaning.",
              [["अधः", "below"], ["प्रतिहतम्", "checked, obstructed"], ["स्वोपचीयमानम्", "increasing of itself"],
               ["अपरा", "aparā (probably the placenta)"], ["आहुः", "they say"]],
              "Checked below, increasing of itself, they call it aparā.",
              "अधः, प्रतिहत, स्वोपचीयमान, अपरा, आहुः."),
        order(2, "Put these parts of unit 12 in the line's order.",
              ["ततः", "तत्", "अधः प्रतिहतम्", "स्वोपचीयमानम्", "अपरा इति आहुः"],
              "Then, that, checked below, increasing of itself, they call aparā (the doubled अपरम् is left out).",
              "ततः → तत् → अधः प्रतिहतम् → स्वोपचीयमानम् → अपरा इति आहुः.", role="extend",
              teaches="स्वोपचीयमान = स्व (of itself) + उपचीयमान (being built up, present passive participle of उप-√चि)."),
        mcq("discriminate", 3, "Which split of स्वोपचीयमानम् is right?",
            ("स्व + उपचीयमानम्", "अ + उ → ओ: स्व + उप… = स्वोप…."),
            [("स्वः + उपचीयमानम्", "-अः before उ drops the visarga and leaves a gap: स्व उप…."),
             ("स्वम् + उपचीयमानम्", "Then the म् would show: स्वमुप…."),
             ("स्वे + उपचीयमानम्", "ए before उ would not give ओ.")],
            "स्व (by itself) + उपचीयमानम् (being built up): अ + उ → ओ.",
            "अ + उ → ओ."),
        mcq("apply", 4, "Which split of अपरेत्याहुः is right?",
            ("अपरा + इति + आहुः", "आ + इ → ए, then इ + आ → या."),
            [("अपरे + इति + आहुः", "ए + इ would give अपर इति, not अपरेति."),
             ("अपरम् + इति + आहुः", "Then the म् would show: अपरमित्याहुः."),
             ("अपरा + इत्या + हुः", "इत्या and हुः are not words of the card.")],
            "अपरा (the name) + इति (thus) + आहुः (they say).",
            "आ + इ → ए; इ + आ → या."),
        mcq("transfer", 5, "By the rule of अपरा + इति → अपरेति, how is महा + इन्द्रः written?",
            ("महेन्द्रः", "आ + इ → ए, as अपरा + इति."),
            [("महैन्द्रः", "आ + इ gives ए, not ऐ."),
             ("महीन्द्रः", "आ + इ does not give ई."),
             ("महायिन्द्रः", "No य् is put between आ and इ.")],
            "महा + इन्द्रः = महेन्द्रः, like अपरा + इति = अपरेति.",
            "आ/अ + इ → ए.",
            teaches="अ or आ before इ or ई joins into ए: अपरा + इति → अपरेति."),
    ],
}

# ---------------------------------------------------------------- unit 13
AUTHORED["13"] = {
    "title": "जरायुरित्यन्ये",
    "question": "In unit 13, what name do others give for the same thing?",
    "rule": ("जरायुः इति अन्ये: others say jarāyu (probably the foetal membrane). The verb 'say' is carried from आहुः of "
             "unit 12; it is another name for the same thing."),
    "limits": ("The data says this 'appears to continue' unit 12. jarāyu = foetal membrane or afterbirth is probable. "
               "The doubled उ of the print (जरायुुः) is a certain misprint. The line does not say who the others are, or "
               "which name is right."),
    "explain_hi": ("‘दूसरे इसे जरायु (सम्भवतः गर्भ की झिल्ली) कहते हैं।’ "
                   "क्रिया ‘कहते हैं’ इकाई १२ के ‘आहुः’ से आती है; यह इकाई उसी वस्तु का दूसरा नाम देती है। "
                   "इकाई १२: ‘अपरा’ (कुछ कहते हैं); इकाई १३: ‘जरायु’ (अन्य कहते हैं)। कौन-सा नाम ठीक है, ग्रन्थ नहीं कहता। "
                   "सन्धि: जरायुः + इति → जरायुरिति (उ के बाद विसर्ग स्वर से पहले र्), इति + अन्ये → इत्यन्ये (इ + अ → य)। "
                   "छपाई का दोहरा ‘ु’ निश्चित भूल है।"),
    "hook": "कोई कहे अपरा, अन्ये कहें जरायु।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 13, what name do others give?",
            ("जरायु (jarāyu)", "जरायुरित्यन्ये = jarāyu, say others."),
            [("अपरा (aparā)", "Aparā is the name of unit 12."),
             ("आर्तव (ārtava)", "Ārtava is not the name given."),
             ("स्रोतस् (srotas)", "Srotas are the channels of unit 10.")],
            "Others call it jarāyu, probably the foetal membrane.",
            "जरायुः इति अन्ये."),
        match(1, "Match each word of unit 13 to its meaning.",
              [["जरायुः", "jarāyu (probably the foetal membrane)"], ["इति", "thus, marking the name quoted"],
               ["अन्ये", "others"]],
              "jarāyu, thus, say others.",
              "जरायुः, इति, अन्ये."),
        T(fill(2, "Others say: ____ इति अन्ये. Type the name in Devanagari or in English letters (e.g. dharma).",
               accepts("जरायुः", None, "जरायु", "jarayu"),
               "The line is जरायुरित्यन्ये: jarāyu, say others.",
               "इति after a word marks it as the name quoted: जरायुः इति अन्ये = 'jarāyu', say others.",
               "जरायुः इति अन्ये."),
          "इति after a word marks it as quoted; the verb say is carried from unit 12."),
        mcq("discriminate", 3, "Which split of जरायुरित्यन्ये is right?",
            ("जरायुः + इति + अन्ये", "-उः → -उर् before a vowel; इ + अ → य."),
            [("जरायु + रिति + अन्ये", "रिति is not a word; the र् comes from the visarga."),
             ("जरायुम् + इति + अन्ये", "Then the म् would show: जरायुमित्यन्ये."),
             ("जरायुः + इति + न्ये", "न्ये is not a word; the अ of अन्ये joins with इ.")],
            "जरायुः (the name) + इति (thus) + अन्ये (others).",
            "-उः + vowel → -उर्; इ + अ → य."),
        mcq("apply", 4, "What does अन्ये mean in unit 13?",
            ("Others", "The card glosses अन्ये as others (nom. pl.)."),
            [("These", "That would be इमे."),
             ("All", "That would be सर्वे."),
             ("Some", "That would be केचित्.")],
            "जरायुरित्यन्ये: jarāyu, say others.",
            "अन्ये = others."),
        mcq("transfer", 5, "By the rule of जरायुरिति, how is गुरुः + आगतः (the teacher has come) written?",
            ("गुरुरागतः", "Visarga after उ becomes र् before a vowel, as जरायुः + इति."),
            [("गुरु आगतः", "After उ the visarga is not dropped before a vowel."),
             ("गुरोरागतः", "The उ of गुरुः does not change to ओ."),
             ("गुरुसागतः", "स् stands for visarga only before त, थ.")],
            "गुरुः + आगतः = गुरुरागतः, like जरायुः + इति = जरायुरिति.",
            "-उः + vowel → -उर् + vowel.",
            teaches="Visarga after उ (any vowel but अ/आ) becomes र् before a vowel: जरायुः + इति → जरायुरिति."),
    ],
}

# ===================================================================== NOTES_HI
NOTES_HI = {
    "1": ("गद्य-पंक्ति; विश्वास उच्च; कोई पाठ-चिह्न नहीं। छपा ‘गर्भावक्रांति’ = गर्भावक्रान्ति (अनुस्वार = न्, केवल वर्तनी)। "
          "‘गर्भावक्रान्ति’ अध्याय का नाम है; ‘गर्भ का उतरना/प्रवेश’ शाब्दिक अर्थ। "
          "सन्धि जाँची: अथ + अतः → अथातः (अ + अ → आ); अतः + गर्भ → अतो गर्भ (अः → ओ घोष से पहले); गर्भ + अवक्रान्ति → गर्भावक्रान्ति।"),
    "2": ("गद्य; विश्वास मध्यम; एक लम्बा वाक्य। पाठ-चिह्न: ‘वशांनुवर्तिना’ → वशानुवर्तिना (सम्भावित; अनुस्वार अनावश्यक)। "
          "‘अन्वक्षम्’ अनिश्चित (सम्भवतः अनु-अक्ष ‘तुरन्त’); अन्य अर्थ भी सम्भव, इस पर प्रश्न नहीं। ‘अभिसंसृष्टम्’ शुक्र से अन्वित माना गया। "
          "छपा ‘रजसिनवे’ = रजसि नवे। "
          "सन्धि जाँची: नवे + अवस्थिते → नवेऽवस्थिते; गर्भस्य + आशये → गर्भस्याशये; बीज + आत्मना → बीजात्मना; "
          "अन्यैः + च → अन्यैश्च; महाभूतैः + अनुगतम् → महाभूतैरनुगतम्; आर्तवेन + अभिमूर्च्छितम् → आर्तवेनाभिमूर्च्छितम्; "
          "जीवेन + अभिसंसृष्टम् → जीवेनाभिसंसृष्टम्। जीव = जीवात्मा (शास्त्रीय, आधुनिक पर्याय नहीं)।"),
    "3": ("गद्य; विश्वास मध्यम। पाठ-चिह्न: छपा ‘कारणानुविधायित्वात्त्त्स्वभावतां’ — तीन त् और ‘तत्’ का अ छूटा; "
          "सुधार कारणानुविधायित्वात् तत्स्वभावताम् (सम्भावित, अर्थ की माँग)। छपे रूप पर प्रश्न नहीं। "
          "कर्ता (गर्भ) इकाई २ से समझा जाता है, लिखा नहीं। सन्धि जाँची: कारण + अनुविधायित्वात् → कारणानु… (अ + अ → आ)।"),
    "4": ("गद्य; विश्वास उच्च; कोई पाठ-चिह्न नहीं; क्रिया नहीं (‘उत्पन्न होता है’ जैसा अर्थ समझा जाता है, अनुवाद में नहीं जोड़ा)। "
          "छपाई में शब्द जुड़े हैं (बाहुल्यात्पुमानार्तवस्यबाहुल्यात्स्त्री) — यह लेखन-शैली है, भूल नहीं। "
          "नपुंसक = तीसरी श्रेणी (शब्दशः ‘न पुरुष’), कोई आधुनिक पर्याय नहीं। "
          "सन्धि जाँची: ततः + एव → तत एव (अः के बाद अ से भिन्न स्वर: विसर्ग लोप, अन्तर रहता है)।"),
    "5": ("गद्य; विश्वास उच्च; कोई पाठ-चिह्न नहीं। ‘उत्पत्तिः’ नामवाक्य है (‘होती है’ समझा हुआ)। ‘अपत्यानाम्’ बहुवचन, संख्या नहीं कही गई। "
          "सन्धि जाँची: शुक्र + आर्तव → शुक्रार्तव; शुक्रार्तवे + अनिलेन → शुक्रार्तवेऽनिलेन (ए + अ → एऽ); "
          "खण्डशः + भिन्ने → खण्डशो भिन्ने (अः → ओ घोष से पहले); यथाविभागम् + अपत्यानाम् + उत्पत्तिः एक साथ छपे। "
          "छपा ‘खंडशो’ = खण्डशो (अनुस्वार = ण्)।"),
    "6": ("गद्य; विश्वास मध्यम; केवल दो शब्द। डेटा का GROUPING: इकाई ५ को आगे बढ़ाती दिखती है (‘उत्पत्तिः’ वहीं से)। "
          "क्या विकृत है (शुक्र-आर्तव या वायु), नहीं कहा गया; ‘वियोनि’ = अन्य योनि; पशु-आकार का अर्थ नहीं जोड़ा गया। "
          "सन्धि जाँची: वियोनि + आकृतीनाम् → वियोन्याकृतीनाम् (इ + आ → या)।"),
    "7": ("गद्य; विश्वास मध्यम। पाठ-चिह्न: ‘अथनार्याः’ = अथ नार्याः (निश्चित, केवल अन्तर)। ‘योन्या’ तृतीया माना गया; षष्ठी ‘योन्याः’ भी सम्भव, "
          "अर्थ लगभग वही। ‘गुरिमा’ = भारीपन (सामान्यतः गरिमा)। "
          "सन्धि जाँची: सद्यः + गृहीत → सद्योगृहीत; गर्भायाः + च → गर्भायाश्च; तृप्तिः + गुरिमा → तृप्तिर्गुरिमा; "
          "शुक्रार्तवयोः + अनुबन्धः → शुक्रार्तवयोरनुबन्धः; अनुबन्धः + च → अनुबन्धश्च।"),
    "8": ("गद्य; विश्वास निम्न। तीन पाठ-चिह्न: ‘महर्षो’ → प्रहर्षः या महाहर्षः (सम्भावित, सबसे कम निश्चित); "
          "‘हृल्लाभ’ → हृल्लासः, जी मिचलाना (सम्भावित, भ/स भ्रम); ‘हृदयन्पथा’ → हृदयव्यथा (सम्भावित, व्य/न्प भ्रम)। "
          "इन तीनों पर प्रश्न नहीं; अनुवाद ‘अनुमानित पाठ पर’। ‘प्रसेक’ = बहाव, कोई संज्ञा नहीं जोड़ी गई। "
          "छपा ‘तंद्राऽंगसादःप्रसेको’ = तन्द्रा अङ्गसादः प्रसेको (ऽ यहाँ मिले हुए अ को दिखाता है)। "
          "सन्धि जाँची: प्रसेकः + हृदय… → प्रसेको हृदय… (अः → ओ घोष से पहले)।"),
    "9": ("गद्य; विश्वास निम्न। पाठ-चिह्न: ‘कुक्षिमात्रौगौरवं’ → कुक्षिमात्रगौरवम् (सम्भावित, छपाई में अतिरिक्त औ)। "
          "‘अक्षिरोमसंतुलनम्’ का अर्थ अस्पष्ट, शाब्दिक रखा गया; ‘क्षामनेत्रस्वरता’ में -ता का अर्थ पक्का नहीं। इन पर प्रश्न नहीं। "
          "अन्तिम ‘इति’ सूची की समाप्ति। "
          "सन्धि जाँची: पादशोफः + अम्ले → पादशोफोऽम्ले; अम्ले + अभिलाषः → अम्लेऽभिलाषः; अभिलाषः + तेषु → अभिलाषस्तेषु; "
          "छर्दिः + अरुचिः → छर्दिररुचिः; च + उच्चावचेषु → चोच्चावचेषु; भावेषु + इति → भावेष्विति।"),
    "10": ("गद्य; विश्वास मध्यम। पाठ-चिह्न: ‘रजोवाहिनीं’ → रजोवाहिनीनाम् (सम्भावित; स्रोतसाम् से मेल के लिए षष्ठी बहुवचन चाहिए, ‘ना’ छूटा)। "
           "इस रूप पर प्रश्न नहीं। ‘स्रोतस्’ = शरीर की वाहिनियाँ (शास्त्रीय शब्द)। "
           "सन्धि जाँची: तस्याः + च → तस्याश्च; रजस् + वाहिनी → रजोवाहिनी; वर्त्मानि + उपरुध्यन्ते → वर्त्मान्युपरुध्यन्ते (इ + उ → यु)। "
           "छपा ‘उपरुध्यंते’ = उपरुध्यन्ते।"),
    "11": ("गद्य; विश्वास उच्च; कोई पाठ-चिह्न नहीं। इकाई १० से जुड़ी: गर्भ के बाद आर्तव का रुकना। "
           "सन्धि जाँची: तस्मात् + ततः → तस्मात्ततः; ततः + परम् → ततः परम् (प से पहले विसर्ग रहता है); परम् + आर्तवम् → परमार्तवम्। "
           "छपाई में ‘तस्मात्ततःपरमार्तवं’ बिना अन्तर।"),
    "12": ("गद्य; विश्वास निम्न; व्याकरण पक्का नहीं। पाठ-चिह्न: दोहरा ‘अपरम् अपरम्’ — पुनरुक्ति (छपाई की) सम्भव, अनुवाद में दोनों रखे। "
           "‘तत्’ को पिछली इकाइयों का रक्त/रज माना गया, यहाँ लिखा नहीं। अपरा = आँवल (सम्भावित)। ‘आहुः’ का कर्ता नहीं कहा गया। "
           "सन्धि जाँची: ततः + तत् → ततस्तत्; तत् + अधः → तदधः; स्व + उपचीयमानम् → स्वोपचीयमानम् (अ + उ → ओ); "
           "अपरा + इति + आहुः → अपरेत्याहुः (आ + इ → ए; इ + आ → या)।"),
    "13": ("गद्य; विश्वास मध्यम। पाठ-चिह्न: छपा ‘जरायुुरित्यन्ये’ में दोहरा ‘ु’ — निश्चित भूल, शुद्ध जरायुरित्यन्ये। "
           "क्रिया ‘कहते हैं’ इकाई १२ के ‘आहुः’ से; GROUPING: इकाई १२ का दूसरा नाम। जरायु = गर्भ की झिल्ली/आँवल (सम्भावित)। "
           "सन्धि जाँची: जरायुः + इति → जरायुरिति (उ के बाद विसर्ग → र्); इति + अन्ये → इत्यन्ये (इ + अ → य)।"),
}

# ===================================================================== AIDS
AIDS = {
    "1": {
        "chunks": "अथातो | गर्भावक्रान्तिशारीरं | व्याख्यास्यामः",
        "sandhi": "अ + अ → आ: अथ + अतः → अथातः · अः → ओ घोष से पहले: अतः + गर्भ… → अतो गर्भ…।",
        "anchors": "याद-सूत्र: अध्याय १ ‘पुत्रकामीय’ (पुत्र की कामना) → अध्याय २ ‘गर्भावक्रान्ति’ (गर्भ का उतरना)। (मेरी याद-पद्धति)",
    },
    "2": {
        "diagram": {"groups": [
            {"label": "शर्तें (सप्तमी)", "items": ["पुराना रज चला गया", "नया रज स्थित", "गर्भाशय और मार्ग शुद्ध"]},
            {"label": "शुक्र (कर्ता)", "items": ["बीज-रूप, अविकृत", "अविकृत वायु से प्रेरित", "अन्य महाभूतों से अनुगत",
                                         "आर्तव से मिला", "जीव से संयुक्त", "गर्भाशय में पहुँचता"]},
            {"label": "जीव", "items": ["राग आदि क्लेशों के वश", "अपने कर्म से प्रेरित", "मन जैसा वेग"]}]},
        "frame": "शर्तें (गते … शुद्धे … मार्गे च) → कर्ता (शुक्रम् + विशेषण) → जीव के विशेषण (तृतीया) → क्रिया (गर्भाशयम् उपयाति)।",
        "sandhi": "ऐः → ऐर् स्वर से पहले: महाभूतैः + अनुगतम् → महाभूतैरनुगतम् · अ + अ → आ: आर्तवेन + अभि… → आर्तवेनाभि… · ए + अ → एऽ: नवे + अवस्थिते → नवेऽवस्थिते।",
        "chunks": "गते पुराणे रजसि नवेऽवस्थिते | शुद्धे गर्भस्याशये मार्गे च | बीजात्मना शुक्रमविकृतम् | अविकृतेन वायुना प्रेरितम् | "
                  "अन्यैश्च महाभूतैरनुगतम् | आर्तवेनाभिमूर्च्छितम् | अन्वक्षमेव (?) | रागादिक्लेशवशानुवर्तिना स्वकर्मचोदितेन मनोजवेन जीवेनाभिसंसृष्टम् | गर्भाशयमुपयाति",
    },
    "3": {
        "chain": {"steps": ["कारण", "कार्य कारण का अनुसरण करते हैं", "इसलिए", "वह (गर्भ) उसी कारण का स्वभाव पाता है"]},
        "chunks": "कार्याणां च | कारणानुविधायित्वात् | तत्स्वभावतां | प्रतिपद्यते",
        "anchors": "याद-सूत्र: ‘जैसा बीज, वैसा पेड़’ — कार्य कारण के पीछे चलता है। (मेरी याद-पद्धति, श्लोक का कथन नहीं)",
    },
    "4": {
        "diagram": {"groups": [
            {"label": "शुक्र की अधिकता", "items": ["पुरुष"]},
            {"label": "आर्तव की अधिकता", "items": ["स्त्री"]},
            {"label": "दोनों की समता", "items": ["नपुंसक"]}]},
        "chunks": "ततएव च | शुक्रस्य बाहुल्यात्पुमान् | आर्तवस्य बाहुल्यात्स्त्री | तयोः साम्येन नपुंसकं",
        "sandhi": "अः + अ से भिन्न स्वर → अ (अन्तर रहता है): ततः + एव → तत एव।",
        "seesaw": "शुक्र भारी पड़े → पुमान् ↔ आर्तव भारी पड़े → स्त्री; बराबर रहे → नपुंसक।",
    },
    "5": {
        "chain": {"steps": ["शुक्र-आर्तव", "वायु (अनिल) से", "टुकड़ों में भिन्न", "विभाग के अनुसार", "सन्तानों की उत्पत्ति"]},
        "chunks": "शुक्रार्तवेऽनिलेन | खण्डशो भिन्ने | यथाविभागम् | अपत्यानामुत्पत्तिः",
        "sandhi": "ए + अ → एऽ: शुक्रार्तवे + अनिलेन → शुक्रार्तवेऽनिलेन · अः → ओ घोष से पहले: खण्डशः + भिन्ने → खण्डशो भिन्ने।",
    },
    "6": {
        "chunks": "विकृते | वियोन्याकृतीनां",
        "sandhi": "इ + आ → या: वियोनि + आकृतीनाम् → वियोन्याकृतीनाम्।",
        "frame": "विकृते (सप्तमी: विकृत होने पर) + वियोन्याकृतीनाम् (षष्ठी बहुवचन: अन्य योनि के आकारों की); क्रिया नहीं, क्या विकृत है यह नहीं कहा गया।",
    },
    "7": {
        "diagram": {"groups": [
            {"label": "सद्योगृहीतगर्भा के लक्षण", "items": ["योनि द्वारा बीज-ग्रहण", "तृप्ति", "गुरिमा (भारीपन)",
                                                    "स्फुरण (फड़कना)", "शुक्र-आर्तव का अनुबन्ध"]}]},
        "chunks": "अथ नार्याः सद्योगृहीतगर्भायाश्च लिङ्गं | योन्या बीजग्रहणं | तृप्तिर्गुरिमा स्फुरणं | शुक्रार्तवयोरनुबन्धश्च",
        "sandhi": "इः → इर् घोष से पहले: तृप्तिः + गुरिमा → तृप्तिर्गुरिमा · अः → ओ घोष से पहले: सद्यः + गृहीत → सद्योगृहीत।",
        "letters": "पाँच लक्षणों के पहले अक्षर: बी-तृ-गु-स्फु-अ (बीजग्रहण, तृप्ति, गुरिमा, स्फुरण, अनुबन्ध)। (मेरी याद-पद्धति)",
    },
    "8": {
        "chunks": "तथा महर्षो (?) | हृल्लाभः (?) तन्द्राऽङ्गसादः प्रसेको | हृदयन्पथा (?) | ग्लानिः पिपासा च",
        "sandhi": "अः → ओ घोष से पहले: प्रसेकः + हृदय… → प्रसेको हृदय… · विसर्ग प से पहले रहता है: अङ्गसादः प्रसेकः।",
        "frame": "निश्चित शब्द: तन्द्रा → अङ्गसाद → प्रसेक → ग्लानि → पिपासा; (?) वाले तीन शब्द अनुमानित पाठ।",
    },
    "9": {
        "diagram": {"groups": [{"label": "व्यक्तगर्भा के निश्चित लक्षण, क्रम से", "items": ["निद्रा", "जृम्भण", "मूर्च्छा", "छर्दि", "अरुचि", "पादशोफ", "अम्ले अभिलाष"]}]},
        "frame": "क्रमेण तु व्यक्तगर्भायाः → निश्चित लक्षण, पाठ-क्रम में: निद्रा → जृम्भण → मूर्च्छा → छर्दि → अरुचि → पादशोफ → अम्ले अभिलाष; (?) वाले पद अनिश्चित पाठ।",
        "chunks": "क्रमेण तु व्यक्तगर्भायाः | कुक्षिमात्रगौरवं (?) | क्षामनेत्रस्वरता | अक्षिरोमसंतुलनं (?) | निद्रा जृम्भणं | "
                  "मूर्च्छा छर्दिररुचिः | पादशोफोऽम्लेऽभिलाषः | तेषु चोच्चावचेषु भावेष्विति",
        "sandhi": "अः + अ → ओऽ: पादशोफः + अम्ले → पादशोफोऽम्ले · ए + अ → एऽ: अम्ले + अभिलाषः → अम्लेऽभिलाषः · उ + इ → वि: भावेषु + इति → भावेष्विति।",
        "pegs": "मेरा बनाया चित्र: रात का दृश्य — जम्हाई लेती, ऊँघती स्त्री, पास में उलटी का पात्र, सूजे पैर, हाथ में इमली। (केवल याद के लिए)",
    },
    "10": {
        "chunks": "तस्याश्च | रजोवाहिनीनां (छपा रजोवाहिनीं) स्रोतसां | वर्त्मान्युपरुध्यन्ते | गर्भेण",
        "sandhi": "इ + उ → यु: वर्त्मानि + उपरुध्यन्ते → वर्त्मान्युपरुध्यन्ते · विसर्ग + च → श्च: तस्याः + च → तस्याश्च।",
        "frame": "कर्मवाच्य: कर्म (वर्त्मानि, प्रथमा) + कर्ता (गर्भेण, तृतीया) + क्रिया (उपरुध्यन्ते)।",
    },
    "11": {
        "chain": {"steps": ["गर्भ", "रजोवाही स्रोतसों के मार्ग रुके (इकाई १०)", "तस्मात् (इसलिए)", "ततः परम् आर्तव नहीं दिखता"]},
        "chunks": "तस्मात् | ततः परम् | आर्तवं | न दृश्यते",
        "sandhi": "विसर्ग प से पहले रहता है: ततः परम् · म् + आ → मा: परम् + आर्तवम् → परमार्तवम्।",
    },
    "12": {
        "chunks": "ततस्तत् | अधः प्रतिहतम् | अपरमपरं (?) | स्वोपचीयमानम् | अपरेत्याहुः",
        "sandhi": "अ + उ → ओ: स्व + उपचीयमानम् → स्वोपचीयमानम् · आ + इ → ए: अपरा + इति → अपरेति · इ + आ → या: इति + आहुः → इत्याहुः।",
        "frame": "क्या (तत्, अनिश्चित) → कैसा (नीचे रुका, अपने आप बढ़ता) → नाम (अपरा) → कौन कहते हैं (आहुः, ‘वे’)।",
    },
    "13": {
        "frame": "नाम (जरायुः, सम्भवतः गर्भ की झिल्ली) + इति (उद्धृत नाम) + कौन (अन्ये, दूसरे); क्रिया ‘कहते हैं’ समझी जाती है।",
        "chunks": "जरायुरिति | अन्ये",
        "sandhi": "उः → उर् स्वर से पहले: जरायुः + इति → जरायुरिति · इ + अ → य: इति + अन्ये → इत्यन्ये।",
    },
}

# ===================================================================== IMAGE_SPECS
IMAGE_SPECS = {
    ("2", "diagram"): {
        "file": "sh2-shukra-garbhashaya-2.svg",
        "alt": ("Chain of unit 2 in the text's order: when old rajas has gone, new rajas is established and womb and passage "
                "are clean, the seed-form unaltered shukra, impelled by unaltered wind, followed by the other great elements, "
                "mingled with artava and joined with the jiva, goes to the womb."),
        "type": "chain",
        "title": "शुक्र गर्भाशय तक (इकाई २, पाठ के क्रम में)",
        "steps": ["शर्त: पुराना रज गया, नया स्थित", "गर्भाशय और मार्ग शुद्ध", "बीज-रूप अविकृत शुक्र",
                  "अविकृत वायु से प्रेरित", "अन्य महाभूतों से अनुगत", "आर्तव से मिला", "जीव से संयुक्त",
                  "गर्भाशय में पहुँचता"],
    },
    ("4", "diagram"): {
        "file": "sh2-linga-nirnaya-4.svg",
        "alt": ("Table of unit 4: abundance of shukra gives a male, abundance of artava a female, equality of the two a "
                "napumsaka."),
        "type": "table",
        "title": "संतान का लिंग (इकाई ४)",
        "heads": ["कारण", "संतान"],
        "rows": [["शुक्र की अधिकता", "पुरुष"], ["आर्तव की अधिकता", "स्त्री"], ["दोनों की समता", "नपुंसक"]],
    },
    ("5", "chain"): {
        "file": "sh2-khandasha-5.svg",
        "alt": ("Flowchart of unit 5: shukra and artava, split into pieces by anila (Vata), give the origin of offspring according "
                "to the divisions."),
        "type": "mermaid",
        "code": ("flowchart TD\n"
                 "  A[\"शुक्र-आर्तव\"] -->|\"वायु (अनिल) से\"| B[\"टुकड़ों में भिन्न\"]\n"
                 "  B -->|\"विभाग के अनुसार\"| C[\"सन्तानों की उत्पत्ति\"]\n"),
    },
    ("7", "diagram"): {
        "file": "sh2-sadyogarbha-7.svg",
        "alt": ("Chart of unit 7, nodes numbered in the text's order in two columns: the signs of a woman who has just conceived: taking in of the seed by the yoni, satisfaction, heaviness, throbbing, and continued connection of shukra and artava."),
        "type": "mermaid",
        "code": ("flowchart TD\n"
                 "  R[\"सद्योगृहीतगर्भा के लक्षण\"] --> A[\"१ योनि द्वारा<br/>बीज-ग्रहण\"]\n"
                 "  R --> D[\"४ स्फुरण<br/>फड़कना\"]\n"
                 "  A ~~~ B[\"२ तृप्ति\"] ~~~ C[\"३ गुरिमा<br/>भारीपन\"]\n"
                 "  D ~~~ E[\"५ शुक्र-आर्तव<br/>का अनुबन्ध\"]\n"),
    },
    ("9", "diagram"): {
        "file": "sh2-garbha-lakshana-9.svg",
        "alt": ("Numbered table of unit 9: the sure signs that come gradually once pregnancy is manifest, in the text's "
                "order: sleep, yawning, fainting, vomiting, distaste for food, swelling of the feet, craving for the sour."),
        "type": "table",
        "title": "व्यक्तगर्भा के निश्चित लक्षण, क्रम से (इकाई ९)",
        "heads": ["क्रम", "लक्षण"],
        "rows": [["१", "निद्रा"], ["२", "जृम्भण"], ["३", "मूर्च्छा"], ["४", "छर्दि (उलटी)"], ["५", "अरुचि"],
                 ["६", "पादशोफ (पैरों की सूजन)"], ["७", "अम्ले अभिलाष (खट्टे की चाह)"]],
    },
    ("11", "chain"): {
        "file": "sh2-artava-nirodha-11.svg",
        "alt": ("Flowchart of units 10 and 11: the embryo blocks the paths of the rajas-carrying channels; therefore, from then "
                "on, artava is not seen."),
        "type": "mermaid",
        "code": ("flowchart TD\n"
                 "  A[\"गर्भ\"] -->|\"रोकता है\"| B[\"रजोवाही स्रोतों के मार्ग, इकाई १०\"]\n"
                 "  B -->|\"तस्मात्, इसलिए\"| C[\"आर्तव नहीं दिखता, इकाई ११\"]\n"),
    },
}
