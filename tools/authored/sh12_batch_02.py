from helpers import mcq, match, order, fill, multi, accepts


def T(q, teaches):
    q["teaches"] = teaches
    return q


AUTHORED = {}

# ---------------------------------------------------------------- unit 14
AUTHORED["14"] = {
    "title": "कीर्तनमिष्टं न दर्शनं",
    "question": "By card 14, for the hare, snake, goat, sheep and monitor lizard, is the mention or the sight desired?",
    "rule": ("For the hare, snake, goat, sheep, monitor lizard (godhā, standard) and others of the list, the mention "
             "(कीर्तनम्) is desired (इष्टम्), not the sight (न दर्शनम्); for the last pair the reverse (विपरीतम्) holds."),
    "limits": ("Prose, low confidence. राजाहक is unclear and boar (sūkara) is a conjecture for printed मूकर; the last pair "
               "is read ṛkṣa-vānara (bear and monkey) only after dropping a stray म् of मृक्ष. Whether the cry (विरुतम्) is "
               "desired is only the natural reading. No question on राजाहक, the boar, the bear or the cry."),
    "explain_hi": ("खरगोश, साँप, बकरी, भेड़ और गोह (मानक पहचान) आदि का नाम लेना (कीर्तनम्) इष्ट है, उनका दर्शन नहीं। "
                   "सूची का ‘राजाहक’ अस्पष्ट है और छपा ‘मूकर’ अनुमान से सूकर (सूअर) पढ़ा गया है। "
                   "‘विरुतं च’ (और ध्वनि) पर भी ‘इष्टम्’ सहज पाठ से लागू माना गया है, पर यह पक्का नहीं। "
                   "अन्तिम जोड़े (छपा ‘मृक्षवानरयोः’, पढ़ा: रीछ और वानर) के लिए उलटा (विपरीतम्) कहा गया है। "
                   "‘कीर्तनमिष्टं’ में कीर्तनम् + इष्टम् की सन्धि है: स्वर से पहले अन्तिम म् अगले स्वर से जुड़ता है।"),
    "hook": "इन जीवों का नाम लो, इन्हें देखो नहीं: कीर्तनमिष्टं न दर्शनं।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "In card 14, what does कीर्तनम् mean?",
            ("Mention, naming", "कीर्तनम् = mention, naming: the creature's name spoken."),
            [("Sight, seeing", "Sight is दर्शनम्, a separate word of card 14."),
             ("Touch, contact", "Touch would be स्पर्शनम्; कीर्तनम् is mention."),
             ("Cry, calling", "The cry is विरुतम्, a separate word of card 14.")],
            "कीर्तनम् = mention, naming.",
            "कीर्तनम् = mention."),
        match(1, "Match each word of card 14 to its meaning.",
              [["कीर्तनम्", "mention"], ["इष्टम्", "desired"], ["दर्शनम्", "sight"], ["विरुतम्", "cry"],
               ["विपरीतम्", "reverse"]],
              "कीर्तनम् = mention, इष्टम् = desired, दर्शनम् = sight, विरुतम् = cry, विपरीतम् = reverse.",
              "कीर्तनम्, इष्टम्, दर्शनम्, विरुतम्, विपरीतम्."),
        order(2, "Put these printed parts of card 14 in the printed order.",
              ["कीर्तनमिष्टं", "न दर्शनं", "विरुतं", "चविपरीतंमृक्षवानरयोः"],
              "Mention desired; not the sight; the cry; and the reverse for the last pair.",
              "कीर्तनमिष्टं → न दर्शनं → विरुतं → चविपरीतंमृक्षवानरयोः.",
              role="extend",
              teaches=("After the list of creatures and तु (but), card 14 says what is desired (the mention), what is not "
                       "(the sight), and ends with the reverse case for one pair.")),
        mcq("discriminate", 3, "By card 14, what is desired for the hare, snake, goat and sheep?",
            ("Their mention, not their sight", "कीर्तनमिष्टं न दर्शनं: the mention is desired, the sight is not."),
            [("Their sight, not their mention", "That reverses card 14, which says कीर्तनमिष्टं न दर्शनं."),
             ("Both their sight and their mention", "न दर्शनं: their sight is not desired."),
             ("Neither sight nor mention", "कीर्तनमिष्टं: their mention is desired.")],
            "Mention (कीर्तनम्) desired; sight (दर्शनम्) not.",
            "कीर्तनम् इष्टम्, न दर्शनम्."),
        mcq("apply", 4, "Which split of कीर्तनमिष्टं in card 14 is right?",
            ("कीर्तनम् + इष्टम्", "Final म् before a vowel joins it: कीर्तनम् + इष्टम् → कीर्तनमिष्टम्."),
            [("कीर्तनम् + ईष्टम्", "A long ई would print कीर्तनमीष्टं; the print has short मि."),
             ("कीर्तनमि + इष्टम्", "इ + इ would merge into ई; कीर्तनमि is not a word."),
             ("कीर्तनम + इष्टम्", "अ + इ would give ए (कीर्तनमेष्टं); the noun is कीर्तनम्.")],
            "कीर्तनम् (mention) + इष्टम् (desired).",
            "Final म् + vowel → written together (म् + इ = मि)."),
        mcq("transfer", 5, "By the pattern of कीर्तनमिष्टं, how is फलम् + इच्छति (he wants the fruit) written in a new example?",
            ("फलमिच्छति", "Final म् before a vowel joins it: फलम् + इच्छति → फलमिच्छति."),
            [("फलं इच्छति", "ं stands for म् only before a consonant; before a vowel म् joins the vowel."),
             ("फलेच्छति", "ए comes from अ + इ; here म् stands between the vowels."),
             ("फलमीच्छति", "The verb has short इ; joining does not lengthen it.")],
            "फलम् + इच्छति = फलमिच्छति, like कीर्तनम् + इष्टम् = कीर्तनमिष्टम्.",
            "Final म् + vowel → म joined with the vowel.",
            teaches="A final म् before a vowel is not written ं; it joins the vowel: कीर्तनम् + इष्टम् → कीर्तनमिष्टम्."),
    ],
}

# ---------------------------------------------------------------- unit 15
AUTHORED["15"] = {
    "title": "सर्वमपि त्वनिष्टं",
    "question": "By card 15, which creatures are wholly undesired?",
    "rule": ("Everything (सर्वम् अपि) of the saraṭa (probably the chameleon or garden lizard), the fowl (कुक्कुट), the cat "
             "(विडाल) and owls (उलूक) is undesired (अनिष्टम्)."),
    "limits": ("Prose, medium confidence. सर्वम् presumably covers sight, mention and cry of the earlier cards, but the line "
               "does not say so: no question on which of these it covers. saraṭa is only probably the chameleon: no question "
               "on its identity."),
    "explain_hi": ("सरट (सम्भवतः गिरगिट या बगीचे की छिपकली), मुर्गा, बिल्ली और उल्लू: इनका तो सब कुछ ही अनिष्ट है। "
                   "‘सर्वम्’ सम्भवतः पिछले कार्डों के दर्शन, नाम और ध्वनि को समेटता है, पर पंक्ति यह नहीं कहती। "
                   "चारों जीव एक द्वन्द्व समास में हैं, जिसके अन्त में षष्ठी बहुवचन -आनाम् है। "
                   "‘त्वनिष्टं’ में तु + अनिष्टम् की सन्धि है: उ के बाद भिन्न स्वर आने पर उ → व्।"),
    "hook": "मुर्गा, बिल्ली, उल्लू: सर्वमपि त्वनिष्टं।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "In card 15, what does अनिष्टम् mean?",
            ("Undesired", "अन्- (not) + इष्टम् (desired): undesired."),
            [("Much desired", "Desired is इष्टम्; the prefix अन्- negates it."),
             ("Never seen", "Unseen would be अदृष्टम्; अनिष्टम् = undesired."),
             ("Not named", "Unnamed would be अनामक; अनिष्टम् = undesired.")],
            "अनिष्टम् = undesired.",
            "अन् + इष्ट = undesired."),
        match(1, "Match each word of card 15 to its meaning.",
              [["सर्वम्", "all, everything"], ["अपि", "also, even"], ["अनिष्टम्", "undesired"], ["कुक्कुट", "fowl"],
               ["विडाल", "cat"], ["उलूक", "owl"]],
              "सर्वम् = all, अपि = also, अनिष्टम् = undesired, कुक्कुट = fowl, विडाल = cat, उलूक = owl.",
              "सर्वम्, अपि, अनिष्टम्, कुक्कुट, विडाल, उलूक."),
        order(2, "Put the creatures of card 15 in the printed order.",
              ["सरट", "कुक्कुट", "विडाळ", "उलूक"],
              "सरट (probably the chameleon), fowl, cat, owl: one dvandva compound.",
              "सरट → कुक्कुट → विडाळ → उलूक.",
              role="extend",
              teaches="One dvandva compound lists the four creatures; its genitive plural ending -आनाम् (of) covers all of them."),
        mcq("discriminate", 3, "Which split of त्वनिष्टं in card 15 is right?",
            ("तु + अनिष्टम्", "उ before a different vowel → व्: तु + अनिष्टम् → त्वनिष्टम्."),
            [("तु + निष्टम्", "No join would happen: it would print तु निष्टं."),
             ("तौ + अनिष्टम्", "औ + अ would give आव्: तावनिष्टं."),
             ("त्व + निष्टम्", "त्व and निष्टम् are not the words; the व् comes from तु.")],
            "तु (but) + अनिष्टम् (undesired): उ + अ → व.",
            "उ + unlike vowel → व्."),
        multi("apply", 4, "Which of these creatures does card 15 name in its list of the wholly undesired?",
              [("कुक्कुट, the fowl", "Right: कुक्कुट is in the list of card 15."),
               ("शश, the hare", "No: the hare is in card 14, where its mention is desired."),
               ("उलूक, the owl", "Right: उलूक is the last of the list."),
               ("अजा, the goat", "No: the goat is in card 14, where its mention is desired.")],
              [0, 2],
              "Card 15 names saraṭa, fowl, cat and owl; hare and goat belong to card 14.",
              "सरट, कुक्कुट, विडाल, उलूक: सर्वम् अनिष्टम्."),
        mcq("transfer", 5, "By the pattern of तु + अनिष्टम् → त्वनिष्टम्, how is मधु + अस्ति (there is honey) joined in a new example?",
            ("मध्वस्ति", "उ before a different vowel → व्: मधु + अस्ति → मध्वस्ति."),
            [("मधोस्ति", "ओ comes from अ + उ, not from उ + अ."),
             ("मधूस्ति", "ऊ comes from उ + उ; here the second vowel is अ."),
             ("मध्वास्ति", "The अ of अस्ति stays short; no आ arises.")],
            "मधु + अस्ति = मध्वस्ति, like तु + अनिष्टम् = त्वनिष्टम्.",
            "उ + unlike vowel → व् + vowel.",
            teaches="A final उ before a different vowel becomes व्: तु + अनिष्टम् → त्वनिष्टम्."),
    ],
}

