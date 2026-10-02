"""Plugin pages: files and system plugins. See __init__.py and the README ("Plugin pages")."""
from . import T


# Small pieces shared by the entries below: line icons for list rows, a row of buttons inside a
# card's body (for buttons that change with a pane, as Pop's “Copy <tab>” does), a page preview.
def _svg(body, extra=""):
    return ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" '
            f'stroke-linejoin="round"{extra}>{body}</svg>')


ICON_PHONE = _svg('<rect x="7" y="2.8" width="10" height="18.4" rx="2.4"/><path d="M10.6 5.6h2.8"/>')
ICON_LAPTOP = _svg('<rect x="4.6" y="5" width="14.8" height="10.4" rx="1.6"/><path d="M2.6 18.6h18.8"/>')
ICON_TABLET = _svg('<rect x="4.4" y="3" width="15.2" height="18" rx="2.4"/><path d="M11 18h2"/>')
ICON_DONE = _svg('<circle cx="12" cy="12" r="9"/><path d="m8 12.4 2.8 2.8 5.6-5.8"/>', ' style="color:var(--pl-green)"')


def _btns(*labels, tint=None):
    """A row of buttons inside the card's body (engine classes; click them with btn:B.N)."""
    if isinstance(labels[0], T):
        return T(_btns(*[x[0] if isinstance(x, T) else x for x in labels], tint=tint),
                 _btns(*[x[1] if isinstance(x, T) else x for x in labels], tint=tint))
    return ('<div class="pl-flow">' + "".join(f'<span class="pl-btn{" is-tint" if i == tint else ""}">{x}</span>'
                                             for i, x in enumerate(labels)) + "</div>")


_DOC = '<i class="t"></i><i class="l1"></i><i class="l2"></i><i class="l3"></i><i class="l4"></i><i class="l5"></i><i class="l6"></i>'
_NUM_AT = {"bc": "left:0;right:0;bottom:6px;text-align:center", "br": "right:9px;bottom:6px", "tr": "right:9px;top:5px"}


def _page(num, at, notes):
    """PDF page numbers: a small page (white paper in both themes) with its number, and notes beside it."""
    return ('<div style="display:flex;gap:14px;align-items:center">'
            '<div style="position:relative;width:78px;height:104px;flex:none;border-radius:3px;overflow:hidden;'
            'box-shadow:0 0 0 0.5px var(--pl-sep),0 2px 6px rgba(0,0,0,0.18)">'
            f'<span class="pl-art pl-art-doc" style="position:absolute;inset:0">{_DOC}</span>'
            f'<b style="position:absolute;{_NUM_AT[at]};font:600 8px var(--pl-mono);color:#3d4250">{num}</b></div>'
            '<div style="display:flex;flex-direction:column;gap:5px">' + "".join(f'<p class="pl-note">{n}</p>' for n in notes) +
            "</div></div>")


def _pages(num, at):
    return T(_page(num, at, ["12 pages; numbers go on pages 1–12", "Start on page 1 · First number: 1",
                             "Saves a copy; the original PDF stays as it is"]),
             _page(num, at, ["共 12 页，标在第 1～12 页", "从第 1 页开始标 · 第一个页码写 1", "另存一份，原来的 PDF 不动"]))


# Subtitles: the first lines, before and after shifting and cleaning up.
_SUB_LINES = [(T("[Door creaks]", "[开门声]")), T("<i>Where were you last night?</i>", "<i>你昨晚去哪儿了？</i>"),
              T("I was at the station.", "我在车站。"), T("(laughs) You’re a terrible liar.", "(笑) 你真不会撒谎。"),
              T("Fine. I was at the river.", "好吧，我在河边。")]


def _cues(times, lines):
    return {"t": "rows", "mono": False, "copy": False, "rows": [[t, x] for t, x in zip(times, lines)]}


# Disk Usage: one bar per item (blocks 2–6), its share of the folder; _slide changes them in place.
def _usage(rows, total):
    return [{"t": "bar", "label": name, "right": size, "to": round(gb / total, 3), "dur": 800} for name, gb, size in rows]


def _slide(rows, total):
    out = []
    for i, (name, gb, size) in enumerate(rows):
        b = f'.pl-card [data-b="{2 + i}"]'
        out += [["text", b + " .pl-prog-h > span:first-child", name], ["text", b + " .pl-prog-r", size], ["prop", 2 + i, "--v", round(gb / total, 3)]]
    return out


_DOCS = [[T("Videos", "视频"), 18.4, "18.4 GB"], [T("Projects", "项目"), 9.7, "9.7 GB"], [T("Old backups", "旧备份"), 6.2, "6.2 GB"],
         [T("Photos export.zip", "照片导出.zip"), 3.1, "3.1 GB"], [T("Scans", "扫描件"), 1.2, "1.2 GB"]]
_VIDEOS = [[T("Japan trip.mov", "日本旅行.mov"), 6.8, "6.8 GB"], [T("Wedding.mov", "婚礼.mov"), 4.9, "4.9 GB"],
           [T("Screen recordings", "屏幕录制"), 3.2, "3.2 GB"], [T("Drone", "航拍"), 2.6, "2.6 GB"], ["GoPro", 0.9, "0.9 GB"]]


