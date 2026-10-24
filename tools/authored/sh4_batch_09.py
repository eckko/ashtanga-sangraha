from helpers import mcq, match, order, fill, multi, accepts


AUTHORED = {}

# ---------------------------------------------------------------- unit 109
AUTHORED["109"] = {
    "title": "जघनशक्तस्य जघनकपालानि दारयित्वेति",
    "question": "By unit 109, what is broken in the case at the jaghana (hip region), and how does the line end?",
    "rule": ("For the one stuck (printed शक्त, read सक्त) at the jaghana (hip region): having broken (दारयित्वा) the "
             "jaghana-kapāla, the bones of the hip region. इति closes the list of cases; 'should extract' is carried "
             "from unit 108."),
    "limits": ("Elliptical prose line with no verb; it appears to continue unit 108, whence 'should extract'. 'Stuck' "
               "rests on reading printed शक्त (able) as सक्त (a possible correction): no question rests on that word. "
               "Pelvic bones is only probable. No instrument is named."),
    "explain_hi": ("यह गद्य-पंक्ति मूढगर्भ निकालने की स्थितियों की सूची का अन्तिम अंश है। "
                   "जो जघन यानी कूल्हे के प्रदेश में अटका हो (छपा ‘शक्त’, पढ़ा गया ‘सक्त’ = अटका), उसके जघन-कपाल यानी "
                   "जघन की हड्डियों को तोड़कर (दारयित्वा)। "
                   "क्रिया ‘निकाले’ यहाँ छपी नहीं; डेटा के अनुसार वह इकाई १०८ से समझी जाती है, जिसे यह पंक्ति सम्भवतः आगे बढ़ाती है। "
                   "जघन-कपाल का अर्थ श्रोणि की हड्डियाँ होना केवल सम्भावित है। "
                   "अन्त का ‘इति’ स्थितियों की सूची को बन्द करता है।"),
    "hook": "जघन में अटका: जघन-कपाल तोड़कर; ‘इति’ से सूची पूरी।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 109, what is to be broken (दारयित्वा)?",
            ("The bones of the hip region", "जघनकपालानि दारयित्वा: having broken the jaghana-kapāla, the hip-region bones."),
            [("The pieces of the skull bones", "Removing the skull pieces (शिरःकपाल) is unit 106, not this line."),
             ("The arm at the shoulder region", "Cutting the arm at the shoulder is unit 108, not this line."),
             ("The belly that is full of wind", "Splitting the wind-filled belly is unit 108, not this line.")],
            "The jaghana-kapāla, the bones of the hip region, are broken.",
            "जघनकपालानि दारयित्वा = having broken the hip-region bones."),
        order(1, "Put the words of unit 109 in the line's order.",
              ["जघनशक्तस्य", "जघनकपालानि", "दारयित्वा", "इति"],
              "For the one stuck at the hips, the hip-region bones, having broken; thus (the list ends).",
              "जघनशक्तस्य → जघनकपालानि → दारयित्वा → इति."),
        match(2, "Match each word of unit 109 to its meaning.",
              [["जघन", "hip region"], ["कपाल", "plate, bone"], ["दारयित्वा", "having split, broken"],
               ["इति", "thus (closes the list)"]],
              "Jaghana is the hip region; its kapāla are its bones; दारयित्वा = having broken them; इति ends the list.",
              "जघन, कपाल, दारयित्वा, इति.", role="extend",
              teaches=("कपाल = a plate or bone, as in the skull pieces (शिरःकपाल) of unit 106; jaghana-kapāla = the bones "
                       "of the hip region (probably the pelvic bones).")),
        mcq("discriminate", 3, "Which split of दारयित्वेति is right?",
            ("दारयित्वा + इति", "आ + इ → ए: दारयित्वा + इति → दारयित्वेति."),
            [("दारयित्वे + इति", "ए + इ would give दारयित्वयिति or दारयित्व इति, not दारयित्वेति."),
             ("दारयित् + वेति", "दारयित् is not a form; the absolutive ends in -त्वा: दारयित्वा."),
             ("दारयित्वः + इति", "अः + इ would drop the visarga and leave a gap: दारयित्व इति.")],
            "दारयित्वा (having broken) + इति (thus): आ + इ → ए.",
            "आ + इ → ए."),
        multi("apply", 4, "Which statements about unit 109 are right by the card?",
              [("The line has its own verb 'should extract'", "No: the verb is not printed; it is carried from unit 108."),
               ("इति closes the list of cases", "Right: the data says the closing इति ends the list."),
               ("The line names the cutting instrument", "No instrument is named in unit 109."),
               ("Jaghana-kapāla as the pelvic bones is only probable", "Right: the data labels it probable.")],
              [1, 3],
              "इति ends the list; the pelvic-bone sense is probable only; the verb comes from unit 108.",
              "जघनकपालानि दारयित्वा इति: no verb, a closing इति."),
        mcq("transfer", 5, "By the rule of दारयित्वेति, how is महा + इन्द्रः (great Indra) joined?",
            ("महेन्द्रः", "आ + इ → ए, as दारयित्वा + इति → दारयित्वेति."),
            [("महैन्द्रः", "ऐ comes from अ or आ + ए or ऐ, not + इ."),
             ("महिन्द्रः", "No short इ results; आ + इ give ए."),
             ("महान्द्रः", "The इ is not lost; आ + इ merge into ए.")],
            "महा + इन्द्रः = महेन्द्रः, like दारयित्वा + इति = दारयित्वेति.",
            "आ + इ → ए.",
            teaches="A final आ followed by इ joins as ए: दारयित्वा + इति → दारयित्वेति."),
    ],
}

# ---------------------------------------------------------------- unit 110
AUTHORED["110"] = {
    "title": "भवंति चात्र",
    "question": "By unit 110, what does the formula भवन्ति चात्र do?",
    "rule": ("भवन्ति च अत्र, 'and on this there are': a formula that introduces the lines that follow. The noun "
             "('verses') is understood, not printed."),
    "limits": ("A formula only: it names no noun and gives no teaching of its own. 'Verses' is the usual understood word "
               "and is not in the Sanskrit. A prose line."),
    "explain_hi": ("यह छोटी गद्य-पंक्ति एक सूत्र-वाक्य है: भवन्ति च अत्र, यानी ‘और इस विषय में ये हैं’। "
                   "इससे आगे आने वाली पंक्तियों का आरम्भ होता है। "
                   "‘श्लोक’ जैसा संज्ञा-शब्द छपा नहीं, केवल समझा जाता है। "
                   "भवन्ति (√भू, वर्तमान, प्रथम पुरुष बहुवचन) = हैं; चात्र = च + अत्र।"),
    "hook": "भवन्ति चात्र: अब आगे की पंक्तियाँ।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 110, what does भवन्ति चात्र introduce?",
            ("The verses that follow", "The data: a formula introducing the verses that follow ('verses' understood)."),
            [("The name of the teacher", "No teacher is named in this formula."),
             ("A new chapter of the book", "No chapter opens here; the formula introduces lines within this chapter."),
             ("The list of the drugs", "The formula names no drug; it only introduces what follows.")],
            "It introduces the verses that follow; the noun itself is understood.",
            "भवन्ति च अत्र = and on this there are (verses)."),
        mcq("warmup", 1, "In भवन्ति चात्र, which word is understood but not printed?",
            ("The noun 'verses'", "Right: 'verses' is the usual understood noun; it is not in the Sanskrit."),
            [("The verb 'there are'", "The verb is printed: भवन्ति."),
             ("The word 'and'", "'And' is printed: च, inside चात्र."),
             ("The word 'here'", "'Here, on this' is printed: अत्र, inside चात्र.")],
            "Only the noun 'verses' is supplied; भवन्ति, च and अत्र are all printed.",
            "भवन्ति च अत्र [श्लोकाः, understood]."),
        match(2, "Match each word of unit 110 to its meaning.",
              [["भवन्ति", "there are (3rd plural present)"], ["च", "and"], ["अत्र", "here, on this"]],
              "भवन्ति = there are; च = and; अत्र = on this.",
              "भवन्ति, च, अत्र.", role="extend",
              teaches="भवन्ति is plural, so the understood noun is plural too: (verses)."),
        mcq("discriminate", 3, "Which split of चात्र is right?",
            ("च + अत्र", "अ + अ → आ: च + अत्र → चात्र."),
            [("चे + अत्र", "ए + अ would give चेऽत्र, with ए kept and ऽ."),
             ("चः + अत्र", "अः + अ would give चोऽत्र, not चात्र."),
             ("चा + त्र", "चा and त्र are not the words; the particle is च and the adverb is अत्र.")],
            "च (and) + अत्र (here): अ + अ → आ.",
            "अ + अ → आ."),
        multi("apply", 4, "Which statements about unit 110 are right by the card?",
              [("भवन्ति is a plural verb", "Right: 3rd person plural present of √भू."),
               ("The formula gives a treatment", "No: it only introduces what follows."),
               ("The noun 'verses' is understood, not printed", "Right: the data shows it in brackets."),
               ("अत्र means 'there, far away'", "No: अत्र = here, on this.")],
              [0, 2],
              "A plural verb with an understood plural noun; no teaching of its own.",
              "भवन्ति (pl.) च अत्र [verses]."),
        mcq("transfer", 5, "By the rule of चात्र, how is तत्र + अपि (there too) joined?",
            ("तत्रापि", "अ + अ → आ, as च + अत्र → चात्र."),
            [("तत्रोपि", "ओ comes from अ + उ, not from अ + अ."),
             ("तत्रेपि", "ए comes from अ + इ, not from अ + अ."),
             ("तत्रपि", "The two अ do not shrink to one short अ; they give long आ.")],
            "तत्र + अपि = तत्रापि, like च + अत्र = चात्र.",
            "अ + अ → आ.",
            teaches="A short अ followed by a short अ joins as long आ: च + अत्र → चात्र."),
    ],
}

# ---------------------------------------------------------------- unit 111
AUTHORED["111"] = {
    "title": "यद्यद्वायुवशादंगं सज्जेद्गर्भस्य खंडशः",
    "question": "By unit 111, what is done with a limb of the fetus that gets stuck, and whom must one protect?",
    "rule": ("Whatever limb (अङ्ग) of the fetus gets stuck (सज्जेत्) by the power of vāyu, having cut that and that "
             "(तत्तत् छित्वा), one should remove it properly (सम्यक्) and protect the mother (जननी) from injury (क्षततः)."),
    "limits": ("Whether खण्डशः (piecemeal) goes with 'gets stuck' or with the cutting is open: no question rests on it. "
               "Vāyu is plain wind here (data). The instrument and the way of cutting are not named. The two printed lines "
               "are one sentence (यत् यत् ... तत् तत्)."),
    "explain_hi": ("ये दो छपी पंक्तियाँ एक ही वाक्य हैं: गर्भ का जो-जो अंग (यद्यत् अङ्गम्) वायु के वश अटक जाए (सज्जेत्), "
                   "उस-उस को (तत्तत्) काटकर भली प्रकार (सम्यक्) निकाले (हरेत्), और माता (जननी) को चोट से (क्षततः) बचाए (रक्षेत्)। "
                   "‘खण्डशः’ (टुकड़े-टुकड़े) अटकने से जुड़ा है या काटने से, यह खुला है; डेटा उसे सम्भवतः काटने से जोड़ता है। "
                   "यहाँ ‘वायु’ साधारण वायु है। "
                   "शस्त्र या काटने की विधि का नाम नहीं दिया गया।"),
    "hook": "जो अंग अटके, वही काटो; पर माँ को चोट न लगे।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 111, whom should one protect from injury?",
            ("The mother", "रक्षेज्जननीं च क्षततः: and one should protect the mother from injury."),
            [("The physician himself", "The physician is the one who acts; the line protects the mother."),
             ("The attending women", "No attendants are named in unit 111."),
             ("The cut-off limb", "The stuck limb is cut and removed, not protected.")],
            "The mother (जननी) is to be protected from injury.",
            "रक्षेत् जननीम् क्षततः."),
        order(1, "Put these phrases of unit 111 in the printed order.",
              ["यद्यद्वायुवशादंगं", "सज्जेद्गर्भस्य खंडशः", "तत्तच्छित्वा", "हरेत्सम्यग्", "रक्षेज्जननीं च क्षततः"],
              "Whatever limb, by the power of vāyu, of the fetus gets stuck, piecemeal; having cut that and that, remove it properly, and protect the mother from injury.",
              "यद्यद्वायुवशादंगं → सज्जेद्गर्भस्य खंडशः → तत्तच्छित्वा → हरेत्सम्यग् → रक्षेज्जननीं च क्षततः."),
        match(2, "Match each word of unit 111 to its meaning.",
              [["अङ्ग", "limb"], ["सज्जेत्", "should get stuck"], ["छित्वा", "having cut"],
               ["सम्यक्", "properly"], ["जननी", "mother"], ["क्षततः", "from injury"]],
              "A stuck limb is cut and properly removed, and the mother is guarded from injury.",
              "अङ्ग, सज्जेत्, छित्वा, सम्यक्, जननी, क्षततः.", role="extend",
              teaches="यद्यत् ... तत्तत् = whatever ... that and that: each such limb is cut and removed."),
        mcq("discriminate", 3, "Which split of तत्तच्छित्वा is right?",
            ("तत् + तत् + छित्वा", "त् + छ → च्छ: तत् + छित्वा → तच्छित्वा."),
            [("तत् + तत् + चित्वा", "त् + च gives च्च: तच्चित्वा, not तच्छित्वा."),
             ("तत्त + च्छित्वा", "तत्त is not a word; the pronoun तत् is said twice."),
             ("ततः + तत् + छित्वा", "ततः before त would give ततस्तत्, not तत्तत्.")],
            "तत् तत् (that and that) + छित्वा (having cut; spelling of छित्त्वा): त् + छ → च्छ.",
            "त् + छ → च्छ."),
        mcq("apply", 4, "A limb of the fetus is stuck by vāyu. What does unit 111 tell the physician?",
            ("Cut it away, protecting the mother", "तत्तच्छित्वा हरेत् ... रक्षेज्जननीम्: cut, remove, guard the mother."),
            [("Wait until the vāyu frees the limb", "The line does not say to wait; it says to cut and remove."),
             ("Pull the whole fetus out in one piece", "The line says to cut the stuck limb, not to pull it whole."),
             ("Leave it be, attend only to the mother", "The limb is to be cut and removed, and the mother guarded.")],
            "Cut the stuck limb, remove it properly, and protect the mother from injury.",
            "छित्वा हरेत् सम्यक्, रक्षेत् जननीम्."),
        mcq("transfer", 5, "By the rule of रक्षेज्जननीम् (रक्षेत् + जननीम्), how is पठेत् + जनः joined?",
            ("पठेज्जनः", "त् + ज → ज्ज, as रक्षेत् + जननीम् → रक्षेज्जननीम्."),
            [("पठेद्जनः", "Before ज the त् does not stop at द्; it becomes ज्."),
             ("पठेत्जनः", "त् does not stay unchanged before ज."),
             ("पठेञ्जनः", "ञ् is a nasal; before ज the त् becomes ज्, not a nasal.")],
            "पठेत् + जनः = पठेज्जनः, like रक्षेत् + जननीम् = रक्षेज्जननीम्.",
            "त् + ज → ज्ज.",
            teaches="A final त् before ज becomes ज्: रक्षेत् + जननीम् → रक्षेज्जननीम्."),
    ],
}

