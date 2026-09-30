/* whrss.com: an interactive recreation of Meno in a Mac menu bar.
   The menu bar items are made-up samples with neutral icons; nothing is fetched.
   Layout, sizes and wording follow the Meno sources (StatusBarController, MenoIconRenderer,
   ShelfView, QuickOpenView, StatusMenuBuilder, SettingsRootView, GeneralPane, LayoutPane,
   RulesPane, Glass) and its en / zh-Hans / zh-Hant Localizable.strings. The block between
   the APP-STRINGS markers holds the app's own translations of every string used here.

   Markup: <figure class="mnd" data-lang="en|zh" data-preset="layout|reveal|shelf|rules|general"
            data-icon="…/meno.png">…fallback…</figure> */
(function () {
  "use strict";

  // ------------------------------------------------------------------ strings
  // Meno's own strings, keyed by the English source string, as in the app.
  var APP = /*APP-STRINGS*/{"zh-Hans":{" and ":"且","%lld items · %lld tucked away":"共 %lld 项 · %lld 项已收起","A Focus can change the menu bar too: in Shortcuts, add an automation for when the Focus turns on or off that opens a scene's link, such as meno://scene/Work.":"专注模式也能改变菜单栏：在快捷指令里为专注模式打开或关闭时添加一个自动化，打开某个场景的链接，例如 meno://scene/Work。","A calm menu bar, made with glass.":"一个安静的菜单栏，由玻璃打造。","A microphone is in use":"麦克风正在使用","A second hidden section for items you rarely need. They never appear in the menu bar, only in the Shelf, Quick Open or with ⌥-click.":"为很少用到的项目准备的第二个隐藏分区。它们从不出现在菜单栏中，只能通过托盘、快速打开或按住 ⌥ 点按来访问。","About":"关于","About Meno":"关于 Meno","Action":"操作","Actions":"更多操作","Active":"生效中","After":"延迟","Also hide the items in the Visible section":"同时隐藏“常显”分区中的项目","Always":"始终","Always shown in the menu bar.":"始终显示在菜单栏中。","An external display is connected":"连接了外接显示器","Appearance":"外观","Apply Scene “%@”":"应用场景“%@”","Apply a scene at the desk":"在办公桌前应用场景","Arrange Menu Bar":"整理菜单栏","Arrange Menu Bar…":"整理菜单栏…","Ask me":"询问我","Automatically":"自动","Check for Updates…":"检查更新…","Check for updates once a day":"每天检查一次更新","Choose which items stay in the menu bar and which ones Meno tucks away.":"选择哪些项目留在菜单栏里，哪些交给 Meno 收起来。","Clear the app menus":"清空 App 菜单","Click an empty part of the menu bar":"点按菜单栏的空白处","Click an item to choose where it goes: another section, or one step to the left or right.":"点一下项目，选择把它放到哪里：别的分区，或者往左、往右挪一格。","Clicking again hides the items.":"再次点按会重新隐藏。","Close":"关闭","Delete":"删除","Drag a file onto the menu bar":"把文件拖到菜单栏上","Drop items here":"拖到这里","Duplicate…":"创建副本…","Edit…":"编辑…","Finder":"访达","Follow System":"跟随系统","General":"通用","Good to know":"小贴士","Hidden":"隐藏","Hidden items appear in the menu bar, so the file can be dropped on one of them. Items in the Shelf cannot take drops.":"隐藏的项目会显示在菜单栏中，方便把文件放到其中一个项目上。托盘中的项目无法接收拖放。","Hidden section divider":"隐藏分区分隔符","Hide Items":"隐藏项目","Hide automatically":"自动隐藏","Hide it":"隐藏它","Hiding again":"重新隐藏","Hotkeys":"快捷键","Hover over an empty part of the menu bar":"指针悬停在菜单栏空白处","How hidden items appear and disappear.":"隐藏项目如何出现和消失。","How you use the menu bar, measured on this Mac only.":"你如何使用菜单栏，仅在这台 Mac 上统计。","Ignore hover, scrolling and clicks while Zen is on":"禅模式开启时忽略悬停、滚动和点按","In the Shelf":"在托盘中","In the menu bar":"在菜单栏中","Insights":"洞察","Items left of this divider are hidden":"此分隔符左侧的项目会被隐藏","Items left of this divider go to the Stash":"此分隔符左侧的项目会放入暗格","Items to the right of the Meno icon stay visible.":"Meno 图标右侧的项目会保持显示。","Keep Visible":"保持显示","Keep items where you put them":"让项目留在你放的位置","Keyboard shortcuts that work in every app.":"在任何 App 中都可用的键盘快捷键。","Language":"语言","Language / 语言 / 語言":"Language / 语言 / 語言","Launch Meno at login":"登录时打开 Meno","Layout":"布局","Leave it where it is":"保持原位","Let the menu bar adapt to what you are doing.":"让菜单栏随你手头的事情自动调整。","Makes room by hiding the menus of the frontmost app while items are shown.":"显示项目时暂时隐藏前台 App 的菜单，腾出空间。","Manage Scenes…":"管理场景…","Markers":"标记","Meno Settings":"Meno 设置","Meno asks GitHub whether there is a newer release. Nothing about you or your Mac is sent.":"Meno 会向 GitHub 查询是否有新版本，不会发送任何关于你或这台 Mac 的信息。","Meno uses the new language after it relaunches.":"Meno 重新打开后才会使用新的语言。","Meno — click to show or hide items, ⌥-click to include the Stash, right-click for more":"Meno — 点按显示或隐藏项目，按住 ⌥ 点按包含暗格，右键点按查看更多","Menu bar, calmed":"让菜单栏安静下来","More":"更多","Move Left":"向左移一格","Move Right":"向右移一格","Move to Hidden":"移到隐藏","Move to Stash":"移到暗格","Move to Visible":"移到常显","Never":"从不","Never shown in the menu bar. Reach these items from the Shelf, Quick Open or with ⌥-click.":"从不显示在菜单栏中。可通过托盘、快速打开或按住 ⌥ 点按来访问。","New Rule":"新建规则","No matching items":"没有匹配的项目","Nothing is hidden":"没有隐藏的项目","Open":"打开","Open Secondary Menu":"打开辅助菜单","Open Shelf":"打开托盘","Or drag it onto a section, or onto another item. A line shows on which side it will land.":"也可以直接拖：拖到某个分区，或拖到另一个项目上，竖线标出它会落在哪一边。","Pause All Rules":"暂停所有规则","Pause Rules":"暂停规则","Permissions":"权限","Put it in the Stash":"放入暗格","Quick Open":"快速打开","Quick Open…":"快速打开…","Quit Meno":"退出 Meno","Relaunch Meno to switch languages.":"重新打开 Meno 以切换语言。","Relaunch Now":"立即重新打开","Resume Rules":"恢复规则","Revealing hidden items":"显示隐藏项目","Rules":"规则","Rules are checked when apps switch, displays change, power or network changes, a microphone or camera starts or stops, and every 30 seconds.":"在切换 App、显示器变化、电源或网络变化、麦克风或摄像头开始或停止使用时，以及每 30 秒检查一次规则。","Rules are paused":"规则已暂停","Save arrangements and switch between them.":"存储多种布局并随时切换。","Scenes":"场景","Scroll or swipe over the menu bar":"在菜单栏上滚动或轻扫","Search menu bar items and actions":"搜索菜单栏项目和操作","Secondary click":"辅助点按","Sections":"分区","Settings…":"设置…","Shelf":"托盘","Show Everything":"显示全部","Show Hidden Items":"显示隐藏项目","Show hidden items":"显示隐藏项目","Show how many items are hidden next to the Meno icon":"在 Meno 图标旁显示隐藏项目的数量","Show in menu bar":"在菜单栏中显示","Show the battery when it runs low":"电量低时显示电池","Shown when you click the Meno icon, hover, scroll or use a hotkey.":"点按 Meno 图标、悬停、滚动或使用快捷键时显示。","Spaces, lines and labels to group your items.":"用空白、细线和标签给项目分组。","Start from a Preset":"从预设开始","Startup":"启动","Stash":"暗格","Stash section divider":"暗格分区分隔符","Swipe down to show, swipe up to hide.":"向下轻扫显示，向上轻扫隐藏。","The Meno icon, the Shelf and the look of the menu bar.":"Meno 图标、托盘以及菜单栏的外观。","The Shelf keeps items reachable when the menu bar is full, for example next to the camera housing.":"当菜单栏放不下时（例如刘海附近），托盘能让项目依然触手可及。","Turn Zen Off":"关闭禅模式","Turn Zen On":"开启禅模式","Undone afterwards.":"条件结束后撤销。","Use the Stash":"使用暗格","Visible":"常显","What Meno needs, and why.":"Meno 需要什么，以及为什么。","When %@: %@.":"当%@时，%@。","When a new item appears":"出现新项目时","When an app or macOS puts an item in another section, for example after the app restarted, Meno moves it back.":"当 App 或 macOS 把项目放到了别的分区（例如 App 重新启动后），Meno 会把它移回来。","When items need the room":"项目需要空间时","When the pointer leaves the menu bar":"指针离开菜单栏时","When you switch to another app or click elsewhere":"切换到其他 App 或点按别处时","While rules are paused, none of them applies. Rules that undo their action when it ends have undone it.":"规则暂停期间，任何规则都不会生效；设为“条件不再满足时撤销”的规则已撤销了它们的动作。","Work":"工作","Zen":"禅模式","Zen clears the menu bar for screenshots, recordings and presentations. Rules can turn it on for you, for example while Keynote is in front.":"禅模式会为截图、录屏和演示清空菜单栏。规则可以自动开启它，例如在 Keynote 位于前台时。","Zen during calls":"通话时开启禅模式","Zen is on. Click to leave Zen.":"禅模式已开启。点按以退出。","a microphone is in use":"麦克风正在使用","an external display is connected":"连接了外接显示器","apply “%@”":"应用场景“%@”","battery below %lld%%":"电量低于 %lld%%","keep %@ visible":"让 %@ 保持显示","macOS keeps this item in place":"macOS 固定了这个项目的位置","on battery":"使用电池供电","turn on Zen":"开启禅模式"},"zh-Hant":{" and ":"且","%lld items · %lld tucked away":"共 %lld 項 · %lld 項已收起","A Focus can change the menu bar too: in Shortcuts, add an automation for when the Focus turns on or off that opens a scene's link, such as meno://scene/Work.":"專注模式也能改變選單列：在「捷徑」裡為專注模式開啟或關閉時加入一個自動化操作，打開某個場景的連結，例如 meno://scene/Work。","A calm menu bar, made with glass.":"一個安靜的選單列，由玻璃打造。","A microphone is in use":"麥克風正在使用","A second hidden section for items you rarely need. They never appear in the menu bar, only in the Shelf, Quick Open or with ⌥-click.":"為很少用到的項目準備的第二個隱藏區段。它們永不出現在選單列中，只能透過托盤、快速開啟或按住 ⌥ 按一下來取用。","About":"關於","About Meno":"關於 Meno","Action":"動作","Actions":"更多動作","Active":"生效中","After":"延遲","Also hide the items in the Visible section":"同時隱藏「常顯」區段中的項目","Always":"永遠","Always shown in the menu bar.":"永遠顯示在選單列中。","An external display is connected":"已連接外接顯示器","Appearance":"外觀","Apply Scene “%@”":"套用場景「%@」","Apply a scene at the desk":"在辦公桌前套用場景","Arrange Menu Bar":"整理選單列","Arrange Menu Bar…":"整理選單列…","Ask me":"詢問我","Automatically":"自動","Check for Updates…":"檢查更新…","Check for updates once a day":"每天檢查一次更新","Choose which items stay in the menu bar and which ones Meno tucks away.":"選擇哪些項目留在選單列裡，哪些交給 Meno 收起來。","Clear the app menus":"清空 App 選單","Click an empty part of the menu bar":"按一下選單列的空白處","Click an item to choose where it goes: another section, or one step to the left or right.":"按一下項目，選擇把它放到哪裡：別的區段，或者往左、往右挪一格。","Clicking again hides the items.":"再次按一下會重新隱藏。","Close":"關閉","Delete":"刪除","Drag a file onto the menu bar":"把檔案拖到選單列上","Drop items here":"拖到這裡","Duplicate…":"製作副本…","Edit…":"編輯…","Finder":"Finder","Follow System":"跟隨系統","General":"一般","Good to know":"小提示","Hidden":"隱藏","Hidden items appear in the menu bar, so the file can be dropped on one of them. Items in the Shelf cannot take drops.":"隱藏的項目會顯示在選單列中，方便把檔案放到其中一個項目上。托盤中的項目無法接收拖放。","Hidden section divider":"隱藏區段分隔線","Hide Items":"隱藏項目","Hide automatically":"自動隱藏","Hide it":"隱藏它","Hiding again":"重新隱藏","Hotkeys":"快速鍵","Hover over an empty part of the menu bar":"指標停留在選單列空白處","How hidden items appear and disappear.":"隱藏項目如何出現和消失。","How you use the menu bar, measured on this Mac only.":"你如何使用選單列，僅在這台 Mac 上統計。","Ignore hover, scrolling and clicks while Zen is on":"禪模式開啟時忽略停留、捲動和按一下","In the Shelf":"在托盤中","In the menu bar":"在選單列中","Insights":"洞察","Items left of this divider are hidden":"此分隔線左側的項目會被隱藏","Items left of this divider go to the Stash":"此分隔線左側的項目會放入暗格","Items to the right of the Meno icon stay visible.":"Meno 圖示右側的項目會保持顯示。","Keep Visible":"保持顯示","Keep items where you put them":"讓項目留在你放的位置","Keyboard shortcuts that work in every app.":"在任何 App 中都可用的鍵盤快速鍵。","Language":"語言","Language / 语言 / 語言":"Language / 语言 / 語言","Launch Meno at login":"登入時開啟 Meno","Layout":"佈局","Leave it where it is":"保持原位","Let the menu bar adapt to what you are doing.":"讓選單列隨你手頭的事情自動調整。","Makes room by hiding the menus of the frontmost app while items are shown.":"顯示項目時暫時隱藏最前方 App 的選單，騰出空間。","Manage Scenes…":"管理場景…","Markers":"標記","Meno Settings":"Meno 設定","Meno asks GitHub whether there is a newer release. Nothing about you or your Mac is sent.":"Meno 會向 GitHub 詢問是否有新版本，不會傳送任何關於你或這台 Mac 的資訊。","Meno uses the new language after it relaunches.":"Meno 重新開啟後才會使用新的語言。","Meno — click to show or hide items, ⌥-click to include the Stash, right-click for more":"Meno — 按一下以顯示或隱藏項目，按住 ⌥ 並按一下以包含暗格，按一下右鍵以顯示更多","Menu bar, calmed":"讓選單列安靜下來","More":"更多","Move Left":"向左移一格","Move Right":"向右移一格","Move to Hidden":"移到隱藏","Move to Stash":"移到暗格","Move to Visible":"移到常顯","Never":"永不","Never shown in the menu bar. Reach these items from the Shelf, Quick Open or with ⌥-click.":"永不顯示在選單列中。可透過托盤、快速開啟或按住 ⌥ 按一下來取用。","New Rule":"新增規則","No matching items":"沒有符合的項目","Nothing is hidden":"沒有隱藏的項目","Open":"開啟","Open Secondary Menu":"開啟輔助選單","Open Shelf":"開啟托盤","Or drag it onto a section, or onto another item. A line shows on which side it will land.":"也可以直接拖：拖到某個區段，或拖到另一個項目上，直線標出它會落在哪一邊。","Pause All Rules":"暫停所有規則","Pause Rules":"暫停規則","Permissions":"權限","Put it in the Stash":"放入暗格","Quick Open":"快速開啟","Quick Open…":"快速開啟…","Quit Meno":"結束 Meno","Relaunch Meno to switch languages.":"重新開啟 Meno 以切換語言。","Relaunch Now":"立即重新開啟","Resume Rules":"恢復規則","Revealing hidden items":"顯示隱藏項目","Rules":"規則","Rules are checked when apps switch, displays change, power or network changes, a microphone or camera starts or stops, and every 30 seconds.":"在切換 App、顯示器變化、電源或網路變化、麥克風或相機開始或停止使用時，以及每 30 秒檢查一次規則。","Rules are paused":"規則已暫停","Save arrangements and switch between them.":"儲存多種佈局並隨時切換。","Scenes":"場景","Scroll or swipe over the menu bar":"在選單列上捲動或輕掃","Search menu bar items and actions":"搜尋選單列項目和動作","Secondary click":"輔助按一下","Sections":"區段","Settings…":"設定…","Shelf":"托盤","Show Everything":"顯示全部","Show Hidden Items":"顯示隱藏項目","Show hidden items":"顯示隱藏項目","Show how many items are hidden next to the Meno icon":"在 Meno 圖示旁顯示隱藏項目的數量","Show in menu bar":"在選單列中顯示","Show the battery when it runs low":"電量低時顯示電池","Shown when you click the Meno icon, hover, scroll or use a hotkey.":"按一下 Meno 圖示、停留、捲動或使用快速鍵時顯示。","Spaces, lines and labels to group your items.":"用空白、細線和標籤替項目分組。","Start from a Preset":"從預設開始","Startup":"啟動","Stash":"暗格","Stash section divider":"暗格區段分隔線","Swipe down to show, swipe up to hide.":"向下輕掃顯示，向上輕掃隱藏。","The Meno icon, the Shelf and the look of the menu bar.":"Meno 圖示、托盤以及選單列的外觀。","The Shelf keeps items reachable when the menu bar is full, for example next to the camera housing.":"當選單列放不下時（例如瀏海附近），托盤能讓項目依然觸手可及。","Turn Zen Off":"關閉禪模式","Turn Zen On":"開啟禪模式","Undone afterwards.":"條件結束後還原。","Use the Stash":"使用暗格","Visible":"常顯","What Meno needs, and why.":"Meno 需要什麼，以及為什麼。","When %@: %@.":"當%@時，%@。","When a new item appears":"出現新項目時","When an app or macOS puts an item in another section, for example after the app restarted, Meno moves it back.":"當 App 或 macOS 把項目放到了別的區段（例如 App 重新啟動後），Meno 會把它移回來。","When items need the room":"項目需要空間時","When the pointer leaves the menu bar":"指標離開選單列時","When you switch to another app or click elsewhere":"切換到其他 App 或按一下別處時","While rules are paused, none of them applies. Rules that undo their action when it ends have undone it.":"規則暫停期間，任何規則都不會生效；設為「條件不再滿足時還原」的規則已還原了它們的動作。","Work":"工作","Zen":"禪模式","Zen clears the menu bar for screenshots, recordings and presentations. Rules can turn it on for you, for example while Keynote is in front.":"禪模式會為截圖、螢幕錄製和簡報清空選單列。規則可以自動開啟它，例如在 Keynote 位於最前方時。","Zen during calls":"通話時開啟禪模式","Zen is on. Click to leave Zen.":"禪模式已開啟。按一下以結束。","a microphone is in use":"麥克風正在使用","an external display is connected":"已連接外接顯示器","apply “%@”":"套用場景「%@」","battery below %lld%%":"電量低於 %lld%%","keep %@ visible":"讓 %@ 保持顯示","macOS keeps this item in place":"macOS 固定了這個項目的位置","on battery":"使用電池供電","turn on Zen":"開啟禪模式"}}/*END-APP-STRINGS*/;

  // Strings of this page, not of the app.
  var SITE = {
    en: {
      demo: "Interactive demo · sample data",
      label: "Interactive demo of Meno in a Mac menu bar, with sample items",
      hint: {
        layout: "Click Meno’s icon to show or hide items. Click a chip, or drag it, to move an item.",
        reveal: "Click Meno’s icon, or empty menu bar, to show or hide items. Right-click the icon for its menu. Drag icons across the dividers.",
        shelf: "Click Meno’s icon to open or close the Shelf. Right-click it for its menu.",
        rules: "Switch on a condition below to see a rule act on the menu bar.",
        general: "Pick another language, then Relaunch Now."
      },
      clock: "Wed Sep 30  9:41",
      apps: ["Finder", "File", "Edit", "View", "Go", "Window", "Help"],
      scenes: ["Work", "Home", "Presenting"],
      notInDemo: "This pane isn’t part of the demo. Try General, Layout or Rules.",
      itemHint: "A sample item. Drag it across Meno’s dividers to move it.",
      tryIt: "Try it",
      window: "Meno Settings",
      closeWin: "Close window",
      menuBar: "Menu bar",
      version: "Version 0.12.0"
    },
    "zh-Hans": {
      demo: "可交互演示 · 示例数据",
      label: "Meno 在 Mac 菜单栏里的可交互演示，使用示例项目",
      hint: {
        layout: "点 Meno 图标显示或隐藏项目。点按或拖动下面的项目，把它移到别的分区。",
        reveal: "点 Meno 图标或菜单栏空白处，显示或隐藏项目；右键点按图标打开菜单。把图标拖过分隔符即可移动。",
        shelf: "点 Meno 图标打开或关闭托盘；右键点按图标打开菜单。",
        rules: "打开下面的一个条件，看看规则怎样改变菜单栏。",
        general: "选一种语言，再点“立即重新打开”。"
      },
      clock: "9月30日 周三  9:41",
      apps: ["访达", "文件", "编辑", "显示", "前往", "窗口", "帮助"],
      scenes: ["工作", "在家", "演示"],
      notInDemo: "演示里没有这个面板。试试通用、布局或规则。",
      itemHint: "示例项目。把它拖过 Meno 的分隔符即可移动。",
      tryIt: "试一试",
      window: "Meno 设置",
      closeWin: "关闭窗口",
      menuBar: "菜单栏",
      version: "版本 0.12.0"
    },
    "zh-Hant": {
      demo: "可互動示範 · 範例資料",
      label: "Meno 在 Mac 選單列裡的可互動示範，使用範例項目",
      hint: {
        layout: "按一下 Meno 圖像顯示或隱藏項目。按一下或拖移下面的項目，把它移到別的區段。",
        reveal: "按一下 Meno 圖像或選單列空白處，顯示或隱藏項目；右鍵按一下圖像打開選單。把圖像拖過分隔符號即可移動。",
        shelf: "按一下 Meno 圖像打開或關閉托盤；右鍵按一下圖像打開選單。",
        rules: "打開下面的一個條件，看看規則怎樣改變選單列。",
        general: "選一種語言，再按「立即重新開啟」。"
      },
      clock: "9月30日 週三  9:41",
      apps: ["Finder", "檔案", "編輯", "顯示方式", "前往", "視窗", "輔助說明"],
      scenes: ["工作", "在家", "簡報"],
      notInDemo: "示範裡沒有這個面板。試試一般、佈局或規則。",
      itemHint: "範例項目。把它拖過 Meno 的分隔符號即可移動。",
      tryIt: "試一試",
      window: "Meno 設定",
      closeWin: "關閉視窗",
      menuBar: "選單列",
      version: "版本 0.12.0"
    }
  };

  // ------------------------------------------------------------------ icons
  var SVG16 = '<svg viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.35" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false">';
  var DOT = function (x, y, r) { return '<circle cx="' + x + '" cy="' + y + '" r="' + r + '" fill="currentColor" stroke="none"/>'; };
  // Menu bar items: neutral template glyphs, drawn for this page.
  var GLYPH = {
    backup: '<rect x="1.8" y="4.6" width="12.4" height="6.8" rx="1.9"/><path d="M4.4 8h3.8"/>' + DOT(11.4, 8, 0.85),
    picker: '<path d="M11.9 1.9a1.5 1.5 0 0 1 2.2 2.2l-1.7 1.7-2.2-2.2zM10.2 3.6l2.2 2.2M11.3 4.7l-6.6 6.6-2.4.6.6-2.4 6.6-6.6"/>',
    translate: '<path d="M1.8 3.6h6.6M5.1 2v1.6M3.4 3.6c.6 2.2 2 3.9 4.2 4.8M6.9 3.6c-.6 2.5-2.2 4.4-4.9 5.5"/><path d="M8.6 14l2.7-6.6L14 14M9.6 11.8h3.4"/>',
    clip: '<rect x="3.2" y="2.9" width="9.6" height="11.3" rx="1.9"/><rect x="5.9" y="1.6" width="4.2" height="2.6" rx="1" fill="currentColor"/><path d="M5.6 7.4h4.8M5.6 10.2h3.2"/>',
    vpn: '<path d="M8 1.7l5.1 2v3.9c0 3.1-2.1 5.3-5.1 6.6-3-1.3-5.1-3.5-5.1-6.6V3.7z"/><path d="M5.9 7.9l1.5 1.5 2.8-2.9"/>',
    weather: '<circle cx="5.4" cy="5.4" r="2.1"/><path d="M5.4 1.3v.8M1.3 5.4h.8M2.5 2.5l.6.6M8.3 2.5l-.6.6"/><path d="M6 14h5.9a2.4 2.4 0 0 0 .3-4.8 3 3 0 0 0-5.7.7A2.1 2.1 0 0 0 6 14z"/>',
    sync: '<path d="M13 6.3A5.2 5.2 0 0 0 3.5 4.5M3 9.7a5.2 5.2 0 0 0 9.5 1.8"/><path d="M3.2 2.1v2.6h2.6M12.8 13.9v-2.6h-2.6"/>',
    timer: '<circle cx="8" cy="9.1" r="5.1"/><path d="M8 9.1V6.5M6.6 1.8h2.8M12.2 4.3l.9-.9"/>',
    cup: '<path d="M2.6 6.3h8.6v3.3a3.6 3.6 0 0 1-3.6 3.6H6.2a3.6 3.6 0 0 1-3.6-3.6z"/><path d="M11.2 7.3h.9a1.7 1.7 0 0 1 0 3.4h-1M5.2 2.1v2.1M7.9 2.1v2.1"/>',
    wifi: '<path d="M1.5 6.3a9.3 9.3 0 0 1 13 0M3.8 8.6a6 6 0 0 1 8.4 0M6 10.8a2.9 2.9 0 0 1 4 0" stroke-width="1.6"/>' + DOT(8, 12.9, 1.15),
    cc: '<rect x="1.8" y="2.4" width="12.4" height="4.8" rx="2.4"/>' + DOT(11.8, 4.8, 1.35) + '<rect x="1.8" y="8.8" width="12.4" height="4.8" rx="2.4"/>' + DOT(4.2, 11.2, 1.35)
  };
  var BATTERY = '<svg class="mnd-batt" viewBox="0 0 25 16" fill="none" stroke="currentColor" aria-hidden="true" focusable="false"><rect x="1.3" y="3.6" width="19.4" height="9" rx="2.8" stroke-opacity=".5" stroke-width="1.1"/><rect x="3" y="5.3" width="12.6" height="5.6" rx="1.4" fill="currentColor" stroke="none"/><path d="M22.6 6.6v3" stroke-opacity=".5" stroke-width="1.6" stroke-linecap="round"/></svg>';
  function glyph(name) { return name === "battery" ? BATTERY : SVG16 + GLYPH[name] + "</svg>"; }

  // Symbols of the Meno interface, drawn to look like their SF Symbols.
  var SYM = {
    gear: '<circle cx="8" cy="8" r="2.2"/><path d="M8 1.6v1.6M8 12.8v1.6M1.6 8h1.6M12.8 8h1.6M3.5 3.5l1.1 1.1M11.4 11.4l1.1 1.1M3.5 12.5l1.1-1.1M11.4 4.6l1.1-1.1"/><circle cx="8" cy="8" r="4.6"/>',
    layout: '<rect x="1.6" y="3.2" width="12.8" height="9.6" rx="2"/><path d="M5.9 3.2v9.6M10.1 3.2v9.6"/>',
    palette: '<path d="M8 1.8a6.2 6.2 0 1 0 0 12.4c1 0 1.4-.6 1.4-1.3 0-.9-.8-1.2-.8-2 0-.7.6-1.2 1.3-1.2h1.6a2.6 2.6 0 0 0 2.7-2.7C14.2 4.1 11.4 1.8 8 1.8z"/>' + DOT(4.8, 7, 0.9) + DOT(7, 4.6, 0.9) + DOT(10.2, 5, 0.9),
    command: '<path d="M5.8 5.8h4.4v4.4H5.8zM5.8 5.8V4.4a1.6 1.6 0 1 0-1.4 1.4zM10.2 5.8V4.4a1.6 1.6 0 1 1 1.4 1.4zM5.8 10.2v1.4a1.6 1.6 0 1 1-1.4-1.4zM10.2 10.2v1.4a1.6 1.6 0 1 0 1.4-1.4z"/>',
    wand: '<path d="M2.4 13.6l7.4-7.4M8.6 4.9l2.5 2.5"/><path d="M12 1.6v2.2M10.9 2.7h2.2M13.6 6.6v1.6M12.8 7.4h1.6M6.2 1.8v1.4M5.5 2.5h1.4" stroke-width="1.1"/>',
    stack: '<path d="M8 2l6 3-6 3-6-3z"/><path d="M2 8l6 3 6-3M2 11l6 3 6-3"/>',
    split: '<rect x="1.6" y="4" width="12.8" height="8" rx="1.8"/><path d="M6 4v8M10 4v8" stroke-dasharray="1.4 1.4"/>',
    chart: '<path d="M2 14h12"/><path d="M4 11.5V8M7 11.5V4.5M10 11.5V7M13 11.5V2.8" stroke-width="1.8"/>',
    lock: '<path d="M8 1.7l5.1 2v3.9c0 3.1-2.1 5.3-5.1 6.6-3-1.3-5.1-3.5-5.1-6.6V3.7z"/><rect x="5.9" y="7.4" width="4.2" height="3.4" rx=".7" fill="currentColor" stroke="none"/><path d="M6.7 7.4V6.5a1.3 1.3 0 0 1 2.6 0v.9"/>',
    info: '<circle cx="8" cy="8" r="6.2"/><path d="M8 7.2v4"/>' + DOT(8, 4.9, 0.9),
    search: '<circle cx="7" cy="7" r="4.4"/><path d="M10.3 10.3l3.6 3.6"/>',
    eye: '<path d="M1.4 8S3.8 3.6 8 3.6 14.6 8 14.6 8 12.2 12.4 8 12.4 1.4 8 1.4 8z"/><circle cx="8" cy="8" r="2"/>',
    eyeSlash: '<path d="M1.4 8S3.8 3.6 8 3.6 14.6 8 14.6 8 12.2 12.4 8 12.4 1.4 8 1.4 8z"/><path d="M2.6 2.6l10.8 10.8"/>',
    eyeCircle: '<circle cx="8" cy="8" r="6.4"/><path d="M3.8 8S5.5 5.5 8 5.5 12.2 8 12.2 8 10.5 10.5 8 10.5 3.8 8 3.8 8z"/>' + DOT(8, 8, 1.1),
    archive: '<rect x="1.8" y="2.6" width="12.4" height="3.2" rx="1"/><path d="M2.8 5.8v6.4a1.3 1.3 0 0 0 1.3 1.3h7.8a1.3 1.3 0 0 0 1.3-1.3V5.8M6.4 8.6h3.2"/>',
    leaf: '<path d="M2.8 13.2C2.8 6.8 6.6 3 13.4 2.8c.2 6.6-3.4 10.4-9.4 10.4"/><path d="M2.8 13.2c1.8-3.2 4.2-5.6 7.2-7.2"/>',
    leafFill: '<path d="M2.8 13.2C2.8 6.8 6.6 3 13.4 2.8c.2 6.6-3.4 10.4-9.4 10.4z" fill="currentColor"/>',
    pause: '<circle cx="8" cy="8" r="6.2"/><path d="M6.4 5.8v4.4M9.6 5.8v4.4"/>',
    shelf: '<rect x="1.6" y="2.4" width="12.8" height="11.2" rx="2"/><rect x="1.6" y="2.4" width="12.8" height="4.2" rx="2" fill="currentColor"/>',
    power: '<path d="M8 1.8v5.4M4.6 4a5.4 5.4 0 1 0 6.8 0"/>',
    update: '<circle cx="8" cy="8" r="6.2"/><path d="M8 4.8v6.2M5.4 8.6L8 11.1l2.6-2.5"/>',
    globe: '<circle cx="8" cy="8" r="6.2"/><path d="M1.8 8h12.4M8 1.8c1.8 1.8 2.6 3.9 2.6 6.2S9.8 12.4 8 14.2C6.2 12.4 5.4 10.3 5.4 8S6.2 3.6 8 1.8z"/>',
    plus: '<path d="M8 3v10M3 8h10" stroke-width="1.7"/>',
    sparkles: '<path d="M6.4 2.2l1.1 3.2 3.2 1.1-3.2 1.1-1.1 3.2-1.1-3.2-3.2-1.1 3.2-1.1zM12 9.4l.6 1.6 1.6.6-1.6.6-.6 1.6-.6-1.6-1.6-.6 1.6-.6z"/>',
    more: '<circle cx="8" cy="8" r="6.2"/>' + DOT(5.2, 8, 0.85) + DOT(8, 8, 0.85) + DOT(10.8, 8, 0.85),
    bulb: '<path d="M5.8 11.2c0-1.4-2.2-2.4-2.2-5a4.4 4.4 0 0 1 8.8 0c0 2.6-2.2 3.6-2.2 5zM6.2 13.4h3.6"/>',
    hand: '<path d="M5.6 8.4V3.6a1 1 0 0 1 2 0v4M7.6 7.6V2.8a1 1 0 0 1 2 0v4.8M9.6 7.6V3.8a1 1 0 0 1 2 0v5.6c0 2.6-1.8 4.6-4.4 4.6-1.6 0-2.6-.8-3.4-2L2.4 9.2a1 1 0 0 1 1.6-1.2l1.6 1.6"/>',
    cursor: '<path d="M3.4 2.4l9 4.4-3.8 1.2L6.8 12z"/>',
    mic: '<rect x="5.8" y="1.8" width="4.4" height="7.8" rx="2.2"/><path d="M3.4 7.6a4.6 4.6 0 0 0 9.2 0M8 12.2v2"/>',
    display: '<rect x="1.6" y="2.4" width="12.8" height="8.6" rx="1.6"/><path d="M6 13.6h4M8 11v2.6"/>',
    battery: '<rect x="1.4" y="4.6" width="11.4" height="6.8" rx="1.8"/><path d="M14.4 7v2"/><rect x="3" y="6.2" width="4" height="3.6" rx=".8" fill="currentColor" stroke="none"/>',
    moon: '<path d="M13.2 10.2A6 6 0 0 1 5.8 2.8 6 6 0 1 0 13.2 10.2z"/>',
    padlock: '<rect x="3.6" y="7" width="8.8" height="6.6" rx="1.6" fill="currentColor" stroke="none"/><path d="M5.4 7V5.2a2.6 2.6 0 0 1 5.2 0V7"/>',
    chevDown: '<path d="M4.4 6.2L8 9.8l3.6-3.6" stroke-width="1.8"/>',
    chevRight: '<path d="M6.2 3.8L10.4 8l-4.2 4.2" stroke-width="1.6"/>',
    updown: '<path d="M5 6.2L8 3.4l3 2.8M5 9.8L8 12.6l3-2.8" stroke-width="1.6"/>',
    check: '<path d="M3.4 8.4l3 3 6.2-6.8" stroke-width="1.8"/>',
    checkCircle: '<circle cx="8" cy="8" r="6.2"/><path d="M5.3 8.2l1.9 1.9 3.6-3.9"/>',
    xfill: '<circle cx="8" cy="8" r="6.6" fill="currentColor" stroke="none"/><path d="M5.8 5.8l4.4 4.4M10.2 5.8l-4.4 4.4" stroke="var(--mnd-xmark)" stroke-width="1.5"/>',
    arrowL: '<path d="M13 8H3.4M7.4 4L3.4 8l4 4"/>',
    arrowR: '<path d="M3 8h9.6M8.6 4l4 4-4 4"/>',
    mouse: '<path d="M3.2 3l9.6 4.2-4 1.4-1.4 4z"/><path d="M9.6 9.6l3 3"/>'
  };
  function sym(name, cls) { return SVG16.replace("<svg ", '<svg class="mnd-sym' + (cls ? " " + cls : "") + '" ') + SYM[name] + "</svg>"; }

  // Meno's own artwork (MenoIconRenderer.menoGlyph): three bars of increasing
  // height that fan out while items are revealed and fold together while they are hidden.
  var MENO_GLYPH = '<svg class="mnd-glyph" viewBox="0 0 18 18" aria-hidden="true" focusable="false">' +
    '<rect class="b1" x="5.2" y="5.25" width="3.2" height="7.5" rx="1.6" fill="currentColor" fill-opacity=".42"/>' +
    '<rect class="b2" x="8" y="3.75" width="3.2" height="10.5" rx="1.6" fill="currentColor" fill-opacity=".68"/>' +
    '<rect class="b3" x="10.8" y="2.25" width="3.2" height="13.5" rx="1.6" fill="currentColor"/></svg>';
  // Section dividers (MenoIconRenderer.dividerImage, chevron style).
  function divider(double) {
    var w = double ? 13 : 9, xs = double ? [-2.5, 2.5] : [0], p = "";
    xs.forEach(function (o) {
      var x = w / 2 + o;
      p += '<path d="M' + (x + 2) + " 4.5L" + (x - 2) + " 9L" + (x + 2) + ' 13.5"/>';
    });
    return '<svg viewBox="0 0 ' + w + ' 18" width="' + w + '" height="18" fill="none" stroke="currentColor" stroke-opacity=".6" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false">' + p + "</svg>";
  }

  // ------------------------------------------------------------------ sample data
  // Items and their sections. `tail` items sit right of the Meno icon, with the system items.
  var ITEMS = [
    { id: "backup", icon: "backup", n: ["Backup", "备份", "備份"] },
    { id: "picker", icon: "picker", n: ["Color Picker", "取色器", "取色器"] },
    { id: "translate", icon: "translate", n: ["Translator", "翻译", "翻譯"] },
    { id: "clip", icon: "clip", n: ["Clipboard", "剪贴板", "剪貼簿"] },
    { id: "vpn", icon: "vpn", n: ["VPN", "VPN", "VPN"] },
    { id: "weather", icon: "weather", text: "18°", n: ["Weather", "天气", "天氣"] },
    { id: "sync", icon: "sync", n: ["Sync", "同步", "同步"] },
    { id: "timer", icon: "timer", text: "24:12", n: ["Focus Timer", "专注计时", "專注計時"] },
    { id: "coffee", icon: "cup", n: ["Stay Awake", "保持唤醒", "保持喚醒"] },
    { id: "wifi", icon: "wifi", tail: true, n: ["Wi‑Fi", "无线局域网", "Wi‑Fi"] },
    { id: "battery", icon: "battery", tail: true, n: ["Battery", "电池", "電池"] },
    { id: "cc", icon: "cc", locked: true, n: ["Control Center", "控制中心", "控制中心"] },
    { id: "clock", locked: true, n: ["Clock", "时钟", "時鐘"] }
  ];
  var BY_ID = {};
  ITEMS.forEach(function (it) { BY_ID[it.id] = it; });
  var DEFAULT_ORD = { stash: ["backup", "picker", "translate"], hidden: ["clip", "vpn", "weather", "sync"], visible: ["timer", "coffee", "wifi", "battery"] };
  // Scenes remember the section and order of every movable item.
  var SCENES = [
    { symbol: "stack", ord: { stash: ["backup", "picker", "translate"], hidden: ["weather", "sync", "coffee"], visible: ["clip", "vpn", "timer", "wifi", "battery"] } },
    { symbol: "stack", ord: { stash: ["backup", "translate", "vpn"], hidden: ["clip", "picker", "timer", "sync"], visible: ["weather", "coffee", "wifi", "battery"] } },
    { symbol: "stack", ord: { stash: ["backup", "picker", "translate", "sync"], hidden: ["clip", "vpn", "weather", "timer", "coffee"], visible: ["wifi", "battery"] } }
  ];
  var LANG_IDX = { en: 0, "zh-Hans": 1, "zh-Hant": 2 };
  var PANES = [
    ["general", "General", "How hidden items appear and disappear.", "gear"],
    ["layout", "Layout", "Choose which items stay in the menu bar and which ones Meno tucks away.", "layout"],
    ["appearance", "Appearance", "The Meno icon, the Shelf and the look of the menu bar.", "palette"],
    ["hotkeys", "Hotkeys", "Keyboard shortcuts that work in every app.", "command"],
    ["rules", "Rules", "Let the menu bar adapt to what you are doing.", "wand"],
    ["scenes", "Scenes", "Save arrangements and switch between them.", "stack"],
    ["markers", "Markers", "Spaces, lines and labels to group your items.", "split"],
    ["insights", "Insights", "How you use the menu bar, measured on this Mac only.", "chart"],
    ["permissions", "Permissions", "What Meno needs, and why.", "lock"],
    ["about", "About", "A calm menu bar, made with glass.", "info"]
  ];
  var SECTIONS = {
    visible: ["Visible", "Always shown in the menu bar.", "eye", "Move to Visible"],
    hidden: ["Hidden", "Shown when you click the Meno icon, hover, scroll or use a hotkey.", "eyeSlash", "Move to Hidden"],
    stash: ["Stash", "Never shown in the menu bar. Reach these items from the Shelf, Quick Open or with ⌥-click.", "archive", "Move to Stash"]
  };
  var LANGUAGES = [["system", null], ["en", "English"], ["zh-Hans", "简体中文"], ["zh-Hant", "繁體中文"]];

  function esc(s) {
    return String(s).replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;").replace(/"/g, "&quot;");
  }
  function clone(o) { return JSON.parse(JSON.stringify(o)); }
  var reduceMotion = function () { return window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches; };

  // ------------------------------------------------------------------ demo
  function Demo(root) {
    this.root = root;
    this.pageLang = root.getAttribute("data-lang") === "zh" ? "zh-Hans" : "en";
    this.lang = this.pageLang;
    this.preset = root.getAttribute("data-preset") || "reveal";
    this.icon = root.getAttribute("data-icon") || "";
    this.st = this.initial(this.preset);
    this.build();
  }

  Demo.prototype = {
    // App strings: English keys, with %@ and %lld filled in order.
    L: function (key) {
      var table = APP[this.lang], s = (table && table[key]) || key, args = Array.prototype.slice.call(arguments, 1), i = 0;
      return s.replace(/%(?:@|lld|%)/g, function (m) { return m === "%%" ? "%" : String(args[i++]); });
    },
    D: function (key) { var t = SITE[this.lang] || SITE.en; return t[key] !== undefined ? t[key] : SITE.en[key]; },
    name: function (id) { return BY_ID[id].n[LANG_IDX[this.lang]]; },
    scene: function (i) { return this.D("scenes")[i]; },

    initial: function (preset) {
      var st = {
        reveal: 0, zen: false, ord: clone(DEFAULT_ORD),
        shelf: null, quick: null, menu: null, win: null, drag: null, flash: null,
        cfg: {
          login: true, updates: true, language: "system", emptyClick: true, hover: false, dragFile: true, scroll: false,
          revealStyle: "automatic", appMenus: "whenNeeded", autoRehide: true, rehideDelay: 10, rehideFocus: true, rehideExit: false,
          stash: true, count: false, newItem: "notify", keep: true, zenVisible: true, zenBlocks: true
        },
        rules: [
          { id: "r1", name: "Zen during calls", cond: ["mic"], action: ["zen"], on: true, undo: true },
          { id: "r2", name: "Apply a scene at the desk", cond: ["ext"], action: ["scene", 0], on: true, undo: false },
          { id: "r3", name: "Show the battery when it runs low", cond: ["battery", "below"], action: ["show", "battery"], on: false, undo: false }
        ],
        paused: false, mic: false, ext: false, active: {}, zenByRule: false
      };
      if (preset === "layout") { st.win = "layout"; st.reveal = 1; }
      else if (preset === "reveal") { st.reveal = 2; st.cfg.revealStyle = "menuBar"; }
      else if (preset === "shelf") { st.shelf = { stash: true }; st.cfg.revealStyle = "shelf"; }
      else if (preset === "rules") st.win = "rules";
      else if (preset === "general") st.win = "general";
      return st;
    },

    build: function () {
      var r = this.root, self = this;
      r.classList.add("mnd-ready");
      r.setAttribute("role", "group");
      var noscript = r.querySelector("noscript");
      r.innerHTML = "";
      if (noscript) r.appendChild(noscript);
      var scroller = document.createElement("div");
      scroller.className = "mnd-scroll";
      scroller.innerHTML = '<div class="mnd-screen mnd-p-' + this.preset + '">' +
        '<div class="mnd-bar"><div class="mnd-apps" aria-hidden="true"></div><div class="mnd-empty" data-act="empty"></div><div class="mnd-status" role="group"></div></div>' +
        '<div class="mnd-desk" data-act="desk"></div><div class="mnd-win-slot"></div><div class="mnd-shelf-slot"></div><div class="mnd-quick-slot"></div><div class="mnd-menu-slot"></div>' +
        '<div class="mnd-live" aria-live="polite"></div></div>';
      r.appendChild(scroller);
      var cap = document.createElement("figcaption");
      cap.className = "mnd-cap";
      r.appendChild(cap);
      this.scroller = scroller;
      this.screen = scroller.firstChild;
      this.bar = this.screen.querySelector(".mnd-bar");
      this.apps = this.screen.querySelector(".mnd-apps");
      this.status = this.screen.querySelector(".mnd-status");
      this.slots = {
        win: this.screen.querySelector(".mnd-win-slot"), shelf: this.screen.querySelector(".mnd-shelf-slot"),
        quick: this.screen.querySelector(".mnd-quick-slot"), menu: this.screen.querySelector(".mnd-menu-slot")
      };
      this.live = this.screen.querySelector(".mnd-live");
      this.cap = cap;
      this.els = {};
      this.makeStatus();
      r.addEventListener("click", function (e) { self.onClick(e); });
      r.addEventListener("contextmenu", function (e) { self.onContext(e); });
      r.addEventListener("keydown", function (e) { self.onKey(e); });
      r.addEventListener("input", function (e) { self.onInput(e); });
      r.addEventListener("change", function (e) { self.onInput(e); });
      r.addEventListener("pointerdown", function (e) { self.onPointerDown(e); });
      r.addEventListener("dragstart", function (e) { self.onDragStart(e); });
      r.addEventListener("dragover", function (e) { self.onDragOver(e); });
      r.addEventListener("dragleave", function (e) { self.onDragLeave(e); });
      r.addEventListener("drop", function (e) { self.onDrop(e); });
      r.addEventListener("dragend", function () { self.clearDrop(); });
      document.addEventListener("pointerdown", function (e) {
        if (!self.root.contains(e.target) && (self.st.menu || self.st.quick)) { self.st.menu = null; self.st.quick = null; self.render(); }
      });
      if (window.ResizeObserver) {
        this.lastW = 0;
        new ResizeObserver(function () {
          var w = self.scroller.clientWidth;
          if (Math.abs(w - self.lastW) < 1) return;
          self.lastW = w;
          if (self.st.menu) self.st.menu = null;
          self.render();
        }).observe(this.scroller);
      }
      this.render(true);
    },

    // ---------------------------------------------------------------- menu bar
    makeStatus: function () {
      var self = this, mk = function (cls, html) {
        var d = document.createElement("div");
        d.className = "mnd-si " + cls;
        d.innerHTML = '<div class="mnd-clip">' + html + "</div>";
        return d;
      };
      ITEMS.forEach(function (it) {
        var inner;
        if (it.id === "clock") inner = '<span class="mnd-sb mnd-clock"><span class="mnd-clock-l"></span><span class="mnd-clock-s">9:41</span></span>';
        else if (it.locked) inner = '<span class="mnd-sb">' + glyph(it.icon) + "</span>";
        else inner = '<button type="button" class="mnd-sb" data-act="item" data-v="' + it.id + '" data-k="si-' + it.id + '">' + glyph(it.icon) + (it.text ? '<span class="mnd-sbt">' + it.text + "</span>" : "") + "</button>";
        var el = mk("mnd-si-" + it.id + (it.locked ? " is-locked" : ""), inner);
        if (it.locked) el.setAttribute("aria-hidden", "true");
        self.els[it.id] = el;
      });
      this.els["D:stash"] = mk("mnd-div mnd-div2", '<button type="button" class="mnd-sb mnd-divb" data-act="divider" data-k="d-stash">' + divider(true) + "</button>");
      this.els["D:hidden"] = mk("mnd-div", '<button type="button" class="mnd-sb mnd-divb" data-act="divider" data-k="d-hidden">' + divider(false) + "</button>");
      this.els.MENO = mk("mnd-meno", '<button type="button" class="mnd-sb mnd-menob" data-act="meno" data-k="meno" aria-haspopup="menu">' + MENO_GLYPH + '<span class="mnd-leaf">' + sym("leafFill") + '</span><span class="mnd-count"></span></button>');
      this.els.MIC = mk("mnd-mic", '<span class="mnd-sb" aria-hidden="true"><span class="mnd-micdot">' + sym("mic") + "</span></span>");
    },

    // Every status element, left to right.
    sequence: function () {
      var o = this.st.ord, seq = [];
      o.stash.forEach(function (id) { seq.push(id); });
      seq.push("D:stash");
      o.hidden.forEach(function (id) { seq.push(id); });
      seq.push("D:hidden");
      o.visible.forEach(function (id) { if (!BY_ID[id].tail) seq.push(id); });
      seq.push("MENO");
      o.visible.forEach(function (id) { if (BY_ID[id].tail) seq.push(id); });
      seq.push("MIC", "cc", "clock");
      return seq;
    },
    sectionOf: function (id) {
      var o = this.st.ord;
      if (o.stash.indexOf(id) >= 0) return "stash";
      if (o.hidden.indexOf(id) >= 0) return "hidden";
      if (o.visible.indexOf(id) >= 0) return "visible";
      return "system";
    },
    // Whether an element is in the menu bar in a state (defaults to the current one).
    shown: function (key, s) {
      s = s || this.st;
      var zen = s.zen, hiddenOut = s.reveal < 1 || zen, stashOut = s.reveal < 2 || zen;
      if (key === "MENO" || key === "cc" || key === "clock") return true;
      if (key === "MIC") return !!s.mic;
      if (key === "D:stash") return s.cfg.stash && !stashOut;
      if (key === "D:hidden") return !hiddenOut;
      var sec = this.sectionOf(key);
      if (sec === "stash") return !stashOut;
      if (sec === "hidden") return !hiddenOut;
      if (sec === "visible") return !(zen && s.cfg.zenVisible && !BY_ID[key].tail);
      return true;
    },

    syncBar: function () {
      var self = this, st = this.st, seq = this.sequence(), status = this.status;
      var before = {};
      if (!this.firstSync) {
        seq.forEach(function (k) { var el = self.els[k]; if (el.parentNode && !el.classList.contains("is-out")) before[k] = el.getBoundingClientRect().left; });
      }
      // Minimal moves, so the transitions of elements that stay put keep running.
      for (var i = 0; i < seq.length; i++) {
        var el = this.els[seq[i]];
        if (status.children[i] !== el) status.insertBefore(el, status.children[i] || null);
      }
      seq.forEach(function (k) {
        var el = self.els[k], on = self.shown(k);
        el.classList.toggle("is-out", !on);
        if (on) el.removeAttribute("inert"); else el.setAttribute("inert", "");
        if (k !== "cc" && k !== "clock" && k !== "MIC") el.setAttribute("aria-hidden", on ? "false" : "true");
      });
      // Labels in the current language.
      ITEMS.forEach(function (it) {
        var b = self.els[it.id].querySelector("button");
        if (b) {
          b.setAttribute("aria-label", self.name(it.id));
          b.classList.toggle("is-flash", st.flash === it.id);
          b.setAttribute("aria-expanded", st.menu && st.menu.owner === "si-" + it.id ? "true" : "false");
        }
      });
      this.els.clock.querySelector(".mnd-clock-l").textContent = this.D("clock");
      var db = this.els["D:hidden"].querySelector("button"), ds = this.els["D:stash"].querySelector("button");
      db.setAttribute("aria-label", this.L("Hidden section divider"));
      db.title = this.L("Items left of this divider are hidden");
      ds.setAttribute("aria-label", this.L("Stash section divider"));
      ds.title = this.L("Items left of this divider go to the Stash");
      this.els["D:stash"].classList.toggle("is-off", !st.cfg.stash);
      var mb = this.els.MENO.querySelector("button");
      mb.classList.toggle("is-revealed", st.reveal > 0 && !st.zen);
      mb.classList.toggle("is-zen", st.zen);
      mb.classList.toggle("is-open", !!(st.menu && st.menu.owner === "meno") || !!st.shelf);
      mb.setAttribute("aria-label", "Meno");
      mb.setAttribute("aria-expanded", st.reveal > 0 && !st.zen ? "true" : "false");
      mb.title = st.zen ? this.L("Zen is on. Click to leave Zen.") : this.L("Meno — click to show or hide items, ⌥-click to include the Stash, right-click for more");
      var count = st.ord.hidden.length;
      mb.querySelector(".mnd-count").textContent = st.cfg.count && st.reveal === 0 && !st.zen && count ? String(count) : "";
      status.setAttribute("aria-label", this.D("menuBar"));
      // FLIP: items that changed places glide to their new spot.
      if (!this.firstSync && !reduceMotion()) {
        seq.forEach(function (k) {
          var el = self.els[k];
          if (before[k] === undefined || el.classList.contains("is-out")) return;
          var dx = before[k] - el.getBoundingClientRect().left;
          if (Math.abs(dx) > 1 && self.movedKeys && self.movedKeys[k] && el.animate) {
            el.animate([{ transform: "translateX(" + dx + "px)" }, { transform: "none" }], { duration: 320, easing: "cubic-bezier(.2,.8,.2,1)" });
          }
        });
      }
      this.movedKeys = null;
      this.firstSync = false;
      // App menus make room while revealed items need it ("Clear the app menus").
      var need = this.neededWidth(st), room = this.bar.clientWidth - 24, appsW = this.apps.scrollWidth;
      var clear = st.cfg.appMenus === "always" ? st.reveal > 0 : st.cfg.appMenus === "whenNeeded" ? st.reveal > 0 && need + appsW + 12 > room : false;
      this.apps.classList.toggle("is-cleared", clear);
      // A row of items wider than the screen: the screen grows and scrolls sideways, kept at its right end.
      var minW = need > this.scroller.clientWidth - 30 ? Math.ceil(need + 30) + "px" : "";
      if (this.screen.style.minWidth !== minW) {
        this.screen.style.minWidth = minW;
        var sc = this.scroller;
        sc.scrollLeft = sc.scrollWidth;
        clearTimeout(this.scrollTimer);
        this.scrollTimer = setTimeout(function () { sc.scrollLeft = sc.scrollWidth; }, 420);
      }
    },
    // Width the status items take in a state.
    neededWidth: function (s) {
      var self = this, w = 0;
      this.sequence().forEach(function (k) {
        if (!self.shown(k, s)) return;
        var inner = self.els[k].querySelector(".mnd-sb");
        w += inner ? inner.offsetWidth : 0;
      });
      return w;
    },

    // ---------------------------------------------------------------- render
    render: function (first) {
      var st = this.st, active = document.activeElement, key = null, sel = null;
      if (active && this.root.contains(active)) {
        key = active.getAttribute("data-k");
        if (active.tagName === "INPUT" && active.type === "search") sel = [active.selectionStart, active.selectionEnd];
      }
      if (first) this.firstSync = true;
      this.root.setAttribute("aria-label", this.D("label"));
      this.root.setAttribute("lang", this.lang === "en" ? "en" : this.lang === "zh-Hans" ? "zh-CN" : "zh-TW");
      this.apps.innerHTML = this.D("apps").map(function (a, i) { return "<span" + (i === 0 ? ' class="is-app"' : "") + ">" + esc(a) + "</span>"; }).join("");
      var narrow = this.screen.clientWidth < 600;
      this.screen.classList.toggle("is-narrow", narrow);
      this.screen.classList.toggle("is-tall", !!st.win || !!st.quick);
      this.screen.classList.toggle("is-menu", !!st.menu);
      if (!st.menu) st.flash = null;
      this.syncBar();
      var wbody = this.slots.win.querySelector(".mnd-wbody"), wscroll = wbody ? wbody.scrollTop : 0, prevPane = wbody ? wbody.getAttribute("data-pane") : null;
      this.slots.win.innerHTML = st.win ? this.windowHtml() : "";
      wbody = this.slots.win.querySelector(".mnd-wbody");
      if (wbody && prevPane === st.win) wbody.scrollTop = wscroll;
      this.slots.shelf.innerHTML = st.shelf ? this.shelfHtml() : "";
      this.slots.quick.innerHTML = st.quick ? this.quickHtml() : "";
      this.slots.menu.innerHTML = st.menu ? this.menuHtml(st.menu) : "";
      this.placeShelf();
      this.placeMenus();
      this.cap.innerHTML = this.capHtml();
      if (this.opening) {
        var el = this.screen.querySelector(this.opening);
        if (el && !reduceMotion()) el.classList.add("is-opening");
        this.opening = null;
      }
      if (st.menu && st.menu.focus && !this.focusKey) key = null; // the menu took focus
      if (key || this.focusKey) {
        var target = this.root.querySelector('[data-k="' + (this.focusKey || key) + '"]');
        if (target && !target.closest("[inert]")) {
          target.focus({ preventScroll: true });
          if (sel && target.setSelectionRange) target.setSelectionRange(sel[0], sel[1]);
        } else if (this.focusKey) {
          var mb = this.root.querySelector('[data-k="meno"]');
          if (mb) mb.focus({ preventScroll: true });
        }
        this.focusKey = null;
      }
      if (first) this.scroller.scrollLeft = this.scroller.scrollWidth;
    },
    focus: function (k) { this.focusKey = k; },
    say: function (text) { this.live.textContent = text; },

    capHtml: function () {
      var st = this.st, h = '<span class="mnd-tag"><span class="mnd-dot" aria-hidden="true"></span>' + esc(this.D("demo")) + "</span>";
      h += '<span class="mnd-hint">' + esc(this.D("hint")[this.preset]) + "</span>";
      if (this.preset === "rules") {
        var sw = function (k, on, label, icon) {
          return '<button type="button" class="mnd-try' + (on ? " is-on" : "") + '" data-act="sim" data-v="' + k + '" data-k="sim-' + k + '" aria-pressed="' + on + '">' + sym(icon) + esc(label) + "</button>";
        };
        h += '<span class="mnd-tries" role="group" aria-label="' + esc(this.D("tryIt")) + '"><span class="mnd-trylabel">' + esc(this.D("tryIt")) + "</span>" +
          sw("mic", st.mic, this.L("A microphone is in use"), "mic") + sw("ext", st.ext, this.L("An external display is connected"), "display") + "</span>";
      }
      return h;
    },

    // ---------------------------------------------------------------- shelf
    shelfHtml: function () {
      var self = this, st = this.st, hidden = st.ord.hidden, stash = st.shelf.stash && st.cfg.stash ? st.ord.stash : [];
      var btn = function (id) {
        return '<button type="button" class="mnd-shi" data-act="shelfitem" data-v="' + id + '" data-k="sh-' + id + '" title="' + esc(self.name(id)) + '" aria-label="' + esc(self.name(id)) + '" aria-haspopup="menu">' + glyph(BY_ID[id].icon) + "</button>";
      };
      var h = '<div class="mnd-shelf mnd-glass" role="toolbar" aria-label="' + esc(this.L("Shelf")) + '">';
      if (!hidden.length && !stash.length) h += '<span class="mnd-shempty">' + sym("checkCircle") + esc(this.L("Nothing is hidden")) + "</span>";
      else {
        h += hidden.map(btn).join("");
        if (stash.length) h += '<span class="mnd-shsep" title="' + esc(this.L("Stash")) + '"></span>' + stash.map(btn).join("");
      }
      h += '<span class="mnd-shtools"><button type="button" class="mnd-shtool" data-act="quick" data-k="sh-quick" title="' + esc(this.L("Quick Open")) + '" aria-label="' + esc(this.L("Quick Open")) + '">' + sym("search") + "</button>" +
        '<button type="button" class="mnd-shtool" data-act="arrange" data-k="sh-arrange" title="' + esc(this.L("Arrange Menu Bar")) + '" aria-label="' + esc(this.L("Arrange Menu Bar")) + '">' + sym("layout") + "</button></span>";
      return h + "</div>";
    },
    placeShelf: function () {
      var shelf = this.slots.shelf.firstChild;
      if (!shelf) return;
      var W = this.screen.clientWidth, sr = this.screen.getBoundingClientRect(), mr = this.els.MENO.getBoundingClientRect();
      var w = shelf.offsetWidth, x = mr.right - sr.left - w + 10; // under the icon, as in ShelfController.layout
      shelf.style.left = Math.max(8, Math.min(x, W - w - 8)) + "px";
    },

    // ---------------------------------------------------------------- quick open
    quickResults: function () {
      var self = this, st = this.st, q = st.quick.q.trim().toLowerCase(), out = [];
      var items = st.ord.stash.concat(st.ord.hidden, st.ord.visible);
      items.forEach(function (id) { out.push({ kind: "item", id: id, title: self.name(id), sec: self.sectionOf(id) }); });
      var cmds = [];
      SCENES.forEach(function (s, i) { cmds.push({ kind: "cmd", id: "scene" + i, title: self.L("Apply Scene “%@”", self.scene(i)), symbol: "stack" }); });
      cmds.push({ kind: "cmd", id: "zen", title: st.zen ? this.L("Turn Zen Off") : this.L("Turn Zen On"), symbol: "leaf", extra: "zen" });
      cmds.push({ kind: "cmd", id: "show", title: this.L("Show Hidden Items"), symbol: "eye" });
      if (st.cfg.stash) cmds.push({ kind: "cmd", id: "showall", title: this.L("Show Everything"), symbol: "eyeCircle" });
      cmds.push({ kind: "cmd", id: "hide", title: this.L("Hide Items"), symbol: "eyeSlash" });
      cmds.push({ kind: "cmd", id: "shelf", title: this.L("Open Shelf"), symbol: "shelf" });
      cmds.push({ kind: "cmd", id: "arrange", title: this.L("Arrange Menu Bar…"), symbol: "layout" });
      cmds.push({ kind: "cmd", id: "settings", title: this.L("Settings…"), symbol: "gear" });
      if (!q) return out.slice(0, 6).concat(cmds.slice(0, 3));
      var all = out.concat(cmds), hits = [];
      all.forEach(function (r) {
        var t = r.title.toLowerCase() + " " + (r.extra || ""), i = t.indexOf(q), score = -1;
        if (i === 0) score = 3; else if (i > 0) score = 2;
        else {
          // Letters in order, like the app's fuzzy match.
          var j = 0;
          for (var c = 0; c < t.length && j < q.length; c++) if (t[c] === q[j]) j++;
          if (j === q.length) score = 1;
        }
        if (score >= 0) hits.push([score, r]);
      });
      hits.sort(function (a, b) { return b[0] - a[0]; });
      return hits.map(function (h) { return h[1]; }).slice(0, 9);
    },
    quickHtml: function () {
      var self = this, st = this.st, res = this.quickResults();
      if (st.quick.sel >= res.length) st.quick.sel = Math.max(0, res.length - 1);
      this.qres = res;
      var rows = res.map(function (r, i) {
        var selc = i === st.quick.sel ? " is-sel" : "", key = i < 9 ? '<span class="mnd-qkey">⌘' + (i + 1) + "</span>" : "";
        if (r.kind === "item") {
          var sc = SECTIONS[r.sec];
          return '<div class="mnd-qrow' + selc + '" role="option" id="mnd-q' + i + '" aria-selected="' + (i === st.quick.sel) + '" data-act="qpick" data-v="' + i + '">' +
            '<span class="mnd-qicon">' + glyph(BY_ID[r.id].icon) + '</span><span class="mnd-qtext"><span class="mnd-qtitle">' + esc(r.title) + "</span></span>" +
            (sc ? '<span class="mnd-badge mnd-b-' + r.sec + '">' + esc(self.L(sc[0])) + "</span>" : "") + key + "</div>";
        }
        return '<div class="mnd-qrow' + selc + '" role="option" id="mnd-q' + i + '" aria-selected="' + (i === st.quick.sel) + '" data-act="qpick" data-v="' + i + '">' +
          '<span class="mnd-qicon is-cmd">' + sym(r.symbol) + '</span><span class="mnd-qtext"><span class="mnd-qtitle">' + esc(r.title) + "</span></span>" +
          '<span class="mnd-qaction">' + esc(self.L("Action")) + "</span>" + key + "</div>";
      }).join("");
      var hint = function (k, l) { return '<span class="mnd-khint"><kbd>' + k + "</kbd>" + esc(self.L(l)) + "</span>"; };
      return '<div class="mnd-quick mnd-glass" role="dialog" aria-label="' + esc(this.L("Quick Open")) + '">' +
        '<div class="mnd-qfield">' + sym("search") + '<input type="search" data-k="quick" class="mnd-qinput" role="combobox" aria-expanded="true" aria-controls="mnd-qlist" aria-activedescendant="' + (res.length ? "mnd-q" + st.quick.sel : "") + '" placeholder="' + esc(this.L("Search menu bar items and actions")) + '" aria-label="' + esc(this.L("Search menu bar items and actions")) + '" value="' + esc(st.quick.q) + '" autocomplete="off" spellcheck="false"></div>' +
        (res.length ? '<div class="mnd-qlist" id="mnd-qlist" role="listbox">' + rows + "</div>" : '<div class="mnd-qnone" id="mnd-qlist" role="listbox">' + esc(this.L("No matching items")) + "</div>") +
        '<div class="mnd-qfoot">' + hint("↩", "Open") + '<span class="mnd-qwide">' + hint("⌘↩", "Secondary click") + hint("⌥↩", "Show in menu bar") + hint("⌘K", "Actions") + "</span><span class=\"mnd-qsp\"></span>" + hint("esc", "Close") + "</div></div>";
    },

    // ---------------------------------------------------------------- menus
    // A menu: { owner, anchor: element key or rect, items: [{t, icon, act, v, dis, chk, sep, sub, key}] }
    menoMenu: function () {
      var st = this.st, L = this.L.bind(this), revealed = st.reveal > 0 && !st.zen, items = [];
      items.push({ t: revealed ? L("Hide Items") : L("Show Hidden Items"), icon: revealed ? "eyeSlash" : "eye", act: "m-toggle" });
      if (st.cfg.stash) items.push({ t: L("Show Everything"), icon: "eyeCircle", act: "m-all" });
      items.push({ sep: 1 });
      items.push({ t: L("Quick Open…"), icon: "search", act: "quick" });
      items.push({ t: L("Open Shelf"), icon: "shelf", act: "m-shelf" });
      items.push({ t: L("Zen"), icon: st.zen ? "leafFill" : "leaf", act: "m-zen", chk: st.zen });
      if (st.rules.length) items.push({ t: L("Pause Rules"), icon: "pause", act: "m-pause", chk: st.paused });
      var sub = SCENES.map(function (s, i) { return { t: this.scene(i), icon: "stack", act: "m-scene", v: i }; }, this);
      sub.push({ sep: 1 }, { t: L("Manage Scenes…"), icon: "layout", act: "m-pane", v: "scenes" });
      items.push({ t: L("Scenes"), icon: "stack", sub: sub });
      items.push({ sep: 1 });
      items.push({ t: L("Arrange Menu Bar…"), icon: "layout", act: "arrange" });
      items.push({ t: L("Settings…"), icon: "gear", act: "m-pane", v: "general", key: "⌘," });
      items.push({ sep: 1 });
      items.push({ t: L("About Meno"), icon: "info", act: "m-pane", v: "about" });
      items.push({ t: L("Check for Updates…"), icon: "update", dis: 1 });
      items.push({ t: L("Quit Meno"), icon: "power", dis: 1, key: "⌘Q" });
      return items;
    },
    moveItems: function (id, withOpen) {
      var sec = this.sectionOf(id), L = this.L.bind(this), items = [];
      if (withOpen) items.push({ t: L("Open"), act: "i-open", v: id }, { t: L("Open Secondary Menu"), act: "i-open", v: id }, { sep: 1 });
      if (sec !== "visible") items.push({ t: withOpen ? L("Keep Visible") : L("Move to Visible"), icon: withOpen ? null : "eye", act: "i-move", v: id + ":visible" });
      if (sec !== "hidden") items.push({ t: L("Move to Hidden"), icon: withOpen ? null : "eyeSlash", act: "i-move", v: id + ":hidden" });
      if (sec !== "stash" && this.st.cfg.stash) items.push({ t: L("Move to Stash"), icon: withOpen ? null : "archive", act: "i-move", v: id + ":stash" });
      return items;
    },
    chipItems: function (id) {
      if (BY_ID[id].locked) return [{ t: this.L("macOS keeps this item in place"), icon: "padlock", dis: 1 }];
      var items = this.moveItems(id, false), list = this.st.ord[this.sectionOf(id)], i = list.indexOf(id);
      items.push({ sep: 1 });
      items.push({ t: this.L("Move Left"), icon: "arrowL", act: "i-step", v: id + ":-1", dis: i <= 0 });
      items.push({ t: this.L("Move Right"), icon: "arrowR", act: "i-step", v: id + ":1", dis: i >= list.length - 1 });
      return items;
    },
    menuHtml: function (m) {
      var h = this.menuList(m.items, "mnd-m0");
      if (m.subOpen !== undefined && m.items[m.subOpen] && m.items[m.subOpen].sub) h += this.menuList(m.items[m.subOpen].sub, "mnd-m1");
      return h;
    },
    menuList: function (items, cls) {
      var anyIcon = items.some(function (it) { return it.icon || it.chk !== undefined || it.radio !== undefined; });
      var h = '<div class="mnd-menu mnd-glassmenu ' + cls + '" role="menu">';
      items.forEach(function (it, i) {
        if (it.sep) { h += '<div class="mnd-msep" role="separator"></div>'; return; }
        if (it.header) { h += '<div class="mnd-mhead" role="presentation">' + esc(it.t) + "</div>"; return; }
        if (it.note) { h += '<div class="mnd-mnote" role="presentation">' + esc(it.t) + "</div>"; return; }
        var role = it.chk !== undefined ? "menuitemcheckbox" : it.radio !== undefined ? "menuitemradio" : "menuitem";
        h += '<button type="button" class="mnd-mi' + (it.dis ? " is-dis" : "") + '" role="' + role + '"' + (it.chk !== undefined || it.radio !== undefined ? ' aria-checked="' + !!(it.chk || it.radio) + '"' : "") +
          (it.dis ? ' aria-disabled="true"' : "") + (it.sub ? ' aria-haspopup="menu" data-sub="' + i + '"' : "") + ' data-act="' + (it.sub ? "m-sub" : it.act || "") + '" data-v="' + esc(it.v !== undefined ? it.v : "") + '" data-mi="' + cls + "-" + i + '" tabindex="-1">' +
          (anyIcon ? '<span class="mnd-mic">' + (it.chk || it.radio ? sym("check") : it.icon ? sym(it.icon) : "") + "</span>" : "") +
          '<span class="mnd-mt">' + esc(it.t) + "</span>" + (it.key ? '<span class="mnd-mk">' + esc(it.key) + "</span>" : "") + (it.sub ? sym("chevRight", "mnd-msub") : "") + "</button>";
      });
      return h + "</div>";
    },
    placeMenus: function () {
      var m = this.st.menu;
      if (!m) return;
      var W = this.screen.clientWidth, H = parseFloat(getComputedStyle(this.screen).getPropertyValue("--h")) || this.screen.clientHeight, sr = this.screen.getBoundingClientRect();
      var m0 = this.slots.menu.querySelector(".mnd-m0"), m1 = this.slots.menu.querySelector(".mnd-m1");
      var a = this.root.querySelector('[data-k="' + m.owner + '"]'), r = a ? a.getBoundingClientRect() : sr;
      var x = r.left - sr.left, y = r.bottom - sr.top + (m.gap !== undefined ? m.gap : 4);
      if (m.popup) { x = r.left - sr.left; y = r.bottom - sr.top + 3; }
      var w = m0.offsetWidth, h = m0.offsetHeight;
      x = Math.max(6, Math.min(x, W - w - 6));
      if (y + h > H - 6) y = Math.max(6, (m.popup ? r.top - sr.top - h - 3 : H - h - 6));
      m0.style.left = x + "px"; m0.style.top = y + "px";
      if (m1) {
        var row = m0.querySelector('[data-sub="' + m.subOpen + '"]'), rr = row.getBoundingClientRect(), w1 = m1.offsetWidth;
        var x1 = x + w - 4;
        if (x1 + w1 > W - 6) x1 = x - w1 + 4;
        var y1 = rr.top - sr.top - 5;
        if (y1 + m1.offsetHeight > H - 6) y1 = H - m1.offsetHeight - 6;
        m1.style.left = Math.max(6, x1) + "px"; m1.style.top = Math.max(6, y1) + "px";
      }
      var focusEl = this.slots.menu.querySelector('[data-mi="' + (m.focus || "") + '"]');
      if (focusEl) focusEl.focus({ preventScroll: true });
    },
    openMenu: function (owner, items, opts) {
      var m = { owner: owner, items: items };
      if (opts) for (var k in opts) m[k] = opts[k];
      if (m.keyboard) {
        var first = -1;
        items.some(function (it, i) { if (!it.sep && !it.header && !it.note && !it.dis) { first = i; return true; } return false; });
        m.focus = first >= 0 ? "mnd-m0-" + first : null;
        if (!m.focus) this.focus(owner);
      }
      this.st.menu = m;
      this.opening = ".mnd-m0";
      this.render();
    },
    closeMenu: function (refocus) {
      var m = this.st.menu;
      this.st.menu = null;
      if (refocus && m) this.focus(m.owner);
      this.render();
    },

    // ---------------------------------------------------------------- settings window
    windowHtml: function () {
      var self = this, st = this.st, pane = st.win, info = PANES.filter(function (p) { return p[0] === pane; })[0];
      var side = PANES.map(function (p, i) {
        var on = p[0] === pane;
        return '<button type="button" class="mnd-sbtn' + (on ? " is-on" : "") + '" data-act="pane" data-v="' + p[0] + '" data-k="pane-' + p[0] + '"' + (on ? ' aria-current="page"' : "") + ' title="' + esc(self.L(p[1])) + " (⌘" + ((i + 1) % 10) + ')">' +
          sym(p[3]) + '<span class="mnd-sbt2">' + esc(self.L(p[1])) + "</span></button>";
      }).join("");
      var tucked = st.ord.hidden.length + st.ord.stash.length, total = ITEMS.length;
      var h = '<section class="mnd-window" aria-label="' + esc(this.D("window")) + '">' +
        '<div class="mnd-lights"><button type="button" class="mnd-light is-close" data-act="closewin" data-k="closewin" aria-label="' + esc(this.D("closeWin")) + '"></button><span class="mnd-light is-min"></span><span class="mnd-light is-zoom"></span></div>' +
        '<nav class="mnd-side mnd-glass" aria-label="' + esc(this.D("window")) + '">' +
        '<div class="mnd-sidehead">' + (this.icon ? '<img src="' + esc(this.icon) + '" alt="" width="34" height="34">' : "") + '<span><strong>Meno</strong><small>' + esc(this.L("Menu bar, calmed")) + "</small></span></div>" +
        '<div class="mnd-sidelist">' + side + "</div>" +
        '<div class="mnd-sidestat"><span class="mnd-green" aria-hidden="true"></span>' + esc(this.L("%lld items · %lld tucked away", total, tucked)) + "</div></nav>" +
        '<div class="mnd-wbody" data-pane="' + pane + '"><div class="mnd-wcontent">' +
        '<header class="mnd-phead"><span class="mnd-ptile mnd-glass">' + sym(info[3]) + '</span><span><h3 class="mnd-ptitle">' + esc(this.L(info[1])) + '</h3><span class="mnd-psub">' + esc(this.L(info[2])) + "</span></span></header>";
      if (pane === "general") h += this.generalPane();
      else if (pane === "layout") h += this.layoutPane();
      else if (pane === "rules") h += this.rulesPane();
      else if (pane === "about") h += this.aboutPane();
      else h += '<p class="mnd-notin">' + esc(this.D("notInDemo")) + "</p>";
      return h + "</div></div></section>";
    },
    card: function (title, icon, body, foot) {
      return '<div class="mnd-card mnd-glass"><div class="mnd-chead">' + sym(icon) + "<span>" + esc(this.L(title)) + "</span></div>" +
        '<div class="mnd-cbody">' + body + "</div>" + (foot ? '<p class="mnd-foot">' + esc(this.L(foot)) + "</p>" : "") + "</div>";
    },
    row: function (title, sub, control, raw) {
      var id = "mnd-l" + (this.uid = (this.uid || 0) + 1);
      return '<div class="mnd-row"><div class="mnd-rtext"><span class="mnd-rtitle" id="' + id + '">' + esc(raw ? title : this.L(title)) + "</span>" +
        (sub ? '<span class="mnd-rsub">' + esc(this.L(sub)) + "</span>" : "") + "</div>" + control.replace(/%LBL%/g, id) + "</div>";
    },
    toggle: function (title, sub, key, on) {
      if (on === undefined) on = this.st.cfg[key];
      return this.row(title, sub, '<button type="button" class="mnd-switch' + (on ? " is-on" : "") + '" role="switch" aria-checked="' + !!on + '" aria-labelledby="%LBL%" data-act="cfg" data-v="' + key + '" data-k="cfg-' + key + '"><span></span></button>');
    },
    popup: function (key, label, width) {
      return '<button type="button" class="mnd-popup" data-act="popup" data-v="' + key + '" data-k="pop-' + key + '" aria-haspopup="menu" aria-labelledby="%LBL% pop-' + key + '-v"' + (width ? ' style="min-width:' + width + 'px"' : "") + '><span id="pop-' + key + '-v">' + esc(label) + "</span>" + sym("updown") + "</button>";
    },
    POPUPS: {
      revealStyle: [["menuBar", "In the menu bar"], ["shelf", "In the Shelf"], ["automatic", "Automatically"]],
      appMenus: [["never", "Never"], ["whenNeeded", "When items need the room"], ["always", "Always"]],
      newItem: [["ignore", "Leave it where it is"], ["notify", "Ask me"], ["hide", "Hide it"], ["stash", "Put it in the Stash"]]
    },
    popupLabel: function (key) {
      var v = this.st.cfg[key];
      if (key === "language") { var l = LANGUAGES.filter(function (x) { return x[0] === v; })[0]; return l[1] || this.L("Follow System"); }
      return this.L(this.POPUPS[key].filter(function (x) { return x[0] === v; })[0][1]);
    },
    popupItems: function (key) {
      var self = this, v = this.st.cfg[key];
      if (key === "language") return LANGUAGES.map(function (l) { return { t: l[1] || self.L("Follow System"), radio: l[0] === v, act: "setcfg", v: key + ":" + l[0] }; });
      return this.POPUPS[key].map(function (o) { return { t: self.L(o[1]), radio: o[0] === v, act: "setcfg", v: key + ":" + o[0] }; });
    },
    atLaunch: function () { return this.launchLang || "system"; },
    generalPane: function () {
      var c = this.st.cfg, h = "";
      h += this.card("Startup", "power", this.toggle("Launch Meno at login", null, "login") +
        this.toggle("Check for updates once a day", "Meno asks GitHub whether there is a newer release. Nothing about you or your Mac is sent.", "updates"));
      var lang = this.row("Language / 语言 / 語言", "Meno uses the new language after it relaunches.", this.popup("language", this.popupLabel("language"), 150));
      if (c.language !== this.atLaunch()) {
        lang += '<div class="mnd-relaunch"><span>' + esc(this.L("Relaunch Meno to switch languages.")) + '</span><button type="button" class="mnd-btn is-prominent" data-act="relaunch" data-k="relaunch">' + esc(this.L("Relaunch Now")) + "</button></div>";
      }
      h += this.card("Language", "globe", lang);
      h += this.card("Revealing hidden items", "eye",
        this.toggle("Click an empty part of the menu bar", "Clicking again hides the items.", "emptyClick") +
        this.toggle("Hover over an empty part of the menu bar", null, "hover") +
        this.toggle("Drag a file onto the menu bar", "Hidden items appear in the menu bar, so the file can be dropped on one of them. Items in the Shelf cannot take drops.", "dragFile") +
        this.toggle("Scroll or swipe over the menu bar", "Swipe down to show, swipe up to hide.", "scroll") +
        '<div class="mnd-hr"></div>' +
        this.row("Show hidden items", "The Shelf keeps items reachable when the menu bar is full, for example next to the camera housing.", this.popup("revealStyle", this.popupLabel("revealStyle"))) +
        this.row("Clear the app menus", "Makes room by hiding the menus of the frontmost app while items are shown.", this.popup("appMenus", this.popupLabel("appMenus"))));
      var after = "";
      if (c.autoRehide) {
        after = this.row("After", null, '<span class="mnd-slider"><input type="range" min="2" max="60" step="1" value="' + c.rehideDelay + '" data-act="delay" data-k="delay" aria-labelledby="%LBL%" aria-valuetext="' + esc(this.secs(c.rehideDelay)) + '"><output>' + esc(this.secs(c.rehideDelay)) + "</output></span>");
      }
      h += this.card("Hiding again", "eyeSlash", this.toggle("Hide automatically", null, "autoRehide") + after +
        this.toggle("When you switch to another app or click elsewhere", null, "rehideFocus") +
        this.toggle("When the pointer leaves the menu bar", null, "rehideExit"));
      h += this.card("Sections", "split",
        this.toggle("Use the Stash", "A second hidden section for items you rarely need. They never appear in the menu bar, only in the Shelf, Quick Open or with ⌥-click.", "stash") +
        this.toggle("Show how many items are hidden next to the Meno icon", null, "count") +
        this.row("When a new item appears", null, this.popup("newItem", this.popupLabel("newItem"))) +
        this.toggle("Keep items where you put them", "When an app or macOS puts an item in another section, for example after the app restarted, Meno moves it back.", "keep"));
      h += this.card("Zen", "leaf",
        this.toggle("Also hide the items in the Visible section", "Items to the right of the Meno icon stay visible.", "zenVisible") +
        this.toggle("Ignore hover, scrolling and clicks while Zen is on", null, "zenBlocks") +
        '<div class="mnd-right"><button type="button" class="mnd-btn' + (this.st.zen ? "" : " is-prominent") + '" data-act="m-zen" data-k="zenbtn">' + esc(this.st.zen ? this.L("Turn Zen Off") : this.L("Turn Zen On")) + "</button></div>",
        "Zen clears the menu bar for screenshots, recordings and presentations. Rules can turn it on for you, for example while Keynote is in front.");
      return h;
    },
    secs: function (v) { return this.lang === "en" ? v + " sec" : v + "秒"; },
    layoutPane: function () {
      var self = this, st = this.st, h = "";
      var tip = function (icon, text) { return '<div class="mnd-tip">' + sym(icon) + "<span>" + esc(self.L(text)) + "</span></div>"; };
      h += this.card("Good to know", "bulb",
        tip("mouse", "Click an item to choose where it goes: another section, or one step to the left or right.") +
        tip("hand", "Or drag it onto a section, or onto another item. A line shows on which side it will land."));
      ["visible", "hidden", "stash"].forEach(function (sec) {
        if (sec === "stash" && !st.cfg.stash) return;
        var ids = st.ord[sec].slice();
        if (sec === "visible") ids = ids.concat(["cc", "clock"]);
        var s = SECTIONS[sec];
        var chips = ids.map(function (id) {
          var it = BY_ID[id];
          return '<button type="button" class="mnd-chip" data-act="chip" data-v="' + id + '" data-k="chip-' + id + '" aria-haspopup="menu"' + (it.locked ? "" : ' draggable="true"') +
            ' aria-label="' + esc(self.name(id) + ", " + self.L(s[0])) + '">' + (it.id === "clock" ? '<span class="mnd-chipclock">9:41</span>' : glyph(it.icon)) + "<span>" + esc(self.name(id)) + "</span>" + sym(it.locked ? "padlock" : "chevDown", "mnd-chipchev") + "</button>";
        }).join("");
        h += '<div class="mnd-lane mnd-glass" data-lane="' + sec + '"><div class="mnd-lhead"><span class="mnd-lsym mnd-c-' + sec + '">' + sym(s[2]) + '</span><span class="mnd-ltitle">' + esc(self.L(s[0])) + '</span><span class="mnd-lcount mnd-b-' + sec + '">' + ids.length + "</span></div>" +
          '<p class="mnd-lsub">' + esc(self.L(s[1])) + "</p>" +
          (ids.length ? '<div class="mnd-chips">' + chips + "</div>" : '<div class="mnd-dropzone">' + esc(self.L("Drop items here")) + "</div>") + "</div>";
      });
      return h;
    },
    ruleText: function (r) {
      var self = this, L = this.L.bind(this);
      var cond = r.cond.map(function (c) {
        return c === "mic" ? L("a microphone is in use") : c === "ext" ? L("an external display is connected") : c === "battery" ? L("on battery") : L("battery below %lld%%", 20);
      }).join(L(" and "));
      var a = r.action, act = a[0] === "zen" ? L("turn on Zen") : a[0] === "scene" ? L("apply “%@”", self.scene(a[1])) : L("keep %@ visible", self.name(a[1]));
      var s = L("When %@: %@.", cond, act);
      if (r.undo) s += " " + L("Undone afterwards.");
      return s;
    },
    rulesPane: function () {
      var self = this, st = this.st, h = "";
      h += this.card("Rules", "wand",
        '<div class="mnd-rulebar"><button type="button" class="mnd-btn is-prominent" data-act="noop" aria-disabled="true">' + sym("plus") + esc(this.L("New Rule")) + '</button>' +
        '<button type="button" class="mnd-btn is-plain" data-act="noop" aria-disabled="true">' + sym("sparkles") + esc(this.L("Start from a Preset")) + sym("chevDown", "mnd-small") + "</button><span class=\"mnd-flex\"></span>" +
        '<span class="mnd-pause"><span id="mnd-pauselbl">' + esc(this.L("Pause All Rules")) + '</span><button type="button" class="mnd-switch is-small' + (st.paused ? " is-on" : "") + '" role="switch" aria-checked="' + st.paused + '" aria-labelledby="mnd-pauselbl" data-act="m-pause" data-k="pause"><span></span></button></span></div>',
        "Rules are checked when apps switch, displays change, power or network changes, a microphone or camera starts or stops, and every 30 seconds.");
      if (st.paused) {
        h += '<div class="mnd-banner mnd-glass">' + sym("pause") + '<div><strong>' + esc(this.L("Rules are paused")) + "</strong><span>" + esc(this.L("While rules are paused, none of them applies. Rules that undo their action when it ends have undone it.")) + '</span></div><button type="button" class="mnd-btn is-prominent" data-act="m-pause" data-k="resume">' + esc(this.L("Resume Rules")) + "</button></div>";
      }
      st.rules.forEach(function (r) {
        var active = !!st.active[r.id], a = r.action[0], icon = a === "zen" ? "leaf" : a === "scene" ? "stack" : "eye";
        h += '<div class="mnd-rule mnd-glass' + (active ? " is-active" : "") + '"><span class="mnd-ricon">' + sym(icon) + '</span><div class="mnd-rtext2"><div class="mnd-rname"><span id="mnd-rn-' + r.id + '">' + esc(self.L(r.name)) + "</span>" +
          (active ? '<span class="mnd-active">' + esc(self.L("Active")) + "</span>" : "") + '</div><p>' + esc(self.ruleText(r)) + "</p></div>" +
          '<button type="button" class="mnd-switch is-small' + (r.on ? " is-on" : "") + '" role="switch" aria-checked="' + r.on + '" aria-labelledby="mnd-rn-' + r.id + '" data-act="rule" data-v="' + r.id + '" data-k="rule-' + r.id + '"><span></span></button>' +
          '<button type="button" class="mnd-rmore" data-act="rulemenu" data-v="' + r.id + '" data-k="rm-' + r.id + '" aria-label="' + esc(self.L("More")) + '" aria-haspopup="menu">' + sym("more") + "</button></div>";
      });
      h += '<div class="mnd-focus">' + sym("moon") + "<span>" + esc(this.L("A Focus can change the menu bar too: in Shortcuts, add an automation for when the Focus turns on or off that opens a scene's link, such as meno://scene/Work.")) + "</span></div>";
      return h;
    },
    aboutPane: function () {
      return '<div class="mnd-card mnd-glass mnd-about">' + (this.icon ? '<img src="' + esc(this.icon) + '" alt="" width="84" height="84">' : "") +
        '<strong>Meno</strong><span>' + esc(this.D("version")) + "</span><em>" + esc(this.L("A calm menu bar, made with glass.")) + "</em></div>";
    },

    // ---------------------------------------------------------------- actions
    // Reveals or hides like RevealCoordinator: `level` 0 hides, 1 shows Hidden, 2 shows everything.
    setReveal: function (level, trigger) {
      var st = this.st;
      if (st.zen) { this.setZen(false); return; }
      if (level > 0 && trigger !== "force") {
        var style = st.cfg.revealStyle;
        var target = clone({ reveal: level, zen: false, mic: st.mic, cfg: st.cfg });
        var room = this.bar.clientWidth - 24;
        if (style === "shelf" || (style === "automatic" && this.neededWidth(target) > room)) {
          this.toggleShelf(level === 2);
          return;
        }
      }
      st.shelf = null;
      st.reveal = level;
      this.say(level ? this.L("Hide Items") : this.L("Show Hidden Items"));
      this.armRehide();
      this.render();
    },
    toggleReveal: function (all) {
      var st = this.st;
      if (st.shelf) { st.shelf = null; this.render(); return; }
      if (all) this.setReveal(st.reveal === 2 ? 0 : 2);
      else this.setReveal(st.reveal > 0 ? 0 : 1);
    },
    toggleShelf: function (stash) {
      var st = this.st;
      if (st.shelf) st.shelf = null;
      else { st.shelf = { stash: !!stash }; st.reveal = 0; this.opening = ".mnd-shelf"; }
      this.render();
    },
    armRehide: function () {
      var self = this, st = this.st;
      clearTimeout(this.rehideTimer);
      if (!st.cfg.autoRehide || st.reveal === 0) return;
      this.rehideTimer = setTimeout(function tick() {
        // Items stay while one of their menus is open or the pointer is on the menu bar.
        if (st.reveal === 0) return;
        if (st.menu || st.drag || self.bar.matches(":hover")) { self.rehideTimer = setTimeout(tick, 1500); return; }
        st.reveal = 0;
        self.render();
      }, st.cfg.rehideDelay * 1000);
    },
    setZen: function (on) {
      var st = this.st;
      st.zen = on;
      st.shelf = null;
      if (on) st.reveal = 0;
      this.render();
    },
    applyScene: function (i) {
      this.markMoved();
      this.st.ord = clone(SCENES[i].ord);
      if (!this.st.cfg.stash) this.mergeStash();
      this.render();
    },
    markMoved: function () {
      var m = {};
      ITEMS.forEach(function (it) { m[it.id] = 1; });
      m["D:hidden"] = m["D:stash"] = m.MENO = 1;
      this.movedKeys = m;
    },
    move: function (id, sec) {
      var o = this.st.ord, from = this.sectionOf(id);
      if (from === sec || BY_ID[id].locked) return;
      o[from].splice(o[from].indexOf(id), 1);
      if (sec === "visible") o.visible.unshift(id); // next to the divider, where a ⌘-drag lands
      else o[sec].push(id);
      this.markMoved();
      this.say(this.name(id) + " · " + this.L(SECTIONS[sec][0]));
    },
    mergeStash: function () {
      var o = this.st.ord;
      o.hidden = o.stash.concat(o.hidden);
      o.stash = [];
    },
    // What the rules do now (AutomationController, simplified to the sample conditions).
    evaluateRules: function () {
      var st = this.st, self = this, prev = st.active;
      st.active = {};
      st.rules.forEach(function (r) {
        var met = r.cond.every(function (c) { return c === "mic" ? st.mic : c === "ext" ? st.ext : false; });
        if (r.on && !st.paused && met) st.active[r.id] = true;
      });
      st.rules.forEach(function (r) {
        var was = !!prev[r.id], now = !!st.active[r.id];
        if (was === now) return;
        if (r.action[0] === "zen") {
          if (now && !st.zen) { st.zen = true; st.reveal = 0; st.shelf = null; st.zenByRule = true; }
          else if (!now && r.undo && st.zenByRule) { st.zen = false; st.zenByRule = false; }
        } else if (r.action[0] === "scene" && now) {
          self.markMoved();
          st.ord = clone(SCENES[r.action[1]].ord);
          if (!st.cfg.stash) self.mergeStash();
        }
      });
    },

    onClick: function (e) {
      var t = e.target.closest ? e.target.closest("[data-act]") : null;
      if (this.suppressClick) { this.suppressClick = false; e.preventDefault(); return; }
      if (!t || !this.root.contains(t)) return;
      var act = t.getAttribute("data-act"), v = t.getAttribute("data-v"), st = this.st;
      var keyboard = e.detail === 0;
      if (t.classList.contains("is-dis") || t.getAttribute("aria-disabled") === "true") return;
      // Choosing a menu item closes the menu; any click outside an open menu closes it first, as on macOS.
      if (st.menu && t.closest(".mnd-menu") && act !== "m-sub") {
        this.focus(st.menu.owner);
        st.menu = null;
      } else if (st.menu && !t.closest(".mnd-menu")) {
        var owner = st.menu.owner;
        st.menu = null;
        if (t.getAttribute("data-k") === owner) { this.render(); return; }
      }
      switch (act) {
        case "meno":
          if (st.zen) { this.setZen(false); break; }
          if (e.altKey) this.toggleReveal(true);
          else this.toggleReveal(false);
          break;
        case "divider":
          if (st.zen) { this.setZen(false); break; }
          this.toggleReveal(false);
          break;
        case "empty":
          if (st.zen && st.cfg.zenBlocks) { this.render(); break; }
          if (st.cfg.emptyClick) this.toggleReveal(false); else this.render();
          break;
        case "desk":
          // Clicking elsewhere hides revealed items and closes the Shelf and Quick Open.
          if (st.quick) st.quick = null;
          if (st.shelf) st.shelf = null;
          if (st.reveal && st.cfg.rehideFocus && !st.win) st.reveal = 0;
          this.render();
          break;
        case "item":
          st.flash = v;
          this.openMenu("si-" + v, [{ t: this.name(v), header: 1 }, { note: 1, t: this.D("itemHint") }], { keyboard: keyboard });
          break;
        case "shelfitem":
          this.openMenu("sh-" + v, this.moveItems(v, true), { keyboard: keyboard });
          break;
        case "chip":
          this.openMenu("chip-" + v, this.chipItems(v), { keyboard: keyboard });
          break;
        case "popup":
          this.openMenu("pop-" + v, this.popupItems(v), { keyboard: keyboard, popup: true });
          break;
        case "rulemenu":
          this.openMenu("rm-" + v, [{ t: this.L("Edit…"), dis: 1 }, { t: this.L("Duplicate…"), dis: 1 }, { t: this.L("Delete"), act: "r-del", v: v }], { keyboard: keyboard });
          break;
        case "m-sub":
          if (st.menu) {
            var idx = +t.getAttribute("data-sub");
            st.menu.subOpen = st.menu.subOpen === idx && !keyboard ? undefined : idx;
            st.menu.focus = keyboard ? "mnd-m1-0" : t.getAttribute("data-mi");
          }
          this.render();
          break;
        case "quick":
          st.shelf = null;
          st.quick = { q: "", sel: 0 };
          this.opening = ".mnd-quick";
          this.focus("quick");
          this.render();
          break;
        case "arrange":
          st.shelf = null; st.quick = null;
          this.openPane("layout");
          break;
        case "m-toggle": this.focus("meno"); this.toggleReveal(false); break;
        case "m-all": this.focus("meno"); this.setReveal(2); break;
        case "m-shelf": this.focus("meno"); st.shelf = null; this.toggleShelf(false); break;
        case "m-zen":
          st.zenByRule = false;
          this.setZen(!st.zen);
          break;
        case "m-pause":
          st.paused = !st.paused;
          this.evaluateRules();
          this.render();
          break;
        case "m-scene": this.focus("meno"); this.applyScene(+v); break;
        case "m-pane": this.openPane(v); break;
        case "pane": st.win = v; this.focus("pane-" + v); this.render(); break;
        case "closewin": st.win = null; this.focus("meno"); this.render(); break;
        case "cfg":
          st.cfg[v] = !st.cfg[v];
          if (v === "stash") {
            if (!st.cfg.stash) this.mergeStash();
            if (st.reveal === 2 && !st.cfg.stash) st.reveal = 1;
            this.markMoved();
          }
          if (v === "autoRehide") this.armRehide();
          this.render();
          break;
        case "setcfg":
          var p = v.split(":");
          st.cfg[p[0]] = p[1];
          this.focus("pop-" + p[0]);
          this.render();
          break;
        case "relaunch":
          this.relaunch();
          break;
        case "i-open":
          st.shelf = null;
          var sec = this.sectionOf(v);
          st.reveal = Math.max(st.reveal, sec === "stash" ? 2 : sec === "hidden" ? 1 : 0);
          st.flash = v;
          this.render();
          this.openMenu("si-" + v, [{ t: this.name(v), header: 1 }, { note: 1, t: this.D("itemHint") }], { keyboard: keyboard });
          this.armRehide();
          break;
        case "i-move":
          var mv = v.split(":");
          this.move(mv[0], mv[1]);
          this.focus(st.win === "layout" ? "chip-" + mv[0] : "meno");
          this.render();
          break;
        case "i-step":
          var sp = v.split(":"), list = st.ord[this.sectionOf(sp[0])], i = list.indexOf(sp[0]), j = i + +sp[1];
          list.splice(i, 1); list.splice(j, 0, sp[0]);
          this.markMoved();
          this.focus("chip-" + sp[0]);
          this.render();
          break;
        case "qpick":
          st.quick.sel = +v;
          this.quickActivate();
          break;
        case "rule":
          st.rules.forEach(function (r) { if (r.id === v) r.on = !r.on; });
          this.evaluateRules();
          this.render();
          break;
        case "r-del":
          st.rules = st.rules.filter(function (r) { return r.id !== v; });
          this.evaluateRules();
          this.focus("pane-rules");
          this.render();
          break;
        case "sim":
          st[v] = !st[v];
          this.evaluateRules();
          this.render();
          break;
        default:
          this.render();
      }
    },
    openPane: function (pane) {
      var st = this.st;
      if (!st.win) this.opening = ".mnd-window";
      st.win = pane;
      st.shelf = null;
      this.focus("pane-" + pane);
      this.render();
    },
    relaunch: function () {
      var st = this.st, self = this, lang = st.cfg.language === "system" ? this.pageLang : st.cfg.language;
      this.launchLang = st.cfg.language;
      var win = this.screen.querySelector(".mnd-window");
      var go = function () {
        self.lang = lang;
        st.menu = null;
        self.focus("pop-language");
        self.opening = ".mnd-window";
        self.render();
      };
      if (win && !reduceMotion()) { win.classList.add("is-closing"); setTimeout(go, 260); } else go();
    },
    quickActivate: function () {
      var st = this.st, r = this.qres && this.qres[st.quick.sel];
      if (!r) return;
      st.quick = null;
      if (r.kind === "item") {
        var sec = this.sectionOf(r.id);
        st.zen = false;
        st.reveal = Math.max(st.reveal, sec === "stash" ? 2 : sec === "hidden" ? 1 : 0);
        st.flash = r.id;
        this.render();
        this.openMenu("si-" + r.id, [{ t: this.name(r.id), header: 1 }, { note: 1, t: this.D("itemHint") }], { keyboard: true });
        this.armRehide();
        return;
      }
      var id = r.id;
      if (id.indexOf("scene") === 0) this.applyScene(+id.slice(5));
      else if (id === "zen") this.setZen(!st.zen);
      else if (id === "show") this.setReveal(1);
      else if (id === "showall") this.setReveal(2);
      else if (id === "hide") this.setReveal(0);
      else if (id === "shelf") this.toggleShelf(false);
      else if (id === "arrange") this.openPane("layout");
      else if (id === "settings") this.openPane("general");
      this.focus("meno");
      this.render();
    },

    onContext: function (e) {
      var t = e.target.closest ? e.target.closest("[data-act]") : null;
      if (!t) return;
      var act = t.getAttribute("data-act");
      if (act === "meno" || act === "divider") {
        e.preventDefault();
        this.openMenu("meno", this.menoMenu(), { keyboard: false });
      } else if (act === "shelfitem" || act === "chip") {
        e.preventDefault();
        t.click();
      }
    },

    onInput: function (e) {
      var t = e.target, st = this.st;
      if (t.getAttribute("data-k") === "quick" && st.quick) {
        if (e.type !== "input") return;
        st.quick.q = t.value;
        st.quick.sel = 0;
        this.render();
      } else if (t.getAttribute("data-act") === "delay") {
        st.cfg.rehideDelay = +t.value;
        var out = t.parentNode.querySelector("output");
        if (out) out.textContent = this.secs(st.cfg.rehideDelay);
        t.setAttribute("aria-valuetext", this.secs(st.cfg.rehideDelay));
        if (e.type === "change") this.armRehide();
      }
    },

    onKey: function (e) {
      var st = this.st, t = e.target, k = e.key;
      if (st.menu) {
        var items = Array.prototype.slice.call(this.slots.menu.querySelectorAll(".mnd-mi:not(.is-dis)"));
        var inSub = t.closest && t.closest(".mnd-m1");
        var level = items.filter(function (b) { return !!b.closest(".mnd-m1") === !!inSub; });
        var i = level.indexOf(t);
        if (k === "ArrowDown" || k === "ArrowUp") {
          e.preventDefault();
          var n = level.length ? level[(i + (k === "ArrowDown" ? 1 : -1) + level.length + (i < 0 && k === "ArrowUp" ? 1 : 0)) % level.length] : null;
          if (n) { st.menu.focus = n.getAttribute("data-mi"); n.focus(); }
          return;
        }
        if (k === "ArrowRight" && t.getAttribute("data-sub")) { e.preventDefault(); t.click(); return; }
        if ((k === "ArrowLeft" || k === "Escape") && inSub) {
          e.preventDefault();
          var sub = st.menu.subOpen;
          st.menu.subOpen = undefined;
          st.menu.focus = "mnd-m0-" + sub;
          this.render();
          return;
        }
        if (k === "Escape" || k === "Tab") {
          e.preventDefault();
          this.closeMenu(true);
          return;
        }
        return;
      }
      if (st.quick) {
        var n2 = (this.qres || []).length;
        if (k === "ArrowDown" || k === "ArrowUp") {
          e.preventDefault();
          if (n2) st.quick.sel = (st.quick.sel + (k === "ArrowDown" ? 1 : -1) + n2) % n2;
          this.render();
          return;
        }
        if (k === "Enter" && t.getAttribute("data-k") === "quick") { e.preventDefault(); this.quickActivate(); return; }
        if ((e.metaKey || e.ctrlKey) && /^[1-9]$/.test(k)) { e.preventDefault(); st.quick.sel = +k - 1; this.quickActivate(); return; }
        if (k === "Escape") { e.preventDefault(); st.quick = null; this.focus("meno"); this.render(); return; }
      }
      if (k === "Escape") {
        if (st.shelf) { e.preventDefault(); st.shelf = null; this.focus("meno"); this.render(); return; }
        if (st.reveal) { e.preventDefault(); this.focus("meno"); this.setReveal(0); return; }
      }
      // The Meno icon: ↓, the context menu key or ⇧F10 open its menu, as a right-click does.
      if (t.getAttribute && t.getAttribute("data-k") === "meno" && (k === "ArrowDown" || k === "ContextMenu" || (k === "F10" && e.shiftKey))) {
        e.preventDefault();
        this.openMenu("meno", this.menoMenu(), { keyboard: true });
        return;
      }
      // ← → move between the Shelf's items, as in the app.
      if ((k === "ArrowLeft" || k === "ArrowRight") && t.closest && t.closest(".mnd-shelf")) {
        var bs = Array.prototype.slice.call(this.slots.shelf.querySelectorAll("button")), j = bs.indexOf(t);
        e.preventDefault();
        bs[(j + (k === "ArrowRight" ? 1 : -1) + bs.length) % bs.length].focus();
        return;
      }
      // ⌘1–⌘9 switch Settings panes.
      if (st.win && (e.metaKey || e.ctrlKey) && /^[0-9]$/.test(k) && this.root.contains(t) && t.closest(".mnd-window")) {
        e.preventDefault();
        var p = PANES[(+k + 9) % 10];
        this.st.win = p[0];
        this.focus("pane-" + p[0]);
        this.render();
      }
    },

    // ---------------------------------------------------------------- dragging in the menu bar
    onPointerDown: function (e) {
      var b = e.target.closest ? e.target.closest(".mnd-status [data-act=item]") : null;
      if (!b || e.button !== 0) return;
      var self = this, id = b.getAttribute("data-v"), el = this.els[id], x0 = e.clientX, y0 = e.clientY, started = false;
      var move = function (ev) {
        var dx = ev.clientX - x0;
        if (!started) {
          if (Math.abs(dx) < 5 && Math.abs(ev.clientY - y0) < 5) return;
          started = true;
          self.st.drag = id;
          if (self.st.menu) { self.st.menu = null; self.slots.menu.innerHTML = ""; }
          el.classList.add("is-dragging");
          self.screen.classList.add("is-dragging");
        }
        ev.preventDefault();
        el.style.transform = "translateX(" + dx + "px)";
        self.dropX = ev.clientX;
        self.markDrop(id, ev.clientX);
      };
      var up = function () {
        document.removeEventListener("pointermove", move);
        document.removeEventListener("pointerup", up);
        document.removeEventListener("pointercancel", up);
        if (!started) return;
        self.suppressClick = true;
        setTimeout(function () { self.suppressClick = false; }, 0);
        el.classList.remove("is-dragging");
        self.screen.classList.remove("is-dragging");
        self.st.drag = null;
        var before = el.getBoundingClientRect().left;
        el.style.transform = "";
        self.dropInBar(id, self.dropX);
        self.clearBarMarks();
        // Settle from where it was dropped.
        var after = el.getBoundingClientRect().left;
        if (el.animate && !reduceMotion()) el.animate([{ transform: "translateX(" + (before - after) + "px)" }, { transform: "none" }], { duration: 220, easing: "cubic-bezier(.2,.8,.2,1)" });
        self.armRehide();
      };
      document.addEventListener("pointermove", move);
      document.addEventListener("pointerup", up);
      document.addEventListener("pointercancel", up);
    },
    // The shown element the dragged item lands in front of, or null for the end.
    dropTarget: function (id, x) {
      var self = this, seq = this.sequence().filter(function (k) { return k !== id && self.shown(k) && k !== "MIC"; });
      var lockedAt = seq.indexOf("cc");
      for (var i = 0; i < seq.length; i++) {
        if (i >= lockedAt) return "cc";
        var r = this.els[seq[i]].getBoundingClientRect();
        if (x < r.left + r.width / 2) return seq[i];
      }
      return "cc";
    },
    markDrop: function (id, x) {
      var t = this.dropTarget(id, x);
      this.clearBarMarks();
      if (t) this.els[t].classList.add("is-dropbefore");
    },
    clearBarMarks: function () {
      var m = this.status.querySelectorAll(".is-dropbefore");
      for (var i = 0; i < m.length; i++) m[i].classList.remove("is-dropbefore");
    },
    dropInBar: function (id, x) {
      if (x === undefined) return;
      var st = this.st, target = this.dropTarget(id, x), seq = this.sequence().filter(function (k) { return k !== id; });
      seq.splice(seq.indexOf(target), 0, id);
      var ord = { stash: [], hidden: [], visible: [] }, sec = st.cfg.stash ? "stash" : "hidden", tail = false;
      seq.forEach(function (k) {
        if (k === "D:stash") { sec = "hidden"; return; }
        if (k === "D:hidden") { sec = "visible"; return; }
        if (k === "MENO") { tail = true; return; }
        if (!BY_ID[k] || BY_ID[k].locked) return;
        if (sec === "visible" && k === id) BY_ID[k].tail = tail;
        ord[sec].push(k);
      });
      // Right of the Meno icon an item stays visible; keep the tail items in their order.
      st.ord = ord;
      this.say(this.name(id) + " · " + this.L(SECTIONS[this.sectionOf(id)][0]));
      this.render();
    },

    // ---------------------------------------------------------------- dragging chips in the layout editor
    onDragStart: function (e) {
      var c = e.target.closest ? e.target.closest(".mnd-chip") : null;
      if (!c) return;
      this.chipDrag = c.getAttribute("data-v");
      if (this.st.menu) { this.st.menu = null; this.slots.menu.innerHTML = ""; }
      e.dataTransfer.effectAllowed = "move";
      try { e.dataTransfer.setData("text/plain", this.name(this.chipDrag)); } catch (err) { /* ignore */ }
      c.classList.add("is-lifted");
    },
    onDragOver: function (e) {
      if (!this.chipDrag) return;
      var lane = e.target.closest ? e.target.closest(".mnd-lane") : null;
      if (!lane) return;
      e.preventDefault();
      e.dataTransfer.dropEffect = "move";
      this.clearDrop();
      lane.classList.add("is-drop");
      var chip = e.target.closest(".mnd-chip");
      if (chip && chip.getAttribute("data-v") !== this.chipDrag && !BY_ID[chip.getAttribute("data-v")].locked) {
        var r = chip.getBoundingClientRect();
        chip.classList.add(e.clientX < r.left + r.width / 2 ? "is-edge-l" : "is-edge-r");
      }
    },
    onDragLeave: function (e) {
      var lane = e.target.closest ? e.target.closest(".mnd-lane") : null;
      if (lane && !lane.contains(e.relatedTarget)) lane.classList.remove("is-drop");
    },
    clearDrop: function () {
      var m = this.root.querySelectorAll(".is-drop, .is-edge-l, .is-edge-r, .is-lifted");
      for (var i = 0; i < m.length; i++) m[i].classList.remove("is-drop", "is-edge-l", "is-edge-r", "is-lifted");
    },
    onDrop: function (e) {
      var id = this.chipDrag;
      this.chipDrag = null;
      var lane = e.target.closest ? e.target.closest(".mnd-lane") : null;
      if (!id || !lane) { this.clearDrop(); return; }
      e.preventDefault();
      var sec = lane.getAttribute("data-lane"), o = this.st.ord, from = this.sectionOf(id);
      var chip = e.target.closest(".mnd-chip"), ref = chip ? chip.getAttribute("data-v") : null;
      o[from].splice(o[from].indexOf(id), 1);
      var list = o[sec], at = list.length;
      if (ref && ref !== id && list.indexOf(ref) >= 0) {
        var r = chip.getBoundingClientRect();
        at = list.indexOf(ref) + (e.clientX < r.left + r.width / 2 ? 0 : 1);
      }
      list.splice(at, 0, id);
      this.markMoved();
      this.clearDrop();
      this.say(this.name(id) + " · " + this.L(SECTIONS[sec][0]));
      this.focus("chip-" + id);
      this.render();
    }
  };

  function init() {
    Array.prototype.forEach.call(document.querySelectorAll("figure.mnd:not(.mnd-ready)"), function (el) {
      try { new Demo(el); } catch (err) { if (window.console) console.error(err); }
    });
  }
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", init);
  else init();
})();
