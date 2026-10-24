from helpers import mcq, match, order, fill, multi, accepts


def T(q, teaches):
    q["teaches"] = teaches
    return q


AUTHORED = {}

# ---------------------------------------------------------------- unit 13
AUTHORED["13"] = {
    "title": "वैकृतास्तु",
    "question": "By unit 13, where do the vaikṛta (abnormal) ones arise and take root, and what is said of ojas?",
    "rule": ("The vaikṛta (abnormal) ones arise from the foods of one come out of the womb and grow only on the "
             "prākṛta (natural) ones; by time and so on they favour and vitiate the body. Ojas: supreme, in the heart, "
             "eight drops in measure."),
    "limits": ('Prose, confidence low, heavily damaged; the noun of वैकृत/प्राकृत is not printed (doṣas, by the section). असात्, स्वप्नमाणवृद्धिक्षययोगात् and प्राकृतिकल्य are unclear; no guess is adopted or asked. The ojas clauses are loose: आधारः has no stated object, so nothing is asked about what ojas supports.'),
    "explain_hi": ("यह पंक्ति प्राकृत और वैकृत का भेद आगे बढ़ाती है: वैकृत (विकृत) गर्भ से बाहर आए व्यक्ति के आहारों से उत्पन्न होते हैं और प्राकृतों (स्वाभाविकों) पर ही जमते हैं। "
                   "वे काल आदि के वश से शरीर का अनुग्रह भी करते हैं और उसे दूषित भी करते हैं। "
                   "उसी प्रकार ओज भी परम है, हृदय में स्थित है और आठ बूँद के माप का है। "
                   "पंक्ति बहुत क्षतिग्रस्त है: ‘असात्’, ‘स्वप्नमाणवृद्धिक्षययोगात्’ और ‘प्राकृतिकल्य’ अस्पष्ट हैं, और ओज वाले अन्तिम वाक्यांश का अनुवाद ढीला है; इन पर कोई प्रश्न नहीं। "
                   "‘प्राकृतेष्वेव’ में प्राकृतेषु + एव (उ + ए → वे) और ‘तद्वदोजः’ में तद्वत् + ओजः (स्वर से पहले त् → द्) है।"),
    "hook": "वैकृत प्राकृत पर ही उगते; ओज हृदय में, आठ बूँद।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 13, where is ojas situated?",
            ("In the heart", "हृदयस्थम्: situated in the heart."),
            [("In the soles", "Unit 13 places ojas in the heart (हृदयस्थम्), not in the soles."),
             ("In the eyes", "Unit 13 places ojas in the heart, not in the eyes."),
             ("In the joints", "Unit 13 places ojas in the heart, not in the joints.")],
            "हृदयस्थम् अष्टबिन्दुप्रमाणम्: in the heart, eight drops in measure.",
            "ओजः ... हृदयस्थम्."),
        order(1, "Put these printed parts of unit 13 in the line's order.",
              ["वैकृतास्तु", "प्राकृतेष्वेव रोहंति", "देहमनुगृह्णंति", "दूषयंति च", "तद्वदोजोऽपि परं"],
              "The abnormal ones; grow only on the natural ones; favour the body; and vitiate; likewise ojas too, supreme.",
              "वैकृतास्तु → प्राकृतेष्वेव रोहंति → देहमनुगृह्णंति → दूषयंति च → तद्वदोजोऽपि परं."),
        match(2, "Match each word of unit 13 to its meaning.",
              [["वैकृत", "abnormal"], ["प्राकृत", "natural"], ["रोहन्ति", "they grow, take root"],
               ["दूषयन्ति", "they vitiate, spoil"], ["अष्टबिन्दु", "eight drops"]],
              "वैकृत = abnormal, प्राकृत = natural, रोहन्ति = grow, दूषयन्ति = vitiate, अष्टबिन्दु = eight drops.",
              "वैकृत, प्राकृत, रोहन्ति, दूषयन्ति, अष्टबिन्दु.", role="extend",
              teaches="प्राकृत (natural) and वैकृत (abnormal) are paired: by unit 13 the vaikṛta ones grow only on the prākṛta ones."),
        mcq("discriminate", 3, "Which split of प्राकृतेष्वेव in unit 13 is right?",
            ("प्राकृतेषु + एव", "उ before a different vowel becomes व्: -षु + एव → -ष्वेव (on the natural ones only)."),
            [("प्राकृतेषु + इव", "उ + इ would give -ष्वि: that would be प्राकृतेष्विव."),
             ("प्राकृतेषु + अव", "उ + अ would give -ष्व: that would be प्राकृतेष्वव."),
             ("प्राकृतेषः + एव", "अः before ए would give अ: that would be प्राकृतेष एव.")],
            "प्राकृतेषु (on the natural ones) + एव (only).",
            "उ + a different vowel → व् + that vowel."),
        mcq("apply", 4, "By unit 13, on what do the vaikṛta (abnormal) ones grow?",
            ("Only on the natural ones", "प्राकृतेष्वेव रोहन्ति: they grow only on the prākṛta (natural) ones."),
            [("Only on the ojas itself", "Unit 13 says they grow on the prākṛta ones, not on ojas."),
             ("Only on other abnormal ones", "They grow on the natural (prākṛta) ones, not on the abnormal."),
             ("Only on the foods outside", "They arise from foods but grow on the prākṛta ones.")],
            "वैकृतास्तु ... प्राकृतेष्वेव रोहन्ति.",
            "वैकृत grow only (एव) on प्राकृत."),
        mcq("transfer", 5, "By the join in तद्वदोजः (तद्वत् + ओजः), how is पूर्ववत् + इदम् (this, as before) joined in a new example?",
            ("पूर्ववदिदम्", "A final त् before a vowel becomes द्: पूर्ववत् + इदम् → पूर्ववदिदम्."),
            [("पूर्ववतिदम्", "त् cannot stay त् before a vowel; it becomes द्."),
             ("पूर्ववन्निदम्", "त् may become न् (optionally) only before a nasal; इ is a vowel, so here it is द्."),
             ("पूर्ववदेदम्", "The इ of इदम् does not change; only त् becomes द्.")],
            "पूर्ववत् + इदम् = पूर्ववदिदम्, like तद्वत् + ओजः = तद्वदोजः.",
            "Final त् + vowel → द् + vowel.",
            teaches="A final त् before a vowel becomes द्: तद्वत् + ओजः → तद्वदोजः, पूर्ववत् + इदम् → पूर्ववदिदम्."),
    ],
}

# ---------------------------------------------------------------- unit 14
AUTHORED["14"] = {
    "title": "वातप्रकृति के लक्षण",
    "question": "By unit 14, what marks of body, mind and liking does one of Vāta constitution show?",
    "rule": ("One of Vāta constitution is thin and dry, with thin, scanty limbs, teeth, nails, hair, eyes and voice; "
             "noisy joints; quick to begin and forget; unsteady; a thief, envious, senses unconquered; fond of music, "
             "quarrel, hunting, journeys; likes unctuous, hot, sweet, salty food."),
    "limits": ('Prose ending in भवति; the description goes on in units 16-17. शीतद्विदुद्वद्ध is read शीतद्विट् + उद्बद्ध (hater of cold, tight calves), not firm; मधुराम्स is read मधुर-अम्ल (sour) by conjecture. Neither is asked. गान्धर्व = music is probable.'),
    "explain_hi": ("अपने दोष के गुणों के अनुसार वातप्रकृति वाला दुबला और रूखा होता है; उसके अंग, दाँत, नाखून, रोम, नेत्र और स्वर पतले और कम होते हैं। "
                   "उसके जोड़ चलते समय शब्द करते हैं; वह आरम्भ, क्षोभ, ग्रहण और भूलने में शीघ्र और धैर्य, बुद्धि, चाल, दृष्टि, स्वभाव और मित्रता में चंचल है। "
                   "वह चोर, अनार्य, ईर्ष्यालु और अजितेन्द्रिय है; संगीत (सम्भावित अर्थ), इतिहास, हास, विलास, कलह, शिकार, उद्यान और यात्रा उसे प्रिय हैं। "
                   "उसे चिकने, गरम, मीठे और नमकीन अन्न-पान की इच्छा होती है और वे उसके अनुकूल हैं; ‘खट्टा’ अनुमानित पाठ पर है। "
                   "‘तनूरूक्षः’ में तनुः + रूक्षः है: उ के बाद का विसर्ग र् बनता, र से पहले वह र् लुप्त होता और उ दीर्घ हो जाता है।"),
    "hook": "वात: तनु, रूक्ष, चंचल, शीघ्र आरम्भ, शीघ्र विस्मरण।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 14, what is the body of one of Vāta constitution like?",
            ("Thin and dry", "तनू रूक्षः: thin (तनुः) and dry (रूक्षः)."),
            [("Warm and fair", "Unit 14 says thin and dry; warm and fair is not said of Vāta."),
             ("Full and handsome", "Unit 14 says thin and dry, the opposite of full."),
             ("Heavy and smooth", "Unit 14 says thin and dry, not heavy and smooth.")],
            "वातप्रकृतिस्तनूरूक्षः: thin and dry.",
            "वातप्रकृति: तनु, रूक्ष."),
        order(1, "Put these things the Vāta person is fond of (प्रिय) in the order of unit 14.",
              ["गान्धर्व (music, probable)", "इतिहास (legends)", "कलह (quarrel)", "मृगया (hunting)",
               "उद्यान (gardens)", "यात्रा (journeys)"],
              "प्रियगान्धर्वेतिहासहासविलासकलहमृगयोद्यानयात्रः: music, legends, (laughter, play), quarrel, hunting, gardens, journeys.",
              "गान्धर्व → इतिहास → कलह → मृगया → उद्यान → यात्रा."),
        match(2, "Match each mark of the Vāta person in unit 14 to its meaning.",
              [["सशब्दसन्धिगामी", "going with noisy joints"], ["स्तेनः", "a thief"], ["मत्सरी", "envious"],
               ["अजितेन्द्रियः", "with senses not conquered"], ["अनार्यः", "ignoble"]],
              "सशब्दसन्धिगामी = going with noisy joints; स्तेनः = a thief; मत्सरी = envious; अजितेन्द्रियः = senses unconquered; अनार्यः = ignoble.",
              "सशब्दसन्धिगामी, स्तेनः, मत्सरी, अजितेन्द्रियः, अनार्यः.", role="extend",
              teaches="Unit 14 lists the Vāta person's marks as nouns and adjectives in the nominative, ending with भवति (he is)."),
        multi("discriminate", 3, "By unit 14, which kinds of food and drink does the Vāta person desire, and which suit him?",
              [("स्निग्ध (unctuous)", "Right: स्निग्ध heads the list of what he desires."),
               ("शीत (cold)", "Not in his list; the list has उष्ण (hot)."),
               ("मधुर (sweet)", "Right: मधुर is in the list."),
               ("रूक्ष (dry)", "Not in his list; he is himself dry (रूक्षः), and the list has स्निग्ध."),
               ("लवण (salty)", "Right: लवण is in the list."),
               ("उष्ण (hot)", "Right: उष्ण is in the list.")],
              [0, 2, 4, 5],
              "स्निग्धोष्णमधुर...लवणान्नपानकाङ्क्षोपशयः: unctuous, hot, sweet, salty (sour only on a conjectural reading).",
              "काङ्क्षा = desire, उपशय = what suits."),
        mcq("apply", 4, "Which split of मत्सर्यजितेंद्रियः in unit 14 is right?",
            ("मत्सरी + अजितेन्द्रियः", "ई before a different vowel becomes य्: मत्सरी + अजित- → मत्सर्यजित-."),
            [("मत्सरी + जितेन्द्रियः", "Before the consonant ज, ई would stay: that would be मत्सरीजितेन्द्रियः."),
             ("मत्सरः + यजितेन्द्रियः", "यजितेन्द्रियः is not a word; the य comes from ई."),
             ("मत्सरे + अजितेन्द्रियः", "ए before अ would give ए + ऽ: that would be मत्सरेऽजितेन्द्रियः.")],
            "मत्सरी (envious) + अजितेन्द्रियः (senses unconquered).",
            "ई + a different vowel → य् + that vowel."),
        mcq("transfer", 5, "By the join तनुः + रूक्षः → तनू रूक्षः in unit 14, how is साधुः + राजते joined in a new example?",
            ("साधू राजते", "After उ the visarga becomes र्; before र that र् drops and उ is lengthened: साधू राजते."),
            [("साधुर्राजते", "Two र् do not stand together; the first drops and उ lengthens."),
             ("साधुराजते", "When the र् drops, the उ before it is lengthened to ऊ."),
             ("साधो राजते", "ओ comes from अः before a voiced consonant, not from उः.")],
            "साधुः + राजते = साधू राजते, like तनुः + रूक्षः = तनू रूक्षः.",
            "उः + र → ऊ र.",
            teaches="After इ or उ a visarga becomes र्; before a following र that र् is dropped and the vowel is lengthened: तनुः + रूक्षः → तनू रूक्षः."),
    ],
}

