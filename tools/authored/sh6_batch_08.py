from helpers import mcq, match, order, fill, multi, accepts


AUTHORED = {}

# ---------------------------------------------------------------- unit 91
AUTHORED["91"] = {
    "title": "ते च प्रायशो दुष्यंत्यग्निदोषात्",
    "question": "By unit 91, through what do they mostly become vitiated?",
    "rule": ("And they (ते) mostly (प्रायशः) become vitiated (दुष्यन्ति) through a fault of agni (अग्निदोषात्, "
             "ablative), agni being the digestive fire."),
    "limits": ("Prose. The unit does not name who 'they' are (card 90 has just spoken of the vitiated doṣas); no "
               "question rests on the referent. 'Mostly' means agni's fault is not called the only cause; no other "
               "cause is named here. The kind of fault of agni is not described."),
    "explain_hi": ("यह गद्य-पंक्ति कहती है: और वे अधिकतर अग्नि के दोष से दूषित होते हैं। "
                   "अग्नि यहाँ पाचन की अग्नि है, ग्रन्थ का पारिभाषिक शब्द। "
                   "‘अग्निदोषात्’ पञ्चमी विभक्ति है: अग्नि के दोष से, उसके कारण। "
                   "‘प्रायशः’ (अधिकतर) बताता है कि यह मुख्य कारण है, एकमात्र नहीं कहा गया; दूसरे कारण यहाँ नहीं गिनाए गए। "
                   "‘वे’ कौन हैं, यह इकाई स्वयं नहीं कहती; पिछली इकाई ९० दूषित दोषों की बात करती है।"),
    "hook": "बिगाड़ की जड़ प्रायः अग्नि का दोष।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 91, through what do they mostly become vitiated?",
            ("A fault of agni", "अग्निदोषात्: through a fault of agni, the digestive fire."),
            [("A fault of the season", "No season is named in unit 91; the cause is agni's fault."),
             ("A fault of the mind", "The mind is not named in unit 91; the cause is agni's fault."),
             ("A fault of the blood", "Blood is not named in unit 91; the cause is agni's fault.")],
            "They mostly become vitiated through a fault of agni.",
            "ते च प्रायशो दुष्यन्त्यग्निदोषात्."),
        match(1, "Match each word of unit 91 to its meaning.",
              [["ते", "they"], ["प्रायशः", "mostly, for the most part"], ["दुष्यन्ति", "become vitiated"],
               ["अग्नि", "the digestive fire"], ["दोषात्", "through a fault"]],
              "And they mostly become vitiated through a fault of agni.",
              "ते, प्रायशः, दुष्यन्ति, अग्नि, दोषात्."),
        mcq("extend", 2, "In unit 91, what does the ablative ending -आत् of अग्निदोषात् express?",
            ("The cause: through agni's fault", "The ablative here gives the source or cause: from, through a fault of agni."),
            [("The place: inside agni's fault", "A place would need the locative (-ए), not the ablative -आत्."),
             ("The owner: belonging to agni", "Ownership would need the genitive (-स्य), not the ablative -आत्."),
             ("The goal: towards agni's fault", "A goal would need the accusative or dative, not the ablative -आत्.")],
            "अग्निदोषात् = from, through a fault of agni: the cause of the vitiation.",
            "Ablative -आत् of an अ-stem: from, because of.",
            teaches="The ablative singular -आत् of अ-stems can state a cause: अग्निदोषात् = through a fault of agni."),
        mcq("discriminate", 3, "Which split of दुष्यंत्यग्निदोषात् in unit 91 is right?",
            ("दुष्यन्ति + अग्निदोषात्", "इ before a different vowel becomes य्: दुष्यन्ति + अग्नि → दुष्यन्त्यग्नि."),
            [("दुष्यन्ते + अग्निदोषात्", "ए + अ would give दुष्यन्तेऽग्नि, with ए kept and ऽ."),
             ("दुष्यन्तः + अग्निदोषात्", "अः + अ would give दुष्यन्तोऽग्नि."),
             ("दुष्यन्त् + यग्निदोषात्", "यग्नि is not a word; the य् comes from the इ of दुष्यन्ति.")],
            "दुष्यन्ति (become vitiated) + अग्निदोषात् (through agni's fault): इ + अ → य.",
            "इ + a different vowel → य् + that vowel."),
        multi("apply", 4, "Which statements fit unit 91?",
              [("Agni here means the digestive fire", "Right: the data reads agni as the digestive fire."),
               ("The unit describes the kind of fault of agni", "No kind of fault is described."),
               ("प्रायशः (mostly) does not make agni the only cause", "Right: 'mostly' leaves room; no other cause is named."),
               ("The verb दुष्यन्ति is singular", "दुष्यन्ति is third person plural: they become vitiated.")],
              [0, 2],
              "Agni = digestive fire; 'mostly' does not make it the only cause.",
              "ते च प्रायशो दुष्यन्त्यग्निदोषात्."),
        mcq("transfer", 5, "By the rule of दुष्यन्त्यग्नि, how is पतन्ति + अधः (they fall down) joined in a new example?",
            ("पतन्त्यधः", "इ before a different vowel becomes य्, as दुष्यन्ति + अग्नि → दुष्यन्त्यग्नि."),
            [("पतन्तीधः", "ई comes from इ + इ; here इ meets अ."),
             ("पतन्तेधः", "ए comes from अ + इ, not from इ + अ."),
             ("पतन्तधः", "The इ does not simply drop; it becomes य्.")],
            "पतन्ति + अधः = पतन्त्यधः, like दुष्यन्ति + अग्नि = दुष्यन्त्यग्नि.",
            "इ + अ → य.",
            teaches="इ before a different vowel becomes य्: दुष्यन्ति + अग्निदोषात् → दुष्यन्त्यग्निदोषात्."),
    ],
}

# ---------------------------------------------------------------- unit 92
AUTHORED["92"] = {
    "title": "तस्मान्निमित्तान्यायुरारोग्यबलोपचयवर्णौजांसि",
    "question": "Which six things does unit 92 list after 'therefore, the causes'?",
    "rule": ("Therefore (तस्मात्), the causes (निमित्तानि): lifespan, health, strength, growth, complexion and ojas, "
             "written as one dvandva compound in the neuter nominative plural."),
    "limits": ("Prose, low confidence: an incomplete statement. There is no verb and no genitive, so it is not said "
               "what the causes are causes of; the data thinks it probably means 'agni is the cause of lifespan ... "
               "and ojas', but supplies nothing. No question rests on that relation. ojas is a doctrinal term (vital "
               "essence, vigour), kept."),
    "explain_hi": ("यह गद्य-पंक्ति अधूरा कथन है: ‘इसलिए निमित्त:’ और फिर छह शब्दों का एक द्वन्द्व समास। "
                   "छह शब्द क्रम से: आयु (जीवन-काल), आरोग्य (स्वास्थ्य), बल, उपचय (वृद्धि), वर्ण (रंगत) और ओजस् (जीवन-सार)। "
                   "क्रिया या षष्ठी छपी नहीं, इसलिए सम्बन्ध साफ़ नहीं; डेटा के अनुसार सम्भवतः अर्थ है कि अग्नि इनका कारण है, पर यह जोड़ा नहीं गया। "
                   "विश्वास निम्न है, इसलिए सम्बन्ध पर कोई प्रश्न नहीं। "
                   "सन्धियाँ सीखने योग्य हैं: अ + उ → ओ (बलोपचय), अ + ओ → औ (वर्णौजांसि)।"),
    "hook": "आयु, आरोग्य, बल, उपचय, वर्ण, ओज: छह की माला।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "Which of these is one of the six things listed in unit 92?",
            ("Complexion (वर्ण)", "वर्ण (complexion) is the fifth member of the compound."),
            [("Sleep (निद्रा)", "निद्रा is not in the compound of unit 92."),
             ("Memory (स्मृति)", "स्मृति is not in the compound of unit 92."),
             ("Hunger (क्षुधा)", "क्षुधा is not in the compound of unit 92.")],
            "The six: lifespan, health, strength, growth, complexion, ojas.",
            "आयुरारोग्यबलोपचयवर्णौजांसि."),
        order(1, "Put the six members of the compound of unit 92 in the printed order.",
              ["आयुः", "आरोग्य", "बल", "उपचय", "वर्ण", "ओजस्"],
              "Lifespan, health, strength, growth, complexion, ojas.",
              "आयुः → आरोग्य → बल → उपचय → वर्ण → ओजस्."),
        match(2, "Match each member of the compound of unit 92 to its meaning.",
              [["आयुः", "lifespan"], ["आरोग्य", "health"], ["बल", "strength"], ["उपचय", "growth"],
               ["वर्ण", "complexion"], ["ओजस्", "ojas, vital essence"]],
              "आयु, आरोग्य, बल, उपचय, वर्ण, ओजस्: lifespan, health, strength, growth, complexion, ojas.",
              "आयुः, आरोग्य, बल, उपचय, वर्ण, ओजस्.", role="extend",
              teaches="The six form one dvandva compound; its last member takes the neuter plural ending: -ओजांसि."),
        mcq("discriminate", 3, "Which split of वर्णौजांसि in unit 92 is right?",
            ("वर्ण + ओजांसि", "अ + ओ → औ: वर्ण + ओजांसि → वर्णौजांसि."),
            [("वर्णः + ओजांसि", "अः before a vowel other than अ loses its visarga with no join: वर्ण ओजांसि."),
             ("वर्णे + ओजांसि", "ए before ओ does not give औ; ए becomes अय् (or अ)."),
             ("वर्णौ + जांसि", "जांसि is not a word; the word is ओजांसि (ojas, plural).")],
            "वर्ण (complexion) + ओजांसि (ojas): अ + ओ → औ.",
            "अ + ओ → औ."),
        multi("apply", 4, "Which statements about unit 92 are certain from the data?",
              [("The unit states that agni causes lifespan", "Not stated: no verb or genitive; it is only a probable reading."),
               ("The six words form one compound in the neuter plural", "Right: one dvandva, neuter nominative plural."),
               ("The unit prints a verb for the sentence", "No verb is printed; the statement is incomplete."),
               ("उपचय means growth", "Right: उपचय = growth.")],
              [1, 3],
              "Sure: the compound and its meanings. Open: what the six are causes of.",
              "तस्मान्निमित्तान्यायुरारोग्यबलोपचयवर्णौजांसि."),
        mcq("transfer", 5, "By the rule of बलोपचय (बल + उपचय), how is सूर्य + उदयः (sunrise) joined in a new example?",
            ("सूर्योदयः", "अ + उ → ओ, as बल + उपचय → बलोपचय."),
            [("सूर्यौदयः", "औ comes from अ + ओ or औ, not from अ + उ."),
             ("सूर्यूदयः", "अ + उ does not give ऊ; the two vowels merge into ओ."),
             ("सूर्यउदयः", "Inside a compound the vowels are joined, not left side by side.")],
            "सूर्य + उदयः = सूर्योदयः, like बल + उपचय = बलोपचय.",
            "अ + उ → ओ.",
            teaches="अ + उ → ओ: बल + उपचय → बलोपचय."),
    ],
}

