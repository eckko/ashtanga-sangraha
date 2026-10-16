from helpers import mcq, match, order, fill, multi, accepts

AUTHORED = {}

# ---------------------------------------------------------------- unit 92
AUTHORED["92"] = {
    "title": "प्रसिद्धकेशवाग्वेषशमसांत्वपरायणः",
    "question": "What is the person told to be devoted to, and what must the lower garment not touch?",
    "rule": ("He is devoted (परायण) to well-kept hair, speech, dress, calm and "
             "conciliation, and he does not touch the body above the navel "
             "with the lower garment (अधरवासस्)."),
    "limits": ("प्रसिद्ध can mean 'adorned, well-arranged' or 'well-known, "
               "established'; the card uses the first and builds no question on "
               "the choice. The verse does not say why the lower garment is "
               "kept off the upper body."),
    "explain_hi": ("यह युग्म दिनचर्या के आचरण की सूची आगे बढ़ाता है। पहली पंक्ति में पाँच "
                   "चीज़ों के प्रति तत्पर रहने को कहा गया है: केश, वाणी, वेश, शम (शान्ति) और "
                   "सांत्व (मीठी, सान्त्वना भरी बात)। ‘परायण’ का अर्थ है उसी में लगा हुआ। दूसरी "
                   "पंक्ति में निषेध है: शरीर के नाभि से ऊपर के भाग को निचले वस्त्र से न छुए। "
                   "‘प्रसिद्ध’ के दो अर्थ संभव हैं, इसलिए उस पर प्रश्न नहीं बना।"),
    "hook": "केश-वाणी-वेश, शान्ति-सांत्व में तत्पर · नाभि से ऊपर निचला वस्त्र नहीं।",
    "core": False,
    "questions": [
        mcq("pretest", 0,
            "What does line 2 say the lower garment must not touch?",
            ("The body above the navel",
             "ऊर्ध्वं नाभेः शरीरस्य: the part of the body above the navel."),
            [("The body below the navel", "The line says ऊर्ध्वम्, above, not below."),
             ("The ground when one walks", "The ground is not mentioned in the line."),
             ("Another person's clothing", "No other person or clothing is named.")],
            "The line forbids touching the part of the body above the navel with the lower garment.",
            "ऊर्ध्वं नाभेः शरीरस्य + अधरवाससा + न स्पृशेत्."),
        match(1, "Match each thing line 1 names to its meaning.",
              [["केश", "hair"], ["वाक्", "speech"], ["वेष", "dress"],
               ["शम", "calm"], ["सांत्व", "conciliating words"]],
              "These five are the things the person is devoted to in line 1.",
              "केश = hair; वाक् = speech; वेष = dress; शम = calm; सांत्व = conciliation."),
        mcq("extend", 2, "Which is the right split of स्पृशेन्नाधरवाससा?",
            ("स्पृशेत् + न + अधरवाससा",
             "Final त् before न becomes न्; न + अ gives ना."),
            [("स्पृशेन् + न + अधरवाससा", "The first word is स्पृशेत्, whose त् changes before न; it is not स्पृशेन्."),
             ("स्पृशेत् + ना + धरवाससा", "धरवासस् is not the word; the word is अधरवासस्."),
             ("स्पृशे + न्ना + अधरवाससा", "न्ना is not a word.")],
            "स्पृशेत् (should touch) + न (not) + अधरवाससा (with the lower garment).",
            "त् + न → न्न; न + अ → ना.",
            teaches="A final त् before न joins as न्न (स्पृशेत् + न = स्पृशेन्न); न followed by अ gives ना."),
        multi("discriminate", 3, "Which does line 1 name as things he is devoted to? Choose all that apply.",
              [("hair (केश)", "Right: the first item."),
               ("speech (वाक्)", "Right: the second item."),
               ("calm (शम)", "Right: the fourth item."),
               ("food", "Food is not in the line."),
               ("sleep", "Sleep is not in the line.")],
              [0, 1, 2],
              "Line 1 names hair, speech, dress, calm and conciliation; food and sleep do not occur.",
              "परायण list: केश, वाक्, वेष, शम, सांत्व."),
        order(4, "Put the five things of line 1 in the order of the verse.",
              ["केश", "वाक्", "वेष", "शम", "सांत्व"],
              "The compound runs केश, वाक्, वेष, शम, सांत्व, then परायणः.",
              "केश · वाक् · वेष · शम · सांत्व.", role="apply"),
        mcq("transfer", 5,
            "An invented word says धर्मपरायणः, like शमसांत्वपरायणः. What does it mean?",
            ("Devoted to dharma",
             "X-परायण means devoted to X."),
            [("Hostile to dharma", "परायण means devoted, not hostile."),
             ("Born of dharma", "'Born of' would be -ज."),
             ("Free from dharma", "'Free from' would be -वर्जित.")],
            "X-परायणः = one who is devoted to X.",
            "X-परायण = devoted to X.",
            teaches="A compound ending in -परायण means 'devoted to' the first part (शमसांत्वपरायणः; धर्मपरायणः)."),
    ],
}

# ---------------------------------------------------------------- unit 93
AUTHORED["93"] = {
    "title": "न कुर्य्यान्मिथुनीभूय",
    "question": "What is one not to delay, and what is one not to do with the mouth uncovered?",
    "rule": ("After intercourse one should not delay cleansing (शौच); with the "
             "mouth uncovered (असंवृत) one should not laugh, sneeze, belch or yawn."),
    "limits": ("The verse gives no reason and no time for the cleansing, and no "
               "instruction beyond the prohibitions. The verb कुर्यात् is carried "
               "to line 2 from line 1."),
    "explain_hi": ("इस युग्म में दो निषेध हैं। पहली पंक्ति: मैथुन के बाद शौच (शुद्धि) में "
                   "विलम्ब न करे। दूसरी पंक्ति: मुँह खुला हो तो हँसना, छींकना, डकार लेना और "
                   "जम्हाई लेना न करे। ‘असंवृतमुखः’ का अर्थ है जिसका मुँह ढका नहीं है। श्लोक "
                   "कारण या समय नहीं बताता, केवल निषेध कहता है।"),
    "hook": "मैथुन के बाद शौच में देर नहीं · खुले मुँह हँसना-छींकना-डकार-जम्हाई नहीं।",
    "core": True,
    "questions": [
        mcq("pretest", 0,
            "What does line 1 say one should not delay after intercourse?",
            ("Cleansing (शौच)",
             "शौचंप्रति विलंबनं: delay regarding cleansing."),
            [("Sleeping", "Sleep is not named in the line."),
             ("Eating", "Eating is not named in the line."),
             ("Speaking", "Speech is not named in the line.")],
            "The line forbids delay regarding cleansing after intercourse.",
            "न कुर्यात् + विलम्बनम् + शौचं प्रति."),
        match(1, "Match each of the four acts in line 2 to its meaning.",
              [["हास्य", "laughing"], ["क्षव", "sneezing"],
               ["उद्गार", "belching"], ["विजृंभण", "yawning"]],
              "These four make the dvandva list that the uncovered mouth is attached to.",
              "हास्य = laughing; क्षव = sneezing; उद्गार = belching; विजृंभण = yawning."),
        mcq("extend", 2, "Which is the right split of नासंवृतमुखो हास्य-?",
            ("न + असंवृतमुखः + हास्य",
             "अ + अ gives आ; the visarga of -मुखः becomes ओ before a voiced sound."),
            [("न + असंवृतमुखो + आस्य", "आस्य is not a word here; हास्य begins with ह."),
             ("ना + संवृतमुखः + हास्य", "The word is असंवृत (uncovered), not संवृत."),
             ("न + असंवृतमुखा + हास्य", "-मुखा would not give -मुखो.")],
            "न (not) + असंवृतमुखः (with mouth uncovered) + हास्य (laughing…).",
            "न + अ → ना; -अः + voiced sound → -ओ.",
            teaches="After -अ a visarga becomes ओ before a voiced sound (असंवृतमुखः + हास्य = असंवृतमुखो हास्य)."),
        mcq("discriminate", 3, "Which translation of line 2 is right?",
            ("With the mouth uncovered one should not laugh, sneeze, belch or yawn.",
             "असंवृतमुख: uncovered mouth; the four acts are all prohibited."),
            [("With the mouth covered one should not laugh, sneeze, belch or yawn.", "असंवृत means not covered."),
             ("With the mouth uncovered one should laugh, sneeze, belch or yawn.", "The न forbids them."),
             ("With the mouth uncovered one should not laugh, sneeze, cough or yawn.", "The list has belching (उद्गार), not coughing.")],
            "The line prohibits laughing, sneezing, belching and yawning when the mouth is uncovered.",
            "असंवृतमुखः + न + हास्य-क्षव-उद्गार-विजृंभणम्."),
        order(4, "Put the four acts of line 2 in the order of the verse.",
              ["हास्य", "क्षव", "उद्गार", "विजृंभण"],
              "The list runs laughing, sneezing, belching, yawning.",
              "हास्य · क्षव · उद्गार · विजृंभण.", role="apply"),
        mcq("transfer", 5,
            "An invented word says शुचीभूय, built like मिथुनीभूय. What does it mean?",
            ("Having become clean",
             "X-ī-bhūya means having become X."),
            [("Having wished to be clean", "Nothing in -भूय means wishing."),
             ("Being about to become clean", "-भूय is a 'having done' form, not a future."),
             ("Having cleaned another", "भू here is 'become', not 'make' another clean.")],
            "मिथुनीभूय = having become a pair; शुचीभूय follows the same build: having become clean.",
            "X + ई + भूय = having become X.",
            teaches="X + ई + भूय is a 'having become X' form (मिथुनीभूय; शुचीभूय)."),
    ],
}

