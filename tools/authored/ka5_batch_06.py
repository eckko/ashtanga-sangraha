from helpers import mcq, match, order, fill, multi, accepts

# Kalpasthana chapter 5 (Siddhabastikalpa), units 74-82 (lines 05.05.142-156), the last batch of the chapter.
# Section (sections_kalpa.py KA5): 74-82 how the potency of the basti spreads; basti the chief procedure.
# 74: from the pakvashaya the basti draws the doshas from foot to head, like the sun the juices of the earth.
# 75-79: the drug's potency passes to samana, then to vyana and the other winds in order; they settle Pitta
#   and phlegm, draw the potency crosswise, down and up through channels; so the basti destroys even yakshmans.
# 80-81: therefore basti is the chief of all procedures (prose); 82: the colophon.

AUTHORED = {}

# ---------------------------------------------------------------- unit 74
AUTHORED["74"] = {
    "title": "यच्च पक्वाशयस्थोऽपि",
    "question": "How does a basti that stays in the pakvāśaya reach the doṣas of the whole body, per verse 74?",
    "rule": ("Though staying in the pakvāśaya (seat of the digested), the basti draws the doṣas from foot to head "
             "by its potency (vīrya), as the sun draws the juices of the earth."),
    "limits": ("Whether यत् is 'that which' or the conjunction 'the fact that' is an open point (05.05.142): no "
               "question on it. The sense of स्वस्थ said of the sun ('healthy' or 'abiding in the sky') is open "
               "(05.05.143): no question on it. The verse names no drug and no dose."),
    "explain_hi": ("यह श्लोक शिष्यों के प्रश्न का एक और उत्तर देता है: बस्ति तो पक्वाशय में रहती है, फिर पूरे शरीर के दोष कैसे हटें? "
                   "उत्तर है: पक्वाशय में स्थित होकर भी बस्ति अपने वीर्य यानी शक्ति से पैर से सिर तक के दोषों को खींच लेती है। "
                   "उपमा सूर्य की है: जैसे सूर्य धरती के रसों को खींच लेता है। "
                   "‘आपादमस्तकम्’ अव्ययीभाव समास है: पैर से लेकर सिर तक। "
                   "पक्वाशय डेटा के अनुसार पचे हुए अन्न का स्थान, यानी निचला पेट या बड़ी आँत है।"),
    "hook": "बस्ति बैठे पक्वाशय में, खींचे पैर से सिर तक, जैसे सूरज धरती का रस।",
    "core": True,
    "questions": [
        mcq("pretest", 0,
            "What does verse 74 compare the basti's drawing of the doṣas to?",
            ("The sun drawing up the juices of the earth",
             "अर्को भूरसानिव: like the sun (draws) the juices of the earth."),
            [("A river carrying all the mud down to the sea",
              "No river is named; the simile is the sun (अर्कः)."),
             ("Fire burning up the dry grass of a whole field",
              "No fire is named in verse 74."),
             ("Wind scattering the clouds across the whole sky",
              "No clouds are named; the verse names the sun and the earth.")],
            "The simile: as the sun draws the juices (रसान्) of the earth (भू), the basti draws the doṣas.",
            "Verse 74: basti draws the doṣas like the sun the earth's juices."),
        match(1, "Match each word of verse 74 to its meaning.",
              [["पक्वाशयस्थः", "staying in the pakvāśaya"], ["आपादमस्तकम्", "from foot to head"],
               ["वीर्येण", "by potency"], ["आदत्ते", "draws, takes in"], ["भूरसान्", "the juices of the earth"]],
              "These words carry the place, the reach, the means and the simile.",
              "पक्वाशयस्थः = staying in the pakvāśaya; आपादमस्तकम् = foot to head; वीर्येण = by potency; आदत्ते = draws; भूरसान् = earth's juices."),
        order(2, "Put these phrases of verse 74 in the order of the verse.",
              ["पक्वाशयस्थोऽपि", "दोषानापादमस्तकम्", "वीर्येण", "बस्तिरादत्ते", "भूरसानिव"],
              "Staying in the pakvāśaya, the doṣas from foot to head, by potency, the basti draws, like the earth's juices.",
              "पक्वाशयस्थोऽपि · दोषानापादमस्तकं · वीर्येण · बस्तिरादत्ते · (अर्को) भूरसानिव.",
              role="extend",
              teaches="Verse 74 runs: though in the pakvāśaya, the doṣas from foot to head, by its potency, the basti draws, like (the sun) the earth's juices."),
        mcq("discriminate", 3, "Which is the right split of बस्तिरादत्ते?",
            ("बस्तिः + आदत्ते",
             "इः before a vowel becomes इर्: बस्तिः + आ- = बस्तिरा-."),
            [("बस्ति + रादत्ते", "रादत्ते is not a word."),
             ("बस्तिम् + आदत्ते", "म् would join the vowel: बस्तिमादत्ते."),
             ("बस्तेः + आदत्ते", "That would print बस्तेरादत्ते, with ए.")],
            "बस्तिः (the basti, subject) + आदत्ते (draws).",
            "Visarga after इ before a vowel or voiced sound → र्."),
        mcq("apply", 4, "By what means does the basti draw the doṣas, according to verse 74?",
            ("By its potency (वीर्य)",
             "वीर्येण = by potency: the instrumental names the means."),
            [("By being held for a long time",
              "No time of holding is stated in verse 74."),
             ("By moving up into the head",
              "The basti stays in the pakvāśaya (-स्थः); it draws from there."),
             ("By the heat of the sun",
              "The sun is only the simile, not the means.")],
            "पक्वाशयस्थोऽपि ... वीर्येण बस्तिरादत्ते: staying below, it draws by potency.",
            "Means = वीर्येण (instrumental)."),
        mcq("transfer", 5,
            "पक्वाशयस्थ means staying in the pakvāśaya. On that model, what does the invented जलस्थः mean?",
            ("Staying in water",
             "-स्थ at the end of a compound means 'staying in, situated in' the first member."),
            [("Giving water", "Giving would be -द (जलद)."),
             ("Born from water", "Born from would be -ज (जलज)."),
             ("Without water", "Without would be निर्- (निर्जल).")],
            "X-स्थ = staying in X: पक्वाशयस्थ, जलस्थ.",
            "-स्थ (from √स्था) = staying in.",
            teaches="-स्थ at the end of a compound means 'staying in': पक्वाशयस्थ (in the pakvāśaya), जलस्थ (in water)."),
    ],
}

