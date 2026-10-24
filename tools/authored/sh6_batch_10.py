from helpers import mcq, match, order, fill, multi, accepts


AUTHORED = {}

# ---------------------------------------------------------------- unit 116
AUTHORED["116"] = {
    "title": "अपरे पुनः शुक्रस्य सारं",
    "question": "By unit 116, what do 'others' (apare) hold the essence (sāra) of śukra to be?",
    "rule": ("Others, however (अपरे पुनः), hold the essence of śukra (शुक्रस्य सारम्) to be the garbha (embryo) "
             "itself (गर्भमेव आमनन्ति)."),
    "limits": ("Prose; a view of 'others', with no reason given. The two accusatives are read 'hold X to be Y'; the "
               "data's other reading ('declare the garbha, the essence of śukra') gives the same sense. The line does "
               "not say whose view it is or whether the author accepts it."),
    "explain_hi": ("यह गद्य-पंक्ति एक मतान्तर बताती है: दूसरे लोग (अपरे) शुक्र यानी वीर्य के सार को ही गर्भ यानी भ्रूण मानते हैं। "
                   "‘आमनन्ति’ के साथ दो द्वितीया हैं: शुक्र का सार और गर्भ; अर्थ है ‘X को Y मानते हैं’। "
                   "डेटा का दूसरा पाठ (‘शुक्र के सार, गर्भ को ही कहते हैं’) भी यही अर्थ देता है। "
                   "यह मत किसका है और लेखक इसे मानता है या नहीं, पंक्ति नहीं कहती। "
                   "‘एवामनन्ति’ में एव का अ और आमनन्ति का आ मिलकर आ बने हैं।"),
    "hook": "दूसरों का मत: शुक्र का सार ही गर्भ।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 116, what do the others hold the essence of śukra (semen) to be?",
            ("The garbha (embryo) itself", "शुक्रस्य सारं गर्भमेव आमनन्ति: the essence of śukra is held to be the garbha itself."),
            [("The majjā (marrow) itself", "Marrow is not the essence of śukra; card 113 makes śukra the essence of marrow."),
             ("The rakta (blood) itself", "Blood is not named in unit 116 or as the essence of śukra."),
             ("The medas (body fat) itself", "Fat is not named in unit 116 or as the essence of śukra.")],
            "Others hold the essence of śukra to be the garbha (embryo) itself.",
            "अपरे पुनः शुक्रस्य सारं गर्भमेवामनंति."),
        order(1, "Put the printed words of unit 116 in the line's order.",
              ["अपरे पुनः", "शुक्रस्य", "सारं", "गर्भमेवामनंति"],
              "Others, however; of śukra; the essence; the garbha itself they hold.",
              "अपरे पुनः → शुक्रस्य → सारं → गर्भमेवामनंति."),
        match(2, "Match each word of unit 116 to its meaning.",
              [["अपरे", "others"], ["पुनः", "however"], ["सार", "essence"], ["गर्भ", "embryo"],
               ["आमनन्ति", "they hold (to be)"]],
              "अपरे = others; पुनः = however; सार = essence; गर्भ = embryo; आमनन्ति = they hold.",
              "अपरे, पुनः, सार, गर्भ, आमनन्ति.", role="extend",
              teaches="आमनन्ति (ā-√mnā, 3rd plural present) takes two accusatives here: 'they hold X to be Y'."),
        mcq("discriminate", 3, "Which split of गर्भमेवामनंति in unit 116 is right?",
            ("गर्भम् + एव + आमनन्ति", "म् joins the vowel ए; अ + आ → आ: एव + आमनन्ति → एवामनन्ति."),
            [("गर्भ + मेव + आमनन्ति", "मेव is not a word; the म् belongs to गर्भम्."),
             ("गर्भम् + इव + आमनन्ति", "म् + इ would give गर्भमिवा-, not गर्भमेवा-."),
             ("गर्भम् + एव + मनन्ति", "एव + म- would give एवमनन्ति, with a short अ.")],
            "गर्भम् (the embryo) + एव (itself) + आमनन्ति (they hold).",
            "अ + आ → आ; म् joins a following vowel."),
        multi("apply", 4, "Which statements fit unit 116?",
              [("The line gives a reason for the view", "No reason is printed in unit 116."),
               ("The view is given as that of others (अपरे)", "Right: अपरे पुनः, others, however."),
               ("It names the garbha the waste (mala) of śukra", "The garbha is named the essence (सार), not a waste."),
               ("The essence of śukra is held to be the garbha", "Right: शुक्रस्य सारं गर्भमेव आमनन्ति.")],
              [1, 3],
              "Others hold the essence of śukra to be the garbha; no reason is given.",
              "अपरे पुनः शुक्रस्य सारं गर्भमेवामनंति."),
        mcq("transfer", 5, "By the rule of एवामनन्ति (एव + आमनन्ति), how is न + आगच्छति (he does not come) joined in a new example?",
            ("नागच्छति", "अ + आ → आ, as एव + आमनन्ति → एवामनन्ति."),
            [("नगच्छति", "अ + आ does not give a short अ; it gives आ."),
             ("नेगच्छति", "ए comes from अ + इ, not from अ + आ."),
             ("नयागच्छति", "No य् comes between अ and आ.")],
            "न + आगच्छति = नागच्छति, like एव + आमनन्ति = एवामनन्ति.",
            "अ + आ → आ.",
            teaches="अ before आ merges into one long आ: एव + आमनन्ति → एवामनन्ति."),
    ],
}

# ---------------------------------------------------------------- unit 117
AUTHORED["117"] = {
    "title": "वायुः पुनरग्नेराहारस्य",
    "question": "By unit 117, through what and where does vāyu (wind) appear?",
    "rule": ("Vāyu (wind), through the abundance and scarcity (बह्वल्पतया) of the fire (अग्नेः) and of the food "
             "(आहारस्य), appears (प्रादुर्भवति) in the koṣṭha (belly cavity); it is called amūrta (non-corporeal) and "
             "śabdavān (having sound)."),
    "limits": ("Prose; confidence low. 'पंचातमा' is printed; पञ्चात्मा (five-natured) is a conjecture, and the five "
               "forms are not named. Mūrcchanā is of uncertain sense; the sense of ईषच्छब्दप्रचुर is uncertain. No "
               "question rests on these three words."),
    "explain_hi": ("यह कठिन गद्य-वाक्य वायु की उत्पत्ति बताता है: अग्नि और आहार की अधिकता और अल्पता (बह्वल्पता) से वायु कोष्ठ यानी पेट के भीतरी भाग में प्रकट होती है। "
                   "उसे अमूर्त (बिना ठोस रूप का) और शब्दवान् (शब्द वाला) कहा गया है। "
                   "‘मूर्च्छना’ का अर्थ अनिश्चित है (सम्भवतः प्रबलता), और ‘ईषच्छब्दप्रचुर’ का अर्थ भी पक्का नहीं। "
                   "छपा ‘पंचातमा’ अस्पष्ट है; ‘पञ्चात्मा’ (पाँच स्वरूप वाली) केवल अनुमानित पाठ है, और पाँच रूपों के नाम यहाँ नहीं हैं। "
                   "इसलिए प्रश्न केवल निश्चित अंशों पर हैं।"),
    "hook": "अग्नि और आहार कम-ज़्यादा: कोष्ठ में वायु प्रकट।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 117, where does vāyu (wind) appear (prādurbhavati)?",
            ("In the koṣṭha (belly cavity)", "कोष्ठे प्रादुर्भवति: it appears in the koṣṭha."),
            [("In the asthi (the bone tissue)", "No bone is named in unit 117."),
             ("In the tvac (the skin)", "No skin is named in unit 117."),
             ("In the netra (the eyes)", "No eye is named in unit 117.")],
            "Vāyu appears in the koṣṭha.",
            "कोष्ठे प्रादुर्भवति."),
        order(1, "Put these printed phrases of unit 117 in the line's order.",
              ["वायुः पुनरग्नेराहारस्य च", "बह्वल्पतया", "तस्मात्तस्मान्मूर्च्छनाविशेषात्", "कोष्ठे प्रादुर्भवति"],
              "Wind, however, of fire and food; through abundance and scarcity; from this-and-that mūrcchanā; appears in the koṣṭha.",
              "वायुः ... → बह्वल्पतया → ...मूर्च्छनाविशेषात् → कोष्ठे प्रादुर्भवति."),
        match(2, "Match each word of unit 117 to its meaning.",
              [["वायु", "wind"], ["अग्नि", "fire"], ["आहार", "food"], ["अमूर्त", "non-corporeal"],
               ["कोष्ठ", "storehouse, belly cavity"]],
              "वायु = wind; अग्नि = fire; आहार = food; अमूर्त = non-corporeal; कोष्ठ = belly cavity.",
              "वायु, अग्नि, आहार, अमूर्त, कोष्ठ.", role="extend",
              teaches="बह्वल्पता = बहु + अल्प + ता: a dvandva of 'much' and 'little' made abstract, 'abundance and scarcity'."),
        mcq("discriminate", 3, "Which split of पुनरग्नेराहारस्य in unit 117 is right?",
            ("पुनर् + अग्नेः + आहारस्य", "एः before the vowel आ → एर्: अग्नेः + आहारस्य → अग्नेराहारस्य."),
            [("पुनः + अग्ने + राहारस्य", "राहारस्य is not a word; the र् comes from the visarga."),
             ("पुनर् + अग्ने + आहारस्य", "ए + आ would give अग्न आहारस्य, never अग्नेरा-."),
             ("पुनर् + अग्निः + आहारस्य", "इः + आ would give अग्निराहारस्य, not अग्नेरा-.")],
            "पुनर् (however) + अग्नेः (of the fire) + आहारस्य (of the food).",
            "A vowel other than अ/आ + visarga before a voiced sound → र्."),
        mcq("apply", 4, "By unit 117, through what does vāyu appear in the koṣṭha?",
            ("Abundance and scarcity of fire and food", "अग्नेराहारस्य च बह्वल्पतया: by the much-and-little of fire and food."),
            [("Abundance and scarcity of water and sleep", "Neither water nor sleep is named in unit 117."),
             ("Abundance and scarcity of blood and fat", "Neither blood nor fat is named in unit 117."),
             ("Abundance and scarcity of heat and cold", "Neither heat nor cold is named in unit 117.")],
            "Through the abundance and scarcity of the fire and of the food.",
            "अग्नेराहारस्य च बह्वल्पतया."),
        mcq("transfer", 5, "By the rule of बह्वल्प (बहु + अल्प), how is मधु + अत्र (honey here) joined in a new example?",
            ("मध्वत्र", "उ before a different vowel becomes व्, as बहु + अल्प → बह्वल्प."),
            [("मधोत्र", "ओ comes from अ + उ, not from उ + अ."),
             ("मधूत्र", "ऊ comes from उ + उ, not from उ + अ."),
             ("मधुत्र", "The अ is not simply lost after उ.")],
            "मधु + अत्र = मध्वत्र, like बहु + अल्प = बह्वल्प.",
            "उ + a different vowel → व्.",
            teaches="उ before a different vowel becomes व्: बहु + अल्प → बह्वल्प."),
    ],
}

