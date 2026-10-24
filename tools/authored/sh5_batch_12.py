from helpers import mcq, match, order, fill, multi, accepts


AUTHORED = {}

# ---------------------------------------------------------------- unit 141
AUTHORED["141"] = {
    "title": "श्रोत्रशृंगाटकेषु शंखाबर्त्ताः",
    "question": "By unit 141, which kind of joint is named for the ears and the śṛṅgāṭakas?",
    "rule": ("In the ears (श्रोत्र) and the śṛṅgāṭakas (शृङ्गाटक, a named site in the head): (ones) of the śaṅkhāvarta "
             "(conch-whorl) kind. From the context these are bone-joints; it is the last kind named before unit 142."),
    "limits": ("Prose, elliptical: no noun or verb is printed ('ones'); that they are bone-joints comes from the context "
               "(unit 142). Śṛṅgāṭaka is a named site (a marma) with no modern equivalent: no question on what it is. The "
               "printed बर्त्ताः is read वर्ताः: no question on that spelling."),
    "explain_hi": ("यह गद्य-पंक्ति अस्थि-सन्धियों के प्रकारों की सूची का अन्तिम नाम देती है। "
                   "श्रोत्र (कान) और शृंगाटकों में शंखावर्त, यानी शंख की भँवर जैसी, सन्धियाँ हैं। "
                   "शृंगाटक सिर में एक नामित स्थान (मर्म) है; डेटा इसका कोई आधुनिक नाम नहीं देता। "
                   "‘सन्धि’ शब्द छपा नहीं है; सन्दर्भ से (इकाई १४२: ‘इस प्रकार आठ प्रकार की अस्थि-सन्धियाँ’) यह सन्धि का एक प्रकार है। "
                   "छपा ‘शंखाबर्त्ताः’ = शंखावर्ताः (ब/व का अदल-बदल और दोहरा त्त सामान्य किया गया)।"),
    "hook": "कान में शंख की भँवर: आठवाँ प्रकार।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 141, which kind of joint lies in the ears and the śṛṅgāṭakas?",
            ("Śaṅkhāvarta (conch-whorl)", "श्रोत्रशृङ्गाटकेषु शङ्खावर्ताः: in the ears and śṛṅgāṭakas, conch-whorl ones."),
            [("Vāyasatuṇḍa (crow's beak)", "The crow-beak kind is named for the jaws (unit 139), not the ears."),
             ("Maṇḍala (a round circle)", "The circle kind is named for the throat, eyes and others (unit 140), not the ears."),
             ("Ulūkhala (stone mortar)", "The mortar kind is named for the armpits, groins and tooth-roots (unit 135).")],
            "In the ears and the śṛṅgāṭakas the joints are of the conch-whorl (śaṅkhāvarta) kind.",
            "श्रोत्रशृङ्गाटकेषु शङ्खावर्ताः."),
        match(1, "Match each part of unit 141 to its meaning.",
              [["श्रोत्र", "ear"], ["शङ्ख", "conch"], ["आवर्त", "whorl, eddy"], ["-एषु", "in (locative plural)"]],
              "In the ears and the śṛṅgāṭakas: conch-whorl (ones).",
              "श्रोत्र, शङ्ख, आवर्त, -एषु."),
        fill(2, "In unit 141 the ear is called ____ (type it in Devanagari or in English letters, e.g. dharma).",
             accepts("श्रोत्र", "śrotra"),
             "श्रोत्र = ear: श्रोत्रशृङ्गाटकेषु, in the ears and the śṛṅgāṭakas.",
             "श्रोत्र = the ear, the organ of hearing.",
             "श्रोत्र = ear."),
        mcq("discriminate", 3, "Which split of शङ्खावर्ताः (printed शंखाबर्त्ताः) in unit 141 is right?",
            ("शङ्ख + आवर्ताः", "अ + आ → आ: शङ्ख (conch) + आवर्ताः (whorls) → शङ्खावर्ताः."),
            [("शङ्खे + आवर्ताः", "ए before आ would give शङ्ख आवर्ताः or शङ्खयावर्ताः, not शङ्खावर्ताः."),
             ("शङ्खौ + आवर्ताः", "औ before आ would give शङ्खावावर्ताः (आव्), not शङ्खावर्ताः."),
             ("शङ्खः + आवर्ताः", "A compound's first member has no ending; and अः before आ would give शङ्ख आवर्ताः.")],
            "शङ्ख + आवर्ताः = शङ्खावर्ताः: अ + आ → आ.",
            "अ + आ → आ."),
        mcq("apply", 4, "श्रोत्रशृङ्गाटकेषु in unit 141 ends in -एषु. What does that ending tell a reader?",
            ("In several places: locative plural", "-एषु is the locative plural of an अ-stem: in the ears and śṛṅgāṭakas."),
            [("Of one place: genitive singular", "The genitive singular of an अ-stem ends in -अस्य, not -एषु."),
             ("With many places: instrumental", "The instrumental plural of an अ-stem ends in -ऐः, not -एषु."),
             ("O places!: a vocative plural form", "The vocative plural of an अ-stem ends in -आः, not -एषु.")],
            "-एषु = locative plural: in the ears and the śṛṅgāṭakas.",
            "अ-stem + -एषु = in (several)."),
        mcq("transfer", 5, "By the rule of शङ्ख + आवर्ताः, how is देव + आलयः (house of a god) joined in a new example?",
            ("देवालयः", "अ + आ → आ, as शङ्ख + आवर्ताः → शङ्खावर्ताः."),
            [("देवलयः", "The long आ cannot vanish; अ + आ gives आ."),
             ("देवेलयः", "ए comes from अ + इ, not from अ + आ."),
             ("देवौलयः", "औ comes from अ + ओ/औ, not from अ + आ.")],
            "देव + आलयः = देवालयः, like शङ्ख + आवर्ताः = शङ्खावर्ताः.",
            "अ + आ → आ.",
            teaches="अ + आ → आ: शङ्ख + आवर्ताः → शङ्खावर्ताः."),
    ],
}

# ---------------------------------------------------------------- unit 142
AUTHORED["142"] = {
    "title": "इत्यस्थिसंधयोऽष्टविधाः",
    "question": "By unit 142, of how many kinds are the bone-joints (asthisaṃdhi)?",
    "rule": ("Thus (इति) the bone-joints (अस्थिसन्धयः) are of eight kinds (अष्टविधाः). इति closes the list of joint kinds "
             "named in units 135-141."),
    "limits": ("Prose; the copula is understood. The line names no kind: the eight are named in units 135-141, one of them "
               "(तूनसेवनी, unit 138) only on a conjectural reading. No question rests on the list of names."),
    "explain_hi": ("यह छोटी गद्य-पंक्ति सन्धि-प्रकारों की सूची को समेटती है: ‘इति’, यानी इस प्रकार, अस्थि-सन्धियाँ आठ प्रकार की हैं। "
                   "आठ नाम इकाई १३५-१४१ में आए हैं: कोर, उलूखल, सामुद्ग, प्रतर, तूनसेवनी (अनुमानित पाठ तुन्नसेवनी), वायसतुण्ड, मण्डल और शंखावर्त। "
                   "‘अष्टविध’ बहुव्रीहि समास है: जिसके आठ प्रकार हों। "
                   "‘संधयोऽष्ट’ में संधयः का अन्तिम अः (अ + विसर्ग) अ से पहले ओ बना, और बाद का अ लुप्त होकर ऽ (अवग्रह) से दिखाया गया। "
                   "क्रिया ‘हैं’ छपी नहीं, समझी जाती है।"),
    "hook": "‘इति’ पर सूची पूरी: आठ प्रकार की सन्धियाँ।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 142, of how many kinds are the bone-joints?",
            ("Eight", "अस्थिसन्धयोऽष्टविधाः: the bone-joints are of eight kinds."),
            [("Seven", "The line says eight (अष्ट), not seven."),
             ("Five", "The line says eight (अष्ट), not five."),
             ("Three", "The line says eight (अष्ट), not three.")],
            "Thus the bone-joints are of eight kinds.",
            "अष्टविधाः = of eight kinds."),
        order(1, "Put the parts of unit 142 in the line's order.",
              ["इति", "अस्थि", "सन्धयः", "अष्ट", "विधाः"],
              "Thus the bone-joints are of eight kinds.",
              "इति → अस्थि → सन्धयः → अष्ट → विधाः."),
        match(2, "Match each part of unit 142 to its meaning.",
              [["इति", "thus"], ["अस्थि", "bone"], ["सन्धि", "joint"], ["अष्ट", "eight"], ["विध", "kind"]],
              "Thus the bone-joints are of eight kinds.",
              "इति, अस्थि, सन्धि, अष्ट, विध.", role="extend",
              teaches="अष्टविध = 'having eight kinds', a bahuvrīhi compound: अष्ट (eight) + विध (kind)."),
        mcq("discriminate", 3, "Why is संधयः printed संधयोऽ before अष्ट in unit 142?",
            ("अः before अ becomes ओ, and that अ is dropped", "सन्धयः + अष्टविधाः → सन्धयोऽष्टविधाः: ओ, and the dropped अ is marked ऽ."),
            [("ओ is the plural ending of सन्धि here", "The plural is सन्धयः; the ओ comes from sandhi with the next अ."),
             ("अः before any vowel at all becomes ओ", "Before vowels other than अ, अः becomes अ (the visarga drops)."),
             ("The ऽ sign shows a long vowel in अष्ट", "ऽ shows the dropped अ of अष्ट, not a long vowel.")],
            "सन्धयः + अष्टविधाः = सन्धयोऽष्टविधाः: अः + अ → ओ, and the following अ is dropped (ऽ).",
            "अः + अ → ओऽ."),
        multi("apply", 4, "Which statements fit unit 142?",
              [("It names the eight kinds again, one by one", "The line names no kind; they come in units 135-141."),
               ("Its इति closes the list of joint kinds before it", "Right: the data: closing इति."),
               ("It gives the number of joints in each kind", "No count per kind is given in the line."),
               ("It says the bone-joints are of eight kinds", "Right: अस्थिसन्धयोऽष्टविधाः.")],
              [1, 3],
              "इति closes the list; the bone-joints are of eight kinds.",
              "इति अस्थिसन्धयः अष्टविधाः."),
        mcq("transfer", 5, "By the rule of सन्धयः + अष्टविधाः, how is देवः + अयम् (this is a god) joined in a new example?",
            ("देवोऽयम्", "अः before अ → ओ, and the अ drops (ऽ), as सन्धयः + अष्ट... → सन्धयोऽष्ट..."),
            [("देव अयम्", "That is the rule before vowels other than अ; before अ it is ओऽ."),
             ("देवा अयम्", "The visarga drops this way after आ; देवः has a short अ."),
             ("देवरयम्", "र् comes from a visarga after vowels other than अ and आ.")],
            "देवः + अयम् = देवोऽयम्, like सन्धयः + अष्टविधाः = सन्धयोऽष्टविधाः.",
            "अः + अ → ओऽ.",
            teaches="अः before अ becomes ओ and the next अ is dropped (ऽ): सन्धयः + अष्टविधाः → सन्धयोऽष्टविधाः."),
    ],
}

