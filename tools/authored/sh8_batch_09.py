from helpers import mcq, match, order, fill, multi, accepts


def T(q, teaches):
    q["teaches"] = teaches
    return q


AUTHORED = {}

# ---------------------------------------------------------------- unit 100
AUTHORED["100"] = {
    "title": "इष्टं च पुनर्…",
    "question": "By card 100, which qualities open the long description of a desirable body, and which parts are sure?",
    "rule": ("Desirable (इष्टम्), moreover, is one with: large head, well-developed thighs, fine bones, long fingers, broad "
             "mouth, steady senses, deep navel, red palate, black hair, low-set ears, dense shoulders, and more: one run "
             "of bahuvrīhi compounds."),
    "limits": ("Low confidence. Three stretches are unreadable and 'breath' (उच्छ्वास) is a conjecture: no question on them. "
               "How far each qualifier reaches, and what उभयगुण means, are not settled: questions use only a qualifier "
               "or the part right after it. No noun is printed (data: continues to card 118)."),
    "explain_hi": ("यह कार्ड प्रशस्त (इष्ट) शरीर के लम्बे वर्णन का आरम्भ है: ‘इष्टं च पुनः’ के बाद बहुव्रीहि विशेषणों की एक लम्बी पंक्ति आती है। "
                   "हर समास किसी गुण से शुरू होता है: महा (बड़ा) शिर आदि, उपचित (पुष्ट) ऊरु आदि, सूक्ष्म अस्थि आदि, दीर्घ अंगुलि आदि, विस्तीर्ण मुख आदि, "
                   "स्थिर इन्द्रिय आदि, गंभीर नाभि आदि, रक्त तालु आदि, कृष्ण केश आदि, नीचे बँधे कान आदि, घने कन्धे आदि। "
                   "हर गुण समास के सब अंगों पर लागू होता है या नहीं, यह संस्कृत से तय नहीं; इसलिए प्रश्न केवल गुण के अर्थ या उसके ठीक बाद वाले अंग पर हैं। "
                   "तीन टुकड़े अपठनीय हैं और ‘उच्छ्वास’ (श्वास) केवल अनुमानित पाठ है; इन पर कोई प्रश्न नहीं। "
                   "कोई संज्ञा यहाँ छपी नहीं; डेटा के अनुसार यही वर्णन आगे कार्ड ११८ के ‘शरीरम्’ तक चलता प्रतीत होता है।"),
    "hook": "इष्ट शरीर: बड़ा सिर, गहरी नाभि, लाल तालु, काले केश, घने कन्धे।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "In card 100, what does the opening word इष्टम् mean?",
            ("Desirable", "इष्टम् = desirable (√इष्, past participle): the head word of the whole description."),
            [("Measured", "Measured would be मित or प्रमाणित; इष्टम् means desirable."),
             ("Diseased", "Diseased would be रोगी or आतुर; इष्टम् means desirable."),
             ("Forbidden", "Forbidden would be निषिद्ध; इष्टम् means desirable.")],
            "इष्टं च पुनः = and desirable, moreover.",
            "इष्ट = desirable."),
        order(1, "Put these qualifiers of card 100 in the printed order.",
              ["महा-", "सूक्ष्म-", "विस्तीर्ण-", "गंभीर-", "नीचैर्बद्ध-"],
              "Large (head ...), fine (bones ...), broad (mouth ...), deep (navel ...), set low (ears ...).",
              "महा → सूक्ष्म → विस्तीर्ण → गंभीर → नीचैर्बद्ध."),
        match(2, "Match each qualifier of card 100 to its meaning.",
              [["सूक्ष्म", "fine, slender"], ["गंभीर", "deep"], ["घन", "dense, solid"], ["विस्तीर्ण", "broad"],
               ["उपचित", "well-developed"], ["गूढ", "hidden"]],
              "सूक्ष्म = fine, गंभीर = deep, घन = dense, विस्तीर्ण = broad, उपचित = well-developed, गूढ = hidden.",
              "Each qualifier opens one bahuvrīhi compound.", role="extend",
              teaches="Each compound of card 100 is a bahuvrīhi: गंभीरनाभि... = 'one whose navel ... is deep'."),
        mcq("discriminate", 3, "By card 100, which body part comes right after गंभीर (deep)?",
            ("The navel (नाभि)", "गंभीरनाभिसंधिस्वरं: deep navel, joints and voice."),
            [("The eyebrows (भ्रू)", "The eyebrows stand in the कृष्ण (black) compound, not after गंभीर."),
             ("The thighs (ऊरु)", "The thighs stand after उपचित (well-developed), not after गंभीर."),
             ("The fingers (अंगुलि)", "The fingers stand after दीर्घ (long), not after गंभीर.")],
            "गंभीर → नाभि: the deep navel.",
            "गंभीरनाभि = deep navel."),
        mcq("apply", 4, "By card 100, which quality stands right before the palate (तालु) at the start of its compound?",
            ("Red (रक्त)", "रक्तताल्वोष्ठनखनेत्रांतम्: red palate, lips, nails and eye-corners."),
            [("Fine (सूक्ष्म)", "सूक्ष्म opens the compound of bones, teeth, nails, finger-joints and hair."),
             ("Black (कृष्ण)", "कृष्ण opens the compound of hair, eyebrows, eyes, eyelashes and pupil."),
             ("Hidden (गूढ)", "गूढ opens the compound of jatru, spine and tooth-roots.")],
            "रक्त + तालु: the red palate.",
            "रक्त = red."),
        mcq("transfer", 5, "By the pattern of नीचैः + बद्ध → नीचैर्बद्ध, how is गुणैः + युक्तः (endowed with qualities) joined in a new example?",
            ("गुणैर्युक्तः", "A visarga after ऐ (a vowel other than अ/आ) before the voiced य becomes र्."),
            [("गुणैयुक्तः", "Dropping the visarga before a voiced sound happens after आ, not after ऐ."),
             ("गुणैस्युक्तः", "स् comes from a visarga before त or थ, not before य."),
             ("गुणैश्युक्तः", "श् comes from a visarga before च, छ or श, not before य.")],
            "गुणैः + युक्तः = गुणैर्युक्तः, like नीचैः + बद्ध = नीचैर्बद्ध.",
            "Vowel other than अ/आ + ः, before a voiced sound → र्.",
            teaches="After a vowel other than अ or आ, a visarga before a voiced sound becomes र्: नीचैः + बद्ध → नीचैर्बद्ध."),
    ],
}

# ---------------------------------------------------------------- unit 101
AUTHORED["101"] = {
    "title": "वृत्तस्फिकग्रीवानखं समपृष्ठदंतललाटेक्षितं",
    "question": "By card 101, which parts are round and which are even?",
    "rule": ("The series of card 100 goes on: (one) with jaw ... and tongue; round (वृत्त) buttocks, neck and nails; even "
             "(सम) back, teeth, forehead and gaze."),
    "limits": ("Prose, low confidence. नवमद्य in the first word is unreadable (perhaps मध्य, 'middle'): no meaning, no "
               "question on the first word. The data reads this card as continuing card 100. Whether वृत्त and सम reach "
               "every member is not stated; questions use the printed grouping only."),
    "explain_hi": ("यह कार्ड कार्ड १०० की बहुव्रीहि-पंक्ति को आगे बढ़ाता है; कोई संज्ञा या क्रिया छपी नहीं। "
                   "पहला शब्द हनु (जबड़ा) से शुरू होकर जिह्वा (जीभ) पर समाप्त होता है, पर बीच का ‘नवमद्य’ अपठनीय है। "
                   "दूसरा समास: वृत्त (गोल) नितम्ब, गरदन और नाखून। "
                   "तीसरा समास: सम (समतल) पीठ, दाँत, माथा और ईक्षित (दृष्टि)। "
                   "‘ललाटेक्षितं’ में ललाट + ईक्षित की सन्धि है (अ + ई → ए)।"),
    "hook": "गोल: नितम्ब, गरदन, नाखून। सम: पीठ, दाँत, माथा, दृष्टि।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "In card 101, what does वृत्त mean?",
            ("Round", "वृत्त = round: वृत्तस्फिकग्रीवानखं, round buttocks, neck and nails."),
            [("Even", "Even is सम, the qualifier of the next compound."),
             ("Long", "Long would be दीर्घ; वृत्त means round."),
             ("Small", "Small would be अल्प; वृत्त means round.")],
            "वृत्त = round.",
            "वृत्त = round."),
        order(1, "Put the members of the सम compound of card 101 in the printed order.",
              ["पृष्ठ", "दंत", "ललाट", "ईक्षित"],
              "Even back, teeth, forehead and gaze.",
              "पृष्ठ → दंत → ललाट → ईक्षित."),
        match(2, "Match each sure word of card 101 to its meaning.",
              [["वृत्त", "round"], ["सम", "even"], ["स्फिक", "buttock"], ["ग्रीवा", "neck"], ["ईक्षित", "gaze"]],
              "वृत्त = round, सम = even, स्फिक = buttock, ग्रीवा = neck, ईक्षित = gaze.",
              "वृत्त, सम, स्फिक, ग्रीवा, ईक्षित.", role="extend",
              teaches="ईक्षित, a participle of √ईक्ष् (to see), stands here for the look or gaze."),
        mcq("discriminate", 3, "By card 101, which of these stands in the सम (even) compound?",
            ("The back (पृष्ठ)", "समपृष्ठदंतललाटेक्षितं: even back, teeth, forehead and gaze."),
            [("The buttocks (स्फिक)", "The buttocks stand in the वृत्त (round) compound."),
             ("The neck (ग्रीवा)", "The neck stands in the वृत्त (round) compound."),
             ("The nails (नख)", "The nails stand in the वृत्त (round) compound.")],
            "सम → पृष्ठ, दंत, ललाट, ईक्षित.",
            "समपृष्ठ = even back."),
        mcq("apply", 4, "By which rule does ललाट + ईक्षितम् give ललाटेक्षितम् in card 101?",
            ("अ + ई → ए", "ललाट ends in अ; अ + ई gives ए: ललाटेक्षितम्."),
            [("अ + ई → ऐ", "ऐ comes from अ + ए or अ + ऐ, not from अ + ई."),
             ("अ + ई → ई", "The two vowels merge into ए, not into ई."),
             ("अ + ई → य", "य् comes from इ/ई before a vowel; here अ stands first.")],
            "ललाट + ईक्षितम्: अ + ई → ए.",
            "अ/आ + इ/ई → ए."),
        mcq("transfer", 5, "By the pattern of ललाट + ईक्षितम् → ललाटेक्षितम्, how is गण + ईशः joined in a new example?",
            ("गणेशः", "अ + ई → ए: गण + ईशः → गणेशः."),
            [("गणैशः", "ऐ would need अ + ए or अ + ऐ."),
             ("गणीशः", "अ does not vanish before ई; the two give ए."),
             ("गण्यीशः", "य् comes from इ/ई before a vowel, not from अ.")],
            "गण + ईशः = गणेशः, like ललाट + ईक्षितम् = ललाटेक्षितम्.",
            "अ + ई → ए.",
            teaches="अ or आ before इ or ई merges into ए: ललाट + ईक्षित → ललाटेक्षित."),
    ],
}

