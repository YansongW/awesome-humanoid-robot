#!/usr/bin/env python3
"""Promote staged entries and relationships from workstream staging to production.

Only schema-valid files whose relationship endpoints exist (in production or in
staging) are promoted. Dangling relationships and schema-invalid files are skipped.

Usage:
    python scripts/auto_promote_staging.py --dry-run
    python scripts/auto_promote_staging.py
"""

from __future__ import annotations

import argparse
import json
import shutil
import sys
from pathlib import Path
from typing import Any

import yaml

try:
    from jsonschema import Draft202012Validator, ValidationError
except ImportError as e:
    print(f"Missing dependency: {e}")
    sys.exit(1)

from ai4sci_lib import config, entry_builder


STAGING_DIR = config.STAGING_DIR
RESEARCH_DIR = config.RESEARCH_DIR
RELATIONSHIPS_DIR = config.RELATIONSHIPS_DIR
SCHEMA_DIR = config.SCHEMA_DIR


def load_frontmatter(path: Path) -> tuple[dict[str, Any] | None, str]:
    """Load YAML frontmatter from a Markdown file. Returns (None, '') on parse failure."""
    try:
        text = path.read_text(encoding="utf-8")
        if not text.startswith("---"):
            return None, ""
        _, rest = text.split("---", 1)
        yaml_text, body = rest.split("---", 1)
        return yaml.safe_load(yaml_text), body
    except Exception:
        return None, ""


def dump_frontmatter(frontmatter: dict[str, Any], body: str) -> str:
    yaml_text = yaml.dump(frontmatter, sort_keys=False, allow_unicode=True, default_flow_style=False)
    return f"---\n{yaml_text}---\n\n{body.strip()}\n"


def compile_validators() -> tuple[Draft202012Validator, Draft202012Validator]:
    entry_schema = json.loads((SCHEMA_DIR / "entry_schema.json").read_text())
    relationship_schema = json.loads((SCHEMA_DIR / "relationship_schema.json").read_text())
    return Draft202012Validator(entry_schema), Draft202012Validator(relationship_schema)


def validate_frontmatter(frontmatter: dict[str, Any], validator: Draft202012Validator) -> list[str]:
    errors: list[str] = []
    try:
        validator.validate(frontmatter)
    except ValidationError as e:
        errors.append(f"{e.message} at {'/'.join(map(str, e.path))}")
    return errors


def collect_entity_ids_from_research_dir(research_dir: Path) -> set[str]:
    """Collect entity $id values under a single research directory."""
    ids: set[str] = set()
    if not research_dir.exists():
        return ids
    for path in research_dir.rglob("*.md"):
        frontmatter, _ = load_frontmatter(path)
        if not frontmatter:
            continue
        eid = frontmatter.get("$id")
        if eid:
            ids.add(eid)
    return ids


def build_entity_lookup(base_dirs: list[Path]) -> set[str]:
    """Return the set of entity $id values present under each base_dir/research."""
    ids: set[str] = set()
    for base_dir in base_dirs:
        ids |= collect_entity_ids_from_research_dir(base_dir / "research")
    return ids


def collect_all_endpoint_ids(skipped_entry_ids: set[str]) -> set[str]:
    """Return entity ids available as relationship endpoints.

    Endpoints may be in production or in any staged workstream research directory.
    Entries that failed validation/promotion are excluded.
    """
    ids = collect_entity_ids_from_research_dir(RESEARCH_DIR)
    workstreams_dir = STAGING_DIR / "workstreams"
    if workstreams_dir.exists():
        for ws_dir in workstreams_dir.iterdir():
            if ws_dir.is_dir():
                ids |= collect_entity_ids_from_research_dir(ws_dir / "research")
    return ids - skipped_entry_ids


def normalize_relationship_frontmatter(frontmatter: dict[str, Any]) -> dict[str, Any]:
    """Normalize relationship type and regenerate $id if the type changed."""
    if "type" in frontmatter and "source" in frontmatter:
        norm = entry_builder.normalize_relationship_type(frontmatter["type"])
        if norm and norm != frontmatter["type"]:
            frontmatter["type"] = norm
            src_id = frontmatter["source"]["id"]
            tgt_id = frontmatter["target"]["id"]
            frontmatter["$id"] = entry_builder.make_relationship_id(src_id, norm, tgt_id)
    return frontmatter


