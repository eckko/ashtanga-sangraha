from helpers import mcq, match, order, fill, multi, accepts


def T(q, teaches):
    q["teaches"] = teaches
    return q


AUTHORED = {}

# ---------------------------------------------------------------- unit 1
AUTHORED["1"] = {
    "title": "अथातो विकृतेहाविज्ञानीयं शारीरं",
    "question": "By card 1, which Śārīra section does the text open here, and what is its title about?",
    "rule": ("Now, therefore (अथ अतः), we shall explain (व्याख्यास्यामः) the Śārīra (शारीरम्) named "
             "Vikṛtehāvijñānīya: on knowing abnormal activity (विकृत-ईहा)."),
    "limits": ("Prose, the stock opening formula; no colophon here. The data reads the title as vikṛta-īhā-vijñānīya; "
               "other readings of the compound are possible, so no question asks how its members relate. The title "
               "names only the topic; the signs come in the cards that follow."),
    "explain_hi": ("यह कार्ड नए शारीर-खण्ड का आरम्भ करता है: ‘अब इसके बाद हम विकृतेहाविज्ञानीय शारीर की व्याख्या करेंगे’। "
                   "डेटा नाम को विकृत (बिगड़ी हुई) + ईहा (चेष्टा, व्यवहार) + विज्ञानीय (जानने से सम्बन्धित) पढ़ता है; समास के दूसरे पाठ भी सम्भव हैं। "
                   "डेटा के अनुसार आगे का अध्याय निकट मृत्यु के लक्षण बताता है। "
                   "‘व्याख्यास्यामः’ भविष्यत्, उत्तम पुरुष बहुवचन है: हम व्याख्या करेंगे। "
                   "‘अथातो’ में अतः का विसर्ग घोष व्यंजन व से पहले ओ बना है।"),
    "hook": "विकृत ईहा का ज्ञान: बिगड़ी चेष्टा पहचानने वाला शारीर।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "In the title word of card 1, what does ईहा mean, by the card?",
            ("Activity", "ईहा = activity, effort, behaviour: विकृत-ईहा = abnormal activity."),
            [("Body, frame", "Body would be शरीर or देह; ईहा is activity."),
             ("Season, time", "Season would be ऋतु, time काल; ईहा is activity."),
             ("Food, diet", "Food would be अन्न or आहार; ईहा is activity.")],
            "विकृत (abnormal) + ईहा (activity) + विज्ञानीय (on knowing).",
            "ईहा = activity, behaviour."),
        order(1, "Put the words of card 1 in the printed order.",
              ["अथ", "अतः", "विकृतेहाविज्ञानीयम्", "शारीरम्", "व्याख्यास्यामः"],
              "Now; therefore; named on knowing abnormal activity; the Śārīra; we shall explain.",
              "अथ → अतः → विकृतेहाविज्ञानीयम् → शारीरम् → व्याख्यास्यामः."),
        match(2, "Match each word of card 1 to its meaning.",
              [["अथ", "now"], ["अतः", "therefore"], ["विकृत", "altered, abnormal"], ["ईहा", "activity"],
               ["व्याख्यास्यामः", "we shall explain"]],
              "अथ = now, अतः = therefore, विकृत = abnormal, ईहा = activity, व्याख्यास्यामः = we shall explain.",
              "अथ, अतः, विकृत, ईहा, व्याख्यास्यामः.", role="extend",
              teaches="A title ending in -ईय means 'concerning ...': विकृतेहाविज्ञानीय = concerning the knowing of abnormal activity."),
        mcq("discriminate", 3, "By the data's reading of card 1, what is the section's title about?",
            ("Knowing abnormal activity", "विकृत-ईहा-विज्ञानीय: the knowing of abnormal activity or behaviour."),
            [("Knowing the healthy body", "विकृत means altered, abnormal, not healthy."),
             ("Knowing the newborn child", "The title names abnormal activity, not a child."),
             ("Knowing the six tastes", "The title names abnormal activity, not tastes.")],
            "विकृत (abnormal) + ईहा (activity): the title is about abnormal activity.",
            "विकृतेहाविज्ञानीय = on knowing abnormal activity."),
        mcq("apply", 4, "Why is अतः printed अतो before विकृतेहा- in card 1?",
            ("अः before a voiced consonant → ओ", "व is a voiced consonant: अतः + विकृत- → अतो विकृत-."),
            [("आः before a voiced consonant → ओ", "आः drops its visarga before a voiced sound; it never gives ओ."),
             ("Every visarga before व → ओ", "Not every: after इ or उ a visarga gives र् before a voiced sound."),
             ("ओ is the adverb's own last vowel", "The adverb is अतः; the ओ comes only from sandhi.")],
            "अतः + विकृतेहा-: अः before the voiced consonant व → ओ.",
            "अः + voiced consonant → ओ."),
        mcq("transfer", 5, "By the pattern of विकृत + ईहा → विकृतेहा, how is गण + ईशः (lord of the hosts) joined in a new example?",
            ("गणेशः", "अ + ई → ए: गण + ईशः → गणेशः, like विकृत + ईहा → विकृतेहा."),
            [("गणीशः", "ई alone would be ई + ई or इ + ई; अ + ई gives ए."),
             ("गणैशः", "ऐ comes from अ + ए or अ + ऐ, not from अ + ई."),
             ("गणोशः", "ओ comes from अ + उ or अ + ऊ, not from अ + ई.")],
            "गण + ईशः = गणेशः, like विकृत + ईहा = विकृतेहा.",
            "अ + ई → ए.",
            teaches="अ + इ or ई joins to ए (guṇa): विकृत + ईहा → विकृतेहा."),
    ],
}

# ---------------------------------------------------------------- unit 2
AUTHORED["2"] = {
    "title": "दृष्टि-विपर्यय: आकाश और घन",
    "question": "By card 2, which reversed sights of sky and solid, formed and formless, does the list begin with?",
    "rule": ("The list of things wrongly seen begins: the sky as if grown solid (घनीभूतमिव आकाशम्), the solid as if "
             "it were sky (आकाशमिव यो घनम्), and the formless and the formed (अमूर्त, मूर्त)."),
    "limits": ("Prose, medium confidence. No verb: the data takes cards 2 to 4 as probably one sentence, the verb "
               "in card 4. Which of अमूर्त / मूर्त is seen as the other, and how अमूर्तवस्थितम् divides, are open: "
               "no question on either."),
    "explain_hi": ("यह कार्ड उन चीज़ों की सूची शुरू करता है जो उलटी दिखती हैं; क्रिया ‘पश्यति’ (देखता है) कार्ड ४ में है। "
                   "डेटा के अनुसार कार्ड २ से ४ सम्भवतः एक ही वाक्य हैं। "
                   "‘घनीभूतमिव आकाशम्’ = आकाश मानो ठोस हो गया हो; ‘आकाशमिव यो घनम्’ = जो ठोस है, वह मानो आकाश हो। "
                   "दूसरी पंक्ति में अमूर्त (आकारहीन) और मूर्त (आकार वाला) का जोड़ा है; कौन किसके जैसा दिखता है, यह स्पष्ट नहीं। "
                   "छपाई में ‘इव’ और ‘आकाशम्’ बिना सन्धि के जुड़े हैं; डेटा इसे सम्भवतः छपाई की आदत मानता है।"),
    "hook": "आकाश ठोस दिखे, ठोस आकाश दिखे: उलटी दृष्टि की सूची।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "In card 2, what does घनीभूत mean?",
            ("Grown solid", "घनी-भूत = become घन (solid, dense)."),
            [("Grown hollow", "Empty would be शून्य; घनीभूत is become solid."),
             ("Grown bright", "Shining would be दीप्त; घनीभूत is become solid."),
             ("Grown watery", "Wet would be आर्द्र; घनीभूत is become solid.")],
            "घन = solid, dense; घनीभूत = become solid.",
            "घनीभूत = thickened, become solid."),
        order(1, "Put these phrases of card 2 in the printed order.",
              ["घनीभूतमिव आकाशम्", "आकाशमिव यो घनं", "अमूर्तमिव मूर्तं च", "मूर्तं वाऽमूर्तवस्थितं"],
              "Sky as if grown solid; the solid as if sky; the formless as if formed, and the formed; or the formed in a formless state.",
              "घनीभूतमिव आकाशम् → आकाशमिव यो घनं → अमूर्तमिव मूर्तं च → मूर्तं वाऽमूर्तवस्थितं."),
        match(2, "Match each word of card 2 to its meaning.",
              [["घन", "solid, dense"], ["आकाश", "sky, space"], ["मूर्त", "having shape"], ["अमूर्त", "formless"],
               ["इव", "as if"]],
              "घन = solid, आकाश = sky, मूर्त = having shape, अमूर्त = formless, इव = as if.",
              "घन, आकाश, मूर्त, अमूर्त, इव.", role="extend",
              teaches="The prefix अ- negates: मूर्त (having shape) → अमूर्त (formless)."),
        mcq("discriminate", 3, "By the data's reading of card 2, what does आकाशमिव यो घनम् describe?",
            ("The solid seen as if it were sky", "आकाशम् इव यः घनम्: the solid (घन) as if it were sky."),
            [("The sky seen as if it were solid", "That is the other phrase, घनीभूतमिव आकाशम्."),
             ("The sky seen full of dark clouds", "The line speaks of solid and sky, not of clouds."),
             ("A solid body seen up in the sky", "Nothing is placed in the sky; the solid looks like sky.")],
            "घनीभूतमिव आकाशम् = sky as solid; आकाशमिव यो घनम् = solid as sky.",
            "आकाशमिव यो घनम् = the solid as if sky."),
        mcq("apply", 4, "A man sees the clear sky as if it had turned solid. Which phrase of card 2 names this?",
            ("घनीभूतमिव आकाशम्", "घनीभूतम् इव आकाशम्: the sky as if grown solid."),
            [("आकाशमिव यो घनम्", "This is the reverse: the solid seen as if it were sky."),
             ("शुक्लं कृष्णमसच्च", "These words are in card 3 (white, black, unreal), not card 2."),
             ("तेजस्व्यतेजस्तद्वत्", "These words are in card 3 (bright, lightless), not card 2.")],
            "Sky → as if solid: घनीभूतमिव आकाशम्.",
            "घनीभूतमिव आकाशम् = sky as if grown solid."),
        mcq("transfer", 5, "By the rule अ + आ → आ (इव + आकाशम् → इवाकाशम्), how is इव + आत्मा joined in a new example?",
            ("इवात्मा", "अ + आ → आ: इव + आत्मा → इवात्मा."),
            [("इवेत्मा", "ए comes from अ + इ or ई, not from अ + आ."),
             ("इवोत्मा", "ओ comes from अ + उ or ऊ, not from अ + आ."),
             ("इवैत्मा", "ऐ comes from अ + ए or ऐ, not from अ + आ.")],
            "इव + आत्मा = इवात्मा, like इव + आकाशम् = इवाकाशम्.",
            "अ + आ → आ.",
            teaches="अ followed by आ merges into one long आ: इव + आकाशम् → इवाकाशम् (the print leaves this pair unjoined)."),
    ],
}

