from helpers import mcq, match, order, fill, multi, accepts

AUTHORED = {}

# ---------------------------------------------------------------- unit 76
AUTHORED["76"] = {
    "title": "स्नेहपाकस्त्रिधा",
    "question": "What are the three kinds of sneha-cooking, and how are the first two known, by verse 76?",
    "rule": ("Sneha-cooking is of three kinds: manda (mild), cikkaṇa (smooth) and khara-cikkaṇa (hard-smooth). "
             "Manda when the residue (kiṭṭa) is like the kalka (paste); cikkaṇa when it is like madana (probably wax)."),
    "limits": ("The verse does not define khara-cikkaṇa beyond its name here; its sign follows in the next verse (line 05.08.93). "
               "'Hard-smooth' is the data's reading of the compound, not a definition given by the text. Madana is taken as "
               "wax (probable); the word also names a tree and the god of love. No times or temperatures are given."),
    "explain_hi": ("स्नेह यानी तेल या वसा (घी या तेल) का पाक तीन प्रकार का बताया गया है: मन्द, चिक्कण यानी चिकना, और खर-चिक्कण। "
                   "पहचान पात्र में बचे किट्ट यानी तलछट से होती है। जब किट्ट कल्क यानी लुगदी के समान ही हो, तब पाक मन्द है; "
                   "जब वह मदन यानी सम्भवतः मोम के समान हो, तब चिक्कण। तीसरे प्रकार खर-चिक्कण का लक्षण अगले श्लोक में आता है। "
                   "‘कल्कसमे किट्टे’ सप्तमी है: ‘जब किट्ट कल्क के समान हो’।"),
    "hook": "किट्ट लुगदी जैसा: मन्द; किट्ट मोम जैसा: चिक्कण।",
    "core": True,
    "questions": [
        mcq("pretest", 0,
            "In verse 76, what does त्रिधा mean?",
            ("Of three kinds",
             "त्रिधा (ind.) = in three ways, of three kinds: sneha-cooking is of three kinds."),
            [("Three times over", "The verse does not say to cook three times; त्रिधा = of three kinds."),
             ("For three days", "No days are named; त्रिधा = of three kinds."),
             ("With three liquids", "No liquids are listed here; त्रिधा = of three kinds.")],
            "स्नेहपाकस्त्रिधा: sneha-cooking is of three kinds.",
            "त्रिधा = of three kinds."),
        match(1, "Match each word of verse 76 to its meaning.",
              [["मन्द", "mild"], ["चिक्कण", "smooth"], ["किट्ट", "residue"], ["कल्क", "paste"],
               ["मदन", "probably wax"]],
              "मंदः कल्कसमे किट्टे चिक्कणो मदनोपमे: manda when the residue is like the paste; cikkaṇa when like madana.",
              "मन्द = mild; चिक्कण = smooth; किट्ट = residue; कल्क = paste; मदन = probably wax."),
        order(2, "Put the three kinds of sneha-cooking in the order of verse 76.",
              ["मन्द", "चिक्कण", "खरचिक्कण"],
              "मंदश्चिक्कणः खरचिक्कणः: manda, cikkaṇa, khara-cikkaṇa.",
              "मन्द · चिक्कण · खरचिक्कण.",
              role="extend",
              teaches="Verse 76 names the three kinds of sneha-cooking in this order: manda (mild), cikkaṇa (smooth), khara-cikkaṇa (hard-smooth)."),
        mcq("discriminate", 3, "Which split is right for स्नेहपाकस्त्रिधा?",
            ("स्नेहपाकः + त्रिधा",
             "A visarga before त becomes स्: स्नेहपाकः + त्रिधा = स्नेहपाकस्त्रिधा."),
            [("स्नेहपाक + स्त्रिधा", "स्त्रिधा is not a word; the स् comes from the visarga of स्नेहपाकः."),
             ("स्नेहपाकाः + त्रिधा", "A plural स्नेहपाकाः would give स्नेहपाकास्त्रिधा, with long आ."),
             ("स्नेहपाकम् + त्रिधा", "म् before त would stay as anusvara: स्नेहपाकं त्रिधा.")],
            "स्नेहपाकः (sneha-cooking) + त्रिधा (of three kinds).",
            "-ः before त → -स्त."),
        mcq("apply", 4,
            "A cook sees that the residue in the pan has become like madana (probably wax). Which kind of cooking is it, by verse 76?",
            ("Cikkaṇa",
             "चिक्कणो मदनोपमे: cikkaṇa when the residue is like madana."),
            [("Manda", "Manda is when the residue is still like the kalka (paste)."),
             ("Dagdha", "Dagdha (burnt) is named only in the next verse, beyond the last kind."),
             ("Svarasa", "Svarasa is an expressed juice, not a kind of sneha-cooking.")],
            "Residue like kalka → manda; residue like madana → cikkaṇa.",
            "Madana-like residue = cikkaṇa."),
        mcq("transfer", 5,
            "कल्कसमे किट्टे means when the residue is like the kalka. By the same pattern, what does मधुसमे किट्टे mean?",
            ("When the residue is like honey",
             "X-same in the locative with किट्टे = when the residue is like X; मधु = honey."),
            [("When honey is added to the residue", "No adding is said; -सम means like, equal to."),
             ("The residue left by the honey", "That would need a genitive; मधुसमे says like honey."),
             ("When the honey has no residue", "Nothing is denied; the residue is said to be like honey.")],
            "-सम = like; the locative pair gives the condition: when the residue is like X.",
            "X-समे किट्टे = when the residue is like X.",
            teaches="A locative pair like कल्कसमे किट्टे gives the condition 'when the residue is like X': मधुसमे किट्टे = when the residue is like honey."),
    ],
}

