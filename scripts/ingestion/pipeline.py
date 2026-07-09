"""Ingestion pipeline CLI.

Usage:
    PYTHONPATH=scripts python -m ingestion.pipeline --source arxiv_ro_rss
    PYTHONPATH=scripts python -m ingestion.pipeline --all --dry-run
"""

from __future__ import annotations

import argparse
import json
import sys
import traceback
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from .adapters import (
    ActuatorSuppliersAdapter,
    ArxivRssAdapter,
    AwesomeHumanoidAdapter,
    AwesomeVLAAdapter,
    IeeeSpectrumRoboticsAdapter,
    IsoRoboticsAdapter,
    NvidiaRssAdapter,
    ProgressJsonAdapter,
    RoboticsTomorrowAdapter,
    UnitreeNewsAdapter,
    WechatArticleAdapter,
)
from ai4sci_lib import entry_builder

from .core import IngestionResult, ParsedItem, Source
from .dedup import DedupService
from .registry import Registry
from .writer import EntryWriter


ADAPTER_MAP: dict[str, type] = {
    "awesome_vla_models": AwesomeVLAAdapter,
    "awesome_humanoid_robot_learning": AwesomeHumanoidAdapter,
    "humanoid_paper_notebooks_progress": ProgressJsonAdapter,
    "arxiv_ro_rss": ArxivRssAdapter,
    "unitree_news": UnitreeNewsAdapter,
    "nvidia_robotics_blog": NvidiaRssAdapter,
    "wechat_articles": WechatArticleAdapter,
    "humanoid_actuators_suppliers": ActuatorSuppliersAdapter,
    "humanoid_workflow_entities": ActuatorSuppliersAdapter,
    "humanoid_manufacturing_systems": ActuatorSuppliersAdapter,
    # industry / business / standards
    "robotics_tomorrow_rss": RoboticsTomorrowAdapter,
    "ieee_spectrum_robotics_rss": IeeeSpectrumRoboticsAdapter,
    "iso_robotics_news": IsoRoboticsAdapter,
    # backward-compatible ids
    "wechat_161_humanoid_papers": WechatArticleAdapter,
    "wechat_42_humanoid_rl": WechatArticleAdapter,
}


class Pipeline:
    """Run ingestion sources and write new entries."""

    def __init__(
        self,
        registry: Registry | None = None,
        writer: EntryWriter | None = None,
        dedup: DedupService | None = None,
    ) -> None:
        self.registry = registry or Registry()
        self.dedup = dedup or DedupService()
        # Load existing IDs once per pipeline run and share with writer.
        self.writer = writer or EntryWriter(existing_ids=entry_builder.load_existing_ids())

    def run_source(self, source: Source, dry_run: bool = False) -> list[IngestionResult]:
        """Fetch, deduplicate, and optionally write items for a single source."""
        results: list[IngestionResult] = []
        adapter_cls = ADAPTER_MAP.get(source.id)
        if adapter_cls is None:
            msg = f"No adapter registered for source {source.id}"
            return [IngestionResult(source_id=source.id, status="error", item_title="", message=msg)]

        adapter = adapter_cls()
        if not hasattr(adapter, "fetch"):
            msg = f"Adapter for {source.id} has no fetch method"
            return [IngestionResult(source_id=source.id, status="error", item_title="", message=msg)]

        try:
            items = adapter.fetch(source)
        except Exception as exc:  # noqa: BLE001
            tb = traceback.format_exc()
            return [IngestionResult(
                source_id=source.id,
                status="error",
                item_title=f"fetch_failed:{source.id}",
                message=f"Fetch failed: {exc}\n{tb}",
            )]

        added = 0
        duplicates = 0
        skipped = 0
        for item in items:
            if not isinstance(item, ParsedItem):
                skipped += 1
                results.append(IngestionResult(
                    source_id=source.id,
                    status="skipped",
                    item_title=str(item),
                    message="Adapter returned non-ParsedItem",
                ))
                continue

            is_dup, reason = self.dedup.check(item.title, item.arxiv_id, item.source_url)
            if is_dup:
                duplicates += 1
                results.append(IngestionResult(
                    source_id=source.id,
                    status="duplicate",
                    item_title=item.title,
                    message=reason,
                ))
                continue

            if dry_run:
                added += 1
                self.dedup.add(item.title, item.arxiv_id, item.source_url)
                results.append(IngestionResult(
                    source_id=source.id,
                    status="added",
                    item_title=item.title,
                    message="dry-run; would write",
                ))
                continue

            try:
                path = self.writer.write(item)
                added += 1
                self.dedup.add(item.title, item.arxiv_id, item.source_url)
                results.append(IngestionResult(
                    source_id=source.id,
                    status="added",
                    item_title=item.title,
                    entry_id=self._entry_id_from_path(path),
                ))
            except Exception as exc:  # noqa: BLE001
                results.append(IngestionResult(
                    source_id=source.id,
                    status="error",
                    item_title=item.title,
                    message=str(exc),
                ))

        status = "healthy" if added or duplicates or not items else "error"
        if not items and not any(r.status == "error" for r in results):
            status = "no_items"
        if any(r.status == "error" for r in results):
            status = "error"

        if not dry_run:
            self.registry.update_stats(source.id, added=added, duplicates=duplicates, status=status)

        return results

    def run_all(self, enabled_only: bool = True, dry_run: bool = False) -> dict[str, list[IngestionResult]]:
        """Run all configured sources."""
        sources = self.registry.list_sources(enabled_only=enabled_only)
        by_source: dict[str, list[IngestionResult]] = {}
        for source in sources:
            by_source[source.id] = self.run_source(source, dry_run=dry_run)
        return by_source

    @staticmethod
    def _entry_id_from_path(path: Path) -> str:
        return path.stem


