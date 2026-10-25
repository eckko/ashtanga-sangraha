from helpers import mcq, match, order, fill, multi, accepts


AUTHORED = {}

# ---------------------------------------------------------------- unit 52
AUTHORED["52"] = {
    "title": "तत्तू न सम्यक्",
    "question": "What does unit 52 say about the view that a grain-filled mortar should be struck with a pestle?",
    "rule": ("तत् तु न सम्यक्: that, however, is not right. तत् points back to the view of others reported in unit 51 "
             "(striking a grain-filled mortar with a pestle); the copula is understood."),
    "limits": ("Prose, three words; the verb is understood. The printed long ū in तत्तू is read as तत् तु (a possible "
               "print slip; the data's split follows it); no question asks about the printed vowel. The reason is not in this unit; unit 53 gives a reason with हि (for)."),
    "explain_hi": ("यह छोटी गद्य-पंक्ति इकाई 51 के दूसरों के मत (अनाज से भरी ओखली पर मूसल से प्रहार) को अस्वीकार करती है: "
                   "वह तो ठीक नहीं है। ‘तत्’ उसी मत की ओर संकेत करता है, और ‘तु’ (तो, परन्तु) विरोध दिखाता है। "
                   "क्रिया ‘है’ लिखी नहीं गई, समझी जाती है। "
                   "छपा ‘तत्तू’ सम्भवतः ‘तत्तु’ (तत् + तु) है; दीर्घ ऊ की आवश्यकता नहीं।"),
    "hook": "मूसल-मत? तत् तु न सम्यक्: ठीक नहीं।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 52, what is said of the view that a grain-filled mortar should be struck with a pestle?",
            ("It is not right", "तत् तु न सम्यक्: that, however, is not right."),
            [("It is the best method", "The line rejects the view; it does not praise it."),
             ("It is right only in the ninth month", "No month is named in unit 52."),
             ("It is to be done by the husband", "No person is named in unit 52.")],
            "Unit 52 rejects the pestle-and-mortar view of unit 51.",
            "तत् तु न सम्यक् = that, however, is not right."),
        order(1, "Put the printed words of unit 52 in the line's order.",
              ["तत्तू", "न", "सम्यक्"],
              "That however, not, right.",
              "तत्तू → न → सम्यक्."),
        match(2, "Match each word of unit 52 to its meaning.",
              [["तत्", "that (the view of unit 51)"], ["तु", "however"], ["न", "not"], ["सम्यक्", "rightly, properly"]],
              "Four words make the whole verdict.",
              "तत्, तु, न, सम्यक्.", role="extend",
              teaches="तु sets a statement against what went before: others say so, but that is not right."),
        mcq("discriminate", 3, "In unit 52, what does तत् (that) point back to?",
            ("The view of others in unit 51", "The data note: तत् refers to the view reported in unit 51, the pestle and mortar."),
            [("The avoidance of severe exertion", "That is the content of unit 53, which follows."),
             ("The turning of the fetus", "The turning is not what the line rejects."),
             ("The skilled woman's pressing", "The pressing comes later, in unit 55.")],
            "तत् = that view: striking a grain-filled mortar with a pestle.",
            "तत् here = the view of others (unit 51)."),
        fill(4, "That, however, is not right: तत्तू न ____ (type it in Devanagari or in English letters, e.g. dharma).",
             accepts("सम्यक्"),
             "The line is तत्तू न सम्यक्.",
             "सम्यक् = rightly, properly; with न it gives not right.",
             "न सम्यक् = not right.", role="apply"),
        mcq("transfer", 5, "In the invented line रामो गच्छति सीता तु तिष्ठति, what does तु do, as in unit 52?",
            ("Sets Sītā against Rāma: but, however", "तु marks a contrast with what went before, as in तत् तु न सम्यक्."),
            [("Adds Sītā to Rāma: and also", "and also would be च or अपि, not तु."),
             ("Gives a reason: because", "A reason would be marked by हि, as in unit 53."),
             ("Marks a question: is it?", "तु does not make a question.")],
            "Rāma goes; Sītā, however, stays: तु marks the contrast.",
            "तु = however, but (contrast).",
            teaches="तु sets one statement against another: अन्ये ... आहुः, तत् तु न सम्यक् (others say ..., but that is not right)."),
    ],
}

# ---------------------------------------------------------------- unit 53
AUTHORED["53"] = {
    "title": "दारुणव्यायामवर्जनं हि",
    "question": "By unit 53, what is constantly prescribed for a pregnant woman?",
    "rule": ("दारुणव्यायामवर्जनम्: avoidance of severe exertion is constantly (सततम्) prescribed (उपदिश्यते) for a "
             "pregnant woman. हि (for) gives a reason, after unit 52 rejected the pestle view."),
    "limits": ("Prose. The line names no particular exertion; it does not itself mention the pestle. Linking this reason "
               "to the verdict of unit 52 follows the sense of हि (for); the unit does not name unit 52."),
    "explain_hi": ("क्योंकि गर्भिणी के लिए कठोर व्यायाम (परिश्रम) से बचना सदा बताया जाता है। "
                   "‘हि’ (क्योंकि) कारण देता है; प्रसंग से यह पिछली इकाई के ‘ठीक नहीं’ का कारण लगता है। "
                   "समास पीछे से पढ़ें: दारुण (कठोर) व्यायाम (परिश्रम) का वर्जन (त्याग)। "
                   "‘उपदिश्यते’ कर्मवाच्य है: बताया जाता है। ‘गर्भिण्याः’ षष्ठी है, जिसके लिए यह नियम है।"),
    "hook": "गर्भिणी: दारुण व्यायाम वर्जित, सततम्।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 53, what is constantly prescribed for a pregnant woman?",
            ("Avoidance of severe exertion", "दारुणव्यायामवर्जनम्: avoidance of severe exertion."),
            [("Daily severe exertion", "The line prescribes avoiding it, not doing it."),
             ("Striking a mortar with a pestle", "That is the view of others in unit 51, rejected in unit 52."),
             ("Walking about again and again", "Walking is not named in unit 53.")],
            "Severe exertion is to be avoided by a pregnant woman.",
            "दारुण-व्यायाम-वर्जन = avoidance of severe exertion."),
        order(1, "Put the words of unit 53 in the line's order.",
              ["दारुणव्यायामवर्जनं", "हि", "गर्भिण्याः", "सततम्", "उपदिश्यते"],
              "Avoidance of severe exertion, for, of a pregnant woman, constantly, is prescribed.",
              "दारुणव्यायामवर्जनं → हि → गर्भिण्याः → सततम् → उपदिश्यते."),
        match(2, "Match each word of unit 53 to its meaning.",
              [["दारुण", "severe"], ["व्यायाम", "exertion"], ["वर्जन", "avoidance"], ["सततम्", "constantly"],
               ["उपदिश्यते", "is prescribed"]],
              "Read the compound from the end: avoidance of exertion that is severe.",
              "दारुण, व्यायाम, वर्जन, सततम्, उपदिश्यते.", role="extend",
              teaches="A tatpuruṣa is read from its last member: दारुण-व्यायाम-वर्जन = the avoidance of severe exertion."),
        mcq("discriminate", 3, "What kind of form is उपदिश्यते in unit 53?",
            ("Present passive: is prescribed", "The data labels it 3 sg. pres. pass. of upa-√diś."),
            [("Present active: prescribes", "The active would be उपदिशति."),
             ("Optative: should prescribe", "An optative ends in -एत्, as उपदिशेत्."),
             ("Future: will prescribe", "A future would have -स्य-, as उपदेक्ष्यति.")],
            "उपदिश्यते = is prescribed: the data labels it 3 sg. present passive (root दिश् + -य- + middle ending).",
            "-य- + middle ending on the root (दिश्यते) = present passive here; but 4th-class verbs such as जायते, मन्यते also end in -यते."),
        multi("apply", 4, "Which statements fit unit 53?",
              [("It names one particular exercise to avoid", "No particular exercise is named, only severe exertion."),
               ("The prescription is called constant (सततम्)", "Right: सततम् उपदिश्यते, constantly prescribed."),
               ("It is a metrical verse line", "It is a prose unit, not a verse."),
               ("गर्भिण्याः names the person it concerns", "Right: genitive, for a pregnant woman.")],
              [1, 3],
              "Constant prescription, for the pregnant woman, of avoiding severe exertion.",
              "दारुणव्यायामवर्जनं ... गर्भिण्याः सततमुपदिश्यते."),
        mcq("transfer", 5, "Built like उपदिश्यते, what does दीयते mean in the invented line औषधं रोगिणे दीयते?",
            ("is given", "-यते is the present passive: medicine is given to the patient."),
            [("gives", "The active would be ददाति."),
             ("should give", "should give would be an optative, दद्यात्."),
             ("will give", "will give would be a future, दास्यति.")],
            "औषधं रोगिणे दीयते = medicine is given to the patient.",
            "-यते = present passive (is ...-ed).",
            teaches="A present passive ends in -यते: उपदिश्यते (is prescribed), दीयते (is given)."),
    ],
}

