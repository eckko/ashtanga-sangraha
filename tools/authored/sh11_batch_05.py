from helpers import mcq, match, order, fill, multi, accepts


AUTHORED = {}

# ---------------------------------------------------------------- unit 51
AUTHORED["51"] = {
    "title": "रूपं शक्तिध्वजादीनां",
    "question": "By card 51, which wounds and which bhagandara does the verse say one should avoid?",
    "rule": ("All those wounds (व्रणान्) showing the form of a spear, a banner and the like are to be avoided (वर्जयेत्); "
             "so too bhagandara (fistula in ano, standard) that passes faeces, urine and vāyu (māruta) and has worms (कृमिणम्)."),
    "limits": ("Medium confidence. The verb of रूपम् is carried from दृश्यते (card 50). शक्ति is taken as spear; it may "
               "also mean 'power': no question on its sense. Printed सर्वास्तान् may stand for सर्वांस्तान् (possible "
               "flag): no question on that join. No cause, time or treatment is stated."),
    "explain_hi": ("पहली पंक्ति कार्ड ५० के व्रण-वर्णन को आगे ले जाती है: जहाँ शक्ति (भाला), ध्वज (पताका) आदि का रूप दिखे "
                   "(क्रिया ‘दृश्यते’ कार्ड ५० से आती है), उन सब व्रणों को वर्जयेत्, यानी त्याग देना चाहिए। "
                   "दूसरी पंक्ति में भगन्दर (fistula in ano, मानक) है जो मल, मूत्र और वायु को बहाता है और कृमियों वाला है; "
                   "डेटा के अनुसार यह भी ‘वर्जयेत्’ का कर्म है। "
                   "‘शक्ति’ का अर्थ ‘बल’ भी हो सकता है; डेटा भाला लेता है। "
                   "छपा ‘सर्वास्तान्’ नियमित सन्धि से ‘सर्वांस्तान्’ होता (सम्भव पाठ-चिह्न), इसलिए उस पर प्रश्न नहीं।"),
    "hook": "भाले या ध्वज के रूप वाले व्रण, और मल-मूत्र-वायु बहाने वाला कृमियों वाला भगन्दर: वर्जयेत्।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "In card 51, what does वर्जयेत् mean?",
            ("One should avoid", "वर्जयेत् = one should avoid (optative of √वृज्)."),
            [("One should cut open", "Cutting open would need a verb like √छिद्; वर्जयेत् = should avoid."),
             ("One should anoint", "Anointing would be from अभि-√अञ्ज्; वर्जयेत् = should avoid."),
             ("One should bandage", "Bandaging would be from √बन्ध्; वर्जयेत् = should avoid.")],
            "वर्जयेत् = one should avoid.",
            "वर्जयेत्, optative: one should avoid."),
        match(1, "Match each word of card 51 to its meaning.",
              [["ध्वज", "banner"], ["व्रणान्", "wounds"], ["कृमिणम्", "having worms"], ["मूत्र", "urine"],
               ["मारुत", "vāyu (bodily air)"], ["-वहम्", "carrying, passing"]],
              "ध्वज = banner, व्रणान् = wounds, कृमिणम् = having worms, मूत्र = urine, मारुत = vāyu (bodily air), -वहम् = carrying.",
              "ध्वज, व्रणान्, कृमिणम्, मूत्र, मारुत, -वहम्."),
        order(2, "Put the parts of card 51 in the printed order.",
              ["रूपं", "शक्तिध्वजादीनां", "सर्वास्तान्", "वर्जयेद्व्रणान्", "विण्मूत्रमारुतवहं", "कृमिणं च भगंदरं"],
              "Line 1: the form of spear, banner and the like; avoid all those wounds. Line 2: the bhagandara passing faeces, urine and vāyu (māruta), with worms.",
              "रूपं → शक्तिध्वजादीनां → सर्वास्तान् → वर्जयेद्व्रणान् → विण्मूत्रमारुतवहं → कृमिणं च भगंदरं.",
              role="extend",
              teaches="Line 1 ends with its verb वर्जयेत्; line 2 adds भगन्दरम् as a further accusative object of the same verb (data)."),
        mcq("discriminate", 3, "Which split of वर्जयेद्व्रणान् in card 51 is right?",
            ("वर्जयेत् + व्रणान्", "त् before the voiced व → द्: वर्जयेत् + व्रणान् → वर्जयेद्व्रणान्."),
            [("वर्जयेत् + अव्रणान्", "That would print वर्जयेदव्रणान्, with द before अ; the print has द्व."),
             ("वर्जयेः + व्रणान्", "A visarga after ए before व gives र्: that would print वर्जयेर्व्रणान्."),
             ("वर्जये + द्व्रणान्", "द्व्रणान् is not a word; the द् comes from the त् of वर्जयेत्.")],
            "वर्जयेत् (should avoid) + व्रणान् (wounds).",
            "त् + voiced consonant → द्."),
        mcq("apply", 4, "Which word of card 51 says that the bhagandara has worms?",
            ("कृमिणं", "कृमिन् (having worms), accusative कृमिणम्, printed कृमिणं."),
            [("विण्मूत्रमारुतवहं", "This says it passes faeces, urine and vāyu (māruta), not that it has worms."),
             ("शक्तिध्वजादीनां", "This names the spear, banner and the like of line 1, not worms."),
             ("वर्जयेद्व्रणान्", "This is 'should avoid the wounds'; it names no worms.")],
            "कृमि (worm) + -इन् (having) = कृमिन्; accusative कृमिणम्.",
            "कृमिणम् = having worms."),
        mcq("transfer", 5, "By the pattern of कृमिणम् (having worms, from कृमिन्), what does शिखिनम् (from शिखिन्, शिखा = crest) mean in a new example?",
            ("One having a crest", "-इन् = having: शिखा (crest) + इन् = शिखिन्, one having a crest; accusative शिखिनम्."),
            [("One without a crest", "Without would need a prefix such as निर्-; -इन् means having."),
             ("One cutting a crest", "Cutting would need a verb such as √छिद्; -इन् means having."),
             ("A thing made of crests", "Made of would be -मय; -इन् means having.")],
            "शिखिनम् = one having a crest, like कृमिणम् = one having worms.",
            "Noun + -इन् = having that thing.",
            teaches="-इन् added to a noun means 'having': कृमि → कृमिन् (having worms); its accusative is कृमिणम् (न् → ण् after ऋ in the same word)."),
    ],
}

# ---------------------------------------------------------------- unit 52
AUTHORED["52"] = {
    "title": "घट्टयन्जानुना जानु",
    "question": "By card 52, which movements of the patient does the verse name, and what does it say of him?",
    "rule": ("The patient (आतुरः) who strikes knee against knee (जानुना जानु घट्टयन्), raises and drops the two feet "
             "(पादावुद्यम्य पातयन्) and again and again turns aside (अपास्यति) his face (a conjectural reading) does not "
             "live (न स जीवति)."),
    "limits": ("Medium confidence. Printed वक्रम् (crooked) gives no sense with अपास्यति; vaktram (face) is a conjecture: "
               "no question on what is turned aside. The data takes both printed lines as one sentence. The text states "
               "the sign and its outcome only; nothing on cause or time."),
    "explain_hi": ("घुटने से घुटने को टकराता हुआ (जानुना जानु घट्टयन्) और दोनों पैरों को उठाकर गिराता हुआ (पादावुद्यम्य पातयन्), "
                   "जो रोगी बार-बार मुख को हटाता है (अनुमानित पाठ पर), वह जीवित नहीं रहता (न स जीवति)। "
                   "छपा ‘वक्रम्’ (टेढ़ा) ‘अपास्यति’ के साथ अर्थ नहीं देता; ‘वक्त्रम्’ (मुख) अनुमानित पाठ है, इसलिए उस पर प्रश्न नहीं। "
                   "डेटा के अनुसार दोनों छपी पंक्तियाँ एक ही वाक्य हैं: ‘घट्टयन्’, ‘पातयन्’ वर्तमान कृदन्त हैं, मुख्य क्रिया ‘न जीवति’ है। "
                   "‘पादावुद्यम्य’ में पादौ + उद्यम्य है: औ स्वर से पहले आव् बनता है।"),
    "hook": "घुटने से घुटना टकराए, पैर उठाकर पटके: आतुरो न स जीवति।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "In card 52, what does जानु mean?",
            ("Knee", "जानु = knee: जानुना जानु, knee with knee."),
            [("Ankle", "Ankle would be गुल्फ; जानु = knee."),
             ("Elbow", "Elbow would be कूर्पर; जानु = knee."),
             ("Thigh", "Thigh would be ऊरु; जानु = knee.")],
            "जानु = knee.",
            "जानु = knee."),
        order(1, "Put the words of line 1 of card 52 in the printed order.",
              ["घट्टयन्", "जानुना", "जानु", "पादौ", "उद्यम्य", "पातयन्"],
              "Striking; with the knee; the knee; the two feet; having raised; dropping.",
              "घट्टयन् → जानुना → जानु → पादौ → उद्यम्य → पातयन्."),
        match(2, "Match each word of card 52 to its meaning.",
              [["घट्टयन्", "striking"], ["जानुना", "with the knee"], ["पादौ", "the two feet"], ["उद्यम्य", "having raised"],
               ["पातयन्", "dropping"], ["आतुरः", "the patient"]],
              "घट्टयन् = striking, जानुना = with the knee, पादौ = the two feet, उद्यम्य = having raised, पातयन् = dropping, आतुरः = patient.",
              "घट्टयन्, जानुना, पादौ, उद्यम्य, पातयन्, आतुरः.", role="extend",
              teaches="जानुना जानु puts one noun in two cases: जानुना (instrumental, with the knee) strikes जानु (accusative, the knee)."),
        mcq("discriminate", 3, "Which split of पादावुद्यम्य in card 52 is right?",
            ("पादौ + उद्यम्य", "औ before a vowel → आव्: पादौ + उद्यम्य → पादावुद्यम्य."),
            [("पाद + उद्यम्य", "अ + उ → ओ: that would print पादोद्यम्य."),
             ("पादाव + उद्यम्य", "पादाव is not a form; the आव् comes from the औ of पादौ."),
             ("पादौ + वुद्यम्य", "वुद्यम्य is not a word; the व् comes from the औ of पादौ.")],
            "पादौ (the two feet) + उद्यम्य (having raised).",
            "औ + vowel → आव्."),
        mcq("apply", 4, "A patient keeps striking one knee against the other. Which phrase of card 52 names this?",
            ("घट्टयन् जानुना जानु", "घट्टयन् (striking) जानुना (with the knee) जानु (the knee)."),
            [("पादौ उद्यम्य पातयन्", "This is raising and dropping the two feet, not striking the knees."),
             ("यः अपास्यति मुहुः", "This is 'who turns aside again and again', not striking the knees."),
             ("आतुरः न सः जीवति", "This is the outcome, 'the patient does not live', not a movement.")],
            "Knee against knee = जानुना जानु घट्टयन्.",
            "घट्टयन् जानुना जानु = striking knee with knee."),
        mcq("transfer", 5, "By the pattern of पादौ + उद्यम्य → पादावुद्यम्य, how is बालौ + आगतौ (the two boys have come) joined in a new example?",
            ("बालावागतौ", "औ before a vowel → आव्: बालौ + आगतौ → बालावागतौ."),
            [("बालायागतौ", "आय् comes from ऐ before a vowel, not from औ."),
             ("बालवागतौ", "The long आ of आव् is kept: बालाव्-, not बालव्-."),
             ("बालौरागतौ", "र् comes from a visarga, not from औ.")],
            "बालौ + आगतौ = बालावागतौ, like पादौ + उद्यम्य = पादावुद्यम्य.",
            "औ + vowel → आव्.",
            teaches="Final औ before a vowel becomes आव्: पादौ + उद्यम्य → पादावुद्यम्य."),
    ],
}

