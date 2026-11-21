"""Measured neck / head landmarks of the current (posed) body."""
from mh import *


def neck_landmarks(ob, ao):
    n1 = bone_world(ao, "neck01"); hd = bone_world(ao, "head")
    prof = []
    z = n1.z - 0.12
    while z < n1.z + 0.10:
        p, _ = surf(ob, Vector((0, 0, z)), Vector((0, -1, 0)), back=0.3); prof.append((z, p.y)); z += 0.003
    zdeep, neck_y = max(((z, y) for z, y in prof if n1.z - 0.06 < z < n1.z + 0.05), key=lambda t: t[1])  # deepest neck front
    chin_z = next(z for z, y in prof if z > zdeep and y < neck_y - 0.030)                    # under-chin step
    notch_z = max(z for z, y in prof if z < chin_z - 0.02 and y < neck_y - 0.010)
    L = {"chin_z": chin_z, "notch_z": notch_z}
    f = Vector((0, -1, 0)); h = chin_z - notch_z
    S = lambda x, z, d=f, back=0.3: surf(ob, Vector((x, 0, z)), d, back=back)[0]
    L["notch"] = S(0, notch_z + 0.004)
    L["isthmus"] = S(0, notch_z + 0.30 * h)
    L["cartilage"] = S(0, notch_z + 0.70 * h)
    L["thyroglossal"] = S(0, notch_z + 0.88 * h)
    L["kocher"] = S(0.0, notch_z + 0.22 * h)
    L["lobeR"] = S(-0.024, notch_z + 0.40 * h, Vector((-0.45, -1, 0)))
    L["lobeL"] = S(0.024, notch_z + 0.40 * h, Vector((0.45, -1, 0)))
    L["veins"] = S(-0.055, notch_z - 0.05)
    # ear: most lateral point of the head side around ear height
    best = None
    for dz in [i * 0.004 for i in range(0, 25)]:
        for dy in [i * 0.005 for i in range(-8, 9)]:
            p, _ = surf(ob, Vector((-0.02, hd.y + dy, hd.z + dz)), Vector((-1, 0, 0)), back=0.2)
            if best is None or p.x < best.x:
                best = p
    ear = best; L["ear"] = ear
    L["preaur"] = surf(ob, ear + Vector((0.014, -0.022, -0.036)), Vector((-1, -0.25, 0)), back=0.06)[0]
    L["postaur"] = surf(ob, ear + Vector((0.016, 0.022, -0.040)), Vector((-1, 0.35, 0)), back=0.06)[0]
    L["occip"] = surf(ob, Vector((-0.032, ear.y + 0.060, ear.z - 0.030)), Vector((-0.2, 1, 0)), back=0.10)[0]
    ang = Vector((ear.x + 0.018, ear.y - 0.018, chin_z + 0.005))
    L["angle"] = surf(ob, ang, Vector((-1, -0.2, -0.3)), back=0.1)[0]
    L["tonsil"] = surf(ob, ang + Vector((0.005, 0.0, -0.022)), Vector((-1, -0.3, 0)), back=0.1)[0]
    L["submand"] = surf(ob, Vector((-0.040, (ear.y + L["notch"].y) / 2 - 0.035, chin_z - 0.004)), Vector((-0.3, -0.3, -1)), back=0.12)[0]
    L["submental"] = surf(ob, Vector((0.0, L["notch"].y - 0.06, chin_z - 0.006)), Vector((0, -0.2, -1)), back=0.12)[0]
    mid = notch_z + 0.55 * h
    L["ant_cerv"] = surf(ob, Vector((-0.045, L["isthmus"].y + 0.035, mid)), Vector((-1, -0.7, 0)), back=0.08)[0]
    L["post_cerv"] = surf(ob, Vector((-0.050, ear.y + 0.03, mid - 0.005)), Vector((-1, 0.1, 0)), back=0.08)[0]
    L["supraclav"] = surf(ob, Vector((-0.075, L["notch"].y + 0.035, notch_z + 0.005)), Vector((-0.2, -0.3, 1)), back=0.12)[0]
    L["virchow"] = surf(ob, Vector((0.075, L["notch"].y + 0.035, notch_z + 0.005)), Vector((0.2, -0.3, 1)), back=0.12)[0]
    return L
