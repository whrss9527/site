"""Plugin pages: developer plugins. See __init__.py and the README ("Plugin pages")."""
import html
import re

from . import T

# ---------------------------------------------------------------- Code Screenshot
# The picture CodeImage.render draws: Pop's dark editor theme (CodeImage.Theme) in a window with
# three dots, on the "sky" gradient (AnnotationBackground.sky). Colours are fixed: it is an image.
_CI_COLORS = {"k": "#cc8cff", "s": "#99de8a", "n": "#ffb373", "c": "#808799", "t": "#fad980"}
_CI_KEYWORDS = {"func", "let", "var", "if", "else", "for", "while", "return", "struct", "class", "enum", "import",
                "true", "false", "nil", "self", "guard", "in", "switch", "case", "default"}
_CI_TOKEN = re.compile(r'(//[^\n]*)|("(?:\\.|[^"\\\n])*")|\b(\d[\d_]*(?:\.\d+)?)\b|\b([A-Za-z_][A-Za-z0-9_]*)\b')


def _ci_tint(code):
    """Code as HTML, tinted the way CodeImage.tokens does: comments and strings first, then numbers,
    keywords and capitalised type names."""
    out, at = [], 0
    for m in _CI_TOKEN.finditer(code):
        kind = "c" if m.group(1) else "s" if m.group(2) else "n" if m.group(3) else None
        if m.group(4):
            word = m.group(4)
            kind = "k" if word in _CI_KEYWORDS else "t" if word[0].isupper() else None
        if not kind:
            continue
        out.append(html.escape(code[at:m.start()]))
        out.append(f'<span style="color:{_CI_COLORS[kind]}">{html.escape(m.group(0))}</span>')
        at = m.end()
    out.append(html.escape(code[at:]))
    return "".join(out)


def _code_image(code):
    dots = "".join(f'<span style="width:8px;height:8px;border-radius:50%;background:{c}"></span>'
                   for c in ("#ff5e57", "#ffbd2e", "#29c940"))
    return ('<div style="position:absolute;inset:0;display:flex;align-items:center;justify-content:center;'
            'background:linear-gradient(135deg,#599eff,#8c5cf5)">'
            '<div style="border-radius:8px;background:#1f1f29;box-shadow:0 7px 20px rgba(0,0,0,0.4);padding:8px 14px 12px">'
            f'<div style="display:flex;gap:6px;margin-bottom:16px">{dots}</div>'
            f'<div style="font:9.5px/1.55 var(--pl-mono);color:#dee0eb;white-space:pre;text-align:left">{_ci_tint(code)}</div>'
            '</div></div>')


CODE_EN = '''// Say hi based on the time of day
func greet(at hour: Int) -> String {
    if hour < 12 {
        return "Good morning, \\(name)!"
    }
    return "Hello, \\(name)!"
}'''
CODE_ZH = '''// 按时间打招呼
func greet(at hour: Int) -> String {
    if hour < 12 {
        return "早上好，\\(name)！"
    }
    return "你好，\\(name)！"
}'''

# ---------------------------------------------------------------- sample data
# A JWT whose payload really decodes to the card (issued 15:14, expires 17:14 on the stage's Wednesday,
# in Los Angeles for the English page and in Shanghai for the Chinese one).
JWT_EN = ("eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ1c2VyXzEwMjQiLCJpc3MiOiJodHRwczovL2F1dGguZXhhbXBsZS5jb20iLCJhdWQiOiJhcGku"
          "ZXhhbXBsZS5jb20iLCJpYXQiOjE3OTA4MDY0NDAsImV4cCI6MTc5MDgxMzY0MH0.WgMDuxkC49fBaKX9odtvjxjWK3AFPGyYMXbgr7-qp04")
JWT_ZH = ("eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ1c2VyXzEwMjQiLCJpc3MiOiJodHRwczovL2F1dGguZXhhbXBsZS5jb20iLCJhdWQiOiJhcGku"
          "ZXhhbXBsZS5jb20iLCJpYXQiOjE3OTA3NTI0NDAsImV4cCI6MTc5MDc1OTY0MH0.hNcSF2gCbkpD87QRZBq1yp-3SXCj2QCcT5KHU1hGRag")