# ---------------------------------------------------------------- unit 77
AUTHORED["77"] = {
    "title": "किंचित्सीदति कृष्णे च",
    "question": "What is the sign of the last kind of sneha-cooking, and what lies beyond it, by verse 77?",
    "rule": ("The last kind (khara-cikkaṇa) is when the residue sinks a little and is black. Beyond this the sneha is "
             "burnt (dagdha) and should be taken out."),
    "limits": ("The verse runs on from verse 76: 'the last' is khara-cikkaṇa, named there. Whether niṣkārya means taken off the "
               "fire or thrown away is not said (OPEN); no question rests on it. The printed आमास् of the last word is flagged "
               "(probably आमः, the raw one); the closing statement on the raw sneha and agnisāda is left without a question."),
    "explain_hi": ("यह श्लोक पिछले श्लोक की बात पूरी करता है। अन्तिम (पश्चिम) प्रकार, यानी खर-चिक्कण, तब है जब किट्ट यानी तलछट थोड़ा "
                   "बैठता है और काला रहता है। इससे आगे पकाने पर स्नेह दग्ध यानी जला हुआ हो जाता है; उसे निकालना चाहिए "
                   "(आग से या प्रयोग से, पाठ नहीं बताता)। अन्त में कहा गया है कि कच्चा स्नेह अग्निसाद यानी पाचन-अग्नि को क्षीण करने "
                   "वाला होता है; इस शब्द के छपे रूप पर सन्देह है।"),
    "hook": "थोड़ा बैठे, काला हो: अन्तिम; उससे आगे: दग्ध।",
    "core": False,
    "questions": [
        mcq("pretest", 0,
            "In verse 77, what does दग्ध mean?",
            ("Burnt",
             "दग्धः (ppp. √दह्) = burnt: beyond the last kind the sneha is burnt."),
            [("Cooled", "Cooling is not named here; दग्ध = burnt."),
             ("Strained", "Straining is not named here; दग्ध = burnt."),
             ("Mixed", "Mixing is not named here; दग्ध = burnt.")],
            "दग्धोऽतऊर्ध्वम्: beyond this it is burnt.",
            "दग्ध = burnt."),
        match(1, "Match each word of verse 77 to its meaning.",
              [["किंचित्", "a little"], ["सीदति", "sinks"], ["कृष्ण", "black"], ["पश्चिम", "the last"],
               ["दग्ध", "burnt"]],
              "किंचित्सीदति कृष्णे च वर्त्तमाने तु पश्चिमः । दग्धोऽतऊर्ध्वम्.",
              "किंचित् = a little; सीदति = sinks; कृष्ण = black; पश्चिम = the last; दग्ध = burnt."),
        order(2, "Put the phrases of verse 77 in the order of the text.",
              ["किंचित्सीदति", "कृष्णे च वर्त्तमाने", "तु पश्चिमः", "दग्धोऽतऊर्ध्वम्"],
              "किंचित्सीदति · कृष्णे च वर्त्तमाने · तु पश्चिमः · दग्धोऽतऊर्ध्वम्: two signs, the kind they mark, then what lies beyond.",
              "Signs (sinks a little, black) · the last kind · beyond it, burnt.",
              role="extend",
              teaches="Verse 77 gives two signs (the residue sinks a little, it is black), names the kind they mark (the last), then says that beyond it the sneha is burnt."),
        mcq("discriminate", 3, "Which split is right for दग्धोऽतऊर्ध्वम्?",
            ("दग्धः + अतः + ऊर्ध्वम्",
             "-अः + अ → -ओऽ (दग्धोऽ); -अः before ऊ drops the visarga and the vowels stay apart (अत ऊर्ध्वम्)."),
            [("दग्ध + अतः + ऊर्ध्वम्", "अ + अ would merge into आ: दग्धातऊर्ध्वम्."),
             ("दग्धः + ततः + ऊर्ध्वम्", "ततः would leave its त in the print; the word is अतः."),
             ("दग्धम् + अतः + ऊर्ध्वम्", "म् before a vowel would give दग्धमतऊर्ध्वम्.")],
            "दग्धः (burnt) + अतः (from this) + ऊर्ध्वम् (beyond).",
            "-अः + अ → -ओऽ; -अः + other vowel → -अ (gap)."),
        mcq("apply", 4,
            "A cook sees the residue sink a little and turn black. Which kind of sneha-cooking has been reached, by verse 77?",
            ("The last, khara-cikkaṇa",
             "किंचित्सीदति कृष्णे च … पश्चिमः: these signs mark the last kind, khara-cikkaṇa of verse 76."),
            [("The first, manda", "Manda is when the residue is like the kalka (verse 76)."),
             ("The middle, cikkaṇa", "Cikkaṇa is when the residue is like madana (verse 76)."),
             ("Beyond it, the burnt", "Burnt is what comes after these signs, not these signs themselves.")],
            "Sinks a little and black → the last kind (khara-cikkaṇa).",
            "Sinks a little + black = khara-cikkaṇa."),
        mcq("transfer", 5,
            "Join ततः + ऊर्ध्वम् (after that) by the rule seen in अतऊर्ध्वम्. Which is right?",
            ("तत ऊर्ध्वम्",
             "After अ, a visarga before a vowel other than अ is dropped and the two vowels stay apart, as in अत ऊर्ध्वम्."),
            [("ततो ऊर्ध्वम्", "-अः → -ओ only before अ or a voiced consonant, not before ऊ."),
             ("ततूर्ध्वम्", "After the visarga is dropped no further joining takes place; the vowels stay apart."),
             ("ततरूर्ध्वम्", "-ः → र् only after vowels other than अ/आ; here अ precedes.")],
            "Same rule as अतः + ऊर्ध्वम् = अत ऊर्ध्वम्.",
            "-अः + vowel (not अ) → -अ, gap stays.",
            teaches="After अ, a visarga before a vowel other than अ is dropped and no more sandhi follows: अतः + ऊर्ध्वम् = अत ऊर्ध्वम्; ततः + ऊर्ध्वम् = तत ऊर्ध्वम्."),
    ],
}

