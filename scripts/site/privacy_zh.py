"""Simplified Chinese privacy policies. Keep them factually identical to the
English ones in privacy.py: when one changes, change the other and the date."""

GITHUB_UPDATE = lambda when, ua: [
    "GitHub（<code>api.github.com</code>、<code>github.com</code> 和 GitHub 的下载服务器）",
    when,
    f"请求最新版本的信息；安装更新时，下载发布包和它的校验文件。请求中带有应用名称和版本号（<code>{ua}</code>），不包含任何关于你或你数据的信息。",
]

POP = {
    "version": "0.25",
    "meta_desc": "没有统计，没有账号，数据留在你的 Mac 上。",
    "summary": [
        "没有统计分析，没有账号，没有广告，也没有我的服务器。我什么都不收集。",
        "剪贴板历史、设置和插件都留在你的 Mac 上。API 密钥保存在 macOS 钥匙串里。",
        "只有当你使用需要某项服务的功能时，文字才会离开你的 Mac，而且发往的是你自己选的服务：AI（你自己的接口）或 DeepL。",
        "Pop 会连接 GitHub 检查更新，打开插件库时也会从那里加载插件列表。",
    ],
    "local_intro": "Pop 需要的一切都保存在本地。苹果的离线翻译、系统自带的 Apple 智能模型（macOS 26）、图片文字识别和所有换算都在你的 Mac 上完成。",
    "local": [
        ["设置（圆盘布局、直达规则、快捷键、翻译和 AI 设置，不含密钥）", "<code>UserDefaults</code>（<code>io.github.whrss9527.pop</code>）", "可以导出到你选择的文件。"],
        ["自己添加的插件", "<code>~/Library/Application Support/Pop/Plugins/</code>", "每个插件一个 JSON 文件。"],
        ["剪贴板历史", "<code>~/Library/Application Support/Pop/Clipboard/</code>（SQLite 数据库和图片）", "包括从复制的图片里识别出的文字，用于搜索。按时间和条数自动清理；密码管理器标记为隐藏的内容从不记录；可以排除指定的应用。"],
        ["生词本", "<code>~/Library/Application Support/Pop/Vocabulary.json</code>", "你从翻译卡片里收藏的单词。"],
        ["收集箱", "<code>~/Documents/Pop 收集箱.md</code>", "只有使用“收集箱”功能时才会创建。"],
        ["AI API 密钥、DeepL 密钥", "这台 Mac 的 macOS 钥匙串", "从不同步，也不导出。"],
        ["从手机收到的文件", "<code>~/Downloads</code>", "只在使用“传到手机”时。"],
    ],
    "net_intro": "Pop 只在下列情况下连接下列地址：",
    "network": [
        GITHUB_UPDATE("开启“自动检查更新”时（默认开启，可以关闭），启动时和之后每 6 小时检查一次；手动检查时。", "Pop/&lt;version&gt; (macOS)"),
        ["插件库（<code>raw.githubusercontent.com</code>，连不上时改用 <code>cdn.jsdelivr.net</code>）", "打开插件库，或从插件库安装、更新插件时。", "请求插件库索引和插件文件，不含任何关于你的信息。"],
        ["你配置的 AI 接口", "只在使用 AI 功能或 AI 插件时。", "选中的文字、你的指令和你的 API 密钥，发送到你填写的地址。只有本机和局域网地址允许使用不加密的 <code>http://</code>。如果在 macOS 26 上使用苹果的本机模型，数据不会离开你的 Mac。"],
        ["DeepL（<code>api.deepl.com</code> 或 <code>api-free.deepl.com</code>）", "只在你选择用 DeepL 翻译时。", "要翻译的文字、目标语言和你的 DeepL 密钥。"],
        ["你要展开的链接", "只在使用“展开短链接”时。", "请求这个链接以及它跳转经过的每个地址，以便显示最终地址。"],
        ["你自己的插件和脚本", "运行它们时。", "取决于插件本身：打开网址，或运行你编写或安装的 shell 脚本、JavaScript 或快捷指令。从插件库安装 shell 脚本前，Pop 会先把脚本给你看；<code>pop://</code> 链接要运行脚本时，Pop 会先征求你的同意。"],
        ["局域网里你自己的手机", "只在“传到手机”开启期间。", "Pop 在你的 Wi-Fi 上提供一个临时网页，用随机令牌保护；关闭共享或闲置 10 分钟后停止。数据不经过互联网。"],
    ],
    "icloud": """<h2>iCloud</h2>
        <p>GitHub 上发布的版本不包含 iCloud 同步。在包含该功能的版本里，并且只在同步开启期间，Pop 会把你的设置和自己添加的插件存到你自己的 iCloud 键值存储中，让你的其他 Mac 读取。剪贴板历史、生词本和 API 密钥从不同步。这些数据由苹果在你的 iCloud 账号下保管，我无法访问。</p>""",
    "permissions": [
        ["辅助功能（必需）", "用来察觉长按右键、读取你正在用的应用里选中的文字，以及在你选择“替换原文”时把结果粘贴回去。"],
        ["屏幕录制", "只用于截图识字和翻译、扫描二维码、截图标注和屏幕标尺。"],
        ["提醒事项或日历", "只用于“加到提醒事项”，第一次使用时才会请求。"],
        ["通知", "告诉你有新版本，以及计时结束。"],
        ["本地网络", "只用于“传到手机”。"],
    ],
    "extra": "<h2>网页搜索和链接</h2><p>搜索、打开链接和地图等功能会把文字或地址交给你的默认浏览器，Pop 本身不会连接这些网站。</p>",
    "delete": "在 Pop 里清空剪贴板历史，删除文件夹 <code>~/Library/Application Support/Pop/</code>，再在“钥匙串访问”里删除名为“Pop”的项目。删除 Pop.app 和这些文件后，Pop 存储的一切就都清除了。",
}

