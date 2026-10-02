#!/usr/bin/env python3
"""Regenerate every page of the site, in English and Simplified Chinese, and sitemap.xml.

Usage: python3 scripts/site/build.py   (from anywhere; writes into the repository)
Then run python3 scripts/check_links.py.
"""
import datetime
import os
import sys

sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import apps      # noqa: E402
import home      # noqa: E402
import pop_plugin_pages  # noqa: E402
import privacy   # noqa: E402
import support   # noqa: E402
from common import APPS, ORIGIN, SITE  # noqa: E402

PAGES = ["/"] + [f"/{k}/" for k in APPS] + pop_plugin_pages.pages() + [f"/privacy/{k}/" for k in APPS] + ["/support/"]


def sitemap(lastmod):
    rows = []
    for p in PAGES:
        for loc in (p, "/zh" + p):
            rows.append(f"  <url><loc>{ORIGIN}{loc}</loc><lastmod>{lastmod}</lastmod></url>")
    xml = ('<?xml version="1.0" encoding="UTF-8"?>\n'
           '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "\n".join(rows) + "\n</urlset>\n")
    with open(os.path.join(SITE, "sitemap.xml"), "w", encoding="utf-8") as f:
        f.write(xml)
    print("wrote sitemap.xml")


def main():
    home.build()
    apps.build_all()
    pop_plugin_pages.build_all()
    privacy.build_all()
    support.build()
    lastmod = os.environ.get("LASTMOD") or datetime.date.today().isoformat()
    sitemap(lastmod)


if __name__ == "__main__":
    main()
