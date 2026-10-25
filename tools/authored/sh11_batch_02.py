from helpers import mcq, match, order, fill, multi, accepts


def T(q, teaches):
    q["teaches"] = teaches
    return q


AUTHORED = {}

# ---------------------------------------------------------------- unit 14
AUTHORED["14"] = {
    "title": "अति रक्तासितस्निग्ध",
    "question": "By card 14, which qualities does line 2 list after अति (very)?",
    "rule": ("Line 2: very (अति) red (रक्त), black (असित), unctuous (स्निग्ध), putrid (पूति), clear (अच्छ), thick (घन), "
             "with pain (वेदन). Line 1 continues card 13's instrumental list: soot (मषी), pus (पूय), honey (माक्षिक) and others."),
    "limits": ("Continues card 13; the noun described (probably the stool) is not stated. मस्तुलुङ्ग (brain-matter, probable) "
               "is a conjecture; अम्बु and वेसवार rest on text flags: no question on these. अति may be a compound member; "
               "घनवेदन may mean 'intense pain'."),
    "explain_hi": ("यह इकाई कार्ड १३ के अतिसार-वर्णन की सूची को आगे बढ़ाती है। "
                   "पहली पंक्ति तृतीया बहुवचन की सूची है: मषी (कालिख), पूय (मवाद), माक्षिक (शहद) आदि; ‘मस्तु लुंग’ को मस्तुलुङ्ग (सम्भवतः मस्तिष्क का पदार्थ) पढ़ना अनुमान है। "
                   "दूसरी पंक्ति गुण गिनाती है: अति (बहुत) लाल, काला, चिकना, सड़ा हुआ, स्वच्छ, घना और पीड़ा वाला। "
                   "किसका वर्णन है, यह छपा नहीं; डेटा इसे सम्भवतः मल मानता है। "
                   "‘पूत्यच्छ’ में पूति + अच्छ की सन्धि है (इ + अ → य)।"),
    "hook": "लाल, काला, चिकना, सड़ा, स्वच्छ, घना: एक ही समास में सात गुण।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "In card 14, what does असित mean?",
            ("Black", "असित = not white, i.e. black: रक्तासित = red, black."),
            [("White", "White is सित; असित is its negation, black."),
             ("Green", "Green would be हरित; असित = black."),
             ("Yellow", "Yellow would be पीत; असित = black.")],
            "असित = black.",
            "अ + सित (white) = असित, black."),
        match(1, "Match each word of card 14, line 2, to its meaning.",
              [["रक्त", "red"], ["असित", "black"], ["स्निग्ध", "unctuous, oily"], ["पूति", "putrid"], ["अच्छ", "clear"]],
              "रक्त = red, असित = black, स्निग्ध = unctuous, पूति = putrid, अच्छ = clear.",
              "रक्त, असित, स्निग्ध, पूति, अच्छ."),
        order(2, "Put these members of the long compound in card 14, line 2, in the printed order.",
              ["रक्त", "असित", "स्निग्ध", "पूति", "अच्छ", "घन"],
              "Red, black, unctuous, putrid, clear, thick; वेदन (pain) closes the compound.",
              "रक्त → असित → स्निग्ध → पूति → अच्छ → घन.",
              role="extend",
              teaches="One long compound can string many qualities in a row; the printed order is the order of its members."),
        mcq("discriminate", 3, "One word is wrong in this English of card 14, line 2: 'Very red, black, dry, putrid, clear, thick, with pain'. Which?",
            ("dry", "स्निग्ध means unctuous, oily: the opposite of dry."),
            [("black", "असित = black: this word is right."),
             ("putrid", "पूति = putrid: this word is right."),
             ("clear", "अच्छ = clear: this word is right.")],
            "स्निग्ध = unctuous, not dry.",
            "स्निग्ध = unctuous, oily."),
        mcq("apply", 4, "Which split of पूत्यच्छ in card 14 is right?",
            ("पूति + अच्छ", "इ before a different vowel → य्: पूति + अच्छ → पूत्यच्छ."),
            [("पूत्य + अच्छ", "अ + अ → आ: that would print पूत्याच्छ."),
             ("पूते + अच्छ", "ए + अ gives एऽ: that would print पूतेऽच्छ."),
             ("पूति + इच्छ", "इ + इ → ई: that would print पूतीच्छ.")],
            "पूति (putrid) + अच्छ (clear): इ + अ → य.",
            "इ + unlike vowel → य् + that vowel."),
        mcq("transfer", 5, "By the pattern of पूति + अच्छ → पूत्यच्छ, how is गिरि + अग्रम् (the top of a hill) joined in a new example?",
            ("गिर्यग्रम्", "इ + अ → य: गिरि + अग्रम् → गिर्यग्रम्."),
            [("गिर्याग्रम्", "या would need इ + आ; here the vowel is short अ."),
             ("गिरेग्रम्", "ए comes from अ + इ, not from इ + अ."),
             ("गिरीग्रम्", "ई comes from इ + इ, not from इ + अ.")],
            "गिरि + अग्रम् = गिर्यग्रम्, like पूति + अच्छ = पूत्यच्छ.",
            "इ + अ → य.",
            teaches="इ before a different vowel becomes य्: पूति + अच्छ → पूत्यच्छ."),
    ],
}

# ---------------------------------------------------------------- unit 15
AUTHORED["15"] = {
    "title": "कर्बुरः तंतुमान्",
    "question": "Which sure words of card 15 describe what is passed, and which parts stay unclear?",
    "rule": ("Sure words: mottled (कर्बुरः); or else (अथवा) with excessive faeces (अतिविट्); fibrous (तन्तुमान्); overspread "
             "with soot-specks (मसिकाक्रान्तः); joined with (युतः) an unclear item."),
    "limits": ("Prose, low confidence, damaged print. प्रस्रवन्धात्त्रिष्पूरीषः and राजैर्मांसेंद्रकैः are unclear (a निष्पुरीष reading "
               "is not adopted): no question on them or on what it is joined with. मसिका is a s/ṣ print habit for मषिका. "
               "The data takes the description as of the stool (cards 13 to 15)."),
    "explain_hi": ("यह गद्य इकाई क्षतिग्रस्त छपाई की है, विश्वास कम है। "
                   "पक्के शब्द: कर्बुर (चितकबरा), अथवा अतिविट् (या बहुत अधिक मल वाला), तन्तुमान् (तन्तुओं वाला), मसिकाक्रान्त (कालिख के कणों से आक्रान्त) और युत (युक्त)। "
                   "‘प्रस्रवन्धात्त्रिष्पूरीषो’ और ‘राजैर्मांसेंद्रकैर्’ अस्पष्ट हैं, इसलिए उन पर प्रश्न नहीं। "
                   "डेटा इसे कार्ड १३ से चल रहे मल के वर्णन का भाग मानता है। "
                   "‘तन्तुमान्’ में -मत् प्रत्यय ‘वाला’ का अर्थ देता है।"),
    "hook": "चितकबरा, तन्तुओं वाला, कालिख के कणों से भरा: बाकी शब्द अस्पष्ट।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "In card 15, what does कर्बुर mean?",
            ("Mottled", "कर्बुर = mottled, variegated."),
            [("Shining", "Shining would be from √भा or √दीप्; कर्बुर = mottled."),
             ("Frothy", "Frothy would be फेनिल; कर्बुर = mottled."),
             ("Smooth", "Smooth would be श्लक्ष्ण; कर्बुर = mottled.")],
            "कर्बुर = mottled.",
            "कर्बुर = mottled, variegated."),
        match(1, "Match each sure word of card 15 to its meaning.",
              [["कर्बुर", "mottled"], ["अतिविट्", "with excessive faeces"], ["तन्तुमान्", "fibrous"],
               ["आक्रान्त", "overspread"], ["युत", "joined with"]],
              "कर्बुर = mottled, अतिविट् = with excessive faeces, तन्तुमान् = fibrous, आक्रान्त = overspread, युत = joined with.",
              "कर्बुर, अतिविट्, तन्तुमान्, आक्रान्त, युत."),
        order(2, "Put these sure words of card 15 in the printed order.",
              ["कर्बुरः", "अथवा", "अतिविट्", "तंतुमान्", "मसिकाक्रांतो", "युतः"],
              "Line 1: mottled ... or else with excessive faeces; line 2: fibrous, overspread with soot-specks, joined with.",
              "कर्बुरः → अथवा → अतिविट् → तंतुमान् → मसिकाक्रांतो → युतः.",
              role="extend",
              teaches="अथवा (or else) offers an alternative description inside a list."),
        mcq("discriminate", 3, "Which split of अथवाऽतिविट् in card 15 is right?",
            ("अथवा + अतिविट्", "आ + अ → आ: अथवा + अतिविट् → अथवातिविट्; the ऽ after आ is a print habit."),
            [("अथवा + इतिविट्", "आ + इ → ए: that would print अथवेतिविट्."),
             ("अथवः + अतिविट्", "अः + अ → ओऽ: that would print अथवोऽतिविट्."),
             ("अथवे + अतिविट्", "ए + अ → एऽ: that would print अथवेऽतिविट्.")],
            "अथवा (or else) + अतिविट् (with excessive faeces).",
            "आ + अ → आ."),
        multi("apply", 4, "Which printed stretches of card 15 does the data leave unclear?",
              [("प्रस्रवन्धात्त्रिष्पूरीषो", "Right: it does not parse and is left unsplit and unclear."),
               ("कर्बुरः", "No: कर्बुरः is a sure word, mottled."),
               ("राजैर्मांसेंद्रकैर्", "Right: these two words give no sure sense and are left unclear."),
               ("तंतुमान्", "No: तन्तुमान् is a sure word, fibrous.")],
              [0, 2],
              "Two stretches are unclear; कर्बुरः and तन्तुमान् are sure.",
              "Build on the sure words only."),
        mcq("transfer", 5, "By the pattern of तन्तुमान् (having threads), what does शक्तिमान् mean in a new example?",
            ("Having power", "-मत् (nom. -मान्) = having: शक्ति (power) + मत् = having power."),
            [("Without power", "Without would need a prefix such as निः- or अ-; -मान् means having."),
             ("Made of power", "Made of would be -मय; -मान् means having."),
             ("Giver of power", "Giver would be -द or -दाता; -मान् means having.")],
            "शक्तिमान् = having power, like तन्तुमान् = having threads.",
            "-मत् (nom. m. sg. -मान्) = having.",
            teaches="The suffix -मत् (nominative masculine -मान्) means 'having': तन्तु + मत् → तन्तुमान्, fibrous."),
    ],
}

