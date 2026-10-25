from helpers import mcq, match, order, fill, multi, accepts


def T(q, teaches):
    q["teaches"] = teaches
    return q


AUTHORED = {}

# ---------------------------------------------------------------- unit 113
AUTHORED["113"] = {
    "title": "ईषत्प्रलं बिन्यौ भ्रुवौ",
    "question": "By unit 113, how are the two eyebrows described?",
    "rule": ("The two eyebrows (भ्रुवौ) are slightly (ईषत्) drooping: the data reads the printed tokens ईषत्प्रलं and "
             "बिन्यौ together as one word, ईषत्-प्रलम्बिन्यौ."),
    "limits": ("Prose, one printed line (02.08.131), no verb. A space is probably printed inside प्रलम्बिन्यौ (text flag, "
               "'possible'): no question rests on joining the tokens or on that word's exact form. That it belongs to the "
               "list begun at card 100 is the data's reading."),
    "explain_hi": ("यह इकाई भौंहों के बारे में है; डेटा के अनुसार यह कार्ड १०० से चल रही इष्ट शरीर-लक्षणों की सूची का भाग प्रतीत होती है। "
                   "दोनों भौंहें (भ्रुवौ) थोड़ी (ईषत्) झुकी हुई, यानी नीचे की ओर लटकती हुई हों। "
                   "छपाई में ‘ईषत्प्रलं’ और ‘बिन्यौ’ अलग छपे हैं; डेटा इन्हें एक शब्द प्रलम्बिन्यौ (प्रलम्बिन् का स्त्रीलिंग द्विवचन) पढ़ता है, बीच की जगह सम्भवतः भूल से छपी। "
                   "भ्रुवौ स्त्रीलिंग द्विवचन है: दोनों भौंहें एक साथ कही गई हैं। "
                   "कोई क्रिया नहीं छपी; ‘हों’ समझा जाता है।"),
    "hook": "भौंहें: ज़रा-सी झुकी, बहुत नहीं।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "In unit 113, what does भ्रू mean?",
            ("The eyebrow", "भ्रुवौ = the two eyebrows: भ्रू is the eyebrow."),
            [("The eyelid", "The eyelid would be वर्त्म; भ्रू is the eyebrow."),
             ("The earlobe", "The ear is कर्ण (unit 112); भ्रू is the eyebrow."),
             ("The temple", "The temple is शङ्ख (unit 110); भ्रू is the eyebrow.")],
            "भ्रू = eyebrow; भ्रुवौ is its dual: the two eyebrows.",
            "भ्रू = eyebrow."),
        order(1, "Put the printed tokens of unit 113 in the printed order.",
              ["ईषत्प्रलं", "बिन्यौ", "भ्रुवौ"],
              "ईषत्प्रलं, then बिन्यौ (read with it by the data), then भ्रुवौ, the two eyebrows.",
              "ईषत्प्रलं → बिन्यौ → भ्रुवौ."),
        T(mcq("extend", 2, "In unit 113, what does ईषत् add to the description of the eyebrows?",
              ("They droop only slightly", "ईषत् = slightly: the drooping is small."),
              [("They droop very strongly", "ईषत् means slightly, not strongly."),
               ("They do not droop at all", "ईषत् softens the drooping; it does not deny it."),
               ("Only one of them droops", "भ्रुवौ is dual: both eyebrows are described.")],
              "ईषत् = slightly: slightly drooping eyebrows.",
              "ईषत् = slightly, a little."),
          "ईषत् is an indeclinable meaning 'slightly'; it is often placed before the word it softens."),
        mcq("discriminate", 3, "What form is भ्रुवौ in unit 113?",
            ("Feminine nominative dual: two brows", "-औ here is the dual of the feminine stem भ्रू: both eyebrows."),
            [("Feminine nominative singular: a brow", "The singular would be भ्रूः."),
             ("Feminine nominative plural: the brows", "The plural would be भ्रुवः (three or more)."),
             ("Feminine genitive singular: of a brow", "The genitive singular would be भ्रुवः, not भ्रुवौ.")],
            "भ्रुवौ = the two eyebrows (f. nom. dual).",
            "भ्रू (f.) → dual भ्रुवौ."),
        multi("apply", 4, "Which statements fit unit 113?",
              [("No verb is printed in the line", "Right: the line is elliptical; 'are' is understood."),
               ("It says the two eyebrows are joined", "No: it says they droop slightly, nothing about joining."),
               ("It gives the eyebrows' length in aṅgulas", "No: no measure is given in this line."),
               ("Both eyebrows are described together", "Right: भ्रुवौ is dual.")],
              [0, 3],
              "Elliptical line; the dual भ्रुवौ names both eyebrows, slightly drooping.",
              "ईषत् + (प्रलम्बिन्यौ) + भ्रुवौ."),
        mcq("transfer", 5, "By the pattern of ईषत् (slightly), how is ईषत् + उष्णम् (slightly warm) joined in a new example?",
            ("ईषदुष्णम्", "त् before a vowel becomes द्: ईषत् + उष्णम् → ईषदुष्णम्."),
            [("ईषतुष्णम्", "त् does not stay त् before a vowel; it becomes द्."),
             ("ईषन्नुष्णम्", "न् can arise only before a nasal; उ is a vowel."),
             ("ईषदोष्णम्", "The vowel उ of उष्णम् does not change; only त् → द्.")],
            "ईषत् + उष्णम् = ईषदुष्णम्, 'slightly warm'.",
            "त् + vowel → द्.",
            teaches="Final त् becomes द् before a vowel; before a voiceless consonant such as प it stays: ईषत्प्र-."),
    ],
}

# ---------------------------------------------------------------- unit 114
AUTHORED["114"] = {
    "title": "ललाटमातपत्रोपमं शिरः",
    "question": "By unit 114, which shapes are named in the line, and which word is unclear?",
    "rule": ("The line names a half-moon shape with well-joined junctures (सुश्लिष्टसन्धि-अर्धचन्द्राकृति), the forehead "
             "(ललाटम्), an umbrella-like form (आतपत्रोपमम्) and the head (शिरः). The data reads: forehead like a half-moon, "
             "head like an umbrella."),
    "limits": ("Low confidence. The first word वलिभं has no sure reading: no question on it. Which noun the half-moon compound "
               "qualifies (forehead or head) and where the umbrella comparison belongs are the data's placements, not sure: "
               "no question asks which part has which shape. Questions stay on word meanings and joins."),
    "explain_hi": ("यह इकाई माथे और सिर के आकार की बात करती है, पर पाठ कमज़ोर है। "
                   "पहला शब्द ‘वलिभं’ अस्पष्ट है (शायद ‘वलि’ यानी सिलवट से आरम्भ), इसलिए उसका अर्थ नहीं दिया गया। "
                   "डेटा के अनुसार माथा (ललाट) भली भाँति जुड़े जोड़ों वाला और अर्धचन्द्र के आकार का है, और सिर (शिरः) छाते (आतपत्र) जैसा। "
                   "पर ‘सुश्लिष्टसन्धि’ वाला विशेषण सिर का भी हो सकता है, और छाते की उपमा का स्थान भी अनुवाद का चुनाव है। "
                   "इसलिए यहाँ केवल शब्दों के अर्थ और सन्धियाँ पूछी गई हैं।"),
    "hook": "अर्धचन्द्र और छाता: दो आकार, किसका कौन-सा, डेटा का पाठ।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "In unit 114, what does आतपत्र mean?",
            ("An umbrella", "आतपत्र = umbrella, parasol (literally a guard against heat)."),
            [("A lotus leaf", "A lotus leaf would be पद्मपत्र; आतपत्र is an umbrella."),
             ("A water pot", "A water pot would be कलश or घट; आतपत्र is an umbrella."),
             ("A tortoise shell", "A tortoise is कूर्म; आतपत्र is an umbrella.")],
            "आतपत्र = umbrella; -उपम = like.",
            "आतपत्र = umbrella."),
        order(1, "Put the printed words of unit 114 in the printed order.",
              ["वलिभं", "सुश्लिष्टसंध्यर्द्धचंद्राकृति", "ललाटम्", "आतपत्रोपमं", "शिरः"],
              "The unclear वलिभं; the half-moon compound; forehead; umbrella-like; head.",
              "वलिभं → सुश्लिष्ट...आकृति → ललाटम् → आतपत्रोपमं → शिरः."),
        match(2, "Match each sure word of unit 114 to its meaning.",
              [["ललाट", "forehead"], ["अर्धचन्द्र", "half-moon"], ["आकृति", "shape"], ["आतपत्र", "umbrella"],
               ["उपम", "like, similar to"], ["शिरस्", "head"]],
              "ललाट = forehead, अर्धचन्द्र = half-moon, आकृति = shape, आतपत्र = umbrella, उपम = like, शिरस् = head.",
              "ललाट, अर्धचन्द्र, आकृति, आतपत्र, उपम, शिरस्.", role="extend",
              teaches="X-उपम at the end of a compound means 'like X': आतपत्रोपम = umbrella-like."),
        mcq("discriminate", 3, "Which split of the printed संध्यर्द्ध (in unit 114) is right?",
            ("सन्धि + अर्ध", "इ before a different vowel becomes य्: सन्धि + अर्ध → सन्ध्यर्ध (printed with double द्द)."),
            [("सन्ध्या + अर्ध", "आ + अ would give long आ: सन्ध्यार्ध, not सन्ध्यर्ध."),
             ("सन्धिः + अर्ध", "Inside a compound there is no visarga; सन्धिः + अर्ध would give सन्धिरर्ध."),
             ("सन्धे + अर्ध", "ए before अ would give सन्धेऽर्ध, not सन्ध्यर्ध.")],
            "सन्धि (joint) + अर्ध (half): इ + अ → य.",
            "इ + unlike vowel → य्."),
        mcq("apply", 4, "Why is आतपत्र + उपमम् printed आतपत्रोपमं in unit 114?",
            ("अ + उ gives ओ", "अ followed by उ merges into ओ: आतपत्र + उपमम् → आतपत्रोपमम्."),
            [("अ + उ gives औ", "औ comes from अ + ओ or अ + औ, not from अ + उ."),
             ("अ + उ gives ऊ", "ऊ comes from उ + उ; here the first vowel is अ."),
             ("The उ is dropped", "The उ is not lost; it merges with अ into ओ.")],
            "आतपत्र + उपमम् = आतपत्रोपमम्.",
            "अ + उ → ओ."),
        mcq("transfer", 5, "By the pattern of आतपत्रोपमम्, how is चन्द्र + उपमम् (moon-like) joined in a new example?",
            ("चन्द्रोपमम्", "अ + उ → ओ: चन्द्र + उपमम् → चन्द्रोपमम्."),
            [("चन्द्रौपमम्", "अ + उ gives ओ, not औ."),
             ("चन्द्रूपमम्", "ऊ would need उ + उ; here it is अ + उ."),
             ("चन्द्रउपमम्", "Inside a compound the two vowels must merge; they cannot stand apart.")],
            "चन्द्र + उपमम् = चन्द्रोपमम्, 'like the moon'.",
            "अ + उ → ओ.",
            teaches="अ + उ → ओ, as in आतपत्र + उपमम् → आतपत्रोपमम्."),
    ],
}