# ---------------------------------------------------------------- unit 143
AUTHORED["143"] = {
    "title": "स्नायुपेशीसिराश्रितैस्तु सह सहस्रद्वयं",
    "question": "By unit 143, what total is given, and why is it not stated separately?",
    "rule": ("Together with (ones) resting on ligaments (स्नायु), muscles (पेशी) and veins (सिरा, probable): two thousand "
             "(सहस्रद्वयम्). Since nothing more is to be said about them in applying the surgical instrument, it is not "
             "stated separately."),
    "limits": ("Low confidence, open parse. What 'two thousand' counts is unstated; the data's plainest reading (the "
               "bone-joints with those on snāyu, peśī and sirā) is not said in the text: no question on it. The subject of "
               "'is not stated' is unstated. sirā = vein or blood vessel (probable)."),
    "explain_hi": ("यह गद्य-पंक्ति कठिन है; डेटा में इसका विश्वास निम्न है। "
                   "स्नायु (बन्धन-तन्तु), पेशी (मांसपेशी) और सिरा (सम्भवतः शिरा या रक्त-वाहिका) पर आश्रितों के साथ गिनती दो हजार (सहस्रद्वयम्) बताई गई है। "
                   "दो हजार किसकी संख्या है, यह पंक्ति नहीं कहती; सबसे सीधा पाठ है कि इकाई १४२ की अस्थि-सन्धियाँ इनके साथ मिलाकर, पर यह केवल पाठ-अनुमान है। "
                   "फिर कारण दिया गया: शस्त्र-प्रणिधान, यानी शस्त्र के प्रयोग, में उनके विषय में और कुछ कहने योग्य नहीं, इसलिए अलग से नहीं कहा जाता। "
                   "‘इति’ यहाँ कारण बताता है।"),
    "hook": "दो हजार गिने, पर शस्त्र के लिए कहने को कुछ नहीं।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 143, what number is given?",
            ("Two thousand", "सहस्रद्वयम्: a pair of thousands, two thousand."),
            [("Two hundred", "शत would be a hundred; the line has सहस्र, a thousand."),
             ("One thousand", "द्वयम् makes it a pair of thousands, not one."),
             ("Twelve hundred", "No twelve is printed; सहस्रद्वयम् is two thousand.")],
            "सहस्रद्वयम् = two thousand.",
            "सहस्र (thousand) + द्वय (pair)."),
        match(1, "Match each word of unit 143 to its meaning.",
              [["स्नायु", "ligament or tendon"], ["पेशी", "muscle"], ["सहस्र", "a thousand"], ["द्वय", "a pair"],
               ["शस्त्र", "surgical instrument"]],
              "With those resting on ligaments, muscles and veins: two thousand; nothing more to say for the surgical instrument.",
              "स्नायु, पेशी, सहस्र, द्वय, शस्त्र."),
        order(2, "Put these parts of unit 143 in the line's order.",
              ["स्नायुपेशीसिराश्रितैस्तु सह", "सहस्रद्वयं", "न पुनः शस्त्रप्रणिधाने", "तेषु वाच्यमस्तीति", "पृथङ्नोच्यते"],
              "With those resting on snāyu, peśī and sirā: two thousand; since nothing more is to be said about them in "
              "applying the instrument, it is not stated separately.",
              "आश्रितैः सह → सहस्रद्वयम् → न पुनः शस्त्रप्रणिधाने → वाच्यम् अस्ति इति → पृथक् न उच्यते.",
              role="extend",
              teaches="शस्त्रप्रणिधान = the application of the surgical instrument (शस्त्र)."),
        mcq("discriminate", 3, "Which split of पृथङ्नोच्यते in unit 143 is right?",
            ("पृथक् + न + उच्यते", "क् before the nasal न is printed ङ्; न + उच्यते → नोच्यते (अ + उ → ओ)."),
            [("पृथक् + नु + उच्यते", "नु + उच्यते would give नूच्यते (उ + उ → ऊ), not नोच्यते."),
             ("पृथक् + न + ओच्यते", "ओच्यते is not a form; the verb is उच्यते (is said)."),
             ("पृथक् + नः + उच्यते", "नः means 'us'; the sense 'not' needs न, and नः + उ would give न उ.")],
            "पृथक् (separately) + न (not) + उच्यते (is said): अ + उ → ओ.",
            "अ + उ → ओ; क् before a nasal may become ङ्."),
        mcq("apply", 4, "In unit 143, what does शस्त्रप्रणिधाने refer to?",
            ("The application of the surgical instrument", "शस्त्र (surgical instrument) + प्रणिधान (application), locative: in its application."),
            [("A list of the body's two thousand joints", "सहस्रद्वयम् is the number; शस्त्रप्रणिधान is the instrument's application."),
             ("The healing of a wound after the operation", "No healing is named; प्रणिधान is application, not healing."),
             ("A bandage tied over a ligament", "No bandage is named; शस्त्र is the surgical instrument.")],
            "शस्त्रप्रणिधाने = in the application of the surgical instrument.",
            "शस्त्र (instrument) + प्रणिधान (application)."),
        mcq("transfer", 5, "By the rule of वाच्यमस्ति + इति → वाच्यमस्तीति, how is अस्ति + इह (is here) joined in a new example?",
            ("अस्तीह", "इ + इ → ई, as अस्ति + इति → अस्तीति."),
            [("अस्त्यिह", "य् comes from इ before an unlike vowel; इ + इ are alike."),
             ("अस्तेह", "ए comes from अ + इ, not from इ + इ."),
             ("अस्तयिह", "अय् comes from ए before a vowel, not from इ.")],
            "अस्ति + इह = अस्तीह, like अस्ति + इति = अस्तीति.",
            "इ + इ → ई.",
            teaches="Two like vowels merge long: इ + इ → ई (अस्ति + इति → अस्तीति)."),
    ],
}

# ---------------------------------------------------------------- unit 144
AUTHORED["144"] = {
    "title": "नव स्नायुशतानि",
    "question": "By unit 144, how many snāyus (ligaments) are there?",
    "rule": ("Nine hundred ligaments (स्नायु): नव (nine) stands before the compound स्नायुशतानि (ligament-hundreds), so nine "
             "hundreds, 900. The line opens the count of the snāyus."),
    "limits": ("Prose, two words, no verb printed. snāyu = ligament or tendon (data). The line gives only the total; the "
               "places follow from unit 145 on."),
    "explain_hi": ("यह गद्य-पंक्ति स्नायुओं की गिनती आरम्भ करती है: नौ सौ स्नायु। "
                   "‘स्नायुशतानि’ = स्नायुओं के सौ-सौ के समूह; उनके पहले ‘नव’ (नौ) है, तो नौ सौ। "
                   "स्नायु यानी बन्धन-तन्तु (लिगामेंट या टेंडन)। "
                   "आगे की इकाइयाँ (१४५-१४७) बताती हैं कि ये नौ सौ कहाँ-कहाँ हैं। "
                   "क्रिया छपी नहीं, समझी जाती है।"),
    "hook": "नौ सौ स्नायु: शरीर के बन्धन।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 144, how many snāyus are counted?",
            ("Nine hundred", "नव स्नायुशतानि: nine hundreds of ligaments."),
            [("Five hundred", "The line says nine (नव), not five."),
             ("Three hundred", "The line says nine (नव), not three."),
             ("Seven hundred", "The line says nine (नव), not seven.")],
            "Nine hundred ligaments.",
            "नव ... शतानि = 900."),
        match(1, "Match each part of unit 144 to its meaning.",
              [["नव", "nine"], ["स्नायु", "ligament"], ["शत", "a hundred"], ["शतानि", "hundreds"]],
              "नव स्नायुशतानि: nine hundreds of ligaments.",
              "नव, स्नायु, शत, शतानि."),
        mcq("extend", 2, "In नव स्नायुशतानि (unit 144), what does नव count?",
            ("The hundreds: nine hundreds, so 900", "नव goes with -शतानि: nine hundreds of ligaments."),
            [("The ligaments singly: so nine in all", "नव goes with -शतानि (hundreds), not with single ligaments."),
             ("Groups of ten: so ninety in all", "शत is a hundred, not ten; ninety would be नवतिः."),
             ("Groups of a thousand: so 9000", "शत is a hundred; a thousand is सहस्र.")],
            "Nine counts the hundreds: 9 × 100 = 900.",
            "number + X-शतानि = that many hundreds of X.",
            teaches="Number + X-शतानि = that many hundreds of X: नव स्नायुशतानि = 900 ligaments."),
        mcq("discriminate", 3, "Which English rendering of unit 144 is right?",
            ("Nine hundred ligaments", "नव (nine) स्नायु (ligament) शतानि (hundreds)."),
            [("Nine thousand ligaments", "शत is a hundred; a thousand would be सहस्र."),
             ("Ninety ligaments in all", "Ninety would be नवतिः; the line has नव ... शतानि."),
             ("Nine hundred muscles", "Muscle is पेशी; स्नायु is ligament or tendon.")],
            "नव स्नायुशतानि = nine hundred ligaments.",
            "स्नायु = ligament; शत = hundred."),
        fill(4, "In unit 144 the word for ligament is ____ (type it in Devanagari or in English letters, e.g. dharma).",
             accepts("स्नायु", "snāyu", "snayu"),
             "स्नायु = ligament or tendon: नव स्नायुशतानि, nine hundred ligaments.",
             "स्नायु = ligament or tendon (बन्धन-तन्तु).",
             "स्नायु = ligament.", role="apply"),
        mcq("transfer", 5, "By the pattern of नव स्नायुशतानि, what does पञ्च अश्वशतानि mean in a new example?",
            ("Five hundred horses", "Number + X-शतानि: five hundreds of horses."),
            [("Fifty horses in all", "Fifty would be पञ्चाशत्; शतानि are hundreds."),
             ("Five horses in all", "शतानि multiplies: five hundreds, not five."),
             ("Five thousand horses", "A thousand would be सहस्र, not शत.")],
            "पञ्च अश्वशतानि = five hundred horses, like नव स्नायुशतानि = nine hundred ligaments.",
            "number + X-शतानि = that many hundreds of X.",
            teaches="Number + X-शतानि = that many hundreds of X (नव स्नायुशतानि = 900 ligaments)."),
    ],
}

