from helpers import mcq, match, order, fill, multi, accepts


def T(q, teaches):
    q["teaches"] = teaches
    return q


AUTHORED = {}

# ---------------------------------------------------------------- unit 24
AUTHORED["24"] = {
    "title": "षडेतानि निवर्तंते",
    "question": "By unit 24, what turns away from one who will die in six months, and which signs mark one who will die in a month?",
    "rule": ("These six (षट् एतानि) turn away (निवर्तन्ते) from one who will die in six months (षड्भिः मासैः). Speech, "
             "tremor and bewilderment (and a doubtful item printed गाति), with a comparison to a drunk man (मत्तवत्) whose reach is open, mark one who will die in a month (मासात्)."),
    "limits": ("Printed गाति is no standard word; गति (gait) or गात्र (limb) are equal conjectures: no question on that item. "
               "'These six' appear to be the six of card 23 (devotion, character, memory, giving up, intellect, strength); "
               "no question rests on that link. Whether मत्तवत् covers all four items is open."),
    "explain_hi": ("ये छह (षडेतानि) उससे हट जाते हैं (निवर्तन्ते) जो छह मास में मरने वाला है; ‘षड्भिर्मासैः’ काल की तृतीया है: छह मास में। "
                   "डेटा के अनुसार ये छह सम्भवतः कार्ड २३ के भक्ति, शील, स्मृति, त्याग, बुद्धि और बल हैं। "
                   "दूसरी पंक्ति: वाणी, कम्पन और मोह (और अस्पष्ट ‘गाति’), मतवाले से उपमा (मत्तवत्) के साथ, एक मास में (मासात्) मरने वाले के लक्षण हैं। "
                   "छपा ‘गाति’ मानक शब्द नहीं; ‘गति’ (चाल) या ‘गात्र’ (अंग) दोनों बराबर अनुमान हैं, इसलिए उस पर प्रश्न नहीं। "
                   "‘मत्तवत्’ केवल चाल-वाणी के लिए है या चारों के लिए, यह तय नहीं।"),
    "hook": "छह हटें तो छह मास; वाणी, कम्प, मोह (मत्तवत्) तो एक मास।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "In unit 24, what does निवर्तन्ते mean?",
            ("They turn away, cease", "नि-√वृत्, present plural: they turn back, cease."),
            [("They grow much stronger", "Growing would be वर्धन्ते; नि-√वृत् is turning away."),
             ("They are born anew", "Being born would be जायन्ते; नि-√वृत् is turning away."),
             ("They stay fixed", "Staying would be तिष्ठन्ति; नि-√वृत् is turning away.")],
            "निवर्तन्ते = they turn away, cease.",
            "नि-√वृत् = turn away."),
        order(1, "Put the printed words of unit 24 in order.",
              ["षडेतानि", "निवर्तंते", "षड्भिर्मासैर्मरिष्यतः", "मत्तवद्गातिवाक्कम्पमोहा", "मासान्मरिष्यतः"],
              "These six; turn away; from one who will die in six months; drunk-like gait(?), speech, tremor, bewilderment; of one who will die in a month.",
              "षडेतानि → निवर्तंते → षड्भिर्मासैर्मरिष्यतः → मत्तवद्गातिवाक्कम्पमोहा → मासान्मरिष्यतः."),
        match(2, "Match each word of unit 24 to its meaning.",
              [["षट्", "six"], ["निवर्तन्ते", "turn away"], ["मास", "month"], ["मरिष्यत्", "one about to die"],
               ["कम्प", "tremor"], ["मोह", "bewilderment"]],
              "षट् = six, निवर्तन्ते = turn away, मास = month, मरिष्यत् = about to die, कम्प = tremor, मोह = bewilderment.",
              "षट्, निवर्तन्ते, मास, मरिष्यत्, कम्प, मोह.", role="extend",
              teaches="मरिष्यतः is the genitive singular of the future participle of √मृ: 'of one who will die'."),
        mcq("discriminate", 3, "By unit 24, within what time will he die from whom 'these six' turn away?",
            ("In six months", "षड्भिर्मासैर्मरिष्यतः: of one who will die in six months."),
            [("In one month", "One month (मासात्) goes with the drunk-like signs of line 2."),
             ("In six years", "The line says मासैः, months, not years."),
             ("In six weeks", "No weeks are named; the line says six months.")],
            "षड्भिः मासैः = in six months (instrumental of time).",
            "षड्भिर्मासैः = in six months."),
        multi("apply", 4, "Which sure printed signs does line 2 of unit 24 give for one who will die in a month?",
              [("Speech (वाक्)", "Right: वाक् is printed in the compound."),
               ("Hiccup (हिक्का)", "No hiccup is named in unit 24."),
               ("Tremor (कम्प)", "Right: कम्प is printed in the compound."),
               ("Bewilderment (मोह)", "Right: मोहाः closes the compound."),
               ("Fever (ज्वर)", "No fever is named in unit 24.")],
              [0, 2, 3],
              "वाक्-कम्प-मोहाः: speech, tremor, bewilderment (the गाति item is doubtful).",
              "मत्तवद् ... वाक्कम्पमोहा मासान्मरिष्यतः."),
        mcq("transfer", 5, "By the pattern of षट् + एतानि → षडेतानि, how is वाक् + ईशः joined in a new example?",
            ("वागीशः", "A final क् before a vowel becomes the voiced ग्: वाक् + ईशः → वागीशः."),
            [("वाकीशः", "क् does not stay voiceless before a vowel, as षट् did not (षडेतानि)."),
             ("वाङीशः", "ङ् arises before a nasal, not before a vowel."),
             ("वागेशः", "ए would need अ + इ; here the vowel is ई and stays ई.")],
            "वाक् + ईशः = वागीशः, like षट् + एतानि = षडेतानि.",
            "Final stop + vowel → voiced stop.",
            teaches="A final stop before a vowel becomes voiced: षट् + एतानि → षडेतानि, वाक् + ईशः → वागीशः."),
    ],
}

# ---------------------------------------------------------------- unit 25
AUTHORED["25"] = {
    "title": "न याति यस्य चाहारः",
    "question": "By unit 25, which sign of food does line 2 name, and with what exception?",
    "rule": ("He whose food (आहारः) does not go to the throat (कण्ठम्), except for a throat ailment (कण्ठामयात् ऋते). "
             "Line 1 is damaged; only 'pain of hair-plucking' (केशलुञ्चनवेदना) is firm."),
    "limits": ("Low confidence. Line 1 is printed as one token; अज्ञाननूषड्हात् cannot be restored, and नश्यति may be wrong: "
               "no question on line 1. Line 2's result lies beyond this card (appears to); "
               "the card states no outcome."),
    "explain_hi": ("पहली पंक्ति छपाई में बिना जगह एक ही शब्द-समूह है और क्षतिग्रस्त है; केवल ‘केशलुञ्चनवेदना’ (बाल नोचने की पीड़ा) पक्का है। "
                   "‘अज्ञाननूषड्हात्’ अस्पष्ट है (एक अनुमान ‘षडहात्’ = छह दिन में), और ‘नश्यति’ भी गलत हो सकता है, इसलिए वाक्य-रचना पर कोई दावा नहीं। "
                   "दूसरी पंक्ति: जिसका आहार गले (कण्ठ) तक नहीं जाता, गले के रोग के सिवा (कण्ठामयात् ऋते)। "
                   "‘ऋते’ पञ्चमी के साथ आता है: कण्ठामयात् ऋते = गले के रोग के बिना। "
                   "इस वाक्य का फल इस कार्ड में नहीं; वह आगे की पंक्ति में है (सम्भवतः)।"),
    "hook": "आहार गले तक न पहुँचे, गले का रोग न हो।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "In unit 25, what does आहार mean?",
            ("Food", "आहार = food, what is taken in."),
            [("Breath", "Breath would be श्वास or प्राण; आहार is food."),
             ("Speech", "Speech would be वाक्; आहार is food."),
             ("Sleep", "Sleep would be निद्रा; आहार is food.")],
            "आहारः = food.",
            "आहार = food."),
        order(1, "Put the words of line 2 of unit 25 in the printed order.",
              ["न याति", "यस्य", "चाहारः", "कंठं", "कंठामयादृते"],
              "Does not go; whose; and food; to the throat; except for a throat ailment.",
              "न याति → यस्य → चाहारः → कंठं → कंठामयादृते."),
        match(2, "Match each word of line 2 of unit 25 to its meaning.",
              [["याति", "goes"], ["यस्य", "whose"], ["आहार", "food"], ["कण्ठ", "throat"],
               ["आमय", "ailment"], ["ऋते", "except"]],
              "याति = goes, यस्य = whose, आहार = food, कण्ठ = throat, आमय = ailment, ऋते = except.",
              "याति, यस्य, आहार, कण्ठ, आमय, ऋते.", role="extend",
              teaches="ऋते (except, without) takes the ablative: कण्ठामयात् ऋते = except for a throat ailment."),
        mcq("discriminate", 3, "By unit 25, what exception does line 2 allow for food not going to the throat?",
            ("A throat ailment", "कण्ठामयादृते: except for an ailment of the throat."),
            [("A long fast", "No fasting is named; the exception is a throat ailment."),
             ("Old age", "No age is named; the exception is a throat ailment."),
             ("A bad tooth", "No tooth is named; the exception is a throat ailment.")],
            "कण्ठ-आमयात् ऋते = except from a throat ailment.",
            "ऋते + ablative = except."),
        mcq("apply", 4, "Why is कण्ठामयात् printed कंठामयाद् before ऋते in unit 25?",
            ("त् before a vowel → द्", "ऋ is a vowel: a final त् before a vowel becomes the voiced द्."),
            [("त् before any sound → द्", "Not any: before a voiceless sound त् stays (तस्मात्तं, card 30)."),
             ("द् is the ablative's ending", "The ablative ends in -आत्; द् comes only from sandhi."),
             ("द् belongs to the word ऋते", "The particle is ऋते; the द् comes from कण्ठामयात्.")],
            "कण्ठामयात् + ऋते → कण्ठामयादृते: त् before the vowel ऋ → द्.",
            "Final त् + vowel → द्."),
        mcq("transfer", 5, "By the pattern of च + आहारः → चाहारः, how is न + आगतः joined in a new example?",
            ("नागतः", "अ + आ → आ: न + आगतः → नागतः."),
            [("नेगतः", "ए comes from अ + इ, not from अ + आ."),
             ("नोगतः", "ओ comes from अ + उ, not from अ + आ."),
             ("नौगतः", "औ comes from अ + ओ, not from अ + आ.")],
            "न + आगतः = नागतः, like च + आहारः = चाहारः.",
            "अ + आ → आ.",
            teaches="अ before आ merges into one long आ: च + आहारः → चाहारः."),
    ],
}