# ---------------------------------------------------------------- unit 102
AUTHORED["102"] = {
    "title": "तथाऽनुपूर्ववृत्तावूरू",
    "question": "By card 102, how are the two thighs described?",
    "rule": "Likewise (तथा), the two thighs (ऊरू) are rounded in due succession (अनुपूर्ववृत्तौ).",
    "limits": ("Prose, one word group, no verb. 'Rounded in due order' is usually understood as evenly tapering; the data "
               "gives only the literal sense, so no question on tapering. The avagraha after तथा is a print habit."),
    "explain_hi": ("तथा (इसी प्रकार) दोनों ऊरु यानी जाँघें अनुपूर्व-वृत्त हैं: क्रम से गोल। "
                   "इसे प्रायः क्रम से पतली होती जाती जाँघ समझा जाता है, पर डेटा केवल शब्दार्थ देता है। "
                   "‘ऊरू’ ऊरु का द्विवचन है, और ‘अनुपूर्ववृत्तौ’ भी द्विवचन है। "
                   "‘वृत्तावूरू’ में वृत्तौ + ऊरू की सन्धि है: स्वर से पहले औ → आव्। "
                   "‘तथाऽनुपूर्व’ में अवग्रह केवल छपाई की आदत है; सन्धि तथा + अनुपूर्व (आ + अ → आ) है।"),
    "hook": "दोनों जाँघें: क्रम से गोल।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "In card 102, what does ऊरू mean?",
            ("Two thighs", "ऊरू is the dual of ऊरु, thigh."),
            [("Two arms", "Arms would be बाहू; ऊरू are the thighs."),
             ("Two knees", "Knees would be जानुनी; ऊरू are the thighs."),
             ("Two shoulders", "Shoulders would be स्कन्धौ or अंसौ; ऊरू are the thighs.")],
            "ऊरु = thigh; ऊरू = the two thighs.",
            "ऊरू = two thighs."),
        order(1, "Put the words of card 102 in the printed order.",
              ["तथा", "अनुपूर्ववृत्तौ", "ऊरू"],
              "Likewise; rounded in due succession; the two thighs.",
              "तथा → अनुपूर्ववृत्तौ → ऊरू."),
        match(2, "Match each word of card 102 to its meaning.",
              [["तथा", "likewise"], ["अनुपूर्व", "in due order"], ["वृत्त", "rounded"], ["ऊरु", "thigh"]],
              "तथा = likewise, अनुपूर्व = in due order, वृत्त = rounded, ऊरु = thigh.",
              "तथा, अनुपूर्व, वृत्त, ऊरु.", role="extend",
              teaches="ऊरू and अनुपूर्ववृत्तौ are both dual: the adjective agrees with 'the two thighs'."),
        mcq("discriminate", 3, "Which split of वृत्तावूरू in card 102 is right?",
            ("वृत्तौ + ऊरू", "औ before a vowel → आव्: वृत्तौ + ऊरू → वृत्तावूरू."),
            [("वृत्ताः + ऊरू", "आः before a vowel drops its visarga: that would give वृत्ता ऊरू."),
             ("वृत्ता + वूरू", "वूरू is not a word; the व् comes from the औ."),
             ("वृत्त + आवूरू", "आवूरू is not a word; ऊरू is the dual of ऊरु.")],
            "वृत्तौ (rounded, dual) + ऊरू (two thighs).",
            "औ + vowel → आव्."),
        mcq("apply", 4, "Why does वृत्तौ appear as वृत्ताव् before ऊरू in card 102?",
            ("औ before a vowel → आव्", "ऊरू begins with a vowel: वृत्तौ + ऊरू → वृत्तावूरू."),
            [("औ before a consonant → आव्", "Before a consonant औ stays; आव् arises only before a vowel."),
             ("The ऊ of ऊरू becomes व्", "The ऊ of ऊरू stays; it is the औ of वृत्तौ that changes."),
             ("आव् is the dual's own ending", "The dual ending is -औ; आव् comes only from sandhi.")],
            "वृत्तौ + ऊरू: औ before a vowel → आव्.",
            "औ + vowel → आव्."),
        mcq("transfer", 5, "By the pattern of वृत्तौ + ऊरू → वृत्तावूरू, how is तौ + उभौ (those two, both) joined in a new example?",
            ("तावुभौ", "औ before a vowel → आव्: तौ + उभौ → तावुभौ."),
            [("तोभौ", "ओ would come from अ + उ; here the first vowel is औ."),
             ("तवुभौ", "अव् comes from ओ before a vowel, not from औ."),
             ("तायुभौ", "आय् comes from ऐ before a vowel, not from औ.")],
            "तौ + उभौ = तावुभौ, like वृत्तौ + ऊरू = वृत्तावूरू.",
            "औ + vowel → आव्.",
            teaches="A final औ before a vowel becomes आव्: वृत्तौ + ऊरू → वृत्तावूरू."),
    ],
}

# ---------------------------------------------------------------- unit 103
AUTHORED["103"] = {
    "title": "दक्षिणावर्त्ता नाभिः",
    "question": "By card 103, what is said of the navel?",
    "rule": "The navel (नाभिः) is right-turning (दक्षिणावर्ता): its whorl turns to the right.",
    "limits": ("Prose, high confidence, no verb ('is' understood). It says only 'turning to the right'; nothing about health "
               "or what the turn shows. The printed doubled त्त is normalised to त."),
    "explain_hi": ("नाभि दक्षिणावर्त है, यानी उसका आवर्त (भँवर) दाहिनी ओर घूमता है। "
                   "‘दक्षिणावर्ता’ बहुव्रीहि है: जिसका आवर्त दक्षिण (दाहिनी ओर) हो; आवर्त पुल्लिंग है, पर समास नाभि (स्त्रीलिंग) के अनुसार स्त्रीलिंग ‘-आ’ लेता है। "
                   "सन्धि: दक्षिण + आवर्ता (अ + आ → आ)। "
                   "इससे अधिक कुछ नहीं कहा गया; क्रिया ‘है’ समझी जाती है।"),
    "hook": "नाभि का भँवर: दाहिनी ओर।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "In card 103, what does नाभिः mean?",
            ("The navel", "नाभि = navel (standard)."),
            [("The waist", "Waist would be कटि; नाभि is the navel."),
             ("The chest", "Chest would be वक्षस् or उरस्; नाभि is the navel."),
             ("The palm", "Palm would be तल or हस्ततल; नाभि is the navel.")],
            "नाभि = navel.",
            "नाभि = navel."),
        match(1, "Match each part of card 103 to its meaning.",
              [["दक्षिण", "right (side)"], ["आवर्त", "turn, whorl"], ["नाभि", "navel"]],
              "दक्षिण = right, आवर्त = turn, whorl, नाभि = navel.",
              "दक्षिण, आवर्त, नाभि."),
        T(multi("extend", 2, "Which statements fit card 103?",
                [("It gives the navel a measure", "No: no measure is given; only the turn to the right."),
                 ("दक्षिणावर्ता agrees with नाभिः", "Yes: both are feminine nominative singular."),
                 ("No verb is printed in the line", "Yes: 'is' is understood."),
                 ("It says what the turn shows", "No: nothing more than 'right-turning' is said.")],
                [1, 2],
                "A right-turning navel; the compound agrees with नाभिः; no verb.",
                "दक्षिणावर्ता नाभिः (अस्ति understood)."),
          "A bahuvrīhi such as दक्षिणावर्ता takes the gender of the noun it describes (नाभि, feminine)."),
        mcq("discriminate", 3, "Which split of दक्षिणावर्ता in card 103 is right?",
            ("दक्षिण + आवर्ता", "अ + आ → आ: दक्षिण + आवर्ता → दक्षिणावर्ता."),
            [("दक्षिणः + आवर्ता", "अः before a vowel other than अ loses its visarga: that would give दक्षिण आवर्ता."),
             ("दक्षिण + वर्ता", "That would join as दक्षिणवर्ता, with a short अ."),
             ("दक्षि + णावर्ता", "Neither दक्षि nor णावर्ता is a word.")],
            "दक्षिण (right) + आवर्ता (turn).",
            "अ + आ → आ."),
        mcq("apply", 4, "Why does दक्षिणावर्ता end in -आ in card 103?",
            ("It is feminine, agreeing with नाभिः", "A bahuvrīhi takes the gender of its noun: नाभि is feminine."),
            [("It is a dual, for two navels", "The dual would be -ए; there is one navel, नाभिः."),
             ("It is the instrumental of आवर्त", "The instrumental of an अ-stem ends in -एन, not -आ."),
             ("It is a verb meaning 'it turns'", "A verb would be वर्तते; दक्षिणावर्ता is an adjective.")],
            "दक्षिणावर्ता नाभिः: feminine nominative singular, like नाभिः.",
            "Bahuvrīhi → gender of the noun described."),
        mcq("transfer", 5, "By the pattern of दक्षिणावर्ता नाभिः, what does दीर्घकेशा बाला mean in a new example?",
            ("A girl whose hair is long", "दीर्घकेशा is a bahuvrīhi in the feminine, agreeing with बाला (girl)."),
            [("The long hair of a girl", "That would need केश as the head noun (दीर्घकेशः); -केशा agrees with बाला."),
             ("A girl whose hair is short", "दीर्घ means long, not short (ह्रस्व)."),
             ("A boy whose hair is long", "बाला is feminine: a girl, not a boy (बालः).")],
            "दीर्घकेशा बाला = a girl whose hair is long, like दक्षिणावर्ता नाभिः = a navel whose turn is to the right.",
            "Bahuvrīhi: 'one whose X is Y', in the gender of its noun.",
            teaches="केश is masculine, yet दीर्घकेशा is feminine: a bahuvrīhi agrees with its noun, as आवर्त → दक्षिणावर्ता with नाभिः."),
    ],
}