# ---------------------------------------------------------------- unit 118
AUTHORED["118"] = {
    "title": "एवं च कृत्वा देहेऽन्नमया",
    "question": "By unit 118, what are all the bhāvas (states, entities) in the body made of?",
    "rule": ("This being so (एवं च कृत्वा, literally 'and having done thus'), all bhāvas in the body (देहे सर्वे भावाः) "
             "are made of food alone (अन्नमया एव)."),
    "limits": ("Prose; the copula is understood. 'एवं च कृत्वा' is rendered literally; the idiom is probably 'this being "
               "so'. The line does not list the bhāvas or say how food makes them."),
    "explain_hi": ("यह गद्य-पंक्ति एक निष्कर्ष देती है: इस प्रकार देह में सभी भाव यानी पदार्थ या अवस्थाएँ अन्न से ही बने हैं (अन्नमय)। "
                   "‘एवं च कृत्वा’ का शाब्दिक अर्थ ‘और ऐसा करके’ है; मुहावरे में सम्भवतः ‘ऐसा होने से’। "
                   "‘अन्नमय’ में -मय प्रत्यय ‘से बना हुआ’ बताता है। "
                   "छपे ‘अन्नमया एव’ में आः का विसर्ग स्वर से पहले लुप्त हुआ है। "
                   "कौन-कौन से भाव, यह पंक्ति नहीं गिनाती।"),
    "hook": "देह के सब भाव अन्नमय।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 118, what are all the bhāvas in the body made of?",
            ("Food (anna) alone", "अन्नमया एव: made of food alone."),
            [("Fire (agni) alone", "Unit 118 says अन्नमय, made of food, not of fire."),
             ("Wind (vāyu) alone", "Unit 118 says अन्नमय, made of food, not of wind."),
             ("Water (jala) alone", "Unit 118 says अन्नमय, made of food, not of water.")],
            "All bhāvas in the body are made of food alone.",
            "देहेऽन्नमया एव सर्वे भावाः."),
        order(1, "Put the printed words of unit 118 in the line's order.",
              ["एवं च कृत्वा", "देहेऽन्नमया", "एव", "सर्वे भावाः"],
              "This being so; in the body made of food; alone; all bhāvas.",
              "एवं च कृत्वा → देहेऽन्नमया → एव → सर्वे भावाः."),
        match(2, "Match each word of unit 118 to its meaning.",
              [["एवम्", "thus"], ["कृत्वा", "having done"], ["देह", "body"], ["अन्नमय", "made of food"],
               ["भाव", "state, entity"]],
              "एवम् = thus; कृत्वा = having done; देह = body; अन्नमय = made of food; भाव = state.",
              "एवम्, कृत्वा, देह, अन्नमय, भाव.", role="extend",
              teaches="-मय added to a noun means 'made of': अन्न (food) → अन्नमय (made of food)."),
        mcq("discriminate", 3, "Why is देहे + अन्नमयाः printed देहेऽन्नमयाः in unit 118?",
            ("After ए, the अ is dropped, marked ऽ", "ए + अ: the ए stays and the अ is dropped, marked by ऽ."),
            [("The ए becomes अय् before the following अ", "ए + अ does not give अय् here; the print keeps ए and marks ऽ."),
             ("The ए and the अ merge into ऐ", "ऐ comes from अ + ए, not from ए + अ."),
             ("The ए is dropped before the अ", "The ए stays (देहे-); it is the अ that is dropped.")],
            "देहे (in the body) + अन्नमयाः: after ए the अ is dropped, written ऽ.",
            "ए + अ → एऽ."),
        mcq("apply", 4, "Why is अन्नमयाः printed अन्नमया before एव in unit 118?",
            ("आः drops its visarga before a vowel", "After आ the visarga is lost before a voiced sound, vowels included."),
            [("आः becomes ओ before a vowel", "ओ comes from अः before a voiced consonant, not from आः."),
             ("आः becomes आर् before a vowel", "र् comes after vowels other than अ/आ, not after आ."),
             ("आः becomes आस् before a vowel", "स् comes before त or थ, not before a vowel.")],
            "अन्नमयाः + एव → अन्नमया एव: आः loses its visarga before a voiced sound.",
            "आः + voiced sound → आ (visarga dropped)."),
        mcq("transfer", 5, "By the pattern of अन्नमय (made of food), what does सुवर्णमय mean in a new example?",
            ("Made of gold", "-मय = made of: सुवर्ण (gold) → सुवर्णमय, like अन्न → अन्नमय."),
            [("Fond of gold", "-मय does not mean fond of."),
             ("Free of gold", "-मय does not mean free of."),
             ("Giver of gold", "-मय does not mean giver of.")],
            "सुवर्णमय = made of gold, like अन्नमय = made of food.",
            "Noun + -मय = made of that noun.",
            teaches="-मय forms adjectives meaning 'made of': अन्नमय (unit 118)."),
    ],
}

# ---------------------------------------------------------------- unit 119
AUTHORED["119"] = {
    "title": "तेनैव चेदमेवं चिरेण",
    "question": "By unit 119, how is this body-machine (śarīra-yantra) kept going?",
    "rule": ("By that alone (तेनैव; the data reads it as the food of the preceding units), this body-machine "
             "(शरीरयन्त्रम्) is kept going (याप्यते) for a long time (चिरेण), with an unbroken flow (अनवरतप्रवाहेण), "
             "endowed with health, strength and growth (स्वास्थ्यबलोपचययुक्तम्)."),
    "limits": ("Prose; confidence low. 'न्यासमंतर्बहिः' is not clearly construed (as a deposit within and without, or "
               "placed within and without). 'यावत्कर्मोपादानं' may mean 'as long as karma is taken up' or 'as far as "
               "karma takes it'. No question rests on these two phrases."),
    "explain_hi": ("यह गद्य-वाक्य बताता है कि शरीर एक यन्त्र की तरह चलता रहता है। "
                   "उसी से (तेन, डेटा के अनुसार पिछली इकाइयों का अन्न) यह शरीर-यन्त्र देर तक, अटूट प्रवाह के साथ, स्वास्थ्य, बल और उपचय यानी वृद्धि से युक्त होकर चलाया जाता है (याप्यते)। "
                   "‘न्यासमन्तर्बहिः’ का अन्वय स्पष्ट नहीं: ‘भीतर-बाहर धरोहर की तरह’ या ‘भीतर-बाहर रखा हुआ’। "
                   "‘यावत्कर्मोपादानम्’ का अर्थ ‘जब तक कर्म का ग्रहण है’ या ‘जहाँ तक कर्म ले जाए’ हो सकता है। "
                   "इन दोनों अस्पष्ट अंशों पर कोई प्रश्न नहीं।"),
    "hook": "शरीर-यन्त्र: अटूट प्रवाह से, स्वास्थ्य-बल-वृद्धि सहित, देर तक चलता।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 119, the body is called a kind of what?",
            ("A machine (yantra)", "शरीरयन्त्रम्: the body-machine."),
            [("A war-chariot (ratha)", "No chariot is named in unit 119."),
             ("A house (gṛha)", "No house is named in unit 119."),
             ("A river (nadī)", "No river is named in unit 119.")],
            "The body is called a machine: शरीर-यन्त्र.",
            "शरीरयंत्रम्."),
        order(1, "Put these printed parts of unit 119 in the line's order.",
              ["तेनैव चेदमेवं चिरेण", "न्यासमंतर्बहिः", "शरीरयंत्रमनवरतप्रवाहेण", "याप्यते"],
              "By that alone, and this, thus, for long; as a deposit within and without; the body-machine with unbroken flow; is kept going.",
              "तेनैव ... → न्यासमंतर्बहिः → शरीरयंत्रमनवरतप्रवाहेण → याप्यते."),
        match(2, "Match each word of unit 119 to its meaning.",
              [["स्वास्थ्य", "health"], ["बल", "strength"], ["उपचय", "growth"], ["अनवरत", "unceasing"],
               ["प्रवाह", "flow"]],
              "स्वास्थ्य-बल-उपचय-युक्त = endowed with health, strength and growth; अनवरत-प्रवाह = unbroken flow.",
              "स्वास्थ्य, बल, उपचय, अनवरत, प्रवाह.", role="extend",
              teaches="स्वास्थ्य-बल-उपचय is a dvandva of three nouns, then tied to युक्त: 'endowed with health, strength and growth'."),
        mcq("discriminate", 3, "Which split of तेनैव in unit 119 is right?",
            ("तेन + एव", "अ + ए → ऐ: तेन + एव → तेनैव."),
            [("तेन + इव", "अ + इ would give तेनेव, with ए, not ऐ."),
             ("तेनः + एव", "There is no form तेनः; a visarga would leave तेन एव."),
             ("तेने + एव", "ए + ए would not give ऐ.")],
            "तेन (by that) + एव (alone).",
            "अ + ए → ऐ."),
        multi("apply", 4, "Which statements fit unit 119?",
              [("It is kept going for a long time (चिरेण)", "Right: चिरेण, for a long time."),
               ("The line makes the sense of न्यास plain", "No: the data finds न्यासमन्तर्बहिः not clearly construed."),
               ("It runs with an unbroken flow", "Right: अनवरतप्रवाहेण."),
               ("It is endowed with health, strength and growth", "Right: स्वास्थ्यबलोपचययुक्तम्.")],
              [0, 2, 3],
              "Kept going long, with unbroken flow, endowed with health, strength and growth; न्यास stays unclear.",
              "चिरेण ... अनवरतप्रवाहेण स्वास्थ्यबलोपचययुक्तं ... याप्यते."),
        mcq("transfer", 5, "By the rule of तेनैव (तेन + एव), how is अत्र + एव (here indeed) joined in a new example?",
            ("अत्रैव", "अ + ए → ऐ, as तेन + एव → तेनैव."),
            [("अत्रेव", "ए comes from अ + इ, not from अ + ए."),
             ("अत्रोव", "ओ comes from अ + उ, not from अ + ए."),
             ("अत्रयेव", "No य् comes between अ and ए.")],
            "अत्र + एव = अत्रैव, like तेन + एव = तेनैव.",
            "अ + ए → ऐ.",
            teaches="अ before ए gives ऐ (vṛddhi): तेन + एव → तेनैव."),
    ],
}

