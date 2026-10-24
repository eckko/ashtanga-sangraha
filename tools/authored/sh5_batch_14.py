from helpers import mcq, match, order, fill, multi, accepts


AUTHORED = {}

# ---------------------------------------------------------------- unit 166
AUTHORED["166"] = {
    "title": "पंच जिव्हायां",
    "question": "By unit 166, what number is given for the tongue?",
    "rule": ("Five (पञ्च) in the tongue (जिह्वायाम्, locative 'in'). The counted item, snāyu (sinews), is carried from the "
             "run of counts begun at unit 144; it is not printed here."),
    "limits": ("Prose, two words; no verb and no counted noun are printed. The print spells जिव्हायां, a variant (h and v "
               "reversed) of जिह्वायाम्, as the data notes. Per side or in all is not said."),
    "explain_hi": ("यह दो शब्दों की गद्य-पंक्ति है: पाँच, जीभ में। "
                   "गिनी गई वस्तु स्नायु है, जो इकाई १४४ से आरम्भ हुई गिनती से चली आ रही है; यहाँ वह शब्द छपा नहीं। "
                   "‘जिह्वायाम्’ जिह्वा (जीभ, स्त्रीलिंग) का सप्तमी एकवचन है: जीभ में। "
                   "छपाई में ‘जिव्हायां’ है, यानी ह और व का क्रम उलटा; यह इस छपाई की एक आदत है। "
                   "क्रिया भी नहीं लिखी; ‘हैं’ समझा जाता है।"),
    "hook": "जीभ में पाँच स्नायु।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 166, how many snāyus are counted in the tongue?",
            ("Five", "पंच जिव्हायां: five in the tongue."),
            [("Four", "Four is the count for the two jaws (unit 165), not the tongue."),
             ("Six", "Six is the count for the head (unit 168), not the tongue."),
             ("Twelve", "Twelve is the count for the gums (unit 167), not the tongue.")],
            "Five in the tongue.",
            "पञ्च = five; जिह्वायाम् = in the tongue."),
        match(1, "Match each part of unit 166 to its meaning.",
              [["पञ्च", "five"], ["जिह्वा", "tongue"], ["जिह्वायाम्", "in the tongue"]],
              "पञ्च जिह्वायाम् = five in the tongue.",
              "पञ्च, जिह्वा, जिह्वायाम्."),
        fill(2, "In unit 166 the number given for the tongue is ____ (type it in Devanagari or in English letters, "
                "e.g. dharma).",
             accepts("पञ्च", "pañca", "पंच", "five"),
             "पञ्च (printed पंच) = five: five snāyus in the tongue.",
             "पञ्च = five; the print writes the nasal as anusvāra, पंच.",
             "पंच जिव्हायां."),
        mcq("discriminate", 3, "What does the data say about the printed spelling जिव्हायां in unit 166?",
            ("A variant of जिह्वायाम्, with ह and व reversed", "The text flag: h/v letter reversal, seen elsewhere in this print."),
            [("A separate word for the jaw, not the tongue", "The data reads the tongue (जिह्वा); the jaws are हनु (unit 165)."),
             ("A dual form meaning in the two tongues", "The data reads a locative singular, जिह्वायाम्."),
             ("A plural noun, the tongues, as subject", "The data reads a locative: in the tongue.")],
            "जिव्हा is this print's spelling of जिह्वा: ह and व are reversed.",
            "जिव्हायां (printed) = जिह्वायाम्."),
        multi("apply", 4, "Which statements fit unit 166?",
              [("It prints the word snāyu", "No word for the counted snāyus is printed; it is carried from unit 144."),
               ("It gives the place in the locative case", "Right: जिह्वायाम् = in the tongue."),
               ("It counts five in the tongue", "Right: पंच जिव्हायां."),
               ("It prints a verb meaning 'are'", "No verb is printed; 'are' is understood.")],
              [1, 2],
              "Five in the tongue, the place in the locative; noun and verb are not printed.",
              "पञ्च जिह्वायाम्."),
        mcq("transfer", 5, "By the pattern of जिह्वायाम् (in the tongue, from जिह्वा), how is in the branch said from शाखा?",
            ("शाखायाम्", "An आ-stem feminine takes -आयाम् for 'in': जिह्वा → जिह्वायाम्, शाखा → शाखायाम्."),
            [("शाखया", "शाखया is the instrumental, 'by the branch'."),
             ("शाखायाः", "शाखायाः is the genitive or ablative singular, not 'in'."),
             ("शाखाम्", "शाखाम् is the accusative singular, not 'in'.")],
            "शाखायाम् = in the branch, like जिह्वायाम् = in the tongue.",
            "आ-stem feminine + -आयाम् = locative singular, 'in'.",
            teaches="जिह्वायाम् is the locative singular of the feminine जिह्वा: -आयाम् means 'in'."),
    ],
}

# ---------------------------------------------------------------- unit 167
AUTHORED["167"] = {
    "title": "द्वादशोत्तराधरेषु दंतमांसेषु",
    "question": "By unit 167, where are twelve snāyus counted?",
    "rule": ("Twelve (द्वादश) in the upper and lower (उत्तराधरेषु) gums (दन्तमांसेषु, literally 'tooth-flesh'). The counted "
             "snāyus are carried from unit 144."),
    "limits": ("Prose; no verb and no counted noun are printed. The line does not split the twelve between upper and lower "
               "gums."),
    "explain_hi": ("यह गद्य-पंक्ति कहती है: ऊपर और नीचे के दन्तमांस यानी मसूड़ों में बारह स्नायु। "
                   "दन्तमांस का शब्दार्थ है ‘दाँत का मांस’, यानी मसूड़े। "
                   "‘द्वादशोत्तर’ में द्वादश + उत्तर जुड़े हैं: अ + उ से ओ बना। "
                   "उत्तर (ऊपर का) और अधर (नीचे का) सप्तमी बहुवचन में दन्तमांसेषु के साथ मेल खाते हैं। "
                   "बारह ऊपर-नीचे में कैसे बँटे, यह नहीं कहा गया।"),
    "hook": "मसूड़ों में बारह: ऊपर और नीचे।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 167, where are twelve snāyus counted?",
            ("In the upper and lower gums", "उत्तराधरेषु दंतमांसेषु: in the upper and lower gums."),
            [("In the upper and lower lips", "The lips (ओष्ठ) are not named in unit 167."),
             ("In the two jaws and the neck", "The jaws come in unit 165; unit 167 names the gums."),
             ("In the tongue and the palate", "The tongue comes in unit 166; unit 167 names the gums.")],
            "Twelve in the upper and lower gums.",
            "द्वादश उत्तराधरेषु दन्तमांसेषु."),
        order(1, "Put the parts of unit 167 in the line's order.",
              ["द्वादश", "उत्तर", "अधरेषु", "दंतमांसेषु"],
              "Twelve, in the upper and lower gums.",
              "द्वादश → उत्तर → अधरेषु → दन्तमांसेषु."),
        match(2, "Match each word of unit 167 to its meaning.",
              [["द्वादश", "twelve"], ["उत्तर", "upper"], ["अधर", "lower"], ["दन्तमांस", "gums (tooth-flesh)"]],
              "Twelve in the upper and lower gums.",
              "द्वादश, उत्तर, अधर, दन्तमांस.", role="extend",
              teaches="दन्तमांस = 'tooth-flesh', the gums; उत्तर and अधर here mean upper and lower."),
        mcq("discriminate", 3, "Which split of द्वादशोत्तर in unit 167 is right?",
            ("द्वादश + उत्तर", "अ + उ → ओ: द्वादश + उत्तर → द्वादशोत्तर."),
            [("द्वादशो + उत्तर", "द्वादशो is not the number; the word is द्वादश (twelve)."),
             ("द्वादश + ओत्तर", "ओत्तर is not a word; the word is उत्तर (upper)."),
             ("द्वादशः + उत्तर", "A visarga after अ drops before उ: that gives द्वादश उत्तर, two words.")],
            "द्वादश (twelve) + उत्तर (upper): अ + उ → ओ.",
            "अ + उ → ओ."),
        mcq("apply", 4, "By unit 167, what does दन्तमांस literally mean?",
            ("Tooth-flesh, that is, the gums", "दन्त (tooth) + मांस (flesh): the gums."),
            [("Tooth-root, that is, the socket", "मांस is flesh, not root or socket."),
             ("Lip-flesh, that is, the lips", "दन्त is tooth, not lip."),
             ("Jaw-bone, that is, the jaw", "दन्त is tooth and मांस is flesh, not bone.")],
            "दन्तमांस = tooth-flesh = the gums.",
            "दन्त + मांस = tooth-flesh."),
        mcq("transfer", 5, "By the pattern of दन्तमांसेषु (in the gums, from दन्तमांस), how is in the houses said from गृह?",
            ("गृहेषु", "An अ-stem takes -एषु for 'in' (plural): दन्तमांस → दन्तमांसेषु, गृह → गृहेषु."),
            [("गृहे", "गृहे is the locative singular, 'in the house'."),
             ("गृहाणि", "गृहाणि is the nominative or accusative plural."),
             ("गृहैः", "गृहैः is the instrumental plural, 'by the houses'.")],
            "गृहेषु = in the houses, like दन्तमांसेषु = in the gums.",
            "अ-stem + -एषु = locative plural, 'in'.",
            teaches="दन्तमांसेषु is the locative plural of an अ-stem: -एषु means 'in' (many)."),
    ],
}

