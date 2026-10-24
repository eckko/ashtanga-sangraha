from helpers import mcq, match, order, fill, multi, accepts


AUTHORED = {}

# ---------------------------------------------------------------- unit 64
AUTHORED["64"] = {
    "title": "जन्मकाले तु",
    "question": "By unit 64, how does the child come out at birth, and what follows it?",
    "rule": ("At birth, through contact with the wind of parturition (prasūti-māruta), the child turns round and comes out "
             "head downward (अवाक्शिराः); afterwards the aparā (placenta) comes out, detached from the mother's heart."),
    "limits": ("Prose. That prasūti-māruta means the contractions of labour is probable only; the text says wind of "
               "parturition. The aparā comes away from the mother's heart as printed; the card does not reinterpret it. "
               "The verb निष्क्रामति is understood again with अपरा; the child is the unstated subject."),
    "explain_hi": ("यह गद्य-पंक्ति जन्म के समय का क्रम बताती है। प्रसूति-मारुत यानी प्रसव की वायु के संयोग से गर्भ पलटता है "
                   "(परिवृत्त्या) और सिर नीचे किए (अवाक्शिराः) बाहर निकलता है। उसके बाद अपरा यानी जेर माता के हृदय से अलग होकर "
                   "निकलती है; दूसरे खण्ड में ‘निष्क्रामति’ फिर से समझा जाता है, लिखा नहीं गया। "
                   "प्रसूति-मारुत को आधुनिक प्रसव-संकुचन मानना सम्भावित है, ग्रन्थ में कहा नहीं गया। "
                   "‘अवाक्शिराः’ बहुव्रीहि है: जिसका सिर नीचे की ओर हो।"),
    "hook": "प्रसव-वायु → पलटना → सिर नीचे बाहर; फिर अपरा।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 64, in what position does the child come out at birth?",
            ("Head downward (अवाक्शिराः)", "अवाक्शिराः निष्क्रामति: he comes out head downward, after turning round."),
            [("Feet first, head last", "The unit says head downward, not feet first."),
             ("Lying sideways across", "No sideways position is named in unit 64."),
             ("Face upward, head last", "The head comes first: अवाक्शिराः.")],
            "After turning round (परिवृत्त्या), the child comes out head downward.",
            "अवाक्शिराः = with head downward."),
        order(1, "Put these words of unit 64 in the line's order.",
              ["जन्मकाले", "प्रसूतिमारुतयोगात्", "परिवृत्त्या", "अवाक्शिराः", "निष्क्रामति", "अपरा च्युता"],
              "At birth, through contact with the wind of parturition, by turning round, head downward, he comes out; "
              "then the aparā, detached.",
              "जन्मकाले → प्रसूतिमारुतयोगात् → परिवृत्त्या → अवाक्शिराः → निष्क्रामति → अपरा च्युता."),
        match(2, "Match each word of unit 64 to its meaning.",
              [["प्रसूतिमारुत", "wind of parturition"], ["परिवृत्त्या", "by turning round"],
               ["अवाक्शिराः", "head downward"], ["अपरा", "placenta"], ["च्युता", "detached"]],
              "These five words carry the whole sequence of the birth.",
              "प्रसूतिमारुत, परिवृत्ति, अवाक्शिराः, अपरा, च्युता.", role="extend",
              teaches="अवाक्शिराः is a bahuvrīhi: अवाक् (downward) + शिरस् (head) = one whose head is downward."),
        mcq("discriminate", 3, "Which split of निष्क्रामत्यनु is right?",
            ("निष्क्रामति + अनु", "इ before a different vowel becomes य्: निष्क्रामति + अनु → निष्क्रामत्यनु."),
            [("निष्क्रामते + अनु", "ए + अ would give निष्क्रामतेऽनु, with ए kept."),
             ("निष्क्रामत् + यनु", "यनु is not a word; the particle is अनु."),
             ("निष्क्रामत्य + नु", "निष्क्रामत्य is not a verb form; the verb is निष्क्रामति.")],
            "निष्क्रामति (comes out) + अनु (afterwards): इ + अ → य.",
            "इ + a different vowel → य् + that vowel."),
        mcq("apply", 4, "By unit 64, from where does the aparā (placenta) come away?",
            ("From the mother's heart", "मातृहृदयात् च्युता: detached from the mother's heart, as printed."),
            [("From the child's navel", "No navel is named in unit 64."),
             ("From the mother's belly", "The printed word is हृदय, heart, not belly."),
             ("From the channels of rasa", "Channels are not named in unit 64.")],
            "The line ends अपरा च्युता मातृहृदयात्: the aparā, detached from the mother's heart.",
            "मातृहृदयात् = from the mother's heart (ablative)."),
        mcq("transfer", 5, "By the rule of अवाक्शिरा निष्क्रामति, how is बालाः + गच्छन्ति (the boys go) written?",
            ("बाला गच्छन्ति", "After आ the visarga drops before a voiced consonant, as अवाक्शिराः + निष्क्रामति."),
            [("बालो गच्छन्ति", "ओ comes from a visarga after short अ, not after आ."),
             ("बालार्गच्छन्ति", "The visarga becomes र् only after vowels other than अ and आ."),
             ("बालाश्गच्छन्ति", "The visarga becomes श् only before च, छ or श.")],
            "बालाः + गच्छन्ति = बाला गच्छन्ति, like अवाक्शिराः + निष्क्रामति = अवाक्शिरा निष्क्रामति.",
            "आः before a voiced consonant → आ (visarga dropped).",
            teaches="A visarga after आ is dropped before a voiced consonant: अवाक्शिराः + निष्क्रामति → अवाक्शिरा निष्क्रामति."),
    ],
}

# ---------------------------------------------------------------- unit 65
AUTHORED["65"] = {
    "title": "एषा प्रकृतिः",
    "question": "What does unit 65 call the course of birth described in unit 64?",
    "rule": ("एषा प्रकृतिः: this is the natural state. प्रकृति here is the natural, normal course of things; "
             "the copula (is) is understood."),
    "limits": ("Two words, prose. प्रकृति here is not the doctrinal prakṛti of body constitution. The line itself says "
               "only that this is the natural state; its counterpart comes in the next unit."),
    "explain_hi": ("दो शब्दों की यह गद्य-पंक्ति पिछली इकाई के जन्म-क्रम को ‘प्रकृति’ कहती है: यह स्वाभाविक अवस्था है। "
                   "यहाँ ‘प्रकृति’ का अर्थ सामान्य, स्वाभाविक क्रम है, शरीर की प्रकृति (देह-स्वभाव) नहीं। "
                   "क्रिया ‘है’ लिखी नहीं गई, समझी जाती है। "
                   "‘एषा’ स्त्रीलिंग है, क्योंकि ‘प्रकृतिः’ स्त्रीलिंग शब्द है।"),
    "hook": "पलटकर, सिर नीचे जन्म: एषा प्रकृतिः, यही स्वाभाविक है।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "What does unit 65 call the course of birth described in unit 64?",
            ("The natural state (प्रकृति)", "एषा प्रकृतिः: this is the natural state."),
            [("An abnormality (विकृति)", "विकृति is the word of unit 66, for the other case."),
             ("A disease of Vāta", "No disease is named in unit 65."),
             ("A rare event", "The line calls it the natural, normal state.")],
            "The birth of unit 64 is called प्रकृति, the natural state.",
            "एषा प्रकृतिः = this is the natural state."),
        mcq("warmup", 1, "In unit 65, what does प्रकृति mean?",
            ("The natural, normal course", "The card reads प्रकृति here as the normal course of things."),
            [("A person's body constitution", "The data notes say it is not the constitution term here."),
             ("The mother's own temperament", "No temperament of the mother is named."),
             ("A medicine given at birth", "No medicine is named in unit 65.")],
            "प्रकृति in this line = the natural, normal state.",
            "प्रकृति here = the natural course, not body constitution."),
        fill(2, "This is the natural state: एषा ____ (type it in Devanagari or in English letters, e.g. dharma).",
             accepts("प्रकृतिः"),
             "The line is एषा प्रकृतिः.",
             "प्रकृति = the natural, normal state; its counterpart विकृति (deviation) is named in unit 66.",
             "एषा प्रकृतिः = this is the natural state."),
        mcq("discriminate", 3, "Which grammar label does the card give एषा?",
            ("Feminine nominative singular: this", "The card labels एषा f. nom. sg."),
            [("Masculine nominative singular: this", "The masculine form is एषः."),
             ("Neuter nominative singular: this", "The neuter form is एतत्."),
             ("Feminine accusative singular: this", "The accusative form is एताम्.")],
            "एषा = this, feminine nominative singular, with the feminine noun प्रकृतिः.",
            "एषा = f. nom. sg. of this."),
        multi("apply", 4, "Which statements about unit 65 are right?",
              [("The line prints a verb meaning is", "No verb is printed; is is understood."),
               ("The copula is understood, not printed", "Right: only two words, no verb."),
               ("प्रकृति here means the normal course", "Right: not the constitution term."),
               ("It is a metrical verse line", "It is a prose unit, not a verse.")],
              [1, 2],
              "Two words of prose, the copula understood, प्रकृति in its plain sense of natural state.",
              "एषा प्रकृतिः: prose, copula understood."),
        mcq("transfer", 5, "Built like एषा प्रकृतिः, which word fits the invented line ____ सुखम् (this is happiness), सुखम् being neuter?",
            ("एतत्", "A neuter noun takes the neuter this: एतत् सुखम्."),
            [("एषा", "एषा is feminine, as with प्रकृतिः."),
             ("एताम्", "एताम् is an accusative, not the subject."),
             ("एषाम्", "एषाम् is a genitive plural, of these.")],
            "एतत् सुखम्, as एषा प्रकृतिः: the pronoun takes the noun's gender.",
            "this: एषः (m.), एषा (f.), एतत् (n.).",
            teaches="The pronoun this takes the gender of its noun: एषा प्रकृतिः (f.), एतत् सुखम् (n.)."),
    ],
}

