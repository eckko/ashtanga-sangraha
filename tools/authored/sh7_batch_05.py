from helpers import mcq, match, order, fill, multi, accepts


AUTHORED = {}

# ---------------------------------------------------------------- unit 55
AUTHORED["55"] = {
    "title": "एकचत्वारिंशच्छिरा मर्माणि",
    "question": "By unit 55, which marmas are the forty-one vessel-marmas (sirā-marma)?",
    "rule": ("Urvī, lohitākhya, nābhi, hṛdaya, stanamūla and the rest, down to śṛṅgāṭaka: forty-one vessel-marmas "
             "(एकचत्वारिंशत् सिरा-मर्माणि), the second of the five kinds by structure."),
    "limits": ("Verbless prose list. Printed मन्मा is read as manyā only by conjecture; अलाप is probably the apālāpa "
               "of unit 26. No question rests on either, or on the count forty-one (it counts sides and limbs by the "
               "data's count check, not printed). Printed शिरा = सिरा."),
    "explain_hi": ("रचना के अनुसार पाँच भेदों में दूसरा: सिरा-मर्म। "
                   "उर्वी, लोहिताख्य, नाभि, हृदय, स्तनमूल, अपस्तम्भ, अलाप, पार्श्वसन्धि, बृहती, नीला, मन्या (अनुमानित पाठ), मातृका, फण, अपाङ्ग, स्थपनी और शृङ्गाटक: ये इकतालीस सिरा-मर्म हैं। "
                   "नाभि और हृदय सामान्य शब्द भी हैं (नाभि, हृदय: मानक); बाकी नाम मर्म-नाम ही रखे गए। "
                   "छपा ‘मन्मा’ कोई मर्म-नाम नहीं, अनुमान से ‘मन्या’ पढ़ा गया; छपा ‘अलाप’ सम्भवतः इकाई २६ का अपालाप है। "
                   "‘इकतालीस’ नामों की गिनती नहीं, हर ओर और हर अंग की गिनती है (डेटा का गणना-निरीक्षण, छपा नहीं)।"),
    "hook": "सिरा-मर्म इकतालीस: उर्वी से शृङ्गाटक तक।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 55, what kind of marma are urvī, nābhi and hṛdaya?",
            ("Vessel-marmas (sirā-marma)", "उर्वी ... एकचत्वारिंशच्छिरा मर्माणि: they are vessel-marmas."),
            [("Sinew-marmas (snāva-marma)", "The sinew-marmas of unit 56 begin with kṣipra and kūrca."),
             ("Bone-marmas (asthi-marma)", "The bone-marmas of unit 57 are kaṭīkataruṇa, nitamba, aṃsaphalaka and śaṅkha."),
             ("Joint-marmas (sandhi-marma)", "The joint-marmas of unit 58 begin with gulpha and maṇibandha.")],
            "Vessel-marmas.",
            "उर्वी ... शिरा मर्माणि."),
        order(1, "Put these marma names of unit 55 in the printed order.",
              ["उर्वी", "नाभि", "पार्श्वसंधि", "मातृका", "स्थपनी", "शृंगाटक"],
              "The list runs from urvī through nābhi, pārśvasandhi and mātṛkā to sthapanī and śṛṅgāṭaka.",
              "उर्वी → नाभि → पार्श्वसंधि → मातृका → स्थपनी → शृंगाटक."),
        match(2, "Match each word of unit 55 to its meaning.",
              [["शिरा (सिरा)", "vessel"], ["मूल", "root, base"], ["नाभि", "navel (standard)"],
               ["हृदय", "heart (standard)"], ["मर्माणि", "marmas (vital points)"]],
              "Marmas of the vessels (stana-mūla = breast-root); nābhi and hṛdaya are also the ordinary words for navel and heart.",
              "शिरा, मूल, नाभि, हृदय, मर्माणि.", role="extend",
              teaches="सिरामर्म is a tat-puruṣa, a marma of vessels: the second kind by structure. The print spells सिरा as शिरा."),
        mcq("discriminate", 3, "Which split of फणापांग in unit 55 is right?",
            ("फण + अपाङ्ग", "अ + अ → आ: फण + अपाङ्ग → फणापाङ्ग; both are marma names of the list."),
            [("फणः + अपाङ्ग", "अः before अ would give ओऽ (फणोऽपाङ्ग); compound members take no case ending."),
             ("फणि + अपाङ्ग", "इ before अ would become य्: फण्यपाङ्ग."),
             ("फण + उपाङ्ग", "अ + उ would give ओ: फणोपाङ्ग.")],
            "फण (phaṇa) + अपाङ्ग (apāṅga): अ + अ → आ.",
            "अ + अ → आ."),
        multi("apply", 4, "Which are named in unit 55 among the forty-one vessel-marmas?",
              [("Hṛdaya", "Right: हृदय is in the list."),
               ("Talahṛdaya", "Talahṛdaya is a flesh-marma (unit 54)."),
               ("Mātṛkā", "Right: मातृका is in the list."),
               ("Gulpha", "Gulpha is a joint-marma (unit 58)."),
               ("Śṛṅgāṭaka", "Right: शृङ्गाटक closes the list.")],
              [0, 2, 4],
              "Hṛdaya, mātṛkā and śṛṅgāṭaka are vessel-marmas; talahṛdaya is a flesh-marma, gulpha a joint-marma.",
              "उर्वी ... शृंगाटकान्येकचत्वारिंशच्छिरा मर्माणि."),
        mcq("transfer", 5, "By the rule of फणापाङ्ग (फण + अपाङ्ग), how is पुष्प + अञ्जलिः (a handful of flowers) joined in a new example?",
            ("पुष्पाञ्जलिः", "अ + अ → आ, as फण + अपाङ्ग → फणापाङ्ग."),
            [("पुष्पञ्जलिः", "The two अs do not shrink to one short अ; they give आ."),
             ("पुष्पेञ्जलिः", "ए comes from अ + इ, not from अ + अ."),
             ("पुष्पोञ्जलिः", "ओ comes from अ + उ, not from अ + अ.")],
            "पुष्प + अञ्जलिः = पुष्पाञ्जलिः, like फण + अपाङ्ग = फणापाङ्ग.",
            "अ + अ → आ.",
            teaches="Two short अs merge into one आ: फण + अपाङ्ग → फणापाङ्ग, पुष्प + अञ्जलिः → पुष्पाञ्जलिः."),
    ],
}

# ---------------------------------------------------------------- unit 56
AUTHORED["56"] = {
    "title": "सप्तविंशति स्नावमर्माणि",
    "question": "By unit 56, which marmas are the twenty-seven sinew-marmas (snāva-marma)?",
    "rule": ("Kṣipra, kūrca, kūrcaśiras, viṭapa, kakṣādhara, āṇi, basti, aṃsa, vidhura and utkṣepa: twenty-seven "
             "sinew-marmas (सप्तविंशति स्नावमर्माणि); स्नाव = sinew (स्नायु)."),
    "limits": ("Verbless prose list, printed as one run. कक्षाधराणि is read by the data as kakṣādhara + āṇi (the marma "
               "of unit 11), not as a neuter plural: no question rests on āṇi. Twenty-seven counts limbs and sides "
               "(the data's count check, not printed). basti = bladder, aṃsa = shoulder (standard)."),
    "explain_hi": ("रचना के अनुसार तीसरा भेद: स्नायु-मर्म (स्नाव = स्नायु)। "
                   "क्षिप्र, कूर्च, कूर्चशिरस्, विटप, कक्षाधर, आणि, बस्ति (मूत्राशय, मानक), अंस (कन्धा, मानक), विधुर और उत्क्षेप: ये सत्ताईस स्नायु-मर्म हैं। "
                   "छपे ‘कक्षाधराणि’ को डेटा कक्षाधर + आणि पढ़ता है (आणि इकाई ११ का मर्म), क्योंकि तब सत्ताईस की गिनती बैठती है; यह विभाजन डेटा का पाठ है, इसलिए आणि पर प्रश्न नहीं। "
                   "सन्धि: कूर्चशिरः + विटप → कूर्चशिरोविटप (अः + घोष व्यंजन → ओ); बस्ति + अंस → बस्त्यंस (इ + अ → य)।"),
    "hook": "स्नायु-मर्म सत्ताईस: क्षिप्र से उत्क्षेप तक।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "In unit 56, what are kṣipra, viṭapa and utkṣepa counted as?",
            ("Sinew-marmas (snāva-marma)", "सप्तविंशति स्नावमर्माणि: they are among the twenty-seven sinew-marmas."),
            [("Bone-marmas (asthi-marma)", "The bone-marmas of unit 57 are kaṭīkataruṇa, nitamba, aṃsaphalaka and śaṅkha."),
             ("Joint-marmas (sandhi-marma)", "The joint-marmas of unit 58 begin with gulpha and maṇibandha."),
             ("Flesh-marmas (māṃsa-marma)", "The flesh-marmas of unit 54 are talahṛdaya, indrabasti, guda and stanarohita.")],
            "They are sinew-marmas.",
            "क्षिप्र ... उत्क्षेपाः सप्तविंशति स्नावमर्माणि."),
        order(1, "Put these marma names of unit 56 in the printed order.",
              ["क्षिप्र", "कूर्चशिरस्", "विटप", "बस्ति", "विधुर", "उत्क्षेप"],
              "Kṣipra, (kūrca), kūrcaśiras, viṭapa, (kakṣādhara, āṇi), basti, (aṃsa), vidhura, utkṣepa.",
              "क्षिप्र → कूर्चशिरस् → विटप → बस्ति → विधुर → उत्क्षेप."),
        match(2, "Match each word of unit 56 to its meaning.",
              [["स्नाव", "sinew (snāyu)"], ["सप्तविंशति", "twenty-seven"], ["बस्ति", "bladder (standard)"],
               ["अंस", "shoulder (standard)"]],
              "Twenty-seven sinew-marmas; basti and aṃsa are also the ordinary words for bladder and shoulder.",
              "स्नाव, सप्तविंशति, बस्ति, अंस.", role="extend",
              teaches="स्नावमर्म is a marma of sinew, the third kind by structure; स्नाव is a form of स्नायु."),
        mcq("discriminate", 3, "Which split of बस्त्यंस in unit 56 is right?",
            ("बस्ति + अंस", "इ before a different vowel becomes य्: बस्ति + अंस → बस्त्यंस."),
            [("बस्त्य + अंस", "अ + अ would give आ: बस्त्यांस, with a long आ."),
             ("बस्ते + अंस", "ए before अ would give एऽ: बस्तेऽंस."),
             ("बस्तिः + अंस", "इः before a vowel would give इर्: बस्तिरंस; compound members take no ending.")],
            "बस्ति (basti) + अंस (aṃsa): इ + अ → य.",
            "इ + a different vowel → य्."),
        mcq("apply", 4, "Why is कूर्चशिरस् printed कूर्चशिरो before विटप in unit 56?",
            ("Final -अस् before a voiced consonant → ओ", "व is a voiced consonant: कूर्चशिरः + विटप → कूर्चशिरोविटप."),
            [("Final -अस् before any consonant → ओ", "Not before every consonant: before त or थ the visarga becomes स्."),
             ("ओ is a case ending put on शिरस्", "Compound members take no case ending; the ओ comes from sandhi."),
             ("Final -अस् at a pause → ओ", "At a pause the visarga stays ः; here विटप follows.")],
            "कूर्चशिरस् + विटप: -अस् (visarga) before the voiced consonant व → ओ.",
            "अः / -अस् + voiced consonant → ओ."),
        mcq("transfer", 5, "By the rule of बस्त्यंस (बस्ति + अंस), how is दधि + अत्र (curd here) joined in a new example?",
            ("दध्यत्र", "इ before अ becomes य्, as बस्ति + अंस → बस्त्यंस."),
            [("दधत्र", "The इ cannot simply drop before अ."),
             ("दधेत्र", "ए comes from अ + इ, not from इ + अ."),
             ("दध्यात्र", "A long आ would need इ + आ; अत्र begins with a short अ.")],
            "दधि + अत्र = दध्यत्र, like बस्ति + अंस = बस्त्यंस.",
            "इ + a different vowel → य् + that vowel.",
            teaches="A final इ before a different vowel becomes य्, and the vowel keeps its length: बस्ति + अंस → बस्त्यंस."),
    ],
}

