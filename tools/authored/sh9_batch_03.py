from helpers import mcq, match, order, fill, multi, accepts


def T(q, teaches):
    q["teaches"] = teaches
    return q


AUTHORED = {}

# ---------------------------------------------------------------- unit 27
AUTHORED["27"] = {
    "title": "यस्योत्सिक्तं मेढ्रम्",
    "question": "By unit 27, which three signs of the male genitals does the text give?",
    "rule": ("He whose penis (मेढ्र) is swollen (उत्सिक्त), or whose two testicles (वृषण) have gone out too far, or the "
             "reverse of this (अतः विपर्ययः): these are signs in the list of this chapter."),
    "limits": ("Prose relative clause; no main clause here. Printed अत्यिनिःसृतौ possibly has an extra य; अतिनिःसृतौ (gone out too far) is probably meant (data: possible). "
               "'Gone out' is literal: whether drawn down or retracted, and what 'the reverse' is, are not said: no "
               "question on either."),
    "explain_hi": ("यह इकाई जननांग के रिष्ट बताती है: जिसका मेढ्र यानी पुरुष-लिंग सूजा हुआ (उत्सिक्त) हो। "
                   "या जिसके दोनों वृषण यानी अण्डकोष बहुत बाहर निकले हों (छपा ‘अत्यिनिःसृतौ’)। "
                   "या इससे उलटा हो (अतः विपर्ययः); उलटा ठीक क्या है, पाठ नहीं बताता। "
                   "छपे ‘अत्यिनिःसृतौ’ में सम्भवतः एक य अधिक है; ‘अतिनिःसृतौ’ अभिप्रेत लगता है (डेटा: सम्भव)। "
                   "‘यस्य’ से शुरू होने वाला यह सम्बन्ध-वाक्य है; ‘वह’ वाला भाग इस इकाई में नहीं छपा।"),
    "hook": "सूजा मेढ्र, बहुत निकले वृषण, या उलटा: तीन विकल्प, दो बार ‘वा’।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "In unit 27, what does उत्सिक्त say about the penis (मेढ्र)?",
            ("It is swollen", "उत्सिक्त = swollen, raised: उत्सिक्तं मेढ्रम्."),
            [("It is itching", "Itching is not named; उत्सिक्त means swollen."),
             ("It is very cold", "Coldness would be शीत or शैत्य; उत्सिक्त means swollen."),
             ("It is dark blue", "A colour such as नील is not named here; उत्सिक्त means swollen.")],
            "उत्सिक्त (ut + √sic) = swollen, raised.",
            "उत्सिक्त = swollen."),
        match(1, "Match each word of unit 27 to its meaning.",
              [["यस्य", "whose"], ["उत्सिक्त", "swollen"], ["मेढ्र", "penis"], ["वृषण", "testicle"],
               ["विपर्यय", "reverse"]],
              "यस्य = whose, उत्सिक्त = swollen, मेढ्र = penis, वृषण = testicle, विपर्यय = reverse.",
              "यस्य, उत्सिक्त, मेढ्र, वृषण, विपर्यय."),
        order(2, "Put the printed parts of unit 27 in their printed order.",
              ["यस्योत्सिक्तं", "मेढ्रमत्यिनिःसृतौ वा", "वृषणावतो", "विपर्ययो वा"],
              "Whose swollen / penis, gone out too far, or / the two testicles, than this / the reverse, or.",
              "यस्योत्सिक्तं → मेढ्रमत्यिनिःसृतौ वा → वृषणावतो → विपर्ययो वा.", role="extend",
              teaches="Three alternatives joined by वा: swollen penis, or testicles gone out too far, or the reverse of this."),
        mcq("discriminate", 3, "Which split of the printed वृषणावतो in unit 27 is right?",
            ("वृषणौ + अतः", "औ before a vowel → आव्; अः before the voiced व of विपर्ययो → ओ."),
            [("वृषणाः + अतः", "आः before a vowel loses its visarga and stays apart: it would print वृषणा अतो."),
             ("वृषणम् + अतः", "म् before a vowel simply joins: it would print वृषणमतो."),
             ("वृषणे + अतः", "ए before अ gives एऽ: it would print वृषणेऽतो.")],
            "वृषणौ (the two testicles, dual) + अतः (than this).",
            "औ + vowel → आव्."),
        mcq("apply", 4, "Why is अतः printed अतो before विपर्ययो in unit 27?",
            ("अः before a voiced consonant → ओ", "व is a voiced consonant: अतः + विपर्ययः → अतो विपर्ययः."),
            [("अः before every consonant → ओ", "Not every: before a voiceless त the visarga becomes स्."),
             ("आः before a voiced consonant → ओ", "आः only drops its visarga before a voiced sound."),
             ("अतो is the adverb's own form", "The adverb is अतः; its ओ comes from sandhi only.")],
            "अतः + विपर्ययः: अः before the voiced consonant व → ओ.",
            "अः + voiced consonant → ओ."),
        mcq("transfer", 5, "By the pattern of वृषणौ + अतः → वृषणावतः, how is हस्तौ + अत्र (the two hands, here) joined in a new example?",
            ("हस्तावत्र", "औ before a vowel becomes आव्: हस्तौ + अत्र → हस्तावत्र."),
            [("हस्तोऽत्र", "ओऽ comes from अः (or ओ) before अ; the dual here ends in औ."),
             ("हस्तौऽत्र", "ऽ marks an अ lost after ए or ओ, not after औ."),
             ("हस्तवत्र", "औ gives आव् with a long आ, not अव्.")],
            "हस्तौ + अत्र = हस्तावत्र, like वृषणौ + अतः = वृषणावतः.",
            "औ + vowel → आव्.",
            teaches="A final औ before a vowel becomes आव्: वृषणौ + अतः → वृषणावतः."),
    ],
}

# ---------------------------------------------------------------- unit 28
AUTHORED["28"] = {
    "title": "यस्य मूत्रमत्युग्रं",
    "question": "By unit 28, what sign of the urine is given, and what does the text leave open?",
    "rule": "He whose urine (मूत्र) is very fierce (अत्युग्र, strong): one more sign in the list.",
    "limits": ("Prose, a relative clause only; the main clause is not in this unit. उग्र (fierce) is kept general: it "
               "could refer to smell or to sharpness, and the text does not say which: no question on that."),
    "explain_hi": ("यह बहुत छोटी इकाई है: जिसका मूत्र बहुत उग्र हो। "
                   "उग्र यानी तीव्र, प्रचण्ड; यह गन्ध के लिए है या तीखेपन के लिए, पाठ नहीं बताता। "
                   "अति + उग्रम् → अत्युग्रम्: इ के बाद भिन्न स्वर आए तो इ → य्। "
                   "‘यस्य’ से शुरू होने वाला सम्बन्ध-वाक्य है; ‘वह’ वाला भाग इस इकाई में नहीं छपा।"),
    "hook": "मूत्र अति-उग्र: तीव्रता कैसी, पाठ चुप।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "In unit 28, what does उग्र mean?",
            ("Fierce, strong", "उग्र = fierce, strong; अति-उग्र = very fierce."),
            [("Scanty, little", "Little would be अल्प; उग्र means fierce."),
             ("Clear, pale", "Clear or pale would be अच्छ or पाण्डु; उग्र means fierce."),
             ("Cool, mild", "Mild would be मृदु; उग्र is its opposite.")],
            "उग्र = fierce, strong.",
            "उग्र = fierce."),
        match(1, "Match each word of unit 28 to its meaning.",
              [["यस्य", "whose"], ["मूत्र", "urine"], ["अति", "very, too"], ["उग्र", "fierce, strong"]],
              "यस्य = whose, मूत्र = urine, अति = very, उग्र = fierce.",
              "यस्य, मूत्र, अति, उग्र."),
        fill(2, "In unit 28, the word for 'urine' is ____ (type it in Devanagari or in English letters, e.g. dharma).",
             accepts("मूत्रम्", None, "मूत्र", "mutram", "mutra"),
             "मूत्रम्, neuter nominative singular: यस्य मूत्रम् अत्युग्रम्.",
             "मूत्रम् (urine) is neuter: its adjective अत्युग्रम् is neuter too.",
             "मूत्र = urine."),
        mcq("discriminate", 3, "Which split of मूत्रमत्युग्रं in unit 28 is right?",
            ("मूत्रम् + अति + उग्रम्", "म् joins the next vowel; इ before उ → य्: मूत्रमत्युग्रम्."),
            [("मूत्र + मत्युग्रम्", "मत्युग्रम् is not a word; the म् ends मूत्रम्."),
             ("मूत्रम् + अत्य + उग्रम्", "अत्य is not a word; the prefix is अति, whose इ became य्."),
             ("मूत्रम + अति + उग्रम्", "मूत्रम is no form; the nominative is मूत्रम्.")],
            "मूत्रम् (urine) + अति (very) + उग्रम् (fierce).",
            "इ + other vowel → य्."),
        mcq("apply", 4, "Why does अति + उग्रम् give अत्युग्रम् in unit 28?",
            ("इ before a different vowel → य्", "इ before उ becomes य्: अति + उग्रम् → अत्युग्रम्."),
            [("इ + उ → ए by guṇa", "ए comes from अ + इ, not from इ + उ."),
             ("इ + उ → ऊ, a long vowel", "Lengthening joins like vowels only (इ + इ, उ + उ)."),
             ("इ is dropped before उ", "The इ is not lost; it becomes the semivowel य्.")],
            "अति + उग्रम्: इ before a different vowel → य्.",
            "इ + other vowel → य्."),
        mcq("transfer", 5, "By the pattern of अति + उग्रम् → अत्युग्रम्, how is अति + अल्पम् (very little) joined in a new example?",
            ("अत्यल्पम्", "इ before a different vowel → य्: अति + अल्पम् → अत्यल्पम्."),
            [("अतल्पम्", "The इ is not lost; it becomes य्."),
             ("अत्याल्पम्", "आ would need a long आ after the इ; here it is short अ."),
             ("अतेल्पम्", "ए comes from अ + इ; here इ stands first.")],
            "अति + अल्पम् = अत्यल्पम्, like अति + उग्रम् = अत्युग्रम्.",
            "इ + other vowel → य्.",
            teaches="Before a different vowel इ becomes य्: अति + उग्रम् → अत्युग्रम्."),
    ],
}

