from helpers import mcq, match, order, fill, multi, accepts


def T(q, teaches):
    q["teaches"] = teaches
    return q


AUTHORED = {}

# ---------------------------------------------------------------- unit 116
AUTHORED["116"] = {
    "title": "बुभुक्षितां च ... स्नेहमात्रां पाययेत्",
    "question": "By unit 116, what dose is the hungry sūtikā given, joined with which powders?",
    "rule": ("To the hungry one (बुभुक्षिता) give a dose of sneha (स्नेहमात्रा), digesting within the day, according to "
             "suitability (यथासात्म्यम्), joined with pañcakola powder or with a powder of yavānī, upakuñcikā, cavya, "
             "citraka, vyoṣa and saindhava."),
    "limits": ("Prose, not a verse. च is read (data note) as linking it to unit 115 (balā oil). yavānī = ajwain (standard); upakuñcikā = probably "
               "nigella (disputed); saindhava = rock salt (standard); vyoṣa = the three pungents. Pañcakola's contents "
               "are not listed. 'Digesting by day's end' is a reading, not stated."),
    "explain_hi": ("यह गद्य-पंक्ति कहती है कि भूखी (बुभुक्षिता) सूतिका को स्नेह (तेल या घी) की मात्रा पिलानी चाहिए। "
                   "वह मात्रा पञ्चकोल के चूर्ण से, या यवानी (अजवायन, मानक), उपकुञ्चिका (सम्भवतः कलौंजी, विवादित), चव्य, "
                   "चित्रक, व्योष (तीन कटु) और सैन्धव (सेंधा नमक, मानक) के चूर्ण से युक्त हो; ‘वा’ इन दो चूर्णों के बीच है। "
                   "मात्रा ऐसी हो जो दिन में पच जाए (अहःपरिणामिनी), और सात्म्य के अनुसार (यथासात्म्यम्) हो। "
                   "आरम्भ का ‘च’ इसे इकाई ११५ (बला-तैल से अभ्यंग) से जोड़ता माना गया है।"),
    "hook": "भूखी को: पञ्चकोल या यवानी-आदि चूर्ण के साथ, दिन में पचने वाली स्नेह-मात्रा।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 116, to whom is the dose of sneha given?",
            ("To the hungry one (बुभुक्षिता)", "बुभुक्षितां ... स्नेहमात्रां पाययेत्: the hungry one is made to drink it."),
            [("To one unfit for sneha (स्नेहायोग्या)", "That woman is the subject of unit 117, not this one."),
             ("To one whose sneha is digested", "That is unit 119, where a yavāgū follows the digested sneha."),
             ("To one with no appetite at all", "The line says hungry (बुभुक्षिता), the opposite.")],
            "The hungry one is given a dose of sneha.",
            "बुभुक्षितां ... स्नेहमात्रां पाययेत्."),
        order(1, "Put the items of the second powder of unit 116 in the line's order.",
              ["यवानी", "उपकुञ्चिका", "चव्य", "चित्रक", "व्योष", "सैन्धव"],
              "yavānī, upakuñcikā, cavya, citraka, vyoṣa, saindhava, then चूर्णेन (with the powder).",
              "यवानी → उपकुञ्चिका → चव्य → चित्रक → व्योष → सैन्धव."),
        match(2, "Match each word of unit 116 to its meaning.",
              [["बुभुक्षिता", "hungry"], ["स्नेहमात्रा", "dose of sneha (oil or fat)"],
               ["यथासात्म्यम्", "according to suitability"], ["अहःपरिणामिनी", "digesting within the day"],
               ["पाययेत्", "should make (her) drink"]],
              "Who, what, how much, how fast and the verb of the line.",
              "बुभुक्षिता, स्नेहमात्रा, यथासात्म्यम्, अहःपरिणामिनी, पाययेत्.", role="extend",
              teaches="यथासात्म्यम् = according to what suits her (sātmya); the dose follows her, not a fixed amount."),
        mcq("discriminate", 3, "In unit 116, what two things does वा (or) set side by side?",
            ("The pañcakola powder and the yavānī-group powder", "The note: वा sits between the two powders."),
            [("The sneha dose and a dose of plain water", "No water is named in this line."),
             ("The hungry woman and the woman unfit for sneha", "The unfit woman comes in unit 117."),
             ("Yavānī and upakuñcikā alone, as two choices", "Both stand inside one list of the second powder.")],
            "वा: with pañcakola powder, or with the powder of yavānī and the rest.",
            "पञ्चकोलचूर्णेन ... चूर्णेन वा."),
        multi("apply", 4, "Which statements does unit 116 make?",
              [("The dose follows what suits her (यथासात्म्यम्)", "Right: यथासात्म्यं स्नेहमात्राम्."),
               ("The dose is given to the woman unfit for sneha (अस्नेह्या)", "That woman is in unit 117; here she is hungry."),
               ("The sneha is taken with milk instead of powder (क्षीर)", "No milk is named; the sneha is joined with powder."),
               ("Saindhava (rock salt) is in the second powder", "Right: ...व्योषसैन्धवचूर्णेन.")],
              [0, 3],
              "The dose suits her, and saindhava is one item of the second powder.",
              "यथासात्म्यं स्नेहमात्रां; ...सैन्धवचूर्णेन."),
        mcq("transfer", 5, "By the rule of यवान्युपकुञ्चिका, how is नदी + उदकम् (river water, a new example) joined?",
            ("नद्युदकम्", "ई + उ → यु, as यवानी + उपकुञ्चिका → यवान्युपकुञ्चिका."),
            [("नदीदकम्", "The उ is not lost after ई."),
             ("नद्योदकम्", "ई + उ does not give यो."),
             ("नदूदकम्", "ई + उ does not give ऊ.")],
            "नदी + उदकम् = नद्युदकम्, like यवानी + उपकुञ्चिका.",
            "ई + a different vowel → य् + that vowel.",
            teaches="A final ई before a different vowel becomes य्: यवानी + उपकुञ्चिका → यवान्युपकुञ्चिका."),
    ],
}

# ---------------------------------------------------------------- unit 117
AUTHORED["117"] = {
    "title": "स्नेहायोग्यां ... वेष्टयेदुदरं वस्त्रेण",
    "question": "By unit 117, what is given to the woman unfit for sneha, and what is done after she has drunk?",
    "rule": ("For one unfit for sneha: a decoction of vāta-relieving medicines, or of the lesser pañcamūla. For one who "
             "has drunk: anoint with yamaka and wrap the belly (उदर) with cloth (वस्त्र)."),
    "limits": ("Printed कथं is read as क्वाथ (decoction): a print habit, not certain; stray '=' sign. The verb of the first "
               "clause is carried from unit 116. yamaka = probably oil and ghee mixed (probable). The five roots of the lesser "
               "pañcamūla and what the second woman drank are not printed."),
    "explain_hi": ("जो स्त्री स्नेह के योग्य नहीं (स्नेहायोग्या), उसे वात हरने वाली औषधियों का क्वाथ, या ह्रस्व (छोटे) पञ्चमूल का "
                   "क्वाथ देना है; क्रिया ‘पाययेत्’ इकाई ११६ से समझी जाती है। "
                   "छपा ‘कथं’ यहाँ ‘क्वाथ’ पढ़ा गया है, यह छपाई की आदत मानी गई है, निश्चित नहीं। "
                   "जिसने पी लिया हो (पीतवती), उसका यमक (सम्भवतः तेल और घी का मिश्रण) से अभ्यंग करके पेट को कपड़े से लपेटना चाहिए। "
                   "ह्रस्व पञ्चमूल की पाँच जड़ों के नाम, और उसने क्या पिया, यह यहाँ छपा नहीं है।"),
    "hook": "स्नेह न सहे तो वातहर क्वाथ; पी ले तो यमक-अभ्यंग और पेट पर कपड़ा।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 117, who receives the vāta-relieving medicines or the lesser pañcamūla?",
            ("One unfit for sneha (स्नेहायोग्या)", "स्नेहायोग्यां वातहरौषध... ह्रस्वपञ्चमूल... वा."),
            [("One who is hungry (बुभुक्षिता)", "The hungry one gets the sneha dose in unit 116."),
             ("One whose sneha is digested", "She gets a yavāgū in unit 119."),
             ("One who is no longer called a sūtikā", "That is the end of the period, unit 125.")],
            "The woman unfit for sneha gets the vāta-relieving remedy instead.",
            "स्नेहायोग्याम् = for one unfit for sneha."),
        order(1, "Put these parts of unit 117 in the line's order.",
              ["स्नेहायोग्याम्", "वातहरौषध…", "ह्रस्वपञ्चमूल… वा", "पीतवत्याश्च", "यमकेनाभ्यज्य",
               "वेष्टयेदुदरं वस्त्रेण"],
              "Unfit for sneha, vāta-relieving medicines, or lesser pañcamūla; and for one who has drunk, anoint, wrap.",
              "स्नेहायोग्याम् → वातहर… → ह्रस्वपञ्चमूल… → पीतवत्याः → यमकेन अभ्यज्य → वेष्टयेत्."),
        match(2, "Match each word of unit 117 to its meaning.",
              [["स्नेहायोग्या", "unfit for sneha"], ["वातहर", "removing vāta"], ["पीतवती", "one who has drunk"],
               ["वेष्टयेत्", "should wrap"], ["उदरम्", "belly"], ["वस्त्रेण", "with cloth"]],
              "Six words carry the two clauses of the line.",
              "स्नेहायोग्या, वातहर, पीतवती, वेष्टयेत्, उदरम्, वस्त्रेण.", role="extend",
              teaches="पीतवती = one who has drunk: -वत् (fem. -वती) on the past participle पीत makes 'having drunk'."),
        mcq("discriminate", 3, "Which split of स्नेहायोग्याम् is right?",
            ("स्नेह + अयोग्याम्", "अ + अ → आ: स्नेह + अयोग्याम् = स्नेहायोग्याम् (unfit for sneha)."),
            [("स्नेहः + अयोग्याम्", "A visarga after अ before अ would give स्नेहोऽयोग्याम्."),
             ("स्नेहम् + अयोग्याम्", "A final म् would give स्नेहमयोग्याम्."),
             ("स्नेह + आयोग्याम्", "आयोग्या is not a word; the word is अयोग्या, unfit.")],
            "स्नेह (sneha) + अयोग्या (unfit): अ + अ → आ.",
            "अ + अ → आ."),
        mcq("apply", 4, "By unit 117, what is done for the woman who has drunk?",
            ("Anoint with yamaka, wrap the belly in cloth", "पीतवत्याश्च यमकेनाभ्यज्य वेष्टयेदुदरं वस्त्रेण."),
            [("Sprinkle her with hot water before the drinks", "Hot-water sprinkling is unit 120."),
             ("Give her a liquid yavāgū in measure", "The yavāgū comes in unit 119."),
             ("Anoint her with balā oil and let her rest", "Balā oil is unit 115.")],
            "After she has drunk: yamaka anointing, then the belly wrapped with cloth.",
            "यमकेन अभ्यज्य वेष्टयेत् उदरं वस्त्रेण."),
        mcq("transfer", 5, "By the rule of पीतवत्याश्च, how is रामः + च (and Rāma, a new example) joined?",
            ("रामश्च", "A visarga before च becomes श्, as पीतवत्याः + च → पीतवत्याश्च."),
            [("रामोच", "ओ comes from अः before a voiced sound; च is not voiced."),
             ("रामच", "The visarga is not lost before च."),
             ("रामस्च", "Before च the visarga becomes श्, not स्.")],
            "रामः + च = रामश्च, like पीतवत्याः + च.",
            "Visarga + च/छ → श्.",
            teaches="A visarga before च becomes श्: पीतवत्याः + च → पीतवत्याश्च."),
    ],
}

