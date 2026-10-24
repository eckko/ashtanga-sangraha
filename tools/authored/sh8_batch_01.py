from helpers import mcq, match, order, fill, multi, accepts


AUTHORED = {}

# ---------------------------------------------------------------- unit 1
AUTHORED["1"] = {
    "title": "अथातः प्रकृतिभेदीयं शारीरं व्याख्यास्यामः",
    "question": "What subject does the opening line of this chapter announce?",
    "rule": ("The chapter opens: 'Now, therefore, we shall explain the Śārīra on the kinds of constitution' "
             "(प्रकृति-भेदीयम्). Prakṛti here is the natural bodily constitution; व्याख्यास्यामः is a future, 'we shall explain'."),
    "limits": ("Prose opening formula. Both accusatives are adjectives; the noun they qualify (chapter, section) is not "
               "printed and is not supplied. The seven kinds themselves come only from unit 2 on."),
    "explain_hi": ("यह अध्याय की आरम्भिक गद्य-पंक्ति है: ‘अब इसलिए हम प्रकृति के भेदों से सम्बन्धित शारीर की व्याख्या करेंगे’। "
                   "यहाँ प्रकृति का अर्थ शरीर की स्वाभाविक बनावट या देह-प्रकृति है, जिसके सात प्रकार इकाई २ से आते हैं। "
                   "‘प्रकृतिभेदीयम्’ और ‘शारीरम्’ दोनों विशेषण हैं; जिस संज्ञा (अध्याय) के वे विशेषण हैं, वह छपी नहीं। "
                   "‘व्याख्यास्यामः’ भविष्यत् काल, उत्तम पुरुष बहुवचन है: हम व्याख्या करेंगे। "
                   "‘अथातः’ में अथ + अतः (अ + अ → आ) है; प के पहले विसर्ग बना रहता है।"),
    "hook": "अथातः प्रकृतिभेदीयम्: अब देह-प्रकृति के भेद।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By its opening line, what will this chapter explain?",
            ("The kinds of bodily constitution", "प्रकृति-भेदीयम्: relating to the kinds (भेद) of constitution (प्रकृति)."),
            [("The marmas of the limbs and trunk", "The opening line names the kinds of prakṛti, not the marmas."),
             ("The growth of the embryo by months", "The opening line names the kinds of prakṛti, not the embryo's months."),
             ("The diseases of the eye and ear", "The opening line names the kinds of prakṛti, not diseases.")],
            "अथातः प्रकृतिभेदीयं शारीरं व्याख्यास्यामः: the kinds of constitution.",
            "प्रकृति-भेद = kinds of constitution."),
        order(1, "Put the words of unit 1 in the printed order.",
              ["अथातः", "प्रकृतिभेदीयं", "शारीरं", "व्याख्यास्यामः"],
              "Now therefore; on the kinds of constitution; the Śārīra; we shall explain.",
              "अथातः → प्रकृतिभेदीयं → शारीरं → व्याख्यास्यामः."),
        match(2, "Match each word of unit 1 to its meaning.",
              [["अथ", "now"], ["अतः", "therefore"], ["प्रकृति", "bodily constitution"], ["भेद", "kind, division"],
               ["व्याख्यास्यामः", "we shall explain"]],
              "अथ = now, अतः = therefore, प्रकृति-भेद = the kinds of constitution, व्याख्यास्यामः = we shall explain.",
              "अथ, अतः, प्रकृति, भेद, व्याख्यास्यामः.", role="extend",
              teaches="प्रकृति in this chapter is the natural bodily constitution; भेद is a kind or division of it."),
        mcq("discriminate", 3, "Which form is व्याख्यास्यामः in unit 1?",
            ("Future, first person plural", "-स्यामः: future, 'we' (first person plural): we shall explain."),
            [("Future, third person plural", "The third person plural future would end in -स्यन्ति (they will explain)."),
             ("Present, first person plural", "The future sign -स्य- is in the word; it is not the present."),
             ("Past, first person plural", "No past augment or past ending: -स्यामः is the future.")],
            "व्याख्यास्यामः = we shall explain (future, 1st person plural).",
            "-स्यामः = future, 1st person plural."),
        mcq("apply", 4, "Why does अतः keep its visarga before प्रकृतिभेदीयं in unit 1?",
            ("Before a voiceless प the visarga stays", "प is voiceless; before क ख प फ the visarga stays as ः."),
            [("Before every consonant the visarga stays", "Not every one: before च it becomes श्, before a voiced consonant after अ it gives ओ."),
             ("प is a voiced sound, so the visarga stays", "प is voiceless; before a voiced consonant अः would become ओ."),
             ("अतः takes no sandhi because it ends a word", "Final visarga does take sandhi inside a sentence; here the rule keeps it.")],
            "अतः + प्रकृति: before the voiceless प the visarga stays.",
            "Visarga before क ख प फ stays ः."),
        mcq("transfer", 5, "By the pattern of व्याख्यास्यामः, which form of √लिख् means we shall write, in a new example?",
            ("लेखिष्यामः", "-(इ)ष्यामः is the future, first person plural: we shall write."),
            [("लिखामः", "लिखामः is the present: we write."),
             ("लेखिष्यन्ति", "लेखिष्यन्ति is future, but third person: they will write."),
             ("अलिखाम", "अलिखाम is the past (imperfect): we wrote.")],
            "लेखिष्यामः = we shall write, like व्याख्यास्यामः = we shall explain.",
            "Future, 1st person plural: -स्यामः / -इष्यामः.",
            teaches="The future, first person plural, ends in -स्यामः (with इ: -इष्यामः): व्याख्यास्यामः, लेखिष्यामः."),
    ],
}

# ---------------------------------------------------------------- unit 2
AUTHORED["2"] = {
    "title": "सप्त प्रकृतयो दोषैः",
    "question": "By unit 2, how many constitutions are there, and in what three ways do the doṣas make them?",
    "rule": ("There are seven constitutions (प्रकृतयः), made by the doṣas singly (पृथक्), by combination (संसर्गेण) and "
             "by equality (साम्येन: the three doṣas equal)."),
    "limits": ("Prose. The line gives the number and the three ways only. The split 3 single + 3 of two combined + 1 equal "
               "is drawn from later units (the data's note), not printed here; no question asks the count of each way."),
    "explain_hi": ("प्रकृतियाँ सात हैं: दोषों से अलग-अलग (पृथक्), मेल से (संसर्गेण) और समता से (साम्येन)। "
                   "‘साम्येन’ का अर्थ है तीनों दोषों का बराबर होना; यह बात इकाई २६ भी कहती है। "
                   "डेटा की टिप्पणी के अनुसार, आगे की इकाइयों से: वात, पित्त, कफ अकेले तीन, दो-दो के मेल से तीन और सम एक; पर यह बँटवारा इस पंक्ति में छपा नहीं। "
                   "‘संसर्गेण’ में र के बाद न ण बनता है, ‘साम्येन’ में र या ष नहीं, इसलिए न रहता है। "
                   "‘प्रकृतयो दोषैः’ में अः घोष व्यंजन द से पहले ओ बना है।"),
    "hook": "सात प्रकृतियाँ: अकेले, मेल से, समता से।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 2, how many constitutions (prakṛti) are there?",
            ("Seven", "सप्त प्रकृतयः: seven constitutions."),
            [("Three", "Three is the number of the doṣas, not of the constitutions."),
             ("Five", "सप्त is seven; five would be पञ्च."),
             ("Eight", "सप्त is seven; eight would be अष्ट.")],
            "सप्त प्रकृतयो ... भवंति: seven.",
            "सप्त = seven."),
        order(1, "Put the parts of unit 2 in the printed order.",
              ["सप्त प्रकृतयो", "दोषैः", "पृथक्", "संसर्गेण", "साम्येन च", "भवंति"],
              "Seven constitutions; by the doṣas; singly; by combination; and by equality; there are.",
              "पृथक् → संसर्गेण → साम्येन: singly, combined, equal."),
        match(2, "Match each word of unit 2 to its meaning.",
              [["सप्त", "seven"], ["पृथक्", "singly, separately"], ["संसर्गेण", "by combination"],
               ["साम्येन", "by equality"], ["भवन्ति", "there are, arise"]],
              "Seven constitutions arise by the doṣas singly, by combination and by equality.",
              "सप्त, पृथक्, संसर्गेण, साम्येन, भवन्ति.", role="extend",
              teaches="साम्य (from सम, equal) is equality: here the three doṣas being equal."),
        mcq("discriminate", 3, "Why does unit 2 print संसर्गेण with ण but साम्येन with न?",
            ("A र earlier in the word turns न into ण", "संसर्ग has र; with only ग and vowels between, न → ण. साम्य has no र or ष."),
            [("ण marks a masculine noun, न a neuter", "Gender does not decide it: देवेन is masculine with न."),
             ("ण follows a short vowel, न a long one", "The vowel before both is ए; vowel length does not decide it."),
             ("The two spellings are free variants", "They are not free: the र in संसर्ग makes ण necessary.")],
            "र or ष before न in the same word, with no blocking letter between, gives ण.",
            "र / ष ... न → ण in the same word, if only vowels, ह य व र, gutturals or labials come between."),
        mcq("apply", 4, "Which constitution does साम्येन (by equality) in unit 2 point to?",
            ("The one where the three doṣas are equal", "The data reads साम्येन as the equality of the three doṣas (the sama type)."),
            [("The one where one doṣa alone is prominent", "That is what पृथक् (singly) points to."),
             ("The one where two doṣas are joined", "That is what संसर्गेण (by combination) points to."),
             ("The one where no doṣa is in the body", "Unit 12 says all are present in the body.")],
            "साम्य = equality of the three doṣas.",
            "पृथक् = one; संसर्ग = combined; साम्य = all equal."),
        mcq("transfer", 5, "By the rule of संसर्गेण, what is the instrumental singular (by the body) of शरीर in a new example?",
            ("शरीरेण", "शरीर has र; with only vowels between, the न of -एन becomes ण."),
            [("शरीरेन", "The र in शरीर turns the न of -एन into ण."),
             ("शरीराय", "-आय is the dative: for the body."),
             ("शरीरस्य", "-स्य is the genitive: of the body.")],
            "शरीरेण = by the body, like संसर्गेण = by combination.",
            "र ... न → ण in the same word.",
            teaches="After र or ष in the same word, न becomes ण if only vowels, ह य व र, gutturals or labials come between: संसर्गेण, शरीरेण; but साम्येन."),
    ],
}

