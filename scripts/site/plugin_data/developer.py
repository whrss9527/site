"""Plugin pages: developer plugins. See __init__.py and the README ("Plugin pages")."""
from . import T

DATA = {
    "qrCode": {
        "chips": [T("Text → QR code", "文字 → 二维码"), "Code 128", T("Read codes in images", "识别图片里的码")],
        "points": [
            T("Select text or a link and get a <b>QR code</b> right away, ready to copy as an image.",
              "选中文字或链接，马上生成<b>二维码</b>，可以复制成图片。"),
            T("Letters and digits, such as an order number, can also become a <b>Code 128 barcode</b>.",
              "订单号这类英文字母和数字，还能生成 <b>Code 128 条形码</b>。"),
            T("Select an image or an image file instead and Pop <b>reads the QR codes and barcodes</b> in it.",
              "选中的是图片或图片文件时，Pop 会<b>识别里面的二维码和条形码</b>。"),
            T("Everything happens on your Mac; nothing is uploaded.", "全部在本机完成，不上传任何东西。"),
        ],
        "scene": {
            "src": {"kind": "text", "app": "Notes", "cap": T("Select a link", "选中一个链接"),
                    "lines": [T("# Share the release", "# 分享新版本"),
                              T("Download page: [[https://github.com/whrss9527/pop/releases]]", "下载地址：[[https://github.com/whrss9527/pop/releases]]"),
                              T("Order number: POP-2026-1002", "订单号：POP-2026-1002")]},
            "card": {"w": 300, "sub": T("41 characters", "41 个字符"), "btns": [T("Copy Image", "复制图片"), T("Barcode", "条形码")],
                     "body": [{"t": "panes", "panes": [[{"t": "qr", "text": "https://github.com/whrss9527/pop/releases"}],
                                                        [{"t": "barcode", "text": "POP-2026-1002"}]]}]},
            "steps": [
                {"cap": T("The QR code is ready", "二维码生成好了"), "sub": T("Copy it as an image and paste it anywhere.", "复制成图片，贴到哪儿都行。"),
                 "acts": [["click", "btn:0", ["toast", T("Copied", "已复制")]]]},
                {"cap": T("Letters and digits make a barcode too", "字母和数字还能生成条形码"),
                 "acts": [["click", "btn:1", ["swap", 0, 1]], ["wait", 600]]},
            ],
        },
    },
    "jsonTypes": {
        "chips": ["TypeScript", "Swift", "Go · Kotlin"],
        "points": [
            T("Select a JSON object or array and get <b>type definitions</b> for TypeScript, Swift, Go and Kotlin.",
              "选中一段 JSON 对象或数组，生成 TypeScript、Swift、Go、Kotlin 的<b>类型定义</b>。"),
            T("Nested objects become their own types; arrays, numbers, booleans and nulls get the right types.",
              "嵌套的对象单独成一个类型；数组、数字、布尔值和 null 都用对应的类型。"),
            T("Switch languages on the card and copy the code.", "在卡片上切换语言，一键复制代码。"),
        ],
        "scene": {
            "src": {"kind": "text", "app": "Xcode", "title": "user.json", "mono": True, "cap": T("Select some JSON", "选中一段 JSON"),
                    "lines": ['[[{', '  "id": 1024,', '  "name": "Ada",', '  "tags": ["admin"],', '  "active": true', '}]]']},
            "card": {"w": 360, "sub": "JSON", "btns": [T("Copy", "复制")],
                     "body": [{"t": "seg", "items": ["TypeScript", "Swift", "Go", "Kotlin"], "on": 0, "ctl": 1},
                              {"t": "panes", "panes": [
                                  [{"t": "code", "lang": "ts", "text": "interface Root {\n  id: number;\n  name: string;\n  tags: string[];\n  active: boolean;\n}"}],
                                  [{"t": "code", "lang": "swift", "text": "struct Root: Codable {\n  let id: Int\n  let name: String\n  let tags: [String]\n  let active: Bool\n}"}],
                                  [{"t": "code", "lang": "go", "text": "type Root struct {\n  ID     int      `json:\"id\"`\n  Name   string   `json:\"name\"`\n  Tags   []string `json:\"tags\"`\n  Active bool     `json:\"active\"`\n}"}],
                                  [{"t": "code", "lang": "kt", "text": "data class Root(\n  val id: Int,\n  val name: String,\n  val tags: List<String>,\n  val active: Boolean\n)"}],
                              ]}]},
            "steps": [
                {"cap": T("Types for TypeScript appear", "生成 TypeScript 类型"), "acts": []},
                {"cap": T("Switch to Swift or Go", "换成 Swift 或 Go"), "acts": [["click", "opt:0.1"], ["wait", 900], ["click", "opt:0.2"]]},
                {"cap": T("Copy the code", "复制代码"), "acts": [["click", "btn:0", ["toast", T("Copied", "已复制")]]]},
            ],
        },
    },
}