# ---------------------------------------------------------------- unit 118
AUTHORED["118"] = {
    "title": "तथा न वायुः ... अनवकाशत्वात्",
    "question": "By unit 118, why would vāyu (wind) not produce an alteration of the belly?",
    "rule": ("Thus (तथा) vāyu would not produce an alteration of the belly (उदरविकृति), because there is no space "
             "(अनवकाशत्वात्). -त्वात् = because of being."),
    "limits": ("The line does not name what 'thus' points back to; by the sequence it follows the wrapping of unit 117. "
               "उदर = belly here, not the disease udara. Printed विक्कृति has a doubled क (read विकृति)."),
    "explain_hi": ("इस प्रकार (तथा) वायु पेट में विकार उत्पन्न नहीं करेगी, क्योंकि उसे अवकाश (जगह) नहीं मिलता (अनवकाशत्वात्)। "
                   "‘तथा’ किस बात की ओर संकेत करता है, यह पंक्ति नहीं कहती; क्रम से यह इकाई ११७ के पेट लपेटने के बाद आती है। "
                   "उदर यहाँ पेट है, उदर-रोग नहीं। "
                   "‘अनवकाशत्वात्’ = अन् (नहीं) + अवकाश (जगह) + त्व (होना) + पञ्चमी: ‘जगह न होने के कारण’। "
                   "छपा ‘विक्कृति’ में क दो बार है, ‘विकृति’ पढ़ा गया।"),
    "hook": "जगह नहीं, तो वायु पेट नहीं बिगाड़ती।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 118, why would vāyu not alter the belly?",
            ("Because it has no space (अनवकाशत्वात्)", "अनवकाशत्वात्: because of the absence of space."),
            [("Because the sneha is digested (जीर्णे)", "Digested sneha is unit 119."),
             ("Because she is bathed (परिषेचन)", "Hot-water sprinkling is unit 120."),
             ("Because of the gruel (यवागू) she drinks", "No gruel is named in unit 118.")],
            "No space, so no alteration of the belly.",
            "अनवकाशत्वात् = because of absence of space."),
        order(1, "Put the words of unit 118 in the line's order.",
              ["तथा", "न", "वायुः", "उदरविकृतिम्", "उत्पादयेत्", "अनवकाशत्वात्"],
              "Thus not wind the belly's alteration would produce, because of no space.",
              "तथा → न → वायुः → उदरविकृतिम् → उत्पादयेत् → अनवकाशत्वात्."),
        match(2, "Match each word of unit 118 to its meaning.",
              [["वायुः", "wind (vāyu)"], ["उदर", "belly"], ["विकृति", "alteration"],
               ["उत्पादयेत्", "would produce"], ["अनवकाशत्वात्", "because of absence of space"]],
              "Five words carry the whole statement.",
              "वायुः, उदर, विकृति, उत्पादयेत्, अनवकाशत्वात्.", role="extend",
              teaches="-त्वात् (ablative of the abstract -त्व) gives the reason: अनवकाशत्वात् = because of having no space."),
        mcq("discriminate", 3, "In unit 118, what does उदर mean, by the data's note?",
            ("The belly", "The note: उदर is rendered belly, not the disease udara."),
            [("The disease udara (abdominal disorder)", "The note rules this out for this line."),
             ("The womb that held the foetus", "The word is उदर, belly; no womb word is used."),
             ("The digestive fire (agni)", "Agni is a different word, named in unit 121.")],
            "उदरविकृति = alteration of the belly.",
            "उदर = belly here."),
        mcq("apply", 4, "Why does the negative in अनवकाशत्वात् take the form अन्- and not अ-?",
            ("Because the next word अवकाश begins with a vowel", "The negative prefix is अन्- before a vowel, अ- before a consonant."),
            [("Because the whole word stands in the ablative case, -त्वात्", "The case ending does not choose the prefix."),
             ("Because अन्- means 'very', not 'not'", "अन्- here is the negative: absence of space."),
             ("Because the subject वायुः is masculine", "Gender does not choose the prefix.")],
            "अन् + अवकाश: अन्- before a vowel.",
            "Negative prefix: अ- before a consonant, अन्- before a vowel."),
        mcq("transfer", 5, "By the rule of अनवकाश, what is the negative of उचित (proper, a new example)?",
            ("अनुचित", "अन्- before a vowel, as अन् + अवकाश → अनवकाश."),
            [("अउचित", "Before a vowel the negative is अन्-, not अ-."),
             ("अनूचित", "The उ of उचित does not lengthen."),
             ("अन्नुचित", "The न is not doubled.")],
            "अन् + उचित = अनुचित, like अन् + अवकाश = अनवकाश.",
            "अन्- before a vowel.",
            teaches="The negative prefix is अन्- before a vowel: अन् + अवकाश → अनवकाश; अन् + उचित → अनुचित."),
    ],
}

# ---------------------------------------------------------------- unit 119
AUTHORED["119"] = {
    "title": "जीर्णे तु स्नेहे ... यवागूं ... पाययेत्",
    "question": "By unit 119, once the sneha is digested, what yavāgū is given and how is it cooked?",
    "rule": ("When the sneha is digested (जीर्णे स्नेहे), give in measure a yavāgū (gruel), well boiled and liquid, cooked "
             "with the same earlier medicines, or with the vidārī group, or with milk."),
    "limits": ("Printed कथाथ is read as क्वाथ (decoction): not certain, no question on it. vidārī = Pueraria tuberosa, "
               "probable (several plants are called vidārī). 'Cooked' is read as governing all three means. No amount "
               "is given for मात्रया."),
    "explain_hi": ("स्नेह पच जाने पर (जीर्णे स्नेहे) यवागू पिलानी है। वह यवागू पहले वाली ही औषधियों से, या विदारी "
                   "(सम्भवतः Pueraria tuberosa, सम्भावित पहचान) आदि गण के क्वाथ से, या दूध से सिद्ध की गई हो। "
                   "वह भली प्रकार उबली (सुस्विन्ना) और तरल (द्रवा) हो, और मात्रा से (मात्रया) दी जाए। "
                   "छपा ‘कथाथ’ यहाँ ‘क्वाथ’ पढ़ा गया है, यह निश्चित नहीं। "
                   "‘एव’ जोर देता है: वही पहले वाली औषधियाँ।"),
    "hook": "स्नेह पचे, तब यवागू: पुरानी औषधि, विदारी-गण या दूध से; पतली, खूब उबली।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 119, when is the yavāgū given?",
            ("When the sneha has been digested", "जीर्णे तु स्नेहे: when the sneha is digested."),
            [("Before any sneha is drunk at all", "Unit 119 opens with the sneha already digested."),
             ("Only after the twelfth night", "The twelve nights belong to unit 121."),
             ("When the menses appear again", "That is a view on the end of the period, unit 126.")],
            "The yavāgū follows the digested sneha.",
            "जीर्णे स्नेहे ... यवागूं पाययेत्."),
        order(1, "Put these parts of unit 119 in the line's order.",
              ["जीर्णे तु स्नेहे", "पूर्वौषधैरेव सिद्धाम्", "विदार्यादिगण…", "क्षीरेण वा", "यवागूम्",
               "मात्रया पाययेत्"],
              "When digested, cooked with the earlier medicines, the vidārī group or milk, a yavāgū, in measure.",
              "जीर्णे स्नेहे → पूर्वौषधैः → विदार्यादिगण… → क्षीरेण वा → यवागूम् → मात्रया पाययेत्."),
        match(2, "Match each word of unit 119 to its meaning.",
              [["जीर्णे", "when digested"], ["सिद्धाम्", "cooked"], ["सुस्विन्नाम्", "well boiled"],
               ["द्रवाम्", "liquid"], ["मात्रया", "in measure"]],
              "These words say when, and what kind of yavāgū.",
              "जीर्णे, सिद्धाम्, सुस्विन्नाम्, द्रवाम्, मात्रया.", role="extend",
              teaches="जीर्णे स्नेहे: two locatives together mark the time, 'when the sneha is digested'."),
        mcq("discriminate", 3, "Which split of पूर्वौषधैः is right?",
            ("पूर्व + औषधैः", "अ + औ → औ: पूर्व + औषधैः = पूर्वौषधैः (the earlier medicines)."),
            [("पूर्वम् + औषधैः", "A final म् would give पूर्वमौषधैः."),
             ("पूर्वः + औषधैः", "अः before a vowel other than अ loses the visarga: पूर्व औषधैः, with a gap."),
             ("पूर्वौ + षधैः", "षधैः is not a word; the word is औषधैः, medicines.")],
            "पूर्व (earlier) + औषधैः (medicines): अ + औ → औ.",
            "अ + औ → औ."),
        multi("apply", 4, "By unit 119, with which may the yavāgū be cooked?",
              [("With hot water alone", "Hot water is for sprinkling in unit 120."),
               ("With the very same earlier medicines", "Right: पूर्वौषधैरेव सिद्धाम्."),
               ("With jāṅgala broths", "Jāṅgala broths come after twelve nights in unit 121."),
               ("With milk", "Right: क्षीरेण वा.")],
              [1, 3],
              "Earlier medicines, the vidārī group, or milk; not hot water or broth.",
              "पूर्वौषधैरेव ... विदार्यादिगण... क्षीरेण वा."),
        mcq("transfer", 5, "By the rule of पूर्वौषधैः, how is जल + औघः (flood of water, a new example) joined?",
            ("जलौघः", "अ + औ → औ, as पूर्व + औषधैः → पूर्वौषधैः."),
            [("जलोघः", "अ + औ does not give ओ."),
             ("जलाघः", "अ + औ does not give आ."),
             ("जलवौघः", "No व is put between अ and औ.")],
            "जल + औघः = जलौघः, like पूर्व + औषधैः.",
            "अ/आ + ओ/औ → औ.",
            teaches="A final अ before औ merges into औ: पूर्व + औषधैः → पूर्वौषधैः."),
    ],
}