# ---------------------------------------------------------------- unit 57
AUTHORED["57"] = {
    "title": "अष्टावस्थिमर्माणि",
    "question": "By unit 57, which marmas are the eight bone-marmas (asthi-marma)?",
    "rule": ("Kaṭīkataruṇa, nitamba, aṃsaphalaka (probably the shoulder-blades) and śaṅkha (probably the temples), "
             "however (तु): eight bone-marmas (अष्टौ अस्थिमर्माणि), the fourth kind by structure."),
    "limits": ("Verbless prose list, one printed token. aṃsaphalaka = shoulder-blade and śaṅkha = temple are probable; "
               "nitamba = buttock, hip is the standard word sense; no question rests on these identifications. Eight "
               "is as printed; how it is reached is not stated in the line."),
    "explain_hi": ("रचना के अनुसार चौथा भेद: अस्थि-मर्म। "
                   "कटीकतरुण, नितम्ब (नितम्ब, कूल्हा: मानक शब्दार्थ), अंसफलक (सम्भवतः कन्धे की चपटी हड्डियाँ) और शङ्ख (सम्भवतः कनपटियाँ): ये आठ अस्थि-मर्म हैं। "
                   "‘तु’ को पिछली सूची से हल्का भेद माना गया है। "
                   "पूरी पंक्ति एक ही छपा शब्द-समूह है, जिसमें चार सन्धियाँ हैं: नितम्ब + अंसफलक → नितम्बांसफलक (अ + अ → आ), शङ्खाः + तु → शङ्खास्तु (त से पहले विसर्ग → स्), "
                   "तु + अष्टौ → त्वष्टौ (उ + अ → व), अष्टौ + अस्थि → अष्टावस्थि (औ + स्वर → आव्)।"),
    "hook": "अस्थि-मर्म आठ: कटीकतरुण, नितम्ब, अंसफलक, शङ्ख।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 57, how many bone-marmas (asthi-marma) are counted?",
            ("Eight (aṣṭau)", "अष्टावस्थिमर्माणि: eight bone-marmas."),
            [("Eleven (ekādaśa)", "Eleven is the count of the flesh-marmas (unit 54)."),
             ("Twenty (viṃśati)", "Twenty is the count of the joint-marmas (unit 58)."),
             ("Forty-one (ekacatvāriṃśat)", "Forty-one is the count of the vessel-marmas (unit 55).")],
            "Eight bone-marmas.",
            "अष्टावस्थिमर्माणि = अष्टौ अस्थिमर्माणि."),
        order(1, "Put the marma names of unit 57 in the printed order.",
              ["कटीकतरुण", "नितंब", "अंसफलक", "शंख"],
              "Kaṭīkataruṇa, nitamba, aṃsaphalaka, śaṅkha: eight bone-marmas.",
              "कटीकतरुण → नितंब → अंसफलक → शंख."),
        fill(2, "Unit 57 names eight ____मर्माणि (bone-marmas). Type the first member in Devanagari or in English letters (e.g. dharma).",
             accepts("अस्थि"),
             "अस्थि (bone): अष्टौ अस्थिमर्माणि, printed अष्टावस्थिमर्माणि.",
             "अस्थि = bone; अस्थिमर्म is a marma of bone, the fourth kind by structure.",
             "अष्टौ अस्थिमर्माणि."),
        mcq("discriminate", 3, "Which split of अष्टावस्थि in unit 57 is right?",
            ("अष्टौ + अस्थि", "औ before a vowel becomes आव्: अष्टौ + अस्थि → अष्टावस्थि (as printed)."),
            [("अष्टा + वस्थि", "वस्थि is not a word; the व् comes from औ."),
             ("अष्टः + अस्थि", "अः before अ would give ओऽ: अष्टोऽस्थि; the numeral is अष्टौ."),
             ("अष्टे + अस्थि", "ए before अ would give एऽ: अष्टेऽस्थि.")],
            "अष्टौ (eight) + अस्थि (bone): औ + vowel → आव्.",
            "औ + vowel → आव् (as printed)."),
        mcq("apply", 4, "Why does शङ्खाः appear as शङ्खास् before तु in unit 57?",
            ("A visarga before त becomes स्", "शङ्खाः + तु → शङ्खास्तु: visarga before त or थ → स्."),
            [("Every visarga after आ becomes स्", "Not every one: आः drops its visarga before a voiced sound."),
             ("The स् belongs to the word तु", "तु is the indeclinable 'but'; the स् comes from the visarga."),
             ("The स् marks a genitive here", "शङ्खाः is nominative plural (gram: m. nom. pl.); the स् is sandhi.")],
            "शङ्खाः + तु: visarga before त → स्.",
            "Visarga + त / थ → स्."),
        mcq("transfer", 5, "By the rule of अष्टावस्थि (अष्टौ + अस्थि), how is तौ + अपि (those two also) joined in a new example?",
            ("तावपि", "औ before a vowel becomes आव्, as अष्टौ + अस्थि → अष्टावस्थि."),
            [("तौपि", "औ does not swallow the following अ."),
             ("तायपि", "आय् comes from ऐ before a vowel, not from औ."),
             ("तोऽपि", "ओऽ comes from अः before अ, not from औ.")],
            "तौ + अपि = तावपि, like अष्टौ + अस्थि = अष्टावस्थि.",
            "औ + vowel → आव्.",
            teaches="A final औ before a vowel becomes आव्: अष्टौ + अस्थि → अष्टावस्थि, तौ + अपि → तावपि."),
    ],
}

# ---------------------------------------------------------------- unit 58
AUTHORED["58"] = {
    "title": "विंशति संधिमर्माणि",
    "question": "By unit 58, which marmas are the twenty joint-marmas (sandhi-marma)?",
    "rule": ("Gulpha (ankle), maṇibandha (wrist), jānu (knee), kūrpara (elbow), kukundara, kṛkāṭikā, āvarta, sīmanta "
             "and adhipati: twenty joint-marmas (विंशति सन्धिमर्माणि), the fifth kind by structure."),
    "limits": ("Verbless prose list. kukundara and kṛkāṭikā regions are probable; no question rests on them. The plural "
               "अधिपतयः after a single name is kept as printed. ऽऽ in कृकाटिकाऽऽवर्त is a print habit for कृकाटिका + "
               "आवर्त. Twenty is as printed."),
    "explain_hi": ("रचना के अनुसार पाँचवाँ भेद: सन्धि-मर्म। "
                   "गुल्फ (टखना), मणिबन्ध (कलाई), जानु (घुटना) और कूर्पर (कोहनी) मानक पहचान हैं; कुकुन्दर (नितम्ब-कटि क्षेत्र का गड्ढा) और कृकाटिका (गर्दन के पीछे का जोड़) सम्भावित; साथ में आवर्त, सीमन्त और अधिपति: ये बीस सन्धि-मर्म हैं। "
                   "अन्त का ‘अधिपतयो’ बहुवचन है, यद्यपि सूची एक नाम पर समाप्त होती है; छपा रूप रखा गया। "
                   "सन्धि: अधिपतयः + विंशति → अधिपतयो विंशति (अः + घोष व्यंजन → ओ); कृकाटिका + आवर्त → कृकाटिकावर्त (आ + आ → आ), छपाई में ‘ऽऽ’ से दिखाया गया।"),
    "hook": "सन्धि-मर्म बीस: टखना, कलाई, घुटना, कोहनी से अधिपति तक।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By the structure kinds, what are the ankle (gulpha) and the wrist (maṇibandha) in unit 58?",
            ("Joint-marmas (sandhi-marma)", "विंशति सन्धिमर्माणि: gulpha and maṇibandha open the list of joint-marmas."),
            [("Vessel-marmas (sirā-marma)", "The vessel-marmas are the forty-one of unit 55."),
             ("Sinew-marmas (snāva-marma)", "The sinew-marmas are the twenty-seven of unit 56."),
             ("Flesh-marmas (māṃsa-marma)", "The flesh-marmas are the eleven of unit 54.")],
            "Joint-marmas.",
            "गुल्फमणिबंध ... विंशति संधिमर्माणि."),
        order(1, "Put these marma names of unit 58 in the printed order.",
              ["गुल्फ", "मणिबंध", "जानु", "कूर्पर", "कुकुंदर", "सीमंत"],
              "Ankle, wrist, knee, elbow, then kukundara, (kṛkāṭikā, āvarta), sīmanta.",
              "गुल्फ → मणिबंध → जानु → कूर्पर → कुकुंदर → सीमंत."),
        match(2, "Match each word of unit 58 to its meaning.",
              [["गुल्फ", "ankle (standard)"], ["मणिबन्ध", "wrist (standard)"], ["जानु", "knee (standard)"],
               ["कूर्पर", "elbow (standard)"], ["सन्धि", "joint"], ["विंशति", "twenty"]],
              "Four of the twenty joint-marmas carry plain joint words: ankle, wrist, knee, elbow.",
              "गुल्फ, मणिबन्ध, जानु, कूर्पर, सन्धि, विंशति.", role="extend",
              teaches="सन्धिमर्म is a marma at a joint, the fifth kind by structure; four of its names are ordinary joint words."),
        mcq("discriminate", 3, "What does ऽऽ show in कृकाटिकाऽऽवर्त of unit 58?",
            ("The join of कृकाटिका and आवर्त, a print habit", "The data reads ऽऽ as the printer's mark of the आ + आ join."),
            [("A syllable lost in the damaged print", "Nothing is lost: the data reads ऽऽ as a print habit, with no flag."),
             ("A pause between two separate sentences", "The list runs on to अधिपतयो; no sentence ends there."),
             ("A doubtful reading flagged by the editor", "The data puts no flag here; it is a print habit.")],
            "कृकाटिका + आवर्त, written with ऽऽ by the printer.",
            "आ + आ → आ; ऽऽ here is a print habit."),
        multi("apply", 4, "Which statements fit unit 58?",
              [("Gulpha, the ankle, is one of the joint-marmas", "Right: गुल्फ opens the list."),
               ("Kukundara is named there as the elbow", "The elbow is kūrpara; kukundara is a different marma."),
               ("Unit 58 counts twenty-seven joint-marmas", "It counts twenty (विंशति); twenty-seven are the sinew-marmas."),
               ("The list ends on a plural, अधिपतयो, after one name", "Right: the plural is kept as printed.")],
              [0, 3],
              "Gulpha is a joint-marma; the list ends on the plural अधिपतयः; the count is twenty.",
              "गुल्फ ... अधिपतयो विंशति संधिमर्माणि."),
        mcq("transfer", 5, "By the rule of अधिपतयो विंशति, how is रामः + वदति (Rāma speaks) joined in a new example?",
            ("रामो वदति", "अः before a voiced consonant → ओ, as अधिपतयः + विंशति → अधिपतयो विंशति."),
            [("राम वदति", "After अ the visarga does not drop before a voiced consonant; that happens after आ."),
             ("रामस् वदति", "स् comes from a visarga before त or थ, not before व."),
             ("रामा वदति", "The अ does not lengthen; अः before a voiced consonant gives ओ.")],
            "रामः + वदति = रामो वदति, like अधिपतयः + विंशति.",
            "अः + voiced consonant → ओ.",
            teaches="A final अः before a voiced consonant becomes ओ: अधिपतयः + विंशति → अधिपतयो विंशति."),
    ],
}