# ---------------------------------------------------------------- unit 26
AUTHORED["26"] = {
    "title": "प्रेष्याः प्रतीपतो यांति",
    "question": "By unit 26, which signs does the text name, and which two states of sleep go with 'he does not live'?",
    "rule": ("Servants (प्रेष्याः) go contrarily (प्रतीपतः), and the form of a preta (प्रेताकृतिः) arises. He whose sleep "
             "(निद्रा) is constant (नित्या), or not at all (नैव वा), does not live (न स जीवति)."),
    "limits": ("Whose preta-form is meant is not stated, and उदीर्यते may be 'arises' or passive 'is stirred up': no question "
               "on either. नैव वा is read 'or not at all' (data). The card adds no time span or outcome beyond 'does not live'."),
    "explain_hi": ("सेवक (प्रेष्याः) उलटा चलते हैं (प्रतीपतो यान्ति) और प्रेत की आकृति उत्पन्न होती है (प्रेताकृतिरुदीर्यते)। "
                   "किसकी आकृति, यह छपा नहीं; ‘उदीर्यते’ का अर्थ ‘उठती है’ या कर्मवाच्य ‘उकसाई जाती है’ दोनों सम्भव हैं। "
                   "दूसरी पंक्ति: जिसकी नींद निरन्तर (नित्या) हो, अथवा बिलकुल न हो (नैव वा), वह जीवित नहीं रहता। "
                   "यहाँ दो उलटी अवस्थाएँ एक साथ कही गई हैं: सदा नींद और नींद का अभाव। "
                   "‘नैव’ में न + एव है: अ + ए → ऐ।"),
    "hook": "नींद सदा, या कभी नहीं: न स जीवति।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "In unit 26, what does प्रेष्य mean?",
            ("Servant", "प्रेष्य = one to be sent: a servant."),
            [("Enemy", "Enemy would be शत्रु; प्रेष्य is a servant."),
             ("Child", "Child would be बाल; प्रेष्य is a servant."),
             ("Stranger", "Stranger would be अपरिचित; प्रेष्य is a servant.")],
            "प्रेष्याः = servants.",
            "प्रेष्य = servant."),
        order(1, "Put the words of line 2 of unit 26 in the printed order.",
              ["यस्य", "निद्रा", "भवेत्", "नित्या", "नैव वा", "न स जीवति"],
              "Whose; sleep; would be; constant; or not at all; he does not live.",
              "यस्य → निद्रा → भवेत् → नित्या → नैव वा → न स जीवति."),
        match(2, "Match each word of unit 26 to its meaning.",
              [["प्रेष्य", "servant"], ["प्रतीपतः", "contrarily"], ["प्रेत", "departed spirit"], ["आकृति", "form"],
               ["निद्रा", "sleep"], ["नित्य", "constant"]],
              "प्रेष्य = servant, प्रतीपतः = contrarily, प्रेत = departed spirit, आकृति = form, निद्रा = sleep, नित्य = constant.",
              "प्रेष्य, प्रतीपतः, प्रेत, आकृति, निद्रा, नित्य.", role="extend",
              teaches="प्रेत-आकृतिः joins अ + आ → आ: प्रेताकृतिः, the form of a preta."),
        mcq("discriminate", 3, "By unit 26, what kind of sleep goes with न स जीवति (he does not live)?",
            ("Constant, or none at all", "निद्रा ... नित्या नैव वा: sleep constant, or not at all."),
            [("Only by day, not at night", "No day or night is named in unit 26."),
             ("Only after a heavy meal", "No meal is named in unit 26."),
             ("Only at dawn and dusk", "No time of day is named in unit 26.")],
            "Two opposite states: नित्या (constant) and नैव (not at all).",
            "नित्या नैव वा → न स जीवति."),
        mcq("apply", 4, "Which split of नैव in unit 26 is right?",
            ("न + एव", "अ + ए → ऐ: न + एव → नैव."),
            [("न + इव", "अ + इ gives ए: न + इव would print नेव."),
             ("नै + एव", "नै is not a word; the negation is न."),
             ("न + ऐव", "ऐव is not a word; the particle is एव.")],
            "न (not) + एव (indeed): नैव = not at all.",
            "अ + ए → ऐ."),
        mcq("transfer", 5, "By the pattern of न + एव → नैव, how is अत्र + एव (right here) joined in a new example?",
            ("अत्रैव", "अ + ए → ऐ: अत्र + एव → अत्रैव."),
            [("अत्रेव", "ए alone would need अ + इ; here the second vowel is ए."),
             ("अत्रौव", "औ comes from अ + ओ, not from अ + ए."),
             ("अत्राव", "आव् comes from औ before a vowel; there is no औ here.")],
            "अत्र + एव = अत्रैव, like न + एव = नैव.",
            "अ + ए → ऐ.",
            teaches="अ before ए gives ऐ: न + एव → नैव."),
    ],
}

# ---------------------------------------------------------------- unit 27
AUTHORED["27"] = {
    "title": "स्विद्यतश्चरणौ भृशं",
    "question": "By unit 27, what is said of the feet and of the eye of one who will go to Yama's realm?",
    "rule": ("Both feet (चरणौ) sweat greatly (स्विद्यतः भृशम्), and the eye (चक्षुः) falls into agitation (आकुलतां याति) "
             "of one who will go to Yama's realm (यमराष्ट्रं गमिष्यतः). The opening about the face and tears is conjectural."),
    "limits": ("Typed prose in the data. वक्रमार्प्यते is read वक्त्रम् आपूर्यते (the face is filled) only by conjecture: no "
               "question on face or tears. स्विद्यतः is taken as a dual verb with चरणौ (data); no question on its form. "
               "No time span is given."),
    "explain_hi": ("यह इकाई डेटा में गद्य (prose) मानी गई है, इसलिए इसे श्लोक नहीं कहा गया। "
                   "आरम्भ ‘वक्रमार्प्यतेऽश्रूणां’ अनुमानित पाठ ‘वक्त्रम् आपूर्यते’ (मुख आँसुओं से भर जाता है) पर ही समझ आता है; इस पर प्रश्न नहीं। "
                   "पक्का भाग: दोनों पैर बहुत पसीजते हैं (स्विद्यतश्चरणौ भृशम्)। "
                   "और जो यम के राज्य को जाने वाला है (यमराष्ट्रं गमिष्यतः), उसकी आँख व्याकुलता में पड़ जाती है (चक्षुश्चाकुलतां याति)। "
                   "‘चक्षुश्चाकुलतां’ में चक्षुः + च (च से पहले विसर्ग → श्) और च + आकुलताम् (अ + आ → आ) हैं।"),
    "hook": "पैरों में भारी पसीना, आँख में व्याकुलता: यम-राष्ट्र की ओर।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "In unit 27, what does चरणौ mean?",
            ("Both feet", "चरण = foot; चरणौ is the dual: both feet."),
            [("Both hands", "Hands would be हस्तौ; चरणौ are the feet."),
             ("Both eyes", "Eyes would be नेत्रे; चरणौ are the feet."),
             ("Both ears", "Ears would be कर्णौ; चरणौ are the feet.")],
            "चरणौ = both feet.",
            "चरण = foot."),
        order(1, "Put these sure parts of unit 27 in the printed order.",
              ["स्विद्यतश्चरणौ", "भृशं", "चक्षुश्चाकुलतां", "याति", "यमराष्ट्रं गमिष्यतः"],
              "Both feet sweat; greatly; and the eye agitation; goes into; of one who will go to Yama's realm.",
              "स्विद्यतश्चरणौ → भृशं → चक्षुश्चाकुलतां → याति → यमराष्ट्रं गमिष्यतः."),
        match(2, "Match each sure word of unit 27 to its meaning.",
              [["चरणौ", "both feet"], ["भृशम्", "greatly"], ["चक्षुः", "eye"], ["आकुलता", "agitation"],
               ["यमराष्ट्र", "Yama's realm"], ["गमिष्यत्", "one about to go"]],
              "चरणौ = both feet, भृशम् = greatly, चक्षुः = eye, आकुलता = agitation, यम-राष्ट्र = Yama's realm, गमिष्यत् = about to go.",
              "चरणौ, भृशम्, चक्षुः, आकुलता, यमराष्ट्र, गमिष्यत्.", role="extend",
              teaches="गमिष्यतः is the genitive singular of the future participle of √गम्: 'of one who will go'."),
        mcq("discriminate", 3, "In unit 27, what is said of the eye of one who will go to Yama's realm?",
            ("It falls into agitation", "चक्षुश्चाकुलतां याति: the eye goes into agitation."),
            [("It becomes calm and clear", "Calm is the opposite of आकुलता, agitation."),
             ("It turns bright red", "No colour is named for the eye in unit 27."),
             ("It stays shut all day", "No closing of the eye is named in unit 27.")],
            "आकुलतां याति = falls into agitation.",
            "चक्षुः आकुलतां याति."),
        mcq("apply", 4, "Why is चक्षुः printed चक्षुश् before च in unit 27?",
            ("Visarga before च becomes श्", "च is a palatal: a visarga before च or छ becomes श्."),
            [("Visarga before च becomes स्", "स् comes before त or थ, not before च."),
             ("Visarga before च becomes र्", "र् comes before a voiced sound; च is voiceless."),
             ("Visarga before च is dropped", "It is not dropped; it becomes श्, as printed.")],
            "चक्षुः + च → चक्षुश्च: visarga before च → श्.",
            "ः + च/छ → श्."),
        mcq("transfer", 5, "By the pattern of चक्षुः + च → चक्षुश्च, how is हरिः + च joined in a new example?",
            ("हरिश्च", "Visarga before च becomes श्: हरिः + च → हरिश्च."),
            [("हरिर्च", "र् arises before a voiced sound; च is voiceless."),
             ("हरिस्च", "स् arises before त or थ, not before च."),
             ("हरी च", "Lengthening with loss of र् happens before र्, not before च.")],
            "हरिः + च = हरिश्च, like चक्षुः + च = चक्षुश्च.",
            "ः + च → श्च.",
            teaches="A visarga before च or छ becomes श्, whatever vowel stands before it: चक्षुः + च → चक्षुश्च."),
    ],
}

