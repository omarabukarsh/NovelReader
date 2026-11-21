from mh import *
from neck import neck_landmarks


def seated(shape=None, gown=True, arms=True):
    ob, ao = human(shape=shape)
    if arms:
        arms_down(ao, 32)
    rot(ao, "clavicle.L", (0, 1, 0), 9); rot(ao, "clavicle.R", (0, 1, 0), -9)   # relaxed, lowered shoulders
    sit(ao); stool(0, 0.12); floor(0)
    if gown:
        cloth(ob, ao, lambda x, y, z: 0.45 < z < 1.13 and not ARMS(x, y, z))   # trousers/gown below the nipples
    return ob, ao


from neck import neck_landmarks


def head_ext(ao, deg=12):
    rot(ao, "neck02", (1, 0, 0), -deg * 0.5); rot(ao, "head", (1, 0, 0), -deg * 0.5)


def thy_inspection():
    """Patient sitting, neck exposed to nipple level, examiner in front at the same level."""
    ob, ao = seated(); head_ext(ao, 10); lights((0, -0.5, 1.0)); L = neck_landmarks(ob, ao)
    camera(L["isthmus"] + Vector((0.08, -0.55, 0.0)), L["isthmus"] + Vector((0, 0, 0.0)), 50)
    pin(1, L["lobeR"]); pin(2, L["thyroglossal"]); pin(3, L["kocher"] + Vector((0.028, 0, 0))); pin(4, L["veins"])
    over("dash", L["kocher"] + Vector((-0.035, 0.006, -0.003)), L["kocher"] + Vector((0.035, 0.006, -0.003)))
    return {}


def thy_tests():
    """Swallowing test and tongue protrusion test - watch the mass from the front/side."""
    ob, ao = seated(); head_ext(ao, 10); lights((0, -0.5, 1.0)); L = neck_landmarks(ob, ao)
    camera(L["isthmus"] + Vector((-0.30, -0.45, 0.0)), L["isthmus"] + Vector((0, 0, 0.015)), 50)
    t = L["isthmus"] + Vector((0, -0.012, 0)); g = L["thyroglossal"] + Vector((0, -0.012, 0))
    over("arrow", t + Vector((0, -0.01, -0.012)), t + Vector((0, -0.01, 0.018)))
    over("arrow", g + Vector((0, -0.01, -0.006)), g + Vector((0, -0.01, 0.020)))
    pin(1, L["isthmus"]); pin(2, L["thyroglossal"])
    return {}


def thy_front3t():
    """From the front - 3T: temperature (back of the hand), tenderness, tracheal position (index fingertip in the notch)."""
    ob, ao = seated(); lights((0, -0.5, 1.0)); L = neck_landmarks(ob, ao)
    nt = L["notch"]
    place_hand("right", "point", nt + Vector((0, -0.002, 0.006)), finger_dir=(0.05, 0.45, -0.89), palm_dir=(0, 1, 0.2))
    camera(nt + Vector((-0.40, -0.40, 0.06)), nt + Vector((0, 0, 0.02)), 45)
    pin(1, nt)
    return {}


def thy_palpation():
    """From behind: neck slightly flexed; pads of index, middle and ring fingers of both hands on each lobe;
    thumbs on the back of the neck."""
    ob, ao = seated(); rot(ao, "neck02", (1, 0, 0), 10); lights((0, -0.5, 1.0)); L = neck_landmarks(ob, ao)
    lr, ll = L["lobeR"], L["lobeL"]
    place_hand("right", "flat", lr + Vector((-0.003, -0.003, 0)), finger_dir=(0.55, -0.80, -0.20), palm_dir=(0.85, -0.45, 0),
               tip="middle-finger-tip")
    place_hand("left", "flat", ll + Vector((0.003, -0.003, 0)), finger_dir=(-0.55, -0.80, -0.20), palm_dir=(-0.85, -0.45, 0),
               tip="middle-finger-tip")
    camera(L["isthmus"] + Vector((0.16, -0.55, 0.10)), L["isthmus"] + Vector((0, 0.03, 0.03)), 42)
    pin(1, lr); pin(2, ll)
    return {}


def thy_nodes():
    """Cervical lymph nodes - examined from behind in this order."""
    ob, ao = seated(); lights((-0.3, -0.4, 1.1)); L = neck_landmarks(ob, ao)
    keys = ["submental", "submand", "tonsil", "preaur", "postaur", "occip", "ant_cerv", "post_cerv", "supraclav"]
    camera(L["angle"] + Vector((-0.56, -0.10, 0.0)), L["angle"] + Vector((0.0, 0.015, -0.015)), 40)
    for i, k in enumerate(keys, 1):
        pin(i, L[k])
    return {}


def thy_general():
    """General exam: arms outstretched, fingers spread, sheet of paper on the dorsum of the hands (fine tremor)."""
    ob, ao = seated(); lights((0, -0.6, 1.0))
    for sd in ("L", "R"):
        sg = 1 if sd == "L" else -1
        aim(ao, f"upperarm01.{sd}", (0.12 * sg, -1, 0), f"lowerarm01.{sd}")
        aim(ao, f"lowerarm01.{sd}", (0.04 * sg, -1, 0), f"wrist.{sd}")
    bpy.context.view_layer.update()
    wl, wr = bone_world(ao, "wrist.L"), bone_world(ao, "wrist.R")
    c = (wl + wr) / 2 + Vector((0, -0.075, 0.032))
    box("paper", c, (0.30, 0.21, 0.002), mat("paper", srgb("#ffffff"), 0.9), 0.0005)
    hd = bone_world(ao, "head")
    camera(hd + Vector((-0.80, -1.00, -0.02)), (c + hd) / 2 + Vector((0, 0, -0.06)), 40)
    pin(1, c + Vector((0, 0, 0.004)))
    return {}


SCENES = dict(thy3d_inspection=thy_inspection, thy3d_tests=thy_tests, thy3d_palpation=thy_palpation,
              thy3d_front=thy_front3t, thy3d_nodes=thy_nodes, thy3d_general=thy_general)
