from helpers import mcq, match, order, fill, multi, accepts


def T(q, teaches):
    q["teaches"] = teaches
    return q


AUTHORED = {}

# ---------------------------------------------------------------- unit 1
AUTHORED["1"] = {
    "title": "अथातो मर्मविभागं शारीरं व्याख्यास्यामः",
    "question": "What does unit 1 announce that this chapter will explain?",
    "rule": ("The chapter opens: 'Now, therefore, we shall explain the Śārīra called Marmavibhāga', the division of the "
             "marmas (vital points of the body). व्याख्यास्यामः is a future: 'we shall explain'."),
    "limits": ("Prose opening formula. शारीरम् is read as the name of the section; it could also be an adjective 'bodily' "
               "with विभागम्, so no question rests on its role. Marma is kept as a doctrinal term with a short gloss, not "
               "given a modern equivalent."),
    "explain_hi": ("यह अध्याय की आरम्भिक गद्य-पंक्ति है: ‘अब इसलिए हम मर्मविभाग शारीर की व्याख्या करेंगे’। "
                   "मर्म यानी शरीर के प्राणस्थान; विभाग यानी उनका बँटवारा। "
                   "‘शारीरम्’ को इस भाग (शारीरस्थान) के अध्याय का नाम माना गया है; इसे ‘शारीरिक’ विशेषण भी पढ़ा जा सकता है। "
                   "‘व्याख्यास्यामः’ भविष्यत् काल, उत्तम पुरुष बहुवचन है: हम व्याख्या करेंगे। "
                   "‘अथातो’ में अथ + अतः (अ + अ → आ) है, और अतः का विसर्ग घोष व्यंजन म से पहले ओ बना है।"),
    "hook": "अथातो... व्याख्यास्यामः: अब मर्मों का विभाग।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 1, what does this chapter announce it will explain?",
            ("The division of the marmas", "मर्मविभागम्: the division of the marmas (vital points of the body)."),
            [("The division of the sirās (vessels)", "Unit 1 names the marmas, not the sirās."),
             ("The signs of approaching death", "Unit 1 names the division of the marmas, not signs of death."),
             ("The growth of the embryo month by month", "Unit 1 names the division of the marmas, not the embryo.")],
            "अथातो मर्मविभागं शारीरं व्याख्यास्यामः: the division of the marmas.",
            "मर्म-विभाग = division of the marmas."),
        order(1, "Put the words of unit 1 in the printed order.",
              ["अथातो", "मर्मविभागं", "शारीरं", "व्याख्यास्यामः"],
              "Now therefore; the division of the marmas; the Śārīra; we shall explain.",
              "अथातो → मर्मविभागं → शारीरं → व्याख्यास्यामः."),
        match(2, "Match each word of unit 1 to its meaning.",
              [["अथ", "now"], ["अतः", "therefore"], ["मर्म", "vital point of the body"], ["विभाग", "division"],
               ["व्याख्यास्यामः", "we shall explain"]],
              "अथ = now, अतः = therefore, मर्म-विभाग = division of the marmas, व्याख्यास्यामः = we shall explain.",
              "अथ, अतः, मर्म, विभाग, व्याख्यास्यामः.", role="extend",
              teaches="व्याख्यास्यामः is the future, first person plural, of वि-आ-√ख्या: 'we shall explain'."),
        mcq("discriminate", 3, "Which split of अथातो in unit 1 is right?",
            ("अथ + अतः", "अ + अ → आ: अथ + अतः → अथातः, printed अथातो before म."),
            [("अथ + इतः", "अ + इ gives ए: that would be अथेतः."),
             ("अथ + उतः", "अ + उ gives ओ: that would be अथोतः."),
             ("अथः + अतः", "अः before अ gives ओऽ: that would be अथोऽतः.")],
            "अथ (now) + अतः (therefore): अ + अ → आ.",
            "अ + अ → आ."),
        mcq("apply", 4, "Why is अतः printed अतो before मर्मविभागं in unit 1?",
            ("अः before a voiced consonant → ओ", "म is a voiced consonant: अतः + मर्म → अतो मर्म."),
            [("अः before any consonant (म too) → ओ", "Not before every consonant: before त it becomes स्, before च श्."),
             ("ओ is a case ending added to अतः", "अतः is an indeclinable (gram: ind.); it takes no case ending."),
             ("The visarga after अ becomes ओ at a pause", "At a pause the visarga stays ः; here a word follows.")],
            "अतः + मर्मविभागम्: अः before the voiced consonant म → ओ.",
            "अः + voiced consonant → ओ."),
        mcq("transfer", 5, "By the pattern of व्याख्यास्यामः (we shall explain), which form of √वद् means we shall speak, in a new example?",
            ("वदिष्यामः", "-स्यामः / -इष्यामः is the future, first person plural: we shall speak."),
            [("वदामः", "वदामः is the present: we speak."),
             ("वदिष्यन्ति", "वदिष्यन्ति is future, but third person: they will speak."),
             ("अवदाम", "अवदाम is the past (imperfect): we spoke.")],
            "वदिष्यामः = we shall speak, like व्याख्यास्यामः = we shall explain.",
            "Future, 1st person plural: -(इ)ष्यामः / -स्यामः.",
            teaches="The future first person plural ends in -स्यामः (after इ: -इष्यामः): व्याख्यास्यामः, वदिष्यामः."),
    ],
}

# ---------------------------------------------------------------- unit 2
AUTHORED["2"] = {
    "title": "मर्मशतं",
    "question": "What does unit 2 say about the number of the marmas, and what part of it is sure?",
    "rule": ("Unit 2 speaks of a hundred marmas (मर्मशतम्) with a number word before it. The printed समोत्तरं gives no "
             "usable sense; the data reads it, by conjecture, as सप्तोत्तरम्: a hundred with seven more (107)."),
    "limits": ("Prose, no verb. The total 107 rests on a conjectural reading (सप्त for the printed सम) and on the sum of "
               "unit 3; no question rests on the number seven or on 107. Only मर्मशतं (a hundred marmas) is asked. The "
               "count appears to continue in unit 3."),
    "explain_hi": ("यह छोटी गद्य-पंक्ति मर्मों की कुल संख्या बताती है और इकाई ३ की गिनती को खोलती दिखती है। "
                   "‘मर्मशतं’ यानी सौ मर्म, यह भाग पक्का है। "
                   "उसके पहले छपा ‘समोत्तरं’ कोई उपयोगी अर्थ नहीं देता; डेटा अनुमान से ‘सप्तोत्तरम्’ (सौ और सात अधिक, यानी एक सौ सात) पढ़ता है, क्योंकि इस छपाई में प्त का म बनना देखा गया है और इकाई ३ का जोड़ ४४ + २६ + ३७ = १०७ बैठता है। "
                   "यह संख्या अनुमानित पाठ पर टिकी है, इसलिए प्रश्न केवल ‘सौ मर्म’ पर हैं। "
                   "पंक्ति में कोई क्रिया नहीं है और कोई जोड़ी नहीं गई।"),
    "hook": "मर्मशतं: सौ तो पक्के, ऊपर के सात अनुमान से।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "In मर्मशतं of unit 2, what does शत mean?",
            ("A hundred", "शतम् = a hundred: मर्मशतम्, a hundred marmas."),
            [("A thousand", "A thousand is सहस्र, not शत."),
             ("Fifty", "Fifty is पञ्चाशत्, not शत."),
             ("Ten", "Ten is दश, not शत.")],
            "शतम् = a hundred.",
            "शत = hundred."),
        match(1, "Match each sure word of unit 2 to its meaning.",
              [["मर्म", "vital point of the body"], ["शत", "a hundred"], ["मर्मशतम्", "a hundred marmas"]],
              "मर्म = vital point; शत = hundred; मर्मशतम् = a hundred marmas.",
              "मर्म, शत, मर्मशतम्."),
        T(multi("extend", 2, "Which statements fit unit 2?",
                [("The line has no verb, and none is supplied", "Right: a nominal statement with no verb."),
                 ("The line names where the marmas lie", "Where they lie comes in unit 3, not here."),
                 ("मर्मशतं speaks of a hundred marmas", "Right: मर्म-शतम्, a hundred marmas."),
                 ("Every word of the line is printed without doubt", "The printed समोत्तरं is doubtful (a conjectural reading).")],
                [0, 2],
                "No verb; a hundred marmas; the number word before it is doubtful.",
                "समोत्तरं (doubtful) मर्मशतं (a hundred marmas)."),
          "A line may state a count with no verb at all; the copula is not supplied."),
        mcq("discriminate", 3, "What does मर्मशतं mean in unit 2?",
            ("A hundred marmas", "मर्म-शतम्: a hundred of marmas."),
            [("The hundredth marma", "The hundredth would be an ordinal (शततम); शतम् is the number."),
             ("A marma a hundred aṅgulas long", "No size is given in unit 2."),
             ("One marma with a hundred names", "No names are given in unit 2.")],
            "मर्मशतम् = a hundred marmas.",
            "X-शतम् = a hundred X's."),
        mcq("apply", 4, "Why does the card give no firm total for the marmas in unit 2?",
            ("The number word before मर्मशतं is doubtful", "the printed समोत्तरं gives no sense; सप्तोत्तरम् is a conjecture."),
            [("The line gives no number word at all", "शतम् (a hundred) is printed and sure."),
             ("The line gives two different totals", "Only one count is printed in unit 2."),
             ("The line counts only the trunk's marmas", "Unit 2 gives the whole count; the parts come in unit 3.")],
            "Only 'a hundred' is sure; the added number rests on a conjectural reading.",
            "Doubtful print → no firm total; ask only the sure part."),
        mcq("transfer", 5, "Built like मर्मशतं, what does वृक्षशतम् mean in a new example?",
            ("A hundred trees", "वृक्ष-शतम् = a hundred of trees, as मर्म-शतम् = a hundred marmas."),
            [("The hundredth tree", "That would need an ordinal; शतम् is the number a hundred."),
             ("A tree of a hundred years", "No years are in the word; शत counts the trees."),
             ("A thousand trees", "A thousand would be सहस्र, not शत.")],
            "वृक्षशतम् = a hundred trees, like मर्मशतम् = a hundred marmas.",
            "X-शतम् = a hundred X's.",
            teaches="A noun joined before शतम् names what is counted: मर्मशतम् = a hundred marmas, वृक्षशतम् = a hundred trees."),
    ],
}

