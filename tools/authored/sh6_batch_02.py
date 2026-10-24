from helpers import mcq, match, order, fill, multi, accepts


AUTHORED = {}

# ---------------------------------------------------------------- unit 14
AUTHORED["14"] = {
    "title": "तासां पृष्ठवंशमुभयतो",
    "question": "By unit 14, where do four of the back's twenty-four (sirās, understood) lie, and which way do they go?",
    "rule": ("Of them (तासाम्, the back's 24, sirās understood, unit 13), on both sides (उभयतः) of the spine (पृष्ठवंश), "
             "two and two go upward (ऊर्ध्वगामिन्यौ); those (ताः) are four (चतस्रः)."),
    "limits": ("Prose; the copula of the last clause is understood. The unit does not say what is to be done with these "
               "four; the data's note on unit 8 counts them among the trunk sirās to be guarded, as an inference only. "
               "The unit appears to continue unit 13 (grouping note)."),
    "explain_hi": ("यह गद्य-पंक्ति इकाई १३ (पीठ में चौबीस सिराएँ) को आगे बढ़ाती दिखती है: उनमें से पृष्ठवंश, यानी रीढ़, के दोनों ओर दो-दो सिराएँ ऊपर जाती हैं। "
                   "‘उभयतः’ = दोनों ओर, और ‘द्वे द्वे’ = दो-दो; इसलिए एक ओर दो, दूसरी ओर दो, कुल चार। "
                   "‘चतस्रः’ ‘चार’ का स्त्रीलिंग रूप है, क्योंकि सिरा शब्द स्त्रीलिंग है। "
                   "इन चार के साथ क्या करना है, यह पंक्ति नहीं कहती। "
                   "सन्धि: ताः + चतस्रः में च से पहले विसर्ग श् बना।"),
    "hook": "रीढ़ के दोनों ओर दो-दो, ऊपर जाती हुई: चार।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 14, where do the two and two upward-going ones (sirās, understood) lie?",
            ("On both sides of the spine", "पृष्ठवंशमुभयतः: on both sides of the pṛṣṭhavaṃśa (spine)."),
            [("In the two groins and the hips", "The groins belong to unit 12, not to the back's list."),
             ("Above the meḍhra, in the belly", "Above the meḍhra is the belly's list (unit 16)."),
             ("Within the heart, in the chest", "The heart is in the chest's list (unit 18).")],
            "Of the back's sirās, two and two go upward on both sides of the spine.",
            "तासां पृष्ठवंशमुभयतो द्वे द्वे ऊर्ध्वगामिन्यौ."),
        order(1, "Put the printed words of unit 14 in the line's order.",
              ["तासां", "पृष्ठवंशमुभयतो", "द्वे द्वे", "ऊर्ध्वगामिन्यौ", "ताश्चतस्रः"],
              "Of them, on both sides of the spine, two and two, going upward; those are four.",
              "तासां → पृष्ठवंशमुभयतो → द्वे द्वे → ऊर्ध्वगामिन्यौ → ताश्चतस्रः."),
        match(2, "Match each word of unit 14 to its meaning.",
              [["तासाम्", "of them"], ["पृष्ठवंशम्", "the spine (back-ridge)"], ["उभयतः", "on both sides"],
               ["ऊर्ध्वगामिन्यौ", "two going upward"], ["चतस्रः", "four"]],
              "Of them, on both sides of the spine, two going upward each; four in all.",
              "तासाम्, पृष्ठवंशम्, उभयतः, ऊर्ध्वगामिन्यौ, चतस्रः.", role="extend",
              teaches="पृष्ठ (back) + वंश (ridge, bamboo) = पृष्ठवंश, the spine (standard); उभयतः takes it in the accusative."),
        mcq("discriminate", 3, "Which split of ताश्चतस्रः in unit 14 is right?",
            ("ताः + चतस्रः", "A visarga before च becomes श्: ताः + चतस्रः → ताश्चतस्रः."),
            [("तात् + चतस्रः", "त् before च becomes च्: it would give ताच्चतस्रः."),
             ("ता + श्चतस्रः", "श्चतस्रः is not a word; the श् comes from the visarga."),
             ("ताः + शतस्रः", "शतस्रः is not a word; the word is चतस्रः (four).")],
            "ताः (those) + चतस्रः (four): visarga before च → श्.",
            "Visarga before च → श्."),
        multi("apply", 4, "Which statements fit unit 14?",
              [("Two lie on each side of the spine", "Right: द्वे द्वे with उभयतः gives two on each side."),
               ("All four lie on one side of the spine", "उभयतः means on both sides."),
               ("द्वे stays unjoined before ऊर्ध्व- because a dual in -ए does not join with a vowel",
                "Right: a dual ending in ए is not joined with a following vowel."),
               ("The unit says the four must not be pierced", "The unit gives no such rule; that is only an inference of the data (unit 8).")],
              [0, 2],
              "Two and two on both sides, four in all; the dual द्वे stays unjoined before a vowel.",
              "उभयतो द्वे द्वे ऊर्ध्वगामिन्यौ ताश्चतस्रः."),
        mcq("transfer", 5, "In a new example, which form of 'four' agrees with the feminine plural नद्यः (rivers)?",
            ("चतस्रः", "चतस्रः is the feminine nominative plural of 'four', as with the sirās in unit 14."),
            [("चत्वारः", "चत्वारः is masculine: it goes with masculine nouns."),
             ("चत्वारि", "चत्वारि is neuter: it goes with neuter nouns."),
             ("चतुरः", "चतुरः is the masculine accusative plural.")],
            "चतस्रो नद्यः: four rivers, as ताश्चतस्रः: those (sirās) are four.",
            "'Four' with a feminine noun: चतस्रः.",
            teaches="'Four' agrees in gender: masculine चत्वारः, neuter चत्वारि, feminine चतस्रः (सिरा is feminine)."),
    ],
}

# ---------------------------------------------------------------- unit 15
AUTHORED["15"] = {
    "title": "चतुर्विंशतिरुदरे",
    "question": "By unit 15, how many (sirās, understood) are in the belly (udara)?",
    "rule": ("Twenty-four (चतुर्विंशतिः) are in the belly (उदरे); the same number as the back of unit 13."),
    "limits": ("Prose, two words; the copula is understood and the counted noun (the sirās of this chapter) is not printed. "
               "Which places in the belly hold them is not said here."),
    "explain_hi": ("यह दो शब्दों की गद्य-पंक्ति है: पेट (उदर) में चौबीस। "
                   "गिनी गई वस्तु छपी नहीं; इस अध्याय के प्रसंग से ये सिराएँ हैं। "
                   "‘चतुर्विंशति’ = चतुर् (चार) + विंशति (बीस), यानी चौबीस; इकाई १३ में पीठ की संख्या भी यही थी। "
                   "‘उदरे’ अ-कारान्त शब्द उदर का सप्तमी एकवचन है: पेट में। "
                   "सन्धि: चतुर्विंशतिः + उदरे में इ के बाद का विसर्ग स्वर से पहले र् बना।"),
    "hook": "पेट में भी चौबीस, पीठ जितनी।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 15, how many (sirās, understood) are in the belly (udara)?",
            ("24", "चतुर्विंशतिरुदरे: twenty-four in the belly."),
            [("40", "Forty is the chest's number (unit 17)."),
             ("32", "Thirty-two is the hip region's number (unit 11)."),
             ("16", "Sixteen is the number of the sides (unit 12).")],
            "Twenty-four in the belly.",
            "चतुर्विंशतिः उदरे."),
        match(1, "Match each word part of unit 15 to its meaning.",
              [["चतुर्", "four"], ["विंशति", "twenty"], ["चतुर्विंशतिः", "twenty-four"], ["उदरे", "in the belly"]],
              "चतुर् + विंशति = twenty-four; उदरे = in the belly.",
              "चतुर्, विंशति, चतुर्विंशतिः, उदरे."),
        fill(2, "In unit 15 'in the belly' is ____ (type it in Devanagari or in English letters, e.g. dharma).",
             accepts("उदरे"),
             "उदरे = in the belly, the locative singular of उदर.",
             "An अ-stem such as उदर takes -ए in the locative singular: उदर → उदरे.",
             "चतुर्विंशतिः + उदरे → चतुर्विंशतिरुदरे."),
        mcq("discriminate", 3, "Which split of चतुर्विंशतिरुदरे in unit 15 is right?",
            ("चतुर्विंशतिः + उदरे", "After इ, a visarga before a vowel becomes र्."),
            [("चतुर्विंशति + रुदरे", "रुदरे is not a word; the र् comes from the visarga."),
             ("चतुर्विंशतिम् + उदरे", "म् before a vowel would give चतुर्विंशतिमुदरे."),
             ("चतुर्विंशते + उदरे", "ए before उ would not give र्.")],
            "चतुर्विंशतिः (twenty-four) + उदरे (in the belly): इः + vowel → इर्.",
            "A visarga after इ → र् before a vowel."),
        mcq("apply", 4, "Which part of the trunk was given the same number as the belly, in unit 13?",
            ("The back (pṛṣṭha)", "Unit 13: चतुर्विंशतिः पृष्ठे, twenty-four in the back."),
            [("The chest (vakṣas)", "The chest has forty (unit 17)."),
             ("The sides (pārśva)", "The sides have sixteen (unit 12)."),
             ("The hips (śroṇi)", "The hip region has thirty-two (unit 11).")],
            "Back and belly both have twenty-four.",
            "चतुर्विंशतिः पृष्ठे · चतुर्विंशतिरुदरे."),
        mcq("transfer", 5, "By the rule of चतुर्विंशतिरुदरे, how is हरिः + आगच्छति (Hari comes) joined in a new example?",
            ("हरिरागच्छति", "After इ, a visarga before a vowel becomes र्, as चतुर्विंशतिः + उदरे."),
            [("हर्यागच्छति", "इ → य् happens only with no visarga; here the visarga gives र्."),
             ("हरिसागच्छति", "Visarga → स् happens before त or थ, not before a vowel."),
             ("हरिशागच्छति", "Visarga → श् happens before च, छ or श, not before a vowel.")],
            "हरिः + आगच्छति = हरिरागच्छति, like चतुर्विंशतिः + उदरे = चतुर्विंशतिरुदरे.",
            "इः + vowel → इर्.",
            teaches="A visarga after इ becomes र् before a vowel: चतुर्विंशतिः + उदरे → चतुर्विंशतिरुदरे."),
    ],
}