# ---------------------------------------------------------------- unit 54
AUTHORED["54"] = {
    "title": "विशेषतश्चप्रसवकाले",
    "question": "By unit 54, what danger does the text name, especially at the time of delivery?",
    "rule": ("Especially at delivery (प्रसवकाले), in her whose dhātus and doṣas are all set in motion, vāyu (वायु, Vāta), "
             "stirred up and finding an opening, might injure (हिंस्यात्) the vital breaths (प्राणान्). इति closes the reason."),
    "limits": ("Low confidence. त्रार्या and मुशल्यायाम are damaged words; what stirs vāyu is unclear, and the pestle "
               "link is only a conjecture: no question on them. अन्तर may mean opening or opportunity. हिंस्यात् states a "
               "possibility, not a certain result."),
    "explain_hi": ("अनुमानित पाठ पर: विशेषकर प्रसव के समय, जिसके सब धातु और दोष चलायमान हो गए हैं, उस स्त्री में, कोमलता के कारण, "
                   "प्रेरित वायु अवसर या छिद्र (अन्तर) पाकर प्राणों को हानि पहुँचा सकती है। "
                   "‘त्रार्या’ और ‘मुशल्यायाम’ टूटे-फूटे शब्द हैं; वायु किससे प्रेरित है, यह स्पष्ट नहीं, इसलिए उन पर प्रश्न नहीं। "
                   "‘हिंस्यात्’ विधिलिङ् है: हानि सम्भव है, निश्चित नहीं। अन्त का ‘इति’ इकाई 53 के निषेध का कारण पूरा करता है।"),
    "hook": "प्रसवकाल: सब धातु-दोष चलायमान, वायु अवसर पाकर प्राणों को चोट कर सकती।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 54, what might the stirred-up vāyu (Vāta) injure?",
            ("The vital breaths", "प्राणान् हिंस्यात्: it might injure the vital breaths."),
            [("The bones of the fetus", "No bones are named in unit 54."),
             ("The mother's eyes", "No eyes are named in unit 54."),
             ("The attendant's hands", "No attendant is named in unit 54.")],
            "The danger named is harm to the vital breaths (prāṇa).",
            "वायुः ... प्राणान् हिंस्यात्."),
        order(1, "Put these sure parts of unit 54 in the line's order.",
              ["विशेषतश्च", "प्रसवकाले", "प्रचलितसर्वधातुदोषायाः", "सौकुमार्यात्", "लब्ध्वा", "प्राणान् हिंस्यादिति"],
              "Especially, at the time of delivery, of her whose dhātus and doṣas are all set in motion, because of "
              "delicacy, having found, might injure the vital breaths.",
              "विशेषतश्च → प्रसवकाले → प्रचलितसर्वधातुदोषायाः → सौकुमार्यात् → लब्ध्वा → प्राणान् हिंस्यादिति."),
        match(2, "Match each word of unit 54 to its meaning.",
              [["विशेषतः", "especially"], ["प्रसवकाले", "at the time of delivery"], ["सौकुमार्यात्", "because of delicacy"],
               ["प्राणान्", "the vital breaths"], ["हिंस्यात्", "might injure"]],
              "When, why, and what might happen to whom.",
              "विशेषतः, प्रसवकाले, सौकुमार्यात्, प्राणान्, हिंस्यात्.", role="extend",
              teaches="An ablative in -आत् can give a cause: सौकुमार्यात् = because of delicacy."),
        mcq("discriminate", 3, "What does the optative हिंस्यात् say in unit 54?",
            ("Harm that might happen", "The data note: हिंस्यात् states what might happen, not a certain result."),
            [("Harm that has already happened", "A past event would need a past form; this is an optative."),
             ("Harm that will certainly happen", "The optative here gives a possibility, not a certainty."),
             ("A command to cause harm", "The line warns of harm; it orders none.")],
            "हिंस्यात् = might injure: a possibility, the reason for the caution.",
            "Optative here = might (possibility)."),
        mcq("apply", 4, "In unit 54, whose dhātus and doṣas are all set in motion?",
            ("The woman's, at delivery", "प्रचलितसर्वधातुदोषायाः is feminine genitive: of her (the woman in labour)."),
            [("The fetus's", "The compound is feminine; गर्भ (fetus) is masculine."),
             ("Vāyu's", "वायुः is the subject that is stirred up, not the one described."),
             ("The pestle-striker's", "No striker is named in this compound.")],
            "The bahuvrīhi is feminine genitive: of her whose dhātus and doṣas are all in motion.",
            "प्रचलित-सर्व-धातु-दोषा = she in whom all dhātus and doṣas are set in motion."),
        mcq("transfer", 5, "By the rule of हिंस्यादिति, how is भवेत् + इति (thus it might be) joined?",
            ("भवेदिति", "A final त् becomes द् before a vowel, as हिंस्यात् + इति → हिंस्यादिति."),
            [("भवेतिति", "त् does not stay unvoiced before a vowel in sandhi."),
             ("भवेन्निति", "त् may become न् (optionally) only before a nasal, not before इ."),
             ("भवेच्चिति", "त् becomes च् only before च or छ.")],
            "भवेत् + इति = भवेदिति, like हिंस्यात् + इति = हिंस्यादिति.",
            "Final त् + vowel → द् + vowel.",
            teaches="A final त् becomes द् before a vowel: हिंस्यात् + इति → हिंस्यादिति."),
    ],
}

# ---------------------------------------------------------------- unit 55
AUTHORED["55"] = {
    "title": "अथ परिवृत्तगर्भां",
    "question": "By unit 55, what does the skilled woman do once the fetus has turned?",
    "rule": ("Once the fetus has turned, a skilled woman places her on a paryaṅka, and from her foot-side, as she sits, "
             "anoints the yoni in the natural direction (anuloma), comfortably; then presses the two buttocks with the feet."),
    "limits": ("Prose, medium confidence. Whose feet press is not stated (the natural reading: the attendant's). "
               "पर्यङ्क may be a couch or a seated posture. The substance used to anoint is not named. No duration or force is given."),
    "explain_hi": ("गर्भ के पलट जाने पर (परिवृत्तगर्भा, बहुव्रीहि) कुशल स्त्री उसे पर्यंक (पलंग; या बैठने का आसन) पर बिठाती है। "
                   "बैठी हुई उस स्त्री के पैरों की ओर से वह योनि यानी जननमार्ग का अनुलोम दिशा में, सुखपूर्वक अभ्यंग करती है, "
                   "फिर दोनों नितम्बों (स्फिजौ) को पैरों से दबाती है। "
                   "किसके पैर, यह नहीं कहा; स्वाभाविक अर्थ परिचारिका के पैर हैं। किस द्रव्य से अभ्यंग, यह भी नहीं कहा।"),
    "hook": "पलटा गर्भ → पर्यंक → पैरों की ओर से अनुलोम अभ्यंग → नितम्ब दबाना।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 55, with what does the skilled woman press the two buttocks?",
            ("With the two feet", "स्फिजौ पादाभ्यां पीडयेत्: she should press the buttocks with the feet."),
            [("With both hands", "Hands are not named; the line says पादाभ्याम्, with the feet."),
             ("With a pestle", "The pestle belongs to the rejected view of unit 51."),
             ("With a cloth soaked in oil", "No cloth or oil is named in unit 55.")],
            "The two buttocks are pressed with the two feet.",
            "स्फिजौ पादाभ्यां पीडयेत्."),
        order(1, "Put the steps of unit 55 in the line's order.",
              ["परिवृत्तगर्भां", "पर्यंकमेनामारोप्य", "पादतोऽस्या निषण्णाया", "योनिमनुलोममनुसुखमभ्यज्य",
               "स्फिजौ पादाभ्यां पीडयेत्"],
              "Her whose fetus has turned, placing her on the paryaṅka, from the foot-side of her seated, anointing the "
              "yoni in the natural direction, comfortably, she should press the buttocks with the feet.",
              "परिवृत्तगर्भां → पर्यंकमेनामारोप्य → पादतोऽस्या निषण्णाया → योनिमनुलोममनुसुखमभ्यज्य → स्फिजौ पादाभ्यां पीडयेत्."),
        match(2, "Match each word of unit 55 to its meaning.",
              [["परिवृत्तगर्भा", "she whose fetus has turned"], ["कुशला स्त्री", "a skilled woman"],
               ["अभ्यज्य", "having anointed"], ["स्फिजौ", "the two buttocks"], ["पीडयेत्", "should press"]],
              "Who acts, on whom, and what she does.",
              "परिवृत्तगर्भा, कुशला स्त्री, अभ्यज्य, स्फिजौ, पीडयेत्.", role="extend",
              teaches="परिवृत्तगर्भा is a bahuvrīhi: she whose (गर्भ) fetus has (परिवृत्त) turned."),
        mcq("discriminate", 3, "Which split of पादतोऽस्या is right?",
            ("पादतः + अस्याः", "अः + अ → ओ with the next अ dropped (ऽ); अस्याः loses its visarga before न of निषण्णाया."),
            [("पादते + अस्याः", "ए + अ would keep ए: it would read पादतेऽस्याः."),
             ("पादता + अस्याः", "आ + अ would merge into आ: पादतास्याः, with no ओ."),
             ("पादतो + स्याः", "स्याः is not the word; ऽ marks the dropped अ of अस्याः.")],
            "पादतः (from the foot-side) + अस्याः (of her).",
            "अः + अ → ओऽ."),
        multi("apply", 4, "Which statements does unit 55 support?",
              [("The substance used for anointing is named (स्नेहद्रव्य)", "No substance is named in unit 55."),
               ("The woman is seated (निषण्णा)", "Right: निषण्णायाः, as she sits."),
               ("The anointing goes in the natural direction (अनुलोम)", "Right: योनिम् अनुलोमम् अभ्यज्य."),
               ("The line says how long to press (काल)", "No duration is given.")],
              [1, 2],
              "Seated, anointed in the natural direction; no substance and no duration are named.",
              "पादतोऽस्या निषण्णाया योनिमनुलोममनुसुखमभ्यज्य."),
        mcq("transfer", 5, "By the rule of आरोप्य and अभ्यज्य, what is the absolutive (having entered) of प्र + √विश्?",
            ("प्रविश्य", "With a prefix the absolutive takes -य, as आ-रोप्य, अभि-अज्य."),
            [("प्रविष्ट्वा", "-त्वा is used without a prefix; with प्र the ending is -य."),
             ("प्रविष्टः", "प्रविष्टः is a past participle, entered, not an absolutive."),
             ("प्रविशति", "प्रविशति is the present, enters.")],
            "प्र + √विश् → प्रविश्य, having entered, like आरोप्य and अभ्यज्य.",
            "Prefix + root → absolutive in -य.",
            teaches="With a prefix the absolutive ends in -य (आरोप्य, अभ्यज्य); without a prefix in -त्वा (लब्ध्वा)."),
    ],
}