# ---------------------------------------------------------------- unit 78
AUTHORED["78"] = {
    "title": "मृदुर्नस्ये खरोऽभ्यंगे",
    "question": "Which cooked sneha suits which use, and which two mountains are named, by verse 78?",
    "rule": ("Mild (mṛdu) for nasya (nasal administration), hard (khara) for abhyaṅga (oil massage), cikkaṇa for drinking "
             "and basti (enema). The earth is mostly marked by the mountains Himavat and Vindhya."),
    "limits": ("Mṛdu and khara are not the names of the kinds in verse 76 (manda, khara-cikkaṇa); the text may mean the same, "
               "but does not say so. The verb of the second line is printed व्यासा, read on a conjecture as व्याप्ता "
               "(pervaded) or व्यस्ता (divided); no question rests on it. The copula is understood."),
    "explain_hi": ("पहली पंक्ति बताती है कि कौन-सा पका स्नेह किस प्रयोग में: नस्य यानी नाक में डालने में मृदु, अभ्यंग यानी मालिश में खर, "
                   "और पान यानी पीने तथा बस्ति यानी एनिमा में चिक्कण। मृदु और खर पिछले श्लोक के प्रकार-नाम (मन्द, खर-चिक्कण) "
                   "नहीं हैं; पाठ उन्हें एक नहीं कहता। दूसरी पंक्ति नया विषय खोलती है: पृथ्वी प्रायः हिमवान् और विन्ध्य पर्वतों से "
                   "(अनुमानित पाठ के अनुसार) व्याप्त है। अगला श्लोक इन दोनों क्षेत्रों की औषधियों के स्वभाव बताता है।"),
    "hook": "नाक में मृदु, मालिश में खर, पीने-बस्ति में चिक्कण।",
    "core": True,
    "questions": [
        mcq("pretest", 0,
            "Which two mountains does verse 78 name?",
            ("Himavat and Vindhya",
             "हिमवद्विंध्यशैलाभ्याम्: by the mountains Himavat and Vindhya."),
            [("Meru and Vindhya", "Meru is not named; the pair is Himavat and Vindhya."),
             ("Himavat and Malaya", "Malaya is not named; the pair is Himavat and Vindhya."),
             ("Kailāsa and Meru", "Neither is named; the pair is Himavat and Vindhya.")],
            "हिमवत् + विन्ध्य + शैल: the Himavat and Vindhya mountains.",
            "Verse 78 names Himavat and Vindhya."),
        match(1, "Match each use in verse 78 to its meaning.",
              [["नस्य", "nasal administration"], ["अभ्यङ्ग", "oil massage"], ["पान", "drinking"], ["बस्ति", "enema"]],
              "मृदुर्नस्ये खरोऽभ्यंगे पाने बस्तौ च चिक्कणः.",
              "नस्य = nasal administration; अभ्यङ्ग = oil massage; पान = drinking; बस्ति = enema."),
        order(2, "Put the four uses of cooked sneha in the order of verse 78.",
              ["नस्य", "अभ्यङ्ग", "पान", "बस्ति"],
              "नस्ये · अभ्यंगे · पाने · बस्तौ: nasya, then abhyaṅga, then drinking and basti.",
              "नस्य · अभ्यङ्ग · पान · बस्ति.",
              role="extend",
              teaches="Verse 78 lists the uses in this order: nasya (mild), abhyaṅga (hard), drinking and basti (cikkaṇa)."),
        mcq("discriminate", 3, "Which cooked sneha does verse 78 give for abhyaṅga (oil massage)?",
            ("Khara (hard)",
             "खरोऽभ्यंगे: hard for abhyaṅga."),
            [("Mṛdu (mild)", "Mild is for nasya, not for abhyaṅga."),
             ("Cikkaṇa (smooth)", "Cikkaṇa is for drinking and basti."),
             ("Dagdha (burnt)", "Burnt sneha is to be taken out (verse 77), not used.")],
            "मृदुः → nasya; खरः → abhyaṅga; चिक्कणः → drinking, basti.",
            "Abhyaṅga takes khara."),
        multi("apply", 4,
              "Which uses take the cikkaṇa sneha, by verse 78? Choose all that apply.",
              [("Drinking (पान)", "Right: पाने … चिक्कणः."),
               ("Basti, enema (बस्ति)", "Right: बस्तौ च चिक्कणः."),
               ("Nasya (नस्य)", "Wrong: nasya takes the mild (मृदु) one."),
               ("Abhyaṅga (अभ्यङ्ग)", "Wrong: abhyaṅga takes the hard (खर) one.")],
              [0, 1],
              "पाने बस्तौ च चिक्कणः: cikkaṇa for drinking and for basti.",
              "Cikkaṇa = drinking + basti."),
        mcq("transfer", 5,
            "हिमवत् + विन्ध्य gives हिमवद्विन्ध्य. By the same rule, which is right for भगवत् + गीता?",
            ("भगवद्गीता",
             "Final त् becomes द् before a voiced consonant: त् + ग → द्ग, as त् + व → द्व in हिमवद्विन्ध्य."),
            [("भगवत्गीता", "त् does not stay voiceless before the voiced ग."),
             ("भगवन्गीता", "त् becomes न् only before a nasal; ग is not a nasal."),
             ("भगवग्गीता", "त् is not made into the next letter here; it only becomes voiced, द्.")],
            "त् + voiced consonant → द्.",
            "Final त् → द् before a voiced consonant.",
            teaches="Final त् becomes द् before a voiced consonant: हिमवत् + विन्ध्य = हिमवद्विन्ध्य; भगवत् + गीता = भगवद्गीता."),
    ],
}

