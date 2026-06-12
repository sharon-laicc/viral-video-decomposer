#!/usr/bin/env python3
from html.parser import HTMLParser
from pathlib import Path
import sys


REQUIRED_TEXT = [
    "Viral Video Lab",
    "topbar-inner",
    "style-switch",
    'body[data-style="swiss"]',
    'id="overview"',
    'id="shots"',
    'id="blueprint"',
    'id="prompt"',
    'class="sheet"',
    'class="shot"',
    "data-style-option=\"editorial\"",
    "data-style-option=\"swiss\"",
]

FORBIDDEN_TEXT = [
    "JSON Brief（机器可读）",
    "<!-- JSON Brief",
    "shot-placeholder",
]


class ImageParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.srcs = []
        self.shot_image_srcs = []
        self.in_shot = False

    def handle_starttag(self, tag, attrs):
        values = dict(attrs)
        class_name = values.get("class", "")
        if tag.lower() in {"section", "div"} and "shot" in class_name.split():
            self.in_shot = True
        if tag.lower() == "img":
            src = values.get("src")
            if src:
                self.srcs.append(src)
                if self.in_shot:
                    self.shot_image_srcs.append(src)

    def handle_endtag(self, tag):
        if tag.lower() in {"section", "div"} and self.in_shot:
            self.in_shot = False


def main():
    if len(sys.argv) != 2:
        print("Usage: validate_report.py <report.html>", file=sys.stderr)
        return 2

    html_path = Path(sys.argv[1]).resolve()
    html = html_path.read_text(encoding="utf-8")
    failed = False

    for token in REQUIRED_TEXT:
        if token not in html:
            print(f"missing required report token: {token}")
            failed = True

    for token in FORBIDDEN_TEXT:
        if token in html:
            print(f"forbidden report token found: {token}")
            failed = True

    parser = ImageParser()
    parser.feed(html)
    if not parser.srcs:
        print("missing image tags")
        failed = True

    if not any("contact_sheet" in src for src in parser.srcs):
        print("missing contact_sheet image reference")
        failed = True

    if not any(Path(src).name.startswith("S001") for src in parser.srcs):
        print("missing S001 shot image reference")
        failed = True

    if len(parser.shot_image_srcs) < 6:
        print(f"too few real shot-card images: {len(parser.shot_image_srcs)}")
        failed = True

    for src in parser.srcs:
        if src.startswith(("http://", "https://", "data:")):
            continue
        target = (html_path.parent / src).resolve()
        if not target.exists():
            print(f"broken image path: {src}")
            failed = True

    if failed:
        return 1

    print("report validation passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