# ---------------------------------------------------------------- unit 56
AUTHORED["56"] = {
    "title": "योनिं च पुनःपुनः",
    "question": "By unit 56, what should be done to the yoni again and again?",
    "rule": ("योनिं च पुनःपुनः प्रसारयेत्: and she should stretch out the yoni again and again. The subject is the skilled "
             "woman of unit 55, not named here."),
    "limits": ("Prose, four words. The line does not say how the yoni is stretched, with what, or how often beyond again "
               "and again. The subject is understood from unit 55."),
    "explain_hi": ("और वह (इकाई 55 की कुशल स्त्री) योनि यानी जननमार्ग को बार-बार फैलाए। "
                   "कर्ता यहाँ नहीं लिखा, पिछली इकाई से समझा जाता है। "
                   "‘प्रसारयेत्’ प्र-√सृ का णिजन्त विधिलिङ् है: फैलाए। "
                   "कैसे और किससे फैलाना, यह पंक्ति नहीं बताती।"),
    "hook": "पुनःपुनः प्रसारयेत्: बार-बार फैलाए।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 56, what should be done to the yoni again and again?",
            ("It should be stretched out", "योनिं च पुनःपुनः प्रसारयेत्."),
            [("It should be washed with cold water", "No washing or water is named in unit 56."),
             ("It should be bound with cloth", "No cloth is named in unit 56."),
             ("It should be left untouched", "The line asks for stretching, again and again.")],
            "The yoni is to be stretched out again and again.",
            "प्रसारयेत् = should stretch out."),
        match(1, "Match each word of unit 56 to its meaning.",
              [["योनिम्", "the yoni (birth passage)"], ["च", "and"], ["पुनःपुनः", "again and again"],
               ["प्रसारयेत्", "should stretch out"]],
              "Four words: what, how often, what to do.",
              "योनिम्, च, पुनःपुनः, प्रसारयेत्."),
        fill(2, "And she should stretch out the yoni again and again: योनिं च पुनःपुनः ____ (type it in Devanagari or in English letters, e.g. dharma).",
             accepts("प्रसारयेत्", None, "prasarayet"),
             "The line is योनिं च पुनःपुनः प्रसारयेत्.",
             "प्रसारयेत् = should stretch out: causative of प्र-√सृ with the optative ending -एत्.",
             "प्रसारयेत् = should stretch out."),
        mcq("discriminate", 3, "Who is the subject of प्रसारयेत् in unit 56?",
            ("Unstated; the skilled woman of unit 55", "The data note: the subject (the skilled woman) is not stated here."),
            [("The pregnant woman, named in the line", "No woman is named in unit 56; only the yoni is."),
             ("Another woman, named अन्या", "अन्या appears in unit 58, not here."),
             ("A physician, named वैद्य", "No physician is named in unit 56.")],
            "The verb has no stated subject; it carries on from the skilled woman of unit 55.",
            "Subject of प्रसारयेत् = understood from unit 55."),
        multi("apply", 4, "Which statements fit unit 56?",
              [("पुनःपुनः asks for repetition", "Right: again and again."),
               ("The line says how the stretching is done", "The data note: it does not say how."),
               ("प्रसारयेत् is an optative: should stretch out", "Right: the -एत् ending."),
               ("The line names an oil for it", "No oil is named in unit 56.")],
              [0, 2],
              "Repeated stretching is asked; the manner is not given.",
              "पुनःपुनः प्रसारयेत् = should stretch out again and again."),
        mcq("transfer", 5, "Built like प्रसारयेत्, which form of धारय- (cause to hold) means should hold?",
            ("धारयेत्", "-एत् on the causative stem gives the optative, as प्रसारय- → प्रसारयेत्."),
            [("धारयति", "धारयति is the present, holds."),
             ("धारयित्वा", "धारयित्वा is an absolutive, having held."),
             ("धारयन्", "धारयन् is a present participle, holding.")],
            "धारय- + -एत् = धारयेत्, should hold, like प्रसारयेत्.",
            "Causative stem in -अय + -एत् = should (optative).",
            teaches="The optative third singular of अ-stem and causative verbs ends in -एत् (should ...): प्रसारयेत्, पीडयेत्, धारयेत्; other verbs take -यात् (ब्रूयात्, हिंस्यात्)."),
    ],
}

# ---------------------------------------------------------------- unit 57
AUTHORED["57"] = {
    "title": "ब्रूयाच्च सुभगे",
    "question": "By unit 57, what should the attendant say to the woman in labour?",
    "rule": ("ब्रूयात्: she (the attendant) should say: सुभगे (O fortunate one), शनैः शनैः प्रवाहयस्व, bear down "
             "(pravāhaṇa, pushing) gently, gently; then words of comfort about her face and a son. इति ends the speech."),
    "limits": ("Medium confidence. The words about the face-colour (सुप्रसन्नेते, read सुप्रसन्नस्ते) and the person of "
               "जनयिष्यति (read जनयिष्यसि, you will bear) are corrected readings: no question rests on them."),
    "explain_hi": ("परिचारिका प्रसव करती स्त्री से कहे: हे सौभाग्यवती (सुभगे), धीरे-धीरे प्रवाहण करो, यानी जोर लगाओ। "
                   "फिर ढाढ़स के शब्द: तुम्हारे मुख का वर्ण बहुत निर्मल है, तुम पुत्र को जन्म दोगी। "
                   "यह अन्तिम भाग दो छोटे सुधारों पर टिका है (सुप्रसन्नेते → सुप्रसन्नस्ते, जनयिष्यति → जनयिष्यसि), "
                   "इसलिए उस पर प्रश्न नहीं। ‘ब्रूयात्’ विधिलिङ् (कहे), ‘प्रवाहयस्व’ आज्ञार्थ मध्यम पुरुष (जोर लगाओ)।"),
    "hook": "सुभगे, शनैः शनैः प्रवाहयस्व: धीरे-धीरे जोर लगाओ।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 57, how is the woman in labour told to bear down?",
            ("Gently, gently", "शनैः शनैः प्रवाहयस्व: bear down gently, gently."),
            [("With all her force at once", "The line says शनैः शनैः, gently."),
             ("While holding her breath", "No breath-holding is named in unit 57."),
             ("Only when the physician arrives", "No physician is named in unit 57.")],
            "She is told to bear down gently, step by step.",
            "शनैः शनैः प्रवाहयस्व = bear down gently, gently."),
        order(1, "Put these printed words of unit 57 in the line's order.",
              ["ब्रूयाच्च", "सुभगे", "शनैः शनैः", "प्रवाहयस्व", "मुखवर्णः", "पुत्रं"],
              "And she should say: O fortunate one, gently gently bear down; ... face-colour ... a son.",
              "ब्रूयाच्च → सुभगे → शनैः शनैः → प्रवाहयस्व → मुखवर्णः → पुत्रं."),
        match(2, "Match each word of unit 57 to its meaning.",
              [["ब्रूयात्", "she should say"], ["सुभगे", "O fortunate one"], ["शनैः", "gently, slowly"],
               ["प्रवाहयस्व", "bear down"]],
              "Who speaks, to whom, and what she is told.",
              "ब्रूयात्, सुभगे, शनैः, प्रवाहयस्व.", role="extend",
              teaches="सुभगे is a vocative (f. sg.): a word of address, O fortunate one."),
        mcq("discriminate", 3, "Which word of unit 57 is a command addressed to the woman herself?",
            ("प्रवाहयस्व", "2 sg. imperative: bear down (you)."),
            [("ब्रूयात्", "3 sg. optative: she (the attendant) should say; an instruction about the attendant."),
             ("सुभगे", "A vocative, O fortunate one: an address, not a command."),
             ("मुखवर्णः", "A noun, colour of the face; no command.")],
            "प्रवाहयस्व is the second-person imperative: the woman is told to bear down.",
            "प्रवाहयस्व = bear down (2 sg. imperative)."),
        mcq("apply", 4, "In unit 57, who speaks these words to the woman in labour?",
            ("The attendant", "Probable, by the data note: ब्रूयात् names no speaker; the data note: the speaker (the attendant) addresses the woman in labour."),
            [("The woman in labour herself", "She is the one addressed (सुभगे), not the speaker."),
             ("Her husband", "No husband is named in unit 57."),
             ("A priest reciting a mantra", "The mantra comes in unit 58, from another woman.")],
            "ब्रूयात् (she should say): the attendant speaks, the woman in labour is addressed.",
            "ब्रूयात् = the attendant should say."),
        mcq("transfer", 5, "By the join ब्रूयात् + च → ब्रूयाच्च, how do स्यात् + च (and it may be) join?",
            ("स्याच्च", "त् before च becomes च्."),
            [("स्याद्च", "त् does not become द् before the voiceless च."),
             ("स्याञ्च", "त् becomes च्, not ञ्."),
             ("स्याश्च", "त् does not become श्.")],
            "स्यात् + च = स्याच्च, like ब्रूयात् + च = ब्रूयाच्च.",
            "त् + च → च्च.",
            teaches="A final त् becomes च् before च: ब्रूयात् + च → ब्रूयाच्च; स्यात् + च → स्याच्च."),
    ],
}

# ---------------------------------------------------------------- unit 58
AUTHORED["58"] = {
    "title": "अन्या तु वामकर्णेऽस्या",
    "question": "By unit 58, who mutters which mantra, and into which ear?",
    "rule": ("Another woman (अन्या) mutters this mantra into her left ear (वामकर्णे): earth (क्षिति), water (जल), sky "
             "(वियत्), fire (तेजस्), wind (वायु), Viṣṇu, Prajāpati. The mantra carries on in unit 59."),
    "limits": ("Two printed lines, prose as a unit. The list of names has no verb here; the data takes the singular verbs "
               "of unit 59 as probably theirs. The card reports the mantra as printed; it adds no claim about its effect."),
    "explain_hi": ("दूसरी स्त्री (अन्या, स्त्रीलिंग) उस प्रसव करती स्त्री के बाएँ कान में यह मन्त्र जपे। "
                   "मन्त्र की पहली पंक्ति सात नाम गिनाती है: क्षिति (पृथ्वी), जल, वियत् (आकाश), तेज (अग्नि), वायु, विष्णु, प्रजापति। "
                   "इस पंक्ति में क्रिया नहीं; डेटा के अनुसार यह इकाई 59 में आगे चलती है। "
                   "सन्धि: क्षितिः + जलम् → क्षितिर्जलम्, तेजः + वायुः → तेजो वायुः, वायुः + विष्णुः → वायुर्विष्णुः।"),
    "hook": "बाएँ कान में: क्षिति, जल, वियत्, तेज, वायु, विष्णु, प्रजापति।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 58, into which ear is the mantra muttered?",
            ("Her left ear", "वामकर्णेऽस्याः: in her left ear."),
            [("Her right ear", "The line says वाम, left."),
             ("Both her ears in turn", "Only one ear is named: the left."),
             ("The attendant's own ear", "अस्याः = her, the woman in labour.")],
            "The mantra is muttered into the left ear of the woman in labour.",
            "वामकर्णे = in the left ear."),
        order(1, "Put the first six names of the mantra in unit 58 in order.",
              ["क्षितिः", "जलम्", "वियत्", "तेजः", "वायुः", "विष्णुः"],
              "Earth, water, sky, fire, wind, Viṣṇu (then Prajāpati).",
              "क्षितिः → जलम् → वियत् → तेजः → वायुः → विष्णुः."),
        match(2, "Match each name in the mantra of unit 58 to its meaning.",
              [["क्षितिः", "earth"], ["जलम्", "water"], ["वियत्", "sky, space"], ["तेजः", "fire"], ["वायुः", "wind"]],
              "The first five names of the mantra.",
              "क्षिति, जल, वियत्, तेजस्, वायु.", role="extend",
              teaches="वियत् = sky, space; तेजस् = fire: two less common names in the list."),
        mcq("discriminate", 3, "Why is तेजः printed तेजो before वायुः in unit 58?",
            ("अः before a voiced consonant becomes ओ", "तेजः + वायुः → तेजो वायुः: व is voiced."),
            [("तेजो is a vocative form", "It is nominative, a name in the list; not an address."),
             ("ओ marks a dual", "तेजः is singular; ओ comes from the sandhi."),
             ("A visarga after अ becomes र् before व", "That would give तेजर्वायुः; after अ it becomes ओ.")],
            "तेजः + वायुः = तेजो वायुः: visarga after अ before a voiced sound → ओ.",
            "अः + voiced consonant → ओ."),
        mcq("apply", 4, "In unit 58, who mutters the mantra?",
            ("Another woman", "अन्या is feminine: another woman, the noun not stated."),
            [("The woman in labour herself", "The mantra goes into her ear (अस्याः), so she hears it."),
             ("A male priest", "अन्या is feminine; no priest is named."),
             ("Her husband", "No husband is named in unit 58.")],
            "अन्या तु ... जपेत्: another woman should mutter it.",
            "अन्या = another (woman)."),
        mcq("transfer", 5, "By the rule of क्षितिर्जलम्, how is मतिः + दृढा (the mind is firm) joined?",
            ("मतिर्दृढा", "A visarga after इ becomes र् before a voiced sound, as क्षितिः + जलम्."),
            [("मती दृढा", "The vowel is lengthened with the visarga dropped only before र."),
             ("मतिस्दृढा", "स् comes only before त or थ."),
             ("मतिश्दृढा", "श् comes only before च, छ or श.")],
            "मतिः + दृढा = मतिर्दृढा, like क्षितिः + जलम् = क्षितिर्जलम्.",
            "इः + voiced sound → इर्.",
            teaches="A visarga after इ becomes र् before a voiced sound: क्षितिः + जलम् → क्षितिर्जलम्."),
    ],
}