# ---------------------------------------------------------------- unit 66
AUTHORED["66"] = {
    "title": "विकृतिरतोऽन्यथा",
    "question": "What does unit 66 call any course other than the natural one?",
    "rule": ("विकृतिः अतः अन्यथा: otherwise than this is abnormality (vikṛti). अतः = than this, pointing back to the "
             "natural state of unit 65."),
    "limits": ("Three words, prose; the copula is understood. The line names no particular abnormal birth and no "
               "disease; it only says that what is otherwise is vikṛti."),
    "explain_hi": ("यह पंक्ति पिछली ‘एषा प्रकृतिः’ का प्रतिरूप है: इससे अन्यथा जो हो, वह विकृति यानी असामान्य अवस्था है। "
                   "‘अतः’ का अर्थ यहाँ ‘इससे’ है, यानी ऊपर कही स्वाभाविक अवस्था से। "
                   "किस प्रकार का असामान्य जन्म, यह पंक्ति नहीं बताती। "
                   "सन्धि: विकृतिः + अतः → विकृतिरतः (इ के बाद विसर्ग स्वर से पहले र्), अतः + अन्यथा → अतोऽन्यथा (अः + अ → ओऽ)।"),
    "hook": "अतः अन्यथा = विकृति: स्वाभाविक से हटकर जो हो।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 66, what is called vikṛti (abnormality)?",
            ("Whatever goes otherwise than this", "अतः अन्यथा: otherwise than this, the natural state."),
            [("Only a birth with the feet first", "The line names no particular kind of birth."),
             ("The natural state of unit 65", "That is प्रकृति, its counterpart."),
             ("A disease of the mother", "No disease is named in unit 66.")],
            "Anything otherwise than the natural state is vikṛti.",
            "विकृतिः अतः अन्यथा = otherwise than this is abnormality."),
        order(1, "Put the words of unit 66 in the line's order.",
              ["विकृतिः", "अतः", "अन्यथा"],
              "Abnormality, than this, otherwise.",
              "विकृतिः → अतः → अन्यथा."),
        match(2, "Match each word of unit 66 to its meaning.",
              [["विकृतिः", "abnormality"], ["अतः", "than this"], ["अन्यथा", "otherwise"]],
              "Three words make the whole line.",
              "विकृति, अतः, अन्यथा.", role="extend",
              teaches="अतः here means than this; with अन्यथा (otherwise) it gives otherwise than this."),
        mcq("discriminate", 3, "Which split of विकृतिरतोऽन्यथा is right?",
            ("विकृतिः + अतः + अन्यथा", "Visarga after इ → र् before अ; अः + अ → ओऽ."),
            [("विकृती + अतः + अन्यथा", "ई + अ would give य्: विकृत्यतो."),
             ("विकृतिः + अते + अन्यथा", "ए + अ keeps ए: it would read विकृतिरतेऽन्यथा."),
             ("विकृतिः + अतः + न्यथा", "न्यथा is not a word; the word is अन्यथा.")],
            "विकृतिः (abnormality) + अतः (than this) + अन्यथा (otherwise).",
            "Visarga after इ → र् before a vowel; अः + अ → ओऽ."),
        mcq("apply", 4, "Why is अतः written अतो before अन्यथा in unit 66?",
            ("अः + अ → ओ, and the next अ drops (ऽ)", "अतः + अन्यथा → अतोऽन्यथा; ऽ marks the dropped अ."),
            [("A visarga becomes स् before a vowel", "A visarga does not become स् before a vowel."),
             ("अतो is a different word from अतः", "The card gives the word as अतः, than this."),
             ("A visarga becomes र् before any vowel", "र् comes after vowels other than अ/आ, as in विकृतिरतः.")],
            "अतः + अन्यथा = अतोऽन्यथा: अः before अ gives ओ, and the अ is marked by ऽ.",
            "अः + अ → ओऽ."),
        mcq("transfer", 5, "By the rule of विकृतिरतः, how is मतिः + अस्ति (there is thought) joined?",
            ("मतिरस्ति", "After इ a visarga becomes र् before a vowel, as विकृतिः + अतः → विकृतिरतः."),
            [("मत्यस्ति", "इ becomes य् only when no visarga stands after it."),
             ("मतिसस्ति", "A visarga does not become स् before a vowel."),
             ("मतिऽस्ति", "ऽ marks an अ dropped after ए or ओ, not here.")],
            "मतिः + अस्ति = मतिरस्ति, like विकृतिः + अतः = विकृतिरतः.",
            "Visarga after इ → र् before a vowel.",
            teaches="A visarga after a vowel other than अ or आ becomes र् before a vowel: विकृतिः + अतः → विकृतिरतः."),
    ],
}

# ---------------------------------------------------------------- unit 67
AUTHORED["67"] = {
    "title": "तत्र या दक्षिणं पादं",
    "question": "By unit 67, which signs does the text give for a woman who will bear a son, and what of the opposite?",
    "rule": ("She who puts the right foot forward first, whose right arm is strong, who has male-named longings and "
             "dreams, a clear face, keen hunger and an upward line of body-hair, bears a son; in the opposite case a girl; "
             "in a mixture a napuṃsaka."),
    "limits": ("Low confidence; the card reports this classical text's prognostic list, not a modern finding. "
               "Uncertain, and used for no question: the compound अत्युन्नततत्कुक्षिपरिमंडलगर्भा (belly raised, embryo round: "
               "conjectural), पुरुषानभिलाषिणी (desiring men, or not desiring men: two-way split), the extra त in "
               "चेष्टतेतस्तने, and whether प्राक् means the right breast."),
    "explain_hi": ("यह एक लम्बा गद्य-वाक्य है: जो स्त्री पहले दाहिना पैर आगे रखती है, जिसकी दाहिनी भुजा बलवान है, "
                   "पुरुष-नाम वालों को देखने-छूने-पूछने के दौर्हृद (गर्भावस्था की इच्छा) में रत है, पुरुष-नाम वाले स्वप्न देखती है, "
                   "जिसका मुख-वर्ण प्रसन्न, भूख तीव्र और रोम-पंक्ति ऊपर की ओर है, वह पुत्र को जन्म देती है। "
                   "इसके विपर्यय में कन्या, और मिश्रण (संकर) में नपुंसक; ‘प्रसूते’ इन दोनों के साथ फिर समझा जाता है। "
                   "बीच का कुक्षि-वाला समास और ‘पुरुषानभिलाषिणी’ का विभाग अनिश्चित हैं, इसलिए उन पर प्रश्न नहीं। "
                   "यह प्राचीन ग्रन्थ का कथन है।"),
    "hook": "दाहिना पैर, दाहिनी भुजा, पुरुष-नाम के स्वप्न → पुत्र; उलटा → कन्या; मिश्र → नपुंसक।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 67, which foot does the woman who bears a son put forward first?",
            ("The right foot", "दक्षिणं पादं पूर्वमभिहरति: she puts the right foot forward first."),
            [("The left foot", "The text says दक्षिणम्, right."),
             ("Both feet together", "One foot, the right, is named."),
             ("The text names no foot", "It names the right foot (दक्षिणं पादम्).")],
            "The first sign of the list: the right foot put forward first.",
            "दक्षिणं पादं पूर्वम् अभिहरति = puts the right foot forward first."),
        order(1, "Put these signs and the result of unit 67 in the text's order.",
              ["दक्षिणं पादं पूर्वमभिहरति", "दक्षिणश्च यस्या बाहुर्बलवान्", "पुन्नामधेयांश्च स्वप्नान् पश्यति",
               "प्रसन्नमुखवर्णा", "सा पुत्रं प्रसूते"],
              "Right foot, right arm, dreams with male names, clear face; then the result: she bears a son.",
              "पाद → बाहु → स्वप्न → मुखवर्ण → पुत्रं प्रसूते."),
        match(2, "Match each word of unit 67 to its meaning.",
              [["अभिहरति", "puts forward"], ["बलवान्", "strong"], ["दौर्हृद", "longing of pregnancy"],
               ["प्रसन्नमुखवर्णा", "with a clear complexion of the face"], ["स्वप्नान्", "dreams"]],
              "These words come from the sure parts of the list.",
              "अभिहरति, बलवान्, दौर्हृद, प्रसन्नमुखवर्णा, स्वप्नान्.", role="extend",
              teaches="दौर्हृद is the longing of pregnancy; here its objects are male-named ones."),
        mcq("discriminate", 3, "By unit 67, what is born in the opposite case (तद्विपर्यये)?",
            ("A girl (कन्या)", "तद्विपर्यये कन्याम्: in the opposite of that, a girl."),
            [("A napuṃsaka", "The napuṃsaka goes with a mixture (संकरे)."),
             ("A son", "A son goes with the signs themselves."),
             ("Twins", "Twins are not named in unit 67.")],
            "Signs → son; their opposite → girl; a mixture → napuṃsaka.",
            "तद्विपर्यये कन्यां संकरे च नपुंसकम्."),
        multi("apply", 4, "Which signs does unit 67 list for the woman who bears a son?",
              [("She puts the left foot forward first", "The text says the right foot."),
               ("Her right arm is strong", "Right: दक्षिणश्च ... बाहुर्बलवान्."),
               ("Her hunger is dull", "The text says keen hunger (तीक्ष्णक्षुत्)."),
               ("She sees dreams bearing male names", "Right: पुन्नामधेयांश्च स्वप्नान् पश्यति.")],
              [1, 3],
              "The right arm is strong and the dreams bear male names; foot and hunger are the other way.",
              "दक्षिण बाहु बलवान्; पुन्नामधेय स्वप्न; तीक्ष्ण क्षुत्."),
        mcq("transfer", 5, "By the rule of तद्विपर्यये, how is तत् + वचनम् (that word) joined?",
            ("तद्वचनम्", "A final त् before a voiced sound becomes द्, as तत् + विपर्यये → तद्विपर्यये."),
            [("तत्वचनम्", "Before the voiced व the त् does not stay त्."),
             ("तन्वचनम्", "त् becomes न् only before a nasal."),
             ("तच्वचनम्", "त् becomes च् only before च, छ or श.")],
            "तत् + वचनम् = तद्वचनम्, like तत् + विपर्यये = तद्विपर्यये.",
            "Final त् → द् before a voiced sound.",
            teaches="A final त् becomes द् before a voiced sound: तत् + विपर्यये → तद्विपर्यये."),
    ],
}

