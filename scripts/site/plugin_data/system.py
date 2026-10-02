"""Plugin pages: files and system plugins that work on the Mac itself (windows, apps, hardware,
timers). See __init__.py and the README ("Plugin pages")."""
from . import T


# ---------------------------------------------------------------- small helpers for the bespoke bits
def _pick(x, i):
    return x[i] if isinstance(x, T) else x


def _both(make):
    """T(make(0), make(1)): HTML built once per language."""
    return T(make(0), make(1))


def _svg(body, sw=1.7, size=None):
    wh = f' width="{size}" height="{size}"' if size else ""
    return (f'<svg viewBox="0 0 24 24"{wh} aria-hidden="true" fill="none" stroke="currentColor" stroke-width="{sw}" '
            f'stroke-linecap="round" stroke-linejoin="round">{body}</svg>')


# Line icons after the SF Symbols Pop uses in these cards.
IC = {
    "speaker": '<path d="M4 9.4h3.2L11.6 5v14l-4.4-4.4H4Z"/><path d="M15 9a4.2 4.2 0 0 1 0 6"/><path d="M17.6 6.6a7.6 7.6 0 0 1 0 10.8"/>',
    "airpods": '<path d="M8 4a3.2 3.2 0 0 0-3.2 3.2c0 1.8 1.4 3.2 3.2 3.2h.6V19a1.2 1.2 0 0 0 2.4 0V7.2A3.2 3.2 0 0 0 8 4Z"/>'
               '<path d="M16 4a3.2 3.2 0 0 1 3.2 3.2c0 1.8-1.4 3.2-3.2 3.2h-.6V19a1.2 1.2 0 0 1-2.4 0V7.2A3.2 3.2 0 0 1 16 4Z"/>',
    "display": '<rect x="3" y="4" width="18" height="12.5" rx="2"/><path d="M9 20.5h6M12 16.5v4"/>',
    "mic": '<rect x="8.6" y="2.8" width="6.8" height="11.6" rx="3.4"/><path d="M5.4 11a6.6 6.6 0 0 0 13.2 0M12 17.6v3.6"/>',
    "keyboard": '<rect x="2.4" y="6" width="19.2" height="12" rx="2.4"/><path d="M6 9.4h.1M9.4 9.4h.1M12.8 9.4h.1M16.2 9.4h.1M6 12.4h.1M9.4 12.4h.1M12.8 12.4h.1M16.2 12.4h1.8M7.6 15.2h8.8"/>',
    "mouse": '<rect x="6.5" y="3" width="11" height="18" rx="5.5"/><path d="M12 7v3"/>',
    "laptop": '<rect x="5" y="5" width="14" height="10" rx="1.5"/><path d="M2.5 18.5h19"/>',
    "app": '<rect x="4" y="4" width="16" height="16" rx="4.5"/>',
    "folder": '<path d="M3.5 7.5a2 2 0 0 1 2-2h4l2 2h7a2 2 0 0 1 2 2v8a2 2 0 0 1-2 2h-13a2 2 0 0 1-2-2Z"/>',
    "box": '<rect x="3.5" y="4.5" width="17" height="4.5" rx="1"/><path d="M5 9v9.5a1.5 1.5 0 0 0 1.5 1.5h11a1.5 1.5 0 0 0 1.5-1.5V9M10 13h4"/>',
    "gear": '<circle cx="12" cy="12" r="3"/><path d="M12 3.5v2.2M12 18.3v2.2M3.5 12h2.2M18.3 12h2.2M6 6l1.6 1.6M16.4 16.4 18 18M6 18l1.6-1.6M16.4 7.6 18 6"/>',
    "people": '<circle cx="9" cy="8.5" r="3"/><path d="M3.5 19a5.5 5.5 0 0 1 11 0"/><circle cx="16.5" cy="9" r="2.5"/><path d="M16 14a4.6 4.6 0 0 1 5 4.6"/>',
    "timer": '<circle cx="12" cy="13.4" r="7.8"/><path d="M12 13.4V9.2M9.6 2.8h4.8"/>',
    "headphones": '<path d="M3.6 15v-3a8.4 8.4 0 0 1 16.8 0v3"/><rect x="3.6" y="13.6" width="4.2" height="7" rx="1.6"/><rect x="16.2" y="13.6" width="4.2" height="7" rx="1.6"/>',
    "trackpad": '<rect x="2.6" y="4.4" width="15.4" height="11.4" rx="2"/><path d="m13.8 21-2.2-3.2a1.2 1.2 0 0 1 1.9-1.4l.9 1v-6.2a1.2 1.2 0 0 1 2.4 0v3.4l3 .6a1.5 1.5 0 0 1 1.2 1.7L20.4 21"/>',
    "clock": '<circle cx="12" cy="12" r="8.6"/><path d="M12 7.4V12l3 2"/>',
    "walk": '<circle cx="13.8" cy="4.4" r="1.9"/><path d="M12.8 7.8 11.2 13.6l2.8 3-.6 4.6M11.2 13.6l-1.8 3.8-3 3.2M7.4 11.6l2.6-3.2 2.8-.6 2 3.4 3 1.2"/>',
    "checkFill": '<circle cx="12" cy="12" r="9.4" fill="currentColor" stroke="none"/><path d="m7.6 12.2 3 3 5.8-6" stroke="#fff" stroke-width="2.2"/>',
}


def icon(name):
    return _svg(IC[name])


# App icons in Finder and in lists: a tinted square with a white glyph.
GLYPH = {
    "pencil": '<path d="m15.6 4.6 3.8 3.8L8.6 19.2l-4.6.8.8-4.6Z"/>',
    "wave": '<path d="M4 10v4M7.5 7v10M11 4v16M14.5 8v8M18 6v12"/>',
    "globe": '<circle cx="12" cy="12" r="8.5"/><path d="M3.5 12h17M12 3.5c2.6 2.6 2.6 14.4 0 17M12 3.5c-2.6 2.6-2.6 14.4 0 17"/>',
    "chart": '<path d="M5 19v-6M10 19V7M15 19v-9M20 19V4"/>',
    "sun": '<circle cx="12" cy="12" r="4"/><path d="M12 3v2M12 19v2M3 12h2M19 12h2M5.6 5.6 7 7M17 17l1.4 1.4M5.6 18.4 7 17M17 7l1.4-1.4"/>',
    "compass": '<circle cx="12" cy="12" r="8.6"/><path d="m15.6 8.4-2.1 5.1-5.1 2.1 2.1-5.1Z"/>',
    "hammer": '<path d="M13.5 4.5 19.5 10.5M9 9l6 6M4.5 19.5l6.8-6.8M13 4l3 3-3.5 3.5-3-3Z"/>',
    "note": '<path d="M9 18V6l10-2v12"/><circle cx="6.5" cy="18" r="2.5"/><circle cx="16.5" cy="16" r="2.5"/>',
    "mail": '<rect x="3.5" y="6" width="17" height="12" rx="2"/><path d="m4 7 8 6 8-6"/>',
    "lines": '<path d="M6 7h12M6 11h12M6 15h8"/>',
}


def app(name, c1, c2, glyph, **kw):
    return dict({"name": name, "kind": "app", "c1": c1, "c2": c2, "glyph": _svg(GLYPH[glyph], 2)}, **kw)


def _tiles(items, on=None, off=(), playing=None):
    """A row of icon tiles (Pop's layout and sound tiles), in the engine's chip style: opt:B.N clicks one."""
    def make(i):
        cells = []
        for k, (svg, label) in enumerate(items):
            style = ("height:auto;min-height:54px;flex-direction:column;justify-content:center;gap:4px;padding:7px 2px;"
                     "border-radius:9px;font-size:10px;text-align:center;min-width:0" + (";opacity:.4" if k in off else ""))
            lab = f'<span style="max-width:100%;overflow:hidden;text-overflow:ellipsis;white-space:nowrap">{_pick(label, i)}</span>'
            if k == playing:
                lab = f'<span style="display:flex;align-items:center;gap:4px;max-width:100%">{_playing_icon()}{lab}</span>'
            cells.append(f'<span class="pl-opt{" is-on" if k == on else ""}" style="{style}">{_svg(svg, 1.6, 20)}{lab}</span>')
        return ('<div class="pl-chips" style="display:grid;grid-template-columns:repeat(5,minmax(0,1fr));gap:6px">'
                + "".join(cells) + "</div>")
    return _both(make)


def _playing_icon():
    """The playing sound keeps moving (Pop animates its symbol): the engine's live wave bars, small, beside the name."""
    bars = "".join(f'<i style="--h:{h}"></i>' for h in (0.45, 0.9, 0.6, 1))
    return f'<span class="pl-wave is-live" style="height:10px;width:11px;gap:1.5px;flex:none">{bars}</span>'


def _buttons(btns, tint=None, note=None, text=None, dim=False):
    """A row of buttons inside the card body, for buttons that change as the card's state changes
    (the footer buttons are fixed): a small note or a line of text on the left. btn:B.N clicks one."""
    def make(i):
        st = ' style="opacity:.45"' if dim else ""
        b = "".join(f'<span class="pl-btn{" is-tint" if k == tint else ""}"{st}>{_pick(x, i)}</span>' for k, x in enumerate(btns))
        if note:
            n = f'<p class="pl-note" style="flex:1;min-width:0">{_pick(note, i)}</p>'
        elif text:
            n = f'<p style="flex:1;min-width:0;margin:0;font-size:12.5px">{_pick(text, i)}</p>'
        else:
            n = '<span style="flex:1"></span>'
        return f'<div style="display:flex;align-items:center;gap:8px">{n}{b}</div>'
    return {"t": "html", "html": _both(make)}


# ---------------------------------------------------------------- Bluetooth Devices
# Pop's own sample devices (DemoBluetooth): connected ones first, then by name. A row's control is Connect,
# Disconnect, or a spinner while it connects.
BT = {
    "airpods": ("AirPods Pro", "airpods", None),
    "keyboard": ("Magic Keyboard", "keyboard", 72),
    "trackpad": ("Magic Trackpad", "trackpad", None),
    "wh": ("WH-1000XM5", "headphones", None),
}


def _bt_list(connected, connecting=()):
    order = sorted(BT, key=lambda k: (k not in connected, BT[k][0].lower()))

    def make(i):
        rows = []
        for k in order:
            name, ic, battery = BT[k]
            on = k in connected
            if k in connecting:
                status, ctl = ("Connecting…", "正在连接…")[i], '<span style="width:44px;display:grid;place-items:center"><span class="pl-spin"></span></span>'
            elif on:
                status = (f"Connected · Battery {battery}%", f"已连接 · 电量 {battery}%")[i] if battery else ("Connected", "已连接")[i]
                ctl = f'<span class="pl-btn">{("Disconnect", "断开")[i]}</span>'
            else:
                status, ctl = ("Not Connected", "未连接")[i], f'<span class="pl-btn">{("Connect", "连接")[i]}</span>'
            color = "var(--pl-accent)" if on else "var(--pl-l2)"
            rows.append(f'<div class="pl-li" data-n="{k}"><span class="pl-li-ic" style="color:{color}">{_svg(IC[ic])}</span>'
                        f'<span class="pl-li-t"><span>{name}</span><small>{status}</small></span>{ctl}</div>')
        return '<div class="pl-list">' + "".join(rows) + "</div>"
    return {"t": "html", "html": _both(make)}


