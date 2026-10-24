from helpers import mcq, match, order, fill, multi, accepts


AUTHORED = {}

# ---------------------------------------------------------------- unit 39
AUTHORED["39"] = {
    "title": "स्वल्पेऽपि च विण्मूत्रविबंधे फलवर्तीः",
    "question": "By unit 39, what should be done even in a slight obstruction of stool and urine?",
    "rule": ("Even in a slight (स्वल्प) obstruction (विबन्ध) of stool and urine (विण्मूत्र), one should insert "
             "phalavartis (फलवर्ति, suppositories). प्रणिदध्यात् is optative: one should insert."),
    "limits": ("The substance called phala is not specified; where the phalavarti is inserted and who inserts it are not "
               "stated. No recipe, size or number is given. A prose line, not a verse."),
    "explain_hi": ("यह गद्य-पंक्ति कहती है कि मल और मूत्र की थोड़ी-सी भी रुकावट (विबन्ध) हो, तो फलवर्तियाँ, यानी बत्ती के आकार "
                   "की वर्तियाँ (suppository), रखनी चाहिए। "
                   "‘स्वल्पेऽपि’ में ‘अपि’ बल देता है: रुकावट थोड़ी हो, तब भी। "
                   "‘फल’ कौन-सा द्रव्य है, यह यहाँ नहीं बताया गया; वर्ति कहाँ रखी जाए और कौन रखे, यह भी नहीं कहा गया। "
                   "‘प्रणिदध्यात्’ विधिलिङ् है: रखे, रखना चाहिए।"),
    "hook": "थोड़ी-सी भी मल-मूत्र रुकावट: फलवर्ति रखो।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 39, what should one insert even in a slight obstruction of stool and urine?",
            ("Phalavartis, suppositories (फलवर्तीः)", "फलवर्तीः प्रणिदध्यात्: one should insert phalavartis."),
            [("Gruel with ghee, to drink (यवागू)", "Gruel with ghee is given to drink in unit 42, not here."),
             ("Lukewarm oil, rubbed on (तैल)", "Lukewarm oil is for anointing in unit 46."),
             ("A drug powder, given (चूर्ण)", "A powder of drugs is given in unit 44.")],
            "Even a slight obstruction calls for phalavartis.",
            "विण्मूत्रविबन्धे फलवर्तीः प्रणिदध्यात्."),
        order(1, "Put the words of unit 39 in the line's order.",
              ["स्वल्पे", "अपि च", "विण्मूत्रविबंधे", "फलवर्तीः", "प्रणिदध्यात्"],
              "Even in a slight, and, obstruction of stool and urine, phalavartis, one should insert.",
              "स्वल्पे → अपि च → विण्मूत्रविबंधे → फलवर्तीः → प्रणिदध्यात्."),
        match(2, "Match each word of unit 39 to its meaning.",
              [["स्वल्प", "slight"], ["विट्", "stool"], ["मूत्र", "urine"], ["विबन्ध", "obstruction"],
               ["वर्ति", "wick-like roll (suppository)"]],
              "विट् + मूत्र + विबन्ध: obstruction of stool and urine; the phalavarti is a wick-like roll.",
              "स्वल्प, विट्, मूत्र, विबन्ध, वर्ति.", role="extend",
              teaches="विबन्ध = obstruction: विण्मूत्रविबन्ध = obstruction of stool and urine."),
        mcq("discriminate", 3, "Which split of स्वल्पेऽपि is right?",
            ("स्वल्पे + अपि", "ए + अ → ए with the अ dropped, marked by the avagraha (ऽ)."),
            [("स्वल्पः + अपि", "अः + अ would give स्वल्पोऽपि, with ओ, not ए."),
             ("स्वल्प + अपि", "अ + अ would give स्वल्पापि, with no ऽ."),
             ("स्वल्पे + पि", "पि is not a word; the word is अपि (even).")],
            "स्वल्पे (in a slight) + अपि (even): the अ of अपि is dropped after ए and marked ऽ.",
            "ए + अ → एऽ."),
        multi("apply", 4, "Which statements does unit 39 make?",
              [("It names the substance phala as a known drug", "The note: the substance phala is not specified here."),
               ("Even a slight obstruction is enough reason", "Right: स्वल्पेऽपि, even in a slight one."),
               ("Both stool and urine are named", "Right: विट् and मूत्र, in विण्मूत्रविबन्धे."),
               ("It says where the phalavarti is inserted", "The note: the insertion site is not stated.")],
              [1, 2],
              "Slight obstruction of stool and urine; the substance and the site are not stated.",
              "स्वल्पेऽपि च विण्मूत्रविबन्धे."),
        mcq("transfer", 5, "By the rule of स्वल्पेऽपि, how is ग्रामे + अपि (even in the village) written when joined?",
            ("ग्रामेऽपि", "ए + अ → एऽ, as स्वल्पे + अपि."),
            [("ग्रामयपि", "A final ए before अ keeps ए and drops the अ; it does not become अय्."),
             ("ग्रामापि", "The ए does not vanish before अ."),
             ("ग्रामोऽपि", "ओऽ comes from अः + अ (ग्रामः + अपि), not from ए.")],
            "ग्रामे + अपि = ग्रामेऽपि, like स्वल्पे + अपि = स्वल्पेऽपि.",
            "ए + अ → एऽ.",
            teaches="A word-final ए before अ stays ए and the अ is dropped, marked ऽ: स्वल्पे + अपि → स्वल्पेऽपि."),
    ],
}

# ---------------------------------------------------------------- unit 40
AUTHORED["40"] = {
    "title": "तत्रासन्नप्रसवायाः क्लमो ग्लानिः",
    "question": "By unit 40, what signs appear in a woman whose delivery is near?",
    "rule": ("In her whose delivery is near (आसन्नप्रसवा): exhaustion (क्लम), weariness (ग्लानि), eyes as if loosened, "
             "much spitting, urine and stool, a loose belly, heaviness below, no desire for food; then pains of several kinds."),
    "limits": ("Low confidence. How वेदना joins the list of body parts is not certain. The printed -दरत्हृदय- (stray त्) "
               "and स्त्रवण (read स्रवण, flow) are corrected readings: no question rests on हृदय, on flow, or on how far "
               "of the yoni reaches. basti here = bladder."),
    "explain_hi": ("जिसका प्रसव निकट है (आसन्नप्रसवा), उसमें थकावट (क्लम), ग्लानि, मानो बन्धन छूटी हुई दोनों आँखें, थूक, मूत्र और मल "
                   "की अधिकता, कुक्षि की शिथिलता, नीचे भारीपन और अन्न में अरुचि होती है। "
                   "फिर पेट, कमर, बस्ति (मूत्राशय) और वंक्षण आदि में वेदना, तथा तोद (चुभन), भेद (फटन), शूल, स्फुरण (फड़कन) "
                   "और स्राव कहे गए हैं। "
                   "‘वेदना’ और अंगों की सूची का व्याकरणिक सम्बन्ध पक्का नहीं है। "
                   "छपे ‘दरत्हृदय’ और ‘स्त्रवण’ सुधारे गए पाठ हैं, इसलिए इन पर कोई प्रश्न नहीं।"),
    "hook": "प्रसव निकट: थकान, ढीली कुक्षि, नीचे भार, भोजन में अरुचि।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 40, which of these is a sign that delivery is near?",
            ("Exhaustion and weariness (क्लम, ग्लानि)", "क्लमो ग्लानिः: the first two signs named."),
            [("A strong desire for food", "The unit says the opposite: अन्नानभिलाषः, no desire for food."),
             ("Lightness in the lower body", "The unit says the opposite: अधोगुरुत्वम्, heaviness below."),
             ("A belly grown firm and tight", "The unit says the opposite: शिथिलकुक्षिता, a loose belly.")],
            "Exhaustion and weariness open the list of signs.",
            "आसन्नप्रसवायाः क्लमो ग्लानिः ..."),
        order(1, "Put these signs of unit 40 in the line's order.",
              ["क्लमः", "ग्लानिः", "मुक्तबन्धने इवाक्षिणी", "निष्टीविकामूत्रपुरीषबाहुल्यम्", "शिथिलकुक्षिता",
               "अधोगुरुत्वम्"],
              "Exhaustion, weariness, eyes as if loosened, much spitting, urine and stool, loose belly, heaviness below.",
              "क्लमः → ग्लानिः → मुक्तबन्धने इवाक्षिणी → निष्टीविका... बाहुल्यम् → शिथिलकुक्षिता → अधोगुरुत्वम्."),
        match(2, "Match each sign named in unit 40 to its meaning.",
              [["क्लम", "exhaustion"], ["निष्टीविका", "spitting"], ["शिथिलकुक्षिता", "looseness of the belly"],
               ["अधोगुरुत्व", "heaviness below"], ["अन्नानभिलाष", "lack of desire for food"]],
              "Five of the signs of near delivery.",
              "क्लम, निष्टीविका, शिथिलकुक्षिता, अधोगुरुत्व, अन्नानभिलाष.", role="extend",
              teaches="अन्- negates before a vowel: अभिलाष (desire) → अनभिलाष (lack of desire)."),
        mcq("discriminate", 3, "Why is क्लमः printed क्लमो before ग्लानिः in unit 40?",
            ("अः before a voiced consonant (ग) becomes ओ", "Visarga after अ before a voiced sound: अः → ओ."),
            [("ओ is the dual ending of क्लम", "क्लमः is nominative singular in the data, not dual."),
             ("अः becomes ओ before every consonant", "Before an unvoiced consonant (क, त, प ...) it does not become ओ."),
             ("क्लमो is the vocative form", "The vocative of क्लम would be क्लम; the data reads nominative.")],
            "क्लमः + ग्लानिः = क्लमो ग्लानिः: ग is voiced.",
            "अः + voiced consonant → ओ."),
        mcq("apply", 4, "A woman near delivery has no wish to eat. Which word of unit 40 names this?",
            ("अन्नानभिलाषः", "अन्न (food) + अनभिलाष (lack of desire)."),
            [("अधोगुरुत्वम्", "This is heaviness below."),
             ("शिथिलकुक्षिता", "This is looseness of the belly."),
             ("क्लमः", "This is exhaustion.")],
            "No desire for food = अन्नानभिलाषः.",
            "अन्न + अनभिलाष = lack of desire for food."),
        mcq("transfer", 5, "By the rule of क्लमो ग्लानिः, how is रामः + गच्छति (Rāma goes) written?",
            ("रामो गच्छति", "अः before the voiced ग becomes ओ."),
            [("रामः गच्छति", "Before a voiced consonant the visarga after अ does not stay."),
             ("रामर्गच्छति", "र् comes after vowels other than अ/आ, not after अ."),
             ("रामा गच्छति", "अः does not become आ.")],
            "रामः + गच्छति = रामो गच्छति, like क्लमः + ग्लानिः = क्लमो ग्लानिः.",
            "अः + voiced consonant → ओ.",
            teaches="A visarga after अ becomes ओ before a voiced consonant: क्लमः + ग्लानिः → क्लमो ग्लानिः."),
    ],
}