# ---------------------------------------------------------------- unit 53
AUTHORED["53"] = {
    "title": "दंतैश्छिन्दन्नखाग्राणि",
    "question": "By card 53, which actions of the patient does the verse list, and in what order?",
    "rule": ("Cutting the nail-tips with the teeth (दन्तैः छिन्दन् नखाग्राणि), and with them hairs or blades of grass; "
             "scratching the ground with a piece of wood (भूमिं काष्ठेन विलिखन्); striking a clod with a clod "
             "(लोष्टं लोष्टेन ताडयन्)."),
    "limits": ("High confidence. Participles only, no main verb: the data takes cards 53 to 55 as probably one sentence "
               "ending in न स जीवति (card 55), boundaries not firm. तैः is taken as 'with those (teeth)'. Nothing is "
               "said of cause or time."),
    "explain_hi": ("दाँतों से नखों के अग्र भाग काटता हुआ, और उन्हीं (दाँतों) से केश या तिनके; लकड़ी से भूमि कुरेदता हुआ; ढेले को ढेले से मारता हुआ। "
                   "यहाँ केवल वर्तमान कृदन्त हैं (छिन्दन्, विलिखन्, ताडयन्), मुख्य क्रिया नहीं। "
                   "डेटा के अनुसार कार्ड ५३ से ५५ (छपी पंक्तियाँ १०२-१०६) सम्भवतः एक वाक्य हैं, जिसका मुख्य वाक्य ‘न स जीवति’ कार्ड ५५ में है; पर सीमाएँ पक्की नहीं। "
                   "‘दन्तैः’, ‘काष्ठेन’, ‘लोष्टेन’ तृतीया विभक्ति में साधन बताते हैं।"),
    "hook": "दाँत से नख काटे, लकड़ी से भूमि कुरेदे, ढेले से ढेला मारे।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "In card 53, what does लोष्ट mean?",
            ("A clod", "लोष्ट = a clod: लोष्टं लोष्टेन ताडयन्, striking a clod with a clod."),
            [("A twig", "A twig would be शाखा or similar; लोष्ट = clod."),
             ("A leaf", "A leaf would be पत्त्र; लोष्ट = clod."),
             ("A feather", "A feather would be पक्ष or पिच्छ; लोष्ट = clod.")],
            "लोष्ट = clod.",
            "लोष्ट = clod."),
        order(1, "Put the phrases of card 53 in the printed order.",
              ["दंतैश्छिन्दन्नखाग्राणि", "तैश्च केशांस्तृणानि वा", "भूमिं काष्ठेन विलिखन्", "लोष्टं लोष्टेन ताडयन्"],
              "Nail-tips cut with the teeth; with them hairs or grass; the ground scratched with wood; a clod struck with a clod.",
              "दंतैश्छिन्दन्नखाग्राणि → तैश्च केशांस्तृणानि वा → भूमिं काष्ठेन विलिखन् → लोष्टं लोष्टेन ताडयन्."),
        match(2, "Match each word of card 53 to its meaning.",
              [["दन्तैः", "with the teeth"], ["नखाग्राणि", "nail-tips"], ["तृणानि", "blades of grass"],
               ["काष्ठेन", "with a piece of wood"], ["विलिखन्", "scratching"], ["ताडयन्", "striking"]],
              "दन्तैः = with the teeth, नखाग्राणि = nail-tips, तृणानि = grass, काष्ठेन = with wood, विलिखन् = scratching, ताडयन् = striking.",
              "दन्तैः, नखाग्राणि, तृणानि, काष्ठेन, विलिखन्, ताडयन्.", role="extend",
              teaches="The instrumental names the tool: -ऐः (plural) in दन्तैः, -एन (singular) in काष्ठेन and लोष्टेन."),
        mcq("discriminate", 3, "Which split of केशांस्तृणानि in card 53 is right?",
            ("केशान् + तृणानि", "न् before त → ंस्त (or ँस्त): केशान् + तृणानि → केशांस्तृणानि."),
            [("केशाः + तृणानि", "That would print केशास्तृणानि, without the ं."),
             ("केशम् + तृणानि", "केशम् + तृणानि gives केशं तृणानि, with no स्."),
             ("केशान् + स्तृणानि", "स्तृणानि is not a word; the स् comes from sandhi.")],
            "केशान् (hairs) + तृणानि (blades of grass).",
            "न् + त → ंस्त."),
        mcq("apply", 4, "A patient scratches the ground with a piece of wood. Which phrase of card 53 names this?",
            ("भूमिं काष्ठेन विलिखन्", "भूमिम् (the ground) काष्ठेन (with wood) विलिखन् (scratching)."),
            [("लोष्टं लोष्टेन ताडयन्", "This is striking a clod with a clod, not scratching the ground."),
             ("दंतैश्छिन्दन्नखाग्राणि", "This is cutting the nail-tips with the teeth."),
             ("तैश्च केशांस्तृणानि वा", "This is cutting hairs or grass with the teeth.")],
            "Scratching the ground with wood = भूमिं काष्ठेन विलिखन्.",
            "विलिखन् = scratching."),
        mcq("transfer", 5, "By the pattern of काष्ठेन (with a piece of wood), what does खड्गेन mean in a new example?",
            ("With a sword", "-एन is the instrumental singular of अ-stems: खड्ग (sword) → खड्गेन, with a sword."),
            [("For a sword", "For a sword would be the dative खड्गाय."),
             ("In a sword", "In a sword would be the locative खड्गे."),
             ("From a sword", "From a sword would be the ablative खड्गात्.")],
            "खड्गेन = with a sword, like काष्ठेन = with a piece of wood.",
            "अ-stem + -एन = instrumental: with ...",
            teaches="The instrumental singular of अ-stems ends in -एन and names the tool: काष्ठेन = with a piece of wood."),
    ],
}

# ---------------------------------------------------------------- unit 54
AUTHORED["54"] = {
    "title": "सांद्रमूत्रः शुष्ककासी ज्वरी च यः",
    "question": "By card 54, which signs are named in its two 'who' (यः) clauses?",
    "rule": ("He who has thick urine (सान्द्रमूत्रः), a dry cough (शुष्ककासी) and fever (ज्वरी), with bristling hair on a "
             "conjectural reading; he who, laughing again and again (मुहुर्हसन्) and humming (sense not certain), strikes the bed "
             "with his foot (शय्यां पादेन हन्ति)."),
    "limits": ("Medium confidence. Printed दृष्टलोमा is read hṛṣṭalomā (bristling hair), a conjecture; क्ष्वेडन् is taken as "
               "'humming' but the sense is not certain: no question on either. Two यः clauses with no main verb; the data "
               "takes them as continuing into card 55 (न स जीवति)."),
    "explain_hi": ("पहली पंक्ति: जिसका मूत्र गाढ़ा हो (सान्द्रमूत्रः), जिसे सूखी खाँसी (शुष्ककासी) और ज्वर (ज्वरी) हो; अनुमानित पाठ पर, जिसके रोम खड़े हों। "
                   "दूसरी पंक्ति: जो बार-बार हँसता हुआ, बार-बार ‘क्ष्वेडन्’ (गुनगुनाता हुआ; अर्थ पक्का नहीं) पैर से शय्या पर आघात करता है। "
                   "छपा ‘दृष्टलोमा’ अर्थ नहीं देता; ‘हृष्टलोमा’ अनुमानित पाठ है; इस पर और ‘क्ष्वेडन्’ के अर्थ पर प्रश्न नहीं। "
                   "दोनों ‘यः’ वाले उपवाक्य हैं; डेटा के अनुसार मुख्य वाक्य कार्ड ५५ में (न स जीवति) आता है। "
                   "‘सान्द्रमूत्रः’ बहुव्रीहि है: जिसका मूत्र गाढ़ा है।"),
    "hook": "गाढ़ा मूत्र, सूखी खाँसी, ज्वर; बार-बार हँसे और शय्या पर पैर मारे।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "In card 54, what does शय्या mean?",
            ("Bed", "शय्या = bed: शय्यां पादेन हन्ति, strikes the bed with the foot."),
            [("Lamp", "A lamp would be दीप; शय्या = bed."),
             ("Door", "A door would be द्वार; शय्या = bed."),
             ("Wall", "A wall would be भित्ति; शय्या = bed.")],
            "शय्या = bed.",
            "शय्या = bed."),
        order(1, "Put the words of line 2 of card 54 in the printed order.",
              ["मुहुर्हसन्", "मुहुः क्ष्वेडन्", "शय्यां", "पादेन", "हंति", "यः"],
              "Laughing again and again; again and again क्ष्वेडन् (taken as humming, sense not certain); the bed; with the foot; strikes; who.",
              "मुहुर्हसन् → मुहुः क्ष्वेडन् → शय्यां → पादेन → हंति → यः."),
        match(2, "Match each word of card 54 to its meaning.",
              [["सान्द्र", "thick"], ["मूत्र", "urine"], ["शुष्क", "dry"], ["कासी", "having a cough"],
               ["ज्वरी", "having fever"], ["पादेन", "with the foot"]],
              "सान्द्र = thick, मूत्र = urine, शुष्क = dry, कासी = having a cough, ज्वरी = having fever, पादेन = with the foot.",
              "सान्द्र, मूत्र, शुष्क, कासी, ज्वरी, पादेन.", role="extend",
              teaches="-इन् gives 'having': कास (cough) → कासिन्, nominative कासी; ज्वर (fever) → ज्वरिन्, nominative ज्वरी."),
        multi("discriminate", 3, "Which of these does card 54 name with certainty?",
              [("Thick urine", "Yes: सान्द्रमूत्रः, one whose urine is thick."),
               ("Dry cough", "Yes: शुष्ककासी, one who has a dry cough."),
               ("Red eyes", "No: card 54 names no eyes."),
               ("Striking the bed with the foot", "Yes: शय्यां पादेन हन्ति."),
               ("Grinding the teeth", "No: card 54 names no teeth.")],
              [0, 1, 3],
              "Sure signs: thick urine, dry cough, fever, laughing again and again, striking the bed with the foot.",
              "सान्द्रमूत्रः, शुष्ककासी, ज्वरी, मुहुर्हसन्, शय्यां पादेन हन्ति."),
        mcq("apply", 4, "Why is मुहुः printed मुहुर् before हसन् in card 54?",
            ("उः before a voiced sound → उर्", "ह is voiced; after उ the visarga becomes र्: मुहुर्हसन्."),
            [("उः before any consonant → उर्", "Not any: before क्ष the print keeps ः (मुहुः क्ष्वेडन्, same card)."),
             ("उः before ह becomes ओ", "ओ comes from अः before a voiced consonant, not from उः."),
             ("उः before ह is dropped", "It is not dropped: the print has र्.")],
            "मुहुः + हसन् → मुहुर्हसन्.",
            "Visarga after a vowel other than अ/आ, before a voiced sound → र्."),
        mcq("transfer", 5, "By the pattern of सान्द्रमूत्रः (one whose urine is thick), what does स्थूलग्रीवः mean in a new example?",
            ("One whose neck is thick", "Bahuvrīhi: स्थूल (thick) + ग्रीवा (neck) = one whose neck is thick."),
            [("One whose neck is thin", "स्थूल means thick, not thin."),
             ("One who has no neck", "No neck would need a prefix like अ- or निर्-."),
             ("One who grips a neck", "Gripping would need a verb; the compound names his own neck.")],
            "स्थूलग्रीवः = one whose neck is thick, like सान्द्रमूत्रः = one whose urine is thick.",
            "Adjective + noun as bahuvrīhi = one whose ... is ...",
            teaches="Adjective + noun can form a bahuvrīhi describing a person: सान्द्र (thick) + मूत्र (urine) = one whose urine is thick."),
    ],
}

