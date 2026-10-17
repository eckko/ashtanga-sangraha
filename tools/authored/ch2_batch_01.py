from helpers import mcq, match, order, fill, multi, accepts

# Chapter 2 (शिष्योपनयनीय), units 1-13.
# Sentences often run across the edition's two-line units; every question here
# keeps to what its own unit contains.

AUTHORED = {}

# ---------------------------------------------------------------- unit 1
AUTHORED["1"] = {
    "title": "अथातः शिष्योपनयनीयम्",
    "question": "What does the speaker announce at the start of the chapter?",
    "rule": ("अथातः + title word in -ीयम् (concerning ...) + अध्यायं + व्याख्यास्यामः = Now, "
             "therefore, we shall explain the chapter concerning that subject."),
    "limits": ("This is the stock opening formula. It names the subject "
               "(the pupil's initiation) but says nothing yet about how the "
               "initiation is done."),
    "explain_hi": ("यह अध्याय का आरम्भ-सूत्र है। ‘अथ’ (अब) और ‘अतः’ (इसलिए) मिलकर "
                   "‘अथातः’ बनते हैं। ‘शिष्योपनयनीयम्’ अध्याय का नाम है, यानी शिष्य के "
                   "उपनयन (दीक्षा) से जुड़ा, और ‘अध्यायम्’ के साथ यह कर्म है, इसलिए दोनों "
                   "में -म् है। ‘व्याख्यास्यामः’ का -मः ‘हम’ (उत्तम पुरुष बहुवचन) बताता है "
                   "और भविष्य है: हम समझाएँगे।"),
    "hook": "अब, इसलिए · शिष्य की दीक्षा वाला अध्याय · हम समझाएँगे।",
    "core": False,
    "questions": [
        mcq("pretest", 0,
            "A chapter opens अथातः शिष्योपनयनीयमध्यायं व्याख्यास्यामः. What is announced?",
            ("The chapter on the pupil's initiation will be explained",
             "व्याख्यास्यामः says 'we shall explain'; the subject is the chapter on the pupil's initiation."),
            [("The pupil's initiation has already been completed",
              "Nothing here says it is finished; the verb looks ahead."),
             ("The teacher will now question the pupil",
              "The verb is 'we shall explain', not a question."),
             ("The previous chapter is being closed",
              "The line opens a new chapter.")],
            "The line announces that the chapter on the pupil's initiation will now be explained.",
            "अथातः ... अध्यायं व्याख्यास्यामः = now, therefore, we shall explain the chapter."),
        match(1, "Match each word of the opening to its meaning.",
              [["अथ", "now"], ["अतः", "therefore"], ["अध्यायम्", "chapter"],
               ["शिष्योपनयनीयम्", "concerning the pupil's initiation"]],
              "Three words of the formula and the title word of this chapter.",
              "अथ = now; अतः = therefore; अध्यायम् = chapter; शिष्योपनयनीयम् = concerning the pupil's initiation."),
        fill(2, "The word for \"we shall explain\" is ____ (type it in Devanagari or in English letters, e.g. dharma).",
             accepts("व्याख्यास्यामः", None, "व्याख्यास्याम"),
             "व्याख्यास्यामः is the verb of the announcement: 'we shall explain'.",
             "The ending -मः marks 'we' (first person plural), and the verb looks ahead: we shall explain.",
             "व्याख्यास्यामः = we shall explain; -मः = 'we'.",
             role="extend"),
        mcq("discriminate", 3, "Which is the right split of अथातः?",
            ("अथ + अतः", "अ + अ joins as आ, so अथ + अतः is written अथातः."),
            [("अथ + इतः", "अ + इ would join as ए, giving अथेतः."),
             ("अथा + तः", "तः is not a word."),
             ("अ + थातः", "Neither part is a word here.")],
            "अथातः = अथ (now) + अतः (therefore).",
            "अ + अ → आ: अथ + अतः = अथातः."),
        order(4, "Put the words of the announcement in the order of the line.",
              ["अथ", "अतः", "शिष्योपनयनीयम्", "अध्यायम्", "व्याख्यास्यामः"],
              "The line runs: now, therefore, the-initiation-chapter, chapter, we-shall-explain.",
              "अथ → अतः → शिष्योपनयनीयम् → अध्यायम् → व्याख्यास्यामः.", role="apply"),
        mcq("transfer", 5,
            "An invented line reads अथातः आहारीयमध्यायं व्याख्यास्यामः (आहारीयम् = concerning food). By the same pattern, what is announced?",
            ("Now, therefore, we shall explain the chapter on food",
             "The pattern is अथातः + title word + अध्यायं + व्याख्यास्यामः; आहारीयम् = concerning food."),
            [("Now, therefore, we shall eat a meal",
              "व्याख्यास्यामः means explaining, and अध्यायम् is a chapter."),
             ("Now, therefore, the chapter on food is finished",
              "The verb is a future 'we shall explain', not a close."),
             ("Now, therefore, you will explain the chapter on food",
              "-मः marks 'we', not 'you'.")],
            "आहारीयम् = concerning food; the rest of the formula is unchanged.",
            "अथातः + title word in -ीयम् + अध्यायं + व्याख्यास्यामः = we shall explain the chapter concerning that subject.",
            teaches="Chapters open with one fixed pattern: only the title word changes."),
    ],
}

# ---------------------------------------------------------------- unit 2
AUTHORED["2"] = {
    "title": "गुरुरुक्तोऽभियुक्तः",
    "question": "Which qualities of mind and body does this verse list?",
    "rule": ("धीस्मृतिपाटवैः = with intellect, memory, skill; ऋजु-आस्य-नासा-नयनः = "
             "with straight mouth, nose and eyes; तनु-स्निग्ध-त्वक्-छविः = with thin, smooth skin and complexion."),
    "limits": ("Who is described is uncertain: the book's own Hindi and English disagree, "
               "and गुरुरुक्तः can be read in more than one way. "
               "The card teaches only the listed qualities."),
    "explain_hi": ("इस श्लोक में गुणों और लक्षणों की सूची है। मन के गुण: बुद्धि (धी), स्मृति और "
                   "कुशलता (पाटव), जो ‘-ैः’ अन्त के कारण ‘के साथ’ के अर्थ में हैं। शरीर के "
                   "लक्षण: मुख, नाक और आँखें सीधी, और त्वचा पतली, चिकनी तथा कान्तिमान। "
                   "‘गुरुरुक्तः’ का वाक्य-अन्वय अनिश्चित है, इसलिए यहाँ यह तय नहीं किया गया कि "
                   "सूची किसकी है; केवल सूची पढ़ें।"),
    "hook": "धी · स्मृति · पाटव; सीधे मुख-नाक-आँख; पतली चिकनी त्वचा।",
    "core": False,
    "questions": [
        mcq("pretest", 0,
            "The verse lists three mental gifts. Which three?",
            ("Intellect, memory and skill",
             "धी, स्मृति and पाटव are the three in the verse."),
            [("Wealth, fame and skill", "Wealth and fame are not listed."),
             ("Anger, pride and memory", "Anger and pride are not listed."),
             ("Speed, courage and strength", "None of these is listed.")],
            "The verse names intellect (धी), memory (स्मृति) and skill (पाटव).",
            "धीस्मृतिपाटवैः = with intellect, memory and skill."),
        match(1, "Match each word to its meaning.",
              [["धी", "intellect"], ["स्मृति", "memory"],
               ["ऋजु", "straight"], ["तनु", "thin"]],
              "Two words are mental gifts, two describe the body.",
              "धी = intellect; स्मृति = memory; ऋजु = straight; तनु = thin."),
        mcq("extend", 2, "Which is the right split of ऋज्वास्य?",
            ("ऋजु + आस्य", "उ before a different vowel becomes व्: ऋजु + आस्य = ऋज्वास्य."),
            [("ऋज + वास्य", "वास्य is not the second word here."),
             ("ऋजो + आस्य", "ओ + आ would not give ज्वा."),
             ("ऋजि + आस्य", "इ + आ would give ज्या (ऋज्यास्य), not ज्वा.")],
            "ऋज्वास्य = ऋजु (straight) + आस्य (mouth).",
            "उ + different vowel → व्: ऋजु + आस्य = ऋज्वास्य.",
            teaches="Before a different vowel, उ turns into व् and the next vowel joins on to it."),
        mcq("discriminate", 3,
            "What does the ending -ैः in धीस्मृतिपाटवैः show?",
            ("Plural 'with': by means of intellect, memory and skill",
             "-ैः here is the instrumental plural, 'with'."),
            [("Singular 'of': the intellect of one man",
              "It is plural, and not 'of'."),
             ("Dual 'two': only intellect and memory",
              "The word names three qualities, and -ैः is not a dual ending here."),
             ("Plural 'from': coming away from these qualities",
              "'From' would be a different ending.")],
            "धीस्मृतिपाटवैः = with intellect, memory and skill (instrumental plural).",
            "-ैः on such a word = 'with' (plural)."),
        order(4, "Put the three mental gifts in the order of the verse.",
              ["धी", "स्मृति", "पाटव"],
              "The verse says intellect, then memory, then skill.",
              "धी → स्मृति → पाटव.", role="apply"),
        mcq("transfer", 5,
            "By the pattern of ऋज्वास्यनासानयनः, whom does a word like दीर्घबाहुः describe?",
            ("One with long arms",
             "Such a compound (bahuvrīhi) names the person who has the features: दीर्घ (long) + बाहु (arm)."),
            [("A long arm itself", "The compound names the owner, not the arm."),
             ("One who cuts arms", "Nothing in the pattern says cutting."),
             ("The length of a road", "बाहु is an arm, not a road.")],
            "A bahuvrīhi like ऋज्वास्यनासानयनः names the one who 'has' these features.",
            "Feature words in a bahuvrīhi describe the person who has them.",
            teaches="A compound of this kind describes a person by what he has: दीर्घबाहुः = one with long arms."),
    ],
}