# ---------------------------------------------------------------- unit 15
AUTHORED["15"] = {
    "title": "अपिच",
    "question": "What does the connective अपिच in unit 15 mean, and how is it built?",
    "rule": "अपि (also) + च (and) = 'and further': a stock link; here it leads into the lines of the next units (data).",
    "limits": ("Prose, one printed word, written without a space between अपि and च. It only links; no question rests on "
               "what follows."),
    "explain_hi": ("यह एक शब्द की गद्य-पंक्ति है: ‘अपि च’ यानी और भी। "
                   "अपि (भी) और च (और) दोनों अव्यय हैं; मिलकर वे आगे की बात खोलते हैं। "
                   "डेटा के अनुसार यह अगली इकाइयों की पंक्तियों का आरम्भ कराता है। "
                   "व्यंजन च से पहले अपि का इ नहीं बदलता; स्वर से पहले वह य् बन जाता (अपि + उक्तम् → अप्युक्तम्)।"),
    "hook": "अपि च: और भी, अब आगे।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "In unit 15, what does अपिच mean?",
            ("And further", "अपि (also) + च (and): and further."),
            [("Not so at all", "No negation (न) is printed; अपि च adds."),
             ("Or else", "'Or' would be वा; अपि च adds."),
             ("Only that", "'Only' would be एव; अपि च adds.")],
            "अपि च = and further.",
            "अपि = also; च = and."),
        match(1, "Match each part of unit 15 to its meaning.",
              [["अपि", "also, too"], ["च", "and"], ["अपि च", "and further"]],
              "अपि = also; च = and; अपि च = and further.",
              "अपि, च, अपि च."),
        fill(2, "Unit 15: अपिच = ____ + च (also + and). Type it in Devanagari or in English letters (e.g. dharma).",
             accepts("अपि"),
             "अपि (also) + च (and) = अपि च.",
             "अपि is an indeclinable, 'also, too'; with च it makes the link अपि च.",
             "अपि + च = अपिच."),
        mcq("discriminate", 3, "Which split of the printed अपिच in unit 15 is right?",
            ("अपि + च", "Two indeclinables, अपि (also) and च (and), printed without a space."),
            [("अप् + इच", "इच is no word; the words are अपि and च."),
             ("अपी + च", "अपी is no word; the particle is अपि."),
             ("अ + पिच", "पिच is no word; the particle is अपि.")],
            "अपि + च.",
            "अपिच = अपि + च."),
        mcq("apply", 4, "In unit 15, why does अपि keep its इ before च?",
            ("च is a consonant", "Vowel sandhi needs a vowel after it; before a consonant the इ stays."),
            [("च is a long vowel", "च is a consonant, not a vowel."),
             ("अपि has no final vowel", "अपि ends in the vowel इ."),
             ("इ never changes at all", "इ does change before a different vowel: it becomes य्.")],
            "अपि + च: the next sound is a consonant, so no vowel sandhi.",
            "A final vowel stays before a consonant."),
        mcq("transfer", 5, "By vowel sandhi, how is अपि + उक्तम् (said too) joined in a new example?",
            ("अप्युक्तम्", "इ before a different vowel becomes य्: अपि + उक्तम् → अप्युक्तम्."),
            [("अपुक्तम्", "The इ is not simply dropped; it becomes य्."),
             ("अपोक्तम्", "ओ comes from अ + उ, not from इ + उ."),
             ("अपीक्तम्", "ई comes from इ + इ, not from इ + उ.")],
            "अपि + उक्तम् = अप्युक्तम्.",
            "इ + a different vowel → य् + that vowel.",
            teaches="अपि stays as it is before a consonant (अपि च), but before a different vowel its इ becomes य् (अप्युक्तम्)."),
    ],
}

# ---------------------------------------------------------------- unit 16
AUTHORED["16"] = {
    "title": "अल्पवित्तबलजीवितनिद्रः",
    "question": "By unit 16, which further marks of the Vāta person are listed?",
    "rule": ("He has little wealth, strength, life and sleep; a body spread over with vessels (probably the visible "
             "veins); he is unfortunate, eats very much, talks much, is an unbeliever (नास्तिक), and has split hair, "
             "hands and feet."),
    "limits": ("Typed prose, though the lines appear metrical (not asked; no metre aid). Continues the Vāta description of unit 14. क्षाम may go with वाच् (weak speech) or with the whole man: not asked. धमनी as visible veins is probable. दुर्भग may also mean disagreeable."),
    "explain_hi": ("ये पंक्तियाँ इकाई १४ के वात-वर्णन को आगे बढ़ाती हैं; वहाँ की क्रिया ‘भवति’ यहाँ दोहराई नहीं गई। "
                   "वातप्रकृति वाले के धन, बल, जीवन और नींद थोड़े होते हैं; उसका शरीर धमनियों (सम्भवतः दिखने वाली नसों) से फैला हुआ होता है। "
                   "वह दुर्भग (भाग्यहीन), बहुत खाने वाला, बहुत बोलने वाला और नास्तिक है; उसके केश, हाथ और पैर फटे हुए होते हैं। "
                   "‘क्षाम’ वाणी के साथ (कृश वाणी) या पूरे व्यक्ति के साथ पढ़ा जा सकता है, इसलिए उस पर प्रश्न नहीं। "
                   "‘वाग्धमनि’ में वाच् का च् पदान्त में क् बनकर घोष ध से पहले ग् हुआ है; ‘दुर्भगोऽति’ में अः + अ → ओऽ।"),
    "hook": "धन-बल-जीवन-नींद थोड़े, पर खाना-बोलना बहुत।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 16, how much does the Vāta person eat?",
            ("Very much", "अतिबहुभुक्: eating very much."),
            [("Very little", "अति-बहु-भुक् is 'very much eating', not little."),
             ("Only once a day", "Unit 16 gives no count of meals; it says very much."),
             ("Only at night", "Unit 16 gives no time of eating; it says very much.")],
            "अतिबहुभुक् = eating very much.",
            "अति-बहु-भुक् = very-much-eating."),
        order(1, "Put the four things of which he has little in the order of अल्पवित्तबलजीवितनिद्रः (unit 16).",
              ["वित्त (wealth)", "बल (strength)", "जीवित (life)", "निद्रा (sleep)"],
              "अल्प-वित्त-बल-जीवित-निद्रः: little wealth, strength, life and sleep.",
              "वित्त → बल → जीवित → निद्रा."),
        match(2, "Match each word of unit 16 to its meaning.",
              [["वित्त", "wealth"], ["निद्रा", "sleep"], ["बहुभाषी", "talkative"], ["दुर्भगः", "unfortunate"],
               ["अंघ्रि", "foot"]],
              "वित्त = wealth; निद्रा = sleep; बहुभाषी = talkative; दुर्भगः = unfortunate; अङ्घ्रि = foot.",
              "वित्त, निद्रा, बहुभाषी, दुर्भगः, अङ्घ्रि.", role="extend",
              teaches="अल्प at the head of a compound qualifies every member after it: अल्प-वित्त-बल-जीवित-निद्रः."),
        mcq("discriminate", 3, "What does नास्तिकः mean in unit 16?",
            ("One who denies", "नास्तिक: one who denies (the next world, or the Veda), an unbeliever."),
            [("One with no nose", "नासिका is the nose; नास्तिक comes from न अस्ति, 'it is not'."),
             ("One who is absent", "नास्तिक is a fixed word for an unbeliever, not one who is away."),
             ("One who is sleepless", "Sleep is निद्रा, named earlier in the unit; नास्तिक denies.")],
            "नास्तिकः = an unbeliever, one who denies.",
            "नास्तिक = one who says 'it is not'."),
        mcq("apply", 4, "Why does printed क्षामवाग्धमनि (unit 16) show ग् where the word वाच् ends in च्?",
            ("च् → क्, then ग् before ध", "A final च् is replaced by क् as at a word end, and क् becomes ग् before the voiced ध."),
            [("ग् is the first sound of धमनी", "धमनी begins with ध; the ग् is the end of वाच्."),
             ("च् becomes ग् before any sound", "Before a vowel or a voiced sound only; before a voiceless one it stays क्."),
             ("च् → ग् before an unvoiced ध", "ध is a voiced consonant; that is why क् becomes ग्.")],
            "वाच् + धमनि → वाक् → वाग्धमनि.",
            "Final च् → क्; क् + voiced consonant → ग्."),
        mcq("transfer", 5, "By the join in दुर्भगोऽति (दुर्भगः + अति), how is नरः + अयम् joined in a new example?",
            ("नरोऽयम्", "अः before अ becomes ओ and the अ is dropped (written ऽ): नरोऽयम्."),
            [("नर अयम्", "अः drops its visarga only before vowels other than अ."),
             ("नरायम्", "अः + अ does not give आ; it gives ओऽ."),
             ("नररयम्", "After अ the visarga does not become र्.")],
            "नरः + अयम् = नरोऽयम्, like दुर्भगः + अति = दुर्भगोऽति.",
            "अः + अ → ओऽ.",
            teaches="अः before अ becomes ओ, and the following अ is elided (marked ऽ): दुर्भगः + अति → दुर्भगोऽति."),
    ],
}

