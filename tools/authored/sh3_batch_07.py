from helpers import mcq, match, order, fill, multi, accepts


AUTHORED = {}

# ---------------------------------------------------------------- unit 78
AUTHORED["78"] = {
    "title": "स्फिजौ वोपसंगृह्य सुपीडितं पीडयेत्",
    "question": "By unit 78, what is the further option when the placenta does not come out?",
    "rule": ("Or (वा), having gripped the two buttocks (स्फिजौ, dual), one should press them thoroughly: सुपीडितं "
             "पीडयेत्, a cognate expression, press so that it is well pressed. वा + उपसंगृह्य → वोपसंगृह्य (आ + उ → ओ)."),
    "limits": ("Prose, high confidence. The condition 'if the placenta (अपरा) does not fall' of unit 76 appears to carry on "
               "here; it is not repeated. Who presses, with what and for how long is not stated."),
    "explain_hi": ("यह गद्य-पंक्ति एक और विकल्प देती है: या दोनों नितम्बों (स्फिजौ, द्विवचन) को पकड़कर खूब दबाए। "
                   "‘सुपीडितं पीडयेत्’ सजातीय प्रयोग है: ऐसे दबाए कि अच्छी तरह दब जाए। "
                   "इकाई 76 की शर्त, ‘यदि अपरा यानी जेर न गिरे’, यहाँ भी चलती लगती है; दोहराई नहीं गई। "
                   "कौन दबाए, किससे और कितनी देर, यह नहीं कहा गया। "
                   "‘वोपसंगृह्य’ में वा + उपसंगृह्य है (आ + उ → ओ)।"),
    "hook": "या: नितम्ब पकड़ो, खूब दबाओ।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 78, what is gripped and then pressed thoroughly?",
            ("The two buttocks (स्फिजौ)", "स्फिजौ वोपसंगृह्य सुपीडितं पीडयेत्."),
            [("The hip, struck with the heel", "Striking the hip with the heel is unit 77, not this one."),
             ("The throat and the palate", "Touching the throat and palate is unit 79."),
             ("The region above the navel", "Pressing above the navel is unit 76.")],
            "The two buttocks are gripped and pressed thoroughly.",
            "स्फिजौ ... पीडयेत्."),
        order(1, "Put the words of unit 78 in the line's order.",
              ["स्फिजौ", "वा", "उपसंगृह्य", "सुपीडितम्", "पीडयेत्"],
              "The two buttocks, or, having gripped, well pressed, one should press.",
              "स्फिजौ → वा → उपसंगृह्य → सुपीडितम् → पीडयेत्."),
        match(2, "Match each word of unit 78 to its meaning.",
              [["स्फिजौ", "the two buttocks"], ["उपसंगृह्य", "having gripped"],
               ["सुपीडितम्", "well pressed, thoroughly"], ["पीडयेत्", "should press"]],
              "Four words: what, having done what, how, and the action.",
              "स्फिजौ, उपसंगृह्य, सुपीडितम्, पीडयेत्.", role="extend",
              teaches="सुपीडितं पीडयेत् is a cognate expression: press so that it is well pressed, i.e. press thoroughly."),
        mcq("discriminate", 3, "Which split of वोपसंगृह्य is right?",
            ("वा + उपसंगृह्य", "आ + उ → ओ: वा (or) + उपसंगृह्य (having gripped)."),
            [("वो + पसंगृह्य", "Neither वो nor पसंगृह्य is a word; the absolutive is उपसंगृह्य."),
             ("वे + उपसंगृह्य", "ए + उ does not give ओ; and वे is not the word for or."),
             ("वाः + उपसंगृह्य", "आः drops its visarga before a vowel and no ओ arises; वाः is not the word.")],
            "वा (or) + उपसंगृह्य (having gripped): आ + उ → ओ.",
            "आ + उ → ओ."),
        mcq("apply", 4, "What does सुपीडितं पीडयेत् ask for in unit 78?",
            ("Pressing thoroughly, so that it is well pressed", "The note: a cognate expression, press so that it is well pressed."),
            [("Pressing lightly, only once", "सु- (well) with the same verb asks for thorough pressing, not light."),
             ("Pressing only after anointing", "No anointing is named in unit 78."),
             ("Not pressing what is already pressed", "There is no negation in the line.")],
            "सुपीडितम् + पीडयेत्: press thoroughly.",
            "सुपीडितं पीडयेत् = press thoroughly."),
        mcq("transfer", 5, "By the rule of वोपसंगृह्य, how is यथा + उक्तम् (as said) written when joined?",
            ("यथोक्तम्", "आ + उ → ओ, as वा + उपसंगृह्य → वोपसंगृह्य."),
            [("यथौक्तम्", "आ + उ does not give औ."),
             ("यथुक्तम्", "The आ is not simply dropped before उ."),
             ("यथाक्तम्", "The उ is not dropped after आ.")],
            "यथा + उक्तम् = यथोक्तम्, like वा + उपसंगृह्य.",
            "आ + उ → ओ.",
            teaches="A final आ before उ joins as ओ: वा + उपसंगृह्य → वोपसंगृह्य."),
    ],
}

# ---------------------------------------------------------------- unit 79
AUTHORED["79"] = {
    "title": "वेण्याऽङ्गुल्या वा केशवेष्टितया",
    "question": "By unit 79, with what is the throat and palate touched?",
    "rule": ("With a braid (वेण्या), or with a finger wound round with hair (अङ्गुल्या केशवेष्टितया), one should touch "
             "(परामृशेत्) the throat and palate (कण्ठतालु, a dvandva). वेण्या and अङ्गुल्या are instrumental: with."),
    "limits": ("Prose, medium confidence. केशवेष्टितया is taken with the finger; it could also go with the braid, so no "
               "question rests on that. The text states no effect of the touch. The placenta condition of unit 76 appears "
               "to carry on; it is not repeated."),
    "explain_hi": ("वेणी (बालों की चोटी) से, या बालों से लिपटी अँगुली से, कण्ठ और तालु को स्पर्श करे (परामृशेत्)। "
                   "‘केशवेष्टितया’ डेटा में अँगुली से जोड़ा गया है; यह वेणी से भी जुड़ सकता है। "
                   "‘कण्ठतालु’ द्वन्द्व समास है: कण्ठ और तालु। "
                   "स्पर्श का फल पंक्ति में नहीं बताया गया। "
                   "इकाई 76 की शर्त (अपरा न गिरे तो) यहाँ भी चलती लगती है।"),
    "hook": "वेणी या बाल-लिपटी अँगुली से कण्ठ-तालु छुए।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 79, what is to be touched?",
            ("The throat and the palate", "च कण्ठतालु परामृशेत्."),
            [("The two buttocks, gripped", "Gripping the buttocks is unit 78."),
             ("The hip, with the heel", "Striking the hip is unit 77."),
             ("The navel region, from above", "Pressing above the navel is unit 76.")],
            "The throat (कण्ठ) and palate (तालु) are touched.",
            "कण्ठतालु परामृशेत्."),
        order(1, "Put the parts of unit 79 in the line's order.",
              ["वेण्या", "अङ्गुल्या वा", "केशवेष्टितया", "च कण्ठतालु", "परामृशेत्"],
              "With a braid, or with a finger, wound with hair, and the throat and palate, one should touch.",
              "वेण्या → अङ्गुल्या वा → केशवेष्टितया → च कण्ठतालु → परामृशेत्."),
        match(2, "Match each word of unit 79 to its meaning.",
              [["वेणी", "braid"], ["अङ्गुलि", "finger"], ["केश", "hair"], ["कण्ठ", "throat"], ["तालु", "palate"]],
              "The two tools, what the finger is wound with, and the two places touched.",
              "वेणी, अङ्गुलि, केश, कण्ठ, तालु.", role="extend",
              teaches="कण्ठतालु is a dvandva: throat and palate, both touched."),
        mcq("discriminate", 3, "In unit 79, what case are वेण्या and अङ्गुल्या?",
            ("Instrumental singular: with a braid, with a finger", "The data: f. inst. sg. for both."),
            [("Locative singular: in a braid, in a finger", "The locative would be वेण्याम्, अङ्गुल्याम्."),
             ("Genitive singular: of a braid, of a finger", "The genitive would be वेण्याः, अङ्गुल्याः."),
             ("Nominative plural: braids, fingers", "The nominative plural would be वेण्यः, अङ्गुलयः.")],
            "-या here is the feminine instrumental singular: with.",
            "वेणी → वेण्या, अङ्गुलि → अङ्गुल्या (instrumental)."),
        multi("apply", 4, "Which statements does unit 79 support?",
              [("It states what the touch brings about", "The text states no effect of the touch."),
               ("The finger is wound round with thread", "The word is केश, hair, not thread."),
               ("A braid may be used for the touch", "Right: वेण्या, with a braid."),
               ("Both throat and palate are named", "Right: कण्ठतालु, a dvandva.")],
              [2, 3],
              "A braid or a hair-wound finger; throat and palate; no effect stated.",
              "वेण्याऽङ्गुल्या वा केशवेष्टितया च कण्ठतालु परामृशेत्."),
        mcq("transfer", 5, "By the form अङ्गुल्या (with a finger, from अङ्गुलि), how is with intelligence said from बुद्धि?",
            ("बुद्ध्या", "Feminine इ-stem: -इ → -या in the instrumental, as अङ्गुलि → अङ्गुल्या."),
            [("बुद्धिना", "-इना is the masculine/neuter pattern (मुनिना), not the feminine."),
             ("बुद्धेः", "बुद्धेः is genitive or ablative: of or from intelligence."),
             ("बुद्धौ", "बुद्धौ is locative: in intelligence.")],
            "बुद्धि → बुद्ध्या, like अङ्गुलि → अङ्गुल्या.",
            "Feminine इ-stem instrumental singular: -या.",
            teaches="A feminine इ- or ई-stem makes its instrumental singular in -या: अङ्गुलि → अङ्गुल्या, वेणी → वेण्या."),
    ],
}