# ---------------------------------------------------------------- unit 115
AUTHORED["115"] = {
    "title": "नैकमुला मृदवः केशाः",
    "question": "By unit 115, what is said of the hairs, and which part is open?",
    "rule": ("The hairs (केशाः) are soft (मृदवः) and नैकमूल: taken literally by the data as 'not having a single root' "
             "(न + एक + मूल)."),
    "limits": ("Prose, one printed line (02.08.133), no verb. The printed मुला is probably मूला (text flag, 'possible'). "
               "नैक may also be read as 'many' (many-rooted); the text does not explain the phrase: no question on its "
               "sense. Questions stay on the soft hair, the sure words and the joins."),
    "explain_hi": ("यह इकाई केशों (बालों) का लक्षण देती है। "
                   "केश कोमल (मृदवः) हों, और ‘नैकमूल’ हों: डेटा इसे शब्दशः ‘एक मूल वाले नहीं’ (न + एक + मूल) पढ़ता है। "
                   "कुछ लोग ‘नैक’ को ‘अनेक’ पढ़ते हैं, यानी अनेक मूल वाले; पाठ इसका अर्थ नहीं समझाता, इसलिए उस पर प्रश्न नहीं। "
                   "छपा ‘मुला’ सम्भवतः ‘मूला’ (दीर्घ ऊ) है। "
                   "मृदवः पुल्लिंग बहुवचन है और केशाः से मेल खाता है।"),
    "hook": "केश: कोमल, और ‘नैकमूल’।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "In unit 115, what does केश mean?",
            ("Hair", "केशाः = the hairs (of the head)."),
            [("Nail", "The nail is नख; केश is hair."),
             ("Skin", "The skin is त्वक्; केश is hair."),
             ("Tooth", "The tooth is दन्त; केश is hair.")],
            "केश = hair.",
            "केश = hair."),
        order(1, "Put the printed words of unit 115 in the printed order.",
              ["नैकमुला", "मृदवः", "केशाः"],
              "नैकमुला (not single-rooted, data's literal reading); soft; the hairs.",
              "नैकमुला → मृदवः → केशाः."),
        match(2, "Match each sure word of unit 115 to its meaning.",
              [["न", "not"], ["एक", "one"], ["मृदु", "soft"], ["केश", "hair"]],
              "न = not, एक = one, मृदु = soft, केश = hair.",
              "न, एक, मृदु, केश.", role="extend",
              teaches="मृदवः is the masculine nominative plural of मृदु (soft), agreeing with केशाः."),
        mcq("discriminate", 3, "By unit 115, what are the hairs called besides नैकमूल?",
            ("Soft", "मृदवः = soft (m. nom. pl. of मृदु)."),
            [("Rough", "Rough would be रूक्ष; the line says मृदवः, soft."),
             ("Stiff", "Stiff is the opposite of मृदु, soft."),
             ("Brittle", "Nothing in the line says brittle; it says soft.")],
            "मृदवः केशाः = soft hairs.",
            "मृदु = soft."),
        mcq("apply", 4, "Why does नैकमूलाः (printed नैकमुला) lose its visarga before मृदवः in unit 115?",
            ("आः drops its visarga before a voiced sound", "म is voiced: -मूलाः + मृदवः → -मूला मृदवः."),
            [("अः becomes ओ before a voiced consonant", "That is for अः; this word ends in आः."),
             ("The visarga before म becomes स् instead", "स् arises before त or थ, not before म."),
             ("Every visarga is lost at any word end", "Not so: मृदवः keeps its visarga before क in केशाः.")],
            "-मूलाः + मृदवः → -मूला मृदवः: आः before the voiced म.",
            "आः + voiced sound → आ."),
        mcq("transfer", 5, "By the pattern of न + एक → नैक, how is अत्र + एव (right here) joined in a new example?",
            ("अत्रैव", "अ + ए → ऐ: अत्र + एव → अत्रैव."),
            [("अत्रेव", "अ + ए gives ऐ, not ए."),
             ("अत्रोव", "ओ comes from अ + उ, not from अ + ए."),
             ("अत्रएव", "The two vowels must merge; they cannot stand apart.")],
            "अत्र + एव = अत्रैव, like न + एक = नैक.",
            "अ + ए → ऐ.",
            teaches="अ + ए → ऐ (vṛddhi), as in न + एक → नैक."),
    ],
}

# ---------------------------------------------------------------- unit 116
AUTHORED["116"] = {
    "title": "दृढं गूढं शिरास्थिसंधि",
    "question": "By unit 116, which parts are called firm and hidden?",
    "rule": ("Firm (दृढम्) and hidden (गूढम्): the veins (शिरा), bones (अस्थि) and joints (सन्धि), taken by the data as "
             "one neuter collective dvandva that both adjectives qualify."),
    "limits": ("Prose, one printed line (02.08.134), no verb. That both adjectives qualify the whole dvandva is the data's "
               "reading. शिरा = vein or vessel (standard: vein). The text does not explain what 'hidden' means for "
               "them: no question on that."),
    "explain_hi": ("यह इकाई शरीर के भीतर की रचनाओं का लक्षण देती है। "
                   "शिरा (नस, मानक), अस्थि (हड्डी) और सन्धि (जोड़) दृढ़ (दृढम्) और छिपे हुए (गूढम्) हों। "
                   "डेटा तीनों को एक नपुंसक एकवचन समाहार-द्वन्द्व मानता है, जिसके दोनों विशेषण हैं; इसीलिए दृढं, गूढं नपुंसक एकवचन हैं। "
                   "‘गूढ’ का विस्तार से क्या अर्थ है, पाठ नहीं बताता। "
                   "‘शिरास्थि’ में आ + अ → आ की सन्धि है।"),
    "hook": "नस, हड्डी, जोड़: पक्के और ढके।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "In unit 116, what does अस्थि mean?",
            ("Bone", "अस्थि = bone: शिरा-अस्थि-सन्धि, veins, bones and joints."),
            [("Flesh", "Flesh would be मांस; अस्थि is bone."),
             ("Fat", "Fat would be मेदस्; अस्थि is bone."),
             ("Marrow", "Marrow would be मज्जा; अस्थि is bone.")],
            "अस्थि = bone.",
            "अस्थि = bone."),
        order(1, "Put the parts of unit 116 in the printed order.",
              ["दृढं", "गूढं", "शिरा", "अस्थि", "संधि"],
              "Firm, hidden; then the compound: veins, bones, joints.",
              "दृढं → गूढं → शिरा → अस्थि → संधि."),
        match(2, "Match each word of unit 116 to its meaning.",
              [["दृढ", "firm"], ["गूढ", "hidden"], ["शिरा", "vein, vessel"], ["अस्थि", "bone"], ["सन्धि", "joint"]],
              "दृढ = firm, गूढ = hidden, शिरा = vein (standard), अस्थि = bone, सन्धि = joint.",
              "दृढ, गूढ, शिरा, अस्थि, सन्धि.", role="extend",
              teaches="A samāhāra dvandva such as शिरास्थिसन्धि is neuter singular, so its adjectives are neuter singular too."),
        mcq("discriminate", 3, "In unit 116, what does गूढ mean?",
            ("Hidden, concealed", "गूढम् = hidden: the veins, bones and joints are not exposed."),
            [("Firm, strong", "That is दृढ, the other adjective of this line."),
             ("Rounded, full", "Rounded would be वृत्त; गूढ is hidden."),
             ("Long, extended", "Long would be दीर्घ; गूढ is hidden.")],
            "दृढ = firm, गूढ = hidden: two different adjectives.",
            "गूढ = hidden."),
        mcq("apply", 4, "Which split of शिरास्थि in unit 116 is right?",
            ("शिरा + अस्थि", "आ + अ → आ: शिरा + अस्थि → शिरास्थि."),
            [("शिरः + अस्थि", "शिरस् (head) + अस्थि would give शिरोऽस्थि, not शिरास्थि."),
             ("शिरा + स्थि", "स्थि is not a word; the bone is अस्थि."),
             ("शिरास् + थि", "Neither शिरास् nor थि is a word here.")],
            "शिरा (vein) + अस्थि (bone): आ + अ → आ.",
            "आ + अ → आ."),
        mcq("transfer", 5, "By the pattern of शिरा + अस्थि → शिरास्थि, how is विद्या + अर्थी (a student) joined in a new example?",
            ("विद्यार्थी", "आ + अ → आ: विद्या + अर्थी → विद्यार्थी."),
            [("विद्यर्थी", "आ + अ gives long आ, not short अ."),
             ("विद्योर्थी", "ओ would need अ + उ; here it is आ + अ."),
             ("विद्याअर्थी", "The two vowels must merge into one आ.")],
            "विद्या + अर्थी = विद्यार्थी, like शिरा + अस्थि = शिरास्थि.",
            "आ + अ → आ.",
            teaches="आ + अ → आ (two like vowels merge into one long vowel)."),
    ],
}

