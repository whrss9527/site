from common import *

UPDATED = "September 30, 2026"
UPDATED_ISO = "2026-09-30"
UPDATED_ZH = "2026 年 9 月 30 日"

def table(head, rows):
    th = "".join(f"<th scope=\"col\">{h}</th>" for h in head)
    trs = "".join("<tr>" + "".join(f'<td data-label="{h}">{c}</td>' for h, c in zip(head, row)) + "</tr>" for row in rows)
    return f'<div class="table-wrap"><table><thead><tr>{th}</tr></thead><tbody>{trs}</tbody></table></div>'

def build(key, d, lang="en"):
    c = Ctx(f"/privacy/{key}/", lang)
    t = c.t
    r = c.r
    a = APPS[key]
    name = a["name"]
    title = t(f"{name} Privacy Policy", f"{name} 隐私政策")
    h = head(c, title, t(f"How {name} for macOS handles your data: {d['meta_desc']}", f"macOS 版 {name} 如何处理你的数据：{d['meta_desc']}"), body_class=f"app-{key}")
    h += header(c, "")
    summary = "".join(f"<li>{s}</li>" for s in d["summary"])
    L = ZH_LABELS if c.zh else EN_LABELS
    when, iso, when_zh = d.get("updated", (UPDATED, UPDATED_ISO, UPDATED_ZH))   # a policy changed on its own keeps its own date
    h += f"""<main id="main">
  <article class="doc">
    <div class="wrap narrow">
      <header class="doc-head hero-copy">
        <div class="icon-row"><img src="{r}assets/icons/{key}.png" alt="" width="48" height="48"><a href="{c.link(key + '/')}">{name}</a></div>
        <h1>{title}</h1>
        <p>{t(f'Last updated <time datetime="{iso}">{when}</time>. Applies to {name} for macOS, version {d["version"]} and later.',
              f'最后更新于 <time datetime="{iso}">{when_zh}</time>。适用于 macOS 版 {name} {d["version"]} 及以后的版本。')}</p>
      </header>

      <section class="summary glass rv" aria-labelledby="sum">
        <h2 id="sum">{t("The short version", "简要说明")}</h2>
        <ul>{summary}</ul>
      </section>

      <div class="prose">
        <h2>{t("Who is responsible", "谁负责")}</h2>
        <p>{t(f'{name} is made and published by whrss9527, an independent developer (“I”, “me”). If you have any question about this policy or your data, email <a href="mailto:{EMAIL}">{EMAIL}</a>.',
              f'{name} 由独立开发者 whrss9527（下称“我”）开发和发布。对本政策或你的数据有任何疑问，请发邮件到 <a href="mailto:{EMAIL}">{EMAIL}</a>。')}</p>

        <h2>{t("What I collect", "我收集什么")}</h2>
        <p>{t(f"<strong>Nothing.</strong> {name} has no analytics, no crash reporting, no advertising, no tracking and no user accounts. I don’t run a server for {name}, so there is nowhere for your data to be sent to me. I never see what you do in the app.",
              f"<strong>什么都不收集。</strong>{name} 没有统计分析，没有崩溃报告，没有广告，没有跟踪，也没有用户账号。我没有为 {name} 运行任何服务器，你的数据根本没有地方可以发给我。我也从来看不到你在应用里做了什么。")}</p>

        <h2>{t("What stays on your Mac", "留在你 Mac 上的数据")}</h2>
        <p>{d['local_intro']}</p>
        {table(L["local"], d['local'])}

        <h2>{t(f"When {name} goes online", f"{name} 什么时候联网")}</h2>
        <p>{d['net_intro']}</p>
        {table(L["network"], d['network'])}
        <p>{t("Like any internet request, these connections reveal your IP address to the server you’re connecting to. Those services are run by third parties under their own privacy policies; I don’t receive anything from them about you.",
              "和所有网络请求一样，这些连接会让对方服务器看到你的 IP 地址。这些服务由第三方运营，适用它们各自的隐私政策；我不会从它们那里收到任何关于你的信息。")}</p>

        {d.get('icloud', '')}

        <h2>{t("Permissions", "权限")}</h2>
        {table(L["permissions"], d['permissions'])}
        <p>{t("You can revoke any of these in System Settings › Privacy &amp; Security at any time.", "这些权限都可以随时在系统设置 › 隐私与安全性里撤销。")}</p>

        {d.get('extra', '')}

        <h2>{t(f"Where you got {name}", f"你从哪里获得 {name}")}</h2>
        <p>{t(f"This policy covers {name} however you obtained it — from GitHub, from this website, or through a store or subscription service such as the Mac App Store or Setapp. Such a service handles your purchase or subscription and may process data under its own privacy policy; {name} itself behaves as described here. If an edition ever works differently, this policy will be updated before that edition is released.",
              f"无论你是从 GitHub、本网站，还是通过 Mac App Store、Setapp 等商店或按期付费的软件服务获得 {name}，本政策都适用。这类服务负责处理你的购买或付费，可能按它们自己的隐私政策处理数据；{name} 本身的行为与本页描述一致。如果将来某个版本的行为有所不同，本政策会在该版本发布之前更新。")}</p>

        <h2>{t("Deleting your data", "删除你的数据")}</h2>
        <p>{d['delete']}</p>

        <h2>{t("Children", "儿童")}</h2>
        <p>{t(f"{name} is a general-purpose utility, not directed at children, and collects no personal information from anyone.",
              f"{name} 是通用工具，并非面向儿童，也不向任何人收集个人信息。")}</p>

        <h2>{t("Changes", "政策变更")}</h2>
        <p>{t(f'If this policy changes, the new version will be published on this page with a new date. {name} is open source, so you can also check its behavior in the <a href="{repo_url(key)}">source code</a>.',
              f'本政策如有变更，新版本会发布在本页并标注新的日期。{name} 是开源软件，你也可以在<a href="{repo_url(key)}">源代码</a>里核对它的行为。')}</p>

        <h2>{t("Contact", "联系方式")}</h2>
        <p>whrss9527 · <a href="mailto:{EMAIL}">{EMAIL}</a> · <a href="{repo_url(key)}/issues">{t(f"{name} issues on GitHub", f"GitHub 上的 {name} issue")}</a></p>
      </div>
    </div>
  </article>
</main>
"""
    h += footer(c)
    write(c.out_file, h)

