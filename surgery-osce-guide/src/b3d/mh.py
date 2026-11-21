"""Blender helpers: MakeHuman CC0 body with its default rig, WebXR hand (MIT), materials, couch, camera, render.
Units: metres. Patient built standing (+Z up, facing -Y), then posed/rotated."""
import bpy, bmesh, json, math, os, mathutils
from mathutils import Vector, Euler, Matrix
from bpy_extras.object_utils import world_to_camera_view

A3D = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "assets3d")
S = 0.1  # MakeHuman decimetre -> metre


def reset():
    bpy.ops.wm.read_factory_settings(use_empty=True)
    sc = bpy.context.scene
    sc.render.engine = "CYCLES"
    sc.cycles.device = "CPU"
    sc.cycles.samples = 48
    sc.cycles.use_denoising = True
    try:
        sc.cycles.denoiser = "OPENIMAGEDENOISE"
    except Exception:
        pass
    sc.view_settings.view_transform = "AgX"
    sc.view_settings.look = "AgX - Medium High Contrast" if "AgX - Medium High Contrast" in [l.name for l in []] else "None"
    w = bpy.data.worlds.new("w"); sc.world = w; w.use_nodes = True
    bg = w.node_tree.nodes["Background"]; bg.inputs[0].default_value = (1, 1, 1, 1); bg.inputs[1].default_value = 0.18
    return sc


# ---------------------------------------------------------------- materials
def mat(name, rgb, rough=0.5, sss=0.0, sss_r=(1.0, 0.35, 0.2), metal=0.0, sheen=0.0):
    m = bpy.data.materials.get(name)
    if m:
        return m
    m = bpy.data.materials.new(name); m.use_nodes = True
    b = m.node_tree.nodes["Principled BSDF"]
    b.inputs["Base Color"].default_value = (*rgb, 1)
    b.inputs["Roughness"].default_value = rough
    b.inputs["Metallic"].default_value = metal
    if sss:
        b.inputs["Subsurface Weight"].default_value = sss
        b.inputs["Subsurface Radius"].default_value = sss_r
        b.inputs["Subsurface Scale"].default_value = 0.01
    if sheen:
        b.inputs["Sheen Weight"].default_value = sheen
    return m


def srgb(h):
    h = h.lstrip("#"); c = [int(h[i:i + 2], 16) / 255 for i in (0, 2, 4)]
    return tuple(((x + 0.055) / 1.055) ** 2.4 if x > 0.04045 else x / 12.92 for x in c)


SKIN = lambda: mat("skin", srgb("#d9a587"), 0.45, 0.25)
GLOVE = lambda: mat("glove", srgb("#8fc3ea"), 0.35, 0.05)
COAT = lambda: mat("coat", srgb("#f4f6f8"), 0.85, sheen=0.3)
GOWN = lambda: mat("gown", srgb("#8db7e0"), 0.9, sheen=0.4)
COUCH = lambda: mat("couch", srgb("#1d3557"), 0.55)
SHEET = lambda: mat("sheet", srgb("#eef2f6"), 0.9, sheen=0.3)
STEEL = lambda: mat("steel", srgb("#c8ced6"), 0.2, metal=1.0)
MANIKIN = lambda: mat("manikin", srgb("#e8bfa6"), 0.35, 0.15)


# ---------------------------------------------------------------- MakeHuman body + rig
def _read_obj(groups=("body",)):
    V, F, grp = [], [], None
    for line in open(os.path.join(A3D, "base.obj")):
        if line.startswith("v "):
            x, y, z = map(float, line.split()[1:4]); V.append((x * S, -z * S, y * S))   # Y-up -> Z-up, facing -Y
        elif line.startswith("g "):
            grp = line.split()[1]
        elif line.startswith("f ") and grp in groups:
            F.append([int(t.split("/")[0]) - 1 for t in line.split()[1:]])
    zmin = min(v[2] for v in V[:13380])
    V = [(x, y, z - zmin) for x, y, z in V]
    return V, F


def female(V):
    """Teaching-manikin breasts: two smooth forward bulges on the chest (standing coords, front = -Y)."""
    out = []
    for x, y, z in V:
        dy = 0.0
        for cx in (0.095, -0.095):
            g = math.exp(-((x - cx) ** 2 / (2 * 0.058 ** 2) + (z - 1.215) ** 2 / (2 * 0.050 ** 2)))
            if y < 0.0:
                dy -= 0.10 * g
        # slight downward sag of the lower pole
        out.append((x, y + dy, z - 0.012 * (dy / -0.055 if dy else 0)))
    return out