# ---------------------------------------------------------------- unit 80
AUTHORED["80"] = {
    "title": "भूर्जपत्र ... सर्पनिर्मोकैश्च योनिं धूपयेत्",
    "question": "By unit 80, with what two sets of things is the yoni fumigated?",
    "rule": ("One should fumigate (धूपयेत्) the yoni with birch bark (भूर्जपत्र), काचमणि and snake slough (सर्पनिर्मोक); "
             "or (वा) with bhūrja and guggulu (Indian bdellium, Commiphora wightii; standard)."),
    "limits": ("Prose, medium confidence. काचमणि (literally glass-gem) has a doubtful sense and may be a corrupt word; it is "
               "not interpreted and no question rests on it. The placenta condition of unit 76 appears to carry on. No amount "
               "or duration is given."),
    "explain_hi": ("भूर्जपत्र यानी भोजपत्र, काचमणि और साँप की केंचुली (सर्पनिर्मोक) से योनि यानी जननमार्ग का धूपन करे; "
                   "या भूर्ज और गुग्गुलु (Commiphora wightii, मानक पहचान) से। "
                   "‘काचमणि’ का शाब्दिक अर्थ काँच-मणि है, पर यहाँ अर्थ संदिग्ध है; शब्द बिगड़ा हुआ हो सकता है। "
                   "‘धूपयेत्’ √धूप् का णिजन्त विधिलिङ् है: धूप दे। "
                   "इकाई 76 की शर्त (अपरा न गिरे तो) यहाँ भी चलती लगती है।"),
    "hook": "धूपन: भोजपत्र-केंचुली, या भूर्ज-गुग्गुलु।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 80, what is to be done to the yoni?",
            ("It is to be fumigated (धूपयेत्)", "योनिं धूपयेत्: one should fumigate the yoni."),
            [("It is to be anointed with ghee", "Anointing with ghee is in unit 81, not here."),
             ("It is to be washed with water", "No washing is named in unit 80."),
             ("It is to be smeared with paste", "Smearing comes in units 82 and 83.")],
            "The yoni is to be fumigated.",
            "योनिं धूपयेत्."),
        order(1, "Put these parts of unit 80 in the line's order.",
              ["भूर्जपत्र", "सर्पनिर्मोकैश्च", "योनिं", "धूपयेत्", "भूर्जगुग्गुलुभ्यां वा"],
              "Birch bark ... and snake slough, the yoni, one should fumigate, or with bhūrja and guggulu.",
              "भूर्जपत्र → सर्पनिर्मोकैश्च → योनिं → धूपयेत् → भूर्जगुग्गुलुभ्यां वा."),
        match(2, "Match each word of unit 80 to its meaning.",
              [["भूर्जपत्र", "birch bark"], ["सर्पनिर्मोक", "snake slough"],
               ["गुग्गुलु", "Indian bdellium (standard)"], ["धूपयेत्", "should fumigate"], ["योनि", "vagina (yoni)"]],
              "The fumigants, the action and the place.",
              "भूर्जपत्र, सर्पनिर्मोक, गुग्गुलु, धूपयेत्, योनि.", role="extend",
              teaches="निर्मोक = slough, the cast-off skin: सर्पनिर्मोक = snake slough."),
        mcq("discriminate", 3, "In unit 80, what does the closing वा (or) set apart?",
            ("A second set of fumigants: bhūrja and guggulu", "भूर्जगुग्गुलुभ्यां वा: or with bhūrja and guggulu."),
            [("A second place to fumigate, the head", "No other place is named; the yoni is the only place."),
             ("A second action, anointing instead", "The only verb in unit 80 is धूपयेत्."),
             ("A second time of day for fumigating", "No time of day is named in unit 80.")],
            "Two sets of fumigants, joined by वा.",
            "... धूपयेत् भूर्जगुग्गुलुभ्यां वा."),
        mcq("apply", 4, "Why does भूर्जगुग्गुलुभ्याम् take a dual ending?",
            ("It names two drugs, bhūrja and guggulu", "A dvandva of two members takes the dual: inst. du., with the two."),
            [("It names the two hands of the helper", "No hands are named in unit 80."),
             ("It is plural, for many kinds of resin", "-भ्याम् is a dual ending, not plural."),
             ("It names two snakes and their sloughs", "The snake slough is in the first set, inst. pl.")],
            "भूर्ज + गुग्गुलु: two members, dual instrumental.",
            "Two members → dual (-भ्याम्)."),
        mcq("transfer", 5, "By the rule of सर्पनिर्मोकैश्च, how is रामः + च (and Rāma) written when joined?",
            ("रामश्च", "Visarga before च becomes श्, as सर्पनिर्मोकैः + च → सर्पनिर्मोकैश्च."),
            [("रामो च", "अः → ओ only before a voiced sound; च is voiceless."),
             ("रामर्च", "र् comes from a visarga after vowels other than अ/आ, and only before voiced sounds."),
             ("रामच", "The visarga is not simply dropped before च.")],
            "रामः + च = रामश्च, like सर्पनिर्मोकैः + च.",
            "Visarga + च → श्च.",
            teaches="A visarga before च/छ becomes श्: सर्पनिर्मोकैः + च → सर्पनिर्मोकैश्च."),
    ],
}

# ---------------------------------------------------------------- unit 81
AUTHORED["81"] = {
    "title": "शालिमूलसिद्धेन वा सर्पिषा",
    "question": "By unit 81, with what is the yoni anointed, and with what is it then fumigated?",
    "rule": ("Or, having anointed the yoni with ghee (सर्पिस्) cooked with the root of śāli (a rice variety), one should "
             "fumigate (धूपयेत्) with kaṭukālābu (probably bitter bottle gourd), jālinī (a Luffa; disputed), nimba (neem; "
             "standard) and snake slough."),
    "limits": ("Prose, medium confidence. Printed योनिम्भ्यज्य is read योनिम् अभ्यज्य (a lost in print), and printed "
               "कदुकालाम्बु is normalised to कटुकालाबु, which may also be two drugs (kaṭukā and alābu). No question rests on "
               "these readings or on the identity of kaṭukālābu or jālinī. शालिमूल is given only literally."),
    "explain_hi": ("या शालि (धान की एक किस्म) की जड़ के साथ पकाए (सिद्ध) घी (सर्पिस्) से योनि का अभ्यंग करके धूपन करे। "
                   "धूपन के द्रव्य: कटुकालाबु (सम्भवतः कड़वी लौकी), जालिनी (सम्भवतः तोरई; पहचान विवादित), निम्ब (नीम, मानक) "
                   "और साँप की केंचुली। "
                   "‘कटुकालाबु’ दो द्रव्य (कटुका और अलाबु) भी हो सकते हैं, और छपा ‘योनिम्भ्यज्य’ में अ छूटा माना गया है; "
                   "इन पर कोई प्रश्न नहीं। "
                   "‘सर्पनिर्मोकैर्धूपयेत्’ में ऐ के बाद विसर्ग घोष ध से पहले र् बना है।"),
    "hook": "शालि-मूल का घी → अभ्यंग → नीम-केंचुली आदि का धूपन।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 81, the ghee used for anointing is cooked with what?",
            ("The root of śāli, a rice variety", "शालिमूलसिद्धेन सर्पिषा: ghee cooked with the śāli root."),
            [("Bhūrja bark and guggulu resin together", "Bhūrja and guggulu are fumigants in unit 80."),
             ("A paste of jaggery and dry ginger", "That paste is unit 83."),
             ("The leaves of the neem tree", "Neem is a fumigant here; no leaves or cooking with it.")],
            "Ghee cooked with śāli root.",
            "शालिमूलसिद्धेन सर्पिषा."),
        order(1, "Put the printed words of unit 81 in the line's order.",
              ["शालिमूलसिद्धेन", "वा", "सर्पिषा", "योनिम्भ्यज्य", "...सर्पनिर्मोकैर्धूपयेत्"],
              "With śāli-root-cooked, or, ghee, having anointed the yoni, ... with snake slough one should fumigate.",
              "शालिमूलसिद्धेन → वा → सर्पिषा → योनिम्भ्यज्य → ...सर्पनिर्मोकैर्धूपयेत्."),
        match(2, "Match each word of unit 81 to its meaning.",
              [["शालि", "a rice variety"], ["मूल", "root"], ["सिद्ध", "cooked"], ["सर्पिस्", "ghee"],
               ["निम्ब", "neem (standard)"]],
              "What the ghee is cooked with, the ghee itself, and one sure fumigant.",
              "शालि, मूल, सिद्ध, सर्पिस्, निम्ब.", role="extend",
              teaches="शालिमूलसिद्ध = cooked (सिद्ध) with the root (मूल) of śāli: a tatpuruṣa."),
        mcq("discriminate", 3, "Which split of सर्पनिर्मोकैर्धूपयेत् is right?",
            ("सर्पनिर्मोकैः + धूपयेत्", "Visarga after ऐ before the voiced ध becomes र्."),
            [("सर्पनिर्मोकः + धूपयेत्", "अः before a voiced sound would give ओ: सर्पनिर्मोको धूपयेत्."),
             ("सर्पनिर्मोकम् + धूपयेत्", "A final म् would give सर्पनिर्मोकं धूपयेत्, with no र्."),
             ("सर्पनिर्मोके + र्धूपयेत्", "र्धूपयेत् is not a word; the verb is धूपयेत्.")],
            "सर्पनिर्मोकैः (with snake sloughs) + धूपयेत् (should fumigate).",
            "ऐः + voiced sound → ऐर्."),
        multi("apply", 4, "Which of these are named as fumigants in unit 81?",
              [("Guggulu (Indian bdellium)", "Guggulu is a fumigant of unit 80, not 81."),
               ("Nimba (neem; standard)", "Right: निम्ब is in the fumigant list."),
               ("Jaggery (गुड)", "Jaggery is in the paste of unit 83."),
               ("Snake slough (सर्पनिर्मोक)", "Right: सर्पनिर्मोकैः closes the fumigant list.")],
              [1, 3],
              "Neem and snake slough are among the fumigants of unit 81.",
              "...निम्बसर्पनिर्मोकैर्धूपयेत्."),
        mcq("transfer", 5, "By the rule of सर्पनिर्मोकैर्धूपयेत्, how is देवैः + दत्तम् (given by the gods) written when joined?",
            ("देवैर्दत्तम्", "Visarga after ऐ before the voiced द becomes र्."),
            [("देवैदत्तम्", "The visarga is not simply dropped after ऐ."),
             ("देवैस्दत्तम्", "स् arises only before त/थ, not before द."),
             ("देवो दत्तम्", "ओ comes from अः, not from ऐः.")],
            "देवैः + दत्तम् = देवैर्दत्तम्, like सर्पनिर्मोकैः + धूपयेत्.",
            "ऐः + voiced sound → ऐर्.",
            teaches="A visarga after a vowel other than अ/आ becomes र् before a voiced sound: सर्पनिर्मोकैः + धूपयेत् → सर्पनिर्मोकैर्धूपयेत्."),
    ],
}