# ---------------------------------------------------------------- unit 75
AUTHORED["75"] = {
    "title": "यत्तत्रौषधवीर्यं हि",
    "question": "Which wind soon takes up the drug's potency in verse 75?",
    "rule": ("The potency (vīrya) of the drug that is there is, by a wind, very soon and fully obtained by samāna, "
             "one of the five winds."),
    "limits": ("The print has तद्पानेन, read as तत् + अपानेन (by apāna): a suggested reading (text_flags), so no "
               "question uses apāna. In the data's English samāna obtains the potency; the Hindi has the potency "
               "reaching samāna. Either way the potency ends with samāna; the verse states no route beyond that."),
    "explain_hi": ("पिछले श्लोक में बस्ति के वीर्य की बात थी; अब बताया जाता है कि वह आगे कैसे पहुँचता है। "
                   "वहाँ (पक्वाशय में) जो औषध का वीर्य यानी शक्ति है, उसे वायु के द्वारा बहुत शीघ्र और पूरी तरह समान वायु प्राप्त कर लेता है (‘समानः’ कर्ता है)। "
                   "छपा ‘तद्पानेन’ अनुमानित पाठ पर ‘तत् अपानेन’ (अपान वायु द्वारा) पढ़ा गया है। "
                   "यहाँ ‘वीर्य’ का अर्थ शक्ति है, शुक्र नहीं। "
                   "समान पाँच वायुओं में से एक है; अगले श्लोक में बाकी वायु क्रम से आते हैं।"),
    "hook": "औषध की शक्ति: वायु के सहारे जल्दी ही समान उसे पा ले।",
    "core": False,
    "questions": [
        mcq("pretest", 0,
            "What is spoken of at the start of verse 75 (यत् तत्र ...)?",
            ("The potency of the drug there",
             "यत् तत्र औषधवीर्यम्: the potency (vīrya) of the drug that is there."),
            [("The taste of the food eaten",
              "No food or taste is named in verse 75."),
             ("The heat of the patient's body",
              "No heat is named in verse 75."),
             ("The length of the basti nozzle",
              "No nozzle or measure is named in verse 75.")],
            "औषध = drug; वीर्य = potency: the subject is the drug's potency.",
            "Verse 75 begins with औषधवीर्य, the potency of the drug."),
        match(1, "Match each word of verse 75 to its meaning.",
              [["तत्र", "there"], ["औषध", "drug"], ["वीर्यम्", "potency"],
               ["अचिरात्", "soon"], ["प्रतिपद्यते", "obtains, reaches"]],
              "These are the clear words of verse 75.",
              "तत्र = there; औषध = drug; वीर्यम् = potency; अचिरात् = soon; प्रतिपद्यते = obtains."),
        order(2, "Put these words of verse 75 in the order of the verse.",
              ["औषधवीर्यम्", "वायुना", "पर्याप्तम्", "अचिरादेव", "समानः", "प्रतिपद्यते"],
              "The drug's potency, by the wind, fully, very soon, samāna obtains.",
              "औषधवीर्यं · वायुना · पर्याप्तम् · अचिरादेव · समानः · प्रतिपद्यते.",
              role="extend",
              teaches="Verse 75 runs: the potency of the drug ... by the wind, fully, very soon, samāna obtains (it)."),
        mcq("discriminate", 3, "What does वीर्य mean in औषधवीर्यम् of verse 75?",
            ("The drug's power to act",
             "The card: वीर्य = potency, शक्ति, the power of the drug."),
            [("The seed of the drug plant", "A seed is not meant; the card gives potency."),
             ("Semen of the patient", "Plain वीर्य can mean semen in Hindi, but here it is potency."),
             ("Bravery of the physician", "No physician is named in verse 75.")],
            "Here वीर्य = potency (वीर्य यानी शक्ति), not semen.",
            "औषधवीर्य = the potency of the drug."),
        mcq("apply", 4, "Which wind does verse 75 name as soon obtaining the drug's potency?",
            ("Samāna (समानः)",
             "अचिरादेव समानः प्रतिपद्यते: very soon samāna obtains (it)."),
            [("Prāṇa", "Prāṇa is not named in verse 75; it comes in 05.05.150."),
             ("Udāna", "Udāna is not named in verse 75."),
             ("Vyāna", "Vyāna follows only after samāna, in 05.05.146.")],
            "The potency passes to samāna first; vyāna and the rest follow in the next verse.",
            "Drug potency → samāna (verse 75)."),
        mcq("transfer", 5,
            "By the rule of अचिरात् + एव = अचिरादेव, how do the invented तस्मात् + एव join?",
            ("तस्मादेव", "त् becomes द् before a vowel, and the vowel stays: तस्मादेव."),
            [("तस्मातेव", "Before a vowel the त् turns voiced, द्."),
             ("तस्मान्नेव", "त् becomes न् only before a nasal; ए is not a nasal."),
             ("तस्माद्यैव", "No य् comes in; the vowel ए joins the द्.")],
            "अचिरात् + एव = अचिरादेव; तस्मात् + एव = तस्मादेव.",
            "Final त् → द् before a vowel.",
            teaches="A final त् becomes द् before a vowel: अचिरात् + एव = अचिरादेव; तस्मात् + एव = तस्मादेव."),
    ],
}

# ---------------------------------------------------------------- unit 76
AUTHORED["76"] = {
    "title": "समानादुत्तरं चैवं",
    "question": "Which winds follow samāna in verse 76, and where do they go?",
    "rule": ("Thus, after samāna, the winds beginning with vyāna, in order. They go to their natural state "
             "(prakṛti), standing in the support of the body."),
    "limits": ("Low confidence. तूमाः cannot be restored (perhaps 'hot ones' or 'quickly', neither sure): no "
               "question on it. What the winds receive is not said here; by context it is the drug's potency "
               "of 05.05.144-145. The verse does not list the winds beyond vyāna."),
    "explain_hi": ("औषध का वीर्य समान तक पहुँचा था; अब बताया जाता है कि आगे क्या होता है। "
                   "समान के बाद इसी प्रकार व्यान आदि वायु क्रम से (उसे ग्रहण करते हैं, प्रसंग से)। "
                   "दूसरी पंक्ति का ‘तूमाः’ अस्पष्ट है; इसका अर्थ तय नहीं, इसलिए इसे छोड़कर पढ़ें। "
                   "स्पष्ट बात यह है: वे वायु अपनी प्रकृति यानी स्वाभाविक अवस्था में लौट जाते हैं और शरीर के अनुग्रह यानी सहारे में स्थित रहते हैं। "
                   "क्रिया ‘यान्ति’ दूसरी पंक्ति में है।"),
    "hook": "समान के बाद व्यान आदि, क्रम से; फिर सब वायु अपनी प्रकृति में।",
    "core": False,
    "questions": [
        mcq("pretest", 0,
            "Which wind does verse 76 name first after samāna?",
            ("Vyāna", "व्यानाद्याः पवनाः: the winds beginning with vyāna."),
            [("Prāṇa", "Prāṇa is not named in verse 76."),
             ("Udāna", "Udāna is not named in verse 76."),
             ("No wind at all", "The verse names vyāna and those that follow it.")],
            "समानात् उत्तरम् ... व्यानाद्याः: after samāna, those beginning with vyāna.",
            "After samāna: vyāna and the rest, in order."),
        match(1, "Match each word of verse 76 to its meaning.",
              [["उत्तरम्", "after, next"], ["पवनाः", "winds"], ["क्रमात्", "in order"],
               ["प्रकृतिम्", "natural state"], ["अनुग्रहे", "in the support"]],
              "These are the clear words of verse 76.",
              "उत्तरम् = after; पवनाः = winds; क्रमात् = in order; प्रकृतिम् = natural state; अनुग्रहे = in the support."),
        order(2, "Put these phrases of verse 76 in the order of the verse.",
              ["समानादुत्तरम्", "व्यानाद्याः पवनाः", "क्रमात्", "प्रकृतिं यान्ति", "शरीरानुग्रहे स्थिताः"],
              "After samāna, the winds from vyāna, in order; they go to their natural state, standing in the body's support.",
              "समानादुत्तरं · व्यानाद्याः पवनाः · क्रमात् · (ते ...) प्रकृतिं यान्ति · शरीरानुग्रहे स्थिताः.",
              role="extend",
              teaches="Verse 76: after samāna, the winds beginning with vyāna, in order; they go to their natural state, standing in the support of the body."),
        mcq("discriminate", 3, "Which is the right split of व्यानाद्याः?",
            ("व्यान + आद्याः", "अ + आ merge into आ: व्यान + आद्याः = व्यानाद्याः."),
            [("व्यानात् + आद्याः", "त् would become द् and stay: व्यानादाद्याः."),
             ("व्यानः + आद्याः", "अः before a vowel loses its visarga and stays apart: व्यान आद्याः."),
             ("व्यानम् + आद्याः", "म् would join the vowel: व्यानमाद्याः.")],
            "व्यान + आद्याः (those beginning with) = व्यानाद्याः.",
            "अ + आ → आ."),
        mcq("apply", 4, "According to verse 76, to what do the winds go?",
            ("To their own natural state", "प्रकृतिं यान्ति: they go to their natural state."),
            [("Out of the body through the mouth", "No leaving of the body is stated."),
             ("To a greatly increased state", "Increase is the opposite of returning to prakṛti."),
             ("Down into the pakvāśaya again", "The pakvāśaya is not named in verse 76.")],
            "प्रकृति = the natural state; the winds return to it while supporting the body.",
            "Verse 76: the winds go to their natural state (प्रकृति)."),
        mcq("transfer", 5,
            "व्यानाद्याः means the winds beginning with vyāna. What does the invented प्राणाद्याः mean?",
            ("Those beginning with prāṇa",
             "X-आद्य at the end of a compound = 'beginning with X'."),
            [("Those ending with prāṇa", "Ending with would be -अन्त (प्राणान्ताः)."),
             ("Those coming after prāṇa", "After would be प्राणात् उत्तरम्, as with samāna here."),
             ("Prāṇa alone, no other", "-आद्य includes the others that follow.")],
            "व्यानाद्याः = vyāna and the rest; प्राणाद्याः = prāṇa and the rest.",
            "-आद्य = beginning with, 'and the rest'.",
            teaches="-आद्य at the end of a compound means 'beginning with X, and the rest': व्यानाद्याः, प्राणाद्याः."),
    ],
}