# ---------------------------------------------------------------- unit 29
AUTHORED["29"] = {
    "title": "यस्य विषदोषाद्विना",
    "question": "By unit 29, which two signs are given, and what is the one with the limbs called?",
    "rule": ("Blood flows from the orifices (ख) with the hair-pores, without the fault of poison (विषदोषाद् विना); limbs too "
             "light or too heavy without cause: such a one is मुमूर्षु, about to die."),
    "limits": ("Two printed lines joined (02.09.33, 02.09.34). The orifices are not named. Whether स मुमूर्षुः also closes "
               "the first clause (bleeding) is not stated: no question on that. मुमूर्षु is literally 'wishing to die'; "
               "'about to die' is the usual sense (data's note). प्रबर्तते is printed for प्रवर्तते."),
    "explain_hi": ("पहला लक्षण: जिसके छिद्रों (ख) से, रोमकूपों सहित, विष के दोष के बिना रक्त बहता है। "
                   "छिद्र कौन-से, पाठ नहीं बताता; ‘विष के बिना’ यह शर्त है। "
                   "दूसरा लक्षण: जिसके अंग बिना कारण बहुत हल्के या बहुत भारी हों, वह मुमूर्षु है। "
                   "मुमूर्षु √मृ का इच्छार्थक रूप है: शब्दार्थ ‘मरने की इच्छा वाला’, सामान्य अर्थ ‘मरने को उद्यत’। "
                   "‘स मुमूर्षुः’ पहले वाक्य को भी समेटता है या नहीं, पाठ नहीं बताता।"),
    "hook": "विष नहीं, फिर भी रक्त; कारण नहीं, फिर भी अंग हल्के या भारी।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "In unit 29, what does मुमूर्षु usually mean?",
            ("About to die", "मुमूर्षु, desiderative of √मृ: literally 'wishing to die', usually 'about to die'."),
            [("Already dead", "Dead would be मृत; मुमूर्षु is one on the way to death."),
             ("Born again", "Rebirth is not this word; मुमूर्षु comes from √मृ, to die."),
             ("Fully cured", "Cure would be आरोग्य; मुमूर्षु is near death.")],
            "मुमूर्षु = about to die (literally 'wishing to die').",
            "मुमूर्षु = about to die."),
        match(1, "Match each word of unit 29 to its meaning.",
              [["विष", "poison"], ["ख", "orifice"], ["रोमकूप", "hair-pore"], ["अनिमित्तम्", "without cause"],
               ["गुरु", "heavy"]],
              "विष = poison, ख = orifice, रोमकूप = hair-pore, अनिमित्तम् = without cause, गुरु = heavy.",
              "विष, ख, रोमकूप, अनिमित्तम्, गुरु."),
        order(2, "Put the printed parts of unit 29 in their printed order.",
              ["यस्य विषदोषाद्विना", "खेभ्यः सरोमकूपेभ्यो", "रक्तं प्रबर्तते", "यस्यानिमित्तमंगान्यतिलघून्यतिगुरूणि",
               "वा स्युः", "स मुमूर्षुः"],
              "Whose, without poison / from the orifices with the hair-pores / blood flows / whose limbs, without cause, too light, too heavy / or would be / he is about to die.",
              "विषदोषाद्विना → खेभ्यः → रक्तं प्रबर्तते → अंगान्यतिलघून्यतिगुरूणि → वा स्युः → स मुमूर्षुः.",
              role="extend",
              teaches="Two yasya clauses: bleeding without poison, and limbs too light or too heavy; then स मुमूर्षुः."),
        mcq("discriminate", 3, "By unit 29, under what condition is the flow of blood from the orifices a sign?",
            ("Only when it is without poison", "विषदोषाद् विना: without the fault of poison."),
            [("Only when poison was taken", "The text says the opposite: विना, without poison."),
             ("Only after a wound or fall", "No wound is named; the condition is the absence of poison."),
             ("Only during a high fever", "No fever is named; the condition is the absence of poison.")],
            "विषदोषाद् विना = without the fault of poison.",
            "Bleeding from the orifices + no poison → a sign."),
        mcq("apply", 4, "A person's limbs are, without cause, far too heavy. By unit 29, what is such a one called?",
            ("मुमूर्षुः, about to die", "अंगान्यतिगुरूणि वा स्युः स मुमूर्षुः: limbs too heavy without cause."),
            [("साध्यः, curable", "साध्य is not said; the line ends स मुमूर्षुः."),
             ("बलवान्, strong", "Strength is not said; the line ends स मुमूर्षुः."),
             ("सुखी, at ease", "Ease is not said; the line ends स मुमूर्षुः.")],
            "Limbs too light or too heavy without cause → मुमूर्षुः.",
            "अनिमित्तम् अतिगुरु अंग → मुमूर्षु."),
        mcq("transfer", 5, "By the pattern of विषदोषात् + विना → विषदोषाद्विना, how is वनात् + गच्छति (goes from the forest) joined in a new example?",
            ("वनाद्गच्छति", "त् before the voiced ग becomes द्: वनात् + गच्छति → वनाद्गच्छति."),
            [("वनात्गच्छति", "त् does not stay voiceless before the voiced ग."),
             ("वनाग्गच्छति", "त् becomes द्, not a copy of the next consonant."),
             ("वनाच्गच्छति", "च् arises before च or छ, not before ग.")],
            "वनात् + गच्छति = वनाद्गच्छति, like विषदोषात् + विना = विषदोषाद्विना.",
            "त् + voiced non-nasal consonant → द्.",
            teaches="A final त् before a voiced non-nasal consonant becomes द्: विषदोषात् + विना → विषदोषाद्विना."),
    ],
}

# ---------------------------------------------------------------- unit 30
AUTHORED["30"] = {
    "title": "यस्यैकोऽनेको वा स्वरो",
    "question": "By unit 30, which changes of the voice are signs, and how do they appear?",
    "rule": ("He whose voice (स्वर), single or manifold, or stammering, thin or piteous, is suddenly (सहसा) perceived: a "
             "sign of the voice."),
    "limits": ("Prose, relative clause only; the main clause is not in this unit. The printed अन्यक्त is no word; "
               "अव्यक्त (indistinct) is a conjecture: no question on it. एकः अनेकः (single or manifold) is kept literal; "
               "what it means for the voice is not explained."),
    "explain_hi": ("यह इकाई स्वर के रिष्ट से एक नया खण्ड शुरू करती है। "
                   "जिसका स्वर एक या अनेक, या गद्गद (हकलाता), क्षाम (कृश) या दीन, अचानक (सहसा) सुनाई दे। "
                   "छपा ‘अन्यक्त’ कोई शब्द नहीं; ‘अव्यक्त’ (अस्पष्ट) अनुमानित पाठ है, इसलिए उस पर प्रश्न नहीं। "
                   "‘एक या अनेक’ का स्वर के लिए ठीक अर्थ पाठ नहीं खोलता। "
                   "‘यस्य’ से शुरू होने वाला सम्बन्ध-वाक्य है; ‘वह’ वाला भाग इस इकाई में नहीं छपा।"),
    "hook": "स्वर अचानक बदले: गद्गद, क्षाम, दीन।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "In unit 30, what does स्वर mean?",
            ("Voice", "स्वर = voice: यस्य ... स्वरः ... सहसोपलभ्यते."),
            [("Pulse", "Pulse is not this word; स्वर is the voice."),
             ("Gait", "Gait would be गति; स्वर is the voice."),
             ("Smell", "Smell would be गन्ध; स्वर is the voice.")],
            "स्वर = voice.",
            "स्वर = voice."),
        match(1, "Match each sure word of unit 30 to its meaning.",
              [["एक", "single"], ["अनेक", "manifold"], ["गद्गद", "stammering"], ["क्षाम", "thin"], ["दीन", "piteous"],
               ["सहसा", "suddenly"]],
              "एक = single, अनेक = manifold, गद्गद = stammering, क्षाम = thin, दीन = piteous, सहसा = suddenly.",
              "एक, अनेक, गद्गद, क्षाम, दीन, सहसा."),
        order(2, "Put the printed parts of unit 30 in their printed order.",
              ["यस्यैकोऽनेको वा", "स्वरो", "गद्गदान्यक्तक्षामदीनो वा", "सहसोपलभ्यते"],
              "Whose, single or manifold / voice / stammering, …, thin, piteous, or / is suddenly perceived.",
              "यस्यैकोऽनेको वा → स्वरो → गद्गदान्यक्तक्षामदीनो वा → सहसोपलभ्यते.", role="extend",
              teaches="The voice's qualities stand between स्वरः and the verb उपलभ्यते (is perceived), with सहसा (suddenly)."),
        T(multi("discriminate", 3, "Which statements fit unit 30?",
                [("The voice must be loud", "Loudness is not named; the qualities are stammering, thin, piteous."),
                 ("The voice may be single or manifold", "एकोऽनेको वा स्वरः: single or manifold."),
                 ("The change returns each night", "No time of night is named; it is perceived suddenly."),
                 ("The voice is perceived suddenly", "सहसा उपलभ्यते: suddenly perceived.")],
                [1, 3],
                "Single or manifold, stammering, thin or piteous, suddenly perceived.",
                "स्वरः ... सहसा उपलभ्यते."),
          "सहसा (suddenly) qualifies the verb उपलभ्यते: the change is perceived all at once."),
        mcq("apply", 4, "Why is एकः + अनेकः printed एकोऽनेको in unit 30?",
            ("अः + अ → ओ, the अ dropped (ऽ)", "Before अ, अः becomes ओ and the next अ is dropped, shown by ऽ."),
            [("अः before any vowel → ओऽ", "Before other vowels अः becomes अ (अंगुलय आयम्यमाना, unit 33)."),
             ("आः + अ → ओ, the अ dropped (ऽ)", "The ending is short अः; आः before a vowel only loses its visarga."),
             ("ऽ marks a long vowel in एको", "ऽ (avagraha) marks the dropped अ of अनेकः.")],
            "एकः + अनेकः → एकोऽनेकः.",
            "अः + अ → ओऽ."),
        mcq("transfer", 5, "By the pattern of सहसा + उपलभ्यते → सहसोपलभ्यते, how is गङ्गा + उदकम् (Gaṅgā water) joined in a new example?",
            ("गङ्गोदकम्", "आ + उ → ओ: गङ्गा + उदकम् → गङ्गोदकम्."),
            [("गङ्गौदकम्", "औ comes from अ/आ + ओ/औ, not from आ + उ."),
             ("गङ्गादकम्", "The उ is not lost; आ + उ merge into ओ."),
             ("गङ्गूदकम्", "ऊ would come from उ + उ; here आ stands first.")],
            "गङ्गा + उदकम् = गङ्गोदकम्, like सहसा + उपलभ्यते = सहसोपलभ्यते.",
            "आ + उ → ओ.",
            teaches="आ followed by उ merges into ओ: सहसा + उपलभ्यते → सहसोपलभ्यते."),
    ],
}

# ---------------------------------------------------------------- unit 31
AUTHORED["31"] = {
    "title": "यो वा विवक्षुर्मुह्यति",
    "question": "By unit 31, what happens to this person when he wishes to speak?",
    "rule": "Or he who, wishing to speak (विवक्षुः), becomes bewildered (मुह्यति): a sign of speech.",
    "limits": ("Prose, relative clause; the main clause is not in this unit. मुह्यति is taken literally, 'becomes "
               "bewildered'; it can also mean 'faints' (data's note): no option rests on choosing between them."),
    "explain_hi": ("या जो बोलना चाहते हुए (विवक्षुः) भ्रमित हो जाता है (मुह्यति)। "
                   "विवक्षु वि + √वच् का इच्छार्थक विशेषण है: बोलने की इच्छा वाला; इकाई २९ का मुमूर्षु भी ऐसा ही इच्छार्थक रूप है। "
                   "मुह्यति का अर्थ ‘मूर्च्छित होता है’ भी हो सकता है; डेटा शाब्दिक ‘भ्रमित होता है’ रखता है। "
                   "सन्धि: यः + वा → यो वा, विवक्षुः + मुह्यति → विवक्षुर्मुह्यति।"),
    "hook": "बोलना चाहे, पर उलझ जाए: विवक्षु मुह्यति।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "In unit 31, what does विवक्षु mean?",
            ("Wishing to speak", "विवक्षु, desiderative of vi + √vac: wishing to speak."),
            [("Wishing to eat", "Wishing to eat would be बुभुक्षु; विवक्षु is about speech."),
             ("Unable to hear", "Hearing is not in this word; विवक्षु is about speech."),
             ("Wishing to sleep", "Sleep is not in this word; विवक्षु is about speech.")],
            "विवक्षु = wishing to speak.",
            "विवक्षु = wishing to speak."),
        order(1, "Put the words of unit 31 in the printed order.",
              ["यः", "वा", "विवक्षुः", "मुह्यति"],
              "Who; or; wishing to speak; becomes bewildered.",
              "यः → वा → विवक्षुः → मुह्यति."),
        match(2, "Match each word of unit 31 to its meaning.",
              [["यः", "who"], ["वा", "or"], ["विवक्षुः", "wishing to speak"], ["मुह्यति", "becomes bewildered"]],
              "यः = who, वा = or, विवक्षुः = wishing to speak, मुह्यति = becomes bewildered.",
              "यः, वा, विवक्षुः, मुह्यति.", role="extend",
              teaches="विवक्षु, like मुमूर्षु of unit 29, is a desiderative adjective: 'wishing to (do)'."),
        mcq("discriminate", 3, "By unit 31, when does the bewilderment come?",
            ("When he wishes to speak", "विवक्षुर्मुह्यति: wishing to speak, he becomes bewildered."),
            [("When he tries to stand", "Standing is not named; the trigger is the wish to speak."),
             ("When he has eaten food", "Eating is not named; the trigger is the wish to speak."),
             ("When he wakes from sleep", "Waking is not named; the trigger is the wish to speak.")],
            "The wish to speak brings the bewilderment.",
            "विवक्षुः → मुह्यति."),
        mcq("apply", 4, "Why is विवक्षुः printed विवक्षुर् before मुह्यति in unit 31?",
            ("उः before a voiced sound → उर्", "After उ, a visarga before a voiced sound (here म) becomes र्."),
            [("उः before a voiced sound → ओ", "ओ comes from अः before a voiced consonant, not from उः."),
             ("Visarga before म is dropped", "It is not dropped: after उ it becomes र्, as printed."),
             ("र् is part of the stem विवक्षुर्", "The stem is विवक्षु; the र् comes from sandhi only.")],
            "विवक्षुः + मुह्यति → विवक्षुर्मुह्यति.",
            "इः/उः + voiced sound → इर्/उर्."),
        mcq("transfer", 5, "By the pattern of विवक्षुः + मुह्यति → विवक्षुर्मुह्यति, how is गुरुः + वदति (the teacher speaks) joined in a new example?",
            ("गुरुर्वदति", "After उ, a visarga before the voiced व becomes र्."),
            [("गुरो वदति", "ओ comes from अः, not from उः."),
             ("गुरु वदति", "After उ the visarga is not dropped; it becomes र्."),
             ("गुरुस्वदति", "स् arises before त or थ, not before व.")],
            "गुरुः + वदति = गुरुर्वदति, like विवक्षुः + मुह्यति = विवक्षुर्मुह्यति.",
            "उः + voiced sound → उर्.",
            teaches="A visarga after उ (or इ) before a voiced sound becomes र्: विवक्षुः + मुह्यति → विवक्षुर्मुह्यति."),
    ],
}