# ---------------------------------------------------------------- unit 120
AUTHORED["120"] = {
    "title": "अन्यथा त्वन्नरसोत्क्षेपादि",
    "question": "By unit 120, what happens otherwise (anyathā), and what are the two outcomes?",
    "rule": ("But otherwise (अन्यथा तु), with the srotas bound by the throwing up of food-rasa and the like, either "
             "(वा) it is cut off (व्यवच्छिद्यते) in the midst of the flow of the dhātus, or (वा) it becomes a vessel "
             "of disease (व्याधिभाजनं भवति)."),
    "limits": ("Prose; confidence low. The subject is not printed (the body-machine of card 119 is understood). "
               "बद्धस्रोतसा (instrumental) may instead be read srotasām (of the srotas bound by ...). No question rests "
               "on the subject or on how बद्धस्रोतसा is construed."),
    "explain_hi": ("यह गद्य-वाक्य इकाई ११९ का उलटा पक्ष बताता है: अन्यथा, अन्न-रस के उत्क्षेप (ऊपर फेंके जाने) आदि से स्रोतस् बँध जाने पर, दो में से एक होता है। "
                   "या तो (वा) ठीक से न जुड़ते धातु-प्रवाह के बीच वह कट जाता है (व्यवच्छिद्यते), या (वा) रोग का पात्र बन जाता है (व्याधिभाजनं भवति)। "
                   "कर्ता छपा नहीं; डेटा इकाई ११९ का शरीर-यन्त्र समझता है। "
                   "‘बद्धस्रोतसा’ तृतीया है, पर इसे ‘स्रोतसाम्’ (षष्ठी बहुवचन) भी पढ़ा जा सकता है। "
                   "यहाँ ‘उत्क्षेप’ का अर्थ ऊपर फेंकना है।"),
    "hook": "अन्यथा: या तो कट जाए, या रोग का पात्र बने।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 120, what are the two outcomes when things go otherwise (anyathā)?",
            ("It is cut off, or falls into disease", "व्यवच्छिद्यते ... व्याधिभाजनं वा भवति."),
            [("It grows, or gains in strength", "Growth and strength belong to unit 119, not to 'otherwise'."),
             ("It is cooked, or it changes into food", "Neither is named in unit 120."),
             ("It dries up, or turns into waste", "Neither is named in unit 120.")],
            "Either it is cut off, or it becomes a vessel of disease.",
            "व्यवच्छिद्यते व्याधिभाजनं वा भवति."),
        order(1, "Put the printed parts of unit 120 in the line's order.",
              ["अन्यथा त्वन्नरसोत्क्षेपादिबद्धस्रोतसा वा", "यथावदनभिसंधीयमानधातुप्रवाहमंतरा", "व्यवच्छिद्यते",
               "व्याधिभाजनं वा भवति"],
              "Otherwise, with srotas bound ...; in the midst of the not duly joined dhātu-flow; is cut off; or becomes a vessel of disease.",
              "अन्यथा ... → ...प्रवाहमंतरा → व्यवच्छिद्यते → व्याधिभाजनं वा भवति."),
        match(2, "Match each word of unit 120 to its meaning.",
              [["अन्यथा", "otherwise"], ["व्याधि", "disease"], ["भाजन", "vessel"], ["व्यवच्छिद्यते", "is cut off"],
               ["यथावत्", "duly"]],
              "अन्यथा = otherwise; व्याधि-भाजन = vessel of disease; व्यवच्छिद्यते = is cut off; यथावत् = duly.",
              "अन्यथा, व्याधि, भाजन, व्यवच्छिद्यते, यथावत्.", role="extend",
              teaches="वा ... वा, with one वा in each clause, means 'either ... or'."),
        mcq("discriminate", 3, "Which split of the printed यथावदनभिसंधीयमान- in unit 120 is right?",
            ("यथावत् + अनभिसन्धीयमान-", "त् before a vowel becomes द्: यथावत् + अ- → यथावदनभि-."),
            [("यथा + वदन् + अभिसन्धीयमान-", "वदन् + अ- would give वदन्नभि-, with two न."),
             ("यथावः + अनभिसन्धीयमान-", "अः before अ would give यथावोऽनभि-."),
             ("यथावत् + नभिसन्धीयमान-", "त् + न would give यथावन्नभि-.")],
            "यथावत् (duly) + अनभिसन्धीयमान (not being joined).",
            "त् + vowel → द्."),
        mcq("apply", 4, "In unit 120, what do the two वा (vā) mark?",
            ("Two alternatives: either ... or", "वा ... वा: either it is cut off, or it becomes a vessel of disease."),
            [("A cause and then its effect", "वा does not mark cause and effect."),
             ("Two steps one after another", "वा does not mark a sequence."),
             ("A question and then its answer", "वा does not mark question and answer.")],
            "वा ... वा = either ... or: two outcomes.",
            "वा ... वा = either ... or."),
        mcq("transfer", 5, "By the rule of यथावदनभि- (यथावत् + अ-), how is जगत् + अपि (the world too) joined in a new example?",
            ("जगदपि", "त् before a vowel becomes द्, as यथावत् + अनभि- → यथावदनभि-."),
            [("जगतपि", "A final त् does not stay त् before a vowel."),
             ("जगन्नपि", "न्न comes from त् + न, not from त् + अ."),
             ("जगच्चपि", "च्च comes from त् + च, not from त् + अ.")],
            "जगत् + अपि = जगदपि, like यथावत् + अनभि- = यथावदनभि-.",
            "त् + vowel → द्.",
            teaches="A final त् before a vowel becomes द्: यथावत् + अनभिसन्धीयमान → यथावदनभिसन्धीयमान."),
    ],
}

# ---------------------------------------------------------------- unit 121
AUTHORED["121"] = {
    "title": "अन्ये तु वर्णयंति",
    "question": "By unit 121, what do the others (anye) do?",
    "rule": "But others describe (अन्ये तु वर्णयन्ति): a lead-in; what they describe is not printed in this line.",
    "limits": ("Prose, three words. GROUPING: a lead-in; the description appears to follow in card 122. The object "
               "of वर्णयन्ति is not stated and not supplied; no question asks what is described."),
    "explain_hi": ("यह तीन शब्दों की गद्य-पंक्ति एक नए मत की भूमिका है: परन्तु दूसरे लोग वर्णन करते हैं। "
                   "‘वर्णयन्ति’ √वर्ण् (दसवाँ गण) का वर्तमान काल, प्रथम पुरुष बहुवचन है। "
                   "क्या वर्णन करते हैं, यह इस पंक्ति में छपा नहीं; डेटा के अनुसार वर्णन अगली इकाई १२२ में आता प्रतीत होता है। "
                   "‘तु’ (परन्तु) पिछली बात से अलग मत की ओर ले जाता है।"),
    "hook": "‘अन्ये तु वर्णयन्ति’: दूसरों का वर्णन आगे।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 121, what do the others (anye) do?",
            ("They describe (varṇayanti)", "वर्णयन्ति = they describe."),
            [("They sing (gāyanti)", "The verb printed is वर्णयन्ति, not गायन्ति."),
             ("They reckon up (gaṇayanti)", "The verb printed is वर्णयन्ति, not गणयन्ति."),
             ("They ask (pṛcchanti)", "The verb printed is वर्णयन्ति, not पृच्छन्ति.")],
            "But others describe.",
            "अन्ये तु वर्णयंति."),
        match(1, "Match each word of unit 121 to its meaning.",
              [["अन्ये", "others"], ["तु", "but"], ["वर्णयन्ति", "they describe"]],
              "अन्ये = others; तु = but; वर्णयन्ति = they describe.",
              "अन्ये, तु, वर्णयन्ति."),
        fill(2, "Unit 121: अन्ये तु ____ (they describe). Type it in Devanagari or in English letters (e.g. dharma).",
             accepts("वर्णयन्ति", None, "वर्णयंति", "varnayanti"),
             "वर्णयन्ति (they describe), printed वर्णयंति.",
             "वर्णयन्ति is the 3rd person plural present of √वर्ण् (10th class, stem वर्णय-).",
             "अन्ये तु वर्णयन्ति."),
        mcq("discriminate", 3, "In unit 121, what form is वर्णयन्ति?",
            ("Present, 3rd plural: they describe", "The data labels it 3 pl. pres.: they describe."),
            [("Present, 3rd singular: he describes", "He describes would be वर्णयति."),
             ("Imperative, 3rd plural: let them describe", "Let them describe would be वर्णयन्तु."),
             ("Optative, 3rd plural: they should describe", "They should describe would be वर्णयेयुः.")],
            "वर्णयन्ति = present, third person plural: they describe.",
            "-अन्ति = present, 3rd plural."),
        multi("apply", 4, "Which statements fit unit 121?",
              [("The subject is अन्ये, 'others'", "Right: अन्ये, others."),
               ("The verb वर्णयन्ति is plural", "Right: -न्ति, third person plural."),
               ("The line states what is described", "No object is printed or supplied."),
               ("तु means 'but' here", "Right: तु = but.")],
              [0, 1, 3],
              "Others (plural) describe; but (तु); what they describe is not printed here.",
              "अन्ये तु वर्णयंति."),
        mcq("transfer", 5, "By the pattern of वर्णयन्ति, which form of √चुर् (चोरयति, he steals) means they steal, in a new example?",
            ("चोरयन्ति", "Stem चोरय- + -न्ति (3rd plural), as वर्णय- + -न्ति → वर्णयन्ति."),
            [("चोरयति", "चोरयति is singular: he steals."),
             ("चोरयन्तु", "चोरयन्तु is imperative: let them steal."),
             ("चोरयामि", "चोरयामि is first person: I steal.")],
            "चोरयन्ति = they steal, like वर्णयन्ति = they describe.",
            "10th-class stem in -अय + -न्ति = they (do).",
            teaches="10th-class verbs take the stem -अय-: वर्णय- → वर्णयन्ति, they describe."),
    ],
}

# ---------------------------------------------------------------- unit 122
AUTHORED["122"] = {
    "title": "अभ्यवहृतमात्रस्याहारस्य",
    "question": "By unit 122, by what path is swallowed food cooked, and where does its prasāda go?",
    "rule": ("Food just swallowed rushes through the throat-tube (कण्ठनाडी, probably the gullet), descends into the great "
             "hollow (महानिम्न, probably the abdominal cavity); whatever part the bodily fire (कायाग्नि) reaches is "
             "brought to cooking (पाकमुपनीयते); its rasa named prasāda spreads equally into all the dhātus (समं "
             "समस्तधातुषु), through the srotas."),
    "limits": ("Prose; confidence low, heavily damaged. Conjectures: अवलीढ (printed अब्लीढः), रसलेश, अभिनिर्वृत्ति, "
               "प्रविसृत, प्रथमतः, पर्यायेण; 'अकासन्नेषु' is unclear. The construction after प्रविस्सृतो is uncertain. "
               "No question rests on these words. GROUPING: appears to continue card 121."),
    "explain_hi": ("यह लम्बा, क्षतिग्रस्त गद्य-वाक्य बताता प्रतीत होता है कि ‘दूसरों’ के मत में आहार कैसे पचता है (इकाई १२१ से आगे, डेटा के अनुसार)। "
                   "निगलते ही आहार कण्ठनाड़ी (सम्भवतः अन्ननलिका) से तेज़ी से जाता है, महानिम्न (सम्भवतः उदर-गुहा) में उतरता है, और जो-जो अंश कायाग्नि तक पहुँचता है वह पाक को पहुँचाया जाता है। "
                   "उस-उस अंश का ‘प्रसाद’ नामक रस-अंश सभी धातुओं में समान रूप से, स्रोतसों के द्वारों से फैलता है; अधिक भाग पहले जाता है, फिर बारी-बारी से अन्य में भी। "
                   "अब्लीढः, रस्लेशो, अभिनिर्वत्ति, प्रविस्सृतो, प्रथमतं, पर्यायैण के पाठ अनुमानित हैं और ‘अकासन्नेषु’ अस्पष्ट है। "
                   "प्रश्न केवल निश्चित अंशों पर हैं।"),
    "hook": "निगला, कण्ठनाड़ी, महानिम्न, कायाग्नि से पाक, प्रसाद सब धातुओं में।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 122, through what does food rush as soon as it is swallowed?",
            ("The kaṇṭha-nāḍī (throat-tube)", "कण्ठनाडीप्लुतिः: the rush through the throat-tube (probably the gullet)."),
            [("The nāsā-mārga (nose-path)", "No nose is named in unit 122."),
             ("The tālu-mūla (root of palate)", "No palate is named in unit 122."),
             ("The hṛdaya (heart region)", "No heart is named in unit 122.")],
            "Swallowed food rushes through the throat-tube (kaṇṭha-nāḍī, probably the gullet).",
            "अभ्यवहृतमात्रस्याहारस्य कंठनाडीप्लुतिः."),
        order(1, "Put these printed parts of unit 122 in the line's order.",
              ["अभ्यवहृतमात्रस्याहारस्य", "कंठनाडीप्लुतिस्तस्य", "महानिम्न मवतीर्णस्य", "पाकमुपनीयते", "प्रसादाख्यो",
               "समं समस्तधातुषु"],
              "Of food just swallowed; the rush through the throat-tube; having descended into the great hollow; is brought to cooking; named prasāda; equally into all dhātus.",
              "swallowed → कण्ठनाडी → महानिम्न → पाक → प्रसाद → सब धातु."),
        match(2, "Match each word of unit 122 to its meaning.",
              [["अभ्यवहृत", "swallowed"], ["महानिम्न", "great hollow (probably the abdominal cavity)"],
               ["कायाग्नि", "bodily fire"], ["प्रसाद", "clear essence"], ["स्रोतस्", "channel"]],
              "अभ्यवहृत = swallowed; महानिम्न = great hollow; कायाग्नि = bodily fire; प्रसाद = clear essence; स्रोतस् = channel.",
              "अभ्यवहृत, महानिम्न, कायाग्नि, प्रसाद, स्रोतस्.", role="extend",
              teaches="कायाग्नि = काय (body) + अग्नि (fire), a tat-puruṣa: the fire of the body."),
        mcq("discriminate", 3, "Which split of पाकमुपनीयते in unit 122 is right?",
            ("पाकम् + उपनीयते", "म् joins the vowel उ: पाकम् + उपनीयते → पाकमुपनीयते."),
            [("पाक + मुपनीयते", "मुपनीयते is not a word; the म् belongs to पाकम्."),
             ("पाकः + उपनीयते", "अः before उ would give पाक उपनीयते, with no म्."),
             ("पाकम् + अपनीयते", "म् + अ would give पाकमपनीयते, not -मुप-.")],
            "पाकम् (to cooking) + उपनीयते (is brought).",
            "म् + vowel: the म् joins the vowel."),
        mcq("apply", 4, "By unit 122, where does the rasa named prasāda spread?",
            ("Equally into all the dhātus", "समं समस्तधातुषु: equally into all the dhātus."),
            [("Only into the bone (asthi)", "Unit 122 says all the dhātus (समस्तधातुषु), not one."),
             ("Only into the śukra (semen)", "Unit 122 says all the dhātus (समस्तधातुषु), not one."),
             ("Only into the blood (rakta)", "Unit 122 says all the dhātus (समस्तधातुषु), not one.")],
            "The prasāda spreads equally into all the dhātus.",
            "प्रसादाख्यो ... समं समस्तधातुषु."),
        mcq("transfer", 5, "By the rule of चान्वेति (च + अन्वेति), how is अत्र + अपि (here too) joined in a new example?",
            ("अत्रापि", "अ + अ → आ, as च + अन्वेति → चान्वेति."),
            [("अत्रपि", "Two अ do not merge into a short अ; they give आ."),
             ("अत्रेपि", "ए comes from अ + इ, not from अ + अ."),
             ("अत्रोपि", "ओ comes from अ + उ, not from अ + अ.")],
            "अत्र + अपि = अत्रापि, like च + अन्वेति = चान्वेति.",
            "अ + अ → आ.",
            teaches="Two short अ merge into आ: च + अन्वेति → चान्वेति."),
    ],
}

