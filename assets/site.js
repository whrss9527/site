/* whrss.com: the language menu, the mobile menu and the home page's reel. Everything works
   without this file; it only remembers the chosen language, closes open menus and shows the
   reel's previous / next buttons (without them the reel still scrolls sideways). */
(function () {
  var KEY = "lang";

  function openMenus() {
    return document.querySelectorAll("details.lang-menu[open], details.nav-menu[open]");
  }

  document.addEventListener("click", function (e) {
    var t = e.target;
    // Picking a language (header menu, mobile menu or footer) remembers it.
    // Only the English home page reads it back: a stored "zh" sends / to /zh/.
    var a = t.closest && t.closest("a[data-lang]");
    if (a) {
      try { localStorage.setItem(KEY, a.getAttribute("data-lang")); } catch (err) { /* storage blocked */ }
    }
    // A click outside an open menu closes it.
    Array.prototype.forEach.call(openMenus(), function (d) {
      if (!d.contains(t)) d.removeAttribute("open");
    });
  });

  document.addEventListener("keydown", function (e) {
    if (e.key !== "Escape") return;
    Array.prototype.forEach.call(openMenus(), function (d) {
      var hadFocus = d.contains(document.activeElement);
      d.removeAttribute("open");
      if (hadFocus) d.querySelector("summary").focus();
    });
  });

  // Moving keyboard focus out of the language menu closes it.
  document.addEventListener("focusin", function (e) {
    Array.prototype.forEach.call(document.querySelectorAll("details.lang-menu[open]"), function (d) {
      if (!d.contains(e.target)) d.removeAttribute("open");
    });
  });

  // Home reel: previous / next buttons step one card; each is disabled at its end.
  Array.prototype.forEach.call(document.querySelectorAll(".reel"), function (reel) {
    var nav = reel.nextElementSibling;
    if (!nav || !nav.classList.contains("reel-nav")) return;
    var btns = nav.querySelectorAll(".reel-btn");
    function sync() {
      var max = reel.scrollWidth - reel.clientWidth - 2;
      nav.hidden = max <= 0;
      btns[0].disabled = reel.scrollLeft <= 2;
      btns[1].disabled = reel.scrollLeft >= max;
    }
    Array.prototype.forEach.call(btns, function (b) {
      b.addEventListener("click", function () {
        var card = reel.firstElementChild;
        var step = card ? card.getBoundingClientRect().width + parseFloat(getComputedStyle(reel).columnGap || 20) : reel.clientWidth;
        reel.scrollBy({ left: step * +b.getAttribute("data-dir") });
      });
    });
    reel.addEventListener("scroll", function () { window.requestAnimationFrame(sync); }, { passive: true });
    window.addEventListener("resize", sync, { passive: true });
    sync();
  });
})();