# ---------------------------------------------------------------- unit 79
AUTHORED["79"] = {
    "title": "सौम्यं पथ्यं च तत्राद्यम्",
    "question": "What are the natures of the medicine of the first region and of the Vindhya, and how does the chapter close?",
    "rule": ("Among these, the first is saumya (of Soma's nature) and pathya (wholesome); the Vindhya medicine is āgneya "
             "(of Agni's nature). Thus the eighth chapter, named Bheṣajakalpa (the preparation of medicines)."),
    "limits": ("'The first' is taken as the first of the two mountains of verse 78 (Himavat), by the plain order; the verse does "
               "not name it. Saumya and āgneya are not defined further. The second line is the chapter colophon, not a verse; "
               "its opening double danda is a printed mark."),
    "explain_hi": ("पिछले श्लोक में हिमवान् और विन्ध्य दो क्षेत्र बताए गए। उनमें पहले (आद्य; सामान्य क्रम से हिमवान्) की औषध सौम्य यानी "
                   "सोम स्वभाव वाली और पथ्य यानी हितकर है; विन्ध्य की औषध आग्नेय यानी अग्नि स्वभाव वाली है। सौम्य और आग्नेय का आगे "
                   "कोई विवरण नहीं दिया गया। दूसरी पंक्ति अध्याय का समापन-वाक्य है: इस प्रकार भेषजकल्प यानी औषध-निर्माण नामक "
                   "आठवाँ अध्याय। ‘अष्टमोऽध्यायः’ = अष्टमः + अध्यायः।"),
    "hook": "पहला क्षेत्र सौम्य-पथ्य, विन्ध्य आग्नेय; आठवाँ अध्याय भेषजकल्प।",
    "core": True,
    "questions": [
        mcq("pretest", 0,
            "In verse 79, what does औषध mean?",
            ("Medicine",
             "औषधम् (n.) = medicine; distinct from ओषधि, herb."),
            [("Mountain", "Mountain is शैल (verse 78); औषध = medicine."),
             ("Region", "No word for region is used here; औषध = medicine."),
             ("Season", "No season is named; औषध = medicine.")],
            "आग्नेयं वैंध्यमौषधम्: the Vindhya medicine is āgneya.",
            "औषध = medicine."),
        match(1, "Match each word of verse 79 to its meaning.",
              [["सौम्य", "of Soma's nature"], ["पथ्य", "wholesome"], ["आग्नेय", "of Agni's nature"],
               ["वैन्ध्य", "of the Vindhya"], ["अष्टम", "eighth"]],
              "सौम्यं पथ्यं च तत्राद्यमाग्नेयं वैंध्यमौषधम् । इति भेषजकल्पो नामाष्टमोऽध्यायः.",
              "सौम्य = of Soma's nature; पथ्य = wholesome; आग्नेय = of Agni's nature; वैन्ध्य = of the Vindhya; अष्टम = eighth."),
        order(2, "Put the parts of unit 79 in the order of the text.",
              ["सौम्यं पथ्यं च", "तत्राद्यम्", "आग्नेयं वैंध्यमौषधम्", "इति भेषजकल्पो नामाष्टमोऽध्यायः"],
              "First the nature of the first (saumya, pathya), then the Vindhya medicine (āgneya), then the colophon.",
              "सौम्यं पथ्यं च · तत्राद्यम् · आग्नेयं वैंध्यमौषधम् · इति … अध्यायः.",
              role="extend",
              teaches="Verse 79 states the nature of the first region's medicine (saumya, pathya), then the Vindhya medicine (āgneya); the colophon closing chapter eight follows."),
        mcq("discriminate", 3, "Which medicine does verse 79 call āgneya (of Agni's nature)?",
            ("The Vindhya medicine",
             "आग्नेयं वैंध्यमौषधम्: the Vindhya medicine is āgneya."),
            [("The first one", "The first is called saumya and pathya, not āgneya."),
             ("Every medicine alike", "The verse sets the two apart; only the Vindhya one is āgneya."),
             ("The burnt sneha", "Burnt sneha is in verse 77; āgneya is said of the Vindhya medicine.")],
            "आद्यम् → saumya, pathya; वैन्ध्यम् औषधम् → āgneya.",
            "Vindhya medicine = āgneya."),
        mcq("apply", 4,
            "A student must name what verse 79 calls saumya and wholesome. Which is it?",
            ("The first (आद्य) of these",
             "सौम्यं पथ्यं च तत्राद्यम्: among these, the first is saumya and wholesome."),
            [("The Vindhya one", "The Vindhya medicine is called āgneya, not saumya."),
             ("The cikkaṇa sneha", "Cikkaṇa is a kind of cooked sneha (verse 76), not named here."),
             ("The kalka paste", "Kalka is not named in this verse.")],
            "तत्र आद्यम् = among these, the first.",
            "The first = saumya and pathya."),
        mcq("transfer", 5,
            "अष्टमः + अध्यायः gives अष्टमोऽध्यायः. By the same rule, which is right for षष्ठः + अध्यायः?",
            ("षष्ठोऽध्यायः",
             "-अः before अ becomes -ओ and the अ drops, marked ऽ: षष्ठोऽध्यायः."),
            [("षष्ठाध्यायः", "That is अ + अ → आ, which needs षष्ठ without visarga."),
             ("षष्ठ अध्यायः", "The visarga drops with a gap only before vowels other than अ."),
             ("षष्ठरध्यायः", "-ः → र् only after vowels other than अ/आ.")],
            "Same rule as अष्टमः + अध्यायः.",
            "-अः + अ- → -ओऽ.",
            teaches="-अः before अ becomes -ओ and the अ drops (ऽ): अष्टमः + अध्यायः = अष्टमोऽध्यायः; षष्ठः + अध्यायः = षष्ठोऽध्यायः."),
    ],
}