# ---------------------------------------------------------------- unit 68
AUTHORED["68"] = {
    "title": "प्रश्नकाले नारी",
    "question": "By unit 68, how is the embryo's sex declared from what the woman touches at the time of the question?",
    "rule": ("At the time of the question, whatever limb or external substance having a gender (liṅga) the woman "
             "touches, one should declare her embryo to be of that same gender."),
    "limits": ("The classical text's prognostic statement, reported as stated. The data reads printed यद्दिंगम् as यत्-लिङ्गम् "
               "(whichever gender); यल्लिंगम् is a possible correction (flagged); no question asks about that spelling or "
               "its sandhi. How a thing's gender is judged, and who declares, are not stated."),
    "explain_hi": ("प्रश्न के समय (प्रसंग से, गर्भ के विषय में पूछे जाने पर) स्त्री जिस लिंग वाले अंग या बाहरी द्रव्य को छूती है, "
                   "उसके गर्भ को उसी लिंग का बताना चाहिए। ‘आदिशेत्’ विधिलिङ् है: ‘बताए’; बताने वाला कौन है, लिखा नहीं। "
                   "किसी वस्तु का लिंग कैसे तय हो, ग्रन्थ नहीं बताता। "
                   "‘तल्लिंगम्’ में तत् + लिङ्गम् है (त् + ल → ल्ल)। यह प्राचीन ग्रन्थ का कथन है।"),
    "hook": "जो छुए उसका लिंग = गर्भ का लिंग (ग्रन्थ का कथन)।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 68, by what is the embryo's sex declared at the time of the question?",
            ("By the gender of what she touches", "तल्लिंगम् ... गर्भम् आदिशेत्: of the same gender as the thing touched."),
            [("By the dreams she reports that night", "Dreams belong to unit 67, not to this unit."),
             ("By the shape and height of her belly", "No belly is named in unit 68."),
             ("By the day on which the question falls", "No day is named, only the time of the question.")],
            "Whatever limb or external thing of a gender she touches, the embryo is declared of that gender.",
            "स्पर्श की वस्तु का लिंग = गर्भ का लिंग, as the text states."),
        order(1, "Put these words of unit 68 in the line's order.",
              ["प्रश्नकाले नारी", "बाह्यद्रव्यं वा", "परामृशति", "तल्लिंगमस्या", "गर्भमादिशेत्"],
              "At the time of the question, the woman ... or an external substance, touches; of that gender, her embryo, "
              "one should declare.",
              "प्रश्नकाले नारी → बाह्यद्रव्यं वा → परामृशति → तल्लिंगमस्या → गर्भमादिशेत्."),
        match(2, "Match each word of unit 68 to its meaning.",
              [["प्रश्नकाल", "time of the question"], ["अङ्ग", "limb"], ["बाह्यद्रव्य", "external substance"],
               ["परामृशति", "touches"], ["आदिशेत्", "should declare"]],
              "These five words carry the whole rule.",
              "प्रश्नकाल, अङ्ग, बाह्यद्रव्य, परामृशति, आदिशेत्.", role="extend",
              teaches="आदिशेत् is an optative (3 sg.): one should declare; its subject is not printed."),
        mcq("discriminate", 3, "Which split of तल्लिंगमस्या is right?",
            ("तत् + लिङ्गम् + अस्याः", "त् + ल → ल्ल; अस्याः drops its visarga before गर्भम्."),
            [("तल् + लिङ्गम् + अस्याः", "तल् is not a word; the pronoun is तत्."),
             ("तत् + लिङ्गम + स्याः", "स्याः is not a word of the card; the word is अस्याः."),
             ("तत् + लिङ्गमस् + याः", "लिङ्गमस् and याः are not words of the card.")],
            "तत् (that) + लिङ्गम् (gender) + अस्याः (her).",
            "त् + ल → ल्ल."),
        mcq("apply", 4, "By unit 68, if the woman touches a thing of female gender at the question, what is declared?",
            ("That her embryo is female", "तल्लिंगम्: the embryo is declared of that same gender."),
            [("That her embryo is male", "The embryo takes the gender of the thing touched."),
             ("That her embryo is neuter", "Neuter would follow a thing of neuter gender."),
             ("Nothing, as only limbs count", "An external substance (बाह्यद्रव्य) counts as well.")],
            "Same gender as the thing touched: here female.",
            "तल्लिंगमस्या गर्भमादिशेत्: the embryo is declared of the gender of the thing touched."),
        mcq("transfer", 5, "By the rule of तल्लिंगम्, how is तत् + लभते (gets that) joined?",
            ("तल्लभते", "त् before ल becomes ल्, as तत् + लिङ्गम् → तल्लिङ्गम्."),
            [("तद्लभते", "Before ल the त् becomes ल्, not द्."),
             ("तत्लभते", "The त् does not stay unchanged before ल."),
             ("तन्लभते", "त् becomes न् only before a nasal.")],
            "तत् + लभते = तल्लभते, like तत् + लिङ्गम् = तल्लिङ्गम्.",
            "त् + ल → ल्ल.",
            teaches="A final त् before ल becomes ल्: तत् + लिङ्गम् → तल्लिङ्गम्."),
    ],
}

# ---------------------------------------------------------------- unit 69
AUTHORED["69"] = {
    "title": "यदा तून्मार्गगो वातो",
    "question": "By unit 69, what happens when Vāta gone astray dries up the embryo's rasa-carrying channels?",
    "rule": ("When Vāta, gone astray (उन्मार्गग), dries up the channels (srotas) of the embryo that carry rasa, the child "
             "is born suffering from a Vāta disease (वातरोगी) and deficient (हीन)."),
    "limits": ("Prose. The text names no particular Vāta illness and does not say in what the child is deficient. "
               "The printed रसवाहिनी may stand for neuter रसवाहीनि (flagged); no question rests on the ending. "
               "The born child is the unstated subject of जायते."),
    "explain_hi": ("यह पंक्ति एक कारण-फल बताती है: जब अपने मार्ग से भटका वात गर्भ के रस ले जाने वाले स्रोतों को सुखा देता है, "
                   "तब बच्चा वातरोगी और हीन पैदा होता है। ‘हीन’ यानी कमी वाला; किस बात में कमी, नहीं कहा गया। "
                   "कोई विशेष रोग का नाम नहीं दिया गया। ‘शोषयति’ √शुष् का णिजन्त है: सुखा देता है। "
                   "सन्धि: तु + उन्मार्गगः → तून्मार्गगः (उ + उ → ऊ); उन्मार्गगः वातः → उन्मार्गगो वातो (अः → ओ घोष से पहले)।"),
    "hook": "भटका वात → रसवाही स्रोत सूखे → वातरोगी, हीन जन्म।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 69, what does the Vāta that has gone astray dry up?",
            ("The embryo's channels carrying rasa", "गर्भस्य रसवाहिनी स्रोतांसि शोषयति."),
            [("The mother's milk in her breast", "Milk is not named in unit 69."),
             ("The placenta (aparā) after birth", "The aparā is not named in this unit."),
             ("The seed of father and mother", "Seed (bīja) is not named in unit 69.")],
            "Vāta gone astray dries up the embryo's rasa-carrying channels.",
            "उन्मार्गगो वातः ... स्रोतांसि शोषयति."),
        order(1, "Put these words of unit 69 in the line's order.",
              ["यदा तु", "उन्मार्गगो वातो", "गर्भस्य", "रसवाहिनी स्रोतांसि", "शोषयति", "तदा वातरोगी हीनो जायते"],
              "When Vāta gone astray dries up the embryo's rasa-carrying channels, then he is born Vāta-diseased and deficient.",
              "यदा … शोषयति → तदा … जायते."),
        match(2, "Match each word of unit 69 to its meaning.",
              [["उन्मार्गग", "gone astray"], ["स्रोतस्", "channel"], ["शोषयति", "dries up"],
               ["वातरोगी", "suffering from a Vāta disease"], ["हीन", "deficient"]],
              "Cause (Vāta astray, channels dried) and result (वातरोगी, हीन).",
              "उन्मार्गग, स्रोतस्, शोषयति, वातरोगी, हीन.", role="extend",
              teaches="शोषयति is a causative of √शुष् (to dry): it makes dry, dries up."),
        mcq("discriminate", 3, "Which split of तून्मार्गगो is right?",
            ("तु + उन्मार्गगः", "उ + उ → ऊ; अः → ओ before the voiced व of वातः."),
            [("ते + उन्मार्गगः", "ए + उ does not give ऊ."),
             ("तो + उन्मार्गगः", "ओ + उ does not give ऊ."),
             ("तुन् + मार्गगः", "That would be written with a short उ: तुन्मार्ग.")],
            "तु (but) + उन्मार्गगः (gone astray): two उ sounds become one long ऊ.",
            "उ + उ → ऊ."),
        multi("apply", 4, "Which statements does the card make about unit 69?",
              [("It names no specific Vāta illness", "Right: only वातरोगी, suffering from a Vāta disease."),
               ("It says in what the child is deficient", "It does not say in what (हीन only)."),
               ("The channels dried are the mother's", "They are the embryo's (गर्भस्य)."),
               ("The Vāta has gone off its path", "Right: उन्मार्गगः.")],
              [0, 3],
              "Vāta off its path; no named illness; deficiency unspecified; the channels are the embryo's.",
              "उन्मार्गगो वातः; गर्भस्य स्रोतांसि; वातरोगी हीनः."),
        mcq("transfer", 5, "By the rule of उन्मार्गगो वातो, how is देवः + जयति (the god wins) written?",
            ("देवो जयति", "अः before a voiced consonant becomes ओ, as उन्मार्गगः + वातः → उन्मार्गगो वातः."),
            [("देव जयति", "After अ the visarga drops only before vowels other than अ."),
             ("देवर्जयति", "र् comes only after vowels other than अ and आ."),
             ("देवश्जयति", "श् comes only before च, छ or श.")],
            "देवः + जयति = देवो जयति, like हीनः + जायते = हीनो जायते.",
            "अः before a voiced consonant → ओ.",
            teaches="A visarga after short अ becomes ओ before a voiced consonant: हीनः + जायते → हीनो जायते."),
    ],
}