def human(name="patient", material=None, shape=None, eyes=True):
    V, F = _read_obj()
    if shape:
        V = shape(V)
    me = bpy.data.meshes.new(name); me.from_pydata(V, [], F); me.update()
    ob = bpy.data.objects.new(name, me); bpy.context.collection.objects.link(ob)
    # rig
    sk = json.load(open(os.path.join(A3D, "default.mhskel")))
    J = {k: sum((Vector(V[i]) for i in v), Vector()) / len(v) for k, v in sk["joints"].items()}
    arm = bpy.data.armatures.new(name + "_rig"); ao = bpy.data.objects.new(name + "_rig", arm)
    bpy.context.collection.objects.link(ao)
    bpy.context.view_layer.objects.active = ao; bpy.ops.object.mode_set(mode="EDIT")
    eb = {}
    for bn, d in sk["bones"].items():
        b = arm.edit_bones.new(bn); b.head = J[d["head"]]; b.tail = J[d["tail"]]
        if (b.tail - b.head).length < 1e-4:
            b.tail = b.head + Vector((0, 0, 0.01))
        eb[bn] = b
    for bn, d in sk["bones"].items():
        if d["parent"]:
            eb[bn].parent = eb[d["parent"]]
    bpy.ops.object.mode_set(mode="OBJECT")
    W = json.load(open(os.path.join(A3D, "default_weights.mhw")))["weights"]
    for bn, lst in W.items():
        vg = ob.vertex_groups.new(name=bn)
        for vi, w in lst:
            vg.add([vi], w, "REPLACE")
    # drop loose helper vertices
    bpy.context.view_layer.objects.active = ob; bpy.ops.object.mode_set(mode="EDIT")
    bpy.ops.mesh.select_all(action="DESELECT"); bpy.ops.mesh.select_loose(); bpy.ops.mesh.delete(type="VERT")
    bpy.ops.object.mode_set(mode="OBJECT")
    m = ob.modifiers.new("arm", "ARMATURE"); m.object = ao
    ob.parent = ao
    sub = ob.modifiers.new("sub", "SUBSURF"); sub.levels = 1; sub.render_levels = 2
    for p in me.polygons:
        p.use_smooth = True
    ob.data.materials.append(material or SKIN())
    ao.data.display_type = "STICK"
    if eyes:
        Ve, Fe = _read_obj(("helper-l-eye", "helper-r-eye"))
        me2 = bpy.data.meshes.new("eyes"); me2.from_pydata(Ve, [], Fe); me2.update()
        eo = bpy.data.objects.new("eyes", me2); bpy.context.collection.objects.link(eo)
        bpy.context.view_layer.objects.active = eo; bpy.ops.object.mode_set(mode="EDIT")
        bpy.ops.mesh.select_all(action="DESELECT"); bpy.ops.mesh.select_loose(); bpy.ops.mesh.delete(type="VERT")
        bpy.ops.object.mode_set(mode="OBJECT")
        vg = eo.vertex_groups.new(name="head"); vg.add(list(range(len(me2.vertices))), 1.0, "REPLACE")
        m3 = eo.modifiers.new("arm", "ARMATURE"); m3.object = ao; eo.parent = ao
        # colour: iris/pupil = vertices facing forward (-Y) beyond the eyeball centre
        col = me2.color_attributes.new("c", "FLOAT_COLOR", "POINT")
        import collections
        cen = {}
        for v in me2.vertices:
            k = "l" if v.co.x > 0 else "r"; cen.setdefault(k, []).append(v.co)
        cen = {k: sum(vs, Vector()) / len(vs) for k, vs in cen.items()}
        rad = {k: max((v - cen[k]).length for v in vs) for k, vs in
               {k2: [v.co for v in me2.vertices if (v.co.x > 0) == (k2 == "l")] for k2 in cen}.items()}
        for i, v in enumerate(me2.vertices):
            k = "l" if v.co.x > 0 else "r"; d = (v.co - cen[k]).normalized()
            a = math.degrees(math.acos(max(-1, min(1, -d.y))))
            c = (0.02, 0.015, 0.01) if a < 10 else (0.20, 0.10, 0.04) if a < 22 else (0.85, 0.84, 0.82)
            col.data[i].color = (*c, 1)
        em = bpy.data.materials.new("eye"); em.use_nodes = True
        nt = em.node_tree; ca = nt.nodes.new("ShaderNodeVertexColor"); ca.layer_name = "c"
        nt.links.new(ca.outputs["Color"], nt.nodes["Principled BSDF"].inputs["Base Color"])
        nt.nodes["Principled BSDF"].inputs["Roughness"].default_value = 0.15
        me2.materials.append(em)
        for p in me2.polygons:
            p.use_smooth = True
    return ob, ao


