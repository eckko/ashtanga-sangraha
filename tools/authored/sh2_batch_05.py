from helpers import mcq, match, order, fill, multi, accepts


AUTHORED = {}

# ---------------------------------------------------------------- unit 51
AUTHORED["51"] = {
    "title": "तस्मात्प्रसवप्रतिषेधार्थं",
    "question": "What should the woman be, by unit 51, in order to prevent delivery?",
    "rule": ("Therefore, to prevent delivery (prasava), the woman should be bathed, pure, chaste (brahmacāriṇī) "
             "and intent on the worship of the deities."),
    "limits": ("तस्मात् (therefore) points back to what precedes; this unit does not restate the reason. "
               "No time, place or rite of worship is named. ब्रह्मचारिणी is taken as 'chaste', as the data gives it."),
    "explain_hi": ("यह गद्य-पंक्ति एक निर्देश है: ‘तस्मात्’ यानी इसलिए, पिछले कथन के कारण। "
                   "प्रसव को रोकने के लिए स्त्री स्नान की हुई, शुद्ध, ब्रह्मचारिणी (ब्रह्मचर्य का पालन करने वाली) "
                   "और देवताओं की आराधना में तत्पर हो। "
                   "चारों विशेषण स्त्रीलिंग प्रथमा एकवचन हैं और ‘स्त्री’ से जुड़ते हैं; क्रिया ‘स्यात्’ (हो) विधिलिङ् है। "
                   "आराधना किस विधि से हो, यह पंक्ति नहीं बताती।"),
    "hook": "स्नाता, शुचि, ब्रह्मचारिणी, देव-आराधन में लगी: प्रसव रोकने को।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 51, for what purpose should the woman be bathed, pure and the rest?",
            ("To prevent delivery", "प्रसवप्रतिषेधार्थम्: for preventing delivery."),
            [("To hasten the delivery", "प्रतिषेध means prevention, not hastening."),
             ("To conceive a male child", "No child's sex is named in this unit."),
             ("To cure a fever she has", "No fever is named in this unit.")],
            "प्रसव (delivery) + प्रतिषेध (prevention) + अर्थम् (for the sake of): to prevent delivery.",
            "प्रसवप्रतिषेधार्थम् = for preventing delivery."),
        order(1, "Put these words of unit 51 in their printed order.",
              ["प्रसवप्रतिषेधार्थम्", "स्त्री", "स्नाता", "शुचिर्ब्रह्मचारिणी", "दैवताराधनपरमा", "स्यात्"],
              "The purpose comes first, then the woman, then her four qualities, and the verb स्यात् closes the line.",
              "Purpose → स्त्री → स्नाता → शुचिः ब्रह्मचारिणी → दैवताराधनपरमा → स्यात्."),
        match(2, "Match each word of unit 51 to its meaning on the card.",
              [["स्नाता", "bathed"], ["शुचिः", "pure"], ["ब्रह्मचारिणी", "chaste (observing brahmacarya)"],
               ["दैवताराधनपरमा", "intent on the worship of the deities"], ["स्यात्", "should be"]],
              "Four qualities of the woman, and the verb that makes them an instruction.",
              "स्नाता, शुचिः, ब्रह्मचारिणी, दैवताराधनपरमा + स्यात्.", role="extend",
              teaches="The woman's four qualities are bathed, pure, chaste and devoted to worship of the deities."),
        mcq("discriminate", 3, "Which split of शुचिर्ब्रह्मचारिणी is right?",
            ("शुचिः + ब्रह्मचारिणी", "Visarga after इ becomes र् before a voiced sound such as ब."),
            [("शुचिम् + ब्रह्मचारिणी", "म् would stay म् or become ं before ब, never र्."),
             ("शुची + ब्रह्मचारिणी", "A final ई does not change before ब; no र् would appear."),
             ("शुचि + र्ब्रह्मचारिणी", "र्ब्रह्मचारिणी is not a word of the card.")],
            "शुचिः (pure) + ब्रह्मचारिणी (chaste): two separate adjectives, not a compound.",
            "इः / उः + voiced sound → इर् / उर्."),
        mcq("apply", 4, "In unit 51, which word do स्नाता, शुचिः and ब्रह्मचारिणी describe, by their feminine endings?",
            ("स्त्री, the woman", "All are f. nom. sg., agreeing with स्त्री."),
            [("गर्भ, the embryo", "गर्भ is masculine and is not named here."),
             ("दैवत, the deities", "दैवत is only inside a compound, as what is worshipped."),
             ("प्रसव, the delivery", "प्रसव is masculine and only part of the purpose compound.")],
            "स्त्री is the subject; the four qualities agree with it in feminine nominative singular.",
            "An adjective agrees with its noun in gender, case and number."),
        mcq("transfer", 5, "By the rule of शुचिर्ब्रह्मचारिणी, how is हरिः + गच्छति written when joined?",
            ("हरिर्गच्छति", "Visarga after इ becomes र् before the voiced ग."),
            [("हरी गच्छति", "The visarga does not drop with a long ई before ग."),
             ("हरिस्गच्छति", "स् comes before त/थ, not before ग."),
             ("हरिश्गच्छति", "श् comes before च/छ/श, not before ग.")],
            "शुचिः + ब्रह्मचारिणी → शुचिर्ब्रह्मचारिणी; so हरिः + गच्छति → हरिर्गच्छति.",
            "इः + voiced consonant → इर्.",
            teaches="A visarga after इ or उ becomes र् before a voiced sound: हरिः + गच्छति → हरिर्गच्छति."),
    ],
}

# ---------------------------------------------------------------- unit 52
AUTHORED["52"] = {
    "title": "मांसौदनबलिं चात्र निर्वपेत्",
    "question": "What offering does unit 52 say should be made here?",
    "rule": "And here one should offer a bali (offering) of meat (māṃsa) and boiled rice (odana).",
    "limits": ("The one who offers is not printed ('one'). अत्र is read as 'here, in this case', i.e. the situation of "
               "unit 51 (preventing delivery); the unit names no deity, place or time for the bali."),
    "explain_hi": ("यह छोटी पंक्ति भी एक निर्देश है: ‘निर्वपेत्’ विधिलिङ् है, यानी अर्पित करे। "
                   "बलि यानी भेंट; यह मांस और ओदन (पके चावल) की हो। "
                   "‘अत्र’ यानी यहाँ, इसी स्थिति में (इकाई ५१ की स्थिति, प्रसव रोकना)। "
                   "कौन अर्पित करे, यह छपा नहीं है; अनुवाद ‘one’ लेता है।"),
    "hook": "मांस और ओदन की बलि: यहाँ अर्पित करे।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 52, of what is the bali (offering) made?",
            ("Of meat and boiled rice", "मांसौदनबलिम्: a bali of meat (मांस) and boiled rice (ओदन)."),
            [("Of milk and honey", "Neither milk nor honey is named here."),
             ("Of flowers and water", "Neither flowers nor water is named here."),
             ("Of ghee and barley", "Neither ghee nor barley is named here.")],
            "मांस + ओदन + बलि: a bali of meat and boiled rice.",
            "मांसौदनबलि = an offering of meat and boiled rice."),
        order(1, "Put these words of unit 52 in their printed order.",
              ["मांसौदनबलिम्", "च", "अत्र", "निर्वपेत्"],
              "The object comes first, then च अत्र (joined as चात्र), and the verb ends the line.",
              "मांसौदनबलिम् → च → अत्र → निर्वपेत्."),
        match(2, "Match each word of unit 52 to its meaning on the card.",
              [["बलि", "offering"], ["निर्वपेत्", "should offer"], ["अत्र", "here"], ["च", "and"]],
              "बलि is what is offered; निर्वपेत् is the verb; च अत्र = and here.",
              "बलि, निर्वपेत्, अत्र, च.", role="extend",
              teaches="बलि means an offering; निर्वपेत् (nir-√vap) means 'should offer'."),
        mcq("discriminate", 3, "Which split of मांसौदन is right?",
            ("मांस + ओदन", "अ + ओ gives औ: मांस + ओदन → मांसौदन."),
            [("मांस + उदन", "अ + उ would give ओ: मांसोदन."),
             ("मांसा + उदन", "आ + उ would give ओ, not औ."),
             ("मांसौ + दन", "दन is not a word of the card.")],
            "मांस (meat) + ओदन (boiled rice), a dvandva inside the compound.",
            "अ/आ + ओ → औ."),
        mcq("apply", 4, "What kind of statement does the optative निर्वपेत् make in unit 52?",
            ("An instruction: one should offer", "The optative (3 sg. opt.) here means 'should offer'."),
            [("A report: one offered", "A past form would be needed; निर्वपेत् is optative."),
             ("A forecast: one will offer", "A future form would be needed; निर्वपेत् is optative."),
             ("A question: does one offer?", "No question word or sign stands in the line.")],
            "Like स्यात् in unit 51, निर्वपेत् is an optative that gives an instruction.",
            "Optative (विधिलिङ्) = should, ought to."),
        mcq("transfer", 5, "By the rule of मांसौदन, how is गङ्गा + ओघः written when joined?",
            ("गङ्गौघः", "आ + ओ gives औ, as अ + ओ does in मांसौदन."),
            [("गङ्गोघः", "आ + ओ does not give ओ."),
             ("गङ्गाओघः", "The two vowels must merge into one."),
             ("गङ्गवोघः", "No व् is inserted after आ.")],
            "मांस + ओदन → मांसौदन; so गङ्गा + ओघः → गङ्गौघः.",
            "अ/आ + ओ/औ → औ.",
            teaches="अ or आ before ओ merges into औ: गङ्गा + ओघः → गङ्गौघः."),
    ],
}