# ---------------------------------------------------------------- unit 94
AUTHORED["94"] = {
    "title": "पाणिद्वयेन युगपत्",
    "question": "Which three things does the unit say one should not do?",
    "rule": ("One should not scratch one's head with both hands at once, nor "
             "carry a load on the head, nor carry fire and water together."),
    "limits": ("Whether 'on the head' also applies to fire and water is not "
               "stated. अग्निवारिणी is read as a dual 'fire and water'. The verse "
               "gives no reason."),
    "explain_hi": ("इस युग्म में तीन निषेध हैं। पहला: अपने सिर को दोनों हाथों से एक साथ न "
                   "खुजलाए। दूसरा: सिर पर बोझ न ढोए। तीसरा: आग और पानी को एक साथ न ले चले। "
                   "‘युगपत्’ का अर्थ है एक साथ, और वह पहले तथा तीसरे निषेध में काम करता है। "
                   "‘अग्निवारिणी’ द्विवचन है: अग्नि और जल। सिर पर ढोने की बात आग-पानी पर लागू "
                   "होती है या नहीं, श्लोक नहीं बताता।"),
    "hook": "दोनों हाथों से एक साथ सिर नहीं खुजलाना · सिर पर बोझ नहीं · आग-पानी साथ नहीं।",
    "core": False,
    "questions": [
        mcq("pretest", 0,
            "What does line 1 say about scratching one's own head?",
            ("Not with both hands at once",
             "पाणिद्वयेन युगपत् … न कंडूयेत्: not with both hands together."),
            [("Not with the left hand", "Left and right hands are not mentioned."),
             ("Not before sunrise", "No time of day is given."),
             ("Not with a comb", "A comb is not named.")],
            "Line 1 forbids scratching the head with both hands at the same time.",
            "पाणिद्वयेन + युगपत् + न कंडूयेत् + आत्मनः शिरः."),
        match(1, "Match each word to its meaning.",
              [["पाणिद्वयेन", "with both hands"], ["युगपत्", "at once"],
               ["शिरसा", "on the head"], ["भारम्", "a load"],
               ["अग्निवारिणी", "fire and water"]],
              "These five words carry the three prohibitions.",
              "पाणिद्वयेन = with both hands; युगपत् = at once; शिरसा = on the head; भारम् = load."),
        mcq("extend", 2, "Which is the right split of वहेन्न भारं?",
            ("वहेत् + न + भारम्",
             "Final त् before न becomes न्: वहेत् + न = वहेन्न."),
            [("वहेन + न + भारम्", "The verb is वहेत् (should carry), not वहेन."),
             ("वहेत् + ना + भारम्", "ना is not a word here; the word is न."),
             ("वहे + न्न + भारम्", "न्न is not a word.")],
            "वहेत् (should carry) + न (not) + भारम् (load).",
            "त् + न → न्न.",
            teaches="A final त् before न becomes न्न (वहेत् + न = वहेन्न); the same joins कंडूयेत् + न."),
        multi("discriminate", 3, "Which does the unit name as things not to do? Choose all that apply.",
              [("scratch the head with both hands at once", "Right: line 1."),
               ("carry a load on the head", "Right: line 2."),
               ("carry fire and water together", "Right: line 2."),
               ("carry water on the back", "Not in the verse."),
               ("sleep with the head covered", "Not in the verse.")],
              [0, 1, 2],
              "The verse names exactly these three prohibitions; the other two are not in it.",
              "Three: both hands scratching, load on head, fire and water together."),
        order(4, "Put the three prohibitions in the order of the verse.",
              ["सिर को दोनों हाथों से एक साथ खुजलाना", "सिर पर बोझ ढोना", "आग और पानी को एक साथ ढोना"],
              "The verse gives scratching the head first, then the load on the head, then fire and water.",
              "खुजलाना · बोझ · अग्नि-जल.", role="apply"),
        mcq("transfer", 5, "How is तत् + च written when joined?",
            ("तच्च", "A final त् before च becomes च्, as in युगपत् + च = युगपच्च."),
            [("तत्च", "त् changes before च."),
             ("तज्च", "The त् becomes the unvoiced च्, not ज्."),
             ("तस्च", "No स् is formed.")],
            "युगपच्चाग्निवारिणी is युगपत् + च + अग्निवारिणी; in the same way तत् + च = तच्च.",
            "त् + च → च्च.",
            teaches="A final त् before च becomes च् (युगपत् + च = युगपच्च; तत् + च = तच्च)."),
    ],
}

# ---------------------------------------------------------------- unit 95
AUTHORED["95"] = {
    "title": "नासिकां न विकुष्णीयात्",
    "question": "Which body parts are named, and which words of the list are clear?",
    "rule": ("Line 1 names the nose (नासिका) and the teeth (दशन) as objects of "
             "prohibited acts. Line 2 lists cutting, splitting, snapping and "
             "rubbing; the text of both lines is doubtful."),
    "limits": ("Low confidence. The verb after दशनान्न (विषह्वयेत्) is unclear, "
               "विकुष्णीयात् is an inferred sense, and line 2 starts with a doubtful "
               "print that would make it a command. Only clear words are tested."),
    "explain_hi": ("यह इकाई दूषित है, इसलिए केवल साफ़ शब्दों पर प्रश्न हैं। पहली पंक्ति में "
                   "नाक (नासिका) और दाँत (दशन) कर्म के रूप में आते हैं; ‘विकुष्णीयात्’ का ‘कुरेदना/"
                   "खींचना’ अर्थ अनुमान से लिया गया है, और दाँतों वाली क्रिया (‘विषह्वयेत्’) अस्पष्ट है। "
                   "दूसरी पंक्ति में छेद, भेद, आस्फोटन और मर्दन (काटना, फाड़ना, चटकाना, मलना) की "
                   "सूची है, पर पंक्ति का आरंभ संदिग्ध है, इसलिए उसे निषेध मानने पर प्रश्न नहीं बना।"),
    "hook": "नाक और दाँत · छेद-भेद-आस्फोटन-मर्दन (पाठ संदिग्ध)।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "Which body part is named right after the first word of line 1?",
            ("The nose (नासिका)",
             "नासिकां is the first word, accusative: the nose."),
            [("The ear", "No ear is named."),
             ("The eye", "No eye is named."),
             ("The hair", "No hair is named in this unit.")],
            "Line 1 begins with नासिकाम्, the nose; दशनान् (teeth) follows.",
            "नासिकाम् = the nose; दशनान् = the teeth."),
        match(1, "Match each clear word of the unit to its meaning.",
              [["नासिका", "nose"], ["दशन", "tooth"], ["छेद", "cutting"],
               ["भेद", "splitting"], ["मर्दन", "rubbing"]],
              "These words are clear in the print, though the verbs around them are doubtful.",
              "नासिका = nose; दशन = tooth; छेद = cutting; भेद = splitting; मर्दन = rubbing."),
        mcq("extend", 2, "Which is the right split of दशनान्न?",
            ("दशनान् + न",
             "दशनान् is accusative plural, 'teeth'; न is 'not'; the two n sounds meet."),
            [("दशना + अन्न", "अन्न (food) would need a second अ that is not there."),
             ("दशन + अन्न", "That would lose the आ of दशनान् and add a food word."),
             ("दशनान् + अन्न", "No अ stands after the joined न्.")],
            "दशनान् (teeth) + न (not).",
            "A final न् joins a following न without change: दशनान् + न = दशनान्न.",
            teaches="A final न् stays when न follows: दशनान् + न = दशनान्न (no vowel is added)."),
        mcq("discriminate", 3,
            "Why does the card not ask whether line 2 forbids or commands?",
            ("Its first word is doubtful in the print",
             "As printed it would be a command, which the context does not fit."),
            [("The line has no verb at all", "कुर्यात् is there."),
             ("Its words are all unknown", "छेद, भेद, आस्फोटन and मर्दन are clear words."),
             ("It is written in prose", "The unit is verse.")],
            "The doubtful first word makes the sense of the line uncertain, so only the clear list words are tested.",
            "Doubtful print → no question on the disputed sense."),
        order(4, "Put the four clear list words of line 2 in the order of the verse.",
              ["छेद", "भेद", "आस्फोटन", "मर्दन"],
              "The list runs cutting, splitting, snapping, rubbing.",
              "छेद · भेद · आस्फोटन · मर्दन.", role="apply"),
        mcq("transfer", 5, "What does the invented compound छेदभेद mean?",
            ("Cutting and splitting",
             "A dvandva joins items with 'and'."),
            [("The splitting of a cut", "A dvandva lists both items; it does not make one belong to the other."),
             ("Neither cutting nor splitting", "Nothing in the compound is negative."),
             ("A cutter, not a splitter", "The compound names acts, not two kinds of persons.")],
            "छेद + भेद in a dvandva = cutting and splitting, like the list छेद-भेद-आस्फोटन-मर्दन.",
            "Dvandva = A and B (and C …).",
            teaches="A dvandva compound names several items side by side, 'A and B' (छेदभेद = cutting and splitting)."),
    ],
}