# ---------------------------------------------------------------- unit 16
AUTHORED["16"] = {
    "title": "तासां मेंढ्रस्योपरि · ताअपि चतस्रः",
    "question": "By unit 16, where do four of the belly's twenty-four (sirās, understood) lie?",
    "rule": ("Of them (the belly's 24, unit 15), above the meḍhra (penis, standard), on both sides of the romarājī "
             "(line of body hair; restored, near certain), two and two; those also (ता अपि) are four."),
    "limits": ("Prose. Printed ‘उपरिोमराजीम्’ lost the र of रोमराजी; restored, near certain, but no question rests on it. "
               "The unit does not call these four upward-going or say what is done with them (unit 8's note infers: "
               "guarded). Appears to continue unit 15."),
    "explain_hi": ("यह गद्य-पंक्ति इकाई १५ (पेट में चौबीस) को आगे बढ़ाती दिखती है: उनमें से मेढ्र यानी शिश्न के ऊपर, रोमराजी के दोनों ओर, दो-दो सिराएँ; वे भी चार हैं। "
                   "रोमराजी = रोमों की रेखा (डेटा); छपाई में इसका ‘रो’ का र गिर गया है, पर पाठ लगभग निश्चित है। "
                   "‘मेढ्रस्योपरि’ = मेढ्रस्य (मेढ्र के) + उपरि (ऊपर); छपा ‘मेंढ्र’ मेढ्र की ही वर्तनी है। "
                   "‘ता अपि’ = ताः + अपि: आ के बाद का विसर्ग स्वर से पहले गिरता है, फिर कोई सन्धि नहीं होती। "
                   "इकाई १४ की तरह यहाँ ‘ऊपर जाने वाली’ नहीं कहा गया।"),
    "hook": "पेट में भी: मेढ्र के ऊपर, दोनों ओर दो-दो, वे भी चार।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 16, the belly's four lie above which part?",
            ("The meḍhra", "मेढ्रस्योपरि: above the meḍhra (penis)."),
            [("The heart", "The heart belongs to the chest's list (unit 18)."),
             ("The groins", "The groins belong to unit 12."),
             ("The spine", "The spine is the back's place (unit 14).")],
            "Of the belly's sirās, two and two lie above the meḍhra, on both sides.",
            "तासां मेंढ्रस्योपरि ... उभयतो द्वे द्वे."),
        order(1, "Put the printed words of unit 16 in the line's order.",
              ["तासां", "मेंढ्रस्योपरिोमराजीमुभयतो", "द्वे द्वे", "ताअपि", "चतस्रः"],
              "Of them, above the meḍhra on both sides of the hair-line, two and two; those also, four.",
              "तासां → मेंढ्रस्योपरिोमराजीमुभयतो → द्वे द्वे → ताअपि → चतस्रः."),
        match(2, "Match each word of unit 16 to its meaning.",
              [["मेढ्रस्य", "of the penis (meḍhra)"], ["उपरि", "above"], ["उभयतः", "on both sides"],
               ["अपि", "also"], ["चतस्रः", "four"]],
              "Above the meḍhra, on both sides, two and two; those also are four.",
              "मेढ्रस्य, उपरि, उभयतः, अपि, चतस्रः.", role="extend",
              teaches="उपरि (above) takes the genitive: मेढ्रस्य उपरि = above the meḍhra."),
        mcq("discriminate", 3, "Which split of मेंढ्रस्योपरि in unit 16 is right?",
            ("मेढ्रस्य + उपरि", "अ + उ → ओ: मेढ्रस्य + उपरि → मेढ्रस्योपरि."),
            [("मेढ्रस्यः + उपरि", "अः before a vowel other than अ would give मेढ्रस्य उपरि, unjoined."),
             ("मेढ्रस्यो + परि", "मेढ्रस्यो is not a word; the ओ comes from अ + उ."),
             ("मेढ्रस्ये + उपरि", "ए before उ would not give ओ.")],
            "मेढ्रस्य (of the meḍhra) + उपरि (above): अ + उ → ओ.",
            "अ + उ → ओ."),
        multi("apply", 4, "Which statements fit unit 16?",
              [("Unit 16 calls these four upward-going", "That is said of the back's four (unit 14), not here."),
               ("ताअपि stands for ताः + अपि", "Right: आः before a vowel drops its visarga; the data calls it regular."),
               ("The two and two lie on both sides", "Right: उभयतो द्वे द्वे."),
               ("All four lie below the meḍhra", "उपरि means above, not below.")],
              [1, 2],
              "Above the meḍhra, on both sides, two and two; ता अपि = ताः अपि.",
              "तासां मेंढ्रस्योपरि ... उभयतो द्वे द्वे ताअपि चतस्रः."),
        mcq("transfer", 5, "By the rule of ताः + अपि → ता अपि, how is देवाः + अत्र (the gods here) joined in a new example?",
            ("देवा अत्र", "आः before a vowel drops its visarga and no further join is made, as ताः + अपि → ता अपि."),
            [("देवात्र", "आ + अ → आ only when there is no visarga; the gap stays."),
             ("देवो अत्र", "ओ comes from अः before a voiced consonant, not from आः."),
             ("देवारत्र", "र् comes from a visarga after vowels other than अ and आ.")],
            "देवाः + अत्र = देवा अत्र, like ताः + अपि = ता अपि.",
            "आः + vowel → आ, with a gap.",
            teaches="After आ the visarga drops before a vowel, and the two vowels are not joined: ताः + अपि → ता अपि."),
    ],
}

# ---------------------------------------------------------------- unit 17
AUTHORED["17"] = {
    "title": "चत्वारिंशद्वक्षसि",
    "question": "By unit 17, how many (sirās, understood) are in the chest (vakṣas)?",
    "rule": ("Forty (चत्वारिंशत्) are in the chest (वक्षसि), the largest count of the trunk. Our own check, not stated in "
             "the text: with 32 + 16 + 24 + 24 of units 11-15 it makes the 136 of the antarādhi (trunk, probable; unit 7)."),
    "limits": ("Prose, two words; copula understood, counted noun not printed. The sum 32 + 16 + 24 + 24 + 40 = 136 is a "
               "check from the printed numbers, not a statement of this unit. Which of the forty are named follows in "
               "units 18-21."),
    "explain_hi": ("यह दो शब्दों की गद्य-पंक्ति है: वक्ष यानी छाती में चालीस। "
                   "‘वक्षसि’ स-कारान्त शब्द वक्षस् का सप्तमी एकवचन है: छाती में। "
                   "सन्धि: चत्वारिंशत् + वक्षसि में त् घोष व्यंजन व से पहले द् बना। "
                   "धड़ की छपी संख्याएँ, श्रोणि ३२, पार्श्व १६, पीठ २४, पेट २४ और छाती ४०, जोड़ने पर १३६ होती हैं, जो इकाई ७ में धड़ का कुल है; यह जोड़ हमारी जाँच है, पंक्ति का कथन नहीं। "
                   "आगे की इकाइयाँ (१८-२१) इन चालीस में से कुछ के स्थान बताती हैं।"),
    "hook": "छाती में चालीस: धड़ की सबसे बड़ी गिनती।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 17, how many (sirās, understood) are in the chest (vakṣas)?",
            ("40", "चत्वारिंशद्वक्षसि: forty in the chest."),
            [("24", "Twenty-four is the number of the back and of the belly."),
             ("32", "Thirty-two is the hip region's number (unit 11)."),
             ("14", "Fourteen is a part of the forty (unit 21), not the whole.")],
            "Forty in the chest.",
            "चत्वारिंशत् वक्षसि."),
        order(1, "Put the trunk places of units 11-17 in the order the text gives them.",
              ["श्रोणि (hips)", "पार्श्व (sides)", "पृष्ठ (back)", "उदर (belly)", "वक्षस् (chest)"],
              "Hip region (11), sides (12), back (13), belly (15), chest (17).",
              "श्रोणि → पार्श्व → पृष्ठ → उदर → वक्षस्."),
        fill(2, "In unit 17 'in the chest' is ____ (type it in Devanagari or in English letters, e.g. dharma).",
             accepts("वक्षसि"),
             "वक्षसि = in the chest, the locative singular of वक्षस्.",
             "An s-stem such as वक्षस् takes -इ in the locative singular: वक्षस् → वक्षसि.",
             "चत्वारिंशत् + वक्षसि → चत्वारिंशद्वक्षसि."),
        mcq("discriminate", 3, "Which split of चत्वारिंशद्वक्षसि in unit 17 is right?",
            ("चत्वारिंशत् + वक्षसि", "त् before a voiced consonant (व) becomes द्."),
            [("चत्वारिंशः + वक्षसि", "अः before व would give चत्वारिंशो वक्षसि."),
             ("चत्वारिंश + द्वक्षसि", "द्वक्षसि is not a word; the द् comes from त्."),
             ("चत्वारिंशम् + वक्षसि", "म् before a consonant would be written चत्वारिंशं वक्षसि.")],
            "चत्वारिंशत् (forty) + वक्षसि (in the chest): त् → द् before a voiced sound.",
            "त् before a voiced sound → द्."),
        mcq("apply", 4, "Add the printed trunk numbers 32, 16, 24, 24 and 40 (units 11-17). Which total of the chapter do they make?",
            ("136, the trunk's total", "32 + 16 + 24 + 24 + 40 = 136: the antarādhi's number in unit 7."),
            [("164, the upper part", "164 is the upper part's number (unit 9); the sum is 136."),
             ("400, the four limbs", "400 is the limbs' number (unit 5); the sum is 136."),
             ("700, all the sirās", "700 is the whole (unit 4); the sum is 136.")],
            "32 + 16 + 24 + 24 + 40 = 136, the trunk's total.",
            "श्रोणि ३२ + पार्श्व १६ + पृष्ठ २४ + उदर २४ + वक्ष ४० = १३६."),
        mcq("transfer", 5, "By the rule of चत्वारिंशद्वक्षसि, how is मरुत् + वहति (the wind blows) joined in a new example?",
            ("मरुद्वहति", "त् before a voiced consonant becomes द्, as चत्वारिंशत् + वक्षसि."),
            [("मरुत्वहति", "त् stays त् only before an unvoiced sound; व is voiced."),
             ("मरुन्वहति", "त् becomes न् only before a nasal such as न or म."),
             ("मरुच्वहति", "त् becomes च् before a palatal such as च, छ or श (त् + श → च्छ), not before व.")],
            "मरुत् + वहति = मरुद्वहति, like चत्वारिंशत् + वक्षसि = चत्वारिंशद्वक्षसि.",
            "त् + voiced consonant → द्.",
            teaches="A final त् becomes द् before a voiced consonant: चत्वारिंशत् + वक्षसि → चत्वारिंशद्वक्षसि."),
    ],
}

