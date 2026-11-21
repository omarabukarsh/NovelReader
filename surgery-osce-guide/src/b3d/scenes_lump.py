from mh import *


def forearm_setup(glow=False, dark=False):
    """Supine patient; lump on the front of the right forearm (patient's right = -X)."""
    def supinate(ao):
        for sd in ("R", "L"):
            el_, wr_ = bone_world(ao, f"lowerarm01.{sd}"), bone_world(ao, f"wrist.{sd}")
            rot(ao, f"lowerarm02.{sd}", (wr_ - el_).normalized(), 75 if sd == "R" else -75)
            rot(ao, f"wrist.{sd}", (wr_ - el_).normalized(), 30 if sd == "R" else -30)
    ob, ao = supine("trunk", extra=supinate); lights((-0.3, 0.1, 0.9), 0.35 if dark else 1.0)
    if dark:
        bpy.context.scene.world.node_tree.nodes["Background"].inputs[1].default_value = 0.02
    el = bone_world(ao, "lowerarm01.R"); wr = bone_world(ao, "wrist.R")
    c0 = el.lerp(wr, 0.45)
    top, n = surf(ob, c0, Vector((0, 0, 1)), back=0.15)
    r = 0.026
    bpy.ops.mesh.primitive_uv_sphere_add(radius=1, location=top - n * 0.006, segments=48, ring_count=24)
    lump = bpy.context.object; lump.scale = (r * 1.0, r * 1.2, r * 0.72)
    if glow:
        m = mat("lumpglow", srgb("#f6b48f"), 0.4, 0.3)
        b = m.node_tree.nodes["Principled BSDF"]; b.inputs["Emission Color"].default_value = (1.0, 0.55, 0.25, 1); b.inputs["Emission Strength"].default_value = 3.0
        lump.data.materials.append(m)
    else:
        lump.data.materials.append(SKIN())
    bpy.ops.object.shade_smooth()
    peak = top + n * (r * 0.72 - 0.006)
    return ob, ao, top, peak, n, r, el, wr


def lump_inspection():
    ob, ao, top, peak, n, r, el, wr = forearm_setup()
    camera(top + Vector((-0.25, -0.12, 0.30)), top, 40)
    pin(1, peak); pin(2, top + Vector((-r * 1.05, 0, 0.004))); pin(3, top + Vector((0, r * 1.25, 0.004)))
    over("dash", top + Vector((-0.026, -0.030, 0.005)), top + Vector((-0.026, 0.030, 0.005)), label="size")
    return {}


def lump_fluctuation():
    """Fluctuation (point map): 2 & 3 = index and middle fingers of one hand fixing the lump on opposite sides;
    1 = index finger of the other hand pressing the centre. Fixing fingers pushed apart = fluid. Repeat at 90 degrees."""
    ob, ao, top, peak, n, r, el, wr = forearm_setup()
    ax = (wr - el).normalized()
    a2, a3 = top + ax * (r * 1.15), top - ax * (r * 1.15)
    over("arrow", peak + n * 0.045, peak + n * 0.008)
    over("arrow", a2 + n * 0.004, a2 + ax * 0.022 + n * 0.004)
    over("arrow", a3 + n * 0.004, a3 - ax * 0.022 + n * 0.004)
    camera(top + Vector((-0.22, -0.05, 0.22)), top + Vector((0, 0, 0.01)), 36)
    pin(1, peak); pin(2, a2); pin(3, a3)
    return {}


def lump_transillumination():
    """Transillumination: dark room; pen torch applied to the side of the lump - a clear-fluid swelling glows."""
    ob, ao, top, peak, n, r, el, wr = forearm_setup(glow=True, dark=True)
    side = top + Vector((-r * 1.1, 0, 0.004))
    bpy.ops.mesh.primitive_cylinder_add(radius=0.009, depth=0.13, location=side + Vector((-0.07, 0, 0.03)))
    t = bpy.context.object; d = Vector((1, 0, -0.42)).normalized(); t.rotation_mode = "QUATERNION"; t.rotation_quaternion = d.to_track_quat("Z", "Y")
    t.data.materials.append(STEEL())
    bpy.ops.object.light_add(type="SPOT", location=side + Vector((-0.012, 0, 0.006)))
    L = bpy.context.object; L.data.energy = 3; L.data.spot_size = 0.6; L.rotation_euler = (-d).to_track_quat("-Z", "Y").to_euler()
    camera(top + Vector((-0.22, -0.22, 0.25)), top, 40)
    pin(1, peak); pin(2, side + Vector((-0.04, 0, 0.02)))
    return {}


def ulcer_setup():
    ob, ao = supine("pelvis"); lights((0, -0.8, 0.8))
    kn = bone_world(ao, "lowerleg01.R"); an = bone_world(ao, "foot.R")
    p0 = kn.lerp(an, 0.80)
    c, n = surf(ob, p0, Vector((1, 0, 0.55)), back=0.09)       # medial gaiter area (above the medial malleolus)
    # pigmented surrounding skin, sloping edge (pink), red granulating floor - each projected onto the skin
    skin_patch(ob, c, n, 0.038, 0.050, mat("pigment", srgb("#b88468"), 0.6), 0.0003, name="pigment")
    skin_patch(ob, c, n, 0.025, 0.032, mat("ulcerrim", srgb("#d89a86"), 0.5), 0.0007, name="edge")
    skin_patch(ob, c, n, 0.019, 0.025, mat("ulcerfloor", srgb("#b03a35"), 0.65), 0.0011, name="floor")
    return ob, ao, c, n, kn, an


def ulcer_inspection():
    ob, ao, c, n, kn, an = ulcer_setup()
    camera(c + n * 0.32 + Vector((0, -0.12, 0.10)), c, 40)
    pin(1, c + Vector((0, 0.0, 0.0)) + n * 0.002); pin(2, c + Vector((0, 0.031, 0)) + n * 0.003)
    pin(3, c + Vector((0, -0.055, 0)) + n * 0.002)
    pin(4, an + Vector((0.035, 0, -0.005)))
    return {}


def ulcer_palpation():
    """Ulcer palpation: gloved index finger on the edge and base (after washing hands and wearing gloves);
    temperature with the dorsum of the hand compared with the other limb; then distal pulses."""
    ob, ao, c, n, kn, an = ulcer_setup()
    edge = c + Vector((0, 0.031, 0)) + n * 0.002
    place_hand("right", "point", edge + n * 0.003, finger_dir=(0.6, -0.2, -0.75), palm_dir=-n)
    camera(c + n * 0.30 + Vector((-0.05, -0.20, 0.18)), c, 40)
    pin(1, edge)
    return {}


SCENES = dict(lump3d_inspection=lump_inspection, lump3d_fluctuation=lump_fluctuation, lump3d_transillum=lump_transillumination,
              ulcer3d_inspection=ulcer_inspection, ulcer3d_palpation=ulcer_palpation)