# ---------------------------------------------------------------- Break Reminder
def _br_switch(on):
    return {"t": "html", "html": _both(lambda i: (
        '<div style="display:flex;align-items:center;gap:8px;font-size:12.5px"><span style="flex:1">'
        f'{("Remind me to take breaks", "连续用电脑一段时间后提醒我休息")[i]}</span><span class="pl-sw2{" is-on" if on else ""}"></span></div>'))}


def _br_status(text, on):
    tone = "var(--pl-accent)" if on else "var(--pl-l2)"
    return {"t": "html", "html": _both(lambda i: (
        f'<div style="display:flex;align-items:flex-start;gap:8px;font-size:12px;line-height:1.4{"" if on else ";color:var(--pl-l2)"}">'
        f'<span style="color:{tone};flex:none;margin-top:1px">{_svg(IC["clock"], 1.7, 15)}</span><span>{_pick(text, i)}</span></div>'))}


def _popup(label, value, i):
    """A pop-up menu (a SwiftUI Picker) with its label."""
    arrows = _svg('<path d="m8 9.5 4-3.5 4 3.5M8 14.5l4 3.5 4-3.5"/>', 2, 11)
    return (f'<div class="pl-seg-row"><span class="pl-lab">{_pick(label, i)}</span>'
            f'<span class="pl-btn" style="gap:6px">{_pick(value, i)}{arrows}</span></div>')


BR_PICKERS = {"t": "html", "html": _both(lambda i: '<div style="display:flex;flex-direction:column;gap:6px">' + _popup(T("Every", "每隔"), T("45 min", "45 分钟"), i)
                                         + _popup(T("Break", "休息"), T("5 min", "5 分钟"), i) + "</div>")}
BR_COVER = {"t": "html", "html": T(
    '<label style="display:flex;align-items:center;gap:7px;font-size:12px"><span class="pl-chk"></span>Cover the screen during breaks</label>',
    '<label style="display:flex;align-items:center;gap:7px;font-size:12px"><span class="pl-chk"></span>休息时盖住屏幕</label>')}


def _banner(i, kind):
    if kind == "due":
        return (f'<div class="pl-bn"><span class="pl-bn-ic">{_svg(IC["walk"], 1.8)}</span><div class="pl-bn-t">'
                f'<strong>{("Time for a Break", "该休息一下了")[i]}</strong>'
                f'<span>{("You’ve been at it for 47 min. Get up, move around and look into the distance", "已经连续用了 47 分钟，起来活动活动、看看远处")[i]}</span></div></div>'
                '<div class="pl-bn-btns">' + "".join(f'<span class="pl-btn{" is-tint" if k == 2 else ""}">{x}</span>' for k, x in enumerate(
                    (("Skip", "In 5 Minutes", "Take a 5 min Break"), ("跳过", "5 分钟后提醒", "休息 5 分钟"))[i])) + "</div>")
    if kind == "break":
        ring = ('<svg class="pl-ring" viewBox="0 0 28 28" aria-hidden="true"><circle class="tr" cx="14" cy="14" r="11.5"/>'
                '<circle class="v" cx="14" cy="14" r="11.5" pathLength="1"/></svg>')
        left = ("On a break, {} left", "休息中，还剩 {}")[i].format('<span class="pl-cd">5:00</span>')
        return (f'<div class="pl-bn is-row">{ring}<div class="pl-bn-t"><strong>{left}</strong>'
                f'<span>{("Look at something 20 feet away and blink", "看看 6 米外的地方，眨眨眼")[i]}</span></div>'
                f'<span class="pl-btn">{("End Break", "结束休息")[i]}</span></div>')
    return (f'<div class="pl-bn is-row"><span class="pl-bn-ic is-ok">{_svg(IC["checkFill"])}</span>'
            f'<div class="pl-bn-t"><strong>{("Break’s over. Back to it!", "休息好了，接着忙吧")[i]}</strong></div></div>')


def banner(kind):
    return _both(lambda i: _banner(i, kind))


# ---------------------------------------------------------------- Window Layout
LAYOUTS = [
    ('<rect x="3" y="5" width="18" height="14" rx="2.5"/><path d="M5.5 5H12v14H5.5A2.5 2.5 0 0 1 3 16.5v-9A2.5 2.5 0 0 1 5.5 5Z" fill="currentColor"/>',
     T("Left Half", "左半屏")),
    ('<rect x="3" y="5" width="18" height="14" rx="2.5"/><path d="M12 5h6.5A2.5 2.5 0 0 1 21 7.5v9a2.5 2.5 0 0 1-2.5 2.5H12Z" fill="currentColor"/>',
     T("Right Half", "右半屏")),
    ('<rect x="3" y="5" width="18" height="14" rx="2.5"/><path d="M3 12V7.5A2.5 2.5 0 0 1 5.5 5h13A2.5 2.5 0 0 1 21 7.5V12Z" fill="currentColor"/>',
     T("Top Half", "上半屏")),
    ('<rect x="3" y="5" width="18" height="14" rx="2.5"/><path d="M3 12h18v4.5a2.5 2.5 0 0 1-2.5 2.5h-13A2.5 2.5 0 0 1 3 16.5Z" fill="currentColor"/>',
     T("Bottom Half", "下半屏")),
    ('<rect x="3" y="5" width="18" height="14" rx="2.5"/><rect x="5" y="7" width="4.5" height="10" rx="1" fill="currentColor" stroke="none"/>',
     T("Left Third", "左三分之一")),
    ('<rect x="3" y="5" width="18" height="14" rx="2.5"/><path d="M9 5v14M15 5v14"/>', T("Center Third", "中间三分之一")),
    ('<rect x="3" y="5" width="18" height="14" rx="2.5"/><rect x="14.5" y="7" width="4.5" height="10" rx="1" fill="currentColor" stroke="none"/>',
     T("Right Third", "右三分之一")),
    ('<path d="M4.5 4.5l6 6M4.5 4.5h5M4.5 4.5v5M19.5 19.5l-6-6M19.5 19.5h-5M19.5 19.5v-5"/>', T("Maximize", "最大化")),
    ('<rect x="3" y="5" width="18" height="14" rx="2.5"/><rect x="7.5" y="9" width="9" height="6" rx="1" fill="currentColor" stroke="none"/>',
     T("Center", "居中")),
    ('<rect x="2.5" y="5" width="13" height="9.5" rx="1.5"/><path d="M6.5 18h5M9 14.5V18M18.5 8h1.5a1.5 1.5 0 0 1 1.5 1.5v6A1.5 1.5 0 0 1 20 17h-3.5"/>',
     T("Next Display", "下一个显示器")),
]
LAYOUT_CARD = {"w": 380, "sub": T("Arrow keys for halves, Return to maximize", "方向键放到半屏，回车最大化"),
               # Only one display on the pretend Mac, so Next Display is dimmed, as in Pop.
               "body": [{"t": "html", "html": _tiles(LAYOUTS, off=(9,))}]}

# ---------------------------------------------------------------- Quit Apps
QA_SAFARI = app(T("Safari", "Safari 浏览器"), "#4fb3ff", "#1f6fd8", "compass")
QA_XCODE = app("Xcode", "#6fc3ff", "#2a62c9", "hammer")
QA_MUSIC = app(T("Music", "音乐"), "#ff6f91", "#e8344e", "note")
QA_MAIL = app(T("Mail", "邮件"), "#58b7ff", "#2d7ff9", "mail")
QA_NOTES = app(T("Notes", "备忘录"), "#ffd84d", "#f5b400", "lines")


def _qa(a, right, warn=False, current=False):
    it = {"file": a, "title": a["name"], "right": right, "btn": T("Quit", "退出")}
    if warn:
        it["tone"] = "warn"
    if current:
        it["sub"] = T("Current", "在用")
    return it


QA_ROWS = {
    "safari": _qa(QA_SAFARI, "7.4% · 2.19 GB"),
    "xcode": _qa(QA_XCODE, "186% · 1.65 GB", warn=True),
    "music": _qa(QA_MUSIC, "14% · 393 MB"),
    "mail": _qa(QA_MAIL, "0.3% · 273 MB"),
    "notes": _qa(QA_NOTES, "0% · 151 MB", current=True),
}


def _qa_list(*keys):
    return {"t": "list", "items": [QA_ROWS[k] for k in keys]}


QA_NOTE = {"t": "note", "text": T("Apps ask before closing unsaved documents. If an app hasn’t quit a few seconds after you click Quit, you can force quit it",
                                  "没存的文稿，App 会先问你要不要存；点了「退出」几秒还没退出的，可以强制退出")}
QA_SEG = {"t": "seg", "items": [T("By Memory", "按内存"), T("By CPU", "按 CPU")], "on": 1}
QA_SUB = T("5 apps running, using 4.63 GB of memory", "正在运行 5 个 App，一共占用 4.63 GB 内存")

# ---------------------------------------------------------------- Uninstall App / App Info
SKETCHPAD = app("Sketchpad", "#ffb36b", "#ff6f3c", "pencil")
WAVEFORM = app("Waveform", "#b07aff", "#6a4bd8", "wave")
APPS = [app("Atlas", "#5fd0a6", "#1f9d74", "globe"), app("Ledger", "#7cc4ff", "#3a7bd5", "chart"), app("Lumen", "#ffd76b", "#f2a33a", "sun")]
UN_HEAD = {"t": "list", "items": [{"file": SKETCHPAD, "title": "Sketchpad", "sub": T("Version 3.2.1 · com.example.sketchpad", "版本 3.2.1 · com.example.sketchpad"),
                                    "right": "2.05 GB"}]}