# ---------------------------------------------------------------- unit 18
AUTHORED["18"] = {
    "title": "तासां द्वे हृदये",
    "question": "By unit 18, how many of the chest's (sirās, understood) are in the heart (hṛdaya)?",
    "rule": ("Of them (तासाम्, the chest's forty, unit 17), two (द्वे) are in the heart (हृदये)."),
    "limits": ("Prose; copula understood. The unit names only the place and the number; it says nothing of what the two "
               "do or how they are to be treated. It appears to continue unit 17 (grouping note)."),
    "explain_hi": ("यह गद्य-पंक्ति इकाई १७ (छाती में चालीस) को आगे बढ़ाती दिखती है: उनमें से दो हृदय में। "
                   "‘तासाम्’ स्त्रीलिंग षष्ठी बहुवचन है (उनमें से), क्योंकि सिरा स्त्रीलिंग है। "
                   "‘हृदये’ = हृदय में (हृदय, मानक)। "
                   "ये दो चालीस का ही भाग हैं, उनसे अलग नहीं। "
                   "इन दो के बारे में पंक्ति इससे अधिक कुछ नहीं कहती।"),
    "hook": "छाती के चालीस में से दो, हृदय में।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 18, how many of the chest's (sirās, understood) are in the heart?",
            ("2", "तासां द्वे हृदये: of them, two in the heart."),
            [("4", "Four is not the heart's number; द्वे is two."),
             ("14", "Fourteen is the total of units 18-20, given in unit 21."),
             ("40", "Forty is the whole chest (unit 17).")],
            "Of them, two in the heart.",
            "तासां द्वे हृदये."),
        match(1, "Match each word of unit 18 to its meaning.",
              [["तासाम्", "of them"], ["द्वे", "two"], ["हृदये", "in the heart"]],
              "Of them, two in the heart.",
              "तासाम्, द्वे, हृदये."),
        mcq("extend", 2, "In unit 18, what does the case of हृदये (locative) tell?",
            ("Where the two lie: in the heart", "-ए of an अ-stem is the locative singular: in the heart."),
            [("Whose the two are: of the heart", "The genitive would be हृदयस्य."),
             ("Where they come from: from the heart", "The ablative would be हृदयात्."),
             ("What they serve: for the heart", "The dative would be हृदयाय.")],
            "हृदये = in the heart: the place of the two.",
            "Locative -ए: the place where.",
            teaches="The locative names the place: हृदये = in the heart, as उदरे, वक्षसि."),
        mcq("discriminate", 3, "By units 17-18, which statement is right?",
            ("Two of the forty lie in the heart", "तासाम्: of them; the two are part of the forty."),
            [("The heart has forty of its own as well", "Forty is the chest's count; the heart has two of them."),
             ("The two are added on top of the forty", "तासाम् (of them) makes the two a part, not an addition."),
             ("The two in the heart are said to go upward", "Unit 18 says nothing of their course.")],
            "Of the chest's forty, two are in the heart.",
            "चत्वारिंशद्वक्षसि · तासां द्वे हृदये."),
        fill(4, "In unit 18 'in the heart' is ____ (type it in Devanagari or in English letters, e.g. dharma).",
             accepts("हृदये"),
             "हृदये = in the heart (hṛdaya), locative singular.",
             "An अ-stem takes -ए in the locative singular: हृदय → हृदये.",
             "तासां द्वे हृदये.", role="apply"),
        mcq("transfer", 5, "तासाम् is the feminine 'of them'. In a new example, which form means 'of them' for masculine nouns?",
            ("तेषाम्", "तेषाम् is the masculine (and neuter) genitive plural of तद्."),
            [("तासु", "तासु is the feminine locative plural: in them."),
             ("ताभिः", "ताभिः is the feminine instrumental plural: by them."),
             ("तस्याः", "तस्याः is a feminine singular form: of her.")],
            "तेषाम् (masc.) : तासाम् (fem.) = of them.",
            "'Of them': masculine तेषाम्, feminine तासाम्.",
            teaches="तद् in the genitive plural: masculine/neuter तेषाम्, feminine तासाम् (सिरा is feminine)."),
    ],
}

# ---------------------------------------------------------------- unit 19
AUTHORED["19"] = {
    "title": "द्वे द्वे च स्तनमूलस्तनरोहितेषु",
    "question": "By unit 19, in which named places of the chest are 'two and two'?",
    "rule": ("And (च) two and two (द्वे द्वे) are in the stanamūlas and the stanarohitas, two named places of the "
             "chest given as one dvandva in the locative plural (-एषु)."),
    "limits": ("Prose; copula understood; confidence medium. रोहित in स्तनरोहित is of uncertain sense. Both are marma "
               "names in this tradition (probable), which the line does not say. How the twos are spread is not decided: "
               "no question on it. Appears to continue unit 18."),
    "explain_hi": ("यह गद्य-पंक्ति छाती की सूची में आगे कहती है: और दो-दो स्तनमूलों और स्तनरोहितों में। "
                   "‘स्तनमूल’ = स्तन की जड़; ‘स्तनरोहित’ में रोहित का अर्थ अनिश्चित है, इसलिए दोनों को नाम ही रखा गया। "
                   "इस परम्परा में दोनों मर्मों के नाम हैं (सम्भावित), पर पंक्ति यह नहीं कहती। "
                   "दोनों नाम एक द्वन्द्व समास में हैं, सप्तमी बहुवचन (-एषु) में। "
                   "‘दो-दो’ हर नाम में कैसे बँटे, यह डेटा तय नहीं करता; इकाई २१ का चौदह का जोड़ केवल एक अनुमान से बैठता है।"),
    "hook": "स्तन की जड़ और स्तनरोहित: दो-दो।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 19, where do the 'two and two' lie?",
            ("Stanamūla and stanarohita", "स्तनमूलस्तनरोहितेषु: in the stanamūlas and stanarohitas."),
            [("Kṛkāṭikā and vidhura", "These are the neck's names (unit 24)."),
             ("Groin and kaṭīkataruṇa", "These are the places of unit 12."),
             ("Spine and the hair-line", "These are the back and belly places (units 14, 16).")],
            "And two and two in the stanamūlas and stanarohitas.",
            "द्वे द्वे च स्तनमूलस्तनरोहितेषु."),
        match(1, "Match each word part of unit 19 to its meaning.",
              [["द्वे", "two"], ["च", "and"], ["स्तन", "breast"], ["मूल", "root"]],
              "And two and two in the breast-roots and stanarohitas.",
              "द्वे, च, स्तन, मूल."),
        mcq("extend", 2, "What kind of compound is स्तनमूलस्तनरोहितेषु, by the data?",
            ("A dvandva, locative plural", "Data: dvandva, loc. pl.: in the stanamūlas and the stanarohitas."),
            [("A bahuvrīhi, nominative plural", "It is not 'having ...'; and -एषु is not a nominative ending."),
             ("A dvandva, nominative plural", "A nominative plural would end in -आः or -आनि, not -एषु."),
             ("A tatpuruṣa, genitive singular", "-एषु is no genitive ending; the two names stand side by side.")],
            "Two place names joined as 'X and Y', in the locative plural.",
            "स्तनमूल + स्तनरोहित, -एषु: in the X and the Y.",
            teaches="A dvandva joins names as 'X and Y'; the ending -एषु, put once at the end, gives 'in the X and the Y'."),
        mcq("discriminate", 3, "By the data, which statement about स्तनमूल and स्तनरोहित is right?",
            ("They are kept as names of places", "Data: marma names (probable); the line does not say so, so they are kept as names."),
            [("The line itself calls them marmas", "The data notes that the line does not say so."),
             ("The data reads रोहित as 'red'", "The data leaves the sense of रोहित uncertain."),
             ("They are the two sides of the chest", "The data does not identify them with the sides.")],
            "Both are kept as place names; marma names in this tradition (probable).",
            "स्तनमूल (breast-root) · स्तनरोहित (sense uncertain)."),
        multi("apply", 4, "Which statements fit unit 19?",
              [("The line gives a verb of guarding", "No verb is printed; the copula is understood."),
               ("The line itself gives the total fourteen", "The total fourteen is unit 21."),
               ("The data reads स्तनमूल as 'breast-root'", "Right: स्तन (breast) + मूल (root)."),
               ("The two names stand in the locative plural", "Right: -एषु, in the ...")],
              [2, 3],
              "Two names in the locative plural; स्तनमूल = breast-root; no verb, no total here.",
              "द्वे द्वे च स्तनमूलस्तनरोहितेषु."),
        mcq("transfer", 5, "Like स्तनमूलस्तनरोहितेषु, how are हस्त (hand) and पाद (foot) made one dvandva meaning in the hands and feet, in a new example?",
            ("हस्तपादेषु", "A dvandva takes one ending at the end: -एषु, locative plural."),
            [("हस्तपादानि", "-आनि is a nominative/accusative plural, not 'in'."),
             ("हस्तपादैः", "-ऐः is the instrumental plural: by the hands and feet."),
             ("हस्तपादस्य", "-अस्य is the genitive singular: of the ...")],
            "हस्तपादेषु = in the hands and feet, like स्तनमूलस्तनरोहितेषु.",
            "Dvandva of अ-stems, locative plural: -एषु at the end.",
            teaches="A dvandva puts one case ending on the last member: स्तनमूल-स्तनरोहित-एषु, हस्त-पाद-एषु."),
    ],
}