# ---------------------------------------------------------------- unit 32
AUTHORED["32"] = {
    "title": "यस्य वदतो भृशमूर्ध्वमुरो रुजति",
    "question": "By unit 32, what happens to the chest while speaking, and which four faults of the exhalation are listed?",
    "rule": ("The chest (उरः) aches greatly upward while he speaks (वदतः); the exhalation (उच्छ्वास) is too long, too "
             "short, foul-smelling or sweet-smelling."),
    "limits": ("Two printed lines joined (02.09.37, 02.09.38); the second has no verb. The data reads these lines as part "
               "of the list of signs gathered up in unit 37 ('all those are ripened by time'). ऊर्ध्वम् is taken as an "
               "adverb, 'upward'."),
    "explain_hi": ("पहला लक्षण: जिसकी छाती बोलते समय (वदतः) ऊपर की ओर बहुत (भृशम्) दुखती है। "
                   "दूसरा: जिसका उच्छ्वास, यानी बाहर निकलती साँस, बहुत लम्बा, बहुत छोटा, दुर्गन्ध वाला या सुगन्ध वाला हो। "
                   "यहाँ दो जोड़े हैं: अतिदीर्घ और अतिह्रस्व, पूतिगन्धि और सुगन्धि। "
                   "डेटा के अनुसार ये पंक्तियाँ उस लक्षण-सूची का भाग हैं जिसे इकाई ३७ ‘सर्वे ते कालपक्वाः’ से समेटती है। "
                   "दूसरी पंक्ति में क्रिया नहीं है।"),
    "hook": "बोलते ही छाती दुखे; साँस बहुत लम्बी या छोटी, दुर्गन्धित या सुगन्धित।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "In unit 32, what does उच्छ्वास mean?",
            ("Exhalation, out-breath", "उच्छ्वास = exhalation, the breath going out."),
            [("Hiccup, a jerk", "Hiccup would be हिक्का; उच्छ्वास is the out-breath."),
             ("Cough, a hack", "Cough would be कास; उच्छ्वास is the out-breath."),
             ("Sneeze, a burst", "Sneeze would be क्षुत; उच्छ्वास is the out-breath.")],
            "उच्छ्वास = exhalation.",
            "उच्छ्वास = out-breath."),
        order(1, "Put the four faults of the exhalation in unit 32's printed order.",
              ["अतिदीर्घः", "अतिह्रस्वः", "पूतिगन्धिः", "सुगन्धिः"],
              "Too long; too short; foul-smelling; sweet-smelling.",
              "अतिदीर्घः → अतिह्रस्वः → पूतिगन्धिः → सुगन्धिः."),
        match(2, "Match each word of unit 32 to its meaning.",
              [["वदतः", "while speaking"], ["भृशम्", "greatly"], ["उरः", "chest"], ["रुजति", "aches"],
               ["पूतिगन्धि", "foul-smelling"], ["सुगन्धि", "sweet-smelling"]],
              "वदतः = while speaking, भृशम् = greatly, उरः = chest, रुजति = aches, पूतिगन्धि = foul-smelling, सुगन्धि = sweet-smelling.",
              "वदतः, भृशम्, उरः, रुजति, पूतिगन्धि, सुगन्धि.", role="extend",
              teaches="वदतः is a present participle in the genitive: 'of one speaking', i.e. while he speaks."),
        mcq("discriminate", 3, "By unit 32, when does the chest ache greatly upward?",
            ("While he is speaking", "यस्य वदतो ... उरो रुजति: of one speaking, the chest aches."),
            [("While he is lying down", "Lying down is not named; वदतः = while speaking."),
             ("While he is eating food", "Eating is not named; वदतः = while speaking."),
             ("While he climbs a hill", "Climbing is not named; वदतः = while speaking.")],
            "वदतः (while speaking) is the condition.",
            "वदतः → उरो रुजति."),
        multi("apply", 4, "A patient shows these findings. Which of them are among the signs of unit 32?",
              [("Exhalation far too short", "अतिह्रस्वः उच्छ्वासः is in the list."),
               ("Fingers that do not crack when pulled", "That is unit 33, not unit 32."),
               ("Chest aching upward while he speaks", "वदतो भृशमूर्ध्वमुरो रुजति."),
               ("Exhalation that smells sweet", "सुगन्धिः उच्छ्वासः is in the list.")],
              [0, 2, 3],
              "Unit 32: chest aching while speaking; exhalation too long, too short, foul- or sweet-smelling.",
              "उरो रुजति; उच्छ्वासः अतिदीर्घः, अतिह्रस्वः, पूतिगन्धिः, सुगन्धिः."),
        mcq("transfer", 5, "By the pattern of सुगन्धिः + वा → सुगन्धिर्वा, how is अग्निः + दहति (fire burns) joined in a new example?",
            ("अग्निर्दहति", "After इ, a visarga before the voiced द becomes र्."),
            [("अग्नी दहति", "Lengthening to ई with loss of र् happens only before र, not before द."),
             ("अग्निस्दहति", "स् arises before त or थ, not before द."),
             ("अग्निश्दहति", "श् arises before च or छ (optionally before श), not before द.")],
            "अग्निः + दहति = अग्निर्दहति, like सुगन्धिः + वा = सुगन्धिर्वा.",
            "इः + voiced sound → इर्.",
            teaches="A visarga after इ before a voiced sound becomes र्: सुगन्धिः + वा → सुगन्धिर्वा."),
    ],
}

# ---------------------------------------------------------------- unit 33
AUTHORED["33"] = {
    "title": "यस्यांगुलय आयम्यमाना न स्फुटेयुः",
    "question": "By unit 33, what sign do the fingers give, and what does the doubtful second clause speak of?",
    "rule": ("He whose fingers, when stretched (आयम्यमानाः), would not crack (न स्फुटेयुः); and whose sound in sneezing, "
             "going, urinating and the like is beyond its natural state."),
    "limits": ("Low confidence. अन्योऽन्योऽपि is doubtful (no firm correction): no question on it. गत is taken as "
               "'going'; another sense cannot be excluded: no question on it. Questions rest on the first clause and on "
               "plain words."),
    "explain_hi": ("पहला वाक्य पक्का है: जिसकी उँगलियाँ खींचे जाने पर (आयम्यमानाः) न चटकें (न स्फुटेयुः)। "
                   "दूसरा वाक्य: जिसका शब्द छींकने, गमन, मूत्रत्याग आदि में अपनी स्वाभाविक अवस्था से परे हो। "
                   "दूसरे वाक्य का ‘अन्योऽन्योऽपि’ संदिग्ध है और ‘गत’ का अर्थ ‘गमन’ के अलावा भी हो सकता है; इन पर प्रश्न नहीं। "
                   "स्फुटेयुः विधिलिङ् (३ बहु.) है: ‘चटकें’। "
                   "डेटा के अनुसार वाक्य आगे चलता है और इकाई ३७ में समेटा जाता है।"),
    "hook": "खींचो तो भी उँगली न चटके।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 33, what would the fingers NOT do when stretched?",
            ("Crack", "न स्फुटेयुः: they would not crack."),
            [("Bend", "Bending is not the verb; स्फुट् = to crack."),
             ("Swell", "Swelling is not the verb; स्फुट् = to crack."),
             ("Shake", "Shaking is not the verb; स्फुट् = to crack.")],
            "न स्फुटेयुः = would not crack.",
            "स्फुट् = crack."),
        match(1, "Match each sure word of unit 33 to its meaning.",
              [["अङ्गुलि", "finger"], ["आयम्यमान", "being stretched"], ["क्षुत", "sneezing"], ["मूत्रण", "urinating"],
               ["शब्द", "sound"], ["स्वभावातीत", "beyond its natural state"]],
              "अङ्गुलि = finger, आयम्यमान = being stretched, क्षुत = sneezing, मूत्रण = urinating, शब्द = sound, स्वभावातीत = beyond its natural state.",
              "अङ्गुलि, आयम्यमान, क्षुत, मूत्रण, शब्द, स्वभावातीत."),
        order(2, "Put the printed words of unit 33's first clause in their printed order.",
              ["यस्यांगुलय", "आयम्यमाना", "न", "स्फुटेयुः"],
              "Whose fingers; being stretched; not; would crack.",
              "यस्यांगुलय → आयम्यमाना → न → स्फुटेयुः.", role="extend",
              teaches="स्फुटेयुः is an optative, 3rd plural: 'would crack'; with न, 'would not crack'."),
        mcq("discriminate", 3, "Why is अङ्गुलयः printed अंगुलय before आयम्यमाना in unit 33?",
            ("अः before a vowel other than अ → अ", "Before आ the visarga of अः is lost and the gap stays."),
            [("अः before any vowel → ओ", "ओ arises before a voiced consonant, or as ओऽ before अ."),
             ("आः before a vowel → आ", "The ending here is short अः, not आः."),
             ("अंगुलय is the stem itself", "The stem is अङ्गुलि; -अयः is the nominative plural.")],
            "अङ्गुलयः + आयम्यमानाः → अङ्गुलय आयम्यमानाः.",
            "अः + vowel other than अ → अ."),
        mcq("apply", 4, "A patient's fingers are stretched. By the first clause of unit 33, which finding is the sign?",
            ("They do not crack", "न स्फुटेयुः: the stretched fingers would not crack."),
            [("They crack loudly", "The sign is the opposite: that they do not crack."),
             ("They turn very red", "Colour is not named; the sign is the missing crack."),
             ("They swell at once", "Swelling is not named; the sign is the missing crack.")],
            "Stretched fingers that do not crack.",
            "आयम्यमानाः न स्फुटेयुः."),
        mcq("transfer", 5, "By the pattern of आयम्यमानाः + न → आयम्यमाना न, how is बालाः + गच्छन्ति (the boys go) joined in a new example?",
            ("बाला गच्छन्ति", "आः before a voiced sound drops its visarga: बाला गच्छन्ति."),
            [("बालो गच्छन्ति", "ओ comes from short अः, not from आः."),
             ("बालार्गच्छन्ति", "र् arises after vowels other than अ or आ."),
             ("बालास्गच्छन्ति", "स् arises before त or थ, not before ग.")],
            "बालाः + गच्छन्ति = बाला गच्छन्ति, like आयम्यमानाः + न = आयम्यमाना न.",
            "आः + voiced sound → आ.",
            teaches="आः drops its visarga before a voiced sound: आयम्यमानाः + न → आयम्यमाना न."),
    ],
}