# ---------------------------------------------------------------- unit 55
AUTHORED["55"] = {
    "title": "मुहुश्छिद्राणि विमृशन्",
    "question": "By card 55, how does line 1 appear to close the series begun in card 53, and which signs open line 2?",
    "rule": ("Line 1: the patient touching the openings (छिद्राणि) again and again does not live (न स जीवति). Line 2 opens a new "
             "list: him whose breath goes upward (ऊर्ध्वश्वासम्; probably laboured breathing), whose heat has gone "
             "(गतोष्माणम्), whose groins are struck by pain (शूलोपहतवंक्षणम्)."),
    "limits": ("Medium confidence. Which openings छिद्राणि means is not stated; विमृशन् may also mean 'considering': no "
               "question on either. Line 1 appears to complete the sentence begun in card 53 (or 54) (data); line 2 is the object of परिवर्जयेत् "
               "(card 56). Laboured breathing is probable (data)."),
    "explain_hi": ("पहली पंक्ति: बार-बार छिद्रों को छूता हुआ वह रोगी जीवित नहीं रहता। कौन-से छिद्र, यह नहीं कहा गया; ‘विमृशन्’ का अर्थ ‘विचार करता हुआ’ भी हो सकता है। "
                   "डेटा के अनुसार यह पंक्ति सम्भवतः कार्ड ५३ (या ५४) से चले वाक्य को पूरा करती है। "
                   "दूसरी पंक्ति नई सूची खोलती है: जिसकी श्वास ऊपर की ओर हो (सम्भवतः कष्टपूर्ण श्वास), जिसकी ऊष्मा चली गई हो, जिसके वंक्षण (जाँघ के जोड़) पीड़ा से पीड़ित हों। "
                   "ये द्वितीया में हैं और कार्ड ५६ के ‘परिवर्जयेत्’ के कर्म हैं। "
                   "‘गतोष्माणम्’ में गत + ऊष्माणम् है: अ + ऊ → ओ।"),
    "hook": "बार-बार छिद्र छूए: न स जीवति। फिर: ऊपर की श्वास, ऊष्मा गई, वंक्षण में शूल।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "In card 55, what does गतोष्माणम् describe?",
            ("One whose heat has gone", "गत (gone) + ऊष्मन् (heat): one whose heat has gone."),
            [("One whose heat has risen", "गत means gone, not risen."),
             ("One whose thirst has gone", "ऊष्मन् is heat, not thirst."),
             ("One whose sleep has gone", "ऊष्मन् is heat, not sleep.")],
            "गतोष्माणम् = one whose heat has gone.",
            "गत + ऊष्मन् = heat gone."),
        match(1, "Match each word of card 55 to its meaning.",
              [["ऊर्ध्व", "upward"], ["श्वास", "breath"], ["गत", "gone"], ["ऊष्मन्", "heat"], ["शूल", "pain"],
               ["वङ्क्षण", "groin"]],
              "ऊर्ध्व = upward, श्वास = breath, गत = gone, ऊष्मन् = heat, शूल = pain, वङ्क्षण = groin.",
              "ऊर्ध्व, श्वास, गत, ऊष्मन्, शूल, वङ्क्षण."),
        order(2, "Put the parts of card 55 in the printed order.",
              ["मुहुश्छिद्राणि", "विमृशन्नातुरो", "न स जीवति", "ऊर्ध्वश्वासं", "गतोष्माणं", "शूलोपहतवंक्षणं"],
              "Line 1 closes a sentence with न स जीवति; line 2 lists upward breath, heat gone, groins struck by pain.",
              "मुहुश्छिद्राणि → विमृशन्नातुरो → न स जीवति → ऊर्ध्वश्वासं → गतोष्माणं → शूलोपहतवंक्षणं.",
              role="extend",
              teaches="Line 1 ends one sentence with न स जीवति; line 2 opens a new list in the accusative (-म्), objects of a verb in card 56."),
        mcq("discriminate", 3, "Which split of गतोष्माणम् in card 55 is right?",
            ("गत + ऊष्माणम्", "अ + ऊ → ओ: गत + ऊष्माणम् → गतोष्माणम्."),
            [("गतः + ऊष्माणम्", "अः before ऊ gives अ with a gap: it would print गत ऊष्माणम्."),
             ("गति + ऊष्माणम्", "इ + ऊ → यू: it would print गत्यूष्माणम्."),
             ("गतो + ष्माणम्", "ष्माणम् is not a word; ऊष्माणम् (heat) is.")],
            "गत (gone) + ऊष्माणम् (heat): अ + ऊ → ओ.",
            "अ + ऊ → ओ."),
        mcq("apply", 4, "Why is मुहुः printed मुहुश् before छिद्राणि in card 55?",
            ("ः before छ → श्", "Before च or छ the visarga becomes श्: मुहुः + छिद्राणि → मुहुश्छिद्राणि."),
            [("ः before any consonant → श्", "Not any: before ह it gives र् (मुहुर्हसन्, card 54)."),
             ("ः after उ always → श्", "Not always: मुहुर्हसन् (card 54) has र्."),
             ("ः before छ is dropped", "It is not dropped: the print has श्.")],
            "मुहुः + छिद्राणि → मुहुश्छिद्राणि.",
            "Visarga + च/छ → श्."),
        mcq("transfer", 5, "By the pattern of गत + ऊष्माणम् → गतोष्माणम्, how is दृढ + ऊरुः (one with firm thighs) joined in a new example?",
            ("दृढोरुः", "अ + ऊ → ओ: दृढ + ऊरुः → दृढोरुः."),
            [("दृढौरुः", "औ comes from अ + ओ or अ + औ, not from अ + ऊ."),
             ("दृढूरुः", "The अ is not lost; it merges with ऊ into ओ."),
             ("दृढवूरुः", "No व् is inserted; अ and ऊ merge into ओ.")],
            "दृढ + ऊरुः = दृढोरुः, like गत + ऊष्माणम् = गतोष्माणम्.",
            "अ + ऊ → ओ.",
            teaches="अ or आ before उ or ऊ gives ओ: गत + ऊष्माणम् → गतोष्माणम्."),
    ],
}

# ---------------------------------------------------------------- unit 56
AUTHORED["56"] = {
    "title": "शर्म चानधिगच्छंतं",
    "question": "By card 56, whom should the wise one avoid, and which two opposite changes does line 2 name?",
    "rule": ("Line 1: the wise one (बुद्धिमान्) should avoid (परिवर्जयेत्) him who does not obtain ease (शर्म "
             "अनधिगच्छन्तम्), which appears to complete the list of card 55 (data). Line 2: he whose disorders (विकाराः) increase (वर्धन्ते) and "
             "whose natural state (प्रकृतिः) diminishes (परिहीयते)."),
    "limits": ("High confidence. Line 1 appears to complete card 55 (data); line 2 continues into card 57. 'Should avoid' is the "
               "text's own word; nothing more is added. Printed वर्द्धंते is an orthographic doubling of वर्धन्ते."),
    "explain_hi": ("पहली पंक्ति सम्भवतः कार्ड ५५ की सूची पूरी करती है: और जो सुख (शर्म) नहीं पाता, उसे बुद्धिमान परिवर्जयेत्, यानी त्याग दे; यह पाठ का अपना शब्द है। "
                   "दूसरी पंक्ति नया वाक्य खोलती है: जिसके विकार बढ़ते हैं और प्रकृति (स्वाभाविक अवस्था) क्षीण होती है; यह वाक्य कार्ड ५७ में पूरा होता है। "
                   "विकार बढ़ें और प्रकृति घटे: दोनों उलटी दिशाएँ इसी इकाई में हैं। "
                   "‘चानधिगच्छन्तम्’ में च + अनधिगच्छन्तम् है (अ + अ → आ); ‘अन्-’ स्वर से पहले निषेध करता है।"),
    "hook": "सुख न पाए: बुद्धिमान त्यागे। विकार बढ़ें, प्रकृति घटे।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "In card 56, what does शर्म mean?",
            ("Ease, comfort", "शर्मन् = ease, comfort: शर्म अनधिगच्छन्तम्, not obtaining ease."),
            [("Shame, disgrace", "Shame is the Hindi sense of शर्म; the Sanskrit शर्मन् means ease."),
             ("Effort, toil", "Effort would be यत्न or श्रम; शर्मन् = ease."),
             ("Heat, fever", "Fever would be ज्वर; शर्मन् = ease.")],
            "शर्म = ease, comfort.",
            "शर्मन् = ease."),
        match(1, "Match each word of card 56 to its meaning.",
              [["शर्म", "ease"], ["अनधिगच्छन्तम्", "not obtaining"], ["बुद्धिमान्", "the wise one"],
               ["परिवर्जयेत्", "should avoid"], ["विकाराः", "disorders"], ["प्रकृतिः", "natural state"]],
              "शर्म = ease, अनधिगच्छन्तम् = not obtaining, बुद्धिमान् = the wise one, परिवर्जयेत् = should avoid, विकाराः = disorders, प्रकृतिः = natural state.",
              "शर्म, अनधिगच्छन्तम्, बुद्धिमान्, परिवर्जयेत्, विकाराः, प्रकृतिः."),
        order(2, "Put the parts of card 56 in the printed order.",
              ["शर्म", "चानधिगच्छंतं", "बुद्धिमान्", "परिवर्जयेत्", "विकारा यस्य वर्द्धंते", "प्रकृतिः परिहीयते"],
              "Ease; and not obtaining; the wise one; should avoid; whose disorders increase; the natural state diminishes.",
              "शर्म → चानधिगच्छंतं → बुद्धिमान् → परिवर्जयेत् → विकारा यस्य वर्द्धंते → प्रकृतिः परिहीयते.",
              role="extend",
              teaches="अन्- negates before a vowel: अन् + अधिगच्छन्तम् = not obtaining."),
        mcq("discriminate", 3, "By card 56, which pair of changes does line 2 set against each other?",
            ("Disorders grow, natural state wanes", "विकाराः वर्धन्ते ⇄ प्रकृतिः परिहीयते."),
            [("Ease grows, disorders wane", "Line 2 names no growing ease; the disorders grow."),
             ("Natural state grows, ease wanes", "The natural state diminishes (परिहीयते); it does not grow."),
             ("Disorders wane, natural state grows", "This reverses both: disorders increase, the natural state diminishes.")],
            "Disorders (विकाराः) increase; the natural state (प्रकृतिः) diminishes.",
            "विकार ↑ ⇄ प्रकृति ↓."),
        mcq("apply", 4, "Why is विकाराः printed विकारा before यस्य in card 56?",
            ("आः drops its visarga before a voiced sound", "य is voiced; after आ the visarga is dropped: विकारा यस्य."),
            [("Every visarga drops before a voiced sound", "Not every: after अ it gives ओ (आतुरो न, card 52)."),
             ("आः before य becomes आर् by rule", "र् comes from a visarga after vowels other than अ/आ."),
             ("The plural is written -आ without ः", "The nominative plural is विकाराः; ः drops only by sandhi.")],
            "विकाराः + यस्य → विकारा यस्य.",
            "आः + voiced sound → आ."),
        mcq("transfer", 5, "By the pattern of विकारा यस्य, how is हंसाः + यान्ति (the swans go) written in a new example?",
            ("हंसा यान्ति", "आः before the voiced य drops its visarga: हंसा यान्ति."),
            [("हंसो यान्ति", "ओ comes from अः before a voiced consonant, not from आः."),
             ("हंसार्यान्ति", "र् comes from a visarga after vowels other than अ/आ."),
             ("हंसास्यान्ति", "स् comes from a visarga before त or थ, not before य.")],
            "हंसाः + यान्ति = हंसा यान्ति, like विकाराः + यस्य = विकारा यस्य.",
            "आः + voiced sound → आ.",
            teaches="A visarga after आ is dropped before a voiced sound: विकाराः + यस्य → विकारा यस्य."),
    ],
}

# ---------------------------------------------------------------- unit 57
AUTHORED["57"] = {
    "title": "सहसा सहसा तस्य",
    "question": "By card 57, what does line 1 say of the one whose disorders increase, and what does line 2 begin?",
    "rule": ("Line 1 completes card 56: suddenly, suddenly (सहसा सहसा), Death (मृत्युः) takes away (हरति) his life "
             "(जीवितम्). Line 2 begins a new sentence: the patient for whom a physician (वैद्यः), to prepare medicine "
             "(संपादयितुम् औषधम्) ... (continued in card 58)."),
    "limits": ("Medium confidence. सहसा is printed twice, for emphasis (kept as printed). Line 2 has no finite verb; the data "
               "says it continues in card 58 (यतमानो न शक्नोति). Nothing is added on how or why."),
    "explain_hi": ("पहली पंक्ति कार्ड ५६ के वाक्य को पूरा करती है: अचानक, अचानक उसके जीवन को मृत्यु हर लेती है। ‘सहसा’ दो बार छपा है, ज़ोर देने के लिए। "
                   "दूसरी पंक्ति नया वाक्य शुरू करती है: जिस रोगी को लक्ष्य करके (उद्दिश्य) वैद्य औषध तैयार करने के लिए (संपादयितुम्) ...; "
                   "डेटा के अनुसार यह कार्ड ५८ (यतमानो न शक्नोति) में पूरा होता है। "
                   "‘उद्दिश्य’ उपसर्ग (उद्-) वाले धातु का ल्यप् रूप है (-य), ‘संपादयितुम्’ तुमुन् (-तुम्) है: उद्देश्य बताता है।"),
    "hook": "सहसा सहसा मृत्यु जीवन हर ले; फिर: जिस रोगी के लिए वैद्य औषध बनाने चले ...",
    "core": False,
    "questions": [
        mcq("pretest", 0, "In card 57, what does सहसा mean?",
            ("Suddenly", "सहसा = suddenly; printed twice for emphasis."),
            [("Slowly", "Slowly would be शनैः; सहसा = suddenly."),
             ("Rarely", "Rarely would be क्वचित्; सहसा = suddenly."),
             ("Gently", "Gently would be मृदु; सहसा = suddenly.")],
            "सहसा = suddenly.",
            "सहसा = suddenly."),
        order(1, "Put the words of line 1 of card 57 in the printed order.",
              ["सहसा सहसा", "तस्य", "मृत्युः", "हरति", "जीवितम्"],
              "Suddenly, suddenly; his; Death; takes away; life.",
              "सहसा सहसा → तस्य → मृत्युः → हरति → जीवितम्."),
        match(2, "Match each word of card 57 to its meaning.",
              [["मृत्युः", "Death"], ["हरति", "takes away"], ["जीवितम्", "life"], ["उद्दिश्य", "having in view"],
               ["वैद्यः", "physician"], ["औषधम्", "medicine"]],
              "मृत्युः = Death, हरति = takes away, जीवितम् = life, उद्दिश्य = having in view, वैद्यः = physician, औषधम् = medicine.",
              "मृत्युः, हरति, जीवितम्, उद्दिश्य, वैद्यः, औषधम्.", role="extend",
              teaches="A root with a prefix forms its absolutive in -य, not -त्वा: उद्-√दिश् → उद्दिश्य (having in view)."),
        mcq("discriminate", 3, "Which split of यमुद्दिश्यातुरं in card 57 is right?",
            ("यम् + उद्दिश्य + आतुरम्", "म् joins a following vowel; अ + आ → आ: यमुद्दिश्यातुरम्."),
            [("यमुद् + दिश्य + आतुरम्", "यमुद् is not a word; यम् (whom) and उद्दिश्य are."),
             ("यम् + उद्दिश्य + यातुरम्", "यातुरम् is not a word; the या comes from य + आ."),
             ("यमः + उद्दिश्य + आतुरम्", "अः before उ gives अ with a gap: यम उद्दिश्य.")],
            "यम् (whom) + उद्दिश्य (having in view) + आतुरम् (patient).",
            "म् + vowel → joined; अ + आ → आ."),
        mcq("apply", 4, "In card 57, what does the -तुम् of संपादयितुम् express?",
            ("Purpose: to prepare", "-तुम् is the infinitive: in order to prepare (the medicine)."),
            [("Past act: having prepared", "Having prepared would be an absolutive in -य or -त्वा."),
             ("Command: let him prepare", "A command would be an imperative such as संपादयतु."),
             ("Wish: he should prepare", "A wish or rule would be an optative such as संपादयेत्.")],
            "संपादयितुम् = to prepare; with औषधम्, to prepare the medicine.",
            "-तुम् = infinitive of purpose."),
        mcq("transfer", 5, "By the pattern of संपादयितुम् (to prepare), what does रक्षितुम् (from √रक्ष्) mean in a new example?",
            ("To protect", "-तुम् = infinitive: रक्षितुम्, to protect."),
            [("Having protected", "Having protected would be रक्षित्वा."),
             ("He protects", "He protects would be रक्षति."),
             ("The protected one", "The protected one would be रक्षितः.")],
            "रक्षितुम् = to protect, like संपादयितुम् = to prepare.",
            "-तुम् = to ...",
            teaches="The infinitive ends in -तुम् and expresses purpose: संपादयितुम् = to prepare."),
    ],
}