# ---------------------------------------------------------------- unit 28
AUTHORED["28"] = {
    "title": "यैः पुरा रमते भावैः",
    "question": "By unit 28, what change of liking is named, and what does line 2 speak of?",
    "rule": ("Displeased (अरतिः) with those things (भावैः) in which he formerly (पुरा) delighted (रमते), he does not live. "
             "Line 2 speaks of the physician (भिषक्), even when asked (पृष्टः अपि), and a death hard to hear (दुःश्रवम्)."),
    "limits": ("Low confidence. कथयेच्च च may be a misprint for कथयेन्न च, which gives the opposite sense ('should not tell'): "
               "no question on whether the physician tells. The second च is unexplained. मरणम् appears to be completed by "
               "the genitives of card 29."),
    "explain_hi": ("जिन भावों (वस्तुओं, अवस्थाओं) में वह पहले रमता था, उन्हीं से अरति (अरुचि) हो जाए, तो वह जीवित नहीं रहता। "
                   "दूसरी पंक्ति वैद्य (भिषक्) की बात करती है: पूछे जाने पर भी (पृष्टोऽपि), सुनने में कठिन (दुःश्रवम्) मृत्यु के विषय में। "
                   "छपा ‘कथयेच्च च’ है; ‘कथयेन्न च’ भी पढ़ा जा सकता है, जिससे अर्थ उलटा हो जाता है (‘न कहे’), इसलिए वैद्य कहे या न कहे, इस पर कोई प्रश्न नहीं। "
                   "‘मरणम्’ सम्भवतः कार्ड २९ के षष्ठी पदों से पूरा होता है। "
                   "‘पृष्टोऽपि’ में पृष्टः + अपि: अः + अ → ओऽ।"),
    "hook": "जो पहले भाता था, वही न भाए।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "In unit 28, what does अरति mean?",
            ("Displeasure, aversion", "अ-रति = absence of delight: displeasure."),
            [("Strong liking and delight", "Delight is रति; अ- negates it."),
             ("Deep sleep", "Sleep would be निद्रा; अरति is displeasure."),
             ("Sharp pain", "Pain would be वेदना; अरति is displeasure.")],
            "अरतिः = displeasure, aversion.",
            "अरति = displeasure."),
        order(1, "Put the words of line 1 of unit 28 in the printed order.",
              ["यैः पुरा", "रमते", "भावैः", "अरतिः", "तैः", "न जीवति"],
              "By which formerly; he delights; by the things; displeasure; with those; he does not live.",
              "यैः पुरा → रमते → भावैः → अरतिः → तैः → न जीवति."),
        match(2, "Match each word of unit 28 to its meaning.",
              [["पुरा", "formerly"], ["रमते", "delights"], ["अरति", "displeasure"], ["भिषक्", "physician"],
               ["पृष्ट", "asked"], ["दुःश्रव", "hard to hear"]],
              "पुरा = formerly, रमते = delights, अरति = displeasure, भिषक् = physician, पृष्ट = asked, दुःश्रव = hard to hear.",
              "पुरा, रमते, अरति, भिषक्, पृष्ट, दुःश्रव.", role="extend",
              teaches="यैः ... तैः is a relative pair: 'the things in which ... with those'."),
        mcq("discriminate", 3, "By unit 28, with what is the person displeased?",
            ("The things he once delighted in", "यैः पुरा रमते भावैः ... तैः: with those in which he formerly delighted."),
            [("Things he has never known", "The line names things known before: पुरा रमते."),
             ("Only bitter tastes", "No taste is named in unit 28."),
             ("Only loud sounds", "No sound is named in unit 28.")],
            "अरतिः तैः = displeasure with those (things he enjoyed before).",
            "यैः पुरा रमते ... अरतिस्तैः."),
        mcq("apply", 4, "Why is पृष्टः printed पृष्टो before ऽपि in unit 28?",
            ("अः + अ → ओ, and ऽ marks the lost अ", "पृष्टः + अपि → पृष्टोऽपि: अः before अ gives ओ, and the अ is elided."),
            [("Every visarga + अ → ओऽ", "Not every: भावैः + अरतिः gives भावैररतिः in this very card."),
             ("ओ is the stem's own last vowel", "The stem is पृष्ट; ओ comes only from sandhi."),
             ("आः + अ → ओ here", "The word ends in अः, not आः; आः would drop its visarga.")],
            "पृष्टः + अपि = पृष्टोऽपि.",
            "अः + अ → ओऽ."),
        mcq("transfer", 5, "By the pattern of पृष्टः + अपि → पृष्टोऽपि, how is वृक्षः + अत्र (the tree here) joined in a new example?",
            ("वृक्षोऽत्र", "अः + अ → ओऽ: वृक्षः + अत्र → वृक्षोऽत्र."),
            [("वृक्षात्र", "आ would need अ + अ with no visarga; वृक्षः has one."),
             ("वृक्षरत्र", "र् comes from a visarga after a vowel other than अ/आ."),
             ("वृक्षौऽत्र", "औ has no source here; अः + अ gives ओऽ.")],
            "वृक्षः + अत्र = वृक्षोऽत्र, like पृष्टः + अपि = पृष्टोऽपि.",
            "अः + अ → ओऽ.",
            teaches="अः before अ gives ओ, and the following अ is elided (ऽ): पृष्टः + अपि → पृष्टोऽपि."),
    ],
}

# ---------------------------------------------------------------- unit 29
AUTHORED["29"] = {
    "title": "गतासोर्बंधुमित्राणां",
    "question": "By unit 29, whose genitives open line 1, and which beings does line 2 name?",
    "rule": ("On conjectured readings (चिकित्सितुम्, परासुर् उपास्यते): and one should not wish (न च इच्छेत्) to treat him (तम्), since one whose breath has departed (परासुः) is "
             "attended by those beginning with Yama's messengers and piśācas (यमदूतपिशाचाद्यैः)."),
    "limits": ("Low confidence. चिकित्सितं → चिकित्सितुम् and -रूपास्यते → परासुर् उपास्यते are conjectures; no question rests "
               "on उपास्यते. How गतासोः and बन्धुमित्राणाम् join (perhaps with मरणम् of card 28) is not sure. गतासु probably "
               "means a dying person (data). The sentence appears to run on into card 30."),
    "explain_hi": ("‘गतासु’ का शाब्दिक अर्थ है जिसके प्राण चले गए; उपचार की बात है, इसलिए डेटा के अनुसार सम्भवतः मरणासन्न व्यक्ति अभिप्रेत है। "
                   "षष्ठी पद ‘गतासोः’ और ‘बन्धुमित्राणाम्’ (बन्धुओं और मित्रों का) सम्भवतः कार्ड २८ के ‘मरणम्’ से जुड़ते हैं; यह निश्चित नहीं। "
                   "पाठ कहता है: और उसकी चिकित्सा करने की इच्छा न करे (न चेच्छेत्), क्योंकि (यत्) परासु के निकट यम के दूत, पिशाच आदि रहते हैं (उपास्यते)। "
                   "‘चिकित्सितुम्’ और ‘परासुर् उपास्यते’ अनुमानित पाठ हैं; वाक्य सम्भवतः कार्ड ३० में आगे चलता है। "
                   "‘गतासोर्बन्धु’ में ओः के बाद घोष ब आने से विसर्ग र् बना है।"),
    "hook": "गतासु, परासु: प्राण गए; यमदूत पास।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "In unit 29, what does गतासु literally mean?",
            ("One whose breath has gone", "गत (gone) + असु (life-breath), a bahuvrīhi: one whose breath has gone."),
            [("One who has gone abroad", "असु is life-breath, not a place abroad."),
             ("One whose kin have gone", "Kin are बन्धु; असु is life-breath."),
             ("One who has gone to sleep", "Sleep would be निद्रा; असु is life-breath.")],
            "गत-असु = one whose life-breath has gone.",
            "असु = life-breath."),
        order(1, "Put the printed words of line 1 of unit 29 in order.",
              ["गतासोः", "बंधुमित्राणां", "न", "चेच्छेत्", "तं"],
              "Of one whose breath has gone; of kinsmen and friends; not; and should wish; him.",
              "गतासोः → बंधुमित्राणां → न → चेच्छेत् → तं."),
        match(2, "Match each word of unit 29 to its meaning.",
              [["गत", "gone"], ["असु", "life-breath"], ["बन्धु", "kinsman"], ["मित्र", "friend"],
               ["यमदूत", "Yama's messenger"], ["पिशाच", "a class of demon"]],
              "गत = gone, असु = life-breath, बन्धु = kinsman, मित्र = friend, यम-दूत = Yama's messenger, पिशाच = a class of demon.",
              "गत, असु, बन्धु, मित्र, यमदूत, पिशाच.", role="extend",
              teaches="परासु (परा + असु) is a bahuvrīhi like गतासु: one whose breath has departed."),
        mcq("discriminate", 3, "Which split of चेच्छेत् in unit 29 is right?",
            ("च + इच्छेत्", "अ + इ → ए: च + इच्छेत् → चेच्छेत्."),
            [("चेत् + इच्छेत्", "चेत् + इ- would print चेदिच्छेत्, not चेच्छेत्."),
             ("च + एच्छेत्", "अ + ए gives ऐ (चैच्छेत्), and एच्छेत् is not a word."),
             ("चे + इच्छेत्", "चे is not a word; the particle is च.")],
            "च (and) + इच्छेत् (should wish).",
            "अ + इ → ए."),
        mcq("apply", 4, "Why is गतासोः printed गतासोर् before बंधु in unit 29?",
            ("After ओ, visarga before voiced ब → र्", "A visarga after a vowel other than अ/आ becomes र् before a voiced sound."),
            [("Visarga before ब always → ओ", "ओ arises from अः before a voiced consonant; here the vowel is ओ already."),
             ("र् belongs to the stem गतासु", "The stem ends in उ; the र् comes only from sandhi."),
             ("Here the visarga becomes स्", "स् arises before त or थ; ब is voiced.")],
            "गतासोः + बन्धु- → गतासोर्बन्धु-: ओः before a voiced sound → ओर्.",
            "इः/उः/ओः + voiced sound → र्."),
        mcq("transfer", 5, "By the pattern of च + इच्छेत् → चेच्छेत्, how is न + इच्छति joined in a new example?",
            ("नेच्छति", "अ + इ → ए: न + इच्छति → नेच्छति."),
            [("नैच्छति", "ऐ comes from अ + ए, not from अ + इ."),
             ("नीच्छति", "ई comes from इ + इ; here the first vowel is अ."),
             ("नाच्छति", "आ comes from अ + अ; here the second vowel is इ.")],
            "न + इच्छति = नेच्छति, like च + इच्छेत् = चेच्छेत्.",
            "अ + इ → ए.",
            teaches="अ before इ gives ए: च + इच्छेत् → चेच्छेत्."),
    ],
}

# ---------------------------------------------------------------- unit 30
AUTHORED["30"] = {
    "title": "अरिष्टं नास्ति मरणं",
    "question": "By unit 30, what does line 1 say to do about him, and what does line 2 say of death and riṣṭa?",
    "rule": ("By those destroying the potencies of medicines (घ्नद्भिः औषधवीर्याणि); therefore (तस्मात्) one should avoid him "
             "(तं परिवर्जयेत्). There is no death without riṣṭa (अरिष्टं नास्ति मरणम्); riṣṭa = sign of death."),
    "limits": ("दृष्टरिष्टं च जीवितम् is open: 'and there is life in which riṣṭa was seen' or 'and no life once riṣṭa is seen' "
               "(opposite senses): no question on its sense. घ्नद्भिः appears to qualify card 29's beings. Who avoids is "
               "unstated ('one')."),
    "explain_hi": ("पहली पंक्ति कार्ड २९ का वाक्य पूरा करती है (सम्भवतः): औषधों के वीर्य (शक्ति) को नष्ट करने वालों (घ्नद्भिः) द्वारा; इसलिए उससे बचना चाहिए (तं परिवर्जयेत्)। "
                   "कौन बचे, यह छपा नहीं। "
                   "दूसरी पंक्ति: रिष्ट (मृत्यु-लक्षण) के बिना मृत्यु नहीं होती (अरिष्टं नास्ति मरणम्)। "
                   "‘दृष्टरिष्टं च जीवितम्’ के दो उलटे अर्थ सम्भव हैं: ‘रिष्ट दिखने पर भी जीवन है’ या ‘रिष्ट दिखने पर जीवन नहीं’; डेटा इसे खुला छोड़ता है, इसलिए इस पर प्रश्न नहीं। "
                   "‘दृष्टरिष्टम्’ = दृष्ट + रिष्ट; दृष्ट + अरिष्ट होता तो आ दिखता।"),
    "hook": "रिष्ट के बिना मृत्यु नहीं।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "In unit 30, what does वीर्य in औषधवीर्याणि mean?",
            ("Potency", "वीर्य = potency: the potencies of medicines."),
            [("Taste", "Taste would be रस; वीर्य is potency."),
             ("Heaviness", "Heaviness would be गुरुत्व; वीर्य is potency."),
             ("Smell", "Smell would be गन्ध; वीर्य is potency.")],
            "औषध-वीर्याणि = potencies of medicines.",
            "वीर्य = potency."),
        order(1, "Put the words of line 1 of unit 30 in the printed order.",
              ["घ्नद्भिः", "औषधवीर्याणि", "तस्मात्", "तं", "परिवर्जयेत्"],
              "By those destroying; the potencies of medicines; therefore; him; one should avoid.",
              "घ्नद्भिः → औषधवीर्याणि → तस्मात् → तं → परिवर्जयेत्."),
        match(2, "Match each word of unit 30 to its meaning.",
              [["घ्नत्", "destroying"], ["औषध", "medicine"], ["वीर्य", "potency"], ["तस्मात्", "therefore"],
               ["परिवर्जयेत्", "should avoid"], ["मरण", "death"]],
              "घ्नत् = destroying, औषध = medicine, वीर्य = potency, तस्मात् = therefore, परिवर्जयेत् = should avoid, मरण = death.",
              "घ्नत्, औषध, वीर्य, तस्मात्, परिवर्जयेत्, मरण.", role="extend",
              teaches="घ्नद्भिः is the instrumental plural of the present participle of √हन्: 'by those destroying'."),
        mcq("discriminate", 3, "Which split of नास्ति in unit 30 is right?",
            ("न + अस्ति", "अ + अ → आ: न + अस्ति → नास्ति."),
            [("न + स्ति", "With स्ति no आ would appear: नस्ति."),
             ("न + आस्ति", "आस्ति is not a form; the verb is अस्ति."),
             ("नास् + ति", "Neither नास् nor ति is a word here.")],
            "न (not) + अस्ति (is).",
            "अ + अ → आ."),
        mcq("apply", 4, "By the first clause of line 2 of unit 30, what does not exist without riṣṭa?",
            ("Death", "अरिष्टं नास्ति मरणम्: there is no death without riṣṭa."),
            [("Medicine", "Medicine is in line 1, with its potencies destroyed."),
             ("Sleep", "No sleep is named in unit 30."),
             ("Fever", "No fever is named in unit 30.")],
            "अ-रिष्टम् मरणम् न अस्ति = there is no death without riṣṭa.",
            "अरिष्टं नास्ति मरणम्."),
        mcq("transfer", 5, "By the pattern of घ्नद्भिः + औषध- → घ्नद्भिरौषध-, how is मुनिभिः + उक्तम् joined in a new example?",
            ("मुनिभिरुक्तम्", "इः before a vowel → इर्: मुनिभिः + उक्तम् → मुनिभिरुक्तम्."),
            [("मुनिभि उक्तम्", "The visarga drops only after अ or आ; after इ it becomes र्."),
             ("मुनिभ्युक्तम्", "इ → य् needs a bare इ; here a visarga stands between."),
             ("मुनिभिसुक्तम्", "स् arises before त or थ, not before a vowel.")],
            "मुनिभिः + उक्तम् = मुनिभिरुक्तम्, like घ्नद्भिः + औषध- = घ्नद्भिरौषध-.",
            "इः + vowel → इर्.",
            teaches="A visarga after इ becomes र् before a vowel or voiced consonant: घ्नद्भिः + औषध- → घ्नद्भिरौषध-."),
    ],
}

