from mh import *

def legpts(ob, ao, sd="R"):
    """Surface landmarks of a supine leg (patient's right = -X)."""
    sg = -1 if sd == "R" else 1
    hip = bone_world(ao, f"upperleg01.{sd}"); knee = bone_world(ao, f"lowerleg01.{sd}")
    ank = bone_world(ao, f"foot.{sd}"); toe1 = bone_world(ao, f"toe1-1.{sd}"); toe2 = bone_world(ao, f"toe2-1.{sd}")
    toe5 = bone_world(ao, f"toe5-1.{sd}"); toe1t = bone_world(ao, f"toe1-2.{sd}", "tail")
    up = Vector((0, 0, 1)); med = Vector((-sg, 0, 0)); lat = Vector((sg, 0, 0))
    P = {}
    gy = hip.y - 0.045
    P["femoral"], _ = surf(ob, Vector((sg * 0.095, gy, hip.z)), up)
    P["popliteal"], _ = surf(ob, knee + Vector((0, 0.0, 0)), Vector((0, 0, -1)))
    P["pt"], _ = surf(ob, ank + Vector((0, 0.025, -0.015)), med)
    P["dp"], P["dp_n"] = surf(ob, ank.lerp(toe2, 0.45), Vector((0, 0.25, 1)))
    P["shin"], _ = surf(ob, knee.lerp(ank, 0.45), up + Vector((0, 0, 0)))
    P["calf"], _ = surf(ob, knee.lerp(ank, 0.3), lat + Vector((0, 0, -0.3)))
    P["thigh"], _ = surf(ob, hip.lerp(knee, 0.55), up)
    P["gaiter"], _ = surf(ob, knee.lerp(ank, 0.82), med + Vector((0, 0, 0.4)))
    P["medknee"], _ = surf(ob, knee + Vector((0, 0.06, 0)), med)
    P["toes"] = toe1.lerp(toe5, 0.5) + Vector((0, -0.02, 0.025))
    P["bigtoe"], _ = surf(ob, toe1t, Vector((0, 0.3, 1)))
    P["heel"], _ = surf(ob, ank + Vector((0, 0.0, -0.06)), Vector((0, -1, -0.4)))
    P["ankle"] = ank; P["knee"] = knee; P["hip"] = hip; P["toe1"] = toe1
    P["tt"], _ = surf(ob, knee.lerp(ank, 0.12), up)        # tibial tuberosity
    return P


def pvd_inspection():
    ob, ao = supine("pelvis"); lights((0, -0.8, 0.8)); P = legpts(ob, ao)
    camera((-0.95, -1.95, 1.55), (0.02, -0.72, 0.82), 42)
    for i, k in enumerate(["thigh", "shin", "calf", "gaiter", "toes", "heel", "medknee", "bigtoe"], 1):
        pin(i, P[k])
    return {}


def pvd_pulses():
    ob, ao = supine("pelvis"); lights((0, -0.8, 0.8)); P = legpts(ob, ao)
    camera((-1.05, -1.65, 1.45), (0.0, -0.62, 0.80), 42)
    for i, k in enumerate(["femoral", "popliteal", "pt", "dp"], 1):
        pin(i, P[k])
    pin(5, P["bigtoe"])
    return {}


def pvd_dp():
    ob, ao = supine("pelvis"); lights((0, -0.9, 0.8)); P = legpts(ob, ao)
    dp, n = P["dp"], P["dp_n"]
    place_hand("right", "pulse", dp + n * 0.004, finger_dir=(1, -0.1, -0.35), palm_dir=-n)
    camera(dp + Vector((-0.40, -0.32, 0.40)), dp + Vector((0.06, 0.02, -0.03)), 45)
    pin(1, dp)
    return {}


def pvd_popliteal():
    """Knee flexed ~40 deg, foot flat on the couch. Both hands wrap round the knee: fingertips of both hands meet
    in the popliteal fossa, thumbs rest on the front of the knee (toward the tibial tuberosity)."""
    ob, ao = supine("pelvis", extra=lambda ao: (aim(ao, "upperleg01.R", (0, -0.45, -0.89), "lowerleg01.R"),
                                                aim(ao, "lowerleg01.R", (0, 0.40, -0.92), "foot.R"),
                                                aim(ao, "foot.R", (0, -1, -0.15), "toe2-1.R")))
    lights((0, -0.7, 0.9)); P = legpts(ob, ao)
    knee = P["knee"]
    pp, n = surf(ob, knee + Vector((0, 0.0, -0.005)), Vector((0, 0.25, -1)), back=0.12)
    place_hand("right", "tips", pp + Vector((-0.012, 0, 0.003)), finger_dir=(0.78, 0.30, -0.55), palm_dir=(0.8, 0, 0.6),
               tip="middle-finger-tip", sleeve_len=0.08)
    place_hand("left", "tips", pp + Vector((0.012, 0, 0.003)), finger_dir=(-0.78, 0.30, -0.55), palm_dir=(-0.8, 0, 0.6),
               tip="middle-finger-tip", sleeve_len=0.08)
    camera(pp + Vector((-0.55, -0.12, -0.03)), pp + Vector((0, 0, 0.03)), 40)
    pin(1, pp)
    return {}