# ---------------------------------------------------------------- unit 82
AUTHORED["82"] = {
    "title": "अनभ्यक्तां वा ... तैलाक्तैरालिम्पेत्",
    "question": "By the sure words of unit 82, what action is enjoined, and with what kinds of things?",
    "rule": ("For one not anointed (अनभ्यक्ताम्), one should smear (आलिम्पेत्) with (things) mixed with kaṭu oil "
             "(probably mustard oil), made into a paste (कल्कीकृत), or smeared with oil (तैलाक्त)."),
    "limits": ("Prose, LOW confidence. The nouns are not printed: अनभ्यक्ताम् (f.) is probably the yoni or the woman; "
               "the instrumentals are probably the fumigants of unit 81. How the two वा divide is uncertain. No question "
               "rests on these points."),
    "explain_hi": ("यह पंक्ति कठिन है और केवल मोटे तौर पर पढ़ी जाती है: जिसका अभ्यंग न हुआ हो (अनभ्यक्ता), उस पर कटुतैल "
                   "(सम्भवतः सरसों का तेल) से मिले, कल्क बनाए हुए, या तेल से लिपे हुए (द्रव्यों) से लेप करे (आलिम्पेत्)। "
                   "संज्ञाएँ नहीं छपीं: ‘अनभ्यक्ताम्’ सम्भवतः योनि या स्त्री है, और तृतीया-पद सम्भवतः इकाई 81 के धूपन-द्रव्य हैं। "
                   "दो ‘वा’ विकल्पों को कैसे बाँटते हैं, यह अनिश्चित है; इन पर प्रश्न नहीं। "
                   "‘अनभ्यक्त’ = अन् (नहीं) + अभ्यक्त (अभ्यंग किया हुआ)।"),
    "hook": "अभ्यंग न हुआ हो तो: तेल-मिले, कल्क बने या तेल-लिपे से लेप।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 82, what is the action enjoined?",
            ("Smearing (आलिम्पेत्)", "The verb of the line is आलिम्पेत्, should smear."),
            [("Fumigating (धूपयेत्)", "Fumigation is units 80 and 81."),
             ("Eating (भक्षयेत्)", "Eating is unit 84."),
             ("Pouring (अनुषेचयेत्)", "Pouring over the head is unit 85.")],
            "One should smear.",
            "...आलिम्पेत्."),
        order(1, "Put the parts of unit 82 in the line's order.",
              ["अनभ्यक्तां वा", "कटुतैलमिश्रैः", "कल्कीकृतैर्वा", "तैलाक्तैः", "आलिम्पेत्"],
              "For one not anointed, or, mixed with kaṭu oil, made into paste, or, smeared with oil, one should smear.",
              "अनभ्यक्तां वा → कटुतैलमिश्रैः → कल्कीकृतैर्वा → तैलाक्तैः → आलिम्पेत्."),
        match(2, "Match each word of unit 82 to its meaning.",
              [["अनभ्यक्ता", "not anointed"], ["कल्कीकृत", "made into a paste"], ["तैलाक्त", "smeared with oil"],
               ["आलिम्पेत्", "should smear"], ["कटुतैल", "pungent oil (probably mustard oil)"]],
              "The sure words of the unit; their nouns are not printed.",
              "अनभ्यक्ता, कल्कीकृत, तैलाक्त, आलिम्पेत्, कटुतैल.", role="extend",
              teaches="कल्कीकृत = made (कृत) into a paste (कल्क): कल्क → कल्की + कृत, the cvi form: made into what it was not before."),
        mcq("discriminate", 3, "Which split of तैलाक्तैरालिम्पेत् is right?",
            ("तैलाक्तैः + आलिम्पेत्", "Visarga after ऐ before a vowel becomes र्."),
            [("तैलाक्तम् + आलिम्पेत्", "A final म् before a vowel would give तैलाक्तमालिम्पेत्."),
             ("तैलाक्तैः + रालिम्पेत्", "रालिम्पेत् is not a word; the verb is आलिम्पेत्."),
             ("तैलाक्ते + आलिम्पेत्", "ए before आ would not give ऐरा.")],
            "तैलाक्तैः (with ones smeared with oil) + आलिम्पेत् (should smear).",
            "ऐः + vowel → ऐर्."),
        mcq("apply", 4, "What does अन्- add in अनभ्यक्ताम् (unit 82)?",
            ("Negation: not anointed", "अन् + अभ्यक्ता = not anointed."),
            [("Repetition: anointed again", "Again would be पुनः, not अन्-."),
             ("Fullness: fully anointed", "अन्- does not mean fully."),
             ("Time: anointed beforehand", "अन्- is not a prefix of time.")],
            "अन्- before a vowel negates: अनभ्यक्ता = not anointed.",
            "अन्- (before a vowel) = not."),
        mcq("transfer", 5, "By the rule of तैलाक्त (तैल + अक्त), how is घृत + अक्त (smeared with ghee) written when joined?",
            ("घृताक्त", "अ + अ → आ, as तैल + अक्त → तैलाक्त."),
            [("घृतक्त", "The two अ do not merge into a single short अ."),
             ("घृतेक्त", "अ + अ does not give ए."),
             ("घृतोक्त", "अ + अ does not give ओ.")],
            "घृत + अक्त = घृताक्त, like तैल + अक्त = तैलाक्त.",
            "अ + अ → आ.",
            teaches="Two short अ join as आ: तैल + अक्तैः → तैलाक्तैः."),
    ],
}

# ---------------------------------------------------------------- unit 83
AUTHORED["83"] = {
    "title": "गुडनागरकल्केन वा",
    "question": "By unit 83, what paste is the further option?",
    "rule": ("Or with a paste (कल्क) of jaggery (गुड) and dry ginger (नागर, Zingiber officinale; standard). The verb "
             "आलिम्पेत् (should smear) is carried from unit 82."),
    "limits": ("Prose, two words, medium confidence. No verb is printed; what is smeared and how much paste are not stated. "
               "Unit 84 adds that this very paste may be eaten."),
    "explain_hi": ("या गुड़ और नागर यानी सोंठ (Zingiber officinale, मानक) के कल्क से। "
                   "पंक्ति में क्रिया नहीं है; ‘आलिम्पेत्’ (लेप करे) इकाई 82 से चलता है। "
                   "‘गुडनागर’ द्वन्द्व है (गुड़ और सोंठ), फिर ‘कल्क’ से तत्पुरुष: गुड़-सोंठ का कल्क। "
                   "‘कल्केन’ तृतीया है: कल्क से। मात्रा और लेप का स्थान नहीं कहा गया।"),
    "hook": "गुड़-सोंठ का कल्क: लेप (82 से), या खाना (84)।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 83, the paste is made of what?",
            ("Jaggery and dry ginger", "गुडनागरकल्केन: with a paste of guḍa and nāgara."),
            [("The root of lāṅgalī alone", "The lāṅgalī root paste is unit 85."),
             ("Kuṣṭha (costus) and elā", "Kuṣṭha and elā are in unit 89."),
             ("Bhūrja bark and guggulu", "Those are fumigants in unit 80.")],
            "A paste of jaggery and dry ginger.",
            "गुडनागरकल्केन."),
        match(1, "Match each word of unit 83 to its meaning.",
              [["गुड", "jaggery"], ["नागर", "dry ginger"], ["कल्क", "paste"], ["वा", "or"]],
              "Two drugs, the form of the preparation, and the link to the options.",
              "गुड, नागर, कल्क, वा."),
        fill(2, "In unit 83, the word for paste is ____ (type it in Devanagari or in English letters, e.g. dharma).",
             accepts("कल्क"),
             "गुडनागरकल्केन = with a paste (कल्क) of jaggery and dry ginger.",
             "कल्क = paste; कल्केन = with a paste (instrumental).",
             "कल्क = paste."),
        mcq("discriminate", 3, "Which verb is understood in unit 83?",
            ("आलिम्पेत्, should smear, from unit 82", "The note: the verb ālimpet is carried from the previous line."),
            [("धूपयेत्, should fumigate, from unit 81", "The note names ālimpet, not dhūpayet."),
             ("पाययेत्, should give to drink", "पाययेत् first comes in unit 86."),
             ("परामृशेत्, should touch, from unit 79", "The note names ālimpet, not parāmṛśet.")],
            "The paste is for smearing; unit 84 adds eating as a further option.",
            "Verb carried: आलिम्पेत्."),
        mcq("apply", 4, "What does the ending of कल्केन show?",
            ("Instrumental: with a paste", "-एन is the instrumental singular of an अ-stem."),
            [("Locative: in a paste", "The locative would be कल्के."),
             ("Dative: for a paste", "The dative would be कल्काय."),
             ("Genitive: of a paste", "The genitive would be कल्कस्य.")],
            "कल्केन = with (by means of) a paste.",
            "अ-stem instrumental singular: -एन."),
        mcq("transfer", 5, "By the form कल्केन (with a paste), how is with water said from जल?",
            ("जलेन", "अ-stem instrumental singular -एन, as कल्क → कल्केन."),
            [("जलस्य", "जलस्य is genitive: of water."),
             ("जले", "जले is locative: in water."),
             ("जलाय", "जलाय is dative: for water.")],
            "जल → जलेन, like कल्क → कल्केन.",
            "अ-stem instrumental: -एन.",
            teaches="An अ-stem makes its instrumental singular in -एन: कल्क → कल्केन (with a paste), जल → जलेन."),
    ],
}

