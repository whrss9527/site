from common import *

def shot(r, src, alt, w, h, cls="", cap=None):
    fc = f"<figcaption>{cap}</figcaption>" if cap else ""
    return f'<figure><div class="shot {cls}"><img src="{r}assets/img/{src}" alt="{alt}" width="{w}" height="{h}" loading="lazy" decoding="async"></div>{fc}</figure>'

def cut(r, src, alt, w, h, dark=None, width=None, cap=None, eager=False):
    style = f' style="width:{width}px"' if width else ""
    load = "" if eager else ' loading="lazy"'
    img = f'<img src="{r}assets/img/{src}" alt="{alt}" width="{w}" height="{h}"{load} decoding="async"{style}>'
    if dark:
        img = f'<picture><source srcset="{r}assets/img/{dark}" media="(prefers-color-scheme: dark)">{img}</picture>'
    fc = f"<figcaption>{cap}</figcaption>" if cap else ""
    return f'<figure class="cut">{img}{fc}</figure>'

def stox_demo(r, lang, preset, fallback, alt, w, h, desk=False):
    """The interactive Stox panel (assets/stox-demo.js, sample data), preset to one state.
    Without JavaScript the real screenshot `fallback` shows instead."""
    d = " data-desk" if desk else ""
    return (f'<figure class="sxd" data-lang="{lang}" data-preset="{preset}"{d} data-icon="{r}assets/icons/stox.png">'
            f'<noscript><img src="{r}assets/img/{fallback}" alt="{alt}" width="{w}" height="{h}" loading="lazy" decoding="async" style="width:300px"></noscript></figure>')

def meno_demo(r, lang, preset, fallback):
    """The interactive Meno demo (assets/meno-demo.js, sample items), preset to one state.
    Without JavaScript the CSS illustration `fallback` shows instead."""
    return (f'<figure class="mnd" data-lang="{lang}" data-preset="{preset}" data-icon="{r}assets/icons/meno.png">'
            f'<noscript>{fallback}</noscript></figure>')

MENO_HEAD = lambda r: f'\n<link rel="stylesheet" href="{r}assets/meno-demo.css">\n<script src="{r}assets/meno-demo.js" defer></script>'

STOX_HEAD = lambda r: f'\n<link rel="stylesheet" href="{r}assets/stox-demo.css">\n<script src="{r}assets/stox-demo.js" defer></script>'

def pop_demo(r, lang, preset, fallback, alt, w, h, desk=False):
    """The interactive Pop demo (assets/pop-demo.js, sample text): a document with Pop's ring
    and result cards, preset to one state. Without JavaScript the real screenshot `fallback` shows instead."""
    d = " data-desk" if desk else ""
    return (f'<figure class="ppd" data-lang="{lang}" data-preset="{preset}"{d} data-icon="{r}assets/icons/pop.png">'
            f'<noscript><img src="{r}assets/img/{fallback}" alt="{alt}" width="{w}" height="{h}" loading="lazy" decoding="async"></noscript></figure>')

POP_HEAD = lambda r: f'\n<link rel="stylesheet" href="{r}assets/pop-demo.css">\n<script src="{r}assets/pop-demo.js" defer></script>'

def proxi_demo(r, lang, preset, fallback, alt, w, h, width=520):
    """The interactive Proxi panel and settings window (assets/proxi-demo.js, sample data),
    preset to one state. Without JavaScript the real screenshot `fallback` shows instead."""
    return (f'<figure class="pxd" data-lang="{lang}" data-preset="{preset}">'
            f'<noscript><img src="{r}assets/img/{fallback}" alt="{alt}" width="{w}" height="{h}" loading="lazy" decoding="async" style="width:{width}px"></noscript></figure>')

PROXI_HEAD = lambda r: f'\n<link rel="stylesheet" href="{r}assets/proxi-demo.css">\n<script src="{r}assets/proxi-demo.js" defer></script>'

def feature(title, body, bullets, media, media_cls=""):
    lis = "".join(f"<li>{b}</li>" for b in bullets)
    ul = f"<ul>{lis}</ul>" if bullets else ""
    return f"""
      <div class="feature">
        <div class="feature-text">
          <h2>{title}</h2>
          <p>{body}</p>
          {ul}
        </div>
        <div class="feature-media {media_cls}">{media}</div>
      </div>"""

def tiles(items):
    return "".join(f'<div class="tile glass"><h3>{a}</h3><p>{b}</p></div>' for a, b in items)

def faq(items):
    out = []
    for q, a in items:
        paras = "".join(f"<p>{p}</p>" for p in (a if isinstance(a, list) else [a]))
        out.append(f'<details class="glass"><summary>{q}</summary><div class="answer">{paras}</div></details>')
    return "".join(out)

def siblings(c, key):
    out = []
    for k, a in APPS.items():
        if k == key:
            continue
        pitch = a["zh"] if c.zh else a["pitch"]
        out.append(f'<a class="sibling glass" href="{c.link(k + "/")}"><img src="{c.r}assets/icons/{k}.png" alt="" width="44" height="44"><div><strong>{a["name"]}</strong><span>{pitch}</span></div></a>')
    return "".join(out)

