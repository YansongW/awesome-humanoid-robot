#!/usr/bin/env python3
"""AI4Sci batch pipeline for a single workstream.

Discovers papers for a workstream, classifies relevance, and runs the full
AI4Sci extraction pipeline in parallel. Outputs are written to a per-workstream
staging directory (e.g., `.staging/workstreams/vla/`).

Usage:
    source .venv/bin/activate
    python scripts/ai4sci_batch_pipeline.py scripts/ai4sci_workstreams/vla.yaml
    python scripts/ai4sci_batch_pipeline.py scripts/ai4sci_workstreams/vla.yaml --dry-run
    python scripts/ai4sci_batch_pipeline.py scripts/ai4sci_workstreams/vla.yaml --max-workers 2 --max-papers 5
"""

from __future__ import annotations

import argparse
import json
import sys
from concurrent.futures import ProcessPoolExecutor, as_completed
from datetime import datetime
from pathlib import Path

import yaml

from ai4sci_lib import config, discovery, pipeline, tracking


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Run the AI4Sci batch pipeline for a workstream."
    )
    parser.add_argument(
        "config",
        type=Path,
        help="Path to a workstream YAML config file.",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=None,
        help="Override the staging output directory for this workstream.",
    )
    parser.add_argument(
        "--max-papers",
        type=int,
        default=None,
        help="Override the max number of papers to process from the config.",
    )
    parser.add_argument(
        "--max-workers",
        type=int,
        default=2,
        help="Maximum parallel workers for processing papers (default: 2).",
    )
    parser.add_argument(
        "--relevance-threshold",
        choices=["low", "medium", "high"],
        default=None,
        help="Override relevance threshold from config.",
    )
    parser.add_argument(
        "--model",
        default=None,
        help="LLM model name override.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Discover and classify but do not write staged files.",
    )
    parser.add_argument(
        "--skip-discovery",
        action="store_true",
        help="Skip discovery; only process explicit paper_ids from config.",
    )
    return parser.parse_args()


def load_workstream_config(path: Path) -> dict:
    with open(path, encoding="utf-8") as f:
        return yaml.safe_load(f)


def process_one(
    source: pipeline.SourceCandidate,
    output_dir: Path,
    relevance_threshold: str,
    model: str | None,
    dry_run: bool,
    relevance_context: str | None,
) -> pipeline.PipelineResult:
    """Wrapper to process one source; suitable for process pool execution."""
    return pipeline.process_source(
        source,
        output_dir=output_dir,
        relevance_threshold=relevance_threshold,
        model=model,
        dry_run=dry_run,
        relevance_context=relevance_context,
    )


