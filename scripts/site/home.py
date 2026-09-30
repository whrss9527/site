from common import *

ICON_SHIELD = '<svg viewBox="0 0 20 20" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M10 2.5 4 4.8v4.6c0 3.8 2.6 6.6 6 8.1 3.4-1.5 6-4.3 6-8.1V4.8L10 2.5Z"/><path d="m7.3 10 1.9 1.9 3.6-3.8"/></svg>'
ICON_UPDATE = '<svg viewBox="0 0 20 20" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M16 10a6 6 0 1 1-1.8-4.3"/><path d="M16.2 3.5v3h-3"/><path d="M10 7v3.4l2 1.3"/></svg>'
ICON_LOCK = '<svg viewBox="0 0 20 20" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="4" y="9" width="12" height="8.5" rx="2"/><path d="M6.8 9V6.6a3.2 3.2 0 0 1 6.4 0V9"/></svg>'
ICON_CODE = '<svg viewBox="0 0 20 20" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m7 6-4 4 4 4M13 6l4 4-4 4"/></svg>'

EN_BULLETS = {
    "pop": ["Translate a selection with Apple's on-device translation, AI or DeepL",
            "A ring of tools you arrange: conversions, OCR, color, JSON, files",
            "Clipboard history, pinned screenshots, plugins and AI with your own endpoint"],
    "meno": ["Visible, Hidden and a Stash for icons you almost never need",
             "Shelf and Quick Open in Liquid Glass on macOS 26",
             "Rules, scenes and a one-key Zen mode for talks and recordings"],
    "stox": ["China A-shares, Hong Kong and US stocks, plus indexes, funds and forex",
             "Holdings and P&L, price alerts, iCloud sync",
             "Right-click the menu bar icon to hide every number"],
    "proxi": ["System proxy, environment variables, git and npm in one switch",
              "Built-in mihomo core: subscriptions, rules, policy groups",
              "LAN sharing for consoles and phones, TUN and gateway modes"],
}
ZH_BULLETS = {
    "pop": ["选中外文直接翻译：系统离线翻译、AI 或 DeepL", "圆盘里的功能随你摆：换算、识字、取色、JSON、文件", "剪贴板历史、贴图、插件，AI 用你自己的接口"],
    "meno": ["显示、隐藏，再加一个放几乎用不到图标的暗格", "托盘和快速打开，macOS 26 上是 Liquid Glass", "规则、场景，一键禅模式，演示录屏更干净"],
    "stox": ["A 股、港股、美股，还有指数、基金和外汇", "持仓与盈亏、价格提醒、iCloud 同步", "右键点一下菜单栏图标，数字全部藏起来"],
    "proxi": ["系统代理、环境变量、git、npm 一个开关", "内置 mihomo 内核：订阅、分流规则、策略组", "局域网共享给游戏机和手机，增强模式与网关模式"],
}

def reel(c):
    """The hero: the four apps as live demos (assets/<app>-demo.js, sample data) in a row you can swipe."""
    from apps import pop_demo, meno_demo, stox_demo, proxi_demo
    r, zh, t = c.r, c.zh, c.t
    lang = "zh" if zh else "en"
    meno_nojs = (f'<div class="demo-nojs glass"><img src="{r}assets/icons/meno.png" alt="" width="40" height="40"><p>'
                 + t("An interactive demo of Meno with sample data appears here when JavaScript is on.",
                     "这里是 Meno 的可交互演示（示例数据），打开 JavaScript 就能试用。") + "</p></div>")
    demos = {
        "pop": pop_demo(r, lang, "ring", desk=True),
        "meno": meno_demo(r, lang, "layout", meno_nojs),
        "stox": stox_demo(r, lang, "list", desk=True),
        "proxi": proxi_demo(r, lang, "panel"),
    }
    blurbs = {
        "pop": t("Hold the right button. Swipe to a tool.", "按住右键，一划选中工具。"),
        "meno": t("A calm menu bar. Icons on call.", "安静的菜单栏，图标随叫随到。"),
        "stox": t("Quotes at a glance. Gone in one click.", "一眼看盘，一键隐身。"),
        "proxi": t("One switch for every proxy.", "一个开关，管好所有代理。"),
    }
    cards = "".join(f"""
          <article class="reel-card glass app-{k}" aria-labelledby="reel-{k}">
            <header>
              <img src="{r}assets/icons/{k}.png" alt="" width="44" height="44">
              <div><h2 id="reel-{k}">{a["name"]}</h2><p>{blurbs[k]}</p></div>
              <a class="reel-more" href="{c.link(k + "/")}" aria-label="{t("Learn more about " + a["name"], "了解 " + a["name"])}">{t("Learn more", "了解更多")}<span aria-hidden="true"> ›</span></a>
            </header>
            <div class="reel-demo">{demos[k]}</div>
          </article>""" for k, a in APPS.items())
    label = t("The four apps, as interactive demos", "四个应用的可交互演示")
    prev, nxt = t("Previous app", "上一个应用"), t("Next app", "下一个应用")
    return f"""<div class="reel" role="region" aria-label="{label}" tabindex="-1">{cards}
        </div>
        <div class="reel-nav" hidden>
          <button type="button" class="reel-btn" data-dir="-1" aria-label="{prev}"><svg viewBox="0 0 16 16" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M10 3 5 8l5 5"/></svg></button>
          <button type="button" class="reel-btn" data-dir="1" aria-label="{nxt}"><svg viewBox="0 0 16 16" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="m6 3 5 5-5 5"/></svg></button>
        </div>"""