# ---------------------------------------------------------------- unit 31
AUTHORED["31"] = {
    "title": "अरिष्टे रिष्टविज्ञानं",
    "question": "By unit 31, what does line 1 say about knowledge of riṣṭa, and to whom is it ascribed?",
    "rule": ("Knowledge of riṣṭa where there is no riṣṭa (अरिष्टे), and none in riṣṭas (न च रिष्टेषु), from lack of skill "
             "(अनैपुणात्): this is Caraka's statement (चरकस्य वचनम्); but by Suśruta is recited (पठ्यते)..."),
    "limits": ("Elliptical, no verb in line 1. 'False recognition' and 'failure to recognise' are an inference, not printed: "
               "no question on them. What Suśruta recites is not stated (probably card 32). Caraka and Suśruta are taken "
               "as names of two authorities."),
    "explain_hi": ("पहली पंक्ति में क्रिया नहीं: जहाँ रिष्ट नहीं, वहाँ रिष्ट का ज्ञान; और रिष्टों में (ज्ञान) नहीं; निपुणता के अभाव से (अनैपुणात्)। "
                   "डेटा के अनुसार सम्भवतः इसका भाव है: अकुशलता से झूठा रिष्ट दिखना और सच्चा रिष्ट न पहचानना; पर ‘झूठा’ या ‘न पहचानना’ शब्द छपे नहीं, यह केवल अनुमान है। "
                   "‘चरकस्येति वचनम्’: यह चरक का वचन है। "
                   "‘सुश्रुतेन तु पठ्यते’: परन्तु सुश्रुत द्वारा पढ़ा जाता है; क्या पढ़ा जाता है, यह छपा नहीं, सम्भवतः कार्ड ३२ की बात। "
                   "‘रिष्टेष्वनैपुणात्’ में रिष्टेषु + अनैपुणात्: उ + अ → व।"),
    "hook": "अनैपुण से: अरिष्टे रिष्ट-ज्ञान, रिष्टों में नहीं (चरक का वचन)।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "In unit 31, what does अनैपुण mean?",
            ("Lack of skill", "अ-नैपुण: absence of skill (नैपुण)."),
            [("Great skill", "नैपुण alone is skill; अ- negates it."),
             ("Lack of food", "Food would be आहार; नैपुण is skill."),
             ("Lack of wealth", "Wealth would be धन; नैपुण is skill.")],
            "अनैपुणात् = from lack of skill.",
            "अनैपुण = lack of skill."),
        order(1, "Put the four quarter-lines of unit 31 in the printed order.",
              ["अरिष्टे रिष्टविज्ञानं", "न च रिष्टेष्वनैपुणात्", "चरकस्येति वचनं", "सुश्रुतेन तु पठ्यते"],
              "Knowledge of riṣṭa where none is; and not in riṣṭas, from lack of skill; this is Caraka's statement; but by Suśruta is recited.",
              "अरिष्टे रिष्टविज्ञानं → न च रिष्टेष्वनैपुणात् → चरकस्येति वचनं → सुश्रुतेन तु पठ्यते."),
        match(2, "Match each word of unit 31 to its meaning.",
              [["अरिष्टे", "where there is no riṣṭa"], ["विज्ञान", "knowledge"], ["अनैपुण", "lack of skill"],
               ["वचन", "statement"], ["पठ्यते", "is recited"]],
              "अरिष्टे = in the absence of riṣṭa, विज्ञान = knowledge, अनैपुण = lack of skill, वचन = statement, पठ्यते = is recited.",
              "अरिष्टे, विज्ञान, अनैपुण, वचन, पठ्यते.", role="extend",
              teaches="पठ्यते is a passive present of √पठ्: 'is recited, is read'."),
        mcq("discriminate", 3, "Which split of रिष्टेष्वनैपुणात् in unit 31 is right?",
            ("रिष्टेषु + अनैपुणात्", "उ + अ → व: रिष्टेषु + अनैपुणात् → रिष्टेष्वनैपुणात्."),
            [("रिष्टेषु + नैपुणात्", "With नैपुणात् no व would appear: रिष्टेषु नैपुणात्."),
             ("रिष्टेष्व + नैपुणात्", "रिष्टेष्व is not a word; the व comes from उ."),
             ("रिष्टे + स्वनैपुणात्", "स्वनैपुणात् is not printed; the letter is ष्, not स्.")],
            "रिष्टेषु (in riṣṭas) + अनैपुणात् (from lack of skill).",
            "उ + unlike vowel → व्."),
        mcq("apply", 4, "In unit 31, line 1 is called whose statement (वचन)?",
            ("Caraka's", "चरकस्येति वचनम्: thus the statement of Caraka."),
            [("Yama's", "Yama is named in other cards, not as the author here."),
             ("The patient's", "No patient speaks in unit 31."),
             ("A messenger's", "No messenger speaks in unit 31.")],
            "चरकस्य वचनम् = the statement of Caraka.",
            "चरकस्येति वचनम्."),
        mcq("transfer", 5, "By the pattern of रिष्टेषु + अनैपुणात् → रिष्टेष्वनैपुणात्, how is तु + अत्र joined in a new example?",
            ("त्वत्र", "उ before a different vowel → व्: तु + अत्र → त्वत्र."),
            [("तोत्र", "ओ comes from अ + उ, not from उ + अ."),
             ("तूत्र", "ऊ comes from उ + उ; here the second vowel is अ."),
             ("तवत्र", "अव् comes from ओ before a vowel; here the vowel is उ.")],
            "तु + अत्र = त्वत्र, like रिष्टेषु + अनैपुणात् = रिष्टेष्वनैपुणात्.",
            "उ + unlike vowel → व्.",
            teaches="उ before a different vowel becomes व्: रिष्टेषु + अनैपुणात् → रिष्टेष्वनैपुणात्."),
    ],
}

# ---------------------------------------------------------------- unit 32
AUTHORED["32"] = {
    "title": "ध्रुवं हि रिष्टे मरणं",
    "question": "By unit 32, what is certain in riṣṭa, and by whom is 'that' said to be warded off?",
    "rule": ("For in riṣṭa death is certain (ध्रुवम्); that (तत्), it is said (किल), is warded off (निवार्यते) by stainless "
             "brāhmaṇas (अमलैः ब्राह्मणैः) and by those intent on rasāyana, austerity and giving."),
    "limits": ("'That' (तत्) has no stated referent (death or its certainty). किल marks a report ('it is said'); no method, "
               "dose or result beyond this is given. This appears to be what Suśruta recites (card 31). rasāyana = "
               "rejuvenation therapy (standard)."),
    "explain_hi": ("क्योंकि रिष्ट होने पर मृत्यु निश्चित (ध्रुवम्) है। "
                   "‘किल’ (कहते हैं) से पता चलता है कि आगे की बात एक कही हुई बात है: वह (तत्) निर्मल ब्राह्मणों द्वारा, और रसायन (पुनर्यौवनकारी चिकित्सा, मानक), तप और दान में लगे लोगों द्वारा टाला जाता है (निवार्यते)। "
                   "‘तत्’ किसके लिए है, मृत्यु या उसकी निश्चितता, यह छपा नहीं। "
                   "डेटा के अनुसार सम्भवतः यही वह बात है जिसे कार्ड ३१ सुश्रुत द्वारा पठित बताता है। "
                   "‘तपोदान’ में तपस् + दान: अस् + घोष व्यंजन द → ओ।"),
    "hook": "रिष्ट में मृत्यु ध्रुव; किल: ब्राह्मण, रसायन, तप, दान से टले।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "In unit 32, what does ध्रुव mean?",
            ("Certain", "ध्रुवम् = fixed, certain."),
            [("Doubtful", "Doubtful is the opposite of ध्रुव."),
             ("Distant", "Distant would be दूर; ध्रुव is certain."),
             ("Painless", "Painless would be अवेदन; ध्रुव is certain.")],
            "ध्रुवं ... मरणम् = death is certain.",
            "ध्रुव = certain."),
        order(1, "Put these parts of unit 32 in the printed order.",
              ["ध्रुवं हि रिष्टे मरणं", "ब्राह्मणैः", "तत् किल", "अमलैः", "रसायनतपोदानतत्परैः", "च निवार्यते"],
              "For in riṣṭa death is certain; by brāhmaṇas; that, it is said; stainless; by those intent on rasāyana, austerity and giving; and is warded off.",
              "ध्रुवं हि रिष्टे मरणं → ब्राह्मणैः → तत् किल → अमलैः → रसायनतपोदानतत्परैः → च निवार्यते."),
        match(2, "Match each word of unit 32 to its meaning.",
              [["ध्रुव", "certain"], ["किल", "it is said"], ["अमल", "stainless"], ["तपस्", "austerity"],
               ["दान", "giving"], ["निवार्यते", "is warded off"]],
              "ध्रुव = certain, किल = it is said, अमल = stainless, तपस् = austerity, दान = giving, निवार्यते = is warded off.",
              "ध्रुव, किल, अमल, तपस्, दान, निवार्यते.", role="extend",
              teaches="तत्पर at the end of a compound means 'intent on': रसायन-तपः-दान-तत्पर = intent on rasāyana, austerity and giving."),
        mcq("discriminate", 3, "Which split of तत्किलामलैः in unit 32 is right?",
            ("तत् + किल + अमलैः", "अ + अ → आ: किल + अमलैः → किलामलैः."),
            [("तत् + किल + मलैः", "With मलैः no आ would appear: किल मलैः."),
             ("तत् + किला + मलैः", "किला is not a word; the particle is किल."),
             ("तत्कि + ला + मलैः", "Neither तत्कि nor ला fits; the parts are तत्, किल, अमलैः.")],
            "तत् (that) + किल (it is said) + अमलैः (by the stainless).",
            "अ + अ → आ."),
        multi("apply", 4, "By unit 32, by whom is 'that' said to be warded off?",
              [("Kinsmen and friends", "No: they are named in card 29, not as warding anything off."),
               ("Stainless brāhmaṇas", "Right: ब्राह्मणैः ... अमलैः."),
               ("Messengers of Yama", "No: Yama's messengers are named in card 29, not in unit 32."),
               ("Those intent on rasāyana, austerity and giving", "Right: रसायनतपोदानतत्परैः.")],
              [1, 3],
              "Two instrumentals: the stainless brāhmaṇas, and those intent on rasāyana, austerity and giving.",
              "ब्राह्मणैः अमलैः, रसायनतपोदानतत्परैः च → निवार्यते."),
        mcq("transfer", 5, "By the pattern of तपस् + दान → तपोदान, how is यशस् + धन joined in a compound, in a new example?",
            ("यशोधन", "-अस् before the voiced consonant ध → -ओ: यशस् + धन → यशोधन."),
            [("यशधन", "The -अस् does not simply drop; before a voiced consonant it gives -ओ."),
             ("यशर्धन", "र् arises from a visarga after a vowel other than अ/आ."),
             ("यशाधन", "आ has no source here; -अस् gives -ओ.")],
            "यशस् + धन = यशोधन, like तपस् + दान = तपोदान.",
            "-अस् + voiced consonant → -ओ.",
            teaches="An -अस् stem before a voiced consonant shows -ओ: तपस् + दान → तपोदान."),
    ],
}