# ---------------------------------------------------------------- unit 104
AUTHORED["104"] = {
    "title": "स्तनौभ्रुवौ च",
    "question": "By card 104, which two pairs are named, and which word is doubtful?",
    "rule": ("The two breasts (स्तनौ) and the two eyebrows (भ्रुवौ), printed as one word, are two separate dual words; on a "
             "conjectural reading they have a wide interval."),
    "limits": ("Prose, low confidence. Printed प्रकृष्टंतरौ is not a word; 'having a wide interval' (प्रकृष्टान्तरौ) is a "
               "conjecture: no question on it. Between what the interval lies is not stated. No verb."),
    "explain_hi": ("अनुमानित पाठ पर: दोनों स्तन और दोनों भौंहें बड़े अन्तर वाली हों। "
                   "छपा ‘प्रकृष्टंतरौ’ कोई शब्द नहीं; ‘प्रकृष्टान्तरौ’ (बड़े अन्तर वाले) केवल अनुमान है, इसलिए उस पर प्रश्न नहीं। "
                   "‘स्तनौभ्रुवौ’ बिना जगह छपा है, पर ये दो अलग द्विवचन शब्द हैं: स्तनौ (दो स्तन) और भ्रुवौ (दो भौंहें); औ + भ में कोई सन्धि नहीं। "
                   "अन्तर किन दोनों के बीच है, यह पाठ नहीं बताता।"),
    "hook": "दो स्तन, दो भौंहें: दोनों द्विवचन।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "In card 104, what does भ्रुवौ mean?",
            ("The two eyebrows", "भ्रू = eyebrow; भ्रुवौ is its dual."),
            [("The two eyelids", "Eyelids would be वर्त्मनी; भ्रुवौ are the eyebrows."),
             ("The two cheeks", "Cheeks would be कपोलौ or गण्डौ; भ्रुवौ are the eyebrows."),
             ("The two lips", "Lips would be ओष्ठौ; भ्रुवौ are the eyebrows.")],
            "भ्रू = eyebrow; भ्रुवौ = the two eyebrows.",
            "भ्रुवौ = two eyebrows."),
        match(1, "Match each sure word of card 104 to its meaning.",
              [["स्तन", "breast"], ["भ्रू", "eyebrow"], ["च", "and"]],
              "स्तन = breast, भ्रू = eyebrow, च = and.",
              "स्तन, भ्रू, च."),
        mcq("extend", 2, "Why does the data split the printed स्तनौभ्रुवौ into two words?",
            ("Each has its own dual ending", "स्तनौ and भ्रुवौ each end in -औ, the dual; a compound's first part would be the stem स्तन-."),
            [("औ + भ joins into a compound", "There is no sandhi between औ and भ; no compound is formed."),
             ("स्तनौ is the stem form of स्तन", "The stem is स्तन; स्तनौ already carries a case ending."),
             ("The print has a space between them", "The print has no space there; the data adds it.")],
            "स्तनौ + भ्रुवौ: two dual words printed without a space.",
            "A word with its own ending is not the first part of a compound.",
            teaches="Inside a compound only the last member takes the case ending; स्तनौ has its own, so it stands alone."),
        mcq("discriminate", 3, "In card 104, what number are स्तनौ and भ्रुवौ?",
            ("Both are dual", "-औ here marks the dual: two breasts, two eyebrows."),
            [("Both are singular", "The singular would be स्तनः and भ्रूः."),
             ("Both are plural", "The plural would be स्तनाः and भ्रुवः."),
             ("Only स्तनौ is dual", "भ्रुवौ is dual too: two eyebrows.")],
            "स्तनौ, भ्रुवौ: both dual.",
            "-औ = dual here."),
        multi("apply", 4, "Which statements about card 104 are sure?",
              [("स्तनौ and भ्रुवौ are separate words", "Yes: each has its own dual ending."),
               ("The line names the nails and feet", "No: those come in card 105."),
               ("It names the eyelids too", "No: only the breasts and the eyebrows are named."),
               ("No verb is printed in the line", "Yes: the line is elliptical.")],
              [0, 3],
              "Two dual words, joined by च; no verb.",
              "स्तनौ भ्रुवौ च (verb understood)."),
        mcq("transfer", 5, "By the pattern of स्तन → स्तनौ (two breasts), which form of हस्त (hand) names two hands in a new example?",
            ("हस्तौ", "An अ-stem masculine forms its nominative dual in -औ: हस्तौ."),
            [("हस्ताः", "हस्ताः is the plural: many hands."),
             ("हस्तः", "हस्तः is the singular: one hand."),
             ("हस्तान्", "हस्तान् is the accusative plural.")],
            "हस्त → हस्तौ, like स्तन → स्तनौ.",
            "अ-stem masculine, nominative dual: -औ.",
            teaches="Masculine अ-stems form the nominative dual in -औ: स्तन → स्तनौ."),
    ],
}

# ---------------------------------------------------------------- unit 105
AUTHORED["105"] = {
    "title": "नखाः पादौ च",
    "question": "By card 105, which parts are named, and what do their endings show?",
    "rule": ("The nails (नखाः, plural) and the two feet (पादौ, dual) are named; on a conjectural reading they have "
             "tortoise-like elevations."),
    "limits": ("Prose, low confidence. Printed कूर्मान्नतयो is not a regular word; 'tortoise-like elevation' (कूर्मोन्नति) "
               "or 'raised like a tortoise' (कूर्मोन्नत) are conjectures: no question on that word or its ending. No verb."),
    "explain_hi": ("अनुमानित पाठ पर: नाखूनों और दोनों पैरों में कछुए जैसी उठान हो। "
                   "छपा ‘कूर्मान्नतयो’ नियमित शब्द नहीं; ‘कूर्मोन्नतयः’ (कछुए जैसी उठानें) या ‘कूर्मोन्नत’ (कछुए जैसा उठा) अनुमान हैं, इसलिए उस पर प्रश्न नहीं। "
                   "पक्के शब्द: नखाः (नाखून, बहुवचन), पादौ (दो पैर, द्विवचन), च (और)। "
                   "‘नखाः पादौ’ में अघोष प से पहले विसर्ग बना रहता है।"),
    "hook": "नाखून बहुवचन, पैर द्विवचन; बीच में विसर्ग जस का तस।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "In card 105, what does नखाः mean?",
            ("Nails", "नख = nail; नखाः is the plural."),
            [("Teeth", "Teeth would be दन्ताः; नखाः are the nails."),
             ("Fingers", "Fingers would be अङ्गुलयः; नखाः are the nails."),
             ("Heels", "Heels would be पार्ष्णयः; नखाः are the nails.")],
            "नखाः = nails.",
            "नख = nail."),
        order(1, "Put the sure words of card 105 in the printed order.",
              ["नखाः", "पादौ", "च"],
              "Nails; the two feet; and.",
              "नखाः → पादौ → च."),
        mcq("extend", 2, "In card 105, what do the endings of नखाः and पादौ show?",
            ("Nails plural, feet dual", "-आः is the plural (many nails); -औ is the dual (two feet)."),
            [("Nails dual, feet plural", "It is the other way: नखाः is plural, पादौ is dual."),
             ("Nails and feet singular", "The singulars would be नखः and पादः."),
             ("Nails and feet both dual", "The dual of नख would be नखौ; नखाः is plural.")],
            "नखाः = many nails, पादौ = two feet.",
            "-आः plural, -औ dual (masculine अ-stems).",
            teaches="Masculine अ-stems: nominative plural -आः (नखाः), dual -औ (पादौ)."),
        mcq("discriminate", 3, "Why does नखाः keep its visarga before पादौ in card 105?",
            ("Before voiceless प it stays", "प is voiceless: the visarga is kept, नखाः पादौ."),
            [("Before voiced प it stays", "प is not voiced; it is a voiceless consonant."),
             ("आः keeps it before every sound", "Not every: आः drops its visarga before a voiced sound."),
             ("Before प it becomes स्", "स् arises before त or थ, not before प.")],
            "नखाः + पादौ: the voiceless प keeps the visarga.",
            "ः before प/फ stays."),
        match(4, "Match each sure word of card 105 to its meaning.",
              [["नख", "nail"], ["पाद", "foot"], ["च", "and"]],
              "नख = nail, पाद = foot, च = and.",
              "नख, पाद, च.", role="apply"),
        mcq("transfer", 5, "By the pattern of नखाः पादौ, how is देवाः + पश्यन्ति (the gods see) written in a new example?",
            ("देवाः पश्यन्ति", "Before the voiceless प the visarga stays, as in नखाः पादौ."),
            [("देवा पश्यन्ति", "आः drops its visarga only before a voiced sound; प is voiceless."),
             ("देवास्पश्यन्ति", "स् comes from a visarga before त or थ, not before प."),
             ("देवाश्पश्यन्ति", "श् comes from a visarga before च, छ or श, not before प.")],
            "देवाः + पश्यन्ति = देवाः पश्यन्ति, like नखाः + पादौ = नखाः पादौ.",
            "ः before प/फ stays.",
            teaches="A visarga before the voiceless प or फ stays as it is: नखाः पादौ."),
    ],
}

# ---------------------------------------------------------------- unit 106
AUTHORED["106"] = {
    "title": "ऋज्वास्यं नासावंशश्च",
    "question": "By card 106, what is called straight?",
    "rule": "A straight (ऋजु) mouth or face (आस्यम्) and nose-bridge (नासावंशः) are named.",
    "limits": ("Prose, no verb. आस्य = mouth, also face. नासावंश = nasal bridge (probable; literally 'nose-bamboo'). Whether "
               "ऋजु also covers the nose-bridge is not stated in the data's notes."),
    "explain_hi": ("सीधा मुख (आस्य) और नासावंश यानी नाक की डण्डी (सम्भावित)। "
                   "आस्य का अर्थ मुख है, चेहरा भी हो सकता है। "
                   "‘ऋज्वास्यं’ में ऋजु + आस्यम् की सन्धि है: भिन्न स्वर से पहले उ → व्। "
                   "‘नासावंशश्च’ में नासावंशः + च: च से पहले विसर्ग → श्। "
                   "वंश का शब्दार्थ बाँस है; यहाँ नाक की डण्डी।"),
    "hook": "सीधा मुख, बाँस-सी नाक की डण्डी।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "In card 106, what does ऋजु mean?",
            ("Straight", "ऋजु = straight: ऋज्वास्यम्, a straight mouth (face)."),
            [("Broad", "Broad would be विस्तीर्ण; ऋजु means straight."),
             ("Curved", "Curved would be वक्र, the opposite of ऋजु."),
             ("Small", "Small would be अल्प; ऋजु means straight.")],
            "ऋजु = straight.",
            "ऋजु = straight."),
        order(1, "Put the words of card 106 in the printed order.",
              ["ऋजु", "आस्यम्", "नासावंशः", "च"],
              "Straight; mouth; nose-bridge; and.",
              "ऋजु → आस्यम् → नासावंशः → च."),
        match(2, "Match each word of card 106 to its meaning.",
              [["ऋजु", "straight"], ["आस्य", "mouth, face"], ["नासा", "nose"], ["वंश", "ridge (literally bamboo)"]],
              "ऋजु = straight, आस्य = mouth, face, नासा = nose, वंश = ridge.",
              "ऋजु, आस्य, नासा, वंश.", role="extend",
              teaches="नासावंश, 'nose-bamboo', names the ridge of the nose (nasal bridge, probable)."),
        mcq("discriminate", 3, "Which split of ऋज्वास्यं in card 106 is right?",
            ("ऋजु + आस्यम्", "उ before a different vowel → व्: ऋजु + आस्यम् → ऋज्वास्यम्."),
            [("ऋजो + आस्यम्", "ओ before a vowel gives अव्: that would be ऋजवास्यम्."),
             ("ऋजुः + आस्यम्", "उः before a vowel gives उर्: that would be ऋजुरास्यम्."),
             ("ऋज्वा + स्यम्", "Neither ऋज्वा nor स्यम् is the word here.")],
            "ऋजु (straight) + आस्यम् (mouth).",
            "उ + unlike vowel → व्."),
        mcq("apply", 4, "Why is नासावंशः printed नासावंशश् before च in card 106?",
            ("Before च a visarga becomes श्", "च is a palatal: a visarga before च or छ becomes श्."),
            [("Before च a visarga becomes स्", "स् arises before त or थ, not before च."),
             ("Before च a visarga is dropped", "It is not dropped: it becomes श्, as printed."),
             ("श् is the last sound of the stem", "The stem is नासावंश; the श् comes from sandhi.")],
            "नासावंशः + च → नासावंशश्च.",
            "ः + च/छ → श्."),
        mcq("transfer", 5, "By the pattern of ऋजु + आस्यम् → ऋज्वास्यम्, how is गुरु + आज्ञा (the teacher's order) joined in a new example?",
            ("गुर्वाज्ञा", "उ before a different vowel → व्: गुरु + आज्ञा → गुर्वाज्ञा."),
            [("गुरवाज्ञा", "अव् comes from ओ before a vowel, not from उ."),
             ("गुरूज्ञा", "ऊ comes from उ + उ; here the second vowel is आ."),
             ("गुराज्ञा", "उ is not dropped; it becomes व्.")],
            "गुरु + आज्ञा = गुर्वाज्ञा, like ऋजु + आस्यम् = ऋज्वास्यम्.",
            "उ + unlike vowel → व्.",
            teaches="इ, उ, ऋ before a different vowel become य्, व्, र्: ऋजु + आस्यम् → ऋज्वास्यम्."),
    ],
}