# ---------------------------------------------------------------- unit 34
AUTHORED["34"] = {
    "title": "यस्येष्टोऽनिष्टो वा गंधो",
    "question": "By unit 34, which smells are signs, and where may they be found?",
    "rule": ("A smell, pleasant (इष्ट) or unpleasant (अनिष्ट), of garlands, fruits, sandalwood, corpses and the like, in "
             "the body, mouth, waste, wound, clothes and the like: a sign."),
    "limits": ("Prose, no verb; part of the list gathered up in unit 37. मल is read as bodily waste; another division of "
               "देहमुखमल cannot be excluded. Both lists end in आदि (and the like), so they are open. चन्दन = sandalwood, "
               "Santalum album (standard)."),
    "explain_hi": ("जिसके शरीर, मुख, मल (अपशिष्ट), व्रण (घाव), वस्त्र आदि में माला, फल, चन्दन, कुणप (शव) आदि की गन्ध हो। "
                   "गन्ध प्रिय (इष्ट) हो या अप्रिय (अनिष्ट), दोनों रिष्ट हैं। "
                   "दोनों सूचियाँ ‘आदि’ पर खत्म होती हैं, इसलिए खुली हैं। "
                   "चन्दन = Santalum album (मानक पहचान); कुणप = शव। "
                   "डेटा के अनुसार यह इकाई ३७ में समेटी गई सूची का भाग है।"),
    "hook": "माला की महक हो या शव की बू: प्रिय या अप्रिय, दोनों रिष्ट।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "In unit 34, what does कुणप mean?",
            ("Corpse", "कुणप = corpse, carrion."),
            [("Incense", "Incense would be धूप; कुणप is a corpse."),
             ("Lotus", "Lotus would be पद्म; कुणप is a corpse."),
             ("Honey", "Honey would be मधु; कुणप is a corpse.")],
            "कुणप = corpse.",
            "कुणप = corpse."),
        order(1, "Put the sources of smell in unit 34's printed order.",
              ["माल्य", "फल", "चन्दन", "कुणप"],
              "Garlands; fruits; sandalwood (Santalum album, standard); corpses (and the like).",
              "माल्य → फल → चन्दन → कुणप (+ आदि)."),
        match(2, "Match each word of unit 34 to its meaning.",
              [["इष्ट", "pleasant"], ["अनिष्ट", "unpleasant"], ["माल्य", "garland"], ["कुणप", "corpse"],
               ["व्रण", "wound"], ["वस्त्र", "clothes"]],
              "इष्ट = pleasant, अनिष्ट = unpleasant, माल्य = garland, कुणप = corpse, व्रण = wound, वस्त्र = clothes.",
              "इष्ट, अनिष्ट, माल्य, कुणप, व्रण, वस्त्र.", role="extend",
              teaches="अनिष्ट = अ (not) + इष्ट (pleasant): the negative prefix makes the opposite."),
        mcq("discriminate", 3, "By unit 34, which kind of smell counts as a sign?",
            ("A pleasant or an unpleasant one", "इष्टोऽनिष्टो वा गन्धः: pleasant or unpleasant."),
            [("Only a foul smell of corpses", "Not only foul: इष्टः (pleasant) is named too."),
             ("Only a sweet smell of flowers", "Not only sweet: अनिष्टः (unpleasant) is named too."),
             ("No smell, only its absence", "The line names smells present, not their absence.")],
            "Both pleasant and unpleasant smells are listed.",
            "इष्टः अनिष्टः वा गन्धः."),
        mcq("apply", 4, "In unit 34, what does the ending -आदिषु of देहमुखमलव्रणवस्त्रादिषु tell us?",
            ("In these and the like", "-आदिषु is locative plural: in body, mouth ... clothes and the like."),
            [("From these and the like", "'From' would need an ablative such as -आदिभ्यः."),
             ("Of these and the like", "'Of' would need the genitive -आदीनाम्."),
             ("With these and the like", "'With' would need the instrumental -आदिभिः.")],
            "-आदिषु = locative plural: 'in ... and the like'.",
            "-इषु = locative plural."),
        mcq("transfer", 5, "By the pattern of यस्य + इष्टः → यस्येष्टः, how is न + इति (not, thus) joined in a new example?",
            ("नेति", "अ + इ → ए: न + इति → नेति."),
            [("नैति", "ऐ comes from अ + ए or ऐ, not from अ + इ."),
             ("नीति", "ई would come from इ + इ; here अ stands first."),
             ("न्यति", "य् comes from इ before a different vowel; here अ stands first.")],
            "न + इति = नेति, like यस्य + इष्टः = यस्येष्टः.",
            "अ + इ → ए.",
            teaches="अ followed by इ merges into ए: यस्य + इष्टः → यस्येष्टः."),
    ],
}

# ---------------------------------------------------------------- unit 35
AUTHORED["35"] = {
    "title": "यस्य शरीरं यूका मक्षिकादयस्त्यजंते",
    "question": "By unit 35, what do lice, flies and the like do to the body, and for which two causes?",
    "rule": ("Lice (यूका), flies (मक्षिका) and the like greatly abandon (त्यजन्ते) or resort to (भजन्ति) the body, because of "
             "deformity (वैरूप्य) or good flavour (सौरस्य)."),
    "limits": ("Prose; part of the list gathered up in unit 37. The text does not say which cause goes with abandoning and "
               "which with resorting: no question pairs them. अत्यर्थम् is taken with the verbs; it could instead qualify "
               "the causes."),
    "explain_hi": ("जिसके शरीर को जूँ, मक्खी आदि बहुत छोड़ देती हैं या उसका आश्रय लेती हैं। "
                   "कारण दो कहे गए: वैरूप्य (विरूपता) या सौरस्य (सुरसता, अच्छा स्वाद)। "
                   "कौन-सा कारण छोड़ने से और कौन-सा आश्रय लेने से जुड़ा है, पाठ नहीं बताता। "
                   "‘अत्यर्थम्’ (बहुत) को क्रियाओं के साथ लिया गया; यह कारणों का विशेषण भी हो सकता है। "
                   "‘वाऽत्यर्थं’ का ऽ केवल छपाई की आदत है (आ + अ → आ)।"),
    "hook": "जूँ-मक्खी बहुत छोड़ दें या बहुत आश्रय लें: वैरूप्य या सौरस्य से।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "In unit 35, what does यूका mean?",
            ("Lice", "यूका = louse; यूकाः, lice."),
            [("Ants", "Ants would be पिपीलिका; यूका is the louse."),
             ("Bees", "Bees would be भ्रमर or मधुकर; यूका is the louse."),
             ("Worms", "Worms would be कृमि; यूका is the louse.")],
            "यूका = louse.",
            "यूका = louse."),
        match(1, "Match each word of unit 35 to its meaning.",
              [["वैरूप्य", "deformity"], ["सौरस्य", "good flavour"], ["यूका", "louse"], ["मक्षिका", "fly"],
               ["त्यजन्ते", "abandon"], ["भजन्ति", "resort to"]],
              "वैरूप्य = deformity, सौरस्य = good flavour, यूका = louse, मक्षिका = fly, त्यजन्ते = abandon, भजन्ति = resort to.",
              "वैरूप्य, सौरस्य, यूका, मक्षिका, त्यजन्ते, भजन्ति."),
        order(2, "Put the printed parts of unit 35 in their printed order.",
              ["यस्य शरीरं", "वैरूप्यात्सौरस्याद्वाऽत्यर्थं", "यूका मक्षिकादयस्त्यजंते", "भजंति वा"],
              "Whose body / from deformity or good flavour, greatly / lice, flies and the like abandon / or resort to.",
              "यस्य शरीरं → वैरूप्यात्सौरस्याद्वाऽत्यर्थं → यूका मक्षिकादयस्त्यजंते → भजंति वा.", role="extend",
              teaches="वैरूप्यात् and सौरस्यात् are ablatives of cause: 'because of deformity, because of good flavour'."),
        mcq("discriminate", 3, "By unit 35, what may lice, flies and the like do to the body?",
            ("Abandon it or resort to it", "त्यजन्ते भजन्ति वा: they abandon it or resort to it."),
            [("Abandon it, never resort to it", "Not only abandoning: भजन्ति वा, or resort to it, is named too."),
             ("Resort to it, never abandon it", "Not only resorting: त्यजन्ते, they abandon it, is named too."),
             ("Bite it until it bleeds", "Biting and bleeding are not named; the verbs are त्यजन्ते and भजन्ति.")],
            "Both actions are named: त्यजन्ते (abandon) or भजन्ति (resort to).",
            "त्यजन्ते भजन्ति वा."),
        mcq("apply", 4, "Why is सौरस्यात् printed सौरस्याद् before वा in unit 35?",
            ("त् before a voiced consonant → द्", "व is voiced: सौरस्यात् + वा → सौरस्याद्वा."),
            [("त् before any consonant → द्", "Not any: before स it stays त्, as in वैरूप्यात्सौरस्यात्."),
             ("The ablative ends in -आद् always", "The ending is -आत्; द् comes from sandhi before व."),
             ("त् before व → न् by nasal rule", "न् can arise only before a nasal; व is not a nasal.")],
            "सौरस्यात् + वा → सौरस्याद्वा.",
            "त् + voiced non-nasal consonant → द्."),
        mcq("transfer", 5, "By the pattern of मक्षिकादयः + त्यजन्ते → मक्षिकादयस्त्यजन्ते, how is देवाः + तत्र (the gods, there) joined in a new example?",
            ("देवास्तत्र", "A visarga before त becomes स्: देवाः + तत्र → देवास्तत्र."),
            [("देवा तत्र", "आः drops its visarga only before a voiced sound; त is voiceless."),
             ("देवाश्तत्र", "श् arises before च or छ (optionally श), not before त."),
             ("देवोस्तत्र", "ओ never arises from आः, and not before त.")],
            "देवाः + तत्र = देवास्तत्र, like मक्षिकादयः + त्यजन्ते = मक्षिकादयस्त्यजन्ते.",
            "ः + त → स्त.",
            teaches="A visarga before त becomes स्: मक्षिकादयः + त्यजन्ते → मक्षिकादयस्त्यजन्ते."),
    ],
}

