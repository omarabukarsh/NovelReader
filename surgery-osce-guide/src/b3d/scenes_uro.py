from mh import *


def renal_angle_setup():
    """Patient sitting, leaning slightly forward, back exposed; examiner behind."""
    from scenes_thy import seated
    ob, ao = human(); arms_down(ao, 30)
    rot(ao, "clavicle.L", (0, 1, 0), 9); rot(ao, "clavicle.R", (0, 1, 0), -9)
    sit(ao); stool(0, 0.12); floor(0)
    rot(ao, "spine03", (1, 0, 0), 12)          # lean slightly forward
    cloth(ob, ao, lambda x, y, z: 0.45 < z < 0.97 and not ARMS(x, y, z))
    lights((0, 0.6, 1.0))
    bpy.context.view_layer.update()
    # 12th rib / renal angle: posterior surface at rest height ~1.06, ~6 cm lateral to the midline (erector spinae edge)
    sp = bone_world(ao, "spine03")
    pts = {}
    for sd, sg in (("R", -1), ("L", 1)):
        a = surf(ob, Vector((sg * 0.065, sp.y, sp.z + 0.06)), Vector((0, 1, 0)), back=0.25)[0]
        pts[sd] = a
    pts["rib12"] = surf(ob, Vector((-0.10, sp.y, sp.z + 0.085)), Vector((-0.3, 1, 0)), back=0.25)[0]
    pts["spine"] = surf(ob, Vector((0, sp.y, sp.z + 0.06)), Vector((0, 1, 0)), back=0.25)[0]
    return ob, ao, pts


def uro_renal_angle():
    ob, ao, P = renal_angle_setup()
    a = P["R"]
    camera(a + Vector((0.10, 0.75, 0.18)), P["spine"] + Vector((0, 0, 0.0)), 40)
    pin(1, P["R"]); pin(2, P["L"]); pin(3, P["rib12"])
    over("dash", P["rib12"] + Vector((-0.03, 0, -0.012)), P["spine"] + Vector((0, 0, 0.02)))
    over("dash", P["spine"] + Vector((-0.045, 0, 0.07)), P["spine"] + Vector((-0.045, 0, -0.06)))
    return {}


def uro_percussion():
    """CVA (renal angle) tenderness: LEFT hand flat over the renal angle, gentle blow with the ulnar side of the RIGHT fist;
    compare both sides, watch the face."""
    ob, ao, P = renal_angle_setup()
    a = P["R"]
    place_hand("left", "flat", a + Vector((0.035, 0.004, 0.0)), finger_dir=(-1, 0.05, 0.05), palm_dir=(0, -1, 0), tip="middle-finger-tip")
    place_hand("right", "fist", a + Vector((-0.005, 0.06, 0.035)), finger_dir=(0.1, -0.2, -1), palm_dir=(1, 0, 0), tip="pinky-finger-phalanx-proximal")
    camera(a + Vector((-0.55, 0.55, 0.10)), a + Vector((0.02, 0.02, 0.03)), 40)
    over("arrow", a + Vector((-0.005, 0.12, 0.09)), a + Vector((-0.005, 0.06, 0.05)))
    pin(1, a)
    return {}


SCENES = dict(uro3d_renal_angle=uro_renal_angle, uro3d_percussion=uro_percussion)
