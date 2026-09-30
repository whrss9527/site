/* whrss.com: scroll motion. Progressive enhancement only — every page reads fine without it.

   - .rv / .rv-group     fade and rise into view once (children of .rv-group are staggered in CSS)
   - [data-p]            gets --p: 0 as it enters the bottom of the viewport, 1 as it leaves the top
                          (parallax on the home page; the hero tilt where CSS scroll timelines are missing)
   - .scrolly            app features: the text steps scroll by while their media stays pinned;
                          the step nearest the middle of the screen is active
   - .menubar / .localnav condense once the page is scrolled

   The hidden starting states live in site.css behind `html.js` and prefers-reduced-motion:
   no-preference, so with JavaScript off or reduced motion everything is simply there.
   Only transform and opacity animate; scroll work is batched into one requestAnimationFrame. */
(function () {
  "use strict";
  window.__motion = 1;
  var root = document.documentElement;
  var mqReduce = window.matchMedia ? window.matchMedia("(prefers-reduced-motion: reduce)") : { matches: false };
  var mqScrolly = window.matchMedia ? window.matchMedia("(min-width: 1024px) and (min-height: 700px) and (prefers-reduced-motion: no-preference)") : { matches: false };
  var cssTimeline = !!(window.CSS && CSS.supports && CSS.supports("animation-timeline: view()"));
  var each = function (list, fn) { Array.prototype.forEach.call(list, fn); };

  // ------------------------------------------------------------ reveal on scroll
  var reveals = document.querySelectorAll(".rv, .rv-group");
  function showAll() { each(reveals, function (el) { el.classList.add("in"); }); }
  if (mqReduce.matches || !("IntersectionObserver" in window)) {
    showAll();
  } else {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (e.isIntersecting) { e.target.classList.add("in"); io.unobserve(e.target); }
      });
    }, { rootMargin: "0px 0px -8% 0px", threshold: 0.12 });
    each(reveals, function (el) {
      // Anything already above the fold (or tall enough to be half on screen) starts in view.
      io.observe(el);
    });
  }
  if (mqReduce.addEventListener) mqReduce.addEventListener("change", function () { if (mqReduce.matches) showAll(); });

  // ------------------------------------------------------------ scroll-linked state
  var menubar = document.querySelector(".menubar");
  var localnav = document.querySelector(".localnav");
  var progress = [];
  each(document.querySelectorAll("[data-p]"), function (el) {
    // [data-p="css"] is handled by CSS scroll timelines when the browser has them.
    if (el.getAttribute("data-p") === "css" && cssTimeline) return;
    progress.push({ el: el, last: -1 });
  });
  var scrolly = document.querySelector(".scrolly");
  var steps = scrolly ? scrolly.querySelectorAll(":scope > .feature") : [];
  var active = -1;
  var vh = window.innerHeight;

  function setActive(i) {
    if (i === active) return;
    active = i;
    each(steps, function (s, k) { s.classList.toggle("is-active", k === i); });
  }

  function update() {
    ticking = false;
    var y = window.pageYOffset || root.scrollTop;
    if (menubar) menubar.classList.toggle("is-scrolled", y > 4);
    if (localnav) localnav.classList.toggle("is-stuck", localnav.getBoundingClientRect().top <= 0.5 && y > 4);

    if (!mqReduce.matches) {
      for (var i = 0; i < progress.length; i++) {
        var p = progress[i], r = p.el.getBoundingClientRect();
        if (r.bottom < -200 || r.top > vh + 200) continue;
        var v = (vh - r.top) / (vh + r.height);
        v = v < 0 ? 0 : v > 1 ? 1 : Math.round(v * 1000) / 1000;
        if (v !== p.last) { p.last = v; p.el.style.setProperty("--p", v); }
      }
    }

    if (scrolly && mqScrolly.matches) {
      // The active step is the text block whose middle is nearest the middle of the screen.
      var mid = vh / 2, best = 0, bestD = Infinity;
      each(steps, function (s, k) {
        var t = s.firstElementChild.getBoundingClientRect();
        var d = Math.abs(t.top + t.height / 2 - mid);
        if (d < bestD) { bestD = d; best = k; }
      });
      setActive(best);
    }
  }

  var ticking = false;
  function onScroll() {
    if (!ticking) { ticking = true; window.requestAnimationFrame(update); }
  }
  window.addEventListener("scroll", onScroll, { passive: true });
  window.addEventListener("resize", function () { vh = window.innerHeight; each(medias, fit); onScroll(); }, { passive: true });

  // A pinned demo taller than the screen is scaled down (CSS zoom) to fit under the local bar.
  var medias = scrolly ? scrolly.querySelectorAll(":scope > .feature > .feature-media") : [];
  function fit(media) {
    var fig = media.firstElementChild;
    if (!fig) return;
    fig.style.zoom = "";
    if (!scrolly.classList.contains("is-pinned")) return;
    var avail = media.clientHeight - 32, h = fig.getBoundingClientRect().height;
    if (h > avail && avail > 0) fig.style.zoom = Math.max(0.7, avail / h).toFixed(3);
  }
  var fitter = "ResizeObserver" in window ? new ResizeObserver(function (entries) {
    entries.forEach(function (e) { var m = e.target.parentElement; if (m && !m.__fitting) { m.__fitting = 1; fit(m); m.__fitting = 0; } });
  }) : null;

  function scrollyMode() {
    if (!scrolly) return;
    scrolly.classList.toggle("is-pinned", mqScrolly.matches);
    if (!mqScrolly.matches) { active = -1; each(steps, function (s) { s.classList.remove("is-active"); }); }
    each(medias, fit);
    onScroll();
  }
  if (scrolly) {
    // Keyboard: focus inside a step's text or its demo makes that step the active one.
    scrolly.addEventListener("focusin", function (e) {
      if (!mqScrolly.matches) return;
      each(steps, function (s, k) {
        if (s.contains(e.target)) {
          setActive(k);
          var media = s.querySelector(".feature-media");
          if (media && media.contains(e.target)) {
            var t = s.firstElementChild.getBoundingClientRect();
            if (t.bottom < vh * 0.25 || t.top > vh * 0.75) s.firstElementChild.scrollIntoView({ block: "center" });
          }
        }
      });
    });
    if (fitter) each(medias, function (m) { if (m.firstElementChild) fitter.observe(m.firstElementChild); });
    if (mqScrolly.addEventListener) mqScrolly.addEventListener("change", scrollyMode);
    else if (mqScrolly.addListener) mqScrolly.addListener(scrollyMode);
    scrollyMode();
  }
  update();
})();