def build(key, d, lang="en"):
    c = Ctx(f"/{key}/", lang)
    t = c.t
    r = c.r
    a = APPS[key]
    extra = d["extra_head"](r) if "extra_head" in d else ""
    h = head(c, d["title"], d["desc"], body_class=f"app-{key}", extra_head=extra)
    h += header(c, key)
    meta = "".join(f"<span>{m}</span>" for m in d["meta"])
    feats = "".join(feature(*f) if len(f) == 4 else feature(f[0], f[1], f[2], f[3], f[4]) for f in d["features"](r))
    specs = "".join(f"<dt>{k}</dt><dd>{v}</dd>" for k, v in d["specs"])
    steps = "".join(f"<li>{s}</li>" for s in d["install"])
    h += f"""<main id="main">
  <section class="app-hero">
    <div class="wrap">
      <img class="icon" src="{r}assets/icons/{key}.png" alt="{t(a['name'] + ' app icon', a['name'] + ' 应用图标')}" width="128" height="128">
      <h1>{a['name']}</h1>
      <p class="say">{d['say']}</p>
      <p class="lede">{d['lede']}</p>
      <div class="actions">
        <a class="btn btn-primary" href="{dl_url(key)}">{ICON_DL}{t('Download ' + a['name'], '下载 ' + a['name'])}</a>
        <a class="btn btn-glass" href="{repo_url(key)}">{ICON_GH}{t('View on GitHub', '在 GitHub 上查看')}</a>
      </div>
      <p class="meta">{meta}</p>
      <div class="stage">{d['stage'](r)}</div>
    </div>
  </section>

  <section class="section" aria-label="{t('Features', '功能')}">
    <div class="wrap">
      <div class="features">{feats}
      </div>
    </div>
  </section>

  <section class="section-tight" aria-labelledby="more-title">
    <div class="wrap">
      <div class="section-head"><h2 id="more-title">{d['more_title']}</h2></div>
      <div class="tiles">{tiles(d['tiles'])}</div>
    </div>
  </section>

  <section class="section-tight" aria-labelledby="req-title">
    <div class="wrap">
      <div class="info-grid">
        <div class="panel-block glass">
          <h2 id="req-title">{t("Requirements", "系统要求")}</h2>
          <dl class="specs">{specs}</dl>
        </div>
        <div class="panel-block glass">
          <h2>{t("Install and update", "安装与更新")}</h2>
          <ol class="steps">{steps}</ol>
          <p class="note">{d['update_note']}</p>
        </div>
      </div>
    </div>
  </section>

  <section class="section-tight" aria-labelledby="faq-title">
    <div class="wrap narrow">
      <div class="section-head"><h2 id="faq-title">{t("Questions", "常见问题")}</h2></div>
      <div class="faq">{faq(d['faq'])}</div>
      <p class="small muted" style="margin-top:24px">{t("More help", "更多帮助")}{t(": ", "：")}<a href="{repo_url(key)}/issues">{t(a['name'] + ' issues on GitHub', 'GitHub 上的 ' + a['name'] + ' issue')}</a> · <a href="{c.link('support/')}">{t("Support", "支持")}</a> · <a href="{c.link('privacy/' + key + '/')}">{t(a['name'] + ' privacy policy', a['name'] + ' 隐私政策')}</a></p>
    </div>
  </section>

  <section class="section-tight" aria-labelledby="sib-title">
    <div class="wrap">
      <div class="section-head"><h2 id="sib-title">{t("Also in the menu bar", "菜单栏里的其他应用")}</h2></div>
      <div class="siblings">{siblings(c, key)}</div>
    </div>
  </section>
</main>
"""
    h += footer(c)
    write(c.out_file, h)