# ---------------------------------------------------------------- unit 3
AUTHORED["3"] = {
    "title": "तेजस्व्यतेजस्तद्वच्च",
    "question": "By card 3, which bare pairs follow in the list, and how is the moon seen?",
    "rule": ("Pairs follow: bright / lightless (and likewise), white / black, unreal / real; the man is free from eye "
             "disease (अनेत्ररोगः), and the moon is seen many-formed and without its mark (बहुरूपमलाञ्छनम्)."),
    "limits": ("Verse, medium confidence. The pairs are printed bare; '(as)' from इव of card 2 is an "
               "interpretation. 'Likewise' probably adds the reverse pair (not spelled out). 'Without mark' "
               "probably means without the dark patch; the text says only 'mark'."),
    "explain_hi": ("सूची आगे बढ़ती है, पर शब्द केवल जोड़ों में छपे हैं: तेजस्वी और तेजहीन, श्वेत और काला, असत् और सत्। "
                   "‘मानो’ का भाव कार्ड २ के ‘इव’ से लिया गया है; यह व्याख्या है, यहाँ छपा नहीं। "
                   "‘तद्वत्’ (उसी प्रकार) सम्भवतः उलटे जोड़े को भी जोड़ता है, पर स्पष्ट नहीं कहा गया। "
                   "व्यक्ति आँख के रोग से रहित है (अनेत्ररोगः), यानी यह दृष्टि किसी ज्ञात नेत्र-रोग से नहीं समझाई जाती। "
                   "चन्द्रमा बहुत रूपों वाला और चिह्नरहित दिखता है; ‘चिह्न’ सम्भवतः उसका काला धब्बा है।"),
    "hook": "उजला-अँधेरा, सफ़ेद-काला, असत्-सत्; चाँद बिना धब्बे का।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "In card 3, what does अलाञ्छन (printed अलांछन) mean?",
            ("Without a mark", "अ (without) + लाञ्छन (mark): without its mark."),
            [("Shining brightly", "Shining would be दीप्त; अलाञ्छन is without a mark."),
             ("Hidden by cloud", "Hidden would be छन्न; अलाञ्छन is without a mark."),
             ("Of a red colour", "Red would be रक्त; अलाञ्छन is without a mark.")],
            "लाञ्छन = mark; अ-लाञ्छन = without its mark.",
            "अलाञ्छन = unmarked."),
        order(1, "Put the paired words of card 3 in the printed order.",
              ["तेजस्वि", "अतेजः", "शुक्लम्", "कृष्णम्", "असत्", "सत्"],
              "Bright; lightless; white; black; unreal; real.",
              "तेजस्वि → अतेजः → शुक्लम् → कृष्णम् → असत् → सत्."),
        match(2, "Match each word of card 3 to its meaning.",
              [["तेजस्वि", "bright"], ["अतेजः", "lightless"], ["शुक्ल", "white"], ["कृष्ण", "black"],
               ["असत्", "unreal"]],
              "तेजस्वि = bright, अतेजः = lightless, शुक्ल = white, कृष्ण = black, असत् = unreal.",
              "तेजस्वि, अतेजः, शुक्ल, कृष्ण, असत्.", role="extend",
              teaches="The words of card 3 come in opposite pairs; अ- forms the opposite of तेजः and सत्."),
        mcq("discriminate", 3, "By card 3, what does अनेत्ररोगः say about the man?",
            ("He has no disease of the eye", "अ-नेत्र-रोगः: one without eye disease (bahuvrīhi)."),
            [("He has a disease of the eye", "The negating अ- says the opposite: no eye disease."),
             ("He has lost both of his eyes", "Nothing is said of losing the eyes; only no eye disease."),
             ("He can see only in the dark", "Nothing is said of the dark; only no eye disease.")],
            "अ (without) + नेत्र (eye) + रोग (disease): without eye disease.",
            "अनेत्ररोगः = free from eye disease."),
        mcq("apply", 4, "Which split of तद्वच्च in card 3 is right?",
            ("तद्वत् + च", "त् before च → च्: तद्वत् + च → तद्वच्च."),
            [("तद् + वच्च", "वच्च is not a word; the adverb is तद्वत्."),
             ("तद्व + च्च", "तद्व and च्च are not words; the split is तद्वत् + च."),
             ("तद्वच् + च", "तद्वच् is not a word; the adverb ends in त्.")],
            "तद्वत् (likewise) + च (and).",
            "त् + च → च्च."),
        mcq("transfer", 5, "By the pattern of तद्वत् + च → तद्वच्च, how is एतत् + च (and this) joined in a new example?",
            ("एतच्च", "त् before च → च्: एतत् + च → एतच्च."),
            [("एतद्च", "द् comes before a voiced sound; च is voiceless."),
             ("एतज्च", "ज् comes before ज or झ, not before च."),
             ("एतश्च", "श् comes from a visarga before च, not from त्.")],
            "एतत् + च = एतच्च, like तद्वत् + च = तद्वच्च.",
            "त् + च → च्च.",
            teaches="A final त् before च becomes च्: तद्वत् + च → तद्वच्च."),
    ],
}

# ---------------------------------------------------------------- unit 4
AUTHORED["4"] = {
    "title": "जाग्रद्रक्षांसि गंधर्वान्",
    "question": "By card 4, which beings are seen while awake, and what does the text say of the one who sees them?",
    "rule": ("While awake (जाग्रत्) he sees demons (रक्षांसि), gandharvas, pretas and others of that kind, a form, an "
             "altered shape, and likewise: 'he who sees (these) perishes' (यः पश्यति स नश्यति)."),
    "limits": ("Verse, medium confidence. व्याकृति is flagged: विकृति is the commoner word and an accusative "
               "व्याकृतिम् is expected; whether रूपं व्याकृति is one phrase or two is open: no question on it. The "
               "beings are not identified further. The data takes cards 2 to 4 as probably one sentence."),
    "explain_hi": ("जागते हुए (जाग्रत्) जो राक्षसों, गन्धर्वों, प्रेतों और वैसे ही दूसरों को देखता है, उसके लिए पाठ कहता है: ‘जो देखता है, वह नष्ट हो जाता है’। "
                   "गन्धर्व = दिव्य प्राणियों का एक वर्ग, प्रेत = मृतकों की आत्मा; डेटा इनकी आगे कोई पहचान नहीं करता। "
                   "‘रूपं व्याकृति’ का पाठ पक्का नहीं: छपा ‘व्याकृति’ असामान्य है और द्वितीया ‘व्याकृतिम्’ अपेक्षित है। "
                   "डेटा के अनुसार कार्ड २ से यहाँ तक सम्भवतः एक ही वाक्य है, और ‘यः पश्यति स नश्यति’ उसकी क्रिया और परिणाम देता है। "
                   "‘जाग्रद्रक्षांसि’ में त् घोष व्यंजन र से पहले द् बना है।"),
    "hook": "जागते में राक्षस-प्रेत दिखें: यः पश्यति स नश्यति।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "In card 4, what does जाग्रत् mean?",
            ("While awake", "जाग्रत् = waking, while awake (present participle of जागृ)."),
            [("While asleep", "Asleep would be सुप्त; जाग्रत् is while awake."),
             ("While ailing", "Ailing would be आतुर; जाग्रत् is while awake."),
             ("While eating", "Eating would be अश्नन्; जाग्रत् is while awake.")],
            "जाग्रत् = while awake: the beings are seen not in a dream.",
            "जाग्रत् = awake."),
        order(1, "Put these words of card 4 in the printed order.",
              ["जाग्रत्", "रक्षांसि", "गन्धर्वान्", "प्रेतान्", "यः पश्यति", "स नश्यति"],
              "While awake; demons; gandharvas; pretas; he who sees; he perishes.",
              "जाग्रत् → रक्षांसि → गन्धर्वान् → प्रेतान् → यः पश्यति → स नश्यति."),
        match(2, "Match each word of card 4 to its meaning.",
              [["रक्षस्", "demon"], ["प्रेत", "spirit of the dead"], ["गन्धर्व", "a class of celestial beings"],
               ["पश्यति", "sees"], ["नश्यति", "perishes"]],
              "रक्षस् = demon, प्रेत = spirit of the dead, गन्धर्व = celestial being, पश्यति = sees, नश्यति = perishes.",
              "रक्षस्, प्रेत, गन्धर्व, पश्यति, नश्यति.", role="extend",
              teaches="यः ... सः (who ... he) pairs a relative clause with its main clause: यः पश्यति स नश्यति."),
        multi("discriminate", 3, "Which statements fit card 4?",
              [("It says the beings are seen in a dream", "Not stated: जाग्रत् says he is awake."),
               ("It names demons, gandharvas and pretas", "Stated: रक्षांसि गन्धर्वान् प्रेतान्."),
               ("It ends: he who sees perishes", "Stated: यः पश्यति स नश्यति."),
               ("It describes how a gandharva looks", "Not stated: no further identification is made.")],
              [1, 2],
              "Awake, he sees demons, gandharvas, pretas and the like: he who sees perishes.",
              "जाग्रत् ... यः पश्यति स नश्यति."),
        mcq("apply", 4, "Why is जाग्रत् printed जाग्रद् before रक्षांसि in card 4?",
            ("त् before a voiced consonant → द्", "र is a voiced consonant: जाग्रत् + रक्षांसि → जाग्रद्रक्षांसि."),
            [("त् before every consonant → द्", "Not every: before a voiceless one such as च it does not become द्."),
             ("द् is the stem's own last letter", "The participle's stem is जाग्रत्; द् comes only from sandhi."),
             ("त् before र always becomes र्", "There is no such change; त् becomes द् before the voiced र.")],
            "जाग्रत् + रक्षांसि: त् before the voiced र → द्.",
            "त् + voiced consonant → द्."),
        mcq("transfer", 5, "By the pattern of यः पश्यति स नश्यति, which word fills यः पठति ___ जानाति (who studies, he knows) in a new example?",
            ("स", "सः drops its visarga before any consonant: सः + जानाति → स जानाति, like स नश्यति."),
            [("सो", "सो (with ऽ) comes only before अ: सोऽपि; ज is a consonant."),
             ("सः", "Before a consonant सः loses its visarga: स जानाति."),
             ("सा", "सा is feminine; it cannot pick up the masculine यः.")],
            "यः पठति स जानाति, like यः पश्यति स नश्यति.",
            "सः + consonant → स.",
            teaches="The pronoun सः drops its visarga before any consonant: सः + नश्यति → स नश्यति."),
    ],
}

