from helpers import mcq, match, order, fill, multi, accepts


AUTHORED = {}

# ---------------------------------------------------------------- unit 65
AUTHORED["65"] = {
    "title": "तथा पराऽनुशिष्यात्",
    "question": "By unit 65, who else gives instruction at the birth?",
    "rule": ("तथा परा अनुशिष्यात्: likewise another (woman) should instruct. परा is feminine, so a woman is meant; "
             "अनुशिष्यात् is an optative, should instruct."),
    "limits": ("Prose, three words. The line does not name the person instructed (the woman in labour is not stated) and "
               "does not give the words of the instruction; the data notes only that it appears to follow in the next "
               "units. No question rests on what follows."),
    "explain_hi": ("यह छोटी गद्य-पंक्ति कहती है: वैसे ही (तथा) दूसरी (परा) समझाए (अनुशिष्यात्)। "
                   "‘परा’ स्त्रीलिंग है, इसलिए समझाने वाली कोई दूसरी स्त्री है। "
                   "किसे समझाए, यह पंक्ति में नहीं लिखा; प्रसव करती स्त्री समझी जाती है, पर छपा नहीं। "
                   "‘अनुशिष्यात्’ विधिलिङ् (optative) प्रथम पुरुष एकवचन है: समझाए, निर्देश दे। "
                   "डेटा के अनुसार निर्देश के शब्द सम्भवतः अगली इकाइयों में आते हैं; यह इकाई उन्हें नहीं देती।"),
    "hook": "तथा परा: एक और स्त्री, जो समझाए।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 65, who should give the instruction?",
            ("Another woman (परा)", "परा is feminine: another woman should instruct."),
            [("The physician", "No physician is named in unit 65."),
             ("The husband", "No husband is named in unit 65."),
             ("The mother herself", "The line says another (परा), not she herself.")],
            "तथा परा अनुशिष्यात्: likewise another woman should instruct.",
            "परा (f.) = another woman."),
        order(1, "Put the words of unit 65 in the line's order.",
              ["तथा", "परा", "अनुशिष्यात्"],
              "Likewise, another (woman), should instruct.",
              "तथा → परा → अनुशिष्यात्."),
        match(2, "Match each word of unit 65 to its meaning.",
              [["तथा", "likewise"], ["परा", "another (woman)"], ["अनुशिष्यात्", "should instruct"]],
              "Three words make the whole line.",
              "तथा, परा, अनुशिष्यात्.", role="extend",
              teaches="अनुशिष्यात् is an optative, 3rd person singular, of अनु-√शास्: (she) should instruct."),
        mcq("discriminate", 3, "Which split of पराऽनुशिष्यात् is right?",
            ("परा + अनुशिष्यात्", "आ + अ → आ; the print marks the merged अ with ऽ."),
            [("परः + अनुशिष्यात्", "अः + अ would give ओऽ: परोऽनुशिष्यात्."),
             ("परे + अनुशिष्यात्", "ए + अ would keep ए: परेऽनुशिष्यात्."),
             ("परा + नुशिष्यात्", "नुशिष्यात् is not a word; the verb is अनुशिष्यात्.")],
            "परा (another woman) + अनुशिष्यात् (should instruct).",
            "आ + अ → आ (ऽ may mark the merged अ)."),
        multi("apply", 4, "Which statements about unit 65 are right?",
              [("The line gives the words of the instruction", "No words of the instruction are in this line."),
               ("The one who instructs is a woman", "Right: परा is feminine."),
               ("The person instructed is named in the line", "The object is not stated in the line."),
               ("The verb is an optative: should instruct", "Right: अनुशिष्यात्, 3rd singular optative.")],
              [1, 3],
              "A woman (परा) should instruct (optative); neither the person instructed nor the words are in the line.",
              "तथा परा अनुशिष्यात्: who and what kind of command, nothing more."),
        mcq("transfer", 5, "By the rule of पराऽनुशिष्यात्, how is सा + अत्र (she, here) joined?",
            ("सात्र", "आ + अ → आ, as परा + अनुशिष्यात् → परानुशिष्यात् (printed with ऽ)."),
            [("सोऽत्र", "ओऽ comes from अः + अ, as सः + अत्र, not from आ."),
             ("सेत्र", "ए comes from अ/आ + इ, not from आ + अ."),
             ("स्यत्र", "य् comes from इ before a vowel, not from आ.")],
            "सा + अत्र = सात्र, like परा + अनुशिष्यात्.",
            "आ + अ → आ.",
            teaches="Two अ-sounds merge into आ: परा + अनुशिष्यात् → परानुशिष्यात्, सा + अत्र → सात्र."),
    ],
}

# ---------------------------------------------------------------- unit 66
AUTHORED["66"] = {
    "title": "अनागतायां वेदनायां",
    "question": "By unit 66, when is she told not to bear down?",
    "rule": ("अनागतायां वेदनायाम्: when the pain (वेदना) has not yet come, मा (do not) bear down. The two locatives "
             "set the time: while the pain has not come."),
    "limits": ("Prose, medium confidence. The printed verb प्रैवाहिट्टाः is not a form; it is read as प्रवाहिष्ठाः (do "
               "not bear down) by a correction the data calls possible, so no question rests on the verb's form. "
               "That वेदना is the pain of labour is a probable reading from context."),
    "explain_hi": ("यह गद्य-पंक्ति प्रवाहण (नीचे की ओर जोर लगाना) का समय बताती है: जब वेदना अभी नहीं आई हो, तब प्रवाहण मत करो। "
                   "‘अनागतायां वेदनायाम्’ दोनों सप्तमी हैं और समय बताते हैं: वेदना के न आने पर। "
                   "‘मा’ निषेध है: मत। छपी क्रिया ‘प्रैवाहिट्टाः’ कोई रूप नहीं; ‘प्रवाहिष्ठाः’ पढ़ना सम्भावित सुधार है, "
                   "अर्थ अगली इकाई से स्पष्ट है, पर रूप पर प्रश्न नहीं। "
                   "वेदना को प्रसव-वेदना मानना सन्दर्भ से सम्भावित है।"),
    "hook": "वेदना नहीं आई? तो मा: अभी जोर मत लगाओ।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 66, when is she told not to bear down?",
            ("While the pain has not yet come", "अनागतायां वेदनायाम्: when the pain has not come."),
            [("Once the child's head is seen", "No head is named in unit 66."),
             ("After the placenta has fallen", "The placenta is not named in unit 66."),
             ("When the pain is at its height", "The line speaks of pain not yet come.")],
            "Before the pain (वेदना) has come, she must not bear down.",
            "अनागतायां वेदनायाम् = when the pain has not come."),
        order(1, "Put the printed words of unit 66 in the line's order.",
              ["अनागतायां", "वेदनायां", "मा", "प्रैवाहिट्टाः"],
              "Not come, pain, do not, bear down (printed form).",
              "अनागतायां → वेदनायां → मा → प्रैवाहिट्टाः."),
        match(2, "Match each sure word of unit 66 to its meaning.",
              [["अनागतायाम्", "not (yet) come"], ["वेदनायाम्", "pain (when there is)"], ["मा", "do not"]],
              "The time (two locatives) and the prohibition.",
              "अनागतायाम्, वेदनायाम्, मा.", role="extend",
              teaches="Two agreeing locatives set the time of an action: अनागतायां वेदनायाम् = when the pain has not come."),
        mcq("discriminate", 3, "Why is the negative prefix अन्- (not अ-) in अनागतायाम्?",
            ("Before a vowel, अ- becomes अन्-", "आगत begins with आ, so अ- becomes अन्-: अन् + आगता."),
            [("अन्- marks the feminine ending", "The feminine is shown by -आयाम्, not by अन्-."),
             ("अन्- means very, not not", "अन्- negates: अनागत = not come."),
             ("अन्- marks the locative case", "The locative is the ending -आयाम्.")],
            "अन् + आगतायाम् = अनागतायाम्, not yet come.",
            "Negative अ- → अन्- before a vowel."),
        mcq("apply", 4, "In unit 66, what does मा do?",
            ("It forbids: do not", "मा with the verb gives a prohibition: do not bear down."),
            [("It means now, setting the time", "The time is set by the locatives, not by मा."),
             ("It means like, a comparison", "Like is इव (unit 67), not मा."),
             ("It means and, joining words", "And is च, not मा.")],
            "मा is the particle of prohibition.",
            "मा = do not."),
        mcq("transfer", 5, "Built like अनागतायां वेदनायाम्, which phrase says when the physician (वैद्य, m.) has not come?",
            ("अनागते वैद्ये", "Both words in the masculine locative singular, agreeing."),
            [("अनागतायां वैद्ये", "अनागतायाम् is feminine; वैद्य is masculine."),
             ("अनागतो वैद्यः", "Nominative: the physician who has not come, not a time."),
             ("अनागतेन वैद्येन", "Instrumental: by the physician, not when.")],
            "अनागते वैद्ये = when the physician has not come, like अनागतायां वेदनायाम्.",
            "Agreeing locatives = when ... (time of the action).",
            teaches="A noun and its participle in the locative, agreeing in gender, set the time: अनागते वैद्ये, when the physician has not come."),
    ],
}