# ---------------------------------------------------------------- unit 96
AUTHORED["96"] = {
    "title": "नाकार्ये न च कार्येऽपि",
    "question": "What is one not to do, whether or not there is a purpose?",
    "rule": ("Neither in a matter without purpose nor even in one with purpose "
             "should one make sounds with the mouth, limbs or nails; one should "
             "not press, scratch or clean one foot with the other."),
    "limits": ("अकार्य can be 'without purpose' or 'unnecessary'. The objects of "
               "scratching and cleaning are not stated; the foot is supplied from "
               "line 2. The verse gives no reason."),
    "explain_hi": ("पहली पंक्ति में कहा गया है कि न बिना प्रयोजन के और न प्रयोजन होने पर भी "
                   "मुँह, अंगों या नखों से आवाज़ (वादन) निकाले। ‘अकार्य’ और ‘कार्य’ यहाँ जोड़ी हैं, "
                   "और ‘अपि’ (भी) कार्य वाली स्थिति को भी शामिल करता है। दूसरी पंक्ति में एक पैर "
                   "को दूसरे पैर से दबाना, खुजलाना और साफ़ करना मना है। क्रियाओं का कर्म श्लोक में "
                   "नहीं दिया, पहले चरण से ‘पैर’ लिया गया है।"),
    "hook": "काम हो या न हो — मुँह, अंग, नख से आवाज़ नहीं · पैर से पैर नहीं दबाना-खुजलाना-धोना।",
    "core": False,
    "questions": [
        mcq("pretest", 0,
            "What does line 1 say about making sounds with mouth, limbs or nails?",
            ("Not without purpose, and not even with a purpose",
             "नाकार्ये न च कार्येऽपि: neither in the purposeless nor even in the purposeful."),
            [("Only forbidden when there is no purpose", "The line adds 'even with purpose' (कार्येऽपि)."),
             ("Allowed whenever there is a purpose", "The line forbids it even then."),
             ("Only forbidden with the nails", "Mouth and limbs are named too.")],
            "Line 1 forbids the sounds in both cases: without purpose and even with a purpose.",
            "न अकार्ये + न च कार्ये अपि."),
        match(1, "Match each word of line 1 to its meaning.",
              [["अकार्य", "without purpose"], ["कार्य", "a purposeful matter"],
               ["मुख", "mouth"], ["अङ्ग", "limb"], ["नख", "nail"]],
              "These words make the pair 'without purpose / with purpose' and the three sound-makers.",
              "अकार्य = without purpose; कार्य = a purposeful matter; मुख = mouth; अङ्ग = limb; नख = nail."),
        mcq("extend", 2, "Which is the right split of नाकार्ये?",
            ("न + अकार्ये", "न + अ gives ना."),
            [("ना + कार्ये", "That would mean 'not in a purposeful matter', losing the अ of अकार्य."),
             ("नाक + आर्ये", "नाक is not what stands here."),
             ("न + आकार्ये", "A long आ would give नाकार्ये only if आकार्ये were a word; it is not.")],
            "न (not) + अकार्ये (in what is without purpose).",
            "न + अ → ना.",
            teaches="न followed by a word that begins with अ joins as ना (न + अकार्ये = नाकार्ये)."),
        fill(3, "The word for 'foot' in line 2 is ____ (type it in Devanagari or in English letters, e.g. dharma).",
             accepts("पादम्", None, "पाद"),
             "पादम् is the accusative of पाद, foot: 'one foot'.",
             "पाद is the foot; पादम् is the accusative, पादेन the instrumental ('with the foot').",
             "पादं पादेन = (one) foot with (the other) foot.", role="discriminate"),
        order(4, "Put the three acts done to a foot, in line 2, in the order of the verse.",
              ["आक्रमेत् (दबाए)", "कंडूयेत् (खुजलाए)", "शौचयेत् (साफ़ करे)"],
              "Line 2 says: press, scratch, clean.",
              "आक्रमेत् · कंडूयेत् · शौचयेत्.", role="apply"),
        mcq("transfer", 5, "How is न + अशुचि (न meaning not, अशुचि unclean) written when joined?",
            ("नाशुचि", "न + अ gives ना."),
            [("नशुचि", "The अ would be lost, which sandhi does not do here."),
             ("नैशुचि", "ऐ comes from न + ए, not न + अ."),
             ("नोशुचि", "ओ comes from न + उ, not न + अ.")],
            "As न + अकार्ये = नाकार्ये, न + अशुचि = नाशुचि.",
            "न + अ → ना.",
            teaches="न + अ- gives ना- (नाकार्ये; नाशुचि)."),
    ],
}

# ---------------------------------------------------------------- unit 97
AUTHORED["97"] = {
    "title": "न कांस्यभाजने तौ च",
    "question": "What does line 2 say to keep clean, and how often?",
    "rule": ("Line 2: one should repeatedly (अभीक्ष्णम्) keep clean the nails, the "
             "feet and the seats of impurity (मलाशय)."),
    "limits": ("Line 1 is uncertain: तौ ('those two') is probably the feet of the "
               "previous unit, and the verb for the bronze vessel is not written. "
               "Nothing is built on that line beyond its clear words. The verse "
               "does not name the 'seats of impurity'."),
    "explain_hi": ("पहली पंक्ति अनिश्चित है: ‘तौ’ (वे दोनों) संभवतः पिछले श्लोक के दोनों पैर हैं, "
                   "काँसे के पात्र (कांस्यभाजन) की क्रिया लिखी नहीं है, और ‘बैठकर न फैलाए’ का अन्वय "
                   "उसी पर टिका है। इसलिए पहली पंक्ति के केवल स्पष्ट शब्दों पर प्रश्न हैं। दूसरी पंक्ति "
                   "साफ़ है: नखों, पैरों और मल के आशयों (मल जमा होने के स्थानों) को बार-बार स्वच्छ रखे। "
                   "‘आशय’ कौन-से स्थान हैं, श्लोक नहीं बताता।"),
    "hook": "नख, पाद और मलाशय — बार-बार निर्मल रखे।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "What does line 2 say to do repeatedly?",
            ("Keep the nails, feet and seats of impurity clean",
             "अभीक्ष्णं निर्मलान् दध्यात्: repeatedly keep clean."),
            [("Oil the hair, face and hands", "None of these is named."),
             ("Cover the nails, feet and ears", "Covering is not mentioned."),
             ("Cut the nails, feet and teeth", "Cutting is not mentioned.")],
            "The line tells one to repeatedly keep the nails, the feet and the seats of impurity clean.",
            "अभीक्ष्णं + निर्मलान् + दध्यात् + नख-पाद-मलाशयान्."),
        match(1, "Match each word of line 2 to its meaning.",
              [["अभीक्ष्णम्", "repeatedly"], ["निर्मलान्", "clean ones"],
               ["दध्यात्", "should keep"], ["नख", "nail"], ["पाद", "foot"]],
              "These words carry the instruction of line 2.",
              "अभीक्ष्णम् = repeatedly; निर्मलान् = clean; दध्यात् = should keep; नख = nail; पाद = foot."),
        mcq("extend", 2, "Which is the right split of नोपविष्टः?",
            ("न + उपविष्टः", "अ + उ gives ओ."),
            [("ना + उपविष्टः", "न + उ does not give ना."),
             ("नो + पविष्टः", "पविष्ट is not the word; it is उपविष्ट (seated)."),
             ("नु + उपविष्टः", "There is no नु here.")],
            "न (not) + उपविष्टः (seated).",
            "अ + उ → ओ.",
            teaches="A word ending in -अ meets उ- and they join as ओ (न + उपविष्टः = नोपविष्टः)."),
        mcq("discriminate", 3, "Which translation of line 2 is right?",
            ("One should repeatedly keep clean the nails, the feet and the seats of impurity.",
             "अभीक्ष्णं निर्मलान् दध्यात् नख-पाद-मलाशयान्."),
            [("One should keep clean the hands, the feet and the seats of impurity.", "Hands are not in the list; it has nails."),
             ("One should rarely keep clean the nails, the feet and the seats of impurity.", "अभीक्ष्णम् means repeatedly."),
             ("One should keep the nails and feet away from the seats of impurity.", "The verb is 'keep clean', not 'keep away'.")],
            "The three items are the nails, the feet and the seats of impurity.",
            "नख · पाद · मलाशय, repeatedly clean."),
        order(4, "Put the three things kept clean in line 2 in the order of the verse.",
              ["नख", "पाद", "मलाशय"],
              "The compound runs nails, feet, seats of impurity.",
              "नख · पाद · मलाशय.", role="apply"),
        mcq("transfer", 5, "How is न + उक्तम् (न meaning not, उक्तम् said) written when joined?",
            ("नोक्तम्", "अ + उ gives ओ."),
            [("नुक्तम्", "The vowel would not stay उ."),
             ("नाक्तम्", "ना would come from न + अ."),
             ("नौक्तम्", "औ comes from न + औ.")],
            "As न + उपविष्टः = नोपविष्टः, न + उक्तम् = नोक्तम्.",
            "अ + उ → ओ.",
            teaches="न + उ- gives नो- (नोपविष्टः; नोक्तम्)."),
    ],
}

# ---------------------------------------------------------------- unit 98
AUTHORED["98"] = {
    "title": "नासमिद्धमुपासीत",
    "question": "In which six conditions is one not to tend the fire?",
    "rule": ("One should not tend (उपासीत) the fire when it is unkindled, when "
             "one is unclean, along the wind, uncovered, weary, or with the "
             "mind elsewhere."),
    "limits": ("विवृत 'uncovered' may mean bare of body; the verse does not say. "
               "The verb उपासीत of line 1 is carried to line 2. The verse gives "
               "no reason for any of the conditions."),
    "explain_hi": ("इस युग्म में अग्नि (हुताश) की उपासना, यानी उसकी सेवा, छह स्थितियों में "
                   "मना है: जब वह जला हुआ न हो (असमिद्ध), जब स्वयं अशुद्ध हो, हवा की दिशा में, "
                   "अनावृत (खुला), थका हुआ, और अन्यमनस्क। क्रिया ‘उपासीत’ पहली पंक्ति में है और दूसरी "
                   "में भी चलती है। ‘अन्यमानसः’ बहुव्रीहि है: जिसका मन अन्यत्र है। श्लोक किसी स्थिति "
                   "का कारण नहीं बताता।"),
    "hook": "असमिद्ध, अशुचि, अनुवात, विवृत, क्लान्त, अन्यमानस — इन छह में अग्नि की उपासना नहीं।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "What does line 1 say about tending a fire that is unkindled?",
            ("One should not tend it",
             "नासमिद्धमुपासीत: not tend the unkindled."),
            [("One should tend it first", "The न forbids it."),
             ("One should tend it only at night", "No time of day is given."),
             ("One should tend it with water", "Water is not mentioned.")],
            "असमिद्ध means not kindled; with न उपासीत the verse says one should not tend such a fire.",
            "न + असमिद्धम् + उपासीत + हुताशम्."),
        match(1, "Match each condition to its meaning.",
              [["असमिद्ध", "not kindled"], ["अशुचि", "unclean"],
               ["अनुवात", "along the wind"], ["विवृत", "uncovered"],
               ["क्लान्त", "weary"], ["अन्यमानस", "with mind elsewhere"]],
              "These six conditions fill the two lines, one after another.",
              "असमिद्ध = not kindled; अशुचि = unclean; अनुवातम् = along the wind; विवृत = uncovered; क्लान्त = weary."),
        mcq("extend", 2, "What does अन्यमानसः mean?",
            ("One whose mind is elsewhere",
             "A bahuvrīhi describes a person by what he has: अन्य-मानस, 'other mind'."),
            [("The mind of another person", "That would be an ordinary genitive, not a person described by it."),
             ("A mind free from others", "अन्य means 'other', not 'free from'."),
             ("Another person's thought", "The compound names the person, not a thought.")],
            "The compound describes the person: he whose mind (मानस) is elsewhere (अन्य).",
            "A bahuvrīhi names the owner of the parts: अन्यमानसः = whose mind is elsewhere.",
            teaches="A bahuvrīhi describes a person by what he has (अन्यमानसः = one whose mind is elsewhere; असंवृतमुखः = with mouth uncovered)."),
        multi("discriminate", 3, "Which does the verse name as conditions in which not to tend the fire? Choose all that apply.",
              [("when the fire is unkindled", "Right: असमिद्ध."),
               ("when one is weary", "Right: क्लान्त."),
               ("when one's mind is elsewhere", "Right: अन्यमानस."),
               ("when one is angry", "Anger is not in this verse."),
               ("when one is hungry", "Hunger is not in this verse.")],
              [0, 1, 2],
              "Unkindled, weary and mind elsewhere are in the verse; anger and hunger are not.",
              "Six conditions: unkindled, unclean, along the wind, uncovered, weary, mind elsewhere."),
        order(4, "Put the six conditions in the order of the verse.",
              ["असमिद्ध", "अशुचि", "अनुवात", "विवृत", "क्लान्त", "अन्यमानस"],
              "Line 1 gives unkindled and unclean; line 2 gives along the wind, uncovered, weary, mind elsewhere.",
              "असमिद्ध · अशुचि · अनुवात · विवृत · क्लान्त · अन्यमानस.", role="apply"),
        mcq("transfer", 5, "How is न + एकम् (न meaning not, एकम् one) written when joined?",
            ("नैकम्", "अ + ए gives ऐ, as in न + एव = नैव."),
            [("नेकम्", "अ + ए does not stay ए."),
             ("नाइकम्", "No इ is inserted."),
             ("नोकम्", "ओ comes from अ + उ.")],
            "The verse has नैव from न + एव; in the same way न + एकम् = नैकम्.",
            "अ + ए → ऐ.",
            teaches="न + ए- gives नै- (नैव, from न + एव; नैकम्, from न + एकम्)."),
    ],
}

