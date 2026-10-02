"""Plugin pages: text plugins. See __init__.py and the README ("Plugin pages")."""
from . import T

# A tick in a checkbox, for the small bits of `html` that show one (the engine's .pl-chk).
_TICK = ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" '
         'stroke-linejoin="round" aria-hidden="true"><path d="m5 12.5 4.5 4.5L19 7.5"/></svg>')


def _check(label, on=True):
    """A checkbox with its label (a Toggle with .checkbox style in Pop)."""
    return f'<span class="pl-chk{" is-on" if on else ""}">{_TICK}</span><span class="pl-lab">{label}</span>'


# ------------------------------------------------------------------ Text to Image
# The long image in the card: Pop's three backgrounds (TextImage.Style). These are the colours of the
# picture itself, so they stay the same in light and dark mode.
_TI_STYLE = {"paper": ("#ffffff", "#212126"), "warm": ("#faf2e0", "#3d3326"), "night": ("#1c1f24", "#dee0e6")}
_TI_TEXT = {
    "en": ["Every morning I leave my phone in the kitchen and walk to the bakery on the corner.",
           "The street is still quiet. The baker knows my order, and the first loaves of the day are still warm.",
           "By the time I’m home, the coffee is ready and the day feels like my own."],
    "zh": ["每天早上，我把手机留在厨房，走到街角的面包店。",
           "街上还很安静。老板记得我要什么，第一炉面包还是热的。",
           "走回家时，咖啡刚好煮好，这一天好像是自己的。"],
}


def _ti_preview(style, lang):
    bg, fg = _TI_STYLE[style]
    paras = "".join(f'<p style="margin:0 0 9px">{p}</p>' for p in _TI_TEXT[lang])
    return (f'<div style="height:150px;overflow:hidden;border-radius:8px;background:var(--pl-fill)">'
            f'<div style="background:{bg};color:{fg};padding:16px 18px 30px;font-size:11px;line-height:1.75">{paras}</div></div>')


def _ti_card(style):
    others = {"paper": [T("Cream", "米黄"), T("Dark", "深色")], "warm": [T("White", "白底"), T("Dark", "深色")],
              "night": [T("White", "白底"), T("Cream", "米黄")]}[style]
    n_en, n_zh = len("\n".join(_TI_TEXT["en"])), len("\n".join(_TI_TEXT["zh"]))
    return {"w": 330, "btns": [T("Copy Image", "复制图片"), T("Save", "存储"), T("Pin to Screen", "贴到屏幕")] + others,
            "body": [{"t": "html", "html": T(_ti_preview(style, "en"), _ti_preview(style, "zh"))},
                     {"t": "note", "text": T(f"{n_en} characters, 1080 pixels wide; drag the preview into another app",
                                             f"{n_zh} 个字，图片宽 1080 像素；按住拖动预览图也能拖到别的 App 里")}]}


# ------------------------------------------------------------------ Font Preview
# One row per font: its name (the Chinese name too, on a Chinese Mac), how many styles, a star, and the text in it.
def _font_row(k, name, styles, family, text, star=False, alt=""):
    alt = f'<span>{alt}</span>' if alt else ""
    star_html = (f'<span class="pl-fstar" data-k="{k}" style="margin-left:auto;font-size:13px;line-height:1;'
                 f'color:{"#ffcc00" if star else "var(--pl-l3)"}">{"★" if star else "☆"}</span>')
    return (f'<div style="display:flex;flex-direction:column;gap:1px;padding:4px 2px 5px;border-bottom:1px solid var(--pl-sep)">'
            f'<div style="display:flex;align-items:baseline;gap:6px;font-size:10.5px;color:var(--pl-l2)">'
            f'<b style="font-weight:600;color:var(--pl-l1)">{name}</b>{alt}<span style="font-size:9.5px;color:var(--pl-l3)">{styles}</span>{star_html}</div>'
            f'<div style="font-family:{family};font-size:21px;line-height:1.3;color:var(--pl-l1);white-space:nowrap;overflow:hidden;text-overflow:ellipsis">{text}</div></div>')


_FP_EN = "Fresh bread &amp; cider"
_FP_ZH = "落霞与孤鹜齐飞"
_FONTS_EN = [("American Typewriter", "7 styles", "'American Typewriter','Courier New',serif"),
             ("Avenir Next", "12 styles", "'Avenir Next',Avenir,'Helvetica Neue',sans-serif"),
             ("Baskerville", "6 styles", "Baskerville,'Baskerville Old Face',Georgia,serif")]
_FONTS_ZH = [("苹方-简", "6 种样式", "'PingFang SC',sans-serif", "PingFang SC"),
             ("宋体-简", "4 种样式", "'Songti SC',STSong,serif", "Songti SC"),
             ("楷体-简", "3 种样式", "'Kaiti SC',STKaiti,KaiTi,serif", "Kaiti SC")]


def _fp_html(lang, starred, favs_only=False):
    if lang == "en":
        return "".join(_font_row(i, n, s, f, _FP_EN, i in starred) for i, (n, s, f) in enumerate(_FONTS_EN)
                       if not favs_only or i in starred)
    return "".join(_font_row(i, n, s, f, _FP_ZH, i in starred, a) for i, (n, s, f, a) in enumerate(_FONTS_ZH)
                   if not favs_only or i in starred)


def _fp_panes(starred_en, starred_zh):
    """The font list for each filter (All, Chinese, Western, Monospaced, Favorites). The English page starts
    on All, the Chinese one on Chinese (Pop starts there when the text has Chinese characters)."""
    rows = {"t": "html", "html": T(_fp_html("en", starred_en), _fp_html("zh", starred_zh))}
    favs = {"t": "html", "html": T(_fp_html("en", starred_en, True), _fp_html("zh", starred_zh, True))}
    return {"t": "panes", "on": T(0, 1), "panes": [[rows], [rows], [], [], [favs]]}


# ------------------------------------------------------------------ Emoji & Symbols
_SMILEYS = "😀 😃 😄 😁 😆 😅 🤣 😂 🙂 🙃 🫠 😉 😊 😇 🥰 😍 🤩 😘 😗 ☺️ 😚 😙 🥲 😋 😛 😜 🤪 😝 🤑 🤗".split()
_MATH = "+ − × ÷ ± ∓ ≠ ≈ ≡ ≤ ≥ ≪ ≫ ∝ ∞ √ ∛ ∑ ∏ ∫ ∬ ∮ ∂ ∇ ∆ π ∠ ⊥ ∥ ⊙".split()
_CATS_EN = "🐈️ 😹 😼 🐱 😺 😸 😻 😽 🙀 😿 😾 🐈‍⬛ 🐯 🐅 🐆".split()
_CATS_ZH = "🐈️ 🐱 🦉 😻 🐈‍⬛ 😺 😸 😹 😼 😽 🙀 😿 😾 🐼".split()


