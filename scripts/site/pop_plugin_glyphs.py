"""Line icons for Pop's plugins, one per plugin, drawn on a 24 × 24 grid.

They follow the SF Symbol each plugin uses in Pop (PluginCatalog.swift), redrawn as plain SVG
so the site loads nothing from elsewhere. Strokes use currentColor; `F` marks a filled shape.
glyph(id) returns the inner SVG; svg(id) a complete <svg>.
"""

F = 'fill="currentColor" stroke="none"'

G = {
    # ------------------------------------------------------------ text
    "screenshotTranslate": f'<path d="M3.5 8V5.5a2 2 0 0 1 2-2H8M16 3.5h2.5a2 2 0 0 1 2 2V8M20.5 16v2.5a2 2 0 0 1-2 2H16M8 20.5H5.5a2 2 0 0 1-2-2V16"/><path d="m6.6 15.4 2.3-6.6 2.3 6.6M7.4 13.2h3"/><path d="M15.4 8v1.2M12.8 9.6h5.4M17 9.6c-.5 2.4-1.9 4.4-4 5.6M13.8 11.6c.8 1.6 2.2 2.9 4.2 3.6"/>',
    "speak": '<path d="M3.8 9.4h3.3l4.6-4.1v13.4l-4.6-4.1H3.8Z"/><path d="M15.2 9.2a4 4 0 0 1 0 5.6M18 6.6a7.7 7.7 0 0 1 0 10.8"/>',
    "webCapture": '<path d="M6.2 3h7.3l4.8 4.8v11.7a1.5 1.5 0 0 1-1.5 1.5H6.2a1.5 1.5 0 0 1-1.5-1.5v-15A1.5 1.5 0 0 1 6.2 3Z"/><path d="M13.3 3v4.9h4.9"/><path d="M11.5 10.2v6.6M8.8 14.2l2.7 2.7 2.7-2.7"/>',
    "textImage": '<rect x="4" y="3" width="16" height="11" rx="2.2"/><path d="m4.4 12.2 4.3-4 3.4 3.1 2.2-1.9 5.3 4.2"/><circle cx="15.6" cy="6.8" r="1.3"/><path d="M5 17.6h14M5 20.8h9"/>',
    "largeType": '<path d="m2.8 19 5.2-14 5.2 14M4.7 14.2h6.6"/><path d="m14.2 19 3.4-8.8L21 19M15.4 16.1h4.4"/>',
    "fontPreview": '<path d="m3.5 18.5 4.8-13 4.8 13M5.3 14h6"/><path d="M20.5 11.2v7.3M20.5 13.4a3 3 0 1 0 0 3"/>',
    "textCleanup": '<path d="M4 5.5h11M4 9.5h8M4 13.5h11M4 17.5h7"/><path d="m18.2 10.4.9 2.3 2.3.9-2.3.9-.9 2.3-.9-2.3-2.3-.9 2.3-.9Z"/><path d="m16.4 3.6.5 1.1 1.1.5-1.1.5-.5 1.1-.5-1.1-1.1-.5 1.1-.5Z"/>',
    "extractInfo": '<path d="M4 5h16M4 9.2h8M4 13.4h5.5M4 17.6h4.5"/><circle cx="15.5" cy="14" r="3.6"/><path d="m18.1 16.6 2.6 2.6"/>',
    "idNumber": '<rect x="2.8" y="5" width="18.4" height="14" rx="2.6"/><circle cx="8.6" cy="10.6" r="2"/><path d="M5.6 16c.5-1.6 1.6-2.4 3-2.4s2.5.8 3 2.4M14 10h4.4M14 13.4h3.2"/>',
    "lineTools": '<rect x="3" y="3.5" width="18" height="17" rx="3"/><circle cx="7.4" cy="8.4" r=".6" ' + F + '/><circle cx="7.4" cy="12" r=".6" ' + F + '/><circle cx="7.4" cy="15.6" r=".6" ' + F + '/><path d="M10.4 8.4h6.6M10.4 12h6.6M10.4 15.6h4.6"/>',
    "reminder": '<path d="m3.6 6.4 1.6 1.6 2.8-3M3.6 13.4l1.6 1.6 2.8-3"/><path d="M11 6.6h9.4M11 13.6h9.4"/><circle cx="5.6" cy="19.6" r="1.6"/><path d="M11 19.6h6.4"/>',
    "spellCheck": '<path d="m3 13.6 2.6-7 2.6 7M3.8 11.6h3.6M10.4 6.6v7M10.4 9.4c.4-.6 1-.9 1.8-.9 1.3 0 2 1 2 2.5s-.7 2.6-2 2.6c-.8 0-1.4-.3-1.8-.9"/><circle cx="17.2" cy="16.8" r="4"/><path d="m15.4 16.9 1.3 1.3 2.4-2.6"/>',
    "textDiff": '<rect x="3" y="4" width="18" height="16" rx="3"/><path d="M12 4v16"/><path d="M5.6 12h3.8M14.6 12h3.8M16.5 10.1v3.8"/>',
    "emojiSymbols": '<circle cx="12" cy="12" r="8.8"/><path d="M8.2 14.2a4.6 4.6 0 0 0 7.6 0"/><circle cx="9.1" cy="9.8" r="1.05" ' + F + '/><circle cx="14.9" cy="9.8" r="1.05" ' + F + '/>',
    "quickNote": '<path d="M3.4 13.4 5.5 5.6a2 2 0 0 1 1.9-1.5h9.2a2 2 0 0 1 1.9 1.5l2.1 7.8v4.6a2 2 0 0 1-2 2H5.4a2 2 0 0 1-2-2Z"/><path d="M3.6 13.4h4.6l1.1 2.2h5.4l1.1-2.2h4.6"/><path d="M12 6.6v5M9.8 9.6l2.2 2.2 2.2-2.2"/>',
    # ------------------------------------------------------------ convert
    "numberStats": '<path d="M17.6 5.2V4H6.2l6.2 8-6.2 8h11.4v-1.2"/>',
    "chart": '<path d="M3.6 3.6v16.8h16.8"/><rect x="7" y="12" width="3" height="5.6" rx=".8"/><rect x="12" y="7.4" width="3" height="10.2" rx=".8"/><rect x="17" y="10" width="3" height="7.6" rx=".8"/>',
    "changeCase": '<path d="m2.8 16.6 3.9-10.4 3.9 10.4M4.2 13.1h5"/><path d="M19.6 10.4v6.2M19.6 12.3a2.5 2.5 0 1 0 0 2.5"/><path d="M12.6 7.2c1.9-1.8 4.6-1.9 6.6-.2M17.4 4.8l1.9 2.3-2.4 1.6"/>',
    "encodeDecode": '<path d="m7.8 6.4-5 5.6 5 5.6M16.2 6.4l5 5.6-5 5.6"/><circle cx="9.9" cy="9.2" r="1.4"/><circle cx="14.1" cy="14.8" r="1.4"/><path d="m14.6 8.6-5.2 6.8"/>',
    "yamlJSON": '<rect x="3" y="3" width="18" height="18" rx="4"/><path d="M7.4 9.4h9.2M14 6.8l2.6 2.6-2.6 2.6M16.6 14.6H7.4M10 12l-2.6 2.6 2.6 2.6"/>',
    "formatXML": '<path d="m8 7.2-4.8 4.8L8 16.8M16 7.2l4.8 4.8-4.8 4.8M13.6 5l-3.2 14"/>',
    "formatSQL": '<ellipse cx="12" cy="5.8" rx="7.4" ry="2.8"/><path d="M4.6 5.8v12.4c0 1.5 3.3 2.8 7.4 2.8s7.4-1.3 7.4-2.8V5.8M4.6 12c0 1.5 3.3 2.8 7.4 2.8s7.4-1.3 7.4-2.8"/>',
    "tableConvert": '<rect x="3" y="3.6" width="18" height="16.8" rx="2.6"/><path d="M3 9.2h18M3 14.8h18M9.4 3.6v16.8M15 3.6v16.8"/>',
    "markdown": '<rect x="2.4" y="5" width="19.2" height="14" rx="2.6"/><path d="M5.6 15.2V8.8l2.8 3.4 2.8-3.4v6.4M16.4 8.8v6.2M14 12.8l2.4 2.4 2.4-2.4"/>',
    "toMarkdown": '<path d="M6.2 3h7.3l4.8 4.8v11.7a1.5 1.5 0 0 1-1.5 1.5H6.2a1.5 1.5 0 0 1-1.5-1.5v-15A1.5 1.5 0 0 1 6.2 3Z"/><path d="M13.3 3v4.9h4.9"/><path d="M9.4 10.4 8.6 17.4M12.4 10.4l-.8 7M7.6 12.6h5.6M7.2 15.2h5.6"/>',
    "markdownTOC": '<path d="M4 5.6h1.2M8.4 5.6H20M4 10.8h1.2M8.4 10.8H20M8.4 15.4h1.2M12.6 15.4H20M8.4 19.6h1.2M12.6 19.6H20"/>',
    "dateSpan": '<path d="M11 17.6H5.4A2.4 2.4 0 0 1 3 15.2V7a2.4 2.4 0 0 1 2.4-2.4h8.6A2.4 2.4 0 0 1 16.4 7v3.4M3 8.8h13.4M6.8 2.8v3.4M12.6 2.8v3.4"/><circle cx="17" cy="16.6" r="4.4"/><path d="M17 14.4v2.4l1.6 1.1"/>',
    "worldTime": '<circle cx="12" cy="12" r="8.8"/><path d="M3.4 12h17.2M12 3.2c2.3 2.4 3.5 5.3 3.5 8.8s-1.2 6.4-3.5 8.8c-2.3-2.4-3.5-5.3-3.5-8.8s1.2-6.4 3.5-8.8Z"/>',
    "numberConvert": '<circle cx="12" cy="12" r="8.8"/><path d="M10.6 7.4 9.4 16.6M14.6 7.4l-1.2 9.2M8 10.2h8.4M7.6 13.8H16"/>',
    "contrast": '<circle cx="12" cy="12" r="8.8"/><path d="M12 3.2a8.8 8.8 0 0 0 0 17.6Z" ' + F + '/>',
    # ------------------------------------------------------------ developer
    "hash": '<rect x="3" y="3" width="18" height="18" rx="4"/><path d="M10.4 7.2 9.2 16.8M14.8 7.2l-1.2 9.6M7.4 10.2h9.6M7 13.8h9.6"/>',
    "qrCode": '<rect x="3.6" y="3.6" width="6.6" height="6.6" rx="1.4"/><rect x="13.8" y="3.6" width="6.6" height="6.6" rx="1.4"/><rect x="3.6" y="13.8" width="6.6" height="6.6" rx="1.4"/><rect x="6" y="6" width="1.8" height="1.8" ' + F + '/><rect x="16.2" y="6" width="1.8" height="1.8" ' + F + '/><rect x="6" y="16.2" width="1.8" height="1.8" ' + F + '/><path d="M13.8 13.8h2.6v2.6M20.4 13.8v.1M13.8 20.4h.1M17.6 17.6h2.8v2.8h-2.8z"/>',
    "base64Image": '<rect x="2.6" y="4" width="18.8" height="16" rx="2.4"/><rect x="5.4" y="6.8" width="13.2" height="10.4" rx="1"/><path d="m5.8 15.6 3.4-3.2 2.6 2.4 1.8-1.6 4.6 3.6"/><circle cx="14.6" cy="9.6" r="1.1"/>',
    "random": '<rect x="3.4" y="3.4" width="17.2" height="17.2" rx="4"/><circle cx="8.2" cy="8.2" r="1.25" ' + F + '/><circle cx="15.8" cy="8.2" r="1.25" ' + F + '/><circle cx="12" cy="12" r="1.25" ' + F + '/><circle cx="8.2" cy="15.8" r="1.25" ' + F + '/><circle cx="15.8" cy="15.8" r="1.25" ' + F + '/>',
    "linkInspect": '<path d="M10.2 13.8a4.2 4.2 0 0 0 6 .2l3-3a4.2 4.2 0 0 0-6-6l-1.6 1.6"/><path d="M13.8 10.2a4.2 4.2 0 0 0-6-.2l-3 3a4.2 4.2 0 0 0 6 6l1.6-1.6"/>',
    "jwtDecode": '<circle cx="7.6" cy="12" r="4.2"/><path d="M11.8 12h9.2M18.2 12v3.6M15.4 12v2.6"/><circle cx="7.6" cy="12" r="1.2" ' + F + '/>',
    "regexTest": '<circle cx="12" cy="12" r="8.8"/><path d="M12 7v10M7.7 9.5l8.6 5M16.3 9.5l-8.6 5"/>',
    "cron": '<path d="M4.4 12a7.6 7.6 0 1 0 2.4-5.6"/><path d="M3.8 3.6v3.6h3.6"/><path d="M12 8v4.4l3 1.8"/>',
    "codeImage": '<rect x="2.6" y="4" width="18.8" height="16" rx="3"/><path d="M2.6 8h18.8"/><circle cx="5.2" cy="6" r=".5" ' + F + '/><circle cx="7" cy="6" r=".5" ' + F + '/><path d="m9.4 11.2-2.6 2.6 2.6 2.6M14.6 11.2l2.6 2.6-2.6 2.6M12.8 10.6l-1.6 6.4"/>',
    "jsonTypes": '<rect x="3" y="3" width="18" height="18" rx="4"/><path d="M10 7.4c-1.1 0-1.5.5-1.5 1.5v1.5c0 .9-.4 1.4-1.2 1.6.8.2 1.2.7 1.2 1.6v1.5c0 1 .4 1.5 1.5 1.5M14 7.4c1.1 0 1.5.5 1.5 1.5v1.5c0 .9.4 1.4 1.2 1.6-.8.2-1.2.7-1.2 1.6v1.5c0 1-.4 1.5-1.5 1.5"/>',
    "charInfo": '<path d="m3 17.6 4.6-12.2 4.6 12.2M4.6 13.4h6"/><circle cx="16.6" cy="14.2" r="3.6"/><path d="m19.2 16.8 2.2 2.2"/>',
    # ------------------------------------------------------------ screen & images
    "tableOCR": '<path d="M3 7.4V5a2 2 0 0 1 2-2h2.4M16.6 3H19a2 2 0 0 1 2 2v2.4M21 16.6V19a2 2 0 0 1-2 2h-2.4M7.4 21H5a2 2 0 0 1-2-2v-2.4"/><rect x="6.6" y="7.4" width="10.8" height="9.2" rx="1.2"/><path d="M6.6 10.6h10.8M6.6 13.6h10.8M10.4 7.4v9.2"/>',
    "scanCode": '<path d="M3 7.4V5a2 2 0 0 1 2-2h2.4M16.6 3H19a2 2 0 0 1 2 2v2.4M21 16.6V19a2 2 0 0 1-2 2h-2.4M7.4 21H5a2 2 0 0 1-2-2v-2.4"/><rect x="7" y="7" width="4" height="4" rx=".8"/><rect x="13" y="7" width="4" height="4" rx=".8"/><rect x="7" y="13" width="4" height="4" rx=".8"/><path d="M13 13h1.6v1.6M17 13v.1M13 17h.1M15.6 15.6H17V17h-1.4z"/>',
    "beautify": '<rect x="2.6" y="3.6" width="18.8" height="16.8" rx="3.6"/><rect x="6.2" y="7.4" width="11.6" height="9.2" rx="1.6"/><path d="m19 1.4.5 1.3 1.3.5-1.3.5-.5 1.3-.5-1.3-1.3-.5 1.3-.5Z"/>',
    "removeBackground": '<path d="m4.2 19.8 10.6-10.6M13.2 7.6l3.2 3.2"/><path d="m16.4 2.8.8 2 2 .8-2 .8-.8 2-.8-2-2-.8 2-.8Z"/><path d="m20 9.6.5 1.3 1.3.5-1.3.5-.5 1.3-.5-1.3-1.3-.5 1.3-.5Z"/><path d="m8.6 3.6.5 1.2 1.2.5-1.2.5-.5 1.2-.5-1.2-1.2-.5 1.2-.5Z"/>',
    "imageConvert": '<path d="M7.2 5.6 16.8 3a1.6 1.6 0 0 1 2 1.1l2.4 9a1.6 1.6 0 0 1-1.1 2l-1.6.4"/><rect x="2.8" y="8.4" width="13.6" height="12" rx="1.8"/><path d="m3.2 18.6 3.8-3.6 3 2.6 1.8-1.6 4.2 3.4"/><circle cx="12.2" cy="12.4" r="1.2"/>',
    "stitchImages": '<rect x="5" y="2.8" width="14" height="8.6" rx="1.8"/><rect x="5" y="12.6" width="14" height="8.6" rx="1.8"/><path d="m5.6 9.8 3.4-3 2.4 2.2 1.6-1.4 5.4 3.4M5.6 19.6l3.4-3 2.4 2.2 1.6-1.4 5.4 3.4"/>',
    "splitImage": '<rect x="3" y="3" width="18" height="18" rx="3"/><path d="M9 3v18M15 3v18M3 9h18M3 15h18"/>',
    "compareImages": '<rect x="2.6" y="4" width="18.8" height="16" rx="2.6"/><path d="M12 2v7.8M12 14.2V22"/><circle cx="12" cy="12" r="2.2"/><path d="m4.2 18 3.4-3.4 2 1.8"/><path d="m14.4 16.4 2.2-2 3.2 3" stroke-dasharray="1.6 1.8"/>',
    "appIcon": '<rect x="3" y="3" width="18" height="18" rx="5.4" stroke-dasharray="3 2.4"/><path d="m12 7.4 1.3 3.3 3.3 1.3-3.3 1.3-1.3 3.3-1.3-3.3L7.4 12l3.3-1.3Z"/>',
    "watermark": '<path d="M3 16.2c2.2-.4 3.2-2.8 3.6-5.8.3-2.4-.1-4.6-1.2-4.6-1.7 0-1.4 6.4.4 9.6 1.1 2 2.8 1.6 3.8-.4.8-1.6 1.2-4 2.4-4 1 0 .4 3.6 1.6 3.6s1.6-2.6 2.8-2.6c.9 0 .8 2.2 1.8 2.2.8 0 1.4-.8 2-1.6"/><path d="M3.2 20h17.6"/>',
    "idPhoto": '<rect x="4.4" y="2.8" width="15.2" height="18.4" rx="2.4"/><circle cx="12" cy="10" r="3.1"/><path d="M6.8 18.6c.9-2.6 2.8-3.9 5.2-3.9s4.3 1.3 5.2 3.9"/>',
    "cropImage": '<path d="M6.4 2.6v13.6a1.4 1.4 0 0 0 1.4 1.4h13.6"/><path d="M2.6 6.4h13.6a1.4 1.4 0 0 1 1.4 1.4v13.6"/>',
    "redact": '<path d="M3.2 12s3.2-6 8.8-6c1.3 0 2.5.3 3.6.8M20.8 12s-1 1.9-3 3.6M12 18c-5.6 0-8.8-6-8.8-6"/><path d="M9.4 13.4a3 3 0 0 1 4-4.2"/><path d="m4 20 16-16"/>',
    "palette": '<path d="M12 3a9 9 0 1 0 0 18c1.2 0 1.8-.9 1.8-1.8 0-1.4-1.4-1.8-1.4-3 0-1 .8-1.8 1.8-1.8h2.4A4.4 4.4 0 0 0 21 10c0-3.9-4-7-9-7Z"/><circle cx="7.8" cy="11.4" r="1.25" ' + F + '/><circle cx="10.4" cy="7.4" r="1.25" ' + F + '/><circle cx="15" cy="7.6" r="1.25" ' + F + '/>',
    "ruler": '<path d="M2.8 15.8 15.8 2.8l5.4 5.4L8.2 21.2Z"/><path d="m6.6 12 2 2M9.4 9.2l1.4 1.4M12.2 6.4l2 2M15 3.6l1.4 1.4"/>',
    # ------------------------------------------------------------ recording & presenting
    "screenRecord": '<circle cx="12" cy="12" r="8.8"/><circle cx="12" cy="12" r="4.4" ' + F + '/>',
    "voiceRecorder": '<rect x="8.6" y="2.8" width="6.8" height="11.6" rx="3.4"/><path d="M5.4 11a6.6 6.6 0 0 0 13.2 0M12 17.6v3.6M8.6 21.2h6.8"/>',
    "scrollCapture": '<rect x="4" y="2.8" width="16" height="12.4" rx="2.2"/><path d="M4 18.4v.6a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2v-.6" stroke-dasharray="2 2"/><path d="M12 6.4v5.6M9.4 9.6 12 12.2l2.6-2.6"/>',
    "showKeystrokes": '<rect x="3" y="3" width="18" height="18" rx="4"/><path d="M10 10V8.6a1.6 1.6 0 1 0-1.6 1.6H10Zm0 0h4m-4 0v4m4-4V8.6a1.6 1.6 0 1 1 1.6 1.6H14Zm0 0v4m0 0h-4m4 0v1.4a1.6 1.6 0 1 0 1.6-1.6H14Zm-4 0v1.4a1.6 1.6 0 1 1-1.6-1.6H10Z"/>',
    "screenPen": '<path d="M3 15.6c2.6-6.6 5.2-9.8 6.6-9 1.8 1-3.6 9.6-1.4 10.6 1.8.8 4.4-6.4 6.6-5.6 1.6.6-1 5 .6 5.6 1 .4 2.6-1 4.6-3.4"/>',
    "cameraBubble": '<circle cx="12" cy="12" r="8.8"/><circle cx="12" cy="9.8" r="3"/><path d="M6.4 18.6c1.2-2.4 3.2-3.6 5.6-3.6s4.4 1.2 5.6 3.6"/>',
    "pointerHighlight": '<path d="m10.4 9.6 9 3.6-3.8 1.4-1.4 3.8Z"/><path d="M7.2 3.4 8 6M3.4 7.2 6 8M3.6 12.6l2.2-1.2M12.6 3.6l-1.2 2.2"/>',
    "spotlight": '<path d="M8 3.6h8l-1 5.6H9Z"/><path d="M9 9.2h6v3.4l-1.2 1.6v6.2h-3.6v-6.2L9 12.6Z"/><path d="M12 15.6v1.8"/><path d="M5 2.6 6.2 4M19 2.6 17.8 4" />',
    "zoom": '<circle cx="10.4" cy="10.4" r="6.6"/><path d="m15.2 15.2 5.4 5.4M10.4 7.6v5.6M7.6 10.4h5.6"/>',
    "teleprompter": '<rect x="2.6" y="3.4" width="18.8" height="12.6" rx="2.4"/><path d="M7.4 7.4h9.2M6 10.2h12M8.4 13h7.2"/><path d="M12 16v4.4M8.4 20.6h7.2"/>',
    # ------------------------------------------------------------ files & system
    "folderTree": '<rect x="2.8" y="3" width="6.4" height="4.8" rx="1.2"/><rect x="12.4" y="9.6" width="8.8" height="4.8" rx="1.2"/><rect x="12.4" y="16.2" width="8.8" height="4.8" rx="1.2"/><path d="M6 7.8v10.8h6.4M6 12h6.4"/>',
    "codeStats": '<path d="M4 20.4h16"/><rect x="5" y="13" width="3" height="4.6" rx=".8"/><rect x="10.5" y="9.4" width="3" height="8.2" rx=".8"/><rect x="16" y="11.4" width="3" height="6.2" rx=".8"/><path d="m8.4 3.6-2.2 2.2 2.2 2.2M15.6 3.6l2.2 2.2-2.2 2.2M13 3.2l-2 5.2"/>',
    "compareFiles": '<path d="M9.4 6.4V5a2 2 0 0 1 2-2h5.2l3.6 3.6V15a2 2 0 0 1-2 2h-1.4"/><rect x="3.8" y="6.4" width="11.4" height="14.6" rx="2"/><path d="M6.6 11h5.8M6.6 14h5.8M6.6 17h3.6"/>',
    "batchRename": '<rect x="2.6" y="6.4" width="15.6" height="11.2" rx="2.4"/><path d="M6 12h.1M9 12h.1M12 12h.1"/><path d="m20.6 5.6-4.8 4.8-1.8.6.6-1.8 4.8-4.8a.9.9 0 0 1 1.2 1.2Z"/>',
    "zip": '<path d="M6.2 3h7.3l4.8 4.8v11.7a1.5 1.5 0 0 1-1.5 1.5H6.2a1.5 1.5 0 0 1-1.5-1.5v-15A1.5 1.5 0 0 1 6.2 3Z"/><path d="M10.6 3v1.6h1.6v1.6h-1.6v1.6h1.6v1.6h-1.6V11"/><rect x="9.8" y="11" width="3.2" height="4.4" rx="1"/>',
    "openInTerminal": '<rect x="2.6" y="3.8" width="18.8" height="16.4" rx="3"/><path d="m6.6 9.2 3 2.8-3 2.8M11.6 15.4h5.4"/>',
    "pdf": '<path d="M6.2 3h7.3l4.8 4.8v11.7a1.5 1.5 0 0 1-1.5 1.5H6.2a1.5 1.5 0 0 1-1.5-1.5v-15A1.5 1.5 0 0 1 6.2 3Z"/><path d="M13.3 3v4.9h4.9"/><path d="M8 16.8c1.8-1.4 3-3.6 3.4-6.2.2-1.2-.9-1.6-1.2-.4-.4 1.8 1.6 4 4.6 4.8 1 .3 1.8-.6.8-1-2-.6-5.4.4-7 2.4-.4.4.1.8.4.4Z"/>',
    "videoConvert": '<rect x="3.4" y="3" width="17.2" height="18" rx="2.4"/><path d="M7 3v18M17 3v18M3.4 7.6H7M3.4 12H7M3.4 16.4H7M17 7.6h3.6M17 12h3.6M17 16.4h3.6"/><path d="m10.6 9.6 3.6 2.4-3.6 2.4Z"/>',
    "trimMedia": '<circle cx="6.4" cy="6.6" r="3"/><circle cx="6.4" cy="17.4" r="3"/><path d="M8.8 8.4 20 17.4M8.8 15.6 20 6.6"/>',
    "transcribe": '<path d="M5 4h14a2.4 2.4 0 0 1 2.4 2.4v8.2a2.4 2.4 0 0 1-2.4 2.4h-5.8L8.8 20.6V17H5a2.4 2.4 0 0 1-2.4-2.4V6.4A2.4 2.4 0 0 1 5 4Z"/><path d="M7 8.6v4M9.6 7.4v6.4M12.2 9.2v2.8M14.8 8v5.2M17.4 9.6v2"/>',
    "airDrop": '<circle cx="12" cy="13.6" r="1.6" ' + F + '/><path d="M8.6 17a4.8 4.8 0 1 1 6.8 0M6 19.6a8.4 8.4 0 1 1 12 0"/>',
    "sendToPhone": '<rect x="7.2" y="2.8" width="9.6" height="18.4" rx="2.4"/><path d="M10.8 5.4h2.4"/><path d="M4.6 9a4.6 4.6 0 0 0 0 6M2.4 7.2a7.6 7.6 0 0 0 0 9.6M19.4 9a4.6 4.6 0 0 1 0 6M21.6 7.2a7.6 7.6 0 0 1 0 9.6"/>',
    "windowLayout": '<rect x="2.6" y="4" width="18.8" height="16" rx="2.6"/><path d="M12 4v16"/><rect x="4.4" y="5.8" width="5.8" height="12.4" rx="1" ' + F + ' opacity=".35"/>',
    "menuShortcuts": '<path d="M9 9V6.6A2.4 2.4 0 1 0 6.6 9H9Zm0 0h6m-6 0v6m6-6V6.6A2.4 2.4 0 1 1 17.4 9H15Zm0 0v6m0 0H9m6 0v2.4a2.4 2.4 0 1 0 2.4-2.4H15Zm-6 0v2.4A2.4 2.4 0 1 1 6.6 15H9Z"/>',
    "keepAwake": '<path d="M4.6 9.4h12.2v4.4a6.1 6.1 0 0 1-12.2 0Z"/><path d="M16.8 10.6h1.4a2.4 2.4 0 0 1 0 4.8h-1.8M3 21h15.4"/><path d="M8.4 2.8c-.8 1 .8 1.8 0 3.2M12.2 2.8c-.8 1 .8 1.8 0 3.2"/>',
    "systemActions": '<rect x="2.8" y="3.6" width="18.4" height="7.4" rx="3.7"/><circle cx="17.4" cy="7.3" r="2.2" ' + F + '/><rect x="2.8" y="13" width="18.4" height="7.4" rx="3.7"/><circle cx="6.6" cy="16.7" r="2.2"/>',
    "quitApps": '<rect x="3" y="3" width="18" height="18" rx="5.4"/><path d="m9 9 6 6M15 9l-6 6"/>',
    "uninstallApp": '<rect x="3" y="3" width="18" height="18" rx="4"/><path d="M7.4 8.6h9.2M10.4 8.6V7.2h3.2v1.4M8.6 8.6l.6 8.2h5.6l.6-8.2"/>',
    "appInfo": '<rect x="3" y="3" width="18" height="18" rx="4"/><path d="M12 11v5.6M10.4 16.6h3.2"/><circle cx="12" cy="7.8" r="1.1" ' + F + '/>',
    "batteryInfo": '<rect x="2.4" y="7" width="17" height="10" rx="2.6"/><path d="M21.6 10.6v2.8"/><rect x="4.6" y="9.2" width="12.6" height="5.6" rx="1.2" ' + F + '/>',
    "systemInfo": '<rect x="4.6" y="4.4" width="14.8" height="10.8" rx="1.8"/><path d="M2.4 19.2h19.2l-1.4-2.6H3.8Z"/><path d="M12 9v3.6"/><circle cx="12" cy="7.2" r=".9" ' + F + '/>',
    "soundDevices": '<rect x="5.4" y="2.8" width="13.2" height="18.4" rx="2.6"/><circle cx="12" cy="14.4" r="3.4"/><circle cx="12" cy="7.2" r="1.4"/>',
    "resolution": '<rect x="2.6" y="3.6" width="18.8" height="12.8" rx="2.2"/><path d="M9 20.4h6M12 16.4v4"/><path d="M6.4 9.2V7.2h2M17.6 9.2V7.2h-2M6.4 10.8v2h2M17.6 10.8v2h-2"/>',
    "diskSpeed": '<path d="M3.6 16.4a8.4 8.4 0 1 1 16.8 0"/><path d="m12 16.4 4.2-5.6"/><circle cx="12" cy="16.4" r="1.4" ' + F + '/><path d="M5.8 10.4l1.2.8M12 6.2v1.4M18.2 10.4l-1.2.8M3.6 20.4h16.8"/>',
    "cleanKeyboard": '<rect x="2.4" y="6" width="19.2" height="12" rx="2.4"/><path d="M6 9.4h.1M9.4 9.4h.1M12.8 9.4h.1M16.2 9.4h.1M6 12.4h.1M9.4 12.4h.1M12.8 12.4h.1M16.2 12.4h1.8M7.6 15.2h8.8"/>',
    "timer": '<circle cx="12" cy="13.4" r="7.8"/><path d="M12 13.4V9.2M9.6 2.8h4.8M18.6 6.6l1.4-1.4"/>',
    "focusSounds": '<path d="M3.6 15v-3a8.4 8.4 0 0 1 16.8 0v3"/><rect x="3.6" y="13.6" width="4.2" height="7" rx="1.6"/><rect x="16.2" y="13.6" width="4.2" height="7" rx="1.6"/>',
    "folderTools": '<path d="M2.8 7.2V5.6a1.6 1.6 0 0 1 1.6-1.6h4.4l2 2.2h8.8a1.6 1.6 0 0 1 1.6 1.6v1.8"/><path d="M11.4 19.2H4.4a1.6 1.6 0 0 1-1.6-1.6V7.2h18.4v3.8"/><circle cx="17.4" cy="16.4" r="2"/><path d="M17.4 12.6v1.6M17.4 18.6v1.6M13.6 16.4h1.6M19.6 16.4h1.6M14.7 13.7l1.1 1.1M19 18l1.1 1.1M14.7 19.1l1.1-1.1M19 14.8l1.1-1.1"/>',
    "tidyFolder": '<path d="M2.8 7.2V5.6a1.6 1.6 0 0 1 1.6-1.6h4.4l2 2.2h8.8a1.6 1.6 0 0 1 1.6 1.6v1.8"/><path d="M2.8 7.2h18.4v10.4a1.6 1.6 0 0 1-1.6 1.6H4.4a1.6 1.6 0 0 1-1.6-1.6Z"/><path d="M7 11.2h3.4M7 14.6h3.4M13.6 11.2H17M13.6 14.6H17"/>',
    "newFile": '<path d="M13.6 21H6.2a1.5 1.5 0 0 1-1.5-1.5v-15A1.5 1.5 0 0 1 6.2 3h7.3l4.8 4.8v4.4"/><path d="M13.3 3v4.9h4.9"/><path d="M18.4 15v6M15.4 18h6"/>',
    "fileEncoding": '<path d="M5 4.4A1.4 1.4 0 0 1 6.4 3h12.6v15H6.6A1.6 1.6 0 0 0 5 19.6Z"/><path d="M5 19.6A1.4 1.4 0 0 0 6.4 21H19v-3"/><path d="m9 14.4 2.4-6.6 2.4 6.6M9.8 12.4h3.2"/>',
    "similarPhotos": '<rect x="2.8" y="7.4" width="13.6" height="13.6" rx="2"/><path d="M6.6 4.8V5a1.8 1.8 0 0 1 1.8-1.8H19a2 2 0 0 1 2 2v10.4a1.8 1.8 0 0 1-1.8 1.8H19"/><path d="m3.2 18.8 3.6-3.4 2.8 2.4 1.8-1.6 4.6 3.8"/><circle cx="12" cy="11.6" r="1.2"/>',
    "mediaInfo": '<path d="M12 18H4.6a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h10.4a2 2 0 0 1 2 2v5.4"/><path d="M6 3v15M13.6 3v8M2.6 7.2H6M2.6 13.8H6M13.6 7.2H17"/><circle cx="17.6" cy="17.4" r="4"/><path d="M17.6 16.6v2.8"/><circle cx="17.6" cy="15" r=".6" ' + F + '/>',
    "subtitles": '<rect x="2.6" y="4.6" width="18.8" height="14.8" rx="3"/><path d="M10.4 10.2a2.4 2.4 0 1 0 0 3.6M17 10.2a2.4 2.4 0 1 0 0 3.6"/>',
    "encryptFiles": '<path d="M12.4 21H6.2a1.5 1.5 0 0 1-1.5-1.5v-15A1.5 1.5 0 0 1 6.2 3h7.3l4.8 4.8v2"/><path d="M13.3 3v4.9h4.9"/><rect x="13.6" y="14.6" width="7.6" height="6.2" rx="1.4"/><path d="M15.4 14.6v-1.6a2 2 0 0 1 4 0v1.6"/>',
}


def glyph(pid):
    return G[pid]


def svg(pid, cls="glyph", sw="1.7"):
    return (f'<svg class="{cls}" viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" '
            f'stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round">{G[pid]}</svg>')
