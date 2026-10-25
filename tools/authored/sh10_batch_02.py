from helpers import mcq, match, order, fill, multi, accepts


AUTHORED = {}

# ---------------------------------------------------------------- unit 13
AUTHORED["13"] = {
    "title": "यो वाऽल्पाशी कफेनार्तो",
    "question": "By unit 13, which signs of eating, Kapha and breathing does the verse list?",
    "rule": ("Or (वा) who, eating little (अल्पाशी) and afflicted by Kapha (कफेनार्तः), breathes long (दीर्घं श्वसिति) "
             "and stirs (चेष्टते); who, having breathed out short (ह्रस्वं निश्वस्य), becomes exhausted (परिताम्यति)."),
    "limits": ("Printed उच्छ्रस्य is no verb form; उच्छ्वस्य (having breathed in) is the data's probable reading: no "
               "question rests on it. Whether चेष्टते goes with दीर्घम् ('breathes long when he exerts himself') is open; "
               "the plain list reading is taken and no question chooses. The verse lists signs only."),
    "explain_hi": ("यह श्लोक दो छपी पंक्तियों (०२.१०.२४ और ०२.१०.२५) से बना है और ‘यो वा’ (अथवा जो) से लक्षणों की सूची में आगे जोड़ता है। "
                   "जो थोड़ा खाने वाला (अल्पाशी) और कफ से पीड़ित (कफेनार्तः) है, लम्बी साँस लेता है और चेष्टा करता है (दीर्घं श्वसिति चेष्टते)। "
                   "दूसरी पंक्ति: जो लम्बी साँस भीतर लेकर और छोटी साँस बाहर छोड़कर (ह्रस्वं निश्वस्य) थक जाता है (परिताम्यति)। "
                   "छपा ‘उच्छ्रस्य’ कोई क्रिया-रूप नहीं; ‘उच्छ्वस्य’ (साँस भीतर लेकर) डेटा का सम्भावित पाठ है। "
                   "‘चेष्टते’ को ‘दीर्घम्’ के साथ पढ़ें तो ‘परिश्रम करने पर लम्बी साँस’ अर्थ भी हो सकता है; डेटा सीधी सूची वाला अर्थ लेता है।"),
    "hook": "थोड़ा खाना, कफ की पीड़ा, लम्बी साँस; छोटी साँस छोड़कर थकान।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "In unit 13, what does अल्पाशी mean?",
            ("Eating little", "अल्प (little) + आशिन् (eating): अल्पाशी, one who eats little."),
            [("Eating much", "Eating much is बह्वाशी; अल्प means little."),
             ("Eating nothing", "अल्प means little, not nothing at all."),
             ("Eating at night", "No time of eating is named; अल्प means little.")],
            "अल्प = little, आशिन् = eating.",
            "अल्पाशी = eating little."),
        order(1, "Put the words of line 1 of unit 13 in the printed order.",
              ["यो वाऽल्पाशी", "कफेनार्तो", "दीर्घं", "श्वसिति", "चेष्टते"],
              "Or who, eating little; afflicted by Kapha; long; breathes; stirs.",
              "यो वाऽल्पाशी → कफेनार्तो → दीर्घं → श्वसिति → चेष्टते."),
        match(2, "Match each word of unit 13 to its meaning.",
              [["अल्प", "little"], ["आशिन्", "eating"], ["आर्त", "afflicted"], ["दीर्घ", "long"],
               ["ह्रस्व", "short"], ["परिताम्यति", "becomes exhausted"]],
              "अल्प = little, आशिन् = eating, आर्त = afflicted, दीर्घ = long, ह्रस्व = short, परिताम्यति = becomes exhausted.",
              "अल्प, आशिन्, आर्त, दीर्घ, ह्रस्व, परिताम्यति.", role="extend",
              teaches="-आशिन् at the end of a compound means 'eating'; अल्पाशी is its nominative singular: one who eats little."),
        mcq("discriminate", 3, "Which split of कफेनार्तो in unit 13 is right?",
            ("कफेन + आर्तः", "अ + आ → आ: कफेन + आर्तः → कफेनार्तः; then अः before the voiced द → ओ."),
            [("कफेन् + आर्तः", "कफेन् is no form; the instrumental is कफेन, ending in अ."),
             ("कफेना + आर्तः", "कफेना is no form; the instrumental of कफ is कफेन."),
             ("कफेन + ऋतः", "अ + ऋ gives अर्, not आर्: it would be कफेनर्तः.")],
            "कफेन (by Kapha) + आर्तः (afflicted): अ + आ → आ.",
            "अ + आ → आ."),
        mcq("apply", 4, "Why is आर्तः printed आर्तो before दीर्घं in unit 13?",
            ("अः before a voiced consonant → ओ", "द is a voiced consonant: आर्तः + दीर्घं → आर्तो दीर्घं (also यः + वा → यो वा)."),
            [("आः before a voiced consonant → ओ", "आः drops its visarga before a voiced sound; here the vowel is short अ."),
             ("Visarga before any consonant → ओ", "Not any: before a voiceless त the visarga becomes स्."),
             ("ओ is the participle's own ending", "The nominative is आर्तः; ओ comes only from sandhi.")],
            "आर्तः + दीर्घं: अः before the voiced consonant द → ओ.",
            "अः + voiced consonant → ओ."),
        mcq("transfer", 5, "By the pattern of अल्पाशी (eating little), what does फलाशी mean in a new example?",
            ("One who eats fruit", "फल (fruit) + आशिन् (eating): one who eats fruit, like अल्पाशी."),
            [("One who sells fruit", "-आशिन् means eating, not selling."),
             ("Fruit that is eaten", "-आशी names the eater, not the thing eaten."),
             ("One who grows fruit", "-आशिन् means eating, not growing.")],
            "फलाशी = fruit-eater, as अल्पाशी = one who eats little.",
            "-आशिन् = eating (the eater).",
            teaches="-आशिन् after a word names the one who eats: अल्पाशी (eats little), फलाशी (eats fruit)."),
    ],
}

# ---------------------------------------------------------------- unit 14
AUTHORED["14"] = {
    "title": "ह्रस्वं च यः प्रश्वसिति",
    "question": "By unit 14, which signs of breath and movement are sure, and which part is damaged?",
    "rule": ("And who breathes short (ह्रस्वं प्रश्वसिति) and throbs violently (स्पंदते भृशम्), jerked about "
             "(व्याविद्धम्); who, on a conjectural reading, tosses his head (शिरो विक्षिपते). The rest of line 2 is damaged in print."),
    "limits": ("Low confidence. अचयित्वा प्रपाणिकौ give no sense and are kept as printed; कृच्छ्रात् (with difficulty) for "
               "printed कृच्छ्रा- is probable, not sure. In line 2 only the words शिरः and विक्षिपते are asked. "
               "व्याविद्धम् may also mean 'with a pierced feeling': no question rests on it."),
    "explain_hi": ("यह श्लोक दो छपी पंक्तियों (०२.१०.२६ और ०२.१०.२७) से बना है; विश्वास कम है। "
                   "पहली पंक्ति पक्की है: और जो छोटी साँस लेता है (ह्रस्वं च यः प्रश्वसिति) और झटके खाता हुआ (व्याविद्धम्) अत्यन्त (भृशम्) फड़कता है (स्पंदते)। "
                   "दूसरी पंक्ति में ‘शिरो विक्षिपते’ (सिर को इधर-उधर फेंकता है) पढ़ा जा सकता है; ‘कृच्छ्रात्’ (कठिनाई से) सम्भावित सुधार है। "
                   "‘अचयित्वा प्रपाणिकौ’ छपाई में टूटे और अस्पष्ट हैं, इसलिए इन पर कोई प्रश्न नहीं। "
                   "‘व्याविद्धम्’ क्रियाविशेषण की तरह लिया गया है (झटके से); ‘चुभन के अनुभव के साथ’ अर्थ भी सम्भव है।"),
    "hook": "छोटी साँस, ज़ोर की फड़कन, सिर इधर-उधर; आगे का पाठ टूटा।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "In unit 14, what does भृशम् mean?",
            ("Violently, greatly", "भृशम् = violently, greatly: स्पंदते भृशम्, throbs violently."),
            [("Slowly, gently", "That is the opposite of भृशम्."),
             ("Rarely, at times", "भृशम् gives the degree, not how often."),
             ("Silently, unseen", "भृशम् gives the degree: violently.")],
            "भृशम् = violently, greatly (an adverb).",
            "भृशम् = violently."),
        order(1, "Put the words of line 1 of unit 14 in the printed order.",
              ["ह्रस्वं च", "यः प्रश्वसिति", "व्याविद्धं", "स्पंदते", "भृशं"],
              "And short; who breathes; jerked about; throbs; violently.",
              "ह्रस्वं च → यः प्रश्वसिति → व्याविद्धं → स्पंदते → भृशं."),
        match(2, "Match each word of unit 14 to its meaning.",
              [["ह्रस्व", "short"], ["प्रश्वसिति", "breathes"], ["स्पन्दते", "throbs, quivers"],
               ["भृश", "violent, great"], ["शिरः", "head"], ["विक्षिपते", "tosses about"]],
              "ह्रस्व = short, प्रश्वसिति = breathes, स्पन्दते = throbs, भृश = violent, शिरः = head, विक्षिपते = tosses about.",
              "ह्रस्व, प्रश्वसिति, स्पन्दते, भृश, शिरः, विक्षिपते.", role="extend",
              teaches="स्पन्दते and विक्षिपते are ātmanepada presents in -ते: 'throbs', 'tosses about'."),
        multi("discriminate", 3, "Which signs does line 1 of unit 14 state?",
              [("He breathes short", "Yes: ह्रस्वं च यः प्रश्वसिति."),
               ("His feet grow cold", "No: line 1 says nothing of the feet or of cold."),
               ("He throbs violently", "Yes: व्याविद्धं स्पंदते भृशम्."),
               ("He sleeps all day", "No: line 1 says nothing of sleep.")],
              [0, 2],
              "Line 1: short breathing and violent, jerking throbbing.",
              "ह्रस्वं प्रश्वसिति; स्पंदते भृशम्."),
        mcq("apply", 4, "Why is शिरः printed शिरो before विक्षिपते in unit 14?",
            ("अः before the voiced व → ओ", "व is a voiced consonant: शिरः + विक्षिपते → शिरो विक्षिपते."),
            [("अः before every consonant → ओ", "Not every: before a voiceless त the visarga becomes स्."),
             ("ओ is the noun's own final", "The stem is शिरस्, nominative-accusative शिरः; ओ comes from sandhi."),
             ("आः before a voiced sound → ओ", "शिरः has short अ; आः would drop its visarga.")],
            "शिरः + विक्षिपते: अः before the voiced consonant व → ओ.",
            "अः + voiced consonant → ओ."),
        mcq("transfer", 5, "By the pattern of स्पंदते भृशम् (throbs violently), what does बालो भृशं रोदिति mean in a new example?",
            ("The child weeps violently", "भृशम् used as an adverb: weeps violently, greatly."),
            [("The child weeps softly", "Softly is the opposite of भृशम्."),
             ("The child weeps rarely", "भृशम् gives the degree, not how often."),
             ("The child stops weeping", "रोदिति means weeps; nothing says he stops.")],
            "भृशं रोदिति = weeps violently, as स्पंदते भृशम् = throbs violently.",
            "भृशम् = violently (adverb).",
            teaches="A neuter accusative such as भृशम् is often used as an adverb: 'violently, greatly'."),
    ],
}