# ---------------------------------------------------------------- Pop
POP = {
    "title": "Pop · Long-press right click, swipe, done",
    "desc": "Pop is a right-click toolbox for the Mac menu bar: long-press the right mouse button to translate a selection or open a ring of 80+ tools. Free and open source.",
    "say": "/pɒp/ — like a bubble: it pops up, you swipe, it pops.",
    "lede": "Hold the right mouse button on anything you’ve selected. Pop translates it, converts it, or opens a ring of tools you pick with one swipe. A short click is still the normal context menu.",
    "meta": ["Free and open source", "macOS 15 or later", "Apple silicon and Intel", "In English and Simplified Chinese"],
    "extra_head": POP_HEAD,
    "stage": lambda r: '<div class="compose pop-stage">' +
        pop_demo(r, "en", "ring", "pop/unit.webp", "Pop’s unit conversion card showing 5 km in centimeters, meters, inches, feet, miles, nautical miles and Chinese units", 325, 249, desk=True) +
        cut(r, "pop/ring.webp", "Real screenshot of Pop’s ring, in Chinese, with Dictionary highlighted", 214, 214, dark="pop/ring-dark.webp", cap="Real screenshot · Chinese interface") +
        "</div>",
    "features": lambda r: [
        ("A right click, held a moment",
         "Press and hold the right button for about a quarter of a second (you can change it) and Pop reads what’s selected in the app you’re using. Release early and you get the system menu as usual; drag with the right button and games or 3D apps get the drag.",
         ["Swipe toward a slot and let go to run it; let go in the middle to close",
          "Or use a modifier + right click, the middle button, or a global shortcut",
          "Optional toolbar above a selection, off by default and excludable per app"],
         '<div class="illus-wrap">' + '''<div class="illus gesture" role="img" aria-label="Illustration: what happens after you press the right mouse button. Released within 0.25 seconds: the usual context menu. Dragged more than 6 pixels: the drag goes to the app. Held for 0.25 seconds: Pop reads the selection.">
  <div class="head"><span>Right button down</span><span>0.25 s</span></div>
  <div class="step"><div class="bar"><i style="width:34%"></i><b></b></div><div><strong>Released early</strong><span>The usual context menu</span></div></div>
  <div class="step"><div class="bar"><i style="width:48%"></i><b></b></div><div><strong>Dragged 6 px or more</strong><span>The drag goes to the app — games, 3D tools</span></div></div>
  <div class="step sel"><div class="bar"><i style="width:100%"></i><b></b></div><div><strong>Held</strong><span>Pop reads the selection: a translation, a result, or the ring</span></div></div>
</div>''' + '<p class="illus-cap">How Pop tells a long press from a normal click. The delay is adjustable.</p></div>'),
        ("Translate what you select",
         "Foreign text goes straight to a translation card. By default it uses Apple’s on-device translation — offline and free. Switch to AI or DeepL, or show them side by side.",
         ["Replace the original text in place, or copy it",
          "Change the target language for one card, or read it aloud",
          "Save words to a vocabulary list and export it for Anki"],
         pop_demo(r, "en", "translate", "pop/translate.webp", "Pop’s translation card comparing the System, AI and DeepL translations of a sentence, with Copy and Replace for each", 325, 297)),
        ("More than 80 tools, where you want them",
         "Arrange 4 to 12 slots, give an app its own ring, and set rules that skip the ring entirely: math is calculated, units and colors are converted, images are read with on-device OCR.",
         ["Text: cleanup, case, encoding, word count, extract links and emails",
          "Developer: JSON, YAML, SQL, regex, JWT, hashes, QR codes, cron",
          "Files and screen: rename, convert images and video, PDF, color picker, ruler"],
         pop_demo(r, "en", "unit", "pop/regex.webp", "Pop’s regex tester card highlighting matched dates and named groups", 442, 274)),
        ("Clipboard history, and pins on top",
         "Pop keeps a searchable history of text, images and files — text inside images is searchable too, recognized on your Mac. Pin a screenshot, image or text above every window to compare against.",
         ["⌘1–⌘9 to paste, ⌘-click several items to paste them together",
          "Skips content that password managers mark as concealed; exclude any app",
          "Stored only on this Mac and cleaned up by age and count"],
         pop_demo(r, "en", "history", "pop/history.webp", "Pop’s clipboard history panel with search, type filters and recent items, two of them selected", 392, 414)),
        ("AI with your own endpoint",
         "Select text and ask AI to polish, summarize, explain or translate it, or ask a question. On macOS 26 with Apple Intelligence, Pop can use the built-in on-device model. Or point it at any OpenAI Chat Completions–compatible endpoint, including a model running on your Mac.",
         ["Answers stream in; copy, replace the original or pin them",
          "Selected text is only sent when you use an AI feature",
          "Your API key stays in this Mac’s Keychain"],
         pop_demo(r, "en", "ai", "pop/ai.webp", "Pop’s AI card with Polish, Summarize, Explain and Translate buttons, a question field and an answer", 358, 210)),
        ("Plugins in one JSON file",
         "Turn a URL template, a shell script, JavaScript or a Shortcut into a tool on the ring. Or install one from the plugin library — Pop checks its SHA-256 before adding it, and shows you shell scripts before they’re installed.",
         ["<code>pop://</code> links and Shortcuts actions let other tools call Pop",
          "Import and export plugins, or share the JSON file"],
         shot(r, "pop/library.jpg", "Pop Settings showing the plugin library with installable plugins", 640, 481, "light")),
    ],
    "more_title": "Also inside",
    "tiles": [
        ("Screenshot OCR and translate", "Draw a box on screen to read or translate the text in it, offline."),
        ("Annotate", "Arrows, boxes, text, pixelation and numbered steps, with an optional backdrop and shadow."),
        ("Color picker and ruler", "Pick any on-screen color and measure distances between elements."),
        ("Send to phone", "Open a temporary page on your phone over the same Wi-Fi to move files both ways."),
        ("Window layout", "Halves, thirds, maximize, center, or move to another display."),
        ("Keep awake and timer", "Stop the Mac from sleeping for a while, or set a quick countdown."),
    ],
    "specs": [
        ("macOS", "15 Sequoia or later; Liquid Glass on macOS 26"),
        ("Mac", "Universal: Apple silicon and Intel"),
        ("Permissions", "Accessibility (required). Screen Recording only for screenshot tools."),
        ("Language", "English or Simplified Chinese interface, following your Mac’s language (0.30.0 and later); translation works across many languages"),
        ("Download", "About 6 MB (<code>Pop-&lt;version&gt;.zip</code>)"),
        ("License", "GPL-3.0"),
    ],
    "install": [
        "Download <code>Pop-&lt;version&gt;.zip</code> from the latest release and unzip it.",
        "Drag <strong>Pop.app</strong> into Applications and double-click it. From 0.22.0 on, releases are signed with a Developer ID and notarized by Apple.",
        "Turn on Pop in System Settings › Privacy &amp; Security › Accessibility. It takes effect within seconds.",
        "Select some English text and hold the right mouse button for about 0.25 seconds.",
    ],
    "update_note": "Pop checks GitHub Releases at launch and every 6 hours (you can turn this off, and opt out of betas). “Update Now” downloads the new version, verifies its SHA-256 checksum and code signature — it must be signed with the same certificate — then replaces Pop and relaunches. Settings, plugins and history are kept.",
    "faq": [
        ("Is it free?", "Yes. Pop is free and open source under GPL-3.0: no account, no subscription, no in-app purchases."),
        ("Why does it need Accessibility?", [
            "macOS only lets apps with Accessibility access watch mouse buttons system-wide, read the selection in other apps and paste into them. Pop needs exactly that: to notice a long right-click, read what you selected, and put results back when you choose “Replace”.",
            "For the same reason Pop can’t be in the Mac App Store — the sandbox doesn’t allow it — so it’s distributed on GitHub and here."]),
        ("Does it need Screen Recording?", "Only for the tools that look at the screen: screenshot OCR and translate, QR scanning, annotation and the ruler. Everything else works without it."),
        ("Is there an English interface?", "Yes. Since 0.30.0 Pop shows its interface in English unless your Mac’s language is Chinese. Translation itself works between many languages using Apple’s on-device translation, AI or DeepL."),
        ("Does Pop send my text anywhere?", f'Only when you ask for it: AI features send the selected text to the AI endpoint you set up, and DeepL translation sends it to DeepL. Apple’s on-device translation and model, OCR and the clipboard history stay on your Mac. See the <a href="../privacy/pop/">privacy policy</a>.'),
        ("Does it sync between Macs?", "You can export settings and plugins to a file in Settings › Sync and import them on another Mac. iCloud sync needs a build signed with iCloud access; the builds on GitHub don’t include it."),
        ("Right-click stopped working after an update.", "Open Pop’s Settings › General and use “Clear old authorization records”, then grant Accessibility again. This mostly affected older, ad-hoc–signed builds; notarized releases keep the permission."),
    ],
}

