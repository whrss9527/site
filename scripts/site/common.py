"""Shared pieces for every page: <head>, header with the language menu, footer.

Every page exists twice: in English at /<path> and in Simplified Chinese at
/zh/<path>. A page is described by a Ctx: its English path and its language.
All links are relative, so the site also works from a local folder (the 404
page is the exception: it is served at any depth, so it uses absolute paths).
"""
import os
import posixpath

SITE = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
ORIGIN = "https://whrss.com"
EMAIL = "whrss9527@gmail.com"
GH = "https://github.com/whrss9527"
BLOG = "https://blog.whrss.com"
LANG_KEY = "lang"   # localStorage key for the visitor's chosen language ("en" or "zh")

APPS = {
    "pop":   {"name": "Pop",   "repo": "pop",   "min": "macOS 15", "pitch": "Long-press right click: translate, convert and 80+ tools in one swipe.", "zh": "长按右键，一划即达：翻译、换算和 80 多个小工具。"},
    "meno":  {"name": "Meno",  "repo": "meno",  "min": "macOS 14", "pitch": "A calm menu bar, made with glass: hide, stash and call back icons.", "zh": "安静的菜单栏，由玻璃打造：隐藏、收起、随时唤回图标。"},
    "stox":  {"name": "Stox",  "repo": "stox",  "min": "macOS 13", "pitch": "A-share, Hong Kong and US quotes at a glance; gone in one click.", "zh": "A 股、港股、美股，一眼看盘，一键隐身。"},
    "proxi": {"name": "Proxi", "repo": "proxi", "min": "macOS 14", "pitch": "One switch for system proxy, shell, git and npm, with a built-in mihomo core.", "zh": "一个开关管好系统代理、终端、git 和 npm，内置 mihomo 内核。"},
}

ICON_DL = '<svg viewBox="0 0 16 16" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><path d="M8 2.5v8M4.5 7 8 10.5 11.5 7M3 13.5h10"/></svg>'
ICON_GH = '<svg viewBox="0 0 16 16" aria-hidden="true" fill="currentColor"><path d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0 0 16 8c0-4.42-3.58-8-8-8Z"/></svg>'
ICON_GLOBE = '<svg class="globe" viewBox="0 0 20 20" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><circle cx="10" cy="10" r="7.5"/><path d="M2.5 10h15M10 2.5c2 2.1 3 4.6 3 7.5s-1 5.4-3 7.5c-2-2.1-3-4.6-3-7.5s1-5.4 3-7.5Z"/></svg>'
ICON_CHECK = '<svg class="check" viewBox="0 0 16 16" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="m3.5 8.5 3 3 6-7"/></svg>'

LANGS = [("en", "en", "English"), ("zh", "zh-CN", "简体中文")]


class Ctx:
    """One page in one language.

    en_path: the English URL path, e.g. "/", "/pop/", "/privacy/pop/".
    lang: "en" or "zh".
    absolute: use root-relative links (for the 404 page).
    """

    def __init__(self, en_path, lang="en", absolute=False):
        self.en_path = en_path
        self.lang = lang
        self.zh = lang == "zh"
        self.absolute = absolute

    def path_for(self, lang):
        return self.en_path if lang == "en" else "/zh" + self.en_path

    @property
    def path(self):
        return self.path_for(self.lang)

    @property
    def html_lang(self):
        return "zh-CN" if self.zh else "en"

    @property
    def depth(self):
        return self.path.strip("/").count("/") + 1 if self.path.strip("/") else 0

    @property
    def r(self):
        """Prefix from this page to the site root."""
        if self.absolute:
            return "/"
        return "../" * self.depth if self.depth else "./"

    def to(self, site_path):
        """Link to a site-root path (no leading slash), as is: assets, or explicit targets."""
        if not site_path and not self.absolute:
            return self.r
        return self.r + site_path

    def page(self, path):
        """Relative link from this page to the page at an absolute site path ("/zh/pop/")."""
        if self.absolute:
            return path
        rel = posixpath.relpath(path, self.path)
        return "./" if rel == "." else rel + "/"

    def link(self, en_path):
        """Link to a page in this page's language. en_path has no leading slash: "", "pop/"."""
        return self.page(("/zh/" if self.zh else "/") + en_path)

    def counterpart(self, lang):
        return self.page(self.path_for(lang))

    def t(self, en, zh):
        return zh if self.zh else en

    @property
    def out_file(self):
        return self.path.lstrip("/") + "index.html"