# ---------------------------------------------------------------- unit 120
AUTHORED["120"] = {
    "title": "प्राक्स्नेहयवागूपानभ्यां ... परिषेचयेत्",
    "question": "By unit 120, when and with what is the sprinkling done?",
    "rule": ("Before (प्राक्) drinking the sneha and the yavāgū, at both times (उभयकालम्), sprinkle or bathe with hot "
             "water (उष्णोदक). प्राक् takes the ablative."),
    "limits": ("Printed पानभ्यां is read पानाभ्याम् (short a for ā). Who or what is sprinkled is not stated. 'Both times' "
               "is read as before the sneha and before the yavāgū; that reading is the data's, not printed."),
    "explain_hi": ("स्नेह और यवागू पीने से पहले (प्राक्), दोनों समय (उभयकालम्), गरम पानी (उष्णोदक) से परिषेचन, यानी सींचना या "
                   "स्नान कराना चाहिए। "
                   "‘प्राक्’ के साथ पञ्चमी आती है: स्नेहयवागूपानाभ्याम् (दो पानों से पहले)। "
                   "किसे सींचना है, यह नहीं लिखा। "
                   "‘दोनों समय’ को डेटा स्नेह से पहले और यवागू से पहले पढ़ता है; यह व्याख्या है।"),
    "hook": "पीने से पहले, दोनों बार, गरम पानी से परिषेक।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 120, with what is the sprinkling (परिषेचन) done?",
            ("With hot water (उष्णोदक)", "उष्णोदकेन परिषेचयेत्."),
            [("With water boiled and cooled", "Cooled water is for drinking, unit 122."),
             ("With balā oil (बलातैल)", "Balā oil is for anointing, unit 115."),
             ("With milk (क्षीर)", "Milk is a way to cook the yavāgū, unit 119.")],
            "Hot water is used for the sprinkling.",
            "उष्णोदकेन परिषेचयेत्."),
        order(1, "Put the words of unit 120 in the line's order.",
              ["प्राक्", "स्नेहयवागूपानाभ्याम्", "च", "उभयकालम्", "उष्णोदकेन", "परिषेचयेत्"],
              "Before the drinkings of sneha and yavāgū, and at both times, with hot water, one should sprinkle.",
              "प्राक् → स्नेहयवागूपानाभ्याम् → च → उभयकालम् → उष्णोदकेन → परिषेचयेत्."),
        match(2, "Match each word of unit 120 to its meaning.",
              [["प्राक्", "before"], ["उभयकालम्", "at both times"], ["उष्ण", "hot"], ["उदक", "water"],
               ["परिषेचयेत्", "should sprinkle, bathe"]],
              "When, how often, with what, and the action.",
              "प्राक्, उभयकालम्, उष्ण, उदक, परिषेचयेत्.", role="extend",
              teaches="प्राक् (before) takes the ablative: प्राक् स्नेहयवागूपानाभ्याम् = before the drinkings of sneha and yavāgū."),
        mcq("discriminate", 3, "Which split of उष्णोदकेन is right?",
            ("उष्ण + उदकेन", "अ + उ → ओ: उष्ण + उदकेन = उष्णोदकेन (with hot water)."),
            [("उष्णः + उदकेन", "अः before उ loses the visarga and leaves a gap: उष्ण उदकेन."),
             ("उष्णम् + उदकेन", "A final म् would give उष्णमुदकेन."),
             ("उष्णो + दकेन", "दकेन is not a word; the word is उदकेन, with water.")],
            "उष्ण (hot) + उदकेन (with water): अ + उ → ओ.",
            "अ + उ → ओ."),
        mcq("apply", 4, "By unit 120, when is the hot-water sprinkling done, relative to the drinks?",
            ("Before drinking the sneha and the yavāgū", "प्राक् = before."),
            [("After drinking the sneha and the yavāgū", "प्राक् means before, not after."),
             ("While she drinks the sneha and the yavāgū", "प्राक् means before, not during."),
             ("In place of the sneha and the yavāgū", "The sprinkling is added, not a substitute.")],
            "प्राक् places the sprinkling before both drinks.",
            "प्राक् + ablative = before."),
        mcq("transfer", 5, "By the rule of चोभयकालम्, how is च + उक्तम् (and said, a new example) joined?",
            ("चोक्तम्", "अ + उ → ओ, as च + उभयकालम् → चोभयकालम्."),
            [("चौक्तम्", "अ + उ gives ओ, not औ."),
             ("चुक्तम्", "The अ does not drop before उ."),
             ("चवुक्तम्", "No व is put between अ and उ.")],
            "च + उक्तम् = चोक्तम्, like च + उभयकालम्.",
            "अ + उ → ओ.",
            teaches="A final अ before उ merges into ओ: च + उभयकालम् → चोभयकालम्."),
    ],
}

# ---------------------------------------------------------------- unit 121
AUTHORED["121"] = {
    "title": "एवं त्रिरात्रंपंचरात्रं ... क्रमादाप्यायेत्",
    "question": "By unit 121, after the first nights, how is the sūtikā gradually nourished?",
    "rule": ("After keeping this up three or five nights, nourish her gradually (क्रमात्) with a soup of barley, jujube "
             "and horse gram and light food and drink; after twelve nights with jāṅgala broths; regarding agni, strength "
             "and so on."),
    "limits": ("Low confidence. The third period, printed समरात्रं, is unclear (perhaps seven nights: not adopted); "
               "no question on it. jāṅgala = flesh of dry-land animals (standard). Who is nourished is not printed."),
    "explain_hi": ("इस प्रकार तीन रात या पाँच रात (या एक अस्पष्ट अवधि ‘समरात्र’) यह क्रम निभाकर, फिर यव, कोल (बेर) और कुलत्थ "
                   "(कुलथी) के यूष से और हल्के अन्न-पान से, और बारह रात के बाद जाङ्गल (सूखे प्रदेश के पशुओं के मांस) के रस "
                   "आदि से, धीरे-धीरे (क्रमात्) पोषण करना चाहिए। "
                   "यह सब अग्नि, बल आदि को देखकर (अपेक्ष्य) हो। "
                   "‘समरात्र’ का अर्थ अस्पष्ट है (शायद सात रात, पर यह पाठ अपनाया नहीं गया), इस पर प्रश्न नहीं।"),
    "hook": "पहले यव-कोल-कुलत्थ का यूष, बारह रात बाद जाङ्गल रस; अग्नि-बल देखकर।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 121, from when are jāṅgala broths given?",
            ("After twelve nights", "द्वादशरात्रात्परं जाङ्गलरसादिभिः."),
            [("After three nights", "Three or five nights is the first stage, before the soup."),
             ("From the first day", "Broths come later, after twelve nights."),
             ("After a month and a half", "One and a half months ends the period, unit 125.")],
            "Jāṅgala broths come after twelve nights.",
            "द्वादशरात्रात् परम् = after twelve nights."),
        order(1, "Put these parts of unit 121 in the line's order.",
              ["त्रिरात्रं पञ्चरात्रं … अनुपाल्य", "यवकोलकुलत्थयूषेण", "लघुना चान्नपानेन",
               "द्वादशरात्रात्परम्", "जाङ्गलरसादिभिश्च", "अग्निबलादीन्यपेक्ष्य"],
              "First nights; soup; light food; after twelve nights; jāṅgala broths; having regard to agni and strength.",
              "त्रिरात्र… → यूष → अन्नपान → द्वादशरात्रात् परम् → जाङ्गलरस → अग्निबलादि."),
        match(2, "Match each food word of unit 121 to its meaning.",
              [["यव", "barley"], ["कोल", "jujube"], ["कुलत्थ", "horse gram"], ["यूष", "soup"],
               ["जाङ्गल", "of dry-land animals (their flesh)"]],
              "The soup's three items, the soup itself, and the later broth.",
              "यव, कोल, कुलत्थ, यूष, जाङ्गल.", role="extend",
              teaches="जाङ्गल = of dry-land animals; used as a noun for their flesh, whose broths (रस) come after twelve nights."),
        mcq("discriminate", 3, "By unit 121, what does the nourishing have regard to (अपेक्ष्य)?",
            ("Digestive fire, strength and so on", "अग्निबलादीन्यपेक्ष्य: having regard to agni, strength and the rest."),
            [("The season of the year and the hour", "No season or hour is named in unit 121."),
             ("The weight and the age of the child", "The child is not named in unit 121."),
             ("Her wishes and her longings alone", "The line names agni and strength, not wishes.")],
            "Agni (digestive fire) and bala (strength) guide the feeding.",
            "अग्निबलादीनि अपेक्ष्य."),
        multi("apply", 4, "Which statements does unit 121 make?",
              [("Jāṅgala broths come before the twelfth night", "They come after twelve nights (परम्)."),
               ("The soup is of barley, jujube and horse gram", "Right: यवकोलकुलत्थयूषेण."),
               ("Light food and drink go with the soup", "Right: लघुना चान्नपानेन."),
               ("All the foods are given at once, from day one", "क्रमात्: gradually, step by step.")],
              [1, 2],
              "The soup has three items and goes with light food; broths come later, gradually.",
              "यवकोलकुलत्थयूषेण लघुना चान्नपानेन ... क्रमात्."),
        mcq("transfer", 5, "By the rule of ततो यव..., how is रामः + गच्छति (Rāma goes, a new example) joined?",
            ("रामो गच्छति", "अः before a voiced sound becomes ओ, as ततः + यव… → ततो यव…."),
            [("रामर्गच्छति", "र् comes from a visarga after vowels other than अ/आ."),
             ("रामा गच्छति", "The visarga of आः drops; this is अः, which becomes ओ."),
             ("रामस् गच्छति", "स् stays only before त/थ, not before ग.")],
            "रामः + गच्छति = रामो गच्छति, like ततः + यव… = ततो यव….",
            "अः + voiced sound → ओ.",
            teaches="अः before a voiced consonant becomes ओ: ततः + यवकोल… → ततो यवकोल…."),
    ],
}

# ---------------------------------------------------------------- unit 122
AUTHORED["122"] = {
    "title": "कथितशीतं च तोयं पाययेत्",
    "question": "By unit 122, what water is given to drink?",
    "rule": ("Water (तोय) that has been boiled and cooled (शीत) should be given to drink. पाययेत् is causative: should "
             "make (her) drink."),
    "limits": ("Printed कथित (said) is read as क्वथित (boiled) from the sense; 'boiled' rests on that reading, so no "
               "question turns on it. Who drinks is not printed."),
    "explain_hi": ("और उबालकर ठण्डा किया हुआ पानी (तोय) पिलाना चाहिए। "
                   "छपा ‘कथित’ का अर्थ ‘कहा हुआ’ होता, जो यहाँ नहीं बैठता; इसलिए इसे ‘क्वथित’ (उबला) पढ़ा गया है, यह अर्थ पर आधारित है। "
                   "‘शीत’ = ठण्डा, यह निश्चित है। "
                   "‘पाययेत्’ प्रेरणार्थक (णिजन्त) है: स्वयं पीना नहीं, ‘पिलाए’। "
                   "किसे पिलाना है, यह नहीं छपा; क्रम से सूतिका।"),
    "hook": "उबला, फिर ठण्डा: ऐसा तोय पिलाएँ।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 122, what kind of water is given to drink?",
            ("Water that has been cooled", "कथितशीतं ... तोयम्: शीत = cooled."),
            [("Water that is still hot", "Hot water is for sprinkling, unit 120."),
             ("Water mixed with milk, served warm", "No milk is named in unit 122."),
             ("Water mixed with broth", "Broths are unit 121, not water here.")],
            "The drinking water is cooled.",
            "शीतं तोयं पाययेत्."),
        match(1, "Match each word of unit 122 to its meaning.",
              [["शीतम्", "cooled"], ["तोयम्", "water"], ["पाययेत्", "should make (her) drink"], ["च", "and"]],
              "Four sure words of the short line.",
              "शीतम्, तोयम्, पाययेत्, च."),
        mcq("extend", 2, "What does the causative पाययेत् mean, beside पिबेत् (should drink)?",
            ("Should make one drink", "The causative of पा: to make drink, to give to drink."),
            [("Should drink it oneself", "That is the plain पिबेत्."),
             ("Has already drunk it", "That would be a past form such as पीतवती."),
             ("Will drink it later on", "The optative is not a future.")],
            "पाययेत् = should give to drink.",
            "पिबति drinks; पाययति makes drink.",
            teaches="पाययेत् is the causative optative of पा: should make (her) drink, not drink oneself."),
        mcq("discriminate", 3, "How is शीतम् + च written, as in the print of unit 122?",
            ("शीतं च", "A final म् before a consonant is written as anusvāra: शीतं च."),
            [("शीतश्च", "श्च comes from a visarga before च; here the ending is म्."),
             ("शीत च", "The म् is not lost; it becomes anusvāra."),
             ("शीतो च", "ओ comes from अः, and there is no visarga here.")],
            "शीतम् + च → शीतं च.",
            "Final म् before a consonant → anusvāra."),
        fill(4, "In unit 122, the word for water is ____ (type it in Devanagari or in English letters, e.g. dharma).",
             accepts("तोयम्", None, "तोय"),
             "तोयम् = water (n. acc. sg.), the object of पाययेत्.",
             "तोय = water.",
             "तोय = water.", role="apply"),
        mcq("transfer", 5, "By the causative of पाययेत्, what does कारयेत् (from कृ, do) mean?",
            ("Should cause one to do", "The causative makes 'cause to do', as पाययेत् = make drink."),
            [("Should do it all oneself", "That is the plain कुर्यात्."),
             ("Was done by someone", "कारयेत् is not a past passive form."),
             ("Will do in the future", "The optative is not a future.")],
            "कारयेत् = should cause to do, like पाययेत् = should make drink.",
            "Causative = cause someone to act.",
            teaches="A causative makes the verb 'cause to ...': पा → पाययेत् (make drink); कृ → कारयेत् (cause to do)."),
    ],
}