# ---------------------------------------------------------------- Meno
MENO_BAR = """<div class="illus screen" role="img" aria-label="Illustration: a menu bar where Meno keeps only three icons visible behind its chevron divider, and a glass Shelf hanging below it that shows the hidden items">
  <div class="mb">
    <span class="menus"><b>Finder</b><span>File</span><span>Edit</span><span>View</span><span>Go</span><span>Window</span><span>Help</span></span>
    <span class="right">
      <span class="div">‹</span>
      <span class="dot"></span><span class="dot c"></span><span class="dot"></span>
      <span class="time">Wed 9:41</span>
    </span>
  </div>
  <div class="shelf" aria-hidden="true"><span class="dot"></span><span class="dot c"></span><span class="dot"></span><span class="dot c"></span><span class="dot"></span><span class="dot"></span><span class="dot c"></span></div>
  <div class="legend"><span>‹ Meno’s divider: everything to its left is hidden</span><span>The Shelf shows hidden items right below the menu bar</span></div>
</div>"""

MENO_REVEAL = """<div class="illus" role="img" aria-label="Illustration: the same menu bar twice. First with only the chevron divider and three visible icons. Then revealed, with the hidden icons shown between the dividers; stashed icons stay out of the menu bar.">
  <p class="tag">Hidden</p>
  <div class="mb">
    <span class="menus"><b>Mail</b><span>File</span><span>Edit</span></span>
    <span class="right"><span class="div">‹</span><span class="dot"></span><span class="dot c"></span><span class="dot"></span><span class="time">9:41</span></span>
  </div>
  <p class="tag" style="margin-top:16px">Revealed</p>
  <div class="mb">
    <span class="menus"><b>Mail</b></span>
    <span class="right"><span class="div">»</span><span class="dot new"></span><span class="dot new c"></span><span class="dot new"></span><span class="dot new c"></span><span class="div">‹</span><span class="dot"></span><span class="dot c"></span><span class="dot"></span><span class="time">9:41</span></span>
  </div>
  <div class="legend"><span>» Stash — stays out of the menu bar</span><span>‹ Hidden — shown on demand</span><span>Visible — always there</span></div>
</div>"""

MENO_QUICK = """<div class="illus" role="img" aria-label="Illustration: Quick Open, a search palette listing menu bar items and actions that match the typed text">
  <div class="palette">
    <div class="q">wi<span class="caret"></span></div>
    <div class="row sel"><span class="dot"></span><span>Wi-Fi</span><small>↩ Open</small></div>
    <div class="row"><span class="dot c"></span><span>Wireless Diagnostics</span><small>⌘2</small></div>
    <div class="row"><span class="dot"></span><span>Scene: Work</span><small>⌘3</small></div>
  </div>
</div>"""