MENO = {
    "version": "0.10",
    "meta_desc": "没有统计，没有账号，只为检查更新联网。",
    "summary": [
        "没有统计分析，没有账号，没有广告，也没有我的服务器。我什么都不收集。",
        "设置、规则和在本机计算的使用统计都留在你的 Mac 上。",
        "Meno 只在向 GitHub 查询最新版本、以及下载你选择安装的版本时联网。",
    ],
    "local_intro": "Meno 把数据存放在你 Mac 上的一个文件夹里：",
    "local": [
        ["设置、布局、规则、场景、分组", "<code>~/Library/Application Support/Meno/</code>", "可以导出到你选择的文件。导入文件时，包含 shell 命令的规则会被关闭。"],
        ["洞察（显示隐藏项目的频率、最常用的项目）", "<code>~/Library/Application Support/Meno/</code>", "只在你的 Mac 上计算和保存。"],
        ["零散的偏好（例如上次检查更新的时间）", "<code>UserDefaults</code>（<code>io.github.whrss9527.meno</code>）", ""],
        ["菜单栏项目的图像", "只在内存中", "允许屏幕录制后，Meno 会截取菜单栏项目的图像，用于在托盘里显示它们和察觉变化。屏幕上的其他内容一概不截取，也不保存任何图像。"],
    ],
    "net_intro": "Meno 只有一种网络连接：",
    "network": [
        GITHUB_UPDATE("点“检查更新”时；如果在设置 › 通用里开启了自动检查，每天一次；以及安装更新时。", "Meno/&lt;version&gt;"),
    ],
    "permissions": [
        ["辅助功能（必需）", "用来读取菜单栏项目，从托盘、快速打开和快捷键打开它们，以及用 ⌘ 拖移来排列它们。"],
        ["屏幕录制（可选）", "用来显示隐藏项目的真实图标，并察觉图标的变化（macOS 14–26）。只截取菜单栏项目。"],
    ],
    "extra": """<h2>会查看 Mac 状态的规则</h2>
        <p>和麦克风、摄像头有关的规则只向 macOS 查询设备是否正在使用，Meno 从不录音或录像。和网络有关的规则会运行系统的 <code>route</code> 和 <code>arp</code> 命令，根据 macOS 已知的信息识别你的路由器，不使用定位服务，也不发送任何数据。运行 shell 命令的规则只会运行你输入的那条命令，而且只在规则开启时运行。</p>""",
    "delete": "删除文件夹 <code>~/Library/Application Support/Meno/</code> 和 Meno.app，Meno 存储的一切就都清除了。",
}