# ---------------------------------------------------------------- unit 15
AUTHORED["15"] = {
    "title": "यो ललाटस्रुतस्वेदः",
    "question": "By unit 15, which signs of sweat, slack joinings and bewilderment does the verse list?",
    "rule": ("Who has sweat trickling from the forehead (ललाटस्रुतस्वेदः), whose joinings and bindings are slack "
             "(श्लथसंधानबंधनः); who, when being raised up, would become bewildered (उत्थाप्यमानः संमुह्येत्), whether "
             "strong or even weak (बली दुर्बलोऽपि वा)."),
    "limits": ("संधान-बंधन = joinings and bindings, probably the joints and what binds them; no closer anatomical term "
               "is given. संमुह्येत् = become bewildered, probably faint: both are possible, so no question chooses. "
               "The verse names no cause and no time."),
    "explain_hi": ("यह श्लोक दो छपी पंक्तियों (०२.१०.२८ और ०२.१०.२९) से बना है और लक्षणों की सूची आगे बढ़ाता है। "
                   "जिसके माथे से पसीना बहता हो (ललाटस्रुतस्वेदः) और जिसके संधान और बन्धन ढीले हों (श्लथसंधानबंधनः); डेटा के अनुसार सम्भवतः जोड़ और उन्हें बाँधने वाले भाग। "
                   "जो उठाए जाने पर (उत्थाप्यमानः) मोहग्रस्त हो जाए (संमुह्येत्), सम्भवतः मूर्च्छित; दोनों अर्थ सम्भव हैं। "
                   "‘बली दुर्बलोऽपि वा’: चाहे बलवान हो या दुर्बल भी, यानी बल कैसा भी हो। "
                   "‘दुर्बलोऽपि’ में दुर्बलः + अपि है: अः + अ → ओ, और अ का लोप ऽ से दिखाया गया।"),
    "hook": "माथे पर पसीना, ढीले बन्धन, उठाने पर मोह: बली हो या दुर्बल।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "In unit 15, what does स्वेद mean?",
            ("Sweat", "स्वेद = sweat: ललाट-स्रुत-स्वेदः, sweat trickled from the forehead."),
            [("Tears", "Tears would be अश्रु; स्वेद is sweat."),
             ("Blood", "Blood would be रक्त; स्वेद is sweat."),
             ("Saliva", "Saliva would be लाला; स्वेद is sweat.")],
            "स्वेद = sweat.",
            "स्वेद = sweat."),
        order(1, "Put these parts of unit 15 in the printed order.",
              ["ललाटस्रुतस्वेदः", "श्लथसंधानबंधनः", "उत्थाप्यमानः", "संमुह्येद्यो", "बली दुर्बलोऽपि वा"],
              "Sweat trickling from the forehead; slack joinings and bindings; being raised up; would become bewildered, who; strong or even weak.",
              "ललाटस्रुतस्वेदः → श्लथसंधानबंधनः → उत्थाप्यमानः → संमुह्येद्यो → बली दुर्बलोऽपि वा."),
        match(2, "Match each word of unit 15 to its meaning.",
              [["ललाट", "forehead"], ["स्रुत", "trickled, flowed"], ["स्वेद", "sweat"], ["श्लथ", "slack, loose"],
               ["उत्थाप्यमान", "being raised up"]],
              "ललाट = forehead, स्रुत = trickled, स्वेद = sweat, श्लथ = slack, उत्थाप्यमान = being raised up.",
              "ललाट, स्रुत, स्वेद, श्लथ, उत्थाप्यमान.", role="extend",
              teaches="ललाटस्रुतस्वेदः is a bahuvrīhi: 'one whose sweat has trickled from the forehead'."),
        mcq("discriminate", 3, "Which split of दुर्बलोऽपि in unit 15 is right?",
            ("दुर्बलः + अपि", "अः + अ → ओ, and the अ of अपि is dropped (ऽ): दुर्बलोऽपि."),
            [("दुर्बल + ओपि", "ओपि is no word; the ओ comes from the visarga of दुर्बलः."),
             ("दुर्बलो + पि", "पि is no word; ऽ marks the dropped अ of अपि."),
             ("दुर्बला + अपि", "आ + अ → आ would give दुर्बलापि.")],
            "दुर्बलः (weak) + अपि (even): अः + अ → ओऽ.",
            "अः + अ → ओऽ."),
        mcq("apply", 4, "By unit 15, for whom does the sign of bewilderment on being raised up hold?",
            ("Strong or even weak alike", "बली दुर्बलोऽपि वा: whether strong or even weak."),
            [("The weak, but never the strong", "The verse names बली (strong) as well."),
             ("The strong, but never the weak", "The verse names दुर्बल (weak) as well."),
             ("Only those who are aged", "No age is named in unit 15.")],
            "बली दुर्बलोऽपि वा: whatever his strength.",
            "बली दुर्बलोऽपि वा = strong or even weak."),
        mcq("transfer", 5, "By the pattern of दुर्बलः + अपि → दुर्बलोऽपि, how is नरः + अपि (the man too) joined in a new example?",
            ("नरोऽपि", "अः + अ → ओ, and the अ is dropped (ऽ): नरोऽपि."),
            [("नरापि", "अः + अ gives ओऽ, not आ."),
             ("नररपि", "र् comes from a visarga after a vowel other than अ/आ; here it is अ."),
             ("नरसपि", "स् comes from a visarga before त or थ, not before a vowel.")],
            "नरः + अपि = नरोऽपि, like दुर्बलः + अपि = दुर्बलोऽपि.",
            "अः + अ → ओऽ.",
            teaches="A final अः before अ becomes ओ and the अ is dropped, marked ऽ: दुर्बलः + अपि → दुर्बलोऽपि."),
    ],
}

# ---------------------------------------------------------------- unit 16
AUTHORED["16"] = {
    "title": "उत्तानएव स्वपिति",
    "question": "By unit 16, which signs of lying, of the feet and of grasping does the verse list?",
    "rule": ("Who sleeps only on his back (उत्तानः एव स्वपिति) and distorts his two feet (पादौ विकरोति); who tries to "
             "grasp only what is non-existent (असत् एव जिघृक्षति) on bed, seat, wall and so on (शयनासनकुड्यादौ)."),
    "limits": ("विकरोति = distorts, alters (another sense: moves them irregularly): no question chooses. The verse says "
               "only 'what is not there', nothing more about it. The print leaves उत्तानएव unjoined (regular: उत्तान एव)."),
    "explain_hi": ("यह श्लोक दो छपी पंक्तियों (०२.१०.३० और ०२.१०.३१) से बना है। "
                   "जो केवल चित लेटकर (उत्तानः एव) सोता है और दोनों पैरों को विकृत करता है (पादौ विकरोति); ‘विकरोति’ का अर्थ अनियमित हिलाना भी हो सकता है। "
                   "जो शय्या, आसन, दीवार आदि पर अविद्यमान वस्तु को ही (असत् एव) पकड़ना चाहता है (जिघृक्षति)। "
                   "‘जिघृक्षति’ √ग्रह् का सन्नन्त (इच्छार्थक) रूप है: पकड़ना चाहता है। "
                   "छपाई में ‘उत्तानएव’ बिना सन्धि के जुड़ा है; नियमित रूप ‘उत्तान एव’ है।"),
    "hook": "चित सोना, पैर विकृत, शय्या-दीवार पर जो नहीं है उसे पकड़ना।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "In unit 16, what does उत्तान mean?",
            ("Lying face up, on the back", "उत्तान = face up, on the back: उत्तान एव स्वपिति."),
            [("Lying face down, on the belly", "That is the opposite of उत्तान."),
             ("Lying on one side only", "उत्तान is face up, not on the side."),
             ("Sitting bolt upright", "उत्तान is lying face up, and the verb is स्वपिति, sleeps.")],
            "उत्तान = face up.",
            "उत्तान = on the back."),
        order(1, "Put these parts of unit 16 in the printed order.",
              ["उत्तानएव स्वपिति", "पादौ विकरोति च", "शयनासनकुड्यादौ", "योऽसदेव जिघृक्षति"],
              "Sleeps only face up; and distorts both feet; on bed, seat, wall and so on; who tries to grasp only what is not there.",
              "उत्तानएव स्वपिति → पादौ विकरोति च → शयनासनकुड्यादौ → योऽसदेव जिघृक्षति."),
        match(2, "Match each word of unit 16 to its meaning.",
              [["स्वपिति", "sleeps"], ["पादौ", "both feet"], ["शयन", "bed"], ["आसन", "seat"],
               ["कुड्य", "wall"], ["जिघृक्षति", "wishes to grasp"]],
              "स्वपिति = sleeps, पादौ = both feet, शयन = bed, आसन = seat, कुड्य = wall, जिघृक्षति = wishes to grasp.",
              "स्वपिति, पादौ, शयन, आसन, कुड्य, जिघृक्षति.", role="extend",
              teaches="-आदौ after a list means 'in the group beginning with': शयनासनकुड्यादौ = on bed, seat, wall and so on."),
        mcq("discriminate", 3, "Which split of योऽसदेव in unit 16 is right?",
            ("यः + असत् + एव", "अः + अ → ओऽ; त् before the vowel ए → द्: योऽसदेव."),
            [("यः + असत् + इव", "त् + इ would give दि (असदिव); the print has दे."),
             ("यः + असत + एव", "अ + ए would give ऐ (असतैव); the print has दे."),
             ("यः + असदे + व", "असदे and व are no words here; एव (only) follows असत्.")],
            "यः (who) + असत् (what is not) + एव (only).",
            "अः + अ → ओऽ; त् + vowel → द्."),
        mcq("apply", 4, "In regular sandhi, how is उत्तानः + एव written (the print has उत्तानएव)?",
            ("उत्तान एव", "अः before a vowel other than अ → अ, and the gap stays: उत्तान एव."),
            [("उत्तानो एव", "ओ comes before a voiced consonant or before अ, not before ए."),
             ("उत्तानैव", "After the visarga is lost, the two vowels do not merge again."),
             ("उत्तानर् एव", "र् comes after a vowel other than अ/आ; here it is अ.")],
            "उत्तानः + एव → उत्तान एव (gap kept).",
            "अः + vowel other than अ → अ (with a gap)."),
        mcq("transfer", 5, "By the pattern of जिघृक्षति (wishes to grasp, desiderative of √ग्रह्), what does पिपासति (desiderative of √पा, drink) mean in a new example?",
            ("Wishes to drink", "A desiderative means 'wishes to do': पिपासति = wishes to drink."),
            [("Is drinking now", "Is drinking would be the present पिबति."),
             ("Makes another drink", "Making another drink is the causative पाययति."),
             ("Has finished drinking", "A desiderative states a wish, not a finished act.")],
            "पिपासति = wishes to drink, as जिघृक्षति = wishes to grasp.",
            "Desiderative = 'wishes to'.",
            teaches="A desiderative (reduplication + -स-) means 'wishes to do': √ग्रह् → जिघृक्षति, √पा → पिपासति."),
    ],
}