EN_LABELS = {
    "local": ["Data", "Where it’s kept", "Notes"],
    "network": ["Service", "When", "What is sent"],
    "permissions": ["Permission", "Why"],
}
ZH_LABELS = {
    "local": ["数据", "存放位置", "说明"],
    "network": ["服务", "何时", "发送的内容"],
    "permissions": ["权限", "用途"],
}

GITHUB_UPDATE = lambda name, when, ua: [
    "GitHub (<code>api.github.com</code>, <code>github.com</code> and GitHub’s download servers)",
    when,
    f"A request for the latest release information and, when you install an update, the download of the release archive and its checksum file. The request identifies the app and version (<code>{ua}</code>). Nothing about you or your data is included.",
]

POP = {
    "version": "0.25",
    "meta_desc": "no analytics, no accounts; data stays on your Mac.",
    "summary": [
        "No analytics, no accounts, no ads, and no server of mine. I collect nothing.",
        "Clipboard history, settings and plugins stay on your Mac. API keys are kept in the macOS Keychain.",
        "Your text leaves the Mac only when you use a feature that needs a service you chose: AI (your own endpoint) or DeepL.",
        "Pop contacts GitHub to check for updates and, when you open it, to load the plugin library.",
    ],
    "local_intro": "Pop keeps everything it needs locally. Apple’s on-device translation, the on-device Apple Intelligence model (macOS 26), text recognition in images, and all conversions run on your Mac.",
    "local": [
        ["Settings (ring layout, rules, shortcuts, translation and AI settings without keys)", "<code>UserDefaults</code> (<code>io.github.whrss9527.pop</code>)", "Can be exported to a file you choose."],
        ["Custom plugins", "<code>~/Library/Application Support/Pop/Plugins/</code>", "One JSON file per plugin."],
        ["Clipboard history", "<code>~/Library/Application Support/Pop/Clipboard/</code> (SQLite database and images)", "Includes text recognized in copied images, for search. Deleted automatically by age and count; items marked concealed by password managers are never recorded; you can exclude apps."],
        ["Vocabulary list", "<code>~/Library/Application Support/Pop/Vocabulary.json</code>", "Words you save from translation cards."],
        ["Inbox", "<code>~/Documents/Pop 收集箱.md</code>", "Only if you use the Inbox tool."],
        ["AI API key, DeepL key", "macOS Keychain on this Mac", "Never synced or exported."],
        ["Files received from your phone", "<code>~/Downloads</code>", "Only when you use Send to Phone."],
    ],
    "net_intro": "Pop connects to the following, and only in the situations listed:",
    "network": [
        GITHUB_UPDATE("Pop", "At launch and every 6 hours if “Check for updates automatically” is on (the default; you can turn it off), and when you check manually.", "Pop/&lt;version&gt; (macOS)"),
        ["Plugin library (<code>raw.githubusercontent.com</code>, falling back to <code>cdn.jsdelivr.net</code>)", "When you open the plugin library or install or update a plugin from it.", "A request for the library index and the plugin file. Nothing about you."],
        ["The AI endpoint you configure", "Only when you use an AI feature or an AI plugin.", "The selected text, your instruction and your API key, sent to the address you entered. Plain <code>http://</code> is only allowed for this Mac and your local network. If you use Apple’s on-device model on macOS 26, nothing leaves your Mac."],
        ["DeepL (<code>api.deepl.com</code> or <code>api-free.deepl.com</code>)", "Only when you choose DeepL for a translation.", "The text to translate, the target language and your DeepL key."],
        ["The link you’re expanding", "Only when you use “expand short link”.", "A request to that link and each redirect it leads to, so Pop can show the final address."],
        ["Your own plugins and scripts", "When you run them.", "Whatever the plugin does: open a URL, run a shell script, JavaScript or a Shortcut you wrote or installed. Pop shows shell scripts from the library before installing them, and asks before a <code>pop://</code> link runs one."],
        ["Your phone, on your local network", "Only while Send to Phone is on.", "Pop serves a temporary page on your Wi-Fi, protected by a random token; it stops when you turn sharing off or after 10 idle minutes. Nothing goes through the internet."],
    ],
    "icloud": """<h2>iCloud</h2>
        <p>The builds published on GitHub do not include iCloud sync. In a build that includes it, and only while it’s turned on, Pop stores your settings and custom plugins in your own iCloud key-value storage so your other Macs can read them. Clipboard history, the vocabulary list and API keys are never synced. That data is held by Apple under your iCloud account, and I have no access to it.</p>""",
    "permissions": [
        ["Accessibility (required)", "To notice a long right-click, read the selected text in the app you’re using, and paste results back when you choose “Replace”."],
        ["Screen Recording", "Only for screenshot OCR and translate, QR scanning, annotation and the screen ruler."],
        ["Reminders or Calendar", "Only for “Add to Reminders”, the first time you use it."],
        ["Notifications", "To tell you about a new version and finished timers."],
        ["Local Network", "Only for Send to Phone."],
    ],
    "extra": "<h2>Web searches and links</h2><p>Search, open-link and map tools hand the text or address to your default browser. Pop itself doesn’t contact those sites.</p>",
    "delete": "Clear the clipboard history in Pop, delete the folder <code>~/Library/Application Support/Pop/</code>, and remove the “Pop” items from Keychain Access. Deleting Pop.app and these files removes everything Pop stored.",
}

