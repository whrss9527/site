/* whrss.com: Pop's plugins — the filter on the plugin gallery, and the animated how-to on each plugin's page.

   The how-to is a recreation of Pop on a pretend Mac, played like a short film: select something,
   hold the right mouse button, swipe to the plugin on Pop's ring, and see what it does. Everything
   is sample data and canned results; nothing is fetched and nothing is sent anywhere. The ring and
   cards follow the Pop sources (RingMenuView, RingGeometry, Cards.swift, Motion, Glass), as the
   interactive demo in pop-demo.js does.

   Markup (written by scripts/site/pop_plugin_pages.py):
     <div class="howto">
       <ol class="pla-steps"><li>…</li>…</ol>               one item per chapter, captions in the page's language
       <figure class="pla" data-lang="en|zh" data-icon="…/pop.png">
         <script type="application/json" class="pla-data">{"name", "glyph", "scene"}</script>
       </figure>
     </div>
   The scene format is described in the README ("Plugin pages"). Chapters: 0 select, 1 hold the right
   button, 2 swipe on the ring, then one per scene step. With reduced motion nothing plays by itself:
   the figure shows a chapter's end state, and the steps pick which. */
(function () {
  "use strict";
  var D = document;
  var mqReduce = window.matchMedia ? window.matchMedia("(prefers-reduced-motion: reduce)") : { matches: false };
  var STOP = { stop: 1 };

  // ------------------------------------------------------------------ helpers
  function esc(s) {
    return String(s == null ? "" : s).replace(/[&<>"']/g, function (c) { return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]; });
  }
  function fmt(s) {
    var a = Array.prototype.slice.call(arguments, 1), i = 0;
    return String(s).replace(/%s/g, function () { return a[i++]; });
  }
  function el(tag, cls, html) {
    var e = D.createElement(tag);
    if (cls) e.className = cls;
    if (html != null) e.innerHTML = html;
    return e;
  }
  function svg(body, sw) {
    return '<svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="' + (sw || 1.7) +
      '" stroke-linecap="round" stroke-linejoin="round">' + body + "</svg>";
  }
  function clamp(v, lo, hi) { return Math.max(lo, Math.min(hi, v)); }
  function ease(p) { return p < 0.5 ? 4 * p * p * p : 1 - Math.pow(-2 * p + 2, 3) / 2; }
  function easeOut(p) { return 1 - Math.pow(1 - p, 3); }
  function lerp(a, b, p) { return a + (b - a) * p; }
  function each(list, fn) { Array.prototype.forEach.call(list, fn); }
  // Inline marks in sample text: [[selected]], {{target}}, **bold**, `code`, {+inserted+}, {-deleted-}, ==highlight==
  function marks(t, raw) {
    var h = esc(t)
      .replace(/\[\[([\s\S]+?)\]\]/g, '<span class="pl-sel">$1</span>')
      .replace(/\{\{([\s\S]+?)\}\}/g, '<span class="pl-tgt">$1</span>');
    if (raw) return h;
    return h.replace(/\*\*([^*]+)\*\*/g, "<b>$1</b>")
      .replace(/`([^`]+)`/g, "<code>$1</code>")
      .replace(/\{\+([\s\S]+?)\+\}/g, "<ins>$1</ins>")
      .replace(/\{-([\s\S]+?)-\}/g, "<del>$1</del>")
      .replace(/==([^=]+)==/g, "<mark>$1</mark>");
  }

  // A selection or target that runs over several lines is closed and reopened on each line.
  function spanLines(lines) {
    var open = { "[[": false, "{{": false }, close = { "[[": "]]", "{{": "}}" };
    return lines.map(function (l) {
      ["[[", "{{"].forEach(function (o) {
        var c = close[o];
        if (open[o]) l = o + l;
        var a = l.lastIndexOf(o), b = l.lastIndexOf(c);
        open[o] = a >= 0 && a > b;
        if (open[o]) l = l + c;
      });
      // An empty line inside a selection stays empty.
      return l === "[[]]" || l === "{{}}" ? "" : l;
    });
  }

  // ------------------------------------------------------------------ strings
  var S = {
    en: {
      tag: "Animated demo · sample data", play: "Play", pause: "Pause", label: "Animated demo: how to use %s in Pop",
      chars: "%s characters", items: "%s items", item: "1 item", image: "Image", images: "%s images", nothing: "Nothing selected",
      link: "Link", folder: "Folder", file: "File", app: "App",
      slots: ["Translate", "Search", "Dictionary", "Open Link", "All Actions", "Clipboard", "Screenshot OCR", "Pick Color"],
      menus: ["File", "Edit", "View", "Window"], clock: "Wed 4:14 PM", finder: "Finder",
      side: ["Recents", "Desktop", "Documents", "Downloads"], fav: "Favorites", search: "Search actions",
      copied: "Copied", close: "Close", rec: "Recording", stop: "Stop", paused: "Paused",
      region: "Drag to select an area", locked: "Keyboard locked", endClean: "End Cleaning",
      telehint: "Space pauses · ↑↓ change speed · Esc closes"
    },
    zh: {
      tag: "动画演示 · 示例数据", play: "播放", pause: "暂停", label: "动画演示：在 Pop 里怎么用%s",
      chars: "%s 字", items: "%s 项", item: "1 项", image: "图片", images: "%s 张图片", nothing: "未选中内容",
      link: "链接", folder: "文件夹", file: "文件", app: "App",
      slots: ["翻译", "搜索", "词典", "打开链接", "全部功能", "剪贴板", "截图识字", "屏幕取色"],
      menus: ["文件", "编辑", "显示", "窗口"], clock: "周三 16:14", finder: "访达",
      side: ["最近使用", "桌面", "文稿", "下载"], fav: "个人收藏", search: "搜索功能",
      copied: "已复制", close: "关闭", rec: "正在录制", stop: "停止", paused: "已暂停",
      region: "拖动选择一块区域", locked: "键盘已锁住", endClean: "结束清洁",
      telehint: "空格暂停 · ↑↓ 调速度 · Esc 关闭"
    }
  };

  // Icons for the ring's other slots (Pop's built-in actions) and a few controls.
  var I = {
    translate: svg('<path d="M5.5 3.8h13a2.3 2.3 0 0 1 2.3 2.3v8.6a2.3 2.3 0 0 1-2.3 2.3H13l-4.2 3.4v-3.4H5.5a2.3 2.3 0 0 1-2.3-2.3V6.1a2.3 2.3 0 0 1 2.3-2.3Z"/><path d="m9.2 13.6 2.8-6.6 2.8 6.6M10.2 11.4h3.6"/>'),
    search: svg('<circle cx="10.3" cy="10.3" r="6.3"/><path d="m15 15 5.3 5.3" stroke-width="2.1"/>'),
    dictionary: svg('<path d="M6.6 3h11.6c.6 0 1 .4 1 1v16.2c0 .5-.4.8-.8.8H6.8A2.6 2.6 0 0 1 4.2 18.4V5.4A2.4 2.4 0 0 1 6.6 3Z"/><path d="M4.2 18.4a2.5 2.5 0 0 1 2.5-2.4h12.5"/><path d="m9.4 12.6 2.6-6.1 2.6 6.1M10.3 10.6h3.4"/>'),
    openLink: svg('<circle cx="12" cy="12" r="8.6"/><path d="m15.6 8.4-2.1 5.1-5.1 2.1 2.1-5.1Z"/>'),
    allActions: svg('<rect x="3.8" y="3.8" width="6.8" height="6.8" rx="1.6"/><rect x="13.4" y="3.8" width="6.8" height="6.8" rx="1.6"/><rect x="3.8" y="13.4" width="6.8" height="6.8" rx="1.6"/><rect x="13.4" y="13.4" width="6.8" height="6.8" rx="1.6"/>'),
    clipboard: svg('<path d="M8.6 4.6H7a2 2 0 0 0-2 2V19a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2V6.6a2 2 0 0 0-2-2h-1.6"/><rect x="8.6" y="3" width="6.8" height="3.4" rx="1.2"/><path d="M8.6 10.6h.1M11 10.6h4.4M8.6 13.8h.1M11 13.8h4.4M8.6 17h.1M11 17h4.4"/>'),
    screenshotOCR: svg('<path d="M3.8 8.6V6.2a2.4 2.4 0 0 1 2.4-2.4h2.4M15.4 3.8h2.4a2.4 2.4 0 0 1 2.4 2.4v2.4M20.2 15.4v2.4a2.4 2.4 0 0 1-2.4 2.4h-2.4M8.6 20.2H6.2a2.4 2.4 0 0 1-2.4-2.4v-2.4"/>'),
    pickColor: svg('<path d="m13.3 6.4 4.3 4.3"/><path d="M15.6 4.1 17 2.7a2.1 2.1 0 0 1 3 3l-1.4 1.4-1.3 1.3-4.3-4.3Z" fill="currentColor"/><path d="m14.4 7.5-8.8 8.8-.9 3.1-1.2 1.2M16.5 9.6l-8.8 8.8-3 .9"/>'),
    close: '<svg viewBox="0 0 16 16" aria-hidden="true"><circle cx="8" cy="8" r="7" fill="currentColor"/><path d="m5.6 5.6 4.8 4.8m0-4.8-4.8 4.8" stroke="var(--pl-xmark)" stroke-width="1.5" stroke-linecap="round"/></svg>',
    copy: svg('<rect x="8.4" y="8.4" width="11.2" height="12.4" rx="2"/><path d="M15.6 8.4V5.6a2 2 0 0 0-2-2H6.4a2 2 0 0 0-2 2v8.8a2 2 0 0 0 2 2h2"/>'),
    check: svg('<path d="m5 12.5 4.5 4.5L19 7.5" stroke-width="2.4"/>'),
    play: '<svg viewBox="0 0 16 16" aria-hidden="true"><path d="M4.5 2.8v10.4L13 8Z" fill="currentColor"/></svg>',
    pause: '<svg viewBox="0 0 16 16" aria-hidden="true"><rect x="3.6" y="2.8" width="3" height="10.4" rx="1" fill="currentColor"/><rect x="9.4" y="2.8" width="3" height="10.4" rx="1" fill="currentColor"/></svg>',
    chevL: svg('<path d="m14.5 6-6 6 6 6"/>', 2),
    chevR: svg('<path d="m9.5 6 6 6-6 6"/>', 2),
    star: svg('<path d="m12 3.6 2.6 5.3 5.8.8-4.2 4.1 1 5.8-5.2-2.7-5.2 2.7 1-5.8-4.2-4.1 5.8-.8Z"/>'),
    cup: svg('<path d="M4.6 9.4h12.2v4.4a6.1 6.1 0 0 1-12.2 0Z"/><path d="M16.8 10.6h1.4a2.4 2.4 0 0 1 0 4.8h-1.8"/>', 2),
    headphones: svg('<path d="M3.6 15v-3a8.4 8.4 0 0 1 16.8 0v3"/><rect x="3.6" y="13.6" width="4.2" height="7" rx="1.6"/><rect x="16.2" y="13.6" width="4.2" height="7" rx="1.6"/>', 2),
    recdot: '<svg viewBox="0 0 16 16" aria-hidden="true"><rect x="3" y="3" width="10" height="10" rx="2.2" fill="currentColor"/></svg>',
    timer: svg('<circle cx="12" cy="13.4" r="7.8"/><path d="M12 13.4V9.2M9.6 2.8h4.8"/>', 2),
    mic: svg('<rect x="8.6" y="2.8" width="6.8" height="11.6" rx="3.4"/><path d="M5.4 11a6.6 6.6 0 0 0 13.2 0M12 17.6v3.6"/>', 2),
    pen: svg('<path d="m15.6 4.6 3.8 3.8L8.6 19.2l-4.6.8.8-4.6Z"/>'),
    marker: svg('<path d="m14 4 6 6-7.6 7.6H6.4v-6Z"/><path d="M4 20h7"/>'),
    arrow: svg('<path d="M5 19 19 5M10 5h9v9"/>'),
    rect: svg('<rect x="4" y="6" width="16" height="12" rx="1.6"/>'),
    oval: svg('<ellipse cx="12" cy="12" rx="8.4" ry="6.2"/>'),
    trash: svg('<path d="M5 7h14M10 7V5h4v2M7 7l.8 12h8.4L17 7"/>'),
    kbd: svg('<rect x="2.4" y="6" width="19.2" height="12" rx="2.4"/><path d="M6 9.4h.1M9.4 9.4h.1M12.8 9.4h.1M16.2 9.4h.1M6 12.4h.1M9.4 12.4h.1M12.8 12.4h.1M16.2 12.4h1.8M7.6 15.2h8.8"/>'),
    sound: svg('<path d="M4 9.4h3.2L11.6 5v14l-4.4-4.4H4Z"/><path d="M15 9a4.2 4.2 0 0 1 0 6"/>'),
    gear: svg('<circle cx="12" cy="12" r="3"/><path d="M12 3.5v2.2M12 18.3v2.2M3.5 12h2.2M18.3 12h2.2M6 6l1.6 1.6M16.4 16.4 18 18M6 18l1.6-1.6M16.4 7.6 18 6"/>')
  };

  // Ring geometry, from RingGeometry: 8 slots, inner radius 38, outer 124.
  var G = { n: 8, inner: 38, outer: 124 };
  G.label = (G.inner + G.outer) / 2;
  G.step = 360 / G.n;
  G.hl = Math.max(Math.min(2 * G.label * Math.sin(Math.PI / G.n) * 0.47, (G.outer - G.inner) / 2 - 4), 12);
  var SLOT_ICONS = ["translate", "search", "dictionary", "openLink", "allActions", "clipboard", "screenshotOCR", "pickColor"];

  // ------------------------------------------------------------------ pictures
  // Sample "photos" and screens, drawn in CSS (pop-plugins.css, .pl-art-*): no image files.
  var ARTS = {
    landscape: '<i class="sun"></i><i class="h1"></i><i class="h2"></i><i class="h3"></i>',
    beach: '<i class="sun"></i><i class="sea"></i><i class="sand"></i>',
    city: '<i class="moon"></i><i class="b1"></i><i class="b2"></i><i class="b3"></i><i class="b4"></i><i class="b5"></i>',
    portrait: '<i class="body"></i><i class="head"></i><i class="hair"></i>',
    flower: '<i class="stem"></i><i class="p1"></i><i class="p2"></i><i class="p3"></i><i class="p4"></i><i class="core"></i>',
    mug: '<i class="cup"></i><i class="handle"></i><i class="steam"></i><i class="shadow"></i>',
    screen: '<i class="bar"></i><i class="side"></i><i class="l1"></i><i class="l2"></i><i class="l3"></i><i class="card1"></i><i class="card2"></i>',
    doc: '<i class="t"></i><i class="l1"></i><i class="l2"></i><i class="l3"></i><i class="l4"></i><i class="l5"></i><i class="l6"></i>',
    logo: '<i class="mark"></i>',
    sunset: '<i class="sun"></i><i class="h1"></i><i class="h2"></i>',
    forest: '<i class="h1"></i><i class="t1"></i><i class="t2"></i><i class="t3"></i><i class="t4"></i>',
    waves: '<i class="w1"></i><i class="w2"></i><i class="w3"></i>'
  };
  function art(name, cls) {
    var a = ARTS[name] ? name : "landscape";
    return '<span class="pl-art pl-art-' + a + (cls ? " " + cls : "") + '" aria-hidden="true">' + ARTS[a] + "</span>";
  }

  // File icons in Finder and in cards. kind: folder, app, photo, video, audio, pdf, zip, dmg, font, code, text, doc…
  var EXT_TINT = { pdf: "#e5483d", zip: "#8e8e93", dmg: "#8e8e93", csv: "#2fa84f", xlsx: "#2fa84f", json: "#e0a100", xml: "#e0a100",
    srt: "#7a5af8", vtt: "#7a5af8", ass: "#7a5af8", lrc: "#7a5af8", md: "#3478f6", txt: "#8e8e93", html: "#ef6c2f", swift: "#f05138",
    py: "#3572a5", js: "#d6a400", ts: "#3178c6", go: "#00add8", sh: "#4caf50", rtf: "#3478f6", m4a: "#ff2d55", mp3: "#ff2d55", wav: "#ff2d55",
    ttf: "#5856d6", otf: "#5856d6", ttc: "#5856d6", icns: "#5856d6", sql: "#8e5cf7", yaml: "#e0a100", docx: "#2b5797", key: "#ff9500" };
  function extOf(name) { var m = /\.([A-Za-z0-9]+)$/.exec(name || ""); return m ? m[1].toLowerCase() : ""; }
  function fileIcon(f) {
    var k = f.kind || "", ext = extOf(f.name);
    if (!k) k = /^(jpe?g|png|heic|gif|webp|tiff?)$/.test(ext) ? "photo" : /^(mov|mp4|m4v|mkv)$/.test(ext) ? "video" : ext === "app" ? "app" : ext ? "doc" : "folder";
    if (k === "folder") return '<span class="pl-fi pl-fi-folder"><i></i></span>';
    if (k === "app") return '<span class="pl-fi pl-fi-app" style="--a1:' + (f.c1 || "#5b7bff") + ";--a2:" + (f.c2 || "#9a5bff") + '">' + (f.glyph || "") + "</span>";
    if (k === "photo") return '<span class="pl-fi pl-fi-photo">' + art(f.art || "landscape") + "</span>";
    if (k === "video") return '<span class="pl-fi pl-fi-video">' + art(f.art || "beach") + "<b></b></span>";
    if (k === "audio") return '<span class="pl-fi pl-fi-doc pl-fi-audio" style="--t:' + (EXT_TINT[ext] || "#ff2d55") + '"><i class="wv"></i><em>' + esc((ext || "m4a").toUpperCase()) + "</em></span>";
    if (k === "font") return '<span class="pl-fi pl-fi-doc pl-fi-font" style="--t:#5856d6"><i>Aa</i><em>' + esc((ext || "ttf").toUpperCase()) + "</em></span>";
    if (k === "zip") return '<span class="pl-fi pl-fi-doc pl-fi-zip" style="--t:#8e8e93"><i class="zp"></i><em>ZIP</em></span>';
    return '<span class="pl-fi pl-fi-doc" style="--t:' + (EXT_TINT[ext] || "#8e8e93") + '"><i class="ln"></i><em>' + esc(ext.toUpperCase().slice(0, 4)) + "</em></span>";
  }

  // A small syntax tint for code blocks: strings, numbers, keywords, comments, keys.
  var KW = /\b(const|let|var|function|return|if|else|for|while|struct|class|interface|type|enum|import|export|package|func|val|data|public|private|static|var|let|true|false|null|nil|SELECT|FROM|WHERE|AND|OR|ORDER|BY|GROUP|JOIN|LEFT|ON|IN|AS|LIMIT|INSERT|INTO|VALUES|UPDATE|SET|DESC|ASC|HAVING|COUNT|string|number|boolean|Int|String|Double|Bool|int|float64|bool|Long)\b/g;
  function tint(code, lang) {
    var out = esc(code);
    if (lang === "plain") return out;
    // Order matters: comments and strings first, then the rest outside them.
    var parts = out.split(/(&quot;[^&]*?&quot;|&#39;[^&]*?&#39;|\/\/[^\n]*|#[^\n]*(?=\n|$)|--[^\n]*)/);
    return parts.map(function (p, i) {
      if (i % 2 === 1) {
        if (/^(\/\/|#|--)/.test(p) && lang !== "md" && lang !== "yaml") return '<span class="c">' + p + "</span>";
        if (/^#/.test(p)) return '<span class="k">' + p + "</span>";
        return '<span class="s">' + p + "</span>";
      }
      return p.replace(KW, '<span class="k">$1</span>').replace(/\b(\d+(?:\.\d+)?)\b/g, '<span class="n">$1</span>');
    }).join("");
  }

  // A QR-like pattern from a string: finder squares in three corners, data from a small hash.
  function qrSVG(text, size) {
    var n = size || 25, h = 2166136261, cells = [];
    for (var i = 0; i < text.length; i++) { h ^= text.charCodeAt(i); h = Math.imul(h, 16777619) >>> 0; }
    function rnd() { h ^= h << 13; h >>>= 0; h ^= h >>> 17; h ^= h << 5; h >>>= 0; return h / 4294967296; }
    function finder(x, y) { return '<path d="M' + x + " " + y + "h7v7h-7zM" + (x + 1) + " " + (y + 1) + "v5h5v-5zM" + (x + 2) + " " + (y + 2) + 'h3v3h-3z" fill-rule="evenodd"/>'; }
    for (var yy = 0; yy < n; yy++) for (var xx = 0; xx < n; xx++) {
      var inF = (xx < 8 && yy < 8) || (xx >= n - 8 && yy < 8) || (xx < 8 && yy >= n - 8);
      if (!inF && rnd() < 0.48) cells.push("M" + xx + " " + yy + "h1v1h-1z");
    }
    return '<svg class="pl-qr" viewBox="-1 -1 ' + (n + 2) + " " + (n + 2) + '" aria-hidden="true" shape-rendering="crispEdges"><rect x="-1" y="-1" width="' + (n + 2) + '" height="' + (n + 2) + '" fill="#fff"/><g fill="#111">' +
      finder(0, 0) + finder(n - 7, 0) + finder(0, n - 7) + '<path d="' + cells.join("") + '"/></g></svg>';
  }
  function barcodeSVG(text) {
    var x = 0, bars = [], h = 0;
    for (var i = 0; i < text.length * 3 + 10; i++) {
      h = (h * 31 + (text.charCodeAt(i % text.length) || 7) + i) % 97;
      var w = 1 + (h % 3);
      if (i % 2 === 0) bars.push('<rect x="' + x + '" y="0" width="' + w + '" height="40"/>');
      x += w;
    }
    return '<svg class="pl-barcode" viewBox="-4 -4 ' + (x + 8) + ' 48" preserveAspectRatio="none" aria-hidden="true"><rect x="-4" y="-4" width="' + (x + 8) + '" height="48" fill="#fff"/><g fill="#111">' + bars.join("") + "</g></svg>";
  }

  // ------------------------------------------------------------------ the player
  var uid = 0;
  function Player(fig) {
    var data = JSON.parse(fig.querySelector(".pla-data").textContent);
    this.fig = fig;
    this.id = "pla" + (++uid);
    this.lang = fig.getAttribute("data-lang") === "zh" ? "zh" : "en";
    this.s = S[this.lang];
    this.icon = fig.getAttribute("data-icon") || "";
    this.name = data.name;
    this.glyph = svg(data.glyph);
    this.sc = data.scene || {};
    this.steps = this.sc.steps || [];
    this.n = 3 + Math.max(1, this.steps.length);
    var how = fig.closest(".howto");
    this.list = how ? how.querySelector(".pla-steps") : null;
    this.gen = 0;
    this.t = 0;
    this.timers = [];
    this.anims = [];
    this.playing = false;
    this.userPaused = false;
    this.visible = false;
    this.ff = false;
    this.still = mqReduce.matches;
    this.build();
  }

  Player.prototype = {
    // -------------------------------------------------------------- clock
    // Virtual time that only advances while playing, so pausing freezes the film.
    frame: function (now) {
      this.raf = 0;
      if (!this.playing) return;
      var dt = this.last ? Math.min(64, now - this.last) : 16;
      this.last = now;
      this.t += dt;
      var t = this.t;
      var due = this.timers.filter(function (x) { return x.at <= t; });
      this.timers = this.timers.filter(function (x) { return x.at > t; });
      due.forEach(function (x) { x.ok(); });
      var live = [], done = [];
      this.anims.forEach(function (a) {
        var p = clamp((t - a.t0) / a.ms, 0, 1);
        a.fn(p);
        (p >= 1 ? done : live).push(a);
      });
      this.anims = live;
      done.forEach(function (a) { a.ok(); });
      this.kick();
    },
    kick: function () {
      var self = this;
      if (!this.raf && this.playing) this.raf = requestAnimationFrame(function (n) { self.frame(n); });
    },
    wait: function (ms) {
      var self = this, gen = this.gen;
      if (this.ff || !ms) return gen === this.gen ? Promise.resolve() : Promise.reject(STOP);
      return new Promise(function (ok, no) {
        self.timers.push({ at: self.t + ms, ok: function () { if (gen === self.gen) ok(); else no(STOP); }, no: no });
        self.kick();
      });
    },
    // Runs fn(p) for p from 0 to 1 over ms of virtual time.
    anim: function (ms, fn) {
      var self = this, gen = this.gen;
      if (this.ff || !ms) { fn(1); return Promise.resolve(); }
      fn(0);
      return new Promise(function (ok, no) {
        self.anims.push({ t0: self.t, ms: ms, fn: fn, ok: function () { if (gen === self.gen) ok(); else no(STOP); }, no: no });
        self.kick();
      });
    },
    cancel: function () {
      this.gen++;
      var stopped = this.timers.concat(this.anims);
      this.timers = [];
      this.anims = [];
      stopped.forEach(function (x) { x.no(STOP); });
    },
    check: function (gen) { if (gen !== this.gen) throw STOP; },

    // -------------------------------------------------------------- frame and controls
    build: function () {
      var f = this.fig, s = this.s, self = this;
      f.classList.add("is-ready");
      f.setAttribute("role", "group");
      f.setAttribute("aria-label", fmt(s.label, this.lang === "zh" ? "「" + this.name + "」" : this.name));
      this.stage = el("div", "pl-stage");
      this.stage.setAttribute("aria-hidden", "true");
      f.insertBefore(this.stage, f.firstChild);
      var bar = el("figcaption", "pla-bar");
      this.btn = el("button", "pla-play");
      this.btn.type = "button";
      this.btn.addEventListener("click", function () {
        if (self.still) { self.show(self.ch == null ? 3 : self.ch); return; }
        if (self.playing) { self.userPaused = true; self.pause(); } else { self.userPaused = false; self.resume(); }
      });
      bar.appendChild(this.btn);
      bar.appendChild(el("span", "pla-tag", '<span class="pla-dot" aria-hidden="true"></span>' + esc(s.tag)));
      f.appendChild(bar);
      if (this.still) this.btn.hidden = true;
      if (this.list) {
        each(this.list.querySelectorAll("li"), function (li, k) {
          li.setAttribute("data-ch", k);
          var b = el("button", "pla-step");
          b.type = "button";
          while (li.firstChild) b.appendChild(li.firstChild);
          li.appendChild(b);
          b.addEventListener("click", function () {
            if (self.still) { self.show(k); return; }
            self.userPaused = false;
            self.start(k);
          });
        });
        this.list.classList.add("is-live");
      }
      this.setBtn();
      if ("IntersectionObserver" in window) {
        new IntersectionObserver(function (es) {
          es.forEach(function (e) { self.visible = e.isIntersecting; self.onVis(); });
        }, { threshold: 0.25 }).observe(f);
      } else { this.visible = true; }
      D.addEventListener("visibilitychange", function () { self.onVis(); });
      if ("ResizeObserver" in window) {
        var w0 = 0;
        new ResizeObserver(function () {
          var w = self.stage.clientWidth;
          if (!w0) { w0 = w; return; }
          if (Math.abs(w - w0) < 24) return;
          w0 = w;
          clearTimeout(self.rz);
          self.rz = setTimeout(function () { if (self.still) self.show(self.ch == null ? 3 : self.ch); else if (self.started) self.start(Math.max(0, self.ch || 0)); }, 200);
        }).observe(this.stage);
      }
      if (mqReduce.addEventListener) mqReduce.addEventListener("change", function () {
        self.still = mqReduce.matches;
        self.btn.hidden = self.still;
        if (self.still) self.show(3); else self.start(0);
      });
      if (this.still) this.show(3); else { this.prepare(); this.onVis(); }
    },
    setBtn: function () {
      var on = this.playing;
      this.btn.innerHTML = on ? I.pause : I.play;
      this.btn.setAttribute("aria-label", on ? this.s.pause : this.s.play);
      this.btn.title = on ? this.s.pause : this.s.play;
    },
    onVis: function () {
      if (this.still) return;
      var on = this.visible && !D.hidden && !this.userPaused;
      if (on && !this.started) { this.start(0); return; }
      if (on) this.resume(); else this.pause();
    },
    pause: function () { this.playing = false; this.last = 0; this.stage.classList.add("is-paused"); this.setBtn(); },
    resume: function () {
      if (!this.started) { this.start(0); return; }
      this.playing = true; this.last = 0; this.stage.classList.remove("is-paused"); this.setBtn(); this.kick();
    },
    mark: function (k) {
      this.ch = k;
      if (!this.list) return;
      each(this.list.querySelectorAll("li"), function (li, i) {
        li.classList.toggle("is-on", i === k);
        li.classList.toggle("is-done", i < k);
        var b = li.firstChild;
        if (b && b.setAttribute) { if (i === k) b.setAttribute("aria-current", "step"); else b.removeAttribute("aria-current"); }
      });
    },

    // Plays from chapter k: earlier chapters are applied instantly (fast-forward), then it runs and loops.
    start: function (k) {
      this.started = true;
      this.cancel();
      var gen = this.gen, self = this;
      this.playing = this.visible && !D.hidden && !this.userPaused;
      this.stage.classList.toggle("is-paused", !this.playing);
      this.setBtn();
      this.prepare();
      this.ff = true;
      this.stage.classList.add("is-ff");
      var run = (async function () {
        for (var i = 0; i < k; i++) await self.chapter(i);
        self.check(gen);
        void self.stage.offsetWidth;
        self.ff = false;
        self.stage.classList.remove("is-ff");
        if (self.tele) self.teleRun();
        for (i = k; i < self.n; i++) { self.mark(i); await self.chapter(i); }
        await self.wait(2800);
        self.stage.classList.add("is-out");
        await self.wait(600);
        self.check(gen);
        self.start(0);
      })();
      run.catch(function (e) { if (e !== STOP && window.console) console.error(e); });
      this.kick();
    },
    // Reduced motion: shows chapter k's end state, without moving.
    show: function (k) {
      this.cancel();
      var gen = this.gen, self = this;
      this.prepare();
      this.ff = true;
      this.stage.classList.add("is-ff");
      this.keepRing = k === 2;
      (async function () {
        for (var i = 0; i <= k; i++) await self.chapter(i);
        self.check(gen);
        self.mark(k);
      })().catch(function (e) { if (e !== STOP && window.console) console.error(e); });
    },

    // -------------------------------------------------------------- the pretend Mac
    prepare: function () {
      var s = this.s, sc = this.sc, st = this.stage;
      st.className = "pl-stage" + (this.ff ? " is-ff" : "") + (this.playing ? "" : " is-paused") + (sc.tall ? " is-tall" : "");
      var src = sc.src || { kind: "desk" };
      var menus = (src.menus || s.menus).map(function (m) { return '<span class="pl-mb-i">' + esc(m) + "</span>"; }).join("");
      var appName = src.kind === "files" ? s.finder : (src.app || "Notes");
      st.innerHTML =
        '<div class="pl-mb"><span class="pl-mb-i pl-mb-app">' + esc(appName) + "</span>" + menus + '<span class="pl-mb-fill"></span>' +
        '<span class="pl-mb-x"></span><span class="pl-mb-i pl-mb-icon"><img src="' + esc(this.icon) + '" alt="" width="16" height="16"></span>' +
        '<span class="pl-mb-i pl-mb-clock">' + esc(s.clock) + "</span></div>" +
        this.window(src) +
        '<div class="pl-layer"></div><div class="pl-cur"><span class="pl-press"><svg viewBox="0 0 40 40"><circle cx="20" cy="20" r="16"/></svg></span>' +
        '<svg class="pl-arrow" viewBox="0 0 24 24"><path d="M5.5 3.2v15.2l3.9-3.7 2.6 6 2.7-1.2-2.6-5.9h5.4Z"/></svg>' +
        '<svg class="pl-ibeam" viewBox="0 0 24 24"><path d="M9 4c1.6 0 2.4.5 3 1.3.6-.8 1.4-1.3 3-1.3M9 20c1.6 0 2.4-.5 3-1.3.6.8 1.4 1.3 3 1.3M12 5.3v13.4M10 12h4"/></svg>' +
        '<svg class="pl-cross" viewBox="0 0 24 24"><path d="M12 3v18M3 12h18"/></svg><span class="pl-kbd"></span></div>';
      this.mb = st.querySelector(".pl-mb");
      this.win = st.querySelector(".pl-win");
      this.layer = st.querySelector(".pl-layer");
      this.cursor = st.querySelector(".pl-cur");
      this.card = null;
      this.fx = this.fxEl = this.tele = this.bubble = this.follow = this.ringAt = null;
      this.blocks = [];
      var W = st.clientWidth || 600, H = st.clientHeight || 440;
      this.W = W; this.H = H;
      this.at = { x: W * 0.62, y: H * 0.86 };
      this.place();
    },
    window: function (src) {
      var s = this.s, k = src.kind || "desk";
      if (k === "none") return "";
      var bar = function (title, extra) {
        return '<div class="pl-tb"><i></i><i></i><i></i>' + (extra || "") + "<span>" + esc(title) + "</span></div>";
      };
      if (k === "files") {
        var items = (src.files || []).map(function (f, i) {
          return '<div class="pl-file' + (f.sel ? " is-target" : "") + '" data-i="' + i + '">' + fileIcon(f) + '<span class="pl-fn">' + esc(f.name) + "</span></div>";
        }).join("");
        var side = s.side.map(function (x, i) { return '<span class="' + (i === 3 && !src.app ? "is-on" : "") + '">' + esc(x) + "</span>"; }).join("");
        return '<div class="pl-win pl-finder">' + bar(src.app || s.side[3], '<b class="pl-nav">' + I.chevL + I.chevR + "</b>") +
          '<div class="pl-fbody"><div class="pl-side"><em>' + esc(s.fav) + "</em>" + side + '</div><div class="pl-grid' + (src.files && src.files.length > 8 ? " is-dense" : "") + '">' + items + "</div></div></div>";
      }
      if (k === "web") {
        var lines = spanLines(src.lines || []).map(function (l, i) { return i === 0 ? "<h4>" + marks(l) + "</h4>" : "<p>" + marks(l) + "</p>"; }).join("");
        return '<div class="pl-win pl-web">' + bar("", '<span class="pl-url">' + marks(src.url || "example.com") + "</span>") +
          '<div class="pl-page"><div class="pl-page-in">' + lines + (src.pic ? '<div class="pl-pic">' + art(src.pic) + "</div>" : "") + (src.more ? (src.more.map(function (l) { return "<p>" + marks(l) + "</p>"; }).join("")) : "") + "</div></div></div>";
      }
      if (k === "text") {
        var raw = !!src.raw;
        var body = spanLines(src.lines || []).map(function (l) {
          if (l === "") return '<p class="pl-gap"></p>';
          if (/^# /.test(l) && !raw) return "<h4>" + marks(l.slice(2)) + "</h4>";
          return "<p>" + marks(l, raw) + "</p>";
        }).join("");
        return '<div class="pl-win pl-text">' + bar(src.title || src.app || "Notes") + '<div class="pl-doc' + (src.mono ? " is-mono" : "") + '">' + body + "</div></div>";
      }
      if (k === "image") {
        return '<div class="pl-win pl-viewer">' + bar(src.title || "Preview") + '<div class="pl-vbody"><div class="pl-shot">' + art(src.art || "landscape") +
          (src.overlay ? '<div class="pl-shot-o">' + src.overlay + "</div>" : "") + "</div></div></div>";
      }
      // desk: a quiet window to hold right click over
      return '<div class="pl-win pl-quiet">' + bar(src.title || "Notes") + '<div class="pl-doc">' +
        (src.lines ? src.lines.map(function (l) { return "<p>" + marks(l) + "</p>"; }).join("") : '<i class="pl-ph" style="width:62%"></i><i class="pl-ph" style="width:84%"></i><i class="pl-ph" style="width:70%"></i><i class="pl-ph" style="width:40%"></i>') + "</div></div>";
    },

    // -------------------------------------------------------------- the pointer
    place: function () {
      this.cursor.style.transform = "translate(" + this.at.x.toFixed(1) + "px," + this.at.y.toFixed(1) + "px)";
      if (this.follow) this.follow(this.at.x, this.at.y);
    },
    rel: function (node) {
      var a = node.getBoundingClientRect(), b = this.stage.getBoundingClientRect();
      return { x: a.left - b.left, y: a.top - b.top, w: a.width, h: a.height };
    },
    // Moves the pointer to (x, y) in stage coordinates.
    move: function (x, y, ms) {
      var self = this, x0 = this.at.x, y0 = this.at.y;
      var dist = Math.sqrt((x - x0) * (x - x0) + (y - y0) * (y - y0));
      if (ms == null) ms = clamp(260 + dist * 1.3, 300, 900);
      return this.anim(ms, function (p) {
        var e = ease(p);
        self.at = { x: lerp(x0, x, e), y: lerp(y0, y, e) };
        self.place();
      });
    },
    moveTo: function (node, fx, fy, ms) {
      var r = this.rel(node);
      return this.move(r.x + r.w * (fx == null ? 0.5 : fx), r.y + r.h * (fy == null ? 0.5 : fy), ms);
    },
    // Follows a list of points, for drawing.
    trace: function (pts, ms) {
      var self = this, len = [0], total = 0;
      for (var i = 1; i < pts.length; i++) { total += Math.hypot(pts[i][0] - pts[i - 1][0], pts[i][1] - pts[i - 1][1]); len.push(total); }
      return this.anim(ms, function (p) {
        var d = ease(p) * total, j = 1;
        while (j < len.length - 1 && len[j] < d) j++;
        var seg = (len[j] - len[j - 1]) || 1, q = clamp((d - len[j - 1]) / seg, 0, 1);
        self.at = { x: lerp(pts[j - 1][0], pts[j][0], q), y: lerp(pts[j - 1][1], pts[j][1], q) };
        self.place();
      });
    },
    shape: function (k) { this.cursor.setAttribute("data-shape", k || ""); },
    click: async function (right) {
      var c = this.cursor;
      c.classList.add(right ? "is-rdown" : "is-down");
      this.ripple();
      await this.wait(140);
      c.classList.remove("is-down", "is-rdown");
      await this.wait(90);
    },
    ripple: function () {
      if (this.ff) return;
      var r = el("span", "pl-ripple");
      r.style.left = this.at.x + "px"; r.style.top = this.at.y + "px";
      this.stage.appendChild(r);
      setTimeout(function () { r.remove(); }, 700);
    },
    key: async function (label) {
      var k = this.cursor.querySelector(".pl-kbd");
      k.textContent = label;
      this.cursor.classList.add("has-key");
      await this.wait(650);
      this.cursor.classList.remove("has-key");
    },

    // -------------------------------------------------------------- chapters
    chapter: function (k) {
      if (k === 0) return this.chSelect();
      if (k === 1) return this.chHold();
      if (k === 2) return this.chRing();
      return this.chResult(k - 3);
    },
    chSelect: async function () {
      var src = this.sc.src || { kind: "desk" }, st = this.stage, self = this;
      await this.wait(500);
      if (src.kind === "text" || src.kind === "web") {
        var sels = st.querySelectorAll(".pl-sel");
        if (!sels.length) { await this.moveTo(this.win, 0.62, 0.62); return; }
        var b = st.getBoundingClientRect(), first = sels[0].getClientRects(), lastR = sels[sels.length - 1].getClientRects();
        var r0 = first[0], r1 = lastR[lastR.length - 1];
        this.shape("ibeam");
        await this.move(r0.left - b.left + 1, r0.top - b.top + r0.height / 2);
        this.cursor.classList.add("is-down");
        var x1 = r1.right - b.left - 1, y1 = r1.top - b.top + r1.height / 2, x0 = this.at.x, y0 = this.at.y;
        var lens = Array.prototype.map.call(sels, function (x) { return Math.max(1, (x.textContent || "").length); });
        var len = lens.reduce(function (a, c) { return a + c; }, 0);
        await this.anim(clamp(len * 28, 500, 1500), function (p) {
          var done = p * len, acc = 0;
          each(sels, function (x, i) {
            x.style.setProperty("--p", (clamp((done - acc) / lens[i], 0, 1) * 100).toFixed(1) + "%");
            acc += lens[i];
          });
          self.at = { x: lerp(x0, x1, p), y: lerp(y0, y1, p) };
          self.place();
        });
        each(sels, function (x) { x.classList.add("is-done"); });
        this.cursor.classList.remove("is-down");
        this.shape("");
        await this.wait(260);
        // Hold right click over the selection, as you would.
        await this.move(lerp(x0, x1, 0.5), lerp(y0, y1, 0.5) + 2, 380);
      } else if (src.kind === "files") {
        var files = st.querySelectorAll(".pl-file.is-target");
        for (var i = 0; i < files.length; i++) {
          await this.moveTo(files[i].querySelector(".pl-fi"), 0.5, 0.55);
          if (i > 0) this.key("⌘");
          await this.click();
          if (i === 0) each(st.querySelectorAll(".pl-file.is-sel"), function (x) { x.classList.remove("is-sel"); });
          files[i].classList.add("is-sel");
          await this.wait(160);
        }
        await this.wait(200);
      } else if (src.kind === "image") {
        var shot = st.querySelector(".pl-shot");
        await this.moveTo(shot, 0.55, 0.5);
        await this.click();
        shot.classList.add("is-sel");
      } else {
        var t = st.querySelector(".pl-tgt");
        if (t) await this.moveTo(t, 0.6, 0.6);
        else await this.move(this.W * (src.x || 0.56), this.H * (src.y || 0.6));
      }
      await this.wait(300);
    },
    chHold: async function () {
      var c = this.cursor;
      c.classList.add("is-hold", "is-rdown");
      var ring = c.querySelector(".pl-press circle");
      await this.anim(this.ff ? 0 : 900, function (p) { ring.style.strokeDashoffset = (1 - p).toFixed(3); });
      c.classList.remove("is-rdown");
      await this.wait(60);
    },
    chRing: async function () {
      var s = this.s, sc = this.sc, self = this;
      var slot = sc.slot == null ? 2 : sc.slot;
      var cx = clamp(this.at.x, 128, this.W - 128), cy = clamp(this.at.y, 152, this.H - 128);
      var ring = el("div", "pl-ring");
      ring.style.left = cx + "px"; ring.style.top = cy + "px";
      var html = '<div class="pl-disc"></div><div class="pl-hl"><span class="pl-hl-dot"></span></div><div class="pl-hub"><div class="pl-center">' +
        '<span class="pl-c-content">' + esc(this.summary()) + '</span><span class="pl-c-fn"></span></div></div>';
      for (var i = 0; i < G.n; i++) {
        var th = i * G.step * Math.PI / 180, x = Math.sin(th) * G.label, y = -Math.cos(th) * G.label;
        var mine = i === slot;
        var label = mine ? this.name : s.slots[i], icon = mine ? this.glyph : I[SLOT_ICONS[i]];
        html += '<div class="pl-slot' + (mine ? " is-mine" : "") + '" style="--x:' + x.toFixed(1) + "px;--y:" + y.toFixed(1) + "px;--i:" + i + '"><span class="pl-slot-in">' + icon + "<span>" + esc(label) + "</span></span></div>";
      }
      ring.innerHTML = html;
      var dot = ring.querySelector(".pl-hl-dot");
      dot.style.width = dot.style.height = (G.hl * 2).toFixed(1) + "px";
      dot.style.top = (G.outer - G.label - G.hl).toFixed(1) + "px";
      this.layer.appendChild(ring);
      this.cursor.classList.remove("is-hold");
      this.cursor.querySelector(".pl-press circle").style.strokeDashoffset = "1";
      void ring.offsetWidth;
      ring.classList.add("is-shown");
      await this.wait(520);
      var th2 = slot * G.step * Math.PI / 180;
      ring.querySelector(".pl-hl").style.transform = "rotate(" + slot * G.step + "deg)";
      var tx = cx + Math.sin(th2) * (G.label + 6), ty = cy - Math.cos(th2) * (G.label + 6);
      var mineEl = ring.querySelector(".is-mine"), fn = ring.querySelector(".pl-c-fn");
      await this.move(tx, ty, 520);
      ring.classList.add("has-hover");
      mineEl.classList.add("is-active");
      fn.textContent = this.name;
      if (this.keepRing) { this.keepRing = false; return; }
      await this.wait(420);
      mineEl.classList.add("is-commit");
      ring.classList.add("is-committed");
      await this.wait(160);
      ring.classList.add("is-leaving");
      await this.wait(220);
      ring.remove();
      this.ringAt = { x: cx, y: cy };
    },
    summary: function () {
      var src = this.sc.src || {}, s = this.s;
      if (src.sum) return src.sum;
      if (src.kind === "text" || src.kind === "web") {
        var t = Array.prototype.map.call(this.stage.querySelectorAll(".pl-sel"), function (x) { return x.textContent; }).join("\n");
        if (/^https?:\/\//.test(t)) return s.link;
        return Array.from(t).length <= 10 ? t : fmt(s.chars, Array.from(t).length);
      }
      if (src.kind === "files") {
        var n = (src.files || []).filter(function (f) { return f.sel; });
        if (n.length === 1) return n[0].name;
        var photos = n.every(function (f) { return (f.kind || "") === "photo" || /\.(jpe?g|png|heic)$/i.test(f.name); });
        return photos ? fmt(s.images, n.length) : fmt(s.items, n.length);
      }
      if (src.kind === "image") return s.image;
      return s.nothing;
    },
    chResult: async function (i) {
      var step = this.steps[i] || {};
      if (i === 0) {
        if (this.sc.fx) await this.fxStart(this.sc.fx);
        if (this.sc.card) await this.openCard(this.sc.card);
      }
      var acts = step.acts || [];
      for (var k = 0; k < acts.length; k++) await this.act(acts[k]);
      await this.wait(step.hold == null ? 1300 : step.hold);
    },

    // -------------------------------------------------------------- result cards
    openCard: async function (spec) {
      var self = this;
      if (this.card) this.card.remove();
      var c = el("div", "pl-card is-entering");
      c.style.setProperty("--w", (spec.w || 380) + "px");
      var head = '<div class="pl-head"><span class="pl-hi">' + this.glyph + "</span><h5>" + esc(spec.title || this.name) + "</h5>" +
        (spec.sub ? '<span class="pl-sub">' + esc(spec.sub) + "</span>" : "") + '<span class="pl-x">' + I.close + "</span></div>";
      c.innerHTML = head;
      this.blocks = [];
      (spec.body || []).forEach(function (b, k) { var n = self.block(b, k); c.appendChild(n); self.blocks.push(n); });
      if (spec.btns && spec.btns.length) {
        var f = el("div", "pl-flow pl-foot");
        spec.btns.forEach(function (b, k) {
          var lab = typeof b === "string" ? b : b.l;
          f.appendChild(el("span", "pl-btn" + (k === (spec.tint == null ? -1 : spec.tint) ? " is-tint" : ""), esc(lab)));
        });
        c.appendChild(f);
      }
      this.layer.appendChild(c);
      this.card = c;
      // Near the pointer, inside the stage.
      var W = this.W, H = this.H, w = c.offsetWidth, h = c.offsetHeight;
      var pos = spec.at || "pointer", p = this.ringAt || this.at, x, y;
      if (pos === "center") { x = (W - w) / 2; y = (H - h) / 2 + 10; }
      else if (pos === "right") { x = W - w - 12; y = 34; }
      else if (pos === "left") { x = 12; y = 34; }
      else { x = p.x - w * 0.42; y = p.y - 60; }
      x = clamp(x, 8, Math.max(8, W - w - 8));
      y = clamp(y, 32, Math.max(32, H - h - 8));
      c.style.left = x + "px"; c.style.top = y + "px";
      void c.offsetWidth;
      c.classList.remove("is-entering");
      await this.wait(260);
      // Blocks that animate as they appear.
      for (var k = 0; k < this.blocks.length; k++) if (!this.blocks[k].classList.contains("is-hidden")) this.reveal(k, true);
      await this.wait(300);
      // Leave the pointer just beside the card.
      if (!spec.keepPointer) {
        var r = this.rel(c);
        var px = r.x + r.w + 26 < W ? r.x + r.w + 18 : r.x + r.w * 0.7;
        await this.move(px, Math.min(H - 20, r.y + r.h * 0.7), 420);
      }
    },
    block: function (b, k) {
      var t = b.t || "text", self = this, n = el("div", "pl-b pl-b-" + t + (b.hide ? " is-hidden" : "") + (b.cls ? " " + b.cls : ""));
      n.setAttribute("data-b", k);
      var h = "";
      switch (t) {
        case "text":
          h = '<p class="' + (b.mono ? "pl-mono " : "") + (b.muted ? "pl-muted " : "") + (b.size ? "pl-sz-" + b.size : "") + '">' + (b.type ? "" : marks(b.text)) + "</p>";
          break;
        case "note": h = '<p class="pl-note">' + marks(b.text) + "</p>"; break;
        case "big": h = '<div class="pl-big"><strong>' + marks(b.text) + "</strong>" + (b.sub ? "<span>" + marks(b.sub) + "</span>" : "") + "</div>"; break;
        case "rows":
          h = '<div class="pl-rows">' + b.rows.map(function (r, i) {
            return '<div class="pl-row' + (r[2] ? " is-" + r[2] : "") + '" data-i="' + i + '"><span class="pl-row-l">' + esc(r[0]) + '</span><span class="pl-row-v' + (b.mono === false ? "" : " pl-mono") + '">' + marks(r[1]) + "</span>" + (b.copy === false ? "" : '<span class="pl-ib">' + I.copy + "</span>") + "</div>";
          }).join("") + "</div>";
          break;
        case "code": h = '<pre class="pl-code">' + tint(b.text, b.lang || "plain") + "</pre>"; break;
        case "seg": case "chips":
          h = '<div class="' + (t === "seg" ? "pl-seg" : "pl-chips") + '">' + b.items.map(function (x, i) {
            var on = Array.isArray(b.on) ? b.on.indexOf(i) >= 0 : i === (b.on || 0);
            return '<span class="pl-opt' + (on ? " is-on" : "") + '" data-i="' + i + '">' + marks(x) + "</span>";
          }).join("") + "</div>";
          if (b.label) h = '<div class="pl-seg-row"><span class="pl-lab">' + esc(b.label) + "</span>" + h + "</div>";
          break;
        case "btns":
          h = '<div class="pl-flow">' + b.items.map(function (x, i) { return '<span class="pl-btn' + (i === b.tint ? " is-tint" : "") + '" data-i="' + i + '">' + marks(x) + "</span>"; }).join("") + "</div>";
          break;
        case "panes":
          h = '<div class="pl-panes">' + b.panes.map(function (p, i) {
            return '<div class="pl-pane' + (i === (b.on || 0) ? " is-on" : "") + '" data-i="' + i + '"></div>';
          }).join("") + "</div>";
          n.innerHTML = h;
          each(n.querySelectorAll(".pl-pane"), function (pane, i) {
            (b.panes[i] || []).forEach(function (sub, j) { pane.appendChild(self.block(sub, k + "." + j)); });
          });
          n.__spec = b;
          return n;
        case "list":
          h = '<div class="pl-list' + (b.dense ? " is-dense" : "") + '">' + b.items.map(function (it, i) {
            var ic = it.file ? fileIcon(it.file) : it.icon ? '<span class="pl-li-ic">' + (it.icon.charAt(0) === "<" ? it.icon : esc(it.icon)) + "</span>" : it.sw ? '<span class="pl-li-sw" style="background:' + esc(it.sw) + '"></span>' : "";
            return '<div class="pl-li' + (it.on ? " is-on" : "") + (it.tone ? " is-" + it.tone : "") + (it.hide ? " is-hidden" : "") + '" data-i="' + i + '">' +
              (it.chk != null ? '<span class="pl-chk' + (it.chk ? " is-on" : "") + '">' + I.check + "</span>" : "") + ic +
              '<span class="pl-li-t"><span>' + marks(it.title) + "</span>" + (it.sub ? "<small>" + marks(it.sub) + "</small>" : "") + "</span>" +
              (it.right ? '<span class="pl-li-r">' + marks(it.right) + "</span>" : "") + (it.btn ? '<span class="pl-btn">' + esc(it.btn) + "</span>" : "") + "</div>";
          }).join("") + "</div>";
          break;
        case "diff":
          h = '<div class="pl-diff">' + b.lines.map(function (l) {
            var cls = l[0] === "+" ? "add" : l[0] === "-" ? "del" : "ctx";
            return '<div class="pl-dl is-' + cls + '"><i>' + (l[0] === " " ? "" : esc(l[0])) + "</i><span>" + marks(l[1]) + "</span></div>";
          }).join("") + "</div>";
          break;
        case "table":
          h = '<div class="pl-tablewrap"><table class="pl-table"><thead><tr>' + b.head.map(function (x) { return "<th>" + marks(x) + "</th>"; }).join("") + "</tr></thead><tbody>" +
            b.rows.map(function (r) { return "<tr>" + r.map(function (x) { return "<td>" + marks(x) + "</td>"; }).join("") + "</tr>"; }).join("") + "</tbody></table></div>";
          break;
        case "chart": h = this.chart(b); break;
        case "swatches":
          h = '<div class="pl-sws">' + b.items.map(function (x) {
            return '<span class="pl-sw"><i style="background:' + esc(x[0]) + '"></i><b>' + esc(x[0]) + "</b>" + (x[1] ? "<small>" + esc(x[1]) + "</small>" : "") + "</span>";
          }).join("") + "</div>";
          break;
        case "grid":
          h = '<div class="pl-cells" style="--cols:' + (b.cols || 8) + '">' + b.items.map(function (x, i) {
            return '<span class="pl-cell' + (i === b.on ? " is-on" : "") + '" data-i="' + i + '">' + esc(x) + "</span>";
          }).join("") + "</div>";
          break;
        case "qr":
          h = '<div class="pl-qrwrap' + (b.small ? " is-small" : "") + '">' + qrSVG(b.text || "pop") + (b.caption ? "<span>" + marks(b.caption) + "</span>" : "") + "</div>";
          break;
        case "barcode": h = '<div class="pl-qrwrap is-bar">' + barcodeSVG(b.text || "POP") + "<span>" + esc(b.text || "") + "</span></div>"; break;
        case "bar":
          h = '<div class="pl-prog"><div class="pl-prog-h"><span>' + marks(b.label || "") + '</span><span class="pl-prog-r">' + marks(b.right || "") + '</span></div><div class="pl-track"><i style="--v:' + (b.from || 0) + '"></i></div></div>';
          break;
        case "stats":
          h = '<div class="pl-stats">' + b.items.map(function (x) {
            return '<div class="pl-stat"><strong data-v="' + esc(x[0]) + '">' + esc(x[0]) + "</strong>" + (x[1] ? "<em>" + esc(x[1]) + "</em>" : "") + "<span>" + esc(x[2] || "") + "</span></div>";
          }).join("") + "</div>";
          break;
        case "dial":
          h = '<div class="pl-dial"><svg viewBox="0 0 120 120"><circle class="tr" cx="60" cy="60" r="52"/><circle class="v" cx="60" cy="60" r="52" pathLength="1"/></svg><div><strong>' + esc(b.text || "") + "</strong><span>" + esc(b.sub || "") + "</span></div></div>";
          break;
        case "thumbs":
          h = '<div class="pl-thumbs" style="--cols:' + (b.cols || 4) + '">' + b.items.map(function (x, i) {
            return '<div class="pl-th' + (x.chk ? " is-chk" : "") + (x.best ? " is-best" : "") + '" data-i="' + i + '">' + art(x.art || "landscape", x.cls) +
              (x.chk != null ? '<span class="pl-chk' + (x.chk ? " is-on" : "") + '">' + I.check + "</span>" : "") + (x.label ? "<em>" + esc(x.label) + "</em>" : "") + "</div>";
          }).join("") + "</div>";
          break;
        case "img":
          h = '<div class="pl-img' + (b.mods ? " " + b.mods.map(function (m) { return "is-" + m; }).join(" ") : "") + '" style="--ar:' + (b.ar || "16/10") + (b.h ? ";--h:" + b.h + "px" : "") + '">' +
            art(b.art || "landscape") + (b.over ? '<div class="pl-img-o">' + b.over + "</div>" : "") + (b.mark ? '<div class="pl-wm">' + Array(13).join("<span>" + esc(b.mark) + "</span>") + "</div>" : "") + "</div>" +
            (b.caption ? '<p class="pl-note">' + marks(b.caption) + "</p>" : "");
          break;
        case "field":
          h = (b.label ? '<span class="pl-lab">' + esc(b.label) + "</span>" : "") + '<span class="pl-field' + (b.mono ? " pl-mono" : "") + '"><span class="pl-fv">' + (b.type ? "" : marks(b.value || "")) + '</span><span class="pl-caret"></span>' +
            (b.ph ? '<span class="pl-ph2">' + esc(b.ph) + "</span>" : "") + "</span>";
          break;
        case "slider":
          h = '<div class="pl-slider"><span class="pl-lab">' + esc(b.label || "") + '</span><span class="pl-sl"><i style="--v:' + (b.value == null ? 0.5 : b.value) + '"></i></span><span class="pl-sl-v">' + esc(b.right || "") + "</span></div>";
          break;
        case "wave":
          var bars = "";
          for (var w = 0; w < (b.n || 48); w++) bars += '<i style="--h:' + (0.18 + 0.8 * Math.abs(Math.sin(w * 1.7) * Math.cos(w * 0.37))).toFixed(2) + '"></i>';
          h = '<div class="pl-wave' + (b.live ? " is-live" : "") + '">' + bars + "</div>";
          break;
        case "hours": h = this.hours(b); break;
        case "sep": h = "<hr>"; break;
        case "html": h = b.html; break;
        default: h = marks(b.text || "");
      }
      n.innerHTML = h;
      n.__spec = b;
      return n;
    },
    chart: function (b) {
      var data = b.data, max = 0;
      data.forEach(function (d) { max = Math.max(max, d[1]); });
      var colors = ["#0a84ff", "#30b0c7", "#34c759", "#ff9f0a", "#ff375f", "#af52de", "#5e5ce6", "#a2845e"];
      if (b.kind === "pie") {
        var tot = 0, acc = 0, segs = [];
        data.forEach(function (d) { tot += d[1]; });
        data.forEach(function (d, i) { var a0 = acc / tot * 100; acc += d[1]; segs.push(colors[i % 8] + " " + a0.toFixed(2) + "% " + (acc / tot * 100).toFixed(2) + "%"); });
        return '<div class="pl-pie"><i style="background:conic-gradient(' + segs.join(",") + ')"></i><ul>' + data.map(function (d, i) {
          return '<li><b style="background:' + colors[i % 8] + '"></b>' + esc(d[0]) + "<span>" + Math.round(d[1] / tot * 100) + "%</span></li>";
        }).join("") + "</ul></div>";
      }
      if (b.kind === "line") {
        var w = 300, hh = 110, pts = data.map(function (d, i) { return [10 + i * (w - 20) / Math.max(1, data.length - 1), hh - 12 - (d[1] / max) * (hh - 26)]; });
        var path = pts.map(function (p, i) { return (i ? "L" : "M") + p[0].toFixed(1) + " " + p[1].toFixed(1); }).join("");
        return (b.title ? '<p class="pl-ch-t">' + esc(b.title) + "</p>" : "") + '<svg class="pl-line" viewBox="0 0 ' + w + " " + hh + '" preserveAspectRatio="none"><path class="a" d="' + path + "L" + pts[pts.length - 1][0] + " " + (hh - 12) + "L" + pts[0][0] + " " + (hh - 12) + 'Z"/><path class="l" d="' + path + '" pathLength="1"/>' +
          pts.map(function (p) { return '<circle cx="' + p[0].toFixed(1) + '" cy="' + p[1].toFixed(1) + '" r="2.6"/>'; }).join("") + '</svg><div class="pl-axis">' + data.map(function (d) { return "<span>" + esc(d[0]) + "</span>"; }).join("") + "</div>";
      }
      var hor = b.kind === "hbar";
      return (b.title ? '<p class="pl-ch-t">' + esc(b.title) + "</p>" : "") + '<div class="pl-bars' + (hor ? " is-h" : "") + '">' + data.map(function (d, i) {
        return '<div class="pl-bc"><span class="pl-bl">' + esc(d[0]) + '</span><span class="pl-bt"><i style="--v:' + (d[1] / max).toFixed(3) + ";background:" + (b.multi ? colors[i % 8] : "var(--pl-accent)") + '"></i></span>' +
          (b.values === false ? "" : '<span class="pl-bv">' + esc(d[2] || d[1]) + "</span>") + "</div>";
      }).join("") + "</div>";
    },
    hours: function (b) {
      // Time zones: one row per city, a 24-hour strip with working hours, and the chosen moment.
      return '<div class="pl-hours" style="--at:' + (b.at || 0.5) + '">' + b.rows.map(function (r) {
        var off = r[2] || 0, work = "";
        for (var i = 0; i < 24; i++) {
          var hr = (i + off + 24) % 24;
          work += '<i class="' + (hr >= 9 && hr < 18 ? "w" : hr >= 22 || hr < 7 ? "n" : "") + '"></i>';
        }
        return '<div class="pl-hr"><span class="pl-hr-c">' + esc(r[0]) + (r[3] ? "<small>" + esc(r[3]) + "</small>" : "") + '</span><span class="pl-hr-t">' + esc(r[1]) + '</span><span class="pl-hr-s">' + work + "</span></div>";
      }).join("") + '<span class="pl-hr-m"></span></div>';
    },
    // Animations that run when a block appears.
    reveal: function (k, first) {
      var n = typeof k === "number" ? this.blocks[k] : k, b = n && n.__spec, self = this;
      if (!n) return;
      n.classList.remove("is-hidden");
      if (!b) return;
      var t = b.t;
      if (t === "panes") { each(n.querySelectorAll(":scope > .pl-panes > .pl-pane.is-on > .pl-b"), function (sub) { self.reveal(sub); }); return; }
      if (t === "text" && b.type) this.typeInto(n.querySelector("p"), b.text, b.speed);
      if (t === "field" && b.type) this.typeInto(n.querySelector(".pl-fv"), b.value, b.speed);
      if (t === "bar") {
        var bar = n.querySelector(".pl-track i"), from = b.from || 0, to = b.to == null ? 1 : b.to, right = n.querySelector(".pl-prog-r");
        this.anim(b.dur || 1600, function (p) {
          bar.style.setProperty("--v", lerp(from, to, p).toFixed(3));
          if (b.count && right) right.textContent = fmt(b.count, Math.round(lerp(b.c0 || 0, b.c1 || 100, p)));
        }).then(function () { if (b.done && right) right.innerHTML = marks(b.done); }, function () {});
      }
      if (t === "stats") {
        each(n.querySelectorAll("strong"), function (s) {
          var v = s.getAttribute("data-v"), m = /^([^\d-]*)(-?[\d,]*\.?\d+)(.*)$/.exec(v);
          if (!m || b.count === false) return;
          var num = parseFloat(m[2].replace(/,/g, "")), dec = (m[2].split(".")[1] || "").length, comma = m[2].indexOf(",") >= 0;
          self.anim(b.dur || 1400, function (p) {
            var x = (num * easeOut(p)).toFixed(dec);
            if (comma) x = Number(x).toLocaleString("en-US", { minimumFractionDigits: dec, maximumFractionDigits: dec });
            s.textContent = m[1] + x + m[3];
          }).catch(function () {});
        });
      }
      if (t === "dial") {
        var v = n.querySelector("circle.v"), lab = n.querySelector("strong"), from2 = b.from == null ? 1 : b.from, to2 = b.to == null ? 0.9 : b.to;
        this.anim(b.dur || 3000, function (p) {
          v.style.strokeDashoffset = (1 - lerp(from2, to2, p)).toFixed(4);
          if (b.secs != null) {
            var s2 = Math.round(lerp(b.secs, b.secs - (b.run || 3), p)), mm = Math.floor(s2 / 60), ss = s2 % 60;
            lab.textContent = mm + ":" + (ss < 10 ? "0" : "") + ss;
          }
        }).catch(function () {});
      }
      if (t === "chart" || t === "hours" || t === "img" || t === "thumbs" || t === "qr" || t === "barcode" || t === "wave" || t === "swatches" || t === "grid" || t === "list" || t === "rows" || t === "diff" || t === "table") {
        if (!this.ff) { n.classList.remove("is-in"); void n.offsetWidth; }
        n.classList.add("is-in");
      }
    },
    typeInto: function (node, text, speed) {
      if (!node) return Promise.resolve();
      var chars = Array.from(String(text));
      var html = marks(text);
      return this.anim(this.ff ? 0 : clamp(chars.length * (speed || 22), 200, 2600), function (p) {
        var k = Math.round(chars.length * p);
        node.innerHTML = k >= chars.length ? html : esc(chars.slice(0, k).join(""));
      });
    },

    // -------------------------------------------------------------- what happens on the card
    // Selectors: "btn:N" footer button, "btn:B.N" a button in block B, "opt:B.N" a segment or chip,
    // "row:B.N" a row or list item, "chk:B.N" a checkbox, "cell:B.N" a grid cell, "th:B.N" a thumbnail,
    // "b:B" the whole block, "x" the close button, or any CSS selector inside the stage.
    find: function (sel) {
      var c = this.card, st = this.stage, m = /^(btn|opt|row|chk|cell|th|b):(\d+)(?:\.(\d+))?$/.exec(sel);
      if (sel === "x") return c && c.querySelector(".pl-x");
      if (!m) return st.querySelector(sel);
      var kind = m[1], a = +m[2], b2 = m[3] == null ? null : +m[3];
      if (kind === "btn" && b2 == null) return c && c.querySelectorAll(".pl-foot .pl-btn")[a];
      var blk = c && c.querySelector('[data-b="' + a + '"]');
      if (!blk) return null;
      if (kind === "b") return blk;
      var q = { btn: ".pl-btn", opt: ".pl-opt", row: ".pl-row, .pl-li", chk: ".pl-chk", cell: ".pl-cell", th: ".pl-th" }[kind];
      var visible = blk.querySelector(".pl-pane.is-on") || blk;
      return visible.querySelectorAll(q)[b2 || 0] || blk.querySelectorAll(q)[b2 || 0];
    },
    act: async function (a) {
      var op = a[0], self = this;
      switch (op) {
        case "wait": await this.wait(a[1]); break;
        case "move":
          if (typeof a[1] === "string") { var tn = this.find(a[1]); if (tn) await this.moveTo(tn, a[2], a[3], a[4]); }
          else await this.move(this.W * a[1], this.H * a[2], a[3]);
          break;
        case "click": case "hover":
          var node = this.find(a[1]);
          if (!node) break;
          await this.moveTo(node, 0.5, 0.55);
          if (op === "hover") { node.classList.add("is-hover"); break; }
          await this.click();
          this.pressed(node);
          if (a[2]) await this.effects(a[2]);
          break;
        case "type":
          var blk = this.find("b:" + a[1]);
          var fv = blk && (blk.querySelector(".pl-fv") || blk.querySelector("p"));
          if (fv) { blk.classList.add("is-focus"); await this.typeInto(fv, a[2], a[3]); }
          break;
        case "key": await this.key(a[1]); if (a[2]) await this.effects(a[2]); break;
        default: await this.effects([a]);
      }
    },
    pressed: function (node) {
      var c = node.classList;
      if (c.contains("pl-opt")) {
        var grp = node.parentNode, multi = grp.classList.contains("pl-chips");
        if (multi) c.toggle("is-on");
        else each(grp.querySelectorAll(".pl-opt"), function (o) { o.classList.toggle("is-on", o === node); });
        var blk = node.closest(".pl-b"), spec = blk && blk.__spec;
        if (spec && spec.ctl != null) this.swap(spec.ctl, +node.getAttribute("data-i"));
      } else if (c.contains("pl-chk")) {
        c.toggle("is-on");
        var th = node.closest(".pl-th");
        if (th) th.classList.toggle("is-chk", c.contains("is-on"));
      } else if (c.contains("pl-li") || c.contains("pl-cell")) {
        each(node.parentNode.children, function (o) { o.classList.toggle("is-on", o === node); });
      } else if (c.contains("pl-x")) {
        this.closeCard();
      } else {
        c.add("is-press");
        setTimeout(function () { c.remove("is-press"); }, 260);
      }
    },
    // Card and stage changes. Each item is [op, …].
    effects: async function (list) {
      if (!Array.isArray(list[0])) list = [list];
      for (var i = 0; i < list.length; i++) {
        var e = list[i], op = e[0];
        if (op === "toast") await this.toast(e[1]);
        else if (op === "show") { this.reveal(e[1]); await this.wait(e[2] == null ? 300 : e[2]); }
        else if (op === "hide") { var hn = this.find("b:" + e[1]); if (hn) hn.classList.add("is-hidden"); }
        else if (op === "swap") { this.swap(e[1], e[2]); await this.wait(360); }
        else if (op === "set") { this.setBlock(e[1], e[2]); await this.wait(260); }
        else if (op === "close") await this.closeCard();
        else if (op === "card") await this.openCard(e[1]);
        else if (op === "file") await this.addFile(e[1]);
        else if (op === "notify") await this.notify(e[1], e[2]);
        else if (op === "mb") this.mbIcon(e[1], e[2]);
        else if (op === "fx") await this.fxCmd(e[1], e[2]);
        else if (op === "win") this.winTo(e[1]);
        else if (op === "grid") await this.setGrid(e[1]);
        else if (op === "replace") await this.replaceSel(e[1]);
        else if (op === "prop") this.prop(e[1], e[2], e[3]);
        else if (op === "text") { var tx = typeof e[1] === "number" ? this.find("b:" + e[1]) : this.find(e[1]); if (tx) { tx.innerHTML = marks(e[2]); tx.classList.remove("is-flash"); void tx.offsetWidth; tx.classList.add("is-flash"); } }
        else if (op === "rename") await this.rename(e[1]);
        else if (op === "sel") { var sn = this.find(e[1]); if (sn) this.pressed(sn); }
        else if (op === "addClass") { var an = this.find(e[1]); if (an) an.classList.add(e[2]); }
        else if (op === "wait") await this.wait(e[1]);
      }
    },
    swap: function (b, i) {
      var blk = this.find("b:" + b);
      if (!blk) return;
      each(blk.querySelectorAll(":scope > .pl-panes > .pl-pane"), function (p, k) { p.classList.toggle("is-on", k === i); });
      var self = this;
      each(blk.querySelectorAll(":scope > .pl-panes > .pl-pane.is-on > .pl-b"), function (sub) { self.reveal(sub); });
    },
    setBlock: function (b, spec) {
      var old = this.find("b:" + b);
      if (!old) return;
      var was = old.__spec;
      if (was && was.t === spec.t && /^(hours|slider|bar)$/.test(spec.t)) { this.morph(old, spec); return; }
      var n = this.block(spec, b);
      old.parentNode.replaceChild(n, old);
      this.blocks[b] = n;
      this.reveal(b);
    },
    // A new state for a time strip, slider or bar, reached with the block's own transition instead of a redraw.
    morph: function (n, spec) {
      var fresh = this.block(spec, n.getAttribute("data-b"));
      n.__spec = spec;
      function flashText(a, bNew) {
        if (!a || !bNew || a.innerHTML === bNew.innerHTML) return;
        a.innerHTML = bNew.innerHTML;
        a.classList.remove("is-flash"); void a.offsetWidth; a.classList.add("is-flash");
      }
      if (spec.t === "hours") {
        var box = n.querySelector(".pl-hours");
        box.style.setProperty("--at", spec.at || 0.5);
        var rows = n.querySelectorAll(".pl-hr"), nrows = fresh.querySelectorAll(".pl-hr");
        each(nrows, function (r, i) {
          if (!rows[i]) return;
          flashText(rows[i].querySelector(".pl-hr-t"), r.querySelector(".pl-hr-t"));
          rows[i].querySelector(".pl-hr-c").innerHTML = r.querySelector(".pl-hr-c").innerHTML;
          rows[i].querySelector(".pl-hr-s").innerHTML = r.querySelector(".pl-hr-s").innerHTML;
        });
      } else if (spec.t === "slider") {
        n.querySelector(".pl-sl i").style.setProperty("--v", spec.value == null ? 0.5 : spec.value);
        flashText(n.querySelector(".pl-sl-v"), fresh.querySelector(".pl-sl-v"));
        n.querySelector(".pl-lab").innerHTML = fresh.querySelector(".pl-lab").innerHTML;
      } else {
        n.querySelector(".pl-track i").style.setProperty("--v", spec.to == null ? 1 : spec.to);
        n.querySelector(".pl-prog-h").innerHTML = fresh.querySelector(".pl-prog-h").innerHTML;
      }
    },
    closeCard: async function () {
      var c = this.card;
      if (!c) return;
      c.classList.add("is-leaving");
      await this.wait(200);
      c.remove();
      this.card = null;
    },
    toast: async function (text) {
      var t = el("div", "pl-toast", esc(text));
      var r = this.card ? this.rel(this.card) : { x: this.W / 2 - 60, y: this.H / 2, w: 120, h: 0 };
      t.style.left = (r.x + r.w / 2) + "px";
      t.style.top = clamp(r.y + r.h / 2, 60, this.H - 40) + "px";
      this.layer.appendChild(t);
      void t.offsetWidth;
      t.classList.add("is-on");
      await this.wait(900);
      t.classList.remove("is-on");
      await this.wait(200);
      t.remove();
    },
    notify: async function (title, body) {
      var n = el("div", "pl-notice", '<img src="' + esc(this.icon) + '" alt="" width="28" height="28"><div><strong>' + esc(title) + "</strong><span>" + marks(body || "") + "</span></div>");
      this.layer.appendChild(n);
      void n.offsetWidth;
      n.classList.add("is-on");
      await this.wait(400);
    },
    mbIcon: function (kind, on) {
      var x = this.mb.querySelector(".pl-mb-x");
      var old = x.querySelector('[data-k="' + kind + '"]');
      if (on === false) { if (old) old.remove(); return; }
      if (old) return old;
      var span = el("span", "pl-mb-i pl-mb-extra is-" + kind, kind === "rec" ? '<b class="pl-recdot"></b><em>0:00</em>' : (I[kind] || ""));
      span.setAttribute("data-k", kind);
      x.appendChild(span);
      return span;
    },
    addFile: async function (f) {
      var grid = this.stage.querySelector(".pl-grid");
      if (!grid) return;
      each(grid.querySelectorAll(".pl-file.is-sel"), function (x) { x.classList.remove("is-sel"); });
      var n = el("div", "pl-file is-new is-sel", fileIcon(f) + '<span class="pl-fn">' + esc(f.name) + "</span>");
      if (f.replace != null) { var o = grid.children[f.replace]; if (o) { grid.replaceChild(n, o); } else grid.appendChild(n); }
      else if (f.at != null && grid.children[f.at]) grid.insertBefore(n, grid.children[f.at]);
      else grid.appendChild(n);
      await this.wait(500);
    },
    // Replace (⌘↩ on Pop's cards): the result goes back into the document in place of the selection.
    replaceSel: async function (text) {
      var sels = this.stage.querySelectorAll(".pl-sel");
      if (!sels.length) return;
      var first = sels[0], lines = String(text).split("\n");
      // A multi-line result fills the selected lines in order; extra selected lines are removed.
      each(sels, function (x, i) {
        var p = x.closest("p");
        if (i < lines.length) {
          x.className = "pl-sel pl-repl";
          x.innerHTML = i === sels.length - 1 ? lines.slice(i).map(esc).join("<br>") : esc(lines[i]);
        } else if (p && p.textContent === x.textContent) p.remove();
        else x.remove();
      });
      if (this.card) await this.closeCard();
      await this.wait(700);
    },
    // Sets a CSS property on block B (or a selector), so it moves with the block's own transition:
    // ["prop", 2, "--at", 0.4] slides the Time Zones moment, ["prop", 3, "--v", 0.7] a slider or bar.
    prop: function (b, name, value) {
      var n = typeof b === "number" ? this.find("b:" + b) : this.find(b);
      if (!n) return;
      var t = n.querySelector(".pl-hours, .pl-sl i, .pl-track i") || n;
      t.style.setProperty(name, value);
    },
    // Finder: replace every item (after tidying, zipping…), or rename some of them.
    setGrid: async function (files) {
      var grid = this.stage.querySelector(".pl-grid");
      if (!grid) return;
      each(grid.children, function (x) { x.classList.add("is-gone"); });
      await this.wait(280);
      grid.innerHTML = files.map(function (f, i) {
        return '<div class="pl-file is-new' + (f.sel ? " is-sel" : "") + '" style="animation-delay:' + (i * 60) + 'ms">' + fileIcon(f) + '<span class="pl-fn">' + esc(f.name) + "</span></div>";
      }).join("");
      await this.wait(500 + files.length * 60);
    },
    rename: async function (list) {
      var grid = this.stage.querySelector(".pl-grid");
      if (!grid) return;
      for (var i = 0; i < list.length; i++) {
        var f = grid.children[list[i][0]], fn = f && f.querySelector(".pl-fn");
        if (!fn) continue;
        fn.textContent = list[i][1];
        fn.classList.remove("is-flash"); void fn.offsetWidth; fn.classList.add("is-flash");
        await this.wait(120);
      }
    },
    winTo: function (where) {
      if (this.win) this.win.setAttribute("data-at", where);
    },

    // -------------------------------------------------------------- effects on the screen
    // Plugins that work on the screen rather than in a card: drawing, spotlight, zoom, recording…
    fxStart: async function (fx) {
      this.fx = fx;
      var name = fx.name, s = this.s, self = this, L = this.layer, W = this.W, H = this.H;
      var o = el("div", "pl-fx pl-fx-" + name);
      this.fxEl = o;
      if (name === "region") {
        o.innerHTML = '<div class="pl-dim"></div><div class="pl-rgn"><span class="pl-rgn-s"></span></div><div class="pl-hint">' + esc(fx.hint || s.region) + "</div>";
        L.appendChild(o);
        await this.wait(200);
        await this.region(fx);
        return;
      }
      if (name === "pen") {
        o.innerHTML = '<div class="pl-pentools">' + [I.pen, I.marker, I.arrow, I.rect, I.oval].map(function (x, i) { return '<span class="pl-tool' + (i === 0 ? " is-on" : "") + '">' + x + "</span>"; }).join("") +
          '<i class="pl-tsep"></i><span class="pl-col" style="--c:#ff3b30"></span><span class="pl-col" style="--c:#ffcc00"></span><span class="pl-col" style="--c:#0a84ff"></span><i class="pl-tsep"></i><span class="pl-tool">' + I.trash + "</span></div>" +
          '<svg class="pl-ink" viewBox="0 0 ' + W + " " + H + '" width="' + W + '" height="' + H + '"></svg>';
        L.appendChild(o);
        void o.offsetWidth; o.classList.add("is-on");
        await this.wait(400);
        return;
      }
      if (name === "spotlight" || name === "pointer") {
        o.innerHTML = name === "spotlight" ? '<div class="pl-spot"></div>' : "";
        L.appendChild(o);
        this.cursor.classList.toggle("has-halo", name === "pointer");
        this.follow = function (x, y) { o.style.setProperty("--x", x.toFixed(1) + "px"); o.style.setProperty("--y", y.toFixed(1) + "px"); };
        this.place();
        void o.offsetWidth; o.classList.add("is-on");
        await this.wait(500);
        return;
      }
      if (name === "zoom") {
        var clone = this.stage.cloneNode(true);
        clone.className = "pl-zclone";
        each(clone.querySelectorAll(".pl-layer, .pl-cur"), function (x) { x.remove(); });
        o.appendChild(clone);
        L.appendChild(o);
        this.zoomK = 1;
        this.follow = function (x, y) { clone.style.transformOrigin = x.toFixed(1) + "px " + y.toFixed(1) + "px"; };
        this.place();
        await this.wait(60);
        o.classList.add("is-on");
        this.zoomK = fx.k || 2;
        clone.style.transform = "scale(" + this.zoomK + ")";
        await this.wait(500);
        return;
      }
      if (name === "camera") {
        o.innerHTML = '<div class="pl-bubble"><div class="pl-person"><i class="room"></i><i class="lamp"></i><i class="body"></i><i class="head"></i><i class="hair"></i></div></div>';
        L.appendChild(o);
        this.bubble = o.querySelector(".pl-bubble");
        this.bubble.style.left = (W - 150) + "px"; this.bubble.style.top = (H - 150) + "px";
        void o.offsetWidth; o.classList.add("is-on");
        await this.wait(600);
        return;
      }
      if (name === "keys") {
        o.innerHTML = '<div class="pl-keys"></div>';
        L.appendChild(o);
        return;
      }
      if (name === "large") {
        o.innerHTML = '<div class="pl-large"><span>' + esc(fx.text || "") + "</span></div>";
        L.appendChild(o);
        void o.offsetWidth; o.classList.add("is-on");
        var span = o.querySelector("span");
        var size = Math.min(W / Math.max(4, Array.from(fx.text || "").length * 0.62), H * 0.34);
        span.style.fontSize = size.toFixed(0) + "px";
        await this.wait(700);
        return;
      }
      if (name === "tele") {
        o.innerHTML = '<div class="pl-tele"><div class="pl-tele-in">' + (fx.lines || []).map(function (l) { return "<p>" + esc(l) + "</p>"; }).join("") + '</div><span class="pl-tele-h">' + esc(s.telehint) + '</span><span class="pl-tele-sp">' + esc(fx.speed || "1.0×") + "</span></div>";
        L.appendChild(o);
        void o.offsetWidth; o.classList.add("is-on");
        var inner = o.querySelector(".pl-tele-in");
        this.tele = { y: 0, inner: inner, rate: 0.018 };
        this.teleRun();
        await this.wait(600);
        return;
      }
      if (name === "ruler") {
        o.innerHTML = '<div class="pl-freeze"></div><svg class="pl-rl" viewBox="0 0 ' + W + " " + H + '" width="' + W + '" height="' + H + '"><line class="h"/><line class="v"/></svg><span class="pl-rl-l a"></span><span class="pl-rl-l b"></span><div class="pl-rbox"><span></span></div>';
        L.appendChild(o);
        var lh = o.querySelector("line.h"), lv = o.querySelector("line.v"), la = o.querySelector(".pl-rl-l.a"), lb = o.querySelector(".pl-rl-l.b");
        var box = fx.box ? this.rel(this.stage.querySelector(fx.box) || this.win) : { x: 16, y: 40, w: W - 32, h: H - 56 };
        this.follow = function (x, y) {
          var x0 = box.x, x1 = box.x + box.w, y0 = box.y, y1 = box.y + box.h;
          lh.setAttribute("x1", x0); lh.setAttribute("x2", x1); lh.setAttribute("y1", y); lh.setAttribute("y2", y);
          lv.setAttribute("x1", x); lv.setAttribute("x2", x); lv.setAttribute("y1", y0); lv.setAttribute("y2", y1);
          la.textContent = Math.round((x1 - x0) * 2) + " px"; la.style.left = (x + 8) + "px"; la.style.top = (y - 22) + "px";
          lb.textContent = Math.round((y1 - y0) * 2) + " px"; lb.style.left = (x + 8) + "px"; lb.style.top = (y + 8) + "px";
        };
        this.shape("cross");
        this.place();
        void o.offsetWidth; o.classList.add("is-on");
        await this.wait(400);
        return;
      }
      if (name === "recorder") {
        o.innerHTML = '<div class="pl-recbar"><b class="pl-recdot"></b><em>0:00</em><span class="pl-lvl">' + Array(15).join("<i></i>") + '</span><span class="pl-rb">' + I.pause + '</span><span class="pl-rb is-stop">' + I.recdot + '</span></div>';
        L.appendChild(o);
        void o.offsetWidth; o.classList.add("is-on");
        this.recClock(o.querySelector("em"), fx.secs || 8);
        await this.wait(400);
        return;
      }
      if (name === "lock") {
        o.innerHTML = '<div class="pl-lock"><span class="pl-lock-ic">' + I.kbd + "</span><strong>" + esc(fx.title || s.locked) + "</strong><span>" + esc(fx.sub || "") + '</span><div class="pl-dial is-sm"><svg viewBox="0 0 120 120"><circle class="tr" cx="60" cy="60" r="52"/><circle class="v" cx="60" cy="60" r="52" pathLength="1"/></svg><div><strong>60</strong></div></div><span class="pl-btn is-tint">' + esc(fx.btn || s.endClean) + "</span></div>";
        L.appendChild(o);
        void o.offsetWidth; o.classList.add("is-on");
        var v = o.querySelector("circle.v"), lab = o.querySelector(".pl-dial strong");
        this.anim(6000, function (p) { v.style.strokeDashoffset = (p / 10).toFixed(4); lab.textContent = String(60 - Math.floor(p * 6)); }).catch(function () {});
        await this.wait(500);
        return;
      }
      L.appendChild(o);
    },
    region: async function (fx) {
      var o = this.fxEl, W = this.W, H = this.H;
      var t = fx.target ? this.stage.querySelector(fx.target) : null, r;
      if (t) { r = this.rel(t); r = { x: r.x - 8, y: r.y - 8, w: r.w + 16, h: r.h + 16 }; }
      else { var f = fx.rect || [0.2, 0.3, 0.5, 0.4]; r = { x: W * f[0], y: H * f[1], w: W * f[2], h: H * f[3] }; }
      var rg = o.querySelector(".pl-rgn"), lab = o.querySelector(".pl-rgn-s");
      this.shape("cross");
      await this.move(r.x, r.y);
      o.classList.add("is-drag");
      var self = this;
      await this.anim(800, function (p) {
        var e = ease(p), w = r.w * e, h = r.h * e;
        rg.style.cssText = "left:" + r.x + "px;top:" + r.y + "px;width:" + w + "px;height:" + h + "px";
        lab.textContent = Math.round(w * 2) + " × " + Math.round(h * 2);
        self.at = { x: r.x + w, y: r.y + h };
        self.place();
      });
      this.shape("");
      o.classList.add("is-done");
      this.rgn = r;
      await this.wait(fx.keep ? 200 : 380);
      if (!fx.keep) { o.classList.add("is-gone"); this.ringAt = { x: r.x + r.w / 2, y: r.y }; }
    },
    teleRun: function () {
      var self = this, tl = this.tele;
      if (!tl || !tl.inner.isConnected || this.ff) return;
      this.anim(400, function () {}).then(function () {
        if (!self.tele) return;
        tl.y += tl.rate * 400 * (tl.paused ? 0 : 1);
        tl.inner.style.transform = "translateY(" + (-tl.y).toFixed(1) + "px)";
        self.teleRun();
      }, function () {});
    },
    recClock: function (em, secs) {
      var self = this, t0 = 0;
      this.anim(secs * 1000, function (p) {
        var s2 = Math.floor(p * secs);
        if (s2 !== t0) { t0 = s2; em.textContent = "0:" + (s2 < 10 ? "0" : "") + s2; }
      }).catch(function () {});
    },
    fxCmd: async function (cmd, arg) {
      var o = this.fxEl, self = this, W = this.W, H = this.H;
      if (!o) return;
      var ink = o.querySelector(".pl-ink");
      if (cmd === "tool") { each(o.querySelectorAll(".pl-tool"), function (t, i) { t.classList.toggle("is-on", i === arg); }); await this.wait(200); return; }
      if (cmd === "color") { o.style.setProperty("--ink", arg); await this.wait(150); return; }
      if (cmd === "draw" && ink) {
        // arg: {shape: "oval|line|arrow|rect|scribble", target: selector | rect: [x,y,w,h] fractions, color, width}
        var t = arg.target ? this.stage.querySelector(arg.target) : null, r;
        if (t) { r = this.rel(t); r = { x: r.x - 10, y: r.y - 8, w: r.w + 20, h: r.h + 16 }; }
        else { var f = arg.rect || [0.3, 0.4, 0.3, 0.12]; r = { x: W * f[0], y: H * f[1], w: W * f[2], h: H * f[3] }; }
        var pts = [], i, n2 = 40;
        if (arg.shape === "oval") for (i = 0; i <= n2; i++) { var a = -Math.PI * 0.9 + i / n2 * Math.PI * 2.08; pts.push([r.x + r.w / 2 + Math.cos(a) * r.w / 2, r.y + r.h / 2 + Math.sin(a) * r.h / 2]); }
        else if (arg.shape === "rect") pts = [[r.x, r.y], [r.x + r.w, r.y], [r.x + r.w, r.y + r.h], [r.x, r.y + r.h], [r.x, r.y]];
        else if (arg.shape === "scribble") for (i = 0; i <= n2; i++) pts.push([r.x + r.w * i / n2, r.y + r.h / 2 + Math.sin(i / 2.2) * r.h * 0.4]);
        else pts = [[r.x, r.y + r.h], [r.x + r.w, r.y]];
        var d = pts.map(function (p, k) { return (k ? "L" : "M") + p[0].toFixed(1) + " " + p[1].toFixed(1); }).join("");
        var path = D.createElementNS("http://www.w3.org/2000/svg", "path");
        path.setAttribute("d", d);
        path.setAttribute("pathLength", "1");
        path.setAttribute("class", "st" + (arg.hl ? " hl" : ""));
        if (arg.color) path.style.stroke = arg.color;
        ink.appendChild(path);
        if (arg.shape === "arrow") {
          var p1 = pts[0], p2 = pts[1], ang = Math.atan2(p2[1] - p1[1], p2[0] - p1[0]), L2 = 14;
          var head = D.createElementNS("http://www.w3.org/2000/svg", "path");
          head.setAttribute("d", "M" + (p2[0] - L2 * Math.cos(ang - 0.5)).toFixed(1) + " " + (p2[1] - L2 * Math.sin(ang - 0.5)).toFixed(1) + "L" + p2[0].toFixed(1) + " " + p2[1].toFixed(1) + "L" + (p2[0] - L2 * Math.cos(ang + 0.5)).toFixed(1) + " " + (p2[1] - L2 * Math.sin(ang + 0.5)).toFixed(1));
          head.setAttribute("class", "st head");
          if (arg.color) head.style.stroke = arg.color;
          head.style.opacity = "0";
          ink.appendChild(head);
        }
        await this.move(pts[0][0], pts[0][1]);
        this.cursor.classList.add("is-down");
        await Promise.all([this.trace(pts, arg.ms || 900), this.anim(arg.ms || 900, function (p) { path.style.strokeDashoffset = (1 - ease(p)).toFixed(3); })]);
        if (head) head.style.opacity = "1";
        this.cursor.classList.remove("is-down");
        await this.wait(200);
        return;
      }
      if (cmd === "fade" && ink) { ink.classList.add("is-fading"); await this.wait(arg || 900); ink.innerHTML = ""; ink.classList.remove("is-fading"); return; }
      if (cmd === "end") {
        o.classList.add("is-gone"); this.follow = null; this.cursor.classList.remove("has-halo"); this.shape("");
        if (this.tele) this.tele = null;
        await this.wait(350); o.remove(); this.fxEl = null; return;
      }
      if (cmd === "zoom") { this.zoomK = arg; var cl = o.querySelector(".pl-zclone"); if (cl) cl.style.transform = "scale(" + arg + ")"; await this.wait(450); return; }
      if (cmd === "key") {
        var keys = o.querySelector(".pl-keys"), k = el("span", "pl-keycap", esc(arg));
        keys.appendChild(k);
        void k.offsetWidth; k.classList.add("is-on");
        await this.wait(700);
        setTimeout(function () { k.classList.add("is-gone"); setTimeout(function () { k.remove(); }, 400); }, 900);
        return;
      }
      if (cmd === "drag" && this.bubble) {
        var b = this.bubble, x0 = parseFloat(b.style.left), y0 = parseFloat(b.style.top), to = arg || [24, H - 150];
        await this.move(x0 + 60, y0 + 60);
        this.cursor.classList.add("is-down");
        await this.anim(900, function (p) {
          var e = ease(p), x = lerp(x0, to[0], e), y = lerp(y0, to[1], e);
          b.style.left = x + "px"; b.style.top = y + "px";
          self.at = { x: x + 60, y: y + 60 }; self.place();
        });
        this.cursor.classList.remove("is-down");
        return;
      }
      if (cmd === "grow" && this.bubble) { this.bubble.classList.add("is-big"); await this.wait(500); return; }
      if (cmd === "shape" && this.bubble) { this.bubble.classList.add("is-" + arg); await this.wait(500); return; }
      if (cmd === "speed" && this.tele) { this.tele.rate = arg; o.querySelector(".pl-tele-sp").textContent = (arg / 0.018).toFixed(1) + "×"; await this.wait(300); return; }
      if (cmd === "pause" && this.tele) { this.tele.paused = !this.tele.paused; o.classList.toggle("is-paused", this.tele.paused); await this.wait(300); return; }
      if (cmd === "box") {
        var rb = o.querySelector(".pl-rbox"), lab = rb.querySelector("span"), f2 = arg || [0.3, 0.35, 0.36, 0.3];
        var r2 = { x: W * f2[0], y: H * f2[1], w: W * f2[2], h: H * f2[3] };
        this.follow = null;
        each(o.querySelectorAll("line, .pl-rl-l"), function (x) { x.style.opacity = "0"; });
        await this.move(r2.x, r2.y);
        this.cursor.classList.add("is-down");
        await this.anim(800, function (p) {
          var e = ease(p), w = r2.w * e, h = r2.h * e;
          rb.style.cssText = "left:" + r2.x + "px;top:" + r2.y + "px;width:" + w + "px;height:" + h + "px;opacity:1";
          lab.textContent = Math.round(w * 2) + " × " + Math.round(h * 2);
          self.at = { x: r2.x + w, y: r2.y + h }; self.place();
        });
        this.cursor.classList.remove("is-down");
        return;
      }
      if (cmd === "rec") {
        // Screen recording: red frame around the area and a clock in the menu bar.
        o.classList.add("is-rec");
        var mi = this.mbIcon("rec");
        this.recClock(mi.querySelector("em"), arg || 6);
        await this.wait(300);
        return;
      }
      if (cmd === "scroll") {
        // Scrolling screenshot: the page moves under the frame while a long strip grows beside it.
        var page = this.stage.querySelector(".pl-page-in"), strip = o.querySelector(".pl-strip");
        if (!strip) { strip = el("div", "pl-strip", "<i></i>"); o.appendChild(strip); }
        var si = strip.querySelector("i");
        await this.anim(arg || 2400, function (p) {
          if (page) page.style.transform = "translateY(" + (-p * 150).toFixed(1) + "px)";
          si.style.height = (30 + p * 70).toFixed(1) + "%";
        });
        return;
      }
      if (cmd === "dimOff") { o.classList.add("is-gone"); await this.wait(250); return; }
      if (cmd === "saved") {
        // Voice recorder: the bar turns into the saved file, with what you can do next.
        var bar = o.querySelector(".pl-recbar");
        if (!bar) return;
        bar.classList.add("is-saved");
        bar.innerHTML = '<span class="pl-rb is-ok">' + I.check + "</span><span class=\"pl-saved\"><b>" + esc(arg.name) + "</b><small>" + esc(arg.sub || "") + "</small></span>" +
          (arg.btns || []).map(function (x, i) { return '<span class="pl-btn' + (i === 0 ? "" : " is-tint") + '">' + esc(x) + "</span>"; }).join("");
        await this.wait(400);
        return;
      }
    }
  };

  // ------------------------------------------------------------------ the gallery: filter by category and search
  function Gallery(root) {
    var input = root.querySelector(".plg-q"), chips = root.querySelectorAll(".plg-chip"), cards = root.querySelectorAll(".plg-card"),
      groups = root.querySelectorAll(".plg-group"), empty = root.querySelector(".plg-empty"), count = root.querySelector(".plg-count");
    var cat = "all";
    root.classList.add("is-live");
    var ctl = root.querySelector(".plg-ctl");
    if (ctl) ctl.hidden = false;
    function norm(s) { return String(s || "").toLowerCase().replace(/\s+/g, " ").trim(); }
    function apply() {
      var q = norm(input && input.value), n = 0;
      each(cards, function (c) {
        var ok = (cat === "all" || c.getAttribute("data-cat") === cat) && (!q || norm(c.getAttribute("data-k")).indexOf(q) >= 0);
        c.hidden = !ok;
        if (ok) n++;
      });
      each(groups, function (g) { g.hidden = !g.querySelector(".plg-card:not([hidden])"); });
      if (empty) empty.hidden = n > 0;
      if (count) count.textContent = count.getAttribute(n === 1 ? "data-one" : "data-n").replace("%s", n);
    }
    each(chips, function (c) {
      c.addEventListener("click", function () {
        cat = c.getAttribute("data-cat");
        each(chips, function (x) { x.setAttribute("aria-pressed", x === c ? "true" : "false"); });
        apply();
      });
    });
    if (input) {
      input.addEventListener("input", apply);
      input.addEventListener("keydown", function (e) { if (e.key === "Escape") { input.value = ""; apply(); } });
    }
    // Open a category from the address (#text, #developer …).
    var h = (location.hash || "").slice(1);
    each(chips, function (c) { if (c.getAttribute("data-cat") === h) c.click(); });
    apply();
  }

  // ------------------------------------------------------------------ boot
  function init() {
    each(D.querySelectorAll(".plg"), function (g) { try { new Gallery(g); } catch (e) { if (window.console) console.error(e); } });
    var figs = D.querySelectorAll("figure.pla:not(.is-ready)");
    function make(f) { if (f.__p) return; try { f.__p = new Player(f); } catch (e) { if (window.console) console.error(e); } }
    if (!("IntersectionObserver" in window)) { each(figs, make); return; }
    var io = new IntersectionObserver(function (es) {
      es.forEach(function (e) { if (e.isIntersecting) { io.unobserve(e.target); setTimeout(function () { make(e.target); }, 0); } });
    }, { rootMargin: "60% 0px 60% 0px" });
    each(figs, function (f) { io.observe(f); });
  }
  if (D.readyState === "loading") D.addEventListener("DOMContentLoaded", init);
  else init();
})();