# ---------------------------------------------------------------- unit 3
AUTHORED["3"] = {
    "title": "ब्रह्मचारी जितद्वंद्वः",
    "question": "What qualities does the verse give for the student?",
    "rule": ("ब्रह्मचारी जितद्वन्द्वो धीरः सुचरितः स्थिरः; षण्मासानुषितः शक्तः "
             "लज्जाशौचकलान्वितः = a celibate student who has overcome the pairs of "
             "opposites, steadfast, well conducted, firm, six months resident, capable, "
             "and endowed with modesty, cleanliness and skill."),
    "limits": ("The verse does not say with whom he lived for six months; the teacher "
               "is only understood. कला is rendered 'skill' ('arts' is possible)."),
    "explain_hi": ("इस श्लोक का कर्ता ‘ब्रह्मचारी’ है। पहली पंक्ति के गुण: द्वन्द्वों "
                   "(सुख-दुःख जैसे जोड़ों) को जीत चुका, धीर, सदाचारी, स्थिर। दूसरी पंक्ति: "
                   "छह महीने रह चुका, समर्थ, और लज्जा, शुचिता तथा कला से ‘अन्वित’ (युक्त)। "
                   "‘जितद्वन्द्वः’ में ‘जित’ का अर्थ जीता हुआ है; जिसने द्वन्द्व जीते वही "
                   "जितद्वन्द्वः। गुरु का नाम श्लोक में नहीं है; वह प्रसंग से समझा जाता है।"),
    "hook": "ब्रह्मचारी: द्वन्द्व जीता · धीर · सदाचारी · स्थिर · छह मास रहा · समर्थ · लज्जा-शौच-कला।",
    "core": True,
    "questions": [
        mcq("pretest", 0,
            "How long has this student already lived, according to the verse?",
            ("Six months",
             "षण्मासानुषितः says he has lived six months."),
            [("Three months", "The verse says six, not three."),
             ("One year", "A year is not mentioned."),
             ("Twelve years", "Twelve years is not mentioned.")],
            "He is ‘षण्मासानुषितः’: one who has lived six months.",
            "षण्मास + अनुषितः = lived six months."),
        match(1, "Match each word of the verse to its meaning.",
              [["ब्रह्मचारी", "celibate student"],
               ["जितद्वन्द्वः", "one who has conquered the pairs of opposites"],
               ["सुचरितः", "of good conduct"], ["शक्तः", "capable"]],
              "These four words are the student and his qualities.",
              "ब्रह्मचारी = celibate student; जितद्वन्द्वः = conquered the pairs of opposites; सुचरितः = of good conduct; शक्तः = capable."),
        mcq("extend", 2,
            "In लज्जाशौचकलान्वितः, what does the ending अन्वितः add to the three nouns?",
            ("Endowed with them",
             "अन्वित means endowed with: modesty, cleanliness and skill belong to him."),
            [("Deprived of them", "That is the opposite of अन्वित."),
             ("Afraid of them", "Nothing here means fear."),
             ("Taught by them", "The nouns are what he has, not who teaches him.")],
            "लज्जा (modesty), शौच (cleanliness), कला (skill) + अन्वितः = endowed with these.",
            "noun-list + अन्वितः = endowed with those.",
            teaches="A list of nouns followed by अन्वितः names what the person has."),
        mcq("discriminate", 3,
            "Which rendering of the second line is correct?",
            ("Having lived six months, capable, endowed with modesty, cleanliness and skill",
             "It follows षण्मासानुषितः शक्तो लज्जाशौचकलान्वितः word for word."),
            [("Having lived six years, capable, endowed with modesty, wealth and skill",
              "Six months, not years; and wealth is not listed."),
             ("Having lived six months, unable, endowed with modesty, cleanliness and skill",
              "शक्तः is capable, not unable."),
             ("Having lived six months, capable, endowed with anger, cleanliness and skill",
              "Anger is not listed; modesty is.")],
            "The line gives one residence of six months and three gifts: लज्जा, शौच, कला.",
            "Second line = six months resident + capable + modesty, cleanliness, skill."),
        order(4, "Put these descriptions in the order of the first line.",
              ["ब्रह्मचारी", "जितद्वन्द्वः", "धीरः", "सुचरितः", "स्थिरः"],
              "The first line runs: student, conqueror of opposites, steadfast, well conducted, firm.",
              "ब्रह्मचारी → जितद्वन्द्वः → धीरः → सुचरितः → स्थिरः.", role="apply"),
        mcq("transfer", 5,
            "By the pattern of जितद्वन्द्वः, what does an invented word जितक्रोधः describe?",
            ("One who has conquered anger",
             "जित (conquered) + क्रोध (anger), used for the person, like जितद्वन्द्वः."),
            [("One who has caused anger", "जित means conquered, not caused."),
             ("Anger that has won", "The compound describes the person, not the anger."),
             ("One who has lost to anger", "That would be the opposite.")],
            "जितद्वन्द्वः = one who has conquered the pairs; जितक्रोधः works the same way.",
            "जित + noun (as a describing compound) = one who has conquered that.",
            teaches="जित + a noun describes the person who has conquered it."),
    ],
}

# ---------------------------------------------------------------- unit 4
AUTHORED["4"] = {
    "title": "शिष्योऽध्याप्यो गतो यावदन्तम्",
    "question": "Until when is the pupil taught, and what occasions does the second line name?",
    "rule": ("शिष्यः अध्याप्यः यावदन्तं तन्त्रार्थकर्मणाम् = the pupil is to be taught "
             "up to the end of the treatise, its meaning and its practices; न + three "
             "occasions in the locative = not (to study) at these times."),
    "limits": ("The verb of the prohibition (पठेत्) comes in the next unit; here only "
               "the occasions are named. गतः (gone) can be read in more than one way, "
               "and Rāhu-sighting is rendered literally. The three items may also be read "
               "as one phrase; the card follows the three-item reading."),
    "explain_hi": ("पहली पंक्ति कहती है कि शिष्य को तब तक पढ़ाया जाए जब तक वह तन्त्र (ग्रन्थ), "
                   "उसके अर्थ और कर्मों के अन्त तक न पहुँच जाए। ‘अध्याप्यः’ का अर्थ ‘पढ़ाने "
                   "योग्य’ है। दूसरी पंक्ति से निषेध शुरू होता है: ‘न’ के साथ तीन सप्तमी रूप: असमय "
                   "बिजली-गर्जन में, भूकम्प में, राहु-दर्शन पर। क्रिया ‘पठेत्’ अगले श्लोक में आती है, "
                   "इसलिए वाक्य दो इकाइयों में चलता है।"),
    "hook": "अन्त तक पढ़ाओ · ‘न’ (क्रिया अगली इकाई में) असमय बिजली-गर्जन, भूकम्प, राहु-दर्शन पर।",
    "core": False,
    "questions": [
        mcq("pretest", 0,
            "Until what point is the pupil to be taught, according to the first line?",
            ("Until he reaches the end of the treatise, its meaning and its practices",
             "यावदन्तं तन्त्रार्थकर्मणाम् = up to the end of the treatise, meaning and practices."),
            [("Until he has taught the whole treatise to another pupil",
              "Teaching others is not mentioned."),
             ("Until the teacher himself grows old and weak",
              "Age is not mentioned."),
             ("Until he can recite a single chapter from memory",
              "The goal is the end of the whole treatise, not one chapter.")],
            "He is taught up to the end of the treatise, its meaning and its practices.",
            "यावदन्तम् = up to the end."),
        match(1, "Match each word to its meaning.",
              [["शिष्यः", "pupil"], ["अध्याप्यः", "to be taught"],
               ["यावदन्तम्", "up to the end"], ["राहुदर्शने", "at the sight of Rāhu"]],
              "The first three belong to the first line, the last to the occasions.",
              "शिष्यः = pupil; अध्याप्यः = to be taught; यावदन्तम् = up to the end; राहुदर्शने = at the sight of Rāhu."),
        mcq("extend", 2, "Which is the right split of नाकालविद्युत्स्तनिते?",
            ("न + अकालविद्युत्स्तनिते",
             "अ + अ joins as आ: न + अकाल... = नाकाल..."),
            [("न + आकालविद्युत्स्तनिते", "The next word begins with अकाल (untimely), not आकाल."),
             ("ना + कालविद्युत्स्तनिते", "That would drop the negative अ- of अकाल and turn 'untimely' into 'timely'."),
             ("नाका + लविद्युत्स्तनिते", "लविद्युत्... is not a word.")],
            "न (not) + अकाल-विद्युत्-स्तनिते (in untimely lightning and thunder).",
            "अ + अ → आ: न + अकाल... = नाकाल...",
            teaches="When न meets a word beginning with अ, the two अ merge into आ."),
        mcq("discriminate", 3,
            "What does the ending -णाम् in तन्त्रार्थकर्मणाम् show?",
            ("Plural 'of': of the listed things",
             "-णाम् here is the genitive plural."),
            [("Singular 'in': inside one single practice of the treatise",
              "It is plural, and 'in' would be a different ending."),
             ("Singular 'by': done by one man through practice",
              "It is not an instrumental."),
             ("Plural 'to': given to the treatises one by one",
              "'To' would be a different ending.")],
            "तन्त्रार्थकर्मणाम् = of the treatise, its meaning and its practices (three-item reading).",
            "-णाम् / -नाम् on a plural word = 'of'."),
        order(4, "Put the three occasions in the order of the second line.",
              ["अकालविद्युत्स्तनिते", "भूकम्पे", "राहुदर्शने"],
              "The line names untimely lightning and thunder first, then an earthquake, then the sight of Rāhu.",
              "अकालविद्युत्स्तनिते → भूकम्पे → राहुदर्शने.", role="apply"),
        mcq("transfer", 5,
            "By the pattern of राहुदर्शने, what does an invented चन्द्रदर्शने mean?",
            ("At the sight of the moon",
             "दर्शने (locative) = at the sight; चन्द्र is the moon."),
            [("By the sight of the moon", "-ने in this pattern is 'at/in', not 'by'."),
             ("From the moon's setting", "दर्शन is sight, not setting."),
             ("Of the moon's sight", "That would be a genitive.")],
            "-दर्शने with the thing seen before it means 'at the sight of' it.",
            "X-दर्शने = at the sight of X.",
            teaches="A word ending in -दर्शने names the time of seeing something: राहुदर्शने, चन्द्रदर्शने."),
    ],
}