# ---------------------------------------------------------------- unit 77
AUTHORED["77"] = {
    "title": "पित्तश्लेष्माणौ यथास्थानं",
    "question": "What do the winds do with Pitta and phlegm in verse 77?",
    "rule": ("Having overpowered (on the suggested reading प्रसह्य) Pitta and phlegm (śleṣman) and placed each in its own place, the winds "
             "nourish all around, in the body, their own respective qualities of the bhūtas."),
    "limits": ("Printed प्रैसह्य is read as प्रसह्य (text_flags): no question on it. 'Nourish' or 'satiate' for "
               "संतर्पयन्ति is open (05.05.149): no question on it. भूत: 'elements' is probable, not stated. "
               "The subject (the winds) comes from 05.05.146-147."),
    "explain_hi": ("अब वायु, जिन्हें औषध का वीर्य मिला है, पित्त और कफ पर काम करते हैं। "
                   "वे पित्त और श्लेष्म यानी कफ को (अनुमानित पाठ पर) बलपूर्वक दबाकर हर एक को उसके अपने स्थान पर स्थापित करते हैं। "
                   "फिर वे शरीर में चारों ओर अपने अपने भूत-गुणों को तृप्त करते हैं। "
                   "‘पित्तश्लेष्माणौ’ द्विवचन है क्योंकि दो दोष हैं; पर ‘तनौ’ का -औ द्विवचन नहीं, सप्तमी एकवचन है: शरीर में। "
                   "कर्ता वायु पिछले श्लोक से आते हैं।"),
    "hook": "वायु पित्त-कफ को अपनी-अपनी जगह बिठाएँ, फिर अपने भूत-गुण तृप्त करें।",
    "core": False,
    "questions": [
        mcq("pretest", 0,
            "What do the winds do with Pitta and phlegm in verse 77?",
            ("Place each in its own place", "यथास्थानं निवेश्य: having placed (them) each in its place."),
            [("Drive both out through the mouth", "Nothing is driven out in verse 77."),
             ("Mix the two into a single doṣa", "No mixing is stated; each goes to its own place."),
             ("Increase both of them greatly", "They are settled each in its own place (यथास्थानं निवेश्य), not increased.")],
            "पित्तश्लेष्माणौ यथास्थानं निवेश्य: Pitta and phlegm, each set in its own place.",
            "Verse 77: Pitta and phlegm are placed back, each in its own place."),
        match(1, "Match each word of verse 77 to its meaning.",
              [["यथास्थानम्", "each in its place"], ["निवेश्य", "having placed"], ["परितः", "all around"],
               ["स्वान् स्वान्", "each its own"], ["तनौ", "in the body"]],
              "These are the clear words of verse 77.",
              "यथास्थानम् = each in its place; निवेश्य = having placed; परितः = all around; स्वान् स्वान् = each its own; तनौ = in the body."),
        order(2, "Put these words of verse 77 in the order of the verse.",
              ["पित्तश्लेष्माणौ", "यथास्थानम्", "निवेश्य च", "परितः", "भूतगुणान्", "तनौ"],
              "Pitta and phlegm, each in its place, having placed; all around, the qualities of the bhūtas, in the body.",
              "पित्तश्लेष्माणौ · यथास्थानं · निवेश्य च · (संतर्पयन्ति) परितः · (स्वान्स्वान्) भूतगुणान् · तनौ.",
              role="extend",
              teaches="Verse 77: Pitta and phlegm, each in its place, having been placed; then all around, their own bhūta-qualities, in the body."),
        mcq("discriminate", 3,
            "पित्तश्लेष्माणौ and तनौ both end in -औ. What is तनौ in verse 77?",
            ("Locative singular: in the body",
             "तनु is an उ-stem; its locative singular is तनौ, 'in the body'."),
            [("Dual number: two bodies together",
              "The card glosses तनौ as 'in the body', f. loc. sg.; only पित्तश्लेष्माणौ is dual."),
             ("Accusative plural: all the bodies",
              "The accusative plural of तनु would be तनूः."),
             ("Dual number: the Pitta and the phlegm",
              "That is पित्तश्लेष्माणौ, the dvandva of two doṣas.")],
            "-औ is not always dual: पित्तश्लेष्माणौ is dual (two doṣas), तनौ is locative singular.",
            "-औ: dual of most stems, but locative singular of इ/उ stems (तनौ)."),
        mcq("apply", 4, "Who places Pitta and phlegm in their places in verse 77?",
            ("The winds of the verse before",
             "The data: the subject is the winds of 05.05.146-147 (vyāna and the rest)."),
            [("The physician by his hand", "No physician is named in verse 77."),
             ("Pitta itself, by its own heat", "Pitta is the object (accusative), not the doer."),
             ("The patient's food and drink", "No food is named in verse 77.")],
            "पित्तश्लेष्माणौ is accusative; the doers are the winds carried over from verse 76.",
            "Subject of verse 77 = the winds (from verse 76)."),
        mcq("transfer", 5,
            "निवेश्य (having placed) has a prefix (नि-), so it ends in -य. Which form means having understood, from वि-√ज्ञा?",
            ("विज्ञाय", "With a prefix the absolutive takes -य: वि-ज्ञा-य, like नि-वेश्य."),
            [("विज्ञात्वा", "-त्वा is used without a prefix (ज्ञात्वा); with वि- it becomes -य."),
             ("विज्ञातुम्", "This is the infinitive, 'to understand'."),
             ("विज्ञातः", "This is the past participle, 'understood'.")],
            "Prefix + root → -य (निवेश्य, विज्ञाय); bare root → -त्वा (ज्ञात्वा).",
            "Absolutive: -त्वा without a prefix, -य with a prefix.",
            teaches="The absolutive ('having X-ed') ends in -त्वा on a bare root (ज्ञात्वा) and in -य after a prefix (निवेश्य, विज्ञाय)."),
    ],
}

