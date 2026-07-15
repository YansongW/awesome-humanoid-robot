#!/usr/bin/env python3
"""
Normalize Markdown heading levels in the Wiki so that headings never skip a
level (e.g. ## -> ####). Code blocks are ignored.

Usage:
    python scripts/normalize_wiki_headings.py [--path wiki/docs/chapters/chapter-04.md]
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).parent.parent
WIKI_DIR = ROOT / "wiki" / "docs"


def normalize_file(p: Path) -> bool:
    text = p.read_text(encoding="utf-8")
    lines = text.splitlines(keepends=True)
    in_code = False
    prev_level = 0
    first_heading = True
    changed = False

    out_lines: list[str] = []
    for line in lines:
        stripped = line.strip()
        if stripped.startswith("```"):
            in_code = not in_code
            out_lines.append(line)
            continue
        if in_code:
            out_lines.append(line)
            continue

        m = re.match(r"^(#{1,6})(\s+.*)$", line)
        if not m:
            out_lines.append(line)
            continue

        level = len(m.group(1))
        content = m.group(2)

        if first_heading:
            # Keep the first heading exactly as-is (chapter title).
            first_heading = False
            prev_level = level
            out_lines.append(line)
            continue

        if level > prev_level + 1:
            new_level = prev_level + 1
            out_lines.append("#" * new_level + content + ("\n" if line.endswith("\n") else ""))
            level = new_level
            changed = True
        else:
            out_lines.append(line)

        prev_level = level

    if changed:
        p.write_text("".join(out_lines), encoding="utf-8")
    return changed


def main() -> int:
    parser = argparse.ArgumentParser(description="Normalize Wiki heading levels.")
    parser.add_argument("--path", type=Path, default=None, help="Single file to normalize")
    args = parser.parse_args()

    if args.path:
        files = [args.path]
    else:
        files = sorted(WIKI_DIR.rglob("*.md"))

    changed_files: list[str] = []
    for p in files:
        if normalize_file(p):
            changed_files.append(str(p.relative_to(ROOT)))

    print(f"Normalized {len(changed_files)} file(s)")
    for f in changed_files:
        print(f"  - {f}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