# ---------------------------------------------------------------- unit 70
AUTHORED["70"] = {
    "title": "बहूनि वा वर्षाण्युदरे",
    "question": "What further outcome does unit 70 give: how long may he stay in the belly?",
    "rule": ("बहूनि वा वर्षाणि उदरे तिष्ठति: or he stays in the belly (udara) for many years. बहूनि वर्षाणि is an "
             "accusative of time: for many years."),
    "limits": ("Prose. The line seems to continue unit 69 as a further outcome after तदा; the subject (the embryo) is "
               "not printed. उदर is the belly, not the disease udara; no illness is named."),
    "explain_hi": ("यह छोटी पंक्ति पिछली इकाई के ‘तदा’ के बाद का एक और फल लगती है: या वह बहुत वर्षों तक पेट में रहता है। "
                   "कर्ता (गर्भ) लिखा नहीं गया, पिछली इकाई से समझा जाता है। "
                   "‘उदर’ यहाँ पेट है, उदर-रोग नहीं। ‘बहूनि वर्षाणि’ द्वितीया है जो समय की अवधि बताती है: बहुत वर्षों तक। "
                   "सन्धि: वर्षाणि + उदरे → वर्षाण्युदरे (इ + उ → यु)।"),
    "hook": "या बहुत वर्ष पेट में ठहरा रहे (उदर = पेट)।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 70, for how long may he stay in the belly?",
            ("For many years", "बहूनि वर्षाणि: for many years."),
            [("For many months", "The text says वर्षाणि, years."),
             ("For nine days", "No days are named in unit 70."),
             ("For one year only", "बहूनि means many, not one.")],
            "बहूनि वा वर्षाण्युदरे तिष्ठति: or he stays in the belly for many years.",
            "बहूनि वर्षाणि = for many years."),
        order(1, "Put the words of unit 70 in the line's order.",
              ["बहूनि", "वा", "वर्षाणि", "उदरे", "तिष्ठति"],
              "Many, or, years, in the belly, stays.",
              "बहूनि → वा → वर्षाणि → उदरे → तिष्ठति."),
        match(2, "Match each word of unit 70 to its meaning.",
              [["बहूनि", "many"], ["वर्षाणि", "years"], ["उदरे", "in the belly"], ["तिष्ठति", "stays"]],
              "Four words carry the whole line; वा (or) seems to add it to the outcome of unit 69.",
              "बहूनि, वर्षाणि, उदरे, तिष्ठति.", role="extend",
              teaches="An accusative of time tells how long: बहूनि वर्षाणि = for many years."),
        mcq("discriminate", 3, "In unit 70, what does उदर mean?",
            ("The belly", "The card reads उदरे as in the belly, not as a disease."),
            [("The disease called udara", "The data notes say no illness is named here."),
             ("The mother's heart", "The heart (हृदय) is named in unit 64, not here."),
             ("A channel carrying rasa", "Channels are named in unit 69, not here.")],
            "उदरे = in the belly (locative).",
            "उदर here = belly."),
        mcq("apply", 4, "Which split of वर्षाण्युदरे is right?",
            ("वर्षाणि + उदरे", "इ before उ becomes य्: वर्षाणि + उदरे → वर्षाण्युदरे."),
            [("वर्षाणे + उदरे", "ए + उ does not give यु."),
             ("वर्षाण्य + उदरे", "अ + उ would give ओ: वर्षाण्योदरे."),
             ("वर्षाणु + दरे", "वर्षाणु and दरे are not words of the card.")],
            "वर्षाणि (years) + उदरे (in the belly): इ + उ → यु.",
            "इ + उ → यु."),
        mcq("transfer", 5, "By the rule of वर्षाण्युदरे, how is अस्ति + उदकम् (there is water) joined?",
            ("अस्त्युदकम्", "इ + उ → य् + उ, as वर्षाणि + उदरे → वर्षाण्युदरे."),
            [("अस्तीउदकम्", "The two vowels do not stand side by side; इ becomes य्."),
             ("अस्तोदकम्", "इ + उ does not give ओ."),
             ("अस्तूदकम्", "The इ is not lost; it becomes य्.")],
            "अस्ति + उदकम् = अस्त्युदकम्, like वर्षाणि + उदरे = वर्षाण्युदरे.",
            "इ + a different vowel → य् + that vowel.",
            teaches="A final इ before a different vowel becomes य्: वर्षाणि + उदरे → वर्षाण्युदरे."),
    ],
}

# ---------------------------------------------------------------- unit 71
AUTHORED["71"] = {
    "title": "यदा स्त्रीपुंसयोः",
    "question": "What condition does unit 71 state about the woman and the man?",
    "rule": ("यदा स्त्रीपुंसयोः समम् अर्थः निष्पद्यते: when the purpose (artha) is accomplished equally for woman and man. "
             "स्त्रीपुंसयोः is a dvandva in the dual."),
    "limits": ("Prose; an unfinished condition: its result is not in this unit, and what the purpose is is not stated. "
               "स्त्रीपुंसयोः can be genitive or locative (of / in woman and man); no question rests on the case."),
    "explain_hi": ("यह पंक्ति केवल एक शर्त है: जब स्त्री और पुरुष दोनों का अर्थ (प्रयोजन) समान रूप से सिद्ध होता है। "
                   "इसका फल इस इकाई में नहीं है; वाक्य आगे चलता है, और ‘अर्थ’ क्या है, यह भी नहीं कहा गया। "
                   "‘स्त्रीपुंसयोः’ द्वन्द्व समास, द्विवचन है: स्त्री और पुरुष दोनों; यह षष्ठी या सप्तमी दोनों हो सकता है। "
                   "सन्धि: समम् + अर्थः → सममर्थः; अर्थः + निष्पद्यते → अर्थो निष्पद्यते (अः → ओ घोष से पहले)।"),
    "hook": "दोनों का अर्थ समान सिद्ध हो, तब... (फल आगे)।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 71, for whom is the purpose accomplished equally?",
            ("For the woman and the man", "स्त्रीपुंसयोः समम्: equally for woman and man."),
            [("For the woman alone", "Both are named: स्त्री and पुंस्."),
             ("For the man alone", "Both are named in one dual compound."),
             ("For the physician", "No physician is named in unit 71.")],
            "The condition concerns both woman and man, equally (समम्).",
            "स्त्रीपुंसयोः समम् = equally for woman and man."),
        order(1, "Put the words of unit 71 in the line's order.",
              ["यदा", "स्त्रीपुंसयोः", "समम्", "अर्थः", "निष्पद्यते"],
              "When, for woman and man, equally, the purpose, is accomplished.",
              "यदा → स्त्रीपुंसयोः → समम् → अर्थः → निष्पद्यते."),
        match(2, "Match each word of unit 71 to its meaning.",
              [["यदा", "when"], ["स्त्रीपुंसयोः", "woman and man (the two)"], ["समम्", "equally"],
               ["अर्थः", "purpose"], ["निष्पद्यते", "is accomplished"]],
              "Five words make the whole condition.",
              "यदा, स्त्रीपुंसयोः, समम्, अर्थः, निष्पद्यते.", role="extend",
              teaches="स्त्रीपुंसयोः is a dvandva in the dual: woman and man, the two together."),
        mcq("discriminate", 3, "What kind of form does the card call स्त्रीपुंसयोः?",
            ("A dvandva in the dual: woman and man", "The card labels it a dvandva, dual."),
            [("A plural meaning many women", "The ending is dual, for two persons."),
             ("A tatpuruṣa: the man's woman", "The card calls it a dvandva, woman and man."),
             ("A singular meaning one woman", "Two persons are named; it is dual.")],
            "स्त्री + पुंस् joined as a dvandva, in the dual.",
            "स्त्रीपुंसयोः = dvandva, dual."),
        multi("apply", 4, "Which statements about unit 71 are right?",
              [("Both woman and man are named", "Right: स्त्रीपुंसयोः."),
               ("The unit says what the purpose is", "It does not say what the artha is."),
               ("The purpose is accomplished equally", "Right: समम् ... निष्पद्यते."),
               ("It gives the age of the woman", "No age is given in unit 71.")],
              [0, 2],
              "Both are named and the purpose is accomplished equally; what the purpose is, is not said.",
              "स्त्रीपुंसयोः समम् अर्थः निष्पद्यते."),
        mcq("transfer", 5, "By the rule of सममर्थः, how is फलम् + अस्ति (there is fruit) joined?",
            ("फलमस्ति", "A final म् before a vowel stays म् and joins it, as समम् + अर्थः → सममर्थः."),
            [("फलंअस्ति", "Anusvara stands only before a consonant, not a vowel."),
             ("फलास्ति", "The म् is not lost before a vowel."),
             ("फलोऽस्ति", "ओऽ comes from अः + अ, not from अम्.")],
            "फलम् + अस्ति = फलमस्ति, like समम् + अर्थः = सममर्थः.",
            "Final म् + vowel → म joined with the vowel.",
            teaches="A final म् before a vowel stays म् and joins the vowel: समम् + अर्थः → सममर्थः."),
    ],
}