# ---------------------------------------------------------------- unit 3
AUTHORED["3"] = {
    "title": "तत्र चतुश्चत्वारिंशच्छाखासु",
    "question": "By unit 3, how are the marmas divided among the limbs, the trunk and the part above?",
    "rule": ("Among these: forty-four (चतुश्चत्वारिंशत्) in the limbs (शाखासु), twenty-six (षड्विंशतिः) in the trunk "
             "(अन्तराधौ), and above (ऊर्ध्वम्) a number printed doubtfully, read by conjecture as thirty-seven."),
    "limits": ("Prose, no verb; appears to continue unit 2. 44 and 26 are sure. The printed समंत्रिश is no numeral: thirty-seven "
               "is a conjecture, so no question rests on the count above. 'Above' as neck and head is the data's remark, "
               "not the line's."),
    "explain_hi": ("यह पंक्ति इकाई २ की गिनती को आगे बढ़ाती दिखती है। "
                   "उनमें शाखाओं यानी हाथ-पैरों में चवालीस, अन्तराधि यानी धड़ में छब्बीस, और ऊपर एक संख्या जो छपाई में संदिग्ध है। "
                   "छपा ‘समंत्रिश’ कोई संख्या नहीं; डेटा अनुमान से ‘सप्तत्रिंशत्’ (सैंतीस) पढ़ता है, जिससे ४४ + २६ + ३७ = १०७ बनता है; इस पर कोई प्रश्न नहीं। "
                   "‘चतुश्चत्वारिंशच्छाखासु’ में त् + श → च्श होता है और स्वर (यहाँ आ) से पहले वैकल्पिक रूप से च्छ, जो छपा है; और ‘षड्विंशतिरंतराधौ’ में इ के बाद का विसर्ग स्वर से पहले र् बना है। "
                   "‘ऊपर’ से गर्दन और सिर समझना डेटा की टिप्पणी है, पंक्ति स्वयं नहीं कहती।"),
    "hook": "शाखा में चवालीस, धड़ में छब्बीस, ऊपर संदिग्ध।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 3, how many marmas lie in the śākhās (limbs)?",
            ("Forty-four", "चतुश्चत्वारिंशत् = four and forty = 44, शाखासु = in the limbs."),
            [("Twenty-six", "Twenty-six is the count of the trunk (antarādhi), not of the limbs."),
             ("Thirty-four", "चत्वारिंशत् is forty, not thirty."),
             ("Fourteen", "चत्वारिंशत् is forty, not ten.")],
            "Forty-four in the limbs.",
            "चतुश्चत्वारिंशच्छाखासु."),
        order(1, "Put the printed parts of unit 3 in the line's order.",
              ["तत्र", "चतुश्चत्वारिंशच्छाखासु", "षड्विंशतिरंतराधौ", "समंत्रिशदूर्ध्वं"],
              "Among these; 44 in the limbs; 26 in the trunk; (a doubtful number) above.",
              "तत्र → चतुश्चत्वारिंशच्छाखासु → षड्विंशतिरंतराधौ → समंत्रिशदूर्ध्वं."),
        match(2, "Match each sure word of unit 3 to its meaning.",
              [["चतुश्चत्वारिंशत्", "forty-four"], ["शाखा", "limb (literally branch)"], ["षड्विंशतिः", "twenty-six"],
               ["अन्तराधि", "trunk"]],
              "44 in the śākhās (limbs), 26 in the antarādhi (trunk).",
              "चतुश्चत्वारिंशत्, शाखा, षड्विंशतिः, अन्तराधि.", role="extend",
              teaches="शाखा (branch) names the limbs; अन्तराधि names the trunk (standard sense)."),
        mcq("discriminate", 3, "Which split of चतुश्चत्वारिंशच्छाखासु in unit 3 is right?",
            ("चतुश्चत्वारिंशत् + शाखासु", "त् before श becomes च्, and before a vowel श optionally becomes छ: -शत् + शाखासु → -शच्छाखासु (as printed)."),
            [("चतुश्चत्वारिंशत् + छाखासु", "छाखासु is not a word; the छ comes from the श of शाखासु."),
             ("चतुश्चत्वारिंशः + छाखासु", "A visarga does not give च्छ, and छाखासु is not a word."),
             ("चतुश्चत्वारिं + शच्छाखासु", "शच्छाखासु is not a word; चतुश्चत्वारिंशत् is one numeral.")],
            "चतुश्चत्वारिंशत् (forty-four) + शाखासु (in the limbs).",
            "त् + श → च्श, or च्छ before a vowel (as printed)."),
        mcq("apply", 4, "In षड्विंशतिरंतराधौ, why does the visarga of षड्विंशतिः appear as र्?",
            ("It follows इ and stands before a vowel", "After a vowel other than अ/आ, visarga before a vowel → र्: -तिर् + अन्तराधौ."),
            [("It follows अ and stands before a vowel", "The vowel before the visarga is इ (-ति); अः before अ would give ओऽ."),
             ("Every visarga before अ becomes र्", "Not every one: अः + अ gives ओऽ, आः + अ gives आ."),
             ("The र् belongs to the word अन्तराधि", "The word is अन्तराधौ; the र् comes from the visarga.")],
            "षड्विंशतिः + अन्तराधौ: इः before a vowel → इर्.",
            "इः / उः + vowel or voiced consonant → इर् / उर्."),
        mcq("transfer", 5, "By the rule of चतुश्चत्वारिंशच्छाखासु, how is तत् + शरीरम् (that body) joined in a new example?",
            ("तच्छरीरम्", "त् before श becomes च्; with a vowel after श, च्छ is the usual option (च्श is also valid), as -शत् + शाखासु → -शच्छाखासु."),
            [("तत्शरीरम्", "त् cannot stay unchanged before श; it becomes च्."),
             ("तद्शरीरम्", "द् comes before a voiced sound; श is not voiced."),
             ("तस्शरीरम्", "त् does not become स् before श.")],
            "तत् + शरीरम् = तच्छरीरम्, like चतुश्चत्वारिंशत् + शाखासु.",
            "त् + श → च्श, or च्छ before a vowel.",
            teaches="A final त् before श becomes च्, and श before a vowel optionally becomes छ: चतुश्चत्वारिंशत् + शाखासु → चतुश्चत्वारिंशच्छाखासु."),
    ],
}

# ---------------------------------------------------------------- unit 4
AUTHORED["4"] = {
    "title": "तलहृदयं नाम मर्म",
    "question": "By unit 4, where is talahṛdaya, and what follows for one pierced there?",
    "rule": ("In each lower limb (सक्थि), near the middle toe, in the middle of the sole (पादतलस्य मध्ये) is the marma "
             "named talahṛdaya; for one pierced there (विद्धस्य), death through pain (रुजया मरणम्)."),
    "limits": ("Prose. सक्थि usually means thigh; since this marma lies in the sole, the data reads it as the whole lower "
               "limb. Death 'through pain' is the text's wording; nothing is added about how. First of the limb marmas: "
               "units 5 to 14 go on with the leg."),
    "explain_hi": ("यहाँ से शाखाओं के मर्म आरम्भ होते हैं। "
                   "प्रत्येक सक्थि यानी पूरे निचले अंग में, मध्यमा अंगुली के पास, पैर के तलवे के बीच तलहृदय नामक मर्म है। "
                   "वहाँ बिंधे हुए (विद्धस्य) की पीड़ा (रुजया) से मृत्यु होती है; पाठ बस इतना कहता है। "
                   "सक्थि का सामान्य अर्थ जाँघ है, पर मर्म तलवे में है, इसलिए डेटा इसे पूरा निचला अंग मानता है। "
                   "‘अथैकैकस्मिन्’ में अथ + एकैकस्मिन् (अ + ए → ऐ) और एक + एक (अ + ए → ऐ) की सन्धि है।"),
    "hook": "तलवे का हृदय: बिंधे तो पीड़ा से मृत्यु।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 4, what follows for one pierced at talahṛdaya?",
            ("Death through pain", "विद्धस्य रुजया मरणम्: for one pierced there, death by pain."),
            [("Death from loss of blood", "Death from loss of blood is named at indrabasti (unit 9)."),
             ("Lameness of the whole leg", "Lameness is named at the knee (jānu, unit 10)."),
             ("Death by ākṣepaka (probably a spasm)", "Death by ākṣepaka is named at kṣipra (unit 5).")],
            "At talahṛdaya: death through pain.",
            "तत्र विद्धस्य रुजया मरणं."),
        order(1, "Put the phrases of unit 4 in the printed order.",
              ["अथैकैकस्मिन्सक्थि", "मध्यमांगुलिमभितो", "मध्ये पादतलस्य", "तलहृदयं नाम मर्म", "तत्र विद्धस्य",
               "रुजया मरणं"],
              "In each lower limb; near the middle toe; in the middle of the sole; the marma named talahṛdaya; for one pierced there; death through pain.",
              "Place → name → result."),
        match(2, "Match each word of unit 4 to its meaning.",
              [["तल", "sole"], ["हृदय", "heart, centre"], ["विद्ध", "pierced"], ["रुजा", "pain"], ["मरण", "death"]],
              "तल-हृदय = sole-heart; विद्धस्य = of one pierced; रुजया मरणम् = death by pain.",
              "तल, हृदय, विद्ध, रुजा, मरण.", role="extend",
              teaches="विद्ध is the past passive participle of √व्यध्: pierced; विद्धस्य = of (for) one pierced."),
        mcq("discriminate", 3, "Which split of अथैकैकस्मिन् in unit 4 is right?",
            ("अथ + एकैकस्मिन्", "अ + ए → ऐ: अथ + एकैकस्मिन् → अथैकैकस्मिन्."),
            [("अथ + इकैकस्मिन्", "अ + इ gives ए, not ऐ: that would be अथेकैकस्मिन्."),
             ("अथ + उकैकस्मिन्", "अ + उ gives ओ, not ऐ; and उकैकस्मिन् is not a word."),
             ("अथै + कैकस्मिन्", "Neither अथै nor कैकस्मिन् is a word.")],
            "अथ (now) + एकैकस्मिन् (in each): अ + ए → ऐ.",
            "अ + ए → ऐ."),
        mcq("apply", 4, "Where exactly does unit 4 place talahṛdaya?",
            ("Mid-sole, near the middle toe", "मध्यमाङ्गुलिम् अभितः, मध्ये पादतलस्य: near the middle toe, in the middle of the sole."),
            [("Between the big toe and the toe", "That is kṣipra (unit 5)."),
             ("Right below the ankle-joint", "That is kūrcaśiras (unit 7)."),
             ("In the middle of the shank", "That is indrabasti (unit 9).")],
            "Near the middle toe, in the middle of the sole.",
            "मध्यमांगुलिमभितो मध्ये पादतलस्य तलहृदयं."),
        mcq("transfer", 5, "By the pattern of रुजया (by pain, from रुजा), which form of शिला means by a stone, in a new example?",
            ("शिलया", "-अया is the instrumental singular of ā-stems, as रुजा → रुजया."),
            [("शिलायाः", "शिलायाः is genitive or ablative: of / from a stone."),
             ("शिलायाम्", "शिलायाम् is locative: on a stone."),
             ("शिलाम्", "शिलाम् is accusative: a stone (as object).")],
            "शिलया = by a stone, like रुजया = by pain.",
            "ā-stem, instrumental singular: -अया.",
            teaches="Feminine ā-stems form the instrumental singular in -अया: रुजा → रुजया (by pain), शिला → शिलया."),
    ],
}