# ---------------------------------------------------------------- unit 53
AUTHORED["53"] = {
    "title": "तस्मिन्नेकदिवसातिक्रांतेऽपि",
    "question": "What do 'they' say of the time of delivery in unit 53, word by word?",
    "rule": ("Literally: even when one day has passed in that (period), they speak of a time of delivery up to a year "
             "(आसंवत्सरात्). The sense is not firm."),
    "limits": ("Low confidence. What तस्मिन् (in that) refers to is not clear (probably the period discussed around it). "
               "The sense of the whole line is not firm, so questions ask only about its words, their order and sandhi, "
               "not about the doctrine."),
    "explain_hi": ("इस पंक्ति का विश्वास कम है; अनुवाद शाब्दिक है और अर्थ पक्का नहीं। "
                   "शब्दशः: उसमें एक दिन बीत जाने पर भी, वे प्रसव का काल एक वर्ष तक कहते हैं। "
                   "‘तस्मिन्’ (उसमें) किसकी ओर संकेत करता है, यह इकाई से स्पष्ट नहीं; सम्भवतः आसपास कही गई अवधि। "
                   "‘आहुः’ (वे कहते हैं) दिखाता है कि यह दूसरों का कथन है। "
                   "‘आसंवत्सरात्’ में आ + पंचमी: एक वर्ष तक।"),
    "hook": "‘आहुः’: वे कहते हैं, ‘आसंवत्सरात्’: वर्ष भर तक (अर्थ पक्का नहीं)।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "Which word of unit 53 means 'up to a year'?",
            ("आसंवत्सरात्", "आ with the ablative संवत्सरात्: up to a year."),
            [("अतिक्रान्ते", "अतिक्रान्ते = when (one day) has passed."),
             ("प्रसवकालम्", "प्रसवकालम् = the time of delivery."),
             ("तस्मिन्", "तस्मिन् = in that.")],
            "आ + संवत्सरात् = up to a year; it closes the line.",
            "आसंवत्सरात् = up to a year."),
        order(1, "Put these words of unit 53 in their printed order.",
              ["तस्मिन्", "एकदिवसातिक्रान्ते", "अपि", "प्रसवकालम्", "आहुः", "आसंवत्सरात्"],
              "In that, one day having passed, even; the time of delivery, they say, up to a year.",
              "तस्मिन् → एकदिवसातिक्रान्ते → अपि → प्रसवकालम् → आहुः → आसंवत्सरात्."),
        match(2, "Match each word of unit 53 to its meaning on the card.",
              [["तस्मिन्", "in that"], ["एकदिवसातिक्रान्ते", "when one day has passed"],
               ["प्रसवकालम्", "the time of delivery"], ["आहुः", "they say"]],
              "These four words carry the literal sense; the meaning of the whole is not firm.",
              "तस्मिन्, एकदिवसातिक्रान्ते, प्रसवकालम्, आहुः.", role="extend",
              teaches="आहुः (3 pl. of √ah) means 'they say': it reports what others hold."),
        mcq("discriminate", 3, "Which split of तस्मिन्नेक is right?",
            ("तस्मिन् + एक", "A final न् after a short vowel doubles before a vowel: तस्मिन् + एक → तस्मिन्नेक."),
            [("तस्मिन्न + एक", "तस्मिन्न is not a word; the form is तस्मिन्."),
             ("तस्मि + न्नेक", "न्नेक is not a word of the card."),
             ("तस्मिन् + नेक", "नेक is not a word of the card; the word is एक.")],
            "तस्मिन् (in that) + एक (one): the न् doubles before the vowel ए.",
            "Short vowel + न् + vowel → न्न् + vowel."),
        mcq("apply", 4, "Whose statement does आहुः present in unit 53?",
            ("What 'they' say", "आहुः is 3rd person plural: they say."),
            [("What 'he' says", "That would be 3rd person singular, आह."),
             ("What 'I' say", "आहुः is not a 1st person form."),
             ("What 'you' say", "आहुः is not a 2nd person form.")],
            "आहुः (3 pl. pf. of √ah) = they say: the line reports others' view.",
            "आहुः = they say."),
        mcq("transfer", 5, "By the join in अतिक्रान्तेऽपि, how is वने + अपि written?",
            ("वनेऽपि", "ए + अ at a word end: the अ is dropped and marked with ऽ."),
            [("वनैपि", "ए + अ does not give ऐ."),
             ("वनापि", "The ए cannot turn into आ here."),
             ("वनोपि", "ए + अ does not give ओ.")],
            "अतिक्रान्ते + अपि → अतिक्रान्तेऽपि; so वने + अपि → वनेऽपि.",
            "Final ए/ओ + अ → ए/ओ + ऽ.",
            teaches="After a final ए or ओ, an initial अ is dropped and marked with ऽ: वने + अपि → वनेऽपि."),
    ],
}

# ---------------------------------------------------------------- unit 54
AUTHORED["54"] = {
    "title": "अतःपरं विकारी भवति",
    "question": "What does unit 54 say happens after this?",
    "rule": "After this, (he) becomes disordered (vikārī, subject to disorder).",
    "limits": ("The subject is not printed: probably the child, but the text does not say. "
               "The kind of disorder is not specified. No question rests on who the subject is."),
    "explain_hi": ("यह बहुत छोटी गद्य-पंक्ति है: इसके बाद वह विकारी हो जाता है। "
                   "‘अतःपरम्’ यानी इसके बाद; ‘विकारी’ यानी विकार वाला; ‘भवति’ यानी होता है। "
                   "कर्ता छपा नहीं है; सम्भवतः शिशु, पर पाठ यह नहीं कहता। ‘विकारी’ पुंलिंग है। "
                   "विकार किस प्रकार का है, यह भी नहीं बताया गया।"),
    "hook": "इसके बाद: विकारी! (कौन, कैसा, नहीं कहा)",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 54, what does (he) become after this?",
            ("Disordered", "विकारी भवति: becomes subject to disorder."),
            [("Strong and well", "The word is विकारी, disordered."),
             ("Ready to be born", "Birth is not named in this unit."),
             ("Free of all disorder", "That is the opposite of विकारी.")],
            "अतःपरम् विकारी भवति: after this he becomes disordered.",
            "विकारी = subject to disorder."),
        order(1, "Put the words of unit 54 in their printed order.",
              ["अतःपरम्", "विकारी", "भवति"],
              "After this → disordered → becomes.",
              "अतःपरम् → विकारी → भवति."),
        match(2, "Match each word of unit 54 to its meaning on the card.",
              [["अतःपरम्", "after this"], ["विकारी", "disordered"], ["भवति", "becomes"]],
              "Three words make the whole line.",
              "अतःपरम् = after this; विकारी = disordered; भवति = becomes.", role="extend",
              teaches="अतःपरम् means 'after this'; भवति (√भू) means 'becomes'."),
        mcq("discriminate", 3, "What form is विकारी in unit 54, by the card?",
            ("Masculine nominative singular", "The data labels विकारी m. nom. sg."),
            [("Feminine nominative singular", "The feminine would be विकारिणी."),
             ("Neuter nominative singular", "The neuter would be विकारि."),
             ("Masculine nominative plural", "The plural would be विकारिणः.")],
            "विकारी (stem विकारिन्) is masculine nominative singular, so the unstated subject is masculine.",
            "-इन् stem, m. nom. sg. → -ई."),
        multi("apply", 4, "Which two are true of unit 54?",
              [("Its subject is not printed", "Right: the line has no subject word."),
               ("It names the child as subject", "The child is only a probable guess of the data, not printed."),
               ("It does not say what the disorder is", "Right: the kind of disorder is not specified."),
               ("It names Vāta as the cause", "No doṣa is named in this unit.")],
              [0, 2],
              "The line says only that (he) becomes disordered after this; subject and kind of disorder are not stated.",
              "Read only what is printed: अतःपरं विकारी भवति."),
        mcq("transfer", 5, "विकारी is the m. nom. sg. of विकारिन्. By the same pattern, what is the m. nom. sg. of ब्रह्मचारिन्?",
            ("ब्रह्मचारी", "-इन् stem, m. nom. sg. → -ई, as विकारिन् → विकारी."),
            [("ब्रह्मचारिः", "-इन् stems take no visarga in the m. nom. sg."),
             ("ब्रह्मचारिन्", "That is the bare stem, not the nominative."),
             ("ब्रह्मचारा", "-आ is no ending of an -इन् stem.")],
            "विकारिन् → विकारी; so ब्रह्मचारिन् → ब्रह्मचारी (feminine ब्रह्मचारिणी).",
            "-इन् stem: m. nom. sg. -ई; feminine -इणी.",
            teaches="An -इन् stem has m. nom. sg. in -ई (विकारी, ब्रह्मचारी) and a feminine in -इणी (ब्रह्मचारिणी)."),
    ],
}