# ---------------------------------------------------------------- unit 3
AUTHORED["3"] = {
    "title": "तत्र शुक्रार्तवगर्भाशयकालेषु",
    "question": "By unit 3, where can a doṣa become predominant, and what follows from that predominant doṣa?",
    "rule": ("Whichever doṣa, one or more, becomes predominant in the semen, the menstrual fluid, the womb, the time, and "
             "the mother's food and conduct, by that the constitution arises; like a creature's own poison."),
    "limits": ("Low confidence. The printed तेनामरणाह्विषवल्यामिव is damaged: 'until death' (ā-maraṇāt) is a conjectural "
               "reading, and the attachment of the poison-comparisons is uncertain. No question rests on 'until death' or on "
               "which genitive goes with which simile."),
    "explain_hi": ("शुक्र (वीर्य), आर्तव, गर्भाशय, काल, और माता के आहार और विहार में जो दोष, एक या अनेक, अधिक होता है, उसी से प्रकृति बनती है। "
                   "उपमा विष की है: जैसे विष की बेल में जन्मे कृमि, बिच्छू आदि या सर्प को अपना विष नहीं मारता; डेटा के अनुसार भाव यही है कि प्रकृति व्यक्ति को हानि नहीं पहुँचाती। "
                   "छपा ‘तेनामरणाह्विषवल्यामिव’ बिगड़ा है; ‘आमरणात्’ (मृत्यु तक) अनुमानित पाठ है, और उपमाओं के षष्ठी पद किससे जुड़ें, यह भी अनिश्चित है। "
                   "डेटा का विश्वास निम्न है; प्रश्न केवल पक्के भाग (कारणों की सूची, एक या अनेक दोष, उपमा का भाव) पर हैं। "
                   "‘एकोऽनेको’ में एकः + अनेकः: अः + अ → ओऽ।"),
    "hook": "जो दोष गर्भ के समय अधिक, वही प्रकृति: अपना विष अपने को नहीं मारता।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 3, from which doṣa does the constitution arise?",
            ("The doṣa that is predominant", "यो दोषो भवत्याधिक्येन तेन ... प्रकृतिर्जायते: by the one in excess."),
            [("The doṣa that is the weakest one", "Unit 3 says the predominant (आधिक्येन) doṣa, not the weakest."),
             ("The doṣa of the father alone", "Unit 3 lists semen, menstrual fluid, womb, time and the mother's food and conduct."),
             ("The doṣa of the child's first food", "Unit 3 names the factors at conception and pregnancy, not the child's food.")],
            "By whichever doṣa is predominant.",
            "आधिक्येन = by predominance."),
        order(1, "Put the places of predominance in unit 3 in the printed order.",
              ["शुक्र", "आर्तव", "गर्भाशय", "काल", "मातुः आहार", "विहार"],
              "Semen, menstrual fluid, womb, time; and the mother's food and conduct.",
              "शुक्र → आर्तव → गर्भाशय → काल → मातुः आहार → विहार."),
        match(2, "Match each word of unit 3 to its meaning.",
              [["शुक्र", "semen"], ["आर्तव", "menstrual fluid"], ["गर्भाशय", "womb"], ["आहार", "food"],
               ["विहार", "conduct, regimen"]],
              "śukra = semen, ārtava = menstrual fluid, garbhāśaya = womb (all standard); āhāra = food, vihāra = conduct.",
              "शुक्र, आर्तव, गर्भाशय, आहार, विहार.", role="extend",
              teaches="शुक्रार्तवगर्भाशयकालेषु is a dvandva in the locative plural: in the semen, the menstrual fluid, the womb and the time."),
        mcq("discriminate", 3, "By the data's note, what do the poison comparisons of unit 3 illustrate?",
            ("A creature's own poison does not harm it", "The data: as a creature's own poison does not harm it, the constitution does not harm the person."),
            [("Every constitution is a kind of poison", "The comparison is about not being harmed, not about prakṛti being poison."),
             ("A poisoned mother bears a poisonous child", "Unit 3 does not speak of a poisoned mother."),
             ("Snakes have the strongest constitution", "Unit 3 compares; it does not rank creatures.")],
            "Own poison does not harm its bearer; so the constitution does not harm the person.",
            "स्वविषेण: by its own poison (which does not harm it)."),
        mcq("apply", 4, "By unit 3, how many doṣas may be predominant when the constitution is formed?",
            ("One, or more than one", "एकोऽनेको वा: one or more than one."),
            [("Always exactly one doṣa", "एकोऽनेको वा: more than one may be predominant."),
             ("Always all three doṣas together", "एकोऽनेको वा: one may be predominant alone."),
             ("None; the doṣas have no part in it", "Unit 3 says the constitution arises by the predominant doṣa.")],
            "एकः अनेकः वा: one or more.",
            "एकोऽनेको वा = one or more."),
        mcq("transfer", 5, "By the join in एकोऽनेको (एकः + अनेकः), how are रामः + अपि joined in a new example?",
            ("रामोऽपि", "अः + अ → ओ, and the अ that follows is dropped (written ऽ)."),
            [("रामा अपि", "आ with a dropped visarga comes from आः, not from अः."),
             ("रामरपि", "र् stands for a visarga after vowels other than अ / आ."),
             ("रामेऽपि", "ए would come from ए + अ, not from अः + अ.")],
            "रामः + अपि = रामोऽपि, like एकः + अनेकः = एकोऽनेकः.",
            "अः + अ → ओऽ.",
            teaches="A final अः before अ becomes ओ, and the following अ is dropped, marked ऽ: एकः + अनेकः → एकोऽनेकः."),
    ],
}

# ---------------------------------------------------------------- unit 4
AUTHORED["4"] = {
    "title": "तस्मान्तन्मयतया",
    "question": "By unit 4, for what three reasons is a person not harmed by the doṣa of his constitution?",
    "rule": ("Therefore, because of being made of that (doṣa) (तन्मयता), because the body is soaked by semen and menstrual "
             "fluid (भावितत्व), and because of being natural (प्राकृतत्व), he is not harmed to that extent by that doṣa."),
    "limits": ("Prose. 'He' (the person or the body) is understood, not printed. The genitive in शुक्रार्तवयोर्देहस्य can be "
               "taken two ways with the same sense. The print तस्मान्तन्मयतया is not the expected join of तस्मात् + तन्मयतया "
               "(तस्मात्तन्मयतया); no question rests on that join."),
    "explain_hi": ("इसलिए, उसी दोष से बने होने के कारण, शरीर के शुक्र और आर्तव से भावित यानी भीगे होने के कारण, और प्राकृत होने के कारण, व्यक्ति उस दोष से उतना आहत नहीं होता। "
                   "यह इकाई ३ की बात का कारण देती है: अपनी प्रकृति का दोष अपने को नहीं मारता। "
                   "‘तन्मयता’ यानी उसी से बना होना; ‘-त्व’ और ‘-ता’ भाववाचक संज्ञाएँ बनाते हैं। "
                   "‘भावितत्वात्’ और ‘प्राकृतत्वात्’ पञ्चमी हैं, कारण बताती हैं। "
                   "छपा ‘तस्मान्तन्मयतया’ अपेक्षित जोड़ ‘तस्मात्तन्मयतया’ से भिन्न है; उस पर कोई प्रश्न नहीं।"),
    "hook": "उसी से बना, उसी में भीगा, स्वाभाविक: इसलिए आहत नहीं।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 4, how does the doṣa of his own constitution act on a person?",
            ("It does not harm him to that extent", "तावता तेन दोषेण न विहन्यते: he is not harmed to that extent."),
            [("It harms him at once and badly", "न विहन्यते: he is not harmed."),
             ("It harms him more than other doṣas", "Unit 4 says that doṣa does not harm him to that extent."),
             ("It leaves his body after birth", "Unit 4 says nothing of the doṣa leaving the body.")],
            "न विहन्यते: not harmed.",
            "तेन दोषेण न विहन्यते."),
        order(1, "Put the parts of unit 4 in the printed order.",
              ["तस्मान्तन्मयतया", "शुक्रार्तवयोर्देहस्य", "भावितत्वात्प्राकृतत्वाच्च", "तावता तेन दोषेण", "न विहन्यते"],
              "Therefore, by being made of that; of semen and menstrual fluid, of the body; by being soaked and being natural; to that extent, by that doṣa; is not harmed.",
              "Three reasons → न विहन्यते."),
        match(2, "Match each word of unit 4 to its meaning.",
              [["तन्मयता", "being made of that"], ["भावितत्व", "being soaked"], ["प्राकृतत्व", "being natural"],
               ["विहन्यते", "is harmed"]],
              "तन्मयता, भावितत्व, प्राकृतत्व are the three reasons; न विहन्यते = is not harmed.",
              "-ता / -त्व = being X.", role="extend",
              teaches="-त्व and -ता make abstract nouns, 'the state of being X': प्राकृत (natural) → प्राकृतत्व (being natural)."),
        mcq("discriminate", 3, "What does the ending -आत् in भावितत्वात् express in unit 4?",
            ("The reason: because of being soaked", "-आत् is the ablative singular; here it gives the cause."),
            [("The place: in the state of being soaked", "The place would be the locative, -ए (भावितत्वे)."),
             ("The owner: of the state of being soaked", "'Of' would be the genitive, -स्य (भावितत्वस्य)."),
             ("The aim: for the sake of being soaked", "The aim would be the dative, -आय (भावितत्वाय).")],
            "भावितत्वात् = because of being soaked (ablative of cause).",
            "-आत् (ablative) = because of."),
        multi("apply", 4, "Which of these are reasons unit 4 gives for not being harmed?",
              [("The doṣa leaves the body at birth", "Unit 4 says nothing of the doṣa leaving."),
               ("He is made of that doṣa", "Right: तन्मयतया."),
               ("The body is soaked by semen and menstrual fluid", "Right: शुक्रार्तवयोः ... भावितत्वात्."),
               ("It is natural to him", "Right: प्राकृतत्वात्.")],
              [1, 2, 3],
              "तन्मयता, भावितत्व, प्राकृतत्व: the three reasons.",
              "Three ablative reasons → न विहन्यते."),
        mcq("transfer", 5, "By the join in प्राकृतत्वाच्च (प्राकृतत्वात् + च), how are तस्मात् + च joined in a new example?",
            ("तस्माच्च", "त् before च becomes च्: तस्मात् + च → तस्माच्च."),
            [("तस्मात्च", "त् does not stay unchanged before च; it becomes च्."),
             ("तस्माद्च", "द् comes before a voiced sound; च is voiceless."),
             ("तस्मान्च", "न् comes before a nasal, optionally; च is not a nasal.")],
            "तस्मात् + च = तस्माच्च, like प्राकृतत्वात् + च = प्राकृतत्वाच्च.",
            "त् + च → च्च.",
            teaches="A final त् before च or छ becomes च्: प्राकृतत्वात् + च → प्राकृतत्वाच्च."),
    ],
}