# ---------------------------------------------------------------- unit 5
AUTHORED["5"] = {
    "title": "अंगुष्ठांगुल्योर्मध्ये क्षिप्रं",
    "question": "By unit 5, where is kṣipra, and what is named there?",
    "rule": ("Between the big toe (अङ्गुष्ठ) and the toe (अङ्गुलि) is kṣipra; there, death by ākṣepaka (probably a "
             "convulsive spasm)."),
    "limits": ("Prose. 'The next toe' is understood, not stated: अङ्गुलि is any finger or toe. The line does not say "
               "'marma'; that kṣipra is one is understood from the series (unit 6 says 'above kṣipra'). ākṣepaka = "
               "convulsive spasm is probable, not certain."),
    "explain_hi": ("अँगूठे और अंगुली के बीच क्षिप्र है; वहाँ आक्षेपक से मृत्यु। "
                   "आक्षेपक का अर्थ सम्भवतः ऐंठन का दौरा है (सम्भावित पहचान)। "
                   "‘अंगुली’ हाथ या पैर की कोई भी उँगली हो सकती है; ‘अगली अंगुली’ समझी जाती है, छपी नहीं। "
                   "पंक्ति ‘मर्म’ शब्द नहीं कहती; क्षिप्र मर्म है, यह क्रम से समझ आता है, क्योंकि इकाई ६ ‘क्षिप्र के ऊपर’ कहती है। "
                   "‘अंगुष्ठांगुल्योः’ द्वन्द्व का षष्ठी द्विवचन है: अँगूठे और अंगुली के।"),
    "hook": "अँगूठे-अंगुली के बीच क्षिप्र: आक्षेपक से मृत्यु।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 5, where does kṣipra lie?",
            ("Between the big toe and the toe", "अङ्गुष्ठाङ्गुल्योर्मध्ये: between the big toe and the toe."),
            [("In the middle of the sole", "That is talahṛdaya (unit 4)."),
             ("Three aṅgulas above the knee", "That is āṇi (unit 11)."),
             ("At the joining of foot and shank", "That is gulpha (unit 8).")],
            "Between the big toe and the toe.",
            "अंगुष्ठांगुल्योर्मध्ये क्षिप्रं."),
        order(1, "Put the words of unit 5 in the printed order.",
              ["अंगुष्ठांगुल्योर्मध्ये", "क्षिप्रं", "तत्र", "आक्षेपकेण", "मरणं"],
              "Between the big toe and the toe; kṣipra; there; by ākṣepaka; death.",
              "अंगुष्ठांगुल्योर्मध्ये → क्षिप्रं → तत्र → आक्षेपकेण → मरणं."),
        match(2, "Match each word of unit 5 to its meaning.",
              [["अङ्गुष्ठ", "big toe"], ["अङ्गुलि", "finger or toe"], ["मध्ये", "between"],
               ["क्षिप्र", "'quick' (the marma's name)"], ["मरण", "death"]],
              "Between the big toe and the toe lies kṣipra ('quick'); there, death.",
              "अङ्गुष्ठ, अङ्गुलि, मध्ये, क्षिप्र, मरण.", role="extend",
              teaches="अङ्गुलि is general (finger or toe); here, with अङ्गुष्ठ in the foot, it names a toe."),
        mcq("discriminate", 3, "Which split of the printed क्षिप्रंतत्राक्षेपकेण is right?",
            ("क्षिप्रम् + तत्र + आक्षेपकेण", "म् before त is written ं; अ + आ → आ: तत्राक्षेपकेण."),
            [("क्षिप्रम् + तत्र + क्षेपकेण", "Without आ the join would be तत्रक्षेपकेण, with a short अ."),
             ("क्षिप्रम् + तत्रा + क्षेपकेण", "तत्रा is not a word; the word is तत्र."),
             ("क्षिप्रम् + तत् + राक्षेपकेण", "राक्षेपकेण is not a word; तत्र is one word.")],
            "क्षिप्रम् (kṣipra) + तत्र (there) + आक्षेपकेण (by ākṣepaka).",
            "अ + आ → आ; final म् before a consonant → ं."),
        multi("apply", 4, "Which statements fit unit 5?",
              [("The line says outright that kṣipra is a marma", "The word 'marma' is not printed; it is understood from the series."),
               ("Kṣipra lies between the big toe and the toe", "Right: अङ्गुष्ठाङ्गुल्योर्मध्ये."),
               ("Death by ākṣepaka is named there", "Right: तत्राक्षेपकेण मरणम्."),
               ("The line names which toe lies next to the big toe", "'The next toe' is understood, not stated.")],
              [1, 2],
              "Between the big toe and the toe; death by ākṣepaka; 'marma' and 'next toe' are understood.",
              "अंगुष्ठांगुल्योर्मध्ये क्षिप्रं तत्राक्षेपकेण मरणं."),
        mcq("transfer", 5, "By the pattern of अङ्गुष्ठाङ्गुल्योः (of the big toe and the toe), which form means of Rāma and Lakṣmaṇa (the two), in a new example?",
            ("रामलक्ष्मणयोः", "A dvandva of two takes the dual; -योः is the genitive dual."),
            [("रामलक्ष्मणानाम्", "-आनाम् is the genitive plural: of more than two."),
             ("रामलक्ष्मणौ", "-औ is the nominative/accusative dual, not 'of'."),
             ("रामलक्ष्मणस्य", "-स्य is the genitive singular: of one.")],
            "रामलक्ष्मणयोः = of Rāma and Lakṣmaṇa, like अङ्गुष्ठाङ्गुल्योः.",
            "Dvandva of two, genitive dual: -योः.",
            teaches="A dvandva naming two things takes dual endings: अङ्गुष्ठ + अङ्गुलि → अङ्गुष्ठाङ्गुल्योः (of the two)."),
    ],
}

# ---------------------------------------------------------------- unit 6
AUTHORED["6"] = {
    "title": "क्षिप्रस्योपरि ... कूर्च्चः",
    "question": "By unit 6, where is kūrca placed, and which part of the line is doubtful?",
    "rule": ("Above kṣipra (क्षिप्रस्योपरि), two aṅgulas (finger-breadths) away, on both sides (उभयतः), is kūrca. The "
             "word naming what occurs there is damaged in print."),
    "limits": ("Low confidence. The printed पादरुयभ्रमणवेपने is damaged: 'whirling and trembling of the foot' is a "
               "conjecture (ruya dropped; or ruya = rujā, pain, giving three items). द्व्यंगुलउभयतः looks like a slip for "
               "द्व्यङ्गुलम् उभयतः. Singular or dual kūrca is open. No question rests on the result or on these forms."),
    "explain_hi": ("क्षिप्र के ऊपर, दो अंगुल यानी दो उँगली-चौड़ाई पर, दोनों ओर कूर्च है। "
                   "वहाँ क्या होता है, वह शब्द छपाई में बिगड़ा है: ‘पादरुयभ्रमणवेपने’ में ‘रुय’ कोई शब्द नहीं। "
                   "डेटा अनुमान से ‘पाँव का घूमना और काँपना’ पढ़ता है; ‘रुय’ को रुजा (पीड़ा) मानें तो तीन बातें बनती हैं। "
                   "‘द्व्यंगुलउभयतः’ भी छपाई की भूल लगती है (द्व्यङ्गुलम् उभयतः)। "
                   "डेटा का विश्वास निम्न है; प्रश्न स्थान, पक्के शब्दों, छपे क्रम और ‘क्षिप्रस्योपरि’ की सन्धि पर हैं, फल के पाठ पर कोई नहीं।"),
    "hook": "क्षिप्र से दो अंगुल ऊपर, दोनों ओर कूर्च; फल अस्पष्ट।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 6, above which marma does kūrca lie?",
            ("Above kṣipra", "क्षिप्रस्योपरि: above kṣipra."),
            [("Above the knee (jānu)", "Above the knee lies āṇi (unit 11)."),
             ("Above urvī", "Above urvī lies lohita (unit 13)."),
             ("Above the groin-joint", "Kūrca lies on the foot, above kṣipra, far below the groin-joint.")],
            "Kūrca lies above kṣipra, two aṅgulas away, on both sides.",
            "क्षिप्रस्योपरि ... कूर्च्चः."),
        order(1, "Put the printed parts of unit 6 in the line's order.",
              ["क्षिप्रस्योपरि", "द्व्यंगुलउभयतः", "कूर्च्चः", "तत्र पादरुयभ्रमणवेपने भवतः"],
              "Above kṣipra; two aṅgulas, on both sides; kūrca; there (a damaged word) occur.",
              "Place → name → (damaged) result."),
        match(2, "Match each sure word of unit 6 to its meaning.",
              [["क्षिप्रस्य", "of kṣipra"], ["उपरि", "above"], ["अङ्गुल", "finger-breadth"], ["उभयतः", "on both sides"]],
              "Above kṣipra, two finger-breadths, on both sides.",
              "क्षिप्रस्य, उपरि, अङ्गुल, उभयतः.", role="extend",
              teaches="अङ्गुल is a measure, a finger-breadth; distances between marmas are given in aṅgulas."),
        mcq("discriminate", 3, "Which split of क्षिप्रस्योपरि in unit 6 is right?",
            ("क्षिप्रस्य + उपरि", "अ + उ → ओ: क्षिप्रस्य + उपरि → क्षिप्रस्योपरि."),
            [("क्षिप्रस्यो + परि", "क्षिप्रस्यो is not a form of क्षिप्र; the ओ comes from अ + उ."),
             ("क्षिप्रस्य + ओपरि", "ओपरि is not a word, and अ + ओ would give औ."),
             ("क्षिप्रस्याः + उपरि", "आः before उ would give the gap क्षिप्रस्या उपरि.")],
            "क्षिप्रस्य (of kṣipra) + उपरि (above): अ + उ → ओ.",
            "अ + उ → ओ."),
        mcq("apply", 4, "Why does the card give no firm result for kūrca in unit 6?",
            ("The word naming the result is damaged", "पादरुयभ्रमणवेपने contains 'ruya', which is not a word."),
            [("The line names no place for kūrca", "The place is printed: above kṣipra, two aṅgulas, both sides."),
             ("The result is held over to unit 7", "Unit 7 names kūrcaśiras and its own result, not kūrca's."),
             ("The line says that nothing happens there", "तत्र ... भवतः: something is said to occur there.")],
            "Only the place is sure; the result word is damaged and read by conjecture.",
            "Damaged word → no question on it."),
        mcq("transfer", 5, "By the rule of क्षिप्रस्योपरि, how is तस्य + उपरि (above him) joined in a new example?",
            ("तस्योपरि", "अ + उ → ओ, as क्षिप्रस्य + उपरि → क्षिप्रस्योपरि."),
            [("तस्यौपरि", "औ comes from अ + ओ or अ + औ, not from अ + उ."),
             ("तस्युपरि", "The अ does not simply drop before उ."),
             ("तस्यपरि", "The उ does not simply drop after अ.")],
            "तस्य + उपरि = तस्योपरि, like क्षिप्रस्य + उपरि.",
            "अ + उ → ओ.",
            teaches="अ before उ joins to ओ: क्षिप्रस्य + उपरि → क्षिप्रस्योपरि."),
    ],
}

# ---------------------------------------------------------------- unit 7
AUTHORED["7"] = {
    "title": "गुल्फसंधेरधः कूर्च्चशिरः",
    "question": "By unit 7, where is kūrcaśiras, and which part of the named result is sure?",
    "rule": ("Below the ankle-joint (गुल्फसन्धेः अधः) is kūrcaśiras, 'the head of the kūrca'; there, pain (रुजा) and a "
             "second sign printed शोक (grief), read by conjecture as शोफ (swelling)."),
    "limits": ("Prose; nominal sentence. शोक → शोफ (swelling) is a conjecture, so no question rests on the second sign; "
               "only pain (रुजा) is asked. Doubled -र्च्च- is a print habit for कूर्च. gulpha = ankle (standard)."),
    "explain_hi": ("टखने के जोड़ (गुल्फसन्धि) के नीचे कूर्चशिर है, यानी कूर्च का सिर। "
                   "वहाँ पीड़ा (रुजा) और एक दूसरा लक्षण कहा गया है। "
                   "छपा ‘शोक’ (दुःख) शरीर के लक्षणों की सूची में नहीं बैठता; डेटा अनुमान से ‘शोफ’ (सूजन) पढ़ता है, इसलिए उस पर कोई प्रश्न नहीं। "
                   "‘गुल्फसंधेरधः’ में ए के बाद का विसर्ग स्वर अ से पहले र् बना है। "
                   "‘कूर्च्च’ का दोहरा च छपाई की आदत है; शब्द कूर्च है।"),
    "hook": "टखने के नीचे कूर्चशिर: पीड़ा, और दूसरा लक्षण संदिग्ध।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 7, where does kūrcaśiras lie?",
            ("Below the ankle-joint", "गुल्फसन्धेः अधः: below the ankle-joint."),
            [("Above the knee, on both sides", "That is āṇi (unit 11)."),
             ("In the middle of the thigh", "That is urvī (unit 12)."),
             ("In the middle of the shank", "That is indrabasti (unit 9).")],
            "Below the ankle-joint.",
            "गुल्फसंधेरधः कूर्च्चशिरः."),
        order(1, "Put the printed parts of unit 7 in the line's order.",
              ["गुल्फसंधेरधः", "कूर्च्चशिरः", "तत्र", "रुजाशोकौ"],
              "Below the ankle-joint; kūrcaśiras; there; pain and (a doubtful second sign).",
              "Place → name → there → result."),
        fill(2, "Unit 7: गुल्फसन्धेः ____ कूर्चशिरः (below the ankle-joint). Type it in Devanagari or in English letters (e.g. dharma).",
             accepts("अधः", None, "adhah", "adha"),
             "अधः (below): गुल्फसन्धेः अधः, printed गुल्फसंधेरधः.",
             "अधः is an indeclinable, 'below'; it takes the genitive of what something lies below (गुल्फसन्धेः).",
             "गुल्फसन्धेः अधः."),
        mcq("discriminate", 3, "Which split of गुल्फसंधेरधः in unit 7 is right?",
            ("गुल्फसन्धेः + अधः", "After ए, a visarga before a vowel → र्: -सन्धेर् + अधः."),
            [("गुल्फसन्धे + रधः", "रधः is not a word; the र् comes from the visarga."),
             ("गुल्फसन्धिः + अधः", "That would join as गुल्फसन्धिरधः, with ि, not े."),
             ("गुल्फसन्धेः + धः", "धः is not a word; the अ belongs to अधः.")],
            "गुल्फसन्धेः (of the ankle-joint) + अधः (below).",
            "Vowel other than अ/आ + visarga before a vowel → र्."),
        match(4, "Match each word of unit 7 to its meaning.",
              [["गुल्फ", "ankle"], ["सन्धि", "joint"], ["अधः", "below"], ["शिरः", "head"], ["रुजा", "pain"]],
              "Below the ankle-joint, the head of the kūrca; there, pain.",
              "गुल्फ, सन्धि, अधः, शिरः, रुजा.", role="apply"),
        mcq("transfer", 5, "By the rule of गुल्फसंधेरधः, how is हरेः + आगमनम् (Hari's coming) joined in a new example?",
            ("हरेरागमनम्", "After ए, a visarga before a vowel becomes र्, as गुल्फसन्धेः + अधः."),
            [("हरे आगमनम्", "After ए the visarga does not drop; it becomes र्."),
             ("हरेसागमनम्", "स् comes from visarga before त or थ, not before a vowel."),
             ("हरेशागमनम्", "श् comes from visarga before च, छ or श, not before a vowel.")],
            "हरेः + आगमनम् = हरेरागमनम्, like गुल्फसन्धेः + अधः = गुल्फसन्धेरधः.",
            "ए + visarga before a vowel → एर्.",
            teaches="After a vowel other than अ/आ, a visarga before a vowel or voiced consonant becomes र्: गुल्फसन्धेः + अधः → गुल्फसन्धेरधः."),
    ],
}