# ---------------------------------------------------------------- unit 80
AUTHORED["80"] = {
    "title": "इति कल्पसिद्धिस्थानं संपूर्णम्",
    "question": "Who composed the work, and which part of it ends here, by the colophon of unit 80?",
    "rule": ("Thus, in the Aṣṭāṅgasaṅgraha composed by the venerable teacher Vāgbhaṭa, son of the venerable Siṃhagupta, "
             "the fifth section, the Kalpasiddhisthāna, is complete."),
    "limits": ("A colophon of the whole fifth part, not a verse or a teaching. It gives the author and his father as the print "
               "says and nothing more. This study calls the part Kalpasthāna for short; the print's title is Kalpasiddhisthāna."),
    "explain_hi": ("यह पूरे पाँचवें स्थान का समापन-वाक्य है, उपदेश नहीं। यह बताता है कि अष्टांगसंग्रह की रचना श्रीमान् वाग्भटाचार्य ने की, "
                   "जो श्रीसिंहगुप्त के पुत्र (सूनु) थे। और इसमें पाँचवाँ कल्पसिद्धिस्थान यहाँ सम्पूर्ण होता है। नाम में कल्प, सिद्धि और "
                   "स्थान तीन भाग हैं; यह अध्ययन इसे संक्षेप में कल्पस्थान कहता है। संधि: विरचिते + अष्टांग = विरचितेऽष्टांग।"),
    "hook": "सिंहगुप्त के पुत्र वाग्भट: पाँचवाँ स्थान पूरा।",
    "core": False,
    "questions": [
        mcq("pretest", 0,
            "By unit 80, who composed the Aṣṭāṅgasaṅgraha?",
            ("Vāgbhaṭa",
             "श्रीमद्वाग्भटाचार्यविरचिते: composed by the venerable teacher Vāgbhaṭa."),
            [("Siṃhagupta", "Siṃhagupta is named as the author's father, not as the author."),
             ("Caraka", "The colophon does not name Caraka."),
             ("Suśruta", "The colophon does not name Suśruta.")],
            "…सूनुश्रीमद्वाग्भटाचार्यविरचिते: composed by Vāgbhaṭa, son of Siṃhagupta.",
            "Composer named: Vāgbhaṭa."),
        match(1, "Match each word of unit 80 to its meaning.",
              [["सूनु", "son"], ["आचार्य", "teacher"], ["विरचित", "composed"], ["पञ्चम", "fifth"],
               ["सम्पूर्ण", "complete"]],
              "श्रीसिंहगुप्तसूनुश्रीमद्वाग्भटाचार्यविरचिते … पंचमं कल्पसिद्धिस्थानं संपूर्णम्.",
              "सूनु = son; आचार्य = teacher; विरचित = composed; पञ्चम = fifth; सम्पूर्ण = complete."),
        order(2, "Put the members of the author's compound in unit 80 in their order.",
              ["श्रीसिंहगुप्त", "सूनु", "श्रीमद्वाग्भट", "आचार्य", "विरचित"],
              "श्रीसिंहगुप्त-सूनु-श्रीमद्वाग्भट-आचार्य-विरचिते: father, son, the name, the title, composed.",
              "सिंहगुप्त · सूनु · वाग्भट · आचार्य · विरचित.",
              role="extend",
              teaches="The compound runs father (Siṃhagupta) · son (sūnu) · Vāgbhaṭa · teacher (ācārya) · composed (viracita): 'composed by the teacher Vāgbhaṭa, son of Siṃhagupta'."),
        mcq("discriminate", 3, "How is Siṃhagupta related to Vāgbhaṭa, by unit 80?",
            ("He is his father",
             "सिंहगुप्त-सूनु: the son (सूनु) of Siṃhagupta is Vāgbhaṭa, so Siṃhagupta is his father."),
            [("He is his son", "सूनु stands after Siṃhagupta: Vāgbhaṭa is the son, not Siṃhagupta."),
             ("He is his pupil", "No pupil is named; सूनु means son."),
             ("He is his teacher", "आचार्य (teacher) is said of Vāgbhaṭa himself.")],
            "X-सूनु = son of X.",
            "Siṃhagupta = father of Vāgbhaṭa."),
        mcq("apply", 4,
            "Which part of the work ends with unit 80, by its own title?",
            ("The fifth, Kalpasiddhisthāna",
             "पंचमं कल्पसिद्धिस्थानं संपूर्णम्: the fifth section, Kalpasiddhisthāna, is complete."),
            [("The eighth, Bheṣajakalpa", "Bheṣajakalpa is the eighth chapter, closed in unit 79."),
             ("The sixth, Kalpasiddhisthāna", "पंचमम् is fifth, not sixth."),
             ("The fifth, Sūtrasthāna", "The title given is Kalpasiddhisthāna.")],
            "पञ्चमम् = fifth; कल्पसिद्धिस्थानम् = the part's name.",
            "Part five = Kalpasiddhisthāna."),
        mcq("transfer", 5,
            "विरचिते + अष्टाङ्ग gives विरचितेऽष्टाङ्ग. By the same rule, which is right for ग्रन्थे + अस्मिन् (in this book)?",
            ("ग्रन्थेऽस्मिन्",
             "After a final ए, an initial अ drops and is shown by ऽ, as in विरचितेऽष्टाङ्ग."),
            [("ग्रन्थास्मिन्", "आ would come from अ + अ; the word ends in ए."),
             ("ग्रन्थैस्मिन्", "ऐ comes from अ + ए, not ए + अ."),
             ("ग्रन्थोऽस्मिन्", "ओ would come from -अः; the word ends in ए, which stays.")],
            "Final ए + अ → एऽ.",
            "Final ए + अ → एऽ (the अ drops).",
            teaches="After a word-final ए an initial अ drops and is written ऽ: विरचिते + अष्टाङ्ग = विरचितेऽष्टाङ्ग; ग्रन्थे + अस्मिन् = ग्रन्थेऽस्मिन्."),
    ],
}

