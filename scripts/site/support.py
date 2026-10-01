import json

from common import *

TIPS = {
    "pop": ("Right-click does nothing after an update? Settings › General › “Clear old authorization records”, then grant Accessibility again.",
            "更新后右键没反应？打开设置 › 通用，点“清除旧的授权记录”，再重新授予辅助功能权限。"),
    "meno": ("Not responding after an update? Settings › Permissions › “Reset and Grant Again”. For a report, use Settings › About › Copy Diagnostic Report.",
             "更新后没反应？打开设置 › 权限，点“清除并重新授权”。反馈问题时，可以用设置 › 关于 › 复制诊断报告。"),
    "stox": ("Quotes not updating? Check the note at the bottom of the panel; Stox switches to its backup source automatically.",
             "行情不刷新？看看面板底部的提示；主数据源出问题时，Stox 会自动切换到备用数据源。"),
    "proxi": ("Proxy not working? Click the speedometer in the panel to test every profile. Settings › Diagnose shows the proxy settings across the system and opens the folder with <code>proxi.log</code>.",
              "代理不好用？点面板里的测速按钮测试全部配置。设置 › 诊断会列出系统里各处的代理设置，还能打开存放 <code>proxi.log</code> 的文件夹。"),
}


def support(zh):
    c = Ctx("/support/", "zh" if zh else "en")
    t = c.t
    r = c.r
    h = head(c, t("Support · whrss apps", "支持 · whrss 的应用"),
             t("How to get help with Pop, Meno, Stox and Proxi: GitHub issues, email, and fixes for common problems.",
               "Pop、Meno、Stox 和 Proxi 的求助方式：GitHub issue、邮件，以及常见问题的解决办法。"),
             body_class="home")
    h += header(c, "support")
    cards = ""
    for k, tips in TIPS.items():
        a = APPS[k]
        tip = tips[1] if zh else tips[0]
        cards += f"""
        <div class="help glass app-{k}">
          <div class="help-top"><img src="{r}assets/icons/{k}.png" alt="" width="40" height="40"><h3>{a['name']}</h3></div>
          <p>{tip}</p>
          <div class="links">
            <a href="{repo_url(k)}/issues/new">{t("Report a problem", "报告问题")}</a>
            <a href="{repo_url(k)}/issues">{t("Known issues", "已知问题")}</a>
            <a href="{repo_url(k)}/releases">{t("Release notes", "更新说明")}</a>
            <a href="{c.link(k + "/")}#faq-title">{t("FAQ", "常见问题")}</a>
            <a href="{c.link("privacy/" + k + "/")}">{t("Privacy", "隐私政策")}</a>
          </div>
        </div>"""
    email_en = f'For questions you’d rather not post publicly, security reports, or anything about privacy and your data: <a href="mailto:{EMAIL}">{EMAIL}</a>. I read everything; replies may take a few days. English or Chinese is fine.'
    email_zh = f'不想公开的问题、安全问题报告，以及和隐私、个人数据有关的事，请写信到 <a href="mailto:{EMAIL}">{EMAIL}</a>。每封信我都会看，回复可能要等几天。中文、英文都可以。'
    h += f"""<main id="main">
  <section class="doc">
    <div class="wrap">
      <header class="doc-head narrow hero-copy" style="padding:0">
        <h1>{t("Support", "支持")}</h1>
        <p class="lede">{t("The fastest way to get help is an issue on GitHub — it’s public, so the answer helps the next person too. For anything private, write to me.",
                           "求助最快的办法是在 GitHub 上提 issue：它是公开的，答案也能帮到后来的人。不方便公开的事，可以给我写信。")}</p>
      </header>
      <div class="help-grid rv-group">{cards}
      </div>

      <div class="info-grid rv-group" style="margin-top:28px">
        <div class="panel-block glass">
          <h2>{t("Email", "邮件")}</h2>
          <p class="muted" style="color:var(--text-2)">{t(email_en, email_zh)}</p>
        </div>
        <div class="panel-block glass">
          <h2>{t("A good report includes", "好的问题报告包括")}</h2>
          <ol class="steps">
            <li>{t("The app version (in its Settings or About page) and your macOS version.", "应用的版本号（在它的设置或“关于”页面里）和 macOS 版本。")}</li>
            <li>{t("Apple silicon or Intel.", "Apple 芯片还是 Intel。")}</li>
            <li>{t("What you did, what you expected, and what happened instead.", "你做了什么、预期是什么、实际发生了什么。")}</li>
            <li>{t("A screenshot or screen recording if it’s visual.", "和界面有关的问题，附上截图或录屏。")}</li>
          </ol>
        </div>
      </div>

      <div class="panel-block glass rv" style="margin-top:20px">
        <h2>{t("Before you write", "写信之前")}</h2>
        <ol class="steps">
          <li>{t("<strong>Update first.</strong> Each app can update itself; the fix may already be out.",
                 "<strong>先更新。</strong>每个应用都能自己更新，问题可能已经修好了。")}</li>
          <li>{t("<strong>Permissions after an update.</strong> If an app that uses Accessibility (Pop, Meno) stops responding, remove it from System Settings › Privacy &amp; Security › Accessibility and add it again, or use the reset button in the app.",
                 "<strong>更新后的权限问题。</strong>用到辅助功能权限的应用（Pop、Meno）如果没反应，到系统设置 › 隐私与安全性 › 辅助功能里把它移除再重新添加，或者用应用里的重置按钮。")}</li>
          <li>{t("<strong>“Can’t be opened” warnings.</strong> Current releases are notarized and open with a double-click. Very old versions were not: right-click the app and choose Open, or download the latest release.",
                 "<strong>提示“无法打开”。</strong>现在发布的版本都经过公证，双击就能打开。很早的版本没有公证：右键点应用选“打开”，或者下载最新版本。")}</li>
        </ol>
      </div>
    </div>
  </section>
</main>
"""
    h += footer(c)
    write(c.out_file, h)