# ---------------------------------------------------------------- unit 36
AUTHORED["36"] = {
    "title": "यस्य सततोष्मस्वंगावयवेषु शैत्यं",
    "question": "By unit 36, what changes of warmth, sweat and stiffness in the limbs are signs?",
    "rule": ("Coldness in limbs that are always warm; or, in cold ones, excessive coldness like कुमुद and उत्पल (both "
             "probable water lilies); excessive sweat; excessive stiffness; slackness as if flesh and blood had gone."),
    "limits": ("Prose, no verb; part of the list gathered up in unit 37. स्त्रंसः is no standard word; स्रंसः "
               "(slackness) is a possible correction: no question on it. कुमुद and उत्पल are probable identifications "
               "and only a comparison of coldness: no question on them."),
    "explain_hi": ("जिसके सदा गर्म रहने वाले अंगों में ठण्डक (शैत्य) हो। "
                   "या ठण्डे अंगों में कुमुद (सम्भवतः श्वेत कुमुदिनी) और उत्पल (सम्भवतः नीलकमल) जैसी अत्यन्त शीतलता; यह केवल ठण्डक की उपमा है। "
                   "फिर अति स्वेद (पसीना), अति स्तम्भ (अकड़न), और ऐसा ढीलापन मानो मांस और रक्त चले गए हों। "
                   "छपा ‘स्त्रंसः’ मानक शब्द नहीं; ‘स्रंसः’ (ढीलापन) सम्भावित सुधार है। "
                   "पंक्ति में क्रिया नहीं; डेटा के अनुसार यह इकाई ३७ में समेटी गई सूची का भाग है।"),
    "hook": "गर्म अंग ठण्डे, ठण्डे अंग और ठण्डे; पसीना, अकड़न, ढीलापन।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "In unit 36, what does शैत्य mean?",
            ("Coldness", "शैत्य, from शीत (cold): coldness."),
            [("Dryness", "Dryness would be रौक्ष्य; शैत्य is coldness."),
             ("Heaviness", "Heaviness would be गौरव; शैत्य is coldness."),
             ("Redness", "Redness would be रक्तता; शैत्य is coldness.")],
            "शैत्य = coldness.",
            "शैत्य = coldness."),
        order(1, "Put these signs of unit 36 in their printed order.",
              ["सततोष्मस्वंगावयवेषु शैत्यं", "शीतेषु वा ... अतिशैत्यम्", "अतिस्वेदः", "अतिस्तंभः"],
              "Coldness in always-warm limbs; or excessive coldness in cold ones; excessive sweat; excessive stiffness.",
              "शैत्यम् → अतिशैत्यम् → अतिस्वेदः → अतिस्तम्भः."),
        match(2, "Match each sure word of unit 36 to its meaning.",
              [["सतत", "constantly"], ["शीत", "cold"], ["स्वेद", "sweat"], ["स्तम्भ", "stiffness"],
               ["मांस", "flesh"], ["शोणित", "blood"]],
              "सतत = constantly, शीत = cold, स्वेद = sweat, स्तम्भ = stiffness, मांस = flesh, शोणित = blood.",
              "सतत, शीत, स्वेद, स्तम्भ, मांस, शोणित.", role="extend",
              teaches="अति- before a noun (अतिस्वेद, अतिस्तम्भ) means 'excessive'."),
        mcq("discriminate", 3, "By unit 36, what is the sign in limbs that are constantly warm?",
            ("They become cold", "सततोष्मसु अंगावयवेषु शैत्यम्: coldness in the always-warm limbs."),
            [("They grow hotter still", "The sign is the reverse: coldness where warmth is normal."),
             ("They turn dark in colour", "No colour is named; the sign is coldness."),
             ("They itch without cause", "No itching is named; the sign is coldness.")],
            "Always-warm limbs turn cold.",
            "सततोष्म अंग → शैत्य."),
        mcq("apply", 4, "Why is शोणितेषु + इव printed शोणितेष्विव in unit 36?",
            ("उ before a different vowel → व्", "उ before इ becomes व्: शोणितेषु + इव → शोणितेष्विव."),
            [("उ + इ → ओ by guṇa", "ओ comes from अ + उ, not from उ + इ."),
             ("उ and इ merge into one long ई vowel", "Lengthening joins like vowels only (इ + इ, उ + उ)."),
             ("उ is dropped before इ", "The उ is not lost; it becomes the semivowel व्.")],
            "शोणितेषु + इव → शोणितेष्विव.",
            "उ + other vowel → व्."),
        mcq("transfer", 5, "By the pattern of शोणितेषु + इव → शोणितेष्विव, how is मधु + अत्र (honey, here) joined in a new example?",
            ("मध्वत्र", "उ before a different vowel → व्: मधु + अत्र → मध्वत्र."),
            [("मधोऽत्र", "ओऽ comes from अः or ओ before अ; here the word ends in उ."),
             ("मधूत्र", "ऊ would come from उ + उ; here अ follows."),
             ("मधवत्र", "अव् comes from ओ before a vowel; here the word ends in उ.")],
            "मधु + अत्र = मध्वत्र, like शोणितेषु + इव = शोणितेष्विव.",
            "उ + other vowel → व्.",
            teaches="Before a different vowel उ becomes व्: शोणितेषु + इव → शोणितेष्विव."),
    ],
}

# ---------------------------------------------------------------- unit 37
AUTHORED["37"] = {
    "title": "सर्वे ते कालपक्वा इति",
    "question": "By unit 37, what last sign is added, and what is said of all the persons in the list?",
    "rule": ("He in whose body a conjunction (योग) or excessive conjunction (अतियोग) of the great elements (महाभूत) is seen "
             "at one time (युगपत्): all those are ripened by time (कालपक्व)."),
    "limits": ("Prose. योग is literal 'conjunction'; what is joined, and whether union or abnormal combination is meant, "
               "is not decided: no question on it. सर्वे ते = the persons of the list (data: units 32 to 37); इति closes it."),
    "explain_hi": ("और जिसके शरीर में महाभूतों का योग या अतियोग एक साथ (युगपत्) दिखाई दे। "
                   "फिर समापन: वे सभी (सर्वे ते) कालपक्व हैं, यानी काल से पके हुए। "
                   "डेटा के अनुसार ‘ते’ सूची में बताए गए व्यक्तियों की ओर लौटता है, और ‘इति’ सूची (इकाई ३२ से यहाँ तक) को बन्द करता है। "
                   "‘योग’ का यहाँ ठीक अर्थ (मेल या असामान्य मेल) पाठ तय नहीं करता। "
                   "दृश्यते = √दृश् का वर्तमान कर्मवाच्य: ‘दिखाई देता है’।"),
    "hook": "सूची के सब लोग: कालपक्व, समय से पके।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "In unit 37, what does कालपक्व literally mean?",
            ("Ripened by time", "काल (time) + पक्व (ripened): kept literal."),
            [("Cooked by fire", "Fire would be अग्नि; the first part is काल, time."),
             ("Born out of season", "Birth is not this word; पक्व means ripened."),
             ("Healed in time", "Healing is not this word; पक्व means ripened.")],
            "कालपक्व = ripened by time.",
            "काल + पक्व."),
        match(1, "Match each word of unit 37 to its meaning.",
              [["शरीर", "body"], ["युगपत्", "at one time"], ["महाभूत", "great element"], ["दृश्यते", "is seen"],
               ["सर्वे", "all"]],
              "शरीर = body, युगपत् = at one time, महाभूत = great element, दृश्यते = is seen, सर्वे = all.",
              "शरीर, युगपत्, महाभूत, दृश्यते, सर्वे."),
        order(2, "Put the printed parts of unit 37 in their printed order.",
              ["यस्य च योगोऽतियोगो वा", "शरीरे", "युगपन्महाभूतानां", "दृश्यते", "सर्वे ते कालपक्वा इति"],
              "And whose conjunction or excessive conjunction / in the body / at one time, of the great elements / is seen / all those are ripened by time.",
              "योगोऽतियोगो वा → शरीरे → युगपन्महाभूतानां → दृश्यते → सर्वे ते कालपक्वा इति.", role="extend",
              teaches="इति at the end closes the whole list of signs; सर्वे ते gathers up the persons described."),
        mcq("discriminate", 3, "By the data of unit 37, who are सर्वे ते (all those)?",
            ("The persons in the list", "Data's note: ते refers back to the persons described in the list."),
            [("The great elements", "सर्वे ते is masculine plural; for neuter महाभूत it would be सर्वाणि तानि."),
             ("The physicians who see", "No physician is named; ते are the persons described."),
             ("The six seasons of time", "Seasons are not named; ते are the persons described.")],
            "सर्वे ते = all those persons of the list.",
            "ते → the persons described."),
        mcq("apply", 4, "Why may युगपत् appear as युगपन् before महाभूतानां in unit 37?",
            ("Optional: त् before a nasal → न्", "Before the nasal म, त् may become न्; युगपद्महाभूतानाम् is also correct."),
            [("त् before every consonant → न्", "Not every: before the voiced व, त् becomes द् (सौरस्याद्वा, unit 35)."),
             ("The adverb's own stem is युगपन्", "The adverb is युगपत्; न् comes from sandhi before म."),
             ("त् must stay unchanged before म", "Before a voiced sound त् cannot stay त्; it becomes द् or, here, न्.")],
            "युगपत् + महाभूतानाम् → युगपन्महाभूतानाम् (optional; द् also correct).",
            "त् + nasal → न् (optional) or द्."),
        mcq("transfer", 5, "By the pattern of दृश्यते (is seen, of √दृश्), what does श्रूयते (of √श्रु) mean in a new example?",
            ("Is heard", "श्रूयते is the present passive of √श्रु, like दृश्यते of √दृश्."),
            [("Hears", "The active 'hears' would be शृणोति."),
             ("Will be heard", "The future passive would be श्रोष्यते."),
             ("Was heard", "The past would be अश्रूयत.")],
            "श्रूयते = is heard, as दृश्यते = is seen.",
            "दृश्यते: present passive, 'is seen'.",
            teaches="दृश्यते is the present passive of √दृश् (is seen); श्रूयते is likewise the present passive of √श्रु."),
    ],
}

# ---------------------------------------------------------------- unit 38
AUTHORED["38"] = {
    "title": "भवति चात्र",
    "question": "By unit 38, what does the formula भवति चात्र do?",
    "rule": "And on this point there is (भवति च अत्र): the set formula that opens the verse(s) which follow.",
    "limits": ("Prose. The thing that 'is' is not named in the line, and nothing is supplied (data's note); the "
               "formula only introduces what follows."),
    "explain_hi": ("‘भवति चात्र’ = ‘और इस विषय में (यह) है’। "
                   "यह एक स्थिर सूत्र है जो आगे आने वाले श्लोक या श्लोकों को खोलता है। "
                   "क्या ‘है’, यह पंक्ति नहीं बताती; डेटा कुछ जोड़ता भी नहीं। "
                   "सन्धि: च + अत्र → चात्र (अ + अ → आ)।"),
    "hook": "भवति चात्र: अब श्लोक आने वाला है।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "In unit 38, what does अत्र mean?",
            ("Here, on this point", "अत्र = here, on this point."),
            [("There, far away", "There would be तत्र; अत्र is here."),
             ("Now, at this time", "Now would be अधुना; अत्र is here."),
             ("Then, after that", "Then would be ततः; अत्र is here.")],
            "अत्र = here.",
            "अत्र = here."),
        match(1, "Match each word of unit 38 to its meaning.",
              [["भवति", "there is"], ["च", "and"], ["अत्र", "on this point"]],
              "भवति = there is, च = and, अत्र = here, on this point.",
              "भवति, च, अत्र."),
        T(multi("extend", 2, "Which statements fit unit 38?",
                [("It opens the verse(s) that follow", "The formula introduces what follows."),
                 ("It names the thing that 'is'", "Nothing is named; the data supplies nothing."),
                 ("Its verb is भवति, 'there is'", "भवति, 3rd singular present of √भू."),
                 ("It gives a sign of coming death", "It gives no sign; it is only a formula.")],
                [0, 2],
                "A set formula with the verb भवति; it opens what follows.",
                "भवति चात्र = and on this point there is."),
          "भवति चात्र is a fixed formula that introduces the following verse(s)."),
        mcq("discriminate", 3, "Which split of चात्र in unit 38 is right?",
            ("च + अत्र", "अ + अ → आ: च + अत्र → चात्र."),
            [("चा + त्र", "चा and त्र are not words here."),
             ("चात् + र", "चात् and र are not words here."),
             ("च + आत्र", "आत्र is not a word; the adverb is अत्र.")],
            "च (and) + अत्र (here).",
            "अ + अ → आ."),
        mcq("apply", 4, "Why does च + अत्र give चात्र in unit 38?",
            ("अ + अ → आ", "Two short अ merge into one long आ."),
            [("अ + अ → ओ", "ओ comes from अ + उ, not from अ + अ."),
             ("अ + अ → ए", "ए comes from अ + इ, not from अ + अ."),
             ("अ + अ → ऐ", "ऐ comes from अ + ए, not from अ + अ.")],
            "च + अत्र → चात्र.",
            "अ + अ → आ."),
        mcq("transfer", 5, "By the pattern of च + अत्र → चात्र, how is न + अस्ति (is not) joined in a new example?",
            ("नास्ति", "अ + अ → आ: न + अस्ति → नास्ति."),
            [("नोस्ति", "ओ comes from अ + उ, not from अ + अ."),
             ("नेस्ति", "ए comes from अ + इ, not from अ + अ."),
             ("नस्ति", "Two अ merge into long आ, not short अ.")],
            "न + अस्ति = नास्ति, like च + अत्र = चात्र.",
            "अ + अ → आ.",
            teaches="Two short अ merge into one long आ: च + अत्र → चात्र."),
    ],
}

