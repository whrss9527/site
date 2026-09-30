#!/usr/bin/env python3
"""Check the static site: every internal link and asset resolves, every #fragment
exists, and no page loads anything from another origin. Also checks the two
languages: every English page has a Chinese counterpart under zh/ and vice
versa, pages link only to pages in their own language (except the language
switcher, marked with hreflang), and each page declares canonical and hreflang
alternates for the pair.

Usage: python3 scripts/check_links.py   (run from the repository root)
Exits with status 1 if a problem is found.
"""
import os
import re
import sys
from html.parser import HTMLParser
from urllib.parse import urlsplit, unquote

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKIP_DIRS = {".git", ".github", "scripts", "_site", "node_modules"}
LOADING_TAGS = {("link", "href"), ("script", "src"), ("img", "src"), ("source", "srcset"),
                ("img", "srcset"), ("iframe", "src"), ("video", "src"), ("audio", "src")}


class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.refs = []   # (tag, attr, value, rel, hreflang)
        self.ids = set()
        self.canonical = None
        self.alternates = {}  # hreflang -> href

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if "id" in a:
            self.ids.add(a["id"])
        if tag == "a" and "name" in a:
            self.ids.add(a["name"])
        if tag == "link" and a.get("rel") == "canonical":
            self.canonical = a.get("href")
        if tag == "link" and a.get("rel") == "alternate" and a.get("hreflang"):
            self.alternates[a["hreflang"]] = a.get("href")
        for attr in ("href", "src", "srcset"):
            if attr in a and a[attr] is not None:
                self.refs.append((tag, attr, a[attr], a.get("rel", ""), a.get("hreflang")))


def html_files():
    for dirpath, dirnames, filenames in os.walk(ROOT):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
        for f in filenames:
            if f.endswith(".html"):
                yield os.path.join(dirpath, f)


def target_file(page_path, url_path):
    if url_path.startswith("/"):
        full = os.path.join(ROOT, url_path.lstrip("/"))
    else:
        full = os.path.normpath(os.path.join(os.path.dirname(page_path), url_path))
    if url_path.endswith("/") or os.path.isdir(full):
        full = os.path.join(full, "index.html")
    return full


ORIGIN = "https://whrss.com"


def url_path(rel_page):
    """zh/pop/index.html -> /zh/pop/"""
    d = os.path.dirname(rel_page).replace(os.sep, "/")
    return "/" + (d + "/" if d else "")


def check_languages(parsed):
    problems = []
    pages = {os.path.relpath(p, ROOT).replace(os.sep, "/"): page for p, page in parsed.items()}
    pages.pop("404.html", None)   # shared by both languages
    zh = {p[len("zh/"):] for p in pages if p.startswith("zh/")}
    en = {p for p in pages if not p.startswith("zh/")}
    for p in sorted(en - zh):
        problems.append(f"{p}: no Chinese version at zh/{p}")
    for p in sorted(zh - en):
        problems.append(f"zh/{p}: no English version at {p}")

    for rel_page, page in pages.items():
        is_zh = rel_page.startswith("zh/")
        own = url_path(rel_page)
        en_path = own[len("/zh"):] if is_zh else own
        want = {"en": ORIGIN + en_path, "zh-CN": ORIGIN + "/zh" + en_path, "x-default": ORIGIN + en_path}
        if page.canonical != ORIGIN + own:
            problems.append(f"{rel_page}: canonical is {page.canonical}, expected {ORIGIN + own}")
        for hl, href in want.items():
            if page.alternates.get(hl) != href:
                problems.append(f"{rel_page}: hreflang {hl} is {page.alternates.get(hl)}, expected {href}")

        # Links to other pages stay in this page's language, except language switches.
        page_file = os.path.join(ROOT, rel_page)
        for tag, attr, value, rel, hreflang in page.refs:
            if tag != "a" or attr != "href":
                continue
            parts = urlsplit(value)
            if parts.scheme or value.startswith("//") or not parts.path:
                continue
            target = os.path.relpath(target_file(page_file, unquote(parts.path)), ROOT).replace(os.sep, "/")
            if not target.endswith(".html") or target == "404.html":
                continue
            target_zh = target.startswith("zh/")
            if hreflang:
                if (hreflang == "zh-CN") != target_zh:
                    problems.append(f"{rel_page}: link {value} marked hreflang={hreflang} goes to {target}")
            elif target_zh != is_zh:
                problems.append(f"{rel_page}: link {value} leaves the page's language ({target})")
    return problems


def main():
    parsed = {}
    for path in html_files():
        p = Page()
        with open(path, encoding="utf-8") as fh:
            p.feed(fh.read())
        parsed[os.path.normpath(path)] = p

    problems = []
    checked = 0
    for path, page in parsed.items():
        rel_page = os.path.relpath(path, ROOT)
        for tag, attr, value, rel, _ in page.refs:
            values = [v.strip().split(" ")[0] for v in value.split(",")] if attr == "srcset" else [value]
            for v in values:
                if not v:
                    continue
                parts = urlsplit(v)
                external = parts.scheme in ("http", "https") or v.startswith("//")
                loads = (tag, attr) in LOADING_TAGS and not (tag == "link" and rel in ("canonical", "alternate"))
                if external:
                    if loads:
                        problems.append(f"{rel_page}: loads an external resource: {v}")
                    continue
                if parts.scheme in ("mailto", "tel", "data"):
                    continue
                checked += 1
                if not parts.path:          # same-page fragment
                    target = path
                else:
                    target = target_file(path, unquote(parts.path))
                    if not os.path.exists(target):
                        problems.append(f"{rel_page}: broken link {v}")
                        continue
                if parts.fragment and target.endswith(".html"):
                    ids = parsed.get(os.path.normpath(target))
                    if ids is not None and parts.fragment not in ids.ids:
                        problems.append(f"{rel_page}: missing anchor #{parts.fragment} in {v or '(same page)'}")

    # CSS: url(...) must be local and exist; no @import from elsewhere
    for dirpath, dirnames, filenames in os.walk(ROOT):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
        for f in filenames:
            if f.endswith(".css"):
                css_path = os.path.join(dirpath, f)
                css = open(css_path, encoding="utf-8").read()
                for m in re.finditer(r"url\(\s*['\"]?([^'\")]+)['\"]?\s*\)|@import\s+['\"]([^'\"]+)", css):
                    u = m.group(1) or m.group(2)
                    if u.startswith(("http:", "https:", "//")):
                        problems.append(f"{os.path.relpath(css_path, ROOT)}: external resource {u}")
                    elif not u.startswith("data:") and not os.path.exists(os.path.normpath(os.path.join(dirpath, u))):
                        problems.append(f"{os.path.relpath(css_path, ROOT)}: broken url({u})")

    problems += check_languages(parsed)

    print(f"{len(parsed)} pages, {checked} internal references checked")
    for p in problems:
        print("  " + p)
    if problems:
        print(f"{len(problems)} problem(s)")
        return 1
    print("OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