# ---------------------------------------------------------------- unit 55
AUTHORED["55"] = {
    "title": "गर्भस्तु मातुः पृष्ठाभिमुखो",
    "question": "How does the embryo lie in the garbha-koṣṭha, and which side does each sex rest on, by unit 55?",
    "rule": ("The embryo faces the mother's back, palms joined at the forehead, limbs contracted, in the garbha-koṣṭha: "
             "the male rests on the right side, the female on the left, the neuter (napuṃsaka) in the middle."),
    "limits": ("आश्रित्य अवतिष्ठते (resting on, stays) is printed once and understood with 'left: female' and "
               "'middle: neuter'. गर्भकोष्ठ as the uterine cavity is probable. The unit gives no reason for the sides."),
    "explain_hi": ("गर्भ माता की पीठ की ओर मुख किए, ललाट पर अञ्जलि बाँधे और अंगों को सिकोड़े हुए गर्भकोष्ठ में रहता है। "
                   "गर्भकोष्ठ यानी सम्भवतः गर्भाशय की गुहा (सम्भावित पहचान)। "
                   "पुमान् (पुरुष) दाहिने पार्श्व का आश्रय लेकर टिकता है, स्त्री बाएँ का, और नपुंसक मध्य का। "
                   "‘आश्रित्य अवतिष्ठते’ एक बार छपा है और बाद के दोनों खण्डों में समझा जाता है। "
                   "नपुंसक यानी जो न पुरुष हो न स्त्री।"),
    "hook": "दाएँ पुमान्, बाएँ स्त्री, बीच में नपुंसक; मुख माँ की पीठ की ओर।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 55, which way does the embryo face in the garbha-koṣṭha?",
            ("Towards the mother's back", "मातुः पृष्ठाभिमुखः: facing the mother's back."),
            [("Towards the mother's front", "पृष्ठ means the back, not the front."),
             ("Towards the mother's head", "The forehead (ललाट) is where its palms are joined."),
             ("Towards the right side", "The right side is where the male rests.")],
            "मातुः (of the mother) पृष्ठ (back) अभिमुखः (facing).",
            "पृष्ठाभिमुख = facing the back."),
        order(1, "Put these phrases of unit 55 in their printed order.",
              ["मातुः पृष्ठाभिमुखः", "ललाटे कृताञ्जलिः", "संकुचिताङ्गः", "गर्भकोष्ठे", "दक्षिणपार्श्वमाश्रित्यावतिष्ठते पुमान्",
               "वामं स्त्री मध्यं नपुंसकम्"],
              "Face, hands, limbs, the place, and then the three sides: right, left, middle.",
              "Facing the back → palms at forehead → limbs contracted → garbha-koṣṭha → right: male → left: female, middle: neuter."),
        match(2, "Match each side in unit 55 to who rests on it.",
              [["दक्षिणपार्श्व (right side)", "पुमान् (male)"], ["वाम (left)", "स्त्री (female)"],
               ["मध्य (middle)", "नपुंसक (neuter)"]],
              "Right side: male; left: female; middle: neuter.",
              "दक्षिण → पुमान्, वाम → स्त्री, मध्य → नपुंसक.", role="extend",
              teaches="Unit 55 places the male on the right side, the female on the left and the neuter in the middle."),
        mcq("discriminate", 3, "Which split of आश्रित्यावतिष्ठते is right?",
            ("आश्रित्य + अवतिष्ठते", "अ + अ gives आ: आश्रित्य + अवतिष्ठते → आश्रित्यावतिष्ठते."),
            [("आश्रित्या + वतिष्ठते", "वतिष्ठते is not a word of the card."),
             ("आश्रिती + अवतिष्ठते", "ई + अ would give य: आश्रित्यवतिष्ठते, with a short अ."),
             ("आश्रित्य + वतिष्ठते", "Then no आ could appear; वतिष्ठते is no word.")],
            "आश्रित्य (resting on, absolutive) + अवतिष्ठते (stays).",
            "अ + अ → आ."),
        mcq("apply", 4, "In वामं स्त्री, which printed words must be understood again?",
            ("आश्रित्य अवतिष्ठते (resting on, stays)", "These are printed once with पुमान् and carried over."),
            [("मातुः पृष्ठाभिमुखः (facing the back)", "That is the embryo's posture, said once of the garbha."),
             ("ललाटे कृताञ्जलिः (palms at the forehead)", "That too is the posture, not the verb of the sides."),
             ("मध्यं नपुंसकम् (middle: neuter)", "That is the next clause, which itself needs the verb.")],
            "The clauses वामं स्त्री and मध्यं नपुंसकम् borrow आश्रित्य अवतिष्ठते from the male clause.",
            "Elliptical clauses borrow the verb printed once."),
        mcq("transfer", 5, "By the join in पृष्ठाभिमुखो ललाटे, how is रामः + गच्छति written?",
            ("रामो गच्छति", "अः before a voiced consonant becomes ओ."),
            [("रामर्गच्छति", "र् comes only after vowels other than अ/आ."),
             ("रामा गच्छति", "अः does not become आ before a consonant."),
             ("रामस्गच्छति", "स् comes before त/थ, not before ग.")],
            "पृष्ठाभिमुखः + ललाटे → पृष्ठाभिमुखो ललाटे; so रामः + गच्छति → रामो गच्छति.",
            "अः + voiced consonant → ओ.",
            teaches="A final अः becomes ओ before a voiced consonant: पृष्ठाभिमुखः + ललाटे → पृष्ठाभिमुखो ललाटे."),
    ],
}

# ---------------------------------------------------------------- unit 56
AUTHORED["56"] = {
    "title": "तत्र स्थितश्च गर्भो",
    "question": "How does unit 56 tie the embryo's sleep and waking to the mother's?",
    "rule": "Staying there, the embryo sleeps when the mother is sleeping and wakes when she is awake.",
    "limits": ("The printed स्वापिति is read as स्वपिति (sleeps); the correction is only possible, so no question asks about "
               "that form. मातरि is understood again with प्रबुद्धायाम्."),
    "explain_hi": ("वहाँ (सम्भवतः गर्भकोष्ठ में) स्थित गर्भ माता के सोने पर सोता है और माता के जागने पर जाग जाता है। "
                   "‘मातरि स्वपन्त्याम्’ और ‘प्रबुद्धायाम्’ सति सप्तमी हैं: जब माता सो रही हो, जब वह जागी हो। "
                   "दूसरे खण्ड में ‘मातरि’ फिर समझा जाता है; ‘प्रबुद्धायाम्’ स्त्रीलिंग है, इसलिए जागी हुई माता है। "
                   "छपा ‘स्वापिति’ सम्भवतः ‘स्वपिति’ है।"),
    "hook": "माँ सोए तो गर्भ सोए, माँ जागे तो गर्भ जागे।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 56, when does the embryo wake?",
            ("When the mother is awake", "प्रबुद्धायाम् (मातरि) प्रबुध्यते: it wakes when she is awake."),
            [("At sunrise each day", "No time of day is named in this unit."),
             ("When the mother eats", "Eating is not named in this unit."),
             ("When it is touched", "Touch is not named in this unit.")],
            "The embryo follows the mother: it wakes when she is awake.",
            "प्रबुध्यते = wakes."),
        order(1, "Put these phrases of unit 56 in their printed order.",
              ["तत्र स्थितश्च", "गर्भो मातरि", "स्वपन्त्याम्", "प्रबुद्धायाम्", "प्रबुध्यते"],
              "Staying there, the embryo, when the mother is sleeping (sleeps); when awake, wakes.",
              "तत्र स्थितश्च → गर्भो मातरि → स्वपन्त्याम् → प्रबुद्धायाम् → प्रबुध्यते."),
        match(2, "Match each phrase of unit 56 to its meaning on the card.",
              [["तत्र", "there"], ["स्थितः", "staying"], ["मातरि स्वपन्त्याम्", "when the mother is sleeping"],
               ["प्रबुद्धायाम्", "when (she is) awake"], ["प्रबुध्यते", "wakes"]],
              "Place, the embryo's staying, the two states of the mother, and the waking.",
              "तत्र, स्थितः, मातरि स्वपन्त्याम्, प्रबुद्धायाम्, प्रबुध्यते.", role="extend",
              teaches="मातरि स्वपन्त्याम् is a locative absolute: 'when the mother is sleeping'."),
        mcq("discriminate", 3, "What is मातरि स्वपन्त्याम् in unit 56?",
            ("A locative absolute: when the mother is sleeping", "Both words are f. loc. sg.: a time-clause."),
            [("A main clause: the mother is sleeping now", "There is no finite verb in these two words."),
             ("An instrumental: by the mother who is sleeping", "The instrumental would be मात्रा स्वपन्त्या."),
             ("A genitive: of the mother who is sleeping", "The genitive would be मातुः स्वपन्त्याः.")],
            "Noun and participle together in the locative mark the time: when the mother is sleeping.",
            "Locative absolute = noun + participle in the locative: 'when …'."),
        mcq("apply", 4, "In प्रबुद्धायां प्रबुध्यते, who is awake (प्रबुद्धा), by the feminine ending?",
            ("The mother", "प्रबुद्धायाम् is feminine, so it goes with मातरि."),
            [("The embryo itself", "गर्भ is masculine and does the waking, प्रबुध्यते."),
             ("The father", "No father is named in this unit."),
             ("The midwife", "No midwife is named in this unit.")],
            "प्रबुद्धायाम् (f. loc. sg.) carries over मातरि: when the mother is awake, the embryo wakes.",
            "A feminine participle goes with a feminine noun."),
        mcq("transfer", 5, "An invented line reads पितरि सुप्ते पुत्रः पठति. What does it say?",
            ("When the father is asleep, the son reads", "पितरि सुप्ते is a locative absolute."),
            [("The father reads while the son sleeps", "पुत्रः goes with पठति; the father is the one asleep."),
             ("The son reads to the sleeping father", "No 'to' (dative) is expressed."),
             ("The son reads about his father's sleep", "No 'about' is expressed; पितरि is a time-clause.")],
            "As मातरि स्वपन्त्याम् = when the mother is sleeping, पितरि सुप्ते = when the father is asleep.",
            "Noun + participle in the locative = 'when …'.",
            teaches="A noun and a participle in the locative make a time-clause: पितरि सुप्ते = when the father is asleep."),
    ],
}

# ---------------------------------------------------------------- unit 57
AUTHORED["57"] = {
    "title": "परतंत्रवृत्तेश्च गर्भस्य",
    "question": "What quality of the embryo does unit 57 name?",
    "rule": "And because of the dependent functioning (paratantra-vṛtti, functioning under another's control) of the embryo.",
    "limits": ("A fragment with no verb. वृत्तेः is read as an ablative of reason; the genitive has the same form, "
               "so no question rests on the case. It probably gives the reason for unit 56 (sleeping and waking); not certain."),
    "explain_hi": ("यह पंक्ति एक वाक्यांश है, इसकी अपनी क्रिया नहीं। "
                   "अर्थ: और गर्भ की परतन्त्र वृत्ति के कारण, यानी उसका काम दूसरे (माता) के अधीन चलता है। "
                   "‘परतन्त्र’ = दूसरे के अधीन; ‘वृत्ति’ = कार्य, चलन। "
                   "‘वृत्तेः’ पंचमी (कारण) ली गई है, पर षष्ठी का रूप भी यही है। "
                   "सम्भवतः यह पास के कथन (माता के साथ सोना-जागना, इकाई ५६) का कारण बताती है; यह पक्का नहीं।"),
    "hook": "गर्भ परतन्त्र: उसकी वृत्ति दूसरे के अधीन।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 57, what kind of functioning does the embryo have?",
            ("Dependent: under another's control", "परतन्त्र = under another's control."),
            [("Free: under its own control", "That would be स्वतन्त्र, the opposite."),
             ("Absent: it has no functioning", "The unit names its functioning, वृत्ति."),
             ("Faulty: full of disorder", "No disorder is named in this unit.")],
            "परतन्त्रवृत्ति = functioning that depends on another.",
            "परतन्त्र = dependent, under another's control."),
        order(1, "Put the words of unit 57 in their printed order.",
              ["परतन्त्रवृत्तेः", "च", "गर्भस्य"],
              "Because of dependent functioning, and, of the embryo.",
              "परतन्त्रवृत्तेः → च → गर्भस्य."),
        match(2, "Match each word of unit 57 to its meaning on the card.",
              [["परतन्त्र", "under another's control"], ["वृत्ति", "functioning"], ["गर्भस्य", "of the embryo"],
               ["च", "and"]],
              "परतन्त्र + वृत्ति = dependent functioning; गर्भस्य names whose it is.",
              "परतन्त्र, वृत्ति, गर्भस्य, च.", role="extend",
              teaches="परतन्त्र means 'under another's control'; वृत्ति means functioning."),
        mcq("discriminate", 3, "Which split of वृत्तेश्च is right?",
            ("वृत्तेः + च", "Visarga before च becomes श्: वृत्तेः + च → वृत्तेश्च."),
            [("वृत्ते + श्च", "श्च is not a word of the card."),
             ("वृत्तेम् + च", "वृत्तेम् is no form of वृत्ति."),
             ("वृत्ते + अश्च", "ए + अ would leave ऽ, and अश्च is no word here.")],
            "वृत्तेः (because of / of the functioning) + च (and).",
            "Visarga + च/छ → श्."),
        multi("apply", 4, "Which two are true of unit 57, by the card?",
              [("It names the mother's heart", "The mother's heart is in unit 58, not here."),
               ("It has no verb of its own", "Right: it is a nominal fragment."),
               ("The form वृत्तेः can be ablative or genitive", "Right: both cases have this form; the card takes ablative."),
               ("It says the embryo acts on its own", "परतन्त्र says the opposite: under another's control.")],
              [1, 2],
              "Unit 57 is a fragment; its वृत्तेः is read as a reason, though the form is also genitive.",
              "Fragment; वृत्तेः = abl. or gen."),
        mcq("transfer", 5, "By the join in वृत्तेश्च, how is अग्नेः + च written?",
            ("अग्नेश्च", "Visarga before च becomes श्."),
            [("अग्ने च", "The visarga is not dropped before च; it becomes श्."),
             ("अग्नेर्च", "After ए the visarga becomes र् only before a voiced sound; च is voiceless."),
             ("अग्नेस्च", "Before च the visarga becomes श्, not स्.")],
            "वृत्तेः + च → वृत्तेश्च; so अग्नेः + च → अग्नेश्च.",
            "Visarga + च → श्च.",
            teaches="A visarga before च or छ becomes श्: अग्नेः + च → अग्नेश्च."),
    ],
}