# ---------------------------------------------------------------- unit 39
AUTHORED["39"] = {
    "title": "यस्यापूर्वाः सिरालेखा",
    "question": "By the verse of unit 39, which vein-lines, in which places, mean that the person does not live six months?",
    "rule": ("He whose vein-lines (सिरालेखा), never seen before or like the young moon, appear on the forehead or at the "
             "head of the bladder (बस्तिशीर्ष): he does not live six months."),
    "limits": ("A verse; two printed lines joined (02.09.45, 02.09.46). सिरा = vein, vessel (probable; a general term). "
               "Which part बस्तिशीर्ष means (upper bladder, or the lower abdomen above it) is not fixed: no question on it."),
    "explain_hi": ("जिसके ललाट पर या बस्ति (मूत्राशय) के शीर्ष पर सिराओं की रेखाएँ पहले कभी न देखी हुई (अपूर्वाः) दिखें। "
                   "या वे बालचन्द्र (नए चन्द्रमा) जैसी हों। "
                   "वह छह मास नहीं जीता (षण्मासान् न जीवति)। "
                   "सिरा का अर्थ नस या रक्तवाहिनी (सम्भावित, सामान्य शब्द) है; ‘बस्तिशीर्ष’ ठीक कौन-सा भाग है, पाठ तय नहीं करता। "
                   "यह अनुष्टुभ् श्लोक है।"),
    "hook": "माथे या बस्तिशीर्ष पर अपूर्व या बालचन्द्र-सी नस-रेखा: छह मास नहीं।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "In unit 39, what does बालेन्दु mean?",
            ("The young moon", "बाल (young) + इन्दु (moon): the young, crescent moon."),
            [("The full moon", "Full moon would be पूर्णचन्द्र; बाल means young."),
             ("A child's face", "इन्दु is the moon, not a face."),
             ("The setting sun", "इन्दु is the moon, not the sun.")],
            "बालेन्दु = young (crescent) moon.",
            "बाल + इन्दु."),
        order(1, "Put the printed parts of the verse of unit 39 in their printed order.",
              ["यस्यापूर्वाः सिरालेखा", "बालेंदुसदृश्योऽपि वा", "ललाटे बस्तिशीर्षे", "वाषण्मासान्न स जीवति"],
              "Whose vein-lines never seen before / or even like the young moon / on the forehead or at the head of the bladder (वा is printed joined to the next word) / he does not live six months.",
              "यस्यापूर्वाः सिरालेखा → बालेंदुसदृश्योऽपि वा → ललाटे बस्तिशीर्षे → वाषण्मासान्न स जीवति."),
        match(2, "Match each word of unit 39 to its meaning.",
              [["अपूर्व", "never seen before"], ["लेखा", "line"], ["ललाट", "forehead"], ["बस्ति", "bladder"],
               ["षण्मासान्", "for six months"], ["जीवति", "lives"]],
              "अपूर्व = never seen before, लेखा = line, ललाट = forehead, बस्ति = bladder, षण्मासान् = for six months, जीवति = lives.",
              "अपूर्व, लेखा, ललाट, बस्ति, षण्मासान्, जीवति.", role="extend",
              teaches="षण्मासान् is an accusative of duration: 'for six months'."),
        mcq("discriminate", 3, "By unit 39, for what span does the text say he does not live?",
            ("Six months", "षण्मासान् न स जीवति: he does not live six months."),
            [("Six days", "The time named is मासान्, months, not days."),
             ("Six years", "The time named is मासान्, months, not years."),
             ("Six seasons", "The time named is मासान्, months, not seasons.")],
            "He does not live (for) six months.",
            "षण्मासान् न जीवति."),
        multi("apply", 4, "By unit 39, where do the vein-lines appear?",
              [("On the palms", "The palms are not named; the places are the forehead and the head of the bladder."),
               ("On the forehead", "ललाटे: on the forehead."),
               ("At the head of the bladder", "बस्तिशीर्षे: at the head of the bladder."),
               ("Around the eyes", "The eyes are not named; the places are the forehead and the head of the bladder.")],
              [1, 2],
              "Two places: ललाटे or बस्तिशीर्षे.",
              "ललाटे बस्तिशीर्षे वा."),
        mcq("transfer", 5, "By the pattern of सः + जीवति → स जीवति, how is सः + गच्छति (he goes) joined in a new example?",
            ("स गच्छति", "सः loses its visarga before a consonant: स गच्छति."),
            [("सो गच्छति", "ओ is the general अः rule; the pronoun सः simply drops it before a consonant."),
             ("सर्गच्छति", "र् arises after vowels other than अ or आ."),
             ("सस्गच्छति", "स् arises before त or थ, not before ग.")],
            "सः + गच्छति = स गच्छति, like सः + जीवति = स जीवति.",
            "सः + consonant → स.",
            teaches="The pronoun सः loses its visarga before a consonant: सः + जीवति → स जीवति."),
    ],
}


