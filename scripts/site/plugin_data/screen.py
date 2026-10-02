"""Plugin pages: screen and image plugins. See __init__.py and the README ("Plugin pages")."""
import random

from . import T, res

# ---------------------------------------------------------------- small pictures and controls
# Bits of the pictures on screen and in the cards, drawn with the engine's classes (pl-art, pl-img,
# pl-seg, pl-opt, pl-lab, pl-chk, pl-btn) and inline styles. Text and backgrounds of the cards use the
# theme's variables; fixed colours appear only inside pictures (a screenshot, a photo, a gradient).

CHECK = ('<svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="1.7" '
         'stroke-linecap="round" stroke-linejoin="round"><path d="m5 12.5 4.5 4.5L19 7.5" stroke-width="2.4"/></svg>')
ART = {
    "screen": '<span class="pl-art pl-art-screen"><i class="bar"></i><i class="side"></i><i class="l1"></i><i class="l2"></i><i class="l3"></i><i class="card1"></i><i class="card2"></i></span>',
    "portrait": '<i class="body"></i><i class="head"></i><i class="hair"></i>',
    "logo": '<i class="mark"></i>',
}
PIC_FONT = "-apple-system,BlinkMacSystemFont,'Helvetica Neue','PingFang SC',sans-serif"


def chk(on=True):
    return f'<span class="pl-chk{" is-on" if on else ""}">{CHECK}</span>'


def seg(cls, items, on):
    """A segmented control in an html block: the engine's pl-seg / pl-opt, so a click selects by itself."""
    return f'<span class="pl-seg {cls}" style="justify-self:start">' + "".join(
        f'<span class="pl-opt{" is-on" if i == on else ""}">{x}</span>' for i, x in enumerate(items)) + "</span>"


def form(rows):
    """Label and control pairs in a grid, the labels lined up as Pop lines them up."""
    return ('<div style="display:grid;grid-template-columns:auto 1fr;gap:8px 10px;align-items:center">' +
            "".join(f'<span class="pl-lab">{lab}</span>{ctl}' for lab, ctl in rows) + "</div>")


def both(fn, *args):
    """T(fn(English…), fn(Chinese…)) for builders that take T arguments (also inside lists)."""
    return T(fn(*res(list(args), "en")), fn(*res(list(args), "zh")))


def qr_svg(seed, n=25, style=""):
    """A QR-like pattern: finder squares in three corners, the rest from a seeded random."""
    rnd = random.Random(seed)
    cells = []
    for y in range(n):
        for x in range(n):
            finder = (x < 8 and y < 8) or (x >= n - 8 and y < 8) or (x < 8 and y >= n - 8)
            if not finder and rnd.random() < 0.48:
                cells.append(f"M{x} {y}h1v1h-1z")
    fp = lambda x, y: f"M{x} {y}h7v7h-7zM{x + 1} {y + 1}v5h5v-5zM{x + 2} {y + 2}h3v3h-3z"
    return (f'<svg class="qr" viewBox="-1 -1 {n + 2} {n + 2}" shape-rendering="crispEdges" style="display:block;{style}">'
            f'<rect x="-1" y="-1" width="{n + 2}" height="{n + 2}" fill="#fff"/>'
            f'<path fill="#111" fill-rule="evenodd" d="{fp(0, 0)}{fp(n - 7, 0)}{fp(0, n - 7)}"/>'
            f'<path fill="#111" d="{"".join(cells)}"/></svg>')


# ---------------------------------------------------------------- Recognize Table: a screenshot of a timetable
TRAINS = {
    "en": (["Train", "Departs", "Arrives", "Fare"],
           [["2151", "6:00 AM", "9:35 AM", "$129"], ["171", "7:05 AM", "11:20 AM", "$49"], ["2153", "8:00 AM", "11:30 AM", "$139"]],
           "Departures", "New York → Boston · Mon, Oct 5", "Fares are per person, one way."),
    "zh": (["车次", "出发", "到达", "二等座"],
           [["G101", "06:20", "11:58", "¥553"], ["G103", "06:25", "12:11", "¥553"], ["G105", "07:00", "12:41", "¥553"]],
           "车次列表", "北京南 → 上海虹桥 · 10月5日 周一", "票价为二等座全价，以购票页面为准。"),
}


def table_shot(lang):
    head, rows, title, sub, foot = TRAINS[lang]
    cell = "padding:1.2cqw 2cqw;border:solid #9ea0ab;border-width:0 1px 1px 0;"
    cells = ("".join(f'<span style="{cell}background:#eef0f6;font-weight:600">{x}</span>' for x in head) +
             "".join(f'<span style="{cell}">{x}</span>' for r in rows for x in r))
    return (f'<div style="position:absolute;inset:0;container-type:inline-size;box-sizing:border-box;padding:5% 6%;'
            f'background:#fff;color:#1d1d1f;font-family:{PIC_FONT}">'
            f'<div style="font-size:4.4cqw;font-weight:700;line-height:1.2">{title}</div>'
            f'<div style="font-size:2.8cqw;color:#6e6e73;margin:.8cqw 0 3cqw">{sub}</div>'
            '<div style="display:grid;grid-template-columns:repeat(4,1fr);border:solid #9ea0ab;border-width:1px 0 0 1px;'
            f'font-size:3.1cqw;line-height:1.3">{cells}</div>'
            f'<div style="font-size:2.6cqw;color:#6e6e73;margin-top:2.4cqw">{foot}</div></div>')


def table_text(lang, kind):
    head, rows = TRAINS[lang][:2]
    if kind == "md":
        out = ["| " + " | ".join(head) + " |", "|" + "|".join(" --- " for _ in head) + "|"]
        return "\n".join(out + ["| " + " | ".join(r) + " |" for r in rows])
    sep = "\t" if kind == "tsv" else ","
    return "\n".join(sep.join(r) for r in [head] + rows)


# ---------------------------------------------------------------- Scan Code: a café table with a Wi-Fi card
def wifi_photo(title, hint):
    return ('<div style="position:absolute;inset:0;container-type:inline-size">'
            '<div style="position:absolute;left:7%;top:9%;width:23%;padding:2cqw 0 1.8cqw;border-radius:1.4cqw;background:#fff;'
            'box-shadow:0 1.2cqw 3cqw rgba(0,0,0,.28);display:flex;flex-direction:column;align-items:center;gap:1.1cqw;transform:rotate(-3deg)">'
            f'<b style="font:700 2.7cqw/1.1 {PIC_FONT};color:#1d1d1f">{title}</b>'
            + qr_svg("WIFI:T:WPA;S:Harbor;P:latte2026;;", style="width:78%;height:auto") +
            f'<span style="font:500 1.9cqw/1 {PIC_FONT};color:#6e6e73">{hint}</span></div></div>')


# ---------------------------------------------------------------- Beautify Screenshot: the captured code on a gradient
BG = [("#599eff", "#8c5cf5"), ("#ff9e59", "#f0548f"), ("#5cdba8", "#299ec7"), ("#c770f2", "#5c45d6"),
      ("#545a66", "#1f2129"), ("#f5f5f7", "#dbdee6")]
CODE = ["struct Greeting: View {", "    let name: String", "", "    var body: some View {",
        '        Text("Hello, \\(name)!")', "            .font(.largeTitle)", "    }", "}"]


def code_html(font):
    kw = lambda s: (s.replace("struct ", '<span style="color:var(--pl-accent)">struct</span> ')
                    .replace("let ", '<span style="color:var(--pl-accent)">let</span> ')
                    .replace("var ", '<span style="color:var(--pl-accent)">var</span> ')
                    .replace('"Hello, \\(name)!"', '<span style="color:var(--pl-red)">"Hello, \\(name)!"</span>'))
    return (f'<div style="height:100%;box-sizing:border-box;padding:3.2cqw 4cqw;border-radius:2.4cqw;background:var(--pl-win);color:var(--pl-l1);'
            f'box-shadow:0 2.6cqw 6cqw rgba(0,0,0,.38);font:{font}cqw/1.5 var(--pl-mono);white-space:pre;overflow:hidden">'
            + "\n".join(kw(l) for l in CODE) + "</div>")


def beautified(bg, pad):
    """The preview: the captured image (about 1.5 : 1) on a gradient, with padding pad × its width on each side."""
    a, b = BG[bg]
    w, h = 1 + 2 * pad, 1 / 1.5 + 2 * pad
    return (f'<div style="container-type:inline-size;box-sizing:border-box;aspect-ratio:{w:.3f}/{h:.3f};padding:{pad / w * 100:.2f}%;'
            f'border-radius:10px;background:linear-gradient(135deg,{a},{b})">{code_html(round(3.0 / w * 1.18, 2))}</div>')


def swatches(on):
    dots = [f'<i style="display:block;width:14px;height:14px;border-radius:50%;background:linear-gradient(135deg,{a},{b})"></i>' for a, b in BG]
    dots.append('<i style="display:block;width:12px;height:12px;border-radius:50%;border:1px dashed var(--pl-l2)"></i>')
    return ('<span class="pl-seg bf-bg" style="justify-self:start">' +
            "".join(f'<span class="pl-opt{" is-on" if i == on else ""}" style="min-width:0;padding:0 4px">{d}</span>' for i, d in enumerate(dots)) +
            "</span>")