# ---------------------------------------------------------------- unit 5
AUTHORED["5"] = {
    "title": "महर्षीणां समीपस्थां",
    "question": "By card 5, which three sky objects does the man fail to see, and what does the text say follows?",
    "rule": ("He who does not see Arundhatī standing near the great sages, or Dhruva, or the Ākāśagaṅgā: he does "
             "not see that year (न स पश्यति तां समाम्)."),
    "limits": ("Verse, medium confidence. Data labels: Arundhatī = Alcor, Dhruva = the pole star, the great sages = "
               "the Great Bear (all probable); Ākāśagaṅgā = the Milky Way (standard). 'Does not see that year' is "
               "literal; 'will not live it out' is only probable."),
    "explain_hi": ("जो महर्षियों के समीप स्थित अरुन्धती को, या ध्रुव को, या आकाशगंगा को नहीं देखता, पाठ कहता है: ‘वह उस वर्ष को नहीं देखता’। "
                   "डेटा की पहचान: अरुन्धती सम्भवतः अलकोर तारा, ध्रुव सम्भवतः ध्रुवतारा, महर्षि सम्भवतः सप्तर्षि यानी सप्तर्षि-मण्डल के तारे, और आकाशगंगा मानक रूप से आकाशगंगा। "
                   "समा = वर्ष; ‘उस वर्ष को नहीं देखता’ का अर्थ डेटा सम्भवतः यह लेता है कि वह वर्ष पूरा नहीं जीता, पर संस्कृत केवल ‘नहीं देखता’ कहती है। "
                   "‘महर्षीणाम्’ में महा + ऋषि की सन्धि है (आ + ऋ → अर्)।"),
    "hook": "अरुन्धती, ध्रुव, आकाशगंगा न दिखें: ‘न स पश्यति तां समाम्’।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "In card 5, what does समा mean?",
            ("Year", "समा (f.) = year: तां समाम्, that year."),
            [("Night", "Night would be रात्रि; समा here is year."),
             ("Month", "Month would be मास; समा here is year."),
             ("Lamp", "Lamp would be दीप; समा here is year.")],
            "समा = year: न स पश्यति तां समाम्.",
            "समा = year."),
        order(1, "Put these parts of card 5 in the printed order.",
              ["महर्षीणां समीपस्थाम्", "अरुन्धतीम्", "ध्रुवम्", "आकाशगङ्गाम्", "न स पश्यति तां समाम्"],
              "Standing near the great sages; Arundhatī; Dhruva; the Ākāśagaṅgā; he does not see that year.",
              "महर्षीणां समीपस्थाम् → अरुन्धतीम् → ध्रुवम् → आकाशगङ्गाम् → न स पश्यति तां समाम्."),
        match(2, "Match each word of card 5 to its meaning.",
              [["महर्षि", "great sage"], ["समीपस्थ", "standing near"], ["ध्रुव", "the fixed one"],
               ["न", "not"], ["समा", "year"]],
              "महर्षि = great sage, समीपस्थ = standing near, ध्रुव = the fixed one, न = not, समा = year.",
              "महर्षि, समीपस्थ, ध्रुव, न, समा.", role="extend",
              teaches="समीप-स्थ is a tat-puruṣa: 'standing (स्थ) near (समीप)'."),
        mcq("discriminate", 3, "By card 5, which identification does the data mark standard, not only probable?",
            ("Ākāśagaṅgā = the Milky Way", "The data labels ākāśagaṅgā = the Milky Way as standard."),
            [("Arundhatī = the star Alcor", "The data labels Arundhatī = Alcor only as probable."),
             ("Dhruva = the pole star", "The data labels Dhruva = the pole star only as probable."),
             ("The sages = the Great Bear", "The data labels the great sages = the Great Bear as probable.")],
            "Only ākāśagaṅgā = Milky Way is standard; the other three are probable.",
            "आकाशगङ्गा = Milky Way (standard)."),
        mcq("apply", 4, "Which split of महर्षीणाम् in card 5 is right?",
            ("महा + ऋषीणाम्", "आ + ऋ → अर्: महा + ऋषीणाम् → महर्षीणाम्."),
            [("मह + र्षीणाम्", "र्षीणाम् is not a word; the र् comes from ऋ."),
             ("महा + र्षीणाम्", "र्षीणाम् is not a word; the noun is ऋषि."),
             ("महा + अर्षीणाम्", "अर्षि is not a word; the noun is ऋषि.")],
            "महा (great) + ऋषीणाम् (of the sages).",
            "आ + ऋ → अर्."),
        mcq("transfer", 5, "By the pattern of महा + ऋषि → महर्षि, how is राजा + ऋषिः (royal sage) joined in a new example?",
            ("राजर्षिः", "आ + ऋ → अर्: राजा + ऋषिः → राजर्षिः."),
            [("राजार्षिः", "The long आ does not stay: आ + ऋ gives अर्."),
             ("राजेर्षिः", "ए comes from अ/आ + इ or ई, not from आ + ऋ."),
             ("राजौर्षिः", "औ comes from अ/आ + ओ or औ, not from आ + ऋ.")],
            "राजा + ऋषिः = राजर्षिः, like महा + ऋषि = महर्षि.",
            "आ + ऋ → अर्.",
            teaches="अ or आ followed by ऋ gives अर्: महा + ऋषीणाम् → महर्षीणाम्."),
    ],
}

# ---------------------------------------------------------------- unit 6
AUTHORED["6"] = {
    "title": "मेघतोयौघनिर्घोष",
    "question": "By card 6, which sounds are heard though not there, and what is the reverse failing?",
    "rule": ("He hears sounds born of the roar of cloud and flood-water, of the vīṇā, the paṇava and the flute "
             "(वेणु), and other sounds that are not there; or he does not hear even existing ones (न सतोऽपि वा)."),
    "limits": ("Verse, medium confidence. Printed वीण is probably the stem वीणा (flagged); printed शब्दानसंतो is "
               "probably शब्दान् असतः (flagged): no question on either form. पणव = a small drum (probable). The verb "
               "of the second half is carried from शृणोति; no result clause is in this card."),
    "explain_hi": ("कार्ड में सुनने का विपर्यय है: जो बादल और जल-प्रवाह की गर्जना, वीणा, पणव और बाँसुरी से उत्पन्न, और दूसरे अविद्यमान शब्द सुनता है। "
                   "उलटा दोष भी कहा है: वह विद्यमान शब्दों को भी नहीं सुनता (न सतोऽपि वा); ‘सुनता’ शृणोति से लिया जाता है। "
                   "पणव सम्भवतः छोटा ढोल है; वेणु = बाँस की बाँसुरी। "
                   "छपा ‘वीण’ समास में सम्भवतः ‘वीणा’ है, और छपा ‘असंतो’ सम्भवतः द्वितीया ‘असतः’; इन रूपों पर प्रश्न नहीं। "
                   "इस कार्ड में परिणाम-वाक्य नहीं है; डेटा के अनुसार वाक्य कार्ड ७ में आगे चलता है।"),
    "hook": "जो शब्द नहीं हैं वे सुनाई दें, जो हैं वे नहीं: सुनने का विपर्यय।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "In card 6, what does वेणु mean?",
            ("Flute", "वेणु = bamboo flute."),
            [("Conch", "Conch would be शङ्ख; वेणु is the flute."),
             ("Bell", "Bell would be घण्टा; वेणु is the flute."),
             ("Lute", "The lute is वीणा, a separate member of the compound.")],
            "वेणु = the bamboo flute, one of the sound sources of card 6.",
            "वेणु = flute."),
        order(1, "Put the sound sources of card 6 in the printed order.",
              ["मेघतोयौघनिर्घोष", "वीण", "पणव", "वेणु"],
              "The roar of cloud and flood-water; the vīṇā (printed वीण); the paṇava; the flute.",
              "मेघतोयौघनिर्घोष → वीण → पणव → वेणु."),
        match(2, "Match each word of card 6 to its meaning.",
              [["मेघ", "cloud"], ["तोय", "water"], ["ओघ", "flood"], ["निर्घोष", "roar"], ["शृणोति", "hears"]],
              "मेघ = cloud, तोय = water, ओघ = flood, निर्घोष = roar, शृणोति = hears.",
              "मेघ, तोय, ओघ, निर्घोष, शृणोति.", role="extend",
              teaches="-ज at the end of a compound means 'born of': पणववेणुजान् = (sounds) born of the drum and flute."),
        mcq("discriminate", 3, "By the data's reading of card 6, what does न सतोऽपि वा add?",
            ("Or not hearing even real sounds", "न सतः अपि वा: or (he does) not (hear) even existing sounds."),
            [("Or hearing only very loud sounds", "Nothing about loudness is said; it is a failure to hear."),
             ("Or hearing the sounds in a dream", "Nothing about dreams is said; it is a failure to hear."),
             ("Or hearing each sound two times", "Nothing about repetition is said; it is a failure to hear.")],
            "The reversal goes both ways: unreal sounds heard, real ones not heard.",
            "न सतोऽपि वा = or not even existing ones."),
        mcq("apply", 4, "Which split of सतोऽपि in card 6 is right?",
            ("सतः + अपि", "अः + अ → ओऽ: सतः + अपि → सतोऽपि."),
            [("सतो + पि", "पि is not a word; the अ of अपि is shown by ऽ."),
             ("सत + उपि", "उपि is not a word; the second word is अपि."),
             ("सतोऽ + अपि", "सतोऽ is not a word; the first word is सतः.")],
            "सतः (existing) + अपि (even).",
            "अः + अ → ओऽ."),
        mcq("transfer", 5, "By the pattern of सतः + अपि → सतोऽपि, how is रामः + अपि (Rāma too) joined in a new example?",
            ("रामोऽपि", "अः + अ → ओ, and the अ is dropped and shown by ऽ: रामोऽपि."),
            [("रामापि", "The visarga does not vanish into a long आ; अः + अ gives ओऽ."),
             ("रामरपि", "र् comes from a visarga after a vowel other than अ/आ; here it is अः."),
             ("रामौपि", "औ does not arise from a visarga; अः + अ gives ओऽ.")],
            "रामः + अपि = रामोऽपि, like सतः + अपि = सतोऽपि.",
            "अः + अ → ओऽ.",
            teaches="अः before अ becomes ओ and the following अ is elided (ऽ): सतः + अपि → सतोऽपि."),
    ],
}

