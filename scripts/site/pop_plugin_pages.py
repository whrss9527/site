"""Pop's plugin pages: the gallery at /pop/plugins/, one page per plugin at /pop/plugins/<slug>/,
and the plugins section on the Pop page. Both languages.

The catalog is in pop_plugins.py, the icons in pop_plugin_glyphs.py, and what each page says and
its animation in plugin_data/. The animation runs in assets/pop-plugins.js.
"""
import json

from common import *
import pop_plugins as PP
from pop_plugin_glyphs import svg as glyph_svg, glyph
from plugin_data import T, res, load

import sys as _sys
DATA = load(tolerant="--only" in _sys.argv)

HEAD = lambda r: (f'\n<link rel="stylesheet" href="{r}assets/pop-plugins.css">'
                  f'\n<script src="{r}assets/pop-plugins.js" defer></script>')

ICON_CHEV = '<svg viewBox="0 0 16 16" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="m6 3.5 4.5 4.5L6 12.5"/></svg>'
ICON_BACK = '<svg viewBox="0 0 16 16" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M10 3.5 5.5 8l4.5 4.5"/></svg>'
ICON_SEARCH = '<svg viewBox="0 0 16 16" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"><circle cx="7" cy="7" r="4.6"/><path d="m10.5 10.5 3.5 3.5"/></svg>'
ICON_SPARK = '<svg viewBox="0 0 16 16" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><path d="m3.5 8.5 3 3 6-7"/></svg>'

# What a plugin handles (PluginInfo.accepts), as people would say it.
ACCEPTS = {
    "text": T("Selected text", "选中的文字"),
    "foreignText": T("Text in another language", "外文"),
    "number": T("Numbers", "数字"),
    "json": T("JSON", "JSON"),
    "url": T("Links", "链接"),
    "image": T("Images", "图片"),
    "imageFile": T("Image files", "图片文件"),
    "files": T("Files and folders", "文件和文件夹"),
}
ALWAYS = T("Always available, nothing to select", "随时可用，不用选中内容")

# Captions for the chapters every animation shares.
SEL_CAP = {
    "text": T("Select the text", "选中文字"),
    "web": T("Select it on the page", "在网页上选中"),
    "files": T("Select it in Finder", "在访达里选中"),
    "image": T("Select the image", "选中图片"),
    "desk": T("No need to select anything", "什么都不用选"),
}
SEL_SUB_DESK = T("It works wherever you are.", "在哪儿都能用。")
HOLD_CAP = T("Hold the right mouse button", "按住鼠标右键")
HOLD_SUB = T("About a quarter of a second. A short click still opens the usual menu.", "大约 0.25 秒。轻点一下还是平常的右键菜单。")
RING_CAP = T("Swipe to “%s” and let go", "划向「%s」，松开")
RING_SUB = T("It sits on the ring where you put it, and it’s always in All Actions.", "它在圆盘上你放的那一格，「全部功能」里也随时找得到。")


def L(c, x):
    return res(x, c.lang)


def tile(p, cls=""):
    return f'<span class="ptile cat-{p.cat}{(" " + cls) if cls else ""}" aria-hidden="true">{glyph_svg(p.id)}</span>'


def cat_tile(key):
    # A category's tile shows its first plugin's icon.
    p = PP.in_cat(key)[0]
    return tile(p)


def plugin_url(c, p):
    return c.link(f"pop/plugins/{p.slug}/")


def entry(p):
    """The page content for a plugin: from plugin_data, or a plain fallback."""
    d = DATA.get(p.id)
    if d:
        return d
    kind = "files" if ("files" in p.accepts or "imageFile" in p.accepts) else "text" if p.accepts else "desk"
    src = {"kind": kind}
    if kind == "text":
        src.update(app="Notes", lines=[T("# Notes", "# 笔记"), T("Some [[sample text]] to work on.", "一段[[示例文字]]。")])
    if kind == "files":
        src.update(files=[{"name": "Sample.txt", "sel": True}, {"name": "Notes.md"}])
    return {
        "chips": [p.en, T("Pop plugin", "Pop 插件"), T("Free", "免费")],
        "points": [T(p.en_sum + ".", p.zh_sum + "。")],
        "scene": {"src": src, "card": {"body": [{"t": "text", "text": T(p.en_sum, p.zh_sum)}]},
                  "steps": [{"cap": T("See the result", "看结果"), "acts": []}]},
    }