def beautify_form(lab_bg, lab_pad, lab_ratio, sizes, auto):
    return form([(lab_bg, swatches(0)), (lab_pad, seg("bf-pad", sizes, 1)), (lab_ratio, seg("bf-ratio", [auto, "1:1", "4:3", "16:9"], 0))])


# ---------------------------------------------------------------- Split Image: the preview dims what isn't used, with grid and numbers
def split_over(x, y, w, h, cols, rows):
    dim = "position:absolute;background:rgba(0,0,0,.55);"
    line = "position:absolute;background:rgba(255,255,255,.95);box-shadow:0 0 2px rgba(0,0,0,.5);"
    out = []
    if y > 0:
        out.append(f'<i style="{dim}left:0;right:0;top:0;height:{y}%"></i>')
    if y + h < 100:
        out.append(f'<i style="{dim}left:0;right:0;top:{y + h}%;bottom:0"></i>')
    if x > 0:
        out.append(f'<i style="{dim}left:0;width:{x}%;top:{y}%;height:{h}%"></i>')
    if x + w < 100:
        out.append(f'<i style="{dim}left:{x + w}%;right:0;top:{y}%;height:{h}%"></i>')
    out.append(f'<i style="position:absolute;left:{x}%;top:{y}%;width:{w}%;height:{h}%;box-sizing:border-box;'
               'border:1.5px solid rgba(255,255,255,.95);box-shadow:0 0 2px rgba(0,0,0,.5)"></i>')
    for c in range(1, cols):
        out.append(f'<i style="{line}left:{x + w * c / cols:.2f}%;top:{y}%;height:{h}%;width:1.5px;margin-left:-.75px"></i>')
    for r in range(1, rows):
        out.append(f'<i style="{line}top:{y + h * r / rows:.2f}%;left:{x}%;width:{w}%;height:1.5px;margin-top:-.75px"></i>')
    for r in range(rows):
        for c in range(cols):
            out.append(f'<b style="position:absolute;left:{x + w * (c + .5) / cols:.2f}%;top:{y + h * (r + .5) / rows:.2f}%;'
                       'transform:translate(-50%,-50%);color:#fff;font:600 13px/1 var(--pl-font);text-shadow:0 0 3px rgba(0,0,0,.7)">'
                       f'{r * cols + c + 1}</b>')
    return "".join(out)


# ---------------------------------------------------------------- Compare Images: what changed in the new screenshot
CHANGES = [(76, 19, 9, 7, "#ff3b30", "99px"), (62, 52, 30, 38, "linear-gradient(135deg,#34c759,#30b0c7)", "6px"),
           (80, 38, 11, 5, "#c9ced8", "3px")]


def changes(opacity=1):
    return "".join(f'<i style="position:absolute;left:{x}%;top:{y}%;width:{w}%;height:{h}%;background:{bg};border-radius:{r};opacity:{opacity}"></i>'
                   for x, y, w, h, bg, r in CHANGES)


def tag(text, right=False):
    return (f'<b style="position:absolute;{"right" if right else "left"}:5px;top:5px;padding:1px 6px;border-radius:5px;background:rgba(0,0,0,.55);'
            f'color:#fff;font:600 9.5px/1.5 var(--pl-font)">{text}</b>')


def difference():
    marks = "".join(f'<i style="position:absolute;left:{x}%;top:{y}%;width:{w}%;height:{h}%;background:rgba(255,45,85,.85);border-radius:{r}"></i>'
                    f'<i style="position:absolute;left:{x - 2}%;top:{y - 3}%;width:{w + 4}%;height:{h + 6}%;border:1.5px solid #ff2d55;box-sizing:border-box"></i>'
                    for x, y, w, h, bg, r in CHANGES)
    return '<i style="position:absolute;inset:0;background:rgba(255,255,255,.55)"></i>' + marks


def swipe(old, new):
    return ('<div style="position:absolute;left:50%;top:0;right:0;bottom:0;overflow:hidden"><div style="position:absolute;top:0;bottom:0;right:0;width:200%">'
            + changes() + "</div></div>"
            '<i style="position:absolute;left:50%;top:0;bottom:0;width:2px;margin-left:-1px;background:#fff;box-shadow:0 0 0 1px rgba(0,0,0,.3)"></i>'
            '<i style="position:absolute;left:50%;top:50%;width:16px;height:16px;margin:-8px 0 0 -8px;border-radius:50%;background:#fff;box-shadow:0 1px 4px rgba(0,0,0,.4)"></i>'
            + tag(old) + tag(new, True))


def side_by_side(old, new):
    one = lambda over: f'<div class="pl-img" style="--ar:16/10">{ART["screen"]}<div class="pl-img-o">{over}</div></div>'
    return ('<div style="aspect-ratio:16/9;box-sizing:border-box;padding:0 6px;border-radius:10px;background:var(--pl-fill);'
            f'display:grid;grid-template-columns:1fr 1fr;gap:6px;align-items:center">{one(tag(old))}{one(changes() + tag(new))}</div>')


# ---------------------------------------------------------------- Make App Icon: the icon in the Dock, on iPhone and in a tab
def logo(style):
    return f'<span class="pl-art pl-art-logo" style="{style}">{ART["logo"]}</span>'


def icon_previews(rounded, name, web):
    mac = (logo("width:80%;height:80%;border-radius:22%;box-shadow:0 2px 5px rgba(0,0,0,.3)") if rounded
           else logo("width:100%;height:100%"))
    col = lambda inner, cap: (f'<div style="display:flex;flex-direction:column;align-items:center;gap:7px">{inner}'
                              f'<span class="pl-lab">{cap}</span></div>')
    return ('<div style="display:flex;align-items:flex-end;justify-content:center;gap:26px;padding:14px 0 8px;border-radius:8px;background:var(--pl-fill)">'
            + col(f'<span style="width:76px;height:76px;display:grid;place-items:center">{mac}</span>', "macOS")
            + col(logo("width:44px;height:44px;border-radius:10px;box-shadow:0 1px 2px rgba(0,0,0,.15)"), "iOS")
            + col('<span style="display:flex;align-items:center;gap:6px;height:24px;padding:0 10px;border-radius:7px;background:var(--pl-fill-2);font-size:11px">'
                  + logo("width:14px;height:14px;border-radius:2px") + f"{name}</span>", web)
            + "</div>")


def icon_form(labs, styles, margins, makes):
    boxes = '<span style="display:flex;align-items:center;gap:6px;font-size:11.5px">' + "".join(
        f'{chk()}<span style="margin-right:8px">{m}</span>' for m in makes) + "</span>"
    return form([(labs[0], seg("ai-style", styles, 0)), (labs[1], seg("ai-margin", margins, 0)), (labs[2], boxes)])


# ---------------------------------------------------------------- ID Photo: the portrait on a plain background, cropped around the face
def id_photo(color):
    return ('<div style="display:flex;justify-content:center;padding:10px 0;border-radius:8px;background:var(--pl-fill)">'
            f'<div class="pl-img is-{color}" style="--ar:295/413;width:108px;border-radius:3px">'
            f'<span class="pl-art pl-art-portrait" style="inset:auto;left:-55%;top:-14.6%;width:210%;height:118%">{ART["portrait"]}</span>'
            "</div></div>")


def id_size_row(size, sheet):
    return (f'<div style="display:flex;align-items:center;flex-wrap:wrap;gap:6px 8px;font-size:11.5px"><span class="pl-btn">{size} ⌄</span>'
            f'{chk(False)}<span>{sheet}</span></div>')


# ---------------------------------------------------------------- Redact: a delivery screenshot, then the same with mosaics
MOSAIC = "background:repeating-conic-gradient(rgba(120,120,130,.95) 0 25%,rgba(170,170,180,.95) 0 50%) 0 0/7px 7px;color:transparent;border-radius:3px"
FACE = "background:repeating-conic-gradient(#b48a6c 0 25%,#6f5547 0 50%) 0 0/8px 8px"


def delivery(lang, hidden):
    name, sub, rows = {
        "en": ("Ada Park", "Your courier · arriving 12:40", [("Phone", "(415) 555-0132", True), ("Email", "ada.park@example.com", True),
                                                           ("Order", "#48213 · 2 items", False), ("Total", "$23.40", False)]),
        "zh": ("王师傅", "骑手 · 预计 12:40 送达", [("电话", "138 0013 8000", True), ("邮箱", "wang.shifu@example.com", True),
                                               ("订单", "#48213 · 共 2 件", False), ("合计", "¥46.50", False)]),
    }[lang]
    face = f'<i style="inset:0;{FACE}"></i>' if hidden else ""
    lines = "".join(f'<div><span style="color:#86868b;margin-right:2.4cqw">{k}</span><span style="{MOSAIC if hidden and s else ""}">{v}</span></div>'
                    for k, v, s in rows)
    return (f'<div style="position:absolute;inset:0;container-type:inline-size;box-sizing:border-box;padding:5.5% 7%;background:#fff;'
            f'color:#1d1d1f;font-family:{PIC_FONT}">'
            '<div style="display:flex;align-items:center;gap:3.4cqw;margin-bottom:4cqw">'
            f'<span class="pl-art pl-art-portrait" style="width:16cqw;height:16cqw;border-radius:50%;flex:none">{ART["portrait"]}{face}</span>'
            f'<div><div style="font-size:5.4cqw;font-weight:700">{name}</div><div style="font-size:3.6cqw;color:#86868b">{sub}</div></div></div>'
            f'<div style="font-size:4.4cqw;line-height:1.85">{lines}</div></div>')