# ---------------------------------------------------------------- unit 41
AUTHORED["41"] = {
    "title": "तदनंतरमावीनां प्रादुर्भावः",
    "question": "By unit 41, what comes after that (तदनन्तरम्)?",
    "rule": ("After that (तदनन्तरम्): the appearance (प्रादुर्भाव) of the āvīs (probably labour pains) and the flow "
             "(प्रवाह) of garbhodaka, the water of the embryo (probably amniotic fluid). No verb is printed."),
    "limits": ("āvī = labour pains and garbhodaka = amniotic fluid are probable identifications. The unit does not name what "
               "तत् (that) points back to. There is no verb, and none is supplied. No time or amount is given."),
    "explain_hi": ("उसके बाद (तदनन्तरम्) आवियों का प्रकट होना (प्रादुर्भाव) और गर्भोदक का बहना (प्रवाह) कहा गया है। "
                   "आवी का अर्थ सम्भवतः प्रसव की पीड़ाएँ है, और गर्भोदक सम्भवतः उल्बद्रव (amniotic fluid); दोनों पहचान सम्भावित हैं। "
                   "पंक्ति में कोई क्रिया नहीं है। "
                   "‘गर्भोदक’ में गर्भ + उदक है (अ + उ → ओ)।"),
    "hook": "उसके बाद: आवियाँ प्रकट, गर्भोदक बहता।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 41, what flows after that?",
            ("Garbhodaka, the water of the embryo", "गर्भोदकप्रवाहः: flow of the water of the embryo (probably amniotic fluid)."),
            [("Hot water poured over her body", "Hot water is sprinkled on her in unit 42; it is not a flow here."),
             ("Urine and stool in abundance", "Abundance of urine and stool is a sign in unit 40."),
             ("Lukewarm oil rubbed on her back", "Lukewarm oil is unit 46.")],
            "The water of the embryo flows.",
            "गर्भोदकप्रवाहश्च."),
        order(1, "Put the words of unit 41 in the line's order.",
              ["तदनन्तरम्", "आवीनाम्", "प्रादुर्भावः", "गर्भोदकप्रवाहः", "च"],
              "After that, of the āvīs, the appearance, the flow of the water of the embryo, and.",
              "तदनन्तरम् → आवीनाम् → प्रादुर्भावः → गर्भोदकप्रवाहः → च."),
        match(2, "Match each word of unit 41 to its meaning.",
              [["तदनन्तरम्", "after that"], ["आवी", "probably labour pains"], ["प्रादुर्भाव", "appearance"],
               ["गर्भोदक", "water of the embryo (probably amniotic fluid)"], ["प्रवाह", "flow"]],
              "Two events after that: appearance of the āvīs, flow of the garbhodaka.",
              "तदनन्तरम्, आवी, प्रादुर्भाव, गर्भोदक, प्रवाह.", role="extend",
              teaches="प्रादुर्भाव = appearance, coming forth; प्रवाह = flow."),
        mcq("discriminate", 3, "Which split of गर्भोदक is right?",
            ("गर्भ + उदक", "अ + उ → ओ: गर्भ + उदक = गर्भोदक."),
            [("गर्भः + उदक", "A compound member has no visarga; अः + उ would not give ओ here."),
             ("गर्भो + दक", "दक is not a word; the word is उदक (water)."),
             ("गर्भ + ओदक", "ओदक is not a word, and अ + ओ would give औ.")],
            "गर्भ (embryo) + उदक (water): अ + उ → ओ.",
            "अ + उ → ओ."),
        multi("apply", 4, "Which statements does unit 41 make?",
              [("No verb is printed in the line", "Right: the note says there is no verb, and none is supplied."),
               ("āvī is identified with certainty", "The identification labour pains is only probable."),
               ("It gives the hours the flow lasts", "No time is given."),
               ("The āvīs appear after that", "Right: तदनन्तरमावीनां प्रादुर्भावः.")],
              [0, 3],
              "A verbless line: after that, the āvīs appear and the garbhodaka flows.",
              "तदनन्तरम् आवीनां प्रादुर्भावः."),
        mcq("transfer", 5, "By the rule of गर्भोदक, how is हित + उपदेशः (good advice) written when joined?",
            ("हितोपदेशः", "अ + उ → ओ, as गर्भ + उदक."),
            [("हितौपदेशः", "अ + उ does not give औ."),
             ("हितुपदेशः", "The अ is not simply dropped before उ."),
             ("हितेपदेशः", "ए comes from अ + इ, not from अ + उ.")],
            "हित + उपदेशः = हितोपदेशः, like गर्भ + उदक = गर्भोदक.",
            "अ + उ → ओ.",
            teaches="A short अ followed by उ joins as ओ: गर्भ + उदक → गर्भोदक."),
    ],
}

# ---------------------------------------------------------------- unit 42
AUTHORED["42"] = {
    "title": "अथैनामुपस्थितगर्भां ... सघृतां यवागूं पाययेत्",
    "question": "By unit 42, how is she prepared, and what is she made to drink?",
    "rule": ("Then (अथ), she whose embryo has come forward (उपस्थितगर्भा), who has done kautuka and auspicious rites, "
             "a male-named fruit in hand, well anointed and sprinkled with hot water, is made to drink gruel (यवागू) with ghee."),
    "limits": ("The male-named fruit (पुंनामफल) is unidentified; the oil of anointing is not named. That delivery is at hand "
               "is an interpretation of उपस्थितगर्भा, not stated. No amount of gruel is given."),
    "explain_hi": ("तब उसे घी सहित यवागू (सघृता यवागू) पिलानी चाहिए। "
                   "वह कैसी हो, यह पाँच विशेषणों से कहा गया है: जिसका गर्भ उपस्थित हो, जिसने कौतुक और मंगल किए हों, हाथ में पुंनामफल "
                   "(पुरुष नाम वाला फल) लिए हो, भली-भाँति तेल लगी हो और गर्म जल से सींची गई हो। "
                   "पुंनामफल की पहचान अज्ञात है, और तेल का नाम भी नहीं दिया गया। "
                   "‘अथैनाम्’ में अथ + एनाम् है (अ + ए → ऐ)।"),
    "hook": "पाँच तैयारियाँ, फिर घी वाली यवागू।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 42, what is she made to drink?",
            ("Gruel with ghee (सघृता यवागू)", "सघृतां यवागूं पाययेत्."),
            [("Milk boiled with herbs", "No milk is named in unit 42."),
             ("Hot water, a full cup", "Hot water is sprinkled on her, not drunk."),
             ("Lukewarm oil, a little", "Lukewarm oil is for anointing in unit 46.")],
            "She drinks gruel with ghee.",
            "सघृतां यवागूं पाययेत्."),
        order(1, "Put her five descriptions in unit 42 in the line's order.",
              ["उपस्थितगर्भाम्", "कृतकौतुकमङ्गलाम्", "पुंनामफलहस्ताम्", "स्वभ्यक्ताम्", "उष्णोदकपरिषिक्ताम्"],
              "Embryo come forward, rites done, fruit in hand, well anointed, sprinkled with hot water.",
              "उपस्थितगर्भाम् → कृतकौतुकमङ्गलाम् → पुंनामफलहस्ताम् → स्वभ्यक्ताम् → उष्णोदकपरिषिक्ताम्."),
        match(2, "Match each description in unit 42 to its meaning.",
              [["उपस्थितगर्भा", "whose embryo has come forward"],
               ["पुंनामफलहस्ता", "with a male-named fruit in hand"],
               ["स्वभ्यक्ता", "well anointed"], ["उष्णोदकपरिषिक्ता", "sprinkled with hot water"],
               ["सघृता यवागू", "gruel with ghee"]],
              "Four descriptions of her and the drink she is given.",
              "उपस्थितगर्भा, पुंनामफलहस्ता, स्वभ्यक्ता, उष्णोदकपरिषिक्ता, सघृता यवागू.", role="extend",
              teaches="स- = with: सघृता = with ghee."),
        mcq("discriminate", 3, "Which split of अथैनाम् is right?",
            ("अथ + एनाम्", "अ + ए → ऐ: अथ + एनाम् = अथैनाम्."),
            [("अथः + एनाम्", "अथ has no visarga; अः + ए would leave अथ एनाम्."),
             ("अथै + नाम्", "अथै and नाम् are not the words here; एनाम् = her."),
             ("अथे + नाम्", "अथे is not a word, and ए + न would give no ऐ.")],
            "अथ (then) + एनाम् (her): अ + ए → ऐ.",
            "अ + ए → ऐ."),
        mcq("apply", 4, "Which of these is NOT among her preparations in unit 42?",
            ("Rubbing her back and sides with lukewarm oil", "That is unit 46, not unit 42."),
            [("Being well anointed (स्वभ्यक्ता)", "Named in unit 42: स्वभ्यक्ताम्."),
             ("Being sprinkled with hot water", "Named in unit 42: उष्णोदकपरिषिक्ताम्."),
             ("Having done kautuka and auspicious rites", "Named in unit 42: कृतकौतुकमङ्गलाम्.")],
            "Rubbing of the back and sides comes later, in unit 46.",
            "उपस्थितगर्भा, कृतकौतुकमङ्गला, पुंनामफलहस्ता, स्वभ्यक्ता, उष्णोदकपरिषिक्ता."),
        mcq("transfer", 5, "By the rule of स्वभ्यक्ता (सु + अभ्यक्ता), how is सु + आगतम् (welcome) written?",
            ("स्वागतम्", "उ + a different vowel → व्: सु + आगतम् = स्वागतम्."),
            [("सुआगतम्", "उ and आ are not left side by side."),
             ("सोगतम्", "उ + आ does not give ओ."),
             ("सवागतम्", "The उ becomes व्, with no अ after स.")],
            "सु + आगतम् = स्वागतम्, like सु + अभ्यक्ता = स्वभ्यक्ता.",
            "उ + a different vowel → व्.",
            teaches="A final उ before a different vowel becomes व्: सु + अभ्यक्ता → स्वभ्यक्ता."),
    ],
}