def pose(ao, rots):
    """rots: {bone: (x, y, z) degrees in bone-local XYZ euler}"""
    for bn, r in rots.items():
        pb = ao.pose.bones[bn]; pb.rotation_mode = "XYZ"; pb.rotation_euler = Euler([math.radians(a) for a in r], "XYZ")
    bpy.context.view_layer.update()


def rot(ao, bone, axis, deg):
    """Rotate a pose bone about a WORLD axis through its head (applied on top of current pose)."""
    pb = ao.pose.bones[bone]; bpy.context.view_layer.update()
    mw = ao.matrix_world; inv = mw.inverted()
    ax = (inv.to_3x3() @ Vector(axis)).normalized()
    head = pb.head.copy()
    R = Matrix.Translation(head) @ Matrix.Rotation(math.radians(deg), 4, ax) @ Matrix.Translation(-head)
    pb.matrix = R @ pb.matrix
    bpy.context.view_layer.update()


def bone_world(ao, bn, where="head"):
    pb = ao.pose.bones[bn]
    return ao.matrix_world @ (pb.head if where == "head" else pb.tail)


def surface_point(ob, p, direction):
    """Closest point on evaluated mesh along a ray from p (outside) in direction."""
    dg = bpy.context.evaluated_depsgraph_get(); eo = ob.evaluated_get(dg)
    mw = eo.matrix_world; inv = mw.inverted()
    ok, loc, nor, idx = eo.ray_cast(inv @ Vector(p), (inv.to_3x3() @ Vector(direction)).normalized())
    return (mw @ loc, (mw.to_3x3() @ nor).normalized()) if ok else (Vector(p), Vector((0, 0, 1)))


def gown(body_ob, ao, groups, thickness=0.006, name="gown", material=None, cut=None):
    """Clothing = copy of the posed body restricted to faces strongly weighted to `groups`, pushed outwards."""
    dg = bpy.context.evaluated_depsgraph_get()
    me = bpy.data.meshes.new_from_object(body_ob.evaluated_get(dg), depsgraph=dg)
    ob = bpy.data.objects.new(name, me); bpy.context.collection.objects.link(ob)
    ob.matrix_world = body_ob.matrix_world.copy()
    # transfer weights by name: evaluated mesh keeps vertex groups? use original groups via index map is lost after subsurf;
    # instead select by world-space test function `cut(world_point)`
    bm = bmesh.new(); bm.from_mesh(me)
    mw = ob.matrix_world
    kill = [f for f in bm.faces if not cut(mw @ f.calc_center_median())]
    bmesh.ops.delete(bm, geom=kill, context="FACES")
    bmesh.ops.delete(bm, geom=[v for v in bm.verts if not v.link_faces], context="VERTS")
    for _ in range(12):                                   # straighten the zig-zag hem
        bnd = [v for v in bm.verts if v.is_boundary]
        new = {}
        for v in bnd:
            nb = [e.other_vert(v) for e in v.link_edges if e.is_boundary]
            if len(nb) == 2:
                new[v] = (nb[0].co + nb[1].co) * 0.5 * 0.6 + v.co * 0.4
        for v, c in new.items():
            v.co = c
    bm.to_mesh(me); bm.free()
    so = ob.modifiers.new("solid", "SOLIDIFY"); so.thickness = thickness; so.offset = 1.0; so.use_rim = True
    ob.modifiers.new("sm", "SUBSURF").levels = 1
    d = ob.modifiers.new("disp", "DISPLACE"); d.strength = 0.004
    ob.data.materials.clear(); ob.data.materials.append(material or GOWN())
    for p in me.polygons:
        p.use_smooth = True
    return ob


