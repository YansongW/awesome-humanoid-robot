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
import os
import subprocess
import sys
from pathlib import Path

import yaml

from ai4sci_lib import config


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Run the next unexecuted AI4Sci workstream."
    )
    parser.add_argument(
        "--max-papers",
        type=int,
        default=5,
        help="Maximum papers to process per workstream (default: 5).",
    )
    parser.add_argument(
        "--max-workers",
        type=int,
        default=2,
        help="Parallel workers inside the batch pipeline (default: 2).",
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


def load_workstream_config(path: Path) -> dict:
    """Load a workstream YAML config, returning an empty dict on error."""
    try:
        with open(path, encoding="utf-8") as f:
            return yaml.safe_load(f) or {}
    except Exception:
        return {}


def list_workstreams(workstreams_dir: Path) -> list[Path]:
    """Return all workstream config files recursively, sorted by priority then path."""
    if not workstreams_dir.exists():
        return []
    paths = [p for p in workstreams_dir.rglob("*.yaml") if p.is_file()]

    def sort_key(p: Path) -> tuple[int, str]:
        cfg = load_workstream_config(p)
        priority = cfg.get("priority", 10)
        try:
            priority = int(priority)
        except Exception:
            priority = 10
        return (priority, str(p))

    return sorted(paths, key=sort_key)


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


def is_exhausted(name: str) -> bool:
    """Skip workstreams that have failed or stagnated without producing entries."""
    summary_path = config.STAGING_DIR / "workstreams" / name / "logs" / "summary.json"
    if not summary_path.exists():
        return False
    try:
        summary = json.loads(summary_path.read_text(encoding="utf-8"))
    except Exception:
        return False
    run_count = summary.get("run_count", 0)
    success = summary.get("success", 0)
    pending = summary.get("pending_review", 0)
    error = summary.get("error", 0)
    total = summary.get("total", 0)
    # If the last run discovered no candidates at all, do not retry.
    if run_count >= 1 and total == 0:
        return True
    # After one full run with no successes and no errors (i.e. all candidates
    # were skipped as low-relevance or duplicates), stop retrying immediately.
    if run_count >= 1 and success == 0 and pending == 0 and error == 0 and total > 0:
        return True
    # After two full runs with errors and no usable outputs, stop retrying.
    if run_count >= 2 and success == 0 and pending == 0 and error > 0:
        return True
    # Legacy fallback: skip if we have run many times with no successes at all.
    if run_count >= 3 and success == 0 and pending == 0:
        return True
    return False


def main() -> int:
    args = parse_args()
    workstreams = list_workstreams(args.workstreams_dir)
    if not workstreams:
        print("[run_next] No workstream configs found.")
        return 0

    next_ws: Path | None = None
    for ws_path in workstreams:
        cfg = load_workstream_config(ws_path)
        name = cfg.get("name", ws_path.stem)
        if has_successful_output(name):
            continue
        if is_exhausted(name):
            print(
                f"[run_next] Skipping exhausted workstream: {name} "
                f"({ws_path.relative_to(args.workstreams_dir)})"
            )
            continue
        next_ws = ws_path
        break

    if next_ws is None:
        print("[run_next] All workstreams have already produced staged outputs.")
        return 0

    rel = next_ws.relative_to(args.workstreams_dir)
    name = load_workstream_config(next_ws).get("name", next_ws.stem)
    print(f"[run_next] Next workstream: {name} ({rel})")

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
    result = subprocess.run(cmd, cwd=config.ROOT, env={**os.environ, "PYTHONUNBUFFERED": "1"})
    return result.returncode


if __name__ == "__main__":
    sys.exit(main())
