"""Simplified Chinese app pages. Same structure, facts and screenshots as the
English data in apps.py; when one changes, change the other."""
from common import GH
from apps import shot, cut, stox_demo, STOX_HEAD, meno_demo, MENO_HEAD

# ---------------------------------------------------------------- Pop
POP = {
    "title": "Pop · 长按右键，一划即达",
    "desc": "Pop 是 Mac 菜单栏里的右键工具箱：长按鼠标右键，翻译选中的文字，或打开装着 80 多个工具的圆盘。开源免费。",
    "say": "/pɒp/ —— 像个气泡：弹出来，一划，啪一下就没了。",
    "lede": "在选中的任何内容上按住鼠标右键，Pop 就会翻译它、换算它，或者打开一个工具圆盘，一划就选好。轻点一下仍然是平常的右键菜单。",
    "meta": ["开源免费", "macOS 15 或更新", "Apple 芯片与 Intel", "简体中文界面"],
    "stage": lambda r: '<div class="compose">' +
        cut(r, "pop/ring.webp", "Pop 的圆盘菜单，格子里有翻译、搜索、词典、打开链接、全部功能、剪贴板、截图识字和屏幕取色，词典处于高亮", 214, 214, dark="pop/ring-dark.webp", eager=True) +
        cut(r, "pop/unit.webp", "Pop 的单位换算卡片，把 5 千米换算成厘米、米、英寸、英尺、英里、海里和市制单位", 325, 249, eager=True) +
        "</div>",
    "features": lambda r: [
        ("按住右键，停一下",
         "按住右键约四分之一秒（可以调整），Pop 就会读取你正在用的应用里选中的内容。提前松开，照常弹出系统菜单；按住右键拖动，拖动照样交给游戏或 3D 应用。",
         ["朝某个格子一划再松开就执行；在中间松开就关闭",
          "也可以用修饰键加右键、鼠标中键或全局快捷键唤出",
          "可选的选中文字工具条，默认关闭，可以按应用排除"],
         '<div class="illus-wrap">' + '''<div class="illus gesture" role="img" aria-label="示意图：按下鼠标右键之后会发生什么。0.25 秒内松开：平常的右键菜单。拖动超过 6 像素：拖动交给应用。按住 0.25 秒：Pop 读取选中的内容。">
  <div class="head"><span>按下右键</span><span>0.25 秒</span></div>
  <div class="step"><div class="bar"><i style="width:34%"></i><b></b></div><div><strong>提前松开</strong><span>平常的右键菜单</span></div></div>
  <div class="step"><div class="bar"><i style="width:48%"></i><b></b></div><div><strong>拖动 6 像素以上</strong><span>拖动交给应用，比如游戏、3D 工具</span></div></div>
  <div class="step sel"><div class="bar"><i style="width:100%"></i><b></b></div><div><strong>按住</strong><span>Pop 读取选中的内容：给出译文、结果或圆盘</span></div></div>
</div>''' + '<p class="illus-cap">Pop 如何区分长按和普通点击。延迟可以调整。</p></div>'),
        ("选中就翻译",
         "外文直接出翻译卡片。默认用苹果的系统翻译，离线又免费。也可以换成 AI 或 DeepL，或者并排对照。",
         ["直接替换原文，或者复制译文",
          "单张卡片临时换目标语言，或者朗读出来",
          "把单词存进生词本，还能导出到 Anki"],
         cut(r, "pop/translate.webp", "Pop 的翻译卡片，对照显示一句英文的 AI 译文和 DeepL 译文，带复制和替换按钮", 325, 297)),
        ("80 多个工具，放在你想要的位置",
         "摆放 4 到 12 个格子，给某个应用单独配一个圆盘，还能设置跳过圆盘的直达规则：算式直接算出结果，单位和颜色直接换算，图片用本机 OCR 识别文字。",
         ["文本：清理格式、大小写、编码、字数统计、提取链接和邮箱",
          "开发：JSON、YAML、SQL、正则、JWT、哈希、二维码、cron",
          "文件和屏幕：重命名、图片和视频转换、PDF、取色器、标尺"],
         '<div class="overlap">' + cut(r, "pop/json.webp", "Pop 的 JSON 转代码卡片，正在生成 TypeScript 接口", 442, 363) + cut(r, "pop/regex.webp", "Pop 的正则测试卡片，高亮匹配到的日期和命名分组", 442, 274) + "</div>"),
        ("剪贴板历史，还能置顶贴图",
         "Pop 会保存可搜索的文字、图片和文件历史；图片里的文字也能搜，识别在你的 Mac 上完成。截图、图片或文字可以贴在所有窗口之上，方便对照。",
         ["⌘1–⌘9 直接粘贴，按住 ⌘ 点选多条一起粘贴",
          "跳过密码管理器标记为隐藏的内容；任何应用都可以排除",
          "只存在这台 Mac 上，按时间和条数自动清理"],
         cut(r, "pop/history.webp", "Pop 的剪贴板历史面板，带搜索、类型筛选和五条最近记录，其中两条已选中", 392, 414)),
        ("AI，用你自己的接口",
         "选中文字，让 AI 润色、总结、解释或翻译，也可以直接提问。在开启了 Apple 智能的 macOS 26 上，Pop 可以用系统自带的本机模型；也可以接入任何兼容 OpenAI Chat Completions 的接口，包括在你 Mac 上运行的模型。",
         ["回答流式输出；可以复制、替换原文或贴在屏幕上",
          "只有使用 AI 功能时才会发送选中的文字",
          "API 密钥保存在这台 Mac 的钥匙串里"],
         cut(r, "pop/ai.webp", "Pop 的 AI 卡片，带润色、总结、解释和翻译按钮，以及提问输入框", 358, 210)),
        ("插件就是一个 JSON 文件",
         "把网址模板、shell 脚本、JavaScript 或快捷指令变成圆盘上的工具。也可以从插件库安装：Pop 添加前会校验 SHA-256，安装 shell 脚本前会先给你看内容。",
         ["<code>pop://</code> 链接和快捷指令操作，让其他工具也能调用 Pop",
          "导入、导出插件，或者直接分享 JSON 文件"],
         shot(r, "pop/library.jpg", "Pop 设置里的插件库，列出可安装的插件", 640, 481, "light")),
    ],
    "more_title": "还有这些",
    "tiles": [
        ("截图识字和翻译", "在屏幕上框选一块区域，识别或翻译里面的文字，离线完成。"),
        ("截图标注", "箭头、方框、文字、马赛克和序号，还可以加背景和阴影。"),
        ("取色器和标尺", "拾取屏幕上任意位置的颜色，测量元素之间的距离。"),
        ("传到手机", "手机连同一个 Wi-Fi，打开一个临时网页，就能双向传文件。"),
        ("窗口布局", "左右半屏、三分屏、最大化、居中，或移到另一块显示器。"),
        ("保持唤醒和计时器", "让 Mac 一段时间内不睡眠，或者快速设个倒计时。"),
    ],
    "specs": [
        ("macOS", "15 Sequoia 或更新；macOS 26 上为 Liquid Glass"),
        ("Mac", "通用：Apple 芯片与 Intel"),
        ("权限", "辅助功能（必需）。屏幕录制只用于截图类工具。"),
        ("语言", "简体中文界面；翻译支持多种语言"),
        ("下载", "约 6 MB（<code>Pop-&lt;version&gt;.zip</code>）"),
        ("许可证", "GPL-3.0"),
    ],
    "install": [
        "从最新版本下载 <code>Pop-&lt;version&gt;.zip</code> 并解压。",
        "把 <strong>Pop.app</strong> 拖进“应用程序”文件夹，双击打开。从 0.22.0 起，发布的版本都用 Developer ID 签名并通过苹果公证。",
        "在系统设置 › 隐私与安全性 › 辅助功能里打开 Pop，几秒内生效。",
        "选中一段英文，按住鼠标右键约 0.25 秒。",
    ],
    "update_note": "Pop 在启动时和之后每 6 小时检查一次 GitHub Releases（可以关闭，也可以不接收测试版）。点“立即更新”会下载新版本，校验 SHA-256 校验和与代码签名（必须由同一个证书签名），然后替换 Pop 并重新打开。设置、插件和历史记录都会保留。",
    "faq": [
        ("免费吗？", "免费。Pop 以 GPL-3.0 开源，不用注册账号，没有订阅，也没有应用内购买。"),
        ("为什么需要辅助功能权限？", [
            "macOS 只允许有辅助功能权限的应用在全局监听鼠标按键、读取其他应用里选中的内容并粘贴进去。Pop 需要的正是这些：察觉长按右键，读取你选中的内容，以及在你选择“替换原文”时把结果放回去。",
            "也正因为这样，Pop 无法上架 Mac App Store（沙盒不允许这么做），所以通过 GitHub 和本网站发布。"]),
        ("需要屏幕录制权限吗？", "只有要看屏幕的工具需要：截图识字和翻译、扫描二维码、截图标注和标尺。其他功能都不需要。"),
        ("有英文界面吗？", "暂时没有，Pop 的界面是简体中文。翻译本身支持多种语言，可以用苹果的系统翻译、AI 或 DeepL。"),
        ("Pop 会把我的文字发到别处吗？", '只在你要求时：AI 功能会把选中的文字发到你设置的 AI 接口，DeepL 翻译会把它发给 DeepL。苹果的系统翻译和本机模型、文字识别以及剪贴板历史都留在你的 Mac 上。详见<a href="../privacy/pop/">隐私政策</a>。'),
        ("能在多台 Mac 之间同步吗？", "可以在设置 › 同步里把设置和插件导出为文件，再到另一台 Mac 上导入。iCloud 同步需要带 iCloud 权限签名的版本，GitHub 上的版本不包含这项功能。"),
        ("更新后右键不管用了。", "打开 Pop 的设置 › 通用，点“清除旧的授权记录”，再重新授予辅助功能权限。这种情况主要出现在以前本地签名（ad-hoc）的版本上；经过公证的版本更新后会保留权限。"),
    ],
}