# ---------------------------------------------------------------- unit 99
AUTHORED["99"] = {
    "title": "धमेन्नास्येन",
    "question": "What is one not to blow with the mouth, and not to gaze at constantly?",
    "rule": ("Line 1 continues the fire of the previous unit: it is not to be "
             "blown with the mouth. Line 2: one should not constantly gaze at "
             "things that are moving, minute or unpleasant."),
    "limits": ("Line 1 is compressed: 'it' (the fire) is supplied, skandet may be "
               "'leap over' or 'spill', and the rest ('put down low', 'with the "
               "foot') is elliptical, so the card asks nothing on those. Line 2 "
               "begins a list that goes on through units 100 to 102."),
    "explain_hi": ("पहली पंक्ति पिछली इकाई की आग की बात आगे बढ़ाती है: उसे मुँह से न फूँके। "
                   "‘स्कंदेत्’ का अर्थ लाँघना भी हो सकता है और गिराना भी, तथा ‘नीचे रखे’ और ‘पैर से’ "
                   "संक्षिप्त हैं, इसलिए इन पर प्रश्न नहीं बने। दूसरी पंक्ति नई सूची शुरू करती है: "
                   "चलती हुई, सूक्ष्म और अप्रिय वस्तुओं को लगातार (सततम्) न देखता रहे। यह सूची इकाई "
                   "१०० से १०२ तक चलती है।"),
    "hook": "आग मुँह से नहीं फूँकनी · चल, सूक्ष्म, अप्रिय को लगातार नहीं देखना।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "What does line 2 say one should not do constantly?",
            ("Gaze at moving, minute or unpleasant things",
             "सततं न निरीक्षेत चलसूक्ष्माप्रियाणि."),
            [("Walk among crowded places", "Walking is not in the line."),
             ("Speak of unpleasant things", "The verb is gazing, not speaking."),
             ("Handle small tools for long", "Handling is not in the line.")],
            "Line 2 forbids constant gazing at things that are moving, minute or unpleasant.",
            "सततम् + न निरीक्षेत + चल-सूक्ष्म-अप्रियाणि."),
        match(1, "Match each word of the unit to its meaning.",
              [["आस्य", "mouth"], ["सततम्", "constantly"],
               ["चल", "moving"], ["सूक्ष्म", "minute"], ["अप्रिय", "unpleasant"]],
              "These words carry the two clear instructions.",
              "आस्य = mouth; सततम् = constantly; चल = moving; सूक्ष्म = minute; अप्रिय = unpleasant."),
        mcq("extend", 2, "Which is the right split of चलसूक्ष्माप्रियाणि?",
            ("चल + सूक्ष्म + अप्रियाणि", "आ here is अ + अ: सूक्ष्म + अप्रियाणि."),
            [("चल + सूक्ष्मा + प्रियाणि", "That loses the negative अ of अप्रिय, 'dear' instead of 'unpleasant'."),
             ("चला + सूक्ष्म + अप्रियाणि", "The first part has no long आ."),
             ("चल + सूक्ष्म + आप्रियाणि", "आप्रिय is not a word.")],
            "Three words are joined: moving, minute, unpleasant (अ-प्रिय, 'not dear').",
            "अ + अ → आ: सूक्ष्म + अप्रिय = सूक्ष्माप्रिय.",
            teaches="Two short अ meeting join as आ (सूक्ष्म + अप्रिय = सूक्ष्माप्रिय; न + अकार्ये = नाकार्ये)."),
        mcq("discriminate", 3, "Which translation of the sandhi in धमेन्नास्येन is right?",
            ("One should not blow with the mouth",
             "धमेत् + न + आस्येन: not blow with the mouth."),
            [("One should not blow with the foot", "पाद, foot, is not in this word."),
             ("One should blow with the mouth", "The न forbids it."),
             ("One should not eat with the mouth", "The verb is धमेत्, blow, not eat.")],
            "आस्येन is 'with the mouth'; धमेत् is 'should blow'; न forbids it.",
            "धमेत् + न + आस्येन."),
        order(4, "Put the three kinds of thing in line 2 in the order of the verse.",
              ["चल (moving)", "सूक्ष्म (minute)", "अप्रिय (unpleasant)"],
              "The list runs moving, minute, unpleasant.",
              "चल · सूक्ष्म · अप्रिय.", role="apply"),
        mcq("transfer", 5, "What does the invented neuter plural compound मधुरशीतानि mean?",
            ("Sweet and cold things",
             "A neuter plural ending -ानि lists adjectives, as चलसूक्ष्माप्रियाणि does."),
            [("One thing both sweet and cold", "-ानि is plural: several things."),
             ("Neither sweet nor cold things", "No negative is in it."),
             ("Sweetness of cold", "The compound lists qualities of things, not an abstract noun.")],
            "Like चल-सूक्ष्म-अप्रियाणि (moving, minute, unpleasant things), मधुरशीतानि means sweet and cold things.",
            "Neuter plural compound = 'A, B (things)'.",
            teaches="A neuter plural adjective list ending in -ाणि/-ानि means 'things that are A, B' (चलसूक्ष्माप्रियाणि; मधुरशीतानि)."),
    ],
}

# ---------------------------------------------------------------- unit 100
AUTHORED["100"] = {
    "title": "नाप्रशस्तं न विण्मूत्रं",
    "question": "What does line 1 list among things not to gaze at, and where is the noun of line 2?",
    "rule": ("The verb 'should not gaze' comes from unit 99. Line 1 lists the "
             "inauspicious, faeces and urine, and an unwiped mirror. The "
             "participles of line 2 wait for their noun in unit 101."),
    "limits": ("Low confidence. The last word (प्रतिभागतं) is doubtful and is not "
               "tested. The participles of line 2 have no noun in this unit; "
               "they go with भास्वन्तम् in unit 101 (the sun, by the notes), so "
               "100 and 101 are one sentence."),
    "explain_hi": ("इस इकाई में क्रिया ‘न निरीक्षेत’ पिछली इकाई (९९) से आती है। पहली पंक्ति में "
                   "न देखने योग्य चीज़ें गिनाई गई हैं: अप्रशस्त (अशुभ), मल-मूत्र और बिना पोंछा "
                   "दर्पण। दूसरी पंक्ति में ‘उगता, अस्त की ओर जाता, तपता’ जैसे विशेषण हैं, पर संज्ञा "
                   "इस इकाई में नहीं है; वह अगली इकाई के ‘भास्वन्तम्’ से जुड़ती है। अंतिम शब्द "
                   "‘प्रतिभागतं’ संदिग्ध है, इसलिए उस पर प्रश्न नहीं बना।"),
    "hook": "अप्रशस्त, मल-मूत्र, बिना पोंछा दर्पण · उगता, अस्त होता, तपता — संज्ञा अगली इकाई में।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "Which of these does line 1 name among things not to gaze at?",
            ("An unwiped mirror",
             "दर्पणममार्जितं: a mirror that has not been wiped."),
            [("A clean mirror", "The line says अमार्जित, not wiped."),
             ("A burning lamp", "No lamp is named."),
             ("A flowing river", "No river is named.")],
            "Line 1 lists the inauspicious, faeces and urine, and an unwiped mirror.",
            "अप्रशस्तम् · विण्मूत्रम् · अमार्जितं दर्पणम्."),
        match(1, "Match each word to its meaning.",
              [["अप्रशस्त", "inauspicious"], ["विण्मूत्र", "faeces and urine"],
               ["अमार्जित", "unwiped"], ["उद्यन्तम्", "rising"],
               ["तपन्तम्", "blazing"]],
              "These are the clear words of the two lines.",
              "अप्रशस्त = inauspicious; विण्मूत्र = faeces and urine; अमार्जित = unwiped; उद्यन्तम् = rising; तपन्तम् = blazing."),
        mcq("extend", 2, "What kind of compound is विण्मूत्रं?",
            ("A dvandva: faeces and urine",
             "Two nouns side by side joined by 'and' make a dvandva."),
            [("A compound meaning 'urine of faeces'", "That would be a genitive tatpuruṣa, which the pair does not need."),
             ("A negative compound: no urine", "There is no negative prefix in it."),
             ("A bahuvrīhi: one who has urine", "The compound names the two things themselves, not a person.")],
            "विष् (faeces) and मूत्र (urine) stand side by side, 'faeces and urine'.",
            "Dvandva = A and B.",
            teaches="A dvandva puts two or more nouns side by side meaning 'A and B' (विण्मूत्रम्; हास्यक्षव…)."),
        mcq("discriminate", 3, "Where is the noun that the participles उद्यन्तम्, आयान्तम्, तपन्तम् describe?",
            ("In unit 101, as भास्वन्तम्",
             "Unit 100 has no noun for them; the notes join them with the 'shining one' of unit 101."),
            [("In line 1 of this unit, as दर्पणम्", "दर्पणम् is a mirror and does not fit 'rising'."),
             ("In unit 99, as चल", "चल is an adjective, not a noun for these."),
             ("It is the word प्रतिभागतम् itself", "That is another participle, and is doubtful.")],
            "The participles are accusative masculine and wait for भास्वन्तम् in the next unit.",
            "Units 100 and 101 form one sentence."),
        order(4, "Put the three things of line 1 in the order of the verse.",
              ["अप्रशस्त", "विण्मूत्र", "अमार्जित दर्पण"],
              "Line 1 gives the inauspicious, faeces and urine, then the unwiped mirror.",
              "अप्रशस्त · विण्मूत्र · अमार्जित दर्पण.", role="apply"),
        mcq("transfer", 5, "Which phrase agrees with अग्निम् (fire, masculine accusative) to say blazing fire?",
            ("अग्निं तपन्तम्",
             "A masculine accusative noun takes -न्तम्, like तपन्तम्."),
            [("अग्निं तपन्ती", "-न्ती is feminine."),
             ("अग्निं तपन्तः", "-न्तः is nominative."),
             ("अग्निं तपन्तीम्", "-न्तीम् is feminine accusative.")],
            "A participle agrees with its noun: masculine accusative singular तपन्तम्.",
            "Participle agrees in case, number and gender.",
            teaches="A participle agrees with its noun in case, number and gender (तपन्तम्, masculine accusative, with a masculine noun)."),
    ],
}