MENO_RULE = """<div class="illus" role="img" aria-label="Illustration: two rules. When a microphone is in use, turn on Zen and undo it afterwards. When an external display is connected, apply the scene Work.">
  <div class="palette">
    <div class="row"><span class="dot c"></span><span><strong>When</strong> a microphone is in use</span></div>
    <div class="row sel"><span class="dot"></span><span>Turn on Zen</span><small>undo afterwards</small><span class="sw" aria-hidden="true"></span></div>
    <div class="sep"></div>
    <div class="row"><span class="dot c"></span><span><strong>When</strong> an external display is connected</span></div>
    <div class="row sel"><span class="dot"></span><span>Apply scene “Work”</span><span class="sw" aria-hidden="true"></span></div>
  </div>
</div>"""

MENO_LANG = """<div class="illus" role="img" aria-label="Illustration: the Language setting in Meno’s General settings, with Follow System, English, Simplified Chinese and Traditional Chinese">
  <div class="palette">
    <div class="row sel"><span class="dot c"></span><span>Follow System</span><small>✓</small></div>
    <div class="row"><span class="dot"></span><span>English</span></div>
    <div class="row"><span class="dot"></span><span>简体中文</span></div>
    <div class="row"><span class="dot"></span><span>繁體中文</span></div>
  </div>
</div>"""

MENO = {
    "title": "Meno · A calm menu bar, made with glass",
    "desc": "Meno is a menu bar manager for macOS: hide and stash icons, bring them back with a click, hover, swipe or shortcut, with a Liquid Glass Shelf, Quick Open, rules, scenes and Zen mode.",
    "say": "/ˈmeː.no/ — Italian for “less”, one letter away from “menu”.",
    "lede": "Meno tucks away the menu bar icons you rarely need and brings them back with a click, a hover, a swipe or a shortcut.",
    "meta": ["Free and open source", "macOS 14 or later", "Apple silicon and Intel", "English, 简体中文, 繁體中文"],
    "extra_head": MENO_HEAD,
    "stage": lambda r: f'<div style="max-width:880px;margin:0 auto">{meno_demo(r, "en", "layout", MENO_BAR)}</div>',
    "features": lambda r: [
        ("Visible, Hidden, and a Stash",
         "Meno adds small dividers to your menu bar. Icons left of the single chevron are hidden until you ask; icons past the double chevron go in the Stash, for things you almost never need — they appear only in the Shelf, Quick Open or with ⌥-click.",
         ["Reveal with a click on Meno, a click or hover on empty menu bar, a scroll or swipe down, or a shortcut",
          "Re-hides after a delay, when you switch apps or when the pointer leaves",
          "When an app restarts and macOS moves its icon, Meno puts it back"],
         meno_demo(r, "en", "reveal", MENO_REVEAL)),
        ("Shelf and Quick Open",
         "The Shelf is a glass bar below the menu bar that shows hidden items — handy next to the camera housing, where the menu bar runs out of room. Quick Open is a Spotlight-style palette that finds any item from the keyboard, pinyin and initials included.",
         ["↩ opens, ⌘↩ opens the secondary menu, ⌘1–⌘9 pick a result",
          "Also runs Meno’s own actions: apply a scene, turn on Zen",
          "Liquid Glass on macOS 26; frosted glass on macOS 14 and 15"],
         meno_demo(r, "en", "shelf", MENO_QUICK)),
        ("A menu bar that reads the room",
         "Rules change the menu bar for you: when a microphone or camera is in use, a display is plugged in, you’re on battery, on a certain network, or at a certain time. Scenes save arrangements like Work, Home or Presenting.",
         ["Actions reveal or hide sections, apply a scene, turn on Zen or move one item",
          "Moves wait until you’re not using the mouse and keyboard",
          "Pause all rules from Meno’s menu or a shortcut"],
         meno_demo(r, "en", "rules", MENO_RULE)),
        ("In your language",
         "Meno speaks English, Simplified Chinese and Traditional Chinese. It follows the system language, or the one you choose in Settings › General › Language, and switches after a relaunch.",
         ["The setting is labelled in all three languages, so it’s easy to find",
          "Everything else in General: how items appear, when they hide again, the Stash and Zen"],
         meno_demo(r, "en", "general", MENO_LANG)),
    ],
    "more_title": "Small things that add up",
    "tiles": [
        ("Zen", "One shortcut clears every app icon and leaves only system status — for screenshots, recordings and talks."),
        ("Layout editor", "Drag items between Visible, Hidden and Stash. Rename them and give them a symbol."),
        ("Groups", "Put related items behind one icon; click it to show them in a Shelf right below."),
        ("Show when it changes", "A hidden item appears for a moment when its icon or text changes, like a failed sync."),
        ("Item shortcuts and links", "Open Wi-Fi, a VPN or a timer from anywhere. <code>meno://</code> links work in Shortcuts and scripts."),
        ("Insights, on device", "How often you reveal, your most used items, and suggestions to keep or stash — never leaves your Mac."),
    ],
    "specs": [
        ("macOS", "14 Sonoma or later; Liquid Glass on macOS 26"),
        ("Mac", "Universal: Apple silicon and Intel"),
        ("Permissions", "Accessibility (required). Screen Recording optional, for the real artwork of hidden items."),
        ("Language", "English, Simplified Chinese, Traditional Chinese"),
        ("Download", "About 5 MB (<code>Meno.zip</code>)"),
        ("License", "GPL-3.0"),
    ],
    "install": [
        "Download <code>Meno.zip</code> from the latest release and unzip it.",
        "Move <strong>Meno.app</strong> to Applications and double-click it. From 0.10.0 on, releases are signed with a Developer ID and notarized by Apple.",
        "Grant Accessibility when asked, then ⌘-drag icons across the dividers or use the Layout editor.",
    ],
    "update_note": "Check for updates in Settings › About, or turn on a daily check in General. “Install and Relaunch” downloads the release from GitHub, verifies its checksum, version and code signature, replaces Meno and opens it again.",
    "faq": [
        ("Is it free?", "Yes. Meno is free and open source under GPL-3.0, with no account and nothing to buy."),
        ("Why does it need Accessibility?", "Meno reads menu bar items through each app’s accessibility tree, opens them from the Shelf, Quick Open and shortcuts, and arranges them by performing ⌘-drags for you. macOS allows all three only with Accessibility access."),
        ("What is Screen Recording for?", "It’s optional. With it, the Shelf shows the real artwork of hidden items and Meno notices when their icons change (macOS 14–26). Only menu bar items are captured, and nothing is recorded or saved. Without it, Meno shows app icons."),
        ("Does Meno go online?", f'Only to ask GitHub for the latest release — when you check, or once a day if you turned that on — and to download a release you chose to install. No analytics, no accounts. See the <a href="../privacy/meno/">privacy policy</a>.'),
        ("An icon is missing on macOS 26.", "macOS only shows items of apps allowed in System Settings › Menu Bar. Meno’s own icon can also be turned off in Settings › Appearance; open Settings again from Quick Open or by opening Meno."),
        ("Meno doesn’t respond after an update.", "Open Settings › Permissions and click “Reset and Grant Again”. Releases from 0.10.0 on share one Developer ID certificate, so later updates keep the permission."),
        ("Does it work on macOS 27?", "Yes. macOS 27 changed how the menu bar handles wide items, so Meno uses a “stepped” hiding engine there; you can choose the engine in Settings › General › Advanced."),
    ],
}

