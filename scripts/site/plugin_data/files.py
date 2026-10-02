"""Plugin pages: files and system plugins. See __init__.py and the README ("Plugin pages")."""
from . import T

DATA = {
    "tidyFolder": {
        "chips": [T("By type", "按类型"), T("By month", "按月份"), T("Undo", "可以撤销")],
        "points": [
            T("Sort the files at the top of <b>Downloads</b>, or the folder you select, into Images, Videos, Audio, Documents, Archives, Installers and Other.",
              "把「<b>下载</b>」（或者选中的文件夹）第一层的文件归到「图像」「视频」「音频」「文档」「压缩包」「安装包」「其他」里。"),
            T("Or by the month they were added, and photos and videos <b>by the date they were taken</b>.",
              "也可以按放进来的月份归，照片和视频还能<b>按拍摄日期</b>归。"),
            T("The card shows how many files go into each folder first; nothing moves until you click Tidy.",
              "卡片上先列出每个文件夹会放进几个文件，点「整理」才动。"),
            T("Folders, apps, hidden files and unfinished downloads stay where they are. <b>Undo</b> puts everything back.",
              "子文件夹、App、隐藏文件和没下载完的文件不动；整理完可以<b>撤销</b>，文件都挪回原处。"),
        ],
        "scene": {
            "src": {"kind": "files", "app": T("Downloads", "下载"), "sum": T("Downloads", "下载"), "cap": T("Open Downloads, or select a folder", "打开「下载」，或者选中一个文件夹"),
                    "sub": T("With nothing selected it tidies Downloads.", "什么都不选时整理的是「下载」。"),
                    "files": [{"name": "IMG_2041.HEIC", "kind": "photo", "art": "sunset"}, {"name": "invoice-0930.pdf"}, {"name": "Song.m4a", "kind": "audio"},
                              {"name": "Clip.mov", "kind": "video", "art": "waves"}, {"name": "Report.docx"}, {"name": "Setup.dmg"},
                              {"name": "Archive.zip", "kind": "zip"}, {"name": "Screenshot.png", "kind": "photo", "art": "screen"}, {"name": "data.csv"}]},
            "card": {"w": 330, "sub": T("Downloads · 9 files", "下载 · 9 个文件"), "btns": [T("Tidy", "整理")], "tint": 0,
                     "body": [{"t": "seg", "items": [T("By type", "按类型"), T("By month", "按月份"), T("By date taken", "按拍摄日期")], "on": 0},
                              {"t": "list", "dense": True, "items": [
                                  {"file": {"kind": "folder"}, "title": T("Images", "图像"), "right": "2"},
                                  {"file": {"kind": "folder"}, "title": T("Videos", "视频"), "right": "1"},
                                  {"file": {"kind": "folder"}, "title": T("Audio", "音频"), "right": "1"},
                                  {"file": {"kind": "folder"}, "title": T("Documents", "文档"), "right": "3"},
                                  {"file": {"kind": "folder"}, "title": T("Archives", "压缩包"), "right": "1"},
                                  {"file": {"kind": "folder"}, "title": T("Installers", "安装包"), "right": "1"}]}]},
            "steps": [
                {"cap": T("See where each file will go", "先看每个文件会去哪"), "acts": []},
                {"cap": T("Click Tidy", "点「整理」"), "sub": T("Undo puts everything back.", "可以撤销，文件都挪回原处。"),
                 "acts": [["click", "btn:0"], ["close"],
                          ["grid", [{"name": T("Images", "图像"), "kind": "folder"}, {"name": T("Videos", "视频"), "kind": "folder"},
                                    {"name": T("Audio", "音频"), "kind": "folder"}, {"name": T("Documents", "文档"), "kind": "folder"},
                                    {"name": T("Archives", "压缩包"), "kind": "folder"}, {"name": T("Installers", "安装包"), "kind": "folder"}]]]},
            ],
        },
    },
}