# ---------------------------------------------------------------- unit 67
AUTHORED["67"] = {
    "title": "अकालप्रवाहणं हि",
    "question": "By unit 67, why is bearing down at the wrong time wrong?",
    "rule": ("Bearing down at the wrong time (अकाल-प्रवाहण) is like forcing out the urges of feces, urine and the rest: "
             "useless and unwholesome, because it causes breathlessness, cough, wasting, hunchedness and so on."),
    "limits": ("Prose. गर्भस्य is taken with अहितम् (unwholesome for the fetus) but could go with the list of harms, so no "
               "question asks whose harms they are. शोष = wasting is labelled probable; अनर्थकरम् may also mean "
               "causing harm. The copula is understood."),
    "explain_hi": ("यह गद्य-पंक्ति पिछली इकाई का कारण बताती है (‘हि’ = क्योंकि)। असमय प्रवाहण वैसा ही है जैसे मल, मूत्र आदि के वेगों को "
                   "जबरन निकालना (उदीरण); यह निरर्थक और अहितकर है। "
                   "कारण: यह श्वास (साँस फूलना), कास (खाँसी), शोष (सूखकर घटना, सम्भावित अर्थ), कुब्जता (कूबड़ापन) आदि करता है। "
                   "‘गर्भस्य’ को ‘अहितम्’ के साथ लिया गया है; सूची के साथ भी जा सकता है, इसलिए किसकी हानि, इस पर प्रश्न नहीं। "
                   "‘-कारित्वात्’ पञ्चमी है: करने के कारण।"),
    "hook": "असमय जोर = वेग को जबरन निकालना: श्वास, कास, शोष, कुब्जता।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 67, bearing down at the wrong time is likened to what?",
            ("Forcing out the urges of feces and urine", "विण्मूत्रादिवेगानाम् इव उदीरणम्: like forcing out those urges."),
            [("Holding back the urges of feces and urine", "Holding back (विधारण) is the likeness of unit 68."),
             ("Lifting a heavy load during the labour", "No load is named in unit 67."),
             ("Fasting through the whole of labour", "No fasting is named in unit 67.")],
            "Untimely bearing down is like forcing out the natural urges.",
            "अकालप्रवाहणम् ≈ वेगों का उदीरण (forcing out)."),
        order(1, "Put the harms named in unit 67 in the line's order.",
              ["श्वास", "कास", "शोष", "कुब्जता"],
              "Breathlessness, cough, wasting, hunchedness, and so on (आदि).",
              "श्वास → कास → शोष → कुब्जता."),
        match(2, "Match each word of unit 67 to its meaning.",
              [["श्वास", "breathlessness"], ["कास", "cough"], ["शोष", "wasting (probable)"],
               ["कुब्जता", "hunchedness"], ["उदीरण", "forcing out"]],
              "The likeness (उदीरण) and the four named harms.",
              "श्वास, कास, शोष, कुब्जता; उदीरण.", role="extend",
              teaches="-कारित्वात् is an ablative of reason: because of causing (breathlessness and the rest)."),
        mcq("discriminate", 3, "Which split of इवोदीरणम् is right?",
            ("इव + उदीरणम्", "अ + उ → ओ: इव + उदीरणम् → इवोदीरणम्."),
            [("एव + उदीरणम्", "That would print एवोदीरणम्, with ए."),
             ("इव + ओदीरणम्", "अ + ओ → औ would print इवौदीरणम्."),
             ("इवः + उदीरणम्", "अः before उ would give इव उदीरणम्, unjoined.")],
            "इव (like) + उदीरणम् (forcing out).",
            "अ + उ → ओ."),
        mcq("apply", 4, "A woman strains hard at the wrong time (अकाल). How does unit 67 judge it?",
            ("Useless and unwholesome (अहित)", "अनर्थकरम् अहितं च: useless and unwholesome."),
            [("Helpful, as it hastens the birth", "The line calls it useless, not helpful."),
             ("Harmless, if it is done gently", "The line names no gentle exception."),
             ("Needed, so that the fetus turns", "Turning is not named in unit 67.")],
            "Untimely bearing down is useless and unwholesome and causes the harms listed.",
            "अकालप्रवाहणम् = अनर्थकरम्, अहितम्."),
        mcq("transfer", 5, "Built like -कारित्वात् (because of causing), which form of गुरुत्व says because of heaviness?",
            ("गुरुत्वात्", "The ablative in -आत् gives the reason, as -कारित्वात्."),
            [("गुरुत्वम्", "Nominative or accusative: heaviness itself."),
             ("गुरुत्वस्य", "Genitive: of heaviness."),
             ("गुरुत्वाय", "Dative: for heaviness.")],
            "गुरुत्वात् = because of heaviness, like श्वास...कारित्वात्, because of causing.",
            "Ablative -आत् = because of.",
            teaches="An ablative in -त्वात् gives the reason: श्वासकास...कारित्वात्, because of causing breathlessness, cough and the rest."),
    ],
}

# ---------------------------------------------------------------- unit 68
AUTHORED["68"] = {
    "title": "तथा तेषामेव विधारणमिव",
    "question": "By unit 68, what does not bearing down when the pain is there lead to?",
    "rule": ("Likewise, not bearing down (अप्रवाहणम्) when there is pain is like holding back (विधारणम्) those very urges: "
             "it is for injury (उपघाताय)."),
    "limits": ("Prose. The text does not say what injury, or to whom. तेषाम् points back to the urges of unit 67. "
               "The copula is understood; उपघाताय is a dative of purpose, rendered leads to injury."),
    "explain_hi": ("पिछली इकाई असमय जोर लगाने को हानिकर कहती है; यह पंक्ति उलटी भूल बताती है। "
                   "वेदना होने पर प्रवाहण न करना वैसा ही है जैसे उन्हीं (मल-मूत्र आदि के) वेगों को रोकना (विधारण), और यह उपघात यानी हानि के लिए है। "
                   "कैसी हानि या किसकी, यह पंक्ति नहीं बताती। "
                   "‘उपघाताय’ चतुर्थी है: हानि के लिए, यानी हानि करता है। ‘अप्रवाहणम्’ में ‘अ’ निषेध है: प्रवाहण न करना।"),
    "hook": "वेदना है पर जोर नहीं? वेग रोकने जैसा: उपघाताय।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 68, what does not bearing down when there is pain lead to?",
            ("Injury (उपघात)", "अप्रवाहणम् उपघाताय: not bearing down is for injury."),
            [("An easy delivery", "The line says injury, not ease."),
             ("Rest for the fetus", "No rest is named in unit 68."),
             ("The birth of a son", "No son is named in unit 68.")],
            "Holding back when the pain has come leads to injury.",
            "उपघाताय = for injury."),
        order(1, "Put the words of unit 68 in the line's order.",
              ["तथा", "तेषामेव", "विधारणमिव", "वेदनायाम्", "अप्रवाहणम्", "उपघाताय"],
              "Likewise, of those very, like the holding back, when there is pain, not bearing down, is for injury.",
              "तथा → तेषामेव → विधारणमिव → वेदनायाम् → अप्रवाहणम् → उपघाताय."),
        match(2, "Match each word of unit 68 to its meaning.",
              [["विधारणम्", "holding back"], ["अप्रवाहणम्", "not bearing down"], ["उपघाताय", "for injury"],
               ["तेषाम्", "of those (urges)"], ["इव", "like"]],
              "The likeness and its result.",
              "विधारणम्, अप्रवाहणम्, उपघाताय, तेषाम्, इव.", role="extend",
              teaches="उपघाताय is a dative of purpose: for injury, that is, it leads to injury."),
        mcq("discriminate", 3, "Which word of unit 68 means not bearing down?",
            ("अप्रवाहणम्", "अ (not) + प्रवाहणम् (bearing down)."),
            [("प्रवाहणम्", "Without अ- it is bearing down itself."),
             ("विधारणम्", "Holding back: the likeness, not the act named."),
             ("उपघाताय", "For injury: the result.")],
            "अ- negates: अप्रवाहणम् = not bearing down.",
            "अ- + प्रवाहणम् = not bearing down."),
        mcq("apply", 4, "A woman feels strong pains but holds back from bearing down. What does unit 68 say of this?",
            ("Injury, as with held-back urges", "वेदनायाम् अप्रवाहणम् उपघाताय, like विधारण of the urges."),
            [("It shields the fetus until the end", "The line calls it injurious, not protective."),
             ("It is right until the head is seen", "No such stage is named in unit 68."),
             ("It is neither good nor harmful", "The line says it is for injury.")],
            "Not bearing down when the pain is there is as harmful as suppressing urges.",
            "वेदना + अप्रवाहण → उपघात."),
        mcq("transfer", 5, "Built like उपघाताय (for injury), which form of आरोग्य (n.) says for health?",
            ("आरोग्याय", "The dative in -आय gives the purpose, as उपघाताय."),
            [("आरोग्यात्", "Ablative: from or because of health."),
             ("आरोग्येण", "Instrumental: by health."),
             ("आरोग्यस्य", "Genitive: of health.")],
            "आरोग्याय = for health, like उपघाताय = for injury.",
            "Dative -आय = for (purpose).",
            teaches="A dative in -आय states the purpose or result: उपघाताय, for injury; आरोग्याय, for health."),
    ],
}

# ---------------------------------------------------------------- unit 69
AUTHORED["69"] = {
    "title": "ततो यथोक्तं कुरुष्व",
    "question": "By unit 69, how is she to bear down at first?",
    "rule": ("ततः यथोक्तं कुरुष्व: then do as stated; शनैः शनैः (gently, gently) and पूर्वम् (at first) bear down. "
             "कुरुष्व is a 2nd person singular imperative: do."),
    "limits": ("Prose, medium confidence. The printed verb प्रबाहिष्टाः is read as प्रवाहिष्ठाः (b/v and a lost h; a "
               "possible correction): no question on its form. The sentence appears to run on into unit 70 (the data's "
               "GROUPING note); questions stay inside unit 69."),
    "explain_hi": ("तब (ततः) जैसा कहा गया है (यथोक्तम्) वैसा करो (कुरुष्व); धीरे-धीरे (शनैः शनैः), और पहले (पूर्वम्) प्रवाहण करो। "
                   "‘कुरुष्व’ आत्मनेपद आज्ञार्थ मध्यम पुरुष एकवचन है: तुम करो। "
                   "छपा ‘प्रबाहिष्टाः’ ब/व के भ्रम और लुप्त ह से ‘प्रवाहिष्ठाः’ पढ़ा गया है (सम्भावित सुधार), इसलिए उसके रूप पर प्रश्न नहीं। "
                   "डेटा के अनुसार यह वाक्य अगली इकाई में आगे चलता प्रतीत होता है, जहाँ बाद की अवस्थाएँ हैं।"),
    "hook": "पहले शनैः शनैः: धीरे-धीरे जोर।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 69, how is the first bearing down to be done?",
            ("Gently, gently (शनैः शनैः)", "शनैः शनैः ... पूर्वम्: gently, at first."),
            [("As hard as she can", "The line says gently, not hard."),
             ("Not at all, holding back", "The line says to do it, gently."),
             ("Only when the head shows", "No head is named in unit 69.")],
            "At first, the bearing down is gentle.",
            "शनैः शनैः = gently, gently; पूर्वम् = at first."),
        order(1, "Put the printed words of unit 69 in the line's order.",
              ["ततो", "यथोक्तं", "कुरुष्व", "शनैः शनैश्च", "पूर्वं", "प्रबाहिष्टाः"],
              "Then, as stated, do, gently gently and, at first, bear down (printed form).",
              "ततो → यथोक्तं → कुरुष्व → शनैः शनैश्च → पूर्वं → प्रबाहिष्टाः."),
        match(2, "Match each word of unit 69 to its meaning.",
              [["ततः", "then"], ["यथोक्तम्", "as stated"], ["कुरुष्व", "do"], ["शनैः", "gently"], ["पूर्वम्", "at first"]],
              "The command and how and when to carry it out.",
              "ततः, यथोक्तम्, कुरुष्व, शनैः, पूर्वम्.", role="extend",
              teaches="कुरुष्व is the 2nd person singular middle imperative of √कृ: (you) do."),
        mcq("discriminate", 3, "Why is शनैः written शनैश् before च in unit 69?",
            ("A visarga before च becomes श्", "शनैः + च → शनैश्च."),
            [("A visarga before च becomes र्", "र् comes before voiced sounds; च is not voiced."),
             ("The word itself ends in श्", "The word is शनैः, with a visarga."),
             ("A visarga before any consonant is श्", "Before त it is स्, before voiced sounds र् here.")],
            "शनैः + च = शनैश्च: visarga → श् before च, छ, श.",
            "Visarga + च → श्च."),
        mcq("apply", 4, "By the word यथोक्तम् in unit 69, how is she to act?",
            ("As has already been stated", "यथा + उक्तम्: as (it was) said."),
            [("As she herself thinks best", "The line points to what was said, not to her own wish."),
             ("Against what was said before", "यथा means as, in the same way, not against."),
             ("Only as the omens will show", "No omens are named in unit 69.")],
            "यथोक्तम् = यथा + उक्तम्, as stated.",
            "यथोक्तम् = as stated."),
        mcq("transfer", 5, "By the rule of ततो यथोक्तम्, how is रामः + याति (Rāma goes) written?",
            ("रामो याति", "अः before a voiced sound → ओ, as ततः + यथोक्तम् → ततो यथोक्तम्."),
            [("रामा याति", "The visarga drops before a voiced sound after आ, not after अ."),
             ("रामर्याति", "र् comes after vowels other than अ and आ."),
             ("रामश्याति", "श् comes only before च, छ or श.")],
            "रामः + याति = रामो याति, like ततः + यथोक्तम्.",
            "अः + voiced consonant → ओ.",
            teaches="A visarga after short अ becomes ओ before a voiced consonant: ततः + यथोक्तम् → ततो यथोक्तम्."),
    ],
}