# ---------------------------------------------------------------- unit 16
AUTHORED["16"] = {
    "title": "तथा ग्रंथ्यर्बुदादिषु",
    "question": "By card 16, which word is desired for each group of diseases?",
    "rule": ("Granthi, arbuda and the like: the word 'cutting' (छेद); gulma, udara and the like: 'breaking' (भेद); atisāra, "
             "raktapitta and the like: 'stopped' (रुद्ध); aśmarī, udāvarta and the like: 'impelling' (प्रवर्तन)."),
    "limits": ("Prose, medium confidence. इष्टः is printed once and carried to the later pairs. gulma (abdominal lump), udara "
               "(abdominal disease) and udāvarta are probable identifications; the others are standard. The line gives no "
               "reason for the pairing and the card adds none."),
    "explain_hi": ("जैसे पहले, यहाँ रोग के अनुसार इष्ट शब्द बताए गए हैं। "
                   "ग्रन्थि (गाँठ) और अर्बुद (रसौली) आदि में ‘छेद’ शब्द इष्ट है; गुल्म (पेट की गाँठ, सम्भावित) और उदर (सम्भवतः पेट का रोग) आदि में ‘भेद’। "
                   "अतिसार (दस्त) और रक्तपित्त (रक्तस्राव का रोग) आदि में ‘रुद्ध’; अश्मरी (पथरी) और उदावर्त (सम्भावित: वायु का ऊपर पलटना) आदि में ‘प्रवर्तन’। "
                   "‘इष्टः’ एक बार छपा है और आगे के जोड़ों पर भी लागू है। "
                   "‘छेदशब्दइष्टो’ में अलग इ नियमित है: अः के बाद अ से भिन्न स्वर आने पर विसर्ग लुप्त होता है और स्वर नहीं मिलते।"),
    "hook": "गाँठ: छेद; गुल्म: भेद; दस्त: रुद्ध; पथरी: प्रवर्तन।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "In card 16, what does छेद mean?",
            ("Cutting", "छेद = cutting: the word desired for granthi, arbuda and the like."),
            [("Breaking", "Breaking is भेद, the word for gulma and udara."),
             ("Stopping", "Stopped is रुद्ध, the word for atisāra and raktapitta."),
             ("Burning", "Burning would be दाह; छेद = cutting.")],
            "छेद = cutting.",
            "छेद = cutting."),
        match(1, "Match each disease group of card 16 to the word desired for it.",
              [["ग्रन्थि, अर्बुद आदि", "छेद (cutting)"], ["गुल्म, उदर आदि", "भेद (breaking)"],
               ["अतिसार, रक्तपित्त आदि", "रुद्ध (stopped)"], ["अश्मरी, उदावर्त आदि", "प्रवर्तन (impelling)"]],
              "Nodule and tumour: cutting; gulma and udara: breaking; diarrhoea and raktapitta: stopped; stone and udāvarta: impelling.",
              "ग्रन्थि → छेद, गुल्म → भेद, अतिसार → रुद्ध, अश्मरी → प्रवर्तन."),
        order(2, "Put the desired words of card 16 in the printed order.",
              ["छेदशब्द", "भेदशब्द", "रुद्धशब्द", "प्रवर्त्तनशब्द"],
              "Cutting, breaking, stopped, impelling: each follows its disease group.",
              "छेद → भेद → रुद्ध → प्रवर्तन.",
              role="extend",
              teaches=("Each disease group stands in the locative (-आदिषु, in ... and the like) and is followed by its word; "
                       "इष्टः (desired) is printed once and carried to the rest.")),
        mcq("discriminate", 3, "Why is छेदशब्दइष्टो printed with a separate इ in card 16?",
            ("After अ, ः drops before इ; no merging", "शब्दः + इष्टः → शब्द इष्टः: regular hiatus, as the data says."),
            [("It is a misprint for छेदशब्देष्टो in the source", "The data calls it regular hiatus after -अः, not a typo."),
             ("अः before the vowel इ always becomes ओ", "ओ comes before a voiced consonant (इष्टो गुल्म-), not before इ."),
             ("ः after अ becomes र् before the vowel इ", "र् comes after vowels other than अ/आ; here ः follows अ.")],
            "शब्दः + इष्टः: अः before a vowel other than अ → अ, and the vowels stay apart.",
            "अः + vowel other than अ → अ (hiatus)."),
        mcq("apply", 4, "A case of atisāra (diarrhoea): by card 16, which word is desired?",
            ("रुद्ध (stopped)", "अतिसाररक्तपित्तादिषु रुद्धशब्दः: in atisāra and the like, 'stopped'."),
            [("छेद (cutting)", "Cutting is for granthi, arbuda and the like."),
             ("भेद (breaking)", "Breaking is for gulma, udara and the like."),
             ("प्रवर्तन (impelling)", "Impelling is for aśmarī, udāvarta and the like.")],
            "Atisāra and raktapitta → रुद्ध.",
            "अतिसार → रुद्धशब्दः इष्टः."),
        mcq("transfer", 5, "By the pattern of शब्दः + इष्टः → शब्द इष्टः, how is अश्वः + इव (like a horse) written in a new example?",
            ("अश्व इव", "अः before a vowel other than अ → अ, and the vowels stay apart: अश्व इव."),
            [("अश्वो इव", "ओ comes before a voiced consonant, not before a vowel."),
             ("अश्वेव", "No merging: once ः is dropped the two vowels stay apart."),
             ("अश्वरिव", "र् comes after vowels other than अ/आ; here ः follows अ.")],
            "अश्वः + इव = अश्व इव, like शब्दः + इष्टः = शब्द इष्टः.",
            "अः + vowel other than अ → अ, with a gap.",
            teaches="अः before a vowel other than अ loses its visarga and the vowels do not merge: शब्दः + इति → शब्द इति."),
    ],
}

# ---------------------------------------------------------------- unit 17
AUTHORED["17"] = {
    "title": "एवमन्येपि ध्वनयो योज्याः",
    "question": "What does card 17 say about sounds not named before?",
    "rule": "In this way (एवम्) other (अन्ये) sounds (ध्वनयः) too (अपि) are to be applied (योज्याः) by the same principle.",
    "limits": ("Prose, high confidence. The line names no further sounds; that they follow the principle of card 16 is the "
               "data's reading of योज्याः. The avagraha of अन्येऽपि is not printed."),
    "explain_hi": ("इसी प्रकार दूसरी ध्वनियाँ भी जोड़ी (लागू की) जानी चाहिए। "
                   "यानी जो ध्वनियाँ नाम लेकर नहीं कही गईं, उन्हें भी पिछले कार्ड के सिद्धान्त से समझा जाए; पंक्ति इससे अधिक नहीं कहती। "
                   "‘योज्याः’ √युज् का कृत्य प्रत्यय वाला रूप है: ‘जोड़ने योग्य’। "
                   "‘अन्येपि’ में अन्ये + अपि है: ए के बाद अ लुप्त होता है (सामान्यतः ऽ लिखा जाता, यहाँ छपा नहीं)।"),
    "hook": "बाकी ध्वनियाँ भी इसी नियम से: एवमन्येपि ध्वनयो योज्याः।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "In card 17, what does योज्याः mean?",
            ("To be applied", "योज्याः = to be applied, fitted (gerundive of √युज्)."),
            [("Were forbidden", "Forbidden is प्रतिषिद्धाः (card 19); योज्याः = to be applied."),
             ("Were never heard", "Nothing in योज्याः means hearing; it is from √युज्, join."),
             ("Are fruitless", "Fruitless is अफलः (card 21); योज्याः = to be applied.")],
            "योज्याः = to be applied.",
            "योज्य = to be applied."),
        match(1, "Match each word of card 17 to its meaning.",
              [["एवम्", "in this way"], ["अन्ये", "other"], ["अपि", "also"], ["ध्वनयः", "sounds"],
               ["योज्याः", "to be applied"]],
              "एवम् = in this way, अन्ये = other, अपि = also, ध्वनयः = sounds, योज्याः = to be applied.",
              "एवम्, अन्ये, अपि, ध्वनयः, योज्याः."),
        mcq("extend", 2, "What kind of form is योज्याः in card 17?",
            ("A gerundive: 'to be applied'", "योज्य from √युज्: what is to be done; masculine plural with ध्वनयः."),
            [("A past participle: 'applied'", "That would be युक्ताः; योज्याः names what is to be done."),
             ("A gerund: 'having applied'", "That would be योजयित्वा; योज्याः agrees with ध्वनयः."),
             ("A present verb: 'they apply'", "That would be युञ्जन्ति; योज्याः is not a finite verb.")],
            "योज्याः = gerundive, 'to be applied', agreeing with ध्वनयः.",
            "-य gerundive = to be done.",
            teaches="A gerundive (-य, -तव्य, -अनीय) says what is to be done and agrees with its noun: ध्वनयो योज्याः."),
        mcq("discriminate", 3, "Which split of अन्येपि in card 17 is right?",
            ("अन्ये + अपि", "After ए the अ of अपि is elided: अन्ये + अपि → अन्येऽपि (ऽ not printed here)."),
            [("अन्य + इपि", "इपि is not a word; the word is अपि."),
             ("अन्ये + पि", "पि is not a word; the अ of अपि is elided."),
             ("अन्यः + अपि", "अः + अ would give अन्योऽपि, with ओ.")],
            "अन्ये (other) + अपि (also).",
            "ए + अ → एऽ."),
        mcq("apply", 4, "Why does ध्वनयः become ध्वनयो before योज्याः in card 17?",
            ("अः before a voiced consonant → ओ", "य is a voiced consonant: ध्वनयः + योज्याः → ध्वनयो योज्याः."),
            [("अः before any consonant → ओ", "Not before त: there ः → स् (स्वप्नस्तु, card 20)."),
             ("ओ belongs to the stem form ध्वनयो", "The stem is ध्वनि; the nominative plural is ध्वनयः."),
             ("ः after अ before य → र्", "र् comes after vowels other than अ/आ.")],
            "ध्वनयः + योज्याः → ध्वनयो योज्याः.",
            "अः + voiced consonant → ओ."),
        mcq("transfer", 5, "By the pattern of अन्ये + अपि, how is गृहे + अपि (in the house too) joined in a new example?",
            ("गृहेऽपि", "ए + अ: the अ is elided, marked ऽ: गृहेऽपि."),
            [("गृहापि", "The ए does not vanish; the अ is the vowel that is elided."),
             ("गृहोऽपि", "ओऽ comes from अः + अ; here the word ends in ए."),
             ("गृहैपि", "ऐ comes from अ + ए; here ए comes before अ.")],
            "गृहे + अपि = गृहेऽपि, like अन्ये + अपि = अन्येऽपि.",
            "Word-final ए + अ → एऽ.",
            teaches="After a word-final ए an initial अ is elided (written ऽ): अन्ये + अपि → अन्येऽपि."),
    ],
}