# ---------------------------------------------------------------- unit 112
AUTHORED["112"] = {
    "title": "अथापतंतीमपरां पातयेत्पूर्ववद्भिषक्",
    "question": "By unit 112, what does the physician do with the aparā (placenta), and then with the woman?",
    "rule": ("Then the physician (भिषक्) should make the aparā (placenta, standard) fall (पातयेत्) as before (पूर्ववत्); "
             "thus, her from whom the śalya has been drawn out (निर्हृतशल्याम्), he should sprinkle (सिञ्चेत्) with warm water."),
    "limits": ("'As before' points to an earlier procedure that the unit does not name. Śalya is not defined here (the "
               "context suggests the retained fetus or placenta; not stated). The letters अथापतन्तीम् also allow "
               "आपतन्तीम्; the data reads अपतन्तीम्, 'not falling'. No question rests on these."),
    "explain_hi": ("यह श्लोक प्रसव के बाद की दो क्रियाएँ कहता है। "
                   "पहले, वैद्य (भिषक्) अपरा यानी जेर (मानक) को पहले की तरह (पूर्ववत्) गिराए (पातयेत्); डेटा उसे ‘न गिरती हुई’ "
                   "(अपतन्तीम्) पढ़ता है। "
                   "फिर, इस प्रकार जिसका शल्य निकाल दिया गया हो (निर्हृतशल्याम्, स्त्रीलिंग), उस स्त्री को गरम जल से (उष्णेन वारिणा) "
                   "सींचे (सिञ्चेत्)। "
                   "‘पूर्ववत्’ किस पहले की विधि को कहता है, और ‘शल्य’ यहाँ क्या है, यह पंक्ति नहीं बताती।"),
    "hook": "जेर न गिरे तो गिराओ; फिर गरम जल से सिंचन।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 112, with what is the woman sprinkled?",
            ("With warm water", "सिञ्चेदुष्णेन वारिणा: should sprinkle with warm water."),
            [("With cold water", "The water is warm (उष्णेन), not cold."),
             ("With warm milk", "The line names water (वारि), not milk."),
             ("With oil and ghee", "Oil and ghee are not named in unit 112.")],
            "She is sprinkled with warm water.",
            "सिञ्चेत् उष्णेन वारिणा."),
        order(1, "Put the quarters of the verse in unit 112 in order.",
              ["अथापतंतीमपरां", "पातयेत्पूर्ववद्भिषक्", "एवं निर्हृतशल्यां च", "सिंचेदुष्णेन वारिणा"],
              "Then the placenta not falling, the physician should make fall as before; and thus her from whom the śalya is drawn out, he should sprinkle with warm water.",
              "अथापतंतीमपरां → पातयेत्पूर्ववद्भिषक् → एवं निर्हृतशल्यां च → सिंचेदुष्णेन वारिणा."),
        match(2, "Match each word of unit 112 to its meaning.",
              [["अपरा", "placenta, afterbirth"], ["पातयेत्", "should cause to fall"], ["पूर्ववत्", "as before"],
               ["भिषक्", "physician"], ["वारि", "water"]],
              "The physician makes the placenta fall as before, then sprinkles the woman with warm water.",
              "अपरा, पातयेत्, पूर्ववत्, भिषक्, वारि.", role="extend",
              teaches="पातयेत् is the causative of √पत् (fall): 'should make (it) fall'."),
        mcq("discriminate", 3, "Which split of पूर्ववद्भिषक् is right?",
            ("पूर्ववत् + भिषक्", "त् before a voiced sound becomes द्: पूर्ववत् + भिषक् → पूर्ववद्भिषक्."),
            [("पूर्व + वद्भिषक्", "वद्भिषक् is not a word; the words are पूर्ववत् (as before) and भिषक्."),
             ("पूर्ववः + भिषक्", "अः before a voiced sound would give पूर्ववो भिषक्."),
             ("पूर्ववत् + अभिषक्", "A following vowel would give पूर्ववदभिषक्, with अ.")],
            "पूर्ववत् (as before) + भिषक् (physician): त् + voiced sound → द्.",
            "त् + voiced sound → द्."),
        multi("apply", 4, "Which statements about unit 112 are right by the card?",
              [("The physician is the subject", "Right: भिषक् is the nominative subject of पातयेत्."),
               ("The unit names the earlier procedure meant by 'as before'", "No: the unit does not say which procedure."),
               ("The unit defines śalya here as the placenta", "No: śalya is not defined; the context only suggests."),
               ("The one sprinkled is a woman", "Right: the feminine accusative निर्हृतशल्याम् shows the woman.")],
              [0, 3],
              "The physician acts; the woman (feminine accusative) is sprinkled; 'as before' and śalya stay open.",
              "भिषक् पातयेत्; निर्हृतशल्याम् सिञ्चेत्."),
        mcq("transfer", 5, "By the rule of सिञ्चेदुष्णेन (सिञ्चेत् + उष्णेन), how is पिबेत् + उदकम् joined?",
            ("पिबेदुदकम्", "त् before a vowel becomes द्, as सिञ्चेत् + उष्णेन → सिञ्चेदुष्णेन."),
            [("पिबेतुदकम्", "Before a vowel the त् does not stay unvoiced; it becomes द्."),
             ("पिबेदूदकम्", "The उ of उदकम् stays short; nothing lengthens it."),
             ("पिबेच्चुदकम्", "च्च arises before च, not before a vowel.")],
            "पिबेत् + उदकम् = पिबेदुदकम्, like सिञ्चेत् + उष्णेन = सिञ्चेदुष्णेन.",
            "त् + vowel → द्.",
            teaches="A final त् before a vowel becomes द्: सिञ्चेत् + उष्णेन → सिञ्चेदुष्णेन."),
    ],
}

# ---------------------------------------------------------------- unit 113
AUTHORED["113"] = {
    "title": "दद्यादभ्यक्तदेहायै योनौ स्नेहपिचुं ततः",
    "question": "By unit 113, what is placed in the yoni, and what follows from it?",
    "rule": ("Then, to her whose body has been anointed (अभ्यक्तदेहायै), one should give a swab of sneha (oil or fat; "
             "स्नेहपिचु) in the yoni (vagina). By that (तेन) the yoni becomes soft (मृदुः) and her pain (शूल) subsides."),
    "limits": ("The kind of sneha and the material of the swab are not stated; no amount or duration. मृदुः is a "
               "masculine form beside feminine योनिः (allowed in a predicate): no question on its gender."),
    "explain_hi": ("यह श्लोक प्रसूता की आगे की परिचर्या कहता है। "
                   "जिसके शरीर पर अभ्यंग हो चुका हो (अभ्यक्तदेहायै), उसे तब (ततः) योनि में स्नेह यानी तेल या वसा का पिचु यानी फाहा दे। "
                   "उस फाहे से (तेन) योनि मृदु हो जाती है और उसकी पीड़ा (शूल) शान्त होती है (प्रशाम्यति)। "
                   "स्नेह किस प्रकार का हो और फाहा किससे बना हो, यह नहीं कहा गया। "
                   "‘मृदुः’ रूप में पुंलिंग है, जबकि ‘योनिः’ स्त्रीलिंग; विधेय में यह प्रयोग चलता है।"),
    "hook": "अभ्यंग के बाद स्नेह-पिचु: योनि मृदु, शूल शान्त।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 113, what is placed in the yoni?",
            ("A swab of oil or fat", "योनौ स्नेहपिचुम्: a swab of sneha (oil or fat) in the yoni."),
            [("A cloth soaked in milk", "Milk and cloth are not named in unit 113."),
             ("A powder of rock salt", "No powder or salt is named in unit 113."),
             ("A pad of dry cotton", "The swab is of sneha, not dry; its material is not stated.")],
            "A swab (picu) of sneha (oil or fat).",
            "योनौ स्नेहपिचुं दद्यात्."),
        order(1, "Put the quarters of the verse in unit 113 in order.",
              ["दद्यादभ्यक्तदेहायै", "योनौ स्नेहपिचुं ततः", "योनिर्मृदुर्भवेत्तेन", "शूलं चास्याः प्रशाम्यति"],
              "One should give, to her whose body is anointed, in the yoni a swab of sneha, then; by that the yoni becomes soft, and her pain subsides.",
              "दद्यादभ्यक्तदेहायै → योनौ स्नेहपिचुं ततः → योनिर्मृदुर्भवेत्तेन → शूलं चास्याः प्रशाम्यति."),
        match(2, "Match each word of unit 113 to its meaning.",
              [["अभ्यक्त", "anointed"], ["पिचु", "swab"], ["स्नेह", "oil or fat"], ["मृदु", "soft"],
               ["शूल", "pain"]],
              "After anointing, a swab of sneha makes the yoni soft and the pain subside.",
              "अभ्यक्त, पिचु, स्नेह, मृदु, शूल.", role="extend",
              teaches="अभ्यक्तदेहायै is a bahuvrīhi in the dative: 'to her whose body is anointed'."),
        mcq("discriminate", 3, "Which split of योनिर्मृदुर्भवेत् is right?",
            ("योनिः + मृदुः + भवेत्", "A visarga after इ or उ becomes र् before a voiced sound: योनिर्, मृदुर्."),
            [("योनी + मृदू + भवेत्", "Long ई and ऊ give no र्; the र् comes from a visarga."),
             ("योनिम् + मृदुम् + भवेत्", "म् before a consonant would be written ं: योनिं मृदुं."),
             ("योने + मृदो + भवेत्", "ए and ओ before a consonant stay as they are; no र् would appear.")],
            "योनिः (the yoni) + मृदुः (soft) + भवेत् (becomes): इः, उः + voiced sound → इर्, उर्.",
            "इः / उः + voiced sound → इर् / उर्."),
        mcq("apply", 4, "By unit 113, what two results come from the swab?",
            ("Soft yoni, and her pain subsides", "योनिर्मृदुर्भवेत्तेन शूलं चास्याः प्रशाम्यति."),
            [("The placenta falls and fever goes", "Neither result is said of the swab in unit 113."),
             ("The fetus turns and comes out", "The swab follows delivery; no turning is named."),
             ("Her skin glows and she gains weight", "Skin and weight are not named in unit 113.")],
            "By the swab the yoni becomes soft and her pain subsides.",
            "तेन योनिः मृदुः, शूलं प्रशाम्यति."),
        mcq("transfer", 5, "By the rule of मृदुर्भवेत् (मृदुः + भवेत्), how is गुरुः + वदति (the teacher speaks) joined?",
            ("गुरुर्वदति", "A visarga after उ before a voiced sound becomes र्, as मृदुः + भवेत् → मृदुर्भवेत्."),
            [("गुरू वदति", "The visarga drops with lengthening only before र्, not before व."),
             ("गुरुश्वदति", "A visarga becomes श् before च or छ (optionally before श), not before व."),
             ("गुरुः वदति", "Before a voiced sound the visarga after उ does not stay; it becomes र्.")],
            "गुरुः + वदति = गुरुर्वदति, like मृदुः + भवेत् = मृदुर्भवेत्.",
            "उः + voiced sound → उर्.",
            teaches="A visarga after a vowel other than अ/आ becomes र् before a voiced sound: मृदुः + भवेत् → मृदुर्भवेत्."),
    ],
}