# ---------------------------------------------------------------- unit 20
AUTHORED["20"] = {
    "title": "एकैकाऽपस्तंभालापेष्विति",
    "question": "By unit 20, how many (sirās, understood) lie in each of the last named places of the chest?",
    "rule": ("One each (एकैका) in the apastambhas and in a second named place, and इति (thus) closes the chest's list. "
             "The second name is printed ‘आलाप’; ‘अपलाप’ is only a conjectural reading."),
    "limits": ("Prose; copula understood; confidence medium. Printed ‘आलाप’ (talk) does not suit a body place; अपलाप is a "
               "conjecture (p lost): no question on the second name. अपस्तम्भ is a marma name in this tradition "
               "(probable). It appears to continue unit 19."),
    "explain_hi": ("यह गद्य-पंक्ति छाती की सूची पूरी करती है: एक-एक अपस्तम्भों में और एक दूसरे नाम वाले स्थानों में; ‘इति’ = इस प्रकार। "
                   "दूसरा नाम छपाई में ‘आलाप’ (बातचीत) है, जो शरीर का स्थान नहीं हो सकता; ‘अपलाप’ (प गिरा हुआ) अनुमानित पाठ है। "
                   "अपस्तम्भ इस परम्परा में एक मर्म का नाम है (सम्भावित)। "
                   "‘एकैका’ = एक + एका, अ + ए मिलकर ऐ। "
                   "‘एकैकाऽप’ में आ के बाद का अवग्रह छपाई की आदत है: आ + अ → आ।"),
    "hook": "अपस्तम्भ आदि में एक-एक; इति, छाती की सूची पूरी।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 20, how many lie in each of the named places?",
            ("One each", "एकैका: one each."),
            [("Two each", "Two and two is unit 19 (द्वे द्वे)."),
             ("Four each", "No four is printed in unit 20."),
             ("Six each", "No six is printed in unit 20.")],
            "One each in the named places.",
            "एकैका ..."),
        match(1, "Match each sure word of unit 20 to its meaning.",
              [["एकैका", "one each"], ["अपस्तम्भ", "apastambha, a named place"], ["इति", "thus"]],
              "One each in the apastambhas ...; thus.",
              "एकैका, अपस्तम्भ, इति."),
        mcq("extend", 2, "How is एकैका (one each) built?",
            ("एक + एका, अ + ए → ऐ", "अ + ए gives ऐ: एक + एका → एकैका."),
            [("एक + ऐका, अ + ऐ → ऐ", "ऐका is not a word; the second part is एका."),
             ("एकः + एका, अः + ए → ऐ", "अः before a vowel other than अ drops to अ and stays unjoined: एक एका."),
             ("एका + एका, आ + ए → आ", "आ + ए gives ऐ, not आ; and the first part is एक.")],
            "एक + एका = एकैका, one each (repeated 'one').",
            "अ + ए → ऐ.",
            teaches="Repeating एक makes 'one each'; अ + ए joins as ऐ: एक + एका → एकैका."),
        mcq("discriminate", 3, "The printed line ends -एष्विति. Which split of that ending is right?",
            ("-एषु + इति", "उ before a different vowel becomes व्: -एषु + इति → -एष्विति."),
            [("-एषि + इति", "इ + इ would give ई: -एषीति."),
             ("-एष्व + इति", "अ + इ would give ए: -एष्वेति."),
             ("-एषः + इति", "अः before इ would give -एष इति, unjoined.")],
            "-एषु (in the ...) + इति (thus): उ + इ → वि.",
            "उ + a different vowel → व् + that vowel."),
        multi("apply", 4, "Which statements fit unit 20 and its data?",
              [("The avagraha after एकैका is a print habit (आ + अ → आ)", "Right: data note; the ऽ marks no lost sound here."),
               ("इति here means 'one each'", "'One each' is एकैका; इति means thus."),
               ("Here the avagraha follows ए or ओ", "The vowel before the ऽ is आ, not ए or ओ."),
               ("अपस्तम्भ is kept as the name of a place", "Right: a marma name in this tradition (probable).")],
              [0, 3],
              "Print-habit ऽ after आ; अपस्तम्भ kept as a name; इति = thus.",
              "एकैकाऽपस्तंभ... इति."),
        mcq("transfer", 5, "By the rule of -एषु + इति → -एष्विति, how is मधु + इति joined in a new example?",
            ("मध्विति", "उ before a different vowel becomes व्, as -एषु + इति → -एष्विति."),
            [("मधूति", "ऊ comes from उ + उ; here उ meets इ."),
             ("मध्वेति", "ए would need अ + इ; there is no अ here."),
             ("मधविति", "अव् comes from ओ before a vowel; there is no ओ.")],
            "मधु + इति = मध्विति, like -एषु + इति = -एष्विति.",
            "उ + इ → वि.",
            teaches="उ before a different vowel becomes व्: -एषु + इति → -एष्विति."),
    ],
}

# ---------------------------------------------------------------- unit 21
AUTHORED["21"] = {
    "title": "ताश्चतुर्दश",
    "question": "By unit 21, how many are the chest's ones (sirās, understood) just listed?",
    "rule": ("Those (ताः, the ones named in units 18-20, sirās understood, as the data reads it) are fourteen (चतुर्दश): a part of the "
             "chest's forty (unit 17)."),
    "limits": ("Prose, two words; copula understood. The print gives only the total; the split 2 + 4 + 4 + 4 is the "
               "data's inference: no question rests on it. Whether a rule of guarding goes with the fourteen is not said "
               "here."),
    "explain_hi": ("यह दो शब्दों की गद्य-पंक्ति छाती की सूची का जोड़ देती है: वे चौदह हैं। "
                   "‘ताः’ (वे) डेटा के अनुसार इकाई १८-२० में गिनी सिराओं की ओर संकेत करता दिखता है। "
                   "चौदह, छाती के चालीस (इकाई १७) का भाग है, उनसे अधिक नहीं। "
                   "२ + ४ + ४ + ४ = १४ का बँटवारा डेटा का अनुमान है; छपाई केवल कुल देती है। "
                   "सन्धि: ताः + चतुर्दश में च से पहले विसर्ग श् बना; ‘चतुर्दश’ = चतुर् (चार) + दश (दस)।"),
    "hook": "छाती की नामित सिराएँ: कुल चौदह।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 21, how many are 'those' (ताः)?",
            ("14", "ताश्चतुर्दश: those are fourteen."),
            [("40", "Forty is the chest's whole count (unit 17)."),
             ("24", "चतुर्दश is fourteen; twenty-four is चतुर्विंशति."),
             ("10", "दश alone is ten; चतुर्दश is four plus ten.")],
            "Those are fourteen.",
            "ताश्चतुर्दश."),
        match(1, "Match each word part of unit 21 to its meaning.",
              [["ताः", "those"], ["चतुर्", "four"], ["दश", "ten"], ["चतुर्दश", "fourteen"]],
              "Those (are) four-ten: fourteen.",
              "ताः, चतुर्, दश, चतुर्दश."),
        mcq("extend", 2, "By the data, how does the fourteen of unit 21 stand to the forty of unit 17?",
            ("It is a part of the forty", "Data: the chest total of forty is in unit 17; fourteen is a part."),
            [("It is added to the forty", "Fourteen is not added; it is counted within the forty."),
             ("It corrects the forty", "The data keeps the forty; nothing is corrected."),
             ("It is the forty's half", "Half of forty would be twenty, not fourteen.")],
            "Fourteen of the chest's forty are the named ones of units 18-20.",
            "चत्वारिंशद्वक्षसि ... ताश्चतुर्दश.",
            teaches="A closing ‘ताः + number’ sums a sub-list; it stays inside the larger count given before."),
        mcq("discriminate", 3, "Which of these number words of the chapter means fourteen?",
            ("चतुर्दश", "चतुर् (four) + दश (ten) = fourteen."),
            [("चतुर्विंशति", "चतुर् + विंशति (twenty) = twenty-four."),
             ("चत्वारिंशत्", "चत्वारिंशत् = forty."),
             ("चतस्रः", "चतस्रः = four (feminine).")],
            "चतुर्दश = 14; चतुर्विंशति = 24; चत्वारिंशत् = 40; चतस्रः = 4.",
            "-दश = ten, -विंशति = twenty."),
        order(4, "Put the printed lines of the chest's list (units 18-21) in the text's order.",
              ["तासां द्वे हृदये", "द्वे द्वे च स्तनमूलस्तनरोहितेषु", "एकैकाऽपस्तंभालापेष्विति", "ताश्चतुर्दश"],
              "Heart (18), stanamūla and stanarohita (19), apastambha ... (20), total fourteen (21).",
              "हृदये → स्तनमूलस्तनरोहितेषु → एकैका... इति → ताश्चतुर्दश.", role="apply"),
        mcq("transfer", 5, "By the pattern of चतुर्दश (4 + 10), what does पञ्चदश mean in a new example?",
            ("15", "पञ्च (five) + दश (ten) = fifteen."),
            [("50", "Fifty is पञ्चाशत्; दश adds ten, it does not multiply."),
             ("25", "Twenty-five is पञ्चविंशति; दश is ten, not twenty."),
             ("5", "पञ्च alone is five; दश adds ten.")],
            "पञ्चदश = 5 + 10 = 15, like चतुर्दश = 4 + 10 = 14.",
            "Unit + दश = that unit plus ten.",
            teaches="A unit before दश adds ten: चतुर्दश = 14, पञ्चदश = 15."),
    ],
}