# ---------------------------------------------------------------- unit 93
AUTHORED["93"] = {
    "title": "तत्प्रतिबद्धान्येवच · तथाऽन्नमपि",
    "question": "By unit 93, what depends on agni, and what does food become digested or undigested?",
    "rule": ("Dependent on that (agni) alone are rañjaka and the rest, the bhūtāgnis and the dhātvagnis. Food too, "
             "digested (पक्व) by that very agni, attains the state of nectar (अमृतता); undigested (अपक्व), of poison (विषता)."),
    "limits": ("Two printed lines, prose. 'That' (तत्, तेन) is agni by the data's understanding; it is not printed. "
               "'And the rest' after rañjaka are not listed. Rañjaka as the colouring kind of Pitta is standard in later "
               "Āyurveda. Printed पक्क = पक्व. Nectar and poison are named as states; no effects are described."),
    "explain_hi": ("पहली पंक्ति: रञ्जक आदि (रंग देने वाला पित्त का एक भेद, और अन्य जो यहाँ गिनाए नहीं), भूताग्नियाँ यानी भूतों की अग्नियाँ, "
                   "और धात्वग्नियाँ यानी धातुओं की अग्नियाँ, सब उसी पर आश्रित हैं; ‘उसी’ से अग्नि समझी जाती है। "
                   "दूसरी पंक्ति: वैसे ही अन्न भी, उसी अग्नि से पचा हुआ, अमृत-भाव को पाता है, और बिना पचा विष-भाव को। "
                   "क्रिया ‘याति’ (पाता है) दोनों हिस्सों में काम करती है। "
                   "छपा ‘पक्क’ पक्व की वर्तनी है।"),
    "hook": "पचा अन्न अमृत, बिना पचा अन्न विष।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 93, what state does food attain when it is digested by agni?",
            ("The state of nectar (amṛta)", "पक्वम् अमृततां याति: digested, it attains the state of nectar."),
            [("The state of poison (viṣa)", "Poison is the state of undigested (अपक्व) food."),
             ("The state of fire (agni)", "Food does not become fire; agni digests it."),
             ("The state of water (ambu)", "Water is not named in unit 93.")],
            "Digested food attains the state of nectar; undigested, of poison.",
            "पक्कममृततां यात्यपक्वं च विषताम्."),
        order(1, "Put the parts of the second line of unit 93 in the printed order.",
              ["तथाऽन्नमपि", "तेनैव पक्कम्", "अमृततां याति", "अपक्वं च", "विषताम्"],
              "Likewise food too, digested by that very agni, attains nectar-state; undigested, poison-state.",
              "तथाऽन्नमपि → तेनैव पक्कम् → अमृततां याति → अपक्वं च → विषताम्."),
        match(2, "Match each term of unit 93 to its meaning.",
              [["रञ्जक", "a kind of Pitta that colours"], ["भूताग्नि", "fire of an element"],
               ["धात्वग्नि", "fire of a dhātu"], ["अमृतता", "state of nectar"], ["विषता", "state of poison"]],
              "Rañjaka, bhūtāgni, dhātvagni depend on agni; digested food → nectar, undigested → poison.",
              "रञ्जक, भूताग्नि, धात्वग्नि; अमृतता, विषता.", role="extend",
              teaches="-ता makes a noun of state: अमृत → अमृतता (nectar-state), विष → विषता (poison-state)."),
        mcq("discriminate", 3, "Which split of धात्वग्नयश्च in unit 93 is right?",
            ("धातु + अग्नयः + च", "उ before a different vowel becomes व्; अग्नयः + च → अग्नयश्च."),
            [("धाता + अग्नयः + च", "आ + अ would give धाताग्नयः, with a long आ."),
             ("धातो + अग्नयः + च", "ओ + अ would give धातोऽग्नयः, with ओ kept."),
             ("धातुः + अग्नयः + च", "A visarga after उ before a vowel becomes र्: धातुरग्नयः.")],
            "धातु (dhātu) + अग्नयः (fires) + च (and): उ + अ → व.",
            "उ + a different vowel → व् + that vowel."),
        mcq("apply", 4, "By unit 93, what happens to food that is not digested (अपक्व)?",
            ("It attains the state of poison", "अपक्वं च विषताम्: undigested, it attains the state of poison."),
            [("It attains the state of nectar", "Nectar is the state of digested food."),
             ("It becomes the rañjaka Pitta", "Rañjaka depends on agni; food does not become it."),
             ("It is turned into a dhātvagni", "The dhātvagnis depend on agni; food does not become one.")],
            "Undigested food attains the state of poison.",
            "अपक्वं च विषताम् (याति)."),
        mcq("transfer", 5, "By the rule of रञ्जकादीनि (रञ्जक + आदीनि), how is देव + आलयः (temple) joined in a new example?",
            ("देवालयः", "अ + आ → आ, as रञ्जक + आदीनि → रञ्जकादीनि."),
            [("देवलयः", "The long आ of आलयः is not lost; अ + आ gives आ."),
             ("देवेलयः", "ए comes from अ + इ, not from अ + आ."),
             ("देवौलयः", "औ comes from अ + ओ or औ, not from अ + आ.")],
            "देव + आलयः = देवालयः, like रञ्जक + आदीनि = रञ्जकादीनि.",
            "अ + आ → आ.",
            teaches="अ + आ → आ: रञ्जक + आदीनि → रञ्जकादीनि."),
    ],
}

# ---------------------------------------------------------------- unit 94
AUTHORED["94"] = {
    "title": "तत्र पित्तविशेषः पाचकसंज्ञोऽग्निरिति प्रागभिहितः",
    "question": "By unit 94, what was stated earlier to be agni?",
    "rule": ("Among these (तत्र), a special kind of Pitta (पित्तविशेषः) named pācaka (पाचकसंज्ञः, 'the digesting one') "
             "is agni: so (इति) it was stated earlier (प्राक् अभिहितः)."),
    "limits": ("Prose. The earlier statement is in an earlier part of the work and is not checked here; no question asks "
               "where it is. The unit does not say how pācaka digests."),
    "explain_hi": ("यह गद्य-पंक्ति एक पहले कही बात दोहराती है: पित्त का एक विशेष भेद, जिसका नाम ‘पाचक’ (पचाने वाला) है, अग्नि है। "
                   "‘इति’ उद्धृत कथन को बन्द करता है, और ‘प्राक् अभिहितः’ बताता है कि यह पहले कहा जा चुका है। "
                   "वह पहला स्थान ग्रन्थ के किसी पहले भाग में है; यहाँ उसकी जाँच नहीं की गई। "
                   "‘पाचक’ √पच् (पकाना, पचाना) से बना है।"),
    "hook": "पाचक पित्त ही अग्नि: यह पहले कहा था।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 94, agni is a special kind of which doṣa?",
            ("Pitta", "पित्तविशेषः ... अग्निः: agni is a special kind of Pitta."),
            [("Kapha", "Kapha is not named in unit 94; agni is a kind of Pitta."),
             ("Vāta", "Vāta is not named in unit 94; agni is a kind of Pitta."),
             ("Ojas", "Ojas is not a doṣa and is not named in unit 94.")],
            "A special kind of Pitta, named pācaka, is agni.",
            "पित्तविशेषः पाचकसंज्ञोऽग्निः."),
        match(1, "Match each word of unit 94 to its meaning.",
              [["तत्र", "among these"], ["पित्तविशेषः", "a special kind of Pitta"], ["पाचकसंज्ञः", "named pācaka"],
               ["प्राक्", "earlier"], ["अभिहितः", "stated"]],
              "Among these, a special kind of Pitta named pācaka is agni: so it was stated earlier.",
              "तत्र, पित्तविशेषः, पाचकसंज्ञः, प्राक्, अभिहितः."),
        fill(2, "By unit 94, the special kind of Pitta that is agni is named ____ (the digesting one). Type it in Devanagari or in English letters (e.g. dharma).",
             accepts("पाचक", None, "पाचकः", "pacaka", "paachaka"),
             "पाचक (the digesting one): पाचकसंज्ञोऽग्निः.",
             "पाचक, from √पच् (to cook, to digest), is the name of the Pitta that is agni.",
             "पाचकसंज्ञः = named pācaka."),
        mcq("discriminate", 3, "Which split of पाचकसंज्ञोऽग्निरिति in unit 94 is right?",
            ("पाचकसंज्ञः + अग्निः + इति", "अः + अ → ओऽ; the visarga of अग्निः after इ before a vowel → र्."),
            [("पाचकसंज्ञा + अग्निः + इति", "आ + अ would give पाचकसंज्ञाग्निः, with no ओ."),
             ("पाचकसंज्ञे + अग्निः + इति", "ए + अ would give पाचकसंज्ञेऽग्निः, with ए kept."),
             ("पाचकसंज्ञो + अग्नि + रिति", "रिति is not a word; the र् comes from the visarga of अग्निः.")],
            "पाचकसंज्ञः + अग्निः + इति → पाचकसंज्ञोऽग्निरिति.",
            "अः + अ → ओऽ; इः + vowel → इर्."),
        mcq("apply", 4, "What does प्रागभिहितः tell the reader in unit 94?",
            ("That this was stated earlier", "प्राक् (earlier) + अभिहितः (stated): it was said before in the work."),
            [("That this will be taught later", "प्राक् means earlier, not later."),
             ("That this is quoted from a Veda", "No Veda is named; प्राक् अभिहितः = stated earlier."),
             ("That this is a new, own view", "It is a repeated statement, not a new one.")],
            "प्रागभिहितः = stated earlier.",
            "प्राक् + अभिहितः: earlier + stated."),
        mcq("transfer", 5, "By the rule of प्रागभिहितः (प्राक् + अभिहितः), how is वाक् + ईशः joined in a new example?",
            ("वागीशः", "A final क् before a vowel (a voiced sound) becomes ग्, as प्राक् + अभिहितः → प्रागभिहितः."),
            [("वाकीशः", "The क् does not stay voiceless before a vowel; it becomes ग्."),
             ("वाङीशः", "ङ् comes before a nasal, not before a vowel."),
             ("वाचीशः", "च् does not come from क् here; क् becomes ग्.")],
            "वाक् + ईशः = वागीशः, like प्राक् + अभिहितः = प्रागभिहितः.",
            "Final क् + vowel → ग्.",
            teaches="A final क् before a vowel (a voiced sound) becomes ग्: प्राक् + अभिहितः → प्रागभिहितः."),
    ],
}

# ---------------------------------------------------------------- unit 95
AUTHORED["95"] = {
    "title": "अन्ये पुनराचक्षते",
    "question": "What does unit 95 say?",
    "rule": ("Others (अन्ये), again (पुनः), say (आचक्षते): the view of other, unnamed authorities is being reported. "
             "पुनः is पुनर् at heart, so its र् shows before a vowel."),
    "limits": ("Prose, three words. The 'others' are not named. Their statement is in card 96; the questions here stay "
               "with these three words. आचक्षते is a present middle form, 'they say', not a passive."),
    "explain_hi": ("यह छोटी गद्य-पंक्ति है: दूसरे फिर कहते हैं। "
                   "‘अन्ये’ (दूसरे) कौन हैं, नाम नहीं दिया गया। "
                   "इकाई ९४ में पाचक पित्त को अग्नि कहा गया; अब किसी और मत की बात आरम्भ होती है, जिसका कथन इकाई ९६ में है। "
                   "‘आचक्षते’ आ + √चक्ष् का वर्तमान काल, प्रथम पुरुष बहुवचन, आत्मनेपद है: वे कहते हैं; यह कर्मवाच्य नहीं। "
                   "‘पुनः’ मूल में ‘पुनर्’ है, इसलिए स्वर से पहले र् दिखता है: पुनः + आचक्षते → पुनराचक्षते।"),
    "hook": "‘अन्ये पुनः’: अब दूसरों का मत।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "What does अन्ये पुनराचक्षते mean?",
            ("Others, again, say", "अन्ये (others), पुनः (again), आचक्षते (they say)."),
            [("Others, again, ask", "आचक्षते means they say, not they ask."),
             ("Others come again", "आचक्षते is from आ-√चक्ष्, to say, not from a verb of coming."),
             ("Others are named again", "आचक्षते is active in sense, 'they say'; it is not a passive.")],
            "Others, again, say.",
            "अन्ये पुनराचक्षते."),
        order(1, "Put the words of unit 95 in the printed order.",
              ["अन्ये", "पुनः", "आचक्षते"],
              "Others, again, say.",
              "अन्ये → पुनः → आचक्षते."),
        fill(2, "Complete unit 95: ____ पुनराचक्षते (others, again, say). Type it in Devanagari or in English letters (e.g. dharma).",
             accepts("अन्ये", None, "anye"),
             "अन्ये = others: अन्ये पुनराचक्षते.",
             "अन्ये (nominative plural of अन्य) = others: the unnamed authorities whose view follows.",
             "अन्ये = others."),
        mcq("discriminate", 3, "Which split of पुनराचक्षते in unit 95 is right?",
            ("पुनः + आचक्षते", "पुनः is पुनर् at heart; before the vowel आ its र् shows: पुनराचक्षते."),
            [("पुन + राचक्षते", "राचक्षते is not a word; the र् belongs to पुनर्."),
             ("पुनः + अचक्षते", "With a short अ the join would be पुनरचक्षते, not पुनराचक्षते."),
             ("पुने + आचक्षते", "ए before आ becomes अय् (or अ), not र्.")],
            "पुनः (again) + आचक्षते (they say) → पुनराचक्षते.",
            "पुनः (पुनर्) + vowel → पुनर्."),
        mcq("apply", 4, "In unit 95, what kind of form is आचक्षते?",
            ("Present, 3rd plural, middle voice", "आ-√चक्ष् is used in the middle: आचक्षते = they say."),
            [("Present, 3rd plural, passive voice", "Not passive: the others do the saying; -अते is a middle ending here."),
             ("Past participle, nominative plural", "A past participle would end in -त; आचक्षते is a finite verb."),
             ("Optative, 3rd singular, active", "The optative would show -एत् or -यात्; this is present plural.")],
            "आचक्षते: present tense, third person plural, middle voice: they say.",
            "-अते (3rd plural) is not always passive."),
        mcq("transfer", 5, "By the pattern of पुनराचक्षते, how is पुनः + अपि (again too) joined in a new example?",
            ("पुनरपि", "पुनः is पुनर् at heart; before a vowel its र् shows, as in पुनराचक्षते."),
            [("पुनोऽपि", "ओऽ would come from a plain अः before अ; पुनः is पुनर्."),
             ("पुन अपि", "The र् of पुनर् does not drop before a vowel."),
             ("पुनश्अपि", "श् comes from a visarga before च, छ or श, not before a vowel.")],
            "पुनः + अपि = पुनरपि, like पुनः + आचक्षते = पुनराचक्षते.",
            "पुनः (पुनर्) + vowel → पुनर्.",
            teaches="पुनः is पुनर् at heart: before a vowel its र् shows (पुनराचक्षते, पुनरपि)."),
    ],
}