# ---------------------------------------------------------------- unit 58
AUTHORED["58"] = {
    "title": "यतमानो न शक्नोति",
    "question": "By card 58, what happens to the striving physician, and how is the medicine of line 2 described?",
    "rule": ("Line 1 completes card 57: striving (यतमानः), he is not able (न शक्नोति); that patient's life is hard to "
             "obtain (दुर्लभं तस्य जीवितम्). Line 2 describes a medicine: known (विज्ञातम्), successful many times (बहुशः "
             "सिद्धम्), applied according to rule (विधिवत् अवचारितम्)."),
    "limits": ("Medium confidence. The subject of शक्नोति (the physician, card 57) and the noun of line 2 (औषधम्, card 59) are "
               "not printed in this card (data). सिद्ध here = successful, proved effective; अवचारित = applied (wording open). "
               "No question asks who the subject is."),
    "explain_hi": ("पहली पंक्ति कार्ड ५७ का वाक्य पूरा करती है: यत्न करता हुआ (वैद्य) समर्थ नहीं होता; उसका जीवन दुर्लभ है। "
                   "दूसरी पंक्ति एक औषध का वर्णन है: जाना हुआ, बहुत बार सफल (सिद्धम्) और विधि के अनुसार प्रयुक्त; डेटा के अनुसार संज्ञा ‘औषधम्’ कार्ड ५९ में है। "
                   "यहाँ ‘सिद्ध’ का अर्थ सफल है। "
                   "‘विधिवच्चावचारितम्’ में विधिवत् + च (त् + च → च्च) और च + अवचारितम् (अ + अ → आ) है।"),
    "hook": "यत्न करते हुए न कर सके: दुर्लभं जीवितम्। औषध जाना हुआ, बार-बार सिद्ध, विधि से दिया।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "In card 58, what does दुर्लभम् mean?",
            ("Hard to obtain", "दुर्- (hard) + लभ (to obtain): hard to obtain."),
            [("Easy to obtain", "Easy to obtain would be सुलभ; दुर्- means hard."),
             ("Long-lasting", "Long-lasting would be चिरस्थायी; दुर्लभ = hard to obtain."),
             ("Already lost", "Lost would be नष्ट; दुर्लभ = hard to obtain.")],
            "दुर्लभम् = hard to obtain.",
            "दुर्- + लभ = hard to obtain."),
        match(1, "Match each word of card 58 to its meaning.",
              [["यतमानः", "striving"], ["शक्नोति", "is able"], ["जीवितम्", "life"], ["विज्ञातम्", "known"],
               ["बहुशः", "many times"], ["विधिवत्", "according to rule"]],
              "यतमानः = striving, शक्नोति = is able, जीवितम् = life, विज्ञातम् = known, बहुशः = many times, विधिवत् = according to rule.",
              "यतमानः, शक्नोति, जीवितम्, विज्ञातम्, बहुशः, विधिवत्."),
        order(2, "Put the words of line 2 of card 58 in the printed order.",
              ["विज्ञातम्", "बहुशः", "सिद्धम्", "विधिवत्", "च", "अवचारितम्"],
              "Known; many times; successful; according to rule; and; applied.",
              "विज्ञातम् → बहुशः → सिद्धम् → विधिवत् → च → अवचारितम्.",
              role="extend",
              teaches="Line 2 lists neuter participles in -तम् that describe a medicine whose noun (औषधम्) comes in card 59."),
        mcq("discriminate", 3, "Which split of विधिवच्चावचारितं in card 58 is right?",
            ("विधिवत् + च + अवचारितम्", "त् before च → च्; अ + अ → आ: विधिवच्चावचारितम्."),
            [("विधिवत् + च + वचारितम्", "That would print विधिवच्चवचारितम्, without the आ."),
             ("विधि + वच्च + अवचारितम्", "वच्च is not a word; विधिवत् (according to rule) is."),
             ("विधिवः + च + अवचारितम्", "A visarga before च gives श्: that would print विधिवश्चा-.")],
            "विधिवत् (by rule) + च (and) + अवचारितम् (applied).",
            "त् + च → च्च; अ + अ → आ."),
        mcq("apply", 4, "Why is यतमानः printed यतमानो before न in card 58?",
            ("अः before a voiced consonant → ओ", "न is a voiced consonant: यतमानः + न → यतमानो न."),
            [("आः before a voiced consonant → ओ", "आः drops its visarga before a voiced sound; the ending here is अः."),
             ("ः before any consonant → ओ", "Not any: the print keeps ः before स in बहुशः सिद्धम् (same card)."),
             ("ओ is the nominative ending", "The nominative singular is -अः; ओ comes only from sandhi.")],
            "यतमानः + न → यतमानो न.",
            "अः + voiced consonant → ओ."),
        mcq("transfer", 5, "By the pattern of विधिवत् + च → विधिवच्च, how is सरित् + च (and the river) joined in a new example?",
            ("सरिच्च", "त् before च → च्: सरित् + च → सरिच्च."),
            [("सरिद्च", "द् comes from त् before a voiced sound; च is not voiced."),
             ("सरिश्च", "श् comes from a visarga before च, not from त्."),
             ("सरिच", "The त् is not lost; it becomes च्, giving च्च.")],
            "सरित् + च = सरिच्च, like विधिवत् + च = विधिवच्च.",
            "त् + च → च्च.",
            teaches="Final त् before च or छ becomes च्: विधिवत् + च → विधिवच्च."),
    ],
}

# ---------------------------------------------------------------- unit 59
AUTHORED["59"] = {
    "title": "न सिद्ध्यत्यौषधं यस्य",
    "question": "By card 59, what does the verse say when medicine does not succeed, and which sign begins line 2?",
    "rule": ("For whom medicine (औषधम्) does not succeed (न सिद्ध्यति), for him there is no treatment (नास्ति तस्य "
             "चिकित्सितम्). Line 2: he for whom, when medicine or food (औषधे अन्ने वा) is being prepared, there would be a "
             "reversal (विपर्ययः)."),
    "limits": ("Medium confidence. Card 58's line 2 probably describes this medicine (data). Whether विपर्यय is a reversal of "
               "the preparation or of its effect is left open: no question on it. कल्प्यमाने is taken with both nouns "
               "(data). Line 2 continues into card 60."),
    "explain_hi": ("जिसके लिए औषध सफल नहीं होता, उसका चिकित्सित (उपचार) नहीं है। "
                   "डेटा के अनुसार कार्ड ५८ की दूसरी पंक्ति (जाना हुआ, बार-बार सफल, विधि से प्रयुक्त) इसी औषध का वर्णन है। "
                   "दूसरी पंक्ति: जिसके लिए औषध या अन्न तैयार किए जाते समय विपर्यय (उलटा परिणाम) हो; यह तैयारी का उलटना है या प्रभाव का, यह खुला है। "
                   "यह वाक्य कार्ड ६० में आगे चलता है। "
                   "सन्धियाँ: सिद्ध्यति + औषधम् (इ + औ → यौ), न + अस्ति (अ + अ → आ), औषधे + अन्ने (ए + अ → एऽ)।"),
    "hook": "औषध सफल न हो: चिकित्सित नहीं। औषध या अन्न बनाते विपर्यय हो।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "In card 59, what does चिकित्सितम् mean?",
            ("Treatment", "चिकित्सित = treatment: नास्ति तस्य चिकित्सितम्, for him there is no treatment."),
            [("Physician", "A physician is वैद्य (card 57); चिकित्सित = treatment."),
             ("Pulse-reading", "Pulse-reading would be नाडीपरीक्षा; चिकित्सित = treatment."),
             ("Poisoning", "Poisoning would be from विष; चिकित्सित = treatment.")],
            "चिकित्सितम् = treatment.",
            "चिकित्सित = treatment."),
        match(1, "Match each word of card 59 to its meaning.",
              [["सिद्ध्यति", "succeeds"], ["औषधम्", "medicine"], ["नास्ति", "there is not"], ["चिकित्सितम्", "treatment"],
               ["अन्ने", "in food"], ["विपर्ययः", "reversal"]],
              "सिद्ध्यति = succeeds, औषधम् = medicine, नास्ति = there is not, चिकित्सितम् = treatment, अन्ने = in food, विपर्ययः = reversal.",
              "सिद्ध्यति, औषधम्, नास्ति, चिकित्सितम्, अन्ने, विपर्ययः."),
        fill(2, "In card 59, नास्ति (there is not) joins न with the verb ____ (there is); type it in Devanagari or in English letters (e.g. dharma).",
             accepts("अस्ति", "asti"),
             "न + अस्ति → नास्ति: अ + अ → आ.",
             "न + अस्ति → नास्ति: अ + अ → आ, 'there is not'.",
             "न + अस्ति = नास्ति."),
        mcq("discriminate", 3, "Which split of सिद्ध्यत्यौषधं in card 59 is right?",
            ("सिद्ध्यति + औषधम्", "इ before a different vowel → य्: सिद्ध्यति + औषधम् → सिद्ध्यत्यौषधम्."),
            [("सिद्ध्यते + औषधम्", "ए before औ gives अय् (the य् may drop): it would print सिद्ध्यतयौषधम् or सिद्ध्यत औषधम्."),
             ("सिद्ध्यत् + यौषधम्", "यौषधम् is not a word; the य् comes from the इ of सिद्ध्यति."),
             ("सिद्ध्य + त्यौषधम्", "त्यौषधम् is not a word; औषधम् (medicine) is.")],
            "सिद्ध्यति (succeeds) + औषधम् (medicine).",
            "इ + unlike vowel → य्."),
        mcq("apply", 4, "Why is औषधे followed by ऽन्ने (for अन्ने) in card 59?",
            ("ए + अ → ए, and the अ drops (ऽ)", "After a final ए, an initial अ is dropped, marked ऽ: औषधेऽन्ने."),
            [("ए + अ → ऐ, and the अ drops (ऽ)", "ऐ comes from अ + ए; the print keeps ए."),
             ("ए + अ → या, and the अ drops (ऽ)", "या comes from इ + आ; the print keeps ए."),
             ("ए + अ → ओ, and the अ drops (ऽ)", "ओ comes from अः before अ; the print keeps ए.")],
            "औषधे + अन्ने → औषधेऽन्ने.",
            "ए + अ → एऽ."),
        mcq("transfer", 5, "By the pattern of औषधे + अन्ने → औषधेऽन्ने, how is क्षेत्रे + अत्र (here in the field) joined in a new example?",
            ("क्षेत्रेऽत्र", "After a final ए the अ drops, marked ऽ: क्षेत्रेऽत्र."),
            [("क्षेत्रैत्र", "ऐ comes from अ + ए, not from ए + अ."),
             ("क्षेत्रयत्र", "A final ए does not become अय् before अ; the अ drops (ऽ)."),
             ("क्षेत्रात्र", "आ comes from अ + अ; the word ends in ए.")],
            "क्षेत्रे + अत्र = क्षेत्रेऽत्र, like औषधे + अन्ने = औषधेऽन्ने.",
            "ए + अ → एऽ.",
            teaches="After a word-final ए (or ओ) an initial अ is dropped and marked ऽ: औषधे + अन्ने → औषधेऽन्ने."),
    ],
}