# ---------------------------------------------------------------- unit 107
AUTHORED["107"] = {
    "title": "अनुल्बणे हनू वेषश्च",
    "question": "By card 107, what is said of the jaws, and what does the text leave open?",
    "rule": "The two jaws (हनू) are not prominent (अनुल्बणे), and the dress (वेषः) is named too.",
    "limits": ("Prose, no verb. अनुल्बणे is dual and agrees with हनू; whether 'not prominent' also covers वेष is not stated, "
               "and वेष may mean dress or appearance: no question decides what is said of वेष (one asks only that the data leaves it open)."),
    "explain_hi": ("दोनों हनु यानी जबड़े अनुल्बण हों: उभरे हुए या अधिक नहीं। "
                   "‘अनुल्बणे’ स्त्रीलिंग द्विवचन है और ‘हनू’ से मेल खाता है; यहाँ हनु स्त्रीलिंग है। "
                   "‘वेषः’ (पहनावा या रूप) च से जुड़ा है, पर उस पर भी ‘अनुल्बण’ लागू है या नहीं, यह नहीं कहा। "
                   "अन्- स्वर से पहले निषेध करता है: अन् + उल्बण → अनुल्बण। "
                   "‘वेषश्च’ में च से पहले विसर्ग → श्।"),
    "hook": "जबड़े उभरे नहीं; वेष भी साथ में गिना।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "In card 107, what does हनू mean?",
            ("The two jaws", "हनु = jaw (standard); हनू is the dual."),
            [("The two cheeks", "Cheeks would be कपोलौ; हनू are the jaws."),
             ("The two temples", "Temples are शंखौ (card 110); हनू are the jaws."),
             ("The two lips", "Lips would be ओष्ठौ; हनू are the jaws.")],
            "हनू = the two jaws.",
            "हनु = jaw."),
        order(1, "Put the words of card 107 in the printed order.",
              ["अनुल्बणे", "हनू", "वेषः", "च"],
              "Not prominent; the two jaws; the dress; and.",
              "अनुल्बणे → हनू → वेषः → च."),
        match(2, "Match each part of card 107 to its meaning.",
              [["अन्-", "not"], ["उल्बण", "prominent"], ["हनु", "jaw"], ["वेष", "dress"]],
              "अन्- = not, उल्बण = prominent, हनु = jaw, वेष = dress.",
              "अन्-, उल्बण, हनु, वेष.", role="extend",
              teaches="Before a vowel the negative prefix is अन्-: अन् + उल्बण → अनुल्बण."),
        mcq("discriminate", 3, "By the data of card 107, which point is left open?",
            ("Whether वेष is not prominent too", "The note says it is not stated whether अनुल्बण also covers वेष."),
            [("Whether हनू is a dual form", "That is stated: हनू is feminine dual, two jaws."),
             ("Whether अनुल्बणे agrees with हनू", "That is stated: both are feminine dual."),
             ("Whether हनु here means the jaw", "That is stated: हनु = jaw (standard).")],
            "Sure: not-prominent jaws; open: what is said of वेष.",
            "च adds वेष; what is said of it is not stated."),
        multi("apply", 4, "Which statements about card 107 are sure?",
              [("It calls the jaws very prominent", "No: अन्-उल्बण means not prominent."),
               ("अनुल्बणे is dual, like हनू", "Yes: both are feminine dual."),
               ("वेष must mean the face here", "No: वेष is dress or appearance."),
               ("हनु is feminine in this line", "Yes: the data takes हनु as feminine here.")],
              [1, 3],
              "Not-prominent jaws (feminine dual); वेष added with च.",
              "अनुल्बणे हनू (f. du.)."),
        mcq("transfer", 5, "By the pattern of अन् + उल्बण → अनुल्बण, how is the negative of उचित (proper) formed in a new example?",
            ("अनुचित", "Before a vowel the negative is अन्-: अन् + उचित → अनुचित."),
            [("अउचित", "अ- is used only before a consonant; before a vowel it is अन्-."),
             ("नउचित", "न + उ would not stay apart (it would join as नो-), and before a vowel the usual negative prefix is अन्-."),
             ("अनोचित", "ओ would come from अ + उ; here न् simply joins the उ.")],
            "अनुचित = not proper, like अनुल्बण = not prominent.",
            "Negative prefix: अ- before a consonant, अन्- before a vowel.",
            teaches="The negative prefix is अ- before a consonant and अन्- before a vowel: अन् + उल्बण → अनुल्बण."),
    ],
}

# ---------------------------------------------------------------- unit 108
AUTHORED["108"] = {
    "title": "श्लक्ष्णं तालु जिह्वा च",
    "question": "By card 108, what is called smooth?",
    "rule": "The palate (तालु) is smooth (श्लक्ष्णम्), and the tongue (जिह्वा) is named too.",
    "limits": ("Prose, high confidence, no verb. श्लक्ष्णम् is neuter and agrees with तालु; whether it also covers the tongue "
               "is not stated: no question on that."),
    "explain_hi": ("तालु चिकना (श्लक्ष्ण) हो, और जिह्वा (जीभ) भी गिनी गई है। "
                   "‘श्लक्ष्णम्’ नपुंसकलिंग है और ‘तालु’ (नपुंसक) से मेल खाता है। "
                   "जीभ भी चिकनी हो, यह पाठ स्पष्ट नहीं कहता। "
                   "‘श्लक्ष्णं तालु’ में वाक्य के भीतर व्यंजन से पहले अन्तिम म् अनुस्वार (ं) लिखा गया है।"),
    "hook": "चिकना तालु, साथ में जीभ।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "In card 108, what does श्लक्ष्ण mean?",
            ("Smooth", "श्लक्ष्ण = smooth: श्लक्ष्णं तालु, the smooth palate."),
            [("Rough", "Rough would be खर or परुष, the opposite."),
             ("Dry", "Dry would be शुष्क or रूक्ष; श्लक्ष्ण means smooth."),
             ("Bitter", "Bitter would be तिक्त; श्लक्ष्ण means smooth.")],
            "श्लक्ष्ण = smooth.",
            "श्लक्ष्ण = smooth."),
        order(1, "Put the words of card 108 in the printed order.",
              ["श्लक्ष्णं", "तालु", "जिह्वा", "च"],
              "Smooth; the palate; the tongue; and.",
              "श्लक्ष्णं → तालु → जिह्वा → च."),
        match(2, "Match each word of card 108 to its meaning.",
              [["श्लक्ष्ण", "smooth"], ["तालु", "palate"], ["जिह्वा", "tongue"], ["च", "and"]],
              "श्लक्ष्ण = smooth, तालु = palate, जिह्वा = tongue, च = and.",
              "श्लक्ष्ण, तालु, जिह्वा, च.", role="extend",
              teaches="तालु is a neuter उ-stem: its nominative singular is तालु, without an ending."),
        mcq("discriminate", 3, "In card 108, which word does श्लक्ष्णम् match in gender?",
            ("तालु, a neuter", "श्लक्ष्णम् is neuter singular, like तालु."),
            [("जिह्वा, a feminine", "The feminine would be श्लक्ष्णा; श्लक्ष्णम् is neuter."),
             ("Both, as a dual", "A dual would end in -ए or -औ; श्लक्ष्णम् is singular."),
             ("च, as a noun", "च is an indeclinable 'and', not a noun.")],
            "श्लक्ष्णम् (n. sg.) ↔ तालु (n. sg.).",
            "An adjective agrees in gender with its noun."),
        fill(4, "The word for 'tongue' in card 108 is ____ (type it in Devanagari or in English letters, e.g. dharma).",
             accepts("जिह्वा", None, "jivha"),
             "जिह्वा = tongue: श्लक्ष्णं तालु जिह्वा च.",
             "जिह्वा (tongue) is a feminine आ-stem; card 100 prints the variant spelling जिव्हा.",
             "जिह्वा = tongue.", role="apply"),
        mcq("transfer", 5, "By the pattern of श्लक्ष्णं तालु, how is फलम् + खादति (eats the fruit) written in a new example?",
            ("फलं खादति", "Final म् before a consonant inside a sentence is written as anusvāra (ं)."),
            [("फलो खादति", "ओ comes from अः before a voiced consonant, not from म्."),
             ("फला खादति", "म् is not dropped with a long आ; it becomes ं."),
             ("फलः खादति", "म् does not turn into a visarga.")],
            "फलम् + खादति = फलं खादति, like श्लक्ष्णम् + तालु = श्लक्ष्णं तालु.",
            "Final म् + consonant → ं.",
            teaches="Inside a sentence a final म् before a consonant is written as anusvāra: श्लक्ष्णं तालु."),
    ],
}

