#!/usr/bin/env python3
"""Compare the site catalog with one published stable Pop release, without edits."""
import argparse
import hashlib
import json
from pathlib import Path
import re
import subprocess
import sys

sys.dont_write_bytecode = True
sys.path.insert(0, str(Path(__file__).resolve().parent / "site"))
from pop_plugins import PLUGINS  # noqa: E402

STRING = r'"(?:[^"\\]|\\.)*"'


def git(repository, *arguments):
    result = subprocess.run(["git", "-C", str(repository), *arguments],
                            check=True, capture_output=True)
    return result.stdout


def source_catalog(repository, sha):
    hashes = {}

    def read(path):
        data = git(repository, "show", f"{sha}:{path}")
        hashes[path] = hashlib.sha256(data).hexdigest()
        return data.decode("utf-8")

    source = read("Pop/Plugins/PluginCatalog.swift")
    strings = read("Pop/Resources/en.lproj/Localizable.strings")
    translations = {json.loads(key): json.loads(value) for key, value in re.findall(
        f"({STRING})\\s*=\\s*({STRING})\\s*;", strings)}
    settings = read("Pop/Core/AppSettings.swift")
    identifiers = settings.split("enum BuiltinPluginID {", 1)[1].split("\n}", 1)[0]
    functions = {name: json.loads(value) for name, value in re.findall(
        rf"static let (\w+)\s*=\s*({STRING})", identifiers)}
    starts = list(re.finditer(rf"PluginPackage\(id:\s*({STRING})", source))
    packages = {}
    for position, start in enumerate(starts):
        end = starts[position + 1].start() if position + 1 < len(starts) else source.index("\n    ]", start.start())
        block = source[start.start():end]
        pid = json.loads(start[1])
        if pid in packages:
            raise ValueError("Duplicate source plugin: " + pid)
        fields = {}
        for field in ("name", "summary"):
            match = re.search(rf"{field}:\s*String\(localized:\s*({STRING})\)", block)
            if not match:
                raise ValueError(f"Unsupported source {field}: {pid}")
            chinese = json.loads(match[1])
            if chinese not in translations and re.search(r"[\u3400-\u9fff]", chinese):
                raise ValueError("Missing English translation: " + pid)
            fields[field + "_zh"] = chinese
            fields[field + "_en"] = translations.get(chinese, chinese)
        match = re.search(r"functions:\s*\[(.*?)\]", block, re.S)
        if not match or not re.fullmatch(r"\s*(?:BuiltinPluginID\.\w+\s*,?\s*)+", match[1]):
            raise ValueError("Unsupported source action list: " + pid)
        fields["functions"] = [functions[name] for name in re.findall(r"BuiltinPluginID\.(\w+)", match[1])]
        packages[pid] = fields

    # Independently distributed native bundles keep their catalog in plugin.json.
    paths = git(repository, "ls-tree", "-r", "--name-only", sha, "PluginBundles").decode().splitlines()
    for path in paths:
        if not path.endswith("/plugin.json"):
            continue
        value = json.loads(read(path))
        pid = value["id"]
        if pid in packages:
            raise ValueError("Duplicate source plugin: " + pid)
        packages[pid] = {"name_en": value["name"]["en"], "name_zh": value["name"]["zh-Hans"],
                         "summary_en": value["summary"]["en"], "summary_zh": value["summary"]["zh-Hans"],
                         "functions": value["functions"]}
    return packages, hashes


def compare(catalog, site=PLUGINS):
    local = {plugin.id: {"name_en": plugin.en, "name_zh": plugin.zh,
                        "summary_en": plugin.en_sum, "summary_zh": plugin.zh_sum,
                        "functions": plugin.funcs} for plugin in site}
    changes = [{"id": pid, "field": field, "site": local[pid][field], "release": value}
               for pid in sorted(catalog.keys() & local.keys())
               for field, value in catalog[pid].items() if local[pid][field] != value]
    return {"added": sorted(catalog.keys() - local.keys()),
            "removed": sorted(local.keys() - catalog.keys()), "changes": changes}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--pop-repo", type=Path, required=True)
    parser.add_argument("--release", type=Path, required=True, help="JSON from GitHub releases/latest")
    parser.add_argument("--manifest", type=Path, required=True, help="The published plugins-VERSION.json")
    args = parser.parse_args()
    release = json.loads(args.release.read_bytes())
    tag = release["tag_name"]
    if not re.fullmatch(r"v\d+\.\d+\.\d+", tag) or release.get("draft") is not False or release.get("prerelease") is not False:
        raise ValueError("A published stable semantic-version release is required")
    version = tag[1:]
    manifest = args.manifest.read_bytes()
    digest = hashlib.sha256(manifest).hexdigest()
    assets = [asset for asset in release["assets"] if asset["name"] == f"plugins-{version}.json"]
    if len(assets) != 1 or assets[0].get("digest") != "sha256:" + digest:
        raise ValueError("The manifest does not match the published asset digest")
    sha = git(args.pop_repo, "rev-parse", "--verify", f"refs/tags/{tag}^{{commit}}").decode().strip()
    if not re.fullmatch(r"[0-9a-f]{40}", sha):
        raise ValueError("The stable source tag cannot be resolved")
    target = release.get("target_commitish", "")
    if re.fullmatch(r"[0-9a-f]{40}", target) and target != sha:
        raise ValueError("The release source and local tag disagree")
    index = json.loads(manifest)
    if index.get("format") != 1 or index.get("version") != version or index.get("build") != f"{version}+{sha[:12]}":
        raise ValueError("The manifest version/build does not match the stable source")
    released = [plugin["id"] for plugin in index["plugins"]]
    if not all(isinstance(pid, str) for pid in released) or len(released) != len(set(released)):
        raise ValueError("The manifest plugin IDs are invalid or duplicated")
    catalog, hashes = source_catalog(args.pop_repo, sha)
    if set(catalog) != set(released):
        raise ValueError("Source catalog and published manifest IDs disagree")
    difference = compare(catalog)
    report = {"version": version, "source_sha": sha, "manifest_sha256": digest,
              "source_files_sha256": hashes, "plugins": len(released), **difference}
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return int(bool(difference["added"] or difference["removed"] or difference["changes"]))


if __name__ == "__main__":
    try:
        sys.exit(main())
    except (ValueError, KeyError, IndexError, TypeError, OSError, subprocess.CalledProcessError) as error:
        print("Catalog comparison failed; no files changed: " + str(error), file=sys.stderr)
        sys.exit(2)