# ---------------------------------------------------------------- unit 114
AUTHORED["114"] = {
    "title": "दीप्यकातिविषा रास्त्रा हिं ग्वेलापंचकोलकान्",
    "question": "By unit 114, which drugs are listed, and in what forms is she made to drink them?",
    "rule": ("Dīpyaka (probably ajwain), ativiṣā (atis), rāsnā (conjectural reading), hiṅgu, elā and the pañcakolaka "
             "group: one should make her drink these as powder (चूर्ण) with sneha, or as kalka (paste), or as decoction "
             "(printed काथ), likewise."),
    "limits": ("Rāsnā is a conjectural reading of printed रास्त्रा (disputed); हिं | ग्वेला is read हिङ्गु + एला and "
               "काथ as क्वाथ (possible repairs). No question builds on these (one only asks that rāsnā is conjectural). "
               "The pañcakolaka's five are not named; no preferred form or dose."),
    "explain_hi": ("यह श्लोक औषधों की एक सूची और उन्हें देने के रूप बताता है। "
                   "दीप्यक यानी सम्भवतः अजवायन, अतिविषा यानी अतीस (मानक), अनुमानित पाठ पर रास्ना (पहचान विवादित), हींग, एला यानी "
                   "छोटी इलायची (मानक), और पञ्चकोलक यानी पाँच का समूह, जिसके सदस्य इस पंक्ति में नाम से नहीं दिए गए। "
                   "इनका चूर्ण स्नेह यानी तेल या वसा के साथ, या कल्क यानी लुगदी, या क्वाथ यानी काढ़ा (छपा ‘काथ’) उसी प्रकार पिलाए। "
                   "कौन-सा रूप उत्तम है, यह नहीं कहा गया; इनका प्रयोजन अगली इकाई (११५) में आता है।"),
    "hook": "अजवायन, अतीस, हींग, इलायची, पंचकोल: चूर्ण, कल्क या काढ़ा।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 114, with what is the powder (चूर्ण) to be taken?",
            ("With sneha (oil, fat)", "चूर्णं स्नेहेन: the powder with sneha, oil or fat."),
            [("With warm water (vāri)", "Water is not named in unit 114."),
             ("With fresh milk (payas)", "Milk is not named in unit 114."),
             ("With honey (madhu)", "Honey is not named in unit 114.")],
            "The powder is given with sneha (oil or fat).",
            "चूर्णम् स्नेहेन."),
        order(1, "Put these printed pieces of unit 114 in order.",
              ["दीप्यकातिविषा", "रास्त्रा", "हिं ग्वेलापंचकोलकान्", "चूर्णं स्नेहेन", "कल्कं वा काथं वा", "पाययेत्तथा"],
              "Dīpyaka, ativiṣā, rāsnā (printed रास्त्रा), hiṅgu, elā, the pañcakolakas; powder with sneha, or paste, or decoction; one should make her drink likewise.",
              "दीप्यकातिविषा → रास्त्रा → हिं ग्वेलापंचकोलकान् → चूर्णं स्नेहेन → कल्कं वा काथं वा → पाययेत्तथा."),
        match(2, "Match each name of unit 114 to the card's identification.",
              [["दीप्यक", "ajwain (probable)"], ["अतिविषा", "atis (standard)"], ["एला", "small cardamom (standard)"],
               ["पञ्चकोलक", "a group of five (not named here)"], ["कल्क", "paste"]],
              "Plant names keep the data's labels; pañcakolaka is a group whose members this line does not name.",
              "दीप्यक, अतिविषा, एला, पञ्चकोलक, कल्क.", role="extend",
              teaches="Dīpyaka is only probably ajwain; ativiṣā and elā are standard identifications."),
        mcq("discriminate", 3, "Which split of दीप्यकातिविषा is right?",
            ("दीप्यक + अतिविषा", "अ + अ → आ: दीप्यक + अतिविषा → दीप्यकातिविषा."),
            [("दीप्यकः + अतिविषा", "अः + अ would give दीप्यकोऽतिविषा."),
             ("दीप्यकी + अतिविषा", "ई + अ would give दीप्यक्यतिविषा."),
             ("दीप्य + कातिविषा", "कातिविषा is not a drug name; the names are दीप्यक and अतिविषा.")],
            "दीप्यक + अतिविषा: अ + अ → आ.",
            "अ + अ → आ."),
        multi("apply", 4, "Which statements about unit 114 are right by the card?",
              [("Rāsnā here rests on a conjectural reading", "Right: printed रास्त्रा is read रास्ना on a conjecture."),
               ("The line names the five members of the pañcakolaka", "No: the five are not named in this line."),
               ("The line does not say which form is preferred", "Right: powder, paste or decoction, none preferred."),
               ("Dīpyaka as ajwain is a standard identification", "No: the data labels it probable.")],
              [0, 2],
              "Rāsnā is conjectural, the pañcakolaka members are unnamed, no form is preferred, dīpyaka is probable.",
              "Labels and readings exactly as the data gives them."),
        mcq("transfer", 5, "By the rule of चूर्णं स्नेहेन, how is जलम् + पिबेत् (should drink water) written in a sentence?",
            ("जलं पिबेत्", "A final म् before a consonant is written ं, as चूर्णम् + स्नेहेन → चूर्णं स्नेहेन."),
            [("जलो पिबेत्", "ओ comes from अः before a voiced sound, not from अम्."),
             ("जला पिबेत्", "The म् is not dropped with a lengthened vowel."),
             ("जलः पिबेत्", "The ending is म्, not a visarga.")],
            "जलम् + पिबेत् = जलं पिबेत्, like चूर्णम् + स्नेहेन = चूर्णं स्नेहेन.",
            "म् + consonant → ं.",
            teaches="Inside a sentence a final म् before a consonant is written as anusvāra: चूर्णं स्नेहेन."),
    ],
}

# ---------------------------------------------------------------- unit 115
AUTHORED["115"] = {
    "title": "कटुकातिविषापाठाशाकत्वग्घिगुतेजनीः",
    "question": "By unit 115, which further drugs are listed, and for what two purposes?",
    "rule": ("Kaṭukā (kutki), ativiṣā (atis), pāṭhā (probably velvetleaf), śāka bark (probably teak), hiṅgu "
             "(conjectural) and tejanī (disputed), given likewise (तद्वत्): for the flowing off of the doṣa and for the "
             "relief of pain (वेदनोपशमाय)."),
    "limits": ("No verb (carried from unit 114). शाकत्वक् may be one item or two; हिङ्गु is a conjectural reading of "
               "printed घिगु; tejanī is disputed; दोषस्यन्दार्थम् is uncertain and names no doṣa. No question builds on "
               "these (one only asks that they are open)."),
    "explain_hi": ("यह श्लोक दूसरी औषध-सूची और प्रयोजन देता है। "
                   "कटुका यानी कुटकी (मानक), अतिविषा यानी अतीस, पाठा यानी सम्भवतः अकनादि, शाक यानी सम्भवतः सागौन की छाल, "
                   "अनुमानित पाठ पर हींग (छपा ‘घिगु’), और तेजनी जिसकी पहचान विवादित है। "
                   "इन्हें उसी प्रकार (तद्वत्) दे: दोष के बह निकलने के लिए और वेदना की शान्ति के लिए (वेदनोपशमाय)। "
                   "क्रिया ‘पिलाए’ इकाई ११४ से आती है। ‘शाकत्वक्’ एक द्रव्य है या दो (शाक और त्वक्), यह तय नहीं।"),
    "hook": "कुटकी, अतीस, पाठा...: दोष बहे, वेदना शमे।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 115, which purpose is stated in the line?",
            ("Relief of pain", "वेदनोपशमाय: for the relief of pain."),
            [("Stopping of bleeding", "Bleeding is not named in unit 115."),
             ("Growth of the fetus", "Growth of the fetus is not named in unit 115."),
             ("Easy sleep at night", "Sleep is not named in unit 115.")],
            "One stated purpose is the relief of pain.",
            "वेदना + उपशमाय = for the relief of pain."),
        order(1, "Put these printed pieces of unit 115 in order.",
              ["कटुकातिविषापाठा", "शाकत्वग्घिगु", "तेजनीः", "तद्वच्च", "दोषस्यंदार्थं", "वेदनोपशमायच"],
              "Kaṭukā, ativiṣā, pāṭhā, śāka bark, hiṅgu (printed घिगु), tejanī; and likewise, for the flowing off of the doṣa and for the relief of pain.",
              "कटुकातिविषापाठा → शाकत्वग्घिगु → तेजनीः → तद्वच्च → दोषस्यंदार्थं → वेदनोपशमायच."),
        match(2, "Match each name of unit 115 to the card's identification.",
              [["कटुका", "kutki (standard)"], ["अतिविषा", "atis (standard)"], ["पाठा", "velvetleaf (probable)"],
               ["तेजनी", "identity disputed"], ["वेदना", "pain"]],
              "Each name keeps the data's label: standard, probable or disputed.",
              "कटुका, अतिविषा, पाठा, तेजनी, वेदना.", role="extend",
              teaches="Kaṭukā (kutki) is standard; pāṭhā (velvetleaf) is probable; tejanī is disputed."),
        mcq("discriminate", 3, "Which split of तद्वच्च is right?",
            ("तद्वत् + च", "त् + च → च्च: तद्वत् + च → तद्वच्च."),
            [("तद्व + च्च", "तद्व is not a word; the adverb is तद्वत् (likewise)."),
             ("तद्वः + च", "A visarga before च would give तद्वश्च."),
             ("तद्वम् + च", "म् before च would be written ं: तद्वं च.")],
            "तद्वत् (likewise) + च (and): त् + च → च्च.",
            "त् + च → च्च."),
        multi("apply", 4, "Which statements about unit 115 are right by the card?",
              [("The line has its own verb", "No: 'make her drink' is carried from unit 114."),
               ("शाकत्वक् may be one item or two", "Right: teak bark, or śāka and tvak; the data leaves it open."),
               ("The line names the doṣa that flows off", "No: the doṣa is not specified."),
               ("हिङ्गु here rests on a conjectural reading", "Right: printed घिगु is read हिङ्गु on a conjecture.")],
              [1, 3],
              "The line has no verb, names no doṣa, and leaves śāka-tvak and hiṅgu open.",
              "Open readings stay open."),
        mcq("transfer", 5, "By the rule of तद्वच्च (तद्वत् + च), how is एतत् + च (and this) joined?",
            ("एतच्च", "त् + च → च्च, as तद्वत् + च → तद्वच्च."),
            [("एतद्च", "Before च the त् becomes च्, not द्."),
             ("एतत्च", "त् does not stay unchanged before च."),
             ("एतश्च", "श्च comes from a visarga before च, not from त्.")],
            "एतत् + च = एतच्च, like तद्वत् + च = तद्वच्च.",
            "त् + च → च्च.",
            teaches="A final त् before च becomes च्: तद्वत् + च → तद्वच्च."),
    ],
}

# ---------------------------------------------------------------- unit 116
AUTHORED["116"] = {
    "title": "त्रिरात्रमेवं सप्ताहं स्नेहमेव ततः पिबेत्",
    "question": "By unit 116, what should she drink, and what in the evening?",
    "rule": ("Thus for three nights (त्रिरात्रम्), for seven days (सप्ताहम्); then she should drink sneha (oil or fat) "
             "alone. In the evening (सायम्) she should drink ariṣṭa, and likewise a well-made āsava (both fermented "
             "medicinal liquors)."),
    "limits": ("The two periods stand side by side with no 'or' or 'and': whether they are alternatives or successive "
               "is not stated, and no question asks which. Which ariṣṭa or āsava is not said; no amount. The subject "
               "(the woman) is understood. सुक्कृत is a print habit for सुकृत."),
    "explain_hi": ("यह श्लोक प्रसूता के पेय बताता है। "
                   "इस प्रकार तीन रात (त्रिरात्रम्), सात दिन (सप्ताहम्); तब वह केवल स्नेह यानी तेल या वसा ही पिए। "
                   "सायं (सायम्) वह अरिष्ट पिए, और उसी प्रकार भली-भाँति बना आसव; दोनों खमीर उठाकर बने औषधीय पेय हैं। "
                   "तीन रात और सात दिन विकल्प हैं या एक के बाद एक, पंक्ति में ‘वा’ या ‘च’ नहीं, इसलिए तय नहीं। "
                   "कौन-सा अरिष्ट या आसव, यह भी नहीं कहा गया।"),
    "hook": "दिन में केवल स्नेह; साँझ को अरिष्ट-आसव।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 116, what should she drink in the evening (सायम्)?",
            ("Ariṣṭa, and likewise āsava", "सायं पिबेदरिष्टं च तथा सुकृतमासवम्."),
            [("Milk boiled with fresh ghee", "Milk and ghee are not named in unit 116."),
             ("A decoction of śirīṣa bark", "Śirīṣa is unit 117, and there it is for swabs, not a drink."),
             ("Warm water with rock salt", "Water and salt are not named in unit 116.")],
            "In the evening: ariṣṭa, and likewise a well-made āsava.",
            "सायं पिबेत् अरिष्टम्, तथा आसवम्."),
        order(1, "Put these phrases of unit 116 in the verse's order.",
              ["त्रिरात्रमेवं", "सप्ताहं", "स्नेहमेव ततः पिबेत्", "सायं पिबेदरिष्टं च", "तथा सुक्कृतमासवं"],
              "Thus three nights, seven days; then she should drink sneha alone; in the evening ariṣṭa, and likewise a well-made āsava.",
              "त्रिरात्रमेवं → सप्ताहं → स्नेहमेव ततः पिबेत् → सायं पिबेदरिष्टं च → तथा सुक्कृतमासवं."),
        match(2, "Match each word of unit 116 to its meaning.",
              [["त्रिरात्रम्", "for three nights"], ["सप्ताहम्", "for seven days"], ["एव", "alone, only"],
               ["सायम्", "in the evening"], ["सुकृत", "well made"]],
              "Two periods, sneha alone, and evening drinks of ariṣṭa and a well-made āsava.",
              "त्रिरात्रम्, सप्ताहम्, एव, सायम्, सुकृत.", role="extend",
              teaches="An accusative of time gives duration: त्रिरात्रम् 'for three nights', सप्ताहम् 'for seven days'."),
        mcq("discriminate", 3, "Which split of पिबेदरिष्टम् is right?",
            ("पिबेत् + अरिष्टम्", "त् before a vowel becomes द्: पिबेत् + अरिष्टम् → पिबेदरिष्टम्."),
            [("पिबेद + रिष्टम्", "पिबेद is not a form; the optative is पिबेत्."),
             ("पिबेः + अरिष्टम्", "एः before a vowel would give पिबेररिष्टम्, with र्."),
             ("पिबेत् + रिष्टम्", "The drink is अरिष्ट; त् + र would not give दर.")],
            "पिबेत् (should drink) + अरिष्टम् (ariṣṭa): त् + vowel → द्.",
            "त् + vowel → द्."),
        mcq("apply", 4, "A reader takes the two periods of unit 116 as alternatives. What does the card say?",
            ("The line has no 'or'; it is open", "The data: no 'or' or 'and'; the relation is not settled."),
            [("Right: वा is printed between them", "No वा (or) is printed between the two periods."),
             ("No: they must add up to ten days", "Nothing in the line adds the periods together."),
             ("No: the seven days come first", "The line prints त्रिरात्रम् first, and states no sequence.")],
            "The two periods stand side by side; whether alternatives or successive is not stated.",
            "त्रिरात्रम् एवम् सप्ताहम्: no वा, no च."),
        mcq("transfer", 5, "By the rule of स्नेहमेव (स्नेहम् + एव), how is फलम् + एव (only the fruit) joined?",
            ("फलमेव", "A final म् joins the following vowel, as स्नेहम् + एव → स्नेहमेव."),
            [("फलं एव", "Before a vowel the म् is not written ं; it joins the vowel."),
             ("फलेव", "The म् is not dropped before a vowel."),
             ("फलमैव", "The vowel ए stays ए; nothing makes it ऐ.")],
            "फलम् + एव = फलमेव, like स्नेहम् + एव = स्नेहमेव.",
            "म् + vowel → म joined to the vowel.",
            teaches="A final म् before a vowel is joined to it: स्नेहम् + एव → स्नेहमेव."),
    ],
}