# ---------------------------------------------------------------- unit 5
AUTHORED["5"] = {
    "title": "तद्गुणैरेव चास्य शरीरमुपस्क्रियते",
    "question": "By unit 5, by what is the body formed, and what follows for the opposites of those qualities?",
    "rule": ("His body is formed (उपस्क्रियते) by the qualities of that doṣa alone; therefore he is not suddenly (सहसा) "
             "afflicted by the opposites (प्रतिपक्ष) of its qualities."),
    "limits": ("Prose, two printed lines joined. 'That' (तद्) is the doṣa of unit 3; 'he' (the person or body) is understood. "
               "The line says 'not suddenly'; it does not say he is never afflicted."),
    "explain_hi": ("इसका शरीर उसी दोष के गुणों से ही गढ़ा जाता है (उपस्क्रियते)। "
                   "इसलिए उस दोष के गुणों के विरोधी (प्रतिपक्ष) उसे सहसा यानी अचानक पीड़ित नहीं करते। "
                   "‘तद्’ इकाई ३ का वही दोष है जिससे प्रकृति बनी; ‘वह’ (व्यक्ति या शरीर) छपा नहीं, समझा गया। "
                   "पंक्ति ‘अचानक नहीं’ कहती है, ‘कभी नहीं’ नहीं। "
                   "‘तद्गुणैरेव’ में तद्गुणैः + एव: ऐ के बाद विसर्ग स्वर से पहले र् बनता है।"),
    "hook": "उसी के गुणों से बना, इसलिए उलटे गुण अचानक नहीं सताते।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 5, by what is his body formed?",
            ("By the qualities of that doṣa alone", "तद्गुणैरेव ... शरीरमुपस्क्रियते: by its qualities alone."),
            [("By the opposites of that doṣa's qualities", "The opposites are what do not suddenly afflict him."),
             ("By the qualities of all six tastes", "Unit 5 names that doṣa's qualities, not the tastes."),
             ("By the father's food and conduct", "Unit 5 names the doṣa's qualities, not the father's food.")],
            "तद्गुणैः एव: by the qualities of that (doṣa) alone.",
            "तद्गुणैरेव = by its qualities alone."),
        order(1, "Put the parts of unit 5 in the printed order.",
              ["तद्गुणैरेव चास्य", "शरीरमुपस्क्रियते", "ततश्च तद्गुणप्रतिपक्षैः", "सहसा न बाध्यते"],
              "By its qualities alone, and his; body is formed; and therefore by the opposites of its qualities; is not suddenly afflicted.",
              "Formed by its qualities → not suddenly afflicted by their opposites."),
        match(2, "Match each word of unit 5 to its meaning.",
              [["तद्गुण", "qualities of that doṣa"], ["उपस्क्रियते", "is formed"], ["प्रतिपक्ष", "opposite"],
               ["सहसा", "suddenly"], ["बाध्यते", "is afflicted"]],
              "Formed by its qualities; not suddenly afflicted by their opposites.",
              "तद्गुण, उपस्क्रियते, प्रतिपक्ष, सहसा, बाध्यते.", role="extend",
              teaches="प्रतिपक्ष means the opposite side: तद्गुणप्रतिपक्ष = the opposites of that doṣa's qualities."),
        mcq("discriminate", 3, "Which split of तद्गुणैरेव in unit 5 is right?",
            ("तद्गुणैः + एव", "ऐ before visarga, then a vowel: the visarga becomes र्: तद्गुणैरेव."),
            [("तद्गुणैः + रेव", "रेव is not a word; the र् comes from the visarga."),
             ("तद्गुणे + एव", "ए + ए would not give ऐरे; and the form is तद्गुणैः."),
             ("तद्गुण + ऐरेव", "ऐरेव is not a word; एव is the word.")],
            "तद्गुणैः (by its qualities) + एव (alone).",
            "Visarga after a vowel other than अ / आ, before a vowel or voiced consonant → र्."),
        mcq("apply", 4, "By unit 5, what do the opposites of that doṣa's qualities do to him?",
            ("They do not afflict him suddenly", "तद्गुणप्रतिपक्षैः सहसा न बाध्यते."),
            [("They afflict him suddenly and hard", "न बाध्यते: he is not afflicted suddenly."),
             ("They build up his body", "His body is built by the doṣa's own qualities."),
             ("They can never affect him at all", "Unit 5 says not suddenly; it does not say never.")],
            "सहसा न बाध्यते: not suddenly afflicted.",
            "सहसा न = not suddenly."),
        mcq("transfer", 5, "By the join in तद्गुण (तत् + गुण), how are तत् + गृहम् (that house) joined in a new example?",
            ("तद्गृहम्", "त् before a voiced consonant (ग) becomes द्."),
            [("तत्गृहम्", "त् does not stay voiceless before the voiced ग."),
             ("तन्गृहम्", "न् comes only before a nasal; ग is not a nasal."),
             ("तच्गृहम्", "च् comes before च / छ / श, not before ग.")],
            "तत् + गृहम् = तद्गृहम्, like तत् + गुण = तद्गुण.",
            "त् + voiced consonant → द्.",
            teaches="A final त् before a voiced consonant becomes द्: तत् + गुण → तद्गुण."),
    ],
}

# ---------------------------------------------------------------- unit 6
AUTHORED["6"] = {
    "title": "तस्यां त्ववस्थायां",
    "question": "By unit 6, what happens if the doṣa is abnormal and excessive in that state?",
    "rule": ("But in that state, when the doṣa is abnormal (विकृतिमत्) and excessive (उल्बण), the embryo (गर्भ) does not "
             "come into being at all (नैव संभवति)."),
    "limits": ("Prose. 'That state' is not named; by context it probably points back to the formation described in units 3 to 5. "
               "The print joins दोषे उल्बणे as दोषेउल्बणे without sandhi (a print habit). The line names no particular doṣa."),
    "explain_hi": ("किन्तु उस अवस्था में, जब दोष विकृत और उल्बण यानी बढ़ा हुआ हो, गर्भ बनता ही नहीं। "
                   "‘विकृतिमति दोषे उल्बणे’ सति-सप्तमी है: ‘दोष के विकृत और बढ़े होने पर’। "
                   "यह इकाई ३-५ के विपरीत है: वहाँ स्वाभाविक रूप से अधिक दोष प्रकृति बनाता है, यहाँ विकृत और अति बढ़ा दोष गर्भ ही नहीं बनने देता। "
                   "छपा ‘दोषेउल्बणे’ बिना सन्धि जुड़ा है, यह छपाई की आदत है। "
                   "‘नैव’ में न + एव (अ + ए → ऐ), और ‘त्ववस्थायां’ में तु + अवस्थायाम् (उ + अ → व)।"),
    "hook": "दोष विकृत और उल्बण: गर्भ बनता ही नहीं।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 6, what happens when the doṣa is abnormal and excessive in that state?",
            ("No embryo comes into being at all", "नैव गर्भः संभवति: the embryo does not arise at all."),
            [("The embryo takes the sama constitution", "Unit 6 says no embryo arises at all."),
             ("The embryo forms but grows slowly", "Unit 6 says no embryo arises at all."),
             ("The doṣa returns to its natural state", "Unit 6 says nothing of the doṣa returning.")],
            "नैव गर्भः संभवति.",
            "विकृत + उल्बण दोष → नैव गर्भः."),
        order(1, "Put the parts of unit 6 in the printed order.",
              ["तस्यां त्ववस्थायां", "विकृतिमति दोषेउल्बणे", "नैव गर्भः", "संभवति"],
              "But in that state; when the doṣa is abnormal and excessive; not at all the embryo; comes into being.",
              "State → abnormal excessive doṣa → no embryo."),
        match(2, "Match each word of unit 6 to its meaning.",
              [["अवस्था", "state"], ["विकृतिमत्", "having abnormality"], ["उल्बण", "excessive"], ["गर्भ", "embryo"],
               ["संभवति", "comes into being"]],
              "In that state, with the doṣa abnormal and excessive, the embryo does not come into being.",
              "अवस्था, विकृतिमत्, उल्बण, गर्भ, संभवति.", role="extend",
              teaches="-मत् means having: विकृति (abnormality) → विकृतिमत् (having abnormality, abnormal)."),
        mcq("discriminate", 3, "Which split of नैव in unit 6 is right?",
            ("न + एव", "अ + ए → ऐ: न + एव → नैव, not at all."),
            [("न + इव", "अ + इ gives ए: that would be नेव."),
             ("नः + एव", "अः before a vowel other than अ drops the visarga: न एव."),
             ("न + उव", "उव is not a word, and अ + उ gives ओ.")],
            "न (not) + एव (at all).",
            "अ + ए → ऐ."),
        mcq("apply", 4, "In unit 6, what does the phrase विकृतिमति दोषे उल्बणे mean?",
            ("When the doṣa is abnormal and excessive", "Locative absolute: 'the doṣa being abnormal and excessive'."),
            [("When the doṣa is natural and balanced", "विकृतिमत् is abnormal, उल्बण excessive: not natural, not balanced."),
             ("When the doṣa has gone out of the body", "Nothing in the phrase speaks of leaving."),
             ("When the doṣa is weak but abnormal", "उल्बण is excessive, not weak.")],
            "दोषे विकृतिमति उल्बणे: the doṣa being abnormal and excessive.",
            "Locative absolute = when X is Y."),
        mcq("transfer", 5, "By the join in त्ववस्थायां (तु + अवस्थायाम्), how are मधु + अत्र joined in a new example?",
            ("मध्वत्र", "उ before a different vowel becomes व्: मधु + अत्र → मध्वत्र."),
            [("मधोत्र", "उ + अ gives व्, not ओ."),
             ("मधवत्र", "अव् would need ओ, not उ; उ before a different vowel becomes व्."),
             ("मधूत्र", "ऊ comes from उ + उ, not from उ + अ.")],
            "मधु + अत्र = मध्वत्र, like तु + अवस्थायाम् = त्ववस्थायाम्.",
            "उ + unlike vowel → व्.",
            teaches="A final उ / ऊ before a different vowel becomes व्: तु + अवस्थायाम् → त्ववस्थायाम्."),
    ],
}

