/* whrss.com: an interactive recreation of Proxi, the menu bar panel and the settings window.
   Everything here is sample data from fixed seeds; nothing is fetched and no proxy is touched.
   Layout, sizes and wording follow the Proxi sources (PanelView, StatusIcon, Glass,
   SettingsWindowController, ProfilesPage, NodesPage, NodeViews, SharePage, ConnectionsPage,
   SyncPage). Proxi's interface is Chinese only: the Chinese page uses its strings as they are,
   the English page shows faithful translations and says so.

   Markup: <figure class="pxd" data-lang="en|zh" data-preset="panel|profiles|nodes|share|sync">…fallback…</figure> */
(function () {
  "use strict";

  // ------------------------------------------------------------------ strings
  var S = {
    zh: {
      demo: "可交互演示 · 示例数据",
      demoLabel: "Proxi 的可交互演示，使用示例数据",
      note: "",
      mb: "Proxi 菜单栏图标，点一下打开或收起面板",
      clock: "9月30日 周三 16:14",
      hint: "点菜单栏里的开关图标打开面板。",
      // panel
      onTitle: "已开启 · %s", offTitle: "代理已关闭",
      nextSub: "下次开启 %s · %s", nodeSub: "节点 %s",
      toggleLabel: "代理开关",
      coreOff: "内置代理已停用", coreStarting: "内核正在启动…",
      autoTitle: "自动选择 · %s", nNodes: "%s 个节点",
      global: "全局", rule: "规则", ruleMode: "规则分流", globalMode: "全局代理",
      modeHelp: "全局：全部走节点；规则：按分流规则",
      collapse: "收起", nodeList: "节点列表", hideList: "收起节点列表", showList: "展开节点列表",
      searchNodes: "搜索节点", testNodes: "测试全部节点的延迟",
      auto: "自动选择", autoType: "自动", nowUsing: "当前 %s", lowest: "延迟最低的节点",
      timeout: "超时", ms: "%s ms",
      proxyGroup: "节点", direct: "直连", pickFor: "给「%s」选节点",
      kSelect: "手动选择", kUrl: "自动选择", kSelectD: "在面板里自己选，默认跟随「节点」的选择", kUrlD: "定期测延迟，自动用最低的那个",
      shareTitle: "局域网共享 · %s:%s", shareOffHelp: "关闭局域网共享",
      shareHelp: "PS5、Switch 等设备把这台 Mac 当代理服务器，享受和本机一样的网络。点击查看设置",
      upEngine: "设备和本机一样走节点", upDirect: "设备经这台 Mac 直连", upProxy: "设备的流量转发到 %s", upPac: "PAC 没法转发，设备暂时直连",
      testProfiles: "测试全部配置的连接和延迟", failed: "失败", available: "可用",
      term: "复制在当前终端里使用代理的命令", zsh: "zsh / bash（终端、iTerm）", fish: "fish",
      hotkey: "%s 开关", diagnose: "网址诊断：某个网站打不开时查原因", settings: "设置", quit: "退出 Proxi",
      quitNote: "演示里不会真的退出",
      // profiles
      pNode: "节点代理", pOffice: "公司内网", pPac: "系统代理",
      builtin: "内置代理 · %s",
      // window
      winLabel: "Proxi 设置窗口", close: "关闭窗口",
      pages: {
        profiles: ["代理配置", "每套配置可以设置系统代理、环境变量、git 和 npm，在菜单栏里一键切换"],
        nodes: ["节点与订阅", "填一个机场的订阅地址，节点就会出现在面板里；策略组给某类流量单独选节点"],
        rules: ["分流规则", "哪些网站走节点、哪些直连、哪些拦截：自定义规则最先匹配，然后按规则集的顺序，都没命中的按「其余流量」"],
        share: ["局域网共享", "让 PS5、Switch、手机这些同一局域网里的设备把这台 Mac 当代理服务器，享受和本机一样的网络"],
        connections: ["连接", "谁在访问什么、走了哪个节点、命中了哪条规则；出口 IP 和按节点累计的流量"],
        diagnose: ["网址诊断", "某个网站打不开？把链路走一遍，告诉你卡在哪、怎么修"],
        automation: ["自动化", "让命令行、快捷指令和系统里的 AI 助手按规则操作 Proxi；换了网络自动切换"],
        advanced: ["高级", "导入导出配置、增强模式、DNS、Hosts、IPv6、内核配置补丁和实时日志；不常用，有需要时再改"],
        general: ["通用", "菜单栏图标的行为、关闭代理的方式、通知"],
        hotkey: ["快捷键", "在任何程序里按下它就能开关代理"],
        sync: ["iCloud 同步", "通过 iCloud 云盘在多台 Mac 之间同步代理配置和设置"],
        diagnostics: ["诊断", "系统里各处的代理设置，以及运行日志"],
        about: ["关于", "Proxi for Mac"]
      },
      notInDemo: "这个演示只做了代理配置、节点与订阅、局域网共享、连接和 iCloud 同步这几页。",
      // profiles page
      newP: "新建", detect: "自动检测", importP: "导入",
      name: "名称", color: "颜色", kind: "类型", pac: "PAC 脚本", server: "代理服务器", host: "主机", port: "端口",
      pasteHint: "可以直接把 127.0.0.1:7890 或 socks5://127.0.0.1:1080 这样的整段地址粘到「主机」里，会自动拆开。",
      pacURL: "PAC 地址", pacOnly: "PAC 脚本只能用于系统代理",
      engineNote: "这是内置代理：地址是本机内核的端口（127.0.0.1:7890），订阅、节点、模式和端口都在「节点与订阅」页管理。",
      manageNodes: "管理节点与订阅",
      scope: "生效范围",
      tSystem: ["系统代理", "浏览器和大多数软件都走它"],
      tEnv: ["环境变量", "launchd 环境：之后新开的终端和程序生效"],
      tGit: ["git", "git clone、pull 等（全局 http.proxy）"],
      tNpm: ["npm / pnpm", "写入用户目录的 .npmrc"],
      del: "删除", testConn: "测试连接", save: "保存", saved: "已保存",
      testResult: "测试结果", testOk: "%s，%s", reachable: "经代理访问测速地址成功",
      // nodes page
      builtinSec: "内置代理", enableCore: "启用内置代理（内核 mihomo）", status: "状态",
      running: "运行中 · mihomo v1.19.31 · %s 个节点", notRunning: "未运行", starting: "正在启动…",
      coreNote: "配置列表里的「%s」就是它：开启后系统代理指向 127.0.0.1:7890，面板里可以选节点、切换模式。",
      restart: "重启内核", showLog: "查看日志", hideLog: "隐藏日志", coreLog: "内核日志",
      subs: "订阅", sub: "订阅 %s", disabled: "已停用", update: "更新", subGear: "筛选、前缀、前置代理", subDel: "删除这条订阅",
      subDetail: "%s 个节点 · 已用 7.09 GB / 200 GB · 到期 2026年12月12日 · 更新于 %s",
      subNoInfo: "%s 个节点 · 更新于 %s", ago2: "2分钟前", justNow: "刚刚",
      nameOpt: "名称（可选）", subURL: "订阅地址 https://…", add: "添加",
      subNote: "订阅每 24 小时自动更新一次。内核以 clash.meta 的身份下载，机场返回 Clash 配置或 base64 节点列表都可以。齿轮里能设筛选（只要某些地区、去掉「剩余流量」这类假节点）、名字前缀和前置代理。",
      nodesSec: "节点", sortOrig: "订阅顺序", sortName: "按名字", sortDelay: "按延迟", sortLabel: "排序",
      testAll: "测速全部", testThese: "测速这些", testingAll: "正在测速…",
      total: "共 %s 个节点", filtered: "筛出 %s / %s 个节点",
      nowAuto: "现在用的是 %s", autoLowest: "自动选延迟最低的节点",
      fav: "收藏", unfav: "取消收藏",
      nodesNote: "点一行就切换到那个节点；点星星收藏，收藏的排在最前面（面板和菜单里也是）。排序会记住，筛选条件只在这一页有效。",
      modeSec: "模式", proxyMode: "代理模式",
      globalNote: "全局代理：除局域网和自定义规则外的全部流量都走选中的节点。",
      ruleNote: "规则分流：按规则集和自定义规则决定哪些走节点、哪些直连、哪些拦截。",
      // share page
      shareSec: "共享", allowLan: "允许局域网里的设备经这台 Mac 上网",
      off: "未开启", listening: "正在监听端口 %s，局域网里的设备可以连接",
      forwardTo: "现在转发到", fwEngine: "内置代理（和本机一样的节点和分流规则）", fwDirect: "直接连接（本机没开代理）", fwPac: "直接连接（PAC 没法转发）",
      fwPacWarn: "系统代理是 PAC 脚本，没法转发给其他设备，共享的设备暂时直连",
      shareNote: "跟着本机走：本机开着内置代理，共享的设备就用同样的节点和分流规则；本机用公司代理或者别的代理软件，就转发给它；本机没开代理，就经这台 Mac 直接上网。本机切换配置时，共享的设备几秒内跟着变。",
      awakeSec: "保持唤醒", keepAwake: "共享期间不让 Mac 睡眠（显示器可以关）", onBattery: "电池供电时也保持",
      holding: "正在保持唤醒", notHolding: "未保持", afterShare: "共享开启后生效",
      awakeNote: "Mac 一睡，设备的网就断了，所以共享开着时阻止空闲睡眠；默认只在接电源时保持，免得忘了关把电用光。合盖仍然会睡眠：接上电源和外接显示器（合盖模式）可以合着盖子用。",
      addrSec: "在 PS5 / Switch 上填写", addrNote: "代理服务器地址填 %s（这台 Mac 的 Wi-Fi），端口填 %s",
      copy: "复制", copied: "已复制",
      ps5Note: "PS5：设置 → 网络 → 设置 → 设置互联网连接 → 选中正在用的网络 → 高级设置 → 代理服务器 → 「使用」，填上面的地址和端口。Switch：设置 → 互联网 → 互联网设置 → 选中网络 → 更改设置 → 代理服务器设置。手机、电脑在 Wi‑Fi 的手动代理里填同样的地址。",
      clientsSec: "正在使用的设备", clientsOff: "共享开启后，这里会列出正在使用的设备。",
      clientDetail: "%s 个连接 · %s", clientsNote: "按来源 IP 归并，只统计现在还开着的连接。右边的菜单能让某台设备固定走某个节点组、直连或者断网（设备规则在「分流规则」页里也能改）。",
      // connections page
      speedSec: "网速", upS: "↑ %s/s", downS: "↓ %s/s", peak: "两分钟内最快 %s/s",
      speedIdle: "内核运行时这里显示最近两分钟经内核的网速。",
      exitSec: "出口 IP", exitNode: "经节点", exitDirect: "本机直连", exitVia: "%s · %s",
      // sync page
      syncSec: "同步", syncToggle: "通过 iCloud 同步配置", synced: "已同步", syncing: "正在同步…",
      lastChange: "最近一次改动来自「%s」，%s", device: "MacBook Pro", ago4: "4分钟前",
      syncNow: "立即同步", finder: "在 Finder 中显示",
      whatSec: "会同步什么",
      what1: "全部代理配置，以及「通用」和「快捷键」页里的设置。登录时启动、上次使用的配置、更新提醒这些本机状态不同步。",
      what2: "文件放在 iCloud 云盘的 Proxi 文件夹里。别的 Mac 上开启同步时会读到它，可以选择用 iCloud 的、用本机的，或者把两边合并。之后任何一台的改动几秒内就会出现在其他 Mac 上；两台同时改动时，以改动时间晚的为准。",
      what3: "第一次开启时系统可能会询问是否允许 Proxi 访问 iCloud 云盘，需要允许。",
      dlgTitle: "iCloud 里已经有配置",
      dlgMsg: "来自「MacBook Pro」，更新于 2026年9月30日 16:10，有 3 套配置；本机现在有 3 套。要怎么处理？",
      useCloud: "用 iCloud 的替换本机的", merge: "合并两边的配置", useLocal: "用本机的覆盖 iCloud", cancel: "取消",
      regions: { HK: "香港", JP: "日本", TW: "台湾", SG: "新加坡", KR: "韩国", US: "美国", GB: "英国", DE: "德国", AU: "澳大利亚" }
    },
    en: {
      demo: "Interactive demo · sample data",
      demoLabel: "Interactive demo of Proxi, with sample data",
      note: "",
      mb: "Proxi in the menu bar. Click to open or close the panel",
      clock: "Wed Sep 30  16:14",
      hint: "Click the switch icon in the menu bar to open the panel.",
      onTitle: "On · %s", offTitle: "Proxy is off",
      nextSub: "Next: %s · %s", nodeSub: "Node %s",
      toggleLabel: "Proxy switch",
      coreOff: "Built-in proxy is off", coreStarting: "Starting the core…",
      autoTitle: "Auto · %s", nNodes: "%s nodes",
      global: "Global", rule: "Rule", ruleMode: "Rules", globalMode: "Global",
      modeHelp: "Global: everything goes through the node. Rule: follow the routing rules",
      collapse: "Hide", nodeList: "Nodes", hideList: "Hide the node list", showList: "Show the node list",
      searchNodes: "Search nodes", testNodes: "Test the latency of every node",
      auto: "Auto", autoType: "Auto", nowUsing: "Now %s", lowest: "The node with the lowest latency",
      timeout: "Timeout", ms: "%s ms",
      proxyGroup: "Nodes", direct: "Direct", pickFor: "Choose a node for “%s”",
      kSelect: "Manual", kUrl: "Auto-select", kSelectD: "Pick in the panel; follows the “Nodes” choice by default", kUrlD: "Tests latency regularly and uses the lowest",
      shareTitle: "LAN sharing · %s:%s", shareOffHelp: "Turn off LAN sharing",
      shareHelp: "A PS5, Switch or phone uses this Mac as its proxy server and gets the same connection. Click for settings",
      upEngine: "Devices use the same nodes as this Mac", upDirect: "Devices go online directly through this Mac", upProxy: "Device traffic is forwarded to %s", upPac: "A PAC script can’t be forwarded; devices connect directly for now",
      testProfiles: "Test the connection and latency of every profile", failed: "Failed", available: "Available",
      term: "Copy the commands that use the proxy in the current terminal", zsh: "zsh / bash (Terminal, iTerm)", fish: "fish",
      hotkey: "%s toggles", diagnose: "URL diagnosis: find out why a site won’t open", settings: "Settings", quit: "Quit Proxi",
      quitNote: "The demo doesn’t really quit",
      pNode: "Node proxy", pOffice: "Office network", pPac: "Auto proxy (PAC)",
      builtin: "Built-in proxy · %s",
      winLabel: "Proxi settings window", close: "Close the window",
      pages: {
        profiles: ["Profiles", "Each profile can set the system proxy, environment variables, git and npm; switch between them from the menu bar"],
        nodes: ["Nodes & Subscriptions", "Enter a provider’s subscription URL and its nodes appear in the panel; policy groups pick a node for one kind of traffic"],
        rules: ["Routing Rules", "Which sites go through a node, which connect directly, which are blocked: custom rules first, then the rule sets in order, then “everything else”"],
        share: ["LAN Sharing", "Let a PS5, Switch or phone on the same network use this Mac as its proxy server and get the same connection"],
        connections: ["Connections", "Who is reaching what, through which node and which rule; the exit IP and traffic per node"],
        diagnose: ["URL Diagnosis", "A site won’t open? Walk the path and see where it breaks and how to fix it"],
        automation: ["Automation", "Let the command line, Shortcuts and AI assistants control Proxi by rules; switch automatically when the network changes"],
        advanced: ["Advanced", "Import and export, Enhanced mode, DNS, hosts, IPv6, core config patches and the live log; rarely needed"],
        general: ["General", "What the menu bar icon does, how the proxy turns off, notifications"],
        hotkey: ["Shortcut", "Press it in any app to turn the proxy on or off"],
        sync: ["iCloud Sync", "Sync profiles and settings between Macs through iCloud Drive"],
        diagnostics: ["Diagnostics", "Proxy settings across the system, and the log"],
        about: ["About", "Proxi for Mac"]
      },
      notInDemo: "This demo includes only the Profiles, Nodes & Subscriptions, LAN Sharing, Connections and iCloud Sync pages.",
      newP: "New", detect: "Detect", importP: "Import",
      name: "Name", color: "Color", kind: "Type", pac: "PAC script", server: "Proxy server", host: "Host", port: "Port",
      pasteHint: "You can paste a whole address such as 127.0.0.1:7890 or socks5://127.0.0.1:1080 into “Host”; it is split up for you.",
      pacURL: "PAC URL", pacOnly: "A PAC script only applies to the system proxy",
      engineNote: "This is the built-in proxy: its address is the local core’s port (127.0.0.1:7890). Subscriptions, nodes, mode and ports are on the “Nodes & Subscriptions” page.",
      manageNodes: "Manage nodes and subscriptions",
      scope: "Applies to",
      tSystem: ["System proxy", "Browsers and most apps use it"],
      tEnv: ["Environment variables", "launchd environment: terminals and apps opened afterwards"],
      tGit: ["git", "git clone, pull and so on (global http.proxy)"],
      tNpm: ["npm / pnpm", "Written to .npmrc in your home folder"],
      del: "Delete", testConn: "Test Connection", save: "Save", saved: "Saved",
      testResult: "Test result", testOk: "%s, %s", reachable: "reached the test URL through the proxy",
      builtinSec: "Built-in proxy", enableCore: "Enable the built-in proxy (mihomo core)", status: "Status",
      running: "Running · mihomo v1.19.31 · %s nodes", notRunning: "Not running", starting: "Starting…",
      coreNote: "The “%s” profile is this proxy: turning it on points the system proxy to 127.0.0.1:7890; pick nodes and switch modes in the panel.",
      restart: "Restart Core", showLog: "Show Log", hideLog: "Hide Log", coreLog: "Core log",
      subs: "Subscriptions", sub: "Subscription %s", disabled: "Disabled", update: "Update", subGear: "Filter, prefix, dialer proxy", subDel: "Delete this subscription",
      subDetail: "%s nodes · 7.09 GB of 200 GB used · expires Dec 12, 2026 · updated %s",
      subNoInfo: "%s nodes · updated %s", ago2: "2 min ago", justNow: "just now",
      nameOpt: "Name (optional)", subURL: "Subscription URL https://…", add: "Add",
      subNote: "Subscriptions update every 24 hours. The core downloads them as clash.meta, so a Clash config or a base64 node list both work. The gear sets a filter (only some regions, no fake “traffic left” nodes), a name prefix and a dialer proxy.",
      nodesSec: "Nodes", sortOrig: "Subscription order", sortName: "By name", sortDelay: "By latency", sortLabel: "Sort",
      testAll: "Test All", testThese: "Test These", testingAll: "Testing…",
      total: "%s nodes", filtered: "%s of %s nodes",
      nowAuto: "Now using %s", autoLowest: "Picks the node with the lowest latency",
      fav: "Favorite", unfav: "Remove from favorites",
      nodesNote: "Click a row to switch to that node; star it to keep it at the top (in the panel and menus too). The sort order is remembered; filters only apply on this page.",
      modeSec: "Mode", proxyMode: "Proxy mode",
      globalNote: "Global: all traffic except the local network and custom rules goes through the chosen node.",
      ruleNote: "Rules: rule sets and custom rules decide what goes through a node, what connects directly and what is blocked.",
      shareSec: "Sharing", allowLan: "Let devices on the local network go online through this Mac",
      off: "Off", listening: "Listening on port %s; devices on the local network can connect",
      forwardTo: "Forwarding to", fwEngine: "Built-in proxy (same nodes and rules as this Mac)", fwDirect: "Direct (this Mac has no proxy on)", fwPac: "Direct (a PAC script can’t be forwarded)",
      fwPacWarn: "The system proxy is a PAC script, which can’t be forwarded to other devices; they connect directly for now",
      shareNote: "It follows this Mac: with the built-in proxy on, shared devices use the same nodes and rules; with an office proxy or another proxy app, traffic is forwarded to it; with no proxy, they go online directly through this Mac. When you switch profiles, shared devices follow within seconds.",
      awakeSec: "Keep awake", keepAwake: "Keep the Mac awake while sharing (the display may sleep)", onBattery: "Also on battery power",
      holding: "Keeping the Mac awake", notHolding: "Not keeping awake", afterShare: "Takes effect when sharing is on",
      awakeNote: "When the Mac sleeps, the devices lose their connection, so idle sleep is blocked while sharing; by default only on power, so a forgotten switch doesn’t drain the battery. Closing the lid still sleeps, unless you use clamshell mode with power and a display.",
      addrSec: "Enter on the PS5 / Switch", addrNote: "Proxy server: %s (this Mac’s Wi-Fi), port: %s",
      copy: "Copy", copied: "Copied",
      ps5Note: "PS5: Settings → Network → Settings → Set Up Internet Connection → your network → Advanced Settings → Proxy Server → Use, then enter the address and port above. Switch: System Settings → Internet → Internet Settings → your network → Change Settings → Proxy Settings. Phones and computers: the same address as a manual Wi‑Fi proxy.",
      clientsSec: "Devices using it", clientsOff: "Devices using the connection are listed here once sharing is on.",
      clientDetail: "%s connections · %s", clientsNote: "Grouped by source IP, counting only open connections. The menu on the right pins a device to a node group, direct, or no connection (device rules are also on the Routing Rules page).",
      speedSec: "Speed", upS: "↑ %s/s", downS: "↓ %s/s", peak: "Fastest in two minutes: %s/s",
      speedIdle: "While the core runs, this shows its speed over the last two minutes.",
      exitSec: "Exit IP", exitNode: "Through the node", exitDirect: "This Mac directly", exitVia: "%s · %s",
      syncSec: "Sync", syncToggle: "Sync settings through iCloud", synced: "Synced", syncing: "Syncing…",
      lastChange: "Latest change from “%s”, %s", device: "MacBook Pro", ago4: "4 min ago",
      syncNow: "Sync Now", finder: "Show in Finder",
      whatSec: "What syncs",
      what1: "All profiles, and the settings on the General and Shortcut pages. Per-Mac state such as launch at login, the last profile used and update reminders is not synced.",
      what2: "The file lives in the Proxi folder in iCloud Drive. Turning on sync on another Mac reads it: keep iCloud’s, keep this Mac’s, or merge the two. After that, changes on any Mac show up on the others within seconds; if two change at once, the later change wins.",
      what3: "The first time, macOS may ask whether Proxi may use iCloud Drive; allow it.",
      dlgTitle: "iCloud already has settings",
      dlgMsg: "From “MacBook Pro”, updated Sep 30, 2026 at 16:10, with 3 profiles; this Mac has 3. What should happen?",
      useCloud: "Replace this Mac’s with iCloud’s", merge: "Merge both", useLocal: "Overwrite iCloud with this Mac’s", cancel: "Cancel",
      regions: { HK: "Hong Kong", JP: "Japan", TW: "Taiwan", SG: "Singapore", KR: "South Korea", US: "United States", GB: "United Kingdom", DE: "Germany", AU: "Australia" }
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
    antenna: svg('<circle cx="8" cy="8" r="1.3" fill="currentColor" stroke="none"/><path d="M5.3 5.3a3.8 3.8 0 0 0 0 5.4M10.7 5.3a3.8 3.8 0 0 1 0 5.4M3.3 3.3a6.6 6.6 0 0 0 0 9.4M12.7 3.3a6.6 6.6 0 0 1 0 9.4"/>'),
    gauge: svg('<circle cx="8" cy="8" r="6.2"/><path d="m8 8 2.6-2.6"/><path d="M4.6 10.8h.01M4 8h.01M4.9 5.1h.01M8 4h.01M11.1 5.1h.01M12 8h.01" stroke-width="1.8"/>'),
    stetho: svg('<path d="M3.2 1.8H2.6v3.6a3 3 0 0 0 6 0V1.8H8"/><path d="M5.6 8.4v1.8a3.4 3.4 0 0 0 6.8 0V8.8"/><circle cx="12.4" cy="7.4" r="1.4"/>'),
    gear: svg('<path d="M13.19 6.49 15.01 6.89 15.01 9.11 13.19 9.51 12.73 10.6 13.74 12.17 12.17 13.74 10.6 12.73 9.51 13.19 9.11 15.01 6.89 15.01 6.49 13.19 5.4 12.73 3.83 13.74 2.26 12.17 3.27 10.6 2.81 9.51 .99 9.11 .99 6.89 2.81 6.49 3.27 5.4 2.26 3.83 3.83 2.26 5.4 3.27 6.49 2.81 6.89 .99 9.11 .99 9.51 2.81 10.6 3.27 12.17 2.26 13.74 3.83 12.73 5.4Z" stroke-width="1.2"/><circle cx="8" cy="8" r="2.3"/>'),
    terminal: svg('<rect x="1.6" y="2.4" width="12.8" height="11.2" rx="2.2"/><path d="m4.6 6.2 2 1.8-2 1.8M8.4 10.4h3"/>'),
    check: svg('<path d="m3.4 8.4 3 3 6.2-6.6"/>'),
    checkFill: svg('<circle cx="8" cy="8" r="7.2"/><path d="m4.8 8.2 2.2 2.2 4.2-4.6" fill="none" stroke="#fff" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/>', null, true),
    circle: svg('<circle cx="8" cy="8" r="6.6"/>'),
    up: svg('<path d="m4 10 4-4 4 4"/>'),
    down: svg('<path d="m4 6 4 4 4-4"/>'),
    updown: svg('<path d="m5 6 3-3 3 3M5 10l3 3 3-3"/>'),
    router: svg('<rect x="1.8" y="9.4" width="12.4" height="4.2" rx="1.2"/><path d="M4.4 11.5h.01M6.6 11.5h.01" stroke-width="1.8"/><path d="M11 9.4V6.8M8.9 4.8a3 3 0 0 1 4.2 0M7.5 3.3a5 5 0 0 1 7 0"/>'),
    hand: svg('<path d="M6.2 8.6V3.2a1.1 1.1 0 0 1 2.2 0v4.4M8.4 7.4V6.3a1.1 1.1 0 0 1 2.2 0v1.6M10.6 7.8a1.1 1.1 0 0 1 2.2 0v2.4c0 2.4-1.6 4.2-4 4.2h-.6c-1.4 0-2.3-.6-3.2-1.7L3.4 10.6a1.1 1.1 0 0 1 1.6-1.5l1.2 1.1"/>'),
    bolt: svg('<path d="M9.2 1.4 3.4 9h4.2l-.8 5.6L12.6 7H8.4Z"/>'),
    star: svg('<path d="m8 1.8 1.9 3.9 4.3.6-3.1 3 .7 4.3L8 11.6l-3.8 2 .7-4.3-3.1-3 4.3-.6Z"/>'),
    starFill: svg('<path d="m8 1.8 1.9 3.9 4.3.6-3.1 3 .7 4.3L8 11.6l-3.8 2 .7-4.3-3.1-3 4.3-.6Z"/>', null, true),
    trash: svg('<path d="M2.6 4h10.8M6.2 4V2.6h3.6V4M4 4l.7 9.4h6.6L12 4M6.6 6.6v4.6M9.4 6.6v4.6"/>'),
    plus: svg('<path d="M8 3v10M3 8h10"/>'),
    wand: svg('<path d="m2.4 13.6 8-8M9.2 4.4l2.4 2.4M12 1.6v2M11 2.6h2M14 5.2v1.6M13.2 6h1.6M5.4 1.8v1.6M4.6 2.6h1.6"/>'),
    importI: svg('<path d="M8 1.8v7.4M5 6.4l3 3 3-3M2.6 9.8v2.6a1.4 1.4 0 0 0 1.4 1.4h8a1.4 1.4 0 0 0 1.4-1.4V9.8"/>'),
    triangle: svg('<path d="M8 1.8 15 14H1Z"/><path d="M8 6.2v3.6M8 11.8h.01" stroke="#fff" stroke-width="1.6" stroke-linecap="round"/>', null, true),
    checkCircle: svg('<circle cx="8" cy="8" r="6.4"/><path d="m5.2 8.2 2 2 3.8-4"/>'),
    icloudCheck: svg('<path d="M4.4 12.6a3 3 0 0 1-.4-6 4.2 4.2 0 0 1 8.1-.6 3.3 3.3 0 0 1 .3 6.6Z"/><path d="m6 9.2 1.6 1.6 2.8-3"/>'),
    game: svg('<path d="M5 4.6h6a3.6 3.6 0 0 1 3.5 4.5l-.6 2.4a1.6 1.6 0 0 1-2.7.7L9.6 10.6H6.4l-1.6 1.6a1.6 1.6 0 0 1-2.7-.7l-.6-2.4A3.6 3.6 0 0 1 5 4.6Z"/><path d="M4.4 7v2M3.4 8h2M10.6 7.6h.01M12 8.6h.01" stroke-width="1.5"/>'),
    cup: svg('<path d="M2.6 5.4h8.6v4a3.6 3.6 0 0 1-3.6 3.6H6.2a3.6 3.6 0 0 1-3.6-3.6Z"/><path d="M11.2 6.4h1a1.8 1.8 0 0 1 0 3.6h-1.2M5 1.6v1.8M7.6 1.6v1.8"/>'),
    wifi: svg('<path d="M1.6 5.8a9.2 9.2 0 0 1 12.8 0M3.8 8.2a6 6 0 0 1 8.4 0M6 10.6a2.8 2.8 0 0 1 4 0"/><circle cx="8" cy="12.9" r=".9" fill="currentColor" stroke="none"/>'),
    battery: svg('<rect x="1.2" y="4.6" width="12" height="6.8" rx="1.8"/><rect x="2.6" y="6" width="7.4" height="4" rx=".8" fill="currentColor" stroke="none"/><path d="M14.6 7v2"/>'),
    // sidebar
    profiles: svg('<circle cx="3.2" cy="4" r="1.6"/><circle cx="12.8" cy="4" r="1.6"/><circle cx="8" cy="12.4" r="1.6"/><path d="M4.8 4h6.4M4 5.4l3.2 5.6M12 5.4l-3.2 5.6" stroke-dasharray="1.2 1.4"/>'),
    rules: svg('<path d="M8 14V8.4L3.6 4M8 8.4 12.4 4M2.6 6.4V3h3.4M13.4 6.4V3H10"/>'),
    list: svg('<rect x="1.6" y="2.2" width="12.8" height="11.6" rx="2"/><path d="M4.4 5.6h.01M4.4 8h.01M4.4 10.4h.01" stroke-width="1.8"/><path d="M6.6 5.6h5M6.6 8h5M6.6 10.4h5"/>'),
    stars: svg('<path d="m1.8 14.2 8.4-8.4M9 4.6l2.4 2.4"/><path d="M12.6 1.4l.5 1.1 1.1.5-1.1.5-.5 1.1-.5-1.1-1.1-.5 1.1-.5ZM5 1.8l.4.8.8.4-.8.4-.4.8-.4-.8-.8-.4.8-.4Z" fill="currentColor" stroke="none"/>'),
    sliders: svg('<path d="M2 4h12M2 8h12M2 12h12"/><circle cx="5" cy="4" r="1.5" fill="var(--px-win-bg)"/><circle cx="10.6" cy="8" r="1.5" fill="var(--px-win-bg)"/><circle cx="6.6" cy="12" r="1.5" fill="var(--px-win-bg)"/>'),
    keyboard: svg('<rect x="1" y="3.6" width="14" height="8.8" rx="1.6"/><path d="M3.6 6.4h.01M6 6.4h.01M8.4 6.4h.01M10.8 6.4h.01M12.6 6.4h.01M3.6 8.4h.01M12.6 8.4h.01" stroke-width="1.6"/><path d="M5.8 10h4.4M6 8.4h4"/>'),
    icloud: svg('<path d="M4.4 12.6a3 3 0 0 1-.4-6 4.2 4.2 0 0 1 8.1-.6 3.3 3.3 0 0 1 .3 6.6Z"/>'),
    info: svg('<circle cx="8" cy="8" r="6.4"/><path d="M8 7.2v4M8 4.8h.01" stroke-width="1.6"/>')
  };
  var PAGE_ICON = {
    profiles: "profiles", nodes: "antenna", rules: "rules", share: "router", connections: "list", diagnose: "stetho",
    automation: "stars", advanced: "sliders", general: "gear", hotkey: "keyboard", sync: "icloud", diagnostics: "stetho", about: "info"
  };
  var PAGES = ["profiles", "nodes", "rules", "share", "connections", "diagnose", "automation", "advanced", "general", "hotkey", "sync", "diagnostics", "about"];
  var BUILT = { profiles: 1, nodes: 1, share: 1, connections: 1, sync: 1 };

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
  // Generic node names; delays are drawn per node and per test round from fixed seeds.
  var NODES = [
    { id: "hk1", en: "Hong Kong 01", zh: "香港 01", type: "vless", sub: 2, rg: "HK", base: 46 },
    { id: "hk2", en: "Hong Kong 02", zh: "香港 02", type: "anytls", sub: 2, rg: "HK", base: 52 },
    { id: "hk3", en: "Hong Kong 03", zh: "香港 03", type: "trojan", sub: 2, rg: "HK", base: 61 },
    { id: "jp1", en: "Tokyo 01", zh: "东京 01", type: "hysteria2", sub: 2, rg: "JP", base: 74 },
    { id: "jp2", en: "Tokyo 02", zh: "东京 02", type: "vless", sub: 2, rg: "JP", base: 83 },
    { id: "tw1", en: "Taipei 01", zh: "台北 01", type: "vmess", sub: 2, rg: "TW", base: 69 },
    { id: "sg1", en: "Singapore 01", zh: "新加坡 01", type: "trojan", sub: 2, rg: "SG", base: 112 },
    { id: "sg2", en: "Singapore 02", zh: "新加坡 02", type: "ss", sub: 2, rg: "SG", base: 124 },
    { id: "kr1", en: "Seoul 01", zh: "首尔 01", type: "vless", sub: 2, rg: "KR", base: 96 },
    { id: "us1", en: "Los Angeles 01", zh: "洛杉矶 01", type: "hysteria2", sub: 2, rg: "US", base: 176 },
    { id: "us2", en: "San Jose 02", zh: "圣何塞 02", type: "trojan", sub: 2, rg: "US", base: 198 },
    { id: "gb1", en: "London 01", zh: "伦敦 01", type: "ss", sub: 2, rg: "GB", base: 330 },
    { id: "jp3", en: "Osaka 01", zh: "大阪 01", type: "vmess", sub: 1, rg: "JP", base: 90 },
    { id: "de1", en: "Frankfurt 01", zh: "法兰克福 01", type: "trojan", sub: 1, rg: "DE", base: 250 },
    { id: "us3", en: "Seattle 01", zh: "西雅图 01", type: "vless", sub: 1, rg: "US", base: 190 },
    { id: "au1", en: "Sydney 01", zh: "悉尼 01", type: "ss", sub: 1, rg: "AU", base: 420 }
  ];
  function delayOf(node, round) {
    var r = rng(hash(node.id) ^ Math.imul(round + 1, 2654435761));
    if (node.id === "gb1" && round % 3 === 0) return 0;         // one node times out now and then
    if (round > 0 && r() < 0.05) return 0;
    return Math.max(18, Math.round(node.base * (0.72 + 0.62 * r())));
  }
  function typeTitle(t) {
    return { ss: "SS", vmess: "VMess", vless: "VLESS", trojan: "Trojan", hysteria2: "Hysteria2", anytls: "AnyTLS" }[t] || t.toUpperCase();
  }
  var PROFILES = [
    { id: "node", nameKey: "pNode", color: "#2563eb", kind: "http", engine: true, host: "127.0.0.1", port: 7890, targets: ["system", "env", "git", "npm"] },
    { id: "office", nameKey: "pOffice", color: "#16a34a", kind: "http", host: "proxy.corp.example", port: 80, targets: ["system", "env", "git"] },
    { id: "pac", nameKey: "pPac", color: "#7c3aed", kind: "pac", pac: "http://wpad/wpad.dat", targets: ["system"] }
  ];
  var COLORS = ["#16a34a", "#2563eb", "#7c3aed", "#db2777", "#ea580c", "#0891b2"];
  var TARGETS = [["system", "tSystem"], ["env", "tEnv"], ["git", "tGit"], ["npm", "tNpm"]];
  var LAN_IP = "192.168.1.23", SHARE_PORT = 7892;

  // Bytes per second at second t: a calm base with a few bursts, the same every time.
  function speedAt(t, on) {
    var r = rng(hash("speed") ^ Math.imul(t + 7, 2246822519));
    var wave = 0.55 + 0.45 * Math.sin(t / 9) * Math.sin(t / 23 + 1);
    var burst = r() < 0.12 ? 2.4 + r() * 2.2 : 1;
    var down = Math.round((on ? 380000 : 26000) * wave * burst * (0.7 + 0.6 * r()));
    var up = Math.round((on ? 22000 : 3200) * (0.6 + 0.8 * r()) * (burst > 1 ? 1.8 : 1));
    return { up: up, down: down };
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
  function bytesText(b) {  // ByteCountFormatter, binary
    if (b < 1024) return b + " bytes";
    var units = ["KB", "MB", "GB"], v = b / 1024, i = 0;
    while (v >= 1000 && i < 2) { v /= 1024; i++; }
    return (v < 10 ? v.toFixed(1) : v < 100 ? v.toFixed(1) : Math.round(v)) + " " + units[i];
  }

  var PRESETS = {
    panel: { surface: "panel", on: true },
    profiles: { surface: "window", page: "profiles", on: true, profilePick: "office" },
    nodes: { surface: "window", page: "nodes", on: true },
    share: { surface: "window", page: "share", on: true, share: true },
    sync: { surface: "window", page: "sync", on: true },
    connections: { surface: "window", page: "connections", on: true }
  };
  var counter = 0;

  function Demo(root) {
    this.root = root;
    this.uid = "pxd" + (++counter);
    this.lang = root.getAttribute("data-lang") === "zh" ? "zh" : "en";
    this.s = S[this.lang];
    var p = PRESETS[root.getAttribute("data-preset")] || PRESETS.panel;
    this.preset = p;
    var self = this;
    this.profiles = PROFILES.map(function (pr) {
      var c = {};
      for (var k in pr) c[k] = pr[k];
      c.targets = pr.targets.slice();
      c.name = self.s[pr.nameKey];
      return c;
    });
    this.st = {
      surface: p.surface, page: p.page || "profiles", open: true,
      on: !!p.on, active: "node", next: "node", busy: false,
      core: "running", mode: "rule", sel: "auto", showNodes: true, filter: "",
      round: 0, testing: false, pending: {}, results: {}, testingProfiles: false,
      groups: [
        { id: "stream", zh: "流媒体", en: "Streaming", kind: "select", now: "sg2" },
        { id: "ai", zh: "AI 服务", en: "AI services", kind: "url", filter: "US" }
      ],
      menu: null, copiedTerm: false,
      share: !!p.share, shareState: p.share ? "listening" : "off", keepAwake: true, battery: false, copied: false,
      sub1: false, sub2: true, updating: false, sub2Updated: "ago2", showLog: false,
      favorites: {}, sort: "original", pageFilter: "",
      sync: "synced", syncAgo: "ago4", dialog: false,
      profilePick: p.profilePick || "node", draft: null, saved: false, profileTest: null, profileTesting: false
    };
    this.delays = {};
    NODES.forEach(function (n) { self.delays[n.id] = n.sub === 1 ? null : delayOf(n, 0); });
    this.tick = 240;
    this.timers = [];
    this.build();
  }

  Demo.prototype = {
    t: function (k) { return this.s[k] !== undefined ? this.s[k] : S.en[k]; },
    nodeName: function (n) { return this.lang === "zh" ? n.zh : n.en; },
    node: function (id) { for (var i = 0; i < NODES.length; i++) if (NODES[i].id === id) return NODES[i]; return null; },
    profile: function (id) { for (var i = 0; i < this.profiles.length; i++) if (this.profiles[i].id === id) return this.profiles[i]; return null; },
    nodes: function () {
      var st = this.st;
      return NODES.filter(function (n) { return n.sub === 1 ? st.sub1 : st.sub2; });
    },
    coreRunning: function () { return this.st.core === "running"; },
    autoNode: function () {
      var best = null, self = this;
      this.nodes().forEach(function (n) {
        var d = self.delays[n.id];
        if (d && (!best || d < self.delays[best.id])) best = n;
      });
      return best;
    },
    effective: function () { return this.st.sel === "auto" ? this.autoNode() : this.node(this.st.sel); },
    delayText: function (d) { return d === null || d === undefined ? "" : d > 0 ? fmt(this.t("ms"), d) : this.t("timeout"); },
    delayClass: function (d) { return d <= 0 ? "bad" : d < 300 ? "good" : d < 800 ? "warn" : "bad"; },
    summary: function (p) {
      if (p.engine) return fmt(this.t("builtin"), p.host + ":" + p.port);
      if (p.kind === "pac") return p.pac;
      if (p.kind === "socks5") return "socks5://" + p.host + ":" + p.port;
      return p.host + ":" + p.port;
    },
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
      tag.innerHTML = '<span class="pxd-tag"><span class="pxd-dot" aria-hidden="true"></span>' + esc(this.t("demo")) + "</span>" +
        (this.t("note") ? '<span class="pxd-note">' + esc(this.t("note")) + "</span>" : "");
      r.appendChild(tag);
      this.stage = stage;
      r.addEventListener("click", function (e) { self.lastClick = e; self.onClick(e); });
      r.addEventListener("keydown", function (e) { self.onKey(e); });
      r.addEventListener("input", function (e) { self.onInput(e); });
      r.addEventListener("change", function (e) { self.onChange(e); });
      document.addEventListener("click", function (e) {
        if (self.st.menu && e !== self.lastClick) { self.st.menu = null; self.render(); }
      });
      this.history = [];
      for (var i = this.tick - 119; i <= this.tick; i++) this.history.push(speedAt(i, this.st.on));
      this.render(true);
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
        self.history.push(speedAt(self.tick, self.st.on));
        if (self.history.length > 120) self.history.shift();
        self.updateSpeed();
      }, 1000);
    },

    // ---------------------------------------------------------------- render
    render: function (first) {
      var active = document.activeElement, key = null, sel = null;
      if (active && this.root.contains(active)) {
        key = active.getAttribute("data-k");
        if (active.tagName === "INPUT" && active.type === "text") sel = [active.selectionStart, active.selectionEnd];
      }
      var scrolls = {};
      Array.prototype.forEach.call(this.stage.querySelectorAll("[data-sc]"), function (el) { scrolls[el.getAttribute("data-sc")] = el.scrollTop; });
      var st = this.st, html = this.menubar();
      html += '<div class="px-scene">';
      if (st.surface === "window") html += this.windowView();
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
      var st = this.st, p = this.profile(st.active), h = this.history[this.history.length - 1];
      var color = st.on ? p.color : null;
      return '<div class="px-mb">' +
        '<button type="button" class="px-mb-item px-mb-proxi' + (st.surface === "panel" && st.open ? " is-open" : "") + '" data-act="mb" data-k="mb" aria-expanded="' + (st.surface === "panel" && st.open) + '" aria-label="' + esc(this.t("mb")) + '">' +
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
      return '<button type="button" role="switch" class="px-switch' + (opts.mini ? " mini" : "") + (opts.small ? " small" : "") + '" aria-checked="' + !!on + '" data-act="' + key + '" data-k="' + key + '"' +
        (label ? ' aria-label="' + esc(label) + '"' : "") + (opts.help ? ' title="' + esc(opts.help) + '"' : "") + (opts.disabled ? " disabled" : "") + '><span class="px-knob"></span></button>';
    },
    seg: function (key, options, value, label, cls) {
      var self = this;
      return '<div class="px-seg ' + (cls || "") + '" role="radiogroup" aria-label="' + esc(label) + '">' + options.map(function (o) {
        var on = o[0] === value;
        return '<button type="button" role="radio" aria-checked="' + on + '" tabindex="' + (on ? 0 : -1) + '" class="' + (on ? "is-on" : "") + '" data-act="' + key + '" data-v="' + o[0] + '" data-k="' + key + "-" + o[0] + '">' + esc(o[1]) + "</button>";
      }).join("") + "</div>";
    },
    spinner: function () { return '<span class="px-spin" aria-hidden="true"></span>'; },

    // ---------------------------------------------------------------- the panel
    panel: function () {
      var st = this.st, h = this.statusCard();
      if (st.core !== "off") {
        h += this.nodeCard();
        if (this.coreRunning()) h += this.groupsCard();
      }
      if (st.share) h += this.shareCard();
      h += this.profileList();
      h += this.footer();
      return h;
    },

    statusCard: function () {
      var st = this.st, p = this.profile(st.on ? st.active : st.next), title, sub;
      if (st.on) {
        title = fmt(this.t("onTitle"), p.name);
        var eff = this.effective(), res = st.results[p.id];
        if (p.engine && eff && this.coreRunning()) sub = fmt(this.t("nodeSub"), this.nodeName(eff)) + (this.delays[eff.id] ? " · " + this.delayText(this.delays[eff.id]) : "");
        else if (res && res.ok && res.ms) sub = this.summary(p) + " · " + res.ms + " ms";
        else sub = this.summary(p);
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

    nodeCard: function () {
      var st = this.st, title, sub;
      var running = this.coreRunning();
      if (st.core === "starting") { title = this.t("coreStarting"); sub = fmt(this.t("nNodes"), this.nodes().length); }
      else {
        var auto = this.autoNode(), eff = this.effective();
        title = st.sel === "auto" ? fmt(this.t("autoTitle"), auto ? this.nodeName(auto) : "…") : this.nodeName(this.node(st.sel));
        var parts = [];
        if (eff) { parts.push(typeTitle(eff.type).toUpperCase()); if (this.delays[eff.id]) parts.push(this.delayText(this.delays[eff.id])); }
        parts.push(fmt(this.t("nNodes"), this.nodes().length) + " · " + (st.mode === "global" ? this.t("global") : this.t("ruleMode")));
        sub = parts.join(" · ");
      }
      var h = '<div class="px-card px-nodes"><div class="px-nodehead">' +
        '<span class="px-ant' + (running ? " is-on" : "") + '">' + I.antenna + "</span>" +
        '<div class="px-grow"><div class="px-title sm">' + esc(title) + '</div><div class="px-sub xs">' + esc(sub) + "</div></div>" +
        '<span title="' + esc(this.t("modeHelp")) + '">' + this.seg("mode", [["global", this.t("global")], ["rule", this.t("rule")]], st.mode, this.t("proxyMode"), "mini") + "</span>" +
        '<button type="button" class="px-link" data-act="shownodes" data-k="shownodes" aria-expanded="' + st.showNodes + '" title="' + esc(st.showNodes ? this.t("hideList") : this.t("showList")) + '">' +
        esc(st.showNodes ? this.t("collapse") : this.t("nodeList")) + (st.showNodes ? I.up : I.down) + "</button></div>";
      if (st.showNodes) h += this.nodeList();
      return h + "</div>";
    },

    filteredNodes: function (text, sort) {
      var self = this, q = (text || "").trim().toLowerCase(), list = this.nodes().slice();
      if (q) list = list.filter(function (n) { return (self.nodeName(n) + " " + n.type + " " + self.t("regions")[n.rg]).toLowerCase().indexOf(q) >= 0; });
      var order = {};
      NODES.forEach(function (n, i) { order[n.id] = n.sub === 2 ? i : 100 + i; });
      list.sort(function (a, b) {
        var fa = !!self.st.favorites[a.id], fb = !!self.st.favorites[b.id];
        if (fa !== fb) return fa ? -1 : 1;
        if (sort === "name") return self.nodeName(a).localeCompare(self.nodeName(b), self.lang === "zh" ? "zh-CN" : "en");
        if (sort === "delay") {
          var da = self.delays[a.id] || 99999, db = self.delays[b.id] || 99999;
          if (da !== db) return da - db;
        }
        return order[a.id] - order[b.id];
      });
      return list;
    },

    nodeList: function () {
      var st = this.st, self = this, running = this.coreRunning();
      var list = this.filteredNodes(st.filter, st.sort);
      var auto = this.autoNode();
      var h = '<div class="px-nodelist"><div class="px-searchrow">' +
        '<input type="text" class="px-field" data-k="filter" placeholder="' + esc(this.t("searchNodes")) + '" aria-label="' + esc(this.t("searchNodes")) + '" value="' + esc(st.filter) + '" autocomplete="off" spellcheck="false">' +
        '<button type="button" class="px-iconbtn" data-act="testnodes" data-k="testnodes" title="' + esc(this.t("testNodes")) + '" aria-label="' + esc(this.t("testNodes")) + '"' + (st.testing || !running ? " disabled" : "") + ">" +
        (st.testing ? this.spinner() : I.gauge) + "</button></div>";
      var selShown = st.sel === "auto" || list.some(function (n) { return n.id === st.sel; });
      var rows = this.nodeRow("auto", this.t("auto"), this.t("autoType"), null, auto ? fmt(this.t("nowUsing"), this.nodeName(auto)) : this.t("lowest"), st.sel === "auto", !selShown);
      list.forEach(function (n) {
        rows += self.nodeRow(n.id, (st.favorites[n.id] ? "★ " : "") + self.nodeName(n), typeTitle(n.type), self.delays[n.id] === null ? undefined : self.delays[n.id], self.t("sub").replace("%s", n.sub), st.sel === n.id);
      });
      var height = Math.min(220, (list.length + 1) * 36);
      h += '<div class="px-scroll" data-sc="nodes" style="height:' + height + 'px" role="radiogroup" aria-label="' + esc(this.t("nodesSec")) + '">' + rows + "</div></div>";
      return h;
    },

    nodeRow: function (id, name, type, delay, sub, selected, tabbable) {
      var pend = this.st.pending[id], running = this.coreRunning();
      var d = delay === undefined || delay === null ? "" :
        '<span class="px-delay ' + this.delayClass(delay) + (pend ? " is-pending" : "") + '">' + esc(this.delayText(delay)) + "</span>";
      if (pend && (delay === undefined || delay === null)) d = '<span class="px-delay is-pending">…</span>';
      return '<button type="button" class="px-row px-noderow' + (selected ? " is-sel" : "") + '" role="radio" aria-checked="' + selected + '" data-act="pick" data-v="' + id + '" data-k="pick-' + id + '" tabindex="' + (selected || tabbable ? 0 : -1) + '"' + (running ? "" : " disabled") + ">" +
        '<span class="px-grow"><span class="px-nname">' + esc(name) + '</span><span class="px-nsub">' + esc(sub) + "</span></span>" +
        '<span class="px-type">' + esc(String(type).toUpperCase()) + "</span>" + d +
        '<span class="px-radio' + (selected ? " is-on" : "") + '">' + (selected ? I.checkFill : I.circle) + "</span></button>";
    },

    memberTitle: function (m, withDelay) {
      if (m === "__direct") return this.t("direct");
      if (m === "__proxy") return this.t("proxyGroup");
      if (m === "__auto") return this.t("auto");
      var n = this.node(m);
      if (!n) return "…";
      return this.nodeName(n) + (withDelay && this.delays[n.id] ? " · " + this.delayText(this.delays[n.id]) : "");
    },
    groupNow: function (g) {
      if (g.kind === "select") return g.now;
      var best = null, self = this;
      this.nodes().forEach(function (n) { if (n.rg === g.filter && self.delays[n.id] && (!best || self.delays[n.id] < self.delays[best.id])) best = n; });
      return best ? best.id : "__direct";
    },
    groupsCard: function () {
      var self = this, st = this.st;
      var rows = st.groups.map(function (g) {
        var name = self.lang === "zh" ? g.zh : g.en, now = self.groupNow(g), right;
        if (g.kind === "select") {
          var open = st.menu === "g-" + g.id;
          var members = ["__proxy", "__auto", "__direct"].concat(self.nodes().map(function (n) { return n.id; }));
          right = '<span class="px-menuwrap"><button type="button" class="px-menubtn" data-act="menu" data-v="g-' + g.id + '" data-k="menu-' + g.id + '" aria-haspopup="menu" aria-expanded="' + open + '" title="' + esc(fmt(self.t("pickFor"), name)) + '">' +
            esc(self.memberTitle(now, false)) + I.updown + "</button>" +
            (open ? '<div class="px-menu" role="menu" aria-label="' + esc(fmt(self.t("pickFor"), name)) + '">' + members.map(function (m) {
              return '<button type="button" role="menuitemradio" aria-checked="' + (m === now) + '" class="px-mi" data-act="gpick" data-g="' + g.id + '" data-v="' + m + '" data-k="gm-' + g.id + "-" + m + '">' +
                '<span class="px-mi-check">' + (m === now ? I.check : "") + "</span>" + esc(self.memberTitle(m, true)) + "</button>";
            }).join("") + "</div>" : "") + "</span>";
        } else {
          right = '<span class="px-gnow" title="' + esc(self.t("kUrl") + (self.lang === "zh" ? "：" : ": ") + self.t("kUrlD")) + '">' + esc(self.memberTitle(now, true)) + "</span>";
        }
        return '<div class="px-grow-row"><span class="px-gicon">' + (g.kind === "select" ? I.hand : I.bolt) + '</span><span class="px-gname">' + esc(name) + "</span>" + right + "</div>";
      }).join("");
      return '<div class="px-card px-groups">' + rows + "</div>";
    },

    upstream: function () {
      var st = this.st;
      if (!st.on) return "direct";
      var p = this.profile(st.active);
      if (p.engine) return "engine";
      if (p.kind === "pac") return "pac";
      return "proxy";
    },
    shareCard: function () {
      var up = this.upstream(), p = this.profile(this.st.active), sub;
      sub = up === "engine" ? this.t("upEngine") : up === "direct" ? this.t("upDirect") : up === "pac" ? this.t("upPac") : fmt(this.t("upProxy"), this.summary(p));
      if (this.st.shareState === "starting") sub = this.t("starting");
      return '<div class="px-card px-share">' +
        '<span class="px-ant' + (this.st.shareState === "listening" ? " is-on" : "") + '">' + I.router + "</span>" +
        '<button type="button" class="px-grow px-plain" data-act="page" data-v="share" data-k="sharecard" title="' + esc(this.t("shareHelp")) + '"><span class="px-title sm">' + esc(fmt(this.t("shareTitle"), LAN_IP, SHARE_PORT)) + '</span><span class="px-sub xs">' + esc(sub) + "</span></button>" +
        this.sw("share", true, this.t("shareOffHelp"), { mini: true, help: this.t("shareOffHelp") }) + "</div>";
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
      h += '<button type="button" class="px-iconbtn" data-act="page" data-v="diagnose" data-k="f-diag" title="' + esc(this.t("diagnose")) + '" aria-label="' + esc(this.t("diagnose")) + '">' + I.stetho + "</button>";
      h += '<button type="button" class="px-iconbtn" data-act="page" data-v="" data-k="f-gear" title="' + esc(this.t("settings")) + '" aria-label="' + esc(this.t("settings")) + '">' + I.gear + "</button>";
      h += '<button type="button" class="px-iconbtn" data-act="quit" data-k="f-quit" title="' + esc(this.t("quit") + " (" + this.t("quitNote") + ")") + '" aria-label="' + esc(this.t("quit")) + '">' + I.power + "</button>";
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
        this.pageBody(st.page) + "</div>" + (st.dialog ? this.dialog() : "") + "</section>";
    },
    appIcon: function () {
      return '<svg viewBox="0 0 28 28"><defs><linearGradient id="' + this.uid + '-ai" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#3b82f6"/><stop offset="1" stop-color="#1d4ed8"/></linearGradient></defs>' +
        '<rect width="28" height="28" rx="6.5" fill="url(#' + this.uid + '-ai)"/><rect x="5" y="9" width="18" height="10" rx="5" fill="#fff"/><circle cx="18" cy="14" r="3.4" fill="#22c55e"/></svg>';
    },
    pageBody: function (id) {
      if (id === "profiles") return this.profilesPage();
      if (id === "nodes") return this.nodesPage();
      if (id === "share") return this.sharePage();
      if (id === "connections") return this.connectionsPage();
      if (id === "sync") return this.syncPage();
      return '<div class="px-form"><div class="px-group"><p class="px-caption pad">' + esc(this.t("notInDemo")) + "</p></div></div>";
    },
    section: function (title, rows, captions) {
      return '<div class="px-sec">' + (title ? '<h4 class="px-sech">' + esc(title) + "</h4>" : "") + '<div class="px-group">' + rows + "</div>" + (captions || "") + "</div>";
    },
    row: function (label, right, cls) {
      return '<div class="px-frow ' + (cls || "") + '"><span class="px-flabel short">' + label + '</span><span class="px-fval">' + right + "</span></div>";
    },
    toggleRow: function (key, label, on, detail, disabled) {
      return '<div class="px-frow"><span class="px-flabel" id="' + this.uid + "-" + key + '">' + esc(label) + (detail ? '<small>' + esc(detail) + "</small>" : "") + "</span>" +
        this.sw(key, on, label, { small: false, disabled: disabled }) + "</div>";
    },
    cap: function (text, cls) { return '<p class="px-caption ' + (cls || "") + '">' + esc(text) + "</p>"; },
    btn: function (act, label, opts) {
      opts = opts || {};
      return '<button type="button" class="px-btn' + (opts.primary ? " primary" : "") + (opts.small ? " small" : "") + '" data-act="' + act + '" data-k="b-' + act + (opts.v ? "-" + opts.v : "") + '"' + (opts.disabled ? " disabled" : "") + (opts.v ? ' data-v="' + opts.v + '"' : "") + ">" + (opts.icon || "") + esc(label) + "</button>";
    },

    // ----- 代理配置
    profilesPage: function () {
      var st = this.st, self = this, pick = this.profile(st.profilePick);
      if (!st.draft || st.draft.id !== pick.id) st.draft = { id: pick.id, name: pick.name, color: pick.color, kind: pick.kind, host: pick.host, port: pick.port, targets: pick.targets.slice() };
      var d = st.draft;
      var list = '<div class="px-plist"><div class="px-group px-plistbox" role="listbox" aria-label="' + esc(this.t("pages").profiles[0]) + '">' + this.profiles.map(function (p) {
        var sel = p.id === st.profilePick, on = st.on && st.active === p.id;
        return '<button type="button" role="option" aria-selected="' + sel + '" class="px-row px-prow' + (sel ? " is-picked" : "") + '" data-act="pickprofile" data-v="' + p.id + '" data-k="pp-' + p.id + '">' +
          '<span class="px-cdot" style="--c:' + p.color + '"></span><span class="px-grow"><span class="px-pname med">' + esc(p.name) + '</span><span class="px-psub">' + esc(self.summary(p)) + "</span></span>" +
          (on ? '<span class="px-radio is-on" style="--c:' + p.color + '">' + I.checkFill + "</span>" : "") + "</button>";
      }).join("") + '</div><div class="px-btnrow">' +
        '<button type="button" class="px-btn small" disabled>' + I.plus + esc(this.t("newP")) + '</button><button type="button" class="px-btn small" disabled>' + I.wand + esc(this.t("detect")) + '</button><button type="button" class="px-btn small" disabled>' + I.importI + esc(this.t("importP")) + "</button></div></div>";
      var ed = '<div class="px-group px-editor"><div class="px-editor-body">';
      ed += this.section("", this.row(esc(this.t("name")), '<input type="text" class="px-inline" data-k="dname" value="' + esc(d.name) + '" aria-label="' + esc(this.t("name")) + '">') +
        this.row(esc(this.t("color")), '<span class="px-colors" role="radiogroup" aria-label="' + esc(this.t("color")) + '">' + COLORS.map(function (c) {
          var on = d.color === c;
          return '<button type="button" role="radio" aria-checked="' + on + '" aria-label="' + c + '" class="px-swatch" style="--c:' + c + '" data-act="dcolor" data-v="' + c + '" data-k="dc-' + c.slice(1) + '">' + (on ? I.check : "") + "</button>";
        }).join("") + "</span>") +
        (pick.engine ? "" : '<div class="px-frow col"><span class="px-flabel">' + esc(this.t("kind")) + "</span>" + this.seg("dkind", [["http", "HTTP / HTTPS"], ["socks5", "SOCKS5"], ["pac", this.t("pac")]], d.kind, this.t("kind"), "wide") + "</div>"));
      if (pick.engine) {
        ed += this.section(this.t("builtinSec"), '<div class="px-frow col">' + this.cap(this.t("engineNote")) + '<span>' + this.btn("page", this.t("manageNodes"), { v: "nodes" }) + "</span></div>");
      } else if (d.kind === "pac") {
        ed += this.section(this.t("pac"), this.row(esc(this.t("pacURL")), '<span class="px-mono">' + esc(pick.pac || "http://127.0.0.1:7890/proxy.pac") + "</span>"));
      } else {
        ed += this.section(this.t("server"), this.row(esc(this.t("host")), esc(d.host || "127.0.0.1")) + this.row(esc(this.t("port")), esc(String(d.port || 7890))), this.cap(this.t("pasteHint")));
      }
      var pacOnly = d.kind === "pac";
      ed += this.section(this.t("scope"), TARGETS.map(function (tg) {
        var on = d.targets.indexOf(tg[0]) >= 0 && !(pacOnly && tg[0] !== "system");
        return self.toggleRow("dt-" + tg[0], self.t(tg[1])[0], on, self.t(tg[1])[1], pacOnly && tg[0] !== "system");
      }).join(""), pacOnly ? this.cap(this.t("pacOnly")) : "");
      if (st.profileTest) ed += this.section(this.t("testResult"), '<div class="px-frow"><span class="px-ok">' + I.checkCircle + esc(fmt(this.t("testOk"), st.profileTest + " ms", this.t("reachable"))) + "</span></div>");
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

    // ----- 节点与订阅
    nodesPage: function () {
      var st = this.st, self = this, running = this.coreRunning(), engineP = this.profile("node");
      var status = st.core === "running" ? '<span class="px-ok">' + I.checkCircle + esc(fmt(this.t("running"), this.nodes().length)) + "</span>" :
        st.core === "starting" ? '<span class="px-muted">' + this.spinner() + esc(this.t("starting")) + "</span>" : '<span class="px-muted">' + esc(this.t("notRunning")) + "</span>";
      var h = '<div class="px-form">';
      h += this.section(this.t("builtinSec"),
        this.toggleRow("core", this.t("enableCore"), st.core !== "off") +
        this.row(esc(this.t("status")), status) +
        '<div class="px-frow col">' + this.cap(fmt(this.t("coreNote"), engineP.name)) + '<span class="px-btnrow">' + this.btn("restart", this.t("restart"), { disabled: st.core === "off" }) + this.btn("log", st.showLog ? this.t("hideLog") : this.t("showLog")) + "</span></div>");
      var subRow = function (n) {
        var on = n === 1 ? st.sub1 : st.sub2, count = NODES.filter(function (x) { return x.sub === n; }).length;
        var detail = !on ? self.t("disabled") : n === 2 ? fmt(self.t("subDetail"), count, self.t(st.sub2Updated)) : fmt(self.t("subNoInfo"), count, self.t("justNow"));
        var url = n === 1 ? "https://sub.example.com/sub?token=7b3e9f1c4d8a2e6b0c5d9f3a" : "https://sub.example.net/v1/subscribe?token=4E7A-9C1B-3D5F-8A2C";
        return '<div class="px-frow px-subrow">' + self.sw("sub" + n, on, fmt(self.t("sub"), n), { small: true }) +
          '<span class="px-grow"><span class="px-subname">' + esc(fmt(self.t("sub"), n)) + '</span><span class="px-caption trunc">' + esc(url) + '</span><span class="px-caption">' + esc(detail) + "</span></span>" +
          '<span class="px-dim" title="' + esc(self.t("subGear")) + '">' + I.gear + "</span>" +
          (st.updating === n ? self.spinner() : '<button type="button" class="px-btn small" data-act="subupdate" data-v="' + n + '" data-k="subup' + n + '"' + (on && running ? "" : " disabled") + ">" + esc(self.t("update")) + "</button>") +
          '<span class="px-dim" title="' + esc(self.t("subDel")) + '">' + I.trash + "</span></div>";
      };
      h += this.section(this.t("subs"), subRow(1) + subRow(2) +
        '<div class="px-frow px-addrow"><span class="px-ghost" style="flex:0 0 32%">' + esc(this.t("nameOpt")) + '</span><span class="px-ghost px-grow">' + esc(this.t("subURL")) + '</span><button type="button" class="px-btn small" disabled>' + esc(this.t("add")) + "</button></div>" +
        '<div class="px-frow col">' + this.cap(this.t("subNote")) + "</div>");
      // 节点
      var list = this.filteredNodes(st.pageFilter, st.sort), all = this.nodes().length, auto = this.autoNode();
      var filtering = !!st.pageFilter.trim();
      var nh = '<div class="px-frow px-filterbar"><input type="text" class="px-field px-grow" data-k="pagefilter" placeholder="' + esc(this.t("searchNodes")) + '" aria-label="' + esc(this.t("searchNodes")) + '" value="' + esc(st.pageFilter) + '" autocomplete="off" spellcheck="false">' +
        '<select class="px-select" data-k="sort" aria-label="' + esc(this.t("sortLabel")) + '">' + [["original", "sortOrig"], ["name", "sortName"], ["delay", "sortDelay"]].map(function (o) {
          return '<option value="' + o[0] + '"' + (st.sort === o[0] ? " selected" : "") + ">" + esc(self.t(o[1])) + "</option>";
        }).join("") + "</select>" +
        '<button type="button" class="px-btn" data-act="testnodes" data-k="testall"' + (st.testing || !running ? " disabled" : "") + ">" + esc(st.testing ? this.t("testingAll") : filtering ? this.t("testThese") : this.t("testAll")) + "</button></div>";
      nh += '<div class="px-frow"><span class="px-caption">' + esc(filtering ? fmt(this.t("filtered"), list.length, all) : fmt(this.t("total"), all)) + "</span></div>";
      nh += this.pageNodeRow("auto", this.t("auto"), auto ? fmt(this.t("nowAuto"), this.nodeName(auto)) : this.t("autoLowest"), this.t("autoType"), null, st.sel === "auto", false);
      list.forEach(function (n) {
        nh += self.pageNodeRow(n.id, self.nodeName(n), fmt(self.t("sub"), n.sub) + " · " + self.t("regions")[n.rg], typeTitle(n.type), self.delays[n.id], st.sel === n.id, true);
      });
      nh += '<div class="px-frow col">' + this.cap(this.t("nodesNote")) + "</div>";
      h += this.section(this.t("nodesSec"), nh);
      h += this.section(this.t("modeSec"), '<div class="px-frow col">' + this.seg("mode", [["rule", this.t("ruleMode")], ["global", this.t("globalMode")]], st.mode, this.t("proxyMode"), "wide") + "</div>" +
        '<div class="px-frow col">' + this.cap(st.mode === "global" ? this.t("globalNote") : this.t("ruleNote")) + "</div>");
      if (st.showLog) {
        h += this.section(this.t("coreLog"), '<pre class="px-log">16:10:02 INF [Config] initial compatible provider 订阅 2\n16:10:02 INF inbound mixed://127.0.0.1:7890 create success.\n16:10:03 INF RESTful API listening at: 127.0.0.1:9097\n16:14:21 INF [TCP] 127.0.0.1:52144 --> example.com:443 match RuleSet(proxy) using 节点[' + esc(auto ? auto.zh : "") + "]</pre>");
      }
      return h + "</div>";
    },
    pageNodeRow: function (id, name, sub, type, delay, selected, starable) {
      var st = this.st, fav = !!st.favorites[id], pend = st.pending[id], running = this.coreRunning();
      var d = delay === null || delay === undefined ? (pend ? "…" : "") : this.delayText(delay);
      return '<div class="px-frow px-pnode"><button type="button" class="px-plain px-grow px-pnbtn" role="radio" aria-checked="' + selected + '" data-act="pick" data-v="' + id + '" data-k="ppick-' + id + '"' + (running ? "" : " disabled") + ">" +
        '<span class="px-radio' + (selected ? " is-on" : "") + '">' + (selected ? I.checkFill : I.circle) + '</span><span class="px-grow"><span class="px-pnname' + (selected ? " is-on" : "") + '">' + esc(name) + '</span><span class="px-caption">' + esc(sub) + "</span></span>" +
        '<span class="px-type">' + esc(type) + '</span><span class="px-delay wide ' + (delay || delay === 0 ? this.delayClass(delay) : "") + (pend ? " is-pending" : "") + '">' + esc(d) + "</span></button>" +
        (starable ? '<button type="button" class="px-star' + (fav ? " is-on" : "") + '" data-act="fav" data-v="' + id + '" data-k="fav-' + id + '" aria-pressed="' + fav + '" aria-label="' + esc((fav ? this.t("unfav") : this.t("fav")) + " " + name) + '" title="' + esc(fav ? this.t("unfav") : this.t("fav")) + '">' + (fav ? I.starFill : I.star) + "</button>" : '<span class="px-star" aria-hidden="true"></span>') + "</div>";
    },

    // ----- 局域网共享
    sharePage: function () {
      var st = this.st, up = this.upstream(), p = this.profile(st.active);
      var status = st.shareState === "listening" ? '<span class="px-ok">' + I.checkCircle + esc(fmt(this.t("listening"), SHARE_PORT)) + "</span>" :
        st.shareState === "starting" ? '<span class="px-muted">' + this.spinner() + esc(this.t("starting")) + "</span>" : '<span class="px-muted">' + esc(this.t("off")) + "</span>";
      var fw = up === "engine" ? this.t("fwEngine") : up === "direct" ? this.t("fwDirect") : up === "pac" ? this.t("fwPac") : this.summary(p);
      var h = '<div class="px-form">';
      h += this.section(this.t("shareSec"),
        this.toggleRow("share", this.t("allowLan"), st.share) +
        this.row(esc(this.t("status")), status) +
        this.row(esc(this.t("forwardTo")), '<span class="px-fwd">' + esc(fw) + (up === "pac" ? '<small class="px-warn">' + esc(this.t("fwPacWarn")) + "</small>" : "") + "</span>") +
        '<div class="px-frow col">' + this.cap(this.t("shareNote")) + "</div>");
      var holding = st.share && st.keepAwake;
      h += this.section(this.t("awakeSec"),
        this.toggleRow("awake", this.t("keepAwake"), st.keepAwake) +
        (st.keepAwake ? this.toggleRow("battery", this.t("onBattery"), st.battery) : "") +
        this.row(esc(this.t("status")), holding ? '<span class="px-ok">' + I.cup + esc(this.t("holding")) + "</span>" : '<span class="px-muted">' + esc(st.share && st.keepAwake ? this.t("notHolding") : this.t("afterShare")) + "</span>") +
        '<div class="px-frow col">' + this.cap(this.t("awakeNote")) + "</div>");
      h += this.section(this.t("addrSec"),
        '<div class="px-frow px-addr"><span class="px-grow"><span class="px-bigaddr">' + LAN_IP + " : " + SHARE_PORT + '</span><span class="px-caption">' + esc(fmt(this.t("addrNote"), LAN_IP, SHARE_PORT)) + "</span></span>" +
        '<button type="button" class="px-btn" data-act="copyaddr" data-k="copyaddr" aria-live="polite">' + esc(st.copied ? this.t("copied") : this.t("copy")) + "</button></div>" +
        '<div class="px-frow col">' + this.cap(this.t("ps5Note")) + "</div>");
      var clients = st.shareState === "listening"
        ? '<div class="px-frow px-client"><span class="px-accent">' + I.game + '</span><span class="px-grow"><span class="px-mono strong">192.168.1.40</span><span class="px-caption trunc">' + esc(fmt(this.t("clientDetail"), 6, "store.playstation.com")) + "</span></span></div>" +
          '<div class="px-frow col">' + this.cap(this.t("clientsNote")) + "</div>"
        : '<div class="px-frow col">' + this.cap(this.t("clientsOff")) + "</div>";
      h += this.section(this.t("clientsSec"), clients);
      return h + "</div>";
    },

    // ----- 连接
    connectionsPage: function () {
      var st = this.st, eff = this.effective(), running = this.coreRunning();
      var h = '<div class="px-form">';
      h += this.section(this.t("speedSec"), running ? '<div class="px-frow col">' + this.speedChart() + '<div class="px-legend" data-speed="legend">' + this.legend() + "</div></div>"
        : '<div class="px-frow col">' + this.cap(this.t("speedIdle")) + "</div>");
      var region = eff ? this.t("regions")[eff.rg] : "";
      h += this.section(this.t("exitSec"),
        this.row(esc(this.t("exitNode")) + (eff ? " · " + esc(this.nodeName(eff)) : ""), '<span class="px-mono">203.0.113.' + (eff ? 10 + (hash(eff.id) % 200) : 1) + "</span> · " + esc(region)) +
        this.row(esc(this.t("exitDirect")), '<span class="px-mono">198.51.100.24</span>'));
      return h + "</div>";
    },
    engineSpeeds: function () {
      var on = this.st.on && this.profile(this.st.active).engine;
      return this.history.map(function (s) { return on ? s : { up: Math.round(s.up * 0.04), down: Math.round(s.down * 0.03) }; });
    },
    speedChart: function () {
      var data = this.engineSpeeds(), W = 400, H = 120;
      var max = 1;
      data.forEach(function (s) { max = Math.max(max, s.down, s.up); });
      var nice = Math.pow(1024, Math.floor(Math.log(max) / Math.log(1024)));
      var top = Math.ceil(max / nice / 2) * 2 * nice || 1;
      var x = function (i) { return (i / (data.length - 1) * W).toFixed(1); };
      var y = function (v) { return (H - v / top * (H - 6)).toFixed(1); };
      var line = function (k) { return data.map(function (s, i) { return (i ? "L" : "M") + x(i) + " " + y(s[k]); }).join(""); };
      var grid = "", labels = "";
      for (var g = 0; g <= 2; g++) {
        var v = top * g / 2, yy = y(v);
        grid += '<line x1="0" x2="' + W + '" y1="' + yy + '" y2="' + yy + '"/>';
        labels += '<span style="top:' + (yy / H * 100).toFixed(1) + '%">' + esc(bytesText(Math.round(v))) + "/s</span>";
      }
      return '<div class="px-chart" data-speed="chart"><div class="px-ylab" aria-hidden="true">' + labels + '</div><svg viewBox="0 0 ' + W + " " + H + '" preserveAspectRatio="none" role="img" aria-label="' + esc(this.t("speedSec")) + '">' +
        '<g class="px-grid">' + grid + '</g><path class="px-line down" d="' + line("down") + '"/><path class="px-line up" d="' + line("up") + '"/></svg></div>';
    },
    legend: function () {
      var data = this.engineSpeeds(), last = data[data.length - 1], peak = 0;
      data.forEach(function (s) { peak = Math.max(peak, s.up, s.down); });
      return '<span class="up">' + esc(fmt(this.t("upS"), bytesText(last.up))) + '</span><span class="down">' + esc(fmt(this.t("downS"), bytesText(last.down))) + '</span><span class="px-grow"></span><span class="px-muted">' + esc(fmt(this.t("peak"), bytesText(peak))) + "</span>";
    },
    updateSpeed: function () {
      var last = this.history[this.history.length - 1];
      var up = this.stage.querySelector('[data-speed="up"]'), down = this.stage.querySelector('[data-speed="down"]');
      if (up) up.textContent = compact(last.up);
      if (down) down.textContent = compact(last.down);
      var chart = this.stage.querySelector('[data-speed="chart"]');
      if (chart) {
        var tmp = document.createElement("div");
        tmp.innerHTML = this.speedChart();
        chart.parentNode.replaceChild(tmp.firstChild, chart);
        var lg = this.stage.querySelector('[data-speed="legend"]');
        if (lg) lg.innerHTML = this.legend();
      }
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
    testNodes: function () {
      var st = this.st, self = this;
      if (st.testing || !this.coreRunning()) return;
      st.testing = true;
      st.round++;
      var list = this.filteredNodes(st.surface === "window" ? st.pageFilter : st.filter, "original");
      list.forEach(function (n) { st.pending[n.id] = true; });
      this.render();
      var spent = 0;
      list.forEach(function (n, i) {
        var d = delayOf(n, st.round);
        var at = 180 + i * 70 + (d > 0 ? Math.min(d, 400) : 520);
        spent = Math.max(spent, at);
        self.later(function () { self.delays[n.id] = d; delete st.pending[n.id]; self.render(); }, at);
      });
      this.later(function () { st.testing = false; st.pending = {}; this.render(); }, spent + 40);
    },
    testProfiles: function () {
      var st = this.st, self = this;
      st.testingProfiles = true;
      st.results = {};
      this.render();
      this.later(function () {
        var r = rng(hash("profiles") + st.round * 31 + this.tick);
        self.profiles.forEach(function (p) {
          if (p.engine) {
            var eff = self.effective();
            st.results[p.id] = { ok: true, ms: eff && self.delays[eff.id] ? self.delays[eff.id] + 40 : 120 };
          } else if (p.kind === "pac") st.results[p.id] = { ok: true, ms: null };
          else st.results[p.id] = { ok: false };
        });
        r();
        st.testingProfiles = false;
        this.render();
      }, reduced ? 200 : 900);
    },
    openPage: function (page) {
      var st = this.st;
      st.surface = "window";
      st.menu = null;
      if (page) st.page = page;
      this.render();
      this.focus("side-" + st.page);
    },
    focus: function (key) {
      var el = this.stage.querySelector('[data-k="' + key + '"]');
      if (el) el.focus({ preventScroll: true });
    },

    onClick: function (e) {
      var el = e.target.closest ? e.target.closest("[data-act]") : null;
      if (!el || !this.root.contains(el) || el.disabled) return;
      var act = el.getAttribute("data-act"), v = el.getAttribute("data-v"), st = this.st, self = this;
      if (act !== "menu" && act !== "gpick" && st.menu) st.menu = null;
      switch (act) {
        case "mb":
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
        case "mode": st.mode = v; break;
        case "shownodes": st.showNodes = !st.showNodes; break;
        case "pick":
          st.sel = v;
          st.next = "node";
          if (st.on && st.active !== "node") { this.setOn(true, "node"); return; }
          break;
        case "testnodes": this.testNodes(); return;
        case "menu":
          st.menu = st.menu === v ? null : v;
          this.render();
          if (st.menu) {
            var first = this.stage.querySelector('.px-menu [aria-checked="true"]') || this.stage.querySelector(".px-menu .px-mi");
            if (first) first.focus({ preventScroll: true });
          }
          return;
        case "gpick":
          st.groups.forEach(function (g) { if (g.id === el.getAttribute("data-g")) g.now = v; });
          st.menu = null;
          this.render();
          this.focus("menu-" + el.getAttribute("data-g"));
          return;
        case "termcopy":
          st.copiedTerm = true;
          this.render();
          this.focus("term");
          this.later(function () { st.copiedTerm = false; this.render(); }, 1500);
          return;
        case "share":
          st.share = !st.share;
          if (st.share) {
            st.shareState = "starting";
            this.later(function () { if (st.share) { st.shareState = "listening"; this.render(); } }, reduced ? 150 : 700);
          } else st.shareState = "off";
          break;
        case "awake": st.keepAwake = !st.keepAwake; break;
        case "battery": st.battery = !st.battery; break;
        case "copyaddr":
          try { if (navigator.clipboard) navigator.clipboard.writeText(LAN_IP + ":" + SHARE_PORT).catch(function () {}); } catch (err) { /* not needed for the demo */ }
          st.copied = true;
          this.later(function () { st.copied = false; this.render(); }, 1500);
          break;
        case "testprofiles": this.testProfiles(); return;
        case "page": this.openPage(v); return;
        case "quit": st.open = false; break;
        case "closewin":
          st.surface = "panel"; st.open = true; st.dialog = false;
          this.render();
          this.focus("mb");
          return;
        case "core":
          if (st.core === "off") {
            st.core = "starting";
            this.later(function () { st.core = "running"; this.render(); }, reduced ? 150 : 800);
          } else st.core = "off";
          break;
        case "restart":
          st.core = "starting";
          this.later(function () { st.core = "running"; this.render(); }, reduced ? 150 : 900);
          break;
        case "log": st.showLog = !st.showLog; break;
        case "sub1": case "sub2":
          st[act] = !st[act];
          if (!this.nodes().length) st[act] = true;
          if (st.sel !== "auto" && !this.nodes().some(function (n) { return n.id === st.sel; })) st.sel = "auto";
          break;
        case "subupdate":
          st.updating = +v;
          this.later(function () {
            st.updating = false;
            if (+v === 2) st.sub2Updated = "justNow";
            this.render();
            this.focus("subup" + v);
          }, reduced ? 150 : 900);
          break;
        case "fav": st.favorites[v] = !st.favorites[v]; break;
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
          if (p.kind === "pac" && !p.pac) p.pac = "http://127.0.0.1:7890/proxy.pac";
          st.saved = true;
          break;
        case "ptest":
          st.profileTesting = true;
          this.render();
          this.later(function () {
            st.profileTesting = false;
            st.profileTest = 38 + (hash(st.draft.id + this.tick) % 60);
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
      void self;
    },
    syncNow: function () {
      var st = this.st;
      st.sync = "syncing";
      this.later(function () { st.sync = "synced"; st.syncAgo = "justNow"; this.render(); }, reduced ? 150 : 1000);
    },

    onKey: function (e) {
      var t = e.target, st = this.st;
      // ⌃⌥P toggles the proxy, as in the app (while focus is inside the demo).
      if (e.ctrlKey && e.altKey && (e.key === "p" || e.key === "P" || e.code === "KeyP")) {
        e.preventDefault();
        if (!st.busy) this.setOn(!st.on);
        return;
      }
      if (e.key === "Escape") {
        if (st.menu) {
          var trig = st.menu === "term" ? "term" : "menu-" + st.menu.slice(2);
          st.menu = null; this.render(); this.focus(trig); e.preventDefault(); return;
        }
        if (st.dialog) { st.dialog = false; this.render(); this.focus("sync"); e.preventDefault(); return; }
        if (t.getAttribute && t.getAttribute("data-k") === "filter" && st.filter) { st.filter = ""; this.render(); e.preventDefault(); return; }
        if (st.surface === "panel" && st.open) { st.open = false; this.render(); this.focus("mb"); e.preventDefault(); }
        return;
      }
      var arrows = { ArrowDown: 1, ArrowRight: 1, ArrowUp: -1, ArrowLeft: -1 };
      if (!(e.key in arrows)) return;
      var dirn = arrows[e.key], group = null, sel = null;
      if (t.closest(".px-menu")) { group = t.closest(".px-menu"); sel = ".px-mi"; if (e.key === "ArrowLeft" || e.key === "ArrowRight") return; }
      else if (t.closest(".px-seg")) { group = t.closest(".px-seg"); sel = "button"; }
      else if (t.closest(".px-side")) { group = t.closest(".px-side"); sel = ".px-side-item"; if (e.key === "ArrowLeft" || e.key === "ArrowRight") return; }
      else if (t.closest(".px-colors")) { group = t.closest(".px-colors"); sel = "button"; }
      else if (t.closest(".px-scroll")) { group = t.closest(".px-scroll"); sel = ".px-noderow"; }
      if (!group) return;
      var items = Array.prototype.slice.call(group.querySelectorAll(sel)), i = items.indexOf(t);
      if (i < 0) return;
      e.preventDefault();
      var next = items[(i + dirn + items.length) % items.length];
      if (group.classList.contains("px-seg") || group.classList.contains("px-colors")) next.click();
      else if (group.classList.contains("px-side")) next.click();
      else next.focus();
      if (group.classList.contains("px-seg") || group.classList.contains("px-colors")) this.focus(next.getAttribute("data-k"));
    },
    onInput: function (e) {
      var t = e.target, k = t.getAttribute("data-k"), st = this.st;
      if (k === "filter") st.filter = t.value;
      else if (k === "pagefilter") st.pageFilter = t.value;
      else if (k === "dname") { st.draft.name = t.value; st.saved = false; }
      else return;
      this.render();
    },
    onChange: function (e) {
      var t = e.target;
      if (t.getAttribute("data-k") === "sort") { this.st.sort = t.value; this.render(); }
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
