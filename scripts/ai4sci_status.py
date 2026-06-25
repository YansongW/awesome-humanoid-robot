#!/usr/bin/env python3
"""AI4Sci workstream status dashboard.

Prints a summary of active workstreams, pending reviews, and recent run results.

Usage:
    source .venv/bin/activate
    python scripts/ai4sci_status.py
    python scripts/ai4sci_status.py --watch  # not implemented, placeholder
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from ai4sci_lib import config, staging, tracking


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Show AI4Sci workstream status.")
    parser.add_argument(
        "--workstreams-dir",
        type=Path,
        default=config.STAGING_DIR / "workstreams",
        help="Base directory containing workstream staging dirs.",
    )
    return parser.parse_args()


def _count_staged(base_dir: Path) -> tuple[int, int]:
    entries = staging.list_staged_entries(base_dir)
    relationships = staging.list_staged_relationships(base_dir)
    return len(entries), len(relationships)


def main() -> int:
    args = parse_args()

    print("# AI4Sci Workstream Status\n")

    # Default staging area.
    default_entries, default_rels = _count_staged(config.STAGING_DIR)
    print(f"Default staging area ({config.STAGING_DIR}):")
    print(f"  Entries pending review:    {default_entries}")
    print(f"  Relationships pending:     {default_rels}\n")

    # Workstreams.
    if not args.workstreams_dir.exists():
        print("No workstream staging directories found.")
        return 0

    progress = tracking.load_all_progress(config.STAGING_DIR)
    print(f"Workstreams ({args.workstreams_dir}):\n")

    for ws_dir in sorted(args.workstreams_dir.iterdir()):
        if not ws_dir.is_dir():
            continue
        name = ws_dir.name
        entries, rels = _count_staged(ws_dir)
        prog = progress.get(name, {})

        print(f"  {name}")
        print(f"    Output dir:              {ws_dir}")
        print(f"    Entries pending review:  {entries}")
        print(f"    Relationships pending:   {rels}")
        print(f"    Last run:                {prog.get('last_run_at', 'never')}")
        print(f"    Total processed:         {prog.get('total', 0)}")
        print(f"    Success:                 {prog.get('success', 0)}")
        print(f"    Skipped:                 {prog.get('skipped', 0)}")
        print(f"    Duplicate:               {prog.get('duplicate', 0)}")
        print(f"    Error:                   {prog.get('error', 0)}")
        print(f"    Pending review (tracked):{prog.get('pending_review', 0)}")
        print()

    return 0


if __name__ == "__main__":
    sys.exit(main())