# ---------------------------------------------------------------- environment
def box(name, loc, size, material, bevel=0.02):
    bpy.ops.mesh.primitive_cube_add(location=loc); ob = bpy.context.object; ob.name = name
    ob.scale = (size[0] / 2, size[1] / 2, size[2] / 2); bpy.ops.object.transform_apply(scale=True)
    bv = ob.modifiers.new("bev", "BEVEL"); bv.width = bevel; bv.segments = 4
    ob.data.materials.append(material); bpy.ops.object.shade_smooth()
    return ob


def couch(x0, x1, y0, y1, top):
    box("couch", ((x0 + x1) / 2, (y0 + y1) / 2, top - 0.05), (x1 - x0, y1 - y0, 0.10), COUCH(), 0.03)
    box("couch_base", ((x0 + x1) / 2, (y0 + y1) / 2, top - 0.40), (x1 - x0 - 0.2, y1 - y0 - 0.2, 0.60), mat("frame", srgb("#c9cfd6"), 0.4, metal=0.3), 0.02)


def floor(z=0.0):
    bpy.ops.mesh.primitive_plane_add(size=30, location=(0, 0, z)); ob = bpy.context.object
    ob.data.materials.append(mat("floor", srgb("#f1f3f5"), 0.8)); ob.is_shadow_catcher = True
    return ob


def lights(target=(0, 0, 1), strength=1.0):
    for loc, e, sz in (((-2.0, -2.5, 3.5), 900, 2.5), ((2.5, -1.0, 2.0), 300, 2.0), ((0.5, 3.0, 2.5), 350, 2.0)):
        bpy.ops.object.light_add(type="AREA", location=loc); L = bpy.context.object
        L.data.energy = e * strength; L.data.size = sz
        d = Vector(target) - Vector(loc); L.rotation_euler = d.to_track_quat("-Z", "Y").to_euler()


def camera(loc, target, lens=45):
    bpy.ops.object.camera_add(location=loc); c = bpy.context.object
    d = Vector(target) - Vector(loc); c.rotation_euler = d.to_track_quat("-Z", "Y").to_euler()
    c.data.lens = lens; c.data.clip_start = 0.005; bpy.context.scene.camera = c
    return c


def project(p):
    bpy.context.view_layer.update()
    sc = bpy.context.scene; co = world_to_camera_view(sc, sc.camera, Vector(p))
    return [round(co.x * 100, 2), round((1 - co.y) * 100, 2)]


def render(path, w=1200, h=900, samples=None):
    sc = bpy.context.scene; sc.render.resolution_x = w; sc.render.resolution_y = h; sc.render.resolution_percentage = 100
    if samples:
        sc.cycles.samples = samples
    sc.render.filepath = path; sc.render.image_settings.file_format = "PNG"
    bpy.ops.render.render(write_still=True)


# ---------------------------------------------------------------- examiner hand (WebXR generic hand, MIT)
def hand(side="right", loc=(0, 0, 1), rot=(0, 0, 0), curls=None, scale=1.0, glove=True, sleeve=True):
    before = set(bpy.data.objects)
    bpy.ops.import_scene.gltf(filepath=os.path.join(A3D, f"hand_{side}.glb"))
    new = [o for o in bpy.data.objects if o not in before]
    arm = [o for o in new if o.type == "ARMATURE"][0]
    root = arm
    while root.parent:
        root = root.parent
    meshes = [o for o in new if o.type == "MESH"]
    for m in meshes:
        m.data.materials.clear(); m.data.materials.append(GLOVE() if glove else SKIN())
        for p in m.data.polygons:
            p.use_smooth = True
        sub = m.modifiers.new("sub", "SUBSURF"); sub.levels = 1; sub.render_levels = 1
        bpy.context.view_layer.objects.active = m
        try:
            bpy.ops.object.modifier_move_to_index(modifier="sub", index=len(m.modifiers) - 1)
        except Exception:
            pass
    root.location = loc; root.rotation_mode = "XYZ"; root.rotation_euler = Euler([math.radians(a) for a in rot], "XYZ")
    root.scale = (scale,) * 3
    if curls:
        for bn, r in curls.items():
            if bn in arm.pose.bones:
                pb = arm.pose.bones[bn]; pb.rotation_mode = "XYZ"
                pb.rotation_euler = Euler([math.radians(a) for a in r], "XYZ")
    bpy.context.view_layer.update()
    return arm, meshes, root