def dl_url(key):
    return f"{GH}/{APPS[key]['repo']}/releases/latest"


def repo_url(key):
    return f"{GH}/{APPS[key]['repo']}"


def head(c, title, desc, body_class="", alternates=True, extra_head=""):
    r = c.r
    canon = ORIGIN + c.path
    alts = ""
    if alternates:
        alts = (f'\n<link rel="alternate" hreflang="en" href="{ORIGIN}{c.path_for("en")}">'
                f'\n<link rel="alternate" hreflang="zh-CN" href="{ORIGIN}{c.path_for("zh")}">'
                f'\n<link rel="alternate" hreflang="x-default" href="{ORIGIN}{c.path_for("en")}">')
    # Open Graph image (assets/og/, rendered by scripts/og/render.js): the app's own for an app page,
    # the home page's for everything else.
    og = c.en_path.strip("/") if c.en_path.strip("/") in APPS else "home"
    name = APPS[og]["name"] if og in APPS else "whrss"
    og_alt = c.t(f"{name}: an interactive recreation of the app, with sample data" if og in APPS else "Pop, Meno, Stox and Proxi, Mac apps for the menu bar",
                 f"{name}：应用界面的可交互还原，示例数据" if og in APPS else "Pop、Meno、Stox、Proxi：住在菜单栏里的 Mac 应用")
    return f"""<!doctype html>
<html lang="{c.html_lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<script>document.documentElement.classList.add("js");setTimeout(function(){{if(!window.__motion)document.documentElement.classList.add("rv-done")}},3000)</script>{extra_head}
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="color-scheme" content="light dark">
<meta name="theme-color" content="#f2f3f5" media="(prefers-color-scheme: light)">
<meta name="theme-color" content="#121315" media="(prefers-color-scheme: dark)">
<link rel="canonical" href="{canon}">{alts}
<meta property="og:type" content="website">
<meta property="og:locale" content="{c.t("en_US", "zh_CN")}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{canon}">
<meta property="og:image" content="{ORIGIN}/assets/og/{og}-{c.lang}.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="{og_alt}">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="{r}assets/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="{r}assets/apple-touch-icon.png">
<link rel="stylesheet" href="{r}assets/site.css">
<script src="{r}assets/site.js" defer></script>
<script src="{r}assets/motion.js" defer></script>
</head>
<body class="{body_class}">
"""


def lang_option(c, code, hreflang, label, cls=""):
    """A link to this page in another language. data-lang makes site.js remember the choice."""
    cur = ' aria-current="true"' if code == c.lang else ""
    return (f'<a{cls} href="{c.counterpart(code)}" hreflang="{hreflang}" lang="{hreflang}" data-lang="{code}"{cur}>'
            f'<span>{label}</span>{ICON_CHECK}</a>')


def lang_menu(c):
    """Globe button in the header; a <details> menu, so it works without JavaScript."""
    current = dict((code, label) for code, _, label in LANGS)[c.lang]
    label = c.t(f"Language: {current}", f"语言：{current}")
    opts = "\n        ".join(lang_option(c, code, hl, name) for code, hl, name in LANGS)
    return f"""<details class="lang-menu">
      <summary aria-label="{label}" title="{c.t("Language", "语言")}">{ICON_GLOBE}<span class="lang-code" aria-hidden="true">{c.t("EN", "中文")}</span></summary>
      <div class="panel lang-list" role="group" aria-label="{c.t("Language", "语言")}">
        {opts}
      </div>
    </details>"""