# ---------------------------------------------------------------- unit 18
AUTHORED["18"] = {
    "title": "वादित्रस्वराश्च श्रेष्ठाः",
    "question": "By card 18, which words and sounds are best everywhere?",
    "rule": ("Everywhere (सर्वत्र एव) the words sthira (firm), sthāvara (stationary), vardhamāna (increasing), trāta, acala "
             "(immovable), dhruva (fixed), kṣema (safety), śiva (auspicious) and the like, and the sounds of musical "
             "instruments (वादित्रस्वराः), are best (श्रेष्ठाः)."),
    "limits": ("Prose, medium confidence. त्रात may be 'protected' or 'protector': no question on it. Printed अन्या is read "
               "अन्ये (agreement); printed स्थावरं has a stray anusvāra. No question on either form."),
    "explain_hi": ("सब जगह स्थिर, स्थावर, वर्धमान, त्रात (रक्षित या रक्षक: रूप अनिश्चित), अचल, ध्रुव, क्षेम, शिव आदि शब्द श्रेष्ठ हैं। "
                   "इनके साथ अन्य वाद्यों के स्वर (वादित्रस्वराः) भी श्रेष्ठ हैं। "
                   "छपा ‘अन्या’ स्त्रीलिंग है और पुंलिंग ‘वादित्रस्वराः’ से मेल नहीं खाता, इसलिए ‘अन्ये’ पढ़ा गया। "
                   "‘सर्वत्रैव’ में सर्वत्र + एव की सन्धि है (अ + ए → ऐ)।"),
    "hook": "स्थिर, अचल, ध्रुव, क्षेम, शिव और बाजों के स्वर: सर्वत्र श्रेष्ठ।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "In card 18, what does श्रेष्ठाः mean?",
            ("Best", "श्रेष्ठाः = best, excellent (masculine plural)."),
            [("Forbidden", "Forbidden is प्रतिषिद्धाः (card 19)."),
             ("Undesired", "Undesired is अनिष्टम् (card 15)."),
             ("Fruitless", "Fruitless is अफलः (card 21).")],
            "श्रेष्ठाः = best.",
            "श्रेष्ठ = best."),
        match(1, "Match each word of card 18 to its meaning.",
              [["स्थिर", "firm"], ["वर्धमान", "increasing"], ["अचल", "immovable"], ["क्षेम", "safety"],
               ["शिव", "auspicious"]],
              "स्थिर = firm, वर्धमान = increasing, अचल = immovable, क्षेम = safety, शिव = auspicious.",
              "स्थिर, वर्धमान, अचल, क्षेम, शिव."),
        order(2, "Put these sure words of card 18 in the printed order.",
              ["स्थिर", "स्थावर", "वर्धमान", "अचल", "ध्रुव", "क्षेम"],
              "Firm, stationary, increasing, (त्रात,) immovable, fixed, safety: six of the list, in order.",
              "स्थिर → स्थावर → वर्धमान → अचल → ध्रुव → क्षेम.",
              role="extend",
              teaches="The good words stand in one dvandva ending in -आदयः (and the like), followed by शब्दाः (words)."),
        mcq("discriminate", 3, "Which split of सर्वत्रैव in card 18 is right?",
            ("सर्वत्र + एव", "अ + ए → ऐ: सर्वत्र + एव → सर्वत्रैव."),
            [("सर्वत्र + इव", "अ + इ gives ए: that would print सर्वत्रेव."),
             ("सर्वत्रे + एव", "सर्वत्रे is not a word; the adverb is सर्वत्र."),
             ("सर्वत्रै + व", "सर्वत्रै is not a word; the ऐ comes from अ + ए.")],
            "सर्वत्र (everywhere) + एव (indeed).",
            "अ + ए → ऐ."),
        mcq("apply", 4, "Besides the good words, what else does card 18 call best?",
            ("Instrument sounds", "वादित्रस्वराः: the sounds of musical instruments are best."),
            [("The sound of sneezing", "Sneeze (क्षुत) is a forbidden word in card 19."),
             ("Cries of 'hā hā'", "'Hā hā' (हाहा) is a forbidden word in card 19."),
             ("Cruel cries of birds", "Cruel cries of birds and beasts are among the bad signs of card 19.")],
            "शब्दाः ... वादित्रस्वराश्च श्रेष्ठाः.",
            "वादित्रस्वराः = sounds of musical instruments."),
        mcq("transfer", 5, "By the pattern of सर्वत्र + एव → सर्वत्रैव, how is मम + एव (mine alone) joined in a new example?",
            ("ममैव", "अ + ए → ऐ: मम + एव → ममैव."),
            [("ममेव", "ए comes from अ + इ (मम + इव), not from अ + ए."),
             ("ममौव", "औ comes from अ + ओ or अ + औ, not from अ + ए."),
             ("ममयेव", "No य् is inserted between अ and ए; they merge into ऐ.")],
            "मम + एव = ममैव, like सर्वत्र + एव = सर्वत्रैव.",
            "अ + ए → ऐ.",
            teaches="अ before ए gives ऐ: सर्वत्र + एव → सर्वत्रैव."),
    ],
}

# ---------------------------------------------------------------- unit 19
AUTHORED["19"] = {
    "title": "शब्दाः प्रतिषिद्धाः",
    "question": "By card 19, which words, sounds and sights count against taking up the treatment?",
    "rule": ("The words sneeze, struck, fallen, outcry, blow, cutting, breaking, burning, 'hā hā', prohibition and the like are "
             "forbidden (प्रतिषिद्धाः); with cruel cries in a forbidden or blazing direction, the sights at the entering and "
             "other signs, all is 'for the prohibition of treatment' (चिकित्साप्रतिषेधाय)."),
    "limits": ("Prose, low confidence: one very long sentence of lists with one predicate. Conjectural: patient's house "
               "(चातुर्गृहात्), planets (यहा → ग्रहाः), Saturn (शिनि), the stray र् of लाभर्तुष्टि; पलल is disputed; "
               "ऊर्ध्वपाद and the attachment of शुभाशुभा are open. No question on any of these."),
    "explain_hi": ("छींक, ‘मारा गया’, ‘गिरा’, चीख, प्रहार, छेद, भेद, दाह, ‘हा हा’ और निषेध आदि शब्द निषिद्ध हैं। "
                   "निषिद्ध और जलती (दीप्त) दिशा में पक्षी-पशुओं की क्रूर ध्वनियाँ, सूखे, काँटों और लताओं वाले वृक्ष पर, और प्रवेश के समय "
                   "तृण, लकड़ी का बोझ, ठीकरा, ढेला, टूटे वाहन-शय्या-आसन, खाली घड़ा, मद्य, वसा, तेल, गर्भिणी, विपत्ति में पड़ा व्यक्ति और मृत आदि का दर्शन गिनाए गए हैं। "
                   "भीतर आए वैद्य का सत्कार न होना भी इसी सूची में है। "
                   "यह सब ‘चिकित्साप्रतिषेधाय’ है, यानी चिकित्सा के निषेध के लिए (रोगी को न लेने के लिए)। "
                   "रोगी का घर, ग्रह, शनि आदि वाले भाग अनुमानित पाठ हैं और ‘पलल’ विवादित है, इसलिए उन पर प्रश्न नहीं।"),
    "hook": "छींक, ‘हा हा’, खाली घड़ा, सूखा काँटेदार पेड़: चिकित्साप्रतिषेधाय।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "In card 19, what does क्षुत mean?",
            ("Sneeze", "क्षुत = sneeze, the first of the forbidden words."),
            [("Cough", "Cough would be कास; क्षुत = sneeze."),
             ("Yawn", "Yawn would be जृम्भा; क्षुत = sneeze."),
             ("Hiccup", "Hiccup would be हिक्का; क्षुत = sneeze.")],
            "क्षुत = sneeze.",
            "क्षुत = sneeze."),
        order(1, "Put these forbidden words of card 19 in the printed order.",
              ["क्षुत", "हत", "पतित", "आक्रोश", "प्रहार", "छेद"],
              "Sneeze, struck, fallen, outcry, blow, cutting: the start of the forbidden list.",
              "क्षुत → हत → पतित → आक्रोश → प्रहार → छेद."),
        match(2, "Match each sight that card 19 lists at the entering to its meaning.",
              [["रिक्तकुंभ", "empty pot"], ["मृत", "the dead"], ["लोष्ट", "clod"], ["तैल", "oil"],
               ["कर्परक", "potsherd"]],
              "रिक्तकुंभ = empty pot, मृत = the dead, लोष्ट = clod, तैल = oil, कर्परक = potsherd.",
              "रिक्तकुंभ, मृत, लोष्ट, तैल, कर्परक.",
              role="extend",
              teaches=("The things seen at the entering stand in two long genitive compounds (-आदीनाम्, -मृतानाम्) "
                        "that the data reads as depending on दर्शनम् (sight).")),
        mcq("discriminate", 3, "By card 19, what is this whole list of signs for?",
            ("For the prohibition of treatment", "चिकित्साप्रतिषेधाय: for prohibiting treatment, refusing the case."),
            [("For choosing the right medicine", "No medicine is named; the line ends चिकित्साप्रतिषेधाय."),
             ("For fixing the time of treatment", "No time of treatment is set; the list prohibits treatment."),
             ("For the patient's diet", "No diet is named; the list prohibits treatment.")],
            "The list ends चिकित्साप्रतिषेधाय: for the prohibition of treatment.",
            "चिकित्सा-प्रतिषेधाय = for prohibiting treatment."),
        multi("apply", 4, "At the entering, which of these sights does card 19 list?",
              [("A full pitcher", "No: the full pitcher (पूर्णकुंभ) is among the auspicious things of card 10."),
               ("An empty pot", "Right: रिक्तकुंभ, an empty pot, is in the list."),
               ("Curd", "No: curd (दधि) is among the auspicious things of card 10."),
               ("Oil", "Right: तैल, oil, is in the list.")],
              [1, 3],
              "Empty pot and oil are in the list of sights; full pitcher and curd are auspicious in card 10.",
              "रिक्तकुंभ, तैल ... दर्शनम्, at the entering."),
        mcq("transfer", 5, "By the pattern of तत् + विधे → तद्विधे, how is एतत् + वनम् (this forest) joined in a new example?",
            ("एतद्वनम्", "त् before a voiced consonant → द्: एतत् + वनम् → एतद्वनम्."),
            [("एतत्वनम्", "Before the voiced व, a final त् becomes voiced द्."),
             ("एतन्वनम्", "न् replaces त् only (optionally) before a nasal; व is not a nasal."),
             ("एतच्वनम्", "च् comes from त् before च or छ, not before व.")],
            "एतत् + वनम् = एतद्वनम्, like तत् + विधे = तद्विधे.",
            "Final त् + voiced consonant → द्.",
            teaches="A final त् becomes द् before a voiced consonant: तत् + विधे → तद्विधे (of that kind)."),
    ],
}

# ---------------------------------------------------------------- unit 20
AUTHORED["20"] = {
    "title": "स सप्तविधो दृष्टः",
    "question": "By card 20, what is a dream a cause of, and what are its seven kinds?",
    "rule": ("A dream (स्वप्नः), seen by oneself or by another, is a cause of the auspicious and the inauspicious. It is of "
             "seven kinds: seen, heard, experienced, desired, imagined, bhāvika (of what will be) and born of the doṣas."),
    "limits": ("Prose, high confidence. भाविक is rendered literally (of what is to come); the line explains no kind. Printed "
               "स्वयमम्येन is read स्वयम् अन्येन. Which kinds bear fruit is in card 21, not here."),
    "explain_hi": ("स्वप्न, चाहे स्वयं देखा गया हो या दूसरे द्वारा, शुभ और अशुभ का कारण है। "
                   "वह सात प्रकार का है: दृष्ट (देखा), श्रुत (सुना), अनुभूत (अनुभव किया), प्रार्थित (चाहा), संकल्पित (कल्पित), भाविक (आगे होने वाले से सम्बन्धित) और दोषज (दोषों से उत्पन्न)। "
                   "पंक्ति किसी प्रकार की व्याख्या नहीं करती; कौन से प्रकार निष्फल हैं, यह कार्ड २१ में है। "
                   "‘श्रुतोऽनुभूतः’ में श्रुतः + अनुभूतः की सन्धि है (अः + अ → ओऽ)।"),
    "hook": "सात स्वप्न: देखा, सुना, अनुभूत, चाहा, कल्पित, भाविक, दोषज।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By card 20, a dream seen by whom is a cause of good and bad?",
            ("By oneself or by another", "स्वयम् अन्येन वा दृष्टः: seen by oneself or by another."),
            [("Only by the patient himself", "The line adds अन्येन वा, or by another."),
             ("Only by the physician", "The physician is not named; seen by oneself or by another."),
             ("Only by a messenger", "No messenger is named here; seen by oneself or by another.")],
            "स्वयम् अन्येन वा दृष्टः = seen by oneself or by another.",
            "स्वयम् / अन्येन = by oneself / by another."),
        order(1, "After दृष्टः (seen), put the other kinds of dream of card 20 in the printed order.",
              ["श्रुतः", "अनुभूतः", "प्रार्थितः", "संकल्पितः", "भाविकः", "दोषजः"],
              "Heard, experienced, desired, imagined, of what will be, born of the doṣas.",
              "दृष्टः → श्रुतः → अनुभूतः → प्रार्थितः → संकल्पितः → भाविकः → दोषजः."),
        match(2, "Match each kind of dream of card 20 to its meaning.",
              [["दृष्टः", "seen"], ["श्रुतः", "heard"], ["अनुभूतः", "experienced"], ["प्रार्थितः", "desired"],
               ["दोषजः", "born of the doṣas"]],
              "दृष्टः = seen, श्रुतः = heard, अनुभूतः = experienced, प्रार्थितः = desired, दोषजः = born of the doṣas.",
              "दृष्ट, श्रुत, अनुभूत, प्रार्थित, दोषज.",
              role="extend",
              teaches="Five kinds are named by past participles (दृष्ट, श्रुत, अनुभूत, प्रार्थित, संकल्पित); भाविक and दोषज are adjectives."),
        mcq("discriminate", 3, "Which split of श्रुतोऽनुभूतः in card 20 is right?",
            ("श्रुतः + अनुभूतः", "अः + अ → ओ, and the अ is elided (ऽ): श्रुतोऽनुभूतः."),
            [("श्रुत + अनुभूतः", "अ + अ would merge into आ: श्रुतानुभूतः."),
             ("श्रुतो + नुभूतः", "नुभूतः is not a word; the अ of अनुभूतः is elided."),
             ("श्रुतः + नुभूतः", "नुभूतः is not a word; the word is अनुभूतः.")],
            "श्रुतः (heard) + अनुभूतः (experienced).",
            "अः + अ → ओऽ."),
        mcq("apply", 4, "In दोषजः (card 20), what does -जः add to दोष?",
            ("Born of", "-ज = born of, arising from: दोषजः, born of the doṣas."),
            [("Free of", "Free of would be निर्- or -रहित, not -ज."),
             ("Destroying", "Destroying would be -घ्न or -नाशन, not -ज."),
             ("Like", "Like would be -वत् or इव, not -ज.")],
            "दोष + ज (from √जन्) = born of the doṣas.",
            "-ज = born of."),
        mcq("transfer", 5, "By the pattern of दोषजः, what does क्रोधजः (from क्रोध, anger) mean in a new example?",
            ("Born of anger", "-ज = born of: क्रोधजः, born of anger."),
            [("Free of anger", "Free of would need निर्- or -रहित; -ज means born of."),
             ("Destroying anger", "Destroying would need -घ्न; -ज means born of."),
             ("Like anger", "Like would need -वत्; -ज means born of.")],
            "क्रोधजः = born of anger, like दोषजः = born of the doṣas.",
            "-ज = born of.",
            teaches="-ज (from √जन्, be born) at the end of a compound means 'born of': दोषजः, born of the doṣas."),
    ],
}

