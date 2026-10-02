"""Checks the plugin pages' data (plugin_data/) before the pages are built, so a typo fails the
build instead of breaking an animation. See the README ("Plugin pages") for the format."""
import re

from plugin_data import T

KINDS = {"text", "web", "files", "image", "desk", "none"}
BLOCKS = {"text", "note", "big", "rows", "code", "seg", "chips", "panes", "list", "diff", "table", "chart", "swatches",
          "grid", "qr", "barcode", "bar", "stats", "dial", "thumbs", "img", "field", "slider", "wave", "hours", "sep", "html"}
EFFECTS = {"toast", "show", "hide", "swap", "set", "close", "card", "file", "grid", "rename", "notify", "mb", "win", "fx",
           "sel", "addClass", "wait", "replace", "prop", "text"}
ACTS = {"click", "hover", "move", "type", "key", "wait"} | EFFECTS
FX = {"region", "pen", "spotlight", "pointer", "zoom", "camera", "keys", "large", "tele", "ruler", "recorder", "lock"}
ARTS = {"landscape", "beach", "sunset", "city", "portrait", "flower", "mug", "screen", "doc", "logo", "forest", "waves"}
SEL = re.compile(r"^(btn|opt|row|chk|cell|th|b):\d+(\.\d+)?$|^x$|^[.#\[]")
CJK = re.compile(r"[　-〿㐀-鿿＀-￯]")


class Bad(Exception):
    pass


def walk_strings(x, path, out):
    """Plain strings (not T) with Chinese in them would show Chinese on the English page."""
    if isinstance(x, T):
        return
    if isinstance(x, str):
        if CJK.search(x):
            out.append(f"{path}: Chinese text outside T(): {x[:40]!r}")
    elif isinstance(x, dict):
        for k, v in x.items():
            walk_strings(v, f"{path}.{k}", out)
    elif isinstance(x, (list, tuple)):
        for i, v in enumerate(x):
            walk_strings(v, f"{path}[{i}]", out)


def check_block(b, path, out):
    if not isinstance(b, dict) or b.get("t", "text") not in BLOCKS:
        out.append(f"{path}: unknown block {b!r:.60}")
        return
    if b.get("t") == "panes":
        for i, pane in enumerate(b.get("panes", [])):
            for j, sub in enumerate(pane):
                check_block(sub, f"{path}.panes[{i}][{j}]", out)
    if b.get("art") and b["art"] not in ARTS:
        out.append(f"{path}: unknown art {b['art']}")
    for it in b.get("items", []) if b.get("t") == "thumbs" else []:
        if it.get("art") and it["art"] not in ARTS:
            out.append(f"{path}: unknown art {it['art']}")


def check_act(a, path, out):
    if not isinstance(a, (list, tuple)) or not a or a[0] not in ACTS:
        out.append(f"{path}: unknown act {a!r:.60}")
        return
    if a[0] in ("click", "hover") and not (isinstance(a[1], str) and SEL.match(a[1])):
        out.append(f"{path}: bad selector {a[1]!r}")
    if a[0] == "click" and len(a) > 2:
        effs = a[2] if a[2] and isinstance(a[2][0], (list, tuple)) else [a[2]]
        for e in effs:
            if not e or e[0] not in EFFECTS:
                out.append(f"{path}: unknown effect {e!r:.60}")
    if a[0] in ("set", "card"):
        blocks = [a[2]] if a[0] == "set" else a[1].get("body", [])
        for i, b in enumerate(blocks):
            check_block(b, f"{path}.block[{i}]", out)


def check(pid, d, plugin):
    out = []
    for k in ("chips", "points", "scene"):
        if k not in d:
            out.append(f"missing {k}")
    if len(d.get("chips", [])) < 3:
        out.append("chips: three wanted")
    if len(d.get("points", [])) < 2:
        out.append("points: at least two wanted")
    sc = d.get("scene", {})
    src = sc.get("src", {})
    kind = src.get("kind", "desk")
    if kind not in KINDS:
        out.append(f"src.kind {kind!r}")
    if kind in ("text", "web"):
        joined = " ".join(x[0] if isinstance(x, T) else str(x) for x in src.get("lines", []))
        if "[[" not in joined and "{{" not in joined and not src.get("cap"):
            out.append("src: a text or web source needs [[a selection]], a {{target}} or a cap saying what to do")
    if kind == "files" and not any(f.get("sel") for f in src.get("files", [])) and not src.get("cap"):
        out.append("src: no file has sel: True (say what to select in cap)")
    for f in src.get("files", []):
        if f.get("art") and f["art"] not in ARTS:
            out.append(f"src.files: unknown art {f['art']}")
    if not sc.get("steps"):
        out.append("scene: no steps")
    for i, st in enumerate(sc.get("steps", [])):
        if not st.get("cap"):
            out.append(f"steps[{i}]: no cap")
        for j, a in enumerate(st.get("acts", [])):
            check_act(a, f"steps[{i}].acts[{j}]", out)
    card = sc.get("card")
    if card:
        for i, b in enumerate(card.get("body", [])):
            check_block(b, f"card.body[{i}]", out)
    fx = sc.get("fx")
    if fx and fx.get("name") not in FX:
        out.append(f"fx {fx.get('name')!r}")
    walk_strings(d, "entry", out)
    return [f"plugin_data[{pid}]: {m}" for m in out]


def check_all(data, plugins):
    problems = []
    ids = {p.id for p in plugins}
    for pid in data:
        if pid not in ids:
            problems.append(f"plugin_data[{pid}]: not in the catalog (pop_plugins.py)")
    for p in plugins:
        if p.id in data:
            problems += check(p.id, data[p.id], p)
    missing = [p.id for p in plugins if p.id not in data]
    return problems, missing