# ---------------------------------------------------------------- unit 145
AUTHORED["145"] = {
    "title": "तेषां षट्शतानि शाखासु",
    "question": "By unit 145, how many of the snāyus lie in the limbs (śākhā)?",
    "rule": ("Of them (तेषाम्: the 900 snāyus of unit 144), six hundred (षट्शतानि) are in the limbs (शाखासु). The line "
             "appears to continue the statement of unit 144 (data)."),
    "limits": ("Prose; no verb printed. The counted noun is carried from unit 144 (the data takes units 145-147 as "
               "probably continuing unit 144). The 600 is for all the limbs together; the count per limb begins at unit 148."),
    "explain_hi": ("यह गद्य-पंक्ति इकाई १४४ के नौ सौ स्नायुओं को बाँटना आरम्भ करती है। "
                   "‘तेषाम्’, यानी उनमें से, छह सौ (षट्शतानि) शाखाओं में हैं। "
                   "शाखा का अर्थ यहाँ हाथ-पैर, यानी चार अंग है; छह सौ चारों का कुल है। "
                   "डेटा की जाँच: एक अंग में १५० (इकाई १४८ से गिनती), × ४ = ६००। "
                   "क्रिया छपी नहीं; गिनी गई वस्तु इकाई १४४ से आती है।"),
    "hook": "नौ सौ में से छह सौ हाथ-पैरों में।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 145, how many snāyus lie in the limbs?",
            ("Six hundred", "षट्शतानि शाखासु: six hundred in the limbs."),
            [("Four hundred", "The line says six (षट्), not four."),
             ("Eight hundred", "The line says six (षट्), not eight."),
             ("Two hundred", "The line says six (षट्), not two.")],
            "Of them, six hundred in the limbs.",
            "षट्शतानि = 600."),
        match(1, "Match each word of unit 145 to its meaning.",
              [["तेषाम्", "of them"], ["षट्", "six"], ["शतानि", "hundreds"], ["शाखासु", "in the limbs"]],
              "Of them, six hundred in the limbs.",
              "तेषाम्, षट्, शतानि, शाखासु."),
        mcq("extend", 2, "In unit 145, what does तेषाम् (of them) refer to?",
            ("The 900 snāyus of unit 144", "तेषाम् takes the share out of the total just named: nine hundred snāyus."),
            [("The eight kinds of bone-joint", "The kinds of joint (unit 142) are not counted in hundreds here."),
             ("The four limbs of the body", "The limbs are where the 600 lie (शाखासु), not what is counted."),
             ("The two thousand of unit 143", "The share is taken from the 900 snāyus just named.")],
            "Of them = of the nine hundred snāyus: six hundred are in the limbs.",
            "तेषाम् = of them (genitive plural), out of the total before.",
            teaches="तेषाम् = 'of them' (genitive plural): a share taken out of a total named just before."),
        mcq("discriminate", 3, "Which form in unit 145 means 'in the limbs'?",
            ("शाखासु", "-आसु is the locative plural of an आ-stem: in the limbs."),
            [("शाखायाः", "शाखायाः is genitive or ablative singular: of or from a limb."),
             ("शाखाभिः", "शाखाभिः is instrumental plural: with the limbs."),
             ("शाखानाम्", "शाखानाम् is genitive plural: of the limbs.")],
            "शाखासु = in the limbs (locative plural of शाखा).",
            "आ-stem + -आसु = in (several)."),
        multi("apply", 4, "Which statements fit unit 145?",
              [("Each single limb holds six hundred", "The 600 is for the limbs together; per limb it is 150 by the data's check."),
               ("Six hundred snāyus lie in the limbs", "Right: षट्शतानि शाखासु."),
               ("The line names the trunk as well", "The trunk (अन्तराधि) comes in unit 146, not here."),
               ("The 600 are part of the 900 of unit 144", "Right: तेषाम्, of them.")],
              [1, 3],
              "Six hundred of the nine hundred lie in the limbs.",
              "तेषां षट्शतानि शाखासु."),
        mcq("transfer", 5, "By the pattern of तेषां षट्शतानि शाखासु, which new phrase means: of them, ten in the hands?",
            ("तेषां दश हस्तेषु", "Genitive 'of them' + number + locative place, as तेषां षट्शतानि शाखासु."),
            [("तेषु दश हस्तानाम्", "The cases are swapped: तेषु is 'in them', हस्तानाम् is 'of the hands'."),
             ("तेषां दश हस्तैः", "हस्तैः is instrumental, 'with the hands', not 'in'."),
             ("ते दश हस्तेषु", "ते is 'they' (nominative), not 'of them'.")],
            "तेषां दश हस्तेषु = of them, ten in the hands.",
            "genitive (of them) + number + locative (in the place).",
            teaches="तेषां ... शाखासु: genitive 'of them' for the whole, locative for the place of the share."),
    ],
}

# ---------------------------------------------------------------- unit 146
AUTHORED["146"] = {
    "title": "त्रिंशच्छतद्वयमंतराधौ",
    "question": "By unit 146, how many snāyus lie in the trunk (antarādhi)?",
    "rule": ("Thirty and two hundred (त्रिंशत्, शतद्वयम्), i.e. 230, in the trunk (अन्तराधौ). त्रिंशत् + शत → त्रिंशच्छत: "
             "त् + श → च्श, optionally च्छ before a vowel or semivowel (the print has च्छ)."),
    "limits": ("Prose; no verb printed; the counted noun (snāyu) is carried from unit 144. The data's check 600 + 230 + 70 "
               "= 900 uses units 145-147."),
    "explain_hi": ("यह गद्य-पंक्ति बताती है कि धड़ (अन्तराधि) में दो सौ तीस स्नायु हैं। "
                   "‘त्रिंशत्’ (तीस) और ‘शतद्वयम्’ (दो सौ) जोड़े जाते हैं: २०० + ३० = २३०। "
                   "त्रिंशत् + शत → त्रिंशच्छत; नियम: त् + श → च्श, विकल्प से च्छ (श के बाद स्वर या य/व/र हो तो; छपा च्छ)। "
                   "‘अन्तराधौ’ इ-अन्त पुंलिंग का सप्तमी एकवचन है, धड़ में; यहाँ -औ द्विवचन नहीं है। "
                   "डेटा की जाँच: ६०० + २३० + ७० = ९००, इकाई १४४ का कुल।"),
    "hook": "धड़ में दो सौ तीस: त्रिंशच्छत।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 146, how many snāyus lie in the trunk?",
            ("Two hundred and thirty", "त्रिंशत् (30) and शतद्वयम् (200): 230 in the trunk."),
            [("Three hundred and twenty", "Two hundred (शतद्वयम्) and thirty, not three hundred and twenty."),
             ("Two hundred and three", "त्रिंशत् is thirty, not three."),
             ("Thirty-two in all", "शतद्वयम् is two hundred; it is added to thirty.")],
            "Two hundred and thirty in the trunk.",
            "त्रिंशत् + शतद्वयम् = 230."),
        match(1, "Match each word of unit 146 to its meaning.",
              [["त्रिंशत्", "thirty"], ["शत", "a hundred"], ["द्वय", "a pair, two"], ["अन्तराधि", "trunk"]],
              "Thirty and two hundred in the trunk.",
              "त्रिंशत्, शत, द्वय, अन्तराधि."),
        fill(2, "In unit 146 the trunk is called ____ (type it in Devanagari or in English letters, e.g. dharma).",
             accepts("अन्तराधि", "antarādhi", "अन्तराधौ", "antaradhi"),
             "अन्तराधि = the trunk: त्रिंशच्छतद्वयमन्तराधौ, two hundred and thirty in the trunk.",
             "अन्तराधि = the trunk, the middle part of the body (standard).",
             "अन्तराधि = trunk."),
        mcq("discriminate", 3, "Which split of त्रिंशच्छत in unit 146 is right?",
            ("त्रिंशत् + शत", "त् + श → च्श, optionally च्छ before a vowel or semivowel (the print has च्छ): त्रिंशत् (thirty) + शत (hundred) → त्रिंशच्छत."),
            [("त्रिंशच् + छत", "छत is not the word for hundred; the word is शत."),
             ("त्रिंशत् + छत", "छत is not the word for hundred; the छ comes from श."),
             ("त्रिंश + च्छत", "च्छत is not a word; the parts are त्रिंशत् and शत.")],
            "त्रिंशत् + शत = त्रिंशच्छत: त् + श → च्श, optionally च्छ before a vowel or semivowel (the print has च्छ).",
            "त् + श → च्छ (optional before a vowel or semivowel; च्श also correct)."),
        mcq("apply", 4, "अन्तराधौ in unit 146 ends in -औ. What form is it?",
            ("Locative singular: in the trunk", "The data: m. loc. sg. of the इ-stem अन्तराधि."),
            [("Nominative dual: two trunks", "The dual of an इ-stem would be अन्तराधी, not अन्तराधौ."),
             ("Genitive singular: of the trunk", "The genitive of an इ-stem would be अन्तराधेः."),
             ("Vocative singular: O trunk!", "The vocative of an इ-stem would be अन्तराधे.")],
            "अन्तराधौ = in the trunk: -औ is the locative singular of a masculine इ-stem.",
            "-औ is not always dual: इ-stem m. locative singular ends in -औ."),
        mcq("transfer", 5, "By the rule of त्रिंशत् + शत → त्रिंशच्छत, how is एतत् + शरीरम् (this body) joined in a new example?",
            ("एतच्छरीरम्", "त् + श → च्श, optionally च्छ before a vowel or semivowel (the print has च्छ), as in त्रिंशत् + शत → त्रिंशच्छत."),
            [("एतद्शरीरम्", "द् comes before a voiced sound; श is unvoiced, and त् before श goes to च्."),
             ("एतत्शरीरम्", "त् cannot stay before श; it becomes च् (च्श, optionally च्छ before a vowel)."),
             ("एतज्शरीरम्", "ज् is voiced; before the unvoiced श the त् becomes च्.")],
            "एतत् + शरीरम् = एतच्छरीरम्, like त्रिंशत् + शत = त्रिंशच्छत.",
            "त् + श → च्छ (optional before a vowel or semivowel; च्श also correct).",
            teaches="त् + श → च्श, optionally च्छ before a vowel or semivowel (the print has च्छ): त्रिंशत् + शत → त्रिंशच्छत."),
    ],
}

