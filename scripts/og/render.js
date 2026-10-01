#!/usr/bin/env node
/* Renders the Open Graph images (assets/og/<page>-<lang>.png, 1200 × 630) from the site itself:
   each page is opened in Chromium and its own interactive demo (sample data, no screenshots) is
   moved into a card beside the page's name and pitch.

   Needs Node and Playwright with a Chromium (not a dependency of the site):
     python3 -m http.server 8000 &          # from the repository root
     node scripts/og/render.js [http://localhost:8000] [/path/to/chromium]
   Re-run it when a hero, a pitch or a demo changes, and commit the PNGs. */
const path = require("path");
const { chromium } = require("playwright");

const base = process.argv[2] || "http://localhost:8000";
const exe = process.argv[3] || process.env.CHROMIUM || undefined;
const out = path.join(__dirname, "..", "..", "assets", "og");
const PAGES = [["home", "/"], ["pop", "/pop/"], ["meno", "/meno/"], ["stox", "/stox/"], ["proxi", "/proxi/"]];

function compose(key) {
  const home = key === "home";
  const $ = (s) => document.querySelector(s);
  const fig = home ? $(".reel-card.app-pop figure") : $(".stage figure");
  const og = document.createElement("div");
  og.id = "og";
  og.className = home ? "home" : "app-" + key;
  const icons = ["pop", "meno", "stox", "proxi"].map((k) => `<img src="${$(`link[rel=icon]`).href.replace("favicon.svg", "icons/" + k + ".png")}" alt="">`).join("");
  const title = home ? $(".hero h1").innerHTML : $(".app-hero h1").textContent;
  const pitch = home ? $(".hero .eyebrow").textContent : $(".cta .lede").textContent;
  const icon = home ? `<div class="og-icons">${icons}</div>` : `<img class="og-icon" src="${$(".app-hero .icon").src}" alt="">`;
  og.innerHTML = `<div class="og-copy">${icon}<h1>${title}</h1><p>${pitch}</p><span>whrss.com</span></div><div class="og-media"></div>`;
  og.querySelector(".og-media").appendChild(fig);
  fig.querySelectorAll("figcaption, [class$='-tag'], .pxd-cap").forEach((el) => el.remove());
  document.body.appendChild(og);
  const st = document.createElement("style");
  st.textContent = `
    body > :not(#og) { visibility: hidden !important; }
    html, body { overflow: hidden !important; }
    #og { position: fixed; inset: 0; z-index: 9999; display: grid; grid-template-columns: 470px 1fr; align-items: center; gap: 24px;
      padding: 0 0 0 72px; background: var(--bg); overflow: hidden; }
    #og::before { content: ""; position: absolute; inset: 0; z-index: -1;
      background: radial-gradient(60% 80% at 10% 10%, color-mix(in srgb, var(--app) 22%, transparent), transparent 70%),
                  radial-gradient(60% 80% at 90% 90%, color-mix(in srgb, var(--app) 14%, transparent), transparent 70%); }
    #og.home::before { background: radial-gradient(50% 70% at 8% 10%, rgba(91,123,255,.2), transparent 70%), radial-gradient(40% 60% at 95% 90%, rgba(240,70,61,.12), transparent 70%), radial-gradient(40% 60% at 60% 5%, rgba(124,108,255,.14), transparent 70%); }
    .og-copy { display: flex; flex-direction: column; align-items: flex-start; gap: 18px; }
    .og-icon { width: 108px; height: 108px; filter: drop-shadow(0 16px 30px color-mix(in srgb, var(--app) 40%, transparent)); }
    .og-icons { display: flex; gap: 12px; } .og-icons img { width: 64px; height: 64px; }
    .og-copy h1 { font-size: ${home ? 54 : 96}px; line-height: ${home ? 1.08 : 1}; letter-spacing: ${home ? "-0.035em" : "-0.05em"}; margin: 0; }
    :lang(zh) .og-copy h1 { letter-spacing: 0; line-height: 1.2; }
    :lang(zh) #og.home .og-copy h1 { font-size: 48px; }
    .og-copy p { font-size: 25px; line-height: 1.35; color: var(--text-2); margin: 0; max-width: 16em; }
    .og-copy span { font-size: 18px; color: var(--text-3); font-weight: 600; }
    .og-media { height: 630px; display: flex; align-items: center; justify-content: center; padding-right: 40px; }
    .og-media figure { margin: 0 !important; width: 100% !important; max-width: 640px !important; animation: none !important; transform: none !important; opacity: 1 !important; }
  `;
  document.head.appendChild(st);
  // Scale the demo to fit the card (CSS zoom keeps it crisp).
  const box = og.querySelector(".og-media").getBoundingClientRect();
  const r = fig.getBoundingClientRect();
  const k = Math.min(1, (box.height - 56) / r.height, (box.width - 40) / r.width);
  if (k < 1) fig.style.zoom = k.toFixed(3);
}

(async () => {
  const browser = await chromium.launch(exe ? { executablePath: exe } : {});
  for (const lang of ["en", "zh"]) {
    for (const [key, p] of PAGES) {
      const page = await browser.newPage({ viewport: { width: 1200, height: 630 }, deviceScaleFactor: 1, colorScheme: "light", reducedMotion: "reduce" });
      await page.goto(base + (lang === "zh" ? "/zh" : "") + p);   // resolves on the load event
      // Build the demo (they are built as they near the viewport) and let fonts and layout settle.
      await page.evaluate(() => { const f = document.querySelector(".stage figure, .reel"); if (f) f.scrollIntoView({ block: "center", behavior: "instant" }); });
      await page.waitForTimeout(700);
      await page.evaluate(() => window.scrollTo({ top: 0, behavior: "instant" }));
      await page.evaluate(compose, key);
      await page.waitForTimeout(600);
      const file = path.join(out, `${key}-${lang}.png`);
      await page.screenshot({ path: file });
      console.log("wrote", path.relative(process.cwd(), file));
      await page.close();
    }
  }
  await browser.close();
})();
