/* whrss.com: an interactive recreation of Proxi, the menu bar panel and the settings window.
   Everything here is sample data; nothing is fetched, no port is probed and no setting is changed.
   Layout, sizes and wording follow the Proxi sources (PanelView, StatusIcon, StatusItemController,
   Glass, SettingsWindowController, ProfilesPage, AutomationPage, SyncPage) and its Localizable.strings:
   the Chinese page shows the zh-Hans interface, the English page the English one.

   Markup: <figure class="pxd" data-lang="en|zh" data-preset="panel|profiles|detect|automation|sync|general|diagnostics">…fallback…</figure> */
(function () {
  "use strict";

  // ------------------------------------------------------------------ strings
  var S = {
    zh: {
      demo: "可交互演示 · 示例数据",
      demoLabel: "Proxi 的可交互演示，使用示例数据",
      mb: "Proxi 菜单栏图标：点一下打开或收起面板，右键弹出菜单",
      clock: "10月1日 周四 09:41",
      hint: "点菜单栏里的开关图标打开面板，右键弹出菜单。",
      // panel
      onTitle: "已开启 · %s", offTitle: "代理已关闭",
      nextSub: "下次开启 %s · %s",
      toggleLabel: "代理开关",
      testProfiles: "测试全部配置的连接和延迟", failed: "失败", available: "可用",
      term: "复制在当前终端里使用代理的命令", zsh: "zsh / bash（终端、iTerm）", fish: "fish",
      hotkey: "%s 开关", settings: "设置", quit: "退出 Proxi", quitNote: "演示里不会真的退出",
      // right-click menu
      menuOn: "代理已开启：%s", menuOff: "代理已关闭", turnOff: "关闭代理", turnOn: "开启代理",
      checkUpdates: "检查更新…", settingsDots: "设置…", menuLabel: "Proxi 菜单",
      // profiles
      pCorp: "公司代理", pCharles: "Charles 调试", pProxyman: "Proxyman", pMitm: "mitmproxy",
      // window
      winLabel: "Proxi 设置窗口", close: "关闭窗口",
      pages: {
        profiles: ["代理配置", "每套配置指向一个你自己的代理服务器（公司代理、内网网关、Charles / Proxyman / mitmproxy 这类调试代理），在菜单栏里一键切换"],
        automation: ["自动化", "让命令行、快捷指令和系统里的 AI 助手按规则操作 Proxi；换了网络自动切换"],
        general: ["通用", "界面语言、菜单栏图标的行为、关闭代理的方式、通知"],
        hotkey: ["快捷键", "在任何程序里按下它就能开关代理"],
        sync: ["iCloud 同步", "通过 iCloud 云盘在多台 Mac 之间同步代理配置和设置"],
        diagnostics: ["诊断", "系统里各处的代理设置，以及运行日志"],
        about: ["关于", "Proxi for Mac"]
      },
      // profiles page
      newP: "新建", detect: "自动检测", detectHelp: "找出本机正在运行的代理软件",
      name: "名称", color: "颜色", kind: "类型", pac: "PAC 脚本", server: "代理服务器", host: "主机", port: "端口",
      pasteHint: "可以直接把 proxy.corp.example:3128、127.0.0.1:8888 或 socks5://127.0.0.1:1080 这样的整段地址粘到「主机」里，会自动拆开。常见的本机调试代理：Charles 是 8888，Proxyman 是 9090，mitmproxy 是 8080。",
      pacURL: "PAC 地址", pacOnly: "PAC 脚本只能用于系统代理",
      signIn: "登录（可选）", user: "用户名", password: "密码", noSignIn: "不需要登录就留空",
      signInNote: "代理服务器要求登录时填写。密码只保存在这台 Mac 的钥匙串里，不写进配置文件、不跟 iCloud 同步，别的 Mac 第一次开启这个配置时会请你输入一次。开启时密码会写进系统代理设置，以及环境变量、git 和 npm 用的代理地址。",
      scope: "生效范围",
      tSystem: ["系统代理", "浏览器和大多数软件都走它"],
      tEnv: ["环境变量", "http_proxy、https_proxy、all_proxy、no_proxy：之后新开的终端和程序生效"],
      tGit: ["git", "git clone、pull 等（全局 http.proxy）"],
      tNpm: ["npm / pnpm / yarn", "写入用户目录的 .npmrc（npm、pnpm 和 yarn 1 都读它）"],
      bypassSec: "不经代理的地址", bypass: "系统代理的例外（逗号分隔）", noProxy: "NO_PROXY（环境变量和 npm）",
      del: "删除", testConn: "测试连接", save: "保存", saved: "已保存",
      testResult: "测试结果", testOk: "%s，%s", viaProxy: "经代理访问成功，HTTP 200", refused: "连不上代理服务器",
      // detect sheet
      detTitle: "自动检测本机代理", detMsg: "检查本机监听的端口，找出能当代理用的，并测出延迟。",
      detecting: "正在检测…", add: "添加", again: "重新检测", closeBtn: "关闭",
      // automation
      ifSec: "本机控制接口", perm: "权限", status: "状态", listening: "在监听", stopped: "已关闭", lastCall: "最近一次调用",
      permOff: "关闭", permRead: "只能查看", permOp: "开关和切换",
      permOffD: "命令行和 AI 助手都连不上", permReadD: "查看状态和代理配置，不能改动任何东西", permOpD: "另外可以开关代理、切换配置、测试连接",
      lastCallV: "命令行 · use_profile · 2分钟前",
      ifNote: "命令行和 AI 助手经本机的套接字（~/Library/Application Support/Proxi/control.sock）操作 Proxi，只有这台 Mac 上你自己的账户能连。它们只能查看状态、开关代理和切换配置，不能改配置。",
      cliSec: "命令行", installed: "已安装：/usr/local/bin/proxi", uninstall: "卸载",
      cliUse: "proxi use 公司代理",
      cliNote: "会在 /usr/local/bin 放一个小脚本（要输一次管理员密码）。不装也可以直接运行 /Applications/Proxi.app/Contents/MacOS/Proxi status。proxi help 看全部命令，加 --json 输出 JSON。",
      mcpSec: "AI 助手（MCP）",
      mcpNote: "支持 MCP 的 AI 客户端（Claude Desktop、Claude Code、Cursor 等）加上下面的配置后，就能让 AI 查看代理状态、开关代理、切换配置和测试连接。它能做到哪一步由上面的权限决定。",
      mcpLabel: "配置文件里的 mcpServers", mcpTools: "给 AI 助手的规则（%s 个工具）",
      urlSec: "URL 命令与快捷指令", urlUse: "proxi://use?name=公司代理",
      urlNote: "快捷指令里用「打开 URL」执行这些命令，或者用「运行 Shell 脚本」调用 proxi 命令。",
      copy: "复制", copied: "已复制",
      netSec: "按网络自动切换", netToggle: "换了网络时按规则自动切换", netNow: "现在的网络",
      netNowV: "Wi‑Fi「Office-5G」 · 路由器 10.20.0.1",
      ruleSsid: "连上 Wi‑Fi「%s」", ruleOn: "开启「%s」", ruleOff: "关闭代理", ruleDel: "删除这条规则",
      netNote: "比如在公司的 Wi‑Fi 自动开公司代理、回家自动关掉。同一个网络只切一次，之后你手动改了不会被改回去。认 Wi‑Fi 名字要定位权限；不给的话可以按路由器（MAC 地址）认。",
      // general
      langLabel: "界面语言", langFollow: "跟随系统",
      langNote: "跟随系统时，系统语言是中文就显示中文，其他语言都显示英文。重新启动时代理保持开着。只影响这台 Mac，不会同步。",
      startSec: "启动", login: "登录时自动启动", offOnQuit: "退出 Proxi 时关闭代理",
      iconSec: "菜单栏图标", leftClick: "左键点击", openPanel: "打开面板", directToggle: "直接开关代理",
      rightNote: "右键或 Control + 点击总是弹出菜单",
      speed: "实时网速", speedSys: "系统网络总速度", speedNone: "不显示",
      proxySec: "代理", whenOff: "关闭代理时", offDirect: "直接连接", offRestore: "恢复开启前的设置",
      health: "定期检查代理服务器能否连上", testURL: "测速地址",
      testURLNote: "测试连接时经代理访问这个地址。默认是苹果的连通性检测页，也可以换成你自己内网里的地址。",
      notifySec: "通知", notifyAll: "全部显示", notifyProblems: "只显示问题", notifyNone: "不显示",
      updSec: "更新", autoUpd: "自动检查更新",
      updNote: "启动后和之后每 6 小时检查一次 GitHub 上的新版本，有新版本时通知，不会自动安装。「关于」页里可以随时手动检查和一键更新。",
      // hotkey
      hkSec: "开 / 关代理", clear: "清除", hkNote: "点击方框后按下新的组合键，至少包含 ⌃、⌥、⇧、⌘ 中的一个。",
      hkCli: "命令行与快捷指令", hkCliNote: "更多的命令、给 AI 助手用的接口和按网络自动切换在「自动化」页。终端里也可以用 open 命令控制：",
      hkUse: "open \"proxi://use?name=配置名\"",
      // sync
      syncSec: "同步", syncToggle: "通过 iCloud 同步配置", synced: "已同步", syncing: "正在同步…", off: "未开启",
      lastChange: "最近一次改动来自「%s」，%s", device: "MacBook Pro", ago4: "4分钟前", justNow: "刚刚",
      syncNow: "立即同步", finder: "在 Finder 中显示",
      whatSec: "会同步什么",
      what1: "全部代理配置，以及「通用」和「快捷键」页里的设置。登录时启动、上次使用的配置、更新提醒这些本机状态不同步。",
      what2: "文件放在 iCloud 云盘的 Proxi 文件夹里。别的 Mac 上开启同步时会读到它，可以选择用 iCloud 的、用本机的，或者把两边合并。之后任何一台的改动几秒内就会出现在其他 Mac 上；两台同时改动时，以改动时间晚的为准。",
      what3: "第一次开启时系统可能会询问是否允许 Proxi 访问 iCloud 云盘，需要允许。",
      dlgTitle: "iCloud 里已经有配置",
      dlgMsg: "来自「MacBook Pro」，更新于 2026年10月1日 09:30，有 4 套配置；本机现在有 4 套。要怎么处理？",
      useCloud: "用 iCloud 的替换本机的", merge: "合并两边的配置", useLocal: "用本机的覆盖 iCloud", cancel: "取消",
      // diagnostics
      sysSec: "系统代理", inEffect: "当前生效", wpad: "自动发现（WPAD）", exceptions: "例外", services: "网络服务",
      onWord: "开", offWord: "关", none: "无", notSet: "未设置", svcList: "Wi‑Fi、USB 10/100/1000 LAN（已停用）",
      openSys: "打开系统的代理设置", clearAll: "清除所有代理设置",
      envSec: "环境变量（launchd）", envNote: "新打开的终端和程序会读到这些变量；已经打开的终端请用面板里的「复制终端命令」。",
      gitSec: "git 与 npm", filesSec: "文件", cfgDir: "配置目录", openDir: "打开配置目录", refresh: "刷新", logSec: "日志",
      // about
      version: "版本 %s", aboutLine: "给开发者用的代理开关：一键把系统代理、终端、git 和 npm 指向你自己的代理服务器。",
      issue: "反馈问题", checkNow: "检查更新", upToDate: "已经是最新版本", checking: "正在检查更新…"
    },
    en: {
      demo: "Interactive demo · sample data",
      demoLabel: "Interactive demo of Proxi, with sample data",
      mb: "Proxi in the menu bar. Click to open or close the panel, right-click for the menu",
      clock: "Thu Oct 1  9:41",
      hint: "Click the switch icon in the menu bar to open the panel, or right-click it for the menu.",
      onTitle: "On · %s", offTitle: "Proxy is off",
      nextSub: "Next: %s · %s",
      toggleLabel: "Proxy switch",
      testProfiles: "Test the connection and latency of all profiles", failed: "Failed", available: "Available",
      term: "Copy the command for using the proxy in the current terminal", zsh: "zsh / bash (Terminal, iTerm)", fish: "fish",
      hotkey: "%s to toggle", settings: "Settings", quit: "Quit Proxi", quitNote: "the demo doesn’t really quit",
      menuOn: "Proxy is on: %s", menuOff: "Proxy is off", turnOff: "Turn Off Proxy", turnOn: "Turn On Proxy",
      checkUpdates: "Check for Updates…", settingsDots: "Settings…", menuLabel: "Proxi menu",
      pCorp: "Corporate proxy", pCharles: "Charles", pProxyman: "Proxyman", pMitm: "mitmproxy",
      winLabel: "Proxi Settings window", close: "Close window",
      pages: {
        profiles: ["Proxy Profiles", "Each profile points at a proxy server of your own (a corporate proxy, an intranet gateway, or a debugging proxy such as Charles, Proxyman or mitmproxy). Switch between them from the menu bar."],
        automation: ["Automation", "Let the command line, Shortcuts and AI assistants on this Mac operate Proxi within limits, and switch automatically when the network changes"],
        general: ["General", "Interface language, menu bar icon behavior, how the proxy turns off, notifications"],
        hotkey: ["Hotkey", "Press it in any app to turn the proxy on or off"],
        sync: ["iCloud Sync", "Sync proxy profiles and settings across your Macs with iCloud Drive"],
        diagnostics: ["Diagnose", "Proxy settings across the system, and the app log"],
        about: ["About", "Proxi for Mac"]
      },
      newP: "New", detect: "Detect", detectHelp: "Find proxy apps running on this Mac",
      name: "Name", color: "Color", kind: "Type", pac: "PAC Script", server: "Proxy Server", host: "Host", port: "Port",
      pasteHint: "You can paste a whole address such as proxy.corp.example:3128, 127.0.0.1:8888 or socks5://127.0.0.1:1080 into Host and it’s split up automatically. Common local debugging proxies: Charles uses 8888, Proxyman 9090 and mitmproxy 8080.",
      pacURL: "PAC URL", pacOnly: "PAC scripts only work with the system proxy",
      signIn: "Sign-in (optional)", user: "User name", password: "Password", noSignIn: "Leave empty if no sign-in is needed",
      signInNote: "Fill these in when the proxy server requires signing in. The password is stored only in this Mac’s keychain; it isn’t written to the configuration file or synced with iCloud, and other Macs ask for it once the first time they turn this profile on. When the profile is on, the password is written into the system proxy settings and the proxy address used for environment variables, git and npm.",
      scope: "Scope",
      tSystem: ["System Proxy", "Browsers and most apps use it"],
      tEnv: ["Environment Variables", "http_proxy, https_proxy, all_proxy, no_proxy: Terminal windows and apps opened afterwards use them"],
      tGit: ["git", "git clone, pull, etc. (global http.proxy)"],
      tNpm: ["npm / pnpm / yarn", "Written to .npmrc in your home folder (read by npm, pnpm and yarn 1)"],
      bypassSec: "Bypass Proxy For", bypass: "System proxy exceptions (comma-separated)", noProxy: "NO_PROXY (environment variables and npm)",
      del: "Delete", testConn: "Test Connection", save: "Save", saved: "Saved",
      testResult: "Test Result", testOk: "%s, %s", viaProxy: "Via proxy: OK, HTTP 200", refused: "Can’t reach the proxy server",
      detTitle: "Detect Local Proxies", detMsg: "Check the ports this Mac is listening on, find the ones that work as proxies, and measure their latency.",
      detecting: "Checking…", add: "Add", again: "Detect Again", closeBtn: "Close",
      ifSec: "Local Control Interface", perm: "Permission", status: "Status", listening: "Listening", stopped: "Off", lastCall: "Last Call",
      permOff: "Off", permRead: "Read Only", permOp: "Switch on/off and profiles",
      permOffD: "Neither the command line nor AI assistants can connect", permReadD: "View the status and proxy profiles; nothing can be changed", permOpD: "Can also turn the proxy on or off, switch profiles and test connections",
      lastCallV: "Command line · use_profile · 2 min. ago",
      ifNote: "The command line and AI assistants control Proxi through a local socket (~/Library/Application Support/Proxi/control.sock) that only your own account on this Mac can connect to. They can view the status, turn the proxy on or off and switch profiles, but can’t change settings.",
      cliSec: "Command line", installed: "Installed: /usr/local/bin/proxi", uninstall: "Uninstall",
      cliUse: "proxi use \"Corporate proxy\"",
      cliNote: "Puts a small script in /usr/local/bin (asks for the administrator password once). You can also run /Applications/Proxi.app/Contents/MacOS/Proxi status directly without installing. proxi help lists all commands; add --json for JSON output.",
      mcpSec: "AI Assistants (MCP)",
      mcpNote: "AI clients that support MCP (Claude Desktop, Claude Code, Cursor and others) can, with the configuration below, check the proxy status, turn the proxy on or off, switch profiles and test connections. What they’re allowed to do is set by the permission above.",
      mcpLabel: "mcpServers in the configuration file", mcpTools: "Rules for AI assistants (%s tools)",
      urlSec: "URL Commands & Shortcuts", urlUse: "proxi://use?name=Corporate%20proxy",
      urlNote: "In Shortcuts, run these with “Open URLs”, or call the proxi command with “Run Shell Script”.",
      copy: "Copy", copied: "Copied",
      netSec: "Switch by Network", netToggle: "Switch automatically by rule when the network changes", netNow: "Current Network",
      netNowV: "Wi‑Fi “Office-5G” · Router 10.20.0.1",
      ruleSsid: "Joined Wi‑Fi “%s”", ruleOn: "Turn on “%s”", ruleOff: "Turn Off Proxy", ruleDel: "Delete this rule",
      netNote: "For example, turn on the corporate proxy on the office Wi‑Fi and turn it off at home. Each network switches only once, so manual changes afterwards aren’t undone. Recognizing Wi‑Fi names needs Location permission; without it, networks can be recognized by router (MAC address).",
      langLabel: "Language", langFollow: "Follow System",
      langNote: "Follow System shows Chinese when the system language is Chinese and English for every other language. The proxy stays on while Proxi relaunches. Only affects this Mac and isn’t synced.",
      startSec: "Startup", login: "Launch at Login", offOnQuit: "Turn Off Proxy When Quitting Proxi",
      iconSec: "Menu Bar Icon", leftClick: "Left Click", openPanel: "Open Panel", directToggle: "Toggle Proxy",
      rightNote: "Right-click or Control-click always shows the menu",
      speed: "Live Speed", speedSys: "Total System Network Speed", speedNone: "Don’t Show",
      proxySec: "Proxy", whenOff: "When Turning Off the Proxy", offDirect: "Direct Connection", offRestore: "Restore Previous Settings",
      health: "Regularly Check That the Proxy Server Is Reachable", testURL: "Test URL",
      testURLNote: "Connection tests fetch this address through the proxy. The default is Apple’s connectivity check page; you can use an address on your own intranet instead.",
      notifySec: "Notifications", notifyAll: "Show All", notifyProblems: "Problems Only", notifyNone: "Don’t Show",
      updSec: "Updates", autoUpd: "Check for Updates Automatically",
      updNote: "Checks GitHub for new versions after launch and every 6 hours after that, and notifies you when there is one; nothing is installed automatically. You can check manually and update with one click on the About page anytime.",
      hkSec: "Proxy On / Off", clear: "Clear", hkNote: "Click the box and press a new key combination that includes at least one of ⌃, ⌥, ⇧ or ⌘.",
      hkCli: "Command Line & Shortcuts", hkCliNote: "More commands, the interface for AI assistants and switching by network are on the Automation page. You can also control Proxi with the open command in Terminal:",
      hkUse: "open \"proxi://use?name=ProfileName\"",
      syncSec: "Sync", syncToggle: "Sync Configuration with iCloud", synced: "Synced", syncing: "Syncing…", off: "Off",
      lastChange: "Latest change from “%s”, %s", device: "MacBook Pro", ago4: "4 min. ago", justNow: "just now",
      syncNow: "Sync Now", finder: "Show in Finder",
      whatSec: "What’s Synced",
      what1: "All proxy profiles, plus the settings on the General and Hotkey pages. Local state such as Launch at Login, the last used profile and update reminders isn’t synced.",
      what2: "The file lives in the Proxi folder in iCloud Drive. When sync is turned on on another Mac, it reads this file and you can choose to use iCloud’s, use the local one, or merge both. After that, changes on any Mac show up on the others within seconds; when two Macs change at the same time, the later change wins.",
      what3: "The first time you turn it on, macOS may ask whether Proxi can access iCloud Drive; allow it.",
      dlgTitle: "iCloud Already Has a Configuration",
      dlgMsg: "From “MacBook Pro”, updated Oct 1, 2026 at 9:30 AM, with 4 profiles; this Mac has 4 now. What would you like to do?",
      useCloud: "Replace This Mac’s with iCloud’s", merge: "Merge Both", useLocal: "Overwrite iCloud with This Mac’s", cancel: "Cancel",
      sysSec: "System Proxy", inEffect: "Currently in Effect", wpad: "Auto Discovery (WPAD)", exceptions: "Exceptions", services: "Network Services",
      onWord: "On", offWord: "Off", none: "none", notSet: "Not set", svcList: "Wi‑Fi, USB 10/100/1000 LAN (disabled)",
      openSys: "Open System Proxy Settings", clearAll: "Clear All Proxy Settings",
      envSec: "Environment Variables (launchd)", envNote: "Newly opened terminals and apps read these variables; for terminals that are already open, use “Copy Terminal Command” in the panel.",
      gitSec: "git & npm", filesSec: "Files", cfgDir: "Configuration Folder", openDir: "Open Configuration Folder", refresh: "Refresh", logSec: "Logs",
      version: "Version %s", aboutLine: "A proxy switch for developers: one click points the system proxy, Terminal, git and npm at your own proxy server.",
      issue: "Report an Issue", checkNow: "Check for Updates", upToDate: "You’re up to date", checking: "Checking for updates…"
    }
  };

  // ------------------------------------------------------------------ icons (SF Symbols, redrawn)
  function svg(body, vb, fill) {
    return '<svg viewBox="' + (vb || "0 0 16 16") + '" aria-hidden="true" focusable="false" fill="' + (fill ? "currentColor" : "none") +
      '" stroke="' + (fill ? "none" : "currentColor") + '" stroke-width="1.4" stroke-linecap="round" stroke-linejoin="round">' + body + "</svg>";
  }
  var I = {
    power: svg('<path d="M8 1.8v5.4"/><path d="M4.6 3.8a5.3 5.3 0 1 0 6.8 0"/>'),
    shield: svg('<path d="M8 1.2 13.6 3.4v4.2c0 3.4-2.4 6-5.6 7.2C4.8 13.6 2.4 11 2.4 7.6V3.4Z"/><path d="m5.2 8 2 2 3.8-3.9" fill="none" stroke="#fff" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/>', null, true),
    gauge: svg('<circle cx="8" cy="8" r="6.2"/><path d="m8 8 2.6-2.6"/><path d="M4.6 10.8h.01M4 8h.01M4.9 5.1h.01M8 4h.01M11.1 5.1h.01M12 8h.01" stroke-width="1.8"/>'),
    stetho: svg('<path d="M3.2 1.8H2.6v3.6a3 3 0 0 0 6 0V1.8H8"/><path d="M5.6 8.4v1.8a3.4 3.4 0 0 0 6.8 0V8.8"/><circle cx="12.4" cy="7.4" r="1.4"/>'),
    gear: svg('<path d="M13.19 6.49 15.01 6.89 15.01 9.11 13.19 9.51 12.73 10.6 13.74 12.17 12.17 13.74 10.6 12.73 9.51 13.19 9.11 15.01 6.89 15.01 6.49 13.19 5.4 12.73 3.83 13.74 2.26 12.17 3.27 10.6 2.81 9.51 .99 9.11 .99 6.89 2.81 6.49 3.27 5.4 2.26 3.83 3.83 2.26 5.4 3.27 6.49 2.81 6.89 .99 9.11 .99 9.51 2.81 10.6 3.27 12.17 2.26 13.74 3.83 12.73 5.4Z" stroke-width="1.2"/><circle cx="8" cy="8" r="2.3"/>'),
    terminal: svg('<rect x="1.6" y="2.4" width="12.8" height="11.2" rx="2.2"/><path d="m4.6 6.2 2 1.8-2 1.8M8.4 10.4h3"/>'),
    check: svg('<path d="m3.4 8.4 3 3 6.2-6.6"/>'),
    checkFill: svg('<circle cx="8" cy="8" r="7.2"/><path d="m4.8 8.2 2.2 2.2 4.2-4.6" fill="none" stroke="#fff" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/>', null, true),
    xFill: svg('<circle cx="8" cy="8" r="7.2"/><path d="m5.6 5.6 4.8 4.8M10.4 5.6l-4.8 4.8" fill="none" stroke="#fff" stroke-width="1.6" stroke-linecap="round"/>', null, true),
    circle: svg('<circle cx="8" cy="8" r="6.6"/>'),
    arrow: svg('<path d="M2.6 8h10.4M9 4l4 4-4 4"/>'),
    trash: svg('<path d="M2.6 4h10.8M6.2 4V2.6h3.6V4M4 4l.7 9.4h6.6L12 4M6.6 6.6v4.6M9.4 6.6v4.6"/>'),
    plus: svg('<path d="M8 3v10M3 8h10"/>'),
    wand: svg('<path d="m2.4 13.6 8-8M9.2 4.4l2.4 2.4M12 1.6v2M11 2.6h2M14 5.2v1.6M13.2 6h1.6M5.4 1.8v1.6M4.6 2.6h1.6"/>'),
    globe: svg('<circle cx="8" cy="8" r="6.4"/><path d="M1.6 8h12.8M8 1.6c1.7 1.8 2.6 4 2.6 6.4S9.7 12.6 8 14.4C6.3 12.6 5.4 10.4 5.4 8S6.3 3.4 8 1.6Z"/>'),
    checkCircle: svg('<circle cx="8" cy="8" r="6.4"/><path d="m5.2 8.2 2 2 3.8-4"/>'),
    icloudCheck: svg('<path d="M4.4 12.6a3 3 0 0 1-.4-6 4.2 4.2 0 0 1 8.1-.6 3.3 3.3 0 0 1 .3 6.6Z"/><path d="m6 9.2 1.6 1.6 2.8-3"/>'),
    chevron: svg('<path d="m6 4 4 4-4 4"/>'),
    wifi: svg('<path d="M1.6 5.8a9.2 9.2 0 0 1 12.8 0M3.8 8.2a6 6 0 0 1 8.4 0M6 10.6a2.8 2.8 0 0 1 4 0"/><circle cx="8" cy="12.9" r=".9" fill="currentColor" stroke="none"/>'),
    battery: svg('<rect x="1.2" y="4.6" width="12" height="6.8" rx="1.8"/><rect x="2.6" y="6" width="7.4" height="4" rx=".8" fill="currentColor" stroke="none"/><path d="M14.6 7v2"/>'),
    // sidebar
    profiles: svg('<circle cx="3.2" cy="4" r="1.6"/><circle cx="12.8" cy="4" r="1.6"/><circle cx="8" cy="12.4" r="1.6"/><path d="M4.8 4h6.4M4 5.4l3.2 5.6M12 5.4l-3.2 5.6" stroke-dasharray="1.2 1.4"/>'),
    stars: svg('<path d="m1.8 14.2 8.4-8.4M9 4.6l2.4 2.4"/><path d="M12.6 1.4l.5 1.1 1.1.5-1.1.5-.5 1.1-.5-1.1-1.1-.5 1.1-.5ZM5 1.8l.4.8.8.4-.8.4-.4.8-.4-.8-.8-.4.8-.4Z" fill="currentColor" stroke="none"/>'),
    keyboard: svg('<rect x="1" y="3.6" width="14" height="8.8" rx="1.6"/><path d="M3.6 6.4h.01M6 6.4h.01M8.4 6.4h.01M10.8 6.4h.01M12.6 6.4h.01M3.6 8.4h.01M12.6 8.4h.01" stroke-width="1.6"/><path d="M5.8 10h4.4M6 8.4h4"/>'),
    icloud: svg('<path d="M4.4 12.6a3 3 0 0 1-.4-6 4.2 4.2 0 0 1 8.1-.6 3.3 3.3 0 0 1 .3 6.6Z"/>'),
    info: svg('<circle cx="8" cy="8" r="6.4"/><path d="M8 7.2v4M8 4.8h.01" stroke-width="1.6"/>')
  };
  var PAGE_ICON = { profiles: "profiles", automation: "stars", general: "gear", hotkey: "keyboard", sync: "icloud", diagnostics: "stetho", about: "info" };
  var PAGES = ["profiles", "automation", "general", "hotkey", "sync", "diagnostics", "about"];

  // ------------------------------------------------------------------ helpers
  function fmt(template) {
    var args = arguments, i = 1;
    return String(template).replace(/%s/g, function () { return args[i++]; });
  }
  function esc(s) {
    return String(s).replace(/[&<>"]/g, function (c) { return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]; });
  }
  function hash(s) {
    var h = 2166136261;
    for (var i = 0; i < s.length; i++) { h ^= s.charCodeAt(i); h = Math.imul(h, 16777619); }
    return h >>> 0;
  }
  function rng(seed) {   // mulberry32: the same seed always draws the same numbers
    var a = seed >>> 0;
    return function () {
      a = (a + 0x6D2B79F5) >>> 0;
      var t = a;
      t = Math.imul(t ^ (t >>> 15), t | 1);
      t ^= t + Math.imul(t ^ (t >>> 7), t | 61);
      return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
    };
  }
  var reduced = window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  // ------------------------------------------------------------------ sample data
  // A corporate proxy and three local debugging proxies. mitmproxy isn't running in this story,
  // so its test fails; the others answer with fixed latencies.
  var PROFILES = [
    { id: "corp", nameKey: "pCorp", color: "#16a34a", kind: "http", host: "proxy.corp.example", port: 3128, user: "dev", ms: 38, targets: ["system", "env", "git", "npm"] },
    { id: "charles", nameKey: "pCharles", color: "#2563eb", kind: "http", host: "127.0.0.1", port: 8888, ms: 3, targets: ["system", "env"] },
    { id: "proxyman", nameKey: "pProxyman", color: "#db2777", kind: "http", host: "127.0.0.1", port: 9090, ms: 4, targets: ["system"] },
    { id: "mitm", nameKey: "pMitm", color: "#ea580c", kind: "http", host: "127.0.0.1", port: 8080, ms: 0, targets: ["system", "env"] }
  ];
  var DETECTED = [
    { name: "Charles", kind: "HTTP / HTTPS", port: 8888, ms: 3 },
    { name: "Proxyman", kind: "HTTP / HTTPS", port: 9090, ms: 4 },
    { name: "mitmproxy", kind: "HTTP / HTTPS", port: 8080, ms: 5 }
  ];
  var COLORS = ["#16a34a", "#2563eb", "#7c3aed", "#db2777", "#ea580c", "#0891b2"];
  var TARGETS = [["system", "tSystem"], ["env", "tEnv"], ["git", "tGit"], ["npm", "tNpm"]];
  var BYPASS = "localhost, 127.0.0.1, *.local, 169.254/16, 10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16";
  var NO_PROXY = "localhost,127.0.0.1,::1";
  var TEST_URL = "https://www.apple.com/library/test/success.html";
  var TOOLS = ["get_status", "list_profiles", "get_logs", "turn_on", "use_profile", "turn_off", "toggle", "test_profiles"];

  // Bytes per second at second t (total system network speed): a calm base with a few bursts, the same every time.
  function speedAt(t) {
    var r = rng(hash("speed") ^ Math.imul(t + 7, 2246822519));
    var wave = 0.55 + 0.45 * Math.sin(t / 9) * Math.sin(t / 23 + 1);
    var burst = r() < 0.12 ? 2.4 + r() * 2.2 : 1;
    return { up: Math.round(18000 * (0.6 + 0.8 * r()) * (burst > 1 ? 1.8 : 1)), down: Math.round(240000 * wave * burst * (0.7 + 0.6 * r())) };
  }
  function threeDigits(v) {
    if (v < 9.995) return v.toFixed(2);
    if (v < 99.95) return v.toFixed(1);
    return String(Math.round(Math.min(v, 999)));
  }
  function compact(b) {   // SpeedFormatter.compact: three digits and B / K / M / G
    var v = Math.max(0, b), units = ["B", "K", "M", "G"];
    for (var i = 0; i < units.length; i++) {
      if (v < 999.5 || i === 3) return threeDigits(v) + units[i];
      v /= 1024;
    }
  }

  var PRESETS = {
    panel: { surface: "panel", on: true },
    profiles: { surface: "window", page: "profiles", on: true, profilePick: "corp" },
    detect: { surface: "window", page: "profiles", on: true, profilePick: "charles", sheet: true },
    automation: { surface: "window", page: "automation", on: true },
    general: { surface: "window", page: "general", on: true },
    sync: { surface: "window", page: "sync", on: true },
    diagnostics: { surface: "window", page: "diagnostics", on: true }
  };
  var counter = 0;

  function Demo(root) {
    this.root = root;
    this.uid = "pxd" + (++counter);
    this.lang = root.getAttribute("data-lang") === "zh" ? "zh" : "en";
    this.s = S[this.lang];
    var p = PRESETS[root.getAttribute("data-preset")] || PRESETS.panel;
    var self = this;
    this.profiles = PROFILES.map(function (pr) {
      var c = {};
      for (var k in pr) c[k] = pr[k];
      c.targets = pr.targets.slice();
      c.name = self.s[pr.nameKey];
      return c;
    });
    this.st = {
      surface: p.surface, page: p.page || "profiles", open: true, ctx: false,
      on: !!p.on, active: "corp", next: "corp", busy: false,
      results: {}, testingProfiles: false, menu: null, copiedTerm: false,
      profilePick: p.profilePick || "corp", draft: null, saved: false, profileTest: null, profileTesting: false,
      sheet: !!p.sheet, detecting: false, added: {},
      perm: "operate", rules: [true, true], netSwitch: true, copiedCmd: null, showTools: false,
      lang: "follow", login: true, offOnQuit: false, click: "panel", speedShow: "system", offMode: "direct", healthOn: true,
      notify: "all", autoUpd: true,
      sync: "synced", syncAgo: "ago4", dialog: false, checking: false, checked: false
    };
    this.tick = 240;
    this.timers = [];
    this.build();
    if (this.st.sheet) this.detect();
  }

  Demo.prototype = {
    t: function (k) { return this.s[k] !== undefined ? this.s[k] : S.en[k]; },
    profile: function (id) { for (var i = 0; i < this.profiles.length; i++) if (this.profiles[i].id === id) return this.profiles[i]; return null; },
    summary: function (p) {
      if (p.kind === "pac") return p.pac;
      if (p.kind === "socks5") return (p.user ? "socks5://" + p.user + "@" : "socks5://") + p.host + ":" + p.port;
      return (p.user ? p.user + "@" : "") + p.host + ":" + p.port;
    },
    proxyURL: function (p) { return (p.kind === "socks5" ? "socks5://" : "http://") + (p.user ? p.user + ":•••@" : "") + p.host + ":" + p.port; },
    later: function (fn, ms) {
      var self = this, id = setTimeout(function () { self.timers.splice(self.timers.indexOf(id), 1); fn.call(self); }, ms);
      this.timers.push(id);
    },

    build: function () {
      var r = this.root, self = this;
      r.classList.add("pxd-ready");
      r.setAttribute("role", "group");
      r.setAttribute("aria-label", this.t("demoLabel"));
      r.setAttribute("lang", this.lang === "zh" ? "zh-CN" : "en");
      var noscript = r.querySelector("noscript");
      r.innerHTML = "";
      if (noscript) r.appendChild(noscript);
      var stage = document.createElement("div");
      stage.className = "pxd-stage";
      r.appendChild(stage);
      var tag = document.createElement("figcaption");
      tag.className = "pxd-cap";
      tag.innerHTML = '<span class="pxd-tag"><span class="pxd-dot" aria-hidden="true"></span>' + esc(this.t("demo")) + "</span>";
      r.appendChild(tag);
      this.stage = stage;
      r.addEventListener("click", function (e) { self.lastClick = e; self.onClick(e); });
      r.addEventListener("contextmenu", function (e) { self.onContext(e); });
      r.addEventListener("keydown", function (e) { self.onKey(e); });
      r.addEventListener("input", function (e) { self.onInput(e); });
      document.addEventListener("click", function (e) {
        if ((self.st.menu || self.st.ctx) && e !== self.lastClick) { self.st.menu = null; self.st.ctx = false; self.render(); }
      });
      this.speed = speedAt(this.tick);
      this.render();
      if (!reduced) this.startTicking();
    },

    startTicking: function () {
      var self = this, visible = false;
      if ("IntersectionObserver" in window) {
        new IntersectionObserver(function (entries) { visible = entries[0].isIntersecting; }).observe(this.root);
      } else visible = true;
      setInterval(function () {
        if (!visible || document.hidden) return;
        self.tick++;
        self.speed = speedAt(self.tick);
        self.updateSpeed();
      }, 1000);
    },
    updateSpeed: function () {
      var up = this.stage.querySelector('[data-speed="up"]'), down = this.stage.querySelector('[data-speed="down"]');
      if (up) up.textContent = compact(this.speed.up);
      if (down) down.textContent = compact(this.speed.down);
    },

    // ---------------------------------------------------------------- render
    render: function () {
      var active = document.activeElement, key = null, sel = null;
      if (active && this.root.contains(active)) {
        key = active.getAttribute("data-k");
        if (active.tagName === "INPUT" && active.type === "text") sel = [active.selectionStart, active.selectionEnd];
      }
      var scrolls = {};
      Array.prototype.forEach.call(this.stage.querySelectorAll("[data-sc]"), function (el) { scrolls[el.getAttribute("data-sc")] = el.scrollTop; });
      var st = this.st, html = this.menubar();
      html += '<div class="px-scene">';
      if (st.ctx) html += this.contextMenu();
      else if (st.surface === "window") html += this.windowView();
      else if (st.open) html += '<div class="px-panel">' + this.panel() + "</div>";
      else html += '<p class="px-hint">' + esc(this.t("hint")) + "</p>";
      html += "</div>";
      this.stage.innerHTML = html;
      Array.prototype.forEach.call(this.stage.querySelectorAll("[data-sc]"), function (el) {
        var v = scrolls[el.getAttribute("data-sc")];
        if (v) el.scrollTop = v;
      });
      if (key) {
        var el = this.stage.querySelector('[data-k="' + key + '"]');
        if (el) {
          el.focus({ preventScroll: true });
          if (sel && el.setSelectionRange) el.setSelectionRange(sel[0], sel[1]);
        }
      }
    },

    menubar: function () {
      var st = this.st, p = this.profile(st.active), h = this.speed;
      var color = st.on ? p.color : null, open = (st.surface === "panel" && st.open) || st.ctx;
      return '<div class="px-mb">' +
        '<button type="button" class="px-mb-item px-mb-proxi' + (open ? " is-open" : "") + '" data-act="mb" data-k="mb" aria-expanded="' + open + '" aria-label="' + esc(this.t("mb")) + '">' +
        '<span class="px-speed"' + (color ? ' style="color:' + color + '"' : "") + '><span>↑</span><span class="px-sv" data-speed="up">' + compact(h.up) + '</span><span>↓</span><span class="px-sv" data-speed="down">' + compact(h.down) + "</span></span>" +
        this.switchIcon() + "</button>" +
        '<span class="px-mb-item px-mb-extra" aria-hidden="true">' + I.wifi + "</span>" +
        '<span class="px-mb-item px-mb-extra" aria-hidden="true">' + I.battery + "</span>" +
        '<span class="px-mb-item px-mb-clock" aria-hidden="true">' + esc(this.t("clock")) + "</span></div>";
    },
    switchIcon: function () {
      // StatusIcon: a 24×14 track with a round knob; off is a template image with a hollow knob.
      var st = this.st;
      if (!st.on) {
        return '<svg class="px-sw-icon" viewBox="0 0 24 14" aria-hidden="true"><path fill="currentColor" fill-rule="evenodd" d="M7 .5h10a6.5 6.5 0 0 1 0 13H7A6.5 6.5 0 0 1 7 .5Zm0 2.5a4 4 0 1 0 0 8 4 4 0 0 0 0-8Z"/></svg>';
      }
      var c = this.profile(st.active).color;
      return '<svg class="px-sw-icon" viewBox="0 0 24 14" aria-hidden="true"><rect x=".5" y=".5" width="23" height="13" rx="6.5" fill="' + c + '"/><circle cx="17" cy="7" r="4" fill="#fff"/></svg>';
    },

    // A macOS switch. `mini` is the small control size.
    sw: function (key, on, label, opts) {
      opts = opts || {};
      return '<button type="button" role="switch" class="px-switch' + (opts.mini ? " mini" : "") + '" aria-checked="' + !!on + '" data-act="' + key + '" data-k="' + key + '"' +
        (label ? ' aria-label="' + esc(label) + '"' : "") + (opts.help ? ' title="' + esc(opts.help) + '"' : "") + (opts.disabled ? " disabled" : "") + '><span class="px-knob"></span></button>';
    },
    seg: function (key, options, value, label, cls) {
      return '<div class="px-seg ' + (cls || "") + '" role="radiogroup" aria-label="' + esc(label) + '">' + options.map(function (o) {
        var on = o[0] === value;
        return '<button type="button" role="radio" aria-checked="' + on + '" tabindex="' + (on ? 0 : -1) + '" class="' + (on ? "is-on" : "") + '" data-act="' + key + '" data-v="' + o[0] + '" data-k="' + key + "-" + o[0] + '">' + esc(o[1]) + "</button>";
      }).join("") + "</div>";
    },
    spinner: function () { return '<span class="px-spin" aria-hidden="true"></span>'; },

    // ---------------------------------------------------------------- the panel
    panel: function () {
      return this.statusCard() + this.profileList() + this.footer();
    },

    statusCard: function () {
      var st = this.st, p = this.profile(st.on ? st.active : st.next), title, sub;
      if (st.on) {
        title = fmt(this.t("onTitle"), p.name);
        var res = st.results[p.id];
        sub = res && res.ok && res.ms ? this.summary(p) + " · " + res.ms + " ms" : this.summary(p);
      } else {
        title = this.t("offTitle");
        sub = fmt(this.t("nextSub"), p.name, this.summary(p));
      }
      var badge = st.on
        ? '<span class="px-badge" style="--c:' + p.color + '">' + I.shield + "</span>"
        : '<span class="px-badge is-off">' + I.power + "</span>";
      return '<div class="px-card prominent px-status">' + badge +
        '<div class="px-grow"><div class="px-title" id="' + this.uid + '-st">' + esc(title) + '</div><div class="px-sub">' + esc(sub) + "</div></div>" +
        (st.busy ? this.spinner() : this.sw("toggle", st.on, this.t("toggleLabel"))) + "</div>";
    },

    profileList: function () {
      var self = this, st = this.st;
      return '<div class="px-card px-profiles" role="radiogroup" aria-labelledby="' + this.uid + '-st">' + this.profiles.map(function (p) {
        var active = st.on && st.active === p.id, res = st.results[p.id];
        var cap = res ? '<span class="px-cap ' + (res.ok ? "good" : "bad") + '">' + esc(res.ok ? (res.ms ? res.ms + " ms" : self.t("available")) : self.t("failed")) + "</span>" :
          (st.testingProfiles ? '<span class="px-cap">…</span>' : "");
        return '<button type="button" class="px-row px-prow" role="radio" aria-checked="' + active + '" data-act="use" data-v="' + p.id + '" data-k="use-' + p.id + '">' +
          '<span class="px-cdot" style="--c:' + p.color + '"></span>' +
          '<span class="px-grow"><span class="px-pname' + (active ? " is-on" : "") + '">' + esc(p.name) + '</span><span class="px-psub">' + esc(self.summary(p)) + "</span></span>" + cap +
          '<span class="px-radio' + (active ? " is-on" : "") + '" style="--c:' + p.color + '">' + (active ? I.checkFill : I.circle) + "</span></button>";
      }).join("") + "</div>";
    },

    footer: function () {
      var st = this.st, p = this.profile(st.active), h = '<div class="px-foot">';
      h += '<button type="button" class="px-iconbtn" data-act="testprofiles" data-k="testprofiles" title="' + esc(this.t("testProfiles")) + '" aria-label="' + esc(this.t("testProfiles")) + '"' + (st.testingProfiles ? " disabled" : "") + ">" + (st.testingProfiles ? this.spinner() : I.gauge) + "</button>";
      if (st.on && p.kind !== "pac") {
        var open = st.menu === "term";
        h += '<span class="px-menuwrap"><button type="button" class="px-iconbtn" data-act="menu" data-v="term" data-k="term" aria-haspopup="menu" aria-expanded="' + open + '" title="' + esc(this.t("term")) + '" aria-label="' + esc(this.t("term")) + '">' + (st.copiedTerm ? I.check : I.terminal) + "</button>" +
          (open ? '<div class="px-menu up" role="menu"><button type="button" role="menuitem" class="px-mi" data-act="termcopy" data-v="zsh" data-k="tm-zsh"><span class="px-mi-check"></span>' + esc(this.t("zsh")) + '</button><button type="button" role="menuitem" class="px-mi" data-act="termcopy" data-v="fish" data-k="tm-fish"><span class="px-mi-check"></span>' + esc(this.t("fish")) + "</button></div>" : "") + "</span>";
      }
      h += '<span class="px-grow"></span><span class="px-hotkey">' + esc(fmt(this.t("hotkey"), "⌃⌥P")) + "</span>";
      h += '<button type="button" class="px-iconbtn" data-act="page" data-v="" data-k="f-gear" title="' + esc(this.t("settings")) + '" aria-label="' + esc(this.t("settings")) + '">' + I.gear + "</button>";
      h += '<button type="button" class="px-iconbtn" data-act="quit" data-k="f-quit" title="' + esc(this.t("quit") + " (" + this.t("quitNote") + ")") + '" aria-label="' + esc(this.t("quit")) + '">' + I.power + "</button>";
      return h + "</div>";
    },

    // The right-click menu (StatusItemController.showContextMenu).
    contextMenu: function () {
      var st = this.st, p = this.profile(st.active);
      var mi = function (act, label, v) {
        return '<button type="button" role="menuitem" class="px-mi" data-act="' + act + '"' + (v ? ' data-v="' + v + '"' : "") + ' data-k="cm-' + act + (v ? "-" + v : "") + '"><span class="px-mi-check"></span>' + esc(label) + "</button>";
      };
      var h = '<div class="px-cmenu" role="menu" aria-label="' + esc(this.t("menuLabel")) + '">';
      h += '<div class="px-mh">' + esc(st.on ? fmt(this.t("menuOn"), p.name) : this.t("menuOff")) + "</div>";
      h += st.on ? mi("ctxoff", this.t("turnOff")) : mi("ctxon", this.t("turnOn"));
      h += '<div class="px-msep"></div>';
      this.profiles.forEach(function (q) {
        var on = st.on && st.active === q.id;
        h += '<button type="button" role="menuitemradio" aria-checked="' + on + '" class="px-mi" data-act="ctxuse" data-v="' + q.id + '" data-k="cm-use-' + q.id + '"><span class="px-mi-check">' + (on ? I.check : "") + '</span><span class="px-cdot sm" style="--c:' + q.color + '"></span>' + esc(q.name) + "</button>";
      });
      h += '<div class="px-msep"></div>';
      h += mi("ctxupd", this.t("checkUpdates")) + mi("page", this.t("settingsDots"), "general") + mi("quit", this.t("quit"));
      return h + "</div>";
    },

    // ---------------------------------------------------------------- the settings window
    windowView: function () {
      var st = this.st, self = this;
      var side = PAGES.map(function (id) {
        var on = st.page === id;
        return '<button type="button" class="px-side-item' + (on ? " is-on" : "") + '" data-act="page" data-v="' + id + '" data-k="side-' + id + '"' + (on ? ' aria-current="page"' : "") + ' title="' + esc(self.t("pages")[id][0]) + '">' +
          '<span class="px-side-icon">' + I[PAGE_ICON[id]] + '</span><span class="px-side-label">' + esc(self.t("pages")[id][0]) + "</span></button>";
      }).join("");
      var page = this.t("pages")[st.page];
      return '<section class="px-win" aria-label="' + esc(this.t("winLabel")) + '">' +
        '<div class="px-lights"><button type="button" class="px-light red" data-act="closewin" data-k="closewin" aria-label="' + esc(this.t("close")) + '" title="' + esc(this.t("close")) + '"></button><span class="px-light yellow"></span><span class="px-light green"></span></div>' +
        '<nav class="px-side" aria-label="' + esc(this.t("settings")) + '"><div class="px-side-app"><span class="px-appicon" aria-hidden="true">' + this.appIcon() + '</span><span class="px-side-label">Proxi</span></div>' + side + "</nav>" +
        '<div class="px-detail" data-sc="detail-' + st.page + '"><header class="px-ph"><h3>' + esc(page[0]) + "</h3><p>" + esc(page[1]) + "</p></header>" +
        this.pageBody(st.page) + "</div>" + (st.dialog ? this.dialog() : "") + (st.sheet && st.page === "profiles" ? this.detectSheet() : "") + "</section>";
    },
    appIcon: function () {
      return '<svg viewBox="0 0 28 28"><defs><linearGradient id="' + this.uid + '-ai" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#3b82f6"/><stop offset="1" stop-color="#1d4ed8"/></linearGradient></defs>' +
        '<rect width="28" height="28" rx="6.5" fill="url(#' + this.uid + '-ai)"/><rect x="5" y="9" width="18" height="10" rx="5" fill="#fff"/><circle cx="18" cy="14" r="3.4" fill="#22c55e"/></svg>';
    },
    pageBody: function (id) {
      if (id === "profiles") return this.profilesPage();
      if (id === "automation") return this.automationPage();
      if (id === "general") return this.generalPage();
      if (id === "hotkey") return this.hotkeyPage();
      if (id === "sync") return this.syncPage();
      if (id === "diagnostics") return this.diagnosticsPage();
      return this.aboutPage();
    },
    section: function (title, rows, captions) {
      return '<div class="px-sec">' + (title ? '<h4 class="px-sech">' + esc(title) + "</h4>" : "") + '<div class="px-group">' + rows + "</div>" + (captions || "") + "</div>";
    },
    row: function (label, right, cls) {
      return '<div class="px-frow ' + (cls || "") + '"><span class="px-flabel short">' + label + '</span><span class="px-fval">' + right + "</span></div>";
    },
    toggleRow: function (key, label, on, detail, disabled) {
      return '<div class="px-frow"><span class="px-flabel" id="' + this.uid + "-" + key + '">' + esc(label) + (detail ? '<small>' + esc(detail) + "</small>" : "") + "</span>" +
        this.sw(key, on, label, { disabled: disabled }) + "</div>";
    },
    // A pop-up button: shows the chosen title; clicking it steps to the next option.
    popup: function (key, label, options, value) {
      var cur = options.filter(function (o) { return o[0] === value; })[0] || options[0];
      return '<div class="px-frow"><span class="px-flabel">' + esc(label) + '</span><button type="button" class="px-popup" data-act="cycle" data-v="' + key + '" data-k="pop-' + key + '" aria-label="' + esc(label + (this.lang === "zh" ? "：" : ": ") + cur[1]) + '">' + esc(cur[1]) + '<span class="px-popchev" aria-hidden="true">' + I.chevron + "</span></button></div>";
    },
    cap: function (text, cls) { return '<p class="px-caption ' + (cls || "") + '">' + esc(text) + "</p>"; },
    btn: function (act, label, opts) {
      opts = opts || {};
      return '<button type="button" class="px-btn' + (opts.primary ? " primary" : "") + (opts.small ? " small" : "") + '" data-act="' + act + '" data-k="b-' + act + (opts.v ? "-" + opts.v : "") + '"' + (opts.disabled ? " disabled" : "") + (opts.v ? ' data-v="' + opts.v + '"' : "") + ">" + (opts.icon || "") + esc(label) + "</button>";
    },
    codeRow: function (text) {
      var done = this.st.copiedCmd === text;
      return '<div class="px-frow px-coderow"><code class="px-mono">' + esc(text) + '</code><button type="button" class="px-btn small" data-act="copycmd" data-v="' + esc(text) + '" data-k="cc-' + hash(text) + '">' + esc(done ? this.t("copied") : this.t("copy")) + "</button></div>";
    },

    // ----- 代理配置
    profilesPage: function () {
      var st = this.st, self = this, pick = this.profile(st.profilePick);
      if (!st.draft || st.draft.id !== pick.id) st.draft = { id: pick.id, name: pick.name, color: pick.color, kind: pick.kind, targets: pick.targets.slice() };
      var d = st.draft;
      var list = '<div class="px-plist"><div class="px-group px-plistbox" role="listbox" aria-label="' + esc(this.t("pages").profiles[0]) + '">' + this.profiles.map(function (p) {
        var sel = p.id === st.profilePick, on = st.on && st.active === p.id;
        return '<button type="button" role="option" aria-selected="' + sel + '" class="px-row px-prow' + (sel ? " is-picked" : "") + '" data-act="pickprofile" data-v="' + p.id + '" data-k="pp-' + p.id + '">' +
          '<span class="px-cdot" style="--c:' + p.color + '"></span><span class="px-grow"><span class="px-pname med">' + esc(p.name) + '</span><span class="px-psub">' + esc(self.summary(p)) + "</span></span>" +
          (on ? '<span class="px-radio is-on" style="--c:' + p.color + '">' + I.checkFill + "</span>" : "") + "</button>";
      }).join("") + '</div><div class="px-btnrow">' +
        '<button type="button" class="px-btn small" disabled>' + I.plus + esc(this.t("newP")) + "</button>" +
        '<button type="button" class="px-btn small" data-act="opendetect" data-k="opendetect" title="' + esc(this.t("detectHelp")) + '">' + I.wand + esc(this.t("detect")) + "</button></div></div>";
      var ed = '<div class="px-group px-editor"><div class="px-editor-body">';
      ed += this.section("", this.row(esc(this.t("name")), '<input type="text" class="px-inline" data-k="dname" value="' + esc(d.name) + '" aria-label="' + esc(this.t("name")) + '">') +
        this.row(esc(this.t("color")), '<span class="px-colors" role="radiogroup" aria-label="' + esc(this.t("color")) + '">' + COLORS.map(function (c) {
          var on = d.color === c;
          return '<button type="button" role="radio" aria-checked="' + on + '" aria-label="' + c + '" class="px-swatch" style="--c:' + c + '" data-act="dcolor" data-v="' + c + '" data-k="dc-' + c.slice(1) + '">' + (on ? I.check : "") + "</button>";
        }).join("") + "</span>") +
        '<div class="px-frow col"><span class="px-flabel">' + esc(this.t("kind")) + "</span>" + this.seg("dkind", [["http", "HTTP / HTTPS"], ["socks5", "SOCKS5"], ["pac", this.t("pac")]], d.kind, this.t("kind"), "wide") + "</div>");
      var pacOnly = d.kind === "pac";
      if (pacOnly) {
        ed += this.section(this.t("pac"), this.row(esc(this.t("pacURL")), '<span class="px-mono">http://proxy.corp.example/proxy.pac</span>'));
      } else {
        ed += this.section(this.t("server"), this.row(esc(this.t("host")), '<span class="px-mono">' + esc(pick.host) + "</span>") + this.row(esc(this.t("port")), '<span class="px-mono">' + esc(String(pick.port)) + "</span>"), this.cap(this.t("pasteHint")));
        ed += this.section(this.t("signIn"),
          this.row(esc(this.t("user")), pick.user ? '<span class="px-mono">' + esc(pick.user) + "</span>" : '<span class="px-ghost">' + esc(this.t("noSignIn")) + "</span>") +
          this.row(esc(this.t("password")), pick.user ? '<span class="px-mono">••••••••</span>' : ""), this.cap(this.t("signInNote")));
      }
      ed += this.section(this.t("scope"), TARGETS.map(function (tg) {
        var on = d.targets.indexOf(tg[0]) >= 0 && !(pacOnly && tg[0] !== "system");
        return self.toggleRow("dt-" + tg[0], self.t(tg[1])[0], on, self.t(tg[1])[1], pacOnly && tg[0] !== "system");
      }).join(""), pacOnly ? this.cap(this.t("pacOnly")) : "");
      ed += this.section(this.t("bypassSec"), '<div class="px-frow col"><span class="px-flabel">' + esc(this.t("bypass")) + '</span><span class="px-mono px-wrap">' + BYPASS + "</span></div>" +
        (pacOnly ? "" : '<div class="px-frow col"><span class="px-flabel">' + esc(this.t("noProxy")) + '</span><span class="px-mono">' + NO_PROXY + "</span></div>"));
      if (st.profileTest) {
        var ok = st.profileTest.ok;
        ed += this.section(this.t("testResult"), '<div class="px-frow"><span class="' + (ok ? "px-ok" : "px-bad") + '">' + (ok ? I.checkFill : I.xFill) +
          esc(ok ? fmt(this.t("testOk"), st.profileTest.ms + " ms", this.t("viaProxy")) : this.t("refused")) + "</span></div>");
      }
      ed += "</div>";
      var dirty = this.dirty();
      ed += '<div class="px-edfoot"><button type="button" class="px-btn" disabled>' + I.trash + esc(this.t("del")) + "</button>" +
        '<button type="button" class="px-btn" data-act="ptest" data-k="ptest"' + (st.profileTesting ? " disabled" : "") + ">" + (st.profileTesting ? this.spinner() : I.gauge) + esc(this.t("testConn")) + "</button>" +
        '<span class="px-grow"></span>' + (st.saved && !dirty ? '<span class="px-savedlbl">' + I.check + esc(this.t("saved")) + "</span>" : "") +
        '<button type="button" class="px-btn primary" data-act="psave" data-k="psave"' + (dirty ? "" : " disabled") + ">" + esc(this.t("save")) + "</button></div></div>";
      return '<div class="px-profpage">' + list + ed + "</div>";
    },
    dirty: function () {
      var d = this.st.draft, p = d && this.profile(d.id);
      if (!p) return false;
      return d.name !== p.name || d.color !== p.color || d.kind !== p.kind || d.targets.slice().sort().join() !== p.targets.slice().sort().join();
    },
    detectSheet: function () {
      var st = this.st, self = this, id = this.uid + "-det", body;
      if (st.detecting) body = '<div class="px-detwait">' + this.spinner() + esc(this.t("detecting")) + "</div>";
      else body = '<div class="px-group px-detlist">' + DETECTED.map(function (d) {
        return '<div class="px-frow"><span class="px-dim">' + I.globe + '</span><span class="px-grow"><span class="px-pname med">' + esc(d.name) + '</span><span class="px-psub">' + esc(d.kind + " · 127.0.0.1:" + d.port + " · " + d.ms + " ms") + "</span></span>" +
          (st.added[d.port] ? '<span class="px-savedlbl">' + I.check + "</span>" : self.btn("detadd", self.t("add"), { v: String(d.port), small: true })) + "</div>";
      }).join("") + "</div>";
      return '<div class="px-dlg-back"><div class="px-dlg px-sheet" role="dialog" aria-modal="true" aria-labelledby="' + id + '">' +
        '<h4 id="' + id + '">' + esc(this.t("detTitle")) + "</h4><p>" + esc(this.t("detMsg")) + "</p>" + body +
        '<div class="px-btnrow px-sheetfoot">' + this.btn("detagain", this.t("again"), { disabled: st.detecting }) + '<span class="px-grow"></span>' + this.btn("detclose", this.t("closeBtn")) + "</div></div></div>";
    },

    // ----- 自动化
    automationPage: function () {
      var st = this.st, self = this, h = '<div class="px-form">';
      var permD = { off: "permOffD", read: "permReadD", operate: "permOpD" }[st.perm];
      h += this.section(this.t("ifSec"),
        '<div class="px-frow col"><span class="px-flabel">' + esc(this.t("perm")) + "</span>" + this.seg("perm", [["off", this.t("permOff")], ["read", this.t("permRead")], ["operate", this.t("permOp")]], st.perm, this.t("perm"), "wide") + this.cap(this.t(permD)) + "</div>" +
        this.row(esc(this.t("status")), st.perm === "off" ? '<span class="px-muted">' + esc(this.t("stopped")) + "</span>" : '<span class="px-ok">' + I.checkCircle + esc(this.t("listening")) + "</span>") +
        (st.perm === "off" ? "" : this.row(esc(this.t("lastCall")), '<span class="px-muted">' + esc(this.t("lastCallV")) + "</span>")),
        this.cap(this.t("ifNote")));
      h += this.section(this.t("cliSec"),
        '<div class="px-frow"><span class="px-ok">' + I.checkCircle + esc(this.t("installed")) + '</span><button type="button" class="px-btn small" disabled>' + esc(this.t("uninstall")) + "</button></div>" +
        ["proxi status", this.t("cliUse"), "proxi off", "proxi test", "proxi profiles --json"].map(function (c) { return self.codeRow(c); }).join(""),
        this.cap(this.t("cliNote")));
      var json = '{\n  "mcpServers": {\n    "proxi": {\n      "command": "/Applications/Proxi.app/Contents/MacOS/Proxi",\n      "args": ["mcp"]\n    }\n  }\n}';
      h += this.section(this.t("mcpSec"),
        '<div class="px-frow col">' + this.cap(this.t("mcpNote")) + '<span class="px-flabel">' + esc(this.t("mcpLabel")) + '</span><pre class="px-log px-code">' + esc(json) + "</pre></div>" +
        '<div class="px-frow col"><button type="button" class="px-disclose" data-act="tools" data-k="tools" aria-expanded="' + st.showTools + '"><span class="px-chev' + (st.showTools ? " is-open" : "") + '">' + I.chevron + "</span>" + esc(fmt(this.t("mcpTools"), TOOLS.length)) + "</button>" +
        (st.showTools ? '<span class="px-mono px-wrap">' + TOOLS.join(", ") + "</span>" : "") + "</div>");
      h += this.section(this.t("urlSec"),
        ["proxi://toggle", "proxi://on", "proxi://off", this.t("urlUse"), "proxi://run?tool=test_profiles"].map(function (c) { return self.codeRow(c); }).join(""),
        this.cap(this.t("urlNote")));
      var corp = this.profile("corp").name;
      var rules = [[fmt(this.t("ruleSsid"), "Office-5G"), fmt(this.t("ruleOn"), corp)], [fmt(this.t("ruleSsid"), "Home"), this.t("ruleOff")]];
      h += this.section(this.t("netSec"),
        this.toggleRow("netswitch", this.t("netToggle"), st.netSwitch) +
        this.row(esc(this.t("netNow")), '<span class="px-muted">' + esc(this.t("netNowV")) + "</span>") +
        rules.map(function (r, i) {
          return '<div class="px-frow px-rule">' + self.sw("rule" + i, st.rules[i], r[0], { mini: true }) + '<span class="px-rmatch">' + esc(r[0]) + '</span><span class="px-dim">' + I.arrow + '</span><strong class="px-raction">' + esc(r[1]) + '</strong><span class="px-grow"></span><span class="px-dim" title="' + esc(self.t("ruleDel")) + '">' + I.trash + "</span></div>";
        }).join(""),
        this.cap(this.t("netNote")));
      return h + "</div>";
    },

    // ----- 通用
    generalPage: function () {
      var st = this.st, h = '<div class="px-form">';
      h += this.section("", this.popup("lang", this.t("langLabel"), [["follow", this.t("langFollow")], ["en", "English"], ["zh", "简体中文"]], st.lang), this.cap(this.t("langNote")));
      h += this.section(this.t("startSec"), this.toggleRow("login", this.t("login"), st.login) + this.toggleRow("offonquit", this.t("offOnQuit"), st.offOnQuit));
      h += this.section(this.t("iconSec"),
        this.popup("click", this.t("leftClick"), [["panel", this.t("openPanel")], ["toggle", this.t("directToggle")]], st.click) +
        this.popup("speedshow", this.t("speed"), [["system", this.t("speedSys")], ["none", this.t("speedNone")]], st.speedShow),
        this.cap(this.t("rightNote")));
      h += this.section(this.t("proxySec"),
        this.popup("offmode", this.t("whenOff"), [["direct", this.t("offDirect")], ["restore", this.t("offRestore")]], st.offMode) +
        this.toggleRow("health", this.t("health"), st.healthOn) +
        '<div class="px-frow col"><span class="px-flabel">' + esc(this.t("testURL")) + '</span><span class="px-mono px-wrap">' + TEST_URL + "</span></div>",
        this.cap(this.t("testURLNote")));
      h += this.section(this.t("notifySec"), this.popup("notify", this.t("notifySec"), [["all", this.t("notifyAll")], ["problems", this.t("notifyProblems")], ["none", this.t("notifyNone")]], st.notify));
      h += this.section(this.t("updSec"), this.toggleRow("autoupd", this.t("autoUpd"), st.autoUpd), this.cap(this.t("updNote")));
      return h + "</div>";
    },

    // ----- 快捷键
    hotkeyPage: function () {
      var self = this, h = '<div class="px-form">';
      h += this.section(this.t("hkSec"), '<div class="px-frow"><span class="px-hkbox">⌃⌥P</span><button type="button" class="px-btn small" disabled>' + esc(this.t("clear")) + "</button></div>", this.cap(this.t("hkNote")));
      h += this.section(this.t("hkCli"), '<div class="px-frow col">' + this.cap(this.t("hkCliNote")) + "</div>" +
        ["open proxi://toggle", "open proxi://on", "open proxi://off", this.t("hkUse"), "open proxi://update"].map(function (c) { return self.codeRow(c); }).join(""));
      return h + "</div>";
    },

    // ----- iCloud 同步
    syncPage: function () {
      var st = this.st, status;
      if (st.sync === "off") status = '<span class="px-muted">' + esc(this.t("off")) + "</span>";
      else if (st.sync === "syncing") status = '<span class="px-muted">' + this.spinner() + esc(this.t("syncing")) + "</span>";
      else status = '<span class="px-stack"><span class="px-ok">' + I.icloudCheck + esc(this.t("synced")) + '</span><span class="px-caption">' + esc(fmt(this.t("lastChange"), this.t("device"), this.t(st.syncAgo))) + "</span></span>";
      var on = st.sync !== "off";
      var h = '<div class="px-form">';
      h += this.section(this.t("syncSec"),
        this.toggleRow("sync", this.t("syncToggle"), on) +
        this.row(esc(this.t("status")), status) +
        (on ? '<div class="px-frow"><span class="px-btnrow">' + this.btn("syncnow", this.t("syncNow"), { disabled: st.sync === "syncing" }) + '<button type="button" class="px-btn" disabled>' + esc(this.t("finder")) + "</button></span></div>" : ""));
      h += this.section(this.t("whatSec"), '<div class="px-frow col">' + this.cap(this.t("what1")) + this.cap(this.t("what2")) + this.cap(this.t("what3")) + "</div>");
      return h + "</div>";
    },
    dialog: function () {
      var id = this.uid + "-dlg";
      return '<div class="px-dlg-back"><div class="px-dlg" role="alertdialog" aria-modal="true" aria-labelledby="' + id + '" aria-describedby="' + id + '-m">' +
        '<span class="px-appicon big" aria-hidden="true">' + this.appIcon() + '</span><h4 id="' + id + '">' + esc(this.t("dlgTitle")) + '</h4><p id="' + id + '-m">' + esc(this.t("dlgMsg")) + "</p>" +
        this.btn("resolve", this.t("useCloud"), { v: "cloud", primary: true }) + this.btn("resolve", this.t("merge"), { v: "merge" }) + this.btn("resolve", this.t("useLocal"), { v: "local" }) + this.btn("resolve", this.t("cancel"), { v: "cancel" }) +
        "</div></div>";
    },

    // ----- 诊断
    diagnosticsPage: function () {
      var st = this.st, p = this.profile(st.active), on = st.on, h = '<div class="px-form">', self = this;
      var url = on ? this.proxyURL(p) : null, has = function (t) { return on && p.targets.indexOf(t) >= 0; };
      var val = function (v) { return v ? '<span class="px-mono px-wrap">' + esc(v) + "</span>" : '<span class="px-muted">' + esc(self.t("notSet")) + "</span>"; };
      h += this.section(this.t("sysSec"),
        this.row(esc(this.t("inEffect")), has("system") ? '<span class="px-mono px-wrap">HTTP ' + esc(p.host + ":" + p.port) + " · HTTPS " + esc(p.host + ":" + p.port) + "</span>" : '<span class="px-muted">' + esc(this.t("offDirect")) + "</span>") +
        this.row(esc(this.t("wpad")), esc(this.t("offWord"))) +
        this.row(esc(this.t("exceptions")), has("system") ? '<span class="px-mono px-wrap">' + BYPASS + "</span>" : esc(this.t("none"))) +
        this.row(esc(this.t("services")), esc(this.t("svcList"))) +
        '<div class="px-frow"><span class="px-btnrow"><button type="button" class="px-btn" disabled>' + esc(this.t("openSys")) + '</button><button type="button" class="px-btn" disabled>' + esc(this.t("clearAll")) + "</button></span></div>");
      h += this.section(this.t("envSec"), ["http_proxy", "https_proxy", "all_proxy", "no_proxy"].map(function (n) {
        return self.row('<span class="px-mono">' + n + "</span>", val(has("env") ? (n === "no_proxy" ? NO_PROXY : url) : null));
      }).join(""), this.cap(this.t("envNote")));
      h += this.section(this.t("gitSec"),
        this.row('<span class="px-mono">git http.proxy</span>', val(has("git") ? url : null)) +
        this.row('<span class="px-mono">npm proxy</span>', val(has("npm") ? url : null)) +
        this.row('<span class="px-mono">npm https-proxy</span>', val(has("npm") ? url : null)));
      h += this.section(this.t("filesSec"), this.row(esc(this.t("cfgDir")), '<span class="px-mono px-wrap">~/Library/Application Support/Proxi</span>') +
        '<div class="px-frow"><span class="px-btnrow"><button type="button" class="px-btn" disabled>' + esc(this.t("openDir")) + '</button><button type="button" class="px-btn" disabled>' + esc(this.t("refresh")) + "</button></span></div>");
      var log = on && p.id === "corp" ?
        "09:30:12 Proxi 0.13.0\n09:30:12 Wi‑Fi Office-5G → " + p.name + "\n09:30:13 networksetup -setwebproxy Wi‑Fi proxy.corp.example 3128\n09:30:13 launchctl setenv http_proxy https_proxy all_proxy no_proxy\n09:30:13 git config --global http.proxy\n09:30:13 ~/.npmrc proxy https-proxy" :
        "09:30:12 Proxi 0.13.0\n09:41:02 " + (on ? p.name : "off");
      h += this.section(this.t("logSec"), '<pre class="px-log">' + esc(log) + "</pre>");
      return h + "</div>";
    },

    // ----- 关于
    aboutPage: function () {
      var st = this.st, h = '<div class="px-form"><div class="px-about"><span class="px-appicon big" aria-hidden="true">' + this.appIcon() + "</span><strong>Proxi</strong>" +
        '<span class="px-muted">' + esc(fmt(this.t("version"), "0.13.0")) + "</span>" + this.cap(this.t("aboutLine")) +
        '<span class="px-btnrow"><button type="button" class="px-btn" disabled>GitHub</button><button type="button" class="px-btn" disabled>' + esc(this.t("issue")) + "</button></span></div>";
      h += this.section(this.t("updSec"), '<div class="px-frow">' + (st.checking ? '<span class="px-muted">' + this.spinner() + esc(this.t("checking")) + "</span>" :
        st.checked ? '<span class="px-ok">' + I.checkCircle + esc(this.t("upToDate")) + "</span>" : '<span class="px-muted">Proxi 0.13.0</span>') +
        this.btn("checkupd", this.t("checkNow"), { disabled: st.checking }) + "</div>");
      return h + "</div>";
    },

    // ---------------------------------------------------------------- actions
    setOn: function (on, profileId) {
      var st = this.st;
      st.busy = true;
      this.render();
      this.later(function () {
        st.busy = false;
        if (on) { st.active = profileId || st.next; st.next = st.active; st.on = true; }
        else st.on = false;
        this.render();
      }, reduced ? 120 : 420);
    },
    testProfiles: function () {
      var st = this.st, self = this;
      st.testingProfiles = true;
      st.results = {};
      this.render();
      this.later(function () {
        self.profiles.forEach(function (p) { st.results[p.id] = p.ms ? { ok: true, ms: p.ms + (hash(p.id + self.tick) % 5) } : { ok: false }; });
        st.testingProfiles = false;
        this.render();
      }, reduced ? 200 : 900);
    },
    detect: function () {
      var st = this.st;
      st.detecting = true;
      this.render();
      this.later(function () { st.detecting = false; this.render(); }, reduced ? 200 : 1100);
    },
    openPage: function (page) {
      var st = this.st;
      st.surface = "window";
      st.menu = null;
      st.ctx = false;
      if (page) st.page = page;
      this.render();
      this.focus("side-" + st.page);
    },
    focus: function (key) {
      var el = this.stage.querySelector('[data-k="' + key + '"]');
      if (el) el.focus({ preventScroll: true });
    },
    cycle: function (key) {
      var st = this.st, opts = {
        lang: ["follow", "en", "zh"], click: ["panel", "toggle"], speedshow: ["system", "none"],
        offmode: ["direct", "restore"], notify: ["all", "problems", "none"]
      }[key], field = { lang: "lang", click: "click", speedshow: "speedShow", offmode: "offMode", notify: "notify" }[key];
      st[field] = opts[(opts.indexOf(st[field]) + 1) % opts.length];
    },

    onContext: function (e) {
      var el = e.target.closest ? e.target.closest('[data-act="mb"]') : null;
      if (!el) return;
      e.preventDefault();
      var st = this.st;
      st.ctx = !st.ctx;
      st.menu = null;
      if (st.ctx) { st.surface = "panel"; st.open = false; st.dialog = false; st.sheet = false; }
      this.lastClick = e;
      this.render();
      var first = this.stage.querySelector(".px-cmenu .px-mi");
      if (first) first.focus({ preventScroll: true });
    },

    onClick: function (e) {
      var el = e.target.closest ? e.target.closest("[data-act]") : null;
      if (!el || !this.root.contains(el) || el.disabled) return;
      var act = el.getAttribute("data-act"), v = el.getAttribute("data-v"), st = this.st;
      if (act !== "menu" && st.menu) st.menu = null;
      if (st.ctx && act !== "mb") st.ctx = false;
      switch (act) {
        case "mb":
          if (st.ctx) { st.ctx = false; break; }
          if (st.surface === "window") { st.surface = "panel"; st.open = true; }
          else st.open = !st.open;
          break;
        case "toggle":
          if (st.busy) return;
          this.setOn(!st.on);
          return;
        case "use":
          if (st.on && st.active === v) this.setOn(false);
          else this.setOn(true, v);
          return;
        case "ctxoff": st.open = false; this.setOn(false); this.focus("mb"); return;
        case "ctxon": st.open = false; this.setOn(true); this.focus("mb"); return;
        case "ctxuse": st.open = false; this.setOn(true, v); this.focus("mb"); return;
        case "ctxupd": this.openPage("about"); this.checkUpdates(); return;
        case "menu":
          st.menu = st.menu === v ? null : v;
          this.render();
          if (st.menu) {
            var first = this.stage.querySelector(".px-menu .px-mi");
            if (first) first.focus({ preventScroll: true });
          }
          return;
        case "termcopy":
          st.copiedTerm = true;
          this.render();
          this.focus("term");
          this.later(function () { st.copiedTerm = false; this.render(); }, 1500);
          return;
        case "testprofiles": this.testProfiles(); return;
        case "page": this.openPage(v); return;
        case "quit": st.open = false; st.surface = "panel"; break;
        case "closewin":
          st.surface = "panel"; st.open = true; st.dialog = false; st.sheet = false;
          this.render();
          this.focus("mb");
          return;
        case "opendetect": st.sheet = true; st.added = {}; this.detect(); this.focus("b-detclose"); return;
        case "detagain": this.detect(); return;
        case "detclose": st.sheet = false; this.render(); this.focus("opendetect"); return;
        case "detadd": st.added[v] = true; break;
        case "perm": st.perm = v; break;
        case "netswitch": st.netSwitch = !st.netSwitch; break;
        case "rule0": case "rule1": st.rules[+act.slice(4)] = !st.rules[+act.slice(4)]; break;
        case "tools": st.showTools = !st.showTools; break;
        case "copycmd":
          try { if (navigator.clipboard) navigator.clipboard.writeText(v).catch(function () {}); } catch (err) { /* not needed for the demo */ }
          st.copiedCmd = v;
          this.later(function () { if (st.copiedCmd === v) { st.copiedCmd = null; this.render(); } }, 1500);
          break;
        case "cycle": this.cycle(v); break;
        case "login": st.login = !st.login; break;
        case "offonquit": st.offOnQuit = !st.offOnQuit; break;
        case "health": st.healthOn = !st.healthOn; break;
        case "autoupd": st.autoUpd = !st.autoUpd; break;
        case "checkupd": this.checkUpdates(); return;
        case "sync":
          if (st.sync === "off") { st.dialog = true; this.render(); this.focus("b-resolve-cloud"); return; }
          st.sync = "off";
          break;
        case "resolve":
          st.dialog = false;
          if (v !== "cancel") this.syncNow();
          this.render();
          this.focus("sync");
          return;
        case "syncnow": this.syncNow(); break;
        case "pickprofile": st.profilePick = v; st.saved = false; st.profileTest = null; break;
        case "dcolor": st.draft.color = v; st.saved = false; break;
        case "dkind": st.draft.kind = v; st.saved = false; break;
        case "psave":
          var p = this.profile(st.draft.id);
          p.name = st.draft.name || p.name; p.color = st.draft.color; p.kind = st.draft.kind; p.targets = st.draft.targets.slice();
          if (p.kind === "pac") { p.pac = "http://proxy.corp.example/proxy.pac"; p.targets = ["system"]; st.draft.targets = ["system"]; }
          st.saved = true;
          break;
        case "ptest":
          st.profileTesting = true;
          this.render();
          this.later(function () {
            var q = this.profile(st.draft.id);
            st.profileTesting = false;
            st.profileTest = q.ms ? { ok: true, ms: q.ms + (hash(q.id + this.tick) % 5) } : { ok: false };
            this.render();
            this.focus("ptest");
          }, reduced ? 150 : 800);
          return;
        default:
          if (act.indexOf("dt-") === 0) {
            var k = act.slice(3), i = st.draft.targets.indexOf(k);
            if (i >= 0) st.draft.targets.splice(i, 1); else st.draft.targets.push(k);
            st.saved = false;
          } else return;
      }
      this.render();
    },
    syncNow: function () {
      var st = this.st;
      st.sync = "syncing";
      this.later(function () { st.sync = "synced"; st.syncAgo = "justNow"; this.render(); }, reduced ? 150 : 1000);
    },
    checkUpdates: function () {
      var st = this.st;
      st.checking = true;
      this.render();
      this.later(function () { st.checking = false; st.checked = true; this.render(); }, reduced ? 150 : 900);
    },

    onKey: function (e) {
      var t = e.target, st = this.st;
      // ⌃⌥P toggles the proxy, as in the app (while focus is inside the demo).
      if (e.ctrlKey && e.altKey && (e.key === "p" || e.key === "P" || e.code === "KeyP")) {
        e.preventDefault();
        if (!st.busy) this.setOn(!st.on);
        return;
      }
      // Shift-F10 or the context-menu key opens the right-click menu from the menu bar icon.
      if (t.getAttribute && t.getAttribute("data-k") === "mb" && (e.key === "ContextMenu" || (e.shiftKey && e.key === "F10"))) {
        this.onContext({ target: t, preventDefault: function () { e.preventDefault(); } });
        return;
      }
      if (e.key === "Escape") {
        if (st.ctx) { st.ctx = false; this.render(); this.focus("mb"); e.preventDefault(); return; }
        if (st.menu) { st.menu = null; this.render(); this.focus("term"); e.preventDefault(); return; }
        if (st.dialog) { st.dialog = false; this.render(); this.focus("sync"); e.preventDefault(); return; }
        if (st.sheet) { st.sheet = false; this.render(); this.focus("opendetect"); e.preventDefault(); return; }
        if (st.surface === "panel" && st.open) { st.open = false; this.render(); this.focus("mb"); e.preventDefault(); }
        return;
      }
      var arrows = { ArrowDown: 1, ArrowRight: 1, ArrowUp: -1, ArrowLeft: -1 };
      if (!(e.key in arrows)) return;
      var dirn = arrows[e.key], group = null, sel = null;
      if (t.closest(".px-menu") || t.closest(".px-cmenu")) { group = t.closest(".px-menu") || t.closest(".px-cmenu"); sel = ".px-mi"; if (e.key === "ArrowLeft" || e.key === "ArrowRight") return; }
      else if (t.closest(".px-seg")) { group = t.closest(".px-seg"); sel = "button"; }
      else if (t.closest(".px-side")) { group = t.closest(".px-side"); sel = ".px-side-item"; if (e.key === "ArrowLeft" || e.key === "ArrowRight") return; }
      else if (t.closest(".px-colors")) { group = t.closest(".px-colors"); sel = "button"; }
      if (!group) return;
      var items = Array.prototype.slice.call(group.querySelectorAll(sel)), i = items.indexOf(t);
      if (i < 0) return;
      e.preventDefault();
      var next = items[(i + dirn + items.length) % items.length];
      if (group.classList.contains("px-seg") || group.classList.contains("px-colors") || group.classList.contains("px-side")) next.click();
      else next.focus();
      if (group.classList.contains("px-seg") || group.classList.contains("px-colors")) this.focus(next.getAttribute("data-k"));
    },
    onInput: function (e) {
      var t = e.target, k = t.getAttribute("data-k"), st = this.st;
      if (k === "dname") { st.draft.name = t.value; st.saved = false; }
      else return;
      this.render();
    }
  };

  // Each demo is built when it comes within a screen of the viewport (for a feature, when its text
  // does), so a page doesn't build every demo at load. Where the browser has no scroll anchoring,
  // a demo that grows above the viewport shifts the scroll position by the same amount.
  function make(el) {
    if (el.__built) return;
    el.__built = 1;
    var top = anchoring ? 0 : el.getBoundingClientRect().top, h0 = anchoring ? 0 : el.offsetHeight;
    try { new Demo(el); } catch (err) { if (window.console) console.error(err); }
    if (top < 0 && !anchoring) { var d = el.offsetHeight - h0; if (d) window.scrollBy(0, d); }
  }
  var anchoring = !!(window.CSS && CSS.supports && CSS.supports("overflow-anchor", "auto"));
  function init() {
    var els = document.querySelectorAll("figure.pxd:not(.pxd-ready)");
    if (!("IntersectionObserver" in window)) { Array.prototype.forEach.call(els, make); return; }
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (!e.isIntersecting) return;
        io.unobserve(e.target);
        // One task per demo, so building several never adds up to one long task.
        (e.target.__pxd || [e.target]).forEach(function (el) { setTimeout(function () { make(el); }, 0); });
      });
    }, { rootMargin: "100% 0px 100% 0px" });
    var sideways = null;
    Array.prototype.forEach.call(els, function (el) {
      // In the home page's sideways reel, a demo is built as its card comes within half a reel of view.
      var reel = el.closest(".reel");
      if (reel) {
        sideways = sideways || new IntersectionObserver(function (entries) {
          entries.forEach(function (e) { if (e.isIntersecting) { sideways.unobserve(e.target); setTimeout(function () { make(e.target); }, 0); } });
        }, { root: reel, rootMargin: "0px 50% 0px 50%" });
        sideways.observe(el);
        return;
      }
      var f = el.closest(".feature"), target = (f && f.querySelector(".feature-text")) || el;
      (target.__pxd = target.__pxd || []).push(el);
      io.observe(target);
    });
    // Keyboard users: build the rest on the first Tab, so the tab order never skips a demo.
    document.addEventListener("keydown", function onTab(e) {
      if (e.key !== "Tab") return;
      document.removeEventListener("keydown", onTab, true);
      Array.prototype.forEach.call(els, make);
    }, true);
  }
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", init);
  else init();
})();