# ---------------------------------------------------------------- unit 117
AUTHORED["117"] = {
    "title": "शिरीषककुभकाथपिचून्योनौ च निक्षिपेत्",
    "question": "By unit 117, what swabs are placed in the yoni, and how are other complications handled?",
    "rule": ("One should place in the yoni swabs (पिचु) of the decoction (printed काथ) of śirīṣa (siris) and kakubha "
             "(arjuna); and whatever other complications (उपद्रव) there may be, those one should treat each according "
             "to its own (यथास्वम्)."),
    "limits": ("काथ is read क्वाथ (a possible repair). 'Swabs of the decoction' may be swabs soaked in it or swabs of the "
               "drugs; the line gives no more. 'Each according to its own' supplies no noun, and no complication is "
               "named. No question rests on these."),
    "explain_hi": ("यह श्लोक दो बातें कहता है। "
                   "शिरीष यानी सिरस (मानक) और ककुभ यानी अर्जुन (मानक) के क्वाथ (छपा ‘काथ’) के पिचु यानी फाहे योनि में रखे (निक्षिपेत्)। "
                   "और जो अन्य उपद्रव यानी जटिलताएँ हों (उपद्रवाश्च येऽन्ये स्युः), उनकी चिकित्सा अपने-अपने अनुसार (यथास्वम्) करे। "
                   "फाहे काढ़े में भिगोए हों या द्रव्यों के बने हों, पंक्ति नहीं बताती; कोई उपद्रव नाम से नहीं दिया गया।"),
    "hook": "सिरस-अर्जुन के फाहे; बाकी उपद्रव अपने-अपने ढंग से।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 117, the decoction for the swabs is of which two trees?",
            ("Śirīṣa and kakubha", "शिरीषककुभक्वाथपिचून्: swabs of the decoction of śirīṣa and kakubha."),
            [("Devadāru and candana", "Devadāru and candana are not named in unit 117."),
             ("Kaṭukā and pāṭhā", "Kaṭukā and pāṭhā are drugs to drink in unit 115, not these swabs."),
             ("Śāka and śālmalī", "Neither tree is named in unit 117.")],
            "Śirīṣa (siris) and kakubha (arjuna).",
            "शिरीष, ककुभ: क्वाथ के पिचु."),
        order(1, "Put the quarters of the verse in unit 117 in order.",
              ["शिरीषककुभकाथपिचून्", "योनौ च निक्षिपेत्", "उपद्रवाश्च येऽन्ये स्युः", "तान्यथास्वमुपाचरेत्"],
              "Swabs of the śirīṣa-kakubha decoction, and in the yoni one should place; and whatever other complications there may be, those one should treat each by its own.",
              "शिरीषककुभकाथपिचून् → योनौ च निक्षिपेत् → उपद्रवाश्च येऽन्ये स्युः → तान्यथास्वमुपाचरेत्."),
        match(2, "Match each word of unit 117 to its meaning.",
              [["शिरीष", "siris (standard)"], ["ककुभ", "arjuna (standard)"], ["निक्षिपेत्", "should place"],
               ["उपद्रव", "complication"], ["उपाचरेत्", "should treat"]],
              "Swabs of the siris-arjuna decoction go in; other complications are treated each by its own.",
              "शिरीष, ककुभ, निक्षिपेत्, उपद्रव, उपाचरेत्.", role="extend",
              teaches="यथास्वम् = each according to its own: every complication is treated in its own way."),
        mcq("discriminate", 3, "Which split of येऽन्ये is right?",
            ("ये + अन्ये", "ए + अ → एऽ: the अ of अन्ये is dropped and marked ऽ."),
            [("यः + अन्ये", "अः + अ would give योऽन्ये."),
             ("य + अन्ये", "अ + अ would give यान्ये."),
             ("ये + न्ये", "न्ये is not a word; the word is अन्ये (others).")],
            "ये (which) + अन्ये (other): ए + अ → एऽ.",
            "ए + अ → एऽ."),
        mcq("apply", 4, "Another complication arises after all this. What does unit 117 say?",
            ("Treat each according to its own", "उपद्रवाश्च येऽन्ये स्युस्तान्यथास्वमुपाचरेत्."),
            [("Repeat the swabs of śirīṣa and kakubha", "The swabs are one measure; other complications are treated each by its own."),
             ("Leave it alone; it will pass with time", "The line says to treat (उपाचरेत्), not to leave it."),
             ("Give only sneha for seven more days", "Unit 117 says nothing of sneha or of days.")],
            "Whatever other complications there are: treat each according to its own.",
            "तान् यथास्वम् उपाचरेत्."),
        mcq("transfer", 5, "By the rule of उपद्रवाश्च (उपद्रवाः + च), how is बालाः + च (and the children) joined?",
            ("बालाश्च", "A visarga before च becomes श्, as उपद्रवाः + च → उपद्रवाश्च."),
            [("बाला च", "आः drops its visarga before a voiced sound or a vowel; before च it becomes श्."),
             ("बालास्च", "Before च the visarga becomes श्, not स्."),
             ("बालाश्छ", "The च stays च; only the visarga changes.")],
            "बालाः + च = बालाश्च, like उपद्रवाः + च = उपद्रवाश्च.",
            "visarga + च → श्च.",
            teaches="A visarga before च or छ becomes श्: उपद्रवाः + च → उपद्रवाश्च."),
    ],
}

# ---------------------------------------------------------------- unit 118
AUTHORED["118"] = {
    "title": "प्रयो वातहरैः सिद्धं दशांहं भोजने हितं",
    "question": "By unit 118, what is beneficial in the meal for ten days, and what else is given for ten days?",
    "rule": ("(What is) cooked (सिद्धम्) with Vāta-removing (ones) is beneficial (हितम्) in the meal for ten days "
             "(दशाहम्); and the rasa (juice) for ten days. The rest names light and little food (part of it conjectural)."),
    "limits": ("Low confidence. Printed प्रयो is read प्रायः 'mostly' and पद्व्या is read पथ्या 'wholesome' (both "
               "conjectural); परम् may be 'thereafter' or 'excellent'. The kind of rasa and the nouns for 'cooked (one)' "
               "and 'Vāta-removing (ones)' are not stated. No question rests on these."),
    "explain_hi": ("यह श्लोक प्रसूता के भोजन की बात कहता है; विश्वास निम्न है। "
                   "वात को हरने वाले (द्रव्यों) से पकाया हुआ (सिद्धम्) दस दिन (दशाहम्) भोजन में हितकर है, और रस दस दिन। "
                   "फिर हल्का और अल्प भोजन; बीच का ‘पथ्य’ अनुमानित पाठ है (छपा ‘पद्व्या’)। "
                   "छपा ‘प्रयो’ अनुमान से ‘प्रायः’ (अधिकतर) पढ़ा गया; ‘परम्’ = उसके बाद या उत्तम, दोनों सम्भव। "
                   "रस किस प्रकार का हो और ‘किनसे’ पकाया, ये संज्ञाएँ नहीं दी गईं।"),
    "hook": "दस दिन वातहर पका भोजन, दस दिन रस; फिर हल्का, थोड़ा।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 118, for how long is the food cooked with Vāta-removing (ones) beneficial?",
            ("Ten days", "दशाहं भोजने हितम्: beneficial in the meal for ten days."),
            [("Seven days", "Seven days (सप्ताहम्) belong to unit 116, not this food."),
             ("Three nights", "Three nights (त्रिरात्रम्) belong to unit 116."),
             ("Four months", "Four months are named in unit 119, not here.")],
            "For ten days (दशाहम्).",
            "दशाहम् = for ten days."),
        order(1, "Put these printed pieces of unit 118 in order.",
              ["प्रयो वातहरैः सिद्धं", "दशांहं भोजने हितं", "रसो दशांहं च", "परं", "लघुपद्व्याल्पभोजना"],
              "Cooked (mostly) with Vāta-removing (ones), for ten days beneficial in the meal; and rasa for ten days; then (or: excellent) light, (wholesome,) little food.",
              "प्रयो वातहरैः सिद्धं → दशांहं भोजने हितं → रसो दशांहं च → परं → लघुपद्व्याल्पभोजना."),
        match(2, "Match each word of unit 118 to its meaning.",
              [["वातहर", "removing Vāta"], ["सिद्ध", "cooked, prepared"], ["भोजन", "meal"], ["हित", "beneficial"],
               ["रस", "juice, essence (kind not stated)"]],
              "Food cooked with Vāta-removing (ones) is beneficial in the meal; rasa is also given.",
              "वातहर, सिद्ध, भोजन, हित, रस.", role="extend",
              teaches="दशाहम् = दश + अहम्, 'for ten days': the accusative gives the duration."),
        mcq("discriminate", 3, "Which split of दशाहम् (printed दशांहं) is right?",
            ("दश + अहम्", "अ + अ → आ: दश (ten) + अहम् (day) → दशाहम्."),
            [("दशम् + अहम्", "म् before a vowel would give दशमहम्."),
             ("दशः + अहम्", "अः + अ would give दशोऽहम्."),
             ("दश + हम्", "हम् is not a word; the word for day is अहन्, here अहम्.")],
            "दश (ten) + अहम् (day): अ + अ → आ.",
            "अ + अ → आ."),
        mcq("apply", 4, "By unit 118, what is said of the rasa?",
            ("Ten days; its kind is not stated", "रसो दशाहं च: rasa for ten days; the kind is not given."),
            [("A meat soup, given for seven days", "The kind is not stated, and the period is ten days."),
             ("Forbidden until four months have passed", "Nothing forbids it; rasa is given for ten days."),
             ("Given for three nights, then stopped", "The period named is ten days, not three nights.")],
            "Rasa is given for ten days; the line does not say which rasa.",
            "रसः दशाहम्."),
        mcq("transfer", 5, "By the rule of रसो दशाहम् (रसः + दशाहम्), how is नरः + वदति (the man speaks) joined?",
            ("नरो वदति", "अः before a voiced sound becomes ओ, as रसः + दशाहम् → रसो दशाहम्."),
            [("नरा वदति", "The visarga drops after आः, not after अः; अः becomes ओ."),
             ("नरर्वदति", "र् comes from a visarga after vowels other than अ/आ."),
             ("नरश्वदति", "A visarga becomes श् before च or छ (optionally before श), not before व.")],
            "नरः + वदति = नरो वदति, like रसः + दशाहम् = रसो दशाहम्.",
            "अः + voiced consonant → ओ.",
            teaches="अः before a voiced consonant becomes ओ: रसः + दशाहम् → रसो दशाहम्."),
    ],
}

