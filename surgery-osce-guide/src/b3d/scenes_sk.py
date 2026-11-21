from mh import *


def arc_wire(c, r, a0, a1, normal_axis, radius, material, plane=("x", "z")):
    """Curved needle: arc of a circle (centre c, radius r) in the X-Z plane, angles in degrees."""
    cu = bpy.data.curves.new("arc", "CURVE"); cu.dimensions = "3D"; cu.bevel_depth = radius; cu.bevel_resolution = 3
    sp = cu.splines.new("POLY"); n = 24; sp.points.add(n - 1)
    for i in range(n):
        a = math.radians(a0 + (a1 - a0) * i / (n - 1))
        sp.points[i].co = (c[0], c[1] + r * math.cos(a), c[2] + r * math.sin(a), 1)
    o = bpy.data.objects.new("arc", cu); bpy.context.collection.objects.link(o); o.data.materials.append(material)
    return o


def suture_pad():
    """Simple interrupted sutures on a skin pad: equal bites 3-5 mm from the edge, 5-10 mm apart, knots to one side;
    needle enters the skin at 90 degrees and follows its curve."""
    floor(0); lights((0, 0, 0.1))
    box("table", (0, 0, 0.04), (0.5, 0.35, 0.08), mat("drape", srgb("#4f8f7a"), 0.8), 0.01)
    pad = box("pad", (0, 0, 0.095), (0.16, 0.10, 0.03), SKIN(), 0.008)
    top = 0.11
    box("wound", (0, 0, top - 0.002), (0.11, 0.0035, 0.006), mat("cut", srgb("#8e2f2a"), 0.6), 0.001)
    thread = mat("thread", srgb("#1f3a8a"), 0.4)
    for i, x in enumerate((-0.032, -0.011, 0.010)):
        # bite: enters 4 mm from one edge, exits 4 mm from the other; knot sits beside the wound (on the +y side)
        tool = bpy.data.curves.new("st", "CURVE"); tool.dimensions = "3D"; tool.bevel_depth = 0.0006
        sp = tool.splines.new("POLY"); pts = [(x, -0.0045, top + 0.0003), (x, -0.002, top + 0.0012), (x, 0.002, top + 0.0012), (x, 0.0045, top + 0.0003)]
        sp.points.add(len(pts) - 1)
        for k, q in enumerate(pts):
            sp.points[k].co = (*q, 1)
        o = bpy.data.objects.new("st", tool); bpy.context.collection.objects.link(o); o.data.materials.append(thread)
        bpy.ops.mesh.primitive_uv_sphere_add(radius=0.0016, location=(x, 0.0052, top + 0.0012)); bpy.context.object.data.materials.append(thread)
        for sg in (1, -1):
            t = bpy.data.curves.new("tail", "CURVE"); t.dimensions = "3D"; t.bevel_depth = 0.0005
            s2 = t.splines.new("POLY"); s2.points.add(1)
            s2.points[0].co = (x, 0.0052, top + 0.0012, 1); s2.points[1].co = (x + 0.004 * sg, 0.0085, top + 0.0012, 1)
            o2 = bpy.data.objects.new("tail", t); bpy.context.collection.objects.link(o2); o2.data.materials.append(thread)
    # needle entering at 90 deg, 4 mm from the edge, for the next stitch
    xn = 0.031
    # needle: 1/2-circle; tip has just entered the skin at 90 deg 4 mm from the near edge, body above the skin
    arc_wire((xn, 0.0, top), 0.0045, 55, 184, None, 0.00045, STEEL())
    tcu = bpy.data.curves.new("thr", "CURVE"); tcu.dimensions = "3D"; tcu.bevel_depth = 0.0004
    sp = tcu.splines.new("POLY"); a = math.radians(55); p0 = (xn, 0.0045 * math.cos(a), top + 0.0045 * math.sin(a))
    sp.points.add(2); sp.points[0].co = (*p0, 1); sp.points[1].co = (xn + 0.006, p0[1] + 0.006, p0[2] + 0.006, 1); sp.points[2].co = (xn + 0.02, p0[1] + 0.012, p0[2] + 0.004, 1)
    o = bpy.data.objects.new("thr", tcu); bpy.context.collection.objects.link(o); o.data.materials.append(mat("thread", srgb("#1f3a8a"), 0.4))
    camera((0.035, -0.055, top + 0.075), (-0.004, 0.002, top), 40)
    pin(1, (-0.032, -0.0045, top)); pin(2, (-0.032, 0.0052, top + 0.0015)); pin(3, (-0.0215, -0.012, top)); pin(4, (xn, -0.0045, top))
    over("dash", Vector((-0.032, -0.012, top)), Vector((-0.011, -0.012, top)))
    return {"size": (1200, 860)}


SCENES = dict(sk3d_suture=suture_pad)