# ---------------------------------------------------------------- unit 168
AUTHORED["168"] = {
    "title": "षण्मूर्द्धनि",
    "question": "By unit 168, what number is given for the head?",
    "rule": ("Six (षट्) in the head (मूर्धनि). Printed as one word: ट् before the nasal म is here written ण् (a nasal before "
             "a nasal; this change is optional). The counted snāyus are carried from unit 144."),
    "limits": ("Prose, one printed word; no verb and no counted noun are printed. The doubled -र्द्ध- is a print habit, "
               "normalised to मूर्धनि in the data."),
    "explain_hi": ("यह एक छपे शब्द की गद्य-पंक्ति है: छह, सिर में। "
                   "‘षण्मूर्द्धनि’ = षट् (छह) + मूर्धनि (सिर में)। "
                   "म जैसे नासिक्य से पहले ट् यहाँ ण् लिखा गया है; यह परिवर्तन विकल्प से होता है। "
                   "‘मूर्द्धनि’ में दोहरा द छपाई की आदत है; शुद्ध रूप मूर्धनि, मूर्धन् (सिर) का सप्तमी एकवचन। "
                   "गिनी गई वस्तु स्नायु है, इकाई १४४ से चली आ रही।"),
    "hook": "सिर में छह: षट् मूर्धनि।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 168, how many snāyus are counted in the head?",
            ("Six", "षण्मूर्द्धनि: six in the head."),
            [("Twelve", "Twelve is the count for the gums (unit 167)."),
             ("Five", "Five is the count for the tongue (unit 166)."),
             ("Sixty", "षट् is six; sixty would be षष्टि.")],
            "Six in the head.",
            "षट् = six; मूर्धनि = in the head."),
        match(1, "Match each part of unit 168 to its meaning.",
              [["षट्", "six"], ["मूर्धन्", "head"], ["मूर्धनि", "in the head"]],
              "षट् + मूर्धनि = षण्मूर्धनि: six in the head.",
              "षट्, मूर्धन्, मूर्धनि."),
        fill(2, "In unit 168 the plain number word hidden in षण्- is ____ (type it in Devanagari or in English letters, "
                "e.g. dharma).",
             accepts("षट्", "ṣaṭ", "six"),
             "षट् = six; before मूर्धनि it is written षण्.",
             "षट् = six; ट् before a nasal may become ण्.",
             "षट् + मूर्धनि → षण्मूर्धनि."),
        mcq("discriminate", 3, "Which split of षण्मूर्द्धनि in unit 168 is right?",
            ("षट् + मूर्धनि", "ट् before the nasal म is written ण् here: षट् + मूर्धनि → षण्मूर्धनि."),
            [("षष्टि + मूर्धनि", "षष्टि is sixty, and no ष्टि is printed; the data reads six, षट्."),
             ("षण्मू + र्धनि", "र्धनि is not a word; the word is मूर्धनि (in the head)."),
             ("षण + मूर्धनि", "षण is not the number word; six is षट्.")],
            "षट् (six) + मूर्धनि (in the head).",
            "ट् + म → ण्म (optional nasal before a nasal)."),
        mcq("apply", 4, "Why is मूर्धनि printed मूर्द्धनि in unit 168?",
            ("A print habit of doubling द after र", "The note: doubled -rdd- is a print habit, normalised to मूर्धनि."),
            [("A dual form, meaning in the two heads", "The data reads a locative singular, मूर्धनि."),
             ("A different word, meaning in the neck", "The data reads मूर्धन्, the head."),
             ("A sandhi change caused by the six", "The six changes only its own ट्; the द्द is a print habit.")],
            "मूर्द्धनि = मूर्धनि; the doubled द is a habit of this print.",
            "Printed र्द्ध = र्ध (print habit)."),
        mcq("transfer", 5, "By the rule of षण्मूर्धनि (ट् before म written ण्), what number stands in षण्मुखः (six-faced), a new example?",
            ("Six (षट्)", "षण्- before मुख is षट् with ट् written ण् before the nasal म."),
            [("Sixty (षष्टि)", "Sixty would be षष्टि, not षण्-."),
             ("Sixteen (षोडश)", "Sixteen is षोडश, not षण्-."),
             ("Five (पञ्च)", "Five is पञ्च, not षण्-.")],
            "षण्मुखः = षट् + मुख: six-faced.",
            "ट् + म → ण्म (optional).",
            teaches="Before a nasal such as म, a final ट् may become ण्: षट् + मूर्धनि → षण्मूर्धनि."),
    ],
}

# ---------------------------------------------------------------- unit 169
AUTHORED["169"] = {
    "title": "तत्र शाखासु संधिषु च प्रतानवंति",
    "question": "By unit 169, which snāyus are tendrilled, and which are called kaṇḍarā?",
    "rule": ("Among these, those in the limbs (शाखा) and joints (सन्धि) are tendrilled (प्रतानवत्, with spreading branches); "
             "but the large round ones (महास्नावानि ... वृत्तानि) are called kaṇḍarā (probably tendons)."),
    "limits": ("Two printed lines, prose; medium confidence; no verb (copula understood). snāva is a variant of snāyu, "
               "'probably ligaments or tendons' (probable); kaṇḍarā = tendon is probable. pratāna = tendril; the Sanskrit "
               "makes no comparison with a creeper, so the card adds none. The kinds of snāyu begin here."),
    "explain_hi": ("ये दो छपी पंक्तियाँ स्नायु के प्रकार बताना आरम्भ करती हैं। "
                   "उनमें (तत्र) जो शाखाओं यानी हाथ-पैरों और सन्धियों में हैं, वे प्रतानवत् हैं, यानी फैली हुई शाखाओं वाले। "
                   "पर (तु) जो बड़े स्नायु गोल (वृत्त) हैं, वे कण्डरा कहलाते हैं; कण्डरा सम्भवतः टेंडन है। "
                   "स्नाव यहाँ स्नायु का ही दूसरा रूप है, सम्भवतः लिगामेंट या टेंडन। "
                   "प्रतान का अर्थ लता की कोंपल या तन्तु है, पर पाठ लता से कोई तुलना नहीं करता।"),
    "hook": "हाथ-पैर व जोड़ों में फैले, बड़े गोल कण्डरा।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 169, what are the large round snāyus called?",
            ("कण्डरा", "महास्नावानि तु वृत्तानि तानि कण्डरासंज्ञानि: called kaṇḍarā."),
            [("प्रतानवत्", "Tendrilled is said of those in the limbs and joints."),
             ("सुषिर", "Hollow ones are named in unit 170, not here."),
             ("पृथु", "Broad ones are named in unit 171, not here.")],
            "The large round ones are called kaṇḍarā (probably tendons).",
            "महास्नावानि ... वृत्तानि ... कण्डरासंज्ञानि."),
        order(1, "Put these printed parts of unit 169 in the lines' order.",
              ["तत्र शाखासु संधिषु च", "प्रतानवंति", "महास्नावानि तु", "वृत्तानितानि", "कंडरासंज्ञानि"],
              "Among these, in the limbs and joints: tendrilled; but the large ones, round, are called kaṇḍarā.",
              "शाखासु संधिषु च → प्रतानवंति → महास्नावानि तु → वृत्तानि तानि → कंडरासंज्ञानि."),
        match(2, "Match each word of unit 169 to its meaning.",
              [["शाखा", "limb"], ["सन्धि", "joint"], ["प्रतान", "tendril"], ["वृत्त", "round"],
               ["कण्डरा", "probably tendon"]],
              "In the limbs and joints: tendrilled; the large round ones: kaṇḍarā.",
              "शाखा, सन्धि, प्रतान, वृत्त, कण्डरा.", role="extend",
              teaches="प्रतानवत् = having tendrils, spreading in branches; कण्डरा is probably a tendon."),
        mcq("discriminate", 3, "Which pairing of place or shape and kind is right by unit 169?",
            ("Limbs and joints: tendrilled", "शाखासु संधिषु च प्रतानवंति."),
            [("Limbs and joints: named kaṇḍarā", "Kaṇḍarā is the name of the large round ones."),
             ("Large and round: tendrilled", "The large round ones are called kaṇḍarā."),
             ("Large and round: called broad", "Unit 169 does not call them broad.")],
            "Limbs and joints → tendrilled; large and round → kaṇḍarā.",
            "शाखासन्धिषु प्रतानवन्ति; महान्ति वृत्तानि कण्डराः."),
        multi("apply", 4, "Which statements fit unit 169?",
              [("It compares the snāyus to a creeper", "The note: the Sanskrit gives no comparison with a creeper."),
               ("Those in the limbs and joints are tendrilled", "Right: शाखासु संधिषु च प्रतानवंति."),
               ("Here snāva names a thing other than snāyu", "The note: snāva is a variant of snāyu."),
               ("The large round ones are called kaṇḍarā", "Right: वृत्तानि तानि कण्डरासंज्ञानि.")],
              [1, 3],
              "Tendrilled in the limbs and joints; the large round ones are kaṇḍarā.",
              "प्रतानवन्ति ... कण्डरासंज्ञानि."),
        mcq("transfer", 5, "By the pattern of महास्नाव (large sinew), what does महावृक्षः mean in a new example?",
            ("A large tree", "महा- at the start of a karmadhāraya = large: महा + स्नाव = large sinew."),
            [("A small tree", "महा- means large, not small."),
             ("Many trees", "महा- is not a plural; the compound is one tree."),
             ("A tree's root", "Nothing in महा- means root.")],
            "महावृक्षः = a large tree, as महास्नाव = a large sinew.",
            "महत् → महा- in a karmadhāraya: large X.",
            teaches="In महास्नाव, महा- (from महत्, large) describes the sinew: a karmadhāraya, 'large sinew'."),
    ],
}