def pvd_pt():
    """Posterior tibial: fingertips (index + middle) just behind and below the medial malleolus."""
    ob, ao = supine("pelvis"); lights((0, -0.9, 0.8)); P = legpts(ob, ao)
    pt = P["pt"]
    place_hand("right", "pulse", pt + Vector((0.004, 0, 0)), finger_dir=(0.15, 0.25, -1), palm_dir=(-1, 0, -0.1), sleeve_len=0.28)
    camera(pt + Vector((0.42, -0.42, 0.22)), pt + Vector((-0.02, 0, 0.02)), 45)
    pin(1, pt)
    return {}


def pvd_femoral():
    """Femoral: pads of index + middle fingers at the mid-inguinal point (between ASIS and pubic symphysis)."""
    ob, ao = supine("pelvis"); lights((0, -0.4, 0.8)); P = legpts(ob, ao)
    fe = P["femoral"]
    place_hand("right", "pulse", fe + Vector((0, 0, 0.004)), finger_dir=(0.45, 0.40, -0.80), palm_dir=(0.3, 0.3, -1), sleeve_len=0.30)
    camera(fe + Vector((-0.50, -0.30, 0.42)), fe + Vector((0.02, 0.02, 0.04)), 45)
    pin(1, fe)
    return {}


def pvd_buerger():
    ob, ao = supine("pelvis", extra=lambda ao: aim(ao, "upperleg01.R", (0, -0.71, -0.71), "lowerleg01.R")); lights((0, -0.5, 1.1)); P = legpts(ob, ao)
    hip, ank = P["hip"], P["ankle"]
    camera(hip + Vector((-1.75, -0.35, 0.35)), hip + Vector((0, -0.40, 0.30)), 42)
    flat = hip + Vector((0, -0.55, 0)); raised = hip + (ank - hip).normalized() * 0.55
    over("dash", hip, flat); over("dash", hip, raised); over("arc", hip, flat, raised, label="45°")
    pin(1, P["bigtoe"])
    # foot pallor
    return {}


def pvd_calf():
    ob, ao = supine("pelvis"); lights((0, -0.8, 0.8)); P = legpts(ob, ao)
    tt, kn, an = P["tt"], P["knee"], P["ankle"]
    axis = (an - kn).normalized(); c = kn + axis * 0.15
    # tape measure ring around the calf 10 cm below the tibial tuberosity
    bpy.ops.mesh.primitive_torus_add(major_radius=0.062, minor_radius=0.004, location=c)
    t = bpy.context.object; t.rotation_mode = "QUATERNION"; t.rotation_quaternion = axis.to_track_quat("Z", "Y")
    t.scale = (1.0, 0.85, 3.0); t.data.materials.append(mat("tape", srgb("#f2c94c"), 0.5))
    tt2, _ = surf(ob, c, Vector((0, 0, 1)))
    camera(kn + Vector((-0.65, -0.55, 0.45)), kn.lerp(an, 0.3), 45)
    pin(1, tt); pin(2, tt2); over("dash", tt, tt2, label="10 cm")
    return {}


def pvd_trendelenburg():
    ob, ao = human(); arms_down(ao); floor(0); lights((0, 0, 0.6))
    cloth(ob, ao, SHORTS); cloth(ob, ao, BRIEF, name="drape", material=GOWN(), thickness=0.012)
    hip = bone_world(ao, "upperleg01.R"); knee = bone_world(ao, "lowerleg01.R")
    c0 = hip.lerp(knee, 0.22)
    f_, _ = surf(ob, c0, Vector((0, -1, 0)), back=0.15); b_, _ = surf(ob, c0, Vector((0, 1, 0)), back=0.15)
    l_, _ = surf(ob, c0, Vector((-1, 0, 0)), back=0.15); m_, _ = surf(ob, c0, Vector((1, 0, 0)), back=0.06)
    c = Vector(((l_.x + m_.x) / 2, (f_.y + b_.y) / 2, c0.z))
    rx, ry = abs(l_.x - m_.x) / 2, abs(f_.y - b_.y) / 2
    bpy.ops.mesh.primitive_torus_add(major_radius=1.0, minor_radius=0.012, location=c)
    t = bpy.context.object; t.scale = (rx + 0.008, ry + 0.008, 1.0); t.data.materials.append(mat("tq", srgb("#5d6773"), 0.5))
    camera((-0.55, -1.10, 0.75), (-0.08, 0, 0.62), 40)
    gsv, _ = surf(ob, knee + Vector((0, 0.0, 0.05)), Vector((1, -0.6, 0)))
    sfj, _ = surf(ob, Vector((-0.085, hip.y - 0.04, hip.z - 0.06)), Vector((0, -1, 0)))
    pin(1, c + Vector((-0.05, -0.065, 0))); pin(2, sfj); pin(3, gsv)
    return {}


SCENES = dict(pvd3d_pt=pvd_pt, pvd3d_femoral=pvd_femoral, pvd3d_inspection=pvd_inspection, pvd3d_pulses=pvd_pulses, pvd3d_dp=pvd_dp, pvd3d_popliteal=pvd_popliteal,
              pvd3d_buerger=pvd_buerger, pvd3d_calf=pvd_calf, pvd3d_trendelenburg=pvd_trendelenburg)