# ---------------------------------------------------------------- unit 17
AUTHORED["17"] = {
    "title": "किंचिदुन्मिषितदृङ्मुख",
    "question": "By unit 17, what does the Vāta person do with his teeth, and where does he go?",
    "rule": ("He grinds his teeth (खादति दन्तान्), and he goes in dry, rough, uneven rivers, in the sky and on mountain "
             "peaks. The subject 'he' (the Vāta person) is understood."),
    "limits": ("Typed prose, though the lines appear metrical (not asked); confidence low. क्थति is unclear, स्तन्यते is not sure, and the split around मुख is not sure: none is asked. The unit has no word for sleep or dream, and none is supplied."),
    "explain_hi": ("ये पंक्तियाँ भी वात-वर्णन में हैं; कर्ता ‘वह’ समझा गया है। "
                   "पहली पंक्ति में थोड़ी खुली दृष्टि और ढीला मुख, कराहना और दाँत चबाना है; पर ‘क्थति’ अस्पष्ट है, ‘स्तन्यते’ रूप अनिश्चित है और मुख वाले समास का विभाग पक्का नहीं। "
                   "दूसरी पंक्ति कहती है कि वह सूखी, रूखी, ऊबड़-खाबड़ नदियों में, आकाश में और पर्वत की चोटियों पर जाता है। "
                   "इस इकाई में नींद या स्वप्न का कोई शब्द नहीं; डेटा कोई शब्द नहीं जोड़ता। "
                   "‘शुष्करूक्षविषमासु’ स्त्रीलिंग सप्तमी बहुवचन है, इसलिए वह ‘सरित्सु’ (नदियों में) का विशेषण है।"),
    "hook": "दाँत चबाए; सूखी नदी, आकाश, पर्वत-शिखर।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 17, what does he do to his teeth (दन्तान्)?",
            ("He grinds them", "खादति दन्तान्: he chews, grinds his teeth."),
            [("He bares them", "खादति is chews, grinds; baring is not said."),
             ("He loses them", "Unit 17 says he grinds them (खादति), not that he loses them."),
             ("He cleans them", "खादति is chews, grinds; cleaning is not said.")],
            "खादति दन्तान् = he grinds his teeth.",
            "खादति = chews, grinds."),
        order(1, "Put the places he goes to in the order of unit 17.",
              ["शुष्करूक्षविषमासु सरित्सु", "व्योम्नि", "शैलशिखरेषु", "च याति"],
              "In dry, rough, uneven rivers; in the sky; on mountain peaks; and he goes.",
              "सरित्सु → व्योम्नि → शैलशिखरेषु → याति."),
        match(2, "Match each word of unit 17 to its meaning.",
              [["सरित्", "river"], ["व्योमन्", "sky"], ["शैलशिखर", "mountain peak"], ["याति", "goes"],
               ["खादति", "chews, grinds"]],
              "सरित् = river; व्योमन् = sky; शैल-शिखर = mountain peak; याति = goes; खादति = chews, grinds.",
              "सरित्, व्योमन्, शैलशिखर, याति, खादति.", role="extend",
              teaches="Three locatives name the places: सरित्सु (in rivers), व्योम्नि (in the sky), शैलशिखरेषु (on mountain peaks)."),
        mcq("discriminate", 3, "Which rendering of शैलशिखरेषु च याति (unit 17) is right?",
            ("And he goes on mountain peaks", "शैलशिखरेषु (loc. pl.) = on mountain peaks; याति = goes."),
            [("And he falls from mountain peaks", "'From' would be an ablative, and याति is goes, not falls."),
             ("And he sees the mountain peaks", "याति is goes (√या), not sees."),
             ("And he goes to the river banks", "शैल-शिखर is mountain peak, not river bank.")],
            "शैलशिखरेषु च याति = and he goes on mountain peaks.",
            "याति = goes; -एषु = locative plural."),
        mcq("apply", 4, "In unit 17, which word does शुष्करूक्षविषमासु (dry, rough, uneven: f. loc. pl.) describe?",
            ("सरित्सु", "सरित्सु is also feminine locative plural: in dry, rough, uneven rivers."),
            [("व्योम्नि", "व्योम्नि is neuter locative singular; it cannot agree with a feminine plural."),
             ("शैलशिखरेषु", "शैलशिखरेषु is neuter locative plural, not feminine."),
             ("दन्तान्", "दन्तान् is masculine accusative plural, not feminine locative.")],
            "शुष्करूक्षविषमासु agrees with सरित्सु: same gender, case and number.",
            "An adjective agrees with its noun in gender, case and number."),
        mcq("transfer", 5, "Built like शुष्करूक्षविषमासु सरित्सु, which form of शीत (cold) agrees with नदीषु (in rivers, f. loc. pl.) in a new example?",
            ("शीतासु", "-आसु is the feminine locative plural: शीतासु नदीषु, in cold rivers."),
            [("शीतेषु", "-एषु is masculine or neuter locative plural; नदी is feminine."),
             ("शीतायाम्", "-आयाम् is feminine locative singular; नदीषु is plural."),
             ("शीतान्", "-आन् is masculine accusative plural, not locative.")],
            "शीतासु नदीषु, like शुष्करूक्षविषमासु सरित्सु.",
            "f. loc. pl. adjective in -आ: -आसु.",
            teaches="An adjective in -अ/-आ takes -आसु to agree with a feminine noun in the locative plural: शुष्करूक्षविषमासु सरित्सु."),
    ],
}

# ---------------------------------------------------------------- unit 18
AUTHORED["18"] = {
    "title": "पित्तप्रकृति के लक्षण",
    "question": "By unit 18, what marks of body, temper and liking does one of Pitta constitution show?",
    "rule": ("One of Pitta constitution is warm and fair-bodied; copper-coloured nails, eyes, tongue, lips, palms and soles; "
             "loose joint-ligaments and flesh; sparse, soft, tawny hair; middling strength and life; brave, proud; early "
             "wrinkles and grey hair; intelligent; likes sweet, astringent, cold."),
    "limits": ('Prose ending in भवति. सृत्पिपासो is read क्षुत्-पिपासः (hunger, thirst) by conjecture: not asked. करभ is camel or young elephant, so the hair comparison is not firm. शीघ्र (early) is taken to qualify the skin and hair changes. Printed तित्त is read तिक्त: not asked.'),
    "explain_hi": ("पित्तप्रकृति वाला गरम और गोरे शरीर वाला होता है; उसके नाखून, नेत्र, जीभ, होंठ, हथेलियाँ और तलवे ताँबे के रंग के होते हैं। "
                   "जोड़ों के बन्धन और मांस ढीले होते हैं; केश और रोम कपिल (भूरे), विरल और मुलायम होते हैं (करभ से तुलना पक्की नहीं)। "
                   "बल और आयु मध्यम, शुक्र, मैथुन और सन्तान थोड़ी; वह शूर, अभिमानी, मेधावी और दुर्भग है। "
                   "उसे झुर्रियाँ, गंजापन, बाल पकना, फुंसियाँ और झाइयाँ जल्दी होती हैं; भूख-प्यास वाला भाग अनुमानित पाठ पर है। "
                   "मीठा, कड़वा, कसैला और ठंडा उसे चाहिए और अनुकूल है; ‘पित्तप्रकृतिरुष्ण’ में इ के बाद का विसर्ग स्वर से पहले र् बना है।"),
    "hook": "पित्त: उष्ण-गौर, ताम्र नख-नेत्र, शीघ्र वली-पलित।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 18, what is the body of one of Pitta constitution like?",
            ("Warm and fair", "उष्णगौरगात्रः: with a warm (उष्ण) and fair (गौर) body."),
            [("Thin and dry", "Unit 18 says warm and fair; thin and dry is the Vāta body of unit 14."),
             ("Cold and dark", "Unit 18 says warm (उष्ण) and fair (गौर), the opposite."),
             ("Full and heavy", "Unit 18 says warm and fair; full is not said of Pitta.")],
            "पित्तप्रकृतिरुष्णगौरगात्रः: warm and fair-bodied.",
            "पित्तप्रकृति: उष्ण, गौर."),
        order(1, "Put the copper-coloured (ताम्र) parts in the order of unit 18.",
              ["नख (nails)", "नयन (eyes)", "जिह्वा (tongue)", "ओष्ठ (lips)", "पाणितल (palms)", "पादतल (soles)"],
              "ताम्र-नख-नयन-जिह्वा-ओष्ठ-पाणि-पाद-तलः: nails, eyes, tongue, lips, palms, soles.",
              "नख → नयन → जिह्वा → ओष्ठ → पाणितल → पादतल."),
        match(2, "Match each word of unit 18 to its meaning.",
              [["ताम्र", "copper-coloured"], ["शिथिल", "loose"], ["वली", "wrinkles"], ["पलित", "grey hair"],
               ["मेधावी", "intelligent"]],
              "ताम्र = copper-coloured; शिथिल = loose; वली = wrinkles; पलित = grey hair; मेधावी = intelligent.",
              "ताम्र, शिथिल, वली, पलित, मेधावी.", role="extend",
              teaches="वली (wrinkles), खलित (baldness) and पलित (grey hair) stand in one compound headed by शीघ्र, read as 'early'."),
        multi("discriminate", 3, "By unit 18, which does the Pitta person desire, and which suit him?",
              [("उष्ण (hot)", "Not in his list; he is himself warm, and the list has शीत (cold)."),
               ("स्वादु (sweet)", "Right: स्वादु heads the list."),
               ("लवण (salty)", "Not in his list."),
               ("शीत (cold)", "Right: शीत ends the list."),
               ("कषाय (astringent)", "Right: कषाय, the astringent taste, is in the list.")],
              [1, 3, 4],
              "स्वादुतित्तकषायशीताभिलाषोपशयः: sweet, bitter (तित्त, read तिक्त), astringent and cold.",
              "अभिलाष = desire, उपशय = what suits."),
        mcq("apply", 4, "In पित्तप्रकृतिरुष्ण (unit 18), why does the visarga of प्रकृतिः appear as र्?",
            ("It follows इ, before a vowel", "After a vowel other than अ/आ, a visarga before a vowel becomes र्: -तिर् + उष्ण."),
            [("It follows अ, before a vowel", "The vowel before the visarga is इ (-ति), not अ."),
             ("Every visarga before उ is र्", "Not every one: अः + उ gives अ उ, आः + उ gives आ उ."),
             ("The र् begins the word उष्ण", "उष्ण begins with the vowel उ; the र् comes from the visarga.")],
            "पित्तप्रकृतिः + उष्ण: इः before a vowel → इर्.",
            "इः / उः + vowel → इर् / उर्."),
        mcq("transfer", 5, "By the join पित्तप्रकृतिः + उष्ण → पित्तप्रकृतिरुष्ण, how is मुनिः + आगतः joined in a new example?",
            ("मुनिरागतः", "After इ, a visarga before a vowel becomes र्: मुनिरागतः."),
            [("मुनि आगतः", "After इ the visarga is not dropped; it becomes र्."),
             ("मुनेरागतः", "The इ of मुनि does not change to ए here."),
             ("मुन्यागतः", "इ → य् only when no visarga stands between; here it becomes र्.")],
            "मुनिः + आगतः = मुनिरागतः, like पित्तप्रकृतिः + उष्ण = पित्तप्रकृतिरुष्ण.",
            "इः + vowel → इर् + vowel.",
            teaches="After इ, a visarga before a vowel becomes र्: पित्तप्रकृतिः + उष्ण → पित्तप्रकृतिरुष्ण, मुनिः + आगतः → मुनिरागतः."),
    ],
}

# ---------------------------------------------------------------- unit 19
AUTHORED["19"] = {
    "title": "अपिच",
    "question": "What do the two words of अपिच in unit 19 mean?",
    "rule": "अपि = also, च = and: together 'and further', a stock link that opens what follows.",
    "limits": "Prose, one printed word (अपि and च without a space). Questions ask only about the two words and their join.",
    "explain_hi": ("इकाई १९ फिर वही जोड़ने वाला शब्द है: ‘अपि च’ यानी और भी। "
                   "डेटा के अनुसार यह अगली इकाइयों की पंक्तियाँ आरम्भ कराता है। "
                   "अपि और च दोनों अव्यय हैं, उनके रूप नहीं बदलते। "
                   "व्यंजन से पहले अपि का इ वैसा ही रहता; स्वर ए से पहले वह य् बनता: अपि + एवम् → अप्येवम्।"),
    "hook": "फिर अपि च: अगला वर्णन आता है।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "In unit 19, what kind of words are अपि and च?",
            ("Indeclinables", "अपि and च are indeclinables (avyaya): they take no endings."),
            [("Verb forms", "Neither has a verb ending; both are indeclinables."),
             ("Noun stems", "Neither is a noun with case endings; both are indeclinables."),
             ("Pronoun forms", "Neither stands for a noun; both are indeclinables.")],
            "अपि, च: indeclinables.",
            "अपि, च = avyaya."),
        match(1, "Match each part of unit 19 to its meaning.",
              [["अपि", "also"], ["च", "and"], ["अपिच", "and further"]],
              "अपि = also; च = and; अपिच = and further.",
              "अपि, च, अपिच."),
        fill(2, "Unit 19: अपिच = अपि + ____ (also + and). Type it in Devanagari or in English letters (e.g. dharma).",
             accepts("च"),
             "अपि (also) + च (and).",
             "च means 'and'; it follows the word it joins: अपि च.",
             "अपि + च = अपिच."),
        mcq("discriminate", 3, "Which rendering of अपिच in unit 19 is right?",
            ("And further", "अपि (also) + च (and) = and further."),
            [("Or else, instead", "'Or' would be वा, not च."),
             ("Not even", "No न is printed; अपि च adds."),
             ("Only so", "'Only' would be एव, not अपि.")],
            "अपिच = and further.",
            "अपि + च = and further."),
        mcq("apply", 4, "Before which kind of sound does a final इ (as in अपि of unit 19) stay unchanged?",
            ("Before a consonant", "Vowel sandhi needs a vowel after it; च is a consonant, so अपि stays."),
            [("Before any vowel", "Before a different vowel इ becomes य्; before इ/ई it joins into ई."),
             ("Only before अ", "Before अ the इ becomes य्: अपि + अहम् → अप्यहम्."),
             ("Only before ए", "Before ए the इ becomes य्: अपि + एवम् → अप्येवम्.")],
            "अपि + च: a consonant follows, so no change.",
            "Final vowel + consonant: no vowel sandhi."),
        mcq("transfer", 5, "How is अपि + एवम् (so too) joined in a new example?",
            ("अप्येवम्", "इ before a different vowel becomes य्: अपि + एवम् → अप्येवम्."),
            [("अपेवम्", "The इ is not dropped; it becomes य्."),
             ("अपैवम्", "ऐ comes from अ + ए, not from इ + ए."),
             ("अपीवम्", "ई comes from इ + इ, not from इ + ए.")],
            "अपि + एवम् = अप्येवम्.",
            "इ + a different vowel → य् + that vowel.",
            teaches="A final इ before a different vowel becomes य्: अपि + एवम् → अप्येवम्; before a consonant it stays (अपि च)."),
    ],
}