# ---------------------------------------------------------------- unit 170
AUTHORED["170"] = {
    "title": "बस्त्यामपक्वाशयांत्रेषु सुषिराणि",
    "question": "By unit 170, which snāyus are hollow, and where are they?",
    "rule": ("Hollow ones (सुषिराणि) are in the bladder (बस्ति), the seats of the raw and the cooked (āmāśaya and pakvāśaya, "
             "probably the stomach and the large intestine) and the intestines (अन्त्र)."),
    "limits": ("Prose; medium confidence; no verb or counted noun printed. आमपक्वाशय may be a contracted dvandva for āmāśaya "
               "and pakvāśaya; that reading and the identifications stomach / large intestine are probable only. "
               "No question on the exact parse of आमपक्वाशय."),
    "explain_hi": ("यह गद्य-पंक्ति स्नायु का एक और प्रकार बताती है: सुषिर यानी खोखले। "
                   "वे बस्ति यानी मूत्राशय में, कच्चे (आम) और पके (पक्व) के आशयों में, और अन्त्र यानी आँतों में हैं। "
                   "आमाशय और पक्वाशय सम्भवतः जठर और बड़ी आँत हैं (सम्भावित पहचान)। "
                   "छपा ‘आमपक्वाशय’ सम्भवतः दोनों आशयों का संक्षिप्त द्वन्द्व है, इसलिए अनुवाद दोनों नाम देता है। "
                   "‘बस्त्याम’ में बस्ति + आम जुड़े हैं: इ + आ से या बना।"),
    "hook": "मूत्राशय, आमाशय-पक्वाशय, आँतें: खोखले स्नायु।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 170, what kind of snāyu is in the bladder and the intestines?",
            ("Hollow (सुषिर)", "सुषिराणि: hollow ones."),
            [("Broad (पृथु)", "Broad ones are in unit 171, in other places."),
             ("Round (वृत्त)", "Round ones are the kaṇḍarās of unit 169."),
             ("Spread (प्रतान)", "Tendrilled ones are in the limbs and joints (unit 169).")],
            "Hollow ones are in the bladder, the two seats and the intestines.",
            "बस्त्यामपक्वाशयांत्रेषु सुषिराणि."),
        order(1, "Put the parts of unit 170 in the line's order.",
              ["बस्ति", "आमपक्वाशय", "अंत्रेषु", "सुषिराणि"],
              "In the bladder, the seats of the raw and the cooked, and the intestines: hollow ones.",
              "बस्ति → आमपक्वाशय → अन्त्रेषु → सुषिराणि."),
        match(2, "Match each word of unit 170 to its meaning.",
              [["बस्ति", "bladder"], ["अन्त्र", "intestine"], ["सुषिर", "hollow"], ["आम", "raw"], ["पक्व", "cooked"]],
              "Hollow ones in the bladder, the seats of the raw and the cooked, and the intestines.",
              "बस्ति, अन्त्र, सुषिर, आम, पक्व.", role="extend",
              teaches="आमाशय and पक्वाशय = seats of the raw and of the cooked, probably the stomach and the large intestine."),
        mcq("discriminate", 3, "Which split of बस्त्याम in unit 170 is right?",
            ("बस्ति + आम", "इ before an unlike vowel becomes य्: बस्ति + आम → बस्त्याम."),
            [("बस्त् + याम", "याम is not the word; the word is आम (raw)."),
             ("बस्ते + आम", "ए + आ would give बस्त आम or बस्तयाम, not बस्त्याम."),
             ("बस्ति + याम", "That would keep the इ: बस्तियाम, not बस्त्याम.")],
            "बस्ति (bladder) + आम (raw): इ + आ → या.",
            "इ + unlike vowel → य् + that vowel."),
        mcq("apply", 4, "Why does the English of unit 170 name both āmāśaya and pakvāśaya for the printed आमपक्वाशय?",
            ("It may be a short dvandva of both seats", "The note: a contracted dvandva for āmāśaya and pakvāśaya."),
            [("The print repeats one and the same word twice", "The word is printed once, as आमपक्वाशय."),
             ("The Hindi adds a seat not in the line", "Both आम and पक्व are printed in the line."),
             ("आम and पक्व are two names of one seat", "आम (raw) and पक्व (cooked) are opposite, two seats.")],
            "आमपक्वाशय is read as आमाशय + पक्वाशय, a contracted dvandva.",
            "आम-पक्व-आशय = the seats of the raw and the cooked."),
        mcq("transfer", 5, "By the rule of बस्ति + आम, how is अति + आचारः (excess conduct) joined?",
            ("अत्याचारः", "इ before आ becomes य्, as बस्ति + आम → बस्त्याम."),
            [("अतीचारः", "ई comes from इ + इ, not from इ + आ."),
             ("अतेचारः", "ए comes from अ + इ, not from इ + आ."),
             ("अतयाचारः", "अय् comes from ए before a vowel, not from इ.")],
            "अति + आचारः = अत्याचारः, like बस्ति + आम = बस्त्याम.",
            "इ + आ → या.",
            teaches="इ before an unlike vowel becomes य्: बस्ति + आम → बस्त्याम."),
    ],
}

# ---------------------------------------------------------------- unit 171
AUTHORED["171"] = {
    "title": "पार्श्वपृष्ठोरःशिरःसु पृथूनि",
    "question": "By unit 171, where are the broad snāyus?",
    "rule": ("Broad ones (पृथूनि) are in the sides (पार्श्व), the back (पृष्ठ), the chest (उरस्) and the head (शिरस्): one "
             "dvandva in the locative plural."),
    "limits": ("Prose; no verb and no counted noun printed (snāyu, carried from unit 144). The line gives no number."),
    "explain_hi": ("यह गद्य-पंक्ति स्नायु का एक और प्रकार बताती है: पृथु यानी चौड़े। "
                   "वे पार्श्वों (बगल), पीठ, छाती और सिर में हैं। "
                   "चारों स्थान एक द्वन्द्व समास में सप्तमी बहुवचन (-सु) में हैं। "
                   "‘पृष्ठोरः’ में पृष्ठ + उरः जुड़े हैं: अ + उ से ओ बना। "
                   "यहाँ कोई संख्या नहीं दी गई।"),
    "hook": "बगल, पीठ, छाती, सिर: चौड़े स्नायु।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 171, where are the broad (पृथु) snāyus found?",
            ("Sides, back, chest and head", "पार्श्वपृष्ठोरःशिरःसु पृथूनि."),
            [("Bladder, stomach and intestines", "Those places hold the hollow ones (unit 170)."),
             ("The limbs and the joints of the body", "Those hold the tendrilled ones (unit 169)."),
             ("Tongue, gums and the two jaws", "Those are counts in units 165-167, not the broad kind.")],
            "Broad ones are in the sides, back, chest and head.",
            "पार्श्व, पृष्ठ, उरस्, शिरस् → पृथूनि."),
        order(1, "Put the words of unit 171 in the line's order.",
              ["पार्श्व", "पृष्ठ", "उरः", "शिरःसु", "पृथूनि"],
              "In the sides, back, chest and head: broad ones.",
              "पार्श्व → पृष्ठ → उरः → शिरःसु → पृथूनि."),
        match(2, "Match each word of unit 171 to its meaning.",
              [["पार्श्व", "side"], ["पृष्ठ", "back"], ["उरस्", "chest"], ["शिरस्", "head"], ["पृथु", "broad"]],
              "Broad ones in the sides, back, chest and head.",
              "पार्श्व, पृष्ठ, उरस्, शिरस्, पृथु.", role="extend",
              teaches="पृथु = broad: the kind of snāyu in the sides, back, chest and head."),
        mcq("discriminate", 3, "Which split of पृष्ठोरः in unit 171 is right?",
            ("पृष्ठ + उरः", "अ + उ → ओ: पृष्ठ + उरः → पृष्ठोरः."),
            [("पृष्ठः + उरः", "A visarga after अ drops before उ: that gives पृष्ठ उरः, two words."),
             ("पृष्ठो + रः", "रः is not a word here; the word is उरः (chest)."),
             ("पृष्ठ + ओरः", "ओरः is not a word; the word is उरः.")],
            "पृष्ठ (back) + उरः (chest): अ + उ → ओ.",
            "अ + उ → ओ."),
        mcq("apply", 4, "A teacher points to the snāyus of the chest. By unit 171, what kind are they?",
            ("Broad (पृथु)", "उरः is among the places of पृथूनि."),
            [("Hollow (सुषिर)", "Hollow ones are in the bladder and the intestines (unit 170)."),
             ("Round (वृत्त)", "Round ones are the large kaṇḍarās (unit 169)."),
             ("Spread (प्रतान)", "Tendrilled ones are in the limbs and joints (unit 169).")],
            "The chest is a place of the broad ones.",
            "उरः ... पृथूनि."),
        mcq("transfer", 5, "By the rule of पृष्ठ + उरः, how is हित + उपदेशः (good advice) joined?",
            ("हितोपदेशः", "अ + उ → ओ, as पृष्ठ + उरः → पृष्ठोरः."),
            [("हितौपदेशः", "औ comes from अ + ओ or अ + औ, not from अ + उ."),
             ("हितूपदेशः", "ऊ comes from उ + उ, not from अ + उ."),
             ("हितवुपदेशः", "अव् comes from ओ before a vowel, not from अ + उ.")],
            "हित + उपदेशः = हितोपदेशः, like पृष्ठ + उरः = पृष्ठोरः.",
            "अ + उ → ओ.",
            teaches="अ + उ gives ओ: पृष्ठ + उरः → पृष्ठोरः."),
    ],
}