# ---------------------------------------------------------------- unit 7
AUTHORED["7"] = {
    "title": "संभवएव वा विपद्यते",
    "question": "By unit 7, what other two outcomes can follow when the doṣa is abnormal and excessive?",
    "rule": ("Or it (the embryo) perishes (विपद्यते) even at conception, or it becomes abnormal (विकृतः भवति). "
             "The two outcomes are joined by वा ... वा (or ... or)."),
    "limits": ("Prose. The subject (the embryo) is carried over from unit 6. The printed संभवएव can be read संभवे एव "
               "('at conception itself') or संभव एव with the same sense; no question rests on that split. विकृत may also "
               "mean deformed; the line does not say how."),
    "explain_hi": ("इकाई ६ के आगे: या तो गर्भ बनते ही नष्ट हो जाता है (विपद्यते), या विकृत हो जाता है (विकृतो भवति)। "
                   "कर्ता ‘गर्भ’ इकाई ६ से लिया गया है, यहाँ छपा नहीं। "
                   "छपा ‘संभवएव’ ‘संभवे एव’ या ‘संभव एव’ दोनों पढ़ा जा सकता है; अर्थ एक है, पर इस पर कोई प्रश्न नहीं। "
                   "‘वा ... वा’ दो विकल्प जोड़ता है: या यह, या वह। "
                   "‘विकृतोवा’ में विकृतः + वा: अः घोष व्यंजन व से पहले ओ बनता है।"),
    "hook": "या बनते ही नष्ट, या विकृत।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 7, what can become of the embryo?",
            ("It perishes at conception, or is abnormal", "संभवएव वा विपद्यते विकृतोवा भवति."),
            [("It grows normally, or is born early", "Unit 7 names perishing or becoming abnormal."),
             ("It becomes twins, or is born late", "Unit 7 names perishing or becoming abnormal."),
             ("It takes the mother's constitution", "Unit 7 names perishing or becoming abnormal.")],
            "Perishes, or becomes abnormal.",
            "विपद्यते वा, विकृतो वा भवति."),
        order(1, "Put the words of unit 7 in the printed order.",
              ["संभवएव वा", "विपद्यते", "विकृतोवा", "भवति"],
              "Even at conception, or; it perishes; or abnormal; it becomes.",
              "संभवएव वा → विपद्यते → विकृतोवा → भवति."),
        match(2, "Match each word of unit 7 to its meaning.",
              [["संभव", "conception, coming into being"], ["विपद्यते", "perishes"], ["विकृत", "abnormal"],
               ["वा", "or"]],
              "At conception it perishes, or it becomes abnormal.",
              "संभव, विपद्यते, विकृत, वा.", role="extend",
              teaches="वा after each of two items gives either ... or: X वा ... Y वा."),
        mcq("discriminate", 3, "Why is विकृतः printed विकृतो before वा in unit 7?",
            ("अः before a voiced consonant → ओ", "व is a voiced consonant: विकृतः + वा → विकृतो वा."),
            [("अः before any consonant → ओ", "Not before every consonant: before त it becomes स्, before च श्."),
             ("ओ is a dual ending of विकृत", "विकृतः here is masculine nominative singular (the embryo)."),
             ("The visarga becomes ओ at a pause", "At a pause the visarga stays ः; here वा follows.")],
            "विकृतः + वा: अः before the voiced consonant व → ओ.",
            "अः + voiced consonant → ओ."),
        multi("apply", 4, "Which statements fit unit 7?",
              [("The line says the mother dies", "Unit 7 speaks only of the embryo."),
               ("Even at conception it may perish", "Right: संभवएव वा विपद्यते."),
               ("The line names which doṣa causes the defect", "No doṣa is named in unit 7."),
               ("Two outcomes are joined by वा ... वा", "Right: विपद्यते वा ... विकृतो वा भवति.")],
              [1, 3],
              "It may perish even at conception, or become abnormal; वा ... वा joins the two.",
              "वा ... वा = or ... or."),
        mcq("transfer", 5, "By the वा ... वा of unit 7, what does जलं वा क्षीरं वा पिबेत् mean in a new example?",
            ("He should drink water or milk", "X वा Y वा = either X or Y."),
            [("He should drink water and milk", "And would be च, not वा."),
             ("He should drink no water or milk", "No negative (न) is in the sentence."),
             ("He drank water and then milk", "पिबेत् is optative (should drink), and वा is or.")],
            "जलं वा क्षीरं वा पिबेत् = he should drink either water or milk.",
            "वा ... वा = either ... or.",
            teaches="वा placed after each of two items means either ... or: संभवएव वा विपद्यते, विकृतो वा भवति."),
    ],
}

# ---------------------------------------------------------------- unit 8
AUTHORED["8"] = {
    "title": "तथा च केचिदाहुः",
    "question": "What does unit 8 introduce?",
    "rule": ("'And so some say' (तथा च केचिदाहुः): the line introduces a view held by some; the statement continues in "
             "the units that follow."),
    "limits": ("Prose, one short line. Who 'some' are is not said. The view itself is in the following units; questions stay "
               "on the words of this line."),
    "explain_hi": ("‘और इसी प्रकार कुछ लोग कहते हैं’: यह पंक्ति कुछ लोगों का मत आरम्भ करती है। "
                   "वे कौन हैं, यह नहीं बताया गया। "
                   "मत आगे की इकाइयों में चलता है। "
                   "‘केचित्’ पुल्लिंग बहुवचन सर्वनाम है: कुछ लोग। "
                   "‘केचिदाहुः’ में केचित् + आहुः: स्वर से पहले त् द् बनता है।"),
    "hook": "तथा च केचिदाहुः: अब कुछ लोगों का मत।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "What does unit 8 do?",
            ("It introduces a view held by some", "तथा च केचिदाहुः: and so some say."),
            [("It closes the whole chapter", "The chapter goes on; this line opens a view."),
             ("It names the seven constitutions", "The seven are in unit 2; unit 8 names no constitution."),
             ("It gives the author's own final rule", "केचित् = some (others), not the author's own rule.")],
            "And so some say.",
            "केचित् आहुः = some say."),
        order(1, "Put the words of unit 8 in the printed order.",
              ["तथा", "च", "केचिदाहुः"],
              "So; and; some say.",
              "तथा → च → केचिदाहुः."),
        match(2, "Match each word of unit 8 to its meaning.",
              [["तथा", "so, thus"], ["च", "and"], ["केचित्", "some"], ["आहुः", "they say"]],
              "तथा च केचिदाहुः = and so some say.",
              "तथा, च, केचित्, आहुः.", role="extend",
              teaches="केचित् (some, masculine plural) with आहुः (they say) introduces the view of other authorities."),
        mcq("discriminate", 3, "Which split of केचिदाहुः in unit 8 is right?",
            ("केचित् + आहुः", "त् before a vowel becomes द्: केचित् + आहुः → केचिदाहुः."),
            [("केचिः + आहुः", "इः before a vowel would give र्: केचिराहुः."),
             ("केचि + दाहुः", "Neither केचि nor दाहुः is a word."),
             ("केचित् + दाहुः", "दाहुः is not a word; that join would give केचिद्दाहुः.")],
            "केचित् (some) + आहुः (they say).",
            "त् + vowel → द्."),
        mcq("apply", 4, "In unit 8, which person and number is आहुः?",
            ("Third person plural: they say", "Gram label: 3 pl. perfect of √अह्, used for 'they say'."),
            [("First person plural: we say", "We say would not be आहुः; it agrees with केचित्, a third person."),
             ("Third person singular: he says", "आहुः is plural, agreeing with the plural केचित्."),
             ("Second person plural: you say", "आहुः agrees with केचित् (some), a third person.")],
            "केचित् आहुः: some (they) say.",
            "आहुः = they say (3rd plural)."),
        mcq("transfer", 5, "By the join in केचिदाहुः, how are तत् + अपि joined in a new example?",
            ("तदपि", "त् before a vowel becomes द्: तत् + अपि → तदपि."),
            [("ततपि", "A final त् before a vowel becomes द्, not त."),
             ("तन्नपि", "न् comes before a nasal (optionally); अ is a vowel."),
             ("तच्चपि", "च् comes before च / छ / श, not before a vowel.")],
            "तत् + अपि = तदपि, like केचित् + आहुः = केचिदाहुः.",
            "त् + vowel → द्.",
            teaches="A final त् before a vowel becomes द्: केचित् + आहुः → केचिदाहुः."),
    ],
}

