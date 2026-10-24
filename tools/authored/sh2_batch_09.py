from helpers import mcq, match, order, fill, multi, accepts


def T(q, teaches):
    q["teaches"] = teaches
    return q


AUTHORED = {}

# ---------------------------------------------------------------- unit 101
AUTHORED["101"] = {
    "title": "अपिच",
    "question": "What does the printed formula अपिच of unit 101 mean, and how does it split?",
    "rule": ("अपिच = अपि (also) + च (and): 'moreover, and also', a formula that opens a further point. "
             "The two words are only written together; no sound changes."),
    "limits": ("The unit is the formula alone and states no content of its own; what it opens is said in the next unit, "
               "not here."),
    "explain_hi": ("यह इकाई केवल एक सूत्र-शब्द है: ‘अपिच’, यानी अपि (भी) + च (और), अर्थ ‘और भी’, ‘इसके अलावा’। "
                   "ऐसा शब्द एक नई बात शुरू करता है; वह बात इस इकाई में नहीं है। "
                   "छपाई में दोनों शब्द जुड़े लिखे हैं, पर कोई ध्वनि नहीं बदलती: अपि की इ और च के बीच कोई सन्धि-विकार नहीं। "
                   "यह गद्य है, श्लोक नहीं।"),
    "hook": "अपि + च = और भी: अब एक और बात।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "What does the formula अपिच of unit 101 mean?",
            ("Moreover, and also", "अपि = also, च = and: together, moreover."),
            [("Therefore, hence", "Therefore is तस्मात्, as in unit 104."),
             ("Namely, as follows", "Namely is तद्यथा, as in unit 107."),
             ("In brief, in short", "In brief is समासतः, as in unit 109.")],
            "अपि च = and also, moreover: a formula that opens a further point.",
            "अपि च = moreover."),
        order(1, "Put the steps of reading the printed अपिच in order.",
              ["printed: अपिच", "split: अपि + च", "अपि = also, च = and", "sense: moreover, and also"],
              "The printed word is split into its two words, each word is glossed, and the two glosses give the sense.",
              "अपिच → अपि + च → also + and → moreover."),
        fill(2, "The printed अपिच splits into ____ + च. Type the first word in Devanagari or in English letters (e.g. dharma).",
             accepts("अपि"),
             "अपि (also) + च (and) → अपिच, written together with no change.",
             "अपि means also, even; with च it makes 'and also, moreover'.",
             "अपि + च → अपिच."),
        mcq("discriminate", 3, "Which split of the printed अपिच is right?",
            ("अपि + च", "Both words keep their sounds; they are only written together."),
            [("अपिः + च", "A visarga before च would give अपिश्च."),
             ("अपी + च", "A long ई would show in print as अपीच."),
             ("अप् + इच", "इच is not a word; the card gives अपि and च.")],
            "अपि (also) + च (and), with no sandhi change.",
            "इ + च: no change."),
        multi("apply", 4, "Which two are right about unit 101, by the card?",
              [("It is a metrical verse (śloka)", "No: the unit is prose, one formula."),
               ("No sound changes when अपि and च are joined", "Right: अपि + च → अपिच, only written together."),
               ("It contains a verb", "No verb is printed; the unit is one formula."),
               ("It means moreover, and also", "Right: अपि (also) + च (and).")],
              [1, 3],
              "Unit 101 is the prose formula अपि च, moreover, written as one word without any change.",
              "अपि च = moreover; no sandhi change."),
        T(mcq("transfer", 5, "In an invented line अपि च बालो गच्छति, what do the opening words add?",
              ("Moreover, the boy goes", "अपि च at the head adds a further point: moreover."),
              [("Therefore, the boy goes", "Therefore would need तस्मात्."),
               ("Namely, the boy goes", "Namely would need तद्यथा."),
               ("The boy does not go", "No न is printed; nothing is denied.")],
              "अपि च opens a further point: moreover, the boy goes.",
              "अपि च + sentence = moreover, ..."),
          "अपि च at the head of a sentence adds a further point: moreover."),
    ],
}

# ---------------------------------------------------------------- unit 102
AUTHORED["102"] = {
    "title": "दृष्टिभागमप्रतिपन्नं तेजो जात्यंधत्वं",
    "question": "What does unit 102 call congenital blindness, and what eyes go with each of its four companions?",
    "rule": ("Tejas (light, fire) that has not reached the share of sight (dṛṣṭibhāga) is congenital blindness. "
             "Followed by Vāta: deformed, dry, reddish eyes; by Pitta: tawny; by Kapha: white; by rakta: red."),
    "limits": ("The line does not say 'in the eye'; tejas gets no elemental sense here. rakta may be blood or redness. "
               "The joined print श्लेष्माऽनुगतंशुक्लाक्षं (possibly a missing space) carries no sandhi question. "
               "No further cause or treatment is given."),
    "explain_hi": ("यह गद्य-पंक्ति जन्मजात अन्धेपन (जात्यन्धत्व) की परिभाषा देती है: तेज (प्रकाश, अग्नि) जो दृष्टि के भाग (दृष्टिभाग) तक नहीं पहुँचा। "
                   "फिर वही अन्धापन चार साथियों के साथ बताया गया है: वात से अनुगत हो तो आँख विकृत, रूखी और अरुण; "
                   "पित्त से अनुगत हो तो पिंगल; कफ (श्लेष्मा) से अनुगत हो तो सफ़ेद; रक्त से अनुगत हो तो लाल। "
                   "पंक्ति ‘आँख में’ नहीं कहती, और ‘तेज’ का महाभूत वाला अर्थ यहाँ लागू नहीं किया गया। "
                   "‘रक्त’ का अर्थ खून या लालिमा हो सकता है; डेटा ‘खून’ लेता है।"),
    "hook": "तेज दृष्टि तक न पहुँचा तो जन्म से अन्धा; वात, पित्त, कफ, रक्त: हर एक की अपनी आँख।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 102, what is congenital blindness (jātyandhatva)?",
            ("Tejas that has not reached the share of sight", "दृष्टिभागमप्रतिपन्नं तेजो जात्यंधत्वं."),
            [("Vāta that has dried up the share of sight", "Vāta only gives one kind of it; it is not the definition."),
             ("Blood that has filled up the share of sight", "Blood (rakta) only gives one kind: red eyes."),
             ("Kapha that has covered the share of sight", "Kapha only gives one kind: white eyes.")],
            "Tejas (light, fire) not reaching the share of sight is congenital blindness.",
            "अप्रतिपन्नं तेजः = जात्यन्धत्व."),
        match(1, "Match each companion of the blindness in unit 102 to the eyes it gives.",
              [["वातानुगत", "deformed, dry, reddish eyes"], ["पित्तानुगत", "tawny eyes"],
               ["श्लेष्माऽनुगत", "white eyes"], ["रक्तानुगत", "red eyes"]],
              "Vāta: विकृतरूक्षारुणाक्ष; Pitta: पिंगाक्ष; Kapha: शुक्लाक्ष; rakta: रक्ताक्ष.",
              "Each companion gives its own eyes."),
        order(2, "Put the four companions of the blindness in the order of unit 102.",
              ["वात", "पित्त", "श्लेष्मा (कफ)", "रक्त"],
              "The line runs वातानुगतं …, पित्तानुगतं …, श्लेष्माऽनुगतं …, रक्तानुगतं ….",
              "वात → पित्त → कफ → रक्त.", role="extend",
              teaches="The unit runs Vāta, Pitta, Kapha, then rakta, each with its own eyes."),
        mcq("discriminate", 3, "Why is तेजः printed as तेजो before जात्यंधत्वं?",
            ("अः before a voiced sound becomes ओ", "ज is voiced: तेजः + जात्य… → तेजो जात्य…."),
            [("तेजो is a separate dual form", "The card gives तेजः, n. nom. sg.; the ओ is sandhi."),
             ("Visarga becomes ओ before any sound", "Before a voiceless त it would become स्, not ओ."),
             ("A letter is lost in the print", "This is regular sandhi, not a loss in print.")],
            "तेजः (n. nom. sg.) + जात्यंधत्वं: अः before voiced ज → ओ.",
            "अः + voiced consonant → ओ."),
        mcq("apply", 4, "Someone is blind from birth and has tawny eyes. By unit 102, which companion is it?",
            ("Pitta", "पित्तानुगतं पिंगाक्षं: with Pitta, tawny eyes."),
            [("Vāta", "Vāta gives deformed, dry, reddish eyes."),
             ("Kapha", "Kapha gives white eyes."),
             ("Rakta", "Rakta gives red eyes.")],
            "Tawny eyes (पिंगाक्ष) go with Pitta in this line.",
            "पित्तानुगत → पिंगाक्ष."),
        T(mcq("transfer", 5, "By the pattern of पिंगाक्षं (पिङ्ग + अक्षम्), how is नील + अक्षम् joined?",
              ("नीलाक्षम्", "अ + अ → आ, as in पिङ्ग + अक्षम् → पिङ्गाक्षम्."),
              [("नीलक्षम्", "The two अ merge into one long आ; none is lost."),
               ("नीलेक्षम्", "अ + अ does not give ए."),
               ("नीलोक्षम्", "अ + अ does not give ओ.")],
              "पिङ्ग + अक्षम् → पिङ्गाक्षम्; so नील + अक्षम् → नीलाक्षम्, having dark-blue eyes.",
              "अ + अ → आ."),
          "अ + अ → आ; X + अक्ष as a bahuvrīhi means 'having X eyes'."),
    ],
}