# ---------------------------------------------------------------- Stox
STOX = {
    "title": "Stox · Menu bar stock quotes for A-shares, Hong Kong and US",
    "desc": "Stox shows China A-share, Hong Kong and US stock quotes in the Mac menu bar, with charts, holdings and P&L, alerts and iCloud sync. Right-click to hide it all. Free and open source.",
    "say": "/stɒks/ — “stocks”, squeezed into four letters.",
    "lede": "China A-share, Hong Kong and US quotes in your menu bar, with holdings and P&amp;L, alerts and iCloud sync. One right-click and only a quiet icon is left.",
    "meta": ["Free and open source", "macOS 13 or later", "Apple silicon and Intel", "In English and Simplified Chinese"],
    "extra_head": STOX_HEAD,
    "stage": lambda r: '<div class="compose stox-stage">' +
        stox_demo(r, "en", "detail", "stox/detail.webp", "Stox panel with a watchlist and an expanded intraday chart for Kweichow Moutai", 376, 645, desk=True) +
        cut(r, "stox/detail.webp", "Real screenshot of the Stox panel, in Chinese, with Kweichow Moutai expanded to its intraday chart", 376, 645, width=300, cap="Real screenshot · Chinese interface") +
        "</div>",
    "features": lambda r: [
        ("Glance, then hide",
         "Left-click the menu bar icon for a glass panel; click again, click elsewhere or press Esc to close it. Right-click switches the menu bar between showing quotes and showing only an icon — useful when someone is looking over your shoulder.",
         ["Pin chosen tickers to the menu bar, on one line or two, rotating on notched screens",
          "⌃⌥S opens the panel from any app; pin it as a floating window",
          "Red-up, green-up, or no red and green at all"],
         stox_demo(r, "en", "list", "stox/panel.webp", "Stox watchlist with a mini intraday chart on every row", 376, 583, desk=True)),
        ("Three markets, and then some",
         "Shanghai, Shenzhen and Beijing A-shares, Hong Kong and US stocks with pre- and after-hours prices, plus indexes, ETFs, mutual funds, international futures and forex.",
         ["Search by code, Chinese name or pinyin initials: <code>600519</code>, <code>gzmt</code>, <code>aapl</code>",
          "Paste several codes at once to add them together",
          "Quotes switch to a backup source automatically if the main one fails"],
         stox_demo(r, "en", "search", "stox/search.webp", "Stox search results showing prices and changes as you type", 376, 467)),
        ("Charts that answer the question",
         "Expand a row for intraday, five-day, daily, weekly and monthly charts with moving averages and volume. Hover for the exact price at any minute. A-shares add the order book and money flow.",
         ["Your cost line on the chart, and B and S marks for recorded trades",
          "Open, high, low, turnover, P/E, market cap, 52-week range",
          "An A-share gainers, losers and industry ranking"],
         stox_demo(r, "en", "kline", "stox/kline.webp", "Stox daily candlestick chart with moving averages and volume", 376, 645)),
        ("Holdings and P&amp;L",
         "Enter shares and cost, and Stox totals today’s and overall P&amp;L per currency, converted to yuan when you hold several. Log trades and dividends; a calendar shows every day’s result.",
         ["Weighted average cost updates as you buy; sells record realized gains",
          "Tap the eye to mask amounts in the panel, menu bar and notifications",
          "Optional closing summary notification"],
         stox_demo(r, "en", "holdings", "stox/holdings.webp", "Stox holdings view with per-currency totals and profit and loss", 376, 647)),
    ],
    "more_title": "Also inside",
    "tiles": [
        ("Alerts", "Price above or below, percentage moves, take-profit and stop-loss, limit up/down, 52-week highs and lows."),
        ("iCloud sync", "Watchlist, groups, holdings and alerts sync through your own iCloud Drive. Or export a backup file."),
        ("Quiet on battery", "Refreshes once a minute when markets are closed and stops while the Mac sleeps."),
        ("Groups and notes", "Group your watchlist and keep a one-line note on why you’re watching a stock."),
        ("Copy to spreadsheets", "Copy holdings, trades and P&amp;L as tables for Numbers or Excel."),
        ("Light", "About 30 MB of memory. No sign-up and no API key."),
    ],
    "specs": [
        ("macOS", "13 Ventura or later; Liquid Glass on macOS 26"),
        ("Mac", "Universal: Apple silicon and Intel"),
        ("Permissions", "None required. Notifications for alerts; iCloud Drive access only if you turn on sync."),
        ("Language", "English or Simplified Chinese, following your Mac’s language (0.47.0 and later)"),
        ("Data", "Tencent Finance public quotes, Sina Finance as backup. Hong Kong quotes are delayed about 15 minutes."),
        ("Download", "About 4 MB (<code>Stox.zip</code>)"),
        ("License", "GPL-3.0"),
    ],
    "install": [
        "Download <code>Stox.zip</code> from the latest release and unzip it.",
        "Drag <strong>Stox.app</strong> into Applications and double-click it. From 0.46.0 on, releases are signed with a Developer ID and notarized by Apple.",
        "Stox appears only in the menu bar: left-click for the panel, right-click to hide quotes. Settings and Quit are at the bottom of the panel.",
    ],
    "update_note": "Stox checks GitHub Releases at launch and every 6 hours (you can turn it off in About &amp; Updates). When there’s a new version, an Update button appears at the bottom of the panel; Stox verifies the SHA-256 checksum and signature, replaces itself and relaunches, keeping your watchlist and settings.",
    "faq": [
        ("Is it free?", "Yes. Stox is free and open source under GPL-3.0. Quotes come from free public sources, so there’s no sign-up and no API key. A Mac App Store edition is being prepared; the GitHub version stays free."),
        ("Does it need Accessibility?", "No. Stox doesn’t ask for Accessibility or Screen Recording. Its global shortcut uses the standard hot-key API, which needs no permission. It only asks to send notifications, for alerts, and to use iCloud Drive if you turn on sync."),
        ("Where do the quotes come from?", "From Tencent Finance’s public quote service, with Sina Finance as an automatic backup. Hong Kong quotes are delayed about 15 minutes. Data is for reference only and is not investment advice."),
        ("Where are my holdings stored?", f'On your Mac, and in your own iCloud Drive (<code>Stox/sync.json</code>) if you turn on sync. Nothing is sent to me. See the <a href="../privacy/stox/">privacy policy</a>.'),
        ("Can I use it in English?", "Yes. Since 0.47.0 Stox shows its interface in English unless your Mac’s language is Chinese. Names of Chinese stocks stay in Chinese, as the quote sources give them."),
    ],
}