# ---------------------------------------------------------------- unit 96
AUTHORED["96"] = {
    "title": "दोषधातुमलसन्निपातजनितोऽन्तरूष्मा",
    "question": "By the view reported in unit 96, what is agni?",
    "rule": ("Agni is the inner heat (अन्तरूष्मा) produced (जनितः) by the coming together (सन्निपात) of doṣa, dhātu "
             "and mala, its seat and function being as indicated (यथानिर्दिष्ट); इति closes the reported view."),
    "limits": ("Prose, medium confidence. This is the view of the 'others' of card 95. 'As indicated' points to earlier "
               "statements not checked here: no question on what the seat and function are. mala = waste product."),
    "explain_hi": ("यह इकाई ९५ में आरम्भ हुए ‘दूसरों’ के मत का कथन है। "
                   "उनके अनुसार अग्नि वह भीतरी ऊष्मा (अन्तर्-ऊष्मा) है जो दोष, धातु और मल (अपशिष्ट) के सन्निपात यानी मिलने से उत्पन्न होती है। "
                   "उसका अधिष्ठान (स्थान) और कर्म वैसे ही हैं जैसे पहले बताए गए; वे पहले स्थान यहाँ जाँचे नहीं गए। "
                   "अन्त का ‘इति’ उद्धृत मत की समाप्ति दिखाता है। "
                   "इकाई ९४ में अग्नि को पाचक नाम का पित्त-विशेष कहा गया था; यह दूसरी परिभाषा है।"),
    "hook": "दोष, धातु, मल मिले, भीतर ऊष्मा जगी: वही अग्नि।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By the view in unit 96, agni is the inner heat produced by what?",
            ("Doṣa, dhātu and mala coming together", "दोषधातुमलसन्निपातजनितः: produced by their coming together."),
            [("Blood, flesh and fat coming together", "Blood, flesh and fat are not named in unit 96."),
             ("The sun's heat entering the body", "The sun is not named; the heat is produced within."),
             ("Food and water mixed in the stomach", "Food and water are not named in unit 96.")],
            "Agni = the inner heat produced by the coming together of doṣa, dhātu and mala.",
            "दोषधातुमलसन्निपातजनितोऽन्तरूष्मा ... अग्निः."),
        order(1, "Put the parts of unit 96 in the printed order.",
              ["दोषधातुमल", "सन्निपातजनितः", "अन्तरूष्मा", "यथानिर्दिष्ट", "अधिष्ठानकर्मा", "अग्निरिति"],
              "Doṣa-dhātu-mala, produced by their coming together, the inner heat, whose seat and function are as indicated, is agni.",
              "दोषधातुमल → सन्निपातजनितः → अन्तरूष्मा → यथानिर्दिष्ट → अधिष्ठानकर्मा → अग्निरिति."),
        match(2, "Match each word part of unit 96 to its meaning.",
              [["सन्निपात", "coming together"], ["जनित", "produced"], ["अन्तर्", "inner"], ["ऊष्मा", "heat"],
               ["अधिष्ठान", "seat"], ["कर्म", "function"]],
              "Produced by the coming together (of doṣa, dhātu, mala), the inner heat, with its seat and function as indicated.",
              "सन्निपात, जनित, अन्तर्, ऊष्मा, अधिष्ठान, कर्म.", role="extend",
              teaches="यथानिर्दिष्टाधिष्ठानकर्मा is a bahuvrīhi: 'whose seat and function are as indicated', describing agni."),
        mcq("discriminate", 3, "Which split of जनितोऽन्तरूष्मा in unit 96 is right?",
            ("जनितः + अन्तरूष्मा", "अः + अ → ओ, and the अ is dropped (ऽ): जनितोऽन्तरूष्मा."),
            [("जनिता + अन्तरूष्मा", "आ + अ would give जनितान्तरूष्मा, with no ओ."),
             ("जनिते + अन्तरूष्मा", "ए + अ would give जनितेऽन्तरूष्मा, with ए kept."),
             ("जनितो + न्तरूष्मा", "न्तरूष्मा is not a word; the word is अन्तरूष्मा (inner heat).")],
            "जनितः (produced) + अन्तरूष्मा (inner heat): अः + अ → ओऽ.",
            "अः + अ → ओऽ."),
        multi("apply", 4, "Which statements fit unit 96?",
              [("It names the seat of agni", "The seat is 'as indicated' earlier; it is not named here."),
               ("It reports the view of the others of card 95", "Right: the closing इति ends that reported view."),
               ("Mala here means a waste product", "Right: mala = waste product (data)."),
               ("It calls agni a kind of Kapha", "Kapha is not named; agni is called the inner heat.")],
              [1, 2],
              "The view of others; agni = inner heat from doṣa, dhātu and mala (waste).",
              "अन्ये पुनराचक्षते: दोषधातुमलसन्निपातजनितोऽन्तरूष्मा ... अग्निरिति."),
        mcq("transfer", 5, "By the rule of जनितोऽन्तरूष्मा, how is बालः + अपि (the boy too) joined in a new example?",
            ("बालोऽपि", "अः + अ → ओ and the अ drops (ऽ), as जनितः + अन्तरूष्मा → जनितोऽन्तरूष्मा."),
            [("बालापि", "आ comes from आ + अ; here it is अः + अ."),
             ("बालरपि", "र् comes from a visarga after other vowels (इ, उ ...), not after अ."),
             ("बाल अपि", "Before अ, अः becomes ओ with ऽ; the visarga is not simply dropped.")],
            "बालः + अपि = बालोऽपि, like जनितः + अन्तरूष्मा = जनितोऽन्तरूष्मा.",
            "अः + अ → ओऽ.",
            teaches="अः before अ becomes ओ and the अ is dropped, marked ऽ: जनितः + अन्तरूष्मा → जनितोऽन्तरूष्मा."),
    ],
}

# ---------------------------------------------------------------- unit 97
AUTHORED["97"] = {
    "title": "स खलु विधिवदभ्यवहृतमन्नजातं",
    "question": "By unit 97, how does the inner fire cook the food that has been eaten?",
    "rule": ("That agni, the inner fire, kindled by samāna, cooks the food eaten by rule: drawn into the koṣṭha by "
             "prāṇa, its mass broken by liquids, softened by sneha, lying in the āmāśaya like water and rice in a pot."),
    "limits": ("Prose, one long sentence, medium confidence. āmāśaya = stomach is probable; koṣṭha = storehouse, belly. "
               "Prāṇa and samāna are doctrinal names of winds, kept. The unit does not say how long the cooking takes "
               "or what it yields."),
    "explain_hi": ("यह लम्बा गद्य-वाक्य बताता है कि भीतरी अग्नि भोजन को कैसे पकाती है। "
                   "विधि से खाया गया अन्न प्राण वायु द्वारा कोष्ठ (भण्डार, पेट) में खींचा जाता है; द्रवों से उसका संघात यानी पिण्ड टूटता है, और स्नेह (तेल या वसा) से वह नरम होता है। "
                   "समान वायु से सुलगाई गई अग्नि आमाशय (सम्भवतः जठर) में पड़े इस अन्न को पकाती है। "
                   "उपमा: जैसे हाँडी (स्थाली) में रखे पानी और चावल पकते हैं। "
                   "‘अग्निरन्तरग्निः’ = अग्नि, यानी भीतरी अग्नि।"),
    "hook": "प्राण खींचे, द्रव तोड़े, स्नेह नरमाए, समान सुलगाए: हाँडी के चावल-सा अन्न पके।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "In the simile of unit 97, the food in the āmāśaya is like what?",
            ("Water and rice in a pot", "स्थालीस्थमिवाम्बुतण्डुलम्: like water and rice in a pot."),
            [("Oil and ghee in a lamp", "No lamp is named; the simile is water and rice in a pot."),
             ("Milk and sugar in a churn", "No churn is named; the simile is water and rice in a pot."),
             ("Wood and fire in a stove", "No stove is named; the simile is water and rice in a pot.")],
            "The agni cooks the food as water and rice are cooked in a pot.",
            "स्थालीस्थमिवाम्बुतण्डुलम्."),
        order(1, "Put the states of the food in the order printed in unit 97.",
              ["विधिवदभ्यवहृतम्", "प्राणेन वायुना कोष्ठमाकृष्टं", "द्रवैर्विभिन्नसंघातं", "स्नेहेन मृदूकृतम्",
               "आमाशयस्थम्"],
              "Eaten by rule → drawn into the koṣṭha by prāṇa → mass broken by liquids → softened by sneha → lying in the āmāśaya.",
              "विधिवदभ्यवहृतम् → कोष्ठमाकृष्टम् → विभिन्नसंघातम् → मृदूकृतम् → आमाशयस्थम्."),
        match(2, "Match each helper in unit 97 to what it does.",
              [["प्राण वायु", "draws the food into the koṣṭha"], ["द्रव (liquids)", "break apart its mass"],
               ["स्नेह (oil, fat)", "softens it"], ["समान वायु", "kindles the agni"]],
              "Prāṇa draws in, liquids break apart, sneha softens, samāna kindles the agni.",
              "प्राणेन, द्रवैः, स्नेहेन, समानेन.", role="extend",
              teaches="Each helper stands in the instrumental (-एन, -ऐः, -उना): प्राणेन वायुना, द्रवैः, स्नेहेन, समानेन."),
        mcq("discriminate", 3, "By unit 97, what does samāna do?",
            ("It kindles the agni", "अभिसन्धुक्षितः समानेन: agni is kindled by samāna."),
            [("It draws the food into the koṣṭha", "That is prāṇa: प्राणेन वायुना कोष्ठमाकृष्टम्."),
             ("It softens the food", "That is sneha: स्नेहेन मृदूकृतम्."),
             ("It breaks the food's mass", "That is the liquids: द्रवैर्विभिन्नसंघातम्.")],
            "Samāna kindles agni; prāṇa draws in; liquids break; sneha softens.",
            "अभिसन्धुक्षितः समानेन."),
        multi("apply", 4, "Which statements fit unit 97?",
              [("Prāṇa draws the food into the koṣṭha", "Right: प्राणेन वायुना कोष्ठमाकृष्टम्."),
               ("The liquids soften the food", "The liquids break its mass; sneha softens it."),
               ("The unit says how long the cooking lasts", "No time is given in unit 97."),
               ("The agni cooks food lying in the āmāśaya", "Right: आमाशयस्थम् ... पचति.")],
              [0, 3],
              "Prāṇa draws in; liquids break; sneha softens; agni cooks the food in the āmāśaya.",
              "प्राणेन ... कोष्ठमाकृष्टम् ... आमाशयस्थम् ... पचति."),
        mcq("transfer", 5, "By the rule of विधिवदभ्यवहृतम् (विधिवत् + अभ्यवहृतम्), how is जगत् + ईशः joined in a new example?",
            ("जगदीशः", "A final त् before a vowel becomes द्, as विधिवत् + अभ्यवहृतम् → विधिवदभ्यवहृतम्."),
            [("जगतीशः", "The त् does not stay voiceless before a vowel; it becomes द्."),
             ("जगन्नीशः", "न् comes from त् before a nasal, not before a vowel."),
             ("जगच्छीशः", "च्छ comes from त् + श, not from त् + ई.")],
            "जगत् + ईशः = जगदीशः, like विधिवत् + अभ्यवहृतम् = विधिवदभ्यवहृतम्.",
            "Final त् + vowel → द्.",
            teaches="A final त् before a vowel becomes द्: विधिवत् + अभ्यवहृतम् → विधिवदभ्यवहृतम्."),
    ],
}