# ---------------------------------------------------------------- unit 103
AUTHORED["103"] = {
    "title": "गर्भसमानयोगक्षेमा हि गर्भिणी",
    "question": "What does unit 103 say about the pregnant woman's welfare (yogakṣema)?",
    "rule": ("For the pregnant woman has the same welfare (yogakṣema) as the embryo. गर्भसमानयोगक्षेमा is a bahuvrīhi "
             "qualifying गर्भिणी; हि (for) gives this as a reason."),
    "limits": ("The unit gives only the reason (हि, for); it draws no conclusion itself and names no regimen. "
               "योगक्षेम, literally attainment and preservation, is read as welfare."),
    "explain_hi": ("यह छोटी गद्य-पंक्ति एक कारण बताती है: गर्भिणी का योगक्षेम (कल्याण) गर्भ के समान होता है। "
                   "‘योगक्षेम’ का शाब्दिक अर्थ है प्राप्ति और रक्षा; यहाँ इसे ‘कल्याण’ पढ़ा गया है। "
                   "‘गर्भसमानयोगक्षेमा’ बहुव्रीहि समास है: जिसका योगक्षेम गर्भ के समान है; स्त्रीलिंग होकर यह ‘गर्भिणी’ का विशेषण है। "
                   "‘हि’ (क्योंकि) बताता है कि यह किसी बात का कारण है; निष्कर्ष इस इकाई में नहीं है।"),
    "hook": "गर्भ का भला, वही माँ का भला: एक ही योगक्षेम।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 103, the pregnant woman has the same welfare as whom?",
            ("The embryo", "गर्भसमानयोगक्षेमा: the same welfare as the embryo."),
            [("Her husband", "No husband is named in this line."),
             ("Her mother", "No mother of hers is named here."),
             ("The physician", "No physician is named here.")],
            "Her welfare (योगक्षेम) is the same as the embryo's.",
            "गर्भ-समान-योगक्षेमा."),
        order(1, "Put the four words of unit 103 in their printed order.",
              ["गर्भसमानयोगक्षेमा", "हि", "गर्भिणी", "भवति"],
              "Same-welfare-as-the-embryo, for, the pregnant woman, is.",
              "गर्भसमानयोगक्षेमा → हि → गर्भिणी → भवति."),
        match(2, "Match each part of unit 103 to its meaning on the card.",
              [["गर्भ", "embryo"], ["समान", "same"], ["योगक्षेम", "welfare (attainment and preservation)"],
               ["हि", "for, because"], ["भवति", "is"]],
              "The compound गर्भ-समान-योगक्षेमा and the words हि, भवति make the whole line.",
              "गर्भ = embryo; समान = same; योगक्षेम = welfare; हि = for; भवति = is.", role="extend",
              teaches="योगक्षेम = योग (attainment) + क्षेम (preservation), read here as welfare."),
        mcq("discriminate", 3, "Why does गर्भसमानयोगक्षेमा end in -आ?",
            ("It is a bahuvrīhi agreeing with गर्भिणी", "As a bahuvrīhi it takes the gender of गर्भिणी: f. nom. sg."),
            [("It is a plural ending of the compound", "The card gives f. nom. sg., not a plural."),
             ("It is an ablative ending meaning from", "The card gives nom. sg.; nothing means from here."),
             ("It names the embryo as a feminine word", "गर्भ is masculine; the -आ form describes the woman.")],
            "A bahuvrīhi describes another word and takes its gender: here feminine, for गर्भिणी.",
            "Bahuvrīhi agrees with the word it qualifies."),
        mcq("apply", 4, "Which English of unit 103 is right?",
            ("For the pregnant woman has the same welfare as the embryo",
             "हि = for; समान = same; योगक्षेम = welfare."),
            [("For the embryo has more welfare than the pregnant woman", "समान means same, not more."),
             ("So the pregnant woman has the same welfare as the embryo", "हि means for, giving a reason, not so."),
             ("For the pregnant woman has a welfare unlike the embryo's", "समान means same, not unlike.")],
            "हि (for) + समान (same) + योगक्षेम (welfare): she shares the embryo's welfare.",
            "गर्भसमानयोगक्षेमा हि = for (she) has the same welfare as the embryo."),
        T(mcq("transfer", 5, "Built like गर्भसमानयोगक्षेमा गर्भिणी, what does an invented पितृसमानबला कन्या mean?",
              ("A girl whose strength equals a father's", "A bahuvrīhi: पितृ + समान + बल, made feminine to agree with कन्या."),
              [("A girl who equals a father in age", "बल is strength, not age."),
               ("A father who is as strong as a girl", "The compound qualifies कन्या; the girl is the one described."),
               ("A girl who gives strength to a father", "समान means same, equal; nothing means giving.")],
              "X-समान-Y-आ + a feminine noun = (she) whose Y is the same as X's.",
              "Bahuvrīhi X-समान-Y = having Y the same as X."),
          "A bahuvrīhi such as X-समान-Y describes a noun whose Y equals X's, and takes that noun's gender."),
    ],
}

# ---------------------------------------------------------------- unit 104
AUTHORED["104"] = {
    "title": "तस्माद्विशेषतस्तां रक्षेत्",
    "question": "By unit 104, from what, and by what, should she be protected?",
    "rule": ("Therefore one should protect her especially, by the pleasant and the beneficial (priya, hita), from the "
             "things that cause injury to the embryo (garbhopaghātakara)."),
    "limits": ("प्रियहिताभ्याम् gives only 'by the pleasant and the beneficial'; the nouns are not in the text. The harmful "
               "things are not listed here. The endings -भ्याम् and -भ्यः serve more than one case, so no question asks the "
               "case; the card follows the data (instrumental dual, ablative plural)."),
    "explain_hi": ("‘तस्मात्’ (इसलिए) से निष्कर्ष आता है: उसकी (गर्भिणी की, जो पिछली इकाई से समझी जाती है) विशेष रूप से रक्षा करनी चाहिए। "
                   "रक्षा किससे: गर्भ को हानि पहुँचाने वालों (गर्भोपघातकर) से। "
                   "रक्षा किस साधन से: ‘प्रियहिताभ्याम्’, प्रिय और हितकर (चीज़ों) से; संज्ञाएँ पाठ में नहीं हैं। "
                   "‘रक्षेत्’ विधिलिङ् है: रक्षा करे, करनी चाहिए। "
                   "हानिकारक चीज़ों की सूची इस इकाई में नहीं दी गई।"),
    "hook": "इसलिए: प्रिय और हित के साथ, गर्भ-घातकों से उसकी रक्षा।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 104, from what should she be protected?",
            ("From things that injure the embryo", "गर्भोपघातकरेभ्यः: from those causing injury to the embryo."),
            [("From her own family and friends", "No family or friends are named in this line."),
             ("From the cold and the strong wind", "Cold and wind are not named in this line."),
             ("From all kinds of food and drink", "No food or drink is named in this line.")],
            "She is guarded from what injures the embryo, by what is pleasant and beneficial.",
            "गर्भोपघातकरेभ्यो रक्षेत्."),
        order(1, "Put the printed parts of unit 104 in their order.",
              ["तस्माद्विशेषतस्तां", "प्रियहिताभ्यां", "गर्भोपघातकरेभ्यो", "रक्षेत्"],
              "Therefore especially her, by the pleasant and beneficial, from the embryo-injuring (things), should protect.",
              "तस्माद्विशेषतस्तां → प्रियहिताभ्यां → गर्भोपघातकरेभ्यो → रक्षेत्."),
        match(2, "Match each word of unit 104 to its meaning on the card.",
              [["तस्मात्", "therefore"], ["विशेषतः", "especially"], ["ताम्", "her"],
               ["प्रियहित", "pleasant and beneficial"], ["रक्षेत्", "should protect"]],
              "These words carry the conclusion: therefore, especially, her, by the pleasant and beneficial, should protect.",
              "तस्मात्, विशेषतः, ताम्, प्रियहित, रक्षेत्.", role="extend",
              teaches="One act, रक्षेत्, has both a means (प्रियहित) and a danger to guard against (गर्भोपघातकर)."),
        mcq("discriminate", 3, "Which split of तस्माद्विशेषतस्तां is right?",
            ("तस्मात् + विशेषतः + ताम्", "त् → द् before voiced व; ः → स् before त; म् → ं before प."),
            [("तस्मा + द्विशेषतः + ताम्", "तस्मा and द्विशेषतः are not the card's words."),
             ("तस्मात् + विशेषतः + ताः", "ताः is plural and would not give तां; the card gives ताम्, her."),
             ("तस्मात् + विशेष + तस्ताम्", "तस्ताम् is not a word.")],
            "तस्मात् (therefore) + विशेषतः (especially) + ताम् (her).",
            "त् + voiced → द्; ः + त → स्त; final म् → ं before a consonant."),
        mcq("apply", 4, "What does the verb रक्षेत् of unit 104 express?",
            ("One should protect (optative)", "The card gives 3 sg. optative: should protect."),
            [("One protects (plain present)", "The present would be रक्षति."),
             ("One protected (a past)", "No past form is printed."),
             ("One will protect (future)", "The future would be रक्षिष्यति.")],
            "रक्षेत् is an optative: an instruction, should protect.",
            "-एत् = optative, should."),
        T(mcq("transfer", 5, "By the rule of तस्माद्विशेषतः, how is तस्मात् + भवति written when joined?",
              ("तस्माद्भवति", "त् before the voiced भ becomes द्."),
              [("तस्मात्भवति", "Before a voiced sound the त् cannot stay."),
               ("तस्मान्भवति", "भ is not a nasal, so त् does not become न्."),
               ("तस्माच्भवति", "त् becomes च् before a palatal such as च, not before भ.")],
              "तस्मात् + विशेषतः → तस्माद्विशेषतः; so तस्मात् + भवति → तस्माद्भवति.",
              "त् + voiced consonant → द्."),
          "A final त् becomes द् before a voiced sound: तस्माद्विशेषतः, तस्माद्भवति."),
    ],
}