# ---------------------------------------------------------------- unit 60
AUTHORED["60"] = {
    "title": "निवाते सेंधनं यस्य",
    "question": "By card 60, what happens to the light of the person named in line 2?",
    "rule": ("Line 2 (sure): he whose light or flame (ज्योतिः), even with fuel (सेन्धनम्), goes out (उपशाम्यति) in a windless "
             "place (निवाते). Line 1, on a doubtful reading, says that even a healthy one (स्वस्थोऽपि) suddenly does not live."),
    "limits": ("Prose, low confidence. Line 1: printed वर्णवादेः cannot be construed; varṇādeḥ is a conjecture and the "
               "sense is not firm: no question on line 1. Which light (lamp or fire) is not stated. Line 2 is a separate "
               "sign (data); its main clause is not in this card."),
    "explain_hi": ("यह इकाई गद्य (डेटा का प्रकार) है, विश्वास कम। "
                   "पहली पंक्ति का छपा ‘वर्णवादेः’ अर्थ नहीं देता; ‘वर्णादेः’ (वर्ण यानी रंग आदि से) अनुमानित पाठ है और अर्थ पक्का नहीं: "
                   "अनुमानित पाठ पर, अचानक स्वस्थ होने पर भी वह जीवित नहीं रहता। इस पंक्ति पर कोई प्रश्न नहीं। "
                   "दूसरी पंक्ति पक्की है: वायुरहित स्थान में (निवाते), ईंधन सहित (सेन्धनम्) भी जिसकी ज्योति बुझ जाती है (उपशाम्यति)। "
                   "ज्योति दीपक की है या अग्नि की, यह नहीं कहा गया। ‘सेन्धनम्’ = स + इन्धनम् (अ + इ → ए)।"),
    "hook": "हवा नहीं, ईंधन है, फिर भी जिसकी ज्योति बुझ जाए।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "In card 60, what does निवाते mean?",
            ("In a windless place", "नि-वात = without wind; निवाते, locative: in a windless place."),
            [("In a very windy place", "नि- here means without; the place has no wind."),
             ("In a dark, closed room", "निवात names the lack of wind, not darkness."),
             ("In an open courtyard", "निवात names the lack of wind, not a courtyard.")],
            "निवाते = in a windless place.",
            "निवात = windless."),
        match(1, "Match each word of line 2 of card 60 to its meaning.",
              [["निवाते", "in a windless place"], ["सेन्धनम्", "with fuel"], ["यस्य", "whose"], ["ज्योतिः", "light, flame"],
               ["उपशाम्यति", "goes out"]],
              "निवाते = in a windless place, सेन्धनम् = with fuel, यस्य = whose, ज्योतिः = light or flame, उपशाम्यति = goes out.",
              "निवाते, सेन्धनम्, यस्य, ज्योतिः, उपशाम्यति."),
        order(2, "Put the words of line 2 of card 60 in the printed order.",
              ["निवाते", "सेंधनं", "यस्य", "ज्योतिः", "च अपि", "उपशाम्यति"],
              "In a windless place; with fuel; whose; light; even; goes out.",
              "निवाते → सेंधनं → यस्य → ज्योतिः → च अपि → उपशाम्यति.",
              role="extend",
              teaches="सेन्धनम् = स (with) + इन्धनम् (fuel), a bahuvrīhi: having fuel; it describes ज्योतिः."),
        mcq("discriminate", 3, "Which split of सेंधनं in card 60 is right?",
            ("स + इन्धनम्", "अ + इ → ए: स + इन्धनम् → सेन्धनम् (printed सेंधनं)."),
            [("स + एन्धनम्", "एन्धनम् is not a word, and अ + ए would give ऐ."),
             ("सः + इन्धनम्", "सः before a vowel loses its visarga and does not merge: स इन्धनम्."),
             ("सम् + धनम्", "सम् + धनम् gives संधनम्, with no ए.")],
            "स (with) + इन्धनम् (fuel): अ + इ → ए.",
            "अ + इ → ए."),
        mcq("apply", 4, "By card 60, which of these is the sign of line 2?",
            ("Flame with fuel dies out with no wind", "निवाते सेन्धनं ... ज्योतिः उपशाम्यति."),
            [("Flame without fuel dies out in wind", "Both are reversed: the flame has fuel and there is no wind."),
             ("Flame with fuel flares up with no wind", "The flame goes out (उपशाम्यति); it does not flare up."),
             ("Flame without fuel keeps burning in wind", "The flame has fuel, there is no wind, and it goes out.")],
            "Windless place + fuel present, yet the light goes out.",
            "निवाते सेन्धनं ज्योतिः उपशाम्यति."),
        mcq("transfer", 5, "By the pattern of स + इन्धनम् → सेन्धनम्, how is पूर्ण + इन्दुः (the full moon) joined in a new example?",
            ("पूर्णेन्दुः", "अ + इ → ए: पूर्ण + इन्दुः → पूर्णेन्दुः."),
            [("पूर्णैन्दुः", "ऐ comes from अ + ए or अ + ऐ, not from अ + इ."),
             ("पूर्णीन्दुः", "ई comes from इ + इ, not from अ + इ."),
             ("पूर्णयिन्दुः", "No य् is inserted; अ and इ merge into ए.")],
            "पूर्ण + इन्दुः = पूर्णेन्दुः, like स + इन्धनम् = सेन्धनम्.",
            "अ + इ → ए.",
            teaches="अ or आ before इ or ई gives ए: स + इन्धनम् → सेन्धनम्."),
    ],
}

# ---------------------------------------------------------------- unit 61
AUTHORED["61"] = {
    "title": "आतुरस्य गृहे यस्य",
    "question": "By card 61, what happening in the patient's house does the verse name, and what does it say of him?",
    "rule": ("The patient in whose house (गृहे) vessels (अमत्राणि) break or fall (भिद्यन्ते वा पतन्ति च) excessively "
             "(अतिमात्रम्): his life is hard to obtain (दुर्लभं तस्य जीवितम्)."),
    "limits": ("Medium confidence. The verbs stand in line 1 and their subject अमत्राणि in line 2 (data). अमत्र = a large "
               "vessel or pot (standard). Nothing is said of why the vessels break, or of anything to be done."),
    "explain_hi": ("जिस रोगी के घर में अमत्र (पात्र, बड़े बर्तन; मानक) अत्यधिक फूटते हैं या गिरते हैं, उसका जीवन दुर्लभ है। "
                   "क्रियाएँ (भिद्यन्ते, पतन्ति) पहली पंक्ति में हैं, उनका कर्ता ‘अमत्राणि’ दूसरी पंक्ति में। "
                   "‘यस्य’ ‘आतुरस्य’ से जुड़ता है: जिस रोगी के घर में; ‘तस्य’ बाद में उसी को उठाता है। "
                   "‘भिद्यन्ते’ √भिद् का कर्मवाच्य वर्तमान है (टूटते हैं); ‘अतिमात्रममत्राणि’ में म् स्वर से जुड़ा है।"),
    "hook": "रोगी के घर में बर्तन बहुत फूटें या गिरें: दुर्लभं तस्य जीवितम्।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "In card 61, what does अमत्र mean?",
            ("A vessel, pot", "अमत्र = a large vessel or pot (standard)."),
            [("A lamp, light", "A lamp would be दीप; अमत्र = vessel."),
             ("A bed, cot", "A bed is शय्या (card 54); अमत्र = vessel."),
             ("A door, gate", "A door would be द्वार; अमत्र = vessel.")],
            "अमत्र = vessel, pot.",
            "अमत्र = vessel."),
        order(1, "Put the parts of card 61 in the printed order.",
              ["आतुरस्य", "गृहे यस्य", "भिद्यंते वा", "पतंति च", "अतिमात्रममत्राणि", "दुर्लभं तस्य जीवितं"],
              "Of the patient; in whose house; break or; fall and; excessively the vessels; his life is hard to obtain.",
              "आतुरस्य → गृहे यस्य → भिद्यंते वा → पतंति च → अतिमात्रममत्राणि → दुर्लभं तस्य जीवितं."),
        match(2, "Match each word of card 61 to its meaning.",
              [["आतुरस्य", "of the patient"], ["गृहे", "in the house"], ["भिद्यन्ते", "break, are broken"],
               ["पतन्ति", "fall"], ["अतिमात्रम्", "excessively"], ["दुर्लभम्", "hard to obtain"]],
              "आतुरस्य = of the patient, गृहे = in the house, भिद्यन्ते = are broken, पतन्ति = fall, अतिमात्रम् = excessively, दुर्लभम् = hard to obtain.",
              "आतुरस्य, गृहे, भिद्यन्ते, पतन्ति, अतिमात्रम्, दुर्लभम्.", role="extend",
              teaches="यस्य agrees with आतुरस्य (of the patient in whose house); तस्य (his) later picks up the same person."),
        mcq("discriminate", 3, "Is भिद्यन्ते in card 61 a passive form?",
            ("Yes: passive present, 'are broken'", "√भिद् has the active भिनत्ति; its -य- here marks the passive (data: pres. pass.)."),
            [("Yes: but future, 'will be broken'", "A future would have -स्य-; भिद्यन्ते is present."),
             ("No: active present, 'they break (it)'", "The active present of √भिद् is भिन्दन्ति, not भिद्यन्ते."),
             ("No: optative, 'they should break'", "An optative would end in -एरन् or -एयुः; भिद्यन्ते is present.")],
            "भिद्यन्ते = are broken (passive present, third person plural).",
            "-य- in भिद्यन्ते marks the passive, since √भिद् has no -य- in its active."),
        mcq("apply", 4, "Why is अतिमात्रम् printed joined to अमत्राणि in card 61 (अतिमात्रममत्राणि)?",
            ("म् joins a following vowel", "Before a vowel, final म् stays म् and joins it: अतिमात्रममत्राणि."),
            [("म् before a vowel becomes ं", "ं replaces म् only before a consonant (दुर्लभं तस्य, same card)."),
             ("म् drops before अ", "It does not drop: the print has मम."),
             ("म् before अ becomes न्", "म् does not change to न् here: the print has मम.")],
            "अतिमात्रम् + अमत्राणि → अतिमात्रममत्राणि.",
            "Final म् + vowel → joined."),
        mcq("transfer", 5, "By the pattern of भिद्यन्ते (are broken, passive of √भिद्), what does छिद्यन्ते (√छिद्) mean in a new example?",
            ("They are cut", "√छिद् has the active छिनत्ति; छिद्यन्ते is its passive present: they are cut."),
            [("They cut things", "They cut (active) would be छिन्दन्ति."),
             ("They will cut", "They will cut would be छेत्स्यन्ति."),
             ("Having cut", "Having cut would be छित्त्वा.")],
            "छिद्यन्ते = they are cut, like भिद्यन्ते = they are broken.",
            "Root + -य- + -न्ते (for a root with no -य- in its active) = passive present.",
            teaches="For roots like √भिद् whose active has no -य-, the passive present adds -य- with -ते/-न्ते: भिद्यन्ते = are broken."),
    ],
}