# ---------------------------------------------------------------- unit 123
AUTHORED["123"] = {
    "title": "तथा जीवनीयबृंहणीय... उपाचरेत्",
    "question": "By unit 123, with what preparations and means is she attended to?",
    "rule": ("Likewise attend (उपाचरेत्) with preparations cooked with life-promoting (jīvanīya), nourishing (bṛṃhaṇīya), "
             "sweet and vāta-relieving drugs, through anointing, ucchādana (unclear), sprinkling and immersion, and with agreeable foods and drinks."),
    "limits": ("Low confidence. उच्छादन is unclear (utsādana is a guess); printed ह्रद्य is read हृद्य. No question on either. "
               "jīvanīya and bṛṃhaṇīya are named drug groups (standard). Who is attended is not printed."),
    "explain_hi": ("इसी प्रकार जीवनीय, बृंहणीय (पोषक), मधुर और वातहर द्रव्यों से सिद्ध किए हुए (पदार्थों; कौन-से, यह नहीं कहा) से अभ्यंग, उच्छादन "
                   "(अस्पष्ट शब्द), परिषेक और अवगाह द्वारा, और हृदय को प्रिय (हृद्य) अन्न-पान से उपचार करना चाहिए। "
                   "जीवनीय और बृंहणीय औषधियों के नामित गण हैं (मानक)। "
                   "‘उच्छादन’ और छपा ‘ह्रद्य’ अनिश्चित हैं, इन पर प्रश्न नहीं। "
                   "छपाई के अन्तराल के आर-पार सन्धि है: अवगाहैः + अन्नपानैः → अवगाहैरन्नपानैः।"),
    "hook": "जीवनीय-बृंहणीय-मधुर-वातहर से सिद्ध: अभ्यंग, परिषेक, अवगाह, और प्रिय अन्न-पान।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 123, with which drugs are the preparations cooked (सिद्ध)?",
            ("Life-promoting, nourishing, sweet, vāta-relieving ones", "जीवनीयबृंहणीयमधुरवातहरसिद्धैः."),
            [("Pungent, drying, bitter and strongly vāta-raising ones", "The line names sweet and vāta-relieving drugs."),
             ("Purging, emetic, sour and kapha-raising ones", "None of these is named in unit 123."),
             ("Cooling, astringent, salty and pitta-raising ones", "None of these is named in unit 123.")],
            "Four qualities: jīvanīya, bṛṃhaṇīya, madhura, vātahara.",
            "जीवनीय-बृंहणीय-मधुर-वातहर-सिद्ध."),
        order(1, "Put the four drug qualities of unit 123 in the line's order.",
              ["जीवनीय", "बृंहणीय", "मधुर", "वातहर"],
              "Life-promoting, nourishing, sweet, vāta-relieving, then सिद्ध (cooked).",
              "जीवनीय → बृंहणीय → मधुर → वातहर."),
        match(2, "Match each word of unit 123 to its meaning.",
              [["अभ्यङ्ग", "anointing"], ["परिषेक", "sprinkling"], ["अवगाह", "immersion"],
               ["अन्नपान", "food and drink"], ["उपाचरेत्", "should attend, treat"]],
              "The sure means of care, the diet, and the verb.",
              "अभ्यङ्ग, परिषेक, अवगाह, अन्नपान, उपाचरेत्.", role="extend",
              teaches="अन्नपान is a dvandva, food and drink; here plural (अन्नपानैः) with हृद्य, agreeable."),
        mcq("discriminate", 3, "The print shows अवगाहै रन्नपानैश्च; which split is right?",
            ("अवगाहैः + अन्नपानैः + च", "ऐः before a vowel: the visarga becomes र्, printed across the gap."),
            [("अवगाहै + रन्नपानैः + च", "रन्नपान is not a word; the र् is the visarga of अवगाहैः."),
             ("अवगाहे + अन्नपानैः + च", "ए before अ would give अवगाहेऽन्नपानैः, with no र्."),
             ("अवगाह + अन्नपानैः + च", "अ + अ would give आ: अवगाहान्नपानैः.")],
            "अवगाहैः + अन्नपानैः: the visarga after ऐ becomes र् before a vowel.",
            "Visarga after a vowel other than अ/आ → र् before a vowel or voiced sound."),
        multi("apply", 4, "Which means of care does unit 123 name?",
              [("Anointing (अभ्यङ्ग)", "Right: अभ्यंग… in the compound."),
               ("Purging (विरेचन)", "No purging is named in unit 123."),
               ("Immersion (अवगाह)", "Right: …परिषेकावगाहैः."),
               ("Fasting (लङ्घन)", "No fasting is named; agreeable food is given.")],
              [0, 2],
              "Anointing, sprinkling and immersion are named; purging and fasting are not.",
              "अभ्यंग… परिषेक… अवगाहैः."),
        mcq("transfer", 5, "By the rule of अवगाहैरन्नपानैः, how is देवैः + अपि (by the gods too, a new example) joined?",
            ("देवैरपि", "Visarga after ऐ becomes र् before a vowel, as अवगाहैः + अन्नपानैः."),
            [("देवोऽपि", "ओऽ comes from अः + अ; here the vowel is ऐ."),
             ("देवैपि", "The visarga is not lost and the vowels do not merge."),
             ("देवैसपि", "Before a vowel the visarga becomes र्, not स्.")],
            "देवैः + अपि = देवैरपि, like अवगाहैः + अन्नपानैः.",
            "ऐः + vowel → ऐर्.",
            teaches="A visarga after a vowel other than अ/आ becomes र् before a vowel: अवगाहैः + अन्नपानैः → अवगाहैरन्नपानैः."),
    ],
}

# ---------------------------------------------------------------- unit 124
AUTHORED["124"] = {
    "title": "एवं हि ... पुनर्नवीभवति",
    "question": "By unit 124, why is the sūtikā's disease hard to cure, and how should she be treated?",
    "rule": ("Thus, from a depleted body, she becomes new again (पुनर्नवीभवति); for this very reason the sūtikā's disease is "
             "hard to cure (कृच्छ्रसाध्य) or incurable (असाध्य). Therefore treat her with effort by the stated procedure."),
    "limits": ("Low confidence. The long compound (body wasted by the foetus's growth, emptied of pain, moisture, blood) is a "
               "conjectural division; प्रवाहुण is unclear. No question rests on it. The disease is not named."),
    "explain_hi": ("क्योंकि इस प्रकार (अनुमानित पाठ पर) गर्भ-वृद्धि से क्षीण और शिथिल धातुओं वाले, तथा वेदना, क्लेद और रक्त-स्राव "
                   "आदि से रिक्त शरीर से वह फिर नई हो जाती है (पुनर्नवीभवति)। "
                   "इसी कारण (अत एव) सूतिका का रोग कष्टसाध्य या असाध्य होता है। "
                   "इसलिए (तस्मात्) उसका यथोक्त विधि से प्रयत्नपूर्वक उपचार करना चाहिए। "
                   "लम्बे समास का विभाग अनुमानित है और ‘प्रवाहुण’ अस्पष्ट है; उस पर प्रश्न नहीं। रोग का नाम नहीं दिया गया।"),
    "hook": "शरीर फिर नया बनता है, इसलिए सूतिका-रोग कठिन: यत्न से विधिपूर्वक उपचार।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 124, what is the sūtikā's disease said to be?",
            ("Hard to cure, or incurable", "कृच्छ्रसाध्यो भवत्यसाध्यो वा."),
            [("Easy to cure, in a few days", "The line says the opposite: hard to cure."),
             ("Mild, passing off by itself", "The line says hard to cure or incurable."),
             ("Cured by fasting, nothing else", "No fasting is named; careful treatment is.")],
            "Her disease is hard to cure or incurable.",
            "सूतिकाया व्याधिः कृच्छ्रसाध्यो भवत्यसाध्यो वा."),
        order(1, "Put these parts of unit 124 in the line's order.",
              ["एवं हि … पुनर्नवीभवति", "अत एव च", "सूतिकाया व्याधिः", "कृच्छ्रसाध्यो भवत्यसाध्यो वा",
               "तस्मात्तां यथोक्तेन विधिना", "प्रयत्नेनोपचरेत्"],
              "She becomes new again; for that reason her disease is hard or incurable; so treat her with effort.",
              "पुनर्नवीभवति → अत एव → व्याधिः → कृच्छ्रसाध्यः/असाध्यः → तस्मात् → उपचरेत्."),
        match(2, "Match each word of unit 124 to its meaning.",
              [["पुनर्नवीभवति", "becomes new again"], ["कृच्छ्रसाध्य", "hard to cure"], ["असाध्य", "incurable"],
               ["यथोक्तेन विधिना", "by the procedure as stated"], ["प्रयत्नेन", "with effort"]],
              "The sure words of the second and third sentences.",
              "पुनर्नवीभवति, कृच्छ्रसाध्य, असाध्य, यथोक्तेन विधिना, प्रयत्नेन.", role="extend",
              teaches="नवी + भवति (the ई before भू): becomes new, what it was not; पुनः adds 'again'."),
        mcq("discriminate", 3, "In unit 124, what is the reason behind तस्मात् (therefore)?",
            ("Her disease is hard to cure or incurable", "That sentence comes just before तस्मात्."),
            [("She is hungry and needs sneha", "Hunger is unit 116."),
             ("The wind has no space in her belly", "That is unit 118."),
             ("Her menses have appeared again", "That is a view in unit 126.")],
            "Because her disease is hard to cure, she must be treated with effort.",
            "... असाध्यो वा, तस्मात् ... प्रयत्नेनोपचरेत्."),
        mcq("apply", 4, "Which split of भवत्यसाध्यो is right?",
            ("भवति + असाध्यः", "इ + अ → य: भवति + असाध्यः → भवत्यसाध्यः (becomes incurable)."),
            [("भवत् + असाध्यः", "A final त् would give भवदसाध्यः."),
             ("भवति + साध्यः", "There is no vowel to join: it would stay भवति साध्यः."),
             ("भवत्य + साध्यः", "भवत्य is not a word; the verb is भवति.")],
            "भवति (becomes) + असाध्यः (incurable): इ + अ → य.",
            "इ + a different vowel → य्."),
        mcq("transfer", 5, "By the rule of भवत्यसाध्यः, how is अस्ति + अत्र (is here, a new example) joined?",
            ("अस्त्यत्र", "इ + अ → य, as भवति + असाध्यः → भवत्यसाध्यः."),
            [("अस्तेत्र", "इ + अ does not give ए."),
             ("अस्तात्र", "The इ is not dropped before अ."),
             ("अस्तीत्र", "इ + अ does not give ई.")],
            "अस्ति + अत्र = अस्त्यत्र, like भवति + असाध्यः.",
            "इ + अ → य.",
            teaches="A final इ before a different vowel becomes य्: भवति + असाध्यः → भवत्यसाध्यः."),
    ],
}

