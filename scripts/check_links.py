#!/usr/bin/env python3
"""Check the static site: every internal link and asset resolves, every #fragment
exists, and no page loads anything from another origin.

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
        self.refs = []   # (tag, attr, value, rel)
        self.ids = set()

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if "id" in a:
            self.ids.add(a["id"])
        if tag == "a" and "name" in a:
            self.ids.add(a["name"])
        for attr in ("href", "src", "srcset"):
            if attr in a and a[attr] is not None:
                self.refs.append((tag, attr, a[attr], a.get("rel", "")))


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
        for tag, attr, value, rel in page.refs:
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