# ---------------------------------------------------------------- unit 105
AUTHORED["105"] = {
    "title": "यथा यथा च गर्भो वृद्धिमाप्नोति",
    "question": "By unit 105, what happens to the woman as the embryo grows?",
    "rule": ("As the embryo grows, so, in the same measure, the woman's strength wanes (balakṣaya). "
             "यथा यथा … तथा तथा = as … so."),
    "limits": ("Low confidence. The printed भाराहारसापचाराच्च is unclear: 'from burden, food and error' is only a conjecture "
               "(the सा is unexplained), so no question rests on these causes. No remedy is given here."),
    "explain_hi": ("यह गद्य-पंक्ति एक अनुपात बताती है: जैसे-जैसे गर्भ वृद्धि पाता है, वैसे-वैसे स्त्री के बल का क्षय होता है। "
                   "‘यथा यथा … तथा तथा’ का अर्थ है ‘जैसे-जैसे … वैसे-वैसे’। "
                   "बीच का छपा अंश ‘भाराहारसापचाराच्च’ अस्पष्ट है: ‘सा’ का अर्थ नहीं बैठता, इसलिए ‘भार, आहार और अपचार से’ केवल अनुमानित पाठ है। "
                   "इसी कारण विश्वास कम है, और कारणों पर कोई प्रश्न नहीं बनाया गया। "
                   "‘स्त्रियाः’ का विसर्ग घोष ‘ब’ से पहले गिरा है: स्त्रिया बलक्षयः।"),
    "hook": "गर्भ बढ़े, माँ का बल घटे: जैसे-जैसे, वैसे-वैसे।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 105, what happens to the woman as the embryo grows?",
            ("Her strength wanes", "स्त्रियाः बलक्षयः: loss of the woman's strength."),
            [("Her strength grows", "क्षय is loss, not growth."),
             ("Her appetite stops", "Appetite is not named in this line."),
             ("Her sleep deepens", "Sleep is not named in this line.")],
            "As the embryo grows, the woman's strength wanes.",
            "वृद्धि (of the embryo) ↔ बलक्षय (of the woman)."),
        order(1, "Put the sure parts of unit 105 in their printed order.",
              ["यथा यथा च", "गर्भो वृद्धिमाप्नोति", "तथा तथा", "स्त्रियाबलक्षयः"],
              "As … the embryo grows … so … the woman's loss of strength (the unclear token stands before the last part).",
              "यथा यथा च → गर्भो वृद्धिमाप्नोति → तथा तथा → स्त्रियाबलक्षयः."),
        match(2, "Match each part of unit 105 to its meaning on the card.",
              [["यथा यथा", "as (more and more)"], ["तथा तथा", "so (in the same measure)"], ["वृद्धि", "growth"],
               ["आप्नोति", "reaches, attains"], ["बलक्षय", "loss of strength"]],
              "The frame pairs two changes: the embryo's growth and the woman's loss of strength.",
              "यथा यथा … तथा तथा = as … so.", role="extend",
              teaches="यथा यथा … तथा तथा ties two changes that go together: as one grows, so the other."),
        mcq("discriminate", 3, "Why is स्त्रियाः printed as स्त्रिया before बलक्षयः?",
            ("आः drops its visarga before a voiced sound", "ब is voiced: स्त्रियाः + बल… → स्त्रिया बल…."),
            [("आः becomes ओ before a voiced sound", "ओ comes from अः, not from आः."),
             ("The visarga becomes स् before the ब", "स् comes before त or थ, not before ब."),
             ("A letter has been lost from the print here", "The note calls it regular sandhi.")],
            "स्त्रियाः (of the woman) before voiced ब loses its visarga.",
            "आः + voiced consonant → आ."),
        multi("apply", 4, "Which two does unit 105 state plainly, by the card?",
              [("As the embryo grows, the woman's strength wanes", "Right: गर्भो वृद्धिमाप्नोति … स्त्रिया बलक्षयः."),
               ("The causes in भाराहारसापचारात् are a firm reading", "No: that token is unclear; the causes are a conjecture."),
               ("यथा यथा … तथा तथा means as … so", "Right: the frame of the line."),
               ("A remedy for the loss is given", "No remedy is named in this line.")],
              [0, 2],
              "The sure content: as the embryo grows, so the woman's strength wanes.",
              "यथा यथा … तथा तथा; बलक्षय."),
        T(mcq("transfer", 5, "Built like unit 105, what does an invented यथा यथा वृक्षो वर्धते तथा तथा छाया वर्धते mean?",
              ("As the tree grows, so the shade grows", "यथा यथा … तथा तथा pairs two changes: as … so."),
              [("The tree grows because the shade grows", "The frame pairs two changes; it does not say because."),
               ("As the tree grows, so the shade wanes", "वर्धते (grows) stands in both halves."),
               ("Neither the tree nor the shade grows", "No न is printed; nothing is denied.")],
              "यथा यथा X … तथा तथा Y = as X, so Y.",
              "यथा यथा … तथा तथा = as … so."),
          "यथा यथा … तथा तथा pairs two changes that go together: as one, so the other."),
    ],
}

# ---------------------------------------------------------------- unit 106
AUTHORED["106"] = {
    "title": "तत्रेमे गर्भोपघातकराः",
    "question": "What does unit 106 announce?",
    "rule": ("In this matter, these are the (things) that cause injury to the embryo (garbhopaghātakara). "
             "The predicate 'are' is understood."),
    "limits": ("The unit only announces; it names none of the harmful things itself: per the data, तद्यथा (unit 107) and the list "
               "of unit 108 follow as one statement. No verb is printed."),
    "explain_hi": ("यह छोटी गद्य-पंक्ति घोषणा करती है: इस विषय में ये गर्भ को हानि पहुँचाने वाले (गर्भोपघातकर) हैं। "
                   "‘हैं’ क्रिया पाठ में नहीं, समझी गई है। "
                   "‘गर्भोपघातकराः’ = गर्भ + उपघात (चोट, हानि) + कर (करने वाला), पुंल्लिंग बहुवचन। "
                   "सन्धियाँ: तत्र + इमे → तत्रेमे (अ + इ → ए); गर्भ + उपघात → गर्भोपघात (अ + उ → ओ)। "
                   "हानिकारक चीज़ों के नाम इस इकाई में नहीं हैं।"),
    "hook": "तत्र इमे: ये रहे गर्भ के घातक।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 106, what are इमे (these)?",
            ("Things causing injury to the embryo", "गर्भोपघातकराः: causers of injury to the embryo."),
            [("Things helping the embryo to grow", "उपघात is injury, not help."),
             ("Signs that the embryo is a male", "No such signs are named here."),
             ("The months of the pregnancy", "No months are named here.")],
            "These are the causes of injury to the embryo.",
            "गर्भ + उपघात + कर = causing injury to the embryo."),
        match(1, "Match each word of unit 106 to its meaning on the card.",
              [["तत्र", "in this matter, there"], ["इमे", "these"], ["गर्भ", "embryo"], ["उपघात", "injury"],
               ["कर", "causing"]],
              "In this matter, these are the embryo-injury-causing (things).",
              "तत्र, इमे, गर्भ, उपघात, कर."),
        order(2, "Put the members of गर्भोपघातकराः in their order.",
              ["गर्भ", "उपघात", "कराः"],
              "गर्भ (embryo) + उपघात (injury) + कराः (causing).",
              "गर्भ → उपघात → कराः.", role="extend",
              teaches="Such a compound is read from its last member back: causers (कर) of injury (उपघात) to the embryo (गर्भ)."),
        mcq("discriminate", 3, "Which split of तत्रेमे is right?",
            ("तत्र + इमे", "अ + इ → ए."),
            [("तत्रे + मे", "तत्रे is not a word; मे would mean to me."),
             ("तत्र + एमे", "एमे is not a word; the card gives इमे."),
             ("तत्रः + इमे", "A visarga before इ would drop and leave तत्र इमे, with no ए.")],
            "तत्र (in this matter) + इमे (these): अ + इ → ए.",
            "अ + इ → ए."),
        mcq("apply", 4, "Which English of तत्रेमे गर्भोपघातकराः is right?",
            ("In this matter, these cause injury to the embryo", "तत्र = in this matter; इमे = these; गर्भोपघातकराः = causing injury to the embryo."),
            [("In this matter, these guard the embryo from injury", "कर means causing, not guarding."),
             ("In this matter, these cause injury to the mother", "गर्भ is the embryo, not the mother."),
             ("Then these were the causes of the embryo's growth", "No past is printed, and उपघात is injury.")],
            "In this matter (तत्र), these (इमे) are the causes of injury to the embryo.",
            "तत्र इमे … = in this matter, these are …."),
        T(mcq("transfer", 5, "By the rule of गर्भोपघात (अ + उ → ओ), how is सूर्य + उदयः joined?",
              ("सूर्योदयः", "अ + उ → ओ, as in गर्भ + उपघात → गर्भोपघात."),
              [("सूर्यौदयः", "औ comes from अ + ओ or औ, not from अ + उ."),
               ("सूर्युदयः", "The अ is not simply lost before उ."),
               ("सूर्येदयः", "ए comes from अ + इ, not from अ + उ.")],
              "गर्भ + उपघात → गर्भोपघात; so सूर्य + उदयः → सूर्योदयः.",
              "अ + उ → ओ."),
          "A final अ and an initial उ merge into ओ."),
    ],
}

# ---------------------------------------------------------------- unit 107
AUTHORED["107"] = {
    "title": "तद्यथा",
    "question": "What does the formula तद्यथा of unit 107 mean, and how is it joined?",
    "rule": "तद्यथा = तत् + यथा, 'namely': a stock formula that opens a list. त् becomes द् before the voiced य.",
    "limits": "The formula alone; it names no item. The list itself is given in the following unit, not here.",
    "explain_hi": ("‘तद्यथा’ एक स्थिर सूत्र है: ‘जैसे कि’, ‘अर्थात्’; इसके बाद गिनती आती है। "
                   "रचना: तत् (वह) + यथा (जैसे); त् घोष अक्षर य से पहले द् हो जाता है। "
                   "इस इकाई में कोई वस्तु गिनाई नहीं गई। यह गद्य है।"),
    "hook": "तद्यथा: अब गिनती सुनो।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "What does तद्यथा of unit 107 mean?",
            ("Namely", "तत् + यथा: that, as, i.e. namely."),
            [("Likewise", "Likewise is तथा, as in unit 110."),
             ("Moreover", "Moreover is अपि च, as in unit 101."),
             ("Therefore", "Therefore is तस्मात्, as in unit 104.")],
            "तद्यथा = namely: it opens a list.",
            "तद्यथा = namely."),
        match(1, "Match each piece to its meaning on the card.",
              [["तत्", "that"], ["यथा", "as"], ["तद्यथा", "namely"]],
              "तत् (that) + यथा (as) make the formula तद्यथा, namely.",
              "तत् + यथा = तद्यथा, namely."),
        order(2, "Put the steps that make तद्यथा in order.",
              ["तत् + यथा", "य is a voiced sound", "त् becomes द्", "तद्यथा"],
              "The two words meet; य is voiced; the त् turns into द्; the joined form results.",
              "तत् + यथा → voiced य → द् → तद्यथा.", role="extend",
              teaches="A final त् turns into द् before a voiced sound such as य."),
        mcq("discriminate", 3, "Which split of तद्यथा is right?",
            ("तत् + यथा", "त् before the voiced य becomes द्."),
            [("तदा + यथा", "तदा + यथा would stay तदा यथा."),
             ("तद् + अयथा", "That would join as तदयथा."),
             ("तः + द्यथा", "तः and द्यथा are not words.")],
            "तत् (that) + यथा (as).",
            "त् + voiced consonant → द्."),
        multi("apply", 4, "Which two are right about unit 107, by the card?",
              [("It names the first item of a list", "No: it names no item; it only opens the list."),
               ("It is a stock formula meaning namely", "Right: तत् + यथा, namely."),
               ("Its द् comes from त् before य", "Right: त् + voiced य → द्."),
               ("It is a metrical verse line", "No: the unit is prose.")],
              [1, 2],
              "तद्यथा is a prose formula, namely, joined as तत् + यथा.",
              "तद्यथा = तत् + यथा = namely."),
        T(mcq("transfer", 5, "By the rule of तद्यथा, how is तत् + गृहम् written when joined?",
              ("तद्गृहम्", "त् before the voiced ग becomes द्."),
              [("तत्गृहम्", "Before a voiced sound the त् cannot stay."),
               ("तच्गृहम्", "त् becomes च् before a palatal such as च, not before ग."),
               ("तन्गृहम्", "ग is not a nasal, so त् does not become न्.")],
              "तत् + यथा → तद्यथा; so तत् + गृहम् → तद्गृहम्.",
              "त् + voiced consonant → द्."),
          "A final त् becomes द् before a voiced sound: तद्यथा, तद्गृहम्."),
    ],
}