# ---------------------------------------------------------------- unit 22
AUTHORED["22"] = {
    "title": "चतुर्विंशतिर्ग्रीवायां",
    "question": "By unit 22, how many (sirās, understood) are in the neck (grīvā)?",
    "rule": ("Twenty-four (चतुर्विंशतिः) are in the neck (ग्रीवायाम्). The data's arithmetic check (unit 32 note) counts "
             "the neck in the 164 of the upper part (unit 9); the text does not say so here."),
    "limits": ("Prose, two words; copula understood, counted noun not printed. Which of the 24 are named follows in "
               "units 23-24."),
    "explain_hi": ("यह दो शब्दों की गद्य-पंक्ति है: ग्रीवा यानी गर्दन में चौबीस। "
                   "डेटा के जोड़ (इकाई ३२ की टिप्पणी) के अनुसार गर्दन ऊपरी भाग के १६४ (इकाई ९) में गिनी जाती है; पंक्ति यह नहीं कहती। "
                   "‘ग्रीवायाम्’ आ-कारान्त स्त्रीलिंग शब्द ग्रीवा का सप्तमी एकवचन है: गर्दन में। "
                   "सन्धि: चतुर्विंशतिः + ग्रीवायाम् में इ के बाद का विसर्ग घोष व्यंजन ग से पहले र् बना। "
                   "आगे की इकाइयाँ (२३-२४) इन चौबीस में से नामित सिराएँ बताती हैं।"),
    "hook": "गर्दन में चौबीस, पेट-पीठ जितनी।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 22, how many (sirās, understood) are in the neck (grīvā)?",
            ("24", "चतुर्विंशतिर्ग्रीवायाम्: twenty-four in the neck."),
            [("16", "Sixteen is the number of the jaws and of the tongue (units 25-26)."),
             ("56", "Fifty-six is the eyes' number (unit 30)."),
             ("12", "Twelve is the head's number (unit 35).")],
            "Twenty-four in the neck.",
            "चतुर्विंशतिः ग्रीवायाम्."),
        match(1, "Match each word of units 15, 17 and 22 to its meaning.",
              [["ग्रीवायाम्", "in the neck"], ["उदरे", "in the belly"], ["वक्षसि", "in the chest"],
               ["चतुर्विंशतिः", "twenty-four"]],
              "In the neck, in the belly, in the chest; twenty-four.",
              "ग्रीवायाम्, उदरे, वक्षसि, चतुर्विंशतिः."),
        mcq("extend", 2, "How is ग्रीवायाम् (in the neck) formed from ग्रीवा?",
            ("Feminine आ-stem, -आयाम्", "A feminine आ-stem takes -आयाम् in the locative singular."),
            [("अ-stem ending, -ए", "-ए (as in उदरे) belongs to अ-stems."),
             ("s-stem ending, -असि", "-असि (as in वक्षसि) belongs to s-stems."),
             ("Locative plural, -आसु", "-आसु is plural: in the necks.")],
            "ग्रीवा → ग्रीवायाम्: in the neck.",
            "Feminine आ-stem, locative singular: -आयाम्.",
            teaches="Feminine आ-stems take -आयाम् in the locative singular: ग्रीवा → ग्रीवायाम्."),
        mcq("discriminate", 3, "Which split of चतुर्विंशतिर्ग्रीवायां in unit 22 is right?",
            ("चतुर्विंशतिः + ग्रीवायाम्", "After इ, a visarga before a voiced consonant (ग) becomes र्."),
            [("चतुर्विंशति + र्ग्रीवायाम्", "र्ग्रीवायाम् is not a word; the र् comes from the visarga."),
             ("चतुर्विंशतिम् + ग्रीवायाम्", "म् before a consonant would be written चतुर्विंशतिं ग्रीवायाम्."),
             ("चतुर्विंशती + ग्रीवायाम्", "A final ई stays ई before ग; no र् would appear.")],
            "चतुर्विंशतिः (twenty-four) + ग्रीवायाम् (in the neck): इः + voiced consonant → इर्.",
            "A visarga after इ → र् before a voiced sound."),
        multi("apply", 4, "In which printed joins of this chapter does a visarga after इ become र्?",
              [("ताश्चतुर्दश (unit 21)", "Here आः before च gives श्, not र्."),
               ("चतुर्विंशतिरुदरे (unit 15)", "Right: इः before the vowel उ → इर्."),
               ("उभयतो द्वे (unit 14)", "Here अः before a voiced consonant gives ओ."),
               ("चतुर्विंशतिर्ग्रीवायां (unit 22)", "Right: इः before the voiced consonant ग → इर्.")],
              [1, 3],
              "After इ the visarga becomes र् before a vowel or a voiced consonant.",
              "चतुर्विंशतिः + उदरे / ग्रीवायाम् → चतुर्विंशतिरुदरे / चतुर्विंशतिर्ग्रीवायाम्."),
        mcq("transfer", 5, "By the rule of चतुर्विंशतिर्ग्रीवायां, how is मुनिः + गच्छति (the sage goes) joined in a new example?",
            ("मुनिर्गच्छति", "After इ, a visarga before a voiced consonant becomes र्."),
            [("मुनिगच्छति", "A visarga drops before a voiced consonant after आ; after इ it becomes र्."),
             ("मुनिस्गच्छति", "Visarga → स् happens before त or थ, not before ग."),
             ("मुनीगच्छति", "इ is lengthened, with र् lost, only before another र्; here ग follows.")],
            "मुनिः + गच्छति = मुनिर्गच्छति, like चतुर्विंशतिः + ग्रीवायाम्.",
            "इः + voiced consonant → इर्.",
            teaches="A visarga after इ becomes र् before a voiced consonant: चतुर्विंशतिः + ग्रीवायाम् → चतुर्विंशतिर्ग्रीवायाम्."),
    ],
}

# ---------------------------------------------------------------- unit 23
AUTHORED["23"] = {
    "title": "तासां चतस्रोऽष्टौ च मर्मसंज्ञाः",
    "question": "By unit 23, how many of the neck's (sirās, understood) are named marma?",
    "rule": ("Of them (the neck's 24, unit 22), four (चतस्रः) and eight (अष्टौ) are named marma (मर्मसंज्ञाः, "
             "'having the name marma'; marma = vital spot, a doctrinal term)."),
    "limits": ("Prose; copula understood. The unit does not say where the four and the eight lie, nor why they are given "
               "as two numbers. Marma is kept as a doctrinal term. It appears to continue unit 22; the sixteen of unit 24 "
               "takes up these twelve."),
    "explain_hi": ("यह गद्य-पंक्ति इकाई २२ (गर्दन में चौबीस) को आगे बढ़ाती दिखती है: उनमें से चार और आठ ‘मर्म’ नाम वाली हैं। "
                   "मर्म यानी जीवन-स्थल, शास्त्र का अपना शब्द है, इसलिए वैसा ही रखा गया। "
                   "‘मर्मसंज्ञाः’ बहुव्रीहि है: जिनकी संज्ञा (नाम) मर्म है। "
                   "चार और आठ कहाँ हैं, यह पंक्ति नहीं बताती। "
                   "सन्धि: चतस्रः + अष्टौ में अः + अ मिलकर ओ बना, और अष्टौ का अ गिरा, जिसे अवग्रह (ऽ) दिखाता है।"),
    "hook": "गर्दन के चौबीस में चार और आठ: मर्म नाम वाली।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 23, what are four and eight of the neck's (sirās, understood) called?",
            ("Marma-named (vital spots)", "मर्मसंज्ञाः: having the name marma."),
            [("Upward-going (ūrdhvagāminī)", "Upward-going is said of the back's four (unit 14)."),
             ("Taste-perceiving (rasavedinī)", "Taste-perceiving is said of two of the tongue's (unit 27)."),
             ("Joint-linked (sandhisambandhinī)", "Joint-linked is said of two of the jaws' (unit 25).")],
            "Four and eight are named marma.",
            "तासां चतस्रोऽष्टौ च मर्मसंज्ञाः."),
        order(1, "Put the printed words of unit 23 in the line's order.",
              ["तासां", "चतस्रोऽष्टौ", "च", "मर्मसंज्ञाः"],
              "Of them, four (and) eight, and, named marma.",
              "तासां → चतस्रोऽष्टौ → च → मर्मसंज्ञाः."),
        match(2, "Match each word part of unit 23 to its meaning.",
              [["तासाम्", "of them"], ["चतस्रः", "four"], ["अष्टौ", "eight"], ["मर्म", "vital spot (doctrinal term)"],
               ["संज्ञा", "name"]],
              "Of them, four and eight are 'having the name marma'.",
              "तासाम्, चतस्रः, अष्टौ, मर्म, संज्ञा.", role="extend",
              teaches="मर्मसंज्ञाः is a bahuvrīhi (data): 'whose name is marma', agreeing with the feminine sirās."),
        mcq("discriminate", 3, "Which split of चतस्रोऽष्टौ in unit 23 is right?",
            ("चतस्रः + अष्टौ", "अः + अ → ओ, and the second अ drops (shown by ऽ)."),
            [("चतस्रे + अष्टौ", "ए + अ would keep ए: चतस्रेऽष्टौ."),
             ("चतस्रः + ष्टौ", "ष्टौ is not a word; the word is अष्टौ (eight)."),
             ("चतस्राः + अष्टौ", "आः before a vowel would give चतस्रा अष्टौ, unjoined.")],
            "चतस्रः (four) + अष्टौ (eight): अः + अ → ओऽ.",
            "अः + अ → ओ + ऽ."),
        mcq("apply", 4, "By unit 23, how many in all are named marma?",
            ("Twelve (four and eight)", "चतस्रः + अष्टौ: 4 + 8 = 12; unit 24 then adds 2 + 2 to make sixteen."),
            [("Thirty-two (four times eight)", "The two numbers are joined by च (and), not multiplied."),
             ("Eight (only the अष्टौ)", "च joins the four and the eight; both are named marma."),
             ("Four (only the चतस्रः)", "च joins the four and the eight; both are named marma.")],
            "Four and eight: twelve named marma.",
            "चतस्रोऽष्टौ च = 4 + 8."),
        mcq("transfer", 5, "By the rule of चतस्रोऽष्टौ, how is रामः + अत्र (Rāma here) joined in a new example?",
            ("रामोऽत्र", "अः + अ → ओ, and the अ drops (ऽ), as चतस्रः + अष्टौ → चतस्रोऽष्टौ."),
            [("रामात्र", "अ + अ → आ only when there is no visarga."),
             ("राम अत्र", "अः drops to अ before vowels other than अ; before अ it gives ओऽ."),
             ("रामरत्र", "र् comes from a visarga after vowels other than अ and आ.")],
            "रामः + अत्र = रामोऽत्र, like चतस्रः + अष्टौ = चतस्रोऽष्टौ.",
            "अः + अ → ओऽ.",
            teaches="A visarga after अ, before अ: अः + अ → ओ with ऽ for the dropped अ (चतस्रः + अष्टौ → चतस्रोऽष्टौ)."),
    ],
}