def cards(c):
    r, zh = c.r, c.zh
    out = []
    for k, a in APPS.items():
        bullets = (ZH_BULLETS if zh else EN_BULLETS)[k]
        lis = "".join(f"<li>{b}</li>" for b in bullets)
        if zh:
            meta = f'{a["min"]} 或更新 · Apple 芯片与 Intel 通用 · GPL\u20113.0'
            b1, b2 = "下载", "了解更多"
            pitch = a["zh"]
        else:
            meta = f'{a["min"]} or later · Universal (Apple silicon and Intel) · GPL\u20113.0'
            b1, b2 = "Download", "Learn more"
            pitch = a["pitch"]
        out.append(f"""
      <article class="card glass app-{k}" data-p>
        <div class="card-top">
          <img class="float" src="{r}assets/icons/{k}.png" alt="" width="64" height="64">
          <div>
            <h3><a href="{c.link(k + "/")}">{a["name"]}</a></h3>
            <p class="pitch">{pitch}</p>
          </div>
        </div>
        <ul>{lis}</ul>
        <p class="meta">{meta}</p>
        <div class="actions">
          <a class="btn btn-primary btn-sm" href="{dl_url(k)}" aria-label="{b1} {a["name"]}">{ICON_DL}{b1}</a>
          <a class="btn btn-glass btn-sm" href="{c.link(k + "/")}" aria-label="{b2}: {a["name"]}">{b2}</a>
        </div>
      </article>""")
    return "".join(out)

