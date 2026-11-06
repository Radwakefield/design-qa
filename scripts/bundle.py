#!/usr/bin/env python3
"""Bundle a prototype folder into one shareable HTML file.

Inlines every local stylesheet (<link rel="stylesheet" href="...">) and script
(<script src="...">), removes the Agentation block (from its
"<!-- Agentation:" comment through the end of its <script>), optionally
replaces the <title>, and writes the result. The controls panel is kept.

Usage:
    python3 -I bundle.py <prototype folder> <output .html> [--title "Title"]
"""

import argparse
import pathlib
import re
import sys


def bundle(folder: pathlib.Path, title: str | None) -> str:
    html = (folder / "index.html").read_text()

    def inline_css(match: re.Match) -> str:
        path = folder / match.group(1)
        return "<style>\n" + path.read_text() + "\n</style>"

    def inline_js(match: re.Match) -> str:
        path = folder / match.group(1)
        return "<script>\n" + path.read_text() + "\n</script>"

    html = re.sub(r'<link rel="stylesheet" href="(?!https?:)([^"]+)"\s*/?>', inline_css, html)
    html = re.sub(r'<script src="(?!https?:)([^"]+)"></script>', inline_js, html)
    html = re.sub(r"\n\s*<!-- Agentation:.*?</script>", "", html, flags=re.S)
    html = re.sub(r'\n\s*<div id="agentation-root"></div>', "", html)
    if title:
        html = re.sub(r"<title>.*?</title>", f"<title>{title}</title>", html, flags=re.S)
    return html


def check(html: str) -> list[str]:
    problems = []
    if "agentation" in html.lower():
        problems.append("Agentation is still present (is the '<!-- Agentation:' comment marker there?)")
    if re.search(r'<link rel="stylesheet" href="(?!https?:)', html):
        problems.append("a local stylesheet link was not inlined")
    if re.search(r'<script src="(?!https?:)', html):
        problems.append("a local script was not inlined")
    return problems


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("folder", type=pathlib.Path)
    parser.add_argument("output", type=pathlib.Path)
    parser.add_argument("--title")
    args = parser.parse_args()

    html = bundle(args.folder, args.title)
    problems = check(html)
    if problems:
        for problem in problems:
            print(f"error: {problem}", file=sys.stderr)
        return 1

    args.output.parent.mkdir(parents=True, exist_ok=True)
    # Write a fresh file rather than overwriting in place, so macOS doesn't
    # carry over attributes from an earlier copy.
    if args.output.exists():
        args.output.unlink()
    args.output.write_text(html)
    print(f"wrote {args.output} ({len(html.encode()):,} bytes)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