def _cat_bar(icons):
    cells = "".join(f'<span style="flex:1;text-align:center;padding:3px 0;border-radius:6px;'
                    f'{"background:var(--pl-accent-22)" if i == 0 else ""}">{x}</span>' for i, x in enumerate(icons))
    html = f'<div style="display:flex;gap:2px;font-size:14px;line-height:1.3">{cells}</div>'
    return {"t": "html", "html": T(html, html)}  # the symbols' bar shows 「」, which is language-neutral here


def _emoji_foot(emoji, name, other, right=T("Return to insert · ⌘C to copy", "回车插入 · ⌘C 复制")):
    """The line under the grid: the emoji, its name, its name in the other language and code points, and how to use it."""
    return {"t": "list", "dense": True, "items": [{"icon": emoji, "title": name, "sub": other, "right": right}]}


# Translate Screenshot: the translations side by side (the card's 「对比」 mode).
_TR_COMPARE = {"t": "rows", "mono": False, "rows": [
    [T("System", "系统"), T("The market opens at 8 am on Town Hall Square, with bread, cheese and flowers.", "集市早上 8 点在市政厅广场开门，有面包、奶酪和鲜花。")],
    ["AI", T("The market opens at 8 a.m. in Town Hall Square, with bread, cheeses and flowers.", "集市上午 8 点在市政厅广场开市，卖面包、奶酪和鲜花。")],
    ["DeepL", T("The market opens at 8 a.m. on Place de la Mairie, with bread, cheese and flowers.", "市场早上 8 点在市政厅广场开放，提供面包、奶酪和鲜花。")]]}

