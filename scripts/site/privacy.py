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
    h += f"""<main id="main">
  <article class="doc">
    <div class="wrap narrow">
      <header class="doc-head">
        <div class="icon-row"><img src="{r}assets/icons/{key}.png" alt="" width="48" height="48"><a href="{c.link(key + '/')}">{name}</a></div>
        <h1>{title}</h1>
        <p>{t(f'Last updated <time datetime="{UPDATED_ISO}">{UPDATED}</time>. Applies to {name} for macOS, version {d["version"]} and later.',
              f'最后更新于 <time datetime="{UPDATED_ISO}">{UPDATED_ZH}</time>。适用于 macOS 版 {name} {d["version"]} 及以后的版本。')}</p>
      </header>

      <section class="summary glass" aria-labelledby="sum">
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
              f"无论你是从 GitHub、本网站，还是通过 Mac App Store、Setapp 等商店或订阅服务获得 {name}，本政策都适用。这类服务负责处理你的购买或订阅，可能按它们自己的隐私政策处理数据；{name} 本身的行为与本页描述一致。如果将来某个版本的行为有所不同，本政策会在该版本发布之前更新。")}</p>

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
    "version": "0.11",
    "meta_desc": "no analytics, no accounts; connects only to the proxies, subscriptions and rule lists you configure.",
    "summary": [
        "No analytics, no accounts, no ads, and no server of mine. I collect nothing.",
        "Profiles, subscriptions, rules and traffic statistics stay on your Mac — and in your own iCloud Drive if you turn on sync.",
        "Proxi downloads the subscriptions and rule lists you add, tests proxies against a test address, and contacts GitHub for updates.",
        "Your traffic goes wherever your proxy settings send it. Proxi doesn’t provide proxy servers and doesn’t see or log your traffic anywhere but on your Mac.",
    ],
    "local_intro": "Proxi keeps its data in folders on your Mac:",
    "local": [
        ["Profiles, subscriptions (URLs and nodes), policy groups, rules, settings", "<code>~/Library/Application Support/Proxi/config.json</code>", "Subscription URLs can contain access tokens from your provider; they stay in this file (and in iCloud Drive if you sync)."],
        ["State, traffic statistics, activity log, imports", "<code>~/Library/Application Support/Proxi/</code> (<code>state.json</code>, <code>journal.json</code>, <code>imports/</code>)", "Traffic totals per node, app and day are counted on your Mac only."],
        ["Log", "<code>~/Library/Application Support/Proxi/proxi.log</code>", "Technical messages and core logs for troubleshooting."],
        ["Core configuration and rule files", "<code>~/Library/Application Support/Proxi/core/</code>", ""],
        ["Privileged helper (only for Enhanced and gateway modes)", "<code>/Library/PrivilegedHelperTools/</code>, <code>/Library/LaunchDaemons/</code>, <code>/Library/Application Support/ProxySwitch/</code>", "A copy of the core configuration in folders only root can write to; removed when you uninstall the helper."],
    ],
    "net_intro": "Apart from the traffic you route through your proxy, Proxi itself connects to the following:",
    "network": [
        ["Your subscription URLs", "When you add a subscription and at its update interval.", "A request to the address you entered, to download the node list."],
        ["Rule lists you add (for the built-in library: <code>raw.githubusercontent.com</code>, falling back to <code>cdn.jsdelivr.net</code>)", "When you add a rule set and at its update interval.", "A request for the list file."],
        ["Speed-test address (default <code>cp.cloudflare.com/generate_204</code>, changeable)", "When you test latency, and periodically for auto-select groups.", "An empty request through the proxy or node being tested."],
        ["IP lookup services (<code>api.ip.sb</code>, falling back to <code>ipinfo.io</code>, <code>ipapi.co</code>)", "While the built-in node proxy is on and the node changes, and when you check your direct exit IP.", "A request through the node (the service sees the node’s address) or directly (the service sees your public IP), to show the exit IP and region."],
        ["Service check sites (ChatGPT, Claude, Gemini, Netflix, YouTube, Google, GitHub, Telegram)", "Only when you run a service check.", "Ordinary page requests through the node you’re checking."],
        ["DNS servers", "When you turn on the core’s own DNS (defaults: <code>doh.pub</code>, <code>dns.alidns.com</code>, <code>1.1.1.1</code>, <code>dns.google</code>, changeable), and <code>cloudflare-dns.com</code> during a URL diagnosis.", "The domain names being resolved."],
        GITHUB_UPDATE("Proxi", "At launch and every 6 hours, unless you turn automatic checks off; and when you install an update.", "Proxi/&lt;version&gt; (macOS)"),
    ],
    "icloud": """<h2>iCloud</h2>
        <p>If you turn on iCloud sync, Proxi writes your configuration — profiles, subscriptions, rules and settings — to a file in your own iCloud Drive, <code>Proxi/config.json</code>, with your Mac’s name and the time of the change. LAN sharing, Enhanced mode and traffic statistics stay on each Mac. The file is stored by Apple under your iCloud account; I have no access to it.</p>""",
    "permissions": [
        ["Administrator password", "To change the system proxy (standard accounts), to install the command-line tool, and to install or remove the privileged helper."],
        ["Privileged helper", "Only for Enhanced and gateway modes: a virtual network interface and IP forwarding need root. It only accepts requests from the user who installed it."],
        ["Location", "Only for switching by Wi-Fi network: macOS requires it to read the Wi-Fi name. Proxi doesn’t read or store your location."],
        ["Screen Recording", "Only to scan a QR code on screen for a node."],
        ["Notifications", "For connection problems and new versions."],
        ["iCloud Drive", "Only if you turn on sync."],
    ],
    "extra": f"""<h2>Local control and LAN sharing</h2>
        <p>The command-line tool, MCP server for AI assistants and <code>proxi://</code> commands use a local socket on your Mac (<code>control.sock</code>) with a permission level you choose, including “off”. LAN sharing, when you turn it on, accepts connections from local network devices only (or the IPs you allow); those devices’ traffic is handled like your own and shown in the Connections page on your Mac.</p>
        <h2>The mihomo core</h2>
        <p>Proxi bundles <a href="https://github.com/MetaCubeX/mihomo">mihomo</a>, an open-source proxy core, and configures it not to fetch anything beyond your configuration: GeoIP data ships inside the app and automatic geo updates are off. The core connects to the nodes, subscriptions, rule lists, speed-test address and DNS servers in your configuration, and nothing else.</p>""",
    "delete": "Delete <code>~/Library/Application Support/Proxi/</code> and Proxi.app. If you installed the privileged helper, uninstall it first in Settings › Advanced (or <code>sudo proxi helper uninstall</code>). If you used sync, also delete the <code>Proxi</code> folder in iCloud Drive.",
}

def build_all():
    from privacy_zh import ZH
    for key, d in (("pop", POP), ("meno", MENO), ("stox", STOX), ("proxi", PROXI)):
        build(key, d, "en")
        build(key, ZH[key], "zh")


if __name__ == "__main__":
    build_all()