def captions(c, p, d):
    sc = d["scene"]
    src = sc.get("src", {})
    kind = src.get("kind", "desk")
    caps = []
    sel = src.get("cap") or SEL_CAP.get(kind, SEL_CAP["desk"])
    sub = src.get("sub") or (SEL_SUB_DESK if kind in ("desk", "none") and not src.get("cap") else None)
    caps.append((L(c, sel), L(c, sub) if sub else ""))
    caps.append((L(c, HOLD_CAP), L(c, HOLD_SUB)))
    caps.append((L(c, RING_CAP).replace("%s", L(c, sc["label"]) if sc.get("label") else p.name(c.lang)), L(c, sc.get("ring_sub") or RING_SUB)))
    for st in sc.get("steps") or [{"cap": T("See the result", "看结果")}]:
        caps.append((L(c, st.get("cap", "")), L(c, st.get("sub", "")) if st.get("sub") else ""))
    return caps


def scene_json(c, p, d):
    sc = res(d["scene"], c.lang)
    # Captions live in the page; the player only needs the choreography.
    sc = json.loads(json.dumps(sc))
    for k in ("cap", "sub"):
        sc.get("src", {}).pop(k, None)
    sc.pop("ring_sub", None)
    for st in sc.get("steps", []):
        st.pop("cap", None)
        st.pop("sub", None)
    data = {"name": p.name(c.lang), "glyph": glyph(p.id), "scene": sc}
    return json.dumps(data, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")


def art(c, p, d):
    chips = "".join(f'<span class="pa-chip c{i + 1}{" is-mono" if isinstance(x, str) and x[:1] in "<{#0123456789$/" else ""}"><i></i>{L(c, x)}</span>'
                    for i, x in enumerate(d.get("chips", [])[:3]))
    rings = '<i></i><i></i><i></i><b style="--a:40deg;--r:41%"></b><b style="--a:220deg;--r:51%"></b>'
    return (f'<div class="pa cat-{p.cat}" aria-hidden="true"><div class="pa-glow"></div><div class="pa-rings">{rings}</div>'
            f'{tile(p)}{chips}</div>')


def howto(c, p, d):
    caps = captions(c, p, d)
    lis = "".join(f'<li><span class="pla-st"><span><strong>{t}</strong>{f"<small>{s}</small>" if s else ""}</span></span></li>' for t, s in caps)
    note = c.t(f"An animated demo of {p.en} appears here when JavaScript is on; the steps beside it say the same.",
               f"打开 JavaScript 后，这里会播放「{p.zh}」的动画演示；旁边的步骤说的是同一件事。")
    return (f'<div class="howto cat-{p.cat}"><ol class="pla-steps">{lis}</ol>'
            f'<figure class="pla" data-lang="{c.lang}" data-icon="{c.to("assets/icons/pop.png")}">'
            f'<script type="application/json" class="pla-data">{scene_json(c, p, d)}</script>'
            f'<noscript><div class="demo-nojs glass"><img src="{c.to("assets/icons/pop.png")}" alt="" width="40" height="40"><p>{note}</p></div></noscript>'
            f'</figure></div>')


def plugin_nav(c, here=""):
    """The sticky bar on plugin pages: Pop, Plugins, section links and Download."""
    t = c.t
    links = []
    if here == "plugin":
        links = [("how", t("How to use", "怎么用")), ("details", t("Details", "功能")), ("install", t("Install", "安装"))]
    elif here == "gallery":
        links = [("how", t("How plugins work", "插件怎么用")), ("all", t("All plugins", "全部插件"))]
    ln = "".join(f'<a href="#{i}">{l}</a>' for i, l in links)
    return f"""<nav class="localnav" aria-label="{t("Pop plugins", "Pop 插件")}">
  <div class="wrap">
    <a class="ln-title" href="{c.link("pop/")}"><img src="{c.to("assets/icons/pop.png")}" alt="" width="24" height="24"><span>Pop</span></a>
    <a class="ln-sub" href="{c.link("pop/plugins/")}"{' aria-current="page"' if here == "gallery" else ""}>{t("Plugins", "插件")}</a>
    <div class="ln-links">{ln}</div>
    <a class="btn btn-primary btn-xs" href="{dl_url("pop")}" aria-label="{t("Download Pop", "下载 Pop")}">{t("Download", "下载")}</a>
  </div>
</nav>
"""


def card(c, p, h="h3"):
    keys = " ".join([p.en, p.zh, p.en_sum, p.zh_sum, p.id, p.slug, PP.cat_name(p.cat, "en"), PP.cat_name(p.cat, "zh")])
    keys = keys.replace('"', "")
    return (f'<a class="plg-card glass cat-{p.cat}" href="{plugin_url(c, p)}" data-cat="{p.cat}" data-k="{keys}">'
            f'{tile(p)}<div><{h}>{p.name(c.lang)}</{h}><p>{p.summary(c.lang)}</p></div>'
            f'<svg class="go" viewBox="0 0 16 16" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M3 8h10M9 4l4 4-4 4"/></svg></a>')


def marquee(c, rows=3):
    """All plugins as a wall of chips, drifting sideways row by row. Each row is doubled for a seamless
    loop; the copy is hidden from assistive tech and the tab order."""
    # Deal the categories out in turn, so neighbours have different colours.
    queues = [list(PP.in_cat(k)) for k in PP.CAT_KEYS]
    ps = []
    while any(queues):
        for q in queues:
            if q:
                ps.append(q.pop(0))
    out = []
    for i in range(rows):
        row = ps[i::rows]
        items = "".join(f'<a href="{plugin_url(c, p)}">{tile(p, "is-sm")}{p.name(c.lang)}</a>' for p in row)
        dup = "".join(f'<a href="{plugin_url(c, p)}" aria-hidden="true" tabindex="-1">{tile(p, "is-sm")}{p.name(c.lang)}</a>' for p in row)
        out.append(f'<div class="plm-row" style="--dur:{110 + i * 18}s">{items}{dup}</div>')
    return f'<div class="plm" role="list" aria-label="{c.t("Pop plugins", "Pop 插件")}">' + "".join(out) + "</div>"


def cat_links(c):
    return '<div class="pop-plugins-cats">' + "".join(
        f'<a class="cat-{k}" href="{c.link("pop/plugins/")}#{k}"><i></i>{PP.cat_name(k, c.lang)}<span>{len(PP.in_cat(k))}</span></a>'
        for k in PP.CAT_KEYS) + "</div>"


def pop_section(c):
    """The plugins section on the Pop page."""
    n = len(PP.PLUGINS)
    t = c.t
    return f"""  <section class="section pop-plugins" id="plugins" aria-labelledby="plugins-title">
    <div class="wrap">
      <div class="section-head rv">
        <p class="eyebrow">{t("Plugins", "插件")}</p>
        <h2 id="plugins-title">{t("A plugin for almost everything", "要什么，装什么")}</h2>
        <p>{t(f"{n} tools come as plugins: translate a screenshot, record the screen, make a chart, test a disk. Install the ones you use in a few seconds, from Settings or straight from the ring, and uninstall them when you’re done.",
               f"{n} 个工具做成了插件：截图翻译、录屏、生成图表、磁盘测速……用得上的几秒就装好，在设置里装、在圆盘上直接装都行，不用了随时卸载。")}</p>
      </div>
    </div>
    <div class="rv">{marquee(c)}</div>
    <div class="wrap rv">
      {cat_links(c)}
      <div class="actions"><a class="btn btn-primary btn-lg" href="{c.link("pop/plugins/")}">{t(f"Browse all {n} plugins", f"看看全部 {n} 个插件")}</a></div>
    </div>
  </section>

"""


# ------------------------------------------------------------------ the gallery
HOW = [
    ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 3.5v11M7.5 10l4.5 4.5 4.5-4.5M4.5 17.5v1.5a1.5 1.5 0 0 0 1.5 1.5h12a1.5 1.5 0 0 0 1.5-1.5v-1.5"/></svg>',
     T("Install in seconds", "几秒装好"),
     T("Under Plugins at the top of Settings › Actions, click Install. It downloads from Pop’s GitHub release and works right away, without a restart.",
       "在「设置 → 功能」最上面的「插件」里点「安装」：从 Pop 的 GitHub 发布页下载，装好就能用，不用重启。")),
    ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="8.5"/><circle cx="12" cy="12" r="3"/><path d="M12 3.5v5.5M12 15v5.5M3.5 12H9M15 12h5.5"/></svg>',
     T("Or right from the ring", "在圆盘上直接装"),
     T("Search All Actions on the ring: plugins you haven’t installed are listed after your actions. Click one and it installs, then runs on what you selected.",
       "在圆盘的「全部功能」里搜：没装的插件列在后面，点一下就装上，接着处理你选中的内容。")),
    ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M20 12a8 8 0 1 1-2.3-5.6"/><path d="M20.5 4.5v4h-4"/></svg>',
     T("Kept up to date", "跟着更新"),
     T("When Pop updates, installed plugins are replaced with the matching new versions. With iCloud sync on, what you install syncs to your other Macs.",
       "Pop 更新后，装着的插件自动换成对应的新版本；打开 iCloud 同步的话，装了哪些会同步到你的其他 Mac。")),
    ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 7h14M10 7V5h4v2M7 7l.8 12.5h8.4L17 7"/></svg>',
     T("Gone when you’re done", "不用就卸载"),
     T("Each plugin shows its download size and the space it takes. Uninstall deletes the plugin and its settings and takes it off the ring.",
       "每个插件都标着下载多大、装好后占多大。卸载时连同它的设置一起删掉，圆盘上的这一格也拿掉。")),
]