# ---------------------------------------------------------------- Meno
MENO_BAR = """<div class="illus screen" role="img" aria-label="示意图：Meno 在它的尖括号分隔符右边只留三个图标，菜单栏下方挂着一条玻璃托盘，显示被隐藏的项目">
  <div class="mb">
    <span class="menus"><b>访达</b><span>文件</span><span>编辑</span><span>显示</span><span>前往</span><span>窗口</span><span>帮助</span></span>
    <span class="right">
      <span class="div">‹</span>
      <span class="dot"></span><span class="dot c"></span><span class="dot"></span>
      <span class="time">周三 9:41</span>
    </span>
  </div>
  <div class="shelf" aria-hidden="true"><span class="dot"></span><span class="dot c"></span><span class="dot"></span><span class="dot c"></span><span class="dot"></span><span class="dot"></span><span class="dot c"></span></div>
  <div class="legend"><span>‹ Meno 的分隔符：它左边的图标都会隐藏</span><span>托盘在菜单栏正下方显示隐藏的项目</span></div>
</div>"""

MENO_REVEAL = """<div class="illus" role="img" aria-label="示意图：同一条菜单栏的两种状态。先是只有尖括号分隔符和三个可见图标；展开后，隐藏的图标出现在两个分隔符之间，暗格里的图标仍然不出现在菜单栏上。">
  <p class="tag">隐藏时</p>
  <div class="mb">
    <span class="menus"><b>邮件</b><span>文件</span><span>编辑</span></span>
    <span class="right"><span class="div">‹</span><span class="dot"></span><span class="dot c"></span><span class="dot"></span><span class="time">9:41</span></span>
  </div>
  <p class="tag" style="margin-top:16px">展开后</p>
  <div class="mb">
    <span class="menus"><b>邮件</b></span>
    <span class="right"><span class="div">»</span><span class="dot new"></span><span class="dot new c"></span><span class="dot new"></span><span class="dot new c"></span><span class="div">‹</span><span class="dot"></span><span class="dot c"></span><span class="dot"></span><span class="time">9:41</span></span>
  </div>
  <div class="legend"><span>» 暗格：不出现在菜单栏里</span><span>‹ 隐藏：需要时才显示</span><span>常显：一直都在</span></div>
</div>"""