# ---------------------------------------------------------------- unit 20
AUTHORED["20"] = {
    "title": "दयितमाल्यविलेपनमंडनः",
    "question": "By unit 20, what is dear to the Pitta person, and with what is he endowed?",
    "rule": ("Garlands, unguents and adornment are dear to him; he is well-behaved, pure, affectionate to dependents; "
             "endowed with wealth (or power), daring, intellect and strength; in fears he is a refuge even for the lords "
             "of the quarters."),
    "limits": ("Typed prose, though the lines appear metrical (not asked; no metre aid). Continues the Pitta description. शुचि is pure or clean; गतिः is refuge or resort; 'for' or 'of' the lords of the quarters is not firm. Printed दिंपताम् is read दिक्पताम्: not asked."),
    "explain_hi": ("ये पंक्तियाँ पित्त-वर्णन को आगे बढ़ाती हैं। "
                   "उसे माला, लेप और सजावट प्रिय हैं; वह सदाचारी, शुचि (शुद्ध या स्वच्छ) और आश्रितों पर स्नेह करने वाला है। "
                   "वह वैभव (धन या शक्ति), साहस, बुद्धि और बल से युक्त होता है; भय में दिशाओं के स्वामियों के लिए भी आश्रय होता है। "
                   "छपा ‘वलान्वितो’ में व छपा है, पढ़ा बल गया; ‘दिंपताम्’ को दिक्पताम् पढ़ा गया। "
                   "‘अन्वितो भवति’ में अः घोष व्यंजन भ से पहले ओ बना है।"),
    "hook": "माला-लेप-मण्डन प्रिय; भय में सबका आश्रय।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 20, what is dear (दयित) to the Pitta person?",
            ("Garlands, unguents, adornment", "दयित-माल्य-विलेपन-मण्डनः: garlands, unguents and adornment are dear to him."),
            [("Music, legends and hunting", "Unit 20 names garlands, unguents and adornment, not these."),
             ("Quarrels, play and journeys", "Unit 20 names garlands, unguents and adornment, not these."),
             ("Lotuses, birds and clouds", "Unit 20 names garlands, unguents and adornment, not these.")],
            "दयितमाल्यविलेपनमण्डनः: garlands, unguents, adornment.",
            "माल्य = garland, विलेपन = unguent, मण्डन = adornment."),
        order(1, "Put these printed parts of unit 20 in order.",
              ["दयितमाल्यविलेपनमंडनः", "सुचरितः", "शुचिराश्रितवत्सलः", "विभवसाहसबुद्धिवलान्वितो", "भवति भीषु"],
              "Garlands etc. dear; well-behaved; pure, affectionate to dependents; endowed with wealth etc.; is, in fears.",
              "दयित... → सुचरितः → शुचिराश्रितवत्सलः → विभव...न्वितो → भवति भीषु."),
        match(2, "Match each word of unit 20 to its meaning.",
              [["विभव", "wealth, power"], ["साहस", "daring"], ["बुद्धि", "intellect"],
               ["आश्रितवत्सलः", "affectionate to dependents"], ["सुचरितः", "well-behaved"]],
              "विभव = wealth or power; साहस = daring; बुद्धि = intellect; आश्रितवत्सलः = affectionate to dependents; सुचरितः = well-behaved.",
              "विभव, साहस, बुद्धि, आश्रितवत्सलः, सुचरितः.", role="extend",
              teaches="X-अन्वित = endowed with X: विभव-साहस-बुद्धि-बल-अन्वितः, endowed with wealth, daring, intellect and strength."),
        mcq("discriminate", 3, "What does भीषु mean in unit 20?",
            ("In fears", "भीषु is the locative plural of भी (fear): in fears."),
            [("From fears", "'From' would be an ablative; -षु is the locative plural."),
             ("To the fearless", "भी is fear itself; nothing says 'fearless'."),
             ("In battles", "भी means fear, not battle.")],
            "भीषु = in fears (loc. pl. of भी).",
            "-षु = locative plural."),
        mcq("apply", 4, "Why is अन्वितः printed अन्वितो before भवति in unit 20?",
            ("अः before a voiced consonant → ओ", "भ is a voiced consonant: अन्वितः + भवति → अन्वितो भवति."),
            [("अः before any consonant → ओ", "Not before every one: before त it becomes स्, before च श्."),
             ("ओ is an ending of the verb", "The ओ belongs to अन्वितः; भवति is unchanged."),
             ("अः before a voiceless भ → ओ", "भ is voiced, not voiceless; that is why ओ comes.")],
            "अन्वितः + भवति → अन्वितो भवति.",
            "अः + voiced consonant → ओ."),
        mcq("transfer", 5, "Built like आश्रितवत्सलः (affectionate to dependents), what does पुत्रवत्सलः mean in a new example?",
            ("Affectionate to his son", "X-वत्सल = affectionate to X: पुत्र-वत्सल, affectionate to the son."),
            [("The son of a loving man", "वत्सल is the head word: the man is affectionate, not a son."),
             ("One who has no son at all", "Nothing negative (अ-) is in the word."),
             ("A son who is much loved", "The word describes the loving one, not the son loved.")],
            "पुत्रवत्सलः = affectionate to his son, like आश्रितवत्सलः.",
            "X-वत्सल = affectionate to X.",
            teaches="In a tat-puruṣa X-वत्सल, the first member names those loved: आश्रित-वत्सल, affectionate to dependents."),
    ],
}

# ---------------------------------------------------------------- unit 21
AUTHORED["21"] = {
    "title": "घर्मद्वेषी स्वेदनः",
    "question": "By unit 21, what does the Pitta person hate, and what would he see asleep?",
    "rule": ("He hates heat and sweats; he has much stool, anger, drinking, eating and jealousy. Asleep he would see "
             "karṇikāra trees (probable identification), palāśa trees (Butea monosperma, standard), burning of the "
             "quarters, meteors, lightning, the sun and fires."),
    "limits": ("Typed prose, though the lines appear metrical (not asked; no metre aid). पूनिंगंधिः is read पूतिगन्धिः (foul-smelling) by conjecture: not asked. भूरि is taken over the whole list. कर्णिकार = Pterospermum acerifolium is probable; अर्क is taken as the sun (or Calotropis): not matched. सुप्तः पश्येत् is read as dreaming."),
    "explain_hi": ("ये पंक्तियाँ पित्त-वर्णन पूरा करती हैं। "
                   "वह घर्म (गरमी) से द्वेष करता है, पसीने वाला है; मल, क्रोध, पान, भोजन और ईर्ष्या उसे बहुत होते हैं; ‘दुर्गन्ध’ अनुमानित पाठ पर है। "
                   "सोया हुआ वह कर्णिकार (सम्भावित पहचान), पलाश (ढाक, मानक पहचान), दिशाओं का जलना, उल्का, बिजली, सूर्य और अग्नि देखे: डेटा इसे स्वप्न में देखना पढ़ता है। "
                   "‘अर्क’ को सूर्य माना गया, पर यह आक का पौधा भी हो सकता है। "
                   "‘अनलांश्च’ में अनलान् + च है: न् च से पहले ं + श् बनता है।"),
    "hook": "पित्त का स्वप्न: कर्णिकार, पलाश, जलती दिशाएँ, उल्का, बिजली, सूर्य, अग्नि।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 21, what does the Pitta person hate (द्वेषी)?",
            ("Heat", "घर्मद्वेषी: hating heat (घर्म)."),
            [("Cold", "Unit 21 says घर्म (heat); unit 18 even lists cold among what he desires."),
             ("Wind", "Unit 21 says घर्म (heat), not wind."),
             ("Rain", "Unit 21 says घर्म (heat), not rain.")],
            "घर्मद्वेषी = hater of heat.",
            "घर्म = heat; द्वेषी = hating."),
        order(1, "Put what he would see asleep in the order of unit 21.",
              ["पलाशान्", "दिग्दाह", "उल्का", "विद्युत्", "अर्क", "अनलान्"],
              "पलाशान् दिग्दाहोल्काविद्युदर्कानलांश्च: palāśa trees, burning of the quarters, meteors, lightning, the sun, fires.",
              "पलाश → दिग्दाह → उल्का → विद्युत् → अर्क → अनल."),
        match(2, "Match each word of unit 21 to its meaning.",
              [["उल्का", "meteor"], ["विद्युत्", "lightning"], ["अनल", "fire"],
               ["दिग्दाह", "burning of the quarters"], ["पलाश", "Butea monosperma (standard)"]],
              "उल्का = meteor; विद्युत् = lightning; अनल = fire; दिग्दाह = burning of the quarters; पलाश = Butea monosperma.",
              "उल्का, विद्युत्, अनल, दिग्दाह, पलाश.", role="extend",
              teaches="दिग्दाह, 'burning of the quarters', is a glow or fire seen on the horizon (data)."),
        mcq("discriminate", 3, "What does सुप्तः पश्येत् say in unit 21?",
            ("Asleep, he would see", "सुप्तः (asleep, nom. sg.) goes with the subject; पश्येत् = he would see."),
            [("Awake, he would see", "सुप्तः means asleep, not awake."),
             ("Having seen, he would sleep", "सुप्तः is asleep; पश्येत् is the verb 'would see'."),
             ("He would see sleepers", "'Sleepers' would be accusative सुप्तान्; सुप्तः is nominative.")],
            "सुप्तः पश्येत् = asleep, he would see (read as dreaming).",
            "सुप्तः (nom.) = the subject asleep."),
        mcq("apply", 4, "In अनलांश्च (unit 21), what has happened to अनलान् before च?",
            ("न् → ं + श् before च", "A final न् before च becomes anusvāra + श्: अनलान् + च → अनलांश्च."),
            [("न् is dropped before च", "The nasal is kept as anusvāra, and श् is added."),
             ("न् → म् before च", "No rule turns न् into म् here; it becomes ं + श्."),
             ("श् belongs to the word च", "The word is च; the श् comes from the final न्.")],
            "अनलान् + च → अनलांश्च.",
            "-न् + च → -ंश्च."),
        mcq("transfer", 5, "By the join अनलान् + च → अनलांश्च, how is वृक्षान् + च (and the trees) joined in a new example?",
            ("वृक्षांश्च", "A final न् before च becomes ं + श्: वृक्षांश्च."),
            [("वृक्षान्च", "न् does not stay unchanged before च."),
             ("वृक्षानश्च", "No vowel is added; न् becomes anusvāra."),
             ("वृक्षाच्च", "न् does not become च्; it becomes ं + श्.")],
            "वृक्षान् + च = वृक्षांश्च, like अनलान् + च = अनलांश्च.",
            "-न् + च → -ंश्च.",
            teaches="A final न् before च becomes anusvāra + श्: अनलान् + च → अनलांश्च, वृक्षान् + च → वृक्षांश्च."),
    ],
}