# ---------------------------------------------------------------- unit 5
AUTHORED["5"] = {
    "title": "पञ्चदश्यामचन्द्रायाम्",
    "question": "On what occasions and in what manner is reciting forbidden?",
    "rule": ("न (from the previous verse) + पठेत् = he should not recite: ... in the teacher's "
             "absence, and not too slowly, nor with tones too high or too low."),
    "limits": ("The tithi phrase (पञ्चदश्याम् अचन्द्रायाम्) is read as the fifteenth day when "
               "the moon is absent; the text itself does not say 'new moon'. The word "
               "अविच्छिन्नपदम् is possibly mistaken; nothing is built on either."),
    "explain_hi": ("पिछले श्लोक का ‘न’ यहाँ ‘पठेत्’ (पढ़े) से पूरा होता है। पहली पंक्ति में समय और "
                   "स्थिति बताई है: पन्द्रहवीं तिथि जब चन्द्रमा न हो, और गुरु की अनुपस्थिति "
                   "(‘परोक्षे’)। दूसरी पंक्ति में पाठ की रीति: न बहुत धीमा (‘अतिमन्दम्’), और न बहुत "
                   "ऊँचे या नीचे स्वर में। ‘पठेत्’ का -एत् ‘चाहिए’ का अर्थ देता है। "
                   "‘अविच्छिन्नपदम्’ का पाठ सन्दिग्ध है, इसलिए उस पर कोई प्रश्न नहीं बना।"),
    "hook": "न पढ़े: गुरु की अनुपस्थिति में · न बहुत धीमा · न बहुत ऊँचा-नीचा स्वर।",
    "core": False,
    "questions": [
        mcq("pretest", 0,
            "In whose absence should he not recite, according to the first line?",
            ("The teacher's",
             "परोक्षे गुरोः = in the absence of the teacher."),
            [("The king's", "The king is not mentioned."),
             ("His father's", "His father is not mentioned."),
             ("A patient's", "A patient is not mentioned.")],
            "The first line says not in the absence of the teacher (गुरोः परोक्षे).",
            "परोक्षे गुरोः = in the teacher's absence."),
        match(1, "Match each word to its meaning.",
              [["पठेत्", "should recite"], ["परोक्षे", "in the absence"],
               ["गुरोः", "of the teacher"], ["अतिमन्दम्", "too slowly"]],
              "Two words come from the first line and two from the second.",
              "पठेत् = should recite; परोक्षे = in the absence; गुरोः = of the teacher; अतिमन्दम् = too slowly."),
        mcq("extend", 2, "Which is the right split of नात्युच्चनीचकैः?",
            ("न + अति + उच्चनीचकैः",
             "इ before a different vowel becomes य्: अति + उच्च = अत्युच्च; न + अत्यु... = नात्यु..."),
            [("ना + त्युच्चनीचकैः", "त्युच्च... is not a word."),
             ("न + आति + उच्चनीचकैः", "आति is not the word here; it is अति (too)."),
             ("न + अत्य + उच्चनीचकैः", "अत्य is not a word; the join of अति and उच्च makes अत्युच्च.")],
            "नात्युच्चनीचकैः = न (not) + अति (too) + उच्च-नीचकैः (high and low tones).",
            "इ + different vowel → य्: अति + उच्च = अत्युच्च.",
            teaches="Before a different vowel, इ turns into य्: अति + उच्च = अत्युच्च."),
        multi("discriminate", 3, "Which of these are named among the manners of reciting in the second line?",
              [("Too slowly", "अतिमन्दम् is named."),
               ("Tones too high or too low", "अत्युच्चनीचकैः is named."),
               ("While walking", "Walking is not mentioned."),
               ("Before sunrise", "The time of day is not mentioned.")],
              [0, 1],
              "The line names too slowly and tones too high or too low (it also has the doubtful phrase अविच्छिन्नपदम्, left aside).",
              "Named faults: अतिमन्दम् (too slow), अत्युच्च-नीचकैः (too high / too low)."),
        order(4, "Put these phrases of the first line in the order of the verse.",
              ["पञ्चदश्याम्", "अचन्द्रायाम्", "परोक्षे", "गुरोः", "पठेत्"],
              "The first line gives the tithi, then 'moonless', then 'in the absence', then 'of the teacher', then the verb.",
              "पञ्चदश्याम् → अचन्द्रायाम् → परोक्षे → गुरोः → पठेत्.", role="apply"),
        mcq("transfer", 5,
            "An invented word लिखेत् is built like पठेत् (from √लिख्, to write). What does it say?",
            ("He should write",
             "-एत् is the 'should' ending, as in पठेत्."),
            [("He wrote", "A past form would not end in -एत्."),
             ("He will write", "-एत् is not the future ending."),
             ("Let them write", "That is a plural, and -एत् is singular.")],
            "पठेत् and लिखेत् share the -एत् ending: 'he should ...'.",
            "root + -एत् = he should do it.",
            teaches="A verb ending in -एत् is a 'should' form: पठेत्, लिखेत्."),
    ],
}

# ---------------------------------------------------------------- unit 6
AUTHORED["6"] = {
    "title": "हितान्यतममाचार्यम्",
    "question": "How should the pupil serve the teacher, and when should he sleep and rise?",
    "rule": ("आचार्यं पर्युपासीत राजवत्; शयीत सुप्त एव अस्मिन्; उत्तिष्ठेत अस्य पूर्वतः = he should "
             "attend upon the teacher as upon a king, lie down after him and rise before him."),
    "limits": ("The compound हितान्यतमम् (one among the well-wishers?) is uncertain and "
               "carries no question. The printed सुप्त एव is regularly सुप्तः + एव; the data reads "
               "it as the locative सुप्ते (\"when he is asleep\") because the sense (\"lie down only "
               "when he sleeps\") is the same either way."),
    "explain_hi": ("आचार्य की सेवा ‘राजवत्’, यानी राजा के समान आदर से करनी है; ‘-वत्’ का अर्थ "
                   "‘के समान’ है। ‘पर्युपासीत’ का अर्थ ‘पास रहकर सेवा करे’ है। दूसरी पंक्ति में दिनचर्या: "
                   "गुरु के सो जाने पर ही सोए (‘शयीत’) और उनसे पहले उठे (‘उत्तिष्ठेत ... पूर्वतः’)। "
                   "‘हितान्यतमम्’ का अर्थ सन्दिग्ध है (हितैषियों में से एक?), इसलिए उस पर कोई प्रश्न नहीं है। ‘पर्युपासीत’ और ‘शयीत’ का -ईत ‘चाहिए’ का अर्थ देता है।"),
    "hook": "राजा के समान सेवा · गुरु के बाद सोए · गुरु से पहले उठे।",
    "core": False,
    "questions": [
        mcq("pretest", 0,
            "How should the pupil treat the teacher, according to the first line?",
            ("As he would a king",
             "राजवत् means 'like a king'."),
            [("As he would a friend", "A friend is not mentioned."),
             ("As he would a father", "A father is not mentioned."),
             ("As he would a guest", "A guest is not mentioned.")],
            "He should wait upon the teacher like a king (राजवत्).",
            "राजवत् = like a king."),
        match(1, "Match each word to its meaning.",
              [["पर्युपासीत", "should attend upon"], ["राजवत्", "like a king"],
               ["शयीत", "should lie down"], ["उत्तिष्ठेत", "should rise"]],
              "Two verbs of service and sleep, one of rising, and the comparison.",
              "पर्युपासीत = should attend upon; राजवत् = like a king; शयीत = should lie down; उत्तिष्ठेत = should rise."),
        mcq("extend", 2, "What does -वत् add in राजवत्?",
            ("'Like': like a king",
             "-वत् after a noun makes a word meaning 'like that'."),
            [("'From': coming from a king", "'From' is a different ending."),
             ("'For': meant for a king", "'For' is a different ending."),
             ("'In': placed in a king", "'In' is a different ending.")],
            "राजवत् = राज + वत्: like a king.",
            "noun + -वत् = like that noun.",
            teaches="-वत् after a noun means 'like' it: राजवत् = like a king."),
        mcq("discriminate", 3,
            "Which pair of times does the second line give the pupil?",
            ("He lies down after the teacher sleeps and rises before him",
             "शयीत सुप्त एवास्मिन् (lies down only when he is asleep) and उत्तिष्ठेतास्य पूर्वतः (rises before him) say exactly this."),
            [("He lies down before the teacher sleeps and rises after him",
              "This reverses both."),
             ("He lies down after the teacher sleeps and rises after him",
              "He rises before the teacher, not after."),
             ("He lies down before the teacher sleeps and rises before him",
              "He lies down only after the teacher is asleep.")],
            "He sleeps only when the teacher has fallen asleep, and rises before him.",
            "After the teacher sleeps; before the teacher rises."),
        order(4, "Put the pupil's actions in the order of the verse.",
              ["पर्युपासीत", "राजवत्", "शयीत", "उत्तिष्ठेत"],
              "The verse gives service, the comparison, lying down, and then rising.",
              "पर्युपासीत → राजवत् → शयीत → उत्तिष्ठेत.", role="apply"),
        mcq("transfer", 5,
            "An invented line reads शिष्यः गुरुं पितृवत् पर्युपासीत. What does it say?",
            ("The pupil should attend upon the teacher as upon a father",
             "पितृवत् = like a father; पर्युपासीत = should attend upon."),
            [("The pupil attended on his father as on a teacher",
              "It is the teacher who is attended upon, and the comparison is a father."),
             ("The father should attend upon the teacher",
              "The doer is the pupil."),
             ("The teacher will attend upon the pupil like a father",
              "The pupil attends, not the teacher.")],
            "The pattern of राजवत् carries over to other nouns.",
            "noun-वत् + पर्युपासीत = he should attend upon, like that noun.",
            teaches="-वत् after a noun gives the comparison, and the middle optative -ईत (पर्युपासीत, शयीत) says \"should\": पितृवत् पर्युपासीत = should attend like a father."),
    ],
}

