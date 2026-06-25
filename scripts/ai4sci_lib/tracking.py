"""Progress tracking for AI4Sci workstreams.

Maintains a JSON progress log per workstream so the orchestrator and reviewer
can see how many candidates were discovered, processed, approved, and rejected.
"""

from __future__ import annotations

import json
from datetime import datetime
from pathlib import Path
from typing import Any

from . import pipeline


def _default_summary() -> dict[str, Any]:
    return {
        "total": 0,
        "success": 0,
        "skipped": 0,
        "duplicate": 0,
        "error": 0,
        "pending_review": 0,
        "approved": 0,
        "rejected": 0,
        "last_run_at": None,
    }


def _summarize_results(results: list[pipeline.PipelineResult]) -> dict[str, Any]:
    summary = _default_summary()
    summary["total"] = len(results)
    for result in results:
        key = result.status if result.status in summary else "error"
        summary[key] += 1
        if result.status == "success":
            summary["pending_review"] += 1
    return summary


def update_workstream_progress(
    name: str,
    output_dir: Path,
    results: list[pipeline.PipelineResult],
    extra: dict[str, Any] | None = None,
) -> dict[str, Any]:
    """Update and return the progress summary for a workstream.

    Args:
        name: Workstream name.
        output_dir: Workstream staging directory.
        results: List of PipelineResult objects from the latest run.
        extra: Optional extra fields to merge into the summary.

    Returns:
        Updated summary dict.
    """
    log_path = output_dir / "logs" / "progress.json"
    log_path.parent.mkdir(parents=True, exist_ok=True)

    existing: dict[str, Any] = {}
    if log_path.exists():
        try:
            existing = json.loads(log_path.read_text(encoding="utf-8"))
        except Exception:
            existing = {}

    summary = _summarize_results(results)
    summary["name"] = name
    summary["output_dir"] = str(output_dir)
    summary["last_run_at"] = datetime.now().isoformat()
    summary["run_count"] = existing.get("run_count", 0) + 1

    if extra:
        summary.update(extra)

    log_path.write_text(json.dumps(summary, indent=2, ensure_ascii=False), encoding="utf-8")
    return summary


def load_workstream_progress(output_dir: Path) -> dict[str, Any]:
    """Load the progress log for a workstream."""
    log_path = output_dir / "logs" / "progress.json"
    if log_path.exists():
        return json.loads(log_path.read_text(encoding="utf-8"))
    return _default_summary()


def load_all_progress(staging_dir: Path) -> dict[str, dict[str, Any]]:
    """Load progress logs for all workstreams under staging_dir/workstreams."""
    progress: dict[str, dict[str, Any]] = {}
    workstreams_dir = staging_dir / "workstreams"
    if not workstreams_dir.exists():
        return progress
    for ws_dir in workstreams_dir.iterdir():
        if ws_dir.is_dir():
            progress[ws_dir.name] = load_workstream_progress(ws_dir)
    return progress