# ---------------------------------------------------------------- unit 101
AUTHORED["101"] = {
    "title": "उपरक्तं च भास्वंतं",
    "question": "Which sights does the unit add to the list of things not to gaze at?",
    "rule": ("Not to be gazed at: the shining one (the sun, by the notes) when "
             "eclipsed or covered by a cloth, anything else excessively bright, "
             "and the face of an angry teacher."),
    "limits": ("भास्वन्तम् is taken as the sun, a common word for it, though the "
               "verse does not say 'sun'. The verb comes from unit 99; the "
               "participles of unit 100 go with भास्वन्तम्. The print has कुद्ध "
               "for क्रुद्ध (angry), a spelling slip."),
    "explain_hi": ("यह इकाई पिछली सूची को पूरा करती है। ‘भास्वन्तम्’ (चमकने वाला, यहाँ सूर्य) को "
                   "ग्रहण-ग्रस्त या वस्त्र से ढका हुआ न देखे; इसके अलावा कोई भी अत्यन्त तेजस्वी चीज़ "
                   "नहीं, और क्रोधित गुरु का मुख भी नहीं। क्रिया ‘न निरीक्षेत’ इकाई ९९ से आती है, और "
                   "इकाई १०० के विशेषण (उगता, तपता आदि) ‘भास्वन्तम्’ के साथ जुड़ते हैं। छपे ‘कुद्ध’ को "
                   "‘क्रुद्ध’ (क्रोधित) पढ़ा गया है।"),
    "hook": "ग्रहण-ग्रस्त या ढका सूर्य, अति तेजस्वी, क्रुद्ध गुरु का मुख — देखना नहीं।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "Whose face does line 2 say one should not gaze at?",
            ("An angry teacher's",
             "न क्रुद्धस्य गुरोर्मुखं: not the face of an angry teacher."),
            [("A sleeping child's", "No child is named."),
             ("A guest's", "No guest is named."),
             ("A king's", "No king is named.")],
            "Line 2 ends with the face of an angry (क्रुद्ध) teacher (गुरु).",
            "न + क्रुद्धस्य गुरोः मुखम्."),
        match(1, "Match each word to its meaning.",
              [["उपरक्त", "eclipsed"], ["भास्वन्तम्", "the shining one"],
               ["तिरोहित", "hidden, covered"], ["अतितेजस्वि", "excessively bright"],
               ["गुरु", "teacher"]],
              "These words carry the four sights of the unit.",
              "उपरक्त = eclipsed; भास्वन्तम् = the shining one; तिरोहित = covered; अतितेजस्वि = excessively bright."),
        mcq("extend", 2, "Which is the right split of नान्यदप्यतितेजस्वि?",
            ("न + अन्यत् + अपि + अतितेजस्वि",
             "Each junction is a plain vowel sandhi; final त् becomes द् before the vowel."),
            [("न + अन्य + दपि + अतितेजस्वि", "दपि is not a word; the word is अपि."),
             ("ना + अन्यत् + अपि + तेजस्वि", "अति is part of the adjective अतितेजस्वि."),
             ("न + अन्यद् + अपि + अति + तेजस्वि", "अन्यद् is only the sandhi form of अन्यत्; the base word is अन्यत्.")],
            "न (not) + अन्यत् (other) + अपि (even) + अतितेजस्वि (excessively bright).",
            "Final त् + vowel → द्: अन्यत् + अपि = अन्यदपि.",
            teaches="A final त् before a vowel is written द् (अन्यत् + अपि = अन्यदपि)."),
        mcq("discriminate", 3, "What does भास्वन्तम् stand for here, by the notes?",
            ("The sun, 'the shining one'",
             "भास्वत् is a common word for the sun; the notes read it so."),
            [("The moon", "The moon is not named in this unit."),
             ("A lamp", "The unit speaks of being eclipsed, which does not suit a lamp."),
             ("The teacher", "The teacher is named separately as गुरु.")],
            "भास्वन्तम् is 'the shining one', taken as the sun; eclipse and cloth fit it.",
            "भास्वत् = shining (the sun)."),
        order(4, "Put the four sights of the unit in the order of the verse.",
              ["ग्रहण-ग्रस्त (भास्वन्तम्)", "वस्त्र से ढका (भास्वन्तम्)", "कोई अन्य अतितेजस्वी", "क्रुद्ध गुरु का मुख"],
              "The unit gives the eclipsed one, the one covered by a cloth, anything else too bright, the angry teacher's face.",
              "उपरक्त · वाससा तिरोहित · अन्य अतितेजस्वि · क्रुद्ध गुरु का मुख.", role="apply"),
        mcq("transfer", 5, "How is तत् + अपि written when joined?",
            ("तदपि", "A final त् before a vowel becomes द्."),
            [("तत्पि", "The अ of अपि does not disappear."),
             ("ततपि", "The त् does not double."),
             ("तथपि", "थ is a different sound.")],
            "As अन्यत् + अपि = अन्यदपि, तत् + अपि = तदपि.",
            "त् + vowel → द् + vowel.",
            teaches="A final त् before a vowel is written द् (अन्यदपि; तदपि)."),
    ],
}

# ---------------------------------------------------------------- unit 102
AUTHORED["102"] = {
    "title": "स्त्रियं स्रवंतीं नोदक्यां",
    "question": "Which four states of a woman does line 1 list?",
    "rule": ("Line 1 (with the verb 'should not gaze' from unit 99) lists a woman "
             "who is discharging, a menstruating woman, a naked woman, and one "
             "united with another. Line 2 names drinking, eating, yawning and "
             "sitting at ease, with one corrupt word."),
    "limits": ("Low confidence. In line 2 the word खमस्रुत is unreadable (the "
               "editors guess क्षुत, 'sneeze'), so nothing rests on it. स्रवन्ती "
               "could be 'river' in general, but स्त्रियम् makes it a woman. Who "
               "line 2 refers to is inferred from line 1."),
    "explain_hi": ("इस इकाई में क्रिया ‘न निरीक्षेत’ इकाई ९९ से आती है। पहली पंक्ति में स्त्री की चार "
                   "अवस्थाएँ गिनाई गई हैं: बहती/स्रावयुक्त (स्रवन्ती), रजस्वला (उदक्या), नग्न, और जो "
                   "दूसरे के साथ संगत हो (अन्यसंगता)। दूसरी पंक्ति में पीना, खाना, जम्हाई और आराम से "
                   "बैठना आते हैं, पर बीच का एक शब्द (‘खमस्रुत’) बिगड़ा हुआ है और संपादकों का ‘क्षुत’ "
                   "केवल अनुमान है, इसलिए उस पर प्रश्न नहीं बना।"),
    "hook": "स्रवन्ती, उदक्या, नग्ना, अन्यसंगता — स्त्री की चार अवस्थाएँ · दूसरी पंक्ति में एक शब्द बिगड़ा।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "Which of these states of a woman does line 1 list?",
            ("Naked (नग्ना)",
             "नग्नां is in the list: naked."),
            [("Asleep", "Sleep is not in the list."),
             ("Weeping", "Weeping is not in the list."),
             ("Travelling", "Travel is not in the list.")],
            "The four states of line 1 are discharging, menstruating, naked and united with another.",
            "स्रवन्तीम् · उदक्याम् · नग्नाम् · अन्यसंगताम्."),
        match(1, "Match each word of line 1 to its meaning.",
              [["स्रवन्ती", "discharging"], ["उदक्या", "menstruating woman"],
               ["नग्ना", "naked"], ["अन्यसंगता", "united with another"]],
              "These four words are the states listed for the woman.",
              "स्रवन्ती = discharging; उदक्या = menstruating woman; नग्ना = naked; अन्यसंगता = united with another."),
        mcq("extend", 2, "Which is the right split of नोदक्यां?",
            ("न + उदक्याम्", "अ + उ gives ओ."),
            [("ना + उदक्याम्", "ना would come from न + अ."),
             ("नो + दक्याम्", "The word is उदक्या, not दक्या."),
             ("न + ओदक्याम्", "There is no ओ in the word.")],
            "न (not) + उदक्याम् (a menstruating woman).",
            "अ + उ → ओ.",
            teaches="न + उ- joins as नो- (नोदक्याम्, like नोपविष्टः)."),
        multi("discriminate", 3, "Which activities does line 2 name? One word in the line is corrupt. Choose all that apply.",
              [("drinking (पान)", "Right: the first item."),
               ("eating (भोजन)", "Right: the second item."),
               ("yawning (जृम्भा)", "Right: it follows the corrupt word."),
               ("walking", "Not in the line."),
               ("sleeping", "Not in the line.")],
              [0, 1, 2],
              "Drinking, eating and yawning are clear (and sitting at ease, सुखासन); walking and sleeping do not occur.",
              "पान · भोजन · (corrupt word) · जृम्भा · सुखासन."),
        order(4, "Put the four states of line 1 in the order of the verse.",
              ["स्रवन्तीम्", "उदक्याम्", "नग्नाम्", "अन्यसंगताम्"],
              "Line 1 runs discharging, menstruating, naked, united with another.",
              "स्रवन्तीम् · उदक्याम् · नग्नाम् · अन्यसंगताम्.", role="apply"),
        mcq("transfer", 5, "Which word agrees with the invented बालाम् (a girl, accusative) to say 'naked'?",
            ("नग्नाम्", "A feminine accusative singular adjective ends in -ाम्, like नग्नाम्."),
            [("नग्नम्", "-म् is neuter or masculine."),
             ("नग्नः", "-ः is masculine nominative."),
             ("नग्ना", "-ा is feminine nominative.")],
            "An adjective takes the gender, number and case of its noun: feminine accusative singular नग्नाम्.",
            "Adjective agrees with its noun.",
            teaches="An adjective agrees with its noun in gender, number and case: feminine accusative singular is -ाम् (नग्नाम्) or -ीम् (स्रवन्तीम्)."),
    ],
}

