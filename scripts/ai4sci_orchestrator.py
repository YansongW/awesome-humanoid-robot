#!/usr/bin/env python3
"""AI4Sci multi-agent workstream orchestrator.

Discovers workstream configs under `scripts/ai4sci_workstreams/` and dispatches
one sub-agent per workstream. Each sub-agent runs `scripts/ai4sci_batch_pipeline.py`
for its config. Results are staged in `.staging/workstreams/<name>/`.

Usage:
    source .venv/bin/activate
    python scripts/ai4sci_orchestrator.py
    python scripts/ai4sci_orchestrator.py --workstreams vla,companies
    python scripts/ai4sci_orchestrator.py --dry-run --max-papers 3
    python scripts/ai4sci_orchestrator.py --max-workers 2 --max-papers 5
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from concurrent.futures import ProcessPoolExecutor, as_completed
from datetime import datetime
from pathlib import Path

import yaml

from ai4sci_lib import config, tracking


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Orchestrate multiple AI4Sci workstreams in parallel."
    )
    parser.add_argument(
        "--workstreams",
        default=None,
        help="Comma-separated list of workstream names to run (default: all).",
    )
    parser.add_argument(
        "--workstreams-dir",
        type=Path,
        default=config.WORKSTREAMS_DIR,
        help="Directory containing workstream YAML configs.",
    )
    parser.add_argument(
        "--max-papers",
        type=int,
        default=None,
        help="Override max papers per workstream.",
    )
    parser.add_argument(
        "--max-workers",
        type=int,
        default=2,
        help="Maximum parallel workstreams to run (default: 2).",
    )
    parser.add_argument(
        "--max-batch-workers",
        type=int,
        default=2,
        help="Maximum parallel workers passed to each batch pipeline (default: 2).",
    )
    parser.add_argument(
        "--relevance-threshold",
        choices=["low", "medium", "high"],
        default=None,
        help="Override relevance threshold.",
    )
    parser.add_argument(
        "--model",
        default=None,
        help="LLM model name override.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Run in dry-run mode (no files written).",
    )
    parser.add_argument(
        "--skip-discovery",
        action="store_true",
        help="Skip discovery; only process explicit paper_ids.",
    )
    return parser.parse_args()


def list_workstreams(workstreams_dir: Path) -> list[Path]:
    """Return all workstream config files recursively under the directory."""
    if not workstreams_dir.exists():
        return []
    return sorted(p for p in workstreams_dir.rglob("*.yaml") if p.is_file())


def run_workstream(
    config_path: Path,
    max_papers: int | None,
    max_batch_workers: int,
    relevance_threshold: str | None,
    model: str | None,
    dry_run: bool,
    skip_discovery: bool,
) -> dict:
    """Run the batch pipeline for a single workstream and return a status dict."""
    name = config_path.stem
    cmd = [
        sys.executable,
        str(config.ROOT / "scripts" / "ai4sci_batch_pipeline.py"),
        str(config_path),
        "--max-batch-workers", str(max_batch_workers),
    ]
    if max_papers is not None:
        cmd.extend(["--max-papers", str(max_papers)])
    if relevance_threshold:
        cmd.extend(["--relevance-threshold", relevance_threshold])
    if model:
        cmd.extend(["--model", model])
    if dry_run:
        cmd.append("--dry-run")
    if skip_discovery:
        cmd.append("--skip-discovery")

    result = subprocess.run(
        cmd,
        cwd=config.ROOT,
        capture_output=True,
        text=True,
        encoding="utf-8",
    )

    return {
        "name": name,
        "config": str(config_path),
        "returncode": result.returncode,
        "stdout": result.stdout,
        "stderr": result.stderr,
    }


def main() -> int:
    args = parse_args()

    workstream_paths = list_workstreams(args.workstreams_dir)
    if args.workstreams:
        selected = {w.strip() for w in args.workstreams.split(",")}
        workstream_paths = [p for p in workstream_paths if p.stem in selected]

    if not workstream_paths:
        print("No workstream configs found.", file=sys.stderr)
        return 1

    print(f"[orchestrator] Discovered {len(workstream_paths)} workstream(s):")
    for p in workstream_paths:
        rel = p.relative_to(args.workstreams_dir)
        print(f"  - {p.stem} ({rel})")

    print(f"[orchestrator] Running up to {args.max_workers} workstream(s) in parallel...")

    results: list[dict] = []
    if args.max_workers <= 1:
        for ws_path in workstream_paths:
            result = run_workstream(
                ws_path,
                args.max_papers,
                args.max_batch_workers,
                args.relevance_threshold,
                args.model,
                args.dry_run,
                args.skip_discovery,
            )
            results.append(result)
            print(f"\n[orchestrator] Workstream '{result['name']}' finished with exit code {result['returncode']}.")
            if result["stdout"]:
                print(result["stdout"])
            if result["stderr"]:
                print(result["stderr"], file=sys.stderr)
    else:
        with ProcessPoolExecutor(max_workers=args.max_workers) as executor:
            futures = {
                executor.submit(
                    run_workstream,
                    ws_path,
                    args.max_papers,
                    args.max_batch_workers,
                    args.relevance_threshold,
                    args.model,
                    args.dry_run,
                    args.skip_discovery,
                ): ws_path
                for ws_path in workstream_paths
            }
            for future in as_completed(futures):
                ws_path = futures[future]
                try:
                    result = future.result()
                except Exception as exc:
                    result = {
                        "name": ws_path.stem,
                        "config": str(ws_path),
                        "returncode": 1,
                        "stdout": "",
                        "stderr": f"Orchestrator exception: {exc}",
                    }
                results.append(result)
                print(f"\n[orchestrator] Workstream '{result['name']}' finished with exit code {result['returncode']}.")
                if result["stdout"]:
                    print(result["stdout"])
                if result["stderr"]:
                    print(result["stderr"], file=sys.stderr)

    # Aggregate summary.
    summary = {
        "run_at": datetime.now().isoformat(),
        "dry_run": args.dry_run,
        "workstreams": results,
    }
    summary_dir = config.STAGING_DIR / "workstreams"
    summary_dir.mkdir(parents=True, exist_ok=True)
    summary_path = summary_dir / "_orchestrator_summary.json"
    summary_path.write_text(json.dumps(summary, indent=2, ensure_ascii=False), encoding="utf-8")

    print(f"\n[orchestrator] Summary written to: {summary_path}")
    failed = [r for r in results if r["returncode"] != 0]
    if failed:
        print(f"[orchestrator] {len(failed)} workstream(s) failed.", file=sys.stderr)
        return 1

    print("[orchestrator] All workstreams completed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