# ---------------------------------------------------------------- unit 172
AUTHORED["172"] = {
    "title": "स्नावबंधनैर्हि संधिषु सुबद्धा तनुः",
    "question": "By unit 172, why are the sinews important for the body?",
    "rule": ("For (हि) the body (तनु), well bound (सुबद्धा) in the joints by the bonds of sinew (स्नावबन्धनैः), acts "
             "properly (सम्यक् ईहते), like a boat (नौः इव)."),
    "limits": ("Prose; medium confidence. ईहते is 'acts' (data); 'moves well' is the alternative: no question on that choice. "
               "The printed doubled ग् (सम्यग्गीहते) is possibly a print slip for सम्यगीहते (text flag). The simile is not "
               "explained further."),
    "explain_hi": ("यह गद्य-पंक्ति स्नायुओं का महत्त्व बताती है। "
                   "क्योंकि (हि) स्नायु के बन्धनों से सन्धियों में भली-भाँति बँधा (सुबद्धा) शरीर (तनु), नाव की तरह, ठीक से चेष्टा करता है। "
                   "तनु (शरीर) और नौ (नाव) दोनों स्त्रीलिंग हैं और सुबद्धा उनसे मेल खाता है। "
                   "ईहते का अर्थ ‘चेष्टा करता है’ लिया गया; ‘ठीक से चलता है’ भी सम्भव है। "
                   "छपा ‘सम्यग्गीहते’ का दोहरा ग सम्भवतः छपाई की भूल है (सम्यक् + ईहते = सम्यगीहते)।"),
    "hook": "स्नायु से बँधा शरीर, नाव-सा ठीक चले।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 172, to what is the well-bound body compared?",
            ("A boat", "तनुर्नौरिव: the body, like a boat."),
            [("A tree", "No tree is named in unit 172; the simile is नौः, a boat."),
             ("A house", "No house is named in unit 172; the simile is a boat."),
             ("A chariot", "No chariot is named in unit 172; the simile is a boat.")],
            "The body, well bound, acts properly like a boat.",
            "तनुः नौः इव."),
        order(1, "Put the printed words of unit 172 in the line's order.",
              ["स्नावबंधनैर्हि", "संधिषु", "सुबद्धा", "तनुर्नौरिव", "सम्यग्गीहते"],
              "For by the bonds of sinew, in the joints, well bound, the body like a boat acts properly.",
              "स्नावबंधनैर्हि → संधिषु → सुबद्धा → तनुर्नौरिव → सम्यग्गीहते."),
        match(2, "Match each word of unit 172 to its meaning.",
              [["बन्धन", "bond"], ["सुबद्धा", "well bound"], ["तनु", "body (here)"], ["नौ", "boat"], ["इव", "like"]],
              "The body, well bound by the bonds of sinew, acts properly like a boat.",
              "बन्धन, सुबद्धा, तनु, नौ, इव.", role="extend",
              teaches="इव = like: तनुः नौः इव, the body like a boat (a simile)."),
        mcq("discriminate", 3, "Which split of तनुर्नौरिव in unit 172 is right?",
            ("तनुः + नौः + इव", "Visarga after उ or औ becomes र् before a voiced sound: तनुर् नौर् इव."),
            [("तनु + र्नौः + इव", "र्नौः is not a word; the र् comes from the visarga of तनुः."),
             ("तनुः + नौ + रिव", "रिव is not a word; the word is इव (like)."),
             ("तनुः + नौरि + व", "नौरि and व are not words here; it is नौः + इव.")],
            "तनुः (body) + नौः (boat) + इव (like).",
            "Visarga after a vowel other than अ/आ → र् before a voiced sound."),
        multi("apply", 4, "Which statements fit unit 172?",
              [("The body is compared with a chariot", "The simile is a boat (नौः), not a chariot."),
               ("The bonds are made of snāva (sinew)", "Right: स्नावबन्धनैः."),
               ("The body is bound in the joints", "Right: संधिषु सुबद्धा."),
               ("It says the joints are hollow", "Hollowness is not named in unit 172.")],
              [1, 2],
              "Bound in the joints by the bonds of sinew, the body acts properly like a boat.",
              "स्नावबन्धनैः संधिषु सुबद्धा."),
        mcq("transfer", 5, "By the rule of तनुः + नौः → तनुर्नौः, how is गुरुः + गच्छति (the teacher goes) joined?",
            ("गुरुर्गच्छति", "A visarga after उ becomes र् before the voiced ग, as तनुः + नौः → तनुर्नौः."),
            [("गुरुः गच्छति", "Before a voiced sound the visarga after उ does not stay."),
             ("गुरुस्गच्छति", "स् comes from a visarga before त or थ, not before ग."),
             ("गुरु गच्छति", "The visarga after उ drops only before र, with lengthening.")],
            "गुरुः + गच्छति = गुरुर्गच्छति, like तनुः + नौः = तनुर्नौः.",
            "उः + voiced sound → उर्.",
            teaches="A visarga after a vowel other than अ/आ becomes र् before a voiced sound: तनुः + नौः → तनुर्नौः."),
    ],
}

# ---------------------------------------------------------------- unit 173
AUTHORED["173"] = {
    "title": "तस्मादस्थिसिरादिभ्योऽपि तानि यत्नतो रक्षेत्",
    "question": "By unit 173, what should one do with the sinews?",
    "rule": ("Therefore (तस्मात्) one should protect (रक्षेत्, optative) them (तानि, the sinews) with effort (यत्नतः), even "
             "more than the bones, vessels (sirā, probable) and the rest (the data's reading)."),
    "limits": ("Prose; medium confidence. 'More than' is the data's reading of the ablative with अपि; 'protect them even from "
               "(injury to) the bones, vessels etc.' is a less natural alternative: no question rests on 'more than'. "
               "sirā = vessel is probable."),
    "explain_hi": ("यह गद्य-पंक्ति स्नायुओं के बारे में एक निर्देश देती है। "
                   "इसलिए (तस्मात्) उन्हें (तानि, पिछली इकाइयों के स्नायु) यत्न से (यत्नतः) रक्षा करनी चाहिए (रक्षेत्)। "
                   "डेटा का पाठ है: अस्थि, सिरा (सम्भवतः वाहिनी) आदि से भी अधिक; अपादान ‘-भ्यः’ यहाँ तुलना का है। "
                   "दूसरा, कम स्वाभाविक, पाठ है: अस्थि-सिरा आदि की चोट से भी बचाना। "
                   "‘सिरादिभ्योऽपि’ में अः + अ से ओऽ बना।"),
    "hook": "स्नायु बचाओ, यत्न से।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 173, what should one do with the sinews?",
            ("Protect them with effort", "तानि यत्नतो रक्षेत्: one should protect them with effort."),
            [("Cut them with great care", "Nothing is said of cutting; रक्षेत् = should protect."),
             ("Bind them up once more", "Nothing is said of binding; रक्षेत् = should protect."),
             ("Leave them quite alone", "The line asks for effort (यत्नतः) in protecting them.")],
            "One should protect them with effort.",
            "तानि यत्नतो रक्षेत्."),
        order(1, "Put the printed parts of unit 173 in the line's order.",
              ["तस्मादस्थिसिरादिभ्योऽपि", "तानि", "यत्नतो", "रक्षेत्"],
              "Therefore, even more than the bones, vessels and the rest, one should protect them with effort.",
              "तस्मादस्थिसिरादिभ्योऽपि → तानि → यत्नतो → रक्षेत्."),
        match(2, "Match each word of unit 173 to its meaning.",
              [["तस्मात्", "therefore"], ["अस्थि", "bone"], ["तानि", "them"], ["यत्नतः", "with effort"],
               ["रक्षेत्", "should protect"]],
              "Therefore one should protect them with effort.",
              "तस्मात्, अस्थि, तानि, यत्नतः, रक्षेत्.", role="extend",
              teaches="रक्षेत् is an optative of √रक्ष्: 'one should protect'."),
        mcq("discriminate", 3, "Which split of सिरादिभ्योऽपि in unit 173 is right?",
            ("सिरादिभ्यः + अपि", "अः before अ becomes ओ, and the अ is shown by ऽ: सिरादिभ्योऽपि."),
            [("सिरादिभ्यो + अपि", "सिरादिभ्यो is not the base form; the ओ comes from अः by sandhi."),
             ("सिरादिभ्यः + पि", "पि is not a word; the word is अपि (even)."),
             ("सिरादिभ्ये + अपि", "ए + अ would give सिरादिभ्येऽपि, not -भ्योऽपि.")],
            "सिरादिभ्यः + अपि: अः + अ → ओऽ.",
            "अः + अ → ओ + ऽ."),
        mcq("apply", 4, "रक्षेत् in unit 173 is an optative (data). What sense does it give?",
            ("One should protect", "The optative here gives an instruction: one should protect."),
            [("One has protected", "That would be a past form, not the optative."),
             ("One will protect", "That would be a future form, not the optative."),
             ("One is being protected by them", "That would be a passive, not this active optative.")],
            "रक्षेत् = one should protect.",
            "Optative = should (instruction)."),
        mcq("transfer", 5, "By the rule of सिरादिभ्यः + अपि, how is रामः + अपि (Rāma also) joined?",
            ("रामोऽपि", "अः before अ becomes ओ, with ऽ for the अ, as सिरादिभ्यः + अपि."),
            [("रामापि", "The visarga drops this way after आ; रामः has a short अ."),
             ("रामरपि", "र् comes from a visarga after vowels other than अ and आ."),
             ("रामः अपि", "Before अ the visarga after अ does not stay.")],
            "रामः + अपि = रामोऽपि, like सिरादिभ्यः + अपि = सिरादिभ्योऽपि.",
            "अः + अ → ओऽ.",
            teaches="A visarga after short अ before अ: अः + अ → ओऽ (सिरादिभ्यः + अपि → सिरादिभ्योऽपि)."),
    ],
}