# ---------------------------------------------------------------- unit 17
AUTHORED["17"] = {
    "title": "अहास्यहासी संमुह्यन्",
    "question": "By unit 17, which signs of laughter, of the lips and of belching does the verse list?",
    "rule": ("Who laughs at what is not laughable (अहास्यहासी), growing bewildered (संमुह्यन्), and licks his two lips "
             "(लेढि दशनच्छदौ); who, on a conjectural reading, licks around the upper lip (उत्तरोष्ठम्) and makes "
             "belches (उद्गारान् करोति)."),
    "limits": ("Printed पेरिलेहन्ति is plural and does not fit the singular यः; परिलेहति is a possible emendation: no "
               "question on that verb. अहास्यहासी may also be 'one who laughs without cause'. The verse lists signs only."),
    "explain_hi": ("यह श्लोक दो छपी पंक्तियों (०२.१०.३२ और ०२.१०.३३) से बना है। "
                   "जो न हँसने योग्य बात पर हँसता है (अहास्यहासी), मोहग्रस्त होता हुआ (संमुह्यन्), और दोनों दशनच्छदों यानी ओठों को चाटता है (लेढि दशनच्छदौ)। "
                   "दूसरी पंक्ति, अनुमानित पाठ पर: जो ऊपरी ओठ (उत्तरोष्ठम्) के चारों ओर चाटता है और डकारें करता है (उद्गारान् करोति)। "
                   "छपा ‘पेरिलेहन्ति’ बहुवचन है, जो एकवचन ‘यः’ से मेल नहीं खाता; ‘परिलेहति’ सम्भव सुधार है। "
                   "‘दशनच्छद’ का शब्दार्थ है ‘दाँतों का ढक्कन’, यानी ओठ (मानक)।"),
    "hook": "बेबात हँसी, ओठ चाटना, डकारें।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "In unit 17, what does दशनच्छद (literally 'tooth-cover') name?",
            ("The lip", "दशनच्छद = tooth-cover, the lip (standard)."),
            [("The tongue", "The tongue is जिह्वा; it does not cover the teeth."),
             ("The nostril", "The nostril is नासापुट; दशनच्छद is the lip."),
             ("The eyelid", "The eyelid is वर्त्म; दशनच्छद is the lip.")],
            "दशन (tooth) + छद (cover) = the lip.",
            "दशनच्छद = lip."),
        order(1, "Put the words of line 1 of unit 17 in the printed order.",
              ["अहास्यहासी", "संमुह्यन्", "यो लेढि", "दशनच्छदौ"],
              "Laughing at what is not laughable; growing bewildered; who licks; the two lips.",
              "अहास्यहासी → संमुह्यन् → यो लेढि → दशनच्छदौ."),
        match(2, "Match each word of unit 17 to its meaning.",
              [["हास्य", "to be laughed at"], ["हासिन्", "laughing"], ["लेढि", "licks"], ["दशन", "tooth"],
               ["उत्तरोष्ठ", "upper lip"], ["उद्गार", "belch"]],
              "हास्य = to be laughed at, हासिन् = laughing, लेढि = licks, दशन = tooth, उत्तरोष्ठ = upper lip, उद्गार = belch.",
              "हास्य, हासिन्, लेढि, दशन, उत्तरोष्ठ, उद्गार.", role="extend",
              teaches="अ- before हास्य negates it: अहास्य = not to be laughed at; अहास्यहासी = one who laughs at such things."),
        mcq("discriminate", 3, "Which rendering of अहास्यहासी संमुह्यन् यो लेढि दशनच्छदौ (unit 17) is right?",
            ("Bewildered, laughs at the unlaughable and licks his lips",
             "हासी = laughing, लेढि = licks, दशनच्छदौ = the two lips."),
            [("Bewildered, laughs at the unlaughable and bites his lips",
              "लेढि is from √लिह्, licks, not bites."),
             ("Bewildered, weeps at the unlaughable and licks his lips",
              "हासी is from √हस्, laughing, not weeping."),
             ("Bewildered, laughs at the unlaughable and licks his teeth",
              "दशनच्छद is the tooth-cover, the lip, not the teeth.")],
            "Each wrong rendering changes one word: bites, weeps, teeth.",
            "लेढि = licks; हासी = laughing; दशनच्छद = lip."),
        mcq("apply", 4, "By unit 17, at what does the man laugh?",
            ("At what is not laughable", "अहास्यहासी: one who laughs at what is not to be laughed at."),
            [("At what is truly funny", "हास्य is what is laughable; the अ- says the opposite."),
             ("He does not laugh at all", "हासी says he does laugh."),
             ("Only at his own sorrow", "No sorrow is named; the object is अहास्य.")],
            "अ-हास्य-हासी = laughing at the not-laughable.",
            "अहास्यहासी = laughs at what is not laughable."),
        mcq("transfer", 5, "By the pattern of उद्गारान् + च → उद्गारांश्च, how is नरान् + च (and the men, acc.) joined in a new example?",
            ("नरांश्च", "Final न् before च becomes anusvāra + श्: नरांश्च."),
            [("नरांस्च", "स् arises before त or थ, not before च."),
             ("नरोंश्च", "The vowel आ of नरान् does not change to ओ."),
             ("नरांच्च", "न् before च gives ंश्, not a doubled च्च.")],
            "नरान् + च = नरांश्च, like उद्गारान् + च = उद्गारांश्च.",
            "न् + च → ंश्च.",
            teaches="A final न् before च becomes anusvāra followed by श्: उद्गारान् + च → उद्गारांश्च."),
    ],
}

# ---------------------------------------------------------------- unit 18
AUTHORED["18"] = {
    "title": "यमभिद्रवति छाया",
    "question": "By unit 18, what sign of a shadow and which hatreds does the verse list?",
    "rule": ("Whom a shadow (छाया), black, yellow or even reddish (कृष्णा पीताऽरुणाऽपि वा), rushes at (अभिद्रवति); "
             "and those who hate the physician, medicine, drink, food, elders and friends "
             "(भिषग्भेषजपानान्नगुरुमित्रद्विषः)."),
    "limits": ("छाया may also mean lustre or colour; 'shadow' is the plainer rendering. How it rushes at him is not "
               "stated. गुरु here = elder or teacher. The clause with ये appears to continue into card 19, which gives "
               "the predicate."),
    "explain_hi": ("यह श्लोक दो छपी पंक्तियों (०२.१०.३४ और ०२.१०.३५) से बना है। "
                   "जिस पर छाया, काली, पीली अथवा लालिमा लिए भी, झपटती है (अभिद्रवति)। ‘छाया’ का अर्थ कान्ति या रंग भी हो सकता है; डेटा सीधा अर्थ ‘छाया’ लेता है। "
                   "दूसरी पंक्ति: और जो वैद्य, औषध, पेय, अन्न, गुरु और मित्र से द्वेष करते हैं; यहाँ गुरु का अर्थ बड़ा या शिक्षक है। "
                   "डेटा के अनुसार ‘ये’ वाला वाक्य सम्भवतः कार्ड १९ में पूरा होता है। "
                   "‘भिषग्’ में भिषज् का ज् घोष भ से पहले ग् बना है।"),
    "hook": "काली, पीली, लाल छाया का झपटना; वैद्य, औषध, मित्र से द्वेष।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "In unit 18, what colour does अरुणा name?",
            ("Reddish", "अरुणा = reddish: कृष्णा पीताऽरुणाऽपि वा."),
            [("Bluish", "Bluish would be नीला; अरुणा is reddish."),
             ("Whitish", "Whitish would be श्वेता; अरुणा is reddish."),
             ("Greenish", "Greenish would be हरिता; अरुणा is reddish.")],
            "अरुण = reddish.",
            "अरुणा = reddish."),
        order(1, "Put the six things hated in unit 18 in the printed order.",
              ["भिषग्", "भेषज", "पान", "अन्न", "गुरु", "मित्र"],
              "Physician; medicine; drink; food; elder or teacher; friend.",
              "भिषग् → भेषज → पान → अन्न → गुरु → मित्र (+ द्विषः)."),
        match(2, "Match each word of unit 18 to its meaning.",
              [["छाया", "shadow"], ["कृष्णा", "black"], ["पीता", "yellow"], ["अभिद्रवति", "rushes at"],
               ["द्विष्", "one who hates"]],
              "छाया = shadow, कृष्णा = black, पीता = yellow, अभिद्रवति = rushes at, द्विष् = one who hates.",
              "छाया, कृष्णा, पीता, अभिद्रवति, द्विष्.", role="extend",
              teaches="-द्विष् at the end of a compound means 'hater of': भिषग्…मित्रद्विषः = haters of the physician … friends."),
        mcq("discriminate", 3, "Which split of पीताऽरुणाऽपि in unit 18 is right?",
            ("पीता + अरुणा + अपि", "आ + अ → आ twice (the print marks it with ऽ); feminine, agreeing with छाया."),
            [("पीता + आरुणा + आपि", "आरुणा and आपि are no words; the words are अरुणा and अपि."),
             ("पीतः + अरुणः + अपि", "These would be printed पीतोऽरुणोऽपि; the print has आ."),
             ("पीते + अरुणे + अपि", "These would be printed पीतेऽरुणेऽपि; the print has आ.")],
            "पीता (yellow) + अरुणा (reddish) + अपि (even).",
            "आ + अ → आ."),
        mcq("apply", 4, "Why is भिषज् printed भिषग् before भेषज in unit 18?",
            ("ज् became ग् before the voiced भ", "The data: j becomes g before bh, a voiced consonant."),
            [("ज् became ग् before a vowel", "भेषज begins with the consonant भ, not a vowel."),
             ("ग् is the stem's own final", "The stem is भिषज्; ग् arises only before the voiced भ."),
             ("ज् became ग् before a pause", "Here भिषज् stands inside a compound, before भ.")],
            "भिषज् + भेषज → भिषग्भेषज.",
            "ज् → ग् before a voiced consonant (here भ)."),
        mcq("transfer", 5, "By the pattern of मित्रद्विषः (haters of friends), what does देवद्विष् mean in a new example?",
            ("A hater of the gods", "देव (god) + द्विष् (hater): a hater of the gods."),
            [("A friend of the gods", "द्विष् means hater, not friend."),
             ("One hated by the gods", "द्विष् names the one who hates, not the one hated."),
             ("A gift for the gods", "द्विष् names a person who hates, not a gift.")],
            "देवद्विष् = hater of the gods, as मित्रद्विष् = hater of friends.",
            "-द्विष् = hater of.",
            teaches="-द्विष् after a noun names the one who hates it: मित्रद्विष्, देवद्विष्."),
    ],
}