STOX = {
    "version": "0.46",
    "meta_desc": "没有统计，没有账号；行情来自公开数据源，数据在你的 Mac 或你的 iCloud 里。",
    "summary": [
        "没有统计分析，没有账号，没有广告，也没有我的服务器。我什么都不收集。",
        "自选、持仓、交易记录和提醒都留在你的 Mac 上；开启同步后，也会存到你自己的 iCloud 云盘。",
        "为了显示价格，Stox 会向腾讯财经请求自选列表里那些代码的行情，新浪财经作为备用。你的持仓从不发送。",
        "Stox 会连接 GitHub 检查更新。",
    ],
    "local_intro": "Stox 把你的数据保存在你的 Mac 上：",
    "local": [
        ["自选、分组、备注、持仓、交易、分红、提醒和设置", "<code>UserDefaults</code>（<code>io.github.whrss9527.stox</code>）", "可以导出到你选择的备份文件。"],
        ["日志", "<code>~/Library/Application Support/Stox/stox.log</code> 和系统日志", "用于排查问题的技术信息，留在你的 Mac 上。"],
    ],
    "net_intro": "Stox 会连接下列地址：",
    "network": [
        ["腾讯财经（<code>qt.gtimg.cn</code>、<code>smartbox.gtimg.cn</code>、<code>web.ifzq.gtimg.cn</code>、<code>proxy.finance.qq.com</code>）", "Stox 运行期间：交易时段每隔几秒一次，休市时每分钟一次；Mac 睡眠时暂停。另外在你搜索、打开图表或排行榜时。", "需要行情或图表的股票代码，或你输入的搜索文字。不含持仓、金额或个人信息。"],
        ["新浪财经（<code>hq.sinajs.cn</code>、<code>stock2.finance.sina.com.cn</code>）", "腾讯行情连不上时自动作为备用；以及期货分时图。", "需要行情的股票代码。"],
        ["汇率（腾讯财经）", "持有多种货币的股票时。", "请求美元/人民币和港币/人民币汇率。"],
        GITHUB_UPDATE("启动时和之后每 6 小时，除非你在“关于与更新”里关闭了自动检查；以及安装更新时。", "Stox/&lt;version&gt; (macOS)"),
        ["雪球等财经网站", "只在你为某只股票选择“在雪球查看”（或类似链接）时。", "网页在你的默认浏览器里打开，Stox 本身不连接这个网站。"],
    ],
    "icloud": """<h2>iCloud</h2>
        <p>开启 iCloud 同步后，Stox 会把你的自选（包括分组、简称、持仓和提醒）和少量显示设置，连同你这台 Mac 的名称和修改时间，写入你自己 iCloud 云盘里的文件 <code>Stox/sync.json</code>，让你的其他 Mac 合并。只和某一台 Mac 有关的设置不同步。这个文件由苹果在你的 iCloud 账号下保存，我无法访问。关闭同步后就不再写入；你可以在访达里删除这个文件。</p>""",
    "permissions": [
        ["通知", "用于价格提醒、可选的收盘总结和更新提示。"],
        ["iCloud 云盘", "只在你开启同步时。"],
        ["辅助功能、屏幕录制", "不使用。Stox 的全局快捷键用的是标准热键接口，不需要任何权限。"],
    ],
    "extra": "<h2>行情数据</h2><p>行情由第三方提供，仅供参考。港股行情延时约 15 分钟。Stox 中的任何内容都不构成投资建议。</p>",
    "delete": "在设置里清空你的自选，或者删除 Stox，连同 <code>~/Library/Preferences/io.github.whrss9527.stox.plist</code> 和 <code>~/Library/Application Support/Stox/</code>。如果用过同步，再删除 iCloud 云盘里的 <code>Stox</code> 文件夹。",
}