# ---------------------------------------------------------------- unit 59
AUTHORED["59"] = {
    "title": "सगर्भां त्वां सदापातु",
    "question": "By unit 59, what does the mantra wish for the woman, and what is she told to do?",
    "rule": ("May (it) protect you with the fetus (सगर्भाम्) at all times (सदा पातु), or also grant freedom from the dart "
             "(वैशल्यम्). Give birth (प्रसूष्व), you unharmed (अविक्लिष्टा), O fair-faced one (शुभानने)."),
    "limits": ("The subject of पातु and दधातु is not stated (probably the names of unit 58). The sense of शल्य here is "
               "uncertain; वा ... अपि is loose. अविक्लिष्टम् may agree with the son of unit 60 or be an adverb: no question on it."),
    "explain_hi": ("यह मन्त्र का अनुष्टुभ् श्लोक है। पहली पंक्ति: (वे/वह) गर्भ सहित तुम्हारी सदा रक्षा करे, या शल्य से मुक्ति (वैशल्य) भी दे। "
                   "दूसरी पंक्ति: हे सुन्दर मुख वाली (शुभानने), तुम स्वयं अपीड़ित (अविक्लिष्टा) रहकर जन्म दो (प्रसूष्व)। "
                   "कर्ता लिखा नहीं; डेटा उसे इकाई 58 के नामों से जोड़ता है। ‘शल्य’ का यहाँ ठीक अर्थ अनिश्चित है। "
                   "‘अविक्लिष्टम्’ अगली इकाई के ‘पुत्रम्’ से जुड़ सकता है या क्रियाविशेषण हो सकता है; इस पर प्रश्न नहीं।"),
    "hook": "रक्षा करे, वैशल्य दे; अपीड़ित तुम, जन्म दो, शुभानने।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "In unit 59, what is the woman told to do in the second line?",
            ("Give birth", "प्रसूष्व त्वम्: give birth, you."),
            [("Rest and wait", "No resting is named in unit 59."),
             ("Keep a fast", "No fast is named in unit 59."),
             ("Keep silent", "No silence is named in unit 59.")],
            "The second line tells her: give birth, unharmed.",
            "प्रसूष्व = give birth."),
        order(1, "Put the parts of unit 59 in the verse's order.",
              ["सगर्भां त्वां", "सदापातु", "वैशल्यं वा दधात्वपि", "प्रसूष्व", "त्वमविक्ळिष्टमविक्ळिष्टा", "शुभानने"],
              "You with the fetus, may (it) protect at all times, or also grant freedom from the dart; give birth, "
              "you unharmed ... , O fair-faced one.",
              "सगर्भां त्वां → सदापातु → वैशल्यं वा दधात्वपि → प्रसूष्व → त्वमविक्ळिष्टमविक्ळिष्टा → शुभानने."),
        match(2, "Match each word of unit 59 to its meaning.",
              [["सगर्भाम्", "with the fetus"], ["पातु", "may (it) protect"], ["दधातु", "may (it) grant"],
               ["प्रसूष्व", "give birth"], ["शुभानने", "O fair-faced one"]],
              "The wishes, the command and the address.",
              "सगर्भाम्, पातु, दधातु, प्रसूष्व, शुभानने.", role="extend",
              teaches="-तु is the third-person imperative (may it ...): पातु, दधातु; प्रसूष्व is a second-person command."),
        mcq("discriminate", 3, "Which split of दधात्वपि is right?",
            ("दधातु + अपि", "उ before a different vowel becomes व्: दधातु + अपि → दधात्वपि."),
            [("दधाति + अपि", "इ + अ would give य्: दधात्यपि."),
             ("दधातो + अपि", "ओ + अ would give दधातोऽपि."),
             ("दधात्व + पि", "पि is not a word; the particle is अपि.")],
            "दधातु (may it grant) + अपि (also).",
            "उ + a different vowel → व् + that vowel."),
        mcq("apply", 4, "In unit 59, which word calls the mother herself unharmed?",
            ("अविक्लिष्टा", "Feminine nominative singular, with त्वम् (you): you, unharmed."),
            [("अविक्लिष्टम्", "Not feminine nominative; the data reads it with the son, or as an adverb."),
             ("शुभानने", "A vocative, O fair-faced one: an address, not unharmed."),
             ("वैशल्यम्", "Freedom from the dart: a thing granted, not her state.")],
            "अविक्लिष्टा agrees with त्वम्: the mother herself is to be unharmed.",
            "अविक्लिष्टा = (you) unharmed, f. nom. sg."),
        mcq("transfer", 5, "By the rule of दधात्वपि, how is मधु + अस्ति (there is honey) joined?",
            ("मध्वस्ति", "उ before a different vowel becomes व्, as दधातु + अपि → दधात्वपि."),
            [("मधूस्ति", "उ is lengthened only before another उ."),
             ("मधोस्ति", "उ does not become ओ before अ."),
             ("मधुस्ति", "The अ of अस्ति is not simply dropped.")],
            "मधु + अस्ति = मध्वस्ति, like दधातु + अपि = दधात्वपि.",
            "उ + a different vowel → व्.",
            teaches="उ before a different vowel becomes व्: दधातु + अपि → दधात्वपि."),
    ],
}

# ---------------------------------------------------------------- unit 60
AUTHORED["60"] = {
    "title": "कार्तिकेयद्युतिं पुत्रं",
    "question": "By unit 60, what kind of son does the mantra wish for?",
    "rule": ("A son (पुत्रम्) having the splendour of Kārtikeya (कार्तिकेयद्युतिम्, bahuvrīhi) and protected by Kārtikeya "
             "(कार्तिकेयाभिरक्षितम्, tatpuruṣa). इति closes the mantra."),
    "limits": ("Prose, no verb: the data carries प्रसूष्व (give birth) from unit 59. Kārtikeya is the name of a god, as "
               "printed; the card adds nothing about him."),
    "explain_hi": ("कार्तिकेय की कान्ति वाले, कार्तिकेय से रक्षित पुत्र को (जन्म दो)। "
                   "यहाँ क्रिया नहीं; डेटा इकाई 59 की ‘प्रसूष्व’ को आगे लेता है। "
                   "दो समास: ‘कार्तिकेयद्युति’ बहुव्रीहि है (जिसकी कान्ति कार्तिकेय की है), ‘कार्तिकेयाभिरक्षित’ तत्पुरुष (कार्तिकेय से रक्षित)। "
                   "अन्त का ‘इति’ मन्त्र को समाप्त करता है।"),
    "hook": "कार्तिकेय-सी द्युति, कार्तिकेय की रक्षा: ऐसा पुत्र।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 60, whose splendour is the son wished to have?",
            ("Kārtikeya's", "कार्तिकेयद्युतिं पुत्रम्: a son with the splendour of Kārtikeya."),
            [("Indra's", "Indra is not named in unit 60."),
             ("The sun's", "The sun is not named in unit 60."),
             ("His father's", "No father is named in unit 60.")],
            "Kārtikeya is named twice: for the splendour and for the protection.",
            "कार्तिकेय-द्युति = having Kārtikeya's splendour."),
        order(1, "Put the words of unit 60 in the line's order.",
              ["कार्तिकेयद्युतिं", "पुत्रं", "कार्तिकेयाभिरक्षितम्", "इति"],
              "Having Kārtikeya's splendour, a son, protected by Kārtikeya: thus.",
              "कार्तिकेयद्युतिं → पुत्रं → कार्तिकेयाभिरक्षितम् → इति."),
        match(2, "Match each word of unit 60 to its meaning.",
              [["द्युति", "splendour"], ["पुत्रम्", "son"], ["अभिरक्षित", "protected"], ["इति", "thus (closes the mantra)"]],
              "The son, his two qualities, and the closing word.",
              "द्युति, पुत्रम्, अभिरक्षित, इति.", role="extend",
              teaches="इति at the end closes a quotation or mantra: here the mantra begun in unit 58 ends."),
        mcq("discriminate", 3, "How do the two compounds of unit 60 differ?",
            ("द्युति one is bahuvrīhi, अभिरक्षित one tatpuruṣa",
             "कार्तिकेयद्युति = (a son) whose splendour is Kārtikeya's; कार्तिकेयाभिरक्षित = protected by Kārtikeya."),
            [("द्युति one is tatpuruṣa, अभिरक्षित one bahuvrīhi", "The data labels them the other way round."),
             ("Both are dvandva compounds", "Neither lists items joined by and."),
             ("Both mean protected by Kārtikeya", "Only the second means protected; the first means splendour.")],
            "One describes the son by what he has (bahuvrīhi); the other says by whom he is protected (tatpuruṣa).",
            "कार्तिकेयद्युति: bahuvrīhi · कार्तिकेयाभिरक्षित: tatpuruṣa."),
        mcq("apply", 4, "What does इति at the end of unit 60 do?",
            ("It closes the mantra", "The data note: the closing इति ends the mantra."),
            [("It begins a new mantra", "इति closes; the new mantra is introduced by तथा in unit 61."),
             ("It means therefore", "Here it marks the end of the quoted words."),
             ("It turns the line into a question", "इति does not make a question.")],
            "इति marks the end of the quoted mantra.",
            "इति = thus (end of quotation)."),
        mcq("transfer", 5, "By the rule of कार्तिकेयाभिरक्षितम्, how is राम + अभिरक्षितः (protected by Rāma) joined?",
            ("रामाभिरक्षितः", "अ + अ → आ, as कार्तिकेय + अभिरक्षितम् → कार्तिकेयाभिरक्षितम्."),
            [("रामभिरक्षितः", "The two अ merge into a long आ; neither is lost."),
             ("रामेभिरक्षितः", "अ + इ gives ए; here the second vowel is अ."),
             ("रामोभिरक्षितः", "अ + उ gives ओ; here the second vowel is अ.")],
            "राम + अभिरक्षितः = रामाभिरक्षितः.",
            "अ + अ → आ.",
            teaches="अ + अ → आ: कार्तिकेय + अभिरक्षितम् → कार्तिकेयाभिरक्षितम्."),
    ],
}