# ---------------------------------------------------------------- unit 174
AUTHORED["174"] = {
    "title": "यश्च स्नावानि बाह्यान्यभ्यंतराणि च",
    "question": "By unit 174, what can one do who knows the sinews well?",
    "rule": ("He who (यः) knows well the sinews, external (बाह्य) and internal (अभ्यन्तर), he (सः) becomes able (समर्थः) to "
             "extract (आहर्तुम्) even a hidden (गूढ) śalya (foreign body, standard)."),
    "limits": ("Prose; high confidence. The knower is not named (no title such as surgeon). The line does not say which sinews "
               "are external or internal. आहर्त्तुं with doubled त is a print habit (normalised आहर्तुम्)."),
    "explain_hi": ("यह गद्य-पंक्ति स्नायु-ज्ञान का फल बताती है। "
                   "जो बाहरी और भीतरी स्नायुओं को भली-भाँति जानता है, वह छिपे हुए शल्य को भी निकालने में समर्थ होता है। "
                   "शल्य यानी शरीर में घुसी बाहरी वस्तु, जैसे काँटा या तीर (मानक)। "
                   "यः ... सः (जो ... वह) का जोड़ा वाक्य को बाँधता है; आहर्तुम् ‘निकालने के लिए’ (तुमुन्) है। "
                   "कौन-से स्नायु बाहरी या भीतरी हैं, यह नहीं बताया गया।"),
    "hook": "स्नायु जानो, छिपा शल्य निकालो।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 174, what can one who knows the sinews well do?",
            ("Extract even a hidden foreign body", "गूढमपि शल्यमाहर्तुं समर्थो भवति."),
            [("Set every broken bone of the limbs", "Bones are not named in unit 174."),
             ("Stop any bleeding of the vessels", "Bleeding is not named in unit 174."),
             ("Cure every fever of the whole body", "Fever is not named in unit 174.")],
            "He becomes able to extract even a hidden śalya.",
            "स गूढमपि शल्यमाहर्तुं समर्थो भवति."),
        order(1, "Put these printed parts of unit 174 in the line's order.",
              ["यश्च स्नावानि", "बाह्यान्यभ्यंतराणि च", "सम्यग्जानाति", "स गूढमपि शल्यमाहर्त्तुं", "समर्थो भवति"],
              "He who knows well the sinews, external and internal, becomes able to extract even a hidden śalya.",
              "यश्च स्नावानि → बाह्यान्यभ्यंतराणि च → सम्यग्जानाति → स गूढमपि शल्यमाहर्त्तुं → समर्थो भवति."),
        match(2, "Match each word of unit 174 to its meaning.",
              [["बाह्य", "external"], ["अभ्यन्तर", "internal"], ["गूढ", "hidden"], ["शल्य", "foreign body"],
               ["आहर्तुम्", "to extract"]],
              "Knowing the external and internal sinews, one can extract even a hidden foreign body.",
              "बाह्य, अभ्यन्तर, गूढ, शल्य, आहर्तुम्.", role="extend",
              teaches="शल्य = a foreign body such as a dart or splinter (standard); आहर्तुम् = to extract."),
        mcq("discriminate", 3, "Which split of बाह्यान्यभ्यंतराणि in unit 174 is right?",
            ("बाह्यानि + अभ्यन्तराणि", "इ before an unlike vowel becomes य्: बाह्यानि + अभ्यन्तराणि."),
            [("बाह्यान् + यभ्यन्तराणि", "यभ्यन्तराणि is not a word; the word is अभ्यन्तराणि."),
             ("बाह्याने + अभ्यन्तराणि", "ए + अ would give बाह्यानेऽभ्यन्तराणि."),
             ("बाह्यान्य + अभ्यन्तराणि", "बाह्यान्य is not a form; the word is बाह्यानि.")],
            "बाह्यानि (external) + अभ्यन्तराणि (internal): इ + अ → य.",
            "इ + unlike vowel → य् + that vowel."),
        mcq("apply", 4, "A healer must remove a splinter buried deep. By unit 174, what knowledge makes one able?",
            ("Knowing the sinews, outer and inner", "यश्च स्नावानि बाह्यान्यभ्यन्तराणि च सम्यग्जानाति."),
            [("Knowing the bones and the joints", "Unit 174 names the sinews, not bones and joints."),
             ("Knowing the vessels and muscles", "Unit 174 names the sinews, not vessels or muscles."),
             ("Knowing the hollow seats of raw and cooked", "Unit 174 names the sinews, external and internal.")],
            "Knowing the external and internal sinews well.",
            "स्नावानि ... सम्यग्जानाति → शल्यमाहर्तुं समर्थः."),
        mcq("transfer", 5, "By the pattern of आहर्तुं समर्थः (able to extract), what does पठितुं समर्थः mean in a new example?",
            ("Able to read", "-तुम् (infinitive) + समर्थ = able to do it, as आहर्तुं समर्थः."),
            [("Has read it well", "-तुम् is not a past form."),
             ("Able since he read", "-तुम् gives 'to do', not a reason."),
             ("Wishes to read", "Wishing would be a desiderative, not -तुम् + समर्थ.")],
            "पठितुं समर्थः = able to read, like आहर्तुं समर्थः = able to extract.",
            "infinitive (-तुम्) + समर्थ = able to ...",
            teaches="आहर्तुम् is an infinitive (-तुम्): with समर्थ it means 'able to extract'."),
    ],
}

# ---------------------------------------------------------------- unit 175
AUTHORED["175"] = {
    "title": "पंच पेशीशतानि",
    "question": "By unit 175, how many peśī (muscles) are counted?",
    "rule": ("Five hundred peśī (पञ्च पेशीशतानि, 'five hundreds of muscles'): this appears to begin a new count, of the "
             "muscles, after the snāyu counts of units 144-174."),
    "limits": ("Prose; no verb (copula understood). peśī also names a flesh-lump elsewhere (embryology); here the data reads "
               "muscle. The places of the five hundred follow in the next units."),
    "explain_hi": ("यह गद्य-पंक्ति नई गिनती आरम्भ करती प्रतीत होती है: पाँच सौ पेशियाँ, यानी मांसपेशियाँ। "
                   "इससे पहले इकाई १४४-१७४ में स्नायुओं की गिनती और प्रकार थे। "
                   "‘पेशीशतानि’ = पेशी + शतानि, यानी पेशियों के सैकड़े; पञ्च के साथ: पाँच सौ। "
                   "पेशी शब्द अन्यत्र (गर्भ के विकास में) मांस-पिण्ड के लिए भी आता है, पर यहाँ उसे मांसपेशी पढ़ा गया है। "
                   "क्रिया नहीं लिखी; ‘हैं’ समझा जाता है।"),
    "hook": "पाँच सौ पेशियाँ: नई गिनती।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 175, how many peśī (muscles) are counted?",
            ("Five hundred", "पंच पेशीशतानि: five hundred muscles."),
            [("Nine hundred", "Nine hundred is the snāyu count (unit 144)."),
             ("Three hundred", "पञ्च शतानि is five hundred, not three hundred."),
             ("Seven hundred", "पञ्च शतानि is five hundred, not seven hundred.")],
            "Five hundred muscles.",
            "पञ्च शतानि = five hundred."),
        match(1, "Match each part of unit 175 to its meaning.",
              [["पञ्च", "five"], ["पेशी", "muscle"], ["शत", "hundred"], ["पेशीशतानि", "hundreds of muscles"]],
              "पञ्च पेशीशतानि = five hundreds of muscles.",
              "पञ्च, पेशी, शत, पेशीशतानि."),
        fill(2, "In unit 175 the word for muscle is ____ (type it in Devanagari or in English letters, e.g. dharma).",
             accepts("पेशी", "peśī"),
             "पेशी = muscle (standard): पञ्च पेशीशतानि, five hundred muscles.",
             "पेशी = muscle; also a flesh-lump in embryology.",
             "पंच पेशीशतानि."),
        mcq("discriminate", 3, "What count does unit 175 appear to begin?",
            ("The muscles (peśī), after the snāyu", "The note: a new enumeration of muscles after the snāyu counts."),
            [("The bones, after the joints", "The bones and joints were counted earlier; this line counts muscles."),
             ("The joints, after the bones", "The joints were counted earlier; this line counts muscles."),
             ("The vessels (sirā), after the muscles", "The line names peśī, muscles, not vessels.")],
            "Unit 175 begins the muscle count.",
            "पेशी = muscle: a new count."),
        mcq("apply", 4, "peśī also names a flesh-lump elsewhere. How does the data read it in unit 175?",
            ("As muscle", "The note: here peśī is read as muscle."),
            [("As a flesh-lump", "That sense belongs to embryology; here it is read as muscle."),
             ("As a sinew", "Sinews are snāva/snāyu, counted before; peśī is muscle."),
             ("As a bone", "Bones are asthi; peśī is read as muscle.")],
            "Here peśī = muscle.",
            "पेशी (here) = muscle."),
        mcq("transfer", 5, "By the pattern of पेशीशतानि (hundreds of muscles), what does अश्वशतानि mean in a new example?",
            ("Hundreds of horses", "X + शतानि = hundreds of X, as पेशीशतानि = hundreds of muscles."),
            [("The hundredth horse", "The hundredth would be शततम, not शतानि."),
             ("A horse of a hundred", "The first member names what is counted: hundreds of horses."),
             ("A hundred and one horses", "शतानि is hundreds; nothing adds one.")],
            "अश्वशतानि = hundreds of horses, like पेशीशतानि = hundreds of muscles.",
            "X-शतानि = hundreds of X.",
            teaches="In पेशीशतानि the first member names what is counted: 'hundreds of muscles'."),
    ],
}

# ---------------------------------------------------------------- unit 176
AUTHORED["176"] = {
    "title": "तासां चत्वारिशतानि शाखासु",
    "question": "By unit 176, how many of the muscles are in the limbs?",
    "rule": ("Of them (तासाम्, the five hundred peśī of unit 175), four hundred (चत्वारि शतानि) are in the limbs (शाखासु)."),
    "limits": ("Prose; no verb (copula understood); the counted peśī are carried from unit 175. The print runs चत्वारि "
               "शतानि together. The line does not divide the four hundred among the four limbs."),
    "explain_hi": ("यह गद्य-पंक्ति पाँच सौ पेशियों (इकाई १७५) में से पहला भाग देती है। "
                   "उनमें से (तासाम्) चार सौ शाखाओं यानी हाथ-पैरों में हैं। "
                   "तासाम् स्त्रीलिंग षष्ठी बहुवचन है, क्योंकि पेशी स्त्रीलिंग है। "
                   "छपाई में ‘चत्वारिशतानि’ जुड़ा है: चत्वारि शतानि, दो शब्द, कोई सन्धि नहीं। "
                   "चार सौ चारों अंगों में कैसे बँटे, यह यहाँ नहीं कहा गया।"),
    "hook": "पाँच सौ में चार सौ हाथ-पैरों में।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 176, how many muscles are in the limbs?",
            ("Four hundred", "चत्वारि शतानि शाखासु: four hundred in the limbs."),
            [("Six hundred", "Six hundred is the snāyu count of the limbs (unit 145)."),
             ("Sixty", "Sixty is the muscle count of the trunk (unit 177)."),
             ("Five hundred", "Five hundred is the total (unit 175), not the limbs.")],
            "Of the muscles, four hundred are in the limbs.",
            "चत्वारि शतानि = four hundred."),
        order(1, "Put the words of unit 176 in the line's order.",
              ["तासां", "चत्वारि", "शतानि", "शाखासु"],
              "Of them, four hundred in the limbs.",
              "तासां → चत्वारि → शतानि → शाखासु."),
        match(2, "Match each word of unit 176 to its meaning.",
              [["तासाम्", "of them"], ["चत्वारि", "four"], ["शतानि", "hundreds"], ["शाखासु", "in the limbs"]],
              "Of them, four hundred in the limbs.",
              "तासाम्, चत्वारि, शतानि, शाखासु.", role="extend",
              teaches="तासाम् = 'of them' (feminine plural): it points back to the peśī of unit 175."),
        mcq("discriminate", 3, "What does तासाम् (of them) refer to in unit 176?",
            ("The five hundred peśī (unit 175)", "The note: the counted item, peśī, is carried from unit 175."),
            [("The nine hundred snāyu (unit 144)", "The snāyu count is finished; this run counts peśī."),
             ("The limbs named in this line", "The limbs are where the four hundred are, not 'them'."),
             ("The bones counted much earlier", "The bones are not the subject here; the peśī are.")],
            "तासाम् = of the peśī.",
            "तासाम् → पेश्यः (unit 175)."),
        mcq("apply", 4, "How does the data read the printed चत्वारिशतानि in unit 176?",
            ("चत्वारि शतानि, two words run together", "The note: catvāri śatāni, two words run together."),
            [("One word meaning the four-hundredth", "The data reads two words, four hundreds."),
             ("चत्वारिंशत्, forty, with a lost dot", "The data reads चत्वारि शतानि, four hundred."),
             ("A sandhi of the two parts चत्वार् and इशतानि", "There is no such word; it is चत्वारि + शतानि.")],
            "चत्वारि (four) शतानि (hundreds): no sandhi, just run together.",
            "चत्वारिशतानि (printed) = चत्वारि शतानि."),
        mcq("transfer", 5, "By the pattern of तासां चत्वारि शतानि (of them, four hundred), what does फलानां त्रीणि mean in a new example?",
            ("Of the fruits, three", "A genitive plural + a number = so many of them, as तासां चत्वारि शतानि."),
            [("Three fruits each", "Each would need a repeated number, as द्वे द्वे."),
             ("With three fruits", "'With' would be the instrumental, not the genitive."),
             ("In the three fruits", "'In' would be the locative, not the genitive.")],
            "फलानां त्रीणि = of the fruits, three.",
            "genitive plural + number = so many of them.",
            teaches="तासाम् is a genitive of the whole: 'of them, four hundred'."),
    ],
}