# ---------------------------------------------------------------- unit 7
AUTHORED["7"] = {
    "title": "न ब्रूयात्केवलं नाम",
    "question": "What does the verse forbid, and which qualities does it list?",
    "rule": ("न ब्रूयात् केवलं नाम = he should not utter the bare name. "
             "अभेद्यः, अनुद्धतः, सूनृतः, प्रियदर्शनः = unshakable, not arrogant, "
             "truthful and pleasant in speech, pleasant to look at."),
    "limits": ("Whose name is not said is not stated here. The phrase न साध्वपि विनोदयेत् "
               "and the word स्तब्धः (read as अस्तब्धः) are uncertain; no question rests "
               "on either."),
    "explain_hi": ("पहली पंक्ति का एक निषेध स्पष्ट है: ‘केवलं नाम’, यानी अकेला नाम न बोले "
                   "(ग्रन्थ का प्रसंग गुरु की ओर संकेत करता है, श्लोक स्वयं नाम नहीं देता)। "
                   "‘न साध्वपि विनोदयेत्’ का अर्थ दो तरह से लग सकता है, इसलिए उसे छोड़ दिया है। "
                   "दूसरी पंक्ति गुणों की सूची है: अभेद्य (अटूट), अनुद्धत (उद्धत नहीं), सूनृत (सत्य और "
                   "प्रिय बोलने वाला), प्रियदर्शन। बीच का ‘स्तब्धः’ शब्द संदिग्ध है, उसे छोड़ दिया गया है।"),
    "hook": "केवल नाम न बोले · अभेद्य · अनुद्धत · सूनृत · प्रियदर्शन।",
    "core": False,
    "questions": [
        mcq("pretest", 0,
            "A good student's speech is described in the second line. Which fits?",
            ("Truthful and pleasant",
             "सूनृतः = truthful and pleasant in speech."),
            [("Fast and forceful", "Speed and force are not mentioned."),
             ("Brief and rare", "Brevity is not mentioned."),
             ("Loud and learned", "Loudness is not mentioned.")],
            "सूनृतः means truthful and pleasant in speech.",
            "सूनृतः = truthful and pleasant in speech."),
        match(1, "Match each word to its meaning.",
              [["अभेद्यः", "unshakable"], ["अनुद्धतः", "not arrogant"],
               ["सूनृतः", "truthful and pleasant in speech"],
               ["प्रियदर्शनः", "pleasant to look at"]],
              "These four words are qualities in the second line.",
              "अभेद्यः = unshakable; अनुद्धतः = not arrogant; सूनृतः = truthful and pleasant in speech; प्रियदर्शनः = pleasant to look at."),
        mcq("extend", 2, "Which is the right split of अनुद्धतः?",
            ("अन् + उद्धतः",
             "The negative अ- becomes अन्- before a vowel: अन् + उद्धत = अनुद्धत."),
            [("अनु + द्धतः", "द्धतः is not a word."),
             ("अ + नुद्धतः", "नुद्धतः is not a word."),
             ("अना + उद्धतः", "अना- is not the negative prefix here.")],
            "अनुद्धतः = अन् (not) + उद्धतः (arrogant): not arrogant.",
            "Negative अ- → अन्- before a vowel: अन् + उद्धत = अनुद्धत.",
            teaches="The negative prefix अ- takes a न् before a vowel, so अन् + उद्धत joins as अनुद्धत."),
        mcq("discriminate", 3, "What does न ब्रूयात् convey?",
            ("He should not say",
             "ब्रूयात् is the 'should' form of √ब्रू; with न it forbids."),
            [("He did not say", "ब्रूयात् is not a past form."),
             ("He will not say", "ब्रूयात् is not a future form."),
             ("Let them not say", "ब्रूयात् is singular.")],
            "न ब्रूयात् केवलं नाम = he should not utter the bare name.",
            "-यात् / -एत् verb with न = a prohibition."),
        order(4, "Put four of the second line's descriptions in the order of the verse.",
              ["अभेद्यः", "अनुद्धतः", "सूनृतः", "प्रियदर्शनः"],
              "The line gives unshakable, not arrogant, (a doubtful word), truthful, pleasant to look at.",
              "अभेद्यः → अनुद्धतः → सूनृतः → प्रियदर्शनः.", role="apply"),
        mcq("transfer", 5,
            "By the pattern of प्रियदर्शनः, an invented word प्रियभाषणः describes whom?",
            ("One whose speech is pleasant",
             "प्रिय (pleasant) + भाषण (speech), used for the person, like प्रियदर्शनः."),
            [("The speech itself", "The compound names the person who has it."),
             ("One who dislikes speaking", "प्रिय is pleasant, not disliked."),
             ("One who shows a pleasant face", "That would be प्रियमुखः (pleasant-faced), not प्रियभाषणः.")],
            "प्रियदर्शनः = pleasant to look at; प्रियभाषणः = pleasant in speech.",
            "प्रिय + noun = one with pleasant [that thing].",
            teaches="प्रिय + a noun describes the person who has that thing pleasant."),
    ],
}

# ---------------------------------------------------------------- unit 8
AUTHORED["8"] = {
    "title": "बहुश्रुतः कालवेदी",
    "question": "What qualities does the verse list, and how does he treat the helpless and the sick?",
    "rule": ("बहुश्रुतः कालवेदी ज्ञातग्रन्थः अर्थशास्त्रवित्; अनाथान् रोगिणः पुत्रवत् समुपाचरेत् = "
             "much learned, knowing the right time, knowing the texts and the meaning of treatises; "
             "he should tend the helpless and the sick as a son."),
    "limits": ("अर्थशास्त्रवित् may also be read as 'knower of the Arthaśāstra'; the meaning "
               "'of the treatises' is followed and no question rests on it. कालवेदी is kept "
               "literal (knower of the right time)."),
    "explain_hi": ("पहली पंक्ति में चार गुण हैं: बहुश्रुत (बहुत सुना-पढ़ा), कालवेदी (समय को जानने "
                   "वाला), ज्ञातग्रन्थ (ग्रन्थ जाने हुए) और अर्थशास्त्रवित् (शास्त्रों का अर्थ जानने "
                   "वाला)। दूसरी पंक्ति में सेवा का भाव है: जो असहायों और रोगियों की ‘पुत्रवत्’, पुत्र के "
                   "समान, देखभाल करे। ‘ज्ञातग्रन्थोऽर्थ...’ में विसर्ग ‘ओ’ बनकर आगे के ‘अ’ का लोप "
                   "(ऽ) करता है।"),
    "hook": "बहुश्रुत · कालवेदी · ग्रन्थ-ज्ञाता · शास्त्रार्थवित्; रोगियों की पुत्र के समान सेवा।",
    "core": True,
    "questions": [
        mcq("pretest", 0,
            "How should he tend the helpless and the sick, according to the second line?",
            ("As he would a son",
             "पुत्रवत् means 'like a son'."),
            [("As he would a king", "A king is the comparison for the teacher, not here."),
             ("As he would a stranger", "A stranger is not mentioned."),
             ("As he would a master", "A master is not mentioned.")],
            "He should tend them like a son (पुत्रवत् समुपाचरेत्).",
            "पुत्रवत् = like a son."),
        match(1, "Match each word to its meaning.",
              [["बहुश्रुतः", "much learned"], ["कालवेदी", "knowing the right time"],
               ["ज्ञातग्रन्थः", "having known the texts"], ["रोगिणः", "the sick (plural object)"]],
              "Three are qualities from the first line; the last is who is tended.",
              "बहुश्रुतः = much learned; कालवेदी = knowing the right time; ज्ञातग्रन्थः = having known the texts; रोगिणः = the sick."),
        mcq("extend", 2, "Which is the right split of ज्ञातग्रन्थोऽर्थशास्त्रवित्?",
            ("ज्ञातग्रन्थः + अर्थशास्त्रवित्",
             "A visarga after अ becomes ो before अ, and the अ is dropped (ऽ)."),
            [("ज्ञातग्रन्थ + ओर्थशास्त्रवित्", "ओर्थ... is not a word."),
             ("ज्ञातग्रन्थो + थशास्त्रवित्", "थशास्त्रवित् is not a word."),
             ("ज्ञातग्रन्थ + उ + अर्थशास्त्रवित्", "There is no separate उ in the verse.")],
            "ज्ञातग्रन्थः (visarga) + अर्थशास्त्रवित् join as ज्ञातग्रन्थोऽर्थशास्त्रवित्.",
            "-अः + अ- → -ो ऽ-: the visarga turns into ो and the अ of the next word is dropped.",
            teaches="A final -अः before अ becomes -ो, and the next अ is written as the sign ऽ."),
        mcq("discriminate", 3, "Which is the right split of यश्च?",
            ("यः + च",
             "A visarga before च becomes श्: यः + च = यश्च; यः is 'who'."),
            [("यशः + च", "That would join as यशश्च."),
             ("यश् + च", "यश् is not a word here."),
             ("य + श्च", "श्च is not a word.")],
            "यश्च = यः (who) + च (and).",
            "visarga + च → श्च: यः + च = यश्च."),
        order(4, "Put the four qualities of the first line in the order of the verse.",
              ["बहुश्रुतः", "कालवेदी", "ज्ञातग्रन्थः", "अर्थशास्त्रवित्"],
              "The line gives: much learned, knower of time, knower of texts, knower of the meaning of treatises.",
              "बहुश्रुतः → कालवेदी → ज्ञातग्रन्थः → अर्थशास्त्रवित्.", role="apply"),
        mcq("transfer", 5,
            "By the pattern of कालवेदी, an invented word ऋतुवेदी describes whom?",
            ("One who knows the seasons",
             "ऋतु (season) + वेदी (knower), like काल + वेदी."),
            [("One who makes the seasons", "वेदी is a knower, not a maker."),
             ("One who fears the seasons", "Nothing in the pattern says fear."),
             ("One who is known by the seasons", "वेदी is the knower, not the known.")],
            "कालवेदी = knower of the right time; ऋतुवेदी = knower of the seasons.",
            "noun + वेदी = knower of that noun.",
            teaches="noun + वेदी describes one who knows it."),
    ],
}

# ---------------------------------------------------------------- unit 9
AUTHORED["9"] = {
    "title": "गुरुणा समनुज्ञातः",
    "question": "Who obtains the name 'physician', and who is described next?",
    "rule": ("गुरुणा समनुज्ञातः स भिषक्शब्दम् अश्नुते = authorised by the teacher, he obtains "
             "the name 'bhiṣak' (physician). यः तु केवलशास्त्रज्ञः कर्मसु अपरिनिष्ठितः = but he who "
             "knows only the treatise and is not established in practice ..."),
    "limits": ("The sentence runs into the next unit; the second half only introduces the "
               "bookish man and says nothing here about what happens to him."),
    "explain_hi": ("पहली पंक्ति: गुरु से अनुमति मिलने पर ही वह ‘भिषक्’ (वैद्य) नाम पाता है; "
                   "‘गुरुणा’ (-णा) से पता चलता है कि अनुमति देने वाला गुरु है। दूसरी पंक्ति एक "
                   "दूसरे व्यक्ति से शुरू होती है: ‘यस्तु’ यानी ‘परन्तु जो’, केवल शास्त्र जानता है "
                   "और कर्मों (व्यावहारिक कार्य) में निपुण नहीं। वाक्य यहाँ पूरा नहीं होता; परिणाम "
                   "अगले श्लोक में है।"),
    "hook": "गुरु की अनुमति से ‘भिषक्’ नाम · परन्तु केवल शास्त्र जाने, कर्म में कच्चा ... (आगे)।",
    "core": True,
    "questions": [
        mcq("pretest", 0,
            "Who obtains the name 'physician' (bhiṣak), according to the first line?",
            ("The one authorised by the teacher",
             "गुरुणा समनुज्ञातः says he is authorised by the teacher."),
            [("The one who has read the most books",
              "Reading is not the condition named."),
             ("The one chosen by the king",
              "The king is not mentioned."),
             ("The one who treats the most patients",
              "Number of patients is not mentioned.")],
            "He obtains the name when the teacher has authorised him.",
            "गुरुणा समनुज्ञातः → भिषक्शब्दम् अश्नुते."),
        match(1, "Match each word to its meaning.",
              [["गुरुणा", "by the teacher"], ["समनुज्ञातः", "authorised"],
               ["अश्नुते", "obtains"], ["भिषक्शब्दम्", "the name 'physician'"]],
              "These four words make the first line.",
              "गुरुणा = by the teacher; समनुज्ञातः = authorised; अश्नुते = obtains; भिषक्शब्दम् = the name 'physician'."),
        mcq("extend", 2, "In गुरुणा समनुज्ञातः, who gives the permission, and how can you tell?",
            ("The teacher: गुरुणा ends in -णा, 'by'",
             "-णा is the instrumental: the one by whom it is done."),
            [("The pupil: समनुज्ञातः shows he is the giver",
              "समनुज्ञातः is 'authorised', so the pupil receives it."),
             ("The pupil gives it: -णा on गुरुणा shows the giver is the pupil",
              "गुरुणा names the teacher; -णा is 'by', so the teacher gives it."),
             ("The teacher, but -णा means 'to'",
              "-णा is 'by', not 'to'; 'to' would be गुरवे.")],
            "The permission comes from the teacher (गुरुणा, 'by the teacher').",
            "-णा / -एन (instrumental) names the one by whom an action is done.",
            teaches="A noun in the instrumental (-णा, -एन) names the one by whom something is done: 'by'."),
        mcq("discriminate", 3, "Which is the right split of यस्तु?",
            ("यः + तु",
             "A visarga before त becomes स्: यः + तु = यस्तु."),
            [("यस् + तु", "यस् is not the word; it is यः."),
             ("य + स्तु", "स्तु is not a word here."),
             ("यस्य + तु", "That would be written यस्य तु.")],
            "यस्तु = यः (who) + तु (but).",
            "visarga + त → स्त: यः + तु = यस्तु."),
        order(4, "Put the parts of the first line in the order of the verse.",
              ["गुरुणा", "समनुज्ञातः", "सः", "भिषक्शब्दम्", "अश्नुते"],
              "The line runs: by the teacher, authorised, he, the name 'physician', obtains.",
              "गुरुणा → समनुज्ञातः → सः → भिषक्शब्दम् → अश्नुते.", role="apply"),
        mcq("transfer", 5,
            "An invented phrase reads वैद्येन समनुज्ञातः शिष्यः. By whom is the pupil permitted?",
            ("By the physician",
             "-एन marks the one by whom, as -णा does in गुरुणा."),
            [("For the physician", "'For' would be a different ending."),
             ("Of the physician", "'Of' would be a different ending."),
             ("The physician himself is permitted", "वैद्येन is not the one permitted.")],
            "The instrumental names who gives the permission.",
            "X (instrumental) + समनुज्ञातः = permitted by X.",
            teaches="The instrumental (-णा, -एन) tells you who gives the permission."),
    ],
}