# ---------------------------------------------------------------- unit 123
AUTHORED["123"] = {
    "title": "साक्षात्सर्वधातून् पुष्णाति",
    "question": "By unit 123, how does the rasa nourish all the dhātus?",
    "rule": ("Thus the rasa itself (the data reads अन्नरस, food-rasa) nourishes (पुष्णाति) all the dhātus "
             "(सर्वधातून्) directly (साक्षात्), by just some difference of time (केनचिदेव कालभेदेन)."),
    "limits": ("Prose; confidence low. Printed 'अन्तरसएव'; अन्नरस (food-rasa) is a conjecture, so no question asks "
               "which rasa nourishes. The line does not say how long the difference of time is. It belongs to the "
               "'others' view (cards 121-124, appears)."),
    "explain_hi": ("यह गद्य-पंक्ति ‘दूसरों’ के मत का निष्कर्ष देती प्रतीत होती है: इस प्रकार रस ही सीधे (साक्षात्) सभी धातुओं का पोषण करता है। "
                   "भेद केवल किसी काल-भेद यानी समय के अन्तर का है (केनचिदेव कालभेदेन)। "
                   "छपा ‘अन्तरस’ है; डेटा इसे ‘अन्नरस’ (अन्न का रस) का अनुमानित पाठ मानता है, इसलिए इस शब्द पर कोई प्रश्न नहीं। "
                   "समय का अन्तर कितना है, यह नहीं बताया गया। "
                   "‘केनचिदेव’ में केनचित् का त् स्वर से पहले द् बना है।"),
    "hook": "रस सीधे सब धातुओं को पोसे, बस समय का अन्तर।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 123, what is nourished directly (sākṣāt)?",
            ("All the dhātus", "साक्षात्सर्वधातून् पुष्णाति: it directly nourishes all the dhātus."),
            [("Only the doṣas", "सर्वधातून्: all the dhātus, not the doṣas."),
             ("Only the srotas", "सर्वधातून्: all the dhātus, not the srotas."),
             ("Only the malas", "सर्वधातून्: all the dhātus, not the wastes.")],
            "All the dhātus are nourished directly.",
            "साक्षात्सर्वधातून् ... पुष्णाति."),
        order(1, "Put the printed words of unit 123 in the line's order.",
              ["एवमन्तरसएव", "साक्षात्सर्वधातून्", "केनचिदेव कालभेदेन", "पुष्णाति"],
              "Thus the rasa itself; directly all the dhātus; by just some difference of time; nourishes.",
              "एवमन्तरसएव → साक्षात्सर्वधातून् → केनचिदेव कालभेदेन → पुष्णाति."),
        match(2, "Match each word of unit 123 to its meaning.",
              [["साक्षात्", "directly"], ["सर्व", "all"], ["काल", "time"], ["भेद", "difference"],
               ["पुष्णाति", "nourishes"]],
              "साक्षात् = directly; सर्व = all; काल-भेद = difference of time; पुष्णाति = nourishes.",
              "साक्षात्, सर्व, काल, भेद, पुष्णाति.", role="extend",
              teaches="पुष्णाति is the 3rd singular present of √पुष् (9th class, -णा-): nourishes."),
        mcq("discriminate", 3, "Which split of केनचिदेव in unit 123 is right?",
            ("केनचित् + एव", "त् before a vowel becomes द्: केनचित् + एव → केनचिदेव."),
            [("केनचित् + इव", "त् + इ would give केनचिदिव, not -देव."),
             ("केनचिद + एव", "अ + ए would give केनचिदैव, with ऐ."),
             ("केनचिः + एव", "There is no form केनचिः; the द् comes from त्.")],
            "केनचित् (by some) + एव (just).",
            "त् + vowel → द्."),
        mcq("apply", 4, "By unit 123, with what difference does the nourishing of all dhātus happen?",
            ("Some difference of time", "केनचिदेव कालभेदेन: by just some difference of time."),
            [("Some difference of place", "देश (place) is not named; the line has काल, time."),
             ("Some difference of taste", "रस-भेद is not named; the line has काल, time."),
             ("Some difference of season", "ऋतु is not named; the line has काल, time.")],
            "By just some difference of time (kāla-bheda).",
            "केनचिदेव कालभेदेन पुष्णाति."),
        mcq("transfer", 5, "By the pattern of कालभेदेन (by difference of time), what does देशभेदेन mean in a new example?",
            ("By difference of place", "-एन is the instrumental: by, through, as कालभेदेन = by difference of time."),
            [("Of difference of place", "Of would be the genitive, देशभेदस्य."),
             ("From difference of place", "From would be the ablative, देशभेदात्."),
             ("In difference of place", "In would be the locative, देशभेदे.")],
            "देशभेदेन = by difference of place, like कालभेदेन = by difference of time.",
            "a-stem + -एन = instrumental singular: by.",
            teaches="-एन marks the instrumental singular of a-stems: कालभेदेन, by difference of time."),
    ],
}

# ---------------------------------------------------------------- unit 124
AUTHORED["124"] = {
    "title": "न पुनर्धातवो धात्वंतरतां",
    "question": "By unit 124, what do the dhātus not do?",
    "rule": ("But the dhātus do not pass (न पुनः ... प्रतिपद्यन्ते) into the state of another dhātu (धात्वन्तरताम्) "
             "through the crushing of their own form (स्वरूपोपमर्देन)."),
    "limits": ("Prose. 'इति' closes the statement; by the data it appears to end the view of 'others' (cards "
               "121-124). The line does not say who holds the opposite view. 'Crushing' (upamarda) is the data's gloss "
               "(also destruction)."),
    "explain_hi": ("यह गद्य-पंक्ति ‘दूसरों’ के मत का अन्तिम कथन प्रतीत होती है: धातु अपने स्वरूप के उपमर्द यानी कुचले या नष्ट होने से दूसरी धातु की अवस्था को प्राप्त नहीं होते। "
                   "अर्थात् इस मत में एक धातु बदलकर दूसरी धातु नहीं बनती; इकाई १२३ के अनुसार रस ही सीधे सबका पोषण करता है। "
                   "‘इति’ कथन का अन्त बताता है; डेटा के अनुसार यह इस मत का अन्त प्रतीत होता है। "
                   "‘धातवो’ में अः का विसर्ग घोष व्यंजन ध से पहले ओ बना है।"),
    "hook": "इस मत में धातु अपना रूप मिटाकर दूसरी धातु नहीं बनते।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 124, into what do the dhātus not pass by crushing their own form?",
            ("The state of another dhātu", "धात्वन्तरतां न प्रतिपद्यन्ते: they do not pass into another dhātu's state."),
            [("The state of the doṣas", "No doṣa is named in unit 124."),
             ("The state of the srotas (channels)", "No srotas is named in unit 124."),
             ("The state of the food", "No food is named in unit 124.")],
            "The dhātus do not pass into the state of another dhātu.",
            "न पुनर्धातवो धात्वंतरतां ... प्रतिपद्यंतइति."),
        order(1, "Put the printed words of unit 124 in the line's order.",
              ["न पुनर्धातवो", "धात्वंतरतां", "स्वरूपोपमर्देन", "प्रतिपद्यंतइति"],
              "Not, however, the dhātus; into another-dhātu-state; by crushing of own form; pass, thus.",
              "न पुनर्धातवो → धात्वंतरतां → स्वरूपोपमर्देन → प्रतिपद्यंतइति."),
        match(2, "Match each word of unit 124 to its meaning.",
              [["धात्वन्तरता", "state of another dhātu"], ["स्वरूप", "own form"], ["उपमर्द", "crushing"],
               ["प्रतिपद्यन्ते", "they pass into"], ["पुनर्", "however"]],
              "धात्वन्तरता = another-dhātu-ness; स्वरूप-उपमर्द = crushing of own form; प्रतिपद्यन्ते = pass into.",
              "धात्वन्तरता, स्वरूप, उपमर्द, प्रतिपद्यन्ते, पुनर्.", role="extend",
              teaches="-ता makes an abstract noun: धातु + अन्तर + ता = the state of being another dhātu."),
        mcq("discriminate", 3, "Which split of स्वरूपोपमर्देन in unit 124 is right?",
            ("स्वरूप + उपमर्देन", "अ + उ → ओ: स्वरूप + उपमर्देन → स्वरूपोपमर्देन."),
            [("स्वरूपः + उपमर्देन", "अः before उ would give स्वरूप उपमर्देन, unjoined."),
             ("स्वरूपो + पमर्देन", "पमर्देन is not a word; the ओ comes from अ + उ."),
             ("स्वरूपम् + उपमर्देन", "म् + उ would give स्वरूपमुपमर्देन.")],
            "स्वरूप (own form) + उपमर्देन (by crushing).",
            "अ + उ → ओ."),
        mcq("apply", 4, "Why is धातवः printed धातवो before धात्वंतरतां in unit 124?",
            ("अः before a voiced consonant becomes ओ", "ध is a voiced consonant: धातवः + धात्व- → धातवो धात्व-."),
            [("अः before every consonant becomes ओ", "Not every consonant: before त the visarga becomes स्."),
             ("ओ is the case ending of धातु", "The ending is -अः (nom. pl. धातवः); ओ comes from sandhi."),
             ("ध begins with a vowel, so अः → ओ", "ध is a consonant, not a vowel.")],
            "धातवः + धात्वन्तरताम्: अः before the voiced consonant ध → ओ.",
            "अः + voiced consonant → ओ."),
        mcq("transfer", 5, "By the rule of स्वरूपोपमर्देन (स्वरूप + उपमर्देन), how is सूर्य + उदयः (sunrise) joined in a new example?",
            ("सूर्योदयः", "अ + उ → ओ, as स्वरूप + उपमर्देन → स्वरूपोपमर्देन."),
            [("सूर्यूदयः", "ऊ comes from उ + उ, not from अ + उ."),
             ("सूर्यौदयः", "औ comes from अ + ओ or औ, not from अ + उ."),
             ("सूर्यवुदयः", "व् comes from उ before a vowel, not from अ + उ.")],
            "सूर्य + उदयः = सूर्योदयः, like स्वरूप + उपमर्देन.",
            "अ + उ → ओ.",
            teaches="अ before उ gives ओ (guṇa): स्वरूप + उपमर्देन → स्वरूपोपमर्देन."),
    ],
}

