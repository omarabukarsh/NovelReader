# -*- coding: utf-8 -*-
"""Checklists taken ONLY from the student's handwritten lecture notes (what the doctors said).

NOTES[topic_id]   = list of checklists (title, phases) built from the notes
KEEP_STD[topic_id] = indexes of the earlier standard checklists to keep (clearly labelled), because
                     the notes do not cover them.
"""

NOTES = {
# ------------------------------------------------------------------ 2. Thyroid & cervical lymph nodes
"thy": [
    ("Local examination of the thyroid", [
        ("Inspection", "", [
            ("Skin changes", ""),
            ("Scar", ""),
            ("Dilated veins", ""),
            ("Masses", ""),
            ("Swallowing test", "If you suspect a mass, ask the patient to drink water — mass moves upward ↑ = high suspicion of thyroid gland", "thy_swallow"),
            ("Tongue protrusion", "Ask to stick out the tongue: midline mass moves up = thyroglossal cyst; does not move = thyroid mass", "thy_tongue"),
        ]),
        ("Palpation", "", [
            ("Stand behind the patient", "From the right side"),
            ("Neck position", "“Flex your neck slightly forward and relax”"),
            ("Thyroid cartilage → isthmus", "Palpate the thyroid cartilage, go down below the cricoid cartilage and palpate the isthmus"),
            ("Both thyroid lobes", "Assess both lobes", "thy_palpation"),
            ("Repeat tongue &amp; swallowing tests", "Confirm by <b>feeling</b>, not by eye only"),
            ("Trachea", "Central or deviated? Deviation happens with a large goitre", "thy_trachea"),
        ]),
        ("Percussion", "", [
            ("Percuss the sternum", "Dullness = retrosternal thyroid extension"),
        ]),
        ("Auscultation", "last step", [
            ("Both thyroid lobes", "Bruit = increased vascularity → Graves’ disease"),
        ]),
    ]),
    ("Cervical lymph node examination", [
        ("Opening", "we examine them to look for malignancy or infection", [
            ("Introduce yourself", "Explain; take verbal consent"),
            ("Position", "Patient comfortable, sitting"),
            ("Neck", "Slightly flexed → muscles relaxed"),
            ("Privacy", ""),
            ("Exposure", "Down to the nipples — to reach the supraclavicular nodes"),
            ("Stand behind the patient", ""),
        ]),
        ("Inspection", "", [
            ("Mass or lump", ""),
            ("Scar", ""),
            ("Colour changes", ""),
        ]),
        ("Palpation", "tips of index &amp; middle fingers, circular movements; groups: upper horizontal + longitudinal", [
            ("Submental", "Below the chin"),
            ("Submandibular", ""),
            ("Tonsillar", ""),
            ("Pre-auricular", "In front of the ear"),
            ("Post-auricular", "Behind the ear"),
            ("Occipital", "At the back (end) of the skull"),
            ("Sternocleidomastoid ★ landmark", "Ask the patient to turn the head to the opposite side so SCM shows: anterior cervical nodes in front, posterior behind", "thy_nodes"),
            ("Supraclavicular (Virchow’s)", "Ask the patient to raise (shrug) the shoulders; drains chest &amp; GIT"),
        ]),
        ("If you find a swelling", "", [
            ("Describe it", "Site, size, shape, tenderness"),
            ("Hotness", "Compare with the area around it"),
            ("Attachment", "To the underlying structure; skin pinch"),
            ("Scattered or matted", "Scattered = small separate nodes; matted = stuck together in one place"),
        ]),
    ]),
],
# ------------------------------------------------------------------ 3. GIT general
"git1": [
    ("General examination related to GIT", [
        ("Opening", "", [
            ("Introduce yourself", "Take verbal consent"),
            ("Privacy", ""),
            ("Exposure", "Whole body"),
            ("Position", "Supine"),
            ("Wash hands", ""),
        ]),
        ("General inspection", "look at the patient", [
            ("Pain or distress", ""),
            ("Fever, dehydration", ""),
            ("Hair loss", ""),
            ("Muscle bulk", ""),
            ("Weight loss or gain", ""),
            ("Pallor", ""),
            ("Jaundice", ""),
        ]),
        ("Face &amp; mouth", "", [
            ("Face", "Xanthelasma, jaundice, pallor", "git1_eyes"),
            ("Chronic anaemia", "Atrophic glossitis or angular stomatitis"),
            ("Mouth", "Glossitis, oral ulcer, parotid enlargement"),
            ("Virchow’s lymph node", "Enlargement", "git1_virchow"),
        ]),
        ("Hands", "", [
            ("Clubbing", "", "git1_hands"),
            ("Xanthomas", ""),
            ("Koilonychia", "Spoon nails"),
            ("Flapping tremor (asterixis)", "", "git1_asterixis"),
            ("Palmar erythema", ""),
            ("Dupuytren’s contracture", ""),
        ]),
        ("Chest, abdomen &amp; lower limb", "", [
            ("Chest", "Spider naevi, gynaecomastia"),
            ("Abdomen", "Dilated veins, ascites"),
            ("Lower limb", "Pigmented ulcer, oedema, purpura, erythema nodosum, scratch marks, pyoderma gangrenosum"),
        ]),
    ]),
],
# ------------------------------------------------------------------ 4. GIT local + PR
"git2": [
    ("Local abdomen examination", [
        ("Opening", "", [
            ("Introduce yourself", ""),
            ("Take permission", ""),
            ("Wash hands", ""),
            ("Privacy", ""),
            ("Exposure", "Female: from the inframammary line · Male: from the 2nd rib — down to the iliac crest"),
            ("Position", "Supine"),
        ]),
        ("Inspection", "", [
            ("From the end of the bed", "Movement with respiration"),
            ("Symmetry &amp; distension", "Abdomen symmetrical? Abdominal distension?"),
            ("Umbilicus", "Inverted or everted"),
            ("Skin", "Scar, skin discolouration, stoma, scratch marks"),
            ("Dilated veins &amp; peristalsis", "Superficial dilated veins, visible peristalsis"),
            ("Cough impulse", "Positive?"),
        ]),
        ("Palpation", "", [
            ("Ask about pain", "“Do you have pain?”"),
            ("Superficial palpation", "Start from the right iliac fossa, at the same level as the abdomen; look at the face → superficial mass or tenderness", "git2_light_palp"),
            ("Deep palpation", "Mass, deep tenderness"),
            ("Liver", "Start in the right iliac fossa, ask the patient to breathe; once you feel a mass → percussion", "git2_liver"),
            ("Spleen", "From the right iliac fossa up to the left hypochondrium; ask the patient to roll, hold the costal margin, repeat", "git2_spleen"),
        ]),
        ("Percussion", "", [
            ("Upper border of the liver", "From the angle of Louis → 2nd rib in front, percuss down until the note becomes dull"),
            ("Lower border of the liver", "Percuss up from below until dull; measure with a tape — normal span 8–12 cm"),
            ("Spleen", "Percuss — dull mass?"),
            ("Ascites — shifting dullness", "Percuss from the epigastrium to dullness, then down to the flank: resonant = normal. Roll the patient towards you: becomes resonant = shifting dullness", "git2_shifting"),
            ("Fluid thrill", "Patient presses the midline with his hand (blocks the fat); tap one side, feel on the other — wave reaches = fluid"),
        ]),
        ("Auscultation", "last step", [
            ("Peristalsis", "Listen in the right iliac fossa"),
            ("Abdominal bruit", ""),
            ("Renal bruit", ""),
            ("Splenic rub", ""),
            ("Venous hum", ""),
            ("Succussion splash", ""),
        ]),
    ]),
    ("Per-rectal examination", [
        ("Opening", "", [
            ("Privacy", "Closed room"),
            ("Exposure", ""),
            ("Position", "Left lateral, knees fully flexed and pressed to the chest", "git2_pr_position"),
        ]),
        ("Inspection", "", [
            ("Around the anus", "Skin abnormality, scars, ulcer, tags, bleeding"),
            ("Anus", "Anal condition, haemorrhoids, fissure, soiling, bleeding"),
        ]),
        ("Palpation", "", [
            ("Gloves &amp; lubricant", "Lubricate the index finger"),
            ("Ask about pain", "“Do you have pain in this area?”"),
            ("Insert the finger fully", "Look at the face for tenderness"),
            ("Muscle tone", "Ask the patient to squeeze your finger"),
            ("Sweep anticlockwise &amp; clockwise", "Mass, impacted faeces, ulcer"),
            ("Examine the glove", "Blood, mucus, stool colour"),
        ]),
        ("End", "", [("Thank the patient", "")]),
    ]),
],
# ------------------------------------------------------------------ 5. Scrotal
"uro": [
    ("Urology &amp; scrotal examination", [
        ("Opening", "", [
            ("Introduce yourself", ""),
            ("Take permission", ""),
            ("Wash hands", ""),
            ("Privacy", "Closed room"),
            ("Exposure", "Full genitalia down to mid-thigh"),
            ("Position", "Standing"),
        ]),
        ("Inspection — penis", "", [
            ("Lesion", "Mass, ulcer"),
            ("Urethral orifice site", "Central, anterior (ventral), dorsal"),
            ("Phimosis", "Inability to retract the foreskin"),
            ("Paraphimosis", "Tight foreskin → emergency"),
        ]),
        ("Inspection — scrotum", "", [
            ("Development of the scrotum", "Wrinkles, darkness"),
            ("Skin lesions", "Anteriorly and at the back"),
            ("Erythema / cellulitis", "Redness, ulcer, scars"),
            ("Testicular / scrotal swelling", "Right, left or both"),
            ("Back surface", "Ulcer or sinus → extra-pulmonary manifestation of TB"),
            ("Cough impulse", "Pure scrotal swelling or not"),
        ]),
        ("Palpation", "", [
            ("Ask about pain", ""),
            ("Tenderness / hotness", "Compare right and left, watch the face"),
            ("Both testes in the scrotum?", "Index &amp; thumb; hold the spermatic cord", "uro_testis_palp"),
            ("Root of the spermatic cord", "“Can I get above this?” — yes = problem in the scrotum; no = from the inguinal area", "uro_get_above"),
            ("Penile shaft", "If you suspect a deformity / erection problem: feel for nodules"),
        ]),
        ("Special tests", "", [
            ("Fluctuation (push &amp; receive)", "Mass or fluid? Positive (you feel waves) = fluid; negative = mass"),
            ("Transillumination", "Dark room, X-ray paper &amp; torch: lights up = pure fluid; no light = blood", "uro_transillum"),
        ]),
    ]),
],
# ------------------------------------------------------------------ 6. Ulcer & lump
"lump": [
    ("Ulcer examination", [
        ("Opening", "", [
            ("Introduce yourself", ""),
            ("Explain the procedure", ""),
            ("Take permission", ""),
            ("Privacy", ""),
            ("Wash hands &amp; wear sterile gloves", ""),
        ]),
        ("Inspection — general", "", [
            ("Lower limbs", "Symmetrical or not"),
            ("Ulcer", "Single or multiple"),
            ("Dressing", "In order or not; bad smell"),
        ]),
        ("Inspection — local", "", [
            ("Site", "Venous → medial lower leg; arterial → lateral lower leg; malignant → anywhere"),
            ("Size", "Measure with a tape"),
            ("Shape", ""),
            ("Edge", ""),
            ("Base / floor", "Tissue, exudate, slough"),
            ("Discharge", ""),
            ("Surrounding skin", "Redness"),
            ("Depth", ""),
        ]),
        ("Palpation", "", [
            ("Temperature", "Dorsum of your hand, both sides"),
            ("Induration", ""),
            ("Edge &amp; base", "Put your finger on the ulcer"),
            ("Distal structures", "Dorsalis pedis &amp; posterior tibial arteries — especially if diabetic foot", "pvd_dp_pulse"),
            ("Peripheral pulses &amp; inguinal lymph nodes", ""),
            ("Neurological exam", ""),
        ]),
    ]),
    ("Lump examination", [
        ("Inspection", "", [
            ("Site", ""),
            ("Number", ""),
            ("Size", "", "lump_measure"),
            ("Shape", ""),
            ("Surface &amp; skin over the lump", ""),
            ("Edge", ""),
        ]),
        ("Palpation", "", [
            ("Temperature", ""),
            ("Tenderness", ""),
            ("Consistency", "Firm, hard, cystic"),
            ("Attachment", "To the skin or the underlying structure", "lump_fixity"),
            ("Check the lymph nodes", ""),
        ]),
        ("Special tests", "", [
            ("Fluctuation", "Fluid (cyst, abscess) or solid?", "lump_fluctuation"),
            ("Fluid thrill", ""),
            ("Transillumination", "Clear fluid (cyst) — same as in the scrotum", "lump_transillum"),
            ("Resonance (percussion)", "Resonant = gas-filled; dull = hard"),
            ("Reducibility", "Hernia"),
            ("Cough impulse", ""),
            ("Pulsatile or transmitted", "Pulsatile (aneurysm) = the mass itself expands in all directions; transmitted = mass lying on a big artery"),
        ]),
        ("Auscultation", "", [
            ("Bruit", "High vascularity"),
        ]),
    ]),
],
# ------------------------------------------------------------------ 7. Breast
"breast": [
    ("Breast examination", [
        ("Opening", "", [
            ("Introduce yourself", ""),
            ("Take permission", ""),
            ("Position", "45°, hands raised above the head"),
            ("Privacy", ""),
            ("Exposure", "Up to the umbilicus"),
        ]),
        ("Inspection", "", [
            ("Symmetry of both breasts", "Same nipple level, same size"),
            ("Nipple", "Cracks or fissure, retraction"),
            ("Abnormal discharge", "Blood, pus, black, white — if not clear, ask the patient to squeeze the nipple"),
            ("Skin changes", "Redness, ulcer, puckered scar, infection, dimpling, mass, peau d’orange"),
            ("Hands raised above the head", "Then describe the mass: site (quadrant), size, shape, skin surface, ulcer, colour change", "breast_positions"),
            ("Area under the breast", ""),
            ("Hands pressed in the middle (on the hips)", "Contracts pectoralis major → look at the mass"),
            ("Axillae, arm &amp; supraclavicular fossa", ""),
        ]),
        ("Palpation", "", [
            ("Hotness &amp; tenderness", ""),
            ("All quadrants, both sides", "Three fingers moving in circles", "breast_palpation"),
        ]),
        ("Lymph nodes", "the most important part — finish with it", [
            ("Support the patient’s arm", "Your hand under the elbow"),
            ("Axillary nodes in order", "Anterior axillary fold → posterior axillary fold (circular motion) → central → apical → lateral", "breast_axilla"),
            ("Supraclavicular nodes", "Ask the patient to raise the hands so the fossa shows, then palpate"),
            ("Describe any lump", ""),
        ]),
    ]),
],
# ------------------------------------------------------------------ 8. Diabetic foot & dressing
"dfoot": [
    ("Diabetic foot examination", [
        ("Opening", "", [
            ("Introduce yourself", ""),
            ("Wash hands, take permission", ""),
            ("Exposure", "From the feet to mid-thigh"),
            ("Position", "Supine"),
        ]),
        ("Inspection", "", [
            ("Both feet", "Symmetrical or not; hair loss, shiny skin"),
            ("Amputation", ""),
            ("Swelling", ""),
            ("Fungal infection", "Between the toes"),
            ("Pressure areas", "Ask the patient to elevate the foot to inspect them"),
            ("Hidden ulcer", "Calf muscle, heel"),
            ("Any ulcer", "Describe it"),
        ]),
        ("Palpation", "", [
            ("Ask about pain", "“Do you have pain?”"),
            ("Tenderness &amp; hotness", ""),
            ("Wash hands &amp; wear gloves", ""),
            ("Base of the ulcer", "Finger on the base: hard or soft?"),
        ]),
        ("“I would like to examine the peripheral pulses”", "", [
            ("Anterior &amp; posterior tibial arteries", "", "pvd_pt_pulse"),
            ("Dorsalis pedis", "Lateral to extensor hallucis longus", "pvd_dp_pulse"),
            ("Popliteal artery", ""),
            ("Femoral artery", ""),
        ]),
        ("“I would like to examine the CNS of the lower limb”", "", [
            ("Vibration", "", "df_tuning_fork"),
            ("Fine touch", ""),
            ("Joint movement", ""),
            ("Monofilament test", "Sensory test of the sole: a wire is touched on the pressure areas — does the patient feel it?", "df_monofilament"),
        ]),
    ]),
    ("Wound dressing", [
        ("Opening", "", [
            ("Confirm patient name &amp; dressing time", "Daily / day after day"),
            ("Introduce yourself", ""),
            ("Explain the procedure", ""),
            ("Take permission", ""),
            ("Wash hands", "Palm, dorsum, thumb, each finger, between fingers, nails, under the nails, wrist"),
        ]),
        ("Sterile aseptic technique — equipment", "", [
            ("Prepare", "Sterile sheet, sterile gauze, normal saline, plaster, antiseptic (Betadine), sterile gloves"),
        ]),
        ("Old dressing", "", [
            ("Remove the plaster", "Expose the wound; note the date &amp; time and the type of exudate"),
        ]),
        ("Assessment", "", [
            ("Wound", "Site, depth, height, exudate type, underlying structure"),
            ("Pulse", ""),
            ("Nerve examination", ""),
        ]),
        ("Cleaning &amp; dressing", "", [
            ("Clean with sterile gauze", "From the centre outwards, distal → proximal; a new gauze each time; then the skin around", "df_cleaning"),
            ("Betadine", "One direction, wound and area around it"),
            ("Put the plaster", "Write the date &amp; time", "df_dressing"),
        ]),
    ]),
],
}

# earlier standard checklists to keep (indexes in the old topic) because the notes do not cover them
KEEP_STD = {
    "pvd": [0, 1, 2],
    "thy": [0],      # history of a neck swelling
    "git1": [0],     # GI history
    "git2": [],
    "uro": [0, 2],   # urological history, renal angle
    "lump": [],
    "breast": [0],   # breast history
    "dfoot": [],
    "skills": [0, 1, 2, 3],
}