def _jwt_payload(iat, exp):
    # JSONSerialization, pretty-printed with sorted keys and unescaped slashes
    return ('{\n  "aud" : "api.example.com",\n  "exp" : %d,\n  "iat" : %d,\n'
            '  "iss" : "https://auth.example.com",\n  "sub" : "user_1024"\n}' % (exp, iat))


# The start of a 640 × 400 JPEG in Base64 (its SOF0 marker says 400 × 640).
JPEG_B64 = ("/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAgGBgcGBQgHBwcJCQgKDBQNDAsLDBkSEw8UHRofHh0aHBwgJC4nICIsIxwcKDcpLDAxNDQ0Hyc5PTgy"
            "PC4zNDL/2wBDAQkJCQwLDBgNDRgyIRwhMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjL/wAARCAGQAoADASIA"
            "AhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwQFBQQEAAABfQECAwAEEQUSITFBBhNRYQcicRQygZGh")

ZWSP = "\u200b"

# Regex Tester: Pop's own demo (RegexTesterEntry.didLoad): dates in release notes, replaced with $3/$2/$1.
REGEX = "(\\d{4})-(\\d{2})-(\\d{2})"
REGEX_EN = ["0.10.0 shipped on 2026-09-29.", "0.9.0 shipped on 2026-09-28.", "Next version due before 2026-10-08."]
REGEX_ZH = ["0.10.0 发布于 2026-09-29。", "0.9.0 发布于 2026-09-28。", "下一版计划在 2026-10-08 之前发布。"]