# ---------------------------------------------------------------- unit 8
AUTHORED["8"] = {
    "title": "पादजंघयोः संधाने गुल्फः",
    "question": "By unit 8, where is gulpha, and which signs are named there?",
    "rule": ("At the joining of the foot and the shank (पादजङ्घयोः सन्धाने) is gulpha (the ankle); there pain (रुक्), "
             "stiffness of the sakthi (स्तब्धसक्थिता), or numbness (जडता): वा at the end makes them alternatives."),
    "limits": ("Prose. जङ्घा is the shank (lower leg), not the Hindi 'thigh' sense. सक्थि is kept as 'thigh' here; as in "
               "unit 4 it may mean the whole leg. जडता may also be 'torpor'; 'numbness' is the plainer sense for a limb."),
    "explain_hi": ("पैर और जंघा यानी घुटने से नीचे की टाँग के जोड़ पर गुल्फ यानी टखना है। "
                   "वहाँ पीड़ा, सक्थि (जाँघ) का अकड़ जाना, अथवा जड़ता यानी सुन्नपन होता है। "
                   "अन्त का ‘वा’ (अथवा) तीनों को विकल्प बनाता है: तीनों का एक साथ होना नहीं कहा गया। "
                   "संस्कृत में जङ्घा घुटने से नीचे का भाग है, हिन्दी की ‘जाँघ’ नहीं। "
                   "सक्थि यहाँ ‘जाँघ’ रखा गया है, पर इकाई ४ की तरह पूरा पैर भी हो सकता है।"),
    "hook": "टखने पर: पीड़ा, अकड़न या सुन्नपन, कोई एक।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 8, where does gulpha lie?",
            ("At the joining of foot and shank", "पादजङ्घयोः सन्धाने: at the joining of the foot and the shank."),
            [("At the joining of shank and thigh", "That is jānu, the knee (unit 10)."),
             ("In the middle of the shank", "That is indrabasti (unit 9)."),
             ("Between the groin and the testes", "That is viṭapa (unit 14), not gulpha.")],
            "At the joining of foot and shank: the ankle.",
            "पादजंघयोः संधाने गुल्फः."),
        order(1, "Put the phrases of unit 8 in the printed order.",
              ["पादजंघयोः संधाने", "गुल्फः", "तत्र रुक्", "स्तब्धसक्थिता", "जडता वा"],
              "At the joining of foot and shank; gulpha; there pain; stiffness of the sakthi; or numbness.",
              "Place → name → three alternative signs."),
        match(2, "Match each word of unit 8 to its meaning.",
              [["पाद", "foot"], ["जङ्घा", "shank (lower leg)"], ["सन्धान", "joining"], ["रुक्", "pain"],
               ["जडता", "numbness"]],
              "At the joining of foot and shank; pain or numbness among the signs.",
              "पाद, जङ्घा, सन्धान, रुक्, जडता.", role="extend",
              teaches="जङ्घा is the shank below the knee, not the thigh; the thigh is ऊरु (unit 10)."),
        mcq("discriminate", 3, "One word of this rendering of unit 8 is wrong: 'At the joining of foot and thigh, the gulpha; there pain, stiffness, or numbness.' Which?",
            ("'thigh' for जङ्घा", "जङ्घा is the shank (lower leg), not the thigh."),
            [("'pain' for रुक्", "रुक् does mean pain."),
             ("'numbness' for जडता", "जडता = numbness (or torpor): right."),
             ("'or' for वा", "वा does mean or.")],
            "पादजङ्घयोः = of the foot and the shank.",
            "जङ्घा = shank; ऊरु = thigh."),
        mcq("apply", 4, "In unit 8, what does वा at the end say about the three signs?",
            ("They are named as alternatives", "वा = or: pain, stiffness, or numbness."),
            [("All three always occur together", "That would need च (and); the line has वा (or)."),
             ("They come one after another in time", "No order in time is stated; वा makes them alternatives."),
             ("Only the last one is really meant", "वा joins all three as alternatives, not the last alone.")],
            "रुक् स्तब्धसक्थिता जडता वा: pain, stiffness, or numbness.",
            "वा = or (alternatives); च = and."),
        mcq("transfer", 5, "By the pattern of जडता (numbness, from जड), which word means muteness (from मूक, mute), in a new example?",
            ("मूकता", "-ता makes a feminine abstract noun: जड → जडता, मूक → मूकता."),
            [("मूकतः", "-तः makes an adverb (from, on the side of), not a state."),
             ("मूकेन", "मूकेन is the instrumental: by the mute one."),
             ("मूकाः", "मूकाः is the plural: the mute ones.")],
            "मूकता = muteness, like जडता = numbness.",
            "Adjective + -ता → abstract noun (f.).",
            teaches="-ता added to an adjective gives the state of it (feminine): जड → जडता, स्तब्धसक्थि → स्तब्धसक्थिता."),
    ],
}

# ---------------------------------------------------------------- unit 9
AUTHORED["9"] = {
    "title": "जंघामध्ये इंद्रबस्तिः",
    "question": "By unit 9, where is indrabasti, and what is named there?",
    "rule": ("At twelve aṅgulas (द्वादशभिरङ्गुलैः), in the middle of the shank (जङ्घामध्ये), is indrabasti; there, death "
             "from loss of blood (शोणित). The starting point, printed पाणि (hand), is read by conjecture as पार्ष्णि (heel)."),
    "limits": ("Prose. 'From the heel' is a conjecture for the printed पाणि; no question rests on it. क्ष्यात् for क्षयात् is "
               "a near-certain print slip. 'Basti' here is part of a marma name, not the urinary bladder of unit 19."),
    "explain_hi": ("जंघा यानी घुटने से नीचे की टाँग के बीच, बारह अंगुल पर, इन्द्रबस्ति है; वहाँ शोणित यानी रक्त के क्षय से मृत्यु। "
                   "माप कहाँ से आरम्भ होता है, वह शब्द छपाई में ‘पाणि’ (हाथ) है, जो टाँग के माप में नहीं बैठता; डेटा अनुमान से ‘पार्ष्णि’ (एड़ी) पढ़ता है, इस पर कोई प्रश्न नहीं। "
                   "छपा ‘क्ष्यात्’ लगभग निश्चित रूप से ‘क्षयात्’ है। "
                   "इन्द्रबस्ति में ‘बस्ति’ मर्म के नाम का भाग है; यह इकाई १९ का मूत्राशय नहीं। "
                   "‘द्वादशभिरंगुलैः’ दोनों तृतीया बहुवचन हैं।"),
    "hook": "टाँग के बीच इन्द्रबस्ति: रक्त-क्षय से मृत्यु।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 9, where does indrabasti lie?",
            ("In the middle of the shank", "जङ्घामध्ये: in the middle of the shank (lower leg)."),
            [("In the middle of the thigh", "That is urvī (unit 12)."),
             ("At the root of the thigh", "That is lohita (unit 13)."),
             ("In the middle of the sole", "That is talahṛdaya (unit 4).")],
            "In the middle of the shank, at twelve aṅgulas.",
            "जंघामध्ये इंद्रबस्तिः."),
        match(1, "Match each sure word of unit 9 to its meaning.",
              [["द्वादश", "twelve"], ["अङ्गुल", "finger-breadth"], ["जङ्घा", "shank"], ["मध्ये", "in the middle"],
               ["शोणित", "blood"]],
              "Twelve finger-breadths, in the middle of the shank; there, (loss of) blood.",
              "द्वादश, अङ्गुल, जङ्घा, मध्ये, शोणित."),
        order(2, "Put the printed parts of unit 9 in the line's order.",
              ["पाणिप्रभृति", "द्वादशभिरंगुलैर्जंघामध्ये", "इंद्रबस्तिः", "तत्र", "शोणितक्ष्यान्मरणं"],
              "Starting from (a doubtful word); at twelve aṅgulas in the middle of the shank; indrabasti; there; death from loss of blood.",
              "Start → distance and place → name → result.", role="extend",
              teaches="A marma is placed by a starting point, a distance in aṅgulas and a part of the body."),
        mcq("discriminate", 3, "In the name indrabasti (unit 9), what is 'basti'?",
            ("Part of a marma's name", "The data: basti here is part of the marma name, not the organ."),
            [("The urinary bladder itself", "The data keeps it apart from the bladder (basti) of unit 19."),
             ("A measure of distance", "The distance is given by अङ्गुलैः, not by basti."),
             ("A sign of injury there", "The sign named there is death from loss of blood.")],
            "Indrabasti is a name; its 'basti' is not the organ of unit 19.",
            "Marma names may borrow words (basti, hṛdaya) without meaning the organ."),
        mcq("apply", 4, "In द्वादशभिरंगुलैः of unit 9, what case are both words?",
            ("Instrumental plural", "-भिः and -ऐः are instrumental plural endings: by (at) twelve aṅgulas."),
            [("Locative plural", "The locative plural ends in -सु / -षु (as शाखासु, unit 3)."),
             ("Genitive plural", "The genitive plural ends in -नाम् / -आणाम्."),
             ("Accusative plural", "An a-stem accusative plural ends in -आन्, not -ऐः.")],
            "द्वादशभिः अङ्गुलैः: instrumental plural.",
            "-भिः, -ऐः = instrumental plural."),
        mcq("transfer", 5, "By the pattern of अङ्गुलैः, which form of हस्त means with the hands (instrumental), in a new example?",
            ("हस्तैः", "-ऐः is the instrumental plural of a-stems, as अङ्गुल → अङ्गुलैः."),
            [("हस्तेषु", "हस्तेषु is the locative plural: in the hands."),
             ("हस्तानाम्", "हस्तानाम् is the genitive plural: of the hands."),
             ("हस्तौ", "हस्तौ is the nominative/accusative dual: the two hands.")],
            "हस्तैः = with the hands, like अङ्गुलैः = by aṅgulas.",
            "a-stem, instrumental plural: -ऐः.",
            teaches="a-stems form the instrumental plural in -ऐः: अङ्गुल → अङ्गुलैः, हस्त → हस्तैः."),
    ],
}