# ---------------------------------------------------------------- unit 117
AUTHORED["117"] = {
    "title": "प्रकृतिमुक्तानि वातमूत्रपुरीषगुह्यानि",
    "question": "By unit 117, which bodily outputs and actions are listed, and which parts are unsure?",
    "rule": ("Wind (वात, flatus), urine (मूत्र), dung (पुरीष) and guhya, released naturally (प्रकृतिमुक्तानि); then "
             "laughing (हसित), weeping (रुदित), a doubtful word, and activities (चेष्टितानि)."),
    "limits": ("Low confidence. The printed आर्द्रनि is no word: no question on it. Whether प्रकृतिमुक्त governs every "
               "item is not stated. गुह्य (probable: genitals) is no keyed answer. वात here = flatus (data). चंचेष्टितानि "
               "is read च चेष्टितानि (text flag, 'possible')."),
    "explain_hi": ("यह इकाई दो सूचियाँ देती है, और इसका पाठ कमज़ोर है। "
                   "पहली सूची: वात (यहाँ अधोवायु, दोष नहीं), मूत्र, पुरीष (मल) और गुह्य (गुप्त अंग या बातें; सम्भावित: जननांग); ये प्रकृति से, यानी स्वाभाविक ढंग से, मुक्त हों। "
                   "दूसरी सूची: हँसना (हसित), रोना (रुदित), फिर अस्पष्ट छपा ‘आर्द्रनि’, और चेष्टाएँ (चेष्टितानि)। "
                   "‘प्रकृतिमुक्त’ सब पर लागू है या नहीं, पाठ नहीं कहता। "
                   "छपा ‘चंचेष्टितानि’ सम्भवतः ‘च चेष्टितानि’ है (भूल से अनुस्वार)।"),
    "hook": "वात, मूत्र, पुरीष: स्वाभाविक ढंग से निकलें।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "In unit 117, what does पुरीष mean?",
            ("Faeces, dung", "पुरीष = faeces: वात-मूत्र-पुरीष, flatus, urine and dung."),
            [("Sweat", "Sweat would be स्वेद; पुरीष is faeces."),
             ("Urine", "Urine is मूत्र, the word just before पुरीष."),
             ("Phlegm", "Phlegm would be श्लेष्मन्; पुरीष is faeces.")],
            "पुरीष = faeces, dung.",
            "पुरीष = faeces."),
        order(1, "Put the items of the first list of unit 117 in the printed order.",
              ["वात", "मूत्र", "पुरीष", "गुह्य"],
              "Flatus, urine, dung, guhya: वातमूत्रपुरीषगुह्यानि.",
              "वात → मूत्र → पुरीष → गुह्य."),
        match(2, "Match each sure word of unit 117 to its meaning.",
              [["मूत्र", "urine"], ["पुरीष", "faeces, dung"], ["हसित", "laughing"], ["रुदित", "weeping"],
               ["चेष्टित", "activity, movement"]],
              "मूत्र = urine, पुरीष = dung, हसित = laughing, रुदित = weeping, चेष्टित = activity.",
              "मूत्र, पुरीष, हसित, रुदित, चेष्टित.", role="extend",
              teaches="हसित, रुदित and चेष्टित are past participles used as neuter action nouns: laughing, weeping, activity."),
        mcq("discriminate", 3, "In unit 117, what does हसित mean?",
            ("Laughing", "हसित = laughing, laughter (from √हस्)."),
            [("Weeping", "That is रुदित, the next word of the list."),
             ("Speaking", "Speaking would be भाषित; हसित is laughing."),
             ("Sleeping", "Sleeping would be स्वप्न; हसित is laughing.")],
            "हसित = laughing, रुदित = weeping.",
            "हसित = laughing."),
        mcq("apply", 4, "By the data's literal reading, what does प्रकृतिमुक्तानि say of the first list in unit 117?",
            ("They are released in the natural way", "प्रकृति-मुक्त: released naturally (data's literal reading)."),
            [("They are held back by an effort", "मुक्त means released, not held back."),
             ("They are removed by a purgative", "The line names no purgative or treatment."),
             ("They are stopped by a medicine", "मुक्त means released; no medicine is named.")],
            "प्रकृतिमुक्त = released by nature, in the natural way.",
            "मुक्त = released."),
        mcq("transfer", 5, "By the pattern of चेष्टितानि (activities, n. nom. pl.), what does फलानि mean in a new example?",
            ("Fruits, three or more", "-आनि is the neuter nominative/accusative plural: फलानि = fruits."),
            [("Only one single fruit", "The singular would be फलम्."),
             ("Exactly two fruits", "The dual would be फले."),
             ("Of the many fruits", "'Of the fruits' would need the genitive फलानाम्.")],
            "फलानि = fruits, like चेष्टितानि = activities.",
            "Neuter -आनि = nom./acc. plural.",
            teaches="-आनि marks the neuter nominative/accusative plural: चेष्टितानि, मूत्रपुरीषगुह्यानि."),
    ],
}

# ---------------------------------------------------------------- unit 118
AUTHORED["118"] = {
    "title": "शुष्यदिष्टं शरीरमिति",
    "question": "By unit 118, which body is desirable after bathing and anointing?",
    "rule": ("Likewise (तथा), desirable (इष्टम्) is the body (शरीरम्) that, bathed and anointed (स्नातानुलिप्तम्), dries "
             "(शुष्यत्) in the order of the downward spread (अधःप्रसृतानुपूर्व्या)."),
    "limits": ("Prose, one printed line (02.08.136). The exact sense of अधःप्रसृतानुपूर्व्या and what spreads (water, "
               "unguent) are open: no question on them. The data reads the closing इति as ending the description begun at "
               "card 100 (इष्टं च पुनर्...); the text does not state the pairing: no question on it."),
    "explain_hi": ("यह इकाई इष्ट शरीर का एक और लक्षण देती है। "
                   "स्नान किया हुआ और लेप लगाया हुआ (स्नातानुलिप्तम्) शरीर, नीचे की ओर फैले क्रम से (अधःप्रसृतानुपूर्व्या) सूखता हुआ (शुष्यत्), इष्ट है। "
                   "क्या फैलता है (जल या लेप) और क्रम का ठीक अर्थ क्या है, पाठ नहीं कहता; इस पर प्रश्न नहीं। "
                   "अन्त का ‘इति’ डेटा के अनुसार कार्ड १०० (‘इष्टं च पुनर्...’) से आरम्भ हुए वर्णन को समाप्त करता प्रतीत होता है; पाठ यह जोड़ नहीं बताता। "
                   "‘शुष्यदिष्टं’ में शुष्यत् + इष्टम् है: स्वर से पहले त् → द्।"),
    "hook": "नहाया, लेप लगा, क्रम से सूखा: इष्ट शरीर।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "In unit 118, what does स्नात mean?",
            ("Bathed", "स्नात = bathed (ppp. of √स्ना)."),
            [("Fed", "Fed would be भुक्त; स्नात is bathed."),
             ("Rested", "Rested would be विश्रान्त; स्नात is bathed."),
             ("Fasted", "Fasting would be उपवास; स्नात is bathed.")],
            "स्नात = bathed; अनुलिप्त = anointed.",
            "स्नात = bathed."),
        order(1, "Put the words of unit 118 in the printed order.",
              ["स्नातानुलिप्तम्", "अधःप्रसृतानुपूर्व्या", "शुष्यत्", "इष्टं", "शरीरमिति"],
              "Bathed and anointed; in the order of the downward spread; drying; desirable; the body (thus).",
              "स्नातानुलिप्तम् → अधःप्रसृतानुपूर्व्या → शुष्यत् → इष्टं → शरीरमिति."),
        match(2, "Match each word of unit 118 to its meaning.",
              [["स्नात", "bathed"], ["अनुलिप्त", "anointed"], ["शुष्यत्", "drying"], ["इष्ट", "desirable"],
               ["शरीर", "body"]],
              "स्नात = bathed, अनुलिप्त = anointed, शुष्यत् = drying, इष्ट = desirable, शरीर = body.",
              "स्नात, अनुलिप्त, शुष्यत्, इष्ट, शरीर.", role="extend",
              teaches="शुष्यत् is a present participle of √शुष्: 'drying', an action going on."),
        mcq("discriminate", 3, "Which split of शुष्यदिष्टं in unit 118 is right?",
            ("शुष्यत् + इष्टम्", "त् before a vowel → द्: शुष्यत् + इष्टम् → शुष्यदिष्टम्."),
            [("शुष्यत् + दिष्टम्", "That would give a double द्: शुष्यद्दिष्टम्."),
             ("शुष्यती + इष्टम्", "ई + इ would give long ई: शुष्यतीष्टम्."),
             ("शुष्यतः + इष्टम्", "अः before इ drops the visarga: शुष्यत इष्टम्.")],
            "शुष्यत् (drying) + इष्टम् (desirable).",
            "त् + vowel → द्."),
        mcq("apply", 4, "Why is शुष्यत् printed शुष्यद् before इष्टं in unit 118?",
            ("त् before a vowel becomes द्", "इ is a vowel: शुष्यत् + इष्टम् → शुष्यदिष्टम्."),
            [("त् before a vowel becomes न्", "न् can arise only before a nasal consonant."),
             ("त् before every sound becomes द्", "Not every: before the voiceless प it stays (गर्भात्प्रभृति, unit 120)."),
             ("द् is the stem's own final sound", "The participle is शुष्यत्; the द् comes from sandhi.")],
            "शुष्यत् + इष्टम्: त् + vowel → द्.",
            "त् + vowel → द्."),
        mcq("transfer", 5, "By the pattern of स्नात + अनुलिप्तम् → स्नातानुलिप्तम्, how is धौत + अम्बरम् (washed garment) joined in a new example?",
            ("धौताम्बरम्", "अ + अ → आ: धौत + अम्बरम् → धौताम्बरम्."),
            [("धौतम्बरम्", "अ + अ gives long आ, not short अ."),
             ("धौतोम्बरम्", "ओ would need अ + उ; here it is अ + अ."),
             ("धौतैम्बरम्", "ऐ would need अ + ए; here it is अ + अ.")],
            "धौत + अम्बरम् = धौताम्बरम्, like स्नात + अनुलिप्तम् = स्नातानुलिप्तम्.",
            "अ + अ → आ.",
            teaches="अ + अ → आ, as in स्नात + अनुलिप्तम् → स्नातानुलिप्तम्."),
    ],
}