# ---------------------------------------------------------------- unit 59
AUTHORED["59"] = {
    "title": "पुनश्च पंचधा",
    "question": "By unit 59, what opens the second fivefold division, and which parts of the line are sure?",
    "rule": ("And again in five ways (पुनश्च पञ्चधा): nineteen marmas, among them nābhi, hṛdaya, mātṛkā, śaṅkha, "
             "śṛṅgāṭaka and adhipati, take life at once (सद्यः प्राणहराणि), because they are fiery (आग्नेयत्वात्)."),
    "limits": ("Low confidence. गुदब is damaged; स्तन is doubtful; समरात्र is unknown (सप्तरात्र only possible). No "
               "question rests on these, the full list or the time. Nineteen is as printed; the data's count check "
               "reaches it only by reading the damaged start as guda and basti."),
    "explain_hi": ("‘पुनश्च पञ्चधा’ से मर्मों का दूसरा पाँच-भेद आरम्भ होता है, अब जीवन पर परिणाम के अनुसार; डेटा के निरीक्षण में पाँचों के शीर्षक इकाई ५९, ६०, ६२, ६४ और ६६ में हैं (यह विन्यास का निरीक्षण है, पंक्ति स्वयं नहीं कहती)। "
                   "पहला भेद: उन्नीस मर्म जो तत्काल (सद्यः) प्राण हरते हैं, आग्नेय यानी अग्नि-स्वभाव के होने से। "
                   "नाभि, हृदय, मातृका, शङ्ख, शृङ्गाटक और अधिपति पक्के नाम हैं; सूची का पहला शब्द ‘गुदब’ बिगड़ा है और ‘स्तन’ संदिग्ध है (अनुमान: गुदबस्ति-नाभि)। "
                   "अन्त का ‘समरात्र’ कोई ज्ञात शब्द नहीं, इसलिए उनका समय अस्पष्ट छोड़ा गया। "
                   "डेटा का विश्वास निम्न है; प्रश्न केवल पक्के भागों पर हैं।"),
    "hook": "पुनश्च पञ्चधा: उन्नीस सद्यःप्राणहर, आग्नेय होने से।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By the printed words of unit 59, what do its nineteen marmas do?",
            ("Take life at once", "सद्यः प्राणहराणि: they take life at once."),
            [("Take life after an interval", "That is the thirty-three of unit 60 (kālāntara)."),
             ("Cause impairment of a limb", "That is the forty-four of unit 64 (vaikalya)."),
             ("Become sources of pain", "That is the eight of unit 66 (rujākara).")],
            "Nineteen take life at once.",
            "एकोनविंशति सद्यः प्राणहराणि."),
        order(1, "Put these parts of unit 59 in the line's order.",
              ["पुनश्च", "पंचधा", "एकोनविंशति", "सद्यः", "प्राणहराण्याग्नेयत्वात्"],
              "Again; in five ways; nineteen; at once; life-taking, because of being fiery.",
              "पुनश्च → पंचधा → एकोनविंशति → सद्यः → प्राणहराण्याग्नेयत्वात्."),
        match(2, "Match each sure word of unit 59 to its meaning.",
              [["पुनः", "again"], ["पञ्चधा", "in five ways"], ["एकोनविंशति", "nineteen"], ["सद्यः", "at once"],
               ["आग्नेय", "fiery, of Agni"]],
              "Again in five ways: nineteen take life at once, being fiery.",
              "पुनः, पञ्चधा, एकोनविंशति, सद्यः, आग्नेय.", role="extend",
              teaches="एकोनविंशति = एक-ऊन-विंशति, 'twenty less one': nineteen."),
        mcq("discriminate", 3, "Which split of प्राणहराण्याग्नेयत्वात् in unit 59 is right?",
            ("प्राणहराणि + आग्नेयत्वात्", "इ before आ becomes य्: -हराणि + आग्नेय- → -हराण्याग्नेय-."),
            [("प्राणहराणि + अग्नेयत्वात्", "इ + short अ would give -हराण्यग्नेय-, with a short अ."),
             ("प्राणहरा + अण्याग्नेयत्वात्", "अण्याग्नेयत्वात् is not a word."),
             ("प्राणहराणे + आग्नेयत्वात्", "ए before आ would give -णयाग्नेय- or a gap, not -ण्याग्नेय-.")],
            "प्राणहराणि (life-taking) + आग्नेयत्वात् (because of being fiery).",
            "इ + आ → या."),
        mcq("apply", 4, "By unit 59, why do these marmas take life at once?",
            ("They are fiery (āgneya)", "आग्नेयत्वात्: because of their being fiery."),
            [("They are soft, cool (saumya)", "Saumya alone is the reason given in unit 64 (impairment)."),
             ("They are of Vāyu (vāyavya)", "Vāyavya is the reason given in unit 62 (viśalyaghna)."),
             ("They are saumya and āgneya", "Both together is the reason of unit 60 (after an interval).")],
            "Because they are āgneya (fiery).",
            "सद्यः प्राणहराण्याग्नेयत्वात्."),
        mcq("transfer", 5, "By the pattern of आग्नेयत्वात् (because of being fiery), what does शीतत्वात् mean in a new example?",
            ("Because of being cold", "-त्वात् is the ablative of an abstract in -त्व: because of being cold."),
            [("Coldness itself, as subject", "That would be the nominative शीतत्वम्."),
             ("For the sake of coldness", "That would be the dative शीतत्वाय."),
             ("In the state of being cold", "That would be the locative शीतत्वे.")],
            "शीतत्वात् = because of being cold, like आग्नेयत्वात् = because of being fiery.",
            "-त्वात् = because of being ...",
            teaches="-त्व makes an abstract noun ('-ness'); its ablative -त्वात् gives the reason: आग्नेयत्वात्, because of being fiery."),
    ],
}

# ---------------------------------------------------------------- unit 60
AUTHORED["60"] = {
    "title": "त्रयस्त्रिंशत्कालांतरप्राणहराणि",
    "question": "By unit 60, which marmas take life after an interval, why, and within what time?",
    "rule": ("Talahṛdaya, kṣipra, indrabasti and the rest to sīmanta: thirty-three take life after an interval "
             "(कालान्तरप्राणहराणि), being both saumya and āgneya; their time is within a fortnight (पक्षाभ्यन्तरम्)."),
    "limits": ("Verbless prose. वक्षोमर्म (chest + marma) is kept as printed: it may be a collective 'chest marmas' "
               "(the data's count check then fits thirty-three) or a lost name; left open, no question on it. "
               "Thirty-three is as printed. Unit 61 appears to continue this line."),
    "explain_hi": ("परिणाम के अनुसार दूसरा भेद: कालान्तर-प्राणहर, यानी जो कुछ समय बाद प्राण हरते हैं। "
                   "तलहृदय, क्षिप्र, इन्द्रबस्ति, वक्षोमर्म, कटीकतरुण, नितम्ब, पार्श्वसन्धि, बृहती और सीमन्त: ये तैंतीस हैं। "
                   "कारण: ये सौम्य (सोम के, कोमल-शीतल) भी हैं और आग्नेय (अग्नि के) भी; उनका समय पक्ष यानी पखवाड़े के भीतर है। "
                   "‘वक्षोमर्म’ छपे रूप में रखा गया: यह छाती के मर्मों का सामूहिक नाम हो सकता है या कोई नाम खो गया हो; बात खुली है। "
                   "सन्धि: सीमन्ताः + त्रयस्त्रिंशत् → सीमन्तास्त्रयस्त्रिंशत् (त से पहले विसर्ग → स्)। इकाई ६१ इसी पंक्ति को आगे बढ़ाती दिखती है।"),
    "hook": "सौम्य भी, आग्नेय भी: तैंतीस, पक्ष के भीतर।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "In unit 60, what does कालान्तरप्राणहर mean?",
            ("Taking life after an interval", "काल-अन्तर-प्राण-हर: taking life after an interval of time."),
            [("Taking life at once", "At once (सद्यः) is said of the nineteen of unit 59."),
             ("Killing once the dart is out", "That is viśalyaghna, unit 62."),
             ("Causing impairment of a limb", "That is vaikalyakara, unit 64.")],
            "After an interval of time.",
            "कालान्तर = after an interval."),
        order(1, "Put these marma names of unit 60 in the printed order.",
              ["तलहृदय", "क्षिप्र", "इंद्रबस्ति", "कटीकतरुण", "नितंब", "सीमंत"],
              "Talahṛdaya, kṣipra, indrabasti, (vakṣomarma), kaṭīkataruṇa, nitamba, (pārśvasandhi, bṛhatī), sīmanta.",
              "तलहृदय → क्षिप्र → इंद्रबस्ति → कटीकतरुण → नितंब → सीमंत."),
        match(2, "Match each word of unit 60 to its meaning.",
              [["काल", "time"], ["अन्तर", "interval"], ["पक्ष", "fortnight"], ["अभ्यन्तरम्", "within"],
               ["सौम्य", "of Soma, soft, cool"], ["त्रयस्त्रिंशत्", "thirty-three"]],
              "Thirty-three take life after an interval of time; their time is within a fortnight.",
              "काल, अन्तर, पक्ष, अभ्यन्तरम्, सौम्य, त्रयस्त्रिंशत्.", role="extend",
              teaches="कालान्तर = an interval of time; पक्षाभ्यन्तरम् = within a fortnight."),
        mcq("discriminate", 3, "By unit 60, why do these marmas take life after an interval?",
            ("They are saumya and āgneya both", "सौम्याग्नेयत्वात्: because of being saumya and āgneya."),
            [("They are āgneya, fiery, alone", "Āgneya alone is the reason of unit 59 (death at once)."),
             ("They are saumya, cool, alone", "Saumya alone is the reason of unit 64 (impairment)."),
             ("They are vāyavya and saumya", "Unit 60 says saumya and āgneya (सौम्याग्नेयत्वात्); vāyavya is the reason of unit 62.")],
            "Because they are both saumya and āgneya.",
            "सौम्याग्नेयत्वात् = because of being saumya and āgneya."),
        mcq("apply", 4, "By unit 60, within what time do these marmas take life?",
            ("Within a fortnight (pakṣa)", "पक्षाभ्यन्तरं कालः: the time is within a fortnight."),
            [("Within a month (māsa)", "The line says पक्ष, a fortnight, not a month."),
             ("Within a year (varṣa)", "The line says पक्ष, a fortnight, not a year."),
             ("Within a single day (dina)", "The line says पक्ष, a fortnight, not a day.")],
            "Within a fortnight.",
            "पक्षाभ्यंतरं कालः."),
        mcq("transfer", 5, "By the rule of सीमन्तास्त्रयस्त्रिंशत्, how is बालाः + तिष्ठन्ति (the boys stand) joined in a new example?",
            ("बालास्तिष्ठन्ति", "A visarga before त becomes स्, as सीमन्ताः + त्रयस्त्रिंशत् → सीमन्तास्त्रयस्त्रिंशत्."),
            [("बाला तिष्ठन्ति", "आः drops its visarga only before a voiced sound; त is not voiced."),
             ("बालाश्तिष्ठन्ति", "श् comes from a visarga before च or छ (optionally before श), not before त."),
             ("बालार्तिष्ठन्ति", "र् comes from a visarga after vowels other than अ/आ, before a voiced sound.")],
            "बालाः + तिष्ठन्ति = बालास्तिष्ठन्ति, like सीमन्ताः + त्रयस्त्रिंशत्.",
            "Visarga + त / थ → स्.",
            teaches="A visarga before त or थ becomes स्: सीमन्ताः + त्रयस्त्रिंशत् → सीमन्तास्त्रयस्त्रिंशत्."),
    ],
}

# ---------------------------------------------------------------- unit 61
AUTHORED["61"] = {
    "title": "तेष्वपि तु क्षिप्राणि",
    "question": "What does unit 61 add about the kṣipra marmas?",
    "rule": ("Even among those (the thirty-three of unit 60), however, the kṣipras: sometimes quickly (कदाचिद् आशु). "
             "The verb is not printed; by the data it is carried over from unit 60 (taking life)."),
    "limits": ("Elliptical prose: no verb is printed and none is supplied; the sense is read with unit 60 (data: "
               "GROUPING). The line does not say how often 'sometimes' is, nor how fast 'quickly' is."),
    "explain_hi": ("यह छोटी पंक्ति इकाई ६० से जुड़ी है (डेटा: GROUPING, ६० की निरन्तरता)। "
                   "उन तैंतीस में भी, किन्तु, क्षिप्र मर्म कभी-कभी (कदाचित्) शीघ्र (आशु)। "
                   "क्रिया छपी नहीं; अर्थ ‘प्राण हरना’ इकाई ६० से चला आता है, जोड़ा नहीं गया। "
                   "पंक्ति इतना ही कहती है; कितनी बार या कितनी जल्दी, यह नहीं बताती। "
                   "सन्धि: तेषु + अपि → तेष्वपि (उ + अ → व); कदाचित् + आशु → कदाचिदाशु (स्वर से पहले त् → द्)।"),
    "hook": "तेष्वपि तु क्षिप्राणि: तैंतीस में भी क्षिप्र कभी शीघ्र।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "Which marmas does unit 61 single out among those of unit 60?",
            ("Kṣipra", "तेष्वपि तु क्षिप्राणि: even among those, the kṣipras."),
            [("Sīmanta", "Sīmanta is in the list of unit 60, but unit 61 names kṣipra."),
             ("Talahṛdaya", "Talahṛdaya is in the list of unit 60, but unit 61 names kṣipra."),
             ("Indrabasti", "Indrabasti is in the list of unit 60, but unit 61 names kṣipra.")],
            "The kṣipras.",
            "तेष्वपि तु क्षिप्राणि."),
        order(1, "Put the words of unit 61 in the printed order.",
              ["तेष्वपि", "तु", "क्षिप्राणि", "कदाचिदाशु"],
              "Even among those; however; the kṣipras; sometimes quickly.",
              "तेष्वपि → तु → क्षिप्राणि → कदाचिदाशु."),
        fill(2, "Unit 61: तेष्वपि तु क्षिप्राणि कदाचिद् ____ (quickly). Type it in Devanagari or in English letters (e.g. dharma).",
             accepts("आशु", None, "ashu"),
             "आशु (quickly): कदाचित् + आशु, printed कदाचिदाशु.",
             "आशु is an indeclinable, 'quickly'; कदाचित् = sometimes.",
             "कदाचिदाशु = कदाचित् आशु."),
        mcq("discriminate", 3, "Which split of तेष्वपि in unit 61 is right?",
            ("तेषु + अपि", "उ before a different vowel becomes व्: तेषु + अपि → तेष्वपि."),
            [("तेषः + अपि", "अः before अ would give ओऽ: तेषोऽपि; and तेषः is not a form."),
             ("तेषु + वपि", "वपि is not a word; the व् comes from उ."),
             ("तेषा + अपि", "आ + अ would give तेषापि, with no व्.")],
            "तेषु (in those) + अपि (even): उ + अ → व.",
            "उ + a different vowel → व्."),
        multi("apply", 4, "Which statements fit unit 61?",
              [("A verb is printed in the line", "No verb is printed; the sense is carried from unit 60."),
               ("Kṣipra is singled out among the marmas of unit 60", "Right: तेष्वपि तु क्षिप्राणि."),
               ("Kṣipra always takes life at once", "कदाचित् means sometimes, not always."),
               ("कदाचिदाशु means sometimes, quickly", "Right: कदाचित् + आशु.")],
              [1, 3],
              "Kṣipra, among the thirty-three, sometimes quickly; no verb is printed.",
              "तेष्वपि तु क्षिप्राणि कदाचिदाशु."),
        mcq("transfer", 5, "By the rule of कदाचिदाशु (कदाचित् + आशु), how is जगत् + अपि (the world too) joined in a new example?",
            ("जगदपि", "त् before a vowel becomes द्, as कदाचित् + आशु → कदाचिदाशु."),
            [("जगन्नपि", "न् can replace त् (optionally) before a nasal consonant, not before a vowel."),
             ("जगदापि", "The अ of अपि stays short; only त् changes."),
             ("जगतेपि", "No ए arises; त् simply turns to द् before the vowel.")],
            "जगत् + अपि = जगदपि, like कदाचित् + आशु = कदाचिदाशु.",
            "त् + vowel → द्.",
            teaches="A final त् before a vowel becomes द्: कदाचित् + आशु → कदाचिदाशु, जगत् + अपि → जगदपि."),
    ],
}