MENO = {
    "version": "0.10",
    "meta_desc": "no analytics, no accounts; only goes online for updates.",
    "summary": [
        "No analytics, no accounts, no ads, and no server of mine. I collect nothing.",
        "Settings, rules and on-device usage statistics stay on your Mac.",
        "Meno goes online only to ask GitHub for the latest release, and to download one you chose to install.",
    ],
    "local_intro": "Meno keeps its data in a folder on your Mac:",
    "local": [
        ["Settings, layout, rules, scenes, groups", "<code>~/Library/Application Support/Meno/</code>", "Can be exported to a file you choose. Rules with shell commands are turned off when you import a file."],
        ["Insights (how often you reveal items, most used items)", "<code>~/Library/Application Support/Meno/</code>", "Computed and kept on your Mac only."],
        ["Small preferences (e.g. last update check)", "<code>UserDefaults</code> (<code>io.github.whrss9527.meno</code>)", ""],
        ["Images of menu bar items", "Memory only", "With Screen Recording allowed, Meno captures menu bar items to show them in the Shelf and to notice changes. Nothing else on screen is captured and nothing is saved."],
    ],
    "net_intro": "Meno makes one kind of connection:",
    "network": [
        GITHUB_UPDATE("Meno", "When you click Check for Updates, or once a day if you turn on automatic checks in Settings › General; and when you install an update.", "Meno/&lt;version&gt;"),
    ],
    "permissions": [
        ["Accessibility (required)", "To read menu bar items, open them from the Shelf, Quick Open and shortcuts, and arrange them with ⌘-drag."],
        ["Screen Recording (optional)", "To show the real artwork of hidden items and notice when their icons change (macOS 14–26). Only menu bar items are captured."],
    ],
    "extra": """<h2>Rules that look at your Mac</h2>
        <p>Rules about a microphone or camera only ask macOS whether a device is running; Meno never records audio or video. Rules about a network run the system <code>route</code> and <code>arp</code> commands to recognize your router from what macOS already knows, without Location Services and without sending anything. A rule that runs a shell command runs exactly the command you typed, and only while the rule is on.</p>""",
    "delete": "Delete the folder <code>~/Library/Application Support/Meno/</code> and Meno.app. That removes everything Meno stored.",
}