# ---------------------------------------------------------------- unit 7
AUTHORED["7"] = {
    "title": "निष्पीड्य कर्णौ शृणुयान्न",
    "question": "By card 7, what does the man fail to hear with his ears pressed, and how does he take the other senses?",
    "rule": ("He who, having pressed both ears (निष्पीड्य कर्णौ), would not hear the sound dhukadhukā; likewise he who "
             "takes smells, tastes and touches by reversal (विपर्ययात्)."),
    "limits": ("Verse, medium confidence. Printed वंध is read गन्ध (smell), probable, near certain, but still a "
               "change: no question rests on it. धुकधुका is an onomatopoeic sound; what makes it is not said "
               "(unidentified): no question on it. Which opposite he perceives is not stated."),
    "explain_hi": ("जो दोनों कानों को दबाकर (निष्पीड्य कर्णौ) धुकधुका ध्वनि नहीं सुनता, वह भी इस सूची में है। "
                   "धुकधुका धड़कने या धमक जैसी बार-बार की ध्वनि का अनुकरण-शब्द है; पाठ नहीं बताता कि यह किससे होती है। "
                   "इसी प्रकार जो गन्ध, रस और स्पर्श को विपर्यय से, यानी उलटा मानता है; कौन-सा उलटा, यह नहीं कहा गया। "
                   "छपा ‘वंध’ कोई शब्द नहीं; ‘गन्ध’ लगभग निश्चित सुधार है, फिर भी छपे पाठ से भिन्न है। "
                   "‘शृणुयात्’ विधिलिङ् (सम्भावना) है: ‘सुने’, ‘सुन सके’।"),
    "hook": "कान दबाकर भी धुकधुक न सुने; रस-स्पर्श उलटे लगें।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "In card 7, what does निष्पीड्य mean?",
            ("Having pressed", "निः-पीड् + -य: having pressed (absolutive)."),
            [("Having washed", "Washing would be प्रक्षाल्य; निष्पीड्य is having pressed."),
             ("Having pierced", "Piercing would be विद्ध्वा; निष्पीड्य is having pressed."),
             ("Having opened", "Opening would be उद्घाट्य; निष्पीड्य is having pressed.")],
            "निष्पीड्य कर्णौ = having pressed both ears.",
            "निष्पीड्य = having pressed."),
        order(1, "Put the words of line 1 of card 7 in the printed order.",
              ["निष्पीड्य", "कर्णौ", "शृणुयात्", "न", "यः", "धुकधुकास्वनम्"],
              "Having pressed; both ears; would hear; not; who; the sound dhukadhukā.",
              "निष्पीड्य → कर्णौ → शृणुयात् → न → यः → धुकधुकास्वनम्."),
        match(2, "Match each word of card 7 to its meaning.",
              [["कर्ण", "ear"], ["स्वन", "sound"], ["रस", "taste"], ["स्पर्श", "touch"], ["विपर्यय", "reversal"]],
              "कर्ण = ear, स्वन = sound, रस = taste, स्पर्श = touch, विपर्यय = reversal.",
              "कर्ण, स्वन, रस, स्पर्श, विपर्यय.", role="extend",
              teaches="कर्णौ is a dual: 'the two ears', ears coming as a natural pair."),
        mcq("discriminate", 3, "By card 7, in what way does the man take tastes and touches (रस, स्पर्श)?",
            ("By reversal", "विपर्ययात् मन्यते: he takes them by reversal."),
            [("Twice as strongly", "Nothing about strength is said; he takes them reversed."),
             ("Only when asleep", "Nothing about sleep is said; he takes them reversed."),
             ("Only on one side", "Nothing about a side is said; he takes them reversed.")],
            "विपर्ययात् = by reversal: what he perceives is taken as its opposite.",
            "विपर्ययात् मन्यते = takes by reversal."),
        mcq("apply", 4, "By its grammar label in card 7, what kind of form is शृणुयात्?",
            ("Optative 3 sg.: would hear", "शृणुयात् = 3 sg. optative of श्रु: 'would hear'."),
            [("Future 3 sg.: will hear", "The future would be श्रोष्यति; -यात् here is optative."),
             ("Past 3 sg.: he heard", "A past would be अशृणोत्; -यात् here is optative."),
             ("Absolutive: having heard", "The absolutive would be श्रुत्वा; शृणुयात् is a finite verb.")],
            "शृणुयात् न = would not hear: an optative.",
            "शृणुयात् = optative, 'would hear'."),
        mcq("transfer", 5, "By the pattern of निष्पीड्य (prefix + root + -य, having pressed), what does उपविश्य mean in a new example?",
            ("Having sat down", "उप-विश् + -य: with a prefix the absolutive ends in -य: having sat down."),
            [("Sitting down now", "The present participle would be उपविशन्; -य marks the absolutive."),
             ("He will sit down", "The future would be उपवेक्ष्यति; -य marks the absolutive."),
             ("He sat down then", "A past would be उपाविशत्; -य marks the absolutive.")],
            "उपविश्य = having sat down, like निष्पीड्य = having pressed.",
            "Prefix + root + -य = having done.",
            teaches="With a prefix the absolutive takes -य, not -त्वा: निः + पीड् → निष्पीड्य (without one: श्रुत्वा)."),
    ],
}

# ---------------------------------------------------------------- unit 8
AUTHORED["8"] = {
    "title": "यश्च दीपगंधं नजिघ्रति",
    "question": "By card 8, which smell does the man fail to perceive, and which line is too damaged to read?",
    "rule": ("Or he who does not (perceive them) at all (सर्वशो वा न यः), and he who does not smell the odour of a "
             "lamp (यश्च दीपगन्धं न जिघ्रति). The second line is damaged in print."),
    "limits": ("Prose, low confidence; two printed lines joined. The verb of सर्वशो वा न यो is probably carried "
               "from मन्यते of card 7. Line 2 has a damaged word (स्वास्थ्येाधाया-); its sense is a guess: no "
               "question on line 2. Whether the lamp is burning or put out is not said."),
    "explain_hi": ("पहली पंक्ति: ‘या जो सर्वथा नहीं, और जो दीपक की गन्ध नहीं सूँघता’। "
                   "‘सर्वशो वा न यो’ की क्रिया छपी नहीं; डेटा सम्भवतः कार्ड ७ का ‘मन्यते’ लेता है: जो उन्हें बिल्कुल भी अनुभव नहीं करता। "
                   "दीपगन्ध = दीपक की गन्ध; दीपक जलता हुआ है या बुझा, यह नहीं कहा गया। "
                   "दूसरी पंक्ति का बीच का शब्द छपाई में टूटा है; रस और विधि के बारे में उसका अर्थ केवल अनुमान है, इसलिए उस पर प्रश्न नहीं। "
                   "‘सर्वशो वा’ में अः घोष व्यंजन व से पहले ओ बना है।"),
    "hook": "दीपक की गन्ध भी न आए: गन्ध का लोप।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "In card 8, what does जिघ्रति mean?",
            ("Smells", "जिघ्रति = smells (present of घ्रा)."),
            [("Sees", "Sees would be पश्यति; जिघ्रति is smells."),
             ("Tastes", "Tastes would be आस्वादयति; जिघ्रति is smells."),
             ("Hears", "Hears would be शृणोति; जिघ्रति is smells.")],
            "न जिघ्रति = does not smell.",
            "जिघ्रति = smells."),
        order(1, "Put the parts of line 1 of card 8 in the printed order.",
              ["सर्वशो", "वा न यो", "यश्च", "दीपगंधं", "नजिघ्रति"],
              "Wholly; or not, who; and who; the smell of a lamp; does not smell.",
              "सर्वशो → वा न यो → यश्च → दीपगंधं → नजिघ्रति."),
        match(2, "Match each sure word of card 8 to its meaning.",
              [["सर्वशः", "wholly, altogether"], ["दीप", "lamp"], ["गन्ध", "smell"], ["जिघ्रति", "smells"],
               ["च", "and"]],
              "सर्वशः = wholly, दीप = lamp, गन्ध = smell, जिघ्रति = smells, च = and.",
              "सर्वशः, दीप, गन्ध, जिघ्रति, च.", role="extend",
              teaches="दीप-गन्ध is a tat-puruṣa: 'the smell (गन्ध) of a lamp (दीप)'."),
        mcq("discriminate", 3, "By line 1 of card 8, which smell does the man fail to perceive?",
            ("The smell of a lamp", "यश्च दीपगन्धं न जिघ्रति: who does not smell the lamp's odour."),
            [("The smell of flowers", "Flowers are not named; the line names a lamp."),
             ("The smell of cooked food", "Food is not named; the line names a lamp."),
             ("The smell of his own body", "The body is not named; the line names a lamp.")],
            "दीप-गन्ध = the smell of a lamp.",
            "दीपगन्धं न जिघ्रति = does not smell a lamp."),
        mcq("apply", 4, "Why is सर्वशः printed सर्वशो before वा in card 8?",
            ("अः before a voiced consonant → ओ", "व is voiced: सर्वशः + वा → सर्वशो वा."),
            [("अः before any consonant → ओ", "Not any: before a voiceless त the visarga becomes स्."),
             ("ओ is the adverb's own ending", "The adverb is सर्वशः; ओ comes only from sandhi."),
             ("आः before a voiced consonant → ओ", "आः drops its visarga before a voiced sound; it gives no ओ.")],
            "सर्वशः + वा: अः before the voiced consonant व → ओ.",
            "अः + voiced consonant → ओ."),
        mcq("transfer", 5, "By the pattern सर्वशः + वा → सर्वशो वा, how is बालः + गच्छति (the boy goes) joined in a new example?",
            ("बालो गच्छति", "अः before the voiced consonant ग → ओ: बालो गच्छति."),
            [("बाला गच्छति", "Dropping the visarga to आ is the rule for आः, not अः."),
             ("बालर्गच्छति", "र् comes from a visarga after a vowel other than अ/आ."),
             ("बालश्गच्छति", "श् comes from a visarga before च, छ or श, not before ग.")],
            "बालः + गच्छति = बालो गच्छति, like सर्वशः + वा = सर्वशो वा.",
            "अः + voiced consonant → ओ.",
            teaches="अः before a voiced consonant (here ग, व) becomes ओ: सर्वशः + वा → सर्वशो वा."),
    ],
}