# ---------------------------------------------------------------- unit 119
AUTHORED["119"] = {
    "title": "स्वेदाभ्यंगपरा स्नेहान् बलातैलादिकान् भजेत्",
    "question": "By unit 119, what should she be intent on, and which oils should she use?",
    "rule": ("Intent on sweating (स्वेद) and anointing (अभ्यङ्ग), she should use (भजेत्) oils and fats (स्नेहान्) "
             "beginning with balā oil (बलातैलादिकान्). The next line ('after four months, she, gradually, and pleasant "
             "(ones)') is incomplete."),
    "limits": ("Low confidence. The second line has no printed verb; 'after four months' is an open reading, and "
               "सुखानि has no noun (perhaps damaged). No question rests on that line beyond its printed order and its "
               "missing verb. The other oils are not named."),
    "explain_hi": ("यह श्लोक प्रसूता की आगे की परिचर्या कहता है; विश्वास निम्न है। "
                   "स्वेद यानी सेंक और अभ्यंग यानी तेल-मालिश में लगी हुई (स्वेदाभ्यङ्गपरा) वह बलातैल आदि स्नेहों का सेवन करे (भजेत्)। "
                   "दूसरी पंक्ति अधूरी है: ‘चार महीनों के बाद वह क्रम से और सुखद...’; उसकी क्रिया छपी नहीं, और ‘सुखानि’ किसके लिए है, "
                   "यह नहीं बताया। "
                   "बलातैल की विधि आगे इकाई १२०-१२१ में आती है।"),
    "hook": "सेंक, मालिश और बलातैल: प्रसूता की परिचर्या।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 119, which oil heads the oils she should use?",
            ("Balā oil (balātaila)", "बलातैलादिकान्: oils beginning with balā oil."),
            [("Sesame oil (tilataila)", "Sesame oil is not named in unit 119."),
             ("Castor oil (eraṇḍataila)", "Castor oil is not named in unit 119."),
             ("Mustard oil (sarṣapataila)", "Mustard oil is not named in unit 119.")],
            "Oils beginning with balā oil.",
            "स्नेहान् बलातैलादिकान् भजेत्."),
        order(1, "Put these phrases of unit 119 in the verse's order.",
              ["स्वेदाभ्यंगपरा", "स्नेहान् बलातैलादिकान्", "भजेत्", "ऊर्ध्वं चतुर्भ्यो मासेभ्यः", "सा क्रमेण सुखानि च"],
              "Intent on sweating and anointing, oils beginning with balā oil she should use; after four months, she, gradually, and pleasant (ones).",
              "स्वेदाभ्यंगपरा → स्नेहान् बलातैलादिकान् → भजेत् → ऊर्ध्वं चतुर्भ्यो मासेभ्यः → सा क्रमेण सुखानि च."),
        match(2, "Match each word of unit 119 to its meaning.",
              [["स्वेद", "sweating, fomentation"], ["अभ्यङ्ग", "anointing"], ["पर", "intent on"],
               ["भजेत्", "should resort to, use"], ["आदिक", "beginning with"]],
              "Intent on sweating and anointing, she uses oils beginning with balā oil.",
              "स्वेद, अभ्यङ्ग, पर, भजेत्, आदिक.", role="extend",
              teaches="-आदिक 'beginning with': बलातैलादिकान् = oils beginning with balā oil; the others are not named."),
        mcq("discriminate", 3, "Which split of स्वेदाभ्यङ्ग is right?",
            ("स्वेद + अभ्यङ्ग", "अ + अ → आ: स्वेद + अभ्यङ्ग → स्वेदाभ्यङ्ग."),
            [("स्वेदः + अभ्यङ्ग", "अः + अ would give स्वेदोऽभ्यङ्ग."),
             ("स्वेदे + अभ्यङ्ग", "ए + अ would give स्वेदेऽभ्यङ्ग."),
             ("स्वेदा + भ्यङ्ग", "भ्यङ्ग is not a word; the word is अभ्यङ्ग (anointing).")],
            "स्वेद (sweating) + अभ्यङ्ग (anointing): अ + अ → आ.",
            "अ + अ → आ."),
        multi("apply", 4, "Which statements about unit 119 are right by the card?",
              [("She should use balā oil only, nothing else", "No: -आदिक means 'beginning with'; other oils are meant."),
               ("Balā oil is taught later, in units 120 and 121", "Right: 120 announces it, 121 gives the recipe."),
               ("The second line has no verb of its own", "Right: the data calls it elliptical and incomplete."),
               ("The line states what she does after four months", "No: that line is incomplete; no verb is printed.")],
              [1, 2],
              "Oils beginning with balā oil; its recipe follows; the second line is incomplete.",
              "बलातैलादिकान्: beginning with balā oil."),
        mcq("transfer", 5, "स्वेदाभ्यङ्गपरा is feminine (she, intent on ...). How would a man intent on study, as subject, be said?",
            ("अध्ययनपरः", "The final -पर agrees with the person: masculine nominative singular -परः."),
            [("अध्ययनपरा", "-परा is feminine, as in स्वेदाभ्यङ्गपरा; a man needs -परः."),
             ("अध्ययनपरम्", "-परम् is neuter, or masculine accusative; the subject needs -परः."),
             ("अध्ययनपराः", "-पराः is plural; one man needs the singular -परः.")],
            "अध्ययनपरः, like स्वेदाभ्यङ्गपरा, but masculine.",
            "-पर at the end of a compound takes the gender, number and case of the person.",
            teaches="A compound ending in -पर ('intent on') agrees with the person: स्वेदाभ्यङ्गपरा (she), अध्ययनपरः (he)."),
    ],
}

# ---------------------------------------------------------------- unit 120
AUTHORED["120"] = {
    "title": "अथ बलातैलमुपदेक्ष्यामः",
    "question": "By unit 120, what does the author announce?",
    "rule": ("Now (अथ) we shall teach (उपदेक्ष्यामः, future, 'we') the oil of balā (country mallow, standard): "
             "balātaila. The recipe follows in unit 121."),
    "limits": ("A formula only: no ingredient, measure or use is given here. Balā = country mallow (standard; the Sida "
               "species are also used under this name). A prose line."),
    "explain_hi": ("यह गद्य-पंक्ति बलातैल के प्रकरण का आरम्भ है: अब (अथ) हम बला यानी बरियार (मानक) के तैल का उपदेश करेंगे "
                   "(उपदेक्ष्यामः)। "
                   "‘उपदेक्ष्यामः’ उप-√दिश् का भविष्यत् काल, उत्तम पुरुष बहुवचन है। "
                   "इसकी विधि अगली इकाई (१२१) में है; यहाँ कोई द्रव्य, मात्रा या प्रयोग नहीं।"),
    "hook": "अथ बलातैलम्: अब तेल की विधि।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 120, what will be taught next?",
            ("The oil of balā", "बलातैलमुपदेक्ष्यामः: we shall teach balā oil."),
            [("The ghee of śatāvarī", "No ghee is announced in unit 120."),
             ("The decoction of śirīṣa", "Śirīṣa decoction belongs to unit 117, not this announcement."),
             ("The ariṣṭa liquor", "Ariṣṭa belongs to unit 116, not this announcement.")],
            "Balātaila, the oil of balā.",
            "बलातैलम् उपदेक्ष्यामः."),
        order(1, "Put the words of unit 120 in the line's order.",
              ["अथ", "बलातैलम्", "उपदेक्ष्यामः"],
              "Now, balā oil, we shall teach.",
              "अथ → बलातैलम् → उपदेक्ष्यामः."),
        match(2, "Match each word of unit 120 to its meaning.",
              [["अथ", "now"], ["बला", "country mallow (standard)"], ["तैल", "oil"], ["उपदेक्ष्यामः", "we shall teach"]],
              "Now we shall teach the oil of balā.",
              "अथ, बला, तैल, उपदेक्ष्यामः.", role="extend",
              teaches="बलातैल = बला + तैल, the oil of balā (country mallow)."),
        mcq("discriminate", 3, "What form is उपदेक्ष्यामः?",
            ("Future, 'we shall teach'", "The data: 1st person plural future of उप-√दिश्."),
            [("Present, 'they teach'", "-स्यामः/-क्ष्यामः is not a present ending, and 'they' would be 3rd person."),
             ("Optative, 'one should teach'", "An optative 'one should teach' would be उपदिशेत्, not -क्ष्यामः."),
             ("Past, 'we have taught'", "-क्ष्यामः marks the future, not the past.")],
            "उपदेक्ष्यामः = we shall teach: future, 1st person plural.",
            "-ष्यामः / -क्ष्यामः = future, 'we'."),
        mcq("apply", 4, "Where does the book give the recipe that unit 120 announces?",
            ("In the next unit, 121", "The data: the opening formula of the recipe in card 121."),
            [("In unit 119, the one before", "Unit 119 only names balā oil among the oils to use."),
             ("Nowhere in this chapter", "The recipe follows at once, in unit 121."),
             ("In unit 116, with ariṣṭa", "Unit 116 is about sneha, ariṣṭa and āsava.")],
            "The recipe follows in unit 121.",
            "अथ ... उपदेक्ष्यामः → recipe in the next unit."),
        mcq("transfer", 5, "By the pattern of उपदेक्ष्यामः, what does वक्ष्यामः (from √वच्, speak) mean?",
            ("We shall speak", "-क्ष्यामः = future, 1st person plural, as in उपदेक्ष्यामः."),
            [("We are speaking", "That would be a present form, not -क्ष्यामः."),
             ("They will speak", "'They will speak' is वक्ष्यन्ति; -मः marks 'we'."),
             ("We have spoken", "-क्ष्यामः marks the future, not the past.")],
            "वक्ष्यामः = we shall speak, like उपदेक्ष्यामः = we shall teach.",
            "-ष्यामः / -क्ष्यामः = we shall ...",
            teaches="The ending -स्यामः (here -क्ष्यामः) makes a future 'we shall': उपदेक्ष्यामः, वक्ष्यामः."),
    ],
}

# ---------------------------------------------------------------- unit 121
AUTHORED["121"] = {
    "title": "बलामूलकषायस्य भागाः षट्",
    "question": "By unit 121, how is balātaila made: what liquids, what additions, how cooked and stored?",
    "rule": ("Six parts of balā-root decoction, as many of milk, a part of the yava-kola-kulattha-daśamūla decoction, "
             "and oil (measure unclear); fine powders of many drugs are added; it is cooked slowly on a gentle fire and "
             "stored, well guarded, in a good vessel."),
    "limits": ("Low confidence. The oil's measure (printed भागश्चैतुर्दशतैलस्य) cannot be restored; ऐकष्ट्यम् is read "
               "'together' only conjecturally; अह्वगन्धा → अश्वगन्धा and कालानुसार्थ्य → कालानुसार्य are conjectural; "
               "kṣīraśuklā and kālānusārya are unidentified. No question rests on these. Identifications keep the data's "
               "labels; uses come in unit 122."),
    "explain_hi": ("यह लम्बी गद्य-पंक्ति बलातैल की विधि देती है। "
                   "बला की जड़ के काढ़े के छह भाग, उतने ही (छह) भाग दूध, यव, कोल यानी बेर, कुलत्थ यानी कुलथी और दशमूल के काढ़े "
                   "का एक भाग, और तेल, जिसकी मात्रा छपाई में अस्पष्ट है। "
                   "इनमें काकोली से सैन्धव तक अनेक द्रव्यों के महीन चूर्ण डालकर, धीरे-धीरे मृदु अग्नि पर पकाकर, अच्छे पात्र में "
                   "सुरक्षित रखे। "
                   "कई नामों की पहचान विवादित या अज्ञात है; अश्वगन्धा और कालानुसार्य अनुमानित पाठ हैं।"),
    "hook": "छह भाग बला-काढ़ा, छह भाग दूध; चूर्ण डालो, धीमी आँच, अच्छा पात्र।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 121, how many parts of balā-root decoction are taken?",
            ("Six parts", "बलामूलकषायस्य भागाः षट्: six parts."),
            [("Four parts", "The line says six (षट्), not four."),
             ("Ten parts", "The line says six (षट्), not ten."),
             ("One part", "One part (भागः) is of the yava-kola-kulattha-daśamūla decoction.")],
            "Six parts of balā-root decoction, and just as many of milk.",
            "भागाः षट्; तावन्त एव पयसः."),
        order(1, "Put these steps of the balātaila recipe (unit 121) in the line's order.",
              ["बलामूलकषायस्य भागाः षट्", "तावंतएव पयसो", "यवकोलकुलत्थदशमूलकषायस्य भागो",
               "श्लक्ष्णचूर्णानि चावाप्य", "शनैर्मृद्वग्निना साधयित्वा", "सुभाजनेऽनु गुप्तं निदध्यात्"],
              "Six parts of balā-root decoction; as many of milk; a part of the yava-kola-kulattha-daśamūla decoction; adding the fine powders; preparing slowly on a gentle fire; storing well guarded in a good vessel.",
              "षट् भाग → पयस् → यव... क्वाथ → चूर्ण → मृदु अग्नि → सुभाजन."),
        match(2, "Match each drug of unit 121 to the card's identification.",
              [["देवदारु", "deodar (standard)"], ["मञ्जिष्ठा", "Indian madder (standard)"], ["वचा", "sweet flag (standard)"],
               ["सैन्धव", "rock salt (standard)"], ["मधुक", "licorice (probable)"]],
              "Each name keeps the data's label.",
              "देवदारु, मञ्जिष्ठा, वचा, सैन्धव, मधुक.", role="extend",
              teaches="In this recipe each drug keeps its own label: standard, probable, disputed or unidentified."),
        mcq("discriminate", 3, "Which split of मृद्वग्निना is right?",
            ("मृदु + अग्निना", "उ before a different vowel becomes व्: मृदु + अग्निना → मृद्वग्निना."),
            [("मृदा + अग्निना", "आ + अ would give मृदाग्निना."),
             ("मृदो + अग्निना", "ओ + अ would give मृदोऽग्निना."),
             ("मृद् + वग्निना", "वग्निना is not a word; the word is अग्नि (fire).")],
            "मृदु (gentle) + अग्निना (with fire): उ + अ → व.",
            "उ + a different vowel → व् + that vowel."),
        multi("apply", 4, "Which drugs of unit 121 does the card label 'standard'?",
              [("शतावरी (wild asparagus)", "Right: standard."),
               ("कुष्ठ (costus)", "Right: standard."),
               ("तगर (tagara)", "No: tagara is disputed."),
               ("मधुक (licorice)", "No: madhuka is probable.")],
              [0, 1],
              "Śatāvarī and kuṣṭha are standard; tagara is disputed; madhuka is probable.",
              "Keep each plant's label exactly."),
        mcq("transfer", 5, "By the rule of मृद्वग्निना (मृदु + अग्निना), how is मधु + अत्र (honey here) joined?",
            ("मध्वत्र", "उ before a different vowel becomes व्, as मृदु + अग्निना → मृद्वग्निना."),
            [("मधात्र", "उ + अ do not give आ."),
             ("मधोत्र", "ओ comes from अ + उ, not from उ + अ."),
             ("मधूत्र", "A long ऊ comes from उ + उ.")],
            "मधु + अत्र = मध्वत्र, like मृदु + अग्निना = मृद्वग्निना.",
            "उ + a different vowel → व्.",
            teaches="A final उ before a different vowel becomes व्: मृदु + अग्निना → मृद्वग्निना."),
    ],
}