# ---------------------------------------------------------------- unit 19
AUTHORED["19"] = {
    "title": "वशगाः सर्वएवैते",
    "question": "By unit 19, under whose sway are all these said to be, and which body parts sweat?",
    "rule": ("All these (सर्वे एव एते) are to be known (विज्ञेयाः) as gone under the sway (वशगाः) of Samavartin "
             "(समवर्तिनः, Yama). Line 2 begins: he whose neck, forehead and heart (ग्रीवाललाटहृदयम्) sweat "
             "(स्विद्यति), cold (शीतलम्)…"),
    "limits": ("Whether the sweat or the parts are cold is not decided: no question on it. 'These' points back to what "
               "was listed before (the data's note says the signs). Line 2 appears to continue in card 20."),
    "explain_hi": ("यह श्लोक दो छपी पंक्तियों (०२.१०.३६ और ०२.१०.३७) से बना है। "
                   "पहली पंक्ति: ये सभी (सर्वे एव एते) समवर्ती यानी यम के वश में गए हुए (वशगाः) जानने चाहिए (विज्ञेयाः)। "
                   "‘समवर्तिन्’ का शब्दार्थ है ‘सम व्यवहार करने वाला’; यह यम की मानक उपाधि है। "
                   "दूसरी पंक्ति: जिसकी गर्दन, ललाट और हृदय पसीजते हैं, शीतल (शीतलम्); ठंडा पसीना है या अंग, यह संस्कृत से तय नहीं। "
                   "डेटा के अनुसार यह वाक्य सम्भवतः कार्ड २० में आगे चलता है। ‘एवैते’ में एव + एते है: अ + ए → ऐ।"),
    "hook": "ये सब समवर्ती (यम) के वश में; गर्दन, माथा, हृदय पसीजते।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "In unit 19, whom does समवर्तिन् name?",
            ("Yama", "समवर्तिन् ('acting evenly') is a standard epithet of Yama."),
            [("Indra", "Indra is not called समवर्तिन्; the data reads Yama."),
             ("Agni", "Agni is not called समवर्तिन्; the data reads Yama."),
             ("Soma", "Soma is not called समवर्तिन्; the data reads Yama.")],
            "समवर्तिन् = Yama (standard epithet).",
            "समवर्तिन् = Yama."),
        order(1, "Put the words of line 1 of unit 19 in the printed order.",
              ["वशगाः", "सर्वएवैते", "विज्ञेयाः", "समवर्तिनः"],
              "Gone under the sway; all these indeed; to be known; of Samavartin.",
              "वशगाः → सर्वएवैते → विज्ञेयाः → समवर्तिनः."),
        match(2, "Match each word of unit 19 to its meaning.",
              [["वशग", "gone under the sway"], ["विज्ञेय", "to be known"], ["ग्रीवा", "neck"],
               ["ललाट", "forehead"], ["हृदय", "heart"], ["स्विद्यति", "sweats"]],
              "वशग = gone under the sway, विज्ञेय = to be known, ग्रीवा = neck, ललाट = forehead, हृदय = heart, स्विद्यति = sweats.",
              "वशग, विज्ञेय, ग्रीवा, ललाट, हृदय, स्विद्यति.", role="extend",
              teaches="विज्ञेयाः is a gerundive ('to be known'); it agrees with वशगाः in the masculine nominative plural."),
        mcq("discriminate", 3, "Which split of सर्वएवैते in unit 19 is right?",
            ("सर्वे + एव + एते", "ए before a vowel → अय्, here with य् dropped (सर्व एव); अ + ए → ऐ (एवैते)."),
            [("सर्वे + एवा + एते", "एवा is no form; the particle is एव."),
             ("सर्व + एवै + ते", "एवै is no word; ऐ comes from एव + एते."),
             ("सर्वे + एव + इते", "अ + इ would give ए (एवेते); the print has ऐ.")],
            "सर्वे (all) + एव (indeed) + एते (these).",
            "अ + ए → ऐ."),
        mcq("apply", 4, "Why does एव + एते give एवैते in unit 19?",
            ("अ + ए → ऐ", "A final अ and a following ए merge into ऐ: एवैते."),
            [("अ + ए → ए", "ए arises from अ + इ, not from अ + ए."),
             ("अ + ए → अय्", "अय् arises from ए before a vowel, not from अ + ए."),
             ("ए + ए → ऐ", "एव ends in अ, not in ए.")],
            "एव + एते: अ + ए → ऐ.",
            "अ + ए → ऐ."),
        mcq("transfer", 5, "By the pattern of एव + एते → एवैते, how is तत्र + एव (in that very place) joined in a new example?",
            ("तत्रैव", "अ + ए → ऐ: तत्र + एव → तत्रैव."),
            [("तत्रेव", "ए would come from अ + इ; here the vowel is ए."),
             ("तत्रोव", "ओ would come from अ + उ; here the vowel is ए."),
             ("तत्रयेव", "अय् comes from ए before a vowel; here अ stands first.")],
            "तत्र + एव = तत्रैव, like एव + एते = एवैते.",
            "अ + ए → ऐ.",
            teaches="A final अ before ए (or ऐ) merges into ऐ: एव + एते → एवैते."),
    ],
}

# ---------------------------------------------------------------- unit 20
AUTHORED["20"] = {
    "title": "उष्णोऽपरः प्रदेशश्च",
    "question": "By unit 20, what is said of the other region and of his refuge, and which signs follow?",
    "rule": ("And the other region (अपरः प्रदेशः) is hot (उष्णः); his refuge is the deities (शरणं तस्य देवताः). He who "
             "is of small light (अणुज्योतिः), not one-pointed (अनेकाग्रः), ill-lustred (दुश्छायः), always low-spirited "
             "(दुर्मनाः सदा)."),
    "limits": ("'The other region' is not specified; line 1 appears to continue the 'whose' clause of card 19. ज्योतिः "
               "(eye-light or bodily lustre) and छाया (lustre, complexion or shadow) are not specified. अनेकाग्र has two "
               "parses with one sense. No main verb; the clause appears to continue."),
    "explain_hi": ("यह श्लोक दो छपी पंक्तियों (०२.१०.३८ और ०२.१०.३९) से बना है। "
                   "पहली पंक्ति, डेटा के अनुसार सम्भवतः कार्ड १९ के ‘यस्य’ वाले वाक्य को आगे चलाती है: और दूसरा भाग (अपरः प्रदेशः) गरम है; उसकी शरण देवता हैं। ‘दूसरा भाग’ कौन-सा, यह पाठ नहीं बताता। "
                   "दूसरी पंक्ति: जो सूक्ष्म ज्योति वाला (अणुज्योतिः), अनेकाग्र यानी एकाग्र नहीं, दुश्छाय यानी बुरी कान्ति वाला, और सदा खिन्न मन वाला (दुर्मनाः) है। "
                   "ज्योति आँख की है या शरीर की, और छाया कान्ति है, रंग है या परछाईं, यह निश्चित नहीं। "
                   "‘दुश्छायो’ में दुः + छायः है: छ से पहले विसर्ग → श्।"),
    "hook": "दूसरा भाग गरम, शरण देवता; मन्द ज्योति, खिन्न मन।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "In unit 20, what does उष्ण mean?",
            ("Hot", "उष्ण = hot: उष्णोऽपरः प्रदेशः, the other region is hot."),
            [("Cold", "Cold would be शीत; उष्ण is hot."),
             ("Moist", "Moist would be आर्द्र; उष्ण is hot."),
             ("Dry", "Dry would be शुष्क; उष्ण is hot.")],
            "उष्ण = hot.",
            "उष्ण = hot."),
        order(1, "Put the signs of line 2 of unit 20 in the printed order.",
              ["अणुज्योतिः", "अनेकाग्रः", "दुश्छायः", "दुर्मनाः", "सदा"],
              "Of small light; not one-pointed; ill-lustred; low-spirited; always.",
              "अणुज्योतिः → अनेकाग्रः → दुश्छायः → दुर्मनाः → सदा."),
        match(2, "Match each word of unit 20 to its meaning.",
              [["अपर", "other"], ["प्रदेश", "region, part"], ["शरण", "refuge"], ["देवता", "deity"],
               ["अणु", "small"], ["दुर्मनस्", "low-spirited"]],
              "अपर = other, प्रदेश = region, शरण = refuge, देवता = deity, अणु = small, दुर्मनस् = low-spirited.",
              "अपर, प्रदेश, शरण, देवता, अणु, दुर्मनस्.", role="extend",
              teaches="दुर्मनाः is the nominative of दुर्मनस् (दुः + मनस्, visarga before the voiced म → र्): low-spirited."),
        mcq("discriminate", 3, "Which split of उष्णोऽपरः in unit 20 is right?",
            ("उष्णः + अपरः", "अः + अ → ओ, and the अ is dropped (ऽ): उष्णोऽपरः."),
            [("उष्णा + अपरः", "आ + अ → आ would give उष्णापरः."),
             ("उष्ण + ओपरः", "ओपरः is no word; the ओ comes from the visarga of उष्णः."),
             ("उष्णे + अपरः", "This would be printed उष्णेऽपरः; the print has ओ.")],
            "उष्णः (hot) + अपरः (other).",
            "अः + अ → ओऽ."),
        mcq("apply", 4, "Why is दुः printed दुश् before छायः in unit 20?",
            ("Visarga before छ → श्", "छ is a voiceless palatal: दुः + छायः → दुश्छायः."),
            [("Visarga before छ → स्", "स् comes before त or थ, not before छ."),
             ("Visarga before छ → र्", "र् comes before a voiced sound; छ is voiceless."),
             ("Visarga before छ drops", "It does not drop; it becomes श्, as printed.")],
            "दुः + छायः: visarga before छ → श्.",
            "ः + च/छ → श्."),
        mcq("transfer", 5, "By the pattern of दुः + छायः → दुश्छायः, how is दुः + चरितम् (bad conduct) joined in a new example?",
            ("दुश्चरितम्", "Visarga before च → श्: दुश्चरितम्."),
            [("दुर्चरितम्", "र् comes before a voiced sound; च is voiceless."),
             ("दुस्चरितम्", "स् comes before त or थ, not before च."),
             ("दुचरितम्", "The visarga does not drop before च; it becomes श्.")],
            "दुः + चरितम् = दुश्चरितम्, like दुः + छायः = दुश्छायः.",
            "ः + च/छ → श्.",
            teaches="A visarga before च or छ becomes श्: दुः + छायः → दुश्छायः."),
    ],
}