# ---------------------------------------------------------------- unit 9
AUTHORED["9"] = {
    "title": "योऽंगे घातं न वेत्ति वा",
    "question": "By card 9, which loss of feeling does the text name, and what is the man said to be without?",
    "rule": ("He whose limbs are strewn as if with dust (conjectural), or who is not aware of a blow on his limb "
             "(योऽङ्गे घातं न वेत्ति); without severe austerity (अन्तरेण तपस्तीव्रम्), or yoga ..."),
    "limits": ("Verse, medium confidence. Printed पं शुनेव is read पांशुनेव ('as if with dust') as a conjecture: no "
               "question on it. वाविधिपूर्वकम् can be वा + विधिपूर्वकम् (by rule) or वा + अविधिपूर्वकम्: no question on "
               "it. The sentence runs on into card 10 (he knows what is beyond the senses)."),
    "explain_hi": ("जो अंग पर लगी चोट को नहीं जानता (योऽङ्गे घातं न वेत्ति), वह भी इस सूची में है। "
                   "पहला अंश ‘जिसके अंग मानो धूल से ढके हों’ अनुमानित पाठ पर है: छपा ‘पं शुनेव’ कोई अर्थ नहीं देता, ‘पांशुनेव’ सुझाव है। "
                   "दूसरी पंक्ति: तीव्र तप के बिना (अन्तरेण तपस्तीव्रम्), अथवा योग के बिना; ‘वाविधिपूर्वकम्’ विधिपूर्वक या अविधिपूर्वक, दोनों पढ़ा जा सकता है। "
                   "डेटा विधिपूर्वक को अधिक समर्थित मानता है, क्योंकि यह छपाई वा + अ- पर अन्यत्र अवग्रह लिखती है। "
                   "वाक्य कार्ड १० में आगे चलता है: ‘इन्द्रियों से परे को जानता है’।"),
    "hook": "अंग पर चोट लगे पर पता न चले; तप के बिना परे का ज्ञान।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "In card 9, what does घात mean?",
            ("Blow", "घात = a blow or stroke: अङ्गे घातम्, a blow on the limb."),
            [("Meal", "Food would be अन्न; घात is a blow."),
             ("Sleep", "Sleep would be निद्रा; घात is a blow."),
             ("Fever", "Fever would be ज्वर; घात is a blow.")],
            "घात = blow, stroke.",
            "घात = blow."),
        order(1, "Put these sure parts of card 9 in the printed order.",
              ["योऽंगे", "घातं", "न वेत्ति वा", "अंतरेण", "तपस्तीव्रं"],
              "Who, on the limb; a blow; does not know, or; without; severe austerity.",
              "योऽंगे → घातं → न वेत्ति वा → अंतरेण → तपस्तीव्रं."),
        match(2, "Match each sure word of card 9 to its meaning.",
              [["अङ्ग", "limb, body"], ["घात", "blow"], ["वेत्ति", "knows"], ["अन्तरेण", "without"],
               ["तीव्र", "severe"]],
              "अङ्ग = limb, घात = blow, वेत्ति = knows, अन्तरेण = without, तीव्र = severe.",
              "अङ्ग, घात, वेत्ति, अन्तरेण, तीव्र.", role="extend",
              teaches="अन्तरेण, 'without', takes the accusative: अन्तरेण तपः तीव्रम् = without severe austerity."),
        T(multi("discriminate", 3, "Which statements fit the sure parts of card 9?",
                [("It names unawareness of a blow on the limb", "Stated: योऽङ्गे घातं न वेत्ति."),
                 ("It says the man feels every blow sharply", "Not stated: he is not aware of the blow."),
                 ("It says the man is a skilled yogin", "Not stated: the line is 'without' tapas or yoga."),
                 ("It speaks of severe austerity, तपस्तीव्रम्", "Stated: अन्तरेण तपस्तीव्रम्, without severe austerity.")],
                [0, 3],
                "Sure: no awareness of a blow; 'without severe austerity'.",
                "योऽङ्गे घातं न वेत्ति; अन्तरेण तपस्तीव्रम्."),
          "Questions keep to the sure words; the dust reading and the yoga reading stay open."),
        mcq("apply", 4, "Which split of तपस्तीव्रं in card 9 is right?",
            ("तपः + तीव्रम्", "Visarga before त → स्: तपः + तीव्रम् → तपस्तीव्रम्."),
            [("तप + स्तीव्रम्", "स्तीव्रम् is not a word; the स् comes from the visarga."),
             ("तपः + स्तीव्रम्", "स्तीव्रम् is not a word; the adjective is तीव्रम्."),
             ("तपस्ती + व्रम्", "Neither part is a word; the split is तपः + तीव्रम्.")],
            "तपः (austerity) + तीव्रम् (severe).",
            "ः + त → स्त."),
        mcq("transfer", 5, "By the pattern तपः + तीव्रम् → तपस्तीव्रम्, how is मनः + तु (but the mind) joined in a new example?",
            ("मनस्तु", "Visarga before त becomes स्: मनः + तु → मनस्तु."),
            [("मनोतु", "ओ arises before a voiced consonant; त is voiceless."),
             ("मनश्तु", "श् comes before च, छ or श, not before त."),
             ("मनर्तु", "र् comes from a visarga after a vowel other than अ/आ.")],
            "मनः + तु = मनस्तु, like तपः + तीव्रम् = तपस्तीव्रम्.",
            "ः + त → स्त.",
            teaches="A visarga before त or थ becomes स्: तपः + तीव्रम् → तपस्तीव्रम्."),
    ],
}

# ---------------------------------------------------------------- unit 10
AUTHORED["10"] = {
    "title": "जिव्हाश्यावा मुखं पूति",
    "question": "By card 10, what does the text say of those who know the supersensory, and which three signs follow?",
    "rule": ("And he who knows what is beyond the senses (अतीन्द्रियम्): of them one should foretell death (तेषां "
             "मरणमादिशेत्). Then: the tongue dusky (श्यावा), the mouth putrid (पूति), the left eye sinks in."),
    "limits": ("Verse, medium confidence. Who foretells is not stated (the physician is understood). तेषाम् is "
               "plural against the singular यः. The signs of line 2 run on into card 11, where 'him one should "
               "avoid' completes them; no verb 'is' is printed."),
    "explain_hi": ("पहली पंक्ति कार्ड ९ के वाक्य को पूरा करती है: ‘और जो इन्द्रियों से परे (अतीन्द्रिय) को जानता है, उनके मरण का कथन करना चाहिए’। "
                   "कथन कौन करे, यह नहीं कहा गया; वैद्य समझा जाता है, और ‘तेषाम्’ बहुवचन ऐसे सब लोगों के वर्ग को बताता है। "
                   "दूसरी पंक्ति नए लक्षण देती है: जीभ श्याव (गहरी साँवली), मुख दुर्गन्ध वाला, और बायीं आँख धँस जाती है। "
                   "ये लक्षण कार्ड ११ के ‘यस्य तं परिवर्जयेत्’ तक चलते हैं। "
                   "छपा ‘जिव्हा’ ‘जिह्वा’ का मान्य रूपान्तर है।"),
    "hook": "साँवली जीभ, दुर्गन्ध मुख, बायीं आँख धँसी।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "In card 10, what does अतीन्द्रिय mean?",
            ("Beyond the senses", "अति (beyond) + इन्द्रिय (sense): what lies beyond the senses."),
            [("Pleasing the senses", "Pleasing would be इन्द्रियप्रिय; अतीन्द्रिय is beyond them."),
             ("Lacking the senses", "Lacking would be निरिन्द्रिय; अतीन्द्रिय is beyond them."),
             ("Of the sense organs", "That would be ऐन्द्रिय; अतीन्द्रिय is beyond them.")],
            "अतीन्द्रियम् = the supersensory, what lies beyond the senses.",
            "अतीन्द्रिय = beyond the senses."),
        order(1, "Put the signs of line 2 of card 10 in the printed order.",
              ["जिव्हा श्यावा", "मुखं पूति", "सव्यमक्षि", "निमज्जति"],
              "The tongue dusky; the mouth putrid; the left eye; sinks in.",
              "जिव्हा श्यावा → मुखं पूति → सव्यमक्षि → निमज्जति."),
        match(2, "Match each word of card 10 to its meaning.",
              [["जिव्हा", "tongue"], ["श्याव", "dusky"], ["पूति", "putrid"], ["सव्य", "left"],
               ["निमज्जति", "sinks in"]],
              "जिव्हा = tongue, श्याव = dusky, पूति = putrid, सव्य = left, निमज्जति = sinks in.",
              "जिव्हा, श्याव, पूति, सव्य, निमज्जति.", role="extend",
              teaches="Adjectives agree with their nouns: जिव्हा श्यावा (f.), मुखं पूति (n.), सव्यम् अक्षि (n.)."),
        mcq("discriminate", 3, "By card 10, which eye is said to sink in?",
            ("The left eye", "सव्यम् अक्षि निमज्जति: the left eye sinks in."),
            [("The right eye", "The right would be दक्षिण; the line says सव्य, left."),
             ("Both of the eyes", "Both would need a dual; सव्यम् अक्षि is one, the left."),
             ("The eye that weeps", "Weeping is not named; the line says the left eye.")],
            "सव्य = left: the left eye sinks in.",
            "सव्यम् अक्षि = the left eye."),
        mcq("apply", 4, "Which split of जानात्यतींद्रियं in card 10 is right?",
            ("जानाति + अतीन्द्रियम्", "इ + अ → य: जानाति + अतीन्द्रियम् → जानात्यतीन्द्रियम्."),
            [("जानात् + यतीन्द्रियम्", "जानात् and यतीन्द्रिय are not the words here."),
             ("जानाती + तीन्द्रियम्", "तीन्द्रिय is not a word; the noun is अतीन्द्रिय."),
             ("जान + अत्यतीन्द्रियम्", "जान is not the verb form; it is जानाति.")],
            "जानाति (knows) + अतीन्द्रियम् (the supersensory).",
            "इ + unlike vowel → य्."),
        mcq("transfer", 5, "By the pattern of आदिशेत् (one should declare), what does पठेत् mean in a new example?",
            ("One should read", "पठेत्, like आदिशेत्, is an optative: 'one should read'."),
            [("One has read", "A past form would be needed; -एत् here is optative."),
             ("One will read", "The future would be पठिष्यति; -एत् here is optative."),
             ("One is reading", "The present would be पठति; -एत् here is optative.")],
            "पठेत् = one should read, like आदिशेत् = one should declare.",
            "-एत् (after an अ-stem verb) = optative 'should'.",
            teaches="Verbs with an अ-stem form the optative in -एत्: आदिशेत्, परिवर्जयेत्. Not every optative ends so: शृणुयात् (card 7)."),
    ],
}

