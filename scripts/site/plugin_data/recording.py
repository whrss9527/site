"""Plugin pages: recording and presenting plugins. See __init__.py and the README ("Plugin pages")."""
from . import T

# A slide-like document to present from.
REVIEW = [T("**Revenue** grew in every region this quarter.", "这个季度各地区的**收入**都在增长。"),
          T("The biggest jump: {{Asia Pacific, +38%}}", "涨得最多的是{{亚太区，+38%}}"),
          T("Next: hiring plan and Q4 targets.", "接下来：招聘计划和第四季度目标。")]

DATA = {
    "screenRecord": {
        "chips": ["MP4", T("Sound and microphone", "电脑声音和麦克风"), T("Then a GIF", "接着转 GIF")],
        "points": [
            T("<b>Drag out an area</b>, click a window, or press Return to record the whole screen. It’s saved as an MP4.",
              "<b>拖出一块区域</b>、单击选一个窗口，或者按回车录整个屏幕，存成 MP4。"),
            T("Record the Mac’s sound or the microphone, show clicks and the keys you press, and count down 3 seconds before it starts.",
              "可以录上电脑里的声音或者麦克风，显示鼠标点击和按下的键，开始前先倒数 3 秒。"),
            T("While recording, a timer sits in the menu bar; click it, or use Record Screen again, to stop.",
              "录的时候菜单栏里有个计时，点它或者再用一次「录屏」就停止。"),
            T("When it’s done, show the file in Finder or <b>convert it to a GIF</b> right away.",
              "录好以后可以在访达中显示，或者直接<b>转成 GIF</b>。"),
        ],
        "scene": {
            "src": {"kind": "desk", "title": T("Quarterly review", "季度回顾"), "lines": REVIEW},
            "steps": [
                {"cap": T("Drag out the area to record", "拖出要录的区域"), "sub": T("Or click a window, or press Return for the whole screen.", "也可以单击选一个窗口，或者按回车录整个屏幕。"),
                 "acts": []},
                {"cap": T("Recording", "开始录"), "sub": T("The timer in the menu bar stops it.", "点菜单栏里的计时就停止。"),
                 "acts": [["fx", "rec", 5], ["move", 0.42, 0.42], ["wait", 900], ["move", 0.6, 0.5], ["wait", 1200],
                          ["click", ".pl-mb-extra.is-rec"], ["fx", "end"], ["mb", "rec", False]]},
                {"cap": T("Saved as an MP4", "存成 MP4"), "sub": T("Show it in Finder, or turn it into a GIF.", "在访达中显示，或者转成 GIF。"),
                 "acts": [["card", {"title": T("Recording Finished", "录好了"), "w": 320, "at": "center",
                                    "body": [{"t": "img", "art": "screen", "ar": "16/10"},
                                             {"t": "note", "text": T("0:07 · 1280 × 720 · in Movies", "0:07 · 1280 × 720 · 存在「影片」")}],
                                    "btns": [T("Show in Finder", "在访达中显示"), T("Convert to GIF", "转成 GIF")], "tint": 1}],
                          ["click", "btn:1", ["toast", T("Converting to GIF…", "正在转成 GIF…")]]]},
            ],
            "fx": {"name": "region", "rect": [0.1, 0.22, 0.62, 0.5], "keep": True,
                   "hint": T("Drag out the area to record · Click a window · Return for the whole screen", "拖出要录的区域 · 单击录窗口 · 回车录整个屏幕")},
        },
    },
    "voiceRecorder": {
        "chips": [".m4a", T("Pause and resume", "可以暂停"), T("Then transcribe", "接着转成文字")],
        "points": [
            T("Record your voice from the microphone and save it as an <b>.m4a</b> in Downloads, named like “Recording 2026-10-01 15.42”.",
              "用麦克风录一段声音，存成 <b>.m4a</b> 放进「下载」，名字是「录音 2026-10-01 15.42」这样。"),
            T("While recording, a small bar at the top of the screen shows a red dot, the time and a level meter; pause, resume or stop from it. Screen recordings and screenshots leave the bar out.",
              "录的时候屏幕上方有个小条：红点、时长、跟着声音跳的音量条，可以暂停、接着录、停止；录屏和截图时看不到它。"),
            T("When it’s saved, show it in Finder or, with the Transcribe plugin, <b>turn it into text</b>.",
              "存好以后可以在访达中显示；装了「语音转文字」时还能<b>接着转成文字</b>。"),
            T("Use Voice Recorder again to stop. Quitting Pop saves the recording first.", "正在录的时候再用一次就停止；退出 Pop 时也会先存好。"),
        ],
        "scene": {
            "src": {"kind": "desk", "title": T("Interview notes", "采访笔记"),
                    "lines": [T("Questions for Thursday", "周四的问题"), T("1. How did the project start?", "1. 这个项目是怎么开始的？"), T("2. What surprised you most?", "2. 最让你意外的是什么？")]},
            "steps": [
                {"cap": T("Recording starts right away", "马上开始录"), "sub": T("The bar at the top shows the time and level.", "上方的小条显示时长和音量。"),
                 "acts": [["wait", 2600]]},
                {"cap": T("Stop when you’re done", "录完点停止"), "acts": [["click", ".pl-rb.is-stop"],
                    ["fx", "saved", {"name": T("Recording 2026-10-01 15.42.m4a", "录音 2026-10-01 15.42.m4a"), "sub": T("0:07 · in Downloads", "0:07 · 存在「下载」"),
                                     "btns": [T("Show in Finder", "在访达中显示"), T("Transcribe", "转成文字")]}]]},
            ],
            "fx": {"name": "recorder", "secs": 7},
        },
    },
    "scrollCapture": {
        "chips": [T("One long image", "拼成一张长图"), T("Web pages, chats, documents", "网页、聊天、长文档"), T("Then OCR", "接着识别文字")],
        "points": [
            T("<b>Select an area and scroll</b>: Pop captures as you go and stitches it all into one long image.",
              "<b>框选一块区域，一边往下滚动一边截</b>，拼成一张长图。"),
            T("Toolbars and bottom bars that stay put are kept only once.", "固定不动的工具栏和底栏只留一份。"),
            T("Web pages, chat histories and long documents all fit. Afterwards, <b>recognize the text</b> in the whole image if you like.",
              "网页、聊天记录、长文档都能截全，还能接着<b>识别整张长图里的文字</b>。"),
            T("Use it again while capturing to finish.", "正在截的时候再用一次就是完成。"),
        ],
        "scene": {
            "src": {"kind": "web", "app": "Safari", "url": "blog.example.com/field-notes", "cap": T("Open the page, or the chat", "打开要截的网页或者聊天"),
                    "sub": T("No need to select anything.", "什么都不用选。"),
                    "lines": [T("Field notes from the coast", "海边的田野笔记"), T("We left before sunrise and reached the cliffs by eight.", "天没亮就出发，八点到了悬崖边。"),
                              T("The tide was lower than the charts promised.", "潮水比潮汐表说的还要低。")],
                    "pic": "beach",
                    "more": [T("By noon the fog had lifted and the whole bay was visible.", "到中午雾散了，整个海湾都看得清清楚楚。"),
                             T("We counted forty-two seals on the rocks.", "礁石上数到了四十二只海豹。"),
                             T("The walk back took twice as long.", "回去的路走了两倍的时间。"),
                             T("Next time: bring a longer lens.", "下次记得带个长焦镜头。")]},
            "steps": [
                {"cap": T("Select the area that scrolls", "框选会滚动的那一块"), "sub": T("Just the part that moves works best.", "只框住会滚动的那一块最好。"),
                 "acts": []},
                {"cap": T("Scroll down while it captures", "一边往下滚动一边截"), "acts": [["move", 0.45, 0.6], ["fx", "scroll", 2600]]},
                {"cap": T("Use it again to finish", "再用一次就是完成"), "sub": T("Then recognize the text if you like.", "可以接着识别文字。"),
                 "acts": [["fx", "end"], ["card", {"w": 240, "at": "center", "title": T("Scrolling Screenshot", "滚动截图"), "sub": "1280 × 3940",
                                                   "body": [{"t": "img", "art": "doc", "ar": "1/1.6", "h": 230}],
                                                   "btns": [T("Copy", "复制"), T("Recognize Text", "识别文字")], "tint": 1}]]},
            ],
            "fx": {"name": "region", "rect": [0.12, 0.2, 0.6, 0.68], "keep": True,
                   "hint": T("Drag out the area to capture · Click a window · Esc cancels", "拖出要滚动截取的区域 · 单击截窗口 · Esc 取消")},
        },
    },
    "showKeystrokes": {
        "chips": ["⌘C · ⇧⌘4", T("Not your typing", "普通打字不显示"), "⌘Z ×3"],
        "points": [
            T("Shows the <b>shortcuts you press</b>, such as ⌘C and ⇧⌘4, plus Return and the arrow keys, at the bottom of the screen for demos and tutorials.",
              "演示、录教程时在屏幕下方显示按下的 <b>⌘C、⇧⌘4 这类组合键</b>，还有回车和方向键。"),
            T("Pressing the same one again shows a count, like “⌘Z ×3”.", "连按几次显示成「⌘Z ×3」。"),
            T("Ordinary typing isn’t shown, so passwords and messages stay private.", "普通打字不显示。"),
            T("Use it again to turn it off. Screen recordings can include it if you choose.", "再用一次关闭；录屏时也可以勾选一起录进去。"),
        ],
        "scene": {
            "src": {"kind": "desk", "title": T("Quarterly review", "季度回顾"), "lines": REVIEW},
            "steps": [
                {"cap": T("Press a shortcut", "按一个组合键"), "acts": [["wait", 400], ["fx", "key", "⌘C"], ["wait", 600], ["fx", "key", "⌘V"]]},
                {"cap": T("Repeats are counted", "连按会计数"), "acts": [["wait", 600], ["fx", "key", "⌘Z ×3"], ["wait", 500], ["fx", "key", "⇧⌘4"]]},
                {"cap": T("Use it again to turn it off", "再用一次关闭"), "acts": [["wait", 900], ["fx", "end"]]},
            ],
            "fx": {"name": "keys"},
        },
    },
    "screenPen": {
        "chips": [T("Pen and highlighter", "画笔和荧光笔"), T("Arrows, boxes, ovals", "箭头、方框、椭圆"), T("Fades by itself", "笔迹自动消失")],
        "points": [
            T("Draw <b>straight on the screen</b> while you present or record a tutorial: pen, highlighter, arrow, box and oval.",
              "演示、录教程时<b>直接在屏幕上画</b>：画笔、荧光笔、箭头、方框、椭圆。"),
            T("Hold ⇧ for straight lines and even shapes.", "按住 ⇧ 画直线和正的形状。"),
            T("Strokes can <b>fade away after a few seconds</b>, or stay while you keep working in the window underneath. Screen recordings include them.",
              "笔迹可以<b>几秒后自动消失</b>，也可以留着，接着操作下面的窗口；录屏时一起录进去。"),
            T("Press Esc or use it again to stop drawing.", "按 Esc 或者再用一次就结束。"),
        ],
        "scene": {
            "src": {"kind": "desk", "title": T("Quarterly review", "季度回顾"), "lines": REVIEW},
            "steps": [
                {"cap": T("Circle what matters", "圈出要讲的地方"), "acts": [["fx", "draw", {"shape": "oval", "target": ".pl-tgt"}]]},
                {"cap": T("Add an arrow, or highlight a line", "加个箭头，或者划重点"),
                 "acts": [["fx", "tool", 2], ["fx", "draw", {"shape": "arrow", "rect": [0.6, 0.38, 0.16, 0.18]}],
                          ["fx", "tool", 1], ["fx", "draw", {"shape": "line", "hl": True, "target": ".pl-doc p"}]]},
                {"cap": T("The strokes fade by themselves", "笔迹自己慢慢消失"), "sub": T("Or keep them and press Esc when you’re done.", "也可以留着，讲完按 Esc。"),
                 "acts": [["wait", 600], ["fx", "fade", 1000], ["fx", "end"]]},
            ],
            "fx": {"name": "pen"},
        },
    },
    "cameraBubble": {
        "chips": [T("Round or rounded square", "圆形或圆角方形"), T("Drag, resize", "拖动、换大小"), T("Switch cameras", "换摄像头")],
        "points": [
            T("Shows your camera in a <b>small round window</b> in a corner of the screen, so you appear in your recordings and demos.",
              "在屏幕角落用一个<b>圆形小窗</b>显示摄像头画面，录教程、演示时把自己也放进画面。"),
            T("Drag it anywhere; scroll or double-click to change its size.", "拖动换位置，滚动或双击换大小。"),
            T("Right-click to make it a rounded square or to switch cameras.", "右键换成圆角方形，或者换摄像头。"),
            T("Use it again to close it.", "再用一次关闭。"),
        ],
        "scene": {
            "src": {"kind": "desk", "title": T("Quarterly review", "季度回顾"), "lines": REVIEW},
            "steps": [
                {"cap": T("You appear in a corner", "你出现在角落里"), "acts": [["wait", 900]]},
                {"cap": T("Drag it where it fits", "拖到合适的位置"), "acts": [["fx", "drag", [24, 300]]]},
                {"cap": T("Make it bigger, or square", "放大，或者换成方形"), "sub": T("Scroll or double-click to resize; right-click for the shape.", "滚动或双击换大小，右键换形状。"),
                 "acts": [["fx", "grow"], ["wait", 500], ["fx", "shape", "square"], ["wait", 900], ["fx", "end"]]},
            ],
            "fx": {"name": "camera"},
        },
    },
    "pointerHighlight": {
        "chips": [T("Yellow halo", "黄色光圈"), T("Click ripples", "点击泛起波纹"), T("For demos", "演示时用")],
        "points": [
            T("Puts a <b>yellow halo</b> around the pointer so everyone can see where it is while you present or record.",
              "演示、录教程时在指针周围加一圈<b>黄色光圈</b>，让人一眼看到指针在哪。"),
            T("Each click sends out a ripple.", "按下鼠标时泛起波纹。"),
            T("Use it again to turn it off.", "再用一次关闭。"),
        ],
        "scene": {
            "src": {"kind": "desk", "title": T("Quarterly review", "季度回顾"), "lines": REVIEW},
            "steps": [
                {"cap": T("A halo follows the pointer", "指针周围多了一圈光"), "acts": [["move", ".pl-tgt"], ["move", 0.3, 0.6]]},
                {"cap": T("Clicks ripple", "点击泛起波纹"), "acts": [["click", ".pl-tgt"], ["wait", 500], ["click", ".pl-doc p"]]},
                {"cap": T("Use it again to turn it off", "再用一次关闭"), "acts": [["wait", 600], ["fx", "end"]]},
            ],
            "fx": {"name": "pointer"},
        },
    },
    "spotlight": {
        "chips": [T("Dims the rest", "其余压暗"), T("Follows the pointer", "跟着指针走"), T("Recorded too", "录屏时一起录")],
        "points": [
            T("<b>Dims the screen</b> except for a circle around the pointer, so people look where you point.",
              "把屏幕<b>压暗</b>，只亮着指针周围一圈，让大家看你指的地方。"),
            T("The light follows the pointer as you move.", "亮着的这一圈跟着指针走。"),
            T("Screen recordings include it. Use it again to turn it off.", "录屏时一起录进去；再用一次关闭。"),
        ],
        "scene": {
            "src": {"kind": "desk", "title": T("Quarterly review", "季度回顾"), "lines": REVIEW},
            "steps": [
                {"cap": T("Everything else dims", "其余的都暗下来"), "acts": [["move", ".pl-tgt"]]},
                {"cap": T("The light follows the pointer", "亮光跟着指针走"), "acts": [["move", ".pl-doc p"], ["wait", 400], ["move", 0.5, 0.42], ["wait", 300], ["move", ".pl-tgt"]]},
                {"cap": T("Use it again to turn it off", "再用一次关闭"), "acts": [["wait", 600], ["fx", "end"]]},
            ],
            "fx": {"name": "spotlight"},
        },
    },
    "zoom": {
        "chips": ["2× · 3×", T("Move to look around", "挪动指针换地方看"), T("Click to go back", "点一下回去")],
        "points": [
            T("<b>Magnifies the area around the pointer</b> so small text is easy to read during a demo.",
              "演示时<b>把指针附近放大</b>，看清小字。"),
            T("It magnifies the screen as it was at that moment; move the pointer to look around.", "放大的是那一刻的屏幕画面，挪动指针换地方看。"),
            T("Scroll or press ↑↓ to change the magnification; click or press Esc to go back.", "滚轮或 ↑↓ 调倍数，点一下或按 Esc 回去。"),
        ],
        "scene": {
            "src": {"kind": "desk", "title": T("Release notes", "发布说明"),
                    "lines": [T("Version 0.59.0 · {{Emoji & Symbols}} is new", "0.59.0 版 · 新增{{表情和符号}}"),
                              T("Search emoji by name in English or Chinese.", "用中文、拼音或者英文搜表情。"),
                              T("Time Zones: labels no longer cut off.", "时区换算：标签不再被截短。")]},
            "steps": [
                {"cap": T("The area around the pointer grows", "指针附近放大了"), "acts": [["wait", 600]]},
                {"cap": T("Move to look around", "挪动指针换地方看"), "acts": [["move", 0.62, 0.36], ["wait", 300], ["move", 0.4, 0.42]]},
                {"cap": T("Scroll for more, click to go back", "滚轮再放大，点一下回去"),
                 "acts": [["key", "↑"], ["fx", "zoom", 3], ["wait", 800], ["click", ".pl-doc"], ["fx", "end"]]},
            ],
            "fx": {"name": "zoom", "k": 2},
        },
    },
    "teleprompter": {
        "chips": [T("Space pauses", "空格暂停"), T("↑↓ speed", "↑↓ 调速度"), T("Hidden from recordings", "录屏时看不到")],
        "points": [
            T("Puts the script you select into a <b>teleprompter at the top of the screen</b>, right under the camera, scrolling up slowly so you can read it to the camera.",
              "把选中的稿子放进<b>屏幕上方的提词器</b>，就在摄像头下面，慢慢往上滚，对着摄像头读。"),
            T("Space pauses; ↑ and ↓ change the speed. Pop remembers the speed and the text size.", "空格暂停，↑↓ 调速度；速度和字号会记住。"),
            T("Screen recordings leave it out, so viewers never see the script.", "录屏时不会录进去，看的人看不到稿子。"),
        ],
        "scene": {
            "src": {"kind": "text", "app": "Pages", "title": T("Script.pages", "讲稿.pages"), "cap": T("Select your script", "选中讲稿"),
                    "lines": [T("# Welcome video", "# 欢迎视频"),
                              T("[[Hi, I’m Ada. In the next two minutes", "[[大家好，我是小林。接下来两分钟，"),
                              T("I’ll show you how to set up your first project,", "我带大家建好第一个项目，"),
                              T("invite your team, and share it with a link.]]", "邀请同事，再用链接分享出去。]]")]},
            "steps": [
                {"cap": T("The script scrolls under the camera", "稿子在摄像头下面慢慢滚"), "acts": [["wait", 1800]]},
                {"cap": T("Change the speed, or pause", "调速度，或者暂停"), "sub": T("↑↓ change the speed; Space pauses.", "↑↓ 调速度，空格暂停。"),
                 "acts": [["key", "↑"], ["fx", "speed", 0.032], ["wait", 1400], ["key", T("Space", "空格")], ["fx", "pause"], ["wait", 900], ["fx", "end"]]},
            ],
            "fx": {"name": "tele", "lines": [T("Hi, I’m Ada. In the next two minutes", "大家好，我是小林。接下来两分钟，"),
                                             T("I’ll show you how to set up your first project,", "我带大家建好第一个项目，"),
                                             T("invite your team, and share it with a link.", "邀请同事，再用链接分享出去。"),
                                             T("Let’s start with a new project.", "先新建一个项目。")]},
        },
    },
}