# ---------------------------------------------------------------- unit 125
AUTHORED["125"] = {
    "title": "अग्निस्तु बलभेदेन",
    "question": "By unit 125, into how many kinds is agni (digestive fire) divided, by what, and which are they?",
    "rule": ("Agni (digestive fire), however, is of four kinds (चतुर्विधो भवति) by difference of strength (बलभेदेन): "
             "sama (even), viṣama (uneven), tīkṣṇa (sharp) and manda (slow)."),
    "limits": ("Prose. Only the four names are given here; their signs follow in cards 126-129. The line does not "
               "say which kind is best or how each arises."),
    "explain_hi": ("यह गद्य-पंक्ति अग्नि यानी पाचन-अग्नि के चार प्रकार बताती है, जिनका आधार बल का भेद है। "
                   "वे हैं: सम (समान), विषम (असमान), तीक्ष्ण (तेज़) और मन्द (धीमी)। "
                   "इनके लक्षण आगे की इकाइयाँ १२६ से १२९ बताती हैं। "
                   "‘अग्निस्तु’ और ‘विषमस्तीक्ष्णो’ में विसर्ग त से पहले स् बना है; ‘समो’ और ‘तीक्ष्णो’ में अः घोष व्यंजन से पहले ओ बना है।"),
    "hook": "बल-भेद से चार अग्नि: सम, विषम, तीक्ष्ण, मन्द।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 125, by what difference is agni of four kinds?",
            ("By difference of strength (bala)", "बलभेदेन चतुर्विधो भवति: fourfold by difference of strength."),
            [("By difference of the season (ṛtu)", "No season is named in unit 125."),
             ("By difference of place (deśa)", "No place is named in unit 125."),
             ("By difference of age (vayas)", "No age is named in unit 125.")],
            "Agni is fourfold by difference of strength.",
            "अग्निस्तु बलभेदेनचतुर्विधो भवति."),
        order(1, "Put the four kinds of agni in the order printed in unit 125.",
              ["सम", "विषम", "तीक्ष्ण", "मन्द"],
              "समो विषमस्तीक्ष्णो मन्दश्च: sama, viṣama, tīkṣṇa, manda.",
              "सम → विषम → तीक्ष्ण → मन्द."),
        match(2, "Match each kind of agni in unit 125 to its meaning.",
              [["सम", "even"], ["विषम", "uneven"], ["तीक्ष्ण", "sharp"], ["मन्द", "slow"]],
              "सम = even; विषम = uneven; तीक्ष्ण = sharp; मन्द = slow.",
              "सम, विषम, तीक्ष्ण, मन्द.", role="extend",
              teaches="विषम = वि + सम with स → ष after इ: 'uneven', the opposite of सम."),
        mcq("discriminate", 3, "Why is विषमः printed विषमस् before तीक्ष्णो in unit 125?",
            ("Visarga before त becomes स्", "विषमः + तीक्ष्णः → विषमस्तीक्ष्णः, as in अग्निः + तु → अग्निस्तु."),
            [("Visarga before every consonant becomes स्", "Not every consonant: before a voiced one अः gives ओ (समो विषमः)."),
             ("स् is part of the stem of विषम", "The stem is विषम; the स् comes from the visarga."),
             ("Visarga before a voiced sound becomes स्", "त is not voiced; before a voiced consonant अः gives ओ.")],
            "Visarga + त → स्त: विषमस्तीक्ष्णो, अग्निस्तु.",
            "Visarga before त → स्."),
        multi("apply", 4, "Which are among the four kinds of agni named in unit 125?",
              [("Sthira (steady)", "Sthira is not one of the four printed kinds."),
               ("Sama (even)", "Right: समो."),
               ("Tīkṣṇa (sharp)", "Right: तीक्ष्णो."),
               ("Manda (slow)", "Right: मंदश्च.")],
              [1, 2, 3],
              "The four are sama, viṣama, tīkṣṇa and manda; sthira is not among them.",
              "समो विषमस्तीक्ष्णो मंदश्च."),
        mcq("transfer", 5, "By the rule of समो विषमः (समः + विषमः), how is रामः + गच्छति (Rāma goes) joined in a new example?",
            ("रामो गच्छति", "अः before a voiced consonant becomes ओ, as समः + विषमः → समो विषमः."),
            [("रामर्गच्छति", "र् comes after vowels other than अ/आ, not after अ."),
             ("रामा गच्छति", "आ is not produced from अः; the visarga drops only after आ."),
             ("रामस्गच्छति", "स् comes before त or थ, not before ग.")],
            "रामः + गच्छति = रामो गच्छति, like समः + विषमः = समो विषमः.",
            "अः + voiced consonant → ओ.",
            teaches="अः before a voiced consonant becomes ओ: समः + विषमः → समो विषमः."),
    ],
}

# ---------------------------------------------------------------- unit 126
AUTHORED["126"] = {
    "title": "तत्र समो यः",
    "question": "By unit 126, what does the sama (even) agni do?",
    "rule": ("Among these (तत्र), the sama (even) one is that which properly digests (सम्यक् पचति) food that has been "
             "taken properly (सम्यगेव उपयुक्तम् अन्नम्)."),
    "limits": ("Prose; the copula is understood and the subject agni is carried from card 125. The line says nothing "
               "of improperly taken food for the sama agni."),
    "explain_hi": ("यह गद्य-पंक्ति सम अग्नि का लक्षण देती है: सम वह है जो ठीक से ही खाए गए अन्न को ठीक से पचाती है। "
                   "‘तत्र’ यानी उन (इकाई १२५ के) चार प्रकारों में। "
                   "‘सम्यक्’ दो बार है: एक बार खाने की रीति के लिए, एक बार पचाने के लिए। "
                   "‘सम्यगेवोपयुक्तम्’ में क् स्वर से पहले ग् बना है और एव + उपयुक्तम् में अ + उ से ओ। "
                   "अनुचित रीति से खाए अन्न के बारे में यहाँ कुछ नहीं कहा गया।"),
    "hook": "सम अग्नि: ठीक खाया, ठीक पचाया।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 126, what does the sama (even) agni do?",
            ("Digests properly what is taken properly", "सम्यगेवोपयुक्तमन्नं सम्यक् पचति."),
            [("Digests quickly what is taken wrongly", "That is the tīkṣṇa (sharp) agni of unit 128, not sama."),
             ("Digests slowly what is taken properly", "Slow digestion is the manda agni (unit 129), not sama."),
             ("Fails to digest even what is taken properly", "That is said of the viṣama agni (unit 127), not sama.")],
            "The sama agni properly digests food properly taken.",
            "तत्र समो यः सम्यगेवोपयुक्तमन्नं सम्यक् पचति."),
        order(1, "Put the printed words of unit 126 in the line's order.",
              ["तत्र समो यः", "सम्यगेवोपयुक्तमन्नं", "सम्यक्", "पचति"],
              "Among these, the even one which; food taken properly alone; properly; digests.",
              "तत्र समो यः → सम्यगेवोपयुक्तमन्नं → सम्यक् → पचति."),
        match(2, "Match each word of unit 126 to its meaning.",
              [["तत्र", "among these"], ["सम्यक्", "properly"], ["उपयुक्त", "taken, eaten"], ["अन्न", "food"],
               ["पचति", "digests"]],
              "तत्र = among these; सम्यक् = properly; उपयुक्त = taken; अन्न = food; पचति = digests.",
              "तत्र, सम्यक्, उपयुक्त, अन्न, पचति.", role="extend",
              teaches="उपयुक्त is the past participle of उप-√युज्: 'used, taken', here of food eaten."),
        mcq("discriminate", 3, "Which split of सम्यगेवोपयुक्तम् in unit 126 is right?",
            ("सम्यक् + एव + उपयुक्तम्", "क् → ग् before ए; अ + उ → ओ: एव + उपयुक्तम् → एवोपयुक्तम्."),
            [("सम्यक् + इव + उपयुक्तम्", "क् + इ would give सम्यगिव-, not सम्यगेव-."),
             ("सम्यक् + एवम् + उपयुक्तम्", "एवम् + उ would give एवमुपयुक्तम्."),
             ("सम्यक् + एव + अपयुक्तम्", "अ + अ would give एवापयुक्तम्.")],
            "सम्यक् (properly) + एव (only) + उपयुक्तम् (taken).",
            "क् + vowel → ग्; अ + उ → ओ."),
        mcq("apply", 4, "Why is सम्यक् printed सम्यग् before एव in unit 126?",
            ("क् before a vowel becomes ग्", "A final क् becomes ग् before a vowel: सम्यक् + एव → सम्यगेव."),
            [("क् before a vowel becomes च्", "च् does not come from क् here."),
             ("क् before a vowel is dropped", "Nothing is dropped: the print shows ग्."),
             ("The word always ends in ग्", "The same line prints सम्यक् before पचति.")],
            "सम्यक् + एव → सम्यगेव: क् before a vowel → ग्.",
            "क् + vowel → ग्."),
        mcq("transfer", 5, "By the rule of सम्यगेव (सम्यक् + एव), how is वाक् + ईशः (lord of speech) joined in a new example?",
            ("वागीशः", "क् before a vowel becomes ग्, as सम्यक् + एव → सम्यगेव."),
            [("वाकीशः", "A final क् does not stay क् before a vowel."),
             ("वाचीशः", "च् does not come from a final क् before a vowel."),
             ("वाङीशः", "ङ् comes from क् before a nasal, not before a vowel.")],
            "वाक् + ईशः = वागीशः, like सम्यक् + एव = सम्यगेव.",
            "क् + vowel → ग्.",
            teaches="A final क् before a vowel becomes ग्: सम्यक् + एव → सम्यगेव."),
    ],
}

