"""Plugin pages: convert plugins. See __init__.py and the README ("Plugin pages")."""
import datetime
from html import escape

from . import T

COPIED = T("Copied", "已复制")


def copy_icon(b, i):
    """The copy icon of row i in a rows block b (for a click)."""
    return f"[data-b='{b}'] .pl-row[data-i='{i}'] .pl-ib"


# Result rows written out in HTML, for what the rows block can't show: values over several lines (Convert Table),
# long labels (Date Difference).
COPY_SVG = ('<svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" '
            'stroke-linejoin="round"><rect x="8.4" y="8.4" width="11.2" height="12.4" rx="2"/>'
            '<path d="M15.6 8.4V5.6a2 2 0 0 0-2-2H6.4a2 2 0 0 0-2 2v8.8a2 2 0 0 0 2 2h2"/></svg>')
CLAMP3 = "white-space:pre-wrap;display:-webkit-box;-webkit-box-orient:vertical;-webkit-line-clamp:3;overflow:hidden"


def long_rows(rows, label_w=None, clamp=True):
    """Rows as Pop lays them out: values over several lines (clamped to three), and a label column as wide as the
    longest label (the rows block has a fixed one)."""
    lw = f' style="flex-basis:{label_w}px"' if label_w else ""
    vs = f' style="{CLAMP3}"' if clamp else ""
    return '<div class="pl-rows">' + "".join(
        f'<div class="pl-row" data-i="{i}"><span class="pl-row-l"{lw}>{escape(label)}</span>'
        f'<span class="pl-row-v pl-mono"{vs}>{escape(value)}</span><span class="pl-ib">{COPY_SVG}</span></div>'
        for i, (label, value) in enumerate(rows)) + "</div>"


def table_rows(rows):
    """Markdown, CSV and JSON of a table copied from a spreadsheet (TableConverter.render)."""
    head = rows[0]
    md = ["| " + " | ".join(head) + " |", "|" + "|".join(" --- " for _ in head) + "|"] + ["| " + " | ".join(r) + " |" for r in rows[1:]]
    csv = [",".join(r) for r in rows]
    js = ["["] + [",\n".join("  {" + ", ".join(f'"{k}": "{v}"' for k, v in zip(head, r)) + "}" for r in rows[1:])] + ["]"]
    return long_rows([("Markdown", "\n".join(md)), ("CSV", "\n".join(csv)), ("JSON", "\n".join(js))])


TABLE_EN = [["Name", "City", "Plan"], ["Ada", "London", "Pro"], ["Mei", "Tokyo", "Free"], ["Sam", "Austin", "Team"]]
TABLE_ZH = [["姓名", "城市", "套餐"], ["小明", "上海", "专业版"], ["小红", "北京", "免费版"], ["阿杰", "深圳", "团队版"]]

# Markdown Preview: the selected Markdown as Pop lays it out (theme colors only).
PREVIEW = ('<div style="display:flex;flex-direction:column;gap:7px;padding:2px 0">'
           '<div style="font-size:18px;font-weight:700;line-height:1.25">{h}</div>'
           '<ul style="margin:0;padding-left:20px;display:flex;flex-direction:column;gap:3px">{items}</ul>'
           '<div style="border-left:3px solid var(--pl-sep);padding:1px 0 1px 10px;color:var(--pl-l2)">{quote}</div></div>')


def preview(h, items, quote):
    return PREVIEW.format(h=h, items="".join(f"<li>{x}</li>" for x in items), quote=quote)


# Time Zones: the cities at three moments (the selected time, dragged back, and when everyone is at work).
# The strips run on local time (New York on the English page, Beijing on the Chinese one); offsets are hours from it.
def zones(en, zh):
    return T([list(r) for r in en], [list(r) for r in zh])


WT_HOURS = [
    zones([("Los Angeles", "15:00", -3, "UTC−7 · Selected"), ("New York", "18:00", 0, "UTC−4 · Local"), ("London", "23:00", 5, "UTC+1 · BST"), ("São Paulo", "19:00", 1, "UTC−3")],
          [("北京", "17:00", 0, "UTC+8 · 本地"), ("伦敦", "10:00", -7, "UTC+1 · 选中的"), ("东京", "18:00", 1, "UTC+9"), ("新加坡", "17:00", 0, "UTC+8")]),
    zones([("Los Angeles", "12:00", -3, "UTC−7 · Selected"), ("New York", "15:00", 0, "UTC−4 · Local"), ("London", "20:00", 5, "UTC+1 · BST"), ("São Paulo", "16:00", 1, "UTC−3")],
          [("北京", "15:00", 0, "UTC+8 · 本地"), ("伦敦", "08:00", -7, "UTC+1 · 选中的"), ("东京", "16:00", 1, "UTC+9"), ("新加坡", "15:00", 0, "UTC+8")]),
    zones([("Los Angeles", "09:00", -3, "UTC−7 · Selected"), ("New York", "12:00", 0, "UTC−4 · Local"), ("London", "17:00", 5, "UTC+1 · BST"), ("São Paulo", "13:00", 1, "UTC−3")],
          [("北京", "16:00", 0, "UTC+8 · 本地"), ("伦敦", "09:00", -7, "UTC+1 · 选中的"), ("东京", "17:00", 1, "UTC+9"), ("新加坡", "16:00", 0, "UTC+8")]),
]
WT_AT = [T(0.75, 0.7083), T(0.625, 0.625), T(0.5, 0.6667)]
# The slider moves the moment up to a day either way: 0.5 is the selected time.
WT_SLIDER = [(0.5, T("Drag to try another time", "拖动换个时间")), (T(0.4375, 0.4583), T("−3 hr", "−2 小时")), (T(0.375, 0.4792), T("−6 hr", "−1 小时"))]
PEOPLE = ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round">'
          '<circle cx="9" cy="8" r="3.2"/><path d="M3.4 19.2c.6-3.2 2.8-5 5.6-5s5 1.8 5.6 5"/><circle cx="16.6" cy="8.8" r="2.6"/><path d="M16.4 14.2c2.4.2 4 1.8 4.4 4.8"/></svg>')


def wt_hours(k):
    return {"t": "hours", "rows": WT_HOURS[k], "at": WT_AT[k]}


def wt_slider(k):
    return {"t": "slider", "label": "", "value": WT_SLIDER[k][0], "right": WT_SLIDER[k][1]}


# ---------------------------------------------------------------- Calendar
# October and November 2026 as Pop draws them, with today on October 1 as in Pop's own demo. The lunar months and
# the solar terms are from Pop's tables (LunarTable.swift, SolarTerms.swift). The English page starts the week on
# Sunday, the Chinese one on Monday; lunar day and month names stay in Chinese in both, as in Pop.
CAL_TODAY = datetime.date(2026, 10, 1)
CAL_LUNAR_MONTHS = [(datetime.date(2026, 9, 11), "八月"), (datetime.date(2026, 10, 10), "九月"),
                    (datetime.date(2026, 11, 9), "十月"), (datetime.date(2026, 12, 9), "冬月")]
CAL_FESTIVALS = {(10, 1): T("National Day", "国庆节"), (10, 18): T("Double Ninth Festival", "重阳节")}
CAL_TERMS = {(10, 8): T("Cold Dew", "寒露"), (10, 23): T("Frost’s Descent", "霜降"), (11, 7): T("Start of Winter", "立冬"),
             (11, 22): T("Minor Snow", "小雪"), (12, 7): T("Major Snow", "大雪")}