# ---------------------------------------------------------------- unit 84
AUTHORED["84"] = {
    "title": "तदेववा भक्षयेत्",
    "question": "By unit 84, what is the further option?",
    "rule": ("Or one should eat (भक्षयेत्) that very (तत् एव) one; तत् most probably refers to the jaggery and dry ginger "
             "paste of unit 83. तत् + एव → तदेव (त् → द् before a vowel)."),
    "limits": ("Prose, high confidence. The noun that तत् stands for is not printed (most probably the paste of unit 83), "
               "and the subject is not stated (probably the woman). Printed joined as तदेववा."),
    "explain_hi": ("या उसी को खाए (भक्षयेत्)। "
                   "‘तत्’ की संज्ञा छपी नहीं; सबसे सम्भवतः यह इकाई 83 का गुड़-सोंठ का कल्क है। "
                   "कर्ता भी नहीं कहा गया (सम्भवतः स्त्री)। "
                   "‘एव’ ज़ोर देता है: वही। ‘तदेव’ में तत् + एव है (स्वर से पहले त् → द्)।"),
    "hook": "उसी को खाए: लेप भी, भोजन भी।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 84, what should be done with that very one?",
            ("It should be eaten (भक्षयेत्)", "तदेव वा भक्षयेत्: or one should eat that very one."),
            [("It should be poured on the head", "Pouring over the head is unit 85."),
             ("It should be used to fumigate", "Fumigation is units 80 and 81."),
             ("It should be tied to the hand", "Nothing is tied in unit 84.")],
            "That very one should be eaten.",
            "भक्षयेत्."),
        order(1, "Put the words of unit 84 in the line's order.",
              ["तत्", "एव", "वा", "भक्षयेत्"],
              "That, very, or, one should eat.",
              "तत् → एव → वा → भक्षयेत्."),
        match(2, "Match each word of unit 84 to its meaning.",
              [["तत्", "that"], ["एव", "very, itself"], ["वा", "or"], ["भक्षयेत्", "should eat"]],
              "Four words make the whole line.",
              "तत्, एव, वा, भक्षयेत्.", role="extend",
              teaches="एव after a word stresses it: तत् एव = that very one."),
        mcq("discriminate", 3, "Which split of तदेव is right?",
            ("तत् + एव", "त् becomes द् before a vowel: तत् + एव → तदेव."),
            [("तदा + एव", "आ + ए would give ऐ: तदैव."),
             ("तद + एव", "अ + ए would give ऐ: तदैव."),
             ("तदे + व", "Neither तदे nor व is the word here.")],
            "तत् (that) + एव (very).",
            "त् + vowel → द् + vowel."),
        multi("apply", 4, "Which statements about unit 84 are right?",
              [("The noun that तत् stands for is not printed", "Right: the noun is not stated; most probably the paste of unit 83."),
               ("The subject is named as the woman", "The subject is not stated; the woman is only a probable reading."),
               ("A new drug is named in unit 84", "No drug is named; तत् points back."),
               ("भक्षयेत् means should eat", "Right: 3 sg. optative of √भक्ष्.")],
              [0, 3],
              "Only तत्, एव, वा and भक्षयेत्: no noun, no subject, no new drug.",
              "तदेव वा भक्षयेत्."),
        mcq("transfer", 5, "By the rule of तदेव, how is एतत् + एव (this very) written when joined?",
            ("एतदेव", "त् → द् before a vowel, as तत् + एव → तदेव."),
            [("एततेव", "त् does not stay voiceless before a vowel here."),
             ("एतदैव", "The final त् does not merge its vowel with ए into ऐ."),
             ("एतेव", "The त् is not dropped.")],
            "एतत् + एव = एतदेव, like तत् + एव = तदेव.",
            "त् + vowel → द्.",
            teaches="A final त् becomes द् before a vowel: तत् + एव → तदेव."),
    ],
}

# ---------------------------------------------------------------- unit 85
AUTHORED["85"] = {
    "title": "लाङ्गलीमुलकल्केन वा पाणिमुदरं चालिम्पेत्",
    "question": "By unit 85, where is the lāṅgalī paste smeared, and what is poured over the head?",
    "rule": ("Or smear the hand (पाणि) and the belly (उदर) with a paste of lāṅgalī (glory lily) root. Or pour the milk "
             "(क्षीर, milky sap) of mahāvṛkṣa (disputed; probably snuhī, a spurge) over the head (मूर्ध्नि)."),
    "limits": ("Prose, two printed lines, medium confidence. Printed लाङ्गलीमुल is read मूल (root; short u flagged). "
               "पाणिम् is singular; whether one or both hands is not said. Mahāvṛkṣa's identity is disputed; no question "
               "rests on it. It appears to continue the placenta remedies from unit 76."),
    "explain_hi": ("या लाङ्गली यानी कलिहारी की जड़ के कल्क से हाथ और पेट (उदर) पर लेप करे। "
                   "या महावृक्ष (पहचान विवादित; सम्भवतः स्नुही यानी थूहर) का क्षीर, यानी पौधे का दूधिया रस, सिर पर डाले। "
                   "‘पाणिम्’ एकवचन है; एक हाथ या दोनों, नहीं कहा गया। "
                   "‘मूर्ध्न्यनुषेचयेत्’ में मूर्ध्नि + अनुषेचयेत् है (इ + अ → य)। "
                   "यह इकाई 76 से चल रहे अपरा-पातन के उपायों की कड़ी लगती है।"),
    "hook": "कलिहारी-मूल का लेप हाथ-पेट पर; महावृक्ष का दूध सिर पर।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 85, what is smeared with the lāṅgalī paste?",
            ("The hand and the belly", "पाणिमुदरं चालिम्पेत्: one should smear the hand and the belly."),
            [("The throat and the palate", "The throat and palate are touched in unit 79."),
             ("The two buttocks", "The buttocks are gripped and pressed in unit 78."),
             ("The head", "The head gets the poured milk of mahāvṛkṣa, not the paste.")],
            "The hand and the belly are smeared.",
            "पाणिम् उदरं च आलिम्पेत्."),
        order(1, "Put the parts of unit 85 in the line's order.",
              ["लाङ्गलीमुलकल्केन वा", "पाणिमुदरं चालिम्पेत्", "महावृक्षक्षीरं वा", "मूर्ध्न्यनुषेचयेत्"],
              "With lāṅgalī root paste, or, hand and belly one should smear; or mahāvṛkṣa milk on the head one should pour.",
              "लाङ्गलीमुलकल्केन वा → पाणिमुदरं चालिम्पेत् → महावृक्षक्षीरं वा → मूर्ध्न्यनुषेचयेत्."),
        match(2, "Match each word of unit 85 to its meaning.",
              [["पाणि", "hand"], ["उदर", "belly"], ["मूर्धन्", "head"], ["क्षीर", "milk, milky sap"],
               ["अनुषेचयेत्", "should pour over"]],
              "The places, the liquid and the action of the two lines.",
              "पाणि, उदर, मूर्धन्, क्षीर, अनुषेचयेत्.", role="extend",
              teaches="क्षीर of a plant = its milky sap (latex)."),
        mcq("discriminate", 3, "Which split of मूर्ध्न्यनुषेचयेत् is right?",
            ("मूर्ध्नि + अनुषेचयेत्", "इ + अ → य: मूर्ध्नि (on the head) + अनुषेचयेत्."),
            [("मूर्ध्नः + अनुषेचयेत्", "अः + अ would give ओऽ: मूर्ध्नोऽनुषेचयेत्."),
             ("मूर्ध्ने + अनुषेचयेत्", "ए + अ would give एऽ: मूर्ध्नेऽनुषेचयेत्."),
             ("मूर्ध्न्य + नुषेचयेत्", "नुषेचयेत् is not a word; the verb is अनुषेचयेत्.")],
            "मूर्ध्नि (loc., on the head) + अनुषेचयेत् (should pour over).",
            "इ + a different vowel → य्."),
        mcq("apply", 4, "In unit 85, what is done with the milk of mahāvṛkṣa?",
            ("It is poured over the head", "महावृक्षक्षीरं वा मूर्ध्न्यनुषेचयेत्."),
            [("It is smeared on the belly", "The belly gets the lāṅgalī root paste."),
             ("It is given to drink", "No drinking is named in unit 85."),
             ("It is used for fumigating", "No fumigation is named in unit 85.")],
            "The milk (sap) is poured over the head.",
            "मूर्ध्नि अनुषेचयेत्."),
        mcq("transfer", 5, "By the rule of चालिम्पेत् (च + आलिम्पेत्), how is न + आगच्छति (does not come) written when joined?",
            ("नागच्छति", "अ + आ → आ, as च + आलिम्पेत् → चालिम्पेत्."),
            [("नेगच्छति", "अ + आ does not give ए."),
             ("नौगच्छति", "अ + आ does not give औ."),
             ("नगच्छति", "The long आ is not shortened away.")],
            "न + आगच्छति = नागच्छति, like च + आलिम्पेत्.",
            "अ + आ → आ.",
            teaches="A short अ before आ merges into आ: च + आलिम्पेत् → चालिम्पेत्."),
    ],
}

# ---------------------------------------------------------------- unit 86
AUTHORED["86"] = {
    "title": "कुष्ठताली सकल्कं ... पाययेत्",
    "question": "By the sure parts of unit 86, with which vehicles is the drink to be given?",
    "rule": ("Kuṣṭha (costus) and tālī (unclear), with paste, should be given to drink (पाययेत्, causative) with any one "
             "(अन्यतम) of bilva ... surā and (surā-)maṇḍa; or with a sour (one) sharp and hot with vyoṣa (the three pungents); or "
             "with horse-gram (कुलत्थ) juice; or with madhuka and pippalī cooked together."),
    "limits": ("Prose, LOW confidence. ताली is unclear (perhaps a truncated tālīsa), bilvaja is unclear, and the opening "
               "may be divided another way (kuṣṭha-tālīsa-kalkam, not adopted). The object of पाययेत् is not plainly "
               "stated. No question rests on these. Madhuka is probably licorice (probable)."),
    "explain_hi": ("यह कठिन पंक्ति है: कुष्ठ यानी कूठ और अस्पष्ट शब्द ताली, कल्क के साथ, पिलाना चाहिए (पाययेत्, णिजन्त)। "
                   "चार विकल्प ‘वा’ से जुड़े हैं: (1) बिल्व, बिल्वज, यूष, मैरेय, आसव, सुरा और मण्ड में से कोई एक; "
                   "(2) व्योष (सोंठ, पीपर, काली मिर्च) से तीखा और गरम खट्टा; (3) कुलथी का रस; (4) मधुक (सम्भवतः मुलेठी) "
                   "और पिप्पली का संपाक। "
                   "‘ताली’ और ‘बिल्वज’ अस्पष्ट हैं, और आरम्भ का शब्द-विभाग दूसरी तरह (कुष्ठ-तालीस-कल्कम्) भी हो सकता है; इन पर प्रश्न नहीं।"),
    "hook": "पिलाओ: बिल्वादि में से कोई, या व्योष-अम्ल, या कुलथी-रस, या मधुक-पिप्पली।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 86, what should be done?",
            ("Something should be given to drink", "पाययेत्: should be given to drink (causative of √पा)."),
            [("Something should be smeared on", "Smearing is units 82 and 85."),
             ("Something should be eaten", "Eating is unit 84."),
             ("Something should be burnt as fumes", "Fumigation is units 80 and 81.")],
            "The verb is पाययेत्: give to drink.",
            "...पाययेत्."),
        order(1, "Put the four vehicles of unit 86 in the line's order.",
              ["बिल्व ... सुरामन्दान्यतमेन", "व्योषतीक्ष्णोष्णेन वाऽम्लेन", "कुलत्थरसेन", "मधुकपिप्पलीसंपाकेन वा"],
              "Any one of bilva ... maṇḍa; or a sour one hot with vyoṣa; horse-gram juice; or madhuka-pippalī cooked together.",
              "अन्यतमेन → अम्लेन → कुलत्थरसेन → मधुकपिप्पलीसंपाकेन."),
        match(2, "Match each word of unit 86 to its meaning.",
              [["व्योष", "the three pungents"], ["कुलत्थ", "horse gram"], ["पिप्पली", "long pepper"],
               ["अम्ल", "sour"], ["अन्यतम", "any one (of several)"]],
              "Sure words of the four vehicles.",
              "व्योष, कुलत्थ, पिप्पली, अम्ल, अन्यतम.", role="extend",
              teaches="व्योष names a group of three pungents: dry ginger, long pepper and black pepper (standard)."),
        mcq("discriminate", 3, "What does पाययेत् (causative of √पा, to drink) mean?",
            ("Should make someone drink, give to drink", "The causative: cause to drink."),
            [("Should drink it oneself", "Drinking oneself would be पिबेत्, not the causative."),
             ("Has already been drunk", "पाययेत् is an optative, not a past form."),
             ("Will drink it later on", "पाययेत् is not a future form.")],
            "पाययेत् = should give to drink.",
            "Causative: cause someone to do the action."),
        multi("apply", 4, "Which vehicles for the drink does unit 86 name?",
              [("Ghee cooked with śāli root", "That ghee is for anointing in unit 81."),
               ("Horse-gram juice (कुलत्थरस)", "Right: कुलत्थरसेन."),
               ("Madhuka and pippalī cooked together", "Right: मधुकपिप्पलीसंपाकेन."),
               ("The milk of mahāvṛkṣa", "That milk is poured over the head in unit 85.")],
              [1, 2],
              "Horse-gram juice and the madhuka-pippalī cooking are two of the four vehicles.",
              "कुलत्थरसेन, मधुकपिप्पलीसंपाकेन."),
        mcq("transfer", 5, "By पाययेत् (should make drink), what does कारयेत्, causative of √कृ (to do), mean?",
            ("Should have it done, cause it to be done", "The causative adds cause to: √कृ do → कारयेत् cause to do."),
            [("Should do it oneself", "Doing oneself would be कुर्यात्."),
             ("Has done it already", "कारयेत् is an optative, not a past form."),
             ("Is unable to do it", "Nothing in the form says unable.")],
            "कारयेत् = should have it done, like पाययेत् = should have (someone) drink.",
            "Causative optative: should cause to ...",
            teaches="A causative adds cause to: √पा drink → पाययेत् should give to drink; √कृ do → कारयेत् should have it done."),
    ],
}