# ---------------------------------------------------------------- unit 177
AUTHORED["177"] = {
    "title": "षष्टिरंतराधौ",
    "question": "By unit 177, how many muscles are in the trunk?",
    "rule": ("Sixty (षष्टिः) in the trunk (अन्तराधौ, antarādhi, standard). The counted peśī are carried from unit 175. "
             "Printed as one word: इः before a vowel becomes इर्."),
    "limits": ("Prose, one printed word; no verb and no counted noun printed."),
    "explain_hi": ("यह एक छपे शब्द की गद्य-पंक्ति है: साठ, अन्तराधि यानी धड़ में। "
                   "गिनी गई वस्तु पेशी है, जो इकाई १७५ से चली आ रही है। "
                   "‘षष्टिरंतराधौ’ = षष्टिः + अन्तराधौ; स्वर से पहले इः का विसर्ग र् बना। "
                   "षष्टि (साठ) स्त्रीलिंग एकवचन संख्या-शब्द है, यद्यपि वह बहुत-सी वस्तुएँ गिनता है।"),
    "hook": "धड़ में साठ पेशियाँ।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 177, how many muscles are in the trunk?",
            ("Sixty", "षष्टिरंतराधौ: sixty in the trunk."),
            [("Two hundred and thirty", "That is the snāyu count of the trunk (unit 146)."),
             ("Forty", "Forty is the count 'above' (unit 178)."),
             ("Four hundred", "Four hundred is the muscle count of the limbs (unit 176).")],
            "Sixty muscles in the trunk.",
            "षष्टिः = sixty; अन्तराधौ = in the trunk."),
        match(1, "Match each part of unit 177 to its meaning.",
              [["षष्टिः", "sixty"], ["अन्तराधि", "trunk"], ["अन्तराधौ", "in the trunk"]],
              "षष्टिः + अन्तराधौ = षष्टिरन्तराधौ: sixty in the trunk.",
              "षष्टिः, अन्तराधि, अन्तराधौ."),
        fill(2, "In unit 177 the number 'sixty' is ____ (type it in Devanagari or in English letters, e.g. dharma).",
             accepts("षष्टिः", "ṣaṣṭiḥ", "षष्टि", "sixty"),
             "षष्टिः = sixty; before a vowel it is printed षष्टिर्.",
             "षष्टि = sixty.",
             "षष्टिः + अन्तराधौ → षष्टिरन्तराधौ."),
        mcq("discriminate", 3, "Which split of षष्टिरंतराधौ in unit 177 is right?",
            ("षष्टिः + अन्तराधौ", "A visarga after इ becomes र् before a vowel: षष्टिर् + अन्तराधौ."),
            [("षष्टि + रन्तराधौ", "रन्तराधौ is not a word; the word is अन्तराधौ (in the trunk)."),
             ("षष्टः + अन्तराधौ", "अः + अ would give षष्टोऽन्तराधौ, and the word is षष्टिः."),
             ("षष्टे + अन्तराधौ", "ए + अ would give षष्टेऽन्तराधौ, not षष्टिर-.")],
            "षष्टिः (sixty) + अन्तराधौ (in the trunk): इः + vowel → इर्.",
            "इः + vowel → इर्."),
        mcq("apply", 4, "Why is षष्टिः singular in unit 177 though it counts many muscles?",
            ("Numbers from twenty up are singular nouns", "षष्टि is a feminine singular number-noun (data: f. nom. sg.)."),
            [("It counts only one muscle in the trunk", "It counts sixty; the singular is the number-word's own."),
             ("The print has lost its plural ending", "No ending is lost; षष्टिः is the normal form."),
             ("It is a dual, for the two sides of the trunk", "The data reads nominative singular, not dual.")],
            "षष्टिः is grammatically singular: number-words from विंशति up are singular nouns.",
            "विंशति, त्रिंशत्, षष्टि ... = singular feminine nouns."),
        mcq("transfer", 5, "By the rule of षष्टिः + अन्तराधौ, how is हरिः + अपि (Hari also) joined?",
            ("हरिरपि", "A visarga after इ becomes र् before a vowel, as षष्टिः + अन्तराधौ."),
            [("हर्यपि", "इ → य् happens without a visarga; हरिः keeps its र्."),
             ("हरोऽपि", "ओऽ comes from अः + अ, not from इः."),
             ("हरिः अपि", "Before a vowel the visarga after इ does not stay.")],
            "हरिः + अपि = हरिरपि, like षष्टिः + अन्तराधौ = षष्टिरन्तराधौ.",
            "इः + vowel → इर्.",
            teaches="A visarga after इ becomes र् before a vowel: षष्टिः + अन्तराधौ → षष्टिरन्तराधौ."),
    ],
}

# ---------------------------------------------------------------- unit 178
AUTHORED["178"] = {
    "title": "चत्वारिंशदूर्ध्वं",
    "question": "By unit 178, what number is given 'above'?",
    "rule": ("Forty (चत्वारिंशत्) above (ऊर्ध्वम्). The counted peśī are carried from unit 175. The data reads 'above' as the "
             "part above the trunk, as in ऊर्ध्वं सप्ततिः (unit 147); the Sanskrit says only 'above'."),
    "limits": ("Prose, one printed word; no verb and no counted noun printed. 'Above the trunk' is the data's reading; no "
               "body part is printed."),
    "explain_hi": ("यह एक छपे शब्द की गद्य-पंक्ति है: चालीस, ऊपर। "
                   "गिनी गई वस्तु पेशी है, इकाई १७५ से चली आ रही। "
                   "‘ऊपर’ को डेटा धड़ से ऊपर का भाग मानता है, जैसे इकाई १४७ में स्नायुओं के लिए ‘ऊर्ध्वं सप्ततिः’; पर संस्कृत केवल ‘ऊपर’ कहती है। "
                   "‘चत्वारिंशदूर्ध्वं’ = चत्वारिंशत् + ऊर्ध्वम्; स्वर से पहले त् का द् हुआ।"),
    "hook": "ऊपर चालीस पेशियाँ।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 178, what number of muscles is given 'above'?",
            ("Forty", "चत्वारिंशदूर्ध्वं: forty above."),
            [("Seventy", "Seventy above is the snāyu count (unit 147)."),
             ("Sixty", "Sixty is the trunk's muscle count (unit 177)."),
             ("Four", "चत्वारिंशत् is forty; four is चत्वारि.")],
            "Forty above.",
            "चत्वारिंशत् = forty; ऊर्ध्वम् = above."),
        match(1, "Match each part of unit 178 to its meaning.",
              [["चत्वारिंशत्", "forty"], ["ऊर्ध्वम्", "above"], ["चत्वारिंशदूर्ध्वम्", "forty above"]],
              "चत्वारिंशत् + ऊर्ध्वम् = चत्वारिंशदूर्ध्वम्: forty above.",
              "चत्वारिंशत्, ऊर्ध्वम्."),
        fill(2, "In unit 178 the word for 'above' is ____ (type it in Devanagari or in English letters, e.g. dharma).",
             accepts("ऊर्ध्वम्", "ūrdhvam", "urdhvam", "urdhvam"),
             "ऊर्ध्वम् (printed ऊर्ध्वं) = above.",
             "ऊर्ध्वम् = above, an indeclinable here.",
             "चत्वारिंशत् + ऊर्ध्वम् → चत्वारिंशदूर्ध्वम्."),
        mcq("discriminate", 3, "Which split of चत्वारिंशदूर्ध्वं in unit 178 is right?",
            ("चत्वारिंशत् + ऊर्ध्वम्", "त् before a vowel becomes द्: चत्वारिंशद् + ऊर्ध्वम्."),
            [("चत्वारिंश + दूर्ध्वम्", "दूर्ध्वम् is not a word; the word is ऊर्ध्वम् (above)."),
             ("चत्वारि + शदूर्ध्वम्", "शदूर्ध्वम् is not a word; the number is चत्वारिंशत्."),
             ("चत्वारिंशत् + दूर्ध्वम्", "दूर्ध्वम् is not a word; the द् comes from the त्.")],
            "चत्वारिंशत् (forty) + ऊर्ध्वम् (above): त् + vowel → द्.",
            "त् + vowel → द्."),
        mcq("apply", 4, "Which statement about ऊर्ध्वम् in unit 178 is right?",
            ("The data reads it as above the trunk", "The note: read as the part above the trunk, as in unit 147."),
            [("The print names the head and neck", "No body part is printed; only 'above'."),
             ("It is a locative: in the upper arm", "The data reads an indeclinable, 'above'."),
             ("It points back to the limbs named in unit 176", "The note reads the part above the trunk, not the limbs.")],
            "ऊर्ध्वम् = above, read as above the trunk; the Sanskrit says only 'above'.",
            "ऊर्ध्वम् = above (the trunk, by the data's reading)."),
        mcq("transfer", 5, "By the rule of चत्वारिंशत् + ऊर्ध्वम्, how is जगत् + ईशः (lord of the world) joined?",
            ("जगदीशः", "त् before a vowel becomes द्, as चत्वारिंशत् + ऊर्ध्वम्."),
            [("जगतीशः", "Before a vowel the final त् becomes द्; it does not stay त्."),
             ("जगन्नीशः", "न् would come before a nasal, not before a vowel."),
             ("जगच्चीशः", "च्च comes from त् before च, not before a vowel.")],
            "जगत् + ईशः = जगदीशः, like चत्वारिंशत् + ऊर्ध्वम् = चत्वारिंशदूर्ध्वम्.",
            "त् + vowel → द्.",
            teaches="Final त् before a vowel becomes द्: चत्वारिंशत् + ऊर्ध्वम् → चत्वारिंशदूर्ध्वम्."),
    ],
}


