"""usage: python run.py OUTDIR [--preview] scene1 scene2 ...   (scenes from scenes_*.py)"""
import sys, os, json, time, importlib
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import mh
from mh import *

SCENES = {}
for m in ("scenes_pvd", "scenes_thy", "scenes_git", "scenes_uro", "scenes_lump", "scenes_breast", "scenes_df", "scenes_sk"):
    try:
        SCENES.update(importlib.import_module(m).SCENES)
    except ModuleNotFoundError:
        pass

out = sys.argv[1]; prev = "--preview" in sys.argv
names = [a for a in sys.argv[2:] if not a.startswith("--")] or list(SCENES)
os.makedirs(out, exist_ok=True)
for n in names:
    t = time.time(); reset(); mh.MARKS.clear(); mh.OVER.clear()
    meta = SCENES[n]() or {}
    w, h = meta.get("size", (1200, 860))
    if prev:
        w, h = w // 2, h // 2
    sc = bpy.context.scene; sc.render.resolution_x = w; sc.render.resolution_y = h; sc.render.resolution_percentage = 100
    marks = {k: project(v) for k, v in mh.MARKS.items()}
    over = []
    for o in mh.OVER:
        o = dict(o); o["pts"] = [project(p) for p in o["pts"]]; over.append(o)
    if "--debug" in sys.argv and mh.MARKS:
        c0 = list(mh.MARKS.values())[0]; cam = sc.camera
        keep = (cam.location.copy(), cam.rotation_euler.copy())
        for tag, off in (("top", Vector((0.0, -0.02, 0.55))), ("side", Vector((-0.55, 0.0, 0.05))), ("end", Vector((0.0, -0.55, 0.12)))):
            camera(c0 + off, c0, 40); render(os.path.join(out, f"{n}__{tag}.png"), 420, 320, 8)
        sc.camera = cam; cam.location, cam.rotation_euler = keep
    sc.render.film_transparent = True
    render(os.path.join(out, n + ".png"), w, h, 16 if prev else 40)
    from PIL import Image
    im = Image.open(os.path.join(out, n + ".png")).convert("RGBA"); bg = Image.new("RGBA", im.size, (255, 255, 255, 255))
    Image.alpha_composite(bg, im).convert("RGB").save(os.path.join(out, n + ".png"))
    json.dump({"marks": marks, "over": over, "w": w, "h": h}, open(os.path.join(out, n + ".json"), "w"), indent=1)
    print(f"{n}: {time.time() - t:.0f}s", flush=True)