# ---------------------------------------------------------------- examiner hand placement
FINGERS = ["index", "middle", "ring", "pinky"]
CURL = {  # (mcp, pip, dip) flexion degrees
    "flat": {f: (8, 8, 4) for f in FINGERS},
    "pulse": {"index": (22, 22, 8), "middle": (20, 22, 8), "ring": (30, 35, 15), "pinky": (45, 55, 25)},
    "tips": {f: (40, 45, 20) for f in FINGERS},
    "cup": {f: (35, 30, 15) for f in FINGERS},
    "point": {"index": (5, 5, 0), "middle": (70, 90, 40), "ring": (75, 90, 40), "pinky": (75, 90, 40)},
    "fist": {f: (85, 100, 60) for f in FINGERS},
    "tap": {"index": (20, 30, 10), "middle": (35, 55, 25), "ring": (70, 85, 40), "pinky": (75, 90, 40)},
    "pinch": {"index": (35, 40, 15), "middle": (60, 70, 30), "ring": (70, 80, 40), "pinky": (75, 85, 40)},
}
THUMB = {"tap": (30, 30, 15), "flat": (10, 5, 5), "pulse": (15, 10, 10), "tips": (20, 15, 10), "cup": (10, 10, 5), "point": (40, 40, 20),
         "fist": (40, 50, 30), "pinch": (25, 30, 25), "wrap": (35, 20, 10)}


def place_hand(side, curl, target, finger_dir, palm_dir, tip="index-finger-tip", glove=True, sleeve=True,
               sleeve_len=0.20, thumb=None, spread=0.0, extra_rot=None):
    """Glove hand whose `tip` touches `target`; fingers point along finger_dir; palm faces palm_dir."""
    for o in [o for o in bpy.data.objects if o.name.startswith("Icosphere")]:
        bpy.data.objects.remove(o)
    before = set(bpy.data.objects)
    bpy.ops.import_scene.gltf(filepath=os.path.join(A3D, f"hand_{side}.glb"))
    new = [o for o in bpy.data.objects if o not in before]
    for o in [o for o in new if o.name.startswith("Icosphere")]:
        bpy.data.objects.remove(o); new.remove(o)
    arm = [o for o in new if o.type == "ARMATURE"][0]
    meshes = [o for o in new if o.type == "MESH"]
    for m in meshes:
        m.data.materials.clear(); m.data.materials.append(GLOVE() if glove else SKIN())
        for p in m.data.polygons:
            p.use_smooth = True
        s2 = m.modifiers.new("sub", "SUBSURF"); s2.levels = 1; s2.render_levels = 2
    bpy.context.view_layer.objects.active = arm
    bpy.ops.object.mode_set(mode="EDIT")
    eb = arm.data.edit_bones
    for ch in (["thumb-metacarpal", "thumb-phalanx-proximal", "thumb-phalanx-distal", "thumb-tip"],) + tuple(
            [f"{f}-finger-metacarpal", f"{f}-finger-phalanx-proximal", f"{f}-finger-phalanx-intermediate",
             f"{f}-finger-phalanx-distal", f"{f}-finger-tip"] for f in FINGERS):
        eb[ch[0]].parent = eb["wrist"]
        for a, b in zip(ch, ch[1:]):
            eb[b].parent = eb[a]; eb[b].use_connect = False
    bpy.ops.object.mode_set(mode="OBJECT")
    bpy.context.view_layer.update()
    tsign = 1 if (arm.matrix_world @ arm.pose.bones["thumb-metacarpal"].head).y > 0 else -1
    # local frame: fingers -Z, thumb +Y*tsign, palm normal -X (right) ; flexion axis = +Y for the right hand
    m = 1 if side == "right" else -1   # left model = right model mirrored in X (palm at +X)
    flex_axis = Vector((0, m, 0))      # bends fingers toward the palm
    c = CURL[curl] if isinstance(curl, str) else curl
    for f in FINGERS:
        sp = {"index": 1, "middle": 0, "ring": -1, "pinky": -2}[f] * spread
        if sp:
            rot(arm, f"{f}-finger-phalanx-proximal", (1, 0, 0), sp)
        for bn, ang in zip(("phalanx-proximal", "phalanx-intermediate", "phalanx-distal"), c[f]):
            rot(arm, f"{f}-finger-{bn}", flex_axis, ang)
    th = thumb or THUMB.get(curl if isinstance(curl, str) else "flat", (10, 5, 5))
    for bn, ang in zip(("thumb-metacarpal", "thumb-phalanx-proximal", "thumb-phalanx-distal"), th):
        rot(arm, bn, Vector((-1, 0, 0)), ang * 0.6)
        rot(arm, bn, flex_axis, ang * 0.5)
    bpy.context.view_layer.update()
    # glove cuff + coat sleeve (in hand-local space, parented)
    extras = []
    bpy.ops.mesh.primitive_cylinder_add(radius=0.034, depth=0.10, location=(0.02, 0, 0.11), vertices=32)
    cuff = bpy.context.object; cuff.data.materials.append(GLOVE() if glove else SKIN()); bpy.ops.object.shade_smooth()
    bv = cuff.modifiers.new("b", "BEVEL"); bv.width = 0.01; bv.segments = 3; extras.append(cuff)
    if sleeve:
        sleeve_len = min(sleeve_len, 0.20)
        bpy.ops.mesh.primitive_cylinder_add(radius=0.044, depth=sleeve_len, location=(0.02, 0, 0.15 + sleeve_len / 2), vertices=40)
        sl = bpy.context.object; sl.data.materials.append(COAT()); bpy.ops.object.shade_smooth()
        bv = sl.modifiers.new("b", "BEVEL"); bv.width = 0.015; bv.segments = 4
        sl.scale = (1.0, 1.08, 1.0); extras.append(sl)
    for e in extras:
        e.parent = arm
    tip_local = arm.matrix_world.inverted() @ (arm.matrix_world @ arm.pose.bones[tip].head)
    # rotation local->world
    fw = Vector(finger_dir).normalized(); pw = Vector(palm_dir).normalized()
    pw = (pw - fw * pw.dot(fw)).normalized()
    dorsal_w = -pw
    # proper rotation: local X = dorsal (right model) / palm (left model), local Z = -finger, local Y = Z x X
    lx = dorsal_w * m
    ly = (-fw).cross(lx).normalized()
    R = Matrix((lx, ly, -fw)).transposed()
    if extra_rot:
        R = Matrix.Rotation(math.radians(extra_rot[1]), 3, Vector(extra_rot[0])) @ R
    arm.matrix_world = Matrix.Translation(Vector(target) - R @ tip_local) @ R.to_4x4()
    bpy.context.view_layer.update()
    return arm