# ---------------------------------------------------------------- Watermark: grey text tiled at 30°, as strong as the slider says
def wm(text, alpha):
    return ('<div class="pl-wm">' + "".join(f'<span style="color:rgba(115,115,115,{alpha});text-shadow:none">{text}</span>' for _ in range(12)) + "</div>")


# ---------------------------------------------------------------- Image Colors: the main colours of the sunset photo
SUNSET = [("#E0679B", 27), ("#5B4BB7", 24), ("#2D2346", 18), ("#FFB36B", 14), ("#FFE2A3", 10), ("#3C2D5A", 7)]

# ---------------------------------------------------------------- Picture in Picture
# The windows on screen as Pop's chooser shows them (its own demo: a call, a live stream, a build, Settings),
# the one under the pointer first. The pictures are drawn in CSS (pl-pic-*), the call with the camera bubble's person.
def pip_meet(name):
    return ('<span class="pl-pic-meet"><span class="pl-person"><i class="room"></i><i class="lamp"></i><i class="body"></i>'
            f'<i class="head"></i><i class="hair"></i></span><b>{name}</b></span>')


PIP_TERM = ('<span class="pl-pic-term"><span>$ npm run build</span><span>&gt; vite build</span><span class="ok">✓ 1204 modules transformed.</span>'
            '<span>dist/assets/index.js 143.2 kB</span><span class="ok">✓ built in 3.81s</span></span>')
PIP_WINDOWS = [  # (app, title, icon colours, picture)
    (T("FaceTime", "FaceTime 通话"), T("Weekly product sync", "产品周会"), ("#6be38a", "#1fae4b"), T(pip_meet("Maya"), pip_meet("李华"))),
    ("Safari", T("Launch event live", "发布会直播"), ("#4fb3ff", "#1f6fd8"), '<span class="pl-pic-live"></span>'),
    (T("Terminal", "终端"), "npm run build", ("#55555c", "#1d1d20"), PIP_TERM),
    (T("System Settings", "系统设置"), "", ("#b4b6bd", "#6b6e76"), ART["screen"]),
]


def pip_title(k, i):
    app, title = PIP_WINDOWS[k][0], PIP_WINDOWS[k][1]
    app, title = _pick(app, i), _pick(title, i)
    return f"{app} — {title}" if title else app


def _pick(x, i):
    return x[i] if isinstance(x, T) else x


PIP_TILES = {"t": "html", "html": T(*[
    '<div class="pl-pips">' + "".join(
        f'<div class="pl-pipt{" is-on" if k == 0 else ""}"><div>{_pick(w[3], i)}</div>'
        f'<span><i style="--c1:{w[2][0]};--c2:{w[2][1]}"></i><em>{pip_title(k, i)}</em></span></div>'
        for k, w in enumerate(PIP_WINDOWS)) + "</div>"
    for i in (0, 1)])}
PIP_MENU = T(["Small", "Medium", "Large", "-", "✓ Opaque", "Slightly Transparent", "Half Transparent", "-", "Go to Window", "Close"],
             ["小", "中", "大", "-", "✓ 不透明", "透明一点", "半透明", "-", "回到窗口", "关闭小窗"])