# ---------------------------------------------------------------- unit 70
AUTHORED["70"] = {
    "title": "निर्गमे बाढं गर्भस्य",
    "question": "By unit 70, how strongly is she to bear down as the fetus comes out?",
    "rule": ("At the exit of the fetus, strongly (बाढम्); on its arrival at the mouth of the yoni, more strongly (बाढतरम्), "
             "until delivery (आ प्रसवात्). The verb bear down is carried from unit 69."),
    "limits": ("Prose, elliptical: no verb is printed; bear down is understood from unit 69 (the data's GROUPING note). "
               "गर्भस्य probably goes with both stages. The line gives no time or count for the stages."),
    "explain_hi": ("यह पंक्ति प्रवाहण की बाद की अवस्थाएँ बताती है; क्रिया पिछली इकाई से समझी जाती है, यहाँ छपी नहीं। "
                   "गर्भ के निकलने (निर्गम) पर जोर से (बाढम्); योनि के मुख तक पहुँचने पर और अधिक जोर से (बाढतरम्), प्रसव तक (आ प्रसवात्)। "
                   "‘-तर’ तुलना का प्रत्यय है: अधिक। अन्त का ‘इति’ निर्देश समाप्त करता है। "
                   "‘गर्भस्य’ सम्भवतः दोनों अवस्थाओं से जुड़ता है।"),
    "hook": "निकलते समय बाढम्, योनिमुख पर बाढतरम्, प्रसव तक।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 70, when is she to bear down more strongly (बाढतरम्)?",
            ("On reaching the yoni's mouth", "योनिमुखप्रतिपत्तौ बाढतरम्: on arrival at the mouth of the yoni."),
            [("Before the pains of labour begin", "No bearing down before the pain: unit 70 names no such stage."),
             ("At the very first, gentle stage", "बाढतरम् is the last stage here, not the first."),
             ("After the placenta has come out", "The stage lasts until delivery, not after it.")],
            "Strongly at the exit, more strongly at the mouth of the yoni, until delivery.",
            "योनिमुखप्रतिपत्तौ = बाढतरम्."),
        order(1, "Put the printed words of unit 70 in the line's order.",
              ["निर्गमे", "बाढं", "गर्भस्य", "योनिमुखप्रतिपत्तौ", "बाढतरम्", "आप्रसवादिति"],
              "At the exit, strongly, of the fetus; on arrival at the mouth of the yoni, more strongly, until delivery: thus.",
              "निर्गमे → बाढं → गर्भस्य → योनिमुखप्रतिपत्तौ → बाढतरम् → आप्रसवादिति."),
        match(2, "Match each word of unit 70 to its meaning.",
              [["निर्गमे", "at the exit"], ["बाढम्", "strongly"], ["प्रतिपत्तौ", "on arrival"],
               ["बाढतरम्", "more strongly"], ["आ प्रसवात्", "until delivery"]],
              "The two stages and how long the second lasts.",
              "निर्गमे, बाढम्, प्रतिपत्तौ, बाढतरम्, आ प्रसवात्.", role="extend",
              teaches="The suffix -तर makes a comparative: बाढम् strongly, बाढतरम् more strongly."),
        mcq("discriminate", 3, "In unit 70, what does the suffix -तर in बाढतरम् add?",
            ("More: more strongly", "-तर is the comparative suffix."),
            [("Most: the strongest of all", "Most would be -तम: बाढतमम्."),
             ("Less: rather more gently", "-तर raises the degree; it does not lower it."),
             ("Again: once more, strongly", "Repetition is not the sense of -तर.")],
            "बाढतरम् = more strongly than बाढम्.",
            "-तर = comparative (more)."),
        mcq("apply", 4, "The fetus has reached the mouth of the yoni. By unit 70, how should she bear down?",
            ("More strongly, until delivery", "योनिमुखप्रतिपत्तौ बाढतरम् आ प्रसवात्."),
            [("Gently, gently, as at first", "Gentle bearing down belongs to the first stage, not this one."),
             ("Not at all, by holding back", "Unit 70 names only stronger bearing down."),
             ("Strongly, then stop and rest", "The line says until delivery, with no pause.")],
            "At the mouth of the yoni the bearing down is stronger still, until the birth.",
            "योनिमुख → बाढतरम्, आ प्रसवात्."),
        mcq("transfer", 5, "Built like बाढतरम् from बाढम्, which word says more slowly from मन्दम् (slowly)?",
            ("मन्दतरम्", "-तर makes the comparative: more slowly."),
            [("मन्दतमम्", "-तम makes the superlative: most slowly."),
             ("अतिमन्दम्", "अति- means very or too, not the comparative."),
             ("मन्दम्", "Plain slowly, without the comparative.")],
            "मन्दम् → मन्दतरम्, like बाढम् → बाढतरम्.",
            "-तर = more.",
            teaches="-तर forms the comparative: बाढम् → बाढतरम्, मन्दम् → मन्दतरम्."),
    ],
}

# ---------------------------------------------------------------- unit 71
AUTHORED["71"] = {
    "title": "तस्यास्तु प्रवाहमानायाः",
    "question": "By unit 71, what cry is raised while she is bearing down?",
    "rule": ("While that woman is bearing down, they should raise the cry: प्रजाता प्रजाता, धन्यं धन्यं पुत्रम्, "
             "she has given birth, she has given birth, to a blessed, blessed son! इति closes the cry."),
    "limits": ("Prose. Who raises the cry (they) is not stated. The genitives तस्याः ... स्त्रियाः are taken as for or over "
               "that woman; the exact relation is loose: no question on it. धन्य may also be fortunate."),
    "explain_hi": ("जब वह स्त्री प्रवाहण कर रही हो (प्रवाहमानायाः, वर्तमान कृदन्त), तब वे यह शब्द करें: "
                   "‘जन्म दे दिया, जन्म दे दिया, धन्य, धन्य पुत्र को!’ "
                   "यानी जन्म से पहले ही, जोर लगाते समय, यह घोषणा की जाती है। "
                   "‘कुर्युः’ विधिलिङ् प्रथम पुरुष बहुवचन है: वे करें; कौन, यह नहीं लिखा। "
                   "षष्ठी ‘तस्याः स्त्रियाः’ का ठीक सम्बन्ध ढीला है (उसके लिए / उस पर)।"),
    "hook": "जोर लगाते समय ही पुकार: प्रजाता! धन्य पुत्र!",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 71, what cry should they raise while she bears down?",
            ("She has given birth: a blessed son!", "प्रजाता प्रजाता धन्यं धन्यं पुत्रम् इति."),
            [("Push harder, the child is near now!", "No such words are in unit 71."),
             ("Hold back, it is not yet the time!", "The cry announces a birth; it gives no order."),
             ("A daughter is born to you today!", "The cry names a son (पुत्रम्).")],
            "The cry announces a birth and a blessed son.",
            "प्रजाता = she has given birth."),
        order(1, "Put the parts of unit 71 in the line's order.",
              ["तस्यास्तु", "प्रवाहमानायाः", "स्त्रियाः", "शब्दं कुर्युः", "प्रजाता प्रजाता", "धन्यंधन्यं पुत्रमिति"],
              "Of that woman, bearing down, they should make the cry: she has given birth, twice; a blessed, blessed son.",
              "तस्यास्तु → प्रवाहमानायाः → स्त्रियाः → शब्दं कुर्युः → प्रजाता प्रजाता → धन्यंधन्यं पुत्रमिति."),
        match(2, "Match each word of unit 71 to its meaning.",
              [["प्रवाहमानायाः", "bearing down"], ["शब्दम्", "cry"], ["कुर्युः", "they should make"],
               ["प्रजाता", "she has given birth"], ["धन्यम्", "blessed"]],
              "When, what is done, and the words of the cry.",
              "प्रवाहमानायाः, शब्दम्, कुर्युः, प्रजाता, धन्यम्.", role="extend",
              teaches="कुर्युः is the 3rd person plural optative of √कृ: they should make."),
        mcq("discriminate", 3, "Why is तस्याः written तस्यास् before तु in unit 71?",
            ("A visarga before त becomes स्", "तस्याः + तु → तस्यास्तु."),
            [("A visarga before त becomes श्", "श् comes before च, छ or श, not before त."),
             ("A visarga before त becomes र्", "र् never comes before an unvoiced त."),
             ("The word itself ends in स्", "The word is तस्याः, with a visarga.")],
            "तस्याः (of that woman) + तु (but) = तस्यास्तु.",
            "Visarga + त → स्त."),
        mcq("apply", 4, "By unit 71, at what time is the cry raised?",
            ("While she is bearing down", "प्रवाहमानायाः is a present participle: while she bears down."),
            [("After the placenta has come out", "The placenta is not named in unit 71."),
             ("Once the son has been seen", "The cry is raised during bearing down."),
             ("Before the pains have begun", "The participle says she is bearing down now.")],
            "The present participle places the cry in the time of bearing down.",
            "प्रवाहमाना = (she) who is bearing down."),
        mcq("transfer", 5, "Built like कुर्युः (they should make), which form of √कृ says he should make?",
            ("कुर्यात्", "3rd person singular optative."),
            [("कुर्याम्", "1st person singular: I should make."),
             ("कुर्याः", "2nd person singular: you should make."),
             ("कुर्वन्ति", "Present indicative: they make.")],
            "कुर्यात् = he should make; कुर्युः = they should make.",
            "Optative: कुर्यात् (he), कुर्युः (they).",
            teaches="The optative of √कृ: कुर्यात् he should make, कुर्युः they should make."),
    ],
}

