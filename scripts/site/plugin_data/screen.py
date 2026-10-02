"""Plugin pages: screen and image plugins. See __init__.py and the README ("Plugin pages")."""
from . import T

DATA = {
    "removeBackground": {
        "chips": [T("People, pets, things", "人、动物、物品"), T("Offline", "离线"), T("Transparent PNG", "透明 PNG")],
        "points": [
            T("Select a picture, or an image file in Finder, and Pop <b>removes the background</b>, keeping the person, animal or object.",
              "选中一张图片，或者访达里的图片文件，Pop 就<b>去掉背景</b>，只留下人、动物或物品。"),
            T("It runs <b>on your Mac</b>, offline: the picture isn’t uploaded anywhere.", "在<b>本机</b>离线处理，图片不上传到任何地方。"),
            T("Copy the cut-out, save it as a PNG with a transparent background, or pin it on the screen.",
              "抠好的图可以复制、存成透明背景的 PNG，或者贴到屏幕上。"),
        ],
        "scene": {
            "src": {"kind": "files", "cap": T("Select a photo in Finder", "在访达里选中一张照片"),
                    "files": [{"name": "Portrait.jpg", "kind": "photo", "art": "portrait", "sel": True}, {"name": "Beach.heic", "kind": "photo", "art": "beach"},
                              {"name": "Mug.png", "kind": "photo", "art": "mug"}, {"name": T("Notes.txt", "笔记.txt")}]},
            "card": {"w": 320, "sub": "Portrait.jpg", "btns": [T("Copy", "复制"), T("Save as PNG", "存成 PNG"), T("Pin to Screen", "贴到屏幕")], "tint": 1,
                     "body": [{"t": "panes", "panes": [[{"t": "img", "art": "portrait", "ar": "4/3"}], [{"t": "img", "art": "portrait", "ar": "4/3", "mods": ["cutout"]}]]}]},
            "steps": [
                {"cap": T("The background disappears", "背景没了"), "acts": [["wait", 500], ["swap", 0, 1]]},
                {"cap": T("Save it as a transparent PNG", "存成透明背景的 PNG"),
                 "acts": [["click", "btn:1"], ["close"], ["file", {"name": T("Portrait cut-out.png", "Portrait 抠图.png"), "kind": "photo", "art": "portrait", "at": 1}]]},
            ],
        },
    },
}