# ---------------------------------------------------------------- unit 61
AUTHORED["61"] = {
    "title": "तथा",
    "question": "What does the one-word unit 61 say?",
    "rule": ("तथा: likewise. A single indeclinable on its own printed line; the data takes it as the link before a "
             "second mantra. (In general Sanskrit, तथा also answers यथा: as ... so.)"),
    "limits": ("Prose, one word, no verb. The data takes it as the link before a second mantra; the unit itself says no more."),
    "explain_hi": ("एक शब्द की गद्य-पंक्ति: ‘तथा’, यानी वैसे ही। यह अव्यय है। "
                   "डेटा के अनुसार यह आगे आने वाले दूसरे मन्त्र से पहले जोड़ने वाला शब्द है। "
                   "व्याकरण में ‘यथा ... तथा’ (जैसे ... वैसे) का जोड़ा प्रसिद्ध है; यहाँ केवल ‘तथा’ है।"),
    "hook": "तथा = वैसे ही; यथा का साथी।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "What does unit 61, the single word तथा, mean?",
            ("Likewise", "तथा = likewise, in the same way."),
            [("Not so", "Negation would need न."),
             ("Here", "here would be इह or अत्र."),
             ("When", "when would be यदा.")],
            "तथा = likewise.",
            "तथा = likewise, so."),
        mcq("warmup", 1, "What kind of unit is 61?",
            ("A prose line of one word", "The data type is prose: the single word तथा."),
            [("A metrical verse line", "One word is not a metrical line."),
             ("A list of divine names", "No names are in unit 61."),
             ("A command with a verb", "Unit 61 has no verb.")],
            "Unit 61 is one indeclinable on its own printed line.",
            "Unit 61 = तथा (prose, one word)."),
        fill(2, "Likewise: ____ (type it in Devanagari or in English letters, e.g. dharma).",
             accepts("तथा", None, "tatha"),
             "The whole unit is तथा.",
             "तथा = likewise, so; an indeclinable, the partner of यथा (as).",
             "तथा = likewise."),
        mcq("discriminate", 3, "Which word means as and pairs with तथा (so) in Sanskrit?",
            ("यथा", "यथा ... तथा = as ... so."),
            [("यदा", "यदा means when; its partner is तदा."),
             ("तदा", "तदा means then, the partner of यदा."),
             ("अथ", "अथ means now, then: it opens a topic.")],
            "यथा ... तथा = as ... so.",
            "यथा (as) ↔ तथा (so)."),
        multi("apply", 4, "Which statements about unit 61 are right?",
              [("तथा is an indeclinable", "Right: the data labels it ind."),
               ("It names a deity", "No deity is named in unit 61."),
               ("It has no verb of its own", "Right: one word, no verb."),
               ("It is a metrical verse", "It is prose.")],
              [0, 2],
              "One indeclinable, no verb, prose.",
              "तथा = ind., likewise."),
        mcq("transfer", 5, "In the invented line यथा गुरुस्तथा शिष्यः, what does तथा mean?",
            ("so: the pupil is so", "यथा ... तथा = as the teacher, so the pupil."),
            [("when: when the pupil is", "when would be यदा."),
             ("not: the pupil is not", "not would be न."),
             ("here: the pupil is here", "here would be इह or अत्र.")],
            "As the teacher, so the pupil: तथा answers यथा.",
            "यथा ... तथा = as ... so.",
            teaches="तथा (so, likewise) answers यथा (as): यथा गुरुस्तथा शिष्यः, as the teacher, so the pupil."),
    ],
}

# ---------------------------------------------------------------- unit 62
AUTHORED["62"] = {
    "title": "इहामृतं चसोमश्च",
    "question": "By unit 62, what does the second mantra wish to dwell in the house?",
    "rule": ("Here: nectar (अमृत), Soma, Citrabhānu, O lady (भामिनि), and Uccaiḥśravas, the horse (तुरगः): may they dwell "
             "(निवसन्तु, plural) in the house (मन्दिरे)."),
    "limits": ("Citrabhānu is an epithet (of fire or the sun); which one is not stated: no question on it. ते may be your or "
               "to you. That the plural verb takes all four names as subjects is the data's probable reading."),
    "explain_hi": ("दूसरे मन्त्र का अनुष्टुभ् श्लोक: यहाँ अमृत, सोम और चित्रभानु, हे भामिनी, और उच्चैःश्रवा घोड़ा, तुम्हारे घर में निवास करें। "
                   "‘निवसन्तु’ बहुवचन आज्ञार्थ है; डेटा के अनुसार चारों नाम सम्भवतः उसके कर्ता हैं। "
                   "‘चित्रभानु’ अग्नि या सूर्य का उपनाम है; कौन-सा, नहीं कहा। ‘ते’ = तुम्हारे (या तुम्हारे लिए)। "
                   "छपा ‘चसोमश्च’ = च सोमः च; ‘निवसंतुते’ = निवसन्तु ते।"),
    "hook": "अमृत, सोम, चित्रभानु, उच्चैःश्रवा: घर में बसें।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 62, where are they asked to dwell?",
            ("In the house", "मन्दिरे निवसन्तु: may they dwell in the house."),
            [("In the forest", "No forest is named in unit 62."),
             ("In the sky", "No sky is named in unit 62."),
             ("In the sea", "No sea is named in unit 62.")],
            "The wish is that they dwell in the house.",
            "मन्दिरे निवसन्तु = may they dwell in the house."),
        order(1, "Put the parts of unit 62 in the verse's order.",
              ["इहामृतं", "चसोमश्च", "चित्रभानुश्च", "भामिनि", "उच्चैःश्रवाश्च तुरगो", "मंदिरे निवसंतुते"],
              "Here nectar, and Soma, and Citrabhānu, O lady; and Uccaiḥśravas the horse; in the house may they dwell.",
              "इहामृतं → चसोमश्च → चित्रभानुश्च → भामिनि → उच्चैःश्रवाश्च तुरगो → मंदिरे निवसंतुते."),
        match(2, "Match each word of unit 62 to its meaning.",
              [["अमृतम्", "nectar"], ["तुरगः", "horse"], ["मन्दिरे", "in the house"], ["भामिनि", "O lady"],
               ["निवसन्तु", "may they dwell"]],
              "What dwells, where, and the address to the woman.",
              "अमृतम्, तुरगः, मन्दिरे, भामिनि, निवसन्तु.", role="extend",
              teaches="-अन्तु is the third-person plural imperative: निवसन्तु = may they dwell."),
        mcq("discriminate", 3, "Which split of उच्चैःश्रवाश्च is right?",
            ("उच्चैःश्रवाः + च", "A visarga before च becomes श्: श्रवाः + च → श्रवाश्च."),
            [("उच्चैःश्रव + च", "With a short final अ the join would be उच्चैःश्रवच, with no श्."),
             ("उच्चैःश्रवाः + श्च", "श्च is not a word; the particle is च."),
             ("उच्चैःश्रवे + च", "ए + च would stay उच्चैःश्रवे च.")],
            "उच्चैःश्रवाः (the horse's name) + च (and).",
            "Visarga + च → श्च."),
        mcq("apply", 4, "In unit 62, what is Uccaiḥśravas called?",
            ("A horse", "उच्चैःश्रवाश्च तुरगः: Uccaiḥśravas, the horse."),
            [("A river", "No river is named in unit 62."),
             ("A bird", "The line says तुरगः, horse."),
             ("A sage", "The line says तुरगः, horse.")],
            "तुरगः = horse: the line names Uccaiḥśravas as a horse.",
            "तुरगः = horse."),
        mcq("transfer", 5, "By the rule of सोमश्च, how is बालः + च (and the boy) joined?",
            ("बालश्च", "A visarga before च becomes श्, as सोमः + च → सोमश्च."),
            [("बालो च", "अः → ओ comes before a voiced sound; च is unvoiced."),
             ("बालर्च", "र् comes after vowels other than अ/आ, and before voiced sounds."),
             ("बालस्च", "स् comes before त or थ, not before च.")],
            "बालः + च = बालश्च, like सोमः + च = सोमश्च.",
            "Visarga + च → श्च.",
            teaches="A visarga before च becomes श्: सोमः + च → सोमश्च, उच्चैःश्रवाः + च → उच्चैःश्रवाश्च."),
    ],
}