# ---------------------------------------------------------------- unit 62
AUTHORED["62"] = {
    "title": "त्रीणि विशल्यघ्नानि",
    "question": "By unit 62, which marmas are viśalyaghna, and why?",
    "rule": ("The two utkṣepas and the sthapanī: three viśalyaghna marmas (killing the one freed of the dart), "
             "because of their nature of Vāyu, wind (वायव्यत्वात्). Unit 63 gives the reason."),
    "limits": ("Verbless prose. viśalyaghna is read with unit 63 as 'killing the one freed from the dart'. Unit 40 adds "
               "that an utkṣepa case may live with the dart in, or after it falls out by suppuration, but not when it "
               "is drawn out; unit 62 itself says no more."),
    "explain_hi": ("परिणाम के अनुसार तीसरा भेद: विशल्यघ्न, यानी जो शल्य निकल जाने पर मारते हैं। "
                   "दोनों उत्क्षेप और स्थपनी: ये तीन; कारण वायव्यत्वात्, यानी वायु के स्वभाव के होने से। "
                   "इसका कारण इकाई ६३ देती है: जब तक शल्य के मुख से रुका हुआ वायु ठहरता है, तब तक वह जीता है। "
                   "इकाई ४० भी कहती है कि उत्क्षेप में शल्य रहते, या पाक से शल्य गिर जाने पर, व्यक्ति जी सकता है, पर शल्य खींच निकालने पर नहीं। "
                   "‘उत्क्षेपौ’ प्रथमा द्विवचन है (दोनों उत्क्षेप); छपा ‘स्थपनीच’ = स्थपनी च।"),
    "hook": "विशल्यघ्न तीन: दो उत्क्षेप, एक स्थपनी, वायु के कारण।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 62, what does विशल्यघ्न say of these marmas?",
            ("They kill the one freed of the dart", "वि-शल्य-घ्न: killing the one who is freed of the dart."),
            [("They kill at once, with or without a dart", "Killing at once is said of the nineteen of unit 59."),
             ("They cause pain and nothing more", "Sources of pain are the eight of unit 66."),
             ("They cause impairment of a limb", "Impairment is said of the forty-four of unit 64.")],
            "Killing the one freed of the dart.",
            "विशल्यघ्नानि."),
        order(1, "Put the words of unit 62 in the printed order.",
              ["उत्क्षेपौ", "स्थपनीच", "त्रीणि", "विशल्यघ्नानि", "वायव्यत्वात्"],
              "The two utkṣepas; and the sthapanī; three; viśalyaghna; because of their Vāyu nature.",
              "उत्क्षेपौ → स्थपनीच → त्रीणि → विशल्यघ्नानि → वायव्यत्वात्."),
        match(2, "Match each word of unit 62 to its meaning.",
              [["उत्क्षेपौ", "the two utkṣepas"], ["त्रीणि", "three"], ["विशल्य", "freed from the dart"],
               ["घ्न", "killing"], ["वायव्य", "of Vāyu (wind)"]],
              "Two utkṣepas and the sthapanī: three that kill the one freed from the dart, being of Vāyu.",
              "उत्क्षेपौ, त्रीणि, विशल्य, घ्न, वायव्य.", role="extend",
              teaches="विशल्यघ्न: वि-शल्य = without the dart; -घ्न = killing (from √हन्)."),
        mcq("discriminate", 3, "Which reason does unit 62 give for the three viśalyaghna marmas?",
            ("Their nature of Vāyu (vāyavya)", "वायव्यत्वात्: because of being of Vāyu."),
            [("Their fiery nature (āgneya)", "Āgneya is the reason of unit 59 (death at once)."),
             ("Their soft, cool nature (saumya)", "Saumya is the reason of unit 64 (impairment)."),
             ("Abundance of all three (bāhulya)", "Abundance of Agni, Vāyu and Soma is the reason of unit 66 (pain).")],
            "Because they are of Vāyu.",
            "विशल्यघ्नानि वायव्यत्वात्."),
        mcq("apply", 4, "Which marmas does unit 62 call viśalyaghna?",
            ("The two utkṣepas and the sthapanī", "उत्क्षेपौ स्थपनी च त्रीणि."),
            [("The two śaṅkhas and the adhipati", "Both are printed among the nineteen of unit 59."),
             ("The two apāṅgas and the sthapanī", "Apāṅga is among the forty-four of unit 64."),
             ("The two utkṣepas and the adhipati", "Adhipati is among the nineteen of unit 59.")],
            "Two utkṣepas and one sthapanī: three.",
            "उत्क्षेपौ स्थपनीच त्रीणि."),
        mcq("transfer", 5, "By the pattern of उत्क्षेपौ (the two utkṣepas, m.), which form names the two hands (हस्त, m.) in a new example?",
            ("हस्तौ", "Masculine a-stems take -औ in the nominative dual, as उत्क्षेप → उत्क्षेपौ."),
            [("हस्ताः", "-आः is the nominative plural: more than two hands."),
             ("हस्तः", "-अः is the nominative singular: one hand."),
             ("हस्ते", "For a masculine a-stem, -ए is the locative singular: in the hand.")],
            "हस्तौ = the two hands, like उत्क्षेपौ = the two utkṣepas.",
            "Masculine a-stem, nominative dual: -औ.",
            teaches="Masculine a-stems form the nominative dual in -औ: उत्क्षेप → उत्क्षेपौ (the two utkṣepas)."),
    ],
}

# ---------------------------------------------------------------- unit 63
AUTHORED["63"] = {
    "title": "यावदत्र वायुस्तिष्ठति",
    "question": "By unit 63, how does the line explain viśalyaghna?",
    "rule": ("For (हि) as long as Vāyu, wind, blocked at the mouth of the dart, stays here, so long he lives "
             "(यावत् ... तावत् जीवति). This gives the reason for unit 62's viśalyaghna."),
    "limits": ("Prose. अवरुद्धः is taken with Vāyu (the plainer reading); it could instead describe the person "
               "('blocked by the dart's mouth'), so no question rests on what it qualifies. The subject of जीवति is not "
               "printed. The line does not itself say what happens when the dart is drawn out."),
    "explain_hi": ("यह इकाई ६२ के ‘विशल्यघ्न’ का कारण देती है (‘हि’ = क्योंकि)। "
                   "जब तक यहाँ शल्य के मुख से रुका हुआ वायु ठहरता है, तब तक वह जीता है। "
                   "‘शल्यमुखावरुद्धः’ को वायु का विशेषण माना गया, जो सरल पाठ है; इसे व्यक्ति का विशेषण भी पढ़ा जा सकता है, इसलिए इस पर प्रश्न नहीं। "
                   "‘जीवति’ का कर्ता छपा नहीं। यावत् ... तावत् = जब तक ... तब तक। "
                   "सन्धि: तावत् + जीवति → तावज्जीवति (त् + ज → ज्ज); यावत् + अत्र → यावदत्र (स्वर से पहले त् → द्); वायुः + तिष्ठति → वायुस्तिष्ठति (त से पहले विसर्ग → स्)।"),
    "hook": "यावद् वायु रुका, तावद् जीवन।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 63, as long as what stays here does he live?",
            ("Vāyu (wind)", "यावदत्र वायुस्तिष्ठति तावज्जीवति: as long as Vāyu stays."),
            [("Blood (śoṇita)", "Blood is not named in unit 63."),
             ("Soma (the moon-principle)", "Soma is named in unit 65, not in unit 63."),
             ("Agni (fire)", "Agni is not named in unit 63.")],
            "As long as Vāyu stays here.",
            "यावत् वायुः तिष्ठति तावत् जीवति."),
        order(1, "Put the parts of unit 63 in the printed order.",
              ["शल्यमुखावरुद्धो हि", "यावदत्र", "वायुस्तिष्ठति", "तावज्जीवति"],
              "Blocked at the dart's mouth, for; as long as here; Vāyu stays; so long he lives.",
              "शल्यमुखावरुद्धो हि → यावदत्र → वायुस्तिष्ठति → तावज्जीवति."),
        match(2, "Match each word of unit 63 to its meaning.",
              [["शल्य", "dart"], ["मुख", "mouth"], ["यावत्", "as long as"], ["तावत्", "so long"],
               ["तिष्ठति", "stays"], ["जीवति", "lives"]],
              "As long as Vāyu, blocked at the dart's mouth, stays, so long he lives.",
              "शल्य, मुख, यावत्, तावत्, तिष्ठति, जीवति.", role="extend",
              teaches="यावत् ... तावत् pair up: as long as ... so long."),
        mcq("discriminate", 3, "Which split of तावज्जीवति in unit 63 is right?",
            ("तावत् + जीवति", "त् before ज becomes ज्: तावत् + जीवति → तावज्जीवति."),
            [("ताव + ज्जीवति", "ज्जीवति is not a word; the first ज् comes from त्."),
             ("तावत् + अजीवति", "That would join as तावदजीवति."),
             ("तावः + जीवति", "अः before a voiced consonant would give तावो जीवति.")],
            "तावत् (so long) + जीवति (lives): त् + ज → ज्ज.",
            "त् + ज → ज्ज."),
        mcq("apply", 4, "What does हि do in unit 63?",
            ("It gives the reason for unit 62", "हि = for: the line explains why these marmas are viśalyaghna."),
            [("It turns the line into a question", "हि does not ask; it means 'for, indeed'."),
             ("It negates the verb जीवति", "Negation would need न; हि means 'for'."),
             ("It closes the list of unit 62", "The list ended in unit 62; हि opens a reason.")],
            "हि = for: a reason follows.",
            "हि = for, indeed."),
        mcq("transfer", 5, "By the rule of तावज्जीवति (तावत् + जीवति), how is सत् + जनः (a good person) joined in a new example?",
            ("सज्जनः", "त् before ज becomes ज्, as तावत् + जीवति → तावज्जीवति."),
            [("सत्जनः", "त् cannot stay unchanged before the voiced ज."),
             ("सच्जनः", "च् comes before the voiceless palatals (च, छ, श), not before the voiced ज."),
             ("सञ्जनः", "ञ् is a nasal; त् does not become a nasal before ज.")],
            "सत् + जनः = सज्जनः, like तावत् + जीवति = तावज्जीवति.",
            "त् + ज → ज्ज.",
            teaches="A final त् before ज becomes ज्: तावत् + जीवति → तावज्जीवति, सत् + जनः → सज्जनः."),
    ],
}

