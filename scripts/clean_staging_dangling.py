#!/usr/bin/env python3
"""Remove dangling edges from a staged workstream before promotion.

Usage:
    source .venv/bin/activate
    python scripts/clean_staging_dangling.py <workstream_name>

The script loads all production entity IDs and the IDs of entries staged by the
workstream, then:
  1. Drops embedded `related_entities` whose target ID is not known.
  2. Deletes standalone relationship files whose source or target is not known.

Known IDs = production IDs + staged IDs, so cross-references between two
entries in the same staged batch are preserved.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

import yaml

from ai4sci_lib import config


def load_frontmatter(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---"):
        return {}
    _, rest = text.split("---", 1)
    yaml_text, _ = rest.split("---", 1)
    return yaml.safe_load(yaml_text) or {}


def save_frontmatter(path: Path, frontmatter: dict) -> None:
    text = path.read_text(encoding="utf-8")
    _, rest = text.split("---", 1)
    _, body = rest.split("---", 1)
    new_yaml = yaml.dump(frontmatter, sort_keys=False, allow_unicode=True, default_flow_style=False)
    path.write_text(f"---\n{new_yaml}---\n{body}", encoding="utf-8")


def collect_production_ids() -> set[str]:
    ids: set[str] = set()
    for p in config.RESEARCH_DIR.rglob("*.md"):
        try:
            data = load_frontmatter(p)
            if data.get("$id"):
                ids.add(data["$id"])
        except Exception:
            continue
    return ids


def main() -> int:
    parser = argparse.ArgumentParser(description="Clean dangling edges in a staged workstream.")
    parser.add_argument("workstream", help="Workstream name (staging subdirectory name).")
    args = parser.parse_args()

    staging_dir = config.STAGING_DIR / "workstreams" / args.workstream
    research_dir = staging_dir / "research"
    rel_dir = staging_dir / "data" / "relationships"

    if not staging_dir.exists():
        print(f"[clean] Staging directory not found: {staging_dir}")
        return 1

    production_ids = collect_production_ids()

    staged_entries = sorted(research_dir.rglob("*.md")) if research_dir.exists() else []
    staged_ids: set[str] = set()
    for p in staged_entries:
        try:
            data = load_frontmatter(p)
            if data.get("$id"):
                staged_ids.add(data["$id"])
        except Exception:
            continue

    known_ids = production_ids | staged_ids
    print(f"[clean] Production IDs: {len(production_ids)}, staged IDs: {len(staged_ids)}")

    dropped_embedded = 0
    for p in staged_entries:
        data = load_frontmatter(p)
        related = data.get("related_entities", [])
        if not related:
            continue
        kept = []
        for rel in related:
            tid = rel.get("id")
            if tid in known_ids:
                kept.append(rel)
            else:
                print(f"[clean] Drop embedded rel in {p.name}: {tid} ({rel.get('relationship')})")
                dropped_embedded += 1
        if kept:
            data["related_entities"] = kept
        else:
            data.pop("related_entities", None)
        save_frontmatter(p, data)

    deleted_files = 0
    rel_files = sorted(rel_dir.glob("*.md")) if rel_dir.exists() else []
    for p in rel_files:
        data = load_frontmatter(p)
        src = data.get("source", {})
        tgt = data.get("target", {})
        src_id = src.get("id") if isinstance(src, dict) else src
        tgt_id = tgt.get("id") if isinstance(tgt, dict) else tgt
        if src_id in known_ids and tgt_id in known_ids:
            continue
        print(f"[clean] Delete dangling relationship file: {p.name} (src={src_id}, tgt={tgt_id})")
        p.unlink()
        deleted_files += 1

    print(
        f"[clean] Done. Dropped {dropped_embedded} embedded relations, "
        f"deleted {deleted_files} relationship files."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