# ---------------------------------------------------------------- unit 63
AUTHORED["63"] = {
    "title": "इदममृतमपां",
    "question": "By unit 63, what is the nectar drawn from the waters asked to do?",
    "rule": ("इदम् अमृतम् अपां समुद्धृतम्: this nectar, drawn up from the waters, indeed: may it release (प्रमुञ्चतु) "
             "this fetus of yours, O woman (स्त्रि)."),
    "limits": ("लघु is taken as quickly; it may mean lightly or easily: no question on it. The card reports the mantra's "
               "words; it adds no claim about its effect."),
    "explain_hi": ("जलों से निकाला गया यह अमृत, निश्चय ही (वै), हे स्त्री, तुम्हारे इस गर्भ को शीघ्र छोड़ दे। "
                   "‘अपाम्’ षष्ठी बहुवचन है: जलों का (से निकाला)। ‘प्रमुञ्चतु’ आज्ञार्थ प्रथम पुरुष: छोड़े, मुक्त करे। "
                   "‘स्त्रि’ स्त्री का सम्बोधन है। ‘लघु’ को शीघ्र माना गया; हल्के से या आसानी से भी हो सकता है।"),
    "hook": "जलों का अमृत: इस गर्भ को छोड़ दे, हे स्त्री।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 63, from what was the nectar (amṛta) drawn up?",
            ("From the waters", "अमृतम् अपां समुद्धृतम्: nectar drawn up from the waters."),
            [("From the sky", "No sky is named in unit 63."),
             ("From milk", "No milk is named in unit 63."),
             ("From the moon", "No moon is named in unit 63.")],
            "The nectar is drawn up from the waters.",
            "अपां समुद्धृतम् = drawn up from the waters."),
        order(1, "Put the parts of unit 63 in the line's order.",
              ["इदममृतमपां", "समुद्धृतं वै", "तव", "लघु", "गर्भमिमं", "प्रमुंचतु स्त्रि"],
              "This nectar of the waters, drawn up indeed, your, quickly, this fetus, may it release, O woman.",
              "इदममृतमपां → समुद्धृतं वै → तव → लघु → गर्भमिमं → प्रमुंचतु स्त्रि."),
        match(2, "Match each word of unit 63 to its meaning.",
              [["अमृतम्", "nectar"], ["समुद्धृतम्", "drawn up"], ["गर्भम्", "fetus"], ["प्रमुञ्चतु", "may it release"],
               ["स्त्रि", "O woman"]],
              "What, from where, and what it is asked to do.",
              "अमृतम्, समुद्धृतम्, गर्भम्, प्रमुञ्चतु, स्त्रि.", role="extend",
              teaches="प्रमुञ्चतु is a third-person imperative: may it release."),
        mcq("discriminate", 3, "Which form addresses the woman in unit 63?",
            ("स्त्रि", "The vocative of स्त्री: O woman."),
            [("स्त्री", "The nominative, woman, as a subject."),
             ("स्त्रियम्", "The accusative, woman, as an object."),
             ("स्त्रियाः", "Genitive or ablative: of or from the woman.")],
            "स्त्रि (short इ) is the regular vocative of स्त्री.",
            "स्त्री → vocative स्त्रि."),
        mcq("apply", 4, "In unit 63, what is the nectar asked to do?",
            ("Release this fetus", "गर्भमिमं प्रमुञ्चतु: may it release this fetus."),
            [("Dwell in the house", "Dwelling in the house is the wish of unit 62."),
             ("Protect the attendant", "No attendant is named in unit 63."),
             ("Grant a son's splendour", "The splendour of Kārtikeya is in unit 60.")],
            "The wish of this line: may the nectar release the fetus.",
            "प्रमुञ्चतु = may it release."),
        mcq("transfer", 5, "By the rule of गर्भमिमम्, how is फलम् + अस्ति (there is fruit) joined?",
            ("फलमस्ति", "A final म् before a vowel stays म् and joins it, as गर्भम् + इमम् → गर्भमिमम्."),
            [("फलोऽस्ति", "ओऽ comes from अः + अ, not from अम्."),
             ("फलास्ति", "The म् is not dropped before a vowel."),
             ("फलंस्ति", "Anusvāra stands before a consonant; and the अ of अस्ति is not lost.")],
            "फलम् + अस्ति = फलमस्ति, like गर्भम् + इमम् = गर्भमिमम्.",
            "Final म् + vowel → म + vowel.",
            teaches="A final म् before a vowel joins it: गर्भम् + इमम् → गर्भमिमम्, इदम् + अमृतम् → इदममृतम्."),
    ],
}

# ---------------------------------------------------------------- unit 64
AUTHORED["64"] = {
    "title": "दिशंतु शांतिमिति",
    "question": "By unit 64, what are the beings of the mantra asked to grant?",
    "rule": ("May they, with the bearers of salt water (लवणाम्बुधरैः सह), grant peace (दिशन्तु शान्तिम्). On a corrected "
             "reading they are fire, wind, sun and Indra. इति closes the mantra."),
    "limits": ("Medium confidence: the list of names rests on reading अनल्पवन as अनलपवन: no question on the list. ते may be "
               "to you or they; whether the salt-water bearers are oceans or clouds is not clear: no question asks what they are."),
    "explain_hi": ("अनुमानित पाठ पर: इसलिए अग्नि, वायु, सूर्य और इन्द्र, लवण-जल धारण करने वालों के साथ, तुम्हें शान्ति दें। "
                   "छपा ‘अनल्पवन’ यहाँ अर्थ नहीं देता (‘अनल्प’ = बहुत, पर ‘अनल्प-वन’ सूची में नहीं बैठता); ‘अनल-पवन’ (अग्नि, वायु) पढ़ने पर ही यह सूची बनती है, इसलिए सूची पर प्रश्न नहीं। "
                   "‘लवणाम्बुधर’ शब्दशः लवण-जल धारण करने वाले हैं; समुद्र या मेघ, स्पष्ट नहीं। "
                   "‘दिशन्तु’ बहुवचन आज्ञार्थ है: दें; अन्त का ‘इति’ मन्त्र समाप्त करता है।"),
    "hook": "लवणाम्बुधरों के साथ: दिशन्तु शान्तिम्, शान्ति दें।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 64, what are they asked to grant?",
            ("Peace", "दिशन्तु शान्तिम्: may they grant peace."),
            [("A son", "A son is named in unit 60, not here."),
             ("Long life", "No long life is named in unit 64."),
             ("Wealth", "No wealth is named in unit 64.")],
            "The mantra ends with a wish for peace.",
            "दिशन्तु शान्तिम् = may they grant peace."),
        order(1, "Put these parts of unit 64 in the line's order.",
              ["तदनल्पवनार्कवासवास्ते", "सह", "लवणांबुधरैः", "दिशंतु", "शांतिमिति"],
              "(Read as: therefore fire, wind, sun, Indra; corrected reading) ..., together with, the bearers of salt water, may they grant, peace: thus.",
              "तदनल्पवनार्कवासवास्ते → सह → लवणांबुधरैः → दिशंतु → शांतिमिति."),
        match(2, "Match each word of unit 64 to its meaning.",
              [["सह", "together with"], ["दिशन्तु", "may they grant"], ["शान्तिम्", "peace"],
               ["इति", "thus (closes the mantra)"]],
              "The sure words of the wish.",
              "सह, दिशन्तु, शान्तिम्, इति.", role="extend",
              teaches="सह takes the instrumental: लवणाम्बुधरैः सह = together with the bearers of salt water."),
        mcq("discriminate", 3, "Which split of लवणांबुधरैर्दिशंतु is right?",
            ("लवणाम्बुधरैः + दिशन्तु", "A visarga after ऐ becomes र् before the voiced द."),
            [("लवणाम्बुधरः + दिशन्तु", "अः before द would give ओ: लवणाम्बुधरो दिशन्तु."),
             ("लवणाम्बुधराः + दिशन्तु", "आः before द would drop the visarga: लवणाम्बुधरा दिशन्तु."),
             ("लवणाम्बुधरै + र्दिशन्तु", "र्दिशन्तु is not a word; the verb is दिशन्तु.")],
            "लवणाम्बुधरैः (instrumental plural, with सह) + दिशन्तु (may they grant).",
            "ऐः + voiced sound → ऐर्."),
        mcq("apply", 4, "Which word of unit 64 shows that more than one is asked to grant?",
            ("दिशन्तु", "3rd plural imperative: may they grant."),
            [("शान्तिम्", "Accusative singular: the thing granted."),
             ("इति", "A closing particle: thus."),
             ("सह", "An indeclinable, together with; it does not mark the verb's number.")],
            "The plural ending -अन्तु in दिशन्तु shows several subjects.",
            "दिशन्तु = may they grant (plural)."),
        mcq("transfer", 5, "By the rule of लवणाम्बुधरैर्दिशन्तु, how is देवैः + दत्तम् (given by the gods) joined?",
            ("देवैर्दत्तम्", "A visarga after ऐ becomes र् before a voiced sound."),
            [("देवै दत्तम्", "After ऐ the visarga becomes र् before a voiced sound; it is dropped only after आ (after अ it gives ओ)."),
             ("देवैस्दत्तम्", "स् comes only before त or थ."),
             ("देवैश्दत्तम्", "श् comes only before च, छ or श.")],
            "देवैः + दत्तम् = देवैर्दत्तम्, like लवणाम्बुधरैः + दिशन्तु.",
            "ऐः + voiced sound → ऐर्.",
            teaches="A visarga after a vowel other than अ/आ becomes र् before a voiced sound: लवणाम्बुधरैः + दिशन्तु → लवणाम्बुधरैर्दिशन्तु."),
    ],
}