# ---------------------------------------------------------------- unit 72
AUTHORED["72"] = {
    "title": "बीजं वा तयोः",
    "question": "What alternative condition does unit 72 give about the seed (bīja) of the two?",
    "rule": ("बीजं वा तयोः समांशं संमुखं च: or the seed (bīja) of the two is of equal portion and face to face. "
             "समांश = सम + अंश, of equal portion."),
    "limits": ("Prose and elliptical; the copula is understood and no result is printed in this unit. bīja is the "
               "generative matter of each parent (probably semen and the female element); no exact modern term is forced."),
    "explain_hi": ("यह पंक्ति पिछली शर्त का विकल्प लगती है (‘वा’): या उन दोनों का बीज समान अंश वाला और आमने-सामने हो। "
                   "‘बीज’ यहाँ प्रत्येक माता-पिता का जनन-तत्त्व है (सम्भवतः शुक्र और स्त्री-तत्त्व); कोई सटीक आधुनिक नाम नहीं थोपा गया। "
                   "इस इकाई में कोई फल नहीं छपा; क्रिया ‘है’ समझी जाती है। "
                   "सन्धि: सम + अंशम् → समांशम् (अ + अ → आ); ‘संमुखं’ = सम्मुखम् (अनुस्वार म् के स्थान पर)।"),
    "hook": "दोनों का बीज: बराबर अंश, आमने-सामने।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 72, what is said of the seed (bīja) of the two?",
            ("Of equal portion and face to face", "समांशं संमुखं च."),
            [("Of unequal portion, turned away", "That is the opposite of समांश and संमुख."),
             ("Spoiled in one of its parts", "Spoiling in a part is in unit 73."),
             ("Dried up by Vāta gone astray", "Drying by Vāta is in unit 69.")],
            "The seed of the two is of equal portion (समांशम्) and face to face (संमुखम्).",
            "समांशं संमुखं च = of equal portion and face to face."),
        order(1, "Put the words of unit 72 in the line's order.",
              ["बीजम्", "वा", "तयोः", "समांशम्", "संमुखम्", "च"],
              "Seed, or, of the two, of equal portion, face to face, and.",
              "बीजम् → वा → तयोः → समांशम् → संमुखम् → च."),
        match(2, "Match each word of unit 72 to its meaning.",
              [["बीजम्", "seed"], ["तयोः", "of the two"], ["समांशम्", "of equal portion"], ["संमुखम्", "face to face"]],
              "Four words carry the description; वा and च link it.",
              "बीज, तयोः, समांश, संमुख.", role="extend",
              teaches="समांश = सम (equal) + अंश (portion): of equal portion."),
        mcq("discriminate", 3, "Which split of समांशम् is right?",
            ("सम + अंशम्", "अ + अ → आ: सम + अंशम् → समांशम्."),
            [("समम् + अंशम्", "A final म् before a vowel stays: it would give सममंशम्."),
             ("समः + अंशम्", "अः + अ would give ओऽ, not आ."),
             ("समे + अंशम्", "ए + अ keeps ए; it would give समेऽंशम्.")],
            "सम (equal) + अंशम् (portion): two short अ sounds become आ.",
            "अ + अ → आ."),
        mcq("apply", 4, "How does the card treat bīja (seed) in unit 72?",
            ("Seed of each parent; no exact modern term", "Probably semen and the female element; no modern term is forced."),
            [("The embryo already formed", "The card does not equate bīja with the embryo."),
             ("A plant seed used as medicine", "No medicine is named in unit 72."),
             ("The mother's blood alone", "The bīja is of the two (तयोः), not of one.")],
            "bīja = the generative matter of each parent; the card forces no modern equivalent.",
            "बीज = seed of each parent (no exact modern term)."),
        mcq("transfer", 5, "By the rule of समांशम्, how is हिम + अंशुः (cool-rayed, the moon) joined?",
            ("हिमांशुः", "अ + अ → आ, as सम + अंशम् → समांशम्."),
            [("हिमंशुः", "One अ is not simply dropped."),
             ("हिमेंशुः", "अ + अ does not give ए."),
             ("हिमोंशुः", "अ + अ does not give ओ.")],
            "हिम + अंशुः = हिमांशुः, like सम + अंशम् = समांशम्.",
            "अ + अ → आ.",
            teaches="Two short अ sounds meeting at a joint become one long आ: सम + अंशम् → समांशम्."),
    ],
}

# ---------------------------------------------------------------- unit 73
AUTHORED["73"] = {
    "title": "यदा च बीजं भागे दुष्यति",
    "question": "By unit 73, what comes to be when the seed is vitiated in a part?",
    "rule": ("When the seed (bīja) becomes vitiated in a part, then a napuṃsaka (neuter) comes to be, having two natures "
             "(द्विप्रकृति) and two seeds (द्विरेतस्)."),
    "limits": ("Prose. The text does not say which part of the seed is spoiled. That the two natures are male and "
               "female is suggested by the context, not stated. प्रकृति here is plain nature, not the constitution term. "
               "No question rests on the grammar labels of the two adjectives."),
    "explain_hi": ("यह पंक्ति कारण और फल बताती है: जब बीज किसी भाग में दूषित होता है, तब नपुंसक होता है, "
                   "जो द्विप्रकृति (दो प्रकृति वाला) और द्विरेतस् (दो रेतस् वाला) है। "
                   "दो प्रकृतियाँ सम्भवतः पुरुष और स्त्री की हैं, यह सन्दर्भ से लगता है, लिखा नहीं। "
                   "कौन सा भाग दूषित होता है, नहीं बताया गया; ‘प्रकृति’ यहाँ सामान्य अर्थ ‘स्वभाव’ में है। "
                   "सन्धि: द्विप्रकृतिः + द्विरेतः → द्विप्रकृतिर्द्विरेतः; द्विरेतः + नपुंसकम् → द्विरेतो नपुंसकम्।"),
    "hook": "बीज भाग में दूषित → द्विप्रकृति, द्विरेतस् नपुंसक।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 73, when does a napuṃsaka come to be?",
            ("When the seed is spoiled in a part", "बीजं भागे दुष्यति ... नपुंसकं भवति."),
            [("When the seed is of equal portion", "Equal portion is the wording of unit 72."),
             ("When Vāta dries up the channels", "That is unit 69, with another result."),
             ("When the woman touches a neuter thing", "That is the sign of unit 68, not a cause.")],
            "Vitiation of the seed in a part → a napuṃsaka with two natures and two seeds.",
            "बीजं भागे दुष्यति → नपुंसकम्."),
        order(1, "Put these words of unit 73 in the line's order.",
              ["यदा च बीजं", "भागे दुष्यति", "तदा", "द्विप्रकृतिर्द्विरेतो", "नपुंसकं भवति"],
              "When the seed is vitiated in a part, then a napuṃsaka of two natures and two seeds comes to be.",
              "यदा … दुष्यति → तदा … भवति."),
        match(2, "Match each word of unit 73 to its meaning.",
              [["भागे", "in a part"], ["दुष्यति", "becomes vitiated"], ["द्विप्रकृति", "having two natures"],
               ["द्विरेतस्", "having two seeds"], ["नपुंसक", "neuter"]],
              "Cause (दुष्यति in a part) and result (the napuṃsaka with two marks).",
              "भागे, दुष्यति, द्विप्रकृति, द्विरेतस्, नपुंसक.", role="extend",
              teaches="द्वि- in a bahuvrīhi: द्विप्रकृति = having two natures, द्विरेतस् = having two seeds."),
        mcq("discriminate", 3, "Which split of द्विप्रकृतिर्द्विरेतो is right?",
            ("द्विप्रकृतिः + द्विरेतः", "इः → इर् before the voiced द्; अः → ओ before the voiced न्."),
            [("द्विप्रकृती + द्विरेतः", "A final ई would not bring in a र्."),
             ("द्विप्रकृतिम् + द्विरेतः", "म् would give द्विप्रकृतिं द्विरेतः."),
             ("द्विप्रकृतिः + द्विरेते", "A final ए stays ए; it would not give ओ.")],
            "द्विप्रकृतिः (two natures) + द्विरेतः (two seeds).",
            "Visarga after इ → र् before a voiced sound; अः → ओ before a voiced sound."),
        multi("apply", 4, "Which statements about unit 73 are right?",
              [("The text names which part of the seed is spoiled", "It says only भागे, in a part."),
               ("प्रकृति here is the body-constitution term", "The notes say plain nature."),
               ("Male and female natures: suggested, not stated", "Right: the context suggests it; the text does not say so."),
               ("The napuṃsaka has two natures and two seeds", "Right: द्विप्रकृतिः, द्विरेतः.")],
              [2, 3],
              "Two natures (probably male and female, by context) and two seeds; the part is not named.",
              "द्विप्रकृति, द्विरेतस्; भागे only."),
        mcq("transfer", 5, "By the rule of द्विप्रकृतिर्द्वि, how is हरिः + गच्छति (Hari goes) written?",
            ("हरिर्गच्छति", "After इ a visarga becomes र् before a voiced consonant, as द्विप्रकृतिः + द्वि-."),
            [("हरि गच्छति", "After इ the visarga is not simply dropped."),
             ("हरिश्गच्छति", "श् comes only before च, छ or श."),
             ("हरिस्गच्छति", "स् comes only before त or थ.")],
            "हरिः + गच्छति = हरिर्गच्छति, like द्विप्रकृतिः + द्विरेतः = द्विप्रकृतिर्द्विरेतः.",
            "Visarga after इ → र् before a voiced consonant.",
            teaches="A visarga after a vowel other than अ or आ becomes र् before a voiced consonant: द्विप्रकृतिः + द्विरेतः → द्विप्रकृतिर्द्विरेतः."),
    ],
}