# ---------------------------------------------------------------- unit 98
AUTHORED["98"] = {
    "title": "पच्यमानमादौ मधुरीभूतं कफं",
    "question": "By unit 98, what happens first as the food is being cooked?",
    "rule": ("The food, though it has all tastes (सर्वरसम् अपि), while being cooked (पच्यमानम्), first (आदौ) becomes "
             "sweet (मधुरीभूतम्) and stirs up (उदीरयति) Kapha, become foamy (फेनीभूतम्)."),
    "limits": ("Prose, medium confidence. The first printed word तस्तु is read as तत् तु (a possible reading): no question "
               "on it. The print shows मू where the split has उदीरयति: no question on that join. The unit does not say "
               "how long this stage lasts."),
    "explain_hi": ("यह इकाई ९७ में आरम्भ हुई पकने की क्रिया का पहला चरण है। "
                   "अन्न, चाहे उसमें सब रस (स्वाद) हों, पकते समय पहले मधुर हो जाता है और फेनिल (झागदार) बने कफ को उभारता है। "
                   "‘उदीरयति’ = उभारता है, गति देता है। "
                   "छपा ‘तस्तु’ अर्थ नहीं देता; डेटा इसे ‘तत् तु’ (वह अन्न तो) पढ़ता है, जो सम्भावित पाठ है। "
                   "‘मधुरीभूत’ और ‘फेनीभूत’ में -ई-भूत का अर्थ है: जो पहले वैसा न था, वैसा हो गया।"),
    "hook": "पहला चरण: अन्न मीठा, कफ झागदार।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 98, which doṣa does the food stir up first, as it is being cooked?",
            ("Kapha", "मधुरीभूतं कफं फेनीभूतम् उदीरयति: it stirs up Kapha."),
            [("Pitta", "Pitta is stirred later, when the food has turned sour (unit 99)."),
             ("Vāta", "Vāta is stirred later, in the pakvāśaya (unit 100)."),
             ("Ojas", "Ojas is not a doṣa and is not named in unit 98.")],
            "First the food becomes sweet and stirs up Kapha, become foamy.",
            "आदौ मधुरीभूतं कफं ... उदीरयति."),
        order(1, "Put the parts of unit 98 in the printed order (after the first word).",
              ["सर्वरसमपि", "पच्यमानमादौ", "मधुरीभूतं", "कफं", "फेनीभूतमूदीरयति"],
              "Though of all tastes, being cooked, at first, become sweet, Kapha, become foamy, it stirs up.",
              "सर्वरसमपि → पच्यमानमादौ → मधुरीभूतं → कफं → फेनीभूतमूदीरयति."),
        match(2, "Match each word of unit 98 to its meaning.",
              [["सर्वरसम्", "having all tastes"], ["पच्यमानम्", "being cooked"], ["आदौ", "at first"],
               ["मधुरीभूतम्", "become sweet"], ["फेनीभूतम्", "become foamy"], ["उदीरयति", "stirs up"]],
              "Though of all tastes, being cooked, at first become sweet, it stirs up Kapha, become foamy.",
              "सर्वरसम्, पच्यमानम्, आदौ, मधुरीभूतम्, फेनीभूतम्, उदीरयति.", role="extend",
              teaches="-ई-भूत means 'become X' (what it was not before): मधुर → मधुरीभूत, फेन → फेनीभूत."),
        mcq("discriminate", 3, "By unit 98, what taste does the food take on first while being cooked?",
            ("Sweet (मधुर)", "आदौ मधुरीभूतम्: at first it becomes sweet."),
            [("Sour (अम्ल)", "Sour comes later, with Pitta (unit 99)."),
             ("Pungent (कटु)", "Pungent comes later, in the pakvāśaya (unit 100)."),
             ("Salty (लवण)", "Salty is not named in unit 98.")],
            "At first the food becomes sweet.",
            "आदौ मधुरीभूतम्."),
        mcq("apply", 4, "In unit 98, what does सर्वरसम् अपि add?",
            ("Even food of all tastes turns sweet first", "सर्वरसम् अपि: though it has all tastes, it first becomes sweet."),
            [("Only food that is sweet stirs up Kapha", "The point is the reverse: even food of all tastes becomes sweet."),
             ("The food loses all its tastes in cooking", "Losing tastes is not said; it becomes sweet at first."),
             ("Each taste stirs up Kapha in its own turn", "No such turn-taking is stated; the food as a whole turns sweet.")],
            "Whatever its tastes, the food first turns sweet in cooking.",
            "सर्वरसमपि पच्यमानमादौ मधुरीभूतम्."),
        mcq("transfer", 5, "By the pattern of मधुरीभूतम् (become sweet, from मधुर), what does शीतीभूतम् mean in a new example?",
            ("Become cold", "-ई-भूत = has become X (what it was not): शीत → शीतीभूत, as मधुर → मधुरीभूत."),
            [("Very cold", "-ई-भूत does not mean 'very'; it means 'become'."),
             ("Cold by nature", "-ई-भूत marks a change into the state, not a natural one."),
             ("Not yet cold", "-ई-भूत says the change has happened, not that it is pending.")],
            "शीतीभूतम् = become cold, like मधुरीभूतम् = become sweet.",
            "X-ई-भूत = become X.",
            teaches="An अ-stem with -ई-भूत means 'become X': मधुर → मधुरीभूत (become sweet)."),
    ],
}

# ---------------------------------------------------------------- unit 99
AUTHORED["99"] = {
    "title": "ततो विदग्धमम्लीभूतमामाशयाच्च्यवमानमच्छंपित्तं",
    "question": "By unit 99, in what state is the food, and which doṣa does it stir up next?",
    "rule": ("Then (ततः) the food, burnt (विदग्धम्), turned sour (अम्लीभूतम्), falling away from the āmāśaya "
             "(आमाशयात् च्यवमानम्), stirs up clear (अच्छम्) Pitta; the verb उदीरयति is carried from card 98."),
    "limits": ("Prose, elliptical: no verb is printed; 'stirs up' and the subject (the food) are understood from card 98. "
               "vidagdha is rendered literally as burnt, overcooked. āmāśaya = stomach is probable."),
    "explain_hi": ("यह पकने का दूसरा चरण है: तब अन्न विदग्ध (जला हुआ, अधिक पका) और खट्टा होकर, आमाशय से खिसकते हुए, अच्छ (स्वच्छ) पित्त को उभारता है। "
                   "इस पंक्ति में क्रिया छपी नहीं; ‘उदीरयति’ (उभारता है) और कर्ता अन्न इकाई ९८ से समझे जाते हैं। "
                   "‘विदग्ध’ का शाब्दिक अर्थ जला हुआ है; डेटा इसे शाब्दिक ही रखता है। "
                   "आमाशय सम्भवतः जठर है। "
                   "सन्धि: आमाशयात् + च्यवमानम् → आमाशयाच्च्यवमानम् (च से पहले त् → च्)।"),
    "hook": "दूसरा चरण: खट्टा अन्न, आमाशय से खिसकता, स्वच्छ पित्त जगा।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 99, from where is the food falling away as it turns sour?",
            ("From the āmāśaya", "आमाशयाच्च्यवमानम्: falling away from the āmāśaya."),
            [("From the pakvāśaya", "The pakvāśaya is reached later (unit 100); the food falls from the āmāśaya."),
             ("From the mouth", "The mouth is not named in unit 99."),
             ("From the heart", "The heart is not named in unit 99.")],
            "Turned sour, the food falls away from the āmāśaya.",
            "आमाशयात् च्यवमानम्."),
        order(1, "Put the parts of unit 99 in the printed order.",
              ["ततो", "विदग्धम्", "अम्लीभूतम्", "आमाशयाच्च्यवमानम्", "अच्छंपित्तं"],
              "Then, burnt, turned sour, falling away from the āmāśaya, clear Pitta.",
              "ततो → विदग्धम् → अम्लीभूतम् → आमाशयाच्च्यवमानम् → अच्छंपित्तं."),
        match(2, "Match each word of unit 99 to its meaning.",
              [["विदग्धम्", "burnt, overcooked"], ["अम्लीभूतम्", "turned sour"], ["च्यवमानम्", "falling away"],
               ["अच्छम्", "clear"], ["पित्तम्", "Pitta"]],
              "Burnt, turned sour, falling away (from the āmāśaya), (it stirs up) clear Pitta.",
              "विदग्धम्, अम्लीभूतम्, च्यवमानम्, अच्छम्, पित्तम्.", role="extend",
              teaches="The food's states are neuter nominatives (विदग्धम्, अम्लीभूतम्, च्यवमानम्); अच्छं पित्तम् is the object of the understood verb."),
        mcq("discriminate", 3, "By unit 99, which doṣa does the sour food stir up?",
            ("Pitta", "अच्छं पित्तम् (उदीरयति): it stirs up clear Pitta."),
            [("Kapha", "Kapha is stirred at the sweet stage (unit 98)."),
             ("Vāta", "Vāta is stirred at the pungent stage (unit 100)."),
             ("Rasa", "Rasa is not a doṣa; it is the essence made later (unit 103).")],
            "Sour food stirs up clear Pitta.",
            "अम्लीभूतम् ... अच्छं पित्तम्."),
        mcq("apply", 4, "Which split of आमाशयाच्च्यवमानम् in unit 99 is right?",
            ("आमाशयात् + च्यवमानम्", "त् before च becomes च्: आमाशयात् + च्यवमानम् → आमाशयाच्च्यवमानम्."),
            [("आमाशयाः + च्यवमानम्", "A visarga before च becomes श्: आमाशयाश्च्यवमानम्."),
             ("आमाशये + च्यवमानम्", "ए stays before a consonant: आमाशये च्यवमानम्."),
             ("आमाशयम् + च्यवमानम्", "म् before च would give ं: आमाशयं च्यवमानम्.")],
            "आमाशयात् (from the āmāśaya) + च्यवमानम् (falling away): त् + च → च्च.",
            "त् + च → च्च."),
        mcq("transfer", 5, "By the rule of आमाशयाच्च्यवमानम्, how is तत् + च (and that) joined in a new example?",
            ("तच्च", "त् before च becomes च्, as आमाशयात् + च्यवमानम् → आमाशयाच्च्यवमानम्."),
            [("तद्च", "द् does not come before च; त् becomes च्."),
             ("तज्च", "ज् comes before a voiced palatal (ज, झ), not before च."),
             ("तश्च", "श् comes from a visarga before च, not from त्.")],
            "तत् + च = तच्च, like आमाशयात् + च्यवमानम् = आमाशयाच्च्यवमानम्.",
            "त् + च → च्च.",
            teaches="A final त् before च becomes च्: आमाशयात् + च्यवमानम् → आमाशयाच्च्यवमानम्."),
    ],
}