# ---------------------------------------------------------------- unit 109
AUTHORED["109"] = {
    "title": "नातिस्थूलकृशावोष्ठौ देहबंधश्च",
    "question": "By card 109, how are the lips described, and what else is named?",
    "rule": "The two lips (ओष्ठौ) are neither very stout nor very lean (नातिस्थूलकृशौ), and the body's build (देहबन्धः) is named too.",
    "limits": ("Prose, no verb. Whether 'neither very stout nor lean' also covers देहबन्ध is not stated: no question on "
               "that. देहबन्ध = binding or structure of the body (frame, build)."),
    "explain_hi": ("दोनों होंठ न बहुत मोटे हों, न बहुत दुबले; और देहबन्ध (शरीर की बनावट) भी गिना गया है। "
                   "‘नाति’ = न + अति (अ + अ → आ): ‘बहुत नहीं’। "
                   "‘कृशावोष्ठौ’ में कृशौ + ओष्ठौ की सन्धि है: स्वर से पहले औ → आव्। "
                   "देहबन्ध पर भी यही गुण लागू है या नहीं, यह नहीं कहा। "
                   "‘देहबंधश्च’ में च से पहले विसर्ग → श्।"),
    "hook": "होंठ: न बहुत मोटे, न बहुत पतले।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "In card 109, what does ओष्ठौ mean?",
            ("The two lips", "ओष्ठ = lip; ओष्ठौ is the dual."),
            [("The two cheeks", "Cheeks would be कपोलौ; ओष्ठौ are the lips."),
             ("The two jaws", "The jaws are हनू (card 107); ओष्ठौ are the lips."),
             ("The two gums", "Gums would be दन्तमांस; ओष्ठौ are the lips.")],
            "ओष्ठौ = the two lips.",
            "ओष्ठ = lip."),
        order(1, "Put the words of card 109 in the printed order.",
              ["नातिस्थूलकृशौ", "ओष्ठौ", "देहबंधः", "च"],
              "Neither very stout nor lean; the two lips; the body's build; and.",
              "नातिस्थूलकृशौ → ओष्ठौ → देहबंधः → च."),
        match(2, "Match each word of card 109 to its meaning.",
              [["अति", "very"], ["स्थूल", "stout"], ["कृश", "lean"], ["ओष्ठ", "lip"], ["देहबन्ध", "build of the body"]],
              "अति = very, स्थूल = stout, कृश = lean, ओष्ठ = lip, देहबन्ध = build of the body.",
              "अति, स्थूल, कृश, ओष्ठ, देहबन्ध.", role="extend",
              teaches="न + अति → नाति, 'not too': नातिस्थूलकृश = neither too stout nor too lean."),
        mcq("discriminate", 3, "Which split of कृशावोष्ठौ in card 109 is right?",
            ("कृशौ + ओष्ठौ", "औ before a vowel → आव्: कृशौ + ओष्ठौ → कृशावोष्ठौ."),
            [("कृशाः + ओष्ठौ", "आः before a vowel drops its visarga: that would give कृशा ओष्ठौ."),
             ("कृशा + वोष्ठौ", "वोष्ठौ is not a word; the व् comes from the औ."),
             ("कृश + आवोष्ठौ", "आवोष्ठौ is not a word; ओष्ठौ means the lips.")],
            "कृशौ (lean, dual) + ओष्ठौ (two lips).",
            "औ + vowel → आव्."),
        mcq("apply", 4, "By card 109, how are the lips described?",
            ("Not too stout and not too lean", "न-अति-स्थूल-कृशौ: neither very stout nor very lean."),
            [("Very stout and very broad", "अति is negated by न: the lips are not very stout."),
             ("Very lean and very small", "अति is negated by न: the lips are not very lean."),
             ("Thick at one end, thin at the other", "The line names no change along the lip.")],
            "नातिस्थूलकृशौ: the middle measure.",
            "न + अति = not too."),
        mcq("transfer", 5, "By the pattern of न + अति → नाति, how is न + अधिकम् (not more) joined in a new example?",
            ("नाधिकम्", "अ + अ → आ: न + अधिकम् → नाधिकम्."),
            [("नधिकम्", "The two अ merge into a long आ; neither is lost."),
             ("नेधिकम्", "ए would come from अ + इ; here both vowels are अ."),
             ("नोधिकम्", "ओ would come from अ + उ; here both vowels are अ.")],
            "न + अधिकम् = नाधिकम्, like न + अति = नाति.",
            "अ + अ → आ.",
            teaches="अ + अ merge into आ: न + अति → नाति."),
    ],
}

# ---------------------------------------------------------------- unit 110
AUTHORED["110"] = {
    "title": "सस्पंदं हृदयं शंखौ मन्ये च",
    "question": "By card 110, what is called throbbing, and which other parts are named?",
    "rule": ("The heart (हृदयम्) is with throbbing (सस्पन्दम्); the two temples (शङ्खौ) and the two manyā (मन्ये) are "
             "named too."),
    "limits": ("Prose, no verb. Whether 'with throbbing' also covers the temples and manyā is not stated: no question on "
               "that. मन्या = side-neck structures, probably the vessels (probable; 'carotid' is a modern guess): no "
               "question on what they are."),
    "explain_hi": ("हृदय सस्पन्द हो, यानी धड़कन सहित; दोनों शंख यानी कनपटियाँ और दोनों मन्या भी गिनी गई हैं। "
                   "‘सस्पन्दम्’ बहुव्रीहि है: स (सहित) + स्पन्द (धड़कन); नपुंसक होने से यह ‘हृदयम्’ से मेल खाता है। "
                   "कनपटियों और मन्या पर भी धड़कन कही गई है या नहीं, यह स्पष्ट नहीं। "
                   "मन्या = गरदन के दोनों ओर की संरचनाएँ, सम्भवतः वहाँ की रक्तवाहिनियाँ (सम्भावित; ‘कैरोटिड’ आधुनिक अनुमान है)।"),
    "hook": "धड़कता हृदय; साथ में कनपटियाँ और मन्या।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "In card 110, what does हृदयम् mean?",
            ("The heart", "हृदय = heart (standard)."),
            [("The lungs", "Lungs would be फुफ्फुस; हृदय is the heart."),
             ("The navel", "Navel is नाभि (card 103); हृदय is the heart."),
             ("The throat", "Throat would be कण्ठ; हृदय is the heart.")],
            "हृदय = heart.",
            "हृदय = heart."),
        order(1, "Put the words of card 110 in the printed order.",
              ["सस्पंदं", "हृदयं", "शंखौ", "मन्ये", "च"],
              "With throbbing; the heart; the two temples; the two manyā; and.",
              "सस्पंदं → हृदयं → शंखौ → मन्ये → च."),
        match(2, "Match each part of card 110 to its meaning.",
              [["स-", "with"], ["स्पन्द", "throbbing"], ["हृदय", "heart"], ["शङ्ख", "temple"]],
              "स- = with, स्पन्द = throbbing, हृदय = heart, शङ्ख = temple.",
              "स-, स्पन्द, हृदय, शङ्ख.", role="extend",
              teaches="स- before a noun makes a bahuvrīhi 'having X': स + स्पन्द = with throbbing."),
        mcq("discriminate", 3, "In card 110, which word does सस्पन्दम् match in gender?",
            ("हृदयम्, a neuter", "सस्पन्दम् is neuter singular, like हृदयम्."),
            [("शङ्खौ, a masculine", "शङ्खौ is masculine dual; सस्पन्दम् is neuter singular."),
             ("मन्ये, a feminine", "मन्ये is feminine dual; सस्पन्दम् is neuter singular."),
             ("All three, as a plural", "सस्पन्दम् is singular, not plural.")],
            "सस्पन्दम् (n. sg.) ↔ हृदयम् (n. sg.).",
            "An adjective agrees in gender and number with its noun."),
        mcq("apply", 4, "By card 110, what are the शङ्खौ?",
            ("The two temples", "शङ्ख = temple (standard): शङ्खौ, the two temples."),
            [("The two cheeks", "Cheeks would be कपोलौ; शङ्खौ are the temples."),
             ("The two ears", "Ears would be कर्णौ; शङ्खौ are the temples."),
             ("The two eyebrows", "Eyebrows are भ्रुवौ (card 104); शङ्खौ are the temples.")],
            "शङ्खौ = the two temples.",
            "शङ्ख = temple (here)."),
        mcq("transfer", 5, "By the pattern of सस्पन्दम् (with throbbing), what does सक्रोध mean in a new example?",
            ("With anger", "स- = with: स + क्रोध = having anger."),
            [("Without anger", "Without would need अ- or निः-: अक्रोध, निष्क्रोध."),
             ("Great anger", "Great would need महा-: महाक्रोध."),
             ("Cause of anger", "A cause would need कारण or हेतु: क्रोधकारण.")],
            "सक्रोध = with anger, like सस्पन्द = with throbbing.",
            "स- + noun = having that noun.",
            teaches="स- before a noun means 'with, having': सस्पन्द = with throbbing."),
    ],
}