# ---------------------------------------------------------------- unit 21
AUTHORED["21"] = {
    "title": "तत्राद्यः पंचविधोऽफलः",
    "question": "By card 21, which dreams are fruitless, and what fruit does a dream in the first part of the night give?",
    "rule": ("Of the seven kinds (card 20), the first five are fruitless (अफलः). Then (तथा) six more are listed. A dream in the "
             "first part of the night gives little fruit (अल्पं फलम्), and after a long time (चिरात्)."),
    "limits": ("Prose, medium confidence. The list after तथा (own prakṛti, forgotten, by day, too short, too long, not seen in "
               "deep sleep) has no printed predicate; the data reads it as parallel to अफलः, but the text does not say so: no "
               "question on whether these are fruitless. नातिसुप्तदृष्टः can be parsed two ways: no question on its parse."),
    "explain_hi": ("कार्ड २० के सात प्रकारों में पहले पाँच (दृष्ट, श्रुत, अनुभूत, प्रार्थित, संकल्पित) निष्फल हैं। "
                   "फिर ‘तथा’ के बाद छह और गिनाए गए: अपनी प्रकृति के अनुसार, भूला हुआ, दिन में देखा, बहुत छोटा, बहुत लम्बा और गहरी नींद में न देखा। "
                   "इनका विधेय छपा नहीं; डेटा इन्हें ‘अफल’ के समान पढ़ता है, पर पाठ यह नहीं कहता। "
                   "रात्रि के पहले भाग का स्वप्न थोड़ा फल देता है, और देर से। "
                   "‘चिराच्च’ में चिरात् + च की सन्धि है (त् + च → च्च)।"),
    "hook": "पहले पाँच अफल; रात के पहले पहर का स्वप्न: थोड़ा और देर से।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By card 21, what is said of the first five kinds of dream?",
            ("They are fruitless", "तत्राद्यः पंचविधोऽफलः: the first five are fruitless."),
            [("They bear fruit at once", "Nothing in card 21 gives the first five any fruit."),
             ("They are born of the doṣas", "Born of the doṣas (दोषज) is the seventh kind, not the first five."),
             ("They bear great fruit", "The first five are अफलः, without fruit.")],
            "आद्यः पञ्चविधः अफलः = the first five kinds are fruitless.",
            "अफल = fruitless."),
        match(1, "Match each word of card 21 to its meaning.",
              [["अफलः", "fruitless"], ["विस्मृतः", "forgotten"], ["दिवा", "by day"], ["अतिह्रस्वः", "too short"],
               ["अतिदीर्घः", "too long"]],
              "अफलः = fruitless, विस्मृतः = forgotten, दिवा = by day, अतिह्रस्वः = too short, अतिदीर्घः = too long.",
              "अफलः, विस्मृतः, दिवा, अतिह्रस्वः, अतिदीर्घः."),
        order(2, "Put the items listed after तथा in card 21 in the printed order.",
              ["यथास्वप्रकृतिः", "विस्मृतः", "दिवा", "अतिह्रस्वः", "अतिदीर्घः", "नातिसुप्तदृष्टः"],
              "Own prakṛti, forgotten, by day, too short, too long, not seen in deep sleep.",
              "यथास्वप्रकृतिः → विस्मृतः → दिवा → अतिह्रस्वः → अतिदीर्घः → नातिसुप्तदृष्टः.",
              role="extend",
              teaches=("After तथा (likewise) six more items follow with no printed predicate; the data reads them as "
                       "parallel to अफलः, but the text does not say so.")),
        mcq("discriminate", 3, "By card 21, what fruit does a dream in the first part of the night give?",
            ("Little fruit, after a long time", "पूर्वरात्रेऽल्पं चिराच्च फलं करोति: little, and late."),
            [("Great fruit, and at once", "That is not card 21's first part of the night; it says अल्पं and चिरात्."),
             ("No fruit at all", "It gives fruit, but little: अल्पं फलं करोति."),
             ("Great fruit, but after a long time", "अल्पम् = little, not great.")],
            "पूर्वरात्रे: अल्पम् (little) and चिरात् (after a long time).",
            "पूर्वरात्रे → अल्पं चिराच्च फलम्."),
        mcq("apply", 4, "Which split of चिराच्च in card 21 is right?",
            ("चिरात् + च", "त् before च → च्: चिरात् + च → चिराच्च."),
            [("चिरा + च्च", "च्च is not a word; the first च् comes from त्."),
             ("चिरम् + च", "म् before च would print चिरं च."),
             ("चिरः + च", "ः before च would print चिरश्च.")],
            "चिरात् (after a long time) + च (and).",
            "त् + च → च्च."),
        mcq("transfer", 5, "By the pattern of चिरात् + च → चिराच्च, how is जगत् + च (and the world) joined in a new example?",
            ("जगच्च", "त् before च → च्: जगत् + च → जगच्च."),
            [("जगत्च", "Before च a final त् becomes च्."),
             ("जगद्च", "द् comes before a voiced sound; च is not voiced."),
             ("जगश्च", "श्च comes from a visarga before च, not from त्.")],
            "जगत् + च = जगच्च, like चिरात् + च = चिराच्च.",
            "त् + च → च्च.",
            teaches="A final त् becomes च् before च or छ: चिरात् + च → चिराच्च."),
    ],
}

# ---------------------------------------------------------------- unit 22
AUTHORED["22"] = {
    "title": "गोसर्गे महत्सद्यश्च",
    "question": "What does card 22 say of a dream at gosarga (daybreak)?",
    "rule": "At gosarga (daybreak, the time cows are let out): great (महत्) and at once (सद्यः).",
    "limits": ("Prose, elliptical. The noun that is 'great' is not printed; presumably the fruit (फलम्) of card 21, but none is "
               "supplied: questions keep to the printed words. The space in महत्सद्यश्च is missing."),
    "explain_hi": ("गोसर्ग, यानी प्रातःकाल जब गायें छोड़ी जाती हैं: महान और तुरन्त। "
                   "क्या महान है, यह छपा नहीं; सम्भवतः कार्ड २१ का ‘फल’, पर वह जोड़ा नहीं गया। "
                   "‘महत्सद्यश्च’ में शब्दों के बीच रिक्त स्थान छूटा है (महत् सद्यः च)। "
                   "‘सद्यश्च’ में सद्यः + च की सन्धि है: च से पहले विसर्ग → श्।"),
    "hook": "भोर का स्वप्न: महत्, सद्यः।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "In card 22, what does सद्यः mean?",
            ("At once", "सद्यः = at once, immediately."),
            [("After long", "After a long time is चिरात् (card 21)."),
             ("Slowly", "Slowly would be शनैः; सद्यः = at once."),
             ("Never", "Never would be न कदापि; सद्यः = at once.")],
            "सद्यः = at once.",
            "सद्यः = at once."),
        match(1, "Match each word of card 22 to its meaning.",
              [["गोसर्गे", "at daybreak"], ["महत्", "great"], ["सद्यः", "at once"], ["च", "and"]],
              "गोसर्गे = at daybreak, महत् = great, सद्यः = at once, च = and.",
              "गोसर्गे, महत्, सद्यः, च."),
        fill(2, "The word for 'great' in card 22 is ____ (type it in Devanagari or in English letters, e.g. dharma).",
             accepts("महत्", "mahat"),
             "महत् = great: गोसर्गे महत्सद्यश्च.",
             "महत् means great; here it stands alone, with its noun not printed.",
             "महत् = great."),
        mcq("discriminate", 3, "By card 22, what does गोसर्ग literally name?",
            ("When cows are let out", "गो (cow) + सर्ग (letting out): daybreak, when the cows are let out."),
            [("The time cows come home", "सर्ग is letting out, not coming home."),
             ("A herd of grazing cows", "गोसर्ग names a time of day, not a herd."),
             ("The place cows are kept", "गोसर्ग names a time of day, not a place.")],
            "गोसर्ग = the letting out of cows: daybreak.",
            "गोसर्ग = daybreak."),
        mcq("apply", 4, "Why does सद्यः become सद्यश् before च in card 22?",
            ("ः before च becomes श्", "A visarga before च or छ becomes श्: सद्यः + च → सद्यश्च."),
            [("ः before any consonant becomes श्", "Not before त: there it becomes स् (स्वप्नस्तु, card 20)."),
             ("श् belongs to the stem सद्यश्", "The word is सद्यः; श् comes only from sandhi."),
             ("ः before च drops entirely", "It does not drop; before च it becomes श्.")],
            "सद्यः + च → सद्यश्च.",
            "ः + च → श्च."),
        mcq("transfer", 5, "By the pattern of सद्यः + च → सद्यश्च, how is रविः + च (and the sun) joined in a new example?",
            ("रविश्च", "ः before च → श्: रविः + च → रविश्च."),
            [("रविस्च", "स् comes from a visarga before त or थ, not before च."),
             ("रविर्च", "र् comes before a voiced sound; च is not voiced."),
             ("रवि च", "The visarga does not drop before च; it becomes श्.")],
            "रविः + च = रविश्च, like सद्यः + च = सद्यश्च.",
            "ः + च → श्च.",
            teaches="A visarga before च or छ becomes श्: सद्यः + च → सद्यश्च."),
    ],
}