# ---------------------------------------------------------------- unit 16
AUTHORED["16"] = {
    "title": "पर्वास्थिशूलिनं स्रस्तपायुं",
    "question": "By card 16, which sure features of the patient are given?",
    "rule": ("Accusative descriptions of the patient: pain in the joints and bones (पर्वास्थिशूलिनम्), a slipped anus "
             "(स्रस्तपायुम्, probably prolapse), wasted in strength (बलक्षीणम्). The verb is carried over."),
    "limits": ("Prose, low confidence. वलि (fold) for printed वालि is conjectural, the sense of नाल (stalk) is not stated, and "
               "अन्नेवोपवेशयन् is unclear: no question on them. Prolapse is only probable. The data takes the list as "
               "continuing card 15."),
    "explain_hi": ("यह गद्य इकाई रोगी के लिए द्वितीया के विशेषण देती है; क्रिया पहले से चली आ रही है, यहाँ नहीं छपी। "
                   "पक्के अंश: पर्वास्थिशूली (जोड़ों और हड्डियों में शूल वाला), स्रस्तपायु (गुदा खिसकी हुई, सम्भवतः गुदभ्रंश) और बलक्षीण (बल से क्षीण)। "
                   "‘वालि’ को ‘वलि’ (तह) पढ़ना अनुमान है, ‘नाल’ का अर्थ यहाँ स्पष्ट नहीं, और अन्तिम शब्द अस्पष्ट है; इन पर प्रश्न नहीं। "
                   "‘शूलिन्’ में -इन् प्रत्यय ‘वाला’ का अर्थ देता है।"),
    "hook": "जोड़-हड्डी में शूल, गुदा खिसकी, बल क्षीण: तीन पक्के लक्षण।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "In card 16, what does बलक्षीण mean?",
            ("Wasted in strength", "बल (strength) + क्षीण (wasted): wasted in strength."),
            [("Strong in his body", "That is the opposite: क्षीण means wasted."),
             ("Quick to grow angry", "Nothing in बलक्षीण names anger."),
             ("Heavy in his limbs", "Heaviness would be गुरु; क्षीण means wasted.")],
            "बलक्षीण = wasted in strength.",
            "क्षीण = wasted."),
        match(1, "Match each sure word part of card 16 to its meaning.",
              [["पर्व", "joint"], ["अस्थि", "bone"], ["शूलिन्", "having pain"], ["स्रस्त", "slipped"], ["क्षीण", "wasted"]],
              "पर्व = joint, अस्थि = bone, शूलिन् = having pain, स्रस्त = slipped, क्षीण = wasted.",
              "पर्व, अस्थि, शूलिन्, स्रस्त, क्षीण."),
        order(2, "Put these printed words of card 16 in the printed order.",
              ["शीर्णपायुवालिं", "मुक्तनालं", "पर्वास्थिशूलिनं", "स्रस्तपायुं", "बलक्षीणम्"],
              "Line 1: withered folds (conjectural), released stalk, pain of joints and bones; line 2: slipped anus, wasted in strength.",
              "शीर्णपायुवालिं → मुक्तनालं → पर्वास्थिशूलिनं → स्रस्तपायुं → बलक्षीणम्.",
              role="extend",
              teaches="A row of accusative bahuvrīhis describes one patient, the object of a verb carried over."),
        mcq("discriminate", 3, "Which split of पर्वास्थि in card 16 is right?",
            ("पर्व + अस्थि", "अ + अ → आ: पर्व + अस्थि → पर्वास्थि."),
            [("पर्वे + अस्थि", "ए + अ → एऽ: that would print पर्वेऽस्थि."),
             ("पर्वि + अस्थि", "इ + अ → य: that would print पर्व्यस्थि."),
             ("पर्वो + अस्थि", "ओ + अ → ओऽ: that would print पर्वोऽस्थि.")],
            "पर्व (joint) + अस्थि (bone): अ + अ → आ.",
            "अ + अ → आ."),
        mcq("apply", 4, "In card 16, who is called स्रस्तपायु?",
            ("One whose anus has slipped", "स्रस्त (slipped) + पायु (anus): probably prolapse of the anus or rectum."),
            [("One whose bones are broken", "Bones appear in पर्वास्थिशूलिन्, as painful, not broken."),
             ("One whose urine is held up", "Nothing in स्रस्तपायु names urine."),
             ("One whose eyes are swollen", "Nothing in स्रस्तपायु names the eyes.")],
            "स्रस्तपायु = one with a slipped anus (prolapse, probable).",
            "स्रस्त = slipped; पायु = anus."),
        mcq("transfer", 5, "By the pattern of शूलिन् (having pain, from शूल), what does धनिन् (from धन, wealth) mean in a new example?",
            ("Having wealth", "-इन् = having: धन + इन् = having wealth."),
            [("Without wealth", "Without would need निर्- or अ-; -इन् means having."),
             ("Made of wealth", "Made of would be -मय; -इन् means having."),
             ("Giver of wealth", "Giver would be -द or -दाता; -इन् means having.")],
            "धनिन् = having wealth, like शूलिन् = having pain.",
            "-इन् = having.",
            teaches="The suffix -इन् means 'having': शूल + इन् → शूलिन्, having pain."),
    ],
}

# ---------------------------------------------------------------- unit 17
AUTHORED["17"] = {
    "title": "अश्मरी शूनवृषणं",
    "question": "By card 17, which features of the patient go with aśmarī (urinary stone)?",
    "rule": ("Line 2 names aśmarī (urinary stone, standard) and, in the accusative, the patient: swollen testicles "
             "(शूनवृषणम्), obstructed urine (बद्धमूत्रम्), afflicted by pain (रुजार्दितम्). The verb is carried over (data: from card 4)."),
    "limits": ("Low confidence. Line 1 (thirst, cough, fever ... pravāhikā) rests on an emendation of printed सतृट्का मज्वर-: no "
               "question on line 1. The data takes it as describing the diarrhoea of cards 13 to 16; pravāhikā (dysentery) is probable."),
    "explain_hi": ("पहली पंक्ति अनुमानित पाठ पर प्यास, खाँसी, ज्वर, उल्टी, दाह, आनाह और प्रवाहिका गिनाती है; छपा ‘सतृट्का मज्वर’ ठीक नहीं बैठता, इसलिए उस पर प्रश्न नहीं। "
                   "दूसरी पंक्ति अश्मरी (मूत्र की पथरी, मानक) का नाम लेती है। "
                   "रोगी के लिए द्वितीया के तीन विशेषण: सूजे वृषण वाला, रुके मूत्र वाला और पीड़ा से पीड़ित। "
                   "क्रिया यहाँ नहीं छपी; डेटा के अनुसार वह कार्ड ४ से चली आ रही है। "
                   "‘रुजार्दितम्’ में रुजा + अर्दितम् की सन्धि है (आ + अ → आ)।"),
    "hook": "अश्मरी: सूजे वृषण, रुका मूत्र, पीड़ा।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "In card 17, what is अश्मरी?",
            ("A urinary stone", "अश्मरी = urinary stone (standard)."),
            [("A boil on skin", "Boils are पिटका / पिटिका, not अश्मरी."),
             ("A nasal catarrh", "Nasal catarrh is पीनस, not अश्मरी."),
             ("A belly swelling", "अश्मरी is a stone of the urinary tract, not a belly swelling.")],
            "अश्मरी = urinary stone.",
            "अश्मरी = urinary stone (standard)."),
        match(1, "Match each word part of card 17, line 2, to its meaning.",
              [["शून", "swollen"], ["वृषण", "testicle"], ["बद्ध", "obstructed"], ["रुजा", "pain"], ["अर्दित", "afflicted"]],
              "शून = swollen, वृषण = testicle, बद्ध = obstructed, रुजा = pain, अर्दित = afflicted.",
              "शून, वृषण, बद्ध, रुजा, अर्दित."),
        order(2, "Put the words of card 17, line 2, in the printed order.",
              ["अश्मरी", "शूनवृषणं", "बद्धमूत्रं", "रुजार्दितं"],
              "Aśmarī; the patient with swollen testicles, with obstructed urine, afflicted by pain.",
              "अश्मरी → शूनवृषणं → बद्धमूत्रं → रुजार्दितं.",
              role="extend",
              teaches="A disease name in the nominative is followed by accusative descriptions of the patient it affects."),
        mcq("discriminate", 3, "Which split of रुजार्दितं in card 17 is right?",
            ("रुजा + अर्दितम्", "आ + अ → आ: रुजा + अर्दितम् → रुजार्दितम्."),
            [("रुजे + अर्दितम्", "ए + अ → एऽ: that would print रुजेऽर्दितम्."),
             ("रुजा + र्दितम्", "र्दितम् is not a word; the र् belongs to अर्दितम्."),
             ("रुजौ + अर्दितम्", "औ + अ → आव: that would print रुजावर्दितम्.")],
            "रुजा (by pain) + अर्दितम् (afflicted).",
            "आ + अ → आ."),
        mcq("apply", 4, "A patient's urine is held back. Which word of card 17 says this?",
            ("बद्धमूत्रम्", "बद्ध (obstructed) + मूत्र (urine): with obstructed urine."),
            [("शूनवृषणम्", "शूनवृषणम् = with swollen testicles."),
             ("रुजार्दितम्", "रुजार्दितम् = afflicted by pain."),
             ("अश्मरी", "अश्मरी names the stone itself.")],
            "बद्धमूत्रम् = with obstructed urine.",
            "बद्ध = obstructed; मूत्र = urine."),
        mcq("transfer", 5, "By the pattern of रुजा + अर्दितम् → रुजार्दितम्, how is शिला + अग्रम् (the tip of a rock) joined in a new example?",
            ("शिलाग्रम्", "आ + अ → आ: शिला + अग्रम् → शिलाग्रम्."),
            [("शिलग्रम्", "The two vowels merge into a long आ, not a short अ."),
             ("शिलेग्रम्", "ए comes from अ/आ + इ, not from आ + अ."),
             ("शिलौग्रम्", "औ comes from अ/आ + ओ or औ, not from आ + अ.")],
            "शिला + अग्रम् = शिलाग्रम्, like रुजा + अर्दितम् = रुजार्दितम्.",
            "आ + अ → आ.",
            teaches="आ before अ merges into a long आ: रुजा + अर्दितम् → रुजार्दितम्."),
    ],
}