# ---------------------------------------------------------------- unit 21
AUTHORED["21"] = {
    "title": "बलिं बलिभुजो यस्य",
    "question": "By unit 21, what sign concerns the offering, and which four goods are named?",
    "rule": ("He whose offering (बलिम्) set out (प्रणीतम्) the bali-eaters (बलिभुजः, probably crows) do not eat "
             "(न उपभुञ्जते). And he who, without cause (निर्निमित्तम्), intellect, beauty, growth, prosperity "
             "(मेधां शोभाम् उपचयं श्रियम्)…"),
    "limits": ("बलिभुज् = 'eater of the bali offering'; crow is the probable sense and other bali-eaters are not "
               "excluded: no question on the identity. The verb of line 2 (प्राप्नोति) is in card 22; this card does "
               "not say what he does with the four goods."),
    "explain_hi": ("यह श्लोक दो छपी पंक्तियों (०२.१०.४० और ०२.१०.४१) से बना है। "
                   "जिसकी रखी हुई बलि (बलिं प्रणीतम्) को बलिभुज, यानी बलि खाने वाले (सम्भवतः कौए), नहीं खाते (नोपभुंजते)। "
                   "‘बलिभुज्’ का शब्दार्थ ‘बलि खाने वाला’ है; कौआ सम्भावित अर्थ है, दूसरे बलि खाने वाले भी शब्द से बाहर नहीं। "
                   "दूसरी पंक्ति: और जो बिना कारण (निर्निमित्तम्) मेधा, शोभा, उपचय (वृद्धि) और श्री (समृद्धि)…; इन चारों की क्रिया ‘प्राप्नोति’ कार्ड २२ में है। "
                   "‘नोपभुंजते’ में न + उपभुञ्जते है: अ + उ → ओ।"),
    "hook": "बलि न खाएँ बलिभुज; बिना कारण मेधा, शोभा, उपचय, श्री।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "In unit 21, what does बलि mean?",
            ("An offering", "बलि = an offering set out: बलिं … प्रणीतम्."),
            [("A strong man", "A strong man is बलिन् (बली); बलि is an offering."),
             ("A boundary", "A boundary is सीमा; बलि is an offering."),
             ("A cooking pot", "A pot is स्थाली; बलि is an offering.")],
            "बलि = offering.",
            "बलि = offering."),
        order(1, "Put the four goods of line 2 of unit 21 in the printed order.",
              ["मेधां", "शोभाम्", "उपचयं", "श्रियं"],
              "Intellect; beauty; growth; prosperity.",
              "मेधां → शोभाम् → उपचयं → श्रियं."),
        match(2, "Match each word of unit 21 to its meaning.",
              [["मेधा", "intellect"], ["शोभा", "beauty"], ["उपचय", "growth"], ["श्री", "prosperity"],
               ["निर्निमित्त", "without cause"]],
              "मेधा = intellect, शोभा = beauty, उपचय = growth, श्री = prosperity, निर्निमित्त = without cause.",
              "मेधा, शोभा, उपचय, श्री, निर्निमित्त.", role="extend",
              teaches="निर्निमित्तम् (निः + निमित्त, visarga before the voiced न → र्) is used as an adverb: 'without cause'."),
        mcq("discriminate", 3, "Which split of नोपभुंजते in unit 21 is right?",
            ("न + उपभुंजते", "अ + उ → ओ: न + उपभुंजते → नोपभुंजते."),
            [("नो + पभुंजते", "पभुंजते is no word; the ओ comes from न + उ."),
             ("न + ओपभुंजते", "ओपभुंजते is no word; the verb is उपभुंजते."),
             ("नौ + उपभुंजते", "औ + उ would give आवु (नावुप-); the print has ओ.")],
            "न (not) + उपभुंजते (eat): अ + उ → ओ.",
            "अ + उ → ओ."),
        mcq("apply", 4, "By unit 21, what is said of the offering set out by such a man?",
            ("The bali-eaters do not eat it", "बलिं बलिभुजो यस्य प्रणीतं नोपभुंजते."),
            [("The bali-eaters eat it at once", "The verse has न: they do not eat it."),
             ("The physician takes it away", "No physician is named in unit 21."),
             ("The deities accept it gladly", "No deity is named in unit 21.")],
            "Not eaten by the bali-eaters.",
            "नोपभुंजते = do not eat."),
        mcq("transfer", 5, "By the pattern of न + उपभुंजते → नोपभुंजते, how is न + उत्तिष्ठति (does not rise) joined in a new example?",
            ("नोत्तिष्ठति", "अ + उ → ओ: न + उत्तिष्ठति → नोत्तिष्ठति."),
            [("नौत्तिष्ठति", "औ would come from अ + ओ or औ; here the vowel is उ."),
             ("नूत्तिष्ठति", "ऊ would come from उ + उ; here न ends in अ."),
             ("नवुत्तिष्ठति", "अव् comes from ओ before a vowel; here न ends in अ.")],
            "न + उत्तिष्ठति = नोत्तिष्ठति, like न + उपभुंजते = नोपभुंजते.",
            "अ + उ → ओ.",
            teaches="A final अ before उ (or ऊ) merges into ओ: न + उपभुंजते → नोपभुंजते."),
    ],
}

# ---------------------------------------------------------------- unit 22
AUTHORED["22"] = {
    "title": "प्राप्नोत्यतोवा विभ्रंशं",
    "question": "By unit 22, what does the man of card 21 gain or lose, where does he go, and what begins in line 2?",
    "rule": ("(He who without cause) obtains (प्राप्नोति) these, or (अतो वा, read two ways) a falling away (विभ्रंशम्): he "
             "reaches the abode of Yama (स प्राप्नोति यमक्षयम्). Line 2 begins: whose (prakṛti), made of guṇa and doṣa "
             "(गुणदोषमयी), of a healthy or an ill person…"),
    "limits": ("अतो वा may be 'from these' or 'from this cause': no question on it. Line 1 appears to complete the sentence "
               "of card 21. The noun प्रकृतिः agreeing with गुणदोषमयी, and its verb, are in card 23. No reason or time "
               "is given here."),
    "explain_hi": ("यह श्लोक दो छपी पंक्तियों (०२.१०.४२ और ०२.१०.४३) से बना है। "
                   "पहली पंक्ति, डेटा के अनुसार सम्भवतः कार्ड २१ का वाक्य पूरा करती है: (जो बिना कारण मेधा, शोभा, उपचय, श्री) पाता है, अथवा इनसे पतन (विभ्रंशम्) पाता है, वह यम के घर (यमक्षयम्) पहुँचता है। "
                   "‘अतो वा’ का अर्थ ‘इनसे’ या ‘इस कारण से’ दोनों हो सकता है; डेटा का भाव: बिना कारण अचानक लाभ या अचानक हानि। "
                   "दूसरी पंक्ति: जिस स्वस्थ या रोगी की गुण और दोष से बनी…; संज्ञा ‘प्रकृतिः’ और क्रिया कार्ड २३ में हैं। "
                   "‘यमक्षय’ में क्षय (पुल्लिंग) का अर्थ घर है।"),
    "hook": "बिना कारण लाभ या पतन: यमक्षय।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "In unit 22, what does यमक्षय mean?",
            ("The abode of Yama", "क्षय (masc.) = abode: यमक्षय, the abode of Yama."),
            [("The anger of Yama", "Anger would be क्रोध; क्षय here is abode."),
             ("The servant of Yama", "A servant would be किंकर; क्षय here is abode."),
             ("The name of Yama", "A name would be नाम; क्षय here is abode.")],
            "यम + क्षय (abode) = Yama's abode.",
            "यमक्षय = abode of Yama."),
        order(1, "Put the words of line 1 of unit 22 in the printed order.",
              ["प्राप्नोत्यतोवा", "विभ्रंशं", "स", "प्राप्नोति", "यमक्षयं"],
              "Obtains, or (अतो वा, read two ways); a falling away; he; reaches; the abode of Yama.",
              "प्राप्नोत्यतोवा → विभ्रंशं → स → प्राप्नोति → यमक्षयं."),
        match(2, "Match each word of unit 22 to its meaning.",
              [["प्राप्नोति", "obtains, reaches"], ["विभ्रंश", "falling away"], ["स्वस्थ", "healthy"],
               ["व्याधित", "ill"], ["-मय", "made of"]],
              "प्राप्नोति = obtains, विभ्रंश = falling away, स्वस्थ = healthy, व्याधित = ill, -मय = made of.",
              "प्राप्नोति, विभ्रंश, स्वस्थ, व्याधित, -मय.", role="extend",
              teaches="-मय (feminine -मयी) means 'made of, consisting of': गुणदोषमयी = made of guṇa and doṣa."),
        mcq("discriminate", 3, "Which split of गुणदोषमयी in unit 22 is right?",
            ("गुण + दोष + मयी", "गुण (quality) + दोष + -मयी (made of, feminine of -मय)."),
            [("गुणः + दोषमयी", "A separate गुणः would be printed गुणो before द; the print has गुणदोष-."),
             ("गुणदोष + अमयी", "अ + अ → आ would give गुणदोषामयी; the print has -षम-."),
             ("गुण + दोषम् + अयी", "अयी is no word; the ending is -मयी, 'made of'.")],
            "गुण + दोष + -मयी = made of guṇa and doṣa.",
            "-मयी = made of (feminine)."),
        mcq("apply", 4, "Why is सः printed स before प्राप्नोति in unit 22?",
            ("सः drops its visarga before a consonant", "The pronoun सः loses its visarga before any consonant: स प्राप्नोति."),
            [("Every अः drops its visarga before a consonant", "Not every: आर्तः + दीर्घं gives आर्तो (card 13)."),
             ("स is the full nominative of the pronoun", "The nominative is सः; the visarga is lost by sandhi."),
             ("सः drops its visarga before अ as well", "Before अ, सः + अ gives सोऽ.")],
            "सः + प्राप्नोति → स प्राप्नोति.",
            "सः + consonant → स."),
        mcq("transfer", 5, "By the pattern of स प्राप्नोति, how is सः + गच्छति (he goes) joined in a new example?",
            ("स गच्छति", "सः drops its visarga before a consonant: स गच्छति."),
            [("सो गच्छति", "सः does not take ओ before a consonant; it drops the visarga."),
             ("सर् गच्छति", "र् comes after a vowel other than अ/आ; here it is अ."),
             ("सश् गच्छति", "श् comes before च, छ or श, not before ग.")],
            "सः + गच्छति = स गच्छति, like सः + प्राप्नोति = स प्राप्नोति.",
            "सः + consonant → स.",
            teaches="The pronouns सः and एषः drop the visarga before any consonant: स प्राप्नोति, स गच्छति."),
    ],
}