# ---------------------------------------------------------------- Proxi
PROXI = {
    "title": "Proxi · One switch for every proxy on your Mac",
    "desc": "Proxi switches the system proxy, environment variables, git and npm together, with a built-in mihomo core for subscriptions, rules, LAN sharing and TUN mode. Free and open source for macOS.",
    "say": "/ˈprɒk.si/ — still “proxy”: the y becomes an i.",
    "lede": "One switch for the system proxy, your shell’s environment variables, git and npm — plus a built-in mihomo core for subscriptions and rules, LAN sharing, and TUN or gateway mode.",
    "meta": ["Free and open source", "macOS 14 or later", "Apple silicon and Intel", "Interface in Simplified Chinese"],
    "extra_head": PROXI_HEAD,
    "stage": lambda r: '<div class="compose proxi-stage">' +
        proxi_demo(r, "en", "panel", "proxi/panel.webp", "Proxi menu bar panel with the proxy switch, the node list with latencies and the proxy profiles", 384, 722, width=300) +
        cut(r, "proxi/panel.webp", "Real screenshot of the Proxi menu bar panel, in Chinese: the proxy switch, nodes with latencies and three profiles", 384, 722, width=300, cap="Real screenshot · Chinese interface") +
        "</div>",
    "features": lambda r: [
        ("One switch, everywhere",
         "Make a profile — HTTP, SOCKS5 or PAC — and choose where it applies: the system proxy, environment variables for new terminals and apps, git and npm. Switch profiles with one click, or with ⌃⌥P.",
         ["Notices when another app changes the proxy, and can save it as a profile",
          "Finds proxy apps already running on your Mac and adds them",
          "Upload and download speed right in the menu bar"],
         proxi_demo(r, "en", "profiles", "proxi/hero.jpg", "Proxi settings window with proxy profiles, next to the menu bar panel listing nodes with latency", 1600, 1000)),
        ("Subscriptions and rules, built in",
         "Paste a subscription URL and its nodes appear in the panel. Pick one, let Proxi choose the fastest, and route by rules. The engine is mihomo (Clash Meta), bundled inside the app.",
         ["Policy groups: manual, auto-select, fallback and load balance",
          "Rule library with blackmatrix7, MetaCubeX, ACL4SSR and Shadowrocket rule sets",
          "Import Clash, mihomo, Surge, Shadowrocket and Quantumult X configs, with preview and undo"],
         proxi_demo(r, "en", "nodes", "proxi/nodes.jpg", "Proxi Nodes and Subscriptions page with two subscriptions and node settings", 820, 770)),
        ("The whole Mac, and your console too",
         "Enhanced mode routes every app — terminals and games included — through the core via a virtual network interface. LAN sharing and gateway mode let a PS5, Switch or phone use the same connection as your Mac.",
         ["LAN sharing on port 7892, limited to local network addresses by default",
          "Gateway mode for devices that can’t set a proxy, including game UDP traffic",
          "A small privileged helper, installed once with your password, only for these modes"],
         proxi_demo(r, "en", "share", "proxi/lan.jpg", "Proxi LAN Sharing page showing the address to enter on a PS5 or Switch", 820, 770)),
        ("Scripts, AI assistants and sync",
         "A <code>proxi</code> command-line tool, an MCP server for AI assistants and <code>proxi://</code> URL commands share one local control interface with four permission levels. Settings sync between Macs through your own iCloud Drive.",
         ["Switch profiles automatically by Wi-Fi network or router",
          "Imports and automatic switches are recorded in an activity log; imports can be undone"],
         proxi_demo(r, "en", "sync", "proxi/icloud.jpg", "Proxi iCloud Sync page", 820, 770)),
    ],
    "more_title": "When something doesn’t connect",
    "tiles": [
        ("Connections", "Every connection through the core: which app or device, which rule, which node, how much traffic."),
        ("Service check", "See whether ChatGPT, Claude, Gemini, Netflix, YouTube Premium or Telegram work through a node, and in which region."),
        ("URL diagnosis", "Enter a site that won’t open; Proxi walks DNS, direct and proxied paths and suggests a fix."),
        ("Exit IP", "The address and region websites see through your node, and your Mac’s own public address."),
        ("Advanced DNS", "Encrypted DNS in the core, per-domain servers, hosts, and mihomo config patches checked before saving."),
        ("Health checks", "Periodically checks the proxy port while it’s on and tells you when it stops answering."),
    ],
    "specs": [
        ("macOS", "14 Sonoma or later; Liquid Glass on macOS 26"),
        ("Mac", "Universal: Apple silicon and Intel (single-architecture builds also available)"),
        ("Permissions", "Administrator password to change the system proxy. Privileged helper only for Enhanced and gateway modes. No Accessibility."),
        ("Language", "Simplified Chinese interface"),
        ("Download", "About 53 MB universal (<code>Proxi-macos.zip</code>), about half for <code>-arm64</code> or <code>-x86_64</code>"),
        ("License", "GPL-3.0; bundles mihomo (GPL-3.0)"),
    ],
    "install": [
        "Download <code>Proxi-macos.zip</code> from the latest release and unzip it.",
        "Drag <strong>Proxi.app</strong> into Applications and double-click it. From 0.11.1 on, releases are signed with a Developer ID and notarized by Apple.",
        "Click the menu bar icon, add a profile or a subscription, and flip the switch.",
    ],
    "update_note": "Proxi checks GitHub Releases at launch and every 6 hours (you can turn it off). “Update” downloads the build for your chip, compares its SHA-256, replaces Proxi and relaunches. Signed releases only install updates signed by the same developer. Proxi used to be called ProxySwitch; updating from it moves your settings over automatically.",
    "faq": [
        ("Is it free?", "Yes. Proxi is free and open source under GPL-3.0. It doesn’t sell or provide proxy servers — you bring your own proxy or subscription."),
        ("Does it need Accessibility?", "No. The global shortcut uses the standard hot-key API. What Proxi does need: an administrator password to change the system proxy, and — only if you use Enhanced or gateway mode — a privileged helper installed once, because a virtual network interface and IP forwarding require root."),
        ("What is mihomo?", "mihomo (Clash Meta) is an open-source proxy core, also GPL-3.0. Proxi bundles it as a separate program inside the app and runs it only when you use the built-in node proxy, LAN sharing or Enhanced mode."),
        ("Is LAN sharing safe?", "By default only devices on private LAN ranges (10.x, 172.16–31.x, 192.168.x) may connect, and you can limit it to specific IPs. Turn it off on public Wi-Fi."),
        ("Why does it ask for Location?", "Only for switching by Wi-Fi network: since macOS 14, reading the Wi-Fi name requires Location permission. Proxi doesn’t read or store your location, and you can switch by router instead."),
        ("Is there a Windows version?", f'Yes, <a href="{GH}/proxyswitch">ProxySwitch</a> for Windows. The two evolve separately.'),
    ],
}

def build_all():
    from apps_zh import ZH
    for key, d in (("pop", POP), ("meno", MENO), ("stox", STOX), ("proxi", PROXI)):
        build(key, d, "en")
        build(key, ZH[key], "zh")


if __name__ == "__main__":
    build_all()