# ---------------------------------------------------------------- unit 58
AUTHORED["58"] = {
    "title": "निषेकात्प्रभृति गर्भाशयोपस्नेहोपस्वेदौ वर्तनं",
    "question": "By unit 58, what sustains the embryo from impregnation onward, and what is fastened at its navel?",
    "rule": ("From niṣeka (impregnation) onward, the moistening (upasneha) and sweating or warming (upasveda) of the womb are the means "
             "of sustenance; a nāḍī (probably the umbilical cord) is fastened at the navel; then aparā and the mother's heart."),
    "limits": ("Two readings are conjectural: the limb compound (stray म and ऽ) and नाड्यांपरा read as नाड्याम् अपरा. "
               "प्रतिबद्धा is understood with the later links. A third-item reading of गर्भाशय is less likely. "
               "No question rests on the aparā link or on the limb compound."),
    "explain_hi": ("निषेक (गर्भाधान, मानक अर्थ) से लेकर गर्भाशय का उपस्नेह (भीगना) और उपस्वेद (पसीना या उष्णता) गर्भ का वर्तन, "
                   "यानी पोषण का साधन है। "
                   "उसके बाद, जब अंग-प्रत्यंग प्रकट होने लगते हैं (पाठ अनुमानित), उसकी नाभि में नाड़ी बँधी होती है; "
                   "नाड़ी सम्भवतः गर्भनाल है (सम्भावित पहचान)। "
                   "नाड़ी में अपरा यानी जेर (मानक अर्थ; पर यहाँ पाठ अनुमानित), और उसमें माता का हृदय। "
                   "‘प्रतिबद्धा’ (बँधी) एक बार छपा है और अगले जुड़ावों में समझा जाता है।"),
    "hook": "पहले भीगना-सिंकना पोषण; फिर नाभि से नाड़ी, नाड़ी से अपरा, अपरा से माँ का हृदय।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 58, from when onward are the womb's upasneha and upasveda the means of sustenance?",
            ("From impregnation", "निषेकात् प्रभृति: from impregnation onward."),
            [("From the birth of the child", "Birth is not the starting point named here."),
             ("From the fifth month", "No month is named in this unit."),
             ("From the first cry", "No cry is named in this unit.")],
            "निषेकात् (from impregnation) प्रभृति (onward).",
            "X-आत् प्रभृति = from X onward."),
        order(1, "Put these phrases of unit 58 in their printed order.",
              ["निषेकात्प्रभृति", "गर्भाशयोपस्नेहोपस्वेदौ", "वर्तनम्", "नाभ्यां प्रतिबद्धा नाडी", "मातृहृदयम्"],
              "From impregnation, moistening and warming of the womb are sustenance; then the duct at the navel; "
              "the mother's heart closes the line.",
              "निषेकात् → उपस्नेह-उपस्वेद → वर्तन → नाभि में नाडी → मातृहृदय."),
        match(2, "Match each word of unit 58 to its meaning on the card.",
              [["निषेक", "impregnation (standard)"], ["उपस्नेह", "moistening"], ["उपस्वेद", "sweating or warming"],
               ["वर्तन", "means of sustenance"], ["नाभि", "navel"]],
              "These words carry the sure first sentence and the navel link.",
              "निषेक, उपस्नेह, उपस्वेद, वर्तन, नाभि.", role="extend",
              teaches="वर्तन means the means of sustenance: at first, the womb's moistening and warming."),
        mcq("discriminate", 3, "By unit 58, what is fastened (प्रतिबद्धा) at the navel?",
            ("The nāḍī", "नाभ्यां प्रतिबद्धा नाडी: a duct is fastened at the navel."),
            [("The womb's moistening", "Moistening is the early sustenance, not a thing fastened."),
             ("The hair-pores of the body", "Hair-pores are not named in this unit."),
             ("The rasa of food", "The rasa of food is not named in this unit.")],
            "नाभ्याम् (at the navel) प्रतिबद्धा (fastened) नाडी (duct; probably the umbilical cord).",
            "नाभ्यां प्रतिबद्धा नाडी."),
        mcq("apply", 4, "Which join makes गर्भाशयोपस्नेह out of गर्भाशय + उपस्नेह?",
            ("अ + उ → ओ", "गर्भाशय ends in अ; with उ it gives ओ."),
            [("आ + उ → औ", "आ + उ gives ओ, never औ."),
             ("अ + ओ → ओ", "अ + ओ would give औ, and उपस्नेह begins with उ."),
             ("इ + उ → ओ", "गर्भाशय does not end in इ.")],
            "गर्भाशय + उपस्नेह → गर्भाशयोपस्नेह; likewise उपस्नेह + उपस्वेदौ → उपस्नेहोपस्वेदौ.",
            "अ/आ + उ/ऊ → ओ."),
        mcq("transfer", 5, "By the same join, how is नर + उत्तमः written?",
            ("नरोत्तमः", "अ + उ → ओ."),
            [("नरौत्तमः", "अ + उ gives ओ, not औ."),
             ("नरुत्तमः", "The अ does not vanish; अ + उ → ओ."),
             ("नरवुत्तमः", "अ + उ does not insert व्.")],
            "गर्भाशय + उपस्नेह → गर्भाशयोपस्नेह; so नर + उत्तमः → नरोत्तमः.",
            "अ + उ → ओ.",
            teaches="अ or आ before उ merges into ओ: नर + उत्तमः → नरोत्तमः."),
    ],
}

# ---------------------------------------------------------------- unit 59
AUTHORED["59"] = {
    "title": "ततो मातृहृदयात्",
    "question": "By unit 59, from where does the rasa of food come, how does it move, and what does it reach?",
    "rule": ("Then from the mother's heart the rasa of food (āhāra-rasa), pulsating through the vessels (dhamanī), "
             "reaches the aparā (placenta)."),
    "limits": ("धमनी as blood vessels is probable (the word is used of arteries and other channels). "
               "The print has आहारसो; the data reads it as आहाररसः (one र fewer in the print), so no question uses that form."),
    "explain_hi": ("तब माता के हृदय से आहार-रस धमनियों के द्वारा स्पन्दित होता हुआ (धड़कता, बहता) अपरा यानी जेर तक पहुँचता है। "
                   "धमनी यानी वाहिका; यहाँ सम्भवतः रक्तवाहिकाएँ (सम्भावित पहचान)। "
                   "‘स्पन्दमानः’ वर्तमान कृदन्त है: स्पन्दित होता हुआ। "
                   "छपा ‘आहारसो’ को डेटा ‘आहाररसः’ पढ़ता है।"),
    "hook": "माँ का हृदय → धमनियाँ (धड़कता रस) → अपरा।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 59, from where does the rasa of food set out?",
            ("From the mother's heart", "मातृहृदयात्: from the mother's heart."),
            [("From the embryo's navel", "The navel comes later, in unit 60."),
             ("From the mother's stomach", "The stomach is not named in this unit."),
             ("From the hair-pores", "Hair-pores belong to unit 62.")],
            "ततः मातृहृदयात्: then from the mother's heart.",
            "मातृहृदयात् = from the mother's heart (ablative)."),
        order(1, "Put these words of unit 59 in their printed order.",
              ["ततः", "मातृहृदयात्", "धमनीभिः", "स्पन्दमानः", "अपराम्", "उपैति"],
              "Then, from the mother's heart, through the vessels, pulsating, to the aparā, it reaches.",
              "ततः → मातृहृदयात् → धमनीभिः → स्पन्दमानः → अपराम् → उपैति."),
        match(2, "Match each word of unit 59 to its meaning on the card.",
              [["ततः", "then"], ["स्पन्दमानः", "pulsating"], ["अपराम्", "to the aparā (placenta)"], ["उपैति", "reaches"]],
              "These words carry the time, the manner, the goal and the verb.",
              "ततः, स्पन्दमानः, अपराम्, उपैति.", role="extend",
              teaches="उपैति (upa-√i) means 'reaches'; अपराम् is its goal, the aparā (placenta)."),
        mcq("discriminate", 3, "Which split of स्पन्दमानोऽपराम् is right?",
            ("स्पन्दमानः + अपराम्", "अः + अ → ओ, and the dropped अ is marked ऽ."),
            [("स्पन्दमान + अपराम्", "अ + अ would give आ: स्पन्दमानापराम्."),
             ("स्पन्दमानम् + अपराम्", "म् + अ would give स्पन्दमानमपराम्."),
             ("स्पन्दमानः + परम्", "The ऽ marks a dropped अ, so the word is अपराम्.")],
            "स्पन्दमानः (pulsating) + अपराम् (to the aparā).",
            "अः + अ → ओऽ."),
        mcq("apply", 4, "By unit 59, through what does the rasa of food move?",
            ("Through the dhamanīs (probably blood vessels)", "धमनीभिः: through the vessels, instrumental plural."),
            [("Through the hair-pores of the mother's skin", "Hair-pores are named in unit 62, not here."),
             ("Through the mouth and throat of the embryo", "No mouth or throat is named in this unit."),
             ("Through the large intestine (pakvāśaya)", "The pakvāśaya comes in unit 61, not here.")],
            "धमनीभिः स्पन्दमानः: pulsating through the dhamanīs.",
            "धमनी = vessel (probably blood vessel)."),
        mcq("transfer", 5, "By the join in स्पन्दमानोऽपराम्, how is बालः + अपि written?",
            ("बालोऽपि", "अः + अ → ओ, with ऽ for the dropped अ."),
            [("बालापि", "अः + अ does not give आ."),
             ("बालरपि", "र् is not used after अ."),
             ("बालौपि", "अः + अ does not give औ.")],
            "स्पन्दमानः + अपराम् → स्पन्दमानोऽपराम्; so बालः + अपि → बालोऽपि.",
            "अः + अ → ओऽ.",
            teaches="A final अः before अ becomes ओ and the अ is dropped (ऽ): बालः + अपि → बालोऽपि."),
    ],
}