MENO_QUICK = """<div class="illus" role="img" aria-label="示意图：快速打开，一个搜索面板，列出与输入文字匹配的菜单栏项目和操作">
  <div class="palette">
    <div class="q">wi<span class="caret"></span></div>
    <div class="row sel"><span class="dot"></span><span>Wi-Fi</span><small>↩ 打开</small></div>
    <div class="row"><span class="dot c"></span><span>无线诊断</span><small>⌘2</small></div>
    <div class="row"><span class="dot"></span><span>场景：工作</span><small>⌘3</small></div>
  </div>
</div>"""

MENO_RULE = """<div class="illus" role="img" aria-label="示意图：两条规则。麦克风正在使用时，打开禅模式，结束后还原。连接外接显示器时，应用场景“工作”。">
  <div class="palette">
    <div class="row"><span class="dot c"></span><span><strong>当</strong>麦克风正在使用</span></div>
    <div class="row sel"><span class="dot"></span><span>打开禅模式</span><small>结束后还原</small><span class="sw" aria-hidden="true"></span></div>
    <div class="sep"></div>
    <div class="row"><span class="dot c"></span><span><strong>当</strong>连接了外接显示器</span></div>
    <div class="row sel"><span class="dot"></span><span>应用场景“工作”</span><span class="sw" aria-hidden="true"></span></div>
  </div>
</div>"""

