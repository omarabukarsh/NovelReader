# -*- coding: utf-8 -*-
"""Guide content taken from the reference Telegram channel (Competenze Cliniche 313).

Checklist  = (title, phases, important_points, source)   source: "channel" | "std"
Phase      = (name, note, items)
Item       = (step, how / what you may find, optional figure id)
Histories  = list of channel post ids (Arabic question scripts) rendered verbatim.
"""

INTRO = lambda expose, position, extra=(): ("Introduction", "", [
    ("Wash hands", ""),
    ("Introduce yourself", "Marks in every station — never skip it"),
    ("Confirm name and age", ""),
    ("Explain the examination, obtain consent", ""),
    *extra,
    ("Exposure", expose),
    ("Position", position),
])

TOPICS = [
# =====================================================================================
dict(
    id="pvd", num=1, title="Peripheral Vascular Disease",
    subtitle="Lower-limb ischaemia · peripheral pulses · varicose veins · DVT · lower-limb swelling",
    ar="محطة الأوعية الدموية: فحص نقص التروية في الطرف السفلي، النبض الطرفي، الدوالي، الجلطة الوريدية العميقة، وتورّم الساق. "
       "القاعدة: قارن دائماً بين الطرفين، وتأكد من النبض وزمن عودة الامتلاء الشعري.",
    checklists=[
        ("Lower limb ischaemia examination", [
            INTRO("From groin to toes", "Lying flat"),
            ("End of bed inspection", "", [
                ("Look around the bed", "Walking aid, wheelchair, dressings, amputation, footwear"),
            ]),
            ("Inspection of both lower limbs", "", [
                ("Symmetry", ""),
                ("Colour", "Pallor, ischaemic rubor, colour changes"),
                ("Trophic changes", "Hair loss, shiny skin, muscle wasting"),
                ("Ulcers, gangrene, necrosis", ""),
                ("Scars, toe deformities, amputation", ""),
                ("Between the toes &amp; heels", "Hidden ulcers"),
            ]),
            ("Palpation", "", [
                ("Temperature", "Compare both limbs; temperature gradient thigh → foot", "pvd_temperature"),
                ("Tenderness", ""),
                ("Capillary refill time", "Great toe", "pvd_cap_refill"),
                ("Femoral pulse", "Presence, rate, rhythm, volume; auscultate for bruit if weak", "pvd_femoral_pulse"),
                ("Popliteal pulse", "", "pvd_popliteal_pulse"),
                ("Posterior tibial pulse", "", "pvd_pt_pulse"),
                ("Dorsalis pedis pulse", "Compare both sides", "pvd_dp_pulse"),
            ]),
            ("Buerger’s test", "", [
                ("Raise both legs to 45°", "Observe Buerger’s angle (pallor)", "pvd_buerger"),
                ("Sit the patient up, legs hanging", "Observe dependent rubor (reactive hyperaemia)"),
            ]),
            ("Neurological assessment", "", [
                ("Sensory", "Fine touch, pinprick, vibration, proprioception"),
                ("Motor", "Dorsiflexion, plantarflexion"),
            ]),
            ("Special examination", "", [("ABPI", "See ABPI table")]),
            ("Completion", "", [
                ("To complete", "Cardiovascular exam, contralateral limb, blood glucose, Doppler / vascular investigations"),
                ("Thank patient, wash hands", ""),
            ]),
        ], ["Hair loss", "Shiny skin", "Temperature", "Capillary refill time", "Femoral, popliteal, PT, DP pulses",
            "Buerger’s test", "Neurological assessment", "ABPI"]),
        ("Peripheral pulse examination (upper limb, neck, abdomen, lower limb)", [
            INTRO("Neck, upper limbs, abdomen and lower limbs", "Supine"),
            ("General inspection", "", [
                ("Patient", "Comfortable? Treatment / adjuncts, scars, central / peripheral cyanosis, limb pallor"),
            ]),
            ("Upper limb", "", [
                ("Inspection", "Colour, finger necrosis / gangrene, Buerger’s disease, tar staining, tendon xanthomata"),
                ("CRT &amp; temperature", "Compare both sides"),
                ("Radial pulse", "Rate, rhythm, volume, both sides, radio-radial delay"),
                ("Brachial pulse", "Rate, rhythm, volume, both sides"),
                ("Collapsing pulse", "If requested"),
            ]),
            ("Neck", "", [
                ("Carotid arteries", "Auscultate for bruit first, then palpate <b>one at a time</b>; volume"),
            ]),
            ("Abdomen", "", [
                ("Inspection", "Scars, sinuses, dilated veins, pulsatile mass (AAA)"),
                ("Palpate the abdominal aorta", ""),
                ("Auscultation", "Aortic bruit, right &amp; left renal artery bruits"),
            ]),
            ("Lower limb", "", [
                ("Inspection", "Scars, ischaemic pallor, dependent rubor, ulcers, hair loss, muscle wasting, hidden ulcers"),
                ("Gross motor", "Raise both legs, dorsiflex both feet"),
                ("Temperature &amp; great-toe CRT", ""),
                ("Femoral pulse", "Rate, rhythm, volume, both sides, radio-femoral delay, femoral bruit", "pvd_femoral_pulse"),
                ("Popliteal → posterior tibial → dorsalis pedis", "In this order", "pvd_popliteal_pulse"),
                ("Fine touch sensation", ""),
                ("Buerger’s test", "Legs to 45° → pallor; sit up → dependent rubor"),
            ]),
            ("Completion", "", [
                ("To complete", "Blood pressure, Doppler, ABPI"),
                ("Help patient dress, thank, wash hands", ""),
            ]),
        ], ["Compare both limbs", "Pulses in order: femoral → popliteal → PT → DP", "Radio-radial &amp; radio-femoral delay",
            "Carotid, aortic &amp; femoral bruits", "Always assess for AAA", "Buerger’s test", "Mention Doppler &amp; ABPI"]),
        ("Varicose veins examination", [
            INTRO("Waist to feet", "<b>Standing</b>", extra=[("Ensure privacy", "")]),
            ("Inspection", "front, side and back", [
                ("Dilated tortuous veins", "Distribution: GSV / SSV"),
                ("Skin", "Pigmentation, varicose eczema, lipodermatosclerosis, atrophie blanche, cellulitis"),
                ("Venous ulcer, oedema, scars, muscle wasting", ""),
            ]),
            ("Palpation", "", [
                ("Temperature", ""),
                ("Tenderness along veins", "Thrombophlebitis"),
                ("Pitting oedema", ""),
                ("Peripheral pulses &amp; CRT", "Femoral, popliteal, DP, PT"),
            ]),
            ("Clinical tests", "", [
                ("Cough impulse test", ""),
                ("Tap (percussion) test", ""),
            ]),
            ("Special tests", "", [
                ("Trendelenburg test", "Elevate leg, empty veins, tourniquet at SFJ, stand; watch filling before &amp; after release; repeat lower", "pvd_tourniquet"),
                ("Perthes test", "Tourniquet at mid-thigh, patient walks 5 min; veins empty or distend?"),
            ]),
            ("Completion", "", [
                ("To complete", "Duplex venous ultrasound; ABPI if arterial disease suspected"),
                ("Thank patient, wash hands", ""),
            ]),
        ], ["Examine the patient standing", "GSV / SSV distribution", "Chronic venous insufficiency signs",
            "Trendelenburg &amp; Perthes — know their purpose", "Always mention duplex ultrasound"]),
        ("DVT examination", [
            INTRO("Mid-thigh to feet", "Lying flat"),
            ("Inspection", "compare both lower limbs", [
                ("Swelling &amp; calf asymmetry", ""),
                ("Skin", "Erythema, dilated superficial veins, discoloration, ulcers or scars"),
                ("Between toes, heels &amp; calves", "Pressure ulcers"),
                ("Signs of pulmonary embolism", ""),
            ]),
            ("Palpation", "", [
                ("Temperature", "Compare both legs"),
                ("Tenderness", "Along both limbs"),
                ("Calf circumference", "10 cm below the tibial tuberosity; compare", "pvd_calf_measure"),
                ("Posterior tibial &amp; dorsalis pedis pulses", ""),
                ("Pitting oedema", "Over the tibia", "pvd_pitting"),
                ("Homan’s sign", "If performed — low sensitivity, not reliable"),
            ]),
            ("Completion", "", [
                ("To complete", "Respiratory exam, ECG, cardiac enzymes"),
                ("Thank, cover, wash hands", ""),
            ]),
        ], ["Calf swelling &amp; asymmetry", "Calf circumference 10 cm below tibial tuberosity", "Tenderness, warmth, erythema",
            "Pitting oedema", "Peripheral pulses", "Signs of PE"]),
        ("Lower limb swelling examination", [
            INTRO("Above the knee", "Supine", extra=[("Ensure privacy", "")]),
            ("Inspection", "front, side and back", [
                ("Swelling", "Unilateral / bilateral, size and extent, ankle / dorsum of foot"),
                ("Skin", "Colour, redness, shiny, ulcers, scars, pigmentation, eczema"),
                ("Veins, muscle wasting, foot deformities", ""),
            ]),
            ("Palpation", "", [
                ("Temperature", "Dorsum of hand, compare"),
                ("Tenderness", ""),
                ("Describe the swelling", "Site, size, shape, surface, edge, consistency, fluctuation, compressibility, reducibility, mobility, skin"),
                ("Pitting oedema", "Press over medial malleolus and shin for 5 s", "pvd_pitting"),
                ("Calf circumference", "Same level, 10 cm below tibial tuberosity", "pvd_calf_measure"),
                ("DP &amp; PT pulses, CRT &lt; 2 s", ""),
            ]),
            ("Completion", "", [
                ("Mention systemic causes", "Cardiac, respiratory and abdominal examination (ascites, liver disease)"),
                ("Thank, cover, wash hands", ""),
            ]),
        ], ["Unilateral vs bilateral", "Pitting oedema", "Calf measurement difference", "DVT red flags (tenderness, warmth)", "Peripheral pulses"]),
    ],
    tables=[dict(title="ABPI (from the channel)", head=["ABPI", "Meaning"],
                 rows=[["1.0 – 1.4", "Normal"], ["0.9 – 1.0", "Acceptable"], ["0.5 – 0.9", "PAD"], ["&lt; 0.5", "Severe ischaemia"]])],
    quiz=[("Definition of intermittent claudication?", ""), ("Mention the 6 Ps of acute limb ischaemia.", ""),
          ("Definition of rest pain?", ""), ("Risk factors of atherosclerosis?", ""), ("Special tests of varicose veins?", ""),
          ("What is Virchow’s triad?", ""), ("Clinical picture of acute ischaemia?", ""), ("Signs of chronic ischaemia?", ""),
          ("What does a negative Perthes’ test indicate?", ""), ("ABPI below 0.5 indicates?", "Severe ischaemia")],
    tips=["Varicose veins in one exam: inspection + only the first two tests (cough impulse and tap test)."],
    histories=["69"],
),
# =====================================================================================
dict(
    id="thy", num=2, title="Thyroid &amp; Cervical Lymph Nodes",
    subtitle="General examination related to thyroid · local thyroid examination · cervical lymph nodes",
    ar="ثلاث لجان: الفحص العام المرتبط بالغدة (اليدين، الوجه، العينين، الرجلين)، الفحص الموضعي للغدة (نظر، جسّ من قدام ومن وراء، قرع، تسمّع)، "
       "وفحص العقد اللمفاوية العنقية بالترتيب من submental إلى supraclavicular.",
    checklists=[
        ("General examination related to thyroid", [
            INTRO("Neck to nipple level, hands above the elbows, legs up to the knees", "Comfortable, not anxious", extra=[("Ensure privacy", "")]),
            ("Hands", "", [
                ("Dorsum", "Dry skin → hypo; warm sweaty → hyper; thyroid acropachy (Graves’)"),
                ("Fine tremor", "Paper test", "thy_tremor"),
                ("Palms", "Dry or sweaty, palmar erythema"),
                ("Pulse", "Tachycardia → hyper; bradycardia → hypo"),
                ("Reflexes", "Brisk → hyper; delayed relaxation → hypo"),
            ]),
            ("Face", "", [("Skin &amp; eyebrows", "Dry or sweaty; loss of lateral third of eyebrow → hypo")]),
            ("Eyes", "", [
                ("Inspection", "Excess blinking, lid retraction, exophthalmos"),
                ("Special tests", "H eye movements, lid lag, forehead wrinkling (absent = positive)", "thy_lidlag"),
            ]),
            ("Lower limbs", "", [
                ("Myxoedema", "Non-pitting swelling → hypo"),
                ("Knee reflex", "Brisk → hyper; delayed → hypo"),
            ]),
            ("Completion", "", [
                ("Say", "“I would like to examine the cervical lymph nodes.”"),
                ("Thank, cover, wash hands", ""),
            ]),
        ], ["Thyroid eye signs (lid lag, exophthalmos)", "Fine tremor (paper test)", "Pulse changes", "Reflex changes",
            "Myxoedema (non-pitting)", "Eyebrow loss", "Link findings to hypo vs hyper"]),
        ("Local thyroid examination", [
            INTRO("Neck down to nipple level", "Sitting; stand at the patient’s right side", extra=[("Ensure privacy", "")]),
            ("Inspection", "patient sitting at the same level as you", [
                ("Scars, sinus, veins, skin", "No Kocher’s scar, no thyroglossal sinus, no dilated veins, no discoloration"),
                ("Swelling or mass", "If present describe with the 6S: site, size, shape, surface, skin over it, special tests"),
                ("Swallowing test", "Moves on swallowing → thyroid swelling", "thy_swallow"),
                ("Tongue protrusion test", "Moves → thyroglossal cyst; no movement → other neck mass", "thy_tongue"),
            ]),
            ("Palpation", "ask about pain first", [
                ("From the front — 3T", "Temperature (compare lobes), tenderness, tracheal position", "thy_trachea"),
                ("From behind", "Patient flexes the neck slightly; both hands, palpate each lobe", "thy_palpation"),
                ("Describe a mass", "Site, size, shape, surface, consistency, mobility, attachment to skin / deep tissues"),
                ("Repeat swallowing &amp; tongue tests", "While palpating"),
                ("Lymph nodes", "Say: “I would like to examine the cervical lymph nodes.”"),
            ]),
            ("Percussion", "", [("Over the sternum", "Resonant = normal; dull = retrosternal extension")]),
            ("Auscultation", "", [
                ("Over the thyroid", "Bruit → hypervascular thyroid (Graves’)"),
                ("Carotid arteries", "Bruit"),
            ]),
            ("Completion", "", [("Thank, cover, wash hands", "")]),
        ], ["Moves on swallowing = thyroid", "Moves with tongue = thyroglossal cyst", "6S description of the mass",
            "Tracheal deviation", "Mention cervical lymph nodes", "Dull sternum = retrosternal extension", "Thyroid bruit (Graves’)"]),
        ("Cervical lymph node examination", [
            INTRO("Neck down to nipple level", "Sitting comfortably"),
            ("Inspection", "", [
                ("Neck", "Swellings, scars, skin changes (redness, ulceration), sinuses / discharge, asymmetry"),
            ]),
            ("Palpation", "from behind, both hands, index &amp; middle fingers in circles; neck slightly flexed", [
                ("Submental", "Under the chin, midline"),
                ("Submandibular", "Under the mandible"),
                ("Tonsillar", "Below the angle of the mandible"),
                ("Pre-auricular (parotid)", "In front of the ear"),
                ("Post-auricular (mastoid)", "Behind the ear"),
                ("Occipital", "Back of the head"),
                ("Sternocleidomastoid — landmark", "Hand on the cheek, patient pushes against it → SCM contracts", "thy_nodes"),
                ("Anterior cervical nodes", "Along the anterior border of SCM"),
                ("Posterior cervical nodes", "Behind SCM, posterior triangle (anterior border of trapezius)"),
                ("Supraclavicular", "Left = Virchow’s node — very important"),
            ]),
            ("If a node is found", "", [
                ("Comment on", "Site, size, shape, surface, consistency, tenderness, temperature, mobility / fixity, matting or scattering"),
            ]),
            ("Completion", "", [
                ("To complete", "Oral cavity &amp; tonsils, scalp &amp; ears, thyroid, axillary &amp; inguinal nodes"),
                ("Thank, wash hands", ""),
            ]),
        ], ["Systematic order", "SCM as the landmark", "Left supraclavicular (Virchow’s)", "Full description of any node"]),
    ],
    tables=[],
    quiz=[("A man has a midline neck swelling that disappears when he protrudes his tongue — diagnosis?", "Thyroglossal cyst")],
    tips=["Short neck: ask the patient to extend the neck slightly so everything is visible.",
          "After palpating the thyroid don’t say “finished” — say you would like to examine the lymph nodes."],
    histories=["7"],
),
# =====================================================================================
dict(
    id="git1", num=3, title="GIT (I): History &amp; General Examination",
    subtitle="General GIT examination · GI history taking",
    ar="الفحص العام للجهاز الهضمي: النظرة العامة ثم اليدين ثم الرأس والرقبة ثم الصدر والبطن والمنطقة الإربية والطرف السفلي. "
       "في الامتحان قد يعطونك صورة (مثل clubbing أو palmar erythema) ويسألونك ما هي وما أسبابها.",
    checklists=[
        ("General GIT examination", [
            INTRO("Full body (as appropriate)", "Supine or 45°; ask about pain", extra=[("Ensure privacy", "")]),
            ("General look", "", [
                ("Patient", "Distressed or comfortable, in pain, dehydrated, feverish"),
                ("Hair &amp; body", "Hair distribution / loss, muscle bulk, cachexia / obesity"),
            ]),
            ("Hands", "", [
                ("Clubbing", "Liver disease — window test if unclear", "git1_hands"),
                ("Flapping tremor (asterixis)", "Hepatic encephalopathy", "git1_asterixis"),
                ("Koilonychia", "Chronic anaemia"),
                ("Palmar erythema", "Chronic liver disease"),
                ("Xanthomas", "Lipid deposition"),
                ("Dupuytren’s contracture", "Liver cirrhosis"),
                ("Also", "Bruising, pulse (rate, rhythm, volume), BP, temperature"),
            ]),
            ("Head &amp; neck", "", [
                ("Parotid enlargement, telangiectasia", "Alcohol-related liver disease"),
                ("Jaundice", "Sclera (look down, lift the lid) and under the tongue", "git1_eyes"),
                ("Pallor", "Anaemia"),
                ("Xanthelasma", "Eyelids"),
                ("Mouth", "Angular stomatitis, atrophic glossitis, central cyanosis, fetor hepaticus"),
                ("Neck", "Virchow’s node (left supraclavicular), JVP", "git1_virchow"),
            ]),
            ("Chest &amp; abdomen", "", [
                ("Chest", "Gynaecomastia (male), breast atrophy (female), spider naevi (&gt; 3 = abnormal)"),
                ("Abdomen", "Ascites, dilated veins"),
            ]),
            ("Groin, perineum &amp; lower limbs", "", [
                ("Groin &amp; perineum", "Inguinal nodes, hernia, fissure / fistula, haemorrhoids, skin tags, masses, testicular atrophy"),
                ("Lower limbs", "Oedema, purpura, pigmented ulcers, scratch marks, erythema nodosum (Crohn’s), pyoderma gangrenosum (UC), fungal infection, pulses"),
            ]),
            ("Completion", "", [("Thank, cover, apologise for the inconvenience, wash hands", "")]),
        ], ["Jaundice + asterixis", "Spider naevi (&gt; 3 abnormal)", "Ascites + dilated veins", "Palmar erythema + Dupuytren’s",
            "JVP + Virchow’s node", "Signs across systems: hands → abdomen → legs"]),
    ],
    tables=[],
    quiz=[("Five stigmata of chronic liver disease?", "Spider naevi, palmar erythema, jaundice, gynaecomastia, clubbing / leukonychia"),
          ("Extra-intestinal skin manifestations of IBD?", "Erythema nodosum, pyoderma gangrenosum, aphthous oral ulcers"),
          ("Causes of generalised abdominal distension?", "The Fs"), ("Definition of odynophagia?", ""),
          ("Definition of haematochezia?", ""), ("Causes of upper (epigastric) abdominal pain?", ""),
          ("Other organs to examine with lower GIT symptoms?", "")],
    tips=["In the general exam they may show a picture (e.g. clubbing) and ask what it is and its differential diagnosis."],
    histories=["30", "33", "36", "39", "137", "138", "139", "140", "232", "233"],
),
# =====================================================================================
dict(
    id="git2", num=4, title="GIT (II): Abdominal Examination, Ascites &amp; PR",
    subtitle="Abdominal examination for organomegaly · ascites · per-rectal examination",
    ar="فحص البطن: النظر من نهاية السرير ثم من يمين المريض، الجسّ السطحي ثم العميق من الحفرة الحرقفية اليمنى، ثم الكبد والطحال والكليتين. "
       "الاستسقاء: القرع والأصمّية المتنقلة وموجة السائل ثم التسمّع. الفحص الشرجي بوجود مرافق وفي وضعية الاستلقاء على الجانب الأيسر.",
    checklists=[
        ("Abdominal examination (organomegaly)", [
            INTRO("Ideal 2nd rib to mid-thigh; modified: male nipples → iliac crest, female inframammary → iliac crest",
                  "Supine, flat, pillow under the head, abdomen relaxed", extra=[("Ensure privacy", "")]),
            ("Inspection", "first from the end of the bed, then from the right side", [
                ("End of bed", "Shape (flat / distended / symmetrical), flank fullness, moves with respiration"),
                ("From the right side", "Scars, dilated veins (caput medusae), discoloration, bruising, scratch marks"),
                ("Dilated veins — emptying test", "Refills from umbilical side → portal hypertension; from the other side → IVC obstruction"),
                ("Cough impulse", "Patient turns the head and coughs → hernia"),
            ]),
            ("Palpation", "warm hands, ask about pain, sit at the patient’s level", [
                ("Superficial palpation", "Clockwise from the RIF: soft, no tenderness, no superficial mass, normal temperature", "git2_light_palp"),
                ("Deep palpation", "Same method: no deep masses"),
                ("Liver", "From the RIF upwards with inspiration, up to the costal margin", "git2_liver"),
                ("Liver span (percussion)", "From above (resonant → dull) and from below (tympanic → dull); measure between the two points"),
                ("Spleen", "From the RIF diagonally to the left hypochondrium, with inspiration; hooking / support at the costal margin", "git2_spleen"),
                ("Kidneys — bimanual", "One hand anterior, one posterior: ballottement", "git2_kidney"),
            ]),
            ("Completion", "", [("Thank, cover, wash hands, ensure comfort", "")]),
        ], ["Inspection from the end of the bed + right side", "Dilated veins + emptying test", "Liver → spleen → kidneys",
            "Liver palpated with respiration", "Ballotable kidney = enlarged", "Superficial before deep"]),
        ("Examination of ascites", [
            INTRO("Xiphisternum to iliac crest (ideally 2nd rib to mid-thigh)", "Supine"),
            ("Inspection", "from the end of the bed", [
                ("Abdomen", "Distension, flank fullness, everted umbilicus, tight shiny skin, reduced movement with respiration"),
                ("Also", "Scars, dilated veins (caput medusae), hernias, visible masses"),
            ]),
            ("Percussion", "ask about pain", [
                ("From the epigastrium downward", "Tympanic → dull in the flanks"),
                ("Shifting dullness", "Umbilicus → flank, patient turns to the other side, wait ~1 min, re-percuss: dullness shifts = ascites", "git2_shifting"),
                ("Fluid thrill (large ascites)", "Hand on the midline, tap one flank, feel on the other: positive = severe; negative = moderate"),
                ("Mild ascites", "Ultrasound, or knee-elbow position with reverse percussion"),
            ]),
            ("Auscultation", "", [
                ("Bowel sounds", "Right iliac fossa (ileocaecal)"),
                ("Aortic bruit", "Epigastrium, midline above the umbilicus"),
                ("Renal artery bruits", "2–3 cm above and lateral to the umbilicus, both sides"),
                ("Iliac artery bruits", "Above and medial to the ASIS, both sides"),
                ("Venous hum", "Periumbilical — portal hypertension"),
            ]),
            ("Completion", "", [
                ("Say", "“To complete, I would like to do a PR and scrotal exam, check for peripheral oedema, and review abdominal ultrasound and LFTs.”"),
                ("Thank, help dress, wash hands", ""),
            ]),
        ], ["Shifting dullness = key sign", "Fluid thrill = severe ascites", "Portal hypertension signs (caput medusae, venous hum)",
            "Inspection → percussion → auscultation", "Mild ascites → ultrasound", "Mention systemic exam at the end"]),
        ("PR (per-rectal) examination", [
            ("Preparation", "", [
                ("Wash hands, introduce yourself, confirm name &amp; age", ""),
                ("Explain", "“I would like to perform a rectal examination using a gloved finger. It may feel uncomfortable. Is that okay?”"),
                ("Consent, privacy, chaperone, curtain", ""),
                ("Position", "Left lateral (Sims), knees flexed", "git2_pr_position"),
                ("Gloves &amp; lubricant", ""),
            ]),
            ("Inspection", "gently separate the buttocks", [
                ("Perianal area", "External haemorrhoids, fissures, skin tags, discharge or bleeding, masses or ulcers"),
            ]),
            ("Digital examination", "", [
                ("Warn the patient", "“I am now going to insert my finger.” Deep breath to relax"),
                ("Anal tone", "Squeeze the finger: normal / reduced / increased"),
                ("Rectal wall", "Clockwise / anticlockwise: masses, tenderness, irregularities, stool"),
                ("Prostate (males)", "Size, surface, consistency, tenderness — normal: smooth, rubbery, non-tender, symmetrical"),
            ]),
            ("Completion", "", [
                ("Withdraw &amp; inspect the glove", "Blood or stool"),
                ("Clean the patient, dispose of gloves, wash hands", ""),
            ]),
        ], ["Chaperone + consent", "Inspect before inserting", "Tone first", "Systematic wall palpation", "Prostate: size, consistency, tenderness", "Inspect the glove"]),
    ],
    tables=[],
    quiz=[("Normal liver span?", ""), ("Name the abdominal quadrants / regions.", ""),
          ("What do you do for a patient with mild ascites?", "Ultrasound")],
    tips=["Before saying you would do PR and scrotal examination, say you would auscultate for bowel sounds and bruits.",
          "In a liver-span station you may be asked whether to palpate the liver and spleen as well."],
    histories=[],
),
# =====================================================================================
dict(
    id="uro", num=5, title="Urology",
    subtitle="Scrotal examination · renal angle &amp; kidney examination · urological histories",
    ar="فحص الصفن والمريض واقف: النظر ثم اختبار الكحة ثم الجسّ لكل جهة لوحدها، ثم اختبار الوصول فوق التورم، والتموّج، ونفاذ الضوء. "
       "وإذا كان الصفن فارغاً ابحث عن الخصية في القناة الإربية. وفحص زاوية الكلية: جسّ ثم قرع ثم الكليتين ثم التسمّع.",
    checklists=[
        ("Scrotal examination", [
            INTRO("Umbilicus to mid-thigh, genitalia exposed", "Standing (wearing his shoes)", extra=[("Privacy + chaperone", "Male nurse")]),
            ("Inspection", "front and sides", [
                ("Scrotum", "Size, shape, symmetry, development (wrinkling)"),
                ("Skin", "Redness, ulcers, rashes, scars, sinuses or fistula"),
                ("Swelling, visible mass, dilated veins", "Varicocele"),
                ("Dorsum of the scrotum", "Ask about pain, elevate the scrotum, look for a sinus"),
                ("Cough impulse", "Turn the face and cough: swelling increases → hernia (on the checklist)"),
            ]),
            ("Palpation", "ask about pain, watch the face", [
                ("Temperature &amp; tenderness", ""),
                ("Each side separately", "Testis: size, shape, consistency, tenderness; spermatic cord; masses", "uro_testis_palp"),
                ("Get above the swelling", "Thumb &amp; index at the deep inguinal ring: can get above → scrotal; cannot → inguinal", "uro_get_above"),
                ("Fluctuation test", "Two hands, push and receive: waves = fluid"),
                ("Transillumination test", "Dark room, torch, rolled X-ray paper: light = serous fluid (hydrocele); dark = blood / solid", "uro_transillum"),
                ("Empty scrotum", "Look for undescended testis in the inguinal canal / lower abdomen (on the checklist)"),
            ]),
            ("Completion", "", [("Thank, cover, wash hands", "")]),
        ], ["Symmetry", "Both testes present", "Cough impulse (on the checklist)", "Fluid vs solid", "Get above the swelling",
            "Empty scrotum → inguinal canal (on the checklist)", "Each side separately"]),
        ("Renal angle &amp; kidney examination", [
            INTRO("Xiphisternum to iliac crest", "Supine", extra=[("Ensure privacy", "")]),
            ("Inspection", "", [
                ("Flanks from the front", "Scars, discoloration, swelling"),
                ("From behind (patient sits forward)", "Renal angles symmetrical, no swelling"),
            ]),
            ("Palpation", "ask about pain first", [
                ("Renal angle", "Between the 12th rib and the vertebral column, both sides; watch the face"),
            ]),
            ("Percussion", "", [
                ("CVA tenderness test", "Hand over the angle, strike gently with the other fist; both sides", "uro_renal_angle"),
            ]),
            ("Kidneys", "", [
                ("Ballottement", "Supine; one hand in the loin pushes, the other feels: ballotable = enlarged kidney", "git2_kidney"),
                ("Renal artery auscultation", "~1 cm above and lateral to the umbilicus, both sides: bruit = stenosis"),
            ]),
            ("Completion", "", [("Thank, cover, wash hands", "")]),
        ], ["CVA tenderness (pyelonephritis)", "Ballotable kidney", "Renal artery bruit", "Compare both sides"]),
    ],
    tables=[],
    quiz=[],
    tips=["There may be a scrotal model with a mass in the exam."],
    histories=["58", "60", "62", "136"],
),
# =====================================================================================
dict(
    id="lump", num=6, title="Lump &amp; Ulcer",
    subtitle="Lump examination · ulcer examination",
    ar="الكتلة: الموقع، الحجم، الشكل، السطح، الحافة، القوام، التموّج، نفاذ الضوء، الحركة والالتصاق، الانضغاط والارتداد، النبض، ثم العقد اللمفاوية. "
       "القرحة: افحص الأوعية الدموية أولاً ثم صِف القرحة: الموقع، الشكل، الحافة، القاع، القاعدة، الجلد المحيط.",
    checklists=[
        ("Lump examination", [
            INTRO("Expose the lump adequately", "Comfortable; ask about pain before examining"),
            ("Inspection", "from the end of the bed and close", [
                ("Site, size, shape, surface", ""),
                ("Skin", "Redness, ulceration, scars, dilated veins, punctum"),
                ("Number &amp; visible pulsation", ""),
            ]),
            ("Palpation", "", [
                ("Temperature &amp; tenderness", "Compare with the surrounding skin"),
                ("Size", "cm, length × width", "lump_measure"),
                ("Shape, surface, edge", "Regular / irregular; smooth / nodular; well / ill defined"),
                ("Consistency", "Soft / firm / hard / cystic"),
                ("Fluctuation", "Cystic swellings", "lump_fluctuation"),
                ("Transillumination", "If cystic", "lump_transillum"),
                ("Mobility &amp; skin attachment", "Pinch the skin over it: fixed → skin involvement", "lump_fixity"),
                ("Deep attachment", "Contract the muscle beneath: reduced mobility → attached"),
                ("Compressibility &amp; reducibility", "Reduces with pressure? Disappears and returns?"),
                ("Pulsation", "Expansile vs transmitted"),
                ("Cough impulse", "If relevant (hernia)"),
                ("Regional lymph nodes", "Breast / upper limb → axillary; lower limb → inguinal; head &amp; neck → cervical"),
                ("Neurovascular", "If indicated: pulses, sensation, motor"),
            ]),
            ("Closure", "", [
                ("Say", "“I would like to complete by examining regional nodes, neurovascular assessment if relevant, and reviewing imaging or biopsy.”"),
                ("Comment example", "“A lump at … measuring … cm, tender / non-tender, soft / firm / hard, mobile / fixed, no overlying skin changes.”"),
            ]),
        ], ["Full description (6–8 features)", "Skin changes (punctum, ulcer, veins)", "Fluctuation + transillumination",
            "Mobility over skin and deep structures", "Expansile vs transmitted", "Regional lymph nodes"]),
        ("Ulcer examination", [
            INTRO("Expose the ulcer adequately", "Comfortable; ask about pain before touching"),
            ("General inspection", "", [("Around the patient", "Walking aid, wheelchair, dressings, compression stockings, footwear")]),
            ("Local inspection", "", [
                ("Site, number, size, shape", ""),
                ("Edge", "Sloping (venous), punched out (arterial), undermined, rolled / everted (malignancy)"),
                ("Floor", "Granulation tissue, slough, necrosis"),
                ("Base", "Depth; underlying structures visible"),
                ("Surrounding skin", "Pigmentation, eczema, cellulitis, varicose veins, hair loss, callus, scars"),
            ]),
            ("Palpation", "", [
                ("Temperature &amp; tenderness", "Compare with the opposite limb"),
                ("Size", "Length × width × depth"),
                ("Edge, floor &amp; base", "Gloved finger; underlying soft tissue, tendon, bone"),
                ("Induration &amp; fixity", "Around the margins; attachment to deep tissues"),
                ("Regional lymph nodes", ""),
                ("Peripheral vascular exam", "Femoral, popliteal, PT, DP pulses; CRT; Buerger’s test if indicated", "pvd_dp_pulse"),
                ("Chronic ischaemia signs", "Hair loss, shiny skin, muscle wasting"),
                ("Neurological exam", "Light touch, pinprick, vibration, proprioception (diabetic ulcers)"),
            ]),
            ("Closure", "", [
                ("Say", "“I would like to complete with a full vascular and neurological assessment, blood glucose / HbA1c, wound swab, Doppler and imaging.”"),
            ]),
        ], ["Edge is key for diagnosis", "Compare both limbs", "Peripheral pulses", "Neuropathy in diabetic ulcers",
            "Site → shape → edge → floor → base → skin"]),
    ],
    tables=[],
    quiz=[("Definition of ulcer?", ""), ("Mention 4 signs of lump examination.", ""), ("Mention 4 special examinations for a lump.", ""),
          ("Mention 2 signs of a healing ulcer.", ""), ("Types of ulcer edge with examples?", ""),
          ("Compare compressibility and reducibility.", ""),
          ("Painful ulcer on the big toe, cold toe, absent pulses — diagnosis?", "Arterial ulcer")],
    tips=["In an ulcer station you do the peripheral vascular examination first, then describe the ulcer."],
    histories=[],
),
# =====================================================================================
dict(
    id="breast", num=7, title="Breast",
    subtitle="Breast examination · breast histories",
    ar="فحص الثدي بوجود مرافِقة: النظر وهي جالسة (ثم اليدين خلف الرأس، ثم على الخصر مع الميل للأمام)، ثم الجسّ وهي مستلقية بدءاً بالثدي السليم مع الذيل الإبطي، "
       "ثم اختبارا الالتصاق بالجلد وبالعضلة الصدرية، ولا تنسَ ذكر العقد الإبطية والفحص التنفسي والهضمي.",
    checklists=[
        ("Breast examination", [
            INTRO("Umbilicus up, upper limbs fully exposed", "Sitting", extra=[("Privacy + chaperone", "")]),
            ("Inspection", "from the front", [
                ("Symmetry", "Both breasts"),
                ("Skin", "Dimpling, peau d’orange, scars, ulcers, dilated veins, colour changes"),
                ("Nipples", "Retraction, protrusion, discharge — ask her to squeeze; describe colour, amount, smell"),
                ("Areola", "Colour changes"),
                ("Hands behind the head", "Retromammary space, axillary swelling / mass", "breast_positions"),
                ("Hands on hips + leaning forward", "Skin dimpling"),
            ]),
            ("Palpation", "warm hands; supine, hand behind the head; <b>normal breast first</b>", [
                ("Systematic palpation", "Finger pads, circular, from outer to inner, include the axillary tail", "breast_palpation"),
                ("Describe any lump", "Site, size, shape, surface, consistency, tenderness, mobility, fixation to skin and muscle"),
            ]),
            ("Special tests", "", [
                ("Skin tethering test", "Move the skin over the lump: fixed → skin involvement"),
                ("Pectoralis major fixation test", "Press hands on hips, re-check: less movement → attached to pectoralis"),
            ]),
            ("Must mention", "", [
                ("Say", "“I would like to examine the axillary lymph nodes.”", "breast_axilla"),
                ("Say", "“I would like to perform respiratory and abdominal (GIT) examination.”"),
            ]),
            ("Completion", "", [("Thank, help her dress, wash hands", "")]),
        ], ["Symmetry", "Skin changes (peau d’orange, dimpling)", "Nipple changes / discharge", "Axillary tail",
            "Systematic palpation", "Lump description (6S)", "Skin tethering &amp; pectoralis fixation", "Mention axillary nodes + systemic exam"]),
    ],
    tables=[],
    quiz=[("Definition of mastalgia?", "Pain or discomfort in one or both breasts"),
          ("Four DDx of a painless breast lump?", "Fibroadenoma, carcinoma, cyst, phyllodes tumour"),
          ("Four DDx of a painful breast lump?", "Abscess, mastitis, cyst, fibrocystic disease"),
          ("Groups of axillary lymph nodes?", "Anterior (pectoral), posterior (subscapular), lateral (humeral), central, apical"),
          ("Quadrants of the breast?", "Upper outer, upper inner, lower outer, lower inner, axillary tail, nipple &amp; areola"),
          ("Two DDx of nipple discharge?", ""), ("Red flags of breast cancer?", ""),
          ("45-year-old, unilateral bloody nipple discharge — two DDx?", ""),
          ("60-year-old, unilateral eczematous nipple — two DDx?", "")],
    tips=["Two breast models: a whole one with skin, nipple and areola abnormalities, and a separated one with 3 obvious masses "
          "(one under the nipple). Comment on every one of them — missing one loses marks."],
    histories=["23", "75", "230", "87"],
),
# =====================================================================================
dict(
    id="dfoot", num=8, title="Diabetic Foot &amp; Wound Dressing",
    subtitle="Diabetic foot examination · wound dressing",
    ar="القدم السكرية: النظر (مع رفع الرجل لرؤية الكعب وبطن القدم)، الجسّ، النبض، والفحص العصبي (اللمس، الألم، وضع المفصل، الاهتزاز، المونوفيلامنت). "
       "الغيار: بتقنية معقّمة، افحص الغيار القديم، ثم تقييم الجرح، الغسل من المركز للخارج بشاش جديد كل مرة، ثم البيتادين، ثم اكتب التاريخ والوقت.",
    checklists=[
        ("Diabetic foot examination", [
            INTRO("Above the knee to the toes", "Supine", extra=[("Ensure privacy", "")]),
            ("Inspection", "", [
                ("Symmetry &amp; amputation", "Toes / foot"),
                ("Skin", "Hair loss, shiny skin, scars, wounds, colour, dry skin / cracks"),
                ("Nails, callus, gangrene", "Nail deformity / fungal infection"),
                ("Swelling, deformity", ""),
                ("Between the toes", "Fungal infection / maceration"),
                ("Heels and soles", "Raise each leg — hidden ulcers"),
                ("Describe any ulcer", "Site, size, shape, edge, base, surrounding skin, discharge"),
            ]),
            ("Palpation", "ask about pain first", [
                ("Temperature", "Dorsum of the hand, compare"),
                ("Tenderness", ""),
                ("If ulcer", "Wash hands, gloves; palpate ulcer, underlying structures, pain, base hard / soft"),
            ]),
            ("Peripheral vascular examination", "", [
                ("Dorsalis pedis &amp; posterior tibial", "Compare both sides", "pvd_dp_pulse"),
                ("Popliteal &amp; femoral", "If required"),
                ("Capillary refill time", ""),
            ]),
            ("Neurological examination", "", [
                ("Fine touch", "Cotton on the sternum first, eyes closed, compare medial &amp; lateral"),
                ("Pain sensation", "Same, with a pin"),
                ("Joint position sense", "Hold big toe at the sides, move up / down"),
                ("Vibration — 128 Hz fork", "Sternum first, then base of big toe → medial malleolus → tibial tuberosity", "df_tuning_fork"),
                ("Monofilament test", "If available — otherwise say you would do it", "df_monofilament"),
            ]),
            ("Completion", "", [
                ("To complete", "Rest of neurological system, ABI, blood glucose, HbA1c, footwear, regional lymph nodes"),
                ("Thank, help to comfortable position, wash hands", ""),
            ]),
        ], ["Compare both feet", "Between toes, heels &amp; soles for hidden ulcers", "Risk features: callus, deformity, dry skin, gangrene",
            "CRT + DP / PT pulses", "Fine touch, pain, vibration, proprioception", "Monofilament if available",
            "Describe ulcers systematically", "Examine footwear", "Mention ABI, HbA1c, glucose"]),
        ("Wound dressing", [
            ("Introduction", "", [
                ("Check indication &amp; timing", "Correct patient and correct time to change"),
                ("Wash hands", "Scrubbing technique"),
                ("Introduce yourself, confirm name &amp; age", ""),
                ("Explain, consent, privacy", ""),
            ]),
            ("Aseptic technique", "", [
                ("Say it", "“This will be done using sterile aseptic technique.”"),
                ("Prepare sterile field", "Sterile gauze, sterile forceps, sterile gloves, normal saline, Betadine, plaster"),
                ("Check glove size", "Before opening"),
            ]),
            ("Old dressing", "", [
                ("Remove carefully", "Check the date / time of the last dressing"),
                ("Inspect it before disposal", "Blood, pus, exudate"),
            ]),
            ("Wound assessment", "", [
                ("Assess", "Site, size (length, width, depth), discharge, odour, surrounding skin, visible structures (fat, muscle, bone)"),
            ]),
            ("Cleaning", "", [
                ("Wound wash", "Normal saline; gauze held with forceps like a pen; centre → periphery; new gauze each time; 2–3 times", "df_cleaning"),
                ("Surrounding skin", "Saline, each side with a separate gauze"),
                ("Betadine", "Same way: wound, then surrounding skin; change gauze every time"),
            ]),
            ("Dressing", "", [
                ("Apply", "Prescribed ointment if ordered; sterile gauze dressing; secure with plaster", "df_dressing"),
                ("Label", "Date and time"),
            ]),
            ("Final steps", "", [("Dispose of waste, remove gloves, wash hands, thank patient", "")]),
        ], ["Strict aseptic technique", "Check timing of dressing change", "Full wound assessment", "Centre → periphery",
            "New gauze each wipe", "Inspect old dressing before disposal", "Correct re-dressing and labelling"]),
    ],
    tables=[],
    quiz=[],
    tips=["A combined station may ask how to wash hands (scrubbing) and wear gloves together.",
          "Know how to remove gloves correctly — removing them the wrong way loses marks."],
    histories=["231"],
),
# =====================================================================================
dict(
    id="skills", num=9, title="Surgical Skills",
    subtitle="Needle &amp; suture identification · sterile gloves · knot · simple suture",
    ar="محطة التعرف على الخيط والإبرة: عرّف بنفسك ثم اقرأ كل ما هو مكتوب على العبوة (النوع، الامتصاص، القياس، الطول، اللون، شكل الإبرة وطولها ونوع القطع، "
       "التعقيم، التصنيع والانتهاء) وأضف الاستخدامات. في لجان الخياطة خذ الإذن واذكر التخدير الموضعي، وفي لبس القفاز اذكر غسل اليدين بطريقة الـ scrubbing.",
    checklists=[
        ("Surgical needle &amp; suture identification", [
            ("Station", "you are given a label and asked to read it", [
                ("Introduce yourself", "It is on the checklist and has a mark"),
                ("Read every word", "Including manufacture and expiry dates and disposal"),
            ]),
            ("Suture", "", [
                ("Material &amp; type", "e.g. polypropylene monofilament; polyglactin 910 braided &amp; coated"),
                ("Absorbable or not", "Non-absorbable stays — skin sutures need removal; absorbable is broken down"),
                ("Colour &amp; length", "e.g. blue, 75 cm"),
                ("Size", "USP (e.g. 3-0) and metric / EP (e.g. 2)"),
            ]),
            ("Needle", "", [
                ("Length", "e.g. 24 mm, 60 mm"),
                ("Shape", "1/2 circle, straight"),
                ("Type of cutting", "Cutting, reverse cutting (cutting edge on the outer curve)"),
            ]),
            ("Packet details", "", [
                ("Sterile (EO), LOT, product code, quantity, manufacturer", ""),
                ("Mfg &amp; Exp dates", "If expired → must not be used clinically"),
            ]),
            ("Uses", "add them yourself", [
                ("Polypropylene", "Skin closure, soft tissue approximation, cardiovascular surgery"),
                ("Polyglactin 910", "Soft tissue approximation / closure, general surgery"),
            ]),
        ], ["Introduce yourself", "Read everything written", "State the uses"], "channel"),
        ("Sterile gloves, knot &amp; simple suture — what the channel says", [
            ("Sterile gloves", "", [("Say", "“I will wash my hands by scrubbing with sterile soap.” — important, has marks")]),
            ("Suturing stations", "", [
                ("Conscious patient", "Take permission, tell him you will suture, and say you will inject local anaesthetic"),
                ("Unconscious / theatre", "Suture without taking permission"),
                ("One exam", "One stitch with the needle without tying — then explain how you would tie it", "sk_suture"),
            ]),
        ], ["Introduce yourself in every station", "Scrubbing with sterile soap", "Mention local anaesthetic"], "channel"),
    ],
    tables=[],
    quiz=[],
    tips=["The label in the exam may differ from yours — the department’s packets are real ones."],
    histories=[],
),
]

# histories of each topic come verbatim from these channel posts (Arabic scripts)
HISTORY_TITLES = {
    "7": "History of neck swelling", "23": "History of breast lump", "30": "History of abdominal pain",
    "33": "History of dysphagia", "36": "History of constipation", "39": "History of diarrhoea",
    "58": "History of red urine (haematuria)", "60": "History of weak stream (LUTS)", "62": "History of flank pain",
    "69": "History of intermittent claudication", "75": "History of nipple discharge", "87": "History of gynaecomastia",
    "136": "History of dysuria", "137": "History of heartburn", "138": "History of epigastric pain",
    "139": "History of vomiting", "140": "History of haematemesis", "230": "History of mastalgia",
    "231": "History of diabetic foot", "232": "History of rectal bleeding", "233": "History of jaundice",
}
