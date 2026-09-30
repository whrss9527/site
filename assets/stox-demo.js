/* whrss.com: an interactive recreation of the Stox menu bar panel.
   Everything here is sample data made up from fixed seeds; nothing is fetched.
   Layout, sizes and wording follow the Stox sources (PanelView, QuoteRow, QuoteChart,
   IntradayChart, OrderBookView, FundFlowView, ProfitCalendarPanel) and its
   en / zh-Hans Localizable.strings.

   Markup: <figure class="sxd" data-lang="en|zh" data-preset="detail|list|search|kline|holdings|calendar"
            data-desk data-icon="…/stox.png">…fallback…</figure> */
(function () {
  "use strict";

  // ------------------------------------------------------------------ strings
  var S = {
    en: {
      demo: "Interactive demo · sample data",
      demoLabel: "Interactive demo of the Stox panel, with sample data",
      cn: "CN %s", hk: "HK %s", us: "US %s",
      closed: "Closed", pre: "Pre", open: "Open",
      search: "Search symbol, name or pinyin; Return to add",
      all: "All", fcn: "A-shares", fhk: "Hong Kong", fus: "US", fhold: "Holdings",
      shown: "%s shown",
      p1d: "1D", p5d: "5D", pday: "Day", pweek: "Week", pmonth: "Month", pbook: "Book", pflow: "Flow",
      n1d: "Intraday chart", n5d: "5-day chart", nday: "Daily candlestick chart", nweek: "Weekly candlestick chart",
      nmonth: "Monthly candlestick chart", nbook: "Order book", nflow: "Fund flow",
      tabHelp: " (use ← → to switch when expanded)",
      open_: "Open", high: "High", low: "Low", prev: "Prev close", change: "Change", volume: "Volume",
      turnover: "Turnover", turnoverRate: "Turnover %", mktCap: "Mkt value", range: "Range", pe: "P/E",
      h52: "52W high", l52: "52W low", limitUp: "Limit up", limitDown: "Limit down", pb: "P/B", volRatio: "Vol ratio",
      shares: "Shares", cost: "Cost", totalPL: "Total P&L", todayPL: "Today’s P&L",
      lots: "%s lots", sh: "%s shares",
      tBJ: "Beijing %s", tHK: "HK %s", delay: " · 15 min delay", tUS: "New York %s", et: " · %s ET",
      holdAlerts: "Holdings & Alerts", alerts: "Alerts", xueqiu: "Xueqiu",
      avg: "Avg %s", nD: "%sD %s", nW: "%sW %s", nM: "%sM %s", bidRatio: "Bid ratio ", main: "Main ",
      rAvg: "  Avg ", rVol: "  Vol ", ohlc: "%s O %s H %s L %s C %s", kVol: " Vol ", mainNet: "Main net inflow ",
      bid: ["Bid 1", "Bid 2", "Bid 3", "Bid 4", "Bid 5"], ask: ["Ask 1", "Ask 2", "Ask 3", "Ask 4", "Ask 5"],
      buyVol: "Buy vol ", sellVol: "Sell vol ", netBids: "Net bids ",
      xl: "Extra large", lg: "Large", md: "Medium", sm: "Small", mainIn: "Main inflow ", out: "Outflow ", prior: "Prior %s days ",
      status: "%s · %s · %s", every: "Every %s s", drag: "Drag to sort", only: "Only %s",
      pillHelp: "%s. Click to switch between % change, change and market cap",
      dPct: "% Change", dChg: "Change", dCap: "Market Cap",
      mktValue: "Mkt value", holdValue: "Holdings value", total: "Total", alloc: "Allocation", hist: "P&L History",
      hideAlloc: "Hide %s",
      CNY: "CNY", HKD: "HKD", USD: "USD",
      week: "This week ", month: "This month ",
      histNote: "Recorded on this Mac after each close; days the Mac was off are missing.",
      calendar: "Calendar", hide: "Hide Amounts", show: "Show Amounts",
      calTitle: "P&L Calendar", calSub: "Today’s P&L recorded after each close, on this Mac only",
      mMonth: "Month", mYear: "Year", back: "Back",
      wd: ["M", "T", "W", "T", "F", "S", "S"],
      monthSum: "This month ", upDown: "%s up · %s down", yearSum: "Full year ", noMonth: "No records this month",
      prevMonth: "Previous Month", nextMonth: "Next Month", prevYear: "Previous Year", nextYear: "Next Year",
      months: ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"],
      mshort: ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
      dayCell: "Day %s", noRecord: "No records",
      added: "Added", none: "No matching securities", tIndex: "Index", tStock: "Stock", tETF: "ETF", tChiNext: "ChiNext", tSTAR: "STAR",
      addTo: "Add %s",
      a11yRow: "%s, %s", a11yPrice: ", price %s", a11yUp: ", up %s%", a11yDown: ", down %s%", a11yFlat: ", unchanged", a11yHold: ", total P&L %s",
      mb: "Stox in the menu bar. Click to open or close the panel; right-click to show only the icon",
      clock: "Wed Sep 30  16:14",
      pinned: "Show in Menu Bar",
      mbHint: "Click the quote in the menu bar to close the panel; right-click it to hide the quotes."
    },
    zh: {
      demo: "可交互演示 · 示例数据",
      demoLabel: "Stox 面板的可交互演示，使用示例数据",
      cn: "A股%s", hk: "港股%s", us: "美股%s",
      closed: "休市", pre: "盘前", open: "交易中",
      search: "搜索代码、名称或拼音，回车添加",
      all: "全部", fcn: "A股", fhk: "港股", fus: "美股", fhold: "持仓",
      shown: "%s 只",
      p1d: "分时", p5d: "五日", pday: "日K", pweek: "周K", pmonth: "月K", pbook: "五档", pflow: "资金",
      n1d: "分时走势", n5d: "五日走势", nday: "日K走势", nweek: "周K走势", nmonth: "月K走势", nbook: "买卖五档", nflow: "资金流向",
      tabHelp: "（展开时也可以用 ← → 切换）",
      open_: "今开", high: "最高", low: "最低", prev: "昨收", change: "涨跌", volume: "成交量",
      turnover: "成交额", turnoverRate: "换手率", mktCap: "市值", range: "振幅", pe: "市盈率",
      h52: "52周最高", l52: "52周最低", limitUp: "涨停", limitDown: "跌停", pb: "市净率", volRatio: "量比",
      shares: "持有", cost: "成本", totalPL: "持仓盈亏", todayPL: "今日盈亏",
      lots: "%s手", sh: "%s股",
      tBJ: "A股时间 %s", tHK: "港股时间 %s", delay: " · 延时约 15 分钟", tUS: "美股时间 %s", et: " · 美东 %s",
      holdAlerts: "持仓与提醒", alerts: "提醒", xueqiu: "雪球",
      avg: "均价 %s", nD: "近 %s 日 %s", nW: "近 %s 周 %s", nM: "近 %s 个月 %s", bidRatio: "委比 ", main: "主力 ",
      rAvg: "  均价 ", rVol: "  量 ", ohlc: "%s 开%s 高%s 低%s 收%s", kVol: " 量", mainNet: "主力净流入 ",
      bid: ["买一", "买二", "买三", "买四", "买五"], ask: ["卖一", "卖二", "卖三", "卖四", "卖五"],
      buyVol: "外盘 ", sellVol: "内盘 ", netBids: "委差 ",
      xl: "超大单", lg: "大单", md: "中单", sm: "小单", mainIn: "主力流入 ", out: "流出 ", prior: "前 %s 日 ",
      status: "%s 更新 · %s · %s", every: "每 %s 秒刷新", drag: "拖动排序", only: "只看%s",
      pillHelp: "%s。点一下切换涨跌幅、涨跌额、总市值",
      dPct: "涨跌幅", dChg: "涨跌额", dCap: "总市值",
      mktValue: "市值", holdValue: "持仓市值", total: "合计", alloc: "持仓分布", hist: "盈亏记录",
      hideAlloc: "收起%s",
      CNY: "人民币", HKD: "港币", USD: "美元",
      week: "本周 ", month: "本月 ",
      histNote: "每个交易日收盘后记在这台 Mac 上，一整天没开机的日子没有。",
      calendar: "日历", hide: "隐藏金额", show: "显示金额",
      calTitle: "盈亏日历", calSub: "每个交易日收盘后记下的今日盈亏，只在这台 Mac 上",
      mMonth: "月", mYear: "年", back: "返回",
      wd: ["一", "二", "三", "四", "五", "六", "日"],
      monthSum: "本月 ", upDown: "赚 %s 天 · 亏 %s 天", upDownY: "赚 %s 个月 · 亏 %s 个月", yearSum: "全年 ", noMonth: "这个月没有记录",
      prevMonth: "上一个月", nextMonth: "下一个月", prevYear: "上一年", nextYear: "下一年",
      dayCell: "%s 日", noRecord: "没有记录",
      added: "已添加", none: "没有找到相关证券", tIndex: "指数", tStock: "股票", tETF: "ETF", tChiNext: "创业板", tSTAR: "科创板",
      addTo: "添加%s",
      a11yRow: "%s，%s", a11yPrice: "，现价 %s", a11yUp: "，上涨 %s%", a11yDown: "，下跌 %s%", a11yFlat: "，平盘", a11yHold: "，持仓盈亏 %s",
      mb: "菜单栏里的 Stox。点一下打开或关闭面板，右键只显示图标",
      clock: "9月30日 周三  16:14",
      pinned: "显示在菜单栏",
      mbHint: "点菜单栏里的行情可以收起面板，右键只显示图标。"
    }
  };

  // ------------------------------------------------------------------ helpers
  function fmt(template) {
    var args = Array.prototype.slice.call(arguments, 1), i = 0;
    return template.replace(/%s/g, function () { return args[i++]; });
  }
  function esc(s) {
    return String(s).replace(/[&<>"]/g, function (c) { return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]; });
  }
  function hash(s) {
    var h = 2166136261;
    for (var i = 0; i < s.length; i++) { h ^= s.charCodeAt(i); h = Math.imul(h, 16777619); }
    return h >>> 0;
  }
  function rng(seed) {   // mulberry32: the same seed always draws the same numbers
    var a = seed >>> 0;
    return function () {
      a = (a + 0x6D2B79F5) >>> 0;
      var t = a;
      t = Math.imul(t ^ (t >>> 15), t | 1);
      t ^= t + Math.imul(t ^ (t >>> 7), t | 61);
      return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
    };
  }
  function gauss(r) { return (r() + r() + r() + r() - 2) * 1.2247; }
  function round(v, d) { var f = Math.pow(10, d); return Math.round(v * f) / f; }
  function fixed(v, d) {
    var s = (Math.round(Math.abs(v) * Math.pow(10, d)) / Math.pow(10, d)).toFixed(d);
    return (v < 0 && Number(s) !== 0 ? "-" : "") + s;
  }
  function signed(v, d) {
    if (Math.abs(v) < 0.5 * Math.pow(10, -d)) return fixed(0, d);
    return (v > 0 ? "+" : "") + fixed(v, d);
  }
  function pad(n) { return (n < 10 ? "0" : "") + n; }
  function hm(minute) { return pad(Math.floor(minute / 60)) + ":" + pad(minute % 60); }
  function dir(v) { return v > 1e-9 ? "up" : (v < -1e-9 ? "down" : "flat"); }

  function Fmt(zh) {
    this.zh = zh;
  }
  Fmt.prototype = {
    percent: function (v) { return signed(v, 2) + "%"; },
    large: function (v, d) {
      d = d === undefined ? 2 : d;
      var m = Math.abs(v);
      if (!this.zh) {
        if (m >= 1e12) return fixed(v / 1e12, d) + "T";
        if (m >= 1e9) return fixed(v / 1e9, d) + "B";
        if (m >= 1e6) return fixed(v / 1e6, d) + "M";
        if (m >= 1e4) return fixed(v / 1e3, d) + "K";
        return fixed(v, 0);
      }
      if (m >= 1e12) return fixed(v / 1e12, d) + "万亿";
      if (m >= 1e8) return fixed(v / 1e8, d) + "亿";
      if (m >= 1e4) return fixed(v / 1e4, d) + "万";
      return fixed(v, 0);
    },
    money: function (v) {
      var m = Math.abs(v);
      if (!this.zh) {
        if (m >= 1e9) return fixed(v / 1e9, 2) + "B";
        if (m >= 1e6) return fixed(v / 1e6, 2) + "M";
        if (m >= 1e5) return fixed(v / 1e3, 2) + "K";
        return fixed(v, 2);
      }
      if (m >= 1e8) return fixed(v / 1e8, 2) + "亿";
      if (m >= 1e5) return fixed(v / 1e4, 2) + "万";
      return fixed(v, 2);
    },
    signedMoney: function (v) { return Math.abs(v) < 0.005 ? fixed(0, 2) : (v > 0 ? "+" : "") + this.money(v); },
    signedLarge: function (v) { return Math.abs(v) < 0.5 ? "0" : (v > 0 ? "+" : "-") + this.large(Math.abs(v)); },
    compact: function (v) {
      var m = Math.abs(v), s = v >= 0.005 ? "+" : (v <= -0.005 ? "-" : "");
      var out;
      if (!this.zh) {
        out = m >= 1e6 ? fixed(m / 1e6, 2) + "M" : m >= 1e4 ? fixed(m / 1e3, 2) + "K" : m >= 100 ? fixed(m, 0) : fixed(m, 2);
      } else {
        out = m >= 1e8 ? fixed(m / 1e8, 2) + "亿" : m >= 1e4 ? fixed(m / 1e4, 2) + "万" : m >= 100 ? fixed(m, 0) : fixed(m, 2);
      }
      return s + out;
    }
  };

  // ------------------------------------------------------------------ markets
  // Minutes on the chart's horizontal axis: lunch takes no room.
  var SESSIONS = { cn: [[570, 690], [780, 900]], hk: [[570, 720], [780, 960]], us: [[570, 960]] };
  function axisLength(region) {
    return SESSIONS[region].reduce(function (n, s) { return n + s[1] - s[0]; }, 0);
  }
  function clockOf(region, offset) {
    var s = SESSIONS[region];
    var first = s[0][1] - s[0][0];
    if (s.length === 1 || offset <= first) return s[0][0] + offset;
    return s[1][0] + offset - first;
  }
  function axisTicks(region) {
    var s = SESSIONS[region], len = axisLength(region);
    var ticks = [{ p: 0, t: hm(s[0][0]) }];
    if (s.length > 1) ticks.push({ p: (s[0][1] - s[0][0]) / len, t: hm(s[0][1]) + "/" + hm(s[1][0]) });
    else ticks.push({ p: 0.5, t: hm(s[0][0] + (s[0][1] - s[0][0]) / 2) });
    ticks.push({ p: 1, t: hm(s[s.length - 1][1]) });
    return ticks;
  }
  var REGION = { sh: "cn", sz: "cn", hk: "hk", us: "us" };
  var BADGE = { sh: ["SH", "沪"], sz: ["SZ", "深"], hk: ["HK", "港"], us: ["US", "美"] };
  var RATES = { CNY: 1, HKD: 0.9138, USD: 7.1326 };
  var CURRENCY = { cn: "CNY", hk: "HKD", us: "USD" };

  // ------------------------------------------------------------------ sample data
  // Prices and previous closes are fixed; everything else (charts, order book, fund
  // flow, P&L history) is drawn from a seed, so every visit shows the same numbers.
  var WATCH = [
    { id: "sh000001", m: "sh", code: "000001", name: "上证指数", py: "szzs", en: "sse composite", index: true, pinned: true,
      price: 3842.19, prev: 3830.32, open: 3831.07, high: 3851.46, low: 3822.83, volume: 4.21e10, amount: 5.46e11, h52: 3899.12, l52: 3040.69 },
    { id: "sz399001", m: "sz", code: "399001", name: "深证成指", py: "szcz", en: "szse component", index: true,
      price: 12887.62, prev: 12901.81, open: 12912.4, high: 12966.35, low: 12836.02, volume: 5.62e10, amount: 7.12e11, h52: 13320.44, l52: 9412.75 },
    { id: "sz399006", m: "sz", code: "399006", name: "创业板指", py: "cybz", en: "chinext", index: true,
      price: 3135.28, prev: 3142.51, open: 3146.12, high: 3161.9, low: 3121.44, volume: 1.94e10, amount: 3.35e11, h52: 3288.1, l52: 1920.6 },
    { id: "hkHSI", m: "hk", code: "HSI", name: "恒生指数", py: "hszs", en: "hang seng", index: true,
      price: 24613.27, prev: 24522.54, open: 24560.1, high: 24688.92, low: 24471.3, volume: 1.62e10, amount: 2.21e11, h52: 25890.2, l52: 19260.43 },
    { id: "usIXIC", m: "us", code: "IXIC", name: "纳斯达克", py: "nsdk", en: "nasdaq", index: true,
      price: 26797.54, prev: 26821.68, open: 26880.2, high: 26944.87, low: 26702.3, volume: 8.9e9, amount: 0, h52: 27410.66, l52: 17220.14 },
    { id: "sh600519", m: "sh", code: "600519", name: "贵州茅台", py: "gzmt", en: "moutai", type: "stock",
      price: 1258.62, prev: 1235.58, open: 1239.53, high: 1268.0, low: 1236.05, volume: 3.833e6, amount: 4.8e9,
      cap: 1.5734e12, pe: 19.32, pb: 6.26, turnover: 0.31, volRatio: 1.36, h52: 1539.98, l52: 1151.01,
      holding: { shares: 100, cost: 1200 }, book: true, flow: true, shape: "afternoon" },
    { id: "hk00700", m: "hk", code: "00700", name: "腾讯控股", py: "txkg", en: "tencent", type: "stock", dec: 3,
      price: 431.0, prev: 432.0, open: 433.8, high: 436.2, low: 428.6, volume: 1.826e7, amount: 7.88e9,
      cap: 3.955e12, pe: 18.7, turnover: 0.2, h52: 508.0, l52: 364.8, holding: { shares: 200, cost: 380 } },
    { id: "usAAPL", m: "us", code: "AAPL", name: "苹果", py: "pg", en: "apple", type: "stock",
      price: 329.4, prev: 338.4, open: 337.1, high: 338.9, low: 327.85, volume: 6.12e7, amount: 2.02e10,
      cap: 4.889e12, pe: 39.62, turnover: 0.41, h52: 351.2, l52: 196.4, holding: { shares: 10, cost: 300 }, pre: 329.6 }
  ];
  var CATALOG = [
    { id: "sh000847", m: "sh", code: "000847", name: "腾讯济安", py: "txja", en: "tencent jian", index: true, price: 3392.8, prev: 3370.56 },
    { id: "hk01698", m: "hk", code: "01698", name: "腾讯音乐-SW", py: "txyy", en: "tencent music", type: "stock", dec: 3, price: 31.5, prev: 32.36 },
    { id: "usTCEHY", m: "us", code: "TCEHY", name: "腾讯控股(ADR)", py: "txkg", en: "tencent adr", type: "stock", price: 54.51, prev: 56.17 },
    { id: "usTME", m: "us", code: "TME", name: "腾讯音乐", py: "txyy", en: "tencent music", type: "stock", price: 7.96, prev: 8.37 },
    { id: "sz000858", m: "sz", code: "000858", name: "五粮液", py: "wly", en: "wuliangye", type: "stock", price: 131.62, prev: 130.05, book: true, flow: true },
    { id: "sz300750", m: "sz", code: "300750", name: "宁德时代", py: "ndsd", en: "catl", type: "chinext", price: 286.4, prev: 281.93, book: true, flow: true },
    { id: "sh600036", m: "sh", code: "600036", name: "招商银行", py: "zsyh", en: "cmb", type: "stock", price: 44.18, prev: 44.31, book: true, flow: true },
    { id: "sz002594", m: "sz", code: "002594", name: "比亚迪", py: "byd", en: "byd", type: "stock", price: 348.9, prev: 342.1, book: true, flow: true },
    { id: "sh510300", m: "sh", code: "510300", name: "沪深300ETF", py: "hs300etf", en: "csi 300 etf", type: "etf", price: 4.512, prev: 4.498, dec: 3, book: true, flow: true },
    { id: "hk09988", m: "hk", code: "09988", name: "阿里巴巴-W", py: "albb", en: "alibaba", type: "stock", dec: 3, price: 152.3, prev: 149.9 },
    { id: "hk01810", m: "hk", code: "01810", name: "小米集团-W", py: "xmjt", en: "xiaomi", type: "stock", dec: 3, price: 56.25, prev: 57.1 },
    { id: "usNVDA", m: "us", code: "NVDA", name: "英伟达", py: "ywd", en: "nvidia", type: "stock", price: 211.36, prev: 207.52 },
    { id: "usTSLA", m: "us", code: "TSLA", name: "特斯拉", py: "tsl", en: "tesla", type: "stock", price: 402.15, prev: 409.33 },
    { id: "usMSFT", m: "us", code: "MSFT", name: "微软", py: "wr", en: "microsoft", type: "stock", price: 538.2, prev: 535.71 }
  ];

  // Fill in what a sample quote leaves out, always the same way for the same symbol.
  function complete(q) {
    if (q.done) return q;
    var r = rng(hash(q.id + "quote"));
    q.region = REGION[q.m];
    q.dec = q.dec || 2;
    q.change = q.price - q.prev;
    q.pct = q.change / q.prev * 100;
    if (!q.open) q.open = round(q.prev * (1 + gauss(r) * 0.004), q.dec);
    if (!q.high) q.high = round(Math.max(q.open, q.price) * (1 + r() * 0.012), q.dec);
    if (!q.low) q.low = round(Math.min(q.open, q.price) * (1 - r() * 0.012), q.dec);
    if (!q.volume) q.volume = (q.region === "cn" ? 2e7 : 8e6) * (0.4 + r());
    if (q.amount === undefined) q.amount = q.volume * (q.price + q.prev) / 2;
    if (!q.index) {
      if (!q.cap) q.cap = q.price * (1e9 + r() * 5e9);
      if (!q.pe) q.pe = round(10 + r() * 40, 2);
      if (!q.turnover) q.turnover = round(0.2 + r() * 1.5, 2);
    }
    if (!q.h52) q.h52 = round(Math.max(q.high, q.prev) * (1.08 + r() * 0.3), q.dec);
    if (!q.l52) q.l52 = round(Math.min(q.low, q.prev) * (0.62 + r() * 0.25), q.dec);
    if (q.region === "cn" && !q.index) {
      var limit = q.type === "chinext" || q.type === "star" ? 0.2 : q.type === "etf" ? 0.1 : 0.1;
      q.limitUp = round(q.prev * (1 + limit), q.dec);
      q.limitDown = round(q.prev * (1 - limit), q.dec);
      if (!q.pb && q.type !== "etf") q.pb = round(1 + r() * 8, 2);
      if (!q.volRatio) q.volRatio = round(0.6 + r() * 1.2, 2);
    }
    q.done = true;
    return q;
  }

  // One trading day's minutes: a walk from the open to the close that touches the high and the low.
  function dayPath(q, seed, region, open, close, high, low, shape) {
    var n = axisLength(region), r = rng(seed), w = [0], v = 0, i;
    // A walk with some momentum, so the line drifts in waves like a real day, plus a little tick noise.
    for (i = 1; i <= n; i++) {
      v = 0.9 * v + gauss(r) * 0.4;
      w.push(w[i - 1] + v + gauss(r) * 0.18);
    }
    var p = [], base, b;
    for (i = 0; i <= n; i++) {
      base = open + (close - open) * i / n;
      b = w[i] - w[n] * i / n;
      if (shape === "afternoon") {  // a quiet morning, a push after lunch, then a gentle fade
        var t = i / n;
        base = open + (close - open) * (t < 0.5 ? t * 0.15 : 0.075 + (t - 0.5) * 1.85);
        base += (high - Math.max(close, open)) * 0.8 * Math.exp(-Math.pow((t - 0.64) / 0.07, 2));
        b *= 0.5;
      }
      base = Math.min(high, Math.max(low, base));
      p.push({ base: base, b: b });
    }
    // Stretch the ups and the downs separately so the line touches the high and the low exactly once.
    var up = Infinity, dn = Infinity;
    for (i = 1; i < n; i++) {
      if (p[i].b > 0) up = Math.min(up, (high - p[i].base) / p[i].b);
      if (p[i].b < 0) dn = Math.min(dn, (low - p[i].base) / p[i].b);
    }
    if (!isFinite(up)) up = 0;
    if (!isFinite(dn)) dn = 0;
    var out = [];
    var total = q.volume || 1e7, vsum = 0, vols = [];
    for (i = 0; i <= n; i++) {
      var price = p[i].base + p[i].b * (p[i].b > 0 ? up : dn);
      if (i === 0) price = open;
      if (i === n) price = close;
      var t2 = i / n;
      var v = (0.35 + 1.6 * Math.pow(2 * t2 - 1, 4) + r() * 0.7) * (i === 0 ? 6 : 1);
      vols.push(v); vsum += v;
      out.push({ i: i, price: round(price, q.dec) });
    }
    var pv = 0, vv = 0;
    for (i = 0; i <= n; i++) {
      out[i].volume = total * vols[i] / vsum;
      pv += out[i].price * out[i].volume; vv += out[i].volume;
      out[i].avg = pv / vv;
    }
    return out;
  }
  function intraday(q) {
    if (!q._intraday) q._intraday = dayPath(q, hash(q.id + "1d"), q.region, q.open, q.price, q.high, q.low, q.shape);
    return q._intraday;
  }

  // Trading days before 2026-09-30 (weekdays; 2026-10-01 starts the National Day holiday).
  function tradingDays(count) {
    var d = new Date(Date.UTC(2026, 8, 30)), out = [];
    while (out.length < count) {
      var wd = d.getUTCDay();
      if (wd !== 0 && wd !== 6) out.unshift(d.getUTCFullYear() + "-" + pad(d.getUTCMonth() + 1) + "-" + pad(d.getUTCDate()));
      d = new Date(d.getTime() - 864e5);
    }
    return out;
  }
  function fiveDay(q) {
    if (q._five) return q._five;
    var days = tradingDays(5), r = rng(hash(q.id + "5d")), close = q.prev, list = [], closes = [];
    for (var k = 3; k >= 0; k--) { closes[k] = close; close = close / (1 + gauss(r) * 0.011); }
    var prev = close, out = [];
    for (var j = 0; j < 5; j++) {
      var dayClose = j === 4 ? q.price : closes[j];
      var open = j === 4 ? q.open : round(prev * (1 + gauss(r) * 0.003), q.dec);
      var hi = j === 4 ? q.high : Math.max(open, dayClose) * (1 + r() * 0.008);
      var lo = j === 4 ? q.low : Math.min(open, dayClose) * (1 - r() * 0.008);
      var pts = j === 4 ? intraday(q) : dayPath(q, hash(q.id + "5d" + j), q.region, open, dayClose, hi, lo);
      out.push({ date: days[j], prev: prev, points: pts });
      prev = dayClose;
    }
    q._five = { days: out, prev: out[0].prev };
    return q._five;
  }

  var MA = [5, 10, 20];
  function klines(q, period) {
    q._k = q._k || {};
    if (q._k[period]) return q._k[period];
    var count = 80, r = rng(hash(q.id + period)), vol = { day: 0.014, week: 0.032, month: 0.07 }[period];
    var labels = [];
    if (period === "day") labels = tradingDays(count);
    else if (period === "week") {
      for (var w = 0; w < count; w++) {
        var d = new Date(Date.UTC(2026, 8, 30) - (w === 0 ? 0 : (w * 7 - 2) * 864e5));
        labels.unshift(d.getUTCFullYear() + "-" + pad(d.getUTCMonth() + 1) + "-" + pad(d.getUTCDate()));
      }
    } else {
      for (var m = 0; m < count; m++) {
        var total = 2026 * 12 + 8 - m;
        labels.unshift(Math.floor(total / 12) + "-" + pad(total % 12 + 1));
      }
    }
    var candles = new Array(count), close = q.price, drift = period === "month" ? 0.008 : 0.0015;
    for (var i = count - 1; i >= 0; i--) {
      var c = { date: labels[i] };
      if (i === count - 1 && period === "day") {
        c.open = q.open; c.high = q.high; c.low = q.low; c.close = q.price; c.volume = q.volume;
        close = q.prev;
      } else {
        c.close = close;
        var open = close / (1 + (gauss(r) * vol + drift * (r() < 0.5 ? 1 : -0.6)));
        if (i === count - 1) open = period === "week" ? q.prev * 0.985 : q.prev * 0.97;
        c.open = open;
        c.high = Math.max(open, close) * (1 + r() * vol * 0.6);
        c.low = Math.min(open, close) * (1 - r() * vol * 0.6);
        c.volume = (q.volume || 1e7) * (period === "day" ? 1 : period === "week" ? 5 : 21) * (0.55 + r() * 0.9);
        close = open * (1 + gauss(r) * vol * 0.25);
      }
      candles[i] = c;
    }
    var averages = MA.map(function (n) {
      return candles.map(function (c, idx) {
        if (idx + 1 < n) return null;
        var s = 0;
        for (var k = idx - n + 1; k <= idx; k++) s += candles[k].close;
        return s / n;
      });
    });
    var shown = 60, cut = count - shown;
    var data = {
      period: period,
      candles: candles.slice(cut),
      averages: averages.map(function (a) { return a.slice(cut); }),
      before: candles[cut - 1].close
    };
    data.changes = data.candles.map(function (c, idx) {
      var p = idx === 0 ? data.before : data.candles[idx - 1].close;
      return (c.close - p) / p * 100;
    });
    q._k[period] = data;
    return data;
  }

  function orderBook(q) {
    if (q._book) return q._book;
    var r = rng(hash(q.id + "book")), tick = Math.pow(10, -q.dec), big = q.price > 500;
    var bids = [], asks = [], p = q.price;
    for (var i = 0; i < 5; i++) {
      bids.push({ price: round(p - tick * (i + (i > 1 && r() < 0.4 ? 1 : 0)), q.dec), volume: 100 * Math.round(big ? 1 + Math.pow(r(), 3) * 40 : 20 + r() * 900) });
      asks.push({ price: round(p + tick * (i + 1), q.dec), volume: 100 * Math.round(big ? 1 + Math.pow(r(), 3) * 12 : 20 + r() * 900) });
    }
    for (i = 2; i < 5; i++) if (bids[i].price >= bids[i - 1].price) bids[i].price = round(bids[i - 1].price - tick, q.dec);
    var bv = bids.reduce(function (s, l) { return s + l.volume; }, 0);
    var av = asks.reduce(function (s, l) { return s + l.volume; }, 0);
    var max = Math.max.apply(null, bids.concat(asks).map(function (l) { return l.volume; }));
    q._book = { bids: bids, asks: asks, bidVolume: bv, askVolume: av, max: max,
      outer: q.volume * 0.523, inner: q.volume * 0.477, imbalance: (bv - av) / (bv + av) * 100 };
    return q._book;
  }

  function fundFlow(q) {
    if (q._flow) return q._flow;
    var r = rng(hash(q.id + "flow")), n = axisLength("cn"), pts = intraday(q);
    var scale = q.amount * 0.06 * (q.pct >= 0 ? 1 : -1);
    var trend = [], v = 0;
    for (var i = 0; i <= n; i++) {
      var move = (pts[i].price - (i ? pts[i - 1].price : q.prev)) / q.prev * 100;
      v += move * Math.abs(scale) * 0.35 + gauss(r) * Math.abs(scale) * 0.012 + scale * 0.0022;
      trend.push({ i: i, value: v, price: pts[i].price });
    }
    var main = v;
    var sup = main * (0.62 + r() * 0.2), bigNet = main - sup;
    var medium = -main * (0.35 + r() * 0.2), small = -main - medium + main * (r() - 0.5) * 0.08;
    var inflow = q.amount * 0.31, outflow = inflow - main;
    var days = [], total = 0;
    for (i = 0; i < 5; i++) { var d = gauss(r) * Math.abs(main) * 0.7; days.push(d); total += d; }
    q._flow = { trend: trend, main: main, sup: sup, big: bigNet, medium: medium, small: small,
      inflow: inflow, outflow: outflow, days: days, total: total };
    return q._flow;
  }

  // Daily P&L recorded after each close, June to September 2026, per currency.
  function profitHistory(items) {
    var days = tradingDays(86), out = { CNY: {}, HKD: {}, USD: {} };
    items.forEach(function (q) {
      if (!q.holding) return;
      var cur = CURRENCY[q.region], r = rng(hash(q.id + "pl")), value = q.holding.shares * q.price;
      days.forEach(function (day, idx) {
        var v = idx === days.length - 1 ? q.change * q.holding.shares : value * gauss(r) * 0.014 + value * 0.0006;
        out[cur][day] = (out[cur][day] || 0) + v;
      });
    });
    return out;
  }

  // ------------------------------------------------------------------ icons (SF Symbols look-alikes)
  var ICON = {
    search: '<svg viewBox="0 0 16 16" aria-hidden="true"><circle cx="6.8" cy="6.8" r="4.6" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="m10.3 10.3 3.6 3.6" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>',
    pin: '<svg viewBox="0 0 16 16" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="1.35" stroke-linejoin="round" stroke-linecap="round"><path d="M5.2 2.2h5.6M6 2.2v4.2L4 9.3h8L10 6.4V2.2M8 9.3v4.9"/></svg>',
    refresh: '<svg viewBox="0 0 16 16" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M12.9 8.4A4.9 4.9 0 1 1 11.3 4.3"/><path d="M11.8 1.8v2.9H8.9"/></svg>',
    sort: '<svg viewBox="0 0 16 16" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="1.45" stroke-linecap="round" stroke-linejoin="round"><path d="M5 13.5V2.8M2.4 5.3 5 2.6l2.6 2.7M11 2.5v10.7M8.4 10.7l2.6 2.7 2.6-2.7"/></svg>',
    gear: '<svg viewBox="0 0 16 16" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="1.35"><circle cx="8" cy="8" r="2.1"/><path d="M8 1.6v1.6M8 12.8v1.6M1.6 8h1.6M12.8 8h1.6M3.5 3.5l1.1 1.1M11.4 11.4l1.1 1.1M3.5 12.5l1.1-1.1M11.4 4.6l1.1-1.1" stroke-linecap="round"/><circle cx="8" cy="8" r="4.6"/></svg>',
    power: '<svg viewBox="0 0 16 16" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"><path d="M8 1.8v6"/><path d="M4.6 4.2a5.2 5.2 0 1 0 6.8 0"/></svg>',
    eye: '<svg viewBox="0 0 16 12" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="1.3"><path d="M1 6s2.6-4.4 7-4.4S15 6 15 6s-2.6 4.4-7 4.4S1 6 1 6Z"/><circle cx="8" cy="6" r="2"/></svg>',
    eyeOff: '<svg viewBox="0 0 16 12" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="1.3" stroke-linecap="round"><path d="M1 6s2.6-4.4 7-4.4S15 6 15 6s-2.6 4.4-7 4.4S1 6 1 6Z"/><path d="M2.5 11 13.5 1"/></svg>',
    up: '<svg viewBox="0 0 10 10" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><path d="m2 6.5 3-3 3 3"/></svg>',
    down: '<svg viewBox="0 0 10 10" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><path d="m2 3.5 3 3 3-3"/></svg>',
    left: '<svg viewBox="0 0 16 16" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><path d="M10 3 5 8l5 5"/></svg>',
    right: '<svg viewBox="0 0 16 16" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><path d="m6 3 5 5-5 5"/></svg>',
    plus: '<svg viewBox="0 0 16 16" aria-hidden="true"><circle cx="8" cy="8" r="7.5" fill="currentColor"/><path d="M8 4.5v7M4.5 8h7" stroke="#fff" stroke-width="1.6" stroke-linecap="round"/></svg>',
    check: '<svg viewBox="0 0 16 16" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><path d="m3 8.5 3.2 3L13 4.5"/></svg>',
    clear: '<svg viewBox="0 0 16 16" aria-hidden="true"><circle cx="8" cy="8" r="7" fill="currentColor"/><path d="m5.5 5.5 5 5m0-5-5 5" stroke="var(--sx-panel-solid)" stroke-width="1.5" stroke-linecap="round"/></svg>',
    case_: '<svg viewBox="0 0 12 11" aria-hidden="true" fill="currentColor"><path d="M4 1.2h4a1 1 0 0 1 1 1V3h1.8A1.2 1.2 0 0 1 12 4.2v5.4a1.2 1.2 0 0 1-1.2 1.2H1.2A1.2 1.2 0 0 1 0 9.6V4.2A1.2 1.2 0 0 1 1.2 3H3v-.8a1 1 0 0 1 1-1Zm.2 1V3h3.6v-.8Z"/></svg>',
    menubar: '<svg viewBox="0 0 16 12" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="1.2"><rect x="1" y="1" width="14" height="10" rx="1.8"/><path d="M1 4.2h14" /><path d="M9.5 2.6h3.5" stroke-width="1.4"/></svg>',
    cc: '<svg viewBox="0 0 18 14" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="1.3"><rect x="1" y="1.5" width="16" height="4.5" rx="2.25"/><circle cx="13.7" cy="3.75" r="1.2" fill="currentColor"/><rect x="1" y="8" width="16" height="4.5" rx="2.25"/><circle cx="4.3" cy="10.25" r="1.2" fill="currentColor"/></svg>'
  };

  // ------------------------------------------------------------------ the demo
  var PRESETS = {
    detail: { expanded: "sh600519", period: "1d" },
    list: {},
    search: { query: { en: "tx", zh: "腾讯" } },
    kline: { expanded: "sh600519", period: "day" },
    book: { expanded: "sh600519", period: "book" },
    holdings: { holdings: true, alloc: true, hist: true, listMax: 184 },
    calendar: { holdings: true, view: "calendar", alloc: true, hist: true }
  };
  var PERIODS = ["1d", "5d", "day", "week", "month", "book", "flow"];
  var counter = 0;
  var VW = 300;  // chart drawing width; the SVGs stretch to the real width

  function Demo(root) {
    this.root = root;
    this.uid = "sxd" + (++counter);
    this.lang = root.getAttribute("data-lang") === "zh" ? "zh" : "en";
    this.s = S[this.lang];
    this.f = new Fmt(this.lang === "zh");
    var p = PRESETS[root.getAttribute("data-preset")] || PRESETS.detail;
    // Holdings are filled in only where the page talks about them, as in the screenshots.
    this.items = WATCH.map(function (q) {
      var item = complete(Object.create(q));
      if (!p.holdings) item.holding = null;
      return item;
    });
    this.st = {
      filter: "all", expanded: p.expanded || null, period: p.period || "1d", display: 0,
      hide: false, alloc: !!p.alloc, hist: !!p.hist, view: p.view || "list",
      query: p.query ? p.query[this.lang] : "", open: true, iconOnly: false,
      calRegion: "CNY", calYear: false, calMonth: 2026 * 12 + 8, calYearValue: 2026
    };
    this.listMax = p.listMax || 430;
    this.desk = root.hasAttribute("data-desk");
    this.icon = root.getAttribute("data-icon") || "";
    this.history = profitHistory(this.items);
    this.build();
  }

  Demo.prototype = {
    t: function (k) { return this.s[k] !== undefined ? this.s[k] : S.en[k]; },
    q: function (id) {
      for (var i = 0; i < this.items.length; i++) if (this.items[i].id === id) return this.items[i];
      return null;
    },
    color: function (d) { return d === "up" ? "var(--sx-up)" : d === "down" ? "var(--sx-down)" : "var(--sx-l2)"; },
    price: function (q, v) { return fixed(v, q.dec); },

    build: function () {
      var r = this.root, self = this;
      r.classList.add("sxd-ready");
      r.setAttribute("role", "group");
      r.setAttribute("aria-label", this.t("demoLabel"));
      r.setAttribute("lang", this.lang === "zh" ? "zh-CN" : "en");
      var noscript = r.querySelector("noscript");
      r.innerHTML = "";
      if (noscript) r.appendChild(noscript);
      var stage = document.createElement("div");
      stage.className = "sxd-stage" + (this.desk ? " sxd-desk" : "");
      r.appendChild(stage);
      var tag = document.createElement("figcaption");
      tag.className = "sxd-tag";
      tag.innerHTML = '<span class="sxd-dot" aria-hidden="true"></span>' + esc(this.t("demo"));
      r.appendChild(tag);
      this.stage = stage;
      r.addEventListener("click", function (e) { self.onClick(e); });
      r.addEventListener("contextmenu", function (e) { self.onContext(e); });
      r.addEventListener("keydown", function (e) { self.onKey(e); });
      r.addEventListener("input", function (e) { self.onInput(e); });
      r.addEventListener("pointermove", function (e) { self.onHover(e); });
      r.addEventListener("pointerleave", function (e) { if (e.target.classList && e.target.classList.contains("sx-chart")) self.endHover(); }, true);
      this.render(true);
    },

    // ---------------------------------------------------------------- render
    render: function (first) {
      var active = document.activeElement, key = null, sel = null;
      if (active && this.root.contains(active)) {
        key = active.getAttribute("data-k");
        if (active.tagName === "INPUT") sel = [active.selectionStart, active.selectionEnd];
      }
      var listEl = this.stage.querySelector(".sx-list"), scroll = listEl ? listEl.scrollTop : 0;
      var html = "";
      if (this.desk) html += this.menubar();
      if (this.st.open) html += '<div class="sx-window"><div class="sx-panel">' + (this.st.view === "calendar" ? this.calendarPanel() : this.watchPanel()) + "</div></div>";
      this.stage.innerHTML = html;
      listEl = this.stage.querySelector(".sx-list");
      if (listEl) {
        if (first && this.st.expanded) {
          var row = listEl.querySelector('[data-row="' + this.st.expanded + '"]');
          if (row) listEl.scrollTop = Math.max(0, row.offsetTop - listEl.clientHeight + row.offsetHeight + 6);
        } else listEl.scrollTop = scroll;
      }
      if (key) {
        var el = this.stage.querySelector('[data-k="' + key + '"]');
        if (el) {
          el.focus({ preventScroll: true });
          if (sel && el.setSelectionRange) el.setSelectionRange(sel[0], sel[1]);
        }
      }
    },

    menubar: function () {
      var q = this.items[0], iconOnly = this.st.iconOnly;
      var ticker = iconOnly
        ? '<span class="sx-mb-icon" aria-hidden="true"><img src="' + esc(this.icon) + '" alt=""></span>'
        : '<span class="sx-mb-name">上证</span> <span style="color:' + this.color(dir(q.change)) + '">' + this.price(q, q.price) + " " + this.f.percent(q.pct) + "</span>";
      return '<div class="sx-mb">' +
        '<button type="button" class="sx-mb-item sx-mb-ticker' + (this.st.open ? " is-open" : "") + '" data-act="mb" data-k="mb" aria-expanded="' + this.st.open + '" aria-label="' + esc(this.t("mb")) + '">' + ticker + "</button>" +
        '<span class="sx-mb-item sx-mb-extra" aria-hidden="true">' + ICON.search + "</span>" +
        '<span class="sx-mb-item sx-mb-extra" aria-hidden="true">' + ICON.cc + "</span>" +
        '<span class="sx-mb-item sx-mb-clock" aria-hidden="true">' + esc(this.t("clock")) + "</span>" +
        "</div>";
    },

    watchPanel: function () {
      var h = this.header();
      h += '<div class="sx-card sx-search"><span class="sx-search-icon">' + ICON.search + "</span>" +
        '<input type="search" data-k="search" class="sx-input" placeholder="' + esc(this.t("search")) + '" aria-label="' + esc(this.t("search")) + '" value="' + esc(this.st.query) + '" autocomplete="off" spellcheck="false">' +
        (this.st.query ? '<button type="button" class="sx-clear" data-act="clear" data-k="clear" aria-label="' + (this.lang === "zh" ? "清除" : "Clear") + '">' + ICON.clear + "</button>" : "") +
        "</div>";
      h += '<div class="sx-content">' + this.content() + "</div>";
      h += this.footer();
      return h;
    },

    content: function () {
      if (this.st.query.trim()) return this.searchResults();
      return this.holdingsCard() + this.watchlist();
    },

    header: function () {
      var t = this, st = function (key, phase, cls) {
        return '<span class="sx-state"><i class="sx-phase ' + cls + '"></i>' + esc(fmt(t.t(key), t.t(phase))) + "</span>";
      };
      return '<div class="sx-card sx-card-strong sx-header">' +
        '<img class="sx-appicon" src="' + esc(this.icon) + '" alt="" width="30" height="30">' +
        '<div class="sx-title"><div class="sx-name">Stox</div><div class="sx-states">' +
        st("cn", "closed", "") + st("hk", "closed", "") + st("us", "pre", "is-pre") +
        "</div></div>" +
        '<span class="sx-iconbtn" aria-hidden="true">' + ICON.pin + "</span>" +
        '<span class="sx-iconbtn" aria-hidden="true">' + ICON.refresh + "</span>" +
        "</div>";
    },

    footer: function () {
      var f = this.st.filter;
      var order = f === "all" ? this.t("drag") : fmt(this.t("only"), this.filterTitle(f));
      var status = fmt(this.t("status"), "16:14:58", fmt(this.t("every"), 5), order);
      return '<div class="sx-footer"><span class="sx-status">' + esc(status) + "</span>" +
        '<span class="sx-iconbtn" aria-hidden="true">' + ICON.sort + "</span>" +
        '<span class="sx-iconbtn" aria-hidden="true">' + ICON.gear + "</span>" +
        '<span class="sx-iconbtn" aria-hidden="true">' + ICON.power + "</span></div>";
    },

    filterTitle: function (f) { return this.t({ all: "all", cn: "fcn", hk: "fhk", us: "fus", hold: "fhold" }[f]); },
    visible: function () {
      var f = this.st.filter;
      return this.items.filter(function (q) {
        return f === "all" || (f === "hold" ? !!q.holding : q.region === f);
      });
    },

    watchlist: function () {
      var self = this, filters = ["all"], regions = {};
      this.items.forEach(function (q) { regions[q.region] = true; });
      ["cn", "hk", "us"].forEach(function (r) { if (regions[r]) filters.push(r); });
      var held = this.items.filter(function (q) { return q.holding; }).length;
      if (held > 0 && held < this.items.length) filters.push("hold");
      var vis = this.visible();
      var bar = '<div class="sx-filters"><div class="sx-chips">' + filters.map(function (f) {
        var on = f === self.st.filter;
        return '<button type="button" class="sx-chip' + (on ? " is-on" : "") + '" data-act="filter" data-v="' + f + '" data-k="f-' + f + '" aria-pressed="' + on + '">' + esc(self.filterTitle(f)) + "</button>";
      }).join("") + '</div><span class="sx-count">' + esc(fmt(this.t("shown"), vis.length)) + "</span></div>";
      var rows = vis.map(function (q) { return self.row(q); }).join("");
      return '<div class="sx-card sx-watch">' + bar + '<div class="sx-list" style="max-height:' + this.listMax + 'px">' + rows + "</div></div>";
    },

    pillText: function (q) {
      if (this.st.display === 0) return this.f.percent(q.pct);
      if (this.st.display === 1) return signed(q.change, q.dec);
      return q.cap ? this.f.large(q.cap) : "--";
    },

    position: function (q) {
      if (!q.holding) return null;
      var h = q.holding, value = h.shares * q.price, basis = h.shares * h.cost;
      return { value: value, total: value - basis, totalPct: basis > 0 ? (value - basis) / basis * 100 : null,
        day: q.change * h.shares, basis: basis };
    },

    row: function (q) {
      var s = this.s, d = dir(q.change), c = this.color(d), exp = this.st.expanded === q.id, pos = this.position(q);
      var badge = BADGE[q.m][this.lang === "zh" ? 1 : 0];
      var extTag = q.pre ? '<span class="sx-ext" style="color:' + this.color(dir(q.pre - q.price)) + '">' + esc(this.t("pre")) + " " + this.f.percent((q.pre - q.price) / q.price * 100) + "</span>" : "";
      var a11y = fmt(this.t("a11yRow"), q.name, q.code) + fmt(this.t("a11yPrice"), this.price(q, q.price)) +
        (d === "up" ? fmt(this.t("a11yUp"), fixed(Math.abs(q.pct), 2)) : d === "down" ? fmt(this.t("a11yDown"), fixed(Math.abs(q.pct), 2)) : this.t("a11yFlat")) +
        (pos && pos.totalPct !== null ? fmt(this.t("a11yHold"), this.f.percent(pos.totalPct)) : "");
      var h = '<div class="sx-row' + (exp ? " is-open" : "") + '" data-row="' + q.id + '">' +
        '<div class="sx-sum">' +
        '<button type="button" class="sx-rowbtn" data-act="row" data-v="' + q.id + '" data-k="r-' + q.id + '" aria-expanded="' + exp + '" aria-label="' + esc(a11y) + '"></button>' +
        '<div class="sx-namecol" aria-hidden="true"><div class="sx-nm"><span class="sx-nmtext">' + esc(q.name) + "</span>" +
        (q.pinned ? '<span class="sx-pinned" title="' + esc(this.t("pinned")) + '">' + ICON.menubar + "</span>" : "") + "</div>" +
        '<div class="sx-codeline"><span class="sx-badge sx-m-' + q.m + '">' + badge + '</span><span class="sx-code">' + esc(q.code) + "</span>" + extTag + "</div></div>" +
        (exp ? '<span class="sx-spark-gap"></span>' : '<span class="sx-spark" aria-hidden="true">' + this.sparkline(q, c) + "</span>") +
        '<div class="sx-pricecol" aria-hidden="true"><div class="sx-price" style="color:' + c + '">' + this.price(q, q.price) + "</div>" +
        (pos ? '<div class="sx-hold" style="color:' + this.color(dir(pos.total)) + '">' + ICON.case_ + (this.st.hide && pos.totalPct === null ? "****" : this.f.percent(pos.totalPct)) + "</div>" : "") +
        "</div>" +
        '<button type="button" class="sx-pill sx-pill-' + d + '" data-act="pill" data-k="p-' + q.id + '" title="' + esc(fmt(this.t("pillHelp"), this.t(["dPct", "dChg", "dCap"][this.st.display]))) + '" aria-label="' + esc(this.pillText(q) + " · " + fmt(this.t("pillHelp"), this.t(["dPct", "dChg", "dCap"][this.st.display]))) + '">' + esc(this.pillText(q)) + "</button>" +
        "</div>";
      if (exp) h += this.detail(q);
      return h + "</div>";
    },

    sparkline: function (q, color) {
      var pts = intraday(q), vals = [], i;
      for (i = 0; i < pts.length; i += 3) vals.push(pts[i].price);
      if (vals.length && (pts.length - 1) % 3) vals.push(pts[pts.length - 1].price);
      var lo = Math.min.apply(null, vals.concat([q.prev])), hi = Math.max.apply(null, vals.concat([q.prev]));
      var min = q.prev * 0.004;
      if (hi - lo < min) { var mid = (hi + lo) / 2; lo = mid - min / 2; hi = mid + min / 2; }
      var y = function (v) { return (20 * (hi - v) / (hi - lo)).toFixed(2); };
      var d = vals.map(function (v, k) { return (k ? "L" : "M") + (40 * k / (vals.length - 1)).toFixed(2) + " " + y(v); }).join("");
      return '<svg viewBox="0 0 40 20" preserveAspectRatio="none"><path d="M0 ' + y(q.prev) + 'H40" class="sx-dash2" vector-effect="non-scaling-stroke"/><path d="' + d + '" fill="none" stroke="' + color + '" stroke-width="1" stroke-linejoin="round" stroke-linecap="round" vector-effect="non-scaling-stroke"/></svg>';
    },

    // ---------------------------------------------------------------- detail
    available: function (q) {
      return PERIODS.filter(function (p) {
        if (p === "book") return !!q.book;
        if (p === "flow") return !!q.flow;
        return true;
      });
    },
    effectivePeriod: function (q) {
      return this.available(q).indexOf(this.st.period) >= 0 ? this.st.period : "1d";
    },

    detail: function (q) {
      var self = this, period = this.effectivePeriod(q), s = this.s;
      var tabs = this.available(q).map(function (p) {
        var on = p === period;
        var help = p === "book" ? (self.lang === "zh" ? "买卖五档和内外盘（展开时也可以用 ← → 切换）" : "Order book and buy/sell volume (use ← → to switch when expanded)") :
          p === "flow" ? self.t("nflow") + self.t("tabHelp") : self.t("n" + p) + self.t("tabHelp");
        return '<button type="button" class="sx-tab' + (on ? " is-on" : "") + '" data-act="period" data-v="' + p + '" data-k="t-' + q.id + "-" + p + '" aria-pressed="' + on + '" title="' + esc(help) + '">' + esc(self.t("p" + p)) + "</button>";
      }).join("");
      var chart = this.chart(q, period);
      var h = '<div class="sx-detail">' +
        '<div class="sx-chartsec" data-chart="' + period + '" data-q="' + q.id + '">' +
        '<div class="sx-chead"><div class="sx-tabs" role="group" aria-label="' + esc(q.name) + '">' + tabs + '</div><span class="sx-csum">' + esc(chart.summary || "") + '</span><span class="sx-readout" aria-hidden="true"></span></div>' +
        '<div class="sx-chart" role="img" aria-label="' + esc(this.t("n" + period) + (chart.summary ? ", " + chart.summary : "")) + '">' + chart.body + "</div>" +
        '<div class="sx-axis" aria-hidden="true">' + chart.axis + "</div></div>";
      var cell = function (title, value, color) {
        return '<div class="sx-cell"><div class="sx-ct">' + esc(title) + '</div><div class="sx-cv"' + (color ? ' style="color:' + color + '"' : "") + ">" + esc(value) + "</div></div>";
      };
      var p = function (v) { return self.price(q, v); };
      var vol = q.region === "cn" ? fmt(this.t("lots"), this.f.large(q.volume / 100)) : fmt(this.t("sh"), this.f.large(q.volume));
      h += '<div class="sx-grid">' +
        cell(this.t("open_"), p(q.open)) + cell(this.t("high"), p(q.high)) + cell(this.t("low"), p(q.low)) + cell(this.t("prev"), p(q.prev)) +
        cell(this.t("change"), signed(q.change, q.dec)) + cell(this.t("volume"), vol) + cell(this.t("turnover"), q.amount > 0 ? this.f.large(q.amount) : "--") +
        cell(this.t("turnoverRate"), q.turnover ? fixed(q.turnover, 2) + "%" : "--") +
        (q.cap ? cell(this.t("mktCap"), this.f.large(q.cap)) : cell(this.t("range"), fixed((q.high - q.low) / q.prev * 100, 2) + "%")) +
        cell(this.t("pe"), q.pe ? fixed(q.pe, 2) : "--") + cell(this.t("h52"), p(q.h52)) + cell(this.t("l52"), p(q.l52));
      if (q.region === "cn" && !q.index) {
        h += cell(this.t("limitUp"), p(q.limitUp), "var(--sx-up)") + cell(this.t("limitDown"), p(q.limitDown), "var(--sx-down)") +
          cell(this.t("pb"), q.pb ? fixed(q.pb, 2) : "--") + cell(this.t("volRatio"), q.volRatio ? fixed(q.volRatio, 2) : "--");
      }
      var pos = this.position(q);
      if (pos) {
        var hide = this.st.hide;
        h += cell(this.t("shares"), hide ? "****" : fmt(this.t("sh"), q.holding.shares)) + cell(this.t("cost"), fixed(q.holding.cost, Math.max(q.dec, 2))) +
          cell(this.t("totalPL"), hide ? "****" : this.f.signedMoney(pos.total), this.color(dir(pos.total))) +
          cell(this.t("todayPL"), hide ? "****" : this.f.signedMoney(pos.day), this.color(dir(pos.day)));
      }
      h += "</div>";
      var time;
      if (q.region === "cn") time = fmt(this.t("tBJ"), "15:00:02");
      else if (q.region === "hk") time = fmt(this.t("tHK"), "16:08:10") + this.t("delay");
      else if (q.pre) time = this.t("pre") + " " + this.price(q, q.pre) + " " + this.f.percent((q.pre - q.price) / q.price * 100) + fmt(this.t("et"), "04:14");
      else time = fmt(this.t("tUS"), "16:00:00");
      h += '<div class="sx-dfoot"><span class="sx-time">' + esc(time) + "</span>" +
        '<span class="sx-link" aria-hidden="true">' + esc(q.index ? this.t("alerts") : this.t("holdAlerts")) + '</span><span class="sx-link" aria-hidden="true">' + esc(this.t("xueqiu")) + "</span></div>";
      return h + "</div>";
    },

    // ---------------------------------------------------------------- charts
    chart: function (q, period) {
      if (period === "1d") return this.intradayChart(q);
      if (period === "5d") return this.fiveDayChart(q);
      if (period === "book") return this.bookChart(q);
      if (period === "flow") return this.flowChart(q);
      return this.klineChart(q, period);
    },

    corners: function (hi, lo, ref, dec) {
      var f = this.f;
      return '<div class="sx-corner sx-tl">' + fixed(hi, dec) + '</div><div class="sx-corner sx-tr">' + f.percent((hi - ref) / ref * 100) + "</div>" +
        '<div class="sx-corner sx-bl">' + fixed(lo, dec) + '</div><div class="sx-corner sx-br">' + f.percent((lo - ref) / ref * 100) + "</div>";
    },
    ticksHtml: function (ticks) {
      return ticks.map(function (t) {
        var style = t.p <= 0.1 ? "left:0" : t.p >= 0.9 ? "right:0" : "left:" + (t.p * 100).toFixed(2) + "%;transform:translateX(-50%)";
        return '<span style="' + style + '">' + esc(t.t) + "</span>";
      }).join("");
    },
    hoverLayer: function () {
      return '<div class="sx-cross" hidden></div><div class="sx-dotm" hidden></div>';
    },

    intradayChart: function (q) {
      var pts = intraday(q), len = axisLength(q.region), H = 56, uid = this.uid + q.id + "g";
      var prices = pts.map(function (p) { return p.price; }).concat([q.prev]).concat(pts.map(function (p) { return p.avg; }));
      var hi = Math.max.apply(null, prices), lo = Math.min.apply(null, prices);
      var span = Math.max(hi - lo, q.prev * 0.004), mid = (hi + lo) / 2, top = mid + span * 0.55, bottom = mid - span * 0.55;
      var y = function (v) { return (top - v) / (top - bottom) * H; };
      var x = function (i) { return i / len * VW; };
      var line = "", avg = "", color = this.color(dir(q.change));
      pts.forEach(function (p, k) { line += (k ? "L" : "M") + x(p.i).toFixed(2) + " " + y(p.price).toFixed(2); avg += (k ? "L" : "M") + x(p.i).toFixed(2) + " " + y(p.avg).toFixed(2); });
      var area = line + "L" + x(pts[pts.length - 1].i).toFixed(2) + " " + H + "L0 " + H + "Z";
      var vols = pts.map(function (p) { return p.volume; }).slice().sort(function (a, b) { return b - a; });
      var cap = vols[0] > vols[1] * 3 ? vols[1] * 1.2 : vols[0];
      var bars = { up: "", down: "", flat: "" }, prev = q.prev, w = Math.max(VW / len - 0.3, 0.8);
      pts.forEach(function (p) {
        var hgt = Math.max(Math.min(p.volume / cap, 1) * H * 0.25, 0.5), d = dir(p.price - prev);
        bars[d] += "M" + (x(p.i) - w / 2).toFixed(2) + " " + (H - hgt).toFixed(2) + "h" + w.toFixed(2) + "v" + hgt.toFixed(2) + "h" + (-w).toFixed(2) + "Z";
        prev = p.price;
      });
      var plo = Math.min.apply(null, prices), phi = Math.max.apply(null, prices);
      var svg = '<svg viewBox="0 0 ' + VW + " " + H + '" preserveAspectRatio="none" aria-hidden="true">' +
        '<defs><linearGradient id="' + uid + '" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="' + color + '" stop-opacity=".22"/><stop offset="1" stop-color="' + color + '" stop-opacity=".02"/></linearGradient></defs>' +
        '<path d="' + bars.up + '" fill="var(--sx-up)" opacity=".3"/><path d="' + bars.down + '" fill="var(--sx-down)" opacity=".3"/><path d="' + bars.flat + '" fill="var(--sx-l2)" opacity=".3"/>' +
        '<path d="' + area + '" fill="url(#' + uid + ')"/>' +
        '<path d="M0 ' + y(q.prev).toFixed(2) + "H" + VW + '" class="sx-dash" vector-effect="non-scaling-stroke"/>' +
        '<path d="' + avg + '" fill="none" stroke="var(--sx-orange)" stroke-opacity=".9" stroke-width=".9" stroke-linejoin="round" vector-effect="non-scaling-stroke"/>' +
        '<path d="' + line + '" fill="none" stroke="' + color + '" stroke-width="1.2" stroke-linejoin="round" stroke-linecap="round" vector-effect="non-scaling-stroke"/></svg>';
      var self = this;
      this.hover = {
        n: len, pos: function (fr) { var i = Math.round(fr * len); return Math.min(Math.max(i, 0), pts.length - 1); },
        x: function (i) { return pts[i].i / len; }, y: function (i) { return y(pts[i].price) / H; }, color: color,
        text: function (i) {
          var p = pts[i], vol = p.volume;
          return hm(clockOf(q.region, p.i)) + "  " + self.price(q, p.price) + "  " + self.f.percent((p.price - q.prev) / q.prev * 100) +
            self.t("rAvg") + self.price(q, p.avg) + self.t("rVol") + (q.region === "cn" ? fmt(self.t("lots"), self.f.large(vol / 100)) : fmt(self.t("sh"), self.f.large(vol)));
        }
      };
      return {
        body: svg + this.corners(phi, plo, q.prev, q.dec) + this.hoverLayer(),
        axis: this.ticksHtml(axisTicks(q.region)),
        summary: fmt(this.t("avg"), this.price(q, pts[pts.length - 1].avg))
      };
    },

    fiveDayChart: function (q) {
      var data = fiveDay(q), len = axisLength(q.region), H = 56, uid = this.uid + q.id + "g5", self = this;
      var all = [];
      data.days.forEach(function (d) { d.points.forEach(function (p) { all.push(p.price, p.avg); }); });
      all.push(data.prev);
      var hi = Math.max.apply(null, all), lo = Math.min.apply(null, all);
      var span = Math.max(hi - lo, data.prev * 0.004), mid = (hi + lo) / 2, top = mid + span * 0.55, bottom = mid - span * 0.55;
      var y = function (v) { return (top - v) / (top - bottom) * H; };
      var dw = VW / 5, line = "", avg = "", flat = [], vbars = "";
      data.days.forEach(function (d, j) {
        var step = 4;
        d.points.forEach(function (p, k) {
          if (k % step && k !== d.points.length - 1) return;
          var xx = (j * dw + p.i / len * dw).toFixed(2);
          line += (line ? "L" : "M") + xx + " " + y(p.price).toFixed(2);
          avg += (k === 0 ? "M" : "L") + xx + " " + y(p.avg).toFixed(2);
          flat.push({ day: j, p: p });
        });
        for (var b = 0; b < 12; b++) {
          var seg = d.points.slice(Math.floor(b * len / 12), Math.floor((b + 1) * len / 12) + 1);
          var v = seg.reduce(function (s, p) { return s + p.volume; }, 0);
          d["v" + b] = v;
        }
      });
      var maxV = 0;
      data.days.forEach(function (d) { for (var b = 0; b < 12; b++) maxV = Math.max(maxV, d["v" + b]); });
      data.days.forEach(function (d, j) {
        for (var b = 0; b < 12; b++) {
          var hgt = Math.max(d["v" + b] / maxV * H * 0.25, 0.5), bw = dw / 12;
          vbars += "M" + (j * dw + b * bw + bw * 0.15).toFixed(2) + " " + (H - hgt).toFixed(2) + "h" + (bw * 0.7).toFixed(2) + "v" + hgt.toFixed(2) + "h" + (-bw * 0.7).toFixed(2) + "Z";
        }
      });
      var last = data.days[4].points[data.days[4].points.length - 1].price, d5 = dir(last - data.prev), color = this.color(d5);
      var seps = "";
      for (var j = 1; j < 5; j++) seps += "M" + (j * dw).toFixed(2) + " 0V" + H;
      var svg = '<svg viewBox="0 0 ' + VW + " " + H + '" preserveAspectRatio="none" aria-hidden="true">' +
        '<defs><linearGradient id="' + uid + '" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="' + color + '" stop-opacity=".22"/><stop offset="1" stop-color="' + color + '" stop-opacity=".02"/></linearGradient></defs>' +
        '<path d="' + vbars + '" fill="var(--sx-l1)" opacity=".16"/>' +
        '<path d="' + seps + '" stroke="var(--sx-l2)" stroke-opacity=".5" stroke-width=".5" vector-effect="non-scaling-stroke"/>' +
        '<path d="' + line + "L" + VW + " " + H + "L0 " + H + 'Z" fill="url(#' + uid + ')"/>' +
        '<path d="M0 ' + y(data.prev).toFixed(2) + "H" + VW + '" class="sx-dash" vector-effect="non-scaling-stroke"/>' +
        '<path d="' + avg + '" fill="none" stroke="var(--sx-orange)" stroke-opacity=".9" stroke-width=".8" vector-effect="non-scaling-stroke"/>' +
        '<path d="' + line + '" fill="none" stroke="' + color + '" stroke-width="1.1" stroke-linejoin="round" vector-effect="non-scaling-stroke"/></svg>';
      this.hover = {
        pos: function (fr) { return Math.min(Math.max(Math.round(fr * (flat.length - 1)), 0), flat.length - 1); },
        x: function (i) { return (flat[i].day + flat[i].p.i / len) / 5; }, y: function (i) { return y(flat[i].p.price) / H; }, color: color,
        text: function (i) {
          var f = flat[i], day = data.days[f.day];
          return day.date.slice(5) + "  " + hm(clockOf(q.region, f.p.i)) + "  " + self.price(q, f.p.price) + "  " +
            self.f.percent((f.p.price - day.prev) / day.prev * 100) + self.t("rAvg") + self.price(q, f.p.avg);
        }
      };
      return {
        body: svg + this.corners(Math.max.apply(null, all), Math.min.apply(null, all), data.prev, q.dec) + this.hoverLayer(),
        axis: this.ticksHtml(data.days.map(function (d, k) { return { p: (k + 0.5) / 5, t: d.date.slice(5) }; })),
        summary: fmt(this.t("nD"), 5, this.f.percent((last - data.prev) / data.prev * 100))
      };
    },

    klineChart: function (q, period) {
      var data = klines(q, period), c = data.candles, n = c.length, H = 45, self = this;
      var vals = [];
      c.forEach(function (k) { vals.push(k.high, k.low); });
      data.averages.forEach(function (a) { a.forEach(function (v) { if (v !== null) vals.push(v); }); });
      var hiV = Math.max.apply(null, vals), loV = Math.min.apply(null, vals), span = Math.max(hiV - loV, hiV * 0.01);
      var top = hiV + span * 0.06, bottom = loV - span * 0.06;
      var y = function (v) { return (top - v) / (top - bottom) * H; };
      var slot = VW / Math.max(n, 40), bw = Math.max(1, Math.min(slot * 0.7, 8));
      var cx = function (i) { return (i + 0.5) * slot; };
      var maxVol = Math.max.apply(null, c.map(function (k) { return k.volume; }));
      var parts = { up: { w: "", b: "", v: "" }, down: { w: "", b: "", v: "" }, flat: { w: "", b: "", v: "" } };
      c.forEach(function (k, i) {
        var d = dir(k.close - k.open), p = parts[d], x = cx(i);
        var bt = y(Math.max(k.open, k.close)), bb = Math.max(y(Math.min(k.open, k.close)), bt + 0.8);
        p.w += "M" + x.toFixed(2) + " " + y(k.high).toFixed(2) + "V" + bt.toFixed(2) + "M" + x.toFixed(2) + " " + bb.toFixed(2) + "V" + y(k.low).toFixed(2);
        p.b += "M" + (x - bw / 2).toFixed(2) + " " + bt.toFixed(2) + "h" + bw.toFixed(2) + "V" + bb.toFixed(2) + "h" + (-bw).toFixed(2) + "Z";
        var vh = Math.max(k.volume / maxVol * H * 0.25, 0.5);
        p.v += "M" + (x - bw / 2).toFixed(2) + " " + (H - vh).toFixed(2) + "h" + bw.toFixed(2) + "v" + vh.toFixed(2) + "h" + (-bw).toFixed(2) + "Z";
      });
      var svg = '<svg viewBox="0 0 ' + VW + " " + H + '" preserveAspectRatio="none" aria-hidden="true">';
      ["up", "down", "flat"].forEach(function (d) {
        var col = self.color(d);
        svg += '<path d="' + parts[d].v + '" fill="' + col + '" opacity=".28"/>';
      });
      ["up", "down", "flat"].forEach(function (d) {
        var col = self.color(d);
        svg += '<path d="' + parts[d].w + '" stroke="' + col + '" stroke-width="1" vector-effect="non-scaling-stroke"/><path d="' + parts[d].b + '" fill="' + col + '"/>';
      });
      var maColors = ["var(--sx-orange)", "var(--sx-blue)", "var(--sx-purple)"];
      data.averages.forEach(function (a, li) {
        var path = "", drawing = false;
        a.forEach(function (v, i) {
          if (v === null) { drawing = false; return; }
          path += (drawing ? "L" : "M") + cx(i).toFixed(2) + " " + y(v).toFixed(2);
          drawing = true;
        });
        svg += '<path d="' + path + '" fill="none" stroke="' + maColors[li] + '" stroke-opacity=".9" stroke-width=".8" stroke-linejoin="round" vector-effect="non-scaling-stroke"/>';
      });
      svg += "</svg>";
      var legend = function (i) {
        return data.averages.map(function (a, li) {
          return '<span style="color:' + maColors[li] + '">MA' + MA[li] + " " + (a[i] === null ? "--" : self.price(q, a[i])) + "</span>";
        }).join("");
      };
      var label = function (k) { return period === "month" ? k.date.slice(0, 7) : k.date; };
      this.hover = {
        pos: function (fr) { var i = Math.floor(fr * VW / slot); return Math.min(Math.max(i, 0), n - 1); },
        x: function (i) { return cx(i) / VW; }, y: null, legend: legend,
        text: function (i) {
          var k = c[i];
          return fmt(self.t("ohlc"), label(k), self.price(q, k.open), self.price(q, k.high), self.price(q, k.low), self.price(q, k.close)) +
            " " + self.f.percent(data.changes[i]) + self.t("kVol") + (q.region === "cn" ? fmt(self.t("lots"), self.f.large(k.volume / 100)) : fmt(self.t("sh"), self.f.large(k.volume)));
        }
      };
      var idx = [0, Math.floor(n / 2), n - 1];
      var total = (c[n - 1].close - data.before) / data.before * 100;
      var sumKey = { day: "nD", week: "nW", month: "nM" }[period];
      return {
        body: '<div class="sx-legend">' + legend(n - 1) + '</div><div class="sx-kbox">' + svg + this.hoverLayer() + "</div>",
        axis: this.ticksHtml(idx.map(function (i) { return { p: cx(i) / VW, t: label(c[i]) }; })),
        summary: fmt(this.t(sumKey), n, this.f.percent(total))
      };
    },

    bookChart: function (q) {
      var b = orderBook(q), self = this;
      this.hover = null;
      var side = function (labels, levels, barColor, edge) {
        return '<div class="sx-side">' + levels.map(function (l, i) {
          var fr = (l.volume / b.max * 100).toFixed(1);
          return '<div class="sx-lvl" role="presentation"><i style="width:' + fr + "%;" + edge + ":0;background:" + barColor + '"></i>' +
            '<span class="sx-lk">' + esc(labels[i]) + '</span><span class="sx-lp" style="color:' + self.color(dir(l.price - q.prev)) + '">' + self.price(q, l.price) + '</span><span class="sx-lv">' + self.f.large(l.volume / 100) + "</span></div>";
        }).join("") + "</div>";
      };
      var lots = function (v) { return fmt(self.t("lots"), self.f.large(v / 100)); };
      var diff = (b.bidVolume - b.askVolume) / 100;
      return {
        body: '<div class="sx-book">' + side(this.s.bid, b.bids, "var(--sx-up)", "right") + side(this.s.ask, b.asks, "var(--sx-down)", "left") + "</div>",
        axis: '<span style="left:0">' + esc(this.t("buyVol") + lots(b.outer) + "  " + this.t("sellVol") + lots(b.inner)) + '</span><span style="right:0">' + esc(this.t("netBids") + (diff >= 0.5 ? "+" : "") + this.f.large(diff)) + "</span>",
        summary: this.t("bidRatio") + this.f.percent(b.imbalance)
      };
    },

    flowChart: function (q) {
      var fl = fundFlow(q), len = axisLength("cn"), H = 56, self = this, uid = this.uid + q.id + "fc";
      var vals = fl.trend.map(function (p) { return p.value; });
      var hi = Math.max(0, Math.max.apply(null, vals)), lo = Math.min(0, Math.min.apply(null, vals));
      if (hi === lo) hi = lo + 1;
      var y = function (v) { return (hi - v) / (hi - lo) * H; }, zero = y(0);
      var line = fl.trend.map(function (p, k) { return (k ? "L" : "M") + (p.i / len * VW).toFixed(2) + " " + y(p.value).toFixed(2); }).join("");
      var area = line + "L" + (fl.trend[fl.trend.length - 1].i / len * VW).toFixed(2) + " " + zero.toFixed(2) + "L0 " + zero.toFixed(2) + "Z";
      var svg = '<svg viewBox="0 0 ' + VW + " " + H + '" preserveAspectRatio="none" aria-hidden="true"><defs>' +
        '<clipPath id="' + uid + 'a"><rect x="0" y="0" width="' + VW + '" height="' + zero.toFixed(2) + '"/></clipPath>' +
        '<clipPath id="' + uid + 'b"><rect x="0" y="' + zero.toFixed(2) + '" width="' + VW + '" height="' + (H - zero).toFixed(2) + '"/></clipPath></defs>' +
        '<path d="M0 ' + zero.toFixed(2) + "H" + VW + '" class="sx-dash" vector-effect="non-scaling-stroke"/>' +
        '<g clip-path="url(#' + uid + 'a)"><path d="' + area + '" fill="var(--sx-up)" fill-opacity=".16"/><path d="' + line + '" fill="none" stroke="var(--sx-up)" stroke-width="1.2" vector-effect="non-scaling-stroke"/></g>' +
        '<g clip-path="url(#' + uid + 'b)"><path d="' + area + '" fill="var(--sx-down)" fill-opacity=".16"/><path d="' + line + '" fill="none" stroke="var(--sx-down)" stroke-width="1.2" vector-effect="non-scaling-stroke"/></g></svg>';
      var row = function (title, v) {
        return '<div class="sx-frow"><span>' + esc(title) + '</span><span style="color:' + self.color(dir(v)) + '">' + self.f.signedLarge(v) + "</span></div>";
      };
      var corners = (hi > 0 ? '<div class="sx-corner sx-tl">' + this.f.signedLarge(Math.max.apply(null, vals.concat([0]))) + "</div>" : "") +
        (lo < 0 ? '<div class="sx-corner sx-bl">' + this.f.signedLarge(Math.min.apply(null, vals.concat([0]))) + "</div>" : "");
      this.hover = {
        pos: function (fr) { return Math.min(Math.max(Math.round(fr * len), 0), fl.trend.length - 1); },
        x: function (i) { return fl.trend[i].i / len; }, y: function (i) { return y(fl.trend[i].value) / H; },
        color: null, dotColor: function (i) { return self.color(dir(fl.trend[i].value)); },
        text: function (i) {
          var p = fl.trend[i];
          return hm(clockOf("cn", p.i)) + "  " + self.t("mainNet") + self.f.signedLarge(p.value) + "  " + self.price(q, p.price);
        }
      };
      return {
        body: '<div class="sx-flow"><div class="sx-fchart">' + svg + corners + this.hoverLayer() + '</div><div class="sx-fbreak">' +
          row(this.t("xl"), fl.sup) + row(this.t("lg"), fl.big) + row(this.t("md"), fl.medium) + row(this.t("sm"), fl.small) + "</div></div>",
        axis: '<span style="left:0">' + esc(this.t("mainIn") + this.f.large(fl.inflow) + "  " + this.t("out") + this.f.large(fl.outflow)) + '</span><span style="right:0">' +
          esc(fmt(this.t("prior"), 5) + this.f.signedLarge(fl.total)) + "</span>",
        summary: this.t("main") + this.f.signedLarge(fl.main)
      };
    },

    // ---------------------------------------------------------------- holdings
    summaries: function () {
      var out = {}, order = [];
      this.visible().forEach(function (q) {
        if (!q.holding) return;
        var cur = CURRENCY[q.region], h = q.holding;
        if (!out[cur]) { out[cur] = { cur: cur, value: 0, day: 0, total: 0, basis: 0, count: 0 }; order.push(cur); }
        var s = out[cur], value = h.shares * q.price;
        s.value += value; s.day += q.change * h.shares; s.basis += h.shares * h.cost; s.total += value - h.shares * h.cost; s.count++;
      });
      return ["CNY", "HKD", "USD"].filter(function (c) { return out[c]; }).map(function (c) { return out[c]; });
    },

    holdingsCard: function () {
      var sums = this.summaries(), self = this, hide = this.st.hide;
      if (!sums.length) return "";
      var filtered = this.st.filter !== "all", showCur = sums.length > 1 || filtered;
      var amount = function (t) { return hide ? "****" : t; };
      var profit = function (v, pct) {
        return '<div class="sx-hv" style="color:' + self.color(dir(v)) + '"><div class="sx-hbig">' + esc(amount(self.f.signedMoney(v))) + '</div><div class="sx-hpct">' + self.f.percent(pct) + "</div></div>";
      };
      var row = function (title, s) {
        return (showCur ? '<div class="sx-hcur">' + esc(title) + "</div>" : "") + profit(s.day, s.day / (s.value - s.day) * 100) + profit(s.total, s.total / s.basis * 100) +
          '<div class="sx-hval">' + esc(amount(self.f.money(s.value))) + "</div>";
      };
      var h = '<div class="sx-card sx-holdings"><div class="sx-hgrid' + (showCur ? " has-cur" : "") + '">';
      if (showCur) h += '<div class="sx-hcur sx-hhead">' + (filtered ? esc(this.filterTitle(this.st.filter)) : "") + "</div>";
      h += '<div class="sx-hhead">' + esc(this.t("todayPL")) + '</div><div class="sx-hhead">' + esc(this.t("totalPL")) + '</div><div class="sx-hhead sx-hvalhead">' +
        esc(showCur ? this.t("mktValue") : this.t("holdValue")) +
        '<button type="button" class="sx-eye" data-act="eye" data-k="eye" aria-pressed="' + hide + '" aria-label="' + esc(hide ? this.t("show") : this.t("hide")) + '">' + (hide ? ICON.eyeOff : ICON.eye) + "</button></div>";
      sums.forEach(function (s) { h += row(self.t(s.cur), s); });
      if (sums.length > 1) {
        var tot = { value: 0, day: 0, total: 0, basis: 0 };
        sums.forEach(function (s) { var r = RATES[s.cur]; tot.value += s.value * r; tot.day += s.day * r; tot.total += s.total * r; tot.basis += s.basis * r; });
        h += '<div class="sx-hdiv"></div>' + row(this.t("total"), tot);
      }
      h += "</div>";
      var count = sums.reduce(function (n, s) { return n + s.count; }, 0);
      if (count > 1) {
        h += this.disclosure("alloc", this.t("alloc"));
        if (this.st.alloc) {
          var entries = [], totalV = 0;
          this.visible().forEach(function (q) {
            if (!q.holding) return;
            var v = q.holding.shares * q.price * RATES[CURRENCY[q.region]];
            entries.push({ name: q.name, v: v }); totalV += v;
          });
          entries.sort(function (a, b) { return b.v - a.v; });
          h += '<div class="sx-alloc">' + entries.map(function (e) {
            var share = e.v / totalV * 100;
            return '<div class="sx-arow"><span class="sx-aname">' + esc(e.name) + '</span><span class="sx-abar"><i style="width:' + share.toFixed(2) + '%"></i></span><span class="sx-apct">' + fixed(share, 1) + "%</span></div>";
          }).join("") + "</div>";
        }
      }
      if (!filtered) {
        h += this.disclosure("hist", this.t("hist"));
        if (this.st.hist) {
          h += '<div class="sx-hist">' + sums.map(function (s) { return self.historyRow(s.cur); }).join("") + "</div>" +
            '<div class="sx-histfoot"><span>' + esc(this.t("histNote")) + '</span><button type="button" class="sx-linkbtn" data-act="cal" data-k="cal">' + esc(this.t("calendar")) + "</button></div>";
        }
      }
      return h + "</div>";
    },

    disclosure: function (key, title) {
      var on = this.st[key];
      return '<button type="button" class="sx-disc" data-act="' + key + '" data-k="d-' + key + '" aria-expanded="' + on + '">' + esc(title) + (on ? ICON.up : ICON.down) + "</button>";
    },

    historyRow: function (cur) {
      var rec = this.history[cur], days = Object.keys(rec).sort(), recent = days.slice(-20), self = this;
      var vals = recent.map(function (d) { return rec[d]; }), big = Math.max.apply(null, vals.map(Math.abs));
      var W = 100, H = 18, slot = W / Math.max(vals.length, 20), bw = Math.max(1, Math.min(slot - 1, 6)), mid = H / 2;
      var bars = { up: "", down: "", flat: "" };
      vals.forEach(function (v, i) {
        var h = Math.max(Math.abs(v) / big * (mid - 1), 0.5), x = i * slot + (slot - bw) / 2;
        bars[dir(v)] += "M" + x.toFixed(2) + " " + (v >= 0 ? mid - h : mid).toFixed(2) + "h" + bw.toFixed(2) + "v" + h.toFixed(2) + "h" + (-bw).toFixed(2) + "Z";
      });
      var week = 0, month = 0;
      days.forEach(function (d) { if (d >= "2026-09-28") week += rec[d]; if (d >= "2026-09-01") month += rec[d]; });
      var amt = function (v) { return self.st.hide ? "****" : self.f.signedMoney(v); };
      return '<div class="sx-hrow"><span class="sx-hrcur">' + esc(this.t(cur)) + '</span><svg class="sx-bars" viewBox="0 0 ' + W + " " + H + '" preserveAspectRatio="none" aria-hidden="true">' +
        '<path d="M0 ' + mid + "H" + W + '" stroke="var(--sx-l2)" stroke-opacity=".5" stroke-width=".5" vector-effect="non-scaling-stroke"/>' +
        '<path d="' + bars.up + '" fill="var(--sx-up)" fill-opacity=".8"/><path d="' + bars.down + '" fill="var(--sx-down)" fill-opacity=".8"/></svg>' +
        '<span class="sx-hrsum"><span style="color:' + this.color(dir(week)) + '">' + esc(this.t("week") + amt(week)) + '</span><span style="color:' + this.color(dir(month)) + '">' + esc(this.t("month") + amt(month)) + "</span></span></div>";
    },

    // ---------------------------------------------------------------- search
    searchResults: function () {
      var q = this.st.query.trim().toLowerCase(), self = this;
      var pool = WATCH.concat(CATALOG), seen = {}, results = [];
      pool.forEach(function (c) {
        if (seen[c.id]) return;
        var hay = [c.code.toLowerCase(), c.name.toLowerCase(), c.py, c.en || ""];
        var hit = hay.some(function (h) { return h.indexOf(q) >= 0; });
        if (hit) { seen[c.id] = true; results.push(c); }
      });
      results = results.slice(0, 8);
      if (!results.length) return '<div class="sx-card sx-empty" role="status">' + esc(this.t("none")) + "</div>";
      var first = null;
      return '<div class="sx-card sx-results" role="list">' + results.map(function (c) {
        var cq = self.q(c.id) || complete(Object.create(c)), added = !!self.q(c.id);
        if (!added && first === null) first = c.id;
        var type = c.index ? self.t("tIndex") : c.type === "etf" ? self.t("tETF") : c.type === "chinext" ? self.t("tChiNext") : self.t("tStock");
        var d = dir(cq.change), col = self.color(d);
        var inner = '<span class="sx-badge sx-m-' + c.m + '">' + BADGE[c.m][self.lang === "zh" ? 1 : 0] + "</span>" +
          '<span class="sx-rname"><span class="sx-rn">' + esc(c.name) + '</span><span class="sx-rs">' + esc(c.code + " · " + type) + "</span></span>" +
          '<span class="sx-rq" style="color:' + col + '"><span class="sx-rp">' + self.price(cq, cq.price) + '</span><span class="sx-rpc">' + self.f.percent(cq.pct) + "</span></span>";
        if (added) return '<div class="sx-result is-added" role="listitem">' + inner + '<span class="sx-added">' + ICON.check + esc(self.t("added")) + "</span></div>";
        return '<div role="listitem"><button type="button" class="sx-result' + (c.id === first ? " is-hl" : "") + '" data-act="add" data-v="' + c.id + '" data-k="a-' + c.id + '" aria-label="' + esc(fmt(self.t("addTo"), c.name + " " + c.code)) + '">' + inner + '<span class="sx-plus">' + ICON.plus + "</span></button></div>";
      }).join("") + "</div>";
    },

    addSymbol: function (id) {
      if (this.q(id)) return;
      var c = null;
      CATALOG.concat(WATCH).forEach(function (x) { if (x.id === id) c = x; });
      if (!c) return;
      this.items.push(complete(Object.create(c)));
      this.st.query = "";
      this.st.filter = "all";
      this.st.expanded = null;
      this.render();
      var list = this.stage.querySelector(".sx-list");
      if (list) list.scrollTop = list.scrollHeight;
      var btn = this.stage.querySelector('[data-k="r-' + id + '"]');
      if (btn) btn.focus({ preventScroll: true });
    },

    // ---------------------------------------------------------------- calendar
    calendarPanel: function () {
      var st = this.st, self = this;
      var h = '<div class="sx-card sx-card-strong sx-calhead">' +
        '<button type="button" class="sx-iconbtn is-btn" data-act="back" data-k="back1" aria-label="' + esc(this.t("back")) + '">' + ICON.left + "</button>" +
        '<div class="sx-title"><div class="sx-name">' + esc(this.t("calTitle")) + '</div><div class="sx-sub">' + esc(this.t("calSub")) + "</div></div>" +
        '<div class="sx-seg" role="group">' +
        '<button type="button" data-act="calmode" data-v="month" data-k="cm-m" aria-pressed="' + !st.calYear + '"' + (!st.calYear ? ' class="is-on"' : "") + ">" + esc(this.t("mMonth")) + "</button>" +
        '<button type="button" data-act="calmode" data-v="year" data-k="cm-y" aria-pressed="' + st.calYear + '"' + (st.calYear ? ' class="is-on"' : "") + ">" + esc(this.t("mYear")) + "</button></div></div>";
      var regions = ["CNY", "HKD", "USD"].filter(function (c) { return Object.keys(self.history[c]).length; });
      h += '<div class="sx-card sx-cal">';
      if (regions.length > 1) {
        h += '<div class="sx-seg sx-seg-wide" role="group">' + regions.map(function (r) {
          var on = r === st.calRegion;
          return '<button type="button" data-act="calregion" data-v="' + r + '" data-k="cr-' + r + '" aria-pressed="' + on + '"' + (on ? ' class="is-on"' : "") + ">" + esc(self.t(r)) + "</button>";
        }).join("") + "</div>";
      }
      h += st.calYear ? this.yearView() : this.monthView();
      h += "</div>";
      h += '<div class="sx-calfoot"><button type="button" class="sx-primary" data-act="back" data-k="back2">' + esc(this.t("back")) + "</button></div>";
      return h;
    },

    monthTitle: function (y, m) {
      return this.lang === "zh" ? y + "年" + (m + 1) + "月" : this.s.months[m] + " " + y;
    },

    monthView: function () {
      var st = this.st, rec = this.history[st.calRegion], self = this;
      var idx = st.calMonth, y = Math.floor(idx / 12), m = idx % 12;
      var minIdx = 2026 * 12 + 5, maxIdx = 2026 * 12 + 8;
      var h = '<div class="sx-calnav"><button type="button" class="sx-iconbtn is-btn" data-act="calprev" data-k="cprev" aria-label="' + esc(this.t("prevMonth")) + '"' + (idx <= minIdx ? " disabled" : "") + ">" + ICON.left + "</button>" +
        '<span class="sx-calt">' + esc(this.monthTitle(y, m)) + "</span>" +
        '<button type="button" class="sx-iconbtn is-btn" data-act="calnext" data-k="cnext" aria-label="' + esc(this.t("nextMonth")) + '"' + (idx >= maxIdx ? " disabled" : "") + ">" + ICON.right + "</button></div>";
      var first = new Date(Date.UTC(y, m, 1)), lead = (first.getUTCDay() + 6) % 7, days = new Date(Date.UTC(y, m + 1, 0)).getUTCDate();
      var vals = [];
      for (var d = 1; d <= days; d++) { var key = y + "-" + pad(m + 1) + "-" + pad(d); if (rec[key] !== undefined) vals.push(rec[key]); }
      var big = vals.length ? Math.max.apply(null, vals.map(Math.abs)) : 0, total = 0, up = 0, down = 0;
      h += '<div class="sx-calgrid"><div class="sx-wds" aria-hidden="true">' + this.s.wd.map(function (w, i) {
        return '<span class="' + (i >= 5 ? "is-we" : "") + '">' + esc(w) + "</span>";
      }).join("") + '</div><div class="sx-days" role="list" aria-label="' + esc(this.monthTitle(y, m)) + '">';
      for (var b = 0; b < lead; b++) h += '<span class="sx-day is-blank" aria-hidden="true"></span>';
      for (d = 1; d <= days; d++) {
        var k = y + "-" + pad(m + 1) + "-" + pad(d), v = rec[k], wd = (lead + d - 1) % 7, today = k === "2026-09-30";
        var style = "";
        if (v !== undefined) {
          total += v; if (v > 0) up++; else if (v < 0) down++;
          var strength = big > 0 ? Math.min(Math.abs(v) / big, 1) : 0;
          style = ' style="background:color-mix(in srgb, ' + this.color(dir(v)) + " " + Math.round((0.08 + 0.3 * strength) * 100) + '%, transparent)"';
        }
        var label = fmt(this.t("dayCell"), d) + ", " + (v !== undefined ? this.t("todayPL") + " " + (st.hide ? "****" : this.f.signedMoney(v)) : this.t("noRecord"));
        h += '<span role="listitem" class="sx-day' + (wd >= 5 ? " is-we" : "") + (today ? " is-today" : "") + '"' + style + '><span class="sx-vh">' + esc(label) + '</span><span class="sx-dn" aria-hidden="true">' + d + "</span>" +
          (v !== undefined && !st.hide ? '<span class="sx-dv" aria-hidden="true" style="color:' + this.color(dir(v)) + '">' + this.f.compact(v) + "</span>" : "") + "</span>";
      }
      h += "</div></div>";
      h += '<div class="sx-calsum">' + (vals.length ? '<span style="color:' + this.color(dir(total)) + '">' + esc(this.t("monthSum") + (st.hide ? "****" : this.f.signedMoney(total))) + '</span><span class="sx-l2">' + esc(fmt(this.t("upDown"), up, down)) + "</span>" : '<span class="sx-l2">' + esc(this.t("noMonth")) + "</span>") + "</div>";
      return h;
    },

    yearView: function () {
      var st = this.st, rec = this.history[st.calRegion], self = this, y = 2026;
      var h = '<div class="sx-calnav"><button type="button" class="sx-iconbtn is-btn" aria-label="' + esc(this.t("prevYear")) + '" disabled>' + ICON.left + "</button>" +
        '<span class="sx-calt">' + (this.lang === "zh" ? y + "年" : y) + "</span>" +
        '<button type="button" class="sx-iconbtn is-btn" aria-label="' + esc(this.t("nextYear")) + '" disabled>' + ICON.right + "</button></div>";
      var totals = [];
      for (var m = 0; m < 12; m++) {
        var sum = null;
        Object.keys(rec).forEach(function (k) { if (k.slice(0, 7) === y + "-" + pad(m + 1)) sum = (sum || 0) + rec[k]; });
        totals.push(sum);
      }
      var big = Math.max.apply(null, totals.map(function (v) { return v === null ? 0 : Math.abs(v); })), up = 0, down = 0, all = 0;
      h += '<div class="sx-months">' + totals.map(function (v, mm) {
        var style = "";
        if (v !== null) {
          all += v; if (v > 0) up++; else if (v < 0) down++;
          style = ' style="background:color-mix(in srgb, ' + self.color(dir(v)) + " " + Math.round((0.08 + 0.3 * Math.min(Math.abs(v) / big, 1)) * 100) + '%, transparent)"';
        }
        var name = self.lang === "zh" ? (mm + 1) + "月" : self.s.mshort[mm];
        var inner = '<span class="sx-dn">' + esc(name) + "</span>" + (v !== null && !st.hide ? '<span class="sx-mv" style="color:' + self.color(dir(v)) + '">' + self.f.compact(v) + "</span>" : "");
        if (v === null) return '<span class="sx-month"' + style + ">" + inner + "</span>";
        return '<button type="button" class="sx-month' + (mm === 8 ? " is-today" : "") + '"' + style + ' data-act="calmonth" data-v="' + (y * 12 + mm) + '" data-k="cmo-' + mm + '">' + inner + "</button>";
      }).join("") + "</div>";
      h += '<div class="sx-calsum"><span style="color:' + this.color(dir(all)) + '">' + esc(this.t("yearSum") + (st.hide ? "****" : this.f.signedMoney(all))) + '</span><span class="sx-l2">' +
        esc(fmt(this.lang === "zh" ? this.s.upDownY : this.t("upDown"), up, down)) + "</span></div>";
      return h;
    },

    // ---------------------------------------------------------------- events
    onClick: function (e) {
      var el = e.target.closest ? e.target.closest("[data-act]") : null;
      if (!el || !this.root.contains(el) || el.disabled) return;
      var act = el.getAttribute("data-act"), v = el.getAttribute("data-v"), st = this.st;
      switch (act) {
        case "filter": st.filter = v; break;
        case "row": st.expanded = st.expanded === v ? null : v; break;
        case "pill": st.display = (st.display + 1) % 3; break;
        case "period": st.period = v; break;
        case "alloc": st.alloc = !st.alloc; break;
        case "hist": st.hist = !st.hist; break;
        case "eye": st.hide = !st.hide; break;
        case "cal": st.view = "calendar"; this.render(); this.focus("back1"); return;
        case "back": st.view = "list"; this.render(); this.focus("cal"); return;
        case "calmode": st.calYear = v === "year"; break;
        case "calregion": st.calRegion = v; break;
        case "calprev": st.calMonth--; break;
        case "calnext": st.calMonth++; break;
        case "calmonth": st.calMonth = Number(v); st.calYear = false; this.render(); this.focus("cprev"); return;
        case "clear": st.query = ""; this.render(); this.focus("search"); return;
        case "add": this.addSymbol(v); return;
        case "mb": st.open = !st.open; break;
        default: return;
      }
      this.render();
    },
    focus: function (key) {
      var el = this.stage.querySelector('[data-k="' + key + '"]');
      if (el) el.focus({ preventScroll: true });
    },
    onContext: function (e) {
      var el = e.target.closest ? e.target.closest('[data-act="mb"]') : null;
      if (!el) return;
      e.preventDefault();
      this.st.iconOnly = !this.st.iconOnly;
      this.render();
    },
    onKey: function (e) {
      var t = e.target;
      if (e.key === "Escape" && t.getAttribute && t.getAttribute("data-k") === "search" && this.st.query) {
        this.st.query = ""; this.render(); e.preventDefault(); return;
      }
      if (e.key === "Enter" && t.getAttribute && t.getAttribute("data-k") === "search") {
        var hl = this.stage.querySelector(".sx-result.is-hl");
        if (hl) { e.preventDefault(); this.addSymbol(hl.getAttribute("data-v")); }
        return;
      }
      // ← → switch charts while a row is expanded, as in the app.
      if ((e.key === "ArrowLeft" || e.key === "ArrowRight") && this.st.expanded && t.closest && t.closest(".sx-row.is-open")) {
        var q = this.q(this.st.expanded), list = this.available(q), i = list.indexOf(this.effectivePeriod(q));
        i = (i + (e.key === "ArrowRight" ? 1 : -1) + list.length) % list.length;
        this.st.period = list[i];
        e.preventDefault();
        this.render();
        this.focus("t-" + q.id + "-" + list[i]);
      }
    },
    onInput: function (e) {
      var t = e.target;
      if (t.getAttribute("data-k") !== "search") return;
      var had = !!this.st.query;
      this.st.query = t.value;
      if (had !== !!t.value) { this.render(); return; }
      var c = this.stage.querySelector(".sx-content");
      if (c) c.innerHTML = this.content();
    },

    onHover: function (e) {
      if (e.pointerType === "touch") return;
      var chart = e.target.closest ? e.target.closest(".sx-chart") : null;
      if (!chart || !this.hover) { this.endHover(); return; }
      var box = chart.querySelector(".sx-kbox") || chart.querySelector(".sx-fchart") || chart;
      var rect = box.getBoundingClientRect(), fr = (e.clientX - rect.left) / rect.width;
      if (fr < 0 || fr > 1) { this.endHover(); return; }
      var hv = this.hover, i = hv.pos(fr), sec = chart.parentNode;
      sec.classList.add("is-hover");
      sec.querySelector(".sx-readout").textContent = hv.text(i);
      var cross = box.querySelector(".sx-cross"), dot = box.querySelector(".sx-dotm");
      cross.hidden = false;
      cross.style.left = (hv.x(i) * 100).toFixed(2) + "%";
      if (hv.y) {
        dot.hidden = false;
        dot.style.left = (hv.x(i) * 100).toFixed(2) + "%";
        dot.style.top = (hv.y(i) * 100).toFixed(2) + "%";
        dot.style.background = hv.dotColor ? hv.dotColor(i) : hv.color;
      }
      if (hv.legend) chart.querySelector(".sx-legend").innerHTML = hv.legend(i);
      this.hovering = sec;
    },
    endHover: function () {
      var sec = this.hovering;
      if (!sec) return;
      this.hovering = null;
      sec.classList.remove("is-hover");
      Array.prototype.forEach.call(sec.querySelectorAll(".sx-cross, .sx-dotm"), function (el) { el.hidden = true; });
      if (this.hover && this.hover.legend) {
        var lg = sec.querySelector(".sx-legend");
        if (lg) lg.innerHTML = this.hover.legend(59);
      }
    }
  };

  function init() {
    Array.prototype.forEach.call(document.querySelectorAll("figure.sxd:not(.sxd-ready)"), function (el) {
      try { new Demo(el); } catch (err) { if (window.console) console.error(err); }
    });
  }
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", init);
  else init();
})();