# ---------------------------------------------------------------- unit 78
AUTHORED["78"] = {
    "title": "व्यानस्तिर्यगपानोऽधः",
    "question": "In which direction does each of the three winds draw, according to verse 78?",
    "rule": ("Vyāna draws crosswise, apāna downward and prāṇa upward, each according to its own (way), "
             "as water (is carried) through carrying channels (nāḍī)."),
    "limits": ("What is drawn is not stated; by context it is the drug's potency. प्रकर्षति is singular and "
               "shared by the three winds. The verse does not say which channels are meant; nāḍī is kept as "
               "the term."),
    "explain_hi": ("यह श्लोक तीन वायुओं की दिशाएँ बताता है। "
                   "व्यान तिरछा (‘तिर्यक्’), अपान नीचे (‘अधः’) और प्राण ऊपर (‘ऊर्ध्वम्’) खींचता है, हर एक अपने अपने ढंग से। "
                   "एक ही एकवचन क्रिया ‘प्रकर्षति’ तीनों के साथ अलग-अलग लगती है। "
                   "उपमा जल की है: जैसे बहाने वाली नाड़ियों से जल ले जाया जाता है। "
                   "क्या खींचा जाता है, यह यहाँ नहीं कहा; प्रसंग से औषध का वीर्य।"),
    "hook": "व्यान तिरछा, अपान नीचे, प्राण ऊपर: नालियों में पानी जैसे।",
    "core": True,
    "questions": [
        mcq("pretest", 0,
            "Which way does apāna draw, according to verse 78?",
            ("Downward", "अपानोऽधः: apāna (draws) downward."),
            [("Upward", "Upward (ऊर्ध्वम्) is said of prāṇa."),
             ("Crosswise", "Crosswise (तिर्यक्) is said of vyāna."),
             ("In a circle", "No circular movement is named.")],
            "व्यानः तिर्यक्, अपानः अधः, प्राणः ऊर्ध्वम्.",
            "अपान → अधः (downward)."),
        match(1, "Match each wind of verse 78 to the direction it draws.",
              [["व्यानः", "crosswise"], ["अपानः", "downward"], ["प्राणः", "upward"]],
              "Each wind has its own direction in verse 78.",
              "व्यान → तिर्यक् (crosswise); अपान → अधः (down); प्राण → ऊर्ध्वम् (up)."),
        order(2, "Put these phrases of verse 78 in the order of the verse.",
              ["व्यानस्तिर्यक्", "अपानोऽधः", "प्राणश्चोर्ध्वम्", "प्रकर्षति", "यथास्वमेव", "नाडीभिः"],
              "Vyāna crosswise, apāna down, prāṇa up, draws; each by its own way; through channels.",
              "व्यानस्तिर्यक् · अपानोऽधः · प्राणश्चोर्ध्वं · प्रकर्षति · यथास्वमेव · नाडीभिः.",
              role="extend",
              teaches="Verse 78 names vyāna (crosswise), apāna (down), prāṇa (up), then the verb, then 'each its own way' and the channels."),
        mcq("discriminate", 3, "What is the simile of verse 78?",
            ("Water carried through channels",
             "नाडीभिर्हारिणीभिरिवोदकम्: like water through carrying channels."),
            [("The sun drawing up the earth's juices",
              "That simile is in verse 74, for the basti in the pakvāśaya."),
             ("A fire spreading through dry wood",
              "No fire is named in verse 78."),
             ("A wind driving the clouds about",
              "No clouds are named in verse 78.")],
            "उदकम् ... इव = like water; नाडीभिः हारिणीभिः = through carrying channels.",
            "Verse 78 simile: water in channels (verse 74: sun and earth's juices)."),
        mcq("apply", 4,
            "Three winds are named, yet प्रकर्षति (draws) is singular. How does the card explain it?",
            ("Each wind draws: the verb goes with each",
             "The data: the singular verb is shared, understood with each singular subject."),
            [("Only prāṇa draws; the others are still",
              "Each wind is given its own direction of drawing."),
             ("The three winds form one compound noun",
              "They are three separate nominatives, each with its own direction word."),
             ("प्रकर्षति is really a plural form",
              "The gram label is 3 sg. pres.; the plural would be प्रकर्षन्ति.")],
            "व्यानः ... अपानः ... प्राणः च प्रकर्षति: each one draws, in its own direction.",
            "One singular verb can serve several singular subjects, each taken separately."),
        mcq("transfer", 5,
            "By the rule of व्यानः + तिर्यक् = व्यानस्तिर्यक्, how do the invented रामः + तत्र join?",
            ("रामस्तत्र", "Visarga becomes स् before त: रामस्तत्र."),
            [("रामो तत्र", "-अः → -ओ happens before a voiced sound; त is unvoiced."),
             ("रामर्तत्र", "र् comes from इः/उः before voiced sounds, not from अः before त."),
             ("रामश्तत्र", "श् comes before च/छ; before त it is स्.")],
            "व्यानः + तिर्यक् = व्यानस्तिर्यक्; रामः + तत्र = रामस्तत्र.",
            "Visarga → स् before त/थ.",
            teaches="A visarga becomes स् before त or थ: व्यानः + तिर्यक् = व्यानस्तिर्यक्; रामः + तत्र = रामस्तत्र."),
    ],
}

# ---------------------------------------------------------------- unit 79
AUTHORED["79"] = {
    "title": "वपुर्बस्तिः सुयोजितः",
    "question": "What does the well-applied basti destroy, according to verse 79?",
    "rule": ("Thus, or by those (unclear) and by the sirās (vessels), the well-applied basti, pervading the body, "
             "forcibly destroys even the very difficult yakṣmans (wasting diseases)."),
    "limits": ("Low confidence. वा तैः ('or by those') may be a mis-division of वातैः ('by the winds'), an open point "
               "(05.05.152): no question on it. Yakṣman = wasting disease, consumption; tuberculosis-type is "
               "probable, not certain. No dose or time is given."),
    "explain_hi": ("यह श्लोक बस्ति के वीर्य के प्रसार का फल बताता है। "
                   "भली-भाँति प्रयोग की गई बस्ति सिराओं के द्वारा पूरे शरीर में फैलती हुई बलपूर्वक अत्यन्त कष्टसाध्य यक्ष्मन् यानी क्षय रोगों को भी नष्ट करती है। "
                   "पहली पंक्ति का ‘वा तैः’ (या उनसे) विवादित है: छपाई में यह ‘वातैः’ (वायुओं से) का गलत विभाजन भी हो सकता है। "
                   "‘व्याप्नुवन्’ का कर्म ‘वपुः’ है: शरीर को व्याप्त करती हुई। "
                   "‘सु-’ यहाँ दो बार है: सुयोजित (अच्छी तरह प्रयुक्त) और सुकृच्छ्र (अत्यन्त कठिन)।"),
    "hook": "ठीक से दी बस्ति पूरे शरीर में फैले, कठिन क्षय को भी मारे।",
    "core": False,
    "questions": [
        mcq("pretest", 0,
            "What does the well-applied basti destroy, according to verse 79?",
            ("Even the very difficult yakṣmans",
             "हन्ति सुकृच्छ्रानपि यक्ष्मणः: it destroys even the very difficult yakṣmans (wasting diseases)."),
            [("Only fevers of recent origin", "Fever is not named in verse 79."),
             ("Worms of the large intestine", "Worms are not named in verse 79."),
             ("Swellings of the feet alone", "Swellings are not named in verse 79.")],
            "यक्ष्मन् = wasting disease (tuberculosis-type, probable); सुकृच्छ्र = very difficult.",
            "Verse 79: basti destroys even very difficult yakṣmans."),
        match(1, "Match each word of verse 79 to its meaning.",
              [["सुयोजितः", "well applied"], ["व्याप्नुवन्", "pervading"], ["प्रसभम्", "forcibly"],
               ["हन्ति", "destroys"], ["सुकृच्छ्रान्", "very difficult"]],
              "These words carry the action of the basti in verse 79.",
              "सुयोजितः = well applied; व्याप्नुवन् = pervading; प्रसभम् = forcibly; हन्ति = destroys; सुकृच्छ्रान् = very difficult."),
        order(2, "Put these phrases of verse 79 in the order of the verse.",
              ["सिराभिश्च", "वपुः", "बस्तिः सुयोजितः", "व्याप्नुवन्", "प्रसभं हन्ति", "सुकृच्छ्रानपि यक्ष्मणः"],
              "By the sirās, the body, the well-applied basti, pervading, forcibly destroys even the very difficult yakṣmans.",
              "सिराभिश्च · वपुः · बस्तिः सुयोजितः · व्याप्नुवन् · प्रसभं हन्ति · सुकृच्छ्रानपि यक्ष्मणः.",
              role="extend",
              teaches="Verse 79 runs: by the sirās, the body, the well-applied basti, pervading, forcibly destroys even the very difficult yakṣmans."),
        mcq("discriminate", 3, "Which is the right split of वपुर्बस्तिः?",
            ("वपुः + बस्तिः", "उः before a voiced sound (ब) becomes उर्: वपुर्बस्तिः."),
            [("वपु + र्बस्तिः", "र्बस्तिः is not a word."),
             ("वपुम् + बस्तिः", "म् before ब would give an anusvara: वपुं बस्तिः."),
             ("वपोः + बस्तिः", "That would print वपोर्बस्तिः, with ओ.")],
            "वपुः (the body, object of व्याप्नुवन्) + बस्तिः (the basti, subject).",
            "Visarga after उ before a voiced sound → र्."),
        mcq("apply", 4, "In verse 79, what does the basti pervade (व्याप्नुवन्)?",
            ("The body (वपुः)", "The data: the body is the object of व्याप्नुवन्."),
            [("The sirās (सिरा)", "सिराभिः is instrumental: the sirās are the way, not what is pervaded."),
             ("The yakṣmans (यक्ष्मन्)", "यक्ष्मणः are the object of हन्ति (destroys)."),
             ("The pakvāśaya alone", "The basti pervades the body; the pakvāśaya is not named in verse 79.")],
            "वपुः व्याप्नुवन्: pervading the body; यक्ष्मणः हन्ति: destroys the yakṣmans.",
            "Two objects: वपुः (of व्याप्नुवन्), यक्ष्मणः (of हन्ति)."),
        mcq("transfer", 5,
            "सु- means well or very, as in सुयोजितः (well applied). What does the invented सुपक्वम् mean?",
            ("Well cooked", "सु- (well) + पक्व (cooked) = well cooked."),
            [("Badly cooked", "Badly would be दुष्- (दुष्पक्व)."),
             ("Not cooked", "Not cooked would be अपक्व."),
             ("Cooked again", "Again would be पुनः, not सु-.")],
            "सु-योजित = well applied; सु-कृच्छ्र = very difficult; सु-पक्व = well cooked.",
            "सु- = well, very.",
            teaches="The prefix सु- means 'well, very': सुयोजित (well applied), सुकृच्छ्र (very difficult), सुपक्व (well cooked)."),
    ],
}