# ---------------------------------------------------------------- unit 10
AUTHORED["10"] = {
    "title": "स मुह्यत्यातुरं प्राप्य",
    "question": "What happens to the man who knows only the treatise, and how is it compared?",
    "rule": ("सः आतुरं प्राप्य प्राप्य मुह्यति, भीरुः इव आहवम् = each time he reaches a patient he "
             "becomes bewildered, like a timid man at a battle. यः शास्त्रविवर्जितः धार्ष्ट्यात् कर्म "
             "कुरुते = he who, devoid of the treatise, acts out of boldness ..."),
    "limits": ("'He' in the first line is the man of the previous unit. The second line starts "
               "a new sentence that is finished in the next unit; nothing is said here about "
               "its result."),
    "explain_hi": ("पिछली इकाई का ‘केवल शास्त्र जानने वाला’ यहाँ ‘सः’ है। वह हर बार रोगी के पास "
                   "पहुँचकर घबरा जाता है (‘प्राप्य प्राप्य’ का दोहराव ‘हर बार’ बताता है), जैसे डरपोक "
                   "आदमी युद्ध में पहुँचकर। ‘प्राप्य’ में उपसर्ग ‘प्र’ है, इसलिए ‘करके’ वाला रूप -त्वा नहीं, -य "
                   "है। दूसरी पंक्ति में ‘जो’ शास्त्र के बिना ढिठाई से कर्म करता है; उसका फल आगे के श्लोक में है।"),
    "hook": "हर बार रोगी के पास घबराता, डरपोक का युद्ध की तरह · शास्त्र बिना ढिठाई से कर्म ... (आगे)।",
    "core": False,
    "questions": [
        mcq("pretest", 0,
            "The man who knows only the treatise reaches a patient. What does the first line say happens?",
            ("He becomes bewildered",
             "मुह्यति means he becomes bewildered."),
            [("He grows confident", "The verse says the opposite."),
             ("He feels pity", "Pity is not mentioned."),
             ("He becomes angry", "Anger is not mentioned.")],
            "Each time he reaches a patient he is bewildered, like a timid man at a battle.",
            "आतुरं प्राप्य मुह्यति = reaching a patient, he is bewildered."),
        match(1, "Match each word to its meaning.",
              [["मुह्यति", "becomes bewildered"], ["आतुरम्", "patient"],
               ["भीरुः", "timid man"], ["आहवम्", "battle"]],
              "These words make the comparison and its two sides.",
              "मुह्यति = becomes bewildered; आतुरम् = patient; भीरुः = timid man; आहवम् = battle."),
        mcq("extend", 2, "Which is the right split of भीरुरिवाहवम्?",
            ("भीरुः + इव + आहवम्",
             "A visarga after उ turns into र् before a vowel; इव + आहवम् joins as इवाहवम्."),
            [("भीरुः + एव + आहवम्", "एव would give भीरुरेवाहवम्, and it means 'only', not 'like'."),
             ("भीरु + रिवा + हवम्", "रिवा and हवम् are not words here."),
             ("भीरुः + इव + ऊहवम्", "The last word is आहवम् (battle), not ऊहवम्.")],
            "भीरुरिवाहवम् = भीरुः (timid man) + इव (like) + आहवम् (battle).",
            "visarga after उ + vowel → र्; अ + आ → आ.",
            teaches="A final visarga after उ becomes र् before a vowel, and अ + आ joins as आ."),
        mcq("discriminate", 3, "Why does प्राप्य end in -य and not in -त्वा?",
            ("It has the prefix प्र-, so it takes -य",
             "A 'having done' word takes -त्वा without a prefix and -य with one."),
            [("Because it is a future form, which always ends in -य",
              "It is a 'having done' form, not a future."),
             ("Because the word is repeated as प्राप्य प्राप्य and doubles",
              "Repetition does not change the ending; it only means 'each time'."),
             ("Because it is a passive form, which takes -य",
              "It is not passive; it is 'having reached'.")],
            "प्र + √आप् + -य = प्राप्य, 'having reached'.",
            "without prefix: -त्वा; with prefix: -य."),
        order(4, "Put the parts of the first line in the order of the verse.",
              ["सः मुह्यति", "आतुरं प्राप्य प्राप्य", "भीरुः इव आहवम्"],
              "He is bewildered; on reaching a patient each time; like a timid man at a battle.",
              "सः मुह्यति → आतुरं प्राप्य प्राप्य → भीरुः इव आहवम्.", role="apply"),
        mcq("transfer", 5,
            "To say 'having known' with the prefix वि- on the root √ज्ञा, which form is right?",
            ("विज्ञाय",
             "With a prefix the 'having done' form ends in -य: वि + ज्ञा → विज्ञाय."),
            [("विज्ञात्वा", "-त्वा is used without a prefix."),
             ("विज्ञायते", "That is a passive verb, not 'having known'."),
             ("विज्ञाता", "That means one who knows, not 'having known'.")],
            "The rule of प्राप्य carries over to other prefixed roots.",
            "prefix + root + -य = having done (with prefix).",
            teaches="A prefixed root forms its 'having done' word with -य, not -त्वा."),
    ],
}

# ---------------------------------------------------------------- unit 11
AUTHORED["11"] = {
    "title": "हेतौ लिङ्गे प्रशमने",
    "question": "What four things about diseases are named in the second line?",
    "rule": ("हेतौ लिङ्गे प्रशमने रोगाणाम् अपुनर्भवे = in the cause, the sign, the alleviation "
             "and the non-recurrence of diseases."),
    "limits": ("The second line begins a sentence that is completed in the next unit; this "
               "unit only lists the four topics. In the first line the word चैच्छन्ति is "
               "doubtful; the translation follows 'meets with', and no question rests on it."),
    "explain_hi": ("पहली पंक्ति पिछले वाक्य का अन्त है: शास्त्र के बिना कर्म करने वाला सज्जनों "
                   "में निन्दा पाता है। ‘सत्सु’ का -सु ‘में, बीच’ बताता है। दूसरी पंक्ति में रोगों के "
                   "चार विषय हैं, सब सप्तमी में: हेतु (कारण), लिङ्ग (लक्षण), प्रशमन (शमन) और "
                   "अपुनर्भव (दोबारा न होना)। ‘ज्ञान’ शब्द यहाँ नहीं है; वह अगले श्लोक में आता है। "
                   "‘चैच्छन्ति’ का पाठ सन्दिग्ध है।"),
    "hook": "रोगों के चार विषय: हेतु · लिङ्ग · प्रशमन · अपुनर्भव।",
    "core": True,
    "questions": [
        mcq("pretest", 0,
            "Which four things about diseases does the second line name?",
            ("Cause, sign, alleviation, non-recurrence",
             "हेतौ, लिङ्गे, प्रशमने, अपुनर्भवे."),
            [("Cause, sign, price, season",
              "Price and season are not named."),
             ("Cause, name, alleviation, spread",
              "The name and the spread are not named."),
             ("Sign, dose, alleviation, season",
              "Dose and season are not named.")],
            "The line names the cause, the sign, the alleviation and the non-recurrence of diseases.",
            "हेतु, लिङ्ग, प्रशमन, अपुनर्भव."),
        match(1, "Match each word to its meaning.",
              [["हेतौ", "in the cause"], ["लिङ्गे", "in the sign"],
               ["प्रशमने", "in the alleviation"], ["अपुनर्भवे", "in the non-recurrence"]],
              "The four words are all in the 'in' form.",
              "हेतौ = in the cause; लिङ्गे = in the sign; प्रशमने = in the alleviation; अपुनर्भवे = in the non-recurrence."),
        mcq("extend", 2, "What does -सु show in सत्सु?",
            ("'Among / in', plural: among the good",
             "-सु is the locative plural ending."),
            [("'By', plural: by the good", "'By' is a different ending."),
             ("'Of', singular: of a good man", "It is plural, and not 'of'."),
             ("'To', singular: given to a good man", "It is plural, and not 'to'.")],
            "सत्सु = among the good.",
            "-सु on a plural word = 'in, among'.",
            teaches="The ending -सु makes a plural word mean 'in' or 'among' the people or things named."),
        mcq("discriminate", 3, "What does अपुनर्भवे mean, from its parts?",
            ("In non-recurrence: not coming again",
             "अ (not) + पुनः (again) + भव (coming to be)."),
            [("In repeated coming: coming again and again",
              "The negative अ- reverses it."),
             ("In a second cause: a different cause",
              "पुनः means again, not second cause."),
             ("In a sudden start: beginning at once",
              "Nothing in the word means sudden.")],
            "अपुनर्भव = a-punar-bhava: no coming again.",
            "अ- + पुनः + भव = non-recurrence."),
        order(4, "Put the four topics in the order of the verse.",
              ["हेतौ", "लिङ्गे", "प्रशमने", "अपुनर्भवे"],
              "The line gives cause, sign, alleviation, non-recurrence.",
              "हेतौ → लिङ्गे → प्रशमने → अपुनर्भवे.", role="apply"),
        mcq("transfer", 5,
            "हेतौ (from masculine हेतु) means in the cause. By the same pattern, which form means in the enemy (शत्रु)?",
            ("शत्रौ",
             "For masculine words in -उ, 'in' ends in -औ: हेतु → हेतौ, शत्रु → शत्रौ."),
            [("शत्रवे", "That is 'for the enemy'."),
             ("शत्रोः", "That is 'of the enemy'."),
             ("शत्रुम्", "That is 'the enemy' as object.")],
            "The ending of हेतौ carries over to other masculine words in -उ.",
            "masculine word in -उ + 'in' = -औ.",
            teaches="For a masculine word in -उ the 'in' form ends in -औ: हेतौ, शत्रौ."),
    ],
}