# ---------------------------------------------------------------- unit 18
AUTHORED["18"] = {
    "title": "मेह और पिटिका",
    "question": "By card 18, what goes with meha, and where are the boils situated?",
    "rule": ("Meha (prameha, probably the diabetes-type) with the patient having pricking pain and burning (conjectural), boils, "
             "decay of flesh and diarrhoea; boils (पिटिकाः) situated in the marmas, back, breast, shoulder, anus and head."),
    "limits": ("Printed तुद्द्वाह is read तुद्दाह (stray व्; तृड्दाह also possible), and हृत् (heart) for printed हत्: both conjectural, "
               "no question on them. Elliptical (verb carried over). The list of sites continues in card 19. मर्म is kept as a doctrinal term."),
    "explain_hi": ("मेह को यहाँ प्रमेह, सम्भवतः मधुमेह वाला रूप, पढ़ा गया है (सम्भावित)। "
                   "रोगी के साथ चुभन और दाह (अनुमानित पाठ), पिटका (फुंसियाँ), मांस का सड़ना और अतिसार कहे गए। "
                   "दूसरी पंक्ति पिटिकाओं के स्थान गिनाती है: मर्म, पीठ, स्तन, कन्धा, गुदा और सिर; छपा ‘हत्’ को ‘हृत्’ (हृदय) पढ़ना अनुमान है। "
                   "स्थानों की सूची कार्ड १९ में आगे चलती है। "
                   "सन्धि: पिटिकाः + मर्म- → पिटिका मर्म- (आः घोष वर्ण से पहले विसर्ग खोता है); मेहः + त → मेहस्त (त से पहले ः → स्)।"),
    "hook": "मेह के साथ पिटिका: मर्म, पीठ, स्तन, कन्धा, गुदा, सिर।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "In card 18, how does the data read मेहः?",
            ("As prameha, a urinary disorder", "मेह is read as prameha, a urinary disorder, probably the diabetes-type."),
            [("As visarpa, a skin inflammation", "Visarpa is a different disease (card 20); मेह is a urinary disorder."),
             ("As gulma, an abdominal lump", "Gulma is a different disease (card 20); मेह is a urinary disorder."),
             ("As pīnasa, a nasal catarrh", "Pīnasa is a different disease (card 21); मेह is a urinary disorder.")],
            "मेहः = prameha (probable).",
            "मेह = prameha, a urinary disorder."),
        match(1, "Match each site of the boils in card 18 to its meaning.",
              [["पृष्ठ", "back"], ["स्तन", "breast"], ["अंस", "shoulder"], ["गुद", "anus"], ["मूर्धन्", "head"]],
              "पृष्ठ = back, स्तन = breast, अंस = shoulder, गुद = anus, मूर्धन् = head.",
              "पृष्ठ, स्तन, अंस, गुद, मूर्धन्."),
        order(2, "Put these sure sites of the boils in card 18 in the printed order.",
              ["मर्म", "पृष्ठ", "स्तन", "अंस", "गुद", "मूर्द्ध"],
              "Vital spots, (heart, conjectural), back, breast, shoulder, anus, head; -गाः (situated in) closes the compound.",
              "मर्म → पृष्ठ → स्तन → अंस → गुद → मूर्द्ध.",
              role="extend",
              teaches="A place compound ending in -ग (situated in) can list many sites; the doubtful हत् is left out here."),
        mcq("discriminate", 3, "Why is पिटिकाः printed पिटिका before मर्म- in card 18?",
            ("After आ, ः drops before a voiced sound", "आः loses its visarga before a voiced sound: म is voiced, so पिटिका मर्म-."),
            [("Any ः drops before any consonant", "Not any: before त it gives स्, as in मेहस्त- of this same card."),
             ("After आ, ः before म becomes ओ", "ओ comes from अः before a voiced consonant, not from आः."),
             ("After आ, ः before म becomes र्", "र् comes after vowels other than अ and आ.")],
            "पिटिकाः + मर्म- → पिटिका मर्म-.",
            "आः + voiced sound → आ (visarga drops)."),
        mcq("apply", 4, "Why is मेहः printed मेहस् before the following त in card 18?",
            ("ः before त becomes स्", "A visarga before त or थ becomes स्: मेहः + त → मेहस्त."),
            [("ः before त becomes श्", "श् comes before च or छ, not before त."),
             ("ः before त becomes ओ", "ओ comes from अः before a voiced consonant; त is unvoiced."),
             ("ः before त becomes र्", "र् comes after vowels other than अ/आ before voiced sounds.")],
            "मेहः + त- → मेहस्त-.",
            "ः + त/थ → स्."),
        mcq("transfer", 5, "By the pattern of पिटिकाः + मर्म- → पिटिका मर्म-, how is लताः + वर्धन्ते (the creepers grow) written in a new example?",
            ("लता वर्धन्ते", "आः drops its visarga before the voiced व: लता वर्धन्ते."),
            [("लतो वर्धन्ते", "ओ comes from अः, not from आः."),
             ("लतार्वर्धन्ते", "र् comes after vowels other than अ/आ."),
             ("लताश्वर्धन्ते", "श् comes before च or छ, not before व.")],
            "लताः + वर्धन्ते = लता वर्धन्ते, like पिटिकाः + मर्म- = पिटिका मर्म-.",
            "आः + voiced sound → आ.",
            teaches="After आ the visarga drops before a voiced sound: पिटिकाः + मर्म- → पिटिका मर्म-."),
    ],
}

# ---------------------------------------------------------------- unit 19
AUTHORED["19"] = {
    "title": "पर्वपादकरस्था वा",
    "question": "By card 19, where else may the boils be, and with what is the case accompanied?",
    "rule": ("(Boils) situated in the joints, feet or hands (पर्वपादकरस्थाः वा); the prameha patient of low energy (मन्दोत्साहम्); "
             "and all with decay of flesh, burning, thirst, intoxication and fever."),
    "limits": ("Continues card 18; 'boils' is not printed here. Printed प्रमेहिण is read प्रमेहिणम् (anusvāra dropped). सर्वम् "
               "('all') has no stated referent: no question on it. Prameha keeps the data's label."),
    "explain_hi": ("यह इकाई कार्ड १८ की पिटिका-सूची को आगे बढ़ाती है: जोड़ों, पैरों या हाथों में स्थित; ‘पिटिका’ शब्द यहाँ छपा नहीं। "
                   "फिर मन्द उत्साह वाले प्रमेही को (छपा ‘प्रमेहिण’, अनुस्वार छूटा हुआ)। "
                   "दूसरी पंक्ति: ‘और सब’, मांस के सड़ने, दाह, प्यास, मद और ज्वर से; ‘सब’ किसके लिए है, यह नहीं कहा गया। "
                   "‘वा’ स्थानों को विकल्प के रूप में जोड़ता है। "
                   "‘मन्दोत्साह’ में मन्द + उत्साह की सन्धि है (अ + उ → ओ)।"),
    "hook": "जोड़, पैर या हाथ; मन्द उत्साह; मांस सड़े, दाह, प्यास, मद, ज्वर।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "In card 19, what does मन्दोत्साह mean?",
            ("Of low energy", "मन्द (low) + उत्साह (energy): of low energy."),
            [("Of great strength", "मन्द means low, slight, not great."),
             ("Of quick temper", "उत्साह is energy, not temper."),
             ("Of deep sleep", "Nothing in मन्दोत्साह names sleep.")],
            "मन्दोत्साह = of low energy.",
            "मन्द = low; उत्साह = energy."),
        order(1, "Put the members of the instrumental list in card 19, line 2, in the printed order.",
              ["मांससंकोथ", "दाह", "तृष्णा", "मद", "ज्वर"],
              "Decay of flesh, burning, thirst, intoxication, fever.",
              "मांससंकोथ → दाह → तृष्णा → मद → ज्वर."),
        match(2, "Match each word of card 19 to its meaning.",
              [["पाद", "foot"], ["कर", "hand"], ["तृष्णा", "thirst"], ["मद", "intoxication"], ["ज्वर", "fever"]],
              "पाद = foot, कर = hand, तृष्णा = thirst, मद = intoxication, ज्वर = fever.",
              "पाद, कर, तृष्णा, मद, ज्वर.", role="extend",
              teaches="पर्वपादकरस्थाः: a dvandva of places (joint, foot, hand) + -स्थ (situated in)."),
        mcq("discriminate", 3, "Which split of मन्दोत्साह in card 19 is right?",
            ("मन्द + उत्साह", "अ + उ → ओ: मन्द + उत्साह → मन्दोत्साह."),
            [("मन्दु + उत्साह", "उ + उ → ऊ: that would print मन्दूत्साह."),
             ("मन्द + ओत्साह", "अ + ओ → औ: that would print मन्दौत्साह."),
             ("मन्दि + उत्साह", "इ + उ → यु: that would print मन्द्युत्साह.")],
            "मन्द (low) + उत्साह (energy): अ + उ → ओ.",
            "अ + उ → ओ."),
        mcq("apply", 4, "In card 19, what does वा after पर्वपादकरस्था do?",
            ("It offers the places as alternatives", "वा = or: the boils are in the joints, feet or hands (read as distributive)."),
            [("It marks a comparison, like", "Like would be इव; वा means or."),
             ("It denies the places, not", "Not would be न; वा means or."),
             ("It closes the sentence, thus", "Thus would be इति; वा means or.")],
            "वा = or.",
            "वा = or."),
        mcq("transfer", 5, "By the pattern of मन्द + उत्साह → मन्दोत्साह, how is चन्द्र + उदयः (moonrise) joined in a new example?",
            ("चन्द्रोदयः", "अ + उ → ओ: चन्द्र + उदयः → चन्द्रोदयः."),
            [("चन्द्रौदयः", "औ comes from अ + ओ or औ, not from अ + उ."),
             ("चन्द्रूदयः", "ऊ comes from उ + उ, not from अ + उ."),
             ("चन्द्रवुदयः", "व् comes from उ before a different vowel, not from अ.")],
            "चन्द्र + उदयः = चन्द्रोदयः, like मन्द + उत्साह = मन्दोत्साह.",
            "अ + उ → ओ.",
            teaches="अ or आ before उ or ऊ gives ओ: मन्द + उत्साह → मन्दोत्साह."),
    ],
}

