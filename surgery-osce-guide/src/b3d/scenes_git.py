from mh import *
from neck import neck_landmarks


Z_UMB, Z_SUBCOSTAL, Z_TT, Z_PUBIS, Z_XIPH = 1.00, 1.08, 0.95, 0.86, 1.165


def abdo_pts(ob, ao):
    """Abdominal landmarks measured on the model (rest-pose heights): umbilicus 1.00, subcostal plane 1.08,
    transtubercular plane 0.95, pubis 0.86, xiphisternum ~1.165; mid-clavicular / mid-inguinal lines x = +-0.06."""
    F = lambda x, z: front(ob, x, z)
    P = {"umb": F(0, Z_UMB)}
    rows = {1: 1.125, 0: 1.015, -1: 0.905}
    cols = {-1: -0.098, 0: 0.0, 1: 0.098}
    names = {(-1, 1): "RH", (0, 1): "EPI", (1, 1): "LH", (-1, 0): "RL", (0, 0): "UMB", (1, 0): "LL", (-1, -1): "RIF", (0, -1): "SP", (1, -1): "LIF"}
    for (cx, cy), nm in names.items():
        P[nm] = F(cols[cx], rows[cy])
    xm = 0.058
    P["lines"] = [(F(-xm, 1.17), F(-xm, 0.875)), (F(xm, 1.17), F(xm, 0.875)),
                  (F(-0.12, Z_SUBCOSTAL), F(0.12, Z_SUBCOSTAL)), (F(-0.13, Z_TT), F(0.13, Z_TT))]
    P["F"] = F
    return P


def abdomen_scene(**kw):
    ob, ao = supine("chest", **kw); lights((0, 0.1, 0.9)); P = abdo_pts(ob, ao)
    return ob, ao, P


def git_regions():
    ob, ao, P = abdomen_scene()
    camera(P["UMB"] + Vector((0.0, -0.05, 0.85)), P["UMB"] + Vector((0, 0.015, 0)), 40)
    for a, b in P["lines"]:
        over("dash", a, b)
    for i, k in enumerate(["RH", "EPI", "LH", "RL", "UMB", "LL", "RIF", "SP", "LIF"], 1):
        pin(i, P[k])
    return {}


def git_inspection():
    """Inspection from the end of the bed (eye level with the abdomen) then from the right side."""
    ob, ao, P = abdomen_scene()
    camera(P["UMB"] + Vector((0.0, -1.15, 0.30)), P["UMB"] + Vector((0, 0.08, 0.0)), 55)
    pin(1, P["UMB"]); pin(2, surf(ob, P["RL"], Vector((-1, 0, 0.3)), back=0.12)[0]); pin(3, P["EPI"])
    return {}


def git_superficial():
    """Superficial palpation: flat hand, fingers together, flexion at the MCP joints; start in the RIF, examiner kneeling
    at the patient's right side, watching the face; move through all 9 regions."""
    ob, ao, P = abdomen_scene()
    rif = P["RIF"]
    place_hand("right", "flat", rif + Vector((0.0, 0.0, 0.005)), finger_dir=(0.45, 0.89, -0.05), palm_dir=(0, 0, -1),
               tip="middle-finger-tip")
    path = [P[k] for k in ("RIF", "RL", "RH", "EPI", "LH", "LL", "LIF", "SP", "UMB")]
    for a, b in zip(path, path[1:]):
        over("arrow", a + Vector((0, 0, 0.01)), b + Vector((0, 0, 0.01)))
    camera(P["UMB"] + Vector((-0.42, -0.38, 0.55)), P["UMB"] + Vector((0, 0.02, 0)), 40)
    pin(1, rif)
    return {}


def git_liver():
    """Liver: radial border of the index finger parallel to the right costal margin; start in the RIF and move up
    1-2 cm with each deep breath in."""
    ob, ao, P = abdomen_scene()
    t = P["F"](-0.075, 1.04)
    place_hand("right", "flat", t + Vector((0, 0, 0.004)), finger_dir=(0.80, 0.60, -0.05), palm_dir=(0, 0, -1), tip="index-finger-tip")
    over("arrow", P["RIF"] + Vector((0, 0, 0.01)), P["RH"] + Vector((0, 0.02, 0.01)))
    camera(P["UMB"] + Vector((-0.42, -0.38, 0.55)), P["UMB"] + Vector((-0.02, 0.03, 0)), 40)
    pin(1, P["RIF"]); pin(2, P["RH"] + Vector((0, 0.02, 0)))
    return {}