# ---------------------------------------------------------------- unit 111
AUTHORED["111"] = {
    "title": "सोष्म तालुपादोदरं निःश्वासश्च",
    "question": "By card 111, which parts are warm, and what else is named?",
    "rule": ("Warm (सोष्म) are the palate, feet and belly (तालुपादोदरम्, one neuter whole); the outbreath (निःश्वासः) is "
             "named too."),
    "limits": ("Prose, no verb. सोष्म is neuter and agrees with the neuter dvandva; whether the outbreath is also called "
               "warm is not stated: no question on that."),
    "explain_hi": ("तालु, पैर और पेट गरम (सोष्म) हों, और निःश्वास भी गिना गया है। "
                   "‘तालुपादोदरम्’ समाहार द्वन्द्व है: तीन अंग एक नपुंसक एकवचन इकाई के रूप में। "
                   "‘सोष्म’ = स + ऊष्म (अ + ऊ → ओ): गरमी सहित। "
                   "‘पादोदरं’ में पाद + उदरम् (अ + उ → ओ)। "
                   "निःश्वास भी गरम हो, यह स्पष्ट नहीं कहा।"),
    "hook": "गरम: तालु, पैर, पेट; साथ में साँस।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "In card 111, what does उदर mean?",
            ("The belly", "उदर = belly: तालुपादोदरम्, palate, feet and belly."),
            [("The back", "Back would be पृष्ठ; उदर is the belly."),
             ("The chest", "Chest would be वक्षस्; उदर is the belly."),
             ("The waist", "Waist would be कटि; उदर is the belly.")],
            "उदर = belly.",
            "उदर = belly."),
        order(1, "Put the words of card 111 in the printed order.",
              ["सोष्म", "तालुपादोदरं", "निःश्वासः", "च"],
              "Warm; palate, feet and belly; the outbreath; and.",
              "सोष्म → तालुपादोदरं → निःश्वासः → च."),
        match(2, "Match each word of card 111 to its meaning.",
              [["ऊष्म", "warmth"], ["तालु", "palate"], ["पाद", "foot"], ["उदर", "belly"], ["निःश्वास", "outbreath"]],
              "ऊष्म = warmth, तालु = palate, पाद = foot, उदर = belly, निःश्वास = outbreath.",
              "ऊष्म, तालु, पाद, उदर, निःश्वास.", role="extend",
              teaches="तालुपादोदरम् is a samāhāra dvandva: several things taken as one neuter singular whole."),
        mcq("discriminate", 3, "Which split of सोष्म in card 111 is right?",
            ("स + ऊष्म", "अ + ऊ → ओ: स + ऊष्म → सोष्म, with warmth."),
            [("सः + ऊष्म", "अः before a vowel other than अ loses its visarga: that would give स ऊष्म."),
             ("सो + ऊष्म", "ओ before a vowel gives अव्: that would be सवूष्म."),
             ("सोष् + म", "Neither सोष् nor म is the word here.")],
            "स (with) + ऊष्म (warmth).",
            "अ + ऊ → ओ."),
        mcq("apply", 4, "Why is तालुपादोदरम् singular though it names three parts?",
            ("A samāhāra dvandva: one neuter whole", "The three parts are taken together as one neuter singular."),
            [("Only the belly is meant by the word", "All three are meant: palate, feet and belly."),
             ("The singular is a misprint for the plural", "No misprint is flagged; the samāhāra form is singular."),
             ("तालु and पाद only describe the belly", "They are members of a dvandva, not qualifiers.")],
            "तालु + पाद + उदर → तालुपादोदरम् (n. sg.).",
            "Samāhāra dvandva → neuter singular."),
        mcq("transfer", 5, "By the pattern of स + ऊष्म → सोष्म, how is जल + ऊर्मिः (a wave of water) joined in a new example?",
            ("जलोर्मिः", "अ + ऊ → ओ: जल + ऊर्मिः → जलोर्मिः."),
            [("जलौर्मिः", "औ would come from अ + ओ or अ + औ."),
             ("जलूर्मिः", "अ does not vanish before ऊ; the two give ओ."),
             ("जल्वूर्मिः", "व् comes from उ/ऊ before a vowel; here अ stands first.")],
            "जल + ऊर्मिः = जलोर्मिः, like स + ऊष्म = सोष्म.",
            "अ + ऊ → ओ.",
            teaches="अ or आ before उ or ऊ merges into ओ: स + ऊष्म → सोष्म."),
    ],
}

# ---------------------------------------------------------------- unit 112
AUTHORED["112"] = {
    "title": "पृष्ठतोऽवनतौ रोमशौ च कर्णौ",
    "question": "By card 112, how are the two ears described?",
    "rule": "The two ears (कर्णौ) are bent down at the back (पृष्ठतः अवनतौ) and hairy (रोमशौ).",
    "limits": ("Prose, no verb. पृष्ठतः = at or from the back; the exact place of the bend is not stated: no question on "
               "it."),
    "explain_hi": ("दोनों कान पीछे की ओर झुके हुए (पृष्ठतः अवनतौ) और रोमयुक्त (रोमशौ) हों। "
                   "झुकाव ठीक कहाँ है, यह पाठ नहीं बताता। "
                   "‘पृष्ठतोऽवनतौ’ में पृष्ठतः + अवनतौ की सन्धि है: अः + अ → ओ, और अगले अ का लोप अवग्रह (ऽ) से दिखाया गया। "
                   "‘अवनतौ’, ‘रोमशौ’ और ‘कर्णौ’ तीनों पुल्लिंग द्विवचन हैं।"),
    "hook": "कान: पीछे झुके, रोमयुक्त।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "In card 112, what does कर्णौ mean?",
            ("The two ears", "कर्ण = ear; कर्णौ is the dual."),
            [("The two eyes", "Eyes would be नेत्रे; कर्णौ are the ears."),
             ("The two cheeks", "Cheeks would be कपोलौ; कर्णौ are the ears."),
             ("The two shoulders", "Shoulders would be स्कन्धौ; कर्णौ are the ears.")],
            "कर्णौ = the two ears.",
            "कर्ण = ear."),
        order(1, "Put the words of card 112 in the printed order.",
              ["पृष्ठतः", "अवनतौ", "रोमशौ", "च", "कर्णौ"],
              "At the back; bent down; hairy; and; the two ears.",
              "पृष्ठतः → अवनतौ → रोमशौ → च → कर्णौ."),
        match(2, "Match each word of card 112 to its meaning.",
              [["पृष्ठतः", "at the back"], ["अवनत", "bent down"], ["रोमश", "hairy"], ["कर्ण", "ear"]],
              "पृष्ठतः = at the back, अवनत = bent down, रोमश = hairy, कर्ण = ear.",
              "पृष्ठतः, अवनत, रोमश, कर्ण.", role="extend",
              teaches="-तः after a noun makes an adverb of place: पृष्ठ (back) → पृष्ठतः (at the back)."),
        mcq("discriminate", 3, "Which split of पृष्ठतोऽवनतौ in card 112 is right?",
            ("पृष्ठतः + अवनतौ", "अः + अ → ओ, the second अ shown by ऽ: पृष्ठतोऽवनतौ."),
            [("पृष्ठता + अवनतौ", "आ + अ → आ: that would give पृष्ठतावनतौ."),
             ("पृष्ठतो + वनतौ", "वनतौ is not a word; the word is अवनतौ, bent down."),
             ("पृष्ठत + ओऽवनतौ", "Neither पृष्ठत nor ओऽवनतौ is the word here.")],
            "पृष्ठतः (at the back) + अवनतौ (bent down).",
            "अः + अ → ओऽ."),
        mcq("apply", 4, "Why is पृष्ठतः printed पृष्ठतो with ऽ before अवनतौ in card 112?",
            ("अः before अ gives ओ, then ऽ", "अः + अ → ओ, and the lost अ is shown by the avagraha ऽ."),
            [("अः before any vowel gives ओ", "Not any: before vowels other than अ, अः becomes अ."),
             ("आः before अ gives ओ", "पृष्ठतः ends in अः, and आः drops its visarga before a vowel."),
             ("ओ is the adverb's own ending", "The adverb ends in -तः; ओ comes only from sandhi.")],
            "पृष्ठतः + अवनतौ → पृष्ठतोऽवनतौ.",
            "अः + अ → ओऽ."),
        mcq("transfer", 5, "By the pattern of पृष्ठतः + अवनतौ → पृष्ठतोऽवनतौ, how is बालः + अयम् (this boy) joined in a new example?",
            ("बालोऽयम्", "अः + अ → ओ, the अ shown by ऽ: बालोऽयम्."),
            [("बाल अयम्", "अः becomes अ only before vowels other than अ."),
             ("बालायम्", "आ would come from अ + अ without a visarga."),
             ("बालरयम्", "र् comes from a visarga after a vowel other than अ/आ.")],
            "बालः + अयम् = बालोऽयम्, like पृष्ठतः + अवनतौ = पृष्ठतोऽवनतौ.",
            "अः + अ → ओऽ.",
            teaches="अः before अ becomes ओ and the अ is dropped, marked by ऽ: पृष्ठतः + अवनतौ → पृष्ठतोऽवनतौ."),
    ],
}