# ---------------------------------------------------------------- unit 23
AUTHORED["23"] = {
    "title": "यात्यन्यथात्वं प्रकृतिः",
    "question": "By unit 23, what goes into change in line 1, and which six things does line 2 list?",
    "rule": ("(Whose) natural state (प्रकृतिः) goes into change (याति अन्यथात्वम्)… Line 2 lists devotion, character, "
             "memory, giving up, intellect and strength (भक्तिः शीलं स्मृतिः त्यागः बुद्धिः बलम्), without cause "
             "(अहेतुकम्)."),
    "limits": ("Low confidence. Printed षण्मासान्त is no grammatical form; the repairs give opposite senses (not six "
               "months / to the end of six months), left open: no question on the time. अहेतुकम् probably goes with "
               "card 24's verb. त्याग may be generosity."),
    "explain_hi": ("यह श्लोक दो छपी पंक्तियों (०२.१०.४४ और ०२.१०.४५) से बना है; विश्वास कम है। "
                   "डेटा के अनुसार पहली पंक्ति कार्ड २२ के ‘यस्य … गुणदोषमयी’ से जुड़ती है: जिसकी प्रकृति (स्वाभाविक अवस्था) बदल जाती है (याति अन्यथात्वम्)। "
                   "छपा ‘षण्मासान्त’ व्याकरण से कोई रूप नहीं; ‘छह मास तक नहीं जीता’ और ‘छह मास के अन्त तक जीता है’ दोनों पाठ सम्भव हैं और उनके अर्थ उलटे हैं, इसलिए समय पर कोई प्रश्न नहीं। "
                   "दूसरी पंक्ति छह बातें गिनाती है: भक्ति, शील, स्मृति, त्याग, बुद्धि और बल, बिना कारण (अहेतुकम्); ‘अहेतुकम्’ सम्भवतः कार्ड २४ की क्रिया से जुड़ता है। "
                   "‘बुद्धिर्बलम्’ में बुद्धिः + बलम् है: इ के बाद का विसर्ग घोष व्यंजन से पहले र् बनता है।"),
    "hook": "प्रकृति बदले; भक्ति, शील, स्मृति, त्याग, बुद्धि, बल।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "In unit 23, what does प्रकृति mean?",
            ("The natural state", "प्रकृति = the natural state: प्रकृतिः याति अन्यथात्वम्."),
            [("The daily food", "Food would be अन्न; प्रकृति is the natural state."),
             ("The bodily strength", "Strength is बल, listed in line 2; प्रकृति is the natural state."),
             ("A teacher's advice", "Advice would be उपदेश; प्रकृति is the natural state.")],
            "प्रकृति = natural state.",
            "प्रकृति = natural state."),
        order(1, "Put the six items of line 2 of unit 23 in the printed order.",
              ["भक्तिः", "शीलं", "स्मृतिः", "त्यागः", "बुद्धिः", "बलम्"],
              "Devotion; character; memory; giving up; intellect; strength.",
              "भक्तिः → शीलं → स्मृतिः → त्यागः → बुद्धिः → बलम्."),
        match(2, "Match each word of unit 23 to its meaning.",
              [["भक्ति", "devotion"], ["शील", "character, conduct"], ["स्मृति", "memory"], ["बुद्धि", "intellect"],
               ["बल", "strength"]],
              "भक्ति = devotion, शील = character, स्मृति = memory, बुद्धि = intellect, बल = strength.",
              "भक्ति, शील, स्मृति, बुद्धि, बल.", role="extend",
              teaches="अन्यथात्वम् = अन्यथा (otherwise) + -त्व (-ness): 'otherness', change; याति अन्यथात्वम् = goes into change."),
        mcq("discriminate", 3, "Which split of यात्यन्यथात्वं in unit 23 is right?",
            ("याति + अन्यथात्वम्", "इ + अ → य: याति + अन्यथात्वम् → यात्यन्यथात्वम्."),
            [("यातु + अन्यथात्वम्", "उ + अ would give व (यात्वन्यथा-); the print has य."),
             ("याति + न्यथात्वम्", "न्यथात्वम् is no word; the word is अन्यथात्वम्."),
             ("यात्य + अन्यथात्वम्", "यात्य is no form; the verb is याति.")],
            "याति (goes) + अन्यथात्वम् (change).",
            "इ + unlike vowel → य्."),
        mcq("apply", 4, "Why is बुद्धिः printed बुद्धिर् before बलम् in unit 23?",
            ("इः before a voiced sound → इर्", "ब is voiced: बुद्धिः + बलम् → बुद्धिर्बलम्."),
            [("इः before a voiced sound → ओ", "ओ comes only from अः before a voiced consonant."),
             ("इः before any consonant → इर्", "Not any: before त it gives स् (स्मृतिस्त्यागो, same line)."),
             ("र् is the noun's own final", "बुद्धि ends in इ; the nominative is बुद्धिः.")],
            "बुद्धिः + बलम्: visarga after इ before the voiced ब → र्.",
            "इः + voiced sound → इर्."),
        mcq("transfer", 5, "By the pattern of बुद्धिः + बलम् → बुद्धिर्बलम्, how is मतिः + भवति (the thought arises) joined in a new example?",
            ("मतिर्भवति", "Visarga after इ before the voiced भ → र्: मतिर्भवति."),
            [("मतिस्भवति", "स् comes before त or थ, not before भ."),
             ("मतीभवति", "The vowel is lengthened only when र् meets र्; here भ follows."),
             ("मतिश्भवति", "श् comes before च, छ or श, not before भ.")],
            "मतिः + भवति = मतिर्भवति, like बुद्धिः + बलम् = बुद्धिर्बलम्.",
            "इः + voiced sound → इर्.",
            teaches="A visarga after इ (or another vowel than अ/आ) before a voiced sound becomes र्: बुद्धिः + बलम् → बुद्धिर्बलम्."),
    ],
}