# ---------------------------------------------------------------- unit 119
AUTHORED["119"] = {
    "title": "भवति चात्र",
    "question": "What does the formula भवति चात्र of unit 119 do?",
    "rule": ("And on this (matter) there is (भवति च अत्र): a formula that introduces what follows (data: the verses); "
             "what 'is' is not printed."),
    "limits": ("Prose, one printed line (02.08.137). The subject of भवति is not printed, and nothing is supplied. In the "
               "data, cards 120 and 121 are typed verse, cards 122 and 123 prose."),
    "explain_hi": ("‘भवति चात्र’ यानी ‘और इस विषय में (यह) है:’। "
                   "यह आगे आने वाली बात, डेटा के अनुसार श्लोकों, का आरम्भ-सूत्र है। "
                   "क्या ‘है’, यह छपा नहीं; डेटा कुछ नहीं जोड़ता और अंग्रेज़ी अनुवाद विराम-चिह्न (:) पर रुकता है। "
                   "‘चात्र’ में च + अत्र है: अ + अ → आ।"),
    "hook": "भवति चात्र: ‘इस पर यह भी है:’",
    "core": False,
    "questions": [
        mcq("pretest", 0, "In unit 119, what does अत्र mean?",
            ("Here, on this", "अत्र = here, on this (matter)."),
            [("There, on that", "There would be तत्र; अत्र is here."),
             ("Now, at once", "Now would be अधुना; अत्र is here."),
             ("Always, ever", "Always would be सदा; अत्र is here.")],
            "अत्र = here.",
            "अत्र = here."),
        order(1, "Put the words of unit 119 in the printed order.",
              ["भवति", "च", "अत्र"],
              "There is; and; on this.",
              "भवति → च → अत्र."),
        match(2, "Match each word of unit 119 to its meaning.",
              [["भवति", "there is, it is"], ["च", "and"], ["अत्र", "here, on this"]],
              "भवति = there is, च = and, अत्र = here, on this.",
              "भवति, च, अत्र.", role="extend",
              teaches="भवति is the 3rd singular present of √भू: 'is, there is'."),
        mcq("discriminate", 3, "Which split of चात्र in unit 119 is right?",
            ("च + अत्र", "अ + अ → आ: च + अत्र → चात्र."),
            [("चा + अत्र", "चा is not a word; the particle is च."),
             ("च + त्र", "त्र is not a word; the adverb is अत्र."),
             ("चात् + र", "Neither चात् nor र is a word here.")],
            "च (and) + अत्र (here).",
            "अ + अ → आ."),
        mcq("apply", 4, "What is the job of भवति चात्र in unit 119?",
            ("It introduces what follows", "A formula: 'and on this there is:' (data: the verses that follow)."),
            [("It closes the whole chapter", "The chapter is closed by the colophon of unit 124."),
             ("It gives the body's measure", "No measure is named in this line."),
             ("It names a disease to treat", "No disease is named in this line.")],
            "भवति चात्र = 'and on this there is:', an opening formula.",
            "भवति चात्र introduces what follows."),
        mcq("transfer", 5, "By the pattern of अत्र (here), what does सर्वत्र mean in a new example?",
            ("Everywhere", "-त्र makes adverbs of place: अत्र here, तत्र there, सर्वत्र everywhere."),
            [("Always", "Always would be सर्वदा, with the time suffix -दा."),
             ("Nowhere", "Nowhere would be न क्वापि; सर्व = all."),
             ("Then", "Then would be तदा; सर्वत्र is a place adverb.")],
            "सर्व + त्र = in all places: everywhere.",
            "-त्र = adverb of place.",
            teaches="The suffix -त्र makes adverbs of place: अत्र (here), तत्र (there)."),
    ],
}

# ---------------------------------------------------------------- unit 120
AUTHORED["120"] = {
    "title": "उत्तरोत्तरसुक्षेत्रं गर्भात्प्रभृति नीरुजं",
    "question": "By unit 120, which marks are listed, and from when is the subject free from disease?",
    "rule": ("With a field better and better (उत्तरोत्तरसुक्षेत्रम्), free from disease (नीरुजम्) from the garbha onward "
             "(गर्भात् प्रभृति), auspicious (शुभम्), growing slowly (शनैः वर्धमानम्) by āyāma, knowledge and specialised "
             "knowledge."),
    "limits": ("Verse, two printed lines joined (02.08.138–139). No noun is stated. क्षेत्र (field or body), गर्भ (embryo "
               "or womb) and आयाम (length or restraint) are open: no question on which sense is meant. The data reads the "
               "adjectives as running on into card 121: no question on it."),
    "explain_hi": ("यह ‘भवति चात्र’ के बाद का पहला श्लोक है और विशेषणों की एक सूची देता है; विशेष्य संज्ञा छपी नहीं। "
                   "उत्तरोत्तर (एक के बाद एक बढ़कर) उत्तम क्षेत्र वाला, गर्भ से आरम्भ करके (गर्भात् प्रभृति) रोगरहित (नीरुजम्)। "
                   "आयाम, ज्ञान और विज्ञान से धीरे-धीरे (शनैः) बढ़ता हुआ (वर्धमानम्), शुभ। "
                   "क्षेत्र का अर्थ खेत या शरीर, गर्भ का भ्रूण या गर्भाशय, और आयाम का लम्बाई या संयम: पाठ इन्हें नहीं खोलता। "
                   "डेटा के अनुसार यह वाक्य अगले कार्ड १२१ में चलता प्रतीत होता है।"),
    "hook": "गर्भ से नीरोग, धीरे-धीरे बढ़ता, शुभ।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "In unit 120, what does नीरुज mean?",
            ("Free from disease", "नीरुज = without disease (रुज् = disease)."),
            [("Full of great strength", "Strength would be बल; नीरुज is free from disease."),
             ("Slow in its growing", "Slow growth is शनैः वर्धमानम्, a different phrase."),
             ("Born before its time", "Nothing is said of birth time; नीरुज is free from disease.")],
            "नीरुज = free from disease.",
            "नीरुज = disease-free."),
        order(1, "Put the phrases of unit 120 in the printed order.",
              ["उत्तरोत्तरसुक्षेत्रं", "गर्भात्प्रभृति नीरुजं", "आयामज्ञानविज्ञानैः", "वर्द्धमानं", "शनैः शुभं"],
              "Better and better field; disease-free from the garbha onward; by āyāma, knowledge, special knowledge; growing; slowly, auspicious.",
              "उत्तरोत्तरसुक्षेत्रं → गर्भात्प्रभृति नीरुजं → आयामज्ञानविज्ञानैः → वर्द्धमानं → शनैः शुभं."),
        match(2, "Match each word of unit 120 to its meaning.",
              [["शनैः", "slowly"], ["वर्धमान", "growing"], ["विज्ञान", "specialised knowledge"],
               ["नीरुज", "free from disease"], ["शुभ", "auspicious"]],
              "शनैः = slowly, वर्धमान = growing, विज्ञान = specialised knowledge, नीरुज = free from disease, शुभ = auspicious.",
              "शनैः, वर्धमान, विज्ञान, नीरुज, शुभ.", role="extend",
              teaches="उत्तरोत्तर (उत्तर + उत्तर) means 'more and more, one after another increasing'."),
        mcq("discriminate", 3, "By unit 120, from when is the subject free from disease?",
            ("From the garbha onward", "गर्भात् प्रभृति: ablative + प्रभृति = from ... onward."),
            [("Only after sixteen years", "No age in years is named in this verse."),
             ("From the first marriage", "No marriage is named in this verse."),
             ("Only in the last years", "प्रभृति means from ... onward, starting at the garbha.")],
            "गर्भात् प्रभृति नीरुजम् = free from disease from the garbha onward.",
            "Ablative + प्रभृति = from ... onward."),
        mcq("apply", 4, "Why is -विज्ञानैः printed -विज्ञानैर् before वर्द्धमानं in unit 120?",
            ("Visarga after ऐ before a voiced sound → र्", "व is voiced: -विज्ञानैः + वर्धमानम् → -विज्ञानैर्वर्धमानम्."),
            [("Visarga before every consonant → र्", "Not every: before the voiceless श of शुभं it is not र्."),
             ("Visarga after ऐ before a voiced sound drops", "Dropping is the rule after आ (and अ before vowels other than अ), not ऐ."),
             ("र् is part of the instrumental ending", "The instrumental plural ending is -ऐः; र् comes only from sandhi.")],
            "-ऐः + voiced व → -ऐर्व.",
            "Vowel other than अ/आ + ः before a voiced sound → र्."),
        mcq("transfer", 5, "By the pattern of -विज्ञानैर्वर्द्धमानं, how is देवैः + वन्दितः (praised by the gods) joined in a new example?",
            ("देवैर्वन्दितः", "Visarga after ऐ before the voiced व → र्."),
            [("देवै वन्दितः", "The visarga drops after आ (or अ), not after ऐ."),
             ("देवैस्वन्दितः", "स् arises from a visarga before त or थ, not before व."),
             ("देवैश्वन्दितः", "श् arises before च, छ (or optionally श), not before व.")],
            "देवैः + वन्दितः = देवैर्वन्दितः.",
            "ऐः + voiced sound → ऐर्.",
            teaches="A visarga after a vowel other than अ/आ becomes र् before a voiced sound: -विज्ञानैः + वर्धमानम् → -विज्ञानैर्वर्धमानम्."),
    ],
}