# ---------------------------------------------------------------- unit 100
AUTHORED["100"] = {
    "title": "प्राप्य च पक्वाशयं कटुकीभूतमनिलं",
    "question": "By unit 100, where has the food arrived, and which doṣa does it stir up?",
    "rule": ("Having reached (प्राप्य) the pakvāśaya (probably the large-bowel region), the food, turned pungent "
             "(कटुकीभूतम्), stirs up anila, the wind, that is Vāta; the verb is carried from card 98."),
    "limits": ("Prose, elliptical: verb and subject come from card 98. pakvāśaya = large-bowel region is probable. anila "
               "(wind) means the doṣa Vāta here by context."),
    "explain_hi": ("यह पकने का तीसरा चरण है: पक्वाशय (पचे अन्न का स्थान, सम्भवतः बड़ी आँत का क्षेत्र) में पहुँचकर अन्न कटु (तीखा) हो जाता है और अनिल यानी वात को उभारता है। "
                   "क्रिया ‘उदीरयति’ और कर्ता अन्न इकाई ९८ से समझे जाते हैं। "
                   "‘प्राप्य’ = पहुँचकर; प्र + √आप् का -य वाला रूप, क्योंकि धातु से पहले उपसर्ग है। "
                   "इकाई ९८-१०० मिलकर क्रम देती हैं: मधुर → कफ, अम्ल → पित्त, कटु → वात।"),
    "hook": "तीसरा चरण: पक्वाशय में तीखा, वात जगा।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 100, which doṣa does the food stir up when it has turned pungent?",
            ("Vāta", "कटुकीभूतमनिलम्: it stirs up anila, that is Vāta."),
            [("Kapha", "Kapha is stirred at the sweet stage (unit 98)."),
             ("Pitta", "Pitta is stirred at the sour stage (unit 99)."),
             ("Ojas", "Ojas is not a doṣa and is not named in unit 100.")],
            "Turned pungent in the pakvāśaya, the food stirs up anila (Vāta).",
            "कटुकीभूतम् अनिलम् (उदीरयति)."),
        order(1, "Put the words of unit 100 in the printed order.",
              ["प्राप्य", "च", "पक्वाशयं", "कटुकीभूतमनिलं"],
              "Having reached, and, the pakvāśaya, turned pungent, the wind.",
              "प्राप्य → च → पक्वाशयं → कटुकीभूतमनिलं."),
        match(2, "Match each word of unit 100 to its meaning.",
              [["प्राप्य", "having reached"], ["पक्वाशयम्", "the seat of the digested (pakvāśaya)"],
               ["कटुकीभूतम्", "turned pungent"], ["अनिलम्", "the wind (Vāta)"]],
              "Having reached the pakvāśaya, turned pungent, (it stirs up) the wind.",
              "प्राप्य, पक्वाशयम्, कटुकीभूतम्, अनिलम्.", role="extend",
              teaches="प्राप्य is an absolutive in -य (prefix प्र + √आप्): having reached."),
        mcq("discriminate", 3, "By unit 100, where has the food arrived when it turns pungent?",
            ("The pakvāśaya", "प्राप्य च पक्वाशयम्: having reached the pakvāśaya."),
            [("The āmāśaya", "The food falls away from the āmāśaya (unit 99); it does not arrive there now."),
             ("The heart", "The heart is not named in unit 100."),
             ("The mouth", "The mouth is not named in unit 100.")],
            "Having reached the pakvāśaya, the food turns pungent.",
            "प्राप्य च पक्वाशयम्."),
        mcq("apply", 4, "Why does प्राप्य in unit 100 end in -य and not -त्वा?",
            ("A prefix (प्र) stands before the root", "With a prefix the absolutive takes -य: प्र + √आप् → प्राप्य."),
            [("The root आप् always takes -य", "Without a prefix आप् takes -त्वा: आप्त्वा."),
             ("-य marks the passive voice here", "-य here is the absolutive ending, not a passive marker."),
             ("The sentence has a plural subject", "The subject (the food) is singular; number does not decide -य.")],
            "Prefix + root → absolutive in -य: प्राप्य = having reached.",
            "Absolutive: -त्वा without a prefix, -य with one."),
        mcq("transfer", 5, "By the pattern of प्राप्य, what is the absolutive of प्र + √विश् (to enter) in a new example?",
            ("प्रविश्य", "With a prefix the absolutive takes -य, as प्र + √आप् → प्राप्य."),
            [("प्रविश्त्वा", "-त्वा is used without a prefix; with प्र the ending is -य."),
             ("प्रविष्टः", "प्रविष्टः is a past participle, 'entered', not 'having entered'."),
             ("प्रविशति", "प्रविशति is the present tense, 'enters'.")],
            "प्र + √विश् → प्रविश्य (having entered), like प्र + √आप् → प्राप्य.",
            "Prefix + root → -य.",
            teaches="A verb with a prefix forms its absolutive with -य: प्राप्य, प्रविश्य."),
    ],
}

# ---------------------------------------------------------------- unit 101
AUTHORED["101"] = {
    "title": "ततश्चैवं विक्लिन्नआहारे",
    "question": "What can be read with certainty in the damaged unit 101?",
    "rule": ("Then, thus, with the food moistened, five (unclear words), scattered by wind (वायुना), each according to "
             "its own (यथास्वम्), cook (पचन्ति) only the five element-qualities lying in the food (भूतगुणान् आहारस्थान्)."),
    "limits": ("Prose, low confidence, damaged print. पंचातमक महाभूतन मयो is unclear; the restoration पञ्चात्मकाः "
               "महाभूताग्नयः is only a guess and is not adopted. So who cooks and what is scattered are uncertain: no "
               "question on them. विक्लिन्नआहारे is read as विक्लिन्ने आहारे (possible)."),
    "explain_hi": ("यह पंक्ति छपाई में क्षतिग्रस्त है और विश्वास निम्न है। "
                   "पढ़ा जा सकने वाला भाग: ‘और तब इस प्रकार आहार के भीगकर नरम हो जाने पर ... वायु से अलग-अलग किए हुए, अपने-अपने अनुसार, आहार में स्थित पाँच ही भूत-गुणों को पकाते हैं।’ "
                   "बीच के शब्द ‘पंचातमक महाभूतन मयो’ अस्पष्ट हैं; ‘पञ्चात्मकाः महाभूताग्नयः’ (पाँच महाभूतों की अग्नियाँ) केवल अनुमान है, अनुवाद में नहीं लिया गया। "
                   "इसलिए कौन पकाते हैं, यह निश्चित नहीं, और इस पर कोई प्रश्न नहीं। "
                   "छपा ‘विक्लिन्नआहारे’ ‘विक्लिन्ने आहारे’ पढ़ा गया है, जो सम्भावित पाठ है।"),
    "hook": "धुँधली पंक्ति, साफ़ अन्त: आहार के पाँच भूत-गुण पकते हैं।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "In unit 101, what does यथास्वम् mean?",
            ("Each according to its own", "यथास्वम् (ind.) = each according to its own."),
            [("Against each one's own nature", "यथा- means 'according to', not 'against'."),
             ("All of them at one and the same time", "यथास्वम् is about each one's own, not about time."),
             ("Only inside the stomach", "No place is meant by यथास्वम्.")],
            "यथास्वम् = each according to its own.",
            "यथा + स्वम्: according to (its) own."),
        order(1, "Put the clearly printed parts of unit 101 in the printed order (the unclear words are left out).",
              ["ततश्चैवं", "विक्लिन्नआहारे", "वायुना", "व्यस्तान्यथास्वं", "पंचैवभूतगुणानाहारस्थान्", "पचंति"],
              "Then thus, the food moistened, ... by wind, scattered, each according to its own, only the five element-qualities lying in the food, cook.",
              "ततश्चैवं → विक्लिन्नआहारे → वायुना → व्यस्तान्यथास्वं → पंचैवभूतगुणानाहारस्थान् → पचंति."),
        match(2, "Match each clearly printed word of unit 101 to its meaning.",
              [["वायुना", "by wind"], ["यथास्वम्", "each according to its own"], ["भूतगुण", "element-quality"],
               ["आहारस्थ", "lying in the food"], ["पचन्ति", "(they) cook"]],
              "By wind ... each according to its own ... the element-qualities lying in the food ... cook.",
              "वायुना, यथास्वम्, भूतगुण, आहारस्थ, पचन्ति.", role="extend",
              teaches="आहारस्थ = आहार + स्थ ('standing in'): the element-qualities that lie in the food."),
        mcq("discriminate", 3, "Which split of ततश्चैवं in unit 101 is right?",
            ("ततः + च + एवम्", "Visarga before च → श्; अ + ए → ऐ: ततश्चैवम्."),
            [("तत् + च + एवम्", "त् + च would give तच्चैवम्, with च्च."),
             ("ततः + च + इवम्", "अ + इ would give ए: ततश्चेवम्."),
             ("ततश्च + ऐवम्", "ऐवम् is not a word; the ऐ comes from च + एवम्.")],
            "ततः (then) + च (and) + एवम् (thus) → ततश्चैवम्.",
            "Visarga + च → श्च; अ + ए → ऐ."),
        multi("apply", 4, "Which statements about unit 101 does the data support?",
              [("The unit surely names the bhūtāgnis as the cooks", "Not sure: that rests on a guessed restoration, not adopted."),
               ("विक्लिन्नआहारे is printed with its vowels joined", "The print leaves the vowels unjoined (ए + आ)."),
               ("पंचातमक महाभूतन मयो is unclear in print", "Right: damaged print, kept unsplit as unclear."),
               ("पचन्ति is a plural verb: they cook", "Right: पचन्ति, third person plural.")],
              [2, 3],
              "The middle words are unclear; पचन्ति is plural; who cooks is not certain.",
              "पंचातमक महाभूतन मयो: unclear; पचंति: they cook."),
        mcq("transfer", 5, "By the rule of पंचैव (पञ्च + एव), how is अत्र + एव (just here) joined in a new example?",
            ("अत्रैव", "अ + ए → ऐ, as पञ्च + एव → पञ्चैव."),
            [("अत्रेव", "ए comes from अ + इ, not from अ + ए."),
             ("अत्रौव", "औ comes from अ + ओ or औ, not from अ + ए."),
             ("अत्रयेव", "य् is not inserted; अ + ए merge into ऐ.")],
            "अत्र + एव = अत्रैव, like पञ्च + एव = पञ्चैव.",
            "अ + ए → ऐ.",
            teaches="अ + ए → ऐ: पञ्च + एव → पञ्चैव, च + एवम् → चैवम्."),
    ],
}