# ---------------------------------------------------------------- unit 10
AUTHORED["10"] = {
    "title": "जंघोर्वोः संधाने जानु",
    "question": "By unit 10, where is jānu, and what is named there?",
    "rule": ("At the joining of the shank and the thigh (जङ्घोर्वोः सन्धाने) is jānu (the knee); there, lameness "
             "(खञ्जता). जङ्घा + ऊर्वोः → जङ्घोर्वोः (आ + ऊ → ओ)."),
    "limits": ("Prose; nominal sentence, no verb supplied. Only one result, lameness, is named; nothing is said of how "
               "long it lasts or of treatment."),
    "explain_hi": ("जंघा यानी घुटने से नीचे की टाँग और ऊरु यानी जाँघ के जोड़ पर जानु यानी घुटना है; वहाँ लंगड़ापन होता है। "
                   "इकाई ८ में पैर और जंघा का जोड़ टखना था; यहाँ जंघा और ऊरु का जोड़ घुटना है। "
                   "‘जंघोर्वोः’ में जङ्घा + ऊर्वोः की सन्धि है: आ + ऊ → ओ। "
                   "यह द्वन्द्व का षष्ठी द्विवचन है: जंघा और ऊरु, दोनों का।"),
    "hook": "जंघा और जाँघ के जोड़ पर घुटना: लंगड़ापन।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 10, what result is named at jānu (the knee)?",
            ("Lameness", "खञ्जता = lameness."),
            [("Death through pain", "Death through pain is named at talahṛdaya (unit 4)."),
             ("Wasting of the thigh", "Wasting of the thigh is named at urvī (unit 12)."),
             ("Paralysis of one side", "Paralysis of one side is named at lohita (unit 13).")],
            "At the knee: lameness.",
            "जानु तत्र खंजता."),
        order(1, "Put the words of unit 10 in the printed order.",
              ["जंघोर्वोः", "संधाने", "जानु", "तत्र", "खंजता"],
              "Of shank and thigh; at the joining; the knee; there; lameness.",
              "जंघोर्वोः → संधाने → जानु → तत्र → खंजता."),
        match(2, "Match each word of unit 10 to its meaning.",
              [["जङ्घा", "shank"], ["ऊरु", "thigh"], ["सन्धान", "joining"], ["जानु", "knee"], ["खञ्जता", "lameness"]],
              "At the joining of shank and thigh, the knee; there, lameness.",
              "जङ्घा, ऊरु, सन्धान, जानु, खञ्जता.", role="extend",
              teaches="ऊरु is the thigh, जङ्घा the shank: the knee (जानु) is where they join."),
        mcq("discriminate", 3, "Which split of जंघोर्वोः in unit 10 is right?",
            ("जङ्घा + ऊर्वोः", "आ + ऊ → ओ: जङ्घा + ऊर्वोः → जङ्घोर्वोः."),
            [("जङ्घा + अर्वोः", "आ + अ gives आ: that would be जङ्घार्वोः."),
             ("जङ्घाः + ऊर्वोः", "आः before a vowel drops the visarga and leaves a gap: जङ्घा ऊर्वोः."),
             ("जङ्घे + ऊर्वोः", "ए before ऊ would give अय् (or a gap), not ओ.")],
            "जङ्घा (shank) + ऊर्वोः (of the thigh): आ + ऊ → ओ.",
            "आ + ऊ → ओ."),
        mcq("apply", 4, "At the joining of which two parts does unit 10 place jānu?",
            ("Shank and thigh", "जङ्घोर्वोः सन्धाने: at the joining of shank and thigh."),
            [("Foot and shank", "The joining of foot and shank is gulpha (unit 8)."),
             ("Thigh and groin", "Near the groin-joint lies lohita (unit 13), not jānu."),
             ("Big toe and toe", "Between the big toe and the toe lies kṣipra (unit 5).")],
            "Jānu: the joining of shank and thigh.",
            "जंघोर्वोः संधाने जानु."),
        mcq("transfer", 5, "By the rule of जंघोर्वोः, how is गङ्गा + ऊर्मिः (wave of the Gaṅgā) joined in a new example?",
            ("गङ्गोर्मिः", "आ + ऊ → ओ, as जङ्घा + ऊर्वोः → जङ्घोर्वोः."),
            [("गङ्गौर्मिः", "औ comes from आ + ओ or आ + औ, not from आ + ऊ."),
             ("गङ्गार्मिः", "आ does not swallow ऊ; the two join to ओ."),
             ("गङ्गूर्मिः", "The आ does not simply drop before ऊ.")],
            "गङ्गा + ऊर्मिः = गङ्गोर्मिः, like जङ्घा + ऊर्वोः = जङ्घोर्वोः.",
            "आ + ऊ → ओ.",
            teaches="आ (or अ) before उ / ऊ joins to ओ: जङ्घा + ऊर्वोः → जङ्घोर्वोः."),
    ],
}

# ---------------------------------------------------------------- unit 11
AUTHORED["11"] = {
    "title": "जानुनस्त्र्यंगुलादूर्ध्वमुभयतआणिः",
    "question": "By unit 11, where is āṇi, and which signs are named there?",
    "rule": ("Three aṅgulas above the knee (जानुनः त्र्यङ्गुलात् ऊर्ध्वम्), on both sides (उभयतः), is āṇi; there, increase "
             "of swelling (शोफाभिवृद्धिः) and stiffness of the sakthi (स्तब्धसक्थिता), joined by च (and)."),
    "limits": ("Prose. āṇi is read as the marma's name (the word means a pin or linchpin). सक्थि is kept as 'thigh'. The "
               "print shows अभिवृद्धिस्तब्ध with one स (the visarga before स्त not written, an optional form); no question "
               "rests on that join."),
    "explain_hi": ("घुटने से तीन अंगुल ऊपर, दोनों ओर, आणि है; वहाँ सूजन का बढ़ना और सक्थि (जाँघ) का अकड़ जाना होता है। "
                   "इकाई ८ के ‘वा’ (अथवा) के विपरीत यहाँ ‘च’ (और) है: दोनों लक्षण साथ कहे गए हैं। "
                   "‘उभयतआणिः’ में उभयतः + आणिः है: अ के बाद का विसर्ग अ से भिन्न स्वर से पहले लुप्त होता है और बीच में अन्तर रहता है (उभयत आणिः)। "
                   "‘त्र्यंगुलादूर्ध्वम्’ में त्रि + अङ्गुल (इ + अ → य) और स्वर से पहले त् → द् हुआ है। "
                   "आणि शब्द का अर्थ कील या धुरी की कील है; यहाँ मर्म का नाम।"),
    "hook": "घुटने से तीन अंगुल ऊपर आणि: सूजन बढ़े और जाँघ अकड़े।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 11, how far above the knee does āṇi lie?",
            ("Three aṅgulas", "जानुनः त्र्यङ्गुलात् ऊर्ध्वम्: three aṅgulas above the knee."),
            [("Two aṅgulas", "Two aṅgulas is the distance of kūrca above kṣipra (unit 6)."),
             ("Twelve aṅgulas", "Twelve aṅgulas is the distance of indrabasti (unit 9)."),
             ("Eight aṅgulas", "त्रि is three, not eight.")],
            "Three aṅgulas above the knee, on both sides.",
            "जानुनस्त्र्यंगुलादूर्ध्वमुभयतआणिः."),
        match(1, "Match each word of unit 11 to its meaning.",
              [["जानु", "knee"], ["ऊर्ध्वम्", "above"], ["उभयतः", "on both sides"], ["शोफ", "swelling"],
               ["अभिवृद्धि", "increase"]],
              "Above the knee, on both sides; there, increase of swelling.",
              "जानु, ऊर्ध्वम्, उभयतः, शोफ, अभिवृद्धि."),
        order(2, "Put the parts of unit 11's place-phrase in the printed order.",
              ["जानुनः", "त्र्यंगुलात्", "ऊर्ध्वम्", "उभयतः", "आणिः"],
              "From the knee; three aṅgulas; above; on both sides; āṇi.",
              "जानुनः → त्र्यंगुलात् → ऊर्ध्वम् → उभयतः → आणिः.", role="extend",
              teaches="A distance is given in the ablative: जानुनः (from the knee) त्र्यङ्गुलात् (by three aṅgulas) ऊर्ध्वम् (above)."),
        mcq("discriminate", 3, "Why does the print show उभयतआणिः with no visarga after उभयत?",
            ("अः before a vowel other than अ drops ः", "उभयतः + आणिः → उभयत आणिः: the visarga goes, a gap remains."),
            [("अः before any vowel at all becomes ओ", "अः gives ओ before a voiced consonant (and ओऽ before अ), not before आ."),
             ("The visarga became र् and then dropped", "र् comes after vowels other than अ/आ; here the vowel is अ."),
             ("The visarga became स् before the आ", "स् comes from visarga before त or थ, not before a vowel.")],
            "उभयतः + आणिः: अः before आ → अ, with a gap.",
            "अः + vowel other than अ → अ (gap)."),
        mcq("apply", 4, "Which split of त्र्यंगुलादूर्ध्वम् in unit 11 is right?",
            ("त्र्यङ्गुलात् + ऊर्ध्वम्", "त् before a vowel is written द्: -लात् + ऊर्ध्वम् → -लादूर्ध्वम्."),
            [("त्र्यङ्गुला + दूर्ध्वम्", "दूर्ध्वम् is not a word; the द् comes from the त् of -लात्."),
             ("त्र्यङ्गुलाः + ऊर्ध्वम्", "आः before a vowel would leave a gap: त्र्यङ्गुला ऊर्ध्वम्."),
             ("त्र्यङ्गुलाम् + ऊर्ध्वम्", "म् before a vowel would give त्र्यङ्गुलामूर्ध्वम्.")],
            "त्र्यङ्गुलात् (by three aṅgulas, ablative) + ऊर्ध्वम् (above).",
            "त् + vowel → द्."),
        mcq("transfer", 5, "By the rule of त्रि + अङ्गुल → त्र्यङ्गुल, how is प्रति + अङ्गम् (to each limb) joined in a new example?",
            ("प्रत्यङ्गम्", "इ before अ becomes य्: प्रति + अङ्गम् → प्रत्यङ्गम्."),
            [("प्रतेङ्गम्", "ए comes from अ + इ, not from इ + अ."),
             ("प्रताङ्गम्", "The इ does not drop and lengthen the अ."),
             ("प्रतीङ्गम्", "ई comes from इ + इ, not from इ + अ.")],
            "प्रति + अङ्गम् = प्रत्यङ्गम्, like त्रि + अङ्गुल = त्र्यङ्गुल.",
            "इ + अ → य.",
            teaches="इ before अ becomes य्: त्रि + अङ्गुलात् → त्र्यङ्गुलात्."),
    ],
}