# ---------------------------------------------------------------- unit 20
AUTHORED["20"] = {
    "title": "गुल्मः पृथुपरीणाहो",
    "question": "By card 20, how is the gulma described?",
    "rule": ("Line 1 continues card 19's instrumental list: visarpa, obstruction of the marmas, hiccup, breathlessness, giddiness, "
             "fatigue. Line 2: gulma (abdominal lump, probable), broad in girth (पृथुपरीणाहः), dense (घनः), raised like a tortoise (कूर्म इव उन्नतः)."),
    "limits": ("Visarpa (erysipelas) and gulma keep the data's label 'probable'. No verb is printed for the gulma. मर्म is a "
               "doctrinal term. The IAST kūrmaiva is an intake artefact; the Devanagari prints कूर्मइवोन्नतः."),
    "explain_hi": ("पहली पंक्ति कार्ड १९ की तृतीया-सूची को आगे बढ़ाती है: विसर्प (सम्भवतः फैलने वाला त्वचा-शोथ), मर्मों की रुकावट, हिचकी, श्वास, चक्कर और थकावट। "
                   "दूसरी पंक्ति नया कर्ता लेती है: गुल्म (सम्भवतः पेट की गाँठ), जो चौड़े घेरे वाला, घना और कछुए की तरह ऊँचा उठा हुआ है। "
                   "गुल्म की क्रिया यहाँ नहीं छपी। "
                   "सन्धियाँ: पृथुपरीणाहः + घनः → पृथुपरीणाहो घनः (अः घोष व्यंजन से पहले → ओ); कूर्मः + इव → कूर्म इव (अः, अ से भिन्न स्वर से पहले → अ); इव + उन्नतः → इवोन्नतः (अ + उ → ओ)।"),
    "hook": "गुल्म: चौड़ा, घना, कछुए की पीठ-सा उठा।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "In card 20, what does कूर्म mean?",
            ("Tortoise", "कूर्म = tortoise: कूर्म इव उन्नतः, raised like a tortoise."),
            [("Fish", "Fish would be मत्स्य; कूर्म = tortoise."),
             ("Frog", "Frog would be मण्डूक; कूर्म = tortoise."),
             ("Crab", "Crab would be कर्कट; कूर्म = tortoise.")],
            "कूर्म = tortoise.",
            "कूर्म = tortoise."),
        match(1, "Match each word of card 20, line 1, to its meaning.",
              [["संरोध", "obstruction"], ["हिध्मा", "hiccup"], ["श्वास", "breathlessness"], ["भ्रम", "giddiness"], ["क्लम", "fatigue"]],
              "संरोध = obstruction, हिध्मा = hiccup, श्वास = breathlessness, भ्रम = giddiness, क्लम = fatigue.",
              "संरोध, हिध्मा, श्वास, भ्रम, क्लम."),
        order(2, "Put the members of the compound in card 20, line 1, in the printed order.",
              ["विसर्प", "मर्मसंरोध", "हिध्मा", "श्वास", "भ्रम", "क्लम"],
              "Visarpa, obstruction of the marmas, hiccup, breathlessness, giddiness, fatigue.",
              "विसर्प → मर्मसंरोध → हिध्मा → श्वास → भ्रम → क्लम.",
              role="extend",
              teaches="An instrumental plural dvandva (-क्लमैः) lists the companions 'with which' a case comes."),
        mcq("discriminate", 3, "Which split of कूर्मइवोन्नतः in card 20 is right?",
            ("कूर्मः + इव + उन्नतः", "अः before इ → अ (hiatus): कूर्म इव; अ + उ → ओ: इवोन्नतः."),
            [("कूर्मः + एव + उन्नतः", "एव would print कूर्मएवोन्नतः, with ए, not इ."),
             ("कूर्म + इव + उन्नतः", "अ + इ → ए: that would print कूर्मेवोन्नतः."),
             ("कूर्मः + इव + नतः", "No join: that would print इवनतः; the print has वो."),],
            "कूर्मः (tortoise) + इव (like) + उन्नतः (raised).",
            "अः + vowel other than अ → अ; अ + उ → ओ."),
        mcq("apply", 4, "Why is कूर्मः printed कूर्म before इव in card 20?",
            ("अः before a vowel other than अ → अ", "The visarga of अः drops before इ, and the vowels stay apart: कूर्म इव."),
            [("Every ः drops before any sound", "Not every: पृथुपरीणाहः + घनः gives पृथुपरीणाहो घनः in this card."),
             ("अः before any vowel becomes ओ", "ओ comes before voiced consonants; before इ it is अ."),
             ("अः before इ becomes the य्", "य् comes from इ or ई before a vowel, not from अः.")],
            "कूर्मः + इव → कूर्म इव.",
            "अः + vowel other than अ → अ."),
        mcq("transfer", 5, "By the pattern of पृथुपरीणाहः + घनः → पृथुपरीणाहो घनः, how is सिंहः + गर्जति (the lion roars) written in a new example?",
            ("सिंहो गर्जति", "अः before the voiced consonant ग → ओ: सिंहो गर्जति."),
            [("सिंह गर्जति", "Only सः and एषः drop the visarga before a consonant."),
             ("सिंहर्गर्जति", "र् comes after vowels other than अ/आ."),
             ("सिंहा गर्जति", "The अ does not lengthen; अः gives ओ.")],
            "सिंहः + गर्जति = सिंहो गर्जति, like पृथुपरीणाहः + घनः = पृथुपरीणाहो घनः.",
            "अः + voiced consonant → ओ.",
            teaches="अः before a voiced consonant becomes ओ: पृथुपरीणाहः + घनः → पृथुपरीणाहो घनः."),
    ],
}

# ---------------------------------------------------------------- unit 21
AUTHORED["21"] = {
    "title": "सिरानद्धो ज्वरच्छर्द्दि",
    "question": "By card 21, what accompanies the gulma described here?",
    "rule": ("Bound by sirās (veins or vessels), with fever, vomiting, hiccup, bloating (आध्मान) and pain; having cough, "
             "pīnasa (nasal catarrh, probable), nausea (हृल्लास), breathlessness, diarrhoea and swelling (-शोफवान्)."),
    "limits": ("The data takes these nominatives as describing the gulma of card 20. sirā = vein or vessel (probable); pīnasa "
               "keeps the label 'probable'. No verb in the unit. The ऽ in हिध्माऽध्मान is a print habit."),
    "explain_hi": ("डेटा के अनुसार यह इकाई कार्ड २० के गुल्म का वर्णन जारी रखती है। "
                   "वह सिराओं से बँधा (नसें या वाहिकाएँ, सम्भावित), ज्वर, उल्टी, हिचकी, आध्मान (अफारा) और पीड़ा से युक्त है। "
                   "दूसरी पंक्ति: खाँसी, पीनस (सम्भवतः पुराना जुकाम), हृल्लास (मिचली), श्वास, अतिसार और शोफ वाला। "
                   "कोई क्रिया नहीं छपी। "
                   "‘-शोफवान्’ में -वत् प्रत्यय ‘वाला’ का अर्थ देता है; सन्धि: सिरानद्धः + ज्वर- → सिरानद्धो ज्वर- (अः घोष व्यंजन से पहले → ओ)।"),
    "hook": "गुल्म के साथी: ज्वर, उल्टी, हिचकी, अफारा; खाँसी, पीनस, मिचली, श्वास, दस्त, सूजन।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "In card 21, what does हृल्लास mean?",
            ("Nausea", "हृल्लास = nausea."),
            [("Hiccup", "Hiccup is हिध्मा, a different word of this card."),
             ("Thirst", "Thirst would be तृष्णा; हृल्लास = nausea."),
             ("Fever", "Fever is ज्वर; हृल्लास = nausea.")],
            "हृल्लास = nausea.",
            "हृल्लास = nausea."),
        match(1, "Match each word of card 21, line 1, to its meaning.",
              [["ज्वर", "fever"], ["छर्दि", "vomiting"], ["हिध्मा", "hiccup"], ["आध्मान", "bloating"], ["अन्वित", "accompanied"]],
              "ज्वर = fever, छर्दि = vomiting, हिध्मा = hiccup, आध्मान = bloating, अन्वित = accompanied.",
              "ज्वर, छर्दि, हिध्मा, आध्मान, अन्वित."),
        order(2, "Put the members of the compound in card 21, line 2, in the printed order.",
              ["कास", "पीनस", "हृल्लास", "श्वास", "अतीसार", "शोफ"],
              "Cough, pīnasa, nausea, breathlessness, diarrhoea, swelling; -वान् (having) closes the compound.",
              "कास → पीनस → हृल्लास → श्वास → अतीसार → शोफ.",
              role="extend",
              teaches="-वत् (nom. -वान्) at the end of a dvandva means 'having' all its members."),
        mcq("discriminate", 3, "Why is सिरानद्धः printed सिरानद्धो before ज्वर- in card 21?",
            ("अः before a voiced consonant → ओ", "ज is voiced: सिरानद्धः + ज्वर- → सिरानद्धो ज्वर-."),
            [("ः before any consonant → ओ", "Not any: before त a visarga gives स् (मेहस्त-, card 18)."),
             ("आः before a voiced sound → ओ", "आः simply drops its visarga (पिटिका मर्म-, card 18)."),
             ("ओ is the stem's own final", "The stem is नद्ध; the nominative is नद्धः.")],
            "सिरानद्धः + ज्वर- → सिरानद्धो ज्वर-.",
            "अः + voiced consonant → ओ."),
        mcq("apply", 4, "One word is wrong in this English of card 21, line 1: 'Bound by veins, with fever, vomiting, hiccup, bloating and thirst'. Which?",
            ("thirst", "The member before अन्वित means pain, not thirst."),
            [("fever", "ज्वर = fever: this word is right."),
             ("hiccup", "हिध्मा = hiccup: this word is right."),
             ("bloating", "आध्मान = bloating: this word is right.")],
            "The last member before अन्वित means pain, not thirst.",
            "रुजा / रुज् = pain."),
        mcq("transfer", 5, "By the pattern of -शोफवान् (having swelling), what does रूपवान् mean in a new example?",
            ("Having beauty", "-वत् (nom. -वान्) = having: रूप (form, beauty) + वत् = having beauty."),
            [("Without beauty", "Without would need a prefix like निः- or अ-; -वान् means having."),
             ("Made of beauty", "Made of would be -मय; -वान् means having."),
             ("Caused by beauty", "Caused by would need -ज or a case form; -वान् means having.")],
            "रूपवान् = having beauty, like शोफवान् = having swelling.",
            "-वत् (nom. m. sg. -वान्) = having.",
            teaches="The suffix -वत् (nominative masculine -वान्) means 'having': शोफ + वत् → शोफवान्."),
    ],
}

# ---------------------------------------------------------------- unit 22
AUTHORED["22"] = {
    "title": "जठरं हंति दुर्बलं",
    "question": "By card 22, with which features does jaṭhara kill the weak one?",
    "rule": ("With retention of faeces and urine, breathlessness, swelling, hiccup, fever, giddiness, and with fainting, vomiting "
             "and diarrhoea, jaṭhara (the belly disorder, probably an ascites-type) kills the weak one (जठरं हन्ति दुर्बलम्)."),
    "limits": ("जठर = belly; read as the belly disorder in this list (probable). दुर्बलम् is shown as 'the weak (one)'. The data "
               "says the sentence runs from card 21 to this card; the verb हन्ति is printed here. The text gives no time or prognosis beyond 'kills'."),
    "explain_hi": ("यहाँ क्रिया छपी है: ‘जठरं हन्ति दुर्बलम्’, यानी जठर (पेट का रोग, सम्भवतः जलोदर प्रकार) दुर्बल को मारता है। "
                   "साथ के लक्षण तृतीया में: मल-मूत्र का रुकना, श्वास, शोफ, हिचकी, ज्वर, चक्कर, और मूर्च्छा, उल्टी तथा अतिसार। "
                   "‘हन्ति’ कार्ड ४ के ‘निहन्ति’ से मेल खाता है। "
                   "सन्धि: छर्दि + अतिसारैः → छर्द्यतिसारैः (इ + अ → य); अतिसारैः + च → अतिसारैश्च (च से पहले ः → श्)।"),
    "hook": "जठर दुर्बल को मारता है: मल-मूत्र रुके, श्वास, शोफ, हिचकी, ज्वर, चक्कर, मूर्च्छा, उल्टी, दस्त।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "In card 22, what does हन्ति mean?",
            ("Kills", "हन्ति = kills (√हन्, present, 3rd singular)."),
            [("Cures", "Cures would be from √चिकित्स्; हन्ति = kills."),
             ("Spares", "Spares would be from √त्यज् or √मुच्; हन्ति = kills."),
             ("Feeds", "Feeds would be from √पुष्; हन्ति = kills.")],
            "हन्ति = kills.",
            "√हन् = to kill."),
        order(1, "Put the members of the compound in card 22, line 1, in the printed order.",
              ["विण्मूत्रसंग्रह", "श्वास", "शोफ", "हिध्मा", "ज्वर", "भ्रम"],
              "Retention of faeces and urine, breathlessness, swelling, hiccup, fever, giddiness.",
              "विण्मूत्रसंग्रह → श्वास → शोफ → हिध्मा → ज्वर → भ्रम."),
        match(2, "Match each word of card 22 to its meaning.",
              [["संग्रह", "retention"], ["शोफ", "swelling"], ["मूर्च्छा", "fainting"], ["छर्दि", "vomiting"], ["दुर्बल", "weak"]],
              "संग्रह = retention, शोफ = swelling, मूर्च्छा = fainting, छर्दि = vomiting, दुर्बल = weak.",
              "संग्रह, शोफ, मूर्च्छा, छर्दि, दुर्बल.", role="extend",
              teaches="दुर्बलम् is the accusative object of हन्ति: whom jaṭhara kills."),
        mcq("discriminate", 3, "Which split of छर्द्यतिसारैश्च in card 22 is right?",
            ("छर्दि + अतिसारैः + च", "इ + अ → य: छर्द्यति-; ः before च → श्: -सारैश्च."),
            [("छर्द्य + अतिसारैः + च", "अ + अ → आ: that would print छर्द्याति-."),
             ("छर्दे + अतिसारैः + च", "ए + अ → एऽ: that would print छर्देऽति-."),
             ("छर्दि + इतिसारैः + च", "इ + इ → ई: that would print छर्दीति-.")],
            "छर्दि (vomiting) + अतिसारैः (with diarrhoea) + च (and).",
            "इ + अ → य; ः + च → श्च."),
        mcq("apply", 4, "Why is अतिसारैः printed अतिसारैश् before च in card 22?",
            ("ः before च or छ becomes श्", "A visarga before च or छ becomes श्: अतिसारैः + च → अतिसारैश्च."),
            [("ः before any consonant → श्", "Not any: before त it gives स् (मेहस्त-, card 18)."),
             ("ः before च is dropped", "It is not dropped; it turns into श्."),
             ("ः before च becomes स्", "स् comes before त or थ, not before च.")],
            "अतिसारैः + च → अतिसारैश्च.",
            "ः + च/छ → श्."),
        mcq("transfer", 5, "By the pattern of अतिसारैः + च → अतिसारैश्च, how is मृगाः + च (and the deer) joined in a new example?",
            ("मृगाश्च", "ः before च → श्: मृगाः + च → मृगाश्च."),
            [("मृगा च", "Before च the visarga is not dropped; it becomes श्."),
             ("मृगास्च", "स् comes before त or थ, not before च."),
             ("मृगोच", "ओ comes from अः before a voiced consonant; च is unvoiced.")],
            "मृगाः + च = मृगाश्च, like अतिसारैः + च = अतिसारैश्च.",
            "ः + च → श्च.",
            teaches="A visarga before च or छ becomes श्: अतिसारैः + च → अतिसारैश्च."),
    ],
}