# ---------------------------------------------------------------- unit 102
AUTHORED["102"] = {
    "title": "ते पक्काः पुनर्यथास्वमेव",
    "question": "By unit 102, what do the cooked element-qualities then nourish?",
    "rule": ("Those (ते, the five element-qualities, understood from card 101), cooked (पक्वाः, printed पक्काः), again, "
             "each according to its own, nourish (आप्याययन्ति) the element-qualities that rest in the body (देहाश्रितान्)."),
    "limits": ("Prose, medium confidence. स्वाविकारभूतान् can be read 'of their own unaltered nature' (the data's reading) "
               "or 'being their own modifications': no question on it. ते is understood from card 101, whose subject is "
               "itself uncertain there."),
    "explain_hi": ("पिछली इकाई में आहार में स्थित पाँच भूत-गुण पकाए गए; डेटा के अनुसार ‘ते’ (वे) उन्हीं भूत-गुणों की ओर संकेत करता है। "
                   "यहाँ वे पके हुए (पक्वाः, छपा ‘पक्काः’) फिर अपने-अपने अनुसार ही शरीर में स्थित भूत-गुणों को पुष्ट करते हैं (आप्याययन्ति)। "
                   "‘देहाश्रितान्’ = देह पर आश्रित, शरीर में रहने वाले। "
                   "‘स्वाविकारभूतान्’ के दो पाठ सम्भव हैं: अपने अविकृत स्वरूप वाले (डेटा का पाठ) या अपने ही विकार रूप; इस पर कोई प्रश्न नहीं। "
                   "सन्धि: देहाश्रितान् + च → देहाश्रितांश्च।"),
    "hook": "पके भूत-गुण शरीर के भूत-गुणों को पोसते हैं।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 102, what do the cooked ones nourish?",
            ("The element-qualities resting in the body", "देहाश्रितान् ... भूतगुणान् आप्याययन्ति."),
            [("The doṣas that were stirred up in cooking", "The doṣas are not named in unit 102."),
             ("The digestive fire in the āmāśaya", "Agni is not named in unit 102."),
             ("The bones and the marrow of the body", "Bones and marrow are not named in unit 102.")],
            "Cooked, they nourish the element-qualities that rest in the body.",
            "देहाश्रितांश्च ... भूतगुणानाप्याययन्ति."),
        order(1, "Put the parts of unit 102 in the printed order.",
              ["ते पक्काः", "पुनर्यथास्वमेव", "देहाश्रितांश्च", "स्वाविकारभूतान्", "भूतगुणानाप्याययंति"],
              "Those, cooked, again each according to its own, resting in the body, of their own nature, the element-qualities, nourish.",
              "ते पक्काः → पुनर्यथास्वमेव → देहाश्रितांश्च → स्वाविकारभूतान् → भूतगुणानाप्याययंति."),
        match(2, "Match each word of unit 102 to its meaning.",
              [["पक्वाः", "cooked, digested"], ["पुनः", "again"], ["देहाश्रित", "resting in the body"],
               ["आप्याययन्ति", "nourish, make grow"]],
              "Cooked, again, they nourish the element-qualities resting in the body.",
              "पक्वाः, पुनः, देहाश्रित, आप्याययन्ति.", role="extend",
              teaches="आप्याययन्ति: causative of आ-√प्याय्, 'make grow, nourish', third person plural."),
        mcq("discriminate", 3, "Which split of देहाश्रितांश्च in unit 102 is right?",
            ("देहाश्रितान् + च", "A final न् before च becomes ंश्: देहाश्रितान् + च → देहाश्रितांश्च."),
            [("देहाश्रिताः + च", "A visarga before च gives श्च with no ं: देहाश्रिताश्च."),
             ("देहाश्रितम् + च", "म् before च gives ं with no श्: देहाश्रितं च."),
             ("देहाश्रिते + च", "ए stays before a consonant: देहाश्रिते च.")],
            "देहाश्रितान् (resting in the body) + च (and): न् + च → ंश्च.",
            "Final न् + च → ंश्च."),
        multi("apply", 4, "Which statements about unit 102 fit the data?",
              [("ते is taken as the element-qualities of card 101", "Right: the data's note reads te so."),
               ("आप्याययन्ति means they nourish", "Right: causative of आ-√प्याय्, make grow."),
               ("स्वाविकारभूतान् surely means 'their own modifications'", "Not sure: the data reads 'unaltered' and calls the other reading possible."),
               ("The nourished qualities lie in the food", "They rest in the body (देहाश्रितान्).")],
              [0, 1],
              "ते = the element-qualities; they nourish those resting in the body; स्वाविकारभूतान् stays two-way.",
              "ते पक्वाः ... देहाश्रितान् ... भूतगुणान् आप्याययन्ति."),
        mcq("transfer", 5, "By the rule of देहाश्रितांश्च, how is तान् + च (and them) joined in a new example?",
            ("तांश्च", "A final न् before च becomes ंश्, as देहाश्रितान् + च → देहाश्रितांश्च."),
            [("तान्च", "The न् does not stay unchanged before च."),
             ("ताश्च", "The nasal sound does not vanish; it stays as ं."),
             ("तांच", "An श् stands between the ं and च.")],
            "तान् + च = तांश्च, like देहाश्रितान् + च = देहाश्रितांश्च.",
            "Final न् + च → ंश्च.",
            teaches="A final न् before च becomes ंश्: देहाश्रितान् + च → देहाश्रितांश्च."),
    ],
}

# ---------------------------------------------------------------- unit 103
AUTHORED["103"] = {
    "title": "सारभूतो रसाख्यः किट्टाख्यश्चमलोऽभिनिर्वर्तते",
    "question": "By unit 103, what two things are produced from the digested food?",
    "rule": ("Thus from the digested food, as if from an oil with various medicines in its core, a clear essence named "
             "rasa (रसाख्यः सारभूतः) and a waste named kiṭṭa (किट्टाख्यः मलः) are produced (अभिनिर्वर्तते)."),
    "limits": ("Prose, medium confidence. The point of the oil simile is not stated: no question on it. The verb is "
               "singular though there are two subjects. Printed पक्क = पक्व. What rasa and kiṭṭa do next is not said here."),
    "explain_hi": ("यह पकने का परिणाम है: पके हुए आहार से दो चीज़ें बनती हैं, ‘रस’ नाम का स्वच्छ सार और ‘किट्ट’ नाम का मल (अपशिष्ट)। "
                   "उपमा: जैसे अनेक औषधें भीतर रखने वाले स्नेह (तेल) से; उपमा का ठीक बिन्दु पाठ नहीं बताता, इसलिए इस पर कोई प्रश्न नहीं। "
                   "क्रिया ‘अभिनिर्वर्तते’ (उत्पन्न होता है) एकवचन है, यद्यपि कर्ता दो हैं। "
                   "किट्ट = अन्न का बचा हुआ कचरा। "
                   "छपा ‘पक्क’ पक्व की वर्तनी है।"),
    "hook": "पका आहार: सार बना रस, बचा किट्ट।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 103, what is the clear essence from digested food called?",
            ("Rasa", "अच्छः सारभूतो रसाख्यः: a clear essence named rasa."),
            [("Kiṭṭa", "Kiṭṭa is the waste (mala), not the essence."),
             ("Ojas", "Ojas is not named in unit 103."),
             ("Sneha", "Sneha (oil) belongs to the simile, not to the products.")],
            "The clear essence is rasa; the waste is kiṭṭa.",
            "अच्छः सारभूतो रसाख्यः."),
        match(1, "Match each word of unit 103 to its meaning.",
              [["रस", "the clear essence"], ["किट्ट", "the waste, refuse"], ["पक्वात् आहारात्", "from the digested food"],
               ["स्नेहात्", "from an oil"], ["अभिनिर्वर्तते", "is produced"]],
              "From the digested food, as from an oil ..., rasa (essence) and kiṭṭa (waste) are produced.",
              "रस, किट्ट, पक्वात् आहारात्, स्नेहात्, अभिनिर्वर्तते."),
        order(2, "Put the parts of unit 103 in the printed order.",
              ["एवं च", "पक्कादाहाराद्", "विविधौषधगर्भादिव स्नेहाद्", "अच्छः सारभूतो रसाख्यः", "किट्टाख्यश्चमलो",
               "ऽभिनिर्वर्तते"],
              "Thus, from the digested food, as if from an oil with medicines inside, a clear essence named rasa, and a waste named kiṭṭa, is produced.",
              "एवं च → पक्कादाहाराद् → ...स्नेहाद् → ...रसाख्यः → किट्टाख्यश्चमलो → ऽभिनिर्वर्तते.", role="extend",
              teaches="The sentence runs: source (ablatives with a simile) → two products (rasa, kiṭṭa) → one singular verb."),
        mcq("discriminate", 3, "By unit 103, which product of the digested food is called mala?",
            ("Kiṭṭa, the refuse", "किट्टाख्यश्च मलः: the waste named kiṭṭa."),
            [("Rasa, the clear essence", "Rasa is the essence (सार), the opposite of the waste."),
             ("Sneha, the oil of the simile", "Sneha belongs to the simile; it is not a product."),
             ("Ojas, the vital essence", "Ojas is not named in unit 103.")],
            "Mala = kiṭṭa; sāra = rasa.",
            "किट्टाख्यश्चमलः."),
        mcq("apply", 4, "Why is सारभूतः printed सारभूतो before रसाख्यः in unit 103?",
            ("अः before a voiced consonant becomes ओ", "र is voiced: सारभूतः + रसाख्यः → सारभूतो रसाख्यः."),
            [("अः before every consonant becomes ओ", "Not before voiceless ones: before क, त, प ... it is not ओ."),
             ("ओ marks the vocative case in this unit", "सारभूतः is nominative; the ओ comes from sandhi."),
             ("ओ is a dual ending of the word here", "The word is singular; the ओ comes from sandhi.")],
            "अः + voiced consonant → ओ: सारभूतो रसाख्यः.",
            "अः + voiced consonant → ओ."),
        mcq("transfer", 5, "By the rule of विविधौषध (विविध + औषध), how is वन + औषधिः (forest herb) joined in a new example?",
            ("वनौषधिः", "अ + औ → औ, as विविध + औषध → विविधौषध."),
            [("वनोषधिः", "ओ comes from अ + उ, not from अ + औ."),
             ("वनावषधिः", "आव् comes from औ before a vowel; here औ follows अ."),
             ("वनऔषधिः", "Inside a compound the vowels are joined, not left side by side.")],
            "वन + औषधिः = वनौषधिः, like विविध + औषध = विविधौषध.",
            "अ + औ → औ.",
            teaches="अ + औ → औ: विविध + औषध → विविधौषध."),
    ],
}