# ---------------------------------------------------------------- unit 72
AUTHORED["72"] = {
    "title": "तथाऽस्या हर्षेण",
    "question": "By unit 72, what nourishes her vital breaths?",
    "rule": ("तथा अस्याः हर्षेण प्राणाः आप्याय्यन्ते: thus her vital breaths (प्राण) are nourished by joy (हर्ष). "
             "आप्याय्यन्ते is a present passive."),
    "limits": ("Prose. That the cry of unit 71 causes the joy is how the data reads the link (appears); the line itself "
               "names only joy. आप्याय्यन्ते may also be refreshed. No medicine or other means is named."),
    "explain_hi": ("इस प्रकार (तथा) उसके (अस्याः) प्राण हर्ष से (हर्षेण) पुष्ट होते हैं (आप्याय्यन्ते)। "
                   "डेटा के अनुसार पिछली इकाई की पुकार ही इस हर्ष का कारण प्रतीत होती है; पंक्ति स्वयं केवल हर्ष कहती है। "
                   "‘आप्याय्यन्ते’ कर्मवाच्य वर्तमान प्रथम पुरुष बहुवचन है: पुष्ट किए जाते हैं, ताज़ा होते हैं। "
                   "‘अस्याः’ स्त्रीलिंग है: स्त्री के प्राण।"),
    "hook": "हर्षेण प्राणाः: खुशी से प्राण भरते हैं।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 72, by what are her vital breaths (प्राण) nourished?",
            ("By joy (हर्षेण)", "हर्षेण प्राणा आप्याय्यन्ते: nourished by joy."),
            [("By food and drink", "No food is named in unit 72."),
             ("By a mantra in her ear", "The mantra is earlier (unit 58), not here."),
             ("By rest after birth", "No rest is named in unit 72.")],
            "Joy nourishes her vital breaths.",
            "हर्षेण = by joy."),
        order(1, "Put the printed words of unit 72 in the line's order.",
              ["तथाऽस्या", "हर्षेण", "प्राणा", "आप्याय्यंते"],
              "Thus her, by joy, vital breaths, are nourished.",
              "तथाऽस्या → हर्षेण → प्राणा → आप्याय्यंते."),
        match(2, "Match each word of unit 72 to its meaning.",
              [["अस्याः", "her"], ["हर्षेण", "by joy"], ["प्राणाः", "vital breaths"], ["आप्याय्यन्ते", "are nourished"]],
              "Whose, by what, what, and what happens.",
              "अस्याः, हर्षेण, प्राणाः, आप्याय्यन्ते.", role="extend",
              teaches="आप्याय्यन्ते is a present passive, 3rd plural: (they) are nourished; the agent हर्ष stands in the instrumental."),
        mcq("discriminate", 3, "Which split of तथाऽस्या हर्षेण is right?",
            ("तथा + अस्याः + हर्षेण", "आ + अ → आ (ऽ); आः drops its visarga before the voiced ह."),
            [("तथा + अस्य + हर्षेण", "अस्य would print short: तथास्य हर्षेण."),
             ("तथे + अस्याः + हर्षेण", "ए + अ would print तथेऽस्या."),
             ("तथः + अस्याः + हर्षेण", "अः + अ would print तथोऽस्या.")],
            "तथा (thus) + अस्याः (her) + हर्षेण (by joy).",
            "आ + अ → आ; आः + voiced sound → आ."),
        multi("apply", 4, "Which statements about unit 72 are right?",
              [("Joy nourishes her vital breaths", "Right: हर्षेण प्राणा आप्याय्यन्ते."),
               ("The child's breaths are meant here", "अस्याः is feminine: her breaths."),
               ("The verb is passive: are nourished", "Right: आप्याय्यन्ते, present passive."),
               ("A medicine for strength is named", "No medicine is named in unit 72.")],
              [0, 2],
              "Her vital breaths are nourished by joy; the verb is passive.",
              "अस्याः (f.) प्राणाः हर्षेण आप्याय्यन्ते."),
        mcq("transfer", 5, "By the rule of प्राणा आप्याय्यन्ते, how is देवाः + आगच्छन्ति (the gods come) written?",
            ("देवा आगच्छन्ति", "आः drops its visarga before a vowel, and no further join is made."),
            [("देवागच्छन्ति", "After the visarga drops, the two vowels are not joined again."),
             ("देवो आगच्छन्ति", "ओ comes from अः, not from आः."),
             ("देवारागच्छन्ति", "र् comes after vowels other than अ and आ.")],
            "देवाः + आगच्छन्ति = देवा आगच्छन्ति, like प्राणाः + आप्याय्यन्ते.",
            "आः + vowel → आ, with a gap.",
            teaches="A visarga after आ drops before a vowel and the words stay apart: प्राणाः + आप्याय्यन्ते → प्राणा आप्याय्यन्ते."),
    ],
}

# ---------------------------------------------------------------- unit 73
AUTHORED["73"] = {
    "title": "गर्भसंगे तु योनिं धूपयेत्",
    "question": "By unit 73, with what is the yoni fumigated in garbha-saṅga?",
    "rule": ("In garbha-saṅga (retention of the fetus) one should fumigate (धूपयेत्) the yoni with the sloughed skin of a "
             "black snake, or (वा) with piṇḍītaka."),
    "limits": ("Prose. Garbha-saṅga = obstructed labour is a probable reading, not stated. The snake's species is not "
               "stated. piṇḍītaka = emetic nut (Randia dumetorum) is probable, not certain. No dose or effect is given."),
    "explain_hi": ("गर्भसंग यानी गर्भ के अटकने (सम्भवतः रुका हुआ प्रसव, सम्भावित अर्थ) में योनि को धूप दे (धूपयेत्)। "
                   "धूपन के दो विकल्प: काले साँप की केंचुली (कृष्णसर्प-निर्मोक) या पिण्डीतक; ‘वा’ = या। "
                   "पिण्डीतक को मैनफल (Randia dumetorum) मानना सम्भावित है, निश्चित नहीं; साँप की जाति नहीं बताई गई। "
                   "‘निर्मोकेन’ और ‘पिण्डीतकेन’ तृतीया हैं: किससे धूप दे। कोई मात्रा या फल नहीं कहा गया।"),
    "hook": "गर्भ अटके तो धूपन: केंचुली या पिण्डीतक।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 73, what is to be done to the yoni in garbha-saṅga?",
            ("It is to be fumigated", "योनिं धूपयेत्: one should fumigate the yoni."),
            [("It is to be anointed", "Anointing is not the act of unit 73."),
             ("It is to be washed", "No washing is named in unit 73."),
             ("It is to be stretched", "Stretching is not the act of unit 73.")],
            "In garbha-saṅga the yoni is fumigated.",
            "धूपयेत् = should fumigate."),
        order(1, "Put the printed words of unit 73 in the line's order.",
              ["गर्भसंगे", "तु", "योनिं", "धूपयेत्", "कृष्णसर्पनिर्मोकेन", "पिंडीतकेन वा"],
              "In garbha-saṅga, however, the yoni, one should fumigate, with black-snake slough, or with piṇḍītaka.",
              "गर्भसंगे → तु → योनिं → धूपयेत् → कृष्णसर्पनिर्मोकेन → पिंडीतकेन वा."),
        match(2, "Match each word of unit 73 to its meaning.",
              [["गर्भसङ्गे", "in retention of the fetus"], ["धूपयेत्", "should fumigate"], ["निर्मोक", "sloughed skin"],
               ["पिण्डीतक", "probably emetic nut (probable)"], ["वा", "or"]],
              "The condition, the act and the two fumigants.",
              "गर्भसङ्गे, धूपयेत्, निर्मोक, पिण्डीतक, वा.", role="extend",
              teaches="वा (or) offers piṇḍītaka as an alternative to the snake slough."),
        mcq("discriminate", 3, "Which statement about piṇḍītaka in unit 73 is right?",
            ("Probably emetic nut; not certain", "The data labels the identification probable."),
            [("Certainly emetic nut; standard", "The data does not call it standard."),
             ("The skin a snake has sloughed", "That is निर्मोक, the other fumigant."),
             ("Unidentified; no candidate given", "The data gives a probable candidate.")],
            "piṇḍītaka = probably emetic nut (Randia dumetorum), labelled probable.",
            "पिण्डीतक: probable identification."),
        mcq("apply", 4, "In garbha-saṅga no snake slough is at hand. What does unit 73 allow instead?",
            ("Fumigating with piṇḍītaka", "निर्मोकेन पिण्डीतकेन वा: the two are alternatives."),
            [("Fumigating with nothing at all", "The line names a fumigant for each case."),
             ("Waiting until slough is found", "वा offers piṇḍītaka as the other choice."),
             ("Using any smoke one likes", "Only the two named things are given.")],
            "वा (or) makes piṇḍītaka an alternative to the slough.",
            "X-ena Y-ena वा = with X or with Y."),
        mcq("transfer", 5, "Built like निर्मोकेण (with the slough), which form of घृत (ghee, n.) says with ghee?",
            ("घृतेन", "Instrumental singular: the means, with ghee."),
            [("घृतम्", "Nominative or accusative: ghee itself."),
             ("घृताय", "Dative: for ghee."),
             ("घृतस्य", "Genitive: of ghee.")],
            "घृतेन = with ghee, like निर्मोकेण, with the slough.",
            "Instrumental -एन/-एण = with (means).",
            teaches="The instrumental names the means of the act: निर्मोकेण धूपयेत्, fumigate with the slough."),
    ],
}