def git_spleen():
    """Spleen: from the RIF diagonally toward the left costal margin (left hypochondrium), with respiration."""
    ob, ao, P = abdomen_scene()
    t = P["F"](0.02, 1.02)
    place_hand("right", "flat", t + Vector((0, 0, 0.004)), finger_dir=(0.70, 0.71, -0.05), palm_dir=(0, 0, -1), tip="index-finger-tip")
    over("arrow", P["RIF"] + Vector((0, 0, 0.01)), P["LH"] + Vector((0, 0.03, 0.01)))
    camera(P["UMB"] + Vector((-0.42, -0.38, 0.55)), P["UMB"] + Vector((0.02, 0.03, 0)), 40)
    pin(1, P["RIF"]); pin(2, P["LH"] + Vector((0, 0.03, 0)))
    return {}


def git_kidney():
    """Bimanual (ballottement) - right kidney: LEFT hand palm-up under the right loin (between couch and back) pushes up;
    RIGHT hand flat on the right lumbar region anteriorly feels the kidney."""
    ob, ao, P = abdomen_scene()
    F = P["F"]; rl = F(-0.085, 1.02)
    back_z = COUCH_TOP + 0.012
    loin = Vector((-0.045, rl.y, back_z))
    place_hand("left", "flat", loin, finger_dir=(1, 0.1, 0.0), palm_dir=(0, 0, 1), tip="middle-finger-tip", sleeve=True)
    place_hand("right", "flat", rl + Vector((0, 0, 0.004)), finger_dir=(0.45, 0.89, -0.05), palm_dir=(0, 0, -1), tip="middle-finger-tip")
    camera(rl + Vector((-0.72, -0.10, 0.06)), rl + Vector((0.03, 0, -0.045)), 38)
    over("arrow", loin + Vector((-0.06, 0, 0.0)), loin + Vector((-0.06, 0, 0.07)))
    pin(1, rl); pin(2, loin + Vector((-0.06, 0, 0)))
    return {}


def git_shifting():
    """Shifting dullness: percuss from the umbilicus out to the right flank with the LEFT middle finger (pleximeter) held
    parallel to the fluid level (along the body axis) and struck by the RIGHT middle finger; where the note becomes dull
    keep the finger there, roll the patient toward you (onto the left side), wait, percuss again."""
    ob, ao, P = abdomen_scene()
    fl = surf(ob, P["RL"] + Vector((-0.035, 0, -0.03)), Vector((-0.8, 0, 0.6)), back=0.12)[0]
    place_hand("left", "flat", fl + Vector((0, 0, 0.004)), finger_dir=(0.10, 1.0, -0.15), palm_dir=(0.5, 0, -1), tip="middle-finger-tip")
    bpy.context.view_layer.update()
    mid = fl + Vector((-0.01, -0.035, 0.012))      # middle phalanx of the left middle finger
    place_hand("right", "tap", mid + Vector((-0.01, 0, 0.018)), finger_dir=(0.25, 0.15, -1), palm_dir=(0.3, 0.6, -0.5),
               tip="middle-finger-tip")
    over("arrow", P["UMB"] + Vector((0, 0, 0.02)), fl + Vector((0.02, 0.03, 0.03)))
    camera(fl + Vector((-0.55, -0.35, 0.18)), fl + Vector((0.04, 0.02, 0.0)), 40)
    pin(1, P["UMB"]); pin(2, fl)
    return {}


def git_auscultation():
    """Auscultation sites (channel): bowel sounds RIF; aortic bruit epigastrium midline above the umbilicus;
    renal bruits 2-3 cm above and lateral to the umbilicus; iliac bruits above and medial to the ASIS; venous hum around the umbilicus."""
    ob, ao, P = abdomen_scene()
    u = P["UMB"]; F = P["F"]
    pts = [P["RIF"], F(0, Z_UMB + 0.06), F(-0.025, Z_UMB + 0.025), F(0.025, Z_UMB + 0.025), F(-0.075, 0.925),
           F(0.075, 0.925), F(0.0, Z_UMB - 0.022)]
    camera(u + Vector((0.0, -0.05, 0.70)), u + Vector((0, 0.015, 0)), 40)
    for i, p in enumerate(pts, 1):
        pin(i, p)
    return {}