# ---------------------------------------------------------------- unit 80
AUTHORED["80"] = {
    "title": "बस्तिस्तस्मात्सर्वकर्मप्रधानं",
    "question": "What rank does unit 80 give the basti among all procedures?",
    "rule": ("Therefore basti is the chief of all procedures (karman), and it destroys the all-ending (ones) "
             "completely."),
    "limits": ("सर्वान्तकान् is rendered literally, 'the all-ending (ones)'; what is meant (deadly diseases?) is not "
               "stated and is not added. प्रधानम् is neuter beside masculine बस्तिः because it is a predicate noun. "
               "No dose or method is given."),
    "explain_hi": ("यह इकाई पूरे तर्क का निष्कर्ष है: ‘तस्मात्’, इसलिए। "
                   "वायु ही सब रोगों का कारण है और बस्ति वायु को जीतती है, इसलिए बस्ति सब कर्मों यानी चिकित्सा-प्रक्रियाओं में प्रधान है। "
                   "वह सब का अन्त करने वालों को पूरी तरह (‘निःशेषतः’) नष्ट करती है। "
                   "‘सर्वान्तक’ से कौन-से रोग अभिप्रेत हैं, यह पाठ नहीं कहता; अनुवाद शब्दशः है। "
                   "‘प्रधानम्’ नपुंसक है, ‘बस्तिः’ पुंलिंग: विधेय संज्ञा कर्ता का लिंग नहीं लेती।"),
    "hook": "इसलिए बस्ति: सब कर्मों में प्रधान, सब-नाशकों का पूरा नाश।",
    "core": True,
    "questions": [
        mcq("pretest", 0,
            "What does unit 80 call the basti?",
            ("The chief of all procedures",
             "सर्वकर्मप्रधानम्: chief (प्रधान) of all procedures (कर्म)."),
            [("A procedure for Kapha alone", "Unit 80 limits basti to no single doṣa."),
             ("A last resort when all else fails", "Unit 80 calls it chief, not a last resort."),
             ("Equal to the other procedures", "प्रधान ranks it above them.")],
            "बस्तिः ... सर्वकर्मप्रधानम्: basti is the chief of all procedures.",
            "Unit 80: basti = सर्वकर्मप्रधान."),
        match(1, "Match each word of unit 80 to its meaning.",
              [["तस्मात्", "therefore"], ["कर्म", "procedure"], ["प्रधानम्", "chief"],
               ["हन्ति", "destroys"], ["निःशेषतः", "completely"]],
              "These words carry the conclusion of unit 80.",
              "तस्मात् = therefore; कर्म = procedure; प्रधानम् = chief; हन्ति = destroys; निःशेषतः = completely."),
        order(2, "Put these words of unit 80 in the order of the text.",
              ["बस्तिः", "तस्मात्", "सर्वकर्मप्रधानम्", "सर्वान्तकान्", "हन्ति", "निःशेषतश्च"],
              "Basti, therefore, chief of all procedures; the all-ending ones it destroys, and completely.",
              "बस्तिः · तस्मात् · सर्वकर्मप्रधानं · सर्वान्तकान् · हन्ति · निःशेषतश्च.",
              role="extend",
              teaches="Unit 80 runs: basti, therefore, (is) chief of all procedures; it destroys the all-ending (ones) completely."),
        mcq("discriminate", 3,
            "Which word is wrong in this rendering of unit 80: Therefore basti is the chief of all procedures, and it destroys the all-ending ones partly?",
            ("partly", "निःशेषतः means completely, 'without remainder', not partly."),
            [("therefore", "तस्मात् = therefore: correct."),
             ("chief", "प्रधानम् = chief: correct."),
             ("procedures", "कर्म = procedures: correct.")],
            "निःशेषतः = completely; the rest of the line is rendered rightly.",
            "निःशेषतः = completely (निः- without + शेष remainder)."),
        mcq("apply", 4,
            "Why can प्रधानम् be neuter though बस्तिः is masculine, per the card?",
            ("It is a predicate noun",
             "The data: a predicate noun keeps its own gender; it need not agree with the subject."),
            [("बस्ति is really a neuter noun", "The gram label of बस्तिः is m. nom. sg."),
             ("It is a printing error to correct", "No text_flag is raised; the data explains the gender."),
             ("It agrees with सर्वान्तकान्", "सर्वान्तकान् is masculine accusative plural.")],
            "बस्तिः (m.) ... प्रधानम् (n.): 'basti is the chief'; the predicate noun keeps its gender.",
            "A predicate noun need not share the subject's gender."),
        mcq("transfer", 5,
            "निःशेषतः is built on निः- (without) + शेष (remainder). What does the invented निःशब्दम् mean?",
            ("Without sound, silently", "निः- = without; शब्द = sound: without sound."),
            [("With much sound", "Much would be बहु-, not निः-."),
             ("By means of sound", "By means of would be the instrumental शब्देन."),
             ("The sound itself", "निः- takes the thing away; it does not name it.")],
            "निः-शेष = without remainder; निः-शब्द = without sound.",
            "निः- (निर्/निस्) = without.",
            teaches="The prefix निः- (निर्-, निस्-) means 'without': निःशेष (without remainder, completely), निःशब्द (without sound)."),
    ],
}