def gallery(lang):
    c = Ctx("/pop/plugins/", lang)
    t = c.t
    r = c.r
    n = len(PP.PLUGINS)
    title = t(f"Pop plugins · {n} tools, installed when you need them", f"Pop 插件 · {n} 个工具，要用时再装")
    desc = t(f"All {n} plugins for Pop, the right-click toolbox for the Mac: text, conversion, developer tools, screen and images, recording and presenting, files and system. Each with a short animated how-to.",
             f"Pop（Mac 上的右键工具箱）的全部 {n} 个插件：文字、转换、开发、屏幕与图片、录屏和演示、文件和系统。每个都有一段怎么用的动画。")
    h = head(c, title, desc, body_class="app-pop app-page plg-page", extra_head=HEAD(r))
    h += header(c, "pop")
    h += plugin_nav(c, "gallery")
    tiles = "".join(f'<div class="tile glass">{ic}<h3>{L(c, a)}</h3><p>{L(c, b)}</p></div>' for ic, a, b in HOW)
    chips = (f'<button type="button" class="plg-chip" data-cat="all" aria-pressed="true">{t("All", "全部")}<span>{n}</span></button>' +
             "".join(f'<button type="button" class="plg-chip cat-{k}" data-cat="{k}" aria-pressed="false"><i></i>{PP.cat_name(k, lang)}<span>{len(PP.in_cat(k))}</span></button>'
                     for k in PP.CAT_KEYS))
    groups = ""
    for k in PP.CAT_KEYS:
        cards = "".join(card(c, p) for p in PP.in_cat(k))
        groups += f"""
      <section class="plg-group cat-{k}" id="{k}" aria-labelledby="{k}-title">
        <div class="plg-gh rv">{cat_tile(k)}<div><h2 id="{k}-title">{PP.cat_name(k, lang)}</h2><p>{PP.cat_blurb(k, lang)}</p></div></div>
        <div class="plg-grid">{cards}</div>
      </section>"""
    h += f"""<main id="main">
  <section class="plg-hero">
    <div class="wrap">
      <p class="eyebrow hero-in">{t("Pop plugins", "Pop 插件")}</p>
      <h1 class="hero-in">{t(f'<span class="plg-count-big">{n}</span> plugins. Install the ones you need.', f'<span class="plg-count-big">{n}</span> 个插件，要用哪个装哪个')}</h1>
      <p class="lede hero-in">{t("Pop keeps its download small: many of its tools are separate plugins. Install one in a few seconds, use it from the ring, and remove it when you’re done. Every plugin is free.",
                                 "Pop 本身很小：很多工具是单独的插件。用得上的几秒就装好，在圆盘上一划就用，不用了就卸载。所有插件都免费。")}</p>
      <div class="actions hero-in">
        <a class="btn btn-primary btn-lg" href="{dl_url("pop")}">{ICON_DL}{t("Download Pop", "下载 Pop")}</a>
        <a class="btn btn-glass btn-lg" href="#all">{t("Browse the plugins", "逛逛插件")}</a>
      </div>
    </div>
  </section>
  <div class="hero-desk">{marquee(c)}</div>

  <section class="section-tight" id="how" aria-labelledby="how-title">
    <div class="wrap">
      <div class="section-head rv"><h2 id="how-title">{t("How plugins work", "插件怎么用")}</h2>
        <p>{t("A plugin is a tool that isn’t part of the Pop download. Once installed, it works like any other action: on the ring, in All Actions, with a shortcut or a <code>pop://</code> link.",
              "插件是不跟着 Pop 一起下载的工具。装好以后和别的功能一样用：放上圆盘、在「全部功能」里找、设快捷键，或者用 <code>pop://</code> 链接调用。")}</p></div>
      <div class="plg-how rv-group">{tiles}</div>
    </div>
  </section>

  <div class="plg" id="all">
    <div class="plg-ctl" hidden>
      <div class="wrap">
        <div class="plg-chips" role="group" aria-label="{t("Category", "分类")}">{chips}</div>
        <label class="plg-search">{ICON_SEARCH}<input type="search" class="plg-q" placeholder="{t("Search plugins", "搜索插件")}" aria-label="{t("Search plugins", "搜索插件")}" autocomplete="off"></label>
        <span class="plg-count" aria-live="polite" data-n="{t("%s plugins", "%s 个插件")}" data-one="{t("1 plugin", "1 个插件")}"></span>
      </div>
    </div>
    <div class="wrap">{groups}
      <p class="plg-empty" hidden>{t("No plugin matches. Try another word, or write your own: a plugin can be one JSON file.", "没有对得上的插件。换个词试试，或者自己写一个：一个 JSON 文件就是一个插件。")}</p>
    </div>
  </div>

  <section class="section cta" aria-labelledby="cta-title">
    <div class="wrap rv-group">
      <img class="cta-icon" src="{r}assets/icons/pop.png" alt="" width="96" height="96">
      <h2 id="cta-title">{t("Your own, too", "也可以自己写")}</h2>
      <p class="lede">{t("Turn a URL template, a shell script, JavaScript or a Shortcut into a tool on the ring, or install one from the plugin library.",
                         "把网址模板、shell 脚本、JavaScript 或快捷指令变成圆盘上的工具，或者从插件库装别人写好的。")}</p>
      <div class="actions">
        <a class="btn btn-primary btn-lg" href="{dl_url("pop")}">{ICON_DL}{t("Download Pop", "下载 Pop")}</a>
        <a class="btn btn-glass btn-lg" href="{repo_url("pop")}/blob/main/docs/{t("guide.md#custom-plugins", "guide.zh-CN.md")}">{ICON_GH}{t("Plugin guide", "插件说明")}</a>
      </div>
    </div>
  </section>
</main>
"""
    h += footer(c)
    write(c.out_file, h)


