from mh import *


def breast_body(name, loc, pose):
    """Female teaching manikin seated, skirt-gown from the waist; pose = sides | head | hips."""
    ob, ao = human(name=name, shape=female, material=MANIKIN())
    if pose == "sides":
        arms_down(ao, 32)
    elif pose == "head":      # hands behind the head
        for sd in ("L", "R"):
            sg = 1 if sd == "L" else -1
            aim(ao, f"upperarm01.{sd}", (0.88 * sg, 0.20, 0.42), f"lowerarm01.{sd}")
            aim(ao, f"lowerarm01.{sd}", (-0.70 * sg, 0.62, 0.30), f"wrist.{sd}")
    elif pose == "hips":      # hands pressed on the hips (contract pectoralis), leaning slightly forward
        for sd in ("L", "R"):
            sg = 1 if sd == "L" else -1
            aim(ao, f"upperarm01.{sd}", (0.55 * sg, 0.25, -0.80), f"lowerarm01.{sd}")
            aim(ao, f"lowerarm01.{sd}", (-0.35 * sg, -0.35, -0.87), f"wrist.{sd}")
        rot(ao, "spine03", (1, 0, 0), 8)
    sit(ao)
    ao.location.x += loc[0]; ao.location.y += loc[1]
    cloth(ob, ao, lambda x, y, z: 0.40 < z < 1.02 and not ARMS(x, y, z), name=name + "_skirt")
    bpy.context.view_layer.update()
    return ob, ao


def breast_points(ob, ao):
    """Nipple = most anterior point of each breast; quadrants around it."""
    P = {}
    for sd, sg in (("R", -1), ("L", 1)):
        best = None
        for dz in [i * 0.005 for i in range(-10, 11)]:
            for dx in [i * 0.005 for i in range(-6, 7)]:
                sp = bone_world(ao, "spine03")
                p, _ = surf(ob, Vector((ao.location.x + sg * 0.095 + dx, sp.y, sp.z + 0.22 + dz)), Vector((0, -1, 0)), back=0.3)
                if best is None or p.y < best.y:
                    best = p
        P["nip" + sd] = best
    return P


def breast_positions():
    """Inspection in 3 positions: arms by the sides - hands behind the head - hands pressed on the hips (leaning forward)."""
    floor(0); lights((0, -0.5, 1.0))
    for i, (nm, pose) in enumerate((("a", "sides"), ("b", "head"), ("c", "hips"))):
        breast_body(nm, ((i - 1) * 0.75, 0.0), pose)
        stool((i - 1) * 0.75, 0.12)
    camera((0.0, -3.2, 1.25), (0, 0, 1.0), 38)
    return {"size": (1500, 760)}


def breast_palpation():
    """Supine (or 45 deg), hand of the examined side behind the head; normal breast first; flat pads of the middle three
    fingers, small circles, systematic - all quadrants + axillary tail."""
    ob, ao = supine(None, shape=female, extra=lambda ao: (aim(ao, "upperarm01.R", (-0.70, 0.10, 0.70), "lowerarm01.R"),
                                                           aim(ao, "lowerarm01.R", (0.55, 0.45, 0.60), "wrist.R")))
    ob.data.materials[0] = MANIKIN()
    cloth(ob, ao, lambda x, y, z: 0.40 < z < 1.02 and not ARMS(x, y, z), name="skirt")
    lights((0, 0.2, 0.9))
    R = lambda x, z: rest_front_supine(x, z, female)
    best = None
    for dx in [i * 0.004 for i in range(-6, 7)]:
        for dz in [i * 0.004 for i in range(-8, 9)]:
            p = R(-0.095 + dx, 1.215 + dz)
            if best is None or p.z > best[0].z:
                best = (p, -0.095 + dx, 1.215 + dz)
    nip, nx, nz = best
    liq = R(nx + 0.040, nz - 0.040)
    place_hand("right", "flat", liq + Vector((0, 0, 0.004)), finger_dir=(0.10, 1, -0.25), palm_dir=(0, 0, -1), tip="middle-finger-tip")
    over("dash", R(nx, nz + 0.085), R(nx, nz - 0.075))
    over("dash", R(nx - 0.075, nz), R(nx + 0.075, nz))
    camera(nip + Vector((-0.04, -0.12, 0.50)), nip + Vector((0, 0.015, 0)), 40)
    pin(1, R(nx - 0.042, nz + 0.042)); pin(2, R(nx + 0.042, nz + 0.042)); pin(3, R(nx - 0.042, nz - 0.042))
    pin(4, R(nx + 0.042, nz - 0.042)); pin(5, R(nx - 0.085, nz + 0.075)); pin(6, nip)
    return {}


def breast_axilla():
    """Axillary node groups (map). Right arm abducted so the axilla is visible:
    1 anterior (pectoral) - behind the anterior axillary fold; 2 posterior (subscapular) - inside the posterior fold;
    3 central - against the chest wall; 4 apical - high at the apex; 5 lateral (humeral) - along the upper humerus."""
    ob, ao = supine(None, shape=female, extra=lambda ao: aim(ao, "upperarm01.R", (-0.98, 0.20, 0.0), "lowerarm01.R"))
    ob.data.materials[0] = MANIKIN()
    cloth(ob, ao, lambda x, y, z: 0.40 < z < 1.02 and not ARMS(x, y, z), name="skirt")
    lights((-0.4, 0.2, 0.9))
    sh = bone_world(ao, "upperarm01.R"); el = bone_world(ao, "lowerarm01.R")
    hollow = Vector((sh.x - 0.01, sh.y - 0.07, sh.z - 0.005))
    up = Vector((0, 0, 1))
    cen = ray(ob, Vector((sh.x - 0.035, sh.y - 0.075, sh.z + 0.25)), (0.25, 0, -1))[0]
    ant = surf(ob, Vector((sh.x + 0.025, sh.y - 0.05, sh.z)), up, back=0.3)[0]
    post = ray(ob, Vector((sh.x - 0.03, sh.y - 0.06, COUCH_TOP + 0.02)), (0.6, 0, 0.3))[0]
    apx = ray(ob, Vector((sh.x - 0.02, sh.y - 0.005, sh.z + 0.25)), (0.15, 0.1, -1))[0]
    lat = surf(ob, sh.lerp(el, 0.28) + Vector((0, -0.03, 0)), Vector((0, -0.4, 1)), back=0.2)[0]
    camera(cen + Vector((-0.30, -0.42, 0.42)), cen + Vector((0.02, 0.0, -0.01)), 40)
    for i, p in enumerate([ant, post, cen, apx, lat], 1):
        pin(i, p)
    return {}


SCENES = dict(breast3d_positions=breast_positions, breast3d_palpation=breast_palpation, breast3d_axilla=breast_axilla)