# ================================================================ NOTES_HI
NOTES_HI = {
    "13": ("श्लोक; विश्वास मध्यम; दो छपी पंक्तियाँ (०२.१०.२४ और ०२.१०.२५) जोड़ी गईं। पाठ-चिह्न (सम्भावित): छपा ‘उच्छ्रस्य’ कोई "
           "क्रिया-रूप नहीं; ‘उच्छ्वस्य’ (साँस भीतर लेकर) ‘निश्वस्य’ (बाहर छोड़कर) से जोड़ा बनाता है, स्कैन में व/र की भूल; इस पर प्रश्न नहीं। "
           "‘चेष्टते’ को ‘दीर्घम्’ के साथ पढ़ना भी सम्भव है; सीधी सूची का अर्थ लिया गया। ‘श्वसिति चेष्टते’ के बीच ‘और’ संस्कृत में नहीं। "
           "सन्धि जाँची: यः + वा → यो वा; वा + अल्पाशी → वाऽल्पाशी (आ + अ → आ, छपाई में ऽ); कफेन + आर्तः → कफेनार्तः (अ + आ → आ); "
           "आर्तः + दीर्घं → आर्तो दीर्घं (अः + घोष व्यंजन → ओ)।"),
    "14": ("श्लोक; विश्वास कम; दो छपी पंक्तियाँ (०२.१०.२६ और ०२.१०.२७) जोड़ी गईं। पाठ-चिह्न: ‘कृच्छ्रायो’ में कृच्छ्रात् का अन्तिम द् छूटा "
           "लगता है (सम्भावित: कृच्छ्राद्यो); ‘अचयित्वा प्रपाणिकौ’ छपाई में टूटे, कोई पहचानने योग्य अर्थ नहीं, जैसे छपे वैसे रखे "
           "(समीक्षक का अनुमान ‘अञ्चयित्वा’ अपनाया नहीं)। इन पर कोई प्रश्न नहीं। ‘व्याविद्धम्’ = झटके से (क्रियाविशेषण); ‘चुभन के साथ’ भी सम्भव। "
           "सन्धि जाँची: शिरः + विक्षिपते → शिरो विक्षिपते (अः + घोष व्यंजन → ओ); ह्रस्वम् + च → ह्रस्वं च (वाक्य में व्यंजन से पहले म् → ं)।"),
    "15": ("श्लोक; विश्वास मध्यम; दो छपी पंक्तियाँ (०२.१०.२८ और ०२.१०.२९) जोड़ी गईं; कोई पाठ-चिह्न नहीं। ‘संधान-बंधन’ = संधान और "
           "बन्धन, सम्भवतः जोड़ और उन्हें बाँधने वाले; कोई सटीक शारीरिक नाम नहीं दिया। ‘संमुह्येत्’ = मोहग्रस्त या सम्भवतः मूर्च्छित, दोनों सम्भव। "
           "सन्धि जाँची: संमुह्येत् + यः → संमुह्येद्यो (घोष य से पहले त् → द्; यः + बली → यो बली, अः + घोष व्यंजन → ओ); "
           "दुर्बलः + अपि → दुर्बलोऽपि (अः + अ → ओऽ)। छपा ‘संधान’, ‘बंधन’ अनुस्वार के साथ = सन्धान, बन्धन।"),
    "16": ("श्लोक; विश्वास मध्यम; दो छपी पंक्तियाँ (०२.१०.३० और ०२.१०.३१) जोड़ी गईं; कोई पाठ-चिह्न नहीं। छपाई में ‘उत्तानएव’ बिना "
           "सन्धि के जुड़ा है; नियमित रूप ‘उत्तान एव’ (अः + अ से भिन्न स्वर → अ, बीच में अन्तर)। ‘विकरोति’ = विकृत करता है, या अनियमित हिलाता है। "
           "‘जिघृक्षति’ √ग्रह् का सन्नन्त। सन्धि जाँची: यः + असत् → योऽसत् (अः + अ → ओऽ); असत् + एव → असदेव (स्वर से पहले त् → द्)।"),
    "17": ("श्लोक; विश्वास मध्यम; दो छपी पंक्तियाँ (०२.१०.३२ और ०२.१०.३३) जोड़ी गईं। पाठ-चिह्न (सम्भव): छपा ‘पेरिलेहन्त्युद्गारांश्च’; "
           "‘लेहन्ति’ बहुवचन है, जो एकवचन ‘यः … करोति’ से मेल नहीं खाता; ‘परिलेहति’ अपेक्षित है (पे/प और अतिरिक्त न् स्कैन की भूल लगती है)। "
           "अनुवाद इसे अनुमानित पाठ पर लेता है; इस क्रिया पर प्रश्न नहीं। ‘अहास्यहासी’ = न हँसने योग्य पर हँसने वाला (या बिना कारण हँसने वाला)। "
           "सन्धि जाँची: दशन + छद → दशनच्छद (ह्रस्व स्वर के बाद छ → च्छ); उद्गारान् + च → उद्गारांश्च (न् + च → ंश्च)।"),
    "18": ("श्लोक; विश्वास मध्यम; दो छपी पंक्तियाँ (०२.१०.३४ और ०२.१०.३५) जोड़ी गईं; कोई पाठ-चिह्न नहीं। ‘छाया’ = परछाईं (कान्ति, रंग "
           "भी सम्भव); ‘अभिद्रवति’ शत्रुता से या पास आने के अर्थ में, यह नहीं कहा। गुरु = बड़ा या शिक्षक। डेटा के अनुसार ‘ये’ वाला वाक्य सम्भवतः "
           "कार्ड १९ (वशगाः सर्व एवैते …) में पूरा होता है। सन्धि जाँची: यम् + अभिद्रवति → यमभिद्रवति; पीता + अरुणा + अपि → पीताऽरुणाऽपि "
           "(आ + अ → आ, छपाई में ऽ); भिषज् + भेषज → भिषग्भेषज (घोष भ से पहले ज् → ग्); पान + अन्न → पानान्न (अ + अ → आ); -द्विषः + च → -द्विषश्च।"),
    "19": ("श्लोक; विश्वास अधिक; दो छपी पंक्तियाँ (०२.१०.३६ और ०२.१०.३७) जोड़ी गईं; कोई पाठ-चिह्न नहीं। समवर्तिन् = यम (मानक उपाधि), "
           "षष्ठी एकवचन। ‘एते’ पहले गिनाए गए की ओर संकेत है; डेटा की टिप्पणी ‘लक्षण’ कहती है, पर पुल्लिंग रूप (एते, वशगाः) व्यक्तियों से भी "
           "मेल खाते हैं; इस पर प्रश्न नहीं। ठंडा पसीना है या अंग, यह तय नहीं। डेटा के अनुसार दूसरी पंक्ति सम्भवतः कार्ड २० में आगे चलती है। "
           "सन्धि जाँची: सर्वे + एव → सर्व एव (ए + स्वर → अय्, य् का वैकल्पिक लोप; छपाई में बिना अन्तर ‘सर्वएव’); एव + एते → एवैते (अ + ए → ऐ)।"),
    "20": ("श्लोक; विश्वास मध्यम; दो छपी पंक्तियाँ (०२.१०.३८ और ०२.१०.३९) जोड़ी गईं; कोई पाठ-चिह्न नहीं। ‘उष्णः अपरः प्रदेशः’ और "
           "‘शरणं तस्य देवताः’ में क्रिया समझी जाती है; ‘दूसरा भाग’ कौन, यह नहीं कहा। ज्योति आँख की या शरीर की, अनिश्चित; छाया = कान्ति, रंग "
           "या परछाईं। ‘अनेकाग्र’ = अन्-एकाग्र या अनेक-अग्र, अर्थ एक। सन्धि जाँची: उष्णः + अपरः → उष्णोऽपरः, यः + अणु- → योऽणु- (अः + अ → ओऽ); "
           "प्रदेशः + च → प्रदेशश्च; दुः + छायः → दुश्छायः (च/छ से पहले विसर्ग → श्); -ज्योतिः + अनेकाग्रः → -ज्योतिरनेकाग्रः (इः + स्वर → इर्)।"),
    "21": ("श्लोक; विश्वास मध्यम; दो छपी पंक्तियाँ (०२.१०.४० और ०२.१०.४१) जोड़ी गईं; कोई पाठ-चिह्न नहीं। बलिभुज् = बलि खाने वाला; "
           "कौआ सम्भावित अर्थ, दूसरे बलि खाने वाले शब्द से बाहर नहीं। ‘प्रणीतम्’ = रखी हुई, ‘बलिम्’ से मेल। दूसरी पंक्ति के चार कर्मों की क्रिया "
           "‘प्राप्नोति’ कार्ड २२ में है। सन्धि जाँची: बलिभुजः + यस्य → बलिभुजो यस्य (अः + घोष व्यंजन → ओ); न + उपभुञ्जते → नोपभुंजते (अ + उ → ओ); "
           "निः + निमित्तम् → निर्निमित्तम् (इः + घोष → इर्); शोभाम् + उपचयम् → शोभामुपचयं।"),
    "22": ("श्लोक; विश्वास मध्यम; दो छपी पंक्तियाँ (०२.१०.४२ और ०२.१०.४३) जोड़ी गईं; कोई पाठ-चिह्न नहीं। ‘अतो वा’ दो तरह पढ़ा जा सकता है "
           "(इनसे, या इस कारण से); भाव: बिना कारण अचानक लाभ या हानि। क्षय (पुल्लिंग) = घर। दूसरी पंक्ति की संज्ञा ‘प्रकृतिः’ (मयी से मेल) "
           "और क्रिया कार्ड २३ में। सन्धि जाँची: प्राप्नोति + अतः → प्राप्नोत्यतः (इ + भिन्न स्वर → य्); अतः + वा → अतो वा (छपाई में बिना अन्तर "
           "‘अतोवा’); सः + प्राप्नोति → स प्राप्नोति (सः व्यंजन से पहले विसर्ग खोता है)।"),
    "23": ("श्लोक; विश्वास कम; दो छपी पंक्तियाँ (०२.१०.४४ और ०२.१०.४५) जोड़ी गईं। पाठ-चिह्न (सम्भव): ‘षण्मासान्त’ कोई व्याकरणिक रूप "
           "नहीं; सुझाव ‘षण्मासान् न’ (छह मास नहीं जीता), दूसरा सम्भव सुधार ‘षण्मासान्ते’ (छह मास के अन्त तक जीता); अर्थ उलटे, स्वामी के लिए खुला; "
           "त/न की भूल इस छपाई में ज्ञात है, पर यह प्रमाण नहीं। समय पर कोई प्रश्न नहीं। ‘अहेतुकम्’ सम्भवतः कार्ड २४ की ‘निवर्तन्ते’ से जुड़ता है; "
           "त्याग = त्याग या उदारता; भक्ति का विषय नहीं कहा। सन्धि जाँची: याति + अन्यथात्वम् → यात्यन्यथात्वं (इ + भिन्न स्वर → य्); "
           "स्मृतिः + त्यागः → स्मृतिस्त्यागः (त से पहले विसर्ग → स्); त्यागः + बुद्धिः → त्यागो बुद्धिः (अः + घोष व्यंजन → ओ); "
           "बुद्धिः + बलम् → बुद्धिर्बलम् (इः + घोष → इर्)।"),
}

