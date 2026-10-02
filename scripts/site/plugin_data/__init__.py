"""What each plugin page says and shows. Each module here defines DATA = {plugin id: entry}
(by category: text.py, convert.py, developer.py, screen.py, recording.py, files.py, system.py). The format is in the README
("Plugin pages"). Any user-visible string that differs between the languages is written T(en, zh).
"""


class T(tuple):
    """A string in English and in Simplified Chinese: T("Copy", "复制")."""

    def __new__(cls, en, zh):
        return tuple.__new__(cls, (en, zh))


def res(x, lang):
    """x with every T resolved to one language."""
    if isinstance(x, T):
        return x[1] if lang == "zh" else x[0]
    if isinstance(x, dict):
        return {k: res(v, lang) for k, v in x.items()}
    if isinstance(x, (list, tuple)):
        return [res(v, lang) for v in x]
    return x


def load(tolerant=False):
    """Every DATA in this folder, merged (a plugin may appear only once). tolerant: skip modules
    that fail to import (pop_plugin_pages.py --only, while other modules are being edited)."""
    import importlib
    import pkgutil
    out = {}
    for info in sorted(pkgutil.iter_modules(__path__), key=lambda i: i.name):
        try:
            m = importlib.import_module(f"{__name__}.{info.name}")
        except Exception as e:  # noqa: BLE001
            if not tolerant:
                raise
            print(f"plugin_data/{info.name}.py skipped: {e!r}")
            continue
        for k, v in getattr(m, "DATA", {}).items():
            assert k not in out, f"plugin_data: {k} is defined twice"
            out[k] = v
    return out