# ---------------------------------------------------------------- unit 121
AUTHORED["121"] = {
    "title": "इति सर्वगुणोपेते शरीरे",
    "question": "By unit 121, what is established in a body endowed with all qualities?",
    "rule": ("Thus, in a body endowed with all qualities (सर्वगुणोपेते शरीरे): a hundred autumns, i.e. years (शरदां शतम्); "
             "life-span (आयुः), lordship (ऐश्वर्यम्) and all desired states (इष्टाः सर्वे भावाः) are established "
             "(प्रतिष्ठिताः)."),
    "limits": ("Verse, two printed lines joined (02.08.140–141); line 1 has no verb. 'A hundred autumns' = a hundred years "
               "is the usual idiom (data). Taking इष्टाः with सर्वे भावाः is the data's reading. Whether this continues "
               "card 120 is not stated: no question on it."),
    "explain_hi": ("इस प्रकार सब गुणों से युक्त शरीर में (सर्वगुणोपेते शरीरे) सौ शरद् (शरदां शतम्), यानी सौ वर्ष। "
                   "आयु (आयुः), ऐश्वर्य और सब इष्ट भाव (इष्टाः सर्वे भावाः) उसमें स्थापित (प्रतिष्ठिताः) रहते हैं। "
                   "‘सौ शरद्’ सौ वर्ष का सामान्य मुहावरा है। "
                   "‘आयुरैश्वर्यम्’ में आयुः + ऐश्वर्यम् है: उ के बाद विसर्ग स्वर से पहले र् बनता है। "
                   "डेटा के अनुसार यह कार्ड १२० के विशेषणों से जुड़ा प्रतीत होता है; पाठ यह नहीं कहता।"),
    "hook": "सर्वगुण शरीर: सौ वर्ष, आयु, ऐश्वर्य।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "In unit 121, what does शरदां शतम् mean?",
            ("A hundred years (autumns)", "शरद् = autumn, used for a year; शत = hundred."),
            [("A hundred months (moons)", "A month would be मास; शरद् is autumn, a year."),
             ("A hundred days (suns)", "A day would be दिवस or अहन्; शरद् is a year."),
             ("A hundred lives (births)", "A birth would be जन्म; शरद् is a year.")],
            "शरदां शतम् = a hundred autumns = a hundred years.",
            "शरद् = autumn, year."),
        order(1, "Put the parts of the second line of unit 121 in the printed order.",
              ["आयुः", "ऐश्वर्यम्", "इष्टाः च", "सर्वे भावाः", "प्रतिष्ठिताः"],
              "Life-span; lordship; and desired; all states; are established.",
              "आयुः → ऐश्वर्यम् → इष्टाः च → सर्वे भावाः → प्रतिष्ठिताः."),
        match(2, "Match each word of unit 121 to its meaning.",
              [["शरद्", "autumn, year"], ["शत", "hundred"], ["आयुस्", "life-span"], ["ऐश्वर्य", "lordship"],
               ["प्रतिष्ठित", "established"]],
              "शरद् = autumn (year), शत = hundred, आयुस् = life-span, ऐश्वर्य = lordship, प्रतिष्ठित = established.",
              "शरद्, शत, आयुस्, ऐश्वर्य, प्रतिष्ठित.", role="extend",
              teaches="सर्वगुणोपेत = सर्व + गुण + उपेत, 'endowed with all qualities' (अ + उ → ओ)."),
        multi("discriminate", 3, "By unit 121, which are established in a body endowed with all qualities?",
              [("Victory in battle (जय)", "No: victory is not named in this verse."),
               ("Life-span (आयुः)", "Right: आयुः is named first in line 2."),
               ("Heaven after death (स्वर्गः)", "No: heaven is not named in this verse."),
               ("Lordship (ऐश्वर्यम्)", "Right: ऐश्वर्यम् follows आयुः.")],
              [1, 3],
              "आयुः, ऐश्वर्यम् and all desired states are प्रतिष्ठिताः.",
              "आयुः ऐश्वर्यम् इष्टाः सर्वे भावाः प्रतिष्ठिताः."),
        mcq("apply", 4, "Why is आयुः printed आयुर् before ऐश्वर्यम् in unit 121?",
            ("Visarga after उ before a vowel → र्", "ऐ is a vowel: आयुः + ऐश्वर्यम् → आयुरैश्वर्यम्."),
            [("Visarga after उ before a vowel drops", "Dropping is the rule after आ (and अ before vowels other than अ), not उ."),
             ("Visarga before a vowel always → र्", "Not always: after अ or आ it does not give र्."),
             ("र् is the stem's own final sound", "The stem is आयुस्; the र् comes only from sandhi.")],
            "आयुः + ऐश्वर्यम् → आयुरैश्वर्यम्.",
            "उः + vowel → उर्."),
        mcq("transfer", 5, "By the pattern of सर्वगुणोपेते शरीरे (in a body endowed with all qualities), what does शुद्धे देशे mean in a new example?",
            ("In a clean place", "देशे is the locative singular of देश (m.), and शुद्धे agrees with it."),
            [("Of a clean place", "'Of' would need the genitive शुद्धस्य देशस्य."),
             ("From a clean place", "'From' would need the ablative शुद्धात् देशात्."),
             ("To a clean place", "'To' would need the dative शुद्धाय देशाय or the accusative.")],
            "शुद्धे देशे = in a clean place, like सर्वगुणोपेते शरीरे = in a body endowed with all qualities.",
            "Locative -ए = in, on.",
            teaches="An adjective agrees with its noun in the locative: सर्वगुणोपेते शरीरे, 'in a body endowed with all qualities'."),
    ],
}

# ---------------------------------------------------------------- unit 122
AUTHORED["122"] = {
    "title": "अनुत्सेकमदैन्यं च सुखं दुःखं च सेवते",
    "question": "By unit 122, how does one experience pleasure and pain, and which line is unsure?",
    "rule": ("One experiences (सेवते) pleasure and pain (सुखं दुःखं च) without arrogance (अनुत्सेकम्) and without "
             "dejection (अदैन्यम्). The second printed line (सत्त्वांस्तप्यमानस्तु ...) is uncertain."),
    "limits": ("Low confidence; typed prose in the data. The subject of सेवते is not printed. Line 2: the sense of "
               "सत्त्वान् and तप्यमानः is unresolved, and तामतः is read तामसः only conjecturally: no question on line 2. "
               "Whether the unit continues card 121 is not stated."),
    "explain_hi": ("पहली पंक्ति साफ़ है: (वह) अहंकार के बिना (अनुत्सेकम्) और दीनता के बिना (अदैन्यम्) सुख और दुःख को भोगता है (सेवते)। "
                   "यानी सुख में घमण्ड नहीं, दुःख में दीनता नहीं। "
                   "दूसरी पंक्ति कठिन है: ‘सत्त्वान्’ किस पर निर्भर है और ‘तप्यमान’ का अर्थ (तपता हुआ या तप करता हुआ) खुला है; छपा ‘तामतः’ अनुमान से ‘तामसः’ पढ़ा गया। "
                   "इसलिए प्रश्न केवल पहली पंक्ति पर हैं। "
                   "अनुत्सेक में अन्- (स्वर से पहले) और अदैन्य में अ- (व्यंजन से पहले) निषेध है।"),
    "hook": "सुख में घमण्ड नहीं, दुःख में दीनता नहीं।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "In unit 122, what does दैन्य mean?",
            ("Dejection", "दैन्य = dejection, wretchedness; अ-दैन्य = without it."),
            [("Arrogance", "Arrogance is उत्सेक, the other word negated here."),
             ("Generosity", "Generosity would be दान or औदार्य; दैन्य is dejection."),
             ("Laziness", "Laziness would be आलस्य; दैन्य is dejection.")],
            "दैन्य = dejection; उत्सेक = arrogance.",
            "दैन्य = dejection."),
        order(1, "Put the words of the first line of unit 122 in the printed order.",
              ["अनुत्सेकम्", "अदैन्यं च", "सुखं", "दुःखं च", "सेवते"],
              "Without arrogance; and without dejection; pleasure; and pain; experiences.",
              "अनुत्सेकम् → अदैन्यं च → सुखं → दुःखं च → सेवते."),
        match(2, "Match each word of the first line of unit 122 to its meaning.",
              [["उत्सेक", "arrogance"], ["दैन्य", "dejection"], ["सुख", "pleasure"], ["दुःख", "pain"],
               ["सेवते", "experiences"]],
              "उत्सेक = arrogance, दैन्य = dejection, सुख = pleasure, दुःख = pain, सेवते = experiences.",
              "उत्सेक, दैन्य, सुख, दुःख, सेवते.", role="extend",
              teaches="अनुत्सेकम् and अदैन्यम् are used adverbially (neuter accusative): 'without arrogance, without dejection'."),
        mcq("discriminate", 3, "By unit 122, how does one experience pleasure and pain?",
            ("Without arrogance and without dejection", "अनुत्सेकम् अदैन्यं च: no arrogance, no dejection."),
            [("With arrogance in pleasure, dejection in pain", "The line negates both: अन्-उत्सेक, अ-दैन्य."),
             ("Only pleasure, while all pain is avoided", "सुखं दुःखं च: both pleasure and pain are experienced."),
             ("Without feeling either of the two at all", "The line says सेवते, one does experience them.")],
            "Pleasure without arrogance, pain without dejection.",
            "अनुत्सेकम् अदैन्यं च सुखं दुःखं च सेवते."),
        mcq("apply", 4, "In unit 122, why does अनुत्सेक have अन्- but अदैन्य has अ-?",
            ("अन्- before a vowel, अ- before a consonant", "उ of उत्सेक is a vowel; द of दैन्य is a consonant."),
            [("अन्- before a consonant, अ- before a vowel", "It is the other way round: अन्-उत्सेक, अ-दैन्य."),
             ("अन्- is for nouns, अ- is only for verbs", "Both words here are nouns; the choice depends on the next sound."),
             ("The two prefixes differ in their meaning", "Both mean 'not, without'; only the form differs.")],
            "Negative अ- becomes अन्- before a vowel.",
            "अन्- + vowel; अ- + consonant."),
        mcq("transfer", 5, "By the pattern of अन्- + उत्सेक → अनुत्सेक, what is the negative of उचित (proper) in a new example?",
            ("अनुचित", "उ is a vowel, so the negative is अन्-: अनुचित, improper."),
            [("अउचित", "Before a vowel the negative is अन्-, not अ-."),
             ("अनोचित", "The उ of उचित does not change to ओ."),
             ("नुचित", "The negative prefix keeps its अ: अन्-.")],
            "अन् + उचित = अनुचित, like अन् + उत्सेक = अनुत्सेक.",
            "Negative अन्- before a vowel.",
            teaches="The negative prefix is अन्- before a vowel and अ- before a consonant: अनुत्सेक, अदैन्य."),
    ],
}