# ---------------------------------------------------------------- unit 22
AUTHORED["22"] = {
    "title": "कफप्रकृतिस्तु",
    "question": "By unit 22, what marks of body, temper and liking does one of Kapha constitution show?",
    "rule": ("One of Kapha constitution has the colour of dūrvā grass, indīvara or śara stalk; a full, handsome body; "
             "eyes with distinct white and dark; a voice like a lion, drum, cloud; endures hunger, thirst, heat; truthful, "
             "not greedy; likes pungent, hot, dry."),
    "limits": ('Prose, confidence low. Flagged readings सममुविभक्त, ससंधिबंधः, बन्होजो (read बहु-ओजः) and the unclear स्थिरशोष are not asked; दूर्वेदीवर is read दूर्वा-इन्दीवर. dūrvā = Cynodon dactylon (standard), indīvara = blue lotus (probable), śara = a reed (probable). उरु, घन, पेशल have two senses: not asked.'),
    "explain_hi": ("कफप्रकृति वाले का रंग दूर्वा (दूब, मानक पहचान), इन्दीवर (सम्भवतः नीला कमल) या शर (सम्भवतः सरकंडा) के डंठल में से किसी एक जैसा होता है। "
                   "उसका शरीर भरा हुआ और सुन्दर, ललाट, जाँघें (‘उरु’ = चौड़ी भी हो सकता है) और भुजाएँ बड़ी; आँखों में सफेद और काला स्पष्ट; स्वर सिंह, मृदंग और मेघ जैसा। "
                   "वह भूख, प्यास और गरमी सह लेता है; शत्रुता दृढ़ और छिपी; सत्यवादी, स्मृतिमान्, धृतिमान्, लोभ रहित; बचपन में भी नहीं रोता। "
                   "कई छपे रूप संदिग्ध हैं (सममुविभक्त, ससंधिबंधः, बन्होजो, स्थिरशोष), इन पर प्रश्न नहीं। "
                   "कटु (तीखा), कड़वा, कसैला, गरम और रूखा उसे चाहिए और अनुकूल है; ‘सितासित’ में सित + असित (अ + अ → आ) है।"),
    "hook": "कफ: भरा शरीर, सिंह-सा स्वर, बचपन में भी न रोए।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 22, what does the Kapha person endure (सहिष्णु)?",
            ("Hunger, thirst and heat", "क्षुत्पिपासोष्णसहिष्णुः: enduring hunger, thirst and heat."),
            [("Cold, wind and grief", "Unit 22 names hunger, thirst and heat."),
             ("Pain, fear and anger", "Unit 22 names hunger, thirst and heat."),
             ("Noise, toil and grief", "Unit 22 names hunger, thirst and heat.")],
            "क्षुत्-पिपासा-उष्ण-सहिष्णुः.",
            "सहिष्णु = enduring."),
        order(1, "Put these printed parts of unit 22 in the line's order.",
              ["परिपूर्णचारुगात्रो", "सिंहमृदंगघनघोषः", "दृढप्रच्छन्नवैरः", "पेशलः", "सत्यवादी", "स्मृतिमान्धृतिमानलोलुपो"],
              "Full handsome body; voice like lion, drum, cloud; firm hidden enmity; gentle; truthful; memory, steadiness, not greedy.",
              "परिपूर्ण... → सिंह... → दृढ... → पेशलः → सत्यवादी → स्मृतिमान्..."),
        match(2, "Match each word of unit 22 to its meaning.",
              [["सत्यवादी", "truthful"], ["स्मृतिमान्", "possessing memory"], ["अलोलुपः", "not greedy"],
               ["प्रच्छन्न", "hidden"], ["सिंह", "lion"]],
              "सत्यवादी = truthful; स्मृतिमान् = with memory; अलोलुपः = not greedy; प्रच्छन्न = hidden; सिंह = lion.",
              "सत्यवादी, स्मृतिमान्, अलोलुपः, प्रच्छन्न, सिंह.", role="extend",
              teaches="-मान् / -वान् makes 'possessing': स्मृतिमान् (with memory), धृतिमान् (with steadiness)."),
        mcq("discriminate", 3, "Which split of सितासित (white and dark) in unit 22 is right?",
            ("सित + असित", "अ + अ → आ: सित (white) + असित (not white, dark) → सितासित."),
            [("सित + सित", "That would be सितसित, with no आ; and both would mean white."),
             ("सितः + असित", "अः before अ would give ओऽ: सितोऽसित."),
             ("सिते + असित", "ए before अ would give एऽ: सितेऽसित.")],
            "सित (white) + असित (dark).",
            "अ + अ → आ."),
        mcq("apply", 4, "What does printed बाल्येप्यरोदनः (unit 22) say of the Kapha person?",
            ("Even in childhood not crying", "बाल्ये (in childhood) + अपि (even) + अरोदनः (not crying)."),
            [("Crying much in his childhood", "अ-रोदन is 'not crying'; the अ- negates."),
             ("Even in old age not crying", "बाल्ये is childhood, not old age."),
             ("Crying only in his childhood", "अ-रोदन negates crying; no 'only' (एव) is printed.")],
            "बाल्ये अपि अरोदनः = not crying even in childhood.",
            "अ- before a word negates it."),
        mcq("transfer", 5, "By the join in प्रच्छन्न (प्र + छन्न), how is वि + छेद joined in a new example?",
            ("विच्छेद", "After a short vowel, छ is written च्छ: वि + छेद → विच्छेद."),
            [("विछेद", "After the short इ, छ takes च् before it: च्छ."),
             ("विश्छेद", "No श् arises; after a short vowel छ becomes च्छ."),
             ("वीछेद", "The इ is not lengthened; च् is added before छ.")],
            "वि + छेद = विच्छेद, like प्र + छन्न = प्रच्छन्न.",
            "Short vowel + छ → च्छ.",
            teaches="After a short vowel, a following छ is doubled as च्छ: प्र + छन्न → प्रच्छन्न (hidden), वि + छेद → विच्छेद."),
    ],
}

# ---------------------------------------------------------------- unit 23
AUTHORED["23"] = {
    "title": "अपिच",
    "question": "How is the link अपिच of unit 23 built, and what does it do?",
    "rule": "अपि + च, two indeclinables: 'and further'. It opens the lines of the next units (data).",
    "limits": "Prose, one printed word, no verb. Questions ask only about the words and the join.",
    "explain_hi": ("तीसरी बार यही जोड़ने वाला शब्द आता है: ‘अपि च’ यानी और भी। "
                   "यह एक ही छपा शब्द है, इसमें कोई क्रिया नहीं; अपि और च दोनों अव्यय हैं। "
                   "डेटा के अनुसार यह आगे की पंक्तियों का आरम्भ कराता है। "
                   "स्वर आ से पहले अपि का इ य् बनता है: अपि + आगतः → अप्यागतः।"),
    "hook": "अपि च: तीसरी बार, आगे और।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 23, which two words make up अपिच?",
            ("अपि and च", "अपि (also) and च (and), printed without a space."),
            [("अपि and इच", "इच is no word; the second word is च."),
             ("अप and इच", "Neither अप nor इच is the word here; it is अपि + च."),
             ("अ and पिच", "पिच is no word; the first word is अपि.")],
            "अपिच = अपि + च.",
            "अपि + च."),
        match(1, "Match each part of unit 23 to its meaning.",
              [["अपि", "also, too"], ["च", "and"], ["अपि च", "and further"]],
              "अपि = also; च = and; अपि च = and further.",
              "अपि, च, अपि च."),
        T(multi("extend", 2, "Which statements fit unit 23?",
              [("It has a verb", "No verb is printed; it is a link word."),
               ("It is printed as one word, अपिच", "Right: अपि and च stand without a space."),
               ("It names a constitution", "No prakṛti is named in unit 23."),
               ("Both parts are indeclinables", "Right: अपि and च take no endings.")],
              [1, 3],
              "अपिच: one printed word, two indeclinables, no verb.",
              "अपि, च = avyaya."),
          "Indeclinables (अव्यय) such as अपि and च take no case or verb endings."),
        mcq("discriminate", 3, "By the data, what does the link अपिच in unit 23 do?",
            ("Opens the lines that follow", "The data: it introduces the lines of the next units."),
            [("Ends the Kapha description", "It opens what follows; it ends nothing."),
             ("Names a new constitution", "No prakṛti is named in unit 23."),
             ("Gives a reason for the above", "A reason would need हि or यतः; अपि च adds.")],
            "अपिच opens the following lines (data).",
            "अपि च = and further: it adds."),
        mcq("apply", 4, "Before च in unit 23, what does the final इ of अपि do?",
            ("It stays unchanged", "च is a consonant, so no vowel sandhi: अपि च."),
            [("It becomes य्", "इ → य् only before a different vowel, not before च."),
             ("It becomes ए", "इ does not become ए before a consonant."),
             ("It becomes ई", "इ joins into ई only with a following इ or ई.")],
            "अपि + च: no change.",
            "Final vowel + consonant: no change."),
        mcq("transfer", 5, "How is अपि + आगतः (has come too) joined in a new example?",
            ("अप्यागतः", "इ before a different vowel becomes य्: अपि + आगतः → अप्यागतः."),
            [("अपागतः", "The इ is not dropped; it becomes य्."),
             ("अपेगतः", "ए comes from अ + इ, not from इ + आ."),
             ("अपीगतः", "ई comes from इ + इ, not from इ + आ.")],
            "अपि + आगतः = अप्यागतः.",
            "इ + a different vowel → य् + that vowel.",
            teaches="A final इ before आ becomes य्: अपि + आगतः → अप्यागतः; before a consonant it stays (अपि च)."),
    ],
}

# ---------------------------------------------------------------- unit 24
AUTHORED["24"] = {
    "title": "अल्पव्याहारक्रोधमेधाशनेहः",
    "question": "By unit 24, what is little and what is abundant in the Kapha person, and what is his temper?",
    "rule": ("He has little speech, anger, intellect (medhā), eating and effort, but abundant life and wealth; he is "
             "far-seeing, generous, faithful, deep, forbearing, noble, prone to sleep, slow to act and grateful."),
    "limits": ("Typed prose, though the lines appear metrical (not asked; no metre aid). Continues the Kapha description. The अल्प compound is read as printed; मेधा is odd here (मेह is conceivable) and ईह is effort or desire: neither is asked. स्थूललक्ष is not firm: not asked."),
    "explain_hi": ("ये पंक्तियाँ कफ-वर्णन को आगे बढ़ाती हैं; इकाई २२ की क्रिया यहाँ दोहराई नहीं गई। "
                   "उसकी वाणी, क्रोध, मेधा, भोजन और ईहा (चेष्टा या इच्छा) थोड़े, पर आयु और धन बहुत (प्राज्य) होते हैं। "
                   "वह दूरदर्शी, उदार, श्रद्धालु, गम्भीर, क्षमावान्, आर्य, निद्रालु, दीर्घसूत्री (देर से काम करने वाला) और कृतज्ञ है। "
                   "‘मेधा’ इस सूची में अटपटा है (मेह भी सम्भव) और ‘स्थूललक्ष’ का अर्थ पक्का नहीं, इसलिए इन पर प्रश्न नहीं। "
                   "‘प्राज्यायुर्वित्तो’ में आयुस् का स् घोष व्यंजन व से पहले र् बना है।"),
    "hook": "कफ: बोले कम, जिए ज़्यादा; धीमा पर कृतज्ञ।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 24, what is abundant (प्राज्य) for the Kapha person?",
            ("Life and wealth", "प्राज्यायुर्वित्तः: abundant life (आयुः) and wealth (वित्त)."),
            [("Speech and anger", "These are in the अल्प (little) list."),
             ("Eating and speech", "These are in the अल्प (little) list."),
             ("Anger and eating", "These are in the अल्प (little) list.")],
            "प्राज्य-आयुस्-वित्तः: abundant life and wealth.",
            "प्राज्य = abundant."),
        order(1, "Put these printed words of unit 24 in order.",
              ["दीर्घदर्शी", "वदान्यः", "गंभीरः", "क्षमावानार्यो", "निद्रालुर्दीर्घसूत्री", "कृतज्ञः"],
              "Far-seeing; generous; deep; forbearing, noble; prone to sleep, slow to act; grateful.",
              "दीर्घदर्शी → वदान्यः → गंभीरः → क्षमावानार्यो → निद्रालुर्दीर्घसूत्री → कृतज्ञः."),
        match(2, "Match each word of unit 24 to its meaning.",
              [["वदान्य", "generous"], ["दीर्घदर्शी", "far-seeing"], ["कृतज्ञ", "grateful"],
               ["निद्रालु", "prone to sleep"], ["क्षमावान्", "forbearing"]],
              "वदान्य = generous; दीर्घदर्शी = far-seeing; कृतज्ञ = grateful; निद्रालु = prone to sleep; क्षमावान् = forbearing.",
              "वदान्य, दीर्घदर्शी, कृतज्ञ, निद्रालु, क्षमावान्.", role="extend",
              teaches="कृत-ज्ञ, 'knowing what was done (for him)', is the word for grateful."),
        mcq("discriminate", 3, "What does दीर्घसूत्री mean in unit 24?",
            ("Slow to act", "दीर्घ-सूत्री, lit. 'long-threaded': slow, dilatory."),
            [("Far-seeing", "Far-seeing is दीर्घदर्शी, a different word."),
             ("Long-lived", "Long life is प्राज्य आयुः; दीर्घसूत्री is slow to act."),
             ("Tall and thin", "दीर्घसूत्री speaks of acting, not of the body.")],
            "दीर्घसूत्री = slow to act.",
            "दीर्घ-सूत्री = long-threaded = dilatory."),
        mcq("apply", 4, "In प्राज्यायुर्वित्तो (unit 24), why does आयुस् show र् before वित्त?",
            ("स् after उ, before voiced व → र्", "A final स् after उ becomes र् before a voiced sound: आयुस् + वित्त → आयुर्वित्त."),
            [("स् after उ always → ओ", "ओ arises only from अस्/अः; after उ it is र्."),
             ("र् is the first sound of वित्त", "वित्त begins with व; the र् comes from स्."),
             ("स् → र् before any consonant", "Before a voiceless one like त it does not become र्.")],
            "आयुस् + वित्त → आयुर्वित्त.",
            "उस् + voiced sound → उर्."),
        mcq("transfer", 5, "By the join आयुस् + वित्त → आयुर्वित्त, how is धनुस् + वेदः joined in a new example?",
            ("धनुर्वेदः", "स् after उ before the voiced व becomes र्: धनुर्वेदः."),
            [("धनुवेदः", "The स् does not vanish; it becomes र्."),
             ("धनोवेदः", "ओ comes from अस्, not from उस्."),
             ("धनुस्वेदः", "स् does not stay before the voiced व.")],
            "धनुस् + वेदः = धनुर्वेदः, like आयुस् + वित्त = आयुर्वित्त.",
            "उस् + voiced sound → उर्.",
            teaches="A final स् after उ (or इ) becomes र् before a voiced sound: आयुस् + वित्त → आयुर्वित्त, धनुस् + वेदः → धनुर्वेदः."),
    ],
}