# ---------------------------------------------------------------- unit 23
AUTHORED["23"] = {
    "title": "निद्रया चपुनरनुपहतः",
    "question": "By card 23, by what may a dream be struck down (cancelled)?",
    "rule": ("Not struck down (अनुपहतः) again by sleep (निद्रया पुनः), or by contrary words (प्रतीपैः वचोभिः), or by giving, "
             "appeasing acts (दान, शमनीय) and the like."),
    "limits": ("Prose, medium confidence. The line continues card 22 and states no subject; the dream is understood. Printed "
               "शमनीयमादिभिः has a stray म्. The line says only 'not cancelled by ...'; no question on what such a dream then does."),
    "explain_hi": ("यह कार्ड २२ से आगे चलता है; कर्ता छपा नहीं, स्वप्न समझा जाता है। "
                   "स्वप्न जो फिर नींद से, या विपरीत वचनों से, या दान, शमनीय (शान्ति के कर्म) आदि से नष्ट न किया गया हो (अनुपहतः)। "
                   "छपे ‘शमनीयमादिभिः’ में म् अतिरिक्त है; ‘दान-शमनीय-आदिभिः’ पढ़ा गया। "
                   "‘प्रतीपैर्वा’ और ‘वचोभिर्दान’ में ऐ/इ के बाद विसर्ग घोष वर्ण से पहले र् बना है।"),
    "hook": "फिर सोकर, उलटे वचन से या दान-शान्ति से न कटे: अनुपहतः।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "In card 23, what does अनुपहतः mean?",
            ("Not cancelled", "अन्- (not) + उपहत (struck down): not cancelled."),
            [("Struck down hard", "That is उपहत without अन्-; अनुपहतः is the negative."),
             ("Seen once again", "पुनः means again, but अनुपहतः is not 'seen'."),
             ("Forgotten", "Forgotten is विस्मृतः (card 21).")],
            "अनुपहतः = not struck down, not cancelled.",
            "अन् + उपहत = not cancelled."),
        match(1, "Match each word of card 23 to its meaning.",
              [["निद्रया", "by sleep"], ["पुनः", "again"], ["प्रतीपैः", "contrary"], ["वचोभिः", "by words"],
               ["दान", "giving"]],
              "निद्रया = by sleep, पुनः = again, प्रतीपैः = contrary, वचोभिः = by words, दान = giving.",
              "निद्रया, पुनः, प्रतीपैः, वचोभिः, दान."),
        order(2, "Put these printed parts of card 23 in the printed order.",
              ["निद्रया", "चपुनरनुपहतः", "प्रतीपैर्वा", "वचोभिर्दानशमनीयमादिभिर्वा"],
              "By sleep; and again not struck down; by contrary; words, giving, appeasing and the like.",
              "निद्रया → चपुनरनुपहतः → प्रतीपैर्वा → वचोभिर्दानशमनीयमादिभिर्वा.",
              role="extend",
              teaches="Card 23 continues card 22 with no subject printed; each 'or' (वा) adds one more thing that can cancel."),
        multi("discriminate", 3, "Which of these does card 23 name among the things that may cancel a dream?",
              [("Sleep, again", "Right: निद्रया पुनः, by sleep again."),
               ("Contrary words", "Right: प्रतीपैर्वा वचोभिः, by contrary words."),
               ("A fast", "No: card 23 names no fast."),
               ("Giving", "Right: दान, giving, opens the last compound."),
               ("Bathing", "No: card 23 names no bathing.")],
              [0, 1, 3],
              "Card 23 names sleep again, contrary words, giving and appeasing acts.",
              "निद्रा, प्रतीप वचन, दान, शमनीय."),
        mcq("apply", 4, "Why does प्रतीपैः become प्रतीपैर् before वा in card 23?",
            ("After ऐ, ः before a voiced sound → र्", "ः follows ऐ (not अ/आ) and व is voiced: प्रतीपैर्वा."),
            [("After any vowel, ः before व → र्", "Not after अ: there it gives ओ (ध्वनयो योज्याः, card 17)."),
             ("र् belongs to the stem प्रतीपैर्", "The form is प्रतीपैः; र् comes only from sandhi."),
             ("ः before any consonant → र्", "Not before त or च: there ः → स् or श्.")],
            "प्रतीपैः + वा → प्रतीपैर्वा.",
            "Visarga after a vowel other than अ/आ, before a voiced sound → र्."),
        mcq("transfer", 5, "By the pattern of प्रतीपैर्वा, how is देवैः + दत्तम् (given by the gods) joined in a new example?",
            ("देवैर्दत्तम्", "ः after ऐ before the voiced द → र्: देवैर्दत्तम्."),
            [("देवैस्दत्तम्", "स् comes from a visarga before त or थ, not before द."),
             ("देवैदत्तम्", "After ऐ the visarga does not drop before a voiced sound; it gives र्."),
             ("देवैश्दत्तम्", "श् comes from a visarga before च or छ, not before द.")],
            "देवैः + दत्तम् = देवैर्दत्तम्, like प्रतीपैः + वा = प्रतीपैर्वा.",
            "ऐः + voiced sound → ऐर्.",
            teaches="A visarga after a vowel other than अ/आ becomes र् before a voiced sound: प्रतीपैः + वा → प्रतीपैर्वा."),
    ],
}

# ---------------------------------------------------------------- unit 24
AUTHORED["24"] = {
    "title": "प्रेतैः सह मद्यं पिबन्",
    "question": "By card 24, which dream goes with being struck down by fever?",
    "rule": ("Among these (dreams), he who, drinking madya (an intoxicating drink) with the departed (pretas), is dragged by a "
             "dog, is struck down (हन्यते) by fever (ज्वरेण)."),
    "limits": ("Prose, high confidence. हन्यते can also mean 'is killed'; the card keeps 'is struck down', as the data does: "
               "no question on that sense. The card states the dream and the disease only."),
    "explain_hi": ("अशुभ स्वप्नों में: जो प्रेतों के साथ मद्य (नशीला पेय) पीता हुआ कुत्ते द्वारा खींचा जाता है, वह ज्वर से आहत होता है। "
                   "‘हन्यते’ का अर्थ ‘मारा जाता है’ भी हो सकता है; डेटा का शब्दशः अर्थ ‘आहत होता है’ रखा गया। "
                   "‘पिबन्’ √पा का वर्तमान कृदन्त है: ‘पीता हुआ’। "
                   "‘यः ... सः’ की जोड़ी: जो ऐसा देखता है, वह ज्वर से।"),
    "hook": "प्रेतों संग मद्य, कुत्ता खींचे: ज्वर।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By card 24, by which disease is this dreamer struck down?",
            ("ज्वर", "हन्यते ज्वरेण: struck down by jvara, fever (standard)."),
            [("रक्तपित्त", "Raktapitta goes with the red dreams of card 25."),
             ("यक्ष्मन्", "Yakṣman goes with the southern direction in card 26."),
             ("गुल्म", "Gulma goes with the growth in the heart in card 26.")],
            "ज्वरेण = by fever.",
            "प्रेत, मद्य, श्वा → ज्वर."),
        match(1, "Match each word of card 24 to its meaning.",
              [["प्रेतैः", "with the departed"], ["मद्यम्", "an intoxicating drink"], ["पिबन्", "drinking"],
               ["शुना", "by a dog"], ["ज्वरेण", "by fever"]],
              "प्रेतैः = with the departed, मद्यम् = an intoxicating drink, पिबन् = drinking, शुना = by a dog, ज्वरेण = by fever.",
              "प्रेतैः, मद्यम्, पिबन्, शुना, ज्वरेण."),
        order(2, "Put the parts of card 24 in the printed order.",
              ["यः", "प्रेतैः सह", "मद्यं पिबन्", "शुना ऽऽकृष्यते", "स हन्यते", "ज्वरेण"],
              "Who; with the departed; drinking madya; is dragged by a dog; he is struck down; by fever.",
              "यः → प्रेतैः सह → मद्यं पिबन् → शुना ऽऽकृष्यते → स हन्यते → ज्वरेण.",
              role="extend",
              teaches="यः (who) ... सः (he): the dream comes in the relative clause, the disease in the main clause."),
        mcq("discriminate", 3, "By card 24, who drags the dreamer?",
            ("A dog", "शुना ऽऽकृष्यते: he is dragged by a dog."),
            [("The departed", "The departed drink with him; they do not drag him."),
             ("A woman", "Being carried off by a woman is in card 25."),
             ("A donkey", "The donkey is named in card 26, not here.")],
            "शुना (by a dog) आकृष्यते (is dragged).",
            "शुना = by a dog."),
        mcq("apply", 4, "In card 24, what does पिबन् mean?",
            ("While drinking", "पिबन् = present participle of √पा: drinking, while drinking."),
            [("Having drunk", "Having drunk would be पीत्वा."),
             ("About to drink", "About to drink would be पास्यन्."),
             ("Was drunk", "Was drunk would be पीतः.")],
            "पिबन् = drinking (present participle, masculine nominative singular).",
            "-अन् (-अत्) = present participle: while doing."),
        mcq("transfer", 5, "By the pattern of पिबन् (drinking), what does पठन् (from √पठ्, read) mean in a new example?",
            ("While reading", "पठन् = present participle: reading, while reading."),
            [("Having read", "Having read would be पठित्वा."),
             ("About to read", "About to read would be पठिष्यन्."),
             ("Was read", "Was read would be पठितः.")],
            "पठन् = while reading, like पिबन् = while drinking.",
            "Present participle in -अन् = while doing.",
            teaches="The present participle (masculine nominative -अन्) means 'while doing': पिबन्, drinking."),
    ],
}

# ---------------------------------------------------------------- unit 25
AUTHORED["25"] = {
    "title": "लाक्षारक्ताभमंबरं पश्यति",
    "question": "By card 25, which dreams go with raktapitta?",
    "rule": ("He who sees an ambara (garment or sky) of the hue of red lac, or who, with red body, garland and cloth, laughing, "
             "is carried off by a woman: he by raktapitta (a bleeding disorder)."),
    "limits": ("Prose, medium confidence. The verb 'is struck down' of card 24 is understood, not printed. अम्बर can be garment "
               "or sky. हसन्नार्या could also be read हसन् + आर्या; 'by a woman' is the data's reading: no question on it."),
    "explain_hi": ("जो लाख के लाल रंग जैसा अम्बर (वस्त्र या आकाश; दोनों सम्भव) देखता है, "
                   "अथवा जो लाल देह, माला और वस्त्र वाला, हँसता हुआ, स्त्री द्वारा ले जाया जाता है: वह रक्तपित्त (रक्तस्राव का रोग) से। "
                   "कार्ड २४ की क्रिया ‘हन्यते’ यहाँ समझी जाती है, छपी नहीं। "
                   "‘हसन्नार्या’ को ‘हसन् + आर्या’ भी पढ़ा जा सकता है; ‘हसन् नार्या’ (स्त्री द्वारा) डेटा का पाठ है। "
                   "‘ह्रियते’ √हृ का कर्मवाच्य है: ले जाया जाता है।"),
    "hook": "लाल लाख-सा अम्बर, लाल देह-माला-वस्त्र: रक्तपित्त।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By card 25, which instrumental word follows स for these dreamers?",
            ("रक्तपित्तेन", "स रक्तपित्तेन: he by raktapitta, a bleeding disorder (standard)."),
            [("ज्वरेण", "ज्वरेण (by fever) closes card 24."),
             ("यक्ष्मणा", "यक्ष्मणा goes with the southern direction, card 26."),
             ("शिरश्छेदनेन", "Cutting off the head is in card 27, not card 25.")],
            "स रक्तपित्तेन = he by raktapitta.",
            "Red dreams → रक्तपित्त."),
        match(1, "Match each word of card 25 to its meaning.",
              [["लाक्षा", "lac"], ["रक्त", "red"], ["पश्यति", "sees"], ["माल्य", "garland"], ["ह्रियते", "is carried off"]],
              "लाक्षा = lac, रक्त = red, पश्यति = sees, माल्य = garland, ह्रियते = is carried off.",
              "लाक्षा, रक्त, पश्यति, माल्य, ह्रियते."),
        T(multi("extend", 2, "By the data of card 25, what can अम्बरम् mean here?",
                [("A lamp", "No: अम्बर is a garment or the sky."),
                 ("A garment", "Right: अम्बर can be clothing."),
                 ("The sky", "Right: अम्बर can be the sky; the data keeps both."),
                 ("A river", "No: अम्बर is a garment or the sky.")],
                [1, 2],
                "अम्बर = garment or sky; both are possible here.",
                "अम्बर = garment / sky."),
          "A word with two senses is kept open when the line does not decide: अम्बर, garment or sky."),
        mcq("discriminate", 3, "By card 25, how is the second dreamer described?",
            ("Laughing, red body, garland and cloth", "रक्तदेहमाल्यवस्त्रो हसन्: with red body, garland and cloth, laughing."),
            [("Weeping, with black garland and cloth", "The garland and cloth are red, and he is laughing."),
             ("Drinking madya with the departed", "That is the dreamer of card 24."),
             ("Naked, sprinkled with ghee by a fire", "That is the dreamer of card 28.")],
            "रक्त-देह-माल्य-वस्त्रः हसन्: red body, garland, cloth; laughing.",
            "Card 25: red and laughing, carried off by a woman."),
        mcq("apply", 4, "In card 25, what does ह्रियते mean?",
            ("Is carried off", "ह्रियते = 3 sg. passive of √हृ: is carried off."),
            [("Carries off", "That active sense would be हरति."),
             ("Will carry off", "The future would be हरिष्यति."),
             ("Having carried", "The gerund would be हृत्वा.")],
            "ह्रियते = is carried off (passive).",
            "ह्रियते = passive of √हृ."),
        mcq("transfer", 5, "By the pattern of ह्रियते (is carried off, √हृ), what does क्रियते (√कृ, do) mean in a new example?",
            ("Is done", "क्रियते = 3 sg. passive of √कृ: is done."),
            [("Does", "The active would be करोति."),
             ("Will do", "The future would be करिष्यति."),
             ("Having done", "The gerund would be कृत्वा.")],
            "क्रियते = is done, like ह्रियते = is carried off.",
            "ऋ-roots: passive in -रियते (√हृ → ह्रियते, √कृ → क्रियते).",
            teaches="Roots in ऋ form the passive with -रियते: √हृ → ह्रियते (is carried off)."),
    ],
}

