#!/usr/bin/env python3
"""Print knowledge-graph coverage metrics.

Usage:
    python scripts/report_coverage.py
"""

from __future__ import annotations

import json
import re
from collections import Counter
from pathlib import Path

import yaml


def load_entries(research_dir: Path) -> list[dict]:
    entries = []
    for p in research_dir.rglob("*.md"):
        try:
            text = p.read_text(encoding="utf-8")
            if not text.startswith("---"):
                continue
            _, rest = text.split("---", 1)
            yaml_text, _ = rest.split("---", 1)
            data = yaml.safe_load(yaml_text) or {}
            entries.append(data)
        except Exception:
            continue
    return entries


def count_workstreams(workstreams_dir: Path) -> int:
    return len(list(workstreams_dir.rglob("*.yaml")))


def count_workstream_tree_leaves(tree_path: Path) -> int:
    """Count unchecked leaf YAML paths in WORKSTREAM_TREE.md."""
    if not tree_path.exists():
        return 0
    text = tree_path.read_text(encoding="utf-8")
    # Lines like `- [ ] path/to/file.yaml` or `- [x] path/to/file.yaml`
    leaves = re.findall(r"- \[[ x]\] `([^`]+\.yaml)`", text)
    return len(leaves)


def main() -> int:
    root = Path(__file__).parent.parent
    research_dir = root / "research"
    relationships_dir = root / "data" / "relationships"
    workstreams_dir = root / "scripts" / "ai4sci_workstreams"
    tree_path = root / "docs" / "ai4sci" / "WORKSTREAM_TREE.md"

    entries = load_entries(research_dir)
    rel_count = len(list(relationships_dir.glob("*.md")))
    ws_count = count_workstreams(workstreams_dir)
    tree_leaves = count_workstream_tree_leaves(tree_path)

    print("=== Coverage Report ===")
    print(f"Production entries: {len(entries)}")
    print(f"Relationships:      {rel_count}")
    print(f"Relationships/entry: {rel_count / len(entries):.2f}" if entries else "N/A")
    print(f"Workstreams:        {ws_count} / {tree_leaves} tree leaves ({ws_count / tree_leaves * 100:.1f}% coverage)" if tree_leaves else f"Workstreams: {ws_count}")

    print("\nEntries by domain:")
    domain_counts = Counter()
    for e in entries:
        for d in e.get("domains", []):
            domain_counts[d] += 1
    for domain, count in domain_counts.most_common():
        print(f"  {domain}: {count}")

    print("\nEntries by type:")
    type_counts = Counter(e.get("type", "unknown") for e in entries)
    for t, count in type_counts.most_common():
        print(f"  {t}: {count}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