DATA = {
    "tidyFolder": {
        "chips": [T("By type", "按类型"), T("By month", "按月份"), T("Undo", "可以撤销")],
        "points": [
            T("Sort the files at the top of <b>Downloads</b>, or the folder you select, into Images, Videos, Audio, Documents, Archives, Installers and Other.",
              "把「<b>下载</b>」（或者选中的文件夹）第一层的文件归到「图像」「视频」「音频」「文档」「压缩包」「安装包」「其他」里。"),
            T("Or by the month they were added, and photos and videos <b>by the date they were taken</b>.",
              "也可以按放进来的月份归，照片和视频还能<b>按拍摄日期</b>归。"),
            T("The card shows how many files go into each folder first; nothing moves until you click Tidy.",
              "卡片上先列出每个文件夹会放进几个文件，点「整理」才动。"),
            T("Folders, apps, hidden files and unfinished downloads stay where they are. <b>Undo</b> puts everything back.",
              "子文件夹、App、隐藏文件和没下载完的文件不动；整理完可以<b>撤销</b>，文件都挪回原处。"),
        ],
        "scene": {
            "src": {"kind": "files", "app": T("Downloads", "下载"), "sum": T("Downloads", "下载"), "cap": T("Open Downloads, or select a folder", "打开「下载」，或者选中一个文件夹"),
                    "sub": T("With nothing selected it tidies Downloads.", "什么都不选时整理的是「下载」。"),
                    "files": [{"name": "IMG_2041.HEIC", "kind": "photo", "art": "sunset"}, {"name": "invoice-0930.pdf"}, {"name": "Song.m4a", "kind": "audio"},
                              {"name": "Clip.mov", "kind": "video", "art": "waves"}, {"name": "Report.docx"}, {"name": "Setup.dmg"},
                              {"name": "Archive.zip", "kind": "zip"}, {"name": "Screenshot.png", "kind": "photo", "art": "screen"}, {"name": "data.csv"}]},
            "card": {"w": 330, "sub": T("Downloads · 9 files", "下载 · 9 个文件"), "btns": [T("Tidy", "整理")], "tint": 0,
                     "body": [{"t": "seg", "items": [T("By type", "按类型"), T("By month", "按月份"), T("By date taken", "按拍摄日期")], "on": 0},
                              {"t": "list", "dense": True, "items": [
                                  {"file": {"kind": "folder"}, "title": T("Images", "图像"), "right": "2"},
                                  {"file": {"kind": "folder"}, "title": T("Videos", "视频"), "right": "1"},
                                  {"file": {"kind": "folder"}, "title": T("Audio", "音频"), "right": "1"},
                                  {"file": {"kind": "folder"}, "title": T("Documents", "文档"), "right": "3"},
                                  {"file": {"kind": "folder"}, "title": T("Archives", "压缩包"), "right": "1"},
                                  {"file": {"kind": "folder"}, "title": T("Installers", "安装包"), "right": "1"}]}]},
            "steps": [
                {"cap": T("See where each file will go", "先看每个文件会去哪"), "acts": []},
                {"cap": T("Click Tidy", "点「整理」"), "sub": T("Undo puts everything back.", "可以撤销，文件都挪回原处。"),
                 "acts": [["click", "btn:0"], ["close"],
                          ["grid", [{"name": T("Images", "图像"), "kind": "folder"}, {"name": T("Videos", "视频"), "kind": "folder"},
                                    {"name": T("Audio", "音频"), "kind": "folder"}, {"name": T("Documents", "文档"), "kind": "folder"},
                                    {"name": T("Archives", "压缩包"), "kind": "folder"}, {"name": T("Installers", "安装包"), "kind": "folder"}]]]},
            ],
        },
    },
    "folderTree": {
        "chips": [T("Tree or Markdown", "树形或 Markdown"), "├── └──", T("Up to 3 levels", "最多展开 3 层")],
        "points": [
            T("Select a folder and Pop writes out what’s inside as a <b>tree</b> (├── └──) or a Markdown list, ready to paste into docs, a README or a message.",
              "选中一个文件夹，Pop 把里面的目录结构写成<b>树形</b>（├── └──）或者 Markdown 列表，贴进文档、README 或者发给别人。"),
            T("Folders come first, it goes up to 3 levels deep, and hidden files aren’t listed.", "文件夹排在前面，最多展开 3 层，隐藏文件不列。"),
            T("Folders such as node_modules, build and Pods are <b>listed by name only</b>, with “…” when they aren’t empty.",
              "node_modules、build、Pods 这类依赖和编译产物的文件夹<b>只列名字</b>，里面有东西时后面加「…」。"),
            T("The card says how many folders and files it found; copy the one you want.", "卡片上写着一共几个文件夹、几个文件，要哪种复制哪种。"),
        ],
        "scene": {
            "src": {"kind": "files", "app": T("Projects", "项目"), "cap": T("Select a folder in Finder", "在访达里选中一个文件夹"),
                    "files": [{"name": "my-app", "kind": "folder", "sel": True}, {"name": "website", "kind": "folder"},
                              {"name": T("Ideas.md", "想法.md")}, {"name": "logo.png", "kind": "photo", "art": "logo"}]},
            "card": {"w": 340, "body": [
                {"t": "seg", "items": [T("Tree", "树形"), T("Markdown List", "Markdown 列表")], "on": 0, "ctl": 1},
                {"t": "panes", "panes": [
                    [{"t": "code", "lang": "plain", "text": "my-app/\n├── node_modules/ …\n├── src/\n│   ├── components/\n│   │   ├── Button.tsx\n│   │   └── Header.tsx\n│   ├── App.tsx\n│   └── main.tsx\n├── package.json\n├── README.md\n└── tsconfig.json"},
                     {"t": "note", "text": T("3 folders, 7 files; up to 3 levels deep, hidden files not listed", "3 个文件夹，7 个文件；最多展开 3 层，隐藏文件不列出")},
                     {"t": "html", "html": _btns(T("Copy Tree", "复制 树形"), tint=0)}],
                    [{"t": "code", "lang": "plain", "text": "- my-app/\n  - node_modules/ …\n  - src/\n    - components/\n      - Button.tsx\n      - Header.tsx\n    - App.tsx\n    - main.tsx\n  - package.json\n  - README.md\n  - tsconfig.json"},
                     {"t": "note", "text": T("3 folders, 7 files; up to 3 levels deep, hidden files not listed", "3 个文件夹，7 个文件；最多展开 3 层，隐藏文件不列出")},
                     {"t": "html", "html": _btns(T("Copy Markdown List", "复制 Markdown 列表"), tint=0)}],
                ]}]},
            "steps": [
                {"cap": T("The tree is written out", "目录结构写好了"), "sub": T("node_modules is listed by name only.", "node_modules 只列名字。"), "acts": [], "hold": 1500},
                {"cap": T("Copy it", "复制下来"), "sub": T("Paste it into a README or a message.", "贴进 README 或者发给别人。"),
                 "acts": [["click", "btn:1.0", ["toast", T("Copied", "已复制")]]]},
                {"cap": T("Or make it a Markdown list", "或者换成 Markdown 列表"), "acts": [["click", "opt:0.1"], ["wait", 600], ["move", "btn:1.0"]]},
            ],
        },
    },
    "codeStats": {
        "chips": [T("Lines per language", "按语言数行数"), T("Markdown table", "Markdown 表格"), T("Skips node_modules", "不算 node_modules")],
        "points": [
            T("Select one or more folders and Pop counts the <b>code files and lines per language</b>, blank lines too, most lines first.",
              "选中一个或几个文件夹，Pop 按语言统计<b>代码文件数和行数</b>，空行也单独数出来，行数多的排在前面。"),
            T("Hidden folders such as .git, dependencies and build output such as node_modules, lock files and minified .min.js files aren’t counted.",
              "隐藏文件夹（.git 这些）、node_modules 这类依赖和编译产物、锁文件、压缩过的 .min.js 都不算。"),
            T("Files that are too large or aren’t text are skipped, and the card says how many.", "太大或者不是文字的文件跳过，卡片上写着跳过了几个。"),
            T("Copy it all as a <b>Markdown table</b>: files, lines, blank lines and code lines for each language, with a total.",
              "可以复制成 <b>Markdown 表格</b>：每种语言的文件数、行数、空行和代码行，最后一行是合计。"),
        ],
        "scene": {
            "src": {"kind": "files", "app": T("Projects", "项目"), "cap": T("Select one or more folders", "选中一个或几个文件夹"),
                    "files": [{"name": "weather-app", "kind": "folder", "sel": True}, {"name": "website", "kind": "folder", "sel": True},
                              {"name": T("Ideas.md", "想法.md")}, {"name": "logo.png", "kind": "photo", "art": "logo"}]},
            "card": {"w": 340, "btns": [T("Copy", "复制")], "tint": 0,
                     "body": [{"t": "rows", "rows": [["Swift", T("8,412 lines, 64 files", "8,412 行，64 个文件")],
                                                     ["TypeScript", T("5,730 lines, 41 files", "5,730 行，41 个文件")],
                                                     ["CSS", T("2,106 lines, 15 files", "2,106 行，15 个文件")],
                                                     ["HTML", T("1,342 lines, 12 files", "1,342 行，12 个文件")],
                                                     ["Markdown", T("518 lines, 8 files", "518 行，8 个文件")],
                                                     ["Shell", T("96 lines, 3 files", "96 行，3 个文件")]]},
                              {"t": "note", "text": T("143 files, 18,204 lines (2,511 blank); hidden folders and dependencies such as node_modules aren’t counted",
                                                      "143 个文件，18,204 行（空行 2,511 行）；不算隐藏文件夹和 node_modules 这类依赖")}]},
            "steps": [
                {"cap": T("Lines per language", "按语言列出行数"), "sub": T("Most lines first.", "行数多的排在前面。"), "acts": [["hover", "row:0.0"]], "hold": 1600},
                {"cap": T("Copy it as a Markdown table", "复制成 Markdown 表格"), "sub": T("Files, lines, blank and code lines, and a total.", "文件数、行数、空行、代码行，还有合计。"),
                 "acts": [["click", "btn:0", ["toast", T("Copied", "已复制")]]]},
            ],
        },
    },
    "compareFiles": {
        "chips": [T("Line by line", "逐行对比"), T("Changed words marked", "改动逐词标出"), T("Older one first", "旧的当原文")],
        "points": [
            T("Select two text files in Finder (code, Markdown, config, CSV…) and see the <b>removed and added lines</b>, with the changed words marked inside them.",
              "在访达里选中两个文本文件（代码、Markdown、配置、CSV……），看<b>删去和新增的行</b>，行里改了哪些词也标出来。"),
            T("The older file, by modification date, is the original.", "按修改时间，旧的那个当原文。"),
            T("Files saved as UTF-8, UTF-16 or GB18030 can all be read.", "UTF-8、UTF-16 和 GB18030 编码的文件都能读。"),
            T("Copy the differences as text. If the two files are the same, Pop just says so.", "差异可以复制下来；两个文件一样时直接提示「两个文件内容相同」。"),
        ],
        "scene": {
            "src": {"kind": "files", "app": "deploy", "cap": T("Select two text files", "选中两个文本文件"),
                    "files": [{"name": "settings-v1.yaml", "sel": True}, {"name": "settings-v2.yaml", "sel": True},
                              {"name": "README.md"}, {"name": "deploy.sh"}]},
            "card": {"w": 380, "btns": [T("Copy", "复制")],
                     "body": [{"t": "diff", "lines": [[" ", T("# Production", "# 正式环境")], [" ", "server:"],
                                                      ["-", "  port: {-8080-}"], ["+", "  port: {+3000+}"], [" ", "  host: 0.0.0.0"],
                                                      ["-", "  timeout: {-30-}s"], ["+", "  timeout: {+60+}s"], [" ", "logging:"],
                                                      ["-", "  level: {-debug-}"], ["+", "  level: {+info+}"], ["+", "  {+file: logs/app.log+}"]]},
                              {"t": "note", "text": T("“settings-v1.yaml” → “settings-v2.yaml” (older first): 3 lines removed, 4 added",
                                                      "「settings-v1.yaml」→「settings-v2.yaml」（旧的在前）：删去 3 行，新增 4 行")}]},
            "steps": [
                {"cap": T("Changed lines and words are marked", "改动的行和词都标出来了"), "sub": T("The older file is the original.", "按修改时间，旧的当原文。"),
                 "acts": [], "hold": 2200},
                {"cap": T("Copy the differences", "复制差异"), "acts": [["click", "btn:0", ["toast", T("Copied", "已复制")]]]},
            ],
        },
    },
    "batchRename": {
        "chips": [T("Numbering", "编号"), T("Find and replace", "替换文字"), T("Capture date", "按拍摄时间")],
        "points": [
            T("Rename the selected files together: <b>numbering</b>, find and replace (regular expressions too), a prefix or suffix, the date a photo was taken, or upper and lower case.",
              "给选中的文件统一改名：<b>编号</b>、替换文字（可以用正则）、加前后缀、照片的拍摄时间，或者改大小写。"),
            T("Numbering can start at any number, with 1 to 4 digits: “Beach trip 01”, “Beach trip 02”…", "编号可以设从几开始、几位数：「海边旅行 01」「海边旅行 02」……"),
            T("Every new name is listed before anything changes; duplicates, names already in the folder and names with / are flagged.",
              "改之前先列出每个文件的新名字，重名的、文件夹里已经有的、名字里带 / 的都会标出来。"),
            T("If something fails halfway, every file goes back to its old name, and <b>Undo</b> works afterwards too.",
              "中途出错会全部改回去；改完也可以<b>撤销</b>。"),
        ],
        "scene": {
            "src": {"kind": "files", "app": T("Beach trip", "海边旅行"), "cap": T("Select the files in Finder", "在访达里选中要改名的文件"),
                    "files": [{"name": "IMG_4101.HEIC", "kind": "photo", "art": "beach", "sel": True},
                              {"name": "IMG_4102.HEIC", "kind": "photo", "art": "sunset", "sel": True},
                              {"name": "IMG_4107.HEIC", "kind": "photo", "art": "waves", "sel": True}]},
            "card": {"w": 380, "sub": T("3 files", "3 个文件"), "btns": [T("Rename", "重命名")], "tint": 0,
                     "body": [{"t": "chips", "items": [T("Numbering", "编号"), T("Replace Text", "替换文字"), T("Add Prefix/Suffix", "加前后缀"),
                                                       T("Capture Date", "拍摄时间"), T("Case", "大小写")], "on": [0]},
                              {"t": "field", "ph": T("Name (numbers are appended; optional)", "名字（后面接编号，可以不填）"), "value": ""},
                              {"t": "rows", "mono": False, "copy": False,
                               "rows": [["IMG_4101.HEIC", "→ 01.HEIC"], ["IMG_4102.HEIC", "→ 02.HEIC"], ["IMG_4107.HEIC", "→ 03.HEIC"]]},
                              {"t": "note", "text": T("Start at 1 · 2 digits · Renames 3 files", "从 1 开始 · 2 位 · 会改 3 个文件的名字")}]},
            "steps": [
                {"cap": T("Type a name; numbers follow", "写个名字，后面接编号"), "sub": T("The new names show up as you type.", "新名字边写边列出来。"),
                 "acts": [["type", 1, T("Beach trip", "海边旅行")],
                          ["set", 2, {"t": "rows", "mono": False, "copy": False,
                                      "rows": [["IMG_4101.HEIC", T("→ Beach trip 01.HEIC", "→ 海边旅行 01.HEIC")], ["IMG_4102.HEIC", T("→ Beach trip 02.HEIC", "→ 海边旅行 02.HEIC")],
                                               ["IMG_4107.HEIC", T("→ Beach trip 03.HEIC", "→ 海边旅行 03.HEIC")]]}]],
                 "hold": 1100},
                {"cap": T("Click Rename", "点「重命名」"), "sub": T("Undo puts the old names back.", "改完可以撤销。"),
                 "acts": [["click", "btn:0"], ["close"],
                          ["rename", [[0, T("Beach trip 01.HEIC", "海边旅行 01.HEIC")], [1, T("Beach trip 02.HEIC", "海边旅行 02.HEIC")],
                                      [2, T("Beach trip 03.HEIC", "海边旅行 03.HEIC")]]], ["wait", 500],
                          ["card", {"w": 300, "at": "center", "sub": T("3 files", "3 个文件"), "btns": [T("Show in Finder", "在访达中显示"), T("Undo", "撤销")],
                                    "body": [{"t": "list", "items": [{"icon": ICON_DONE, "title": T("Renamed 3 files", "已重命名 3 个文件")}]}]}]],
                 "hold": 1800},
            ],
        },
    },
    "zip": {
        "chips": [T("Compress to zip", "压缩成 zip"), T("Unzip", "解压"), T("Right next to them", "就在原来的文件夹")],
        "points": [
            T("Select files or folders and <b>Compress</b> puts them in a zip in the same folder, then selects it in Finder.",
              "选中文件或文件夹，用「<b>压缩</b>」打包成一个 zip，存在原来的文件夹里，并在访达里选中它。"),
            T("One item keeps its name, such as “Photos.zip”; several make “Archive.zip”, without the folder above them inside.",
              "只选了一个就用它的名字，比如「照片.zip」；选了好几个叫「归档.zip」，压缩包里不带上层目录。"),
            T("A single file or folder is compressed the way Finder does it, so it unzips just as it was.", "单个文件或文件夹和访达的「压缩」一样，解压后还是原来的样子。"),
            T("Select zip files and <b>Unzip</b> extracts each one into a folder with the same name next to it.", "选中 zip 文件，用「<b>解压</b>」解到旁边的同名文件夹里。"),
        ],
        "scene": {
            "src": {"kind": "files", "app": T("Trip plan", "旅行计划"), "cap": T("Select files or folders", "选中文件或文件夹"),
                    "files": [{"name": T("Itinerary.pdf", "行程.pdf"), "sel": True}, {"name": T("Hotel booking.pdf", "酒店预订.pdf"), "sel": True},
                              {"name": T("Map.png", "地图.png"), "kind": "photo", "art": "landscape", "sel": True}, {"name": T("Budget.csv", "预算.csv")}]},
            # Pop shows no card here: the zip appears in Finder with a short notice. The (invisible)
            # keys effect stands in for a card so the scene has something to start.
            "fx": {"name": "keys"},
            "steps": [
                {"cap": T("A zip appears next to them", "旁边多了一个 zip"), "sub": T("Several items make “Archive.zip”.", "选了好几个时叫「归档.zip」。"),
                 "acts": [["wait", 400], ["file", {"name": T("Archive.zip", "归档.zip"), "kind": "zip", "at": 3}],
                          ["toast", T("Compressed to Archive.zip", "已压缩成 归档.zip")], ["fx", "end"]], "hold": 1600},
            ],
        },
    },
    "openInTerminal": {
        "chips": [T("Folder → Terminal", "文件夹 → 终端"), T("Files open their folder", "选文件就开所在文件夹"), "zsh"],
        "points": [
            T("Select a folder in Finder and Pop opens it in <b>Terminal</b>, ready for your commands.", "在访达里选中一个文件夹，Pop 直接在<b>终端</b>里打开它，马上就能敲命令。"),
            T("Select a file and Terminal opens in the folder it’s in.", "选中的是文件时，打开它所在的文件夹。"),
            T("It uses the Terminal app that comes with macOS.", "用的是 macOS 自带的「终端」。"),
        ],
        "scene": {
            "src": {"kind": "files", "app": T("Projects", "项目"), "cap": T("Select a folder in Finder", "在访达里选中一个文件夹"),
                    "files": [{"name": "website", "kind": "folder", "sel": True}, {"name": "scripts", "kind": "folder"},
                              {"name": T("Ideas.md", "想法.md")}, {"name": "backup.zip", "kind": "zip"}]},
            "card": {"title": "website — -zsh — 80×24", "w": 400, "at": "center",
                     "body": [{"t": "code", "lang": "plain", "text": "Last login: Wed Oct  1 16:14:02 on ttys002\nada@MacBook-Air website % "}]},
            "steps": [
                {"cap": T("Terminal opens in that folder", "终端在这个文件夹里打开"), "acts": [], "hold": 1400},
                {"cap": T("Type your commands", "直接敲命令"), "sub": T("No cd needed.", "不用再 cd 过去。"),
                 "acts": [["set", 0, {"t": "code", "lang": "plain", "text": "Last login: Wed Oct  1 16:14:02 on ttys002\nada@MacBook-Air website % ls\nREADME.md  assets  index.html  package.json\nada@MacBook-Air website % "}],
                          ["wait", 900],
                          ["set", 0, {"t": "code", "lang": "plain", "text": "Last login: Wed Oct  1 16:14:02 on ttys002\nada@MacBook-Air website % ls\nREADME.md  assets  index.html  package.json\nada@MacBook-Air website % git status\nOn branch main\nnothing to commit, working tree clean\nada@MacBook-Air website % "}]],
                 "hold": 1800},
            ],
        },
    },
    "pdf": {
        "chips": [T("Combine into one PDF", "合成一个 PDF"), T("Page numbers", "加页码"), T("Password · Compress", "加密码 · 压缩")],
        "points": [
            T("Select images and PDFs and Pop <b>combines them into one PDF</b> in file name order, saved next to the first one.",
              "选中图片和 PDF，Pop 按文件名顺序<b>合成一个 PDF</b>，存在第一个文件旁边。"),
            T("With a single PDF, the card can save each page as an image, copy all its text, extract pages or split it, add page numbers, add or remove a password, or compress it.",
              "只选了一个 PDF 时，卡片上可以把每页存成图片、复制全部文字、取出几页或者拆成单页、加页码、加密码或者去掉密码、压缩。"),
            T("<b>Page numbers</b> come in four styles (1, Page 1, 1 / 12, - 1 -) at the bottom center, bottom right or top right; the cover can be skipped, and the little preview shows the result.",
              "<b>加页码</b>有「1」「第 1 页」「1 / 12」「- 1 -」四种样式，放在底部居中、右下角或右上角，封面可以不标，左边的小图就是加好的样子。"),
            T("For a scan, <b>Recognize Text</b> saves a copy that looks the same but can be searched and copied from, recognized on your Mac. The original is never changed.",
              "扫描件可以「<b>识别文字</b>」，在本机认出文字，另存一份看起来一样、能搜索和复制的 PDF；原文件都不动。"),
        ],
        "scene": {
            "src": {"kind": "files", "app": T("Contracts", "合同"), "cap": T("Select a PDF in Finder", "在访达里选中一个 PDF"),
                    "sub": T("Select images and PDFs together to combine them.", "图片和 PDF 一起选，就合成一个 PDF。"),
                    "files": [{"name": T("Lease 2026.pdf", "租房合同.pdf"), "sel": True}, {"name": T("Invoice.pdf", "发票.pdf")},
                              {"name": "Scan 01.jpg", "kind": "photo", "art": "doc"}, {"name": "Scan 02.jpg", "kind": "photo", "art": "doc"}]},
            "card": {"title": "PDF", "w": 380,
                     "btns": [T("Save Pages as Images", "每页存成图片"), T("Copy All Text", "复制全部文字"), T("Extract Pages…", "取出几页…"),
                              T("Add Page Numbers…", "加页码…"), T("Add Password…", "加密码…"), T("Compress", "压缩")],
                     "body": [{"t": "text", "text": T("Lease 2026.pdf", "租房合同.pdf")},
                              {"t": "note", "text": T("12 pages, 9860 characters", "12 页，9860 个字")}]},
            "steps": [
                {"cap": T("Everything you can do with it", "能做的都在卡片上"), "sub": T("Images, text, pages, numbers, password, compress.", "存图片、复制文字、取页、加页码、加密码、压缩。"),
                 "acts": [], "hold": 1500},
                {"cap": T("Add page numbers", "加页码"),
                 "acts": [["click", "btn:3", ["card", {"title": T("Add Page Numbers", "加页码"), "sub": T("Lease 2026.pdf", "租房合同.pdf"), "w": 380,
                                                       "btns": [T("Add Page Numbers", "加页码")], "tint": 0,
                                                       "body": [{"t": "html", "html": _pages("1", "bc")},
                                                                {"t": "seg", "label": T("Position", "位置"), "items": [T("Bottom Center", "底部居中"), T("Bottom Right", "右下角"), T("Top Right", "右上角")], "on": 0},
                                                                {"t": "seg", "label": T("Style", "样式"), "items": ["1", T("Page 1", "第 1 页"), "1 / 12", "- 1 -"], "on": 0}]}]]],
                 "hold": 700},
                {"cap": T("Pick the place and style", "选位置和样式"), "sub": T("The preview shows the result.", "小图就是加好以后的样子。"),
                 "acts": [["click", "opt:1.1", ["set", 0, {"t": "html", "html": _pages("1", "br")}]], ["wait", 500],
                          ["click", "opt:2.2", ["set", 0, {"t": "html", "html": _pages("1 / 12", "br")}]]], "hold": 900},
                {"cap": T("A numbered copy appears", "另存了一份带页码的"),
                 "acts": [["click", "btn:0"], ["close"], ["file", {"name": T("Lease 2026 numbered.pdf", "租房合同 页码.pdf"), "at": 1}],
                          ["toast", T("Saved “Lease 2026 numbered.pdf”", "加好了页码，存成了「租房合同 页码.pdf」")]], "hold": 1600},
            ],
        },
    },
    "videoConvert": {
        "chips": ["GIF · MP4 · 720p", T("Extract audio", "提取音频"), T("16-frame contact sheet", "16 帧缩略图")],
        "points": [
            T("Select videos and <b>convert them to GIF</b> or MP4, compress them to 720p, or extract the sound as M4A.",
              "选中视频，<b>转成 GIF</b> 或 MP4、压缩到 720p，或者把声音提取成 M4A。"),
            T("GIFs are 10 frames per second, at most 640 pixels wide, and loop; they cover up to the first 60 seconds.",
              "GIF 每秒 10 帧、宽度不超过 640、循环播放，最多转前 60 秒。"),
            T("A <b>contact sheet</b> puts 16 evenly spaced frames into one image.", "<b>拼缩略图</b>均匀取 16 帧，拼成一张图。"),
            T("Results are saved next to the originals and selected in Finder. With one video, the card shows its length, size and dimensions, and Trim… cuts out a part.",
              "结果存在原视频旁边，在访达里选中；只选了一个视频时，卡片上写着时长、画面和大小，还能「截取一段…」。"),
        ],
        "scene": {
            "src": {"kind": "files", "app": T("Movies", "影片"), "cap": T("Select a video in Finder", "在访达里选中一个视频"),
                    "files": [{"name": T("Surfing.mov", "冲浪.mov"), "kind": "video", "art": "waves", "sel": True},
                              {"name": T("Sunset.mp4", "日落.mp4"), "kind": "video", "art": "sunset"},
                              {"name": T("Birthday.mov", "生日.mov"), "kind": "video", "art": "city"}, {"name": T("Notes.txt", "笔记.txt")}]},
            "card": {"w": 380, "btns": [T("Convert to GIF", "转成 GIF"), T("Convert to MP4", "转成 MP4"), T("Compress to 720p", "压缩到 720p"),
                                        T("Extract Audio", "提取音频"), T("Contact Sheet", "拼缩略图"), T("Trim…", "截取一段…")], "tint": 0,
                     "body": [{"t": "text", "text": T("Surfing.mov", "冲浪.mov")},
                              {"t": "rows", "rows": [[T("Duration", "时长"), "0:42"], [T("Video", "画面"), "1920 × 1080"], [T("Size", "大小"), "86.4 MB"]]},
                              {"t": "note", "text": T("Saved next to the original video. GIFs are 10 fps, at most 640 wide, and cover up to the first 60 seconds",
                                                      "转换后存在原视频旁边；GIF 每秒 10 帧、宽度不超过 640，最多转前 60 秒")}]},
            "steps": [
                {"cap": T("Pick what to make", "选要转成什么"), "sub": T("GIF, MP4, 720p, audio or a contact sheet.", "GIF、MP4、720p、音频，或者拼缩略图。"), "acts": [], "hold": 1500},
                {"cap": T("Convert to GIF", "转成 GIF"), "sub": T("It’s saved next to the video and selected.", "存在原视频旁边，在访达里选中。"),
                 "acts": [["click", "btn:0"], ["close"], ["toast", T("Converting to GIF…", "正在转成 GIF…")],
                          ["file", {"name": T("Surfing.gif", "冲浪.gif"), "kind": "photo", "art": "waves", "at": 1}], ["toast", T("Converted to GIF", "已转成 GIF")]],
                 "hold": 1500},
            ],
        },
    },
    "trimMedia": {
        "chips": ["0:10-1:25", T("No re-encoding", "不重新编码"), T("Audio and video", "音频和视频")],
        "points": [
            T("Select an audio or video file, type the start and end, such as <b>0:10-1:25</b>, and Pop cuts out that part.",
              "选中一个音频或视频，写上开始和结束的时间，比如 <b>0:10-1:25</b>，Pop 就截出这一段。"),
            T("“1:25-” goes to the end and “-0:30” starts from the beginning; the card checks the times against the length as you type.",
              "「1:25-」是到结尾，「-0:30」是从头开始；边写边对着总时长检查。"),
            T("MP4, MOV and M4A are cut <b>without re-encoding</b>; MP3, WAV and the like are saved as M4A.", "MP4、MOV、M4A <b>原样截取，不重新编码</b>；MP3、WAV 这类存成 M4A。"),
            T("The clip is saved next to the original and selected in Finder. Convert Video’s card has Trim… too.",
              "截好的片段存在原文件旁边，在访达里选中；「视频转换」卡片上也有「截取一段…」。"),
        ],
        "scene": {
            "src": {"kind": "files", "app": T("Recordings", "录音"), "cap": T("Select a recording or a video", "选中一段录音或视频"),
                    "files": [{"name": T("Interview.m4a", "采访.m4a"), "kind": "audio", "sel": True}, {"name": T("Podcast draft.mp3", "播客草稿.mp3"), "kind": "audio"},
                              {"name": T("Meeting.m4a", "会议.m4a"), "kind": "audio"}, {"name": T("Talk.mov", "演讲.mov"), "kind": "video", "art": "city"}]},
            "card": {"title": T("Trim", "截取片段"), "sub": T("Interview.m4a", "采访.m4a"), "w": 360, "btns": [T("Trim to This Range", "截取这一段")], "tint": 0,
                     "body": [{"t": "field", "ph": T("Start–end, e.g. 0:10-1:25", "开始-结束，比如 0:10-1:25"), "value": "", "mono": True},
                              {"t": "note", "text": T("12:48 in total. Enter a start and end time, e.g. 0:10-1:25 (1:25- goes to the end).",
                                                      "一共 12:48。写上开始和结束的时间，比如 0:10-1:25（1:25- 是到结尾）")}]},
            "steps": [
                {"cap": T("Type the start and end", "写上开始和结束的时间"),
                 "acts": [["type", 0, "2:05-3:40"], ["text", '.pl-card [data-b="1"] p', T("From 2:05 to 3:40, 1:35 in total", "从 2:05 到 3:40，一共 1:35")]], "hold": 1000},
                {"cap": T("Trim to this range", "截取这一段"), "sub": T("The clip is saved next to the original.", "片段存在原文件旁边。"),
                 "acts": [["click", "btn:0"], ["close"], ["toast", T("Trimming…", "正在截取…")],
                          ["file", {"name": T("Interview Clip.m4a", "采访 片段.m4a"), "kind": "audio", "at": 1}], ["toast", T("Trimmed 1:35", "已截取 1:35")]],
                 "hold": 1500},
            ],
        },
    },
    "transcribe": {
        "chips": [".txt + .srt", T("Mandarin, English…", "普通话、英语……"), T("On your Mac", "在本机识别")],
        "points": [
            T("Select a recording or a video, choose the language spoken, and Pop turns the speech into <b>text and SRT subtitles</b>, saved next to the original.",
              "选中录音或视频，选说的是哪种话，Pop 把里面说的话转成<b>文字和 SRT 字幕</b>，存在原文件旁边。"),
            T("Mandarin, English, Cantonese and Japanese. When this Mac can recognize the language itself, the audio <b>stays on your Mac</b>.",
              "普通话、英语、粤语、日语都行；这台 Mac 能在本机识别时只在本机识别，<b>不上传音频</b>。"),
            T("Subtitles are split by sentences and pauses, with times. On macOS 26 it uses the system’s new transcription, which handles long recordings in full.",
              "字幕按句子和停顿分好条、带时间；macOS 26 上用系统新的转写，长录音也能完整识别。"),
            T("Both files are selected in Finder, and a card shows the text and the subtitles, ready to copy.", "两个文件在访达里选中，再弹出结果卡片，「文字」和「字幕 SRT」都能直接复制。"),
        ],
        "scene": {
            "src": {"kind": "files", "app": T("Podcast", "播客"), "cap": T("Select a recording or a video", "选中一段录音或视频"),
                    "files": [{"name": T("Episode 12.m4a", "第 12 期.m4a"), "kind": "audio", "sel": True}, {"name": T("Episode 11.m4a", "第 11 期.m4a"), "kind": "audio"},
                              {"name": T("Cover.png", "封面.png"), "kind": "photo", "art": "flower"}, {"name": T("Show notes.md", "节目笔记.md")}]},
            "card": {"w": 340, "btns": [T("English", "普通话"), T("Mandarin", "英语"), T("Cantonese", "粤语"), T("Japanese", "日语")], "tint": 0,
                     "body": [{"t": "text", "text": T("Which language is spoken?", "说的是哪种话？")},
                              {"t": "rows", "rows": [[T("File", "文件"), T("Episode 12.m4a", "第 12 期.m4a")], [T("Duration", "时长"), "18:42"]]},
                              {"t": "note", "text": T("When done, the text (.txt) and subtitles (.srt) are saved next to the original. Long recordings take a while.",
                                                      "识别完，文字（.txt）和字幕（.srt）存在原文件旁边；长录音要等一会儿")}]},
            "steps": [
                {"cap": T("Pick the language spoken", "选说的是哪种话"), "sub": T("Mandarin, English, Cantonese or Japanese.", "普通话、英语、粤语或者日语。"),
                 "acts": [["click", "btn:0"], ["close"], ["toast", T("Transcribing “Episode 12.m4a”…", "正在识别「第 12 期.m4a」里说的话…")]], "hold": 300},
                {"cap": T("Text and subtitles are saved", "文字和字幕存好了"), "sub": T("Right next to the recording.", "就在录音旁边。"),
                 "acts": [["file", {"name": T("Episode 12.srt", "第 12 期.srt"), "at": 1}], ["file", {"name": T("Episode 12.txt", "第 12 期.txt"), "at": 1}]],
                 "hold": 900},
                {"cap": T("Copy the text or the subtitles", "文字和字幕都能复制"),
                 "acts": [["card", {"w": 360, "body": [
                     {"t": "seg", "items": [T("Text", "文字"), T("SRT Subtitles", "字幕 SRT")], "on": 0, "ctl": 1},
                     {"t": "panes", "panes": [
                         [{"t": "text", "mono": True, "text": T("Welcome back to the show. Today we’re talking about small tools that save a lot of time. My guest has been making Mac apps for ten years…",
                                                                 "欢迎回来。今天聊聊能省下大把时间的小工具。今天的嘉宾做了十年 Mac App……")},
                          {"t": "note", "text": T("The text and subtitles were saved next to “Episode 12.m4a”", "文字和字幕已经存在「第 12 期.m4a」旁边")},
                          {"t": "html", "html": _btns(T("Copy Text", "复制 文字"))}],
                         [{"t": "text", "mono": True, "text": T("1\n00:00:00,000 --> 00:00:02,400\nWelcome back to the show.\n\n2\n00:00:02,400 --> 00:00:05,900\nToday we’re talking about small tools…",
                                                                 "1\n00:00:00,000 --> 00:00:01,600\n欢迎回来。\n\n2\n00:00:01,600 --> 00:00:05,200\n今天聊聊能省下大把时间的小工具。")},
                          {"t": "note", "text": T("The text and subtitles were saved next to “Episode 12.m4a”", "文字和字幕已经存在「第 12 期.m4a」旁边")},
                          {"t": "html", "html": _btns(T("Copy SRT Subtitles", "复制 字幕 SRT"))}],
                     ]}]}],
                          ["wait", 900], ["click", "opt:0.1"], ["wait", 500], ["click", "btn:1.0", ["toast", T("Copied", "已复制")]]], "hold": 1200},
            ],
        },
    },
    "airDrop": {
        "chips": [T("Files, links, text", "文件、链接、文字"), "iPhone · iPad · Mac", T("Nearby", "附近的设备")],
        "points": [
            T("Send the selected files, images, links or text to a <b>nearby iPhone, iPad or Mac</b> with AirDrop.",
              "用隔空投送把选中的文件、图片、链接或文字发到<b>附近的 iPhone、iPad 或 Mac</b>。"),
            T("It works in Finder and in other apps: select a picture, a link or some text and swipe to AirDrop.", "访达里、别的 App 里都能用：选中图片、链接或一段文字，划向「隔空投送」就行。"),
            T("If AirDrop can’t be used right now, Pop says to check that Wi-Fi and Bluetooth are on and AirDrop isn’t turned off.",
              "暂时用不了时，Pop 会提醒检查无线局域网和蓝牙有没有打开、「隔空投送」有没有被关闭。"),
        ],
        "scene": {
            "src": {"kind": "files", "app": T("Pictures", "图片"), "cap": T("Select what to send", "选中要发的东西"),
                    "sub": T("Files, images, a link or some text.", "文件、图片、链接或者一段文字。"),
                    "files": [{"name": T("Beach.heic", "海边.heic"), "kind": "photo", "art": "beach", "sel": True},
                              {"name": T("Sunset.heic", "日落.heic"), "kind": "photo", "art": "sunset", "sel": True},
                              {"name": T("Garden.jpg", "花园.jpg"), "kind": "photo", "art": "flower"}, {"name": T("Mug.png", "杯子.png"), "kind": "photo", "art": "mug"}]},
            "card": {"title": T("AirDrop", "隔空投送"), "w": 300, "at": "center",
                     "body": [{"t": "thumbs", "cols": 5, "items": [{"art": "beach"}, {"art": "sunset"}]},
                              {"t": "list", "items": [{"icon": ICON_PHONE, "title": T("Ada’s iPhone", "小林的 iPhone"), "sub": "iPhone"},
                                                      {"icon": ICON_LAPTOP, "title": T("Ben’s MacBook Air", "老王的 MacBook Air"), "sub": "MacBook Air"},
                                                      {"icon": ICON_TABLET, "title": T("Living Room iPad", "客厅的 iPad"), "sub": "iPad"}]}]},
            "steps": [
                {"cap": T("Nearby devices show up", "附近的设备都列出来了"), "sub": T("Pop opens the AirDrop window.", "Pop 打开隔空投送的窗口。"), "acts": [], "hold": 1200},
                {"cap": T("Click one to send", "点一个就发过去"),
                 "acts": [["click", "row:1.0"], ["wait", 300],
                          ["text", '.pl-card [data-b="1"] .pl-li small', T("Waiting…", "等待中…")], ["wait", 1300],
                          ["text", '.pl-card [data-b="1"] .pl-li small', T("Sent", "已发送")]],
                 "hold": 1600},
            ],
        },
    },
    "sendToPhone": {
        "chips": [T("Scan to download", "扫码就能下载"), T("Same Wi-Fi", "同一个 Wi-Fi"), T("Android too", "安卓也能用")],
        "points": [
            T("A <b>QR code</b> appears on the card: scan it with your phone’s camera to download the selected files or images in the browser, no app needed.",
              "卡片上出现一个<b>二维码</b>，用手机相机一扫，就能在浏览器里下载选中的文件和图片，不用装 App。"),
            T("Folders are zipped first; selected text shows up on the page, ready to copy with a long press.", "文件夹先打包成 zip；选中的是文字就直接显示在网页上，长按拷贝。"),
            T("The page can also <b>send files from the phone</b> to the Mac’s Downloads folder, with a notice for each one.",
              "网页上也能选手机里的文件<b>传到 Mac 的「下载」文件夹</b>，传来一个提示一次。"),
            T("The phone and Mac just need the same Wi-Fi; Android works too. Sharing goes on after you close the card, stops from the menu bar, and stops by itself after 10 minutes without access. The address includes a random key.",
              "手机和 Mac 连同一个 Wi-Fi 就行，安卓手机也能用。关掉卡片后继续共享，菜单栏里可以停止，10 分钟没人访问自动停止；网址里带一段随机口令。"),
        ],
        "scene": {
            "src": {"kind": "files", "app": T("Downloads", "下载"), "cap": T("Select what to send", "选中要传的文件"),
                    "sub": T("Or nothing, to receive files from the phone.", "什么都不选，就只从手机传过来。"),
                    "files": [{"name": T("Boarding pass.pdf", "登机牌.pdf"), "sel": True}, {"name": T("Beach.heic", "海边.heic"), "kind": "photo", "art": "beach", "sel": True},
                              {"name": T("Slides.key", "幻灯片.key")}, {"name": "Setup.dmg"}]},
            "card": {"w": 340, "at": "right", "btns": [T("Copy", "复制"), T("Stop Sharing", "停止共享")],
                     "body": [{"t": "qr", "text": "http://192.168.1.23:52817/k7m2xq9pda/"},
                              {"t": "text", "size": "s", "text": T("Scan with your phone’s camera and tap Download on the page to save to your phone. You can also send files from your phone.",
                                                                    "用手机相机扫码，在网页上点「下载」存到手机；也能从手机传文件过来")},
                              {"t": "rows", "rows": [[T("URL", "网址"), "http://192.168.1.23:52817/k7m2xq9pda/"],
                                                     [T("Available", "可以下载"), T("Boarding pass.pdf\nBeach.heic", "登机牌.pdf\n海边.heic")]]}]},
            "steps": [
                {"cap": T("Scan it with your phone", "用手机扫一扫"), "sub": T("Phone and Mac on the same Wi-Fi.", "手机和 Mac 连同一个 Wi-Fi。"),
                 "acts": [["wait", 1400], ["toast", T("Phone downloaded “Boarding pass.pdf”", "手机下载了「登机牌.pdf」")]], "hold": 600},
                {"cap": T("Send files from the phone too", "也能从手机传过来"), "sub": T("They land in Downloads.", "存进「下载」文件夹。"),
                 "acts": [["wait", 500], ["file", {"name": "IMG_4012.HEIC", "kind": "photo", "art": "flower", "at": 0}],
                          ["toast", T("Received “IMG_4012.HEIC” in Downloads", "收到「IMG_4012.HEIC」，在「下载」文件夹里")]], "hold": 700},
                {"cap": T("Stop sharing when you’re done", "传完点「停止共享」"), "sub": T("Or from the menu bar later.", "也可以以后在菜单栏里停止。"),
                 "acts": [["click", "btn:1"], ["close"]], "hold": 1200},
            ],
        },
    },
    "folderTools": {
        "chips": [T("Disk Usage", "占用空间"), T("Find Duplicates", "查找重复文件"), T("Compare Folders", "比较文件夹")],
        "points": [
            T("Three tools for folders. <b>Disk Usage</b> shows how much each item in a folder takes and its share of the total; click a folder to look inside, or list the largest files.",
              "三个管文件夹的工具。<b>占用空间</b>：看文件夹里每一项占多少、占总共的多大比例，点文件夹进去看下一层，也能直接列出最大的文件。"),
            T("<b>Find Duplicates</b> finds files with identical contents, even under different names, keeps one of each and moves the rest to the Trash.",
              "<b>查找重复文件</b>：找出内容完全一样的文件，名字不一样也认得出来，每组只留一个，其余移到废纸篓。"),
            T("<b>Compare Folders</b>: with two folders selected, it lists the files that are only on one side and the ones that differ, subfolders included.",
              "<b>比较文件夹</b>：正好选中两个文件夹时，列出只在一边有的、两边都有但内容不一样的文件，子文件夹里的也算。"),
            T("Whatever goes to the Trash can be put back. Scans run in the background and stop when you close the card.", "移到废纸篓的都能放回原处；在后台扫描，卡片关掉就停。"),
        ],
        "scene": {
            "src": {"kind": "files", "app": "ada", "cap": T("Select a folder in Finder", "在访达里选中一个文件夹"),
                    "files": [{"name": T("Documents", "文稿"), "kind": "folder", "sel": True}, {"name": T("Movies", "影片"), "kind": "folder"},
                              {"name": T("Music", "音乐"), "kind": "folder"}, {"name": T("Pictures", "图片"), "kind": "folder"}]},
            "card": {"title": T("Disk Usage", "占用空间"), "sub": T("Documents", "文稿"), "w": 360,
                     "body": [{"t": "seg", "items": [T("By Folder", "按层级看"), T("Largest Files", "最大的文件")], "on": 0},
                              {"t": "note", "text": T("38.6 GB, 4812 files", "38.6 GB，4812 个文件")},
                              *_usage(_DOCS, 38.6),
                              {"t": "note", "hide": True, "text": T("Moved “Japan trip.mov” to the Trash, freeing 6.8 GB. You can put it back from the Trash.",
                                                                    "已把「日本旅行.mov」移到废纸篓，腾出 6.8 GB，可以从废纸篓放回")}]},
            "steps": [
                {"cap": T("See what takes the most space", "看看什么最占地方"), "acts": [], "hold": 1300},
                {"cap": T("Click a folder to look inside", "点文件夹进去看"),
                 "acts": [["click", "b:2", [["text", '.pl-card [data-b="1"] p', T("‹ Documents › Videos · 18.4 GB, 212 files", "‹ 文稿 › 视频 · 18.4 GB，212 个文件")]] +
                           _slide(_VIDEOS, 18.4)], ["wait", 700]],
                 "hold": 1000},
                {"cap": T("Move what you don’t need to the Trash", "不要的移到废纸篓"), "sub": T("Right-click it. You can put it back from the Trash.", "右键就行，还能从废纸篓放回。"),
                 "acts": [["click", "b:2"], ["hide", 6]] + _slide(_VIDEOS[1:], 11.6) +
                         [["text", '.pl-card [data-b="1"] p', T("‹ Documents › Videos · 11.6 GB, 211 files", "‹ 文稿 › 视频 · 11.6 GB，211 个文件")], ["show", 7]],
                 "hold": 1800},
            ],
        },
    },
    "newFile": {
        "chips": [T("8 kinds of files", "8 种文件"), T("Clipboard → file", "剪贴板存成文件"), T("Create and Open", "新建并打开")],
        "points": [
            T("Create a <b>new file</b> in the selected folder, or the folder open in Finder: plain text, Markdown, rich text, JSON, HTML, CSV, Python or a shell script.",
              "在选中的文件夹（什么都没选时是访达当前的文件夹）里<b>新建文件</b>：纯文本、Markdown、富文本、JSON、HTML、CSV、Python、Shell 脚本。"),
            T("Markdown starts with a title, HTML is a minimal web page, and shell scripts start with #!/bin/bash and can run right away.",
              "Markdown 先写好标题，HTML 是一个最简单的网页，Shell 脚本带上 #!/bin/bash，而且能直接运行。"),
            T("Or save the selected text, or the text or image on the clipboard, <b>straight to a file</b>; images become PNG.",
              "也可以把选中的文字、剪贴板里的文字或图片<b>直接存成文件</b>，图片存成 PNG。"),
            T("Choosing a kind changes the extension, and typing an extension changes the kind. The new file is selected in Finder, or opened right away.",
              "选种类时扩展名跟着变，名字里写上扩展名时种类也跟着变；新建以后在访达里选中，或者直接打开。"),
        ],
        "scene": {
            "src": {"kind": "files", "app": T("Meeting notes", "会议记录"), "cap": T("Open a folder in Finder", "在访达里打开一个文件夹"),
                    "sub": T("Nothing needs to be selected.", "什么都不用选。"), "sum": T("Meeting notes", "会议记录"),
                    "files": [{"name": "2026-09-17.md"}, {"name": "2026-09-24.md"}, {"name": T("Agenda.txt", "议程.txt")}]},
            "card": {"sub": T("Meeting notes", "会议记录"), "w": 380, "at": "center", "btns": [T("Create", "新建"), T("Create and Open", "新建并打开")], "tint": 1,
                     "body": [{"t": "note", "text": T("Save to “Meeting notes”", "存到「会议记录」")},
                              {"t": "seg", "items": [T("Blank", "空白"), T("Text on the clipboard", "剪贴板里的文字")], "on": 0},
                              {"t": "chips", "items": [T("Plain Text", "纯文本"), "Markdown", T("Rich Text", "富文本"), "JSON", "HTML", "CSV", "Python", T("Shell Script", "Shell 脚本")], "on": [0]},
                              {"t": "text", "mono": True, "size": "s", "hide": True,
                               "text": T("## Weekly sync\n- Ship 2.4 on Friday\n- New onboarding screens", "## 周会\n- 周五发布 2.4\n- 新的引导页")},
                              {"t": "field", "value": T("Untitled.txt", "未命名.txt")}]},
            "steps": [
                {"cap": T("Pick a kind", "选一种文件"), "sub": T("The extension follows.", "扩展名跟着变。"),
                 "acts": [["click", "opt:2.1", [["set", 2, {"t": "chips", "items": [T("Plain Text", "纯文本"), "Markdown", T("Rich Text", "富文本"), "JSON", "HTML", "CSV", "Python", T("Shell Script", "Shell 脚本")], "on": [1]}],
                                                ["text", '.pl-card [data-b="4"] .pl-fv', T("Untitled.md", "未命名.md")]]]], "hold": 900},
                {"cap": T("Or save the clipboard text", "或者把剪贴板里的文字存下来"), "acts": [["click", "opt:1.1"], ["show", 3]], "hold": 900},
                {"cap": T("Name it and create it", "起个名字，新建"), "sub": T("It’s selected in Finder.", "新文件在访达里选中。"),
                 "acts": [["type", 4, T("Weekly sync.md", "周会.md")], ["click", "btn:0"], ["close"],
                          ["file", {"name": T("Weekly sync.md", "周会.md")}], ["toast", T("Created “Weekly sync.md”", "新建了「周会.md」")]], "hold": 1400},
            ],
        },
    },
    "fileEncoding": {
        "chips": ["UTF-8 · GBK · Big5", T("CSV for Excel", "CSV 给 Excel 用"), "LF · CRLF"],
        "points": [
            T("Select text files (.txt, .csv, .srt subtitles, source code…) and see which <b>encoding</b> and line endings each one uses: UTF-8, UTF-16, GBK/GB18030, Big5, Shift_JIS…",
              "选中文本文件（.txt、.csv、.srt 字幕、源代码……），认出每个文件是什么<b>编码</b>、用的什么换行：UTF-8、UTF-16、GBK/GB18030、Big5、Shift_JIS……"),
            T("Each file’s first line is shown so you can spot garbled text; if the guess is wrong, read it with another encoding.",
              "卡片上写着每个文件的第一行，看是不是乱码；认错了可以换一种编码读。"),
            T("Convert them to UTF-8, <b>UTF-8 with a BOM</b> (so Excel opens CSV files correctly) or GBK, with LF or CRLF line endings.",
              "一键转成 UTF-8、<b>带 BOM 的 UTF-8</b>（Excel 打开 CSV 才不乱码）或者 GBK，换行统一成 LF 或 CRLF。"),
            T("Files that already match are left alone, and Undo restores the originals.", "已经是的不动，转完可以撤销。"),
        ],
        "scene": {
            "src": {"kind": "files", "app": T("Exports", "导出"), "cap": T("Select text files", "选中文本文件"),
                    "files": [{"name": T("orders.csv", "订单.csv"), "sel": True}, {"name": T("subtitles.srt", "字幕.srt"), "sel": True},
                              {"name": "README.md", "sel": True}, {"name": T("logo.png", "标志.png"), "kind": "photo", "art": "logo"}]},
            "card": {"w": 400, "sub": T("3 files", "3 个文件"), "btns": [T("Convert", "转换")], "tint": 0,
                     "body": [{"t": "list", "dense": True, "items": [
                                  {"file": {"name": "orders.csv"}, "title": T("orders.csv", "订单.csv"), "sub": T("Order,Item,Qty,Price", "订单号,商品,数量,金额"),
                                   "right": T("Western (Windows) · CRLF", "GB18030（GBK） · CRLF")},
                                  {"file": {"name": "subtitles.srt"}, "title": T("subtitles.srt", "字幕.srt"), "sub": "1", "right": T("UTF-16 LE · CRLF", "GB18030（GBK） · CRLF")},
                                  {"file": {"name": "README.md"}, "title": "README.md", "sub": T("# How to use", "# 使用说明"), "right": "UTF-8 · LF"}]},
                              {"t": "seg", "label": T("Convert To", "转成"), "items": ["UTF-8", T("UTF-8 with BOM", "UTF-8 带 BOM"), T("GB18030 (GBK)", "GB18030（GBK）")], "on": 0},
                              {"t": "seg", "label": T("Line feed", "换行"), "items": [T("Keep", "不变"), T("LF (Mac, Linux)", "LF（Mac、Linux）"), T("CRLF (Windows)", "CRLF（Windows）")], "on": 0},
                              {"t": "note", "text": T("Converts 2 files to UTF-8. The original contents are kept so you can undo", "会把 2 个文件转成 UTF-8，原来的内容记着，转完可以撤销")}]},
            "steps": [
                {"cap": T("See each file’s encoding", "看每个文件是什么编码"), "sub": T("The first line shows whether it reads right.", "第一行没乱码，就是认对了。"),
                 "acts": [["hover", "row:0.0"]], "hold": 1500},
                {"cap": T("Pick UTF-8 with BOM for Excel", "要给 Excel 用，选带 BOM 的"),
                 "acts": [["click", "opt:1.1", ["text", '.pl-card [data-b="3"] p', T("Excel opens CSV files saved as UTF-8 with a BOM correctly. Converts 3 files to UTF-8 with BOM. The original contents are kept so you can undo",
                                                                               "带 BOM 的 UTF-8 用 Excel 打开 CSV 不会乱码；会把 3 个文件转成 UTF-8 带 BOM，原来的内容记着，转完可以撤销")]]], "hold": 1200},
                {"cap": T("Convert, and undo if you like", "转换，还能撤销"),
                 "acts": [["click", "btn:0", ["card", {"w": 300, "sub": T("3 files", "3 个文件"), "btns": [T("Undo", "撤销"), T("Done", "完成")], "tint": 1,
                                                       "body": [{"t": "text", "text": T("Converted 3 files", "转好了 3 个文件")}]}]]],
                 "hold": 1600},
            ],
        },
    },
    "similarPhotos": {
        "chips": [T("Bursts and duplicates", "连拍和重复的"), T("Keeps the sharpest", "留最清楚的"), T("Three levels", "三档相似度")],
        "points": [
            T("Select a folder, or a few images, and Pop finds <b>burst shots</b> and photos saved twice, resized or recompressed.",
              "选中一个文件夹（或者几张图片），Pop 找出<b>连拍</b>、重复存的、改过大小或者重新压缩过的相似照片。"),
            T("Each group keeps the best one by pixels, sharpness and file size; the rest are checked, and a click on a thumbnail changes that.",
              "每组按像素多少、清晰程度、文件大小挑出最好的一张留着，其余的勾上，点一下缩略图就能换。"),
            T("Switch between Nearly Identical, Very Similar and Somewhat Similar at any time.", "「几乎一样」「很像」「有点像」三档随时切换。"),
            T("The card says how much space you’ll free. Checked photos go to the <b>Trash</b>, where you can put them back.", "写着能腾出多少空间；勾上的移到<b>废纸篓</b>，可以放回原处。"),
        ],
        "scene": {
            "src": {"kind": "files", "app": T("Pictures", "图片"), "cap": T("Select a folder of photos", "选中一个放照片的文件夹"),
                    "sub": T("Or a few images.", "或者几张图片。"),
                    "files": [{"name": T("Beach trip", "海边旅行"), "kind": "folder", "sel": True}, {"name": T("Family", "家人"), "kind": "folder"},
                              {"name": T("Garden.jpg", "花园.jpg"), "kind": "photo", "art": "flower"}, {"name": T("Mug.png", "杯子.png"), "kind": "photo", "art": "mug"}]},
            "card": {"w": 360, "sub": T("Beach trip", "海边旅行"), "btns": [T("Move to Trash (5)", "移到废纸篓（5 张）")], "tint": 0,
                     "body": [{"t": "seg", "items": [T("Nearly Identical", "几乎一样"), T("Very Similar", "很像"), T("Somewhat Similar", "有点像")], "on": 1},
                              {"t": "thumbs", "cols": 4, "items": [{"art": "beach", "best": True, "chk": False, "label": T("Keep", "留着")},
                                                                    {"art": "beach", "chk": True}, {"art": "beach", "chk": True}, {"art": "beach", "chk": True}]},
                              {"t": "thumbs", "cols": 4, "items": [{"art": "sunset", "best": True, "chk": False, "label": T("Keep", "留着")},
                                                                    {"art": "sunset", "chk": True}, {"art": "sunset", "chk": True}]},
                              {"t": "note", "text": T("Found 2 groups of similar photos, 7 photos in all. Moving the 5 checked ones to the Trash frees 18.6 MB",
                                                      "找到 2 组相似的照片，一共 7 张；勾上的 5 张移到废纸篓能腾出 18.6 MB")}]},
            "steps": [
                {"cap": T("Each group keeps the best one", "每组留最清楚的一张"), "sub": T("The rest are checked.", "其余的都勾上了。"), "acts": [], "hold": 1500},
                {"cap": T("Click to change your mind", "点一下就能换"),
                 "acts": [["click", "chk:2.2", [["text", '.pl-card [data-b="3"] p', T("Found 2 groups of similar photos, 7 photos in all. Moving the 4 checked ones to the Trash frees 14.9 MB",
                                                                                     "找到 2 组相似的照片，一共 7 张；勾上的 4 张移到废纸篓能腾出 14.9 MB")],
                                                ["text", "btn:0", T("Move to Trash (4)", "移到废纸篓（4 张）")]]]], "hold": 1000},
                {"cap": T("Move the rest to the Trash", "其余的移到废纸篓"), "sub": T("You can put them back.", "还能从废纸篓放回。"),
                 "acts": [["click", "btn:0", ["card", {"w": 300, "sub": T("Beach trip", "海边旅行"), "btns": [T("Open Trash", "打开废纸篓"), T("Done", "完成")], "tint": 1,
                                                         "body": [{"t": "text", "text": T("Moved 4 photos, freeing 14.9 MB", "移走了 4 张，腾出 14.9 MB")}]}]]],
                 "hold": 1600},
            ],
        },
    },
    "mediaInfo": {
        "chips": ["4K · HDR", T("Audio and subtitle tracks", "音轨和字幕"), T("Remove the location", "去掉拍摄地点")],
        "points": [
            T("Select a video or audio file and see its <b>codec</b> (H.264, HEVC, ProRes, AV1…), its resolution named as 4K or 1080p, frame rate and bit rate.",
              "选中一个视频或音频，看它的<b>编码</b>（H.264、HEVC、ProRes、AV1……）、分辨率（标出 4K、1080p 这些叫法）、帧率和码率。"),
            T("Whether it’s HDR (HDR10, HLG, Dolby Vision), its color space and bit depth; each audio track’s codec, channels, sample rate and language; and the subtitle languages.",
              "是不是 HDR（HDR10、HLG、Dolby Vision）、色域和色深；每条音轨的编码、声道、采样率和语言；有哪些语言的字幕。"),
            T("Also which device shot it, when and where. Before sharing, <b>save a copy without the location</b>: the picture and sound are copied as they are.",
              "还有拍摄设备、拍摄时间和拍摄地点；发给别人前可以<b>去掉位置另存一份</b>，画面和声音原样复制，不重新编码。"),
            T("Copy all the information at once.", "可以一键复制全部信息。"),
        ],
        "scene": {
            "src": {"kind": "files", "app": T("Movies", "影片"), "cap": T("Select a video or audio file", "选中一个视频或音频"),
                    "files": [{"name": T("Sunset walk.mov", "傍晚散步.mov"), "kind": "video", "art": "sunset", "sel": True},
                              {"name": T("Interview.mp4", "采访.mp4"), "kind": "video", "art": "portrait"},
                              {"name": T("Theme.m4a", "主题曲.m4a"), "kind": "audio"}, {"name": T("Drone.mov", "航拍.mov"), "kind": "video", "art": "landscape"}]},
            "tall": True,
            "card": {"title": T("Media Info", "媒体信息"), "sub": T("Sunset walk.mov", "傍晚散步.mov"), "w": 360, "at": "right",
                     "btns": [T("Show in Finder", "在访达中显示"), T("Copy Info", "复制信息")], "tint": 1,
                     "body": [{"t": "list", "items": [{"file": {"kind": "video", "art": "sunset"}, "title": T("Sunset walk.mov", "傍晚散步.mov"),
                                                       "sub": "QuickTime · 1:23 · 412 MB · 39.5 Mbps"}]},
                              {"t": "note", "text": T("**Video**", "**视频**")},
                              {"t": "rows", "mono": False, "copy": False,
                               "rows": [[T("Codec", "编码格式"), T("HEVC (H.265)", "HEVC（H.265）")], [T("Video", "画面"), "3840 × 2160 · 4K"],
                                        [T("Frame Rate", "帧率"), T("29.97 fps", "29.97 帧/秒")], [T("Dynamic Range", "动态范围"), T("Dolby Vision (HLG)", "Dolby Vision（HLG）")]]},
                              {"t": "note", "text": T("**Details**", "**信息**")},
                              {"t": "rows", "mono": False, "copy": False,
                               "rows": [[T("Device", "设备"), "Apple iPhone 15 Pro"], [T("Location", "拍摄地点"), T("37.8080, -122.4177", "31.2304, 121.4737"), "warn"]]},
                              {"t": "note", "text": T("This file records where it was shot. You can remove the location before sharing it.", "这个文件里记着拍摄地点，发给别人前可以去掉")},
                              {"t": "html", "html": _btns(T("Show in Maps", "在地图中查看"), T("Save a Copy Without Location", "去掉位置另存一份"), tint=1)}]},
            "steps": [
                {"cap": T("Everything about the file", "文件的方方面面都在这"), "sub": T("Codec, resolution, HDR, device and place.", "编码、分辨率、HDR、设备和拍摄地点。"),
                 "acts": [["hover", "row:2.3"]], "hold": 1600},
                {"cap": T("Remove the location before sharing", "发出去前去掉拍摄地点"), "sub": T("The picture and sound aren’t re-encoded.", "画面和声音不重新编码。"),
                 "acts": [["click", "btn:6.1"],
                          ["text", '.pl-card [data-b="5"] p', T("Saved as “Sunset walk without location.mov”. The video and sound weren’t re-encoded.",
                                                                 "已另存为「傍晚散步 无位置.mov」，画面和声音没有重新编码")],
                          ["text", '.pl-card [data-b="6"] .pl-btn:nth-child(2)', T("Show the Copy", "显示另存的文件")],
                          ["file", {"name": T("Sunset walk without location.mov", "傍晚散步 无位置.mov"), "kind": "video", "art": "sunset", "at": 0}]], "hold": 1300},
                {"cap": T("Copy all the info", "复制全部信息"), "acts": [["click", "btn:1", ["toast", T("Copied", "已复制")]]]},
            ],
        },
    },
    "subtitles": {
        "chips": ["SRT · WebVTT · ASS · LRC", T("Shift and clean up", "调时间、清理"), T("Bilingual merge", "合成双语字幕")],
        "points": [
            T("Select subtitles (SRT, WebVTT, ASS/SSA, LRC) and <b>shift them earlier or later</b>, or convert between frame rates (23.976, 24, 25).",
              "选中字幕文件（SRT、WebVTT、ASS/SSA、LRC），<b>整体提前或推后</b>，或者换帧率（23.976、24、25 互相换）。"),
            T("Remove style tags (italics, colors, positions, ASS effects) and hearing-impaired descriptions such as [Music] and (laughs).",
              "去掉样式标签（斜体、颜色、位置、ASS 的特效）和听障说明（[音乐]、(笑声)）。"),
            T("Save as SRT, WebVTT, LRC or plain text, with the first lines previewed. Keeping the format updates the original (as UTF-8) and can be undone; a new format saves a copy.",
              "转成 SRT、WebVTT、LRC 或者纯文字，卡片上能看到处理以后的前几句。格式不变时直接改原文件（存成 UTF-8），可以撤销；换了格式另存一份。"),
            T("Select two, such as English and Chinese, to <b>merge them into one bilingual file</b>; you choose which goes on top.",
              "选两份字幕（比如中文和英文）可以<b>合成一份双语字幕</b>，上面一行用哪一份可以选。"),
        ],
        "scene": {
            "src": {"kind": "files", "app": T("Movies", "影片"), "cap": T("Select a subtitle file", "选中字幕文件"),
                    "sub": T("Two of them to make a bilingual one.", "选两份就能合成双语字幕。"),
                    "files": [{"name": T("The Long Walk.mp4", "长路.mp4"), "kind": "video", "art": "city"}, {"name": T("The Long Walk.srt", "长路.srt"), "sel": True},
                              {"name": T("Trailer.mp4", "预告片.mp4"), "kind": "video", "art": "landscape"}]},
            "tall": True,
            "card": {"sub": T("The Long Walk.srt", "长路.srt"), "w": 400, "btns": [T("Save", "存好")], "tint": 0,
                     "body": [{"t": "note", "text": T("**The Long Walk.srt**  SRT · 842 lines · 0:01 – 1:52:10 · Unicode (UTF-8)", "**长路.srt**  SRT · 842 句 · 0:01 – 1:52:10 · GBK")},
                              _cues(["00:00:01,200", "00:00:03,900", "00:00:06,400", "00:00:08,750"], _SUB_LINES[:4]),
                              {"t": "field", "label": T("Timing", "时间"), "value": "0", "mono": True},
                              {"t": "note", "text": T("No shift", "不调")},
                              {"t": "list", "dense": True, "items": [{"chk": False, "title": T("Remove style tags", "去掉样式标签")},
                                                                     {"chk": False, "title": T("Remove hearing-impaired descriptions", "去掉听障说明")}]},
                              {"t": "seg", "label": T("Save As", "存成"), "items": ["SRT", "WebVTT", "LRC", T("Plain Text", "纯文字")], "on": 0},
                              {"t": "note", "text": T("Changes the original file; you can undo", "直接改原文件，可以撤销")}]},
            "steps": [
                {"cap": T("Shift them 1.5 s later", "整体推后 1.5 秒"), "sub": T("The preview follows.", "预览跟着变。"),
                 "acts": [["type", 2, "1.5"], ["text", '.pl-card [data-b="3"] p', T("1.5 s later", "推后 1.5 秒")],
                          ["set", 1, _cues(["00:00:02,700", "00:00:05,400", "00:00:07,900", "00:00:10,250"], _SUB_LINES[:4])]], "hold": 1000},
                {"cap": T("Clean up tags and descriptions", "去掉样式标签和听障说明"),
                 "acts": [["click", "chk:4.0"], ["click", "chk:4.1"],
                          ["set", 1, _cues(["00:00:05,400", "00:00:07,900", "00:00:10,250", "00:00:13,600"],
                                           [T("Where were you last night?", "你昨晚去哪儿了？"), _SUB_LINES[2], T("You’re a terrible liar.", "你真不会撒谎。"), _SUB_LINES[4]])]],
                 "hold": 1100},
                {"cap": T("Save", "存好"), "sub": T("Undo is right there.", "可以撤销。"),
                 "acts": [["click", "btn:0", ["card", {"w": 400, "sub": T("The Long Walk.srt", "长路.srt"), "btns": [T("Undo", "撤销"), T("Show in Finder", "在访达中显示"), T("Done", "完成")], "tint": 2,
                                                       "body": [{"t": "note", "text": T("Updated “The Long Walk.srt” and saved it as UTF-8", "改好了「长路.srt」，存成 UTF-8")}]}]]],
                 "hold": 1600},
            ],
        },
    },
    "encryptFiles": {
        "chips": ["AES-256", T("Opens on any Mac", "任何 Mac 都能打开"), T("Password twice", "密码输两遍")],
        "points": [
            T("Put the selected files and folders into a <b>password-protected disk image</b> (AES-256, or AES-128) before you send them or copy them to a USB drive or cloud storage.",
              "把选中的文件和文件夹放进一个<b>用密码加密的磁盘映像</b>（AES-256，也可以选 AES-128），发给别人、存到 U 盘或者网盘前用。"),
            T("It opens on any Mac with a double-click and the password, like a USB drive.", "在任何一台 Mac 上双击、输入密码就能打开，像一个 U 盘。"),
            T("You type the password twice; one that’s too short isn’t accepted, and a simple one gets a warning.", "密码要输两遍，太短不让做，太简单会提醒。"),
            T("You can move the originals to the Trash afterwards (off by default). The password never appears on a command line and is cleared from memory when it’s done.",
              "可以做好后把原文件移到废纸篓（默认不勾）；密码不会出现在命令行里，做完就从内存里清掉。"),
        ],
        "scene": {
            "src": {"kind": "files", "app": T("Documents", "文稿"), "cap": T("Select files or folders", "选中文件或文件夹"),
                    "files": [{"name": T("Tax 2025", "2025 报税"), "kind": "folder", "sel": True}, {"name": T("Photos", "照片"), "kind": "folder"},
                              {"name": T("Passport.pdf", "护照.pdf")}, {"name": T("Notes.txt", "笔记.txt")}]},
            "card": {"w": 360, "sub": T("Tax 2025, 48.2 MB in total", "2025 报税，一共 48.2 MB"), "btns": [T("Encrypt Files", "加密打包")], "tint": 0,
                     "body": [{"t": "field", "label": T("Name", "名字"), "value": T("Tax 2025", "2025 报税")},
                              {"t": "field", "label": T("Password", "密码"), "value": ""},
                              {"t": "field", "label": T("Confirm", "再输一遍"), "value": ""},
                              {"t": "seg", "label": T("Encryption", "加密强度"), "items": ["AES-256", "AES-128"], "on": 0},
                              {"t": "list", "dense": True, "items": [{"chk": False, "title": T("Move the originals to the Trash afterwards", "做好后把原文件移到废纸篓")}]},
                              {"t": "note", "text": T("Saved in “Documents”", "存在「文稿」里")}]},
            "steps": [
                {"cap": T("Type a password twice", "密码输两遍"), "sub": T("Too short won’t do; too simple gets a warning.", "太短不让做，太简单会提醒。"),
                 "acts": [["type", 1, "••••••••••••"], ["set", 1, {"t": "field", "label": T("Password", "密码"), "value": "••••••••••••"}],
                          ["type", 2, "••••••••••••"]], "hold": 700},
                {"cap": T("Click Encrypt Files", "点「加密打包」"), "sub": T("Double-click it on any Mac and enter the password.", "在任何一台 Mac 上双击、输入密码就能打开。"),
                 "acts": [["click", "btn:0"], ["close"], ["file", {"name": T("Tax 2025.dmg", "2025 报税.dmg"), "at": 1}], ["wait", 300],
                          ["card", {"w": 340, "at": "center", "sub": T("Tax 2025, 48.2 MB in total", "2025 报税，一共 48.2 MB"),
                                                       "btns": [T("Show in Finder", "在访达中显示"), T("Done", "完成")], "tint": 1,
                                                       "body": [{"t": "text", "text": T("Created “Tax 2025.dmg” (51.3 MB)", "做好了「2025 报税.dmg」（51.3 MB）")},
                                                                {"t": "note", "text": T("Double-click it on any Mac and enter the password to open it. Without the password it can’t be opened, so keep it safe.",
                                                                                        "在任何一台 Mac 上双击它、输入密码就能打开。密码忘了就打不开了，记好它")}]}]], "hold": 1800},
            ],
        },
    },
}