# ---------------------------------------------------------------- unit 62
AUTHORED["62"] = {
    "title": "यं नरं सहसा रोगो",
    "question": "By card 62, what does Ātreya say of the weak man whom a disease suddenly leaves?",
    "rule": ("The weak man (दुर्बलं नरम्) whom a disease (रोगः) suddenly (सहसा) leaves (परिमुञ्चति): Ātreya (आत्रेयः) "
             "considers (मन्यते) his life to have reached doubt (संशयं प्राप्तम्)."),
    "limits": ("High confidence. 'Leaves' is the text's word; nothing is added about recovery or about what follows. आत्रेय "
               "is kept as a name, with no role added. The text gives this as Ātreya's view (मन्यते)."),
    "explain_hi": ("जिस दुर्बल मनुष्य को रोग अचानक छोड़ देता है (परिमुञ्चति), आत्रेय उसके जीवन को संशय को प्राप्त हुआ मानते हैं। "
                   "‘छोड़ देता है’ पाठ का अपना शब्द है; स्वस्थ होने के बारे में कुछ नहीं जोड़ा गया। "
                   "आत्रेय केवल नाम के रूप में रखा गया है। "
                   "‘मन्यते’ √मन् का आत्मनेपद वर्तमान है (मानते हैं), कर्मवाच्य नहीं: -यते होने से रूप कर्मवाच्य नहीं हो जाता। "
                   "सन्धियाँ: रोगः + दुर्बलम् → रोगो दुर्बलम् (अः + घोष व्यंजन → ओ), प्राप्तम् + आत्रेयः → प्राप्तमात्रेयः।"),
    "hook": "दुर्बल को रोग अचानक छोड़ दे: आत्रेय उसके जीवन को संशय में मानते हैं।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "In card 62, what does संशय mean?",
            ("Doubt", "संशय = doubt, uncertainty: संशयं प्राप्तम्, reached doubt."),
            [("Rest", "Rest would be विश्राम; संशय = doubt."),
             ("Certainty", "Certainty would be निश्चय, the opposite of संशय."),
             ("Healing", "Healing would be from √रुह् or शम; संशय = doubt.")],
            "संशय = doubt.",
            "संशय = doubt."),
        match(1, "Match each word of card 62 to its meaning.",
              [["नरम्", "man"], ["रोगः", "disease"], ["दुर्बलम्", "weak"], ["परिमुञ्चति", "leaves"], ["संशयम्", "doubt"],
               ["मन्यते", "considers"]],
              "नरम् = man, रोगः = disease, दुर्बलम् = weak, परिमुञ्चति = leaves, संशयम् = doubt, मन्यते = considers.",
              "नरम्, रोगः, दुर्बलम्, परिमुञ्चति, संशयम्, मन्यते."),
        order(2, "Put the words of line 2 of card 62 in the printed order.",
              ["संशयं", "प्राप्तम्", "आत्रेयः", "जीवितं", "तस्य", "मन्यते"],
              "Doubt; reached; Ātreya; the life; his; considers.",
              "संशयं → प्राप्तम् → आत्रेयः → जीवितं → तस्य → मन्यते.",
              role="extend",
              teaches="मन्यते takes the object जीवितम् with a predicate (संशयं प्राप्तम्): he considers the life as having reached doubt."),
        mcq("discriminate", 3, "Is मन्यते in card 62 a passive form?",
            ("No: ātmanepada present, 'considers'", "√मन् takes -य- in its own ātmanepada present: मन्यते = he considers."),
            [("No: but future, 'will consider'", "A future would be मंस्यते; मन्यते is present."),
             ("Yes: passive present, 'is considered'", "Not here: आत्रेयः is the subject who considers; -यते is not always passive."),
             ("Yes: optative, 'should be considered'", "An optative would be मन्येत; मन्यते is present.")],
            "मन्यते = considers (ātmanepada present, third person singular).",
            "-यते is not always passive: मन्यते, जायते."),
        mcq("apply", 4, "Which split of प्राप्तमात्रेयो in card 62 is right?",
            ("प्राप्तम् + आत्रेयः", "म् joins a following vowel: प्राप्तम् + आत्रेयः → प्राप्तमात्रेयः."),
            [("प्राप्तम् + अत्रेयः", "That would print प्राप्तमत्रेयो, without the आ."),
             ("प्राप्तः + आत्रेयः", "अः before आ gives अ with a gap: प्राप्त आत्रेयः."),
             ("प्राप्तौ + आत्रेयः", "औ before a vowel gives आव्: प्राप्तावात्रेयः.")],
            "प्राप्तम् (reached) + आत्रेयः (Ātreya).",
            "Final म् + vowel → joined."),
        mcq("transfer", 5, "By the pattern of रोगः + दुर्बलम् → रोगो दुर्बलम्, how is बालः + वदति (the boy speaks) written in a new example?",
            ("बालो वदति", "अः before the voiced व → ओ: बालो वदति."),
            [("बाला वदति", "आ would come from आः losing its visarga; here the ending is अः."),
             ("बालर्वदति", "र् comes from a visarga after vowels other than अ/आ."),
             ("बाल वदति", "Only सः and एषः drop their visarga before a consonant.")],
            "बालः + वदति = बालो वदति, like रोगः + दुर्बलम् = रोगो दुर्बलम्.",
            "अः + voiced consonant → ओ.",
            teaches="अः before a voiced consonant becomes ओ: रोगः + दुर्बलम् → रोगो दुर्बलम्."),
    ],
}

# ---------------------------------------------------------------- unit 63
AUTHORED["63"] = {
    "title": "इति विकृतव्याधिविज्ञानीयो",
    "question": "What does the colophon of card 63 state?",
    "rule": ("Thus (इति) the eleventh (एकादशः) chapter (अध्यायः), named (नाम) Vikṛtavyādhivijñānīya: the chapter title "
             "announced in card 1."),
    "limits": ("Prose colophon, high confidence. The name is kept in Sanskrit; its parts mean roughly 'to be understood about "
               "abnormal (altered) diseases' (data). No verb is printed."),
    "explain_hi": ("यह गद्य समापन-वाक्य (colophon) है: इस प्रकार विकृतव्याधिविज्ञानीय नामक ग्यारहवाँ अध्याय। "
                   "यही नाम कार्ड १ में अध्याय के आरम्भ में आया था। "
                   "नाम के भाग मोटे तौर पर ‘विकृत (असामान्य) रोगों के विषय में जानने योग्य’ हैं; नाम संस्कृत में ही रखा गया। "
                   "सन्धियाँ: नाम + एकादशः → नामैकादशः (अ + ए → ऐ), एकादशः + अध्यायः → एकादशोऽध्यायः (अः + अ → ओऽ)।"),
    "hook": "इति विकृतव्याधिविज्ञानीयो नामैकादशोऽध्यायः: ग्यारहवाँ अध्याय पूरा।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "In card 63, what does एकादशः mean?",
            ("Eleventh", "एकादश = eleven; एकादशः अध्यायः = the eleventh chapter."),
            [("Twelfth", "Twelfth would be द्वादशः; एकादशः = eleventh."),
             ("Thirteenth", "Thirteenth would be त्रयोदशः; एकादशः = eleventh."),
             ("Fifteenth", "Fifteenth would be पञ्चदशः; एकादशः = eleventh.")],
            "एकादशः = eleventh.",
            "एकादशः = eleventh."),
        order(1, "Put the words of card 63 in the printed order.",
              ["इति", "विकृतव्याधिविज्ञानीयः", "नाम", "एकादशः", "अध्यायः"],
              "Thus; Vikṛtavyādhivijñānīya; named; eleventh; chapter.",
              "इति → विकृतव्याधिविज्ञानीयः → नाम → एकादशः → अध्यायः."),
        match(2, "Match each word of card 63 to its meaning.",
              [["इति", "thus"], ["नाम", "named, by name"], ["एकादशः", "eleventh"], ["अध्यायः", "chapter"],
               ["विकृत", "altered, abnormal"], ["व्याधि", "disease"]],
              "इति = thus, नाम = by name, एकादशः = eleventh, अध्यायः = chapter, विकृत = altered, व्याधि = disease.",
              "इति, नाम, एकादशः, अध्यायः, विकृत, व्याधि.", role="extend",
              teaches="The chapter name is a tatpuruṣa, विकृत-व्याधि-विज्ञानीय: roughly 'to be understood about abnormal (altered) diseases' (data)."),
        mcq("discriminate", 3, "Which split of नामैकादशो in card 63 is right?",
            ("नाम + एकादशः", "अ + ए → ऐ: नाम + एकादशः → नामैकादशः."),
            [("नाम + इकादशः", "अ + इ → ए: that would print नामेकादश-."),
             ("नामः + एकादशः", "अः before ए gives अ with a gap: नाम एकादशः."),
             ("नामे + एकादशः", "A final ए before ए does not give ऐ; the print would differ.")],
            "नाम (by name) + एकादशः (eleventh): अ + ए → ऐ.",
            "अ + ए → ऐ."),
        mcq("apply", 4, "Why is एकादशः printed एकादशोऽ before अध्यायः in card 63?",
            ("अः + अ → ओ, and the अ drops", "Before अ, the अः gives ओ and the next अ drops, marked ऽ: एकादशोऽध्यायः."),
            [("अः + any vowel → ओ, with ऽ", "Not any: before other vowels अः gives अ with a gap (रामः + एव → राम एव)."),
             ("आः + अ → ओ, and the अ drops", "The ending is अः, and आः only loses its visarga before a voiced sound."),
             ("ओ is the ordinal's own ending", "The ordinal ends in -अः; ओ comes only from sandhi.")],
            "एकादशः + अध्यायः → एकादशोऽध्यायः.",
            "अः + अ → ओऽ."),
        mcq("transfer", 5, "By the pattern of नाम + एकादशः → नामैकादशः, how is पुत्र + एषणा (desire for a son) joined in a new example?",
            ("पुत्रैषणा", "अ + ए → ऐ: पुत्र + एषणा → पुत्रैषणा."),
            [("पुत्रेषणा", "ए comes from अ + इ, not from अ + ए."),
             ("पुत्रौषणा", "औ comes from अ + ओ or अ + औ, not from अ + ए."),
             ("पुत्रयेषणा", "No य् is inserted; अ and ए merge into ऐ.")],
            "पुत्र + एषणा = पुत्रैषणा, like नाम + एकादशः = नामैकादशः.",
            "अ + ए → ऐ.",
            teaches="अ or आ before ए or ऐ gives ऐ: नाम + एकादशः → नामैकादशः."),
    ],
}