# ---------------------------------------------------------------- unit 125
AUTHORED["125"] = {
    "title": "एवं साऽध्यर्द्धमासमुपसंस्कृता",
    "question": "By unit 125, after how long and how does the woman stop being called sūtikā?",
    "rule": ("Treated thus for one and a half months (अध्यर्धमासम्) and gradually (क्रमेण) released from the restraint "
             "(यन्त्रणा) of food and conduct, she would be one from whom the name sūtikā has gone."),
    "limits": ("Printed विगंत is read विगत (gone): a correction, so no question rests on it. The compound with विमुक्त "
               "may also split as विमुक्ता + a separate word (the data notes this as possible). The next unit appears to give another view."),
    "explain_hi": ("इस प्रकार डेढ़ मास (अध्यर्धमासम्) तक उपचारित (उपसंस्कृता) होकर, और क्रम से (क्रमेण) आहार और विहार के "
                   "नियन्त्रण (यन्त्रणा) से मुक्त होकर, वह ऐसी हो जाती है कि उसका ‘सूतिका’ नाम चला जाता है। "
                   "अध्यर्ध = एक और आधा (पूरे में आधा जुड़ा)। "
                   "छपा ‘विगंत’ ‘विगत’ पढ़ा गया है, इसलिए उस पर प्रश्न नहीं। "
                   "अगली इकाई (१२६) इस अवधि पर कुछ लोगों का दूसरा मत देती प्रतीत होती है।"),
    "hook": "डेढ़ मास, धीरे-धीरे छूट: फिर ‘सूतिका’ नाम नहीं।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 125, for how long is she treated as a sūtikā?",
            ("One and a half months", "अध्यर्धमासम्: for one and a half months."),
            [("Twelve nights in all", "Twelve nights marks the broths, unit 121."),
             ("Three or five nights", "That is the first stage of unit 121."),
             ("Exactly one month, no more", "अध्यर्ध is one and a half, not one.")],
            "The period is one and a half months.",
            "अध्यर्धमासम् उपसंस्कृता."),
        order(1, "Put these parts of unit 125 in the line's order.",
              ["एवं सा", "अध्यर्धमासम्", "उपसंस्कृता", "क्रमेण", "विमुक्त… यन्त्रणा", "…सूतिकाभिधाना स्यात्"],
              "Thus she, a month and a half, treated, gradually, released from restraint, would lose the name sūtikā.",
              "एवं सा → अध्यर्धमासम् → उपसंस्कृता → क्रमेण → विमुक्त… → …सूतिकाभिधाना स्यात्."),
        match(2, "Match each word of unit 125 to its meaning.",
              [["अध्यर्ध", "one and a half"], ["मास", "month"], ["उपसंस्कृता", "treated"], ["क्रमेण", "gradually"],
               ["यन्त्रणा", "restraint"], ["अभिधान", "name"]],
              "How long, how, from what, and what goes.",
              "अध्यर्ध, मास, उपसंस्कृता, क्रमेण, यन्त्रणा, अभिधान.", role="extend",
              teaches="अध्यर्ध = one and a half: a half added to a whole (अधि + अर्ध)."),
        mcq("discriminate", 3, "By unit 125, from what is she gradually released?",
            ("The restraint of food and conduct", "आहारविहारयन्त्रणा: restraint of food (आहार) and conduct (विहार)."),
            [("The care of the newborn child", "No child is named in unit 125."),
             ("The rule of daily oil massage", "Massage is not named in unit 125."),
             ("The house set apart for delivery", "No house is named in unit 125.")],
            "आहार = food, विहार = conduct; यन्त्रणा = restraint.",
            "विमुक्त-आहार-विहार-यन्त्रणा."),
        mcq("apply", 4, "Which split of साऽध्यर्द्धमासम् is right?",
            ("सा + अध्यर्धमासम्", "आ + अ → आ; the ऽ marks the merged अ, as printed."),
            [("सः + अध्यर्धमासम्", "सः before अ would give सोऽध्यर्ध…, and the subject is feminine."),
             ("सा + ध्यर्धमासम्", "ध्यर्ध is not a word; the word is अध्यर्ध."),
             ("सा + आध्यर्धमासम्", "आध्यर्ध is not a word; the word is अध्यर्ध.")],
            "सा (she) + अध्यर्धमासम् (one and a half months).",
            "आ + अ → आ."),
        mcq("transfer", 5, "By the rule of साऽध्यर्ध…, how is सा + अपि (she too, a new example) joined?",
            ("सापि", "आ + अ → आ, as सा + अध्यर्ध… → साऽध्यर्ध…."),
            [("सोऽपि", "That is सः + अपि, the masculine."),
             ("सेपि", "आ + अ does not give ए."),
             ("सायपि", "No य is put between आ and अ.")],
            "सा + अपि = सापि (also printed साऽपि).",
            "आ + अ → आ.",
            teaches="A final आ before अ merges into आ: सा + अध्यर्धमासम् → साऽध्यर्धमासम्."),
    ],
}

# ---------------------------------------------------------------- unit 126
AUTHORED["126"] = {
    "title": "पुनरार्त्तवदर्शनादित्येके",
    "question": "By unit 126, what do some take as the end of the sūtikā period?",
    "rule": ("Some (एके) say: from the reappearance (पुनः दर्शन) of ārtava (menses). इति एके = so some (say), a view set "
             "beside another."),
    "limits": ("The verb 'say' is not printed. The ablative may mean 'after' or 'at the time of' the reappearance. That "
               "it continues unit 125 as a variant view is the data's reading."),
    "explain_hi": ("कुछ लोगों (एके) का मत है: आर्तव (रज) के फिर दिखने से (पुनरार्तवदर्शनात्)। "
                   "‘इति एके’ = ऐसा कुछ कहते हैं; ‘कहते हैं’ छपा नहीं है। "
                   "यह इकाई १२५ के डेढ़ मास वाले कथन के बाद एक दूसरा मत प्रतीत होती है (डेटा का पाठ)। "
                   "पञ्चमी का अर्थ ‘के बाद’ या ‘के समय’ दोनों हो सकता है। "
                   "छपा ‘आर्त्तव’ (दो त) ‘आर्तव’ पढ़ा गया है।"),
    "hook": "कुछ कहते हैं: रज फिर दिखे, तब।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 126, what event do some (एके) name?",
            ("The reappearance of the menses", "पुनरार्तवदर्शनात्: from the menses appearing again."),
            [("The passing of twelve nights", "Twelve nights belongs to unit 121."),
             ("The child's first full month", "No child's month is named in unit 126."),
             ("The first full bath in hot water", "Hot water is unit 120.")],
            "Some mark it by the menses appearing again.",
            "पुनरार्तवदर्शनात् इति एके."),
        order(1, "Put the words of unit 126 in the line's order.",
              ["पुनः", "आर्तवदर्शनात्", "इति", "एके"],
              "Again, from the appearance of the menses, thus, some.",
              "पुनः → आर्तवदर्शनात् → इति → एके."),
        match(2, "Match each word of unit 126 to its meaning.",
              [["पुनः", "again"], ["आर्तव", "menses"], ["दर्शन", "appearance"], ["एके", "some (people)"]],
              "Four words make the whole view.",
              "पुनः, आर्तव, दर्शन, एके.", role="extend",
              teaches="इति एके = so some (say): it marks a view held by some, set beside another."),
        mcq("discriminate", 3, "Which split of पुनरार्त्तव… (पुनरार्तव) is right?",
            ("पुनः + आर्तव", "The visarga after उ becomes र् before a vowel."),
            [("पुनर + आर्तव", "पुनर is not a word; the word is पुनः."),
             ("पुनः + अर्तव", "अर्तव is not a word, and र् + अ would give पुनरर्तव."),
             ("पुनरा + र्तव", "पुनरा and र्तव are not words.")],
            "पुनः (again) + आर्तव (menses): उः + vowel → उर्.",
            "Visarga after उ → र् before a vowel."),
        mcq("apply", 4, "By unit 126, whose view is this?",
            ("A view held by some", "इति एके: so some (say)."),
            [("The only view the text allows", "It is a view of some, beside another account."),
             ("The view of all teachers", "एके means some, not all."),
             ("The sūtikā's own view", "एके is masculine plural: some (people), not the woman.")],
            "एके marks a view held by some.",
            "इति एके = so some (say)."),
        mcq("transfer", 5, "By the rule of इत्येके, how is इति + एव (thus indeed, a new example) joined?",
            ("इत्येव", "इ + ए → ये, as इति + एके → इत्येके."),
            [("इतेव", "The इ does not drop before ए."),
             ("इत्यैव", "इ + ए gives ये, not यै."),
             ("इतैव", "इ + ए does not give ऐ.")],
            "इति + एव = इत्येव, like इति + एके.",
            "इ + ए → ये.",
            teaches="A final इ before ए becomes य्: इति + एके → इत्येके."),
    ],
}