# ---------------------------------------------------------------- unit 12
AUTHORED["12"] = {
    "title": "ऊरुमध्ये उर्वी",
    "question": "By unit 12, where is urvī, and what is named there?",
    "rule": ("In the middle of the thigh (ऊरुमध्ये) is urvī; there, from loss of blood (रक्तक्षयात्, ablative of cause), "
             "wasting of the sakthi (सक्थिशोषः)."),
    "limits": ("Prose; nominal sentence. urvī is a marma name (the word means 'wide'). सक्थि is kept as 'thigh'. The print "
               "joins तत्र and रक्तक्षयात् without a space (no sandhi there)."),
    "explain_hi": ("ऊरु यानी जाँघ के बीच उर्वी है; वहाँ रक्त के क्षय से सक्थि (जाँघ) का शोष यानी सूखकर क्षीण होना होता है। "
                   "‘रक्तक्षयात्’ पञ्चमी है: कारण बताती है, ‘रक्त के क्षय से’। "
                   "उर्वी शब्द का अर्थ ‘चौड़ी’ है; यहाँ मर्म का नाम। "
                   "छपाई में ‘तत्ररक्तक्षयात्’ बिना अन्तर के जुड़ा है, यह सन्धि नहीं, केवल छपाई। "
                   "अगली इकाई १३ का लोहित इसी उर्वी के ऊपर रखा गया है।"),
    "hook": "जाँघ के बीच उर्वी: रक्त घटे, जाँघ सूखे।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 12, what result is named at urvī?",
            ("Wasting of the thigh, from blood loss", "रक्तक्षयात् सक्थिशोषः: from loss of blood, wasting of the sakthi."),
            [("Paralysis of one side, from blood loss", "That is named at lohita (unit 13), not at urvī."),
             ("Death, from loss of blood in the shank", "Death from loss of blood is named at indrabasti (unit 9)."),
             ("Lameness, from injury at the joining", "Lameness is named at the knee (unit 10).")],
            "At urvī: wasting of the thigh from loss of blood.",
            "तत्ररक्तक्षयात्सक्थिशोषः."),
        order(1, "Put the words of unit 12 in the printed order.",
              ["ऊरुमध्ये", "उर्वी", "तत्र", "रक्तक्षयात्", "सक्थिशोषः"],
              "In the middle of the thigh; urvī; there; from loss of blood; wasting of the thigh.",
              "Place → name → cause → result."),
        match(2, "Match each word of unit 12 to its meaning.",
              [["ऊरु", "thigh"], ["मध्ये", "in the middle"], ["रक्त", "blood"], ["क्षय", "loss"], ["शोष", "wasting"]],
              "In the middle of the thigh; from loss of blood, wasting.",
              "ऊरु, मध्ये, रक्त, क्षय, शोष.", role="extend",
              teaches="शोष is wasting (drying up, thinning); क्षय is loss: रक्तक्षय = loss of blood."),
        mcq("discriminate", 3, "What does the ablative रक्तक्षयात् express in unit 12?",
            ("The cause: from loss of blood", "The ablative here names the cause of the wasting."),
            [("The place: in the lost blood", "Place would be the locative (-ए), not -आत्."),
             ("The owner: of the loss of blood", "Possession would be the genitive (-स्य)."),
             ("The object: the loss of blood itself", "An object would be accusative (-म्).")],
            "रक्तक्षयात् = from loss of blood: the cause.",
            "-आत् (a-stem ablative) can name a cause: 'from'."),
        mcq("apply", 4, "Which split of रक्तक्षयात्सक्थिशोषः in unit 12 is right?",
            ("रक्तक्षयात् + सक्थिशोषः", "त् stays before स: रक्तक्षयात् सक्थिशोषः."),
            [("रक्तक्षया + त्सक्थिशोषः", "त्सक्थिशोषः is not a word; the त् ends रक्तक्षयात्."),
             ("रक्तक्षयाः + सक्थिशोषः", "A visarga does not turn into त्; ः before स would stay ः or become स्."),
             ("रक्तक्षयम् + सक्थिशोषः", "म् before स would be written ं, not त्.")],
            "रक्तक्षयात् (from loss of blood) + सक्थिशोषः (wasting of the thigh).",
            "त् before स is unchanged."),
        mcq("transfer", 5, "By the pattern of रक्तक्षयात् (from loss of blood), which form of भय means from fear, in a new example?",
            ("भयात्", "-आत् is the ablative singular of a-stems, as क्षय → क्षयात्."),
            [("भयेन", "भयेन is the instrumental: by fear."),
             ("भये", "भये is the locative: in fear."),
             ("भयस्य", "भयस्य is the genitive: of fear.")],
            "भयात् = from fear, like रक्तक्षयात् = from loss of blood.",
            "a-stem, ablative singular: -आत्.",
            teaches="a-stems form the ablative singular in -आत्, which can name a cause: रक्तक्षयात्, भयात्."),
    ],
}

# ---------------------------------------------------------------- unit 13
AUTHORED["13"] = {
    "title": "ऊरुमूले लोहिताख्यं",
    "question": "By unit 13, where is lohita, and what is named there?",
    "rule": ("Above urvī and below the groin-joint (वङ्क्षणसन्धि), at the root of the thigh (ऊरुमूले), is the one named "
             "lohita ('red'); there, from loss of blood, pakṣāghāta (paralysis of one side, hemiplegia: standard)."),
    "limits": ("Prose. ऊर्व्याः may be genitive or ablative; no question rests on its case. 'marma' is understood with the "
               "neuter लोहिताख्यम्. pakṣāghāta = hemiplegia is the data's standard identification; nothing is added about "
               "its course."),
    "explain_hi": ("उर्वी के ऊपर और वंक्षण-सन्धि यानी जाँघ और पेड़ू के जोड़ के नीचे, ऊरु के मूल में, लोहित नामक मर्म है। "
                   "वहाँ रक्त के क्षय से पक्षाघात यानी शरीर के एक ओर का लकवा होता है (मानक पहचान)। "
                   "‘ऊर्व्याः’ षष्ठी या पञ्चमी दोनों हो सकता है; अर्थ ‘उर्वी के ऊपर’ ही रहता है। "
                   "‘लोहिताख्यम्’ नपुंसक है, इसलिए ‘मर्म’ संज्ञा समझी जाती है। "
                   "‘तूर्ध्वम्’ में तु + ऊर्ध्वम् (उ + ऊ → ऊ) और ‘अधो वंक्षण’ में अः घोष व्यंजन व से पहले ओ बना है।"),
    "hook": "जाँघ की जड़ में लोहित: रक्त घटे, आधा शरीर लकवाग्रस्त।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 13, what result is named at lohita?",
            ("Paralysis of one side", "रक्तक्षयात् पक्षाघातः: from loss of blood, paralysis of one side."),
            [("Wasting of the thigh", "Wasting of the thigh is named at urvī (unit 12)."),
             ("Lameness of the leg", "Lameness is named at the knee (unit 10)."),
             ("Death through pain", "Death through pain is named at talahṛdaya (unit 4).")],
            "At lohita: pakṣāghāta (hemiplegia).",
            "तत्र रक्तक्षयात्पक्षाघातः."),
        order(1, "Put the phrases of unit 13 in the printed order.",
              ["ऊर्व्यास्तूर्ध्वम्", "अधो वंक्षणसंधेः", "ऊरुमूले", "लोहिताख्यं", "तत्र रक्तक्षयात्पक्षाघातः"],
              "Above urvī; below the groin-joint; at the root of the thigh; the one named lohita; there, from loss of blood, paralysis of one side.",
              "Above → below → place → name → result."),
        match(2, "Match each word of unit 13 to its meaning.",
              [["ऊरुमूल", "root of the thigh"], ["वङ्क्षण", "groin"], ["लोहित", "red"], ["आख्य", "named"],
               ["पक्षाघात", "paralysis of one side"]],
              "At the thigh-root below the groin-joint, the one named 'red'; there, paralysis of one side.",
              "ऊरुमूल, वङ्क्षण, लोहित, आख्य, पक्षाघात.", role="extend",
              teaches="X-आख्य = named X (a bahuvrīhi): लोहिताख्यम् = (the marma) named lohita."),
        mcq("discriminate", 3, "Which split of ऊर्व्यास्तूर्ध्वम् in unit 13 is right?",
            ("ऊर्व्याः + तु + ऊर्ध्वम्", "Visarga before त → स्; उ + ऊ → ऊ: -स्तूर्ध्वम्."),
            [("ऊर्व्याः + तु + अर्ध्वम्", "उ before अ would become व्: -स्त्वर्ध्वम्."),
             ("ऊर्व्याः + त + ऊर्ध्वम्", "अ + ऊ would give ओ: -स्तोर्ध्वम्."),
             ("ऊर्व्याः + तुः + ऊर्ध्वम्", "उः before a vowel would give र्: -स्तुरूर्ध्वम्.")],
            "ऊर्व्याः + तु + ऊर्ध्वम्: ः → स् before त; उ + ऊ → ऊ.",
            "उ + ऊ → ऊ; visarga before त → स्."),
        mcq("apply", 4, "Where does unit 13 place lohita?",
            ("Above urvī, at the thigh-root", "ऊर्व्याः ऊर्ध्वम् ... ऊरुमूले: above urvī, at the root of the thigh, below the groin-joint."),
            [("Below urvī, a little above the knee", "Above the knee lies āṇi (unit 11); lohita is above urvī."),
             ("In the middle of the thigh itself", "The middle of the thigh is urvī (unit 12)."),
             ("Between the groin and the testes", "That is viṭapa (unit 14), not lohita.")],
            "Above urvī, below the groin-joint, at the thigh-root.",
            "ऊर्व्यास्तूर्ध्वमधो वंक्षणसंधेरूरुमूले लोहिताख्यं."),
        mcq("transfer", 5, "By the rule of पक्ष + आघात → पक्षाघात, how is देव + आलयः (temple) joined in a new example?",
            ("देवालयः", "अ + आ → आ, as पक्ष + आघातः → पक्षाघातः."),
            [("देवलयः", "The आ of आलयः does not shorten; अ + आ gives आ."),
             ("देवेलयः", "ए comes from अ + इ, not from अ + आ."),
             ("देवौलयः", "औ comes from अ + ओ or अ + औ, not from अ + आ.")],
            "देव + आलयः = देवालयः, like पक्ष + आघातः = पक्षाघातः.",
            "अ + आ → आ.",
            teaches="अ before आ joins to आ: पक्ष + आघातः → पक्षाघातः, लोहित + आख्यम् → लोहिताख्यम्."),
    ],
}