# ---------------------------------------------------------------- unit 25
AUTHORED["25"] = {
    "title": "ऋजुर्विपश्चित्सुभगः",
    "question": "By unit 25, what is the Kapha person's character, and what does he see in a dream?",
    "rule": ("He is upright, learned, fortunate, modest, devoted to his elders, firm in friendship. In a dream he sees "
             "water-reservoirs with lotuses and rows of birds, and clouds (तोयद, water-giver)."),
    "limits": ("Typed prose, though the lines appear metrical (not asked). Continues the Kapha description. गुरु "
               "is elder or teacher (a plural of respect). पद्म = lotus, Nelumbo nucifera (standard). सपद्म and "
               "सविहङ्गमाल are taken with तोयाशय."),
    "explain_hi": ("ये पंक्तियाँ कफ-वर्णन पूरा करती हैं। "
                   "वह सीधा (ऋजु), विद्वान (विपश्चित्), सौभाग्यशाली, लज्जावान्, गुरुओं (बड़ों या आचार्यों) का भक्त और दृढ़ मित्रता वाला है। "
                   "स्वप्न में वह कमलों वाले और पक्षियों की पंक्तियों वाले जलाशयों को और बादलों को देखता है। "
                   "तोयद = जल देने वाला, यानी बादल; पद्म = कमल (मानक पहचान)। "
                   "‘सविहंगमालांस्तोयाशयान्’ में -आन् + त → -आंस्त, और ‘तोयदांश्च’ में -आन् + च → -आंश्च हुआ है।"),
    "hook": "कफ का स्वप्न: कमल-भरे जलाशय, पक्षी-पंक्तियाँ, बादल।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 25, what does the Kapha person see in a dream?",
            ("Ponds, birds and clouds", "सपद्मान् सविहङ्गमालान् तोयाशयान् ... तोयदान्: ponds with lotuses and rows of birds, and clouds."),
            [("Meteors, lightning and fire", "Unit 25 names water-reservoirs, birds and clouds."),
             ("Dry rivers and mountain peaks", "Unit 25 names water-reservoirs, birds and clouds."),
             ("Burning skies and the sun", "Unit 25 names water-reservoirs, birds and clouds.")],
            "स्वप्ने ... तोयाशयान् पश्यति तोयदांश्च.",
            "तोयाशय = water-reservoir; तोयद = cloud."),
        order(1, "Put these words of unit 25 in the line's order.",
              ["ऋजुः", "विपश्चित्", "सुभगः", "सलज्जो", "भक्तो गुरूणां", "दृढसौहृदश्च"],
              "Upright; learned; fortunate; modest; devoted to elders; firm in friendship.",
              "ऋजुः → विपश्चित् → सुभगः → सलज्जो → भक्तो गुरूणां → दृढसौहृदश्च."),
        match(2, "Match each word of unit 25 to its meaning.",
              [["ऋजु", "upright"], ["विपश्चित्", "learned"], ["सलज्ज", "modest"], ["तोयाशय", "water-reservoir"],
               ["तोयद", "cloud"]],
              "ऋजु = upright; विपश्चित् = learned; सलज्ज = modest; तोयाशय = water-reservoir; तोयद = cloud.",
              "ऋजु, विपश्चित्, सलज्ज, तोयाशय, तोयद.", role="extend",
              teaches="तोय-द, 'water-giver', is a cloud; तोय-आशय, 'water-receptacle', is a pond or lake."),
        mcq("discriminate", 3, "In unit 25, which word names the clouds?",
            ("तोयदान्", "तोय-द, water-giver: clouds."),
            [("तोयाशयान्", "तोय-आशय is a water-receptacle: ponds, lakes."),
             ("विहङ्गमालान्", "विहङ्ग-माला is rows of birds."),
             ("सपद्मान्", "स-पद्म is 'with lotuses', describing the ponds.")],
            "तोयदान् = clouds.",
            "-द = giving; तोयद = water-giver."),
        mcq("apply", 4, "In सविहंगमालांस्तोयाशयान् (unit 25), what has happened to -मालान् before तोय?",
            ("न् → ं + स् before त", "A final न् before त becomes anusvāra + स्: -मालान् + तोय → -मालांस्तोय."),
            [("न् → ं + स् before any consonant", "Not before every one: before च it is ं + श् (तोयदांश्च)."),
             ("स् is the first sound of तोय", "तोय begins with त; the स् comes from the final न्."),
             ("न् is dropped and स् is a plural ending", "The nasal stays as anusvāra; the ending is -आन्.")],
            "-मालान् + तोयाशयान् → -मालांस्तोयाशयान्.",
            "-न् + त → -ंस्त."),
        mcq("transfer", 5, "Built like तोयद (water-giver, cloud), what does अन्नदः mean in a new example?",
            ("A giver of food", "X-द = giver of X: अन्न-द, giver of food."),
            [("An eater of food", "Eating is -भुज् / -अद; -द is 'giving'."),
             ("One without food", "Nothing negative (अ-, निर्-) is in the word."),
             ("A store of food", "A store would be -आशय or -कोश; -द is 'giving'.")],
            "अन्नदः = giver of food, like तोयदः = giver of water.",
            "X-द = giver of X.",
            teaches="-द (from √दा, give) at the end of a compound means 'giver of': तोय-द, water-giver, i.e. cloud."),
    ],
}


NOTES_HI = {
    "13": ("पंक्ति बहुत क्षतिग्रस्त है, विश्वसनीयता कम। तीन छपे पद अस्पष्ट हैं: ‘असात्’ (अनुमान: असात्म्यात्), "
           "‘स्वप्नमाणवृद्धिक्षययोगात्’ (अनुमान: स्वमान/स्वप्रमाण) और ‘प्राकृतिकल्य’ (अनुमान: प्राकृतिकल्प); कोई अनुमान अपनाया नहीं गया। "
           "‘आधारः’ का आधेय नहीं बताया गया; ‘रसात्मकस्यौजसः क्षयवृद्धिभाजः’ को एक वाक्यांश पढ़ा गया, अनुवाद ढीला है। "
           "जाँची सन्धियाँ: वैकृताः + तु → वैकृतास्तु (त से पहले विसर्ग → स्); प्राकृतेषु + एव → प्राकृतेष्वेव; तद्वत् + ओजः → तद्वदोजः; "
           "ओजः + अपि → ओजोऽपि (अः + अ → ओऽ); रसात्मकस्य + ओजसः → रसात्मकस्यौजसः (अ + ओ → औ)।"),
    "14": ("दो छपे रूप चिह्नित: ‘शीतद्विदुद्वद्ध’ को शीतद्विट् + उद्बद्ध पढ़ा गया (सन्धि से ड अपेक्षित है पर द छपा है, और व का ब; यह सम्भावित पठन है, पक्का नहीं); "
           "‘मधुराम्स’ को मधुर-अम्ल पढ़ा गया (म्स, म्ल की छपाई-भूल)। "
           "जाँची सन्धियाँ: अनुरोधात् + वात → अनुरोधाद्वात (घोष से पहले त् → द्); प्रकृतिः + तनुः → प्रकृतिस्तनुः; तनुः + रूक्षः → तनू रूक्षः "
           "(उ के बाद विसर्ग र्, र से पहले लुप्त, उ दीर्घ); स्तेनः + अनार्यः → स्तेनोऽनार्यः; अनार्यः + मत्सरी → अनार्यो मत्सरी; "
           "मत्सरी + अजितेन्द्रियः → मत्सर्यजितेन्द्रियः; गान्धर्व + इतिहास → गान्धर्वेतिहास (अ + इ → ए)। ‘स्तेन’ संज्ञा है: चोर।"),
    "15": "एक शब्द ‘अपिच’ = अपि + च, बिना अन्तर के छपा। कोई सन्धि-परिवर्तन नहीं (व्यंजन से पहले इ नहीं बदलता)। कोई पाठ-भेद नहीं।",
    "16": ("[02.08.17] क्षाम को वाच् के साथ (कृश वाणी) पढ़ा गया; यह पूरे व्यक्ति का विशेषण भी हो सकता है, विभाग पक्का नहीं। "
           "धमनी = सम्भवतः दिखने वाली नसें (सम्भावित)। ‘धमनि’ का ह्रस्व इ छन्द या छपाई का है। वाच् + धमनि → वाग्धमनि। "
           "[02.08.18] दुर्भगः + अति → दुर्भगोऽति (अः + अ → ओऽ)। दुर्भग = भाग्यहीन (दूसरों को अप्रिय भी सम्भव)। "
           "‘स्फुटित’ केशों पर भी उतना ही लागू है या नहीं, यह स्पष्ट नहीं; समास छपे रूप में एक है।"),
    "17": ("[02.08.19] कठिन और आंशिक क्षतिग्रस्त, विश्वसनीयता कम। ‘क्थति’ अपठनीय है (अनुमान: कूथति, कराहता है; केवल चिह्नित)। "
           "‘सुस्रस्तस्तन्यते’ = सुस्रस्तः + स्तन्यते पढ़ा गया; ‘स्तन्यते’ √स्तन् का अनियमित रूप है, पक्का नहीं। मुख वाले समास का विभाग पक्का नहीं। "
           "किञ्चित् + उन्मिषित → किञ्चिदुन्मिषित (स्वर से पहले त् → द्)। "
           "[02.08.20] कर्ता ‘वह’ समझा गया। इस इकाई में नींद या स्वप्न का शब्द नहीं; डेटा कोई नहीं जोड़ता।"),
    "18": ("छपा ‘सृत्पिपासो’ अनुमान से क्षुत्-पिपासः पढ़ा गया (इकाई २२ के क्षुत्पिपासा जैसा); ‘पिट्कु’ = पिटक (छपाई में उ)। चिह्नित। "
           "छपा ‘स्वादुतित्त’ = स्वादु-तिक्त पढ़ा गया। करभ = ऊँट या हाथी का बच्चा, तुलना पक्की नहीं। "
           "जाँची सन्धियाँ: पित्तप्रकृतिः + उष्ण → पित्तप्रकृतिरुष्ण (इ के बाद विसर्ग + स्वर → र्); -गात्रः + ताम्र → -गात्रस्ताम्र; "
           "शूरः + अभिमानी → शूरोऽभिमानी; अपत्यः + शूरः → अपत्यः शूरः (श से पहले विसर्ग बना रहा, जो मान्य है)।"),
    "19": "एक शब्द ‘अपिच’ = अपि + च। अपि और च अव्यय हैं; व्यंजन से पहले इ नहीं बदलता। कोई पाठ-भेद नहीं।",
    "20": ("[02.08.23] ‘दयित’ तीनों (माल्य, विलेपन, मण्डन) के साथ लिया गया (छपा एक समास)। शुचिः + आश्रित → शुचिराश्रित (इ के बाद विसर्ग + स्वर → र्)। "
           "[02.08.24] छपा ‘वलान्वितो’ में व, पढ़ा बल; ‘दिंपताम्’ को दिक्पताम् पढ़ा गया। अन्वितः + भवति → अन्वितो भवति; "
           "गतिः + दिक्पताम् → गतिर्दिक्पताम्। ‘दिक्पतियों के लिए’ या ‘के’, सम्बन्ध पक्का नहीं।"),
    "21": ("[02.08.25] छपा ‘पूनिंगंधिर्’ अनुमान से पूतिगन्धिः पढ़ा गया (चिह्नित)। पूतिगन्धिः + भूरि → -गन्धिर्भूरि; भूरि + उच्चार → भूर्युच्चार (इ + उ → यु); "
           "पान + अशन → पानाशन; अशन + ईर्ष्य → अशनेर्ष्य (अ + ई → ए)। "
           "[02.08.26] छपा ‘सुप्तःपश्येत्कर्णिकारान्’ एक साथ जुड़ा है। दिक् + दाह → दिग्दाह; दाह + उल्का → दाहोल्का; विद्युत् + अर्क → विद्युदर्क; "
           "अनलान् + च → अनलांश्च। कर्णिकार = Pterospermum acerifolium (सम्भावित; Cassia fistula भी प्रस्तावित); पलाश = Butea monosperma (मानक); "
           "अर्क = सूर्य माना (आक भी सम्भव)।"),
    "22": ("विश्वसनीयता कम। चिह्नित: ‘सममुविभक्त’ (पढ़ा सम-सुविभक्त), ‘ससंधिबंधः’ (पढ़ा सुसन्धिबन्धः), ‘बन्होजो’ (पढ़ा बहु-ओजः, अनुमानित); "
           "‘स्थिरशोष’ अस्पष्ट। छपा ‘दूर्वेदीवर’ को दूर्वा-इन्दीवर पढ़ा गया; ‘कटुतित्त’ = कटु-तिक्त। "
           "जाँची सन्धियाँ: कफप्रकृतिः + तु → कफप्रकृतिस्तु; सित + असित → सितासित; ललाट + उरु/ऊरु → ललाटोरु (अ + उ/ऊ → ओ; अर्थ जाँघ या चौड़ा, पक्का नहीं); "
           "सहिष्णुः + (छपा) बन्हो... → सहिष्णुर्बन्हो... (उ के बाद विसर्ग, घोष से पहले र्); बाल्ये + अपि → बाल्येऽपि (छपे में ऽ नहीं); प्र + छन्न → प्रच्छन्न। "
           "पहचान: दूर्वा = Cynodon dactylon (मानक), इन्दीवर = नीला कमल, Nymphaea (सम्भावित), शर = Saccharum वर्ग का सरकंडा (सम्भावित)।"),
    "23": "एक शब्द ‘अपिच’ = अपि + च; अगली पंक्तियों का आरम्भ। कोई सन्धि-परिवर्तन नहीं, कोई पाठ-भेद नहीं।",
    "24": ("[02.08.29] ‘अल्प’ पाँचों पर लागू पढ़ा गया; ‘मेधा’ यहाँ अटपटा है (मेह सम्भव) और ‘ईह’ चेष्टा या इच्छा, समास पक्का नहीं। "
           "अशन + ईह → अशनेह; प्राज्य + आयुस् → प्राज्यायुस्; आयुस् + वित्त → आयुर्वित्त; वित्तः + दीर्घ → वित्तो दीर्घ। "
           "[02.08.30] श्राद्धः + गम्भीरः → श्राद्धो गम्भीरः; क्षमावान् + आर्यः → क्षमावानार्यः; आर्यः + निद्रालुः → आर्यो निद्रालुः; "
           "निद्रालुः + दीर्घ → निद्रालुर्दीर्घ। ‘स्थूललक्ष’ का अर्थ पक्का नहीं (बड़े लक्ष्य वाला / उदार)।"),
    "25": ("[02.08.31] ऋजुः + विपश्चित् → ऋजुर्विपश्चित्; सलज्जः + भक्तः → सलज्जो भक्तः; भक्तः + गुरूणाम् → भक्तो गुरूणाम्; गुरु = बड़े या आचार्य (आदरार्थ बहुवचन)। "
           "[02.08.32] सविहङ्गमालान् + तोयाशयान् → सविहंगमालांस्तोयाशयान् (न् + त → ंस्त); तोयदान् + च → तोयदांश्च (न् + च → ंश्च)। "
           "पद्म = कमल, Nelumbo nucifera (मानक)। कोई पाठ-भेद नहीं।"),
}