# ---------------------------------------------------------------- unit 43
AUTHORED["43"] = {
    "title": "ततः ... स्त्रियः सूतिकां ... पर्युपासीरन्",
    "question": "By unit 43, where does the sūtikā lie, and what kind of women attend her?",
    "rule": ("She lies face up (उत्तान) on a soft ground-bed covered with a very red bull's hide, thighs and back bent. "
             "Women in new clothes, trustworthy, pleasant to see, older, bold, nails cut, attend her with kind, true words."),
    "limits": ("Skilled in delivery rests on the conjectural reading प्रजननकुशलाः for printed प्रजनकशलाः; no question rests "
               "on it. The posture beyond bent thighs and back is not described. सूतिका here = the woman in labour, by context."),
    "explain_hi": ("तब सूतिका (प्रसव करने वाली स्त्री) अच्छे लाल बैल के चमड़े से ढकी कोमल भूमि-शय्या पर उत्तान, यानी पीठ के बल, "
                   "जाँघें और पीठ मोड़े लेटी हो। "
                   "उसके पास ऐसी स्त्रियाँ बैठें: नए वस्त्र पहने, विश्वसनीय (अशंकनीय), देखने में प्रिय, प्रौढ़ आयु की, निर्भीक "
                   "(प्रगल्भ) और कटे नखों वाली। "
                   "वे मधुर और सच्ची वाणी से उसे आश्वासन देती रहें। "
                   "‘प्रसव में कुशल’ छपे ‘प्रजनकशलाः’ का अनुमानित पाठ है, इसलिए उस पर प्रश्न नहीं।"),
    "hook": "लाल चर्म की कोमल शय्या, प्रौढ़ निर्भीक सखियाँ, मीठे सच्चे बोल।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 43, how do the attending women speak to her?",
            ("With pleasant, true words, comforting her", "सूनृताभिर्वाणीभिराश्वासयन्त्यः."),
            [("In silence, saying nothing at all", "The unit names words (वाणीभिः) that comfort her."),
             ("With stern orders to push at once", "The words are pleasant and true, and they comfort her."),
             ("With the puṇyāha formula only", "Puṇyāha is named in unit 38, not here.")],
            "They comfort her with pleasant, true words.",
            "सूनृताभिर्वाणीभिराश्वासयन्त्यः पर्युपासीरन्."),
        order(1, "Put these descriptions of the women in unit 43 in the line's order.",
              ["अहतवाससः", "अशङ्कनीयाः", "प्रियदर्शनाः", "परिणतवयसः", "प्रगल्भाः", "कृत्तनखाः"],
              "New clothes, trustworthy, pleasant to see, older, bold, nails cut.",
              "अहतवाससः → अशङ्कनीयाः → प्रियदर्शनाः → परिणतवयसः → प्रगल्भाः → कृत्तनखाः."),
        match(2, "Match each word of unit 43 to its meaning.",
              [["उत्तान", "face upward"], ["अहतवासस्", "wearing new, unworn clothes"],
               ["अशङ्कनीय", "not to be suspected, trustworthy"], ["परिणतवयस्", "advanced in age"],
               ["कृत्तनख", "with cut nails"]],
              "Her posture and four qualities of the women.",
              "उत्तान, अहतवासस्, अशङ्कनीय, परिणतवयस्, कृत्तनख.", role="extend",
              teaches="अहत = unworn, new: अहतवाससः = women in new clothes."),
        mcq("discriminate", 3, "Which split of अहतवाससोऽशङ्कनीयाः is right?",
            ("अहतवाससः + अशङ्कनीयाः", "अः + अ → ओऽ: the अ of अशङ्कनीयाः is dropped and marked ऽ."),
            [("अहतवासस + अशङ्कनीयाः", "अ + अ would give आ (अहतवाससाशङ्कनीयाः), not ओऽ."),
             ("अहतवाससे + अशङ्कनीयाः", "ए + अ would give एऽ (अहतवाससेऽशङ्कनीयाः), not ओऽ."),
             ("अहतवाससः + शङ्कनीयाः", "No अ follows, so no ओ and no ऽ would appear.")],
            "अहतवाससः (in new clothes) + अशङ्कनीयाः (trustworthy).",
            "अः + अ → ओऽ."),
        mcq("apply", 4, "By unit 43, on what does the woman in labour lie?",
            ("A soft bed on the ground, covered with red bull's hide", "सुरक्तार्षभचर्मप्रच्छदे मृदुनि भूमिशयने."),
            [("A raised cot spread with a white cloth", "The bed is on the ground (भूमिशयन), covered with hide."),
             ("A bed of grass laid close to the fire", "Grass and fire are not named in unit 43."),
             ("A low seat, sitting with her back upright", "She lies face upward (उत्तानाम्), not seated.")],
            "A soft ground-bed with a very red bull's hide covering.",
            "मृदुनि भूमिशयने शयानाम् उत्तानाम्."),
        mcq("transfer", 5, "By the rule of अहतवाससोऽशङ्कनीयाः, how is रामः + अपि (Rāma too) written?",
            ("रामोऽपि", "अः + अ → ओऽ."),
            [("रामापि", "अः + अ does not give आ."),
             ("रामरपि", "र् appears after vowels other than अ/आ, not after अ."),
             ("रामः अपि", "Before अ the visarga after अ does not stay.")],
            "रामः + अपि = रामोऽपि, like अहतवाससः + अशङ्कनीयाः.",
            "अः + अ → ओऽ.",
            teaches="A visarga after अ before अ: अः becomes ओ and the next अ is dropped (ऽ): अहतवाससः + अशङ्कनीयाः → अहतवाससोऽशङ्कनीयाः."),
    ],
}

# ---------------------------------------------------------------- unit 44
AUTHORED["44"] = {
    "title": "अथास्यै दद्यात् ... चूर्णम्",
    "question": "By unit 44, of which drugs is the powder given to her made?",
    "rule": ("Then one should give her a powder (चूर्ण) of kuṣṭha (costus), elā (small cardamom), lāṅgalī (glory lily), "
             "vacā (sweet flag), an unclear cyanya, citraka (leadwort) and cirabilva (probably Indian elm)."),
    "limits": ("Low confidence. cyanya is unclear (possibly cavya, not certain). To smell (उपाघ्रातुम्) is a conjectural "
               "reading of printed उपाघातुं, so no question rests on smelling or on cyanya. cirabilva is probable; the others "
               "standard. No amount is stated."),
    "explain_hi": ("तब उसे इन द्रव्यों का चूर्ण देना चाहिए: कुष्ठ (कूठ), एला (छोटी इलायची), लाङ्गली (कलिहारी), वचा (बच), च्यन्य "
                   "(अस्पष्ट शब्द), चित्रक (चीता) और चिरबिल्व (सम्भवतः चिलबिल)। "
                   "पहले पाँच की पहचान मानक है, चिरबिल्व की सम्भावित, और च्यन्य अस्पष्ट है। "
                   "छपा ‘उपाघातुं’ अनुमानित पाठ पर ‘उपाघ्रातुम्’ (सूँघने के लिए) पढ़ा गया है, इसलिए सूँघने पर प्रश्न नहीं। "
                   "‘कुष्ठैला’ में कुष्ठ + एला है (अ + ए → ऐ)।"),
    "hook": "कूठ-इलायची-कलिहारी-बच ... चीता-चिलबिल: सबका चूर्ण।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 44, in what form are the drugs given to her?",
            ("A powder (चूर्ण)", "...चिरबिल्वचूर्णम्: the compound ends in चूर्ण, powder."),
            [("A gruel (यवागू)", "Gruel with ghee is unit 42."),
             ("An oil (तैल)", "Oil is unit 46."),
             ("A suppository (वर्ति)", "Phalavartis are unit 39.")],
            "The drugs are given as a powder.",
            "...चूर्णम् दद्यात्."),
        order(1, "Put these drugs of unit 44 in the line's order.",
              ["कुष्ठ", "एला", "लाङ्गली", "वचा", "चित्रक"],
              "Kuṣṭha, elā, lāṅgalī, vacā, (unclear cyanya), citraka.",
              "कुष्ठ → एला → लाङ्गली → वचा → चित्रक."),
        match(2, "Match each drug of unit 44 to the identification its data gives.",
              [["कुष्ठ", "costus, Saussurea costus (standard)"],
               ["एला", "small cardamom, Elettaria cardamomum (standard)"],
               ["लाङ्गली", "glory lily, Gloriosa superba (standard)"],
               ["वचा", "sweet flag, Acorus calamus (standard)"],
               ["चित्रक", "leadwort, Plumbago zeylanica (standard)"]],
              "Five drugs with standard identifications.",
              "कुष्ठ, एला, लाङ्गली, वचा, चित्रक.", role="extend",
              teaches="चूर्ण = powder: the drug names stand in one compound ending in चूर्णम्."),
        mcq("discriminate", 3, "Which split of कुष्ठैला is right?",
            ("कुष्ठ + एला", "अ + ए → ऐ: कुष्ठ + एला = कुष्ठैला."),
            [("कुष्ठः + एला", "A compound member has no visarga; अः + ए would not give ऐ."),
             ("कुष्ठि + एला", "इ + ए would give ये (कुष्ठ्येला), not ऐ."),
             ("कुष्ठे + ला", "ला is not a drug; the word is एला (cardamom).")],
            "कुष्ठ (costus) + एला (cardamom): अ + ए → ऐ.",
            "अ + ए → ऐ."),
        mcq("apply", 4, "Which drug of unit 44 has only a probable identification in its data?",
            ("चिरबिल्व, probably Indian elm", "The data tags cirabilva as probable."),
            [("वचा, sweet flag", "Tagged standard."),
             ("एला, small cardamom", "Tagged standard."),
             ("चित्रक, leadwort", "Tagged standard.")],
            "cirabilva = Holoptelea integrifolia is probable; the others are standard.",
            "चिरबिल्व: probable."),
        mcq("transfer", 5, "By the rule of कुष्ठैला, how is तत्र + एव (right there) written when joined?",
            ("तत्रैव", "अ + ए → ऐ, as कुष्ठ + एला."),
            [("तत्रेव", "अ + ए gives ऐ, not ए."),
             ("तत्रयेव", "अ does not become अय् before ए."),
             ("तत्रौव", "औ comes from अ + ओ, not from अ + ए.")],
            "तत्र + एव = तत्रैव, like कुष्ठ + एला = कुष्ठैला.",
            "अ + ए → ऐ.",
            teaches="A short अ followed by ए joins as ऐ: कुष्ठ + एला → कुष्ठैला."),
    ],
}