# ---------------------------------------------------------------- unit 64
AUTHORED["64"] = {
    "title": "चतुश्चत्वारिंशद्वैकल्यकराणि",
    "question": "By unit 64, which marmas cause impairment (vaikalya), and why?",
    "rule": ("Kūrca, jānu, kūrpara, urvī, viṭapa, phaṇa, apāṅga and others: forty-four marmas cause impairment "
             "(वैकल्यकराणि), because they are saumya, soft, of Soma (सौम्यत्वात्)."),
    "limits": ("Verbless list. Printed मन्द्या is manyā only by conjecture; कूर्पराणि is read kūrpara + āṇi; the printed "
               "names give 42, so forty-four is open (data's count check). No modern equivalent of vaikalya is stated. "
               "No question rests on manyā, āṇi, āvarta (printed आवार्त) or the count."),
    "explain_hi": ("परिणाम के अनुसार चौथा भेद: वैकल्यकर, यानी अंग या इन्द्रिय में वैकल्य (अपूर्णता) करने वाले। "
                   "कूर्च, जानु, कूर्पर, आणि, उर्वी, लोहिताख्य, विटप, कक्षाधर, कुकुन्दर, अंसफलक, नीला, मन्या (अनुमानित पाठ), कृकाटिका, विधुर, फण, अपाङ्ग और आवर्त: ये चवालीस हैं, सौम्य होने से। "
                   "वैकल्य का कोई आधुनिक समतुल्य (विकृति या अक्षमता) पाठ में नहीं कहा गया। "
                   "डेटा के गणना-निरीक्षण में छपे नाम ४२ देते हैं; ४४ के लिए ‘अंस’ भी चाहिए, जो छपा नहीं, इसलिए यह बात खुली है। "
                   "सन्धि: चतुश्चत्वारिंशत् + वैकल्य → चतुश्चत्वारिंशद्वैकल्य (घोष व्यंजन से पहले त् → द्)।"),
    "hook": "सौम्य होने से चवालीस वैकल्यकर।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 64, what do the marmas of its list cause?",
            ("Impairment (vaikalya)", "वैकल्यकराणि: they cause impairment."),
            [("Death at once (sadyaḥ)", "Death at once is said of the nineteen of unit 59."),
             ("Pain (ruj)", "Pain is said of the eight of unit 66."),
             ("Death after an interval (kālāntara)", "That is said of the thirty-three of unit 60.")],
            "Impairment.",
            "चतुश्चत्वारिंशद्वैकल्यकराणि."),
        order(1, "Put these marma names of unit 64 in the printed order.",
              ["कूर्च्च", "जानु", "उर्वी", "विटप", "कुकुंदर", "अंसफलक"],
              "Kūrca, jānu, (kūrpara, āṇi), urvī, (lohitākhya), viṭapa, (kakṣādhara), kukundara, aṃsaphalaka ...",
              "कूर्च्च → जानु → उर्वी → विटप → कुकुंदर → अंसफलक."),
        match(2, "Match each word of unit 64 to its meaning.",
              [["वैकल्य", "impairment"], ["कर", "causing"], ["सौम्य", "soft, of Soma"],
               ["कूर्पर", "elbow (standard)"]],
              "These cause impairment, because they are saumya; kūrpara is also the ordinary word for elbow.",
              "वैकल्य, कर, सौम्य, कूर्पर.", role="extend",
              teaches="वैकल्यकर = वैकल्य (impairment) + -कर (causing); सौम्यत्वात् = because of being saumya."),
        mcq("discriminate", 3, "Which split of चतुश्चत्वारिंशद्वैकल्यकराणि in unit 64 is right?",
            ("चतुश्चत्वारिंशत् + वैकल्यकराणि", "त् before the voiced व becomes द्: -शत् + वैकल्य- → -शद्वैकल्य-."),
            [("चतुश्चत्वारिंश + द्वैकल्यकराणि", "द्वैकल्य is not a word; the द् comes from त्."),
             ("चतुश्चत्वारिंशः + वैकल्यकराणि", "अः before a voiced consonant would give -शो वैकल्य-."),
             ("चतुश्चत्वारिंशति + वैकल्यकराणि", "That would stay -शति वैकल्य-, with no द्.")],
            "चतुश्चत्वारिंशत् (forty-four) + वैकल्यकराणि (causing impairment).",
            "त् + voiced consonant → द्."),
        multi("apply", 4, "Which are named in unit 64 among the marmas that cause impairment?",
              [("Nābhi", "Nābhi is among the nineteen that kill at once (unit 59)."),
               ("Jānu", "Right: जानु is in the list."),
               ("Śaṅkha", "Śaṅkha is printed among the nineteen of unit 59."),
               ("Viṭapa", "Right: विटप is in the list."),
               ("Apāṅga", "Right: अपाङ्ग is in the list.")],
              [1, 3, 4],
              "Jānu, viṭapa and apāṅga cause impairment; nābhi and śaṅkha are among the nineteen of unit 59.",
              "कूर्च्चजानु ... फणापांगावार्ताश्चतुश्चत्वारिंशद्वैकल्यकराणि."),
        mcq("transfer", 5, "By the rule of चतुश्चत्वारिंशद्वैकल्य-, how is महत् + वनम् (a great forest) joined in a new example?",
            ("महद्वनम्", "त् before a voiced consonant becomes द्, as -शत् + वैकल्य- → -शद्वैकल्य-."),
            [("महत्वनम्", "त् cannot stay unchanged before the voiced व."),
             ("महन्वनम्", "न् can replace त् (optionally) only before a nasal consonant; व is not one."),
             ("महव्वनम्", "त् does not copy the व.")],
            "महत् + वनम् = महद्वनम्, like चतुश्चत्वारिंशत् + वैकल्य-.",
            "त् + voiced consonant → द्.",
            teaches="A final त् before a voiced consonant such as व becomes द्: चतुश्चत्वारिंशत् + वैकल्यकराणि → चतुश्चत्वारिंशद्वैकल्यकराणि."),
    ],
}

# ---------------------------------------------------------------- unit 65
AUTHORED["65"] = {
    "title": "सोमो हि स्थैर्यशैत्याभ्यां",
    "question": "By unit 65, how does Soma sustain the life-breaths, and what is said of 'those' marmas?",
    "rule": ("For Soma sustains the life-breaths (प्राणान् धारयति) by steadiness and coolness (स्थैर्य-शैत्य). And "
             "those too (the saumya marmas of unit 64), when struck, sometimes (कदाचित्) kill (मारयन्ति)."),
    "limits": ("Two printed lines. Soma is glossed the moon-principle, cool and steady; no more is claimed. 'Those' "
               "(तानि) is the data's reading for the saumya marmas of unit 64. The person killed is not printed. "
               "Printed तान्यापि is kept as printed (the usual join of तानि + अपि would be तान्यपि)."),
    "explain_hi": ("पहली पंक्ति: क्योंकि सोम स्थिरता (स्थैर्य) और शीतलता (शैत्य) से प्राणों को धारण करता है; यह इकाई ६४ के ‘सौम्यत्वात्’ से जुड़ता है। "
                   "दूसरी पंक्ति: और वे भी (तानि, डेटा के अनुसार इकाई ६४ के सौम्य मर्म) कभी-कभी आहत होने पर मार देते हैं; किसे, यह छपा नहीं। "
                   "‘धारयति’ णिजन्त रूप है, पर अर्थ सीधा ‘धारण करता है’; ‘मारयन्ति’ √मृ का णिजन्त है: मरवाते, यानी मार देते हैं। "
                   "छपा ‘तान्यापि’ रखा गया; तानि + अपि की सामान्य सन्धि तान्यपि होती। "
                   "सन्धि: सोमः + हि → सोमो हि (अः + घोष व्यंजन → ओ)।"),
    "hook": "सोम: स्थिर और शीतल, प्राणों को थामे।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 65, by which two qualities does Soma sustain the life-breaths?",
            ("Steadiness and coolness", "स्थैर्यशैत्याभ्यां: by steadiness and coolness."),
            [("Heat and sharpness", "Unit 65 names steadiness and coolness, not heat."),
             ("Lightness and swift motion", "Unit 65 names steadiness and coolness, not motion."),
             ("Dryness and roughness", "Unit 65 names steadiness and coolness, not dryness.")],
            "Steadiness and coolness.",
            "सोमो हि स्थैर्यशैत्याभ्यां प्राणान्धारयति."),
        order(1, "Put the parts of unit 65 in the printed order.",
              ["सोमो हि", "स्थैर्यशैत्याभ्यां", "प्राणान्धारयति", "तान्यापि च", "कदाचिदभिहतानि", "मारयंति"],
              "For Soma; by steadiness and coolness; sustains the life-breaths; and those too; sometimes, when struck; kill.",
              "सोमो हि → स्थैर्यशैत्याभ्यां → प्राणान्धारयति → तान्यापि च → कदाचिदभिहतानि → मारयंति."),
        match(2, "Match each word of unit 65 to its meaning.",
              [["स्थैर्य", "steadiness"], ["शैत्य", "coolness"], ["प्राणान्", "the life-breaths (prāṇa)"],
               ["धारयति", "sustains, holds"], ["अभिहत", "struck"], ["मारयन्ति", "kill"]],
              "Soma holds the prāṇas by steadiness and coolness; those, when struck, sometimes kill.",
              "स्थैर्य, शैत्य, प्राणान्, धारयति, अभिहत, मारयन्ति.", role="extend",
              teaches="स्थैर्य (from स्थिर) and शैत्य (from शीत) are abstract nouns: steadiness, coolness."),
        mcq("discriminate", 3, "Which split of प्राणान्धारयति in unit 65 is right?",
            ("प्राणान् + धारयति", "न् stays before ध: प्राणान् (acc. pl.) + धारयति."),
            [("प्राणाः + धारयति", "आः drops its visarga before a voiced sound: प्राणा धारयति, with no न्."),
             ("प्राण + अन्धारयति", "अन्धारयति is not a word."),
             ("प्राणा + न्धारयति", "न्धारयति is not a word.")],
            "प्राणान् (the life-breaths) + धारयति (sustains).",
            "Final न् before ध is unchanged."),
        mcq("apply", 4, "By unit 65, when do 'those' marmas kill?",
            ("Sometimes, when struck", "कदाचिदभिहतानि मारयन्ति: sometimes, when struck, they kill."),
            [("Always, when struck", "कदाचित् means sometimes, not always."),
             ("Only when the dart is drawn out", "That is viśalyaghna, said of the three of unit 62."),
             ("Never; they only cause pain", "The line says they kill (मारयन्ति).")],
            "Sometimes, when struck.",
            "कदाचित् = sometimes; अभिहत = struck."),
        mcq("transfer", 5, "By the pattern of मारयन्ति (cause to die, from √मृ), what does पाठयति (from √पठ्) mean in a new example?",
            ("Causes to read, teaches", "Here पाठ- + -अयति, with the lengthened आ, is the causative of √पठ्: causes to read."),
            [("Reads, by itself", "That would be the plain present पठति."),
             ("Is being read", "That would be the passive पठ्यते."),
             ("Will read later", "That would be the future पठिष्यति.")],
            "पाठयति = causes to read, like मारयन्ति = cause to die.",
            "Causative: -अयति = cause to ...",
            teaches="The causative stem in -अय- means 'cause to do': √मृ → मारयति, √पठ् → पाठयति. Some keep a plain sense, as धारयति (holds)."),
    ],
}

# ---------------------------------------------------------------- unit 66
AUTHORED["66"] = {
    "title": "कूर्च्चशिरोगुल्फमणिबंधास्त्वष्टौ",
    "question": "By unit 66, which marmas are sources of pain (rujākara), and why?",
    "rule": ("Kūrcaśiras, gulpha (ankle) and maṇibandha (wrist), however: eight sources of pain (रुजाकराणि), because of "
             "an abundance of the qualities of Agni, Vāyu and Soma (अग्निवायुसोमगुणबाहुल्यात्)."),
    "limits": ("Verbless prose. Eight is as printed. ākara means mine, source; the line names only pain as their result. "
               "Gulpha and maṇibandha keep their standard senses. Unit 67 explains the reason further."),
    "explain_hi": ("परिणाम के अनुसार पाँचवाँ भेद: रुजाकर, यानी पीड़ा के स्रोत (आकर = खान, स्रोत)। "
                   "कूर्चशिरस्, गुल्फ (टखना) और मणिबन्ध (कलाई): ये आठ हैं। "
                   "कारण: अग्नि, वायु और सोम, तीनों के गुणों की अधिकता (बाहुल्य)। "
                   "इकाई ६७ आगे कहती है कि अग्नि और वायु विशेष रूप से पीड़ा के स्रोत हैं। "
                   "सन्धि: मणिबन्धाः + तु → मणिबन्धास्तु (त से पहले विसर्ग → स्); तु + अष्टौ → त्वष्टौ (उ + अ → व); रुजाकराणि + अग्नि → रुजाकराण्यग्नि (इ + अ → य)।"),
    "hook": "कूर्चशिर, गुल्फ, मणिबन्ध: आठ पीड़ा के आकर।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 66, what are kūrcaśiras, gulpha and maṇibandha called?",
            ("Sources of pain (rujākara)", "रुजाकराणि: sources of pain."),
            [("Causes of impairment (vaikalyakara)", "Impairment is said of the forty-four of unit 64."),
             ("Takers of life at once (sadyaḥprāṇahara)", "That is said of the nineteen of unit 59."),
             ("Killers once the dart is out (viśalyaghna)", "That is said of the three of unit 62.")],
            "Sources of pain.",
            "रुजाकराणि."),
        order(1, "Put these words of unit 66 in the printed order (shown unjoined).",
              ["कूर्चशिरः", "गुल्फ", "मणिबन्ध", "अष्टौ", "रुजाकराणि", "बाहुल्यात्"],
              "Kūrcaśiras, gulpha, maṇibandha; eight; sources of pain; because of abundance (of the three qualities).",
              "कूर्चशिरः → गुल्फ → मणिबन्ध → अष्टौ → रुजाकराणि → बाहुल्यात्."),
        match(2, "Match each word of unit 66 to its meaning.",
              [["गुल्फ", "ankle (standard)"], ["मणिबन्ध", "wrist (standard)"], ["रुज्", "pain"],
               ["आकर", "mine, source"], ["बाहुल्य", "abundance"], ["अष्टौ", "eight"]],
              "Eight sources of pain, from an abundance of the three qualities.",
              "गुल्फ, मणिबन्ध, रुज्, आकर, बाहुल्य, अष्टौ.", role="extend",
              teaches="रुजाकर = रुज् (pain) + आकर (mine, source): a source of pain."),
        mcq("discriminate", 3, "By unit 66, why are these eight sources of pain?",
            ("Abundant qualities of Agni, Vāyu and Soma", "अग्निवायुसोमगुणबाहुल्यात्: all three, in abundance."),
            [("Abundant qualities of Soma alone, the cool one", "Soma alone (saumya) is the reason of unit 64."),
             ("Abundant qualities of Agni alone, the fiery one", "Agni alone (āgneya) is the reason of unit 59."),
             ("Abundant qualities of Soma and Vāyu", "Unit 66 names Agni as well: अग्निवायुसोमगुणबाहुल्यात्.")],
            "Because of an abundance of the qualities of Agni, Vāyu and Soma.",
            "अग्निवायुसोमगुणबाहुल्यात्."),
        mcq("apply", 4, "In the division by outcome (units 59 to 66), which class does the wrist marma (maṇibandha) belong to?",
            ("Rujākara, a source of pain", "मणिबन्ध is among the eight rujākara of unit 66."),
            [("Vaikalyakara, causing impairment", "Maṇibandha is not in the list of unit 64."),
             ("Viśalyaghna, killing when freed", "The viśalyaghna are the utkṣepas and sthapanī (unit 62)."),
             ("Sadyaḥprāṇahara, killing at once", "Maṇibandha is not among the nineteen of unit 59.")],
            "Maṇibandha is rujākara.",
            "कूर्च्चशिरोगुल्फमणिबंधास्त्वष्टौ रुजाकराणि."),
        mcq("transfer", 5, "By the rule of त्वष्टौ (तु + अष्टौ), how is मधु + अत्र (honey here) joined in a new example?",
            ("मध्वत्र", "उ before a different vowel becomes व्, as तु + अष्टौ → त्वष्टौ."),
            [("मधत्र", "The उ cannot simply drop before अ."),
             ("मधोत्र", "ओ comes from अ + उ, not from उ + अ."),
             ("मध्वात्र", "A long आ would need उ + आ; अत्र begins with a short अ.")],
            "मधु + अत्र = मध्वत्र, like तु + अष्टौ = त्वष्टौ.",
            "उ + a different vowel → व्.",
            teaches="A final उ before a different vowel becomes व्: तु + अष्टौ → त्वष्टौ, मधु + अत्र → मध्वत्र."),
    ],
}