AIDS = {
    "13": {
        "chain": {"steps": ["गर्भ से निकले के आहारों से", "वैकृत उत्पन्न होते", "प्राकृतों पर ही जमते",
                            "काल आदि के वश से", "शरीर का अनुग्रह भी, दूषण भी"]},
        "chunks": "वैकृतास्तु | गर्भादभिनिःसृतस्याहारैरसात्संभवंतः | प्राकृतेष्वेव रोहंति | ते कालादिवशेन | स्वप्नमाणवृद्धिक्षययोगाद्देहमनुगृह्णंति | दूषयंति च | तद्वदोजोऽपि परं | हृदयस्थमष्टबिंदुप्रमाणमाधारः | प्राकृतिकल्य | रसात्मकस्यौजसः क्षयवृद्धिभाजः",
        "sandhi": "उ + ए → वे: प्राकृतेषु + एव → प्राकृतेष्वेव · स्वर से पहले त् → द्: तद्वत् + ओजः → तद्वदोजः · अः + अ → ओऽ: ओजः + अपि → ओजोऽपि।",
        "anchors": "पक्का भाग: वैकृत प्राकृत पर जमते; ओज हृदय में, आठ बूँद। अस्पष्ट: असात्, स्वप्नमाण..., प्राकृतिकल्य। (मेरी याद-पद्धति)",
    },
    "14": {
        "diagram": {"groups": [
            {"label": "शरीर", "items": ["तनु, रूक्ष", "अंग-दाँत-नख-रोम-नेत्र-स्वर पतले, कम", "सशब्द सन्धि"]},
            {"label": "मन और स्वभाव", "items": ["शीघ्र आरम्भ, क्षोभ, ग्रहण, विस्मरण", "धृति-मति-गति-दृष्टि-स्वभाव-सौहार्द चंचल",
                                              "स्तेन, अनार्य, मत्सरी, अजितेन्द्रिय"]},
            {"label": "प्रिय", "items": ["गान्धर्व (संगीत, सम्भावित)", "इतिहास, हास, विलास", "कलह, मृगया, उद्यान, यात्रा"]},
            {"label": "इच्छा और उपशय", "items": ["स्निग्ध, उष्ण, मधुर", "अम्ल (अनुमानित पाठ)", "लवण"]}]},
        "sandhi": ("उ के बाद विसर्ग र्, र से पहले लुप्त, उ दीर्घ: तनुः + रूक्षः → तनू रूक्षः · अः + अ → ओऽ: स्तेनः + अनार्यः → स्तेनोऽनार्यः · "
                   "ई + अ → य: मत्सरी + अजित → मत्सर्यजित।"),
        "frame": "किसके अनुसार: स्वदोषगुणानुरोधात् → कौन: वातप्रकृतिः → कैसा: शरीर, मन, प्रिय, इच्छा → क्रिया: भवति।",
        "pegs": "‘वात = हवा’: हवा जैसी चंचल, सूखी, जल्दी आने-जाने वाली। (मेरा बनाया चित्र, पाठ का कथन नहीं)",
    },
    "15": {
        "chunks": "अपि | च",
        "frame": "अपि (भी) + च (और) = और भी: आगे की बात खोलने वाला।",
        "sandhi": "व्यंजन से पहले इ नहीं बदलता: अपि + च → अपि च · भिन्न स्वर से पहले इ → य्: अपि + उक्तम् → अप्युक्तम्।",
    },
    "16": {
        "chunks": "अल्पवित्तबलजीवितनिद्रः | क्षामवाग्धमनिसंततगात्रः | दुर्भगोऽतिबहुभुक् | बहुभाषी | नास्तिकः | स्फुटितकेशकरांघ्रिः",
        "seesaw": "अल्प (थोड़ा): धन, बल, जीवन, नींद ↔ बहु (बहुत): अतिबहुभुक् (खाना), बहुभाषी (बोलना)।",
        "sandhi": "च् पदान्त में क्, घोष से पहले ग्: वाच् + धमनि → वाग्धमनि · अः + अ → ओऽ: दुर्भगः + अति → दुर्भगोऽति।",
    },
    "17": {
        "chain": {"steps": ["शुष्क-रूक्ष-विषम नदियों में", "आकाश में", "पर्वत-शिखरों पर", "याति: जाता है"]},
        "chunks": "किंचिदुन्मिषितदृङ्मुखसुस्रस्तस्तन्यते | क्थति | खादति दंतान् | शुष्करूक्षविषमासु सरित्सु | व्योम्नि | शैलशिखरेषु च याति",
        "anchors": "पक्का: दाँत चबाना; नदी, आकाश, शिखर। अस्पष्ट: क्थति, स्तन्यते। नींद या स्वप्न का शब्द नहीं। (मेरी याद-पद्धति)",
    },
    "18": {
        "diagram": {"groups": [
            {"label": "शरीर", "items": ["उष्ण, गौर गात्र", "ताम्र नख-नयन-जिह्वा-ओष्ठ-पाणितल-पादतल", "शिथिल सन्धिबन्ध, मांस",
                                     "कपिल, विरल, मृदु केश-रोम"]},
            {"label": "बल और आयु", "items": ["मध्य बल, आयु", "अल्प शुक्र, व्यवाय, अपत्य"]},
            {"label": "स्वभाव और शीघ्र विकार", "items": ["शूर, अभिमानी", "वली, खलित, पलित (शीघ्र)", "पिट्कु (पढ़ा पिटक), व्यङ्ग (शीघ्र)", "क्षुत्-पिपासा (अनुमानित पाठ)", "मेधावी, दुर्भग"]},
            {"label": "इच्छा और उपशय", "items": ["स्वादु, तित्त (पढ़ा तिक्त), कषाय, शीत"]}]},
        "sandhi": "इ के बाद विसर्ग + स्वर → र्: पित्तप्रकृतिः + उष्ण → पित्तप्रकृतिरुष्ण · अः + अ → ओऽ: शूरः + अभिमानी → शूरोऽभिमानी।",
        "frame": "कौन: पित्तप्रकृतिः → शरीर → बल-आयु → स्वभाव → शीघ्र विकार → इच्छा → क्रिया: भवति।",
        "pegs": "पित्त को ‘ताँबा’ से याद रखें: ताम्र नख-नेत्र, उष्ण गात्र। (मेरी याद-पद्धति, पाठ का कथन नहीं)",
    },
    "19": {
        "chunks": "अपि | च",
        "frame": "अपि = भी; च = और; अपि च = और भी।",
        "sandhi": "भिन्न स्वर से पहले इ → य्: अपि + एवम् → अप्येवम्; व्यंजन से पहले कोई परिवर्तन नहीं: अपि च।",
    },
    "20": {
        "chunks": "दयितमाल्यविलेपनमंडनः | सुचरितः | शुचिराश्रितवत्सलः | विभवसाहसबुद्धिवलान्वितो | भवति | भीषु गतिर्दिंपतामपि",
        "frame": "क्या प्रिय: माला, लेप, मण्डन → आचरण: सुचरित, शुचि, आश्रितवत्सल → युक्त: विभव, साहस, बुद्धि, बल → भय में: दिक्पतियों का भी आश्रय।",
        "sandhi": "इ के बाद विसर्ग + स्वर → र्: शुचिः + आश्रित → शुचिराश्रित · अः + घोष व्यंजन → ओ: अन्वितः + भवति → अन्वितो भवति।",
    },
    "21": {
        "chain": {"steps": ["सुप्तः पश्येत्: सोया हुआ देखे", "कर्णिकार (सम्भावित पहचान)", "पलाश (ढाक, मानक)", "दिग्दाह",
                            "उल्का", "विद्युत्", "अर्क (सूर्य माना)", "अनल (अग्नि)"]},
        "chunks": "घर्मद्वेषी | स्वेदनः | पूनिंगंधिर्भूर्युच्चारक्रोधपानाशनेर्ष्यः | सुप्तःपश्येत्कर्णिकारान् | पलाशान् | दिग्दाहोल्काविद्युदर्कानलांश्च",
        "sandhi": ("न् + च → ंश्च: अनलान् + च → अनलांश्च · स्वर से पहले त् → द्: विद्युत् + अर्क → विद्युदर्क · इ + उ → यु: भूरि + उच्चार → भूर्युच्चार।"),
        "pegs": "पित्त के स्वप्न को ‘आग और रोशनी’ से याद रखें: जलती दिशाएँ, उल्का, बिजली, सूर्य, अग्नि। (मेरी याद-पद्धति, पाठ का कथन नहीं)",
    },
    "22": {
        "diagram": {"groups": [
            {"label": "वर्ण", "items": ["दूर्वेदीवर (पढ़ा दूर्वा (मानक), इन्दीवर (सम्भावित)), शरकाण्ड (सम्भावित): कोई एक"]},
            {"label": "शरीर", "items": ["परिपूर्ण, चारु गात्र", "महा ललाट, उरु (जाँघ या चौड़ा), बाहु", "व्यक्त सित-असित नेत्र",
                                     "सिंह-मृदंग-घन जैसा घोष"]},
            {"label": "सहन और स्वभाव", "items": ["सहे: क्षुत्, पिपासा, उष्ण", "दृढ, प्रच्छन्न वैर", "पेशल, सत्यवादी", "स्मृतिमान्, धृतिमान्, अलोलुप",
                                       "बाल्य में भी अरोदन"]},
            {"label": "इच्छा और उपशय", "items": ["कटु, तित्त (पढ़ा तिक्त), कषाय, उष्ण, रूक्ष"]}]},
        "seesaw": "सित (सफेद) ↔ असित (काला): दोनों आँखों में व्यक्त (स्पष्ट) दिखते हैं।",
        "sandhi": "अ + अ → आ: सित + असित → सितासित · ह्रस्व स्वर के बाद छ → च्छ: प्र + छन्न → प्रच्छन्न · उ के बाद विसर्ग + घोष → र्: महाललाटोरुबाहुः + व्यक्त → महाललाटोरुबाहुर्व्यक्त।",
        "pegs": "कफ को ‘भरा-पूरा’ से याद रखें: परिपूर्ण गात्र, महा ललाट, गहरा घोष। (मेरी याद-पद्धति, पाठ का कथन नहीं)",
    },
    "23": {
        "chunks": "अपि | च",
        "frame": "एक छपा शब्द, दो अव्यय, कोई क्रिया नहीं: अपि च = और भी।",
        "sandhi": "भिन्न स्वर से पहले इ → य्: अपि + आगतः → अप्यागतः; व्यंजन से पहले कोई परिवर्तन नहीं: अपि च।",
    },
    "24": {
        "contrast": {"groups": [
            {"label": "अल्प (थोड़ा)", "items": ["व्याहार (वाणी)", "क्रोध", "मेधा (पाठ अटपटा)", "अशन (भोजन)", "ईहा"]},
            {"label": "प्राज्य (बहुत)", "items": ["आयु", "वित्त (धन)"]}]},
        "chunks": "अल्पव्याहारक्रोधमेधाशनेहः | प्राज्यायुर्वित्तो | दीर्घदर्शी | वदान्यः | श्राद्धो | गंभीरः | स्थूललक्षः | क्षमावानार्यो | निद्रालुर्दीर्घसूत्री | कृतज्ञः",
        "sandhi": "उ के बाद स् + घोष → र्: आयुस् + वित्त → आयुर्वित्त · अः + घोष व्यंजन → ओ: श्राद्धः + गम्भीरः → श्राद्धो गम्भीरः।",
    },
    "25": {
        "diagram": {"groups": [
            {"label": "स्वभाव", "items": ["ऋजु", "विपश्चित्", "सुभग", "सलज्ज", "गुरुओं का भक्त", "दृढ सौहृद"]},
            {"label": "स्वप्ने पश्यति", "items": ["तोयाशय: कमल (पद्म, मानक) सहित", "तोयाशय: पक्षी-पंक्तियों सहित", "तोयद: बादल"]}]},
        "chunks": "ऋजुर्विपश्चित्सुभगः | सलज्जो | भक्तो गुरूणां | दृढसौहृदश्च | स्वप्ने | सपद्मान्सविहंगमालांस्तोयाशयान् | पश्यति | तोयदांश्च",
        "sandhi": "न् + त → ंस्त: -मालान् + तोयाशयान् → -मालांस्तोयाशयान् · न् + च → ंश्च: तोयदान् + च → तोयदांश्च · उ के बाद विसर्ग + घोष → र्: ऋजुः + विपश्चित् → ऋजुर्विपश्चित्।",
        "pegs": "कफ के स्वप्न को ‘पानी’ से याद रखें: कमल-ताल, पक्षी, बादल। (मेरी याद-पद्धति, पाठ का कथन नहीं)",
    },
}