# ===================================================================== NOTES_HI
NOTES_HI = {
    "166": ("गद्य; विश्वास उच्च। पाठ-चिह्न: छपा ‘जिव्हायां’ = जिह्वायाम् (ह/व का क्रम उलटा, इस छपाई की आदत; डेटा में सामान्य किया गया)। "
            "गिनी गई वस्तु (स्नायु) और क्रिया छपी नहीं; स्नायु इकाई १४४ की गिनती से। छपा पंच = पञ्च; पंक्ति के अन्त में ं = म्।"),
    "167": ("गद्य; विश्वास उच्च; कोई पाठ-चिह्न नहीं। गिनी गई वस्तु (स्नायु, इकाई १४४ से) और क्रिया छपी नहीं। उत्तर और अधर विशेषण हैं, "
            "दन्तमांसेषु से सप्तमी बहुवचन में मेल। सन्धि जाँची: द्वादश + उत्तर → द्वादशोत्तर (अ + उ → ओ); उत्तर + अधरेषु → उत्तराधरेषु "
            "(अ + अ → आ); छपा दंत = दन्त। बारह ऊपर-नीचे में कैसे बँटे, नहीं कहा गया।"),
    "168": ("गद्य; विश्वास उच्च; कोई पाठ-चिह्न नहीं। छपा दोहरा ‘-र्द्ध-’ छपाई की आदत, डेटा में मूर्धनि। गिनी गई वस्तु (स्नायु) और क्रिया छपी नहीं। "
            "सन्धि जाँची: षट् + मूर्धनि → षण्मूर्धनि (नासिक्य म से पहले ट् → ण्; यह विकल्प से, षड्मूर्धनि भी शुद्ध)।"),
    "169": ("गद्य, दो छपी पंक्तियाँ जोड़ी गईं; विश्वास मध्यम; कोई पाठ-चिह्न नहीं। क्रिया समझी जाती है। स्नाव = स्नायु का दूसरा रूप "
            "(सम्भवतः लिगामेंट या टेंडन, सम्भावित); कण्डरा = टेंडन (सम्भावित)। ‘तत्र’ = उनमें (स्वाभाविक पाठ) या ‘वहाँ’। प्रतान = लता का तन्तु, "
            "पर पाठ लता से तुलना नहीं करता। छपा ‘वृत्तानितानि’ = वृत्तानि तानि (दो शब्द, कोई सन्धि नहीं)। छपा प्रतानवंति = प्रतानवन्ति, "
            "कंडरा = कण्डरा।"),
    "170": ("गद्य; विश्वास मध्यम; कोई पाठ-चिह्न नहीं। ‘आमपक्वाशय’ सम्भवतः आमाशय और पक्वाशय का संक्षिप्त द्वन्द्व; आमाशय = जठर, पक्वाशय = बड़ी आँत "
            "(दोनों सम्भावित)। बस्ति = मूत्राशय (मानक; देखें इकाई १५६)। सन्धि जाँची: बस्ति + आम → बस्त्याम (इ + आ → या); "
            "आशय + अन्त्रेषु → आशयान्त्रेषु (अ + अ → आ); छपा ‘यांत्रेषु’ = यान्त्रेषु।"),
    "171": ("गद्य; विश्वास उच्च; कोई पाठ-चिह्न नहीं। गिनी गई वस्तु (स्नायु) और क्रिया छपी नहीं; कोई संख्या नहीं। सन्धि जाँची: पृष्ठ + उरः → पृष्ठोरः "
            "(अ + उ → ओ); समास के भीतर उरः और शिरः का विसर्ग श/स से पहले छपा है।"),
    "172": ("गद्य; विश्वास मध्यम। पाठ-चिह्न (सम्भावित): छपा ‘सम्यग्गीहते’ का दोहरा ग सम्भवतः छपाई की भूल; सम्यक् + ईहते = सम्यगीहते। "
            "ईहते = चेष्टा करता है (चुना गया), ‘ठीक से चलता है’ विकल्प। तनु (शरीर) और नौ (नाव) स्त्रीलिंग, सुबद्धा से मेल। सन्धि जाँची: "
            "बन्धनैः + हि → बन्धनैर्हि, तनुः + नौः → तनुर्नौः, नौः + इव → नौरिव (अ/आ के अतिरिक्त स्वर के बाद विसर्ग → र्, घोष ध्वनि से पहले)।"),
    "173": ("गद्य; विश्वास मध्यम; कोई पाठ-चिह्न नहीं। ‘से भी अधिक’ = अपादान (तुलना) + अपि, डेटा का पाठ; ‘अस्थि-सिरा आदि की चोट से भी बचाना’ "
            "कम स्वाभाविक विकल्प। तानि = पिछली इकाइयों के स्नायु। सिरा = वाहिनी (सम्भावित)। सन्धि जाँची: तस्मात् + अस्थि → तस्मादस्थि "
            "(त् + स्वर → द्); आदिभ्यः + अपि → आदिभ्योऽपि (अः + अ → ओऽ); यत्नतः + रक्षेत् → यत्नतो रक्षेत् (अः + घोष व्यंजन → ओ)।"),
    "174": ("गद्य; विश्वास उच्च; कोई पाठ-चिह्न नहीं। छपा ‘आहर्त्तुं’ (दोहरा त) छपाई की आदत, डेटा में आहर्तुम्। शल्य = शरीर में घुसी बाहरी वस्तु "
            "(मानक)। सन्धि जाँची: यः + च → यश्च (च से पहले विसर्ग → श्); बाह्यानि + अभ्यन्तराणि → बाह्यान्यभ्यन्तराणि (इ + अ → य); "
            "सम्यक् + जानाति → सम्यग्जानाति (घोष ज से पहले क् → ग्); सः + गूढम् → स गूढम् (सः का विसर्ग व्यंजन से पहले लुप्त); "
            "समर्थः + भवति → समर्थो भवति (अः + घोष व्यंजन → ओ)।"),
    "175": ("गद्य; विश्वास उच्च; कोई पाठ-चिह्न नहीं। समूह-टिप्पणी: इकाई १४४-१७४ की स्नायु-गिनती के बाद पेशियों की नई गिनती प्रतीत होती है। "
            "पेशी अन्यत्र (गर्भ-विकास में) मांस-पिण्ड भी; यहाँ मांसपेशी। क्रिया समझी जाती है। छपा पंच = पञ्च।"),
    "176": ("गद्य; विश्वास उच्च; कोई पाठ-चिह्न नहीं। गिनी गई वस्तु (पेशी, इकाई १७५ से) और क्रिया छपी नहीं। छपा ‘चत्वारिशतानि’ = चत्वारि शतानि "
            "(दो शब्द, कोई सन्धि नहीं)। इकाई १७६-१७८ के अंक ४०० + ६० + ४० = ५०० होते हैं; यह केवल गणना है, पाठ यह जोड़ स्वयं नहीं कहता।"),
    "177": ("गद्य; विश्वास उच्च; कोई पाठ-चिह्न नहीं। गिनी गई वस्तु (पेशी, इकाई १७५ से) और क्रिया छपी नहीं। अन्तराधि = धड़ (मानक)। "
            "सन्धि जाँची: षष्टिः + अन्तराधौ → षष्टिरन्तराधौ (इः + स्वर → इर्); छपा ‘रंत’ = रन्त।"),
    "178": ("गद्य; विश्वास उच्च; कोई पाठ-चिह्न नहीं। गिनी गई वस्तु (पेशी) और क्रिया छपी नहीं। ‘ऊर्ध्वम्’ को धड़ से ऊपर का भाग पढ़ा गया, इकाई १४७ "
            "(ऊर्ध्वं सप्ततिः) के अनुसार; संस्कृत केवल ‘ऊपर’ कहती है। सन्धि जाँची: चत्वारिंशत् + ऊर्ध्वम् → चत्वारिंशदूर्ध्वम् (त् + स्वर → द्); "
            "पंक्ति के अन्त में ं = म्।"),
}