# ---------------------------------------------------------------- unit 87
AUTHORED["87"] = {
    "title": "पिप्पल्येलाकोलविडचव्यचित्रकोपकुञ्चिकाकल्कं वा",
    "question": "By unit 87, of which drugs is the further paste made?",
    "rule": ("Or a paste (कल्क) of pippalī (long pepper), elā (probably cardamom), kola (probably jujube fruit), viḍa (a drug "
             "name), cavya (probably Piper chaba), citraka (leadwort; standard) and upakuñcikā (probably nigella; disputed). "
             "The verb, should be given to drink, is carried from unit 86."),
    "limits": ("Prose, medium confidence. No verb is printed. Viḍa is only a drug name here (no identification); upakuñcikā "
               "is disputed; no question rests on their identity. No amounts are given."),
    "explain_hi": ("या पिप्पली (पीपर), एला (सम्भवतः इलायची), कोल (सम्भवतः बेर का फल), विड (एक द्रव्य का नाम), चव्य "
                   "(सम्भवतः चव), चित्रक (चीता, मानक) और उपकुञ्चिका (सम्भवतः कलौंजी; पहचान विवादित) का कल्क। "
                   "क्रिया ‘पिलाए’ इकाई 86 से चलती है। "
                   "‘पिप्पल्येला’ में पिप्पली + एला (ई + ए → ये), और ‘चित्रकोपकुञ्चिका’ में चित्रक + उपकुञ्चिका (अ + उ → ओ)।"),
    "hook": "सात द्रव्यों का कल्क: पि-ए-को-वि-च-चि-उ।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 87, what is made of the listed drugs?",
            ("A paste (कल्क)", "...उपकुञ्चिकाकल्कं वा: or a paste of these."),
            [("A decoction (कषाय)", "A decoction is in unit 90."),
             ("A fumigation (धूप)", "Fumigation is units 80 and 81."),
             ("A cooked ghee (सर्पिस्)", "Cooked ghee is unit 81.")],
            "The drugs are made into a paste.",
            "...कल्कं वा."),
        order(1, "Put the first six drugs of unit 87 in the line's order.",
              ["पिप्पली", "एला", "कोल", "विड", "चव्य", "चित्रक"],
              "Pippalī, elā, kola, viḍa, cavya, citraka, then upakuñcikā.",
              "पिप्पली → एला → कोल → विड → चव्य → चित्रक."),
        match(2, "Match each drug of unit 87 to its identification, with the data's label.",
              [["पिप्पली", "long pepper"], ["चित्रक", "leadwort (standard)"], ["एला", "cardamom (probable)"],
               ["कोल", "jujube fruit (probable)"], ["चव्य", "Piper chaba (probable)"]],
              "Five of the seven drugs; viḍa and upakuñcikā are left out (no sure identification).",
              "पिप्पली, चित्रक, एला, कोल, चव्य.", role="extend",
              teaches="An identification keeps its label: citraka = leadwort (standard), elā = cardamom (probable)."),
        mcq("discriminate", 3, "Which split of पिप्पल्येला is right?",
            ("पिप्पली + एला", "ई + ए → ये: पिप्पली + एला = पिप्पल्येला."),
            [("पिप्पल + एला", "अ + ए would give ऐ: पिप्पलैला."),
             ("पिप्पल्य + एला", "अ + ए would give ऐ: पिप्पल्यैला."),
             ("पिप्पल्ये + ला", "ला is not a word; the drug is एला.")],
            "पिप्पली (long pepper) + एला (probably cardamom).",
            "ई + a different vowel → य्."),
        mcq("apply", 4, "Which verb is understood in unit 87?",
            ("Should be given to drink, from unit 86", "The note: the verb is carried from the line of unit 86."),
            [("Should smear, from unit 82", "The note names the drinking verb of unit 86."),
             ("Should fumigate, from unit 81", "The note names the drinking verb of unit 86."),
             ("Should eat, from unit 84", "The note names the drinking verb of unit 86.")],
            "वा adds this paste to the drink options of unit 86.",
            "Verb carried: पाययेत्."),
        mcq("transfer", 5, "By the rule of पिप्पल्येला, how is नदी + एव (the river itself) written when joined?",
            ("नद्येव", "ई + ए → ये, as पिप्पली + एला → पिप्पल्येला."),
            [("नदैव", "ई + ए does not give ऐ."),
             ("नदीव", "The ए is not dropped after ई."),
             ("नदेव", "ई + ए does not give a plain ए.")],
            "नदी + एव = नद्येव, like पिप्पली + एला.",
            "ई + a different vowel → य्.",
            teaches="A final ई before a different vowel becomes य्: पिप्पली + एला → पिप्पल्येला."),
    ],
}

# ---------------------------------------------------------------- unit 88
AUTHORED["88"] = {
    "title": "खरस्य वृषभस्य वा जीवतो दक्षिणं कर्णमुद्धृत्य",
    "question": "By unit 88, what are the steps of the ear-dip preparation?",
    "rule": ("Take out the right ear (दक्षिणं कर्णम्) of a living donkey or bull; put it into any one of the dips "
             "(आप्लवन) beginning with bilva, bilvaja and yūṣa; take it out after it has stayed a muhūrta; then give that "
             "dip to drink (तदाप्लवनं पाययेत्)."),
    "limits": ("Prose, medium confidence. The text does not give the length of a muhūrta (about 48 minutes in standard "
               "reckoning). Bilvaja is unclear. Who drinks is not stated. The card reports the procedure as the text "
               "states it."),
    "explain_hi": ("गधे या बैल के जीवित रहते उसका दाहिना कान निकालकर, बिल्व, बिल्वज और यूष आदि आप्लवनों (डुबाने वाले द्रव) "
                   "में से किसी एक में डाले; मुहूर्त भर रहने पर निकालकर वह आप्लवन पिलाए। "
                   "मुहूर्त की लम्बाई पाठ में नहीं दी गई (सामान्य गणना में लगभग 48 मिनट)। ‘बिल्वज’ अस्पष्ट है। "
                   "क्रम पूर्वकालिक क्रियाओं (उद्धृत्य, प्रक्षिप्य, उद्धृत्य) से बनता है, अन्त में ‘पाययेत्’। "
                   "‘जीवतो दक्षिणम्’ में जीवतः + दक्षिणम् है (अः → ओ घोष द से पहले)।"),
    "hook": "कान निकाल → आप्लवन में डाल → मुहूर्त बाद निकाल → वही पिला।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 88, which ear is taken out?",
            ("The right ear", "दक्षिणं कर्णमुद्धृत्य: having taken out the right ear."),
            [("The left ear", "The line says दक्षिणम्, right."),
             ("Both of the ears", "कर्णम् is singular: one ear."),
             ("Any ear at all", "The line names the right ear.")],
            "The right ear of a living donkey or bull.",
            "दक्षिणं कर्णम्."),
        order(1, "Put the steps of unit 88 in the line's order.",
              ["खरस्य वृषभस्य वा जीवतो", "दक्षिणं कर्णमुद्धृत्य", "आप्लवनानामन्यतमे प्रक्षिप्य",
               "मुहूर्तस्थितमुद्धृत्य", "तदाप्लवनं पाययेत्"],
              "Of a living donkey or bull, take out the right ear, put it into one of the dips, take it out after a muhūrta, give that dip to drink.",
              "खरस्य... → कर्णमुद्धृत्य → प्रक्षिप्य → मुहूर्तस्थितमुद्धृत्य → पाययेत्."),
        match(2, "Match each word of unit 88 to its meaning.",
              [["खर", "donkey"], ["वृषभ", "bull"], ["दक्षिण", "right (side)"], ["आप्लवन", "dip, immersion liquid"],
               ["मुहूर्त", "a short period (muhūrta)"]],
              "The animals, the side, the liquid and the time.",
              "खर, वृषभ, दक्षिण, आप्लवन, मुहूर्त.", role="extend",
              teaches="A chain of absolutives (उद्धृत्य, प्रक्षिप्य, उद्धृत्य) gives the steps in order, ending in one finite verb (पाययेत्)."),
        mcq("discriminate", 3, "Why is जीवतः printed जीवतो before दक्षिणं?",
            ("अः becomes ओ before a voiced sound such as द", "जीवतः + दक्षिणम् → जीवतो दक्षिणम्."),
            [("अः becomes ओ before every consonant", "Before a voiceless त it gives स्त, not ओ."),
             ("The stem of the word ends in ओ", "The stem is जीवत्; the form is जीवतः (gen. sg.)."),
             ("The ओ marks a dual form", "जीवतः here is genitive singular, of a living (one).")],
            "जीवतः (of a living one) + दक्षिणम् (right).",
            "अः + voiced consonant → ओ."),
        mcq("apply", 4, "By unit 88, what is finally given to drink?",
            ("That dip (तदाप्लवनम्)", "तदाप्लवनं पाययेत्: one should give that dip to drink."),
            [("The ear itself, ground up", "The ear is taken out of the dip; it is not given."),
             ("Plain surā, with nothing added", "The drink is the dip in which the ear stayed."),
             ("Milk of the same animal", "No milk is named in unit 88.")],
            "The dip in which the ear stayed a muhūrta.",
            "तदाप्लवनं पाययेत्."),
        mcq("transfer", 5, "By उद्धृत्य and प्रक्षिप्य, what is the absolutive (having deposited) of नि + √क्षिप्?",
            ("निक्षिप्य", "With a prefix the absolutive takes -य, as प्र + √क्षिप् → प्रक्षिप्य."),
            [("निक्षिप्त्वा", "-त्वा is used without a prefix; with नि the ending is -य."),
             ("निक्षिप्तः", "निक्षिप्तः is a past participle, deposited."),
             ("निक्षिपति", "निक्षिपति is the present, deposits.")],
            "नि + √क्षिप् → निक्षिप्य, like प्रक्षिप्य.",
            "Prefix + root → absolutive in -य.",
            teaches="With a prefix the absolutive ends in -य: प्रक्षिप्य (having put in), निक्षिप्य (having deposited)."),
    ],
}