# ---------------------------------------------------------------- unit 67
AUTHORED["67"] = {
    "title": "अग्निवायू हि विशेषेण रुजाकरौ",
    "question": "By unit 67, which two are especially the sources of pain?",
    "rule": ("For Agni and Vāyu (fire and wind) are especially (विशेषेण) the two sources of pain (रुजाकरौ). This "
             "explains unit 66."),
    "limits": ("Verbless prose; हि = for. 'Especially' (विशेषेण) does not say that Soma causes no pain; unit 66 names all "
               "three. No verb is supplied."),
    "explain_hi": ("यह इकाई ६६ का कारण स्पष्ट करती है (‘हि’ = क्योंकि)। "
                   "अग्नि और वायु विशेष रूप से (विशेषेण) पीड़ा के दो स्रोत हैं। "
                   "‘विशेषेण’ का अर्थ ‘केवल’ नहीं: इकाई ६६ तीनों, अग्नि, वायु और सोम, के गुणों की अधिकता को कारण कहती है। "
                   "‘अग्निवायू’ दो का द्वन्द्व समास है, इसलिए प्रथमा द्विवचन; ‘रुजाकरौ’ भी द्विवचन है और उसी से मेल खाता है। "
                   "पंक्ति में क्रिया नहीं छपी।"),
    "hook": "अग्नि और वायु: पीड़ा के दो विशेष आकर।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 67, which two are especially the sources of pain?",
            ("Agni and Vāyu", "अग्निवायू हि विशेषेण रुजाकरौ."),
            [("Soma and Vāyu", "Soma is not named in unit 67."),
             ("Agni and Soma", "Soma is not named in unit 67."),
             ("Agni and Prāṇa", "Prāṇa is not named in unit 67.")],
            "Agni and Vāyu.",
            "अग्निवायू ... रुजाकरौ."),
        order(1, "Put the words of unit 67 in the printed order.",
              ["अग्निवायू", "हि", "विशेषेण", "रुजाकरौ"],
              "Agni and Vāyu; for; especially; the two sources of pain.",
              "अग्निवायू → हि → विशेषेण → रुजाकरौ."),
        match(2, "Match each word of unit 67 to its meaning.",
              [["अग्नि", "fire (Agni)"], ["वायु", "wind (Vāyu)"], ["विशेषेण", "especially"], ["हि", "for, indeed"],
               ["रुजाकरौ", "the two sources of pain"]],
              "For Agni and Vāyu are especially the two sources of pain.",
              "अग्नि, वायु, विशेषेण, हि, रुजाकरौ.", role="extend",
              teaches="विशेषेण works as an adverb (gram: ind.): especially."),
        mcq("discriminate", 3, "Why does अग्निवायू in unit 67 end in ऊ?",
            ("Dual of a dvandva naming two", "अग्नि + वायु, two things: nominative dual, वायु → वायू."),
            [("Plural of a dvandva naming many", "The plural would be अग्निवायवः."),
             ("A feminine ending put on वायु", "वायु is masculine; the ऊ here is the dual."),
             ("A locative ending: in fire and wind", "The locative dual would be अग्निवाय्वोः.")],
            "अग्निवायू: nominative dual of a dvandva of two.",
            "Dvandva of two → dual: -उ stem → -ऊ."),
        multi("apply", 4, "Which statements fit unit 67?",
              [("It says Soma causes no pain at all", "It says nothing of Soma; unit 66 names Soma too."),
               ("It gives a reason for unit 66 (हि = for)", "Right: हि introduces the reason."),
               ("रुजाकरौ is dual, agreeing with अग्निवायू", "Right: both are dual."),
               ("It names Agni and Vāyu as the only sources", "विशेषेण means especially, not only.")],
              [1, 2],
              "हि gives the reason for unit 66; अग्निवायू and रुजाकरौ are both dual; 'especially' is not 'only'.",
              "अग्निवायू हि विशेषेण रुजाकरौ."),
        mcq("transfer", 5, "By the pattern of अग्निवायू (Agni and Vāyu, two), which form names Indra and Vāyu together (two) in a new example?",
            ("इन्द्रवायू", "A dvandva of two takes the nominative dual: final -उ → -ऊ, as अग्निवायू."),
            [("इन्द्रवायवः", "-अवः is the nominative plural: more than two."),
             ("इन्द्रवायौ", "-औ on a u-stem is the locative singular here."),
             ("इन्द्रवायुम्", "-उम् is the accusative singular.")],
            "इन्द्रवायू = Indra and Vāyu (two), like अग्निवायू.",
            "Dvandva of two, u-stem final: nominative dual -ऊ.",
            teaches="A dvandva naming two takes the dual; a final u-stem gives -ऊ in the nominative dual: अग्नि + वायु → अग्निवायू."),
    ],
}


# ================================================================= NOTES_HI
NOTES_HI = {
    "55": ("गद्य; विश्वास मध्यम; दो पाठ-चिह्न। (१) छपा ‘नीलामन्मामातृका’: ‘मन्मा’ कोई मर्म-नाम नहीं; अनुमान से ‘मन्या’ (गर्दन का मर्म), "
           "य → न्म छपाई की भूल सम्भव (इकाई ६४ का ‘मन्द्या’ भी देखें); अनुवाद में अनुमानित पाठ कहकर रखा गया। (२) छपा ‘अपस्तंभालाप’: "
           "‘अलाप’ सम्भवतः अपालाप (इकाई २६ में ‘अपालापौ’ छपा), एक ‘पा’ लुप्त; विभाजन में छपा रूप रखा, अनुवाद में नहीं अपनाया। "
           "छपाई ‘स्तन मूल’ में समास के बीच अन्तर (स्तनमूल); छपा ‘शिरा’ = सिरा। गणना-निरीक्षण (डेटा का): पक्षों और अंगों को गिनकर ४१ बैठता है, छपा नहीं। "
           "सन्धि जाँची: मूल + अपस्तम्भ → मूलापस्तम्भ, फण + अपाङ्ग → फणापाङ्ग (अ + अ → आ); शृङ्गाटकानि + एकचत्वारिंशत् → "
           "शृङ्गाटकान्येकचत्वारिंशत् (इ + भिन्न स्वर → य्); एकचत्वारिंशत् + शिरा → एकचत्वारिंशच्छिरा (त् + श → च्श, स्वर से पहले वैकल्पिक च्छ; छपा च्छ)।"),
    "56": ("गद्य; विश्वास मध्यम; कोई पाठ-चिह्न नहीं। पूरी सूची एक छपे शब्द-समूह में; एक द्वन्द्व-सूची पढ़ी गई। ‘कक्षाधराणि’ = कक्षाधर + आणि "
           "(इकाई ११ का मर्म), नपुंसक बहुवचन नहीं: डेटा का पाठ, जिससे २७ की गिनती बैठती है (गणना छपी नहीं)। स्नाव = स्नायु। "
           "बस्ति (मूत्राशय) और अंस (कन्धा) मानक अर्थ। सन्धि जाँची: कूर्चशिरः + विटप → कूर्चशिरोविटप (अः + घोष व्यंजन → ओ); "
           "कक्षाधर + आणि → कक्षाधराणि (अ + आ → आ); बस्ति + अंस → बस्त्यंस (इ + अ → य); विधुर + उत्क्षेपाः → विधुरोत्क्षेपाः (अ + उ → ओ)।"),
    "57": ("गद्य; विश्वास मध्यम; कोई पाठ-चिह्न नहीं। एक छपा शब्द-समूह, क्रियाहीन सूची। ‘तु’ पिछली सूची से हल्का भेद। पहचानें: अंसफलक "
           "(कन्धे की चपटी हड्डी) और शङ्ख (कनपटी) सम्भावित; नितम्ब मानक शब्दार्थ। सन्धि जाँची: कटीकतरुण + नितम्ब (कोई परिवर्तन नहीं); "
           "नितम्ब + अंसफलक → नितम्बांसफलक (अ + अ → आ); शङ्खाः + तु → शङ्खास्तु (त से पहले विसर्ग → स्); तु + अष्टौ → त्वष्टौ (उ + अ → व); "
           "अष्टौ + अस्थि → अष्टावस्थि (औ + स्वर → आव्)।"),
    "58": ("गद्य; विश्वास मध्यम; कोई पाठ-चिह्न नहीं। ‘कृकाटिकाऽऽवर्त’ का दोहरा अवग्रह छपाई की आदत (कृकाटिका + आवर्त, आ + आ → आ)। "
           "‘अधिपतयो’ बहुवचन है, यद्यपि सूची एक नाम पर समाप्त; छपा रूप रखा। पहचानें: गुल्फ, मणिबन्ध, जानु, कूर्पर मानक; कुकुन्दर, "
           "कृकाटिका सम्भावित। सन्धि जाँची: अधिपतयः + विंशति → अधिपतयो विंशति (अः + घोष व्यंजन → ओ); सीमन्त + अधिपतयः → "
           "सीमन्ताधिपतयः (अ + अ → आ)।"),
    "59": ("गद्य; विश्वास निम्न; दो पाठ-चिह्न। (१) ‘गुदब’ कोई शब्द नहीं; सम्भवतः ‘गुदब स्तनाभि’ = गुदबस्तिनाभि (एक मात्रा लुप्त), तब "
           "‘स्तन’ मर्म नहीं; अनुवाद में नहीं अपनाया, ‘गुदब’ अपठनीय छोड़ा गया। (२) ‘समरात्र’ ज्ञात शब्द नहीं; प्त/म की भूल से सप्तरात्र (सात रातें) "
           "सम्भव, कोई अर्थ नहीं अपनाया। संख्या ‘उन्नीस’ छपे अनुसार; डेटा के गणना-निरीक्षण में गुद १ (इकाई १८), बस्ति १ (इकाई १९), नाभि १ "
           "(इकाई २१), हृदय १ (इकाई २२), मातृका ८ (इकाई ३५), शङ्ख २ (इकाई ३९), शृङ्गाटक ४ (इकाई ४३), अधिपति १ (इकाई ४४) = १९। "
           "सन्धि जाँची: पुनः + च → पुनश्च (च से पहले विसर्ग → श्); प्राणहराणि + आग्नेयत्वात् → प्राणहराण्याग्नेयत्वात् (इ + आ → या); "
           "छपाई ‘अधिपतयएकोनविंशति’ में विसर्ग के लोप के बाद अन्तर नहीं छोड़ा गया।"),
    "60": ("गद्य; विश्वास मध्यम; एक पाठ-चिह्न: ‘वक्षोमर्म’ नाम-सूची में अटपटा, कोई नाम खोया हो या ‘मर्म’ फालतू हो; कोई सुधार नहीं अपनाया। "
           "डेटा के गणना-निरीक्षण में नामित मर्म २५ देते हैं और इकाई २३ से २६ के छाती-मर्म (स्तनमूल, स्तनरोहित, अपस्तम्भ, अपालाप, दो-दो) ८, "
           "कुल ३३: इसलिए ‘वक्षोमर्म’ ‘छाती के मर्म’ का सामूहिक नाम भी हो सकता है; बात खुली। छपाई सूची को ‘नितंब’ / ‘पार्श्वसंधि’ पर दो भागों में "
           "तोड़ती है। सन्धि जाँची: क्षिप्र + इन्द्रबस्ति → क्षिप्रेन्द्रबस्ति (अ + इ → ए); सीमन्ताः + त्रयस्त्रिंशत् → सीमन्तास्त्रयस्त्रिंशत् (त से पहले "
           "विसर्ग → स्); सौम्याग्नेयत्वात् + तेषाम् → सौम्याग्नेयत्वात्तेषां; पक्ष + अभ्यन्तरम् → पक्षाभ्यन्तरम् (अ + अ → आ)।"),
    "61": ("गद्य; विश्वास मध्यम; कोई पाठ-चिह्न नहीं। अधूरा वाक्य: क्रिया इकाई ६० से चली आती है, जोड़ी नहीं गई; डेटा: GROUPING, ६० की "
           "निरन्तरता। सन्धि जाँची: तेषु + अपि → तेष्वपि (उ + अ → व); कदाचित् + आशु → कदाचिदाशु (स्वर से पहले त् → द्)।"),
    "62": ("गद्य; विश्वास उच्च; कोई पाठ-चिह्न नहीं। क्रियाहीन। ‘विशल्य’ = शल्य-रहित; समास ‘शल्य से मुक्त हुए को मारने वाले’ पढ़ा गया, "
           "जिसका कारण इकाई ६३ में। इकाई ४० (छपी पंक्ति ४२) कहती है कि उत्क्षेप में शल्य रहते व्यक्ति जी सकता है। वायव्य = वायु का। छपा "
           "‘स्थपनीच’ = स्थपनी च (अन्तर नहीं छोड़ा)।"),
    "63": ("गद्य; विश्वास मध्यम; कोई पाठ-चिह्न नहीं। ‘अवरुद्धः’ दो प्रकार से पढ़ा जा सकता है: वायु का विशेषण (सरल पाठ, अपनाया) या "
           "अनुक्त व्यक्ति का (‘शल्य-मुख से रुका हुआ’)। ‘जीवति’ का कर्ता छपा नहीं; अंग्रेज़ी में केवल सर्वनाम ‘he’ जोड़ा गया। सन्धि जाँची: "
           "शल्यमुख + अवरुद्धः → शल्यमुखावरुद्धः (अ + अ → आ); अवरुद्धः + हि → अवरुद्धो हि (अः + घोष व्यंजन → ओ); यावत् + अत्र → यावदत्र "
           "(स्वर से पहले त् → द्); वायुः + तिष्ठति → वायुस्तिष्ठति (त से पहले विसर्ग → स्); तावत् + जीवति → तावज्जीवति (त् + ज → ज्ज)।"),
    "64": ("गद्य; विश्वास मध्यम; एक पाठ-चिह्न: छपा ‘नीलामन्द्या’, ‘मन्द्या’ कोई मर्म-नाम नहीं, अनुमान से ‘मन्या’ (इकाई ५५ का ‘मन्मा’ भी "
           "देखें); अनुवाद में अनुमानित पाठ कहकर। छपा ‘कूर्च्च’ (दोहरा च) = कूर्च। ‘कूर्पराण्युर्वी’ = कूर्पर + आणि + उर्वी (डेटा का पाठ)। "
           "डेटा का गणना-निरीक्षण: छपे नाम ४२ देते हैं; ४४ के लिए ‘अंस’ (२) भी चाहिए, जो सम्भवतः ‘कुकुंदरांसफलक’ में लुप्त हो; खुला। "
           "छपा ‘फणापांगावार्ताः’ में ‘आवार्त’ दिखता है; डेटा इसे आवर्त पढ़ता है। सन्धि जाँची: कूर्पराणि + उर्वी → कूर्पराण्युर्वी (इ + उ → यु); "
           "आवर्ताः + चतुः → आवर्ताश्चतुः (च से पहले विसर्ग → श्); चतुश्चत्वारिंशत् + वैकल्य → चतुश्चत्वारिंशद्वैकल्य (घोष व्यंजन से पहले त् → द्)।"),
    "65": ("गद्य, दो छपी पंक्तियाँ (०२.०७.६८ और ०२.०७.६९); विश्वास उच्च; कोई पाठ-चिह्न नहीं। सोम = चन्द्र-तत्त्व, शीतल और स्थिर। "
           "‘धारयति’ णिजन्त रूप, अर्थ सीधा ‘धारण करता है’। ‘तानि’ = इकाई ६४ के सौम्य मर्म (डेटा)। मारे जाने वाला व्यक्ति छपा नहीं। "
           "छपा ‘तान्यापि’: तानि + अपि की सामान्य सन्धि तान्यपि होती; डेटा ने इसे चिह्नित नहीं किया, छपा रूप रखा। सन्धि जाँची: सोमः + हि → "
           "सोमो हि (अः + घोष व्यंजन → ओ); कदाचित् + अभिहतानि → कदाचिदभिहतानि (स्वर से पहले त् → द्)।"),
    "66": ("गद्य; विश्वास उच्च; कोई पाठ-चिह्न नहीं। छपा ‘कूर्च्च’ = कूर्च। आकर = खान, स्रोत। क्रियाहीन। सन्धि जाँची: कूर्चशिरः + गुल्फ → "
           "कूर्चशिरोगुल्फ (अः + घोष व्यंजन → ओ); मणिबन्धाः + तु → मणिबन्धास्तु (त से पहले विसर्ग → स्); तु + अष्टौ → त्वष्टौ (उ + अ → व); "
           "रुजाकराणि + अग्नि → रुजाकराण्यग्नि (इ + अ → य)।"),
    "67": ("गद्य; विश्वास उच्च; कोई पाठ-चिह्न नहीं। क्रियाहीन; इकाई ६६ का कारण। ‘अग्निवायू’ द्वन्द्व, प्रथमा द्विवचन; ‘रुजाकरौ’ द्विवचन, "
           "मेल खाता। विशेषेण = विशेष रूप से (अव्यय)। सन्धि: शब्दों के बीच कोई परिवर्तन नहीं।"),
}