# ---------------------------------------------------------------- unit 81
AUTHORED["81"] = {
    "title": "श्रीकृष्णार्पणमस्तु",
    "question": "What does the closing line of the part say?",
    "rule": "May it be an offering to Śrī Kṛṣṇa: a closing dedication formula.",
    "limits": ("Not a verse and not part of the teaching. It is probably a copyist's or printer's addition; the text itself "
               "does not say who wrote it."),
    "explain_hi": ("यह पूरे भाग के बाद की समर्पण-पंक्ति है: ‘यह श्रीकृष्ण को अर्पण हो’। यह उपदेश का भाग नहीं, सम्भवतः लिपिक या "
                   "मुद्रक का जोड़ा हुआ वाक्य है। संधि: कृष्ण + अर्पणम् = कृष्णार्पणम् (अ + अ → आ); अर्पणम् + अस्तु = अर्पणमस्तु "
                   "(पदान्त म् स्वर से जुड़ता है)। ‘अस्तु’ √अस् का लोट् लकार है: ‘हो’, ‘हो जाए’।"),
    "hook": "अन्त में अर्पण: श्रीकृष्णार्पणमस्तु।",
    "core": False,
    "questions": [
        mcq("pretest", 0,
            "In unit 81, what does अस्तु mean?",
            ("Let it be",
             "अस्तु (3 sg. imp. √अस्) = let it be, may it be."),
            [("It was", "A past form is not used; अस्तु is the imperative."),
             ("It will be", "A future form is not used; अस्तु is the imperative."),
             ("He gives", "No verb of giving is used; अस्तु = let it be.")],
            "श्रीकृष्णार्पणमस्तु: may it be an offering to Śrī Kṛṣṇa.",
            "अस्तु = let it be."),
        match(1, "Match each part of unit 81 to its meaning.",
              [["श्री", "venerable"], ["कृष्ण", "Kṛṣṇa"], ["अर्पण", "offering"], ["अस्तु", "let it be"]],
              "श्री-कृष्ण-अर्पणम् अस्तु: may it be an offering to Śrī Kṛṣṇa.",
              "श्री = venerable; कृष्ण = Kṛṣṇa; अर्पण = offering; अस्तु = let it be."),
        order(2, "Put the parts of unit 81 in their order.",
              ["श्री", "कृष्ण", "अर्पणम्", "अस्तु"],
              "श्री · कृष्ण · अर्पणम् · अस्तु = श्रीकृष्णार्पणमस्तु.",
              "श्री · कृष्ण · अर्पणम् · अस्तु.",
              role="extend",
              teaches="The formula is one compound and a verb: श्री-कृष्ण-अर्पणम् (an offering to Śrī Kṛṣṇa) + अस्तु (let it be)."),
        mcq("discriminate", 3, "Which split is right for कृष्णार्पणम्?",
            ("कृष्ण + अर्पणम्",
             "अ + अ → आ: कृष्ण + अर्पणम् = कृष्णार्पणम्."),
            [("कृष्णः + अर्पणम्", "-अः + अ would give कृष्णोऽर्पणम्."),
             ("कृष्णम् + अर्पणम्", "म् before a vowel would give कृष्णमर्पणम्."),
             ("कृष्णे + अर्पणम्", "ए + अ would give कृष्णेऽर्पणम्.")],
            "कृष्ण (Kṛṣṇa) + अर्पणम् (offering).",
            "अ + अ → आ."),
        mcq("apply", 4,
            "A reader asks what kind of line unit 81 is, by the card. What is the answer?",
            ("A closing dedication",
             "The card: a dedication formula, not a verse and not part of the teaching."),
            [("A rule on sneha", "No rule is given; it is a dedication."),
             ("The chapter title", "The chapter title came in unit 79; this is a dedication."),
             ("The author's name", "The author was named in unit 80; this line names Kṛṣṇa as receiver.")],
            "श्रीकृष्णार्पणमस्तु = may it be an offering to Śrī Kṛṣṇa.",
            "Unit 81 = dedication formula."),
        mcq("transfer", 5,
            "By the pattern of अर्पणमस्तु (= अर्पणम् + अस्तु), what does a new phrase शुभमस्तु mean?",
            ("May it be auspicious",
             "शुभम् + अस्तु: अस्तु = let it be; final म् joins the vowel, as in अर्पणमस्तु."),
            [("It was auspicious", "अस्तु is an imperative, not a past form."),
             ("It will be auspicious", "अस्तु is an imperative, not a future form."),
             ("Offer the auspicious", "No verb of offering is in शुभमस्तु.")],
            "-म् + अस्तु → -मस्तु; अस्तु = let it be.",
            "X-म् अस्तु = may it be X.",
            teaches="अस्तु (imperative of √अस्) means 'let it be'; a final म् joins the next vowel: अर्पणम् + अस्तु = अर्पणमस्तु; शुभम् + अस्तु = शुभमस्तु."),
    ],
}