# ---------------------------------------------------------------- unit 9
AUTHORED["9"] = {
    "title": "द्विविधा वातादयः",
    "question": "By unit 9, of what two kinds are Vāta and the other doṣas?",
    "rule": ("Vāta and the others (वातादयः: Vāta, Pitta, Kapha) are of two kinds (द्विविधाः): natural (प्राकृत) and "
             "abnormal (वैकृत)."),
    "limits": ("Prose, no verb (copula understood). The line only names the two kinds; what each kind does comes in units 10 "
               "to 13. It may be part of the view that unit 8 introduces."),
    "explain_hi": ("वात आदि यानी वात, पित्त, कफ दो प्रकार के हैं: प्राकृत (स्वाभाविक) और वैकृत (विकृत)। "
                   "पंक्ति में क्रिया नहीं; ‘हैं’ समझा गया। "
                   "प्राकृत दोष क्या करते हैं, यह इकाई १०-१२ बताती हैं; वैकृत इकाई १३ से। "
                   "‘द्विविधा’ और ‘प्राकृता’ में आः का विसर्ग घोष व्यंजन व से पहले लुप्त हुआ है। "
                   "‘वैकृताश्च’ में वैकृताः + च: च से पहले विसर्ग श् बनता है।"),
    "hook": "दोष दो तरह के: प्राकृत और वैकृत।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 9, what are the two kinds of Vāta and the other doṣas?",
            ("Natural and abnormal", "प्राकृता वैकृताश्च: natural and abnormal."),
            [("Hot and cold", "Unit 9 names prākṛta and vaikṛta, not hot and cold."),
             ("Inner and outer", "Unit 9 names prākṛta and vaikṛta, not inner and outer."),
             ("Moving and fixed", "Unit 9 names prākṛta and vaikṛta, not moving and fixed.")],
            "द्विविधा: प्राकृत और वैकृत.",
            "प्राकृत / वैकृत."),
        order(1, "Put the words of unit 9 in the printed order.",
              ["द्विविधा", "वातादयः", "प्राकृता", "वैकृताश्च"],
              "Of two kinds; Vāta and the others; natural; and abnormal.",
              "द्विविधा → वातादयः → प्राकृता → वैकृताश्च."),
        match(2, "Match each word of unit 9 to its meaning.",
              [["द्विविध", "of two kinds"], ["वातादयः", "Vāta and the others"], ["प्राकृत", "natural"],
               ["वैकृत", "abnormal"]],
              "Vāta and the others are of two kinds: natural and abnormal.",
              "द्विविध, वातादयः, प्राकृत, वैकृत.", role="extend",
              teaches="प्राकृत (from प्रकृति, nature) = natural; वैकृत (from विकृति, abnormality) = abnormal."),
        mcq("discriminate", 3, "Why is प्राकृताः printed प्राकृता before वैकृताश्च in unit 9?",
            ("आः drops the visarga before a voiced sound", "व is voiced: प्राकृताः + वैकृताः → प्राकृता वैकृताः."),
            [("आः drops the visarga before any consonant", "Not before every consonant: before च it gives आश्, before त आस्."),
             ("अः before a voiced sound becomes आ", "The vowel is already long आ; अः before a voiced consonant would give ओ."),
             ("A visarga always drops inside a list", "Lists do not decide it: वैकृताश्च keeps it as श् before च.")],
            "आः + voiced sound → आ (visarga lost).",
            "आः before a voiced sound drops the visarga."),
        mcq("apply", 4, "In वैकृताश्च of unit 9, what does the visarga of वैकृताः become before च?",
            ("श्", "Before च / छ the visarga becomes श्: वैकृताः + च → वैकृताश्च."),
            [("र्", "र् stands for a visarga after vowels other than अ / आ, before a voiced sound."),
             ("ओ", "ओ comes from अः before a voiced consonant; च is voiceless."),
             ("स्", "स् comes before त / थ; before च it is श्.")],
            "वैकृताः + च → वैकृताश्च.",
            "Visarga + च → श्च."),
        mcq("transfer", 5, "Built like वातादयः, what does ज्वरादयः mean in a new example?",
            ("Fever and the others", "X-आदयः = X and the others (X and so on), as वात-आदयः."),
            [("The first of the fevers", "आदि here is 'and so on', not an ordinal 'first'."),
             ("The causes of fever", "Causes would need a word like हेतु; आदयः is 'and the others'."),
             ("After the fever has gone", "आदयः is a nominative plural noun, not 'after'.")],
            "ज्वरादयः = fever and the others, like वातादयः = Vāta and the others.",
            "X-आदयः = X and the others.",
            teaches="A noun joined before आदयः means 'X and the others': वात + आदयः → वातादयः (अ + आ → आ)."),
    ],
}

# ---------------------------------------------------------------- unit 10
AUTHORED["10"] = {
    "title": "तत्र प्राकृताः",
    "question": "By unit 10, what are the natural doṣas the causes of, and when do they arise?",
    "rule": ("Among these, the natural (प्राकृत) doṣas are the causes (हेतुभूताः) of the sevenfold constitution and have "
             "one birth with the body (शरीरैकजन्मानः): they are born together with it."),
    "limits": ("Prose, no verb (copula understood). 'The natural ones' are the natural Vāta, Pitta and Kapha of unit 9. "
               "The line does not say how long they last."),
    "explain_hi": ("उनमें प्राकृत दोष सात प्रकार की प्रकृति के कारण (हेतुभूत) हैं। "
                   "वे शरीर के साथ ही एक साथ जन्मे हैं: ‘शरीरैकजन्मानः’ यानी शरीर के साथ एक ही जन्म वाले। "
                   "‘प्राकृत’ यहाँ इकाई ९ के प्राकृत वात, पित्त, कफ हैं। "
                   "‘शरीरैक’ में शरीर + एक: अ + ए → ऐ। "
                   "‘प्रकृतेर्हेतु’ में प्रकृतेः + हेतु: ए के बाद विसर्ग घोष व्यंजन ह से पहले र् बनता है।"),
    "hook": "प्राकृत दोष: प्रकृति के कारण, शरीर के साथ जन्मे।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 10, the natural doṣas are the causes of what?",
            ("Of the sevenfold constitution", "सप्तविधायाः प्रकृतेर्हेतुभूताः: causes of the sevenfold prakṛti."),
            [("Of every disease of the body", "Unit 10 calls them causes of the constitution, not of disease."),
             ("Of the abnormal doṣas' decay", "Unit 10 calls them causes of the constitution."),
             ("Of the mother's food cravings", "Unit 10 calls them causes of the constitution.")],
            "Causes of the sevenfold constitution.",
            "प्रकृतेर्हेतुभूताः."),
        order(1, "Put the parts of unit 10 in the printed order.",
              ["तत्र प्राकृताः", "सप्तविधायाः", "प्रकृतेर्हेतुभूताः", "शरीरैकजन्मानः"],
              "Among these the natural ones; of the sevenfold; constitution, the causes; having one birth with the body.",
              "प्राकृताः → सप्तविधायाः प्रकृतेः हेतु → शरीरैकजन्मानः."),
        match(2, "Match each word of unit 10 to its meaning.",
              [["सप्तविध", "sevenfold"], ["हेतु", "cause"], ["शरीर", "body"], ["एक", "one, the same"],
               ["जन्मन्", "birth"]],
              "Causes of the sevenfold constitution; one birth with the body.",
              "सप्तविध, हेतु, शरीर, एक, जन्मन्.", role="extend",
              teaches="हेतुभूत = being the cause: -भूत after a noun means 'being, serving as' that."),
        mcq("discriminate", 3, "What does शरीरैकजन्मानः say about the natural doṣas in unit 10?",
            ("They are born together with the body", "शरीर-एक-जन्मानः: having one (the same) birth with the body."),
            [("They are born after the body is formed", "एक-जन्मन् is one, the same birth, not a later one."),
             ("They are born only once in a lifetime", "The compound ties their birth to the body's, not to a count."),
             ("They are born from the mother's body", "The compound says nothing of the mother.")],
            "Same birth as the body: born together with it.",
            "शरीरैकजन्मन् = born together with the body."),
        mcq("apply", 4, "Which split of शरीरैक in unit 10 is right?",
            ("शरीर + एक", "अ + ए → ऐ: शरीर + एक → शरीरैक."),
            [("शरीर + इक", "अ + इ gives ए: that would be शरीरेक."),
             ("शरीरे + एक", "ए before ए would not give ऐ."),
             ("शरीर + उक", "अ + उ gives ओ, and उक is not the word here.")],
            "शरीर (body) + एक (one, same).",
            "अ + ए → ऐ."),
        mcq("transfer", 5, "By the join in प्रकृतेर्हेतु (प्रकृतेः + हेतु), how are बुद्धेः + बलम् joined in a new example?",
            ("बुद्धेर्बलम्", "After ए, a visarga before a voiced consonant (ब) becomes र्."),
            [("बुद्धे बलम्", "The visarga is dropped only after अ / आ; after ए it becomes र्."),
             ("बुद्धेस्बलम्", "स् comes before त / थ, not before ब."),
             ("बुद्धेश्बलम्", "श् comes before च / छ / श, not before ब.")],
            "बुद्धेः + बलम् = बुद्धेर्बलम्, like प्रकृतेः + हेतु = प्रकृतेर्हेतु.",
            "Visarga after ए, before a voiced sound → र्.",
            teaches="A visarga after a vowel other than अ / आ becomes र् before a vowel or voiced consonant: प्रकृतेः + हेतु → प्रकृतेर्हेतु."),
    ],
}