# ---------------------------------------------------------------- Focus sounds
SOUNDS = [
    ('<path d="M4 10v4M7.5 7v10M11 4v16M14.5 8v8M18 6v12M21 10.5v3"/>', T("White Noise", "白噪音")),
    ('<path d="M2.5 12h2l2-6 3 12 3-14 3 14 2.5-8 1.5 2h2"/>', T("Pink Noise", "粉红噪音")),
    ('<path d="M2.5 12h5l2-5 3 10 2.5-7 1.5 2h5"/>', T("Brown Noise", "棕色噪音")),
    ('<path d="M7 14.5a4 4 0 0 1-.4-8A5.5 5.5 0 0 1 17.2 7.4a3.6 3.6 0 0 1 .3 7.1Z"/><path d="M8 17.5l-1 2.5M12 17.5l-1 2.5M16 17.5l-1 2.5"/>', T("Rain", "雨声")),
    ('<path d="M3 8c1.5-1.3 3-1.3 4.5 0s3 1.3 4.5 0 3-1.3 4.5 0 3 1.3 4.5 0M3 12.5c1.5-1.3 3-1.3 4.5 0s3 1.3 4.5 0 3-1.3 4.5 0 3 1.3 4.5 0'
     'M3 17c1.5-1.3 3-1.3 4.5 0s3 1.3 4.5 0 3-1.3 4.5 0 3 1.3 4.5 0"/>', T("Waves", "海浪")),
]

# ---------------------------------------------------------------- the cards that come back (Timer, Keep Awake, System Actions)
TIMER_CARD = {"w": 350, "body": [{"t": "text", "text": T(
    "Choose a duration to start a countdown. When time’s up, Pop plays a sound and sends a notification. You can also select text such as “25 min” or “1:30” and use the timer. The Pomodoro timer alternates 25 minutes of focus with a 5-minute break (15 minutes after every fourth) until you end it.",
    "选一个时长开始倒计时；到点时响一声、发一条通知。也可以选中「25 分钟」「1:30」这样的文字再用它。番茄钟是专注 25 分钟、休息 5 分钟轮流来（每四个番茄休息 15 分钟），一直到你结束。")}],
    "btns": [T("1 min", "1 分钟"), T("3 min", "3 分钟"), T("5 min", "5 分钟"), T("10 min", "10 分钟"), T("15 min", "15 分钟"),
             T("25 min", "25 分钟"), T("45 min", "45 分钟"), T("1 hr", "1 小时"), T("Pomodoro", "番茄钟")]}

AWAKE_BTNS = [T("30 min", "30 分钟"), T("1 hr", "1 小时"), T("2 hr", "2 小时"), T("Indefinitely", "一直保持")]


def _system_card(hidden_shown):
    return {"w": 380, "body": [{"t": "note", "text": T("Hiding desktop icons or showing hidden files relaunches Finder; close files that are open on a disk before ejecting it",
                                                       "隐藏桌面图标、显示隐藏文件时会重新打开访达；推出前请先关掉磁盘上打开的文件")}],
            "btns": [T("Lock Screen", "锁屏"), T("Turn Off Display", "熄屏"), T("Sleep", "睡眠"), T("Screen Saver", "屏幕保护程序"),
                     T("Switch to Dark Mode", "换成深色模式"), T("Mute", "静音"), T("Hide Desktop Icons", "隐藏桌面图标"),
                     T("Hide Hidden Files", "不显示隐藏文件") if hidden_shown else T("Show Hidden Files", "显示隐藏文件"),
                     T("Eject 2 Disks", "推出 2 个磁盘")]}


SITE_FILES = [{"name": "assets", "kind": "folder"}, {"name": "index.html"}, {"name": "about.html"}, {"name": "styles.css"},
              {"name": "app.js"}, {"name": "README.md"}]
DOT_FILES = [{"name": ".git", "kind": "folder"}, {"name": ".gitignore"}, {"name": ".env"}]

# ---------------------------------------------------------------- Disk Speed
DISK_NOTE = T("Writes, then reads, bypassing the system cache. The test file is deleted afterwards",
              "先写后读，绕过系统缓存；测完删掉测试文件")

# ---------------------------------------------------------------- Resolution


def _pending():
    """Pop's “Keep this resolution?” bar; the seconds (.pl-cd) count down with the text effect."""
    def make(i):
        text = _pick(T("Keep this resolution? Switching back in <span class=\"pl-cd\">15</span> s",
                       "保留这个分辨率吗？<span class=\"pl-cd\">15</span> 秒后换回原来的"), i)
        return ('<div style="display:flex;align-items:center;gap:8px;padding:8px;border-radius:8px;background:rgba(255,149,0,.14)">'
                f'<span style="display:inline-flex;color:var(--pl-orange)">{_svg(IC["timer"], 2, 15)}</span>'
                f'<span style="flex:1;min-width:0;font-size:12px;line-height:1.35;font-variant-numeric:tabular-nums">{text}</span>'
                f'<span class="pl-btn">{_pick(T("Switch Back", "换回去"), i)}</span><span class="pl-btn is-tint">{_pick(T("Keep", "保留"), i)}</span></div>')
    return {"t": "html", "html": _both(make), "hide": True}


# ---------------------------------------------------------------- System Info
SI_WIDEST = T("Model Identifier", "型号标识")


def _serial():
    """The serial number row with Pop's Show link (the rows block can't hold a button). A hidden row with the
    widest label of the rows above keeps the label column as wide as theirs."""
    def make(i):
        label = _pick(T("Serial Number", "序列号"), i)
        link = _pick(T("Show", "显示"), i)
        return ('<div class="pl-rows" style="row-gap:0;gap:0">'
                f'<div class="pl-row" style="height:0;overflow:hidden;visibility:hidden" aria-hidden="true"><span class="pl-row-l">{_pick(SI_WIDEST, i)}</span><span></span></div>'
                f'<div class="pl-row pl-serial"><span class="pl-row-l">{label}</span><span class="pl-row-v">'
                '<span class="pl-mono pl-serial-v">••••••••••••</span> '
                f'<span class="pl-btn pl-serial-b" style="height:auto;padding:0 2px;background:none;color:var(--pl-accent);font-size:11px">{link}</span></span></div></div>')
    return {"t": "html", "html": _both(make)}


# ---------------------------------------------------------------- Battery Info
def _battery_head():
    def make(i):
        bolt = '<svg viewBox="0 0 24 24" width="12" height="12" aria-hidden="true"><path d="M13.5 2 5 13.6h6.2L10 22l9-12.2h-6.4Z" style="fill:var(--pl-green)"/></svg>'
        return ('<div style="display:flex;align-items:center;gap:14px">'
                '<span style="position:relative;width:58px;height:58px;flex:none;display:grid;place-items:center">'
                '<svg viewBox="0 0 58 58" width="58" height="58" style="position:absolute;inset:0;transform:rotate(-90deg)" aria-hidden="true">'
                '<circle cx="29" cy="29" r="26" style="fill:none;stroke:var(--pl-fill-2);stroke-width:6"/>'
                '<circle cx="29" cy="29" r="26" pathLength="100" style="fill:none;stroke:var(--pl-green);stroke-width:6;stroke-linecap:round;stroke-dasharray:76 100"/></svg>'
                '<b style="font-size:15px;font-variant-numeric:tabular-nums">76%</b></span>'
                '<span style="display:flex;flex-direction:column;gap:3px;min-width:0">'
                f'<span style="display:flex;align-items:center;gap:4px">{bolt}<b style="font-size:13px">{_pick(T("Charging", "正在充电"), i)}</b>'
                '<span style="color:var(--pl-l2);font-variant-numeric:tabular-nums">43.1 W</span></span>'
                f'<span class="pl-note">{_pick(T("0:38 until full", "充满还要 0:38"), i)}</span></span></div>')
    return {"t": "html", "html": _both(make)}