# ---------------------------------------------------------------- unit 24
AUTHORED["24"] = {
    "title": "षोडश शस्त्रेण न स्पृशेत्",
    "question": "By unit 24, which two neck places are added to make sixteen, and what rule goes with them?",
    "rule": ("Two in the two kṛkāṭikās and two in the two vidhuras: thus (इति) sixteen with the twelve of unit 23; "
             "one should not touch them with the knife (शस्त्रेण न स्पृशेत्)."),
    "limits": ("Prose. कृकाटिका (head-neck junction behind) and विधुर (behind the ear) are marma names; the places are "
               "probable: no question on where they lie. Sixteen = 4 + 8 (unit 23) + 2 + 2 (data note). Only 'not "
               "touching with the knife' is stated."),
    "explain_hi": ("यह गद्य-पंक्ति गर्दन की सूची पूरी करती है: दो दोनों कृकाटिकाओं में और दो दोनों विधुरों में; इस प्रकार सोलह; शस्त्र से न छुए। "
                   "कृकाटिका (सिर-गर्दन का पिछला जोड़) और विधुर (कान के पीछे) इस परम्परा में मर्मों के नाम हैं; स्थान सम्भावित हैं। "
                   "डेटा के अनुसार सोलह = इकाई २३ के चार और आठ + यहाँ के दो और दो। "
                   "‘स्पृशेत्’ विधिलिङ् (optative) है: छूना चाहिए; ‘न’ के साथ: नहीं छूना चाहिए। "
                   "सन्धि: कृकाटिकयोः + द्वे और विधुरयोः + इति में ओ के बाद का विसर्ग र् बना।"),
    "hook": "४ + ८ + २ + २ = सोलह: शस्त्र से न छुओ।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 24, what should one not do to the sixteen?",
            ("Touch them with the knife", "शस्त्रेण न स्पृशेत्: one should not touch them with the knife."),
            [("Rub them with any oil", "No oil is named in unit 24."),
             ("Press them with a hand", "No pressing is named in unit 24."),
             ("Warm them with a fire", "No fire is named in unit 24.")],
            "The sixteen are not to be touched with the knife.",
            "षोडश शस्त्रेण न स्पृशेत्."),
        order(1, "Put these words of unit 24 in the line's order.",
              ["कृकाटिकयोः", "विधुरयोः", "षोडश", "शस्त्रेण", "न स्पृशेत्"],
              "In the kṛkāṭikās, in the vidhuras, (thus) sixteen; with the knife not one should touch.",
              "कृकाटिकयोः → विधुरयोः → षोडश → शस्त्रेण → न स्पृशेत्."),
        match(2, "Match each word of unit 24 to its meaning.",
              [["इति", "thus"], ["षोडश", "sixteen"], ["शस्त्रेण", "with the knife"], ["न", "not"],
               ["स्पृशेत्", "one should touch"]],
              "Thus sixteen; one should not touch (them) with the knife.",
              "इति, षोडश, शस्त्रेण, न, स्पृशेत्.", role="extend",
              teaches="शस्त्रेण is the instrumental singular of शस्त्र (knife): 'with the knife'."),
        mcq("discriminate", 3, "By the data, which count makes the sixteen of unit 24?",
            ("4 + 8 + 2 + 2", "The four and eight of unit 23, plus two kṛkāṭikā and two vidhura."),
            [("4 + 8 + 4 + 4", "That would be twenty; unit 24 gives two and two."),
             ("8 + 8 + 2 + 2", "That would be twenty; unit 23 gives four and eight."),
             ("2 + 2 + 2 + 2", "That would be eight; the twelve of unit 23 are counted in.")],
            "Sixteen = 4 + 8 (unit 23) + 2 + 2 (unit 24).",
            "चतस्रोऽष्टौ (२३) + द्वे, द्वे (२४) = षोडश."),
        mcq("apply", 4, "What form is स्पृशेत् in न स्पृशेत्?",
            ("An optative: 'one should touch'", "Data: 3 sg. optative of √स्पृश्; with न, 'one should not touch'."),
            [("A future: 'one will touch'", "The data labels it optative, not future."),
             ("A past: 'one has touched'", "The data labels it optative, not past."),
             ("A command: 'touch it!'", "The data labels it optative (3rd person), not imperative.")],
            "स्पृशेत् = one should touch; न स्पृशेत् = one should not touch.",
            "Optative 3 sg.: स्पृशेत्."),
        mcq("transfer", 5, "By the rule of विधुरयोरिति, how is हस्तयोः + इति joined in a new example?",
            ("हस्तयोरिति", "After ओ, a visarga before a vowel becomes र्, as विधुरयोः + इति."),
            [("हस्तयो इति", "Before a vowel the visarga drops after आ (and after अ before a vowel other than अ); after ओ it becomes र्."),
             ("हस्तयोसिति", "Visarga → स् happens before त or थ, not before a vowel."),
             ("हस्तयविति", "ओ → अव् happens with no visarga; here the visarga gives र्.")],
            "हस्तयोः + इति = हस्तयोरिति, like विधुरयोः + इति = विधुरयोरिति.",
            "ओः + vowel → ओर्.",
            teaches="A visarga after ओ becomes र् before a vowel or voiced consonant: विधुरयोः + इति → विधुरयोरिति."),
    ],
}

# ---------------------------------------------------------------- unit 25
AUTHORED["25"] = {
    "title": "हन्वोः षोडश",
    "question": "By unit 25, how many (sirās, understood) are in the jaws (hanu), and what is said of two of them?",
    "rule": ("In the two jaws (हन्वोः), sixteen; of them (तासाम्), two (द्वे) are connected with the joint "
             "(सन्धिसम्बन्धिन्यौ)."),
    "limits": ("Prose; copula understood. Which joint is not stated (the jaw joint is the natural but unstated reading). "
               "The unit does not say what is to be done with the two."),
    "explain_hi": ("यह गद्य-पंक्ति कहती है: दोनों हनु यानी जबड़ों में सोलह; उनमें दो सन्धि (जोड़) से सम्बद्ध हैं। "
                   "कौन-सा जोड़, यह नहीं कहा गया; जबड़े का जोड़ स्वाभाविक अर्थ है, पर छपा नहीं। "
                   "‘सन्धिसम्बन्धिन्यौ’ स्त्रीलिंग प्रथमा द्विवचन है और ‘द्वे’ (दो सिराएँ) से मेल खाता है। "
                   "छपे ‘तासांसंधि’ में तासाम् का म् व्यंजन से पहले अनुस्वार बना और शब्द जुड़कर छपे हैं।"),
    "hook": "जबड़ों में सोलह; दो जोड़ से जुड़ी।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 25, how many (sirās, understood) are in the two jaws (hanu)?",
            ("16", "हन्वोः षोडश: sixteen in the two jaws."),
            [("24", "Twenty-four is the neck's number (unit 22)."),
             ("12", "Twelve is the head's number (unit 35)."),
             ("56", "Fifty-six is the eyes' number (unit 30).")],
            "Sixteen in the two jaws.",
            "हन्वोः षोडश."),
        order(1, "Put the printed words of unit 25 in the line's order.",
              ["हन्वोः", "षोडश", "तासांसंधिसंबंधिन्यौ", "द्वे"],
              "In the two jaws, sixteen; of them, connected with the joint, two.",
              "हन्वोः → षोडश → तासांसंधिसंबंधिन्यौ → द्वे."),
        match(2, "Match each word of unit 25 to its meaning.",
              [["हन्वोः", "in the two jaws"], ["षोडश", "sixteen"], ["तासाम्", "of them"],
               ["सन्धिसम्बन्धिन्यौ", "two connected with the joint"], ["द्वे", "two"]],
              "In the two jaws, sixteen; of them, two connected with the joint.",
              "हन्वोः, षोडश, तासाम्, सन्धिसम्बन्धिन्यौ, द्वे.", role="extend",
              teaches="सन्धि (joint) + सम्बन्धिन् (connected with): which joint is not stated; the jaw joint is only the natural reading."),
        mcq("discriminate", 3, "In the printed तासांसंधिसंबंधिन्यौ, what is the ं of तासां?",
            ("The final म् of तासाम्", "Final म् before a consonant (स) is written as anusvāra."),
            [("A dual ending of तासा", "तासाम् is a genitive plural; there is no word तासा."),
             ("A trace of a lost न्", "Nothing is lost; ं stands for the final म्."),
             ("A locative plural sign", "The locative plural would be तासु.")],
            "तासाम् + सन्धि... → तासां सन्धि...: म् → ं before a consonant.",
            "Final म् before a consonant → ं."),
        mcq("apply", 4, "Why is सन्धिसम्बन्धिन्यौ in the feminine dual?",
            ("It agrees with द्वे, the two", "Data: f. nom. du., going with द्वे, the two (sirās, understood), a feminine noun."),
            [("It agrees with हन्वोः, two jaws", "हन्वोः is locative; सम्बन्धिन्यौ is nominative, so it goes with द्वे."),
             ("Joints always come in pairs", "Grammar, not anatomy, sets the ending: it agrees with द्वे."),
             ("It is not dual but plural", "-इन्यौ is a dual ending (data: f. nom. du.).")],
            "द्वे ... सन्धिसम्बन्धिन्यौ: two (sirās) connected with the joint.",
            "Adjective agrees with its noun: f. nom. du."),
        mcq("transfer", 5, "By the pattern of सम्बन्धिन्यौ, which form of वासिन् (dwelling) goes with two feminine nouns in a new example?",
            ("वासिन्यौ", "Feminine -इनी stem, nominative dual -इन्यौ, as सम्बन्धिन्यौ."),
            [("वासिनौ", "वासिनौ is the masculine dual."),
             ("वासिन्यः", "वासिन्यः is the feminine plural."),
             ("वासी", "वासी is the masculine nominative singular.")],
            "द्वे वासिन्यौ, like द्वे सन्धिसम्बन्धिन्यौ.",
            "-इन् adjective, feminine dual: -इन्यौ.",
            teaches="An -इन् adjective makes its feminine in -इनी; its nominative dual is -इन्यौ (सम्बन्धिन्यौ, ऊर्ध्वगामिन्यौ)."),
    ],
}