# ---------------------------------------------------------------- unit 11
AUTHORED["11"] = {
    "title": "ते शरीरधारणाद्धातुसंज्ञाः",
    "question": "By unit 11, why are they (by context, the natural doṣas) called dhātu, and which part of the line is unclear?",
    "rule": ("They (by context, the natural doṣas of unit 10) are named dhātu (धातुसंज्ञाः) from supporting the body "
             "(शरीरधारणात्). The rest of the line is damaged and its sense is uncertain."),
    "limits": ("Low confidence. The printed दोषार्व्यानां does not parse and is left unclear; the syntax of the genitives "
               "(विकृतानां बीजभूतानां मुमूर्षोः) is uncertain, so the second half is a loose rendering. Questions rest only "
               "on the first half and on plain joins."),
    "explain_hi": ("वे (प्रसंग से इकाई १० के प्राकृत दोष) शरीर को धारण करने के कारण धातु कहलाते हैं; ‘धातु’ का यह कारण पाठ स्वयं देता है। "
                   "पंक्ति का दूसरा भाग बिगड़ा है: ‘दोषार्व्यानां’ कोई शब्द नहीं बनाता, और विकृतानां, बीजभूतानां, मुमूर्षोः के षष्ठी पद किससे जुड़ें, यह अनिश्चित है। "
                   "डेटा का अनुवाद वहाँ ढीला है और उस पर भरोसा नहीं करना चाहिए; इसलिए उस भाग पर कोई प्रश्न नहीं। "
                   "‘शरीरधारणाद्धातु’ में शरीरधारणात् + धातु: घोष व्यंजन ध से पहले त् द् बनता है। "
                   "डेटा का विश्वास निम्न है।"),
    "hook": "शरीर को धारण करें, इसलिए धातु।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 11, why are they (by context, the natural doṣas) named dhātu?",
            ("From supporting the body", "शरीरधारणात्: from supporting (धारण) the body."),
            [("From flowing through the channels", "Unit 11 gives supporting the body as the reason."),
             ("From being made of digested food", "Unit 11 gives supporting the body as the reason."),
             ("From burning like a fire inside", "Unit 11 gives supporting the body as the reason.")],
            "शरीरधारणाद्धातुसंज्ञाः: named dhātu from supporting the body.",
            "धारण → धातु."),
        order(1, "Put the parts of the sure first half of unit 11 in the printed order.",
              ["ते", "शरीरधारणात्", "धातु", "संज्ञाः"],
              "They; from supporting the body; dhātu; named.",
              "ते → शरीरधारणात् → धातु → संज्ञाः."),
        match(2, "Match each word of the sure first half of unit 11 to its meaning.",
              [["ते", "they"], ["शरीर", "body"], ["धारण", "supporting"], ["संज्ञा", "name"]],
              "ते शरीरधारणाद्धातुसंज्ञाः: they are named dhātu from supporting the body.",
              "ते, शरीर, धारण, संज्ञा.", role="extend",
              teaches="X-संज्ञ (bahuvrīhi) = having the name X: धातुसंज्ञाः = named dhātu."),
        mcq("discriminate", 3, "Which split of शरीरधारणाद्धातु in unit 11 is right?",
            ("शरीरधारणात् + धातु", "त् before the voiced ध becomes द्: -णात् + धातु → -णाद्धातु."),
            [("शरीरधारणा + द्धातु", "द्धातु is not a word; the द् comes from the त् of -णात्."),
             ("शरीरधारणाः + धातु", "आः before a voiced sound would drop the visarga: शरीरधारणा धातु."),
             ("शरीरधारणम् + धातु", "म् before ध would be written ं: शरीरधारणं धातु.")],
            "शरीरधारणात् (from supporting the body) + धातु.",
            "त् + voiced consonant → द्."),
        multi("apply", 4, "Which statements fit the first half of unit 11?",
              [("They are named dhātu from supporting the body", "Right: शरीरधारणाद्धातुसंज्ञाः."),
               ("They are named dhātu from flowing in the body", "Unit 11 gives supporting (धारण), not flowing."),
               ("धारण here means supporting", "Right: शरीरधारणात् = from supporting the body."),
               ("धातुसंज्ञाः is a singular form", "It is masculine nominative plural, agreeing with ते.")],
              [0, 2],
              "Named dhātu from supporting (धारण) the body.",
              "धारण → धातु."),
        mcq("transfer", 5, "By the join in शरीरधारणाद्धातु, how are तत् + धनम् (that wealth) joined in a new example?",
            ("तद्धनम्", "त् before the voiced ध becomes द्: तत् + धनम् → तद्धनम्."),
            [("तत्धनम्", "त् does not stay voiceless before the voiced ध."),
             ("तन्धनम्", "न् comes before a nasal (optionally); ध is not a nasal."),
             ("तच्धनम्", "च् comes before च / छ / श, not before ध.")],
            "तत् + धनम् = तद्धनम्, like शरीरधारणात् + धातु.",
            "त् + voiced consonant → द्.",
            teaches="A final त् before a voiced consonant becomes द्: शरीरधारणात् + धातु → शरीरधारणाद्धातु."),
    ],
}

# ---------------------------------------------------------------- unit 12
AUTHORED["12"] = {
    "title": "सर्वेष्वपि देहे सन्निहितेषु",
    "question": "By unit 12, if all three doṣas are present in the body, how is a constitution named?",
    "rule": ("Even when all (the three doṣas) are present in the body (सन्निहितेषु), the constitution is named "
             "(व्यपदेशः) by the prominent (उल्बण) one."),
    "limits": ("Prose, no verb. 'All' = the three doṣas (the data's note); उल्बणेन stands for an unstated noun ('one'). The "
               "line does not say how prominent a doṣa must be."),
    "explain_hi": ("शरीर में सब यानी तीनों दोष उपस्थित रहते हैं, फिर भी प्रकृति का नाम उल्बण यानी बढ़े हुए दोष से रखा जाता है। "
                   "‘सर्वेषु सन्निहितेषु’ सति-सप्तमी है: सबके उपस्थित होने पर भी। "
                   "जैसे, पित्त उल्बण हो तो प्रकृति पित्त के नाम से कही जाती है, यद्यपि वात और कफ भी हैं। "
                   "‘प्रकृतावुल्बणेन’ में प्रकृतौ + उल्बणेन: औ स्वर से पहले आव् बनता है। "
                   "‘सर्वेष्वपि’ में सर्वेषु + अपि: उ + अ → व।"),
    "hook": "तीनों मौजूद, नाम उल्बण का।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 12, by which doṣa is a constitution named?",
            ("By the prominent one", "प्रकृतौ उल्बणेन व्यपदेशः: named by the prominent one."),
            [("By the one that came first", "Unit 12 names the prominent (उल्बण) one, not the first."),
             ("By the one that is weakest", "Unit 12 names the prominent (उल्बण) one, not the weakest."),
             ("By none, as all three are present", "All are present, yet the prominent one gives the name.")],
            "उल्बणेन व्यपदेशः.",
            "Name = the prominent doṣa."),
        order(1, "Put the words of unit 12 in the printed order.",
              ["सर्वेष्वपि", "देहे", "सन्निहितेषु", "प्रकृतावुल्बणेन", "व्यपदेशः"],
              "Even all; in the body; being present; in the constitution, by the prominent one; the naming.",
              "सर्वेष्वपि → देहे → सन्निहितेषु → प्रकृतावुल्बणेन → व्यपदेशः."),
        match(2, "Match each word of unit 12 to its meaning.",
              [["सर्व", "all"], ["देह", "body"], ["सन्निहित", "present"], ["उल्बण", "prominent"],
               ["व्यपदेश", "naming, designation"]],
              "All present in the body; the naming is by the prominent one.",
              "सर्व, देह, सन्निहित, उल्बण, व्यपदेश.", role="extend",
              teaches="व्यपदेश = designation, the name a thing is called by."),
        mcq("discriminate", 3, "Which split of प्रकृतावुल्बणेन in unit 12 is right?",
            ("प्रकृतौ + उल्बणेन", "औ before a vowel becomes आव्: प्रकृतौ + उल्बणेन → प्रकृतावुल्बणेन."),
            [("प्रकृता + उल्बणेन", "आ + उ gives ओ: that would be प्रकृतोल्बणेन."),
             ("प्रकृतिः + उल्बणेन", "इः before a vowel gives र्: that would be प्रकृतिरुल्बणेन."),
             ("प्रकृते + उल्बणेन", "ए before उ gives अय् or अ, not आव्.")],
            "प्रकृतौ (in the constitution) + उल्बणेन (by the prominent one).",
            "औ + vowel → आव्."),
        mcq("apply", 4, "By unit 12, how is a constitution named if Pitta is prominent while Vāta and Kapha are present too?",
            ("By Pitta", "उल्बणेन व्यपदेशः: the prominent one, Pitta, gives the name."),
            [("By Vāta", "Vāta is present but not prominent here."),
             ("By all three equally", "All are present, yet the name is by the prominent one."),
             ("By Kapha", "Kapha is present but not prominent here.")],
            "The prominent doṣa names the constitution.",
            "उल्बण → व्यपदेश."),
        mcq("transfer", 5, "By the join in प्रकृतावुल्बणेन (प्रकृतौ + उल्बणेन), how are गुरौ + अत्र joined in a new example?",
            ("गुरावत्र", "औ before a vowel becomes आव्: गुरौ + अत्र → गुरावत्र."),
            [("गुरवत्र", "अव् would need ओ, not औ; औ before a vowel becomes आव्."),
             ("गुरोत्र", "No vowel join gives ओ from औ + अ."),
             ("गुरौत्र", "औ does not absorb a following अ; it becomes आव्.")],
            "गुरौ + अत्र = गुरावत्र, like प्रकृतौ + उल्बणेन = प्रकृतावुल्बणेन.",
            "औ + vowel → आव्.",
            teaches="A final औ before a vowel becomes आव्: प्रकृतौ + उल्बणेन → प्रकृतावुल्बणेन."),
    ],
}