# ---------------------------------------------------------------- unit 122
AUTHORED["122"] = {
    "title": "एष भगवतो धन्वंतरेरभिमतस्तैलराजः",
    "question": "By unit 122, who approved the king of oils, how is it used, and for whom?",
    "rule": ("This king of oils (तैलराज, the balātaila), approved by the venerable Dhanvantari, is to be used in "
             "drinking, nasal administration (नावन), anointing and enema (बस्ति), for kings, the emaciated, women "
             "recently delivered, infants, the aged, the delicate and others."),
    "limits": ("Low confidence. राजमात्र has no certain sense; the marma compound can be divided two ways; the last group "
               "(divine injury, cursing, मनोज्वर) rests on a conjectural reading of printed ममो; graha (seizer) is not "
               "explained. No question rests on these. No dose is given."),
    "explain_hi": ("यह गद्य-पंक्ति बलातैल की प्रशंसा और प्रयोग कहती है। "
                   "यह तैलराज यानी तेलों का राजा भगवान् धन्वन्तरि को मान्य (अभिमत) है। "
                   "इसका प्रयोग पान, नावन यानी नाक में डालना, अभ्यंग और बस्ति यानी एनिमा में होता है। "
                   "किनके लिए: राजा, कृश, सूतिका यानी प्रसूता, शिशु, बीती आयु वाले, सुकुमार, महाग्रह से गृहीत, दीर्घ रोग से क्षीण, "
                   "और जिनके अंग मर्म में बिंधे, गिरे, आहत, टूटे या उखड़े हों। "
                   "‘राजमात्र’ का अर्थ अस्पष्ट है, और अन्तिम समूह (दैव उपघात, अभिशाप, मनोज्वर) अनुमानित पाठ पर है।"),
    "hook": "धन्वन्तरि का तैलराज: पान, नस्य, अभ्यंग, बस्ति।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 122, by whom is this king of oils approved?",
            ("The venerable Dhanvantari", "भगवतो धन्वन्तरेरभिमतः: approved by the venerable Dhanvantari."),
            [("The kings who use it daily", "Kings are among the users, not the one who approved it."),
             ("The women recently delivered", "Sūtikās are among the users, not the approver."),
             ("The physician who prepares it", "No preparing physician is named as approver.")],
            "It is approved by the venerable Dhanvantari.",
            "धन्वन्तरेः अभिमतः."),
        order(1, "Put the four ways of using the oil in unit 122 in the line's order.",
              ["पान", "नावन", "अभ्यङ्ग", "बस्ति"],
              "Drinking, nasal administration, anointing, enema: पाननावनाभ्यंगबस्तिषु.",
              "पान → नावन → अभ्यङ्ग → बस्ति."),
        match(2, "Match each word of unit 122 to its meaning.",
              [["कृश", "the emaciated"], ["सूतिका", "a woman recently delivered"], ["शिशु", "an infant"],
               ["सुकुमार", "the delicate"], ["नावन", "nasal administration"]],
              "Among the users: the emaciated, women recently delivered, infants, the delicate; nāvana is one way of use.",
              "कृश, सूतिका, शिशु, सुकुमार, नावन.", role="extend",
              teaches="The users stand in the genitive plural: कृशानाम्, सूतिकानाम्, शिशूनाम्, 'for the emaciated, ...'."),
        mcq("discriminate", 3, "Which split of धन्वन्तरेरभिमतः is right?",
            ("धन्वन्तरेः + अभिमतः", "A visarga after ए before a vowel becomes र्: धन्वन्तरेरभिमतः."),
            [("धन्वन्तरे + अभिमतः", "ए + अ would give धन्वन्तरेऽभिमतः."),
             ("धन्वन्तरिः + अभिमतः", "इः + अ would give धन्वन्तरिरभिमतः, with इ."),
             ("धन्वन्तरेर + भिमतः", "भिमत is not a word; the word is अभिमत (approved).")],
            "धन्वन्तरेः (of Dhanvantari) + अभिमतः (approved): एः + vowel → एर्.",
            "एः + vowel → एर्."),
        multi("apply", 4, "Which persons does unit 122 name among those the oil serves?",
              [("Pregnant women (garbhiṇī)", "No: garbhiṇī is not named in unit 122."),
               ("Women recently delivered (sūtikā)", "Right: सूतिकानाम्."),
               ("Infants (śiśu)", "Right: शिशूनाम्."),
               ("Wrestlers (malla)", "No: wrestlers are not named in unit 122.")],
              [1, 2],
              "Sūtikās and infants are named; pregnant women and wrestlers are not.",
              "सूतिकानाम्, शिशूनाम्: for them it is to be used."),
        mcq("transfer", 5, "By the rule of धन्वन्तरेरभिमतः, how is हरेः + आज्ञा (Hari's command) joined?",
            ("हरेराज्ञा", "A visarga after ए before a vowel becomes र्, as धन्वन्तरेः + अभिमतः."),
            [("हरे आज्ञा", "After ए the visarga does not drop before a vowel; it becomes र्."),
             ("हरेयाज्ञा", "य् arises from इ before a vowel, not from एः."),
             ("हरोराज्ञा", "The ए of हरेः does not change to ओ.")],
            "हरेः + आज्ञा = हरेराज्ञा, like धन्वन्तरेः + अभिमतः = धन्वन्तरेरभिमतः.",
            "एः + vowel → एर्.",
            teaches="A visarga after a vowel other than अ/आ becomes र् before a vowel: धन्वन्तरेः + अभिमतः → धन्वन्तरेरभिमतः."),
    ],
}