# ---------------------------------------------------------------- unit 81
AUTHORED["81"] = {
    "title": "शोधयित्वा च कुर्यात्",
    "question": "What does the basti do after cleansing, according to unit 81?",
    "rule": ("Having cleansed (within the channel, srotas), it would make brightness (dīpti) of semen (śukra), body and "
             "digestive fire (agni); the doṣas and tejas stand in the same sentence. The closing iti ends the teaching."),
    "limits": ("Low confidence. Whether दोषान् is the object of शोधयित्वा (cleansed the doṣas) and whether तेजः is a "
               "member of the brightness compound is an open point (05.05.155): no question on it. The print has "
               "स्त्रोतसि and दीप्तिमिमिति (text_flags): no question on स्रोतस् or on the -मिमिति ending."),
    "explain_hi": ("यह इकाई बस्ति के फल की बात पूरी करती है और अन्तिम ‘इति’ से गुरु का उत्तर समाप्त होता है। "
                   "बस्ति (स्रोत के भीतर) शुद्ध करके शुक्र, देह और अग्नि यानी जठराग्नि की दीप्ति करती है। "
                   "वाक्य का ढाँचा विवादित है: डेटा में ‘दोषों, तेज और शुक्र-देह-अग्नि की दीप्ति करे’, समीक्षक के अनुसार ‘दोषों को शुद्ध करके तेज, शुक्र, देह और अग्नि की दीप्ति करे’। "
                   "‘शोधयित्वा’ णिजन्त से बना -त्वा वाला रूप है: शुद्ध करके। "
                   "‘कुर्यात्’ विधिलिङ् है: करे, कर सकती है।"),
    "hook": "शुद्ध करके: शुक्र, देह और अग्नि में चमक।",
    "core": False,
    "questions": [
        mcq("pretest", 0,
            "What does शोधयित्वा in unit 81 mean?",
            ("Having cleansed", "शोधयित्वा = having cleansed (absolutive of the causative of √शुध्)."),
            [("Having heated", "Heating would be from √तप्, not √शुध्."),
             ("Having bound", "Binding would be from √बन्ध्."),
             ("Having drunk", "Drinking would be पीत्वा, from √पा.")],
            "शुध् = to be clean; causative शोधय- = to cleanse; -इत्वा = having done.",
            "शोधयित्वा = having cleansed."),
        match(1, "Match each word of unit 81 to its meaning.",
              [["शोधयित्वा", "having cleansed"], ["कुर्यात्", "would make"], ["शुक्र", "semen"],
               ["देह", "body"], ["अग्नि", "digestive fire"]],
              "These are the clear words of unit 81.",
              "शोधयित्वा = having cleansed; कुर्यात् = would make; शुक्र = semen; देह = body; अग्नि = digestive fire."),
        order(2, "Put these words of unit 81 in the order of the text.",
              ["शोधयित्वा", "कुर्यात्", "शुक्र", "देह", "अग्नि"],
              "Having cleansed, it would make (the brightness of) semen, body and digestive fire.",
              "शोधयित्वा · (च) कुर्यात् · (दोषान् तेजः) शुक्र- · देह- · अग्नि-(दीप्तिम्).",
              role="extend",
              teaches="Unit 81 runs: having cleansed, it would make ... the brightness of semen, body and digestive fire."),
        mcq("discriminate", 3, "Which is the right split of कुर्याद्दोषान्?",
            ("कुर्यात् + दोषान्", "त् becomes द् before the voiced द: कुर्याद्दोषान्."),
            [("कुर्याम् + दोषान्", "म् before द would give an anusvara: कुर्यां दोषान्."),
             ("कुर्याः + दोषान्", "आः before a voiced sound loses its visarga: कुर्या दोषान्."),
             ("कुर्या + द्दोषान्", "द्दोषान् is not a word.")],
            "कुर्यात् (would make) + दोषान् (the doṣas).",
            "Final त् → द् before a voiced consonant."),
        multi("apply", 4,
              "Which of these does the brightness compound (-दीप्तिम्) of unit 81 name? Choose all that apply.",
              [("Semen (शुक्र)", "Right: शुक्र is the first clear member."),
               ("The body (देह)", "Right: देह is a member."),
               ("Digestive fire (अग्नि)", "Right: अग्नि is a member."),
               ("Blood (रक्त)", "Wrong: blood is not named in unit 81."),
               ("The eyes (नेत्र)", "Wrong: the eyes are not named in unit 81.")],
              [0, 1, 2],
              "शुक्र-देह-अग्नि-दीप्तिम्: the brightness of semen, body and digestive fire.",
              "The compound names शुक्र, देह and अग्नि."),
        mcq("transfer", 5,
            "कुर्यात् (would make) is the optative of √कृ. Which form means he would go, from √गम् (गच्छति)?",
            ("गच्छेत्", "The optative 3 sg. of an -अ stem ends in -एत्: गच्छ + एत् = गच्छेत्."),
            [("गच्छति", "This is the present, 'he goes'."),
             ("गमिष्यति", "This is the future, 'he will go'."),
             ("गत्वा", "This is the absolutive, 'having gone'.")],
            "कुर्यात् and गच्छेत् are optatives: 'would / should do', 'would / should go'.",
            "Optative 3 sg.: -एत् on -अ stems (गच्छेत्), -यात् on others (कुर्यात्).",
            teaches="The optative ('would, should') 3rd singular ends in -एत् on -अ stems (गच्छेत्) and in -यात् on some others (कुर्यात्)."),
    ],
}

# ---------------------------------------------------------------- unit 82
AUTHORED["82"] = {
    "title": "इति सिद्धबस्तिकल्पो नाम",
    "question": "What is the name and number of the chapter that unit 82 closes?",
    "rule": "Thus the fifth chapter, named Siddhabastikalpa: the preparations of the siddha bastis.",
    "limits": ("A colophon, not a verse: it names the chapter and teaches nothing new. 'Siddha' in the title is kept "
               "as printed; the data glosses it 'accomplished' (the glossary's usual sense of siddha is 'cooked')."),
    "explain_hi": ("यह पञ्चम अध्याय का समापन-वाक्य है: इस प्रकार सिद्धबस्तिकल्प नामक पाँचवाँ अध्याय। "
                   "‘सिद्धबस्तिकल्प’ = सिद्ध बस्तियों के कल्प यानी उन्हें बनाने की विधियाँ। "
                   "इस अध्याय में एरण्डमूल, मुस्तादि यापन, क्षीर-बस्ति और अनुवासन तैल जैसी बस्तियाँ आईं, और अन्त में बताया गया कि बस्ति दोषों को कैसे हरती है। "
                   "‘पञ्चमोऽध्यायः’ = पञ्चमः + अध्यायः।"),
    "hook": "पाँचवाँ अध्याय: सिद्धबस्तिकल्प, सिद्ध बस्तियों की विधियाँ।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "Which number is the chapter that unit 82 closes?",
            ("Fifth", "पञ्चमः = fifth."),
            [("Fourth", "Fourth would be चतुर्थः."),
             ("Sixth", "Sixth would be षष्ठः."),
             ("Fiftieth", "Fiftieth would be पञ्चाशत्तमः; पञ्चम is fifth.")],
            "पञ्चमोऽध्यायः = the fifth chapter.",
            "पञ्चम = fifth."),
        match(1, "Match each word of unit 82 to its meaning.",
              [["इति", "thus"], ["बस्ति", "basti (enema)"], ["कल्प", "preparations"],
               ["नाम", "named"], ["अध्यायः", "chapter"]],
              "इति सिद्धबस्तिकल्पो नाम पञ्चमोऽध्यायः.",
              "इति = thus; बस्ति = basti; कल्प = preparations; नाम = named; अध्यायः = chapter."),
        order(2, "Put the words of unit 82 in the order of the text, after the split.",
              ["इति", "सिद्धबस्तिकल्पः", "नाम", "पञ्चमः", "अध्यायः"],
              "Thus, Siddhabastikalpa, named, fifth, chapter.",
              "इति · सिद्धबस्तिकल्पः · नाम · पञ्चमः · अध्यायः.",
              role="extend",
              teaches="The colophon runs: इति सिद्धबस्तिकल्पो नाम पञ्चमोऽध्यायः, thus the fifth chapter, named Siddhabastikalpa."),
        mcq("discriminate", 3, "Which split is right for पञ्चमोऽध्यायः?",
            ("पञ्चमः + अध्यायः", "-अः before अ gives -ओ, and the lost अ is marked by ऽ."),
            [("पञ्चम + अध्यायः", "अ + अ would merge to आ: पञ्चमाध्यायः."),
             ("पञ्चमो + ध्यायः", "ध्यायः is not the word; the chapter is अध्यायः."),
             ("पञ्चमम् + अध्यायः", "म् would join the vowel: पञ्चममध्यायः.")],
            "पञ्चमः (fifth) + अध्यायः (chapter).",
            "-अः + अ- → -ओऽ."),
        mcq("apply", 4, "Which of these is the subject of the chapter named in unit 82?",
            ("Preparations of bastis", "सिद्धबस्तिकल्प: the kalpa (preparations) of the siddha bastis."),
            [("Complications of a basti", "Complications (व्यापद्) are not in this title."),
             ("Signs of coming death", "The title names bastis, not signs of death."),
             ("Rules for daily routine", "The title names no daily routine.")],
            "बस्ति + कल्प: the title is about preparing bastis.",
            "सिद्धबस्तिकल्प = preparations of siddha bastis."),
        mcq("transfer", 5,
            "पञ्चमोऽध्यायः means the fifth chapter. Which phrase means the sixth chapter?",
            ("षष्ठोऽध्यायः", "षष्ठ = sixth; षष्ठः + अध्यायः = षष्ठोऽध्यायः."),
            [("सप्तमोऽध्यायः", "सप्तम is seventh."),
             ("चतुर्थोऽध्यायः", "चतुर्थ is fourth."),
             ("षडध्यायः", "This compound means 'six chapters', not 'the sixth'.")],
            "Ordinals: चतुर्थ 4th, पञ्चम 5th, षष्ठ 6th, सप्तम 7th.",
            "षष्ठ = sixth; -अः + अ- → -ओऽ.",
            teaches="Ordinals name a chapter's place: पञ्चमोऽध्यायः (fifth chapter), षष्ठोऽध्यायः (sixth chapter)."),
    ],
}