# ---------------------------------------------------------------- unit 89
AUTHORED["89"] = {
    "title": "कुष्ठैलाकल्कं वा सुरया",
    "question": "By unit 89, what paste is given, and with what?",
    "rule": ("Or a paste (कल्क) of kuṣṭha (costus) and elā (probably cardamom) with surā (grain liquor). The verb, should be "
             "given to drink, is carried from unit 86. कुष्ठ + एला → कुष्ठैला (अ + ए → ऐ)."),
    "limits": ("Prose, medium confidence. No verb is printed; amounts are not given."),
    "explain_hi": ("या कुष्ठ यानी कूठ और एला (सम्भवतः इलायची) का कल्क, सुरा (अन्न से बनी मदिरा) के साथ। "
                   "क्रिया ‘पिलाए’ इकाई 86 से चलती है। "
                   "‘सुरया’ तृतीया है: सुरा के साथ। "
                   "‘कुष्ठैला’ में कुष्ठ + एला है (अ + ए → ऐ)।"),
    "hook": "कूठ-इलायची का कल्क, सुरा के साथ।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 89, with what is the kuṣṭha and elā paste taken?",
            ("With surā (grain liquor)", "कुष्ठैलाकल्कं वा सुरया."),
            [("With horse-gram (kulattha) juice", "Horse-gram juice is a vehicle of unit 86."),
             ("With ghee cooked with śāli root", "That ghee is for anointing in unit 81."),
             ("With the ear-dip", "The ear-dip is unit 88.")],
            "The paste goes with surā.",
            "सुरया."),
        order(1, "Put the words of unit 89 in the line's order.",
              ["कुष्ठ", "एला", "कल्कम्", "वा", "सुरया"],
              "Kuṣṭha, elā, paste, or, with surā.",
              "कुष्ठ → एला → कल्कम् → वा → सुरया."),
        match(2, "Match each word of unit 89 to its meaning.",
              [["कुष्ठ", "costus"], ["एला", "cardamom (probable)"], ["कल्क", "paste"], ["सुरा", "grain liquor"]],
              "Two drugs, the preparation and the vehicle.",
              "कुष्ठ, एला, कल्क, सुरा.", role="extend",
              teaches="कुष्ठैलाकल्क = a paste of kuṣṭha and elā: a dvandva inside a tatpuruṣa."),
        mcq("discriminate", 3, "Which split of कुष्ठैला is right?",
            ("कुष्ठ + एला", "अ + ए → ऐ: कुष्ठ + एला = कुष्ठैला."),
            [("कुष्ठः + एला", "अः before ए drops its visarga and does not join: कुष्ठ एला."),
             ("कुष्ठै + ला", "ला is not a word; the drug is एला."),
             ("कुष्ठे + एला", "ए before ए would not give ऐ.")],
            "कुष्ठ (costus) + एला (probably cardamom).",
            "अ + ए → ऐ."),
        mcq("apply", 4, "What does the ending of सुरया show?",
            ("Instrumental: with surā", "The data: f. inst. sg., with surā."),
            [("Locative: in surā", "The locative would be सुरायाम्."),
             ("Genitive: of surā", "The genitive would be सुरायाः."),
             ("Nominative: surā itself", "The nominative would be सुरा.")],
            "सुरया = with surā.",
            "आ-stem feminine instrumental singular: -अया."),
        mcq("transfer", 5, "By the rule of कुष्ठैला, how is तत्र + एव (there itself) written when joined?",
            ("तत्रैव", "अ + ए → ऐ, as कुष्ठ + एला → कुष्ठैला."),
            [("तत्रेव", "अ + ए gives ऐ, not ए."),
             ("तत्रौव", "अ + ए does not give औ."),
             ("तत्र्येव", "य् arises from इ/ई, not from अ.")],
            "तत्र + एव = तत्रैव, like कुष्ठ + एला.",
            "अ + ए → ऐ.",
            teaches="A short अ before ए joins as ऐ: कुष्ठ + एला → कुष्ठैला."),
    ],
}

# ---------------------------------------------------------------- unit 90
AUTHORED["90"] = {
    "title": "अर्कालेर्ककषायं वा सुरोन्मिश्रं",
    "question": "By the sure words of unit 90, what kind of preparation is given, and mixed with what?",
    "rule": ("Or a decoction (कषाय) ... mixed with surā (सुरोन्मिश्रम्; सुरा + उन्मिश्रम्, आ + उ → ओ). The verb, should be "
             "given to drink, is carried from unit 86."),
    "limits": ("Prose, LOW confidence. The split of printed अर्कालेर्क is doubtful (arka + ala + arka, or arka + alarka); "
               "the drugs of the decoction are not settled, so no question rests on them. Only कषाय (decoction) and the "
               "mixing with surā are asked."),
    "explain_hi": ("या (कुछ द्रव्यों का) काढ़ा (कषाय), सुरा में मिलाया हुआ। "
                   "छपा ‘अर्कालेर्क’ संदिग्ध है: अर्क (आक, सम्भावित) + अस्पष्ट ‘अला’ + अर्क, या अर्क + अलर्क (विवादित); "
                   "इसलिए काढ़े के द्रव्यों पर कोई प्रश्न नहीं। "
                   "‘सुरोन्मिश्रम्’ = सुरा + उन्मिश्रम् (आ + उ → ओ)। "
                   "क्रिया ‘पिलाए’ इकाई 86 से चलती है।"),
    "hook": "काढ़ा, सुरा में मिला।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 90, the decoction is mixed with what?",
            ("With surā", "सुरोन्मिश्रम्: mixed with surā."),
            [("With honey", "No honey is named in unit 90."),
             ("With ghee", "No ghee is named in unit 90."),
             ("With milk", "No milk is named in unit 90.")],
            "The decoction is mixed with surā.",
            "सुरोन्मिश्रम्."),
        match(1, "Match each word of unit 90 to its meaning.",
              [["कषाय", "decoction"], ["सुरा", "grain liquor"], ["उन्मिश्र", "mixed"], ["वा", "or"]],
              "The sure words of the unit.",
              "कषाय, सुरा, उन्मिश्र, वा."),
        fill(2, "Join सुरा + उन्मिश्रम्: ____ (type it in Devanagari or in English letters, e.g. dharma).",
             accepts("सुरोन्मिश्रम्"),
             "आ + उ → ओ: सुरा + उन्मिश्रम् = सुरोन्मिश्रम् (printed सुरोन्मिश्रं).",
             "A final आ before उ joins as ओ: सुरा + उन्मिश्रम् → सुरोन्मिश्रम्.",
             "आ + उ → ओ."),
        mcq("discriminate", 3, "Which split of सुरोन्मिश्रम् is right?",
            ("सुरा + उन्मिश्रम्", "आ + उ → ओ: सुरा (grain liquor) + उन्मिश्रम् (mixed)."),
            [("सुरो + न्मिश्रम्", "न्मिश्रम् is not a word; the word is उन्मिश्रम्."),
             ("सुराः + उन्मिश्रम्", "आः drops its visarga before a vowel and does not join: सुरा उन्मिश्रम्."),
             ("सुरौ + उन्मिश्रम्", "औ before उ would give आवु: सुरावुन्मिश्रम्.")],
            "सुरा + उन्मिश्रम् = सुरोन्मिश्रम्.",
            "आ + उ → ओ."),
        mcq("apply", 4, "In unit 90, what kind of preparation is कषाय?",
            ("A decoction", "The note: kaṣāya here is the preparation, decoction."),
            [("A paste", "A paste is कल्क, as in units 87 and 89."),
             ("A fumigation", "Fumigation is धूप, units 80 and 81."),
             ("An oil", "Oil is तैल, as in unit 82.")],
            "कषाय = decoction.",
            "कषाय = decoction; कल्क = paste."),
        mcq("transfer", 5, "By the rule of सुरोन्मिश्रम्, how is महा + उत्सवः (a great festival) written when joined?",
            ("महोत्सवः", "आ + उ → ओ, as सुरा + उन्मिश्रम् → सुरोन्मिश्रम्."),
            [("महौत्सवः", "आ + उ does not give औ."),
             ("महुत्सवः", "The आ is not simply dropped before उ."),
             ("महात्सवः", "The उ is not dropped after आ.")],
            "महा + उत्सवः = महोत्सवः, like सुरा + उन्मिश्रम्.",
            "आ + उ → ओ.",
            teaches="A final आ before उ joins as ओ: सुरा + उन्मिश्रम् → सुरोन्मिश्रम्."),
    ],
}