# ---------------------------------------------------------------- unit 23
AUTHORED["23"] = {
    "title": "शूनाक्षं कुटिलोपस्थम्",
    "question": "By card 23, which sure features of the patient does line 1 give?",
    "rule": ("Line 1, accusative: (one) with swollen eyes (शूनाक्षम्), crooked genitals (कुटिलोपस्थम्, upastha: standard) and "
             "moist, thin skin (उपक्लिन्नतनुत्वचम्). Line 2 ends with पुनः पुनः, again and again."),
    "limits": ("Prose, low confidence. Line 2's विरेचनहत- (harmed by purgation) is a conjecture for printed विरेचनहतानाम्, and "
               "आनह्यन्तम् is an unusual form: no question on them. No verb in the unit; the data takes it as describing the weak "
               "patient of card 22."),
    "explain_hi": ("पहली पंक्ति रोगी के तीन पक्के लक्षण द्वितीया में देती है: सूजी आँखें, टेढ़ा उपस्थ (जननांग, मानक) और गीली, पतली त्वचा। "
                   "दूसरी पंक्ति का ‘विरेचन से आहत’ अनुमानित पाठ है (छपा ‘विरेचनहतानाम्’), इसलिए उस पर प्रश्न नहीं; ‘पुनः पुनः’ = बार-बार। "
                   "इकाई में कोई क्रिया नहीं; डेटा इसे कार्ड २२ के दुर्बल रोगी का वर्णन मानता है। "
                   "सन्धि: कुटिल + उपस्थम् → कुटिलोपस्थम् (अ + उ → ओ); उपस्थम् + उपक्लिन्न- → उपस्थमुपक्लिन्न- (स्वर से पहले म् जुड़ जाता है)।"),
    "hook": "सूजी आँखें, टेढ़ा उपस्थ, गीली पतली त्वचा।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "In card 23, what does शूनाक्ष mean?",
            ("Having swollen eyes", "शून (swollen) + अक्ष (eye): having swollen eyes."),
            [("Having sunken eyes", "Sunken would be प्रविष्ट; शून = swollen."),
             ("Having reddish eyes", "Red would be रक्त; शून = swollen."),
             ("Having closed eyes", "Closed would be निमीलित; शून = swollen.")],
            "शूनाक्ष = having swollen eyes.",
            "शून = swollen; अक्ष = eye."),
        match(1, "Match each word part of card 23, line 1, to its meaning.",
              [["शून", "swollen"], ["अक्ष", "eye"], ["कुटिल", "crooked"], ["उपक्लिन्न", "moist"], ["तनु", "thin"]],
              "शून = swollen, अक्ष = eye, कुटिल = crooked, उपक्लिन्न = moist, तनु = thin.",
              "शून, अक्ष, कुटिल, उपक्लिन्न, तनु."),
        order(2, "Put these printed parts of card 23 in the printed order.",
              ["शूनाक्षं", "कुटिलोपस्थम्", "उपक्लिन्नतनुत्वचं", "पुनः पुनः"],
              "Swollen eyes, crooked genitals, moist thin skin; line 2 ends again and again.",
              "शूनाक्षं → कुटिलोपस्थम् → उपक्लिन्नतनुत्वचं → पुनः पुनः.",
              role="extend",
              teaches="Each accusative bahuvrīhi names one feature of the person it describes: शून-अक्ष = whose eyes are swollen."),
        mcq("discriminate", 3, "Why does उपस्थम् join the next word as उपस्थमुपक्लिन्न- in card 23?",
            ("Final म् before a vowel stays and joins", "Before the vowel उ the म् is kept and written with it: -स्थमुप-."),
            [("Final म् before a vowel → ं", "ं is written for म् before a consonant, not before a vowel."),
             ("Final म् before a vowel drops", "म् does not drop; it joins the vowel."),
             ("Final म् before उ becomes व्", "व् comes from उ before a vowel, not from म्.")],
            "उपस्थम् + उपक्लिन्न- → उपस्थमुपक्लिन्न-.",
            "Final म् + vowel → joined म्."),
        multi("apply", 4, "Which statements fit card 23 as the data gives it?",
              [("Line 2 opens with a sure reading", "No: विरेचनहत- is a conjecture for the printed विरेचनहतानाम्."),
               ("Line 1 gives three features of the patient", "Right: swollen eyes, crooked genitals, moist thin skin."),
               ("The unit prints its own main verb", "No: there is no verb in this unit."),
               ("पुनः पुनः means again and again", "Right: पुनः पुनः = again and again.")],
              [1, 3],
              "Three sure features in line 1; line 2 is partly conjectural; no verb.",
              "Ask only about the sure parts."),
        mcq("transfer", 5, "By the pattern of उपस्थम् + उपक्लिन्न- → उपस्थमुपक्लिन्न-, how is पुष्पम् + इदम् (this flower) joined in a new example?",
            ("पुष्पमिदम्", "Final म् before a vowel joins it: पुष्पम् + इदम् → पुष्पमिदम्."),
            [("पुष्पेदम्", "म् is not lost to give अ + इ → ए; it stays."),
             ("पुष्पोदम्", "ओ would need अ + उ; here म् simply joins इ."),
             ("पुष्पयिदम्", "No य् is inserted; म् joins the vowel.")],
            "पुष्पम् + इदम् = पुष्पमिदम्, like उपस्थम् + उपक्लिन्न- = उपस्थमुपक्लिन्न-.",
            "Final म् + vowel → joined म्.",
            teaches="Inside a sentence a final म् before a vowel stays and is written with it: उपस्थम् + उप- → उपस्थमुप-."),
    ],
}

# ---------------------------------------------------------------- unit 24
AUTHORED["24"] = {
    "title": "पांडुरोगः श्वयथुमान्",
    "question": "By card 24, which features go with pāṇḍu disease?",
    "rule": ("Pāṇḍuroga (anaemia with pallor, standard) with swelling (श्वयथुमान्); yellow eyes and nails seen; having drowsiness, "
             "burning, distaste for food (अरुचि), vomiting, fainting, flatulent distension (आध्मान) and diarrhoea."),
    "limits": ("No verb here: the data says cards 24 and 25 form one run, with हन्ति only in card 25. पीत is taken with both eyes "
               "and nails (the data's reading): no question on it. The ऽ in मूर्च्छाऽध्मान is a print habit."),
    "explain_hi": ("पाण्डु रोग (रक्ताल्पता, मानक) सूजन वाला हो, और जिसमें आँखें और नाखून पीले दिखें। "
                   "दूसरी पंक्ति के लक्षण: तन्द्रा (ऊँघ), दाह, अरुचि (भोजन में अरुचि), छर्दि, मूर्च्छा, आध्मान और अतिसार। "
                   "यहाँ क्रिया नहीं; डेटा के अनुसार वाक्य कार्ड २५ के ‘हन्ति’ तक चलता है। "
                   "सन्धि: दाह + अरुचि → दाहारुचि (अ + अ → आ); अरुचि + छर्दि → अरुचिच्छर्दि (ह्रस्व स्वर के बाद छ → च्छ)।"),
    "hook": "पाण्डु: सूजन, पीली आँखें और नाखून, ऊँघ, जलन, अरुचि, उल्टी, मूर्च्छा, अफारा, दस्त।",
    "core": False,
    "questions": [
        mcq("pretest", 0, "In card 24, what is पाण्डुरोग?",
            ("Anaemia with pallor", "पाण्डुरोग = pāṇḍu disease, anaemia with pallor (standard)."),
            [("A urinary stone", "A urinary stone is अश्मरी (card 17)."),
             ("A nasal catarrh", "Nasal catarrh is पीनस (card 21)."),
             ("A hiccup disease", "Hiccup is हिध्मा, not पाण्डु.")],
            "पाण्डुरोग = anaemia with pallor.",
            "पाण्डु = pale."),
        order(1, "Put these members of the compound in card 24, line 2, in the printed order.",
              ["तन्द्रा", "दाह", "अरुचि", "छर्दि", "मूर्च्छा", "आध्मान"],
              "Drowsiness, burning, distaste for food, vomiting, fainting, distension; अतिसार and -वान् close it.",
              "तन्द्रा → दाह → अरुचि → छर्दि → मूर्च्छा → आध्मान."),
        match(2, "Match each word of card 24 to its meaning.",
              [["तन्द्रा", "drowsiness"], ["अरुचि", "distaste for food"], ["पीत", "yellow"], ["नख", "nail"], ["श्वयथु", "swelling"]],
              "तन्द्रा = drowsiness, अरुचि = distaste for food, पीत = yellow, नख = nail, श्वयथु = swelling.",
              "तन्द्रा, अरुचि, पीत, नख, श्वयथु.", role="extend",
              teaches="श्वयथुमान् = having swelling: -मत् (nom. -मान्) means having."),
        mcq("discriminate", 3, "One word is wrong in this English of card 24, line 2: 'Having drowsiness, burning, hunger, vomiting, fainting, distension and diarrhoea'. Which?",
            ("hunger", "अरुचि is distaste for food, not hunger."),
            [("drowsiness", "तन्द्रा = drowsiness: this word is right."),
             ("fainting", "मूर्च्छा = fainting: this word is right."),
             ("burning", "दाह = burning: this word is right.")],
            "अरुचि = distaste for food.",
            "अरुचि = distaste for food."),
        mcq("apply", 4, "Why is छर्दि printed -च्छर्द्दि after अरुचि in card 24?",
            ("After a short vowel छ is doubled as च्छ", "अरुचि ends in short इ, so छ is written च्छ."),
            [("च् is added before every consonant", "Only छ is so treated, and only after a vowel."),
             ("च् is part of the stem अरुचिच्", "The stem is अरुचि; the च् comes from sandhi."),
             ("छ is doubled after every vowel", "After a long vowel it is optional: card 22 prints मूर्च्छाछर्दि.")],
            "अरुचि + छर्दि → अरुचिच्छर्दि.",
            "Short vowel + छ → च्छ."),
        mcq("transfer", 5, "By the pattern of अरुचि + छर्दि → अरुचिच्छर्दि, how is तरु + छाया (shade of a tree) joined in a new example?",
            ("तरुच्छाया", "After the short उ, छ is doubled: तरु + छाया → तरुच्छाया."),
            [("तरुछाया", "After a short vowel छ must be written च्छ."),
             ("तरूछाया", "The उ of तरु does not lengthen."),
             ("तरुश्छाया", "श् comes from a visarga before छ; तरु has none.")],
            "तरु + छाया = तरुच्छाया, like अरुचि + छर्दि = अरुचिच्छर्दि.",
            "Short vowel + छ → च्छ.",
            teaches="After a short vowel छ is written च्छ: अरुचि + छर्दि → अरुचिच्छर्दि."),
    ],
}