# The 404 page in Chinese: English text node (trimmed) -> Chinese, and attribute values.
NOTFOUND_ZH_TEXT = {
    "Skip to content": "跳到正文", "Blog": "博客", "Support": "支持", "Menu": "菜单", "EN": "中文",
    "This page isn’t in the menu bar.": "菜单栏里没有这一页。",
    "It may have moved, or the link is wrong. Maybe you were looking for one of these:": "它可能搬走了，也可能是链接写错了。你也许在找这些：",
    "Home": "首页",
    "Looking for an old blog post? The blog now lives at": "在找以前的博客文章？博客已经搬到了",
    ".": "。",
    "Native Mac apps for the menu bar. Free and open source.": "住在菜单栏里的原生 Mac 小工具，开源免费。",
    "Apps": "应用", "Privacy": "隐私政策", "More": "更多",
    "© 2026 whrss9527. This site uses no cookies, no analytics and no third-party requests.": "© 2026 whrss9527. 本站不使用 Cookie，不做统计，也不从第三方加载任何内容。",
}
NOTFOUND_ZH_ATTR = {"Main": "主导航", "Language": "语言", "Language: English": "语言：简体中文"}


def notfound():
    """One 404 page for both languages. GitHub Pages serves it at any path, so links are absolute.

    It is written in English; under /zh/ the script after the footer switches
    its text and links to Chinese. The script in <main>, which sends old blog
    addresses to blog.whrss.com, must keep its behaviour exactly.
    """
    c = Ctx("/", "en", absolute=True)
    h = head(c, "Page not found · whrss", "This page doesn’t exist.", body_class="home", alternates=False)
    # Not a translated pair: canonical stays on /404.html.
    h = h.replace(f'<link rel="canonical" href="{ORIGIN}/">', f'<link rel="canonical" href="{ORIGIN}/404.html">')
    h = h.replace(f'<meta property="og:url" content="{ORIGIN}/">', f'<meta property="og:url" content="{ORIGIN}/404.html">')
    h = h.replace('\n<meta property="og:locale" content="en_US">', "")
    h += header(c)
    h += """<main id="main">
  <section class="lost">
    <div class="wrap hero-copy">
      <p class="code" aria-hidden="true">404</p>
      <h1>This page isn’t in the menu bar.</h1>
      <p>It may have moved, or the link is wrong. Maybe you were looking for one of these:</p>
      <div class="actions">
        <a class="btn btn-primary" href="/">Home</a>
        <a class="btn btn-glass" href="/pop/">Pop</a>
        <a class="btn btn-glass" href="/meno/">Meno</a>
        <a class="btn btn-glass" href="/stox/">Stox</a>
        <a class="btn btn-glass" href="/proxi/">Proxi</a>
      </div>
      <p class="small muted" style="margin-top:22px">Looking for an old blog post? The blog now lives at <a id="blog-link" href="https://blog.whrss.com">blog.whrss.com</a>.</p>
      <script>
        (function () {
          var p = location.pathname;
          if (p && p !== "/" && p !== "/404.html") {
            var target = "https://blog.whrss.com" + p + location.search + location.hash;
            // Addresses that only ever existed on the old blog go straight to it.
            if (/^\\/(posts|post|feed|rss|atom|tags?|categor(y|ies)|archives?|page|search)(\\/|\\.|$)/.test(p)) {
              location.replace(target);
              return;
            }
            var a = document.getElementById("blog-link");
            a.href = target;
            a.textContent = "blog.whrss.com" + p;
          }
        })();
      </script>
    </div>
  </section>
</main>
"""
    h += footer(c)
    # After the footer, so the whole page has been parsed.
    swap = """<script>
        (function () {
          // Under /zh/, show this page in Chinese: swap the text and point links at the Chinese pages.
          if (!/^\\/zh(\\/|$)/.test(location.pathname)) return;
          var T = %s, A = %s;
          document.documentElement.lang = "zh-CN";
          document.title = "找不到页面 · whrss";
          var w = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT), n, s;
          while ((n = w.nextNode())) {
            s = n.nodeValue.trim();
            if (n.parentNode.nodeName !== "SCRIPT" && Object.prototype.hasOwnProperty.call(T, s)) n.nodeValue = n.nodeValue.replace(s, T[s]);
          }
          document.querySelectorAll("[aria-label],[title]").forEach(function (e) {
            ["aria-label", "title"].forEach(function (k) {
              var v = e.getAttribute(k);
              if (v !== null && Object.prototype.hasOwnProperty.call(A, v)) e.setAttribute(k, A[v]);
            });
          });
          document.querySelectorAll("a[href^='/']").forEach(function (a) {
            var l = a.getAttribute("data-lang"), href = a.getAttribute("href");
            if (l === "en") { a.removeAttribute("aria-current"); return; }
            if (l === "zh") { a.setAttribute("aria-current", "true"); return; }
            if (!/^\\/(zh\\/|assets\\/)/.test(href)) a.setAttribute("href", "/zh" + href);
          });
          var m = document.querySelector(".nav-list .lang-link");
          if (m) {
            m.setAttribute("href", "/"); m.setAttribute("hreflang", "en"); m.setAttribute("lang", "en");
            m.setAttribute("data-lang", "en"); m.lastChild.nodeValue = "English";
          }
        })();
</script>
""" % (json.dumps(NOTFOUND_ZH_TEXT, ensure_ascii=False), json.dumps(NOTFOUND_ZH_ATTR, ensure_ascii=False))
    h = h.replace("</footer>\n", "</footer>\n" + swap, 1)
    write("404.html", h)


def build():
    support(False)
    support(True)
    notfound()


if __name__ == "__main__":
    build()