CAL_MONTHS = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
CAL_DAYS = [("Monday", "星期一"), ("Tuesday", "星期二"), ("Wednesday", "星期三"), ("Thursday", "星期四"), ("Friday", "星期五"),
            ("Saturday", "星期六"), ("Sunday", "星期日")]
CAL_HEADS = (["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"], ["一", "二", "三", "四", "五", "六", "日"])
CAL_SVG = ('<span class="pl-btn"><svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="2.2" '
           'stroke-linecap="round" stroke-linejoin="round"><path d="{d}"/></svg></span>')
CAL_PREV, CAL_NEXT = CAL_SVG.format(d="m14.5 6-6 6 6 6"), CAL_SVG.format(d="m9.5 6 6 6-6 6")


def _lunar_day(n):
    digits = ["", "一", "二", "三", "四", "五", "六", "七", "八", "九", "十"]
    if n <= 10:
        return "初" + digits[n]
    if n < 20:
        return "十" + digits[n - 10]
    if n == 20:
        return "二十"
    return "廿" + digits[n - 20] if n < 30 else "三十"


def _lunar(d):
    """(month name, day) of the lunar date."""
    start, month = max(x for x in CAL_LUNAR_MONTHS if x[0] <= d)
    return month, (d - start).days + 1


def _cal_note(d, i):
    """What a day's cell says under the date: a festival, a solar term, the lunar month on its first day, or the lunar day."""
    key = (d.month, d.day)
    if key in CAL_FESTIVALS:
        return "fe", CAL_FESTIVALS[key][i]
    if key in CAL_TERMS:
        return "st", CAL_TERMS[key][i]
    month, n = _lunar(d)
    return ("lm", month) if n == 1 else ("", _lunar_day(n))


def cal_head(first, sel):
    def make(i):
        title = f"{CAL_MONTHS[first.month - 1]} {first.year}" if i == 0 else f"{first.year}年{first.month}月"
        last = (first.replace(day=28) + datetime.timedelta(days=4)).replace(day=1) - datetime.timedelta(days=1)
        a, b = _lunar(first)[0], _lunar(last)[0]
        sub = "丙午年 " + (a if a == b else f"{a}—{b}")
        off = " is-off" if sel == CAL_TODAY else ""
        today = ("Today", "今天")[i]
        return (f'<div class="pl-cal-h"><div><strong>{title}</strong><small>{sub}</small></div>{CAL_PREV}'
                f'<span class="pl-btn{off}">{today}</span>{CAL_NEXT}</div>')
    return {"t": "html", "html": T(make(0), make(1))}


def cal_grid(first, sel):
    def make(i):
        lead = (first.weekday() + 1) % 7 if i == 0 else first.weekday()
        start = first - datetime.timedelta(days=lead)
        cells = []
        for k in range(42):
            d = start + datetime.timedelta(days=k)
            kind, note = _cal_note(d, i)
            cls = "".join(c for c, on in ((" out", d.month != first.month), (" we", d.weekday() >= 5), (" today", d == CAL_TODAY),
                                         (" is-on", d == sel)) if on)
            cells.append(f'<span class="pl-cell{cls}" data-d="{d.isoformat()}"><b>{d.day}</b><i class="{kind}">{note}</i></span>')
        heads = "".join(f'<span class="pl-cal-w">{h}</span>' for h in CAL_HEADS[i])
        return f'<div class="pl-cal"><div class="pl-cal-g">{heads}{"".join(cells)}</div></div>'
    return {"t": "html", "html": T(make(0), make(1))}


def cal_detail(d):
    def make(i):
        days = (d - CAL_TODAY).days
        wd = CAL_DAYS[d.weekday()][i]
        month, n = _lunar(d)
        lunar = "丙午年（马年）" + month + _lunar_day(n)
        event = CAL_FESTIVALS.get((d.month, d.day)) or CAL_TERMS.get((d.month, d.day))
        week, yday = d.isocalendar()[1], d.timetuple().tm_yday
        nxt = min(datetime.date(2026, m, dd) for (m, dd) in CAL_TERMS if datetime.date(2026, m, dd) > d)
        term = CAL_TERMS[(nxt.month, nxt.day)][i]
        gap = (nxt - d).days
        if i == 0:
            head = f"{wd}, {CAL_MONTHS[d.month - 1]} {d.day}, {d.year}"
            rel = "Today" if days == 0 else f"In {days} days"
            lines = [f"Lunar: {lunar}", f"Week {week} · Day {yday} of the year",
                     f"Next solar term: {term} on {CAL_MONTHS[nxt.month - 1]} {nxt.day}, in {gap} days"]
        else:
            head = f"{d.year}年{d.month}月{d.day}日 {wd}"
            rel = "今天" if days == 0 else f"{days} 天后"
            lines = [f"农历{lunar}", f"第 {week} 周 · 全年第 {yday} 天", f"下一个节气：{term}，{nxt.month}月{nxt.day}日，还有 {gap} 天"]
        ev = f'<span class="fe">{event[i]}</span>' if event else ""
        em = '<em class="is-today">' if days == 0 else "<em>"
        return (f'<div class="pl-cal-dt"><div><strong>{head}</strong>{em}{rel}</em></div>'
                f'<span>{lines[0]}</span>{ev}<span class="mu">{lines[1]}</span><span class="mu">{lines[2]}</span></div>')
    return {"t": "html", "html": T(make(0), make(1))}


_CHK = ('<span class="pl-chk is-on"><svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="2.4" '
        'stroke-linecap="round" stroke-linejoin="round"><path d="m5 12.5 4.5 4.5L19 7.5"/></svg></span>')
# Pop lays the footer out on one line in Chinese; in English the key hint goes on a line of its own.
CAL_FOOT = {"t": "html", "html": T(
    f'<div class="pl-cal-f"><label>{_CHK}Lunar Dates &amp; Solar Terms</label><span class="sp"></span><span class="pl-btn">Copy</span>'
    '<span class="br"></span><small>Arrows: day · Page Up/Down: month · T: today</small></div>',
    f'<div class="pl-cal-f is-one"><label>{_CHK}农历和节气</label><span class="sp"></span><small>方向键换一天 · PageUp/Down 换月 · T 今天</small>'
    '<span class="pl-btn">复制</span></div>')}
OCT, NOV = datetime.date(2026, 10, 1), datetime.date(2026, 11, 1)
D18, D23, N23 = datetime.date(2026, 10, 18), datetime.date(2026, 10, 23), datetime.date(2026, 11, 23)