# ===================================================================== NOTES_HI
NOTES_HI = {
    "91": ("गद्य; विश्वास उच्च; कोई पाठ-चिह्न नहीं (०२.०६.१०१)। अग्नि = पाचन की अग्नि, पारिभाषिक शब्द। ‘अग्निदोषात्’ पञ्चमी: अग्नि के दोष से। "
           "‘ते’ (वे) किसकी ओर संकेत करता है, यह इकाई नहीं कहती; इस पर कोई प्रश्न नहीं। सन्धि जाँची: प्रायशः + दुष्यन्ति → प्रायशो दुष्यन्ति "
           "(अः + घोष व्यंजन → ओ); दुष्यन्ति + अग्नि → दुष्यन्त्यग्नि (इ + भिन्न स्वर → य्); छपा ‘दुष्यंति’ में ं = न्।"),
    "92": ("गद्य; विश्वास निम्न; कोई पाठ-चिह्न नहीं (०२.०६.१०२)। अधूरा कथन: क्रिया या षष्ठी नहीं, इसलिए ‘किसके निमित्त’ स्पष्ट नहीं; "
           "‘अग्नि इनका कारण’ डेटा का सम्भावित अर्थ भर है, जोड़ा नहीं गया; इस पर कोई प्रश्न नहीं। ओजस् = जीवन-सार, ओज (पारिभाषिक)। "
           "सन्धि जाँची: तस्मात् + निमित्तानि → तस्मान्निमित्तानि (नासिक्य से पहले त् → न्, यहाँ यही छपा); निमित्तानि + आयुः → "
           "निमित्तान्यायुः (इ + आ → या); आयुः + आरोग्य → आयुरारोग्य (उ के बाद विसर्ग + स्वर → र्); बल + उपचय → बलोपचय (अ + उ → ओ); "
           "वर्ण + ओजांसि → वर्णौजांसि (अ + ओ → औ)।"),
    "93": ("गद्य; विश्वास मध्यम; दो छपी पंक्तियाँ (०२.०६.१०३, ०२.०६.१०४); कोई पाठ-चिह्न नहीं। ‘तत्’ और ‘तेन’ = वह अग्नि (समझी हुई)। "
           "रञ्जक = रंग देने वाला पित्त-भेद (परवर्ती आयुर्वेद में मानक); ‘आदि’ के अन्य भेद यहाँ नहीं गिनाए। नपुंसक ‘रञ्जकादीनि’ के साथ पुंलिंग "
           "अग्नियाँ: सूची ढीली है। छपा ‘पक्क’ = पक्व (वर्तनी)। क्रिया ‘याति’ दोनों हिस्सों की है। सन्धि जाँची: प्रतिबद्धानि + एव → "
           "प्रतिबद्धान्येव (इ + ए → ये); भूत + अग्नयः → भूताग्नयः (अ + अ → आ); भूताग्नयः + धात्व... → भूताग्नयो धात्व... (अः + घोष व्यंजन → ओ); "
           "धातु + अग्नयः → धात्वग्नयः (उ + अ → व); तथा + अन्नम् → तथाऽन्नम् (आ + अ → आ, ऽ छपाई की आदत); तेन + एव → तेनैव (अ + ए → ऐ); "
           "याति + अपक्वम् → यात्यपक्वम् (इ + अ → य)।"),
    "94": ("गद्य; विश्वास उच्च; कोई पाठ-चिह्न नहीं (०२.०६.१०५)। ‘इति’ उद्धृत कथन को बन्द करता है। पहले का कथन ग्रन्थ के किसी पहले भाग में "
           "है, यहाँ जाँचा नहीं गया। सन्धि जाँची: पाचकसंज्ञः + अग्निः → पाचकसंज्ञोऽग्निः (अः + अ → ओऽ); अग्निः + इति → अग्निरिति (इ के बाद "
           "विसर्ग + स्वर → र्); प्राक् + अभिहितः → प्रागभिहितः (स्वर से पहले क् → ग्)।"),
    "95": ("गद्य; विश्वास उच्च; कोई पाठ-चिह्न नहीं (०२.०६.१०६)। समूह-टिप्पणी: यह इकाई ९६ (पंक्ति १०७) के मत का आरम्भ करती है। ‘अन्ये’ "
           "के नाम नहीं। ‘आचक्षते’ = आ-√चक्ष्, वर्तमान, प्रथम पुरुष बहुवचन, आत्मनेपद (कर्मवाच्य नहीं)। सन्धि जाँची: पुनः (मूल पुनर्) + "
           "आचक्षते → पुनराचक्षते।"),
    "96": ("गद्य; विश्वास मध्यम; कोई पाठ-चिह्न नहीं (०२.०६.१०७)। अन्त का ‘इति’ उद्धृत मत की समाप्ति। मल = अपशिष्ट (पारिभाषिक)। "
           "‘यथानिर्दिष्ट’ पहले के कथनों की ओर संकेत करता है, यहाँ जाँचे नहीं गए; अधिष्ठान और कर्म पर कोई प्रश्न नहीं। सन्धि जाँची: "
           "जनितः + अन्तर् → जनितोऽन्तर् (अः + अ → ओऽ); अन्तर् + ऊष्मा → अन्तरूष्मा; कर्मा + अग्निः → कर्माऽग्निः (आ + अ → आ, ऽ छपाई "
           "की आदत); अग्निः + इति → अग्निरिति।"),
    "97": ("गद्य; विश्वास मध्यम; कोई पाठ-चिह्न नहीं (०२.०६.१०८)। एक लम्बा वाक्य; ‘अभिसन्धुक्षितः’ (सुलगाया हुआ) अग्नि का विशेषण है। "
           "‘अग्निरन्तरग्निः’ = अग्निः + अन्तर्-अग्निः। प्राण और समान वायुओं के पारिभाषिक नाम। आमाशय = जठर (सम्भावित); कोष्ठ = भण्डार, पेट। "
           "सन्धि जाँची: विधिवत् + अभ्यवहृतम् → विधिवदभ्यवहृतम् (स्वर से पहले त् → द्); द्रवैः + विभिन्न → द्रवैर्विभिन्न (ऐ के बाद विसर्ग "
           "+ घोष ध्वनि → र्); समानेन + आमाशय → समानेनामाशय (अ + आ → आ); स्थालीस्थम् + इव → स्थालीस्थमिव; अग्निः + अन्तरग्निः → "
           "अग्निरन्तरग्निः। छपाई में कई शब्द जुड़े हैं (‘अन्नजातंप्राणेन’)।"),
    "98": ("गद्य; विश्वास मध्यम (०२.०६.१०९)। पाठ-चिह्न (सम्भावित): छपा ‘तस्तु’ अर्थ नहीं देता; ‘तत् तु’ (वह अन्न तो) पढ़ा गया, क्योंकि "
           "नपुंसक कृदन्त (पच्यमानम्) उससे मेल खाते हैं; इस पर कोई प्रश्न नहीं। छपा ‘फेनीभूतमूदीरयति’ में मू (दीर्घ) है, जबकि शब्द-विभाग "
           "‘उदीरयति’ (ह्रस्व उ) देता है; पाठ-चिह्न नहीं लगा; इस जोड़ पर कोई प्रश्न नहीं। सर्वरस = सब रसों वाला। मधुरीभूत, फेनीभूत: -ई-भूत = "
           "जो पहले न था, वैसा हो गया। सन्धि जाँची: सर्वरसम् + अपि → सर्वरसमपि; पच्यमानम् + आदौ → पच्यमानमादौ (स्वर से पहले म्)।"),
    "99": ("गद्य; विश्वास मध्यम; कोई पाठ-चिह्न नहीं (०२.०६.११०)। अधूरा वाक्य: क्रिया ‘उदीरयति’ इकाई ९८ (पंक्ति १०९) से आती है, जोड़ी नहीं "
           "गई; कर्ता अन्न समझा जाता है। विदग्ध = जला हुआ, अधिक पका (शाब्दिक); अच्छ = स्वच्छ। सन्धि जाँची: ततः + विदग्धम् → ततो विदग्धम् "
           "(अः + घोष व्यंजन → ओ); आमाशयात् + च्यवमानम् → आमाशयाच्च्यवमानम् (च से पहले त् → च्); अच्छम् + पित्तम् → अच्छं पित्तम्।"),
    "100": ("गद्य; विश्वास मध्यम; कोई पाठ-चिह्न नहीं (०२.०६.१११)। अधूरा वाक्य: क्रिया ‘उदीरयति’ इकाई ९८ (पंक्ति १०९) से आती है। "
            "पक्वाशय = बड़ी आँत का क्षेत्र (सम्भावित)। अनिल = वायु, यहाँ प्रसंग से वात दोष। प्राप्य = प्र + √आप्, ल्यप् (-य)। सन्धि जाँची: "
            "पक्व + आशय → पक्वाशय (अ + आ → आ); कटुकीभूतम् + अनिलम् → कटुकीभूतमनिलम्।"),
    "101": ("गद्य; विश्वास निम्न; क्षतिग्रस्त छपाई (०२.०६.११२)। पाठ-चिह्न (सम्भावित): ‘पंचातमक महाभूतन मयो’ अस्पष्ट; ‘पञ्चात्मकाः "
            "महाभूताग्नयः’ केवल अनुमान, अपनाया नहीं; नपुंसक ‘व्यस्तानि’ नपुंसक कर्ता (जैसे महाभूतानि) की ओर भी संकेत कर सकता है। इसलिए "
            "‘पचन्ति’ का कर्ता और ‘व्यस्तानि’ का व्याकरण अनिश्चित; इन पर कोई प्रश्न नहीं। पाठ-चिह्न (सम्भावित): छपा ‘विक्लिन्नआहारे’ = "
            "‘विक्लिन्ने आहारे’ (स्वर जुड़े नहीं छपे)। छपा ‘व्यस्तान्यथास्वं’ को डेटा ‘व्यस्तानि यथास्वम्’ पढ़ता है। तुलना: इकाई ९३ की "
            "भूताग्नियाँ। सन्धि जाँची: ततः + च → ततश्च (च से पहले विसर्ग → श्); च + एवम् → चैवम् (अ + ए → ऐ); पञ्च + एव → पञ्चैव "
            "(अ + ए → ऐ); भूतगुणान् + आहार... → भूतगुणानाहार...।"),
    "102": ("गद्य; विश्वास मध्यम; कोई पाठ-चिह्न नहीं (०२.०६.११३)। ‘ते’ = पाँच भूत-गुण, इकाई १०१ (पंक्ति ११२) से समझे गए। छपा ‘पक्काः’ = "
            "पक्वाः। ‘स्वाविकारभूतान्’ दो तरह पढ़ा जा सकता है: स्व-अविकार-भूतान् (अपने अविकृत स्वरूप वाले, डेटा का पाठ) या स्व-विकार-भूतान् "
            "(अपने ही विकार रूप); इस पर कोई प्रश्न नहीं। सन्धि जाँची: पुनः (पुनर्) + यथास्वम् → पुनर्यथास्वम्; यथास्वम् + एव → यथास्वमेव; "
            "देहाश्रितान् + च → देहाश्रितांश्च (च से पहले न् → ंश्)।"),
    "103": ("गद्य; विश्वास मध्यम; कोई पाठ-चिह्न नहीं (०२.०६.११४)। स्नेह की उपमा शाब्दिक रखी गई; उसका बिन्दु पाठ नहीं बताता, इस पर कोई प्रश्न "
            "नहीं। छपा ‘पक्क’ = पक्व। किट्ट = अन्न का बचा कचरा। दो कर्ताओं के साथ क्रिया एकवचन। सन्धि जाँची: पक्वात् + आहारात् → "
            "पक्वादाहारात् (स्वर से पहले त् → द्); आहारात् + विविध → आहाराद्विविध (घोष व्यंजन से पहले त् → द्); विविध + औषध → विविधौषध "
            "(अ + औ → औ); गर्भात् + इव → गर्भादिव; स्नेहात् + अच्छः → स्नेहादच्छः; सारभूतः + रसाख्यः → सारभूतो रसाख्यः (अः + घोष व्यंजन "
            "→ ओ); किट्टाख्यः + च → किट्टाख्यश्च; मलः + अभि... → मलोऽभि... (अः + अ → ओऽ)।"),
}