# ---------------------------------------------------------------- unit 11
AUTHORED["11"] = {
    "title": "खगा वा मूर्ध्नि लीयंते",
    "question": "By card 11, which sign about birds completes the list, what is said of that man, and how does the next man move?",
    "rule": ("Or he on whose head birds settle (खगा वा मूर्ध्नि लीयन्ते यस्य): him one should avoid (तं परिवर्जयेत्). "
             "He who creeps about with drooping shoulders, as if scraping his two feet (निकषन्निव पादौ)."),
    "limits": ("Verse, high confidence. 'Avoid' is the literal sense; the text gives no reason, and who avoids is "
               "not stated (the physician is understood). Scraping the feet against the ground is not stated. The "
               "second line has no main clause in this card."),
    "explain_hi": ("पहली पंक्ति कार्ड १० के लक्षणों को पूरा करती है: ‘या जिसके सिर पर पक्षी बैठ जाते हैं, उससे बचना चाहिए’। "
                   "‘परिवर्जयेत्’ का शाब्दिक अर्थ ‘त्याग दे, बचे’ है; पाठ कारण नहीं बताता, और बचने वाला वैद्य समझा जाता है। "
                   "दूसरी पंक्ति नया लक्षण शुरू करती है: जो मानो दोनों पैरों को रगड़ता हुआ, ढले कन्धों वाला, इधर-उधर सरकता है। "
                   "पैर किससे रगड़ता है, यह नहीं कहा गया; इस पंक्ति का मुख्य वाक्य इस कार्ड में नहीं। "
                   "‘खगा वा’ में आः का विसर्ग घोष व्यंजन व से पहले लुप्त हुआ है।"),
    "hook": "सिर पर पक्षी बैठें; कन्धे ढले, पैर घिसटते चले।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "In card 11, what does खग mean?",
            ("Bird", "खग = sky-goer, a bird: खगाः, birds."),
            [("Snake", "Snake would be सर्प; खग is a bird."),
             ("Dog", "Dog would be श्वन्; खग is a bird."),
             ("Hair", "Hair would be केश; खग is a bird.")],
            "खगाः मूर्ध्नि लीयन्ते = birds settle on the head.",
            "खग = bird."),
        order(1, "Put the words of line 2 of card 11 in the printed order.",
              ["निकषन्निव", "यः", "पादौ", "च्युतांसः", "परिसर्पति"],
              "As if scraping; who; both feet; with drooping shoulders; creeps about.",
              "निकषन्निव → यः → पादौ → च्युतांसः → परिसर्पति."),
        match(2, "Match each word of card 11 to its meaning.",
              [["मूर्धन्", "head"], ["पाद", "foot"], ["अंस", "shoulder"], ["च्युत", "fallen, drooping"],
               ["परिसर्पति", "creeps about"]],
              "मूर्धन् = head, पाद = foot, अंस = shoulder, च्युत = fallen, परिसर्पति = creeps about.",
              "मूर्धन्, पाद, अंस, च्युत, परिसर्पति.", role="extend",
              teaches="च्युत-अंसः is a bahuvrīhi: 'one whose shoulders (अंस) have dropped (च्युत)'."),
        mcq("discriminate", 3, "By card 11, where do the birds settle?",
            ("On the man's head", "मूर्ध्नि (locative of मूर्धन्): on the head."),
            [("On the man's feet", "The feet (पादौ) belong to the next sign, not the birds."),
             ("On the man's house", "No house is named; मूर्ध्नि is on the head."),
             ("On the man's bed", "No bed is named; मूर्ध्नि is on the head.")],
            "खगा वा मूर्ध्नि लीयन्ते यस्य: birds settle on his head.",
            "मूर्ध्नि = on the head."),
        mcq("apply", 4, "Why is खगाः printed खगा before वा in card 11?",
            ("आः drops its visarga before a voiced sound", "व is voiced: खगाः + वा → खगा वा."),
            [("आः before a voiced consonant → ओ", "ओ comes from अः, not आः; आः just drops the visarga."),
             ("Every visarga is dropped before व", "Not every: अः before व gives ओ (सर्वशो वा, card 8)."),
             ("खगा is the stem's own nominative", "The nominative plural is खगाः; the drop comes from sandhi.")],
            "खगाः + वा: आः before the voiced व drops its visarga.",
            "आः + voiced sound → आ."),
        mcq("transfer", 5, "By the pattern खगाः + वा → खगा वा, how is देवाः + गच्छन्ति (the gods go) joined in a new example?",
            ("देवा गच्छन्ति", "आः drops its visarga before the voiced ग: देवा गच्छन्ति."),
            [("देवो गच्छन्ति", "ओ comes from अः before a voiced consonant, not from आः."),
             ("देवार्गच्छन्ति", "र् comes from a visarga after a vowel other than अ/आ."),
             ("देवाश्गच्छन्ति", "श् comes from a visarga before च, छ or श, not before ग.")],
            "देवाः + गच्छन्ति = देवा गच्छन्ति, like खगाः + वा = खगा वा.",
            "आः + voiced sound → आ.",
            teaches="आः loses its visarga before a voiced sound (vowel or voiced consonant): खगाः + वा → खगा वा."),
    ],
}

# ---------------------------------------------------------------- unit 12
AUTHORED["12"] = {
    "title": "हीयते बलतः शश्वद्",
    "question": "By card 12, which signs link eating with strength and with the amount of faeces and urine?",
    "rule": ("He who, eating much wholesome food, continually declines in strength (हीयते बलतः शश्वत्); he who eats "
             "little and has much faeces and urine (अल्पाशी बहुविण्मूत्रः), and who eats much and has little (बह्वाशी अल्पमूत्रविट्)."),
    "limits": ("Verse, high confidence. The signs are listed only; no reason and no main clause are in this card, "
               "and the list goes on in card 13. 'Though' is not printed: the participle अश्नन् (eating) stands beside "
               "the decline."),
    "explain_hi": ("कार्ड तीन लक्षण देता है: जो हितकर अन्न बहुत खाते हुए भी बल से लगातार क्षीण होता जाता है। "
                   "जो थोड़ा खाता है (अल्पाशी) पर जिसके मल-मूत्र बहुत हों (बहुविण्मूत्रः)। "
                   "और जो बहुत खाता है (बह्वाशी) पर जिसके मूत्र-मल थोड़े हों (अल्पमूत्रविट्): दोनों उलटे जोड़े इसी कार्ड में हैं। "
                   "‘भी’ का भाव कृदन्त ‘अश्नन्’ (खाता हुआ) से आता है; संस्कृत में अलग शब्द नहीं। "
                   "‘बह्वाशी’ में बहु + आशी की सन्धि है: उ के बाद भिन्न स्वर आने पर उ → व्।"),
    "hook": "कम खाए, बहुत निकले; बहुत खाए, कम निकले।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "In card 12, what does हीयते mean?",
            ("Declines", "हीयते = declines, wastes: हीयते बलतः, declines in strength."),
            [("Grows", "Grows would be वर्धते; हीयते is declines."),
             ("Recovers", "Recovery would be the noun आरोग्य; हीयते is declines."),
             ("Is born", "Is born would be जायते; हीयते is declines.")],
            "हीयते बलतः = declines in strength.",
            "हीयते = declines."),
        order(1, "Put these parts of card 12 in the printed order.",
              ["हीयते बलतः", "शश्वत्", "अन्नमश्नन् हितं बहु", "योऽल्पाशी बहुविण्मूत्रो", "बह्वाशी चाल्पमूत्रविट्"],
              "Declines in strength; continually; eating much wholesome food; who eats little, much faeces and urine; eats much, little urine and faeces.",
              "हीयते बलतः → शश्वत् → अन्नमश्नन् हितं बहु → योऽल्पाशी बहुविण्मूत्रो → बह्वाशी चाल्पमूत्रविट्."),
        match(2, "Match each word of card 12 to its meaning.",
              [["अल्पाशी", "eating little"], ["बह्वाशी", "eating much"], ["विट्", "faeces"], ["मूत्र", "urine"],
               ["बल", "strength"]],
              "अल्पाशी = eating little, बह्वाशी = eating much, विट् = faeces, मूत्र = urine, बल = strength.",
              "अल्पाशी, बह्वाशी, विट्, मूत्र, बल.", role="extend",
              teaches="बहु-विट्-मूत्रः is a bahuvrīhi: 'one who has much faeces and urine'."),
        mcq("discriminate", 3, "By card 12, what goes with eating little (अल्पाशी)?",
            ("Much faeces and urine", "योऽल्पाशी बहुविण्मूत्रः: eats little, has much faeces and urine."),
            [("Little faeces and urine", "That goes with eating much: बह्वाशी अल्पमूत्रविट्."),
             ("Great hunger and thirst", "Hunger and thirst are not named in this card."),
             ("A steady gain in strength", "Strength is named only as declining, with much food.")],
            "Little in, much out; much in, little out: the two reversed pairs.",
            "अल्पाशी → बहुविण्मूत्रः."),
        mcq("apply", 4, "A man eats much wholesome food yet keeps losing strength. Which words of card 12 name this?",
            ("हीयते बलतः शश्वत्", "हीयते बलतः शश्वत् ... अन्नम् अश्नन् हितं बहु: declines in strength while eating much."),
            [("बह्वाशी चाल्पमूत्रविट्", "This is eating much with little urine and faeces, not loss of strength."),
             ("योऽल्पाशी बहुविण्मूत्रो", "This is eating little with much faeces and urine."),
             ("सव्यमक्षि निमज्जति", "This is the sinking left eye of card 10.")],
            "Much wholesome food, yet strength declines: हीयते बलतः शश्वत्.",
            "हीयते बलतः = declines in strength."),
        mcq("transfer", 5, "By the pattern of बहु + आशी → बह्वाशी, how is मधु + आसवः (honey liquor) joined in a new example?",
            ("मध्वासवः", "उ before an unlike vowel → व्: मधु + आसवः → मध्वासवः."),
            [("मधूसवः", "ऊ comes from उ + उ or ऊ; आ is an unlike vowel."),
             ("मधोसवः", "ओ comes from अ/आ + उ, not from उ + आ."),
             ("मध्वसवः", "The आ stays long: व् + आ gives वा, not व.")],
            "मधु + आसवः = मध्वासवः, like बहु + आशी = बह्वाशी.",
            "उ + आ → वा.",
            teaches="उ or ऊ before an unlike vowel becomes व्: बहु + आशी → बह्वाशी."),
    ],
}