# ---------------------------------------------------------------- unit 147
AUTHORED["147"] = {
    "title": "ऊर्ध्वं सप्ततिः",
    "question": "By unit 147, how many snāyus lie above?",
    "rule": ("Seventy (सप्ततिः) above (ऊर्ध्वम्), probably the neck and head. With 600 in the limbs and 230 in the trunk "
             "this makes the 900 of unit 144 (the data's check)."),
    "limits": ("Prose, two words. The line does not say what 'above' covers; neck and head is the data's probable reading "
               "(as in unit 122): no question names the region as certain."),
    "explain_hi": ("यह दो शब्दों की गद्य-पंक्ति है: ऊपर सत्तर। "
                   "‘ऊर्ध्वम्’ = ऊपर; डेटा के अनुसार सम्भवतः धड़ के ऊपर का भाग, यानी गर्दन और सिर (जैसे इकाई १२२ में)। "
                   "‘सप्ततिः’ = सत्तर, स्त्रीलिंग एकवचन संख्या-शब्द। "
                   "इससे इकाई १४४ का कुल पूरा होता है: ६०० + २३० + ७० = ९००। "
                   "छपा ‘ऊर्ध्वं’ में व्यंजन से पहले अन्तिम म् अनुस्वार लिखा गया है।"),
    "hook": "ऊपर सत्तर, और नौ सौ पूरे।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 147, how many snāyus lie above (ūrdhvam)?",
            ("Seventy", "ऊर्ध्वं सप्ततिः: seventy above."),
            [("Seventeen", "Seventeen would be सप्तदश; the line has सप्ततिः."),
             ("Fifty", "The line says seventy (सप्ततिः), not fifty."),
             ("Ninety", "The line says seventy (सप्ततिः), not ninety.")],
            "Seventy above.",
            "सप्ततिः = seventy."),
        match(1, "Match each word to its meaning.",
              [["ऊर्ध्वम्", "above"], ["सप्त", "seven"], ["सप्ततिः", "seventy"]],
              "ऊर्ध्वं सप्ततिः: seventy above.",
              "ऊर्ध्वम्, सप्त, सप्ततिः."),
        fill(2, "In unit 147 the number seventy is ____ (type it in Devanagari or in English letters, e.g. dharma).",
             accepts("सप्ततिः", "saptatiḥ", "सप्तति"),
             "सप्ततिः = seventy: ऊर्ध्वं सप्ततिः, seventy above.",
             "सप्तति = seventy (a feminine number noun).",
             "सप्ततिः = seventy."),
        mcq("discriminate", 3, "Why is ऊर्ध्वम् printed ऊर्ध्वं in unit 147?",
            ("Final म् before a consonant is written ं", "ऊर्ध्वम् + सप्ततिः: final म् before the consonant स becomes anusvāra."),
            [("ं marks a dual form of the word", "The data reads ऊर्ध्वम् as an indeclinable; ं is no dual sign."),
             ("ं marks a plural form of the word", "The data reads ऊर्ध्वम् as an indeclinable; ं is no plural sign."),
             ("The print has lost a vowel after ध्व", "Nothing is lost; ं is the regular anusvāra for म्.")],
            "ऊर्ध्वम् + सप्ततिः = ऊर्ध्वं सप्ततिः: final म् before a consonant → ं.",
            "Final म् + consonant inside a sentence → ं."),
        mcq("apply", 4, "Units 145-147 give 600 in the limbs, 230 in the trunk and seventy above. What do they make, by the data's check?",
            ("900, the total of unit 144", "600 + 230 + 70 = 900, the nine hundred of unit 144."),
            [("830, short of the total", "With the seventy above the sum is 900, not 830."),
             ("1000, over the total", "600 + 230 + 70 makes 900, not 1000."),
             ("870, short of the total", "600 + 230 + 70 makes 900, not 870.")],
            "600 + 230 + 70 = 900: the shares add up to unit 144's total.",
            "Limbs + trunk + above = the total."),
        mcq("transfer", 5, "By the rule of ऊर्ध्वं सप्ततिः, how is फलम् + ददाति (gives a fruit) written in a new sentence?",
            ("फलं ददाति", "Final म् before a consonant is written ं, as ऊर्ध्वम् → ऊर्ध्वं before स."),
            [("फलो ददाति", "ओ comes from अः before a voiced consonant, not from अम्."),
             ("फला ददाति", "The म् does not simply drop; it becomes ं."),
             ("फलः ददाति", "म् does not turn into a visarga.")],
            "फलम् + ददाति = फलं ददाति, like ऊर्ध्वम् + सप्ततिः = ऊर्ध्वं सप्ततिः.",
            "Final म् + consonant → ं.",
            teaches="Final म् before a consonant inside a sentence is written as anusvāra: ऊर्ध्वं सप्ततिः."),
    ],
}

# ---------------------------------------------------------------- unit 148
AUTHORED["148"] = {
    "title": "तत्रैकैकस्मिन्सक्थि पादांगुल्यां",
    "question": "By unit 148, how many snāyus are in each toe?",
    "rule": ("There (तत्र), in each single sakthi (probably each limb), in each toe (पादाङ्गुल्याम्, प्रत्येकम्), six each "
             "(षट् षट्). A repeated number means 'so many each'."),
    "limits": ("Prose, medium confidence. The printed सक्थि is flagged (the locative would be सक्थ्नि) and 'limb' is a "
               "probable reading: no question on that word. The counted noun (snāyu) is carried from unit 144. Units "
               "148-149 belong together (data)."),
    "explain_hi": ("यह गद्य-पंक्ति एक-एक अंग में स्नायुओं की गिनती आरम्भ करती है। "
                   "वहाँ (तत्र), प्रत्येक सक्थि, यानी सम्भवतः प्रत्येक शाखा, में, पैर की प्रत्येक अंगुली में छह-छह स्नायु हैं। "
                   "‘षट् षट्’ में संख्या दोहराने का अर्थ है ‘छह-छह’, यानी हर एक में छह। "
                   "छपा ‘सक्थि’: नपुंसक सप्तमी ‘सक्थ्नि’ होती, इसलिए डेटा इसे सम्भावित पाठ-चिह्न मानता है (शायद संस्करण की आदत); यही इकाई १२३ में भी है। "
                   "इकाई १४९ इसी गिनती का योग देती है।"),
    "hook": "हर अंगुली में छह-छह।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 148, how many snāyus are in each toe?",
            ("Six", "पादाङ्गुल्यां प्रत्येकं षट् षट्: six in each toe."),
            [("Four", "The line says six (षट्), not four."),
             ("Eight", "The line says six (षट्), not eight."),
             ("Five", "The line says six (षट्), not five.")],
            "Six in each toe.",
            "षट् षट् = six each."),
        order(1, "Put the printed parts of unit 148 in the line's order.",
              ["तत्रैकैकस्मिन्", "सक्थि", "पादांगुल्यां", "प्रत्येकं", "षट्षट्"],
              "There, in each single sakthi, in each toe, six each.",
              "तत्रैकैकस्मिन् → सक्थि → पादांगुल्यां → प्रत्येकं → षट्षट्."),
        match(2, "Match each word of unit 148 to its meaning.",
              [["तत्र", "there"], ["एकैक", "each single"], ["पादाङ्गुली", "toe"], ["प्रत्येकम्", "in each, severally"],
               ["षट् षट्", "six each"]],
              "There, in each single sakthi (probably limb), in each toe, six each.",
              "तत्र, एकैक, पादाङ्गुली, प्रत्येकम्, षट् षट्.", role="extend",
              teaches="A number said twice (षट् षट्) means 'so many each': six in each toe."),
        mcq("discriminate", 3, "Which split of तत्रैकैकस्मिन् in unit 148 is right?",
            ("तत्र + एक + एकस्मिन्", "अ + ए → ऐ twice: तत्र + एक → तत्रैक; एक + एकस्मिन् → एकैकस्मिन्."),
            [("तत्र + इक + इकस्मिन्", "अ + इ gives ए, not ऐ; and इक is not the word for one."),
             ("तत्रे + एक + एकस्मिन्", "ए + ए would give तत्रयेक (अय्), not तत्रैक."),
             ("तत्रै + क + एकस्मिन्", "तत्रै and क are not the words; they are तत्र and एक.")],
            "तत्र (there) + एक + एकस्मिन् (in each single): अ + ए → ऐ.",
            "अ + ए → ऐ."),
        mcq("apply", 4, "What does षट् षट् (six six) mean in unit 148?",
            ("Six in each of the toes", "Said twice with प्रत्येकम्: six in each toe."),
            [("Twelve in each toe, six and six", "The repeat means 'six each', not six plus six."),
             ("Six in all the toes together", "प्रत्येकम् means in each, so six per toe."),
             ("Thirty-six, six times six", "The repeat means 'six each', not six times six.")],
            "षट् षट् = six each: six in each toe.",
            "number said twice = so many each."),
        mcq("transfer", 5, "By the pattern of षट् षट्, what does पञ्च पञ्च फलानि mean in a new example?",
            ("Five fruits each", "A number said twice means 'so many each', as षट् षट् = six each."),
            [("Ten fruits in all", "The repeat does not add; it means 'five each'."),
             ("Twenty-five fruits", "The repeat does not multiply; it means 'five each'."),
             ("Five ripe fruits", "The second पञ्च is the repeat, not 'ripe' (पक्व).")],
            "पञ्च पञ्च फलानि = five fruits each, like षट् षट् = six each.",
            "number said twice = so many each.",
            teaches="A repeated number means 'so many each': षट् षट् = six each."),
    ],
}