# ---------------------------------------------------------------- unit 74
AUTHORED["74"] = {
    "title": "यदा स्त्री प्रथमं कृतार्था",
    "question": "By unit 74, in what sequence of events does a vātendriya come to be?",
    "rule": ("When the woman first has her purpose accomplished, then afterwards the man's semen is emitted, and the "
             "Vāta of the woman, whose mind is unsteady with joy, vitiates and damages the virility-carrying channels: "
             "then a vātendriya comes to be."),
    "limits": ("Low confidence; a hard sentence. The object of विगुणीकरोति is not printed (taken as the semen: a "
               "conjecture); whose channels अस्य means is not stated; the ending of पुंस्त्ववाहिनी is doubtful. "
               "vātendriya is kept as printed (probably a kind of impotent person, not stated). No question rests on these."),
    "explain_hi": ("यह कठिन गद्य-वाक्य घटनाओं का क्रम बताता है: पहले स्त्री कृतार्था होती है, फिर बाद में पुरुष का शुक्र छूटता है, "
                   "और हर्ष से अस्थिर चित्त वाली स्त्री का वात विगुण करता है तथा पुंस्त्व ले जाने वाले स्रोतों को क्षति पहुँचाता है; "
                   "तब ‘वातेन्द्रिय’ होता है। विगुण किसे करता है, लिखा नहीं (शुक्र मानना अनुमान है); ‘अस्य’ किसका, नहीं कहा गया। "
                   "‘वातेन्द्रिय’ सम्भवतः नपुंसक का एक प्रकार है, यहाँ बताया नहीं गया। "
                   "सन्धि: पश्चात् + शुक्रम् → पश्चाच्छुक्रम् (त् + श → च्छ, जैसा छपा); वात + इन्द्रियम् → वातेन्द्रियम् (अ + इ → ए)।"),
    "hook": "स्त्री पहले, शुक्र बाद में, हर्ष-अस्थिर स्त्री का वात → वातेन्द्रिय।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 74, which partner first has the purpose accomplished?",
            ("The woman", "यदा स्त्री प्रथमं कृतार्था भवति."),
            [("The man", "The man's semen is emitted afterwards (पश्चात्)."),
             ("Both at once", "Equal accomplishment is the wording of unit 71."),
             ("It is not said", "The text says स्त्री प्रथमम्, the woman first.")],
            "The woman first (प्रथमम्), the man's semen afterwards (पश्चात्).",
            "स्त्री प्रथमं कृतार्था; पुरुषेण पश्चात् शुक्रम्."),
        order(1, "Put these parts of unit 74 in the text's order.",
              ["यदा स्त्री प्रथमं कृतार्था भवति", "ततः पुरुषेण पश्चाच्छुक्रमुत्सृष्टं", "हर्षानवस्थितचेतसः स्त्रिया वातो",
               "स्रोतांसि चोपहंति", "तदा वातेंद्रियं भवति"],
              "The woman first, then the man's semen, then the woman's Vāta, then the channels damaged, then the result.",
              "स्त्री प्रथमम् → पुरुषेण पश्चात् → स्त्रिया वातः → स्रोतांसि उपहन्ति → वातेन्द्रियम्."),
        match(2, "Match each word of unit 74 to its meaning.",
              [["कृतार्था", "one whose purpose is accomplished"], ["पश्चात्", "afterwards"], ["उत्सृष्टम्", "emitted"],
               ["हर्षानवस्थितचेतस्", "whose mind is unsteady with joy"], ["उपहन्ति", "damages"]],
              "These words come from the sure parts of the sentence.",
              "कृतार्था, पश्चात्, उत्सृष्टम्, हर्षानवस्थितचेतस्, उपहन्ति.", role="extend",
              teaches="कृतार्था is a bahuvrīhi: कृत (done) + अर्थ (purpose), she whose purpose is done."),
        mcq("discriminate", 3, "Which split of पश्चाच्छुक्रम् is right?",
            ("पश्चात् + शुक्रम्", "त् + श is written च्छ here: पश्चात् + शुक्रम् → पश्चाच्छुक्रम्."),
            [("पश्चा + शुक्रम्", "Without त् it would stay पश्चाशुक्रम्."),
             ("पश्चः + शुक्रम्", "A visarga before श would not give च्छ."),
             ("पश्चाम् + शुक्रम्", "A final म् would give पश्चां शुक्रम्.")],
            "पश्चात् (afterwards) + शुक्रम् (semen): त् + श → च्छ, as printed.",
            "त् + श → च्छ."),
        mcq("apply", 4, "By unit 74, what state is the woman's mind in?",
            ("Unsteady with joy", "हर्षानवस्थितचेतसः: whose mind is unsteady with joy."),
            [("Calm and steady", "अनवस्थित means unsteady, not steady."),
             ("Full of fear", "हर्ष is joy, not fear."),
             ("Heavy with grief", "हर्ष is joy, not grief.")],
            "हर्ष (joy) + अनवस्थित (unsteady) + चेतस् (mind).",
            "हर्षानवस्थितचेतस् = whose mind is unsteady with joy."),
        mcq("transfer", 5, "By the rule of पश्चाच्छुक्रम्, how may तत् + श्रुत्वा (having heard that) be written?",
            ("तच्छ्रुत्वा", "त् + श → च्छ, as पश्चात् + शुक्रम् → पश्चाच्छुक्रम्."),
            [("तद्श्रुत्वा", "त् does not become द् before the unvoiced श."),
             ("तस्श्रुत्वा", "त् does not become स् before श."),
             ("तञ्श्रुत्वा", "त् becomes a nasal only before a nasal.")],
            "तत् + श्रुत्वा = तच्छ्रुत्वा, like पश्चात् + शुक्रम् = पश्चाच्छुक्रम्.",
            "त् + श → च्छ.",
            teaches="A final त् before श can be written च्छ: पश्चात् + शुक्रम् → पश्चाच्छुक्रम्."),
    ],
}

# ---------------------------------------------------------------- unit 75
AUTHORED["75"] = {
    "title": "तन्मैथुने वातमेवोत्सृजति",
    "question": "By unit 75, what does it release in sexual union?",
    "rule": ("तत् मैथुने वातम् एव उत्सृजति: in sexual union it releases only Vāta. एव = only."),
    "limits": ("Prose. The subject तत् is carried from the preceding unit; what it refers to is not stated here, and "
               "no question rests on it. Vāta is kept as the humour; the line does not say whether plain wind is meant."),
    "explain_hi": ("यह पंक्ति पिछले वाक्य से जुड़ी है: ‘तत्’ (वह) का कर्ता पिछली इकाई से आता है; वह क्या है, यहाँ नहीं कहा गया। "
                   "वह मैथुन में केवल वात को छोड़ता है; ‘एव’ का अर्थ ‘केवल’ है। "
                   "वात को दोष के रूप में रखा गया; सामान्य वायु से तात्पर्य है या नहीं, पंक्ति नहीं बताती। "
                   "सन्धि: तत् + मैथुने → तन्मैथुने (त् → न् अनुनासिक से पहले, जैसा छपा); एव + उत्सृजति → एवोत्सृजति (अ + उ → ओ)।"),
    "hook": "मैथुन में केवल वात ही छोड़े (वातमेव)।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 75, what does it release in sexual union?",
            ("Only Vāta", "वातम् एव उत्सृजति: it releases only Vāta."),
            [("Only semen", "The line says वातम् एव, only Vāta."),
             ("Vāta and semen", "एव means only; one thing is named."),
             ("Nothing at all", "Vāta is released, so not nothing.")],
            "In sexual union it releases only Vāta.",
            "वातमेव = only Vāta."),
        order(1, "Put the words of unit 75 in the line's order.",
              ["तत्", "मैथुने", "वातम्", "एव", "उत्सृजति"],
              "That (one), in sexual union, Vāta, only, releases.",
              "तत् → मैथुने → वातम् → एव → उत्सृजति."),
        match(2, "Match each word of unit 75 to its meaning.",
              [["मैथुने", "in sexual union"], ["वातम्", "Vāta"], ["एव", "only"], ["उत्सृजति", "releases"]],
              "Four words after the subject तत्.",
              "मैथुने, वातम्, एव, उत्सृजति.", role="extend",
              teaches="एव after a word means only: वातम् एव = only Vāta."),
        mcq("discriminate", 3, "Which split of वातमेवोत्सृजति is right?",
            ("वातम् + एव + उत्सृजति", "म् joins the vowel; अ + उ → ओ."),
            [("वातम् + एवः + उत्सृजति", "अः before उ would drop the visarga and not join: एव उत्."),
             ("वातम् + इव + उत्सृजति", "म् + इव would give वातमिव, not वातमेव."),
             ("वातम् + एव + ओत्सृजति", "अ + ओ would give औ, not ओ.")],
            "वातम् (Vāta) + एव (only) + उत्सृजति (releases).",
            "अ + उ → ओ."),
        fill(4, "In sexual union it releases only Vāta: तन्मैथुने ____ एवोत्सृजति (type it in Devanagari or in English letters, e.g. dharma).",
             accepts("वातम्"),
             "The line is तन्मैथुने वातमेवोत्सृजति: वातम् + एव.",
             "वातम् is the accusative object of उत्सृजति: Vāta is what is released.",
             "वातम् एव उत्सृजति = releases only Vāta.", role="apply"),
        mcq("transfer", 5, "By the rule of एवोत्सृजति, how is सूर्य + उदयः (sunrise) joined?",
            ("सूर्योदयः", "अ + उ → ओ, as एव + उत्सृजति → एवोत्सृजति."),
            [("सूर्यौदयः", "अ + उ gives ओ, not औ."),
             ("सूर्युदयः", "The अ is not lost; it joins with उ."),
             ("सूर्यवुदयः", "अ does not turn into व्.")],
            "सूर्य + उदयः = सूर्योदयः, like एव + उत्सृजति = एवोत्सृजति.",
            "अ + उ → ओ.",
            teaches="A short अ before उ joins into ओ: एव + उत्सृजति → एवोत्सृजति."),
    ],
}