# ---------------------------------------------------------------- unit 103
AUTHORED["103"] = {
    "title": "शयीत नैकशयने",
    "question": "What does line 1 say about sleeping and eating with 'her'?",
    "rule": ("Line 1: one should not sleep on the same bed with her, and should "
             "not eat together with her. Line 2 is damaged and is not used."),
    "limits": ("Low confidence. Line 2 is corrupt: 'anīrṇya' (probably 'free from "
               "jealousy'), 'svairiṇī' and 'nāśayed ahaṃ' have no secure reading. "
               "Who 'her' (तया) is, is inferred from unit 102 and is not "
               "tested. The verse gives no reason."),
    "explain_hi": ("पहली पंक्ति स्पष्ट है: उसके (तया) साथ एक ही शय्या पर न सोए, और उसके साथ "
                   "बैठकर भोजन न करे। ‘तया’ संभवतः पिछली इकाई की स्त्री है, पर यह अनुमान है। दूसरी "
                   "पंक्ति में ‘तामनीर्ण्यश्च’, ‘स्वैरिणी’ और ‘नाशयेदहं’ बिगड़े हुए हैं: ‘ईर्ष्या-रहित होकर "
                   "रक्षा करे’ जैसा अर्थ केवल संभव है। इसलिए दूसरी पंक्ति पर कोई प्रश्न नहीं बना।"),
    "hook": "उसके साथ एक शय्या पर नहीं सोना, साथ भोजन नहीं करना · दूसरी पंक्ति बिगड़ी।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "What does line 1 say about sleeping?",
            ("Not on the same bed with her",
             "शयीत नैकशयने: not on one (the same) bed."),
            [("Only on the ground", "The ground is not mentioned."),
             ("Only by day", "No time of day is given."),
             ("Not at all", "It forbids the same bed, not all sleep.")],
            "Line 1 says one should not sleep on the same bed (एकशयने) with her.",
            "शयीत + न + एकशयने."),
        match(1, "Match each word of line 1 to its meaning.",
              [["शयीत", "should sleep"], ["एकशयने", "on the same bed"],
               ["अश्नीयात्", "should eat"], ["तया", "with her"],
               ["सह", "together"]],
              "These five words carry both prohibitions of line 1.",
              "शयीत = should sleep; एकशयने = on the same bed; अश्नीयात् = should eat; तया = with her; सह = together."),
        mcq("extend", 2, "Which is the right split of नैकशयने?",
            ("न + एकशयने", "अ + ए gives ऐ."),
            [("न + ऐकशयने", "ऐकशयन is not the word; the word is एकशयन."),
             ("ना + एकशयने", "ना would come from न + अ, and then the ए would stay separate."),
             ("नै + कशयने", "कशयन is not a word.")],
            "न (not) + एकशयने (on one bed, on the same bed).",
            "अ + ए → ऐ.",
            teaches="न + ए- joins as नै- (नैकशयने; नैव)."),
        mcq("discriminate", 3, "Which is right for न चाश्नीयात्तया सह?",
            ("And one should not eat together with her",
             "न च अश्नीयात् तया सह: not eat with her."),
            [("And one should eat together with her", "The न forbids it."),
             ("And one should not eat before her", "तया सह is 'together with her', not 'before'."),
             ("And one should not sleep beside her", "The verb is अश्नीयात्, eat; sleeping was line 1.")],
            "अश्नीयात् is 'should eat', तया सह is 'together with her', and न forbids it.",
            "न + अश्नीयात् + तया सह."),
        order(4, "Put the main words of line 1 in the order of the verse (leaving out न).",
              ["शयीत", "एकशयने", "अश्नीयात्", "तया", "सह"],
              "Line 1 runs: should sleep, on one bed, should eat, with her, together.",
              "शयीत · एकशयने · अश्नीयात् · तया · सह.", role="apply"),
        mcq("transfer", 5, "What does the invented compound एकासने mean?",
            ("On the same seat",
             "एक in such a compound means 'one, the same', as in एकशयने."),
            [("On every seat", "एक is 'one', not 'every'."),
             ("On no seat", "There is no negative."),
             ("On a higher seat", "Nothing like 'higher' is in it.")],
            "Like एकशयने (on the same bed), एकासने is एक + आसने: on the same seat.",
            "एक + noun = the same … .",
            teaches="एक at the start of a compound can mean 'the same' (एकशयने = on the same bed; एकासने = on the same seat)."),
    ],
}

# ---------------------------------------------------------------- unit 104
AUTHORED["104"] = {
    "title": "नोच्छिष्टस्तारकाराहतुहिनांशुदिवाकरान्",
    "question": "What must the person who is ucchiṣṭa not do, according to this unit?",
    "rule": ("While ucchiṣṭa (unpurified from food), one should not look at the "
             "stars, the moon or the sun; nor go, recite or study, sleep, or "
             "touch the head."),
    "limits": ("The print has राह for a probable राहु (the editors suggest it), so "
               "Rāhu is left out of the questions. The verbs यायात्, पठेत्, स्वप्यात् have "
               "no object. उच्छिष्ट is 'one who has eaten and not cleansed'; the verse "
               "gives no further rule."),
    "explain_hi": ("इस युग्म में एक शर्त है, ‘उच्छिष्ट’ यानी खाने के बाद जो अभी शुद्ध नहीं हुआ। उस "
                   "अवस्था में तारों, चन्द्रमा (तुहिनांशु) और सूर्य (दिवाकर) को न देखे; छपा ‘राह’ संभवतः "
                   "‘राहु’ है, पर यह सुझाव है। दूसरी पंक्ति में पाँच निषेध क्रम से हैं: देखना, जाना, पढ़ना, "
                   "सोना और सिर को छूना। ‘जाना’ का गंतव्य श्लोक में नहीं दिया।"),
    "hook": "उच्छिष्ट रहते: तारे-चन्द्र-सूर्य को देखना, जाना, पढ़ना, सोना, सिर छूना — सब नहीं।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "Which state does this unit make the condition for its prohibitions?",
            ("Being ucchiṣṭa, unpurified from food",
             "नोच्छिष्टः: not (to do these) while ucchiṣṭa."),
            [("Being weary", "Weariness belongs to unit 98."),
             ("Being naked", "Nakedness belongs to unit 102."),
             ("Being angry", "Anger belongs to unit 101, and concerns the teacher.")],
            "The unit begins with उच्छिष्टः, one who has eaten and not yet cleansed.",
            "न + उच्छिष्टः … पश्येत् … न."),
        match(1, "Match each word to its meaning.",
              [["उच्छिष्ट", "unpurified from food"], ["तारका", "star"],
               ["तुहिनांशु", "the moon, cool-rayed"], ["दिवाकर", "the sun"],
               ["शिरः", "head"]],
              "These words carry the condition and the objects of the unit.",
              "उच्छिष्ट = unpurified from food; तारका = star; तुहिनांशु = moon; दिवाकर = sun; शिरः = head."),
        mcq("extend", 2, "Which is the right split of स्पृशेच्छिरः?",
            ("स्पृशेत् + शिरः", "Final त् before श joins as च्छ."),
            [("स्पृशे + च्छिरः", "च्छिर is not a word."),
             ("स्पृशेच् + शिरः", "The verb is स्पृशेत्, not स्पृशेच्."),
             ("स्पृशेत् + छिरः", "There is no word छिरः; the word is शिरः.")],
            "स्पृशेत् (should touch) + शिरः (head).",
            "त् + श → च्छ.",
            teaches="A final त् before श becomes च्छ (स्पृशेत् + शिरः = स्पृशेच्छिरः)."),
        mcq("discriminate", 3, "Which word names the sun in line 1?",
            ("दिवाकर", "दिवाकर, 'day-maker', is the sun."),
            [("तारका", "तारका is a star."),
             ("तुहिनांशु", "तुहिनांशु, 'cool-rayed', is the moon."),
             ("उच्छिष्ट", "उच्छिष्ट is a state of the person.")],
            "The compound lists stars, then the moon (तुहिनांशु), then the sun (दिवाकर).",
            "तुहिनांशु = moon; दिवाकर = sun."),
        order(4, "Put the five prohibited acts of line 2 in the order of the verse.",
              ["पश्येत् (देखे)", "यायात् (जाए)", "पठेत् (पढ़े)", "स्वप्यात् (सोए)", "स्पृशेत् (छुए)"],
              "Line 2 runs: look, go, recite, sleep, touch the head.",
              "पश्येत् · यायात् · पठेत् · स्वप्यात् · स्पृशेत् शिरः.", role="apply"),
        mcq("transfer", 5, "How is तत् + शरीरम् written when joined?",
            ("तच्छरीरम्", "A final त् before श becomes च्छ."),
            [("तत्शरीरम्", "त् changes before श."),
             ("तश्शरीरम्", "त् does not become श्."),
             ("तछरीरम्", "The त् becomes च् and the श becomes छ; the sound is च्छ.")],
            "As स्पृशेत् + शिरः = स्पृशेच्छिरः, तत् + शरीरम् = तच्छरीरम्.",
            "त् + श → च्छ.",
            teaches="A final त् before श becomes च्छ (स्पृशेच्छिरः; तच्छरीरम्)."),
    ],
}