# ===================================================================== NOTES_HI
NOTES_HI = {
    "52": ("गद्य; विश्वास उच्च। पाठ-चिह्न: छपा ‘तत्तू’ — सम्भवतः ‘तत्तु’ (तत् + तु), दीर्घ ऊ की आवश्यकता नहीं; इस पर प्रश्न नहीं। "
           "क्रिया ‘है’ समझी जाती है। ‘तत्’ इकाई 51 के मत (मूसल से ओखली पर प्रहार) की ओर। सन्धि: तत् + तु → तत्तु (कोई परिवर्तन नहीं)।"),
    "53": ("गद्य; विश्वास उच्च; कोई पाठ-चिह्न नहीं। ‘गर्भिण्याः’ षष्ठी, ‘गर्भिणी के लिए’ अर्थ में। व्यायाम = परिश्रम। "
           "सन्धि जाँची: सततम् + उपदिश्यते → सततमुपदिश्यते; दारुणव्यायामवर्जनम् + हि → वर्जनं हि (व्यंजन से पहले म् → अनुस्वार)।"),
    "54": ("गद्य; विश्वास निम्न; अनुमानित पाठ। पाठ-चिह्न: ‘त्रार्या’ कोई शब्द नहीं (सम्भवतः ‘नार्याः’, निश्चित नहीं); "
           "‘मुशल्यायाम’ भी शब्द नहीं — प्रसंग से ‘मुशल-व्यायाम’ (मूसल से परिश्रम) का अनुमान, पर यह अर्थ में नहीं लिया गया; "
           "छपा ‘वायुअंतरं’ में र् छूटा: वायुः + अन्तरम् → वायुरन्तरम् होना चाहिए। इन तीनों पर प्रश्न नहीं। "
           "‘अन्तर’ = छिद्र (या अवसर)। ‘धातु-दोष’ द्वन्द्व माना गया। ‘हिंस्यात्’ सम्भावना है। "
           "सन्धि जाँची: विशेषतः + च → विशेषतश्च; हिंस्यात् + इति → हिंस्यादिति (त् → द् स्वर से पहले); ईरितः + वायुः → ईरितो वायुः।"),
    "55": ("गद्य; विश्वास मध्यम; कोई पाठ-चिह्न नहीं। ‘पादाभ्याम्’ किसके पैर, नहीं कहा (स्वाभाविक अर्थ: परिचारिका के)। "
           "‘पर्यङ्क’ = पलंग (या बैठने का आसन)। ‘अनुलोम’ = स्वाभाविक दिशा में; अधिक विवरण नहीं। अभ्यंग का द्रव्य नहीं बताया। "
           "सन्धि जाँची: पादतः + अस्याः → पादतोऽस्याः (अः + अ → ओऽ); अस्याः + निषण्णायाः → अस्या निषण्णायाः; "
           "निषण्णायाः + योनिम् → निषण्णाया योनिम् (आः → आ घोष से पहले); पर्यङ्कम् + एनाम् + आरोप्य → पर्यंकमेनामारोप्य; "
           "अभि + अज्य → अभ्यज्य (इ + अ → य)।"),
    "56": ("गद्य; विश्वास उच्च; कोई पाठ-चिह्न नहीं। कर्ता (इकाई 55 की कुशल स्त्री) यहाँ नहीं लिखा। कैसे फैलाना, नहीं कहा। "
           "छपा ‘योनिं’ = योनिम् (व्यंजन से पहले अनुस्वार); ‘पुनःपुनः’ बिना अन्तराल।"),
    "57": ("गद्य; विश्वास मध्यम; अनुमानित पाठ। पाठ-चिह्न: ‘सुप्रसन्नेते’ → सुप्रसन्नस्ते (तुम्हारा … बहुत निर्मल); "
           "‘जनयिष्यतीति’ → जनयिष्यसीति (सम्बोधित ‘तुम’ के लिए मध्यम पुरुष)। दोनों सुधार डेटा में अपनाए गए; इन पर प्रश्न नहीं। "
           "छपे रूप में ‘जनयिष्यति’ का कर्ता मुख-वर्ण या अलिखित ‘वह’ होता। प्रवाहण = जोर लगाना। "
           "सन्धि जाँची: ब्रूयात् + च → ब्रूयाच्च (त् + च → च्च)।"),
    "58": ("गद्य (दो छपी पंक्तियाँ जोड़ी गईं); विश्वास उच्च; कोई पाठ-चिह्न नहीं। [02.03.61] ‘अन्या’ स्त्रीलिंग: दूसरी स्त्री। "
           "[02.03.62] वर्गीकरण: नामों की सूची में क्रिया नहीं; डेटा के अनुसार यह इकाई 59 में आगे चलती है, जहाँ की एकवचन क्रियाएँ "
           "(पातु, दधातु) सम्भवतः इन्हीं की हैं, यद्यपि नाम सात हैं। दूसरी छपी पंक्ति (8+8 अक्षर) अनुष्टुभ् की अर्धाली जैसी लगती है (लेखक का अवलोकन; डेटा में नहीं)। "
           "सन्धि जाँची: वामकर्णे + अस्याः → वामकर्णेऽस्याः (ए + अ → एऽ); अस्याः + मन्त्रम् → अस्या मन्त्रम्; मन्त्रम् + इमम् → मन्त्रमिमम्; "
           "क्षितिः + जलम् → क्षितिर्जलम्; तेजः + वायुः → तेजो वायुः; वायुः + विष्णुः → वायुर्विष्णुः।"),
    "59": ("श्लोक (अनुष्टुभ्); विश्वास मध्यम; कोई पाठ-चिह्न नहीं। [02.03.63] वर्गीकरण: पिछली पंक्ति के नामों से जुड़ता लगता है; "
           "कर्ता नहीं लिखा। ‘शल्य’ = काँटा/बाहरी वस्तु/चुभती पीड़ा — यहाँ ठीक अर्थ अनिश्चित। ‘वा … अपि’ का अर्थ ढीला। "
           "[02.03.64] ‘अविक्लिष्टम्’ अगली इकाई के ‘पुत्रम्’ से (सम्भावित) या क्रियाविशेषण ‘बिना कष्ट’ — दो तरह; इस पर प्रश्न नहीं। "
           "छपा ‘ळ’ (अविक्ळिष्ट) ‘ल’ माना गया। सन्धि जाँची: दधातु + अपि → दधात्वपि (उ + अ → व); त्वम् + अविक्लिष्टम् → त्वमविक्लिष्टम्; "
           "शुभ + आनने → शुभानने (अ + आ → आ)।"),
    "60": ("गद्य; विश्वास उच्च; कोई पाठ-चिह्न नहीं। अध्याहार: क्रिया ‘प्रसूष्व’ इकाई 59 से; कोई क्रिया जोड़ी नहीं गई। "
           "कार्तिकेय देवता का नाम, जैसा छपा। अन्त का ‘इति’ मन्त्र समाप्त करता है। "
           "सन्धि जाँची: कार्तिकेय + अभिरक्षितम् → कार्तिकेयाभिरक्षितम् (अ + अ → आ); अभिरक्षितम् + इति → अभिरक्षितमिति।"),
    "61": "गद्य; विश्वास उच्च; कोई पाठ-चिह्न नहीं। एक अव्यय ‘तथा’; डेटा के अनुसार आगे के दूसरे मन्त्र से पहले जोड़ने वाला शब्द। कोई सन्धि नहीं।",
    "62": ("श्लोक (अनुष्टुभ्); विश्वास मध्यम; कोई पाठ-चिह्न नहीं। [02.03.67] वर्गीकरण: पहली पंक्ति में क्रिया नहीं; दूसरी पंक्ति की "
           "बहुवचन ‘निवसन्तु’ उसे पूरा करती लगती है। ‘चित्रभानु’ अग्नि या सूर्य का उपनाम — कौन, नहीं कहा। "
           "[02.03.68] ‘ते’ = तुम्हारे (या तुम्हारे लिए)। मन्दिर = घर, निवास। छपा ‘चसोमश्च’ = च सोमः च, ‘निवसंतुते’ = निवसन्तु ते। "
           "सन्धि जाँची: इह + अमृतम् → इहामृतम्; सोमः + च → सोमश्च; चित्रभानुः + च → चित्रभानुश्च; उच्चैःश्रवाः + च → उच्चैःश्रवाश्च; "
           "तुरगः + मन्दिरे → तुरगो मन्दिरे (अः → ओ घोष से पहले)।"),
    "63": ("छन्दोबद्ध पंक्ति (अनुष्टुभ् नहीं, पुष्पिताग्रा-जैसी); डेटा में गद्य-इकाई के रूप में रखी; विश्वास उच्च; कोई पाठ-चिह्न नहीं। ‘स्त्रि’ स्त्री का नियमित सम्बोधन। ‘लघु’ = शीघ्र "
           "(या हल्के से, आसानी से) — दो तरह; इस पर प्रश्न नहीं। "
           "सन्धि जाँची: इदम् + अमृतम् + अपाम् → इदममृतमपाम्; गर्भम् + इमम् → गर्भमिमम्; छपा ‘प्रमुंचतु’ = प्रमुञ्चतु।"),
    "64": ("छन्दोबद्ध पंक्ति (अनुष्टुभ् नहीं, पुष्पिताग्रा-जैसी); डेटा में गद्य-इकाई के रूप में रखी; विश्वास मध्यम। पाठ-चिह्न: छपा ‘अनल्पवन’ यहाँ अर्थ नहीं देता; ‘अनलपवन’ (अग्नि, वायु) पढ़ने पर "
           "अर्क (सूर्य) और वासव (इन्द्र) के साथ सूची बनती है — सूची इसी सुधार पर टिकी है, इस पर प्रश्न नहीं। "
           "‘ते’ = तुम्हें (या ‘वे’); ‘लवणाम्बुधर’ = लवण-जल धारण करने वाले, समुद्र या मेघ स्पष्ट नहीं; ‘अर्क’ यहाँ सूर्य (पौधे का नाम भी); "
           "‘तत्’ = इसलिए (या ‘वह’)। सन्धि जाँची: वासवाः + ते → वासवास्ते (विसर्ग → स् त से पहले); "
           "लवणाम्बुधरैः + दिशन्तु → लवणाम्बुधरैर्दिशन्तु; शान्तिम् + इति → शान्तिमिति।"),
}