def git_pr():
    """PR: left lateral (Sims) position, back to the examiner, knees fully flexed toward the chest, covered with a sheet."""
    ob, ao = human()
    arms_down(ao)
    for sd in ("L", "R"):
        aim(ao, f"upperleg01.{sd}", (0.05 * (1 if sd == "L" else -1), -0.78, 0.62), f"lowerleg01.{sd}")   # hips flexed ~130 deg (knees to chest)
        aim(ao, f"lowerleg01.{sd}", (0, 0.62, -0.78), f"foot.{sd}")                                    # knees fully flexed, heels near buttocks
    aim(ao, "upperarm01.L", (0.2, -0.7, -0.6), "lowerarm01.L"); aim(ao, "upperarm01.R", (-0.1, -0.8, -0.5), "lowerarm01.R")
    rot(ao, "spine03", (1, 0, 0), 12)
    cloth(ob, ao, lambda x, y, z: 0.97 < z < 1.40 and not ARMS(x, y, z), thickness=0.008, push=0.006)
    cloth(ob, ao, lambda x, y, z: 0.35 < z <= 0.99 and not ARMS(x, y, z), name="sheet", material=SHEET(), thickness=0.012, push=0.010)
    bpy.context.view_layer.update()
    M = Matrix.Rotation(math.radians(90), 4, "Y") @ Matrix.Rotation(math.radians(-90), 4, "X")
    ao.matrix_world = Matrix.Translation((0, -0.55, COUCH_TOP + 0.16)) @ M
    bpy.context.view_layer.update()
    hips = (bone_world(ao, "upperleg01.L") + bone_world(ao, "upperleg01.R")) / 2
    ao.location.x += (-0.42 + 0.13) - hips.x          # buttocks at the edge of the couch, toward the examiner
    bpy.context.view_layer.update()
    couch(-0.42, 0.42, -1.25, 0.70, COUCH_TOP); floor(0); lights((0, -0.3, 0.9))
    anus = (bone_world(ao, "upperleg01.L") + bone_world(ao, "upperleg01.R")) / 2
    camera(anus + Vector((-1.10, -0.55, 0.70)), anus + Vector((0.05, 0.25, -0.02)), 38)
    pin(1, anus + Vector((-0.09, 0, -0.01)))
    return {}


def git_general():
    """General GIT examination - where to look (channel order: general look, hands, head & neck, chest, abdomen,
    groin & perineum, lower limbs)."""
    ob, ao = supine("brief"); lights((0, -0.2, 0.9))
    hand_r = bone_world(ao, "wrist.R"); face = bone_world(ao, "head")
    eye = surf(ob, face + Vector((-0.03, 0.04, 0)), Vector((0, 0, 1)))[0]
    mouth = surf(ob, face + Vector((0, 0.0, 0)), Vector((0, 0, 1)))[0]
    L = neck_landmarks(ob, ao) if False else None
    S = lambda x, y: surf(ob, Vector((x, y, COUCH_TOP + 0.10)), Vector((0, 0, 1)))[0]
    n1 = bone_world(ao, "neck01")
    hd_r = surf(ob, bone_world(ao, "finger3-1.R"), Vector((-0.3, 0, 1)), back=0.12)[0]
    pts = [hd_r, eye, mouth, front(ob, 0.07, 1.37, (0.3, 0, 1)), front(ob, -0.09, 1.25), front(ob, 0.04, 1.03),
           front(ob, -0.10, 0.85), surf(ob, bone_world(ao, "lowerleg01.R").lerp(bone_world(ao, "foot.R"), 0.6), Vector((0, 0, 1)))[0]]
    camera((-1.35, -0.55, 1.95), (0, -0.25, 0.82), 40)
    for i, p in enumerate(pts, 1):
        pin(i, p)
    return {}


def git_asterixis():
    """Flapping tremor: arms outstretched, wrists dorsiflexed (cocked back), fingers spread, hold for 15 s."""
    from scenes_thy import seated
    ob, ao = seated(); lights((0, -0.6, 1.0))
    for sd in ("L", "R"):
        sg = 1 if sd == "L" else -1
        aim(ao, f"upperarm01.{sd}", (0.12 * sg, -1, 0), f"lowerarm01.{sd}")
        aim(ao, f"lowerarm01.{sd}", (0.04 * sg, -1, 0), f"wrist.{sd}")
        aim(ao, f"wrist.{sd}", (0.05 * sg, -0.35, 1), f"finger3-1.{sd}")
    bpy.context.view_layer.update()
    wr = bone_world(ao, "wrist.R"); f3 = bone_world(ao, "finger3-3.R", "tail")
    camera(wr + Vector((-0.75, 0.05, 0.10)), (wr + f3) / 2 + Vector((0, 0.15, 0)), 40)
    over("arc", wr, f3, wr + (f3 - wr).length * Vector((0, -0.75, 0.66)).normalized(), label="")
    pin(1, wr)
    return {}


SCENES = dict(git3d_regions=git_regions, git3d_inspection=git_inspection, git3d_superficial=git_superficial,
              git3d_liver=git_liver, git3d_spleen=git_spleen, git3d_kidney=git_kidney, git3d_shifting=git_shifting,
              git3d_auscultation=git_auscultation, git3d_pr=git_pr, git3d_general=git_general, git3d_asterixis=git_asterixis)