def surf(ob, p, out_dir, back=None):
    """Point on the skin: cast a ray from p + out_dir*back toward -out_dir."""
    d = Vector(out_dir).normalized()
    if back is None:
        back = 0.35 if d.z > 0.6 else 0.09
    loc, n = surface_point(ob, Vector(p) + d * back, -d)
    return loc, n


# ---------------------------------------------------------------- standard patient set-ups
COUCH_TOP = 0.74


def arms_down(ao, deg=36):
    for sd, sg in (("L", 1), ("R", -1)):
        rot(ao, f"lowerarm01.{sd}", (1, 0, 0), 52)
        rot(ao, f"upperarm01.{sd}", (0, 1, 0), deg * sg)
        rot(ao, f"wrist.{sd}", (0, 0, 1), 0)


def relaxed_feet(ao, plantar=18, ext=12):
    for sd, sg in (("L", 1), ("R", -1)):
        rot(ao, f"upperleg01.{sd}", (0, 0, 1), ext * sg)
        rot(ao, f"foot.{sd}", (1, 0, 0), plantar)


def supine(gown_cut="pelvis", extra=None, shape=None, top=None):
    """Patient lying on the couch, head toward +Y, feet toward -Y, patient's right = -X."""
    ob, ao = human(shape=shape); arms_down(ao); relaxed_feet(ao)
    if gown_cut == "trunk":
        cloth(ob, ao, FULLGOWN)
    elif gown_cut == "chest":     # abdomen exposed: gown above the nipples, sheet from the pubis down
        cloth(ob, ao, lambda x, y, z: 1.21 < z < 1.43 and not ARMS(x, y, z))
        cloth(ob, ao, lambda x, y, z: 0.50 < z < 0.865 and not ARMS(x, y, z), name="sheet", material=SHEET(), thickness=0.012)
    elif gown_cut == "pelvis":
        cloth(ob, ao, SHORTS); cloth(ob, ao, BRIEF, name="drape", material=SHEET(), thickness=0.012)
    elif gown_cut == "brief":
        cloth(ob, ao, BRIEF, name="drape", material=SHEET(), thickness=0.012)
    elif callable(gown_cut):
        gown_cut(ob, ao)
    if extra:
        extra(ao)
    Y0 = -1.12
    ao.rotation_euler = (math.radians(-90), 0, 0); ao.location = (0, Y0, COUCH_TOP + 0.105)
    bpy.context.view_layer.update()
    couch(-0.42, 0.42, -1.25, 0.70, COUCH_TOP)
    floor(0)
    return ob, ao


