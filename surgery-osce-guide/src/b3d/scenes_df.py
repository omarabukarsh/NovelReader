from mh import *
from scenes_pvd import legpts


def tool_cyl(a, b, r, material):
    a, b = Vector(a), Vector(b); d = b - a
    bpy.ops.mesh.primitive_cylinder_add(radius=r, depth=d.length, location=(a + b) / 2, vertices=24)
    o = bpy.context.object; o.rotation_mode = "QUATERNION"; o.rotation_quaternion = d.normalized().to_track_quat("Z", "Y")
    o.data.materials.append(material); bpy.ops.object.shade_smooth(); return o


def tuning_fork(base, axis, side):
    """128 Hz fork: foot (base) on the skin, stem along axis, two prongs."""
    axis = Vector(axis).normalized(); side = Vector(side).normalized()
    tool_cyl(base, base + axis * 0.09, 0.004, STEEL())
    tool_cyl(base + axis * 0.09 + side * 0.009, base + axis * 0.09 - side * 0.009, 0.004, STEEL())
    for sg in (1, -1):
        tool_cyl(base + axis * 0.09 + side * 0.009 * sg, base + axis * 0.21 + side * 0.009 * sg, 0.0035, STEEL())
    bpy.ops.mesh.primitive_uv_sphere_add(radius=0.007, location=base + axis * 0.004); bpy.context.object.data.materials.append(STEEL())


def sole_pts(ob, ao):
    """Points on the sole of the right foot of the supine patient (sole faces the foot end, -Y)."""
    an = bone_world(ao, "foot.R")
    S = lambda b, where="head", dz=0.0: ray(ob, bone_world(ao, b, where) + Vector((0, -0.25, dz)), (0, 1, 0))[0]
    P = {"hallux": S("toe1-2.R", "tail", -0.004), "mt1": S("toe1-1.R", "head", -0.012), "mt3": S("toe3-1.R", "head", -0.012),
         "mt5": S("toe5-1.R", "head", -0.010), "heel": ray(ob, an + Vector((0, -0.25, -0.045)), (0, 1, 0))[0],
         "web": S("toe2-1.R", "tail", 0.004)}
    return an, P


def sole_cam(an):
    camera(Vector((an.x + 0.02, an.y - 0.62, an.z + 0.10)), Vector((an.x + 0.03, an.y, an.z + 0.02)), 34)


def df_inspection():
    """Inspect both feet: soles, heels, between the toes (hidden ulcers, fungal infection), nails, callus, deformity."""
    ob, ao = supine("pelvis"); lights((0, -1.6, 1.0))
    an, P = sole_pts(ob, ao)
    sole_cam(an)
    pin(1, P["heel"]); pin(2, P["mt1"]); pin(3, P["web"])
    return {}


def df_sole_points():
    """Monofilament / pressure sites on the sole: plantar big toe, 1st, 3rd, 5th metatarsal heads, heel."""
    ob, ao = supine("pelvis"); lights((0, -1.6, 1.0))
    an, P = sole_pts(ob, ao)
    sole_cam(an)
    for i, k in enumerate(["hallux", "mt1", "mt3", "mt5", "heel"], 1):
        pin(i, P[k])
    return {}


def df_monofilament():
    """10 g monofilament pressed perpendicular to the sole until it bends, 1-2 s; patient's eyes closed."""
    ob, ao = supine("pelvis"); lights((0, -1.6, 1.0))
    an, P = sole_pts(ob, ao)
    p = P["mt1"]
    tool_cyl(p, p + Vector((0, -0.032, 0.006)), 0.0009, mat("nylon", srgb("#3c6fb0"), 0.4))
    tool_cyl(p + Vector((0, -0.032, 0.006)), p + Vector((0.01, -0.14, 0.03)), 0.005, mat("handle", srgb("#e9eef3"), 0.4))
    place_hand("right", "pinch", p + Vector((0.006, -0.10, 0.022)), finger_dir=(-0.2, 0.75, -0.6), palm_dir=(0, 0.3, -1),
               tip="index-finger-tip")
    camera(Vector((an.x - 0.50, an.y - 0.16, an.z + 0.10)), p + Vector((0, -0.05, 0.0)), 38)
    pin(1, p)
    return {}


def df_vibration():
    """Vibration: 128 Hz tuning fork on the base of the big toe (then medial malleolus, tibial tuberosity if not felt)."""
    ob, ao = supine("pelvis"); lights((0, -0.9, 0.8)); P = legpts(ob, ao)
    t1 = bone_world(ao, "toe1-1.R")
    p, n = surf(ob, t1, Vector((0, -0.2, 1)), back=0.12)
    side = n.cross(Vector((0, 1, 0)))
    tuning_fork(p, n, side)
    place_hand("right", "pinch", p + n * 0.05 + Vector((-0.010, 0, 0)), finger_dir=(0.85, 0.1, -0.5), palm_dir=(0.4, 0, -1),
               tip="index-finger-tip")
    camera(p + Vector((-0.38, -0.40, 0.22)), p + n * 0.06, 40)
    pin(1, p)
    return {}


def df_dressing():
    """Wound cleaning: sterile gauze held in sterile forceps (like a pen), saline, from the centre to the periphery,
    a new gauze each stroke."""
    ob, ao = supine("pelvis"); lights((0, -0.9, 0.8)); P = legpts(ob, ao)
    kn, an = P["knee"], P["ankle"]
    c, n = surf(ob, kn.lerp(an, 0.55), Vector((0, 0, 1)), back=0.12)
    skin_patch(ob, c, n, 0.022, 0.032, mat("woundfloor", srgb("#b8463f"), 0.6), 0.0008, name="wound")
    tip = c + Vector((0.004, 0.012, 0.006))
    tool_cyl(tip, tip + Vector((-0.10, -0.06, 0.10)), 0.0025, STEEL())
    tool_cyl(tip + Vector((0.004, 0, 0)), tip + Vector((-0.096, -0.06, 0.10)), 0.0025, STEEL())
    bpy.ops.mesh.primitive_uv_sphere_add(radius=0.011, location=tip + Vector((0, 0, 0.003)))
    g = bpy.context.object; g.scale = (1.1, 0.9, 0.55); g.data.materials.append(mat("gauze", srgb("#ffffff"), 0.9))
    place_hand("right", "pinch", tip + Vector((-0.065, -0.04, 0.065)), finger_dir=(0.5, 0.3, -0.8), palm_dir=(0.3, 0.6, -0.7),
               tip="index-finger-tip", sleeve_len=0.10)
    for ang in range(0, 360, 60):
        a = math.radians(ang); d = Vector((math.cos(a) * 0.012, math.sin(a) * 0.016, 0))
        over("arrow", c + d * 0.6 + n * 0.003, c + d * 2.4 + n * 0.003)
    camera(c + Vector((0.18, -0.32, 0.40)), c, 38)
    pin(1, c)
    return {}


SCENES = dict(df3d_inspection=df_inspection, df3d_sole=df_sole_points, df3d_monofilament=df_monofilament,
              df3d_vibration=df_vibration, df3d_dressing=df_dressing)