# ---------------------------------------------------------------- unit 127
AUTHORED["127"] = {
    "title": "इत्याद्यं मासमादाय",
    "question": "By unit 127, over what span has the whole procedure been shown?",
    "rule": ("Taking the first month (as the start), as long as (यावत्) the woman would again be capable of a foetus, so "
             "long (तावत्) the whole procedure (विधिः सर्वः) has been shown well in every way. यावत् ... तावत् are correlatives."),
    "limits": ("A verse of two printed lines read as one sentence (the data's grouping); the data translation keeps the lines "
               "apart. 'From the first month onward' is the sense of आदाय, not printed. The verse names no procedure."),
    "explain_hi": ("इस प्रकार प्रथम मास को (आरम्भ) लेकर (आदाय), जब तक (यावत्) स्त्री फिर से गर्भ के योग्य (गर्भक्षमा) हो, तब तक "
                   "(तावत्) की सारी विधि सब प्रकार से भली भाँति दिखा दी गई है। "
                   "‘यावत् ... तावत्’ जोड़ी है: जब तक ... तब तक। "
                   "डेटा दोनों छपी पंक्तियों को एक वाक्य मानता है, अनुवाद उन्हें अलग रखता है। "
                   "यह श्लोक (अनुष्टुभ्) कहता है कि सारी विधि भली भाँति दिखा दी गई है।"),
    "hook": "पहले मास से, फिर गर्भ-योग्य होने तक: सारी विधि भली भाँति दिखाई गई।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 127, what has been shown well in every way?",
            ("The whole procedure", "विधिः सर्वः सर्वथा साधु दर्शितः."),
            [("The whole list of her possible diseases", "No diseases are listed in unit 127."),
             ("The signs of a male child", "Those signs are not in unit 127."),
             ("The full set of mantras", "No mantras are named in unit 127.")],
            "The verse closes: the whole procedure has been shown.",
            "विधिः सर्वः सर्वथा साधु दर्शितः."),
        order(1, "Put the phrases of unit 127 in the verse's order.",
              ["इत्याद्यं मासमादाय", "यावद्गर्भक्षमा पुनः", "स्त्री स्यात्तावत्", "विधिः सर्वः",
               "सर्वथा साधु दर्शितः"],
              "Taking the first month, as long as again capable of a foetus the woman is, so long the whole procedure is shown.",
              "इत्याद्यं → यावद्गर्भक्षमा → स्त्री स्यात्तावत् → विधिः सर्वः → सर्वथा साधु दर्शितः."),
        match(2, "Match each word of unit 127 to its meaning.",
              [["आद्यम्", "first"], ["आदाय", "having taken"], ["गर्भक्षमा", "capable of a foetus"],
               ["सर्वथा", "in every way"], ["दर्शितः", "shown"]],
              "The span (first month to fitness for a foetus) and the closing praise.",
              "आद्यम्, आदाय, गर्भक्षमा, सर्वथा, दर्शितः.", role="extend",
              teaches="यावत् ... तावत् = as long as ... so long: the two halves of one sentence."),
        mcq("discriminate", 3, "In unit 127, which word answers यावत् (as long as)?",
            ("तावत्", "तावत् is the correlative of यावत्: so long."),
            [("पुनः", "पुनः means again, inside the यावत् clause."),
             ("सर्वथा", "सर्वथा means in every way, not so long."),
             ("इति", "इति opens the verse: thus.")],
            "यावत् ... तावत्: as long as ... so long.",
            "यावत् ↔ तावत्."),
        mcq("apply", 4, "Why is यावत् printed यावद् before गर्भक्षमा?",
            ("A final त् becomes द् before a voiced sound", "ग is voiced, so त् → द्."),
            [("Because गर्भक्षमा is feminine", "Gender does not change a final consonant."),
             ("Because the metre needs a long syllable at that place", "The change is sandhi, not metre."),
             ("Because द् marks the plural here", "यावत् is an indeclinable; it has no plural.")],
            "यावत् + गर्भक्षमा → यावद्गर्भक्षमा.",
            "Final त् → द् before a voiced sound."),
        mcq("transfer", 5, "By the rule of यावद्गर्भ…, how is जगत् + ईशः (lord of the world, a new example) joined?",
            ("जगदीशः", "त् → द् before a voiced sound (here a vowel), as यावत् + गर्भ… → यावद्गर्भ…."),
            [("जगतीशः", "Before a vowel the final त् does not stay त्."),
             ("जगन्नीशः", "त् becomes न् only before a nasal."),
             ("जगदिशः", "The ई of ईशः is not shortened.")],
            "जगत् + ईशः = जगदीशः, like यावत् + गर्भक्षमा → यावद्गर्भक्षमा.",
            "Final त् → द् before a voiced sound or a vowel.",
            teaches="A final त् becomes द् before a voiced sound: यावत् + गर्भक्षमा → यावद्गर्भक्षमा; तावत् + विधिः → तावद्विधिः."),
    ],
}

# ---------------------------------------------------------------- unit 128
AUTHORED["128"] = {
    "title": "इति गर्भोपचरणीयो नाम तृतीयोऽध्यायः",
    "question": "By unit 128, what is the name of this third chapter?",
    "rule": ("The colophon: thus ends the third chapter (तृतीयः अध्यायः), named Garbhopacaraṇīya: what is to be done for "
             "(the woman with) the foetus, the care of pregnancy and its aftermath."),
    "limits": ("A colophon, not a verse. The title is kept as a name, not translated as a fixed phrase; its sense is the "
               "data's reading."),
    "explain_hi": ("यह अध्याय की समाप्ति-पंक्ति (पुष्पिका) है: ‘इस प्रकार गर्भोपचरणीय नामक तीसरा अध्याय’। "
                   "‘गर्भोपचरणीय’ = गर्भ (वाली स्त्री) के लिए जो उपचार करना है, यानी गर्भावस्था और उसके बाद की देखभाल; "
                   "इसे नाम के रूप में ही रखा गया है। "
                   "‘नाम’ अव्यय है: नामक। "
                   "‘तृतीयोऽध्यायः’ में तृतीयः + अध्यायः है (अः + अ → ओऽ)।"),
    "hook": "तीसरा अध्याय: गर्भोपचरणीय, गर्भिणी और सूतिका की देखभाल।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 128, what is this chapter named?",
            ("Garbhopacaraṇīya", "इति गर्भोपचरणीयो नाम तृतीयोऽध्यायः."),
            [("Sūtikopacaraṇīya", "Not the printed name; the name begins with garbha."),
             ("Garbhāvataraṇīya", "Not the printed name of this chapter."),
             ("Prasavopacaraṇīya", "Not the printed name of this chapter.")],
            "The third chapter is Garbhopacaraṇīya.",
            "गर्भोपचरणीयो नाम तृतीयोऽध्यायः."),
        order(1, "Put the words of unit 128 in the line's order.",
              ["इति", "गर्भोपचरणीयः", "नाम", "तृतीयः", "अध्यायः"],
              "Thus, Garbhopacaraṇīya, named, the third chapter.",
              "इति → गर्भोपचरणीयः → नाम → तृतीयः → अध्यायः."),
        match(2, "Match each word of unit 128 to its meaning.",
              [["इति", "thus (it ends)"], ["नाम", "named"], ["तृतीयः", "third"], ["अध्यायः", "chapter"]],
              "Four words frame the chapter's name.",
              "इति, नाम, तृतीयः, अध्यायः.", role="extend",
              teaches="नाम (indeclinable) = named: X नाम अध्यायः = the chapter named X."),
        mcq("discriminate", 3, "Which split of तृतीयोऽध्यायः is right?",
            ("तृतीयः + अध्यायः", "अः + अ → ओऽ: the अ is merged and marked ऽ."),
            [("तृतीयम् + अध्यायः", "A final म् would give तृतीयमध्यायः."),
             ("तृतीये + अध्यायः", "ए + अ would give तृतीयेऽध्यायः."),
             ("तृतीया + अध्यायः", "आ + अ would give तृतीयाध्यायः.")],
            "तृतीयः (third) + अध्यायः (chapter).",
            "अः + अ → ओऽ."),
        mcq("apply", 4, "By the data's note, what does the name Garbhopacaraṇīya refer to?",
            ("Care in pregnancy and after it", "The note: what is to be done for (the woman with) the foetus."),
            [("The signs that foretell death", "Not the sense given for this name."),
             ("The bones and joints of the body", "Not the sense given for this name."),
             ("The rites for begetting a son", "Not the sense given for this name.")],
            "garbha (foetus) + upacaraṇīya (to be attended to).",
            "गर्भ + उपचरणीय → गर्भोपचरणीय."),
        mcq("transfer", 5, "By the rule of तृतीयोऽध्यायः, how is प्रथमः + अध्यायः (the first chapter, a new example) joined?",
            ("प्रथमोऽध्यायः", "अः + अ → ओऽ, as तृतीयः + अध्यायः."),
            [("प्रथमेऽध्यायः", "ए comes from a different ending, not अः."),
             ("प्रथमरध्यायः", "र् comes from a visarga after vowels other than अ/आ."),
             ("प्रथमसध्यायः", "Before a vowel the visarga does not become स्.")],
            "प्रथमः + अध्यायः = प्रथमोऽध्यायः, like तृतीयः + अध्यायः.",
            "अः + अ → ओऽ.",
            teaches="अः before अ becomes ओ and the अ is marked ऽ: तृतीयः + अध्यायः → तृतीयोऽध्यायः."),
    ],
}