PROXI = {
    "version": "0.13",
    "updated": ("October 1, 2026", "2026-10-01", "2026 年 10 月 1 日"),
    "meta_desc": "没有统计，没有账号；只修改你 Mac 上的代理设置，只在测试连接和检查更新时联网。",
    "summary": [
        "没有统计分析，没有账号，没有广告，也没有我的服务器。我什么都不收集。",
        "Proxi 不提供代理服务，也不转发任何流量。它只修改你 Mac 上的设置（系统代理、终端的环境变量、git 和 npm），让它们指向你选择的代理服务器。",
        "你的代理配置和设置留在你的 Mac 上；开启同步后，也会存到你自己的 iCloud 云盘。代理密码只存在这台 Mac 的钥匙串里，从不同步。",
        "Proxi 自身只在两种情况下联网：经你的代理测试连接（默认访问 apple.com），以及到 GitHub 检查更新。",
    ],
    "local_intro": "Proxi 把数据存放在你 Mac 上的这些位置：",
    "local": [
        ["代理配置（名称、颜色、类型、服务器地址、用户名、生效范围、例外列表）和设置", "<code>~/Library/Application Support/Proxi/config.json</code>", "密码不在这个文件里，只记着某个配置有密码。"],
        ["代理密码", "你的登录钥匙串（服务名为 <code>com.whrss9527.proxyswitch</code> 的通用密码）", "只存在这台 Mac 上，不进 iCloud 钥匙串。"],
        ["状态和日志", "<code>~/Library/Application Support/Proxi/</code>（<code>state.json</code>、<code>proxi.log</code>，以及 Proxi 运行时的套接字 <code>control.sock</code>）", "状态里记着上次用的配置，以及 Proxi 开启代理之前的代理设置，用来恢复。日志里的密码一律隐藏。"],
        ["少量偏好设置（界面语言、跳过的版本）", "<code>~/Library/Preferences/com.whrss9527.proxyswitch.plist</code>", ""],
        ["命令行工具（如果你安装了）", "<code>/usr/local/bin/proxi</code>（旧版本装过的还有 <code>/usr/local/bin/proxyswitch</code>）", "一个启动 Proxi 自身可执行文件的小脚本。"],
    ],
    "extra": """<h2>Proxi 会修改的设置</h2>
        <p>开启一套配置时，Proxi 把它的代理地址写进你为它选择的地方；关闭时再清掉（系统代理也可以选择恢复成开启前的设置）：</p>
        <ul>
          <li>各个网络服务的系统代理（通过 <code>networksetup</code>；需要登录时，macOS 会把密码保存在系统钥匙串里）；</li>
          <li>登录会话里的 <code>http_proxy</code>、<code>https_proxy</code>、<code>all_proxy</code>、<code>no_proxy</code> 环境变量（以及大写形式，通过 <code>launchctl setenv</code>），之后打开的程序和终端会读到它们；</li>
          <li><code>~/.gitconfig</code> 里 git 全局的 <code>http.proxy</code> 和 <code>https.proxy</code>；带密码的配置，地址放在只有你能读的 <code>~/Library/Application Support/Proxi/git-proxy.inc</code> 里，由 <code>~/.gitconfig</code> 引用；</li>
          <li><code>~/.npmrc</code> 里的 <code>proxy</code> 和 <code>https-proxy</code>，npm、pnpm 和 yarn 1 都读它。</li>
        </ul>
        <p>需要登录的配置，用户名和密码会按这些工具的要求写在地址里。使用这些设置的程序随后经你的代理服务器联网；Proxi 看不到这些流量。</p>
        <h2>本机控制</h2>
        <p>命令行工具、给 AI 助手用的 MCP 服务器和 <code>proxi://</code> 命令，都通过你 Mac 上一个只有你自己的账户能连的本地套接字（<code>control.sock</code>）工作，权限级别由你选择，也可以设为“关闭”。它们能查看状态和配置、开关代理、切换配置和测试连接，不能修改设置，也读不到密码。</p>""",
    "net_intro": "除了你自己的程序经你设置的代理发出的连接，Proxi 自身会连接下列地址：",
    "network": [
        ["测速地址（默认 <code>https://www.apple.com/library/test/success.html</code>，可以在设置 › 通用里修改）", "测试连接时，以及“自动检测”检查本机哪些端口能当代理用时。", "对这个页面的普通请求，经被测试的代理发出。"],
        ["你的代理服务器", "开启了“定期检查代理服务器能否连上”时，代理开着期间每 20 秒一次。", "向代理的地址和端口建立一次 TCP 连接后立即断开，不发送任何请求。"],
        ["PAC 配置的 PAC 地址", "这套配置开启或测试时；和任何 PAC 设置一样由 macOS 获取。", "请求你填写的地址上的 PAC 文件。"],
        GITHUB_UPDATE("启动时和之后每 6 小时，除非你关闭了自动检查；以及安装更新时。", "Proxi/&lt;version&gt; (macOS)"),
    ],
    "icloud": """<h2>iCloud</h2>
        <p>开启 iCloud 同步后，Proxi 会把你的代理配置以及“通用”和“快捷键”页里的设置，连同你这台 Mac 的名称和修改时间，写入你自己 iCloud 云盘里的文件 <code>Proxi/config.json</code>。密码不在其中：每台 Mac 的密码各自存在自己的钥匙串里，第一次用时请你输入一次。这个文件由苹果在你的 iCloud 账号下保存，我无法访问。</p>""",
    "permissions": [
        ["管理员密码", "用于安装命令行工具、macOS 要求时修改系统代理，以及移除以前版本安装的后台助手。"],
        ["钥匙串", "保存和读取需要登录的代理配置的密码。"],
        ["定位", "只用于按 Wi-Fi 网络自动切换：macOS 要求有这项权限才能读取 Wi-Fi 名称。Proxi 不读取也不保存你的位置。"],
        ["通知", "用于切换、连接问题和新版本提示。"],
        ["iCloud 云盘", "只在你开启同步时。"],
    ],
    "delete": "先关闭代理（这样上面那些设置会被清掉），退出 Proxi，再删除 Proxi.app、<code>~/Library/Application Support/Proxi/</code> 和 <code>~/Library/Preferences/com.whrss9527.proxyswitch.plist</code>。命令行工具请先在“自动化”页卸载（或删除 <code>/usr/local/bin/proxi</code>）。保存的密码可以在“钥匙串访问”里删除（搜索 <code>com.whrss9527.proxyswitch</code>）。如果用过同步，再删除 iCloud 云盘里的 <code>Proxi</code> 文件夹。",
}

ZH = {"pop": POP, "meno": MENO, "stox": STOX, "proxi": PROXI}