# ---------------------------------------------------------------- unit 108
AUTHORED["108"] = {
    "title": "व्यवायव्यायामकर्शनाभिघात",
    "question": "Which things does unit 108 list, and how is the list closed?",
    "rule": ("A long list, closed by आदयः (and so on): among them intercourse (vyavāya), exertion, emaciating (things), "
             "blows, day sleep, holding back urges, undigested (ajīrṇa), sun-heat, fire, grief, fear, fasting, falls, "
             "disagreeable sights and sounds."),
    "limits": ("रात्रि is read across a stray space; the doubled यान is dropped; क्रोध corrects printed क्रोघ; उत्कटक "
               "(squatting) is probable: no question rests on these. vyavāya = intercourse (standard). आदयः leaves the "
               "list open. Per the data it appears to complete units 106-107 (things that injure the embryo)."),
    "explain_hi": ("यह इकाई एक लम्बी सूची है, एक बड़े द्वन्द्व समास के रूप में, जो ‘आदयः’ (आदि) से खुली छोड़ी गई है। "
                   "छपे क्रम में: व्यवाय (मैथुन), व्यायाम, कर्शन (दुबला करने वाला), अभिघात (चोट), अत्यधिक झटके देने वाली सवारी, "
                   "रात में जागना, दिन में सोना, वेगों को रोकना, अजीर्ण, धूप, आग, क्रोध, शोक, भय, घबराहट, उपवास, "
                   "उत्कटक (सम्भवतः उकड़ूँ बैठना), ऊबड़-खाबड़ और कठोर आसन, गड्ढे और कुएँ में गिरना, अप्रिय देखना और सुनना। "
                   "‘क्रोध’ छपे ‘क्रोघ’ का सुधार है; ‘रात्रि’ एक बीच की खाली जगह के पार पढ़ा गया है; छपा दोहरा ‘यान’ एक बार गिना गया। "
                   "यह गद्य है।"),
    "hook": "मैथुन से लेकर अप्रिय देखने-सुनने तक: एक लम्बी, खुली सूची।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "Which of these does unit 108 name in its list?",
            ("Sleep by day (दिवास्वप्न)", "दिवास्वप्न is in the printed list."),
            [("Drinking warm milk at night", "Milk is not named in this line."),
             ("Wearing red garments (वासांसि)", "Red garments come in unit 111, not in this line."),
             ("Bathing in cold water", "Bathing is not named in this line.")],
            "Day sleep stands in the list, after night waking and before holding back urges.",
            "दिवास्वप्न = sleep by day."),
        match(1, "Match each item of unit 108 to its meaning on the card.",
              [["व्यवाय", "sexual intercourse"], ["व्यायाम", "exertion"], ["अभिघात", "blow, injury"],
               ["वेगविधारण", "holding back urges"], ["उपवास", "fasting"]],
              "Five sure items of the list with their meanings.",
              "व्यवाय, व्यायाम, अभिघात, वेगविधारण, उपवास."),
        order(2, "Put these first four items of unit 108 in their printed order.",
              ["व्यवाय", "व्यायाम", "कर्शन", "अभिघात"],
              "The print opens व्यवायव्यायामकर्शनाभिघात…: intercourse, exertion, emaciating, blows.",
              "व्यवाय → व्यायाम → कर्शन → अभिघात.", role="extend",
              teaches="The list opens with intercourse and exertion, then emaciating (things) and blows."),
        mcq("discriminate", 3, "Which split of भयोत्रास in unit 108 is right?",
            ("भय + उत्रास", "अ + उ → ओ: fear and fright."),
            [("भयः + उत्रास", "A visarga before उ would leave भय उत्रास, with no ओ."),
             ("भये + उत्रास", "ए before उ does not give ओ."),
             ("भयो + त्रास", "भयो is not a stem; the card gives भय and उत्रास.")],
            "भय (fear) + उत्रास (fright): अ + उ → ओ.",
            "अ + उ → ओ."),
        multi("apply", 4, "A pregnant woman does these things. Which two are named in unit 108's list?",
              [("She wears red garments", "That is in unit 111, not in this line."),
               ("She drinks cool water", "Water is not named in this line."),
               ("She sleeps by day", "Right: दिवास्वप्न."),
               ("She holds back her natural urges", "Right: वेगविधारण.")],
              [2, 3],
              "Day sleep and holding back urges both stand in the list.",
              "दिवास्वप्न, वेगविधारण."),
        T(mcq("transfer", 5, "By the rule of कठिनासन (कठिन + आसन), how is देव + आलयः joined?",
              ("देवालयः", "अ + आ → आ, as in कठिन + आसन → कठिनासन."),
              [("देवलयः", "The long आ cannot be lost."),
               ("देवेलयः", "ए comes from अ + इ, not from अ + आ."),
               ("देवोलयः", "ओ comes from अ + उ, not from अ + आ.")],
              "अ + आ → आ: कठिनासन, देवालयः.",
              "अ/आ + अ/आ → आ."),
          "A final अ and an initial अ or आ merge into one long आ."),
    ],
}

# ---------------------------------------------------------------- unit 109
AUTHORED["109"] = {
    "title": "समासतः सर्वमतिगुरूष्णतीक्ष्णरूक्षमन्नपानं",
    "question": "What does unit 109 add, in brief?",
    "rule": ("In brief: all food and drink that is excessively (ati) heavy, hot, sharp (tīkṣṇa) and dry, and harsh "
             "activities. The line has no verb."),
    "limits": ("ati is read to govern all four qualities (the data's reading). No verb is printed and nothing is supplied. "
               "No amount or dose is given."),
    "explain_hi": ("संक्षेप में (समासतः) यह इकाई बात को समेटती है: सब अन्न-पान जो अत्यन्त भारी (गुरु), गरम (उष्ण), तीक्ष्ण और रूखा (रूक्ष) हो, "
                   "और दारुण (कठोर) चेष्टाएँ। ‘अति’ चारों गुणों पर लगा माना गया है। "
                   "‘अन्नपान’ द्वन्द्व है, पर नपुंसक एकवचन में। "
                   "पंक्ति में क्रिया नहीं; यह इकाई १०८ की सूची को आगे बढ़ाती है, कुछ जोड़ा नहीं गया। "
                   "छपा ‘समासत:’ का कोलन विसर्ग का स्थानापन्न है।"),
    "hook": "संक्षेप में: अति-गुरु, उष्ण, तीक्ष्ण, रूक्ष अन्न-पान, और दारुण चेष्टा।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 109, which food and drink is meant, in brief?",
            ("Excessively heavy, hot, sharp and dry", "अतिगुरूष्णतीक्ष्णरूक्षम् अन्नपानम्."),
            [("Excessively light, cool, mild and oily", "Those are not the qualities named."),
             ("Any food or drink taken at night", "Night is not named in this line."),
             ("Food and drink that are sweet or sour", "Tastes are not named in this line.")],
            "All food and drink that is excessively heavy, hot, sharp and dry.",
            "अति + गुरु, उष्ण, तीक्ष्ण, रूक्ष."),
        order(1, "Put the four qualities of unit 109 in their printed order.",
              ["गुरु", "उष्ण", "तीक्ष्ण", "रूक्ष"],
              "The print reads अतिगुरूष्णतीक्ष्णरूक्षम्: heavy, hot, sharp, dry.",
              "गुरु → उष्ण → तीक्ष्ण → रूक्ष."),
        match(2, "Match each word of unit 109 to its meaning on the card.",
              [["समासतः", "in brief"], ["अति", "excessively"], ["अन्नपान", "food and drink"], ["दारुण", "harsh, violent"],
               ["चेष्टा", "activity, movement"]],
              "In brief: excessive food and drink, and harsh activities.",
              "समासतः, अति, अन्नपान, दारुण, चेष्टा.", role="extend",
              teaches="समासतः sums up: food and drink of four qualities under अति, and harsh activities."),
        mcq("discriminate", 3, "Which split of गुरूष्ण is right?",
            ("गुरु + उष्ण", "उ + उ → ऊ."),
            [("गुर + उष्ण", "अ + उ would give गुरोष्ण."),
             ("गुरुः + उष्ण", "A visarga after उ before a vowel would give गुरुरुष्ण."),
             ("गुरु + ष्ण", "ष्ण is not a word, and no ऊ would arise.")],
            "गुरु (heavy) + उष्ण (hot): उ + उ → ऊ.",
            "उ + उ → ऊ."),
        multi("apply", 4, "Which two are right about unit 109, by the card?",
              [("It sums up in brief (समासतः)", "Right: समासतः, in brief."),
               ("It names light and cool food", "No: it names heavy, hot, sharp and dry."),
               ("It prints a verb: should avoid", "No verb is printed; nothing is supplied."),
               ("It names harsh activities (दारुणाश्च चेष्टाः)", "Right: harsh activities.")],
              [0, 3],
              "In brief: excessive food and drink of four qualities, and harsh activities; no verb.",
              "समासतः …; दारुणाश्च चेष्टाः."),
        T(mcq("transfer", 5, "Built like अतिगुरु (excessively heavy), what does an invented अतिशीतं जलम् mean?",
              ("Excessively cold water", "अति- before a quality means excessively."),
              [("Slightly cold water", "अति means excess, not a little."),
               ("Water that is not cold", "अति does not deny; there is no न."),
               ("Cold water and cold food", "No food is named; जलम् is water alone.")],
              "अति + गुरु = excessively heavy; अति + शीत = excessively cold.",
              "अति- + quality = excessively."),
          "अति- before a quality means excessively: अतिगुरु, अतिशीत."),
    ],
}

