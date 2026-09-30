/* whrss.com: an interactive recreation of Pop — the ring and its result cards — on a pretend document.
   Everything here is sample text and canned results; nothing is fetched and nothing is sent anywhere.
   Layout, sizes and wording follow the Pop sources (RingMenuView, RingGeometry, Cards.swift —
   CardContainer, ResultCardView, ResultRowsView, TranslationCardView —, AICard, RegexTesterView,
   ClipboardHistoryView, PluginChooserView, UnitConverter, Motion, Glass) and its en / zh-Hans
   Localizable.strings.

   Markup: <figure class="ppd" data-lang="en|zh" data-preset="ring|translate|unit|json|regex|ai|history|actions"
            data-desk data-icon="…/pop.png">…fallback…</figure> */
(function () {
  "use strict";

  // ------------------------------------------------------------------ strings
  var S = {
    en: {
      demo: "Interactive demo · sample data",
      demoLabel: "Interactive demo of Pop, with sample text",
      docTitle: "Release Notes.txt",
      docHead: "Release notes",
      hintMouse: "Select some text above, then press and hold on it — or hold here",
      hintTouch: "Tap underlined text to open Pop — or tap here",
      holdLabel: "Open Pop for the selected text",
      snLabel: "Sample text: %s. Press Return to open Pop for it",
      ringLabel: "Pop ring. Arrow keys choose a slot, Return runs it, Esc closes",
      translate: "Translate", search: "Search", dictionary: "Dictionary", openLink: "Open Link",
      allActions: "All Actions", clipboard: "Clipboard", screenshotOCR: "Screenshot OCR", pickColor: "Pick Color",
      reading: "Reading…", nothing: "Nothing selected", notAvailable: "Not available for this content",
      needText: "Select text first", needLink: "Select a link first", nChars: "%s characters",
      kLink: "Link", kMeasure: "Measurement",
      close: "Close (Esc)", copy: "Copy", replace: "Replace", more: "More Actions", pin: "Pin to Screen", speak: "Speak",
      copyTr: "Copy Translation", to: "To %s", system: "System", deepl: "DeepL", compare: "Compare",
      translating: "Translating…", langHelp: "Translate into another language",
      engineHelp: "Switch translation engines, or compare several translations side by side",
      replaceHelp: "Replace the selected text with the translation (⌘↩)",
      pinHelp: "Pin the translation on top of everything to compare with the original",
      noSample: "This demo only has sample translations into %s.",
      copied: "Copied", copiedPlain: "Copied as plain text",
      rowCopy: "Copy", rowReplace: "Paste back into the app (replacing the selected text)",
      units: "Convert Units", detail: "%s: %s", length: "Length",
      u_cm: "Centimeters", u_m: "Meters", u_km: "Kilometers", u_in: "Inches", u_ft: "Feet", u_mi: "Miles",
      u_nmi: "Nautical miles", u_chi: "Chi (Chinese foot)", u_li: "Li (Chinese mile)", u_mm: "Millimeters", u_ftin: "Feet and inches",
      formatJSON: "Format JSON", copyMin: "Copy Minified",
      openDict: "Open in Dictionary", notFound: "“%s” wasn’t found in the system dictionaries. You can turn on more dictionaries in the Dictionary app’s settings.",
      stats: "Text Statistics", sChars: "Characters", sNoSpace: "Without spaces", sHan: "Chinese characters", sWords: "Words",
      sLines: "Lines", sBytes: "UTF-8 bytes", sRead: "Reading time", under1: "Under 1 minute", aboutMin: "About %s minutes",
      regex: "Regex Tester", nMatches: "%s matches", badRegex: "Invalid expression", regexPh: "Regular expression, e.g. \\d+",
      presets: "Presets", ignoreCase: "Ignore case", multiline: "^ $ match each line", dotAll: ". matches newlines",
      replacePh: "Replace with ($1 is the first group, $0 the whole match)", copyMatches: "Copy All Matches",
      copyExpr: "Copy Expression", copyReplaced: "Copy Replaced Text", empty: "(Empty)", noMatch: "(no match)",
      rp: ["Number", "Chinese", "English word", "Email", "Mobile number", "URL", "IP Address", "Date", "Blank line", "Leading/trailing spaces"],
      ai: "AI", aiActs: ["Polish", "Summarize", "Explain", "Translate"], askPh: "Ask about this text, press Return to send",
      aiIdle: "Choose a prompt or ask a question. The selected text is sent to the service set in Settings → AI.",
      thinking: "Thinking…", stop: "Stop", regen: "Regenerate",
      history: "Clipboard History", nItems: "%s items", searchPh: "Search",
      filters: ["All", "Text", "Image", "Files", "Pin"],
      hHint: "⏎ Paste · ⌘1–9 Quick paste · ⌘-click to select several · ⌘P Pin · ⌘⌫ Delete · Right-click for more",
      hMarked: "%s selected · ⏎ Paste together in order · ⌘C Copy together · Esc Cancel",
      noItems: "No matching items", imageSize: "Image · %s", imageHas: "Image contains “%s”",
      now: "now", minAgo: "%s minutes ago", minAgo1: "1 minute ago",
      chooser: "All Actions", chooserSub: "↑↓ Choose · ⏎ Run", chooserPh: "Search actions", noActions: "No matching actions",
      tSearch: "In Pop, this searches for the text in your browser",
      tLink: "In Pop, this opens the link in your browser",
      tOCR: "In Pop, you’d now drag a box on the screen",
      tColor: "In Pop, a loupe now follows the pointer to pick a color",
      tDict: "In Pop, this opens the Dictionary app",
      tNotInDemo: "Not in this demo — try it in Pop",
      tPasted: "Pasted",
      pinClose: "Close pinned text",
      mbLabel: "Menu bar", clock: "Wed Sep 30  16:14", app: "TextEdit", menus: ["File", "Edit", "Format", "View"],
      acts: {
        translate: ["Translate", "Translate the selected text with offline System Translation by default; switch to AI or DeepL on the card, or compare them"],
        search: ["Search", "Search the selected text in your default browser"],
        dictionary: ["Dictionary", "Look up the selected word or phrase in the system Dictionary"],
        units: ["Convert Units", "Convert length, weight, temperature, volume, area, speed, data size and data rate, including Chinese units such as jin and mu"],
        json: ["Format JSON", "Format or minify the selected JSON"],
        jsonTypes: ["JSON to Code", "Generate TypeScript, Swift, Go and Kotlin type definitions from the selected JSON"],
        openLink: ["Open Link", "Open the link in your browser, or write to the email address"],
        speak: ["Speak", "Read the selected text aloud with the system voice; use it again to stop"],
        ai: ["AI Assistant", "Ask about the selected text, or have AI polish, summarize, explain or translate it (set up the API in Settings → AI first)"],
        regex: ["Regex Tester", "Try regular expressions on the selected text: live highlighting of matches, groups and replacements"],
        stats: ["Text Statistics", "Count characters, Chinese characters, words and lines, and estimate reading time"],
        cleanup: ["Clean Up Text", "Join lines, remove blank lines and extra spaces, space Chinese and Latin text, full-width to half-width, Simplified ↔ Traditional Chinese, Pinyin, sort and deduplicate lines"],
        extract: ["Extract Info", "Find links, email addresses, phone numbers and IP addresses in text and copy them one by one or together"],
        plain: ["Copy as Plain Text", "Copy just the text to the clipboard, without formatting"],
        qr: ["QR Code", "Generate a QR code from text or a link (letters and digits can also become a barcode); with an image selected, read the QR codes and barcodes in it"],
        clipboard: ["Clipboard", "Open clipboard history and paste an item"],
        ocr: ["Screenshot OCR", "Select an area of the screen and recognize the text in it"],
        color: ["Pick Color", "Pick a color anywhere on the screen"]
      }
    },
    zh: {
      demo: "可交互演示 · 示例数据",
      demoLabel: "Pop 的可交互演示，使用示例文字",
      docTitle: "发布说明.txt",
      docHead: "发布说明",
      hintMouse: "先选中上面的一段文字，再按住它，或者按住这里",
      hintTouch: "点一下带下划线的文字打开 Pop，或者点这里",
      holdLabel: "为选中的文字打开 Pop",
      snLabel: "示例文字：%s。按回车为它打开 Pop",
      ringLabel: "Pop 圆盘。方向键选择格子，回车执行，Esc 关闭",
      translate: "翻译", search: "搜索", dictionary: "词典", openLink: "打开链接",
      allActions: "全部功能", clipboard: "剪贴板", screenshotOCR: "截图识字", pickColor: "屏幕取色",
      reading: "读取中…", nothing: "未选中内容", notAvailable: "当前内容用不了",
      needText: "要先选中文字", needLink: "要先选中链接", nChars: "%s 字",
      kLink: "链接", kMeasure: "带单位的数值",
      close: "关闭（Esc）", copy: "复制", replace: "替换原文", more: "更多功能", pin: "贴到屏幕", speak: "朗读",
      copyTr: "复制译文", to: "译成%s", system: "系统", deepl: "DeepL", compare: "对比",
      translating: "翻译中…", langHelp: "换一种语言重新翻译",
      engineHelp: "换一个翻译引擎，或者把几家的译文放在一起对比",
      replaceHelp: "用译文替换选中的文字（⌘↩）",
      pinHelp: "把译文贴在屏幕最前面，边看原文边对照",
      noSample: "这个演示只准备了译成%s的示例译文。",
      copied: "已复制", copiedPlain: "已复制纯文本",
      rowCopy: "复制", rowReplace: "粘贴回原来的 App（替换选中的文字）",
      units: "单位换算", detail: "%s：%s", length: "长度",
      u_cm: "厘米", u_m: "米", u_km: "千米", u_in: "英寸", u_ft: "英尺", u_mi: "英里",
      u_nmi: "海里", u_chi: "尺（市尺）", u_li: "里（市里）", u_mm: "毫米", u_ftin: "英尺英寸",
      formatJSON: "JSON 格式化", copyMin: "复制压缩版",
      openDict: "在词典中打开", notFound: "系统词典里没有找到「%s」。可以在「词典」App 的设置里启用更多词典。",
      stats: "字数统计", sChars: "字符", sNoSpace: "不含空白", sHan: "汉字", sWords: "词",
      sLines: "行", sBytes: "UTF-8 字节", sRead: "阅读时间", under1: "不到 1 分钟", aboutMin: "约 %s 分钟",
      regex: "正则测试", nMatches: "%s 处匹配", badRegex: "表达式有误", regexPh: "正则表达式，比如 \\d+",
      presets: "常用", ignoreCase: "忽略大小写", multiline: "^ $ 匹配每一行", dotAll: ". 也匹配换行",
      replacePh: "替换为（$1 是第一个分组，$0 是整个匹配）", copyMatches: "复制所有匹配",
      copyExpr: "复制表达式", copyReplaced: "复制替换结果", empty: "（空）", noMatch: "（未参与）",
      rp: ["数字", "中文", "英文单词", "邮箱", "手机号", "网址", "IP 地址", "日期", "空行", "行首尾空白"],
      ai: "AI", aiActs: ["润色", "总结", "解释", "翻译"], askPh: "就这段文字提问，回车发送",
      aiIdle: "选一个指令，或者直接提问。选中的文字会发给「设置 → AI」里填写的服务。",
      thinking: "思考中…", stop: "停止", regen: "重新生成",
      history: "剪贴板历史", nItems: "%s 条", searchPh: "搜索",
      filters: ["全部", "文字", "图片", "文件", "固定"],
      hHint: "⏎ 粘贴 · ⌘1–9 快速粘贴 · ⌘ 点选多条 · ⌘P 固定 · ⌘⌫ 删除 · 右键更多",
      hMarked: "已选 %s 条 · ⏎ 按顺序合在一起粘贴 · ⌘C 合在一起复制 · Esc 取消",
      noItems: "没有匹配的记录", imageSize: "图片 · %s", imageHas: "图里有「%s」",
      now: "现在", minAgo: "%s分钟前", minAgo1: "1分钟前",
      chooser: "全部功能", chooserSub: "↑↓ 选择 · ⏎ 执行", chooserPh: "搜索功能，比如 fy 找到翻译", noActions: "没有匹配的功能",
      tSearch: "在 Pop 里，这会用浏览器搜索这段文字",
      tLink: "在 Pop 里，这会用浏览器打开链接",
      tOCR: "在 Pop 里，这时可以在屏幕上框选一块区域",
      tColor: "在 Pop 里，这时会出现放大镜，点一下取色",
      tDict: "在 Pop 里，这会打开「词典」App",
      tNotInDemo: "这个演示里没有，去 Pop 里试试",
      tPasted: "已粘贴",
      pinClose: "关闭贴在屏幕上的文字",
      mbLabel: "菜单栏", clock: "9月30日 周三 16:14", app: "文本编辑", menus: ["文件", "编辑", "格式", "显示"],
      acts: {
        translate: ["翻译", "翻译选中的文字：默认用系统离线翻译，卡片上可以换成 AI 或 DeepL，或者几家一起对比"],
        search: ["搜索", "用默认浏览器搜索选中的文字"],
        dictionary: ["词典", "用系统「词典」查询选中的单词或词语"],
        units: ["单位换算", "长度、重量、温度、体积、面积、速度、数据大小和传输速率互相换算，认得斤、亩等市制单位"],
        json: ["JSON 格式化", "格式化或压缩选中的 JSON"],
        jsonTypes: ["JSON 转代码", "根据选中的 JSON 生成 TypeScript、Swift、Go、Kotlin 的类型定义"],
        openLink: ["打开链接", "在浏览器中打开链接，或给邮箱写邮件"],
        speak: ["朗读", "用系统语音朗读选中的文字，朗读中再用一次就停止"],
        ai: ["AI 助手", "就选中的文字提问，或者让 AI 润色、总结、解释、翻译（先在「设置 → AI」里填写接口）"],
        regex: ["正则测试", "在选中的文字里试正则表达式：实时标出每处匹配、列出分组，也可以试替换"],
        stats: ["字数统计", "统计字符、汉字、单词、行数和阅读时间"],
        cleanup: ["文字整理", "合并换行、去掉空行和多余空格、中英文之间加空格、全角转半角、简繁转换、拼音、按行排序去重"],
        extract: ["提取信息", "从一段文字里找出链接、邮箱、电话号码和 IP 地址，逐个复制或者一起复制"],
        plain: ["纯文本复制", "去掉格式，只把文字复制到剪贴板"],
        qr: ["二维码", "把文字或链接生成二维码（英文字母和数字还能生成条形码）；选中图片时识别里面的二维码和条形码"],
        clipboard: ["剪贴板", "打开剪贴板历史，选一条粘贴"],
        ocr: ["截图识字", "框选屏幕上的一块区域，识别里面的文字"],
        color: ["屏幕取色", "拾取屏幕上任意位置的颜色"]
      }
    }
  };

  // ------------------------------------------------------------------ sample text
  // The document: runs of plain text and selectable snippets {id: text}.
  var JSON_SAMPLE = '{"app": "Pop", "slots": 8, "glass": true, "tags": ["ring", "ocr"]}';
  var LINK = "https://github.com/whrss9527/pop";
  var DOC = {
    en: [
      [["a", "Hold the right mouse button on anything you’ve selected, and Pop opens a ring of tools."]],
      ["From the Paris office: ", ["b", "Le verre liquide reflète et réfracte ce qui se trouve derrière lui, si bien que chaque contrôle semble vivant."]],
      ["Launch-day run: ", ["c", "5 km"], " along the river."],
      ["Settings export: ", ["d", JSON_SAMPLE]],
      [["e", "0.10.0 shipped on 2026-09-29, 0.9.0 on 2026-09-28. The next release is planned before 2026-10-08."]],
      ["Download: ", ["f", LINK]],
      ["Word of the day: ", ["g", "refraction"]]
    ],
    zh: [
      [["a", "在选中的内容上按住鼠标右键，Pop 就会打开一个工具圆盘。"]],
      ["设计组的留言：", ["b", "Liquid glass reflects and refracts what is behind it, so every control feels alive."]],
      ["发布当天晨跑 ", ["c", "5 km"], "，沿着河边。"],
      ["导出的设置：", ["d", JSON_SAMPLE]],
      [["e", "0.10.0 发布于 2026-09-29，0.9.0 发布于 2026-09-28。下一版计划在 2026-10-08 之前发布。"]],
      ["下载：", ["f", LINK]],
      ["今日一词：", ["g", "折射"]]
    ]
  };

  var LANGS = [["zh-Hans", "简体中文"], ["zh-Hant", "繁體中文"], ["en", "English"], ["ja", "日本語"], ["ko", "한국어"],
    ["fr", "Français"], ["de", "Deutsch"], ["es", "Español"], ["it", "Italiano"], ["pt", "Português"], ["ru", "Русский"]];
  function langName(id) {
    for (var i = 0; i < LANGS.length; i++) if (LANGS[i][0] === id) return LANGS[i][1];
    return id;
  }

  // The glass sentence in every target language; the app's three engines differ where it matters.
  var GLASS = {
    "zh-Hans": { system: "液态玻璃会反射和折射其后方的内容，让每个控件都显得生动。",
      ai: "液态玻璃会映出并折射身后的内容，让每个控件都显得生动。",
      deepl: "液态玻璃反射和折射其背后的东西，因此每个控件都感觉栩栩如生。" },
    "zh-Hant": "液態玻璃會反射並折射其後方的內容，讓每個控制項都顯得生動。",
    en: { system: "Liquid glass reflects and refracts what is behind it, so that each control seems alive.",
      ai: "Liquid glass reflects and refracts whatever sits behind it, so every control feels alive.",
      deepl: "Liquid glass reflects and refracts what lies behind it, making every control feel alive." },
    ja: "リキッドグラスは背後にあるものを映し込み、屈折させるので、どのコントロールも生き生きと感じられます。",
    ko: "리퀴드 글래스는 뒤에 있는 것을 반사하고 굴절시켜 모든 컨트롤이 살아 있는 것처럼 느껴집니다.",
    fr: "Le verre liquide reflète et réfracte ce qui se trouve derrière lui, si bien que chaque contrôle semble vivant.",
    de: "Flüssiges Glas spiegelt und bricht, was dahinter liegt, sodass sich jedes Bedienelement lebendig anfühlt.",
    es: "El vidrio líquido refleja y refracta lo que hay detrás, de modo que cada control parece vivo.",
    it: "Il vetro liquido riflette e rifrange ciò che si trova dietro, così ogni controllo sembra vivo.",
    pt: "O vidro líquido reflete e refrata o que está atrás dele, e assim cada controle parece vivo.",
    ru: "Жидкое стекло отражает и преломляет то, что находится за ним, поэтому каждый элемент управления кажется живым."
  };
  // Other snippets: sample translations into the page's "other" language only.
  var TR = {
    en: {
      a: { "zh-Hans": { system: "在你选中的任何内容上按住鼠标右键，Pop 就会打开一个工具圆盘。", ai: "在选中的任何内容上按住鼠标右键，Pop 就会弹出一圈工具。", deepl: "在所选内容上按住鼠标右键，Pop 就会打开一个工具环。" } },
      e: { "zh-Hans": "0.10.0 于 2026-09-29 发布，0.9.0 于 2026-09-28 发布。下一版计划在 2026-10-08 之前发布。" },
      g: { "zh-Hans": "折射" },
      c: { "zh-Hans": "5 公里" }
    },
    zh: {
      a: { en: { system: "Hold the right mouse button on the selected content, and Pop opens a tool ring.", ai: "Hold the right mouse button on whatever you’ve selected and Pop opens a ring of tools.", deepl: "Press and hold the right mouse button on the selection and Pop will open a tool dial." } },
      e: { en: "0.10.0 was released on 2026-09-29 and 0.9.0 on 2026-09-28. The next version is planned before 2026-10-08." },
      g: { en: "refraction" },
      c: { en: "5 km" }
    }
  };

  var DICT = {
    refraction: "re·frac·tion | rɪˈfrakʃ(ə)n |\nnoun\nthe bending of light, sound or another wave as it passes at an angle from one medium into another, as from air into water or glass: the refraction of light by a prism.\nDERIVATIVES refractive adjective",
    "折射": "折射 | zhéshè\n动词\n1. 光线、声波等从一种介质斜着进入另一种介质时，传播方向发生偏折：阳光穿过玻璃杯，在桌上折射出一道彩虹。\n2. 比喻把事物的表象或实质间接地表现出来：这部小说折射出一个时代的变迁。"
  };

  // Canned AI answers per snippet: [polish, summarize, explain, translate].
  var AI = {
    en: {
      a: ["Hold the right mouse button on anything you’ve selected and Pop opens a ring of tools around the pointer.",
        "Long-press the right mouse button on a selection to open Pop’s tool ring.",
        "It describes Pop’s main gesture: select something, then keep the **right mouse button** pressed for a moment. Instead of the usual context menu, Pop shows a ring of tools around the pointer, and you pick one by moving toward it.",
        "在你选中的任何内容上按住鼠标右键，Pop 就会在指针周围打开一圈工具。"],
      b: ["Le verre liquide reflète et réfracte ce qui se trouve derrière lui : chaque contrôle semble ainsi vivant.",
        "Liquid glass reflects and bends what’s behind it, so controls feel alive.",
        "This French sentence says that **liquid glass** — a see-through interface material — both reflects and refracts the content behind it, which makes every control look alive rather than flat.",
        "Liquid glass reflects and refracts whatever sits behind it, so every control feels alive."],
      c: ["5 km", "Five kilometers.", "**5 km** is five kilometers: 5,000 meters, or about 3.1 miles — a common distance for a short race.", "5 公里"],
      d: ['{"app": "Pop", "glass": true, "slots": 8, "tags": ["ring", "ocr"]}',
        "Pop settings: 8 ring slots, glass on, tagged “ring” and “ocr”.",
        "A small JSON object with four keys: `app` is the string \"Pop\", `slots` is the number 8, `glass` is `true`, and `tags` is a list of two strings, \"ring\" and \"ocr\".",
        '{"app": "Pop", "slots": 8, "glass": true, "tags": ["圆盘", "文字识别"]}'],
      e: ["Version 0.10.0 shipped on 2026-09-29 and 0.9.0 on 2026-09-28; the next release is planned for before 2026-10-08.",
        "Two releases a day apart; the next one is due by October 8, 2026.",
        "It lists two release dates one day apart — 0.9.0 on **September 28** and 0.10.0 on **September 29, 2026** — and says the next version should come out before **October 8, 2026**.",
        "0.10.0 于 2026-09-29 发布，0.9.0 于 2026-09-28 发布。下一版计划在 2026-10-08 之前发布。"],
      f: [LINK, "Pop’s GitHub repository.", "This is Pop’s page on **GitHub**, where its source code, releases and issue tracker live.", LINK],
      g: ["refraction", "Light bending between materials.",
        "**Refraction** is the bending of a wave, such as light, when it passes from one material into another — it’s why a straw looks broken in a glass of water.", "折射"],
      other: "Here Pop streams the answer from the AI service you set up in Settings → AI. (This demo shows sample answers only.)",
      ask: "This is a sample answer: the demo doesn’t send your question anywhere. In Pop, your question and the selected text go to the AI service you set up — Apple’s on-device model or any OpenAI-compatible endpoint — and the answer streams in here."
    },
    zh: {
      a: ["在选中的内容上按住鼠标右键，Pop 就会在指针周围弹出一个工具圆盘。",
        "长按右键打开 Pop 的工具圆盘。",
        "这句话说的是 Pop 的核心手势：先选中内容，再**按住鼠标右键**停一下。Pop 不会弹出平常的右键菜单，而是在指针周围打开一圈工具，朝哪个方向一划就选中哪一个。",
        "Hold the right mouse button on whatever you’ve selected and Pop opens a ring of tools."],
      b: ["Liquid glass reflects and refracts whatever lies behind it, making every control feel alive.",
        "液态玻璃映出并折射身后的内容，让控件显得生动。",
        "这句英文的意思是：**液态玻璃**这种半透明的界面材质，会反射并折射它后面的内容，所以每个控件看起来都是活的，而不是平平的一块。",
        "液态玻璃会映出并折射身后的内容，让每个控件都显得生动。"],
      c: ["5 km", "五公里。", "**5 km** 就是 5 千米，也就是 5000 米，约合 3.1 英里，是短距离跑步常见的距离。", "5 km"],
      d: ['{"app": "Pop", "glass": true, "slots": 8, "tags": ["ring", "ocr"]}',
        "Pop 的设置：圆盘 8 格，开启玻璃效果，标签是 ring 和 ocr。",
        "这是一个有四个键的 JSON 对象：`app` 是字符串 \"Pop\"，`slots` 是数字 8，`glass` 是 `true`，`tags` 是两个字符串组成的列表：\"ring\" 和 \"ocr\"。",
        '{"app": "Pop", "slots": 8, "glass": true, "tags": ["ring", "ocr"]}'],
      e: ["0.10.0 于 2026-09-29 发布，0.9.0 于 2026-09-28 发布；下一版计划在 2026-10-08 之前推出。",
        "两个版本相隔一天发布，下一版 10 月 8 日前推出。",
        "这里列了两个版本的发布日期，相隔一天：0.9.0 在 **2026 年 9 月 28 日**，0.10.0 在 **9 月 29 日**；下一版计划在 **10 月 8 日**之前发布。",
        "0.10.0 was released on 2026-09-29 and 0.9.0 on 2026-09-28. The next version is planned before 2026-10-08."],
      f: [LINK, "Pop 的 GitHub 仓库。", "这是 Pop 在 **GitHub** 上的页面，源代码、发布版本和问题反馈都在这里。", LINK],
      g: ["折射", "光在两种介质之间偏折。", "**折射**是光、声波等从一种介质斜着进入另一种介质时，传播方向发生偏折的现象。插在水杯里的吸管看起来像折断了，就是折射造成的。", "refraction"],
      other: "在 Pop 里，回答会从你在「设置 → AI」里填写的服务流式输出。（这个演示只显示示例回答。）",
      ask: "这是示例回答：这个演示不会把你的问题发到任何地方。在 Pop 里，问题和选中的文字会发给你设置的 AI 服务（系统自带的本机模型，或任何兼容 OpenAI 的接口），回答会在这里流式显示。"
    }
  };

  var HISTORY = {
    en: [
      [2, "text", "Hold right-click to open the ring, release to run"],
      [3, "text", "pop@example.com"],
      [5, "text", "Meeting moved to Friday at 3 pm"],
      [6, "text", "https://github.com/whrss9527/pop/releases"],
      [8, "text", "SELECT * FROM orders WHERE id IN (1001, 1002, 1003);"],
      [14, "image", "Pop 0.32 release notes", "1.2 MB", true],
      [27, "files", "Invoice-0930.pdf"]
    ],
    zh: [
      [2, "text", "长按右键唤起圆盘，松开就执行"],
      [3, "text", "pop@example.com"],
      [5, "text", "会议改到周五下午三点"],
      [6, "text", "https://github.com/whrss9527/pop/releases"],
      [8, "text", "SELECT * FROM orders WHERE id IN (1001, 1002, 1003);"],
      [14, "image", "Pop 0.32 发布说明", "1.2 MB", true],
      [27, "files", "发票-0930.pdf"]
    ]
  };

  var REGEX_PRESETS = ["-?\\d+(?:\\.\\d+)?", "\\p{Script=Han}+", "\\b[A-Za-z]+(?:'[A-Za-z]+)?\\b", "[\\w.%+-]+@[\\w-]+(?:\\.[\\w-]+)+",
    "(?<!\\d)1[3-9]\\d{9}(?!\\d)", "https?://[^\\s\"'<>，。）]+", "\\b(?:\\d{1,3}\\.){3}\\d{1,3}\\b",
    "(?<year>\\d{4})[-/.](?<month>\\d{1,2})[-/.](?<day>\\d{1,2})", "^[ \\t]*$\\n?", "^[ \\t]+|[ \\t]+$"];

  // ------------------------------------------------------------------ icons (SF Symbols, redrawn)
  function svg(body, fill) {
    return '<svg viewBox="0 0 24 24" aria-hidden="true" fill="' + (fill ? "currentColor" : "none") +
      '" stroke="' + (fill ? "none" : "currentColor") + '" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round">' + body + "</svg>";
  }
  var I = {
    translate: svg('<path d="M5.5 3.8h13a2.3 2.3 0 0 1 2.3 2.3v8.6a2.3 2.3 0 0 1-2.3 2.3H13l-4.2 3.4v-3.4H5.5a2.3 2.3 0 0 1-2.3-2.3V6.1a2.3 2.3 0 0 1 2.3-2.3Z"/><path d="m9.2 13.6 2.8-6.6 2.8 6.6M10.2 11.4h3.6"/>'),
    search: svg('<circle cx="10.3" cy="10.3" r="6.3"/><path d="m15 15 5.3 5.3" stroke-width="2.1"/>'),
    dictionary: svg('<path d="M6.6 3h11.6c.6 0 1 .4 1 1v16.2c0 .5-.4.8-.8.8H6.8A2.6 2.6 0 0 1 4.2 18.4V5.4A2.4 2.4 0 0 1 6.6 3Z"/><path d="M4.2 18.4a2.5 2.5 0 0 1 2.5-2.4h12.5"/><path d="m9.4 12.6 2.6-6.1 2.6 6.1M10.3 10.6h3.4"/>'),
    openLink: svg('<circle cx="12" cy="12" r="8.6"/><path d="m15.6 8.4-2.1 5.1-5.1 2.1 2.1-5.1Z"/>'),
    allActions: svg('<rect x="3.8" y="3.8" width="6.8" height="6.8" rx="1.6"/><rect x="13.4" y="3.8" width="6.8" height="6.8" rx="1.6"/><rect x="3.8" y="13.4" width="6.8" height="6.8" rx="1.6"/><rect x="13.4" y="13.4" width="6.8" height="6.8" rx="1.6"/>'),
    clipboard: svg('<path d="M8.6 4.6H7a2 2 0 0 0-2 2V19a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2V6.6a2 2 0 0 0-2-2h-1.6"/><rect x="8.6" y="3" width="6.8" height="3.4" rx="1.2"/><path d="M8.6 10.6h.1M11 10.6h4.4M8.6 13.8h.1M11 13.8h4.4M8.6 17h.1M11 17h4.4"/>'),
    screenshotOCR: svg('<path d="M3.8 8.6V6.2a2.4 2.4 0 0 1 2.4-2.4h2.4M15.4 3.8h2.4a2.4 2.4 0 0 1 2.4 2.4v2.4M20.2 15.4v2.4a2.4 2.4 0 0 1-2.4 2.4h-2.4M8.6 20.2H6.2a2.4 2.4 0 0 1-2.4-2.4v-2.4"/>'),
    pickColor: svg('<path d="m13.3 6.4 4.3 4.3"/><path d="M15.6 4.1 17 2.7a2.1 2.1 0 0 1 3 3l-1.4 1.4-1.3 1.3-4.3-4.3Z" fill="currentColor"/><path d="m14.4 7.5-8.8 8.8-.9 3.1-1.2 1.2M16.5 9.6l-8.8 8.8-3 .9"/>'),
    ai: svg('<path d="M10 3.6 11.7 8l4.4 1.7-4.4 1.7L10 15.8l-1.7-4.4L3.9 9.7 8.3 8Z"/><path d="m17.4 13.4.9 2.3 2.3.9-2.3.9-.9 2.3-.9-2.3-2.3-.9 2.3-.9Z"/>'),
    units: svg('<path d="M3.5 15.6 15.6 3.5l4.9 4.9L8.4 20.5Z"/><path d="m7.4 11.7 1.8 1.8M9.9 9.2l1.2 1.2M12.3 6.8l1.8 1.8M14.8 4.3l1.2 1.2"/>'),
    json: svg('<path d="M8.5 3.8c-1.9 0-2.4 1-2.4 2.8v2.2c0 1.6-.8 2.9-2.3 3.2 1.5.3 2.3 1.6 2.3 3.2v2.2c0 1.8.5 2.8 2.4 2.8M15.5 3.8c1.9 0 2.4 1 2.4 2.8v2.2c0 1.6.8 2.9 2.3 3.2-1.5.3-2.3 1.6-2.3 3.2v2.2c0 1.8-.5 2.8-2.4 2.8"/>'),
    jsonTypes: svg('<rect x="3.4" y="3.4" width="17.2" height="17.2" rx="3.6"/><path d="M10 7.6c-1 0-1.3.5-1.3 1.4v1.4c0 .8-.4 1.4-1.1 1.6.7.2 1.1.8 1.1 1.6v1.4c0 .9.3 1.4 1.3 1.4M14 7.6c1 0 1.3.5 1.3 1.4v1.4c0 .8.4 1.4 1.1 1.6-.7.2-1.1.8-1.1 1.6v1.4c0 .9-.3 1.4-1.3 1.4"/>'),
    regex: svg('<circle cx="12" cy="12" r="8.6"/><path d="M12 7.4v9.2M8 9.7l8 4.6M16 9.7l-8 4.6"/>'),
    stats: svg('<path d="M9.4 4 7.6 20M16.4 4l-1.8 16M4.6 9h15.6M3.8 15h15.6"/>'),
    speak: svg('<path d="M4 9.4h3.2L11.6 5v14l-4.4-4.4H4Z"/><path d="M15 9a4.2 4.2 0 0 1 0 6M17.8 6.4a8 8 0 0 1 0 11.2"/>'),
    cleanup: svg('<path d="M4 6h16M4 10h10M4 14h16M4 18h10"/>'),
    extract: svg('<path d="M4 6h16M4 10h7M4 14h5M4 18h6"/><circle cx="16" cy="14" r="3.4"/><path d="m18.5 16.5 2.3 2.3"/>'),
    plain: svg('<path d="M9 4.6H7.4a2 2 0 0 0-2 2V19a2 2 0 0 0 2 2h9.2a2 2 0 0 0 2-2V6.6a2 2 0 0 0-2-2H15"/><rect x="9" y="3" width="6" height="3.2" rx="1.1"/><path d="M9.4 11h5.2M9.4 14.2h5.2M9.4 17.4h3.2"/>'),
    qr: svg('<rect x="3.8" y="3.8" width="6.4" height="6.4" rx="1"/><rect x="13.8" y="3.8" width="6.4" height="6.4" rx="1"/><rect x="3.8" y="13.8" width="6.4" height="6.4" rx="1"/><path d="M13.8 13.8h2.6v2.6h-2.6zM17.6 17.6h2.6v2.6h-2.6zM13.8 18.8v1.4M18.8 13.8h1.4"/>'),
    close: '<svg viewBox="0 0 16 16" aria-hidden="true"><circle cx="8" cy="8" r="7" fill="currentColor"/><path d="m5.6 5.6 4.8 4.8m0-4.8-4.8 4.8" stroke="var(--pp-xmark)" stroke-width="1.5" stroke-linecap="round"/></svg>',
    copy: svg('<rect x="8.4" y="8.4" width="11.2" height="12.4" rx="2"/><path d="M15.6 8.4V5.6a2 2 0 0 0-2-2H6.4a2 2 0 0 0-2 2v8.8a2 2 0 0 0 2 2h2"/>'),
    back: svg('<path d="M9.4 14.2 4.6 9.4l4.8-4.8"/><path d="M4.6 9.4h10a5.2 5.2 0 0 1 0 10.4h-3"/>'),
    chev: '<svg viewBox="0 0 10 10" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="m2.5 3.8 2.5 2.5 2.5-2.5"/></svg>',
    pinFill: svg('<path d="M9 3h6l-1 6 3.5 3.5V14h-11v-1.5L10 9Z"/><path d="M12 14v7" stroke="currentColor" stroke-width="1.8"/>', true),
    doc: svg('<path d="M6.5 3h7.4L18.6 7.7V19.4a1.6 1.6 0 0 1-1.6 1.6H6.5a1.6 1.6 0 0 1-1.6-1.6V4.6A1.6 1.6 0 0 1 6.5 3Z"/><path d="M13.6 3v4.8h4.8"/>'),
    hold: '<svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"><rect x="6" y="2.8" width="12" height="18.4" rx="6"/><path d="M12 2.8v6.6M6 9.4h12"/><path d="M12.2 3.2h4.6a.6.6 0 0 1 .6.6V9h-5.2Z" fill="currentColor" stroke="none"/></svg>'
  };

  // ------------------------------------------------------------------ helpers
  function esc(s) {
    return String(s).replace(/[&<>"']/g, function (c) { return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]; });
  }
  function fmt(s) {
    var args = Array.prototype.slice.call(arguments, 1), i = 0;
    return s.replace(/%s/g, function () { return args[i++]; });
  }
  function clamp(v, lo, hi) { return Math.max(lo, Math.min(hi, v)); }
  function chars(t) { return Array.from ? Array.from(t).length : t.length; }
  function reduced() {
    return !!(window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches);
  }
  function touchFirst() {
    return !!(window.matchMedia && window.matchMedia("(hover: none)").matches);
  }
  // A tiny inline Markdown for AI answers: **bold** and `code`, as the app's AIOutputText shows them.
  function md(t) {
    return esc(t).replace(/\*\*([^*]+)\*\*/g, "<strong>$1</strong>").replace(/`([^`]+)`/g, "<code>$1</code>");
  }

  // Ring geometry, from RingGeometry: 8 slots, inner radius 38, outer 124.
  var G = { n: 8, inner: 38, outer: 124 };
  G.label = (G.inner + G.outer) / 2;
  G.step = 360 / G.n;
  G.hl = Math.max(Math.min(2 * G.label * Math.sin(Math.PI / G.n) * 0.47, (G.outer - G.inner) / 2 - 4), 12);
  G.arc = Math.min(G.step * 0.62, 42);
  G.hub = G.inner * 2 - 4;
  function slotAt(dx, dy) {  // dy grows downward
    if (Math.sqrt(dx * dx + dy * dy) < G.inner) return null;
    var theta = Math.atan2(dx, -dy) * 180 / Math.PI;  // 0 at the top, clockwise
    if (theta < 0) theta += 360;
    return Math.floor((theta + G.step / 2) / G.step) % G.n;
  }

  // Length units, from UnitConverter (meters per unit).
  var UNITS = [["mm", "mm", 0.001], ["cm", "cm", 0.01], ["m", "m", 1], ["km", "km", 1000], ["in", "in", 0.0254],
    ["ft", "ft", 0.3048], ["mi", "mi", 1609.344], ["nmi", "nmi", 1852], ["chi", "尺", 1 / 3], ["li", "里", 500]];
  var ALIASES = { mm: "mm", "毫米": "mm", cm: "cm", "厘米": "cm", "公分": "cm", m: "m", "米": "m", meter: "m", meters: "m",
    km: "km", "千米": "km", "公里": "km", kilometer: "km", kilometers: "km", "in": "in", inch: "in", inches: "in", "英寸": "in",
    ft: "ft", foot: "ft", feet: "ft", "英尺": "ft", mi: "mi", mile: "mi", miles: "mi", "英里": "mi", nmi: "nmi", "海里": "nmi",
    "尺": "chi", "市尺": "chi", "里": "li", "市里": "li" };
  function parseQuantity(t) {
    var m = /^\s*(-?[\d,]*\.?\d+)\s*([A-Za-z一-鿿]+)\s*$/.exec(t);
    if (!m) return null;
    var id = ALIASES[m[2].toLowerCase()] || ALIASES[m[2]];
    if (!id) return null;
    var v = parseFloat(m[1].replace(/,/g, ""));
    return isFinite(v) ? { value: v, unit: id } : null;
  }
  function unitOf(id) { for (var i = 0; i < UNITS.length; i++) if (UNITS[i][0] === id) return UNITS[i]; return null; }
  function num6(v) {  // at most 6 significant digits, with thousands separators (en_US), like UnitConverter.format
    if (Math.abs(v) < 1e-12) return "0";
    var s = Number(v.toPrecision(6));
    return s.toLocaleString("en-US", { maximumFractionDigits: 20 });
  }
  function unitDisplay(v, u) {
    var tight = u[1].charCodeAt(0) >= 0x2e80;
    return num6(v) + (tight ? "" : " ") + u[1];
  }

  // JSONSerialization with .prettyPrinted and .sortedKeys: two spaces, a space before the colon.
  function pretty(v, ind) {
    ind = ind || "";
    var next = ind + "  ";
    if (Array.isArray(v)) {
      if (!v.length) return "[\n\n" + ind + "]";
      return "[\n" + v.map(function (x) { return next + pretty(x, next); }).join(",\n") + "\n" + ind + "]";
    }
    if (v && typeof v === "object") {
      var keys = Object.keys(v).sort();
      if (!keys.length) return "{\n\n" + ind + "}";
      return "{\n" + keys.map(function (k) { return next + JSON.stringify(k) + " : " + pretty(v[k], next); }).join(",\n") + "\n" + ind + "}";
    }
    return JSON.stringify(v);
  }
  function minify(v) {
    if (Array.isArray(v)) return "[" + v.map(minify).join(",") + "]";
    if (v && typeof v === "object") return "{" + Object.keys(v).sort().map(function (k) { return JSON.stringify(k) + ":" + minify(v[k]); }).join(",") + "}";
    return JSON.stringify(v);
  }
  // Capture group names in pattern order (null for unnamed groups).
  function groupNames(p) {
    var names = [], inClass = false;
    for (var i = 0; i < p.length; i++) {
      var ch = p.charAt(i);
      if (ch === "\\") { i++; continue; }
      if (inClass) { if (ch === "]") inClass = false; continue; }
      if (ch === "[") { inClass = true; continue; }
      if (ch !== "(") continue;
      if (p.charAt(i + 1) !== "?") names.push(null);
      else if (p.charAt(i + 2) === "<" && p.charAt(i + 3) !== "=" && p.charAt(i + 3) !== "!") {
        var m = /^\(\?<([A-Za-z_$][\w$]*)>/.exec(p.slice(i));
        names.push(m ? m[1] : null);
      }
    }
    return names;
  }
  function parseJSON(t) {
    t = t.trim();
    if (!/^(\{[\s\S]*\}|\[[\s\S]*\])$/.test(t)) return undefined;
    try { return JSON.parse(t); } catch (e) { return undefined; }
  }

  // ------------------------------------------------------------------ the demo
  var PRESETS = {
    ring: { sel: "g", ring: 2 },
    translate: { sel: "b", card: "translate", mode: "compare" },
    unit: { sel: "c", card: "units" },
    json: { sel: "d", card: "json" },
    regex: { sel: "e", card: "regex" },
    ai: { sel: "a", card: "ai", ai: 2 },
    history: { sel: null, card: "history" },
    actions: { sel: "d", card: "chooser" }
  };
  var SLOTS = ["translate", "search", "dictionary", "openLink", "allActions", "clipboard", "screenshotOCR", "pickColor"];
  var counter = 0;

  function Demo(root) {
    this.root = root;
    this.uid = "ppd" + (++counter);
    this.lang = root.getAttribute("data-lang") === "zh" ? "zh" : "en";
    this.s = S[this.lang];
    this.desk = root.hasAttribute("data-desk");
    this.icon = root.getAttribute("data-icon") || "";
    this.presetName = root.getAttribute("data-preset") || "ring";
    this.preset = PRESETS[this.presetName] || PRESETS.ring;
    var texts = {};
    DOC[this.lang].forEach(function (p) { p.forEach(function (r) { if (typeof r !== "string") texts[r[0]] = r[1]; }); });
    this.texts = texts;
    this.orig = {};
    for (var k in texts) this.orig[k] = texts[k];
    this.sel = null;
    this.ov = null;  // the open ring or card
    this.hist = HISTORY[this.lang].map(function (h, i) {
      return { id: "h" + i, min: h[0], kind: h[1], text: h[2], size: h[3] || "", pinned: !!h[4] };
    });
    this.hseq = 0;
    this.build();
  }

  Demo.prototype = {
    t: function (k) { return this.s[k] !== undefined ? this.s[k] : S.en[k]; },

    // -------------------------------------------------------------- content
    // What Pop reads from the selection (ContentClassifier, simplified): kinds, the ring's centre text,
    // and whether a direct rule skips the ring (foreign text → Translate, a measurement → Convert Units).
    classify: function (id) {
      if (!id) return { id: null, text: "", kinds: {}, summary: this.t("nothing") };
      var text = this.texts[id], k = { text: true }, summary;
      var han = /[一-鿿]/.test(text);
      if (/^(https?:\/\/|www\.)\S+$/i.test(text)) { k.url = true; summary = this.t("kLink"); }
      else if (parseJSON(text) !== undefined) { k.json = true; summary = "JSON"; }
      else if (parseQuantity(text)) { k.measure = true; summary = chars(text) <= 12 ? text : this.t("kMeasure"); }
      else {
        if (this.lang === "zh") { if (han) k.chinese = true; else if (/[A-Za-z]/.test(text)) k.foreign = true; }
        else if (han || /[àâçéèêëîïôûùüÿœ]|\b(le|la|les|qui|est|et|des|du|lui|si|chaque)\b/i.test(text)) k.foreign = true;
        if (/^[\p{L}'’-]+$/u.test(text) && chars(text) <= 40) k.word = true;
        summary = k.word ? text : fmt(this.t("nChars"), chars(text));
      }
      var direct = k.foreign ? "translate" : k.measure ? "units" : null;
      return { id: id, text: text, kinds: k, summary: summary, direct: direct };
    },
    // Whether a slot or action can handle the content, and the ring's hint when it can't (RingViewModel.unavailableHint).
    can: function (act, c) {
      var k = c.kinds;
      switch (act) {
        case "translate": case "search": case "speak": case "ai": case "regex": case "stats": case "plain": case "cleanup":
          return k.text ? true : "needText";
        case "dictionary": return k.text ? (chars(c.text) <= 60 ? true : "notAvailable") : "needText";
        case "openLink": return k.url ? true : "needLink";
        case "units": return k.measure ? true : "notAvailable";
        case "json": case "jsonTypes": return k.json ? true : "notAvailable";
        case "extract": return k.text && /https?:\/\/|@\w/.test(c.text) ? true : "notAvailable";
        case "qr": return k.text && chars(c.text) <= 1000 ? true : "needText";
        default: return true;  // allActions, clipboard, screenshotOCR, pickColor
      }
    },
    actionList: function (c) {
      var self = this;
      var order = ["units", "json", "jsonTypes", "openLink", "translate", "search", "dictionary", "speak", "ai", "regex",
        "stats", "cleanup", "extract", "plain", "qr", "clipboard", "ocr", "color"];
      return order.filter(function (a) { return self.can(a === "ocr" || a === "color" ? "x" : a, c) === true; });
    },

    // -------------------------------------------------------------- build
    build: function () {
      var r = this.root, self = this;
      r.classList.add("ppd-ready");
      r.setAttribute("role", "group");
      r.setAttribute("aria-label", this.t("demoLabel"));
      r.setAttribute("lang", this.lang === "zh" ? "zh-CN" : "en");
      var noscript = r.querySelector("noscript");
      r.innerHTML = "";
      if (noscript) r.appendChild(noscript);
      var stage = document.createElement("div");
      stage.className = "pp-stage" + (this.desk ? " pp-desk" : "");
      stage.innerHTML = (this.desk ? this.menubar() : "") + this.windowHTML() +
        '<div class="pp-layer"></div><div class="pp-toast" role="status" aria-live="polite"></div>';
      r.appendChild(stage);
      var tag = document.createElement("figcaption");
      tag.className = "ppd-tag";
      tag.innerHTML = '<span class="ppd-dot" aria-hidden="true"></span>' + esc(this.t("demo"));
      r.appendChild(tag);
      this.stage = stage;
      this.layer = stage.querySelector(".pp-layer");
      this.toastEl = stage.querySelector(".pp-toast");
      this.doc = stage.querySelector(".pp-doc");

      stage.addEventListener("pointerdown", function (e) { self.onDown(e); });
      stage.addEventListener("pointermove", function (e) { self.onMove(e); });
      stage.addEventListener("click", function (e) { self.onClick(e); });
      stage.addEventListener("contextmenu", function (e) { e.preventDefault(); });
      stage.addEventListener("keydown", function (e) { self.onKey(e); });
      stage.addEventListener("input", function (e) { self.onInput(e); });
      stage.addEventListener("compositionend", function (e) { self.onInput(e); });
      stage.addEventListener("change", function (e) { self.onChange(e); });
      stage.addEventListener("focusin", function (e) {
        var slot = e.target.closest && e.target.closest(".pp-slot");
        if (slot && self.ov && self.ov.type === "ring") self.setHover(+slot.getAttribute("data-i"));
      });
      this.upHandler = function (e) { self.onUp(e); };
      this.moveHandler = function (e) { self.onMove(e); };
      if (window.ResizeObserver) {
        var w = 0;
        new ResizeObserver(function () {
          if (stage.clientWidth === w) return;
          w = stage.clientWidth;
          self.reposition();
        }).observe(stage);
      }
      this.applyPreset();
    },

    menubar: function () {
      var s = this.s, menus = s.menus.map(function (m) { return '<span class="pp-mb-item">' + esc(m) + "</span>"; }).join("");
      return '<div class="pp-mb" aria-hidden="true"><span class="pp-mb-apple"></span><span class="pp-mb-item pp-mb-app">' +
        esc(s.app) + "</span>" + menus + '<span class="pp-mb-fill"></span>' +
        (this.icon ? '<span class="pp-mb-item pp-mb-icon"><img src="' + esc(this.icon) + '" alt=""></span>' : "") +
        '<span class="pp-mb-item">' + esc(s.clock) + "</span></div>";
    },

    windowHTML: function () {
      var self = this;
      var paras = DOC[this.lang].map(function (p) {
        return "<p>" + p.map(function (run) {
          if (typeof run === "string") return esc(run);
          var id = run[0];
          var mono = id === "d" ? " is-mono" : "";
          return '<button type="button" class="pp-sn' + mono + '" data-sn="' + id + '" aria-pressed="false">' + esc(self.texts[id]) + "</button>";
        }).join("") + "</p>";
      }).join("");
      var touch = touchFirst();
      return '<div class="pp-win"><div class="pp-bar" aria-hidden="true"><i></i><i></i><i></i><span>' + esc(this.t("docTitle")) +
        '</span></div><div class="pp-doc"><h4>' + esc(this.t("docHead")) + "</h4>" + paras + "</div>" +
        '<button type="button" class="pp-hold" aria-label="' + esc(this.t("holdLabel")) + '">' + I.hold +
        "<span>" + esc(this.t(touch ? "hintTouch" : "hintMouse")) + "</span></button></div>";
    },

    applyPreset: function () {
      var p = this.preset;
      this.select(p.sel || null);
      var self = this;
      var place = function () {
        var a = self.anchorFor(p.sel);
        if (p.ring !== undefined) {
          self.openRing(a.x, a.y, { instant: true, hover: p.ring });
        } else if (p.card) {
          var opts = { instant: true, noFocus: true };
          if (p.card === "translate") opts.mode = p.mode;
          if (p.card === "ai") opts.run = p.ai;
          if (p.card === "history") opts.marked = ["h1", "h2"];
          self.openCard(p.card, a, opts);
        }
      };
      place();
    },

    // Where a snippet sits in the stage (the ring and cards open there).
    anchorFor: function (id) {
      var st = this.stage.getBoundingClientRect();
      var el = id ? this.doc.querySelector('[data-sn="' + id + '"]') : this.stage.querySelector(".pp-hold");
      if (!el || !st.width) return { x: st.width / 2 || 200, y: 160 };
      var rects = el.getClientRects(), r = rects.length ? rects[0] : el.getBoundingClientRect();
      return { x: r.left - st.left + Math.min(r.width, 160) / 2, y: r.top - st.top + r.height / 2 };
    },
    point: function (e) {
      var st = this.stage.getBoundingClientRect();
      return { x: e.clientX - st.left, y: e.clientY - st.top };
    },

    select: function (id) {
      this.sel = id;
      Array.prototype.forEach.call(this.doc.querySelectorAll(".pp-sn"), function (b) {
        var on = b.getAttribute("data-sn") === id;
        b.classList.toggle("is-sel", on);
        b.setAttribute("aria-pressed", on ? "true" : "false");
      });
    },

    // -------------------------------------------------------------- pointer
    onDown: function (e) {
      this.ptype = e.pointerType || "mouse";
      var t = e.target;
      if (this.ov && this.ov.type === "ring") {
        if (this.ptype !== "mouse") {
          var sl = t.closest(".pp-slot");
          if (sl) this.setHover(+sl.getAttribute("data-i"));
        }
        return;
      }
      if (t.closest(".pp-pin")) return;
      if (this.ov && this.ov.el.contains(t)) {
        if (this.ov.menu && !t.closest(".pp-menu") && !t.closest("[data-menu]")) { this.ov.menu = null; this.renderCard(); }
        return;
      }
      if (this.ptype !== "mouse") return;  // touch and pen: a tap opens Pop (see onClick)
      if (e.button !== 0 && e.button !== 2) return;
      var sn = t.closest(".pp-sn"), hold = t.closest(".pp-hold"), inDoc = t.closest(".pp-win");
      if (this.ov) this.close(true);
      if (!inDoc) return;
      if (sn) this.select(sn.getAttribute("data-sn"));
      else if (!hold && e.button === 0) this.select(null);
      this.returnTo = sn || hold || null;
      var p = this.point(e), self = this;
      this.press = { x: p.x, y: p.y, cx: e.clientX, cy: e.clientY, opened: false };
      this.press.timer = setTimeout(function () {
        if (!self.press) return;
        self.press.opened = true;
        self.open(self.press.x, self.press.y, { held: true });
      }, 250);
      window.addEventListener("pointerup", this.upHandler, true);
      window.addEventListener("pointermove", this.moveHandler, true);
      if (sn || hold) e.preventDefault();
    },
    onMove: function (e) {
      if (e.pointerType && e.pointerType !== "mouse") return;
      var pr = this.press;
      if (pr && !pr.opened) {
        var dx = e.clientX - pr.cx, dy = e.clientY - pr.cy;
        if (dx * dx + dy * dy > 36) { clearTimeout(pr.timer); this.endPress(); }  // a drag goes to the app
        return;
      }
      var ov = this.ov;
      if (ov && ov.type === "ring" && !ov.committed && !ov.leaving) {
        var p = this.point(e);
        var dx2 = p.x - ov.x, dy2 = p.y - ov.y, d = Math.sqrt(dx2 * dx2 + dy2 * dy2);
        this.setHover(d > G.outer + 24 && !ov.held ? null : slotAt(dx2, dy2));
      }
    },
    onUp: function (e) {
      var pr = this.press;
      if (!pr) return;
      clearTimeout(pr.timer);
      this.endPress();
      if (!pr.opened) return;
      this.suppressClick = true;
      var self = this;
      setTimeout(function () { self.suppressClick = false; }, 0);
      var ov = this.ov;
      if (ov && ov.type === "ring") {
        ov.held = false;
        // Released on a slot that can run: run it. Otherwise the ring stays open for clicking
        // (RingReleaseAction.keepOpen, as with "Keep the ring open" in Pop's settings).
        if (ov.hover !== null && ov.enabled[ov.hover] === true && !ov.loading) this.commit(ov.hover);
        else if (ov.hover === null) this.focusRing();
      }
    },
    endPress: function () {
      this.press = null;
      window.removeEventListener("pointerup", this.upHandler, true);
      window.removeEventListener("pointermove", this.moveHandler, true);
    },

    onClick: function (e) {
      if (this.suppressClick) { this.suppressClick = false; return; }
      var t = e.target, ov = this.ov;
      var pin = t.closest(".pp-pin-x");
      if (pin) { this.unpin(); return; }
      if (ov && ov.type === "ring") {
        if (ov.committed || ov.leaving) return;
        var slot = t.closest(".pp-slot");
        if (slot) { this.activate(+slot.getAttribute("data-i")); return; }
        if (e.detail === 0) return;
        var p = this.point(e), dx = p.x - ov.x, dy = p.y - ov.y, d = Math.sqrt(dx * dx + dy * dy);
        if (this.ptype !== "mouse" || d < G.inner || d > G.outer + 24) { this.close(); return; }
        var i = slotAt(dx, dy);
        if (i !== null) this.activate(i);
        return;
      }
      if (ov && ov.type === "card") {
        if (ov.el.contains(t)) { this.onCardClick(e); return; }
        if (this.ptype !== "mouse" && e.detail !== 0) this.close();  // a tap outside closes the card
        ov = this.ov;
      }
      var sn = t.closest(".pp-sn"), hold = t.closest(".pp-hold");
      if (!sn && !hold) return;
      var keyboard = e.detail === 0;
      var tap = this.ptype !== "mouse" && !keyboard;
      if (sn && !keyboard && !tap) return;  // a short click only selects
      if (sn) this.select(sn.getAttribute("data-sn"));
      if (ov) this.close(true);
      this.returnTo = sn || hold;
      var a;
      if (keyboard || !tap) {
        var el = sn || hold, st = this.stage.getBoundingClientRect(), r = el.getBoundingClientRect();
        a = sn ? this.anchorFor(sn.getAttribute("data-sn")) : { x: r.left - st.left + r.width / 2, y: r.top - st.top + r.height / 2 };
      } else a = this.point(e);
      this.open(a.x, a.y, { keyboard: keyboard });
    },

    // -------------------------------------------------------------- open / close
    open: function (x, y, opts) {
      opts = opts || {};
      var c = this.classify(this.sel);
      if (c.direct) this.openCard(c.direct, { x: x, y: y }, { focus: opts.keyboard });
      else this.openRing(x, y, { held: opts.held, keyboard: opts.keyboard });
    },

    close: function (quick) {
      var ov = this.ov;
      if (!ov) return;
      this.ov = null;
      clearTimeout(ov.timer);
      clearInterval(ov.stream);
      var el = ov.el, hadFocus = el.contains(document.activeElement);
      if (quick || reduced()) el.parentNode && el.parentNode.removeChild(el);
      else {
        el.classList.add("is-leaving");
        setTimeout(function () { if (el.parentNode) el.parentNode.removeChild(el); }, 170);
      }
      if (hadFocus) {
        var back = this.returnTo && this.stage.contains(this.returnTo) ? this.returnTo : this.stage.querySelector(".pp-hold");
        back.focus({ preventScroll: true });
      }
    },

    // -------------------------------------------------------------- the ring
    openRing: function (x, y, opts) {
      var W = this.stage.clientWidth, H = this.stage.clientHeight, pad = 6;
      x = W < G.outer * 2 + pad * 2 ? W / 2 : clamp(x, G.outer + pad, W - G.outer - pad);
      y = clamp(y, G.outer + pad + (this.desk ? 24 : 0), Math.max(G.outer + pad, H - G.outer - pad));
      var c = this.classify(this.sel), self = this;
      var ov = { type: "ring", x: x, y: y, content: c, hover: null, angle: 0, committed: null, held: !!opts.held,
        loading: !opts.instant, enabled: [] };
      var el = document.createElement("div");
      el.className = "pp-ring";
      el.setAttribute("role", "menu");
      el.setAttribute("aria-label", this.t("ringLabel"));
      el.style.left = x + "px";
      el.style.top = y + "px";
      var slots = SLOTS.map(function (name, i) {
        var a = (90 - i * G.step) * Math.PI / 180;
        var dx = Math.cos(a) * G.label, dy = -Math.sin(a) * G.label;
        return '<button type="button" role="menuitem" class="pp-slot" data-i="' + i + '" tabindex="-1" style="--x:' + dx.toFixed(2) +
          "px;--y:" + dy.toFixed(2) + "px;--i:" + i + '"><span class="pp-slot-in">' + I[name] + "<span>" + esc(self.t(name)) + "</span></span></button>";
      }).join("");
      var arcR = G.outer - 5, half = G.arc / 2 * Math.PI / 180;
      var ax = arcR * Math.sin(half);
      var ay = G.outer - arcR * Math.cos(half);
      el.innerHTML = '<div class="pp-disc"></div>' +
        '<div class="pp-hl" aria-hidden="true"><i class="pp-hl-dot" style="width:' + (G.hl * 2).toFixed(1) + "px;height:" + (G.hl * 2).toFixed(1) +
        "px;top:" + (G.outer - G.label - G.hl).toFixed(1) + 'px"></i><svg viewBox="0 0 ' + G.outer * 2 + " " + G.outer * 2 + '"><path d="M' +
        (G.outer - ax).toFixed(2) + " " + ay.toFixed(2) + "A" + arcR + " " + arcR + " 0 0 1 " + (G.outer + ax).toFixed(2) + " " + ay.toFixed(2) + '"/></svg></div>' +
        slots +
        '<div class="pp-hub"><div class="pp-hub-rot" aria-hidden="true"><i></i></div><div class="pp-center" aria-live="polite"></div></div>';
      this.layer.appendChild(el);
      ov.el = el;
      this.ov = ov;
      this.applyContent(ov.loading ? null : c);
      if (opts.instant || reduced()) el.classList.add("is-shown");
      else { void el.offsetWidth; el.classList.add("is-shown"); }
      if (opts.hover !== undefined) this.setHover(opts.hover);
      if (ov.loading) {
        ov.timer = setTimeout(function () { if (self.ov === ov) { ov.loading = false; self.applyContent(c); } }, 140);
      }
      this.focusRing(!!opts.keyboard);
    },
    applyContent: function (c) {
      var ov = this.ov, self = this;
      ov.el.classList.toggle("is-loading", !c);
      SLOTS.forEach(function (name, i) {
        var ok = c ? self.can(name, c) : false;
        ov.enabled[i] = c ? ok : false;
        var b = ov.el.querySelector('.pp-slot[data-i="' + i + '"]');
        b.classList.toggle("is-off", c ? ok !== true : false);
        b.setAttribute("aria-disabled", ok === true ? "false" : "true");
        var hint = ok === true || !c ? "" : ", " + self.t(ok);
        b.setAttribute("aria-label", self.t(name) + hint);
      });
      this.updateCenter();
      if (ov.hover !== null) this.setHover(ov.hover, true);
    },
    updateCenter: function () {
      var ov = this.ov, box = ov.el.querySelector(".pp-center"), html;
      if (ov.loading) html = '<span class="pp-spin" aria-label="' + esc(this.t("reading")) + '"></span>';
      else if (ov.hover === null) html = '<span class="pp-c-content">' + esc(ov.content.summary) + "</span>";
      else {
        var name = SLOTS[ov.hover], ok = ov.enabled[ov.hover];
        html = '<span class="pp-c-fn' + (ok === true ? "" : " is-off") + '">' + esc(this.t(name)) + "</span>" +
          (ok === true ? "" : '<span class="pp-c-detail">' + esc(this.t(ok)) + "</span>");
      }
      box.innerHTML = html;
    },
    setHover: function (i, force) {
      var ov = this.ov;
      if (!ov || ov.type !== "ring" || ov.committed !== null) return;
      if (i === ov.hover && !force) return;
      var el = ov.el, hl = el.querySelector(".pp-hl"), rot = el.querySelector(".pp-hub-rot");
      if (i !== null) {
        var target = i * G.step;
        if (ov.hover === null) {
          // A fresh highlight appears on its slot rather than sliding in from where the last one left.
          ov.angle = target;
          hl.style.transition = rot.style.transition = "none";
          hl.style.transform = rot.style.transform = "rotate(" + ov.angle + "deg)";
          void hl.offsetWidth;
          hl.style.transition = rot.style.transition = "";
        } else {
          ov.angle = target + 360 * Math.round((ov.angle - target) / 360);  // RingGeometry.continuousAngle: the short way round
          hl.style.transform = rot.style.transform = "rotate(" + ov.angle + "deg)";
        }
      }
      ov.hover = i;
      el.classList.toggle("has-hover", i !== null);
      el.classList.toggle("hover-off", i !== null && ov.enabled[i] !== true);
      Array.prototype.forEach.call(el.querySelectorAll(".pp-slot"), function (b, j) {
        b.classList.toggle("is-active", j === i && ov.enabled[j] === true);
      });
      this.updateCenter();
    },
    focusRing: function (first) {
      var ov = this.ov;
      if (!ov || ov.type !== "ring") return;
      var i = ov.hover !== null ? ov.hover : 0;
      if (first && ov.hover === null) this.setHover(0);
      var b = ov.el.querySelector('.pp-slot[data-i="' + i + '"]');
      Array.prototype.forEach.call(ov.el.querySelectorAll(".pp-slot"), function (x) { x.tabIndex = x === b ? 0 : -1; });
      if (first) b.focus({ preventScroll: true });
    },
    activate: function (i) {
      var ov = this.ov;
      if (!ov || ov.loading) return;
      this.setHover(i);
      if (ov.enabled[i] === true) this.commit(i);
    },
    commit: function (i) {
      var ov = this.ov, self = this;
      ov.committed = i;
      ov.el.classList.add("is-committed");
      ov.el.querySelector('.pp-slot[data-i="' + i + '"]').classList.add("is-commit");
      var name = SLOTS[i], anchor = { x: ov.x, y: ov.y }, hadFocus = ov.el.contains(document.activeElement);
      setTimeout(function () {
        if (self.ov !== ov) return;
        self.close();
        self.run(name, anchor, hadFocus);
      }, reduced() ? 0 : 150);
    },

    // -------------------------------------------------------------- actions
    run: function (name, anchor, focus) {
      var c = this.classify(this.sel), self = this;
      var toast = { search: "tSearch", openLink: "tLink", screenshotOCR: "tOCR", ocr: "tOCR", pickColor: "tColor", color: "tColor",
        jsonTypes: "tNotInDemo", cleanup: "tNotInDemo", extract: "tNotInDemo", qr: "tNotInDemo" }[name];
      if (toast) { this.toast(this.t(toast)); if (focus) this.refocus(); return; }
      if (name === "plain") { this.copy(c.text, "copiedPlain"); if (focus) this.refocus(); return; }
      if (name === "speak") {
        try {
          if (window.speechSynthesis) {
            var u = new SpeechSynthesisUtterance(c.text);
            u.lang = c.kinds.foreign ? (this.lang === "zh" ? "en-US" : "fr-FR") : (this.lang === "zh" ? "zh-CN" : "en-US");
            speechSynthesis.cancel();
            speechSynthesis.speak(u);
          }
        } catch (err) { /* no voice */ }
        if (focus) this.refocus();
        return;
      }
      var card = { translate: "translate", dictionary: "dictionary", allActions: "chooser", clipboard: "history",
        units: "units", json: "json", ai: "ai", regex: "regex", stats: "stats" }[name];
      if (card) self.openCard(card, anchor, { focus: focus || !touchFirst() });
    },
    refocus: function () {
      var back = this.returnTo && this.stage.contains(this.returnTo) ? this.returnTo : this.stage.querySelector(".pp-hold");
      back.focus({ preventScroll: true });
    },
    toast: function (msg) {
      var el = this.toastEl, self = this;
      el.textContent = msg;
      el.classList.remove("is-on");
      void el.offsetWidth;
      el.classList.add("is-on");
      clearTimeout(this.toastTimer);
      this.toastTimer = setTimeout(function () { el.classList.remove("is-on"); }, Math.max(1100, msg.length * 45));
      void self;
    },
    copy: function (text, key) {
      try { if (navigator.clipboard && window.isSecureContext) navigator.clipboard.writeText(text).catch(function () {}); } catch (e) { /* ignore */ }
      this.remember(text);
      this.toast(this.t(key || "copied"));
    },
    remember: function (text) {
      for (var i = 0; i < this.hist.length; i++) if (this.hist[i].kind === "text" && this.hist[i].text === text) { this.hist.splice(i, 1); break; }
      this.hist.unshift({ id: "n" + (++this.hseq), min: 0, kind: "text", text: text, pinned: false });
    },
    replace: function (text) {
      var id = this.sel;
      if (!id) { this.copy(text); return; }
      this.texts[id] = text;
      var b = this.doc.querySelector('[data-sn="' + id + '"]');
      b.textContent = text;
      b.classList.toggle("is-mono", parseJSON(text) !== undefined);
      b.classList.remove("is-flash");
      void b.offsetWidth;
      b.classList.add("is-flash");
    },
    pin: function (text) {
      this.unpin();
      var el = document.createElement("div");
      el.className = "pp-pin";
      el.innerHTML = '<button type="button" class="pp-x pp-pin-x" aria-label="' + esc(this.t("pinClose")) + '">' + I.close + "</button><p>" + esc(text) + "</p>";
      this.stage.appendChild(el);
      this.pinEl = el;
    },
    unpin: function () {
      if (this.pinEl && this.pinEl.parentNode) this.pinEl.parentNode.removeChild(this.pinEl);
      this.pinEl = null;
    },

    // -------------------------------------------------------------- cards
    openCard: function (type, anchor, opts) {
      opts = opts || {};
      if (this.ov) this.close(true);
      var c = this.classify(this.sel);
      var ov = { type: "card", card: type, content: c, x: anchor.x, y: anchor.y, menu: null };
      if (type === "translate") {
        var src = c.kinds.foreign ? (this.lang === "zh" ? "en" : "fr") : (this.lang === "zh" ? "zh-Hans" : "en");
        ov.src = src;
        ov.target = this.lang === "zh" ? (src === "zh-Hans" ? "en" : "zh-Hans") : (src === "en" ? "zh-Hans" : "en");
        ov.mode = opts.mode || "system";
        ov.done = {};
        if (opts.instant) { ov.done.system = ov.done.ai = ov.done.deepl = true; }
      } else if (type === "regex") {
        ov.pattern = REGEX_PRESETS[7];
        ov.replacement = "$3/$2/$1";
        ov.flags = { i: false, m: true, s: false };
      } else if (type === "ai") {
        ov.phase = "idle"; ov.output = ""; ov.active = null; ov.label = null; ov.question = "";
      } else if (type === "history") {
        ov.query = ""; ov.filter = 0; ov.hsel = 0; ov.marked = opts.marked ? opts.marked.slice() : [];
      } else if (type === "chooser") {
        ov.query = ""; ov.csel = 0;
      }
      var el = document.createElement("div");
      el.className = "pp-card pp-card-" + type;
      el.setAttribute("role", "dialog");
      el.tabIndex = -1;
      ov.el = el;
      this.ov = ov;
      this.layer.appendChild(el);
      this.renderCard();
      if (!opts.instant && !reduced()) {
        el.classList.add("is-entering");
        void el.offsetWidth;
        el.classList.remove("is-entering");
      }
      if (type === "translate" && !opts.instant) this.fetch(ov.mode === "compare" ? ["system", "ai", "deepl"] : [ov.mode]);
      if (type === "ai" && opts.run !== undefined) {
        ov.active = opts.run; ov.label = this.s.aiActs[opts.run]; ov.phase = "done"; ov.output = this.aiAnswer(opts.run);
        this.renderCard();
      }
      if (!opts.noFocus && (opts.focus || !touchFirst())) {
        // On touch screens focus the card, not its text field, so the on-screen keyboard stays down.
        var f = touchFirst() ? el : el.querySelector("[data-autofocus]") || el;
        f.focus({ preventScroll: true });
      }
    },

    reposition: function () {
      var ov = this.ov;
      if (!ov) return;
      if (ov.type === "ring") {
        var W = this.stage.clientWidth, H = this.stage.clientHeight, pad = 6;
        var x = W < G.outer * 2 + pad * 2 ? W / 2 : clamp(ov.x, G.outer + pad, W - G.outer - pad);
        var y = clamp(ov.y, G.outer + pad, Math.max(G.outer + pad, H - G.outer - pad));
        ov.x = x; ov.y = y;
        ov.el.style.left = x + "px"; ov.el.style.top = y + "px";
      } else this.placeCard();
    },
    placeCard: function () {
      var ov = this.ov, el = ov.el, W = this.stage.clientWidth, H = this.stage.clientHeight, m = 8;
      var top0 = this.desk ? 30 : m;
      var w = el.offsetWidth, h = el.offsetHeight;
      var left = clamp(ov.x - w / 2, m, Math.max(m, W - w - m));
      var top = clamp(ov.y - 28, top0, Math.max(top0, H - h - m));
      el.style.left = left + "px";
      el.style.top = top + "px";
      el.style.transformOrigin = clamp(ov.x - left, 0, w) + "px " + clamp(ov.y - top, 0, h) + "px";
    },

    renderCard: function () {
      var ov = this.ov;
      if (!ov || ov.type !== "card") return;
      var el = ov.el, active = document.activeElement, key = null, sel = null, scroll = {};
      if (active && el.contains(active)) {
        key = active.getAttribute("data-k");
        if (active.tagName === "INPUT" && active.type === "text") sel = [active.selectionStart, active.selectionEnd];
      }
      Array.prototype.forEach.call(el.querySelectorAll("[data-scroll]"), function (s) { scroll[s.getAttribute("data-scroll")] = s.scrollTop; });
      var body = this["card_" + ov.card]();
      el.setAttribute("aria-label", body.title);
      el.style.setProperty("--w", body.width + "px");
      el.innerHTML = '<div class="pp-head"><h5>' + esc(body.title) + "</h5>" +
        (body.subtitle ? '<span class="pp-sub">' + esc(body.subtitle) + "</span>" : "") +
        '<button type="button" class="pp-x" data-a="close" data-k="close" aria-label="' + esc(this.t("close")) + '" title="' + esc(this.t("close")) + '">' + I.close + "</button></div>" +
        body.html;
      Array.prototype.forEach.call(el.querySelectorAll("[data-scroll]"), function (s) {
        var k = s.getAttribute("data-scroll");
        if (scroll[k]) s.scrollTop = scroll[k];
      });
      if (key) {
        var f = el.querySelector('[data-k="' + key + '"]');
        if (f) {
          f.focus({ preventScroll: true });
          if (sel && f.setSelectionRange) f.setSelectionRange(sel[0], sel[1]);
        } else el.focus({ preventScroll: true });
      }
      this.placeCard();
    },

    btn: function (label, a, extra) {
      extra = extra || {};
      return '<button type="button" class="pp-btn' + (extra.cls ? " " + extra.cls : "") + '" data-a="' + a + '" data-k="' + (extra.k || a) + '"' +
        (extra.arg !== undefined ? ' data-arg="' + esc(extra.arg) + '"' : "") + (extra.title ? ' title="' + esc(extra.title) + '"' : "") +
        (extra.disabled ? " disabled" : "") + (extra.pressed !== undefined ? ' aria-pressed="' + extra.pressed + '"' : "") + ">" + esc(label) + "</button>";
    },
    flow: function (items) { return '<div class="pp-flow">' + items.join("") + "</div>"; },
    rowsHTML: function (rows, replaceable) {
      var self = this;
      return '<div class="pp-rows">' + rows.map(function (r, i) {
        return '<div class="pp-row"><span class="pp-row-l" title="' + esc(r[0]) + '">' + esc(r[0]) + '</span><span class="pp-row-v">' + esc(r[1]) + "</span>" +
          '<button type="button" class="pp-ib" data-a="copyRow" data-arg="' + i + '" data-k="rc' + i + '" aria-label="' + esc(self.t("rowCopy") + " " + r[1]) + '" title="' + esc(self.t("rowCopy")) + '">' + I.copy + "</button>" +
          (replaceable ? '<button type="button" class="pp-ib" data-a="replaceRow" data-arg="' + i + '" data-k="rr' + i + '" aria-label="' + esc(self.t("rowReplace") + ": " + r[1]) + '" title="' + esc(self.t("rowReplace")) + '">' + I.back + "</button>" : "") +
          "</div>";
      }).join("") + "</div>";
    },
    more: function () { return this.btn(this.t("more"), "more"); },

    // Convert Units (UnitConvertPlugin → ResultCard with replaceable rows and a detail line)
    card_units: function () {
      var q = parseQuantity(this.ov.content.text) || { value: 5, unit: "km" }, src = unitOf(q.unit), self = this;
      var meters = q.value * src[2];
      var all = UNITS.filter(function (u) { return u[0] !== q.unit; }).map(function (u) { return [u, meters / u[2]]; });
      var readable = all.filter(function (x) { var m = Math.abs(x[1]); return m === 0 || (m >= 0.01 && m <= 1e6); });
      var list = (readable.length >= 3 ? readable : all).slice(0, 8);
      var rows = list.map(function (x) { return [self.t("u_" + x[0][0]), unitDisplay(x[1], x[0])]; });
      if (["ft", "in", "mi", "nmi"].indexOf(q.unit) < 0 && meters >= 0.3 && meters < 3) {
        var ti = meters / 0.0254, ft = Math.floor(ti / 12), inch = Math.round((ti - ft * 12) * 10) / 10;
        if (inch >= 12) { ft += 1; inch = 0; }
        rows.push([this.t("u_ftin"), ft + "′ " + inch.toFixed(1).replace(/\.0$/, "") + "″"]);
      }
      this.ov.rows = rows;
      return { title: this.t("units"), width: 380,
        html: this.rowsHTML(rows, true) + '<p class="pp-cap">' + esc(fmt(this.t("detail"), this.t("length"), unitDisplay(q.value, src))) + "</p>" + this.flow([this.more()]) };
    },

    card_stats: function () {
      var text = this.ov.content.text, han = (text.match(/[一-鿿]/g) || []).length;
      var latin = (text.match(/[A-Za-z0-9]+(?:['’.-][A-Za-z0-9]+)*/g) || []).length;
      var words = latin + Math.ceil(han / 1.6);
      var minutes = han / 400 + latin / 200;
      var rows = [[this.t("sChars"), String(chars(text))], [this.t("sNoSpace"), String(chars(text.replace(/\s/g, "")))]];
      if (han) rows.push([this.t("sHan"), String(han)]);
      rows.push([this.t("sWords"), String(words)], [this.t("sLines"), String(text.split(/\n/).length)],
        [this.t("sBytes"), String(window.TextEncoder ? new TextEncoder().encode(text).length : text.length)],
        [this.t("sRead"), minutes < 1 ? this.t("under1") : fmt(this.t("aboutMin"), Math.round(minutes))]);
      this.ov.rows = rows;
      return { title: this.t("stats"), width: 380, html: this.rowsHTML(rows, false) + this.flow([this.more()]) };
    },

    card_json: function () {
      var v = parseJSON(this.ov.content.text), body = pretty(v);
      this.ov.body = body; this.ov.min = minify(v);
      return { title: this.t("formatJSON"), width: 380,
        html: '<pre class="pp-mono pp-scroll" data-scroll="json">' + esc(body) + "</pre>" +
          this.flow([this.btn(this.t("copy"), "copyBody", { title: "⌘C" }), this.btn(this.t("replace"), "replaceBody", { title: "⌘↩" }),
            this.btn(this.t("copyMin"), "copyMin"), this.more()]) };
    },

    card_dictionary: function () {
      var text = this.ov.content.text, def = DICT[text];
      return { title: this.t("dictionary"), width: 380,
        html: '<p class="pp-body pp-pre">' + esc(def || fmt(this.t("notFound"), text)) + "</p>" +
          this.flow([this.btn(this.t("openDict"), "toast", { arg: "tDict" }), this.more()]) };
    },

    // Translate (TranslationCardView)
    trText: function (engine, target) {
      var ov = this.ov, id = ov.content.id;
      target = target || ov.target;
      var entry;
      if (id === "b" && this.texts.b === this.orig.b) entry = GLASS[target];
      else if (TR[this.lang][id] && this.texts[id] === this.orig[id]) entry = TR[this.lang][id][target];
      if (!entry && (ov.content.kinds.json || ov.content.kinds.url)) entry = ov.content.text;
      if (!entry) return null;
      return typeof entry === "string" ? entry : entry[engine];
    },
    card_translate: function () {
      var ov = this.ov, s = this.s, self = this;
      var pair = langName(ov.src) + " → " + langName(ov.target);
      var engines = [["system", s.system], ["ai", "AI"], ["deepl", "DeepL"], ["compare", s.compare]];
      var seg = '<div class="pp-seg" role="group" aria-label="' + esc(this.t("engineHelp")) + '" title="' + esc(this.t("engineHelp")) + '">' + engines.map(function (e) {
        return '<button type="button" data-a="mode" data-arg="' + e[0] + '" data-k="m-' + e[0] + '" aria-pressed="' + (ov.mode === e[0]) + '"' +
          (ov.mode === e[0] ? ' class="is-on"' : "") + ">" + esc(e[1]) + "</button>";
      }).join("") + "</div>";
      var menu = "";
      if (ov.menu === "lang") {
        menu = '<div class="pp-menu" role="menu">' + LANGS.map(function (l) {
          return '<button type="button" role="menuitem" data-a="target" data-arg="' + l[0] + '" data-k="t-' + l[0] + '"' + (l[0] === ov.target ? " disabled" : "") + ">" + esc(l[1]) + "</button>";
        }).join("") + "</div>";
      }
      var top = '<div class="pp-trbar"><div class="pp-menuwrap"><button type="button" class="pp-menubtn" data-a="menu" data-arg="lang" data-menu data-k="lang" aria-haspopup="menu" aria-expanded="' +
        (ov.menu === "lang") + '" title="' + esc(this.t("langHelp")) + '">' + esc(fmt(this.t("to"), langName(ov.target))) + I.chev + "</button>" + menu + "</div>" + seg + "</div>";
      var src = '<p class="pp-src">' + esc(ov.content.text) + "</p><hr>";
      var result = function (engine) {
        if (!ov.done[engine]) return '<p class="pp-wait"><span class="pp-spin"></span>' + esc(self.t("translating")) + "</p>";
        var tx = self.trText(engine);
        if (tx === null) return '<p class="pp-note">' + esc(fmt(self.t("noSample"), self.lang === "zh" ? "English" : "简体中文")) + "</p>";
        return '<p class="pp-body">' + esc(tx) + "</p>";
      };
      var html = top + src, buttons = [];
      if (ov.mode === "compare") {
        html += '<div class="pp-compare">' + ["system", "ai", "deepl"].map(function (e) {
          var tx = ov.done[e] ? self.trText(e) : null;
          return '<div class="pp-cmp"><div class="pp-cmp-h"><span>' + esc(e === "system" ? s.system : e === "ai" ? "AI" : "DeepL") + "</span>" +
            (tx !== null ? '<button type="button" class="pp-link" data-a="copyTr" data-arg="' + e + '" data-k="cc-' + e + '">' + esc(self.t("copy")) + '</button><button type="button" class="pp-link" data-a="replaceTr" data-arg="' + e + '" data-k="cr-' + e + '">' + esc(self.t("replace")) + "</button>" : "") +
            "</div>" + result(e) + "</div>";
        }).join("") + "</div>";
      } else {
        html += result(ov.mode);
        if (ov.done[ov.mode] && this.trText(ov.mode) !== null) {
          buttons.push(this.btn(this.t("copyTr"), "copyTr", { arg: ov.mode, title: "⌘C" }), this.btn(this.t("replace"), "replaceTr", { arg: ov.mode, title: this.t("replaceHelp") }),
            this.btn(this.t("pin"), "pinTr", { arg: ov.mode, title: this.t("pinHelp") }), this.btn(this.t("speak"), "speakTr", { arg: ov.mode }));
        }
      }
      buttons.push(this.more());
      return { title: this.t("translate"), subtitle: pair, width: 380, html: html + this.flow(buttons) };
    },
    fetch: function (engines) {
      var ov = this.ov, self = this, missing = engines.filter(function (e) { return !ov.done[e]; });
      if (!missing.length) return;
      this.renderCard();
      var delays = { system: 360, ai: 700, deepl: 520 };
      missing.forEach(function (e) {
        setTimeout(function () {
          if (self.ov !== ov) return;
          ov.done[e] = true;
          self.renderCard();
        }, reduced() ? 60 : delays[e]);
      });
    },

    // Regex Tester (RegexTesterView)
    regexRun: function () {
      var ov = this.ov, text = ov.content.text, out = { matches: [], error: null, replaced: null };
      if (!ov.pattern) return out;
      var re;
      try {
        re = new RegExp(ov.pattern, "gu" + (ov.flags.i ? "i" : "") + (ov.flags.m ? "m" : "") + (ov.flags.s ? "s" : ""));
      } catch (e) { out.error = this.t("badRegex"); return out; }
      var m, guard = 0;
      re.lastIndex = 0;
      while ((m = re.exec(text)) && guard++ < 500) {
        out.matches.push(m);
        if (m[0] === "") re.lastIndex++;
      }
      if (ov.replacement) out.replaced = text.replace(re, ov.replacement.replace(/\$0/g, "$$&"));
      return out;
    },
    // A match in the list: "2026-09-29 · year = 2026 · $2 = 09" (RegexTester.describe)
    describe: function (m, names) {
      var parts = [m[0] === "" ? this.t("empty") : m[0]];
      for (var g = 1; g < m.length; g++) parts.push((names[g - 1] || "$" + g) + " = " + (m[g] === undefined ? this.t("noMatch") : m[g]));
      return parts.join(" · ");
    },
    card_regex: function () {
      var ov = this.ov, r = this.regexRun(), text = ov.content.text, self = this;
      ov.result = r;
      var sub = r.error ? this.t("badRegex") : ov.pattern ? fmt(this.t("nMatches"), r.matches.length) : "";
      var hl = "", last = 0;
      r.matches.forEach(function (m, i) {
        if (!m[0]) return;
        hl += esc(text.slice(last, m.index)) + '<mark class="' + (i % 2 ? "o" : "y") + '">' + esc(m[0]) + "</mark>";
        last = m.index + m[0].length;
      });
      hl += esc(text.slice(last));
      var menu = ov.menu === "presets" ? '<div class="pp-menu pp-menu-r" role="menu">' + this.s.rp.map(function (name, i) {
        return '<button type="button" role="menuitem" data-a="preset" data-arg="' + i + '" data-k="p' + i + '">' + esc(name) + "</button>";
      }).join("") + "</div>" : "";
      var check = function (f, label) {
        return '<label class="pp-check"><input type="checkbox" data-f="' + f + '" data-k="f' + f + '"' + (ov.flags[f] ? " checked" : "") + "><span>" + esc(label) + "</span></label>";
      };
      var html = '<div class="pp-fieldrow"><input type="text" class="pp-field pp-mono" data-in="pattern" data-k="pattern" data-autofocus spellcheck="false" autocomplete="off" aria-label="' +
        esc(this.t("regexPh")) + '" placeholder="' + esc(this.t("regexPh")) + '" value="' + esc(ov.pattern) + '"><div class="pp-menuwrap"><button type="button" class="pp-popup" data-a="menu" data-arg="presets" data-menu data-k="presets" aria-haspopup="menu" aria-expanded="' +
        (ov.menu === "presets") + '">' + esc(this.t("presets")) + I.chev + "</button>" + menu + "</div></div>" +
        '<div class="pp-checks">' + check("i", this.t("ignoreCase")) + check("m", this.t("multiline")) + check("s", this.t("dotAll")) + "</div>" +
        '<div class="pp-mono pp-preview pp-scroll" data-scroll="pv">' + hl + "</div>";
      if (r.error) html += '<p class="pp-err">' + esc(r.error) + "</p>";
      else if (r.matches.length) {
        var names = groupNames(ov.pattern);
        html += '<ol class="pp-matches pp-scroll" data-scroll="ml">' + r.matches.slice(0, 50).map(function (m, i) {
          return '<li><span class="pp-mn">' + (i + 1) + '</span><span class="pp-mono">' + esc(self.describe(m, names)) + "</span></li>";
        }).join("") + "</ol>";
      }
      html += '<input type="text" class="pp-field pp-field-soft pp-mono" data-in="replacement" data-k="replacement" spellcheck="false" autocomplete="off" aria-label="' +
        esc(this.t("replacePh")) + '" placeholder="' + esc(this.t("replacePh")) + '" value="' + esc(ov.replacement) + '">';
      if (r.replaced !== null) html += '<p class="pp-mono pp-replaced">' + esc(r.replaced) + "</p>";
      var b = [this.btn(this.t("copyMatches"), "copyMatches", { disabled: !r.matches.length }), this.btn(this.t("copyExpr"), "copyExpr", { disabled: !ov.pattern })];
      if (r.replaced !== null) b.push(this.btn(this.t("copyReplaced"), "copyReplaced"), this.btn(this.t("replace"), "replaceRegex"));
      return { title: this.t("regex"), subtitle: sub, width: 520, html: html + this.flow(b) };
    },

    // AI (AICardView)
    aiAnswer: function (i) {
      var a = AI[this.lang], id = this.ov.content.id;
      if (id && a[id] && this.texts[id] === this.orig[id]) return a[id][i];
      if (i === 0) return this.ov.content.text;
      return a.other;
    },
    card_ai: function () {
      var ov = this.ov, s = this.s, self = this;
      var acts = s.aiActs.map(function (label, i) {
        return self.btn(label, "aiRun", { arg: i, k: "ai" + i, cls: ov.active === i ? "is-tint" : "", title: "⌘" + (i + 1), pressed: ov.active === i });
      }).join("");
      var html = '<p class="pp-src pp-src2">' + esc(ov.content.text || this.t("nothing")) + '</p><div class="pp-acts">' + acts + "</div>" +
        '<input type="text" class="pp-field" data-in="question" data-k="question" autocomplete="off" aria-label="' + esc(this.t("askPh")) + '" placeholder="' + esc(this.t("askPh")) + '" value="' + esc(ov.question) + '"><hr>';
      if (ov.phase === "idle") html += '<p class="pp-note">' + esc(this.t("aiIdle")) + "</p>";
      else if (ov.phase === "running" && !ov.output) html += '<p class="pp-wait"><span class="pp-spin"></span>' + esc(this.t("thinking")) + "</p>";
      else html += '<div class="pp-body pp-ai-out pp-scroll" data-scroll="ai">' + md(ov.output) + "</div>";
      var b = [];
      if (ov.output && ov.phase !== "running") {
        b.push(this.btn(this.t("copy"), "copyAI"), this.btn(this.t("replace"), "replaceAI", { title: "⌘↩" }), this.btn(this.t("pin"), "pinAI"));
      }
      if (ov.phase === "running") b.push(this.btn(this.t("stop"), "aiStop"));
      else if (ov.label !== null) b.push(this.btn(this.t("regen"), "aiRegen"));
      b.push(this.more());
      return { title: "AI", subtitle: ov.label || "", width: 420, html: html + this.flow(b) };
    },
    aiStart: function (label, answer) {
      var ov = this.ov, self = this;
      clearInterval(ov.stream);
      ov.label = label; ov.output = ""; ov.phase = "running"; ov.answer = answer;
      this.renderCard();
      if (reduced()) { ov.output = answer; ov.phase = "done"; this.renderCard(); return; }
      var pos = 0, pieces = Array.from(answer);
      setTimeout(function () {
        if (self.ov !== ov || ov.phase !== "running") return;
        ov.stream = setInterval(function () {
          if (self.ov !== ov) { clearInterval(ov.stream); return; }
          pos = Math.min(pieces.length, pos + (self.lang === "zh" ? 2 : 4));
          ov.output = pieces.slice(0, pos).join("");
          if (pos >= pieces.length) { clearInterval(ov.stream); ov.phase = "done"; self.renderCard(); return; }
          var out = ov.el.querySelector(".pp-ai-out");
          if (out) { out.innerHTML = md(ov.output); self.placeCard(); } else self.renderCard();
        }, 30);
      }, 380);
    },

    // Clipboard History (ClipboardHistoryView)
    histItems: function () {
      var ov = this.ov, q = ov.query.trim().toLowerCase();
      var kinds = [null, "text", "image", "files", "pin"];
      return this.hist.filter(function (h) {
        var f = kinds[ov.filter];
        if (f === "pin" ? !h.pinned : f && h.kind !== f) return false;
        return !q || h.text.toLowerCase().indexOf(q) >= 0;
      });
    },
    ago: function (m) {
      if (m < 1) return this.t("now");
      return m === 1 ? this.t("minAgo1") : fmt(this.t("minAgo"), m);
    },
    card_history: function () {
      var ov = this.ov, s = this.s, self = this, items = this.histItems();
      ov.items = items;
      ov.hsel = clamp(ov.hsel, 0, Math.max(items.length - 1, 0));
      var q = ov.query.trim();
      var rows = items.map(function (h, i) {
        var n = ov.marked.indexOf(h.id), preview;
        if (h.kind === "image") {
          preview = '<span class="pp-thumb" aria-hidden="true"></span><span class="pp-hv"><span class="pp-cap0">' + esc(fmt(self.t("imageSize"), h.size)) + "</span>" +
            (q ? '<span class="pp-cap1">' + esc(fmt(self.t("imageHas"), h.text)) + "</span>" : "") + "</span>";
        } else if (h.kind === "files") preview = '<span class="pp-fi">' + I.doc + "</span><span>" + esc(h.text) + "</span>";
        else preview = "<span>" + esc(h.text) + "</span>";
        return '<li role="option" id="' + self.uid + "-h" + i + '" aria-selected="' + (i === ov.hsel) + '" class="pp-hrow' + (i === ov.hsel ? " is-sel" : "") + '" data-a="hpick" data-arg="' + i + '">' +
          (n >= 0 ? '<span class="pp-badge">' + (n + 1) + "</span>" : "") +
          '<span class="pp-hp">' + preview + "</span>" +
          '<span class="pp-hm">' + (h.pinned ? '<span class="pp-pinned">' + I.pinFill + "</span>" : "") + "<span>" + esc(self.ago(h.min)) + "</span>" + (i < 9 ? "<span>⌘" + (i + 1) + "</span>" : "") + "</span></li>";
      }).join("");
      var seg = '<div class="pp-seg pp-seg-l" role="group">' + s.filters.map(function (f, i) {
        return '<button type="button" data-a="hfilter" data-arg="' + i + '" data-k="hf' + i + '" aria-pressed="' + (ov.filter === i) + '"' + (ov.filter === i ? ' class="is-on"' : "") + ">" + esc(f) + "</button>";
      }).join("") + "</div>";
      var html = '<input type="text" class="pp-field" data-in="query" data-k="hq" data-autofocus autocomplete="off" role="combobox" aria-expanded="true" aria-controls="' + this.uid + '-hl" aria-activedescendant="' +
        (items.length ? this.uid + "-h" + ov.hsel : "") + '" aria-label="' + esc(this.t("searchPh")) + '" placeholder="' + esc(this.t("searchPh")) + '" value="' + esc(ov.query) + '">' + seg +
        '<div class="pp-list-wrap"><ul class="pp-list pp-scroll" id="' + this.uid + '-hl" role="listbox" data-scroll="hl" aria-label="' + esc(this.t("history")) + '">' + rows + "</ul>" +
        (items.length ? "" : '<p class="pp-empty">' + esc(this.t("noItems")) + "</p>") + "</div>" +
        '<p class="pp-hint' + (ov.marked.length ? " is-accent" : "") + '">' + esc(ov.marked.length ? fmt(this.t("hMarked"), ov.marked.length) : this.t("hHint")) + "</p>";
      return { title: this.t("history"), subtitle: items.length ? fmt(this.t("nItems"), items.length) : "", width: 460, html: html };
    },
    histPaste: function (items) {
      var text = items.map(function (h) { return h.text; }).join("\n");
      var self = this;
      this.close();
      if (this.sel) this.replace(text);
      else this.toast(this.t("tPasted"));
      items.forEach(function (h) { h.min = 0; });
      items.slice().reverse().forEach(function (h) { var i = self.hist.indexOf(h); self.hist.splice(i, 1); self.hist.unshift(h); });
    },

    // All Actions (PluginChooserView)
    chooserItems: function () {
      var ov = this.ov, s = this.s, q = ov.query.trim().toLowerCase();
      return this.actionList(ov.content).filter(function (a) {
        var info = s.acts[a];
        return !q || info[0].toLowerCase().indexOf(q) >= 0 || info[1].toLowerCase().indexOf(q) >= 0 || a.toLowerCase().indexOf(q) >= 0;
      });
    },
    card_chooser: function () {
      var ov = this.ov, s = this.s, self = this, items = this.chooserItems();
      ov.items = items;
      ov.csel = clamp(ov.csel, 0, Math.max(items.length - 1, 0));
      var rows = items.map(function (a, i) {
        var info = s.acts[a], icon = I[{ ocr: "screenshotOCR", color: "pickColor" }[a] || a];
        return '<li role="option" id="' + self.uid + "-c" + i + '" aria-selected="' + (i === ov.csel) + '" class="pp-crow' + (i === ov.csel ? " is-sel" : "") + '" data-a="cpick" data-arg="' + i + '">' +
          '<span class="pp-ci">' + icon + '</span><span class="pp-ct"><span>' + esc(info[0]) + '</span><span class="pp-cap0">' + esc(info[1]) + "</span></span>" +
          (i < 9 ? '<span class="pp-ck">⌘' + (i + 1) + "</span>" : "") + "</li>";
      }).join("");
      var html = '<input type="text" class="pp-field" data-in="cquery" data-k="cq" data-autofocus autocomplete="off" role="combobox" aria-expanded="true" aria-controls="' + this.uid + '-cl" aria-activedescendant="' +
        (items.length ? this.uid + "-c" + ov.csel : "") + '" aria-label="' + esc(this.t("chooserPh")) + '" placeholder="' + esc(this.t("chooserPh")) + '" value="' + esc(ov.query) + '">' +
        '<div class="pp-list-wrap"><ul class="pp-list pp-clist pp-scroll" id="' + this.uid + '-cl" role="listbox" data-scroll="cl" aria-label="' + esc(this.t("chooser")) + '">' + rows + "</ul>" +
        (items.length ? "" : '<p class="pp-empty">' + esc(this.t("noActions")) + "</p>") + "</div>";
      return { title: this.t("chooser"), subtitle: this.t("chooserSub"), width: 380, html: html };
    },

    // -------------------------------------------------------------- card events
    onCardClick: function (e) {
      var t = e.target.closest("[data-a]");
      if (!t || !this.ov || t.disabled) return;
      var ov = this.ov, a = t.getAttribute("data-a"), arg = t.getAttribute("data-arg"), self = this;
      var anchor = { x: ov.x, y: ov.y };
      switch (a) {
        case "close": this.close(); break;
        case "more": this.openCard("chooser", anchor, { focus: true }); break;
        case "toast": this.toast(this.t(arg)); break;
        case "copyRow": this.close(); this.copy(ov.rows[+arg][1]); break;
        case "replaceRow": this.close(); this.replace(ov.rows[+arg][1]); break;
        case "copyBody": this.close(); this.copy(ov.body); break;
        case "replaceBody": this.close(); this.replace(ov.body); break;
        case "copyMin": this.close(); this.copy(ov.min); break;
        case "menu": ov.menu = ov.menu === arg ? null : arg; this.renderCard(); if (ov.menu) this.focusMenu(); break;
        case "target":
          ov.menu = null; ov.target = arg; ov.done = {};
          var eng = ov.mode === "compare" ? ["system", "ai", "deepl"] : [ov.mode];
          this.fetch(eng);
          var lb = ov.el.querySelector('[data-k="lang"]');
          if (lb) lb.focus({ preventScroll: true });
          break;
        case "mode": ov.mode = arg; this.fetch(arg === "compare" ? ["system", "ai", "deepl"] : [arg]); this.renderCard(); break;
        case "copyTr": this.close(); this.copy(this.trText(arg)); break;
        case "replaceTr": this.close(); this.replace(this.trText(arg)); break;
        case "pinTr": this.close(); this.pin(this.trText(arg)); break;
        case "speakTr":
          try {
            var u = new SpeechSynthesisUtterance(this.trText(arg));
            u.lang = ov.target;
            speechSynthesis.cancel(); speechSynthesis.speak(u);
          } catch (err) { /* no voice */ }
          break;
        case "preset": ov.menu = null; ov.pattern = REGEX_PRESETS[+arg]; this.renderCard(); var pf = ov.el.querySelector('[data-k="pattern"]'); if (pf) pf.focus({ preventScroll: true }); break;
        case "copyMatches": this.close(); this.copy(ov.result.matches.map(function (m) { return m[0]; }).join("\n")); break;
        case "copyExpr": this.close(); this.copy(ov.pattern); break;
        case "copyReplaced": this.close(); this.copy(ov.result.replaced); break;
        case "replaceRegex": this.close(); this.replace(ov.result.replaced); break;
        case "aiRun": ov.active = +arg; this.aiStart(this.s.aiActs[+arg], this.aiAnswer(+arg)); break;
        case "aiStop": clearInterval(ov.stream); ov.phase = ov.output ? "done" : "idle"; this.renderCard(); break;
        case "aiRegen": this.aiStart(ov.label, ov.answer); break;
        case "copyAI": this.close(); this.copy(ov.output); break;
        case "replaceAI": this.close(); this.replace(ov.output); break;
        case "pinAI": this.close(); this.pin(ov.output); break;
        case "hfilter": ov.filter = +arg; ov.hsel = 0; this.renderCard(); break;
        case "hpick":
          var h = ov.items[+arg];
          if (e.metaKey || e.ctrlKey) { this.toggleMark(h); ov.hsel = +arg; this.renderCard(); }
          else this.histPaste([h]);
          break;
        case "cpick": this.runChoice(+arg); break;
      }
      void self;
    },
    focusMenu: function () {
      var m = this.ov.el.querySelector(".pp-menu button:not([disabled])");
      if (m) m.focus({ preventScroll: true });
    },
    toggleMark: function (h) {
      if (!h || h.kind !== "text") return;
      var ov = this.ov, i = ov.marked.indexOf(h.id);
      if (i >= 0) ov.marked.splice(i, 1); else ov.marked.push(h.id);
    },
    runChoice: function (i) {
      var ov = this.ov, a = ov.items[i];
      if (!a) return;
      var anchor = { x: ov.x, y: ov.y };
      this.close(true);
      this.run(a === "ocr" ? "screenshotOCR" : a === "color" ? "pickColor" : a === "clipboard" ? "clipboard" : a, anchor, true);
    },

    onInput: function (e) {
      var t = e.target, ov = this.ov;
      if (!ov || ov.type !== "card" || !t.getAttribute) return;
      var k = t.getAttribute("data-in");
      if (!k) return;
      if (e.isComposing) return;  // wait for compositionend with Chinese input methods
      if (k === "pattern") ov.pattern = t.value;
      else if (k === "replacement") ov.replacement = t.value;
      else if (k === "question") { ov.question = t.value; return; }
      else if (k === "query") { ov.query = t.value; ov.hsel = 0; }
      else if (k === "cquery") { ov.query = t.value; ov.csel = 0; }
      this.renderCard();
    },
    onChange: function (e) {
      var t = e.target, ov = this.ov, f = t.getAttribute && t.getAttribute("data-f");
      if (!f || !ov) return;
      ov.flags[f] = t.checked;
      this.renderCard();
    },

    onKey: function (e) {
      var ov = this.ov, k = e.key;
      if (!ov) return;
      var cmd = e.metaKey || e.ctrlKey;
      if (k === "Escape") {
        if (ov.type === "card" && ov.menu) {
          var which = ov.menu;
          ov.menu = null; this.renderCard();
          var mb = ov.el.querySelector('[data-arg="' + which + '"][data-menu]');
          if (mb) mb.focus({ preventScroll: true });
        } else if (ov.type === "card" && ov.card === "history" && ov.marked.length) { ov.marked = []; this.renderCard(); }
        else this.close();
        e.preventDefault(); e.stopPropagation();
        return;
      }
      if (ov.type === "ring") {
        var i = ov.hover === null ? -1 : ov.hover, n = G.n, next = null;
        if (k === "ArrowRight" || k === "ArrowDown") next = ((i < 0 ? -1 : i) + 1 + n) % n;
        else if (k === "ArrowLeft" || k === "ArrowUp") next = ((i < 0 ? 0 : i) - 1 + n) % n;
        else if (k === "Home") next = 0;
        else if (k === "End") next = n - 1;
        if (next !== null) {
          e.preventDefault();
          this.setHover(next);
          this.focusRing(true);
        }
        return;
      }
      if (ov.menu) {
        if (k === "ArrowDown" || k === "ArrowUp") {
          var items = Array.prototype.filter.call(ov.el.querySelectorAll(".pp-menu button"), function (b) { return !b.disabled; });
          var at = items.indexOf(document.activeElement);
          var to = items[(at + (k === "ArrowDown" ? 1 : -1) + items.length) % items.length];
          if (to) to.focus({ preventScroll: true });
          e.preventDefault();
        }
        return;
      }
      if (ov.card === "history" || ov.card === "chooser") {
        var list = ov.items || [], selKey = ov.card === "history" ? "hsel" : "csel";
        if (k === "ArrowDown" || k === "ArrowUp") {
          ov[selKey] = clamp(ov[selKey] + (k === "ArrowDown" ? 1 : -1), 0, Math.max(list.length - 1, 0));
          this.renderCard();
          var row = ov.el.querySelector(".pp-list .is-sel");
          if (row && row.scrollIntoView) row.scrollIntoView({ block: "nearest" });
          e.preventDefault();
          return;
        }
        if (k === "Enter" && e.target.tagName === "INPUT") {
          e.preventDefault();
          if (ov.card === "chooser") this.runChoice(ov.csel);
          else if (ov.marked.length) this.histPaste(ov.marked.map(function (id) { return list.filter(function (h) { return h.id === id; })[0]; }).filter(Boolean));
          else if (list[ov.hsel]) this.histPaste([list[ov.hsel]]);
          return;
        }
        if (cmd && /^[1-9]$/.test(k)) {
          e.preventDefault();
          var idx = +k - 1;
          if (ov.card === "chooser") this.runChoice(idx);
          else if (list[idx]) this.histPaste([list[idx]]);
          return;
        }
        if (ov.card === "history" && cmd && (k === "p" || k === "P")) {
          e.preventDefault();
          if (list[ov.hsel]) { list[ov.hsel].pinned = !list[ov.hsel].pinned; this.renderCard(); }
          return;
        }
        if (ov.card === "history" && cmd && (k === "c" || k === "C") && ov.marked.length && !window.getSelection().toString()) {
          e.preventDefault();
          var text = ov.marked.map(function (id) { return list.filter(function (h) { return h.id === id; })[0]; }).filter(Boolean).map(function (h) { return h.text; }).join("\n");
          this.close();
          this.copy(text);
          return;
        }
      }
      if (ov.card === "ai" && k === "Enter" && e.target.getAttribute("data-in") === "question") {
        e.preventDefault();
        var q = ov.question.trim();
        if (!q) return;
        ov.active = null; ov.question = "";
        this.aiStart(q, AI[this.lang].ask);
        return;
      }
      if (ov.card === "ai" && cmd && /^[1-4]$/.test(k)) {
        e.preventDefault();
        ov.active = +k - 1;
        this.aiStart(this.s.aiActs[+k - 1], this.aiAnswer(+k - 1));
      }
    }
  };

  function init() {
    Array.prototype.forEach.call(document.querySelectorAll("figure.ppd:not(.ppd-ready)"), function (el) {
      try { new Demo(el); } catch (err) { if (window.console) console.error(err); }
    });
  }
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", init);
  else init();
})();