NOTES_HI = {
    "92": "विश्वास: मध्यम। ‘प्रसिद्ध’ को ‘सजाया हुआ, व्यवस्थित’ लिया गया है; ‘जाना-माना, स्थापित’ भी संभव है, इसलिए उस पर प्रश्न नहीं। संधि जाँची: स्पृशेन्नाधरवाससा = स्पृशेत् + न + अधरवाससा (त् + न → न्न; न + अ → ना)। पहली पंक्ति का पूरा पद ‘परायणः’ तक एक ही समास है (सात अवयव)। कोई पाठभेद नहीं।",
    "93": "विश्वास: उच्च। ‘कुर्य्यात्’ केवल कुर्यात् की वर्तनी है। दूसरी पंक्ति की क्रिया ‘कुर्यात्’ पहली पंक्ति से ली गई है। संधि जाँची: नासंवृतमुखो = न + असंवृतमुखः (अ + अ → आ; अः + घोष → ओ); मिथुनीभूय = मिथुनी + भूय (cvi, ‘बनकर’)। ‘हास्य-क्षव-उद्गार-विजृंभण’ द्वन्द्व है।",
    "94": "विश्वास: मध्यम। ‘अग्निवारिणी’ को द्विवचन द्वन्द्व ‘अग्नि और जल’ माना गया है; सिर पर ढोने की बात इन पर लागू है या नहीं, श्लोक नहीं कहता। ‘युगपत्’ दूसरी पंक्ति में ‘अग्निवारिणी’ के साथ पढ़ा गया है। संधि जाँची: कंडूयेन्नात्मनः = कंडूयेत् + न + आत्मनः; वहेन्न = वहेत् + न; युगपच्चाग्निवारिणी = युगपत् + च + अग्निवारिणी।",
    "95": "विश्वास: कम (दोनों पंक्तियों में पाठ संदिग्ध)। पहली पंक्ति में ‘विषह्वयेत्’ अस्पष्ट है (संभवतः ‘विघट्टयेत्’, पर यह सुझाव है)। दूसरी पंक्ति में ‘कुर्य्यादिलेखन…’ में ‘इलेखन’ शब्द नहीं है, ‘विलेखन’ बैठता है; जैसा छपा है वैसा वाक्य आज्ञा बनता है, जो संदर्भ से मेल नहीं खाता, इसलिए निषेध माना गया है। ‘विकुष्णीयात्’ का ‘कुरेदना’ अर्थ अनुमान है। केवल साफ़ शब्दों पर प्रश्न हैं। संधि: दशनान्न = दशनान् + न।",
    "96": "विश्वास: मध्यम। ‘अकार्ये’ का अर्थ ‘बिना प्रयोजन’ लिया गया (‘अनावश्यक’ भी संभव)। ‘कंडूयेत्’ और ‘शौचयेत्’ का कर्म श्लोक में नहीं है; पैर पहले चरण से लिया गया। ‘आक्रामेत्’ = दबाए/रौंदे। संधि जाँची: नाकार्ये = न + अकार्ये; कार्येऽपि = कार्ये + अपि (अवग्रह); नाक्रामेन्नकंडूयेन्न = न + आक्रामेत् + न + कंडूयेत् + न।",
    "97": "विश्वास: मध्यम। पहली पंक्ति अनिश्चित: ‘तौ’ संभवतः पिछले श्लोक के दोनों पैर हैं (दूसरा द्विवचन भी संभव है); काँसे के पात्र की क्रिया लिखी नहीं है (‘रखे’ ऊपर से जोड़ा गया)। ‘मल-आशय’ = मल जमा होने के स्थान; श्लोक उन्हें नाम नहीं देता। संधि जाँची: नोपविष्टः = न + उपविष्टः (अ + उ → ओ); दध्यान्नखपाद… = दध्यात् + नख-पाद-मल-आशयान्।",
    "98": "विश्वास: मध्यम। ‘विवृत’ का अर्थ ‘अनावृत’ है, शरीर से खुला भी हो सकता है; श्लोक स्पष्ट नहीं करता। ‘हुताश’ = अग्नि (शाब्दिक: आहुति खाने वाला)। ‘उपासीत’ की क्रिया दूसरी पंक्ति में भी चलती है। संधि जाँची: नासमिद्धमुपासीत = न + असमिद्धम् + उपासीत; नैव = न + एव (अ + ए → ऐ); चाशुचिः = च + अशुचिः; नानुवातम् = न + अनुवातम्; नान्यमानसः = न + अन्यमानसः।",
    "99": "विश्वास: मध्यम। पहली पंक्ति पिछली इकाई की आग के बारे में है (‘उसे’ ऊपर से जोड़ा गया)। ‘स्कंदेत्’ के अर्थ (लाँघे / गिराए) में संदेह है; ‘अधः कुर्यात्’ और ‘न पादतः’ संक्षिप्त हैं, इसलिए उन पर प्रश्न नहीं। दूसरी पंक्ति नई सूची है जो इकाई १०२ तक चलती है। संधि जाँची: धमेन्नास्येन = धमेत् + न + आस्येन; चलसूक्ष्माप्रियाणि = चल + सूक्ष्म + अप्रियाणि (अ + अ → आ)।",
    "100": "विश्वास: कम। अंतिम शब्द ‘प्रतिभागतं’ संदिग्ध है (शायद ‘प्रतिबिम्बगत’, पर जैसा छपा है वैसा रखा गया); उस पर प्रश्न नहीं। उद्यन्तम्, अस्तम्, आयान्तम्, तपन्तम् के लिए संज्ञा इस इकाई में नहीं है; ये इकाई १०१ के ‘भास्वन्तम्’ से जुड़ते हैं, इसलिए १००–१०१ एक वाक्य हैं। क्रिया ‘न निरीक्षेत’ इकाई ९९ से। ‘अस्तम्’ यहाँ ‘अस्त होना’ (अस्त-स्थान) है। संधि: नाप्रशस्तम् = न + अप्रशस्तम्; उद्यन्तमस्तमायान्तम् = उद्यन्तम् + अस्तम् + आयान्तम्।",
    "101": "विश्वास: मध्यम। छपा ‘कुद्धस्य’ वर्तनी की भूल है, ‘क्रुद्धस्य’ (क्रोधित) पढ़ा गया। ‘भास्वन्तम्’ को सूर्य लिया गया (भास्वत् = चमकने वाला, सूर्य के लिए प्रचलित शब्द)। इकाई १०० के विशेषण इसी के साथ हैं। क्रिया ‘न निरीक्षेत’ इकाई ९९ से। संधि जाँची: नान्यदप्यतितेजस्वि = न + अन्यत् + अपि + अतितेजस्वि (त् → द् स्वर से पहले); गुरोर्मुखम् = गुरोः + मुखम्।",
    "102": "विश्वास: कम। दूसरी पंक्ति में ‘खमस्रुत’ अपठनीय है (संपादक ‘क्षुत’ = छींक सुझाते हैं, पर मात्राएँ मेल नहीं खातीं); उस पर प्रश्न नहीं। ‘स्रवन्ती’ ‘नदी’ भी हो सकती है, पर ‘स्त्रियम्’ के साथ स्त्री है। दूसरी पंक्ति का कर्ता-विषय पहली से अनुमानित है। क्रिया ‘न निरीक्षेत’ इकाई ९९ से। संधि जाँची: नोदक्याम् = न + उदक्याम्; नग्नां नान्यसंगताम् = नग्नाम् + न + अन्यसंगताम्।",
    "103": "विश्वास: कम। दूसरी पंक्ति दूषित है: ‘तामनीर्ण्यश्च’ संभवतः ‘तामनीर्ष्युश्च’ (ईर्ष्या-रहित), ‘स्वैरिणी’ संभवतः ‘स्वैरिणीम्’, और ‘नाशयेदहं’ का कोई सुरक्षित पाठ नहीं; इसलिए उस पंक्ति पर कोई प्रश्न नहीं। ‘तया’ संभवतः पिछली इकाई की स्त्री है (अनुमान)। संधि जाँची: नैकशयने = न + एकशयने; चाश्नीयात्तया = च + अश्नीयात् + तया।",
    "104": "विश्वास: मध्यम। छपा ‘तारकाराह…’ में ‘राह’ संभवतः ‘राहु’ है (संपादकों का सुझाव; अक्षर-संख्या वही रहती है), इसलिए राहु पर प्रश्न नहीं। ‘तुहिनांशु’ = चन्द्र, ‘दिवाकर’ = सूर्य। ‘उच्छिष्ट’ = जिसने खाया है और शुद्ध नहीं हुआ। यायात्, पठेत्, स्वप्यात् का कर्म नहीं है। संधि जाँची: नोच्छिष्टः = न + उच्छिष्टः; पश्येन्न = पश्येत् + न; स्पृशेच्छिरः = स्पृशेत् + शिरः (त् + श → च्छ)।",
}