# ---------------------------------------------------------------- unit 26
AUTHORED["26"] = {
    "title": "षोडश जिव्हायां",
    "question": "By unit 26, how many (sirās, understood) are in the tongue (jihvā)?",
    "rule": ("Sixteen (षोडश) are in the tongue (जिह्वायाम्); the print has जिव्हा, a letter reversal of जिह्वा."),
    "limits": ("Prose, two words; copula understood. Which of the sixteen are named follows in unit 27, outside this "
               "unit."),
    "explain_hi": ("यह दो शब्दों की गद्य-पंक्ति है: जिह्वा यानी जीभ में सोलह। "
                   "छपा ‘जिव्हा’ जिह्वा के अक्षरों का उलट-फेर है (ह्व की जगह व्ह); डेटा इसे जिह्वा पढ़ता है। "
                   "‘जिह्वायाम्’ आ-कारान्त स्त्रीलिंग शब्द का सप्तमी एकवचन है, ग्रीवायाम् की तरह। "
                   "हनु (इकाई २५) और जिह्वा, दोनों में सोलह-सोलह हैं। "
                   "आगे इकाई २७, जो डेटा के अनुसार इसी की निरन्तरता प्रतीत होती है, कुछ सिराओं के काम बताती है।"),
    "hook": "जीभ में भी सोलह, जबड़ों जितनी।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 26, how many (sirās, understood) are in the tongue (jihvā)?",
            ("16", "षोडश जिह्वायाम्: sixteen in the tongue."),
            [("24", "Twenty-four is the neck's number (unit 22)."),
             ("40", "Forty is the chest's number (unit 17)."),
             ("56", "Fifty-six is the eyes' number (unit 30).")],
            "Sixteen in the tongue.",
            "षोडश जिह्वायाम्."),
        fill(1, "In unit 26 'in the tongue' is ____ (type it in Devanagari or in English letters, e.g. dharma).",
             accepts("जिह्वायाम्", None, "जिव्हायाम्", "jihvayam", "jivhayam"),
             "जिह्वायाम् = in the tongue; printed जिव्हायां.",
             "जिह्वा → जिह्वायाम्, locative singular.",
             "षोडश जिह्वायाम्.", role="warmup"),
        mcq("extend", 2, "What does the data say about the printed जिव्हा in unit 26?",
            ("A letter reversal of जिह्वा", "Data: printed jivhā is a letter reversal of jihvā, normalised."),
            [("A separate word for 'lip'", "No such word; the data reads जिह्वा, tongue."),
             ("A conjectural, doubtful reading", "The data does not flag it as doubtful; it is a plain reversal."),
             ("A dual form of the tongue", "-आयाम् is singular; the data reads loc. sg.")],
            "जिव्हा (print) = जिह्वा (tongue), with ह and व swapped.",
            "Printed व्ह = ह्व here.",
            teaches="Some printed spellings swap letters (व्ह for ह्व); the data records the print and reads the true word."),
        mcq("discriminate", 3, "By units 25-26, which pair of parts both have sixteen?",
            ("The jaws and the tongue", "हन्वोः षोडश (25), षोडश जिह्वायाम् (26)."),
            [("The neck and the jaws", "The neck has twenty-four (unit 22)."),
             ("The tongue and the nose", "The nose has twenty-four (unit 28)."),
             ("The jaws and the eyes", "The eyes have fifty-six (unit 30).")],
            "Jaws sixteen, tongue sixteen.",
            "हन्वोः षोडश · षोडश जिह्वायाम्."),
        multi("apply", 4, "Which statements fit unit 26?",
              [("The unit names two taste-perceiving sirās", "Those come in unit 27, not here."),
               ("The data reads the printed जिव्हा as जिह्वा", "Right: a letter reversal, normalised."),
               ("The number given is twenty-four", "The number is षोडश, sixteen."),
               ("No verb is printed; 'are' is understood", "Right: copula understood.")],
              [1, 3],
              "Sixteen in the tongue; जिव्हा = जिह्वा; copula understood.",
              "षोडश जिव्हायां."),
        mcq("transfer", 5, "By the pattern of जिह्वायाम्, how is शाला (hall) put in the locative singular in a new example?",
            ("शालायाम्", "A feminine आ-stem takes -आयाम् in the locative singular, as जिह्वा → जिह्वायाम्."),
            [("शाले", "-ए is the locative of अ-stems (उदरे), not of feminine आ-stems."),
             ("शालासु", "शालासु is plural: in the halls."),
             ("शालायाः", "शालायाः is genitive or ablative: of / from the hall.")],
            "शालायाम् = in the hall, like जिह्वायाम् = in the tongue.",
            "Feminine आ-stem, locative singular: -आयाम्.",
            teaches="Feminine आ-stems take -आयाम् in the locative singular: जिह्वा → जिह्वायाम्, शाला → शालायाम्."),
    ],
}


# ===================================================================== NOTES_HI
NOTES_HI = {
    "14": ("गद्य; विश्वास उच्च; कोई पाठ-चिह्न नहीं। अन्तिम वाक्यांश में क्रिया समझी जाती है। डेटा के अनुसार यह पंक्ति इकाई १३ (पीठ में "
           "चौबीस) को आगे बढ़ाती दिखती है। पृष्ठवंश = रीढ़ (मानक)। सन्धि जाँची: पृष्ठवंशम् + उभयतः → पृष्ठवंशमुभयतः (म् स्वर से पहले "
           "जुड़ा); उभयतः + द्वे → उभयतो द्वे (अः + घोष व्यंजन → ओ); द्वे ऊर्ध्व... में द्विवचन का ए स्वर से नहीं जुड़ता; ताः + चतस्रः → "
           "ताश्चतस्रः (च से पहले विसर्ग → श्)। इकाई ८ के पाठ-चिह्न में इन चार को रक्षणीय सिराओं में गिना गया है; यह अनुमान है।"),
    "15": ("गद्य; विश्वास उच्च; कोई पाठ-चिह्न नहीं। क्रिया ‘हैं’ समझी जाती है; गिनी गई वस्तु (सिराएँ) छपी नहीं। सन्धि जाँची: "
           "चतुर्विंशतिः + उदरे → चतुर्विंशतिरुदरे (इ के बाद विसर्ग + स्वर → र्)।"),
    "16": ("गद्य; विश्वास उच्च। पाठ-चिह्न (लगभग निश्चित): छपा ‘मेंढ्रस्योपरिोमराजीम्’ में रोमराजी का र गिरा है (केवल मात्रा छपी); "
           "रोमराजी = पेट पर रोमों की रेखा; इस पर कोई प्रश्न नहीं। छपा मेंढ्र = मेढ्र (शिश्न, मानक)। सन्धि जाँची: मेढ्रस्य + उपरि → "
           "मेढ्रस्योपरि (अ + उ → ओ); ताः + अपि → ता अपि (आ के बाद विसर्ग स्वर से पहले गिरता है; डेटा: नियमित)। डेटा के अनुसार "
           "इकाई १५ की निरन्तरता प्रतीत होती है।"),
    "17": ("गद्य; विश्वास उच्च; कोई पाठ-चिह्न नहीं। क्रिया समझी जाती है। सन्धि जाँची: चत्वारिंशत् + वक्षसि → चत्वारिंशद्वक्षसि "
           "(त् + घोष व्यंजन → द्)। धड़ का जोड़ ३२ + १६ + २४ + २४ + ४० = १३६ (इकाई ७) छपी संख्याओं से हमारी जाँच है।"),
    "18": ("गद्य; विश्वास उच्च; कोई पाठ-चिह्न नहीं। क्रिया समझी जाती है। हृदय (मानक)। डेटा: इकाई १७ (छाती) की निरन्तरता "
           "दिखती है; ‘तासाम्’ = छाती के चालीस में से।"),
    "19": ("गद्य; विश्वास मध्यम; कोई पाठ-चिह्न नहीं। स्तनमूल (स्तन की जड़) और स्तनरोहित (रोहित का अर्थ अनिश्चित) इस परम्परा में "
           "मर्म-नाम (सम्भावित); पंक्ति यह नहीं कहती, इसलिए नाम ही रखे गए। ‘द्वे द्वे’ का बँटवारा तय नहीं: इकाई २१ का चौदह तभी बैठता "
           "है जब हर नाम में दोनों ओर दो-दो मानें; यह अनुमान है, इस पर कोई प्रश्न नहीं। द्वन्द्व, सप्तमी बहुवचन।"),
    "20": ("गद्य; विश्वास मध्यम। पाठ-चिह्न (सम्भावित): छपा ‘आलाप’ (बातचीत) शरीर का स्थान नहीं; ‘अपलाप’ (प गिरा) अनुमानित पाठ "
           "है; दूसरे नाम पर कोई प्रश्न नहीं। अपस्तम्भ मर्म-नाम (सम्भावित)। ‘एकैकाऽप’ का अवग्रह छपाई की आदत (आ + अ → आ)। सन्धि "
           "जाँची: एक + एका → एकैका (अ + ए → ऐ); -एषु + इति → -एष्विति (उ + भिन्न स्वर → व्)। इकाई १९ की निरन्तरता प्रतीत होती है (डेटा)।"),
    "21": ("गद्य; विश्वास उच्च; कोई पाठ-चिह्न नहीं। ‘ताः’ = इकाई १८-२० में गिनी सिराएँ (डेटा: प्रतीत होता है)। चौदह, छाती के "
           "चालीस (इकाई १७) का भाग है। २ + ४ + ४ + ४ का बँटवारा अनुमान है, छपाई केवल कुल देती है। सन्धि जाँची: ताः + चतुर्दश → "
           "ताश्चतुर्दश (च से पहले विसर्ग → श्)।"),
    "22": ("गद्य; विश्वास उच्च; कोई पाठ-चिह्न नहीं। क्रिया समझी जाती है। सन्धि जाँची: चतुर्विंशतिः + ग्रीवायाम् → "
           "चतुर्विंशतिर्ग्रीवायाम् (इ के बाद विसर्ग + घोष व्यंजन → र्)। पंक्ति के अन्त का ‘ग्रीवायां’ म् का अनुस्वार-लेखन है।"),
    "23": ("गद्य; विश्वास उच्च; कोई पाठ-चिह्न नहीं। मर्म = जीवन-स्थल, शास्त्रीय शब्द, वैसा ही रखा गया। मर्मसंज्ञाः बहुव्रीहि, "
           "स्त्रीलिंग प्रथमा बहुवचन। सन्धि जाँची: चतस्रः + अष्टौ → चतस्रोऽष्टौ (अः + अ → ओ, अ का लोप ऽ से)। इकाई २२ की निरन्तरता प्रतीत होती है (डेटा)।"),
    "24": ("गद्य; विश्वास उच्च; कोई पाठ-चिह्न नहीं। कृकाटिका (सिर-गर्दन का पिछला जोड़) और विधुर (कान के पीछे): मर्म-नाम, स्थान "
           "सम्भावित। छपा ‘द्वेविधुरयोरिति’ = द्वे विधुरयोः इति। सोलह = इकाई २३ के ४ + ८ और यहाँ के २ + २ (डेटा)। स्पृशेत् = विधिलिङ् "
           "३ एकवचन। सन्धि जाँची: कृकाटिकयोः + द्वे → कृकाटिकयोर्द्वे, विधुरयोः + इति → विधुरयोरिति (ओ के बाद विसर्ग → र्)।"),
    "25": ("गद्य; विश्वास उच्च; कोई पाठ-चिह्न नहीं। क्रिया समझी जाती है। कौन-सा सन्धि (जोड़), यह नहीं कहा गया; जबड़े का जोड़ "
           "स्वाभाविक पर अकथित अर्थ है। हनु (मानक)। छपा ‘तासांसंधि’ = तासाम् + सन्धि (म् → ं, व्यंजन से पहले), शब्द जुड़े छपे।"),
    "26": ("गद्य; विश्वास उच्च; कोई पाठ-चिह्न नहीं। छपा ‘जिव्हा’ जिह्वा के अक्षरों का उलट-फेर है (एक बार दर्ज, शब्द-सूची में "
           "सामान्य किया गया)। क्रिया समझी जाती है। इकाई २७ इसकी निरन्तरता प्रतीत होती है (डेटा)।"),
}