# ================================================================ NOTES_HI
NOTES_HI = {
    "100": ("गद्य; विश्वास कम; एक छपी पंक्ति (०२.०८.११८)। बहुव्रीहि विशेषणों की लम्बी शृंखला, सब प्रथमा/द्वितीया एकवचन (डेटा लिंग नहीं बताता); "
            "कोई संज्ञा छपी नहीं; डेटा के अनुसार वर्णन कार्ड १०१ में जारी है और कार्ड ११८ (‘शरीरम्’) तक चलता प्रतीत होता है। "
            "पाठ-चिह्न (सम्भव): ‘बाहूच्च्छासेक्षित’ में अतिरिक्त च, ‘उच्छास’ कोई शब्द नहीं, ‘उच्छ्वास’ (श्वास) अनुमानित पाठ; ‘लालटा’ = ललाट; "
            "‘मेंढ्र’ = मेढ्र (मानक: शिश्न); ‘जिव्हा’ = जिह्वा (वर्तनी-भेद)। तीन टुकड़े अपठनीय, अविभक्त रखे गए: ‘त्वकचकरजन’, "
            "‘शुक्लशुकंमंडलदशनचरित’, ‘वंतांगुलि’ (शायद आवर्ताङ्गुलि या अवनताङ्गुलि); समीक्षक का अनुमान त्वक्-कच-करज (त्वचा, केश, नाखून) लागू नहीं किया गया। "
            "अंगों के बीच ‘चित्त’ (मन) सम्भवतः छपाई की भूल है (सुधारा नहीं)। हर गुण समास के सब अंगों पर लागू है या नहीं (महा, उपचित, दीर्घ), और ‘उभयगुण’ "
            "क्या है, यह निश्चित नहीं। ‘अधरोष्ठ’ एक (निचला होंठ) या दो अंग भी हो सकते हैं। जत्रु = हँसली का स्थान (सम्भावित), पृष्ठवंश = रीढ़ (सम्भावित), "
            "स्तनाग्र = स्तन का अग्र (सम्भावित: चूचुक)। सन्धि जाँची: पुनर् + महा → पुनर्महा; -स्वरम् + उपचित → -स्वरमुपचित; उपचित + ऊरु → उपचितोरु "
            "(अ + ऊ → ओ); वक्षस् + ग्रीवा → वक्षोग्रीवा (अस् + घोष व्यंजन → ओ); वक्षः + अल्प → वक्षोऽल्प (अः + अ → ओऽ); स्थिर + इन्द्रिय → स्थिरेन्द्रिय "
            "(अ + इ → ए); नीचैः + बद्ध → नीचैर्बद्ध (ऐः + घोष → ऐर्); नेत्र + अन्तम् → नेत्रान्तम्; नासा + अग्र → नासाग्र; ललाट + उदर → ललाटोदर।"),
    "101": ("गद्य; विश्वास कम; एक छपी पंक्ति (०२.०८.११९)। डेटा के अनुसार कार्ड १०० की शृंखला जारी। पाठ-चिह्न (सम्भव क्षति): ‘नवमद्य’ "
            "का कोई पक्का पाठ नहीं; ‘मद्य’ शायद ‘मध्य’ (बीच) की भूल; अर्थ नहीं दिया गया; ‘जिह्वं’ को हनु और अस्पष्ट अंश वाले समास का अन्तिम पद "
            "माना गया, यह भी अनिश्चित। पहले शब्द पर कोई प्रश्न नहीं। ईक्षित = दृष्टि। सन्धि जाँची: ललाट + ईक्षितम् → ललाटेक्षितम् (अ + ई → ए); "
            "छपा ‘दंत’ अनुस्वार के साथ = दन्त।"),
    "102": ("गद्य; विश्वास मध्यम; एक छपी पंक्ति (०२.०८.१२०); कोई पाठ-चिह्न नहीं। ‘तथाऽनुपूर्व’ में अवग्रह छपाई की आदत है; सन्धि तथा + अनुपूर्व "
            "(आ + अ → आ)। ‘अनुपूर्ववृत्त’ = क्रम से गोल; प्रायः ‘क्रम से पतली होती’ समझा जाता है, पर डेटा केवल शब्दार्थ देता है। क्रिया नहीं। "
            "सन्धि जाँची: वृत्तौ + ऊरू → वृत्तावूरू (स्वर से पहले औ → आव्)। ऊरू = ऊरु का पुं. द्विवचन।"),
    "103": ("गद्य; विश्वास उच्च; एक छपी पंक्ति (०२.०८.१२१); कोई पाठ-चिह्न नहीं। क्रिया ‘है’ समझी जाती है। छपा दुहरा ‘त्त’ (दक्षिणावर्त्ता) "
            "सामान्य ‘त’ माना गया। दक्षिणावर्त = दाहिनी ओर घूमा हुआ; इससे आगे कुछ नहीं कहा। बहुव्रीहि का लिंग नाभि (स्त्री.) से। "
            "सन्धि जाँची: दक्षिण + आवर्ता → दक्षिणावर्ता (अ + आ → आ)।"),
    "104": ("गद्य; विश्वास कम; एक छपी पंक्ति (०२.०८.१२२)। पाठ-चिह्न (सम्भव): छपा ‘प्रकृष्टंतरौ’ कोई शब्द नहीं; अनुस्वार से पहले आ की मात्रा "
            "छूटी मानकर ‘प्रकृष्टान्तरौ’ (बड़े अन्तर वाले) पढ़ा गया; अनुवाद अनुमानित पाठ पर है; इस पर प्रश्न नहीं। पाठ-चिह्न: ‘स्तनौभ्रुवौ’ बिना जगह छपा, "
            "शब्द स्तनौ + भ्रुवौ (औ + भ में कोई सन्धि नहीं), समास नहीं। अन्तर हर जोड़े के दोनों सदस्यों के बीच माना गया; पाठ यह नहीं कहता। क्रिया नहीं।"),
    "105": ("गद्य; विश्वास कम; एक छपी पंक्ति (०२.०८.१२३)। पाठ-चिह्न (सम्भव): ‘कूर्मान्नतयो’ नियमित शब्द नहीं; ‘आ’ को ‘ओ’ की भूल मानकर "
            "‘कूर्मोन्नतयः’ (कछुए जैसी उठानें, स्त्री. बहु.) पढ़ा गया; दूसरा सम्भव पाठ ‘कूर्मोन्नत’ (कछुए जैसा उठा, विशेषण)। नखाः (बहुवचन) और पादौ "
            "(द्विवचन) का वचन मेल नहीं खाता, इसलिए पाठ पक्का नहीं। पहले शब्द और उसके अन्त पर कोई प्रश्न नहीं। सन्धि जाँची: नखाः + पादौ → नखाः पादौ "
            "(अघोष प से पहले विसर्ग बना रहता है)। क्रिया नहीं।"),
    "106": ("गद्य; विश्वास मध्यम; एक छपी पंक्ति (०२.०८.१२४); कोई पाठ-चिह्न नहीं। आस्य = मुख, चेहरा भी। नासावंश = नाक की डण्डी (सम्भावित; "
            "शब्दार्थ ‘नाक का बाँस’)। क्रिया नहीं। सन्धि जाँची: ऋजु + आस्यम् → ऋज्वास्यम् (उ + भिन्न स्वर → व्); नासावंशः + च → नासावंशश्च "
            "(च से पहले विसर्ग → श्)।"),
    "107": ("गद्य; विश्वास मध्यम; एक छपी पंक्ति (०२.०८.१२५); कोई पाठ-चिह्न नहीं। अनुल्बणे स्त्री. द्विवचन, हनू (स्त्री. द्विवचन) से मेल; हनु "
            "पुं./स्त्री. दोनों होता है, यहाँ स्त्री.। ‘अनुल्बण’ वेष पर भी लागू है या नहीं, यह नहीं कहा; वेष = पहनावा या रूप। अंग्रेज़ी का ‘too’ च का अनुवाद। "
            "सन्धि जाँची: अन् + उल्बण → अनुल्बण; वेषः + च → वेषश्च (च से पहले विसर्ग → श्)।"),
    "108": ("गद्य; विश्वास उच्च; एक छपी पंक्ति (०२.०८.१२६); कोई पाठ-चिह्न नहीं। श्लक्ष्णम् नपुंसक, तालु (नपुं.) से मेल; जिह्वा पर भी लागू है या "
            "नहीं, यह नहीं कहा। क्रिया नहीं। सन्धि जाँची: श्लक्ष्णम् + तालु → श्लक्ष्णं तालु (वाक्य के भीतर व्यंजन से पहले अन्तिम म् → ं)।"),
    "109": ("गद्य; विश्वास मध्यम; एक छपी पंक्ति (०२.०८.१२७); कोई पाठ-चिह्न नहीं। ‘नातिस्थूलकृशौ’ पुं. द्विवचन, ओष्ठौ से मेल; देहबन्ध पर भी "
            "यही गुण लागू है या नहीं, यह नहीं कहा। देहबन्ध = शरीर का बन्ध, बनावट। क्रिया नहीं। सन्धि जाँची: न + अति → नाति (अ + अ → आ); कृशौ + ओष्ठौ → "
            "कृशावोष्ठौ (स्वर से पहले औ → आव्); देहबन्धः + च → देहबन्धश्च (च से पहले विसर्ग → श्); छपा ‘बंध’ अनुस्वार के साथ = बन्ध।"),
    "110": ("गद्य; विश्वास मध्यम; एक छपी पंक्ति (०२.०८.१२८); कोई पाठ-चिह्न नहीं। सस्पन्दम् नपुंसक, हृदयम् से मेल; शंख और मन्या पर भी लागू है "
            "या नहीं, यह नहीं कहा। शंख = कनपटी (मानक)। मन्या = गरदन के दोनों ओर की संरचनाएँ, प्रायः वहाँ की रक्तवाहिनियाँ (सम्भावित; ‘कैरोटिड’ "
            "आधुनिक अनुमान)। ‘मन्ये’ यहाँ मन्या का स्त्री. द्विवचन है (डेटा)। सन्धि: सस्पन्दम् + हृदयम्, हृदयम् + शङ्खौ: व्यंजन से पहले अन्तिम म् → ं; "
            "छपा ‘शंखौ’ = शङ्खौ, ‘सस्पंदं’ = सस्पन्दम्।"),
    "111": ("गद्य; विश्वास मध्यम; एक छपी पंक्ति (०२.०८.१२९); कोई पाठ-चिह्न नहीं। सोष्म नपुंसक, समाहार द्वन्द्व तालुपादोदरम् (नपुं. एकवचन) से मेल; "
            "निःश्वास भी गरम है या नहीं, यह नहीं कहा। क्रिया नहीं। सन्धि जाँची: स + ऊष्म → सोष्म (अ + ऊ → ओ); पाद + उदरम् → पादोदरम् (अ + उ → ओ); "
            "निःश्वासः + च → निःश्वासश्च (च से पहले विसर्ग → श्)।"),
    "112": ("गद्य; विश्वास मध्यम; एक छपी पंक्ति (०२.०८.१३०); कोई पाठ-चिह्न नहीं। पृष्ठतः = पीछे, पीछे से; झुकाव का ठीक स्थान नहीं बताया गया। "
            "क्रिया नहीं। सन्धि जाँची: पृष्ठतः + अवनतौ → पृष्ठतोऽवनतौ (अः + अ → ओ, अगला अ लुप्त, अवग्रह ऽ)। अवनतौ = अव-√नम् का भूतकृदन्त, पुं. द्विवचन।"),
}