def page(zh):
    c = Ctx("/", "zh" if zh else "en")
    r = c.r
    if zh:
        title = "whrss · 住在菜单栏里的 Mac 小工具"
        desc = "Pop、Meno、Stox、Proxi：原生 Swift 编写的 macOS 菜单栏应用，开源免费，经过苹果公证，一键更新。"
    else:
        title = "whrss · Mac apps for the menu bar"
        desc = "Pop, Meno, Stox and Proxi: native Swift menu bar apps for macOS. Free and open source, notarized by Apple, with one-click updates."
    # English home only: a visitor who chose Chinese in the language menu goes to /zh/.
    # Never guessed from the browser language.
    redirect = "" if zh else ('\n<script>try{if(localStorage.getItem("%s")==="zh")location.replace("zh/"+location.search+location.hash)}catch(e){}</script>' % LANG_KEY)
    demo_head = "".join(f'\n<link rel="stylesheet" href="{r}assets/{k}-demo.css">\n<script src="{r}assets/{k}-demo.js" defer></script>' for k in APPS)
    h = head(c, title, desc, body_class="home", extra_head=redirect + demo_head)
    h += header(c)
    t = c.t
    facts = [
        (ICON_SHIELD, t("Signed and notarized", "签名并经过公证"),
         t("Current releases are signed with a Developer ID and notarized by Apple. Download, unzip, double-click.",
           "现在发布的版本都用 Developer ID 签名并通过苹果公证。下载、解压、双击就能打开。")),
        (ICON_UPDATE, t("Updates itself", "一键更新"),
         t("Each app checks GitHub Releases, verifies the SHA-256 checksum and code signature, replaces itself and relaunches.",
           "直接从 GitHub Releases 检查新版本，比对 SHA-256 校验和与代码签名，替换后自动重新打开。")),
        (ICON_LOCK, t("Private by default", "数据留在你这儿"),
         t("No accounts, no analytics, no servers of mine. Your data stays on your Mac or in your own iCloud.",
           "不用注册，没有统计，也没有我的服务器。数据只在你的 Mac 或你自己的 iCloud 里。")),
        (ICON_CODE, t("Open source", "开源"),
         t("All four are free software under GPL-3.0. Read the code, build it yourself, send a fix.",
           "四个应用都以 GPL-3.0 开源。可以读代码、自己编译，也欢迎提交修改。")),
    ]
    facts_html = "".join(f'<div class="fact glass"><span class="fact-icon">{i}</span><h3>{a}</h3><p>{b}</p></div>' for i, a, b in facts)
    h += f"""<main id="main">
  <section class="hero">
    <div class="wrap hero-center">
      <p class="eyebrow hero-in">{t("Mac apps by whrss9527", "whrss9527 做的 Mac 应用")}</p>
      <h1 class="hero-in">{t("Small, quiet apps that live in your menu bar.", "安静的小工具，<br>住在你的菜单栏里。")}</h1>
      <p class="lede hero-in">{t("Four native Swift utilities for macOS: a right-click toolbox, a menu bar manager, stock quotes and a proxy switch. They share one glass look, stay out of the way, and cost nothing.",
                          "四个原生 Swift 写的 macOS 工具：右键工具箱、菜单栏管理、股票行情和代理开关。同一种玻璃质感，不打扰你，也不收钱。")}</p>
      <div class="actions hero-in">
        <a class="btn btn-primary btn-lg" href="#apps">{t("See the apps", "看看这些应用")}</a>
        <a class="btn btn-glass btn-lg" href="{GH}">{ICON_GH}{t("whrss9527 on GitHub", "GitHub 主页")}</a>
      </div>
    </div>
    <div class="hero-desk">
      {reel(c)}
    </div>
  </section>

  <section class="section" id="apps" aria-labelledby="apps-title">
    <div class="wrap">
      <div class="section-head center rv">
        <h2 id="apps-title">{t("The apps", "应用")}</h2>
        <p>{t("Each one does a single job from the menu bar. Download buttons go to the latest release on GitHub.",
              "每个应用只在菜单栏里做好一件事。下载按钮会打开 GitHub 上的最新版本。")}</p>
      </div>
      <div class="cards rv-group">{cards(c)}
      </div>
    </div>
  </section>

  <section class="section" aria-labelledby="shared-title">
    <div class="wrap">
      <div class="section-head center rv">
        <h2 id="shared-title">{t("What they have in common", "它们的共同点")}</h2>
        <p>{t("Native Swift, universal binaries for Apple silicon and Intel, and a glass interface that turns into Liquid Glass on macOS 26.",
              "原生 Swift，Apple 芯片和 Intel 通用，玻璃质感的界面在 macOS 26 上变成 Liquid Glass。")}</p>
      </div>
      <div class="facts bento rv-group">{facts_html}</div>
    </div>
  </section>

  <section class="section about" aria-labelledby="about-title">
    <div class="wrap narrow rv-group">
      <h2 id="about-title">{t("About", "关于")}</h2>
      <p class="statement">{t(f'I’m whrss9527, an independent developer. I build these apps for my own Mac first and publish them in the open. I write about how they’re made on <a href="{BLOG}">my blog</a>, and everything else is on <a href="{GH}">GitHub</a>.',
                                                 f'我是 whrss9527，一名独立开发者。这些应用先是给自己的 Mac 做的，然后公开发布。做它们的过程写在<a href="{BLOG}">博客</a>里，代码都在 <a href="{GH}">GitHub</a> 上。')}</p>
      <p style="margin-top:16px" class="muted">{t(f'Questions or bugs: see <a href="{c.link("support/")}">Support</a>, or write to <a href="mailto:{EMAIL}">{EMAIL}</a>.',
                                                  f'有问题或者发现了 bug：看看<a href="{c.link("support/")}">支持页面</a>，或者写信到 <a href="mailto:{EMAIL}">{EMAIL}</a>。')}</p>
    </div>
  </section>
</main>
"""
    h += footer(c)
    write(c.out_file, h)


def build():
    page(False)
    page(True)


if __name__ == "__main__":
    build()