NOTES_HI = {
    "74": ("विश्वास: मध्यम। पंक्तियाँ ०५.०५.१४२-१४३, एक वाक्य; क्रिया ‘आदत्ते’ दूसरी पंक्ति में। "
           "खुला अवलोकन (०५.०५.१४२): ‘यत्’ नपुंसक है और ‘पक्वाशयस्थः’ पुंलिंग, इसलिए ‘यत्’ सम्भवतः संयोजक ‘कि, यह बात कि’ है; इस पर प्रश्न नहीं। "
           "खुला अवलोकन (०५.०५.१४३): सूर्य के लिए ‘स्वस्थ’ (स्वस्थ या आकाश में स्थित) अटपटा; इस पर प्रश्न नहीं। "
           "संधि जाँची: यच्च = यत् + च; पक्वाशयस्थोऽपि = -स्थः + अपि; दोषानापादमस्तकं = दोषान् + आपादमस्तकम्; "
           "बस्तिरादत्ते = बस्तिः + आदत्ते; स्वस्थोऽर्को = स्वस्थः + अर्कः; भूरसानिव = भूरसान् + इव। "
           "पक्वाशय = पचे हुए का स्थान, निचला पेट या बड़ी आँत (डेटा के अनुसार मानक)।"),
    "75": ("विश्वास: मध्यम। पंक्तियाँ ०५.०५.१४४-१४५, एक वाक्य। "
           "text_flag: छपा ‘तद्पानेन’, सुझाया पाठ ‘तदपानेन’ = तत् + अपानेन (अ छूटा); अपान पर इसलिए प्रश्न नहीं। "
           "डेटा में अंग्रेज़ी ‘समान उसे प्राप्त करता है’ (समानः प्रथमा), हिन्दी ‘वह समान वायु प्राप्त कर लेता है’: कर्ता उलटा (रिपोर्ट किया)। "
           "‘पर्याप्तम्’ का अर्थ ‘पूरी तरह’, पर व्याकरण-चिह्न क्त-प्रत्ययान्त नपुंसक प्रथमा। "
           "संधि जाँची: यत्तत्रौषध- = यत् + तत्र + औषध- (अ + औ → औ); पर्याप्तमचिरादेव = पर्याप्तम् + अचिरात् + एव। वीर्य यहाँ शक्ति।"),
    "76": ("विश्वास: निम्न। पंक्तियाँ ०५.०५.१४६-१४७; क्रिया ‘यान्ति’ दूसरी पंक्ति में। "
           "‘तूमाः’ अपुनर्स्थापनीय: शायद ‘ऊष्माणः’ (गरम) या ‘तूर्णम्’ (शीघ्र), कोई पक्का नहीं; छपा रूप रखा, इस पर प्रश्न नहीं। "
           "डेटा की हिन्दी ‘अनुमानित पाठ के अनुसार तूमाः अस्पष्ट’ में कोई अनुमानित पाठ अपनाया नहीं गया है। "
           "संधि जाँची: समानादुत्तरं = समानात् + उत्तरम्; चैवं = च + एवम्; व्यानाद्याः = व्यान + आद्याः; शरीरानुग्रहे = शरीर + अनुग्रहे। छपा ‘यांति’ = यान्ति।"),
    "77": ("विश्वास: मध्यम। पंक्तियाँ ०५.०५.१४८-१४९, एक वाक्य; कर्ता १४६-१४७ के वायु। "
           "text_flag: छपा ‘प्रैसह्य’ कोई शब्द नहीं, सुझाया पाठ ‘प्रसह्य’ (बलपूर्वक दबाकर); इस पर प्रश्न नहीं। "
           "खुला अवलोकन (०५.०५.१४९): ‘संतर्पयन्ति’ का अंग्रेज़ी ‘nourish’ बनाम शब्दावली का ‘satiate’ (तर्पण = तृप्ति); इस पर प्रश्न नहीं। "
           "‘भूत’ = महाभूत (सम्भावित), पाठ नहीं कहता। संधि जाँची: परितःस्वान्स्वान् = परितः + स्वान् + स्वान्; "
           "भूतगुणांस्तनौ = भूतगुणान् + तनौ (न् + त → ंस्त)। ‘तनौ’ = तनु, सप्तमी एकवचन (द्विवचन नहीं)।"),
    "78": ("विश्वास: मध्यम। पंक्तियाँ ०५.०५.१५०-१५१। एकवचन क्रिया ‘प्रकर्षति’ तीनों कर्ताओं के साथ; कर्म (औषध-वीर्य) अनुक्त। "
           "संधि जाँची: व्यानस्तिर्यगपानोऽधः = व्यानः + तिर्यक् + अपानः + अधः (क् → ग् स्वर से पहले); "
           "प्राणश्चोर्ध्वं = प्राणः + च + ऊर्ध्वम्; यथास्वमेव = यथास्वम् + एव; "
           "नाडीभिर्हारिणीभिरिवोदकं = नाडीभिः + हारिणीभिः + इव + उदकम् (अ + उ → ओ)। ‘उदकम्’ उपमा में।"),
    "79": ("विश्वास: निम्न। पंक्तियाँ ०५.०५.१५२-१५३, एक वाक्य। "
           "खुला अवलोकन (०५.०५.१५२): ‘एवं वा तैः’ छपाई का गलत विभाजन हो सकता है: ‘एवं वातैः’ = वायुओं द्वारा, जिससे ‘तैः’ को अर्थ मिलता; "
           "डेटा छपे पाठ पर ‘या उनसे’; इस पर प्रश्न नहीं। "
           "यक्ष्मन् यानी क्षय रोग (क्षयरोग-प्रकार सम्भावित); ‘यक्ष्मणः’ पुंलिंग द्वितीया बहुवचन, ‘सुकृच्छ्रान्’ से मेल। "
           "संधि जाँची: सिराभिश्च = सिराभिः + च; वपुर्बस्तिः = वपुः + बस्तिः; सुकृच्छ्रानपि = सुकृच्छ्रान् + अपि। छपा ‘हंति’ = हन्ति।"),
    "80": ("विश्वास: मध्यम। पंक्ति ०५.०५.१५४, गद्य-इकाई। ‘सर्वान्तकान्’ शब्दशः ‘सब का अन्त करने वाले’; अभिप्रेत रोग अनुक्त, जोड़े नहीं गए। "
           "‘प्रधानम्’ नपुंसक, ‘बस्तिः’ पुंलिंग: विधेय संज्ञा। ‘कर्म’ = चिकित्सा-प्रक्रियाएँ। "
           "संधि जाँची: बस्तिस्तस्मात् = बस्तिः + तस्मात् (ः → स् त से पहले); निःशेषतश्च = निःशेषतः + च। छपा ‘सर्वांतकान्’ = सर्वान्तकान्।"),
    "81": ("विश्वास: निम्न। पंक्ति ०५.०५.१५५, गद्य-इकाई; अन्तिम ‘इति’ गुरु के उत्तर को समाप्त करता है (अनुवाद से बाहर)। "
           "खुला अवलोकन (०५.०५.१५५, गम्भीर): ‘दोषान्’ सम्भवतः ‘शोधयित्वा’ का कर्म और ‘तेजः’ दीप्ति वाले समास का पहला सदस्य; "
           "डेटा शब्दशः क्रम रखता है; निर्णय बाकी, इस पर प्रश्न नहीं। "
           "text_flags: छपा ‘स्त्रोतसि’ = स्रोतसि (वर्तनी-सामान्यीकरण); छपा ‘दीप्तिमिमिति’ में अतिरिक्त ‘मि’, शुद्ध ‘दीप्तिमिति’; इन पर प्रश्न नहीं। "
           "संधि जाँची: कुर्याद्दोषांस्तेजः = कुर्यात् + दोषान् + तेजः (न् + त → ंस्त)।"),
    "82": ("विश्वास: उच्च। पंक्ति ०५.०५.१५६, अध्याय का समापन-वाक्य (कोलोफ़ोन), श्लोक नहीं। आरम्भ का ‘॥’ छपाई-चिह्न है। "
           "संधि जाँची: इतिसिद्धबस्तिकल्पो नाम = इति + सिद्धबस्तिकल्पः + नाम (अः → ओ सघोष से पहले); पंचमोऽध्यायः = पञ्चमः + अध्यायः। "
           "‘सिद्ध’ डेटा में ‘accomplished’; शब्दावली में सिद्ध का सामान्य अर्थ ‘पकाया हुआ’। शीर्षक का अनुवाद छपे रूप पर।"),
}