# ================================================================ AIDS
AIDS = {
    "100": {
        "diagram": {"groups": [
            {"label": "गुण → उसके बाद पहला अंग (छपे क्रम में)",
             "items": ["१ महा → शिर", "२ उपचित → ऊरु", "३ सूक्ष्म → अस्थि", "४ दीर्घ → अंगुलि", "५ विस्तीर्ण → आस्य",
                       "६ स्थिर → इंद्रिय", "७ गंभीर → नाभि", "८ गूढ → जत्रु (सम्भावित)", "९ रक्त → तालु", "१० कृष्ण → केश",
                       "११ नीचैर्बद्ध → कर्ण", "१२ घन → स्कंध"]}]},
        "chunks": ("इष्टं च | पुनर्महाशिरोदशनवदनहनुस्तनाग्रपृष्ठस्वरमुपचितोरुस्फिककटिवक्षोग्रीवातालुकमुभयगुणपाणिपादचुबुककर्णललाटं | "
                   "सूक्ष्मास्थिदंतनखांगुलिपर्वकेशं | दीर्घांगुलिसक्थिबाहूच्च्छासेक्षितनेत्रजिह्वं | "
                   "विस्तीर्णास्याधरोष्ठजिह्वलालटाकर्णपीठवक्षोऽल्पमेंढ्रग्रीवाकेशं | स्निग्धत्वकचकरजननयनदशनस्वनं | "
                   "स्थिरेंद्रियत्वङ्नखकेशपार्श्वं | गंभीरनाभिसंधिस्वरं | गूढजत्रुपृष्ठवंशदंतमूलं | "
                   "रक्तताल्वोष्ठनखनेत्रांतमाताम्रजिव्हाहस्तपादतलं | "
                   "कृष्णकेशभ्रूनेत्रपक्ष्मतारकंशुक्लशुकंमंडलदशनचरितमुन्नतचित्तस्कंधललाटोदरमुखनखपादं | "
                   "नीचैर्बद्धकर्णस्तननासाग्रचंक्रमणं | घनस्कंधकंधरावंतांगुलित्वक्सौहार्दं"),
        "sandhi": ("अ + ऊ → ओ: उपचित + ऊरु → उपचितोरु · अः + अ → ओऽ: वक्षः + अल्प → वक्षोऽल्प · अ + इ → ए: स्थिर + इन्द्रिय → "
                   "स्थिरेन्द्रिय · अ/आ के अलावा स्वर के बाद विसर्ग, घोष ध्वनि से पहले → र्: नीचैः + बद्ध → नीचैर्बद्ध।"),
        "anchors": ("पक्का: हर समास का पहला गुण और उसके ठीक बाद का अंग। अस्पष्ट: त्वकचकरजन, शुक्लशुकंमंडलदशनचरित, वंतांगुलि, "
                    "और अनुमानित ‘उच्छ्वास’। (मेरी याद-पद्धति)"),
        "pegs": ("सिर से कन्धे तक एक घूमती यात्रा: बड़ा सिर → पुष्ट जाँघ → पतली हड्डी → लम्बी उँगली → चौड़ा मुख → स्थिर इन्द्रिय → "
                 "गहरी नाभि → लाल तालु → काले केश → नीचे कान → घने कन्धे। (मेरा बनाया स्मरण-क्रम)"),
    },
    "101": {
        "contrast": "वृत्त (गोल): नितम्ब, गरदन, नाखून ⇄ सम (समतल): पीठ, दाँत, माथा, दृष्टि: दोनों इसी कार्ड में।",
        "chunks": "हनुनवमद्यजिह्वं | वृत्तस्फिकग्रीवानखं | समपृष्ठदंतललाटेक्षितं",
        "sandhi": "अ + ई → ए: ललाट + ईक्षितम् → ललाटेक्षितम्।",
        "anchors": "पक्का: वृत्त और सम वाले दो समास। अस्पष्ट: पहले शब्द का ‘नवमद्य’। (मेरी याद-पद्धति)",
    },
    "102": {
        "frame": "जोड़: तथा (इसी प्रकार) → कैसे: अनुपूर्ववृत्तौ (क्रम से गोल) → कौन: ऊरू (दोनों जाँघें)।",
        "chunks": "तथाऽनुपूर्ववृत्तावूरू",
        "sandhi": "आ + अ → आ: तथा + अनुपूर्व → तथानुपूर्व (अवग्रह केवल छपाई) · स्वर से पहले औ → आव्: वृत्तौ + ऊरू → वृत्तावूरू।",
    },
    "103": {
        "frame": "कौन: नाभिः → कैसी: दक्षिणावर्ता (दाहिनी ओर घूमी) → क्रिया: ‘है’ समझी जाती है।",
        "chunks": "दक्षिणावर्त्ता | नाभिः",
        "sandhi": "अ + आ → आ: दक्षिण + आवर्ता → दक्षिणावर्ता।",
    },
    "104": {
        "chunks": "प्रकृष्टंतरौ | स्तनौभ्रुवौ | च",
        "anchors": "पक्का: स्तनौ, भ्रुवौ: दो अलग द्विवचन। अनुमान: ‘प्रकृष्टंतरौ’ → प्रकृष्टान्तरौ (बड़े अन्तर वाले)। (मेरी याद-पद्धति)",
        "frame": "कौन: स्तनौ (दो स्तन) और भ्रुवौ (दो भौंहें) → जोड़: च → कैसे: अनुमानित पाठ पर बड़े अन्तर वाले।",
    },
    "105": {
        "chunks": "कूर्मान्नतयो | नखाः | पादौ | च",
        "anchors": "पक्का: नखाः (बहुवचन), पादौ (द्विवचन)। अनुमान: ‘कूर्मान्नतयो’ → कछुए जैसी उठान। (मेरी याद-पद्धति)",
        "sandhi": "अघोष प से पहले विसर्ग बना रहता है: नखाः + पादौ → नखाः पादौ।",
    },
    "106": {
        "chunks": "ऋज्वास्यं | नासावंशश्च",
        "sandhi": "उ + भिन्न स्वर → व्: ऋजु + आस्यम् → ऋज्वास्यम् · च से पहले विसर्ग → श्: नासावंशः + च → नासावंशश्च।",
        "pegs": "नाक की डण्डी को सीधे बाँस (वंश) की तरह सोचो। (मेरा बनाया चित्र)",
    },
    "107": {
        "chunks": "अनुल्बणे | हनू | वेषश्च",
        "frame": "कैसे: अनुल्बणे (उभरे नहीं) → कौन: हनू (दोनों जबड़े) → और: वेषः (पहनावा; उस पर क्या कहा, यह खुला)।",
        "sandhi": "अन् + उल्बण → अनुल्बण (स्वर से पहले निषेध अन्-) · च से पहले विसर्ग → श्: वेषः + च → वेषश्च।",
    },
    "108": {
        "chunks": "श्लक्ष्णं | तालु | जिह्वा | च",
        "frame": "कैसा: श्लक्ष्णम् (चिकना) → कौन: तालु → और: जिह्वा (उस पर भी ‘चिकना’ लागू है या नहीं, यह नहीं कहा)।",
        "sandhi": "वाक्य के भीतर व्यंजन से पहले अन्तिम म् → ं: श्लक्ष्णम् + तालु → श्लक्ष्णं तालु।",
    },
    "109": {
        "diagram": {"groups": [
            {"label": "ओष्ठौ (दोनों होंठ)", "items": ["न अति स्थूल: बहुत मोटे नहीं", "न अति कृश: बहुत दुबले नहीं"]},
            {"label": "देहबन्धः च", "items": ["शरीर की बनावट भी गिनी गई", "उस पर यही गुण? कहा नहीं"]}]},
        "chunks": "नातिस्थूलकृशावोष्ठौ | देहबंधश्च",
        "sandhi": "अ + अ → आ: न + अति → नाति · स्वर से पहले औ → आव्: कृशौ + ओष्ठौ → कृशावोष्ठौ।",
    },
    "110": {
        "diagram": {"groups": [
            {"label": "छपे क्रम में", "items": ["सस्पंदं हृदयं: धड़कता हृदय", "शंखौ: दोनों कनपटियाँ",
                                             "मन्ये: दोनों मन्या (सम्भावित: गरदन की वाहिनियाँ)"]}]},
        "chunks": "सस्पंदं | हृदयं | शंखौ | मन्ये | च",
        "frame": "कैसा: सस्पन्दम् (धड़कन सहित) → कौन: हृदयम् → और: शङ्खौ, मन्ये (उन पर धड़कन? कहा नहीं)।",
    },
    "111": {
        "diagram": {"groups": [
            {"label": "सोष्म (गरम)", "items": ["तालु", "पाद", "उदर"]},
            {"label": "च से जुड़ा", "items": ["निःश्वास (गरम? स्पष्ट नहीं)"]}]},
        "chunks": "सोष्म | तालुपादोदरं | निःश्वासश्च",
        "sandhi": "अ + ऊ → ओ: स + ऊष्म → सोष्म · अ + उ → ओ: पाद + उदरम् → पादोदरम् · च से पहले विसर्ग → श्: निःश्वासः + च → निःश्वासश्च।",
    },
    "112": {
        "diagram": {"groups": [
            {"label": "कर्णौ (दोनों कान)", "items": ["पृष्ठतः अवनतौ: पीछे की ओर झुके", "रोमशौ: रोमयुक्त"]}]},
        "chunks": "पृष्ठतोऽवनतौ | रोमशौ | च | कर्णौ",
        "sandhi": "अः + अ → ओ, अगला अ लुप्त (ऽ): पृष्ठतः + अवनतौ → पृष्ठतोऽवनतौ।",
    },
}

# ================================================================ IMAGE_SPECS
IMAGE_SPECS = {
    ("100", "diagram"): {
        "file": "sh8-ishta-anga-100.svg",
        "alt": ("Table of card 100 in printed order: twelve of its qualifiers (those followed by a sure body part), each with the first body part after it: large head, "
                "well-developed thighs, fine bones, long fingers, broad mouth, steady senses, deep navel, hidden jatru "
                "(probable), red palate, black hair, low-set ears, dense shoulders."),
        "type": "table",
        "title": "कार्ड १००: गुण और पहला अंग",
        "heads": ["गुण", "पहला अंग"],
        "rows": [["१ महा: बड़ा", "शिर"], ["२ उपचित: पुष्ट", "ऊरु"], ["३ सूक्ष्म: पतला", "अस्थि"],
                 ["४ दीर्घ: लम्बा", "अंगुलि"], ["५ विस्तीर्ण: चौड़ा", "आस्य"], ["६ स्थिर: अचल", "इंद्रिय"],
                 ["७ गंभीर: गहरा", "नाभि"], ["८ गूढ: छिपा", "जत्रु (सम्भावित)"], ["९ रक्त: लाल", "तालु"],
                 ["१० कृष्ण: काला", "केश"], ["११ नीचैर्बद्ध: नीचे बँधा", "कर्ण"], ["१२ घन: घना", "स्कंध"]],
    },
    ("101", "contrast"): {
        "file": "sh8-vritta-sama-101.svg",
        "alt": "Split of card 101: round, the buttocks, neck and nails; even, the back, teeth, forehead and gaze.",
        "type": "split",
        "title": "कार्ड १०१: वृत्त और सम",
        "cols": [["वृत्त: गोल", ["स्फिक: नितम्ब", "ग्रीवा: गरदन", "नख: नाखून"]],
                 ["सम: समतल", ["पृष्ठ: पीठ", "दंत: दाँत", "ललाट: माथा", "ईक्षित: दृष्टि"]]],
    },
    ("109", "diagram"): {
        "file": "sh8-oshtha-109.svg",
        "alt": ("Split of card 109: the two lips, not very stout and not very lean; the body's build, named too, with "
                "nothing said of its measure."),
        "type": "split",
        "title": "कार्ड १०९: होंठ और देहबन्ध",
        "cols": [["ओष्ठौ: दोनों होंठ", ["बहुत मोटे नहीं", "बहुत दुबले नहीं"]],
                 ["देहबन्धः च", ["शरीर की बनावट", "यही गुण? कहा नहीं"]]],
    },
    ("110", "diagram"): {
        "file": "sh8-saspanda-110.svg",
        "alt": ("Table of card 110 in printed order: the heart, with throbbing; the two temples; the two manyā (probably "
                "the vessels at the sides of the neck); throbbing is printed with the heart; whether it also covers the others is not stated."),
        "type": "table",
        "title": "कार्ड ११०: धड़कता हृदय",
        "heads": ["अंग", "छपा गुण"],
        "rows": [["हृदयम्: हृदय", "सस्पंद: धड़कन सहित"], ["शंखौ: कनपटियाँ", "सस्पंद भी? कहा नहीं"],
                 ["मन्ये: मन्या (सम्भावित)", "सस्पंद भी? कहा नहीं"]],
    },
    ("111", "diagram"): {
        "file": "sh8-soshma-111.svg",
        "alt": ("Split of card 111: warm, the palate, feet and belly; joined by and, the outbreath, not clearly called "
                "warm."),
        "type": "split",
        "title": "कार्ड १११: सोष्म अंग",
        "cols": [["सोष्म: गरम", ["तालु", "पाद: पैर", "उदर: पेट"]],
                 ["च से जुड़ा", ["निःश्वास", "गरम? स्पष्ट नहीं"]]],
    },
    ("112", "diagram"): {
        "file": "sh8-karna-112.svg",
        "alt": "Chain of card 112 in printed order: at the back; bent down; hairy; and; the two ears.",
        "type": "chain",
        "title": "कार्ड ११२: दोनों कान",
        "steps": ["पृष्ठतः (पीछे की ओर)", "अवनतौ (झुके हुए)", "रोमशौ च (और रोमयुक्त)", "कर्णौ (दोनों कान)"],
    },
}
