# -*- coding: utf-8 -*-
"""Topics 4-6."""
from content_1 import wiper, closing

TOPICS_B = [
# =====================================================================================
dict(
    id="git2", num=4, title="GIT (II): Abdominal Examination &amp; PR",
    subtitle="Abdominal examination including organomegaly &amp; ascites · per-rectal examination",
    ar="فحص البطن بالترتيب: نظر ← جسّ سطحي ثم عميق للمناطق التسع (ابدأ بعيداً عن الألم وراقب وجه المريض) ← الكبد والطحال والكليتين ← "
       "القرع وفحص الاستسقاء (الأصمّية المتنقلة وموجة السائل) ← التسمّع. "
       "الفحص الشرجي يتم بوجود مرافق وبعد الموافقة، والمريض مستلقٍ على جانبه الأيسر.",
    lookfor=[
        ("Inspection", ["Contour – distension (5 Fs: fat, fluid, flatus, faeces, fetus)", "Scars", "Stomas",
                        "Visible peristalsis", "Visible pulsation (AAA)", "Distended veins / caput medusae",
                        "Striae, bruising (Cullen’s / Grey Turner’s)", "Umbilicus (everted / hernia)",
                        "Hernial orifices – ask to cough", "Movement with respiration"]),
        ("Palpation", ["Tenderness (watch the face)", "Guarding / rigidity", "Rebound tenderness", "Masses",
                       "Liver", "Spleen", "Kidneys (ballot)", "Abdominal aorta", "Hernial orifices"]),
        ("Percussion", ["Liver span (upper + lower border)", "Spleen (Traube’s space)", "Bladder", "Shifting dullness",
                        "Fluid thrill (tense ascites)"]),
        ("Auscultation", ["Bowel sounds (absent / tinkling)", "Aortic &amp; renal bruits", "Succussion splash (gastric outlet obstruction)"]),
        ("Per-rectal exam", ["Perianal skin: tags, haemorrhoids, fissure, fistula, warts", "Anal tone (squeeze)",
                             "Rectal wall 360° – masses", "Prostate (men) / cervix (women)", "Glove: blood, mucus, melaena, stool colour"]),
    ],
    procedures=[
        ("A. Abdominal examination", [
            wiper("from the nipples to the groin (cover the genitalia)", "lying <b>flat</b>, one pillow, arms by the sides"),
            (None, "<b>General inspection</b> + quick hands / face / neck (see GIT I)."),
            (None, "<b>Inspect the abdomen</b> from the foot of the bed and from the side at the level of the abdomen; "
                   "ask the patient to <b>take a deep breath</b> and to <b>cough</b> (hernias, pain)."),
            (None, "<b>Light palpation</b> of all 9 regions with a flat hand, flexing at the MCP joints – start away from "
                   "the painful area, <b>kneel</b> to the patient’s level and <b>watch the face</b>."),
            (None, "<b>Deep palpation</b> of the 9 regions – describe any mass like a lump (site, size, shape, consistency, "
                   "mobility, pulsatility)."),
            (None, "<b>Liver</b>: start in the right iliac fossa, radial border of the index finger parallel to the costal margin; "
                   "move up 1–2 cm with each breath in. <b>Percuss</b> the upper and lower borders (span)."),
            (None, "<b>Spleen</b>: start in the right iliac fossa and move diagonally towards the left costal margin; "
                   "if not felt, roll the patient onto the right side and repeat. Percuss Traube’s space."),
            (None, "<b>Kidneys</b>: ballot each kidney bimanually (one hand in the loin, the other anteriorly)."),
            (None, "<b>Aorta</b>: both index fingers above the umbilicus – pulsatile or <b>expansile</b>?"),
            (None, "<b>Shifting dullness</b>: percuss from the midline to the flank until dull; keep your finger there, roll the "
                   "patient towards you, wait 30 s, percuss again – dull area now resonant = ascites."),
            (None, "<b>Fluid thrill</b> (tense ascites): patient’s / assistant’s hand edge on the midline, flick one flank and "
                   "feel the impulse on the other."),
            (None, "<b>Auscultate</b>: bowel sounds (listen for at least 10–30 s), aortic and renal bruits."),
            (None, "Examine the <b>hernial orifices</b> (cough impulse) and state you would examine the external genitalia."),
            *closing("examine the external genitalia and perform a <b>PR examination</b> with a chaperone; dip the urine.",
                     "FBC, U&amp;E, LFT, amylase, CRP, clotting; erect CXR (free gas), US abdomen, CT abdomen; "
                     "diagnostic ascitic tap (SAAG, cells, culture, cytology).",
                     "e.g. hepatomegaly / splenomegaly / ascites – state the most likely cause"),
        ]),
        ("B. Per-rectal (PR) examination", [
            ("open", "<b>Wash hands</b>, introduce yourself, explain, obtain <b>verbal consent</b> and have a <b>chaperone</b> present."),
            (None, "Position: <b>left lateral</b>, buttocks at the edge of the bed, <b>knees drawn up to the chest</b>; "
                   "cover the patient with a sheet."),
            (None, "Put on gloves; part the buttocks and <b>inspect</b> the perianal area (ask the patient to strain): "
                   "skin tags, haemorrhoids, fissure (usually posterior midline), fistula openings, warts, ulcers, blood."),
            (None, "Lubricate the index finger; place the pulp on the anal verge, ask the patient to breathe out and "
                   "<b>gently insert</b> the finger, pointing towards the umbilicus."),
            (None, "Assess <b>anal tone</b>: ask the patient to squeeze your finger."),
            (None, "Sweep the finger through <b>360°</b> feeling the rectal wall for masses, ulcers or tenderness."),
            (None, "Anteriorly feel the <b>prostate</b> (size, consistency, surface, median sulcus, nodules, tenderness) "
                   "or the cervix in women."),
            (None, "Withdraw and <b>inspect the glove</b>: stool colour, fresh blood, melaena, mucus, pus."),
            ("close", "Clean the patient, allow them to dress, dispose of gloves, wash hands, thank the patient and the chaperone, "
                      "<b>document</b> and summarise; if indicated: proctoscopy / sigmoidoscopy, FOB, PSA (before PR or 2 days later)."),
        ]),
    ],
    figures=[
        ("git2_light_palp", "Light palpation – flat hand, fingers together, flex at the MCP joints; watch the patient’s face."),
        ("git2_liver", "Liver – from the right iliac fossa upwards, index finger parallel to the costal margin, with each breath in."),
        ("git2_spleen", "Spleen – from the right iliac fossa diagonally towards the left costal margin."),
        ("git2_kidney", "Ballot the kidney – one hand in the loin, push up; feel with the anterior hand."),
        ("git2_shifting", "Shifting dullness – percuss to the flank, keep the finger in place, roll the patient towards you."),
        ("git2_pr_position", "PR examination – left lateral position, knees to chest, patient covered, chaperone present."),
    ],
    map=dict(img="git2_abdomen_map", title="Abdomen – the 9 regions &amp; common scars",
             markers=[(1, 29.4, 21.7), (2, 50, 21.7), (3, 70.6, 21.7), (4, 29.4, 44.7), (5, 50, 51.3), (6, 70.6, 44.7), (7, 31.4, 67.8), (8, 50, 67.8), (9, 68.6, 67.8)],
             rows=[("Right hypochondrium", "Liver, gallbladder; Kocher’s (right subcostal) scar"),
                   ("Epigastrium", "Stomach, pancreas, AAA pulsation; upper midline scar"),
                   ("Left hypochondrium", "Spleen; splenectomy scar"),
                   ("Right flank (lumbar)", "Right kidney, ascending colon; nephrectomy scar"),
                   ("Umbilical region", "Umbilical hernia, caput medusae, laparoscopic port, small bowel"),
                   ("Left flank (lumbar)", "Left kidney, descending colon"),
                   ("Right iliac fossa", "Appendix, caecum; Lanz / gridiron scar; ileostomy (spouted)"),
                   ("Suprapubic (hypogastrium)", "Bladder, uterus; Pfannenstiel scar"),
                   ("Left iliac fossa", "Sigmoid colon, diverticular mass; colostomy (flush)")]),
    tables=[
        dict(title="Spleen vs left kidney", head=["Feature", "Spleen", "Left kidney"],
             rows=[["Direction of enlargement", "Towards the right iliac fossa", "Downwards"],
                   ["Notch", "Present on the medial border", "Absent"],
                   ["Get above it?", "No", "Yes"],
                   ["Ballotable", "No", "Yes"],
                   ["Moves with respiration", "Yes, markedly", "Slightly"],
                   ["Percussion", "Dull", "Resonant (colon in front)"]]),
        dict(title="Causes of organomegaly", head=["Finding", "Common causes"],
             rows=[["Hepatomegaly", "Congestive heart failure, cirrhosis (early), metastases, hepatitis, fatty liver, schistosomiasis"],
                   ["Splenomegaly", "Portal hypertension, haematological (CML, myelofibrosis, lymphoma), infection (malaria, schistosomiasis, EBV), haemolysis"],
                   ["Hepatosplenomegaly", "Chronic liver disease with portal hypertension, lymphoma / leukaemia, schistosomiasis, myeloproliferative disease"],
                   ["Ascites", "Cirrhosis, malignancy (peritoneal), heart failure, nephrotic syndrome, TB peritonitis"]]),
        dict(title="Ascitic fluid – SAAG (serum albumin − ascitic albumin)", head=["SAAG", "Meaning", "Causes"],
             rows=[["≥ 11 g/L", "Portal hypertension (transudate-like)", "Cirrhosis, heart failure, Budd–Chiari, hepatic metastases"],
                   ["&lt; 11 g/L", "Not portal hypertension (exudate-like)", "Peritoneal carcinomatosis, TB, pancreatitis, nephrotic syndrome"]]),
    ],
    checklist=["WIPER; patient flat, exposed nipples to groin", "General inspection + hands/face/neck",
               "Inspects abdomen from foot of bed and side", "Asks to breathe in and cough", "Kneels to the patient’s level",
               "Light palpation of 9 regions, watching face", "Deep palpation of 9 regions", "Palpates liver from RIF with respiration",
               "Percusses liver span", "Palpates spleen from RIF; rolls patient", "Ballots both kidneys", "Palpates aorta",
               "Tests shifting dullness", "Fluid thrill if tense", "Auscultates bowel sounds and bruits",
               "Hernial orifices; mentions genitalia and PR", "PR: consent, chaperone, left lateral position",
               "PR: inspects, tone, 360° sweep, prostate, glove", "Thanks, covers, washes hands", "Summary, differential, investigations"],
    links=[("Abdominal examination", "abdominal examination OSCE"),
           ("Ascites – shifting dullness", "shifting dullness ascites examination"),
           ("Per-rectal examination", "digital rectal examination OSCE")],
),
# =====================================================================================
dict(
    id="uro", num=5, title="Urology",
    subtitle="History of urological symptoms · scrotal examination · renal angle",
    ar="التاريخ البولي: أعراض المسالك البولية السفلية (أعراض التخزين وأعراض الإفراغ)، البيلة الدموية (غير المؤلمة = ورم حتى يثبت العكس)، "
       "ألم الخاصرة (المغص الكلوي). فحص كيس الصفن: هل يمكن الوصول فوق التورم؟ هل الخصية منفصلة عنه؟ هل ينفذ الضوء؟ "
       "وفحص زاوية الكلية بالضغط أو الطَّرْق الخفيف.",
    lookfor=[
        ("Urological history", ["Storage LUTS: frequency, urgency, nocturia, urge incontinence",
                                "Voiding LUTS: hesitancy, poor stream, straining, intermittency, terminal dribbling, incomplete emptying",
                                "Haematuria – timing, painless?", "Dysuria, fever, rigors", "Loin pain (colic → groin)",
                                "Scrotal pain / swelling", "Sexual function", "Smoking, occupational dyes / rubber",
                                "Schistosomiasis exposure", "Previous stones, surgery, catheters"]),
        ("Scrotal inspection", ["Skin: redness, oedema, ulcers, sebaceous cysts", "Scars", "Size &amp; symmetry of the scrotum",
                                "Lie of the testes (horizontal lie – torsion)", "Visible veins (varicocele, standing)"]),
        ("Scrotal palpation", ["Can you get above the swelling?", "Is the testis separate from the swelling?",
                               "Testis: size, consistency, surface, tenderness", "Epididymis (posterolateral)",
                               "Spermatic cord &amp; vas deferens", "Cough impulse", "Transillumination",
                               "Inguinal lymph nodes"]),
        ("Renal angle", ["Inspect loins (scars, swelling)", "Tenderness at the renal angle", "Gentle fist percussion",
                         "Ballot the kidneys"]),
    ],
    procedures=[
        ("A. History of urological symptoms", [
            ("open", "Introduce yourself, confirm identity, consent; open question about the main complaint."),
            (None, "<b>LUTS</b>: storage (frequency, urgency, nocturia, urge incontinence) and voiding (hesitancy, poor stream, "
                   "straining, intermittency, terminal dribbling, incomplete emptying); retention episodes."),
            (None, "<b>Haematuria</b>: visible / non-visible, painful / painless, timing (initial = urethra, terminal = bladder neck "
                   "/ schistosomiasis, total = bladder / kidney), clots."),
            (None, "<b>Pain</b>: loin pain radiating to the groin (ureteric colic), suprapubic pain, dysuria, testicular pain (SOCRATES)."),
            (None, "<b>Infection</b>: fever, rigors, cloudy / offensive urine."),
            (None, "<b>Risk factors</b>: smoking, occupational exposure (aniline dyes, rubber), <b>schistosomiasis</b>, stones, "
                   "catheters, pelvic radiotherapy; drugs (anticholinergics, anticoagulants)."),
            (None, "<b>Systemic</b>: weight loss, bone pain (prostate cancer), symptoms of renal failure."),
            ("close", "<b>ICE</b>, summary and differential diagnosis."),
        ]),
        ("B. Scrotal examination", [
            wiper("from the umbilicus to the knees", "first <b>standing</b> (hernia, varicocele) then lying; <b>chaperone</b> present"),
            (None, "<b>Inspect</b>: scrotal skin, scars, symmetry, swelling, lie of the testes, visible veins; ask the patient to cough."),
            (None, "Put on gloves. <b>Palpate each testis</b> gently between the thumb and the first two fingers, "
                   "starting with the normal side: size, consistency, surface, tenderness."),
            (None, "Feel the <b>epididymis</b> (posterolateral – head, body, tail) and the <b>spermatic cord</b>, rolling the "
                   "<b>vas deferens</b> between finger and thumb."),
            (None, "For a swelling: <b>Can I get above it?</b> (no → inguinoscrotal hernia). <b>Is the testis separate?</b> "
                   "Cystic or solid? Tender?"),
            (None, "<b>Transilluminate</b> with a pen torch in a darkened room (hydrocele, epididymal cyst glow)."),
            (None, "Feel for a <b>cough impulse</b> and a varicocele (‘bag of worms’) with the patient standing."),
            (None, "Palpate the <b>inguinal lymph nodes</b> (scrotal skin drains there; testes drain to para-aortic nodes)."),
            *closing("examine the abdomen (para-aortic nodes, liver, renal mass – left varicocele), the hernial orifices "
                     "and the other testis.",
                     "scrotal ultrasound (all solid lumps), tumour markers (AFP, β-hCG, LDH), urine dipstick &amp; culture; "
                     "suspected torsion = <b>urgent surgical exploration</b> (do not delay for imaging).",
                     "hydrocele, epididymal cyst, testicular tumour, varicocele, inguinoscrotal hernia, epididymo-orchitis, torsion"),
        ]),
        ("C. Renal angle examination", [
            wiper("the back and loins", "sitting up, leaning slightly forward"),
            (None, "Inspect the loins for scars (nephrectomy), swelling, erythema."),
            (None, "Locate the <b>renal angle</b>: between the <b>12th rib</b> and the lateral border of <b>erector spinae</b>."),
            (None, "Press with the thumb, then <b>gently percuss</b> with the ulnar side of a closed fist (or fist on your other "
                   "hand) – watch the face, <b>compare both sides</b>. Tenderness = pyelonephritis, stone, perinephric abscess."),
            (None, "Lie the patient flat and <b>ballot</b> each kidney bimanually."),
            *closing("examine the abdomen, external genitalia and do a PR (prostate).",
                     "urine dipstick, MSU culture, U&amp;E, FBC, CRP; CT KUB (stones), ultrasound kidneys.",
                     "pyelonephritis, ureteric / renal stone, perinephric abscess, musculoskeletal pain"),
        ]),
    ],
    figures=[
        ("uro_renal_angle", "Renal angle – between the 12th rib and erector spinae; gentle fist percussion, compare both sides."),
        ("uro_testis_palp", "Testis between the thumb and first two fingers (diagram, cross-section of the scrotal contents)."),
        ("uro_get_above", "‘Can I get above it?’ – thumb and index finger pinch the cord above the swelling (diagram)."),
        ("uro_transillum", "Transillumination with a pen torch – hydrocele and epididymal cysts glow (diagram)."),
    ],
    map=dict(img="uro_scrotum_map", title="Scrotal contents – anatomical diagram (side view)",
             markers=[(1, 46.8, 22.6), (2, 49.6, 38.7), (3, 46.4, 74.2), (4, 59.3, 59.7), (5, 55.4, 87.1), (6, 32.1, 79)],
             rows=[("Spermatic cord above the swelling", "Get above it? No = inguinoscrotal hernia; ‘bag of worms’ = varicocele"),
                   ("Vas deferens in the cord", "Thickened / beaded (TB)"),
                   ("Testis", "Hard irregular painless lump = tumour; tender, high-riding = torsion"),
                   ("Head of epididymis", "Epididymal cyst (separate, transilluminates)"),
                   ("Tail of epididymis", "Tender swelling = epididymitis; craggy = TB"),
                   ("Tunica vaginalis around testis", "Hydrocele – testis impalpable inside, transilluminates")]),
    tables=[
        dict(title="Scrotal swellings – diagnostic algorithm", head=["Get above?", "Separate from testis?", "Transilluminates?", "Diagnosis"],
             rows=[["No", "—", "No (cough impulse +)", "Inguinoscrotal hernia"],
                   ["Yes", "No (testis impalpable inside)", "Yes", "Hydrocele"],
                   ["Yes", "Yes (above &amp; behind testis)", "Yes", "Epididymal cyst"],
                   ["Yes", "No – arises from testis", "No", "Testicular tumour (until proven otherwise)"],
                   ["Yes", "Yes – in the cord, ‘bag of worms’", "No", "Varicocele (disappears lying down)"],
                   ["Yes", "Tender epididymis ± testis", "No", "Epididymo-orchitis"]]),
        dict(title="Testicular torsion vs epididymo-orchitis", head=["", "Torsion", "Epididymo-orchitis"],
             rows=[["Age", "Usually 10–25 years", "Sexually active adults / older men"],
                   ["Onset", "Sudden, severe pain ± vomiting", "Gradual over days, fever, dysuria"],
                   ["Testis", "High-riding, horizontal lie", "Normal lie, swollen tender epididymis"],
                   ["Cremasteric reflex", "Absent", "Usually present"],
                   ["Prehn’s sign (elevation)", "Pain not relieved", "Pain relieved"],
                   ["Management", "Emergency exploration (&lt; 6 h)", "Antibiotics"]]),
        dict(title="Storage vs voiding LUTS", head=["Storage (irritative)", "Voiding (obstructive)"],
             rows=[["Frequency", "Hesitancy"], ["Urgency", "Poor / weak stream"], ["Nocturia", "Straining"],
                   ["Urge incontinence", "Intermittency"], ["", "Terminal dribbling, incomplete emptying"]]),
    ],
    checklist=["Introduces self, consent, chaperone offered", "LUTS – storage and voiding", "Haematuria characterised",
               "Pain (SOCRATES), fever", "Risk factors incl. smoking and schistosomiasis", "ICE and summary",
               "Scrotum: exposure umbilicus to knees, standing then lying", "Inspects skin, symmetry, lie",
               "Palpates normal testis first", "Testis: size, consistency, surface, tenderness", "Epididymis and spermatic cord / vas",
               "Gets above the swelling; separate from testis?", "Transillumination", "Cough impulse / varicocele",
               "Inguinal lymph nodes", "Renal angle: locates landmarks correctly", "Gentle fist percussion, compares sides",
               "Ballots the kidneys", "Thanks, covers, washes hands", "Summary, differential, investigations"],
    links=[("Urological history", "urological history taking OSCE LUTS haematuria"),
           ("Testicular / scrotal examination", "testicular examination OSCE"),
           ("Renal angle tenderness", "renal angle tenderness examination")],
),
# =====================================================================================
dict(
    id="lump", num=6, title="Lump &amp; Ulcer",
    subtitle="History and examination of a lump · history and examination of an ulcer",
    ar="أي كتلة توصف بنفس الترتيب: الموقع، الحجم، الشكل، السطح، الحافة، القوام، الحرارة والإيلام، التموّج، نفاذ الضوء، النبض، القابلية للرد، "
       "الالتصاق بالجلد وبما تحته، ثم العقد اللمفاوية. والقرحة توصف: الموقع، الحجم، الشكل، الحافة، القاع، القاعدة، العمق، الإفراز، الجلد المحيط، "
       "ثم النبض والإحساس والعقد اللمفاوية.",
    lookfor=[
        ("Lump history", ["When &amp; how noticed", "Duration", "Change in size", "Pain", "Discharge",
                          "Other lumps", "Trauma", "Systemic symptoms (fever, weight loss, night sweats)"]),
        ("Lump – inspection", ["Site (anatomical)", "Size", "Shape", "Skin over it (colour, punctum, scars, ulcer)",
                               "Visible pulsation / movement"]),
        ("Lump – palpation", ["Temperature", "Tenderness", "Size (measure in 2 planes)", "Shape &amp; surface",
                              "Edge (well / ill defined)", "Consistency", "Fluctuation", "Transillumination",
                              "Pulsatility (expansile vs transmitted)", "Compressibility / reducibility, cough impulse",
                              "Fixity to skin and deep structures", "Regional lymph nodes"]),
        ("Ulcer – examination", ["Site", "Size", "Shape", "Edge", "Floor", "Base", "Depth", "Discharge",
                                 "Surrounding skin", "Temperature &amp; tenderness", "Regional lymph nodes",
                                 "Pulses &amp; sensation of the limb"]),
    ],
    procedures=[
        ("A. Examination of a lump", [
            wiper("the lump and the surrounding area generously (compare with the other side)", "comfortably, good light"),
            (None, "Ask about the <b>history</b> briefly: duration, change in size, pain, other lumps."),
            (None, "<b>Inspect</b>: site, size, shape, skin over it (colour, punctum – sebaceous cyst, scars, ulceration), "
                   "visible pulsation."),
            (None, "<b>Palpate</b> (ask about tenderness first): <b>temperature</b> with the back of the fingers, <b>tenderness</b>, "
                   "<b>size</b> with a tape / calipers in two dimensions, <b>shape, surface, edge, consistency</b> (soft, firm, rubbery, hard, bony)."),
            (None, "<b>Fluctuation</b>: two fingers of one hand fix the lump, the index of the other hand presses the centre – "
                   "fixing fingers are displaced = fluid. Test in two planes at right angles."),
            (None, "<b>Transillumination</b>: pen torch from the side in a dark room."),
            (None, "<b>Pulsatility</b>: fingers on either side – pushed apart (expansile = aneurysm) vs pushed up (transmitted)."),
            (None, "<b>Compressibility / reducibility</b> and <b>cough impulse</b> (hernia, saphena varix)."),
            (None, "<b>Fixity</b>: move the skin over the lump (attached to skin?) then contract the underlying muscle "
                   "(fixed to deep structures?)."),
            (None, "<b>Percuss</b> (resonant = gas) and <b>auscultate</b> (bruit, bowel sounds)."),
            (None, "Examine the <b>regional lymph nodes</b>."),
            *closing("examine the regional lymph nodes and the rest of the system / other lumps; general examination.",
                     "ultrasound, FNAC / core biopsy or excision biopsy, MRI / CT as needed, FBC / ESR.",
                     "e.g. lipoma, sebaceous (epidermoid) cyst, ganglion, lymph node, neurofibroma, sarcoma"),
        ]),
        ("B. Examination of an ulcer", [
            wiper("the whole limb / area and compare with the other side", "comfortably"),
            (None, "<b>History</b>: onset, duration, trauma, pain, discharge, previous ulcers, healing, diabetes, PAD, "
                   "varicose veins / DVT, smoking."),
            (None, "<b>Site</b> (gaiter area = venous; tips of toes / pressure points = arterial; sole / metatarsal heads = neuropathic)."),
            (None, "<b>Size</b> (measure) and <b>shape</b> (round, oval, irregular – photograph with a ruler)."),
            (None, "<b>Edge</b>: sloping, punched-out, undermined, rolled or everted (see table)."),
            (None, "<b>Floor</b> (what you see): granulation tissue, slough, necrotic tissue, exposed tendon / bone. "
                   "<b>Base</b> (what you feel beneath): induration, attachment to deep structures. <b>Depth</b>."),
            (None, "<b>Discharge</b>: serous, purulent, blood-stained, offensive."),
            (None, "<b>Surrounding skin</b>: inflammation, pigmentation, venous eczema, lipodermatosclerosis, callus."),
            (None, "Palpate for <b>temperature</b> and <b>tenderness</b>; examine <b>regional lymph nodes</b>."),
            (None, "Assess the <b>local circulation</b> (pulses, ABPI) and <b>sensation</b> of the limb."),
            *closing("perform a full vascular and neurological examination of the limb; check urine glucose.",
                     "wound swab, FBC, CRP, glucose / HbA1c, ABPI, arterial / venous duplex, X-ray (osteomyelitis), "
                     "biopsy of the edge if malignancy suspected (Marjolin’s ulcer).",
                     "venous, arterial, neuropathic (diabetic), pressure, malignant ulcer"),
        ]),
    ],
    figures=[
        ("lump_fluctuation", "Fluctuation test – two fingers fix the lump, the other index finger presses the centre."),
        ("lump_fixity", "Fixity to skin – try to move the skin over the lump."),
        ("lump_transillum", "Transillumination – pen torch from the side in a darkened room."),
        ("lump_measure", "Measure the lump in two dimensions with a tape or calipers."),
    ],
    map=dict(img="lump_ulcer_map", title="Ulcer edges – cross-section diagrams",
             markers=[(1, 6.25, 13.5), (2, 37.5, 13.5), (3, 68.75, 13.5), (4, 6.25, 59.6), (5, 37.5, 59.6), (6, 68.75, 59.6)],
             rows=[("Sloping edge", "Healing ulcer, venous ulcer"),
                   ("Punched-out edge", "Arterial, neuropathic (diabetic), syphilitic gumma"),
                   ("Undermined edge", "Tuberculous ulcer, pressure sore"),
                   ("Rolled (pearly) edge", "Basal cell carcinoma (rodent ulcer)"),
                   ("Everted edge", "Squamous cell carcinoma, Marjolin’s ulcer"),
                   ("Floor / base", "Granulation (healing), slough, tendon / bone exposed (deep)")]),
    tables=[
        dict(title="Venous vs arterial vs neuropathic ulcer", head=["", "Venous", "Arterial", "Neuropathic"],
             rows=[["Site", "Gaiter area, above medial malleolus", "Toes, heels, shins, pressure points",
                    "Sole – metatarsal heads, heel, toe tips"],
                   ["Pain", "Mild, aching; better on elevation", "Very painful, worse on elevation / at night", "Painless"],
                   ["Edge", "Sloping, irregular", "Punched-out", "Punched-out, surrounded by callus"],
                   ["Floor", "Granulation, shallow, exudative", "Pale, necrotic, deep, little exudate", "Deep, may reach bone"],
                   ["Surrounding skin", "Haemosiderin, eczema, lipodermatosclerosis, varicose veins",
                    "Cold, hairless, shiny, pale", "Dry, cracked, warm, callus"],
                   ["Pulses / ABPI", "Present / &gt; 0.8", "Absent / &lt; 0.5", "Present (unless combined); may be calcified"],
                   ["Treatment", "Compression bandaging (after ABPI), elevation", "Revascularisation", "Off-loading, glucose control, debridement"]]),
        dict(title="Consistency of a lump – examples", head=["Consistency", "Feels like", "Examples"],
             rows=[["Soft", "Lips", "Lipoma"], ["Firm", "Tip of the nose", "Reactive lymph node, fibroadenoma"],
                   ["Rubbery", "Thenar eminence", "Lymphoma"], ["Hard", "Forehead", "Carcinoma, calcified lesion"],
                   ["Bony hard", "Bone", "Exostosis, osteoma"]]),
        dict(title="Special signs of lumps", head=["Sign", "Meaning"],
             rows=[["Punctum", "Sebaceous (epidermoid) cyst"], ["Slip sign", "Lipoma – edge slips under the finger"],
                   ["Fluctuation", "Fluid-filled (cyst, abscess)"], ["Transillumination", "Clear fluid – hydrocele, cystic hygroma, ganglion"],
                   ["Expansile pulsation", "Aneurysm"], ["Cough impulse / reducible", "Hernia, saphena varix"],
                   ["Fixed to deep structures", "Malignancy, muscle origin"]]),
    ],
    checklist=["Introduces self, consent, exposes and compares sides", "Brief history of the lump / ulcer",
               "Inspects: site, size, shape, skin", "Asks about tenderness before palpating", "Temperature with back of fingers",
               "Measures size in 2 dimensions", "Surface, edge, consistency", "Fluctuation in 2 planes", "Transillumination",
               "Pulsatility and compressibility / cough impulse", "Fixity to skin and deep structures", "Regional lymph nodes",
               "Ulcer: site, size, shape", "Ulcer: edge, floor, base, depth", "Ulcer: discharge, surrounding skin",
               "Ulcer: pulses and sensation", "Thanks, covers, washes hands", "Summary with differential and investigations"],
    links=[("Lump examination", "lump examination OSCE"),
           ("Ulcer examination", "ulcer examination OSCE edge floor base"),
           ("Leg ulcers – venous vs arterial", "venous vs arterial ulcer examination")],
),
]