# ===================================================================== NOTES_HI
NOTES_HI = {
    "78": ("गद्य; विश्वास उच्च; कोई पाठ-चिह्न नहीं। ‘सुपीडितं पीडयेत्’ सजातीय प्रयोग (अच्छी तरह दबाए)। इकाई 76 की शर्त "
           "(अपरा न गिरे तो) यहाँ चलती लगती है, दोहराई नहीं गई। छपा ‘उपसंगृह्य’ = उपसङ्गृह्य। सन्धि जाँची: वा + उपसंगृह्य → "
           "वोपसंगृह्य (आ + उ → ओ); सुपीडितम् + पीडयेत् → सुपीडितं पीडयेत् (व्यंजन से पहले म् → अनुस्वार)।"),
    "79": ("गद्य; विश्वास मध्यम; कोई पाठ-चिह्न नहीं। ‘केशवेष्टितया’ अँगुली से जोड़ा गया; वेणी से भी जुड़ सकता है — इस पर प्रश्न नहीं। "
           "स्पर्श का फल नहीं कहा गया। छपा ‘चकण्ठतालु’ = च कण्ठतालु। छपा ‘वेण्याऽङ्गुल्या’: नियमित सन्धि आ + अ → आ है, "
           "ऽ केवल मिले हुए अ का संकेत है। इकाई 76 की शर्त यहाँ चलती लगती है।"),
    "80": ("गद्य; विश्वास मध्यम; कोई पाठ-चिह्न नहीं। ‘काचमणि’ (शाब्दिक: काँच-मणि) का अर्थ संदिग्ध, शब्द बिगड़ा हो सकता है; "
           "व्याख्या नहीं की गई और इस पर प्रश्न नहीं। गुग्गुलु = Commiphora wightii (मानक)। छपा ‘धूपयेत्भूर्ज…’ बिना अन्तराल; "
           "नियमित सन्धि में घोष भ से पहले त् → द् (धूपयेद्भूर्ज…) होता। सन्धि जाँची: सर्पनिर्मोकैः + च → सर्पनिर्मोकैश्च "
           "(विसर्ग → श्); योनिम् → योनिं (व्यंजन से पहले)।"),
    "81": ("गद्य; विश्वास मध्यम। पाठ-चिह्न: छपा ‘योनिम्भ्यज्य’ → योनिम् अभ्यज्य (अ छूटा); छपा ‘कदुकालाम्बु’ → कटुकालाबु "
           "(ड/ट और अलाम्बु/अलाबु)। ‘कटुकालाबु’ एक द्रव्य (कड़वी लौकी, सम्भावित) या दो (कटुका + अलाबु) — तय नहीं; जालिनी "
           "विवादित; इन पर प्रश्न नहीं। शालिमूल का केवल शाब्दिक अर्थ। सन्धि जाँची: योनिम् + अभ्यज्य → योनिमभ्यज्य; कटुक + "
           "अलाबु → कटुकालाबु (अ + अ → आ); सर्पनिर्मोकैः + धूपयेत् → सर्पनिर्मोकैर्धूपयेत् (ऐ के बाद विसर्ग → र्)।"),
    "82": ("गद्य; विश्वास निम्न; कोई पाठ-चिह्न नहीं। संज्ञाएँ नहीं छपीं: ‘अनभ्यक्ताम्’ (स्त्रीलिंग) सम्भवतः योनि या स्त्री; तृतीया-पद "
           "सम्भवतः इकाई 81 के धूपन-द्रव्य। दो ‘वा’ की रचना अनिश्चित। कटुतैल = सम्भवतः सरसों का तेल (सम्भावित)। सन्धि जाँची: "
           "अन् + अभ्यक्ताम् → अनभ्यक्ताम्; कल्कीकृतैः + वा → कल्कीकृतैर्वा; तैल + अक्तैः → तैलाक्तैः (अ + अ → आ); "
           "तैलाक्तैः + आलिम्पेत् → तैलाक्तैरालिम्पेत्।"),
    "83": ("गद्य; विश्वास मध्यम; कोई पाठ-चिह्न नहीं। क्रिया ‘आलिम्पेत्’ इकाई 82 से। नागर = सोंठ (Zingiber officinale, मानक)। "
           "‘गुडनागर’ द्वन्द्व + ‘कल्क’ तत्पुरुष। कोई सन्धि-परिवर्तन नहीं।"),
    "84": ("गद्य; विश्वास उच्च; कोई पाठ-चिह्न नहीं। छपा ‘तदेववा’ एक टोकन = तत् एव वा। ‘तत्’ सबसे सम्भवतः इकाई 83 का गुड़-सोंठ "
           "कल्क (संज्ञा छपी नहीं); कर्ता नहीं कहा गया। सन्धि जाँची: तत् + एव → तदेव (स्वर से पहले त् → द्)।"),
    "85": ("गद्य (दो छपी पंक्तियाँ जोड़ी गईं); विश्वास मध्यम। पाठ-चिह्न: ‘लाङ्गलीमुल’ → लाङ्गलीमूल (ह्रस्व उ)। [02.03.91] ‘पाणिम्’ "
           "एकवचन; एक या दोनों हाथ, नहीं कहा। लाङ्गली = कलिहारी (देखें इकाई 44)। [02.03.92] महावृक्ष की पहचान विवादित "
           "(सम्भवतः स्नुही/थूहर); पौधे का क्षीर = दूधिया रस। सन्धि जाँची: पाणिम् + उदरम् → पाणिमुदरम्; च + आलिम्पेत् → "
           "चालिम्पेत् (अ + आ → आ); मूर्ध्नि + अनुषेचयेत् → मूर्ध्न्यनुषेचयेत् (इ + अ → य)।"),
    "86": ("गद्य; विश्वास निम्न। पाठ-चिह्न: ‘सुरामन्द’ → सम्भवतः सुरामण्ड (दन्त्य न)। ‘ताली’ अस्पष्ट (सम्भवतः अधूरा तालीस); "
           "‘बिल्वज’ अस्पष्ट; ‘बिल्वबिल्वजयूष’ को बिल्व + बिल्वज-यूष भी पढ़ा जा सकता है। समीक्षा-टिप्पणी: आरम्भ ‘कुष्ठ-तालीस-कल्कम्’ "
           "भी हो सकता है (अपनाया नहीं)। पाययेत् का कर्म स्पष्ट नहीं। मधुक = मुलेठी (सम्भावित)। इन बिन्दुओं पर प्रश्न नहीं। "
           "सन्धि जाँची: तीक्ष्ण + उष्णेन → तीक्ष्णोष्णेन (अ + उ → ओ); मण्ड + अन्यतमेन → मण्डान्यतमेन (अ + अ → आ); "
           "छपा ‘वाऽम्लेन’ = वा + अम्लेन (आ + अ → आ; ऽ केवल संकेत)।"),
    "87": ("गद्य; विश्वास मध्यम; कोई पाठ-चिह्न नहीं। क्रिया ‘पिलाए’ इकाई 86 से। पहचान: एला, कोल, चव्य सम्भावित; चित्रक मानक; "
           "उपकुञ्चिका विवादित; विड केवल द्रव्य-नाम। सन्धि जाँची: पिप्पली + एला → पिप्पल्येला (ई + ए → ये); चित्रक + "
           "उपकुञ्चिका → चित्रकोपकुञ्चिका (अ + उ → ओ); कल्कम् + वा → कल्कं वा।"),
    "88": ("गद्य; विश्वास मध्यम; कोई पाठ-चिह्न नहीं। ‘मुहूर्तस्थितम्’ द्वितीया, ‘कर्णम्’ से मेल। मुहूर्त की अवधि पाठ में नहीं "
           "(सामान्य गणना ~48 मिनट)। ‘बिल्वज’ अस्पष्ट। सन्धि जाँची: जीवतः + दक्षिणम् → जीवतो दक्षिणम् (अः → ओ घोष से पहले); "
           "कर्णम् + उद्धृत्य → कर्णमुद्धृत्य; आदीनाम् + आप्लवनानाम् + अन्यतमे → आदीनामाप्लवनानामन्यतमे; तत् + आप्लवनम् → "
           "तदाप्लवनम् (त् → द्)।"),
    "89": ("गद्य; विश्वास मध्यम; कोई पाठ-चिह्न नहीं। क्रिया ‘पिलाए’ इकाई 86 से। एला = इलायची (सम्भावित)। सन्धि जाँची: "
           "कुष्ठ + एला → कुष्ठैला (अ + ए → ऐ); कल्कम् + वा → कल्कं वा।"),
    "90": ("गद्य; विश्वास निम्न। पाठ-चिह्न: छपा ‘अर्कालेर्क’ — अर्क + अला/अले + अर्क, या अर्क + अलर्क (‘अर्कालर्क’); "
           "छपा रूप सुधारा नहीं गया, बीच का शब्द अस्पष्ट; इस पर प्रश्न नहीं। अर्क = आक (सम्भावित); अलर्क विवादित। "
           "कषाय = काढ़ा। क्रिया इकाई 86 से। सन्धि जाँची: सुरा + उन्मिश्रम् → सुरोन्मिश्रम् (आ + उ → ओ)।"),
}