# ================================================================= NOTES_HI
NOTES_HI = {
    "1": ("गद्य; विश्वास उच्च; कोई पाठ-चिह्न नहीं। अध्याय की आरम्भिक पंक्ति। दोनों द्वितीया पद विशेषण हैं; संज्ञा (अध्याय) नहीं "
          "जोड़ी गई। यहाँ प्रकृति = स्वाभाविक देह-प्रकृति (मानक)। सन्धि जाँची: अथ + अतः → अथातः (अ + अ → आ); अतः + प्रकृति → "
          "अतः प्रकृति (अघोष प के पहले विसर्ग बना रहता है); प्रकृतिभेदीयम् + शारीरम् → प्रकृतिभेदीयं शारीरम् (व्यंजन से पहले म् → ं)।"),
    "2": ("गद्य; विश्वास उच्च; कोई पाठ-चिह्न नहीं। सात का बँटवारा (३ अकेले, ३ दो-दो के मेल, १ सम) डेटा की टिप्पणी आगे की इकाइयों से "
          "देती है, यहाँ छपा नहीं। ‘साम्येन’ = तीनों दोषों की समता (इकाई २६ में समदोषप्रकृति)। छपा भवंति = भवन्ति (न के लिए "
          "अनुस्वार, लेखन)। सन्धि जाँची: प्रकृतयः + दोषैः → प्रकृतयो दोषैः (अः + घोष व्यंजन → ओ); संसर्गेण में र के बाद न → ण; "
          "साम्येन में र/ष नहीं, न बना रहता है।"),
    "3": ("गद्य; विश्वास निम्न। पाठ-चिह्न (सम्भव): छपा ‘तेनामरणाह्विषवल्यामिव’; ‘आह्वि’ कोई शब्द नहीं, ‘तेनामरणाद् विषवल्याम् इव’ "
          "अनुमानित पाठ। ‘आमरणात्’ (मृत्यु तक) का ‘तेन’ से जुड़ना भी एक पठन है, पक्का नहीं; उपमाओं के षष्ठी पद (कृमेः, सविषकृमेः, "
          "वृश्चिकादेः, आशीविषस्य) किससे जुड़ें, अनिश्चित। इन पर कोई प्रश्न नहीं। शुक्र = वीर्य, आर्तव = मासिक स्राव, गर्भाशय = "
          "गर्भाशय (सभी मानक)। सन्धि जाँची: एकः + अनेकः → एकोऽनेकः (अः + अ → ओऽ); मातुः + च → मातुश्च (च से पहले विसर्ग → श्); "
          "दोषः + भवति → दोषो भवति (अः + घोष व्यंजन → ओ); प्रकृतिः + जायते → प्रकृतिर्जायते (इ के बाद विसर्ग + घोष → र्)।"),
    "4": ("गद्य; विश्वास मध्यम; डेटा में कोई पाठ-चिह्न नहीं। ध्यान दें: छपा ‘तस्मान्तन्मयतया’ अपेक्षित ‘तस्मात्तन्मयतया’ (त् + त → त्त) "
          "से भिन्न है; शब्द-विभाग तस्मात् ही मानता है, पर डेटा इसे चिह्नित नहीं करता; इस जोड़ पर कोई प्रश्न नहीं। "
          "‘शुक्रार्तवयोर्देहस्य भावितत्वात्’ की षष्ठी दो तरह पढ़ी जा सकती है, अर्थ एक। कर्ता (व्यक्ति/शरीर) समझा गया। "
          "सन्धि जाँची: तत् + मय → तन्मय (अनुनासिक म से पहले त् → न्, वैकल्पिक; द् भी सही); शुक्रार्तवयोः + देहस्य → "
          "शुक्रार्तवयोर्देहस्य (ओ के बाद विसर्ग + घोष → र्); भावितत्वात् + प्राकृतत्वात् → भावितत्वात्प्राकृतत्वात् (प से पहले त् अपरिवर्तित); "
          "प्राकृतत्वात् + च → प्राकृतत्वाच्च (च से पहले त् → च्)।"),
    "5": ("गद्य; विश्वास मध्यम; कोई पाठ-चिह्न नहीं। दो छपी पंक्तियाँ ([02.08.5], [02.08.6]) एक इकाई में। ‘तद्’ = इकाई ३ का दोष; "
          "कर्ता ‘वह’ समझा गया। उपस्क्रियते = उप-√कृ, बीच में स् (सुट्), कर्मवाच्य। सन्धि जाँची: तद्गुणैः + एव → तद्गुणैरेव (ऐ के बाद "
          "विसर्ग + स्वर → र्); च + अस्य → चास्य (अ + अ → आ); शरीरम् + उपस्क्रियते → शरीरमुपस्क्रियते; ततः + च → ततश्च (च से पहले "
          "विसर्ग → श्); तत् + गुण → तद्गुण (घोष व्यंजन से पहले त् → द्)।"),
    "6": ("गद्य; विश्वास मध्यम; कोई पाठ-चिह्न नहीं। सति-सप्तमी (विकृतिमति दोषे उल्बणे)। छपा ‘दोषेउल्बणे’ बिना सन्धि जुड़ा, "
          "छपाई की आदत (मानक सन्धि में दोष उल्बणे होता)। सन्धि जाँची: तस्याम् + तु → तस्यां तु (व्यंजन से पहले म् → ं); तु + "
          "अवस्थायाम् → त्ववस्थायाम् (उ + अ → व); न + एव → नैव (अ + ए → ऐ); छपा संभवति = सम्भवति।"),
    "7": ("गद्य; विश्वास मध्यम; कोई पाठ-चिह्न नहीं। छपा ‘संभवएव’: ‘संभवे एव’ (ए स्वर से पहले अ लिखा, विराम रखा) या ‘संभव एव’ "
          "(संभव ही), दोनों सम्भव, अर्थ एक; इस पर कोई प्रश्न नहीं। कर्ता ‘गर्भ’ इकाई ६ से। विपद्यते = वि-√पद्, दिवादि आत्मनेपद, "
          "कर्मवाच्य नहीं। सन्धि जाँची: विकृतः + वा → विकृतो वा (अः + घोष व्यंजन → ओ; छपाई में जुड़ा ‘विकृतोवा’)।"),
    "8": ("गद्य; विश्वास उच्च; कोई पाठ-चिह्न नहीं। मत आगे की इकाइयों में चलता है; ‘केचित्’ कौन हैं, नहीं बताया। आहुः = √अह्, "
          "लिट् प्रथम पुरुष बहुवचन, वर्तमान अर्थ में। सन्धि जाँची: केचित् + आहुः → केचिदाहुः (स्वर से पहले त् → द्)।"),
    "9": ("गद्य; विश्वास उच्च; कोई पाठ-चिह्न नहीं। वातादयः = वात, पित्त, कफ। क्रिया समझी गई। सन्धि जाँची: द्विविधाः + वातादयः → "
          "द्विविधा वातादयः और प्राकृताः + वैकृताः → प्राकृता वैकृताः (आः + घोष ध्वनि → विसर्ग लोप); वात + आदयः → वातादयः (अ + आ → आ); "
          "वैकृताः + च → वैकृताश्च (च से पहले विसर्ग → श्)।"),
    "10": ("गद्य; विश्वास मध्यम; कोई पाठ-चिह्न नहीं। प्राकृताः = इकाई ९ के प्राकृत वात, पित्त, कफ। क्रिया समझी गई। सन्धि जाँची: "
           "प्रकृतेः + हेतु → प्रकृतेर्हेतु (ए के बाद विसर्ग + घोष → र्); शरीर + एक → शरीरैक (अ + ए → ऐ); सप्तविधायाः + प्रकृतेः → "
           "सप्तविधायाः प्रकृतेः (अघोष प के पहले विसर्ग बना रहता है)।"),
    "11": ("गद्य; विश्वास निम्न। पाठ-चिह्न (सम्भव): छपा ‘दोषार्व्यानां’ कोई शब्द नहीं बनाता; ‘दोषाणाम्’ सुझाव है, पक्का नहीं; अविभक्त "
           "और अस्पष्ट छोड़ा गया। विकृतानां, बीजभूतानां, मुमूर्षोः का वाक्य-सम्बन्ध अनिश्चित; दूसरे भाग का अनुवाद ढीला है। उस भाग पर "
           "कोई प्रश्न नहीं। ‘धातु’ नाम का कारण (शरीर-धारण) पाठ स्वयं देता है। सन्धि जाँची: शरीरधारणात् + धातु → शरीरधारणाद्धातु "
           "(घोष व्यंजन से पहले त् → द्); स्वरूपात् + चलन्ति → स्वरूपाच्चलन्ति (च से पहले त् → च्); छपा चलंति = चलन्ति।"),
    "12": ("गद्य; विश्वास मध्यम; कोई पाठ-चिह्न नहीं। ‘सब’ = तीनों दोष (डेटा की टिप्पणी)। सति-सप्तमी (सर्वेषु सन्निहितेषु)। ‘उल्बणेन’ "
           "के साथ संज्ञा छपी नहीं। क्रिया समझी गई। सन्धि जाँची: सर्वेषु + अपि → सर्वेष्वपि (उ + अ → व); प्रकृतौ + उल्बणेन → "
           "प्रकृतावुल्बणेन (औ + स्वर → आव्); सम् + निहित → सन्निहित (न से पहले म् → न्)।"),
}