# ---------------------------------------------------------------- unit 149
AUTHORED["149"] = {
    "title": "तानि त्रिंशत्",
    "question": "By unit 149, what does 'those are thirty' total?",
    "rule": ("Those (तानि) are thirty (त्रिंशत्). The data's check: six snāyus in each of the five toes of unit 148, "
             "6 × 5 = 30."),
    "limits": ("Prose; the copula is understood. The line does not itself name what 'those' are; 6 × 5 is the data's check "
               "against unit 148. No question on सक्थि."),
    "explain_hi": ("यह दो शब्दों की गद्य-पंक्ति इकाई १४८ की गिनती का योग देती है: ‘तानि त्रिंशत्’, वे तीस हैं। "
                   "डेटा की जाँच: पाँच अंगुलियों में छह-छह, यानी ६ × ५ = ३०। "
                   "‘तानि’ नपुंसकलिंग प्रथमा बहुवचन है (वे)। "
                   "‘त्रिंशत्’ (तीस) स्त्रीलिंग एकवचन संख्या-शब्द है। "
                   "क्रिया ‘हैं’ छपी नहीं, समझी जाती है।"),
    "hook": "छह-छह पाँच बार: तीस।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 149, how many are 'those'?",
            ("Thirty", "तानि त्रिंशत्: those are thirty."),
            [("Twenty", "Twenty would be विंशतिः; the line has त्रिंशत्."),
             ("Forty", "Forty would be चत्वारिंशत्; the line has त्रिंशत्."),
             ("Sixty", "Sixty would be षष्टिः; the line has त्रिंशत्.")],
            "Those are thirty.",
            "त्रिंशत् = thirty."),
        mcq("warmup", 1, "Which word of unit 149 means 'those' (as the subject)?",
            ("तानि", "तानि = those, neuter nominative plural."),
            [("तत्र", "तत्र means 'there' (unit 148), not 'those'."),
             ("तेषाम्", "तेषाम् means 'of them', a genitive, not the subject."),
             ("त्रिंशत्", "त्रिंशत् means 'thirty', the number.")],
            "तानि = those; त्रिंशत् = thirty.",
            "तानि = those (n. nom. pl.)."),
        fill(2, "In unit 149 the number thirty is ____ (type it in Devanagari or in English letters, e.g. dharma).",
             accepts("त्रिंशत्", "triṃśat"),
             "त्रिंशत् = thirty: तानि त्रिंशत्, those are thirty.",
             "त्रिंशत् = thirty (a feminine number noun).",
             "त्रिंशत् = thirty."),
        mcq("discriminate", 3, "Which reading of unit 149 does the data's check give?",
            ("Six in each of the five toes make thirty", "Unit 148: six each in each toe; 6 × 5 = 30."),
            [("Three in each of ten toes make thirty", "Unit 148 gives six in each toe of one limb, not three."),
             ("Thirty lie in each single toe of a limb", "Each toe has six (unit 148); thirty is the total."),
             ("Thirty lie in all four limbs together", "The thirty totals one limb's toes, not all four limbs.")],
            "Six in each of five toes = thirty.",
            "तानि त्रिंशत् = 6 × 5 (data's check)."),
        multi("apply", 4, "Which statements about unit 149 are right?",
              [("तानि is neuter nominative plural", "Right: the data: n. nom. pl."),
               ("It names a new place of the body", "No place is named; it totals the toes of unit 148."),
               ("It is a metrical verse (śloka)", "The data types it as prose."),
               ("The verb 'are' is not printed", "Right: the copula is understood.")],
              [0, 3],
              "तानि is n. nom. pl.; the verb is understood.",
              "तानि त्रिंशत् (copula understood)."),
        mcq("transfer", 5, "By the pattern of तानि त्रिंशत्, which new phrase says: those fruits (फलानि) are twenty?",
            ("तानि विंशतिः", "Neuter plural तानि for फलानि + the number, as तानि त्रिंशत्."),
            [("ते विंशतिः", "ते is the masculine plural; neuter फलानि needs तानि."),
             ("तत् विंशतिः", "तत् is singular; many fruits need the plural तानि."),
             ("तेषां विंशतिः", "तेषाम् is 'of them', not the subject 'those'.")],
            "तानि विंशतिः = those are twenty, like तानि त्रिंशत् = those are thirty.",
            "तानि (n. nom. pl.) + number word.",
            teaches="तानि = 'those' for neuter plural things, the subject of a number sentence: तानि त्रिंशत्."),
    ],
}

# ---------------------------------------------------------------- unit 150
AUTHORED["150"] = {
    "title": "दश दश पादतलकूर्च्चगुल्फेषु",
    "question": "By unit 150, how many snāyus are in the sole, the kūrca and the ankle?",
    "rule": ("Ten each (दश दश) in the sole (पादतल), the kūrca (a named part of the foot) and the ankle (गुल्फ): one "
             "compound in the locative plural names the three places."),
    "limits": ("Prose, medium confidence. kūrca is a named part of the foot left untranslated: no question on what it is. "
               "The printed कूर्च्च (doubled च) is read कूर्च. The counted noun (snāyu) is carried from unit 144."),
    "explain_hi": ("यह गद्य-पंक्ति एक अंग की गिनती आगे बढ़ाती है: तलवे (पादतल), कूर्च और टखने (गुल्फ) में दस-दस स्नायु। "
                   "‘दश दश’ = दस-दस, यानी तीनों स्थानों में से हर एक में दस। "
                   "कूर्च पैर का एक नामित भाग है; डेटा इसका अनुवाद नहीं करता। "
                   "‘पादतलकूर्चगुल्फेषु’ द्वन्द्व समास है, सप्तमी बहुवचन (-एषु)। "
                   "छपा ‘कूर्च्च’ (दोहरा च) सामान्य किया गया।"),
    "hook": "तलवा, कूर्च, टखना: दस-दस।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 150, how many snāyus are in each of the sole, the kūrca and the ankle?",
            ("Ten", "दश दश: ten each."),
            [("Six", "The line says ten (दश), not six."),
             ("Five", "The line says ten (दश), not five."),
             ("Twenty", "दश दश means ten each, not twenty.")],
            "Ten each in the sole, the kūrca and the ankle.",
            "दश दश = ten each."),
        order(1, "Put the printed parts of unit 150 in the line's order.",
              ["दश दश", "पादतल", "कूर्च्च", "गुल्फेषु"],
              "Ten each in the sole, the kūrca and the ankle.",
              "दश दश → पादतल → कूर्च्च → गुल्फेषु."),
        match(2, "Match each word of unit 150 to its meaning.",
              [["दश", "ten"], ["दश दश", "ten each"], ["पादतल", "sole of the foot"], ["गुल्फ", "ankle"]],
              "Ten each in the sole, the kūrca and the ankle.",
              "दश, दश दश, पादतल, गुल्फ.", role="extend",
              teaches="पादतल = foot (पाद) + surface (तल): the sole of the foot."),
        mcq("discriminate", 3, "Which English rendering of unit 150 is right?",
            ("Ten each in the sole, the kūrca and the ankle", "दश दश पादतल-कूर्च-गुल्फेषु."),
            [("Ten each in the sole, the kūrca and the knee", "गुल्फ is the ankle; the knee is जानु."),
             ("Ten in all in the sole, the kūrca and the ankle", "दश दश means ten each, not ten in all."),
             ("Ten each in the palm, the kūrca and the ankle", "पादतल is the sole of the foot (पाद), not the palm.")],
            "Ten each in the sole, the kūrca and the ankle.",
            "दश दश = ten each; गुल्फ = ankle; पादतल = sole."),
        mcq("apply", 4, "By unit 150, how many snāyus do the three places hold together?",
            ("Thirty", "Ten in each of three places: 10 × 3 = 30."),
            [("Ten", "Ten is for each place; there are three places."),
             ("Twenty", "Ten in each of three places makes thirty, not twenty."),
             ("Sixty", "Ten in each of three places makes thirty, not sixty.")],
            "Ten each in three places = thirty.",
            "दश दश × 3 places = 30."),
        mcq("transfer", 5, "By the pattern of गुल्फेषु (in the ankles), how is वृक्ष (tree) put to mean in the trees, in a new example?",
            ("वृक्षेषु", "अ-stem + -एषु = locative plural, as गुल्फ → गुल्फेषु."),
            [("वृक्षासु", "-आसु is the locative plural of आ-stems (शाखासु), not of अ-stems."),
             ("वृक्षैः", "वृक्षैः is instrumental plural: with the trees."),
             ("वृक्षाणाम्", "वृक्षाणाम् is genitive plural: of the trees.")],
            "वृक्षेषु = in the trees, like गुल्फेषु = in the ankles.",
            "अ-stem + -एषु = in (several).",
            teaches="अ-stem nouns take -एषु for 'in' (plural): गुल्फ → गुल्फेषु."),
    ],
}