AIDS = {
    "92": {
        "diagram": {"groups": [
            {"label": "परायणः (तत्पर)",
             "items": ["केश", "वाक्", "वेष", "शम", "सांत्व"]},
            {"label": "न छुए",
             "items": ["नाभि से ऊपर का शरीर", "निचले वस्त्र से"]}]},
        "chunks": "प्रसिद्धकेशवाग्वेषशमसांत्वपरायणः ‖ ऊर्ध्वं नाभेः शरीरस्य | स्पृशेन्नाधरवाससा।",
        "sandhi": "त् + न → न्न; न + अ → ना: स्पृशेत् + न + अधरवाससा → स्पृशेन्नाधरवाससा।",
        "anchors": "परायण = उसी में लगा · अधर = निचला · वासस् = वस्त्र · ऊर्ध्वम् = ऊपर, नाभेः = नाभि से।",
    },
    "93": {
        "diagram": {"groups": [
            {"label": "मैथुन के बाद न करे",
             "items": ["शौच में विलम्ब"]},
            {"label": "खुले मुँह से न करे",
             "items": ["हास्य", "क्षव", "उद्गार", "विजृंभण"]}]},
        "chunks": "न कुर्यान्मिथुनीभूय | शौचंप्रति विलंबनं ‖ नासंवृतमुखो | हास्यक्षवोद्गारविजृंभणं।",
        "sandhi": "न + अ → ना; अः + घोष → ओ: न + असंवृतमुखः + हास्य → नासंवृतमुखो हास्य। ‘मिथुनी + भूय’ = ‘बनकर’ रूप।",
        "frame": "पहली पंक्ति: मैथुन के बाद · शौच में विलम्ब नहीं · दूसरी पंक्ति: मुँह खुला हो तो · हँसना, छींकना, डकार, जम्हाई नहीं।",
    },
    "94": {
        "diagram": {"groups": [
            {"label": "तीन निषेध",
             "items": ["दोनों हाथों से एक साथ सिर खुजलाना",
                       "सिर पर बोझ ढोना",
                       "आग और पानी एक साथ ढोना"]}]},
        "chunks": "पाणिद्वयेन युगपत्कंडूयेन्नात्मनः शिरः ‖ वहेन्न भारं शिरसा | युगपच्चाग्निवारिणी।",
        "sandhi": "त् + न → न्न: वहेत् + न → वहेन्न; त् + च → च्च: युगपत् + च → युगपच्च।",
        "frame": "क्या न करे: सिर खुजलाना (दोनों हाथ, एक साथ) · सिर पर बोझ · आग-पानी एक साथ।",
    },
    "95": {
        "chunks": "नासिकां न विकुष्णीयाद् | दशनान्न (विषह्वयेत् अस्पष्ट) ‖ (कुर्य्यादिलेखन… संदिग्ध) छेद-भेद-आस्फोटन-मर्दनं।",
        "anchors": "नासिका = नाक · दशन = दाँत · छेद = काटना · भेद = फाड़ना · आस्फोटन = चटकाना · मर्दन = मलना।",
        "sandhi": "दशनान् + न → दशनान्न (न् के बाद न, कोई स्वर नहीं जुड़ता)।",
    },
    "96": {
        "seesaw": "अकार्य ↔ कार्य: बिना प्रयोजन भी नहीं, और प्रयोजन होने पर भी नहीं (‘न … न च … अपि’)।",
        "chunks": "नाकार्ये न च कार्येऽपि | मुखांगनखवादनं ‖ पादं पादेन नाक्रामेन् | नकंडूयेन्न शौचयेत्।",
        "sandhi": "न + अ → ना: न + अकार्ये → नाकार्ये। कार्ये + अपि → कार्येऽपि (अवग्रह)।",
        "frame": "पहली पंक्ति: मुँह, अंग, नख से आवाज़ — काम हो या न हो, नहीं · दूसरी पंक्ति: पैर से पैर — दबाना, खुजलाना, साफ़ करना नहीं।",
    },
    "97": {
        "chunks": "(पहली पंक्ति अनिश्चित: न कांस्यभाजने तौ च नोपविष्टः प्रसारयेत्) ‖ अभीक्ष्णं निर्मलान् दध्यान् | नखपादमलाशयान्।",
        "sandhi": "अ + उ → ओ: न + उपविष्टः → नोपविष्टः। दध्यात् + नख → दध्यान्नख।",
        "frame": "क्या: बार-बार निर्मल रखे · किन्हें: नख, पाद, मलाशय।",
    },
    "98": {
        "diagram": {"groups": [
            {"label": "इनमें अग्नि की उपासना न करे",
             "items": ["असमिद्ध", "अशुचि", "अनुवात", "विवृत", "क्लान्त", "अन्यमानस"]}]},
        "chunks": "नासमिद्धमुपासीत | हुताशं नैव चाशुचिः ‖ नानुवातं न विवृतो | न क्लांतो नान्यमानसः।",
        "sandhi": "अ + ए → ऐ: न + एव → नैव। न + अ → ना: न + अन्यमानसः → नान्यमानसः।",
        "contrast": "समिद्ध (जलाई हुई) ↔ असमिद्ध (बिना जलाई): श्लोक असमिद्ध अग्नि की उपासना मना करता है।",
    },
    "99": {
        "diagram": {"groups": [
            {"label": "लगातार न देखे",
             "items": ["चल", "सूक्ष्म", "अप्रिय"]}]},
        "chunks": "धमेन्नास्येन (…अगले चरण संक्षिप्त) ‖ सततं न निरीक्षेत | चलसूक्ष्माप्रियाणि च।",
        "sandhi": "अ + अ → आ: सूक्ष्म + अप्रियाणि → सूक्ष्माप्रियाणि। धमेत् + न + आस्येन → धमेन्नास्येन।",
        "frame": "पहली पंक्ति: आग मुँह से नहीं · दूसरी पंक्ति: नई सूची — लगातार न देखे: चल, सूक्ष्म, अप्रिय।",
    },
    "100": {
        "chunks": "नाप्रशस्तं न विण्मूत्रं | न दर्पणममार्जितं ‖ उद्यंतमस्तमायांतं | तपंतं (प्रतिभागतं संदिग्ध)।",
        "frame": "पहली पंक्ति: न देखे — अप्रशस्त, मल-मूत्र, बिना पोंछा दर्पण · दूसरी पंक्ति: उगता, अस्त की ओर, तपता — संज्ञा इकाई १०१ में।",
        "anchors": "अप्रशस्त = अशुभ · विण्मूत्र = मल और मूत्र · अमार्जित = बिना पोंछा · उद्यन्तम् = उगता हुआ · तपन्तम् = तपता हुआ।",
    },
    "101": {
        "diagram": {"groups": [
            {"label": "भास्वन्तम्",
             "items": ["उपरक्त (ग्रस्त)", "वाससा तिरोहित (ढका)"]},
            {"label": "और भी न देखे",
             "items": ["कोई अन्य अतितेजस्वि", "क्रुद्ध गुरु का मुख"]}]},
        "chunks": "उपरक्तं च भास्वंतं | वाससा वा तिरोहितं ‖ नान्यदप्यतितेजस्वि | न क्रुद्धस्य गुरोर्मुखं।",
        "sandhi": "त् + स्वर → द्: अन्यत् + अपि → अन्यदपि। न + अ → ना: न + अन्यत् → नान्यत्।",
        "frame": "पिछली इकाई के विशेषण भास्वन्तम् के साथ · ग्रहण या वस्त्र से ढका · कोई भी अति तेज · क्रोधित गुरु का मुख।",
    },
    "102": {
        "chunks": "स्त्रियं स्रवंतीं नोदक्यां | न नग्नां नान्यसंगतां ‖ न पानभोजन (खमस्रुत अस्पष्ट) | जृंभासुखासने।",
        "sandhi": "न + उ → नो: न + उदक्याम् → नोदक्याम्। न + अ → ना: न + अन्यसंगताम् → नान्यसंगताम्।",
        "anchors": "स्रवन्ती = बहती/स्रावयुक्त · उदक्या = रजस्वला · नग्ना = नग्न · अन्यसंगता = दूसरे के साथ संगत।",
    },
    "103": {
        "chunks": "शयीत नैकशयने | न चाश्नीयात्तया सह ‖ (दूसरी पंक्ति दूषित: तामनीर्ण्यश्च … नाशयेदहं)",
        "sandhi": "न + ए → नै: न + एकशयने → नैकशयने। अश्नीयात् + तया → अश्नीयात्तया।",
        "frame": "पहली पंक्ति: उसके साथ — एक शय्या पर सोना नहीं, साथ भोजन नहीं · दूसरी पंक्ति: बिगड़ी, उपयोग नहीं।",
    },
    "104": {
        "diagram": {"groups": [
            {"label": "उच्छिष्ट रहते न देखे",
             "items": ["तारका", "राह (राहु?)", "तुहिनांशु", "दिवाकर"]},
            {"label": "और न करे",
             "items": ["जाना", "पढ़ना", "सोना", "सिर छूना"]}]},
        "chunks": "नोच्छिष्टस्तारकाराहतुहिनांशुदिवाकरान् ‖ पश्येन्न यायान्न पठेन् | न स्वप्यान्न स्पृशेच्छिरः।",
        "sandhi": "त् + श → च्छ: स्पृशेत् + शिरः → स्पृशेच्छिरः। न + उ → नो: न + उच्छिष्टः → नोच्छिष्टः।",
        "anchors": "तुहिनांशु = ठंडी किरणों वाला (चन्द्र) · दिवाकर = दिन करने वाला (सूर्य) · उच्छिष्ट = खाकर अशुद्ध।",
    },
}

IMAGE_SPECS = {
    ("92", "diagram"): {
        "file": "ch3b08-devoted-92.svg",
        "alt": "Mind map: devoted to five things: hair, speech, dress, calm, conciliation",
        "type": "mermaid",
        "code": 'mindmap\n  परायण\n    केश\n    वाक्\n    वेष\n    शम\n    सांत्व\n',
    },
    ("93", "diagram"): {
        "file": "ch3b08-two-nots-93.svg",
        "alt": "Two columns: after intercourse, no delay in cleansing; with the mouth uncovered, no laughing, sneezing, belching, yawning",
        "type": "split",
        "title": "श्लोक ९३: दो निषेध",
        "cols": [["मैथुन के बाद", ["शौच में विलम्ब नहीं"]],
                 ["खुले मुँह से नहीं", ["हास्य", "क्षव", "उद्गार", "विजृंभण"]]],
    },
    ("94", "diagram"): {
        "file": "ch3b08-three-nots-94.svg",
        "alt": "Mind map: three prohibitions: scratching the head with both hands at once, a load on the head, fire and water together",
        "type": "mermaid",
        "code": ('mindmap\n  तीन निषेध\n    दोनों हाथों से एक साथ सिर खुजलाना\n'
                 '    सिर पर बोझ\n    आग और पानी एक साथ\n'),
    },
    ("98", "diagram"): {
        "file": "ch3b08-fire-conditions-98.svg",
        "alt": "Mind map: six conditions in which the fire is not tended: unkindled, unclean, along the wind, uncovered, weary, mind elsewhere",
        "type": "mermaid",
        "code": ('mindmap\n  अग्नि की उपासना न करे\n    असमिद्ध\n    अशुचि\n    अनुवात\n'
                 '    विवृत\n    क्लान्त\n    अन्यमानस\n'),
    },
    ("99", "diagram"): {
        "file": "ch3b08-not-gaze-99.svg",
        "alt": "Mind map: not to be gazed at constantly: moving, minute, unpleasant things",
        "type": "mermaid",
        "code": 'mindmap\n  लगातार न देखे\n    चल\n    सूक्ष्म\n    अप्रिय\n',
    },
    ("101", "diagram"): {
        "file": "ch3b08-not-gaze-101.svg",
        "alt": "Two columns: the shining one eclipsed or covered by a cloth; and anything else too bright, the angry teacher's face",
        "type": "split",
        "title": "श्लोक १०१: न देखे",
        "cols": [["भास्वन्तम्", ["उपरक्त (ग्रस्त)", "वस्त्र से ढका"]],
                 ["और भी", ["अन्य अतितेजस्वि", "क्रुद्ध गुरु का मुख"]]],
    },
    ("104", "diagram"): {
        "file": "ch3b08-ucchishta-104.svg",
        "alt": "Two columns: while ucchishta do not look at the stars, the printed 'raha' (probably Rahu), the moon, the sun; do not go, recite, sleep, touch the head",
        "type": "split",
        "title": "श्लोक १०४: उच्छिष्ट रहते",
        "cols": [["न देखे", ["तारका", "राह (राहु?)", "तुहिनांशु", "दिवाकर"]],
                 ["न करे", ["जाना", "पढ़ना", "सोना", "सिर छूना"]]],
    },
}