# ---------------------------------------------------------------- unit 60
AUTHORED["60"] = {
    "title": "ततः क्रमान्नाभिं",
    "question": "What does the fragment of unit 60 add, and what does it lack?",
    "rule": "Then, in sequence, to the navel. No verb is printed.",
    "limits": ("A fragment: no verb is printed and none is supplied. It appears to continue the movement of unit 59 (उपैति) "
               "and to lead into unit 61, but the card keeps to its own three words."),
    "explain_hi": ("यह तीन शब्दों का वाक्यांश है: तब क्रम से नाभि को। "
                   "इसमें कोई क्रिया नहीं छपी। "
                   "डेटा के अनुसार यह इकाई ५९ की गति (‘उपैति’, पहुँचता है) को आगे बढ़ाता लगता है और इकाई ६१ की ओर ले जाता है। "
                   "‘क्रमात्’ यानी क्रम से, एक-एक चरण; ‘नाभिम्’ द्वितीया: नाभि की ओर।"),
    "hook": "फिर क्रम से नाभि की ओर (क्रिया नहीं छपी)।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "What does क्रमात् mean in unit 60?",
            ("In sequence, step by step", "क्रमात् (abl. of क्रम) = in sequence."),
            [("All at once", "That is the opposite of क्रमात्."),
             ("Against the flow", "No contrary motion is named."),
             ("From the heart", "That is मातृहृदयात् in unit 59.")],
            "ततः क्रमात् नाभिम्: then, in sequence, to the navel.",
            "क्रमात् = in sequence."),
        order(1, "Put the words of unit 60 in their printed order.",
              ["ततः", "क्रमात्", "नाभिम्"],
              "Then → in sequence → to the navel.",
              "ततः → क्रमात् → नाभिम्."),
        fill(2, "Unit 60 reads ततः क्रमात् ____ (to the navel). Type it in Devanagari or in English letters (e.g. dharma).",
             accepts("नाभिम्", None, "nabhim"),
             "नाभिम् is the accusative of नाभि (navel): to the navel.",
             "नाभिम् (acc. of नाभि) = to the navel.",
             "नाभिम् = to the navel."),
        mcq("discriminate", 3, "Which split of क्रमान्नाभिम् is right?",
            ("क्रमात् + नाभिम्", "त् before the nasal न may become न् (optional; द् is also correct): क्रमात् + नाभिम् → क्रमान्नाभिम्."),
            [("क्रमम् + नाभिम्", "That would give क्रमं नाभिम् or क्रमन्नाभिम्, with a short अ; the print has क्रमा-."),
             ("क्रमा + न्नाभिम्", "न्नाभिम् is not a word of the card."),
             ("क्रमात् + अन्नाभिम्", "अन्नाभिम् is not a word of the card.")],
            "क्रमात् (in sequence) + नाभिम् (to the navel).",
            "त् + न → न्न (optional; द् is also correct)."),
        mcq("apply", 4, "What does unit 60 lack that a full sentence needs?",
            ("A verb: none is printed", "The data notes that no verb is printed and none is supplied."),
            [("A noun: none is printed", "नाभिम् is a noun."),
             ("An ablative: none is printed", "क्रमात् is an ablative."),
             ("A word for 'then'", "ततः means 'then'.")],
            "ततः, क्रमात् and नाभिम् are there; a verb is not.",
            "A fragment lacks its own finite verb."),
        mcq("transfer", 5, "By the join in क्रमान्नाभिम्, how may तत् + नगरम् be written?",
            ("तन्नगरम्", "त् before न may become न् (optional; तद्नगरम् is also correct), as in क्रमान्नाभिम्."),
            [("ततनगरम्", "No vowel is inserted after त्."),
             ("तच्नगरम्", "च् comes before च/छ, not before न."),
             ("तस्नगरम्", "त् does not become स् here.")],
            "क्रमात् + नाभिम् → क्रमान्नाभिम्; so तत् + नगरम् → तन्नगरम्.",
            "त् + nasal → न् + nasal (optional; द् is also correct).",
            teaches="A final त् before a nasal such as न may become न् (optional; द् is also correct): तत् + नगरम् → तन्नगरम्."),
    ],
}

# ---------------------------------------------------------------- unit 61
AUTHORED["61"] = {
    "title": "ततश्च स पुनर्गर्भस्य पक्वाशये",
    "question": "By unit 61, where and by what is the rasa cooked, and what does it then become?",
    "rule": ("Then it (the rasa) again, in the embryo's pakvāśaya, cooked by its own bodily fire (kāyāgni), "
             "through the abundance of the clear part (prasāda) becomes nourishing to the dhātus and the rest."),
    "limits": ("पक्वाशय as the large intestine is probable. Whose 'own' (स्व-) fire is meant is not stated, so no question asks it. "
               "पुनः is read as 'again, then in turn'. Which dhātus are meant is not listed."),
    "explain_hi": ("और तब वह (इकाई ५९ का आहार-रस) फिर गर्भ के पक्वाशय में, अपनी कायाग्नि यानी शरीर की पाचन-अग्नि (मानक अर्थ) से पकता हुआ, "
                   "प्रसाद यानी निर्मल भाग की अधिकता से धातु आदि की पुष्टि करने वाला हो जाता है। "
                   "पक्वाशय यानी पचे हुए पदार्थ का स्थान; बड़ी आँत इसका सामान्य समानार्थ है (सम्भावित पहचान)। "
                   "‘धातु’ शास्त्रीय शब्द है, अनुवाद नहीं किया गया।"),
    "hook": "पक्वाशय में, कायाग्नि से पका रस: प्रसाद अधिक, तो धातुएँ पुष्ट।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 61, where is the rasa cooked?",
            ("In the embryo's pakvāśaya", "गर्भस्य पक्वाशये: in the embryo's pakvāśaya."),
            [("In the mother's heart", "The mother's heart is where it sets out, unit 59."),
             ("In the aparā (placenta)", "The aparā is reached in unit 59; cooking is not said there."),
             ("In the hair-pores", "Hair-pores belong to unit 62.")],
            "पक्वाशय = site of digested matter, probably the large intestine.",
            "पक्वाशये = in the pakvāśaya (locative)."),
        order(1, "Put these phrases of unit 61 in their printed order.",
              ["गर्भस्य पक्वाशये", "स्वकायाग्निना", "पच्यमानः", "प्रसादबाहुल्यात्", "धात्वादिपुष्टिकरः", "सम्पद्यते"],
              "Place, fire, being cooked, the cause (abundance of prasāda), the result, the verb.",
              "पक्वाशये → स्वकायाग्निना → पच्यमानः → प्रसादबाहुल्यात् → धात्वादिपुष्टिकरः → सम्पद्यते."),
        match(2, "Match each word of unit 61 to its meaning on the card.",
              [["कायाग्नि", "bodily (digestive) fire"], ["पच्यमान", "being cooked"], ["प्रसाद", "the clear part"],
               ["बाहुल्य", "abundance"], ["पुष्टिकर", "nourishing"]],
              "Fire cooks it; the abundance of the clear part makes it nourishing.",
              "कायाग्नि, पच्यमान, प्रसाद, बाहुल्य, पुष्टिकर.", role="extend",
              teaches="प्रसाद is the clear, pure part of what is digested; its abundance nourishes the dhātus."),
        mcq("discriminate", 3, "Which split of बाहुल्याद्धात्वादि is right?",
            ("बाहुल्यात् + धात्वादि", "त् before the voiced ध becomes द्: बाहुल्याद्धात्वादि."),
            [("बाहुल्यात् + हात्वादि", "हात्वादि is not a word of the card."),
             ("बाहुल्या + द्धात्वादि", "द्धात्वादि is not a word of the card."),
             ("बाहुल्यम् + धात्वादि", "म् before ध would not give द्ध.")],
            "प्रसादबाहुल्यात् (from abundance of the clear part) + धात्वादि (dhātus and the rest).",
            "त् + voiced consonant → द्."),
        mcq("apply", 4, "In unit 61, what does सः (it) stand for, given its masculine form?",
            ("The rasa of food of unit 59", "The data reads सः as that rasa (masculine रसः)."),
            [("The mother's heart (हृदय)", "हृदय is neuter; सः is masculine."),
             ("The duct (नाडी)", "नाडी is feminine; सः is masculine."),
             ("The aparā (अपरा)", "अपरा is feminine; सः is masculine.")],
            "सः (m.) = the āhāra-rasa that reached the aparā in unit 59.",
            "A pronoun agrees in gender with what it stands for."),
        mcq("transfer", 5, "By the join in बाहुल्याद्धात्वादि, how is मार्गात् + गच्छति written?",
            ("मार्गाद्गच्छति", "त् before the voiced ग becomes द्."),
            [("मार्गात्गच्छति", "त् cannot stay voiceless before ग."),
             ("मार्गान्गच्छति", "न् comes before a nasal, not before ग."),
             ("मार्गाग्गच्छति", "त् does not become ग् here.")],
            "बाहुल्यात् + धातु → बाहुल्याद्धातु; so मार्गात् + गच्छति → मार्गाद्गच्छति.",
            "त् + voiced consonant → द्.",
            teaches="A final त् becomes द् before a voiced consonant: मार्गात् + गच्छति → मार्गाद्गच्छति."),
    ],
}