# ===================================================================== NOTES_HI
NOTES_HI = {
    "109": ("गद्य-पंक्ति; विश्वास मध्यम। पाठ-चिह्न: छपा ‘जघनशक्तस्य’ → सम्भावित ‘जघनसक्तस्य’ (‘शक्त’ = समर्थ, अर्थ नहीं बैठता; "
            "‘सक्त’ = अटका, जैसे इकाई १०८ में ‘अंससंसक्त’)। इस शब्द पर प्रश्न नहीं। पंक्ति में क्रिया नहीं; ‘निकाले’ इकाई १०८ "
            "(छपी पंक्ति ११५) से समझी जाती है, डेटा के अनुसार यह पंक्ति उसी को आगे बढ़ाती प्रतीत होती है। जघनकपाल = श्रोणि की "
            "हड्डियाँ (सम्भावित)। अन्त का ‘इति’ स्थितियों की सूची बन्द करता है। सन्धि जाँची: दारयित्वा + इति → दारयित्वेति "
            "(आ + इ → ए); जघन + कपाल (सन्धि नहीं)।"),
    "110": ("गद्य-पंक्ति; विश्वास उच्च; कोई पाठ-चिह्न नहीं। आगे की पंक्तियों का आरम्भ-सूत्र; ‘श्लोक’ शब्द छपा नहीं, समझा जाता है। "
            "छपा ‘भवंति’ = भवन्ति (अनुस्वार)। सन्धि जाँची: च + अत्र → चात्र (अ + अ → आ)।"),
    "111": ("दो छपी पंक्तियाँ (०२.०४.११८-११९), एक वाक्य; विश्वास मध्यम; कोई पाठ-चिह्न नहीं। डेटा इस इकाई को गद्य कहता है, "
            "यद्यपि पंक्तियाँ अनुष्टुभ् जैसी लम्बाई की लगती हैं (रिपोर्ट किया)। ‘खण्डशः’ अटकने से जुड़ा है या काटने से, खुला है; "
            "डेटा उसे सम्भवतः काटने से जोड़ता है; इस पर प्रश्न नहीं। ‘वायु’ यहाँ साधारण वायु। छपा ‘छित्वा’ = छित्त्वा की वर्तनी। "
            "सन्धि जाँची: यत् + यत् → यद्यत्, यत् + वायु → यद्वायु (त् + घोष → द्); वायुवशात् + अङ्गम् → वायुवशादङ्गम् "
            "(त् + स्वर → द्); सज्जेत् + गर्भस्य → सज्जेद्गर्भस्य; तत् + छित्वा → तच्छित्वा (त् + छ → च्छ); सम्यक् + रक्षेत् → "
            "सम्यग्रक्षेत् (क् + घोष → ग्); रक्षेत् + जननीम् → रक्षेज्जननीम् (त् + ज → ज्ज)।"),
    "112": ("श्लोक (०२.०४.१२०-१२१); विश्वास मध्यम; कोई पाठ-चिह्न नहीं। अपरा = जेर (मानक)। ‘पूर्ववत्’ किस पहले की विधि को कहता है, "
            "पंक्ति नहीं बताती। ‘शल्य’ यहाँ परिभाषित नहीं (प्रसंग से रुका गर्भ या अपरा, पर कहा नहीं)। अक्षर ‘अथापतन्तीम्’ को "
            "अथ + आपतन्तीम् भी पढ़ने देते हैं (अ + आ → आ); डेटा अर्थ से ‘अपतन्तीम्’ (न गिरती) पढ़ता है; इस पर प्रश्न नहीं। "
            "‘निर्हृतशल्याम्’ स्त्रीलिंग: स्त्री समझी जाती है। सन्धि जाँची: अथ + अपतन्तीम् → अथापतन्तीम् (अ + अ → आ); "
            "पूर्ववत् + भिषक् → पूर्ववद्भिषक् (त् + घोष → द्); एवम् → एवं (व्यंजन से पहले); सिञ्चेत् + उष्णेन → सिञ्चेदुष्णेन "
            "(त् + स्वर → द्)।"),
    "113": ("श्लोक (०२.०४.१२२-१२३); विश्वास उच्च; कोई पाठ-चिह्न नहीं। छपा एक टुकड़ा ‘स्नेहपिचुंततः’ = स्नेहपिचुम् ततः। पिचु = फाहा "
            "(सामग्री नहीं बताई); स्नेह = तेल या वसा (प्रकार नहीं बताया)। ‘मृदुः’ पुंलिंग रूप स्त्रीलिंग ‘योनिः’ के साथ विधेय में; "
            "इस पर प्रश्न नहीं। ‘तेन’ = पिचु से। सन्धि जाँची: दद्यात् + अभ्यक्त → दद्यादभ्यक्त (त् + स्वर → द्); स्नेहपिचुम् + ततः → "
            "स्नेहपिचुं ततः; योनिः + मृदुः → योनिर्मृदुः (इः + घोष → इर्); मृदुः + भवेत् → मृदुर्भवेत् (उः + घोष → उर्); भवेत् + तेन → "
            "भवेत्तेन; च + अस्याः → चास्याः (अ + अ → आ)।"),
    "114": ("श्लोक (०२.०४.१२४-१२५); विश्वास मध्यम। पाठ-चिह्न: (१) छपा ‘रास्त्रा’ → ‘रास्ना’ (सम्भावित; पहचान विवादित); "
            "(२) छपा ‘हिं | ग्वेला’ → हिङ्गु + एला = हिङ्ग्वेला (सम्भावित; बीच का अन्तर भटका हुआ); (३) छपा ‘काथं’ → ‘क्वाथम्’ "
            "(सम्भावित; व छूटा)। इन पाठों पर प्रश्न नहीं। पहचान: दीप्यक = अजवायन (सम्भावित), अतिविषा = अतीस (मानक), हिङ्गु = हींग "
            "(मानक), एला = छोटी इलायची (मानक)। पञ्चकोलक के पाँच सदस्य इस पंक्ति में नाम से नहीं। कौन-सा रूप उत्तम, नहीं कहा। "
            "सन्धि जाँची: दीप्यक + अतिविषा → दीप्यकातिविषा (अ + अ → आ); हिङ्गु + एला → हिङ्ग्वेला (उ + ए → वे); चूर्णम् + स्नेहेन → "
            "चूर्णं स्नेहेन; वा + पाययेत् → वा पाययेत् (छपा एक साथ ‘वापाययेत्’); पाययेत् + तथा → पाययेत्तथा।"),
    "115": ("श्लोक (०२.०४.१२६-१२७); विश्वास मध्यम। पाठ-चिह्न: छपा ‘...त्वग्घिगु...’ → ‘...त्वग्घिङ्गु...’ (सम्भावित; ङ् छूटा)। "
            "‘शाकत्वक्’ = सागौन की छाल (एक द्रव्य) या शाक और त्वक् (दो द्रव्य), तय नहीं। तेजनी विवादित; पाठा = अकनादि (सम्भावित); "
            "कटुका = कुटकी (मानक)। ‘दोषस्यन्दार्थम्’ पाठ निश्चित नहीं, दोष का नाम नहीं। क्रिया (पाययेत्) इकाई ११४ से। इन पर प्रश्न "
            "नहीं, केवल इतना पूछा कि ये खुले हैं। सन्धि जाँची: कटुका + अतिविषा → कटुकातिविषा (आ + अ → आ); शाकत्वक् + हिङ्गु → "
            "शाकत्वग्घिङ्गु (क् + ह → ग्घ); तद्वत् + च → तद्वच्च (त् + च → च्च); वेदना + उपशमाय → वेदनोपशमाय (आ + उ → ओ)।"),
    "116": ("श्लोक (०२.०४.१२८-१२९); विश्वास मध्यम; कोई पाठ-चिह्न नहीं। ‘त्रिरात्रमेवं सप्ताहम्’: बीच में ‘वा’ या ‘च’ नहीं, विकल्प या "
            "क्रम तय नहीं; इस पर कोई कुंजी नहीं। छपा ‘सुक्कृत’ = सुकृत (द्वित्व छपाई की आदत)। अरिष्ट, आसव = खमीर से बने औषधीय पेय "
            "(मानक); कौन-सा, नहीं कहा। सन्धि जाँची: त्रिरात्रम् + एवम् → त्रिरात्रमेवम्; स्नेहम् + एव → स्नेहमेव; पिबेत् + अरिष्टम् → "
            "पिबेदरिष्टम् (त् + स्वर → द्); सायम् → सायं (व्यंजन से पहले); सुकृतम् + आसवम् → सुकृतमासवम्।"),
    "117": ("श्लोक (०२.०४.१३०-१३१); विश्वास मध्यम। पाठ-चिह्न: छपा ‘काथ’ → ‘क्वाथ’ (सम्भावित; व छूटा, जैसे इकाई ११४ में)। "
            "पिचु काढ़े में भिगोए हों या द्रव्यों के, पंक्ति नहीं बताती। शिरीष = सिरस (मानक), ककुभ = अर्जुन (मानक)। ‘यथास्वम्’ के साथ "
            "संज्ञा नहीं दी। सन्धि जाँची: पिचून् + योनौ → पिचून्योनौ; उपद्रवाः + च → उपद्रवाश्च (विसर्ग + च → श्); ये + अन्ये → "
            "येऽन्ये (ए + अ → एऽ); स्युः + तान् → स्युस्तान् (विसर्ग + त → स्); यथास्वम् + उपाचरेत् → यथास्वमुपाचरेत्।"),
    "118": ("श्लोक (०२.०४.१३२-१३३); विश्वास निम्न। पाठ-चिह्न: (१) छपा ‘प्रयो’ → ‘प्रायो’ (प्रायः, अधिकतर; सम्भावित, ‘प्रयः’ शब्द "
            "नहीं); (२) छपा ‘लघुपद्व्याल्पभोजना’ → ‘लघुपथ्याल्पभोजना’ (सम्भावित; ‘पद्व्या’ शब्द नहीं)। ‘परम्’ = उसके बाद या उत्तम। "
            "रस का प्रकार और ‘सिद्धम्’, ‘वातहरैः’ की संज्ञाएँ नहीं दीं। इन पर प्रश्न नहीं। छपा ‘दशांहं’ = दशाहम् (अनुस्वार अतिरिक्त)। "
            "सन्धि जाँची: प्रायः + वातहरैः → प्रायो वातहरैः (अः + घोष → ओ); दश + अहम् → दशाहम् (अ + अ → आ); रसः + दशाहम् → "
            "रसो दशाहम् (अः + घोष → ओ); लघु-पथ्य-अल्प → लघुपथ्याल्प (अ + अ → आ)।"),
    "119": ("श्लोक (०२.०४.१३४-१३५); विश्वास निम्न; कोई पाठ-चिह्न नहीं। दूसरी पंक्ति अधूरी: क्रिया छपी नहीं (सम्भवतः ‘भजेत्’ पहली "
            "पंक्ति से); ‘ऊर्ध्वम् + पंचमी’ = चार महीनों के बाद (खुला); ‘सुखानि’ की संज्ञा नहीं, शायद बिगड़ा शब्द, पर छपाई में "
            "चिह्न नहीं। इन पर प्रश्न नहीं, केवल क्रम और क्रिया का अभाव। ‘-भ्यः’ रूप (चतुर्भ्यः, मासेभ्यः) पंचमी पढ़े गए। "
            "बलातैल का वर्णन इकाई १२१ में। सन्धि जाँची: स्वेद + अभ्यङ्ग → स्वेदाभ्यङ्ग (अ + अ → आ); बलातैल + आदिकान् → "
            "बलातैलादिकान् (अ + आ → आ); चतुर्भ्यः + मासेभ्यः → चतुर्भ्यो मासेभ्यः (अः + घोष → ओ); ऊर्ध्वम् → ऊर्ध्वं।"),
    "120": ("गद्य-पंक्ति; विश्वास उच्च; कोई पाठ-चिह्न नहीं। इकाई १२१ की विधि का आरम्भ-सूत्र। बला = बरियार (मानक; Sida की जातियाँ भी "
            "इसी नाम से)। उपदेक्ष्यामः = उप-√दिश्, भविष्यत्, उत्तम पुरुष बहुवचन। सन्धि जाँची: बलातैलम् + उपदेक्ष्यामः → "
            "बलातैलमुपदेक्ष्यामः।"),
    "121": ("गद्य-पंक्ति; विश्वास निम्न। पाठ-चिह्न: (१) ‘भागश्चैतुर्दशतैलस्य’: तेल की मात्रा अस्पष्ट (‘चतुर्दश’ एक अनुमान), "
            "पुनर्स्थापित नहीं; (२) ‘ऐकष्ट्यम्’ → ‘ऐक्यम्’ (एक साथ; सम्भावित); (३) ‘अह्वगन्धा’ → ‘अश्वगन्धा’ (सम्भावित); "
            "(४) ‘कालानुसार्थ्य’ → ‘कालानुसार्य’ (सम्भावित); (५) छपा ‘सुभाजने’नु | गुप्तं’ = सुभाजने अनुगुप्तम्। इन पर प्रश्न नहीं। "
            "पहचान डेटा के अनुसार: मानक: देवदारु, मञ्जिष्ठा, चन्दन, कुष्ठ, शतावरी, अश्वगन्धा, पुनर्नवा, वचा, अगुरु, सैन्धव, बला, "
            "यव, कोल, कुलत्थ; सम्भावित: मुद्गपर्णी, माषपर्णी, मधुक, सारिवा, पत्र, त्वक्, सर्ज, शैलेय; विवादित: काकोली, क्षीरकाकोली, "
            "जीवक, ऋषभक, मेदा और महामेदा नामक द्रव्य, तगर, शतपुष्पा; अज्ञात: क्षीरशुक्ला, कालानुसार्य। सन्धि जाँची: तावन्तः + एव → "
            "तावन्त एव (अः + अ से भिन्न स्वर → अ; छपा बिना अन्तर); पयसः + यव → पयसो यव (अः + घोष → ओ); भागः + भागः → "
            "भागो भागः; च + आवाप्य → चावाप्य (अ + आ → आ); शनैः + मृदु → शनैर्मृदु (ऐः + घोष → ऐर्); मृदु + अग्निना → "
            "मृद्वग्निना (उ + अ → व); सुभाजने + अनुगुप्तम् → सुभाजनेऽनुगुप्तम् (ए + अ → एऽ); शतावरी + अश्वगन्धा → "
            "शतावर्यश्वगन्धा (ई + अ → य)।"),
    "122": ("गद्य-पंक्ति; विश्वास निम्न। पाठ-चिह्न: छपा ‘ममोज्वर’ → ‘मनोज्वर’ (सम्भावित; म/न की भूल); ‘दैवाेपघात’ = दैवोपघात "
            "(ओ की मात्रा का छपाई-विभाजन)। ‘राजमात्र’ का अर्थ अस्पष्ट; मर्म वाला समास दो प्रकार से बँट सकता है; ‘ग्रह’ = पकड़ने "
            "वाला, समझाया नहीं। इन पर प्रश्न नहीं। तैलराज = इकाई १२१ का बलातैल; नावन = नस्य; बस्ति = एनिमा। सन्धि जाँची: "
            "एषः + भगवतः → एष भगवतः (एषः का विसर्ग व्यंजन से पहले लुप्त); भगवतः + धन्वन्तरेः → भगवतो धन्वन्तरेः (अः + घोष → ओ); "
            "धन्वन्तरेः + अभिमतः → धन्वन्तरेरभिमतः (एः + स्वर → एर्); अभिमतः + तैलराजः → अभिमतस्तैलराजः (विसर्ग + त → स्); "
            "तैलराजः + राज्ञाम् → तैलराजो राज्ञाम् (अः + घोष → ओ); शिशूनाम् + अतीत → शिशूनामतीत।"),
}