DATA = {
    "windowLayout": {
        "chips": [T("Halves and thirds", "半屏和三分之一"), T("Arrow keys, Return", "方向键、回车"), T("Next display", "下一个显示器")],
        "points": [
            T("Put the window you’re using on the <b>left or right half</b>, the top or bottom half or a third of the screen, maximize it or center it.",
              "把正在用的窗口放到<b>左半屏、右半屏</b>、上半屏、下半屏或者三分之一，最大化，或者居中。"),
            T("Center keeps the window’s size, shrinking it only if it doesn’t fit.", "居中时窗口大小不变，放不下才缩小。"),
            T("With more than one display, Next Display moves the window to the other screen in the same relative spot.",
              "接着几台显示器时，「下一个显示器」把窗口挪过去，在屏幕上的相对位置不变。"),
            T("On the card, the arrow keys pick a half, Return maximizes, C centers and 1–3 pick a third. It works even better with a shortcut.",
              "卡片上用方向键放到半屏，回车最大化，C 居中，1–3 放到三分之一；配上快捷键更顺手。"),
        ],
        "scene": {
            "src": {"kind": "desk", "app": T("Notes", "备忘录"), "title": T("Trip plan", "旅行计划"), "cap": T("Work in any window", "在任意窗口里"),
                    "sub": T("It moves the window you’re using.", "挪的是正在用的窗口。"),
                    "lines": [T("**Day 1** · Fly to Lisbon, check in by the river", "**第一天** · 飞里斯本，住河边"),
                              T("**Day 2** · Tram 28, Alfama, dinner at eight", "**第二天** · 坐 28 路电车，逛阿尔法玛"),
                              T("**Day 3** · Train to Sintra, back before dark", "**第三天** · 坐火车去辛特拉，天黑前回来")]},
            "card": LAYOUT_CARD,
            "steps": [
                {"cap": T("Click Left Half", "点「左半屏」"), "acts": [["wait", 400], ["click", "opt:0.0", [["close"], ["win", "left"]]]], "hold": 1100},
                {"cap": T("Or press Return to maximize", "或者按回车最大化"), "sub": T("Arrow keys pick a half.", "方向键放到半屏。"),
                 "acts": [["card", LAYOUT_CARD], ["key", "↩"], ["close"], ["win", "max"]], "hold": 1100},
                {"cap": T("Press 1–3 for a third", "按 1–3 放到三分之一"),
                 "acts": [["card", LAYOUT_CARD], ["hover", "opt:0.4"], ["key", "1"], ["close"], ["win", "third"]]},
            ],
        },
    },
    "menuShortcuts": {
        "chips": [T("Grouped by menu", "按菜单分组"), "⌘ ⌥ ⇧ ⌃", T("Click to run", "点一下就执行")],
        "points": [
            T("Lists every <b>keyboard shortcut</b> in the menus of the app you’re using, grouped by menu.",
              "列出正在用的 App 菜单里的<b>所有快捷键</b>，按菜单分好组。"),
            T("Search by title, by the menu it’s in or by the shortcut itself. Press ⇥ to list every menu item, with or without a shortcut.",
              "可以搜标题、所在的菜单或者快捷键（支持拼音首字母）；按 ⇥ 换成全部菜单项，没有快捷键的也列出来。"),
            T("Click an item or press Return and the app runs it, so commands hidden deep in submenus are a search away.",
              "点一项或者按回车，那个 App 就直接执行它；藏在深处的菜单项也一搜就到。"),
            T("Items that are dimmed in the menu are dimmed here too. Pop needs Accessibility permission to read the menus.",
              "菜单里是灰色的项，列表里也是灰的。要读菜单，得在「辅助功能」里允许 Pop。"),
        ],
        "scene": {
            "src": {"kind": "files", "app": T("Projects", "项目"), "sum": T("Nothing selected", "未选中内容"), "cap": T("Work in any app", "在任意 App 里"),
                    "sub": T("It reads the menus of the app in front, here Finder.", "读的是前台 App 的菜单，这里是访达。"),
                    "files": [{"name": T("Invoices", "发票"), "kind": "folder"}, {"name": "brief.pdf"}, {"name": "logo.png", "kind": "photo", "art": "logo"},
                              {"name": T("Budget.xlsx", "预算.xlsx")}, {"name": T("Notes.txt", "笔记.txt")}]},
            "card": {"w": 350, "sub": T("Finder", "访达"),
                     "body": [{"t": "field", "ph": T("Search menus and shortcuts", "搜索菜单和快捷键")},
                              {"t": "seg", "items": [T("Shortcuts (72)", "有快捷键（72）"), T("All (118)", "全部（118）")], "on": 0},
                              {"t": "panes", "panes": [
                                  [{"t": "note", "text": T("**File**", "**文件**")},
                                   {"t": "list", "dense": True, "items": [{"title": T("New Finder Window", "新建访达窗口"), "right": "`⌘N`", "on": True},
                                                                          {"title": T("New Folder", "新建文件夹"), "right": "`⇧⌘N`"},
                                                                          {"title": T("Get Info", "显示简介"), "right": "`⌘I`"}]},
                                   {"t": "note", "text": T("**Go**", "**前往**")},
                                   {"t": "list", "dense": True, "items": [{"title": T("Downloads", "下载"), "right": "`⌥⌘L`"},
                                                                          {"title": T("Applications", "应用程序"), "right": "`⇧⌘A`"},
                                                                          {"title": T("Connect to Server…", "连接服务器…"), "right": "`⌘K`"}]}],
                                  [{"t": "note", "text": T("**File**", "**文件**")},
                                   {"t": "list", "dense": True, "items": [{"title": T("New Folder", "新建文件夹"), "right": "`⇧⌘N`", "on": True},
                                                                          {"title": T("New Folder with Selection", "用所选项目新建文件夹"), "right": "`⌃⌘N`"},
                                                                          {"title": T("New Smart Folder", "新建智能文件夹"), "right": "`⌥⌘N`"}]},
                                   {"t": "note", "text": T("**Go**", "**前往**")},
                                   {"t": "list", "dense": True, "items": [{"title": T("Enclosing Folder", "上层文件夹"), "right": "`⌘↑`"},
                                                                          {"title": T("Go to Folder…", "前往文件夹…"), "right": "`⇧⌘G`"}]}],
                              ]},
                              {"t": "note", "text": T("↑↓ Choose · ⏎ Run · ⇥ Switch", "↑↓ 选择 · ⏎ 执行 · ⇥ 切换")}]},
            "steps": [
                {"cap": T("Every shortcut, by menu", "所有快捷键，按菜单分组"), "acts": [["move", "row:2.4"], ["wait", 500]]},
                {"cap": T("Search for a command", "搜要找的菜单项"), "sub": T("By title, menu or shortcut.", "标题、菜单、快捷键都能搜，拼音首字母也行。"),
                 "acts": [["type", 0, T("folder", "wjj")], ["swap", 2, 1], ["wait", 300]]},
                {"cap": T("Click it, and the app runs it", "点一下，App 就执行"), "sub": T("Finder makes a new folder.", "访达新建了一个文件夹。"),
                 "acts": [["click", "row:2.0", [["close"], ["file", {"name": T("untitled folder", "未命名文件夹"), "kind": "folder"}]]]]},
            ],
        },
    },
    "keepAwake": {
        "chips": [T("30 min · 1 hr · 2 hr", "30 分钟 · 1 小时 · 2 小时"), T("Or indefinitely", "或者一直保持"), T("Stop any time", "随时停止")],
        "points": [
            T("For <b>30 minutes, 1 hour, 2 hours</b> or until you stop it, the display won’t dim and the Mac won’t go to sleep on its own.",
              "选 <b>30 分钟、1 小时、2 小时</b>或者一直，这段时间里屏幕不会变暗，电脑也不会自己睡眠。"),
            T("Handy for reading, presenting or waiting for a download. Closing the lid still puts the Mac to sleep.",
              "看文档、演示、等下载时用；合上盖子照常睡眠。"),
            T("Use it again to see when it ends, choose another duration (it counts from now) or stop it. Pop’s menu bar menu shows the end time and can stop it too.",
              "再用一次能看到到几点结束，可以重新选一个时长（从现在开始算），或者停止；Pop 菜单栏的菜单里也能看到到几点、随时停止。"),
            T("Quitting Pop ends it.", "退出 Pop 时自动失效。"),
        ],
        "scene": {
            "src": {"kind": "desk", "app": T("Preview", "预览"), "title": T("Annual report.pdf", "年度报告.pdf"),
                    "lines": [T("**Annual report 2026**", "**2026 年度报告**"), T("Letter from the founders", "创始人的信"),
                              T("This year we doubled the team and opened two offices…", "这一年团队翻了一倍，开了两个新办公室……")]},
            "card": {"w": 340, "body": [{"t": "text", "text": T("Choose a duration. During it, the display won’t dim and the Mac won’t sleep on its own; closing the lid still puts it to sleep.",
                                                               "选一个时长，这段时间里屏幕不会变暗，电脑也不会自己睡眠；合上盖子照常睡眠。")}],
                     "btns": AWAKE_BTNS},
            "steps": [
                {"cap": T("Choose how long", "选一个时长"), "acts": [["hover", "btn:1"], ["wait", 300]]},
                {"cap": T("The display stays on for an hour", "一小时内屏幕都不会暗"),
                 "acts": [["click", "btn:1", [["close"], ["toast", T("Keeping awake for 1 hr", "保持唤醒 1 小时")]]]], "hold": 900},
                {"cap": T("Use it again to see when it ends", "再用一次，看到几点结束"), "sub": T("Stop it here or from Pop’s menu bar menu.", "在这里或者 Pop 菜单栏的菜单里停止。"),
                 "acts": [["card", {"w": 340, "body": [{"t": "text", "text": T("Keeping awake until 17:14 (1 hr left)", "保持唤醒到 17:14（还剩 1 小时）")},
                                                       {"t": "note", "text": T("Choosing another duration starts counting from now", "重新选一个时长会从现在开始算")}],
                                    "btns": AWAKE_BTNS + [T("Stop", "停止")]}],
                          ["click", "btn:4", [["close"], ["toast", T("Stopped keeping awake", "已停止保持唤醒")]]]]},
            ],
        },
    },
    "systemActions": {
        "chips": [T("Lock · Sleep · Screen saver", "锁屏 · 睡眠 · 屏保"), T("Dark Mode in a click", "一键换深色模式"), T("Eject all disks", "推出所有磁盘")],
        "points": [
            T("The switches you reach for often, on one card: <b>Lock Screen</b>, Turn Off Display, Sleep, Screen Saver, Switch to Dark or Light Mode, and Mute.",
              "常用的开关都在一张卡片上：<b>锁屏</b>、熄屏、睡眠、屏幕保护程序、换成深色或浅色模式、静音。"),
            T("Hide the desktop icons before a recording or a demo, or have Finder show the hidden files that start with a dot. Finder relaunches to apply it.",
              "录屏、演示前可以隐藏桌面图标，也能让访达显示以点开头的隐藏文件；会重新打开一下访达。"),
            T("With external drives, disk images or network disks mounted, <b>Eject</b> takes them all out at once and names any that are still in use.",
              "插着移动硬盘、U 盘，或者开着磁盘映像、连着网络磁盘时，「<b>推出磁盘</b>」一次全部推出，推不出来的会说是哪个正在用。"),
            T("Button labels follow the current state: Mute becomes Unmute, Show Hidden Files becomes Hide Hidden Files. The first time you switch Dark Mode, macOS asks whether Pop may control System Events.",
              "按钮上的说法跟着现在的状态变：「静音」变成「取消静音」，「显示隐藏文件」变成「不显示隐藏文件」。第一次换深浅色时，系统会问能不能让 Pop 控制「System Events」，允许就行。"),
        ],
        "scene": {
            "src": {"kind": "files", "app": "my-site", "files": SITE_FILES, "sum": T("Nothing selected", "未选中内容"),
                    "cap": T("No need to select anything", "什么都不用选")},
            "card": _system_card(False),
            "steps": [
                {"cap": T("Common switches on one card", "常用开关都在一张卡片上"), "acts": [["hover", "btn:4"], ["wait", 400]]},
                {"cap": T("Show the hidden files", "显示隐藏文件"), "sub": T("Finder relaunches and lists the dot files.", "访达重新打开，列出以点开头的文件。"),
                 "acts": [["click", "btn:7", [["close"], ["grid", DOT_FILES + SITE_FILES],
                                             ["toast", T("Finder now shows hidden files", "访达里显示隐藏文件了")]]]], "hold": 1100},
                {"cap": T("The button now hides them", "按钮变成了「不显示隐藏文件」"),
                 "acts": [["card", _system_card(True)],
                          ["click", "btn:7", [["close"], ["grid", SITE_FILES], ["toast", T("Finder no longer shows hidden files", "访达里不再显示隐藏文件")]]]]},
            ],
        },
    },
    "quitApps": {
        "chips": [T("Memory and CPU", "内存和 CPU"), T("Force Quit", "强制退出"), T("Quit Other Apps", "退出其他 App")],
        "points": [
            T("Lists the running apps and <b>how much memory and CPU</b> each one uses, counting the processes it started; the numbers update while the card is open.",
              "列出正在运行的 App 和<b>各占多少内存、CPU</b>（连同它开出来的子进程），卡片开着时一直在更新。"),
            T("Sort by memory or by CPU to find the app that’s draining the battery or heating up; anything using more than a full core is orange.",
              "可以按内存或者按 CPU 排，找出正在耗电、发热的 App；用满一个核以上的标橙。"),
            T("Click Quit and the app leaves the list once it has quit. If it’s still running a few seconds later, <b>Force Quit</b> appears.",
              "点「退出」，退出后从列表里拿掉；几秒还没退出的（没有响应，或者在问要不要存），换成「<b>强制退出</b>」。"),
            T("Quit Other Apps asks first, then quits everything except the app you’re using: a clean slate before a meeting or a demo. Apps still ask about unsaved documents.",
              "「退出其他 App」先确认一下，再把除了正在用的那个以外的 App 都退出，开会、演示前清清场；没存的文稿 App 会先问你。"),
        ],
        "scene": {
            "src": {"kind": "desk", "app": T("Notes", "备忘录"), "title": T("Demo checklist", "演示前检查"),
                    "lines": [T("1. Close the other apps", "1. 关掉别的 App"), T("2. Turn on Do Not Disturb", "2. 打开勿扰模式"), T("3. Open the slides", "3. 打开幻灯片")]},
            "card": {"w": 390, "sub": QA_SUB,
                     "body": [dict(QA_SEG, on=0), _qa_list("safari", "xcode", "music", "mail", "notes"), QA_NOTE, _buttons([T("Quit Other Apps", "退出其他 App")])]},
            "steps": [
                {"cap": T("Memory and CPU for each app", "每个 App 占多少内存、CPU"), "acts": [["wait", 500]]},
                {"cap": T("Sort by CPU to find the busy one", "按 CPU 排，找出最忙的"),
                 "acts": [["click", "opt:0.1", ["set", 1, _qa_list("xcode", "music", "safari", "mail", "notes")]], ["wait", 300]]},
                {"cap": T("Quit it with a click", "点「退出」就退出"),
                 "acts": [["click", "btn:1.0", [["addClass", "row:1.0", "is-gone"], ["wait", 450], ["set", 1, _qa_list("music", "safari", "mail", "notes")]]]]},
                {"cap": T("Or quit all the others", "或者退出其他所有 App"), "sub": T("It asks first, and keeps the app you’re using.", "先确认一下，正在用的那个留着。"),
                 "acts": [["click", "btn:3.0", ["set", 3, _buttons([T("Cancel", "取消"), T("Quit 3", "退出 3 个")], tint=1,
                                                                   text=T("Quit the 3 apps other than “Notes”?", "除了「备忘录」，退出其他 3 个 App？"))]],
                          ["wait", 400],
                          ["click", "btn:3.1", [["addClass", "row:1.0", "is-gone"], ["addClass", "row:1.1", "is-gone"], ["addClass", "row:1.2", "is-gone"],
                                                ["wait", 450], ["set", 1, _qa_list("notes")], ["set", 3, _buttons([T("Quit Other Apps", "退出其他 App")], dim=True)]]]]},
            ],
        },
    },
    "uninstallApp": {
        "chips": [T("Leftover files too", "连同留下的文件"), T("Size of each", "各占多大"), T("Reset to a fresh install", "恢复成刚装好")],
        "points": [
            T("Select an app in Finder and Pop finds the <b>settings, caches and containers</b> it left in your Library, plus saved window state, website data, logs and launch agents, with the size of each.",
              "在访达里选中一个 App，Pop 找出它在「资源库」里留下的<b>设置、缓存、容器</b>、窗口状态、网页数据、日志、开机启动的服务，每一项写着占多大。"),
            T("Items that match the app’s bundle ID are checked. Ones whose name only starts the same, or that may be shared with another app from the same developer, are left unchecked.",
              "和 App（以及它带的扩展）的 bundle ID 正好对上的默认勾上；只是名字开头对上的、可能和同一个开发者的别的 App 共用的，默认不勾。"),
            T("Everything checked goes to the <b>Trash</b>, so you can put it back. If the app is running, Pop asks it to quit first.",
              "勾上的一起移到<b>废纸篓</b>，需要时可以放回原处；App 正在运行时先请它退出。"),
            T("Uncheck the app itself to clear only its leftovers: the app starts fresh, as if just installed. Apps that come with macOS can’t be uninstalled.",
              "不勾 App 本身、只清掉留下的文件，就是把 App 恢复成刚装好的样子。系统自带的 App 不能卸载。"),
        ],
        "scene": {
            "src": {"kind": "files", "app": T("Applications", "应用程序"), "cap": T("Select an app in Finder", "在访达里选中一个 App"),
                    "files": [APPS[0], dict(SKETCHPAD, sel=True), WAVEFORM, APPS[1], APPS[2]]},
            "card": {"w": 380, "sub": "Sketchpad", "btns": [T("Move to Trash", "移到废纸篓")], "tint": 0,
                     "body": [UN_HEAD,
                              {"t": "list", "dense": True, "items": [
                                  {"chk": True, "icon": icon("app"), "title": T("The App", "App 本身"), "sub": "/Applications/Sketchpad.app", "right": "412 MB"},
                                  {"chk": True, "icon": icon("folder"), "title": T("Application Support", "应用程序支持"), "sub": "~/Library/Application Support/Sketchpad", "right": "1.28 GB"},
                                  {"chk": True, "icon": icon("box"), "title": T("Caches", "缓存"), "sub": "~/Library/Caches/com.example.sketchpad", "right": "356 MB"},
                                  {"chk": True, "icon": icon("gear"), "title": T("Preferences", "偏好设置"), "sub": "~/Library/Preferences/com.example.sketchpad.plist", "right": "12 KB"},
                                  {"chk": False, "icon": icon("people"), "title": T("Group Container", "共享容器"), "sub": "~/Library/Group Containers/ABCDE12345.com.example.sketchpad", "right": "48 MB"},
                              ]},
                              {"t": "note", "text": T("Moves the 8 checked items (2.05 GB) to the Trash. You can put them back from the Trash if needed",
                                                      "把勾上的 8 项（2.05 GB）移到废纸篓；需要时可以从废纸篓放回原处")}]},
            "steps": [
                {"cap": T("It finds what the app left behind", "找出 App 留下的文件"), "sub": T("Ones that may be shared stay unchecked.", "可能和别的 App 共用的默认不勾。"),
                 "acts": [["move", "row:1.4"], ["wait", 500]]},
                {"cap": T("Move it all to the Trash", "一起移到废纸篓"),
                 "acts": [["click", "btn:0", ["card", {"w": 380, "sub": "Sketchpad", "btns": [T("Open Trash", "打开废纸篓"), T("Done", "完成")], "tint": 1,
                                                        "body": [UN_HEAD, {"t": "text", "text": T("Moved 8 items to the Trash, freeing 2.05 GB", "已把 8 项移到废纸篓，腾出 2.05 GB")}]}]]]},
                {"cap": T("The app is gone", "App 卸载好了"),
                 "acts": [["click", "btn:1", [["close"], ["grid", [APPS[0], WAVEFORM, APPS[1], APPS[2]]]]]]},
            ],
        },
    },
    "appInfo": {
        "chips": [T("Apple silicon or Intel", "Apple 芯片还是 Intel"), T("Signed and notarized?", "签名、公证"), T("Sandbox, permissions", "沙盒、权限")],
        "points": [
            T("Select an app to see which <b>chips</b> it’s built for (Apple silicon, Intel or both) and the oldest macOS it runs on.",
              "选中一个 App，看它是给哪种<b>芯片</b>做的（Apple 芯片、Intel 还是通用）、最低要哪个版本的 macOS。"),
            T("Who signed it, whether it’s <b>notarized</b> and sandboxed, and whether the hardened runtime is on. Intel-only, unsigned and unnotarized apps are marked orange.",
              "谁签的名、有没有<b>公证</b>、在不在沙盒里、开没开加固运行时；只给 Intel 做的、没签名、没公证的标成橙色。"),
            T("What it’s built with (Electron, Flutter, Qt, Java, Mac Catalyst…, and whether it updates itself with Sparkle), where it came from and how big it is.",
              "用什么做的（Electron、Flutter、Qt、Java、Mac Catalyst……还有带没带 Sparkle 自动更新）、从哪来的（App Store，或者用哪个 App 下载的）、有多大。"),
            T("The permissions it may ask for, such as the camera or microphone, and the links that open it. <b>Copy it all</b> as text.",
              "它可能会要的权限（摄像头、麦克风、通讯录……）和能打开它的链接；可以<b>一键复制</b>成文字。"),
        ],
        "scene": {
            "src": {"kind": "files", "app": T("Applications", "应用程序"), "cap": T("Select an app in Finder", "在访达里选中一个 App"),
                    "files": [APPS[0], SKETCHPAD, dict(WAVEFORM, sel=True), APPS[1], APPS[2]]},
            "card": {"w": 380, "sub": "Waveform", "btns": [T("Show in Finder", "在访达中显示"), T("Copy Info", "复制信息")], "tint": 1,
                     "body": [{"t": "list", "items": [{"file": WAVEFORM, "title": T("**Waveform 2.4.0 (240)**", "**Waveform 2.4.0（240）**"), "sub": "com.example.waveform"}]},
                              {"t": "rows", "mono": False, "copy": False, "rows": [
                                  [T("Architecture", "芯片"), T("Universal (Apple silicon and Intel)", "通用（Apple 芯片和 Intel）")],
                                  [T("Minimum macOS", "最低系统"), "macOS 12.0"],
                                  [T("Signature", "签名"), T("Developer ID: Example Audio (QWERT12345)", "Developer ID：Example Audio（QWERT12345）")],
                                  [T("Notarization", "公证"), T("Notarized", "已公证")],
                                  [T("Sandbox", "沙盒"), T("Not sandboxed", "不在沙盒里")],
                                  [T("Built With", "用什么做的"), T("Electron · Sparkle updates", "Electron · Sparkle 自动更新")],
                                  [T("Source", "来源"), T("Downloaded with Safari", "用「Safari」下载的")],
                                  [T("Size", "大小"), "286 MB"]]},
                              {"t": "note", "text": T("Permissions It May Ask For", "会要的权限")},
                              {"t": "chips", "on": [], "items": [T("Microphone", "麦克风"), T("Bluetooth", "蓝牙"), T("Downloads Folder", "下载文件夹")]}]},
            "steps": [
                {"cap": T("Chip, signature, sandbox…", "芯片、签名、沙盒……"), "acts": [["move", "b:1", 0.7, 0.3], ["wait", 400], ["move", "opt:3.0"], ["wait", 400]]},
                {"cap": T("Copy it all as text", "一键复制成文字"), "sub": T("For a bug report, or to compare apps.", "报问题、比较几个 App 时用。"),
                 "acts": [["click", "btn:1", ["toast", T("Copied", "已复制")]]]},
            ],
        },
    },
    "batteryInfo": {
        "chips": [T("Health and cycles", "健康度和循环次数"), T("Watts in or out", "充电、耗电功率"), "AirPods · Magic Mouse"],
        "points": [
            T("See the charge, whether it’s charging, <b>how many watts</b> are going in or out, and how long until it’s full or empty.",
              "看电量、是不是在充电，<b>充电或者耗电的功率</b>，还要多久充满或者用完。"),
            T("<b>Maximum capacity</b> (what a full charge holds now compared with when it was new), the cycle count against its design life, condition, temperature, voltage and the charger’s wattage.",
              "<b>最大容量</b>（现在充满能有出厂时的百分之几）、循环次数和设计寿命、状况、温度、电压，还有充电器多少瓦。"),
            T("Capacity under 80%, Service Recommended and a hot battery are marked orange.", "最大容量低于 80%、建议维修、太热时标成橙色。"),
            T("Below, the battery levels of connected Bluetooth keyboards, mice, trackpads and headphones, with each AirPod and the case listed separately; under 20% is orange. On a desktop Mac you see just these.",
              "下面列出连着的蓝牙键盘、鼠标、触控板和耳机的电量，AirPods 左耳、右耳、充电盒分开写，20% 以下标橙；台式 Mac 上只列这些设备。"),
            T("It refreshes every 3 seconds while open. Copy it all, or jump to Battery Settings.", "卡片开着时每 3 秒刷新，可以复制，也能直接打开「电池」设置。"),
        ],
        "scene": {
            "src": {"kind": "desk", "app": T("Notes", "备忘录"), "title": T("Travel checklist", "出差清单"),
                    "lines": [T("Charger and USB-C cable", "充电器和 USB-C 线"), T("AirPods case", "AirPods 充电盒"), T("Passport", "护照")]},
            "card": {"w": 360, "btns": [T("Battery Settings", "电池设置"), T("Copy Info", "复制信息"), T("Done", "完成")], "tint": 2,
                     "body": [_battery_head(),
                              {"t": "stats", "items": [["91%", "", T("Maximum Capacity", "最大容量")],
                                                       ["286", T("designed for\u00a01000", "设计寿命 1000\u00a0次"), T("Cycle Count", "循环次数")],
                                                       ["31.2 ℃", "", T("Temperature", "温度")]]},
                              {"t": "rows", "mono": False, "copy": False, "rows": [[T("Power Adapter", "电源适配器"), "96 W · 96W USB-C Power Adapter"]]},
                              {"t": "sep"},
                              {"t": "note", "text": T("Bluetooth Devices", "蓝牙设备")},
                              {"t": "list", "dense": True, "items": [
                                  {"icon": icon("keyboard"), "title": T("Magic Keyboard", "妙控键盘"), "right": "85%"},
                                  {"icon": icon("mouse"), "title": T("Magic Mouse", "妙控鼠标"), "right": "18%", "tone": "warn"},
                                  {"icon": icon("airpods"), "title": "AirPods Pro", "right": T("Left 100% · Right 99% · Case 50%", "左耳 100% · 右耳 99% · 充电盒 50%")}]}]},
            "steps": [
                {"cap": T("Charge, health and cycles", "电量、健康度、循环次数"), "acts": [["wait", 900]]},
                {"cap": T("Bluetooth devices too", "蓝牙设备的电量也在"), "sub": T("Under 20% is marked orange.", "20% 以下标橙。"),
                 "acts": [["move", "row:5.1", 0.85, 0.5], ["wait", 600], ["move", "row:5.2", 0.75, 0.5]]},
                {"cap": T("Copy it all", "一键复制"), "acts": [["click", "btn:1", ["toast", T("Copied", "已复制")]]]},
            ],
        },
    },
    "systemInfo": {
        "chips": [T("Chip and cores", "芯片和核心数"), T("Displays and Hz", "显示器和刷新率"), T("Copy for bug reports", "复制去报问题")],
        "points": [
            T("This Mac’s model and model identifier, <b>chip</b>, CPU cores (performance and efficiency) and GPU cores, and memory.",
              "这台 Mac 的型号和型号标识、<b>芯片</b>、CPU 核心（性能核、能效核）和 GPU 核心、内存。"),
            T("The macOS version with its name and build number, how long since it started up, and the free space on the startup disk (orange when less than a tenth is left).",
              "macOS 版本（带名字和构建号）、开机多久、启动磁盘还剩多少（不到一成标橙）。"),
            T("For each display: how big it looks, its actual pixels and its refresh rate.", "每台显示器看起来多大、实际多少像素、刷新率。"),
            T("<b>Copy it all</b> in one go for a bug report or when asking for help. The serial number stays hidden until you click Show, and is copied only then.",
              "可以<b>一键复制</b>，报问题、问人时用；序列号先藏着，点「显示」才露出来，复制时也只在露出来以后带上。"),
        ],
        "scene": {
            "src": {"kind": "desk", "app": "Safari", "title": T("Report a bug", "反馈问题"),
                    "lines": [T("**Describe the problem**", "**说说遇到的问题**"), T("The app freezes when I export a large file.", "导出大文件的时候卡住不动。"),
                              T("**Your Mac**: model, macOS version…", "**你的 Mac**：型号、macOS 版本……")]},
            "card": {"w": 390, "btns": [T("Copy Info", "复制信息"), T("Done", "完成")], "tint": 1,
                     "body": [{"t": "list", "items": [{"icon": icon("laptop"), "title": "**MacBook Pro (14-inch, 2023)**",
                                                       "sub": T("macOS Sequoia 15.6.1 (24G90)", "macOS Sequoia 15.6.1（24G90）")}]},
                              {"t": "rows", "mono": False, "copy": False, "rows": [
                                  [T("Model Identifier", "型号标识"), "Mac14,9"],
                                  [T("Chip", "芯片型号"), "Apple M2 Pro"],
                                  [T("Cores", "核心"), T("10-core CPU (6 performance + 4 efficiency) · 16-core GPU", "10 核 CPU（6 性能核 + 4 能效核）· 16 核 GPU")],
                                  [T("Memory", "内存"), "16 GB"],
                                  [T("Uptime", "已开机"), T("3 days 4 hr", "3 天 4 小时")],
                                  [T("Startup Disk", "启动磁盘"), T("Macintosh HD · 233.88\u00a0GB available of 494.38\u00a0GB", "Macintosh HD · 可用 233.88\u00a0GB，共 494.38\u00a0GB")],
                                  [T("Display", "显示器"), T("Studio Display · 2560\u00a0×\u00a01440 (5120\u00a0×\u00a02880\u00a0pixels) · 60\u00a0Hz", "Studio Display · 2560\u00a0×\u00a01440（像素 5120\u00a0×\u00a02880）· 60\u00a0Hz")]]},
                              _serial()]},
            "steps": [
                {"cap": T("Model, chip, memory, displays", "型号、芯片、内存、显示器"), "acts": [["wait", 900]]},
                {"cap": T("Click Show for the serial number", "点「显示」看序列号"), "sub": T("It stays hidden until you do.", "不点就一直藏着。"),
                 "acts": [["click", "btn:2.0", [["addClass", ".pl-serial", "is-hl"], ["text", ".pl-serial-v", "C02XK1ABCD12"], ["text", ".pl-serial-b", T("Hide", "隐藏")]]],
                          ["wait", 300]]},
                {"cap": T("Copy it all at once", "一键全部复制"), "acts": [["click", "btn:0", ["toast", T("Copied", "已复制")]]]},
            ],
        },
    },
    "soundDevices": {
        "chips": [T("Output and input", "输出和输入"), T("AirPods, displays, AirPlay", "AirPods、显示器、AirPlay"), T("Volume and mute", "音量和静音")],
        "points": [
            T("Switch <b>where sound plays</b> and which microphone is used in one click: speakers, headphones, AirPods, displays (HDMI, DisplayPort) or AirPlay.",
              "一下子换<b>声音从哪出</b>、用哪个麦克风：扬声器、耳机、AirPods、显示器（HDMI、DisplayPort）、AirPlay，现在用的打勾，点一下就换。"),
            T("Adjust the output and input volume, or mute; dragging the volume up while muted unmutes.", "能调输出和输入的音量，一键静音；静音时把音量往上拖就取消静音。"),
            T("The list keeps up while the card is open: plug in headphones or connect AirPods and they appear right away.",
              "卡片开着时插上耳机、连上 AirPods，列表马上跟着变。"),
            T("Devices that macOS sets up for a single app aren’t listed.", "系统给某个 App 临时建的设备不列。"),
        ],
        "scene": {
            "src": {"kind": "desk", "app": T("Music", "音乐"), "title": T("Morning playlist", "早上的歌单"),
                    "lines": [T("1. Sunrise Avenue", "1. 晨光大道"), T("2. Paper Boats", "2. 纸船"), T("3. Slow Train Home", "3. 慢车回家")]},
            "card": {"w": 340, "btns": [T("Sound Settings", "声音设置"), T("Done", "完成")], "tint": 1,
                     "body": [{"t": "note", "text": T("Output", "输出")},
                              {"t": "list", "dense": True, "items": [
                                  {"icon": icon("speaker"), "title": T("MacBook Pro Speakers", "MacBook Pro 扬声器"), "on": True},
                                  {"icon": icon("airpods"), "title": "AirPods Pro", "sub": T("Bluetooth", "蓝牙")},
                                  {"icon": icon("display"), "title": "LG HDR 4K", "sub": "DisplayPort"}]},
                              {"t": "slider", "label": "", "value": 0.4},
                              {"t": "sep"},
                              {"t": "note", "text": T("Input", "输入")},
                              {"t": "list", "dense": True, "items": [
                                  {"icon": icon("mic"), "title": T("MacBook Pro Microphone", "MacBook Pro 麦克风"), "on": True},
                                  {"icon": icon("airpods"), "title": "AirPods Pro", "sub": T("Bluetooth", "蓝牙")}]}]},
            "steps": [
                {"cap": T("Every speaker and microphone", "所有扬声器和麦克风"), "sub": T("The one in use is highlighted.", "现在用的那个亮着。"), "acts": [["wait", 700]]},
                {"cap": T("Click AirPods to switch", "点一下 AirPods 就换过去"), "acts": [["click", "row:1.1"], ["wait", 300]]},
                {"cap": T("Set the volume", "调音量"),
                 "acts": [["move", ".pl-b-slider .pl-sl", 0.4, 0.5], ["prop", 2, "--v", 0.72], ["move", ".pl-b-slider .pl-sl", 0.72, 0.5, 500], ["wait", 200]]},
            ],
        },
    },
    "bluetooth": {
        "chips": [T("Connect · Disconnect", "连接 · 断开"), "AirPods", T("Battery level", "电量")],
        "points": [
            T("Lists your <b>paired</b> headphones, AirPods, keyboards, mice, trackpads and game controllers, connected ones first.",
              "列出<b>配对过的</b>耳机、AirPods、键盘、鼠标、触控板、手柄，连着的排在前面。"),
            T("<b>Connect or disconnect</b> one with a click, without opening System Settings. A spinner shows while it connects; if it can’t, the card says to check that the device is on, nearby and not connected to another device.",
              "点一下就<b>连接或者断开</b>，不用打开系统设置；连接要等一会儿时转着圈，连不上会说一句（确认它开着、在附近、没连着别的设备）。"),
            T("Connected Magic Keyboard, Mouse and Trackpad show their <b>battery level</b>.", "连着的妙控键盘、鼠标、触控板写着<b>电量</b>。"),
            T("macOS asks once for Bluetooth access the first time; if it was denied, the card tells you where to turn it on. New devices are paired in Bluetooth Settings first.",
              "第一次用时 macOS 会问一次蓝牙权限，没给的话卡片上告诉你去哪里打开；新设备先在「蓝牙设置」里配对。"),
        ],
        "scene": {
            "src": {"kind": "desk", "app": T("FaceTime", "FaceTime 通话"), "title": T("Weekly sync", "周会"),
                    "lines": [T("**10:00** · starts in 2 minutes", "**10:00** · 两分钟后开始"), T("Headphones on, then join", "戴上耳机再进会")]},
            "card": {"w": 360, "btns": [T("Bluetooth Settings", "蓝牙设置"), T("Done", "完成")], "tint": 1,
                     "body": [_bt_list({"airpods", "keyboard"})]},
            "steps": [
                {"cap": T("Your paired devices", "配对过的设备"), "sub": T("Connected ones first, with the keyboard’s battery level.", "连着的排在前面，键盘写着电量。"),
                 "acts": [["move", "[data-n='wh']", 0.4, 0.5], ["wait", 500]]},
                {"cap": T("Click Connect", "点「连接」"), "sub": T("A moment later, the headphones are connected.", "等一会儿就连上了。"),
                 "acts": [["click", "[data-n='wh'] .pl-btn", ["set", 0, _bt_list({"airpods", "keyboard"}, {"wh"})]], ["wait", 1100],
                          ["set", 0, _bt_list({"airpods", "keyboard", "wh"})]], "hold": 1400},
                {"cap": T("Click Disconnect to let go of one", "点「断开」放开一个"),
                 "acts": [["click", "[data-n='airpods'] .pl-btn", ["set", 0, _bt_list({"keyboard", "wh"})]]], "hold": 1500},
            ],
        },
    },
    "resolution": {
        "chips": [T("Looks like 2560 × 1440", "看起来像 2560 × 1440"), T("Refresh rate", "刷新率"), T("Keep within 15 s", "15 秒内点「保留」")],
        "points": [
            T("Change each display’s resolution by <b>how big it looks</b>. The system’s default size says Default, and sizes without HiDPI, where text looks blurry, say Low resolution.",
              "按<b>「看起来像多大」</b>换每台显示器的分辨率：系统默认的写着「默认」，没有 HiDPI、文字会发虚的写着「低分辨率」。"),
            T("Switch the refresh rate when a size has more than one, such as 120 Hz and 60 Hz.", "这个大小有几种刷新率时可以换，比如 120 Hz 和 60 Hz。"),
            T("With several displays, pick which one to change (the one under the pointer comes first), or make one the main display so the menu bar and Dock move to it.",
              "接着几台显示器时可以选换哪一台（先选指针所在的那台），也能把一台设成主显示器，菜单栏和程序坞跟着过去。"),
            T("After a change on an external display, click <b>Keep</b> within 15 seconds or it switches back, so a mode the display can’t show never leaves you with a black screen.",
              "外接显示器换了以后 15 秒内要点「<b>保留</b>」，不然换回原来的；换成显示器不支持的模式、屏幕黑了时什么都不用做。"),
        ],
        "scene": {
            "src": {"kind": "desk", "app": T("Freeform", "无边记"), "title": T("Mood board", "灵感板"),
                    "lines": [T("**Spring campaign**", "**春季活动**"), T("Need more room on this display?", "这块屏幕不够用？")]},
            "card": {"w": 340, "at": "center", "btns": [T("Display Settings", "显示器设置"), T("Done", "完成")], "tint": 1,
                     "body": [{"t": "seg", "items": [T("Built-in Display", "内建显示器"), "Studio Display"], "on": 1},
                              {"t": "note", "text": T("Looks like", "看起来像")},
                              {"t": "list", "dense": True, "items": [
                                  {"title": "1280 × 720", "right": T("Low resolution", "低分辨率"), "tone": "warn"},
                                  {"title": "1600 × 900"},
                                  {"title": "2048 × 1152", "on": True},
                                  {"title": "2560 × 1440", "right": T("Default", "默认")},
                                  {"title": "2880 × 1620"}]},
                              _pending()]},
            "steps": [
                {"cap": T("Choose how big it looks", "选看起来像多大"), "sub": T("The display under the pointer comes first.", "先选的是指针所在的那台。"),
                 "acts": [["move", "row:2.3", 0.4, 0.5], ["wait", 400]]},
                {"cap": T("Pick 2560 × 1440", "点「2560 × 1440」"),
                 "acts": [["click", "row:2.3"], ["show", 3], ["wait", 700], ["text", ".pl-cd", "14"], ["wait", 1000], ["text", ".pl-cd", "13"]], "hold": 1000},
                {"cap": T("Click Keep within 15 seconds", "15 秒内点「保留」"), "sub": T("Otherwise it switches back by itself.", "不点就自己换回原来的。"),
                 "acts": [["text", ".pl-cd", "12"], ["click", "btn:3.1", ["hide", 3]]]},
            ],
        },
    },
    "diskSpeed": {
        "chips": [T("Write · Read", "写入 · 读取"), "256 MB · 1 GB · 4 GB", T("Bypasses the cache", "绕过系统缓存")],
        "points": [
            T("Measure how fast the startup disk, an external drive, a USB stick or a portable SSD <b>writes and reads</b> sequentially.",
              "测启动磁盘、移动硬盘、U 盘、移动固态硬盘<b>连续写入和读取</b>有多快。"),
            T("Select a file or folder on a drive to test that drive, or nothing to test the startup disk; the card also lets you switch, and shows the format, internal or external, and free space.",
              "选中磁盘里的文件或文件夹就测那块盘，什么都不选时测启动磁盘，卡片上也能换；写着磁盘的格式、内置还是外接、还剩多少空间。"),
            T("Pick a 256 MB, 1 GB or 4 GB test file. It writes, then reads, <b>bypassing the system cache</b>; the numbers move while it runs and end on the average.",
              "测试文件可以选 256 MB、1 GB、4 GB（会记住），先写后读，<b>绕过系统缓存</b>，测的时候两个大数字跟着跳，测完写着平均速度。"),
            T("The test file is deleted afterwards, even if you stop or something fails, and the test won’t start without enough space. Copy the result in one click.",
              "测完、停下或者出错都会删掉测试文件，空间不够时不让测；结果可以复制。"),
        ],
        "scene": {
            "src": {"kind": "files", "app": "T7 Shield", "cap": T("Select something on the drive", "选中这块盘上的东西"),
                    "sub": T("With nothing selected it tests the startup disk.", "什么都不选时测启动磁盘。"),
                    "files": [{"name": T("Footage", "素材"), "kind": "folder", "sel": True}, {"name": T("Photos 2026", "照片 2026"), "kind": "folder"},
                              {"name": "Interview.mov", "kind": "video", "art": "city"}, {"name": "Backup.zip", "kind": "zip"}, {"name": T("Pitch.key", "提案.key")}]},
            "card": {"w": 360, "sub": "T7 Shield",
                     "body": [{"t": "seg", "label": T("Test File", "测试文件"), "items": ["256 MB", "1 GB", "4 GB"], "on": 1},
                              {"t": "note", "text": T("ExFAT · External · 1.2 TB available of 2 TB", "ExFAT · 外接 · 可用 1.2 TB，共 2 TB")},
                              {"t": "stats", "items": [["—", "MB/s", T("Write", "写入")], ["—", "MB/s", T("Read", "读取")]]},
                              {"t": "bar", "hide": True, "from": 0, "to": 1, "dur": 2600, "count": "%s%", "c0": 0, "c1": 100},
                              _buttons([T("Start Test", "开始测速")], tint=0, note=DISK_NOTE)]},
            "steps": [
                {"cap": T("It tests the drive you selected", "测的是选中的那块盘"), "acts": [["move", "opt:0.1"], ["wait", 500]]},
                {"cap": T("It writes, then reads", "先写，再读"), "sub": T("The numbers move as it runs.", "测的时候数字跟着跳。"),
                 "acts": [["click", "btn:4.0", [["set", 4, _buttons([T("Stop", "停止")], note=DISK_NOTE)], ["show", 3, 0],
                                                ["set", 2, {"t": "stats", "dur": 2600, "items": [["921", "MB/s", T("Write", "写入")], ["1,013", "MB/s", T("Read", "读取")]]}]]],
                          ["wait", 2500], ["hide", 3], ["set", 4, _buttons([T("Copy Result", "复制结果"), T("Test Again", "再测一次")], tint=1, note=DISK_NOTE)]]},
                {"cap": T("Copy the result", "复制结果"), "acts": [["click", "btn:4.0", ["toast", T("Copied", "已复制")]]]},
            ],
        },
    },
    "cleanKeyboard": {
        "chips": [T("Locked for a minute", "锁住一分钟"), T("Brightness keys too", "亮度、音量键也锁"), T("End it with the mouse", "用鼠标随时结束")],
        "points": [
            T("<b>Locks the keyboard for a minute</b> so you can wipe it without typing anything into the app you were using.",
              "<b>锁住键盘一分钟</b>，擦键盘时不会往正在用的 App 里误打字。"),
            T("Brightness, volume and the other function keys are blocked too.", "亮度、音量这些功能键也不起作用。"),
            T("The screen shows how long is left; click <b>End Cleaning</b> with the mouse to stop any time.",
              "屏幕上显示倒计时，用鼠标点「<b>结束清洁</b>」随时恢复。"),
            T("When it ends, the app you were using comes back to the front.", "结束后回到之前在用的 App。"),
        ],
        "scene": {
            "src": {"kind": "desk", "app": T("Notes", "备忘录"), "title": T("Notes", "备忘录"),
                    "lines": [T("Saturday chores", "周六要做的事"), T("Water the plants · wipe the keyboard · laundry", "浇花 · 擦键盘 · 洗衣服")]},
            "fx": {"name": "lock", "title": T("The keyboard is locked. Go ahead and wipe it", "键盘已经锁住，可以放心擦了"),
                   "sub": T("Keys, brightness and volume don’t respond; unlocks by itself in 1:00", "按键、亮度和音量键都不起作用；1:00 后自动恢复"),
                   "btn": T("End Cleaning", "结束清洁")},
            "steps": [
                {"cap": T("The keyboard locks for a minute", "键盘锁住一分钟"), "acts": [["move", 0.3, 0.75], ["wait", 500]]},
                {"cap": T("Wipe away: keys do nothing", "放心擦，按什么都没反应"), "sub": T("Brightness and volume keys too.", "亮度、音量键也一样。"),
                 "acts": [["key", "A"], ["key", "⌘Q"], ["key", "F12"]], "hold": 600},
                {"cap": T("Click End Cleaning when you’re done", "擦完点「结束清洁」"), "sub": T("Or it unlocks by itself after a minute.", "不点的话一分钟后自动恢复。"),
                 "acts": [["click", ".pl-lock .pl-btn"], ["fx", "end"]]},
            ],
        },
    },
    "timer": {
        "chips": [T("1 min to 1 hr", "1 分钟到 1 小时"), T("Select “25 min”", "选中「25 分钟」"), T("Pomodoro", "番茄钟")],
        "points": [
            T("Start a <b>countdown</b> of 1, 3, 5, 10, 15, 25 or 45 minutes or an hour. When time’s up, Pop plays a sound, sends a notification and shows a message on screen.",
              "<b>倒计时</b> 1、3、5、10、15、25、45、60 分钟；到点时响一声、发一条通知、屏幕上提示。"),
            T("Or select text such as “25 min”, “1h30m” or “1:30” and it starts right away.", "也可以选中「25 分钟」「1h30m」「1:30」这样的文字，直接开始。"),
            T("The <b>Pomodoro</b> timer alternates 25 minutes of focus with 5-minute breaks (15 minutes after every fourth) until you end it.",
              "<b>番茄钟</b>：专注 25 分钟、休息 5 分钟轮流来，每四个番茄休息 15 分钟，一直到你点「结束番茄钟」。"),
            T("Pop’s menu bar menu shows how long is left and can cancel it. Quitting Pop stops the timer.", "Pop 菜单栏的菜单里能看到还剩多久，也可以取消；退出 Pop 后不再计时。"),
        ],
        "scene": {
            "src": {"kind": "desk", "app": "Pages", "title": T("Weekly report", "周报"), "sub": T("Or select text like “25 min” to start right away.", "也可以选中「25 分钟」这样的文字，直接开始。"),
                    "lines": [T("**Done this week**", "**本周完成**"), T("Shipped the new sign-up flow", "上线了新的注册流程"), T("**Next week**", "**下周计划**")]},
            "card": TIMER_CARD,
            "steps": [
                {"cap": T("Choose a duration", "选一个时长"), "acts": [["hover", "btn:5"], ["wait", 300]]},
                {"cap": T("Click 25 min to start", "点「25 分钟」开始"),
                 "acts": [["click", "btn:5", [["close"], ["toast", T("Timer started: 25 min", "开始计时 25 分钟")]]]], "hold": 700},
                {"cap": T("Time’s up: a sound and a notification", "到点了：响一声，发通知"),
                 "acts": [["move", 0.3, 0.7], ["notify", T("Time’s Up", "时间到"), T("Your 25 min timer is done", "25 分钟的计时到了")],
                          ["toast", T("Time’s up: Your 25 min timer is done", "时间到：25 分钟的计时到了")]], "hold": 900},
                {"cap": T("Or start a Pomodoro", "或者开始番茄钟"), "sub": T("25 minutes of focus, then a 5-minute break.", "专注 25 分钟，休息 5 分钟。"),
                 "acts": [["card", TIMER_CARD], ["click", "btn:8", [["close"], ["toast", T("Pomodoro started: focus for 25 minutes", "番茄钟开始：先专注 25 分钟")]]]]},
            ],
        },
    },
    "breakReminder": {
        "chips": [T("Every 45 min", "每 45 分钟"), T("Stepping away counts", "离开就算休息"), T("Quiet in meetings", "开会时不打扰")],
        "points": [
            T("Once it’s on, a reminder appears <b>at the top of the screen</b> after 45 minutes at the computer (20 minutes to an hour and a half, your choice): take a break, get reminded again in 5 minutes, or skip.",
              "打开以后，连续用电脑 45 分钟（20 分钟到 1 个半小时可选）就在<b>屏幕上方</b>提醒你休息一下，可以马上休息、5 分钟后再提醒或者跳过。"),
            T("Breaks last 20 seconds to 10 minutes, counting down in the banner, or <b>covering the screen</b> if you choose; Esc ends one early, and a sound plays when it’s over.",
              "休息 20 秒到 10 分钟，倒计时显示在上方的小条里，也可以选<b>「休息时盖住屏幕」</b>，按 Esc 随时提前结束；休息完了响一声。"),
            T("<b>Stepping away</b> for as long as a break (at least 3 minutes) counts as one, time asleep with the lid closed included, and the clock restarts when you’re back.",
              "<b>离开电脑</b>够久（一次休息的时长，至少 3 分钟）就算休息过了，合上盖子睡着的时间也算在里面，回来重新计时。"),
            T("No reminders while an app is playing video or in a video call, and that time doesn’t count as a break. Pop picks up the count the next time it starts.",
              "有 App 在放视频、开视频会议时不提醒，那段时间也不算休息。Pop 下次启动时接着计时。"),
        ],
        "scene": {
            "src": {"kind": "desk", "app": T("Numbers", "Numbers 表格"), "title": T("Q4 budget", "第四季度预算"),
                    "lines": [T("**Marketing** · 128,000", "**市场** · 128,000"), T("**Travel** · 46,500", "**差旅** · 46,500")]},
            "card": {"w": 360, "btns": [T("Take a Break Now", "现在休息"), T("Done", "完成")], "tint": 1,
                     "body": [_br_switch(False),
                              _br_status(T("Off. When it’s on, you’ll get a reminder to take a 5 min break after 45 min at the computer.",
                                           "没开。打开以后，连续用电脑 45 分钟会提醒你休息 5 分钟。"), False),
                              BR_PICKERS, BR_COVER,
                              {"t": "note", "text": T("Stepping away for 3 minutes or more (or the break length, if longer) counts as a break, including time the Mac spends asleep, and the clock restarts when you’re back. No reminders while an app keeps the display awake, such as during a video or a video call, and that time doesn’t count as a break.",
                                                      "离开电脑 3 分钟以上（休息时长更长时按休息时长）就算休息过了，合上盖子睡着的时间也算，回来重新计时；有 App 在放视频、开视频会议（不让屏幕变暗）时不提醒，这段时间也不算休息。")}]},
            "steps": [
                {"cap": T("Turn it on", "打开它"), "sub": T("Every 45 minutes, a 5-minute break; both can be changed.", "每 45 分钟休息 5 分钟，都可以改。"),
                 "acts": [["click", ".pl-sw2", [["addClass", ".pl-sw2", "is-on"],
                                                ["set", 1, _br_status(T("You’ve been at it for under a minute. Break reminder in 45 min", "已经连续用了不到一分钟，45 分钟后提醒休息"), True)]]]],
                 "hold": 1400},
                {"cap": T("45 minutes later, a reminder at the top", "45 分钟后，屏幕上方提醒你"), "sub": T("Stepping away for a while counts as a break.", "离开一会儿就算休息过了。"),
                 "acts": [["click", "btn:1", [["close"], ["fx", "start", {"name": "banner", "html": banner("due")}]]]], "hold": 1600},
                {"cap": T("Take a break", "休息一下"), "sub": T("The banner counts down; Esc ends it early.", "上方的小条倒计时，Esc 提前结束。"),
                 "acts": [["click", ".pl-banner .pl-btn.is-tint", ["fx", "html", banner("break")]], ["fx", "count", [300, 300, 293, 2600]]], "hold": 600},
                {"cap": T("A sound when it’s over", "休息完了响一声"), "acts": [["fx", "html", banner("done")]], "hold": 1600},
            ],
        },
    },
    "focusSounds": {
        "chips": [T("Rain · Waves · Noise", "雨声 · 海浪 · 噪音"), T("Sleep timer", "定时停止"), T("Made on your Mac", "本机实时生成")],
        "points": [
            T("Play <b>white, pink or brown noise, rain or waves</b> to cover the chatter and typing around you while you focus or nap.",
              "放<b>白噪音、粉红噪音、棕色噪音、雨声或者海浪</b>，盖住周围的说话声和键盘声，专心做事、午睡时用。"),
            T("The sound is generated on your Mac, with nothing to download. Click a sound to play it and again to pause; switching, volume, pausing and stopping all fade instead of cutting off.",
              "声音在本机实时生成，不用下载音频；点一种就放，再点一下暂停，换声音、调音量、暂停和停止都是慢慢变过去的，不会「啪」的一声。"),
            T("A <b>sleep timer</b> stops it after 15 minutes, 30 minutes, 1 hour or 2 hours, fading out over the last few seconds.",
              "可以<b>定时</b> 15 分钟、30 分钟、1 小时或者 2 小时后停下，最后几秒慢慢变小声。"),
            T("It keeps playing after you close the card; the headphones icon in the menu bar pauses, resumes or stops it. Pop remembers the sound, volume and timer.",
              "关掉卡片也接着放，菜单栏的耳机图标可以暂停、接着放、停止；放哪种、多大声、定时多久都会记住。"),
        ],
        "scene": {
            "src": {"kind": "desk", "app": "Pages", "title": T("Chapter 3 draft", "第三章草稿"),
                    "lines": [T("**Chapter 3** · The harbor", "**第三章** · 港口"), T("The ferry was late again, and nobody on the pier seemed to mind.", "渡轮又晚点了，码头上的人好像谁都不着急。")]},
            "card": {"w": 370,
                     "body": [{"t": "html", "html": _tiles(SOUNDS, on=0)},
                              {"t": "note", "text": T("Every frequency equally loud; the best at covering voices and typing", "各个频率一样响，最能盖住说话声和键盘声")},
                              {"t": "slider", "label": T("Volume", "音量"), "value": 0.45},
                              {"t": "note", "text": T("Keeps playing after you close the card; pause or stop it from the headphones icon in the menu bar",
                                                      "关掉卡片也接着放，菜单栏的耳机图标可以暂停、停止")},
                              {"t": "seg", "label": T("Sleep Timer", "定时停止"), "on": 0,
                               "items": [T("Off", "不限时"), T("15 min", "15 分钟"), T("30 min", "30 分钟"), T("1 hr", "1 小时"), T("2 hr", "2 小时")]},
                              _buttons([T("Play", "播放")], tint=0)]},
            "steps": [
                {"cap": T("Pick a sound", "选一种声音"), "acts": [["move", "opt:0.3"], ["wait", 400]]},
                {"cap": T("Click Rain and it plays", "点「雨声」就放"),
                 "acts": [["click", "opt:0.3", [["set", 0, {"t": "html", "html": _tiles(SOUNDS, on=3, playing=3)}],
                                                ["set", 1, {"t": "note", "text": T("Steady rain tapping on the window", "细密的雨点打在窗上")}],
                                                ["set", 5, _buttons([T("Stop", "停止"), T("Pause", "暂停")], tint=1)], ["mb", "headphones"]]]]},
                {"cap": T("Set a sleep timer", "定时停止"), "sub": T("It fades out at the end.", "快到点时慢慢变小声。"), "acts": [["click", "opt:4.2"], ["wait", 300]]},
                {"cap": T("Close it; it keeps playing", "关掉卡片，接着放"), "sub": T("The headphones icon in the menu bar pauses or stops it.", "菜单栏的耳机图标可以暂停、停止。"),
                 "acts": [["click", "x"], ["move", ".pl-mb-extra.is-headphones", 0.5, 0.9]]},
            ],
        },
    },
}