# ================================================================ NOTES_HI
NOTES_HI = {
    "1": ("गद्य; विश्वास उच्च; एक छपी पंक्ति (०२.१०.१); कोई पाठ-चिह्न नहीं। अध्याय-आरम्भ का मानक सूत्र, समापन-वाक्य इसमें नहीं। "
          "डेटा नाम को विकृत-ईहा-विज्ञानीय पढ़ता है; समास के अन्य पाठ भी सम्भव हैं। सन्धि जाँची: अथ + अतः → अथातः (अ + अ → आ); "
          "अतः + वि- → अतो (अः + घोष व्यंजन → ओ); विकृत + ईहा → विकृतेहा (अ + ई → ए); व्यंजन से पहले अन्तिम म् → ं (विकृतेहाविज्ञानीयं, शारीरं)।"),
    "2": ("गद्य; विश्वास मध्यम; दो छपी पंक्तियाँ (०२.१०.२ और ०२.१०.३) जोड़ी गईं। अपूर्ण वाक्य: क्रिया ‘पश्यति’ कार्ड ४ में; डेटा के अनुसार "
          "कार्ड २ से ४ सम्भवतः एक वाक्य हैं। पाठ-चिह्न (सम्भव): ‘घनीभूतमिवआकाशम्’ में इव + आकाशम् बिना सन्धि (इवाकाशम् अपेक्षित), सम्भवतः "
          "छपाई की आदत; ‘वाऽमूर्तवस्थितं’ में अ + अ से दीर्घ आ अपेक्षित (अमूर्तावस्थित), अर्थ अप्रभावित। अमूर्त/मूर्त में कौन किस जैसा "
          "दिखता है, दोनों तरह पढ़ा जा सकता है; ‘अमूर्तावस्थितम्’ को ‘अमूर्ते अवस्थितम्’ भी पढ़ा जा सकता है: इन पर प्रश्न नहीं।"),
    "3": ("विश्वास मध्यम; दो छपी पंक्तियाँ (०२.१०.४ और ०२.१०.५) जोड़ी गईं; कोई पाठ-चिह्न नहीं। जोड़े बिना क्रिया और बिना ‘इव’ छपे हैं; "
          "‘मानो’ कार्ड २ के इव से लिया गया अर्थ है। ‘तद्वत्’ सम्भवतः उलटे जोड़े को भी कहता है, पर स्पष्ट नहीं। ‘बहुरूपमलांछनं’ = बहुरूपम् "
          "अलाञ्छनम् (बहुरूप-मल-अञ्छन नहीं)। सन्धि जाँची: तेजस्वि + अतेजः → तेजस्व्यतेजः (इ + भिन्न स्वर → य्); अतेजः + तद्वत् → अतेजस्तद्वत् "
          "(त से पहले विसर्ग → स्); तद्वत् + च → तद्वच्च (च से पहले त् → च्); अनेत्ररोगः + च → अनेत्ररोगश्च (च से पहले विसर्ग → श्)।"),
    "4": ("विश्वास मध्यम; दो छपी पंक्तियाँ (०२.१०.६ और ०२.१०.७) जोड़ी गईं। पाठ-चिह्न (सम्भव): ‘व्याकृति’ असामान्य शब्द है, ‘विकृति’ "
          "अधिक प्रचलित; द्वितीया ‘व्याकृतिम्’ अपेक्षित, अनुस्वार छूटा हो सकता है; पाठ बदला नहीं गया, इस पर प्रश्न नहीं। ‘रूपं व्याकृति’ "
          "एक पद-समूह या दो संज्ञाएँ, दोनों सम्भव। सन्धि जाँची: जाग्रत् + र- → जाग्रद्र- (घोष व्यंजन से पहले त् → द्); अन्यान् + च → "
          "अन्यांश्च (च से पहले न् → ंश्); सः + नश्यति → स नश्यति (व्यंजन से पहले सः का विसर्ग लुप्त)।"),
    "5": ("विश्वास मध्यम; दो छपी पंक्तियाँ (०२.१०.८ और ०२.१०.९) जोड़ी गईं, एक वाक्य; कोई पाठ-चिह्न नहीं। पहचानें डेटा से, उसी के लेबल "
          "के साथ: महर्षि = सप्तर्षि-मण्डल के तारे (सम्भावित), अरुन्धती = अलकोर (सम्भावित), ध्रुव = ध्रुवतारा (सम्भावित), आकाशगंगा = "
          "आकाशगंगा (मानक)। ‘तां समां’ को विशेषण (‘वह समान’) पढ़ना डेटा को स्वीकार नहीं। सन्धि जाँची: महा + ऋषि → महर्षि (आ + ऋ → अर्); "
          "पश्यति + अरुन्धतीम् → पश्यत्यरुन्धतीम् (इ + भिन्न स्वर → य्)।"),
    "6": ("विश्वास मध्यम; दो छपी पंक्तियाँ (०२.१०.१० और ०२.१०.११) जोड़ी गईं। पाठ-चिह्न (सम्भावित): समास-पद ‘वीण’ स्त्रीलिंग मूल ‘वीणा’ "
          "होना चाहिए; ‘वीण’ के बाद छपाई में अतिरिक्त खाली स्थान। पाठ-चिह्न (सम्भव): ‘शब्दानसंतो’ में ‘असन्तः’ (प्रथमा) ‘शब्दान्’ से मेल "
          "नहीं खाता; ‘असतः’ (द्वितीया) अपेक्षित, अनुस्वार फालतू लगता है। पणव = छोटा ढोल (सम्भावित)। ‘मेघ-तोय-ओघ’ को ‘बादल-जल-बाढ़’ भी "
          "पढ़ा जा सकता है। सन्धि जाँची: सतः + अपि → सतोऽपि (अः + अ → ओऽ); शृणोति + अन्यान् → शृणोत्यन्यान् (इ + भिन्न स्वर → य्)।"),
    "7": ("विश्वास मध्यम; दो छपी पंक्तियाँ (०२.१०.१२ और ०२.१०.१३) जोड़ी गईं। पाठ-चिह्न (सम्भावित, लगभग निश्चित): छपा ‘वंध’ कोई शब्द "
          "नहीं; ‘गन्ध’ रस-स्पर्श और कार्ड ८ के ‘दीपगन्धम्’ से मेल खाता है (स्कैन में ग/व की भूल); फिर भी छपे पाठ से भिन्न, इसलिए इस पर "
          "प्रश्न नहीं। धुकधुका = अनुकरण-शब्द, स्रोत अज्ञात (अपहचाना)। सन्धि जाँची: शृणुयात् + न → शृणुयान्न (अनुनासिक से पहले त् → न्, "
          "वैकल्पिक; द् भी सही); तद्वत् + गन्ध- → तद्वद्गन्ध- (घोष व्यंजन से पहले त् → द्); -स्पर्शान् + मन्यते → -स्पर्शान्मन्यते।"),
    "8": ("गद्य; विश्वास कम; दो छपी पंक्तियाँ (०२.१०.१४ और ०२.१०.१५) जोड़ी गईं। पहली पंक्ति: ‘सर्वशो वा न यो’ की क्रिया कार्ड ७ के ‘मन्यते’ "
          "से सम्भवतः आती है; ‘नजिघ्रति’ = न जिघ्रति, बिना खाली स्थान के छपा। दूसरी पंक्ति टूटी हुई: छपा ‘स्वास्थ्येाधाया-’ (े + ा = ो) "
          "निश्चित रूप से पुनर्स्थापित नहीं होता; ‘स्वास्थ्याय अविधिना’ केवल अनुमान है, अनुवाद में भी अपनाया नहीं गया; दूसरी पंक्ति पर कोई "
          "प्रश्न नहीं। सन्धि जाँची: सर्वशः + वा → सर्वशो वा (अः + घोष व्यंजन → ओ); यः + च → यश्च (च से पहले विसर्ग → श्)।"),
    "9": ("विश्वास मध्यम; दो छपी पंक्तियाँ (०२.१०.१६ और ०२.१०.१७) जोड़ी गईं। पाठ-चिह्न (सम्भव): छपा ‘पं शुनेव’ कोई पद-समूह नहीं; "
          "पांशुना + इव = पांशुनेव (‘मानो धूल से’) सुझाव अनुवाद में अपनाया गया, इसलिए वह अंश अनुमानित पाठ पर है; ‘शुना इव’ (कुत्ते जैसे) "
          "व्याकरण से सम्भव पर निरर्थक। ‘वाविधिपूर्वकं’ = वा + विधिपूर्वकम् या वा + अविधिपूर्वकम्; डेटा पहला मानता है, क्योंकि यह छपाई "
          "वा + अ- पर अन्यत्र अवग्रह लिखती है (कार्ड २ ‘वाऽमूर्त’, कार्ड १३ ‘वाऽल्पाशी’)। सन्धि जाँची: यः + अङ्गे → योऽङ्गे (अः + अ → ओऽ); "
          "तपः + तीव्रम् → तपस्तीव्रम् (त से पहले विसर्ग → स्)।"),
    "10": ("विश्वास मध्यम; दो छपी पंक्तियाँ (०२.१०.१८ और ०२.१०.१९) जोड़ी गईं; कोई पाठ-चिह्न नहीं। पहली पंक्ति कार्ड ९ से चल रहे वाक्य "
           "का मुख्य वाक्य प्रतीत होती है; ‘आदिशेत्’ का कर्ता नहीं छपा (वैद्य समझा जाता है); ‘तेषाम्’ बहुवचन, ‘यः’ एकवचन के सामने। "
           "‘जिव्हा’ = ‘जिह्वा’ का मान्य रूपान्तर; ‘जिव्हाश्यावा’ दो शब्द साथ छपे, समास नहीं (स्त्रीलिंग श्यावा)। दूसरी पंक्ति कार्ड ११ में "
           "आगे चलती है। सन्धि जाँची: जानाति + अतीन्द्रियम् → जानात्यतीन्द्रियम् (इ + भिन्न स्वर → य्); यः + च → यश्च।"),
    "11": ("विश्वास उच्च; दो छपी पंक्तियाँ (०२.१०.२० और ०२.१०.२१) जोड़ी गईं; कोई पाठ-चिह्न नहीं। पहली पंक्ति कार्ड १० के सापेक्ष वाक्य को "
           "पूरा करती है; ‘परिवर्जयेत्’ का कर्ता नहीं छपा। ‘लीयन्ते’ = बैठ जाते, चिपकते; ‘छिपना, घुलना’ अर्थ यहाँ नहीं। ‘च्युतांस’ = ढले "
           "कन्धों वाला। सन्धि जाँची: खगाः + वा → खगा वा (आः + घोष ध्वनि → आ, विसर्ग लुप्त); निकषन् + इव → निकषन्निव (ह्रस्व स्वर के बाद "
           "अन्तिम न् स्वर से पहले दोहरा)।"),
    "12": ("विश्वास उच्च; दो छपी पंक्तियाँ (०२.१०.२२ और ०२.१०.२३) जोड़ी गईं; कोई पाठ-चिह्न नहीं। ‘अश्नन्’ कृदन्त है; ‘भी/यद्यपि’ का भाव "
           "उसी से आता है, अलग शब्द छपा नहीं। ‘अल्पमूत्रविट्’ बहुव्रीहि: थोड़े मूत्र-मल वाला। सन्धि जाँची: शश्वत् + यः → शश्वद्यः (घोष "
           "व्यंजन से पहले त् → द्); यः + अन्नम् → योऽन्नम् (अः + अ → ओऽ); बहु + आशी → बह्वाशी (उ + भिन्न स्वर → व्); -विट् + मूत्रः → "
           "-विण्मूत्रः (अनुनासिक से पहले ट् → ण्, वैकल्पिक; ड् भी सही); च + अल्प → चाल्प (अ + अ → आ)।"),
}