MENO_LANG = """<div class="illus" role="img" aria-label="示意图：Meno 通用设置里的语言选项：跟随系统、English、简体中文和繁體中文">
  <div class="palette">
    <div class="row sel"><span class="dot c"></span><span>跟随系统</span><small>✓</small></div>
    <div class="row"><span class="dot"></span><span>English</span></div>
    <div class="row"><span class="dot"></span><span>简体中文</span></div>
    <div class="row"><span class="dot"></span><span>繁體中文</span></div>
  </div>
</div>"""

MENO = {
    "title": "Meno · 安静的菜单栏，由玻璃打造",
    "desc": "Meno 是 macOS 菜单栏管理工具：隐藏图标、收进暗格，点击、悬停、轻扫或快捷键随时唤回；还有 Liquid Glass 托盘、快速打开、规则、场景和禅模式。",
    "say": "/ˈmeː.no/ —— 意大利语里的“更少”，和 menu 只差一个字母。",
    "lede": "Meno 把不常用的菜单栏图标收起来，点一下、悬停、轻扫或按快捷键，就能随时唤回。",
    "meta": ["开源免费", "macOS 14 或更新", "Apple 芯片与 Intel", "English、简体中文、繁體中文"],
    "extra_head": MENO_HEAD,
    "stage": lambda r: f'<div style="max-width:880px;margin:0 auto">{meno_demo(r, "zh", "layout", MENO_BAR)}</div>',
    "features": lambda r: [
        ("常显、隐藏，还有暗格",
         "Meno 在菜单栏里加几个小分隔符。单尖括号左边的图标会隐藏，需要时才出现；越过双尖括号的图标收进暗格，留给几乎用不到的东西：它们只在托盘、快速打开里，或按住 ⌥ 点击时出现。",
         ["点 Meno、点击或悬停在菜单栏空白处、向下滚动或轻扫，或按快捷键，都能展开",
          "延迟一段时间、切换应用或指针离开后，自动重新隐藏",
          "应用重启后 macOS 挪了它的图标，Meno 会放回原处"],
         meno_demo(r, "zh", "reveal", MENO_REVEAL)),
        ("托盘和快速打开",
         "托盘是菜单栏下方的一条玻璃栏，显示隐藏的项目；在摄像头所在的刘海旁、菜单栏放不下时尤其好用。快速打开是类似聚焦搜索的面板，用键盘就能找到任何项目，支持拼音和首字母。",
         ["↩ 打开，⌘↩ 打开次级菜单，⌘1–⌘9 选择结果",
          "也能执行 Meno 自己的操作：应用场景、打开禅模式",
          "macOS 26 上是 Liquid Glass；macOS 14 和 15 上是磨砂玻璃"],
         meno_demo(r, "zh", "shelf", MENO_QUICK)),
        ("会看场合的菜单栏",
         "规则会替你调整菜单栏：麦克风或摄像头正在使用、接上显示器、使用电池、连到某个网络，或者到了某个时间。场景可以把布局保存成“工作”“在家”“演示”等。",
         ["操作可以显示或隐藏分区、应用场景、打开禅模式，或移动某个项目",
          "移动会等到你不再使用鼠标和键盘时才进行",
          "从 Meno 的菜单或用快捷键暂停所有规则"],
         meno_demo(r, "zh", "rules", MENO_RULE)),
        ("用你的语言",
         "Meno 支持英语、简体中文和繁体中文。它跟随系统语言，也可以在设置 › 通用 › 语言里另选一种，重新打开后切换。",
         ["这个设置用三种语言标注，哪种界面下都好找",
          "通用里的其他设置：项目怎样出现、何时重新隐藏、暗格和禅模式"],
         meno_demo(r, "zh", "general", MENO_LANG)),
    ],
    "more_title": "积少成多的小细节",
    "tiles": [
        ("禅模式", "一个快捷键清空所有应用图标，只留系统状态，适合截图、录屏和演讲。"),
        ("布局编辑器", "在常显、隐藏和暗格之间拖动项目，还能重命名，配上符号。"),
        ("分组", "把相关的项目收到一个图标后面；点它，就在正下方的托盘里显示出来。"),
        ("变化时显示", "隐藏项目的图标或文字有变化时（比如同步失败），它会短暂出现一下。"),
        ("项目快捷键和链接", "在任何地方打开 Wi-Fi、VPN 或计时器。<code>meno://</code> 链接可以在快捷指令和脚本里使用。"),
        ("洞察，只在本机", "你多久展开一次、最常用哪些项目，以及该保留还是收进暗格的建议；数据从不离开你的 Mac。"),
    ],
    "specs": [
        ("macOS", "14 Sonoma 或更新；macOS 26 上为 Liquid Glass"),
        ("Mac", "通用：Apple 芯片与 Intel"),
        ("权限", "辅助功能（必需）。屏幕录制可选，用来显示隐藏项目的真实图标。"),
        ("语言", "英文、简体中文、繁体中文"),
        ("下载", "约 5 MB（<code>Meno.zip</code>）"),
        ("许可证", "GPL-3.0"),
    ],
    "install": [
        "从最新版本下载 <code>Meno.zip</code> 并解压。",
        "把 <strong>Meno.app</strong> 移到“应用程序”文件夹，双击打开。从 0.10.0 起，发布的版本都用 Developer ID 签名并通过苹果公证。",
        "按提示授予辅助功能权限，然后按住 ⌘ 把图标拖过分隔符，或者使用布局编辑器。",
    ],
    "update_note": "在设置 › 关于里检查更新，或者在通用里打开每日自动检查。“安装并重新打开”会从 GitHub 下载新版本，校验校验和、版本号和代码签名，替换 Meno 后重新打开。",
    "faq": [
        ("免费吗？", "免费。Meno 以 GPL-3.0 开源，不用注册账号，也没有任何需要购买的东西。"),
        ("为什么需要辅助功能权限？", "Meno 通过各个应用的辅助功能接口读取菜单栏项目，从托盘、快速打开和快捷键打开它们，并替你执行 ⌘ 拖移来排列它们。这三件事，macOS 都只允许有辅助功能权限的应用去做。"),
        ("屏幕录制是做什么用的？", "这项权限是可选的。有了它，托盘会显示隐藏项目的真实图标，Meno 也能察觉它们的图标变化（macOS 14–26）。只截取菜单栏项目，不录制也不保存任何东西。没有这项权限时，Meno 显示应用图标。"),
        ("Meno 会联网吗？", '只在向 GitHub 查询最新版本时（你手动检查时，或开启后每天一次），以及下载你选择安装的版本时。没有统计，没有账号。详见<a href="../privacy/meno/">隐私政策</a>。'),
        ("在 macOS 26 上少了一个图标。", "macOS 只显示在系统设置 › 菜单栏里允许显示的应用项目。Meno 自己的图标也可以在设置 › 外观里关掉；要再打开设置，可以用快速打开，或者再次打开 Meno。"),
        ("更新后 Meno 没反应。", "打开设置 › 权限，点“清除并重新授权”。0.10.0 及以后的版本使用同一个 Developer ID 证书，之后更新都会保留权限。"),
        ("支持 macOS 27 吗？", "支持。macOS 27 改变了菜单栏处理宽项目的方式，所以 Meno 在上面使用“阶梯式”隐藏引擎；你可以在设置 › 通用 › 高级里选择引擎。"),
    ],
}