DATA = {
    "removeBackground": {
        "chips": [T("People, pets, things", "人、动物、物品"), T("Offline", "离线"), T("Transparent PNG", "透明 PNG")],
        "points": [
            T("Select a picture, or an image file in Finder, and Pop <b>removes the background</b>, keeping the person, animal or object.",
              "选中一张图片，或者访达里的图片文件，Pop 就<b>去掉背景</b>，只留下人、动物或物品。"),
            T("It runs <b>on your Mac</b>, offline: the picture isn’t uploaded anywhere.", "在<b>本机</b>离线处理，图片不上传到任何地方。"),
            T("Copy the cut-out, save it as a PNG with a transparent background, or pin it on the screen.",
              "抠好的图可以复制、存成透明背景的 PNG，或者贴到屏幕上。"),
        ],
        "scene": {
            "src": {"kind": "files", "cap": T("Select a photo in Finder", "在访达里选中一张照片"),
                    "files": [{"name": "Portrait.jpg", "kind": "photo", "art": "portrait", "sel": True}, {"name": "Beach.heic", "kind": "photo", "art": "beach"},
                              {"name": "Mug.png", "kind": "photo", "art": "mug"}, {"name": T("Notes.txt", "笔记.txt")}]},
            "card": {"w": 320, "sub": "Portrait.jpg", "btns": [T("Copy", "复制"), T("Save as PNG", "存成 PNG"), T("Pin to Screen", "贴到屏幕")], "tint": 1,
                     "body": [{"t": "panes", "panes": [[{"t": "img", "art": "portrait", "ar": "4/3"}], [{"t": "img", "art": "portrait", "ar": "4/3", "mods": ["cutout"]}]]}]},
            "steps": [
                {"cap": T("The background disappears", "背景没了"), "acts": [["wait", 500], ["swap", 0, 1]]},
                {"cap": T("Save it as a transparent PNG", "存成透明背景的 PNG"),
                 "acts": [["click", "btn:1"], ["close"], ["file", {"name": T("Portrait cut-out.png", "Portrait 抠图.png"), "kind": "photo", "art": "portrait", "at": 1}]]},
            ],
        },
    },
    "tableOCR": {
        "chips": ["Markdown", "CSV · TSV", "macOS 26"],
        "points": [
            T("Select a screenshot or picture of a table, or with nothing selected drag over one on screen, and Pop <b>reads it row by row and column by column</b>.",
              "选中表格的截图或图片，什么都没选时就在屏幕上框住表格，Pop <b>按行列认出每个格子的文字</b>。"),
            T("Switch between a Markdown table, tab-separated text (paste it into a spreadsheet and the columns line up) and CSV, then copy the one you need.",
              "可以在 Markdown 表格、制表符分隔（粘贴到表格软件里直接分好列）和 CSV 之间切换，复制要用的那种。"),
            T("Reading rows and columns needs macOS 26; earlier versions recognize the text as plain text.",
              "按行列识别需要 macOS 26，更早的系统按普通文字识别。"),
            T("Images in the clipboard history have Recognize Table in their menu too.", "剪贴板历史里的图片，右键菜单里也有「识别表格」。"),
        ],
        "scene": {
            "src": {"kind": "image", "app": T("Preview", "预览"), "title": T("Timetable.png", "车次.png"), "art": "doc",
                    "overlay": T(table_shot("en"), table_shot("zh")),
                    "cap": T("Select a screenshot of a table", "选中表格的截图"),
                    "sub": T("With nothing selected, you drag over a table on screen.", "什么都没选时，就在屏幕上框住表格。")},
            "card": {"w": 350, "btns": [T("Copy Markdown", "复制 Markdown")],
                     "body": [{"t": "seg", "items": ["Markdown", T("Tab-Separated", "制表符分隔"), "CSV"], "on": 0, "ctl": 1},
                              {"t": "panes", "panes": [[{"t": "text", "mono": True, "text": T(table_text("en", "md"), table_text("zh", "md"))}],
                                                       [{"t": "text", "mono": True, "text": T(table_text("en", "tsv"), table_text("zh", "tsv"))}],
                                                       [{"t": "text", "mono": True, "text": T(table_text("en", "csv"), table_text("zh", "csv"))}]]},
                              {"t": "note", "text": T("4 rows × 4 columns", "4 行 × 4 列")}]},
            "steps": [
                {"cap": T("Rows and columns, as Markdown", "按行列认出，转成 Markdown"), "acts": [], "hold": 1600},
                {"cap": T("Or tab-separated, or CSV", "也可以是制表符分隔或 CSV"), "sub": T("Tab-separated text pastes into a spreadsheet in columns.", "制表符分隔的粘贴到表格软件里直接分好列。"),
                 "acts": [["click", "opt:0.1"], ["wait", 1100], ["click", "opt:0.2"], ["wait", 1100], ["click", "opt:0.0"]]},
                {"cap": T("Copy it", "复制"), "acts": [["click", "btn:0", ["toast", T("Copied", "已复制")]]]},
            ],
        },
    },
    "scanCode": {
        "chips": [T("QR codes and barcodes", "二维码和条形码"), T("Wi-Fi passwords", "Wi-Fi 密码"), T("Open links", "直接打开链接")],
        "points": [
            T("<b>Drag over a QR code or barcode</b> anywhere on screen, in a photo, a slide or a web page, and Pop reads it.",
              "在屏幕上<b>框住二维码或条形码</b>，照片里、幻灯片上、网页里的都行，Pop 识别出里面的内容。"),
            T("A Wi-Fi code shows the network name, the password and the security, each ready to copy.",
              "Wi-Fi 二维码直接列出网络名称、密码和加密方式，每一项都能复制。"),
            T("A link can be opened right away; anything else can be copied. If the area holds several codes, Pop reads them all.",
              "链接可以直接打开，其他内容一键复制；框住的地方有几个码就认出几个。"),
            T("Needs Screen Recording permission; without it, the capture may show only the desktop background.",
              "需要「录屏与系统录音」权限，没有的话框到的可能只有桌面背景。"),
        ],
        "scene": {
            "src": {"kind": "image", "app": T("Preview", "预览"), "title": T("Café.jpg", "咖啡馆.jpg"), "art": "mug",
                    "overlay": T(wifi_photo("Free Wi-Fi", "Scan to join"), wifi_photo("免费 Wi-Fi", "扫码连接")),
                    "cap": T("Find the code on screen", "找到屏幕上的码"), "sub": T("Nothing needs to be selected.", "不用选中什么。")},
            "slot": 1,
            "fx": {"name": "region", "target": ".pl-shot-o .qr", "hint": T("Drag over the code", "框住二维码")},
            "card": {"w": 320, "title": T("Wi-Fi QR Code", "Wi-Fi 二维码"),
                     "body": [{"t": "rows", "rows": [[T("Network name", "网络名称"), T("Harbor Café Guest", "港湾咖啡-访客")],
                                                     [T("Password", "密码"), "latte2026"], [T("Security", "加密方式"), "WPA"]]}]},
            "steps": [
                {"cap": T("Drag over the code", "框住二维码"), "sub": T("A Wi-Fi code shows its network and password.", "Wi-Fi 二维码直接列出网络名和密码。"),
                 "acts": [], "hold": 1500},
                {"cap": T("Copy the password", "复制密码"),
                 "acts": [["click", ".pl-b-rows .pl-row[data-i=\"1\"] .pl-ib", ["toast", T("Copied", "已复制")]]]},
            ],
        },
    },
    "beautify": {
        "chips": [T("Gradient backgrounds", "渐变背景"), "1:1 · 4:3 · 16:9", T("Rounded corners, shadow", "圆角和阴影")],
        "points": [
            T("Puts a screenshot on a <b>gradient background</b> with padding, rounded corners and a shadow, so it looks good in posts and slides.",
              "给截图垫上<b>渐变背景</b>，四周留白，加上圆角和阴影，发文章、做演示更好看。"),
            T("Six backgrounds or none, small, medium or large padding, and a ratio of 1:1, 4:3 or 16:9 to fill the picture out.",
              "六种背景或者透明，留白小、中、大，还能按 1:1、4:3、16:9 把画面补齐。"),
            T("Uses the selected image; with nothing selected, you drag over an area of the screen first.",
              "选中图片就用它，没选中就先框选屏幕上的一块。"),
            T("The preview follows every change. Copy it, save it to Downloads or pin it to the screen at full size; Pop remembers the look you chose.",
              "改什么预览都跟着变；复制、存到「下载」或者贴到屏幕上时按原图大小画，上次选的样子会记住。"),
        ],
        "scene": {
            "src": {"kind": "text", "app": "Xcode", "title": "Greeting.swift", "mono": True, "lines": CODE,
                    "cap": T("Open what you want to share", "打开要分享的内容"), "sub": T("Nothing selected: you drag over an area.", "没选中图片时，先框选一块。")},
            "slot": 3,
            "fx": {"name": "region", "target": ".pl-doc", "hint": T("Drag to select an area", "拖动选择一块区域")},
            "card": {"w": 350, "btns": [T("Pin to Screen", "贴到屏幕"), T("Save to Downloads", "存到「下载」"), T("Copy Image", "复制图片")], "tint": 2,
                     "body": [{"t": "panes", "panes": [[{"t": "html", "html": beautified(0, .09)}], [{"t": "html", "html": beautified(1, .09)}],
                                                       [{"t": "html", "html": beautified(1, .14)}]]},
                              {"t": "html", "html": both(beautify_form, T("Background", "背景"), T("Padding", "留白"), T("Ratio", "比例"),
                                                         [T("Small", "小"), T("Medium", "中"), T("Large", "大")], T("Auto", "自动"))}]},
            "steps": [
                {"cap": T("On a gradient, with a shadow", "垫上渐变背景，加上阴影"), "acts": [], "hold": 1400},
                {"cap": T("Pick a background and padding", "换背景、调留白"), "sub": T("The preview follows every change.", "预览跟着变。"),
                 "acts": [["click", ".bf-bg .pl-opt:nth-child(2)", ["swap", 0, 1]], ["wait", 700],
                          ["click", ".bf-pad .pl-opt:nth-child(3)", ["swap", 0, 2]]]},
                {"cap": T("Copy the image", "复制图片"), "sub": T("Or save it to Downloads, or pin it to the screen.", "也可以存到「下载」，或者贴到屏幕上。"),
                 "acts": [["click", "btn:2", ["toast", T("Image copied", "已复制图片")]]]},
            ],
        },
    },
    "imageConvert": {
        "chips": ["PNG · JPEG · HEIC", T("Under 500 KB", "压到 500 KB 以内"), T("Remove location", "去掉位置信息")],
        "points": [
            T("Select image files in Finder to <b>convert them to PNG, JPEG or HEIC</b>, halve their size, compress them, rotate or flip them.",
              "在访达里选中图片文件，<b>转成 PNG、JPEG、HEIC</b>，缩小一半、压缩体积，或者旋转、左右翻转。"),
            T("Compress to Size… keeps a JPEG under 100 KB, 200 KB, 500 KB, 1 MB, 2 MB or a size you type: lower quality first, smaller dimensions only if needed.",
              "「压缩到指定大小…」把图片压到 100 KB、200 KB、500 KB、1 MB、2 MB 或者自己写的大小以内：先降画质，还不够再缩小尺寸。"),
            T("Photos with a location or capture info can get a copy without the location, or without any of it.",
              "带位置、拍摄信息的照片，可以另存一份去掉位置的，或者连拍摄信息一起去掉。"),
            T("Results are <b>saved next to the originals</b>, never over them, and selected in Finder.",
              "结果<b>存在原图旁边</b>，不会覆盖原图，转好后在访达里选中。"),
        ],
        "scene": {
            "src": {"kind": "files", "app": T("Pictures", "图片"), "cap": T("Select photos in Finder", "在访达里选中照片"),
                    "files": [{"name": "IMG_2041.HEIC", "kind": "photo", "art": "sunset", "sel": True}, {"name": "IMG_2042.HEIC", "kind": "photo", "art": "beach"},
                              {"name": T("Screenshot.png", "截图.png"), "kind": "photo", "art": "screen"}, {"name": T("Tickets.pdf", "门票.pdf")}]},
            "card": {"w": 380,
                     "btns": [T("Convert to PNG", "转成 PNG"), T("Convert to JPEG", "转成 JPEG"), T("Convert to HEIC", "转成 HEIC"), T("Half Size", "缩小一半"),
                              T("Compress", "压缩"), T("Rotate Left", "向左转"), T("Rotate Right", "向右转"), T("Flip Horizontal", "左右翻转"),
                              T("Remove Location", "去掉位置信息"), T("Remove Capture Info", "去掉拍摄信息"), T("Compress to Size…", "压缩到指定大小…")],
                     "body": [{"t": "rows", "rows": [[T("Dimensions", "尺寸"), "4032 × 3024"], [T("Format", "格式"), "HEIC"], [T("Size", "大小"), "2.9 MB"]]},
                              {"t": "note", "text": T("IMG_2041.HEIC. Converted files are saved next to the originals.", "IMG_2041.HEIC，转换后存在原图旁边")}]},
            "steps": [
                {"cap": T("Pick a format or an action", "选一种格式或者操作"), "sub": T("Its size and format are on the card.", "卡片上写着尺寸、格式和大小。"),
                 "acts": [["hover", "btn:1"]], "hold": 1100},
                {"cap": T("Compress to a size", "压缩到指定大小"), "sub": T("For forms that limit the file size.", "网上报名这类有大小限制的场合。"),
                 "acts": [["click", "btn:10"],
                          ["card", {"w": 340, "title": T("Compress to Size", "压缩到指定大小"), "sub": "IMG_2041.HEIC",
                                    "body": [{"t": "note", "text": T("Saves a JPEG copy, lowering the quality first and then the size if needed. The original stays unchanged. Currently 2.9 MB in total.",
                                                                     "存成 JPEG：先降低画质，还不够就缩小尺寸，另存一份，原图不动。现在一共 2.9 MB。")},
                                             {"t": "html", "html": '<div class="pl-flow cz">' + "".join(f'<span class="pl-btn">{x}</span>' for x in ["100 KB", "200 KB", "500 KB", "1 MB", "2 MB"]) + "</div>"},
                                             {"t": "html", "html": T('<div style="display:flex;align-items:center;gap:6px"><span class="pl-field" style="width:100px"><span class="pl-ph2">Other size</span></span>'
                                                                     '<span class="pl-lab">KB</span><span class="pl-btn is-tint">Compress</span></div>',
                                                                     '<div style="display:flex;align-items:center;gap:6px"><span class="pl-field" style="width:100px"><span class="pl-ph2">其他大小</span></span>'
                                                                     '<span class="pl-lab">KB</span><span class="pl-btn is-tint">压缩</span></div>')}]}]]},
                {"cap": T("A copy under 500 KB", "另存一份 500 KB 以内的"),
                 "acts": [["click", ".cz .pl-btn:nth-child(3)"], ["close"],
                          ["file", {"name": "IMG_2041 500KB.jpg", "kind": "photo", "art": "sunset", "at": 1}],
                          ["toast", T("Compressed to 486 KB", "已压缩到 486 KB")]]},
            ],
        },
    },
    "stitchImages": {
        "chips": [T("Vertical or horizontal", "竖着或横着拼"), T("Animated GIF", "合成动图"), T("In file name order", "按文件名排序")],
        "points": [
            T("Select several images and <b>stitch them into one</b>: vertically, such as chat screenshots into one long image, or horizontally.",
              "选中几张图片，<b>拼成一张</b>：竖着拼（比如几张聊天截图拼成一张长图），或者横着拼。"),
            T("They go in file name order, which for screenshots is the order they were taken. If widths differ, they’re scaled to the smallest, so nothing gets blurry.",
              "按文件名的顺序拼，截图的名字带着时间，就是先后顺序；宽度不一样时按最小的那张缩放，小图不会被放大变糊。"),
            T("Or make an animated image: a looping GIF that shows each picture for a second.", "也可以合成动图：循环播放的 GIF，每张停 1 秒。"),
            T("The result is saved next to the first image. Up to 50 images at a time.", "结果存在第一张旁边，一次最多 50 张。"),
        ],
        "scene": {
            "src": {"kind": "files", "app": T("Desktop", "桌面"), "cap": T("Select the images in Finder", "在访达里选中几张图片"),
                    "files": [{"name": T("Chat 1.png", "聊天 1.png"), "kind": "photo", "art": "screen", "sel": True},
                              {"name": T("Chat 2.png", "聊天 2.png"), "kind": "photo", "art": "screen", "sel": True},
                              {"name": T("Chat 3.png", "聊天 3.png"), "kind": "photo", "art": "screen", "sel": True},
                              {"name": T("Receipt.pdf", "发票.pdf")}, {"name": "Mug.png", "kind": "photo", "art": "mug"}]},
            "slot": 6,
            "card": {"w": 360, "btns": [T("Stitch Vertically", "竖着拼接"), T("Stitch Horizontally", "横着拼接"), T("Make Animated Image", "合成动图")],
                     "body": [{"t": "list", "dense": True, "items": [{"file": {"kind": "photo", "art": "screen"}, "title": T("Chat 1.png", "聊天 1.png")},
                                                                    {"file": {"kind": "photo", "art": "screen"}, "title": T("Chat 2.png", "聊天 2.png")},
                                                                    {"file": {"kind": "photo", "art": "screen"}, "title": T("Chat 3.png", "聊天 3.png")}]},
                              {"t": "note", "text": T("3 images are stitched in the order above; if widths (heights when horizontal) differ, they’re scaled to the smallest. Animated images show each frame for 1 s at the size of the first image.",
                                                      "3 张图片按上面的顺序拼接；宽度（横着拼时是高度）不一样时按最小的那张缩放。合成动图时每张停 1 秒，画面大小按第一张")}]},
            "steps": [
                {"cap": T("Check the order", "看一下顺序"), "sub": T("File name order: for screenshots, the order they were taken.", "按文件名排，截图就是先后顺序。"),
                 "acts": [], "hold": 1500},
                {"cap": T("Stitch them vertically", "竖着拼成一张"),
                 "acts": [["click", "btn:0"], ["close"],
                          ["file", {"name": T("Chat 1 Stitched.png", "聊天 1 拼接.png"), "kind": "photo", "art": "screen", "at": 1}],
                          ["toast", T("Stitched and saved next to the first image", "已拼成一张，存在第一张旁边")]]},
            ],
        },
    },
    "splitImage": {
        "chips": [T("3 × 3 grid", "九宫格"), T("Three across", "横切三张"), T("Long image into pages", "长图分页")],
        "points": [
            T("Cut a photo into a <b>3 × 3 or 2 × 2 grid</b>, cropped to a square around the subject, or into three squares side by side.",
              "把照片切成<b>九宫格、四宫格</b>（先对准画面里的主体裁成正方形），或者横着切成三张正方形。"),
            T("A long image, such as a scrolling screenshot, can be cut into up to 9 pages of the same length.",
              "长图（比如滚动截图）可以切成几页，每页一样长，最多 9 页。"),
            T("The preview dims what isn’t used and numbers each piece in posting order, left to right and top to bottom.",
              "预览里压暗用不到的部分，画出格线和编号，编号就是发出去的顺序：从左到右、从上到下。"),
            T("The pieces go into <b>a new folder next to the original</b>: photos as JPEG, screenshots as PNG. Pop remembers the layout you used.",
              "切好的存在<b>原图旁边的新文件夹</b>里，照片存成 JPEG，截图存成 PNG；上次用的切法会记住。"),
        ],
        "scene": {
            "src": {"kind": "files", "app": T("Pictures", "图片"), "cap": T("Select a photo in Finder", "在访达里选中一张照片"),
                    "files": [{"name": T("Beach.jpg", "海边.jpg"), "kind": "photo", "art": "beach", "sel": True}, {"name": T("Sunset.jpg", "日落.jpg"), "kind": "photo", "art": "sunset"},
                              {"name": T("Forest.jpg", "森林.jpg"), "kind": "photo", "art": "forest"}, {"name": T("City.jpg", "城市.jpg"), "kind": "photo", "art": "city"}]},
            "card": {"w": 340, "sub": T("Beach.jpg", "海边.jpg"), "btns": [T("Split and Save", "切好存下")], "tint": 0,
                     "body": [{"t": "seg", "items": [T("3 × 3 Grid", "九宫格"), T("2 × 2 Grid", "四宫格"), T("Three Across", "横切三张")], "on": 0, "ctl": 1},
                              {"t": "panes", "panes": [
                                  [{"t": "img", "art": "beach", "ar": "3/2", "over": split_over(16.67, 0, 66.67, 100, 3, 3)},
                                   {"t": "note", "text": T("9 pieces, 720 × 720 each, saved in order in the “Beach 3 × 3 Grid” folder next to the original",
                                                           "切成 9 张 720 × 720，按编号的顺序存在原图旁边的「海边 九宫格」文件夹")}],
                                  [{"t": "img", "art": "beach", "ar": "3/2", "over": split_over(16.67, 0, 66.67, 100, 2, 2)},
                                   {"t": "note", "text": T("4 pieces, 1080 × 1080 each, saved in order in the “Beach 2 × 2 Grid” folder next to the original",
                                                           "切成 4 张 1080 × 1080，按编号的顺序存在原图旁边的「海边 四宫格」文件夹")}],
                                  [{"t": "img", "art": "beach", "ar": "3/2", "over": split_over(0, 17.5, 100, 50, 3, 1)},
                                   {"t": "note", "text": T("3 pieces, 1080 × 1080 each, saved in order in the “Beach Three Across” folder next to the original",
                                                           "切成 3 张 1080 × 1080，按编号的顺序存在原图旁边的「海边 横切三张」文件夹")}]]}]},
            "steps": [
                {"cap": T("A 3 × 3 grid around the subject", "对准主体切九宫格"), "sub": T("What isn’t used is dimmed; the numbers are the posting order.", "用不到的部分压暗，编号就是发出去的顺序。"),
                 "acts": [], "hold": 1500},
                {"cap": T("Or 2 × 2, or three across", "也可以切四宫格、横切三张"),
                 "acts": [["click", "opt:0.1"], ["wait", 1000], ["click", "opt:0.2"], ["wait", 1000], ["click", "opt:0.0"]]},
                {"cap": T("Split and save", "切好存下"), "sub": T("The pieces go into a new folder.", "切好的放进一个新文件夹。"),
                 "acts": [["click", "btn:0"], ["close"],
                          ["file", {"name": T("Beach 3 × 3 Grid", "海边 九宫格"), "kind": "folder", "at": 1}],
                          ["toast", T("Saved 9 pieces in “Beach 3 × 3 Grid”", "切好了 9 张，存在「海边 九宫格」")]]},
            ],
        },
    },
    "compareImages": {
        "chips": [T("Swipe divider", "滑动分界线"), T("Changes in red", "不同之处标红"), T("Design vs. build", "设计稿对照实现")],
        "points": [
            T("Select two images in Finder and compare them side by side, with a <b>swipe divider</b>, or with the new one laid translucently over the old.",
              "在访达里选中两张图片，可以并排看、拖动<b>分界线</b>看，或者把新的半透明地叠在旧的上面。"),
            T("Difference <b>marks the pixels that changed in red</b>, boxes each area and says how many there are and what share of the pixels they cover.",
              "「差异」把<b>不一样的像素涂成红色</b>，每一处框起来，写明有几处、占多少像素。"),
            T("The file modified earlier counts as the old one. Ignore subtle differences skips the invisible noise of compressed photos and exported screenshots.",
              "修改时间早的算旧的；勾上「忽略细微差别」，压缩过的照片、导出过的截图里肉眼看不出的杂色就不算。"),
            T("Copy, save or pin the view you’re looking at, drawn at full size. Pop remembers the view you used last.",
              "复制、存到「下载」或者贴到屏幕上的，就是当前看到的样子，按原图大小画；上次用的看法会记住。"),
        ],
        "scene": {
            "src": {"kind": "files", "app": T("Desktop", "桌面"), "cap": T("Select two images in Finder", "在访达里选中两张图片"),
                    "files": [{"name": T("Settings old.png", "设置页 旧.png"), "kind": "photo", "art": "screen", "sel": True},
                              {"name": T("Settings new.png", "设置页 新.png"), "kind": "photo", "art": "screen", "sel": True},
                              {"name": T("Release notes.md", "发布说明.md")}]},
            "slot": 7,
            "card": {"w": 360, "sub": T("Settings old.png → Settings new.png", "设置页 旧.png → 设置页 新.png"),
                     "btns": [T("Pin to Screen", "贴到屏幕"), T("Save to Downloads", "存到「下载」"), T("Copy Image", "复制图片")], "tint": 2,
                     "body": [{"t": "seg", "items": [T("Side by Side", "并排"), T("Swipe", "滑动"), T("Overlay", "叠加"), T("Difference", "差异")], "on": 3, "ctl": 1},
                              {"t": "panes", "on": 3, "panes": [
                                  [{"t": "html", "html": both(side_by_side, T("Old", "旧"), T("New", "新"))}],
                                  [{"t": "img", "art": "screen", "ar": "16/9", "over": both(swipe, T("Old", "旧"), T("New", "新"))},
                                   {"t": "note", "text": T("Drag the divider", "拖动中间的分界线")}],
                                  [{"t": "img", "art": "screen", "ar": "16/9", "over": changes(.5)},
                                   {"t": "slider", "label": T("Old", "旧"), "value": .5, "right": T("New", "新")}],
                                  [{"t": "img", "art": "screen", "ar": "16/9", "mods": ["gray"], "over": difference()},
                                   {"t": "list", "dense": True, "items": [{"chk": False, "title": T("Ignore subtle differences", "忽略细微差别")}]}]]},
                              {"t": "note", "text": T("Areas that differ: 3 · 1.2% of the pixels", "3 处不一样，占 1.2% 的像素")}]},
            "steps": [
                {"cap": T("What changed is marked in red", "不一样的地方标成红色"), "sub": T("Each area is boxed and counted.", "每一处都框出来，写明有几处。"),
                 "acts": [], "hold": 1600},
                {"cap": T("Swipe, overlay or side by side", "滑动、叠加或者并排看"),
                 "acts": [["click", "opt:0.1"], ["wait", 1100], ["click", "opt:0.2"], ["wait", 1000], ["click", "opt:0.0"], ["wait", 900]]},
                {"cap": T("Copy what you see", "复制当前看到的样子"), "acts": [["click", "btn:2", ["toast", T("Image copied", "已复制图片")]]]},
            ],
        },
    },
    "appIcon": {
        "chips": [".icns · AppIcon", "iOS 1024", "favicon.ico"],
        "points": [
            T("Turn one image into a <b>macOS .icns and an Xcode icon set</b> (ten sizes from 16 to 1024), a 1024 iOS icon and a website favicon.",
              "用一张图生成 <b>macOS 的 .icns 和 Xcode 用的图标集</b>（16 到 1024 的十种尺寸）、iOS 的 1024 图标，还有网站的 favicon。"),
            T("The macOS icon can take the rounded square shape and size of the system’s app icons, with a little shadow, or fill the whole square as is.",
              "macOS 的图标可以做成和系统 App 一样的圆角方块（四周留白、底下带一点阴影），也可以原样铺满。"),
            T("A logo on a transparent background can get a margin and a white or black background; an image that isn’t square is cropped around the subject or fitted whole.",
              "透明底的标志可以留一圈边，垫上白色或黑色；不是正方形的图对准主体裁成正方形，或者整张放进去。"),
            T("The website set has favicon.ico, the PNG sizes for phones and a site.webmanifest. Everything goes into a folder next to the image.",
              "网站用的有 favicon.ico、手机加到主屏幕用的几种 PNG 和 site.webmanifest；全都放在原图旁边的文件夹里。"),
        ],
        "scene": {
            "src": {"kind": "files", "app": T("Design", "设计"), "cap": T("Select an image in Finder", "在访达里选中一张图片"),
                    "files": [{"name": "Logo.png", "kind": "photo", "art": "logo", "sel": True}, {"name": "Banner.png", "kind": "photo", "art": "sunset"},
                              {"name": T("Brand guide.pdf", "品牌规范.pdf")}]},
            "card": {"w": 350, "sub": "Logo.png", "btns": [T("Make", "生成")], "tint": 0,
                     "body": [{"t": "panes", "panes": [[{"t": "html", "html": both(icon_previews, True, "Logo", T("Website", "网站"))}],
                                                       [{"t": "html", "html": both(icon_previews, False, "Logo", T("Website", "网站"))}]]},
                              {"t": "html", "html": both(icon_form, [T("Style", "样式"), T("Margin", "留边"), T("Make", "生成")],
                                                         [T("Rounded Square", "圆角方块"), T("As Is", "原样")],
                                                         [T("None", "不留"), T("Narrow", "窄"), T("Wide", "宽")], ["macOS", "iOS", T("Website", "网站")])},
                              {"t": "note", "text": T("Makes a macOS .icns and icon set, a 1024 iOS icon, a website favicon, saved in the “Logo Icons” folder next to the image",
                                                      "生成 macOS 的 .icns 和图标集、iOS 的 1024 图标、网站的 favicon，存在原图旁边的「Logo 图标」文件夹")}]},
            "steps": [
                {"cap": T("In the Dock, on iPhone, in a tab", "Dock、iPhone、标签页上的样子"), "acts": [], "hold": 1500},
                {"cap": T("Rounded square, or as is", "圆角方块，或者原样铺满"),
                 "acts": [["click", ".ai-style .pl-opt:nth-child(2)", ["swap", 0, 1]], ["wait", 1000],
                          ["click", ".ai-style .pl-opt:nth-child(1)", ["swap", 0, 0]]]},
                {"cap": T("Make them all at once", "一次全部生成"), "sub": T("macOS, iOS and Website folders, side by side.", "macOS、iOS、网站各一个文件夹。"),
                 "acts": [["click", "btn:0"], ["close"], ["file", {"name": T("Logo Icons", "Logo 图标"), "kind": "folder", "at": 1}],
                          ["toast", T("Made 21 files in “Logo Icons”", "生成了 21 个文件，存在「Logo 图标」")]]},
            ],
        },
    },
    "watermark": {
        "chips": [T("Images and PDFs", "图片和 PDF"), T("Tiled diagonally", "斜着铺满"), T("Light to strong", "浓淡可调")],
        "points": [
            T("Tiles <b>semi-transparent text diagonally</b> across the selected images, or every page of a PDF, before you send copies of IDs or documents.",
              "给选中的图片（PDF 是每一页）<b>斜着铺满一层半透明的文字</b>，证件照片、复印件发给别人之前加一层。"),
            T("The text starts as “For this purpose only. Not valid for any other use.”, and Pop remembers what you write; the slider goes from light to strong.",
              "文字默认是「仅供办理业务使用，他用无效」，下次还用上次写的；滑块调浓淡。"),
            T("The preview follows as you type. Each file gets a copy named “Name Watermark”, and the originals stay unchanged.",
              "边写边看预览；每个文件另存一份「原名 水印」，原文件不动。"),
            T("A watermarked PDF’s text can still be selected and searched.", "加了水印的 PDF，原来的文字还能选中、搜索。"),
        ],
        "scene": {
            "src": {"kind": "files", "app": T("Documents", "文稿"), "cap": T("Select images or PDFs", "选中图片或 PDF"),
                    "files": [{"name": T("ID card.jpg", "身份证.jpg"), "kind": "photo", "art": "portrait", "sel": True},
                              {"name": T("Lease.pdf", "租房合同.pdf"), "sel": True}, {"name": T("Payslip.pdf", "工资条.pdf")}]},
            "card": {"w": 340, "sub": T("2 files", "2 个文件"), "btns": [T("Watermark 2 Files", "给 2 个文件加水印")], "tint": 0,
                     "body": [{"t": "panes", "panes": [
                                  [{"t": "img", "art": "portrait", "ar": "2/1", "over": both(wm, T("For this purpose only. Not valid for any other use.", "仅供办理业务使用，他用无效"), .3)}],
                                  [{"t": "img", "art": "portrait", "ar": "2/1", "over": both(wm, T("For the apartment lease only", "仅供租房使用，他用无效"), .3)}],
                                  [{"t": "img", "art": "portrait", "ar": "2/1", "over": both(wm, T("For the apartment lease only", "仅供租房使用，他用无效"), .55)}]]},
                              {"t": "field", "value": T("For this purpose only. Not valid for any other use.", "仅供办理业务使用，他用无效"), "ph": T("Watermark text", "水印文字")},
                              {"t": "slider", "label": T("Light", "淡"), "value": .4, "right": T("Strong", "浓")},
                              {"t": "note", "text": T("Tiled diagonally across the image (every page of a PDF) and saved as a copy named “Name Watermark” next to the original, which stays unchanged",
                                                      "斜着铺满整张图（PDF 每一页都铺），另存一份「原名 水印」放在原文件旁边，原文件不动")}]},
            "steps": [
                {"cap": T("Preview it on the first file", "在第一个文件上预览"), "acts": [], "hold": 1200},
                {"cap": T("Your own text, light or strong", "写上自己的文字，调浓淡"), "sub": T("The preview follows as you type.", "边写边看预览。"),
                 "acts": [["type", 1, T("For the apartment lease only", "仅供租房使用，他用无效")], ["swap", 0, 1], ["wait", 500],
                          ["move", ".pl-b-slider .pl-sl", .4, .5], ["prop", 2, "--v", .9], ["move", ".pl-b-slider .pl-sl", .9, .5, 500], ["swap", 0, 2]]},
                {"cap": T("Watermark both files", "两个文件都加上"), "sub": T("Each gets a copy; the originals stay unchanged.", "各自另存一份，原文件不动。"),
                 "acts": [["click", "btn:0"], ["close"],
                          ["file", {"name": T("ID card Watermark.jpg", "身份证 水印.jpg"), "kind": "photo", "art": "portrait", "at": 1}],
                          ["file", {"name": T("Lease Watermark.pdf", "租房合同 水印.pdf"), "at": 3}],
                          ["toast", T("Watermarked 2 files", "已给 2 个文件加上水印")]]},
            ],
        },
    },
    "idPhoto": {
        "chips": [T("White · blue · red", "白底 · 蓝底 · 红底"), T("1-inch, 2-inch", "一寸、二寸"), "300 dpi"],
        "points": [
            T("Select a portrait and get an <b>ID photo</b>: the background becomes white, blue or red, and it’s cropped around the face.",
              "选中一张人像照片，做成<b>证件照</b>：换成白底、蓝底或红底，按人脸的位置裁好。"),
            T("Small 1-inch, 1-inch, large 1-inch, small 2-inch or 2-inch at 300 dpi, so it prints at the right size; or keep the original size and change only the background.",
              "小一寸、一寸、大一寸、小二寸、二寸，带 300 dpi，打印出来正好是标准尺寸；也可以保持原尺寸只换底色。"),
            T("Also save a 6-inch print sheet: as many copies as fit (12 at 1-inch, 4 at 2-inch), with cutting lines, ready for a photo lab.",
              "勾上「另存 6 寸冲印排版」，再存一张排满的 6 寸相纸（一寸 12 张、二寸 4 张），带裁切线，直接拿去冲印。"),
            T("Removing the background and finding the face <b>happen on your Mac</b>; the photo isn’t uploaded. The copy is saved next to the original.",
              "抠图和找人脸都<b>在本机进行</b>，不上传照片；另存一份放在原图旁边，原图不动。"),
        ],
        "scene": {
            "src": {"kind": "files", "cap": T("Select a portrait in Finder", "在访达里选中一张人像照片"),
                    "files": [{"name": T("Selfie.jpg", "自拍.jpg"), "kind": "photo", "art": "portrait", "sel": True}, {"name": "Beach.heic", "kind": "photo", "art": "beach"},
                              {"name": T("Visa form.pdf", "签证申请表.pdf")}]},
            "card": {"w": 350, "sub": T("Selfie.jpg", "自拍.jpg"), "btns": [T("Save Next to Original", "存到原图旁边")], "tint": 0,
                     "body": [{"t": "panes", "on": 1, "panes": [[{"t": "html", "html": id_photo("white")}], [{"t": "html", "html": id_photo("blue")}],
                                                                [{"t": "html", "html": id_photo("red")}]]},
                              {"t": "seg", "label": T("Background", "底色"), "items": [T("White", "白底"), T("Blue", "蓝底"), T("Red", "红底")], "on": 1, "ctl": 0},
                              {"t": "html", "html": both(id_size_row, T("1-inch", "一寸"), T("Also save a 6-inch print sheet", "另存 6 寸冲印排版"))},
                              {"t": "note", "text": T("1-inch: 295 × 413 pixels (300 dpi). A copy is saved next to the original, which stays untouched.",
                                                      "一寸 295×413 像素（300 dpi）；另存一份放在原图旁边，原图不动")}]},
            "steps": [
                {"cap": T("Blue background, 1-inch", "蓝底，一寸"), "sub": T("Cut out and cropped around the face, on your Mac.", "在本机抠图，按人脸裁好。"),
                 "acts": [], "hold": 1400},
                {"cap": T("Or white, or red", "也可以换白底、红底"),
                 "acts": [["click", "opt:1.0"], ["wait", 900], ["click", "opt:1.2"], ["wait", 900], ["click", "opt:1.1"]]},
                {"cap": T("Save a copy", "另存一份"),
                 "acts": [["click", "btn:0"], ["close"], ["file", {"name": T("Selfie Blue 1-inch.jpg", "自拍 蓝底 一寸.jpg"), "kind": "photo", "art": "portrait", "at": 1}],
                          ["toast", T("Saved as “Selfie Blue 1-inch.jpg”", "已存成「自拍 蓝底 一寸.jpg」")]]},
            ],
        },
    },
    "cropImage": {
        "chips": ["1:1 · 4:3 · 16:9", "3:4 · 9:16", T("Centered on the subject", "对准主体")],
        "points": [
            T("Crop the selected images to <b>1:1, 4:3, 3:4, 16:9 or 9:16</b>, taking the largest area with that ratio.",
              "把选中的图片裁成 <b>1:1、4:3、3:4、16:9 或 9:16</b>，在这个比例下裁出最大的一块。"),
            T("The crop is centered on the subject, which Pop finds on your Mac; nothing is uploaded.", "自动对准画面里的主体，在本机找，不上传。"),
            T("Each copy is saved next to its original, named like “Beach 16x9.jpg”; images that already have that ratio are left alone.",
              "每张另存一份「原名 16比9.jpg」放在原图旁边，原图不动；本来就是这个比例的不再另存。"),
        ],
        "scene": {
            "src": {"kind": "files", "app": T("Pictures", "图片"), "cap": T("Select images in Finder", "在访达里选中几张图片"),
                    "files": [{"name": T("Beach.jpg", "海边.jpg"), "kind": "photo", "art": "beach", "sel": True},
                              {"name": T("Flower.jpg", "花.jpg"), "kind": "photo", "art": "flower", "sel": True},
                              {"name": T("Mug.jpg", "杯子.jpg"), "kind": "photo", "art": "mug", "sel": True},
                              {"name": T("City.jpg", "城市.jpg"), "kind": "photo", "art": "city"}]},
            "slot": 1,
            "card": {"w": 330, "btns": [T("1:1 Square", "1:1 方形"), "4:3", "3:4", "16:9", "9:16"],
                     "body": [{"t": "text", "text": T("Crop 3 images to which ratio?", "把 3 张图片裁成哪种比例？")},
                              {"t": "note", "text": T("Crops the largest area with this ratio, centered on the subject. A copy is saved next to the original, which stays untouched.",
                                                      "在这个比例下裁出最大的一块，自动对准画面里的主体；另存一份放在原图旁边，原图不动")}]},
            "steps": [
                {"cap": T("Pick a ratio", "选一个比例"), "acts": [["hover", "btn:3"]], "hold": 1100},
                {"cap": T("Copies appear next to the originals", "裁好的出现在原图旁边"), "sub": T("Each one centered on its subject.", "每张都对准自己的主体。"),
                 "acts": [["click", "btn:0"], ["close"],
                          ["file", {"name": T("Beach 1x1.jpg", "海边 1比1.jpg"), "kind": "photo", "art": "beach", "at": 1}],
                          ["file", {"name": T("Flower 1x1.jpg", "花 1比1.jpg"), "kind": "photo", "art": "flower", "at": 3}],
                          ["file", {"name": T("Mug 1x1.jpg", "杯子 1比1.jpg"), "kind": "photo", "art": "mug", "at": 5}],
                          ["toast", T("Cropped 3 images to 1:1 Square", "已把 3 张裁成 1:1 方形")]]},
            ],
        },
    },
    "redact": {
        "chips": [T("Faces", "人脸"), T("Phone numbers, emails", "电话、邮箱"), T("ID and card numbers", "证件号、银行卡号")],
        "points": [
            T("Finds <b>faces, phone numbers, email addresses, ID and bank card numbers and license plates</b> in the selected images and pixelates them.",
              "找出选中图片里的<b>人脸、电话号码、邮箱、身份证号、银行卡号和车牌</b>，打上马赛克。"),
            T("ID and bank card numbers must pass their checksums, so order numbers and other long numbers are left alone.",
              "身份证号和银行卡号要校验通过才算，订单号这类长数字不会被误伤。"),
            T("The card previews the result first; Also Redact All Text covers every piece of text in the image too.",
              "卡片上先预览打好码的样子；点「文字也全部打码」，图里的文字也全部打上码。"),
            T("Recognized on your Mac. The copy, “Name redacted”, carries no capture info or location, and the original is untouched.",
              "在本机识别；另存的「原名 打码」不带拍摄信息和位置，原图不动。"),
        ],
        "scene": {
            "src": {"kind": "files", "app": T("Desktop", "桌面"), "cap": T("Select a screenshot or photo", "选中截图或照片"),
                    "files": [{"name": T("Delivery.png", "外卖.png"), "kind": "photo", "art": "doc", "sel": True}, {"name": "IMG_2041.HEIC", "kind": "photo", "art": "sunset"},
                              {"name": T("Notes.txt", "笔记.txt")}]},
            "card": {"w": 330, "btns": [T("Save Next to Original", "存到原图旁边"), T("Also Redact All Text", "文字也全部打码")], "tint": 0,
                     "body": [{"t": "panes", "panes": [[{"t": "img", "art": "doc", "ar": "16/10", "over": T(delivery("en", False), delivery("zh", False))}],
                                                       [{"t": "img", "art": "doc", "ar": "16/10", "over": T(delivery("en", True), delivery("zh", True))}]]},
                              {"t": "note", "text": T("Found Faces: 1, Phone numbers: 1, Email: 1. The preview is already pixelated; saving makes a copy and leaves the original untouched.",
                                                      "找到人脸 1 处、电话号码 1 处、邮箱 1 处，预览里已经打上马赛克；存的时候另存一份，原图不动")}]},
            "steps": [
                {"cap": T("Face and contact details found", "找出人脸和联系方式"), "sub": T("Recognized on your Mac.", "在本机识别。"),
                 "acts": [["wait", 700], ["swap", 0, 1]], "hold": 1500},
                {"cap": T("Save a pixelated copy", "另存一份打好码的"), "sub": T("Without capture info or location.", "不带拍摄信息和位置。"),
                 "acts": [["click", "btn:0"], ["close"], ["file", {"name": T("Delivery redacted.png", "外卖 打码.png"), "kind": "photo", "art": "doc", "at": 1}],
                          ["toast", T("Redacted and saved next to the original", "已打码，另存在原图旁边")]]},
            ],
        },
    },
    "palette": {
        "chips": [T("Largest area first", "按面积排序"), "#E0679B", T("Click to copy", "点一下复制")],
        "points": [
            T("Finds the <b>main colors</b> of the selected image or image file, up to six, from the largest area to the smallest.",
              "找出选中的图片或图片文件里的<b>主要颜色</b>，最多六种，按面积从大到小列出来。"),
            T("Each color shows its share of the picture and its hex value.", "每种颜色写着占多少，还有十六进制色值。"),
            T("Click a swatch, or the copy button beside a value, to copy it.", "点一下色块，或者色值旁边的复制按钮，就复制下来。"),
        ],
        "scene": {
            "src": {"kind": "image", "app": T("Preview", "预览"), "title": T("Sunset.jpg", "日落.jpg"), "art": "sunset"},
            "slot": 3,
            "card": {"w": 420,
                     "body": [{"t": "swatches", "items": [[c, ""] for c, p in SUNSET]},
                              {"t": "rows", "rows": [[T(f"{p}%", f"占 {p}%"), c] for c, p in SUNSET]},
                              {"t": "note", "text": T("Largest area first; click a swatch to copy its value", "按面积从大到小；点色块复制色值")}]},
            "steps": [
                {"cap": T("The main colors, largest first", "主要颜色，按面积排好"), "acts": [], "hold": 1600},
                {"cap": T("Click a swatch to copy it", "点色块就复制"),
                 "acts": [["click", ".pl-sw:nth-child(1) i", ["toast", T("Copied", "已复制")]], ["wait", 300],
                          ["click", ".pl-b-rows .pl-row[data-i=\"3\"] .pl-ib", ["toast", T("Copied", "已复制")]]]},
            ],
        },
    },
    "windowPiP": {
        "chips": [T("Floats above everything", "一直浮在最上面"), T("Up to 4 at once", "最多同时开 4 个"), T("Drag · scroll · double-click", "拖动 · 滚动 · 双击")],
        "points": [
            T("Float a <b>live view of any window</b> in a corner of the screen, above all other windows; it stays in sight when you switch apps or desktops, or go full screen. Keep an eye on a video, a call, a download or a build while you work.",
              "把任意一个窗口的画面<b>实时放进屏幕角落的小窗</b>，一直浮在别的窗口上面，切到别的 App、别的桌面、全屏的 App 里也看得到：边干活边看着视频、会议、下载或者编译的进度。"),
            T("Choose the window in the card: each has a thumbnail, and the one under the pointer comes first. The view keeps the window’s proportions in the bottom-right corner; open another and it stacks above, up to four at once.",
              "先在卡片里选窗口：每个窗口都有缩略图，指针下的那个排第一个。小窗按原来窗口的比例放在屏幕右下角，再开一个就往上摞，最多同时开 4 个。"),
            T("<b>Drag</b> to move it, <b>scroll</b> to resize it (the size is remembered) and <b>double-click</b> to go back to the window, even a minimized one. Right-click to change its size or opacity, or close it.",
              "<b>拖动</b>换位置，<b>滚动</b>换大小（下次还是这么大），<b>双击</b>回到原来的窗口（最小化了也会还原）；右键可以换大小、调透明度、关闭。"),
            T("When the original window closes, the view says so and goes away. It needs the Screen &amp; System Audio Recording permission.",
              "原来的窗口关掉了，小窗说一声就收起。需要「录屏与系统录音」权限。"),
        ],
        "scene": {
            "src": {"kind": "desk", "app": "Pages", "title": T("Q4 plan", "第四季度计划"),
                    "lines": [T("**Goals**", "**目标**"), T("Ship the new onboarding by November", "11 月前上线新的引导流程"),
                              T("The call is still going in another window…", "另一个窗口里还开着会……")]},
            "card": {"w": 400, "at": "center", "btns": [T("Float Window", "放进小窗")], "tint": 0,
                     "body": [{"t": "note", "text": T("Choose a window to float a live view of it in a corner of the screen. Double-click the view to go back to the window",
                                                      "选一个窗口，它的画面会一直浮在屏幕角落；双击小窗回到原来的窗口")},
                              PIP_TILES]},
            "steps": [
                {"cap": T("Choose a window", "选一个窗口"), "sub": T("The one under the pointer comes first.", "指针下的那个排第一个。"),
                 "acts": [["move", ".pl-pipt:nth-child(2)", 0.5, 0.5], ["wait", 400], ["move", ".pl-pipt:nth-child(1)", 0.5, 0.45], ["wait", 300]]},
                {"cap": T("It floats in the corner", "它浮在屏幕角落"), "sub": T("Above every window, even full-screen apps.", "浮在所有窗口上面，全屏的 App 里也在。"),
                 "acts": [["click", ".pl-pipt.is-on", [["close"], ["fx", "start", {"name": "pip", "html": PIP_WINDOWS[0][3], "w": 190,
                                                                                    "title": T("FaceTime — Weekly product sync", "FaceTime 通话 — 产品周会")}]]]],
                 "hold": 1200},
                {"cap": T("Drag it anywhere, scroll to resize", "拖动换位置，滚动换大小"), "sub": T("Double-click it to go back to the window.", "双击回到原来的窗口。"),
                 "acts": [["fx", "hover"], ["fx", "drag", [0.96, 0.1]], ["fx", "grow", 1.25]], "hold": 1000},
                {"cap": T("Right-click for size and opacity", "右键换大小、透明度"),
                 "acts": [["fx", "menu", PIP_MENU], ["click", ".pl-pmenu .i5", ["fx", "alpha", 0.5]]], "hold": 1500},
            ],
        },
    },
    "ruler": {
        "chips": [T("Edge to edge", "边到边"), T("Drag for an area", "拖动量区域"), T("Click to copy", "单击复制")],
        "points": [
            T("<b>Freezes the screen</b>; wherever the pointer rests, Pop measures the distance to the edges around it: up, down, left and right.",
              "把屏幕<b>定格</b>下来，指针停在哪里，就量出那里到上下左右边缘（颜色变化的地方）的距离。"),
            T("Drag to measure an area; its width and height stay on screen until you drag again.", "按住拖动量一块区域的宽高，松开后这块区域留在屏幕上。"),
            T("Click to copy the size, such as “120 × 44” (in points). Press Esc or right-click to exit.",
              "单击复制量到的尺寸（比如「120 × 44」，单位是点），Esc 或右键退出。"),
            T("Needs Screen Recording permission.", "需要「录屏与系统录音」权限。"),
        ],
        "scene": {
            "src": {"kind": "web", "app": "Safari", "url": "localhost:3000/pricing", "pic": "landscape",
                    "cap": T("Open what you want to measure", "打开要量的界面"), "sub": T("Nothing needs to be selected.", "不用选中什么。"),
                    "lines": [T("Pricing", "价格"), T("Simple plans for teams of every size.", "适合各种规模团队的简单方案。")],
                    "more": [T("Start free, upgrade when you need more.", "先免费用，需要时再升级。")]},
            "slot": 6,
            "fx": {"name": "ruler", "box": ".pl-pic"},
            "steps": [
                {"cap": T("Point at it: edge to edge", "指针停住，量到边缘"), "sub": T("Up, down, left and right.", "上下左右都量出来。"),
                 "acts": [["move", ".pl-pic", .4, .45], ["wait", 500], ["move", ".pl-pic", .66, .6], ["wait", 600]]},
                {"cap": T("Drag to measure an area", "拖动量一块区域"), "acts": [["fx", "box", [.16, .2, .3, .1]], ["wait", 500]]},
                {"cap": T("Click to copy the size", "单击复制尺寸"), "sub": T("Esc or a right-click exits.", "Esc 或右键退出。"),
                 "acts": [["click", ".pl-rbox", ["toast", T("Copied", "已复制")]], ["fx", "end"]]},
            ],
        },
    },
}