# ================================================================ NOTES_HI
NOTES_HI = {
    "27": ("गद्य; विश्वास मध्यम; एक छपी पंक्ति (०२.०९.३१)। पाठ-चिह्न (सम्भव): छपे ‘अत्यिनिःसृतौ’ में एक य अधिक है; अभिप्रेत "
           "‘अतिनिःसृतौ’ (बहुत बाहर निकले)। ‘निःसृत’ शाब्दिक रखा गया: वृषण नीचे लटके या ऊपर खिंचे, पाठ नहीं बताता। ‘अतः ... विपर्ययः’ = "
           "इससे उलटा। सन्धि जाँची: यस्य + उत्सिक्तम् → यस्योत्सिक्तम् (अ + उ → ओ); व्यंजन से पहले अन्तिम म् → ं (उत्सिक्तं मेढ्रम्); "
           "वृषणौ + अतः → वृषणावतः (औ + स्वर → आव्); अतः + विपर्ययः → अतो विपर्ययः और विपर्ययः + वा → विपर्ययो वा (अः + घोष व्यंजन → ओ)।"),
    "28": ("गद्य; विश्वास उच्च; एक छपी पंक्ति (०२.०९.३२); कोई पाठ-चिह्न नहीं। केवल सम्बन्ध-वाक्य। ‘उग्र’ सामान्य रखा गया: गन्ध या "
           "तीखापन, पाठ नहीं बताता। सन्धि जाँची: मूत्रम् + अति → मूत्रमति; अति + उग्रम् → अत्युग्रम् (इ + भिन्न स्वर → य्); छपा "
           "‘अत्युग्रं’ अनुस्वार के साथ।"),
    "29": ("गद्य; विश्वास उच्च; दो छपी पंक्तियाँ (०२.०९.३३ और ०२.०९.३४) जोड़ी गईं; कोई पाठ-चिह्न नहीं। छपा ‘प्रबर्तते’ = प्रवर्तते "
           "(व/ब की वर्तनी)। छिद्रों के नाम नहीं दिए। व्याकरण-लेबल ‘सरोमकूपेभ्यः’ को पुल्लिंग कहता है, जबकि यह नपुंसक ‘खेभ्यः’ का "
           "विशेषण है (रूप दोनों में समान)। -एभ्यः पंचमी/चतुर्थी दोनों हो सकता है; यहाँ अर्थ से पंचमी। ‘स मुमूर्षुः’ पहले वाक्य को भी "
           "समेटता है या नहीं, अनिश्चित। सन्धि जाँची: विषदोषात् + विना → विषदोषाद्विना (घोष व्यंजन से पहले त् → द्); सरोमकूपेभ्यः + "
           "रक्तम् → सरोमकूपेभ्यो रक्तम् (अः + घोष व्यंजन → ओ); यस्य + अनिमित्तम् → यस्यानिमित्तम् (अ + अ → आ); अंगानि + अतिलघूनि → "
           "अंगान्यतिलघूनि (इ + भिन्न स्वर → य्); सः + मुमूर्षुः → स मुमूर्षुः।"),
    "30": ("गद्य; विश्वास मध्यम; एक छपी पंक्ति (०२.०९.३५)। पाठ-चिह्न (सम्भव): ‘अन्यक्त’ कोई शब्द नहीं; ‘अव्यक्त’ (अस्पष्ट) अनुमान "
           "(व को न पढ़ा गया), अनुवाद में अनुमान-चिह्न के साथ; इस पर प्रश्न नहीं। ‘एकः अनेकः’ शाब्दिक रखा गया। सन्धि जाँची: यस्य + "
           "एकः → यस्यैकः (अ + ए → ऐ); एकः + अनेकः → एकोऽनेकः (अः + अ → ओऽ); अनेकः + वा → अनेको वा और स्वरः + गद्गद- → स्वरो गद्गद- "
           "(अः + घोष व्यंजन → ओ); सहसा + उपलभ्यते → सहसोपलभ्यते (आ + उ → ओ)।"),
    "31": ("गद्य; विश्वास उच्च; एक छपी पंक्ति (०२.०९.३६); कोई पाठ-चिह्न नहीं। सम्बन्ध-वाक्य; मुख्य वाक्य इस इकाई में नहीं। ‘मुह्यति’ "
           "= भ्रमित होता है; ‘मूर्च्छित होता है’ भी सम्भव, शाब्दिक अर्थ रखा गया। सन्धि जाँची: यः + वा → यो वा (अः + घोष व्यंजन → ओ); "
           "विवक्षुः + मुह्यति → विवक्षुर्मुह्यति (उः + घोष → उर्)।"),
    "32": ("गद्य; विश्वास मध्यम; दो छपी पंक्तियाँ (०२.०९.३७ और ०२.०९.३८) जोड़ी गईं; कोई पाठ-चिह्न नहीं। डेटा के अनुसार यह इकाई ३७ "
           "में समेटी गई सूची का भाग है। ‘वदतः’ षष्ठी वर्तमान कृदन्त: बोलते हुए का। ‘ऊर्ध्वम्’ क्रियाविशेषण माना गया। छपा ‘गंधि’ = "
           "गन्धि। दूसरी पंक्ति में क्रिया नहीं। सन्धि जाँची: वदतः + भृशम् → वदतो भृशम् और उरः + रुजति → उरो रुजति (अः + घोष व्यंजन → "
           "ओ); यस्य + उच्छ्वासः → यस्योच्छ्वासः (अ + उ → ओ); उच्छ्वासः + अतिदीर्घः → उच्छ्वासोऽतिदीर्घः (अः + अ → ओऽ); सुगन्धिः + वा → "
           "सुगन्धिर्वा (इः + घोष → इर्)।"),
    "33": ("गद्य; विश्वास कम; एक छपी पंक्ति (०२.०९.३९)। पाठ-चिह्न (सम्भव): ‘अन्योऽन्योऽपि’ का अर्थ कमज़ोर है; कोई पक्का सुधार नहीं "
           "(शायद ‘अन्योन्यम् अपि’), छपा पाठ रखा गया; इस पर प्रश्न नहीं। ‘गत’ = गमन माना गया, दूसरा अर्थ (जैसे वायु निकलना) भी सम्भव; "
           "इस पर प्रश्न नहीं। सन्धि जाँची: यस्य + अंगुलयः → यस्यांगुलयः (अ + अ → आ); अंगुलयः + आयम्यमानाः → अंगुलय आयम्यमानाः (अः + "
           "अ-भिन्न स्वर → अ); आयम्यमानाः + न → आयम्यमाना न (आः + घोष → आ)।"),
    "34": ("गद्य; विश्वास मध्यम; एक छपी पंक्ति (०२.०९.४०); कोई पाठ-चिह्न नहीं। क्रिया नहीं; डेटा के अनुसार इकाई ३७ में समेटी गई सूची "
           "का भाग। कुणप = शव (मुर्दार भी); मल = शरीर का अपशिष्ट माना गया, ‘देहमुखमल’ का दूसरा विभाजन भी सम्भव। चन्दन = Santalum "
           "album (मानक)। सन्धि जाँची: यस्य + इष्टः → यस्येष्टः (अ + इ → ए); इष्टः + अनिष्टः → इष्टोऽनिष्टः (अः + अ → ओऽ); अनिष्टः + वा "
           "→ अनिष्टो वा (अः + घोष व्यंजन → ओ); कुणप + आदि → कुणपादि, वस्त्र + आदिषु → वस्त्रादिषु (अ + आ → आ)।"),
    "35": ("गद्य; विश्वास मध्यम; एक छपी पंक्ति (०२.०९.४१); कोई पाठ-चिह्न नहीं। ‘अत्यर्थम्’ क्रियाओं के साथ लिया गया; कारणों का विशेषण "
           "(अत्यधिक) भी हो सकता है। कौन-सा कारण किस क्रिया से, पाठ नहीं बताता। सन्धि जाँची: वैरूप्यात् + सौरस्यात् (स से पहले त् "
           "वैसा ही); सौरस्यात् + वा → सौरस्याद्वा (घोष व्यंजन से पहले त् → द्); वा + अत्यर्थम् → वाऽत्यर्थम् (आ + अ → आ; ऽ छपाई की "
           "आदत); यूकाः + मक्षिका- → यूका मक्षिका- (आः + घोष → आ); मक्षिका + आदयः → मक्षिकादयः (आ + आ → आ); मक्षिकादयः + त्यजन्ते → "
           "मक्षिकादयस्त्यजन्ते (त से पहले विसर्ग → स्)।"),
    "36": ("गद्य; विश्वास मध्यम; एक छपी पंक्ति (०२.०९.४२)। पाठ-चिह्न (सम्भव): ‘स्त्रंसः’ मानक शब्द नहीं; ‘स्रंसः’ (ढीलापन) सम्भावित "
           "सुधार; इस पर प्रश्न नहीं। कुमुद = सम्भवतः श्वेत कुमुदिनी, Nymphaea (सम्भावित); उत्पल = सम्भवतः नीलकमल, Nymphaea nouchali "
           "(सम्भावित); केवल ठण्डक की उपमा। ‘शीतेषु’ में ‘अंगावयवेषु’ समझा गया। क्रिया नहीं; डेटा के अनुसार इकाई ३७ में समेटी गई सूची "
           "का भाग। सन्धि जाँची: अंग + अवयवेषु → अंगावयवेषु (अ + अ → आ); कुमुद + उत्पल → कुमुदोत्पल (अ + उ → ओ); अनुकारि + अति → "
           "अनुकार्यति (इ + भिन्न स्वर → य्); अतिस्वेदः + अतिस्तम्भः → अतिस्वेदोऽतिस्तम्भः (अः + अ → ओऽ); शोणितेषु + इव → शोणितेष्विव "
           "(उ + भिन्न स्वर → व्)।"),
    "37": ("गद्य; विश्वास मध्यम; एक छपी पंक्ति (०२.०९.४३); कोई पाठ-चिह्न नहीं। अन्तिम ‘इति’ पिछली लक्षण-सूची (डेटा: इकाई ३२ से ३७) को "
           "बन्द करता है, अनुवाद में नहीं लिया गया। ‘योग’ शाब्दिक ‘मेल’ रखा गया; क्या जुड़ता है, पाठ यहाँ नहीं बताता। ‘ते’ = सूची के "
           "व्यक्ति। सन्धि जाँची: योगः + अतियोगः → योगोऽतियोगः (अः + अ → ओऽ); अतियोगः + वा → अतियोगो वा (अः + घोष व्यंजन → ओ); युगपत् + "
           "महाभूतानाम् → युगपन्महाभूतानाम् (नासिक्य से पहले त् → न् वैकल्पिक, द् भी शुद्ध); कालपक्वाः + इति → कालपक्वा इति (आः + स्वर → "
           "आ)।"),
    "38": ("गद्य; विश्वास उच्च; एक छपी पंक्ति (०२.०९.४४); कोई पाठ-चिह्न नहीं। आगे के श्लोक(ों) को खोलने वाला सूत्र; क्या ‘है’, पंक्ति "
           "में नहीं, कुछ जोड़ा नहीं गया। सन्धि जाँची: च + अत्र → चात्र (अ + अ → आ)।"),
    "39": ("श्लोक (अनुष्टुभ्); विश्वास मध्यम; दो छपी पंक्तियाँ (०२.०९.४५ और ०२.०९.४६) जोड़ी गईं; कोई पाठ-चिह्न नहीं। सिरा = नस, "
           "वाहिनी (सम्भावित, सामान्य शब्द)। ‘बस्तिशीर्ष’ शाब्दिक: मूत्राशय का ऊपरी भाग या उसके ऊपर का निचला पेट, पाठ तय नहीं करता। "
           "‘षण्मासान्’ अवधि की द्वितीया। छपा ‘वाषण्मासान्न’ = वा + षण्मासान् + न (बिना जगह)। सन्धि जाँची: यस्य + अपूर्वाः → "
           "यस्यापूर्वाः (अ + अ → आ); सिरालेखाः + बाल- → सिरालेखा बाल- (आः + घोष → आ); बाल + इन्दु → बालेन्दु (अ + इ → ए); सदृश्यः + अपि → "
           "सदृश्योऽपि (अः + अ → ओऽ); सः + जीवति → स जीवति (सः व्यंजन से पहले विसर्ग खोता है)।"),
}