# ---------------------------------------------------------------- unit 33
AUTHORED["33"] = {
    "title": "द्विधा रिष्टं स्थिरास्थिरविभेदतः",
    "question": "By unit 33, how is riṣṭa divided, and from what may a semblance of riṣṭa arise?",
    "rule": ("Riṣṭa is twofold (द्विधा), by the division into stable and unstable (स्थिर-अस्थिर). Even from an abundance of "
             "the doṣas (दोषाणाम् बाहुल्यात्) a semblance of riṣṭa (रिष्टाभासः) may arise."),
    "limits": ("Typed prose in the data; no verb in line 1 ('says' or 'holds' understood). The printed name कृष्णातरेयो is read "
               "Kṛṣṇātreya only by conjecture: no question on the name or on whose view it is. Stable and unstable are "
               "taken up in card 34."),
    "explain_hi": ("यह इकाई डेटा में गद्य मानी गई है, इसलिए इसे श्लोक नहीं कहा गया। "
                   "छपा नाम ‘कृष्णातरेयो’ ज्ञात नहीं; ‘कृष्णात्रेय’ अनुमानित पाठ है, इसलिए नाम पर प्रश्न नहीं। "
                   "रिष्ट दो प्रकार का (द्विधा) है: स्थिर और अस्थिर, इस भेद से (स्थिरास्थिरविभेदतः)। "
                   "दोषों की अधिकता (बाहुल्य) से भी रिष्ट का आभास (रिष्टाभास) उत्पन्न हो सकता है (समुद्भवेत्), यानी रिष्ट जैसा दिखना। "
                   "स्थिर और अस्थिर की बात कार्ड ३४ में आगे आती है।"),
    "hook": "रिष्ट दो: स्थिर, अस्थिर; दोष बढ़ें तो रिष्ट-आभास।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 33, into which two kinds is riṣṭa divided?",
            ("Stable and unstable", "स्थिरास्थिरविभेदतः: by the division into stable and unstable."),
            [("Visible and invisible", "No such pair is printed; the pair is स्थिर / अस्थिर."),
             ("Inner and outer", "No such pair is printed; the pair is स्थिर / अस्थिर."),
             ("Hot and cold", "No such pair is printed; the pair is स्थिर / अस्थिर.")],
            "द्विधा रिष्टं: stable (स्थिर) and unstable (अस्थिर).",
            "स्थिर / अस्थिर."),
        order(1, "Put these parts of unit 33 in the printed order.",
              ["द्विधा रिष्टं", "स्थिरास्थिरविभेदतः", "दोषाणामपि", "बाहुल्यात्", "रिष्टाभासः समुद्भवेत्"],
              "Riṣṭa twofold; by the division into stable and unstable; even of the doṣas; from abundance; a semblance of riṣṭa may arise.",
              "द्विधा रिष्टं → स्थिरास्थिरविभेदतः → दोषाणामपि → बाहुल्यात् → रिष्टाभासः समुद्भवेत्."),
        match(2, "Match each word of unit 33 to its meaning.",
              [["द्विधा", "twofold"], ["स्थिर", "stable"], ["अस्थिर", "unstable"], ["बाहुल्य", "abundance"],
               ["आभास", "semblance"], ["समुद्भवेत्", "may arise"]],
              "द्विधा = twofold, स्थिर = stable, अस्थिर = unstable, बाहुल्य = abundance, आभास = semblance, समुद्भवेत् = may arise.",
              "द्विधा, स्थिर, अस्थिर, बाहुल्य, आभास, समुद्भवेत्.", role="extend",
              teaches="रिष्ट-आभास is a tatpuruṣa: a semblance (only an appearance) of riṣṭa."),
        mcq("discriminate", 3, "Which split of स्थिरास्थिर in unit 33 is right?",
            ("स्थिर + अस्थिर", "अ + अ → आ: स्थिर + अस्थिर → स्थिरास्थिर."),
            [("स्थिर + आस्थिर", "आस्थिर is not a word; the opposite of स्थिर is अस्थिर."),
             ("स्थि + रास्थिर", "Neither स्थि nor रास्थिर is a word."),
             ("स्थिरः + अस्थिर", "A compound member has no visarga; अः + अ would give ओऽ.")],
            "स्थिर (stable) + अस्थिर (unstable).",
            "अ + अ → आ."),
        mcq("apply", 4, "By unit 33, from what may a semblance of riṣṭa arise?",
            ("Abundance of the doṣas", "दोषाणामपि बाहुल्याद्रिष्टाभासः समुद्भवेत्."),
            [("A long journey on foot", "No journey is named in unit 33."),
             ("Eating only cold food", "No food is named in unit 33."),
             ("Old age on its own", "No age is named in unit 33.")],
            "दोषाणाम् बाहुल्यात् = from an abundance of the doṣas.",
            "दोष-बाहुल्य → रिष्टाभास."),
        mcq("transfer", 5, "By the pattern of बाहुल्यात् + रिष्ट- → बाहुल्याद्रिष्ट-, how is तस्मात् + रामः joined in a new example?",
            ("तस्माद्रामः", "त् before the voiced र → द्: तस्मात् + रामः → तस्माद्रामः."),
            [("तस्मान्रामः", "न् is a choice only before a nasal; र is not a nasal."),
             ("तस्माच्रामः", "च् arises before च or छ, not before र."),
             ("तस्मा रामः", "The त् is not dropped; it becomes द्.")],
            "तस्मात् + रामः = तस्माद्रामः, like बाहुल्यात् + रिष्ट- = बाहुल्याद्रिष्ट-.",
            "त् + voiced र → द्.",
            teaches="A final त् before a voiced sound such as र becomes द्: बाहुल्यात् + रिष्ट- → बाहुल्याद्रिष्ट-."),
    ],
}

# ---------------------------------------------------------------- unit 34
AUTHORED["34"] = {
    "title": "तद्दोषाणां शमे शाम्येत्",
    "question": "By unit 34, what subsides with the doṣas, what is certainly for death, and where is Āyurveda's whole fruit established?",
    "rule": ("On the subsiding (शमे) of those doṣas (it) would subside (शाम्येत्); but the lasting one (स्थायि) is certainly "
             "(अवश्यम्) for death (मृत्यवे). The whole fruit of Āyurveda, which is established in the knower of lifespan (आयुर्ज्ञे)..."),
    "limits": ("The subject of शाम्येत् (the semblance of card 33) and 'the lasting one' (the stable riṣṭa of card 33) are "
               "the data's readings, not printed here: no question on them. स्थायि may be m. or n. Line 2's main clause "
               "is in card 35 (appears to)."),
    "explain_hi": ("उन दोषों के शान्त होने पर (तद्दोषाणां शमे) वह शान्त हो जाए (शाम्येत्); डेटा के अनुसार ‘वह’ कार्ड ३३ का रिष्टाभास है। "
                   "परन्तु स्थायी (स्थायि) निश्चय ही मृत्यु के लिए है (अवश्यं तु मृत्यवे); डेटा इसे कार्ड ३३ का स्थिर रिष्ट मानता है। "
                   "यहाँ दो उलटी बातें एक साथ हैं: जो शान्त हो जाए और जो टिका रहे। "
                   "दूसरी पंक्ति: आयुर्वेद का सम्पूर्ण फल, जो आयु के ज्ञाता (आयुर्ज्ञ) में प्रतिष्ठित है; मुख्य वाक्य सम्भवतः कार्ड ३५ में है। "
                   "‘स्थाय्यवश्यं’ में इ (या ई) + अ → य।"),
    "hook": "दोष शान्त तो आभास शान्त; स्थायी तो अवश्य मृत्यु।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "In unit 34, what does शम mean?",
            ("Subsiding, calming", "शम = calming, subsiding (√शम्)."),
            [("Increase, swelling up", "Increase would be वृद्धि; शम is subsiding."),
             ("Mixing, joining", "Mixing would be संसर्ग; शम is subsiding."),
             ("Seeing, sight", "Seeing would be दर्शन; शम is subsiding.")],
            "शमे = on the subsiding.",
            "शम = subsiding."),
        order(1, "Put these parts of unit 34 in the printed order.",
              ["तद्दोषाणां शमे", "शाम्येत्", "स्थाय्यवश्यं तु मृत्यवे", "आयुर्वेदफलं कृत्स्नं", "यदायुर्ज्ञे प्रतिष्ठितं"],
              "On the subsiding of those doṣas; would subside; but the lasting one certainly for death; the whole fruit of Āyurveda; which is established in the knower of lifespan.",
              "तद्दोषाणां शमे → शाम्येत् → स्थाय्यवश्यं तु मृत्यवे → आयुर्वेदफलं कृत्स्नं → यदायुर्ज्ञे प्रतिष्ठितं."),
        match(2, "Match each word of unit 34 to its meaning.",
              [["शम", "subsiding"], ["स्थायिन्", "lasting"], ["अवश्यम्", "certainly"], ["कृत्स्न", "whole"],
               ["फल", "fruit"], ["प्रतिष्ठित", "established"]],
              "शम = subsiding, स्थायिन् = lasting, अवश्यम् = certainly, कृत्स्न = whole, फल = fruit, प्रतिष्ठित = established.",
              "शम, स्थायिन्, अवश्यम्, कृत्स्न, फल, प्रतिष्ठित.", role="extend",
              teaches="मृत्यवे is the dative of मृत्यु: 'for death'."),
        mcq("discriminate", 3, "By unit 34, what is said of the lasting one (स्थायि)?",
            ("It is certainly for death", "स्थाय्यवश्यं तु मृत्यवे: but the lasting one is certainly for death."),
            [("It subsides with the doṣas", "That is said of what subsides (शाम्येत्), set against the lasting one by तु."),
             ("It is the fruit of Āyurveda", "The fruit of Āyurveda (आयुर्वेदफलम्) is the subject of line 2, not the lasting one."),
             ("It lasts only for one day", "No day is named; स्थायि means lasting.")],
            "स्थायि ... अवश्यं मृत्यवे: the lasting one is certainly for death.",
            "स्थायि → अवश्यं मृत्यवे."),
        mcq("apply", 4, "Which split of स्थाय्यवश्यं in unit 34 is right?",
            ("स्थायि + अवश्यम्", "इ before a different vowel → य्: स्थायि + अवश्यम् → स्थाय्यवश्यम् (स्थायी would join the same way)."),
            [("स्थाये + अवश्यम्", "ए + अ would give एऽ: स्थायेऽवश्यम्, not the print."),
             ("स्थायि + वश्यम्", "With वश्यम् no य् would appear: स्थायिवश्यम्."),
             ("स्थाय्य + वश्यम्", "स्थाय्य is not a word; the य् comes from इ.")],
            "स्थायि (lasting) + अवश्यम् (certainly).",
            "इ + unlike vowel → य्."),
        mcq("transfer", 5, "By the pattern of यत् + आयुर्ज्ञे → यदायुर्ज्ञे, how is जगत् + ईशः joined in a new example?",
            ("जगदीशः", "त् before a vowel → द्: जगत् + ईशः → जगदीशः."),
            [("जगतीशः", "त् does not stay voiceless before a vowel, as यत् did not (यदायुर्ज्ञे)."),
             ("जगन्नीशः", "न् is a choice only before a nasal; ई is a vowel."),
             ("जगदिशः", "The ई of ईशः stays long; nothing shortens it.")],
            "जगत् + ईशः = जगदीशः, like यत् + आयुर्ज्ञे = यदायुर्ज्ञे.",
            "Final त् + vowel → द्.",
            teaches="A final त् before a vowel becomes द्: यत् + आयुर्ज्ञे → यदायुर्ज्ञे."),
    ],
}