DATA = {
    "chart": {
        "chips": [T("Bar · Line · Pie", "柱状 · 折线 · 饼图"), T("Reads tables and lists", "认得表格和列表"), "1920 × 1200"],
        "points": [
            T("Select a table (copied from a spreadsheet, CSV or Markdown), one “name value” per line, or a list of numbers, and Pop <b>draws a chart</b>.",
              "选中表格（从表格软件复制的、CSV、Markdown 表格）、一行一个「名字 数值」，或者一串数，Pop 就<b>画成图表</b>。"),
            T("Bar, horizontal bar, line or pie. Months and quarters start as a line; long or many names start as horizontal bars.",
              "柱状图、条形图、折线图、饼图。按月份、季度排的先画成折线，名字长或者很多的先画成条形图。"),
            T("Understands headers, thousands separators, percent signs, currencies and units, and several series in different colors.",
              "认得表头、千分位、百分号、货币符号和单位，几组数用不同颜色并排画。"),
            T("Add a title, show values, sort from largest, then <b>copy it as an image</b> (1920 × 1200) or save it to Downloads.",
              "可以加标题、显示数值、从大到小排，然后<b>复制成图片</b>（1920 × 1200）或者存到「下载」。"),
        ],
        "scene": {
            "src": {"kind": "text", "app": "Numbers", "title": T("Sales.numbers", "销售.numbers"), "mono": True, "cap": T("Select a table or a list", "选中表格或者列表"),
                    "lines": [T("[[Month\tSales", "[[月份\t销售额"), T("January\t1,200", "一月\t1,200"), T("February\t1,850", "二月\t1,850"),
                              T("March\t2,400", "三月\t2,400"), T("April\t2,100", "四月\t2,100"), T("May\t3,050]]", "五月\t3,050]]")]},
            "card": {"w": 380, "sub": T("5 values", "5 个数"), "btns": [T("Copy Image", "复制图片"), T("Save to Downloads", "存到「下载」")],
                     "body": [{"t": "seg", "items": [T("Bar", "柱状"), T("Line", "折线"), T("Pie", "饼图")], "on": 1, "ctl": 1},
                              {"t": "panes", "on": 1, "panes": [
                                  [{"t": "chart", "kind": "bar", "title": T("Sales", "销售额"), "data": [[T("Jan", "一月"), 1200, "1,200"], [T("Feb", "二月"), 1850, "1,850"], [T("Mar", "三月"), 2400, "2,400"], [T("Apr", "四月"), 2100, "2,100"], [T("May", "五月"), 3050, "3,050"]]}],
                                  [{"t": "chart", "kind": "line", "title": T("Sales", "销售额"), "data": [[T("Jan", "一月"), 1200], [T("Feb", "二月"), 1850], [T("Mar", "三月"), 2400], [T("Apr", "四月"), 2100], [T("May", "五月"), 3050]]}],
                                  [{"t": "chart", "kind": "pie", "data": [[T("Jan", "一月"), 1200], [T("Feb", "二月"), 1850], [T("Mar", "三月"), 2400], [T("Apr", "四月"), 2100], [T("May", "五月"), 3050]]}],
                              ]}]},
            "steps": [
                {"cap": T("Months become a line chart", "按月份的数据画成折线"), "acts": []},
                {"cap": T("Switch to bars or a pie", "换成柱状图或者饼图"), "acts": [["click", "opt:0.0"], ["wait", 1100], ["click", "opt:0.2"]]},
                {"cap": T("Copy it as an image", "复制成图片"), "sub": T("Paste it into a document or a chat.", "贴进文档、聊天里。"),
                 "acts": [["click", "btn:0", ["toast", T("Copied", "已复制")]]]},
            ],
        },
    },
    "numberStats": {
        "chips": [T("Sum · Average · Median", "合计 · 平均 · 中位数"), "1,200 · −8 · $4.50", T("A column or a row", "一列或者一行")],
        "points": [
            T("Select a column of numbers, or one line of numbers separated by commas or spaces, and get the <b>sum, average, median, max and min</b>, and how many there are.",
              "选中一列数字，或者一行用逗号、空格隔开的数字，算出<b>合计、平均、中位数、最大、最小</b>和个数。"),
            T("Lines can start with words, like “Taxi 23.00”: Pop takes the number at the end of each line.",
              "每行前面可以带文字，比如「打车 46」：取每行最后的那个数。"),
            T("Thousands separators, negative numbers and currency signs are understood.", "千分位、负数、货币符号都认得。"),
            T("It shows up on the ring only when the selection really is a list of numbers. Copy any result with one click.",
              "只有选中的真是一串数字时圆盘里才出现；每个结果都能一键复制。"),
        ],
        "scene": {
            "src": {"kind": "text", "app": "Notes", "cap": T("Select a list of numbers", "选中一串数字"),
                    "sub": T("Words in front of the numbers are fine.", "数字前面带着文字也行。"),
                    "lines": [T("# Trip expenses", "# 出差报销"), T("[[Taxi from the airport 23.00", "[[机场打车 46"), T("Coffee 4.50", "咖啡 18"),
                              T("Lunch 12.80", "午饭 32.5"), T("Museum tickets 36.40", "博物馆门票 89.9"), T("Dinner 28.75", "晚饭 76"),
                              T("Bus pass 9.60]]", "公交卡 25]]")]},
            "card": {"w": 300, "body": [
                {"t": "rows", "rows": [[T("Sum", "合计"), T("115.05", "287.4")], [T("Average", "平均"), T("19.175", "47.9")],
                                       [T("Median", "中位数"), T("17.9", "39.25")], [T("Max", "最大"), T("36.4", "89.9")],
                                       [T("Min", "最小"), T("4.5", "18")], [T("Count", "个数"), "6"]]},
                {"t": "note", "text": T("6 numbers", "共 6 个数")}]},
            "steps": [
                {"cap": T("Sum, average, median…", "合计、平均、中位数……"), "acts": [["wait", 400], ["hover", "row:0.1"], ["wait", 500], ["hover", "row:0.2"], ["wait", 300]]},
                {"cap": T("Copy the total", "复制合计"),
                 "acts": [["click", copy_icon(0, 0), [["addClass", "row:0.0", "is-hl"], ["toast", COPIED]]]]},
            ],
        },
    },
    "changeCase": {
        "chips": [T("UPPERCASE · lowercase", "大写 · 小写"), "camelCase · PascalCase", "snake_case · kebab-case"],
        "points": [
            T("Select a word, a phrase or a variable name and see it in <b>eight cases</b> at once: UPPERCASE, lowercase, Capitalized, camelCase, PascalCase, snake_case, kebab-case and CONSTANT.",
              "选中一个词、一句话或者变量名，一次列出<b>八种写法</b>：大写、小写、首字母大写、camelCase、PascalCase、snake_case、kebab-case、CONSTANT。"),
            T("Names written in one piece are split into words first, acronyms included: getHTTPResponse becomes get, HTTP, Response.",
              "连在一起的名字先拆成单词，连着的大写缩写也拆得开：getHTTPResponse 拆成 get、HTTP、Response。"),
            T("Copy any line, or <b>put it back</b> in place of the selection.", "每一行都能复制，也能直接<b>替换原文</b>。"),
        ],
        "scene": {
            "slot": 1,
            "src": {"kind": "text", "app": "Xcode", "title": "Profile.swift", "mono": True, "cap": T("Select a name", "选中一个名字"),
                    "lines": ["struct Profile {", "    let [[userProfileId]]: Int", "    let displayName: String", "}"]},
            "card": {"w": 320, "title": T("Change Case", "大小写转换"), "body": [
                {"t": "rows", "rows": [[T("UPPERCASE", "大写"), "USERPROFILEID"], [T("lowercase", "小写"), "userprofileid"],
                                       [T("Capitalized", "首字母大写"), "Userprofileid"], ["camelCase", "userProfileId"], ["PascalCase", "UserProfileId"],
                                       ["snake_case", "user_profile_id"], ["kebab-case", "user-profile-id"], ["CONSTANT", "USER_PROFILE_ID"]]}]},
            "steps": [
                {"cap": T("Every case at once", "各种写法一次列出"), "acts": []},
                {"cap": T("Copy the snake_case one", "复制 snake_case 的写法"), "sub": T("Or put it back in place of the selection.", "也可以直接替换原文。"),
                 "acts": [["hover", "row:0.5"], ["addClass", "row:0.5", "is-hl"], ["click", copy_icon(0, 5), ["toast", COPIED]]]},
            ],
        },
    },
    "encodeDecode": {
        "chips": ["Base64 · URL", T("Unicode · HTML entities", "Unicode · HTML 实体"), T("Decoded first", "能解码的排在前面")],
        "points": [
            T("Select text and see it as <b>Base64, URL encoding, Unicode escapes and HTML entities</b>, one per line.",
              "选中文字，列出 <b>Base64、URL 编码、Unicode 转义、HTML 实体</b>，一种一行。"),
            T("When the selection is already encoded, the decoded text comes first: Base64 (standard or URL-safe), %XX, <code>\\uXXXX</code> and HTML entities.",
              "选中的已经是编码过的文字时，解码的结果排在最前面：Base64（标准的和 URL 安全的都认）、%XX、<code>\\uXXXX</code>、HTML 实体。"),
            T("Copy any line, or replace the selection with it.", "每一行都能复制，也能直接替换原文。"),
        ],
        "scene": {
            "slot": 3,
            "src": {"kind": "text", "app": "Console", "title": "access.log", "mono": True, "cap": T("Select encoded text", "选中编码过的文字"),
                    "lines": [T("10:42:07 GET /search?[[q=caf%C3%A9%20au%20lait&lang=fr]] 200", "10:42:07 GET /search?[[q=%E5%92%96%E5%95%A1&city=%E4%B8%8A%E6%B5%B7]] 200"),
                              "10:42:09 GET /static/app.js 304", "10:42:12 POST /api/cart 201"]},
            "card": {"w": 360, "title": T("Encode & Decode", "编码转换"), "body": [
                {"t": "rows", "rows": [[T("URL Decoded", "URL 解码"), T("q=café au lait&lang=fr", "q=咖啡&city=上海")],
                                       [T("Base64 Encoded", "Base64 编码"), T("cT1jYWYlQzMlQTklMjBhdSUyMGxhaXQmbGFuZz1mcg==", "cT0lRTUlOTIlOTYlRTUlOTUlQTEmY2l0eT0lRTQlQjglOEElRTYlQjUlQjc=")],
                                       [T("URL Encoded", "URL 编码"), T("q%3Dcaf%25C3%25A9%2520au%2520lait%26lang%3Dfr", "q%3D%25E5%2592%2596%25E5%2595%25A1%26city%3D%25E4%25B8%258A%25E6%25B5%25B7")],
                                       [T("HTML Escaped", "HTML 转义"), T("q=caf%C3%A9%20au%20lait&amp;lang=fr", "q=%E5%92%96%E5%95%A1&amp;city=%E4%B8%8A%E6%B5%B7")]]}]},
            "steps": [
                {"cap": T("Decoded first, then each encoding", "先解码，再列出各种编码"), "acts": [["wait", 300], ["addClass", "row:0.0", "is-hl"]], "hold": 1600},
                {"cap": T("Copy the line you need", "复制要用的那一行"), "acts": [["click", copy_icon(0, 0), ["toast", COPIED]]]},
            ],
        },
    },
    "yamlJSON": {
        "chips": ["JSON → YAML", "YAML → JSON", T("Key order kept", "键的顺序不变")],
        "points": [
            T("Select JSON to get YAML, or select YAML, such as a config file or a CI workflow, to get JSON.",
              "选中 JSON 转成 YAML，选中 YAML（配置文件、CI 工作流……）转成 JSON。"),
            T("<b>Keys stay in their order</b>, and numbers are kept exactly as written.", "<b>键的顺序不变</b>，数字按原样保留。"),
            T("Understands comments, multi-line text (| and >), “- key: value”, [a, b] and {a: 1}. If something’s wrong, it tells you which line.",
              "认得注释、多行文字（| 和 >）、「- key: value」、[a, b] 和 {a: 1} 这些常用写法，写错了会指出是第几行。"),
            T("Copy the result or replace the selection with it; JSON made from YAML can also be copied minified.",
              "结果可以复制、替换原文；YAML 转成的 JSON 还能复制压缩版。"),
        ],
        "scene": {
            "src": {"kind": "text", "app": "Xcode", "title": "config.json", "mono": True, "cap": T("Select JSON or YAML", "选中 JSON 或者 YAML"),
                    "lines": ["[[{", '  "name": "pop",', '  "version": "0.59.0",', '  "ports": [80, 443],', '  "owner": { "login": "whrss9527", "site": null },',
                              T('  "tags": ["productivity", "mac app"]', '  "tags": ["效率", "mac app"]'), "}]]"]},
            "card": {"w": 320, "title": T("JSON to YAML", "JSON 转 YAML"), "btns": [T("Copy", "复制"), T("Replace", "替换原文")], "body": [
                {"t": "code", "lang": "yaml", "text": T('name: pop\nversion: "0.59.0"\nports:\n  - 80\n  - 443\nowner:\n  login: whrss9527\n  site: null\ntags:\n  - productivity\n  - mac app',
                                                         'name: pop\nversion: "0.59.0"\nports:\n  - 80\n  - 443\nowner:\n  login: whrss9527\n  site: null\ntags:\n  - 效率\n  - mac app')}]},
            "steps": [
                {"cap": T("JSON becomes YAML", "JSON 转成 YAML"), "sub": T("Keys stay in the same order.", "键的顺序不变。"), "acts": [], "hold": 1700},
                {"cap": T("Press ⌘C to copy it", "按 ⌘C 复制"), "sub": T("Select YAML instead and you get JSON.", "选中的是 YAML 就转成 JSON。"),
                 "acts": [["key", "⌘C", ["toast", COPIED]]]},
            ],
        },
    },
    "formatXML": {
        "chips": ["SVG · plist · XHTML", T("Format or minify", "格式化或者压缩"), T("Replace in place", "直接替换原文")],
        "points": [
            T("Select XML that’s squeezed onto one line or badly indented, and get it <b>neatly indented</b>, one level per tag.",
              "选中挤成一行或者缩进乱了的 XML，按层级<b>重新缩进</b>，一层一级。"),
            T("SVG, plist and XHTML are read too.", "SVG、plist、XHTML 也认。"),
            T("Copy the result, replace the selection with it, or <b>copy a minified version</b> without the whitespace between tags.",
              "结果可以复制、替换原文，也可以<b>复制压缩版</b>：去掉标签之间的空白，压成一行。"),
        ],
        "scene": {
            "slot": 1,
            "src": {"kind": "text", "app": "TextEdit", "title": "Info.plist", "mono": True, "cap": T("Select some XML", "选中一段 XML"),
                    "lines": ['[[<?xml version="1.0" encoding="UTF-8"?><plist version="1.0"><dict><key>CFBundleName</key><string>Pop</string><key>LSUIElement</key><true/></dict></plist>]]']},
            "card": {"w": 340, "title": T("Format XML", "XML 格式化"), "btns": [T("Copy", "复制"), T("Replace", "替换原文"), T("Copy Minified", "复制压缩版")], "body": [
                {"t": "code", "lang": "xml", "text": '<?xml version="1.0" encoding="UTF-8"?>\n<plist version="1.0">\n    <dict>\n        <key>CFBundleName</key>\n'
                                                     '        <string>Pop</string>\n        <key>LSUIElement</key>\n        <true/>\n    </dict>\n</plist>'}]},
            "steps": [
                {"cap": T("One tag per line, indented", "一层一层缩进好"), "acts": [], "hold": 1600},
                {"cap": T("Or copy it minified", "也可以复制压缩版"), "acts": [["click", "btn:2", ["toast", COPIED]]]},
            ],
        },
    },
    "formatSQL": {
        "chips": ["SELECT · JOIN · WHERE", T("Subqueries indented", "子查询缩进一层"), T("Back to one line", "也能压回一行")],
        "points": [
            T("Select a query squeezed onto one line and get <b>one clause per line</b>, with the keywords in capitals.",
              "选中挤在一行里的 SQL，<b>按子句分行</b>、关键字大写。"),
            T("SELECT columns and SET and VALUES items go one per line when there are several; AND and OR in WHERE start indented lines, and subqueries are indented a level.",
              "SELECT 的字段和 SET、VALUES 有好几项时一项一行，WHERE 里的 AND、OR 换行缩进，子查询缩进一层。"),
            T("Strings, quoted names and comments are left exactly as they are.", "字符串、带引号的名字和注释原样保留。"),
            T("Copy it, replace the selection with it, or <b>copy it as one line</b> again.", "可以复制、替换原文，也可以<b>压成一行</b>复制。"),
        ],
        "scene": {
            "slot": 3,
            "src": {"kind": "text", "app": "TextEdit", "title": "slow-queries.log", "mono": True, "cap": T("Select a query", "选中一条 SQL"),
                    "lines": ["-- 2026-10-02 09:14:07 (2.41 s)",
                              "[[select u.id, u.name, count(o.id) as orders from users u left join orders o on o.user_id = u.id where u.created_at >= '2026-01-01' and u.vip = true group by u.id, u.name order by orders desc limit 20]]",
                              "-- 2026-10-02 09:15:22 (0.08 s)", "select * from plans where id = 3"]},
            "card": {"w": 340, "title": T("Format SQL", "SQL 格式化"), "btns": [T("Copy", "复制"), T("Replace", "替换原文"), T("Copy as One Line", "复制成一行")], "body": [
                {"t": "code", "lang": "sql", "text": "SELECT\n  u.id,\n  u.name,\n  count(o.id) AS orders\nFROM users u\nLEFT JOIN orders o ON o.user_id = u.id\n"
                                                     "WHERE u.created_at >= '2026-01-01'\n  AND u.vip = TRUE\nGROUP BY u.id, u.name\nORDER BY orders DESC\nLIMIT 20"}]},
            "steps": [
                {"cap": T("One clause per line", "按子句分行"), "sub": T("Keywords in capitals, conditions indented.", "关键字大写，条件缩进。"), "acts": [], "hold": 1800},
                {"cap": T("Or squeeze it onto one line", "也可以压回一行"), "acts": [["click", "btn:2", ["toast", COPIED]]]},
                {"cap": T("Replace the query in place", "直接替换原文"), "sub": T("Replace (⌘↩) puts it back where it was.", "「替换原文」（⌘↩）放回原来的位置。"),
                 "acts": [["click", "btn:1"], ["replace", "SELECT\n  u.id,\n  u.name,\n  count(o.id) AS orders\nFROM users u\nLEFT JOIN orders o ON o.user_id = u.id\n"
                                                         "WHERE u.created_at >= '2026-01-01'\n  AND u.vip = TRUE\nGROUP BY u.id, u.name\nORDER BY orders DESC\nLIMIT 20"]]},
            ],
        },
    },
    "tableConvert": {
        "chips": ["CSV · Markdown · JSON", T("From a spreadsheet", "从表格软件复制的"), T("First row as header", "第一行当表头")],
        "points": [
            T("Select a table, copied from a spreadsheet, as CSV or as a Markdown table, and get it in the <b>other formats</b>: Markdown, CSV, tab-separated or JSON.",
              "选中一个表格（从表格软件复制的文字、CSV 或者 Markdown 表格），转成<b>其他格式</b>：Markdown、CSV、制表符分隔、JSON。"),
            T("For JSON, the first row gives the keys and every other row becomes an object.", "转成 JSON 时第一行当作键名，其余每行一个对象。"),
            T("It needs at least two rows and two columns, with the same number of columns in every row.", "至少两行两列，每行的列数一样。"),
            T("Copy any format, or <b>replace the selection</b> with it.", "每种格式都能复制，也能直接<b>替换原文</b>。"),
        ],
        "scene": {
            "src": {"kind": "text", "app": "Numbers", "title": T("Team.numbers", "团队.numbers"), "mono": True, "cap": T("Select a table", "选中一个表格"),
                    "sub": T("From a spreadsheet, CSV or a Markdown table.", "从表格软件复制的、CSV、Markdown 表格都行。"),
                    "lines": [T("[[" + "\t".join(r), "[[" + "\t".join(z)) if i == 0 else T("\t".join(r) + ("]]" if i == 3 else ""), "\t".join(z) + ("]]" if i == 3 else ""))
                              for i, (r, z) in enumerate(zip(TABLE_EN, TABLE_ZH))]},
            "card": {"w": 360, "title": T("Convert Table", "表格转换"), "body": [
                {"t": "html", "html": T(table_rows(TABLE_EN), table_rows(TABLE_ZH))},
                {"t": "note", "text": T("4 rows × 3 columns (first row as header)", "4 行 × 3 列（第一行当作表头）")}]},
            "steps": [
                {"cap": T("Markdown, CSV and JSON", "转成 Markdown、CSV、JSON"), "acts": [], "hold": 1800},
                {"cap": T("Copy the Markdown table", "复制 Markdown 表格"), "sub": T("Or replace the selection with it.", "也可以直接替换原文。"),
                 "acts": [["hover", "row:0.0"], ["addClass", "row:0.0", "is-hl"], ["click", copy_icon(0, 0), ["toast", COPIED]]]},
            ],
        },
    },
    "markdown": {
        "chips": [T("Preview", "预览"), T("Copy as Rich Text", "复制为富文本"), T("Headings · lists · quotes", "标题 · 列表 · 引用")],
        "points": [
            T("<b>Markdown Preview</b> shows the selected Markdown formatted: headings, lists, bold, code, quotes… Select part of it to copy, or copy all of it as rich text.",
              "<b>Markdown 预览</b>：把选中的 Markdown 显示成排好版的样子（标题、列表、粗体、代码、引用……），可以选中一部分复制，也可以整段复制为富文本。"),
            T("<b>Copy as Rich Text</b> skips the preview and copies it as formatted text right away.",
              "<b>复制为富文本</b>：不用预览，直接转成带格式的文字复制下来。"),
            T("Paste it into documents, Mail or Notes, and headings, bold, italics, code, links, lists and quotes keep their formatting.",
              "粘贴到文稿、邮件、备忘录里，标题、粗体、斜体、代码、链接、列表、引用都保留格式。"),
            T("They are two separate actions, so you can put either one on the ring.", "这是两个分开的功能，哪个都能放上圆盘。"),
        ],
        "scene": {
            "slot": 1,
            "src": {"kind": "text", "app": "TextEdit", "title": "release.md", "mono": True, "cap": T("Select some Markdown", "选中一段 Markdown"),
                    "lines": [T("[[## Release checklist", "[[## 发布清单"), T("- Update the __CHANGELOG__", "- 更新 __CHANGELOG__"),
                              T("- Bump the version number", "- 改版本号"), T("- Tag the release", "- 打上 tag"),
                              T("> Merging to main publishes it]]", "> 合并到 main 后自动发版]]")]},
            "card": {"w": 320, "title": T("Markdown Preview", "Markdown 预览"), "btns": [T("Copy as Rich Text", "复制为富文本")], "tint": 0, "body": [
                {"t": "html", "html": T(preview("Release checklist", ["Update the <b>CHANGELOG</b>", "Bump the version number", "Tag the release"], "Merging to main publishes it"),
                                        preview("发布清单", ["更新 <b>CHANGELOG</b>", "改版本号", "打上 tag"], "合并到 main 后自动发版"))}]},
            "steps": [
                {"cap": T("See it formatted", "显示成排好版的样子"), "acts": [], "hold": 1800},
                {"cap": T("Copy it as rich text", "复制为富文本"), "sub": T("Paste it into Mail, Notes or a document with the formatting.", "粘贴到邮件、备忘录、文稿里，格式都在。"),
                 "acts": [["click", "btn:0", ["toast", T("Copied as rich text", "已复制为富文本")]]]},
            ],
        },
    },
    "toMarkdown": {
        "chips": [T("Headings · links · tables", "标题 · 链接 · 表格"), T("Task lists · code", "任务列表 · 代码块"), T("Web pages and Mail", "网页、邮件、文档")],
        "points": [
            T("Select formatted text in a web page, an email or a document and get <b>Markdown</b>.", "在网页、邮件、文档里选中一段带格式的文字，转成 <b>Markdown</b>。"),
            T("Headings, paragraphs, bold, italics, strikethrough, links, images, lists (task lists too), quotes, code blocks with their language and tables are all kept.",
              "标题、段落、粗体、斜体、删除线、链接、图片、列表（包括任务列表）、引用、代码块（带语言）、表格都保留。"),
            T("In apps that only provide RTF, such as TextEdit and Pages, bold, italics, monospaced text, links and lists are worked out from the fonts.",
              "只有 RTF 的 App（比如文本编辑、Pages）按字体转换粗体、斜体、等宽字体、链接和列表。"),
            T("Copy the Markdown, or <b>pin it to the screen</b>.", "可以复制，也可以<b>贴到屏幕</b>上。"),
        ],
        "scene": {
            "slot": 3,
            "src": {"kind": "web", "app": "Safari", "url": "pop.example.com/blog/0-59", "cap": T("Select formatted text", "选中带格式的文字"),
                    "sub": T("On a web page, in Mail or in a document.", "网页、邮件、文档里都行。"),
                    "lines": [T("[[What’s new in Pop 0.59", "[[Pop 0.59 更新说明"), T("Adds **Emoji & Symbols**.", "新增**表情和符号**插件。"),
                              T("• Search by name or pinyin", "• 用中文、拼音或英文搜"), T("• Recent ones come first", "• 最近用过的排在前面"),
                              T("• Insert with a click]]", "• 点一下就插进去]]")],
                    "more": [T("Install it from Settings › Actions.", "在「设置 → 功能」里安装。")]},
            "card": {"w": 330, "title": T("Convert to Markdown", "转成 Markdown"), "btns": [T("Copy", "复制"), T("Pin to Screen", "贴到屏幕")], "body": [
                {"t": "code", "lang": "md", "text": T("## What’s new in Pop 0.59\n\nAdds **Emoji & Symbols**.\n\n- Search by name or pinyin\n- Recent ones come first\n- Insert with a click",
                                                       "## Pop 0.59 更新说明\n\n新增**表情和符号**插件。\n\n- 用中文、拼音或英文搜\n- 最近用过的排在前面\n- 点一下就插进去")}]},
            "steps": [
                {"cap": T("The same text, in Markdown", "转成 Markdown"), "sub": T("Headings, bold and lists come along.", "标题、粗体、列表都在。"), "acts": [], "hold": 1800},
                {"cap": T("Copy it", "复制下来"), "sub": T("Or pin it on the screen while you write.", "也可以贴到屏幕上，边看边写。"),
                 "acts": [["click", "btn:0", ["toast", COPIED]]]},
            ],
        },
    },
    "markdownTOC": {
        "chips": [T("#use-the-ring", "#使用圆盘"), T("GitHub-style anchors", "锚点和 GitHub 一样"), T("Duplicates numbered", "重名的自动编号")],
        "points": [
            T("Select a Markdown document and get a <b>table of contents</b> from its headings, indented by level.",
              "选中一篇 Markdown，按里面的标题生成<b>目录</b>，按级别缩进。"),
            T("Each entry links to its heading, with the anchor written the way GitHub writes it; headings with the same name get numbers.",
              "每一项都链到对应的标题，锚点和 GitHub 的写法一样，重名的标题自动加编号。"),
            T("A # inside a code block isn’t taken for a heading.", "代码块里的 # 不算标题。"),
        ],
        "scene": {
            "src": {"kind": "text", "app": "TextEdit", "title": "README.md", "mono": True, "cap": T("Select a Markdown document", "选中一篇 Markdown"),
                    "lines": ["[[# Pop", T("Right-click toolbox for macOS.", "macOS 上的右键工具箱。"), T("## Install", "## 安装"), T("## Use the ring", "## 使用圆盘"),
                              T("### Hold and swipe", "### 按住右键一划"), T("### Add actions", "### 添加功能"), T("## Plugins]]", "## 插件]]")]},
            "card": {"w": 350, "title": T("Markdown Table of Contents", "Markdown 目录"), "btns": [T("Copy", "复制")], "body": [
                {"t": "code", "lang": "md", "text": T("- [Pop](#pop)\n  - [Install](#install)\n  - [Use the ring](#use-the-ring)\n    - [Hold and swipe](#hold-and-swipe)\n"
                                                       "    - [Add actions](#add-actions)\n  - [Plugins](#plugins)",
                                                       "- [Pop](#pop)\n  - [安装](#安装)\n  - [使用圆盘](#使用圆盘)\n    - [按住右键一划](#按住右键一划)\n"
                                                       "    - [添加功能](#添加功能)\n  - [插件](#插件)")},
                {"t": "note", "text": T("6 headings", "6 个标题")}]},
            "steps": [
                {"cap": T("A linked table of contents", "生成带链接的目录"), "acts": [], "hold": 1800},
                {"cap": T("Copy it into the README", "复制到 README 里"), "sub": T("The links jump to each heading, on GitHub too.", "点链接跳到对应的标题，在 GitHub 上也一样。"),
                 "acts": [["click", "btn:0", ["toast", COPIED]]]},
            ],
        },
    },
    "dateSpan": {
        "chips": [T("Days · weeks · months", "天 · 周 · 月"), T("Workdays", "工作日"), "2026-09-29 → 12-25"],
        "points": [
            T("Select two dates, like “2026-09-29 to 2026-12-25”, and see <b>how many days</b> are between them.",
              "选中两个日期（比如「2026-09-29 到 2026-12-25」），算出<b>相差多少天</b>。"),
            T("Also in weeks and days, in years, months and days, and counting both the first and the last day.",
              "还有折合几周几天、几年几个月几天，以及首尾都算是多少天。"),
            T("And how many of them are <b>workdays</b>, Monday to Friday (holidays aren’t taken out).",
              "以及其中有多少个<b>工作日</b>（周一到周五，不算节假日）。"),
            T("Dates can be written 2026-09-29, 2026/9/29 or 2026.9.29, on one line or on two.",
              "日期可以写成 2026-09-29、2026/9/29、2026年9月29日，写在一行或者两行都行。"),
        ],
        "scene": {
            "slot": 1,
            "src": {"kind": "text", "app": "Notes", "cap": T("Select two dates", "选中两个日期"),
                    "lines": [T("# Project plan", "# 项目计划"), T("Kickoff to launch: [[2026-09-29 to 2026-12-25]]", "从启动到上线：[[2026-09-29 到 2026-12-25]]"),
                              T("Reviews every other Friday.", "每两周的周五评审一次。")]},
            "card": {"w": 350, "title": T("Date Difference", "日期计算"), "body": [
                # Pop sizes the label column to the longest label ("Counting both ends"); the rows block would cut it short.
                {"t": "html", "html": T(long_rows([("Difference", "87 days"), ("Equals", "12 weeks 3 days"), ("That is", "2 months 26 days"),
                                                   ("Counting both ends", "88 days"), ("Workdays", "63 days (Monday to Friday, not counting holidays)")], 100, False),
                                        long_rows([("相差", "87 天"), ("折合", "12 周 3 天"), ("也就是", "2 个月 26 天"), ("首尾都算", "88 天"),
                                                   ("工作日", "63 天（周一到周五，不算节假日）")], None, False))},
                {"t": "note", "text": T("From 2026-09-29 Tue to 2026-12-25 Fri", "从 2026-09-29 周二 到 2026-12-25 周五")}]},
            "steps": [
                {"cap": T("87 days between them", "相差 87 天"), "acts": [["wait", 300], ["addClass", "row:0.0", "is-hl"]], "hold": 1500},
                {"cap": T("63 of them are workdays", "其中 63 个工作日"), "acts": [["hover", "row:0.4"], ["addClass", "row:0.4", "is-hl"]], "hold": 1500},
                {"cap": T("Copy any line", "每一行都能复制"), "acts": [["click", copy_icon(0, 4), ["toast", COPIED]]]},
            ],
        },
    },
    "worldTime": {
        "chips": ["3pm PST", T("Working hours in green", "上班时间标成绿色"), T("Find a meeting time", "找开会的时间")],
        "points": [
            T("Select a time such as “3pm PST”, “9 pm Beijing time” or “tomorrow 10:00 London time” and see it <b>in the cities you use</b>, with the date and whether it’s a day earlier or later.",
              "选中「3pm PST」「北京时间晚上 9 点」「明天 10:00 伦敦时间」这样的时间，换算成<b>常用的几个城市</b>的时间，写着当地的日期，比本地早一天还是晚一天。"),
            T("Each city has a 24-hour bar, so you can see whether it’s working hours or the middle of the night there.",
              "每个城市旁边一条一天 24 小时的时间条，看得出那时是上班时间还是半夜。"),
            T("Drag the slider to try other times. When everyone listed is between 9:00 and 18:00 is worked out for you: <b>one click jumps there</b>.",
              "拖动滑块往前往后挪，看那时各地是几点；列出的几个地方都在 9:00–18:00 之间的时间会算出来，<b>点一下跳过去</b>。"),
            T("PST, EST and similar abbreviations follow local daylight saving time even when written as standard time, with a note saying so. A time without a day means the next one.",
              "PST、EST 这类缩写写成了冬令时也按当地实际的时间算，另外提示一句；没写哪天的按接下来的那一次算。"),
            T("With nothing selected, see what time it is everywhere now. Add cities by name, pinyin initials, English name or abbreviation, and copy all the times at once.",
              "什么都不选时看各地现在几点。城市可以用中文、拼音首字母、英文或者时区缩写搜着加，各地的时间可以一键复制。"),
        ],
        "scene": {
            "slot": 3,
            "src": {"kind": "text", "app": "Mail", "title": T("Re: Launch sync", "和伦敦团队的周会"), "cap": T("Select a time", "选中一个时间"),
                    "sub": T("Or nothing, to see the time everywhere now.", "什么都不选，就看各地现在几点。"),
                    "lines": [T("Hi Sam,", "各位："), T("Could we move the launch sync to [[3pm PST]]?", "周会改到[[明天 10:00 伦敦时间]]，大家看看行不行。"),
                              T("Thanks, Ada", "—— Ada")]},
            "card": {"w": 400, "body": [
                {"t": "text", "text": T("“3pm PST” is Thu, Oct 1 15:00 in Los Angeles", "「明天 10:00 伦敦时间」是伦敦 10月2日周五 10:00")},
                {"t": "note", "hide": T(False, True),
                 "text": T("PST is read as local time in Los Angeles, where daylight saving time is in effect that day (UTC−7)", "")},
                wt_hours(0),
                wt_slider(0),
                {"t": "list", "dense": True, "items": [{"icon": PEOPLE, "title": T("Everyone is at work (9:00–18:00)", "大家都在上班（9:00–18:00）"),
                                                        "sub": T("12:00–13:00 local time", "本地 16:00–17:00"), "btn": T("Show Me", "看看那时")}]}],
                     "btns": [T("Add City", "添加城市"), T("Copy", "复制")]},
            "steps": [
                {"cap": T("See it in every city", "换算成各地的时间"), "sub": T("Green on the bars is working hours.", "时间条上绿色的是上班时间。"), "acts": [], "hold": 1800},
                {"cap": T("Drag to try another time", "拖动滑块换个时间"),
                 "acts": [["move", ".pl-sl", 0.5, 0.5], ["wait", 200], ["move", ".pl-sl", WT_SLIDER[1][0], 0.5], ["set", 3, wt_slider(1)], ["set", 2, wt_hours(1)]], "hold": 1500},
                {"cap": T("Find when everyone’s at work", "找大家都在上班的时间"),
                 "acts": [["click", "btn:4.0", [["set", 3, wt_slider(2)], ["set", 2, wt_hours(2)]]]], "hold": 1800},
                {"cap": T("Copy every city’s time", "复制各地的时间"), "acts": [["click", "btn:1", ["toast", COPIED]]]},
            ],
        },
    },
    "calendar": {
        "chips": [T("Lunar dates & solar terms", "农历和节气"), T("Jump to a festival", "翻到节日"), "1900–2100"],
        "points": [
            T("A <b>month calendar</b> with each day’s Chinese lunar date, solar term and festival: lunar festivals such as the Spring Festival and Mid-Autumn, and dates such as New Year’s Day, National Day and Mother’s Day. Today is marked.",
              "<b>一个月的月历</b>，每天写着农历、节气和节日（春节、中秋这些农历节日，元旦、国庆、母亲节这些公历节日），今天的日期标出来。"),
            T("Select text such as “2026-10-01”, “October 1”, “Mid-Autumn Festival”, “冬至” or “农历八月十五” and it <b>jumps to that day</b>; festivals and lunar dates go to the next one from today.",
              "选中「2026-10-01」「10月1日」「中秋节」「冬至」「农历八月十五」这样的文字再用，<b>直接翻到那一天</b>；节日、农历日子翻到今天以后最近的那次。"),
            T("Below the month: the weekday, how far the day is from today, the week number and the next solar term.",
              "下面写着选中的那天是星期几、离今天几天、第几周，还有下一个节气在哪天。"),
            T("Arrow keys move a day, Page Up and Page Down change the month, T goes back to today and ⌘C copies the day. Turn off lunar dates and solar terms to see just the Gregorian calendar.",
              "方向键换一天，PageUp、PageDown 换月，T 回到今天，⌘C 复制这一天；农历和节气可以关掉，只看公历。"),
            T("Solar terms fall on their day in Beijing time; every one from 1900 to 2100 was checked against an astronomical algorithm.",
              "节气按北京时间算到哪一天，1900 到 2100 年每一个都和天文算法对过。"),
        ],
        "scene": {
            "tall": True,
            "src": {"kind": "text", "app": T("Notes", "备忘录"), "cap": T("Select a date or a festival", "选中一个日期或者节日"),
                    "sub": T("Or nothing, to see this month.", "什么都不选，就看这个月。"),
                    "lines": [T("# Autumn plans", "# 秋天的安排"), T("Visit Grandma on the [[Double Ninth Festival]]", "[[重阳节]]回去看外婆"),
                              T("Book the train tickets a week ahead", "提前一周买好火车票")]},
            "card": {"w": 380, "at": "center", "body": [cal_head(OCT, D18), cal_grid(OCT, D18), {"t": "sep"}, cal_detail(D18), CAL_FOOT]},
            "steps": [
                {"cap": T("It opens on that day", "直接翻到那一天"), "sub": T("The next Double Ninth Festival from today.", "今天以后最近的那个重阳节。"),
                 "acts": [["move", "[data-d='2026-10-18']", 0.5, 0.6]], "hold": 1800},
                {"cap": T("Click a day for its details", "点一天看看"), "sub": T("Solar terms in green, festivals in red.", "绿色的是节气，红色的是节日。"),
                 "acts": [["click", "[data-d='2026-10-23']", ["set", 3, cal_detail(D23)]]], "hold": 1600},
                {"cap": T("Page Down for the next month", "PageDown 换到下个月"),
                 "acts": [["key", T("Page Down", "PageDown"), [["set", 0, cal_head(NOV, N23)], ["set", 1, cal_grid(NOV, N23)], ["set", 3, cal_detail(N23)]]]],
                 "hold": 1600},
                {"cap": T("T goes back to today", "按 T 回到今天"),
                 "acts": [["key", "T", [["set", 0, cal_head(OCT, CAL_TODAY)], ["set", 1, cal_grid(OCT, CAL_TODAY)], ["set", 3, cal_detail(CAL_TODAY)]]]],
                 "hold": 1400},
                {"cap": T("⌘C copies the day", "⌘C 复制这一天"), "sub": T("With its lunar date and festival.", "连同农历和节日。"),
                 "acts": [["key", "⌘C", [["close"], ["toast", COPIED]]]]},
            ],
        },
    },
    "numberConvert": {
        "chips": ["0x35E8 · 0b1101…", "13,800", T("RMB in words", "人民币大写")],
        "points": [
            T("Select a number and see it in <b>decimal, hexadecimal, octal and binary</b>.", "选中一个数，换算成<b>十进制、十六进制、八进制、二进制</b>。"),
            T("Also with thousands separators, spelled out in English and in Chinese, and as <b>RMB in words</b> (壹万叁仟捌佰元整).",
              "还有千分位、英文读法、中文读法，以及<b>人民币大写</b>（壹万叁仟捌佰元整）。"),
            T("It reads numbers starting with 0x, 0b or 0o, thousands separators, decimals and negative numbers.", "认得 0x、0b、0o 开头的写法，千分位、小数、负数也行。"),
            T("Copy any line, or replace the selection with it.", "每一行都能复制，也能直接替换原文。"),
        ],
        "scene": {
            "src": {"kind": "text", "app": "Notes", "cap": T("Select a number", "选中一个数"),
                    "lines": [T("# Invoice 1042", "# 合同"), T("Total due: [[13800]]", "合同金额：[[13800]] 元"), T("Due by October 31.", "签订后 10 个工作日内付清。")]},
            "card": {"w": 350, "title": T("Numbers", "数字转换"), "body": [
                {"t": "rows", "rows": [[T("Decimal", "十进制"), "13800"], [T("Hexadecimal", "十六进制"), "0x35E8"], [T("Octal", "八进制"), "0o32750"],
                                       [T("Binary", "二进制"), "0b11010111101000"], [T("Grouped", "千分位"), "13,800"],
                                       [T("In English", "英文读法"), "thirteen thousand eight hundred"], [T("In Chinese", "中文读法"), T("一万三千八百", "一万三千八百")],
                                       [T("RMB in words", "人民币大写"), T("壹万叁仟捌佰元整", "壹万叁仟捌佰元整")]]}]},
            "steps": [
                {"cap": T("Every base at once", "各种进制一次列出"), "acts": [], "hold": 1500},
                {"cap": T("Spelled out in words", "英文、中文读法"), "acts": [["hover", "row:0.5"], ["addClass", "row:0.5", "is-hl"], ["wait", 350], ["addClass", "row:0.6", "is-hl"]], "hold": 1300},
                {"cap": T("Copy the RMB in words", "复制人民币大写"), "sub": T("For invoices and contracts in China.", "开发票、写合同时用。"),
                 "acts": [["click", copy_icon(0, 7), [["addClass", "row:0.7", "is-hl"], ["toast", COPIED]]]]},
            ],
        },
    },
    "contrast": {
        "chips": ["3.26 : 1", "WCAG AA · AAA", T("Normal and large text", "普通和大号文字")],
        "points": [
            T("Select two colors, such as “#333333 #FFFFFF”, and get the <b>contrast ratio</b> of text in the first color on a background of the second.",
              "选中两个颜色（比如「#333333 #FFFFFF」），算出前一个当文字、后一个当背景时的<b>对比度</b>。"),
            T("It says whether normal and large text meet <b>WCAG AA and AAA</b>. Large text means 18pt or larger, or bold 14pt or larger.",
              "看普通文字、大号文字能不能达到 <b>WCAG 的 AA、AAA</b>；大号文字指 18pt 以上，或 14pt 以上的粗体。"),
            T("Colors can be hex, rgb() or hsl(), with a word such as “on”, a comma or a slash between them. Click a color to copy it.",
              "颜色可以写成十六进制、rgb()、hsl()，中间可以有「on」「和」、逗号、斜杠；点一下颜色复制色值。"),
            T("The Convert Color card also shows a single color’s contrast on white and on black.", "「颜色转换」卡片下面也会写出一个颜色在白底、黑底上的对比度。"),
        ],
        "scene": {
            "src": {"kind": "text", "app": "Notes", "cap": T("Select two colors", "选中两个颜色"), "sub": T("The text color first, then the background.", "前一个是文字颜色，后一个是背景。"),
                    "lines": [T("# Design review", "# 设计走查"), T("Caption text: [[#8E8E93 on #FFFFFF]]", "说明文字：[[#8E8E93 和 #FFFFFF]]"),
                              T("Buttons: #FFFFFF on #007AFF", "按钮：#FFFFFF 和 #007AFF")]},
            "card": {"w": 330, "body": [
                {"t": "swatches", "items": [["#8E8E93", ""], ["#FFFFFF", ""]]},
                {"t": "rows", "rows": [[T("Contrast", "对比度"), "3.26 : 1"], [T("Normal text", "普通文字"), T("AA Fail · AAA Fail", "AA 不通过 · AAA 不通过"), "warn"],
                                                      [T("Large text", "大号文字"), T("AA Pass · AAA Fail", "AA 通过 · AAA 不通过")]]},
                {"t": "note", "text": T("The first is the text color, the second the background; large text means 18pt or larger, or bold 14pt or larger",
                                        "前一个当文字颜色，后一个当背景；大号文字指 18pt 以上，或 14pt 以上的粗体")}]},
            "steps": [
                {"cap": T("3.26 : 1 fails for body text", "3.26 : 1，正文不通过"), "acts": [["wait", 300], ["addClass", "row:1.1", "is-hl"]], "hold": 1500},
                {"cap": T("Large text passes AA", "大号文字能过 AA"), "acts": [["hover", "row:1.2"], ["addClass", "row:1.2", "is-hl"]], "hold": 1400},
                {"cap": T("Click a color to copy it", "点颜色复制色值"), "acts": [["click", "[data-b='0'] .pl-sw", ["toast", COPIED]]]},
            ],
        },
    },
}