# ---------------------------------------------------------------- unit 45
AUTHORED["45"] = {
    "title": "तथा भूर्जपत्रशिशिपासर्ज रसान्यतमधूमम्",
    "question": "By unit 45, what smoke is given likewise, and how?",
    "rule": ("Likewise (तथा): smoke (धूम) of any one (अन्यतम) of birch bark (भूर्जपत्र), śiśipā (sissoo) or sarja (sāl) "
             "sap, and at intervals (अन्तरान्तरा). The verb is carried over from before."),
    "limits": ("Elliptical: no verb is printed; दद्यात् (one should give) is understood from earlier. Reading सर्ज and रस "
               "together as sarja sap is an interpretation; रस could be a separate item. The note takes the intervals as "
               "between the sniffings, which the line does not say."),
    "explain_hi": ("वैसे ही भूर्जपत्र (भोजपत्र), शिशिपा (शीशम) या सर्ज (साल) के रस, इनमें से किसी एक (अन्यतम) का धुआँ (धूम) "
                   "बीच-बीच में (अन्तरान्तरा) भी दिया जाए। "
                   "पंक्ति में क्रिया नहीं है; ‘दद्यात्’ पिछली पंक्ति से समझा जाता है। "
                   "छपे में ‘सर्ज’ और ‘रस’ अलग हैं; दोनों को साथ पढ़कर ‘सर्ज का रस’ एक व्याख्या है, ‘रस’ अलग द्रव्य भी हो सकता है। "
                   "‘रसान्यतम’ में रस + अन्यतम है (अ + अ → आ)।"),
    "hook": "भोजपत्र, शीशम या साल-रस: कोई एक, धुआँ बीच-बीच में।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 45, whose smoke is given?",
            ("Of any one of the substances listed", "अन्यतम = any one of them."),
            [("Of all the listed ones burnt together", "अन्यतम means any one, not all together."),
             ("Of the drug powder from unit 44", "The powder is unit 44; unit 45 lists other substances."),
             ("Of ghee poured on a fire", "Ghee is not named in unit 45.")],
            "Any one of birch bark, śiśipā or sarja sap.",
            "...अन्यतमधूमम्."),
        order(1, "Put the parts of unit 45 in the line's order.",
              ["तथा", "भूर्जपत्र", "शिशिपा", "सर्ज रस", "अन्यतमधूमम्", "अन्तरान्तरा च"],
              "Likewise, birch bark, śiśipā, sarja sap, smoke of any one, and at intervals.",
              "तथा → भूर्जपत्र → शिशिपा → सर्ज रस → अन्यतमधूमम् → अन्तरान्तरा च."),
        match(2, "Match each word of unit 45 to its meaning.",
              [["भूर्जपत्र", "birch bark, Betula utilis (standard)"],
               ["शिशिपा", "sissoo, Indian rosewood, Dalbergia sissoo (standard)"],
               ["सर्ज", "sāl tree, Shorea robusta (standard)"],
               ["अन्यतम", "any one of"], ["अन्तरान्तरा", "at intervals"]],
              "Three sources of smoke, and how the smoke is used.",
              "भूर्जपत्र, शिशिपा, सर्ज, अन्यतम, अन्तरान्तरा.", role="extend",
              teaches="अन्यतम = any one of several: the smoke of one substance at a time."),
        mcq("discriminate", 3, "Which split of रसान्यतम is right?",
            ("रस + अन्यतम", "अ + अ → आ: रस + अन्यतम = रसान्यतम."),
            [("रसः + अन्यतम", "अः + अ would give रसोऽन्यतम."),
             ("रसा + न्यतम", "न्यतम is not a word; the word is अन्यतम."),
             ("रस + आन्यतम", "आन्यतम is not a word; the word is अन्यतम (any one).")],
            "रस (sap) + अन्यतम (any one): अ + अ → आ.",
            "अ + अ → आ."),
        multi("apply", 4, "Which statements fit unit 45?",
              [("A verb is printed in the line", "No verb is printed; दद्यात् is carried over."),
               ("The smoke is of one substance at a time", "Right: अन्यतम, any one."),
               ("The smoke is to be blown into the yoni", "No route is stated in unit 45."),
               ("The smoke is given at intervals", "Right: अन्तरान्तरा च.")],
              [1, 3],
              "Any one substance's smoke, at intervals; the verb is understood.",
              "अन्यतमधूमम् अन्तरान्तरा च."),
        mcq("transfer", 5, "By the rule of रसान्यतम, how is न + अस्ति (is not) written when joined?",
            ("नास्ति", "अ + अ → आ, as रस + अन्यतम."),
            [("नस्ति", "The two अ do not shrink to one short अ."),
             ("नोस्ति", "अ + अ does not give ओ."),
             ("नअस्ति", "Two vowels are not left side by side.")],
            "न + अस्ति = नास्ति, like रस + अन्यतम = रसान्यतम.",
            "अ + अ → आ.",
            teaches="Two short अ join as long आ: रस + अन्यतम → रसान्यतम."),
    ],
}

# ---------------------------------------------------------------- unit 46
AUTHORED["46"] = {
    "title": "पार्श्वपृष्ठकटीसक्थिदेशान्कोष्णेन तैलेनाभ्यज्य",
    "question": "By unit 46, which regions of her are anointed, and with what?",
    "rule": ("Having anointed (अभ्यज्य) the regions (देश) of her sides, back, waist and thighs with lukewarm (कोष्ण) oil, "
             "one should rub them comfortably (अनुसुखम्). अभ्यज्य is an absolutive: having anointed."),
    "limits": ("The final verb is printed मृद्गीयात्, not a form; मृद्नीयात् (should rub, knead) is a conjectural reading, "
               "so no question rests on it. The oil is not named, and no time or amount is given."),
    "explain_hi": ("उसके पार्श्व, पीठ, कटि और जाँघ के प्रदेशों पर गुनगुने (कोष्ण) तेल से अभ्यंग करके सुखपूर्वक (अनुसुखम्) मर्दन करना चाहिए। "
                   "‘अभ्यज्य’ पूर्वकालिक रूप है: तेल लगाकर। "
                   "छपा ‘मृद्गीयात्’ कोई रूप नहीं; ‘मृद्नीयात्’ (मले) अनुमानित पाठ है, इसलिए उस पर प्रश्न नहीं। "
                   "तेल का नाम नहीं दिया गया। "
                   "‘अस्या मृद्...’ में अस्याः का विसर्ग घोष म से पहले नियम से लुप्त हुआ है।"),
    "hook": "पार्श्व-पीठ-कटि-जाँघ: गुनगुना तेल, फिर सुख से मर्दन।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 46, what is the oil like?",
            ("Lukewarm (कोष्ण)", "कोष्णेन तैलेन: with lukewarm oil."),
            [("Cold", "The unit says कोष्ण, lukewarm."),
             ("Boiling", "The unit says कोष्ण, lukewarm."),
             ("Mixed with ghee", "No ghee is named in unit 46.")],
            "The oil is lukewarm.",
            "कोष्णेन तैलेन."),
        order(1, "Put the regions named in unit 46 in the line's order.",
              ["पार्श्व", "पृष्ठ", "कटी", "सक्थि"],
              "Sides, back, waist, thighs.",
              "पार्श्व → पृष्ठ → कटी → सक्थि."),
        match(2, "Match each word of unit 46 to its meaning.",
              [["पार्श्व", "side"], ["पृष्ठ", "back"], ["कटी", "waist, hip"], ["सक्थि", "thigh"],
               ["कोष्ण", "lukewarm"]],
              "Four regions and the warmth of the oil.",
              "पार्श्व, पृष्ठ, कटी, सक्थि, कोष्ण.", role="extend",
              teaches="देश = region, part: पार्श्वपृष्ठकटीसक्थिदेशान् = the regions of the sides, back, waist and thighs."),
        mcq("discriminate", 3, "Why is अस्याः printed अस्या before मृद्गीयात् in unit 46?",
            ("After आ, a visarga drops before a voiced sound", "The note: regular sandhi, not a typo."),
            [("It is a misprint for अस्य", "The note says this is regular sandhi, not a typo."),
             ("अस्या is a separate instrumental form", "The data reads अस्याः, genitive singular."),
             ("A visarga drops before every consonant", "Before त it would become स्, for example; not dropped.")],
            "अस्याः + म... → अस्या म...: आः before a voiced sound loses the visarga.",
            "आः + voiced sound → आ."),
        multi("apply", 4, "Which statements does unit 46 make?",
              [("The oil is lukewarm", "Right: कोष्णेन तैलेन."),
               ("The oil is named as sesame oil", "The note: the oil is unspecified."),
               ("The waist and thighs are among the regions", "Right: कटी and सक्थि are named."),
               ("The anointing lasts one hour", "No time is given.")],
              [0, 2],
              "Lukewarm, unnamed oil on sides, back, waist and thighs.",
              "पार्श्वपृष्ठकटीसक्थिदेशान् कोष्णेन तैलेन अभ्यज्य."),
        mcq("transfer", 5, "By the -य of अभ्यज्य (having anointed), what does प्रविश्य mean, from प्र-√विश् (enter)?",
            ("Having entered", "A prefixed verb makes its absolutive with -य: having done."),
            [("Entering now", "That would be a present participle, not -य."),
             ("To enter", "That would be the infinitive प्रवेष्टुम्."),
             ("One should enter", "That would be the optative प्रविशेत्.")],
            "प्रविश्य = having entered, like अभ्यज्य = having anointed.",
            "prefix + verb + -य = absolutive (having done).",
            teaches="A verb with a prefix forms its absolutive with -य, not -त्वा: अभि-√अञ्ज् → अभ्यज्य, प्र-√विश् → प्रविश्य."),
    ],
}

# ---------------------------------------------------------------- unit 47
AUTHORED["47"] = {
    "title": "एवमवाक् परिवर्तते गर्भः",
    "question": "By unit 47, what happens to the fetus by this procedure?",
    "rule": ("Thus (एवम्) the fetus (गर्भ) turns around (परिवर्तते) downward (अवाक्). परिवर्तते is present, middle voice, "
             "of परि-√वृत्."),
    "limits": ("The line does not say which part of the fetus leads or what position results. By the data's note, एवम् "
               "points back to the procedure of units 44 to 46."),
    "explain_hi": ("इस प्रकार (एवम्) गर्भ नीचे की ओर (अवाक्) पलट जाता है (परिवर्तते)। "
                   "‘एवम्’ डेटा की टिप्पणी के अनुसार पिछली विधि (इकाई 44 से 46) की ओर संकेत करता है। "
                   "गर्भ का कौन-सा भाग आगे होता है, या कौन-सी स्थिति बनती है, यह पंक्ति नहीं बताती। "
                   "‘एवमवाक्’ में एवम् + अवाक् है: स्वर से पहले म् बना रहता है।"),
    "hook": "विधि से गर्भ नीचे को पलटता है।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 47, which way does the fetus turn?",
            ("Downward (अवाक्)", "अवाक् परिवर्तते: turns around, downward."),
            [("Upward, toward the heart", "The unit says अवाक्, downward."),
             ("To the right side", "No side is named."),
             ("It does not turn at all", "परिवर्तते: it turns around.")],
            "The fetus turns downward.",
            "एवमवाक् परिवर्तते गर्भः."),
        order(1, "Put the words of unit 47 in the line's order.",
              ["एवम्", "अवाक्", "परिवर्तते", "गर्भः"],
              "Thus, downward, turns around, the fetus.",
              "एवम् → अवाक् → परिवर्तते → गर्भः."),
        match(2, "Match each word of unit 47 to its meaning.",
              [["एवम्", "thus"], ["अवाक्", "downward"], ["परिवर्तते", "turns around"], ["गर्भः", "the fetus"]],
              "Four words make the whole line.",
              "एवम्, अवाक्, परिवर्तते, गर्भः.", role="extend",
              teaches="परि-√वृत् = turn around: परिवर्तते = it turns around."),
        mcq("discriminate", 3, "By unit 47, which part of the fetus leads as it turns?",
            ("The unit does not say", "The note: the line does not say which part leads."),
            [("The head leads", "No part is named in the line."),
             ("The feet lead", "No part is named in the line."),
             ("The back leads", "No part is named in the line.")],
            "Only the direction, downward, is stated.",
            "अवाक् = downward; no leading part is named."),
        fill(4, "In unit 47, the word for downward is ____ (type it in Devanagari or in English letters, e.g. dharma).",
             accepts("अवाक्", None, "avak"),
             "एवमवाक् = एवम् + अवाक् (downward).",
             "अवाक् = downward: the direction of the turning.",
             "अवाक् = downward.", role="apply"),
        mcq("transfer", 5, "By the join एवमवाक् (एवम् + अवाक्), how is किम् + अपि (anything) written?",
            ("किमपि", "A final म् before a vowel stays म् and joins it."),
            [("किंअपि", "Anusvāra stands only before a consonant, not before a vowel."),
             ("किमोपि", "म् + अ gives म, not मो."),
             ("किम्पि", "The अ of अपि is not dropped.")],
            "किम् + अपि = किमपि, like एवम् + अवाक् = एवमवाक्.",
            "final म् + vowel → म + vowel.",
            teaches="A final म् before a vowel stays म् and is written joined: एवम् + अवाक् → एवमवाक्."),
    ],
}