# ---------------------------------------------------------------- unit 35
AUTHORED["35"] = {
    "title": "रिष्टज्ञानादृतस्तस्मात्",
    "question": "By unit 35, what should the physician always be, and how does the chapter close?",
    "rule": ("Therefore (तस्मात्) the physician (भिषक्) should always (सर्वदा एव) be attentive to the knowledge of riṣṭa "
             "(रिष्टज्ञानादृतः). Thus (इति) ends the tenth chapter (दशमः अध्यायः), named Vikṛtehāvijñānīya."),
    "limits": ("Typed prose in the data. आदृत is read active 'attentive'; 'honoured for knowledge of riṣṭa' is possible: no "
               "question on which sense. The analysis of the title as 'knowledge of abnormal activity' is probable, not "
               "printed."),
    "explain_hi": ("यह इकाई डेटा में गद्य मानी गई है और अध्याय का समापन है। "
                   "इसलिए (तस्मात्) वैद्य (भिषक्) को सदा ही (सर्वदैव) रिष्ट के ज्ञान का आदर करने वाला, यानी उस पर ध्यान देने वाला, होना चाहिए (भवेत्)। "
                   "‘आदृत’ का दूसरा अर्थ ‘रिष्ट-ज्ञान के लिए सम्मानित’ भी सम्भव है, इसलिए इस पर प्रश्न नहीं। "
                   "अन्तिम पंक्ति पुष्पिका है: इस प्रकार विकृतेहाविज्ञानीय नामक दसवाँ अध्याय (समाप्त)। "
                   "‘सर्वदैव’ में सर्वदा + एव: आ + ए → ऐ।"),
    "hook": "वैद्य सदा रिष्ट-ज्ञान पर ध्यान दे: दसवाँ अध्याय पूरा।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "In unit 35, what does भिषक् mean?",
            ("Physician", "भिषज् (भिषक्) = physician."),
            [("Messenger", "Messenger would be दूत; भिषक् is the physician."),
             ("Servant", "Servant would be प्रेष्य; भिषक् is the physician."),
             ("Teacher", "Teacher would be गुरु; भिषक् is the physician.")],
            "भिषक् = physician.",
            "भिषक् = physician."),
        order(1, "Put the words of line 1 of unit 35 in the printed order.",
              ["रिष्टज्ञानादृतः", "तस्मात्", "सर्वदैव", "भवेत्", "भिषक्"],
              "Attentive to the knowledge of riṣṭa; therefore; always indeed; should be; the physician.",
              "रिष्टज्ञानादृतः → तस्मात् → सर्वदैव → भवेत् → भिषक्."),
        match(2, "Match each word of unit 35 to its meaning.",
              [["सर्वदा", "always"], ["भवेत्", "should be"], ["भिषक्", "physician"], ["इति", "thus"],
               ["दशम", "tenth"], ["अध्याय", "chapter"]],
              "सर्वदा = always, भवेत् = should be, भिषक् = physician, इति = thus, दशम = tenth, अध्याय = chapter.",
              "सर्वदा, भवेत्, भिषक्, इति, दशम, अध्याय.", role="extend",
              teaches="भवेत् is the optative of √भू: 'should be'."),
        mcq("discriminate", 3, "Which split of सर्वदैव in unit 35 is right?",
            ("सर्वदा + एव", "आ + ए → ऐ: सर्वदा + एव → सर्वदैव."),
            [("सर्वदा + इव", "आ + इ gives ए: सर्वदा + इव would print सर्वदेव."),
             ("सर्वदै + एव", "सर्वदै is not a word; the adverb is सर्वदा."),
             ("सर्वदा + ऐव", "ऐव is not a word; the particle is एव.")],
            "सर्वदा (always) + एव (indeed).",
            "आ + ए → ऐ."),
        mcq("apply", 4, "By the colophon of unit 35, which chapter ends here?",
            ("The tenth", "दशमोऽध्यायः: the tenth chapter."),
            [("The ninth", "Ninth would be नवमः; the colophon says दशमः."),
             ("The twelfth", "Twelfth would be द्वादशः; the colophon says दशमः."),
             ("The eleventh", "Eleventh would be एकादशः; the colophon says दशमः.")],
            "इति विकृतेहाविज्ञानीयो नाम दशमोऽध्यायः.",
            "दशम = tenth."),
        mcq("transfer", 5, "By the pattern of भवेत् + भिषक् → भवेद्भिषक्, how is भवेत् + बुधः (one should be wise) joined in a new example?",
            ("भवेद्बुधः", "त् before the voiced ब → द्: भवेत् + बुधः → भवेद्बुधः."),
            [("भवेन्बुधः", "न् is a choice only before a nasal; ब is not a nasal."),
             ("भवेच्बुधः", "च् arises before च or छ, not before ब."),
             ("भवेर्बुधः", "र् arises from a visarga, not from त्.")],
            "भवेत् + बुधः = भवेद्बुधः, like भवेत् + भिषक् = भवेद्भिषक्.",
            "त् + voiced consonant → द्.",
            teaches="A final त् before a voiced consonant such as भ or ब becomes द्: भवेत् + भिषक् → भवेद्भिषक्."),
    ],
}

