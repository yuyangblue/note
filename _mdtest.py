import markdown
import material.extensions.emoji as emoji

html = """<div class="course-list">

<p><a href="B站.md"><strong>B站</strong></a></p>
<p><a href="学习路线.md"><strong>学习路线</strong></a></p>

</div>"""

exts = [
    "admonition",
    "footnotes",
    "toc",
    "attr_list",
    "md_in_html",
    "pymdownx.arithmatex",
    "pymdownx.highlight",
    "pymdownx.superfences",
    "pymdownx.tabbed",
    "pymdownx.details",
    "pymdownx.emoji",
    "pymdownx.caret",
    "pymdownx.mark",
    "pymdownx.tilde",
]
ext_cfg = {
    "pymdownx.emoji": {
        "emoji_index": emoji.twemoji,
        "emoji_generator": emoji.to_svg,
    }
}
md = markdown.Markdown(extensions=exts, extension_configs=ext_cfg)
out = md.convert(html)
print(out)