# ---------------------------------------------------------------- unit 62
AUTHORED["62"] = {
    "title": "तथा रोमकूपैरुपस्नेहो",
    "question": "Through what does unit 62 say there is moistening (upasneha)?",
    "rule": "Likewise, through the hair-pores there is moistening (upasneha), and the rasa itself having become payas.",
    "limits": ("Low confidence. पयस् can mean milk or water and the line does not say which; the second half is not a full "
               "sentence and its sense is not firm. Questions on the second half ask only its printed words and their order, "
               "never its sense or पयस्."),
    "explain_hi": ("इस पंक्ति का विश्वास कम है। पहला खण्ड अपेक्षाकृत स्पष्ट है: वैसे ही रोमकूपों से उपस्नेह (भीगना) होता है। "
                   "दूसरा खण्ड अधूरा है: ‘रस ही पयस् बना हुआ’; पयस् का अर्थ दूध या जल, पंक्ति नहीं बताती। "
                   "‘रोमकूपैः’ तृतीया बहुवचन है: रोमकूपों के द्वारा। "
                   "‘होता है’ समझा गया है, छपा नहीं।"),
    "hook": "रोमकूपों से भी भीगना: उपस्नेह।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 62, through what is there moistening (upasneha)?",
            ("Through the hair-pores", "रोमकूपैः उपस्नेहः: moistening through the hair-pores."),
            [("Through the mouth", "No mouth is named in this unit."),
             ("Through the navel duct", "The nāḍī is named in unit 58, not here."),
             ("Through the dhamanīs", "The dhamanīs carry rasa in unit 59.")],
            "रोम (hair) + कूप (pit, pore): the hair-pores.",
            "रोमकूप = hair-pore."),
        order(1, "Put these words of unit 62 in their printed order.",
              ["तथा", "रोमकूपैः", "उपस्नेहः", "रसः एव", "च", "पयोभूतः"],
              "Likewise, through the hair-pores, moistening; the rasa itself, and, having become payas.",
              "तथा → रोमकूपैः → उपस्नेहः → रसः एव → च → पयोभूतः."),
        match(2, "Match each word of unit 62 to its meaning on the card.",
              [["तथा", "likewise"], ["उपस्नेहः", "moistening"], ["एव", "itself, only"]],
              "तथा links the line to what precedes; उपस्नेह is the moistening; एव stresses रसः.",
              "तथा, उपस्नेहः, एव.", role="extend",
              teaches="उपस्नेह means moistening; तथा (likewise) adds it to the ways named before."),
        mcq("discriminate", 3, "Which split of रोमकूपैरुपस्नेहो is right?",
            ("रोमकूपैः + उपस्नेहः", "Visarga after ऐ becomes र् before a vowel."),
            [("रोमकूपै + रुपस्नेहः", "रुपस्नेहः is not a word of the card."),
             ("रोमकूपम् + उपस्नेहः", "म् + उ would give रोमकूपमुपस्नेहः."),
             ("रोमकूपैर + उपस्नेहः", "रोमकूपैर is no full word; the ending is -ऐः.")],
            "रोमकूपैः (through the hair-pores) + उपस्नेहः (moistening).",
            "ऐः + vowel → ऐर् + vowel."),
        mcq("apply", 4, "What form is रोमकूपैः in unit 62?",
            ("Instrumental plural: through the hair-pores", "-ऐः is the instrumental plural of an अ-stem."),
            [("Locative plural: in and inside the hair-pores", "The locative plural would be रोमकूपेषु."),
             ("Genitive plural: belonging to the hair-pores", "The genitive plural would be रोमकूपाणाम्."),
             ("Nominative singular: one single hair-pore", "The nominative singular would be रोमकूपः.")],
            "रोमकूपैः = by / through the hair-pores (inst. pl.).",
            "अ-stem inst. pl. → -ऐः."),
        mcq("transfer", 5, "By the join in रोमकूपैरुपस्नेहो, how is अश्वैः + आगतम् written?",
            ("अश्वैरागतम्", "Visarga after ऐ becomes र् before a vowel."),
            [("अश्वैआगतम्", "The visarga cannot simply drop here."),
             ("अश्वैसागतम्", "स् comes before त/थ, not before a vowel."),
             ("अश्वायागतम्", "ऐः does not turn into आय्.")],
            "रोमकूपैः + उपस्नेहः → रोमकूपैरुपस्नेहः; so अश्वैः + आगतम् → अश्वैरागतम्.",
            "ऐः + vowel → ऐर्.",
            teaches="A visarga after ऐ becomes र् before a vowel: अश्वैः + आगतम् → अश्वैरागतम्."),
    ],
}

# ---------------------------------------------------------------- unit 63
AUTHORED["63"] = {
    "title": "अजातस्य साक्षादन्नपानाननुप्रवेशात्",
    "question": "Why, by unit 63, does gross waste not arise in the unborn embryo?",
    "rule": ("In the unborn embryo gross waste (sthūla-mala) does not arise, because food and drink do not enter directly "
             "and because the rasa is free from mala (amala)."),
    "limits": ("The genitives can also be read 'of the rasa of the unborn embryo'; no question rests on whose rasa. "
               "The text speaks only of gross waste; it does not say whether fine waste arises."),
    "explain_hi": ("जन्म न लिए हुए गर्भ में स्थूल मल उत्पन्न नहीं होता। "
                   "इसके दो कारण दिए हैं: अन्न और पान का सीधा (साक्षात्) प्रवेश नहीं होता, और रस अमल यानी मल-रहित होता है। "
                   "‘अननुप्रवेशात्’ और ‘अमलत्वात्’ पंचमी हैं: कारण बताते हैं। "
                   "पाठ केवल स्थूल मल की बात करता है; सूक्ष्म मल के बारे में कुछ नहीं कहता।"),
    "hook": "न सीधा अन्न-पान, न मलिन रस: इसलिए गर्भ में स्थूल मल नहीं।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 63, what does not arise in the unborn embryo?",
            ("Gross waste", "स्थूलमलासम्भवः: non-arising of gross waste."),
            [("The rasa of food", "The rasa is there; it is free of mala."),
             ("Sleep and waking", "Sleep is unit 56's topic; not named here."),
             ("The bodily fire", "No fire is named in this unit.")],
            "स्थूल (gross) + मल (waste) + असम्भव (non-arising).",
            "स्थूलमलासम्भव = gross waste does not arise."),
        order(1, "Put these phrases of unit 63 in their printed order.",
              ["अजातस्य", "साक्षादन्नपानाननुप्रवेशात्", "अमलत्वाच्च रसस्य", "गर्भस्य", "स्थूलमलासम्भवः"],
              "Of the unborn; because food and drink do not enter directly; and because the rasa is stainless; of the embryo; "
              "no gross waste.",
              "अजातस्य → अन्नपान-अननुप्रवेशात् → अमलत्वात् च रसस्य → गर्भस्य → स्थूलमलासम्भवः."),
        match(2, "Match each word of unit 63 to its meaning on the card.",
              [["अजात", "unborn"], ["साक्षात्", "directly"], ["अननुप्रवेश", "non-entry"], ["अमलत्व", "being free of waste"],
               ["असम्भव", "non-arising"]],
              "Four of the words carry the negative अ-/अन्-: अजात (unborn), अननुप्रवेश (non-entry), अमलत्व (being free of waste), असम्भव (non-arising).",
              "अजात, साक्षात्, अननुप्रवेश, अमलत्व, असम्भव.", role="extend",
              teaches="अ- or अन्- before a word negates it: अजात = unborn, अननुप्रवेश = non-entry."),
        multi("discriminate", 3, "Which two reasons does unit 63 give?",
              [("The mother's fire burns the waste", "No fire is named in this unit."),
               ("Food and drink do not enter directly", "Right: साक्षात् अन्नपान-अननुप्रवेशात्."),
               ("The hair-pores carry the waste out", "Hair-pores are not named here."),
               ("The rasa is free from mala", "Right: अमलत्वात् रसस्य.")],
              [1, 3],
              "Two ablatives of reason: अननुप्रवेशात् and अमलत्वात्.",
              "Ablative (-आत्) = because of."),
        mcq("apply", 4, "What does unit 63 say about fine (subtle) waste in the embryo?",
            ("Nothing: it speaks only of gross waste", "स्थूल limits the statement to gross waste."),
            [("That fine waste also arises", "The unit does not say so."),
             ("That no waste of any kind arises", "Only gross (स्थूल) waste is denied."),
             ("That fine waste leaves by the navel", "Nothing of the kind is said.")],
            "The text denies only स्थूल मल; about fine waste it is silent.",
            "Read the qualifier: स्थूल = gross."),
        mcq("transfer", 5, "By the negative in अननुप्रवेश, how is the negative of उदय (rise) formed?",
            ("अनुदय", "Before a vowel the negative prefix is अन्-: अन् + उदय."),
            [("अउदय", "अ- stands only before a consonant."),
             ("नोदय", "न + उदय is a sandhi of two words, not the prefix."),
             ("अदुदय", "No द् comes into the negative prefix.")],
            "अन् + अनुप्रवेश → अननुप्रवेश; so अन् + उदय → अनुदय. Before a consonant: अ + जात → अजात.",
            "Negative prefix: अ- before a consonant, अन्- before a vowel.",
            teaches="The negative prefix is अ- before a consonant (अजात, असम्भव) and अन्- before a vowel (अननुप्रवेश, अनुदय)."),
    ],
}


