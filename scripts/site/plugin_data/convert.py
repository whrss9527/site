"""Plugin pages: convert plugins. See __init__.py and the README ("Plugin pages")."""
from . import T

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
}