def promote_research(
    dry_run: bool,
    entry_validator: Draft202012Validator,
) -> tuple[int, int, int, set[str], set[str]]:
    """Promote staged research entries.

    Returns:
        (promoted, skipped_duplicate, skipped_invalid, promoted_ids, skipped_ids)
    """
    promoted = 0
    skipped_duplicate = 0
    skipped_invalid = 0
    promoted_ids: set[str] = set()
    skipped_ids: set[str] = set()

    for path in sorted(STAGING_DIR.rglob("research/**/*.md")):
        rel = path.relative_to(STAGING_DIR)
        parts = rel.parts
        # Strip two-level workstream segment: .staging/workstreams/<name>/research/...
        if len(parts) < 4 or parts[0] != "workstreams":
            continue
        target = RESEARCH_DIR / Path(*parts[3:])

        frontmatter, body = load_frontmatter(path)
        if not frontmatter:
            skipped_invalid += 1
            continue

        eid = frontmatter.get("$id")
        validation_errors = validate_frontmatter(frontmatter, entry_validator)
        if validation_errors:
            skipped_invalid += 1
            if eid:
                skipped_ids.add(eid)
            continue

        if target.exists():
            skipped_duplicate += 1
            if eid:
                skipped_ids.add(eid)
            continue

        if not dry_run:
            target.parent.mkdir(parents=True, exist_ok=True)
            if frontmatter.get("verification", {}).get("status") == "ai_proposed":
                frontmatter["verification"]["status"] = "unverified"
            target.write_text(dump_frontmatter(frontmatter, body), encoding="utf-8")

        promoted += 1
        if eid:
            promoted_ids.add(eid)

    return promoted, skipped_duplicate, skipped_invalid, promoted_ids, skipped_ids


def promote_relationships(
    dry_run: bool,
    relationship_validator: Draft202012Validator,
    promoted_entry_ids: set[str],
    skipped_entry_ids: set[str],
) -> tuple[int, int, int, int]:
    """Promote staged relationships whose endpoints exist.

    Returns:
        (promoted, skipped_duplicate, skipped_invalid, skipped_dangling)
    """
    # Endpoints may live in production or in any staged entry that was promoted.
    valid_endpoint_ids = collect_all_endpoint_ids(skipped_entry_ids)

    promoted = 0
    skipped_duplicate = 0
    skipped_invalid = 0
    skipped_dangling = 0

    for path in sorted(STAGING_DIR.rglob("data/relationships/*.md")):
        target = RELATIONSHIPS_DIR / path.name

        frontmatter, body = load_frontmatter(path)
        if not frontmatter:
            skipped_invalid += 1
            continue

        frontmatter = normalize_relationship_frontmatter(frontmatter)
        validation_errors = validate_frontmatter(frontmatter, relationship_validator)
        if validation_errors:
            skipped_invalid += 1
            continue

        source_id = frontmatter.get("source", {}).get("id")
        target_id = frontmatter.get("target", {}).get("id")
        if not source_id or not target_id:
            skipped_dangling += 1
            continue
        if source_id not in valid_endpoint_ids or target_id not in valid_endpoint_ids:
            skipped_dangling += 1
            continue

        if target.exists():
            skipped_duplicate += 1
            continue

        if not dry_run:
            RELATIONSHIPS_DIR.mkdir(parents=True, exist_ok=True)
            if frontmatter.get("verification", {}).get("status") == "ai_proposed":
                frontmatter["verification"]["status"] = "unverified"
            target.write_text(dump_frontmatter(frontmatter, body), encoding="utf-8")

        promoted += 1

    return promoted, skipped_duplicate, skipped_invalid, skipped_dangling


def main() -> int:
    parser = argparse.ArgumentParser(description="Auto-promote staged outputs to production.")
    parser.add_argument("--dry-run", action="store_true", help="Preview without moving files.")
    args = parser.parse_args()

    entry_validator, relationship_validator = compile_validators()

    entries_promoted, entries_dup, entries_invalid, promoted_ids, skipped_ids = promote_research(
        args.dry_run, entry_validator
    )
    rels_promoted, rels_dup, rels_invalid, rels_dangling = promote_relationships(
        args.dry_run, relationship_validator, promoted_ids, skipped_ids
    )

    print(f"Entries: promoted={entries_promoted}, skipped_duplicate={entries_dup}, skipped_invalid={entries_invalid}")
    print(
        f"Relationships: promoted={rels_promoted}, skipped_duplicate={rels_dup}, "
        f"skipped_invalid={rels_invalid}, skipped_dangling={rels_dangling}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