# ---------------------------------------------------------------- unit 48
AUTHORED["48"] = {
    "title": "तस्य लक्षणम्",
    "question": "By unit 48, what does this short line name?",
    "rule": ("Its sign (तस्य लक्षणम्). तस्य is genitive singular, of it, of that; लक्षणम् = sign, mark. The copula is "
             "understood."),
    "limits": ("The line does not itself state the sign. By the data's note, तस्य most likely refers to the turning of the "
               "fetus in unit 47, and the sign is stated in unit 49 (GROUPING). Printed as one token, तस्यलक्षणं."),
    "explain_hi": ("यह छोटी पंक्ति केवल इतना कहती है: ‘उसका लक्षण’। "
                   "‘तस्य’ षष्ठी एकवचन है (उसका), और ‘लक्षणम्’ का अर्थ है चिह्न, पहचान। "
                   "डेटा की टिप्पणी के अनुसार ‘तस्य’ सम्भवतः इकाई 47 के गर्भ के पलटने की ओर संकेत करता है, और लक्षण अगली इकाई (49) में कहा गया है। "
                   "क्रिया ‘है’ समझी जाती है।"),
    "hook": "‘तस्य लक्षणम्’: उसका चिह्न, आगे सुनो।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 48, what does लक्षणम् mean?",
            ("Sign, mark", "लक्षणम् = sign, mark."),
            [("Cause", "A cause would be कारण or हेतु."),
             ("Remedy", "A remedy would be चिकित्सा or औषध."),
             ("Time", "Time would be काल.")],
            "लक्षणम् = sign.",
            "तस्य लक्षणम् = its sign."),
        mcq("warmup", 1, "Which split of the printed तस्यलक्षणं is right?",
            ("तस्य + लक्षणम्", "Two words printed together: of it + sign."),
            [("तस्यल + क्षणम्", "तस्यल is not a word."),
             ("तस् + यलक्षणम्", "Neither part is a word."),
             ("तस्याः + लक्षणम्", "That would be printed तस्या लक्षणम्, with आ.")],
            "तस्य (of it) + लक्षणम् (sign).",
            "तस्यलक्षणं = तस्य लक्षणम्."),
        fill(2, "In unit 48, the word for sign is ____ (type it in Devanagari or in English letters, e.g. dharma).",
             accepts("लक्षणम्", None, "लक्षण", "lakshanam", "lakshana"),
             "तस्य लक्षणम् = its sign.",
             "लक्षण = sign, mark.",
             "लक्षणम् = sign."),
        mcq("discriminate", 3, "In unit 48, what case is तस्य?",
            ("Genitive singular: of it", "The data: तस्य, gen. sg."),
            [("Nominative: it, the subject", "The nominative would be सः or तत्."),
             ("Dative: for it", "The dative would be तस्मै."),
             ("Locative: in it", "The locative would be तस्मिन्.")],
            "तस्य = of it.",
            "तस्य = genitive singular."),
        multi("apply", 4, "Which statements about unit 48 are right?",
              [("The line itself lists the sign", "The line names a sign but does not state it."),
               ("लक्षणम् is a plural form", "लक्षणम् is neuter nominative singular."),
               ("No verb is printed; the copula is understood", "Right: the note says copula understood."),
               ("By the note, तस्य most likely means the turning", "Right: of the fetus's turning in unit 47.")],
              [2, 3],
              "A verbless heading: its sign; तस्य most likely means the turning.",
              "तस्य लक्षणम् (copula understood)."),
        mcq("transfer", 5, "By तस्य लक्षणम्, how is the sign of a disease (रोग) said in an invented phrase?",
            ("रोगस्य लक्षणम्", "-स्य = of, as in तस्य."),
            [("रोगः लक्षणम्", "रोगः is nominative: the disease, not of the disease."),
             ("रोगेण लक्षणम्", "रोगेण is instrumental: by the disease."),
             ("रोगाय लक्षणम्", "रोगाय is dative: for the disease.")],
            "रोगस्य लक्षणम् = the sign of the disease, like तस्य लक्षणम्.",
            "genitive -स्य = of.",
            teaches="The genitive singular ending -स्य means of: तस्य (of it), रोगस्य (of the disease)."),
    ],
}

# ---------------------------------------------------------------- unit 49
AUTHORED["49"] = {
    "title": "विमुच्य हृदयमुदरमाविशति",
    "question": "By unit 49, what does the turning fetus do?",
    "rule": ("Having left (विमुच्य) the heart (हृदय), it enters (आविशति) the belly (उदर) and takes hold of (अवगृह्णाति) the "
             "head of the bladder (बस्तिशिरस्; basti, probably bladder). विमुच्य is an absolutive: the leaving comes first."),
    "limits": ("The subject, the fetus, is understood from unit 47; it is not printed. basti = bladder is probable here. "
               "Printed अवगृण्हाति is read अवगृह्णाति (letters swapped). The unit says nothing more about the sign."),
    "explain_hi": ("हृदय को छोड़कर (विमुच्य) वह उदर में प्रवेश करता है (आविशति) और बस्ति-शिर, यानी सम्भवतः मूत्राशय के सिरे, को पकड़ लेता है। "
                   "कर्ता (गर्भ) यहाँ छपा नहीं, इकाई 47 से समझा जाता है। "
                   "‘विमुच्य’ पूर्वकालिक रूप है, इसलिए छोड़ना पहले और प्रवेश बाद में है। "
                   "बस्ति = मूत्राशय यहाँ सम्भावित पहचान है। "
                   "‘बस्तिशिरोऽव...’ में शिरः + अवगृह्णाति है (अः + अ → ओऽ)।"),
    "hook": "हृदय छोड़ा, उदर में आया, बस्ति-शिर पकड़ा।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "By unit 49, what does it enter?",
            ("The belly (उदर)", "उदरमाविशति: enters the belly."),
            [("The heart (हृदय)", "The heart is what it leaves (विमुच्य)."),
             ("The waist (कटी)", "The waist is not named in unit 49."),
             ("The back (पृष्ठ)", "The back is not named in unit 49.")],
            "It enters the belly.",
            "उदरम् आविशति."),
        order(1, "Put the three actions of unit 49 in the line's order.",
              ["विमुच्य हृदयम्", "उदरम् आविशति", "बस्तिशिरः अवगृह्णाति"],
              "Leaves the heart, enters the belly, takes hold of the head of the bladder.",
              "विमुच्य हृदयम् → उदरम् आविशति → बस्तिशिरः अवगृह्णाति."),
        match(2, "Match each word of unit 49 to its meaning.",
              [["विमुच्य", "having left"], ["हृदयम्", "the heart"], ["आविशति", "enters"],
               ["बस्तिशिरः", "head of the bladder (basti, probable)"], ["अवगृह्णाति", "takes hold of"]],
              "Leaving, entering and taking hold.",
              "विमुच्य, हृदयम्, आविशति, बस्तिशिरः, अवगृह्णाति.", role="extend",
              teaches="विमुच्य is an absolutive (having left): its action comes before the main verb आविशति."),
        mcq("discriminate", 3, "By unit 49, which does it leave, and which does it enter?",
            ("Leaves the heart, enters the belly", "विमुच्य हृदयम् उदरम् आविशति."),
            [("Leaves the belly, enters the heart", "The other way round: it leaves the heart."),
             ("Leaves the bladder, enters the belly", "It takes hold of the head of the bladder; it does not leave it."),
             ("Leaves the heart, enters the bladder", "It enters the belly; the bladder's head it takes hold of.")],
            "Heart left, belly entered, bladder's head held.",
            "विमुच्य हृदयम् → उदरम् आविशति."),
        mcq("apply", 4, "Which split of बस्तिशिरोऽव... (बस्तिशिरोऽवगृह्णाति) is right?",
            ("बस्तिशिरः + अवगृह्णाति", "अः + अ → ओऽ: शिरः + अवगृह्णाति."),
            [("बस्तिशिरो + वगृह्णाति", "वगृह्णाति is not a word; the verb is अवगृह्णाति."),
             ("बस्तिशिर + अवगृह्णाति", "अ + अ would give आ (शिरावगृह्णाति), not ओऽ."),
             ("बस्तिशिरे + अवगृह्णाति", "ए + अ would give एऽ, not ओऽ.")],
            "बस्तिशिरः (head of the bladder) + अवगृह्णाति (takes hold of).",
            "अः + अ → ओऽ."),
        mcq("transfer", 5, "By the order of विमुच्य ... आविशति, what does गृहं विमुच्य वनमाविशति mean?",
            ("Having left the house, he enters the forest", "विमुच्य: the leaving comes first, then आविशति."),
            [("Entering the house, he leaves the forest", "गृहम् is what is left; वनम् is entered."),
             ("He enters the forest without leaving home", "विमुच्य says he has left the house."),
             ("Having left the forest, he enters the house", "The objects are the other way round.")],
            "गृहं विमुच्य वनमाविशति = having left the house, he enters the forest.",
            "absolutive + main verb: first the absolutive's action.",
            teaches="An absolutive (विमुच्य, having left) names an action done before the main verb (आविशति, enters)."),
    ],
}

# ---------------------------------------------------------------- unit 50
AUTHORED["50"] = {
    "title": "न चेदेवं परिवर्त्तते",
    "question": "By unit 50, what is done if the fetus does not turn in this way?",
    "rule": ("If it does not turn thus (न चेदेवं परिवर्तते), then (ततः) she is to be made to do (कारयितव्या) yawning "
             "(जृम्भण) and walking about (चङ्क्रमण) again and again, and the procedure stated just before."),
    "limits": ("Low confidence. The opening त्वरयन्त्येनामाढ्यः is damaged: आढ्यः is unclear, so they urge her on is only "
               "conjectural; no question rests on it. The procedure stated just before appears, by the note, to point to "
               "units 44 to 46."),
    "explain_hi": ("पंक्ति का आरम्भ (‘त्वरयन्त्येनामाढ्यः’) क्षतिग्रस्त है; ‘आढ्यः’ अस्पष्ट है, इसलिए ‘वे उसे जल्दी को प्रेरित करते हैं’ "
                   "केवल अनुमानित पाठ है। "
                   "निश्चित भाग यह है: यदि गर्भ इस प्रकार नहीं पलटता, तो उससे बार-बार जम्हाई (जृम्भण) और टहलना (चङ्क्रमण) "
                   "कराना चाहिए, और अभी कही गई विधि भी। "
                   "‘कारयितव्या’ प्रेरणार्थक कृत्य-रूप है: उससे कराया जाना चाहिए। "
                   "‘चेदेवम्’ में चेत् + एवम् है (स्वर से पहले त् → द्)।"),
    "hook": "न पलटे तो: बार-बार जम्हाई और टहलना।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 50, what is she made to do if the fetus does not turn?",
            ("Yawn and walk about, again and again", "मुहुर्मुहुर्जृम्भणं चङ्क्रमणं च कारयितव्या."),
            [("Lie still on her back and rest", "The unit names yawning and walking about."),
             ("Fast from all food and drink", "No fasting is named in unit 50."),
             ("Bathe again in hot water", "No bath is named in unit 50.")],
            "Yawning and walking about, repeatedly.",
            "जृम्भणं चङ्क्रमणं च."),
        order(1, "Put the sure parts of unit 50 in the line's order.",
              ["न चेदेवं परिवर्त्तते", "ततो मुहुर्मुहुः", "जृंभणं चंक्रमणं च", "कारयितव्या"],
              "If it does not turn thus, then again and again, yawning and walking about, she is to be made to do.",
              "न चेदेवं परिवर्त्तते → ततो मुहुर्मुहुः → जृंभणं चंक्रमणं च → कारयितव्या."),
        match(2, "Match each word of unit 50 to its meaning.",
              [["चेत्", "if"], ["जृम्भण", "yawning"], ["चङ्क्रमण", "walking about"],
               ["मुहुर्मुहुः", "again and again"], ["विधि", "procedure"]],
              "The condition and what she is to be made to do.",
              "चेत्, जृम्भण, चङ्क्रमण, मुहुर्मुहुः, विधि.", role="extend",
              teaches="चेत् = if; न चेत् = if not."),
        mcq("discriminate", 3, "Which split of चेदेवं is right?",
            ("चेत् + एवम्", "त् before a vowel becomes द्: चेत् + एवम् = चेदेवम्."),
            [("चे + देवम्", "चे is not a word, and देवम् (god) does not fit."),
             ("चेत + एवम्", "अ + ए would give ऐ (चेतैवम्)."),
             ("चेदे + वम्", "Neither part is a word.")],
            "चेत् (if) + एवम् (thus): त् → द् before a vowel.",
            "final त् + vowel → द् + vowel."),
        mcq("apply", 4, "In unit 50, what does कारयितव्या say about the woman?",
            ("She is to be made to do these things", "A causative gerundive: is to be made to do."),
            [("She has already done these things", "A gerundive is not past; it says what is to be done."),
             ("She must not do these things", "No न stands with कारयितव्या."),
             ("She makes the fetus do these things", "She herself is to be made to do them.")],
            "कारयितव्या = (she) is to be made to do.",
            "कारयितव्या: causative gerundive of √कृ."),
        mcq("transfer", 5, "By the rule of चेदेवम्, how is जगत् + ईशः (lord of the world) written?",
            ("जगदीशः", "त् before a vowel becomes द्."),
            [("जगतीशः", "Before a vowel the final त् becomes द्."),
             ("जगदिशः", "The long ई does not become short."),
             ("जगतेशः", "त् + ई does not give ते.")],
            "जगत् + ईशः = जगदीशः, like चेत् + एवम् = चेदेवम्.",
            "final त् + vowel → द्.",
            teaches="A word-final त् before a vowel becomes द्: चेत् + एवम् → चेदेवम्."),
    ],
}

