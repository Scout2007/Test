"""Blender helper for the trailer's preview passes. It runs inside Blender (5.x; 4.2+ should work).

    blender -b <file.blend> --python trailer/tools/blender_preview.py -- inventory --out inv.json
    blender -b <file.blend> --python trailer/tools/blender_preview.py -- render --spec shot.json --out <dir or file.png>

inventory  Writes the scene's facts to JSON for the agents: scenes, frame range, fps, resolution, engines
           available, collections (with object counts), cameras (lens, sensor, transform), mesh objects (dimensions,
           location, collection), lights and linked libraries. Run it once per .blend at preflight.

render     Renders one preview shot from a JSON spec:
    {
      "engine": "WORKBENCH" | "EEVEE" | "CYCLES",
      "resolution": [1280, 536], "percent": 100, "samples": 16,
      "still": 1                          # one frame; or "frames": [1, 48] for a sequence
      "fps": 24,
      "camera": {"name": "CAM_x"}         # an existing camera, or a new one:
                {"location": [x, y, z], "look_at": "ObjectName" | [x, y, z], "rotation_deg": [x, y, z],
                 "lens_mm": 50, "sensor_mm": 36, "clip_end": 2e7, "roll_deg": 0},
      "keys": [ {"frame": 1, "location": [...], "look_at": ..., "lens_mm": 50, "roll_deg": 0}, ... ],
      "ease": "BEZIER" | "LINEAR",
      "hide_collections": ["..."], "show_collections": ["..."],
      "workbench": {"lighting": "STUDIO" | "FLAT", "color": "MATERIAL" | "OBJECT" | "SINGLE"},
      "set": {"ObjectName": {"prop_name": value}}   # custom properties, e.g. rig controls
    }
    Units are the scene's (the LREF files: 1 unit = 1 m). Output: <out> as a .png for a still, or
    <out>/frame_####.png for a sequence (join them with trailer/tools/animatic.py, or ffmpeg).

The file is never saved: every change is in memory for this render only.
"""
import json
import math
import sys
from pathlib import Path

import bpy
from mathutils import Euler, Vector


def args():
    a = sys.argv[sys.argv.index("--") + 1:] if "--" in sys.argv else []
    if not a:
        sys.exit(__doc__)
    mode, opts = a[0], {}
    for i in range(1, len(a) - 1, 2):
        opts[a[i].lstrip("-")] = a[i + 1]
    return mode, opts


def set_engine(render, name):
    """Set the render engine, trying each known identifier (they differ between Blender versions).
    The RNA enum is static in some builds, so each name is tried rather than looked up."""
    want = {"WORKBENCH": ["BLENDER_WORKBENCH"], "EEVEE": ["BLENDER_EEVEE_NEXT", "BLENDER_EEVEE"],
            "CYCLES": ["CYCLES"]}.get(name.upper(), [name])
    if name.upper() == "CYCLES":
        try:
            import addon_utils
            addon_utils.enable("cycles", default_set=True)
        except Exception:
            pass
    for w in want:
        try:
            render.engine = w
            return w
        except TypeError:
            continue
    sys.exit(f"engine {name} not available in this Blender (tried {want})")


def inventory(out):
    sc = bpy.context.scene
    r = sc.render
    data = {
        "blender": bpy.app.version_string, "file": bpy.data.filepath, "scene": sc.name,
        "scenes": [s.name for s in bpy.data.scenes],
        "frame_range": [sc.frame_start, sc.frame_end], "fps": r.fps / r.fps_base,
        "resolution": [r.resolution_x, r.resolution_y, r.resolution_percentage], "engine": r.engine,
        "engines_available": [e.identifier for e in bpy.types.RenderSettings.bl_rna.properties["engine"].enum_items],
        "unit_scale": sc.unit_settings.scale_length, "active_camera": sc.camera.name if sc.camera else None,
        "collections": [{"name": c.name, "objects": len(c.all_objects), "hidden_render": c.hide_render}
                        for c in bpy.data.collections],
        "cameras": [{"name": o.name, "lens_mm": round(o.data.lens, 2), "sensor_mm": round(o.data.sensor_width, 2),
                     "location": [round(v, 2) for v in o.matrix_world.translation],
                     "rotation_deg": [round(math.degrees(v), 2) for v in o.matrix_world.to_euler()],
                     "clip": [o.data.clip_start, o.data.clip_end]}
                    for o in bpy.data.objects if o.type == "CAMERA"],
        "meshes": [{"name": o.name, "collection": o.users_collection[0].name if o.users_collection else None,
                    "location": [round(v, 1) for v in o.matrix_world.translation],
                    "dimensions": [round(v, 1) for v in o.dimensions], "parent": o.parent.name if o.parent else None,
                    "custom_props": [k for k in o.keys() if not k.startswith("_")][:20]}
                   for o in bpy.data.objects if o.type == "MESH" and not o.parent][:400],
        "empties_with_props": [{"name": o.name, "custom_props": [k for k in o.keys() if not k.startswith("_")][:30]}
                               for o in bpy.data.objects if o.type == "EMPTY" and len(o.keys()) > 0][:100],
        "lights": [{"name": o.name, "type": o.data.type, "energy": getattr(o.data, "energy", None)}
                   for o in bpy.data.objects if o.type == "LIGHT"],
        "libraries": [lib.filepath for lib in bpy.data.libraries],
    }
    Path(out).parent.mkdir(parents=True, exist_ok=True)
    Path(out).write_text(json.dumps(data, indent=1))
    print(f"inventory: {len(data['collections'])} collections, {len(data['cameras'])} cameras, "
          f"{len(data['meshes'])} top-level meshes -> {out}")