AIDS = {
    "74": {
        "chain": {"steps": ["बस्ति पक्वाशय में स्थित", "अपने वीर्य (शक्ति) से", "पैर से सिर तक के दोष खींचे",
                            "जैसे सूर्य धरती के रस"]},
        "sandhi": "इः → इर् स्वर से पहले: बस्तिः + आदत्ते → बस्तिरादत्ते; अः + अ → ओऽ: पक्वाशयस्थः + अपि → पक्वाशयस्थोऽपि।",
        "anchors": "पक्वाशय = पचे हुए का स्थान · आपादमस्तकम् = पैर से सिर तक · वीर्य = शक्ति · आदत्ते = खींच लेता है · अर्क = सूर्य · भूरस = धरती के रस।",
    },
    "75": {
        "chain": {"steps": ["वहाँ औषध का वीर्य", "वायु के द्वारा (छपा ‘तद्पानेन’: अपान, अनुमानित)", "शीघ्र ही, पूरी तरह",
                            "समान वायु उसे पाए"]},
        "sandhi": "त् → द् स्वर से पहले: अचिरात् + एव → अचिरादेव; अ + औ → औ: तत्र + औषध → तत्रौषध।",
        "anchors": "औषध = दवा · वीर्य = शक्ति (शुक्र नहीं) · अचिरात् = शीघ्र · प्रतिपद्यते = प्राप्त करता है · समान = समान नामक वायु।",
    },
    "76": {
        "frame": "पहले: समान · फिर: व्यान आदि वायु, क्रम से · वे: अपनी प्रकृति में जाते हैं · कैसे: शरीर के अनुग्रह में स्थित (‘तूमाः’ अस्पष्ट)।",
        "sandhi": "त् → द् स्वर से पहले: समानात् + उत्तरम् → समानादुत्तरम्; अ + आ → आ: व्यान + आद्याः → व्यानाद्याः।",
        "anchors": "उत्तरम् = बाद में · आद्य = से आरम्भ होने वाले · पवन = वायु · क्रमात् = क्रम से · प्रकृति = स्वाभाविक अवस्था · अनुग्रह = सहारा।",
    },
    "77": {
        "contrast": "-औ के दो रूप: पित्तश्लेष्माणौ = द्विवचन (दो दोष, पित्त और कफ) ↔ तनौ = तनु की सप्तमी एकवचन (शरीर में)।",
        "sandhi": "न् + त → ंस्त: भूतगुणान् + तनौ → भूतगुणांस्तनौ।",
        "anchors": "श्लेष्मन् = कफ · यथास्थानम् = अपने अपने स्थान पर · निवेश्य = स्थापित करके · परितः = चारों ओर · स्वान् स्वान् = अपने अपने · तनु = शरीर।",
    },
    "78": {
        "diagram": {"groups": [{"label": "व्यान", "items": ["तिरछा (तिर्यक्)"]},
                               {"label": "अपान", "items": ["नीचे (अधः)"]},
                               {"label": "प्राण", "items": ["ऊपर (ऊर्ध्वम्)"]}]},
        "sandhi": "ः → स् त से पहले: व्यानः + तिर्यक् → व्यानस्तिर्यक्; क् → ग् स्वर से पहले: तिर्यक् + अपानः → तिर्यगपानः; अः + अ → ओऽ: अपानः + अधः → अपानोऽधः।",
        "anchors": "तिर्यक् = तिरछा · अधः = नीचे · ऊर्ध्वम् = ऊपर · प्रकर्षति = खींचता है · नाडी = नाली · हारिणी = बहाने वाली · उदक = जल।",
    },
    "79": {
        "chain": {"steps": ["सुयोजित बस्ति", "सिराओं के द्वारा", "पूरे शरीर में व्याप्त", "कष्टसाध्य यक्ष्मन् भी नष्ट"]},
        "sandhi": "उः → उर् सघोष से पहले: वपुः + बस्तिः → वपुर्बस्तिः; इः + च → इश्च: सिराभिः + च → सिराभिश्च।",
        "anchors": "सिरा = नली (वाहिका) · वपुः = शरीर · सुयोजित = ठीक से प्रयुक्त · व्याप्नुवन् = फैलता हुआ · प्रसभम् = बलपूर्वक · यक्ष्मन् = क्षय रोग।",
    },
    "80": {
        "chain": {"steps": ["तस्मात्: इसलिए", "बस्ति सब कर्मों में प्रधान",
                            "सर्वान्तकों को पूरी तरह नष्ट करे"]},
        "sandhi": "ः → स् त से पहले: बस्तिः + तस्मात् → बस्तिस्तस्मात्; ः → श् च से पहले: निःशेषतः + च → निःशेषतश्च।",
        "anchors": "तस्मात् = इसलिए · कर्म = चिकित्सा-प्रक्रिया · प्रधान = मुख्य · सर्वान्तक = सब का अन्त करने वाले · निःशेषतः = पूरी तरह।",
    },
    "81": {
        "chunks": "(स्रोतसि अन्तः) | शोधयित्वा च | कुर्यात् | दोषान् तेजः | शुक्र-देह-अग्नि-दीप्तिम् | इति",
        "sandhi": "त् → द् सघोष से पहले: कुर्यात् + दोषान् → कुर्याद्दोषान्; न् + त → ंस्त: दोषान् + तेजः → दोषांस्तेजः।",
        "anchors": "शोधयित्वा = शुद्ध करके · कुर्यात् = करे · शुक्र = वीर्य (रेतस्) · देह = शरीर · अग्नि = जठराग्नि · दीप्ति = चमक।",
    },
    "82": {
        "chunks": "इति | सिद्धबस्तिकल्पो | नाम | पञ्चमोऽध्यायः",
        "anchors": "इति = इस प्रकार · कल्प = विधि · नाम = नामक · पञ्चम = पाँचवाँ · अध्याय = अध्याय।",
    },
}


IMAGE_SPECS = {
    ("74", "chain"): {
        "file": "ka5-virya-akarshana-74.svg",
        "alt": ("Flowchart of verse 74: the basti staying in the pakvashaya, by its potency, draws the doshas from "
                "foot to head, as the sun draws the juices of the earth"),
        "type": "mermaid",
        "code": ('flowchart TD\n  A["बस्ति पक्वाशय में"] --> B["अपने वीर्य से"]\n'
                 '  B --> C["पैर से सिर तक के<br/>दोष खींचे"]\n'
                 '  D["उपमा: सूर्य खींचे<br/>धरती के रस"] -.-> C\n'),
    },
    ("75", "chain"): {
        "file": "ka5-samana-prapti-75.svg",
        "alt": ("Chain of verse 75: the drug's potency there; by a wind (apana on a suggested reading); very soon "
                "and fully; the samana wind obtains it"),
        "type": "chain",
        "title": "श्लोक ७५: औषध-वीर्य कहाँ",
        "steps": ["वहाँ औषध का वीर्य", "वायु द्वारा (अपान, अनुमानित)", "शीघ्र ही, पूरी तरह", "समान वायु उसे पाए"],
    },
    ("78", "diagram"): {
        "file": "ka5-vayu-disha-78.svg",
        "alt": ("Table of verse 78: three winds and the direction each draws: vyana crosswise, apana downward, "
                "prana upward, as water through carrying channels"),
        "type": "table",
        "title": "श्लोक ७८: वायु और दिशा (नालियों में जल जैसे)",
        "heads": ["वायु", "किस ओर खींचे"],
        "rows": [["व्यान", "तिरछा"], ["अपान", "नीचे"], ["प्राण", "ऊपर"]],
    },
    ("79", "chain"): {
        "file": "ka5-yakshma-nasha-79.svg",
        "alt": ("Flowchart of verse 79: the well-applied basti, by the siras, pervades the body and forcibly destroys "
                "even the very difficult yakshmans"),
        "type": "mermaid",
        "code": ('flowchart TD\n  A["सुयोजित बस्ति"] --> B["सिराओं के द्वारा"]\n'
                 '  B --> C["पूरे शरीर में व्याप्त"]\n'
                 '  C --> D["कष्टसाध्य यक्ष्मन्<br/>भी नष्ट"]\n'),
    },
    ("80", "chain"): {
        "file": "ka5-pradhana-karma-80.svg",
        "alt": ("Flowchart of unit 80: therefore basti is the chief of all procedures, and it destroys the "
                "all-ending ones completely"),
        "type": "mermaid",
        "code": ('flowchart TD\n  A["तस्मात्: इसलिए"] --> B["बस्ति: सब कर्मों<br/>में प्रधान"]\n'
                 '  B --> C["सर्वान्तकों को<br/>पूरी तरह नष्ट"]\n'),
    },
}