# ================================================================= NOTES_HI
NOTES_HI = {
    "1": ("गद्य; विश्वास उच्च; कोई पाठ-चिह्न नहीं। ‘शारीरम्’ को अध्याय (शारीर) का नाम पढ़ा गया; ‘विभागम्’ का विशेषण ‘शारीरिक’ भी "
          "सम्भव। सन्धि जाँची: अथ + अतः → अथातः (अ + अ → आ); अतः + मर्म → अतो मर्म (अः + घोष व्यंजन → ओ); मर्मविभागम् + शारीरम् → "
          "मर्मविभागं शारीरम् (व्यंजन से पहले अन्तिम म् → ं); व्याख्यास्यामः = भविष्यत्, उत्तम पुरुष बहुवचन।"),
    "2": ("गद्य; विश्वास मध्यम। पाठ-चिह्न (सम्भव): छपा ‘समोत्तरं’ कोई उपयोगी अर्थ नहीं देता; ‘सप्तोत्तरम्’ अनुमानित पाठ है (प्त → म "
          "इस छपाई की देखी गई भूल), और १०७ इसी पर तथा इकाई ३ के जोड़ पर टिका है; इस पर कोई प्रश्न नहीं। कोई क्रिया नहीं, जोड़ी नहीं गई। "
          "समूह-टिप्पणी: इकाई ३ की गिनती को खोलती दिखती है। पंक्ति-अन्त का ‘मर्मशतं’ छपाई में ं के साथ।"),
    "3": ("गद्य; विश्वास मध्यम। पाठ-चिह्न (सम्भव): छपा ‘समंत्रिश’ संख्या नहीं; ‘सप्तत्रिंशत्’ (३७) अनुमानित पाठ (प्त → म, और "
          "अनुस्वार त्रि के बजाय म पर), ४४ + २६ + ३७ = १०७ इकाई २ से मिलता है; इस पर कोई प्रश्न नहीं। ४४ और २६ छपे और पक्के। ‘ऊर्ध्वम्’ = "
          "ऊपरी भाग (गर्दन-सिर डेटा की टिप्पणी, पंक्ति में नहीं)। अन्तराधि = धड़ (मानक)। समूह-टिप्पणी: इकाई २ को आगे बढ़ाती दिखती है। "
          "सन्धि जाँची: चतुः + चत्वारिंशत् → चतुश्चत्वारिंशत् (च से पहले विसर्ग → श्); चतुश्चत्वारिंशत् + शाखासु → "
          "चतुश्चत्वारिंशच्छाखासु (त् + श → च्श, स्वर से पहले वैकल्पिक च्छ; छपा च्छ); षड्विंशतिः + अन्तराधौ → षड्विंशतिरन्तराधौ (इ के बाद विसर्ग + स्वर → र्)।"),
    "4": ("गद्य; विश्वास उच्च; कोई पाठ-चिह्न नहीं। ‘सक्थि’ इ-अन्त नपुंसक का सप्तमी रूप; मर्म तलवे में है, इसलिए अनुवाद ‘निचला अंग’ "
          "रखते हैं (डेटा की पुरानी टिप्पणी ‘thigh’ अब लागू नहीं)। ‘अभितः’ द्वितीया के साथ: समीप। मध्यमाङ्गुलि = यहाँ बीच की अंगुली। "
          "‘रुजया मरणम्’ पाठ का अपना शब्द, कुछ जोड़ा नहीं गया। सन्धि जाँची: अथ + एकैकस्मिन् → अथैकैकस्मिन् (अ + ए → ऐ); एक + एक → "
          "एकैक; एकैकस्मिन् + सक्थि → एकैकस्मिन्सक्थि (केवल जुड़ी छपाई); मध्यमाङ्गुलिम् + अभितः → मध्यमाङ्गुलिमभितः; अभितः + मध्ये → "
          "अभितो मध्ये (अः + घोष व्यंजन → ओ)।"),
    "5": ("गद्य; विश्वास मध्यम; कोई पाठ-चिह्न नहीं। ‘अगली अंगुली’ समझी गई, छपी नहीं; अङ्गुलि = हाथ या पैर की उँगली। ‘मर्म’ शब्द "
          "छपा नहीं, क्रम से समझा गया (इकाई ६: क्षिप्र के ऊपर)। आक्षेपक = ऐंठन का दौरा (सम्भावित)। छपाई क्षिप्रं + तत्र + आक्षेपकेण को "
          "जोड़ती है। सन्धि जाँची: अङ्गुष्ठ + अङ्गुल्योः → अङ्गुष्ठाङ्गुल्योः (अ + अ → आ); अङ्गुल्योः + मध्ये → अङ्गुल्योर्मध्ये (ओ के बाद "
          "विसर्ग + घोष → र्); तत्र + आक्षेपकेण → तत्राक्षेपकेण (अ + आ → आ)।"),
    "6": ("गद्य; विश्वास निम्न। पाठ-चिह्न (सम्भव): (१) ‘द्व्यंगुलउभयतः’ सम्भवतः ‘द्व्यङ्गुलम् उभयतः’ की भूल (इकाई २३-२४ का रूप); "
          "(२) ‘पादरुयभ्रमणवेपने’ बिगड़ा: ‘रुय’ कोई शब्द नहीं; ‘पाद-भ्रमण-वेपने’ (पाँव का घूमना और काँपना) अनुमानित पाठ, द्विवचन "
          "‘भवतः’ दो बातों से मेल खाता है; या ‘रुय’ = रुजा (पीड़ा) तो तीन बातें। फल पर कोई प्रश्न नहीं। ‘कूर्च्चः’ का दोहरा र्च्च "
          "छपाई की आदत (इकाई ७ में भी)। ‘उभयतः’ के कारण द्विवचन कूर्चौ भी अभिप्रेत हो सकता है; छपा एकवचन रखा गया। सन्धि जाँची: "
          "क्षिप्रस्य + उपरि → क्षिप्रस्योपरि (अ + उ → ओ); द्वि + अङ्गुल → द्व्यङ्गुल (इ + अ → य)।"),
    "7": ("गद्य; विश्वास मध्यम। पाठ-चिह्न (सम्भव): छपा ‘रुजाशोकौ’; शोक (दुःख) शरीर-लक्षण नहीं, इसलिए ‘शोफ’ (सूजन) अनुमानित पाठ "
          "(क/फ की भूल; तुलना इकाई ११ का शोफ); इस पर कोई प्रश्न नहीं, केवल रुजा (पीड़ा) पर। ‘कूर्च्च’ का दोहरा च छपाई की आदत। गुल्फ = "
          "टखना (मानक)। सन्धि जाँची: गुल्फसन्धेः + अधः → गुल्फसन्धेरधः (ए के बाद विसर्ग + स्वर → र्); रुजा + शोकौ → रुजाशोकौ "
          "(समास, कोई परिवर्तन नहीं)।"),
    "8": ("गद्य; विश्वास उच्च; कोई पाठ-चिह्न नहीं। अन्त का ‘वा’: तीनों लक्षण विकल्प। जडता = सुन्नपन या जड़ता। जङ्घा = घुटने से "
          "नीचे की टाँग, हिन्दी ‘जाँघ’ नहीं। ‘सक्थि’ यहाँ ‘जाँघ’ रखा गया; इकाई ४ की तरह पूरा पैर भी सम्भव। सन्धि जाँची: पाद + "
          "जङ्घयोः → पादजङ्घयोः (समास); छपे जंघ, संधान में ं = ङ्/न्; रुक् + स्तब्ध → रुक् स्तब्ध (कोई परिवर्तन नहीं)।"),
    "9": ("गद्य; विश्वास मध्यम। पाठ-चिह्न: (१) छपा ‘पाणि’ (हाथ) टाँग के माप में नहीं बैठता; ‘पार्ष्णि’ (एड़ी) अनुमानित पाठ (सम्भव), "
          "इस पर कोई प्रश्न नहीं; (२) छपा ‘क्ष्यात्’ = क्षयात् (लगभग निश्चित; अ छूटा)। इन्द्रबस्ति का ‘बस्ति’ मर्म-नाम का भाग, इकाई १९ "
          "का मूत्राशय नहीं। सन्धि जाँची: द्वादशभिः + अङ्गुलैः → द्वादशभिरङ्गुलैः (इ के बाद विसर्ग + स्वर → र्); अङ्गुलैः + जङ्घा → "
          "अङ्गुलैर्जङ्घा (ऐ के बाद विसर्ग + घोष → र्); क्षयात् + मरणम् → क्षयान्मरणम् (म से पहले त् → न्, वैकल्पिक; द् भी सही; छपा न्)।"),
    "10": ("गद्य; विश्वास उच्च; कोई पाठ-चिह्न नहीं। क्रिया नहीं, जोड़ी नहीं गई। जानु = घुटना (मानक)। सन्धि जाँची: जङ्घा + ऊर्वोः → "
           "जङ्घोर्वोः (आ + ऊ → ओ); द्वन्द्व, षष्ठी द्विवचन; छपा खंजता = खञ्जता।"),
    "11": ("गद्य; विश्वास उच्च; कोई पाठ-चिह्न नहीं। छपाई उभयतः और आणिः को जोड़ती है (उभयत आणिः)। आणि = कील, यहाँ मर्म-नाम। "
           "‘शोफाभिवृद्धिस्तब्ध’ में स्त से पहले विसर्ग लिखा नहीं गया (वैकल्पिक लोप का मान्य रूप); इस पर कोई प्रश्न नहीं। सन्धि जाँची: "
           "जानुनः + त्र्यङ्गुलात् → जानुनस्त्र्यङ्गुलात् (त से पहले विसर्ग → स्); त्रि + अङ्गुल → त्र्यङ्गुल (इ + अ → य); "
           "त्र्यङ्गुलात् + ऊर्ध्वम् → त्र्यङ्गुलादूर्ध्वम् (स्वर से पहले त् → द्); ऊर्ध्वम् + उभयतः → ऊर्ध्वमुभयतः; उभयतः + आणिः → उभयत "
           "आणिः (अः + अ से भिन्न स्वर → अ); शोफ + अभिवृद्धिः → शोफाभिवृद्धिः (अ + अ → आ)।"),
    "12": ("गद्य; विश्वास उच्च; कोई पाठ-चिह्न नहीं। छपाई ‘तत्ररक्तक्षयात्’ बिना अन्तर (सन्धि नहीं)। उर्वी = मर्म-नाम (शब्दार्थ "
           "‘चौड़ी’)। रक्तक्षयात् पञ्चमी: कारण। सन्धि जाँची: ऊरुमध्ये उर्वी अलग (ए के बाद उ, छपाई में अन्तर); रक्तक्षयात् + सक्थि → "
           "रक्तक्षयात्सक्थि (स से पहले त् अपरिवर्तित)।"),
    "13": ("गद्य; विश्वास उच्च; कोई पाठ-चिह्न नहीं। ऊर्व्याः षष्ठी या पञ्चमी, दोनों सम्भव; ‘ऊर्ध्वम्’ उसी से, ‘अधः’ वंक्षणसन्धि से। "
           "‘मर्म’ संज्ञा लोहिताख्यम् (नपुंसक) के साथ समझी गई। पक्षाघात = एक ओर का लकवा (मानक)। सन्धि जाँची: ऊर्व्याः + तु → "
           "ऊर्व्यास्तु (त से पहले विसर्ग → स्); तु + ऊर्ध्वम् → तूर्ध्वम् (उ + ऊ → ऊ); ऊर्ध्वम् + अधः → ऊर्ध्वमधः; अधः + वङ्क्षण → अधो "
           "वङ्क्षण (अः + घोष व्यंजन → ओ); वङ्क्षणसन्धेः + ऊरुमूले → वङ्क्षणसन्धेरूरुमूले (ए के बाद विसर्ग + स्वर → र्); लोहित + आख्यम् → "
           "लोहिताख्यम्; पक्ष + आघातः → पक्षाघातः (अ + आ → आ)।"),
}