# ---------------------------------------------------------------- unit 110
AUTHORED["110"] = {
    "title": "तथा",
    "question": "What does the lone तथा of unit 110 mean?",
    "rule": ("तथा standing alone = 'likewise, also': it adds a further point. Paired with यथा (यथा यथा … तथा तथा, "
             "unit 105) it means 'so'. तद्यथा (unit 107) means 'namely'."),
    "limits": "A one-word unit; it states no content. What it introduces follows in the next unit, not here.",
    "explain_hi": ("यह इकाई केवल ‘तथा’ है: ‘वैसे ही’, ‘और भी’; यह एक नई बात जोड़ता है। "
                   "जब ‘तथा’ ‘यथा’ के साथ जोड़ी में आता है, जैसे इकाई १०५ के ‘यथा यथा … तथा तथा’ में, तब अर्थ होता है ‘जैसे … वैसे’। "
                   "‘तद्यथा’ (इकाई १०७) अलग सूत्र है: ‘जैसे कि’, सूची खोलने वाला। "
                   "यहाँ ‘तथा’ अकेला है, इसलिए अर्थ ‘वैसे ही, और भी’। यह गद्य है।"),
    "hook": "अकेला तथा = और भी; यथा के साथ तथा = वैसे।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "What does तथा, standing alone in unit 110, mean?",
            ("Likewise, also", "तथा alone adds a further point: likewise."),
            [("Namely, as follows", "Namely is तद्यथा, as in unit 107."),
             ("In brief, in short", "In brief is समासतः, as in unit 109."),
             ("Therefore, hence", "Therefore is तस्मात्, as in unit 104.")],
            "तथा alone = likewise, also.",
            "तथा (alone) = likewise."),
        match(1, "Match each formula on the card to its meaning.",
              [["तथा (alone)", "likewise, also"], ["यथा यथा … तथा तथा", "as … so"], ["तद्यथा", "namely"]],
              "Alone, तथा adds a point; with यथा it answers 'as'; तद्यथा opens a list.",
              "तथा = likewise; यथा … तथा = as … so; तद्यथा = namely."),
        fill(2, "The one word of unit 110, meaning likewise, is ____. Type it in Devanagari or in English letters (e.g. dharma).",
             accepts("तथा"),
             "तथा = likewise, also.",
             "तथा means in that way: likewise, also.",
             "तथा = likewise."),
        mcq("discriminate", 3, "Which word does तथा answer when the two stand as a pair, as in unit 105?",
            ("यथा (as)", "यथा … तथा = as … so."),
            [("यदा (when)", "यदा is answered by तदा (then)."),
             ("यत्र (where)", "यत्र is answered by तत्र (there)."),
             ("यतः (whence)", "यतः is answered by ततः (thence).")],
            "The pair is यथा … तथा: as … so.",
            "यथा ↔ तथा."),
        multi("apply", 4, "Which two are right about unit 110, by the card?",
              [("It is a prose unit", "Right: one word of prose."),
               ("It means namely and opens a list", "No: that is तद्यथा."),
               ("It is a metrical verse line", "No: the unit is prose."),
               ("It stands alone here, not paired with यथा", "Right: so it means likewise, also.")],
              [0, 3],
              "A lone prose तथा: likewise, also.",
              "तथा alone = likewise."),
        T(mcq("transfer", 5, "In an invented line रामो गच्छति तथा सीता, what does तथा mean?",
              ("Rāma goes; likewise Sītā", "तथा alone adds: likewise, Sītā (goes too)."),
              [("Rāma goes; therefore Sītā", "Therefore would need तस्मात्."),
               ("Rāma goes; namely Sītā", "Namely would need तद्यथा."),
               ("Rāma goes, but not Sītā", "No न is printed; nothing is denied.")],
              "A lone तथा adds a further item: likewise.",
              "तथा (alone) = likewise."),
          "A lone तथा adds a further item in the same way: likewise, also."),
    ],
}

# ---------------------------------------------------------------- unit 111
AUTHORED["111"] = {
    "title": "न रक्त्तानि वासांसि",
    "question": "Which three things does unit 111 forbid?",
    "rule": ("For the sake of protection (parirakṣaṇārtham, with deities, rakṣas and non-increase named), (she) should not "
             "wear red garments, should not mount a vehicle, should not consume madya (an intoxicating drink) and meat."),
    "limits": ("How देवता, रक्षः and अनुपचय relate to the protection is not decided, so no question asks it. The verb of the "
               "third clause is a correction (printed अश्रीयात्, read अश्नीयात्), so questions keep to its printed object. "
               "रक्त्तानि is read रक्तानि (red), a print habit. The subject (she) is understood."),
    "explain_hi": ("यह इकाई तीन निषेध देती है, विधिलिङ् ‘न … -एत्’ (न करे) के साथ: लाल वस्त्र न पहने, सवारी पर न चढ़े, मद्य (मादक पेय) और मांस का सेवन न करे। "
                   "उद्देश्य है ‘देवतारक्षोऽनुपचयपरिरक्षणार्थम्’: देवता, राक्षस और अनुपचय (वृद्धि न होना) के सम्बन्ध में रक्षा के लिए; "
                   "इन तीनों का रक्षा से ठीक सम्बन्ध डेटा तय नहीं करता। "
                   "कर्ता ‘वह’ (गर्भिणी) पिछली इकाइयों से समझी गई है। "
                   "छपा ‘रक्त्तानि’ का दोहरा त छपाई की आदत है (रक्तानि, लाल); छपा ‘अश्रीयात्’ कोई रूप नहीं, ‘अश्नीयात्’ (खाए) सम्भावित सुधार है।"),
    "hook": "तीन ‘न’: लाल वस्त्र नहीं, सवारी नहीं, मद्य-मांस नहीं।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 111, which garments should she not wear?",
            ("Red garments", "न रक्त्तानि (रक्तानि) वासांसि धारयेत्."),
            [("White garments", "White garments are not named here."),
             ("Wet garments", "Wet garments are not named here."),
             ("Old garments", "Old garments are not named here.")],
            "She should not wear red garments.",
            "रक्त = red; वासांसि = garments."),
        order(1, "Put the three forbidden things of unit 111 in their printed order.",
              ["रक्त्तानि वासांसि (red garments)", "यानम् (a vehicle)", "मद्यमांसम् (madya and meat)"],
              "Not to wear red garments, not to mount a vehicle, not (to consume) madya and meat.",
              "वासांसि → यानम् → मद्यमांसम्."),
        match(2, "Match each word of unit 111 to its meaning on the card.",
              [["वासांसि", "garments"], ["धारयेत्", "should wear"], ["यानम्", "vehicle"], ["अधिरोहेत्", "should mount"],
               ["मद्य", "an intoxicating drink"]],
              "Garments are worn (धारयेत्), a vehicle is mounted (अधिरोहेत्); मद्य is an intoxicating drink.",
              "वासांसि, धारयेत्, यानम्, अधिरोहेत्, मद्य.", role="extend",
              teaches="Each prohibition is न with an optative verb: न धारयेत्, न अधिरोहेत्."),
        mcq("discriminate", 3, "Which split of रक्षोऽनुपचय is right?",
            ("रक्षः + अनुपचय", "अः before अ gives ओ, and the lost अ is marked by ऽ."),
            [("रक्षा + अनुपचय", "आ + अ would give रक्षानुपचय, with no ओ."),
             ("रक्षो + नुपचय", "नुपचय is not a word; the card gives अनुपचय."),
             ("रक्षः + नुपचय", "Before न the visarga would give रक्षो नुपचय, without ऽ.")],
            "रक्षः (rakṣas) + अनुपचय (non-increase): अः + अ → ओऽ.",
            "अः + अ → ओ + ऽ."),
        mcq("apply", 4, "What does न … धारयेत् express in unit 111?",
            ("A prohibition: she should not wear", "न + optative: should not."),
            [("A past fact: she did not wear", "No past form is printed."),
             ("A future: she will not wear", "धारयेत् is an optative, not a future."),
             ("A question: does she not wear?", "Nothing marks a question.")],
            "न with the optative forbids: she should not wear.",
            "न + optative = should not."),
        T(mcq("transfer", 5, "Built like न यानमधिरोहेत्, what does an invented न दिवा स्वपेत् mean?",
              ("One should not sleep by day", "न + optative स्वपेत्: should not sleep."),
              [("One did not sleep by day", "स्वपेत् is not a past."),
               ("One sleeps only by day", "न denies; nothing says only."),
               ("One will sleep by day", "स्वपेत् is an optative, not a future.")],
              "न + optative = should not: न अधिरोहेत्, न स्वपेत्.",
              "न + optative = should not."),
          "न with an optative (-एत्) states a prohibition: should not."),
    ],
}