# ---------------------------------------------------------------- unit 127
AUTHORED["127"] = {
    "title": "विषमो ऽसम्यगप्युपयुक्तं",
    "question": "By unit 127, what does the viṣama (uneven) agni do?",
    "rule": ("The viṣama (uneven) one digests (पचति) even what is improperly taken (असम्यगप्युपयुक्तम्), and even "
             "when it is properly taken (सम्यगपि च) does not digest (न पचति)."),
    "limits": ("Prose. The object is not printed (the food, अन्नम्, of card 126 is understood). The line does not "
               "say when or why it digests or fails."),
    "explain_hi": ("यह गद्य-पंक्ति विषम अग्नि का लक्षण देती है: वह अनुचित रीति से खाए हुए को भी पचा लेती है, और ठीक से खाए हुए को भी नहीं पचाती। "
                   "इस प्रकार उसका व्यवहार एक-सा नहीं, यही ‘विषम’ है। "
                   "कर्म (अन्न) छपा नहीं; इकाई १२६ का अन्न समझा जाता है। "
                   "‘विषमो ऽसम्यक्’ में अः + अ से ओ बना और अ का लोप ऽ से दिखाया गया है। "
                   "कब पचाती है और कब नहीं, यह नहीं बताया गया।"),
    "hook": "विषम अग्नि: गलत खाया भी पचाए, सही खाया भी न पचाए।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 127, what does the viṣama agni do with food taken properly?",
            ("Even then, it does not digest it", "सम्यगपि च न पचति: even when properly taken, it does not digest."),
            [("It digests it quickly and well", "Quick digestion is said of the tīkṣṇa agni (unit 128)."),
             ("It digests it properly, always", "Proper digestion of proper food is the sama agni (unit 126)."),
             ("It digests it, after a long time", "Late digestion is the manda agni (unit 129), not viṣama.")],
            "The viṣama agni, even with food properly taken, does not digest.",
            "सम्यगपिच न पचति."),
        order(1, "Put the printed words of unit 127 in the line's order.",
              ["विषमो", "ऽसम्यगप्युपयुक्तं पचति", "सम्यगपिच", "न पचति"],
              "The uneven one; digests even what is improperly taken; and even properly; does not digest.",
              "विषमो → ऽसम्यगप्युपयुक्तं पचति → सम्यगपिच → न पचति."),
        match(2, "Match each word of unit 127 to its meaning.",
              [["विषम", "uneven"], ["असम्यक्", "improperly"], ["सम्यक्", "properly"], ["अपि", "even"],
               ["न", "not"]],
              "विषम = uneven; असम्यक् = improperly; सम्यक् = properly; अपि = even; न = not.",
              "विषम, असम्यक्, सम्यक्, अपि, न.", role="extend",
              teaches="The prefix अ- negates: सम्यक् (properly) → असम्यक् (improperly)."),
        mcq("discriminate", 3, "Which split of असम्यगप्युपयुक्तं in unit 127 is right?",
            ("असम्यक् + अपि + उपयुक्तम्", "क् → ग् before अ; इ + उ → यु: अपि + उपयुक्तम् → अप्युपयुक्तम्."),
            [("असम्यक् + अपि + अपयुक्तम्", "इ + अ would give अप्यपयुक्तम्, not -प्युप-."),
             ("असम्यक् + अप्य + उपयुक्तम्", "अप्य is not a word; अ + उ would also give -प्योप-."),
             ("असम्यक् + अपु + उपयुक्तम्", "अपु is not a word; उ + उ would give -पूप-.")],
            "असम्यक् (improperly) + अपि (even) + उपयुक्तम् (taken).",
            "क् + vowel → ग्; इ + a different vowel → य्."),
        mcq("apply", 4, "In विषमो ऽसम्यक् (विषमः + असम्यक्) of unit 127, what does the sandhi do?",
            ("अः + अ → ओ, and the अ is dropped", "विषमः + असम्यक् → विषमोऽसम्यक्."),
            [("अः + अ → अर्, and the अ stays", "र् does not come after अ; that is for other vowels."),
             ("अः + अ → अ, with a gap left between", "The gap (अः → अ) is before vowels other than अ."),
             ("अः + अ → आ, and the two merge", "अः + अ does not merge into आ.")],
            "अः before अ: ओ, and the following अ is dropped (ऽ).",
            "अः + अ → ओऽ."),
        mcq("transfer", 5, "By the rule of विषमो ऽसम्यक्, how is रामः + अपि (Rāma too) joined in a new example?",
            ("रामोऽपि", "अः + अ → ओऽ, as विषमः + असम्यक् → विषमोऽसम्यक्."),
            [("राम अपि", "The gap (अः → अ) is before vowels other than अ."),
             ("रामरपि", "र् does not come after अ; it comes after other vowels."),
             ("रामापि", "अः + अ does not merge into आ.")],
            "रामः + अपि = रामोऽपि, like विषमः + असम्यक् = विषमोऽसम्यक्.",
            "अः + अ → ओऽ.",
            teaches="अः before अ becomes ओ and the अ is dropped (ऽ): विषमः + असम्यक् → विषमोऽसम्यक्."),
    ],
}

# ---------------------------------------------------------------- unit 128
AUTHORED["128"] = {
    "title": "तीक्ष्णो ऽसम्यगप्युपयुक्तमाशु",
    "question": "By unit 128, what does the tīkṣṇa (sharp) agni do, and what does it become?",
    "rule": ("The tīkṣṇa (sharp) one digests quickly (आशु पचति) even what is improperly taken; that very one, "
             "increasing (स एव वर्धमानः), becomes atyagni (excessive fire, अत्यग्निर्भवति)."),
    "limits": ("Prose. Atyagni is kept as a term with the plain gloss 'excessive fire'; the text does not describe it "
               "further here. The line does not say what makes the tīkṣṇa agni increase."),
    "explain_hi": ("यह गद्य-पंक्ति तीक्ष्ण अग्नि का लक्षण देती है: वह अनुचित रीति से खाए हुए को भी शीघ्र (आशु) पचा देती है। "
                   "वही बढ़ती हुई (वर्धमान) अत्यग्नि यानी अत्यधिक अग्नि हो जाती है। "
                   "अत्यग्नि का आगे वर्णन यहाँ नहीं है, और बढ़ने का कारण भी नहीं बताया गया। "
                   "‘अत्यग्नि’ = अति + अग्नि (इ + अ → य); ‘अत्यग्निर्भवति’ में इ के बाद का विसर्ग घोष भ से पहले र् बना है।"),
    "hook": "तीक्ष्ण अग्नि: गलत खाया भी झट पचाए; बढ़े तो अत्यग्नि।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 128, what does the tīkṣṇa agni become when it increases?",
            ("Atyagni (excessive fire)", "स एव वर्धमानोऽत्यग्निर्भवति: increasing, it becomes atyagni."),
            [("Manda (the slow kind of fire)", "Manda is a separate kind (unit 125), not what tīkṣṇa becomes."),
             ("Sama (the even fire)", "Sama is a separate kind (unit 125), not what tīkṣṇa becomes."),
             ("Viṣama (uneven fire)", "Viṣama is a separate kind (unit 125), not what tīkṣṇa becomes.")],
            "That very one, increasing, becomes atyagni.",
            "स एव वर्धमानोऽत्यग्निर्भवति."),
        order(1, "Put the printed parts of unit 128 in the line's order.",
              ["तीक्ष्णो ऽसम्यगप्युपयुक्तम्", "आशु पचति", "स एव", "वर्धमानोऽत्यग्निर्भवति"],
              "The sharp one, even what is improperly taken; digests quickly; that very one; increasing becomes atyagni.",
              "तीक्ष्णो ... → आशु पचति → स एव → वर्धमानोऽत्यग्निर्भवति."),
        match(2, "Match each word of unit 128 to its meaning.",
              [["तीक्ष्ण", "sharp"], ["आशु", "quickly"], ["वर्धमान", "increasing"], ["अत्यग्नि", "excessive fire"],
               ["भवति", "becomes"]],
              "तीक्ष्ण = sharp; आशु = quickly; वर्धमान = increasing; अत्यग्नि = excessive fire; भवति = becomes.",
              "तीक्ष्ण, आशु, वर्धमान, अत्यग्नि, भवति.", role="extend",
              teaches="वर्धमान is a present participle (√वृध्, -मान): 'increasing', still going on."),
        mcq("discriminate", 3, "Which split of अत्यग्निर्भवति in unit 128 is right?",
            ("अत्यग्निः + भवति", "इः before the voiced भ → इर्: अत्यग्निर्भवति."),
            [("अत्यग्नि + र्भवति", "र्भवति is not a word; the र् comes from the visarga."),
             ("अत्यग्निम् + भवति", "म् before भ would be written ं, not र्."),
             ("अत्यग्नेः + भवति", "एः before भ would give अत्यग्नेर्भवति.")],
            "अत्यग्निः (excessive fire) + भवति (becomes).",
            "इः + voiced sound → इर्."),
        mcq("apply", 4, "How is अति + अग्निः joined in अत्यग्निः of unit 128?",
            ("इ before अ becomes य्", "अति + अग्निः → अत्यग्निः: इ before a different vowel → य्."),
            [("इ and अ merge into ए", "ए comes from अ + इ, not from इ + अ."),
             ("इ and अ merge into ई", "ई comes from इ + इ, not from इ + अ."),
             ("The इ is dropped before अ", "The इ is not dropped; it becomes य्.")],
            "अति + अग्निः → अत्यग्निः: इ + अ → य.",
            "इ + a different vowel → य्."),
        mcq("transfer", 5, "By the rule of अत्यग्नि (अति + अग्नि), how is प्रति + अक्षम् joined in a new example?",
            ("प्रत्यक्षम्", "इ before अ becomes य्, as अति + अग्नि → अत्यग्नि."),
            [("प्रतेक्षम्", "ए comes from अ + इ, not from इ + अ."),
             ("प्रताक्षम्", "The इ does not drop and lengthen the अ."),
             ("प्रतिक्षम्", "The अ is not simply lost after इ.")],
            "प्रति + अक्षम् = प्रत्यक्षम्, like अति + अग्नि = अत्यग्नि.",
            "इ + अ → य.",
            teaches="इ before a different vowel becomes य्: अति + अग्नि → अत्यग्नि."),
    ],
}