# ---------------------------------------------------------------- unit 12
AUTHORED["12"] = {
    "title": "ज्ञानं चतुर्विधं यस्य",
    "question": "Who is the best physician, and what three things are named for merit and fault?",
    "rule": ("ज्ञानं चतुर्विधं यस्य सः राजार्हः भिषक्तमः = he whose knowledge is fourfold is the "
             "best of physicians, worthy of a king. शस्त्रं शास्त्राणि सलिलं गुणदोषप्रवृत्तये = a weapon, "
             "treatises and water are for the arising of merit and fault."),
    "limits": ("The four kinds are the four topics listed in the previous unit; this verse itself "
               "does not name them. The second line continues in the next unit, so what the "
               "three things depend on is not said here."),
    "explain_hi": ("पहली पंक्ति पिछले वाक्य को पूरा करती है: जिसका ज्ञान ‘चतुर्विध’ (चार प्रकार का) है, "
                   "वह राजा के योग्य ‘भिषक्तम’ (श्रेष्ठ वैद्य) है। ‘-तम’ श्रेष्ठता बताता है। चार "
                   "प्रकार पिछली इकाई के हैं, यहाँ वे नाम से नहीं आते। दूसरी पंक्ति में तीन वस्तुएँ: शस्त्र, "
                   "शास्त्र और जल, जो गुण-दोष की उत्पत्ति के लिए हैं। इस वाक्य की बात अगली "
                   "इकाई में पूरी होती है।"),
    "hook": "चार प्रकार का ज्ञान → राजा के योग्य श्रेष्ठ वैद्य · शस्त्र, शास्त्र, जल: गुण-दोष के लिए।",
    "core": False,
    "questions": [
        mcq("pretest", 0,
            "What is said of the physician whose knowledge is fourfold?",
            ("He is the best of physicians, worthy of a king",
             "राजार्हो भिषक्तमः says exactly this."),
            [("He must serve a king for life", "Serving a king for life is not mentioned."),
             ("He should not treat the helpless", "That is not said here."),
             ("He is the youngest of the physicians", "Age is not mentioned.")],
            "The man with fourfold knowledge is best of physicians and worthy of a king.",
            "चतुर्विधं ज्ञानम् → राजार्हः भिषक्तमः."),
        match(1, "Match each word to its meaning.",
              [["ज्ञानम्", "knowledge"], ["चतुर्विधम्", "fourfold"],
               ["राजार्हः", "worthy of a king"], ["भिषक्तमः", "best physician"]],
              "These four words make the first line.",
              "ज्ञानम् = knowledge; चतुर्विधम् = fourfold; राजार्हः = worthy of a king; भिषक्तमः = best physician."),
        mcq("extend", 2, "What does -तमः add in भिषक्तमः?",
            ("'Best of': the best among physicians",
             "-तम is the superlative: the most excellent."),
            [("'A little': somewhat of a physician", "-तम does not make a diminutive."),
             ("'Without': no physician at all", "-तम does not mean 'without'."),
             ("'Former': once a physician", "-तम does not mean 'former'.")],
            "भिषक्तमः = best physician.",
            "word + -तम = the best of that kind.",
            teaches="-तम makes a word mean 'the best' of that kind: भिषक्तमः = the best physician."),
        mcq("discriminate", 3, "In चतुर्विधम्, what does -विध mean?",
            ("Kind, sort",
             "चतुर् (four) + विध (kind): fourfold."),
            [("Time", "विध does not mean time."),
             ("Cause", "विध does not mean cause."),
             ("Place", "विध does not mean place.")],
            "चतुर्विधम् = of four kinds.",
            "number + विध = so many kinds."),
        order(4, "Put the three things of the second line in the order of the verse.",
              ["शस्त्रम्", "शास्त्राणि", "सलिलम्"],
              "The line names a weapon, then treatises, then water.",
              "शस्त्रम् → शास्त्राणि → सलिलम्.", role="apply"),
        mcq("transfer", 5,
            "By the pattern of चतुर्विधम्, what does an invented षड्विधम् mean?",
            ("Of six kinds",
             "षट् (six) + विध (kind) = sixfold, as चतुर् (four) + विध = fourfold."),
            [("Of six places", "विध is 'kind', not place."),
             ("Six times over", "विध is 'kind', not a repeat."),
             ("The sixth one", "That would be a different word.")],
            "The pattern of चतुर्विधम् carries over to other numbers.",
            "number + विध = that many kinds.",
            teaches="number + विध names how many kinds there are: चतुर्विध = four kinds, षड्विध = six kinds."),
    ],
}

# ---------------------------------------------------------------- unit 13
AUTHORED["13"] = {
    "title": "प्रदीपभूतं शास्त्रं हि",
    "question": "How is the treatise compared, and what is the wide intellect called?",
    "rule": ("प्रज्ञां बाहुश्रुत्येन बृंहयेत् = he should strengthen his intellect by wide learning. "
             "प्रदीपभूतं शास्त्रम्, दर्शनं विपुला मतिः = the treatise is like a lamp, and a wide "
             "intellect is the sight."),
    "limits": ("The first word of the first line is damaged; the reading 'depending on the "
               "vessel' is conjectural, so nothing is built on it or on how this line joins "
               "the previous unit."),
    "explain_hi": ("पहली पंक्ति का पहला शब्द बिगड़ा हुआ है (सुझाया पाठ ‘पात्राश्रयीणि’ केवल अनुमान है), "
                   "इसलिए केवल बाकी हिस्सा पढ़ें: ‘बाहुश्रुत्येन’ (-एन, ‘से’) साधन बताता है, यानी बहुत "
                   "पढ़ने-सुनने से ‘प्रज्ञा’ (बुद्धि) को बढ़ाए। दूसरी पंक्ति में दो उपमाएँ: शास्त्र दीपक के "
                   "समान है (‘प्रदीपभूतम्’) और विशाल बुद्धि ‘दर्शन’ (दृष्टि) है।"),
    "hook": "शास्त्र = दीपक · विशाल बुद्धि = दृष्टि; बहुश्रुतता से प्रज्ञा बढ़ाए।",
    "core": False,
    "questions": [
        mcq("pretest", 0,
            "In the second line the treatise is compared to what?",
            ("A lamp",
             "प्रदीपभूतं शास्त्रम् = the treatise is like a lamp."),
            [("A mirror", "A mirror is not mentioned."),
             ("A road", "A road is not mentioned."),
             ("A fire", "A fire is not mentioned.")],
            "The treatise is like a lamp (प्रदीप).",
            "प्रदीपभूतं शास्त्रम् = the treatise is like a lamp."),
        match(1, "Match each word to its meaning.",
              [["प्रदीपभूतम्", "like a lamp"], ["दर्शनम्", "sight"],
               ["विपुला", "wide"], ["मतिः", "intellect"]],
              "These words make up the second line's two images.",
              "प्रदीपभूतम् = like a lamp; दर्शनम् = sight; विपुला = wide; मतिः = intellect."),
        mcq("extend", 2, "By what means is the intellect to be strengthened, and which word shows it?",
            ("By wide learning: बाहुश्रुत्येन ends in -एन, 'by'",
             "-एन is the instrumental: the means."),
            [("By a king's order: बाहुश्रुत्येन means 'of a king'",
              "बाहुश्रुत्येन is not about a king."),
             ("For wide learning: बाहुश्रुत्येन ends in a 'for' ending",
              "-एन is 'by', not 'for'."),
             ("In wide learning: बाहुश्रुत्येन ends in an 'in' ending",
              "-एन is 'by', not 'in'.")],
            "प्रज्ञां बाहुश्रुत्येन बृंहयेत् = strengthen the intellect by wide learning.",
            "-एन (instrumental) = by means of.",
            teaches="The instrumental (-एन) names the means by which something is done."),
        mcq("discriminate", 3, "Which pairing does the second line make?",
            ("Treatise = lamp; wide intellect = sight",
             "प्रदीपभूतं शास्त्रम् and दर्शनं विपुला मतिः."),
            [("Treatise = sight; wide intellect = lamp",
              "This swaps them."),
             ("Treatise = lamp; wide intellect = fire",
              "The line says the intellect is the sight, not a fire."),
             ("Lamp = sight; treatise = wide intellect",
              "The line does not equate those.")],
            "The treatise is the lamp, and the wide intellect is the sight.",
            "शास्त्रम् = प्रदीप; विपुला मतिः = दर्शनम्."),
        order(4, "Put these items in the order of the second line.",
              ["प्रदीपभूतम्", "शास्त्रम्", "दर्शनम्", "विपुला मतिः"],
              "The line gives: like a lamp, the treatise, sight, wide intellect.",
              "प्रदीपभूतम् → शास्त्रम् → दर्शनम् → विपुला मतिः.", role="apply"),
        mcq("transfer", 5,
            "An invented line reads नौकाभूतः गुरुः. By the pattern of प्रदीपभूतम्, what does it say?",
            ("The teacher is like a boat",
             "-भूत after a noun, as in प्रदीपभूतम्, gives 'being like' it."),
            [("The teacher is a boat-maker", "-भूत does not make a maker."),
             ("The boat is like a teacher", "The teacher is the one compared."),
             ("The teacher has left the boat", "Nothing here means leaving.")],
            "प्रदीपभूतम् = like a lamp; नौकाभूतः = like a boat.",
            "noun + -भूत = being like that noun.",
            teaches="noun + -भूत makes a comparison: 'being like' it."),
    ],
}