# ---------------------------------------------------------------- unit 112
AUTHORED["112"] = {
    "title": "यच्चान्यदपि वृद्धस्त्रियो ब्रूयुः",
    "question": "Whose word does unit 112 bring in, and how is its opening joined?",
    "rule": ("And whatever else old women may also say: यत् च अन्यत् अपि … ब्रूयुः (optative, may say). "
             "The sentence is left open in this unit."),
    "limits": ("The main clause is not in this unit; what is to be done with what the old women say is not stated here, and "
               "no question asks it. Nothing they say is listed."),
    "explain_hi": ("यह छोटी गद्य-पंक्ति कहती है: और भी जो कुछ वृद्ध स्त्रियाँ कहें। "
                   "‘यत् … अन्यत् अपि’ = जो कुछ और भी; ‘ब्रूयुः’ = कहें (विधिलिङ्, प्रथम पुरुष बहुवचन)। "
                   "मुख्य वाक्य इस इकाई में नहीं है, इसलिए उनकी बात का क्या करना है, यह यहाँ नहीं कहा गया। "
                   "सन्धियाँ: यत् + च → यच्च; च + अन्यत् → चान्यत्; अन्यत् + अपि → अन्यदपि; स्त्रियः + ब्रूयुः → स्त्रियो ब्रूयुः।"),
    "hook": "यच्चान्यदपि: जो कुछ और भी वृद्ध स्त्रियाँ कहें।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 112, who may say whatever else?",
            ("Old women (वृद्धस्त्रियः)", "वृद्धस्त्रियो ब्रूयुः: old women may say."),
            [("The physicians of old", "Physicians are not named here."),
             ("The pregnant woman's husband", "No husband is named here."),
             ("The teachers of the science", "Teachers are not named here.")],
            "Whatever else old women may say.",
            "वृद्ध + स्त्रियः = old women."),
        order(1, "Put the words of unit 112 in their order.",
              ["यत्", "च", "अन्यत्", "अपि", "वृद्धस्त्रियः", "ब्रूयुः"],
              "Whatever, and, else, also, old women, may say.",
              "यत् → च → अन्यत् → अपि → वृद्धस्त्रियः → ब्रूयुः."),
        match(2, "Match each word of unit 112 to its meaning on the card.",
              [["यत्", "whatever"], ["अन्यत्", "other, else"], ["अपि", "also"], ["वृद्ध", "old"], ["ब्रूयुः", "may say"]],
              "Whatever else old women may also say.",
              "यत्, अन्यत्, अपि, वृद्ध, ब्रूयुः.", role="extend",
              teaches="यत् … अन्यत् अपि = whatever else, also."),
        mcq("discriminate", 3, "Why is स्त्रियः printed as स्त्रियो before ब्रूयुः?",
            ("अः before a voiced sound becomes ओ", "ब is voiced: स्त्रियः + ब्रूयुः → स्त्रियो ब्रूयुः."),
            [("अः before any consonant becomes ओ", "Before a voiceless sound such as त it becomes स्, not ओ."),
             ("स्त्रियो is a dual form", "The card gives f. nom. pl.; the ओ is sandhi."),
             ("A letter is lost in the print", "This is regular sandhi, not a loss in print.")],
            "स्त्रियः (nom. pl.) + voiced ब → स्त्रियो.",
            "अः + voiced consonant → ओ."),
        multi("apply", 4, "Which two are right about unit 112, by the card?",
              [("ब्रूयुः is a past tense: they said", "No: it is an optative, may say."),
               ("The speakers are old women", "Right: वृद्धस्त्रियः."),
               ("The unit lists what they say", "No: nothing they say is listed."),
               ("यत् … अन्यत् अपि means whatever else, also", "Right: यच्चान्यदपि.")],
              [1, 3],
              "Old women are the speakers; यत् … अन्यत् अपि = whatever else; ब्रूयुः = may say.",
              "यच्चान्यदपि वृद्धस्त्रियो ब्रूयुः."),
        T(mcq("transfer", 5, "By the rule of यच्च (यत् + च), how is तत् + च written when joined?",
              ("तच्च", "त् before च becomes च्."),
              [("तद्च", "Before च the त् becomes च्, not द्."),
               ("तत्च", "त् cannot stay unchanged before च."),
               ("तन्च", "च is not a nasal, so त् does not become न्.")],
              "यत् + च → यच्च; so तत् + च → तच्च.",
              "त् + च → च्च."),
          "A final त् becomes च् before च: यच्च, तच्च."),
    ],
}

# ---------------------------------------------------------------- unit 113
AUTHORED["113"] = {
    "title": "प्रतानोत्तानशायिन्याः",
    "question": "What mishap does unit 113 link to the woman sleeping stretched out and face up?",
    "rule": ("In a woman who sleeps stretched out and face up (uttāna), the nāḍī of the fetus that rests on the navel "
             "(probably the umbilical cord) winds around the neck and causes a mishap (vyāpatti)."),
    "limits": ("nāḍī as the umbilical cord is probable, not stated; whose neck is not stated (the fetus's is the natural "
               "reading); pratāna is not firmly known. The printed नाडीं is read नाडी (nom.). No question rests on these "
               "points. No remedy is given."),
    "explain_hi": ("यह गद्य-पंक्ति माता के सोने के ढंग का एक परिणाम बताती है: जो स्त्री तानकर (प्रतान) और उत्तान (चित, पीठ के बल) सोती है, "
                   "उसके गर्भ की नाभि पर टिकी नाड़ी कण्ठ को लपेटकर विपत्ति (व्यापत्ति) करती है। "
                   "‘नाड़ी’ का अर्थ नली या वाहिका है; इसे गर्भनाल पढ़ना सम्भावित है, पक्का नहीं। "
                   "किसका कण्ठ, यह पाठ नहीं कहता (गर्भ का पढ़ना स्वाभाविक है); ‘प्रतान’ का अर्थ भी पक्का नहीं। "
                   "‘अनुवेष्ट्य’ उपसर्ग वाला ल्यबन्त रूप है: लपेटकर।"),
    "hook": "चित लेटना → नाभि की नाड़ी कण्ठ पर → विपत्ति।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 113, how does the woman lie in this case?",
            ("Face up (uttāna)", "उत्तानशायिनी: she sleeps face up."),
            [("On her left side", "No side is named in this line."),
             ("Propped up, sitting", "Sitting is not named in this line."),
             ("Face down", "उत्तान is face up, the opposite.")],
            "She sleeps face up (and stretched out, a less sure word).",
            "उत्तान = lying face up."),
        order(1, "Put the printed parts of unit 113 in their order.",
              ["प्रतानोत्तानशायिन्याः", "पुनर्गर्भस्य", "नाभ्याश्रया नाडीं", "कंठमनुवेष्ट्य", "व्यापत्तिं करोति"],
              "Of her who sleeps stretched out and face up, of the fetus, the nāḍī on the navel, winding round the neck, causes a mishap.",
              "शायिन्याः → गर्भस्य → नाडी → कण्ठम् अनुवेष्ट्य → व्यापत्तिं करोति."),
        match(2, "Match each word of unit 113 to its meaning on the card.",
              [["उत्तान", "lying face up"], ["नाभि", "navel"], ["कण्ठ", "neck, throat"], ["अनुवेष्ट्य", "having wound around"],
               ["व्यापत्ति", "mishap"]],
              "Face up; on the navel; around the neck; having wound; a mishap.",
              "उत्तान, नाभि, कण्ठ, अनुवेष्ट्य, व्यापत्ति.", role="extend",
              teaches="The chain runs: resting on the navel, wound around the neck, a mishap."),
        mcq("discriminate", 3, "Why does अनुवेष्ट्य end in -य and not in -त्वा?",
            ("With a prefix the absolutive takes -य", "अनु- is a prefix, so the ending is -य: having wound around."),
            [("-य marks an optative verb of wishing", "The optative ends in -एत्, as in रक्षेत्."),
             ("-य marks a feminine noun ending", "The card gives an absolutive, not a noun."),
             ("-य marks a verb in the future tense", "The card gives an absolutive: having wound.")],
            "A verb with a prefix makes its absolutive in -य, not -त्वा.",
            "Prefix + root → absolutive in -य."),
        multi("apply", 4, "Which two does unit 113 state plainly, by the card?",
              [("The unit names the nāḍī as the umbilical cord", "No: the cord is a probable reading, not stated."),
               ("The mishap is tied to how the woman sleeps", "Right: प्रतानोत्तानशायिन्याः."),
               ("नाभ्याश्रया means resting on the navel", "Right: नाभि + आश्रया."),
               ("The unit says it is the mother's neck", "No: whose neck is not stated.")],
              [1, 2],
              "Sure: the posture of sleep and the word नाभ्याश्रया; probable: the cord; unstated: whose neck.",
              "शयन → नाभ्याश्रया नाडी → व्यापत्ति."),
        T(mcq("transfer", 5, "By the rule of अनुवेष्ट्य, what is the absolutive of प्र + √विश् (to enter)?",
              ("प्रविश्य", "With the prefix प्र the absolutive takes -य: having entered."),
              [("प्रविश्त्वा", "With a prefix the ending is -य, not -त्वा."),
               ("प्रविष्टः", "That is a past participle: entered."),
               ("प्रविशेत्", "That is an optative: should enter.")],
              "अनु + √वेष्ट् → अनुवेष्ट्य; प्र + √विश् → प्रविश्य.",
              "Prefix + root → -य."),
          "A verb with a prefix makes its absolutive (having done) in -य, not -त्वा."),
    ],
}