# ===================================================================== AIDS
AIDS = {
    "78": {
        "chunks": "स्फिजौ | वोपसंगृह्य | सुपीडितं पीडयेत्",
        "sandhi": "आ + उ → ओ: वा + उपसंगृह्य → वोपसंगृह्य।",
        "frame": "शर्त (इकाई 76 से, दोहराई नहीं): अपरा न गिरे → विकल्प (वा): स्फिजौ (दोनों नितम्ब) पकड़कर → सुपीडितं पीडयेत् (खूब दबाए)।",
    },
    "79": {
        "chunks": "वेण्याऽङ्गुल्या वा | केशवेष्टितया | चकण्ठतालु | परामृशेत्",
        "frame": "किससे (तृतीया): वेण्या, या अङ्गुल्या केशवेष्टितया → किसे (द्वितीया): कण्ठतालु → क्रिया: परामृशेत् (स्पर्श करे)। फल नहीं कहा।",
        "pegs": "मेरा बनाया चित्र (केवल याद के लिए): चोटी का सिरा और बाल-लिपटी उँगली, दोनों गले की ओर।",
    },
    "80": {
        "chunks": "भूर्जपत्रकाचमणिसर्पनिर्मोकैश्च | योनिं धूपयेत् | भूर्जगुग्गुलुभ्यां वा",
        "diagram": {"groups": [
            {"label": "पहला समूह (क्रम से)", "items": ["भूर्जपत्र (भोजपत्र)", "काचमणि (अर्थ संदिग्ध)", "सर्पनिर्मोक (साँप की केंचुली)"]},
            {"label": "या (वा): दूसरा समूह", "items": ["भूर्ज", "गुग्गुलु (मानक)"]}]},
        "sandhi": "विसर्ग + च → श्च: सर्पनिर्मोकैः + च → सर्पनिर्मोकैश्च।",
    },
    "81": {
        "chunks": "शालिमूलसिद्धेन वा सर्पिषा | योनिम्भ्यज्य | कदुकालाम्बुजालिनीनिम्बसर्पनिर्मोकैः | धूपयेत्",
        "chain": {"steps": ["शालि-मूल के साथ पकाया घी", "उससे योनि का अभ्यंग", "फिर धूपन: कटुकालाबु (सम्भावित), जालिनी (विवादित), निम्ब (मानक), साँप की केंचुली"]},
        "sandhi": "ऐ के बाद विसर्ग → र् घोष से पहले: सर्पनिर्मोकैः + धूपयेत् → सर्पनिर्मोकैर्धूपयेत्।",
    },
    "82": {
        "chunks": "अनभ्यक्तां वा | कटुतैलमिश्रैः | कल्कीकृतैर्वा | तैलाक्तैरालिम्पेत्",
        "frame": "किस पर: अनभ्यक्ताम् (संज्ञा नहीं छपी) → किससे (तृतीया, संज्ञा नहीं छपी): कटुतैल-मिश्र / कल्कीकृत / तैलाक्त → क्रिया: आलिम्पेत्।",
        "sandhi": "अ + अ → आ: तैल + अक्तैः → तैलाक्तैः · ऐ के बाद विसर्ग → र्: तैलाक्तैः + आलिम्पेत् → तैलाक्तैरालिम्पेत्।",
    },
    "83": {
        "chunks": "गुडनागरकल्केन | वा",
        "frame": "साधन: गुड + नागर (द्वन्द्व) का कल्क (तत्पुरुष), तृतीया → क्रिया इकाई 82 से: आलिम्पेत्।",
        "anchors": "याद-सूत्र: ‘गुड़-सोंठ’ — 83 में लेप, 84 में वही खाना। (मेरी याद-पद्धति)",
    },
    "84": {
        "chunks": "तदेव | वा | भक्षयेत्",
        "sandhi": "स्वर से पहले त् → द्: तत् + एव → तदेव।",
        "frame": "कर्म: तत् (संज्ञा नहीं छपी; सम्भवतः इकाई 83 का कल्क) + एव (वही) → क्रिया: भक्षयेत्। कर्ता नहीं कहा।",
    },
    "85": {
        "chunks": "लाङ्गलीमुलकल्केन वा | पाणिमुदरं चालिम्पेत् | महावृक्षक्षीरं वा | मूर्ध्न्यनुषेचयेत्",
        "diagram": {"groups": [
            {"label": "पहला विकल्प", "items": ["लाङ्गली (कलिहारी) की जड़ का कल्क", "हाथ और पेट पर लेप"]},
            {"label": "दूसरा विकल्प", "items": ["महावृक्ष (विवादित) का क्षीर", "सिर पर डालना"]}]},
        "sandhi": "इ + अ → य: मूर्ध्नि + अनुषेचयेत् → मूर्ध्न्यनुषेचयेत् · अ + आ → आ: च + आलिम्पेत् → चालिम्पेत्।",
    },
    "86": {
        "chunks": "कुष्ठताली सकल्कं | बिल्व…सुरामन्दान्यतमेन | व्योषतीक्ष्णोष्णेन वाऽम्लेन | कुलत्थरसेन | मधुकपिप्पलीसंपाकेन वा | पाययेत्",
        "diagram": {"groups": [
            {"label": "पिलाने के साथ (क्रम से)", "items": ["1 बिल्व आदि में से कोई एक", "2 व्योष से तीखा-गरम अम्ल",
                                                     "3 कुलत्थ (कुलथी) का रस", "4 मधुक-पिप्पली का संपाक"]}]},
        "sandhi": "अ + उ → ओ: तीक्ष्ण + उष्णेन → तीक्ष्णोष्णेन · अ + अ → आ: मण्ड + अन्यतमेन → मण्डान्यतमेन।",
    },
    "87": {
        "chunks": "पिप्पल्येला | कोलविडचव्य | चित्रकोपकुञ्चिका | कल्कं वा",
        "diagram": {"groups": [
            {"label": "कल्क के द्रव्य (क्रम से)", "items": ["पिप्पली (पीपर)", "एला (इलायची, सम्भावित)", "कोल (बेर, सम्भावित)",
                                                       "विड (द्रव्य-नाम)", "चव्य (चव, सम्भावित)", "चित्रक (चीता, मानक)",
                                                       "उपकुञ्चिका (कलौंजी, विवादित)"]}]},
        "letters": "सात द्रव्यों के पहले अक्षर क्रम से: पि-ए-को-वि-च-चि-उ। (मेरी याद-पद्धति)",
        "sandhi": "ई + ए → ये: पिप्पली + एला → पिप्पल्येला · अ + उ → ओ: चित्रक + उपकुञ्चिका → चित्रकोपकुञ्चिका।",
    },
    "88": {
        "chunks": "खरस्य वृषभस्य वा जीवतो | दक्षिणं कर्णमुद्धृत्य | बिल्वबिल्वजयूषादीनामाप्लवनानामन्यतमे प्रक्षिप्य | मुहूर्तस्थितमुद्धृत्य | तदाप्लवनं पाययेत्",
        "chain": {"steps": ["जीवित गधे या बैल का दाहिना कान निकाले", "बिल्व आदि आप्लवनों में से किसी एक में डाले",
                            "मुहूर्त भर रहने पर निकाले", "वह आप्लवन पिलाए"]},
        "sandhi": "अः → ओ घोष से पहले: जीवतः + दक्षिणम् → जीवतो दक्षिणम् · त् → द् स्वर से पहले: तत् + आप्लवनम् → तदाप्लवनम्।",
    },
    "89": {
        "chunks": "कुष्ठैलाकल्कं | वा | सुरया",
        "sandhi": "अ + ए → ऐ: कुष्ठ + एला → कुष्ठैला।",
        "frame": "कल्क: कुष्ठ + एला → किसके साथ: सुरया (तृतीया) → क्रिया इकाई 86 से: पाययेत्।",
    },
    "90": {
        "chunks": "अर्कालेर्ककषायं (?) | वा | सुरोन्मिश्रं",
        "sandhi": "आ + उ → ओ: सुरा + उन्मिश्रम् → सुरोन्मिश्रम्।",
        "contrast": "कषाय = काढ़ा (इकाई 90) ↔ कल्क = पिसा लेप (इकाई 87, 89): दोनों शब्द याद रखें। (द्रव्य-नाम संदिग्ध)",
    },
}

# ===================================================================== IMAGE_SPECS
IMAGE_SPECS = {
    ("80", "diagram"): {
        "file": "sh3-yoni-dhupana-80.svg",
        "alt": ("Two columns of unit 80, fumigating the yoni: first set, in order, birch bark (bhūrjapatra), kāca-maṇi "
                "(sense doubtful) and snake slough; or the second set, bhūrja and guggulu (standard)."),
        "type": "split",
        "title": "इकाई ८०: योनि-धूपन के दो विकल्प",
        "cols": [["पहला समूह (क्रम से)", ["१ भूर्जपत्र (भोजपत्र)", "२ काचमणि (अर्थ संदिग्ध)", "३ साँप की केंचुली"]],
                 ["या (वा): दूसरा समूह", ["भूर्ज", "गुग्गुलु (मानक)"]]],
    },
    ("81", "chain"): {
        "file": "sh3-shalimula-ghrita-81.svg",
        "alt": ("Flowchart of unit 81: ghee cooked with śāli root; with it the yoni is anointed; then fumigation with "
                "kaṭukālābu (probable), jālinī (disputed), nimba (neem, standard) and snake slough."),
        "type": "mermaid",
        "code": ("flowchart TD\n"
                 "  A[\"शालि-मूल से सिद्ध घी\"] --> B[\"योनि का अभ्यंग\"]\n"
                 "  B --> C[\"फिर धूपन\"]\n"
                 "  C --> D[\"कटुकालाबु (सम्भावित)\"]\n"
                 "  C --> E[\"जालिनी (विवादित)\"]\n"
                 "  C --> F[\"निम्ब, नीम (मानक)\"]\n"
                 "  C --> G[\"साँप की केंचुली\"]\n"),
    },
    ("85", "diagram"): {
        "file": "sh3-langali-mahavriksha-85.svg",
        "alt": ("Table of unit 85: a paste of lāṅgalī (glory lily) root is smeared on the hand and belly; or the milk of "
                "mahāvṛkṣa (identity disputed) is poured over the head."),
        "type": "table",
        "title": "इकाई ८५: दो विकल्प",
        "heads": ["द्रव्य", "कहाँ, कैसे"],
        "rows": [["लाङ्गली (कलिहारी) की जड़ का कल्क", "हाथ और पेट पर लेप"],
                 ["महावृक्ष (विवादित) का क्षीर", "सिर पर डालना"]],
    },
    ("86", "diagram"): {
        "file": "sh3-pana-vikalpa-86.svg",
        "alt": ("Numbered flowchart of unit 86: to be given to drink with one of four vehicles, in order: 1 any one of "
                "bilva and the rest, 2 a sour one sharp and hot with vyoṣa, 3 horse-gram juice, 4 madhuka and pippalī "
                "cooked together."),
        "type": "mermaid",
        "code": ("flowchart TD\n"
                 "  A[\"पाययेत्: इनमें से किसी के साथ\"] --> B[\"१ बिल्व आदि में से कोई एक\"]\n"
                 "  A --> C[\"२ व्योष से तीखा-गरम अम्ल\"]\n"
                 "  A --> D[\"३ कुलथी का रस\"]\n"
                 "  A --> E[\"४ मधुक-पिप्पली का संपाक\"]\n"),
    },
    ("87", "diagram"): {
        "file": "sh3-saptadravya-kalka-87.svg",
        "alt": ("Numbered table of unit 87, the seven drugs of the paste in order with the data's labels: pippalī (long "
                "pepper), elā (cardamom, probable), kola (jujube, probable), viḍa (drug name only), cavya (probable), "
                "citraka (leadwort, standard), upakuñcikā (nigella, disputed)."),
        "type": "table",
        "title": "इकाई ८७: कल्क के सात द्रव्य",
        "heads": ["द्रव्य (क्रम से)", "पहचान"],
        "rows": [["१ पिप्पली", "पीपर"], ["२ एला", "इलायची (सम्भावित)"], ["३ कोल", "बेर का फल (सम्भावित)"],
                 ["४ विड", "द्रव्य-नाम (पहचान नहीं)"], ["५ चव्य", "चव (सम्भावित)"], ["६ चित्रक", "चीता (मानक)"],
                 ["७ उपकुञ्चिका", "कलौंजी (विवादित)"]],
    },
    ("88", "chain"): {
        "file": "sh3-karna-aplavana-88.svg",
        "alt": ("Numbered flowchart of unit 88: 1 a living donkey or bull, 2 take out the right ear, 3 put it into one of "
                "the dips, 4 take it out after a muhūrta, 5 give that dip to drink."),
        "type": "mermaid",
        "code": ("flowchart TD\n"
                 "  A[\"१ जीवित गधा या बैल\"] --> B[\"२ दाहिना कान निकाले\"]\n"
                 "  B --> C[\"३ किसी एक आप्लवन में डाले\"]\n"
                 "  C --> D[\"४ मुहूर्त भर बाद निकाले\"]\n"
                 "  D --> E[\"५ वह आप्लवन पिलाए\"]\n"),
    },
}