# ===================================================================== AIDS
AIDS = {
    "1": {
        "chunks": "अथातः | प्रकृतिभेदीयं | शारीरं | व्याख्यास्यामः",
        "frame": "कब: अथ (अब) → क्यों: अतः (इसलिए) → किस विषय पर: प्रकृतिभेदीयं शारीरं → क्या करेंगे: व्याख्यास्यामः (हम व्याख्या करेंगे)।",
        "sandhi": "अ + अ → आ: अथ + अतः → अथातः · अघोष प से पहले विसर्ग बना रहता है: अथातः प्रकृति।",
    },
    "2": {
        "diagram": {"groups": [
            {"label": "सप्त प्रकृतयो दोषैः", "items": ["पृथक्: अकेले", "संसर्गेण: मेल से", "साम्येन च: समता से"]}]},
        "chunks": "सप्त प्रकृतयो | दोषैः | पृथक् | संसर्गेण | साम्येन च | भवंति",
        "sandhi": ("अः + घोष व्यंजन → ओ: प्रकृतयः + दोषैः → प्रकृतयो दोषैः · र के बाद न → ण: संसर्गेण; र/ष नहीं, इसलिए साम्येन।"),
        "anchors": "पृथक् = एक, संसर्ग = दो, साम्य = तीनों बराबर। (मेरी याद-पद्धति; गिनती आगे की इकाइयों से)",
    },
    "3": {
        "chain": {"steps": ["शुक्र", "आर्तव", "गर्भाशय", "काल", "माता का आहार और विहार",
                            "इनमें जो दोष (एक या अनेक) अधिक", "उसी से प्रकृति"]},
        "chunks": ("तत्र | शुक्रार्तवगर्भाशयकालेषु | मातुश्चाहारविहारयोरेकोऽनेको वा | यो दोषो भवत्याधिक्येन | "
                   "तेनामरणाह्विषवल्यामिवोत्पद्यमानस्य | कृमेर्विषेण | सविषकृमेरिव | वृश्चिकादेराशीविषस्येव वा | स्वविषेण | प्रकृतिर्जायते"),
        "sandhi": "अः + अ → ओऽ: एकः + अनेकः → एकोऽनेकः · च से पहले विसर्ग → श्: मातुः + च → मातुश्च।",
        "story": ("विष की बेल में पला कृमि उसी विष से नहीं मरता, न बिच्छू या साँप अपने विष से: वैसे ही अपनी प्रकृति का दोष "
                  "व्यक्ति को नहीं मारता। (डेटा का बताया भाव; उपमाओं का ठीक जुड़ाव अनिश्चित)"),
    },
    "4": {
        "chain": {"steps": ["तन्मयता: उसी दोष से बना", "भावितत्व: शुक्र-आर्तव से भीगा शरीर", "प्राकृतत्व: स्वाभाविक होना",
                            "इसलिए उस दोष से उतना आहत नहीं"]},
        "chunks": "तस्मान्तन्मयतया | शुक्रार्तवयोर्देहस्य | भावितत्वात्प्राकृतत्वाच्च | तावता तेन दोषेण | न विहन्यते",
        "sandhi": "च से पहले त् → च्: प्राकृतत्वात् + च → प्राकृतत्वाच्च · ओ के बाद विसर्ग + घोष → र्: शुक्रार्तवयोः + देहस्य → शुक्रार्तवयोर्देहस्य।",
    },
    "5": {
        "chunks": "तद्गुणैरेव चास्य | शरीरमुपस्क्रियते | ततश्च तद्गुणप्रतिपक्षैः | सहसा न बाध्यते",
        "frame": "किससे बना: तद्गुणैः एव (उसी दोष के गुणों से) → इसलिए: ततः → किससे नहीं: तद्गुणप्रतिपक्षैः (उलटे गुणों से) → कैसे नहीं: सहसा (अचानक)।",
        "sandhi": ("ऐ के बाद विसर्ग + स्वर → र्: तद्गुणैः + एव → तद्गुणैरेव · अ + अ → आ: च + अस्य → चास्य · घोष व्यंजन से पहले "
                   "त् → द्: तत् + गुण → तद्गुण।"),
    },
    "6": {
        "chunks": "तस्यां त्ववस्थायां | विकृतिमति दोषेउल्बणे | नैव गर्भः | संभवति",
        "frame": "कब: तस्यां अवस्थायां (उस अवस्था में) → शर्त: दोष विकृत और उल्बण → फल: नैव गर्भः संभवति (गर्भ बनता ही नहीं)।",
        "sandhi": "उ + अ → व: तु + अवस्थायाम् → त्ववस्थायाम् · अ + ए → ऐ: न + एव → नैव।",
    },
    "7": {
        "chunks": "संभवएव वा | विपद्यते | विकृतोवा | भवति",
        "contrast": "पहला विकल्प: संभव में ही विपद्यते (नष्ट) ⇄ दूसरा विकल्प: विकृतो भवति (विकृत होता है)। दोनों इसी पंक्ति में, वा ... वा से जुड़े।",
        "sandhi": "अः + घोष व्यंजन → ओ: विकृतः + वा → विकृतो वा।",
    },
    "8": {
        "chunks": "तथा च | केचिदाहुः",
        "sandhi": "स्वर से पहले त् → द्: केचित् + आहुः → केचिदाहुः।",
        "frame": "कैसे: तथा च (और इसी प्रकार) → कौन: केचित् (कुछ लोग) → क्या करते हैं: आहुः (कहते हैं) → मत: आगे की इकाइयों में।",
    },
    "9": {
        "seesaw": "प्राकृत (स्वाभाविक) ⇄ वैकृत (विकृत): वात आदि के दो प्रकार, दोनों इसी पंक्ति में।",
        "chunks": "द्विविधा | वातादयः | प्राकृता | वैकृताश्च",
        "sandhi": ("आः + घोष ध्वनि → विसर्ग लोप: प्राकृताः + वैकृताः → प्राकृता वैकृताः · च से पहले विसर्ग → श्: वैकृताः + च → "
                   "वैकृताश्च · अ + आ → आ: वात + आदयः → वातादयः।"),
    },
    "10": {
        "diagram": {"groups": [
            {"label": "तत्र प्राकृताः", "items": ["सप्तविधायाः प्रकृतेर्हेतुभूताः: सात प्रकृतियों के कारण",
                                              "शरीरैकजन्मानः: शरीर के साथ जन्मे"]}]},
        "chunks": "तत्र प्राकृताः | सप्तविधायाः | प्रकृतेर्हेतुभूताः | शरीरैकजन्मानः",
        "sandhi": "ए के बाद विसर्ग + घोष → र्: प्रकृतेः + हेतु → प्रकृतेर्हेतु · अ + ए → ऐ: शरीर + एक → शरीरैक।",
    },
    "11": {
        "chunks": "ते | शरीरधारणाद्धातुसंज्ञाः | दोषार्व्यानां | विकृतानां बीजभूतानां | मुमूर्षोः | स्वरूपाच्चलंति",
        "frame": "कौन: ते (प्रसंग से प्राकृत दोष) → क्यों: शरीरधारणात् (शरीर को धारण करने से) → नाम: धातु। आगे का भाग अस्पष्ट।",
        "sandhi": "घोष व्यंजन से पहले त् → द्: शरीरधारणात् + धातु → शरीरधारणाद्धातु · च से पहले त् → च्: स्वरूपात् + चलन्ति → स्वरूपाच्चलन्ति।",
        "puns": "धारण करे सो धातु: ‘धा’ दोनों में। (केवल सुनने की सहायता, मेरा बनाया)",
    },
    "12": {
        "chain": {"steps": ["सर्वेष्वपि देहे सन्निहितेषु: तीनों दोष उपस्थित", "प्रकृतौ: प्रकृति के विषय में",
                            "उल्बणेन: बढ़े हुए दोष से", "व्यपदेशः: नामकरण"]},
        "chunks": "सर्वेष्वपि | देहे | सन्निहितेषु | प्रकृतावुल्बणेन | व्यपदेशः",
        "sandhi": "उ + अ → व: सर्वेषु + अपि → सर्वेष्वपि · औ + स्वर → आव्: प्रकृतौ + उल्बणेन → प्रकृतावुल्बणेन।",
    },
}


# ============================================================== IMAGE_SPECS
IMAGE_SPECS = {
    ("2", "diagram"): {
        "file": "sh8-sapta-prakriti-2.svg",
        "alt": ("Flowchart of unit 2: the seven constitutions arise from the doṣas in three ways, singly, by combination "
                "and by equality."),
        "type": "mermaid",
        "code": ("flowchart TD\n"
                 "  A[\"दोषैः: दोषों से\"] --> B[\"१ पृथक्: अकेले\"]\n"
                 "  A --> C[\"२ संसर्गेण: मेल से\"]\n"
                 "  A --> D[\"३ साम्येन: समता से\"]\n"
                 "  B --> E[\"सप्त प्रकृतयः\"]\n"
                 "  C --> E\n"
                 "  D --> E\n"),
    },
    ("3", "chain"): {
        "file": "sh8-prakriti-hetu-3.svg",
        "alt": ("Flowchart of unit 3 in line order: semen, menstrual fluid, womb, time, and the mother's food and conduct; "
                "the doṣa, one or more, predominant in these; from it the constitution arises."),
        "type": "mermaid",
        "code": ("flowchart LR\n"
                 "  A[\"१ शुक्र\"] --> G[\"जो दोष अधिक: एक या अनेक\"]\n"
                 "  B[\"२ आर्तव\"] --> G\n"
                 "  C[\"३ गर्भाशय\"] --> G\n"
                 "  D[\"४ काल\"] --> G\n"
                 "  E[\"५ माता का आहार\"] --> G\n"
                 "  F[\"६ माता का विहार\"] --> G\n"
                 "  G --> H[\"उसी से प्रकृति\"]\n"),
    },
    ("4", "chain"): {
        "file": "sh8-na-vihanyate-4.svg",
        "alt": ("Chain of unit 4: made of that doṣa; body soaked by semen and menstrual fluid; being natural; therefore "
                "not harmed to that extent by that doṣa."),
        "type": "chain",
        "title": "इकाई ४: तीन कारण, फिर फल",
        "steps": ["तन्मयता: उसी दोष से बना", "भावितत्व: शुक्र-आर्तव से भीगा", "प्राकृतत्व: स्वाभाविक",
                  "फल: उस दोष से उतना आहत नहीं"],
    },
    ("7", "contrast"): {
        "file": "sh8-vipadyate-vikrita-7.svg",
        "alt": ("Two columns for unit 7, joined by or: the embryo perishes even at conception, or it becomes abnormal."),
        "type": "split",
        "title": "इकाई ७: वा ... वा, दो विकल्प",
        "cols": [["विपद्यते", ["संभव में ही नष्ट"]], ["विकृतो भवति", ["विकृत हो जाता है"]]],
    },
    ("10", "diagram"): {
        "file": "sh8-prakrita-dosha-10.svg",
        "alt": ("Flowchart of unit 10: the natural doṣas are the causes of the sevenfold constitution and are born "
                "together with the body."),
        "type": "mermaid",
        "code": ("flowchart LR\n"
                 "  A[\"प्राकृत दोष\"] --> B[\"सात प्रकृतियों के कारण\"]\n"
                 "  A --> C[\"शरीर के साथ जन्मे\"]\n"),
    },
    ("12", "chain"): {
        "file": "sh8-vyapadesha-12.svg",
        "alt": ("Flowchart of unit 12: all three doṣas present in the body; in the matter of constitution; by the prominent "
                "one; the naming."),
        "type": "mermaid",
        "code": ("flowchart TD\n"
                 "  A[\"१ देह में तीनों दोष उपस्थित\"] --> B[\"२ प्रकृति के विषय में\"]\n"
                 "  B --> C[\"३ उल्बण: बढ़ा हुआ दोष\"]\n"
                 "  C --> D[\"४ उसी से नामकरण\"]\n"),
    },
}