STOX = {
    "version": "0.46",
    "meta_desc": "no analytics, no accounts; quotes from public providers, data on your Mac or in your iCloud.",
    "summary": [
        "No analytics, no accounts, no ads, and no server of mine. I collect nothing.",
        "Your watchlist, holdings, trades and alerts stay on your Mac — and in your own iCloud Drive if you turn on sync.",
        "To show prices, Stox requests quotes for the symbols on your watchlist from Tencent Finance, with Sina Finance as a backup. Your holdings are never sent.",
        "Stox contacts GitHub to check for updates.",
    ],
    "local_intro": "Stox keeps your data on your Mac:",
    "local": [
        ["Watchlist, groups, notes, holdings, trades, dividends, alerts and settings", "<code>UserDefaults</code> (<code>io.github.whrss9527.stox</code>)", "Can be exported to a backup file you choose."],
        ["Log", "<code>~/Library/Application Support/Stox/stox.log</code> and the system log", "Technical messages for troubleshooting; stays on your Mac."],
    ],
    "net_intro": "Stox connects to the following:",
    "network": [
        ["Tencent Finance (<code>qt.gtimg.cn</code>, <code>smartbox.gtimg.cn</code>, <code>web.ifzq.gtimg.cn</code>, <code>proxy.finance.qq.com</code>)", "While Stox is running: every few seconds during trading hours, once a minute when markets are closed; paused while the Mac sleeps. Also when you search, open a chart or the rankings.", "The stock symbols whose quotes or charts are needed, or the search text you type. No holdings, amounts or personal information."],
        ["Sina Finance (<code>hq.sinajs.cn</code>, <code>stock2.finance.sina.com.cn</code>)", "Automatically, as a backup when Tencent’s quotes can’t be reached, and for futures intraday charts.", "The symbols whose quotes are needed."],
        ["Exchange rates (Tencent Finance)", "When you hold stocks in more than one currency.", "A request for USD/CNY and HKD/CNY rates."],
        GITHUB_UPDATE("Stox", "At launch and every 6 hours, unless you turn automatic checks off in About &amp; Updates; and when you install an update.", "Stox/&lt;version&gt; (macOS)"),
        ["Xueqiu and other finance sites", "Only when you choose “View on Xueqiu” (or a similar link) for a stock.", "The page opens in your default browser; Stox itself doesn’t contact the site."],
    ],
    "icloud": """<h2>iCloud</h2>
        <p>If you turn on iCloud sync, Stox writes your watchlist (with groups, short names, holdings and alerts) and a few display settings to a file in your own iCloud Drive, <code>Stox/sync.json</code>, together with your Mac’s name and the time of the change, so your other Macs can merge it. Settings that only concern one Mac are not synced. The file is stored by Apple under your iCloud account; I have no access to it. Turning sync off stops writing; you can delete the file in Finder.</p>""",
    "permissions": [
        ["Notifications", "For price alerts, the optional closing summary and update notices."],
        ["iCloud Drive", "Only if you turn on sync."],
        ["Accessibility, Screen Recording", "Not used. Stox’s global shortcut uses the standard hot-key API, which needs no permission."],
    ],
    "extra": "<h2>Market data</h2><p>Quotes are provided by third parties for reference only. Hong Kong quotes are delayed about 15 minutes. Nothing in Stox is investment advice.</p>",
    "delete": "Use Settings to remove your watchlist, or delete Stox together with <code>~/Library/Preferences/io.github.whrss9527.stox.plist</code> and <code>~/Library/Application Support/Stox/</code>. If you used sync, also delete the <code>Stox</code> folder in iCloud Drive.",
}