# ================================================================ NOTES_HI
NOTES_HI = {
    "51": ("पद्य; विश्वास मध्यम; दो छपी पंक्तियाँ (०२.११.९८ और ०२.११.९९) जोड़ी गईं। पाठ-चिह्न (सम्भव): छपा ‘सर्वास्तान्’; सर्वान् + तान् नियमित सन्धि से "
           "‘सर्वांस्तान्’ देता, अनुस्वार छूटा हो सकता है; इस पर प्रश्न नहीं। ‘रूपम्’ की क्रिया ‘दृश्यते’ कार्ड ५० (छपी पंक्ति ९७) से आती है। "
           "‘शक्ति’ = भाला लिया गया, ‘बल’ भी सम्भव। डेटा के अनुसार दूसरी पंक्ति पहली को आगे ले जाती है; ‘भगन्दरम्’ ‘वर्जयेत्’ का कर्म है। "
           "सन्धि जाँची: वर्जयेत् + व्रणान् → वर्जयेद्व्रणान् (घोष व से पहले त् → द्); विट् + मूत्र → विण्मूत्र (नासिक्य म से पहले ट् → ण्, विकल्प से)।"),
    "52": ("पद्य; विश्वास मध्यम; दो छपी पंक्तियाँ (०२.११.१०० और ०२.११.१०१)। पाठ-चिह्न (सम्भव): छपा ‘वक्रम्’ (टेढ़ा) ‘अपास्यति’ के साथ अर्थ नहीं देता; "
           "‘वक्त्रम्’ (मुख) अनुमानित पाठ है (क्त/क की भूल); इस पर प्रश्न नहीं। डेटा के अनुसार दोनों पंक्तियाँ एक वाक्य हैं। "
           "छपा ‘घट्टयन्जानुना’: नियमित सन्धि में न् + ज → ञ्ज होता, छपाई न् रखती है; इस पर प्रश्न नहीं। ‘सजीवति’ = स जीवति, एक खण्ड में छपा। "
           "सन्धि जाँची: पादौ + उद्यम्य → पादावुद्यम्य (औ + स्वर → आव्); यः + अपास्यति → योऽपास्यति (अः + अ → ओऽ); आतुरः + न → आतुरो न।"),
    "53": ("पद्य; विश्वास उच्च; दो छपी पंक्तियाँ (०२.११.१०२ और ०२.११.१०३); कोई पाठ-चिह्न नहीं। डेटा के अनुसार छपी पंक्ति १०१ (कार्ड ५२) पूरा वाक्य है; "
           "छपी पंक्तियाँ १०२-१०६ (कार्ड ५३, ५४ और ५५ की पहली पंक्ति) सम्भवतः दूसरा वाक्य हैं, पर सीमाएँ पक्की नहीं। ‘तैः’ = उन्हीं (दाँतों) से लिया गया। "
           "सन्धि जाँची: दन्तैः + छिन्दन् → दन्तैश्छिन्दन् (छ से पहले ः → श्); छिन्दन् + नखाग्राणि → छिन्दन्नखाग्राणि; "
           "केशान् + तृणानि → केशांस्तृणानि (त से पहले न् → ंस्, या ँस्); तैः + च → तैश्च।"),
    "54": ("पद्य; विश्वास मध्यम; दो छपी पंक्तियाँ (०२.११.१०४ और ०२.११.१०५)। पाठ-चिह्न (सम्भव): छपा ‘दृष्टलोमा’ अर्थ नहीं देता; ‘हृष्टलोमा’ (खड़े रोम) "
           "मानक शब्द है, दृ/हृ की भूल सम्भव; अनुमानित पाठ, इस पर प्रश्न नहीं। ‘क्ष्वेडन्’ दुर्लभ धातु है (गुनगुनाना, बड़बड़ाना या गर्जना), अर्थ पक्का नहीं; प्रश्न नहीं। "
           "डेटा के अनुसार दोनों ‘यः’ उपवाक्य कार्ड ५५ में आगे चलते हैं। छपा ‘हंति’ = हन्ति (अनुस्वार)। "
           "सन्धि जाँची: मुहुः + हसन् → मुहुर्हसन् (उ के बाद विसर्ग, घोष ह से पहले → र्); मुहुः क्ष्वेडन् में ः बना रहा।"),
    "55": ("पद्य; विश्वास मध्यम; दो छपी पंक्तियाँ (०२.११.१०६ और ०२.११.१०७); कोई पाठ-चिह्न नहीं। डेटा: पहली पंक्ति कार्ड ५३ (या ५४) से चला वाक्य पूरा करती है; "
           "दूसरी पंक्ति कार्ड ५६ के ‘परिवर्जयेत्’ का कर्म है। ‘छिद्र’ = छेद या द्वार; कौन-से, नहीं कहा। ‘विमृश्’ का अर्थ ‘विचार करना’ भी हो सकता है; ‘छूना’ लिया गया, "
           "पुनः जाँच योग्य। ऊर्ध्वश्वास = सम्भवतः कष्टपूर्ण श्वास (सम्भावित)। "
           "सन्धि जाँची: मुहुः + छिद्राणि → मुहुश्छिद्राणि (छ से पहले ः → श्); विमृशन् + आतुरः → विमृशन्नातुरः (ह्रस्व स्वर के बाद अन्तिम न् स्वर से पहले द्वित्व); "
           "गत + ऊष्माणम् → गतोष्माणम् (अ + ऊ → ओ); शूल + उपहत → शूलोपहत (अ + उ → ओ)।"),
    "56": ("पद्य; विश्वास उच्च; दो छपी पंक्तियाँ (०२.११.१०८ और ०२.११.१०९); कोई पाठ-चिह्न नहीं। डेटा: पहली पंक्ति कार्ड ५५ को पूरा करती है; दूसरी कार्ड ५७ में आगे चलती है। "
           "छपा ‘वर्द्धंते’ में द्द छपाई की आदत है (= वर्धन्ते)। ‘परिहीयते’ कर्मवाच्य वर्तमान (डेटा)। "
           "सन्धि जाँची: च + अनधिगच्छन्तम् → चानधिगच्छन्तम् (अ + अ → आ); विकाराः + यस्य → विकारा यस्य (आ के बाद विसर्ग, घोष य से पहले लुप्त)।"),
    "57": ("पद्य; विश्वास मध्यम; दो छपी पंक्तियाँ (०२.११.११० और ०२.११.१११); कोई पाठ-चिह्न नहीं। ‘सहसा’ दो बार छपा (ज़ोर के लिए), जैसा छपा वैसा रखा। "
           "‘हरतिजीवितं’ बिना रिक्त स्थान के छपा। डेटा: दूसरी पंक्ति का वाक्य कार्ड ५८ (यतमानो न शक्नोति) में पूरा होता है, वहाँ वैद्य कर्ता है। "
           "सन्धि जाँची: मृत्युः + हरति → मृत्युर्हरति (उ के बाद विसर्ग, घोष ह से पहले → र्); यम् + उद्दिश्य → यमुद्दिश्य; उद्दिश्य + आतुरम् → उद्दिश्यातुरम् (अ + आ → आ); "
           "संपादयितुम् + औषधम् → संपादयितुमौषधम्।"),
    "58": ("पद्य; विश्वास मध्यम; दो छपी पंक्तियाँ (०२.११.११२ और ०२.११.११३); कोई पाठ-चिह्न नहीं। डेटा: पहली पंक्ति कार्ड ५७ का वाक्य पूरा करती है; "
           "दूसरी पंक्ति की संज्ञा (औषधम्) कार्ड ५९ में है। ‘सिद्ध’ = सफल (यहाँ ‘पका हुआ’ नहीं); ‘अवचारित’ = प्रयुक्त (शब्द खुला)। "
           "सन्धि जाँची: यतमानः + न → यतमानो न (अः + घोष व्यंजन → ओ); दुर्लभम् + तस्य → दुर्लभं तस्य; विधिवत् + च → विधिवच्च (च से पहले त् → च्); "
           "च + अवचारितम् → चावचारितम् (अ + अ → आ)।"),
    "59": ("पद्य; विश्वास मध्यम; दो छपी पंक्तियाँ (०२.११.११४ और ०२.११.११५); कोई पाठ-चिह्न नहीं। डेटा: कार्ड ५८ की दूसरी पंक्ति इसी औषध का वर्णन है; "
           "‘विपर्यय’ तैयारी का उलटना है या प्रभाव का, यह खुला है; प्रश्न नहीं। ‘कल्प्यमाने’ दोनों संज्ञाओं के साथ सति सप्तमी लिया गया। दूसरी पंक्ति कार्ड ६० में आगे चलती है। "
           "सन्धि जाँची: सिद्ध्यति + औषधम् → सिद्ध्यत्यौषधम् (इ + औ → यौ); न + अस्ति → नास्ति; भवेत् + यस्य → भवेद्यस्य (घोष य से पहले त् → द्); "
           "यस्य + औषधे → यस्यौषधे (अ + औ → औ); औषधे + अन्ने → औषधेऽन्ने (ए + अ → एऽ)।"),
    "60": ("गद्य (डेटा का प्रकार); विश्वास कम; दो छपी पंक्तियाँ (०२.११.११६ और ०२.११.११७)। पाठ-चिह्न (सम्भव): छपा ‘अकस्माद्वर्णवादेःस्वस्थोऽपि’ में ‘वर्णवादेः’ का अन्वय नहीं बनता; "
           "‘वर्णादेः’ (रंग आदि से) अनुमानित पाठ है, अतिरिक्त ‘व’ OCR की पुनरावृत्ति हो सकता है, और ‘स्वस्थो’ से पहले रिक्त स्थान नहीं छपा; दूसरा संशोधन भी सम्भव। "
           "अर्थ पक्का नहीं, इसलिए पहली पंक्ति पर कोई प्रश्न नहीं। डेटा: पहली पंक्ति सम्भवतः कार्ड ५९ को आगे ले जाती है; दूसरी पंक्ति अलग लक्षण है। "
           "ज्योतिः = प्रकाश या लौ (दीपक या अग्नि, नहीं बताया); ‘च अपि’ = भी। "
           "सन्धि जाँची: स + इन्धनम् → सेन्धनम् (अ + इ → ए); ज्योतिः + च → ज्योतिश्च; च + अपि → चापि; अपि + उपशाम्यति → अप्युपशाम्यति (इ + उ → यु)।"),
    "61": ("पद्य; विश्वास मध्यम; दो छपी पंक्तियाँ (०२.११.११८ और ०२.११.११९); कोई पाठ-चिह्न नहीं। डेटा: कर्ता ‘अमत्राणि’ दूसरी पंक्ति में है, क्रियाएँ पहली में; "
           "‘यस्य’ ‘आतुरस्य’ से अन्वित। अमत्र = बड़ा पात्र या घड़ा (मानक)। छपे ‘भिद्यंते’, ‘पतंति’ = भिद्यन्ते, पतन्ति (अनुस्वार)। "
           "सन्धि जाँची: अतिमात्रम् + अमत्राणि → अतिमात्रममत्राणि (म् स्वर से जुड़ता है); दुर्लभम् + तस्य → दुर्लभं तस्य।"),
    "62": ("पद्य; विश्वास उच्च; दो छपी पंक्तियाँ (०२.११.१२० और ०२.११.१२१); कोई पाठ-चिह्न नहीं। ‘परिमुञ्चति’ = छोड़ देता है; स्वस्थ होने के बारे में कुछ नहीं जोड़ा। "
           "‘आत्रेय’ नाम के रूप में रखा, कोई भूमिका नहीं जोड़ी। ‘मन्यते’ आत्मनेपद वर्तमान (डेटा)। छपा ‘परिमुंचति’ = परिमुञ्चति। "
           "सन्धि जाँची: रोगः + दुर्बलम् → रोगो दुर्बलम् (अः + घोष व्यंजन → ओ); प्राप्तम् + आत्रेयः → प्राप्तमात्रेयः; आत्रेयः + जीवितम् → आत्रेयो जीवितम्।"),
    "63": ("गद्य; विश्वास उच्च; एक छपी पंक्ति (०२.११.१२२); कोई पाठ-चिह्न नहीं। अध्याय का समापन-वाक्य; नाम संस्कृत में रखा गया, हिन्दी में नाम के रूप में दिया गया। "
           "सन्धि जाँची: विज्ञानीयः + नाम → विज्ञानीयो नाम (अः + घोष व्यंजन → ओ); नाम + एकादशः → नामैकादशः (अ + ए → ऐ); एकादशः + अध्यायः → एकादशोऽध्यायः (अः + अ → ओऽ)।"),
}


