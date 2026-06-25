#!/usr/bin/env python3
"""Run the next unexecuted workstream from the workstream tree.

This is intended to be called repeatedly by a scheduler or daemon loop. It
picks the first workstream whose staging directory has no successful entries,
runs it with conservative limits, and exits.

Usage:
    source .venv/bin/activate
    python scripts/ai4sci_run_next_workstream.py
    python scripts/ai4sci_run_next_workstream.py --max-papers 3 --max-workers 1
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path

from ai4sci_lib import config


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Run the next unexecuted AI4Sci workstream."
    )
    parser.add_argument(
        "--max-papers",
        type=int,
        default=3,
        help="Maximum papers to process per workstream (default: 3).",
    )
    parser.add_argument(
        "--max-workers",
        type=int,
        default=1,
        help="Parallel workers inside the batch pipeline (default: 1).",
    )
    parser.add_argument(
        "--workstreams-dir",
        type=Path,
        default=config.WORKSTREAMS_DIR,
        help="Directory containing workstream YAML configs.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print the next workstream without running it.",
    )
    return parser.parse_args()


def list_workstreams(workstreams_dir: Path) -> list[Path]:
    """Return all workstream config files recursively, sorted."""
    if not workstreams_dir.exists():
        return []
    return sorted(p for p in workstreams_dir.rglob("*.yaml") if p.is_file())


def has_successful_output(name: str) -> bool:
    """Check whether a workstream has already produced staged entries."""
    summary_path = config.STAGING_DIR / "workstreams" / name / "logs" / "summary.json"
    if not summary_path.exists():
        return False
    try:
        summary = json.loads(summary_path.read_text(encoding="utf-8"))
        return summary.get("success", 0) > 0 or summary.get("pending_review", 0) > 0
    except Exception:
        return False


def main() -> int:
    args = parse_args()
    workstreams = list_workstreams(args.workstreams_dir)
    if not workstreams:
        print("[run_next] No workstream configs found.")
        return 0

    next_ws: Path | None = None
    for ws_path in workstreams:
        if not has_successful_output(ws_path.stem):
            next_ws = ws_path
            break

    if next_ws is None:
        print("[run_next] All workstreams have already produced staged outputs.")
        return 0

    rel = next_ws.relative_to(args.workstreams_dir)
    print(f"[run_next] Next workstream: {next_ws.stem} ({rel})")

    if args.dry_run:
        return 0

    cmd = [
        sys.executable,
        str(config.ROOT / "scripts" / "ai4sci_batch_pipeline.py"),
        str(next_ws),
        "--max-papers",
        str(args.max_papers),
        "--max-workers",
        str(args.max_workers),
    ]
    result = subprocess.run(cmd, cwd=config.ROOT)
    return result.returncode


if __name__ == "__main__":
    sys.exit(main())