DATA = {
    # ------------------------------------------------------------------ Translate Screenshot
    "screenshotTranslate": {
        "chips": [T("Any text on screen", "屏幕上的任何文字"), T("Recognized on your Mac", "本机识别"), T("Compare engines", "几家译文对比")],
        "points": [
            T("Drag over part of the screen, even text you can’t select in an image, a video or an app, and Pop <b>recognizes the text and translates it</b>.",
              "在屏幕上拖出一块区域，图片、视频、App 界面里选不中的文字也行，Pop <b>认出里面的文字再翻译</b>。"),
            T("Lines broken by the layout on screen are joined into paragraphs first, so the translation reads naturally.",
              "按屏幕上的行断开的文字会先接成段落，译文才通顺。"),
            T("The text is recognized on your Mac; with the system translation and its language pack, nothing goes online.",
              "文字在本机识别；用系统翻译（装好语言包）时，翻译也不联网。"),
            T("The result is Pop’s translation card: change the target language or the engine, <b>compare engines</b>, copy the translation, pin it to the screen or hear it read aloud.",
              "结果就是 Pop 的翻译卡片：可以换目标语言、换引擎、<b>几家的译文放在一起对比</b>，复制译文、贴到屏幕上，或者朗读。"),
            T("It needs Screen Recording permission.", "需要「屏幕录制」权限。"),
        ],
        "scene": {
            "src": {"kind": "web", "app": T("Safari", "Safari浏览器"), "url": T("marche.example.fr/samedi", "market.example.com/saturday"),
                    "cap": T("Open what you want to read", "打开要看的内容"), "sub": T("No need to select anything.", "什么都不用选。"), "sum": T("Nothing selected", "未选中内容"),
                    "lines": [T("Marché du samedi", "Saturday Market"),
                              T("Le marché ouvre à 8 h place de la Mairie, avec du pain, des fromages et des fleurs.",
                                "The market opens at 8 am on Town Hall Square, with bread, cheese and flowers."),
                              T("Pensez à apporter vos sacs : les sacs en plastique ne sont plus fournis.",
                                "Please bring your own bags: plastic bags are no longer provided.")],
                    "pic": "flower"},
            "fx": {"name": "region", "target": ".pl-page p"},
            "card": {"title": T("Translate", "翻译"), "sub": T("Français → English", "English → 简体中文"), "w": 360, "at": "right",
                     "btns": [T("Copy Translation", "复制译文"), T("Pin to Screen", "贴到屏幕"), T("Speak", "朗读")],
                     "body": [{"t": "seg", "label": T("To English", "译成简体中文"), "items": [T("System", "系统"), "AI", "DeepL", T("Compare", "对比")], "on": 0},
                              {"t": "text", "muted": True, "text": T("Le marché ouvre à 8 h place de la Mairie, avec du pain, des fromages et des fleurs.",
                                                                     "The market opens at 8 am on Town Hall Square, with bread, cheese and flowers.")},
                              {"t": "sep"},
                              {"t": "text", "type": True, "text": T("The market opens at 8 am on Town Hall Square, with bread, cheese and flowers.",
                                                                    "集市早上 8 点在市政厅广场开门，有面包、奶酪和鲜花。")}]},
            "steps": [
                {"cap": T("Drag over the text", "拖过要看的文字"), "sub": T("It’s recognized and translated right away.", "认出文字，马上翻译。"), "acts": [], "hold": 1600},
                {"cap": T("Copy it, pin it or hear it", "复制、贴到屏幕或者朗读"), "acts": [["click", "btn:0", ["toast", T("Copied", "已复制")]]]},
                {"cap": T("Compare the engines", "几家译文对比"), "sub": T("AI and DeepL work once they’re set up in Settings.", "AI 和 DeepL 在设置里设置好就能用。"),
                 "acts": [["click", "opt:0.3", ["set", 3, _TR_COMPARE]], ["wait", 600]], "hold": 2000},
            ],
        },
    },

    # ------------------------------------------------------------------ Speak
    "speak": {
        "chips": [T("System voices", "系统语音"), T("Use again to stop", "再用一次就停"), T("Save as .m4a", "存成 .m4a")],
        "points": [
            T("Select text and Pop <b>reads it aloud</b> in a system voice for its language: Mandarin for Chinese, a Taiwanese voice for Traditional Chinese.",
              "选中文字，Pop 用对应语言的系统语音<b>读出来</b>：中文用普通话，繁体用台湾的语音。"),
            T("Use Speak again while it’s reading to stop.", "朗读中再用一次就停止。"),
            T("<b>Save Speech as Audio</b>, the plugin’s second action, saves the speech as an .m4a file in Downloads named after the first few words, and shows it in Finder with its length: for voice-overs or listening practice.",
              "插件里的第二项「<b>朗读存成音频</b>」把读出来的声音存成 .m4a 放进「下载」，文件名是开头几个字，存好后在访达里选中，写着有多长：配音、听力材料都能用。"),
            T("If a voice can’t be saved (some Siri voices can’t), Pop says so: choose another system voice in Accessibility settings.",
              "有的语音（比如部分 Siri 语音）不能存成音频，Pop 会说一声：到「系统设置 → 辅助功能 → 朗读内容」里换一个系统语音。"),
        ],
        "scene": {
            "src": {"kind": "web", "app": T("Safari", "Safari浏览器"), "url": T("radio.example.com/morning", "radio.example.com/zaojian"),
                    "lines": [T("Morning briefing", "晨间简报"),
                              T("[[Good morning, everyone. Today will be sunny with a light breeze, and the farmers market opens at eight.]]",
                                "[[大家早上好，欢迎收听今天的晨间简报。今天晴，有微风，农贸市场八点开门。]]"),
                              T("Traffic is light on the ring road this morning.", "今天早上环路上车不多。")],
                    "pic": "sunset"},
            # Pop shows no card here, only a short notice: the voice is the result.
            "label": T("Speak", "朗读"),
            "steps": [
                {"cap": T("It reads the text aloud", "读出来"), "sub": T("In a system voice for the text’s language.", "用对应语言的系统语音。"),
                 "acts": [["toast", T("Speaking…", "正在朗读…"), 2400]], "hold": 900},
                {"cap": T("Use it again to stop", "再用一次就停"), "acts": [["toast", T("Stopped speaking", "已停止朗读"), 1500]], "hold": 700},
                {"cap": T("Or save it as audio", "或者存成音频"), "sub": T("Save Speech as Audio puts an .m4a in Downloads.", "「朗读存成音频」存一个 .m4a 放进「下载」。"),
                 "acts": [["toast", T("Saving as audio…", "正在存成音频…"), 1300], ["wait", 200],
                          ["toast", T("Saved “Speech Good morning….m4a” (8 s long)", "存好了「朗读 大家早上好，欢迎收听今天….m4a」，长 8 秒"), 2600]], "hold": 900},
            ],
        },
    },

    # ------------------------------------------------------------------ Save Web Page
    "webCapture": {
        "chips": [T("One long PDF", "一页长 PDF"), T("Long image", "长图"), T("Article as Markdown", "正文存成 Markdown")],
        "points": [
            T("Select a link and Pop opens the page <b>in the background</b>, scrolls through it so images that load late appear, saves it to Downloads under the page’s title and selects it in Finder.",
              "选中一个网址，Pop <b>在后台</b>打开这个网页，往下滚一遍让懒加载的图片都出来，用网页标题存进「下载」，并在访达里选中。"),
            T("As a PDF it’s one long page whose text you can select and search, with working links; or save it as one long image.",
              "存成 PDF 是一页长 PDF，文字能选、能搜，链接能点；也可以存成一张长图。"),
            T("<b>Save as Markdown</b> keeps just the article, without navigation, sidebars and footers, with full addresses for links and images and the title and original link at the top: ready for your notes.",
              "「<b>存成 Markdown</b>」只取正文，去掉导航、侧栏、页脚，链接和图片换成完整的网址，最前面是标题和原文链接，适合做笔记。"),
            T("Pages are saved as they look in light mode. Pop doesn’t use your browser’s sign-ins, so a page that needs one is saved as the sign-in page.",
              "按浅色的样子存。用的是 Pop 自己打开的网页，没有浏览器里的登录状态，要登录才能看的页面存下来是登录页。"),
        ],
        "scene": {
            "src": {"kind": "text", "app": T("Notes", "备忘录"), "title": T("Reading list", "稍后阅读"), "cap": T("Select a link", "选中一个网址"),
                    "lines": [T("# Reading list", "# 稍后阅读"),
                              "[[https://blog.example.com/field-notes]]",
                              "https://news.example.org/tide-tables",
                              T("Read before the trip on Saturday.", "周六出发前看完。")]},
            "card": {"title": T("Save Web Page", "网页存档"), "w": 360,
                     "btns": [T("Save as PDF", "存成 PDF"), T("Save as Long Image", "存成长图"), T("Save as Markdown", "存成 Markdown")],
                     "body": [{"t": "text", "text": "https://blog.example.com/field-notes"},
                              {"t": "note", "text": T("Saved to Downloads: PDF and image keep the whole page, Markdown just the article. Pages behind a sign-in save as the sign-in page.",
                                                      "在后台打开网页存到「下载」：PDF 和长图是整页，Markdown 只取正文；要登录的页面存下来是登录页")}]},
            "steps": [
                {"cap": T("PDF, long image or Markdown", "PDF、长图还是 Markdown"), "acts": [["move", "btn:2"], ["wait", 400], ["move", "btn:1"], ["wait", 300], ["move", "btn:0"]], "hold": 700},
                {"cap": T("It opens the page in the background", "在后台打开网页"), "sub": T("And scrolls through it so every image loads.", "往下滚一遍，让图片都加载出来。"),
                 "acts": [["click", "btn:0"], ["close"], ["toast", T("Opening the web page…", "正在打开网页…")]], "hold": 500},
                {"cap": T("Saved to Downloads", "存进「下载」"), "sub": T("Named after the page, and selected in Finder.", "用网页标题命名，在访达里选中。"),
                 "acts": [["toast", T("Saved to Downloads: Field Notes.pdf", "已存到「下载」：海边的田野笔记.pdf")]], "hold": 900},
            ],
        },
    },

    # ------------------------------------------------------------------ Text to Image
    "textImage": {
        "chips": [T("1080 px wide", "宽 1080 像素"), T("White · Cream · Dark", "白底 · 米黄 · 深色"), T("Pin to Screen", "贴到屏幕")],
        "points": [
            T("Lays out the selected text as <b>one long image</b> that reads well on a phone, 1080 pixels wide with room between paragraphs, for places where long text is awkward to paste.",
              "把选中的文字排成<b>一张长图</b>，宽 1080 像素，段落之间留出空隙，手机上看着舒服，发到不方便贴长文字的地方。"),
            T("Switch between a white, cream and dark background.", "可以换白底、米黄、深色三种底色。"),
            T("Copy it, save it to Downloads, pin it on the screen, or drag the preview straight into another app.",
              "可以复制、存到「下载」、贴到屏幕上，也能按住预览图直接拖到别的 App 里。"),
            T("Very long text is drawn up to 8,000 characters, with a note at the end saying how much is left.",
              "特别长的只画前 8000 字，末尾注明还剩多少。"),
        ],
        "scene": {
            "src": {"kind": "text", "app": T("Notes", "备忘录"), "title": T("Morning notes", "早晨笔记"),
                    "lines": [T("# Slow mornings", "# 慢一点的早晨"),
                              T("[[" + _TI_TEXT["en"][0], "[[" + _TI_TEXT["zh"][0]),
                              T(_TI_TEXT["en"][1], _TI_TEXT["zh"][1]),
                              T(_TI_TEXT["en"][2] + "]]", _TI_TEXT["zh"][2] + "]]")]},
            "card": _ti_card("paper"),
            "steps": [
                {"cap": T("A long image, easy to read on a phone", "一张手机上好读的长图"), "acts": [], "hold": 1500},
                {"cap": T("Try cream or dark", "换米黄或者深色"),
                 "acts": [["click", "btn:3", ["card", dict(_ti_card("warm"), keepPointer=True)]], ["wait", 700],
                          ["click", "btn:4", ["card", dict(_ti_card("night"), keepPointer=True)]]], "hold": 1100},
                {"cap": T("Copy it, save it or pin it", "复制、存储或者贴到屏幕"), "sub": T("Or drag the preview into a chat.", "也可以把预览图直接拖进聊天窗口。"),
                 "acts": [["click", "btn:1"], ["close"], ["toast", T("Saved to Downloads", "已存到「下载」")]]},
            ],
        },
    },

    # ------------------------------------------------------------------ Large Type
    "largeType": {
        "chips": [T("Wi-Fi passwords", "Wi-Fi 密码"), T("Phone numbers", "电话号码"), T("Any key closes", "按任意键关闭")],
        "points": [
            T("Shows the selected text across the whole screen <b>as large as it fits</b>, so the person next to you can read a phone number, a Wi-Fi password or a pickup code.",
              "把选中的文字用<b>尽量大的字号</b>铺满整个屏幕，给旁边的人看电话号码、Wi-Fi 密码、取件码都方便。"),
            T("Numbers and words aren’t split across two lines; long links can wrap.", "号码、单词不会被拆到两行，长链接可以换行。"),
            T("Click or press any key to close; ⌘C copies the text as it closes.", "点一下或按任意键关闭，⌘C 复制。"),
        ],
        "scene": {
            "src": {"kind": "text", "app": T("Notes", "备忘录"), "title": T("Guest Wi-Fi", "访客 Wi-Fi"),
                    "lines": [T("# Guest Wi-Fi", "# 访客 Wi-Fi"), T("Network: Harbor Guest", "网络：Harbor Guest"),
                              T("Password: [[sunny-otter-42]]", "密码：[[sunny-otter-42]]"), T("Ask at the front desk for a printed card.", "前台也有打印好的卡片。")]},
            "fx": {"name": "large", "text": "sunny-otter-42"},
            "steps": [
                {"cap": T("It fills the screen", "铺满整个屏幕"), "sub": T("Easy to read from across the room.", "隔着桌子也看得清。"), "acts": [["wait", 2200]]},
                {"cap": T("Press any key to close", "按任意键关闭"), "sub": T("⌘C copies it first.", "按 ⌘C 先复制再关闭。"),
                 "acts": [["key", "⌘C"], ["fx", "end"]], "hold": 1000},
            ],
        },
    },

    # ------------------------------------------------------------------ Font Preview
    "fontPreview": {
        "chips": [T("Every font on your Mac", "每一种字体"), T("Copy CSS", "复制 CSS"), T("Install font files", "安装字体文件")],
        "points": [
            T("Shows the selected text in <b>every font on your Mac</b>, one per row, with its name and how many styles it has; with nothing selected, it shows a sample sentence.",
              "用这台 Mac 上的<b>每一种字体</b>显示选中的文字，一行一种，写着字体的中文名和英文名、有几种样式；什么都没选时用一句示例。"),
            T("Filter by All, Chinese, Western, Monospaced or Favorites, search by name and change the size. With text selected, only the fonts that can show all of it are listed.",
              "按「全部」「中文」「西文」「等宽」「收藏」筛选，可以搜索字体名、调字号；选了文字时默认只列能完整显示它的字体。"),
            T("Star the fonts you use. Right-click a row to copy the font name, the PostScript name or the CSS, or copy the row as an image.",
              "点星号收藏常用的字体；右键复制字体名、PostScript 名、CSS 的写法，或者把这一行复制成图片。"),
            T("Select font files (.ttf, .otf, .ttc) to see each face before installing, then <b>install</b> them into ~/Library/Fonts with one click.",
              "选中字体文件（.ttf、.otf、.ttc）时不用装就能先看每一款的样子，一键<b>装到</b>「~/资源库/Fonts」。"),
        ],
        "scene": {
            "src": {"kind": "text", "app": T("Pages", "Pages 文稿"), "title": T("Market poster.pages", "海报.pages"), "cap": T("Select a headline", "选中一句标题"),
                    "lines": [T("# Autumn market", "# 秋日市集"), T("[[Fresh bread & cider]]", "[[落霞与孤鹜齐飞]]"),
                              T("Saturday 8 am to noon · Town Hall Square", "周六上午 8 点到中午 · 市政厅广场")]},
            "card": {"w": 380,
                     "body": [{"t": "field", "value": T("Fresh bread & cider", "落霞与孤鹜齐飞")},
                              {"t": "seg", "items": [T("All", "全部"), T("Chinese", "中文"), T("Western", "西文"), T("Monospaced", "等宽"), T("Favorites", "收藏")],
                               "on": T(0, 1), "ctl": 2},
                              _fp_panes({1}, {0}),
                              {"t": "html", "html": T('<div class="pl-seg-row">' + _check("Only fonts that can show it") + "</div>",
                                                      '<div class="pl-seg-row">' + _check("只看能显示的") + "</div>")},
                              {"t": "note", "text": T("84 fonts can show all of this text", "31 种字体能完整显示这段文字")}]},
            "steps": [
                {"cap": T("Your text in every font", "每一种字体都看一遍"), "acts": [], "hold": 1500},
                {"cap": T("Star the ones you like", "收藏喜欢的字体"),
                 "acts": [["click", ".pl-card .pl-pane.is-on .pl-fstar[data-k='2']"],
                          ["set", 2, _fp_panes({1, 2}, {0, 2})], ["wait", 600],
                          ["click", "opt:1.4"]], "hold": 1300},
                {"cap": T("Right-click to copy the CSS", "右键复制 CSS"), "sub": T("Or the font name, or the row as an image.", "也能复制字体名，或者把这一行复制成图片。"),
                 "acts": [["hover", ".pl-card .pl-pane.is-on .pl-b-html > div > div"], ["wait", 300], ["toast", T("Copied", "已复制")]]},
            ],
        },
    },

    # ------------------------------------------------------------------ Clean Up Text
    "textCleanup": {
        "chips": [T("Join broken lines", "合并换行"), T("Simplified ↔ Traditional", "简繁转换"), T("Pinyin", "拼音")],
        "points": [
            T("<b>Joins lines</b> broken in the middle of sentences, as in text copied from a PDF; a word split with a hyphen at the end of a line is put back together. Paragraphs stay apart.",
              "把被硬换行切开的句子<b>接起来</b>（从 PDF 复制的文字常见），行尾用连字符断开的英文单词也接回去；空行分开的段落还是分开。"),
            T("Removes blank lines, extra spaces and invisible characters such as zero-width spaces, and turns full-width letters and digits into half-width ones.",
              "去掉空行、多余空格和零宽空格这类看不见的字符，全角字母数字转半角。"),
            T("Adds spaces between Chinese and Latin text, converts between Simplified and Traditional Chinese, and gives pinyin with or without tones.",
              "中英文之间加空格、简繁转换，汉字转拼音（带声调或不带）。"),
            T("Also sorts lines and removes duplicates. Only the cleanups that change your text are listed: copy one, or put it in place of the selection.",
              "还能按行排序、去重。只列出会让文字变样的整理方式，结果可以复制，也可以直接替换原文。"),
        ],
        "scene": {
            "src": {"kind": "text", "app": T("Notes", "备忘录"), "title": T("Copied from a PDF", "从 PDF 复制的"), "cap": T("Select text with broken lines", "选中被切断的文字"),
                    "lines": T(["# Office move", "[[The new office opens on Monday,  Oct-", "ober 6. Bring your badge and update", "your parking details by Friday.]]"],
                               ["# 项目周报", "[[我们用React重写了前端，", "页面加载时间从3秒降到了", "0.8秒。]]"])},
            "card": {"title": T("Clean Up Text", "文字整理"), "w": 380,
                     "body": [{"t": "rows", "rows": T(
                         [["Join Lines", "The new office opens on Monday, October 6…"],
                          ["Remove Extra Spaces", "The new office opens on Monday, Oct-…"],
                          ["Sort Lines", "ober 6. Bring your badge…"]],
                         [["合并换行", "我们用React重写了前端，页面加载时间从3秒降到了0.8秒。"],
                          ["中英文空格", "我们用 React 重写了前端，\n页面加载时间从 3 秒降到了…"],
                          ["转为繁体", "我們用React重寫了前端，\n頁面加載時間從3秒降到了…"],
                          ["拼音", "wǒ men yòng React zhòng xiě le qián duān，yè miàn jiā zài…"],
                          ["无调拼音", "wo men yong React zhong xie le qian duan，ye mian jia zai…"],
                          ["按行排序", "0.8秒。\n我们用React重写了前端，…"]])}]},
            "steps": [
                {"cap": T("Every cleanup that changes it", "列出能做的整理"), "sub": T("Only the ones that make a difference.", "只列会让文字变样的。"), "acts": [], "hold": 1600},
                {"cap": T("Copy any version", "哪一种都能复制"), "acts": [["click", ".pl-card .pl-row[data-i='2'] .pl-ib", ["toast", T("Copied", "已复制")]]]},
                {"cap": T("Or put it back, joined", "或者接好了直接换回去"), "sub": T("Replace puts it in place of the selection.", "替换原文，放回选中的地方。"),
                 "acts": [["click", "row:0.0"], ["replace", T("The new office opens on Monday,  October 6. Bring your badge and update your parking details by Friday.",
                                                             "我们用React重写了前端，页面加载时间从3秒降到了0.8秒。")]], "hold": 1800},
            ],
        },
    },

    # ------------------------------------------------------------------ Extract Info
    "extractInfo": {
        "chips": [T("Links · Emails", "链接 · 邮箱"), T("Phone numbers", "电话号码"), T("IP addresses", "IP 地址")],
        "points": [
            T("Select an email, a web page or a chat and get <b>each link, email address, phone number and IP address</b> on its own row, in order and without duplicates.",
              "选中一封邮件、一段网页或者聊天记录，<b>链接、邮箱、电话号码、IP 地址</b>一项一行列出来，按出现的顺序，去掉重复的。"),
            T("Phone numbers include mobile numbers, landlines with an area code, 400 and 800 numbers, and international numbers starting with +.",
              "电话号码认得手机号、带区号的固定电话、400 电话，还有 + 开头的国际号码。"),
            T("Copy one, or every one of a kind at once. With 2 to 10 links, open them all (addresses without http open as https).",
              "可以逐个复制，也可以一类一起复制；找到 2 到 10 个链接时能一次全部打开（没写 http 的按 https 打开）。"),
            T("File names such as main.py or Pop.app aren’t mistaken for web addresses.", "main.py、Pop.app 这样的文件名不会被当成网址。"),
        ],
        "scene": {
            "src": {"kind": "text", "app": T("Mail", "邮件"), "title": T("Kickoff details", "周五团建"),
                    "lines": T(["# Kickoff details", "[[Agenda: https://example.com/kickoff", "Call Ana at +1 415 555 0132 or email ana@example.com.",
                                "Backup line (415) 555-0199 · RSVP at www.example.com/rsvp", "Staging server: 10.0.4.21]]"],
                               ["# 周五团建", "[[报名表：https://forms.example.cn/team，周三前填好", "有问题打 138 0013 8000 找小林，或者发邮件到 lin@example.cn",
                                "行政电话 021-62881234，照片传到 www.example.cn/photos", "打印机在 192.168.1.20]]"])},
            "card": {"title": T("Extract Info", "提取信息"), "w": 380,
                     "btns": [T("Copy Every Link", "复制全部链接"), T("Copy Every Phone", "复制全部电话"), T("Open All Links", "打开全部链接")],
                     "body": [{"t": "rows", "rows": T(
                         [["Link 1", "https://example.com/kickoff"], ["Phone 1", "+1 415 555 0132"], ["Email 1", "ana@example.com"],
                          ["Phone 2", "(415) 555-0199"], ["Link 2", "www.example.com/rsvp"], ["IP Address 1", "10.0.4.21"]],
                         [["链接 1", "https://forms.example.cn/team"], ["电话 1", "138 0013 8000"], ["邮箱 1", "lin@example.cn"],
                          ["电话 2", "021-62881234"], ["链接 2", "www.example.cn/photos"], ["IP 地址 1", "192.168.1.20"]])},
                              {"t": "note", "text": T("Link: 2, Email: 1, Phone: 2, IP Address: 1", "2 个链接，1 个邮箱，2 个电话，1 个 IP 地址")}]},
            "steps": [
                {"cap": T("Every link, email, phone and IP", "链接、邮箱、电话、IP 一项一行"), "acts": [], "hold": 1600},
                {"cap": T("Copy one", "逐个复制"), "acts": [["click", ".pl-card .pl-row[data-i='2'] .pl-ib", ["toast", T("Copied", "已复制")]]]},
                {"cap": T("Or a whole kind at once", "或者一类一起复制"), "sub": T("With a few links, open them all.", "链接不多时还能一次全部打开。"),
                 "acts": [["click", "btn:1", ["toast", T("Copied", "已复制")]]]},
            ],
        },
    },

    # ------------------------------------------------------------------ ID Numbers
    "idNumber": {
        "chips": [T("Check digit", "校验位"), T("Birth date · Age · Sex", "出生日期 · 年龄 · 性别"), T("Offline", "不联网")],
        "points": [
            T("Select a Chinese resident ID number, a unified social credit code or a bank card number, and Pop <b>checks the last digit</b>. When it’s wrong, it says what it should be, given the other digits.",
              "选中身份证号、统一社会信用代码或银行卡号，Pop <b>检查最后一位校验码</b>对不对；输错时告诉你按前面的数字最后一位应该是什么。"),
            T("ID numbers give the date of birth, age, sex and region; old 15-digit numbers are converted to 18 digits.",
              "身份证读出出生日期、年龄、性别和地区，老的 15 位号码换算成 18 位。"),
            T("Credit codes give the registration authority, the organization type, where it’s registered and the organization code; bank cards give the card network and the number in groups of four.",
              "信用代码读出登记管理部门、机构类别、登记地和组织机构代码；银行卡读出卡组织，按 4 位一组写好。"),
            T("Everything is worked out from the number itself, <b>offline</b>; copy it all as text.", "全部按号码本身推算，<b>不联网</b>；结果可以一起复制。"),
        ],
        "scene": {
            "src": {"kind": "text", "app": T("Numbers", "Numbers 表格"), "title": T("Visitor log", "访客登记"), "cap": T("Select an ID number", "选中一个证件号码"),
                    "lines": [T("# Visitor log", "# 访客登记"), T("ID number: [[11010519491231002X]]", "身份证号：[[11010519491231002X]]"),
                              T("Visiting: Room 402 · 10:30", "来访：402 室 · 10:30")]},
            "card": {"title": T("Resident ID Card", "居民身份证"), "w": 340, "btns": [T("Copy", "复制")],
                     "body": [{"t": "text", "text": T("The check digit is valid", "校验通过")},
                              {"t": "rows", "rows": [[T("Check digit", "校验"), T("Pass", "通过"), "ok"], [T("Date of birth", "出生日期"), T("1949-12-31", "1949 年 12 月 31 日")],
                                                     [T("Age", "年龄"), T("76 years", "76 岁")], [T("Sex", "性别"), T("Female", "女")],
                                                     [T("Region", "地区"), T("北京 (110105)", "北京（110105）")]]},
                              {"t": "note", "text": T("Derived from the number itself; nothing is looked up online", "只根据号码本身推算，不联网查询")}]},
            "steps": [
                {"cap": T("The check digit is right", "校验位没问题"), "sub": T("If not, it says what the last digit should be.", "输错时会说最后一位应该是什么。"),
                 "acts": [["move", ".pl-card .pl-row[data-i='0'] .pl-row-v"]], "hold": 1200},
                {"cap": T("Birth date, age, sex and region", "出生日期、年龄、性别和地区"), "sub": T("Worked out from the number, offline.", "全按号码本身推算，不联网。"),
                 "acts": [["move", ".pl-card .pl-row[data-i='1'] .pl-row-v"], ["wait", 500], ["move", ".pl-card .pl-row[data-i='2'] .pl-row-v"], ["wait", 400],
                          ["move", ".pl-card .pl-row[data-i='4'] .pl-row-v"]], "hold": 1100},
                {"cap": T("Copy it all", "一起复制"), "acts": [["click", "btn:0", ["toast", T("Copied", "已复制")]]]},
            ],
        },
    },

    # ------------------------------------------------------------------ Lines
    "lineTools": {
        "chips": ["SQL IN ('…')", T("JSON array", "JSON 数组"), T("Number, reverse, shuffle", "序号、倒序、打乱")],
        "points": [
            T("Select a column of values, one per line, and <b>quote them for an SQL IN list</b>: single quotes and commas, with quotes inside escaped.",
              "选中一列值（每行一个），<b>加上单引号和逗号</b>，正好放进 SQL 的 IN 列表，单引号自动转义。"),
            T("Or double-quote them, make a JSON array, join them with commas, add or remove numbering, remove quotes, reverse or shuffle them.",
              "也可以加双引号、转 JSON 数组、用逗号连起来、加序号或者去掉序号、去掉引号、倒序、打乱。"),
            T("A single line separated by commas, semicolons, tabs or vertical bars (Chinese punctuation too) is split into lines.",
              "一行里用逗号、顿号、分号、竖线或者制表符隔开的，可以拆成多行。"),
            T("Copy any version, or put it in place of the selection.", "每一种都可以复制，也可以直接替换原文。"),
        ],
        "scene": {
            "src": {"kind": "text", "app": T("TextEdit", "文本编辑"), "title": "refunds.sql", "mono": True, "cap": T("Select a column of values", "选中一列值"),
                    "sub": T("Pasted from a spreadsheet, one per line.", "从表格里粘过来的，一行一个。"),
                    "lines": [T("-- orders to refund", "-- 要退款的订单"), "SELECT * FROM orders", "WHERE id IN (", "  [[A-1024", "  A-1031", "  A-1047", "  B-2002]]", ");"]},
            "card": {"title": T("Lines", "按行处理"), "w": 380,
                     "body": [{"t": "rows", "rows": [
                         [T("Comma-Separated", "逗号隔开"), "A-1024, A-1031, A-1047, B-2002"],
                         [T("Single-Quoted", "单引号"), "'A-1024', 'A-1031', 'A-1047', 'B-2002'"],
                         [T("Double-Quoted", "双引号"), '"A-1024", "A-1031", "A-1047", "B-2002"'],
                         [T("JSON Array", "JSON 数组"), '["A-1024", "A-1031", "A-1047", "B-2002"]'],
                         [T("Add Numbering", "加序号"), "1. A-1024\n2. A-1031…"],
                         [T("Reverse", "倒序"), "B-2002\nA-1047…"],
                         [T("Shuffle", "打乱顺序"), "A-1047\nB-2002…"]]},
                              {"t": "note", "text": T("4 items", "共 4 项")}]},
            "steps": [
                {"cap": T("Every way to write the list", "列出各种写法"), "acts": [], "hold": 1500},
                {"cap": T("Copy it as a JSON array", "复制成 JSON 数组"), "acts": [["click", ".pl-card .pl-row[data-i='3'] .pl-ib", ["toast", T("Copied", "已复制")]]]},
                {"cap": T("Or quote it right there for SQL IN", "或者就地加上单引号"), "sub": T("Replace puts it in place of the selection.", "替换原文，放回选中的地方。"),
                 "acts": [["click", "row:0.1"], ["replace", "'A-1024', 'A-1031', 'A-1047', 'B-2002'"]], "hold": 1800},
            ],
        },
    },

    # ------------------------------------------------------------------ Add to Reminders
    "reminder": {
        "chips": [T("“Friday at 3 pm”", "「周五下午 3 点」"), T("Reminders", "提醒事项"), T("Calendar", "日历")],
        "points": [
            T("Select a sentence with a time in it, such as “明天下午 3 点和设计组过一遍截图” (go over the screenshots with the design team tomorrow at 3 pm), and Pop <b>picks out the time and the task</b>. It knows Chinese phrases for today, tomorrow, weekdays and next week, dates, “in 3 days”, “in half an hour”, morning, afternoon and evening, half past and a quarter past.",
              "选中一句话，比如「明天下午 3 点和设计组过一遍截图」「周五之前交周报」「半小时后给妈妈打电话」，Pop <b>认出时间和要做的事</b>：今天明天后天、周几和下周几、几月几号、几天后、半小时后、上午下午晚上几点几分、几点半、一刻都认得。"),
            T("English sentences such as “tomorrow at 3pm” are read by the system’s date detection.", "英文交给系统识别（tomorrow at 3pm）。"),
            T("Change the to-do, date and time if you like, then add it to Reminders, where a time gets an alert, or to Calendar, where a day without a time becomes an all-day event. The original sentence goes into the notes.",
              "标题、日期和时间都可以再改，然后加到「提醒事项」（说了几点的到点提醒）或者「日历」（没说几点的是全天日程），原文放在备注里。"),
            T("The first time, macOS asks for permission. Calendar only needs write access: Pop doesn’t read your events.",
              "第一次用时系统会问要不要允许；日历只申请写入权限，不读你的日程。"),
        ],
        "scene": {
            "src": {"kind": "text", "app": T("Notes", "备忘录"), "title": T("This week", "本周"),
                    "lines": [T("# This week", "# 本周"),
                              T("[[Remind me to send the design files Friday at 3 pm]]", "[[提醒我周五下午 3 点交设计稿]]"),
                              T("Book the meeting room for Monday", "订好周一的会议室"), T("Reply to Sam about the invoice", "回复小林发票的事")]},
            "card": {"title": T("Add to Reminders", "加到提醒事项"), "w": 330, "btns": [T("Add to Reminders", "加到提醒事项"), T("Add to Calendar", "加到日历")],
                     "body": [{"t": "field", "value": T("send the design files", "交设计稿")},
                              {"t": "html", "html": T('<div class="pl-seg-row"><span class="pl-field pl-mono">10/2/2026, 3:00 PM</span>' + _check("Set a time") + "</div>",
                                                      '<div class="pl-seg-row"><span class="pl-field pl-mono">2026/10/2 15:00</span>' + _check("指定时间") + "</div>")},
                              {"t": "note", "text": T("Fri, Oct 2, 15:00 · in 2 days", "10月2日 周五 15:00 · 后天")}]},
            "steps": [
                {"cap": T("It finds the time and the task", "认出时间和要做的事"), "acts": [], "hold": 1700},
                {"cap": T("Change anything you like", "想改就改"), "sub": T("The to-do, the date or the time.", "标题、日期、时间都能改。"),
                 "acts": [["click", "b:0"], ["type", 0, T("Send the design files to Sam", "交设计稿给小林")]], "hold": 900},
                {"cap": T("Add it to Reminders", "加到「提醒事项」"), "sub": T("Or to Calendar: without a time, it’s an all-day event.", "或者加到「日历」：没说几点的是全天日程。"),
                 "acts": [["click", "btn:0"], ["close"], ["toast", T("Added to Reminders", "已加到提醒事项")]]},
            ],
        },
    },

    # ------------------------------------------------------------------ Spell Check
    "spellCheck": {
        "chips": [T("Built into macOS", "系统自带"), T("Offline", "离线"), T("Replace in place", "直接替换原文")],
        "points": [
            T("Select text in English or another language and Pop finds the <b>misspelled words</b> with macOS’s own spell checking, offline.",
              "选中外文，Pop 用系统自带的拼写检查找出<b>拼错的词</b>，不联网。"),
            T("Each one is listed with up to four suggestions.", "每个拼错的词列出最多四个改法。"),
            T("Above them is the whole text with each word replaced by its first suggestion: copy it, or put it in place of the selection.",
              "上面是按第一个建议改好的整段文字，可以复制，也可以直接替换原文。"),
            T("When nothing is wrong, Pop just says so.", "没有拼错时，Pop 只提示一句。"),
        ],
        "scene": {
            "src": {"kind": "text", "app": T("Mail", "邮件"), "title": "Re: Your order",
                    "lines": ["Hi Sam,", "[[Thanks for your patience. We will definately send the reciept to your new adress tommorow.]]", "Best, Ana"]},
            "card": {"title": T("Spell Check", "拼写检查"), "w": 360, "btns": [T("Copy", "复制"), T("Replace", "替换原文")],
                     "body": [{"t": "text", "text": "Thanks for your patience. We will definitely send the receipt to your new address tomorrow."},
                              {"t": "rows", "copy": False, "rows": [["definately", "definitely / defiantly"], ["reciept", "receipt / recipe"],
                                                                    ["adress", "address / dress / adders"], ["tommorow", "tomorrow / tomorrows"]]},
                              {"t": "note", "text": T("Found 4 spelling issues; above is the text corrected with the first suggestions",
                                                      "发现 4 处拼写问题；上面是按第一个建议改好的文字")}]},
            "steps": [
                {"cap": T("The text, corrected", "改好的整段文字"), "sub": T("Each word fixed with its first suggestion.", "每个词按第一个建议改。"),
                 "acts": [["move", "b:0"]], "hold": 1300},
                {"cap": T("Each misspelling, with suggestions", "每个拼错的词和改法"),
                 "acts": [["move", ".pl-card .pl-row[data-i='0'] .pl-row-v"], ["wait", 500], ["move", ".pl-card .pl-row[data-i='2'] .pl-row-v"], ["wait", 400],
                          ["move", ".pl-card .pl-row[data-i='3'] .pl-row-v"]], "hold": 900},
                {"cap": T("Replace the selection", "直接替换原文"), "sub": T("Or copy the corrected text.", "也可以复制改好的文字。"),
                 "acts": [["click", "btn:1"], ["replace", "Thanks for your patience. We will definitely send the receipt to your new address tomorrow."]], "hold": 1800},
            ],
        },
    },

    # ------------------------------------------------------------------ Compare Text
    "textDiff": {
        "chips": [T("Clipboard ↔ selection", "剪贴板 ↔ 选中的文字"), T("Changed words marked", "标出改了哪些词"), T("Copy the diff", "复制差异")],
        "points": [
            T("Copy one version, select the other, and Pop <b>compares them line by line</b>.", "先复制一版，再选中另一版，Pop <b>按行对比</b>两段文字。"),
            T("Removed lines are red, added lines green, and the words that changed within a line (characters, in Chinese) are darker.",
              "删去的行标红、新增的行标绿，行里具体改了哪些词（中文按字）颜色更深。"),
            T("Long stretches that are the same fold away. Copy the differences as text.", "大段相同的内容自动折叠；差异可以复制下来。"),
            T("When the two are identical, Pop just says so.", "两段完全相同时，Pop 只提示一句。"),
        ],
        "scene": {
            "src": {"kind": "text", "app": T("Notes", "备忘录"), "title": T("Invite", "邀请"),
                    "cap": T("Copy one version, select the other", "先复制一版，再选中另一版"), "sub": T("It compares the selection with the clipboard.", "拿选中的文字和剪贴板里的对比。"),
                    "lines": T(["# Draft · copied", "The launch review is on Tuesday at 10 am.", "Please bring the latest numbers.",
                                "# Final", "[[The launch review is on Thursday at 2 pm.", "Please bring the latest numbers.", "Dial-in details are in the invite.]]"],
                               ["# 初稿 · 已复制", "发布评审定在周二上午 10 点。", "请带上最新的数据。",
                                "# 定稿", "[[发布评审改到周四下午 2 点。", "请带上最新的数据。", "线上参会的链接在邀请里。]]"])},
            "card": {"title": T("Compare Text", "文本对比"), "w": 390, "at": "right", "btns": [T("Copy", "复制")],
                     "body": [{"t": "diff", "lines": T(
                         [["-", "The launch review is on {-Tuesday-} at {-10 am-}."], ["+", "The launch review is on {+Thursday+} at {+2 pm+}."],
                          [" ", "Please bring the latest numbers."], ["+", "{+Dial-in details are in the invite.+}"]],
                         [["-", "发布评审{-定在-}周{-二上-}午 {-10-} 点。"], ["+", "发布评审{+改到+}周{+四下+}午 {+2+} 点。"],
                          [" ", "请带上最新的数据。"], ["+", "{+线上参会的链接在邀请里。+}"]])},
                              {"t": "note", "text": T("Clipboard → selection: 1 line removed, 2 lines added. Red is only on the clipboard; green is only in the selection.",
                                                      "剪贴板 → 选中的文字：删去 1 行，新增 2 行。红色是只在剪贴板里有的，绿色是只在选中的文字里有的。")}]},
            "steps": [
                {"cap": T("See what changed", "看哪里改了"), "sub": T("Red was copied; green is selected.", "红色是剪贴板里的，绿色是选中的。"), "acts": [], "hold": 2000},
                {"cap": T("Copy the differences", "复制差异"), "acts": [["click", "btn:0", ["toast", T("Copied", "已复制")]]]},
            ],
        },
    },

    # ------------------------------------------------------------------ Emoji & Symbols
    "emojiSymbols": {
        "chips": ["😄 🐱 🎉", T("smile · 笑 · xiao", "笑 · xiao · smile"), "→ ① ℃ ⌘"],
        "points": [
            T("Search emoji in Chinese, pinyin, pinyin initials or English (“笑”, “dx”, “smile”), or browse them by category: smileys, people, animals, food, travel, activities, objects, symbols and flags.",
              "用中文、拼音、拼音首字母或者英文搜表情（「笑」「dx」「smile」），也能按笑脸、人物、动物、食物、旅行、活动、物品、符号、旗帜一类类看。"),
            T("Everyday special symbols have names you can search: check marks, arrows, circled and Roman numerals, math, punctuation, units and currency (℃, ㎡, ¥, €), shapes, Greek letters, superscripts and subscripts, and Mac key symbols (⌘ ⌥ ⇧).",
              "常用的特殊符号都有中文名能搜：对勾和叉、箭头、带圈数字和罗马数字、数学符号、标点（直角引号、书名号、省略号）、单位和货币（℃、㎡、¥、€）、形状、希腊字母、上标和下标、Mac 的按键符号（⌘ ⌥ ⇧）。"),
            T("Click one or press Return to <b>insert it where you’re typing</b>, or press ⌘C to copy it. Choose a skin tone for people and hands; recently used ones come first.",
              "点一下或者按回车就<b>插到正在打字的地方</b>，⌘C 复制；人物和手势可以选肤色，最近用过的排在前面。"),
            T("Select a word first and Pop searches for it, then replaces it with the emoji you pick.", "选中一个词再用，就拿它来搜，选好的表情直接把它换掉。"),
        ],
        "scene": {
            "src": {"kind": "text", "app": T("Messages", "信息"), "title": T("Ana", "小林"), "cap": T("Click where you’re typing", "在要打字的地方点一下"),
                    "sub": T("Or select a word to swap it for an emoji.", "也可以选中一个词，换成表情。"), "sum": T("Nothing selected", "未选中内容"),
                    "lines": [T("Dinner at 7? I’ll bring the cake.", "晚上 7 点吃饭？我带蛋糕。"), T("Sure! Bring the cat photos too [[\u00a0]]", "好呀！把猫的照片也带上[[\u00a0]]")]},
            "card": {"title": T("Emoji & Symbols", "表情和符号"), "w": 380,
                     "body": [{"t": "field", "ph": T("Search emoji and symbols: smile, cat, check, arrow", "搜表情和符号：笑、猫、对勾、箭头、smile")},
                              {"t": "seg", "items": [T("Recent", "最近"), T("Emoji", "表情"), T("Symbols", "符号")], "on": 1, "ctl": 2},
                              {"t": "panes", "on": 1, "panes": [
                                  [],
                                  [_cat_bar(["😀", "👋", "🐱", "🍎", "✈️", "⚽️", "💡", "❤️", "🏁"]), {"t": "grid", "cols": 10, "on": 0, "items": _SMILEYS}],
                                  [_cat_bar(["±", "→", "①", "「」", "℃", "★", "α", "x²", "⌘"]), {"t": "grid", "cols": 10, "on": 0, "items": _MATH}],
                                  [{"t": "grid", "cols": 10, "on": 0, "items": T(_CATS_EN, _CATS_ZH)}]]},
                              _emoji_foot("😀", T("grinning face", "嘿嘿"), T("嘿嘿 · U+1F600", "grinning face · U+1F600"))]},
            "steps": [
                {"cap": T("Browse emoji and symbols", "表情、符号一类类看"), "acts": [["wait", 500], ["click", "opt:1.2"], ["wait", 900], ["click", "opt:1.1"]], "hold": 700},
                {"cap": T("Or type to search", "或者打字搜"), "sub": T("In English, Chinese or pinyin.", "中文、拼音、英文都行。"),
                 "acts": [["type", 0, T("cat", "猫")], ["hide", 1], ["swap", 2, 3],
                          ["set", 3, _emoji_foot("🐈️", T("cat", "猫"), T("猫 · U+1F408 U+FE0F", "cat · U+1F408 U+FE0F"))]], "hold": 1000},
                {"cap": T("Click one to insert it", "点一下就插进去"), "sub": T("Or press Return; ⌘C copies.", "回车也行，⌘C 复制。"),
                 "acts": [["click", "cell:2.3", ["set", 3, T(_emoji_foot("🐱", "cat face", "猫脸 · U+1F431", "Return to insert · ⌘C to copy"),
                                                    _emoji_foot("😻", "花痴的猫", "smiling cat with heart-eyes · U+1F63B", "回车插入 · ⌘C 复制"))]], ["wait", 400],
                          ["replace", T("🐱", "😻")]], "hold": 1800},
            ],
        },
    },

    # ------------------------------------------------------------------ Inbox
    "quickNote": {
        "chips": [T("One Markdown file", "一个 Markdown 文件"), T("Date, time and app", "日期、时间和来源"), T("Nothing to open", "不用打开窗口")],
        "points": [
            T("Select text anywhere and it’s <b>appended to Pop 收集箱.md</b> in your Documents folder, without opening anything.",
              "在哪儿选中文字都行，<b>追加到「文稿」里的 Pop 收集箱.md</b>，不用打开任何窗口。"),
            T("Each entry starts with a heading: the date, the time and the app it came from.", "每一条前面是一个标题：日期、时间和从哪个 App 来的。"),
            T("It’s a plain Markdown file, created the first time you use it, and it follows your Documents folder.",
              "就是一个普通的 Markdown 文件，第一次用时自动建好，跟着你的「文稿」文件夹走。"),
        ],
        "scene": {
            "src": {"kind": "web", "app": T("Safari", "Safari浏览器"), "url": "blog.example.com/tools",
                    "lines": [T("Notes on good tools", "关于好工具"),
                              T("[[Good tools disappear: you notice the work, not the tool.]]", "[[好用的工具会隐形：你看到的是活儿，不是工具。]]"),
                              T("The best ones fit the hand so well that you forget they’re there.", "最好的那些顺手到让人忘了它们的存在。")],
                    "pic": "mug"},
            # Pop shows no card here: the text is appended to Documents › Pop 收集箱.md with a short notice.
            "steps": [
                {"cap": T("It’s added to your Inbox", "记进收集箱"), "sub": T("No window to open: just a short note.", "不用打开窗口，只提示一句。"),
                 "acts": [["toast", T("Added to Inbox", "已记到收集箱"), 2000]], "hold": 1200},
            ],
        },
    },
}
