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
    down = Vector((0, 0, 1))
    T = lambda x, y: surf(ob, Vector((x, y, COUCH_TOP + 0.1)), down, back=0.4)[0]
    yb = SUP_Y0 + 1.215
    nip = max((T(-0.095 + i * 0.004, yb + j * 0.004) for i in range(-7, 8) for j in range(-9, 10)), key=lambda p: p.z)
    nx, ny = nip.x, nip.y
    liq = T(nx + 0.042, ny - 0.045)
    place_hand("right", "flat", liq + Vector((0, 0, 0.004)), finger_dir=(0.10, 1, -0.25), palm_dir=(0, 0, -1), tip="middle-finger-tip")
    over("dash", T(nx, ny + 0.085), T(nx, ny - 0.075))
    over("dash", T(nx - 0.08, ny), T(nx + 0.075, ny))
    camera(nip + Vector((-0.04, -0.12, 0.50)), nip + Vector((0, 0.015, 0)), 40)
    pin(1, T(nx - 0.040, ny + 0.055)); pin(2, T(nx + 0.042, ny + 0.050)); pin(3, T(nx - 0.042, ny - 0.045))
    pin(4, T(nx + 0.042, ny - 0.042)); pin(5, T(nx - 0.085, ny + 0.080)); pin(6, nip)
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
    chest = surf(ob, Vector((sh.x + 0.05, sh.y - 0.09, COUCH_TOP + 0.1)), Vector((0, 0, 1)), back=0.4)[0]
    zm = (COUCH_TOP + chest.z) / 2
    X = Vector((1, 0, 0))
    cen = ray(ob, Vector((sh.x - 0.20, sh.y - 0.085, zm)), X)[0]
    apx = ray(ob, Vector((sh.x - 0.20, sh.y - 0.035, zm + 0.01)), X)[0]
    post = ray(ob, Vector((sh.x - 0.20, sh.y - 0.075, COUCH_TOP + 0.035)), X)[0]
    ant = surf(ob, Vector((sh.x + 0.015, sh.y - 0.075, COUCH_TOP + 0.1)), Vector((0, 0, 1)), back=0.4)[0]
    lat = ray(ob, Vector((sh.x - 0.08, sh.y - 0.16, zm)), (0, 1, 0))[0]
    camera(cen + Vector((-0.50, -0.38, 0.30)), cen + Vector((-0.01, 0.01, 0.0)), 38)
    for i, p in enumerate([ant, post, cen, apx, lat], 1):
        pin(i, p)
    return {}


SCENES = dict(breast3d_positions=breast_positions, breast3d_palpation=breast_palpation)