# ---------------------------------------------------------------- unit 26
AUTHORED["26"] = {
    "title": "यो याम्यां दिशं",
    "question": "By card 26, which two dreams go with yakṣman and with gulma?",
    "rule": ("He who (verb not printed) the southern direction by any one of donkey, camel, buffalo and boar: he by yakṣman "
             "(wasting disease; probable). He in whose heart a thorny creeper, a bamboo or a palm grows: he by gulma "
             "(abdominal lump; probable)."),
    "limits": ("Prose, low confidence; two printed lines joined. Line 1 prints no verb (one such as 'is taken' is expected): no "
               "question on what happens with the animals or the direction. yakṣman and gulma are probable identifications. "
               "The verb of 'he by ...' is understood."),
    "explain_hi": ("पहली छपी पंक्ति: जो दक्षिण (याम्य) दिशा को गधा, ऊँट, भैंसा, सूअर में से किसी एक के द्वारा...: वह यक्ष्मन् (क्षय रोग, सम्भावित) से। "
                   "इस पंक्ति की क्रिया छपी नहीं (‘ले जाया जाता है’ जैसी अपेक्षित), इसलिए कोई क्रिया नहीं जोड़ी गई। "
                   "दूसरी पंक्ति: जिसके हृदय में काँटेदार लता, बाँस या ताड़ उगता है, वह गुल्म (पेट की गाँठ, सम्भावित) से। "
                   "‘खरोष्ट्र’ में खर + उष्ट्र की सन्धि है (अ + उ → ओ); ‘जायतेस’ में जायते और स के बीच रिक्त स्थान छूटा है।"),
    "hook": "दक्षिण दिशा, गधा-ऊँट: यक्ष्मन्; हृदय में बाँस-ताड़: गुल्म।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "In card 26, which direction is named?",
            ("Southern", "याम्यां दिशम्: the southern direction (of Yama)."),
            [("Northern", "Northern would be उत्तराम्; the line has याम्याम्."),
             ("Eastern", "Eastern would be प्राचीम्; the line has याम्याम्."),
             ("Western", "Western would be प्रतीचीम्; the line has याम्याम्.")],
            "याम्या = of Yama, southern.",
            "याम्या दिक् = the south."),
        match(1, "Match each word of card 26 to its meaning.",
              [["खर", "donkey"], ["उष्ट्र", "camel"], ["महिष", "buffalo"], ["वराह", "boar"], ["वंश", "bamboo"],
               ["ताल", "palm"]],
              "खर = donkey, उष्ट्र = camel, महिष = buffalo, वराह = boar, वंश = bamboo, ताल = palm.",
              "खर, उष्ट्र, महिष, वराह, वंश, ताल."),
        order(2, "Put the printed parts of card 26 in the printed order.",
              ["यो याम्यां दिशं", "खरोष्ट्रमहिषवराहान्यतमेन", "स यक्ष्मणा", "यस्य कंटकिनी लता", "वंशस्तालो वा हृदि",
               "जायतेस गुल्मेन"],
              "Line 1: the southern direction, the animals, yakṣman. Line 2: thorny creeper, bamboo or palm in the heart, gulma.",
              "यो याम्यां दिशं → खरोष्ट्र... → स यक्ष्मणा → यस्य कंटकिनी लता → वंशस्तालो वा हृदि → जायतेस गुल्मेन.",
              role="extend",
              teaches="Each printed line has the यः/यस्य ... सः frame: the dream first, then सः with the disease in the instrumental."),
        mcq("discriminate", 3, "By card 26, which dream goes with gulma?",
            ("A thorn creeper or palm in the heart", "यस्य कंटकिनी लता वंशस्तालो वा हृदि जायते स गुल्मेन."),
            [("The south with a donkey or a camel", "That line ends स यक्ष्मणा, with yakṣman."),
             ("Lotuses growing out on the chest", "Lotuses on the chest go with kuṣṭha, card 28."),
             ("Drinking madya with the departed", "That dream goes with fever, card 24.")],
            "Thorny creeper, bamboo or palm in the heart → gulma.",
            "हृदि लता / वंश / ताल → गुल्म."),
        mcq("apply", 4, "Which split of खरोष्ट्र in card 26 is right?",
            ("खर + उष्ट्र", "अ + उ → ओ: खर + उष्ट्र → खरोष्ट्र."),
            [("खरः + उष्ट्र", "With ः, अः + उ would print खर उष्ट्र, apart."),
             ("खरो + ष्ट्र", "ष्ट्र is not a word; the ओ comes from अ + उ."),
             ("खर + ओष्ट्र", "ओष्ट्र is not a word; the camel is उष्ट्र.")],
            "खर (donkey) + उष्ट्र (camel): अ + उ → ओ.",
            "अ + उ → ओ."),
        mcq("transfer", 5, "By the pattern of खर + उष्ट्र → खरोष्ट्र, how is ग्राम + उत्सवः (village festival) joined in a new example?",
            ("ग्रामोत्सवः", "अ + उ → ओ: ग्राम + उत्सवः → ग्रामोत्सवः."),
            [("ग्रामौत्सवः", "औ comes from अ + ओ or अ + औ, not from अ + उ."),
             ("ग्रामूत्सवः", "ऊ comes from उ + उ; here अ meets उ."),
             ("ग्रामवुत्सवः", "No व् is inserted; अ and उ merge into ओ.")],
            "ग्राम + उत्सवः = ग्रामोत्सवः, like खर + उष्ट्र = खरोष्ट्र.",
            "अ + उ → ओ.",
            teaches="अ before उ gives ओ: खर + उष्ट्र → खरोष्ट्र (donkey and camel)."),
    ],
}