# ---------------------------------------------------------------- Stox
STOX = {
    "title": "Stox · 菜单栏里的 A 股、港股、美股行情",
    "desc": "Stox 在 Mac 菜单栏里显示 A 股、港股和美股行情，还有图表、持仓盈亏、提醒和 iCloud 同步。右键一点，全部隐藏。开源免费。",
    "say": "/stɒks/ —— 就是 stocks，挤成了四个字母。",
    "lede": "A 股、港股、美股行情就在菜单栏里，还有持仓盈亏、提醒和 iCloud 同步。右键点一下，只剩一个安静的图标。",
    "meta": ["开源免费", "macOS 13 或更新", "Apple 芯片与 Intel", "简体中文和英文界面"],
    "extra_head": STOX_HEAD,
    "stage": lambda r: '<div class="compose stox-stage">' +
        stox_demo(r, "zh", "detail", "stox/detail.webp", "Stox 面板：自选列表和贵州茅台展开的分时图", 376, 645, desk=True) +
        cut(r, "stox/detail.webp", "Stox 面板的真实截图：自选列表和贵州茅台展开的分时图", 376, 645, width=300, cap="真实截图") +
        "</div>",
    "features": lambda r: [
        ("看一眼，就藏起来",
         "左键点菜单栏图标，打开玻璃面板；再点一下、点别处或按 Esc 关闭。右键在显示行情和只显示图标之间切换，身后有人的时候正好用得上。",
         ["把选中的股票固定在菜单栏上，单行或双行显示，刘海屏上轮播",
          "⌃⌥S 在任何应用里打开面板；也可以固定成浮动窗口",
          "红涨绿跌、绿涨红跌，或者干脆不用红绿"],
         stox_demo(r, "zh", "list", "stox/panel.webp", "Stox 自选列表，每一行都有迷你分时图", 376, 583, desk=True)),
        ("三个市场，还不止",
         "沪深北 A 股、港股、美股（含盘前盘后价格），另外还有指数、ETF、场外基金、国际期货和外汇。",
         ["按代码、中文名或拼音首字母搜索：<code>600519</code>、<code>gzmt</code>、<code>aapl</code>",
          "一次粘贴多个代码，一起添加",
          "主数据源出问题时，自动切换到备用数据源"],
         stox_demo(r, "zh", "search", "stox/search.webp", "Stox 搜索结果，边输入边显示价格和涨跌", 376, 467)),
        ("图表，一看就懂",
         "展开一行，查看分时、五日、日 K、周 K 和月 K，带均线和成交量。鼠标悬停，就能看到任意一分钟的准确价格。A 股还有盘口和资金流向。",
         ["图上画出你的成本线，记录过的交易标上 B 和 S",
          "开盘、最高、最低、成交额、市盈率、市值、52 周区间",
          "A 股涨幅榜、跌幅榜和行业排行"],
         stox_demo(r, "zh", "kline", "stox/kline.webp", "Stox 的日 K 线图，带均线和成交量", 376, 645)),
        ("持仓与盈亏",
         "填入股数和成本，Stox 会按币种算出当日盈亏和总盈亏，持有多种货币时折算成人民币。可以记录交易和分红；日历里能看到每一天的结果。",
         ["买入时自动更新加权平均成本，卖出时记录已实现收益",
          "点一下眼睛图标，面板、菜单栏和通知里的金额都会隐藏",
          "可选的收盘总结通知"],
         stox_demo(r, "zh", "holdings", "stox/holdings.webp", "Stox 的持仓页面，按币种汇总并显示盈亏", 376, 647)),
    ],
    "more_title": "还有这些",
    "tiles": [
        ("提醒", "价格高于或低于、涨跌幅、止盈止损、涨停跌停、52 周新高新低。"),
        ("iCloud 同步", "自选、分组、持仓和提醒通过你自己的 iCloud 云盘同步。也可以导出备份文件。"),
        ("用电池时也安静", "休市时每分钟刷新一次，Mac 睡眠时停止刷新。"),
        ("分组和备注", "给自选分组，再用一句话记下你关注某只股票的理由。"),
        ("复制到表格", "把持仓、交易和盈亏复制成表格，贴进 Numbers 或 Excel。"),
        ("轻巧", "内存占用约 30 MB。不用注册，也不用 API 密钥。"),
    ],
    "specs": [
        ("macOS", "13 Ventura 或更新；macOS 26 上为 Liquid Glass"),
        ("Mac", "通用：Apple 芯片与 Intel"),
        ("权限", "无需特殊权限。提醒需要通知权限；只有开启同步时才需要访问 iCloud 云盘。"),
        ("语言", "简体中文或英文，跟随 Mac 的系统语言（0.47.0 起）"),
        ("数据", "腾讯财经公开行情，新浪财经作为备用。港股行情延时约 15 分钟。"),
        ("下载", "约 4 MB（<code>Stox.zip</code>）"),
        ("许可证", "GPL-3.0"),
    ],
    "install": [
        "从最新版本下载 <code>Stox.zip</code> 并解压。",
        "把 <strong>Stox.app</strong> 拖进“应用程序”文件夹，双击打开。从 0.46.0 起，发布的版本都用 Developer ID 签名并通过苹果公证。",
        "Stox 只出现在菜单栏里：左键打开面板，右键隐藏行情。设置和退出在面板底部。",
    ],
    "update_note": "Stox 在启动时和之后每 6 小时检查一次 GitHub Releases（可以在“关于与更新”里关闭）。有新版本时，面板底部会出现“更新”按钮；Stox 会校验 SHA-256 校验和与签名，替换自己并重新打开，自选和设置都会保留。",
    "faq": [
        ("免费吗？", "免费。Stox 以 GPL-3.0 开源。行情来自免费的公开数据源，所以不用注册，也不用 API 密钥。Mac App Store 版正在准备中；GitHub 上的版本会一直免费。"),
        ("需要辅助功能权限吗？", "不需要。Stox 不申请辅助功能或屏幕录制权限。它的全局快捷键用的是标准热键接口，不需要任何权限。它只会申请发送通知（用于提醒），以及在你开启同步时使用 iCloud 云盘。"),
        ("行情从哪里来？", "来自腾讯财经的公开行情服务，新浪财经作为自动备用。港股行情延时约 15 分钟。数据仅供参考，不构成投资建议。"),
        ("我的持仓存在哪里？", '存在你的 Mac 上；开启同步后，也存在你自己的 iCloud 云盘里（<code>Stox/sync.json</code>）。不会发给我。详见<a href="../privacy/stox/">隐私政策</a>。'),
        ("能用英文界面吗？", "能。从 0.47.0 起，Mac 的系统语言不是中文时，Stox 的界面就是英文。A 股、港股的名称仍是中文，和行情源给的一样。"),
    ],
}