# ---------------------------------------------------------------- unit 123
AUTHORED["123"] = {
    "title": "दानशीलदयास्त्यब्रह्मचर्यकृतज्ञताः",
    "question": "By unit 123, which qualities and measures are listed?",
    "rule": ("Giving (दान), conduct (शील), compassion (दया), a doubtful item, continence (ब्रह्मचर्य), gratitude "
             "(कृतज्ञता); rasāyanas, friendliness (मैत्री), and the quality (गुणः) that causes the increase of merit and "
             "life-span."),
    "limits": ("Prose, two printed lines joined (02.08.144–145), no verb. The printed दयास्त्य is damaged (सत्य a "
               "conjecture, अस्तेय an alternative): no question on that item. Whether the list is the subject of line 2, "
               "and what rasāyana means here, are not stated. गुणः is singular as printed."),
    "explain_hi": ("यह इकाई गुणों की एक सूची देती है: दान, शील (आचरण), दया, एक अस्पष्ट शब्द, ब्रह्मचर्य (संयम) और कृतज्ञता। "
                   "फिर रसायन (कायाकल्प के साधन), मैत्री, और वह गुण जो पुण्य तथा आयु की वृद्धि का कारण है। "
                   "छपा ‘दयास्त्य’ बिगड़ा है: ‘सत्य’ अनुमानित पाठ है, ‘अस्तेय’ (चोरी न करना) भी सम्भव; इसलिए उस पर प्रश्न नहीं। "
                   "यह सूची दूसरी पंक्ति की कर्ता है या नहीं, और रसायन से यहाँ क्या अभिप्रेत है, पाठ नहीं कहता। "
                   "‘पुण्यायुर्वृद्धि’ में पुण्य + आयुः (अ + आ → आ) और आयुः + वृद्धि (घोष व्यंजन से पहले उः → उर्) हैं।"),
    "hook": "दान, शील, दया, ब्रह्मचर्य, कृतज्ञता: आयु बढ़ाने वाले।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "In unit 123, what does कृतज्ञता mean?",
            ("Gratitude", "कृत (what was done) + ज्ञ (knowing) + -ता: knowing what was done for one, gratitude."),
            [("Generosity", "Giving is दान, the first item; कृतज्ञता is gratitude."),
             ("Patience", "Patience would be क्षमा or धैर्य; कृतज्ञता is gratitude."),
             ("Modesty", "Modesty would be ह्री or विनय; कृतज्ञता is gratitude.")],
            "कृतज्ञता = gratitude.",
            "कृतज्ञता = gratitude."),
        order(1, "Put these sure items of the first line of unit 123 in the printed order (the doubtful item is left out).",
              ["दान", "शील", "दया", "ब्रह्मचर्य", "कृतज्ञता"],
              "Giving, conduct, compassion, (doubtful item), continence, gratitude.",
              "दान → शील → दया → ब्रह्मचर्य → कृतज्ञता."),
        match(2, "Match each sure item of unit 123 to its meaning.",
              [["दान", "giving"], ["शील", "conduct, character"], ["दया", "compassion"], ["ब्रह्मचर्य", "continence"],
               ["मैत्री", "friendliness"]],
              "दान = giving, शील = conduct, दया = compassion, ब्रह्मचर्य = continence, मैत्री = friendliness.",
              "दान, शील, दया, ब्रह्मचर्य, मैत्री.", role="extend",
              teaches="रसायन = a rejuvenation measure; the text does not say which ones are meant here."),
        mcq("discriminate", 3, "Which split of पुण्यायुर्वृद्धि in unit 123 is right?",
            ("पुण्य + आयुः + वृद्धि", "अ + आ → आ; उः before the voiced व → उर्."),
            [("पुण्यः + आयुः + वृद्धि", "No visarga stands inside a compound; पुण्यः would not give पुण्या-."),
             ("पुण्य + आयुर् + ऋद्धि", "आयुर् + ऋद्धि would give आयुरृद्धि, not आयुर्वृद्धि."),
             ("पुण्या + युर् + वृद्धि", "Neither पुण्या here nor युर् is the word; the life-span is आयुस्.")],
            "पुण्य (merit) + आयुः (life-span) + वृद्धि (increase).",
            "अ + आ → आ; उः + voiced sound → उर्."),
        mcq("apply", 4, "In पुण्यायुर्वृद्धिहेतुगुणः of unit 123, the quality (गुण) is the cause (हेतु) of what?",
            ("The increase of merit and life-span", "पुण्य-आयुः-वृद्धि-हेतु: cause of the increase of merit and life-span."),
            [("The decrease of merit and life-span", "वृद्धि is increase, not decrease."),
             ("The increase of wealth and fame", "पुण्य is merit and आयुः is life-span, not wealth or fame."),
             ("The increase of strength and colour", "The compound names merit and life-span, not strength or colour.")],
            "हेतु = cause; वृद्धि = increase; of पुण्य and आयुः.",
            "पुण्यायुर्वृद्धिहेतु = cause of increase of merit and life-span."),
        mcq("transfer", 5, "By the pattern of पुण्य + आयुः → पुण्यायुः, how is दीर्घ + आयुः (long-lived) joined in a new example?",
            ("दीर्घायुः", "अ + आ → आ: दीर्घ + आयुः → दीर्घायुः."),
            [("दीर्घयुः", "अ + आ gives long आ, not short अ."),
             ("दीर्घेयुः", "ए would need अ + इ; here it is अ + आ."),
             ("दीर्घोयुः", "ओ would need अ + उ; here it is अ + आ.")],
            "दीर्घ + आयुः = दीर्घायुः, like पुण्य + आयुः = पुण्यायुः.",
            "अ + आ → आ.",
            teaches="अ + आ → आ, as in पुण्य + आयुः → पुण्यायुः."),
    ],
}

# ---------------------------------------------------------------- unit 124
AUTHORED["124"] = {
    "title": "इति प्रकृतिभेदीयो नामाष्टमोऽध्यायः",
    "question": "What is the name and number of the chapter that unit 124 closes?",
    "rule": ("Thus (इति) the eighth (अष्टमः) chapter (अध्यायः), named (नाम) Prakṛtibhedīya: concerning the divisions "
             "(भेद) of prakṛti (natural constitution)."),
    "limits": ("Colophon, one printed line (02.08.146). The title is explained by its own words; the line says nothing "
               "more about the chapter."),
    "explain_hi": ("यह अध्याय का समापन-वाक्य (पुष्पिका) है: ‘इस प्रकार प्रकृतिभेदीय नामक आठवाँ अध्याय’। "
                   "प्रकृतिभेदीय यानी प्रकृति (स्वाभाविक शरीर-रचना) के भेदों से सम्बन्धित। "
                   "‘प्रकृतिभेदीयो नाम’ में घोष व्यंजन न से पहले अः → ओ हुआ है। "
                   "‘नामाष्टमोऽध्यायः’ में नाम + अष्टमः (अ + अ → आ) और अष्टमः + अध्यायः (अः + अ → ओऽ) हैं।"),
    "hook": "प्रकृति के भेद: आठवाँ अध्याय पूरा।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "In unit 124, what does अध्याय mean?",
            ("Chapter", "अध्यायः = chapter: अष्टमः अध्यायः, the eighth chapter."),
            [("Verse", "A verse would be श्लोक; अध्याय is a chapter."),
             ("Teacher", "A teacher would be आचार्य; अध्याय is a chapter."),
             ("Book", "A book would be ग्रन्थ; अध्याय is a chapter.")],
            "अध्याय = chapter.",
            "अध्याय = chapter."),
        order(1, "Put the words of unit 124 in the printed order.",
              ["इति", "प्रकृतिभेदीयः", "नाम", "अष्टमः", "अध्यायः"],
              "Thus; Prakṛtibhedīya; by name; eighth; chapter.",
              "इति → प्रकृतिभेदीयः → नाम → अष्टमः → अध्यायः."),
        match(2, "Match each word of unit 124 to its meaning.",
              [["इति", "thus"], ["भेद", "division"], ["नाम", "by name"], ["अष्टम", "eighth"], ["अध्याय", "chapter"]],
              "इति = thus, भेद = division, नाम = by name, अष्टम = eighth, अध्याय = chapter.",
              "इति, भेद, नाम, अष्टम, अध्याय.", role="extend",
              teaches="-ईय makes an adjective 'concerning': प्रकृतिभेदीय = concerning the divisions of prakṛti."),
        mcq("discriminate", 3, "What does the chapter name प्रकृतिभेदीय in unit 124 mean?",
            ("Concerning the divisions of prakṛti", "प्रकृति (constitution) + भेद (division) + -ईय (concerning)."),
            [("Concerning the measures of the body", "Measures are a topic inside the chapter, not its name."),
             ("Concerning the signs of near death", "The name has भेद (division), not signs of death."),
             ("Concerning growth of the embryo", "The name has प्रकृति and भेद, not the embryo.")],
            "प्रकृतिभेदीय = concerning the divisions of prakṛti.",
            "प्रकृति + भेद + ईय."),
        mcq("apply", 4, "Why is अष्टमः printed अष्टमो before ऽध्यायः in unit 124?",
            ("अः before अ → ओ, and that अ is elided", "अष्टमः + अध्यायः → अष्टमोऽध्यायः: the avagraha marks the elided अ."),
            [("अः before any vowel at all → ओ", "Not any: before a vowel other than अ, अः becomes अ."),
             ("आः before the vowel अ → ओ", "The word ends in अः; आः only drops its visarga before a voiced sound."),
             ("ओ is the ordinal's own ending", "The nominative is अष्टमः; ओ comes only from sandhi.")],
            "अष्टमः + अध्यायः → अष्टमोऽध्यायः.",
            "अः + अ → ओऽ."),
        mcq("transfer", 5, "By the pattern of अष्टमोऽध्यायः, how is नवमः + अध्यायः (the ninth chapter) joined in a new example?",
            ("नवमोऽध्यायः", "अः + अ → ओ, with the अ elided (ऽ)."),
            [("नवम अध्यायः", "अः drops to अ only before vowels other than अ; before अ it gives ओऽ."),
             ("नवमरध्यायः", "र् arises after vowels other than अ/आ; here the vowel is अ."),
             ("नवमौध्यायः", "अः + अ gives ओ, not औ.")],
            "नवमः + अध्यायः = नवमोऽध्यायः.",
            "अः + अ → ओऽ.",
            teaches="अः + अ → ओऽ: अष्टमः + अध्यायः → अष्टमोऽध्यायः."),
    ],
}