# ===================================================================== AIDS
AIDS = {
    "52": {
        "chunks": "तत्तू | न | सम्यक्",
        "frame": "कर्ता ‘तत्’ (वह मत, इकाई 51 का) + ‘न सम्यक्’ (ठीक नहीं); क्रिया ‘है’ समझी जाती है। ‘तु’ = परन्तु।",
        "anchors": "याद-सूत्र: ‘अन्ये तु … आहुः’ (दूसरे कहते हैं) → ‘तत् तु न सम्यक्’ (पर वह ठीक नहीं)। (मेरी याद-पद्धति)",
    },
    "53": {
        "chain": {"steps": ["दूसरों का मत: ओखली पर मूसल-प्रहार (इकाई 51)", "वह ठीक नहीं (इकाई 52)",
                            "हि: गर्भिणी के लिए कठोर व्यायाम-वर्जन सदा उपदिष्ट (इकाई 53)"]},
        "chunks": "दारुणव्यायामवर्जनं हि | गर्भिण्याः | सततमुपदिश्यते",
        "frame": "क्या (दारुण-व्यायाम-वर्जन) → किसके लिए (गर्भिण्याः) → कब (सततम्) → क्रिया (उपदिश्यते, कर्मवाच्य)।",
        "sandhi": "म् + स्वर: सततम् + उपदिश्यते → सततमुपदिश्यते।",
    },
    "54": {
        "chain": {"steps": ["विशेषकर प्रसव के समय", "सब धातु-दोष चलायमान", "कोमलता के कारण",
                            "वायु प्रेरित (किससे: अस्पष्ट)", "अन्तर (छिद्र/अवसर) पाकर", "प्राणों को हानि सम्भव"]},
        "chunks": ("विशेषतश्चप्रसवकाले | प्रचलितसर्वधातुदोषायाः | सौकुमार्यात्त्रार्या (?) | मुशल्यायामेनेरितो (?) | "
                   "वायुअंतरं | लब्ध्वा | प्राणान् हिंस्यादिति"),
        "sandhi": "विसर्ग + च → श्च: विशेषतः + च → विशेषतश्च · त् → द् स्वर से पहले: हिंस्यात् + इति → हिंस्यादिति · अः → ओ घोष से पहले: ईरितः + वायुः → ईरितो वायुः।",
    },
    "55": {
        "chain": {"steps": ["१ गर्भ पलट जाने पर", "२ पर्यंक पर बिठाना", "३ बैठी स्त्री के पैरों की ओर से",
                            "४ योनि का अनुलोम, सुखपूर्वक अभ्यंग", "५ दोनों नितम्ब पैरों से दबाना"]},
        "chunks": ("अथ परिवृत्तगर्भां | पर्यंकमेनामारोप्य | कुशला स्त्री | पादतोऽस्या निषण्णाया | "
                   "योनिमनुलोममनुसुखमभ्यज्य | स्फिजौ पादाभ्यां पीडयेत्"),
        "sandhi": "अः + अ → ओऽ: पादतः + अस्याः → पादतोऽस्याः · आः → आ घोष से पहले: अस्याः + निषण्णायाः → अस्या निषण्णायाः · इ + अ → य: अभि + अज्य → अभ्यज्य।",
        "frame": "कर्ता (कुशला स्त्री) → किसे (परिवृत्तगर्भाम्, एनाम्) → कहाँ (पर्यंक) → कहाँ से (पादतः) → क्या (अभ्यज्य … पीडयेत्)।",
    },
    "56": {
        "chunks": "योनिं च | पुनःपुनः | प्रसारयेत्",
        "frame": "कर्म (योनिम्) → कितनी बार (पुनःपुनः) → क्रिया (प्रसारयेत्); कर्ता इकाई 55 की कुशल स्त्री, अलिखित।",
        "anchors": "शब्द-परिवार: प्र-√सृ → प्रसारयेत् (फैलाए), प्रसार (फैलाव)।",
    },
    "57": {
        "chunks": "ब्रूयाच्च | सुभगे | शनैः शनैः प्रवाहयस्व | सुप्रसन्नेते (?) मुखवर्णः | पुत्रं जनयिष्यतीति (?)",
        "frame": "कौन बोले (परिचारिका: ब्रूयात्) → किससे (सुभगे: प्रसव करती स्त्री) → क्या (शनैः शनैः प्रवाहयस्व) → ढाढ़स (मुख-वर्ण, पुत्र)।",
        "sandhi": "त् + च → च्च: ब्रूयात् + च → ब्रूयाच्च।",
        "puns": "‘शनैः शनैः’ — दो बार ‘धीरे’, दो क़दम धीमे। (मेरी याद-पद्धति)",
    },
    "58": {
        "chain": {"steps": ["१ क्षिति (पृथ्वी)", "२ जल", "३ वियत् (आकाश)", "४ तेज (अग्नि)", "५ वायु", "६ विष्णु", "७ प्रजापति"]},
        "chunks": "अन्या तु | वामकर्णेऽस्या | मंत्रमिमं जपेत् | क्षितिर्जलं | वियत्तेजो | वायुर्विष्णुः | प्रजापतिः",
        "sandhi": "इ/उ के बाद विसर्ग → र् घोष वर्ण से पहले: क्षितिः + जलम् → क्षितिर्जलम्, वायुः + विष्णुः → वायुर्विष्णुः · अः → ओ घोष वर्ण से पहले: तेजः + वायुः → तेजो वायुः · ए + अ → एऽ: वामकर्णे + अस्याः → वामकर्णेऽस्याः।",
        "letters": "क्षि-ज-वि-ते-वा-वि-प्र: सात नामों के पहले अक्षर, मन्त्र के क्रम में।",
    },
    "59": {
        "diagram": {"groups": [
            {"label": "पहली पंक्ति: कामना", "items": ["सगर्भां त्वां सदा पातु: गर्भ सहित तुम्हारी सदा रक्षा करे",
                                                    "वैशल्यं वा दधात्वपि: या शल्य से मुक्ति भी दे"]},
            {"label": "दूसरी पंक्ति: आदेश", "items": ["प्रसूष्व त्वम्: तुम जन्म दो", "अविक्लिष्टा: स्वयं अपीड़ित",
                                                   "शुभानने: हे सुन्दर मुख वाली"]}]},
        "chunks": "सगर्भां त्वां सदापातु | वैशल्यं वा दधात्वपि | प्रसूष्व त्वमविक्ळिष्टम् | अविक्ळिष्टा शुभानने",
        "sandhi": "उ + अ → व: दधातु + अपि → दधात्वपि · अ + आ → आ: शुभ + आनने → शुभानने।",
    },
    "60": {
        "contrast": "कार्तिकेयद्युति (बहुव्रीहि: जिसकी द्युति कार्तिकेय की है) ↔ कार्तिकेयाभिरक्षित (तत्पुरुष: कार्तिकेय से रक्षित) — एक ही नाम, दो तरह के समास।",
        "chunks": "कार्तिकेयद्युतिं | पुत्रं | कार्तिकेयाभिरक्षितमिति",
        "sandhi": "अ + अ → आ: कार्तिकेय + अभिरक्षितम् → कार्तिकेयाभिरक्षितम् · म् + स्वर: अभिरक्षितम् + इति → अभिरक्षितमिति।",
    },
    "61": {
        "chunks": "तथा",
        "anchors": "शब्द-परिवार: यथा (जैसे) ↔ तथा (वैसे); यदा (जब) ↔ तदा (तब)।",
        "frame": "एक अव्यय, अपनी छपी पंक्ति पर; क्रिया नहीं।",
    },
    "62": {
        "diagram": {"groups": [
            {"label": "निवास करें (क्रम से)", "items": ["अमृत", "सोम", "चित्रभानु (अग्नि या सूर्य: अनिश्चित)", "उच्चैःश्रवा, घोड़ा"]},
            {"label": "कहाँ", "items": ["मन्दिरे: घर में"]}]},
        "chunks": "इहामृतं | चसोमश्च | चित्रभानुश्च | भामिनि | उच्चैःश्रवाश्च | तुरगो | मंदिरे | निवसंतुते",
        "sandhi": "विसर्ग + च → श्च: सोमः + च → सोमश्च, उच्चैःश्रवाः + च → उच्चैःश्रवाश्च · अ + अ → आ: इह + अमृतम् → इहामृतम् · अः → ओ घोष वर्ण से पहले: तुरगः + मन्दिरे → तुरगो मन्दिरे।",
    },
    "63": {
        "chunks": "इदममृतमपां | समुद्धृतं वै | तव लघु | गर्भमिमं | प्रमुंचतु स्त्रि",
        "frame": "कर्ता (इदम् अमृतम्, जलों से निकाला) → कर्म (तव गर्भम् इमम्) → क्रिया (प्रमुञ्चतु) → सम्बोधन (स्त्रि)।",
        "sandhi": "म् + स्वर: इदम् + अमृतम् → इदममृतम्, अमृतम् + अपाम् → अमृतमपाम्, गर्भम् + इमम् → गर्भमिमम्।",
    },
    "64": {
        "chunks": "तदनल्पवनार्कवासवास्ते (?) | सह लवणांबुधरैः | दिशंतु | शांतिमिति",
        "frame": "कर्ता (सुधरे पाठ पर: अग्नि, वायु, सूर्य, इन्द्र) → साथ (लवणाम्बुधरैः सह) → क्रिया (दिशन्तु) → कर्म (शान्तिम्)।",
        "sandhi": "ऐ के बाद विसर्ग → र्: लवणाम्बुधरैः + दिशन्तु → लवणाम्बुधरैर्दिशन्तु · विसर्ग → स् त से पहले: वासवाः + ते → वासवास्ते।",
    },
}


# ===================================================================== IMAGE_SPECS
IMAGE_SPECS = {
    ("53", "chain"): {
        "file": "sh3-musala-khandana-53.svg",
        "alt": ("Flowchart of units 51 to 53: others' view, striking a grain-filled mortar with a pestle (unit 51); "
                "that is not right (unit 52); for (hi, read from context as the reason) avoidance of severe exertion is constantly prescribed for a "
                "pregnant woman (unit 53)."),
        "type": "mermaid",
        "code": ("flowchart TD\n"
                 "  A[\"दूसरों का मत (इकाई ५१)\"] --> B[\"ओखली पर मूसल-प्रहार\"]\n"
                 "  B --> C[\"वह ठीक नहीं (इकाई ५२)\"]\n"
                 "  C -->|\"हि: क्योंकि (प्रसंग से)\"| D[\"कठोर व्यायाम-वर्जन\"]\n"
                 "  D --> E[\"गर्भिणी को सदा उपदिष्ट\"]\n"),
    },
    ("54", "chain"): {
        "file": "sh3-prasava-vayu-54.svg",
        "alt": ("Flowchart of the sure parts of unit 54: especially at delivery; all dhātus and doṣas set in motion; "
                "because of delicacy; vāyu (Vāta) stirred up (by what, unclear); having found an opening or opportunity; "
                "it might injure the vital breaths."),
        "type": "mermaid",
        "code": ("flowchart TD\n"
                 "  A[\"विशेषकर प्रसव-काल\"] --> B[\"सब धातु-दोष चलायमान\"]\n"
                 "  B --> C[\"कोमलता के कारण\"]\n"
                 "  C --> D[\"वायु प्रेरित (अस्पष्ट)\"]\n"
                 "  D --> E[\"अन्तर पाकर\"]\n"
                 "  E --> F[\"प्राणों को हानि सम्भव\"]\n"),
    },
    ("55", "chain"): {
        "file": "sh3-prasava-vidhi-55.svg",
        "alt": ("Numbered flowchart of unit 55: 1 once the fetus has turned, 2 placing her on the paryaṅka, 3 from the "
                "foot-side of her as she sits, 4 anointing the yoni in the natural direction, comfortably, 5 pressing "
                "the two buttocks with the feet."),
        "type": "mermaid",
        "code": ("flowchart TD\n"
                 "  A[\"१ गर्भ पलट जाने पर\"] --> B[\"२ पर्यंक पर बिठाना\"]\n"
                 "  B --> C[\"३ पैरों की ओर से\"]\n"
                 "  C --> D[\"४ योनि का अनुलोम अभ्यंग\"]\n"
                 "  D --> E[\"५ नितम्ब पैरों से दबाना\"]\n"),
    },
    ("58", "chain"): {
        "file": "sh3-mantra-nama-58.svg",
        "alt": ("Chain of the seven names of the mantra in unit 58, in order: earth, water, sky, fire, wind, Viṣṇu, "
                "Prajāpati."),
        "type": "chain",
        "title": "बाएँ कान में मन्त्र: नाम क्रम से (इकाई ५८)",
        "steps": ["१ क्षिति (पृथ्वी)", "२ जल", "३ वियत् (आकाश)", "४ तेज (अग्नि)", "५ वायु", "६ विष्णु", "७ प्रजापति"],
    },
    ("59", "diagram"): {
        "file": "sh3-mantra-kamana-59.svg",
        "alt": ("Table of unit 59, phrase by phrase: may (it) protect you with the fetus at all times; or also grant "
                "freedom from the dart; give birth, you; unharmed (the mother); O fair-faced one."),
        "type": "table",
        "title": "इकाई ५९: मन्त्र की कामना और आदेश",
        "heads": ["वाक्यांश", "अर्थ"],
        "rows": [["सगर्भां त्वां सदा पातु", "गर्भ सहित तुम्हारी सदा रक्षा करे"], ["वैशल्यं वा दधात्वपि", "या शल्य से मुक्ति भी दे"],
                 ["प्रसूष्व त्वम्", "तुम जन्म दो"], ["अविक्लिष्टा", "स्वयं अपीड़ित"], ["शुभानने", "हे सुन्दर मुख वाली"]],
    },
    ("62", "diagram"): {
        "file": "sh3-mandire-nivasa-62.svg",
        "alt": ("Table of unit 62: nectar, Soma, Citrabhānu (an epithet of fire or the sun, which is not stated) and "
                "Uccaiḥśravas the horse; may they dwell in the house."),
        "type": "table",
        "title": "इकाई ६२: घर में निवास करें",
        "heads": ["पद (क्रम से)", "टिप्पणी"],
        "rows": [["अमृत", "सुधा"], ["सोम", "नाम, जैसा छपा"], ["चित्रभानु", "अग्नि या सूर्य का उपनाम: अनिश्चित"],
                 ["उच्चैःश्रवा", "घोड़ा (तुरग)"], ["मन्दिरे निवसन्तु", "घर में निवास करें"]],
    },
}