# ---------------------------------------------------------------- unit 151
AUTHORED["151"] = {
    "title": "त्रिंशज्जंघायां",
    "question": "By unit 151, how many snāyus are in the shank (jaṅghā)?",
    "rule": ("Thirty (त्रिंशत्) in the shank (जङ्घायाम्, the lower leg). त्रिंशत् + जङ्घायाम् → त्रिंशज्जङ्घायाम्: त् "
             "before ज becomes ज्."),
    "limits": ("Prose, one printed word-group; no verb. The counted noun (snāyu) is carried from unit 144."),
    "explain_hi": ("यह गद्य-पंक्ति एक अंग की गिनती आगे बढ़ाती है: जङ्घा में तीस स्नायु। "
                   "जङ्घा = घुटने से टखने तक की टाँग, यानी पिंडली वाला भाग (मानक)। "
                   "त्रिंशत् + जङ्घायाम् में त् + ज → ज्ज हुआ: त्रिंशज्जङ्घायाम्। "
                   "‘जङ्घायाम्’ आ-अन्त स्त्रीलिंग का सप्तमी एकवचन है; छपा ‘जंघायां’ अनुस्वार वाली वर्तनी है। "
                   "क्रिया छपी नहीं।"),
    "hook": "पिंडली में तीस: त्रिंशज्जङ्घा।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 151, how many snāyus are in the shank?",
            ("Thirty", "त्रिंशत् जङ्घायाम्: thirty in the shank."),
            [("Twenty", "The line says thirty (त्रिंशत्), not twenty."),
             ("Ten", "The line says thirty (त्रिंशत्), not ten."),
             ("Fifty", "The line says thirty (त्रिंशत्), not fifty.")],
            "Thirty in the shank.",
            "त्रिंशत् = thirty."),
        match(1, "Match each word to its meaning.",
              [["त्रिंशत्", "thirty"], ["जङ्घा", "shank, lower leg"], ["जङ्घायाम्", "in the shank"]],
              "त्रिंशत् जङ्घायाम्: thirty in the shank.",
              "त्रिंशत्, जङ्घा, जङ्घायाम्."),
        mcq("extend", 2, "What part of the leg is the jaṅghā of unit 151?",
            ("The lower leg, knee to ankle", "जङ्घा = the shank, the lower leg (standard)."),
            [("The thigh, hip to knee", "The thigh is ऊरु, not जङ्घा."),
             ("The sole of the foot", "The sole is पादतल (unit 150), not जङ्घा."),
             ("The groin, at the top", "The groin is वङ्क्षण, not जङ्घा.")],
            "जङ्घा = the shank: the lower leg between knee and ankle.",
            "जङ्घा = shank.",
            teaches="जङ्घा = the shank, the lower leg from knee to ankle (standard)."),
        mcq("discriminate", 3, "Which split of त्रिंशज्जंघायां in unit 151 is right?",
            ("त्रिंशत् + जङ्घायाम्", "त् before ज becomes ज्: त्रिंशत् + जङ्घायाम् → त्रिंशज्जङ्घायाम्."),
            [("त्रिंशत् + यङ्घायाम्", "यङ्घा is not a word, and त् + य gives त्य, not ज्ज."),
             ("त्रिंशम् + जङ्घायाम्", "म् before ज gives ं or ञ्, not ज्ज."),
             ("त्रिंशः + जङ्घायाम्", "अः before the voiced ज would give ओ, not ज्ज.")],
            "त्रिंशत् (thirty) + जङ्घायाम् (in the shank): त् + ज → ज्ज.",
            "त् + ज → ज्ज."),
        fill(4, "In unit 151 the shank is called ____ (type it in Devanagari or in English letters, e.g. dharma).",
             accepts("जङ्घा", "jaṅghā", "जङ्घायाम्", "jangha"),
             "जङ्घा = shank: त्रिंशज्जङ्घायाम्, thirty in the shank.",
             "जङ्घा = the shank, the lower leg.",
             "जङ्घा = shank.", role="apply"),
        mcq("transfer", 5, "By the rule of त्रिंशत् + जङ्घायाम्, how is तत् + जलम् (that water) joined in a new example?",
            ("तज्जलम्", "त् before ज becomes ज्, as त्रिंशत् + जङ्घायाम् → त्रिंशज्जङ्घायाम्."),
            [("तद्जलम्", "Before the palatal ज the त् becomes the palatal ज्, not द्."),
             ("तच्जलम्", "च् is unvoiced; before the voiced ज it becomes ज्."),
             ("तत्जलम्", "त् cannot stay before ज; it becomes ज्.")],
            "तत् + जलम् = तज्जलम्, like त्रिंशत् + जङ्घायाम् = त्रिंशज्जङ्घायाम्.",
            "त् + ज → ज्ज.",
            teaches="त् before ज becomes ज्: त्रिंशत् + जङ्घायाम् → त्रिंशज्जङ्घायाम्."),
    ],
}

# ---------------------------------------------------------------- unit 152
AUTHORED["152"] = {
    "title": "दश जानुनि",
    "question": "By unit 152, how many snāyus are in the knee (jānu)?",
    "rule": ("Ten (दश) in the knee (जानुनि). जानुनि is the locative singular of the neuter उ-stem जानु (data): 'in the "
             "knee'."),
    "limits": ("Prose, two words; no verb. The counted noun (snāyu) is carried from unit 144. The data adds no note."),
    "explain_hi": ("यह दो शब्दों की गद्य-पंक्ति है: जानु, यानी घुटने, में दस स्नायु। "
                   "‘जानुनि’ उ-अन्त नपुंसकलिंग ‘जानु’ का सप्तमी एकवचन है (डेटा)। "
                   "यहाँ ‘दश’ एक ही बार है, इसलिए ‘दस-दस’ नहीं, बस दस। "
                   "गिनी गई वस्तु इकाई १४४ से आती है; क्रिया छपी नहीं। "
                   "एक अंग की गिनती इकाई १४८ से इस क्रम में चल रही है: अंगुलियाँ, तलवा-कूर्च-टखना, जङ्घा, जानु।"),
    "hook": "घुटने में दस।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 152, how many snāyus are in the knee?",
            ("Ten", "दश जानुनि: ten in the knee."),
            [("Six", "The line says ten (दश), not six."),
             ("Twenty", "The line says ten (दश), not twenty."),
             ("Forty", "The line says ten (दश), not forty.")],
            "Ten in the knee.",
            "दश = ten."),
        match(1, "Match each word to its meaning.",
              [["दश", "ten"], ["जानु", "knee"], ["जानुनि", "in the knee"]],
              "दश जानुनि: ten in the knee.",
              "दश, जानु, जानुनि."),
        mcq("extend", 2, "जानुनि in unit 152 ends in -उनि. What form is it?",
            ("Locative singular: in the knee", "The data: n. loc. sg. of the उ-stem जानु."),
            [("Nominative plural: the knees", "The neuter plural has a long ऊ: जानूनि."),
             ("Instrumental: with the knee", "The instrumental singular is जानुना."),
             ("Nominative dual: two knees", "The neuter dual is जानुनी, with a long ई.")],
            "जानुनि = in the knee (locative singular).",
            "neuter उ-stem + -उनि = in (one).",
            teaches="Neuter उ-stems take -उनि for 'in' (singular): जानु → जानुनि."),
        mcq("discriminate", 3, "Which English rendering of unit 152 is right?",
            ("Ten in the knee", "दश (ten) जानुनि (in the knee)."),
            [("Ten in the ankle", "The ankle is गुल्फ; जानु is the knee."),
             ("Ten in the thigh", "The thigh is ऊरु; जानु is the knee."),
             ("Ten in the elbow", "The elbow is कूर्पर; जानु is the knee.")],
            "दश जानुनि = ten in the knee.",
            "जानु = knee."),
        multi("apply", 4, "Which statements about unit 152 are right?",
              [("दश is the number word 'ten'", "Right: दश = ten."),
               ("A verb is printed in the line", "No verb is printed."),
               ("जानुनि is a locative: in the knee", "Right: the data: n. loc. sg."),
               ("दश is said twice, meaning 'ten each'", "दश stands once here: just ten.")],
              [0, 2],
              "दश = ten; जानुनि = in the knee.",
              "दश जानुनि."),
        mcq("transfer", 5, "By the pattern of जानु → जानुनि, how does मधु (n., honey) mean in the honey, in a new example?",
            ("मधुनि", "Neuter उ-stem + -उनि = in, as जानु → जानुनि."),
            [("मधुना", "मधुना is instrumental: with honey."),
             ("मधूनि", "मधूनि (long ऊ) is the nominative or accusative plural."),
             ("मधुनी", "मधुनी (long ई) is the dual form.")],
            "मधुनि = in the honey, like जानुनि = in the knee.",
            "neuter उ-stem + -उनि = in (one).",
            teaches="Neuter उ-stems take -उनि for the locative singular: जानु → जानुनि."),
    ],
}