# ---------------------------------------------------------------- unit 74
AUTHORED["74"] = {
    "title": "बध्नीयाच्च हिरण्यपुष्पीमूलं",
    "question": "By unit 74, what is tied, and where?",
    "rule": ("बध्नीयात् च: and one should tie the root (मूलम्) of hiraṇyapuṣpī on the hand and foot (हस्तपादे)."),
    "limits": ("Prose. hiraṇyapuṣpī (literally golden-flowered) is unidentified: no question on its identity. Whose hand and "
               "foot, and whether both sides, is not said. The garbha-saṅga condition of unit 73 appears to carry on; it is "
               "not repeated here."),
    "explain_hi": ("और हिरण्यपुष्पी की जड़ (मूल) हाथ और पैर में बाँधे (बध्नीयात्)। "
                   "हिरण्यपुष्पी (शब्दशः ‘सुनहरे फूल वाली’) की पहचान अज्ञात है; स्रोत अलग-अलग हैं, इसलिए कोई पहचान नहीं दी गई। "
                   "‘हस्तपादे’ समाहार द्वन्द्व है: हाथ-पैर, एक समूह के रूप में एकवचन; किसके और किस ओर के, नहीं कहा। "
                   "पिछली इकाई की गर्भसंग वाली शर्त यहाँ चलती प्रतीत होती है, दोहराई नहीं गई।"),
    "hook": "हिरण्यपुष्पी की जड़: हाथ-पैर पर बाँधो।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 74, which part of hiraṇyapuṣpī is to be tied?",
            ("The root (मूल)", "हिरण्यपुष्पीमूलम्: the root of hiraṇyapuṣpī."),
            [("The flower (पुष्प)", "पुष्पी is in the plant's name; the part tied is मूल."),
             ("The leaf (पत्र)", "No leaf is named in unit 74."),
             ("The bark (त्वक्)", "No bark is named in unit 74.")],
            "The root is tied on the hand and foot.",
            "मूलम् = root."),
        order(1, "Put the words of unit 74 in the line's order.",
              ["बध्नीयात्", "च", "हिरण्यपुष्पीमूलम्", "हस्तपादे"],
              "One should tie, and, the root of hiraṇyapuṣpī, on the hand and foot.",
              "बध्नीयात् → च → हिरण्यपुष्पीमूलम् → हस्तपादे."),
        match(2, "Match each word of unit 74 to its meaning.",
              [["बध्नीयात्", "one should tie"], ["च", "and"], ["मूलम्", "root"], ["हस्तपादे", "on the hand and foot"]],
              "The act, the thing and the place.",
              "बध्नीयात्, च, मूलम्, हस्तपादे.", role="extend",
              teaches="हस्तपादे is a collective (samāhāra) dvandva: hand-and-foot as one group, neuter singular, here locative."),
        mcq("discriminate", 3, "Which split of बध्नीयाच्च is right?",
            ("बध्नीयात् + च", "त् + च → च्च."),
            [("बध्नीयाः + च", "A visarga before च would print बध्नीयाश्च."),
             ("बध्नीयाम् + च", "म् before च would print बध्नीयाञ्च or बध्नीयांच."),
             ("बध्नीया + च्च", "च्च is not a word; the particle is च.")],
            "बध्नीयात् (one should tie) + च (and).",
            "त् + च → च्च."),
        mcq("apply", 4, "By unit 74, where is the root tied?",
            ("On the hand and foot", "हस्तपादे: on the hand and foot (whose is not said)."),
            [("Round the waist only", "No waist is named in unit 74."),
             ("Round her neck", "No neck is named in unit 74."),
             ("Into the braided hair", "No hair is named in unit 74.")],
            "The place is हस्तपादे, the hand and foot.",
            "हस्तपादे = on the hand and foot."),
        mcq("transfer", 5, "By the rule of बध्नीयाच्च, how is पिबेत् + च (and one should drink) joined?",
            ("पिबेच्च", "त् before च becomes च्: पिबेत् + च → पिबेच्च."),
            [("पिबेद्च", "द् comes before voiced sounds; च is not voiced."),
             ("पिबेश्च", "श् comes from a visarga before च, not from त्."),
             ("पिबेत्च", "त् does not stay unchanged before च.")],
            "पिबेत् + च = पिबेच्च, like बध्नीयात् + च = बध्नीयाच्च.",
            "त् + च → च्च.",
            teaches="A final त् becomes च् before च: बध्नीयात् + च → बध्नीयाच्च."),
    ],
}

# ---------------------------------------------------------------- unit 75
AUTHORED["75"] = {
    "title": "धारयेच्च सुवर्चलां",
    "question": "By unit 75, what should be held, and how sure are the plant names?",
    "rule": ("धारयेत् च: and one should hold suvarcalā (identity disputed) or (वा) viśalyā (probably the same as lāṅgalī)."),
    "limits": ("Prose. suvarcalā is disputed (candidates include Cleome gynandra and others); viśalyā = lāṅgalī (Gloriosa "
               "superba) is probable. Where or how it is held is not said. It appears to continue unit 74 (the data's "
               "GROUPING note); no question on that."),
    "explain_hi": ("और सुवर्चला या विशल्या धारण करे (धारयेत्)। "
                   "सुवर्चला की पहचान विवादित है (Cleome gynandra आदि कई उम्मीदवार); विशल्या सम्भवतः लाङ्गली यानी कलिहारी "
                   "(Gloriosa superba) है, यह सम्भावित पहचान है। "
                   "‘सुवर्चलाम्’ और ‘विशल्याम्’ द्वितीया हैं: जिन्हें धारण करना है; ‘वा’ = या। "
                   "कैसे या कहाँ धारण करे, यह नहीं लिखा।"),
    "hook": "धारयेत्: सुवर्चला (विवादित) या विशल्या (सम्भावित लाङ्गली)।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 75, what should be done with suvarcalā or viśalyā?",
            ("It should be held (धारयेत्)", "धारयेत्: one should hold."),
            [("It should be burnt as smoke", "Fumigation is the act of unit 73."),
             ("It should be ground to paste", "No paste is named in unit 75."),
             ("It should be drunk in milk", "No drink is named in unit 75.")],
            "The plant is to be held.",
            "धारयेत् = should hold."),
        order(1, "Put the words of unit 75 in the line's order.",
              ["धारयेत्", "च", "सुवर्चलाम्", "विशल्याम्", "वा"],
              "One should hold, and, suvarcalā, viśalyā, or.",
              "धारयेत् → च → सुवर्चलाम् → विशल्याम् → वा."),
        match(2, "Match each word of unit 75 to what the card says of it.",
              [["धारयेत्", "one should hold"], ["सुवर्चला", "identity disputed"],
               ["विशल्या", "probably lāṅgalī (probable)"], ["वा", "or"]],
              "The act, the two plants with their labels, and the choice.",
              "धारयेत्, सुवर्चला, विशल्या, वा.", role="extend",
              teaches="Plant names keep the data's label: suvarcalā disputed, viśalyā probable (= lāṅgalī)."),
        mcq("discriminate", 3, "In unit 75, why do सुवर्चलाम् and विशल्याम् end in -आम्?",
            ("Accusative: they are what is held", "Feminine accusative singular, the object of धारयेत्."),
            [("Locative: the holding is in them", "The feminine locative would be -आयाम्."),
             ("Genitive: they are of the woman", "The feminine genitive would be -आयाः."),
             ("Nominative: they do the holding", "The nominative would be -आ.")],
            "Both are objects of धारयेत्: f. acc. sg.",
            "-आम् (f.) = accusative singular."),
        mcq("apply", 4, "A student says: viśalyā in unit 75 is certainly lāṅgalī. What should the card answer?",
            ("Probably so: the label is probable", "The data tags viśalyā = lāṅgalī as probable."),
            [("Yes: the identity is a standard one", "The data does not call it standard."),
             ("No: viśalyā is the same as suvarcalā", "They are two plants joined by वा (or)."),
             ("No: viśalyā is left unidentified", "The data gives lāṅgalī as probable.")],
            "viśalyā is probably lāṅgalī (Gloriosa superba); the card keeps the label probable.",
            "विशल्या = लाङ्गली (probable)."),
        mcq("transfer", 5, "Built like सुवर्चलाम् (object), what is the object form of माला (garland, f.)?",
            ("मालाम्", "Feminine accusative singular in -आम्."),
            [("माला", "Nominative: the garland as subject."),
             ("मालायाम्", "Locative: in or on the garland."),
             ("मालायाः", "Genitive or ablative: of or from the garland.")],
            "मालाम् धारयेत् = one should hold (wear) the garland, like सुवर्चलाम्.",
            "आ-stem f. accusative = -आम्.",
            teaches="A feminine noun in -आ takes -आम् as the object: सुवर्चला → सुवर्चलाम्, माला → मालाम्."),
    ],
}

# ---------------------------------------------------------------- unit 76
AUTHORED["76"] = {
    "title": "अथ प्रसूताया न चेदपरा पतति",
    "question": "By unit 76, what is done if the placenta does not fall after delivery?",
    "rule": ("If the aparā (placenta) of one who has delivered does not fall, then, pressing firmly with the right hand "
             "from above the navel and gripping from behind, one should shake (विधूनुयात्)."),
    "limits": ("Prose. The object of gripping and shaking is not stated (not even the abdomen), and who acts is not said. "
               "उपरिष्ठात् is printed with ष्ठ and read उपरिष्टात् (a possible misprint). No force or time is given."),
    "explain_hi": ("अब, यदि प्रसव कर चुकी स्त्री का अपरा (जेर) नहीं गिरता, तो उपाय: "
                   "दाहिने हाथ से (दक्षिणेन पाणिना) नाभि के ऊपर से (नाभेः उपरिष्टात्) जोर से दबाकर (बलवत् उपपीड्य), "
                   "पीछे से पकड़कर (पृष्ठतः उपसङ्गृह्य) हिलाए (विधूनुयात्)। "
                   "किसे पकड़े और हिलाए, यह नहीं लिखा, इसलिए कुछ जोड़ा नहीं गया। "
                   "‘उपपीड्य’, ‘उपसङ्गृह्य’ उपसर्ग वाले ल्यबन्त हैं: -य = ‘करके’।"),
    "hook": "जेर न गिरे: दाहिना हाथ, नाभि के ऊपर दबाओ, पीछे से पकड़ो, हिलाओ।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 76, what problem is being treated?",
            ("The placenta not falling out", "न चेदपरा पतति: if the placenta does not fall."),
            [("The fetus not turning round", "Turning is not the problem of unit 76."),
             ("The pains not coming at all", "Pains are not named in unit 76."),
             ("The breast milk not flowing", "Milk is not named in unit 76.")],
            "The procedure is for a placenta that has not come out after delivery.",
            "अपरा = placenta; न पतति = does not fall."),
        order(1, "Put the steps of unit 76 in the line's order.",
              ["दक्षिणेन पाणिना", "नाभेरुपरिष्ठात्", "बलवदुपपीड्य", "पृष्ठत उपसंगृह्य", "विधूनुयात्"],
              "With the right hand, from above the navel, pressing firmly, gripping from behind, one should shake.",
              "दक्षिणेन पाणिना → नाभेरुपरिष्ठात् → बलवदुपपीड्य → पृष्ठत उपसंगृह्य → विधूनुयात्."),
        match(2, "Match each word of unit 76 to its meaning.",
              [["अपरा", "placenta"], ["दक्षिणेन पाणिना", "with the right hand"], ["नाभेः", "of the navel"],
               ["उपपीड्य", "having pressed"], ["विधूनुयात्", "should shake"]],
              "The problem, the hand, the place and the two acts.",
              "अपरा, दक्षिणेन पाणिना, नाभेः, उपपीड्य, विधूनुयात्.", role="extend",
              teaches="उपपीड्य and उपसङ्गृह्य are absolutives with a prefix (-य): having pressed, having gripped."),
        mcq("discriminate", 3, "Why do उपपीड्य and उपसङ्गृह्य end in -य, not -त्वा?",
            ("With a prefix, -य replaces -त्वा", "उप- and उप-सम्- are prefixes, so -य, not -त्वा."),
            [("-य marks an action still to come", "-य marks an action done before the main verb."),
             ("-य turns the verb into a command", "The command is the optative विधूनुयात्."),
             ("-य marks the passive voice here", "These are absolutives, not passives.")],
            "Prefixed verbs form the absolutive in -य: उपपीड्य, having pressed.",
            "Absolutive: -त्वा without a prefix, -य with one."),
        mcq("apply", 4, "The placenta has already come out after the birth. Does unit 76's procedure apply?",
            ("No: only if it has not fallen", "न चेदपरा पतति: only if the placenta does not fall."),
            [("Yes: it is done after every birth", "The line sets a condition with चेत् (if)."),
             ("Yes: it hastens the next delivery", "No next delivery is named in unit 76."),
             ("No: it is only for a fetus not turning", "Turning is not the condition of unit 76.")],
            "The condition is न चेत् ... पतति: if it does not fall.",
            "चेत् = if; the procedure applies only then."),
        mcq("transfer", 5, "By the rule of नाभेरुपरिष्टात्, how is हरेः + आज्ञा (Hari's command) joined?",
            ("हरेराज्ञा", "A visarga after ए becomes र् before a vowel, as नाभेः + उपरिष्टात्."),
            [("हरे आज्ञा", "The visarga drops before a vowel only after अ or आ."),
             ("हरेसाज्ञा", "A visarga does not become स् before a vowel."),
             ("हरोऽज्ञा", "ओऽ comes from अः + अ, not from एः.")],
            "हरेः + आज्ञा = हरेराज्ञा, like नाभेः + उपरिष्टात् = नाभेरुपरिष्टात्.",
            "Visarga after ए + vowel → र्.",
            teaches="A visarga after a vowel other than अ or आ becomes र् before a vowel: नाभेः + उपरिष्टात् → नाभेरुपरिष्टात्."),
    ],
}