# ---------------------------------------------------------------- Proxi
PROXI_SCOPE = """<div class="illus" role="img" aria-label="示意图：一个代理配置同时在四处生效：系统代理、环境变量、git 和 npm">
  <div class="palette">
    <div class="q">公司代理 · 127.0.0.1:7890</div>
    <div class="row"><span>系统代理</span><small>networksetup</small><span class="sw" aria-hidden="true"></span></div>
    <div class="row"><span>环境变量</span><small>launchctl setenv</small><span class="sw" aria-hidden="true"></span></div>
    <div class="row"><span>git</span><small>http.proxy</small><span class="sw" aria-hidden="true"></span></div>
    <div class="row"><span>npm</span><small>proxy</small><span class="sw" aria-hidden="true"></span></div>
  </div>
</div>"""

PROXI = {
    "title": "Proxi · 一个开关，管好 Mac 上所有代理",
    "desc": "Proxi 同时切换系统代理、环境变量、git 和 npm，内置 mihomo 内核，支持订阅、分流规则、局域网共享和增强模式（TUN）。macOS 上开源免费。",
    "say": "/ˈprɒk.si/ —— 还是 proxy，只是 y 换成了 i。",
    "lede": "一个开关管好系统代理、终端环境变量、git 和 npm；还内置 mihomo 内核，支持订阅和分流规则、局域网共享，以及增强模式（TUN）和网关模式。",
    "meta": ["开源免费", "macOS 14 或更新", "Apple 芯片与 Intel", "简体中文界面"],
    "stage": lambda r: shot(r, "proxi/hero.jpg", "Proxi 设置窗口里的代理配置列表，旁边是列出节点和延迟的菜单栏面板，以及菜单栏上的网速显示", 1600, 1000, "light"),
    "features": lambda r: [
        ("一个开关，处处生效",
         "建一个代理配置（HTTP、SOCKS5 或 PAC），选好它作用在哪里：系统代理、新开的终端和应用的环境变量、git 和 npm。一键切换配置，或者按 ⌃⌥P。",
         ["发现其他应用改了代理时会提示你，还能把它存成一个配置",
          "自动发现你 Mac 上已经在运行的代理软件并添加进来",
          "菜单栏里直接显示上传和下载速度"],
         PROXI_SCOPE),
        ("订阅和规则，内置就有",
         "粘贴订阅地址，节点就出现在面板里。手动选一个，或者让 Proxi 自动选最快的，再按规则分流。引擎是 mihomo（Clash Meta），打包在应用里。",
         ["策略组：手动选择、自动选择、故障转移和负载均衡",
          "规则库收录 blackmatrix7、MetaCubeX、ACL4SSR 和 Shadowrocket 规则集",
          "导入 Clash、mihomo、Surge、Shadowrocket 和 Quantumult X 配置，可以预览和撤销"],
         shot(r, "proxi/nodes.jpg", "Proxi 的节点与订阅页面，有两个订阅和节点设置", 820, 770, "light")),
        ("整台 Mac，连游戏机也算上",
         "增强模式通过虚拟网卡，让每个应用（包括终端和游戏）都经过内核。局域网共享和网关模式让 PS5、Switch 或手机和你的 Mac 用同一个连接。",
         ["局域网共享使用 7892 端口，默认只允许局域网地址连接",
          "网关模式适合不能设置代理的设备，游戏的 UDP 流量也能处理",
          "一个小小的特权助手，输一次密码安装，只在这两种模式下使用"],
         shot(r, "proxi/lan.jpg", "Proxi 的局域网共享页面，显示要在 PS5 或 Switch 上填写的地址", 820, 770, "light")),
        ("脚本、AI 助手和同步",
         "<code>proxi</code> 命令行工具、给 AI 助手用的 MCP 服务器和 <code>proxi://</code> 网址命令，共用一个本地控制接口，有四档权限。设置可以通过你自己的 iCloud 云盘在多台 Mac 之间同步。",
         ["按 Wi-Fi 网络或路由器自动切换配置",
          "导入和自动切换都记在操作记录里；导入可以撤销"],
         shot(r, "proxi/icloud.jpg", "Proxi 的 iCloud 同步页面", 820, 770, "light")),
    ],
    "more_title": "连不上的时候",
    "tiles": [
        ("连接", "经过内核的每一条连接：来自哪个应用或设备、命中哪条规则、走哪个节点、用了多少流量。"),
        ("服务检测", "看看 ChatGPT、Claude、Gemini、Netflix、YouTube Premium 或 Telegram 通过某个节点能不能用，被识别为哪个地区。"),
        ("网址诊断", "输入打不开的网站，Proxi 会逐一检查 DNS、直连和代理路径，并给出修复建议。"),
        ("出口 IP", "网站通过你的节点看到的地址和地区，以及你 Mac 自己的公网地址。"),
        ("进阶 DNS", "内核自带加密 DNS、按域名指定服务器、hosts，以及保存前会先检查的 mihomo 配置补丁。"),
        ("健康检查", "代理开启时定期检查代理端口，没有响应时提醒你。"),
    ],
    "specs": [
        ("macOS", "14 Sonoma 或更新；macOS 26 上为 Liquid Glass"),
        ("Mac", "通用：Apple 芯片与 Intel（也提供单一架构版本）"),
        ("权限", "修改系统代理需要管理员密码。特权助手只用于增强模式和网关模式。不需要辅助功能权限。"),
        ("语言", "简体中文界面"),
        ("下载", "通用版约 53 MB（<code>Proxi-macos.zip</code>），<code>-arm64</code> 或 <code>-x86_64</code> 版约为一半"),
        ("许可证", "GPL-3.0；内置 mihomo（GPL-3.0）"),
    ],
    "install": [
        "从最新版本下载 <code>Proxi-macos.zip</code> 并解压。",
        "把 <strong>Proxi.app</strong> 拖进“应用程序”文件夹，双击打开。从 0.11.1 起，发布的版本都用 Developer ID 签名并通过苹果公证。",
        "点菜单栏图标，添加一个代理配置或订阅，打开开关。",
    ],
    "update_note": "Proxi 在启动时和之后每 6 小时检查一次 GitHub Releases（可以关闭）。点“更新”会下载适合你芯片的版本，比对 SHA-256，替换 Proxi 并重新打开。签名版本只会安装同一开发者签名的更新。Proxi 以前叫 ProxySwitch；从 ProxySwitch 更新时，设置会自动迁移过来。",
    "faq": [
        ("免费吗？", "免费。Proxi 以 GPL-3.0 开源。它不出售也不提供代理服务器，代理或订阅需要你自己准备。"),
        ("需要辅助功能权限吗？", "不需要。全局快捷键用的是标准热键接口。Proxi 真正需要的是：修改系统代理时的管理员密码；以及只有使用增强模式或网关模式时，要安装一次特权助手，因为虚拟网卡和 IP 转发需要 root 权限。"),
        ("mihomo 是什么？", "mihomo（Clash Meta）是一个开源代理内核，同样采用 GPL-3.0。Proxi 把它作为独立程序打包在应用里，只在你使用内置节点代理、局域网共享或增强模式时运行。"),
        ("局域网共享安全吗？", "默认只允许私有局域网网段（10.x、172.16–31.x、192.168.x）的设备连接，你也可以限定为指定的 IP。在公共 Wi-Fi 上请关闭它。"),
        ("为什么要定位权限？", "只用于按 Wi-Fi 网络自动切换：从 macOS 14 起，读取 Wi-Fi 名称需要定位权限。Proxi 不读取也不保存你的位置，你也可以改为按路由器切换。"),
        ("有 Windows 版吗？", f'有，Windows 上是 <a href="{GH}/proxyswitch">ProxySwitch</a>。两者各自独立发展。'),
    ],
}

ZH = {"pop": POP, "meno": MENO, "stox": STOX, "proxi": PROXI}