# ================================================================ AIDS
AIDS = {
    "27": {
        "frame": "किसका: यस्य → क्या: उत्सिक्तं मेढ्रम् (सूजा) · वा: वृषणौ अत्यिनिःसृतौ (छपा; सम्भवतः अतिनिःसृतौ: बहुत बाहर निकले) · वा: अतः विपर्ययः (इससे उलटा)।",
        "chunks": "यस्योत्सिक्तं | मेढ्रमत्यिनिःसृतौ वा | वृषणावतो | विपर्ययो वा",
        "sandhi": ("अ + उ → ओ: यस्य + उत्सिक्तम् → यस्योत्सिक्तम् · औ + स्वर → आव्: वृषणौ + अतः → वृषणावतः · अः + घोष व्यंजन → ओ: "
                   "अतः + विपर्ययः → अतो विपर्ययः।"),
    },
    "28": {
        "chunks": "यस्य | मूत्रमत्युग्रं",
        "sandhi": "इ + भिन्न स्वर → य्: अति + उग्रम् → अत्युग्रम् · म् + स्वर जुड़ता है: मूत्रम् + अति → मूत्रमति।",
        "anchors": "पक्का: मूत्र अति-उग्र। खुला: उग्रता गन्ध की या तीखेपन की, पाठ नहीं बताता। (मेरी याद-पद्धति)",
    },
    "29": {
        "diagram": {"groups": [
            {"label": "पहला लक्षण", "items": ["विषदोषाद्विना: विष के दोष के बिना", "खेभ्यः सरोमकूपेभ्यो: छिद्रों से, रोमकूपों सहित",
                                            "रक्तं प्रबर्तते: रक्त बहता है"]},
            {"label": "दूसरा लक्षण", "items": ["अनिमित्तम्: बिना कारण", "अंग अतिलघु या अतिगुरु", "स मुमूर्षुः: वह मरणासन्न (पहले लक्षण को भी समेटे या नहीं, पाठ नहीं बताता)"]}]},
        "chunks": ("यस्य विषदोषाद्विना | खेभ्यः सरोमकूपेभ्यो | रक्तं प्रबर्तते || यस्यानिमित्तमंगान्यतिलघून्यतिगुरूणि वा स्युः | "
                   "स मुमूर्षुः"),
        "seesaw": "अतिलघूनि (बहुत हल्के) ⇄ अतिगुरूणि (बहुत भारी): दोनों इसी इकाई में; इनमें से कोई भी बिना कारण हो तो लक्षण।",
        "sandhi": ("घोष व्यंजन से पहले त् → द्: विषदोषात् + विना → विषदोषाद्विना · अः + घोष व्यंजन → ओ: सरोमकूपेभ्यः + रक्तम् → "
                   "सरोमकूपेभ्यो रक्तम् · इ + भिन्न स्वर → य्: अंगानि + अतिलघूनि → अंगान्यतिलघूनि।"),
    },
    "30": {
        "frame": "किसका: यस्य → क्या: स्वरः → कैसा: एक/अनेक, गद्गद, क्षाम, दीन → कैसे: सहसा (अचानक) → क्रिया: उपलभ्यते (सुनाई देता है)।",
        "chunks": "यस्यैकोऽनेको वा | स्वरो | गद्गदान्यक्तक्षामदीनो वा | सहसोपलभ्यते",
        "sandhi": ("अ + ए → ऐ: यस्य + एकः → यस्यैकः · अः + अ → ओऽ: एकः + अनेकः → एकोऽनेकः · अः + घोष व्यंजन → ओ: स्वरः + गद्गद- → "
                   "स्वरो गद्गद- · आ + उ → ओ: सहसा + उपलभ्यते → सहसोपलभ्यते।"),
    },
    "31": {
        "chunks": "यो वा | विवक्षुर्मुह्यति",
        "sandhi": "अः + घोष व्यंजन → ओ: यः + वा → यो वा · उः + घोष → उर्: विवक्षुः + मुह्यति → विवक्षुर्मुह्यति।",
        "anchors": "विवक्षु (बोलना चाहता, इकाई ३१) और मुमूर्षु (मरणासन्न, इकाई २९): दोनों इच्छार्थक रूप। (मेरी याद-पद्धति)",
    },
    "32": {
        "frame": "लक्षण १: वदतः (बोलते समय) → उरः रुजति (छाती दुखे) · लक्षण २: उच्छ्वासः → अतिदीर्घ, अतिह्रस्व, पूतिगन्धि, सुगन्धि।",
        "chunks": "यस्य वदतो | भृशमूर्ध्वमुरो रुजति || यस्योच्छ्वासोऽतिदीर्घोऽतिह्रस्वः | पूतिगंधिः सुगंधिर्वा",
        "contrast": "अतिदीर्घ ⇄ अतिह्रस्व (लम्बाई), पूतिगन्धि ⇄ सुगन्धि (गन्ध): दोनों जोड़े इसी इकाई में।",
        "sandhi": ("अः + घोष व्यंजन → ओ: उरः + रुजति → उरो रुजति · अ + उ → ओ: यस्य + उच्छ्वासः → यस्योच्छ्वासः · अः + अ → ओऽ: "
                   "उच्छ्वासः + अतिदीर्घः → उच्छ्वासोऽतिदीर्घः · इः + घोष → इर्: सुगन्धिः + वा → सुगन्धिर्वा।"),
    },
    "33": {
        "chunks": "यस्यांगुलय | आयम्यमाना | न स्फुटेयुः || यस्यान्योऽन्योऽपि | क्षुतगतमूत्रणादिषु | स्वभावातीतः शब्दः",
        "sandhi": ("अ + अ → आ: यस्य + अंगुलयः → यस्यांगुलयः · अः + अ-भिन्न स्वर → अ: अंगुलयः + आयम्यमानाः → अंगुलय आयम्यमानाः · "
                   "आः + घोष → आ: आयम्यमानाः + न → आयम्यमाना न।"),
        "anchors": "पक्का: खींचने पर उँगली न चटके; छींक, मूत्रत्याग आदि में शब्द असामान्य। संदिग्ध: ‘अन्योऽन्योऽपि’, ‘गत’ का अर्थ। (मेरी याद-पद्धति)",
    },
    "34": {
        "diagram": {"groups": [
            {"label": "गन्ध (प्रिय या अप्रिय), छपे क्रम में", "items": ["१ माल्य", "२ फल", "३ चन्दन", "४ कुणप", "आदि"]},
            {"label": "कहाँ, छपे क्रम में", "items": ["१ देह", "२ मुख", "३ मल", "४ व्रण", "५ वस्त्र", "आदि"]}]},
        "chunks": "यस्येष्टोऽनिष्टो वा | माल्यफलचंदनकुणपादिगंधो | देहमुखमलव्रणवस्त्रादिषु",
        "seesaw": "इष्ट (प्रिय) ⇄ अनिष्ट (अप्रिय): दोनों इसी इकाई में; दोनों प्रकार की गन्ध रिष्ट।",
        "sandhi": ("अ + इ → ए: यस्य + इष्टः → यस्येष्टः · अः + अ → ओऽ: इष्टः + अनिष्टः → इष्टोऽनिष्टः · अ + आ → आ: कुणप + आदि → "
                   "कुणपादि।"),
    },
    "35": {
        "diagram": {"groups": [
            {"label": "कारण (पंचमी)", "items": ["वैरूप्यात्: विरूपता से", "सौरस्यात्: सुरसता से"]},
            {"label": "जीव क्या करते हैं", "items": ["त्यजन्ते: छोड़ते हैं", "भजन्ति: आश्रय लेते हैं"]},
            {"label": "जोड़ी", "items": ["कौन-सा कारण किस क्रिया से, पाठ नहीं बताता"]}]},
        "chunks": "यस्य शरीरं | वैरूप्यात्सौरस्याद्वाऽत्यर्थं | यूका मक्षिकादयस्त्यजंते | भजंति वा",
        "sandhi": ("घोष व्यंजन से पहले त् → द्: सौरस्यात् + वा → सौरस्याद्वा (स से पहले त् वैसा ही: वैरूप्यात्सौरस्यात्) · आः + घोष → आ: "
                   "यूकाः + मक्षिका- → यूका मक्षिका- · त से पहले विसर्ग → स्: मक्षिकादयः + त्यजन्ते → मक्षिकादयस्त्यजन्ते।"),
    },
    "36": {
        "chain": {"steps": ["१ सदा गर्म अंगों में ठण्डक", "२ ठण्डे अंगों में अति शीतलता (कुमुद, सम्भवतः श्वेत कुमुदिनी, और उत्पल, सम्भवतः नीलकमल, जैसी)", "३ अति स्वेद",
                            "४ अति स्तम्भ", "५ ढीलापन, मानो मांस-रक्त गए (स्त्रंसः, सम्भवतः स्रंसः)"]},
        "chunks": "यस्य सततोष्मस्वंगावयवेषु शैत्यं | शीतेषु वा | कुमुदोत्पलानुकार्यातिशैत्यमतिस्वेदोऽतिस्तंभो | विगतमांसशोणितेष्विव च स्त्रंसः",
        "contrast": "सदा गर्म अंग → शैत्य ⇄ ठण्डे अंग → अति शैत्य: दोनों इसी इकाई में।",
        "sandhi": ("अ + उ → ओ: कुमुद + उत्पल → कुमुदोत्पल · अः + अ → ओऽ: अतिस्वेदः + अतिस्तम्भः → अतिस्वेदोऽतिस्तम्भः · उ + भिन्न स्वर "
                   "→ व्: शोणितेषु + इव → शोणितेष्विव।"),
    },
    "37": {
        "diagram": {"groups": [
            {"label": "सूची (डेटा: इकाई ३२ से ३६)", "items": ["छाती, उच्छ्वास", "उँगली, शब्द", "गन्ध", "जूँ-मक्खी", "ठण्डक, स्वेद, स्तम्भ"]},
            {"label": "इकाई ३७", "items": ["महाभूतों का योग या अतियोग, एक साथ", "सर्वे ते कालपक्वाः इति"]}]},
        "chunks": "यस्य च योगोऽतियोगो वा | शरीरे | युगपन्महाभूतानां | दृश्यते | सर्वे ते कालपक्वा इति",
        "sandhi": ("अः + अ → ओऽ: योगः + अतियोगः → योगोऽतियोगः · नासिक्य से पहले त् → न् वैकल्पिक (द् भी शुद्ध): युगपत् + महाभूतानाम् → "
                   "युगपन्महाभूतानाम् · आः + स्वर → आ: कालपक्वाः + इति → कालपक्वा इति।"),
    },
    "38": {
        "frame": "भवति (है) · च (और) · अत्र (इस विषय में) → आगे के श्लोक।",
        "chunks": "भवति | चात्र",
        "sandhi": "अ + अ → आ: च + अत्र → चात्र।",
    },
    "39": {
        "frame": "क्या: सिरालेखाः (अपूर्व या बालेन्दु जैसी) → कहाँ: ललाटे या बस्तिशीर्षे → फल: षण्मासान् न जीवति।",
        "diagram": {"groups": [
            {"label": "सिरा-रेखाएँ", "items": ["अपूर्वाः: पहले न देखी", "बालेन्दुसदृश्यः: बालचन्द्र जैसी"]},
            {"label": "स्थान", "items": ["ललाटे: माथे पर", "बस्तिशीर्षे: बस्ति के शीर्ष पर"]},
            {"label": "फल", "items": ["षण्मासान्न स जीवति: छह मास नहीं जीता"]}]},
        "chunks": "यस्यापूर्वाः सिरालेखा | बालेंदुसदृश्योऽपि वा | ललाटे बस्तिशीर्षे | वाषण्मासान्न स जीवति",
        "sandhi": ("आः + घोष → आ: सिरालेखाः + बाल- → सिरालेखा बाल- · अ + इ → ए: बाल + इन्दु → बालेन्दु · अः + अ → ओऽ: सदृश्यः + अपि → "
                   "सदृश्योऽपि · सः + व्यंजन → स: सः + जीवति → स जीवति।"),
    },
}

# ================================================================ IMAGE_SPECS
IMAGE_SPECS = {
    ("29", "diagram"): {
        "file": "sh9-mumurshu-29.svg",
        "alt": ("Split of card 29: first sign, blood flowing from the orifices with the hair-pores without poison; second "
                "sign, limbs too light or too heavy without cause, he is mumūrṣu (about to die); whether this also covers the first sign is not stated."),
        "type": "split",
        "title": "कार्ड २९: दो लक्षण",
        "cols": [["रक्तस्राव", ["विष के दोष के बिना", "छिद्रों से, रोमकूपों सहित", "रक्त बहता है"]],
                 ["अंग", ["बिना कारण", "अति हल्के या अति भारी", "स मुमूर्षुः: मरणासन्न (पहले लक्षण पर भी? पाठ नहीं बताता)"]]],
    },
    ("32", "contrast"): {
        "file": "sh9-ucchvasa-32.svg",
        "alt": ("Split of card 32: four faults of the exhalation in two pairs: too long or too short; foul-smelling or "
                "sweet-smelling."),
        "type": "split",
        "title": "कार्ड ३२: उच्छ्वास के चार विकार",
        "cols": [["लम्बाई", ["अतिदीर्घ: बहुत लम्बा", "अतिह्रस्व: बहुत छोटा"]],
                 ["गन्ध", ["पूतिगन्धि: दुर्गन्ध", "सुगन्धि: सुगन्ध"]]],
    },
    ("34", "diagram"): {
        "file": "sh9-gandha-34.svg",
        "alt": ("Split of card 34 in printed order: the smell, pleasant or unpleasant, of garlands, fruits, sandalwood, "
                "corpses and the like; found in body, mouth, waste, wound, clothes and the like."),
        "type": "split",
        "title": "कार्ड ३४: गन्ध (प्रिय या अप्रिय)",
        "cols": [["किसकी गन्ध", ["१ माल्य: माला", "२ फल", "३ चन्दन", "४ कुणप: शव", "आदि"]],
                 ["कहाँ", ["१ देह", "२ मुख", "३ मल", "४ व्रण: घाव", "५ वस्त्र", "आदि"]]],
    },
    ("35", "diagram"): {
        "file": "sh9-yuka-35.svg",
        "alt": ("Split of card 35: two causes, deformity and good flavour; two actions of lice and flies, abandoning and "
                "resorting to; which cause goes with which action is not stated."),
        "type": "split",
        "title": "कार्ड ३५: जोड़ी पाठ में नहीं",
        "cols": [["कारण", ["वैरूप्य: विरूपता", "सौरस्य: सुरसता"]],
                 ["जूँ, मक्खी आदि", ["त्यजन्ते: छोड़ती हैं", "भजन्ति: आश्रय लेती हैं"]]],
    },
    ("36", "chain"): {
        "file": "sh9-shaitya-36.svg",
        "alt": ("Chain of card 36 in printed order: coldness in always-warm limbs; excessive coldness in cold limbs; "
                "excessive sweat; excessive stiffness; slackness as if flesh and blood had gone (reading straṃsa, "
                "possibly sraṃsa)."),
        "type": "chain",
        "title": "कार्ड ३६: अंगों के पाँच लक्षण",
        "steps": ["१ सदा गर्म अंगों में ठण्डक", "२ ठण्डे अंगों में अति शीतलता", "३ अति स्वेद: पसीना",
                  "४ अति स्तम्भ: अकड़न", "५ ढीलापन (पाठ स्त्रंसः, सम्भवतः स्रंसः)"],
    },
    ("37", "diagram"): {
        "file": "sh9-kalapakva-37.svg",
        "alt": ("Flowchart of card 37: the signs of cards 32 to 36 and the conjunction or excessive conjunction of the "
                "great elements seen at one time all lead to: all those are ripened by time."),
        "type": "mermaid",
        "code": ("flowchart TD\n"
                 "  A[\"कार्ड ३२ से ३६ के लक्षण\"] --> C[\"सर्वे ते कालपक्वाः\"]\n"
                 "  B[\"महाभूतों का योग या अतियोग\"] --> C\n"
                 "  C --> D[\"इति: सूची समाप्त\"]\n"),
    },
    ("39", "diagram"): {
        "file": "sh9-siralekha-39.svg",
        "alt": ("Flowchart of card 39: vein-lines never seen before, or like the young moon, on the forehead or at the "
                "head of the bladder: he does not live six months."),
        "type": "mermaid",
        "code": ("flowchart TD\n"
                 "  A[\"अपूर्व सिरा-रेखाएँ\"] --> P[\"ललाट या बस्तिशीर्ष पर\"]\n"
                 "  B[\"बालचन्द्र जैसी रेखाएँ\"] --> P\n"
                 "  P --> R[\"छह मास नहीं जीता\"]\n"),
    },
}