# ================================================================ NOTES_HI
NOTES_HI = {
    "14": ("गद्य; विश्वास निम्न; एक छपी पंक्ति (०२.१२.१४)। पाठ-चिह्न (सम्भव): छपा ‘मूकर’ कोई शब्द नहीं, अनुमान से ‘सूकर’ (सूअर) पढ़ा गया; "
           "‘राजाहक’ अस्पष्ट छोड़ा गया (राज + जाहक छपे अक्षरों से मेल नहीं खाता)। छपे ‘विपरीतंमृक्ष’ में ऋक्ष से पहले अतिरिक्त म् है, "
           "और ‘च’ बिना रिक्त स्थान के जुड़ा है। ‘अजाऽवि’ में ऽ छपाई की आदत है (आ + अ → आ)। ‘विरुतम्’ पर ‘इष्टम्’ सहज पाठ से लागू। "
           "गोधा = गोह (मानक)। सन्धि जाँची: कीर्तनम् + इष्टम् → कीर्तनमिष्टम्; सर्प + अजा → सर्पाजा (अ + अ → आ)। इन अनिश्चित भागों पर प्रश्न नहीं।"),
    "15": ("गद्य; विश्वास मध्यम; एक छपी पंक्ति (०२.१२.१५); कोई पाठ-चिह्न नहीं। छपे ‘विडाळ’ में ळ छपाई की आदत है (ल)। "
           "सरट = गिरगिट या बगीचे की छिपकली (सम्भावित)। ‘सर्वम्’ का दायरा (दर्शन, नाम, ध्वनि) कहा नहीं गया। "
           "सन्धि जाँची: सर्वम् + अपि → सर्वमपि; तु + अनिष्टम् → त्वनिष्टम् (उ + अ → व); विडाल + उलूक → विडालोलूक (अ + उ → ओ)।"),
    "16": ("गद्य; विश्वास मध्यम; एक छपी पंक्ति (०२.१२.१६); कोई पाठ-चिह्न नहीं। ‘इष्टः’ एक बार छपा, आगे के जोड़ों पर लागू। "
           "पहचान: ग्रन्थि, अर्बुद, अतिसार, रक्तपित्त, अश्मरी मानक; गुल्म, उदर (रोग), उदावर्त सम्भावित। ‘प्रवर्त्तन’ का दोहरा त्त सामान्य किया गया। "
           "सन्धि जाँची: ग्रन्थि + अर्बुद → ग्रन्थ्यर्बुद (इ + अ → य); शब्दः + इष्टः → शब्द इष्टः और शब्दः + इति → शब्द इति (नियमित विराम, भूल नहीं); "
           "इष्टः + गुल्म- → इष्टो गुल्म- (घोष व्यंजन से पहले अः → ओ); शब्दः + अतिसार → शब्दोऽतिसार; अश्मरी + उदावर्त → अश्मर्युदावर्त (ई + उ → यु)।"),
    "17": ("गद्य; विश्वास उच्च; एक छपी पंक्ति (०२.१२.१७)। पाठ-चिह्न (सम्भव): ‘अन्येपि’ में ऽ नहीं छपा (अन्येऽपि)। "
           "‘योज्याः’ = पिछले सिद्धान्त से लागू किए जाने योग्य; पंक्ति और कुछ नहीं कहती। "
           "सन्धि जाँची: एवम् + अन्ये → एवमन्ये; अन्ये + अपि → अन्येऽपि; ध्वनयः + योज्याः → ध्वनयो योज्याः (घोष व्यंजन से पहले अः → ओ)।"),
    "18": ("गद्य; विश्वास मध्यम; एक छपी पंक्ति (०२.१२.१८)। पाठ-चिह्न (सम्भव): छपा ‘अन्या’ (स्त्रीलिंग) पुंलिंग ‘वादित्रस्वराः’ से मेल नहीं खाता, "
           "‘अन्ये’ पढ़ा गया; ‘स्थावरं’ में समास के भीतर अतिरिक्त अनुस्वार (या छूटा रिक्त स्थान)। ‘त्रात’ = रक्षित या रक्षक (त्रातृ), रूप अनिश्चित। "
           "सन्धि जाँची: सर्वत्र + एव → सर्वत्रैव (अ + ए → ऐ); त्रात + अचल → त्राताचल (छपाई में ऽ); शब्दाः + अन्ये → शब्दा अन्ये (आः स्वर से पहले विसर्ग खोता है); "
           "स्वराः + च → स्वराश्च।"),
    "19": ("गद्य; विश्वास निम्न; एक छपी पंक्ति (०२.१२.१९), सूचियों का एक बहुत लम्बा वाक्य; एकमात्र विधेय ‘प्रतिषिद्धाः’। पाठ-चिह्न (सम्भव): "
           "‘चातुर्गृहात्पूर्वीक्त’ → च आतुरगृहात् पूर्वोक्त (अनुमान; पूर्वोक्त मंगल कार्ड १० के); ‘लाभर्तुष्टि’ में अतिरिक्त र्; ‘वक्रानुवक्रायहा’ → वक्रानुवक्रा ग्रहाः (अनुमान); "
           "‘केतुशिनि’ → केतुशनि; ‘उपकरणेषुवा’ में रिक्त स्थान छूटा (निश्चित)। ‘पलल’ विवादित (कीचड़, मांस या तिल की लुगदी); ‘ऊर्ध्वपाद’ अस्पष्ट; "
           "‘शुभाशुभा आतुरस्य’ पिछले या अगले भाग से जुड़ सकता है। सन्धि जाँची: प्रहार + छेद → प्रहारच्छेद (ह्रस्व स्वर के बाद छ → च्छ); "
           "तत् + विधे → तद्विधे (घोष से पहले त् → द्); भग्न + उपस्कर → भग्नोपस्कर; प्रादुर्भावः + च → प्रादुर्भावश्च। अनुमानित भागों पर प्रश्न नहीं।"),
    "20": ("गद्य; विश्वास उच्च; एक छपी पंक्ति (०२.१२.२०)। पाठ-चिह्न: छपा ‘स्वयमम्येन’ (सम्भव) → स्वयम् अन्येन (म के स्थान पर न); "
           "‘प्रार्थितःसंकल्पितो’ में रिक्त स्थान छूटा (निश्चित), विसर्ग छपा रहा। ‘भाविक’ शब्दशः (आगे होने वाले से सम्बन्धित)। "
           "सन्धि जाँची: स्वप्नः + तु → स्वप्नस्तु (त से पहले ः → स्); सः + सप्तविधः → स सप्तविधः; सप्तविधः + दृष्टः → सप्तविधो दृष्टः; "
           "श्रुतः + अनुभूतः → श्रुतोऽनुभूतः (अः + अ → ओऽ); दोषजः + च → दोषजश्च।"),
    "21": ("गद्य; विश्वास मध्यम; एक छपी पंक्ति (०२.१२.२१); कोई पाठ-चिह्न नहीं। अपूर्ण: ‘तथा’ के बाद की सूची का विधेय नहीं छपा; डेटा इसे ‘अफलः’ के समान पढ़ता है। "
           "‘नातिसुप्तदृष्टः’ दो प्रकार से पढ़ा जा सकता है। ‘आद्यः पञ्चविधः’ = कार्ड २० के पहले पाँच प्रकार। "
           "सन्धि जाँची: तत्र + आद्यः → तत्राद्यः; पञ्चविधः + अफलः → पञ्चविधोऽफलः; -प्रकृतिः + विस्मृतः → -प्रकृतिर्विस्मृतः (इ के बाद ः, घोष से पहले → र्); "
           "दिवा + अति- → दिवाऽति- (छपाई में ऽ); पूर्वरात्रे + अल्पम् → पूर्वरात्रेऽल्पम्; चिरात् + च → चिराच्च।"),
    "22": ("गद्य; विश्वास मध्यम; एक छपी पंक्ति (०२.१२.२२)। पाठ-चिह्न (निश्चित): ‘महत्सद्यश्च’ में रिक्त स्थान छूटे (महत् सद्यश् च)। "
           "अपूर्ण: ‘महत्’ किसका, यह छपा नहीं (सम्भवतः कार्ड २१ का फल), जोड़ा नहीं गया। गोसर्ग = प्रातःकाल। "
           "सन्धि जाँची: सद्यः + च → सद्यश्च (च से पहले ः → श्); महत् + सद्यः में स से पहले त् नहीं बदलता।"),
    "23": ("गद्य; विश्वास मध्यम; एक छपी पंक्ति (०२.१२.२३); कार्ड २२ से आगे, कर्ता (स्वप्न) छपा नहीं। पाठ-चिह्न: ‘चपुनरनुपहतः’ में रिक्त स्थान छूटे (निश्चित); "
           "‘शमनीयमादिभिः’ में अतिरिक्त म् (सम्भव), ‘दान-शमनीय-आदिभिः’ पढ़ा गया। शमनीय = शान्ति के कर्म। "
           "सन्धि जाँची: पुनर् + अनुपहतः → पुनरनुपहतः; प्रतीपैः + वा → प्रतीपैर्वा; वचोभिः + दान → वचोभिर्दान; आदिभिः + वा → आदिभिर्वा "
           "(अ/आ से भिन्न स्वर के बाद ः, घोष से पहले → र्)।"),
    "24": ("गद्य; विश्वास उच्च; एक छपी पंक्ति (०२.१२.२४); कोई पाठ-चिह्न नहीं। ‘हन्यते’ = आहत होता है; ‘मारा जाता है’ भी सम्भव, शब्दशः अर्थ रखा गया। "
           "ज्वर = बुखार (मानक); प्रेत = दिवंगत आत्मा। सन्धि जाँची: शुना + आकृष्यते → शुनाऽऽकृष्यते (आ + आ → आ; छपाई में रिक्त स्थान और ऽऽ); "
           "सः + हन्यते → स हन्यते; मद्यम् + पिबन् → मद्यं पिबन्।"),
    "25": ("गद्य; विश्वास मध्यम; एक छपी पंक्ति (०२.१२.२५)। पाठ-चिह्न (सम्भव): ‘हसन्नार्या’ = हसन् नार्या (रिक्त स्थान छूटा), पर हसन् + आर्या की नियमित सन्धि भी यही रूप देती है; "
           "‘स्त्री द्वारा’ अर्थ डेटा ने चुना। अम्बर = वस्त्र या आकाश, दोनों सम्भव। कार्ड २४ की क्रिया समझी जाती है। रक्तपित्त = रक्तस्राव का रोग (मानक)। "
           "सन्धि जाँची: रक्त + आभम् → रक्ताभम्; यः + वा → यो वा; -वस्त्रः + हसन् → -वस्त्रो हसन्; सः + रक्तपित्तेन → स रक्तपित्तेन।"),
    "26": ("गद्य; विश्वास निम्न; दो छपी पंक्तियाँ (०२.१२.२६ और ०२.१२.२७) जोड़ी गईं। पंक्ति ०२.१२.२६ में क्रिया नहीं छपी (‘ले जाया जाता है’ जैसी अपेक्षित), जोड़ी नहीं गई। "
           "यक्ष्मन् = क्षय, शोष (सम्भावित); गुल्म = पेट की गाँठ (सम्भावित); हृद् = हृदय (मानक)। पाठ-चिह्न (निश्चित): ‘जायतेस’ = जायते स। "
           "सन्धि जाँची: खर + उष्ट्र → खरोष्ट्र (अ + उ → ओ); वराह + अन्यतमेन → वराहान्यतमेन; वंशः + तालः → वंशस्तालः (त से पहले ः → स्); तालः + वा → तालो वा।"),
}