# ===================================================================== NOTES_HI
NOTES_HI = {
    "101": ("विश्वास उच्च, कोई पाठ-चिह्न नहीं; गद्य, एक छपी पंक्ति (02.02.104)। छपा ‘अपिच’ = अपि + च, एक संक्रमण-सूत्र। "
            "सन्धि जाँची: अपि + च → अपिच, कोई ध्वनि-परिवर्तन नहीं, केवल जुड़ा लेखन। यह आगे की बात खोलता है (डेटा की टिप्पणी)।"),
    "102": ("विश्वास मध्यम; गद्य (02.02.105)। पाठ-चिह्न: ‘श्लेष्माऽनुगतंशुक्लाक्षं’ में सम्भवतः दूरी छूटी है "
            "(श्लेष्मानुगतं शुक्लाक्षं); आ के बाद का ऽ छपाई की आदत है, लोप नहीं। ‘तेज’ का अर्थ प्रकाश/अग्नि; पंक्ति ‘आँख में’ नहीं कहती। "
            "‘रक्त’ = खून या लालिमा, दोनों सम्भव। विशेषण (विकृतरूक्षारुणाक्षम् आदि) नपुंसक ‘जात्यन्धत्वम्’ से मेल खाते हैं। "
            "सन्धियाँ जाँचीं: तेजः + जात्य… → तेजो जात्य… (अः + घोष → ओ); तत् + एव → तदेव; वात + अनुगतम् → वातानुगतम्; "
            "पिङ्ग + अक्षम् → पिङ्गाक्षम्; रक्ताक्षम् + इति → रक्ताक्षमिति।"),
    "103": ("विश्वास उच्च, कोई पाठ-चिह्न नहीं; गद्य (02.02.106)। ‘योगक्षेम’ (प्राप्ति और रक्षा) को ‘कल्याण’ पढ़ा गया; "
            "‘गर्भसमानयोगक्षेमा’ बहुव्रीहि, ‘गर्भिणी’ का विशेषण। ‘हि’ से कारण; डेटा के अनुसार यह और अगली इकाई (१०४) एक ही तर्क लगते हैं।"),
    "104": ("विश्वास मध्यम, कोई पाठ-चिह्न नहीं; गद्य (02.02.107)। ‘प्रियहिताभ्याम्’ द्वन्द्व, तृतीया द्विवचन माना गया "
            "(‘-भ्याम्’ अन्य विभक्तियों का भी रूप है); संज्ञाएँ पाठ में नहीं। ‘गर्भोपघातकरेभ्यः’ पञ्चमी बहुवचन माना गया (‘से’)। "
            "सन्धियाँ जाँचीं: तस्मात् + विशेषतः → तस्माद्विशेषतः; विशेषतः + ताम् → विशेषतस्ताम्; ताम् + प्रिय… → तां प्रिय…; "
            "गर्भ + उपघात → गर्भोपघात; …करेभ्यः + रक्षेत् → …करेभ्यो रक्षेत्।"),
    "105": ("विश्वास कम; गद्य (02.02.108)। पाठ-चिह्न: ‘भाराहारसापचाराच्च’ में ‘सा’ अस्पष्ट; ‘भार-आहार-अपचारात्’ (भार, आहार और अपचार से) "
            "केवल अनुमान है, ‘भार-आहार-सापचारात्’ भी सम्भव; इस पर कोई प्रश्न नहीं। ‘अपचार’ किस बात का, पाठ नहीं कहता। "
            "सन्धियाँ जाँचीं: गर्भः + वृद्धिम् → गर्भो वृद्धिम्; वृद्धिम् + आप्नोति → वृद्धिमाप्नोति; स्त्रियाः + बल… → स्त्रिया बल… "
            "(आः के बाद घोष ब से पहले विसर्ग-लोप)।"),
    "106": ("विश्वास उच्च, कोई पाठ-चिह्न नहीं; गद्य (02.02.109)। क्रिया ‘हैं’ समझी गई। डेटा के अनुसार यह, इकाई १०७ (तद्यथा) "
            "और इकाई १०८ (सूची) एक ही कथन हैं। सन्धियाँ जाँचीं: तत्र + इमे → तत्रेमे (अ + इ → ए); गर्भ + उपघात → गर्भोपघात (अ + उ → ओ)।"),
    "107": ("विश्वास उच्च, कोई पाठ-चिह्न नहीं; गद्य (02.02.110)। स्थिर सूत्र, सूची का परिचय। "
            "सन्धि जाँची: तत् + यथा → तद्यथा (त् घोष य से पहले द्)।"),
    "108": ("विश्वास मध्यम; गद्य (02.02.111), बिना दूरी का एक लम्बा द्वन्द्व। पाठ-चिह्न: (१) ‘यानयान’ में ‘यान’ दोहरा छपा लगता है, "
            "अनुवाद में एक बार; (२) ‘…यानरा त्रिजागरण…’ की खाली जगह के पार ‘रात्रिजागरण’ पढ़ा गया (सम्भावित); "
            "(३) छपा ‘क्रोघ’ कोई शब्द नहीं, ‘क्रोध’ पढ़ा गया (लगभग निश्चित)। ‘उत्कटक’ = उकड़ूँ बैठना (सम्भावित); ‘उत्कटविषम’ विभाजन भी सम्भव। "
            "व्यवाय = मैथुन (मानक)। ‘आदयः’ सूची खुली छोड़ता है। "
            "सन्धियाँ जाँचीं: कर्शन + अभिघात → कर्शनाभिघात; अभिघात + अतिमात्र → अभिघातातिमात्र; विधारण + अजीर्ण → विधारणाजीर्ण; "
            "आतप + अग्नि → आतपाग्नि; भय + उत्रास → भयोत्रास; उपवास + उत्कटक → उपवासोत्कटक; कठिन + आसन → कठिनासन; "
            "प्रपात + अप्रिय → प्रपाताप्रिय; अप्रिय + अवलोकन → अप्रियावलोकन; श्रवण + आदयः → श्रवणादयः।"),
    "109": ("विश्वास मध्यम; गद्य (02.02.112)। पाठ-चिह्न: छपा ‘समासत:’ का कोलन विसर्ग का स्थानापन्न (निश्चित): समासतः। "
            "‘अति’ चारों गुणों पर लगा माना गया। क्रिया नहीं, कुछ जोड़ा नहीं गया। "
            "सन्धियाँ जाँचीं: सर्वम् + अति → सर्वमति; गुरु + उष्ण → गुरूष्ण (उ + उ → ऊ); रूक्षम् + अन्नपानम् → रूक्षमन्नपानम्; "
            "दारुणाः + च → दारुणाश्च (विसर्ग च से पहले श्)।"),
    "110": ("विश्वास उच्च, कोई पाठ-चिह्न नहीं; गद्य (02.02.113)। अकेला ‘तथा’ = वैसे ही, और भी; डेटा के अनुसार यह आगे की बात (इकाई १११) खोलता है।"),
    "111": ("विश्वास मध्यम; गद्य (02.02.114)। पाठ-चिह्न: ‘रक्त्तानि’ का दोहरा त छपाई की आदत (रक्तानि, लाल; रंगा हुआ लाल भी सम्भव); "
            "छपा ‘अश्रीयात्’ कोई रूप नहीं, ‘अश्नीयात्’ (खाए) सम्भावित सुधार। "
            "‘देवतारक्षोऽनुपचयपरिरक्षणार्थम्’ में तीनों सदस्यों का सम्बन्ध तय नहीं (‘से रक्षा’ या अन्य अर्थ); इस पर कोई प्रश्न नहीं। "
            "सन्धियाँ जाँचीं: रक्षः + अनुपचय → रक्षोऽनुपचय; धारयेत् + न → धारयेन्न; यानम् + अधिरोहेत् → यानमधिरोहेत्; "
            "अधिरोहेत् + न → अधिरोहेन्न (त् + न → न्न; यहाँ द्न भी वैकल्पिक रूप होता, इसलिए इस पर प्रश्न नहीं)।"),
    "112": ("विश्वास मध्यम, कोई पाठ-चिह्न नहीं; गद्य (02.02.115)। डेटा के अनुसार यह किसी लम्बे कथन का अंश है, मुख्य वाक्य इकाई में नहीं। "
            "सन्धियाँ जाँचीं: यत् + च → यच्च (त् च से पहले च्); च + अन्यत् → चान्यत्; अन्यत् + अपि → अन्यदपि (त् स्वर से पहले द्); "
            "वृद्धस्त्रियः + ब्रूयुः → वृद्धस्त्रियो ब्रूयुः (अः + घोष → ओ)।"),
    "113": ("विश्वास मध्यम; गद्य (02.02.116)। पाठ-चिह्न: छपा ‘नाडीं’ (द्वितीया) सम्भवतः ‘नाडी’ (प्रथमा) है, क्योंकि ‘नाभ्याश्रया’ प्रथमा स्त्रीलिंग है। "
            "नाड़ी = गर्भनाल (सम्भावित); किसका कण्ठ, नहीं कहा; ‘प्रतान’ अनिश्चित, समास दो आदतें भी हो सकता है। स्त्री की षष्ठी ढीली (‘के प्रसंग में’)। "
            "सन्धियाँ जाँचीं: प्रतान + उत्तान → प्रतानोत्तान; पुनः + गर्भस्य → पुनर्गर्भस्य; नाभि + आश्रया → नाभ्याश्रया (इ + आ → या); "
            "कण्ठम् + अनुवेष्ट्य → कण्ठमनुवेष्ट्य।"),
}