# ---------------------------------------------------------------- unit 25
AUTHORED["25"] = {
    "title": "नारीं शोफो मुखाद्धंति",
    "question": "By card 25, from where does swelling (śopha) kill a man, a woman and both?",
    "rule": ("Swelling (शोफः), joined with many complications (अनेकोपद्रवयुतः), kills a man spread from the two feet "
             "(पादाभ्यां प्रसृतं नरम्), a woman from the face (नारीं मुखात्), and both from the belly and private parts (कुक्षिगुह्यात् उभौ अपि)."),
    "limits": ("What has spread in the man is not stated (śopha is the data's inference). उभौ (both) is most likely man and woman: "
               "an inference. पादाभ्याम् may be 'from' or 'by': no question on its case. मुखात् is literally 'from the face'. हन्ति is printed once."),
    "explain_hi": ("यहाँ कार्ड २४ से चला आ रहा वाक्य ‘हन्ति’ (मारता है) पर पूरा होता है। "
                   "शोफ (सूजन, मानक), अनेक उपद्रवों से युक्त, पुरुष को दोनों पैरों से फैला हुआ होने पर मारता है; पैरों से क्या फैला, यह छपा नहीं, डेटा शोफ मानता है। "
                   "स्त्री को मुख से, और कुक्षि (पेट) व गुह्य (गुप्त अंग) से दोनों को भी; ‘दोनों’ सम्भवतः पुरुष और स्त्री हैं। "
                   "सन्धि: मुखात् + हन्ति → मुखाद्धन्ति (घोष ह से पहले त् → द्, फिर ह विकल्प से ध); उभौ + अपि → उभावपि (औ + स्वर → आव्)।"),
    "hook": "शोफ: पुरुष को पैरों से, स्त्री को मुख से, दोनों को पेट और गुह्य से।",
    "core": True,
    "questions": [
        mcq("pretest", 0, "In card 25, what does शोफ mean?",
            ("Swelling", "शोफ = swelling (oedema, standard)."),
            [("Fever", "Fever is ज्वर; शोफ = swelling."),
             ("Thirst", "Thirst is तृष्णा; शोफ = swelling."),
             ("Cough", "Cough is कास; शोफ = swelling.")],
            "शोफ = swelling.",
            "शोफ = swelling (oedema)."),
        match(1, "Match each word of card 25 to its meaning.",
              [["नर", "man"], ["नारी", "woman"], ["मुख", "face"], ["कुक्षि", "belly"], ["गुह्य", "private parts"]],
              "नर = man, नारी = woman, मुख = face, कुक्षि = belly, गुह्य = private parts.",
              "नर, नारी, मुख, कुक्षि, गुह्य."),
        order(2, "Put these printed parts of card 25 in the printed order.",
              ["पादाभ्यां", "प्रसृतं नरं", "नारीं", "शोफो", "मुखाद्धंति", "कुक्षिगुह्यादुभावपि"],
              "From the feet, the man spread; the woman; swelling; kills from the face; from belly and private parts both too.",
              "पादाभ्यां → प्रसृतं नरं → नारीं → शोफो → मुखाद्धंति → कुक्षिगुह्यादुभावपि.",
              role="extend",
              teaches="One verb (हन्ति) serves several objects: नरम्, नारीम् and उभौ."),
        mcq("discriminate", 3, "By card 25, from where does the swelling kill a woman?",
            ("From the face", "नारीं शोफो मुखाद्धन्ति: swelling kills a woman from the face."),
            [("From the two feet", "The two feet (पादाभ्याम्) are said of the man."),
             ("From the back", "The back is not named in card 25."),
             ("From the eyes", "The eyes are not named in card 25.")],
            "Woman: from the face (मुखात्).",
            "नारी → मुखात्."),
        mcq("apply", 4, "Which split of मुखाद्धंति in card 25 is right?",
            ("मुखात् + हन्ति", "त् before the voiced ह → द्, and ह after it may become ध (optional): मुखाद्धन्ति."),
            [("मुखा + द्धन्ति", "द्धन्ति is not a word; the द् comes from the त् of मुखात्."),
             ("मुखात् + धन्ति", "धन्ति is not a word; the verb is हन्ति."),
             ("मुखम् + हन्ति", "That would print मुखं हन्ति; the print has मुखाद्-.")],
            "मुखात् (from the face) + हन्ति (kills).",
            "त् + ह → द्ध (ह → ध optional; द्ह also valid)."),
        mcq("transfer", 5, "By the pattern of उभौ + अपि → उभावपि, how is पितरौ + अपि (both parents too) joined in a new example?",
            ("पितरावपि", "औ before a vowel → आव्: पितरौ + अपि → पितरावपि."),
            [("पितरोऽपि", "ओऽ comes from अः + अ, not from औ + अ."),
             ("पितरापि", "औ does not just turn into आ; it gives आव्."),
             ("पितरवपि", "अव् comes from ओ before a vowel, not from औ.")],
            "पितरौ + अपि = पितरावपि, like उभौ + अपि = उभावपि.",
            "औ + vowel → आव्.",
            teaches="औ before a vowel becomes आव्: उभौ + अपि → उभावपि."),
    ],
}