def header(c, current=""):
    zh = c.zh
    items = []
    for k, a in APPS.items():
        cur = ' aria-current="page"' if current == k else ""
        items.append(f'<a href="{c.link(k + "/")}"{cur}><img src="{c.to("assets/icons/" + k + ".png")}" alt="" width="18" height="18">{a["name"]}</a>')
    support_cur = ' aria-current="page"' if current == "support" else ""
    tail = [
        f'<a href="{BLOG}">{c.t("Blog", "博客")}</a>',
        f'<a href="{c.link("support/")}"{support_cur}>{c.t("Support", "支持")}</a>',
        f'<a href="{GH}">GitHub</a>',
    ]
    nav = "\n    ".join(items) + '\n    <span class="sep" aria-hidden="true"></span>\n    ' + "\n    ".join(tail)
    other = "zh" if not zh else "en"
    other_hl, other_label = {"en": ("en", "English"), "zh": ("zh-CN", "简体中文")}[other]
    menu_lang = (f'<span class="sep" aria-hidden="true"></span>\n    '
                 f'<a class="lang-link" href="{c.counterpart(other)}" hreflang="{other_hl}" lang="{other_hl}" data-lang="{other}">{ICON_GLOBE}{other_label}</a>')
    nav_label = c.t("Main", "主导航")
    return f"""<a class="skip" href="#main">{c.t("Skip to content", "跳到正文")}</a>
<header class="menubar">
  <div class="wrap">
    <a class="brand" href="{c.link("")}"><span class="brand-mark" aria-hidden="true"><span></span></span>whrss</a>
    <nav class="nav" aria-label="{nav_label}">
    {nav}
    </nav>
    {lang_menu(c)}
    <details class="nav-menu">
      <summary>{c.t("Menu", "菜单")}</summary>
      <nav class="panel nav-list" aria-label="{nav_label}">
    {nav}
    {menu_lang}
      </nav>
    </details>
  </div>
</header>
"""


def local_nav(c, key):
    """App pages: a second, sticky bar with the app's name, section links and Download
    (like the product bars on apple.com). The global header above it scrolls away."""
    t = c.t
    a = APPS[key]
    links = "".join(f'<a href="#{i}">{l}</a>' for i, l in (
        ("features", t("Features", "功能")), ("specs", t("Specs", "规格")), ("faq", t("Questions", "常见问题"))))
    return f"""<nav class="localnav" aria-label="{a['name']}">
  <div class="wrap">
    <a class="ln-title" href="#main"><img src="{c.to("assets/icons/" + key + ".png")}" alt="" width="24" height="24"><span>{a['name']}</span></a>
    <div class="ln-links">{links}</div>
    <a class="btn btn-primary btn-xs" href="{dl_url(key)}" aria-label="{t('Download ' + a['name'], '下载 ' + a['name'])}">{t("Download", "下载")}</a>
  </div>
</nav>
"""


def footer(c):
    t = c.t
    apps = "".join(f'<li><a href="{c.link(k + "/")}">{a["name"]}</a></li>' for k, a in APPS.items())
    priv = "".join(f'<li><a href="{c.link("privacy/" + k + "/")}">{a["name"]}</a></li>' for k, a in APPS.items())
    langs = "".join(f"<li>{lang_option(c, code, hl, name)}</li>" for code, hl, name in LANGS)
    return f"""<footer class="footer">
  <div class="wrap">
    <div class="footer-grid">
      <div>
        <h2>whrss</h2>
        <p>{t("Native Mac apps for the menu bar. Free and open source.", "住在菜单栏里的原生 Mac 小工具，开源免费。")}</p>
      </div>
      <div>
        <h2>{t("Apps", "应用")}</h2>
        <ul>{apps}</ul>
      </div>
      <div>
        <h2>{t("Privacy", "隐私政策")}</h2>
        <ul>{priv}</ul>
      </div>
      <div>
        <h2>{t("More", "更多")}</h2>
        <ul>
          <li><a href="{c.link("support/")}">{t("Support", "支持")}</a></li>
          <li><a href="{BLOG}">{t("Blog", "博客")}</a></li>
          <li><a href="{GH}">GitHub</a></li>
          <li><a href="mailto:{EMAIL}">{EMAIL}</a></li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom">
      <p class="fine">© 2026 whrss9527. {t("This site uses no cookies, no analytics and no third-party requests.", "本站不使用 Cookie，不做统计，也不从第三方加载任何内容。")}</p>
      <nav class="footer-lang" aria-label="{t("Language", "语言")}">{ICON_GLOBE}<ul>{langs}</ul></nav>
    </div>
  </div>
</footer>
</body>
</html>
"""


def write(path, html):
    full = os.path.join(SITE, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(html)
    print("wrote", path)