# ===================================================================== AIDS
AIDS = {
    "101": {
        "frame": "अपि (भी) + च (और) → अपिच: ‘और भी’, नई बात का आरम्भ।",
        "sandhi": "इ + च: कोई परिवर्तन नहीं: अपि + च → अपिच (केवल जुड़ा लेखन)।",
        "anchors": "मेरी याद-पद्धति, इस अध्याय के सूत्र-शब्द: अपि च = और भी · तस्मात् = इसलिए · तद्यथा = जैसे कि · तथा = वैसे ही।",
    },
    "102": {
        "diagram": {"groups": [
            {"label": "परिभाषा", "items": ["दृष्टिभाग तक न पहुँचा तेज", "= जात्यन्धत्व"]},
            {"label": "वही, अनुगत हो तो (छपे क्रम में)",
             "items": ["वात: विकृत, रूखी, अरुण आँख", "पित्त: पिंगल आँख", "कफ: सफ़ेद आँख", "रक्त: लाल आँख"]}]},
        "sandhi": ("अः + घोष → ओ: तेजः + जात्य… → तेजो जात्य… · त् + स्वर → द्: तत् + एव → तदेव · "
                   "अ + अ → आ: वात + अनुगतम् → वातानुगतम्; पिङ्ग + अक्षम् → पिङ्गाक्षम्।"),
        "chunks": ("दृष्टिभागमप्रतिपन्नं तेजो जात्यंधत्वं | तदेव | वातानुगतं विकृतरूक्षारुणाक्षं | पित्तानुगतं पिंगाक्षं | "
                   "श्लेष्माऽनुगतंशुक्लाक्षं | रक्तानुगतं रक्ताक्षमिति"),
        "letters": "छपे क्रम के साथी: वा-पि-श्ले-र (वात, पित्त, श्लेष्मा, रक्त)।",
    },
    "103": {
        "frame": "गर्भिणी → (उसका) योगक्षेम → गर्भ के समान · हि = क्योंकि (कारण)।",
        "chunks": "गर्भसमानयोगक्षेमा | हि | गर्भिणी | भवति",
        "pegs": "मेरा बनाया चित्र, पाठ का दावा नहीं: एक ही नाव में माँ और गर्भ; नाव सुरक्षित तो दोनों सुरक्षित।",
    },
    "104": {
        "frame": "तस्मात् (इसलिए) → विशेषतः ताम् (विशेषकर उसकी) → प्रियहिताभ्याम् (प्रिय और हित से) → गर्भोपघातकरेभ्यः (गर्भ-घातकों से) → रक्षेत् (रक्षा करे)।",
        "sandhi": ("त् + घोष → द्: तस्मात् + विशेषतः → तस्माद्विशेषतः · ः + त → स्त: विशेषतः + ताम् → विशेषतस्ताम् · "
                   "अः + घोष → ओ: …करेभ्यः + रक्षेत् → …करेभ्यो रक्षेत्।"),
        "chunks": "तस्माद्विशेषतस्तां | प्रियहिताभ्यां | गर्भोपघातकरेभ्यो | रक्षेत्",
    },
    "105": {
        "seesaw": "गर्भ की वृद्धि ↑ ↔ स्त्री के बल का क्षय ↓ (दोनों इसी पंक्ति में: यथा यथा … तथा तथा)।",
        "frame": "यथा यथा (जैसे-जैसे) गर्भ वृद्धि पाता → तथा तथा (वैसे-वैसे) … [छपा ‘भाराहारसापचाराच्च’: अस्पष्ट] … स्त्री का बलक्षय।",
        "sandhi": "अः + घोष → ओ: गर्भः + वृद्धिम् → गर्भो वृद्धिम् · आः + घोष → आ: स्त्रियाः + बल… → स्त्रिया बल…।",
    },
    "106": {
        "frame": "तत्र (इस विषय में) → इमे (ये) → गर्भोपघातकराः (गर्भ को हानि पहुँचाने वाले) · क्रिया ‘हैं’ समझी गई।",
        "sandhi": "अ + इ → ए: तत्र + इमे → तत्रेमे · अ + उ → ओ: गर्भ + उपघात → गर्भोपघात।",
        "chunks": "तत्रेमे | गर्भोपघातकराः",
    },
    "107": {
        "frame": "तत् (वह) + यथा (जैसे) → तद्यथा: ‘जैसे कि’, सूची खोलने वाला सूत्र।",
        "sandhi": "त् + घोष य → द्य: तत् + यथा → तद्यथा।",
        "anchors": "मेरी याद-पद्धति: तद्यथा सुनते ही गिनती के लिए उँगलियाँ तैयार।",
    },
    "108": {
        "diagram": {"groups": [
            {"label": "छपे क्रम में (१)", "items": ["व्यवाय (मैथुन)", "व्यायाम", "कर्शन", "अभिघात", "अतिमात्र संक्षोभी यान",
                                               "रात्रिजागरण (पाठ अनुमानित)", "दिवास्वप्न", "वेगविधारण"]},
            {"label": "छपे क्रम में (२)", "items": ["अजीर्ण", "आतप", "अग्नि", "क्रोध (सुधार)", "शोक", "भय", "उत्रास", "उपवास"]},
            {"label": "छपे क्रम में (३)", "items": ["उत्कटक (सम्भावित)", "विषम, कठिन आसन", "श्वभ्र, कूप में प्रपात",
                                               "अप्रिय अवलोकन, श्रवण", "आदयः (आदि)"]}]},
        "letters": "आरम्भ के आदि-अक्षर, छपे क्रम में: व्य-व्या-क-अ (व्यवाय, व्यायाम, कर्शन, अभिघात)।",
        "sandhi": ("अ + अ → आ: आतप + अग्नि → आतपाग्नि; विधारण + अजीर्ण → विधारणाजीर्ण · "
                   "अ + उ → ओ: भय + उत्रास → भयोत्रास; उपवास + उत्कटक → उपवासोत्कटक · अ + आ → आ: कठिन + आसन → कठिनासन।"),
    },
    "109": {
        "diagram": {"groups": [
            {"label": "अति- (अत्यन्त) … अन्नपान", "items": ["गुरु (भारी)", "उष्ण (गरम)", "तीक्ष्ण", "रूक्ष (रूखा)"]},
            {"label": "और", "items": ["दारुण (कठोर) चेष्टाएँ"]}]},
        "sandhi": ("उ + उ → ऊ: गुरु + उष्ण → गुरूष्ण · म् + स्वर: सर्वम् + अति → सर्वमति · "
                   "ः + च → श्च: दारुणाः + च → दारुणाश्च।"),
        "frame": "समासतः (संक्षेप में) → सर्वम् … अन्नपानम् → दारुणाः च चेष्टाः · क्रिया नहीं।",
    },
    "110": {
        "frame": "अकेला तथा = वैसे ही, और भी · यथा … तथा = जैसे … वैसे (इकाई १०५)।",
        "anchors": "मेरी याद-पद्धति: ‘य’ वाला प्रश्न पूछे (यथा, यदा, यत्र), ‘त’ वाला उत्तर दे (तथा, तदा, तत्र)।",
    },
    "111": {
        "diagram": {"groups": [
            {"label": "उद्देश्य", "items": ["देवता, रक्षः, अनुपचय: परिरक्षणार्थम् (सम्बन्ध अनिश्चित)"]},
            {"label": "न … -एत् (छपे क्रम में)",
             "items": ["लाल वस्त्र न पहने", "सवारी पर न चढ़े", "मद्य और मांस न खाए (क्रिया: सुधार)"]}]},
        "sandhi": ("अः + अ → ओऽ: रक्षः + अनुपचय → रक्षोऽनुपचय · म् + स्वर: यानम् + अधिरोहेत् → यानमधिरोहेत् · "
                   "त् + न → न्न (वैकल्पिक; द्न भी शुद्ध): धारयेत् + न → धारयेन्न।"),
        "frame": "(वह, गर्भिणी) → न धारयेत् · न अधिरोहेत् · न (अश्नीयात्): तीन निषेध।",
    },
    "112": {
        "frame": "यत् च अन्यत् अपि (जो कुछ और भी) → वृद्धस्त्रियः (वृद्ध स्त्रियाँ) → ब्रूयुः (कहें) · मुख्य वाक्य इकाई में नहीं।",
        "sandhi": ("त् + च → च्च: यत् + च → यच्च · अ + अ → आ: च + अन्यत् → चान्यत् · त् + स्वर → द्: अन्यत् + अपि → अन्यदपि · "
                   "अः + घोष → ओ: स्त्रियः + ब्रूयुः → स्त्रियो ब्रूयुः।"),
        "chunks": "यच्चान्यदपि | वृद्धस्त्रियो | ब्रूयुः",
    },
    "113": {
        "chain": {"steps": ["प्रतान-उत्तान सोने वाली स्त्री", "गर्भ की, नाभि पर टिकी नाड़ी", "कण्ठ को लपेटकर",
                            "व्यापत्ति (विपत्ति) करती"]},
        "sandhi": ("अ + उ → ओ: प्रतान + उत्तान → प्रतानोत्तान · र् से बना विसर्ग + घोष → र्: पुनः (मूल पुनर्) + गर्भस्य → पुनर्गर्भस्य · "
                   "इ + आ → या: नाभि + आश्रया → नाभ्याश्रया।"),
        "frame": "शायिन्याः (सोने वाली के प्रसंग में) → गर्भस्य नाडी (गर्भनाल: सम्भावित) → कण्ठम् अनुवेष्ट्य → व्यापत्तिं करोति।",
    },
}

# ===================================================================== IMAGE_SPECS
IMAGE_SPECS = {
    ("102", "diagram"): {
        "file": "sh2-jatyandha-102.svg",
        "alt": ("Flowchart of unit 102: tejas that has not reached the share of sight is congenital blindness; the same, "
                "followed by Vata, gives deformed, dry, reddish eyes; by Pitta, tawny eyes; by Kapha, white eyes; by rakta, "
                "red eyes (four numbered branches in printed order)."),
        "type": "mermaid",
        "code": ("flowchart TD\n"
                 "  A[\"दृष्टिभाग तक न पहुँचा तेज\"] --> B[\"जात्यन्धत्व\"]\n"
                 "  B -->|\"१ वात से\"| C[\"विकृत, रूखी, अरुण आँख\"]\n"
                 "  B -->|\"२ पित्त से\"| D[\"पिंगल आँख\"]\n"
                 "  B -->|\"३ कफ से\"| E[\"सफ़ेद आँख\"]\n"
                 "  B -->|\"४ रक्त से\"| F[\"लाल आँख\"]\n"),
    },
    ("105", "seesaw"): {
        "file": "sh2-balakshaya-105.svg",
        "alt": ("Split of unit 105: as (yatha yatha) the embryo grows, so (tatha tatha) the woman's strength wanes; "
                "the unclear causes are left out."),
        "type": "split",
        "title": "जैसे-जैसे … वैसे-वैसे (इकाई १०५)",
        "cols": [["यथा यथा", ["गर्भ वृद्धि पाता है"]], ["तथा तथा", ["स्त्री का बल घटता है"]]],
    },
    ("108", "diagram"): {
        "file": "sh2-garbhopaghata-108.svg",
        "alt": ("Table of unit 108's list in printed order, in ten rows: intercourse, exertion, emaciating, blows; jolting "
                "vehicles; night waking (reading conjectural), day sleep, holding urges; undigested, sun, fire; anger "
                "(corrected), grief, fear, fright; fasting, squatting (probable); uneven and hard seats; falls into pit or "
                "well; disagreeable seeing and hearing; and so on."),
        "type": "table",
        "title": "इकाई १०८ की सूची (छपे क्रम में)",
        "heads": ["छपा अंश", "अर्थ"],
        "rows": [["व्यवाय, व्यायाम, कर्शन, अभिघात", "मैथुन, व्यायाम, दुबला करने वाला, चोट"],
                 ["अतिमात्र संक्षोभी यान", "बहुत झटके देने वाली सवारी"],
                 ["रात्रिजागरण, दिवास्वप्न, वेगविधारण", "रात जागना (पाठ अनुमानित), दिन में सोना, वेग रोकना"],
                 ["अजीर्ण, आतप, अग्नि", "अजीर्ण, धूप, आग"],
                 ["क्रोध, शोक, भय, उत्रास", "क्रोध (सुधार), शोक, भय, घबराहट"],
                 ["उपवास, उत्कटक", "उपवास, उकड़ूँ बैठना (सम्भावित)"],
                 ["विषम, कठिन आसन", "ऊबड़-खाबड़, कठोर आसन"],
                 ["श्वभ्र, कूप प्रपात", "गड्ढे, कुएँ में गिरना"],
                 ["अप्रिय अवलोकन, श्रवण", "अप्रिय देखना, सुनना"],
                 ["आदयः", "आदि (सूची खुली)"]],
    },
    ("109", "diagram"): {
        "file": "sh2-samasatah-109.svg",
        "alt": ("Split of unit 109: excessively (ati) heavy, hot, sharp and dry food and drink, in printed order; and harsh "
                "activities."),
        "type": "split",
        "title": "संक्षेप में (इकाई १०९)",
        "cols": [["अति- … अन्नपान", ["गुरु (भारी)", "उष्ण (गरम)", "तीक्ष्ण", "रूक्ष (रूखा)"]],
                 ["और", ["दारुण चेष्टाएँ"]]],
    },
    ("111", "diagram"): {
        "file": "sh2-trini-nishedha-111.svg",
        "alt": ("Table of unit 111's three prohibitions in printed order: not to wear red garments; not to mount a vehicle; "
                "not to consume madya and meat (verb corrected)."),
        "type": "table",
        "title": "इकाई १११: तीन निषेध",
        "heads": ["छपा अंश", "अर्थ"],
        "rows": [["न रक्त्तानि वासांसि धारयेत्", "लाल वस्त्र न पहने"],
                 ["न यानमधिरोहेत्", "सवारी पर न चढ़े"],
                 ["न मद्यमांसम् (अश्नीयात्: सुधार)", "मद्य और मांस न खाए"]],
    },
    ("113", "chain"): {
        "file": "sh2-nadi-kantha-113.svg",
        "alt": ("Chain of unit 113 in four steps: a woman who sleeps stretched out and face up; the fetus's nadi resting "
                "on the navel (umbilical cord, probable); having wound around the neck; causes a mishap."),
        "type": "chain",
        "title": "इकाई ११३: शयन से व्यापत्ति",
        "steps": ["प्रतान-उत्तान सोने वाली स्त्री", "नाभि पर टिकी नाड़ी (गर्भनाल: सम्भावित)", "कण्ठ को लपेटकर",
                  "व्यापत्ति (विपत्ति)"],
    },
}