PROXI = {
    "version": "0.13",
    "updated": ("October 1, 2026", "2026-10-01", "2026 年 10 月 1 日"),
    "meta_desc": "no analytics, no accounts; it only changes proxy settings on your Mac, and goes online for connection tests and updates.",
    "summary": [
        "No analytics, no accounts, no ads, and no server of mine. I collect nothing.",
        "Proxi provides no proxy service and relays no traffic. It only changes settings on your Mac — the system proxy, Terminal’s environment variables, git and npm — so that they point at a proxy server you choose.",
        "Your profiles and settings stay on your Mac, and in your own iCloud Drive if you turn on sync. Proxy passwords stay in this Mac’s Keychain and are never synced.",
        "Proxi itself goes online only to test a connection through your proxy (by default against apple.com) and to check GitHub for updates.",
    ],
    "local_intro": "Proxi keeps its data in these places on your Mac:",
    "local": [
        ["Profiles (name, color, type, server address, user name, scope, bypass lists) and settings", "<code>~/Library/Application Support/Proxi/config.json</code>", "Passwords are not in this file, only a note that a profile has one."],
        ["Proxy passwords", "Your login Keychain (a generic password for the service <code>com.whrss9527.proxyswitch</code>)", "Stored on this Mac only, not in iCloud Keychain."],
        ["State and log", "<code>~/Library/Application Support/Proxi/</code> (<code>state.json</code>, <code>proxi.log</code>, and the socket <code>control.sock</code> while Proxi runs)", "The state remembers the last profile and the proxy settings from before Proxi turned one on, so they can be restored. Passwords are hidden in the log."],
        ["Small preferences (interface language, skipped update)", "<code>~/Library/Preferences/com.whrss9527.proxyswitch.plist</code>", ""],
        ["Command-line tool, if you install it", "<code>/usr/local/bin/proxi</code> (and <code>/usr/local/bin/proxyswitch</code> if an older version installed it)", "A small script that starts Proxi’s own executable."],
    ],
    "extra": """<h2>Settings Proxi changes</h2>
        <p>When you turn a profile on, Proxi writes its proxy address into the places you chose for it, and clears them again when you turn it off (for the system proxy, you can choose to restore the previous settings instead):</p>
        <ul>
          <li>the system proxy of your network services (with <code>networksetup</code>; macOS keeps a sign-in password for it in the System keychain);</li>
          <li>the <code>http_proxy</code>, <code>https_proxy</code>, <code>all_proxy</code> and <code>no_proxy</code> variables (and their upper-case forms) in your login session (<code>launchctl setenv</code>), which apps and Terminal windows opened afterwards read;</li>
          <li>git’s global <code>http.proxy</code> and <code>https.proxy</code> in <code>~/.gitconfig</code>; for a profile with a password, the address is kept in <code>~/Library/Application Support/Proxi/git-proxy.inc</code>, readable only by you, and <code>~/.gitconfig</code> includes that file;</li>
          <li>the <code>proxy</code> and <code>https-proxy</code> lines in <code>~/.npmrc</code>, read by npm, pnpm and yarn 1.</li>
        </ul>
        <p>For a profile with a sign-in, the user name and password are part of that address, as those tools expect. Apps that use these settings then connect through your proxy server; Proxi doesn’t see that traffic.</p>
        <h2>Local control</h2>
        <p>The command-line tool, the MCP server for AI assistants and <code>proxi://</code> commands use a local socket on your Mac (<code>control.sock</code>) that only your own account can connect to, with a permission level you choose, including “off”. They can view the status and profiles, turn the proxy on or off, switch profiles and test connections; they can’t change settings or read passwords.</p>""",
    "net_intro": "Apart from the connections your own apps make through the proxy you set, Proxi itself connects to the following:",
    "network": [
        ["The test address (default <code>https://www.apple.com/library/test/success.html</code>, changeable in Settings › General)", "When you test a connection, and when Detect checks which ports on this Mac answer as a proxy.", "An ordinary request for that page, sent through the proxy being tested."],
        ["Your proxy server", "Every 20 seconds while a proxy is on, if “Regularly check that the proxy server is reachable” is on.", "A TCP connection to the proxy’s address and port, closed straight away; no request is sent."],
        ["The PAC address of a PAC profile", "When the profile is on or tested; macOS fetches it as it does for any PAC setting.", "A request for the PAC file at the address you entered."],
        GITHUB_UPDATE("Proxi", "At launch and every 6 hours, unless you turn automatic checks off; and when you install an update.", "Proxi/&lt;version&gt; (macOS)"),
    ],
    "icloud": """<h2>iCloud</h2>
        <p>If you turn on iCloud sync, Proxi writes your profiles and the settings on the General and Hotkey pages to a file in your own iCloud Drive, <code>Proxi/config.json</code>, with your Mac’s name and the time of the change. Passwords are not included: each Mac keeps its own in its Keychain and asks for it once. The file is stored by Apple under your iCloud account; I have no access to it.</p>""",
    "permissions": [
        ["Administrator password", "To install the command-line tool, when macOS asks for it to change the system proxy, and to remove the background helper an earlier version installed."],
        ["Keychain", "To store and read the passwords of profiles that sign in to their proxy server."],
        ["Location", "Only for switching by Wi-Fi network: macOS requires it to read the Wi-Fi name. Proxi doesn’t read or store your location."],
        ["Notifications", "For switching, connection problems and new versions."],
        ["iCloud Drive", "Only if you turn on sync."],
    ],
    "delete": "Turn the proxy off (so the settings above are cleared), quit Proxi, then delete Proxi.app, <code>~/Library/Application Support/Proxi/</code> and <code>~/Library/Preferences/com.whrss9527.proxyswitch.plist</code>. Remove the command-line tool on the Automation page first (or delete <code>/usr/local/bin/proxi</code>). Saved passwords can be removed in Keychain Access (search for <code>com.whrss9527.proxyswitch</code>). If you used sync, also delete the <code>Proxi</code> folder in iCloud Drive.",
}

def build_all():
    from privacy_zh import ZH
    for key, d in (("pop", POP), ("meno", MENO), ("stox", STOX), ("proxi", PROXI)):
        build(key, d, "en")
        build(key, ZH[key], "zh")


if __name__ == "__main__":
    build_all()