# ---------------------------------------------------------------- unit 51
AUTHORED["51"] = {
    "title": "अन्ये तु ... आहनीयमित्याहुः",
    "question": "By unit 51, what do others say is to be done?",
    "rule": ("Others (अन्ये), however (तु), say (आहुः) that a mortar (उलूखल) filled with grain (धान्यपूर्ण) is to be "
             "struck (आहनीय) with a pestle (मुशल). इति closes the reported view."),
    "limits": ("The purpose is not stated in this unit; the kind of grain is not named. This is the others' view, not the "
               "author's; the next unit rejects it, but this unit does not judge it."),
    "explain_hi": ("दूसरे आचार्य (अन्ये) तो कहते हैं कि अनाज से भरी ओखली (उलूखल) पर मूसल (मुशल) से प्रहार करना चाहिए। "
                   "‘इति’ इस दूसरे मत के उद्धरण को समाप्त करता है, और ‘आहुः’ = वे कहते हैं। "
                   "प्रहार का उद्देश्य यहाँ नहीं बताया गया, और अनाज का प्रकार भी नहीं। "
                   "‘आहनीयम्’ कृत्य-रूप है: प्रहार किया जाना चाहिए। "
                   "‘इत्याहुः’ में इति + आहुः है (इ + आ → या)।"),
    "hook": "दूसरों का मत: अनाज-भरी ओखली पर मूसल मारो।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "By unit 51, what is to be struck, in the others' view?",
            ("A mortar filled with grain", "उलूखलं धान्यपूर्णम् आहनीयम्."),
            [("A drum beside her bed", "No drum is named."),
             ("The ground beside her bed", "The mortar is struck, not the ground."),
             ("A pot filled with water", "The mortar is filled with grain (धान्य).")],
            "A grain-filled mortar, struck with a pestle.",
            "मुशलेन उलूखलं धान्यपूर्णम् आहनीयम्."),
        order(1, "Put the words of unit 51 in the line's order.",
              ["अन्ये तु", "मुशलेन", "उलूखलम्", "धान्यपूर्णम्", "आहनीयम्", "इत्याहुः"],
              "Others however, with a pestle, a mortar, filled with grain, is to be struck, thus they say.",
              "अन्ये तु → मुशलेन → उलूखलम् → धान्यपूर्णम् → आहनीयम् → इत्याहुः."),
        match(2, "Match each word of unit 51 to its meaning.",
              [["मुशल", "pestle"], ["उलूखल", "mortar"], ["धान्य", "grain"], ["आहनीय", "to be struck"],
               ["आहुः", "they say"]],
              "Tool, vessel, filling, action and the reporting verb.",
              "मुशल, उलूखल, धान्य, आहनीय, आहुः.", role="extend",
              teaches="-अनीय makes a gerundive (is to be done): आहनीय = is to be struck."),
        mcq("discriminate", 3, "In unit 51, whose view is stated?",
            ("Others' view (अन्ये), reported with इति ... आहुः", "अन्ये तु ... इत्याहुः: others say."),
            [("The author's own instruction", "अन्ये तु marks it as the view of others."),
             ("The woman's own wish", "The woman's wish is not named."),
             ("A view this unit calls right", "This unit does not judge the view.")],
            "The view of others, quoted with इति and आहुः.",
            "अन्ये ... इति आहुः = others say ..."),
        mcq("apply", 4, "Which split of इत्याहुः is right?",
            ("इति + आहुः", "इ + a different vowel → य्: इति + आहुः = इत्याहुः."),
            [("इतिः + आहुः", "इति has no visarga; इः + आ would give इतिराहुः."),
             ("इते + आहुः", "ए + आ would not give या."),
             ("इत् + याहुः", "याहुः is not a word; the verb is आहुः.")],
            "इति (thus) + आहुः (they say).",
            "इ + आ → या."),
        mcq("transfer", 5, "By the -अनीय of आहनीयम्, what does करणीयम् mean, from √कृ (do)?",
            ("Is to be done", "-अनीय makes a gerundive: is to be done."),
            [("Was done already", "That would be the past participle कृतम्."),
             ("Doing it now", "That would be a present participle."),
             ("Having done it", "That would be the absolutive कृत्वा.")],
            "करणीयम् = is to be done, like आहनीयम् = is to be struck.",
            "-अनीय = gerundive (to be done).",
            teaches="The suffix -अनीय makes a gerundive, is to be done: आ-√हन् → आहनीय, √कृ → करणीय."),
    ],
}