# ===================================================================== AIDS
AIDS = {
    "91": {
        "chunks": "ते च | प्रायशो | दुष्यंत्यग्निदोषात्",
        "frame": "कौन: ते (वे) → कितना: प्रायशः (अधिकतर) → क्या होता है: दुष्यन्ति (दूषित होते हैं) → किस कारण: अग्निदोषात् (अग्नि के दोष से)।",
        "sandhi": "अः + घोष व्यंजन → ओ: प्रायशः + दुष्यन्ति → प्रायशो दुष्यन्ति · इ + भिन्न स्वर → य्: दुष्यन्ति + अग्नि → दुष्यन्त्यग्नि।",
    },
    "92": {
        "diagram": {"groups": [
            {"label": "निमित्तानि के बाद छह शब्द, छपे क्रम में (सम्बन्ध नहीं बताया)",
             "items": ["१ आयुः (जीवन-काल)", "२ आरोग्य (स्वास्थ्य)", "३ बल", "४ उपचय (वृद्धि)", "५ वर्ण (रंगत)",
                       "६ ओजस् (जीवन-सार)"]}]},
        "chunks": "तस्मान्निमित्तानि | आयुरारोग्यबलोपचयवर्णौजांसि",
        "sandhi": ("अ + उ → ओ: बल + उपचय → बलोपचय · अ + ओ → औ: वर्ण + ओजांसि → वर्णौजांसि · उ के बाद विसर्ग + स्वर → र्: "
                   "आयुः + आरोग्य → आयुरारोग्य।"),
        "letters": "पहले अक्षर क्रम से: आ-आ-ब-उ-व-ओ (आयु, आरोग्य, बल, उपचय, वर्ण, ओज)। (मेरी याद-पद्धति)",
    },
    "93": {
        "diagram": {"groups": [
            {"label": "पंक्ति १: उसी (अग्नि) पर आश्रित", "items": ["रञ्जक आदि (रंग देने वाला पित्त-भेद)", "भूताग्नियाँ",
                                                             "धात्वग्नियाँ"]},
            {"label": "पंक्ति २: अन्न", "items": ["उसी से पचा (पक्व) → अमृतता", "बिना पचा (अपक्व) → विषता"]}]},
        "seesaw": "पक्व (पचा) अन्न → अमृतता (अमृत-भाव) ⟷ अपक्व (बिना पचा) अन्न → विषता (विष-भाव)।",
        "chunks": "तत्प्रतिबद्धान्येवच | रंजकादीनि | भूताग्नयो | धात्वग्नयश्च || तथाऽन्नमपि | तेनैव पक्कम् | अमृततां याति | अपक्वं च | विषतां",
        "sandhi": "अ + ए → ऐ: तेन + एव → तेनैव · उ + अ → व: धातु + अग्नयः → धात्वग्नयः · इ + अ → य: याति + अपक्वम् → यात्यपक्वम्।",
    },
    "94": {
        "chunks": "तत्र | पित्तविशेषः | पाचकसंज्ञोऽग्निरिति | प्रागभिहितः",
        "frame": "कहाँ से: तत्र (उनमें) → क्या: पित्तविशेषः (पित्त का विशेष भेद) → नाम: पाचक → वह है: अग्निः → स्रोत: प्राक् अभिहितः (पहले कहा)।",
        "sandhi": "अः + अ → ओऽ: पाचकसंज्ञः + अग्निः → पाचकसंज्ञोऽग्निः · स्वर से पहले क् → ग्: प्राक् + अभिहितः → प्रागभिहितः।",
        "anchors": "पाचक ~ पचाना: जो पचाए वह पाचक। (मेरी याद-पद्धति, शब्द-साम्य पर)",
    },
    "95": {
        "chunks": "अन्ये | पुनराचक्षते",
        "sandhi": "पुनः मूल में पुनर् है; स्वर से पहले र् दिखता है: पुनः + आचक्षते → पुनराचक्षते।",
        "frame": "कौन: अन्ये (दूसरे, नाम नहीं) → फिर: पुनः → क्या करते हैं: आचक्षते (कहते हैं, वर्तमान, आत्मनेपद)।",
    },
    "96": {
        "diagram": {"groups": [
            {"label": "दूसरों का मत: अग्नि क्या है", "items": ["दोष", "धातु", "मल (अपशिष्ट)", "इनका सन्निपात (मेल)",
                                                         "उससे जनित अन्तर्-ऊष्मा (भीतरी ताप)", "यही अग्नि",
                                                         "अधिष्ठान और कर्म: जैसे पहले बताए"]}]},
        "chunks": "दोषधातुमलसन्निपातजनितोऽन्तरूष्मा | यथानिर्दिष्टाधिष्ठानकर्माऽग्निरिति",
        "sandhi": "अः + अ → ओऽ: जनितः + अन्तरूष्मा → जनितोऽन्तरूष्मा · आ + अ → आ: कर्मा + अग्निः → कर्माऽग्निः (ऽ छपाई की आदत)।",
        "frame": "किससे: दोष-धातु-मल का सन्निपात → क्या बना: अन्तर्-ऊष्मा → स्थान, कर्म: यथानिर्दिष्ट → नाम: अग्नि।",
    },
    "97": {
        "chain": {"steps": ["विधि से खाया अन्न", "प्राण वायु ने कोष्ठ में खींचा", "द्रवों से संघात टूटा", "स्नेह से नरम हुआ",
                            "आमाशय में स्थित", "समान से सुलगी अग्नि पकाती है"]},
        "chunks": ("स खलु | विधिवदभ्यवहृतमन्नजातं | प्राणेन वायुना कोष्ठमाकृष्टं | द्रवैर्विभिन्नसंघातं | स्नेहेन मृदूकृतम् | "
                   "अभिसंधुक्षितः समानेन | आमाशयस्थं | स्थालीस्थमिवांबुतंडुलम् | अग्निरंतरग्निःपचति"),
        "sandhi": ("स्वर से पहले त् → द्: विधिवत् + अभ्यवहृतम् → विधिवदभ्यवहृतम् · ऐ के बाद विसर्ग + घोष ध्वनि → र्: द्रवैः + विभिन्न "
                   "→ द्रवैर्विभिन्न · अ + आ → आ: समानेन + आमाशय → समानेनामाशय।"),
        "story": "उपमा पाठ की ही है: जैसे हाँडी (स्थाली) में पानी और चावल आग पर पकते हैं, वैसे आमाशय में पड़ा अन्न भीतरी अग्नि से पकता है।",
    },
    "98": {
        "chunks": "तस्तु | सर्वरसमपि | पच्यमानमादौ | मधुरीभूतं | कफं | फेनीभूतमूदीरयति",
        "frame": "क्या: अन्न (सब रसों वाला भी) → कब: पकते समय, आदौ (पहले) → कैसा बना: मधुर → क्या करता है: फेनिल कफ को उभारता है।",
        "sandhi": "स्वर से पहले म् बना रहता है: पच्यमानम् + आदौ → पच्यमानमादौ · -ई-भूत: मधुर → मधुरीभूत (मधुर हो गया)।",
    },
    "99": {
        "chunks": "ततो | विदग्धम् | अम्लीभूतम् | आमाशयाच्च्यवमानम् | अच्छंपित्तं",
        "frame": "कब: ततः (तब) → अन्न कैसा: विदग्ध, अम्ल → कहाँ से: आमाशय से खिसकता → किसे (उदीरयति, इकाई ९८ से): अच्छ पित्त।",
        "sandhi": "अः + घोष व्यंजन → ओ: ततः + विदग्धम् → ततो विदग्धम् · च से पहले त् → च्: आमाशयात् + च्यवमानम् → आमाशयाच्च्यवमानम्।",
    },
    "100": {
        "diagram": {"groups": [
            {"label": "पकने के तीन चरण, इकाई ९८-१०० (अन्न का रस → उभरा दोष)",
             "items": ["१ आदौ, पहले (९८): मधुर → फेनिल कफ", "२ ततः, आमाशय से खिसकता (९९): अम्ल → अच्छ पित्त",
                       "३ पक्वाशय पहुँचकर (१००): कटु → अनिल (वात)"]}]},
        "chunks": "प्राप्य च | पक्वाशयं | कटुकीभूतम् | अनिलं",
        "frame": "कहाँ पहुँचकर: पक्वाशय (सम्भावित: बड़ी आँत का क्षेत्र) → अन्न कैसा: कटु → किसे (उदीरयति, इकाई ९८ से): अनिल, वात।",
    },
    "101": {
        "chunks": "ततश्चैवं | विक्लिन्नआहारे | पंच (पंचातमक महाभूतन मयो: अस्पष्ट) | वायुना | व्यस्तान्यथास्वं | पंचैवभूतगुणानाहारस्थान् | पचंति",
        "sandhi": "च से पहले विसर्ग → श्: ततः + च → ततश्च · अ + ए → ऐ: च + एवम् → चैवम्, पञ्च + एव → पञ्चैव।",
        "frame": "कब: आहार भीगने पर → कौन: अस्पष्ट (क्षतिग्रस्त छपाई) → कैसे: वायु से, अपने-अपने अनुसार → किसे पकाते हैं: आहार में स्थित पाँच भूत-गुण।",
    },
    "102": {
        "chunks": "ते पक्काः | पुनर्यथास्वमेव | देहाश्रितांश्च | स्वाविकारभूतान् | भूतगुणानाप्याययंति",
        "sandhi": "च से पहले न् → ंश्: देहाश्रितान् + च → देहाश्रितांश्च · पुनः (पुनर्) + यथास्वम् → पुनर्यथास्वम्।",
        "frame": "कौन: ते (भूत-गुण, इकाई १०१ से), पके हुए → कैसे: फिर, अपने-अपने अनुसार → किसे: देह में स्थित भूत-गुण → क्या: आप्याययन्ति (पुष्ट करते हैं)।",
    },
    "103": {
        "contrast": {"groups": [
            {"label": "रस (सार)", "items": ["अच्छ: स्वच्छ", "सारभूत: सार रूप", "नाम: रस"]},
            {"label": "किट्ट (मल)", "items": ["मल: अपशिष्ट", "नाम: किट्ट"]}]},
        "chunks": "एवं च | पक्कादाहाराद् | विविधौषधगर्भादिव स्नेहाद् | अच्छः सारभूतो रसाख्यः | किट्टाख्यश्चमलो | ऽभिनिर्वर्तते",
        "sandhi": ("स्वर से पहले त् → द्: पक्वात् + आहारात् → पक्वादाहारात् · अ + औ → औ: विविध + औषध → विविधौषध · अः + घोष व्यंजन → ओ: "
                   "सारभूतः + रसाख्यः → सारभूतो रसाख्यः · अः + अ → ओऽ: मलः + अभि... → मलोऽभि..."),
    },
}


# ===================================================================== IMAGE_SPECS
IMAGE_SPECS = {
    ("92", "diagram"): {
        "file": "sh6-ayuradi-shat-92.svg",
        "alt": ("Numbered table of the six words that follow 'therefore, the causes' in unit 92, in printed order: 1 lifespan, "
                "2 health, 3 strength, 4 growth, 5 complexion, 6 ojas. Their relation to the causes is not stated."),
        "type": "table",
        "title": "इकाई ९२: निमित्तानि के बाद छह शब्द",
        "heads": ["क्रम", "शब्द (अर्थ)"],
        "rows": [["१", "आयुः (जीवन-काल)"], ["२", "आरोग्य (स्वास्थ्य)"], ["३", "बल"], ["४", "उपचय (वृद्धि)"],
                 ["५", "वर्ण (रंगत)"], ["६", "ओजस् (जीवन-सार)"]],
    },
    ("93", "diagram"): {
        "file": "sh6-amrita-visha-93.svg",
        "alt": ("Flowchart of unit 93: agni (understood) at the top; dependent on it are rañjaka and the rest, the bhūtāgnis "
                "and the dhātvagnis; food digested by it attains the state of nectar, while undigested food attains the "
                "state of poison."),
        "type": "mermaid",
        "code": ("flowchart TD\n"
                 "  A[\"अग्नि (तत्, समझी हुई)\"]\n"
                 "  A --> B[\"आश्रित: रञ्जक आदि\"]\n"
                 "  A --> C[\"आश्रित: भूताग्नियाँ\"]\n"
                 "  A --> D[\"आश्रित: धात्वग्नियाँ\"]\n"
                 "  A --> E[\"उसी से पचा अन्न\"]\n"
                 "  E --> F[\"अमृतता: अमृत-भाव\"]\n"
                 "  G[\"अपक्व: बिना पचा अन्न\"] --> H[\"विषता: विष-भाव\"]\n"),
    },
    ("96", "diagram"): {
        "file": "sh6-antarushma-96.svg",
        "alt": ("Flowchart of the view in unit 96: doṣa, dhātu and mala come together; their coming together produces the "
                "inner heat; that inner heat is agni, with seat and function as indicated earlier."),
        "type": "mermaid",
        "code": ("flowchart TD\n"
                 "  A[\"दोष\"] --> D[\"सन्निपात: मेल\"]\n"
                 "  B[\"धातु\"] --> D\n"
                 "  C[\"मल: अपशिष्ट\"] --> D\n"
                 "  D --> E[\"अन्तर् ऊष्मा: भीतरी ताप\"]\n"
                 "  E --> F[\"यही अग्नि: दूसरों का मत\"]\n"),
    },
    ("97", "chain"): {
        "file": "sh6-sthali-97.svg",
        "alt": ("Chain of unit 97 in printed order: food eaten by rule; drawn into the koṣṭha by prāṇa; its mass broken by "
                "liquids; softened by sneha; lying in the āmāśaya; the agni kindled by samāna cooks it, like water and "
                "rice in a pot."),
        "type": "chain",
        "title": "इकाई ९७: हाँडी में पानी-चावल जैसे",
        "steps": ["विधि से खाया अन्न", "प्राण वायु ने कोष्ठ में खींचा", "द्रवों से संघात टूटा", "स्नेह से नरम हुआ",
                  "आमाशय में स्थित", "समान से सुलगी अग्नि पकाती है"],
    },
    ("100", "diagram"): {
        "file": "sh6-tin-charana-100.svg",
        "alt": ("Table of the three stages of cooking in units 98-100: first (98) sweet, stirring up foamy Kapha; then, "
                "falling from the āmāśaya (99), sour, stirring up clear Pitta; having reached the pakvāśaya (100), "
                "pungent, stirring up anila (Vāta)."),
        "type": "table",
        "title": "इकाई ९८-१००: पकने के तीन चरण",
        "heads": ["चरण (इकाई)", "अन्न का रस → उभरा दोष"],
        "rows": [["१ आदौ, पहले (९८)", "मधुर → फेनिल कफ"], ["२ आमाशय से खिसकता (९९)", "अम्ल → अच्छ पित्त"],
                 ["३ पक्वाशय पहुँचकर (१००)", "कटु → अनिल (वात)"]],
    },
    ("103", "contrast"): {
        "file": "sh6-rasa-kitta-103.svg",
        "alt": ("Two columns of unit 103: from the digested food come rasa, the clear essence (clear, of the nature of "
                "essence, named rasa), and kiṭṭa, the waste (mala, named kiṭṭa)."),
        "type": "split",
        "title": "इकाई १०३: पके आहार से दो",
        "cols": [["रस (सार)", ["अच्छ: स्वच्छ", "सारभूत: सार रूप", "नाम: रस"]],
                 ["किट्ट (मल)", ["मल: अपशिष्ट", "नाम: किट्ट"]]],
    },
}