# ================================================================= NOTES_HI
NOTES_HI = {
    "116": ("गद्य; विश्वास मध्यम; कोई पाठ-चिह्न नहीं। ‘आमनन्ति’ के दो कर्म: शुक्र का सार और गर्भ (‘X को Y मानते हैं’); डेटा का "
            "दूसरा पाठ (‘शुक्र के सार, गर्भ को ही कहते हैं’) भी वही अर्थ देता है। गर्भ = भ्रूण (मानक)। सन्धि जाँची: गर्भम् + एव → "
            "गर्भमेव (स्वर से पहले म्); एव + आमनन्ति → एवामनन्ति (अ + आ → आ); छपा ‘सारं’ (म् → ं), ‘आमनंति’ (ं = न्)।"),
    "117": ("गद्य; विश्वास निम्न। पाठ-चिह्न (सम्भावित): छपा ‘पंचातमा’ अस्पष्ट; ‘पञ्चात्मा’ (पाँच स्वरूप वाली) अनुमानित पाठ है; "
            "पाँच रूप यहाँ नहीं गिनाए गए। ‘मूर्च्छना’ का अर्थ अनिश्चित (मूर्छा / गाढ़ापन / प्रबलता)। ‘ईषच्छब्दप्रचुरोऽल्पो वा’ का अर्थ "
            "दो प्रकार से सम्भव; इन पर कोई प्रश्न नहीं। छपा ‘अमूर्त्तः’ = अमूर्तः (वर्तनी)। सन्धि जाँची: पुनर् + अग्नेः → पुनरग्नेः; "
            "अग्नेः + आहारस्य → अग्नेराहारस्य (ए के बाद विसर्ग + स्वर → र्); बहु + अल्प → बह्वल्प (उ + भिन्न स्वर → व्); तस्मात् + "
            "मूर्च्छना → तस्मान्मूर्च्छना (त् + म → न्म); विशेषात् + अमूर्तः → विशेषादमूर्तः (त् + स्वर → द्); शब्दप्रचुरः + अल्पः → "
            "शब्दप्रचुरोऽल्पः (अः + अ → ओऽ)।"),
    "118": ("गद्य; विश्वास मध्यम; कोई पाठ-चिह्न नहीं। ‘एवं च कृत्वा’ शाब्दिक (‘और ऐसा करके’); मुहावरा सम्भवतः ‘ऐसा होने से’। "
            "क्रिया समझी जाती है। सन्धि जाँची: देहे + अन्नमयाः → देहेऽन्नमयाः (ए + अ → एऽ); अन्नमयाः + एव → अन्नमया एव (आ के बाद "
            "विसर्ग घोष ध्वनि से पहले लुप्त); एवम् + च → एवं च।"),
    "119": ("गद्य; विश्वास निम्न। ‘न्यासमन्तर्बहिः’ का अन्वय स्पष्ट नहीं (‘धरोहर की तरह भीतर-बाहर’ या ‘भीतर-बाहर रखा’); "
            "‘यावत्कर्मोपादानम्’ = ‘जब तक कर्म का ग्रहण’ या ‘जहाँ तक कर्म ले जाए’; इन पर कोई प्रश्न नहीं। ‘तेन’ = उससे (डेटा: "
            "पिछली इकाइयों का अन्न)। ‘याप्यते’ डेटा में णिजन्त कर्मवाच्य। छपाई में कई शब्द बिना अन्तर के जुड़े (केवल छपाई)। "
            "सन्धि जाँची: तेन + एव → तेनैव (अ + ए → ऐ); च + इदम् → चेदम् (अ + इ → ए); इदम् + एवम् → इदमेवम्; शरीरयन्त्रम् + अनवरत → "
            "शरीरयन्त्रमनवरत; कर्म + उपादानम् → कर्मोपादानम् (अ + उ → ओ)।"),
    "120": ("गद्य; विश्वास निम्न; कोई पाठ-चिह्न नहीं। कर्ता छपा नहीं (इकाई ११९ का शरीर-यन्त्र समझा जाता है)। ‘बद्धस्रोतसा’ "
            "तृतीया एकवचन; ‘स्रोतसाम्’ (षष्ठी बहुवचन) भी पढ़ा जा सकता है; इस पर कोई प्रश्न नहीं। ‘वा ... वा’ = या तो ... या। उत्क्षेप "
            "= ऊपर फेंकना। सन्धि जाँची: तु + अन्न → त्वन्न (उ + अ → व); यथावत् + अनभि → यथावदनभि (त् + स्वर → द्); -प्रवाहम् + "
            "अन्तरा → -प्रवाहमन्तरा।"),
    "121": ("गद्य; विश्वास उच्च; कोई पाठ-चिह्न नहीं। समूह-टिप्पणी: भूमिका-वाक्य; वर्णन इकाई १२२ में आगे आता प्रतीत होता है। "
            "‘वर्णयन्ति’ का कर्म छपा नहीं और जोड़ा नहीं गया। छपा ‘वर्णयंति’ (ं = न्)। कोई सन्धि-परिवर्तन नहीं।"),
    "122": ("गद्य; विश्वास निम्न; बहुत क्षतिग्रस्त। अनुमानित पाठ: ‘अब्लीढः’ → अवलीढः (सम्भावित; आलीढः भी), ‘रस्लेशो’ → रसलेशः, "
            "‘अभिनिर्वत्ति’ → अभिनिर्वृत्ति, ‘प्रविस्सृतो’ → प्रविसृतः, ‘प्रथमतं’ → प्रथमतः, ‘पर्यायैण’ → पर्यायेण। ‘अकासन्नेषु’ अस्पष्ट "
            "(सम्भवतः ‘आसन्नेषु’)। छपा ‘महानिम्न मवतीर्णस्य’ = महानिम्नम् अवतीर्णस्य (अन्तर की भूल)। ‘प्रविस्सृतो’ के बाद का अन्वय "
            "अनिश्चित। कण्ठनाडी = सम्भवतः अन्ननलिका; महानिम्न = सम्भवतः उदर-गुहा। समूह-टिप्पणी: इकाई १२१ के ‘अन्ये तु वर्णयन्ति’ "
            "का आगे का भाग प्रतीत होती है। सन्धि जाँची: -मात्रस्य + आहारस्य → -मात्रस्याहारस्य; -प्लुतिः + तस्य → -प्लुतिस्तस्य "
            "(त से पहले विसर्ग → स्); यः + यः → यो यः (अः + घोष → ओ); पाकम् + उपनीयते → पाकमुपनीयते; तस्य + एव → तस्यैव; च + "
            "अन्वेति → चान्वेति (अ + अ → आ)।"),
    "123": ("गद्य; विश्वास निम्न। पाठ-चिह्न (सम्भावित): छपा ‘अन्तरस’; ‘अन्नरस’ (त/न का भ्रम, इकाई १०८ के आहार-रस से मेल) "
            "अनुमानित पाठ; इस शब्द पर कोई प्रश्न नहीं। ‘रस एव’ नियमित (अः + ए → अ ए)। सन्धि जाँची: एवम् + अन्तरस → एवमन्तरस (स्वर से पहले म्); "
            "केनचित् + एव → केनचिदेव (त् + स्वर → द्); साक्षात् + सर्व → साक्षात्सर्व (परिवर्तन नहीं)।"),
    "124": ("गद्य; विश्वास उच्च; कोई पाठ-चिह्न नहीं। ‘इति’ कथन का अन्त; डेटा के अनुसार ‘दूसरों’ के मत (इकाई १२१-१२४) का "
            "अन्त प्रतीत होता है; ‘इति’ का अनुवाद नहीं किया गया, यह केवल अन्त-चिह्न है। सन्धि जाँची: धातवः + धात्व- → धातवो (अः + घोष व्यंजन → "
            "ओ); धातु + अन्तर → धात्वन्तर (उ + अ → व); स्वरूप + उपमर्द → स्वरूपोपमर्द (अ + उ → ओ); प्रतिपद्यन्ते + इति → "
            "प्रतिपद्यन्त इति (ए + इ → अ इ), छपा ‘प्रतिपद्यंतइति’।"),
    "125": ("गद्य; विश्वास उच्च; कोई पाठ-चिह्न नहीं। अग्नि = पाचन-अग्नि (इस प्रसंग में)। छपा ‘बलभेदेनचतुर्विधो’ में शब्द बिना "
            "अन्तर के जुड़े (केवल छपाई)। सन्धि जाँची: अग्निः + तु → अग्निस्तु (त से पहले विसर्ग → स्); चतुर्विधः + भवति → "
            "चतुर्विधो भवति (अः + घोष व्यंजन → ओ); समः + विषमः → समो विषमः; विषमः + तीक्ष्णः → विषमस्तीक्ष्णः; तीक्ष्णः + मन्दः → "
            "तीक्ष्णो मन्दः; मन्दः + च → मन्दश्च (च से पहले विसर्ग → श्)।"),
    "126": ("गद्य; विश्वास उच्च; कोई पाठ-चिह्न नहीं। क्रिया समझी जाती है; कर्ता (अग्नि) इकाई १२५ से। सन्धि जाँची: समः + यः → "
            "समो यः (अः + घोष → ओ); सम्यक् + एव → सम्यगेव (क् + स्वर → ग्); एव + उपयुक्तम् → एवोपयुक्तम् (अ + उ → ओ); उपयुक्तम् + "
            "अन्नम् → उपयुक्तमन्नम्; छपा ‘अन्नं’।"),
    "127": ("गद्य; विश्वास उच्च। छपा ‘सम्यगपिच’ में अपि और च बिना अन्तर के (केवल छपाई)। कर्म (अन्न) छपा नहीं; इकाई १२६ का अन्न "
            "समझा जाता है। सन्धि जाँची: विषमः + असम्यक् → विषमोऽसम्यक् (अः + अ → ओऽ; छपाई में ‘विषमो ऽसम्यक्’ अन्तर सहित); "
            "असम्यक् + अपि → असम्यगपि (क् + स्वर → ग्); अपि + उपयुक्तम् → अप्युपयुक्तम् (इ + भिन्न स्वर → य्)।"),
    "128": ("गद्य; विश्वास उच्च; कोई पाठ-चिह्न नहीं। अत्यग्नि = अत्यधिक अग्नि; यहाँ आगे वर्णन नहीं। सन्धि जाँची: तीक्ष्णः + असम्यक् "
            "→ तीक्ष्णोऽसम्यक् (अः + अ → ओऽ); उपयुक्तम् + आशु → उपयुक्तमाशु; सः + एव → स एव (सः का विसर्ग लुप्त); वर्धमानः + "
            "अत्यग्निः → वर्धमानोऽत्यग्निः; अति + अग्निः → अत्यग्निः (इ + अ → य); अत्यग्निः + भवति → अत्यग्निर्भवति (इ के बाद विसर्ग "
            "+ घोष → र्)।"),
}