# ===================================================================== NOTES_HI
NOTES_HI = {
    "39": ("गद्य-पंक्ति; विश्वास मध्यम; कोई पाठ-चिह्न नहीं। ‘फल’ द्रव्य, वर्ति रखने का स्थान और कर्ता नहीं बताए गए। छपा ‘विबंधे’ = "
           "विबन्धे। सन्धि जाँची: सु + अल्पे → स्वल्पे (उ + अ → व); स्वल्पे + अपि → स्वल्पेऽपि (ए + अ → एऽ); विट् + मूत्र → "
           "विण्मूत्र (अनुनासिक के पहले ट् → ण्; यह वैकल्पिक है, विड्मूत्र भी शुद्ध, इसलिए इस पर प्रश्न नहीं)।"),
    "40": ("विश्वास निम्न। पाठ-चिह्न: ‘वेदनोदरत्हृदय...’ → सम्भवतः वेदनोदरहृदय... (अतिरिक्त त्); ‘स्त्रवणानि’ → स्रवणानि। ‘वेदना’ और "
           "अंग-सूची का व्याकरणिक सम्बन्ध अनिश्चित; ‘योन्याः’ कितने शब्दों से जुड़ता है, तय नहीं (हिन्दी अनुवाद केवल स्राव से जोड़ता है, "
           "अंग्रेज़ी सब से)। इन पर प्रश्न नहीं। ‘निष्टीविका’ छपा रूप; थूक या अधिक लार। सन्धि जाँची: क्लमः + ग्लानिः → क्लमो ग्लानिः "
           "(अः + घोष → ओ); ग्लानिः + मुक्त → ग्लानिर्मुक्त; ‘मुक्तबन्धने इव’ में द्विवचन -ए प्रगृह्य है, इसलिए सन्धि नहीं; "
           "इव + अक्षिणी → इवाक्षिणी; अधः + गुरुत्वम् → अधोगुरुत्वम्; अन्न + अनभिलाषः → अन्नानभिलाषः; वेदना + उदर → वेदनोदर; "
           "योन्याः + भवन्ति → योन्या भवन्ति।"),
    "41": ("विश्वास मध्यम; कोई पाठ-चिह्न नहीं। आवी = प्रसव-पीड़ा (सम्भावित); गर्भोदक = उल्बद्रव (सम्भावित)। क्रिया नहीं, जोड़ी भी "
           "नहीं गई। छपा ‘तदनंतरम्’ = तदनन्तरम्। सन्धि जाँची: तदनन्तरम् + आवीनाम् → तदनन्तरमावीनाम्; प्रादुर्भावः + गर्भ... → "
           "प्रादुर्भावो गर्भ... (अः + घोष → ओ); गर्भ + उदक → गर्भोदक; प्रवाहः + च → प्रवाहश्च।"),
    "42": ("विश्वास मध्यम; कोई पाठ-चिह्न नहीं। पुंनामफल अज्ञात (अनिश्चित पहचान); अभ्यंग का तेल नामित नहीं। छपा ‘पुन्नाम’ = पुंनाम "
           "(द्वित्व न् छपाई की आदत)। ‘उपस्थितगर्भा’ = प्रसव निकट, यह व्याख्या है। सन्धि जाँची: अथ + एनाम् → अथैनाम् (अ + ए → ऐ); "
           "सु + अभ्यक्ताम् → स्वभ्यक्ताम् (उ + अ → व); स्वभ्यक्ताम् + उष्ण → स्वभ्यक्तामुष्ण; उष्ण + उदक → उष्णोदक।"),
    "43": ("विश्वास मध्यम। पाठ-चिह्न: ‘प्रजनकशलाः’ → सम्भवतः प्रजननकुशलाः (‘न’ और ‘कु’ लुप्त), अनुमानित, इसलिए इस पर प्रश्न नहीं। "
           "‘आभुग्नसक्थिपृष्ठाम्’ छपे रूप में लिया गया। सूतिका = प्रसव करती स्त्री (प्रसंग से)। सन्धि जाँची: सुरक्त + आर्षभ → "
           "सुरक्तार्षभ; शयानाम् + उत्तानाम् → शयानामुत्तानाम्; अहतवाससः + अशङ्कनीयाः → अहतवाससोऽशङ्कनीयाः (अः + अ → ओऽ); "
           "सूनृताभिः + वाणीभिः → सूनृताभिर्वाणीभिः; वाणीभिः + आश्वासयन्त्यः → वाणीभिराश्वासयन्त्यः।"),
    "44": ("विश्वास निम्न। पाठ-चिह्न: ‘च्यन्य’ अस्पष्ट (सम्भवतः चव्य, पक्का नहीं); ‘उपाघातुं’ → अनुमानित उपाघ्रातुम् (सूँघने को)। "
           "इन पर प्रश्न नहीं। पहचान: कुष्ठ = कूठ, एला = छोटी इलायची, लाङ्गली = कलिहारी, वचा = बच, चित्रक = चीता (सब मानक); "
           "चिरबिल्व = चिलबिल (सम्भावित)। छपाई में अनुस्वार वर्गीय नासिक्य के लिए (लांगली = लाङ्गली)। सन्धि जाँची: अथ + अस्यै → "
           "अथास्यै; कुष्ठ + एला → कुष्ठैला (अ + ए → ऐ); चूर्णम् + उपा... → चूर्णमुपा...; मुहुः + मुहुः → मुहुर्मुहुः।"),
    "45": ("विश्वास मध्यम; कोई पाठ-चिह्न नहीं। क्रिया नहीं; ‘दद्यात्’ पीछे से। छपे में ‘सर्ज’ और ‘रस’ अलग; ‘सर्जरस’ (साल का रस) "
           "व्याख्या है, ‘रस’ अलग द्रव्य भी हो सकता है। ‘शिशिपा’ छपा रूप; सामान्य रूप शिंशपा या शिशपा (शीशम)। पहचान: भूर्ज, शिशिपा, सर्ज "
           "मानक। सन्धि जाँची: रस + अन्यतम → रसान्यतम (अ + अ → आ); धूमम् + अन्तरान्तरा → धूममन्तरान्तरा।"),
    "46": ("विश्वास मध्यम। पाठ-चिह्न: ‘मृद्गीयात्’ कोई रूप नहीं → अनुमानित मृद्नीयात् (मले), इसलिए क्रिया पर प्रश्न नहीं। तेल नामित नहीं। "
           "सन्धि जाँची: देशान् + कोष्णेन → देशान्कोष्णेन (परिवर्तन नहीं); तैलेन + अभ्यज्य → तैलेनाभ्यज्य; अभ्यज्य + अनुसुखम् → "
           "अभ्यज्यानुसुखम्; अनुसुखम् + अस्याः → अनुसुखमस्याः; अस्याः + मृ... → अस्या मृ... (आः + घोष → आ, विसर्ग लुप्त; नियमित, छपाई-दोष नहीं)।"),
    "47": ("विश्वास उच्च; कोई पाठ-चिह्न नहीं। ‘अवाक्’ = नीचे की ओर (अव्यय); कौन-सा भाग आगे, कोई स्थिति नहीं कही। ‘एवम्’ = पिछली "
           "विधि (इकाई 44 से 46)। सन्धि जाँची: एवम् + अवाक् → एवमवाक् (स्वर से पहले म् बना रहता है)।"),
    "48": ("विश्वास उच्च; कोई पाठ-चिह्न नहीं। छपा ‘तस्यलक्षणं’ एक टोकन = तस्य लक्षणम्। GROUPING: यह छोटी इकाई अगली इकाई (49) की "
           "भूमिका है, जहाँ लक्षण कहा गया है; ‘तस्य’ सम्भवतः इकाई 47 का पलटना। ‘है’ समझा गया।"),
    "49": ("विश्वास उच्च। पाठ-चिह्न: ‘अवगृण्हाति’ → अवगृह्णाति (ह और ण का स्थान-परिवर्तन)। कर्ता (गर्भ) इकाई 47 से। बस्ति = मूत्राशय "
           "(सम्भावित); हृदय = हृदय (मानक)। सन्धि जाँची: हृदयम् + उदरम् → हृदयमुदरम्; उदरम् + आविशति → उदरमाविशति; बस्तिशिरः + "
           "अवगृह्णाति → बस्तिशिरोऽवगृह्णाति (अः + अ → ओऽ)।"),
    "50": ("विश्वास निम्न। पाठ-चिह्न: ‘त्वरयंत्येनामाढ्यः’ में ‘आढ्यः’ अस्पष्ट, अनसुलझा; ‘अनंतरोंक्तं’ में अतिरिक्त अनुस्वार → "
           "अनन्तरोक्तम्। छपा ‘परिवर्त्तते’ = परिवर्तते (द्वित्व त्त छपाई की आदत)। ‘कारयितव्या’ समझी गई ‘स्त्री’ से मेल खाता है। "
           "आरम्भ पर कोई प्रश्न नहीं। सन्धि जाँची: चेत् + एवम् → चेदेवम् (त् → द्); ततः + मुहुः → ततो मुहुः; मुहुः + जृम्भणम् → "
           "मुहुर्जृम्भणम्।"),
    "51": ("विश्वास उच्च; कोई पाठ-चिह्न नहीं। ‘मुशल’ = मुसल की वैकल्पिक वर्तनी। अनाज का प्रकार और उद्देश्य नहीं कहा; अगली इकाई इस मत का "
           "खंडन करती है। सन्धि जाँची: मुशलेन + उलूखलम् → मुशलेनोलूखलम् (अ + उ → ओ); धान्यपूर्णम् + आहनीयम् → "
           "धान्यपूर्णमाहनीयम्; आहनीयम् + इति → आहनीयमिति; इति + आहुः → इत्याहुः (इ + आ → या)।"),
}

# ===================================================================== AIDS
AIDS = {
    "39": {
        "chunks": "स्वल्पेऽपि च | विण्मूत्रविबंधे | फलवर्तीः प्रणिदध्यात्",
        "sandhi": "उ + अ → व: सु + अल्पे → स्वल्पे · ए + अ → एऽ: स्वल्पे + अपि → स्वल्पेऽपि।",
        "frame": "कब: स्वल्पे अपि विबन्धे (थोड़ी भी रुकावट में) → किसकी: विट्-मूत्र की → क्या: फलवर्तीः (कर्म) → क्रिया: प्रणिदध्यात् (रखे)।",
    },
    "40": {
        "diagram": {"groups": [
            {"label": "सामान्य लक्षण (क्रम से)", "items": ["क्लम (थकावट)", "ग्लानि", "आँखें मानो बन्धन-मुक्त",
                                                         "थूक, मूत्र, मल की अधिकता", "कुक्षि की शिथिलता",
                                                         "नीचे भारीपन", "अन्न में अरुचि"]},
            {"label": "वेदना आदि", "items": ["उदर, हृदय, कटि, बस्ति, वंक्षण में वेदना",
                                            "तोद, भेद, शूल, स्फुरण, स्राव"]}]},
        "chunks": "तत्रासन्नप्रसवायाः | क्लमो ग्लानिः | मुक्तबंधने इवाक्षिणी | निष्टीविकामूत्रपुरीषबाहुल्यं | "
                  "शिथिलकुक्षिताऽधोगुरुत्वमन्नानभिलाषो | वेदनोदरत्हृदयकटीबस्तिवंक्षणेषु | तोदभेदशूलस्फुरणस्त्रवणानि च योन्याभवंति",
        "sandhi": "अः + घोष → ओ: क्लमः + ग्लानिः → क्लमो ग्लानिः · अ + अ → आ: अन्न + अनभिलाषः → अन्नानभिलाषः · "
                  "द्विवचन -ए के बाद सन्धि नहीं: मुक्तबन्धने इव।",
        "contrast": "उलटे से याद: भूख नहीं (अन्नानभिलाष), हल्कापन नहीं, नीचे भार (अधोगुरुत्व), कसाव नहीं, कुक्षि ढीली (शिथिलकुक्षिता)। (मेरी याद-पद्धति)",
    },
    "41": {
        "chunks": "तदनंतरम् | आवीनां प्रादुर्भावो | गर्भोदकप्रवाहश्च",
        "sandhi": "अ + उ → ओ: गर्भ + उदक → गर्भोदक · अः + घोष → ओ: प्रादुर्भावः + गर्भ... → प्रादुर्भावो गर्भ...",
        "frame": "समय: तदनन्तरम् → १ आवियों (सम्भवतः प्रसव-पीड़ा) का प्रादुर्भाव, २ गर्भोदक (सम्भवतः उल्बद्रव) का प्रवाह। क्रिया नहीं।",
    },
    "42": {
        "diagram": {"groups": [
            {"label": "उसका वर्णन (क्रम से)", "items": ["उपस्थितगर्भा", "कौतुक-मंगल किए हुए", "हाथ में पुंनामफल (अज्ञात)",
                                                     "भली-भाँति अभ्यक्त", "गर्म जल से परिषिक्त"]},
            {"label": "क्रिया", "items": ["सघृत यवागू पिलाए"]}]},
        "chunks": "अथैनामुपस्थितगर्भां | कृतकौतुकमंगलां | पुन्नामफलहस्तां | स्वभ्यक्तामुष्णोदकपरिषिक्तां | सघृतां यवागूं पाययेत्",
        "sandhi": "अ + ए → ऐ: अथ + एनाम् → अथैनाम् · उ + अ → व: सु + अभ्यक्ताम् → स्वभ्यक्ताम् · अ + उ → ओ: उष्ण + उदक → उष्णोदक।",
        "letters": "पाँच विशेषणों के पहले अक्षर क्रम से: उ-कृ-पु-स्व-उ (उपस्थितगर्भा, कृतकौतुकमङ्गला, पुंनामफलहस्ता, स्वभ्यक्ता, उष्णोदकपरिषिक्ता)। (मेरी याद-पद्धति)",
    },
    "43": {
        "diagram": {"groups": [
            {"label": "शय्या और स्थिति", "items": ["कोमल भूमि-शय्या", "बहुत लाल बैल-चर्म का आच्छादन", "लेटी, उत्तान",
                                                 "जाँघें और पीठ मुड़ी"]},
            {"label": "परिचारिकाएँ", "items": ["नए वस्त्र", "अशंकनीय (विश्वसनीय)", "प्रियदर्शना", "प्रौढ़ आयु",
                                             "प्रसव-कुशल (अनुमानित पाठ)", "प्रगल्भ (निर्भीक)", "कटे नख",
                                             "मधुर-सत्य वाणी से आश्वासन"]}]},
        "chunks": "ततः सुरक्तार्षभचर्मप्रच्छदे मृदुनि भूमिशयने | शयानामुत्तानामाभुग्नसक्थिपृष्ठाम् | "
                  "अहतवाससोऽशंकनीयाः प्रियदर्शनाः परिणतवयसः प्रजनकशलाः प्रगल्भाः कृत्तनखाः स्त्रियः | "
                  "सूतिकां सूनृताभिर्वाणीभिराश्वासयंत्यः पर्युपासीरन्",
        "sandhi": "अः + अ → ओऽ: अहतवाससः + अशङ्कनीयाः → अहतवाससोऽशङ्कनीयाः · ई के बाद विसर्ग → र्: सूनृताभिः + वाणीभिः → "
                  "सूनृताभिर्वाणीभिः, वाणीभिः + आश्वासयन्त्यः → वाणीभिराश्वासयन्त्यः।",
        "frame": "कर्ता: स्त्रियः (विशेषण-सूची के साथ) → कर्म: सूतिकाम् (शय्या, स्थिति सहित) → साधन: सूनृताभिः वाणीभिः → क्रिया: पर्युपासीरन् (घेरकर सेवा करें)।",
    },
    "44": {
        "diagram": {"groups": [
            {"label": "चूर्ण के द्रव्य (क्रम से)", "items": ["कुष्ठ: कूठ (मानक)", "एला: छोटी इलायची (मानक)",
                                                          "लाङ्गली: कलिहारी (मानक)", "वचा: बच (मानक)", "च्यन्य: अस्पष्ट",
                                                          "चित्रक: चीता (मानक)", "चिरबिल्व: चिलबिल (सम्भावित)"]}]},
        "chunks": "अथास्यै दद्यात् | कुष्ठैलालांगलीवचाच्यन्यचित्रकचिरबिल्वचूर्णम् | उपाघातुं (?) मुहुर्मुहुः",
        "sandhi": "अ + ए → ऐ: कुष्ठ + एला → कुष्ठैला · अ + अ → आ: अथ + अस्यै → अथास्यै।",
        "letters": "सात द्रव्यों के पहले अक्षर क्रम से: कु-ए-ला-व-च्य-चि-चि (च्य अस्पष्ट शब्द)। (मेरी याद-पद्धति)",
    },
    "45": {
        "chunks": "तथा | भूर्जपत्रशिशिपासर्ज रसान्यतमधूमम् | अंतरांतरा च",
        "sandhi": "अ + अ → आ: रस + अन्यतम → रसान्यतम।",
        "frame": "किसका धूम: भूर्जपत्र / शिशिपा / सर्ज-रस, इनमें से अन्यतम (कोई एक) → कब: अन्तरान्तरा (बीच-बीच में) → क्रिया: पीछे से (दद्यात्)।",
    },
    "46": {
        "chain": {"steps": ["गुनगुना (कोष्ण) तेल", "पार्श्व, पीठ, कटि, जाँघ पर अभ्यंग (अभ्यज्य)",
                            "सुखपूर्वक मर्दन (अनुमानित पाठ: मृद्नीयात्)"]},
        "chunks": "पार्श्वपृष्ठकटीसक्थिदेशान् | कोष्णेन तैलेनाभ्यज्य | अनुसुखमस्या मृद्गीयात्",
        "sandhi": "अ + अ → आ: तैलेन + अभ्यज्य → तैलेनाभ्यज्य · आः + घोष → आ: अस्याः + मृ... → अस्या मृ...",
        "letters": "चार प्रदेश क्रम से: पा-पृ-क-स (पार्श्व, पृष्ठ, कटी, सक्थि)। (मेरी याद-पद्धति)",
    },
    "47": {
        "chunks": "एवमवाक् | परिवर्तते गर्भः",
        "sandhi": "स्वर से पहले म् बना रहता है: एवम् + अवाक् → एवमवाक्।",
        "anchors": "याद-सूत्र: ‘अवाक्’ = अव (नीचे) की ओर; विधि का फल: गर्भ नीचे पलटे। (मेरी याद-पद्धति)",
    },
    "48": {
        "chunks": "तस्य | लक्षणम्",
        "frame": "किसका: तस्य (षष्ठी, सम्भवतः पलटने का) → क्या: लक्षणम्; क्रिया ‘है’ समझी जाती है।",
        "anchors": "याद-सूत्र: ‘तस्य लक्षणम्’ = शीर्षक; लक्षण अगली इकाई में। (मेरी याद-पद्धति)",
    },
    "49": {
        "chain": {"steps": ["हृदय को छोड़कर (विमुच्य)", "उदर में प्रवेश (आविशति)",
                            "बस्ति-शिर को पकड़ना (बस्ति: सम्भावित मूत्राशय)"]},
        "chunks": "विमुच्य हृदयम् | उदरमाविशति | बस्तिशिरोऽवगृण्हाति",
        "sandhi": "अः + अ → ओऽ: बस्तिशिरः + अवगृह्णाति → बस्तिशिरोऽवगृह्णाति · स्वर से पहले म्: हृदयम् + उदरम् → हृदयमुदरम्।",
    },
    "50": {
        "diagram": {"groups": [
            {"label": "शर्त", "items": ["यदि ऐसे न पलटे (न चेदेवं परिवर्तते)"]},
            {"label": "तब कराएँ", "items": ["बार-बार जृम्भण (जम्हाई)", "बार-बार चङ्क्रमण (टहलना)", "अभी कही गई विधि"]}]},
        "chunks": "त्वरयंत्येनामाढ्यः (?) | न चेदेवं परिवर्त्तते | ततो मुहुर्मुहुर्जृंभणं चंक्रमणं च | कारयितव्याऽनंतरोंक्तं विधिं",
        "sandhi": "त् + स्वर → द्: चेत् + एवम् → चेदेवम् · अः + घोष → ओ: ततः + मुहुः → ततो मुहुः।",
    },
    "51": {
        "chunks": "अन्ये तु | मुशलेनोलूखलं | धान्यपूर्णमाहनीयम् | इत्याहुः",
        "sandhi": "अ + उ → ओ: मुशलेन + उलूखलम् → मुशलेनोलूखलम् · इ + आ → या: इति + आहुः → इत्याहुः।",
        "frame": "कौन कहते: अन्ये (दूसरे) → साधन: मुशलेन → कर्म: उलूखलं धान्यपूर्णम् → कृत्य: आहनीयम् → इति आहुः (ऐसा कहते हैं)।",
    },
}