# ===================================================================== AIDS
AIDS = {
    "55": {
        "diagram": {"groups": [
            {"label": "सिरा-मर्म, छपे क्रम में (१-८)", "items": ["१ उर्वी", "२ लोहिताख्य", "३ नाभि (मानक)", "४ हृदय (मानक)",
                                                          "५ स्तन मूल", "६ अपस्तंभ", "७ अलाप (सम्भवतः अपालाप)",
                                                          "८ पार्श्वसंधि"]},
            {"label": "सिरा-मर्म, छपे क्रम में (९-१६)", "items": ["९ बृहती", "१० नीला", "११ मन्मा (अनुमान: मन्या)", "१२ मातृका",
                                                           "१३ फण", "१४ अपांग", "१५ स्थपनी", "१६ शृंगाटक"]}]},
        "chunks": ("उर्वीलोहिताख्यनाभिहृदयस्तन | मूलापस्तंभालापपार्श्वसंधिबृहतीनीलामन्मामातृकाफणापांगस्थपनीशृंगाटकान्येकचत्वारिंशच्छिरा | "
                   "मर्माणि"),
        "sandhi": ("अ + अ → आ: फण + अपाङ्ग → फणापाङ्ग · इ + भिन्न स्वर → य्: शृङ्गाटकानि + एकचत्वारिंशत् → शृङ्गाटकान्येकचत्वारिंशत् · "
                   "त् + श → च्श, स्वर से पहले वैकल्पिक च्छ: एकचत्वारिंशत् + शिरा → एकचत्वारिंशच्छिरा (छपा च्छ)।"),
        "anchors": "रचना के पाँच भेद, क्रम से: मांस ११ (इकाई ५४) → सिरा ४१ (यह इकाई) → स्नायु २७ → अस्थि ८ → सन्धि २०। (मेरी याद-पद्धति)",
    },
    "56": {
        "diagram": {"groups": [
            {"label": "स्नायु-मर्म, छपे क्रम में", "items": ["१ क्षिप्र", "२ कूर्च", "३ कूर्चशिरस्", "४ विटप", "५ कक्षाधर",
                                                      "६ आणि (डेटा का विभाजन)", "७ बस्ति (मूत्राशय, मानक)",
                                                      "८ अंस (कन्धा, मानक)", "९ विधुर", "१० उत्क्षेप"]}]},
        "chunks": "क्षिप्रकूर्चकूर्चशिरोविटपकक्षाधराणिबस्त्यंसविधुरोत्क्षेपाः | सप्तविंशति | स्नावमर्माणि",
        "sandhi": ("अः / -अस् + घोष व्यंजन → ओ: कूर्चशिरः + विटप → कूर्चशिरोविटप · इ + अ → य: बस्ति + अंस → बस्त्यंस · "
                   "अ + उ → ओ: विधुर + उत्क्षेपाः → विधुरोत्क्षेपाः।"),
        "puns": "‘स्नाव’ सुनते ही ‘स्नायु’ याद करें: स्नाव-मर्म = स्नायु के मर्म। (केवल सुनने की सहायता, मेरी बनाई)",
    },
    "57": {
        "diagram": {"groups": [
            {"label": "अस्थि-मर्म, छपे क्रम में", "items": ["१ कटीकतरुण", "२ नितम्ब (नितम्ब, कूल्हा: मानक शब्दार्थ)",
                                                     "३ अंसफलक (सम्भवतः कन्धे की चपटी हड्डी)", "४ शङ्ख (सम्भवतः कनपटी)"]}]},
        "chunks": "कटीकतरुणनितंबांसफलकशंखास्त्वष्टावस्थिमर्माणि",
        "sandhi": ("त से पहले विसर्ग → स्: शङ्खाः + तु → शङ्खास्तु · उ + अ → व: तु + अष्टौ → त्वष्टौ · औ + स्वर → आव्: "
                   "अष्टौ + अस्थि → अष्टावस्थि।"),
    },
    "58": {
        "diagram": {"groups": [
            {"label": "सन्धि-मर्म, छपे क्रम में", "items": ["१ गुल्फ: टखना (मानक)", "२ मणिबंध: कलाई (मानक)", "३ जानु: घुटना (मानक)",
                                                     "४ कूर्पर: कोहनी (मानक)", "५ कुकुंदर (सम्भावित क्षेत्र)",
                                                     "६ कृकाटिका (सम्भावित क्षेत्र)", "७ आवर्त", "८ सीमंत", "९ अधिपति"]}]},
        "chunks": "गुल्फमणिबंधजानुकूर्परकुकुंदरकृकाटिकाऽऽवर्तसीमंताधिपतयो | विंशति | संधिमर्माणि",
        "sandhi": ("आ + आ → आ: कृकाटिका + आवर्त → कृकाटिकावर्त (छपाई में ‘ऽऽ’) · अः + घोष व्यंजन → ओ: अधिपतयः + विंशति → "
                   "अधिपतयो विंशति।"),
        "anchors": "पहले चार नाम शरीर के चार बड़े जोड़: टखना, कलाई, घुटना, कोहनी, पैर-हाथ-पैर-हाथ। (मेरी याद-पद्धति)",
    },
    "59": {
        "chain": {"steps": ["पुनश्च पञ्चधा: दूसरा पाँच-भेद", "नाम: नाभि, हृदय, मातृका, शङ्ख, शृङ्गाटक, अधिपति (आरम्भ अस्पष्ट)",
                            "एकोनविंशति: उन्नीस", "सद्यः प्राणहर: तत्काल प्राण हरते", "कारण: आग्नेय होने से",
                            "समय: छपा समरात्र (अस्पष्ट शब्द)"]},
        "chunks": ("पुनश्च | पंचधा | गुदब | स्तनाभिहृदयमातृकाशंखशृंगाटकाधिपतयएकोनविंशति | सद्यः | प्राणहराण्याग्नेयत्वात्तेषां | "
                   "समरात्राभ्यंतरं | कालः"),
        "sandhi": ("च से पहले विसर्ग → श्: पुनः + च → पुनश्च · इ + आ → या: प्राणहराणि + आग्नेयत्वात् → प्राणहराण्याग्नेयत्वात्।"),
        "frame": "कितने प्रकार: पञ्चधा → कौन: उन्नीस (सूची का आरम्भ बिगड़ा) → क्या करते: सद्यः प्राण हरते → क्यों: आग्नेयत्वात् → कब तक: अस्पष्ट।",
    },
    "60": {
        "chain": {"steps": ["नाम: तलहृदय से सीमन्त तक (वक्षोमर्म छपे रूप में)", "त्रयस्त्रिंशत्: तैंतीस",
                            "कालान्तर-प्राणहर: कुछ समय बाद प्राण हरते", "कारण: सौम्य भी, आग्नेय भी", "समय: पक्ष के भीतर"]},
        "chunks": ("तलहृदयक्षिप्रेंद्रबस्तिवक्षोमर्मकटीकतरुणनितंब | पार्श्वसंधिबृहतीसीमंतास्त्रयस्त्रिंशत्कालांतरप्राणहराणि | "
                   "सौम्याग्नेयत्वात्तेषां | पक्षाभ्यंतरं | कालः"),
        "contrast": "इसी इकाई के दो गुण साथ: सौम्य (सोम का, शीतल) ⇄ आग्नेय (अग्नि का)। दोनों मिले हैं, इसलिए मृत्यु तत्काल नहीं, पक्ष के भीतर।",
        "sandhi": ("त से पहले विसर्ग → स्: सीमन्ताः + त्रयस्त्रिंशत् → सीमन्तास्त्रयस्त्रिंशत् · अ + अ → आ: पक्ष + अभ्यन्तरम् → "
                   "पक्षाभ्यन्तरम्।"),
    },
    "61": {
        "chunks": "तेष्वपि | तु | क्षिप्राणि | कदाचिदाशु",
        "frame": "किनमें: तेषु (इकाई ६० के तैंतीस) → कौन: क्षिप्राणि → कब: कदाचित् (कभी) → कैसे: आशु (शीघ्र) → क्रिया: छपी नहीं, ६० से।",
        "sandhi": "उ + अ → व: तेषु + अपि → तेष्वपि · स्वर से पहले त् → द्: कदाचित् + आशु → कदाचिदाशु।",
        "puns": "‘क्षिप्र’ = शीघ्र, और यहाँ कहा भी ‘आशु’ (शीघ्र): नाम और बात मेल खाते हैं। (केवल सुनने की सहायता, मेरी बनाई; पाठ यह कारण नहीं बताता)",
    },
    "62": {
        "diagram": {"groups": [
            {"label": "त्रीणि विशल्यघ्नानि", "items": ["उत्क्षेपौ: दो उत्क्षेप", "स्थपनी: एक", "कारण: वायव्यत्वात् (वायु का स्वभाव)"]}]},
        "chunks": "उत्क्षेपौ | स्थपनीच | त्रीणि | विशल्यघ्नानि | वायव्यत्वात्",
        "anchors": "इकाई ४०: शल्य रहते उत्क्षेप में जीवन सम्भव, खींच निकालने पर नहीं → इकाई ६२: विशल्यघ्न → इकाई ६३: कारण, रुका हुआ वायु।",
        "frame": "कौन: उत्क्षेपौ + स्थपनी → कितने: त्रीणि → क्या: विशल्यघ्न (शल्य निकलने पर मारने वाले) → क्यों: वायव्यत्वात्।",
    },
    "63": {
        "chain": {"steps": ["शल्य का मुख", "वायु को रोकता है (सरल पाठ)", "यावत्: जब तक वायु यहाँ ठहरता है",
                            "तावत्: तब तक वह जीता है"]},
        "chunks": "शल्यमुखावरुद्धो | हि | यावदत्र | वायुस्तिष्ठति | तावज्जीवति",
        "sandhi": ("स्वर से पहले त् → द्: यावत् + अत्र → यावदत्र · त से पहले विसर्ग → स्: वायुः + तिष्ठति → वायुस्तिष्ठति · "
                   "त् + ज → ज्ज: तावत् + जीवति → तावज्जीवति।"),
        "frame": "यावत् ... तावत्: जब तक (शर्त) ... तब तक (फल)।",
    },
    "64": {
        "diagram": {"groups": [
            {"label": "वैकल्यकर, छपे क्रम में (१-९)", "items": ["१ कूर्च्च", "२ जानु", "३ कूर्पर", "४ आणि (डेटा का विभाजन)", "५ उर्वी",
                                                         "६ लोहिताख्य", "७ विटप", "८ कक्षाधर", "९ कुकुंदर"]},
            {"label": "वैकल्यकर, छपे क्रम में (१०-१७)", "items": ["१० अंसफलक", "११ नीला", "१२ मन्द्या (अनुमान: मन्या)", "१३ कृकाटिका",
                                                           "१४ विधुर", "१५ फण", "१६ अपांग", "१७ आवार्त (आवर्त)"]}]},
        "chunks": "कूर्च्चजानुकूर्पराण्युर्वीलोहिताख्यविटपकक्षाधरकुकुंदरांसफलकनीलामन्द्याकृकाटिकाविधुरफणापांगावार्ताश्चतुश्चत्वारिंशद्वैकल्यकराणि | सौम्यत्वात्",
        "sandhi": ("इ + उ → यु: कूर्पराणि + उर्वी → कूर्पराण्युर्वी · च से पहले विसर्ग → श्: आवर्ताः + चतुः → आवर्ताश्चतुः · "
                   "घोष व्यंजन से पहले त् → द्: चतुश्चत्वारिंशत् + वैकल्य → चतुश्चत्वारिंशद्वैकल्य।"),
        "anchors": "परिणाम के कारण, क्रम से: आग्नेय → सद्यः (५९) · सौम्य + आग्नेय → कालान्तर (६०) · वायव्य → विशल्यघ्न (६२) · सौम्य → वैकल्य (६४) · तीनों का बाहुल्य → रुजा (६६)। (मेरी याद-पद्धति)",
    },
    "65": {
        "chain": {"steps": ["सोम", "स्थैर्य और शैत्य से", "प्राणों को धारण करता है", "वे भी (इकाई ६४ के सौम्य मर्म)",
                            "कभी आहत होने पर", "मार देते हैं"]},
        "chunks": "सोमो हि | स्थैर्यशैत्याभ्यां | प्राणान्धारयति || तान्यापि च | कदाचिदभिहतानि | मारयंति",
        "sandhi": "अः + घोष व्यंजन → ओ: सोमः + हि → सोमो हि · स्वर से पहले त् → द्: कदाचित् + अभिहतानि → कदाचिदभिहतानि।",
    },
    "66": {
        "diagram": {"groups": [
            {"label": "अष्टौ रुजाकराणि", "items": ["कूर्चशिरस्", "गुल्फ: टखना (मानक)", "मणिबन्ध: कलाई (मानक)"]},
            {"label": "कारण: गुणों का बाहुल्य", "items": ["अग्नि", "वायु", "सोम"]}]},
        "chunks": "कूर्च्चशिरोगुल्फमणिबंधास्त्वष्टौ | रुजाकराण्यग्निवायुसोमगुणबाहुल्यात्",
        "sandhi": ("त से पहले विसर्ग → स्: मणिबन्धाः + तु → मणिबन्धास्तु · उ + अ → व: तु + अष्टौ → त्वष्टौ · इ + अ → य: "
                   "रुजाकराणि + अग्नि → रुजाकराण्यग्नि।"),
        "puns": "‘रुज-आकर’ = पीड़ा की खान: जैसे खान से धातु निकले, वैसे इन मर्मों से पीड़ा। (केवल सुनने की सहायता, मेरी बनाई)",
    },
    "67": {
        "chunks": "अग्निवायू | हि | विशेषेण | रुजाकरौ",
        "frame": "कौन: अग्निवायू (दो) → कैसे: विशेषेण (विशेष रूप से, केवल नहीं) → क्या: रुजाकरौ (दो पीड़ा-स्रोत) → क्यों कहा: हि, इकाई ६६ का कारण।",
        "anchors": "इकाई ६६: तीनों (अग्नि, वायु, सोम) → इकाई ६७: उनमें विशेष दो (अग्नि, वायु)।",
    },
}