# ------------------------------------------------------------------ one plugin
def plugin_page(p, lang, prev, nxt):
    c = Ctx(f"/pop/plugins/{p.slug}/", lang)
    t = c.t
    r = c.r
    d = entry(p)
    name = p.name(lang)
    title = t(f"{name} · a Pop plugin", f"{name} · Pop 插件")
    h = head(c, title, p.summary(lang), body_class=f"app-pop app-page plp-page cat-{p.cat}", extra_head=HEAD(r))
    h += header(c, "pop")
    h += plugin_nav(c, "plugin")
    works = ", ".join(L(c, ACCEPTS[a]) for a in p.accepts) if p.accepts else L(c, ALWAYS)
    if lang == "zh":
        works = works.replace(", ", "、")
    points = "".join(f'<div class="plp-point glass"><span class="n">{ICON_SPARK}</span><p>{L(c, x)}</p></div>' for x in d.get("points", []))
    fid = p.funcs[0]
    link = f"pop://run?plugin={fid}"
    more = [q for q in PP.in_cat(p.cat) if q.id != p.id][:6]
    more_cards = "".join(card(c, q, "h3") for q in more)
    h += f"""<main id="main">
  <section class="plp-hero">
    <div class="wrap">
      <div class="hero-copy">
        <nav class="crumbs" aria-label="{t("Breadcrumb", "位置")}"><a href="{c.link("pop/")}">Pop</a>{ICON_CHEV}<a href="{c.link("pop/plugins/")}">{t("Plugins", "插件")}</a>{ICON_CHEV}<a href="{c.link("pop/plugins/")}#{p.cat}">{PP.cat_name(p.cat, lang)}</a></nav>
        <p class="plp-cat">{t("Pop plugin", "Pop 插件")} · {PP.cat_name(p.cat, lang)}</p>
        <h1>{name}</h1>
        <p class="lede">{p.summary(lang)}{t(".", "。")}</p>
        <div class="plp-meta"><span><b>{t("Works with", "处理")}</b> {works}</span><span>{t("Free", "免费")}</span></div>
        <div class="actions">
          <a class="btn btn-primary btn-lg" href="#how">{t("See how it works", "看看怎么用")}</a>
          <a class="btn btn-glass btn-lg" href="{dl_url("pop")}">{ICON_DL}{t("Download Pop", "下载 Pop")}</a>
        </div>
      </div>
      <div class="plp-art">{art(c, p, d)}</div>
    </div>
  </section>

  <section class="section-tight" id="how" aria-labelledby="how-title">
    <div class="wrap">
      <div class="howto-h rv"><h2 id="how-title">{t("How to use it", "怎么用")}</h2>
        <p>{t("Select something, hold the right mouse button, swipe. The animation plays the steps one after another; click a step to see it again.",
              "选中内容，按住右键，一划。动画按步骤播放，点一下某一步可以从那里重看。")}</p></div>
      {howto(c, p, d)}
    </div>
  </section>

  <section class="section-tight" id="details" aria-labelledby="details-title">
    <div class="wrap">
      <div class="section-head rv"><h2 id="details-title">{t("What it does", "能做什么")}</h2></div>
      <div class="plp-details rv-group">{points}</div>
    </div>
  </section>

  <section class="section-tight" id="install" aria-labelledby="install-title">
    <div class="wrap">
      <div class="section-head rv"><h2 id="install-title">{t("Install it", "安装")}</h2>
        <p>{t("Plugins aren’t part of the Pop download. Install this one when you need it.", "插件不跟着 Pop 一起下载，要用时再装。")}</p></div>
      <div class="plp-install rv-group">
        <div class="plp-way glass"><h3><span>1</span>{t("From Settings", "在设置里装")}</h3>
          <p>{t(f"In Pop’s Settings › Actions, find “{name}” under Plugins at the top and click Install. It downloads from Pop’s GitHub release in a few seconds and works right away, without a restart.",
                f"在 Pop 的「设置 → 功能」最上面的「插件」里找到「{name}」，点「安装」：从 Pop 的 GitHub 发布页下载，几秒就好，装好就能用，不用重启。")}</p></div>
        <div class="plp-way glass"><h3><span>2</span>{t("Or from the ring", "或者在圆盘上装")}</h3>
          <p>{t(f"Open All Actions on the ring and search for “{name}”. Plugins that aren’t installed are listed after your actions: click it to install, and it runs right away if it can handle what you selected.",
                f"在圆盘的「全部功能」里搜「{name}」：没装的插件列在后面，点一下就装上，能处理当前选中的内容时直接运行。")}</p></div>
        <div class="plp-way glass"><h3><span>3</span>{t("Then use it your way", "然后，怎么顺手怎么用")}</h3>
          <p>{t("Put it on the ring in Settings › Ring, give it a shortcut, or run it from Shortcuts and scripts with its link:",
                "在「设置 → 圆盘」里把它放上圆盘、给它设个快捷键，或者在快捷指令和脚本里用它的链接：")}</p>
          <div class="cmd"><code>{link}</code><button type="button" class="btn btn-glass btn-xs copy" data-copy="{link}" data-done="{t("Copied", "已复制")}" hidden>{t("Copy", "复制")}</button></div></div>
      </div>
      <p class="note rv">{t("Uninstall it from the same list when you no longer need it: the plugin and its settings are deleted. After Pop updates, installed plugins are updated with it, and with iCloud sync on, what you install syncs to your other Macs.",
                            "不用了在同一个列表里点「卸载」，插件和它的设置一起删掉。Pop 更新后，装着的插件会跟着换成新版本；打开 iCloud 同步的话，装了哪些会同步到你的其他 Mac。")}</p>
    </div>
  </section>

  <section class="section-tight" aria-labelledby="more-title">
    <div class="wrap">
      <div class="section-head rv"><h2 id="more-title">{t("More in", "更多")}{t(" ", "")}{PP.cat_name(p.cat, lang)}</h2></div>
      <div class="plg-grid rv-group">{more_cards}</div>
      <nav class="plp-nav rv" aria-label="{t("Previous and next plugin", "上一个和下一个插件")}" style="margin-top:28px">
        <a class="glass prev cat-{prev.cat}" href="{plugin_url(c, prev)}"><span class="arr">{ICON_BACK}</span>{tile(prev, "is-sm")}<span><small>{t("Previous", "上一个")}</small><strong>{prev.name(lang)}</strong></span></a>
        <a class="glass next cat-{nxt.cat}" href="{plugin_url(c, nxt)}"><span class="arr">{ICON_CHEV}</span>{tile(nxt, "is-sm")}<span><small>{t("Next", "下一个")}</small><strong>{nxt.name(lang)}</strong></span></a>
      </nav>
      <p class="small muted" style="margin-top:28px;text-align:center"><a href="{c.link("pop/plugins/")}">{t(f"All {len(PP.PLUGINS)} plugins", f"全部 {len(PP.PLUGINS)} 个插件")}</a> · <a href="{c.link("pop/")}">{t("About Pop", "关于 Pop")}</a> · <a href="{repo_url("pop")}/issues">{t("Pop issues on GitHub", "GitHub 上的 Pop issue")}</a></p>
    </div>
  </section>
</main>
"""
    h += footer(c)
    write(c.out_file, h)