# ===================================================================== NOTES_HI
NOTES_HI = {
    "51": ("विश्वास ऊँचा। ‘शुचिर्ब्रह्मचारिणी’ = शुचिः + ब्रह्मचारिणी: दो अलग विशेषण, समास नहीं (विसर्ग इ के बाद घोष ब से पहले र्)। "
           "सन्धियाँ: प्रतिषेध + अर्थम् → प्रतिषेधार्थम् (छपा ‘ार्थं’, अनुस्वार); दैवत + आराधन → दैवताराधन (अ + आ → आ); "
           "तस्मात् + प्रसव → तस्मात्प्रसव (त् अघोष प से पहले अपरिवर्तित)। ब्रह्मचारिणी = ब्रह्मचर्य पालने वाली, यहाँ ‘संयमी, ब्रह्मचर्य का पालन करने वाली’ (chaste), जैसा डेटा लेता है।"),
    "52": ("विश्वास ऊँचा। ‘निर्वपेत्’ का कर्ता नहीं छपा। ‘अत्र’ = इस स्थिति में (इकाई ५१ की स्थिति)। ओदन = पका चावल (मानक)। "
           "सन्धियाँ: मांस + ओदन → मांसौदन (अ + ओ → औ); बलिम् + च → बलिं च; च + अत्र → चात्र (अ + अ → आ)।"),
    "53": ("विश्वास कम: अनुवाद शाब्दिक, अर्थ पक्का नहीं। ‘तस्मिन्’ किसकी ओर है, स्पष्ट नहीं। ‘आसंवत्सरात्’ = आ + पंचमी, वर्ष तक। "
           "सन्धियाँ: तस्मिन् + एक → तस्मिन्नेक (ह्रस्व स्वर के बाद न् स्वर से पहले द्वित्व); दिवस + अतिक्रान्ते → दिवसातिक्रान्ते; "
           "अतिक्रान्ते + अपि → अतिक्रान्तेऽपि; प्रसवकालम् + आहुः → प्रसवकालमाहुः; आहुः + आसंवत्सरात् → आहुरासंवत्सरात्। "
           "छपा ‘क्रांते’ में न् के स्थान पर अनुस्वार।"),
    "54": ("विश्वास मध्यम। कर्ता नहीं छपा; सम्भवतः शिशु, पाठ नहीं कहता। ‘विकारी’ पुंलिंग प्रथमा एकवचन (विकारिन्)। विकार का प्रकार नहीं बताया। "
           "‘अतःपरं’ छपाई में एक साथ; परम् + विकारी → परं विकारी (म् व्यंजन से पहले अनुस्वार)।"),
    "55": ("विश्वास ऊँचा। ‘आश्रित्य अवतिष्ठते’ एक बार छपा, ‘वामं स्त्री’ और ‘मध्यं नपुंसकं’ में समझा जाता है। "
           "गर्भकोष्ठ = गर्भाशय की गुहा (सम्भावित)। सन्धियाँ: गर्भः + तु → गर्भस्तु; पृष्ठ + अभिमुखः → पृष्ठाभिमुखः, + ललाटे → पृष्ठाभिमुखो ललाटे; "
           "कृत + अञ्जलिः → कृताञ्जलिः (छपा ‘कृतांजलिः’); संकुचित + अङ्गः → संकुचिताङ्गः, + गर्भ → संकुचिताङ्गो गर्भ; "
           "पार्श्वम् + आश्रित्य → पार्श्वमाश्रित्य; आश्रित्य + अवतिष्ठते → आश्रित्यावतिष्ठते।"),
    "56": ("पाठ-सूचना: छपा ‘स्वापिति’ सामान्य वर्तमान रूप नहीं (णिजन्त ‘स्वापयति’ होता); ‘स्वपिति’ सम्भावित सुधार, ‘स्वपन्त्याम्’ से मेल खाता है। "
           "‘गर्भोमातरि’ छपाई में बिना दूरी: गर्भः + मातरि → गर्भो मातरि। स्थितः + च → स्थितश्च। "
           "‘मातरि स्वपन्त्याम्’ और ‘प्रबुद्धायाम्’ सति सप्तमी; दूसरे में मातरि समझा जाता है। छपा ‘स्वपंत्यां’ = स्वपन्त्याम्।"),
    "57": ("विश्वास मध्यम। वाक्यांश, अपनी क्रिया नहीं। ‘वृत्तेः’ पंचमी (कारण) ली गई; षष्ठी का रूप भी यही, दोनों अर्थ सम्भव। "
           "सम्भवतः पास के कथन (इकाई ५६) का कारण, पक्का नहीं। सन्धि: वृत्तेः + च → वृत्तेश्च (विसर्ग + च → श्च)। छपा ‘परतंत्र’ = परतन्त्र।"),
    "58": ("विश्वास मध्यम। दो अनुमानित पाठ: (१) ‘नाड्यांपरा’ को ‘नाड्याम् अपरा’ पढ़ा गया, क्योंकि इकाई ५९ में ‘अपराम्’ अगली कड़ी है; "
           "(२) ‘व्यक्तीभवदंगमप्रत्यंगस्याऽस्य’ में ‘म’ फालतू लगता है और ‘ऽ’ गलत (अ + अ → आ: प्रत्यङ्गस्यास्य)। "
           "‘प्रतिबद्धा’ अपरा और मातृहृदय के साथ भी समझा जाता है। गर्भाशय को द्वन्द्व का तीसरा पद मानने का पाठ कम सम्भव। "
           "निषेक = वीर्य-सेचन, गर्भाधान (मानक); नाडी = गर्भनाल (सम्भावित); अपरा = जेर (मानक)। "
           "सन्धियाँ: गर्भ + आशय → गर्भाशय; आशय + उपस्नेह → आशयोपस्नेह (अ + उ → ओ); उपस्नेह + उपस्वेदौ → उपस्नेहोपस्वेदौ; ततः + व्यक्ती → ततो व्यक्ती।"),
    "59": ("विश्वास ऊँचा। छपा ‘मातृहृदयादाहारसो’ में ‘आहारसो’ है, जबकि डेटा इसे ‘आहाररसः’ (आहार-रस) पढ़ता है: छपाई में एक ‘र’ कम लगता है "
           "(डेटा ने इसे पाठ-सूचना में नहीं रखा)। धमनी = वाहिका, यहाँ सम्भवतः रक्तवाहिकाएँ (सम्भावित)। "
           "सन्धियाँ: ततः + मातृ → ततो मातृ; हृदयात् + आहार → हृदयादाहार; रसः + धमनीभिः → रसो धमनीभिः; "
           "स्पन्दमानः + अपराम् → स्पन्दमानोऽपराम्; अपराम् + उपैति → अपरामुपैति; उप + एति → उपैति (अ + ए → ऐ)।"),
    "60": ("विश्वास मध्यम। वाक्यांश: कोई क्रिया नहीं छपी, न जोड़ी गई। डेटा के अनुसार यह इकाई ५९ की गति (उपैति) को आगे बढ़ाता और इकाई ६१ की ओर ले जाता लगता है। "
           "सन्धियाँ: क्रमात् + नाभिम् → क्रमान्नाभिम् (त् + न → न्न, विकल्प से; द् भी शुद्ध); ततः + क्रमात् → ततः क्रमात् (क से पहले विसर्ग बना रहता)। छपा ‘नाभिं’ = नाभिम्।"),
    "61": ("विश्वास मध्यम। ‘सः’ = इकाई ५९ का आहार-रस। कायाग्नि = शरीर की पाचन-अग्नि (मानक); पक्वाशय = बड़ी आँत (सम्भावित)। "
           "‘स्व-’ (अपनी) किसकी, यह नहीं कहा। ‘पुनर्’ = फिर, बदले में। "
           "सन्धियाँ: ततः + च → ततश्च; सः + पुनः → स पुनः; पुनः + गर्भस्य → पुनर्गर्भस्य; काय + अग्निना → कायाग्निना; "
           "बाहुल्यात् + धातु → बाहुल्याद्धातु (त् + ध → द्ध); धातु + आदि → धात्वादि (उ + आ → वा)।"),
    "62": ("विश्वास कम। पयस् = दूध या जल; पंक्ति नहीं बताती। दूसरा खण्ड अधूरा, अर्थ पक्का नहीं; ‘होता है’ समझा गया। "
           "छपा ‘रसएव’ = रसः + एव → रस एव (अः + ए → अ, बीच में विराम)। "
           "सन्धियाँ: रोमकूपैः + उपस्नेहः → रोमकूपैरुपस्नेहः; उपस्नेहः + रसः → उपस्नेहो रसः; पयः + भूतः → पयोभूतः।"),
    "63": ("विश्वास मध्यम। ‘अजातस्य’, ‘गर्भस्य’ और ‘रसस्य’ तीनों षष्ठी: ‘अजन्मे गर्भ के रस का’ ऐसा पाठ भी सम्भव। ‘होता है’ समझा गया। "
           "केवल स्थूल मल का निषेध; सूक्ष्म मल पर मौन। सन्धियाँ: साक्षात् + अन्न → साक्षादन्न; पान + अननुप्रवेशात् → पानाननुप्रवेशात्; "
           "अनुप्रवेशात् + अमल → अनुप्रवेशादमल; अमलत्वात् + च → अमलत्वाच्च; मल + असम्भवः → मलासम्भवः।"),
}

