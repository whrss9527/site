"""Mouse wheel settings, accidental-quit protection and scheduled system actions."""
from . import T


def desk(title):
    return {"kind": "desk", "app": "Pages", "title": title,
            "lines": [T("**A quiet evening on your Mac**", "**Mac 上安静的夜晚**"),
                      T("Keep working, with a few small helpers.", "几个小帮手，让你安心继续手上的事。") ]}


def sleep_notice():
    def html(title, detail, postpone, cancel):
        return (f'<div class="pl-bn"><div class="pl-bn-t"><strong>{title}</strong>'
                f'<span>{detail}</span></div></div><div class="pl-bn-btns">'
                f'<span class="pl-btn is-tint">{postpone}</span><span class="pl-btn">{cancel}</span></div>')
    return T(html("Sleeping soon", "Sleep in 00:59 · volume fading", "Postpone 10 min", "Cancel"),
             html("快要睡眠了", "00:59 后睡眠 · 音量慢慢调小", "推迟 10 分钟", "取消"))


DATA = {
    "mouseWheel": {
        "chips": [T("Wheel mice only", "只改滚轮鼠标"), T("1× · 2× · 3×", "1× · 2× · 3×"), T("Trackpad stays as it is", "触控板照旧")],
        "points": [
            T("Reverse <b>vertical wheel scrolling</b> independently of the Mac’s natural-scrolling setting. Horizontal wheel scrolling can be reversed too.", "单独把鼠标滚轮的<b>上下方向反过来</b>，不用改 Mac 的自然滚动设置；左右滚动也可以反过来。"),
            T("Choose <b>1×, 2× or 3×</b> scrolling speed. Trackpads, Magic Mouse and mice with smooth scrolling stay unchanged.", "滚动速度选 <b>1×、2× 或 3×</b>；触控板、妙控鼠标和开着平滑滚动的鼠标照旧。"),
            T("Allow Accessibility access when asked. Pop remembers the settings and resumes them at launch.", "第一次使用时允许辅助功能权限。设置会记住，Pop 启动时接着生效。"),
        ],
        "scene": {
            "src": desk(T("Reading a document", "读一份文档")),
            "card": {"at": "center", "w": 360, "body": [
                {"t": "list", "items": [{"title": T("Reverse wheel direction", "滚轮方向反过来"), "chk": False}]},
                {"t": "seg", "label": T("Scrolling speed", "滚动速度"), "items": ["1×", "2×", "3×"], "on": 0},
                {"t": "note", "text": T("Trackpad and Magic Mouse stay unchanged", "触控板和妙控鼠标照旧")},
            ], "btns": [T("Done", "完成")]},
            "steps": [
                {"cap": T("Reverse just the mouse wheel", "只反转鼠标滚轮"), "acts": [["click", "chk:0.0"], ["toast", T("Wheel down → page down with natural scrolling on", "自然滚动开着：滚轮向下，页面也向下")]]},
                {"cap": T("Scroll twice as fast", "滚得快一倍"), "acts": [["click", "opt:1.1"], ["wait", 500]]},
                {"cap": T("The settings are remembered", "下次启动接着生效"), "acts": [["click", "btn:0", [["close"], ["toast", T("Wheel settings saved", "已记住滚轮设置")]]]]},
            ],
        },
    },
    "holdToQuit": {
        "chips": [T("Hold ⌘Q", "按住 ⌘Q"), T("Or press twice", "也能连按两下"), T("Per-app exceptions", "App 可以例外")],
        "points": [
            T("A stray <b>⌘Q</b> leaves the app open. Choose holding the keys or pressing them twice, with a duration of 0.5, 1, 1.5 or 2 seconds.", "误按一下 <b>⌘Q</b> 不会退出整个 App。可以选按住，或者连按两下；时长选 0.5、1、1.5、2 秒。"),
            T("Add exceptions for apps that should quit immediately. Finder is left alone; installed Chrome starts on the exception list because it has its own quit guard.", "可以让一些 App 照旧一按就退出。访达不拦；Chrome 自己有退出保护，装了的话一开始就在例外列表里。"),
            T("Requires Accessibility access. During secure password entry, macOS hides keystrokes from other apps and ⌘Q works normally.", "需要辅助功能权限。输入密码时，系统不让其他 App 看到按键，这时 ⌘Q 照常一按就退出。"),
        ],
        "scene": {
            "src": desk(T("A document you want to keep open", "还想继续写的文稿")),
            "card": {"at": "center", "w": 380, "body": [
                {"t": "list", "items": [{"title": T("Don’t quit on a single ⌘Q", "误按一下 ⌘Q 不退出"), "chk": True}]},
                {"t": "seg", "label": T("Quit by", "怎样才退出"), "items": [T("Holding ⌘Q", "按住 ⌘Q"), T("Pressing ⌘Q twice", "连按两下 ⌘Q")], "on": 0},
                {"t": "seg", "label": T("Duration", "按住多久"), "items": ["0.5 s", "1 s", "1.5 s", "2 s"], "on": 1},
            ], "btns": [T("Done", "完成")]},
            "steps": [
                {"cap": T("Choose how to quit", "选怎样才退出"), "acts": [["hover", "opt:1.0"], ["wait", 400]]},
                {"cap": T("One accidental press keeps the app open", "误按一下，文稿还在"), "acts": [["click", "btn:0", ["close"]], ["key", "⌘Q"], ["toast", T("Hold ⌘Q to quit Pages", "按住 ⌘Q 才退出 Pages")]]},
                {"cap": T("Hold to confirm your intent", "按住一会儿，确认要退出"), "acts": [["key", "⌘Q"], ["card", {"title": T("Quit Pages", "退出 Pages"), "at": "center", "w": 300, "body": [{"t": "bar", "label": T("Holding ⌘Q", "按住 ⌘Q"), "from": 0, "to": 1, "dur": 1000}]}], ["wait", 1100], ["close"], ["toast", T("Quit confirmed — unsaved documents still ask to save", "确认退出；未保存的文稿仍会问要不要存")]], "hold": 900},
            ],
        },
    },
    "sleepTimer": {
        "chips": [T("Sleep · Lock · Shut Down", "睡眠 · 锁屏 · 关机"), T("After a while or at a time", "过一会儿或到几点"), T("Postpone or cancel", "推迟或取消")],
        "points": [
            T("Schedule <b>sleep, display sleep, lock or shutdown</b> after 15–120 minutes or at a time you choose.", "过 15–120 分钟或者到指定时间，让 Mac <b>睡眠、熄屏、锁屏或关机</b>。"),
            T("The final minute shows a notice. <b>Postpone by 10 minutes</b> or cancel if you’re still using the Mac.", "最后一分钟会提示，还在用电脑时可以<b>推迟 10 分钟</b>或者取消。"),
            T("Before sleep or shutdown, optionally fade the volume out. Apps can still ask you to save unsaved documents when shutting down.", "睡眠或关机前可以慢慢把音量调小。关机时，App 仍可能问要不要保存未存的文稿。"),
        ],
        "scene": {
            "src": desk(T("Finish listening, then sleep", "听完就睡")),
            "card": {"at": "center", "w": 360, "body": [
                {"t": "seg", "items": [T("Sleep", "睡眠"), T("Display Off", "熄屏"), T("Lock", "锁屏"), T("Shut Down", "关机")], "on": 0},
                {"t": "seg", "label": T("After", "过多久"), "items": [T("15 min", "15 分钟"), T("30 min", "30 分钟"), T("60 min", "60 分钟")], "on": 1},
                {"t": "list", "items": [{"title": T("Fade volume before sleep", "睡眠前慢慢调小音量"), "chk": True}]},
            ], "btns": [T("Start", "开始")]},
            "steps": [
                {"cap": T("Sleep in 30 minutes", "30 分钟后睡眠"), "acts": [["click", "btn:0", [["close"], ["toast", T("Sleep scheduled in 30 minutes", "已设为 30 分钟后睡眠")]]]]},
                {"cap": T("A notice in the final minute", "最后一分钟提醒一下"), "acts": [["fx", "start", {"name": "banner", "html": sleep_notice()}], ["wait", 700]]},
                {"cap": T("Still listening? Add ten minutes", "还在听？再等十分钟"), "acts": [["click", ".pl-banner .pl-btn.is-tint", [["fx", "stop"], ["toast", T("Sleep postponed by 10 minutes", "睡眠已推迟 10 分钟")]]]]},
            ],
        },
    },
}