# ================================================================ AIDS
AIDS = {
    "51": {
        "diagram": {"groups": [
            {"label": "पंक्ति १: व्रण", "items": ["शक्ति (भाला), ध्वज आदि का रूप", "उन सब व्रणों को: वर्जयेत्"]},
            {"label": "पंक्ति २: भगन्दर", "items": ["मल, मूत्र, वायु बहाने वाला", "कृमियों वाला"]}]},
        "chunks": "रूपं शक्तिध्वजादीनां | सर्वास्तान् वर्जयेद्व्रणान् || विण्मूत्रमारुतवहं | कृमिणं च भगंदरं",
        "sandhi": ("घोष व से पहले त् → द्: वर्जयेत् + व्रणान् → वर्जयेद्व्रणान् · छपा ‘सर्वास्तान्’: नियमित सन्धि से ‘सर्वांस्तान्’ होता "
                   "(सम्भव पाठ-चिह्न), इस पर प्रश्न नहीं।"),
        "anchors": "कृमि + इन् = कृमिन् (कृमियों वाला), जैसे ज्वर + इन् = ज्वरिन्। (मेरी याद-पद्धति)",
    },
    "52": {
        "chain": {"steps": ["घट्टयन्जानुना जानु = घुटने से घुटना टकराए", "पादावुद्यम्य पातयन् = पैर उठाकर गिराए",
                            "योऽपास्यति मुहुः = बार-बार हटाए (मुख: अनुमानित पाठ)", "आतुरो न सजीवति = वह रोगी जीवित नहीं रहता"]},
        "chunks": "घट्टयन्जानुना जानु | पादावुद्यम्य पातयन् || योऽपास्यति | मुहुर्वक्रमातुरो | न सजीवति",
        "sandhi": "औ + स्वर → आव्: पादौ + उद्यम्य → पादावुद्यम्य · अः + अ → ओऽ: यः + अपास्यति → योऽपास्यति · अः + घोष व्यंजन → ओ: आतुरः + न → आतुरो न।",
    },
    "53": {
        "diagram": {"groups": [
            {"label": "क्रियाएँ (छपे क्रम में)",
             "items": ["१ दाँतों से नखों के अग्र काटे", "२ उन्हीं से केश या तिनके", "३ लकड़ी से भूमि कुरेदे", "४ ढेले से ढेला मारे"]}]},
        "chunks": "दंतैश्छिन्दन्नखाग्राणि | तैश्च केशांस्तृणानि वा || भूमिं काष्ठेन विलिखन् | लोष्टं लोष्टेन ताडयन्",
        "sandhi": ("छ से पहले ः → श्: दन्तैः + छिन्दन् → दन्तैश्छिन्दन् · त से पहले न् → ंस् (या ँस्): केशान् + तृणानि → केशांस्तृणानि · "
                   "च से पहले ः → श्: तैः + च → तैश्च।"),
        "pegs": "साधन तृतीया में: दाँतों से (दन्तैः), लकड़ी से (काष्ठेन), ढेले से (लोष्टेन)। (मेरा बनाया स्मरण-सूत्र)",
    },
    "54": {
        "frame": ("पहला ‘यः’: सान्द्रमूत्रः (गाढ़ा मूत्र), शुष्ककासी (सूखी खाँसी), ज्वरी (ज्वर); अनुमानित पाठ पर खड़े रोम → "
                  "दूसरा ‘यः’: मुहुर्हसन् (बार-बार हँसे), मुहुः क्ष्वेडन् (अर्थ पक्का नहीं), शय्यां पादेन हन्ति (पैर से शय्या पर मारे) → मुख्य वाक्य: कार्ड ५५ में।"),
        "chunks": "दृष्टलोमा | सांद्रमूत्रः | शुष्ककासी | ज्वरी च यः || मुहुर्हसन्मुहुः क्ष्वेडन् | शय्यां पादेन हंति यः",
        "sandhi": "उ के बाद विसर्ग, घोष ह से पहले → र्: मुहुः + हसन् → मुहुर्हसन् · क्ष से पहले छपाई ः रखती है: मुहुः क्ष्वेडन्।",
    },
    "55": {
        "diagram": {"groups": [
            {"label": "कार्ड ५३-५५: सम्भवतः एक वाक्य (सीमाएँ पक्की नहीं)",
             "items": ["५३: दाँत से नख काटे, भूमि कुरेदे, ढेला मारे", "५४: गाढ़ा मूत्र, सूखी खाँसी, ज्वर",
                       "५४: बार-बार हँसे, शय्या पर पैर मारे", "५५: बार-बार छिद्र छूए", "५५: मुख्य वाक्य: न स जीवति"]}]},
        "chunks": "मुहुश्छिद्राणि | विमृशन्नातुरो | न स जीवति || ऊर्ध्वश्वासं | गतोष्माणं | शूलोपहतवंक्षणं",
        "sandhi": ("छ से पहले ः → श्: मुहुः + छिद्राणि → मुहुश्छिद्राणि · ह्रस्व स्वर के बाद अन्तिम न् स्वर से पहले दुगना: विमृशन् + आतुरः → विमृशन्नातुरः · "
                   "अ + ऊ → ओ: गत + ऊष्माणम् → गतोष्माणम् · अ + उ → ओ: शूल + उपहत → शूलोपहत।"),
    },
    "56": {
        "seesaw": "विकाराः वर्धन्ते (विकार बढ़ते हैं) ⇄ प्रकृतिः परिहीयते (स्वाभाविक अवस्था घटती है): दोनों इसी इकाई की दूसरी पंक्ति में।",
        "chunks": "शर्म चानधिगच्छंतं | बुद्धिमान्परिवर्जयेत् || विकारा यस्य वर्द्धंते | प्रकृतिः परिहीयते",
        "sandhi": "अ + अ → आ: च + अनधिगच्छन्तम् → चानधिगच्छन्तम् · आ के बाद विसर्ग, घोष य से पहले लुप्त: विकाराः + यस्य → विकारा यस्य।",
    },
    "57": {
        "frame": ("पंक्ति १ (कार्ड ५६ का वाक्य पूरा): सहसा सहसा → तस्य जीवितम् → मृत्युः हरति · "
                  "पंक्ति २ (नया वाक्य): यम् आतुरम् उद्दिश्य → वैद्यः → औषधं संपादयितुम् → आगे कार्ड ५८।"),
        "chunks": "सहसा सहसा | तस्य | मृत्युर्हरतिजीवितं || यमुद्दिश्यातुरं | वैद्यः | संपादयितुमौषधं",
        "sandhi": "उ के बाद विसर्ग, घोष ह से पहले → र्: मृत्युः + हरति → मृत्युर्हरति · म् + स्वर → जुड़ता है: यम् + उद्दिश्य → यमुद्दिश्य · अ + आ → आ: उद्दिश्य + आतुरम् → उद्दिश्यातुरम्।",
    },
    "58": {
        "chain": {"steps": ["कार्ड ५७: जिस रोगी को लक्ष्य करके", "कार्ड ५७: वैद्य औषध तैयार करने को", "कार्ड ५८: यत्न करता हुआ",
                            "कार्ड ५८: समर्थ नहीं होता", "कार्ड ५८: उसका जीवन दुर्लभ"]},
        "chunks": "यतमानो न शक्नोति | दुर्लभं तस्य जीवितं || विज्ञातं | बहुशः सिद्धं | विधिवच्चावचारितं",
        "sandhi": "अः + घोष व्यंजन → ओ: यतमानः + न → यतमानो न · च से पहले त् → च्: विधिवत् + च → विधिवच्च · अ + अ → आ: च + अवचारितम् → चावचारितम्।",
    },
    "59": {
        "frame": "किसका: यस्य → क्या न हो: औषधं न सिद्ध्यति → फल: नास्ति तस्य चिकित्सितम् · फिर: औषध या अन्न बनाते समय → विपर्ययः (उलटा परिणाम; किसका, खुला) → आगे कार्ड ६०।",
        "chunks": "न सिद्ध्यत्यौषधं यस्य | नास्ति तस्य चिकित्सितं || भवेद्यस्यौषधेऽन्ने वा | कल्प्यमाने विपर्ययः",
        "sandhi": "इ + औ → यौ: सिद्ध्यति + औषधम् → सिद्ध्यत्यौषधम् · अ + अ → आ: न + अस्ति → नास्ति · घोष य से पहले त् → द्: भवेत् + यस्य → भवेद्यस्य · ए + अ → एऽ: औषधे + अन्ने → औषधेऽन्ने।",
    },
    "60": {
        "chain": {"steps": ["निवाते: हवा नहीं", "सेन्धनम्: ईंधन है", "फिर भी: ज्योतिः उपशाम्यति", "ज्योति बुझ जाती है"]},
        "chunks": "अकस्माद्वर्णवादेःस्वस्थोऽपि | न स जीवति || निवाते सेंधनं यस्य | ज्योतिश्चाप्युपशाम्यति",
        "sandhi": "अ + इ → ए: स + इन्धनम् → सेन्धनम् · च से पहले ः → श्: ज्योतिः + च → ज्योतिश्च · अ + अ → आ: च + अपि → चापि · इ + उ → यु: अपि + उपशाम्यति → अप्युपशाम्यति।",
    },
    "61": {
        "frame": "कहाँ: आतुरस्य गृहे यस्य (जिस रोगी के घर में) → क्या: अमत्राणि (पात्र) → कैसे: अतिमात्रम् भिद्यन्ते वा पतन्ति च → फल: दुर्लभं तस्य जीवितम्।",
        "chunks": "आतुरस्य गृहे यस्य | भिद्यंते वा पतंति च || अतिमात्रममत्राणि | दुर्लभं तस्य जीवितं",
        "sandhi": "म् + स्वर → जुड़ता है: अतिमात्रम् + अमत्राणि → अतिमात्रममत्राणि · व्यंजन से पहले म् → ं: दुर्लभम् + तस्य → दुर्लभं तस्य।",
    },
    "62": {
        "frame": "किसे: यं दुर्बलं नरम् → क्या हो: रोगः सहसा परिमुञ्चति (रोग अचानक छोड़ दे) → किसका मत: आत्रेयः मन्यते → क्या: तस्य जीवितं संशयं प्राप्तम्।",
        "chunks": "यं नरं सहसा | रोगो दुर्बलं परिमुंचति || संशयं प्राप्तमात्रेयो | जीवितं तस्य मन्यते",
        "sandhi": "अः + घोष व्यंजन → ओ: रोगः + दुर्बलम् → रोगो दुर्बलम्, आत्रेयः + जीवितम् → आत्रेयो जीवितम् · म् + स्वर → जुड़ता है: प्राप्तम् + आत्रेयः → प्राप्तमात्रेयः।",
        "anchors": "मन्यते: -यते होते हुए भी कर्तृवाच्य (आत्मनेपद); कर्ता आत्रेयः। (मेरी याद-पद्धति)",
    },
    "63": {
        "diagram": {"groups": [
            {"label": "समापन-वाक्य के भाग (छपे क्रम में)",
             "items": ["इति = इस प्रकार", "विकृत = बदला हुआ, असामान्य", "व्याधि = रोग", "विज्ञानीय = जानने योग्य",
                       "नाम = नामक", "एकादशः = ग्यारहवाँ", "अध्यायः = अध्याय"]}]},
        "chunks": "इति | विकृतव्याधिविज्ञानीयो | नामैकादशोऽध्यायः",
        "sandhi": "अ + ए → ऐ: नाम + एकादशः → नामैकादशः · अः + अ → ओऽ: एकादशः + अध्यायः → एकादशोऽध्यायः।",
    },
}


# ================================================================ IMAGE_SPECS
IMAGE_SPECS = {
    ("51", "diagram"): {
        "file": "sh11-varjya-vrana-51.svg",
        "alt": ("Split of card 51: line 1, wounds with the form of a spear, a banner and the like, all to be avoided; "
                "line 2, bhagandara passing faeces, urine and vāyu (māruta), and with worms."),
        "type": "split",
        "title": "कार्ड ५१: वर्जयेत्",
        "cols": [["पंक्ति १: व्रण", ["शक्ति (भाला), ध्वज आदि का रूप", "उन सब व्रणों को त्यागे"]],
                 ["पंक्ति २: भगन्दर", ["मल, मूत्र, वायु बहाए", "कृमियों वाला"]]],
    },
    ("53", "diagram"): {
        "file": "sh11-cheshta-53.svg",
        "alt": ("Table of card 53 in printed order: 1 cutting the nail-tips with the teeth, 2 with them hairs or grass, "
                "3 scratching the ground with wood, 4 striking a clod with a clod."),
        "type": "table",
        "title": "कार्ड ५३: क्रियाएँ",
        "heads": ["क्रम", "छपा शब्द: अर्थ"],
        "rows": [["१", "दंतैश्छिन्दन्नखाग्राणि: दाँत से नख-अग्र काटे"], ["२", "तैश्च केशांस्तृणानि वा: केश या तिनके"],
                 ["३", "भूमिं काष्ठेन विलिखन्: भूमि कुरेदे"], ["४", "लोष्टं लोष्टेन ताडयन्: ढेले से ढेला मारे"]],
    },
    ("55", "diagram"): {
        "file": "sh11-ekavakya-55.svg",
        "alt": ("Table of cards 53 to 55, which the data takes as probably one sentence (boundaries not firm): card 53 actions "
                "with teeth, wood and clods; card 54 thick urine, dry cough, fever, laughing, striking the bed; card 55 "
                "touching the openings, and the main clause na sa jīvati."),
        "type": "table",
        "title": "कार्ड ५३-५५: सम्भवतः एक वाक्य",
        "heads": ["कार्ड", "लक्षण"],
        "rows": [["५३", "दाँत से नख काटे, भूमि कुरेदे"], ["५३", "ढेले से ढेला मारे"], ["५४", "गाढ़ा मूत्र, सूखी खाँसी, ज्वर"],
                 ["५४", "बार-बार हँसे, शय्या पर पैर मारे"], ["५५", "बार-बार छिद्र छूए"], ["५५", "मुख्य वाक्य: न स जीवति"]],
    },
    ("56", "seesaw"): {
        "file": "sh11-vikara-prakriti-56.svg",
        "alt": "Split of card 56, line 2: the disorders (vikāra) increase, while the natural state (prakṛti) diminishes.",
        "type": "split",
        "title": "कार्ड ५६: विकार और प्रकृति",
        "cols": [["विकाराः", ["वर्धन्ते", "बढ़ते हैं"]], ["प्रकृतिः", ["परिहीयते", "घटती है"]]],
    },
    ("58", "chain"): {
        "file": "sh11-vaidya-58.svg",
        "alt": ("Chain across cards 57 and 58: the patient for whom a physician, to prepare medicine, striving, is not "
                "able; that patient's life is hard to obtain."),
        "type": "chain",
        "title": "कार्ड ५७-५८: एक वाक्य",
        "steps": ["५७: जिस रोगी को लक्ष्य करके", "५७: वैद्य औषध बनाने को", "५८: यत्न करता हुआ", "५८: समर्थ नहीं होता",
                  "५८: उसका जीवन दुर्लभ"],
    },
    ("60", "chain"): {
        "file": "sh11-jyoti-60.svg",
        "alt": ("Chain of card 60, line 2: in a windless place, with fuel present, yet the light or flame goes out. "
                "Line 1 (doubtful reading) is not shown."),
        "type": "chain",
        "title": "कार्ड ६०, पंक्ति २",
        "steps": ["निवाते: हवा नहीं", "सेन्धनम्: ईंधन है", "फिर भी: उपशाम्यति", "ज्योति बुझ जाती है"],
    },
    ("63", "diagram"): {
        "file": "sh11-samapti-63.svg",
        "alt": ("Table of the colophon of card 63 in printed order: iti thus, vikṛta altered, vyādhi disease, vijñānīya to be "
                "understood, nāma named, ekādaśa eleventh, adhyāya chapter."),
        "type": "table",
        "title": "कार्ड ६३: समापन-वाक्य",
        "heads": ["शब्द (छपे क्रम में)", "अर्थ"],
        "rows": [["इति", "इस प्रकार"], ["विकृत", "बदला हुआ, असामान्य"], ["व्याधि", "रोग"], ["विज्ञानीयः", "जानने योग्य"],
                 ["नाम", "नामक"], ["एकादशः", "ग्यारहवाँ"], ["अध्यायः", "अध्याय"]],
    },
}
