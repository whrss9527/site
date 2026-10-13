#!/usr/bin/env python3
"""Compare committed pages with a rebuild in a temporary copy of the site."""
import datetime
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parent.parent
SKIP = {".git", ".github", "scripts", "_site", "node_modules", "__pycache__"}


def generated(root):
    pages = {}
    for directory, dirs, files in os.walk(root):
        dirs[:] = [name for name in dirs if name not in SKIP]
        for name in files:
            path = Path(directory) / name
            if name.endswith(".html") or path == root / "sitemap.xml":
                pages[path.relative_to(root)] = path.read_bytes()
    return pages


def main():
    try:
        dates = {node.text for node in ET.parse(ROOT / "sitemap.xml").iter(
            "{http://www.sitemaps.org/schemas/sitemap/0.9}lastmod")}
        if len(dates) != 1:
            raise ValueError("sitemap must contain one shared lastmod date")
        lastmod = dates.pop()
        if datetime.date.fromisoformat(lastmod).isoformat() != lastmod:
            raise ValueError("lastmod must use YYYY-MM-DD")
    except (OSError, ET.ParseError, ValueError, TypeError) as error:
        print(f"Cannot read the build date: {error}", file=sys.stderr)
        return 1

    committed = generated(ROOT)
    with tempfile.TemporaryDirectory(prefix="site-generated-") as directory:
        copy = Path(directory) / "site"
        shutil.copytree(ROOT, copy, ignore=shutil.ignore_patterns(
            ".git", ".github", "_site", "node_modules", "__pycache__", "*.pyc"))
        # Start without old pages, so removed generator output is detected too.
        for path in committed:
            (copy / path).unlink()
        result = subprocess.run(
            [sys.executable, "scripts/site/build.py"], cwd=copy,
            env={**os.environ, "LASTMOD": lastmod, "PYTHONDONTWRITEBYTECODE": "1"},
            stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
        if result.returncode:
            print(result.stdout, end="")
            return result.returncode
        rebuilt = generated(copy)

    differences = sorted(path for path in committed.keys() | rebuilt.keys()
                         if committed.get(path) != rebuilt.get(path))
    for path in differences:
        state = "missing" if path not in committed else "obsolete" if path not in rebuilt else "changed"
        print(f"{state}: {path}")
    if differences:
        print(f"{len(differences)} generated file(s) differ. Regenerate with "
              f"LASTMOD={lastmod} python3 scripts/site/build.py and review the changes.")
        return 1
    print(f"{len(committed)} generated files match (LASTMOD={lastmod}); checkout unchanged.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