# ================================================================ NOTES_HI
NOTES_HI = {
    "24": ("श्लोक; विश्वास मध्यम; दो छपी पंक्तियाँ (०२.१०.४६ और ०२.१०.४७) जोड़ी गईं। पाठ-चिह्न (सम्भव): छपा ‘गाति’ मानक शब्द नहीं; "
           "‘गति’ (चाल) या ‘गात्र’ (अंग) बराबर छोटे सुधार हैं, छपाई से तय नहीं; इस पर प्रश्न नहीं। पहली पंक्ति कार्ड २३ को पूरा करती है "
           "(सम्भवतः): छह = भक्ति, शील, स्मृति, त्याग, बुद्धि, बल। ‘मत्तवत्’ केवल चाल-वाणी पर है या चारों पर, तय नहीं। दूसरी पंक्ति में "
           "क्रिया नहीं। सन्धि जाँची: षट् + एतानि → षडेतानि (स्वर से पहले ट् → ड्); षट् + भिः → षड्भिः; मासैः + मरिष्यतः → "
           "मासैर्मरिष्यतः (ऐः + घोष → ऐर्); मासात् + मरिष्यतः → मासान्मरिष्यतः (अनुनासिक म से पहले त् → न्, वैकल्पिक; द् भी शुद्ध)। "
           "छपा ‘निवर्तंते’ अनुस्वार के साथ = निवर्तन्ते।"),
    "25": ("श्लोक; विश्वास कम; दो छपी पंक्तियाँ (०२.१०.४८ और ०२.१०.४९)। पाठ-चिह्न: पहली पंक्ति बिना जगह एक शब्द-समूह छपी है और "
           "क्षतिग्रस्त है; ‘अज्ञाननूषड्हात्’ ठीक नहीं किया जा सकता (एक अनुमान ‘षडहात्’ = छह दिन में; ‘अज्ञान’ और ‘नू’ अस्पष्ट); "
           "‘वेदनाम्’ (द्वितीया) के लिए कोई क्रिया नहीं, इसलिए ‘नश्यति’ भी गलत हो सकता है। केवल ‘केशलुञ्चनवेदना’ पक्का। दूसरी पंक्ति का "
           "वाक्य इस कार्ड से आगे चलता है (सम्भवतः); फल यहाँ नहीं। सन्धि जाँची: च + आहारः → चाहारः (अ + आ → आ); कण्ठामयात् + ऋते → "
           "कण्ठामयादृते (स्वर से पहले त् → द्); छपा ‘कंठं’ = कण्ठम्। ऋते पञ्चमी के साथ।"),
    "26": ("श्लोक; विश्वास मध्यम; कोई पाठ-चिह्न नहीं; दो छपी पंक्तियाँ (०२.१०.५० और ०२.१०.५१)। ‘उदीर्यते’ आत्मनेपद ‘उठती है’ लिया गया; "
           "कर्मवाच्य ‘उकसाई जाती है’ भी सम्भव। ‘प्रेताकृति’ = प्रेत की आकृति; किसकी, छपा नहीं। ‘नैव वा’ = अथवा बिलकुल नहीं। सन्धि जाँची: "
           "प्रतीपतः + यान्ति → प्रतीपतो यान्ति (अः + घोष व्यंजन → ओ); प्रेत + आकृतिः → प्रेताकृतिः; प्रेताकृतिः + उदीर्यते → "
           "प्रेताकृतिरुदीर्यते (इः + स्वर → इर्); भवेत् + नित्या → भवेन्नित्या (अनुनासिक से पहले त् → न्, वैकल्पिक; द् भी शुद्ध); "
           "न + एव → नैव (अ + ए → ऐ)।"),
    "27": ("डेटा में प्रकार गद्य (prose) है, यद्यपि पंक्तियाँ छन्द-जैसी लगती हैं; प्रकार वैसा ही रखा, छन्द पर कुछ नहीं कहा। विश्वास मध्यम। "
           "पाठ-चिह्न (सम्भव): ‘वक्रमार्प्यते’ → ‘वक्त्रम् आपूर्यते’ (मुख भर जाता है); छपा ‘आर्प्यते’ का अर्थ ‘रखा जाता है’ होगा; दोनों "
           "षष्ठी ‘अश्रूणाम्’ के साथ अटपटे; पूरा सुधार अनुमानित, इस पर प्रश्न नहीं। ‘स्विद्यतः’ = प्रथम पुरुष द्विवचन, ‘चरणौ’ के साथ "
           "(डेटा)। ‘वक्त्र’ = मुख या मुँह। सन्धि जाँची: स्विद्यतः + चरणौ → स्विद्यतश्चरणौ और चक्षुः + च → चक्षुश्च (च से पहले विसर्ग → "
           "श्); च + आकुलताम् → चाकुलताम् (अ + आ → आ)।"),
    "28": ("श्लोक; विश्वास कम; दो छपी पंक्तियाँ (०२.१०.५४ और ०२.१०.५५)। पाठ-चिह्न (सम्भव): ‘कथयेच्च च’ में दो ‘च’ अटपटे; छपाई में "
           "न्न को च्च पढ़ा जा सकता है, तब ‘कथयेन्न च’ = ‘पूछे जाने पर भी न कहे’, उलटा अर्थ; यह अपनाया नहीं गया, छपा पाठ ही अनूदित है; "
           "दूसरे ‘च’ का कार्य अस्पष्ट है, उसका अनुवाद नहीं किया गया। इसलिए वैद्य के कहने या न कहने पर कोई प्रश्न नहीं। ‘मरणम्’ सम्भवतः कार्ड २९ की षष्ठियों से पूरा "
           "होता है। ‘कथयेत्’ दसवें गण का है, णिजन्त नहीं। सन्धि जाँची: भावैः + अरतिः → भावैररतिः (ऐः + स्वर → ऐर्); अरतिः + तैः → "
           "अरतिस्तैः (त से पहले विसर्ग → स्); पृष्टः + अपि → पृष्टोऽपि (अः + अ → ओऽ); कथयेत् + च → कथयेच्च।"),
    "29": ("श्लोक; विश्वास कम; दो छपी पंक्तियाँ (०२.१०.५६ और ०२.१०.५७)। पाठ-चिह्न (सम्भव): ‘चिकित्सितं’ → ‘चिकित्सितुम्’ (इच्छेत् के "
           "बाद तुमुन् अपेक्षित); ‘-रूपास्यते’ का दीर्घ ऊ छपाई की भूल, पाठ ‘परासुर् उपास्यते’। ‘गतासोः’ और ‘बन्धुमित्राणाम्’ सम्भवतः "
           "कार्ड २८ के ‘मरणम्’ से जुड़ते हैं; सम्बन्ध निश्चित नहीं। ‘गतासु’ मरणासन्न या मृत, यहाँ सम्भवतः मरणासन्न। ‘यत्’ = क्योंकि। "
           "वाक्य कार्ड ३० में आगे (सम्भवतः)। सन्धि जाँची: गतासोः + बन्धु- → गतासोर्बन्धु- (ओः + घोष → ओर्); न च इच्छेत् → न चेच्छेत् "
           "(अ + इ → ए); इच्छेत् + तम् → इच्छेत्तम्; -आद्यैः + यत् → -आद्यैर्यत् (ऐः + घोष → ऐर्)।"),
    "30": ("श्लोक; विश्वास मध्यम; कोई पाठ-चिह्न नहीं; दो छपी पंक्तियाँ (०२.१०.५८ और ०२.१०.५९)। पहली पंक्ति कार्ड २९ को पूरा करती है "
           "(सम्भवतः): ‘घ्नद्भिः’ वहाँ के तृतीया पदों का विशेषण। ‘परिवर्जयेत्’ का कर्ता छपा नहीं। ‘अरिष्टम्’ = अ-रिष्ट (रिष्ट के बिना), "
           "‘मरणम्’ के साथ; ‘दृष्टरिष्टम्’ = दृष्ट + रिष्ट (दृष्ट + अरिष्ट होता तो आ दिखता)। समीक्षक: ‘च’ से ‘नास्ति’ दूसरे वाक्य में भी "
           "जा सकता है: ‘और रिष्ट दिखने पर जीवन नहीं’; यह कार्ड ३१ और ३२ से अधिक मेल खाता है; मालिक के लिए खुला, इस पर प्रश्न नहीं। "
           "सन्धि जाँची: घ्नद्भिः + औषध- → घ्नद्भिरौषध- (इः + स्वर → इर्); न + अस्ति → नास्ति (अ + अ → आ)।"),
    "31": ("श्लोक; विश्वास मध्यम; कोई पाठ-चिह्न नहीं; दो छपी पंक्तियाँ (०२.१०.६० और ०२.१०.६१)। पहली पंक्ति में क्रिया नहीं। ‘झूठा रिष्ट "
           "पहचानना’ और ‘सच्चा रिष्ट न पहचानना’ डेटा का अनुमान है, शब्द छपे नहीं। ‘इति’ = इस प्रकार। ‘पठ्यते’ का कर्म छपा नहीं; "
           "सम्भवतः कार्ड ३२ की बात। चरक और सुश्रुत दो आचार्यों के नाम माने गए। सन्धि जाँची: रिष्टेषु + अनैपुणात् → रिष्टेष्वनैपुणात् "
           "(उ + भिन्न स्वर → व्); चरकस्य + इति → चरकस्येति (अ + इ → ए)।"),
    "32": ("श्लोक; विश्वास मध्यम; कोई पाठ-चिह्न नहीं; दो छपी पंक्तियाँ (०२.१०.६२ और ०२.१०.६३)। टिप्पणी ‘क्रिया अगली में’ छपी पंक्ति गिनती "
           "है: ‘निवार्यते’ इसी कार्ड की दूसरी पंक्ति में है, इसलिए वाक्य इसी कार्ड में पूरा। ‘तत्’ (नपुं.) अगली क्रिया का कर्ता; मृत्यु या "
           "उसकी निश्चितता, छपा नहीं। ‘ध्रुवम्’ क्रियाविशेषण ‘निश्चय ही’ भी हो सकता है। रसायन = पुनर्यौवनकारी चिकित्सा (मानक)। सन्धि "
           "जाँची: ब्राह्मणैः + तत् → ब्राह्मणैस्तत् (त से पहले विसर्ग → स्); किल + अमलैः → किलामलैः (अ + अ → आ); तपस् + दान → तपोदान "
           "(अस् + घोष व्यंजन → ओ); -तत्परैः + च → -तत्परैश्च (च से पहले विसर्ग → श्)।"),
    "33": ("डेटा में प्रकार गद्य (prose) है, यद्यपि पंक्तियाँ छन्द-जैसी लगती हैं; प्रकार वैसा ही रखा, छन्द पर कुछ नहीं कहा। विश्वास मध्यम। "
           "पाठ-चिह्न (सम्भव): ‘कृष्णातरेयो’ ज्ञात नाम नहीं; ‘कृष्णात्रेयो’ अनुमान; इस पर प्रश्न नहीं। पहली पंक्ति में क्रिया नहीं (‘कहते "
           "हैं’ समझा जाता है)। ‘अपि’ को ‘दोषाणाम्’ के साथ लिया: दोषों से भी, बिना सच्चे रिष्ट के रिष्ट-जैसा रूप। सन्धि जाँची: "
           "कृष्णात्रेयः + द्विधा → कृष्णात्रेयो द्विधा (अः + घोष व्यंजन → ओ); स्थिर + अस्थिर → स्थिरास्थिर (अ + अ → आ); दोषाणाम् + अपि "
           "→ दोषाणामपि; बाहुल्यात् + रिष्ट- → बाहुल्याद्रिष्ट- (घोष र से पहले त् → द्); रिष्ट + आभासः → रिष्टाभासः।"),
    "34": ("श्लोक; विश्वास मध्यम; कोई पाठ-चिह्न नहीं; दो छपी पंक्तियाँ (०२.१०.६६ और ०२.१०.६७)। ‘शाम्येत्’ का अनकहा कर्ता कार्ड ३३ का "
           "रिष्टाभास, और ‘स्थायि’ कार्ड ३३ का स्थिर रिष्ट (डेटा, सम्भवतः)। ‘स्थायि’ स्थायी (पुं.) या स्थायि (नपुं.) हो सकता है, "
           "इसलिए लिंग नहीं दिया। दूसरे वाक्य में क्रिया समझी जाती है। ‘यत्’ = जो, ‘फलम्’ (नपुं.) के साथ; मुख्य वाक्य कार्ड ३५ में "
           "(सम्भवतः)। सन्धि जाँची: तत् + दोषाणाम् → तद्दोषाणाम् (घोष द से पहले त् → द्); शाम्येत् + स्थायि → शाम्येत्स्थायि; स्थायि + "
           "अवश्यम् → स्थाय्यवश्यम् (इ + भिन्न स्वर → य्); यत् + आयुर्ज्ञे → यदायुर्ज्ञे (स्वर से पहले त् → द्)।"),
    "35": ("डेटा में प्रकार गद्य (prose) है; पहली पंक्ति छन्द-जैसी लगती है, दूसरी पुष्पिका है; प्रकार वैसा ही रखा। विश्वास मध्यम; कोई "
           "पाठ-चिह्न नहीं। ‘आदृत’ सक्रिय अर्थ ‘ध्यान देने वाला’ लिया; ‘रिष्ट-ज्ञान के लिए सम्मानित’ भी सम्भव, पर कम स्वाभाविक। "
           "पुष्पिका का ‘इति’ = इस प्रकार; शीर्षक लिप्यन्तरित रखा, विश्लेषण ‘विकृत-ईहा-विज्ञानीय’ सम्भावित। सन्धि जाँची: "
           "रिष्टज्ञान + आदृतः → रिष्टज्ञानादृतः (अ + आ → आ); आदृतः + तस्मात् → आदृतस्तस्मात् (त से पहले विसर्ग → स्); सर्वदा + एव → "
           "सर्वदैव (आ + ए → ऐ); भवेत् + भिषक् → भवेद्भिषक् (घोष भ से पहले त् → द्); दशमः + अध्यायः → दशमोऽध्यायः (अः + अ → ओऽ)।"),
}