# ===================================================================== NOTES_HI
NOTES_HI = {
    "141": ("गद्य; विश्वास उच्च; कोई पाठ-चिह्न नहीं। छपा ‘शंखाबर्त्ताः’ = शङ्खावर्ताः (ब/व का अदल-बदल और दोहरा त्त, सामान्य किया गया)। "
            "शृंगाटक सिर का एक नामित स्थान (मर्म) है, कोई आधुनिक नाम नहीं थोपा गया। संज्ञा ‘(वे)’ छपी नहीं; सन्दर्भ से सन्धि का प्रकार। "
            "सन्धि जाँची: शङ्ख + आवर्ताः → शङ्खावर्ताः (अ + आ → आ); छपा शृंगाटक/शंख = शृङ्गाटक/शङ्ख (अनुस्वार वर्तनी)।"),
    "142": ("गद्य; विश्वास उच्च; कोई पाठ-चिह्न नहीं। अन्त वाला ‘इति’ पिछली सूची (इकाई १३५-१४१) को समेटता है; अनुवाद में नहीं लिया गया। "
            "क्रिया समझी जाती है। आठ नामों में तूनसेवनी (इकाई १३८) अनुमानित पाठ (तुन्नसेवनी) पर है। सन्धि जाँची: इति + अस्थि → इत्यस्थि "
            "(इ + अ → य); सन्धयः + अष्टविधाः → सन्धयोऽष्टविधाः (अः + अ → ओ, बाद का अ लुप्त, ऽ)।"),
    "143": ("गद्य; विश्वास निम्न; पद-विभाग खुला (OPEN parse)। ‘दो हजार’ किसकी गिनती है, पंक्ति नहीं कहती; सबसे सीधा पाठ: इकाई १४२ की "
            "अस्थि-सन्धियाँ स्नायु, पेशी, सिरा पर आश्रितों के साथ, पर यह कहा नहीं गया। इस पर कोई प्रश्न नहीं। ‘उच्यते’ का कर्ता छपा नहीं। "
            "‘इति’ को कारण-सूचक पढ़ा गया। स्नायु, पेशी: मानक; सिरा = शिरा या रक्त-वाहिका (सम्भावित)। सन्धि जाँची: सिरा + आश्रितैः → सिराश्रितैः "
            "(आ + आ → आ); आश्रितैः + तु → आश्रितैस्तु (त से पहले विसर्ग → स्); अस्ति + इति → अस्तीति (इ + इ → ई); पृथक् + न → पृथङ् न "
            "(नासिक्य से पहले क् → ङ्, जैसा छपा); न + उच्यते → नोच्यते (अ + उ → ओ)।"),
    "144": ("गद्य; विश्वास उच्च; कोई पाठ-चिह्न नहीं। नव शतानि = नौ सौ = ९००। स्नायु = लिगामेंट या टेंडन (बन्धन-तन्तु)। क्रिया छपी नहीं।"),
    "145": ("गद्य; विश्वास उच्च; कोई पाठ-चिह्न नहीं। समूह-टिप्पणी: इकाई १४५-१४७ इकाई १४४ का ही कथन आगे बढ़ाती लगती हैं। "
            "डेटा की जाँच: एक अंग में ३० (अंगुलियाँ) + ३० (तल, कूर्च, गुल्फ) + ३० (जङ्घा) + १० (जानु) + ४० (ऊरु) + १० (वंक्षण) = १५०, × ४ = ६००। "
            "छपा ‘तेषां’ = तेषाम् (व्यंजन से पहले म् → ं); षट् + शतानि → षट्शतानि (कोई परिवर्तन नहीं)।"),
    "146": ("गद्य; विश्वास उच्च; कोई पाठ-चिह्न नहीं। त्रिंशत् + शतद्वयम् = तीस और दो सौ = २३०। जाँच: ६०० + २३० + ७० = ९००, इकाई १४४ से मेल। "
            "सन्धि जाँची: त्रिंशत् + शत → त्रिंशच्छत, नियम: त् + श → च्श, विकल्प से च्छ (श के बाद स्वर या य/व/र हो तो; छपा च्छ); शतद्वयम् + अन्तराधौ → शतद्वयमन्तराधौ (स्वर से पहले म् बना रहा); "
            "छपा ‘मंतराधौ’ = मन्तराधौ (अनुस्वार वर्तनी)। अन्तराधौ = इ-अन्त पुंलिंग सप्तमी एकवचन।"),
    "147": ("गद्य; विश्वास उच्च; कोई पाठ-चिह्न नहीं। ऊर्ध्वम् = ऊपर; सम्भवतः गर्दन और सिर (जैसे इकाई १२२ में), निश्चित नहीं। "
            "सन्धि जाँची: ऊर्ध्वम् + सप्ततिः → ऊर्ध्वं सप्ततिः (व्यंजन से पहले अन्तिम म् → ं)।"),
    "148": ("गद्य; विश्वास मध्यम। पाठ-चिह्न (सम्भावित): छपा ‘सक्थि’; नपुंसक सप्तमी ‘सक्थ्नि’ होगी; यही छपा रूप इकाई १२३ में भी है। "
            "इस शब्द पर कोई प्रश्न नहीं। ‘सक्थि’ = सम्भवतः शाखा (अंग)। समूह-टिप्पणी: इकाई १४८-१४९ साथ हैं। गिनी गई वस्तु (स्नायु) इकाई १४४ से। "
            "सन्धि जाँची: तत्र + एक + एकस्मिन् → तत्रैकैकस्मिन् (अ + ए → ऐ, दो बार); छपा ‘पादांगुल्यां’, ‘प्रत्येकं’ = पादाङ्गुल्याम्, प्रत्येकम् "
            "(अनुस्वार वर्तनी)। ‘एकैकस्मिन्सक्थि’ छपाई में जुड़ा है।"),
    "149": ("गद्य; विश्वास उच्च; कोई पाठ-चिह्न नहीं। क्रिया समझी जाती है। डेटा की जाँच: पाँच अंगुलियों में छह-छह = ३०। "
            "तानि = नपुंसक प्रथमा बहुवचन; त्रिंशत् = स्त्रीलिंग एकवचन संख्या-शब्द।"),
    "150": ("गद्य; विश्वास मध्यम; कोई पाठ-चिह्न नहीं। कूर्च पैर का एक नामित भाग है, अनुवाद नहीं किया गया। पादतल = तलवा। "
            "छपा ‘कूर्च्च’ (दोहरा च) = कूर्च (वर्तनी, सामान्य किया गया)। दश दश = दस-दस। समास: पादतल-कूर्च-गुल्फेषु (द्वन्द्व, सप्तमी बहुवचन)।"),
    "151": ("गद्य; विश्वास उच्च; कोई पाठ-चिह्न नहीं। जङ्घा = घुटने से टखने तक की टाँग (मानक)। सन्धि जाँची: त्रिंशत् + जङ्घायाम् → "
            "त्रिंशज्जङ्घायाम् (त् + ज → ज्ज); छपा ‘जंघायां’ = जङ्घायाम् (अनुस्वार वर्तनी)।"),
    "152": ("गद्य; विश्वास उच्च; कोई पाठ-चिह्न नहीं; डेटा में कोई टिप्पणी नहीं। जानुनि = जानु (नपुंसक, उ-अन्त) का सप्तमी एकवचन। "
            "गिनी गई वस्तु (स्नायु) इकाई १४४ से; क्रिया छपी नहीं।"),
}