NOTES_HI = {
    "76": ("विश्वास: मध्यम। पंक्तियाँ ०५.०८.९१-९२। पाठ-चिह्न नहीं। ‘खरचिक्कण’ को ‘कठोर-चिकना’ पढ़ा गया; पाठ इस समास का अर्थ नहीं "
           "बताता। ‘मदन’ = सम्भवतः मोम (probable); यही शब्द एक वृक्ष (मदनफल) और कामदेव का नाम भी है, पर किट्ट की तुलना में "
           "मोम ठीक बैठता है। ‘किट्ट’ = पात्र में बची तलछट; दूसरी पंक्ति के ‘चिक्कणो मदनोपमे’ में भी विषय वही किट्ट। "
           "संधि जाँची: स्नेहपाकस्त्रिधा = स्नेहपाकः + त्रिधा (विसर्ग → स् त से पहले); मंदश्चिक्कणः = मन्दः + चिक्कणः (विसर्ग → श् च से पहले); "
           "चिक्कणो मदनोपमे = चिक्कणः + मदन + उपमे (अः → ओ घोष से पहले; अ + उ → ओ)। छपा ‘मंद’ = मन्द।"),
    "77": ("विश्वास: मध्यम। पंक्तियाँ ०५.०८.९३-९४। ‘पश्चिम’ = तीसरा प्रकार खरचिक्कण (पंक्ति ०५.०८.९१)। ‘सीदति’ वर्तमान काल या "
           "शतृ-प्रत्यय की सप्तमी (सीदति = सीदत् का सप्तमी रूप), दोनों सम्भव; ‘कृष्णे च वर्तमाने’ सप्तमी (‘जब काला हो’)। "
           "छपा ‘वर्त्तमाने’ = वर्तमाने (त्त छपाई की आदत)। खुला प्रश्न (OPEN, ०५.०८.९४): ‘निष्कार्य’ = आग से उतारना या फेंक देना, "
           "पाठ तय नहीं करता; इस पर प्रश्न नहीं। पाठ-चिह्न: ‘स्यादामास्त्वग्निसादकृत्’ में ‘आमाः’ (बहुवचन) अर्थ में नहीं बैठता, "
           "‘आमः’ (कच्चा) अपेक्षित; इसलिए कच्चे स्नेह वाले अन्तिम कथन पर प्रश्न नहीं। अग्निसाद = पाचन-अग्नि का क्षीण होना (मानक शब्द)। "
           "संधि जाँची: दग्धोऽतऊर्ध्वं = दग्धः + अतः + ऊर्ध्वम् (अः + अ → ओऽ; अः + ऊ → अ, बीच में अन्तर)।"),
    "78": ("विश्वास: मध्यम। पंक्तियाँ ०५.०८.९५-९६। पहली पंक्ति में क्रिया अनुक्त। ‘मृदु’ और ‘खर’ पंक्ति ०५.०८.९१ के प्रकार-नाम "
           "(मन्द, खरचिक्कण) नहीं; वही अर्थ हो सकता है, पर कहा नहीं गया। पाठ-चिह्न: छपा ‘व्यासा’ अर्थहीन; ‘व्याप्ता’ (व्याप्त) अनुमान "
           "(‘प्त’ संयुक्ताक्षर ‘स’ छपा, तुलना ०५.०८.६५ का ‘अनुगुसं’); ‘व्यस्ता’ (बँटी हुई) भी सम्भव; इस पर प्रश्न नहीं। "
           "बस्ति = यहाँ एनिमा। संधि जाँची: मृदुर्नस्ये = मृदुः + नस्ये (उः → उर् घोष से पहले); खरोऽभ्यंगे = खरः + अभ्यङ्गे (अः + अ → ओऽ); "
           "हिमवद्विंध्य = हिमवत् + विन्ध्य (त् → द्); प्रायो व्यासा = प्रायः + … (अः → ओ घोष से पहले)। छपा ‘अभ्यंग’ = अभ्यङ्ग, ‘वसुंधरा’ = वसुन्धरा।"),
    "79": ("विश्वास: उच्च। पंक्ति ०५.०८.९७ में क्रिया अनुक्त। ‘आद्य’ = पंक्ति ०५.०८.९६ के दो क्षेत्रों में पहला (हिमवान्), सामान्य क्रम से "
           "पढ़ा गया; पाठ नाम नहीं लेता। सौम्य और आग्नेय की आगे परिभाषा नहीं। पंक्ति ०५.०८.९८ अध्याय का समापन-वाक्य है, श्लोक नहीं; "
           "आरम्भ का ॥ छपाई का चिह्न। ‘औषध’ (नपुंसक) = दवा, ‘ओषधि’ (स्त्रीलिङ्ग, पौधा) से अलग। संधि जाँची: तत्राद्यमाग्नेयं = तत्र + आद्यम् + "
           "आग्नेयम् (अ + आ → आ; म् स्वर से जुड़ा); वैंध्यमौषधं = वैन्ध्यम् + औषधम्; भेषजकल्पोनामाष्टमोऽध्यायः = भेषजकल्पः + नाम + अष्टमः + "
           "अध्यायः (अः → ओ; अ + अ → आ; अः + अ → ओऽ)।"),
    "80": ("विश्वास: उच्च। पंक्ति ०५.०८.९९। पूरे पाँचवें भाग का समापन-वाक्य, श्लोक नहीं; आरम्भ का ॥ छपाई का चिह्न। लेखक वाग्भट "
           "‘आचार्य’ उपाधि के साथ और सिंहगुप्त के पुत्र के रूप में, जैसा छपा है; इससे अधिक कुछ नहीं जोड़ा। छपा नाम ‘कल्पसिद्धिस्थान’ "
           "सम्भवतः इस भाग का मूल नाम है (कल्प और सिद्धि अध्याय एक स्थान में); ‘कल्पस्थान’ इस अध्ययन का संक्षिप्त नाम। "
           "संधि जाँची: श्रीमद्वाग्भट = श्रीमत् + वाग्भट (त् → द्); वाग्भटाचार्य = वाग्भट + आचार्य (अ + आ → आ); विरचितेऽष्टांग = "
           "विरचिते + अष्टाङ्ग (ए + अ → एऽ)। छपा ‘पंचमं’ = पञ्चमम्, ‘संपूर्णम्’ = सम्पूर्णम्।"),
    "81": ("विश्वास: उच्च। पंक्ति ०५.०८.१००। समर्पण-सूत्र, श्लोक नहीं और उपदेश का भाग नहीं; सम्भवतः लिपिक या मुद्रक का जोड़ा हुआ, "
           "पाठ स्वयं नहीं बताता। संधि जाँची: कृष्णार्पणम् = कृष्ण + अर्पणम् (अ + अ → आ); अर्पणमस्तु = अर्पणम् + अस्तु। "
           "‘अस्तु’ = √अस् लोट्, प्रथम पुरुष एकवचन।"),
}

