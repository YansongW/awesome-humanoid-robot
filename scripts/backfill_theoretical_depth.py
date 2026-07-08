#!/usr/bin/env python3
"""Backfill missing theoretical_depth on existing entries based on entity type.

Usage:
    source .venv/bin/activate
    python scripts/backfill_theoretical_depth.py --dry-run
    python scripts/backfill_theoretical_depth.py
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path

import yaml

from ai4sci_lib import config


TYPE_TO_DEPTH = {
    "paper": ["system"],
    "robot_system": ["system"],
    "component": ["system"],
    "material": ["system"],
    "technology": ["method"],
    "method": ["method"],
    "algorithm": ["method"],
    "formalism": ["formalism"],
    "equation": ["formalism"],
    "operator": ["formalism"],
    "variable": ["formalism"],
    "constant": ["formalism"],
    "principle": ["principle"],
    "theorem": ["principle"],
    "foundation": ["foundation"],
    "benchmark": ["system"],
    "dataset": ["system"],
    "company": ["system"],
    "oem": ["system"],
    "tier1_supplier": ["system"],
    "tier2_supplier": ["system"],
    "component_manufacturer": ["system"],
    "standard": ["system"],
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Backfill theoretical_depth on entries.")
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print changes without writing them.",
    )
    return parser.parse_args()


def update_file(path: Path, dry_run: bool) -> bool:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---"):
        return False

    # Split frontmatter and body.
    parts = text.split("---", 2)
    if len(parts) < 3:
        return False
    frontmatter_text = parts[1]
    body = parts[2]

    data = yaml.safe_load(frontmatter_text)
    if not isinstance(data, dict):
        return False

    if data.get("theoretical_depth"):
        return False

    entity_type = data.get("type", "paper")
    depth = TYPE_TO_DEPTH.get(entity_type, ["system"])
    data["theoretical_depth"] = depth

    new_frontmatter = yaml.dump(data, sort_keys=False, allow_unicode=True, default_flow_style=False)
    new_text = f"---\n{new_frontmatter}---{body}"

    if dry_run:
        print(f"[dry-run] {path}: would set theoretical_depth={depth}")
    else:
        path.write_text(new_text, encoding="utf-8")
        print(f"[updated] {path}: theoretical_depth={depth}")
    return True


def main() -> int:
    args = parse_args()
    updated = 0
    for path in config.RESEARCH_DIR.rglob("*.md"):
        if update_file(path, args.dry_run):
            updated += 1
    print(f"\n{'[dry-run] ' if args.dry_run else ''}Updated {updated} entry file(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