# ================================================================ NOTES_HI
NOTES_HI = {
    "113": ("गद्य; विश्वास मध्यम; एक छपी पंक्ति (०२.०८.१३१)। पाठ-चिह्न (सम्भव): ‘ईषत्प्रलं’ और ‘बिन्यौ’ के बीच भूल से जगह छपी; डेटा "
            "दोनों को एक शब्द ईषत्-प्रलम्बिन्यौ (प्रलम्बिन् का स्त्री. द्विवचन, ‘लटकती हुई’) पढ़ता है; इस जोड़ पर प्रश्न नहीं। "
            "सन्धि जाँची: ईषत् + प्र → ईषत्प्र (अघोष प से पहले त् वैसा ही)। क्रिया नहीं छपी।"),
    "114": ("गद्य; विश्वास निम्न; एक छपी पंक्ति (०२.०८.१३२)। पाठ-चिह्न (सम्भव): ‘वलिभं’ का कोई निश्चित पाठ नहीं (शायद ‘वलि’ = सिलवट "
            "से आरम्भ); अर्थ नहीं दिया गया। ‘सुश्लिष्टसन्ध्यर्धचन्द्राकृति’ किस संज्ञा का विशेषण है (ललाटम् निकटतम नपुंसक, पर शिरः भी "
            "सम्भव) और छाते की उपमा का स्थान, दोनों अनुवाद के चुनाव हैं। छपा ‘अर्द्ध’ = अर्ध (र के बाद द्वित्व, छपाई की आदत)। सन्धि "
            "जाँची: सन्धि + अर्ध → सन्ध्यर्ध (इ + भिन्न स्वर → य्); चन्द्र + आकृति → चन्द्राकृति (अ + आ → आ); ललाटम् + आतपत्र → "
            "ललाटमातपत्र; आतपत्र + उपमम् → आतपत्रोपमम् (अ + उ → ओ)।"),
    "115": ("गद्य; विश्वास मध्यम; एक छपी पंक्ति (०२.०८.१३३)। पाठ-चिह्न (सम्भव): छपा ‘मुला’ सम्भवतः ‘मूला’ (दीर्घ ऊ)। ‘नैक’ को शब्दशः "
            "‘एक नहीं’ लिया गया; कुछ इसे ‘अनेक’ पढ़ते हैं; पाठ अर्थ नहीं खोलता। सन्धि जाँची: न + एक → नैक (अ + ए → ऐ); -मूलाः + "
            "मृदवः → -मूला मृदवः (घोष ध्वनि से पहले आः का विसर्ग लुप्त); मृदवः + केशाः: क से पहले विसर्ग ः ही छपा।"),
    "116": ("गद्य; विश्वास मध्यम; एक छपी पंक्ति (०२.०८.१३४); कोई पाठ-चिह्न नहीं। शिरा = नस या वाहिनी (मानक: नस)। तीनों शब्द एक "
            "नपुंसक समाहार-द्वन्द्व माने गए, जिसके दोनों विशेषण हैं (डेटा का पाठ)। सन्धि जाँची: दृढम् + गूढम् → दृढं गूढं और गूढम् + "
            "शिरा → गूढं शिरा (वाक्य में व्यंजन से पहले अन्तिम म् → ं); शिरा + अस्थि → शिरास्थि (आ + अ → आ)।"),
    "117": ("गद्य; विश्वास निम्न; एक छपी पंक्ति (०२.०८.१३५)। पाठ-चिह्न (सम्भव): ‘हसितरुदितार्द्रनि’ का अन्त ‘आर्द्रनि’ कोई शब्द नहीं "
            "(शायद आर्द्राणि; आर्द्र = गीला), इसलिए अस्पष्ट; केवल हसित और रुदित निश्चित। ‘चंचेष्टितानि’ = च चेष्टितानि (भूल से "
            "अनुस्वार)। वात यहाँ अधोवायु है, दोष नहीं (डेटा); गुह्य = गुप्त अंग या बातें (सम्भावित: जननांग)। ‘प्रकृतिमुक्त’ सब पर लागू "
            "है, यह नहीं कहा। सन्धि: समास के भीतर कोई स्वर-सन्धि नहीं, केवल पद जुड़े हैं।"),
    "118": ("गद्य; विश्वास मध्यम; एक छपी पंक्ति (०२.०८.१३६); कोई पाठ-चिह्न नहीं। ‘अधःप्रसृतानुपूर्व्या’ का ठीक अर्थ और क्या फैलता है "
            "(जल या लेप), खुला है। अन्त का ‘इति’ डेटा के अनुसार कार्ड १०० (छपी पंक्ति ११८, ‘इष्टं च पुनर्...’) से चले वर्णन (कार्ड "
            "१००–११७) को समाप्त करता प्रतीत होता है; पाठ यह नहीं कहता। सन्धि जाँची: स्नात + अनुलिप्तम् → स्नातानुलिप्तम् (अ + अ → "
            "आ); -लिप्तम् + अधः → -लिप्तमधः; अधः + प्रसृत: प से पहले विसर्ग ः ही; प्रसृत + आनुपूर्व्या → प्रसृतानुपूर्व्या (अ + आ → आ); "
            "शुष्यत् + इष्टम् → शुष्यदिष्टम् (स्वर से पहले त् → द्); शरीरम् + इति → शरीरमिति।"),
    "119": ("गद्य; विश्वास उच्च; एक छपी पंक्ति (०२.०८.१३७); कोई पाठ-चिह्न नहीं। आगे की बात का आरम्भ-सूत्र; ‘भवति’ का कर्ता छपा नहीं, "
            "कुछ जोड़ा नहीं गया। सन्धि जाँची: च + अत्र → चात्र (अ + अ → आ)।"),
    "120": ("श्लोक (अनुष्टुभ्); विश्वास मध्यम; दो छपी पंक्तियाँ (०२.०८.१३८ और ०२.०८.१३९) जोड़ी गईं; कोई पाठ-चिह्न नहीं। विशेष्य संज्ञा "
            "छपी नहीं। क्षेत्र = खेत या शरीर, गर्भ = भ्रूण या गर्भाशय, आयाम = लम्बाई या संयम: तीनों खुले। छपा ‘वर्द्धमानं’ = "
            "वर्धमानम् (र के बाद द्वित्व, छपाई की आदत)। सन्धि जाँची: उत्तर + उत्तर → उत्तरोत्तर (अ + उ → ओ); गर्भात् + प्रभृति: अघोष "
            "प से पहले त् वैसा ही; -विज्ञानैः + वर्धमानम् → -विज्ञानैर्वर्धमानम् (ऐ के बाद विसर्ग घोष ध्वनि से पहले र्); शनैः + शुभम्: "
            "श से पहले विसर्ग वैसा रहे या विकल्प से श् बने, छपाई में ः।"),
    "121": ("श्लोक (अनुष्टुभ्); विश्वास मध्यम; दो छपी पंक्तियाँ (०२.०८.१४० और ०२.०८.१४१) जोड़ी गईं; कोई पाठ-चिह्न नहीं। छपा "
            "‘शरीरेशरदां’ बिना जगह; ए + श में कोई सन्धि नहीं, इसलिए विभाग नियमित। ‘इष्टाः’ को ‘सर्वे भावाः’ के साथ लेना डेटा का पाठ। "
            "सन्धि जाँची: गुण + उपेते → गुणोपेते (अ + उ → ओ); शरदाम् + शतम् → शरदां शतम् (व्यंजन से पहले अन्तिम म् → ं); आयुः + "
            "ऐश्वर्यम् → आयुरैश्वर्यम् (उ के बाद विसर्ग स्वर से पहले र्); -मिष्टाः + च → -मिष्टाश्च (च से पहले विसर्ग → श्)।"),
    "122": ("डेटा में गद्य (पहली पंक्ति अनुष्टुभ्-जैसी लगती है, पर प्रकार वही रखा गया); विश्वास निम्न; दो छपी पंक्तियाँ (०२.०८.१४२ "
            "और ०२.०८.१४३)। पाठ-चिह्न (सम्भव): छपा ‘तामतः’ कोई शब्द नहीं, अनुमान से ‘तामसः’ (राजस के जोड़ में)। ‘सत्त्वान्’ किस पर "
            "निर्भर है, और ‘तप्यमान’ = तपता या तप करता, खुला। सन्धि जाँची: अदैन्यम् + च → अदैन्यं च (व्यंजन से पहले अन्तिम म् → ं); "
            "सत्त्वान् + तप्यमानः → सत्त्वांस्तप्यमानः (त से पहले न् → ंस्); तप्यमानः + तु → तप्यमानस्तु (त से पहले विसर्ग → स्); "
            "राजसः + न → राजसो न (घोष व्यंजन से पहले अः → ओ); न + एव → नैव (अ + ए → ऐ)।"),
    "123": ("डेटा में गद्य; विश्वास मध्यम; दो छपी पंक्तियाँ (०२.०८.१४४ और ०२.०८.१४५)। पाठ-चिह्न (सम्भव): छपा ‘दयास्त्य’ बिगड़ा; "
            "अनुमान ‘दया-सत्य’, विकल्प ‘दया-अस्तेय’; उस पद पर प्रश्न नहीं। ‘चपुण्य’ = च पुण्य (जगह छूटी)। ‘गुणः’ छपाई में एकवचन "
            "(बहुवचन सूची से अधिक मेल खाता; सुधारा नहीं)। सन्धि जाँची: पुण्य + आयुः → पुण्यायुः (अ + आ → आ); आयुः + वृद्धि → "
            "आयुर्वृद्धि (उ के बाद विसर्ग घोष व्यंजन से पहले र्)।"),
    "124": ("गद्य (पुष्पिका); विश्वास उच्च; एक छपी पंक्ति (०२.०८.१४६); कोई पाठ-चिह्न नहीं। सन्धि जाँची: प्रकृतिभेदीयः + नाम → "
            "प्रकृतिभेदीयो नाम (घोष व्यंजन से पहले अः → ओ); नाम + अष्टमः → नामाष्टमः (अ + अ → आ); अष्टमः + अध्यायः → अष्टमोऽध्यायः "
            "(अः + अ → ओऽ)।"),
}