def _regex_text(lines, how=""):
    text = "\n".join(lines)
    if how == "mark":
        return re.sub(REGEX, r"==\g<0>==", text)
    if how == "replace":
        return re.sub(REGEX, r"\3/\2/\1", text)
    return text


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
    "hash": {
        "chips": ["MD5 · SHA-1", "SHA-256 · SHA-512", T("Text or files", "文字或文件")],
        "points": [
            T("Select some text or a file and get its <b>MD5, SHA-1, SHA-256 and SHA-512</b> at once; copy any of them.",
              "选中文字或文件，一次算出 <b>MD5、SHA-1、SHA-256、SHA-512</b>，哪一个都能单独复制。"),
            T("Text is hashed as UTF-8. Files are read in chunks, so big downloads and disk images are fine.",
              "文字按 UTF-8 计算；文件分块读取，很大的安装包、磁盘映像也没问题。"),
            T("Select several files to get the <b>SHA-256 of each one</b>, up to 20 at a time.",
              "选中好几个文件时，列出<b>每个文件的 SHA-256</b>，一次最多 20 个。"),
            T("Folders can’t be hashed: select the files inside.", "文件夹没法计算哈希，要选里面的文件。"),
        ],
        "scene": {
            "src": {"kind": "files", "cap": T("Select a file in Finder", "在访达里选中一个文件"), "sub": T("Or select some text.", "选中一段文字也行。"),
                    "files": [{"name": "Setup-2.4.dmg", "sel": True}, {"name": "Photos.zip", "kind": "zip"}, {"name": "Report.pdf"},
                              {"name": "IMG_2041.HEIC", "kind": "photo", "art": "sunset"}, {"name": T("notes.txt", "笔记.txt")}]},
            "card": {"w": 400, "title": "Setup-2.4.dmg",
                     "body": [{"t": "rows", "rows": [
                         ["MD5", "618346a5878350030e152fd9570730b0"],
                         ["SHA-1", "1f3c278985ecfe1e293f472fa0c8697966125c22"],
                         ["SHA-256", "81993c8ecf54f3c5f9b116f84192fba1e20d729229978ae24a73c6e40f25e029"],
                         ["SHA-512", "0ca5f6ebd6ec44970229618d2edd3b5b80442da81f8d7b2e0ca30f4ceeb25ba4d8a36700d26a4d83889a9f14489651de0a899890105fd721c28d69fac33ad237"],
                     ]}]},
            "steps": [
                {"cap": T("Four hashes at once", "四种哈希一次算好"), "sub": T("Big files are read bit by bit.", "大文件分块读，不占内存。"), "acts": [["wait", 600]]},
                {"cap": T("Copy the one you need", "复制要用的那一个"), "sub": T("Compare it with the checksum on the download page.", "和下载页上写的校验值对一对。"),
                 "acts": [["click", '.pl-card .pl-row[data-i="2"] .pl-ib', ["toast", T("Copied", "已复制")]]]},
            ],
        },
    },
    "base64Image": {
        "chips": ["data:image/…", "PNG · JPEG · WebP · GIF", T("Copy, save or pin", "复制、保存、贴到屏幕")],
        "points": [
            T("Select Base64 image data, with or without a <code>data:image/…;base64,</code> prefix, and Pop <b>shows it as a picture</b>.",
              "选中一串 Base64 图片数据，带不带 <code>data:image/…;base64,</code> 开头都行，Pop 直接<b>显示成图片</b>。"),
            T("It tells PNG, JPEG, GIF, WebP, HEIC and more apart from the data itself, and lists the format, dimensions and size.",
              "按数据本身认出 PNG、JPEG、GIF、WebP、HEIC 这些格式，列出格式、尺寸和大小。"),
            T("Line breaks and URL-safe Base64 are fine.", "中间有换行、用的是 URL 安全的 Base64 也没关系。"),
            T("Copy the image, <b>save it to Downloads</b> or pin it on the screen.", "图片可以复制、<b>存到「下载」</b>，或者贴到屏幕上。"),
        ],
        "scene": {
            "src": {"kind": "text", "app": "Xcode", "title": "listing.json", "mono": True, "cap": T("Select the Base64 data", "选中 Base64 数据"),
                    "lines": ["{", '  "id": 1024,', T('  "title": "Hillside cabin",', '  "title": "山坡小屋",'), '  "photo": "[[' + JPEG_B64 + ']]"', "}"]},
            "slot": 1,
            "card": {"w": 340, "btns": [T("Copy Image", "复制图片"), T("Save to Downloads", "存到「下载」"), T("Pin to Screen", "贴到屏幕")],
                     "body": [{"t": "img", "art": "landscape", "ar": "16/10"},
                              {"t": "rows", "rows": [[T("Format", "格式"), "JPEG"], [T("Dimensions", "尺寸"), "640 × 400"], [T("Size", "大小"), "48 KB"]]}]},
            "steps": [
                {"cap": T("The data becomes a picture", "一串字符变回图片"), "sub": T("With its format, dimensions and size.", "还列出格式、尺寸和大小。"), "acts": [["wait", 700]]},
                {"cap": T("Save it to Downloads", "存到「下载」"), "sub": T("Or copy it, or pin it on the screen.", "也可以复制，或者贴到屏幕上。"),
                 "acts": [["click", "btn:1", ["toast", T("Saved to Downloads", "已存到「下载」")]]]},
            ],
        },
    },
    "random": {
        "chips": ["UUID", T("Passwords", "密码"), T("6 digits", "6 位数字")],
        "points": [
            T("Nothing to select: you get a <b>UUID</b> in capitals and in lowercase, two passwords and a 6-digit number.",
              "什么都不用选：给出大写和小写的 <b>UUID</b>、两种密码和一个 6 位数字。"),
            T("One password is 16 characters with symbols, the other 20 without. Each has lowercase letters, capitals and digits, and none of the easily confused l, I, O, 0 and 1.",
              "一种密码 16 位、带符号，一种 20 位、不带符号；大写、小写、数字都有，不用 l、I、O、0、1 这些容易看错的字符。"),
            T("Copy a value, or <b>paste it straight into the field</b> you’re typing in.", "每一项都能复制，也能<b>直接粘贴到正在输入的地方</b>。"),
            T("The values are new every time.", "每次用都重新生成。"),
        ],
        "scene": {
            "src": {"kind": "desk", "app": "Safari", "title": T("Create account", "注册账号"),
                    "lines": [T("Email: ada@example.com", "邮箱：xiaolin@example.com"), T("Password: {{[[▏]]}}", "密码：{{[[▏]]}}"), T("Invite code:", "邀请码：")]},
            "slot": 7,
            "card": {"w": 380, "body": [{"t": "rows", "rows": [
                ["UUID", "3F2B8C71-9D4E-4A6B-B0C5-7E1D2F9A4C83"],
                [T("UUID lowercase", "UUID 小写"), "3f2b8c71-9d4e-4a6b-b0c5-7e1d2f9a4c83"],
                [T("Password", "密码"), "pK7#vR2m-Tx9!qWe"],
                [T("Password without symbols", "密码 无符号"), "h4TzR8kWm3PqX7vN2cYd"],
                [T("6 digits", "6 位数字"), "482917"],
            ]}]},
            "steps": [
                {"cap": T("Fresh values every time", "每次都是新的"), "acts": [["wait", 800]]},
                {"cap": T("Copy the password", "复制密码"), "sub": T("Each value has its own copy button.", "每一项都能单独复制。"),
                 "acts": [["click", '.pl-card .pl-row[data-i="2"] .pl-ib', [["close"], ["toast", T("Copied", "已复制")]]]]},
                {"cap": T("Paste it into the field", "粘贴到输入框里"), "sub": T("The ↩ beside a value pastes it there directly.", "点一项旁边的 ↩ 也能直接粘贴过去。"),
                 "acts": [["click", ".pl-tgt"], ["key", "⌘V", ["replace", "pK7#vR2m-Tx9!qWe"]]]},
            ],
        },
    },
    "linkInspect": {
        "chips": [T("Decoded parameters", "参数解码"), T("Without utm_source", "去掉 utm_source"), T("Expand short links", "展开短链接")],
        "points": [
            T("Select a link to see its <b>scheme, host, path and every parameter</b>, with the values decoded.",
              "选中一个链接，列出<b>协议、主机、路径和每个参数</b>，参数值已经解码。"),
            T("Tracking parameters such as utm_source, fbclid and spm are removed: <b>copy the clean link</b> or replace the original with it. The other parameters keep their encoding.",
              "utm_source、fbclid、spm 这类跟踪参数会去掉，<b>干净的链接</b>可以复制，也可以直接替换原文；留下的参数保持原来的编码。"),
            T("Some are only removed where they track, such as si on YouTube and Spotify links.", "有些参数只在特定网站上才去掉，比如 YouTube、Spotify 链接里的 si。"),
            T("For short links such as bit.ly or t.cn, <b>Expand Short Link</b> follows each redirect to where it ends up. Only then does Pop go online.",
              "t.cn、bit.ly 这类短链接多一个「<b>展开短链接</b>」，一跳一跳跟过去，看最后到了哪个网址；只有点了它才会联网。"),
        ],
        "scene": {
            "src": {"kind": "text", "app": T("Mail", "邮件"), "title": T("This week’s picks", "本周精选"), "cap": T("Select a link", "选中一个链接"),
                    "lines": [T("# Back in stock", "# 又到货了"), T("Our most popular desk lamp is here again:", "最受欢迎的那款台灯又到货了："),
                              T("[[https://shop.example.com/search?q=desk%20lamp&utm_source=newsletter&utm_medium=email]]",
                                "[[https://shop.example.com/search?q=%E5%8F%B0%E7%81%AF&spm=a2141.7631564&utm_source=newsletter]]")]},
            "slot": 3,
            "card": {"w": 380, "btns": [T("Replace", "替换原文"), T("Copy Clean Link", "复制干净的链接")], "tint": 0,
                     "body": [{"t": "text", "hide": True, "mono": True, "text": T("https://shop.example.com/search?q=desk%20lamp", "https://shop.example.com/search?q=%E5%8F%B0%E7%81%AF")},
                              {"t": "rows", "rows": [
                                  [T("Scheme", "协议"), "https"], [T("Host", "主机"), "shop.example.com"], [T("Path", "路径"), "/search"],
                                  ["q", T("desk lamp", "台灯")],
                                  T(["utm_source", "newsletter"], ["spm", "a2141.7631564"]),
                                  T(["utm_medium", "email"], ["utm_source", "newsletter"]),
                              ]},
                              {"t": "note", "hide": True, "text": T("Above is the link without tracking parameters; you can replace the original with it",
                                                      "上面是去掉跟踪参数后的链接，可以直接替换原文")}]},
            "steps": [
                {"cap": T("Every part, decoded", "每一部分都拆开了"), "sub": T("desk%20lamp reads “desk lamp”.", "%E5%8F%B0%E7%81%AF 变回「台灯」。"),
                 "acts": [["move", "row:1.3"], ["wait", 700]]},
                {"cap": T("The clean link, without tracking", "去掉跟踪参数的干净链接"),
                 "acts": [["show", 0, 150], ["show", 2], ["move", "b:0", 0.75, 0.5], ["wait", 900]]},
                {"cap": T("Replace the original", "替换原文"), "sub": T("Or copy the clean link.", "也可以复制干净的链接。"),
                 "acts": [["click", "btn:0", ["replace", T("https://shop.example.com/search?q=desk%20lamp", "https://shop.example.com/search?q=%E5%8F%B0%E7%81%AF")]]]},
            ],
        },
    },
    "jwtDecode": {
        "chips": [T("Expiry at a glance", "过期时间一眼看到"), T("Local dates", "换成本地时间"), T("Decode only", "只解码")],
        "points": [
            T("Select a JWT to list its <b>algorithm, issuer, subject and audience</b>, and when it was issued, starts and expires, as local dates.",
              "选中一个 JWT，列出<b>算法、签发者、主题、受众</b>，签发时间、生效时间、过期时间都换成本地时间。"),
            T("The expiry says whether the token has <b>already expired</b>, or when it will.", "过期时间后面标着<b>是否已经过期</b>，没过期的写着还有多久。"),
            T("The decoded payload is shown in full and neatly formatted. Copy it, or copy the header.", "完整显示解码后的内容，排好了版，可以复制，也可以复制头部。"),
            T("It only decodes: the signature isn’t verified.", "只解码，不验证签名。"),
        ],
        "scene": {
            "tall": True,
            "src": {"kind": "text", "app": T("Terminal", "终端"), "title": "zsh", "mono": True, "raw": True, "cap": T("Select a JWT", "选中一个 JWT"),
                    "lines": [T("# Which account is this token for?", "# 这个令牌是哪个账号的？"), "$ curl https://api.example.com/v1/me \\",
                              T('    -H "Authorization: Bearer [[' + JWT_EN + ']]"', '    -H "Authorization: Bearer [[' + JWT_ZH + ']]"')]},
            "slot": 1,
            "card": {"w": 420, "title": "JWT", "btns": [T("Copy", "复制"), T("Copy Header", "复制头部")],
                     "body": [{"t": "text", "mono": True, "text": T(_jwt_payload(1790806440, 1790813640), _jwt_payload(1790752440, 1790759640))},
                              {"t": "rows", "rows": [
                                  [T("Algorithm", "算法"), "HS256"], [T("Issuer", "签发者"), "https://auth.example.com"],
                                  [T("Subject", "主题"), "user_1024"], [T("Audience", "受众"), "api.example.com"],
                                  [T("Issued at", "签发时间"), "2026-09-30 15:14:00"],
                                  [T("Expires", "过期时间"), T("2026-09-30 17:14:00 (expires in 1 hour)", "2026-09-30 17:14:00（1小时后过期）")],
                              ]},
                              {"t": "note", "text": T("Decoded only; the signature wasn’t verified", "只是解码，没有验证签名")}]},
            "steps": [
                {"cap": T("The claims, decoded", "声明都解出来了"), "acts": [["wait", 600]]},
                {"cap": T("See when it expires", "看看什么时候过期"), "sub": T("In local time, with how long it has left.", "换成本地时间，还标着还有多久。"),
                 "acts": [["move", "row:1.5", 0.55, 0.5], ["wait", 1000]]},
                {"cap": T("Copy the payload", "复制解码后的内容"), "acts": [["click", "btn:0", ["toast", T("Copied", "已复制")]]]},
            ],
        },
    },
    "regexTest": {
        "chips": [T("Live highlighting", "边输入边标出"), T("Groups by name", "分组和命名分组"), "$3/$2/$1"],
        "points": [
            T("Select some text and type a regular expression: matches are <b>highlighted as you type</b>, and each one is listed with its groups (named groups by name).",
              "选中一段文字，输入正则表达式，<b>边输入边标出</b>每处匹配，逐条列出匹配到的文字和每个分组（命名分组显示名字）。"),
            T("Turn on Ignore case, ^ $ match each line or . matches newlines. Presets has ready-made expressions for numbers, email addresses, URLs, IP addresses, dates, blank lines and more.",
              "可以打开「忽略大小写」「^ $ 匹配每一行」「. 也匹配换行」；「常用」里有数字、中文、邮箱、手机号、网址、IP 地址、日期、空行这些现成的表达式。"),
            T("Type a replacement ($1 for the first group) to see the <b>replaced text</b> right away, then copy it or replace the original.",
              "填上替换内容（$1 引用第一个分组），马上看到<b>替换后的全文</b>，可以复制，也可以直接替换原文。"),
            T("An expression that would take forever stops after 1.5 seconds, so nothing hangs.", "写出回溯很慢的表达式时，匹配到 1.5 秒会自己停下，不会卡住。"),
        ],
        "scene": {
            "tall": True,
            "src": {"kind": "text", "app": T("Notes", "备忘录"),
                    "lines": [T("# Release notes", "# 发布记录"), T("[[" + REGEX_EN[0], "[[" + REGEX_ZH[0]), T(REGEX_EN[1], REGEX_ZH[1]),
                              T(REGEX_EN[2] + "]]", REGEX_ZH[2] + "]]")]},
            "card": {"w": 420, "btns": [T("Copy All Matches", "复制所有匹配"), T("Copy Expression", "复制表达式")],
                     "body": [{"t": "field", "mono": True, "ph": T("Regular expression, e.g. \\d+", "正则表达式，比如 \\d+")},
                              {"t": "chips", "items": [T("Ignore case", "忽略大小写"), T("^ $ match each line", "^ $ 匹配每一行"), T(". matches newlines", ". 也匹配换行")], "on": [1]},
                              {"t": "text", "mono": True, "text": T(_regex_text(REGEX_EN), _regex_text(REGEX_ZH))},
                              {"t": "list", "hide": True, "dense": True, "items": [
                                  {"icon": str(i), "title": "%s-%s-%s · $1 = %s · $2 = %s · $3 = %s" % (y, m, d, y, m, d)}
                                  for i, (y, m, d) in enumerate([("2026", "09", "29"), ("2026", "09", "28"), ("2026", "10", "08")], 1)]},
                              {"t": "field", "ph": T("Replace with ($1 is the first group, $0 the whole match)", "替换为（$1 是第一个分组，$0 是整个匹配）")},
                              {"t": "text", "hide": True, "mono": True, "text": T(_regex_text(REGEX_EN, "replace"), _regex_text(REGEX_ZH, "replace"))}]},
            "steps": [
                {"cap": T("Type a pattern", "输入正则表达式"), "sub": T("Every match lights up, with its groups.", "每处匹配都标出来，还列出分组。"),
                 "acts": [["type", 0, REGEX, 55], ["set", 2, {"t": "text", "mono": True, "text": T(_regex_text(REGEX_EN, "mark"), _regex_text(REGEX_ZH, "mark"))}],
                          ["show", 3]]},
                {"cap": T("Try a replacement", "试试替换"), "sub": T("$1 is the first group, $3 the third.", "$1 是第一个分组，$3 是第三个。"),
                 "acts": [["set", 0, {"t": "field", "mono": True, "value": REGEX}], ["type", 4, "$3/$2/$1", 110], ["show", 5]]},
                {"cap": T("Copy all the matches", "复制所有匹配"), "acts": [["click", "btn:0", ["toast", T("Copied", "已复制")]]]},
            ],
        },
    },
    "cron": {
        "chips": ["*/15 9-17 * * 1-5", T("Next 5 runs", "接下来 5 次"), "@daily · @weekly"],
        "points": [
            T("Select a cron expression and Pop <b>says it in words</b>: <code>0 2 * * 0</code> is “every Sunday at 02:00”.",
              "选中 cron 表达式，Pop <b>把它说成中文</b>：<code>0 2 * * 0</code> 就是「每周日 02:00」。"),
            T("It lists the <b>next five runs</b> in your Mac’s time zone, or tells you it won’t run in the next five years.",
              "列出<b>接下来 5 次</b>运行的时间（按本机时区）；五年内都不会运行的也会告诉你。"),
            T("Ranges, lists and steps, JAN–DEC and SUN–SAT, and shortcuts such as @daily, @weekly and @hourly are all understood.",
              "认得范围、列表、步长，JAN–DEC、SUN–SAT 这些缩写，还有 @daily、@weekly、@hourly 这类写法。"),
            T("When both the day and the weekday are set, it runs when either matches, as cron does.", "「日」和「周」都写了时，满足其中一个就运行，和 cron 的规矩一样。"),
        ],
        "scene": {
            "src": {"kind": "text", "app": T("Terminal", "终端"), "title": "crontab", "mono": True, "raw": True, "cap": T("Select a cron expression", "选中一个 cron 表达式"),
                    "lines": [T("# Sync orders during office hours", "# 上班时间同步订单"), "[[*/15 9-17 * * 1-5]] ~/bin/sync-orders", "",
                              T("# Back up every Sunday at 2 am", "# 每周日凌晨 2 点备份"), "0 2 * * 0 ~/bin/backup"]},
            "slot": 3,
            "card": {"w": 360, "btns": [T("Copy", "复制")],
                     "body": [{"t": "text", "type": True, "text": T("every weekday (Monday to Friday) every 15 minutes during hours 9–17", "每个工作日（周一到周五） 9 点到 17 点每 15 分钟")},
                              {"t": "rows", "hide": True, "rows": [[T("Run %d" % i, "第 %d 次" % i), T("2026-09-30 %s Wed" % t, "2026-09-30 %s 周三" % t)]
                                                                    for i, t in enumerate(["16:15", "16:30", "16:45", "17:00", "17:15"], 1)]},
                              {"t": "note", "hide": True, "text": T("Next runs (local time zone America/Los_Angeles)", "接下来几次（本机时区 Asia/Shanghai）")}]},
            "steps": [
                {"cap": T("In plain words", "说成了中文"), "acts": [["wait", 1400]]},
                {"cap": T("The next five runs", "接下来 5 次运行"), "sub": T("In your Mac’s time zone.", "按本机时区。"), "acts": [["show", 1, 100], ["show", 2]]},
                {"cap": T("Copy the description", "复制这句说明"), "acts": [["click", "btn:0", ["toast", T("Copied", "已复制")]]]},
            ],
        },
    },
    "codeImage": {
        "chips": [T("Syntax colors", "语法着色"), T("Gradient background", "渐变背景"), T("Indent trimmed", "去掉多余缩进")],
        "points": [
            T("Select some code and Pop <b>draws it as a picture</b>: a dark editor window with syntax colors, on a gradient background with a soft shadow.",
              "选中一段代码，Pop 把它<b>画成一张图片</b>：深色编辑器窗口、语法着色，外面是带阴影的渐变背景。"),
            T("Keywords, strings, numbers, comments and type names each get a color, in most common languages.", "关键字、字符串、数字、注释和类型名各有颜色，常见的语言都认得。"),
            T("Extra indentation is removed and tabs become four spaces, so a snippet from deep inside a file still looks tidy.",
              "自动去掉多余的缩进，Tab 换成 4 个空格，从文件深处选的一段也整整齐齐。"),
            T("<b>Copy the image</b>, save it to Downloads or pin it on the screen, or drag the preview into another app.",
              "可以<b>复制图片</b>、存到「下载」、贴到屏幕上，也可以按住预览图拖到别的 App 里。"),
        ],
        "scene": {
            "src": {"kind": "text", "app": "Xcode", "title": "Greeter.swift", "mono": True, "cap": T("Select some code", "选中一段代码"),
                    "lines": ["struct Greeter {", "    let name: String", "",
                              T("    [[// Say hi based on the time of day", "    [[// 按时间打招呼"),
                              "    func greet(at hour: Int) -> String {", "        if hour < 12 {",
                              T('            return "Good morning, \\(name)!"', '            return "早上好，\\(name)！"'), "        }",
                              T('        return "Hello, \\(name)!"', '        return "你好，\\(name)！"'), "    }]]", "}"]},
            "slot": 1,
            "card": {"w": 360, "btns": [T("Copy Image", "复制图片"), T("Save", "存储"), T("Pin to Screen", "贴到屏幕")], "tint": 0,
                     "body": [{"t": "img", "art": "landscape", "ar": "3/2", "over": T(_code_image(CODE_EN), _code_image(CODE_ZH))},
                              {"t": "note", "text": T("You can also drag the preview into another app", "按住拖动预览图也能拖到别的 App 里")}]},
            "steps": [
                {"cap": T("Your code, as a picture", "代码变成了一张图"), "sub": T("Colored, on a gradient, without the extra indent.", "带语法着色和渐变背景，多余的缩进去掉了。"),
                 "acts": [["wait", 900]]},
                {"cap": T("Copy the image", "复制图片"), "sub": T("Paste it into a chat, a post or slides.", "贴到聊天、文章、幻灯片里。"),
                 "acts": [["click", "btn:0", ["toast", T("Image copied", "已复制图片")]]]},
                {"cap": T("Or save it to Downloads", "或者存到「下载」"), "acts": [["click", "btn:1", ["toast", T("Saved to Downloads", "已存到「下载」")]]]},
            ],
        },
    },
    "charInfo": {
        "chips": ["U+200B", "UTF-8 · UTF-16", T("Invisible characters", "看不见的字符")],
        "points": [
            T("Select a few characters to see each one’s <b>Unicode code point, name and UTF-8 bytes</b>, plus UTF-16 for emoji. Emoji with a skin tone are split into their parts.",
              "选中几个字符，看每个字符的 <b>Unicode 码点、名称和 UTF-8 编码</b>，表情还有 UTF-16；带肤色的表情会拆开列出。"),
            T("It finds <b>invisible characters</b> such as zero-width spaces, no-break spaces, BOMs and bidirectional controls, which often come along when you copy from web pages and chats.",
              "能找出零宽空格、不换行空格、BOM、双向控制符这类<b>看不见的字符</b>，从网页、聊天软件复制的文字里常有。"),
            T("Remove them and replace the original, or copy the cleaned text; no-break spaces become ordinary spaces.",
              "可以去掉后替换原文，也可以去掉后复制；不换行空格换成普通空格。"),
            T("Up to 20 characters are listed one by one; in longer text it just looks for invisible ones.", "20 个字以内逐个列出，更长的文字只检查看不见的字符。"),
        ],
        "scene": {
            "src": {"kind": "text", "app": T("Messages", "信息"), "cap": T("Select a few characters", "选中几个字符"),
                    "lines": [T("Ben: Lunch tomorrow at 12?", "老陈：明天中午一起吃饭？"), T("Ada: [[OK" + ZWSP * 2 + "👍🏽]]", "小林：[[好的" + ZWSP * 2 + "👍🏽]]")]},
            "card": {"w": 400, "btns": [T("Copy Code Points", "复制码点"), T("Remove and Replace", "去掉后替换原文"), T("Remove and Copy", "去掉后复制")], "tint": 1,
                     "body": [{"t": "rows", "rows": [
                         T(["O", "U+004F · LATIN CAPITAL LETTER O\nUTF-8 4F"], ["好", "U+597D · CJK UNIFIED IDEOGRAPH-597D\nUTF-8 E5 A5 BD"]),
                         T(["K", "U+004B · LATIN CAPITAL LETTER K\nUTF-8 4B"], ["的", "U+7684 · CJK UNIFIED IDEOGRAPH-7684\nUTF-8 E7 9A 84"]),
                         [T("Zero-width space", "零宽空格"), T("U+200B · Zero-width space\nUTF-8 E2 80 8B", "U+200B · 零宽空格\nUTF-8 E2 80 8B")],
                         ["👍🏽", "U+1F44D U+1F3FD · THUMBS UP SIGN + EMOJI MODIFIER FITZPATRICK TYPE-4\nUTF-8 F0 9F 91 8D F0 9F 8F BD · UTF-16 D83D DC4D D83C DFFD"]]},
                              {"t": "note", "text": T("2 invisible characters: Zero-width space ×2", "有 2 个看不见的字符：零宽空格 ×2")}]},
            "steps": [
                {"cap": T("Code point, name and bytes", "码点、名称、编码"), "sub": T("The emoji is split into its parts.", "带肤色的表情拆开列出。"), "acts": [["wait", 700]]},
                {"cap": T("Something invisible is hiding", "藏着看不见的字符"), "sub": T("Two zero-width spaces.", "两个零宽空格。"),
                 "acts": [["move", "row:0.2", 0.4, 0.5], ["text", '.pl-card .pl-row[data-i="2"] .pl-row-l', T("Zero-width space", "零宽空格")],
                          ["text", '.pl-card [data-b="1"] p', T("2 invisible characters: Zero-width space ×2", "有 2 个看不见的字符：零宽空格 ×2")], ["wait", 1000]]},
                {"cap": T("Remove them and replace", "去掉后替换原文"), "sub": T("Or copy the cleaned text.", "也可以去掉后复制。"),
                 "acts": [["click", "btn:1", ["replace", T("OK👍🏽", "好的👍🏽")]]]},
            ],
        },
    },
}