# ================================================================== NOTES
NOTES_HI = {
    "1": "‘अथातः’ = अथ + अतः (अ + अ → आ); शब्द-रूप वही छपा है। इकाई सूत्र-रूप आरम्भ-वाक्य है (गद्य); कोई पाठ-संदेह नहीं, विश्वास उच्च।",
    "2": "विश्वास: निम्न। पहली पंक्ति के ‘गुरुरुक्तः’ का अन्वय अनिश्चित है: ‘गुरुः उक्तः’ (गुरु कहा गया) या ‘गुरूक्तः’ (गुरु द्वारा कहा गया)। पुस्तक के अपने हिन्दी और अंग्रेज़ी यह अलग-अलग लेते हैं कि सूची गुरु की है या शिष्य की; इस कार्ड में यह तय नहीं किया गया। ‘अभियुक्तः’ को ‘परिश्रमी’ या ‘जुड़ा हुआ’ दोनों पढ़ सकते हैं। ‘ऋज्वास्य...’ में ऋजु + आस्य → ऋज्वास्य संधि जाँची गई। इकाई अगले श्लोक की ओर चलती है।",
    "3": "विश्वास: उच्च। ‘षण्मासानुषितः’ को षट्-मास-अनुषितः या षण्-मासान् उषितः दोनों तरह पढ़ा जा सकता है; अर्थ वही रहता है। गुरु का नाम श्लोक में नहीं है। ‘कला’ का अर्थ ‘कुशलता’ लिया गया है, ‘कलाएँ’ भी सम्भव है। ‘जितद्वंद्वो’ = जितद्वन्द्वः (विसर्ग → ओ, धीरः के घोष ‘ध’ से पहले)।",
    "4": "विश्वास: मध्यम। ‘गतो यावदन्तम्’ को ‘अन्त तक पहुँचा हुआ’ भी पढ़ा जा सकता है। ‘तन्त्रार्थकर्मणाम्’ के तीन पदों को एक वाक्यांश (‘तन्त्र के अर्थ-कर्म’) भी पढ़ा जा सकता है। ‘राहुदर्शन’ शाब्दिक अनुवाद है; पुस्तक इसे ग्रहण मानती है। दूसरी पंक्ति का ‘न’ अगले श्लोक के ‘पठेत्’ से पूरा होता है। ‘नाकाल...’ = न + अकाल... (अ + अ → आ)।",
    "5": "विश्वास: मध्यम। ‘पञ्चदश्याम् अचन्द्रायाम्’ में पुस्तक अमावस्या लेती है, पर पाठ में ‘अमावस्या’ नहीं है; अंग्रेज़ी टिप्पणी का सुझाव ‘पन्द्रहवीं तिथि और चन्द्रहीन रात’ भी है, इसलिए इस पर प्रश्न नहीं बना। ‘नाविच्छिन्नपदम्’ में ‘न अविच्छिन्न’ या ‘न विच्छिन्न’ दोनों सम्भव हैं (पाठ-दोष सम्भव); अपरिवर्तित। ‘नीचकैः’ को नीच + क प्रत्यय वाला रूप माना गया है। ‘नात्युच्च...’ = न + अति + उच्च (इ → य्)।",
    "6": "विश्वास: मध्यम। ‘हितान्यतमम्’: पुस्तक का विभाजन ‘हितान् यतमम्’ मान्य शब्द-विभाजन नहीं है; ‘हित + अन्यतमम्’ (हितैषियों में से एक) माना गया है, अर्थ सन्दिग्ध। सुप्त एवास्मिन् = सुप्तः + एव + अस्मिन् (अः + स्वर → अ + स्वर); डेटा इसे सुप्ते (सप्तमी) लेता है; अर्थ वही रहता है।",
    "7": "विश्वास: मध्यम। (१) ‘न साध्वपि विनोदयेत्’: कर्म स्पष्ट नहीं; हिन्दी और अंग्रेज़ी में अलग-अलग लिया गया है। (२) ‘स्तब्धः’ छपा है, पर ‘अनुद्धतः’ और अन्य गुणों से मेल नहीं खाता; ‘ऽस्तब्धः’ (अस्तब्धः) का अवग्रह खोया लगता है। अनुवाद ‘अस्तब्धः’ लेता है, पर कोई प्रश्न इस पर नहीं टिका। डेटा का हिन्दी ‘अडिग’ और अंग्रेज़ी ‘gentle’ पुराने पाठ पर आधारित हो सकते हैं।",
    "8": "विश्वास: मध्यम। ‘अर्थशास्त्रवित्’ का अर्थ ‘अर्थशास्त्र का जानकार’ भी हो सकता है; ‘शास्त्रों के अर्थ का जानकार’ लिया गया। ‘कालवेदी’ शाब्दिक रखा है। ‘ज्ञातग्रन्थोऽर्थ...’ = ज्ञातग्रन्थः + अर्थ... (विसर्ग → ओ, अ का लोप ऽ)। ‘यश्च’ = यः + च (विसर्ग → श्)।",
    "9": "विश्वास: उच्च। वाक्य अगली इकाई (‘स मुह्यति...’) में चलता है। ‘यस्तु’ = यः + तु (विसर्ग → स्)। ‘भिषक्शब्द’ = ‘भिषक्’ नाम। ‘कर्म’ = व्यावहारिक कार्य।",
    "10": "विश्वास: उच्च। वाक्य अगली इकाई में चलता है (‘स सत्सु गर्हाम्...’)। ‘प्राप्य प्राप्य’ दोहराव = हर बार। ‘भीरुरिवाहवम्’ = भीरुः + इव + आहवम् (विसर्ग → र्; अ + आ → आ)। ‘धार्ष्ट्यात्’ = ढिठाई/दुस्साहस से।",
    "11": "विश्वास: निम्न। ‘चैच्छंति’ संदिग्ध है: बहुवचन है जबकि कर्ता एकवचन है, और च + इच्छ- से ‘चेच्छ-’ बनता, ‘चैच्छ-’ नहीं। अनुवाद ‘च + ऋच्छति’ (पाता है) लेता है; ‘चार्हति’ (योग्य है) भी सम्भव। कोई प्रश्न इस पर नहीं टिका। दूसरी पंक्ति नया वाक्य शुरू करती है जो अगली इकाई में पूरा होता है।",
    "12": "विश्वास: उच्च। पहली पंक्ति पिछले वाक्य (हेतु, लिङ्ग, प्रशमन, अपुनर्भव) को पूरा करती है; दूसरी पंक्ति का वाक्य अगली इकाई में चलता है। ‘राजार्हो’ = राजार्हः (विसर्ग → ओ)। ‘गुणदोषप्रवृत्तये’ = गुण-दोष की उत्पत्ति के लिए।",
    "13": "विश्वास: निम्न। पहला शब्द ‘पात्राश्रक्षीण्यतः’ बिगड़ा है; सुझाया पाठ ‘पात्राश्रयीण्यतः’ (पात्र पर आश्रित) केवल अनुमान है, कोई पाठ नहीं बदला। ‘बाहुश्रुत्य’ बहुश्रुत से बना है। दूसरी पंक्ति की दो उपमाएँ: शास्त्र = दीप, विशाल बुद्धि = दृष्टि।",
}