# ===================================================================== AIDS
AIDS = {
    "14": {
        "chain": {"steps": ["पीठ में चौबीस (इकाई १३)", "उनमें: रीढ़ के दोनों ओर", "दो-दो, ऊपर जाने वाली", "वे चार"]},
        "chunks": "तासां | पृष्ठवंशमुभयतो | द्वे द्वे | ऊर्ध्वगामिन्यौ | ताश्चतस्रः",
        "sandhi": "अः + घोष व्यंजन → ओ: उभयतः + द्वे → उभयतो द्वे · च से पहले विसर्ग → श्: ताः + चतस्रः → ताश्चतस्रः · द्विवचन का ए स्वर से नहीं जुड़ता: द्वे ऊर्ध्व...।",
    },
    "15": {
        "chunks": "चतुर्विंशतिः | उदरे",
        "sandhi": "इ के बाद विसर्ग + स्वर → र्: चतुर्विंशतिः + उदरे → चतुर्विंशतिरुदरे।",
        "frame": "कितने: चतुर्-विंशति (४ + २० = २४) → कहाँ: उदरे (पेट में)।",
    },
    "16": {
        "diagram": {"groups": [
            {"label": "पीठ (इकाई १३-१४)", "items": ["कुल चौबीस", "रीढ़ के दोनों ओर", "दो-दो, ऊपर जाने वाली", "वे चार"]},
            {"label": "पेट (इकाई १५-१६)", "items": ["कुल चौबीस", "मेढ्र के ऊपर, दोनों ओर", "दो-दो", "वे भी चार"]}]},
        "chunks": "तासां | मेंढ्रस्योपरिोमराजीमुभयतो | द्वे द्वे | ताअपि चतस्रः",
        "sandhi": "अ + उ → ओ: मेढ्रस्य + उपरि → मेढ्रस्योपरि · आ के बाद विसर्ग स्वर से पहले गिरता है: ताः + अपि → ता अपि।",
    },
    "17": {
        "diagram": {"groups": [
            {"label": "धड़ (अन्तराधि, सम्भावित) की सिराएँ, इकाई ११-१७ (स्थान: संख्या)",
             "items": ["श्रोणि (११): ३२", "पार्श्व (१२): १६", "पृष्ठ (१३): २४", "उदर (१५): २४", "वक्ष (१७): ४०",
                       "जोड़ (हमारी जाँच): १३६ = इकाई ७"]}]},
        "chunks": "चत्वारिंशत् | वक्षसि",
        "sandhi": "त् + घोष व्यंजन → द्: चत्वारिंशत् + वक्षसि → चत्वारिंशद्वक्षसि।",
    },
    "18": {
        "chunks": "तासां | द्वे | हृदये",
        "frame": "किसमें से: तासाम् (छाती के चालीस में से) → कितने: द्वे (दो) → कहाँ: हृदये (हृदय में)।",
        "anchors": "छाती के चालीस का पहला भाग हृदय: केवल दो। (मेरी याद-पद्धति)",
    },
    "19": {
        "chunks": "द्वे द्वे च | स्तनमूलस्तनरोहितेषु",
        "frame": "कितने: द्वे द्वे (दो-दो) → कहाँ: स्तनमूल + स्तनरोहित, द्वन्द्व, सप्तमी बहुवचन (-एषु)।",
        "anchors": "स्तनमूल = स्तन की जड़; स्तनरोहित को केवल नाम की तरह याद रखें, उसका अर्थ अनिश्चित है।",
    },
    "20": {
        "chunks": "एकैकाऽपस्तंभालापेष्विति",
        "sandhi": "अ + ए → ऐ: एक + एका → एकैका · उ + भिन्न स्वर → व्: -एषु + इति → -एष्विति · आ + अ → आ (ऽ छपाई की आदत)।",
        "frame": "कितने: एकैका (एक-एक) → कहाँ: अपस्तम्भ और छपा ‘आलाप’ (अनुमानित पाठ अपलाप) → इति: सूची पूरी।",
    },
    "21": {
        "chain": {"steps": ["हृदय में दो (इकाई १८)", "स्तनमूल, स्तनरोहित में दो-दो (१९)",
                            "अपस्तम्भ आदि में एक-एक (२०)", "वे चौदह (२१)"]},
        "chunks": "ताश्चतुर्दश",
        "sandhi": "च से पहले विसर्ग → श्: ताः + चतुर्दश → ताश्चतुर्दश।",
    },
    "22": {
        "chunks": "चतुर्विंशतिः | ग्रीवायां",
        "sandhi": "इ के बाद विसर्ग + घोष व्यंजन → र्: चतुर्विंशतिः + ग्रीवायाम् → चतुर्विंशतिर्ग्रीवायाम्।",
        "frame": "कितने: चतुर्विंशति (२४) → कहाँ: ग्रीवायाम् (गर्दन में; आ-कारान्त स्त्रीलिंग, सप्तमी -आयाम्)।",
    },
    "23": {
        "chunks": "तासां | चतस्रोऽष्टौ च | मर्मसंज्ञाः",
        "sandhi": "अः + अ → ओ, अ का लोप (ऽ): चतस्रः + अष्टौ → चतस्रोऽष्टौ।",
        "frame": "किसमें से: तासाम् (गर्दन के चौबीस में से) → कितने: चार और आठ → क्या: मर्मसंज्ञाः (मर्म नाम वाली)।",
    },
    "24": {
        "chain": {"steps": ["गर्दन में चौबीस (इकाई २२)", "उनमें चार और आठ मर्म नाम वाली (२३)",
                            "दो कृकाटिका में, दो विधुर में (२४)", "इस प्रकार सोलह", "शस्त्र से न छुए"]},
        "chunks": "द्वे कृकाटिकयोर्द्वेविधुरयोरिति | षोडश | शस्त्रेण न स्पृशेत्",
        "sandhi": "ओ के बाद विसर्ग → र्: कृकाटिकयोः + द्वे → कृकाटिकयोर्द्वे · विधुरयोः + इति → विधुरयोरिति।",
    },
    "25": {
        "chunks": "हन्वोः षोडश | तासांसंधिसंबंधिन्यौ द्वे",
        "frame": "कहाँ: हन्वोः (दोनों जबड़ों में) → कितने: षोडश (१६) → उनमें: द्वे सन्धिसम्बन्धिन्यौ (दो, जोड़ से सम्बद्ध; कौन-सा जोड़, अकथित)।",
        "sandhi": "व्यंजन से पहले अन्तिम म् → ं: तासाम् + सन्धि... → तासां सन्धि... (छपाई में जुड़ा)।",
    },
    "26": {
        "chunks": "षोडश | जिव्हायां",
        "frame": "कितने: षोडश (१६) → कहाँ: जिह्वायाम् (जीभ में; छपा जिव्हा = जिह्वा)।",
        "anchors": "जबड़े (२५) सोलह, जीभ (२६) सोलह: पास-पास दो सोलह। (मेरी याद-पद्धति)",
    },
}


# ===================================================================== IMAGE_SPECS
IMAGE_SPECS = {
    ("14", "chain"): {
        "file": "sh6-prishthavamsha-14.svg",
        "alt": ("Flowchart of units 13-14: twenty-four sirās in the back; of them, on both sides of the spine; two and two "
                "going upward; those are four."),
        "type": "mermaid",
        "code": ("flowchart TD\n"
                 "  A[\"पीठ में २४ (इकाई १३)\"] --> B[\"उनमें: रीढ़ के दोनों ओर\"]\n"
                 "  B --> C[\"दो-दो, ऊपर जाने वाली\"]\n"
                 "  C --> D[\"वे चार (इकाई १४)\"]\n"),
    },
    ("16", "diagram"): {
        "file": "sh6-prishtha-udara-16.svg",
        "alt": ("Two columns. Back (units 13-14): twenty-four in all; on both sides of the spine; two and two, going "
                "upward; those are four. Belly (units 15-16): twenty-four in all; above the meḍhra, on both sides; two "
                "and two; those also are four."),
        "type": "split",
        "title": "इकाई १३-१६: पीठ और पेट",
        "cols": [["पीठ (इकाई १३-१४)", ["कुल चौबीस", "रीढ़ के दोनों ओर", "दो-दो, ऊपर जाने वाली", "वे चार"]],
                 ["पेट (इकाई १५-१६)", ["कुल चौबीस", "मेढ्र के ऊपर, दोनों ओर", "दो-दो", "वे भी चार"]]],
    },
    ("17", "diagram"): {
        "file": "sh6-antaradhi-17.svg",
        "alt": ("Table of the trunk's sirās by the printed numbers of units 11-17: hip region 32, sides 16, back 24, "
                "belly 24, chest 40; their sum 136 matches the trunk total of unit 7 (a check, not a statement of the text)."),
        "type": "table",
        "title": "इकाई ११-१७: धड़ (अन्तराधि, सम्भावित)",
        "heads": ["स्थान (इकाई)", "संख्या"],
        "rows": [["श्रोणि (११)", "३२"], ["पार्श्व (१२)", "१६"], ["पृष्ठ (१३)", "२४"], ["उदर (१५)", "२४"],
                 ["वक्ष (१७)", "४०"], ["जोड़, हमारी जाँच (इकाई ७)", "१३६"]],
    },
    ("21", "chain"): {
        "file": "sh6-vaksha-14-21.svg",
        "alt": ("Chain of the chest list, units 18-21 in printed order: two in the heart; two and two in the stanamūlas "
                "and stanarohitas; one each in the apastambhas and a second named place; those are fourteen."),
        "type": "chain",
        "title": "इकाई १८-२१: छाती की नामित सिराएँ",
        "steps": ["हृदय में दो (१८)", "स्तनमूल, स्तनरोहित में दो-दो (१९)", "अपस्तम्भ आदि में एक-एक (२०)",
                  "वे चौदह (२१)"],
    },
    ("24", "chain"): {
        "file": "sh6-griva-16-24.svg",
        "alt": ("Flowchart of units 22-24: twenty-four in the neck; of them four and eight named marma; two in the "
                "kṛkāṭikās and two in the vidhuras (marma names, places probable); thus sixteen; not to be touched "
                "with the knife."),
        "type": "mermaid",
        "code": ("flowchart TD\n"
                 "  A[\"गर्दन में २४ (इकाई २२)\"] --> B[\"उनमें ४ और ८: मर्म नाम\"]\n"
                 "  B --> C[\"२ कृकाटिका, २ विधुर\"]\n"
                 "  C --> D[\"इस प्रकार १६\"]\n"
                 "  D --> E[\"शस्त्र से न छुए\"]\n"),
    },
}