# ===================================================================== IMAGE_SPECS
IMAGE_SPECS = {
    ("40", "diagram"): {
        "file": "sh3-asanna-prasava-40.svg",
        "alt": ("Two columns of unit 40, signs of near delivery. General signs in order: exhaustion, weariness, eyes as if "
                "loosened, much spitting, urine and stool, loose belly, heaviness below, no desire for food. Pains: pain in "
                "belly, heart, waist, bladder and groin; pricking, tearing, pain, throbbing and flow."),
        "type": "split",
        "title": "इकाई ४०: आसन्न प्रसव के लक्षण",
        "cols": [["सामान्य लक्षण (क्रम से)", ["१ क्लम (थकावट)", "२ ग्लानि", "३ आँखें मानो बन्धन-मुक्त",
                                            "४ थूक, मूत्र, मल अधिक", "५ कुक्षि शिथिल", "६ नीचे भारीपन",
                                            "७ अन्न में अरुचि"]],
                 ["वेदना आदि", ["उदर, हृदय, कटि, बस्ति, वंक्षण में वेदना", "तोद, भेद, शूल, स्फुरण, स्राव"]]],
    },
    ("42", "diagram"): {
        "file": "sh3-saghrita-yavagu-42.svg",
        "alt": ("Table of unit 42 in line order: her five descriptions (embryo come forward; kautuka and auspicious rites "
                "done; a male-named, unidentified fruit in hand; well anointed; sprinkled with hot water), then the action: "
                "make her drink gruel with ghee."),
        "type": "table",
        "title": "इकाई ४२: सघृत यवागू",
        "heads": ["छपा शब्द", "अर्थ"],
        "rows": [["उपस्थितगर्भां", "जिसका गर्भ उपस्थित हो"],
                 ["कृतकौतुकमंगलां", "कौतुक-मंगल किए हुए"],
                 ["पुन्नामफलहस्तां", "हाथ में पुंनामफल (अज्ञात)"],
                 ["स्वभ्यक्तां", "भली-भाँति अभ्यक्त"],
                 ["उष्णोदकपरिषिक्तां", "गर्म जल से सींची"],
                 ["सघृतां यवागूं पाययेत्", "घी सहित यवागू पिलाए"]],
    },
    ("43", "diagram"): {
        "file": "sh3-sutika-paricharika-43.svg",
        "alt": ("Two columns of unit 43. Bed and posture: soft ground-bed, covered with a very red bull's hide, lying face "
                "up, thighs and back bent. Attending women: new clothes, trustworthy, pleasant to see, older, skilled in "
                "delivery (conjectural reading), bold, nails cut, comforting with pleasant true words."),
        "type": "split",
        "title": "इकाई ४३: शय्या और परिचारिकाएँ",
        "cols": [["शय्या और स्थिति", ["कोमल भूमि-शय्या", "लाल बैल-चर्म का आच्छादन", "लेटी, उत्तान",
                                    "जाँघें और पीठ मुड़ी"]],
                 ["परिचारिकाएँ (क्रम से)", ["१ नए वस्त्र", "२ अशंकनीय", "३ प्रियदर्शना", "४ प्रौढ़ आयु",
                                          "५ प्रसव-कुशल (अनुमानित)", "६ प्रगल्भ", "७ कटे नख",
                                          "मधुर-सत्य वाणी से आश्वासन"]]],
    },
    ("44", "diagram"): {
        "file": "sh3-churna-dravya-44.svg",
        "alt": ("Table of unit 44, the drugs of the powder in line order with the identification labels of the data: "
                "kuṣṭha costus (standard), elā small cardamom (standard), lāṅgalī glory lily (standard), vacā sweet flag "
                "(standard), cyanya unclear, citraka leadwort (standard), cirabilva Indian elm (probable)."),
        "type": "table",
        "title": "इकाई ४४: चूर्ण के द्रव्य",
        "heads": ["द्रव्य (क्रम से)", "पहचान"],
        "rows": [["कुष्ठ", "कूठ (मानक)"], ["एला", "छोटी इलायची (मानक)"], ["लाङ्गली", "कलिहारी (मानक)"],
                 ["वचा", "बच (मानक)"], ["च्यन्य", "अस्पष्ट शब्द"], ["चित्रक", "चीता (मानक)"],
                 ["चिरबिल्व", "चिलबिल (सम्भावित)"]],
    },
    ("46", "chain"): {
        "file": "sh3-koshna-taila-46.svg",
        "alt": ("Chain of unit 46: lukewarm oil; anointing the sides, back, waist and thighs; then comfortable rubbing "
                "(a conjectural reading of the verb)."),
        "type": "chain",
        "title": "इकाई ४६: कोष्ण तैल से अभ्यंग",
        "steps": ["गुनगुना (कोष्ण) तेल", "पार्श्व, पीठ, कटि, जाँघ पर अभ्यंग", "सुखपूर्वक मर्दन (अनुमानित पाठ)"],
    },
    ("49", "chain"): {
        "file": "sh3-garbha-avatarana-49.svg",
        "alt": ("Chain of unit 49: having left the heart, it enters the belly, and takes hold of the head of the bladder "
                "(basti, probably the bladder)."),
        "type": "chain",
        "title": "इकाई ४९: पलटने का लक्षण",
        "steps": ["हृदय को छोड़कर", "उदर में प्रवेश", "बस्ति-शिर को पकड़ना (बस्ति: सम्भावित मूत्राशय)"],
    },
    ("50", "diagram"): {
        "file": "sh3-na-parivartate-50.svg",
        "alt": ("Flowchart of unit 50: if the fetus does not turn in this way, then she is to be made to do yawning and "
                "walking about again and again, and the procedure stated just before."),
        "type": "mermaid",
        "code": ("flowchart TD\n"
                 "  A[\"यदि ऐसे न पलटे\"] --> B[\"तब कराएँ\"]\n"
                 "  B --> M[\"बार-बार\"]\n"
                 "  M --> C[\"१ जृम्भण (जम्हाई)\"]\n"
                 "  M --> D[\"२ चङ्क्रमण (टहलना)\"]\n"
                 "  B --> E[\"३ अभी कही विधि\"]\n"),
    },
}