def _parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run the unified ingestion pipeline.")
    parser.add_argument("--source", action="append", help="Run one or more sources by id (can be given multiple times)")
    parser.add_argument("--all", action="store_true", help="Run all enabled sources")
    parser.add_argument("--all-sources", action="store_true", help="Run all sources regardless of enabled flag")
    parser.add_argument("--dry-run", action="store_true", help="Do not write files, only report counts")
    parser.add_argument("--json", action="store_true", help="Emit machine-readable JSON output")
    parser.add_argument("--summary", action="store_true", help="Print per-source summary even in JSON mode")
    return parser.parse_args(argv)


def _summarize(results: list[IngestionResult]) -> dict[str, int]:
    counts: dict[str, int] = {}
    for r in results:
        counts[r.status] = counts.get(r.status, 0) + 1
    return counts


def main(argv: list[str] | None = None) -> int:
    args = _parse_args(argv)
    pipeline = Pipeline()

    if args.source:
        by_source: dict[str, list[IngestionResult]] = {}
        for source_id in args.source:
            source = pipeline.registry.get(source_id)
            if source is None:
                print(f"Unknown source: {source_id}", file=sys.stderr)
                return 1
            by_source[source.id] = pipeline.run_source(source, dry_run=args.dry_run)
    elif args.all or args.all_sources:
        by_source = pipeline.run_all(enabled_only=not args.all_sources, dry_run=args.dry_run)
    else:
        print("Use --source <id> or --all", file=sys.stderr)
        return 1

    if args.json:
        payload: dict[str, Any] = {}
        for sid, results in by_source.items():
            payload[sid] = {
                "summary": _summarize(results),
                "items": [
                    {
                        "status": r.status,
                        "title": r.item_title,
                        "entry_id": r.entry_id,
                        "message": r.message,
                    }
                    for r in results
                ],
            }
        print(json.dumps(payload, ensure_ascii=False, indent=2))
    else:
        for sid, results in by_source.items():
            counts = _summarize(results)
            print(f"[{sid}] {counts}")
            if args.summary:
                for r in results:
                    print(f"  {r.status}: {r.item_title[:80]}{'...' if len(r.item_title) > 80 else ''}")

    # Non-zero exit if any errors occurred.
    for results in by_source.values():
        if any(r.status == "error" for r in results):
            return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