# ===================================================================== NOTES_HI
NOTES_HI = {
    "116": ("गद्य; विश्वास मध्यम। पाठ-चिह्न: छपा ‘चपंचकोलचूर्णेन’ = च पञ्चकोलचूर्णेन (बिना अन्तराल)। आरम्भ का ‘च’ इसे इकाई ११५ से "
            "जोड़ता है। ‘वा’ दोनों चूर्णों के बीच है। ‘अहःपरिणामिनी’ = दिन में पचने वाली; ‘दिन के अन्त तक पचे’ मानक व्याख्या, कथन नहीं। "
            "पहचान: यवानी = अजवायन (मानक); उपकुञ्चिका = सम्भवतः कलौंजी (विवादित); सैन्धव = सेंधा नमक (मानक); व्योष = तीन कटु। "
            "सन्धि जाँची: यवानी + उपकुञ्चिका → यवान्युपकुञ्चिका (ई + उ → यु); युक्ताम् + अहः → युक्तामहः।"),
    "117": ("गद्य; विश्वास मध्यम। पाठ-चिह्न: ‘वातहरौषधकथं’ और ‘=ह्रस्वपंचमूलकथं’ में ‘कथ’ को ‘क्वाथ’ पढ़ा गया (छपाई की आदत, "
            "निश्चित नहीं); दूसरे शब्द से पहले भटका ‘=’ चिह्न। पहले खण्ड की क्रिया इकाई ११६ (पाययेत्) से समझी जाती है। "
            "यमक = सम्भवतः तेल-घी का मिश्रण (सम्भावित)। ह्रस्व पञ्चमूल के पाँच नाम डेटा के अनुवाद में हैं, पाठ में नहीं। "
            "सन्धि जाँची: स्नेह + अयोग्याम् → स्नेहायोग्याम् (अ + अ → आ); वातहर + औषध → वातहरौषध (अ + औ → औ); "
            "पीतवत्याः + च → पीतवत्याश्च; यमकेन + अभ्यज्य → यमकेनाभ्यज्य; वेष्टयेत् + उदरम् → वेष्टयेदुदरम्।"),
    "118": ("गद्य; विश्वास मध्यम। पाठ-चिह्न: छपा ‘विक्कृति’ (क दो बार), ‘विकृति’ पढ़ा गया। उदर = पेट, उदर-रोग नहीं। "
            "विधिलिङ् ‘उत्पादयेत्’ सम्भावना के अर्थ में (‘करेगी नहीं’)। ‘तथा’ किस बात की ओर, पंक्ति नहीं कहती। "
            "सन्धि जाँची: वायुः + उदर → वायुरुदर (उ के बाद विसर्ग → र् स्वर से पहले); उत्पादयेत् + अनवकाशत्वात् → "
            "उत्पादयेदनवकाशत्वात् (त् → द् स्वर से पहले); अन् + अवकाश → अनवकाश।"),
    "119": ("गद्य; विश्वास मध्यम। पाठ-चिह्न: छपा ‘विदार्यादिगणकथाथेन’ में ‘कथाथ’ को ‘क्वाथ’ पढ़ा गया (निश्चित नहीं)। "
            "‘सिद्धाम्’ तीनों साधनों (पूर्व औषध, गण-क्वाथ, दूध) पर लागू माना गया। विदारी = सम्भवतः Pueraria tuberosa (सम्भावित)। "
            "‘मात्रया’ = उचित मात्रा में; मात्रा बताई नहीं गई। सन्धि जाँची: पूर्व + औषधैः → पूर्वौषधैः (अ + औ → औ); "
            "पूर्वौषधैः + एव → पूर्वौषधैरेव (ऐ के बाद विसर्ग → र्); विदारी + आदि → विदार्यादि (ई + आ → या)।"),
    "120": ("गद्य; विश्वास मध्यम। पाठ-चिह्न: छपा ‘पानभ्यां’ = पानाभ्याम् (आ की जगह अ छपा)। ‘प्राक्’ के साथ पञ्चमी। "
            "किसे सींचना, नहीं लिखा। ‘उभयकालम्’ को स्नेह से पहले और यवागू से पहले पढ़ा गया (व्याख्या)। "
            "सन्धि जाँची: च + उभयकालम् → चोभयकालम् (अ + उ → ओ); उभयकालम् + उष्णोदकेन → उभयकालमुष्णोदकेन; "
            "उष्ण + उदकेन → उष्णोदकेन (अ + उ → ओ)।"),
    "121": ("गद्य; विश्वास निम्न। पाठ-चिह्न: ‘समरात्रं’ अस्पष्ट (शायद सप्तरात्रं; अपनाया नहीं), इस पर प्रश्न नहीं; "
            "‘त्रिरात्रंपंचरात्रं’ बिना अन्तराल। ‘वाऽनुपाल्य’ की सन्धि छपे अनुसार। ‘आप्यायेत्’ का कर्म नहीं छपा। "
            "जाङ्गल = सूखे प्रदेश के पशुओं का मांस (मानक)। सन्धि जाँची: ततः + यव… → ततो यव… (अः → ओ घोष से पहले); "
            "लघुना + च → लघुना च, च + अन्नपानेन → चान्नपानेन (अ + अ → आ); द्वादशरात्रात् + परम् → द्वादशरात्रात्परम्; "
            "जाङ्गलरसादिभिः + च → जाङ्गलरसादिभिश्च; अग्निबलादीनि + अपेक्ष्य → अग्निबलादीन्यपेक्ष्य (इ + अ → य)।"),
    "122": ("गद्य; विश्वास मध्यम। पाठ-चिह्न: छपा ‘कथित’ (कहा हुआ) को अर्थ के आधार पर ‘क्वथित’ (उबला) पढ़ा गया, इसलिए "
            "‘उबला’ पर प्रश्न नहीं। किसे पिलाना, नहीं छपा। सन्धि जाँची: शीतम् + च → शीतं च (म् → अनुस्वार व्यंजन से पहले); "
            "तोयम् + पाययेत् → तोयं पाययेत्।"),
    "123": ("गद्य; विश्वास निम्न। पाठ-चिह्न: ‘उच्छादन’ स्पष्ट शब्द नहीं (‘उत्सादन’ केवल अनुमान); छपा ‘ह्रद्यै’ = हृद्यैः। "
            "इन दोनों पर प्रश्न नहीं। जीवनीय और बृंहणीय औषधियों के नामित गण (मानक)। ‘सिद्धैः’ पूरे समास का अन्तिम पद माना गया। "
            "छपे अन्तराल के आर-पार सन्धि: अवगाहैः + अन्नपानैः → अवगाहैरन्नपानैः (छपा ‘अवगाहै रन्नपानैश्च’)। "
            "अन्य सन्धि: सिद्धैः + अभ्यङ्ग → सिद्धैरभ्यङ्ग; अभ्यङ्ग + उच्छादन → अभ्यङ्गोच्छादन; परिषेक + अवगाह → परिषेकावगाह; "
            "हृद्यैः + उपाचरेत् → हृद्यैरुपाचरेत्।"),
    "124": ("गद्य; विश्वास निम्न। पाठ-चिह्न: लम्बे समास में ‘वृद्धिं’ का अनुस्वार भटका प्रतीत; ‘प्रवाहुण’ अस्पष्ट (शायद प्रवाहण, "
            "अपनाया नहीं); समास और ‘च’ बिना अन्तराल; ‘यथोक्तेनविधिना’ बिना अन्तराल। समास का विभाग अनुमानित, दूसरा अर्थ भी सम्भव "
            "(प्रवाहण, वेदना, क्लेद, रक्त-स्राव से क्षीण शरीर)। रोग का नाम नहीं। ‘पुनर्नवी’ च्वि-रूप। सन्धि जाँची: "
            "भवति + असाध्यः → भवत्यसाध्यः (इ + अ → य); कृच्छ्रसाध्यः + भवति → कृच्छ्रसाध्यो भवति (अः → ओ घोष से पहले); "
            "अतः + एव → अत एव (छपा ‘अतएव’); तस्मात् + ताम् → तस्मात्ताम्; प्रयत्नेन + उपचरेत् → प्रयत्नेनोपचरेत् (अ + उ → ओ)।"),
    "125": ("गद्य; विश्वास मध्यम। पाठ-चिह्न: छपा ‘विगंत’ = विगत (अनुस्वार भटका, अर्थ से); ‘क्रमेणविमुक्तआहार…’ बिना अन्तराल, "
            "‘विमुक्तआहार’ में असामान्य स्वर-विराम; दूसरा विभाग ‘विमुक्ता + आहारविहारयन्त्रणात्’ केवल अनुमान। छपा ‘अध्यर्द्ध’ = "
            "अध्यर्ध, ‘यंत्रणा’ = यन्त्रणा। सन्धि जाँची: सा + अध्यर्ध → साऽध्यर्ध (आ + अ → आ, ऽ मिले अ का चिह्न); "
            "अध्यर्धमासम् + उपसंस्कृता → अध्यर्धमासमुपसंस्कृता।"),
    "126": ("गद्य; विश्वास मध्यम; कोई पाठ-चिह्न नहीं। छपा ‘आर्त्तव’ = आर्तव। ‘कहते हैं’ क्रिया छपी नहीं। पञ्चमी ‘के बाद’ या ‘के समय’ "
            "दोनों हो सकती है। इकाई १२५ के बाद दूसरा मत प्रतीत (डेटा का पाठ)। सन्धि जाँची: पुनः + आर्तव → पुनरार्तव (उ के बाद "
            "विसर्ग → र् स्वर से पहले); आर्तवदर्शनात् + इति → आर्तवदर्शनादिति (त् → द् स्वर से पहले); इति + एके → इत्येके (इ + ए → ये)।"),
    "127": ("श्लोक (अनुष्टुभ्); विश्वास मध्यम; कोई पाठ-चिह्न नहीं। दो छपी पंक्तियाँ (१३६, १३७) एक वाक्य मानी गईं: ‘यावत्’ का "
            "उत्तर ‘तावत्’। डेटा का अनुवाद पंक्तियों को अलग रखता है (‘स्त्री हो; तब तक …’), जो इस वाक्य-योजना से कुछ अटपटा है। "
            "‘आदाय’ = (आरम्भ) लेकर। सन्धि जाँची: इति + आद्यम् → इत्याद्यम् (इ + आ → या); मासम् + आदाय → मासमादाय; "
            "यावत् + गर्भ → यावद्गर्भ; स्यात् + तावत् → स्यात्तावत्; तावत् + विधिः → तावद्विधिः (त् → द् घोष से पहले)।"),
    "128": ("पुष्पिका; विश्वास उच्च; कोई पाठ-चिह्न नहीं। ‘गर्भोपचरणीय’ नाम के रूप में रखा गया। छपा ‘नामतृतीयोऽध्यायः’ = नाम + "
            "तृतीयः + अध्यायः (बिना अन्तराल)। सन्धि जाँची: गर्भ + उपचरणीयः → गर्भोपचरणीयः (अ + उ → ओ); गर्भोपचरणीयः + नाम → "
            "गर्भोपचरणीयो नाम (अः → ओ घोष से पहले); तृतीयः + अध्यायः → तृतीयोऽध्यायः (अः + अ → ओऽ)।"),
}