# ---------------------------------------------------------------- unit 77
AUTHORED["77"] = {
    "title": "पाष्ण्यां वा श्रोणिमाकुट्टयेत्",
    "question": "By unit 77, what other measure is given, and on which part?",
    "rule": ("वा: or one should strike (आकुट्टयेत्) the hip (श्रोणि) with the heel. आकुट्टयेत् is an optative: an "
             "instruction."),
    "limits": ("Prose. The printed पाष्ण्यां is read as पाष्ण्या, with the heel (a possible correction; a locative would be "
               "on the heel): no question on it. Whose heel is not said; श्रोणि may also be the buttock. The condition "
               "of unit 76 appears to carry on."),
    "explain_hi": ("या (वा) एड़ी से श्रोणि यानी कूल्हे पर प्रहार करे (आकुट्टयेत्)। "
                   "छपा ‘पाष्ण्यां’ सप्तमी (एड़ी पर) जैसा दिखता है; ‘पाष्ण्या’ (एड़ी से, तृतीया) पढ़ना सम्भावित सुधार है, इसलिए इस पर प्रश्न नहीं। "
                   "किसकी एड़ी, यह नहीं कहा; श्रोणि का अर्थ कूल्हा/श्रोणि-प्रदेश है, नितम्ब भी हो सकता है। "
                   "पिछली इकाई की शर्त (अपरा न गिरे) यहाँ चलती प्रतीत होती है, दोहराई नहीं गई।"),
    "hook": "या फिर: श्रोणि पर एड़ी से आघात।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 77, which part of the body is struck?",
            ("The hip (श्रोणि)", "श्रोणिम् आकुट्टयेत्: one should strike the hip."),
            [("The navel (नाभि)", "The navel is named in unit 76, not struck here."),
             ("The back (पृष्ठ)", "No back is named in unit 77."),
             ("The head (शिरस्)", "No head is named in unit 77.")],
            "The hip region is struck.",
            "श्रोणि = hip (pelvic region)."),
        order(1, "Put the words of unit 77 in the line's order.",
              ["पाष्ण्यां", "वा", "श्रोणिम्", "आकुट्टयेत्"],
              "With the heel (printed form), or, the hip, one should strike.",
              "पाष्ण्यां → वा → श्रोणिम् → आकुट्टयेत्."),
        match(2, "Match each sure word of unit 77 to its meaning.",
              [["वा", "or"], ["श्रोणिम्", "the hip"], ["आकुट्टयेत्", "one should strike"]],
              "The choice, the place and the act.",
              "वा, श्रोणिम्, आकुट्टयेत्.", role="extend",
              teaches="आकुट्टयेत् is a 3rd singular optative of आ-√कुट्ट: one should strike."),
        mcq("discriminate", 3, "Which split of श्रोणिमाकुट्टयेत् is right?",
            ("श्रोणिम् + आकुट्टयेत्", "A final म् before a vowel joins it: श्रोणिमा..."),
            [("श्रोणीम् + आकुट्टयेत्", "That would print श्रोणीमा... with long ई."),
             ("श्रोणिः + आकुट्टयेत्", "Visarga after इ before a vowel would print श्रोणिरा..."),
             ("श्रोणिम् + अकुट्टयेत्", "That would print श्रोणिमकु... with short अ.")],
            "श्रोणिम् (the hip) + आकुट्टयेत् (one should strike).",
            "Final म् + vowel → म + vowel."),
        mcq("apply", 4, "What kind of statement does the optative आकुट्टयेत् make unit 77?",
            ("A rule: one should strike", "The optative gives the rule of what to do."),
            [("A past report: one struck", "A past tense would be needed for that."),
             ("A prohibition: do not strike", "No मा or न stands in unit 77."),
             ("A forecast: one will strike", "A future tense would be needed for that.")],
            "Like the other lines of this procedure, unit 77 instructs with an optative.",
            "Optative -एत् = one should."),
        mcq("transfer", 5, "By the rule of श्रोणिमाकुट्टयेत्, how is जलम् + आनयेत् (one should bring water) joined?",
            ("जलमानयेत्", "A final म् before a vowel joins it: जलम् + आनयेत्."),
            [("जलोऽनयेत्", "ओऽ comes from अः + अ, not from अम्."),
             ("जलानयेत्", "The म् is not dropped before a vowel."),
             ("जलमनयेत्", "The आ of आनयेत् stays long.")],
            "जलम् + आनयेत् = जलमानयेत्, like श्रोणिम् + आकुट्टयेत्.",
            "Final म् + vowel → म + vowel.",
            teaches="A final म् before a vowel joins it: श्रोणिम् + आकुट्टयेत् → श्रोणिमाकुट्टयेत्."),
    ],
}