def pages():
    """English paths of every page made here, for the sitemap."""
    return ["/pop/plugins/"] + [f"/pop/plugins/{p.slug}/" for p in PP.PLUGINS]


def build_all():
    ps = PP.PLUGINS
    import plugin_check
    problems, missing = plugin_check.check_all(DATA, ps)
    if missing:
        print(f"plugin pages: no plugin_data entry for {len(missing)} plugin(s), using a plain page: " + ", ".join(missing))
    if problems:
        raise SystemExit("plugin pages:\n  " + "\n  ".join(problems))
    for lang in ("en", "zh"):
        gallery(lang)
        for i, p in enumerate(ps):
            plugin_page(p, lang, ps[i - 1], ps[(i + 1) % len(ps)])


def build_only(ids):
    """Checks and writes just these plugins' pages, in both languages: for working on a few
    entries (python3 scripts/site/pop_plugin_pages.py --only qrCode,hash). build.py builds everything."""
    import plugin_check
    ps = PP.PLUGINS
    problems = []
    for pid in ids:
        if pid not in PP.BY_ID:
            problems.append(f"{pid}: not in the catalog")
        elif pid not in DATA:
            problems.append(f"{pid}: no plugin_data entry")
        else:
            problems += plugin_check.check(pid, DATA[pid], PP.BY_ID[pid])
    if problems:
        raise SystemExit("plugin pages:\n  " + "\n  ".join(problems))
    for lang in ("en", "zh"):
        for i, p in enumerate(ps):
            if p.id in ids:
                plugin_page(p, lang, ps[i - 1], ps[(i + 1) % len(ps)])


if __name__ == "__main__":
    if "--only" in _sys.argv:
        build_only(_sys.argv[_sys.argv.index("--only") + 1].split(","))
    else:
        build_all()