# ================================================================ AIDS
AIDS = {
    "24": {
        "chunks": "षडेतानि | निवर्तंते | षड्भिर्मासैर्मरिष्यतः || मत्तवद्गातिवाक्कम्पमोहा | मासान्मरिष्यतः",
        "contrast": ("छह मास: ‘ये छह’ हट जाते हैं (कार्ड २३ की सूची, सम्भवतः) ⇄ एक मास: वाणी, कम्प, मोह (और ‘गाति’, "
                     "अस्पष्ट); ‘मत्तवत्’ कितनों पर, तय नहीं। दोनों काल इसी इकाई में।"),
        "sandhi": ("स्वर से पहले ट् → ड्: षट् + एतानि → षडेतानि · घोष से पहले ऐः → ऐर्: मासैः + मरिष्यतः → मासैर्मरिष्यतः · "
                   "अनुनासिक म से पहले त् → न् (वैकल्पिक; द् भी शुद्ध): मासात् + मरिष्यतः → मासान्मरिष्यतः।"),
        "anchors": "पक्का: छह, छह मास, वाणी, कम्प, मोह, एक मास। अस्पष्ट: ‘गाति’ (गति या गात्र)। (मेरी याद-पद्धति)",
    },
    "25": {
        "chunks": "नश्यत्यज्ञाननूषड्हात्केशलुंचनवेदनां || न याति | यस्य | चाहारः | कंठं | कंठामयादृते",
        "sandhi": "अ + आ → आ: च + आहारः → चाहारः · स्वर से पहले त् → द्: कण्ठामयात् + ऋते → कण्ठामयादृते।",
        "anchors": "पक्का: केशलुञ्चनवेदना; आहार गले तक न जाए, कण्ठ-रोग के सिवा। अस्पष्ट: पहली पंक्ति का बाकी भाग। (मेरी याद-पद्धति)",
    },
    "26": {
        "chunks": "प्रेष्याः | प्रतीपतो यांति | प्रेताकृतिरुदीर्यते || यस्य | निद्राभवेन्नित्या | नैव वा | न स जीवति",
        "seesaw": "नित्या निद्रा (सदा नींद) ⇄ नैव (नींद बिलकुल नहीं): दोनों इसी इकाई में; दोनों के साथ ‘न स जीवति’।",
        "sandhi": ("अः + घोष व्यंजन → ओ: प्रतीपतः + यान्ति → प्रतीपतो यान्ति · इः + स्वर → इर्: प्रेताकृतिः + उदीर्यते → "
                   "प्रेताकृतिरुदीर्यते · अ + ए → ऐ: न + एव → नैव।"),
        "frame": "पहली पंक्ति: सेवक उलटे चलें, प्रेत-आकृति उठे · दूसरी पंक्ति: जिसकी नींद सदा हो या कभी न हो → फल: न स जीवति।",
    },
    "27": {
        "chunks": "वक्रमार्प्यतेऽश्रूणां | स्विद्यतश्चरणौ भृशं || चक्षुश्चाकुलतां याति | यमराष्ट्रं गमिष्यतः",
        "sandhi": ("च से पहले विसर्ग → श्: स्विद्यतः + चरणौ → स्विद्यतश्चरणौ, चक्षुः + च → चक्षुश्च · अ + आ → आ: च + आकुलताम् → "
                   "चाकुलताम्।"),
        "anchors": "पक्का: पैर बहुत पसीजें; आँख व्याकुल; यम-राष्ट्र जाने वाला। अनुमान: मुख आँसुओं से भरे। (मेरी याद-पद्धति)",
    },
    "28": {
        "chunks": "यैः पुरा रमते | भावैररतिस्तैर्न जीवति || कथयेच्च च | पृष्टोऽपि | दुःश्रवं | मरणंभिषक्",
        "frame": "किनसे: यैः पुरा रमते भावैः (जिनमें पहले रमता था) → क्या: अरतिः तैः (उन्हीं से अरुचि) → फल: न जीवति।",
        "sandhi": ("ऐः + स्वर → ऐर्: भावैः + अरतिः → भावैररतिः · त से पहले विसर्ग → स्: अरतिः + तैः → अरतिस्तैः · अः + अ → ओऽ: "
                   "पृष्टः + अपि → पृष्टोऽपि।"),
        "anchors": "पक्का: पहली पंक्ति। खुला: ‘कथयेच्च च’ या ‘कथयेन्न च’, अर्थ उलटा हो जाता है। (मेरी याद-पद्धति)",
    },
    "29": {
        "chunks": "गतासोर्बंधुमित्राणां | न चेच्छेत्तं | चिकित्सितं || यमदूतपिशाचाद्यैर्यत्परासुरूपास्यते",
        "sandhi": ("ओः + घोष → ओर्: गतासोः + बन्धु- → गतासोर्बन्धु- · अ + इ → ए: च + इच्छेत् → चेच्छेत् · ऐः + घोष → ऐर्: "
                   "-आद्यैः + यत् → -आद्यैर्यत्।"),
        "anchors": "पक्का: गतासु, बन्धु-मित्र, न चेच्छेत्, यमदूत-पिशाच आदि, परासु। अनुमान: चिकित्सितुम्, उपास्यते। (मेरी याद-पद्धति)",
    },
    "30": {
        "chunks": "घ्नद्भिरौषधवीर्याणि | तस्मात्तं परिवर्जयेत् || अरिष्टं नास्ति मरणं | दृष्टरिष्टं च जीवितं",
        "chain": {"steps": ["घ्नद्भिः औषधवीर्याणि: औषध-वीर्य नष्ट करने वालों द्वारा", "तस्मात्: इसलिए", "तं परिवर्जयेत्: उससे बचे",
                            "अरिष्टं नास्ति मरणम्: रिष्ट के बिना मृत्यु नहीं"]},
        "sandhi": "इः + स्वर → इर्: घ्नद्भिः + औषध- → घ्नद्भिरौषध- · अ + अ → आ: न + अस्ति → नास्ति।",
    },
    "31": {
        "chunks": "अरिष्टे रिष्टविज्ञानं | न च रिष्टेष्वनैपुणात् || चरकस्येति वचनं | सुश्रुतेन तु पठ्यते",
        "contrast": "चरक: यह वचन (पहली पंक्ति) ⇄ सुश्रुत: ‘तु पठ्यते’, आगे की बात (सम्भवतः कार्ड ३२)। दोनों नाम इसी इकाई में।",
        "sandhi": "उ + भिन्न स्वर → व्: रिष्टेषु + अनैपुणात् → रिष्टेष्वनैपुणात् · अ + इ → ए: चरकस्य + इति → चरकस्येति।",
    },
    "32": {
        "chunks": "ध्रुवं हि रिष्टे मरणं | ब्राह्मणैस्तत्किलामलैः || रसायनतपोदानतत्परैश्च | निवार्यते",
        "diagram": {"groups": [
            {"label": "ध्रुवं हि रिष्टे मरणम्", "items": ["रिष्ट में मृत्यु निश्चित"]},
            {"label": "तत् किल निवार्यते (कहते हैं, टाला जाता है)",
             "items": ["अमलैः ब्राह्मणैः", "रसायन-तप-दान-तत्परैः"]}]},
        "sandhi": ("त से पहले विसर्ग → स्: ब्राह्मणैः + तत् → ब्राह्मणैस्तत् · अ + अ → आ: किल + अमलैः → किलामलैः · अस् + घोष "
                   "व्यंजन → ओ: तपस् + दान → तपोदान।"),
    },
    "33": {
        "chunks": "कृष्णातरेयो | द्विधा रिष्टं | स्थिरास्थिरविभेदतः || दोषाणामपि | बाहुल्याद्रिष्टाभासः | समुद्भवेत्",
        "diagram": {"groups": [
            {"label": "द्विधा रिष्टम्", "items": ["स्थिर", "अस्थिर"]},
            {"label": "दोषाणां बाहुल्यात्", "items": ["रिष्टाभासः समुद्भवेत्"]}]},
        "sandhi": ("अ + अ → आ: स्थिर + अस्थिर → स्थिरास्थिर · घोष र से पहले त् → द्: बाहुल्यात् + रिष्ट- → बाहुल्याद्रिष्ट- · "
                   "अ + आ → आ: रिष्ट + आभासः → रिष्टाभासः।"),
    },
    "34": {
        "chunks": "तद्दोषाणां शमे | शाम्येत्स्थाय्यवश्यं तु मृत्यवे || आयुर्वेदफलं कृत्स्नं | यदायुर्ज्ञे प्रतिष्ठितं",
        "seesaw": "शाम्येत् (दोष शान्त हों तो शान्त) ⇄ स्थायि (टिका रहे, अवश्य मृत्यु के लिए): दोनों इसी इकाई में; बीच में ‘तु’।",
        "sandhi": ("घोष द से पहले त् → द्: तत् + दोषाणाम् → तद्दोषाणाम् · इ + भिन्न स्वर → य्: स्थायि + अवश्यम् → स्थाय्यवश्यम् · "
                   "स्वर से पहले त् → द्: यत् + आयुर्ज्ञे → यदायुर्ज्ञे।"),
    },
    "35": {
        "chunks": "रिष्टज्ञानादृतस्तस्मात् | सर्वदैव | भवेद्भिषक् || इति विकृतेहाविज्ञानीयो नाम दशमोऽध्यायः",
        "frame": "क्यों: तस्मात् (इसलिए) → कौन: भिषक् (वैद्य) → कब: सर्वदैव (सदा ही) → कैसा: रिष्टज्ञानादृतः (रिष्ट-ज्ञान पर ध्यान देने वाला)।",
        "sandhi": ("आ + ए → ऐ: सर्वदा + एव → सर्वदैव · घोष भ से पहले त् → द्: भवेत् + भिषक् → भवेद्भिषक् · अः + अ → ओऽ: दशमः + "
                   "अध्यायः → दशमोऽध्यायः।"),
    },
}

# ================================================================ IMAGE_SPECS
IMAGE_SPECS = {
    ("24", "contrast"): {
        "file": "sh10-masa-24.svg",
        "alt": ("Table of card 24: one who will die in six months, from whom 'these six' turn away (probably the six of "
                "card 23); one who will die in a month, with speech, tremor and bewilderment, compared with a drunk man (how far "
                "the comparison reaches is open; gait is a doubtful reading)."),
        "type": "table",
        "title": "कार्ड २४: दो काल, दो लक्षण-समूह",
        "heads": ["काल", "छपा लक्षण"],
        "rows": [["छह मास में मरने वाला", "ये छह हट जाते हैं (सम्भवतः कार्ड २३ के छह)"],
                 ["एक मास में मरने वाला", "वाणी, कम्प, मोह; ‘मत्तवत्’ कितनों पर, तय नहीं"],
                 ["एक मास: अस्पष्ट शब्द", "‘गाति’: गति या गात्र, तय नहीं"]],
    },
    ("26", "seesaw"): {
        "file": "sh10-nidra-26.svg",
        "alt": ("Split of card 26: sleep constant (nityā) and sleep not at all (naiva); with either, the text says he "
                "does not live."),
        "type": "split",
        "title": "कार्ड २६: नींद के दो उलटे रूप",
        "cols": [["नित्या निद्रा", ["नींद सदा बनी रहे", "न स जीवति"]],
                 ["नैव वा", ["नींद बिलकुल न हो", "न स जीवति"]]],
    },
    ("31", "contrast"): {
        "file": "sh10-charaka-sushruta-31.svg",
        "alt": ("Split of card 31: Caraka's statement, knowledge of riṣṭa where there is none and none in riṣṭas, from "
                "lack of skill; Suśruta recites what follows (probably card 32)."),
        "type": "split",
        "title": "कार्ड ३१: दो आचार्य",
        "cols": [["चरक का वचन", ["अरिष्टे रिष्टविज्ञानम्", "न च रिष्टेषु", "कारण: अनैपुण"]],
                 ["सुश्रुत द्वारा पठित", ["सुश्रुतेन तु पठ्यते", "आगे की बात", "(सम्भवतः कार्ड ३२)"]]],
    },
    ("32", "diagram"): {
        "file": "sh10-nivaryate-32.svg",
        "alt": ("Flowchart of card 32: in riṣṭa death is certain; that, it is said, is warded off by stainless "
                "brāhmaṇas and by those intent on rasāyana, austerity and giving."),
        "type": "mermaid",
        "code": ("flowchart TD\n"
                 "  A[\"रिष्ट में मृत्यु ध्रुव\"] --> B[\"किल: वह टाला जाता है\"]\n"
                 "  B -- \"द्वारा\" --> C[\"निर्मल ब्राह्मण\"]\n"
                 "  B -- \"द्वारा\" --> D[\"रसायन, तप, दान में लगे\"]\n"),
    },
    ("33", "diagram"): {
        "file": "sh10-dvidha-33.svg",
        "alt": ("Flowchart of card 33: riṣṭa is twofold, stable and unstable; from an abundance of the doṣas a "
                "semblance of riṣṭa may arise."),
        "type": "mermaid",
        "code": ("flowchart TD\n"
                 "  A[\"द्विधा रिष्ट\"] --> B[\"स्थिर\"]\n"
                 "  A --> C[\"अस्थिर\"]\n"
                 "  D[\"दोषों का बाहुल्य\"] --> E[\"रिष्टाभास हो सकता है\"]\n"),
    },
    ("34", "seesaw"): {
        "file": "sh10-sthayi-34.svg",
        "alt": ("Split of card 34: what subsides when those doṣas subside (the semblance of card 33, data's reading); "
                "the lasting one, certainly for death (the stable riṣṭa, data's reading)."),
        "type": "split",
        "title": "कार्ड ३४: शान्त होने वाला और स्थायी",
        "cols": [["शाम्येत्", ["दोष शान्त हों तो शान्त", "(रिष्टाभास, डेटा का पाठ)"]],
                 ["स्थायि", ["अवश्यं मृत्यवे", "(स्थिर रिष्ट, डेटा का पाठ)"]]],
    },
}