# ===================================================================== NOTES_HI
NOTES_HI = {
    "64": ("गद्य; विश्वास मध्यम; कोई पाठ-चिह्न नहीं। दूसरे खण्ड (अपरा) में ‘निष्क्रामति’ फिर से समझा जाता है, क्रिया नहीं जोड़ी गई; "
           "कर्ता (जन्म लेता गर्भ) लिखा नहीं। प्रसूति-मारुत = प्रसव की वायु; आधुनिक प्रसव-संकुचन मानना सम्भावित, ग्रन्थ में नहीं। "
           "सन्धि जाँची: परिवृत्त्या + अवाक्शिराः → परिवृत्त्याऽवाक्शिराः (आ + अ → आ, ऽ मिले अ का चिह्न); "
           "अवाक्शिराः + निष्क्रामति → अवाक्शिरा निष्क्रामति (आः → आ घोष से पहले); निष्क्रामति + अनु → निष्क्रामत्यनु (इ + अ → य); "
           "च + अपरा → चापरा (अ + अ → आ)।"),
    "65": ("गद्य; विश्वास उच्च; कोई पाठ-चिह्न नहीं। क्रिया ‘है’ समझी जाती है। ‘प्रकृति’ यहाँ स्वाभाविक, सामान्य अवस्था है "
           "(अगली छपी पंक्ति की ‘विकृति’ का प्रतिरूप), शरीर-प्रकृति का पारिभाषिक अर्थ नहीं। कोई सन्धि नहीं।"),
    "66": ("गद्य; विश्वास उच्च; कोई पाठ-चिह्न नहीं। क्रिया समझी जाती है; पूरी पंक्ति पिछली ‘एषा प्रकृतिः’ का प्रतिरूप है। "
           "सन्धि जाँची: विकृतिः + अतः → विकृतिरतः (इ के बाद विसर्ग → र् स्वर से पहले); अतः + अन्यथा → अतोऽन्यथा (अः + अ → ओऽ)।"),
    "67": ("गद्य; विश्वास निम्न। पाठ-चिह्न: ‘चेष्टतेतस्तने’ — सम्भवतः चेष्टते स्तने, बीच का ‘त’ अतिरिक्त (शायद कटा ‘तस्याः’ या भूल)। "
           "‘अत्युन्नततत्कुक्षिपरिमंडलगर्भा’ अनिश्चित: ‘तत्’ = उसकी (कुक्षि) या भटका अक्षर; ‘कुक्षि बहुत ऊँची, गर्भ गोल’ अनुमानित पाठ। "
           "‘पुरुषानभिलाषिणी’ दो तरह: पुरुषान् + अभिलाषिणी (पुरुषों की इच्छा करती) या पुरुष + अनभिलाषिणी (न चाहती) — तय नहीं। "
           "‘प्राक्’ = पहले; दाहिने स्तन में, यह नहीं कहा गया। ‘प्रसूते’ कन्या और नपुंसक के साथ फिर समझा जाता है। "
           "छपा ‘पुत्रंप्रसूते’ बिना अन्तराल। सन्धि जाँची: दक्षिणः + च → दक्षिणश्च; बाहुः + बलवान् → बाहुर्बलवान्; "
           "बलवान् + तेन → बलवांस्तेन; पयः + दृश्यते → पयो दृश्यते; तत् + विपर्यये → तद्विपर्यये (त् → द् घोष से पहले)।"),
    "68": ("गद्य; विश्वास मध्यम। पाठ-चिह्न: छपा ‘यद्दिंगमंगं’ सम्भवतः यल्लिंगमंगं (यत् + लिङ्ग में ल्ल चाहिए; बाद का ‘तल्लिंगम्’ ल्ल वाला है; "
           "इस छपाई में द्द और ल्ल भ्रमित होते हैं) — इस पर प्रश्न नहीं। लिंग = छुई वस्तु का लिंग (पुं, स्त्री, नपुंसक); कैसे तय हो, नहीं कहा। "
           "‘आदिशेत्’ का कर्ता अलिखित। सन्धि जाँची: तत् + लिङ्गम् → तल्लिङ्गम् (त् + ल → ल्ल); अस्याः + गर्भम् → अस्या गर्भम् "
           "(आः → आ घोष से पहले); गर्भम् + आदिशेत् → गर्भमादिशेत्।"),
    "69": ("गद्य; विश्वास मध्यम। पाठ-चिह्न: छपा ‘रसवाहिनी’ — नपुंसक बहुवचन ‘स्रोतांसि’ के साथ रसवाहीनि (ह्रस्व इ) होना चाहिए, "
           "दीर्घ ई सम्भवतः भूल; इस पर प्रश्न नहीं। ‘हीन’ किस बात में, नहीं कहा; कोई विशेष रोग नहीं। "
           "सन्धि जाँची: तु + उन्मार्गगः → तून्मार्गगः (उ + उ → ऊ); उन्मार्गगः + वातः → उन्मार्गगो वातः; वातः + गर्भस्य → वातो गर्भस्य; "
           "हीनः + जायते → हीनो जायते (अः → ओ घोष से पहले)।"),
    "70": ("गद्य; विश्वास मध्यम; कोई पाठ-चिह्न नहीं। वर्गीकरण: पिछली इकाई के ‘तदा’ के बाद का एक और फल प्रतीत होता है; "
           "कर्ता (गर्भ) अलिखित। उदर = पेट, उदर-रोग नहीं। सन्धि जाँची: वर्षाणि + उदरे → वर्षाण्युदरे (इ + उ → यु)।"),
    "71": ("गद्य; विश्वास मध्यम; कोई पाठ-चिह्न नहीं। ‘स्त्रीपुंसयोः’ द्विवचन, षष्ठी या सप्तमी — दोनों सम्भव। ‘अर्थ’ क्या है, नहीं कहा; "
           "वाक्य अधूरा है, फल इस इकाई में नहीं। सन्धि जाँची: समम् + अर्थः → सममर्थः; अर्थः + निष्पद्यते → अर्थो निष्पद्यते।"),
    "72": ("गद्य; विश्वास मध्यम; कोई पाठ-चिह्न नहीं। अध्याहार: क्रिया ‘है’ समझी जाती है। वर्गीकरण: पिछली इकाई के साथ एक ही कथन की "
           "शर्तें लगती हैं, फल यहाँ नहीं छपा। बीज = प्रत्येक माता-पिता का जनन-तत्त्व (सम्भवतः शुक्र और स्त्री-तत्त्व)। "
           "सन्धि जाँची: सम + अंशम् → समांशम् (अ + अ → आ); छपा ‘संमुखं’ = सम्मुखम्।"),
    "73": ("गद्य; विश्वास मध्यम; कोई पाठ-चिह्न नहीं। दोनों विशेषण (द्विप्रकृतिः, द्विरेतः) नपुंसक के हैं; डेटा उन्हें पुंलिंग कहता है "
           "जबकि नपुंसकम् नपुंसकलिंग है — इसलिए उनके व्याकरण-चिह्न पर प्रश्न नहीं। रेतस् = वीर्य (मानक), यहाँ ‘बीज’। "
           "दो प्रकृति = सम्भवतः पुरुष और स्त्री की (सन्दर्भ से, लिखा नहीं)। सन्धि जाँची: द्विप्रकृतिः + द्विरेतः → द्विप्रकृतिर्द्विरेतः "
           "(इ के बाद विसर्ग → र्); द्विरेतः + नपुंसकम् → द्विरेतो नपुंसकम् (अः → ओ)।"),
    "74": ("गद्य; विश्वास निम्न; कठिन वाक्य। ‘विगुणीकरोति’ का कर्म नहीं छपा; पिछला शुक्र मानना अनुमान है। ‘अस्य’ (इसका) को गर्भ मानना "
           "ग्रन्थ नहीं कहता। ‘पुंस्त्ववाहिनी’ को स्रोतांसि के साथ पुंस्त्ववाहीनि पढ़ा गया। ‘वातेन्द्रिय’ छपे अनुसार; सम्भवतः नपुंसक का "
           "एक प्रकार (यहाँ नहीं कहा)। पाठ-चिह्न ‘चास्यस्रोतांसि’ केवल अन्तराल का है। सन्धि जाँची: पश्चात् + शुक्रम् → पश्चाच्छुक्रम् "
           "(त् + श → च्छ, जैसा छपा); स्त्रियाः + वातः → स्त्रिया वातः; हर्ष + अनवस्थित → हर्षानवस्थित; च + उपहन्ति → चोपहन्ति; "
           "वात + इन्द्रियम् → वातेन्द्रियम्।"),
    "75": ("गद्य; विश्वास मध्यम; कोई पाठ-चिह्न नहीं। कर्ता ‘तत्’ पिछली इकाई से आता है; किसका बोध, यहाँ नहीं कहा। वात दोष के रूप में "
           "रखा गया। सन्धि जाँची: तत् + मैथुने → तन्मैथुने (त् → न् अनुनासिक से पहले, जैसा छपा); वातम् + एव → वातमेव; "
           "एव + उत्सृजति → एवोत्सृजति (अ + उ → ओ)।"),
}