AIDS = {
    "76": {
        "chunks": "स्नेहपाकस्त्रिधा | मंदश्चिक्कणः खरचिक्कणः ‖ मंदः कल्कसमे किट्टे | चिक्कणो मदनोपमे।",
        "chain": {"steps": ["स्नेहपाक: तीन प्रकार", "मन्द: किट्ट कल्क के समान", "चिक्कण: किट्ट मदन (सम्भवतः मोम) के समान",
                            "खरचिक्कण: लक्षण अगले श्लोक में"]},
        "anchors": "त्रिधा = तीन प्रकार · मन्द = हल्का · चिक्कण = चिकना · किट्ट = तलछट · कल्क = लुगदी · मदन = सम्भवतः मोम · -सम/-उपम = के समान।",
        "sandhi": "विसर्ग → स् त से पहले: स्नेहपाकः + त्रिधा → स्नेहपाकस्त्रिधा; विसर्ग → श् च से पहले: मन्दः + चिक्कणः → मन्दश्चिक्कणः।",
    },
    "77": {
        "chain": {"steps": ["मन्द: किट्ट कल्क-समान", "चिक्कण: किट्ट मदन-समान", "पश्चिम (खरचिक्कण): थोड़ा बैठे, काला",
                            "इसके आगे: दग्ध, निकालो"]},
        "anchors": "किंचित् = थोड़ा · सीदति = बैठता है · कृष्ण = काला · पश्चिम = अन्तिम · दग्ध = जला हुआ · अतः ऊर्ध्वम् = इसके आगे।",
        "sandhi": "अः + अ → ओऽ: दग्धः + अतः → दग्धोऽतः; अः + ऊ → अ (बीच में अन्तर): अतः + ऊर्ध्वम् → अत ऊर्ध्वम्।",
        "frame": "श्लोक ७६ और ७७ मिलकर एक सीढ़ी: मन्द, चिक्कण, खरचिक्कण, और उसके बाद दग्ध।",
    },
    "78": {
        "frame": "पहली पंक्ति: कौन-सा पका स्नेह किस प्रयोग में; दूसरी पंक्ति: नया विषय, हिमवान् और विन्ध्य।",
        "chunks": "मृदुर्नस्ये | खरोऽभ्यंगे | पाने बस्तौ च चिक्कणः ‖ हिमवद्विंध्यशैलाभ्यां | प्रायो व्यासा वसुंधरा।",
        "anchors": "नस्य = नाक में डालना · अभ्यंग = मालिश · पान = पीना · बस्ति = एनिमा · शैल = पर्वत · वसुन्धरा = पृथ्वी।",
        "sandhi": "त् → द् घोष व्यंजन से पहले: हिमवत् + विन्ध्य → हिमवद्विन्ध्य; उः → उर्: मृदुः + नस्ये → मृदुर्नस्ये।",
    },
    "79": {
        "contrast": "आद्य (पहला क्षेत्र; सामान्य क्रम से हिमवान्): सौम्य और पथ्य · विन्ध्य की औषध: आग्नेय।",
        "anchors": "सौम्य = सोम स्वभाव वाला · पथ्य = हितकर · आग्नेय = अग्नि स्वभाव वाला · वैन्ध्य = विन्ध्य का · औषध = दवा · अष्टम = आठवाँ।",
        "frame": "पहली पंक्ति दोनों क्षेत्रों की औषध का स्वभाव; दूसरी पंक्ति आठवें अध्याय भेषजकल्प का समापन।",
    },
    "80": {
        "frame": "पूरे पाँचवें स्थान का समापन: रचयिता, उसके पिता, ग्रन्थ का नाम, भाग का नाम।",
        "chunks": "इति | श्रीसिंहगुप्तसूनु- | श्रीमद्वाग्भटाचार्यविरचिते | ऽष्टांगसंग्रहे | पंचमं | कल्पसिद्धिस्थानं | संपूर्णम्।",
        "anchors": "सूनु = पुत्र · आचार्य = गुरु · विरचित = रचा हुआ · पञ्चम = पाँचवाँ · सम्पूर्ण = पूरा।",
    },
    "81": {
        "frame": "समर्पण-पंक्ति, उपदेश नहीं: सब श्रीकृष्ण को अर्पित।",
        "anchors": "श्री = आदरसूचक · अर्पण = भेंट · अस्तु = हो।",
        "sandhi": "अ + अ → आ: कृष्ण + अर्पणम् → कृष्णार्पणम्; म् + स्वर: अर्पणम् + अस्तु → अर्पणमस्तु।",
    },
}

IMAGE_SPECS = {
    ("76", "chain"): {
        "file": "ka8-snehapaka-tridha-76.svg",
        "alt": ("Flowchart of verse 76: sneha-cooking has three kinds, manda, cikkana and khara-cikkana; manda when the residue "
                "is like the kalka paste, cikkana when it is like madana, probably wax"),
        "type": "mermaid",
        "code": ('flowchart TD\n  A["स्नेहपाक: त्रिधा"] --> B["मन्द"]\n  A --> C["चिक्कण"]\n  A --> D["खरचिक्कण"]\n'
                 '  B --> B2["किट्ट कल्क-समान"]\n  C --> C2["किट्ट मदन-समान"]\n'),
    },
    ("77", "chain"): {
        "file": "ka8-paka-dagdha-77.svg",
        "alt": ("Chain of four steps of verses 76 and 77: manda, residue like kalka; cikkana, residue like madana; the last, "
                "khara-cikkana, residue sinks a little and is black; beyond this, burnt, to be taken out"),
        "type": "chain",
        "title": "श्लोक ७६-७७: पाक की सीढ़ी",
        "steps": ["मन्द: किट्ट कल्क-समान", "चिक्कण: किट्ट मदन-समान", "पश्चिम (खरचिक्कण): थोड़ा बैठे, काला",
                  "इसके आगे: दग्ध, निकालो"],
    },
    ("78", "frame"): {
        "file": "ka8-sneha-prayoga-78.svg",
        "alt": ("Table of verse 78: mild cooked sneha for nasya; hard for abhyanga, oil massage; cikkana for drinking and basti, enema"),
        "type": "table",
        "title": "श्लोक ७८: पाक और प्रयोग",
        "heads": ["पाक", "प्रयोग"],
        "rows": [["मृदु", "नस्य (नाक में)"], ["खर", "अभ्यंग (मालिश)"], ["चिक्कण", "पान, बस्ति"]],
    },
    ("79", "contrast"): {
        "file": "ka8-saumya-agneya-79.svg",
        "alt": ("Two columns of verse 79: the first region, by plain order Himavat, its medicine saumya and wholesome; "
                "the Vindhya medicine, agneya"),
        "type": "split",
        "title": "श्लोक ७९: दो क्षेत्रों की औषध",
        "cols": [["आद्य (हिमवान्, क्रम से)", ["सौम्य", "पथ्य"]],
                 ["विन्ध्य की औषध", ["आग्नेय"]]],
    },
}