# ===================================================================== AIDS
AIDS = {
    "1": {
        "chunks": "अथातो | मर्मविभागं | शारीरं | व्याख्यास्यामः",
        "frame": "कब: अथ (अब) → क्यों: अतः (इसलिए) → क्या: मर्मविभागं शारीरं → कौन करेगा: व्याख्यास्यामः (हम व्याख्या करेंगे)।",
        "sandhi": "अ + अ → आ: अथ + अतः → अथातः · अः + घोष व्यंजन → ओ: अतः + मर्म → अतो मर्म।",
    },
    "2": {
        "frame": "कितने: शतम् (सौ, पक्का) + ऊपर की संख्या (छपा ‘समोत्तरं’, अनुमान से ‘सप्तोत्तरम्’) → किसके: मर्म।",
        "chunks": "समोत्तरं | मर्मशतं",
        "anchors": "पक्का भाग: मर्मशतं = सौ मर्म। संदिग्ध भाग: ‘समोत्तरं’ (अनुमान: सात अधिक)। (मेरी याद-पद्धति)",
    },
    "3": {
        "diagram": {"groups": [
            {"label": "तत्र: मर्मों का बँटवारा", "items": ["शाखासु: ४४ (पक्का)", "अन्तराधौ: २६ (पक्का)",
                                                    "ऊर्ध्वम्: ३७ (अनुमानित पाठ)"]}]},
        "chunks": "तत्र | चतुश्चत्वारिंशच्छाखासु | षड्विंशतिरंतराधौ | समंत्रिशदूर्ध्वं",
        "sandhi": ("त् + श → च्श, स्वर से पहले वैकल्पिक च्छ: चतुश्चत्वारिंशत् + शाखासु → चतुश्चत्वारिंशच्छाखासु · इ के बाद विसर्ग + स्वर → र्: "
                   "षड्विंशतिः + अन्तराधौ → षड्विंशतिरन्तराधौ।"),
    },
    "4": {
        "chain": {"steps": ["एकैकस्मिन् सक्थि: प्रत्येक निचले अंग में", "मध्यमा अंगुली के समीप", "पादतल के बीच",
                            "तलहृदय नामक मर्म", "वहाँ विद्ध होने पर", "रुजा (पीड़ा) से मरण"]},
        "chunks": "अथैकैकस्मिन्सक्थि | मध्यमांगुलिमभितो | मध्ये पादतलस्य | तलहृदयं नाम मर्म | तत्र विद्धस्य | रुजया मरणं",
        "sandhi": "अ + ए → ऐ: अथ + एकैकस्मिन् → अथैकैकस्मिन्; एक + एक → एकैक · अः + घोष व्यंजन → ओ: अभितः + मध्ये → अभितो मध्ये।",
        "puns": "‘तल-हृदय’ = तलवे का हृदय: तलवे के ठीक बीच का स्थान। (केवल सुनने की सहायता, मेरा बनाया)",
    },
    "5": {
        "diagram": {"groups": [
            {"label": "क्षिप्र", "items": ["कहाँ: अँगूठे और अंगुली के बीच", "फल: आक्षेपक (सम्भवतः ऐंठन) से मरण"]}]},
        "chunks": "अंगुष्ठांगुल्योर्मध्ये | क्षिप्रं | तत्र | आक्षेपकेण | मरणं",
        "sandhi": "ओ के बाद विसर्ग + घोष → र्: अङ्गुल्योः + मध्ये → अङ्गुल्योर्मध्ये · अ + आ → आ: तत्र + आक्षेपकेण → तत्राक्षेपकेण।",
        "puns": "‘क्षिप्र’ = शीघ्र: नाम ही जल्दी का संकेत देता है। (केवल सुनने की सहायता, मेरा बनाया; पाठ यह कारण नहीं बताता)",
    },
    "6": {
        "frame": "किसके ऊपर: क्षिप्रस्य उपरि → कितनी दूरी: दो अंगुल → किस ओर: उभयतः (दोनों ओर) → नाम: कूर्च → फल: शब्द बिगड़ा (अनुमानित पाठ)।",
        "chunks": "क्षिप्रस्योपरि | द्व्यंगुलउभयतः | कूर्च्चः | तत्र | पादरुयभ्रमणवेपने | भवतः",
        "sandhi": "अ + उ → ओ: क्षिप्रस्य + उपरि → क्षिप्रस्योपरि · इ + अ → य: द्वि + अङ्गुल → द्व्यङ्गुल।",
    },
    "7": {
        "frame": "किसके नीचे: गुल्फसन्धेः अधः (टखने के जोड़ के नीचे) → नाम: कूर्चशिर → फल: रुजा (पक्का) + दूसरा लक्षण (छपा शोक, अनुमान से शोफ)।",
        "chunks": "गुल्फसंधेरधः | कूर्च्चशिरः | तत्र | रुजाशोकौ",
        "sandhi": "ए के बाद विसर्ग + स्वर → र्: गुल्फसन्धेः + अधः → गुल्फसन्धेरधः।",
    },
    "8": {
        "diagram": {"groups": [
            {"label": "गुल्फ: पैर और जंघा का जोड़", "items": ["रुक्: पीड़ा", "स्तब्धसक्थिता: सक्थि की अकड़न",
                                                          "जडता: सुन्नपन", "वा: तीनों विकल्प"]}]},
        "chunks": "पादजंघयोः संधाने | गुल्फः | तत्र रुक् | स्तब्धसक्थिता | जडता वा",
        "frame": "कहाँ: पादजङ्घयोः सन्धाने (पैर और जङ्घा यानी घुटने से नीचे की टाँग का जोड़) → नाम: गुल्फ → फल: रुक्, स्तब्धसक्थिता, जडता → जोड़ने वाला: वा (अथवा)।",
    },
    "9": {
        "chain": {"steps": ["आरम्भ: छपा पाणि (अनुमान से एड़ी)", "बारह अंगुल पर", "जंघा के बीच", "इन्द्रबस्ति",
                            "शोणित-क्षय से मरण"]},
        "chunks": "पाणिप्रभृति | द्वादशभिरंगुलैर्जंघामध्ये | इंद्रबस्तिः | तत्र | शोणितक्ष्यान्मरणं",
        "sandhi": ("इ के बाद विसर्ग + स्वर → र्: द्वादशभिः + अङ्गुलैः → द्वादशभिरङ्गुलैः · ऐ के बाद विसर्ग + घोष → र्: "
                   "अङ्गुलैः + जङ्घा → अङ्गुलैर्जङ्घा · म (अनुनासिक) से पहले त् → न्, वैकल्पिक (द् भी सही; छपा न्): क्षयात् + मरणम् → क्षयान्मरणम्।"),
    },
    "10": {
        "frame": "किन दोनों का जोड़: जङ्घा + ऊरु → नाम: जानु (घुटना) → फल: खञ्जता (लंगड़ापन)।",
        "chunks": "जंघोर्वोः | संधाने | जानु | तत्र | खंजता",
        "sandhi": "आ + ऊ → ओ: जङ्घा + ऊर्वोः → जङ्घोर्वोः।",
    },
    "11": {
        "diagram": {"groups": [
            {"label": "आणि: घुटने से ३ अंगुल ऊपर, दोनों ओर", "items": ["शोफाभिवृद्धि: सूजन का बढ़ना",
                                                                   "स्तब्धसक्थिता: सक्थि की अकड़न", "च: दोनों साथ"]}]},
        "chunks": "जानुनस्त्र्यंगुलादूर्ध्वमुभयतआणिः | तत्र | शोफाभिवृद्धिस्तब्धसक्थिता च",
        "sandhi": ("त से पहले विसर्ग → स्: जानुनः + त्र्यङ्गुलात् → जानुनस्त्र्यङ्गुलात् · स्वर से पहले त् → द्: त्र्यङ्गुलात् + "
                   "ऊर्ध्वम् → त्र्यङ्गुलादूर्ध्वम् · अः + अ से भिन्न स्वर → अ: उभयतः + आणिः → उभयत आणिः।"),
    },
    "12": {
        "chain": {"steps": ["ऊरु के बीच", "उर्वी", "रक्त-क्षय से", "सक्थि-शोष: जाँघ का सूखना"]},
        "chunks": "ऊरुमध्ये | उर्वी | तत्ररक्तक्षयात्सक्थिशोषः",
        "frame": "कहाँ: ऊरुमध्ये → नाम: उर्वी → कारण: रक्तक्षयात् (पञ्चमी) → फल: सक्थिशोषः।",
    },
    "13": {
        "chain": {"steps": ["उर्वी के ऊपर", "वंक्षण-सन्धि के नीचे", "ऊरु-मूल में", "लोहित नामक मर्म",
                            "रक्त-क्षय से पक्षाघात"]},
        "chunks": "ऊर्व्यास्तूर्ध्वमधो | वंक्षणसंधेरूरुमूले | लोहिताख्यं | तत्र | रक्तक्षयात्पक्षाघातः",
        "sandhi": ("उ + ऊ → ऊ: तु + ऊर्ध्वम् → तूर्ध्वम् · अः + घोष व्यंजन → ओ: अधः + वङ्क्षण → अधो वङ्क्षण · ए के बाद विसर्ग + "
                   "स्वर → र्: वङ्क्षणसन्धेः + ऊरुमूले → वङ्क्षणसन्धेरूरुमूले · अ + आ → आ: पक्ष + आघातः → पक्षाघातः।"),
        "anchors": "उर्वी (जाँघ का बीच, इकाई १२) → उसके ऊपर लोहित: दोनों में कारण रक्त-क्षय, फल अलग: शोष ⇄ पक्षाघात। (मेरी याद-पद्धति)",
    },
}


# ============================================================== IMAGE_SPECS
IMAGE_SPECS = {
    ("3", "diagram"): {
        "file": "sh7-marma-sankhya-3.svg",
        "alt": ("Table of unit 3: forty-four marmas in the limbs (sure), twenty-six in the trunk (sure), thirty-seven "
                "above (conjectural reading)."),
        "type": "table",
        "title": "इकाई ३: मर्मों का बँटवारा",
        "heads": ["कहाँ", "संख्या"],
        "rows": [["शाखासु (हाथ-पैर)", "४४ (पक्का)"], ["अन्तराधौ (धड़)", "२६ (पक्का)"],
                 ["ऊर्ध्वम् (ऊपर)", "३७ (अनुमानित पाठ)"]],
    },
    ("4", "chain"): {
        "file": "sh7-talahridaya-4.svg",
        "alt": ("Flowchart of unit 4 in line order: in each lower limb; near the middle toe; in the middle of the sole; "
                "the marma talahṛdaya; for one pierced there; death through pain."),
        "type": "mermaid",
        "code": ("flowchart TD\n"
                 "  A[\"१ प्रत्येक निचले अंग में\"] --> B[\"२ मध्यमा अंगुली के समीप\"]\n"
                 "  B --> C[\"३ पादतल के बीच\"]\n"
                 "  C --> D[\"४ तलहृदय नामक मर्म\"]\n"
                 "  D --> E[\"५ वहाँ विद्ध होने पर\"]\n"
                 "  E --> F[\"६ रुजा से मरण\"]\n"),
    },
    ("8", "diagram"): {
        "file": "sh7-gulpha-8.svg",
        "alt": ("Flowchart of unit 8: the joining of foot and shank is gulpha (the ankle); there, as alternatives (or), "
                "pain, stiffness of the sakthi, or numbness."),
        "type": "mermaid",
        "code": ("flowchart TD\n"
                 "  A[\"पैर और जंघा का जोड़\"] --> B[\"गुल्फ (टखना)\"]\n"
                 "  B --> C[\"वा: अथवा (विकल्प)\"]\n"
                 "  C --> D[\"रुक्: पीड़ा\"]\n"
                 "  C --> E[\"सक्थि की अकड़न\"]\n"
                 "  C --> F[\"जडता: सुन्नपन\"]\n"),
    },
    ("9", "chain"): {
        "file": "sh7-indrabasti-9.svg",
        "alt": ("Chain of unit 9: starting point printed pāṇi, read by conjecture as the heel; at twelve aṅgulas; in "
                "the middle of the shank; indrabasti; death from loss of blood."),
        "type": "chain",
        "title": "इकाई ९: इन्द्रबस्ति",
        "steps": ["आरम्भ: छपा पाणि (अनुमान से एड़ी)", "बारह अंगुल पर", "जंघा के बीच", "इन्द्रबस्ति",
                  "शोणित-क्षय से मरण"],
    },
    ("11", "diagram"): {
        "file": "sh7-ani-11.svg",
        "alt": ("Flowchart of unit 11: three aṅgulas above the knee, on both sides, is āṇi; there, joined by 'and', "
                "increase of swelling and stiffness of the sakthi."),
        "type": "mermaid",
        "code": ("flowchart TD\n"
                 "  A[\"घुटने से ३ अंगुल ऊपर\"] --> B[\"दोनों ओर: आणि\"]\n"
                 "  B --> C[\"च: दोनों साथ\"]\n"
                 "  C --> D[\"सूजन का बढ़ना\"]\n"
                 "  C --> E[\"सक्थि की अकड़न\"]\n"),
    },
    ("12", "chain"): {
        "file": "sh7-urvi-12.svg",
        "alt": ("Chain of unit 12: in the middle of the thigh; urvī; from loss of blood; wasting of the thigh."),
        "type": "chain",
        "title": "इकाई १२: उर्वी",
        "steps": ["ऊरु के बीच", "उर्वी", "रक्त-क्षय से", "सक्थि-शोष: जाँघ का सूखना"],
    },
    ("13", "chain"): {
        "file": "sh7-lohita-13.svg",
        "alt": ("Flowchart of unit 13 in line order: above urvī; below the groin-joint; at the root of the thigh; the "
                "marma named lohita; from loss of blood, paralysis of one side."),
        "type": "mermaid",
        "code": ("flowchart TD\n"
                 "  A[\"१ उर्वी के ऊपर\"] --> B[\"२ वंक्षण-सन्धि के नीचे\"]\n"
                 "  B --> C[\"३ ऊरु-मूल में\"]\n"
                 "  C --> D[\"४ लोहित नामक मर्म\"]\n"
                 "  D --> E[\"५ रक्त-क्षय से पक्षाघात\"]\n"),
    },
}
