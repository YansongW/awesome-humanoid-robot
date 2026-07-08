#!/usr/bin/env python3
"""
Coverage dashboard and human review queue generator.

Outputs:
    docs/coverage_dashboard.md       — high-level coverage metrics.
    .staging/review/human_review_queue.md — prioritized list of items needing review.

Usage:
    source .venv/bin/activate
    python scripts/coverage_dashboard.py
"""

from __future__ import annotations

import json
import sys
from collections import Counter
from datetime import datetime
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).parent))
from ai4sci_lib import config


ROOT = Path(__file__).parent.parent
DOCS_DIR = ROOT / "docs"
DASHBOARD_PATH = DOCS_DIR / "coverage_dashboard.md"
QUEUE_PATH = config.STAGING_DIR / "review" / "human_review_queue.md"


def load_yaml_frontmatter(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---"):
        raise ValueError(f"No frontmatter in {path}")
    _, rest = text.split("---", 1)
    yaml_text, _ = rest.split("---", 1)
    return yaml.safe_load(yaml_text)


def depth_for(entity: dict) -> str:
    depths = entity.get("theoretical_depth", [])
    for d in config.THEORETICAL_DEPTH_ORDER:
        if d in depths:
            return d
    type_to_depth = {
        "paper": "system",
        "robot_system": "system",
        "component": "system",
        "material": "system",
        "technology": "method",
        "method": "method",
        "algorithm": "method",
        "formalism": "formalism",
        "equation": "formalism",
        "operator": "formalism",
        "variable": "formalism",
        "constant": "formalism",
        "principle": "principle",
        "theorem": "principle",
        "foundation": "foundation",
    }
    return type_to_depth.get(entity.get("type", "paper"), "system")


def gather_entities() -> list[tuple[Path, dict]]:
    items = []
    for path in config.RESEARCH_DIR.rglob("*.md"):
        try:
            data = load_yaml_frontmatter(path)
        except Exception:
            continue
        items.append((path, data))
    return items


def gather_relationships() -> list[tuple[Path, dict]]:
    items = []
    dirs = [config.RELATIONSHIPS_DIR]
    if config.STAGING_RELATIONSHIPS_DIR.exists():
        dirs.append(config.STAGING_RELATIONSHIPS_DIR)
    for directory in dirs:
        if not directory.exists():
            continue
        for path in directory.rglob("*.md"):
            try:
                data = load_yaml_frontmatter(path)
            except Exception:
                continue
            items.append((path, data))
    return items


def gather_staging() -> list[tuple[Path, dict, str]]:
    """Return staged items with kind (entry|relationship|review|rejected)."""
    items = []
    for path in config.STAGING_RESEARCH_DIR.rglob("*.md"):
        try:
            data = load_yaml_frontmatter(path)
        except Exception:
            continue
        items.append((path, data, "entry"))
    for path in config.STAGING_RELATIONSHIPS_DIR.glob("*.md"):
        try:
            data = load_yaml_frontmatter(path)
        except Exception:
            continue
        items.append((path, data, "relationship"))
    for path in config.STAGING_REVIEW_DIR.rglob("*.md"):
        items.append((path, {}, "review"))
    for path in config.STAGING_REJECTED_DIR.rglob("*.md"):
        items.append((path, {}, "rejected"))
    return items


def compute_metrics(entities: list[tuple[Path, dict]], relationships: list[tuple[Path, dict]]) -> dict:
    type_counter = Counter()
    depth_counter = Counter()
    domain_counter = Counter()
    missing_depth = []
    for path, data in entities:
        etype = data.get("type", "unknown")
        type_counter[etype] += 1
        depth_counter[depth_for(data)] += 1
        for domain in data.get("domains", []):
            domain_counter[domain] += 1
        if not data.get("theoretical_depth"):
            missing_depth.append((path, data.get("$id")))

    # Outgoing cross-layer relationships per source entity.
    outgoing_cross: dict[str, int] = {}
    dangling = []
    entity_ids = {data.get("$id") for _, data in entities if data.get("$id")}
    for path, data in relationships:
        src = data.get("source", {}).get("id")
        tgt = data.get("target", {}).get("id")
        if not src or not tgt:
            continue
        if src not in entity_ids or tgt not in entity_ids:
            dangling.append((path.name, src, tgt))
            continue
        # Depth is inferred by scanning entities; we don't store lookup here, so skip.

    # Build lookup for depth checks.
    lookup = {data.get("$id"): data for _, data in entities if data.get("$id")}
    for path, data in relationships:
        src = data.get("source", {}).get("id")
        tgt = data.get("target", {}).get("id")
        if src in lookup and tgt in lookup:
            if depth_for(lookup[src]) != depth_for(lookup[tgt]):
                outgoing_cross[src] = outgoing_cross.get(src, 0) + 1

    system_without_cross = [
        (data.get("$id"), data.get("names", {}).get("en", ""))
        for _, data in entities
        if depth_for(data) == "system" and outgoing_cross.get(data.get("$id"), 0) == 0
    ]

    return {
        "total_entities": len(entities),
        "total_relationships": len(relationships),
        "by_type": dict(type_counter),
        "by_depth": dict(depth_counter),
        "by_domain": dict(domain_counter),
        "missing_depth_count": len(missing_depth),
        "missing_depth": missing_depth[:20],
        "dangling_count": len(dangling),
        "dangling": dangling[:20],
        "system_without_cross_count": len(system_without_cross),
        "system_without_cross": system_without_cross[:30],
        "cross_layer_relationship_count": sum(outgoing_cross.values()),
    }


def render_dashboard(metrics: dict, staging_counts: dict) -> str:
    lines = [
        "# Knowledge Graph Coverage Dashboard",
        "",
        f"_Generated at {datetime.utcnow().isoformat()}Z_",
        "",
        "## Summary",
        "",
        f"- **Total entities**: {metrics['total_entities']}",
        f"- **Total relationships**: {metrics['total_relationships']}",
        f"- **Cross-layer relationships**: {metrics['cross_layer_relationship_count']}",
        f"- **Entities missing `theoretical_depth`**: {metrics['missing_depth_count']}",
        f"- **Dangling relationships**: {metrics['dangling_count']}",
        f"- **System-level entities without cross-layer links**: {metrics['system_without_cross_count']}",
        "",
        "## Staging Queue",
        "",
        f"- Staged entries: {staging_counts.get('entry', 0)}",
        f"- Staged relationships: {staging_counts.get('relationship', 0)}",
        f"- Review notes: {staging_counts.get('review', 0)}",
        f"- Rejected items: {staging_counts.get('rejected', 0)}",
        "",
        "## Entities by Type",
        "",
        "| Type | Count |",
        "|------|-------|",
    ]
    for t, c in sorted(metrics["by_type"].items(), key=lambda x: -x[1]):
        lines.append(f"| {t} | {c} |")

    lines.extend([
        "",
        "## Entities by Theoretical Depth",
        "",
        "| Depth | Count |",
        "|-------|-------|",
    ])
    order = ["foundation", "principle", "formalism", "method", "system"]
    for depth in order:
        lines.append(f"| {depth} | {metrics['by_depth'].get(depth, 0)} |")

    lines.extend([
        "",
        "## Top Domains",
        "",
        "| Domain | Count |",
        "|--------|-------|",
    ])
    for domain, count in sorted(metrics["by_domain"].items(), key=lambda x: -x[1])[:12]:
        lines.append(f"| {domain} | {count} |")

    if metrics["dangling"]:
        lines.extend([
            "",
            "## Sample Dangling Relationships",
            "",
        ])
        for rel_name, src, tgt in metrics["dangling"]:
            lines.append(f"- `{rel_name}`: `{src}` → `{tgt}`")

    if metrics["system_without_cross"]:
        lines.extend([
            "",
            "## System-Level Entities Without Cross-Layer Links (Top 30)",
            "",
            "These are high-priority candidates for the cross-layer backfill script.",
            "",
        ])
        for eid, name in metrics["system_without_cross"]:
            display = f"{name} (`{eid}`)" if name else f"`{eid}`"
            lines.append(f"- {display}")

    lines.append("")
    return "\n".join(lines)


def render_queue(staging: list[tuple[Path, dict, str]]) -> str:
    lines = [
        "# Human Review Queue",
        "",
        f"_Generated at {datetime.utcnow().isoformat()}Z_",
        "",
        "## Prioritized Items",
        "",
        "| Kind | ID / File | Status | Confidence | Path |",
        "|------|-----------|--------|------------|------|",
    ]

    def sort_key(item):
        path, data, kind = item
        verification = data.get("verification", {}) if isinstance(data, dict) else {}
        status = verification.get("status", "unverified")
        confidence = verification.get("confidence", "low")
        priority = {"speculative": 0, "unverified": 1, "partially_verified": 2, "verified": 3}
        conf_rank = {"low": 0, "medium": 1, "high": 2}
        return (priority.get(status, 0), conf_rank.get(confidence, 0), str(path))

    for path, data, kind in sorted(staging, key=sort_key, reverse=True):
        if kind == "review":
            lines.append(f"| review note | {path.name} | - | - | {path} |")
            continue
        if kind == "rejected":
            lines.append(f"| rejected | {path.name} | - | - | {path} |")
            continue
        eid = data.get("$id", path.stem)
        name = data.get("names", {}).get("en", "") if isinstance(data.get("names"), dict) else ""
        display = f"{name} (`{eid}`)" if name else f"`{eid}`"
        verification = data.get("verification", {}) or {}
        status = verification.get("status", "unverified")
        confidence = verification.get("confidence", "low")
        lines.append(f"| {kind} | {display} | {status} | {confidence} | {path} |")

    lines.append("")
    return "\n".join(lines)


def main() -> int:
    DOCS_DIR.mkdir(parents=True, exist_ok=True)
    config.STAGING_REVIEW_DIR.mkdir(parents=True, exist_ok=True)

    entities = gather_entities()
    relationships = gather_relationships()
    staging = gather_staging()
    metrics = compute_metrics(entities, relationships)

    staging_counts = Counter(kind for _, _, kind in staging)

    dashboard = render_dashboard(metrics, staging_counts)
    DASHBOARD_PATH.write_text(dashboard, encoding="utf-8")
    print(f"[info] Wrote coverage dashboard to {DASHBOARD_PATH}")

    queue = render_queue(staging)
    QUEUE_PATH.write_text(queue, encoding="utf-8")
    print(f"[info] Wrote human review queue to {QUEUE_PATH}")

    # Also emit a compact JSON summary for programmatic consumers.
    summary = {
        "generated_at": datetime.utcnow().isoformat() + "Z",
        "entities": metrics["total_entities"],
        "relationships": metrics["total_relationships"],
        "cross_layer_relationships": metrics["cross_layer_relationship_count"],
        "missing_depth": metrics["missing_depth_count"],
        "dangling": metrics["dangling_count"],
        "system_without_cross_layer": metrics["system_without_cross_count"],
        "staging": dict(staging_counts),
    }
    summary_path = config.STAGING_DIR / "review" / "dashboard_summary.json"
    summary_path.write_text(json.dumps(summary, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"[info] Wrote JSON summary to {summary_path}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