# ===================================================================== AIDS
AIDS = {
    "116": {
        "diagram": {"groups": [
            {"label": "पहला चूर्ण", "items": ["पञ्चकोल"]},
            {"label": "या दूसरा चूर्ण (क्रम से)", "items": ["यवानी (अजवायन, मानक)", "उपकुञ्चिका (सम्भवतः कलौंजी, विवादित)",
                                                     "चव्य", "चित्रक", "व्योष (तीन कटु)", "सैन्धव (सेंधा नमक, मानक)"]}]},
        "chunks": ("बुभुक्षितां च | पंचकोलचूर्णेन | यवान्युपकुंचिकाचव्यचित्रकव्योषसैंधवचूर्णेन वा | युक्तामहःपरिणामिनीं | "
                   "यथासात्म्यं | स्नेहमात्रां पाययेत्"),
        "frame": "किसे (बुभुक्षिताम्) → किससे युक्त (पञ्चकोल-चूर्ण या यवानी-आदि चूर्ण) → कैसी (अहःपरिणामिनी, यथासात्म्य) → क्या (स्नेहमात्रा) → क्रिया (पाययेत्)।",
        "sandhi": "ई + उ → यु: यवानी + उपकुञ्चिका → यवान्युपकुञ्चिका · म् + स्वर: युक्ताम् + अहः → युक्तामहः।",
    },
    "117": {
        "chain": {"steps": ["(१) स्नेह के अयोग्य को: वातहर औषध-क्वाथ या ह्रस्व पञ्चमूल-क्वाथ",
                            "(२) अलग खण्ड: जिसने पी लिया हो (क्या पिया, नहीं कहा)", "यमक से अभ्यंग",
                            "पेट कपड़े से लपेटना"]},
        "chunks": "स्नेहायोग्यां | वातहरौषधकथं | =ह्रस्वपंचमूलकथं वा | पीतवत्याश्च | यमकेनाभ्यज्य | वेष्टयेदुदरं वस्त्रेण",
        "sandhi": "अ + अ → आ: स्नेह + अयोग्याम् → स्नेहायोग्याम् · विसर्ग + च → श्च: पीतवत्याः + च → पीतवत्याश्च · त् → द् स्वर से पहले: वेष्टयेत् + उदरम् → वेष्टयेदुदरम्।",
        "frame": "दो खण्ड: (१) स्नेहायोग्या को क्वाथ (क्रिया ११६ से) · (२) पीतवती का अभ्यंग, फिर पेट पर कपड़ा।",
    },
    "118": {
        "chunks": "तथा न वायुः | उदरविक्कृतिम् | उत्पादयेत् | अनवकाशत्वात्",
        "sandhi": "उ के बाद विसर्ग → र् स्वर से पहले: वायुः + उदर → वायुरुदर · त् → द् स्वर से पहले: उत्पादयेत् + अनवकाशत्वात् → उत्पादयेदनवकाशत्वात्।",
        "frame": "निषेध (न) + कर्ता (वायुः) + कर्म (उदरविकृतिम्) + क्रिया (उत्पादयेत्) + कारण (अनवकाशत्वात्: पञ्चमी)।",
        "anchors": "याद-सूत्र: भरे थैले में हवा नहीं घूमती; जगह नहीं तो विकार नहीं। (मेरी याद-पद्धति, ग्रन्थ का दावा नहीं)",
    },
    "119": {
        "diagram": {"groups": [
            {"label": "कब", "items": ["स्नेह पच जाने पर"]},
            {"label": "यवागू किससे सिद्ध (कोई एक)", "items": ["वही पहले वाली औषधियाँ", "विदारी-आदि गण का क्वाथ (छपा कथाथ)", "या दूध"]},
            {"label": "यवागू कैसी", "items": ["भली प्रकार उबली", "तरल", "मात्रा से"]}]},
        "chunks": "जीर्णे तु स्नेहे | पूर्वौषधैरेव सिद्धां | विदार्यादिगणकथाथेन | क्षीरेण वा | यवागूं सुस्विन्नां द्रवां | मात्रया पाययेत्",
        "sandhi": "अ + औ → औ: पूर्व + औषधैः → पूर्वौषधैः · ऐ के बाद विसर्ग, स्वर या घोष से पहले → र्: पूर्वौषधैः + एव → पूर्वौषधैरेव · ई + आ → या: विदारी + आदि → विदार्यादि।",
    },
    "120": {
        "chunks": "प्राक् | स्नेहयवागूपानभ्यां | चोभयकालम् | उष्णोदकेन | परिषेचयेत्",
        "sandhi": "अ + उ → ओ: च + उभयकालम् → चोभयकालम्; उष्ण + उदकेन → उष्णोदकेन।",
        "frame": "कब (प्राक् + पञ्चमी: दोनों पानों से पहले) → कितनी बार (उभयकालम्) → किससे (उष्णोदकेन) → क्रिया (परिषेचयेत्)।",
    },
    "121": {
        "chain": {"steps": ["१ तीन या पाँच रात यह क्रम", "२ यव-कोल-कुलत्थ का यूष और हल्का अन्न-पान",
                            "३ बारह रात के बाद", "४ जाङ्गल रस आदि", "५ अग्नि-बल देखकर, क्रम से"]},
        "chunks": ("एवं त्रिरात्रं पंचरात्रं समरात्रं (?) वाऽनुपाल्य | ततो यवकोलकुलत्थयूषेण | लघुना चान्नपानेन | "
                   "द्वादशरात्रात्परं | जांगलरसादिभिश्च | क्रमादाप्यायेत् | अग्निबलादीन्यपेक्ष्य"),
        "sandhi": "अः → ओ घोष से पहले: ततः + यव… → ततो यव… · अ + अ → आ: च + अन्नपानेन → चान्नपानेन · इ + अ → य: अग्निबलादीनि + अपेक्ष्य → अग्निबलादीन्यपेक्ष्य।",
        "pegs": "मेरा बनाया चित्र: सीढ़ी — नीचे की पायदान पर यव-बेर-कुलथी का पतला यूष, बारहवीं पायदान पर जाङ्गल-रस का कटोरा, और सीढ़ी के पास अग्नि का दीपक। (केवल याद के लिए)",
    },
    "122": {
        "chunks": "कथितशीतं च | तोयं | पाययेत्",
        "sandhi": "म् → अनुस्वार व्यंजन से पहले: शीतम् + च → शीतं च; तोयम् + पाययेत् → तोयं पाययेत्।",
        "frame": "कर्म (तोयम्, विशेषण कथितशीतम्) + क्रिया (पाययेत्: प्रेरणार्थक, ‘पिलाए’)।",
    },
    "123": {
        "diagram": {"groups": [
            {"label": "किनसे सिद्ध (क्रम से)", "items": ["जीवनीय", "बृंहणीय", "मधुर", "वातहर"]},
            {"label": "किस साधन से (क्रम से)", "items": ["अभ्यंग", "उच्छादन (अस्पष्ट)", "परिषेक", "अवगाह"]},
            {"label": "और", "items": ["हृद्य अन्न-पान"]}]},
        "chunks": "तथा | जीवनीयबृंहणीयमधुरवातहरसिद्धैः | अभ्यंगोच्छादनपरिषेकावगाहैः | अन्नपानैश्च ह्रद्यैः (= हृद्यैः) | उपाचरेत्",
        "sandhi": "ऐ के बाद विसर्ग → र् स्वर से पहले: अवगाहैः + अन्नपानैः → अवगाहैरन्नपानैः (छपा ‘अवगाहै रन्नपानैश्च’) · अ + अ → आ: परिषेक + अवगाह → परिषेकावगाह।",
    },
    "124": {
        "chain": {"steps": ["क्षीण, रिक्त शरीर (अनुमानित पाठ)", "फिर नई हो जाती है", "इसी कारण रोग कष्टसाध्य या असाध्य",
                            "इसलिए यत्न से यथोक्त उपचार"]},
        "chunks": ("एवं हि | (लम्बा समास, अनुमानित) …शून्यशरीराच्च | पुनर्नवीभवति | अत एव च | सूतिकाया व्याधिः | "
                   "कृच्छ्रसाध्यो भवत्यसाध्यो वा | तस्मात्तां यथोक्तेन विधिना | प्रयत्नेनोपचरेत्"),
        "sandhi": "इ + अ → य: भवति + असाध्यः → भवत्यसाध्यः · अः → ओ घोष से पहले: कृच्छ्रसाध्यः + भवति → कृच्छ्रसाध्यो भवति · अ + उ → ओ: प्रयत्नेन + उपचरेत् → प्रयत्नेनोपचरेत्।",
        "frame": "हि (क्योंकि) … पुनर्नवीभवति → अत एव (इसी कारण) … असाध्यो वा → तस्मात् (इसलिए) … उपचरेत्।",
    },
    "125": {
        "chain": {"steps": ["डेढ़ मास उपचार", "क्रम से आहार-विहार की यन्त्रणा से मुक्ति", "‘सूतिका’ नाम चला गया"]},
        "chunks": "एवं सा | अध्यर्द्धमासम् | उपसंस्कृता | क्रमेण | विमुक्तआहारविहारयंत्रणा | विगंत(= विगत)सूतिकाभिधाना | स्यात्",
        "sandhi": "आ + अ → आ (ऽ): सा + अध्यर्ध → साऽध्यर्ध · म् + स्वर: अध्यर्धमासम् + उपसंस्कृता → अध्यर्धमासमुपसंस्कृता।",
        "anchors": "याद-सूत्र: अध्यर्ध = अधि (ऊपर) + अर्ध (आधा): एक पूरा और ऊपर से आधा। (मेरी याद-पद्धति)",
    },
    "126": {
        "chunks": "पुनः | आर्त्तवदर्शनात् | इति | एके",
        "sandhi": "उ के बाद विसर्ग → र् स्वर से पहले: पुनः + आर्तव → पुनरार्तव · त् → द् स्वर से पहले: …दर्शनात् + इति → …दर्शनादिति · इ + ए → ये: इति + एके → इत्येके।",
        "frame": "मत-सूचक: ‘इति एके’ = ऐसा कुछ (कहते हैं); क्रिया छपी नहीं।",
    },
    "127": {
        "chunks": "इत्याद्यं मासमादाय | यावद्गर्भक्षमा पुनः | स्त्री स्यात्तावद्विधिः सर्वः | सर्वथा साधु दर्शितः",
        "sandhi": "इ + आ → या: इति + आद्यम् → इत्याद्यम् · त् → द् घोष से पहले: यावत् + गर्भ → यावद्गर्भ, तावत् + विधिः → तावद्विधिः।",
        "frame": "यावत् (जब तक: स्त्री फिर गर्भक्षमा हो) ↔ तावत् (तब तक: सारी विधि दिखा दी गई)।",
    },
    "128": {
        "chunks": "इति | गर्भोपचरणीयो | नाम | तृतीयोऽध्यायः",
        "sandhi": "अ + उ → ओ: गर्भ + उपचरणीयः → गर्भोपचरणीयः · अः + अ → ओऽ: तृतीयः + अध्यायः → तृतीयोऽध्यायः।",
        "anchors": "याद-सूत्र: अध्याय ३ = गर्भ-उपचार; गर्भिणी-चर्या से सूतिका-काल तक। (अध्याय के खण्डों से मेरा सार)",
    },
}

# ===================================================================== IMAGE_SPECS
IMAGE_SPECS = {
    ("116", "diagram"): {
        "file": "sh3-sneha-churna-116.svg",
        "alt": ("Two columns of unit 116: the sneha dose is joined either with pañcakola powder, or with a powder of six "
                "items in the line's order: yavānī (ajwain, standard), upakuñcikā (probably nigella, disputed), cavya, "
                "citraka, vyoṣa (three pungents), saindhava (rock salt, standard)."),
        "type": "split",
        "title": "इकाई ११६: स्नेह-मात्रा के साथ चूर्ण",
        "cols": [["पहला चूर्ण", ["पञ्चकोल"]],
                 ["या दूसरा चूर्ण", ["यवानी (अजवायन, मानक)", "उपकुञ्चिका (सम्भवतः कलौंजी, विवादित)", "चव्य", "चित्रक",
                                    "व्योष (तीन कटु)", "सैन्धव (सेंधा नमक, मानक)"]]],
    },
    ("117", "chain"): {
        "file": "sh3-snehayogya-117.svg",
        "alt": ("Flowchart of unit 117: for one unfit for sneha, a decoction of vāta-relieving medicines, or of the lesser "
                "pañcamūla (printed katha, read kvātha); separately, for one who has drunk, anointing with yamaka (probably oil and ghee), "
                "then the belly wrapped with cloth."),
        "type": "mermaid",
        "code": ("flowchart TD\n"
                 "  A[\"स्नेह के अयोग्य\"] --> B[\"वातहर औषधों का क्वाथ (छपा कथ)\"]\n"
                 "  A -->|\"या\"| C[\"ह्रस्व पञ्चमूल का क्वाथ (छपा कथ)\"]\n"
                 "  D[\"जिसने पी लिया हो\"] --> E[\"यमक से अभ्यंग\"]\n"
                 "  E --> F[\"पेट कपड़े से लपेटना\"]\n"),
    },
    ("119", "diagram"): {
        "file": "sh3-jirna-sneha-yavagu-119.svg",
        "alt": ("Two columns of unit 119: once the sneha is digested, the yavāgū is cooked with one of three: the same "
                "earlier medicines, the vidārī-group decoction (printed kathātha, read kvātha), or milk; it is well boiled, liquid and given in measure."),
        "type": "split",
        "title": "इकाई ११९: स्नेह पचने पर यवागू",
        "cols": [["किससे सिद्ध (कोई एक)", ["वही पहले वाली औषधियाँ", "विदारी-आदि गण का क्वाथ (छपा कथाथ)", "या दूध"]],
                 ["यवागू कैसी", ["भली प्रकार उबली", "तरल", "मात्रा से"]]],
    },
    ("121", "chain"): {
        "file": "sh3-kramad-apyayana-121.svg",
        "alt": ("Numbered flowchart of unit 121: 1 three or five nights of this regimen (a third, unclear period is left "
                "out), 2 soup of barley, jujube and horse gram with light food and drink, 3 after twelve nights, "
                "4 jāṅgala broths and the like, 5 gradually, having regard to digestive fire and strength."),
        "type": "mermaid",
        "code": ("flowchart TD\n"
                 "  A[\"१ तीन या पाँच रात\"] --> B[\"२ यव-कोल-कुलत्थ का यूष और हल्का अन्न-पान\"]\n"
                 "  B --> D[\"३ बारह रात के बाद\"]\n"
                 "  D --> E[\"४ जाङ्गल रस आदि\"]\n"
                 "  E --> F[\"५ अग्नि-बल देखकर, क्रम से\"]\n"),
    },
    ("124", "chain"): {
        "file": "sh3-sutika-vyadhi-124.svg",
        "alt": ("Flowchart of unit 124: from a depleted body (conjectural reading) she becomes new again; for this reason "
                "the sūtikā's disease is hard to cure or incurable; therefore she is treated with effort by the stated "
                "procedure."),
        "type": "mermaid",
        "code": ("flowchart TD\n"
                 "  A[\"रिक्त शरीर (अनुमानित पाठ)\"] --> B[\"फिर नई हो जाती है\"]\n"
                 "  B -->|\"इसी कारण\"| C[\"रोग कष्टसाध्य या असाध्य\"]\n"
                 "  C -->|\"इसलिए\"| D[\"यत्न से यथोक्त उपचार\"]\n"),
    },
    ("125", "chain"): {
        "file": "sh3-sutika-kala-125.svg",
        "alt": ("Flowchart of unit 125: treated for one and a half months, gradually released from the restraint of food "
                "and conduct, she is no longer called sūtikā."),
        "type": "mermaid",
        "code": ("flowchart TD\n"
                 "  A[\"डेढ़ मास उपचार\"] --> B[\"क्रम से यन्त्रणा से मुक्त\"]\n"
                 "  B --> C[\"सूतिका नाम चला गया\"]\n"),
    },
}