# ================================================================ AIDS
AIDS = {
    "1": {
        "chunks": "अथातो | विकृतेहाविज्ञानीयं | शारीरं | व्याख्यास्यामः",
        "frame": "कब: अथ अतः (अब, इसलिए) → क्या: विकृतेहाविज्ञानीयं शारीरं → कौन: हम → क्या करेंगे: व्याख्यास्यामः।",
        "sandhi": ("अ + अ → आ: अथ + अतः → अथातः · अः + घोष व्यंजन → ओ: अतः + वि- → अतो वि- · अ + ई → ए: विकृत + ईहा → "
                   "विकृतेहा।"),
    },
    "2": {
        "chunks": "घनीभूतमिवआकाशमाकाशमिव | यो घनं || अमूर्तमिव | मूर्तं च | मूर्तं वाऽमूर्तवस्थितं",
        "contrast": ("आकाश → मानो ठोस (घनीभूतमिव आकाशम्) ⇄ ठोस → मानो आकाश (आकाशमिव यो घनम्): दोनों इसी कार्ड में। "
                     "अमूर्त/मूर्त का जोड़ा भी यहीं है, पर उसकी दिशा स्पष्ट नहीं।"),
        "anchors": "पक्का: आकाश ठोस दिखे, ठोस आकाश दिखे। अस्पष्ट: अमूर्त-मूर्त की दिशा, ‘अमूर्तवस्थितं’ का पाठ। (मेरी याद-पद्धति)",
    },
    "3": {
        "chunks": "तेजस्व्यतेजस्तद्वच्च | शुक्लं कृष्णमसच्च सत् || अनेत्ररोगश्चंद्रंच | बहुरूपमलांछनं",
        "seesaw": "तेजस्वि ⇄ अतेजः · शुक्लम् ⇄ कृष्णम् · असत् ⇄ सत्: तीनों उलटे जोड़े इसी कार्ड में छपे हैं।",
        "sandhi": ("इ + भिन्न स्वर → य्: तेजस्वि + अतेजः → तेजस्व्यतेजः · त से पहले विसर्ग → स्: अतेजः + तद्वत् → अतेजस्तद्वत् · "
                   "च से पहले त् → च्: तद्वत् + च → तद्वच्च।"),
    },
    "4": {
        "chunks": "जाग्रद्रक्षांसि | गंधर्वान्प्रेतानन्यांश्च तद्विधान् || रूपं व्याकृति तद्वच्च | यः पश्यति स नश्यति",
        "diagram": {"groups": [
            {"label": "कार्ड २", "items": ["आकाश और घन", "अमूर्त और मूर्त"]},
            {"label": "कार्ड ३", "items": ["तेजस्वि/अतेजः", "शुक्ल/कृष्ण", "असत्/सत्", "बहुरूप, चिह्नरहित चन्द्र"]},
            {"label": "कार्ड ४", "items": ["जागते हुए: राक्षस, गन्धर्व, प्रेत", "यः पश्यति स नश्यति"]}]},
        "sandhi": ("घोष व्यंजन से पहले त् → द्: जाग्रत् + रक्षांसि → जाग्रद्रक्षांसि · च से पहले न् → ंश्: अन्यान् + च → अन्यांश्च · "
                   "व्यंजन से पहले सः → स: सः + नश्यति → स नश्यति।"),
    },
    "5": {
        "chunks": "महर्षीणां समीपस्थांयो | न पश्यत्यरुंधतीं || ध्रुवमाकाशगंगां वा | न स पश्यति तां समां",
        "diagram": {"groups": [
            {"label": "जो नहीं देखता", "items": ["अरुन्धती: सम्भवतः अलकोर", "ध्रुव: सम्भवतः ध्रुवतारा",
                                                "आकाशगंगा: मानक, आकाशगंगा"]},
            {"label": "पाठ का कथन", "items": ["न स पश्यति तां समाम्: वह उस वर्ष को नहीं देखता"]}]},
        "sandhi": "आ + ऋ → अर्: महा + ऋषीणाम् → महर्षीणाम् · इ + भिन्न स्वर → य्: पश्यति + अरुन्धतीम् → पश्यत्यरुन्धतीम्।",
    },
    "6": {
        "chunks": "मेघतोयौघनिर्घोषवीण | पणववेणुजान् || शृणोत्यन्यांश्च यः | शब्दानसंतो | न सतोऽपि वा",
        "chain": {"steps": ["१ मेघ-तोय-ओघ का निर्घोष: बादल, जल-प्रवाह की गर्जना", "२ वीण (छपा; सम्भावित पाठ वीणा)",
                            "३ पणव: सम्भवतः छोटा ढोल", "४ वेणु: बाँसुरी", "और दूसरे अविद्यमान शब्द सुनता है",
                            "या विद्यमान शब्द भी नहीं सुनता"]},
        "contrast": "असत् शब्द सुनना ⇄ सत् शब्द भी न सुनना: दोनों इसी कार्ड में; सुनने का विपर्यय दोनों ओर।",
    },
    "7": {
        "chunks": "निष्पीड्य कर्णौ | शृणुयान्न यो | धुकधुकास्वनं || तद्वद्वंधरसस्पर्शान् | मन्यते यो विपर्ययात्",
        "frame": "क्या करके: निष्पीड्य कर्णौ (दोनों कान दबाकर) → क्या नहीं: शृणुयात् न (न सुने) → कौन-सी ध्वनि: धुकधुकास्वनम्।",
        "anchors": "पक्का: कान दबाना, ध्वनि न सुनना, रस-स्पर्श विपर्यय से। सुधार: छपा ‘वंध’ → गन्ध (लगभग निश्चित)। (मेरी याद-पद्धति)",
    },
    "8": {
        "chunks": "सर्वशो वा न यो | यश्च दीपगंधं नजिघ्रति || विधिना यस्य दोषाय | स्वास्थ्येाधायाविधिना रसाः",
        "anchors": "पक्का: पहली पंक्ति, दीपक की गन्ध न सूँघना। अस्पष्ट: दूसरी पंक्ति का टूटा शब्द। (मेरी याद-पद्धति)",
        "sandhi": "अः + घोष व्यंजन → ओ: सर्वशः + वा → सर्वशो वा · च से पहले विसर्ग → श्: यः + च → यश्च।",
    },
    "9": {
        "chunks": "यः पं शुनेव कीर्णांगो | योऽंगे घातं न वेत्ति वा || अंतरेण तपस्तीव्रं | योगं वाविधिपूर्वकं",
        "anchors": "पक्का: अंग पर चोट का पता न चलना; तीव्र तप के बिना। अनुमान: ‘पं शुनेव’ → पांशुनेव; दो पाठ: वा + (अ)विधिपूर्वकम्। (मेरी याद-पद्धति)",
        "sandhi": "अः + अ → ओऽ: यः + अङ्गे → योऽङ्गे · त से पहले विसर्ग → स्: तपः + तीव्रम् → तपस्तीव्रम्।",
    },
    "10": {
        "chunks": "जानात्यतींद्रियं यश्च | तेषां मरणमादिशेत् || जिव्हाश्यावा | मुखं पूति | सव्यमक्षि निमज्जति",
        "diagram": {"groups": [
            {"label": "पंक्ति १ (कार्ड ९ से चलता वाक्य)", "items": ["जानात्यतीन्द्रियं यश्च", "तेषां मरणमादिशेत्"]},
            {"label": "पंक्ति २ के लक्षण (छपे क्रम में)", "items": ["१ जिह्वा श्यावा", "२ मुखं पूति", "३ सव्यम् अक्षि निमज्जति"]}]},
        "sandhi": "इ + भिन्न स्वर → य्: जानाति + अतीन्द्रियम् → जानात्यतीन्द्रियम् · च से पहले विसर्ग → श्: यः + च → यश्च।",
    },
    "11": {
        "chunks": "खगा वा मूर्ध्नि लीयंते | यस्य तं परिवर्जयेत् || निकषन्निव यः पादौ | च्युतांसः परिसर्पति",
        "frame": "किसके: यस्य (जिसके) → कहाँ: मूर्ध्नि (सिर पर) → क्या: खगाः लीयन्ते (पक्षी बैठते) → पाठ का कथन: तं परिवर्जयेत्।",
        "sandhi": "आः + घोष ध्वनि → आ: खगाः + वा → खगा वा · ह्रस्व स्वर के बाद न् + स्वर → न्न्: निकषन् + इव → निकषन्निव।",
    },
    "12": {
        "chunks": "हीयते बलतः शश्वद् | योऽन्नमश्नन् हितं बहु || योऽल्पाशी बहुविण्मूत्रो | बह्वाशी चाल्पमूत्रविट्",
        "seesaw": "अल्पाशी → बहुविण्मूत्रः ⇄ बह्वाशी → अल्पमूत्रविट्: दोनों उलटे जोड़े इसी कार्ड में।",
        "sandhi": ("उ + भिन्न स्वर → व्: बहु + आशी → बह्वाशी · अ + अ → आ: च + अल्प → चाल्प · अः + अ → ओऽ: यः + अल्पाशी → "
                   "योऽल्पाशी।"),
    },
}

# ================================================================ IMAGE_SPECS
IMAGE_SPECS = {
    ("3", "seesaw"): {
        "file": "sh10-jode-3.svg",
        "alt": ("Table of card 3: the three printed opposite pairs, bright and lightless, white and black, unreal and "
                "real."),
        "type": "table",
        "title": "कार्ड ३: छपे उलटे जोड़े",
        "heads": ["पहला शब्द", "जोड़ा"],
        "rows": [["तेजस्वि: तेजस्वी", "अतेजः: तेजहीन"], ["शुक्लम्: श्वेत", "कृष्णम्: काला"], ["असत्", "सत्"]],
    },
    ("4", "diagram"): {
        "file": "sh10-drishti-4.svg",
        "alt": ("Flowchart of cards 2 to 4, which the data takes as probably one sentence: sky and solid, formed and "
                "formless (card 2); bright, colours, unreal and real, the moon (card 3); demons, gandharvas, pretas "
                "seen while awake (card 4); then: he who sees perishes."),
        "type": "mermaid",
        "code": ("flowchart TD\n"
                 "  A[\"कार्ड २: आकाश, घन, मूर्त\"] --> B[\"कार्ड ३: तेज, रंग, चन्द्र\"]\n"
                 "  B --> C[\"कार्ड ४: राक्षस, प्रेत आदि\"]\n"
                 "  C --> D[\"यः पश्यति स नश्यति\"]\n"),
    },
    ("5", "diagram"): {
        "file": "sh10-arundhati-5.svg",
        "alt": ("Table of card 5: Arundhatī (probably Alcor), Dhruva (probably the pole star), Ākāśagaṅgā (the "
                "Milky Way, standard): the three not seen."),
        "type": "table",
        "title": "कार्ड ५: जो नहीं दिखते",
        "heads": ["छपा नाम", "पहचान (डेटा)"],
        "rows": [["अरुन्धती", "सम्भवतः अलकोर"], ["ध्रुव", "सम्भवतः ध्रुवतारा"], ["आकाशगंगा", "मानक: आकाशगंगा"]],
    },
    ("6", "chain"): {
        "file": "sh10-shabda-6.svg",
        "alt": ("Table of card 6 in printed order: the roar of cloud and flood-water, the vīṇā (printed vīṇa, "
                "probable reading vīṇā), the paṇava (probably a small drum), the flute."),
        "type": "table",
        "title": "कार्ड ६: शब्दों के स्रोत",
        "heads": ["क्रम", "स्रोत"],
        "rows": [["१", "मेघ-तोय-ओघ का निर्घोष"], ["२", "वीण (सम्भावित: वीणा)"], ["३", "पणव: सम्भवतः ढोल"],
                 ["४", "वेणु: बाँसुरी"]],
    },
    ("10", "diagram"): {
        "file": "sh10-lakshana-10.svg",
        "alt": ("Table of card 10 in printed order: the tongue dusky, the mouth putrid, the left eye sinks in."),
        "type": "table",
        "title": "कार्ड १०: तीन लक्षण",
        "heads": ["अंग", "लक्षण"],
        "rows": [["१ जिह्वा", "श्यावा: गहरी साँवली"], ["२ मुख", "पूति: दुर्गन्ध वाला"], ["३ बायीं आँख", "निमज्जति: धँसती है"]],
    },
    ("12", "seesaw"): {
        "file": "sh10-ahara-mala-12.svg",
        "alt": ("Split of card 12: eating little with much faeces and urine; eating much with little urine and "
                "faeces."),
        "type": "split",
        "title": "कार्ड १२: खाना और मल-मूत्र",
        "cols": [["अल्पाशी: थोड़ा खाए", ["मल-मूत्र बहुत", "बहुविण्मूत्रः"]],
                 ["बह्वाशी: बहुत खाए", ["मूत्र-मल थोड़े", "अल्पमूत्रविट्"]]],
    },
}