# ================================================================ AIDS
AIDS = {
    "13": {
        "chunks": "यो वाऽल्पाशी | कफेनार्तो | दीर्घं श्वसिति चेष्टते || दीर्घमुच्छ्रस्य | यो ह्रस्वं निश्वस्य | परिताम्यति",
        "seesaw": ("दीर्घम् ⇄ ह्रस्वम्: दोनों इसी इकाई की दूसरी पंक्ति में; दीर्घम् उच्छ्रस्य (सम्भावित पाठ उच्छ्वस्य: भीतर साँस) ⇄ "
                   "ह्रस्वं निश्वस्य (बाहर छोड़कर), फिर परिताम्यति।"),
        "sandhi": ("अ + आ → आ: कफेन + आर्तः → कफेनार्तः · अः + घोष व्यंजन → ओ: आर्तः + दीर्घं → आर्तो दीर्घं, यः + वा → यो वा · "
                   "आ + अ → आ: वा + अल्पाशी → वाऽल्पाशी (छपाई में ऽ)।"),
        "anchors": "पक्का: अल्पाशी, कफ, दीर्घ श्वास, ह्रस्व निश्वास, परिताम्यति। अनुमान: उच्छ्रस्य → उच्छ्वस्य। (मेरी याद-पद्धति)",
    },
    "14": {
        "chunks": "ह्रस्वं च यः प्रश्वसिति | व्याविद्धं स्पंदते भृशं || शिरो विक्षिपते | कृच्छ्रायोऽचयित्वा प्रपाणिकौ",
        "sandhi": "अः + घोष व्यंजन → ओ: शिरः + विक्षिपते → शिरो विक्षिपते · वाक्य में व्यंजन से पहले म् → ं: ह्रस्वम् + च → ह्रस्वं च।",
        "anchors": "पक्का: छोटी साँस, झटके के साथ ज़ोर की फड़कन। अनुमानित पाठ पर: सिर इधर-उधर। टूटा: अचयित्वा प्रपाणिकौ। (मेरी याद-पद्धति)",
    },
    "15": {
        "diagram": {"groups": [
            {"label": "लक्षण (छपे क्रम में)", "items": ["१ ललाटस्रुतस्वेदः: माथे से पसीना", "२ श्लथसंधानबंधनः: संधान-बन्धन ढीले",
                                                   "३ उत्थाप्यमानः संमुह्येत्: उठाने पर मोह"]},
            {"label": "किसके लिए", "items": ["बली दुर्बलोऽपि वा: बली हो या दुर्बल भी"]}]},
        "chunks": "यो ललाटस्रुतस्वेदः | श्लथसंधानबंधनः || उत्थाप्यमानः | संमुह्येद्यो | बली दुर्बलोऽपि वा",
        "sandhi": ("अः + अ → ओऽ: दुर्बलः + अपि → दुर्बलोऽपि · घोष य से पहले त् → द्: संमुह्येत् + यः → संमुह्येद्यः · "
                   "अः + घोष व्यंजन → ओ: यः + बली → यो बली।"),
    },
    "16": {
        "diagram": {"groups": [
            {"label": "लक्षण (छपे क्रम में)", "items": ["१ उत्तानएव स्वपिति: केवल चित सोता", "२ पादौ विकरोति: दोनों पैर विकृत",
                                                   "३ शयनासनकुड्यादौ असदेव जिघृक्षति: जो नहीं है उसे पकड़ना चाहता"]}]},
        "chunks": "उत्तानएव स्वपिति | यः पादौ विकरोति च || शयनासनकुड्यादौ | योऽसदेव जिघृक्षति",
        "sandhi": ("अः + अ → ओऽ: यः + असत् → योऽसत् · स्वर से पहले त् → द्: असत् + एव → असदेव · छपा उत्तानएव: नियमित रूप उत्तान एव "
                   "(अः + अ से भिन्न स्वर → अ, बीच में अन्तर)।"),
    },
    "17": {
        "chunks": "अहास्यहासी | संमुह्यन् | यो लेढि दशनच्छदौ || उत्तरोष्ठं | पेरिलेहन्त्युद्गारांश्च | करोति यः",
        "sandhi": "ह्रस्व स्वर के बाद छ → च्छ: दशन + छद → दशनच्छद · न् + च → ंश्च: उद्गारान् + च → उद्गारांश्च।",
        "anchors": "पक्का: बेबात हँसी, मोह, ओठ चाटना, डकारें। अनुमान: पेरिलेहन्ति → परिलेहति। (मेरी याद-पद्धति)",
    },
    "18": {
        "diagram": {"groups": [
            {"label": "छाया के रंग (छपे क्रम में)", "items": ["१ कृष्णा: काली", "२ पीता: पीली", "३ अरुणा: लालिमा लिए"]},
            {"label": "जिनसे द्वेष (छपे क्रम में)", "items": ["१ भिषग्: वैद्य", "२ भेषज: औषध", "३ पान: पेय", "४ अन्न",
                                                       "५ गुरु: बड़ा या शिक्षक", "६ मित्र"]}]},
        "chunks": "यमभिद्रवति छाया | कृष्णा पीताऽरुणाऽपि वा || भिषग्भेषजपानान्नगुरुमित्रद्विषश्च ये",
        "sandhi": ("घोष भ से पहले ज् → ग्: भिषज् + भेषज → भिषग्भेषज · अ + अ → आ: पान + अन्न → पानान्न · आ + अ → आ: पीता + अरुणा → "
                   "पीताऽरुणा (छपाई में ऽ) · च से पहले विसर्ग → श्: -द्विषः + च → -द्विषश्च।"),
        "pegs": "भि-भे-पा-अ-गु-मि: द्वेष के छह विषयों के पहले अक्षर। (मेरा बनाया स्मरण-सूत्र)",
    },
    "19": {
        "frame": "कौन: सर्वे एव एते (ये सभी) → क्या: वशगाः (वश में गए) → किसके: समवर्तिनः (यम के) → कैसे जानें: विज्ञेयाः (जानने चाहिए)।",
        "chunks": "वशगाः सर्वएवैते | विज्ञेयाः समवर्तिनः || ग्रीवाललाटहृदयं | यस्य स्विद्यति शीतलं",
        "sandhi": "ए + स्वर → अय्, य् का वैकल्पिक लोप: सर्वे + एव → सर्व एव (छपा सर्वएव) · अ + ए → ऐ: एव + एते → एवैते।",
    },
    "20": {
        "diagram": {"groups": [
            {"label": "पहली पंक्ति", "items": ["अपरः प्रदेशः: दूसरा भाग गरम", "शरणं तस्य देवताः: शरण देवता"]},
            {"label": "दूसरी पंक्ति के लक्षण (छपे क्रम में)", "items": ["१ अणुज्योतिः: सूक्ष्म ज्योति", "२ अनेकाग्रः: एकाग्र नहीं",
                                                                 "३ दुश्छायः: बुरी कान्ति", "४ दुर्मनाः सदा: सदा खिन्न मन"]}]},
        "chunks": "उष्णोऽपरः प्रदेशश्च | शरणं तस्य देवताः || योऽणुज्योतिरनेकाग्रो | दुश्छायो | दुर्मनाः सदा",
        "sandhi": ("अः + अ → ओऽ: उष्णः + अपरः → उष्णोऽपरः · च/छ से पहले विसर्ग → श्: प्रदेशः + च → प्रदेशश्च, दुः + छायः → दुश्छायः · "
                   "इः + स्वर → इर्: -ज्योतिः + अनेकाग्रः → -ज्योतिरनेकाग्रः।"),
    },
    "21": {
        "chain": {"steps": ["निर्निमित्तं: बिना कारण", "१ मेधां: बुद्धि", "२ शोभाम्: सुन्दरता", "३ उपचयं: वृद्धि", "४ श्रियं: समृद्धि",
                            "क्रिया प्राप्नोति: कार्ड २२ में"]},
        "chunks": "बलिं बलिभुजो यस्य | प्रणीतं नोपभुंजते || निर्निमित्तं च यो | मेधां शोभामुपचयं श्रियं",
        "sandhi": ("अ + उ → ओ: न + उपभुञ्जते → नोपभुंजते · अः + घोष व्यंजन → ओ: बलिभुजः + यस्य → बलिभुजो यस्य · "
                   "इः + घोष → इर्: निः + निमित्त → निर्निमित्त।"),
        "anchors": "पक्का: बलि न खाई जाए; बिना कारण चार वस्तुएँ। सम्भावित: बलिभुज = कौआ। (मेरी याद-पद्धति)",
    },
    "22": {
        "diagram": {"groups": [
            {"label": "बिना कारण (कार्ड २१ से)", "items": ["मेधा आदि पाना", "अथवा पतन (विभ्रंश; अतो वा दो तरह पढ़ा जाता है)"]},
            {"label": "फल (पाठ के अनुसार)", "items": ["स प्राप्नोति यमक्षयं: यम के घर पहुँचता"]}]},
        "chunks": "प्राप्नोत्यतोवा विभ्रंशं | स प्राप्नोति यमक्षयं || गुणदोषमयी यस्य | स्वस्थस्य व्याधितस्य वा",
        "sandhi": ("इ + भिन्न स्वर → य्: प्राप्नोति + अतः → प्राप्नोत्यतः · अः + घोष व्यंजन → ओ: अतः + वा → अतो वा · "
                   "सः + व्यंजन → स: सः + प्राप्नोति → स प्राप्नोति।"),
        "seesaw": "पाना (प्राप्नोति) ⇄ पतन (विभ्रंशम्): दोनों इसी इकाई की पहली पंक्ति में; दोनों बिना कारण, दोनों का फल यमक्षय।",
    },
    "23": {
        "diagram": {"groups": [
            {"label": "दूसरी पंक्ति के छह (छपे क्रम में)", "items": ["१ भक्ति", "२ शील", "३ स्मृति", "४ त्याग", "५ बुद्धि", "६ बल"]}]},
        "chunks": "यात्यन्यथात्वं प्रकृतिः | षण्मासान्त स जीवति || भक्तिः शीलं स्मृतिस्त्यागो | बुद्धिर्बलमहेतुकं",
        "sandhi": ("इ + भिन्न स्वर → य्: याति + अन्यथात्वम् → यात्यन्यथात्वं · त से पहले विसर्ग → स्: स्मृतिः + त्यागः → स्मृतिस्त्यागः · "
                   "अः + घोष व्यंजन → ओ: त्यागः + बुद्धिः → त्यागो बुद्धिः · इः + घोष → इर्: बुद्धिः + बलम् → बुद्धिर्बलम्।"),
        "anchors": "पक्का: प्रकृति बदले; छह बातें। खुला: ‘षण्मासान्त’ का अर्थ (छह मास नहीं, या छह मास के अन्त तक)। (मेरी याद-पद्धति)",
        "pegs": "भ-शी-स्मृ-त्या-बु-ब: छह बातों के पहले अक्षर। (मेरा बनाया स्मरण-सूत्र)",
    },
}

# ================================================================ IMAGE_SPECS
IMAGE_SPECS = {
    ("13", "seesaw"): {
        "file": "sh10-dirgha-hrasva-13.svg",
        "alt": ("Split of card 13, line 2: long (dīrgham) with the printed ucchrasya, probably ucchvasya, having breathed "
                "in; short (hrasvam) with niśvasya, having breathed out; then he becomes exhausted."),
        "type": "split",
        "title": "कार्ड १३: दीर्घ और ह्रस्व",
        "cols": [["दीर्घम्", ["उच्छ्रस्य (छपा)", "सम्भावित: उच्छ्वस्य", "भीतर साँस लेकर"]],
                 ["ह्रस्वम्", ["निश्वस्य", "बाहर छोड़कर", "फिर परिताम्यति: थकान"]]],
    },
    ("15", "diagram"): {
        "file": "sh10-sveda-15.svg",
        "alt": ("Table of card 15 in printed order: sweat trickling from the forehead; slack joinings and bindings; "
                "bewildered when raised up; whether strong or even weak."),
        "type": "table",
        "title": "कार्ड १५: लक्षण छपे क्रम में",
        "heads": ["क्रम", "लक्षण"],
        "rows": [["१", "माथे से पसीना बहे"], ["२", "संधान और बन्धन ढीले"], ["३", "उठाने पर मोह"],
                 ["किसके लिए", "बली हो या दुर्बल भी"]],
    },
    ("16", "diagram"): {
        "file": "sh10-uttana-16.svg",
        "alt": ("Table of card 16: sleeps only face up; distorts both feet; tries to grasp what is not there on bed, "
                "seat, wall and so on."),
        "type": "table",
        "title": "कार्ड १६: लक्षण छपे क्रम में",
        "heads": ["क्रम", "लक्षण"],
        "rows": [["१", "केवल चित सोता"], ["२", "दोनों पैर विकृत करता"], ["३", "जो नहीं है उसे पकड़ना चाहता"],
                 ["कहाँ", "शय्या, आसन, दीवार आदि पर"]],
    },
    ("18", "diagram"): {
        "file": "sh10-dvesha-18.svg",
        "alt": ("Table of card 18 in printed order: the six things hated: physician, medicine, drink, food, elder or "
                "teacher, friend."),
        "type": "table",
        "title": "कार्ड १८: जिनसे द्वेष",
        "heads": ["क्रम", "विषय"],
        "rows": [["१", "भिषग्: वैद्य"], ["२", "भेषज: औषध"], ["३", "पान: पेय"], ["४", "अन्न"],
                 ["५", "गुरु: बड़ा या शिक्षक"], ["६", "मित्र"]],
    },
    ("20", "diagram"): {
        "file": "sh10-anujyoti-20.svg",
        "alt": ("Table of card 20, line 2 in printed order: of small light; not one-pointed; ill-lustred; always "
                "low-spirited."),
        "type": "table",
        "title": "कार्ड २०: दूसरी पंक्ति के लक्षण",
        "heads": ["क्रम", "लक्षण"],
        "rows": [["१", "अणुज्योतिः: सूक्ष्म ज्योति"], ["२", "अनेकाग्रः: एकाग्र नहीं"], ["३", "दुश्छायः: बुरी कान्ति"],
                 ["४", "दुर्मनाः सदा: सदा खिन्न मन"]],
    },
    ("21", "chain"): {
        "file": "sh10-medha-21.svg",
        "alt": ("Chain of card 21, line 2 in printed order: without cause; intellect; beauty; growth; prosperity; the "
                "verb obtains is in card 22."),
        "type": "chain",
        "title": "कार्ड २१: बिना कारण, छपे क्रम में",
        "steps": ["निर्निमित्तं: बिना कारण", "१ मेधा: बुद्धि", "२ शोभा: सुन्दरता", "३ उपचय: वृद्धि", "४ श्री: समृद्धि",
                  "क्रिया प्राप्नोति: कार्ड २२ में"],
    },
    ("22", "diagram"): {
        "file": "sh10-yamakshaya-22.svg",
        "alt": ("Flowchart of card 22: without cause (from card 21), obtaining intellect and the rest, or a falling away "
                "(vibhraṃśa), both lead to: he reaches the abode of Yama."),
        "type": "mermaid",
        "code": ("flowchart TD\n"
                 "  A[\"बिना कारण (कार्ड २१)\"] --> B[\"मेधा आदि पाना\"]\n"
                 "  A --> C[\"अथवा पतन (विभ्रंश)\"]\n"
                 "  B --> D[\"यमक्षय: यम का घर\"]\n"
                 "  C --> D\n"),
    },
    ("23", "diagram"): {
        "file": "sh10-shad-guna-23.svg",
        "alt": ("Table of card 23, line 2 in printed order: devotion, character, memory, giving up, intellect, "
                "strength."),
        "type": "table",
        "title": "कार्ड २३: दूसरी पंक्ति के छह",
        "heads": ["क्रम", "विषय"],
        "rows": [["१", "भक्ति"], ["२", "शील: स्वभाव, आचरण"], ["३", "स्मृति"], ["४", "त्याग"], ["५", "बुद्धि"], ["६", "बल"]],
    },
}