# ===================================================================== AIDS
AIDS = {
    "141": {
        "chunks": "श्रोत्रशृंगाटकेषु | शंखाबर्त्ताः",
        "sandhi": "अ + आ → आ: शङ्ख + आवर्ताः → शङ्खावर्ताः।",
        "frame": "कहाँ: श्रोत्र (कान) और शृंगाटक (सिर का नामित स्थान) → कौन-सा प्रकार: शंखावर्त (शंख की भँवर) → संज्ञा: छपी नहीं, सन्दर्भ से सन्धि।",
        "pegs": "शंख को कान से लगाओ तो भँवर-सी गूँज सुनाई देती है: कान में शंखावर्त। (मेरा बनाया चित्र, केवल याद की सहायता)",
    },
    "142": {
        "diagram": {"groups": [
            {"label": "आठ सन्धि-प्रकार, इकाई १३५-१४१ के क्रम से",
             "items": ["कोर (कली)", "उलूखल (ओखली)", "सामुद्ग (डिब्बा)", "प्रतर", "तूनसेवनी (अनुमानित: तुन्नसेवनी)",
                       "वायसतुण्ड (कौए की चोंच)", "मण्डल (गोला)", "शंखावर्त (शंख की भँवर)"]}]},
        "chunks": "इत्य् | अस्थिसंधयो | ऽष्टविधाः",
        "sandhi": "इ + अ → य: इति + अस्थि → इत्यस्थि · अः + अ → ओऽ: सन्धयः + अष्टविधाः → सन्धयोऽष्टविधाः।",
        "frame": "इति (इस प्रकार, सूची समाप्त) → अस्थिसन्धयः (हड्डियों के जोड़) → अष्टविधाः (आठ प्रकार के)।",
    },
    "143": {
        "chain": {"steps": ["स्नायु, पेशी, सिरा (सम्भावित) पर आश्रितों के साथ", "दो हजार (क्या गिना, अनकहा)",
                            "शस्त्र-प्रयोग में उनके विषय में और कहने योग्य नहीं", "इसलिए अलग से नहीं कहा जाता"]},
        "chunks": "स्नायुपेशीसिराश्रितैस्तु सह | सहस्रद्वयं | न पुनः शस्त्रप्रणिधाने | तेषु वाच्यमस्तीति | पृथङ्नोच्यते",
        "sandhi": "त से पहले विसर्ग → स्: आश्रितैः + तु → आश्रितैस्तु · इ + इ → ई: अस्ति + इति → अस्तीति · अ + उ → ओ: न + उच्यते → नोच्यते।",
    },
    "144": {
        "chunks": "नव | स्नायुशतानि",
        "frame": "संख्या: नव (नौ) → इकाई: शतानि (सौ-सौ) → वस्तु: स्नायु (बन्धन-तन्तु) → कुल: ९००।",
        "letters": "‘नव स्नायु’: न से नौ, स से सौ, नौ सौ। (मेरी याद-पद्धति)",
    },
    "145": {
        "chunks": "तेषां | षट्शतानि | शाखासु",
        "frame": "किनमें से: तेषाम् (इकाई १४४ के ९०० में से) → कितने: षट्शतानि (६००) → कहाँ: शाखासु (हाथ-पैरों में)।",
        "anchors": "चार अंग, हर अंग में डेढ़ सौ: चार × डेढ़ सौ = छह सौ (डेटा की जाँच)।",
    },
    "146": {
        "diagram": {"groups": [
            {"label": "इकाई १४४ के ९०० स्नायुओं का बँटवारा (डेटा की जाँच)",
             "items": ["शाखाएँ: ६०० (इकाई १४५)", "अन्तराधि (धड़): २३० (इकाई १४६)", "ऊर्ध्व (ऊपर): ७० (इकाई १४७)"]}]},
        "chunks": "त्रिंशच्छतद्वयम् | अंतराधौ",
        "sandhi": "त् + श → च्श, विकल्प से च्छ (श के बाद स्वर या य/व/र हो तो; छपा च्छ): त्रिंशत् + शत → त्रिंशच्छत।",
        "frame": "संख्या: त्रिंशत् (३०) + शतद्वयम् (२००) = २३० → कहाँ: अन्तराधौ (धड़ में; -औ यहाँ सप्तमी, द्विवचन नहीं)।",
    },
    "147": {
        "chunks": "ऊर्ध्वं | सप्ततिः",
        "sandhi": "व्यंजन से पहले अन्तिम म् → ं: ऊर्ध्वम् + सप्ततिः → ऊर्ध्वं सप्ततिः।",
        "frame": "कहाँ: ऊर्ध्वम् (ऊपर; सम्भवतः गर्दन-सिर) → कितने: सप्ततिः (७०) → योग: ६०० + २३० + ७० = ९००।",
    },
    "148": {
        "chain": {"steps": ["तत्र: वहाँ", "एकैकस्मिन् सक्थि: प्रत्येक सक्थि (सम्भवतः शाखा) में", "पादाङ्गुल्याम् प्रत्येकम्: हर अंगुली में",
                            "षट् षट्: छह-छह"]},
        "chunks": "तत्रैकैकस्मिन्सक्थि | पादांगुल्यां | प्रत्येकं | षट्षट्",
        "sandhi": "अ + ए → ऐ: तत्र + एक → तत्रैक; एक + एकस्मिन् → एकैकस्मिन्।",
        "pegs": "हर अंगुली पर छह का पासा रखा है: पाँच अंगुलियाँ, पाँच ‘छक्के’। (मेरा बनाया चित्र, केवल याद की सहायता)",
    },
    "149": {
        "chunks": "तानि | त्रिंशत्",
        "frame": "कौन: तानि (वे, इकाई १४८ की गिनती) → कितने: त्रिंशत् (३०) → जाँच: ६ × ५ अंगुलियाँ = ३० (डेटा)।",
        "anchors": "इकाई १४८ के ‘छह-छह’ को पाँच अंगुलियों से गुणा करो: तीस।",
    },
    "150": {
        "diagram": {"groups": [
            {"label": "दश दश: हर स्थान में दस (छपे क्रम से)", "items": ["पादतल (तलवा): १०", "कूर्च: १०", "गुल्फ (टखना): १०"]}]},
        "chunks": "दश दश | पादतलकूर्च्चगुल्फेषु",
        "frame": "संख्या: दश दश (दस-दस) → कहाँ: पादतल, कूर्च, गुल्फ (एक द्वन्द्व समास, सप्तमी बहुवचन)।",
        "letters": "स्थानों के पहले अक्षर क्रम से: पा-कू-गु (पादतल, कूर्च, गुल्फ)। (मेरी याद-पद्धति)",
    },
    "151": {
        "chunks": "त्रिंशज् | जंघायां",
        "sandhi": "त् + ज → ज्ज: त्रिंशत् + जङ्घायाम् → त्रिंशज्जङ्घायाम्।",
        "frame": "संख्या: त्रिंशत् (३०) → कहाँ: जङ्घायाम् (घुटने से टखने तक की टाँग में)।",
    },
    "152": {
        "chain": {"steps": ["अंगुलियाँ: ६ × ५ = ३० (इकाई १४८-१४९)", "पादतल, कूर्च, गुल्फ: दस-दस (इकाई १५०)",
                            "जङ्घा: ३० (इकाई १५१)", "जानु: १० (इकाई १५२)"]},
        "chunks": "दश | जानुनि",
        "frame": "संख्या: दश (दस, एक ही बार) → कहाँ: जानुनि (घुटने में; उ-अन्त नपुंसक सप्तमी)।",
    },
}


# ===================================================================== IMAGE_SPECS
IMAGE_SPECS = {
    ("142", "diagram"): {
        "file": "sh5-sandhi-ashtavidha-142.svg",
        "alt": ("Table of the eight kinds of bone-joint closed by unit 142, in the order of units 135-141: kora (bud), "
                "ulūkhala (mortar), sāmudga (casket), pratara, tūnasevanī (conjectural tunnasevanī), vāyasatuṇḍa (crow's "
                "beak), maṇḍala (circle), śaṅkhāvarta (conch-whorl)."),
        "type": "table",
        "title": "इकाई १४२: आठ प्रकार की अस्थि-सन्धियाँ",
        "heads": ["नाम (इकाई)", "शब्दार्थ"],
        "rows": [["कोर (१३५)", "कली"], ["उलूखल (१३५)", "ओखली"], ["सामुद्ग (१३६)", "डिब्बा"], ["प्रतर (१३७)", "शब्दार्थ नहीं दिया गया"],
                 ["तूनसेवनी (१३८)", "अनुमानित पाठ; सेवनी = सीवन"], ["वायसतुण्ड (१३९)", "कौए की चोंच"],
                 ["मण्डल (१४०)", "गोला"], ["शंखावर्त (१४१)", "शंख की भँवर"]],
    },
    ("143", "chain"): {
        "file": "sh5-sahasradvaya-143.svg",
        "alt": ("Chain of unit 143: together with those resting on snāyu, peśī and sirā (probable); two thousand (what is "
                "counted is unstated); nothing more to say about them in applying the surgical instrument; so it is not "
                "stated separately."),
        "type": "chain",
        "title": "इकाई १४३: दो हजार, अलग से नहीं",
        "steps": ["स्नायु, पेशी, सिरा (सम्भावित) पर आश्रितों के साथ", "दो हजार (क्या गिना, अनकहा)",
                  "शस्त्र-प्रयोग में उनके विषय में और कहने योग्य नहीं", "इसलिए अलग से नहीं कहा जाता"],
    },
    ("146", "diagram"): {
        "file": "sh5-snayu-vibhaga-146.svg",
        "alt": ("Pie chart of the 900 snāyus of unit 144 as the data's check divides them: limbs 600 (unit 145), trunk 230 "
                "(unit 146), above 70 (unit 147)."),
        "type": "mermaid",
        "code": ("pie title नौ सौ स्नायुओं का बँटवारा\n"
                 "    \"शाखाएँ ६००\" : 600\n"
                 "    \"अन्तराधि (धड़) २३०\" : 230\n"
                 "    \"ऊर्ध्व ७०\" : 70\n"),
    },
    ("148", "chain"): {
        "file": "sh5-padanguli-snayu-148.svg",
        "alt": ("Chain of unit 148: there; in each single sakthi (probably each limb); in each toe; six each."),
        "type": "chain",
        "title": "इकाई १४८: हर अंगुली में छह-छह",
        "steps": ["तत्र: वहाँ", "एकैकस्मिन् सक्थि: प्रत्येक सक्थि (सम्भवतः शाखा) में", "पादाङ्गुल्याम् प्रत्येकम्: हर अंगुली में",
                  "षट् षट्: छह-छह"],
    },
    ("150", "diagram"): {
        "file": "sh5-padatala-gulpha-150.svg",
        "alt": ("Table of unit 150 in printed order: sole (pādatala) 10, kūrca 10, ankle (gulpha) 10: ten each."),
        "type": "table",
        "title": "इकाई १५०: दश दश, हर स्थान में दस",
        "heads": ["स्थान (क्रम से)", "स्नायु"],
        "rows": [["पादतल (तलवा)", "१०"], ["कूर्च", "१०"], ["गुल्फ (टखना)", "१०"]],
    },
    ("152", "chain"): {
        "file": "sh5-sakthi-snayu-152.svg",
        "alt": ("Chain of the snāyu count of one limb so far, units 148-152 in order: toes 6 x 5 = 30; sole, kūrca and "
                "ankle ten each; shank 30; knee 10."),
        "type": "chain",
        "title": "एक अंग के स्नायु: इकाई १४८-१५२",
        "steps": ["अंगुलियाँ: ६ × ५ = ३० (इकाई १४८-१४९)", "पादतल, कूर्च, गुल्फ: दस-दस (इकाई १५०)",
                  "जङ्घा: ३० (इकाई १५१)", "जानु: १० (इकाई १५२)"],
    },
}