# ===================================================================== AIDS
AIDS = {
    "116": {
        "frame": "किनका मत: अपरे (दूसरे) → किसका: शुक्रस्य सारम् (शुक्र का सार) → क्या माना: गर्भम् एव (गर्भ ही) → क्रिया: आमनन्ति।",
        "chunks": "अपरे पुनः | शुक्रस्य सारं | गर्भमेवामनंति",
        "sandhi": "अ + आ → आ: एव + आमनन्ति → एवामनन्ति · स्वर से पहले म्: गर्भम् + एव → गर्भमेव।",
    },
    "117": {
        "seesaw": "बहु (अधिक) ⇄ अल्प (कम): दोनों इसी पंक्ति के ‘बह्वल्पतया’ में; अग्नि और आहार की कमी-बेशी।",
        "chunks": "वायुः पुनरग्नेराहारस्य च | बह्वल्पतया | तस्मात्तस्मान्मूर्च्छनाविशेषादमूर्त्तः | शब्दवानीषच्छब्दप्रचुरोऽल्पो वा | पंचातमा | कोष्ठे प्रादुर्भवति",
        "sandhi": ("ए के बाद विसर्ग + स्वर → र्: अग्नेः + आहारस्य → अग्नेराहारस्य · उ + भिन्न स्वर → व्: बहु + अल्प → बह्वल्प · "
                   "त् + स्वर → द्: विशेषात् + अमूर्तः → विशेषादमूर्तः।"),
        "frame": "कौन: वायुः → किससे: अग्नि और आहार की बह्वल्पता → कैसी: अमूर्त, शब्दवान् → कहाँ: कोष्ठे प्रादुर्भवति।",
    },
    "118": {
        "frame": "कहाँ: देहे (देह में) → कौन: सर्वे भावाः (सभी भाव) → कैसे: अन्नमयाः एव (अन्न से ही बने)।",
        "chunks": "एवं च कृत्वा | देहेऽन्नमया | एव | सर्वे भावाः",
        "sandhi": "ए + अ → एऽ: देहे + अन्नमयाः → देहेऽन्नमयाः · आ के बाद विसर्ग स्वर से पहले लुप्त: अन्नमयाः + एव → अन्नमया एव।",
    },
    "119": {
        "chain": {"steps": ["तेनैव: उसी से (डेटा: पिछला अन्न)", "शरीरयन्त्र: शरीर रूपी यन्त्र", "चिरेण: देर तक",
                            "अनवरतप्रवाहेण: अटूट प्रवाह से", "स्वास्थ्य, बल, उपचय से युक्त", "याप्यते: चलाया जाता है"]},
        "seesaw": "अन्तर् (भीतर) ⇄ बहिः (बाहर): दोनों इसी पंक्ति के ‘न्यासमंतर्बहिः’ में; अन्वय अस्पष्ट।",
        "chunks": "तेनैव चेदमेवं चिरेण | न्यासमंतर्बहिः | शरीरयंत्रमनवरतप्रवाहेण | स्वास्थ्यबलोपचययुक्तं | यावत्कर्मोपादानं | याप्यते",
        "sandhi": "अ + ए → ऐ: तेन + एव → तेनैव · अ + इ → ए: च + इदम् → चेदम् · अ + उ → ओ: कर्म + उपादानम् → कर्मोपादानम्।",
    },
    "120": {
        "diagram": {"groups": [
            {"label": "अन्यथा तु (बद्ध स्रोतस् से)", "items": ["वा: व्यवच्छिद्यते (कट जाता है)",
                                                         "वा: व्याधिभाजनं भवति (रोग का पात्र बनता है)"]}]},
        "chunks": "अन्यथा त्वन्नरसोत्क्षेपादिबद्धस्रोतसा वा | यथावदनभिसंधीयमानधातुप्रवाहमंतरा | व्यवच्छिद्यते | व्याधिभाजनं वा भवति",
        "sandhi": "उ + अ → व: तु + अन्न → त्वन्न · त् + स्वर → द्: यथावत् + अनभि → यथावदनभि।",
    },
    "121": {
        "frame": "कौन: अन्ये (दूसरे) → परन्तु: तु → क्या करते हैं: वर्णयन्ति (वर्णन करते हैं) → क्या: छपा नहीं।",
        "chunks": "अन्ये | तु | वर्णयंति",
    },
    "122": {
        "chain": {"steps": ["अभ्यवहृत: आहार निगला गया", "कण्ठनाडी (सम्भवतः अन्ननलिका) से प्लुति",
                            "महानिम्न (सम्भवतः उदर-गुहा) में उतरा", "कायाग्नि से अंश पाक को पहुँचा",
                            "प्रसाद नामक रस-अंश", "समं समस्तधातुषु: सब धातुओं में"]},
        "seesaw": "संवृत (बन्द) ⇄ असंवृत (खुले): दोनों इसी पंक्ति के ‘संवृतासंवृतैः’ में।",
        "chunks": ("अभ्यवहृतमात्रस्याहारस्य | कंठनाडीप्लुतिस्तस्य | महानिम्न मवतीर्णस्य | यो य एवांशः | कायाग्निनाऽब्लीढः | "
                   "पाकमुपनीयते | तस्य तस्यैव प्रसादाख्यो | रस्लेशोऽभिनिर्वत्तिसमनंतरं | समं समस्तधातुषु"),
        "sandhi": "त से पहले विसर्ग → स्: प्लुतिः + तस्य → प्लुतिस्तस्य · अ + ए → ऐ: तस्य + एव → तस्यैव · अ + अ → आ: च + अन्वेति → चान्वेति।",
    },
    "123": {
        "frame": "कैसे: साक्षात् (सीधे) → किसे: सर्वधातून् (सब धातुओं को) → भेद: केनचिदेव कालभेदेन (बस समय का अन्तर) → क्रिया: पुष्णाति।",
        "chunks": "एवमन्तरसएव | साक्षात्सर्वधातून् | केनचिदेव कालभेदेन | पुष्णाति",
        "sandhi": "त् + स्वर → द्: केनचित् + एव → केनचिदेव · त् + स → परिवर्तन नहीं: साक्षात् + सर्व → साक्षात्सर्व।",
    },
    "124": {
        "frame": "कौन: धातवः → क्या नहीं: धात्वन्तरताम् (दूसरी धातु की अवस्था) → किससे: स्वरूपोपमर्देन → क्रिया: न प्रतिपद्यन्ते।",
        "chunks": "न पुनर्धातवो | धात्वंतरतां | स्वरूपोपमर्देन | प्रतिपद्यंतइति",
        "sandhi": ("अः + घोष व्यंजन → ओ: धातवः + धात्व- → धातवो · अ + उ → ओ: स्वरूप + उपमर्द → स्वरूपोपमर्द · "
                   "उ + अ → व: धातु + अन्तर → धात्वन्तर।"),
    },
    "125": {
        "diagram": {"groups": [
            {"label": "अग्नि: बलभेद से चतुर्विध (क्रम से)", "items": ["१ सम: समान", "२ विषम: असमान", "३ तीक्ष्ण: तेज़",
                                                               "४ मन्द: धीमी"]}]},
        "chunks": "अग्निस्तु | बलभेदेनचतुर्विधो भवति | समो | विषमस्तीक्ष्णो | मंदश्च",
        "sandhi": ("त से पहले विसर्ग → स्: अग्निः + तु → अग्निस्तु · अः + घोष व्यंजन → ओ: समः + विषमः → समो विषमः · "
                   "च से पहले विसर्ग → श्: मन्दः + च → मन्दश्च।"),
        "anchors": "क्रम याद रखें: ‘सम-विषम’ जोड़ा, फिर ‘तीक्ष्ण-मन्द’ जोड़ा। (मेरी याद-पद्धति)",
    },
    "126": {
        "frame": "कौन: समः (अग्नि) → किसे: सम्यगेव उपयुक्तम् अन्नम् (ठीक खाया अन्न) → कैसे: सम्यक् पचति (ठीक पचाती है)।",
        "chunks": "तत्र समो यः | सम्यगेवोपयुक्तमन्नं | सम्यक् | पचति",
        "sandhi": "क् + स्वर → ग्: सम्यक् + एव → सम्यगेव · अ + उ → ओ: एव + उपयुक्तम् → एवोपयुक्तम्।",
    },
    "127": {
        "seesaw": "असम्यक् (अनुचित) ⇄ सम्यक् (उचित): दोनों इसी पंक्ति में; अनुचित खाया भी पचे, उचित खाया भी न पचे।",
        "chunks": "विषमो | ऽसम्यगप्युपयुक्तं पचति | सम्यगपिच | न पचति",
        "sandhi": "अः + अ → ओऽ: विषमः + असम्यक् → विषमोऽसम्यक् · इ + भिन्न स्वर → य्: अपि + उपयुक्तम् → अप्युपयुक्तम्।",
    },
    "128": {
        "chain": {"steps": ["तीक्ष्ण अग्नि", "असम्यक् उपयुक्त को भी आशु पचति", "स एव वर्धमानः: वही बढ़ती हुई",
                            "अत्यग्निर्भवति: अत्यग्नि होती है"]},
        "chunks": "तीक्ष्णो | ऽसम्यगप्युपयुक्तमाशु पचति | स एव | वर्धमानोऽत्यग्निर्भवति",
        "sandhi": "इ + अ → य: अति + अग्निः → अत्यग्निः · इ के बाद विसर्ग + घोष → र्: अत्यग्निः + भवति → अत्यग्निर्भवति · सः + एव → स एव।",
    },
}


# ============================================================== IMAGE_SPECS
IMAGE_SPECS = {
    ("119", "chain"): {
        "file": "sh6-sharira-yantra-119.svg",
        "alt": ("Chain of unit 119 in line order: by that alone (the data reads: the food); the body-machine; for a long "
                "time; with an unbroken flow; endowed with health, strength and growth; is kept going."),
        "type": "chain",
        "title": "इकाई ११९: शरीर-यन्त्र",
        "steps": ["तेनैव: उसी से (डेटा: अन्न)", "शरीरयन्त्र", "चिरेण: देर तक", "अनवरतप्रवाहेण: अटूट प्रवाह",
                  "स्वास्थ्य, बल, उपचय से युक्त", "याप्यते: चलाया जाता है"],
    },
    ("120", "diagram"): {
        "file": "sh6-anyatha-120.svg",
        "alt": ("Flowchart of unit 120: otherwise, with the srotas bound, either it is cut off, or it becomes a vessel "
                "of disease."),
        "type": "mermaid",
        "code": ("flowchart TD\n"
                 "  A[\"अन्यथा: स्रोतस् बद्ध\"] --> B[\"वा: व्यवच्छिद्यते\"]\n"
                 "  A --> C[\"वा: व्याधिभाजनं भवति\"]\n"
                 "  B --> D[\"कट जाता है\"]\n"
                 "  C --> E[\"रोग का पात्र\"]\n"),
    },
    ("122", "chain"): {
        "file": "sh6-ahara-paka-122.svg",
        "alt": ("Chain of unit 122 in line order: food swallowed; rush through the throat-tube (probably the gullet); "
                "descent into the great hollow (probably the abdominal cavity); a part brought to cooking by the bodily "
                "fire; the rasa named prasāda; into all the dhātus equally."),
        "type": "chain",
        "title": "इकाई १२२: आहार का पाक (सम्भवतः दूसरों का मत)",
        "steps": ["अभ्यवहृत: आहार निगला", "कण्ठनाडी (सम्भवतः अन्ननलिका)", "महानिम्न (सम्भवतः उदर-गुहा)",
                  "कायाग्नि से पाक", "प्रसाद नामक रस-अंश", "समं समस्तधातुषु"],
    },
    ("125", "diagram"): {
        "file": "sh6-agni-chatur-125.svg",
        "alt": ("Table of unit 125, numbered in line order: the four kinds of agni by difference of strength: 1 sama "
                "(even), 2 viṣama (uneven), 3 tīkṣṇa (sharp), 4 manda (slow)."),
        "type": "table",
        "title": "इकाई १२५: बलभेद से चार अग्नि",
        "heads": ["छपा नाम", "अर्थ"],
        "rows": [["१ सम", "समान"], ["२ विषम", "असमान"], ["३ तीक्ष्ण", "तेज़"], ["४ मन्द", "धीमी"]],
    },
    ("127", "seesaw"): {
        "file": "sh6-vishama-127.svg",
        "alt": ("Two columns for unit 127, the viṣama agni: food improperly taken, it digests even that; food properly "
                "taken, even that it does not digest."),
        "type": "split",
        "title": "इकाई १२७: विषम अग्नि",
        "cols": [["असम्यक् उपयुक्त", ["अनुचित खाया हुआ", "उसे भी पचति"]],
                 ["सम्यक् उपयुक्त", ["ठीक खाया हुआ", "उसे भी न पचति"]]],
    },
    ("128", "chain"): {
        "file": "sh6-tikshna-128.svg",
        "alt": ("Chain of unit 128: the tīkṣṇa agni; digests quickly even what is improperly taken; that very one, "
                "increasing; becomes atyagni (excessive fire)."),
        "type": "chain",
        "title": "इकाई १२८: तीक्ष्ण से अत्यग्नि",
        "steps": ["तीक्ष्ण अग्नि", "असम्यक् खाया भी आशु पचति", "स एव वर्धमानः", "अत्यग्निर्भवति"],
    },
}