def pin(name, p):
    MARKS[str(name)] = Vector(p).copy()


def over(kind, *pts, **kw):
    """2-D overlay drawn later by code: kind = arrow | line | dash | arc (centre, p1, p2) | label."""
    OVER.append(dict(kind=kind, pts=[Vector(p).copy() for p in pts], **kw))


MARKS, OVER = {}, []


# ---------------------------------------------------------------- pose by aiming bones; clothing that follows the pose
def aim(ao, bone, direction, end=None):
    """Rotate `bone` (about its head) so that head->end (end = head of child bone `end`, else own tail) points along direction."""
    bpy.context.view_layer.update()
    h = bone_world(ao, bone)
    e = bone_world(ao, end) if end else bone_world(ao, bone, "tail")
    cur = (e - h).normalized(); tgt = Vector(direction).normalized()
    ax = cur.cross(tgt)
    if ax.length < 1e-6:
        return
    ang = math.degrees(cur.angle(tgt))
    rot(ao, bone, ax.normalized(), ang)


REST = {}


def cloth(body_ob, ao, cut, name="gown", material=None, thickness=0.006, push=0.004):
    """Copy of the body restricted to faces whose REST-pose centre satisfies cut(x, y, z) (standing coords:
    z = height, front = -y, patient's left = +x); follows the armature, pushed slightly outwards."""
    if "V" not in REST:
        REST["V"] = _read_obj()[0]
    me = body_ob.data.copy(); ob = bpy.data.objects.new(name, me); bpy.context.collection.objects.link(ob)
    ob.parent = ao
    bm = bmesh.new(); bm.from_mesh(me)
    kill = [f for f in bm.faces if not cut(*f.calc_center_median())]
    bmesh.ops.delete(bm, geom=kill, context="FACES")
    bmesh.ops.delete(bm, geom=[v for v in bm.verts if not v.link_faces], context="VERTS")
    for _ in range(12):
        new = {}
        for v in [v for v in bm.verts if v.is_boundary]:
            nb = [e.other_vert(v) for e in v.link_edges if e.is_boundary]
            if len(nb) == 2:
                new[v] = (nb[0].co + nb[1].co) * 0.3 + v.co * 0.4
        for v, c in new.items():
            v.co = c
    bm.to_mesh(me); bm.free()
    for m in list(ob.modifiers):
        ob.modifiers.remove(m)
    a = ob.modifiers.new("arm", "ARMATURE"); a.object = ao
    d = ob.modifiers.new("push", "DISPLACE"); d.strength = push; d.mid_level = 0
    so = ob.modifiers.new("solid", "SOLIDIFY"); so.thickness = thickness; so.offset = 1.0
    sb = ob.modifiers.new("sub", "SUBSURF"); sb.levels = 1; sb.render_levels = 2
    ob.data.materials.clear(); ob.data.materials.append(material or GOWN())
    return ob


ARMS = lambda x, y, z: abs(x) > 0.19 and z > 0.55
SHORTS = lambda x, y, z: 0.95 < z < 1.43 and not ARMS(x, y, z)
BRIEF = lambda x, y, z: 0.70 < z <= 0.97 and abs(x) < 0.075
FULLGOWN = lambda x, y, z: 0.62 < z < 1.43 and not ARMS(x, y, z)
SKIRT = lambda x, y, z: 0.45 < z < 1.02 and not ARMS(x, y, z)
SHEET_HIP = lambda x, y, z: 0.55 < z < 0.92 and not ARMS(x, y, z)