# ================================================================ AIDS
AIDS = {
    "113": {
        "chunks": "ईषत्प्रलं | बिन्यौ | भ्रुवौ",
        "sandhi": "अघोष प से पहले त् वैसा ही: ईषत् + प्र → ईषत्प्र · स्वर से पहले त् → द् (नया उदाहरण): ईषत् + उष्णम् → ईषदुष्णम्।",
        "anchors": "ईषत् = ‘ज़रा-सा’: भौंहें ज़रा-सी झुकी, बहुत नहीं। (मेरी याद-पद्धति)",
    },
    "114": {
        "diagram": {"groups": [
            {"label": "छपे शब्द, क्रम से", "items": ["वलिभं: अस्पष्ट", "सुश्लिष्टसन्धि अर्धचन्द्राकृति: अर्धचन्द्र-आकार",
                                                "ललाटम्: माथा", "आतपत्रोपमम्: छाते जैसा", "शिरः: सिर"]}]},
        "chunks": "वलिभं | सुश्लिष्टसंध्यर्द्धचंद्राकृति | ललाटमातपत्रोपमं | शिरः",
        "sandhi": ("इ + भिन्न स्वर → य्: सन्धि + अर्ध → सन्ध्यर्ध · अ + आ → आ: चन्द्र + आकृति → चन्द्राकृति · अ + उ → ओ: "
                   "आतपत्र + उपमम् → आतपत्रोपमम्।"),
        "pegs": "आधा चाँद और छाता: दोनों ऊपर से गोल। डेटा माथे को अर्धचन्द्र, सिर को छाता पढ़ता है। (मेरा बनाया चित्र)",
    },
    "115": {
        "chunks": "नैकमुला | मृदवः | केशाः",
        "sandhi": "अ + ए → ऐ: न + एक → नैक · घोष ध्वनि से पहले आः का विसर्ग लुप्त: -मूलाः + मृदवः → -मूला मृदवः।",
        "anchors": "मृदु केश: कोमल बाल। (केवल सुनने की सहायता)",
    },
    "116": {
        "diagram": {"groups": [
            {"label": "दृढं, गूढं", "items": ["१ शिरा: नस", "२ अस्थि: हड्डी", "३ सन्धि: जोड़"]}]},
        "chunks": "दृढं | गूढं | शिरास्थिसंधि",
        "sandhi": "आ + अ → आ: शिरा + अस्थि → शिरास्थि · वाक्य में व्यंजन से पहले अन्तिम म् → ं: दृढम् + गूढम् → दृढं गूढं।",
        "contrast": "दृढ (पक्का) ⇄ गूढ (छिपा): दोनों विशेषण इसी इकाई में, अर्थ अलग; दृ-ढ और गू-ढ, दोनों में ‘ढ’। (केवल सुनने की सहायता)",
    },
    "117": {
        "diagram": {"groups": [
            {"label": "प्रकृतिमुक्तानि", "items": ["१ वात: अधोवायु", "२ मूत्र", "३ पुरीष: मल", "४ गुह्य (सम्भावित: जननांग)"]},
            {"label": "दूसरी सूची", "items": ["१ हसित: हँसना", "२ रुदित: रोना", "३ आर्द्रनि: अस्पष्ट", "४ चेष्टितानि: चेष्टाएँ"]}]},
        "chunks": "प्रकृतिमुक्तानि | वातमूत्रपुरीषगुह्यानि | हसितरुदितार्द्रनि | चंचेष्टितानि",
        "anchors": "पहले शरीर से निकलने वाले चार, फिर भाव और चेष्टाएँ। (मेरी याद-पद्धति)",
    },
    "118": {
        "frame": ("कैसा शरीर: स्नात और अनुलिप्त → क्या होता है: अधःप्रसृत क्रम से सूखता (शुष्यत्) → निर्णय: इष्टम्; अन्त में इति।"),
        "chunks": "तथा | स्नातानुलिप्तमधःप्रसृतानुपूर्व्या | शुष्यदिष्टं | शरीरमिति",
        "sandhi": ("अ + अ → आ: स्नात + अनुलिप्तम् → स्नातानुलिप्तम् · अ + आ → आ: प्रसृत + आनुपूर्व्या → प्रसृतानुपूर्व्या · "
                   "स्वर से पहले त् → द्: शुष्यत् + इष्टम् → शुष्यदिष्टम्।"),
    },
    "119": {
        "frame": "भवति (है) + च (और) + अत्र (इस पर) → आगे आने वाली बात का आरम्भ; क्या ‘है’, यह छपा नहीं।",
        "sandhi": "अ + अ → आ: च + अत्र → चात्र।",
        "anchors": "भवति चात्र = ‘इस पर यह भी है:’ (केवल सुनने की सहायता)",
    },
    "120": {
        "diagram": {"groups": [
            {"label": "छपा क्रम", "items": ["उत्तरोत्तरसुक्षेत्रम्", "गर्भात् प्रभृति नीरुजम्", "आयाम, ज्ञान, विज्ञान से",
                                        "वर्धमानम्", "शनैः, शुभम्"]}]},
        "chunks": "उत्तरोत्तरसुक्षेत्रं | गर्भात्प्रभृति | नीरुजं || आयामज्ञानविज्ञानैः | वर्द्धमानं | शनैः शुभं",
        "sandhi": ("अ + उ → ओ: उत्तर + उत्तर → उत्तरोत्तर · ऐ के बाद विसर्ग घोष ध्वनि से पहले र्: -विज्ञानैः + वर्धमानम् → "
                   "-विज्ञानैर्वर्धमानम् · अघोष प से पहले त् वैसा ही: गर्भात्प्रभृति।"),
    },
    "121": {
        "diagram": {"groups": [
            {"label": "सर्वगुणोपेते शरीरे", "items": ["शरदां शतम्: सौ वर्ष", "आयुः", "ऐश्वर्यम्", "इष्ट सब भाव"]}]},
        "chunks": "इति | सर्वगुणोपेते | शरीरेशरदां | शतं || आयुरैश्वर्यमिष्टाश्च | सर्वे भावाः | प्रतिष्ठिताः",
        "sandhi": ("अ + उ → ओ: गुण + उपेते → गुणोपेते · उ के बाद विसर्ग स्वर से पहले र्: आयुः + ऐश्वर्यम् → आयुरैश्वर्यम् · "
                   "च से पहले विसर्ग → श्: इष्टाः + च → इष्टाश्च।"),
        "anchors": "सौ शरद् = सौ वर्ष। (केवल सुनने की सहायता)",
    },
    "122": {
        "seesaw": "सुख ⇄ दुःख और उत्सेक (अहंकार) ⇄ दैन्य (दीनता): दोनों जोड़े इसी इकाई की पहली पंक्ति में।",
        "chunks": "अनुत्सेकमदैन्यं च | सुखं दुःखं च सेवते || सत्त्वांस्तप्यमानस्तु | राजसो नैव तामतः",
        "sandhi": ("निषेध: स्वर से पहले अन्-, व्यंजन से पहले अ-: अन् + उत्सेक → अनुत्सेक, अ + दैन्य → अदैन्य · वाक्य में व्यंजन से "
                   "पहले अन्तिम म् → ं: अदैन्यम् + च → अदैन्यं च।"),
    },
    "123": {
        "diagram": {"groups": [
            {"label": "पहली पंक्ति", "items": ["१ दान", "२ शील", "३ दया", "४ -स्त्य-: अस्पष्ट", "५ ब्रह्मचर्य", "६ कृतज्ञता"]},
            {"label": "दूसरी पंक्ति", "items": ["रसायनानि", "मैत्री", "पुण्य-आयु-वृद्धि का हेतु गुण"]}]},
        "chunks": "दानशीलदयास्त्यब्रह्मचर्यकृतज्ञताः || रसायनानि | मैत्री | चपुण्यायुर्वृद्धिहेतुगुणः",
        "sandhi": "अ + आ → आ: पुण्य + आयुः → पुण्यायुः · उ के बाद विसर्ग घोष व्यंजन से पहले र्: आयुः + वृद्धि → आयुर्वृद्धि।",
    },
    "124": {
        "frame": "इति (समाप्ति) → प्रकृतिभेदीयः (नाम) → नाम → अष्टमः (आठवाँ) → अध्यायः।",
        "chunks": "इति | प्रकृतिभेदीयो | नामाष्टमोऽध्यायः",
        "sandhi": ("घोष व्यंजन से पहले अः → ओ: प्रकृतिभेदीयः + नाम → प्रकृतिभेदीयो नाम · अ + अ → आ: नाम + अष्टमः → नामाष्टमः · "
                   "अः + अ → ओऽ: अष्टमः + अध्यायः → अष्टमोऽध्यायः।"),
    },
}

# ================================================================ IMAGE_SPECS
IMAGE_SPECS = {
    ("114", "diagram"): {
        "file": "sh8-lalata-shira-114.svg",
        "alt": ("Table of card 114 in printed order: valibham (unclear); the half-moon shape with well-joined junctures; "
                "the forehead; umbrella-like; the head. Which noun each shape belongs to is the data's reading."),
        "type": "table",
        "title": "कार्ड ११४: छपे शब्द, क्रम से",
        "heads": ["छपा शब्द", "अर्थ"],
        "rows": [["वलिभं", "अस्पष्ट"], ["सुश्लिष्टसन्धि-अर्धचन्द्राकृति", "अर्धचन्द्र-आकार"],
                 ["ललाटम्", "माथा"], ["आतपत्रोपमम्", "छाते जैसा"], ["शिरः", "सिर"]],
    },
    ("116", "diagram"): {
        "file": "sh8-dridha-gudha-116.svg",
        "alt": ("Flowchart of card 116: the two adjectives firm and hidden both point to the one compound of veins, bones "
                "and joints, numbered one to three."),
        "type": "mermaid",
        "code": ("flowchart TD\n"
                 "  A[\"दृढं: पक्के\"] --> D[\"शिरास्थिसन्धि\"]\n"
                 "  B[\"गूढं: छिपे हुए\"] --> D\n"
                 "  D --> E[\"१ शिरा: नस\"]\n"
                 "  D --> F[\"२ अस्थि: हड्डी\"]\n"
                 "  D --> G[\"३ सन्धि: जोड़\"]\n"),
    },
    ("117", "diagram"): {
        "file": "sh8-prakriti-mukta-117.svg",
        "alt": ("Table of card 117: first list, released naturally: flatus, urine, faeces, guhya (probably the genitals); "
                "second list: laughing, weeping, an unclear word, activities."),
        "type": "table",
        "title": "कार्ड ११७: दो सूचियाँ",
        "heads": ["प्रकृतिमुक्तानि", "दूसरी सूची"],
        "rows": [["१ वात: अधोवायु", "१ हसित: हँसना"], ["२ मूत्र", "२ रुदित: रोना"],
                 ["३ पुरीष: मल", "३ आर्द्रनि: अस्पष्ट"], ["४ गुह्य (सम्भावित: जननांग)", "४ चेष्टित: चेष्टाएँ"]],
    },
    ("120", "diagram"): {
        "file": "sh8-uttarottara-120.svg",
        "alt": ("Table of card 120 in printed order: a field better and better; free from disease from the garbha onward; "
                "by āyāma, knowledge and specialised knowledge; growing; slowly, auspicious."),
        "type": "table",
        "title": "कार्ड १२०: छपा क्रम",
        "heads": ["क्रम", "विशेषण"],
        "rows": [["१", "उत्तरोत्तर सुक्षेत्र: बढ़ता उत्तम क्षेत्र"], ["२", "गर्भात् प्रभृति नीरुज: रोगरहित"],
                 ["३", "आयाम, ज्ञान, विज्ञान से"], ["४", "वर्धमान: बढ़ता हुआ"], ["५", "शनैः: धीरे-धीरे; शुभ"]],
    },
    ("121", "diagram"): {
        "file": "sh8-sarvaguna-121.svg",
        "alt": ("Flowchart of card 121: in a body endowed with all qualities, a hundred years; life-span, lordship and all "
                "desired states are established."),
        "type": "mermaid",
        "code": ("flowchart TD\n"
                 "  A[\"सर्वगुणोपेत शरीर में\"] --> B[\"शरदां शतम्: सौ वर्ष\"]\n"
                 "  A -- \"प्रतिष्ठित\" --> C[\"आयुः\"]\n"
                 "  A -- \"प्रतिष्ठित\" --> D[\"ऐश्वर्यम्\"]\n"
                 "  A -- \"प्रतिष्ठित\" --> E[\"सब इष्ट भाव\"]\n"),
    },
    ("122", "seesaw"): {
        "file": "sh8-sukha-duhkha-122.svg",
        "alt": ("Split of card 122, first line: experienced, pleasure and pain; without, arrogance and dejection."),
        "type": "split",
        "title": "कार्ड १२२: पहली पंक्ति",
        "cols": [["सेवते: भोगता है", ["सुखं: सुख", "दुःखं: दुःख"]],
                 ["बिना: अन्-, अ-", ["उत्सेक: अहंकार", "दैन्य: दीनता"]]],
    },
    ("123", "diagram"): {
        "file": "sh8-dana-shila-123.svg",
        "alt": ("Table of card 123 in printed order: giving, conduct, compassion, an unclear item, continence, gratitude; "
                "then rasāyanas, friendliness, and the quality causing increase of merit and life-span."),
        "type": "table",
        "title": "कार्ड १२३: गुणों की सूची",
        "heads": ["क्रम", "गुण"],
        "rows": [["१", "दान"], ["२", "शील: आचरण"], ["३", "दया"], ["४", "-स्त्य-: अस्पष्ट"], ["५", "ब्रह्मचर्य"],
                 ["६", "कृतज्ञता"], ["७", "रसायनानि"], ["८", "मैत्री"], ["९", "पुण्य-आयु-वृद्धि का हेतु गुण"]],
    },
}