def target(spec_look):
    if isinstance(spec_look, str):
        ob = bpy.data.objects.get(spec_look)
        if not ob:
            sys.exit(f"look_at object {spec_look!r} not found")
        return ob.matrix_world.translation.copy()
    return Vector(spec_look)


def aim(cam, loc, look_at=None, rotation_deg=None, roll_deg=0.0):
    cam.location = Vector(loc)
    if look_at is not None:
        d = target(look_at) - cam.location
        q = d.to_track_quat("-Z", "Y")
        if roll_deg:
            from mathutils import Quaternion
            q = q @ Quaternion((0, 0, 1), math.radians(roll_deg))
        cam.rotation_mode = "QUATERNION"
        cam.rotation_quaternion = q
    elif rotation_deg is not None:
        cam.rotation_mode = "XYZ"
        cam.rotation_euler = Euler([math.radians(v) for v in rotation_deg], "XYZ")


def render(spec_path, out):
    spec = json.loads(Path(spec_path).read_text())
    sc = bpy.context.scene
    r = sc.render
    set_engine(r, spec.get("engine", "WORKBENCH"))
    r.resolution_x, r.resolution_y = spec.get("resolution", [1280, 536])
    r.resolution_percentage = spec.get("percent", 100)
    r.fps, r.fps_base = spec.get("fps", 24), 1.0
    if r.engine == "CYCLES":
        sc.cycles.samples = spec.get("samples", 16)
    elif "EEVEE" in r.engine and hasattr(sc.eevee, "taa_render_samples"):
        sc.eevee.taa_render_samples = spec.get("samples", 16)
    if r.engine == "BLENDER_WORKBENCH":
        wb = spec.get("workbench", {})
        sc.display.shading.light = wb.get("lighting", "STUDIO")
        sc.display.shading.color_type = wb.get("color", "MATERIAL")
    for name in spec.get("hide_collections", []):
        c = bpy.data.collections.get(name)
        if c:
            c.hide_render = True
    for name in spec.get("show_collections", []):
        c = bpy.data.collections.get(name)
        if c:
            c.hide_render = False
    for ob_name, props in spec.get("set", {}).items():
        ob = bpy.data.objects.get(ob_name)
        if not ob:
            print(f"warning: set: object {ob_name!r} not found")
            continue
        for k, v in props.items():
            ob[k] = v
    cs = spec.get("camera", {})
    if cs.get("name"):
        cam = bpy.data.objects.get(cs["name"])
        if not cam or cam.type != "CAMERA":
            sys.exit(f"camera {cs['name']!r} not found")
    else:
        cam = bpy.data.objects.new("PREVIZ_CAM", bpy.data.cameras.new("PREVIZ_CAM"))
        sc.collection.objects.link(cam)
        cam.data.lens = cs.get("lens_mm", 50)
        cam.data.sensor_width = cs.get("sensor_mm", 36)
        cam.data.clip_start = cs.get("clip_start", 0.5)
        cam.data.clip_end = cs.get("clip_end", 2e7)
        if "location" in cs:
            aim(cam, cs["location"], cs.get("look_at"), cs.get("rotation_deg"), cs.get("roll_deg", 0))
    sc.camera = cam
    for key in spec.get("keys", []):
        f = key["frame"]
        if "location" in key:
            aim(cam, key["location"], key.get("look_at"), key.get("rotation_deg"), key.get("roll_deg", 0))
            cam.keyframe_insert("location", frame=f)
            cam.keyframe_insert("rotation_quaternion" if cam.rotation_mode == "QUATERNION" else "rotation_euler", frame=f)
        if "lens_mm" in key:
            cam.data.lens = key["lens_mm"]
            cam.data.keyframe_insert("lens", frame=f)
    ease = spec.get("ease", "BEZIER")
    for idb in (cam, cam.data):
        ad = idb.animation_data
        fcurves = getattr(ad.action, "fcurves", []) if ad and ad.action else []
        for fc in fcurves:
            for kp in fc.keyframe_points:
                kp.interpolation = ease
    out = Path(out)
    if "still" in spec:
        sc.frame_set(spec["still"])
        out.parent.mkdir(parents=True, exist_ok=True)
        r.filepath = str(out if out.suffix else out.with_suffix(".png"))
        r.image_settings.file_format = "PNG"
        bpy.ops.render.render(write_still=True)
        print(f"rendered still -> {r.filepath}")
    else:
        a, b = spec.get("frames", [sc.frame_start, sc.frame_end])
        sc.frame_start, sc.frame_end = a, b
        out.mkdir(parents=True, exist_ok=True)
        r.filepath = str(out / "frame_")
        r.image_settings.file_format = "PNG"
        bpy.ops.render.render(animation=True)
        print(f"rendered frames {a}-{b} -> {out}")


def main():
    mode, opts = args()
    if mode == "inventory":
        inventory(opts.get("out", "inventory.json"))
    elif mode == "render":
        if "spec" not in opts or "out" not in opts:
            sys.exit("render needs --spec <shot.json> --out <path>")
        render(opts["spec"], opts["out"])
    else:
        sys.exit(f"unknown mode {mode!r}: use inventory or render")


main()