# ================================================================ AIDS
AIDS = {
    "14": {
        "frame": "किनका: शश, सर्प, अजा, अवि, गोधा आदि → क्या इष्ट: कीर्तनम् (नाम लेना) → क्या नहीं: दर्शनम् → अन्तिम जोड़ा: विपरीतम्।",
        "contrast": "कीर्तनम् (नाम लेना) इष्ट ⇄ दर्शनम् (देखना) इष्ट नहीं: दोनों इसी इकाई में।",
        "chunks": "शशसर्पाजाऽविगोधराजाहकमूकराणां तु | कीर्तनमिष्टं | न दर्शनं | विरुतं | चविपरीतंमृक्षवानरयोः",
        "sandhi": "स्वर से पहले अन्तिम म् जुड़ता है: कीर्तनम् + इष्टम् → कीर्तनमिष्टम् · अ + अ → आ: सर्प + अजा → सर्पाजा।",
    },
    "15": {
        "chunks": "सर्वमपि | त्वनिष्टं | सरटकुक्कुटविडाळोलूकानां",
        "sandhi": "उ + भिन्न स्वर → व्: तु + अनिष्टम् → त्वनिष्टम् · अ + उ → ओ: विडाल + उलूक → विडालोलूक।",
        "anchors": "चार जीव, सब कुछ अनिष्ट: सरट (सम्भावित: गिरगिट), मुर्गा, बिल्ली, उल्लू। (मेरी याद-पद्धति)",
    },
    "16": {
        "diagram": {"groups": [
            {"label": "रोग-समूह → इष्ट शब्द (छपे क्रम में)",
             "items": ["१ ग्रन्थि, अर्बुद आदि → छेद", "२ गुल्म, उदर आदि → भेद", "३ अतिसार, रक्तपित्त आदि → रुद्ध",
                       "४ अश्मरी, उदावर्त आदि → प्रवर्तन"]}]},
        "chunks": "तथा | ग्रंथ्यर्बुदादिषु छेदशब्दइष्टो | गुल्मोदरादिषु भेदशब्दो | ऽतिसाररक्तपित्तादिषु रुद्धशब्दो | ऽश्मर्युदावर्तादिषु प्रवर्त्तनशब्दइति",
        "sandhi": ("अः + अ से भिन्न स्वर → अ, स्वर अलग: शब्दः + इष्टः → शब्द इष्टः · घोष व्यंजन से पहले अः → ओ: इष्टः + गुल्म- → इष्टो गुल्म- · "
                   "इ + अ → य: ग्रन्थि + अर्बुद → ग्रन्थ्यर्बुद · ई + उ → यु: अश्मरी + उदावर्त → अश्मर्युदावर्त।"),
    },
    "17": {
        "frame": "कैसे: एवम् (इसी प्रकार) → कौन: अन्ये ध्वनयः (दूसरी ध्वनियाँ) → क्या करें: योज्याः (लागू करें)।",
        "chunks": "एवमन्येपि | ध्वनयो | योज्याः",
        "sandhi": "ए + अ → एऽ: अन्ये + अपि → अन्येऽपि (यहाँ ऽ नहीं छपा) · घोष व्यंजन से पहले अः → ओ: ध्वनयः + योज्याः → ध्वनयो योज्याः।",
    },
    "18": {
        "chunks": "सर्वत्रैव च | स्थिरस्थावरंवर्धमानत्राताऽचलध्रुवक्षेमशिवादयः शब्दा | अन्या वादित्रस्वराश्च | श्रेष्ठाः",
        "sandhi": "अ + ए → ऐ: सर्वत्र + एव → सर्वत्रैव · आः स्वर से पहले विसर्ग खोता है: शब्दाः + अन्ये → शब्दा अन्ये · च से पहले ः → श्: स्वराः + च → स्वराश्च।",
        "anchors": "सब शब्द ‘टिकाऊ, बढ़ता, सुरक्षित, शुभ’ के: स्थिर, अचल, ध्रुव, वर्धमान, क्षेम, शिव। (मेरी याद-पद्धति)",
    },
    "19": {
        "frame": ("क्या: निषिद्ध शब्द, क्रूर ध्वनियाँ, सूखा काँटेदार वृक्ष, प्रवेश पर अशुभ दर्शन, वैद्य का असत्कार आदि → "
                  "किसलिए: चिकित्साप्रतिषेधाय (चिकित्सा के निषेध के लिए)।"),
        "diagram": {"groups": [
            {"label": "निषिद्ध शब्द (छपे क्रम में)",
             "items": ["१ क्षुत", "२ हत", "३ पतित", "४ आक्रोश", "५ प्रहार", "६ छेद", "७ भेद", "८ दाह", "९ हाहा", "१० प्रतिषेध"]}]},
        "chunks": ("क्षुतहतपतिताक्रोशप्रहारच्छेदभेददाहहाहाप्रतिषेधादिशब्दाः प्रतिषिद्धाः | प्रतिषिद्धायां दीप्तायां च दिशि | क्रूराः पक्षिमृगध्वनयो | "
                   "वृक्षे वा रूक्षशुष्के सवल्लिकंटके | तद्विधे वा देशे | दर्शनं च ... | प्रवेशे | ... | प्रविष्टस्य तु भिषजः न सत्कारो | ... | चिकित्साप्रतिषेधाय"),
        "sandhi": ("घोष से पहले त् → द्: तत् + विधे → तद्विधे · ह्रस्व स्वर के बाद छ → च्छ: प्रहार + छेद → प्रहारच्छेद · "
                   "अ + उ → ओ: भग्न + उपस्कर → भग्नोपस्कर।"),
    },
    "20": {
        "diagram": {"groups": [
            {"label": "स्वप्न के सात प्रकार (छपे क्रम में)",
             "items": ["१ दृष्ट", "२ श्रुत", "३ अनुभूत", "४ प्रार्थित", "५ संकल्पित", "६ भाविक", "७ दोषज"]}]},
        "seesaw": "स्वयम् (स्वयं) ⇄ अन्येन (दूसरे द्वारा) देखा · शुभ ⇄ अशुभ का कारण: दोनों जोड़े इसी इकाई में।",
        "chunks": "स्वप्नस्तु | स्वयमम्येन वा दृष्टः | शुभाशुभहेतुः | स सप्तविधो | दृष्टः श्रुतोऽनुभूतः | प्रार्थितःसंकल्पितो | भाविको दोषजश्च",
        "sandhi": "त से पहले ः → स्: स्वप्नः + तु → स्वप्नस्तु · अः + अ → ओऽ: श्रुतः + अनुभूतः → श्रुतोऽनुभूतः · सः व्यंजन से पहले विसर्ग खोता है: सः + सप्तविधः → स सप्तविधः।",
    },
    "21": {
        "diagram": {"groups": [
            {"label": "कार्ड २१ (छपे क्रम में)",
             "items": ["पहले पाँच प्रकार: अफल", "तथा: अपनी प्रकृति के अनुसार", "विस्मृत", "दिवा (दिन में)", "अतिह्रस्व", "अतिदीर्घ",
                       "गहरी नींद में न देखा", "(इन छह का विधेय नहीं छपा)", "रात्रि का पहला भाग: थोड़ा फल, देर से"]}]},
        "seesaw": "अतिह्रस्व (बहुत छोटा) ⇄ अतिदीर्घ (बहुत लम्बा): दोनों इसी इकाई में।",
        "chunks": "तत्राद्यः | पंचविधोऽफलः | तथा यथास्वप्रकृतिर्विस्मृतो | दिवाऽतिह्रस्वोऽतिदीर्घो | नातिसुप्तदृष्टश्च | पूर्वरात्रेऽल्पं चिराच्च | फलं करोति",
        "sandhi": "अः + अ → ओऽ: पञ्चविधः + अफलः → पञ्चविधोऽफलः · च से पहले त् → च्: चिरात् + च → चिराच्च · ए + अ → एऽ: पूर्वरात्रे + अल्पम् → पूर्वरात्रेऽल्पम्।",
    },
    "22": {
        "frame": "कब: गोसर्गे (भोर में, गायें छोड़ते समय) → कैसा: महत् (महान) → कब फले: सद्यः (तुरन्त); संज्ञा छपी नहीं।",
        "chunks": "गोसर्गे | महत्सद्यश्च",
        "sandhi": "च से पहले ः → श्: सद्यः + च → सद्यश्च · स से पहले त् नहीं बदलता: महत् + सद्यः → महत्सद्यः।",
    },
    "23": {
        "frame": "कौन: (स्वप्न, छपा नहीं) → किससे नष्ट न हुआ: निद्रा (फिर), प्रतीप वचन, दान, शमनीय आदि → अनुपहतः।",
        "chunks": "निद्रया | चपुनरनुपहतः | प्रतीपैर्वा | वचोभिर्दानशमनीयमादिभिर्वा",
        "sandhi": "अ/आ से भिन्न स्वर के बाद ः, घोष से पहले → र्: प्रतीपैः + वा → प्रतीपैर्वा, वचोभिः + दान → वचोभिर्दान · र् + स्वर जुड़ता है: पुनर् + अनुपहतः → पुनरनुपहतः।",
    },
    "24": {
        "chain": {"steps": ["यः: जो", "प्रेतैः सह: प्रेतों के साथ", "मद्यं पिबन्: मद्य पीता हुआ", "शुना ऽऽकृष्यते: कुत्ते से खींचा जाता",
                            "स हन्यते ज्वरेण: वह ज्वर से आहत"]},
        "chunks": "तत्र | यः प्रेतैः सह | मद्यं पिबन् | शुना ऽऽकृष्यते | स हन्यते | ज्वरेण",
        "sandhi": "आ + आ → आ: शुना + आकृष्यते → शुनाऽऽकृष्यते (छपाई में ऽऽ) · सः व्यंजन से पहले विसर्ग खोता है: सः + हन्यते → स हन्यते।",
    },
    "25": {
        "frame": "कौन (१): लाख-लाल अम्बर देखे → कौन (२): लाल देह-माला-वस्त्र, हँसता, स्त्री द्वारा ले जाया जाए → फल: स रक्तपित्तेन।",
        "chunks": "यो लाक्षारक्ताभमंबरं पश्यति | यो वा रक्तदेहमाल्यवस्त्रो | हसन्नार्या ह्रियते | स रक्तपित्तेन",
        "sandhi": "अ + आ → आ: रक्त + आभम् → रक्ताभम् · घोष व्यंजन से पहले अः → ओ: यः + वा → यो वा, -वस्त्रः + हसन् → -वस्त्रो हसन्।",
    },
    "26": {
        "diagram": {"groups": [
            {"label": "कार्ड २६: दो स्वप्न",
             "items": ["पंक्ति १: दक्षिण दिशा, गधा-ऊँट-भैंसा-सूअर में से एक (क्रिया नहीं छपी) → यक्ष्मन्",
                       "पंक्ति २: हृदय में काँटेदार लता, बाँस या ताड़ उगे → गुल्म"]}]},
        "chunks": "यो याम्यां दिशं | खरोष्ट्रमहिषवराहान्यतमेन | स यक्ष्मणा || यस्य कंटकिनी लता | वंशस्तालो वा हृदि | जायतेस गुल्मेन",
        "sandhi": "अ + उ → ओ: खर + उष्ट्र → खरोष्ट्र · अ + अ → आ: वराह + अन्यतमेन → वराहान्यतमेन · त से पहले ः → स्: वंशः + तालः → वंशस्तालः।",
    },
}

# ================================================================ IMAGE_SPECS
IMAGE_SPECS = {
    ("16", "diagram"): {
        "file": "sh12-ishta-shabda-16.svg",
        "alt": ("Table of card 16: granthi and arbuda with the word 'cutting'; gulma and udara with 'breaking'; atisāra "
                "and raktapitta with 'stopped'; aśmarī and udāvarta with 'impelling'."),
        "type": "table",
        "title": "कार्ड १६: रोग और इष्ट शब्द",
        "heads": ["रोग-समूह (आदि)", "इष्ट शब्द"],
        "rows": [["ग्रन्थि, अर्बुद", "छेद: काटना"], ["गुल्म, उदर", "भेद: तोड़ना"], ["अतिसार, रक्तपित्त", "रुद्ध: रुका हुआ"],
                 ["अश्मरी, उदावर्त", "प्रवर्तन: चलाना"]],
    },
    ("19", "diagram"): {
        "file": "sh12-nishiddha-19.svg",
        "alt": ("Table of card 19 in printed order: ten forbidden words: sneeze, struck, fallen, outcry, blow, cutting, "
                "breaking, burning, 'hā hā', prohibition."),
        "type": "table",
        "title": "कार्ड १९: निषिद्ध शब्द",
        "heads": ["क्रम", "छपा शब्द: अर्थ"],
        "rows": [["१", "क्षुत: छींक"], ["२", "हत: मारा गया"], ["३", "पतित: गिरा"], ["४", "आक्रोश: चीख"], ["५", "प्रहार: चोट"],
                 ["६", "छेद: काटना"], ["७", "भेद: तोड़ना"], ["८", "दाह: जलना"], ["९", "हाहा"], ["१०", "प्रतिषेध: निषेध"]],
    },
    ("20", "diagram"): {
        "file": "sh12-svapna-20.svg",
        "alt": ("Table of card 20 in printed order: the seven kinds of dream: seen, heard, experienced, desired, imagined, "
                "bhāvika (of what will be), born of the doṣas."),
        "type": "table",
        "title": "कार्ड २०: स्वप्न के सात प्रकार",
        "heads": ["क्रम", "छपा शब्द: अर्थ"],
        "rows": [["१", "दृष्टः: देखा"], ["२", "श्रुतः: सुना"], ["३", "अनुभूतः: अनुभव किया"], ["४", "प्रार्थितः: चाहा"],
                 ["५", "संकल्पितः: कल्पित"], ["६", "भाविकः: आगे होने वाला"], ["७", "दोषजः: दोषों से उत्पन्न"]],
    },
    ("21", "diagram"): {
        "file": "sh12-phala-21.svg",
        "alt": ("Table of card 21: the first five kinds are fruitless; six more listed after tathā have no printed "
                "predicate; a dream in the first part of the night gives little fruit, after a long time."),
        "type": "table",
        "title": "कार्ड २१: स्वप्न और फल",
        "heads": ["स्वप्न", "पंक्ति क्या कहती है"],
        "rows": [["पहले पाँच प्रकार", "अफल: निष्फल"],
                 ["तथा: प्रकृति अनुसार, विस्मृत, दिन का, अतिह्रस्व, अतिदीर्घ, गहरी नींद में न देखा", "विधेय नहीं छपा"],
                 ["रात्रि का पहला भाग", "थोड़ा फल, देर से"]],
    },
    ("24", "chain"): {
        "file": "sh12-jvara-24.svg",
        "alt": ("Chain of card 24: he who, drinking madya with the departed, is dragged by a dog, is struck down by "
                "fever (jvara)."),
        "type": "chain",
        "title": "कार्ड २४: स्वप्न और ज्वर",
        "steps": ["प्रेतों के साथ मद्य पीता हुआ", "कुत्ते द्वारा खींचा जाता है", "वह ज्वर से आहत होता है"],
    },
    ("26", "diagram"): {
        "file": "sh12-yakshma-gulma-26.svg",
        "alt": ("Table of card 26: line 1, the southern direction with one of donkey, camel, buffalo or boar (verb not "
                "printed), goes with yakṣman (probable: wasting disease); line 2, a thorny creeper, bamboo or palm "
                "growing in the heart goes with gulma (probable: abdominal lump)."),
        "type": "table",
        "title": "कार्ड २६: दो स्वप्न, दो रोग",
        "heads": ["स्वप्न", "रोग"],
        "rows": [["दक्षिण दिशा; गधा, ऊँट, भैंसा या सूअर (क्रिया नहीं छपी)", "यक्ष्मन् (सम्भावित: क्षय)"],
                 ["हृदय में काँटेदार लता, बाँस या ताड़ उगे", "गुल्म (सम्भावित: पेट की गाँठ)"]],
    },
}