# ================================================================ NOTES_HI
NOTES_HI = {
    "14": ("पद्य; विश्वास मध्यम; दो छपी पंक्तियाँ (०२.११.२४ और ०२.११.२५) जोड़ी गईं; कार्ड १३ (छपी पंक्तियाँ २२-२३) की सूची जारी। "
           "पाठ-चिह्न (सम्भव): ‘मस्तु लुंग’ के बीच रिक्त स्थान को भूल मानकर मस्तुलुङ्ग (मस्तिष्क) पढ़ना अनुमान है; विकल्प: मस्तु (दही का पानी) और लुङ्ग (बिजौरा) दो शब्द। "
           "‘वेसवारंबु’ में स/श की अदला-बदली और अनुस्वार भटका हुआ: वेशवार + अम्बु (वेशवारांबु) सुझाया गया। इन पर प्रश्न नहीं। "
           "‘अति’ अलग छपा, समास का पहला भाग भी हो सकता है; ‘घनवेदन’ = ‘तीव्र पीड़ा’ भी सम्भव। "
           "सन्धि जाँची: रक्त + असित → रक्तासित (अ + अ → आ); पूति + अच्छ → पूत्यच्छ (इ + अ → य)।"),
    "15": ("गद्य (डेटा का प्रकार; छन्द पर कोई प्रश्न नहीं); विश्वास कम; दो छपी पंक्तियाँ (०२.११.२६ और ०२.११.२७)। क्षतिग्रस्त छपाई। "
           "‘प्रस्रवन्धात्त्रिष्पूरीषो’ विश्लेषित नहीं होता; ‘त्रिष्’ को ‘निष्’ पढ़ने से निष्पुरीष (मल-रहित) बनता, जो अतिविट् से जोड़ा बनाता, पर यह स्वीकार नहीं किया गया। "
           "‘राजैर्मांसेंद्रकैर्’ का अर्थ निश्चित नहीं। ‘मसिका’ = मषिका (स/ष छपाई की आदत)। "
           "सन्धि जाँची: अथवा + अतिविट् → अथवातिविट् (आ + अ → आ; ऽ छपाई की आदत); तन्तुमान् + मसिका- → तंतुमान्मसिका- (बिना परिवर्तन जुड़ा)।"),
    "16": ("गद्य (डेटा का प्रकार; छन्द पर कोई प्रश्न नहीं); विश्वास कम; दो छपी पंक्तियाँ (०२.११.२८ और ०२.११.२९)। "
           "पाठ-चिह्न (सम्भव): ‘वालिं’ को ‘वलिं’ (तह) पढ़ा गया, अनुमानित। ‘नाल’ = डंठल; यहाँ क्या अभिप्रेत है, छपा नहीं। "
           "‘अन्नेवोपवेशयन्’ अस्पष्ट (अन्नं वा उपवेशयन् या अन्ने वा उपवेशयन्), अर्थ स्पष्ट नहीं। क्रिया पहले से चली आ रही; डेटा के अनुसार यह कार्ड १५-१६ की कर्म-सूची है। "
           "स्रस्तपायु = गुदभ्रंश (सम्भावित)। सन्धि जाँची: पर्व + अस्थि → पर्वास्थि (अ + अ → आ)।"),
    "17": ("पद्य; विश्वास कम; दो छपी पंक्तियाँ (०२.११.३० और ०२.११.३१)। पाठ-चिह्न (सम्भव): ‘सतृट्का मज्वर-’ विश्लेषित नहीं होता; "
           "स/म के भ्रम से ‘सतृट् कास, ज्वर-’ पढ़ा गया (अनुमानित), इसलिए पहली पंक्ति पर प्रश्न नहीं। प्रवाहिका = पेचिश (सम्भावित)। "
           "डेटा पहली पंक्ति को कार्ड १३-१६ के अतिसार/मल का वर्णन मानता है। अश्मरी = मूत्र की पथरी (मानक)। "
           "क्रिया कार्ड ४ (छपी पंक्ति ४) से चली आ रही। छपा ‘रुजार्दितं’ = रुजार्दितम् (पंक्ति के अन्त में अनुस्वार)। "
           "सन्धि जाँची: रुजा + अर्दितम् → रुजार्दितम् (आ + अ → आ)।"),
    "18": ("पद्य; विश्वास मध्यम; दो छपी पंक्तियाँ (०२.११.३२ और ०२.११.३३)। पाठ-चिह्न (सम्भव): ‘तुद्द्वाह’ में भटका व्, ‘तुद्दाह’ पढ़ा गया; "
           "समीक्षक के अनुसार ‘तुद्’ स्वतन्त्र संज्ञा के रूप में प्रमाणित नहीं, ‘तृड्दाह’ (प्यास, दाह) भी सम्भव। ‘हत्’ को ‘हृत्’ (हृदय) पढ़ना अनुमान। इन पर प्रश्न नहीं। "
           "मेह = प्रमेह, सम्भवतः मधुमेह वाला रूप (सम्भावित)। मर्म शास्त्रीय शब्द के रूप में रखा गया। स्थान-सूची कार्ड १९ (छपी पंक्ति ३४) में जारी। "
           "सन्धि जाँची: मेहः + त- → मेहस्त- (त से पहले ः → स्); पिटिकाः + मर्म- → पिटिका मर्म- (आः घोष वर्ण से पहले विसर्ग खोता है)।"),
    "19": ("पद्य; विश्वास मध्यम; दो छपी पंक्तियाँ (०२.११.३४ और ०२.११.३५); कार्ड १८ जारी। पाठ-चिह्न (सम्भव): छपा ‘मंदोत्साहंप्रमेहिण’ = "
           "मन्दोत्साहं प्रमेहिणम् (अन्तिम अनुस्वार छूटा, रिक्त स्थान नहीं)। ‘पिटिका’ शब्द यहाँ छपा नहीं, केवल अंग्रेज़ी में कोष्ठक में। "
           "‘वा’ विभाजक अर्थ में पढ़ा गया। ‘सर्वम्’ किसके लिए, यह नहीं कहा गया; उस पर प्रश्न नहीं। "
           "सन्धि जाँची: मन्द + उत्साह → मन्दोत्साह (अ + उ → ओ); सर्वम् + च → सर्वं च (व्यंजन से पहले म् → ं)।"),
    "20": ("पद्य; विश्वास मध्यम; दो छपी पंक्तियाँ (०२.११.३६ और ०२.११.३७); कोई पाठ-चिह्न नहीं। पहली पंक्ति कार्ड १९ की तृतीया-सूची जारी रखती है। "
           "विसर्प और गुल्म के आधुनिक नाम सम्भावित (डेटा का लेबल)। मर्मसंरोध = मर्मों की रुकावट। "
           "देवनागरी में ‘कूर्मइवोन्नतः’ छपा; IAST का kūrmaiva प्रविष्टि की भूल है, छपाई की नहीं। "
           "सन्धि जाँची: पृथुपरीणाहः + घनः → पृथुपरीणाहो घनः (अः + घोष व्यंजन → ओ); कूर्मः + इव → कूर्म इव (अः + अ से भिन्न स्वर → अ); इव + उन्नतः → इवोन्नतः (अ + उ → ओ)।"),
    "21": ("पद्य; विश्वास मध्यम; दो छपी पंक्तियाँ (०२.११.३८ और ०२.११.३९); कोई पाठ-चिह्न नहीं। डेटा इसे कार्ड २० के गुल्म का वर्णन मानता है (प्रथमा)। "
           "सिरा = नस या वाहिका (सम्भावित); पीनस = पुराना जुकाम (सम्भावित)। ‘हिध्माऽध्मान’ में ऽ छपाई की आदत (आ + आ → आ)। "
           "सन्धि जाँची: सिरानद्धः + ज्वर- → सिरानद्धो ज्वर- (अः + घोष व्यंजन → ओ); डेटा पीड़ा के लिए ‘रुज्’ देता है, पर छपा ‘रुजान्वितः’ रुजा + अन्वितः (आ + अ → आ) से बनता है (रुज् + अन्वितः से ‘रुजन्वितः’ होता); इस सन्धि पर प्रश्न नहीं।"),
    "22": ("पद्य; विश्वास मध्यम; दो छपी पंक्तियाँ (०२.११.४० और ०२.११.४१); कोई पाठ-चिह्न नहीं। डेटा के अनुसार वाक्य कार्ड २१ से चलकर यहाँ ‘हन्ति’ पर पूरा होता है; "
           "‘हन्ति’ कार्ड ४ (छपी पंक्ति ४) के ‘निहन्ति’ से मेल खाता है। जठर = पेट; यहाँ पेट का रोग, सम्भवतः जलोदर प्रकार (सम्भावित)। "
           "छपा ‘हंति’ = हन्ति, ‘दुर्बलं’ = दुर्बलम्। ‘विण्मूत्र’ = विट् + मूत्र (ट् अनुनासिक से पहले विकल्प से ण्; इस पर प्रश्न नहीं)। "
           "सन्धि जाँची: छर्दि + अतिसारैः → छर्द्यतिसारैः (इ + अ → य); अतिसारैः + च → अतिसारैश्च (च से पहले ः → श्); जठरम् + हन्ति → जठरं हन्ति।"),
    "23": ("गद्य (डेटा का प्रकार; छन्द पर कोई प्रश्न नहीं); विश्वास कम; दो छपी पंक्तियाँ (०२.११.४२ और ०२.११.४३)। "
           "पाठ-चिह्न (सम्भव): ‘विरेचनहतानाम्’ (षष्ठी बहुवचन) द्वितीया ‘आनह्यन्तम्’ से मेल नहीं खाता; ‘विरेचनहतम्’ अनुमानित पाठ है, बीच में ‘च’ था या नहीं, अज्ञात। "
           "‘आनह्यन्तम्’ असामान्य परस्मैपद रूप (आनह्यमानम् अपेक्षित)। इन पर प्रश्न नहीं। उपस्थ = जननांग (मानक)। कोई क्रिया नहीं; डेटा इसे कार्ड २२ के दुर्बल रोगी का वर्णन मानता है। "
           "सन्धि जाँची: शून + अक्षम् → शूनाक्षम् (अ + अ → आ); कुटिल + उपस्थम् → कुटिलोपस्थम् (अ + उ → ओ); उपस्थम् + उपक्लिन्न- → उपस्थमुपक्लिन्न-।"),
    "24": ("पद्य; विश्वास मध्यम; दो छपी पंक्तियाँ (०२.११.४४ और ०२.११.४५); कोई पाठ-चिह्न नहीं। डेटा के अनुसार छपी पंक्तियाँ ४४-४७ (कार्ड २४-२५) एक वर्णन हैं, "
           "‘हन्ति’ केवल कार्ड २५ में। ‘पीत’ आँख और नख दोनों के साथ लिया गया (डेटा का पाठ)। पाण्डुरोग = रक्ताल्पता (मानक); श्वयथु = शोफ (मानक)। "
           "‘मूर्च्छाऽध्मान’ में ऽ छपाई की आदत; ‘च्छर्द्दि’ में द्द छपाई की वर्तनी। "
           "सन्धि जाँची: दाह + अरुचि → दाहारुचि (अ + अ → आ); अरुचि + छर्दि → अरुचिच्छर्दि (ह्रस्व स्वर के बाद छ → च्छ); मूर्च्छा + आध्मान → मूर्च्छाध्मान (आ + आ → आ)।"),
    "25": ("पद्य; विश्वास मध्यम; दो छपी पंक्तियाँ (०२.११.४६ और ०२.११.४७); कोई पाठ-चिह्न नहीं। ‘प्रसृतम्’ नरम् से मेल खाता है, पर क्या फैला, छपा नहीं; "
           "डेटा शोफ को सम्भावित कर्ता मानता है (अनुमान)। ‘पादाभ्याम्’ पञ्चमी, तृतीया (या चतुर्थी) द्विवचन हो सकता है; ‘से’ लिया गया, विभक्ति पर प्रश्न नहीं। "
           "‘उभौ’ सम्भवतः नर और नारी (अनुमान)। ‘मुखात्’ शब्दशः ‘मुख/चेहरे से’। ‘हन्ति’ संस्कृत में एक बार। "
           "सन्धि जाँची: अनेक + उपद्रव → अनेकोपद्रव (अ + उ → ओ); मुखात् + हन्ति → मुखाद्धन्ति (त् → द्, ह विकल्प से ध; मुखाद्हन्ति भी मान्य); "
           "कुक्षिगुह्यात् + उभौ → -गुह्यादुभौ (स्वर से पहले त् → द्); उभौ + अपि → उभावपि (औ + स्वर → आव्)।"),
}