# ===================================================================== AIDS
AIDS = {
    "51": {
        "chunks": "तस्मात् | प्रसवप्रतिषेधार्थं | स्त्री | स्नाता | शुचिर्ब्रह्मचारिणी | दैवताराधनपरमा | स्यात्।",
        "sandhi": "इः + ब → इर्ब: शुचिः + ब्रह्मचारिणी → शुचिर्ब्रह्मचारिणी · अ + आ → आ: दैवत + आराधन → दैवताराधन · अ + अ → आ: प्रतिषेध + अर्थम् → प्रतिषेधार्थम्।",
        "letters": "मेरी याद-पद्धति: स्ना-शु-ब्र-दै (स्नाता, शुचिः, ब्रह्मचारिणी, दैवताराधनपरमा), छपे क्रम में।",
    },
    "52": {
        "frame": "मांसौदनबलिम् (क्या) → च अत्र (और यहाँ) → निर्वपेत् (अर्पित करे): विधि-वाक्य, कर्ता नहीं छपा।",
        "sandhi": "अ + ओ → औ: मांस + ओदन → मांसौदन · अ + अ → आ: च + अत्र → चात्र · म् + व्यंजन → ं: बलिम् + च → बलिं च।",
        "pegs": "मेरा बनाया चित्र: एक पत्तल पर मांस और भात, ऊपर लिखा ‘बलि’। (केवल याद के लिए)",
    },
    "53": {
        "chunks": "तस्मिन्नेकदिवसातिक्रान्तेऽपि | प्रसवकालम् | आहुः | आसंवत्सरात्।",
        "sandhi": "न् + ए → न्ने: तस्मिन् + एक → तस्मिन्नेक · ए + अ → एऽ: अतिक्रान्ते + अपि → अतिक्रान्तेऽपि · उः + आ → उरा: आहुः + आसंवत्सरात् → आहुरासंवत्सरात्।",
        "frame": "‘आहुः’ = वे कहते हैं: यह दूसरों का मत बताया गया है; अर्थ पक्का नहीं।",
    },
    "54": {
        "frame": "अतःपरम् (इसके बाद) → विकारी (विकार वाला) → भवति (होता है)। कर्ता नहीं छपा, विकार का प्रकार नहीं बताया।",
        "puns": "मेरी बनाई, केवल सुनने की सहायता: ‘वि-कारी’: जो ‘विकार’ वाला हो जाए।",
    },
    "55": {
        "diagram": {"groups": [
            {"label": "मुद्रा", "items": ["माता की पीठ की ओर मुख", "ललाट पर अञ्जलि", "अंग सिकुड़े", "गर्भकोष्ठ में"]},
            {"label": "पार्श्व", "items": ["दाहिना: पुमान्", "बायाँ: स्त्री", "मध्य: नपुंसक"]}]},
        "sandhi": "अः + ल → ओ ल: पृष्ठाभिमुखः + ललाटे → पृष्ठाभिमुखो ललाटे · अ + अ → आ: आश्रित्य + अवतिष्ठते → आश्रित्यावतिष्ठते · अः + त → स्त: गर्भः + तु → गर्भस्तु।",
        "anchors": "दाएँ-बाएँ-बीच = पुमान्-स्त्री-नपुंसक (छपे क्रम में)।",
        "frame": "‘आश्रित्य अवतिष्ठते’ एक बार छपा, ‘वामं स्त्री’ और ‘मध्यं नपुंसकम्’ में समझा जाता है।",
    },
    "56": {
        "seesaw": "माता सोती ↔ माता जागती: गर्भ भी सोता ↔ गर्भ भी जागता।",
        "sandhi": "अः + च → श्च: स्थितः + च → स्थितश्च · अः + म → ओ म: गर्भः + मातरि → गर्भो मातरि।",
        "frame": "मातरि स्वपन्त्याम् / प्रबुद्धायाम्: सति सप्तमी (‘जब माता …’); दूसरे में ‘मातरि’ समझा गया।",
    },
    "57": {
        "frame": "परतन्त्रवृत्तेः (दूसरे के अधीन वृत्ति के कारण) च गर्भस्य: वाक्यांश, क्रिया नहीं।",
        "sandhi": "विसर्ग + च → श्च: वृत्तेः + च → वृत्तेश्च।",
    },
    "58": {
        "chain": {"steps": ["निषेक से: गर्भाशय का उपस्नेह-उपस्वेद वर्तन", "नाभि में बँधी नाडी (सम्भवतः गर्भनाल)",
                            "नाडी में अपरा (पाठ अनुमानित)", "उसमें माता का हृदय (बँधा, समझा गया)"]},
        "sandhi": "अ + उ → ओ: आशय + उपस्नेह → आशयोपस्नेह; उपस्नेह + उपस्वेदौ → उपस्नेहोपस्वेदौ · अ + आ → आ: गर्भ + आशय → गर्भाशय · अः + व → ओ व: ततः + व्यक्ती → ततो व्यक्ती।",
        "chunks": "निषेकात्प्रभृति | गर्भाशयोपस्नेहोपस्वेदौ वर्तनं | ततो व्यक्तीभवदङ्गप्रत्यङ्गस्यास्य (अनुमानित) | नाभ्यां प्रतिबद्धा नाडी | नाड्यामपरा (अनुमानित) | तस्यां मातृहृदयम्।",
    },
    "59": {
        "chain": {"steps": ["माता का हृदय", "आहार-रस धमनियों से", "स्पन्दित होता हुआ", "अपरा तक पहुँचता"]},
        "sandhi": "अः + अ → ओऽ: स्पन्दमानः + अपराम् → स्पन्दमानोऽपराम् · अ + ए → ऐ: उप + एति → उपैति · त् + आ → दा: हृदयात् + आहार → हृदयादाहार।",
        "anchors": "हृदय → धमनी → अपरा: ‘ह-ध-अ’ (मेरी याद-पद्धति)।",
    },
    "60": {
        "chain": {"steps": ["इकाई ५९: माता के हृदय से धमनियों द्वारा अपरा तक", "इकाई ६०: फिर क्रम से नाभि की ओर (क्रिया नहीं छपी, जुड़ाव सम्भावित)",
                            "इकाई ६१: गर्भ के पक्वाशय में पकता"]},
        "sandhi": "त् + न → न्न (विकल्प से; द् भी शुद्ध): क्रमात् + नाभिम् → क्रमान्नाभिम् · विसर्ग क से पहले बना रहता: ततः + क्रमात् → ततः क्रमात्।",
        "frame": "ततः (फिर) → क्रमात् (क्रम से) → नाभिम् (नाभि को): केवल तीन शब्द, क्रिया नहीं।",
    },
    "61": {
        "chain": {"steps": ["गर्भ के पक्वाशय में", "अपनी कायाग्नि से पकता हुआ", "प्रसाद की अधिकता से", "धातु आदि का पोषक बनता"]},
        "sandhi": "त् + ध → द्ध: बाहुल्यात् + धातु → बाहुल्याद्धातु · उ + आ → वा: धातु + आदि → धात्वादि · अ + अ → आ: काय + अग्निना → कायाग्निना · अः + च → श्च: ततः + च → ततश्च।",
        "letters": "मेरी याद-पद्धति: प-का-प्र-धा (पक्वाशय, कायाग्नि, प्रसाद, धातु), छपे क्रम में।",
    },
    "62": {
        "frame": "अपेक्षाकृत स्पष्ट: तथा रोमकूपैः उपस्नेहः (रोमकूपों से भीगना) · अनिश्चित: रस एव च पयोभूतः (पयस् = दूध या जल?)।",
        "sandhi": "ऐः + उ → ऐरु: रोमकूपैः + उपस्नेहः → रोमकूपैरुपस्नेहः · अः + र → ओ र: उपस्नेहः + रसः → उपस्नेहो रसः · अः + भ → ओ भ: पयः + भूतः → पयोभूतः।",
    },
    "63": {
        "diagram": {"groups": [
            {"label": "कारण १", "items": ["साक्षात् अन्न-पान का अननुप्रवेश"]},
            {"label": "कारण २", "items": ["रस का अमलत्व"]},
            {"label": "फल", "items": ["अजात गर्भ में स्थूल मल का असम्भव"]}]},
        "sandhi": "त् + अ → द: साक्षात् + अन्न → साक्षादन्न · त् + च → च्च: अमलत्वात् + च → अमलत्वाच्च · अ + अ → आ: मल + असम्भवः → मलासम्भवः।",
        "frame": "कहा: स्थूल मल नहीं बनता · नहीं कहा: सूक्ष्म मल के बारे में कुछ।",
    },
}

# ===================================================================== IMAGE_SPECS
IMAGE_SPECS = {
    ("55", "diagram"): {
        "file": "sh2-garbha-sthiti-55.svg",
        "alt": ("Table of unit 55: the embryo faces the mother's back, palms joined at the forehead, limbs contracted, in the "
                "garbha-koshtha (probably the uterine cavity); the male rests on the right side, the female on the left, the "
                "neuter in the middle (the verb understood for the last two)."),
        "type": "table",
        "title": "गर्भकोष्ठ में गर्भ (इकाई ५५)",
        "heads": ["क्या", "कैसे / कौन"],
        "rows": [["मुख", "माता की पीठ की ओर"], ["हाथ", "ललाट पर अञ्जलि"], ["अंग", "सिकुड़े हुए"],
                 ["स्थान", "गर्भकोष्ठ (सम्भवतः गर्भाशय-गुहा)"], ["दाहिना पार्श्व", "पुमान्"],
                 ["बायाँ (क्रिया समझी गई)", "स्त्री"], ["मध्य (क्रिया समझी गई)", "नपुंसक"]],
    },
    ("56", "seesaw"): {
        "file": "sh2-svapna-bodha-56.svg",
        "alt": ("Split of unit 56: when the mother sleeps, the embryo sleeps; when the mother is awake, the embryo wakes."),
        "type": "split",
        "title": "माता के साथ गर्भ (इकाई ५६)",
        "cols": [["माता सोती", ["गर्भ भी सोता"]], ["माता जागती", ["गर्भ भी जागता"]]],
    },
    ("58", "chain"): {
        "file": "sh2-garbha-sambandha-58.svg",
        "alt": ("Chain of unit 58: from impregnation, the moistening and warming of the womb are the sustenance; a duct "
                "(probably the umbilical cord) is fastened at the navel; in the duct the apara (conjectural reading); in that "
                "the mother's heart (fastened, understood)."),
        "type": "chain",
        "title": "इकाई ५८: पोषण और जुड़ाव",
        "steps": ["निषेक से: गर्भाशय का उपस्नेह-उपस्वेद वर्तन", "नाभि में बँधी नाडी (सम्भवतः गर्भनाल)",
                  "नाडी में अपरा (पाठ अनुमानित)", "उसमें माता का हृदय (बँधा, समझा गया)"],
    },
    ("59", "chain"): {
        "file": "sh2-ahara-rasa-59.svg",
        "alt": ("Flowchart of unit 59: from the mother's heart, the rasa of food, through the vessels (dhamani), pulsating, "
                "reaches the apara."),
        "type": "mermaid",
        "code": ("flowchart TD\n"
                 "  A[\"माता का हृदय\"] --> B[\"आहार-रस धमनियों से\"]\n"
                 "  B --> C[\"स्पन्दित होता हुआ\"]\n"
                 "  C --> D[\"अपरा तक पहुँचता\"]\n"),
    },
    ("60", "chain"): {
        "file": "sh2-rasa-marga-60.svg",
        "alt": ("Chain across units 59 to 61 (the link is probable, as the data notes): unit 59, from the mother's heart through the vessels to the apara; unit 60, then "
                "in sequence towards the navel (no verb printed); unit 61, cooked in the embryo's pakvashaya."),
        "type": "chain",
        "title": "रस का मार्ग (इकाई ५९-६१, जुड़ाव सम्भावित)",
        "steps": ["इकाई ५९: माता के हृदय से धमनियों द्वारा अपरा तक", "इकाई ६०: फिर क्रम से नाभि की ओर (क्रिया नहीं छपी, जुड़ाव सम्भावित)",
                  "इकाई ६१: गर्भ के पक्वाशय में पकता"],
    },
    ("61", "chain"): {
        "file": "sh2-pakvashaya-61.svg",
        "alt": ("Flowchart of unit 61: in the embryo's pakvashaya, cooked by its own bodily fire, through the abundance of "
                "the clear part (prasada), it becomes nourishing to the dhatus and the rest."),
        "type": "mermaid",
        "code": ("flowchart TD\n"
                 "  A[\"गर्भ के पक्वाशय में\"] --> B[\"अपनी कायाग्नि से पकता\"]\n"
                 "  B --> C[\"प्रसाद की अधिकता\"]\n"
                 "  C --> D[\"धातु आदि की पुष्टि\"]\n"),
    },
    ("63", "diagram"): {
        "file": "sh2-mala-asambhava-63.svg",
        "alt": ("Flowchart of unit 63: two causes, food and drink do not go in directly, and the rasa is free of mala, lead "
                "to the result that gross waste does not arise in the unborn embryo."),
        "type": "mermaid",
        "code": ("flowchart TD\n"
                 "  A[\"अन्न-पान सीधे नहीं जाते\"] --> C[\"स्थूल मल नहीं बनता\"]\n"
                 "  B[\"रस मल-रहित\"] --> C\n"),
    },
}