# ===================================================================== AIDS
AIDS = {
    "166": {
        "chunks": "पंच | जिव्हायां",
        "letters": "छपा ‘जिव्हा’ = जिह्वा: ह और व का क्रम उलटा। शुद्ध रूप में पहले ह, फिर व।",
        "frame": "संख्या: पञ्च (पाँच) → स्थान: जिह्वायाम् (जीभ में) → वस्तु: स्नायु (इकाई १४४ से, छपी नहीं)।",
    },
    "167": {
        "chunks": "द्वादशोत्तराधरेषु | दंतमांसेषु",
        "sandhi": "अ + उ → ओ: द्वादश + उत्तर → द्वादशोत्तर · अ + अ → आ: उत्तर + अधरेषु → उत्तराधरेषु।",
        "frame": "संख्या: द्वादश (बारह) → कौन-से: उत्तर-अधर (ऊपर-नीचे के) → स्थान: दन्तमांसेषु (मसूड़ों में)।",
        "letters": "दन्त + मांस = ‘दाँत का मांस’ = मसूड़े: शब्द स्वयं अर्थ बताता है।",
    },
    "168": {
        "chunks": "षण् | मूर्द्धनि",
        "sandhi": "नासिक्य म से पहले ट् → ण् (विकल्प से): षट् + मूर्धनि → षण्मूर्धनि।",
        "frame": "संख्या: षट् (छह) → स्थान: मूर्धनि (सिर में) → वस्तु: स्नायु (छपी नहीं)।",
    },
    "169": {
        "diagram": {"groups": [
            {"label": "शाखाओं व सन्धियों में", "items": ["प्रतानवत् (फैली शाखाओं वाले)"]},
            {"label": "बड़े और गोल स्नायु", "items": ["कण्डरा नाम (सम्भवतः टेंडन)"]}]},
        "chunks": "तत्र शाखासु संधिषु च | प्रतानवंति | महास्नावानि तु | वृत्तानितानि | कंडरासंज्ञानि",
        "contrast": "‘तु’ (पर) दो समूहों को अलग करता है: हाथ-पैर व जोड़ों के फैले हुए (प्रतानवत्) बनाम बड़े गोल (कण्डरा)।",
        "frame": "कहाँ: शाखा, सन्धि → कैसे: प्रतानवत् · कौन: महास्नाव, वृत्त → नाम: कण्डरा।",
    },
    "170": {
        "diagram": {"groups": [
            {"label": "सुषिर (खोखले) स्नायु, क्रम से", "items": ["बस्ति (मूत्राशय)", "आमाशय (सम्भवतः जठर)",
                                                          "पक्वाशय (सम्भवतः बड़ी आँत)", "अन्त्र (आँतें)"]}]},
        "chunks": "बस्त्याम | पक्वाशयांत्रेषु | सुषिराणि",
        "sandhi": "इ + आ → या: बस्ति + आम → बस्त्याम · अ + अ → आ: आशय + अन्त्रेषु → आशयान्त्रेषु।",
        "seesaw": "आम (कच्चा) ↔ पक्व (पका): एक ही शब्द में दोनों आशय, कच्चे और पके के स्थान।",
    },
    "171": {
        "diagram": {"groups": [
            {"label": "पृथु (चौड़े) स्नायु, क्रम से", "items": ["पार्श्व (बगल)", "पृष्ठ (पीठ)", "उरस् (छाती)", "शिरस् (सिर)"]}]},
        "chunks": "पार्श्वपृष्ठोरःशिरःसु | पृथूनि",
        "sandhi": "अ + उ → ओ: पृष्ठ + उरः → पृष्ठोरः।",
        "pegs": "चौड़ी जगहें, चौड़े स्नायु: बगल, पीठ, छाती, सिर, सब शरीर के चौड़े भाग। (मेरी याद-पद्धति)",
    },
    "172": {
        "chain": {"steps": ["स्नायु के बन्धन", "सन्धियों में सुबद्ध शरीर", "नाव की तरह", "ठीक से चेष्टा करता है"]},
        "chunks": "स्नावबंधनैर्हि | संधिषु | सुबद्धा | तनुर्नौरिव | सम्यग्गीहते",
        "sandhi": "अ/आ के अतिरिक्त स्वर के बाद विसर्ग, घोष ध्वनि से पहले → र्: बन्धनैः + हि → बन्धनैर्हि, तनुः + नौः → तनुर्नौः, नौः + इव → नौरिव।",
        "story": "रस्सियों से कसकर बँधी नाव पानी में ठीक चलती है; वैसे ही स्नायुओं से जोड़ों पर बँधा शरीर। (मेरा बनाया चित्र; पाठ केवल ‘नाव की तरह’ कहता है)",
    },
    "173": {
        "chunks": "तस्मादस्थिसिरादिभ्योऽपि | तानि | यत्नतो | रक्षेत्",
        "sandhi": "त् + स्वर → द्: तस्मात् + अस्थि → तस्मादस्थि · अः + अ → ओऽ: आदिभ्यः + अपि → आदिभ्योऽपि · अः + घोष व्यंजन → ओ: यत्नतः + रक्षेत् → यत्नतो रक्षेत्।",
        "frame": "क्यों: तस्मात् (इसलिए) → किनकी: तानि (स्नायु) → कैसे: यत्नतः (यत्न से) → क्या करे: रक्षेत् (रक्षा करे)।",
    },
    "174": {
        "chain": {"steps": ["बाहरी और भीतरी स्नायु", "जो भली-भाँति जानता है", "वह छिपा शल्य भी", "निकालने में समर्थ"]},
        "chunks": "यश्च स्नावानि | बाह्यान्यभ्यंतराणि च | सम्यग्जानाति | स गूढमपि शल्यमाहर्त्तुं | समर्थो भवति",
        "seesaw": "बाह्य (बाहरी) ↔ अभ्यन्तर (भीतरी): दोनों प्रकार के स्नायु जानने हैं।",
        "frame": "यः (जो) ... जानाति → सः (वह) ... समर्थो भवति: जो-वह का जोड़ा।",
    },
    "175": {
        "chunks": "पंच | पेशीशतानि",
        "frame": "संख्या: पञ्च शतानि (पाँच सौ) → वस्तु: पेशी (मांसपेशी) → नई गिनती, स्नायुओं के बाद।",
        "anchors": "‘पेशी’ से हिन्दी ‘मांसपेशी’: वही शब्द आज भी।",
    },
    "176": {
        "chunks": "तासां | चत्वारिशतानि | शाखासु",
        "frame": "किनमें से: तासाम् (पेशियों में से) → संख्या: चत्वारि शतानि (चार सौ) → स्थान: शाखासु (हाथ-पैरों में)।",
        "anchors": "चार शाखाएँ (दो हाथ, दो पैर), चार सौ पेशियाँ: चार से चार। (मेरी याद-पद्धति; पाठ बँटवारा नहीं कहता)",
    },
    "177": {
        "chunks": "षष्टिर् | अंतराधौ",
        "sandhi": "इः + स्वर → इर्: षष्टिः + अन्तराधौ → षष्टिरन्तराधौ।",
        "frame": "संख्या: षष्टिः (साठ) → स्थान: अन्तराधौ (धड़ में) → वस्तु: पेशी (छपी नहीं)।",
    },
    "178": {
        "chunks": "चत्वारिंशद् | ऊर्ध्वं",
        "sandhi": "त् + स्वर → द्: चत्वारिंशत् + ऊर्ध्वम् → चत्वारिंशदूर्ध्वम्।",
        "frame": "संख्या: चत्वारिंशत् (चालीस) → स्थान: ऊर्ध्वम् (ऊपर; डेटा: धड़ से ऊपर) → वस्तु: पेशी (छपी नहीं)।",
    },
}


# ===================================================================== IMAGE_SPECS
IMAGE_SPECS = {
    ("169", "diagram"): {
        "file": "sh5-pratana-kandara-169.svg",
        "alt": ("Two columns of unit 169: in the limbs and joints, tendrilled (pratānavat, with spreading branches); the "
                "large round sinews, called kaṇḍarā (probably tendons)."),
        "type": "split",
        "title": "इकाई १६९: प्रतानवत् और कण्डरा",
        "cols": [["शाखाओं व सन्धियों में", ["प्रतानवत्", "(फैली शाखाओं वाले)"]],
                 ["बड़े और गोल स्नायु", ["कण्डरा नाम", "(सम्भवतः टेंडन)"]]],
    },
    ("170", "diagram"): {
        "file": "sh5-sushira-170.svg",
        "alt": ("Table of unit 170, places of the hollow (suṣira) sinews in line order: bladder (basti); āmāśaya, probably "
                "the stomach; pakvāśaya, probably the large intestine; intestines (antra)."),
        "type": "table",
        "title": "इकाई १७०: सुषिर (खोखले) स्नायु",
        "heads": ["स्थान (क्रम से)", "अर्थ"],
        "rows": [["बस्ति", "मूत्राशय"], ["आमाशय", "सम्भवतः जठर"], ["पक्वाशय", "सम्भवतः बड़ी आँत"], ["अन्त्र", "आँतें"]],
    },
    ("171", "diagram"): {
        "file": "sh5-prithu-171.svg",
        "alt": ("Table of unit 171, places of the broad (pṛthu) sinews numbered in line order: 1 sides (pārśva), 2 back "
                "(pṛṣṭha), 3 chest (uras), 4 head (śiras)."),
        "type": "table",
        "title": "इकाई १७१: पृथु (चौड़े) स्नायु",
        "heads": ["क्रम", "स्थान"],
        "rows": [["१", "पार्श्व (बगल)"], ["२", "पृष्ठ (पीठ)"], ["३", "उरस् (छाती)"], ["४", "शिरस् (सिर)"]],
    },
    ("172", "chain"): {
        "file": "sh5-nau-172.svg",
        "alt": ("Flowchart of unit 172: the bonds of sinew; the body well bound in the joints; like a boat; it acts "
                "properly."),
        "type": "mermaid",
        "code": ("flowchart TD\n"
                 "  A[\"स्नायु के बन्धन\"] --> B[\"सन्धियों में सुबद्ध शरीर\"]\n"
                 "  B --> C[\"नाव की तरह\"]\n"
                 "  C --> D[\"ठीक से चेष्टा करता है\"]\n"),
    },
    ("174", "chain"): {
        "file": "sh5-shalya-174.svg",
        "alt": ("Flowchart of unit 174: the sinews, external and internal; he who knows them well; he becomes able to "
                "extract even a hidden śalya (foreign body)."),
        "type": "mermaid",
        "code": ("flowchart TD\n"
                 "  A[\"बाहरी और भीतरी स्नायु\"] --> B[\"जो भली-भाँति जानता है\"]\n"
                 "  B --> C[\"वह छिपा शल्य भी\"]\n"
                 "  C --> D[\"निकालने में समर्थ\"]\n"),
    },
}