def main() -> int:
    args = parse_args()
    workstream = load_workstream_config(args.config)
    name = workstream["name"]

    output_dir = args.output_dir or (config.STAGING_DIR / "workstreams" / name)
    output_dir.mkdir(parents=True, exist_ok=True)

    max_papers = args.max_papers if args.max_papers is not None else workstream.get("max_papers", 10)
    relevance_threshold = args.relevance_threshold or workstream.get("relevance_threshold", "medium")
    seed_queries = workstream.get("seed_queries", [])
    paper_ids = workstream.get("paper_ids", [])
    sources = workstream.get("sources", ["arxiv"])
    relevance_context = workstream.get("relevance_context")

    # Pagination/discovery limits from workstream config. Decouple "how many to
    # pull" from "how many to process" so workstreams can surface dense pools.
    max_results_per_query = workstream.get("max_results_per_query", 50)
    max_total = workstream.get("max_total", max(max_results_per_query, max_papers * 3))

    print(f"[batch] Workstream: {name}")
    print(f"[batch] Output dir: {output_dir}")
    print(f"[batch] Max papers to process: {max_papers}")
    print(f"[batch] Max candidates to discover: {max_total}")
    print(f"[batch] Relevance threshold: {relevance_threshold}")
    if relevance_context:
        print(f"[batch] Relevance context: {relevance_context[:120]}{'...' if len(relevance_context) > 120 else ''}")

    # Per-workstream tried log for backwards compatibility.
    logs_dir = output_dir / "logs"
    logs_dir.mkdir(parents=True, exist_ok=True)
    tried_path = logs_dir / "tried.json"
    local_tried: set[str] = set()
    if tried_path.exists():
        try:
            local_tried = set(json.loads(tried_path.read_text(encoding="utf-8")))
        except Exception:
            local_tried = set()

    # Discovery.
    if args.skip_discovery:
        print("[batch] Skipping discovery; using explicit paper_ids only.")
        candidates = []
    else:
        print("[batch] Discovering candidates...")
        candidates = discovery.discover_candidates(
            seed_queries=seed_queries,
            paper_ids=paper_ids,
            max_results_per_query=max_results_per_query,
            max_total=max_total,
            sources=sources,
            polite_delay=workstream.get("polite_delay", 0.5),
        )
        print(f"[batch] Discovered {len(candidates)} candidate(s).")

    # Add explicit paper IDs that were not already included.
    seen = {c.arxiv_id or c.source_url for c in candidates}
    for pid in paper_ids:
        candidate = discovery.resolve_candidate(pid)
        if candidate and (candidate.arxiv_id or candidate.source_url) not in seen:
            candidates.append(candidate)
            seen.add(candidate.arxiv_id or candidate.source_url)

    # Skip candidates already attempted in previous runs (global + local).
    fresh_candidates = [
        c for c in candidates
        if (c.arxiv_id or c.source_url) not in local_tried
    ]
    skipped_already_tried = len(candidates) - len(fresh_candidates)
    if skipped_already_tried:
        print(f"[batch] Skipping {skipped_already_tried} already-tried candidate(s).")

    if not fresh_candidates:
        print("[batch] No new candidates to process.")
        return 0

    if args.dry_run:
        print("[batch] Dry run: discovered candidates but skipping LLM extraction.")
        return 0

    candidates_to_process = fresh_candidates[:max_papers]
    print(f"[batch] Processing {len(candidates_to_process)} candidate(s) with up to {args.max_workers} worker(s)...")

    results: list[pipeline.PipelineResult] = []
    if args.max_workers <= 1:
        for source in candidates_to_process:
            result = process_one(
                source,
                output_dir,
                relevance_threshold,
                args.model,
                args.dry_run,
                relevance_context,
            )
            results.append(result)
            print(f"  {result.status:12s} {source.input} — {result.message}")
    else:
        with ProcessPoolExecutor(max_workers=args.max_workers) as executor:
            futures = {
                executor.submit(
                    process_one,
                    source,
                    output_dir,
                    relevance_threshold,
                    args.model,
                    args.dry_run,
                    relevance_context,
                ): source
                for source in candidates_to_process
            }
            for future in as_completed(futures):
                source = futures[future]
                try:
                    result = future.result()
                except Exception as exc:
                    result = pipeline.PipelineResult(
                        status="error",
                        message=f"Worker exception: {exc}",
                    )
                results.append(result)
                print(f"  {result.status:12s} {source.input} — {result.message}")

    # Persist tried candidate IDs locally and in the project-wide log.
    if not args.dry_run:
        for source in candidates_to_process:
            local_tried.add(source.arxiv_id or source.source_url)
            discovery.record_tried_candidate(source)
        tried_path.write_text(json.dumps(sorted(local_tried), indent=2, ensure_ascii=False), encoding="utf-8")

    # Tracking and summary.
    summary = tracking.update_workstream_progress(name, output_dir, results)
    summary_path = logs_dir / "summary.json"
    summary_path.parent.mkdir(parents=True, exist_ok=True)
    summary_path.write_text(json.dumps(summary, indent=2, ensure_ascii=False), encoding="utf-8")

    print("\n[batch] Summary:")
    print(f"  Total:    {summary['total']}")
    print(f"  Success:  {summary['success']}")
    print(f"  Skipped:  {summary['skipped']}")
    print(f"  Duplicate:{summary['duplicate']}")
    print(f"  Error:    {summary['error']}")
    print(f"  Written to: {summary_path}")

    if args.dry_run:
        print("\n[batch] Dry run complete. No files were written.")
    else:
        print(f"\n[batch] Done. Review with: python scripts/ai4sci_review.py --workstream {name}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