# ================================================================== AIDS
AIDS = {
    "1": {
        "chunks": "अथातः | शिष्योपनयनीयम् अध्यायं | व्याख्यास्यामः ॥",
        "sandhi": "अ + अ → आ: अथ + अतः → अथातः · -म् + अ: शिष्योपनयनीयम् + अध्यायम् → शिष्योपनयनीयमध्यायम् (म् अगले स्वर से जुड़ गया)।",
        "anchors": "व्याख्या ← वि + आ + ख्या (खोलकर कहना) · अध्याय ← अधि + √इ (पढ़ना; पढ़ाई का भाग) · उपनयन = पास ले जाना (उप + नयन)।",
    },
    "2": {
        "chunks": "गुरुरुक्तोऽभियुक्तोऽतियुक्तो धीस्मृतिपाटवैः ‖ ऋज्वास्यनासानयनः तनुस्निग्धत्वक्छविः ॥",
        "sandhi": "विसर्ग → र् (उ के बाद, स्वर से पहले): गुरुः + उक्तः → गुरुरुक्तः · उ + आ → वा: ऋजु + आस्य → ऋज्वास्य · विसर्ग → ओ और अ का लोप (ऽ): उक्तः + अभियुक्तः → उक्तोऽभियुक्तः, अभियुक्तः + अतियुक्तः → अभियुक्तोऽतियुक्तः।",
        "pegs": "मेरा बनाया चित्र: तीन दीये (धी, स्मृति, पाटव), और एक चेहरे पर सीधी आँखें, नाक और मुख।",
    },
    "3": {
        "diagram": {"groups": [
            {"label": "पहली पंक्ति",
             "items": ["ब्रह्मचारी", "जितद्वन्द्वः", "धीरः", "सुचरितः", "स्थिरः"]},
            {"label": "दूसरी पंक्ति",
             "items": ["षण्मासानुषितः", "शक्तः", "लज्जा", "शौच", "कला"]}]},
        "frame": "कौन: ब्रह्मचारी · कैसा: द्वन्द्व जीता, धीर, सदाचारी, स्थिर · अवधि: छह मास · क्षमता: समर्थ · युक्त: लज्जा, शौच, कला।",
        "chunks": "ब्रह्मचारी | जितद्वन्द्वः | धीरः | सुचरितः | स्थिरः ‖ षण्मासानुषितः | शक्तः | लज्जाशौचकलान्वितः ॥",
        "letters": "ब्र-ज-धी-सु-स्थि (पहली पंक्ति): ब्रह्मचारी, जित, धीर, सुचरित, स्थिर; फिर ष-श-ल-शौ-क (दूसरी): षण्मास, शक्त, लज्जा, शौच, कला।",
    },
    "4": {
        "diagram": {"groups": [
            {"label": "पहली पंक्ति",
             "items": ["शिष्यः अध्याप्यः", "यावदन्तम्", "तन्त्र · अर्थ · कर्म"]},
            {"label": "दूसरी पंक्ति: ‘न’ के साथ अवसर",
             "items": ["अकालविद्युत्स्तनिते", "भूकम्पे", "राहुदर्शने"]}]},
        "chunks": "शिष्यः अध्याप्यः | गतः यावदन्तम् | तन्त्रार्थकर्मणाम् ‖ न अकालविद्युत्स्तनिते | भूकम्पे | राहुदर्शने ॥",
        "sandhi": "अ + अ → आ: न + अकाल... → नाकाल... · विसर्ग → ओ और ऽ: शिष्यः + अध्याप्यः → शिष्योऽध्याप्यः।",
        "pegs": "मेरा बनाया चित्र: कड़कती बिजली, हिलती धरती और काला ग्रहण: तीन चेतावनी-बोर्ड।",
    },
    "5": {
        "chunks": "पञ्चदश्याम् अचन्द्रायाम् | परोक्षे वा गुरोः पठेत् ‖ न अविच्छिन्नपदम् | न अतिमन्दम् | न अत्युच्चनीचकैः ॥",
        "sandhi": "इ + अलग स्वर → य्: अति + उच्च → अत्युच्च; न + अति → नाति; अ + अ → आ।",
        "contrast": "उच्च (ऊँचा स्वर) ↔ नीच (नीचा स्वर): दोनों अति-वाले दोष, अत्युच्चनीचकैः में एक साथ।",
    },
    "6": {
        "diagram": {"groups": [
            {"label": "सेवा",
             "items": ["आचार्यं पर्युपासीत", "राजवत्"]},
            {"label": "सोना और उठना",
             "items": ["शयीत", "उत्तिष्ठेत पूर्वतः"]}]},
        "chunks": "आचार्यं पर्युपासीत राजवत् ‖ शयीत सुप्त एव अस्मिन् | उत्तिष्ठेत अस्य पूर्वतः ॥",
        "seesaw": "शयीत (गुरु के बाद सोए) ↔ उत्तिष्ठेत पूर्वतः (गुरु से पहले उठे)।",
        "pegs": "मेरा बनाया चित्र: राजा के सामने झुका हुआ सेवक; रात को राजा के बाद दीया बुझाता, सुबह पहले जलाता।",
    },
    "7": {
        "chunks": "न ब्रूयात् केवलं नाम | न साध्वपि विनोदयेत् ‖ अभेद्यः अनुद्धतः (स्तब्धः: संदिग्ध) सूनृतः प्रियदर्शनः ॥",
        "sandhi": "अन् + उ: अन् + उद्धतः → अनुद्धतः (न् अगले स्वर से जुड़ा) · विसर्ग → ओ और ऽ: अभेद्यः + अनुद्धतः → अभेद्योऽनुद्धतः।",
        "anchors": "सूनृत = सत्य और प्रिय वाणी (डेटा का अर्थ) · प्रिय + दर्शन = देखने में प्रिय · अभेद्य = जिसे भेदा न जा सके।",
        "puns": "केवल सुनने की सहायता: ‘सूनृत’ ≈ ‘सुन-ऋत’ (सुनने में मीठा, सच्चा)।",
    },
    "8": {
        "diagram": {"groups": [
            {"label": "पहली पंक्ति: गुण",
             "items": ["बहुश्रुतः", "कालवेदी", "ज्ञातग्रन्थः", "अर्थशास्त्रवित्"]},
            {"label": "दूसरी पंक्ति: सेवा",
             "items": ["अनाथान्", "रोगिणः", "पुत्रवत्", "समुपाचरेत्"]}]},
        "chunks": "बहुश्रुतः | कालवेदी | ज्ञातग्रन्थः | अर्थशास्त्रवित् ‖ अनाथान् रोगिणः यः च | पुत्रवत् समुपाचरेत् ॥",
        "sandhi": "विसर्ग → ओ और ऽ: ज्ञातग्रन्थः + अर्थ... → ज्ञातग्रन्थोऽर्थ... · विसर्ग + च → श्च: यः + च → यश्च।",
        "letters": "ब-का-ज्ञा-अर्थ: बहुश्रुत, कालवेदी, ज्ञातग्रन्थ, अर्थशास्त्रवित्।",
    },
    "9": {
        "frame": "कौन: जो गुरु से अनुमति पाए · क्या पाता है: ‘भिषक्’ नाम · दूसरा व्यक्ति: ‘यस्तु’: जो केवल शास्त्र जाने, कर्म में कच्चा (वाक्य आगे)।",
        "chunks": "गुरुणा समनुज्ञातः | सः भिषक्शब्दम् अश्नुते ‖ यः तु केवलशास्त्रज्ञः | कर्मसु अपरिनिष्ठितः ॥",
        "sandhi": "विसर्ग → स्: यः + तु → यस्तु · म् + अ: भिषक्शब्दम् + अश्नुते → भिषक्शब्दमश्नुते।",
        "contrast": "गुरु की अनुमति वाला (भिषक् नाम पाता है) ↔ केवल शास्त्रज्ञ, कर्म में अपरिनिष्ठित (वाक्य आगे चलता है)।",
    },
    "10": {
        "diagram": {"steps": [
            "सः (पिछली इकाई का केवल-शास्त्रज्ञ)",
            "मुह्यति",
            "आतुरं प्राप्य प्राप्य",
            "भीरुः इव आहवम् (उपमा)"]},
        "chain": {"steps": ["सः मुह्यति", "आतुरं प्राप्य प्राप्य", "भीरुः इव आहवम्"]},
        "sandhi": "विसर्ग → र्: भीरुः + इव → भीरुरिव · अ + आ → आ: इव + आहवम् → इवाहवम्।",
        "anchors": "प्राप्य = प्र + आप् + य (उपसर्ग वाला ‘करके’ रूप) · मुह्यति ← मोह।",
        "pegs": "मेरा बनाया चित्र: युद्ध-भूमि के द्वार पर काँपता सिपाही; वैद्य के हाथ में बस एक पोथी।",
    },
    "11": {
        "diagram": {"groups": [
            {"label": "रोगों के चार विषय",
             "items": ["हेतौ", "लिङ्गे", "प्रशमने", "अपुनर्भवे"]}]},
        "chunks": "स सत्सु गर्हाम् आप्नोति | वधं च ... राजतः ‖ हेतौ | लिङ्गे | प्रशमने | रोगाणाम् अपुनर्भवे ॥",
        "letters": "हे-लि-प्र-अ: हेतु, लिङ्ग, प्रशमन, अपुनर्भव।",
        "anchors": "प्रशमन ← शम (शान्त होना) · अपुनर्भव = अ + पुनः + भव।",
        "sandhi": "म् + अ: रोगाणाम् + अपुनर्भवे → रोगाणामपुनर्भवे (म् अगले स्वर से जुड़ा) · (रूप-सूचना) उ-अन्त पुल्लिंग शब्द का ‘में’ -औ: हेतौ; अ-अन्त का -ए: लिङ्गे, प्रशमने।",
    },
    "12": {
        "frame": "किसका ज्ञान: चतुर्विध (चार प्रकार का) · वह कैसा: राजा के योग्य, श्रेष्ठ वैद्य · दूसरी पंक्ति: शस्त्र, शास्त्र, जल: गुण-दोष की उत्पत्ति के लिए।",
        "chunks": "ज्ञानं चतुर्विधं यस्य | सः राजार्हः भिषक्तमः ‖ शस्त्रं शास्त्राणि सलिलं | गुणदोषप्रवृत्तये ॥",
        "sandhi": "अ + अ → आ: राज + अर्हः → राजार्हः · विसर्ग → ओ: राजार्हः + भिषक्तमः → राजार्हो भिषक्तमः।",
        "anchors": "भिषक् + तम = श्रेष्ठ वैद्य · चतुर् + विध = चार प्रकार का · प्रवृत्ति = प्र + वृत्त (आरम्भ होना)।",
    },
    "13": {
        "diagram": {"groups": [
            {"label": "उपमा 1",
             "items": ["शास्त्रम्", "प्रदीपभूतम्"]},
            {"label": "उपमा 2",
             "items": ["विपुला मतिः", "दर्शनम्"]}]},
        "chunks": "प्रज्ञां बाहुश्रुत्येन बृंहयेत् ‖ प्रदीपभूतं शास्त्रं हि | दर्शनं विपुला मतिः ॥",
        "pegs": "मेरा बनाया चित्र: हाथ में दीया (शास्त्र) और माथे पर खुली आँख (विशाल बुद्धि)।",
        "contrast": "शास्त्र = दीपक-सा (प्रदीपभूतम्) ; विशाल बुद्धि = दृष्टि (दर्शनम्): श्लोक की दो उपमाएँ।",
    },
}

# ================================================================== IMAGES
IMAGE_SPECS = {
    ("3", "diagram"): {
        "file": "ch2b01-brahmacari-3.svg",
        "alt": "Two columns for verse 3 of chapter 2: the student (brahmacari), first line four qualities, second line five: conqueror of opposites, steadfast, well conducted, firm; six months resident, capable, modesty, cleanliness, skill.",
        "type": "split",
        "title": "ब्रह्मचारी के गुण",
        "cols": [["पहली पंक्ति", ["जितद्वन्द्वः", "धीरः", "सुचरितः", "स्थिरः"]],
                 ["दूसरी पंक्ति", ["षण्मासानुषितः", "शक्तः", "लज्जा", "शौच", "कला"]]],
    },
    ("4", "diagram"): {
        "file": "ch2b01-occasions-4.svg",
        "alt": "Mind map of verse 4 of chapter 2: three occasions after the word na (not): untimely lightning and thunder, an earthquake, the sight of Rahu. The layout of the map is not the verse order; the verse order is lightning and thunder, earthquake, Rahu.",
        "type": "mermaid",
        "code": '''mindmap
  न · इन अवसरों पर
    असमय बिजली-गर्जन
    भूकम्प
    राहु-दर्शन''',
    },
    ("8", "diagram"): {
        "file": "ch2b01-qualities-8.svg",
        "alt": "Two columns for verse 8 of chapter 2: four qualities of the first line (much learned, knows the right time, knows the texts, knows the meaning of the treatises) and the care of the helpless and the sick as for a son.",
        "type": "split",
        "title": "गुण और सेवा",
        "cols": [["पहली पंक्ति: गुण", ["बहुश्रुतः", "कालवेदी", "ज्ञातग्रन्थः", "अर्थशास्त्रवित्"]],
                 ["दूसरी पंक्ति: सेवा", ["अनाथ और रोगी", "पुत्रवत् सेवा"]]],
    },
    ("10", "diagram"): {
        "file": "ch2b01-bewildered-10.svg",
        "alt": "Flow chart of verse 10 of chapter 2, left to right in verse order: he (the man of the previous unit), is bewildered, on reaching a patient each time, like a timid man at a battle.",
        "type": "mermaid",
        "code": '''flowchart LR
  A["सः<br/>(केवल शास्त्रज्ञ)"] --> C["मुह्यति"]
  C --> B["आतुरं प्राप्य<br/>प्राप्य"]
  B -.->|"जैसे"| D["भीरुः इव<br/>आहवम्"]''',
    },
    ("11", "diagram"): {
        "file": "ch2b01-four-topics-11.svg",
        "alt": "Mind map of verse 11 of chapter 2: four topics about diseases: cause, sign, alleviation, non-recurrence.",
        "type": "mermaid",
        "code": '''mindmap
  रोगों के विषय में
    हेतु
    लिङ्ग
    प्रशमन
    अपुनर्भव''',
    },
    ("13", "diagram"): {
        "file": "ch2b01-lamp-sight-13.svg",
        "alt": "Table of verse 13 of chapter 2: the treatise is like a lamp; a wide intellect is the sight.",
        "type": "table",
        "title": "दो उपमाएँ",
        "heads": ["विषय", "उपमा"],
        "rows": [["शास्त्रम्", "प्रदीपभूतम् (दीपक-सा)"],
                 ["विपुला मतिः", "दर्शनम् (दृष्टि)"]],
    },
}