IMAGE_SPECS = {
    ("13", "chain"): {
        "file": "sh8-vaikrita-13.svg",
        "alt": ("Flowchart of the sure parts of unit 13, in the order of the sense: from the foods of one come out of the womb; the "
                "abnormal (vaikṛta) ones arise; they grow only on the natural (prākṛta) ones; by time and so on; they "
                "favour and also vitiate the body."),
        "type": "mermaid",
        "code": ("flowchart TD\n"
                 "  A[\"१ गर्भ से निकले के आहारों से\"] --> B[\"२ वैकृत उत्पन्न\"]\n"
                 "  B --> C[\"३ प्राकृतों पर ही जमते\"]\n"
                 "  C --> D[\"४ काल आदि के वश से\"]\n"
                 "  D --> E[\"५ शरीर का अनुग्रह भी\"]\n"
                 "  D --> F[\"६ शरीर का दूषण भी\"]\n"),
    },
    ("14", "diagram"): {
        "file": "sh8-vata-prakriti-14.svg",
        "alt": ("Table of unit 14 in printed order: body thin and dry with thin, scanty limbs, teeth, nails, hair, eyes and "
                "voice; noisy joints; quick to begin, be agitated, grasp and forget; unsteady; thief, ignoble, envious, "
                "senses unconquered; fond of music (probable), legends, laughter, play, quarrel, hunting, gardens, journeys; desires "
                "unctuous, hot, sweet, sour (conjectural reading) and salty."),
        "type": "table",
        "title": "इकाई १४: वातप्रकृति",
        "heads": ["क्रम", "लक्षण"],
        "rows": [["१ शरीर", "तनु, रूक्ष"], ["२ अंग आदि", "अंग, दाँत, नख, रोम, नेत्र, स्वर पतले-कम"],
                 ["३ सन्धि", "चलते समय सशब्द"], ["४ शीघ्र", "आरम्भ, क्षोभ, ग्रहण, विस्मरण"],
                 ["५ चंचल", "धृति, मति, गति, दृष्टि, स्वभाव, सौहार्द"],
                 ["६ स्वभाव", "स्तेन, अनार्य, मत्सरी, अजितेन्द्रिय"],
                 ["७ प्रिय", "संगीत (सम्भावित), इतिहास, हास, विलास, कलह, मृगया, उद्यान, यात्रा"],
                 ["८ इच्छा", "स्निग्ध, उष्ण, मधुर, अम्ल (अनुमानित), लवण"]],
    },
    ("18", "diagram"): {
        "file": "sh8-pitta-prakriti-18.svg",
        "alt": ("Table of unit 18 in printed order: warm, fair body; copper-coloured nails, eyes, tongue, lips, palms and "
                "soles; loose joint-ligaments and flesh; tawny, sparse, soft hair; middling strength and life, little "
                "semen, intercourse and offspring; brave, proud; early wrinkles, baldness, grey hair, pimples, blemishes; "
                "intelligent; desires sweet, bitter, astringent and cold."),
        "type": "table",
        "title": "इकाई १८: पित्तप्रकृति",
        "heads": ["क्रम", "लक्षण"],
        "rows": [["१ शरीर", "उष्ण, गौर"], ["२ ताम्र", "नख, नयन, जिह्वा, ओष्ठ, पाणितल, पादतल"],
                 ["३ शिथिल", "सन्धिबन्ध, मांस"], ["४ केश-रोम", "कपिल, विरल, मृदु"],
                 ["५ मध्य", "बल, आयु"], ["६ अल्प", "शुक्र, व्यवाय, अपत्य"], ["७ स्वभाव", "शूर, अभिमानी"],
                 ["८ शीघ्र", "वली, खलित, पलित, पिट्कु (पढ़ा पिटक), व्यङ्ग"], ["९ गुण", "मेधावी, दुर्भग"],
                 ["१० इच्छा", "स्वादु, तित्त (पढ़ा तिक्त), कषाय, शीत"]],
    },
    ("21", "chain"): {
        "file": "sh8-pitta-svapna-21.svg",
        "alt": ("Numbered table of unit 21: asleep he would see, in printed order, karṇikāra trees (probable "
                "identification), palāśa trees (standard), burning of the quarters, meteors, lightning, arka (taken as the "
                "sun) and fires."),
        "type": "table",
        "title": "इकाई २१: सुप्तः पश्येत्",
        "heads": ["क्रम", "क्या देखे"],
        "rows": [["१", "कर्णिकार (सम्भावित)"], ["२", "पलाश: ढाक (मानक)"], ["३", "दिग्दाह"], ["४", "उल्का"],
                 ["५", "विद्युत्: बिजली"], ["६", "अर्क: सूर्य माना"], ["७", "अनल: अग्नि"]],
    },
    ("22", "diagram"): {
        "file": "sh8-kapha-prakriti-22.svg",
        "alt": ("Table of the sure marks of unit 22 in printed order: colour of any one of dūrvā (standard), indīvara "
                "(probable) or śara stalk (probable); full, handsome body; large forehead, thighs (or: broad), arms; eyes with distinct "
                "white and dark; voice like lion, drum, cloud; endures hunger, thirst, heat; firm hidden enmity; gentle, "
                "truthful; memory, steadiness, not greedy; not crying even in childhood; desires pungent, bitter, "
                "astringent, hot, dry."),
        "type": "table",
        "title": "इकाई २२: कफप्रकृति (मुख्य लक्षण)",
        "heads": ["क्रम", "लक्षण"],
        "rows": [["१ वर्ण", "दूर्वेदीवर (पढ़ा दूर्वा, मानक; इन्दीवर, सम्भावित) या शरकाण्ड (सम्भावित)"], ["२ गात्र", "परिपूर्ण, चारु"],
                 ["३ महा", "ललाट, उरु (जाँघ या चौड़ा), बाहु"], ["४ नेत्र", "सित-असित व्यक्त, आयत, विशाल"],
                 ["५ घोष", "सिंह, मृदंग, घन जैसा"], ["६ सहन", "क्षुत्, पिपासा, उष्ण"],
                 ["७ वैर", "दृढ, प्रच्छन्न"], ["८ स्वभाव", "पेशल, सत्यवादी, स्मृतिमान्, धृतिमान्, अलोलुप"],
                 ["९ बाल्य में", "अरोदन"], ["१० इच्छा", "कटु, तित्त (पढ़ा तिक्त), कषाय, उष्ण, रूक्ष"]],
    },
    ("24", "contrast"): {
        "file": "sh8-kapha-alpa-prajya-24.svg",
        "alt": ("Two columns from unit 24: little (alpa): speech, anger, medhā (odd reading), eating, īhā; abundant "
                "(prājya): life and wealth."),
        "type": "split",
        "title": "इकाई २४: अल्प और प्राज्य",
        "cols": [["अल्प (थोड़ा)", ["व्याहार: वाणी", "क्रोध", "मेधा (पाठ अटपटा)", "अशन: भोजन", "ईहा"]],
                 ["प्राज्य (बहुत)", ["आयु", "वित्त: धन"]]],
    },
    ("25", "diagram"): {
        "file": "sh8-kapha-svapna-25.svg",
        "alt": ("Flowchart of unit 25: in a dream he sees water-reservoirs, with lotuses and with rows of birds, and "
                "clouds (water-givers)."),
        "type": "mermaid",
        "code": ("flowchart TD\n"
                 "  S[\"स्वप्ने पश्यति\"] --> A[\"तोयाशय: जलाशय\"]\n"
                 "  A --> B[\"सपद्म: कमल सहित (मानक)\"]\n"
                 "  A --> C[\"सविहङ्गमाल: पक्षी-पंक्ति\"]\n"
                 "  S --> D[\"तोयद: बादल\"]\n"),
    },
}