# ===================================================================== AIDS
AIDS = {
    "109": {
        "chunks": "जघनशक्तस्य | जघनकपालानि | दारयित्वेति",
        "sandhi": "आ + इ → ए: दारयित्वा + इति → दारयित्वेति।",
        "frame": "किसका: जघन में अटका (छपा ‘शक्त’, पढ़ा ‘सक्त’) → क्या करें: जघन-कपाल (जघन की हड्डियाँ) तोड़कर → "
                 "क्रिया ‘निकाले’ इकाई १०८ से → ‘इति’: सूची पूरी।",
    },
    "110": {
        "chunks": "भवंति | चात्र",
        "sandhi": "अ + अ → आ: च + अत्र → चात्र।",
        "anchors": "याद-सूत्र: ‘भवन्ति चात्र’ सुनते ही समझो: अब पंक्तियाँ आ रही हैं (इकाई १२६ में भी यही सूत्र छपा है)। (मेरी याद-पद्धति)",
    },
    "111": {
        "chain": {"steps": ["वायु के वश गर्भ का जो-जो अंग अटके", "उस-उस अंग को काटे", "भली प्रकार निकाले",
                            "साथ ही माता को चोट से बचाए"]},
        "chunks": "यद्यद्वायुवशादंगं | सज्जेद्गर्भस्य खंडशः | तत्तच्छित्वा | हरेत्सम्यग् | रक्षेज्जननीं च क्षततः",
        "sandhi": "त् + छ → च्छ: तत् + छित्वा → तच्छित्वा · त् + ज → ज्ज: रक्षेत् + जननीम् → रक्षेज्जननीम् · "
                  "क् + घोष → ग्: सम्यक् + रक्षेत् → सम्यग्रक्षेत्।",
    },
    "112": {
        "chain": {"steps": ["अपरा (जेर) न गिरे", "वैद्य पहले की तरह गिराए", "जिसका शल्य निकला, वह स्त्री",
                            "गरम जल से सिंचन"]},
        "chunks": "अथापतंतीमपरां | पातयेत्पूर्ववद्भिषक् | एवं निर्हृतशल्यां च | सिंचेदुष्णेन वारिणा",
        "sandhi": "त् + घोष → द्: पूर्ववत् + भिषक् → पूर्ववद्भिषक् · त् + स्वर → द्: सिञ्चेत् + उष्णेन → सिञ्चेदुष्णेन।",
    },
    "113": {
        "chain": {"steps": ["शरीर पर अभ्यंग हो चुका", "योनि में स्नेह-पिचु", "योनि मृदु होती है", "पीड़ा शान्त होती है"]},
        "chunks": "दद्यादभ्यक्तदेहायै | योनौ स्नेहपिचुं ततः | योनिर्मृदुर्भवेत्तेन | शूलं चास्याः प्रशाम्यति",
        "sandhi": "इः + घोष → इर्: योनिः + मृदुः → योनिर्मृदुः · उः + घोष → उर्: मृदुः + भवेत् → मृदुर्भवेत् · "
                  "अ + अ → आ: च + अस्याः → चास्याः।",
    },
    "114": {
        "diagram": {"groups": [
            {"label": "द्रव्य (क्रम से)", "items": ["दीप्यक: अजवायन (सम्भावित)", "अतिविषा: अतीस (मानक)",
                                                 "रास्ना: अनुमानित पाठ, विवादित", "हिङ्गु: हींग (मानक)",
                                                 "एला: छोटी इलायची (मानक)", "पञ्चकोलक: पाँच का समूह (नाम यहाँ नहीं)"]},
            {"label": "देने के रूप", "items": ["चूर्ण, स्नेह के साथ", "कल्क (लुगदी)", "क्वाथ (छपा ‘काथ’)"]}]},
        "chunks": "दीप्यकातिविषा | रास्त्रा | हिं ग्वेलापंचकोलकान् | चूर्णं स्नेहेन | कल्कं वा काथं वा | पाययेत्तथा",
        "sandhi": "अ + अ → आ: दीप्यक + अतिविषा → दीप्यकातिविषा · उ + ए → वे: हिङ्गु + एला → हिङ्ग्वेला (छपा ‘हिं ग्वेला’) · "
                  "म् + व्यंजन → ं: चूर्णम् + स्नेहेन → चूर्णं स्नेहेन।",
    },
    "115": {
        "diagram": {"groups": [
            {"label": "द्रव्य (क्रम से)", "items": ["कटुका: कुटकी (मानक)", "अतिविषा: अतीस (मानक)", "पाठा: अकनादि (सम्भावित)",
                                                 "शाक: सागौन की छाल (सम्भावित)", "हिङ्गु (अनुमानित पाठ)",
                                                 "तेजनी (पहचान विवादित)"]},
            {"label": "प्रयोजन", "items": ["दोष का बह निकलना (पाठ अनिश्चित)", "वेदना की शान्ति"]}]},
        "chunks": "कटुकातिविषापाठाशाकत्वग्घिगुतेजनीः | तद्वच्च | दोषस्यंदार्थं | वेदनोपशमायच",
        "sandhi": "त् + च → च्च: तद्वत् + च → तद्वच्च · आ + उ → ओ: वेदना + उपशमाय → वेदनोपशमाय · "
                  "क् + ह → ग्घ: शाकत्वक् + हिङ्गु → शाकत्वग्घिङ्गु।",
    },
    "116": {
        "chunks": "त्रिरात्रमेवं | सप्ताहं | स्नेहमेव ततः पिबेत् | सायं पिबेदरिष्टं च | तथा सुक्कृतमासवं",
        "sandhi": "म् + स्वर: स्नेहम् + एव → स्नेहमेव · त् + स्वर → द्: पिबेत् + अरिष्टम् → पिबेदरिष्टम्।",
        "frame": "अवधि: तीन रात, सात दिन (सम्बन्ध तय नहीं) → तब: केवल स्नेह पिए → सायं: अरिष्ट, और उसी प्रकार भली-भाँति बना आसव।",
    },
    "117": {
        "diagram": {"groups": [
            {"label": "योनि में", "items": ["शिरीष (सिरस) और ककुभ (अर्जुन)", "उनके क्वाथ के पिचु (फाहे) रखे"]},
            {"label": "अन्य उपद्रव", "items": ["जो भी हों", "अपने-अपने अनुसार (यथास्वम्) चिकित्सा"]}]},
        "chunks": "शिरीषककुभकाथपिचून्योनौ च निक्षिपेत् | उपद्रवाश्च येऽन्ये स्युः | तान्यथास्वमुपाचरेत्",
        "sandhi": "विसर्ग + च → श्: उपद्रवाः + च → उपद्रवाश्च · ए + अ → एऽ: ये + अन्ये → येऽन्ये · "
                  "विसर्ग + त → स्: स्युः + तान् → स्युस्तान्।",
    },
    "118": {
        "chunks": "प्रयो वातहरैः सिद्धं | दशांहं भोजने हितं | रसो दशांहं च | परं | लघुपद्व्याल्पभोजना",
        "sandhi": "अ + अ → आ: दश + अहम् → दशाहम् · अः + घोष → ओ: रसः + दशाहम् → रसो दशाहम्।",
        "frame": "दस दिन: वातहर (द्रव्यों) से पका भोजन हितकर → और दस दिन: रस (प्रकार नहीं बताया) → परम् (उसके बाद या उत्तम): "
                 "हल्का, अल्प भोजन (‘पथ्य’ अनुमानित पाठ)।",
    },
    "119": {
        "chunks": "स्वेदाभ्यंगपरा | स्नेहान् बलातैलादिकान् भजेत् | ऊर्ध्वं चतुर्भ्यो मासेभ्यः | सा क्रमेण सुखानि च",
        "sandhi": "अ + अ → आ: स्वेद + अभ्यङ्ग → स्वेदाभ्यङ्ग · अ + आ → आ: बलातैल + आदिकान् → बलातैलादिकान् · "
                  "अः + घोष → ओ: चतुर्भ्यः + मासेभ्यः → चतुर्भ्यो मासेभ्यः।",
        "frame": "वह कैसी: स्वेद और अभ्यंग में लगी → क्या सेवे: बलातैल आदि स्नेह → (दूसरी पंक्ति अधूरी: चार महीनों के बाद, क्रम से, "
                 "सुखद...; क्रिया छपी नहीं)।",
    },
    "120": {
        "chunks": "अथ | बलातैलमुपदेक्ष्यामः",
        "sandhi": "म् + स्वर: बलातैलम् + उपदेक्ष्यामः → बलातैलमुपदेक्ष्यामः।",
        "anchors": "याद-सूत्र: इकाई ११९ में ‘बलातैलादिकान्’ नाम आया, इकाई १२० में उसकी विधि का वादा, इकाई १२१ में विधि। (मेरी याद-पद्धति)",
    },
    "121": {
        "chain": {"steps": ["बला-मूल का काढ़ा: छह भाग", "दूध: उतने ही भाग", "यव-कोल-कुलत्थ-दशमूल का काढ़ा: एक भाग",
                            "तेल: मात्रा अस्पष्ट", "अनेक द्रव्यों के महीन चूर्ण डालें", "धीरे-धीरे मृदु अग्नि पर पकाएँ",
                            "अच्छे पात्र में सुरक्षित रखें"]},
        "chunks": "बलामूलकषायस्य भागाः षट् | तावंतएव पयसो | यवकोलकुलत्थदशमूलकषायस्य भागो | भागश्चैतुर्दशतैलस्य (?) | "
                  "तत्सर्वमैकष्ट्यं (?) कृत्वा | श्लक्ष्णचूर्णानि चावाप्य | काकोली ... सैंधवानि | शनैर्मृद्वग्निना साधयित्वा | "
                  "सुभाजनेऽनु गुप्तं निदध्यात्",
        "sandhi": "उ + अ → व: मृदु + अग्निना → मृद्वग्निना · ऐः + घोष → ऐर्: शनैः + मृदु → शनैर्मृदु · "
                  "ए + अ → एऽ: सुभाजने + अनुगुप्तम् → सुभाजनेऽनुगुप्तम्।",
        "diagram": {"groups": [
            {"label": "मानक", "items": ["देवदारु", "मञ्जिष्ठा", "चन्दन", "कुष्ठ", "शतावरी", "अश्वगन्धा (अनुमानित पाठ)",
                                       "पुनर्नवा", "वचा", "अगुरु", "सैन्धव", "बला"]},
            {"label": "सम्भावित", "items": ["मुद्गपर्णी", "माषपर्णी", "मधुक", "सारिवा", "पत्र", "त्वक्", "सर्ज", "शैलेय"]},
            {"label": "विवादित", "items": ["काकोली", "क्षीरकाकोली", "जीवक", "ऋषभक", "मेदा", "महामेदा", "तगर", "शतपुष्पा"]},
            {"label": "अज्ञात", "items": ["क्षीरशुक्ला", "कालानुसार्य (अनुमानित पाठ)"]}]},
    },
    "122": {
        "diagram": {"groups": [
            {"label": "प्रयोग (क्रम से)", "items": ["पान", "नावन (नाक में)", "अभ्यंग", "बस्ति (एनिमा)"]},
            {"label": "किनके लिए (कुछ, क्रम से)", "items": ["राजा", "कृश", "सूतिका (प्रसूता)", "शिशु", "बीती आयु वाले",
                                                          "सुकुमार", "दीर्घ रोग से क्षीण"]}]},
        "chunks": "एष भगवतो धन्वंतरेरभिमतस्तैलराजो | राज्ञां राजमात्राणां कृशानां सूतिकानां | शिशूनामतीतवयसां सुकुमाराणां | "
                  "महाग्रहगृहीतानां दीर्घरोगक्षपितवपुषां | मर्मविद्ध...विश्लिष्टांगानां | दैवाेपघात...परीतानां | "
                  "पाननावनाभ्यंगबस्तिषु प्रयोज्यः",
        "sandhi": "एः + स्वर → एर्: धन्वन्तरेः + अभिमतः → धन्वन्तरेरभिमतः · विसर्ग + त → स्: अभिमतः + तैलराजः → "
                  "अभिमतस्तैलराजः · अः + घोष → ओ: तैलराजः + राज्ञाम् → तैलराजो राज्ञाम्।",
    },
}

# ===================================================================== IMAGE_SPECS
IMAGE_SPECS = {
    ("111", "chain"): {
        "file": "sh4-anga-chhedana-111.svg",
        "alt": ("Flowchart of unit 111: whatever limb of the fetus gets stuck by the power of wind; cut that limb; remove "
                "it properly; and, alongside, protect the mother from injury."),
        "type": "mermaid",
        "code": ("flowchart TD\n"
                 "  A[\"वायु के वश अंग अटके\"] --> B[\"उस-उस अंग को काटे\"]\n"
                 "  B --> C[\"भली प्रकार निकाले\"]\n"
                 "  B -.- D[\"साथ ही: माता को चोट न लगे\"]\n"
                 "  C -.- D\n"),
    },
    ("112", "chain"): {
        "file": "sh4-apara-patana-112.svg",
        "alt": ("Chain of unit 112: the placenta (aparā) not falling; the physician makes it fall as before; the woman "
                "from whom the śalya is drawn out; sprinkled with warm water."),
        "type": "chain",
        "title": "इकाई ११२: अपरा-पातन, फिर सिंचन",
        "steps": ["अपरा (जेर) न गिरे", "वैद्य पहले की तरह गिराए", "जिसका शल्य निकला, वह स्त्री", "गरम जल से सिंचन"],
    },
    ("113", "chain"): {
        "file": "sh4-sneha-pichu-113.svg",
        "alt": ("Flowchart of unit 113: her body anointed; a swab of oil or fat in the yoni; by that two results: the "
                "yoni becomes soft, and her pain subsides."),
        "type": "mermaid",
        "code": ("flowchart TD\n"
                 "  A[\"शरीर पर अभ्यंग\"] --> B[\"योनि में स्नेह-पिचु\"]\n"
                 "  B --> C[\"योनि मृदु\"]\n"
                 "  B --> D[\"पीड़ा शान्त\"]\n"),
    },
    ("114", "diagram"): {
        "file": "sh4-dipyaka-churna-114.svg",
        "alt": ("Table of unit 114, drugs in line order with labels: dīpyaka, ajwain (probable); ativiṣā, atis "
                "(standard); rāsnā, conjectural reading, disputed; hiṅgu, asafoetida (standard); elā, small cardamom "
                "(standard); pañcakolaka, a group of five not named here; then the forms: powder with sneha, paste, "
                "decoction (printed kātha)."),
        "type": "table",
        "title": "इकाई ११४: द्रव्य और रूप",
        "heads": ["नाम", "पहचान / रूप"],
        "rows": [["दीप्यक", "अजवायन (सम्भावित)"], ["अतिविषा", "अतीस (मानक)"], ["रास्ना", "अनुमानित पाठ; विवादित"],
                 ["हिङ्गु", "हींग (मानक)"], ["एला", "छोटी इलायची (मानक)"], ["पञ्चकोलक", "पाँच का समूह (नाम यहाँ नहीं)"],
                 ["रूप", "चूर्ण स्नेह के साथ, कल्क, या क्वाथ"]],
    },
    ("115", "diagram"): {
        "file": "sh4-katuka-vedana-115.svg",
        "alt": ("Two columns of unit 115. Drugs in line order: kaṭukā, kutki (standard); ativiṣā, atis (standard); "
                "pāṭhā, velvetleaf (probable); śāka bark, teak (probable); hiṅgu (conjectural reading); tejanī "
                "(identity disputed). Purposes: flowing off of the doṣa (uncertain reading); relief of pain."),
        "type": "split",
        "title": "इकाई ११५: द्रव्य और प्रयोजन",
        "cols": [["द्रव्य (क्रम से)", ["१ कटुका: कुटकी (मानक)", "२ अतिविषा: अतीस (मानक)", "३ पाठा: अकनादि (सम्भावित)",
                                      "४ शाक की छाल: सागौन (सम्भावित)", "५ हिङ्गु (अनुमानित पाठ)", "६ तेजनी (विवादित)"]],
                 ["प्रयोजन", ["दोष का बह निकलना (पाठ अनिश्चित)", "वेदना की शान्ति"]]],
    },
    ("121", "chain"): {
        "file": "sh4-balataila-vidhi-121.svg",
        "alt": ("Chain of unit 121, the balātaila recipe: six parts of balā-root decoction; as many parts of milk; one "
                "part of the barley-jujube-horse gram-ten roots decoction; oil, measure unclear; add fine powders of many "
                "drugs; cook slowly on a gentle fire; store well guarded in a good vessel."),
        "type": "chain",
        "title": "इकाई १२१: बलातैल की विधि",
        "steps": ["बला-मूल का काढ़ा: छह भाग", "दूध: उतने ही भाग", "यव-कोल-कुलत्थ-दशमूल काढ़ा: एक भाग",
                  "तेल: मात्रा अस्पष्ट", "महीन चूर्ण डालें", "धीमी मृदु आँच पर पकाएँ", "अच्छे पात्र में सुरक्षित रखें"],
    },
    ("122", "diagram"): {
        "file": "sh4-tailaraja-prayoga-122.svg",
        "alt": ("Table of unit 122: the king of oils (balātaila), approved by Dhanvantari, is used in four ways, numbered "
                "in line order: 1 drinking, 2 nasal administration, 3 anointing, 4 enema."),
        "type": "table",
        "title": "इकाई १२२: धन्वन्तरि को मान्य तैलराज",
        "heads": ["क्रम", "प्रयोग"],
        "rows": [["१", "पान"], ["२", "नावन (नाक में)"], ["३", "अभ्यंग"], ["४", "बस्ति (एनिमा)"]],
    },
}
