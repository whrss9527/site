/* whrss.com: the language menu and the mobile menu. Everything works without this
   file; it only remembers the chosen language and closes open menus. */
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
})();
