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

def desk(c):
    r, zh = c.r, c.zh
    icons = "".join(f'<img src="{r}assets/icons/{k}.png" alt="" width="18" height="18">' for k in APPS)
    alt_stox = "Stox 面板：自选列表和分时图" if zh else "Stox panel with a watchlist and an intraday chart"
    alt_proxi = "Proxi 菜单栏面板：节点列表和延迟" if zh else "Proxi menu bar panel listing nodes and their latency"
    alt_ring = "Pop 的圆盘菜单" if zh else "Pop’s ring menu"
    cap = "真实截图：Proxi 和 Stox 的菜单栏面板，Pop 的圆盘。" if zh else "Real screenshots: the Proxi and Stox menu bar panels, and Pop’s ring."
    return f"""<figure class="desk-wrap">
        <div class="desk">
          <div class="bar" aria-hidden="true">{icons}<span>{"周三 9:41" if zh else "Wed 9:41"}</span></div>
          <div class="p proxi"><img src="{r}assets/img/proxi/panel.webp" alt="{alt_proxi}" width="384" height="722"></div>
          <div class="p stox"><img src="{r}assets/img/stox/detail.webp" alt="{alt_stox}" width="376" height="645"></div>
          <div class="p ring"><picture><source srcset="{r}assets/img/pop/ring-dark.webp" media="(prefers-color-scheme: dark)"><img src="{r}assets/img/pop/ring.webp" alt="{alt_ring}" width="214" height="214"></picture></div>
        </div>
        <figcaption class="desk-cap">{cap}</figcaption>
      </figure>"""

def cards(c):
    r, zh = c.r, c.zh
    out = []
    for k, a in APPS.items():
        bullets = (ZH_BULLETS if zh else EN_BULLETS)[k]
        lis = "".join(f"<li>{b}</li>" for b in bullets)
        if zh:
            meta = f'{a["min"]} 或更新 · Apple 芯片与 Intel 通用 · GPL-3.0'
            b1, b2 = "下载", "了解更多"
            pitch = a["zh"]
        else:
            meta = f'{a["min"]} or later · Universal (Apple silicon and Intel) · GPL-3.0'
            b1, b2 = "Download", "Learn more"
            pitch = a["pitch"]
        out.append(f"""
      <article class="card glass app-{k}">
        <div class="card-top">
          <img src="{r}assets/icons/{k}.png" alt="" width="64" height="64">
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
    h = head(c, title, desc, body_class="home", extra_head=redirect)
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
    facts_html = "".join(f'<div class="fact glass"><h3>{i}{a}</h3><p>{b}</p></div>' for i, a, b in facts)
    h += f"""<main id="main">
  <section class="hero">
    <div class="wrap hero-grid">
      <div>
        <p class="eyebrow">{t("Mac apps by whrss9527", "whrss9527 做的 Mac 应用")}</p>
        <h1>{t("Small, quiet apps that live in your menu bar.", "安静的小工具，<br>住在你的菜单栏里。")}</h1>
        <p class="lede">{t("Four native Swift utilities for macOS: a right-click toolbox, a menu bar manager, stock quotes and a proxy switch. They share one glass look, stay out of the way, and cost nothing.",
                            "四个原生 Swift 写的 macOS 工具：右键工具箱、菜单栏管理、股票行情和代理开关。同一种玻璃质感，不打扰你，也不收钱。")}</p>
        <div class="actions">
          <a class="btn btn-primary" href="#apps">{t("See the apps", "看看这些应用")}</a>
          <a class="btn btn-glass" href="{GH}">{ICON_GH}{t("whrss9527 on GitHub", "GitHub 主页")}</a>
        </div>
      </div>
      {desk(c)}
    </div>
  </section>

  <section class="section-tight" id="apps" aria-labelledby="apps-title">
    <div class="wrap">
      <div class="section-head">
        <h2 id="apps-title">{t("The apps", "应用")}</h2>
        <p>{t("Each one does a single job from the menu bar. Download buttons go to the latest release on GitHub.",
              "每个应用只在菜单栏里做好一件事。下载按钮会打开 GitHub 上的最新版本。")}</p>
      </div>
      <div class="cards">{cards(c)}
      </div>
      <p class="small muted" style="margin-top:20px">{t("Languages: Meno is in English, Simplified and Traditional Chinese. Pop, Stox and Proxi currently have a Simplified Chinese interface.",
                                                          "界面语言：Meno 支持英文、简体中文和繁体中文；Pop、Stox、Proxi 目前是简体中文界面。")}</p>
    </div>
  </section>

  <section class="section" aria-labelledby="shared-title">
    <div class="wrap">
      <div class="section-head">
        <h2 id="shared-title">{t("What they have in common", "它们的共同点")}</h2>
        <p>{t("Native Swift, universal binaries for Apple silicon and Intel, and a glass interface that turns into Liquid Glass on macOS 26.",
              "原生 Swift，Apple 芯片和 Intel 通用，玻璃质感的界面在 macOS 26 上变成 Liquid Glass。")}</p>
      </div>
      <div class="facts">{facts_html}</div>
    </div>
  </section>

  <section class="section-tight" aria-labelledby="about-title">
    <div class="wrap narrow">
      <h2 id="about-title">{t("About", "关于")}</h2>
      <p class="lede" style="margin-top:16px">{t(f'I’m whrss9527, an independent developer. I build these apps for my own Mac first and publish them in the open. I write about how they’re made on <a href="{BLOG}">my blog</a>, and everything else is on <a href="{GH}">GitHub</a>.',
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