# ===================================================================== NOTES_HI
NOTES_HI = {
    "65": ("गद्य; विश्वास उच्च; कोई पाठ-चिह्न नहीं। ‘परा’ स्त्रीलिंग, अतः कोई दूसरी स्त्री। कर्म (किसे समझाए) अलिखित; "
           "डेटा के अनुसार निर्देश सम्भवतः छपी पंक्तियों ७२-७६ (इकाई ६६-७०) में आता है। "
           "सन्धि जाँची: परा + अनुशिष्यात् → परानुशिष्यात् (आ + अ → आ), छपाई में मिले अ का चिह्न ऽ: पराऽनुशिष्यात्।"),
    "66": ("गद्य; विश्वास मध्यम। पाठ-चिह्न: छपा ‘प्रैवाहिट्टाः’ कोई रूप नहीं; ‘मा’ + लुङ् ‘प्रवाहिष्ठाः’ (प्रवाहण मत करो) सम्भावित सुधार; "
           "छपी पंक्ति ७५ (इकाई ६९) में वही क्रिया ‘प्रबाहिष्टाः’ छपी है। व्याकरण पूरी तरह निश्चित नहीं, अर्थ अगली पंक्ति से स्पष्ट — "
           "रूप पर प्रश्न नहीं। वेदना = प्रसव-वेदना, सन्दर्भ से सम्भावित। "
           "सन्धि जाँची: अनागतायाम् + वेदनायाम् → अनागतायां वेदनायां (म् → अनुस्वार व्यञ्जन से पहले); अन् + आगता → अनागता।"),
    "67": ("गद्य; विश्वास मध्यम; कोई पाठ-चिह्न नहीं। क्रिया समझी जाती है। ‘गर्भस्य’ को ‘अहितम्’ के साथ लिया, हानियों की सूची के साथ भी "
           "सम्भव — इस पर प्रश्न नहीं। शोष = सूखकर घटना (सम्भावित; पुराने प्रयोग में कभी क्षय)। ‘अनर्थकरम्’ = निरर्थक, या हानिकर। "
           "छपा ‘अकालप्रवाहणंहि’ बिना अन्तराल। सन्धि जाँची: वेगानाम् + इव → वेगानामिव; इव + उदीरणम् → इवोदीरणम् (अ + उ → ओ); "
           "उदीरणम् + अनर्थकरम् + अहितम् → उदीरणमनर्थकरमहितम् (म् + स्वर); विट् + मूत्र → विण्मूत्र (ट् → ण् अनुनासिक म से पहले, जैसा छपा)।"),
    "68": ("गद्य; विश्वास मध्यम; कोई पाठ-चिह्न नहीं। ‘तेषाम्’ पिछली इकाई (छपी पंक्ति ७३) के वेगों की ओर संकेत करता है। "
           "क्रिया समझी जाती है; ‘उपघाताय’ प्रयोजन की चतुर्थी। कौन-सी हानि, नहीं कहा। "
           "सन्धि जाँची: तेषाम् + एव → तेषामेव; विधारणम् + इव → विधारणमिव; वेदनायाम् + अप्रवाहणम् → वेदनायामप्रवाहणम्; "
           "अप्रवाहणम् + उपघाताय → अप्रवाहणमुपघाताय (म् + स्वर)।"),
    "69": ("गद्य; विश्वास मध्यम। पाठ-चिह्न: छपा ‘प्रबाहिष्टाः’ = प्रवाहिष्ठाः (ब/व भ्रम, ह लुप्त; सम्भावित सुधार), छपी पंक्ति ७२ (इकाई ६६) "
           "वाली क्रिया — रूप पर प्रश्न नहीं। वर्गीकरण: पंक्ति ७५ और ७६ (इकाई ६९-७०) एक वाक्य प्रतीत होती हैं। "
           "सन्धि जाँची: ततः + यथोक्तम् → ततो यथोक्तम् (अः → ओ घोष य से पहले); यथा + उक्तम् → यथोक्तम् (आ + उ → ओ); "
           "शनैः + च → शनैश्च (विसर्ग → श् च से पहले); छपा ‘शनैः शनैः’ में श से पहले विसर्ग रखा गया है।"),
    "70": ("गद्य; विश्वास मध्यम; कोई पाठ-चिह्न नहीं। अध्याहार: क्रिया ‘प्रवाहिष्ठाः’ छपी पंक्ति ७५ (इकाई ६९) से आती है, यहाँ जोड़ी नहीं गई। "
           "‘गर्भस्य’ सम्भवतः दोनों (निर्गमे, प्रतिपत्तौ) से जुड़ता है। अन्त का ‘इति’ निर्देश समाप्त करता है। "
           "सन्धि जाँची: बाढम् + गर्भस्य → बाढं गर्भस्य; बाढतरम् + आप्रसवात् → बाढतरमाप्रसवात् (म् + स्वर); "
           "आप्रसवात् + इति → आप्रसवादिति (त् → द् स्वर से पहले)।"),
    "71": ("गद्य; विश्वास उच्च; कोई पाठ-चिह्न नहीं। ‘तस्याः … स्त्रियाः’ षष्ठी को ‘उस स्त्री के लिए/उस पर’ लिया; सम्बन्ध ढीला। "
           "‘कुर्युः’ का कर्ता (वे) अलिखित। ‘प्रजाता’ कर्तृ-अर्थ में: जन्म दे दिया। धन्य = धन्य या भाग्यशाली। छपा ‘धन्यंधन्यं’ बिना अन्तराल। "
           "सन्धि जाँची: तस्याः + तु → तस्यास्तु (विसर्ग → स् त से पहले); शब्दम् + कुर्युः → शब्दं कुर्युः; पुत्रम् + इति → पुत्रमिति; "
           "स से पहले विसर्ग (प्रवाहमानायाः स्त्रियाः) छपे अनुसार रखा।"),
    "72": ("गद्य; विश्वास उच्च; कोई पाठ-चिह्न नहीं। ‘आप्याय्यन्ते’ = पुष्ट/ताज़ा होते हैं। डेटा के अनुसार पिछली इकाई की पुकार इस हर्ष का "
           "कारण प्रतीत होती है — कहा नहीं गया। सन्धि जाँची: तथा + अस्याः → तथाऽस्याः (आ + अ → आ, ऽ चिह्न); "
           "अस्याः + हर्षेण → अस्या हर्षेण (आः → आ घोष से पहले); प्राणाः + आप्याय्यन्ते → प्राणा आप्याय्यन्ते (आः का विसर्ग स्वर से पहले लुप्त, "
           "आगे सन्धि नहीं); छपा ‘आप्याय्यंते’ में न् के स्थान पर अनुस्वार।"),
    "73": ("गद्य; विश्वास मध्यम; कोई पाठ-चिह्न नहीं। गर्भसंग = गर्भ का अटकना; ‘रुका हुआ प्रसव’ आधुनिक अर्थ सम्भावित। "
           "कृष्णसर्प = काला साँप, जाति नहीं बताई। पिण्डीतक = मदन/मैनफल (Randia dumetorum), सम्भावित, निश्चित नहीं। "
           "छपा ‘तुयोनिं’ बिना अन्तराल (तु योनिम्); ‘निर्मोकेन’ ण के स्थान पर न से छपा (वर्तनी, शुद्ध निर्मोकेण); ‘पिंडीतक’ = पिण्डीतक। "
           "सन्धि जाँची: योनिम् + धूपयेत् → योनिं धूपयेत् (म् → अनुस्वार व्यञ्जन से पहले)।"),
    "74": ("गद्य; विश्वास मध्यम; कोई पाठ-चिह्न नहीं। हिरण्यपुष्पी (शब्दशः सुनहरे फूल वाली) अज्ञात: स्रोतों में मतभेद, कोई सुरक्षित पहचान नहीं — "
           "पहचान पर प्रश्न नहीं। ‘हस्तपादे’ समाहार द्वन्द्व, एकवचन; किसके, किस ओर के, नहीं कहा। "
           "छपी पंक्ति ७९ (इकाई ७३) की गर्भसंग-शर्त यहाँ चलती प्रतीत होती है। "
           "सन्धि जाँची: बध्नीयात् + च → बध्नीयाच्च (त् + च → च्च); मूलम् + हस्तपादे → मूलं हस्तपादे।"),
    "75": ("गद्य; विश्वास मध्यम; कोई पाठ-चिह्न नहीं। वर्गीकरण: छपी पंक्ति ८० और ८१ (इकाई ७४-७५) एक-दूसरे को आगे बढ़ाती प्रतीत होती हैं। "
           "सुवर्चला विवादित (Cleome gynandra आदि उम्मीदवार); विशल्या = लाङ्गली (Gloriosa superba), सम्भावित। "
           "सन्धि जाँची: धारयेत् + च → धारयेच्च (त् + च → च्च); सुवर्चलाम् + विशल्याम् → सुवर्चलां विशल्याम्; विशल्याम् + वा → विशल्यां वा।"),
    "76": ("गद्य; विश्वास मध्यम। पाठ-चिह्न: ‘उपरिष्ठात्’ ष्ठ से छपा, उपरिष्टात् पढ़ा (सम्भावित छपाई-भूल)। ‘उपसङ्गृह्य’ और ‘विधूनुयात्’ का कर्म "
           "अलिखित, कुछ नहीं जोड़ा। अपरा = जेर/अपरा (मानक)। छपा ‘प्रसूतायान’ = प्रसूताया न; ‘बलवदुपपीड्यपृष्ठत’ बिना अन्तराल। "
           "सन्धि जाँची: प्रसूतायाः + न → प्रसूताया न (आः → आ घोष से पहले); चेत् + अपरा → चेदपरा (त् → द् स्वर से पहले); "
           "ततः + दक्षिणेन → ततो दक्षिणेन; नाभेः + उपरिष्टात् → नाभेरुपरिष्टात् (ए के बाद विसर्ग → र्); "
           "उपरिष्टात् + बलवत् → उपरिष्टाद्बलवत् (त् → द् घोष से पहले); बलवत् + उपपीड्य → बलवदुपपीड्य; "
           "पृष्ठतः + उपसङ्गृह्य → पृष्ठत उपसङ्गृह्य (अः → अ, अ-भिन्न स्वर से पहले, बीच में अन्तर)।"),
    "77": ("गद्य; विश्वास मध्यम। पाठ-चिह्न: छपा ‘पाष्ण्यां’; तृतीया ‘पाष्ण्या’ (एड़ी से) अपेक्षित, अनुस्वार भटका चिह्न लगता है "
           "(सप्तमी ‘पाष्ण्याम्’ = एड़ी पर) — सम्भावित सुधार, इस पर प्रश्न नहीं। कोश का सामान्य रूप ‘पार्ष्णि’ (र् सहित) है; छपाई में र् नहीं, "
           "डेटा इस पर कुछ नहीं कहता। श्रोणि = कूल्हा/श्रोणि-प्रदेश (या नितम्ब)। किसकी एड़ी, नहीं कहा। छपी पंक्ति ८२ (इकाई ७६) की शर्त "
           "यहाँ चलती प्रतीत होती है। सन्धि जाँची: श्रोणिम् + आकुट्टयेत् → श्रोणिमाकुट्टयेत् (म् + स्वर)।"),
}