def sit(ao, seat_h=0.48):
    """Sitting pose: hips & knees flexed 90 degrees; returns nothing, moves armature so buttocks rest at seat_h."""
    for sd in ("L", "R"):
        aim(ao, f"upperleg01.{sd}", (0, -1, -0.05), f"lowerleg01.{sd}")
        aim(ao, f"lowerleg01.{sd}", (0, 0.05, -1), f"foot.{sd}")
        rot(ao, f"foot.{sd}", (1, 0, 0), 0)
    bpy.context.view_layer.update()
    hip = bone_world(ao, "upperleg01.L")
    ao.location.z += seat_h + 0.06 - hip.z
    bpy.context.view_layer.update()


def stool(x=0, y=0.05, h=0.48):
    box("stool", (x, y, h - 0.03), (0.46, 0.42, 0.06), mat("stoolm", srgb("#2b3f5c"), 0.5), 0.02)
    bpy.ops.mesh.primitive_cylinder_add(radius=0.03, depth=h - 0.06, location=(x, y, (h - 0.06) / 2))
    bpy.context.object.data.materials.append(mat("frame", srgb("#c9cfd6"), 0.4, metal=0.3))


SUP_Y0 = -1.12


def front(ob, x, zrest, tilt=(0, 0, 1)):
    """Skin point of the SUPINE patient's front at rest-pose height zrest (patient's right = -x)."""
    return surf(ob, Vector((x, SUP_Y0 + zrest, COUCH_TOP + 0.12)), Vector(tilt), back=0.35)[0]


def skin_patch(ob, centre, normal, rx, ry, material, offset=0.0006, res=28, name="patch"):
    """Elliptical decal (dense grid) projected onto the skin surface around `centre`."""
    q = Vector(normal).to_track_quat("Z", "Y")
    bm = bmesh.new()
    rings, segs = 10, 72                       # polar grid: smooth round edge
    centre_v = bm.verts.new((0, 0, 0)); prev = None
    rows = []
    for i in range(1, rings + 1):
        rr = i / rings
        rows.append([bm.verts.new((rx * rr * math.cos(2 * math.pi * k / segs), ry * rr * math.sin(2 * math.pi * k / segs), 0)) for k in range(segs)])
    for k in range(segs):
        bm.faces.new((centre_v, rows[0][k], rows[0][(k + 1) % segs]))
    for a, b in zip(rows, rows[1:]):
        for k in range(segs):
            bm.faces.new((a[k], b[k], b[(k + 1) % segs], a[(k + 1) % segs]))
    me = bpy.data.meshes.new(name); bm.to_mesh(me); bm.free()
    o = bpy.data.objects.new(name, me); bpy.context.collection.objects.link(o)
    o.location = Vector(centre) + Vector(normal) * 0.02; o.rotation_mode = "QUATERNION"; o.rotation_quaternion = q
    sw = o.modifiers.new("sw", "SHRINKWRAP"); sw.target = ob; sw.wrap_method = "PROJECT"
    sw.use_negative_direction = True; sw.use_positive_direction = True; sw.use_project_z = True; sw.offset = offset
    sw2 = o.modifiers.new("sw2", "SHRINKWRAP"); sw2.target = ob; sw2.wrap_method = "NEAREST_SURFACEPOINT"
    sw2.wrap_mode = "OUTSIDE_SURFACE"; sw2.offset = offset
    o.data.materials.append(material)
    for p in me.polygons:
        p.use_smooth = True
    return o


def ray(ob, a, d):
    """First hit of a ray from point a in direction d."""
    return surface_point(ob, Vector(a), Vector(d))


_REST_FEMALE = {}


def rest_front_supine(x, z, shape=None):
    """World point on the front skin of the SUPINE patient for rest-pose (x, z), from the rest mesh (unaffected by arm pose)."""
    key = id(shape)
    if key not in _REST_FEMALE:
        V = _read_obj()[0]
        if shape:
            V = shape(V)
        _REST_FEMALE[key] = [v for v in V[:13380] if v[1] < 0]
    pts = _REST_FEMALE[key]
    best = min(pts, key=lambda v: (v[0] - x) ** 2 + (v[2] - z) ** 2 + 0.02 * max(0.0, v[1] + 0.2))
    near = [v for v in pts if (v[0] - x) ** 2 + (v[2] - z) ** 2 < 0.012 ** 2] or [best]
    y = min(v[1] for v in near)
    return Vector((x, SUP_Y0 + z, COUCH_TOP + 0.105 - y + 0.002))