# ============================================================== IMAGE_SPECS
IMAGE_SPECS = {
    ("55", "diagram"): {
        "file": "sh7-sira-marma-55.svg",
        "alt": ("Two columns of unit 55's sixteen printed names in printed order: 1 urvī to 8 pārśvasandhi, 9 bṛhatī to "
                "16 śṛṅgāṭaka; nābhi and hṛdaya standard; alāpa probably apālāpa; printed manmā read manyā by "
                "conjecture: forty-one vessel-marmas."),
        "type": "split",
        "title": "इकाई ५५: इकतालीस सिरा-मर्म",
        "cols": [["१ से ८", ["१ उर्वी", "२ लोहिताख्य", "३ नाभि (मानक)", "४ हृदय (मानक)", "५ स्तन मूल", "६ अपस्तंभ",
                            "७ अलाप (सम्भवतः अपालाप)", "८ पार्श्वसंधि"]],
                 ["९ से १६", ["९ बृहती", "१० नीला", "११ मन्मा (अनुमान: मन्या)", "१२ मातृका", "१३ फण", "१४ अपांग",
                             "१५ स्थपनी", "१६ शृंगाटक"]]],
    },
    ("56", "diagram"): {
        "file": "sh7-snava-marma-56.svg",
        "alt": ("Two columns of unit 56's ten names in printed order: kṣipra, kūrca, kūrcaśiras, viṭapa, kakṣādhara; "
                "āṇi (data's split), basti (bladder, standard), aṃsa (shoulder, standard), vidhura, utkṣepa: twenty-seven "
                "sinew-marmas."),
        "type": "split",
        "title": "इकाई ५६: सत्ताईस स्नायु-मर्म",
        "cols": [["१ से ५", ["१ क्षिप्र", "२ कूर्च", "३ कूर्चशिरस्", "४ विटप", "५ कक्षाधर"]],
                 ["६ से १०", ["६ आणि (डेटा का विभाजन)", "७ बस्ति (मूत्राशय, मानक)", "८ अंस (कन्धा, मानक)", "९ विधुर",
                             "१० उत्क्षेप"]]],
    },
    ("58", "diagram"): {
        "file": "sh7-sandhi-marma-58.svg",
        "alt": ("Table of unit 58's nine names in printed order with the data's labels: gulpha ankle, maṇibandha wrist, "
                "jānu knee, kūrpara elbow (standard); kukundara and kṛkāṭikā (probable regions); āvarta, sīmanta, "
                "adhipati: twenty joint-marmas."),
        "type": "table",
        "title": "इकाई ५८: बीस सन्धि-मर्म",
        "heads": ["छपा नाम", "डेटा का लेबल"],
        "rows": [["१ गुल्फ", "टखना (मानक)"], ["२ मणिबंध", "कलाई (मानक)"], ["३ जानु", "घुटना (मानक)"],
                 ["४ कूर्पर", "कोहनी (मानक)"], ["५ कुकुंदर", "क्षेत्र सम्भावित"], ["६ कृकाटिका", "क्षेत्र सम्भावित"],
                 ["७ आवर्त", "मर्म-नाम"], ["८ सीमंत", "मर्म-नाम"], ["९ अधिपति", "मर्म-नाम"], ["कुल", "विंशति (२०)"]],
    },
    ("59", "chain"): {
        "file": "sh7-sadyah-pranahara-59.svg",
        "alt": ("Chain of unit 59: again in five ways; names nābhi, hṛdaya, mātṛkā, śaṅkha, śṛṅgāṭaka, adhipati (start of "
                "list damaged); nineteen; take life at once; reason: being fiery; time: printed samarātra, an unclear word."),
        "type": "chain",
        "title": "इकाई ५९: सद्यः प्राणहर",
        "steps": ["पुनश्च पञ्चधा: दूसरा पाँच-भेद", "नाम: नाभि, हृदय, मातृका, शङ्ख, शृङ्गाटक, अधिपति (आरम्भ अस्पष्ट)",
                  "एकोनविंशति: उन्नीस", "सद्यः प्राणहर: तत्काल प्राण हरते", "कारण: आग्नेय होने से",
                  "समय: छपा समरात्र (अस्पष्ट शब्द)"],
    },
    ("60", "chain"): {
        "file": "sh7-kalantara-60.svg",
        "alt": ("Chain of unit 60: names from talahṛdaya to sīmanta (vakṣomarma as printed); thirty-three; take life "
                "after an interval; reason: both saumya and āgneya; time: within a fortnight."),
        "type": "chain",
        "title": "इकाई ६०: कालान्तर-प्राणहर",
        "steps": ["नाम: तलहृदय से सीमन्त तक (वक्षोमर्म छपे रूप में)", "त्रयस्त्रिंशत्: तैंतीस",
                  "कालान्तर-प्राणहर: कुछ समय बाद प्राण हरते", "कारण: सौम्य भी, आग्नेय भी", "समय: पक्ष के भीतर"],
    },
    ("62", "diagram"): {
        "file": "sh7-vishalyaghna-62.svg",
        "alt": ("Flowchart of unit 62: the two utkṣepas and the one sthapanī make three viśalyaghna marmas; reason: "
                "their nature of Vāyu (wind)."),
        "type": "mermaid",
        "code": ("flowchart TD\n"
                 "  A[\"उत्क्षेप: दो\"] --> C[\"तीन विशल्यघ्न\"]\n"
                 "  B[\"स्थपनी: एक\"] --> C\n"
                 "  D[\"कारण: वायु का स्वभाव\"] --> C\n"),
    },
    ("65", "chain"): {
        "file": "sh7-soma-65.svg",
        "alt": ("Chain of unit 65 in line order: Soma; by steadiness and coolness; sustains the life-breaths; those too "
                "(the saumya marmas of unit 64); sometimes, when struck; kill."),
        "type": "chain",
        "title": "इकाई ६५: सोम और सौम्य मर्म",
        "steps": ["सोम", "स्थैर्य और शैत्य से", "प्राणों को धारण करता है", "वे भी (इकाई ६४ के सौम्य मर्म)",
                  "कभी आहत होने पर", "मार देते हैं"],
    },
    ("66", "diagram"): {
        "file": "sh7-rujakara-66.svg",
        "alt": ("Flowchart of unit 66: kūrcaśiras, gulpha (ankle) and maṇibandha (wrist) are eight sources of pain; "
                "reason: abundance of the qualities of Agni, Vāyu and Soma."),
        "type": "mermaid",
        "code": ("flowchart TD\n"
                 "  A[\"कूर्चशिरस्, गुल्फ, मणिबन्ध\"] --> D[\"आठ रुजाकर\"]\n"
                 "  E[\"अग्नि, वायु, सोम\"] --> F[\"गुणों का बाहुल्य\"]\n"
                 "  F --> D\n"),
    },
}