# ===================================================================== AIDS
AIDS = {
    "65": {
        "chunks": "तथा | पराऽनुशिष्यात्",
        "frame": "तथा (वैसे ही) → कर्ता ‘परा’ (दूसरी स्त्री) → क्रिया ‘अनुशिष्यात्’ (समझाए); कर्म (किसे) अलिखित।",
        "sandhi": "आ + अ → आ: परा + अनुशिष्यात् → परानुशिष्यात् (छपा पराऽनुशिष्यात्, ऽ मिले अ का चिह्न)।",
    },
    "66": {
        "chunks": "अनागतायां वेदनायां | मा प्रैवाहिट्टाः (= प्रवाहिष्ठाः? सम्भावित)",
        "frame": "कब (अनागतायां वेदनायाम्: वेदना न आने पर) → निषेध (मा) → क्रिया (प्रवाहण, सम्भावित पाठ)।",
        "sandhi": "म् → अनुस्वार व्यञ्जन से पहले: अनागतायाम् + वेदनायाम् → अनागतायां वेदनायां · नञ् स्वर से पहले अन्: अन् + आगता → अनागता।",
        "anchors": "याद-सूत्र: ‘अन्-आगत’ = जो अभी आया नहीं; वेदना नहीं आई तो जोर नहीं। (मेरी याद-पद्धति)",
    },
    "67": {
        "chain": {"steps": ["असमय प्रवाहण", "मल-मूत्र आदि वेगों के उदीरण जैसा", "निरर्थक और अहितकर",
                            "१ श्वास", "२ कास", "३ शोष (सम्भावित: सूखकर घटना)", "४ कुब्जता", "आदि"]},
        "chunks": "अकालप्रवाहणं हि | विण्मूत्रादिवेगानामिवोदीरणम् | अनर्थकरमहितं च गर्भस्य | श्वासकासशोषकुब्जतादिकारित्वात्",
        "sandhi": "अ + उ → ओ: इव + उदीरणम् → इवोदीरणम् · म् + स्वर: उदीरणम् + अनर्थकरम् → उदीरणमनर्थकरम् · ट् → ण् म से पहले: विट् + मूत्र → विण्मूत्र।",
        "frame": "कर्ता (अकालप्रवाहणम्) → उपमा (वेगों का उदीरण इव) → विधेय (अनर्थकरम्, अहितम्) → कारण (-कारित्वात्)।",
    },
    "68": {
        "chain": {"steps": ["वेदना है", "फिर भी प्रवाहण न करना", "उन्हीं वेगों को रोकने (विधारण) जैसा", "उपघात (हानि) के लिए"]},
        "chunks": "तथा | तेषामेव विधारणमिव | वेदनायामप्रवाहणम् | उपघाताय",
        "sandhi": "म् + स्वर: तेषाम् + एव → तेषामेव, विधारणम् + इव → विधारणमिव, वेदनायाम् + अप्रवाहणम् → वेदनायामप्रवाहणम्, अप्रवाहणम् + उपघाताय → अप्रवाहणमुपघाताय।",
    },
    "69": {
        "chunks": "ततो यथोक्तं कुरुष्व | शनैः शनैश्च | पूर्वं प्रबाहिष्टाः (= प्रवाहिष्ठाः, सम्भावित)",
        "sandhi": "अः → ओ घोष से पहले: ततः + यथोक्तम् → ततो यथोक्तम् · आ + उ → ओ: यथा + उक्तम् → यथोक्तम् · विसर्ग → श् च से पहले: शनैः + च → शनैश्च।",
        "frame": "कब (ततः) → कैसे (यथोक्तम्) → आज्ञा (कुरुष्व) → कैसे (शनैः शनैः) → कब (पूर्वम्) → क्रिया (प्रवाहण)।",
    },
    "70": {
        "chain": {"steps": ["गर्भ के निकलने पर: जोर से (बाढम्)", "योनि-मुख पहुँचने पर: और जोर से (बाढतरम्)", "प्रसव तक (आ प्रसवात्)"]},
        "chunks": "निर्गमे बाढं गर्भस्य | योनिमुखप्रतिपत्तौ बाढतरम् | आप्रसवादिति",
        "sandhi": "म् + स्वर: बाढतरम् + आप्रसवात् → बाढतरमाप्रसवात् · त् → द् स्वर से पहले: आप्रसवात् + इति → आप्रसवादिति।",
        "letters": "बाढम् → बाढ-तर-म्: ‘तर’ जुड़ा तो ‘और अधिक’। (केवल सुनने की सहायता)",
    },
    "71": {
        "chunks": "तस्यास्तु प्रवाहमानायाः स्त्रियाः | शब्दं कुर्युः | प्रजाता प्रजाता | धन्यंधन्यं पुत्रमिति",
        "sandhi": "विसर्ग → स् त से पहले: तस्याः + तु → तस्यास्तु · म् → अनुस्वार व्यञ्जन से पहले: शब्दम् + कुर्युः → शब्दं कुर्युः · म् + स्वर: पुत्रम् + इति → पुत्रमिति।",
        "frame": "कब (प्रवाहमानायाः: जोर लगाते समय) → क्या (शब्दं कुर्युः) → पुकार के शब्द (प्रजाता प्रजाता … पुत्रम्) → इति।",
        "story": "मेरा बनाया चित्र: स्त्री जोर लगा रही है, पास की स्त्रियाँ पहले से ही पुकारती हैं ‘प्रजाता! धन्य पुत्र!’ (केवल याद के लिए, श्लोक का दावा नहीं)",
    },
    "72": {
        "chunks": "तथाऽस्या | हर्षेण | प्राणा | आप्याय्यंते",
        "sandhi": "आ + अ → आ: तथा + अस्याः → तथाऽस्याः · आः → आ घोष से पहले: अस्याः + हर्षेण → अस्या हर्षेण · आः स्वर से पहले, विसर्ग लुप्त: प्राणाः + आप्याय्यन्ते → प्राणा आप्याय्यन्ते।",
        "frame": "किसके (अस्याः) → किससे (हर्षेण, तृतीया) → क्या (प्राणाः) → क्रिया (आप्याय्यन्ते, कर्मवाच्य)।",
    },
    "73": {
        "diagram": {"groups": [
            {"label": "स्थिति और क्रिया", "items": ["गर्भसंगे (गर्भ अटकने पर)", "योनिं धूपयेत् (योनि को धूप दे)"]},
            {"label": "धूपन-द्रव्य (वा = या)", "items": ["कृष्णसर्प-निर्मोक (काले साँप की केंचुली)",
                                                   "पिण्डीतक (सम्भावित: मैनफल)"]}]},
        "chunks": "गर्भसंगे तु | योनिं धूपयेत् | कृष्णसर्पनिर्मोकेन | पिंडीतकेन वा",
        "sandhi": "म् → अनुस्वार व्यञ्जन से पहले: योनिम् + धूपयेत् → योनिं धूपयेत् · छपा ‘तुयोनिं’ = तु योनिम्।",
    },
    "74": {
        "chunks": "बध्नीयाच्च | हिरण्यपुष्पीमूलं | हस्तपादे",
        "sandhi": "त् + च → च्च: बध्नीयात् + च → बध्नीयाच्च · म् → अनुस्वार व्यञ्जन से पहले: मूलम् + हस्तपादे → मूलं हस्तपादे।",
        "frame": "क्रिया (बध्नीयात्) → क्या (हिरण्यपुष्पी का मूल; पहचान अज्ञात) → कहाँ (हस्तपादे)।",
    },
    "75": {
        "diagram": {"groups": [
            {"label": "धारयेत् (धारण करे): वा = या", "items": ["सुवर्चला: पहचान विवादित",
                                                         "विशल्या: सम्भावित लाङ्गली (कलिहारी)"]}]},
        "chunks": "धारयेच्च | सुवर्चलां | विशल्यां वा",
        "sandhi": "त् + च → च्च: धारयेत् + च → धारयेच्च · म् → अनुस्वार व्यञ्जन से पहले: सुवर्चलाम् + विशल्याम् → सुवर्चलां विशल्यां वा।",
    },
    "76": {
        "chain": {"steps": ["१ यदि अपरा न गिरे", "२ दाहिने हाथ से", "३ नाभि के ऊपर से जोर से दबाकर",
                            "४ पीछे से पकड़कर", "५ हिलाए"]},
        "chunks": "अथ प्रसूताया न चेदपरा पतति | ततो दक्षिणेन पाणिना | नाभेरुपरिष्ठाद्बलवदुपपीड्य | पृष्ठत उपसंगृह्य | विधूनुयात्",
        "sandhi": "त् → द् स्वर से पहले: चेत् + अपरा → चेदपरा · ए के बाद विसर्ग → र्: नाभेः + उपरिष्टात् → नाभेरुपरिष्टात् · अः → अ (अ-भिन्न स्वर से पहले): पृष्ठतः + उपसङ्गृह्य → पृष्ठत उपसङ्गृह्य।",
        "frame": "शर्त (न चेत् … पतति) → ततः → साधन (दक्षिणेन पाणिना) → ल्यबन्त (उपपीड्य, उपसङ्गृह्य) → मुख्य क्रिया (विधूनुयात्)।",
    },
    "77": {
        "chunks": "पाष्ण्यां (= पाष्ण्या? सम्भावित) | वा | श्रोणिमाकुट्टयेत्",
        "sandhi": "म् + स्वर: श्रोणिम् + आकुट्टयेत् → श्रोणिमाकुट्टयेत्।",
        "frame": "वा (या: एक और उपाय) → किससे (एड़ी, पाठ सम्भावित) → किस पर (श्रोणिम्) → क्रिया (आकुट्टयेत्)।",
    },
}

# ===================================================================== IMAGE_SPECS
IMAGE_SPECS = {
    ("67", "chain"): {
        "file": "sh3-akala-pravahana-67.svg",
        "alt": ("Flowchart of unit 67: bearing down at the wrong time is like forcing out the urges of feces and urine; "
                "it is useless and unwholesome; it causes, numbered, 1 breathlessness, 2 cough, 3 wasting (probable), "
                "4 hunchedness, and so on."),
        "type": "mermaid",
        "code": ("flowchart TD\n"
                 "  A[\"असमय प्रवाहण\"] --> B[\"मल-मूत्र वेग उदीरण जैसा\"]\n"
                 "  B --> C[\"निरर्थक और अहितकर\"]\n"
                 "  C --> D[\"१ श्वास\"]\n"
                 "  C --> E[\"२ कास\"]\n"
                 "  C --> F[\"३ शोष (सम्भावित)\"]\n"
                 "  C --> G[\"४ कुब्जता\"]\n"
                 "  C --> H[\"आदि\"]\n"),
    },
    ("68", "chain"): {
        "file": "sh3-apravahana-68.svg",
        "alt": ("Flowchart of unit 68: pain is present, yet no bearing down; this is like holding back those very urges; "
                "it leads to injury."),
        "type": "mermaid",
        "code": ("flowchart TD\n"
                 "  A[\"वेदना है\"] --> B[\"फिर भी प्रवाहण नहीं\"]\n"
                 "  B --> C[\"वेगों को रोकने जैसा\"]\n"
                 "  C --> D[\"उपघात (हानि)\"]\n"),
    },
    ("70", "chain"): {
        "file": "sh3-pravahana-avastha-70.svg",
        "alt": ("Flowchart of unit 70: at the exit of the fetus, strongly; on arrival at the mouth of the yoni, more "
                "strongly; until delivery."),
        "type": "mermaid",
        "code": ("flowchart TD\n"
                 "  A[\"गर्भ निकलने पर: बाढम्\"] --> B[\"योनि-मुख पर: बाढतरम्\"]\n"
                 "  B --> C[\"प्रसव तक\"]\n"),
    },
    ("73", "diagram"): {
        "file": "sh3-garbhasanga-dhupana-73.svg",
        "alt": ("Flowchart of unit 73: in garbha-saṅga (retention of the fetus), fumigate the yoni with one of two: the "
                "sloughed skin of a black snake, or piṇḍītaka (probably emetic nut)."),
        "type": "mermaid",
        "code": ("flowchart TD\n"
                 "  A[\"गर्भसंग\"] --> B[\"योनि का धूपन\"]\n"
                 "  B --> C[\"काले साँप की केंचुली\"]\n"
                 "  B -->|\"या\"| D[\"पिण्डीतक\"]\n"
                 "  D -.-> E[\"सम्भावित: मैनफल\"]\n"),
    },
    ("75", "diagram"): {
        "file": "sh3-dharana-dravya-75.svg",
        "alt": ("Table of unit 75: the two plants to be held, with the data's labels: suvarcalā, identity disputed; "
                "viśalyā, probably lāṅgalī."),
        "type": "table",
        "title": "धारण करे: एक या दूसरी (इकाई ७५)",
        "heads": ["द्रव्य", "पहचान"],
        "rows": [["सुवर्चला", "विवादित"], ["विशल्या", "सम्भावित: लाङ्गली (कलिहारी)"]],
    },
    ("76", "chain"): {
        "file": "sh3-apara-patana-76.svg",
        "alt": ("Numbered flowchart of unit 76: 1 if the placenta does not fall, 2 with the right hand, 3 pressing firmly "
                "from above the navel, 4 gripping from behind, 5 one should shake."),
        "type": "mermaid",
        "code": ("flowchart TD\n"
                 "  A[\"१ अपरा न गिरे\"] --> B[\"२ दाहिने हाथ से\"]\n"
                 "  B --> C[\"३ नाभि ऊपर जोर से दबाकर\"]\n"
                 "  C --> D[\"४ पीछे से पकड़कर\"]\n"
                 "  D --> E[\"५ हिलाए\"]\n"),
    },
}