# ===================================================================== AIDS
AIDS = {
    "64": {
        "chain": {"steps": ["जन्म का समय", "प्रसूति-मारुत का संयोग", "पलटना (परिवृत्ति)", "सिर नीचे, बाहर निकलना",
                            "बाद में अपरा, माता के हृदय से अलग"]},
        "chunks": "जन्मकाले तु | प्रसूतिमारुतयोगात् | परिवृत्त्याऽवाक्शिरा | निष्क्रामति | अनु चापरा च्युता | मातृहृदयात्",
        "sandhi": "इ + अ → य: निष्क्रामति + अनु → निष्क्रामत्यनु · आः → आ घोष से पहले: अवाक्शिराः + निष्क्रामति → अवाक्शिरा निष्क्रामति · अ + अ → आ: च + अपरा → चापरा।",
        "frame": "कब (जन्मकाले) → किससे (प्रसूतिमारुतयोगात्) → कैसे (परिवृत्त्या, अवाक्शिराः) → क्रिया (निष्क्रामति) → फिर (अनु: अपरा च्युता)।",
    },
    "65": {
        "chunks": "एषा | प्रकृतिः",
        "frame": "कर्ता ‘एषा’ (यह, स्त्रीलिंग) + विधेय ‘प्रकृतिः’; क्रिया ‘है’ समझी जाती है।",
        "anchors": "याद-सूत्र: प्रकृति = जैसा स्वभाव से होता है; यहाँ देह-प्रकृति नहीं। (मेरी याद-पद्धति)",
    },
    "66": {
        "chunks": "विकृतिः | अतः | अन्यथा",
        "sandhi": "इ के बाद विसर्ग → र् स्वर से पहले: विकृतिः + अतः → विकृतिरतः · अः + अ → ओऽ: अतः + अन्यथा → अतोऽन्यथा।",
        "frame": "विधेय ‘विकृतिः’ + ‘अतः अन्यथा’ (इससे अन्यथा, यानी स्वाभाविक से हटकर जो हो); क्रिया समझी जाती है।",
    },
    "67": {
        "diagram": {"groups": [
            {"label": "लक्षण (क्रम से, निश्चित अंश)", "items": ["दाहिना पैर पहले आगे", "दाहिनी भुजा बलवान, उसी से चेष्टा",
                                                      "पुरुष-नाम वालों का दौर्हृद", "पुरुष-नाम वाले स्वप्न", "प्रसन्न मुख-वर्ण",
                                                      "तीव्र भूख, ऊपर की रोम-पंक्ति"]},
            {"label": "फल", "items": ["लक्षण → पुत्र", "विपर्यय → कन्या", "संकर → नपुंसक"]}]},
        "chunks": ("तत्र या दक्षिणं पादं पूर्वमभिहरति | दक्षिणश्च यस्या बाहुर्बलवांस्तेन च चेष्टते(त)स्तने च प्राक् पयो दृश्यते | "
                   "अत्युन्नततत्कुक्षिपरिमंडलगर्भा (?) | पुन्नामदर्शनस्पर्शनप्रश्नदौर्हृदाभिरता | पुन्नामधेयांश्च स्वप्नान् पश्यति | "
                   "प्रसन्नमुखवर्णा | तीक्ष्णक्षुदूर्ध्वरोमराजिः | पुरुषानभिलाषिणी (?) च | सा पुत्रं प्रसूते | तद्विपर्यये कन्यां | संकरे च नपुंसकं"),
        "sandhi": "विसर्ग + च → श्च: दक्षिणः + च → दक्षिणश्च · उ के बाद विसर्ग → र्: बाहुः + बलवान् → बाहुर्बलवान् · त् → द् घोष से पहले: तत् + विपर्यये → तद्विपर्यये।",
        "pegs": "मेरा बनाया चित्र: ‘दाहिनी ओर’ का दीपक — दाहिना पैर आगे, दाहिना हाथ मज़बूत; पीछे पुरुष-नाम लिखी पट्टियाँ (स्वप्न, दौर्हृद)। (केवल याद के लिए, श्लोक का दावा नहीं)",
    },
    "68": {
        "chain": {"steps": ["प्रश्न का समय", "स्त्री अंग या बाहरी द्रव्य छूती है", "उसी लिंग का गर्भ बताए"]},
        "chunks": "प्रश्नकाले नारी | यद्दिंगमंगं (= यल्लिंगम्? अनिश्चित) | बाह्यद्रव्यं वा | परामृशति | तल्लिंगमस्या | गर्भमादिशेत्",
        "sandhi": "त् + ल → ल्ल: तत् + लिङ्गम् → तल्लिङ्गम् · आः → आ घोष से पहले: अस्याः + गर्भम् → अस्या गर्भम्।",
    },
    "69": {
        "chain": {"steps": ["वात उन्मार्गग (मार्ग से भटका)", "गर्भ के रसवाही स्रोत सूखे", "वातरोगी, हीन जन्म"]},
        "chunks": "यदा तून्मार्गगो वातो | गर्भस्य रसवाहिनी स्रोतांसि | शोषयति | तदा वातरोगी हीनो जायते",
        "sandhi": "उ + उ → ऊ: तु + उन्मार्गगः → तून्मार्गगः · अः → ओ घोष से पहले: उन्मार्गगः + वातः → उन्मार्गगो वातः, हीनः + जायते → हीनो जायते।",
        "frame": "यदा (जब: कारण) … शोषयति → तदा (तब: फल) … जायते।",
    },
    "70": {
        "chunks": "बहूनि वा | वर्षाण्युदरे | तिष्ठति",
        "sandhi": "इ + उ → यु: वर्षाणि + उदरे → वर्षाण्युदरे।",
        "frame": "‘वा’ (या): पिछली इकाई के ‘तदा’ के बाद एक और फल प्रतीत होता है; समय-अवधि द्वितीया में (बहूनि वर्षाणि), स्थान सप्तमी में (उदरे)।",
    },
    "71": {
        "chunks": "यदा | स्त्रीपुंसयोः | सममर्थो | निष्पद्यते",
        "sandhi": "म् + स्वर: समम् + अर्थः → सममर्थः · अः → ओ घोष से पहले: अर्थः + निष्पद्यते → अर्थो निष्पद्यते।",
        "frame": "केवल शर्त (यदा …); ‘तदा’ वाला फल इस इकाई में नहीं।",
    },
    "72": {
        "chunks": "बीजं वा | तयोः | समांशं | संमुखं च",
        "sandhi": "अ + अ → आ: सम + अंशम् → समांशम् · छपा ‘संमुखं’ = सम्मुखम् (अनुस्वार म् के स्थान पर)।",
        "anchors": "याद-सूत्र: दो बीज — बराबर हिस्सा, आमने-सामने। (मेरी याद-पद्धति)",
    },
    "73": {
        "chain": {"steps": ["बीज किसी भाग में दूषित", "नपुंसक होता है", "द्विप्रकृति (दो प्रकृति)", "द्विरेतस् (दो रेतस्)"]},
        "chunks": "यदा च बीजं | भागे दुष्यति | तदा | द्विप्रकृतिर्द्विरेतो | नपुंसकं भवति",
        "sandhi": "इ के बाद विसर्ग → र् घोष से पहले: द्विप्रकृतिः + द्विरेतः → द्विप्रकृतिर्द्विरेतः · अः → ओ: द्विरेतः + नपुंसकम् → द्विरेतो नपुंसकम्।",
    },
    "74": {
        "chain": {"steps": ["१ स्त्री पहले कृतार्था", "२ बाद में पुरुष का शुक्र", "३ हर्ष-अस्थिर स्त्री का वात",
                            "४ पुंस्त्ववाही स्रोतों को क्षति", "५ तब वातेन्द्रिय"]},
        "chunks": ("यदा स्त्री प्रथमं कृतार्था भवति | ततः पुरुषेण पश्चाच्छुक्रमुत्सृष्टं | हर्षानवस्थितचेतसः स्त्रिया वातो | "
                   "विगुणीकरोति (किसे? अलिखित) | पुंस्त्ववाहिनी चास्यस्रोतांसि चोपहंति | तदा वातेंद्रियं भवति"),
        "sandhi": "त् + श → च्छ (जैसा छपा): पश्चात् + शुक्रम् → पश्चाच्छुक्रम् · अ + उ → ओ: च + उपहन्ति → चोपहन्ति · अ + इ → ए: वात + इन्द्रियम् → वातेन्द्रियम्।",
    },
    "75": {
        "chunks": "तन्मैथुने | वातमेव | उत्सृजति",
        "sandhi": "त् → न् अनुनासिक से पहले (जैसा छपा): तत् + मैथुने → तन्मैथुने · अ + उ → ओ: एव + उत्सृजति → एवोत्सृजति।",
        "frame": "कर्ता ‘तत्’ (पिछले वाक्य से) → कहाँ (मैथुने) → क्या (वातम् एव) → क्रिया (उत्सृजति)।",
    },
}

# ===================================================================== IMAGE_SPECS
IMAGE_SPECS = {
    ("64", "chain"): {
        "file": "sh2-janma-krama-64.svg",
        "alt": ("Flowchart of unit 64: at the time of birth, contact with the wind of parturition, turning round, coming "
                "out head downward, and afterwards the aparā (placenta), detached from the mother's heart."),
        "type": "mermaid",
        "code": ("flowchart TD\n"
                 "  A[\"जन्म का समय\"] --> B[\"प्रसूति-मारुत का संयोग\"]\n"
                 "  B --> C[\"पलटना (परिवृत्ति)\"]\n"
                 "  C --> D[\"सिर नीचे, बाहर निकलना\"]\n"
                 "  D -->|\"बाद में\"| E[\"अपरा, हृदय से अलग\"]\n"),
    },
    ("67", "diagram"): {
        "file": "sh2-putra-lakshana-67.svg",
        "alt": ("Table of unit 67 as the text states it: the listed signs (right foot first, strong right arm, male-named "
                "longings and dreams, clear face, keen hunger) go with a son; their opposite with a girl; a mixture with a "
                "napuṃsaka."),
        "type": "table",
        "title": "लक्षण और फल (इकाई ६७, ग्रन्थ का कथन)",
        "heads": ["लक्षण", "फल"],
        "rows": [["दाहिना पैर पहले, दाहिनी भुजा बलवान", "पुत्र"], ["पुरुष-नाम के दौर्हृद और स्वप्न", "पुत्र"],
                 ["प्रसन्न मुख, तीव्र भूख", "पुत्र"], ["इनका विपर्यय", "कन्या"], ["संकर (मिश्रण)", "नपुंसक"]],
    },
    ("68", "chain"): {
        "file": "sh2-prashna-sparsha-68.svg",
        "alt": ("Flowchart of unit 68: at the time of the question, the woman touches a limb or an external substance; "
                "the embryo is declared of that same gender."),
        "type": "mermaid",
        "code": ("flowchart TD\n"
                 "  A[\"प्रश्न का समय\"] --> B[\"अंग या बाहरी द्रव्य छूना\"]\n"
                 "  B --> C[\"उसी लिंग का गर्भ बताए\"]\n"),
    },
    ("69", "chain"): {
        "file": "sh2-unmarga-vata-69.svg",
        "alt": ("Flowchart of unit 69: Vāta gone astray dries up the embryo's rasa-carrying channels; then the child is "
                "born suffering from a Vāta disease and deficient."),
        "type": "mermaid",
        "code": ("flowchart TD\n"
                 "  A[\"वात मार्ग से भटका\"] --> B[\"गर्भ के रसवाही स्रोत सूखे\"]\n"
                 "  B -->|\"तब\"| C[\"वातरोगी, हीन जन्म\"]\n"),
    },
    ("73", "chain"): {
        "file": "sh2-dviretas-73.svg",
        "alt": ("Flowchart of unit 73: when the seed is vitiated in a part, a napuṃsaka comes to be, having two natures "
                "and two seeds."),
        "type": "mermaid",
        "code": ("flowchart TD\n"
                 "  A[\"बीज किसी भाग में दूषित\"] -->|\"तब\"| B[\"नपुंसक\"]\n"
                 "  B --> C[\"द्विप्रकृति\"]\n"
                 "  B --> D[\"द्विरेतस्\"]\n"),
    },
    ("74", "chain"): {
        "file": "sh2-vatendriya-74.svg",
        "alt": ("Numbered flowchart of unit 74: 1 the woman first has her purpose accomplished, 2 afterwards the man's "
                "semen, 3 the Vāta of the woman unsteady with joy, 4 damage to the virility-carrying channels, "
                "5 then a vātendriya."),
        "type": "mermaid",
        "code": ("flowchart TD\n"
                 "  A[\"१ स्त्री पहले कृतार्था\"] --> B[\"२ बाद में पुरुष का शुक्र\"]\n"
                 "  B --> C[\"३ हर्ष-अस्थिर स्त्री का वात\"]\n"
                 "  C --> D[\"४ पुंस्त्ववाही स्रोतों को क्षति\"]\n"
                 "  D --> E[\"५ तब वातेन्द्रिय\"]\n"),
    },
}