# ================================================================ AIDS
AIDS = {
    "14": {
        "diagram": {"groups": [
            {"label": "अति (बहुत), फिर छपे क्रम में",
             "items": ["१ रक्त: लाल", "२ असित: काला", "३ स्निग्ध: चिकना", "४ पूति: सड़ा", "५ अच्छ: स्वच्छ",
                       "६ घन: घना", "७ वेदन: पीड़ा वाला"]}]},
        "chunks": "मस्तु लुंगमषीपूयवेसवारंबुमाक्षिकैः || अति | रक्तासितस्निग्धपूत्यच्छघनवेदनः",
        "sandhi": "अ + अ → आ: रक्त + असित → रक्तासित · इ + अ → य: पूति + अच्छ → पूत्यच्छ।",
        "anchors": "पक्का: मषी (कालिख), पूय (मवाद), माक्षिक (शहद) और पंक्ति २ के सात गुण। अनुमान: मस्तुलुङ्ग, अम्बु। (मेरी याद-पद्धति)",
    },
    "15": {
        "chunks": "कर्बुरः | प्रस्रवन्धात्त्रिष्पूरीषोऽथवाऽतिविट् || तंतुमान्मसिकाक्रांतो | राजैर्मांसेंद्रकैर्युतः",
        "frame": "पक्का: कर्बुर (चितकबरा) → अथवा अतिविट् (या बहुत मल) → तन्तुमान् (तन्तुओं वाला) → मसिकाक्रान्त (कालिख-कणों से भरा) → युत (युक्त)। अस्पष्ट: दो खण्ड।",
        "sandhi": "आ + अ → आ: अथवा + अतिविट् → अथवातिविट् (छपाई में ऽ)।",
    },
    "16": {
        "chunks": "शीर्णपायुवालिं | मुक्तनालं | पर्वास्थिशूलिनं || स्रस्तपायुं | बलक्षीणमन्नेवोपवेशयन्",
        "frame": "पक्का: पर्वास्थिशूली (जोड़-हड्डी में शूल) · स्रस्तपायु (गुदा खिसकी, सम्भवतः गुदभ्रंश) · बलक्षीण (बल क्षीण)। अनुमान/अस्पष्ट: वलि, नाल, अन्तिम शब्द।",
        "sandhi": "अ + अ → आ: पर्व + अस्थि → पर्वास्थि।",
        "anchors": "शूल + इन् = शूलिन् (शूल वाला): -इन् = ‘वाला’। (मेरी याद-पद्धति)",
    },
    "17": {
        "chain": {"steps": ["अश्मरी: मूत्र की पथरी", "शूनवृषणम्: सूजे वृषण वाला", "बद्धमूत्रम्: रुके मूत्र वाला",
                            "रुजार्दितम्: पीड़ा से पीड़ित"]},
        "chunks": "सतृट्का मज्वरच्छर्द्दिदाहानाहप्रवाहिकः || अश्मरी | शूनवृषणं | बद्धमूत्रं | रुजार्दितं",
        "sandhi": "आ + अ → आ: रुजा + अर्दितम् → रुजार्दितम्।",
    },
    "18": {
        "diagram": {"groups": [
            {"label": "पिटिकाओं के स्थान (छपे क्रम में)",
             "items": ["१ मर्म", "२ हत् (अनुमान: हृत्, हृदय)", "३ पृष्ठ: पीठ", "४ स्तन", "५ अंस: कन्धा", "६ गुद: गुदा",
                       "७ मूर्द्ध: सिर"]}]},
        "chunks": "मेहस्तुद्द्वाहपिटकामांसकोथातिसारिणं || पिटिका | मर्महत्पृष्ठस्तनांसगुदमूर्द्धगाः",
        "sandhi": "त से पहले ः → स्: मेहः + त- → मेहस्त- · आः घोष वर्ण से पहले विसर्ग खोता है: पिटिकाः + मर्म- → पिटिका मर्म-।",
        "pegs": "पीठ से सिर तक: पृष्ठ, स्तन, अंस, गुद, मूर्ध; ‘पीठ-स्तन-कन्धा-गुदा-सिर’। (मेरा बनाया स्मरण-सूत्र)",
    },
    "19": {
        "chunks": "पर्वपादकरस्था वा | मंदोत्साहंप्रमेहिण || सर्वं च | मांससंकोथदाहतृष्णामदज्वरैः",
        "chain": {"steps": ["मांससंकोथ: मांस का सड़ना", "दाह: जलन", "तृष्णा: प्यास", "मद: नशा", "ज्वर: बुखार"]},
        "sandhi": "अ + उ → ओ: मन्द + उत्साह → मन्दोत्साह · व्यंजन से पहले म् → ं: सर्वम् + च → सर्वं च।",
    },
    "20": {
        "diagram": {"groups": [
            {"label": "गुल्म (सम्भवतः पेट की गाँठ)",
             "items": ["पृथुपरीणाहः: चौड़े घेरे वाला", "घनः: घना", "कूर्म इव उन्नतः: कछुए-सा उठा"]}]},
        "chunks": "विसर्पमर्मसंरोधहिध्माश्वासभ्रमक्लमैः || गुल्मः | पृथुपरीणाहो | घनः | कूर्मइवोन्नतः",
        "sandhi": ("अः + घोष व्यंजन → ओ: पृथुपरीणाहः + घनः → पृथुपरीणाहो घनः · अः + अ से भिन्न स्वर → अ: कूर्मः + इव → कूर्म इव · "
                   "अ + उ → ओ: इव + उन्नतः → इवोन्नतः।"),
        "anchors": "कछुए की उभरी पीठ = उठा हुआ गुल्म: कूर्म इव उन्नतः। (मेरी याद-पद्धति)",
    },
    "21": {
        "chunks": "सिरानद्धो | ज्वरच्छर्द्दिहिध्माऽध्मानरुजान्वितः || कासपीनसहृल्लासश्वासातीसारशोफवान्",
        "chain": {"steps": ["कास: खाँसी", "पीनस: सम्भवतः पुराना जुकाम", "हृल्लास: मिचली", "श्वास: साँस फूलना",
                            "अतीसार: दस्त", "शोफ: सूजन"]},
        "sandhi": "अः + घोष व्यंजन → ओ: सिरानद्धः + ज्वर- → सिरानद्धो ज्वर-।",
    },
    "22": {
        "diagram": {"groups": [
            {"label": "इनके साथ (छपे क्रम में)",
             "items": ["१ मल-मूत्र का रुकना", "२ श्वास", "३ शोफ", "४ हिध्मा", "५ ज्वर", "६ भ्रम", "७ मूर्च्छा",
                       "८ छर्दि", "९ अतिसार", "फल: जठरं हन्ति दुर्बलम्"]}]},
        "chunks": "विण्मूत्रसंग्रहश्वासशोफहिध्माज्वरभ्रमैः || मूर्च्छाछर्द्यतिसारैश्च | जठरं | हंति | दुर्बलं",
        "sandhi": "इ + अ → य: छर्दि + अतिसारैः → छर्द्यतिसारैः · च से पहले ः → श्: अतिसारैः + च → अतिसारैश्च।",
        "frame": "कर्ता: जठरम् (पेट का रोग, सम्भावित) → क्रिया: हन्ति (मारता है) → कर्म: दुर्बलम् (दुर्बल को) → साथ: तृतीया के नौ लक्षण।",
    },
    "23": {
        "chunks": "शूनाक्षं | कुटिलोपस्थमुपक्लिन्नतनुत्वचं || विरेचनहतानामानह्यंतं | पुनः पुनः",
        "frame": "पक्का: शूनाक्ष (सूजी आँखें) · कुटिलोपस्थ (टेढ़ा उपस्थ) · उपक्लिन्नतनुत्वच् (गीली पतली त्वचा) · पुनः पुनः। अनुमान: विरेचनहत।",
        "sandhi": "अ + उ → ओ: कुटिल + उपस्थम् → कुटिलोपस्थम् · स्वर से पहले म् जुड़ता है: उपस्थम् + उपक्लिन्न- → उपस्थमुपक्लिन्न-।",
    },
    "24": {
        "diagram": {"groups": [
            {"label": "पाण्डुरोग के साथ (छपे क्रम में)",
             "items": ["श्वयथु: सूजन", "पीली आँखें और नाखून", "तन्द्रा: ऊँघ", "दाह: जलन", "अरुचि: भोजन में अरुचि",
                       "छर्दि: उल्टी", "मूर्च्छा", "आध्मान: अफारा", "अतिसार: दस्त"]}]},
        "chunks": "पांडुरोगः | श्वयथुमान् | पीताक्षिनखदर्शनं || तंद्रादाहारुचिच्छर्द्दिमूर्च्छाऽध्मानातिसारवान्",
        "sandhi": "अ + अ → आ: दाह + अरुचि → दाहारुचि · ह्रस्व स्वर के बाद छ → च्छ: अरुचि + छर्दि → अरुचिच्छर्दि।",
    },
    "25": {
        "contrast": "नर (पुरुष): दोनों पैरों से फैला हुआ ⇄ नारी (स्त्री): मुख से; उभौ (दोनों, सम्भवतः नर-नारी): कुक्षि और गुह्य से। सब इसी इकाई में।",
        "chunks": "अनेकोपद्रवयुतः | पादाभ्यां | प्रसृतं नरं || नारीं | शोफो | मुखाद्धंति | कुक्षिगुह्यादुभावपि",
        "sandhi": ("त् घोष ह से पहले → द्, ह विकल्प से ध: मुखात् + हन्ति → मुखाद्धन्ति · स्वर से पहले त् → द्: -गुह्यात् + उभौ → -गुह्यादुभौ · "
                   "औ + स्वर → आव्: उभौ + अपि → उभावपि।"),
        "pegs": "पुरुष नीचे से (पैर), स्त्री ऊपर से (मुख), दोनों बीच से (पेट, गुह्य)। (मेरा बनाया स्मरण-सूत्र)",
    },
}

# ================================================================ IMAGE_SPECS
IMAGE_SPECS = {
    ("14", "diagram"): {
        "file": "sh11-guna-14.svg",
        "alt": ("Table of card 14, line 2, in printed order after ati (very): red, black, unctuous, putrid, clear, thick, "
                "with pain."),
        "type": "table",
        "title": "कार्ड १४: अति ... (छपे क्रम में)",
        "heads": ["क्रम", "छपा शब्द: अर्थ"],
        "rows": [["१", "रक्त: लाल"], ["२", "असित: काला"], ["३", "स्निग्ध: चिकना"], ["४", "पूति: सड़ा"],
                 ["५", "अच्छ: स्वच्छ"], ["६", "घन: घना"], ["७", "वेदन: पीड़ा वाला"]],
    },
    ("18", "diagram"): {
        "file": "sh11-pitika-18.svg",
        "alt": ("Table of card 18: the sites of the boils in printed order: vital spots, hat (conjecture: heart), back, "
                "breast, shoulder, anus, head."),
        "type": "table",
        "title": "कार्ड १८: पिटिकाओं के स्थान",
        "heads": ["क्रम", "छपा शब्द: अर्थ"],
        "rows": [["१", "मर्म"], ["२", "हत्: अनुमान हृत् (हृदय)"], ["३", "पृष्ठ: पीठ"], ["४", "स्तन"],
                 ["५", "अंस: कन्धा"], ["६", "गुद: गुदा"], ["७", "मूर्द्ध: सिर"]],
    },
    ("20", "diagram"): {
        "file": "sh11-gulma-20.svg",
        "alt": ("Table of card 20: the gulma (abdominal lump, probable) is broad in girth, dense, and raised like a tortoise."),
        "type": "table",
        "title": "कार्ड २०: गुल्म (सम्भवतः पेट की गाँठ)",
        "heads": ["छपा शब्द", "अर्थ"],
        "rows": [["पृथुपरीणाहः", "चौड़े घेरे वाला"], ["घनः", "घना"], ["कूर्म इव उन्नतः", "कछुए-सा उठा"]],
    },
    ("22", "diagram"): {
        "file": "sh11-jathara-22.svg",
        "alt": ("Table of card 22 in printed order: retention of faeces and urine, breathlessness, swelling, hiccup, fever, "
                "giddiness, fainting, vomiting, diarrhoea; result: jaṭhara (belly disorder, probable) kills the weak one."),
        "type": "table",
        "title": "कार्ड २२: जठरं हन्ति दुर्बलम्",
        "heads": ["क्रम", "साथ के लक्षण"],
        "rows": [["१", "मल-मूत्र का रुकना"], ["२", "श्वास"], ["३", "शोफ: सूजन"], ["४", "हिध्मा: हिचकी"], ["५", "ज्वर"],
                 ["६", "भ्रम: चक्कर"], ["७", "मूर्च्छा"], ["८", "छर्दि: उल्टी"], ["९", "अतिसार: दस्त"],
                 ["फल", "जठर दुर्बल को मारता है"]],
    },
    ("24", "diagram"): {
        "file": "sh11-pandu-24.svg",
        "alt": ("Table of card 24: pāṇḍu disease (anaemia with pallor) with swelling, yellow eyes and nails, drowsiness, "
                "burning, distaste for food, vomiting, fainting, distension and diarrhoea."),
        "type": "table",
        "title": "कार्ड २४: पाण्डुरोग के साथ",
        "heads": ["क्रम", "छपा शब्द: अर्थ"],
        "rows": [["१", "श्वयथु: सूजन"], ["२", "पीत अक्षि-नख"], ["३", "तन्द्रा: ऊँघ"], ["४", "दाह: जलन"],
                 ["५", "अरुचि: भोजन में अरुचि"], ["६", "छर्दि: उल्टी"], ["७", "मूर्च्छा"], ["८", "आध्मान: अफारा"],
                 ["९", "अतिसार: दस्त"]],
    },
    ("25", "contrast"): {
        "file": "sh11-shopha-25.svg",
        "alt": ("Table of card 25: swelling kills a man spread from the two feet (what spread is not printed), a woman from "
                "the face, and both (probably man and woman) from the belly and private parts."),
        "type": "table",
        "title": "कार्ड २५: शोफ हन्ति",
        "heads": ["किसे", "कहाँ से"],
        "rows": [["नर: पुरुष", "दोनों पैरों से फैला"], ["नारी: स्त्री", "मुख से"], ["उभौ: दोनों", "कुक्षि और गुह्य से"]],
    },
}
