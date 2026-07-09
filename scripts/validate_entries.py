#!/usr/bin/env python3
"""
Validate entity and relationship files against JSON schemas.

Usage:
    python scripts/validate_entries.py
    python scripts/validate_entries.py --staging-dir .staging/workstreams/vla
    python scripts/validate_entries.py --include-workstreams
"""

import argparse
import json
import sys
from pathlib import Path
from typing import Any

try:
    import yaml
    from jsonschema import Draft202012Validator, ValidationError
except ImportError as e:
    print(f"Missing dependency: {e}")
    print("Run: source .venv/bin/activate && pip install jsonschema pyyaml")
    sys.exit(1)

sys.path.insert(0, str(Path(__file__).parent))
from ai4sci_lib import config


ROOT = Path(__file__).parent.parent
SCHEMA_DIR = ROOT / "data" / "schema" / "v1"
RESEARCH_DIR = ROOT / "research"
RELATIONSHIPS_DIR = ROOT / "data" / "relationships"
STAGING_DIR = ROOT / ".staging"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Validate entries and relationships.")
    parser.add_argument(
        "--staging-dir",
        type=Path,
        default=None,
        help="Validate a specific staging directory (e.g., .staging/workstreams/vla).",
    )
    parser.add_argument(
        "--include-workstreams",
        action="store_true",
        help="Also validate all workstream staging directories under .staging/workstreams/.",
    )
    return parser.parse_args()


def load_yaml_frontmatter(path: Path) -> dict:
    """Load YAML frontmatter from a Markdown file."""
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---"):
        raise ValueError(f"No YAML frontmatter found in {path}")
    _, rest = text.split("---", 1)
    yaml_text, _ = rest.split("---", 1)
    return yaml.safe_load(yaml_text)


def validate_file(path: Path, validator: Draft202012Validator) -> list[str]:
    """Validate a single file. Returns list of error messages."""
    errors = []
    try:
        data = load_yaml_frontmatter(path)
    except Exception as e:
        return [f"{path}: failed to parse YAML frontmatter: {e}"]

    try:
        validator.validate(data)
    except ValidationError as e:
        errors.append(f"{path}: {e.message} at {'/'.join(map(str, e.path))}")

    return errors


def validate_directory(directory: Path, validator: Draft202012Validator) -> list[str]:
    """Validate all Markdown files in a directory recursively."""
    errors = []
    for path in directory.rglob("*.md"):
        errors.extend(validate_file(path, validator))
    return errors


def build_entity_lookup(base_dirs: list[Path]) -> dict[str, dict[str, Any]]:
    """Build a lookup of entity id -> {type, theoretical_depth, path}."""
    lookup: dict[str, dict[str, Any]] = {}
    for base_dir in base_dirs:
        research_dir = base_dir / "research"
        if not research_dir.exists():
            continue
        for path in research_dir.rglob("*.md"):
            try:
                data = load_yaml_frontmatter(path)
            except Exception:
                continue
            eid = data.get("$id")
            if not eid:
                continue
            lookup[eid] = {
                "type": data.get("type", "paper"),
                "theoretical_depth": data.get("theoretical_depth", []),
                "path": path,
            }
    return lookup


def _depth_for_lookup(entity: dict[str, Any]) -> str:
    """Return the most concrete theoretical depth available, or infer from type."""
    depths = entity.get("theoretical_depth", [])
    if depths:
        # Prefer the most concrete (system > method > ...)
        for d in config.THEORETICAL_DEPTH_ORDER:
            if d in depths:
                return d
        return depths[0]
    # Fallback inference from entity type.
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


def validate_cross_layer_relationships(
    base_dirs: list[Path],
    warnings_only: bool = True,
) -> tuple[list[str], list[str]]:
    """Validate relationships against the cross-layer whitelist.

    Returns (errors, warnings). If warnings_only is True, cross-layer mismatches
    are reported as warnings rather than hard errors, to avoid blocking existing
    data while the graph is being migrated.
    """
    lookup = build_entity_lookup(base_dirs)
    errors: list[str] = []
    warns: list[str] = []

    for base_dir in base_dirs:
        rel_dir = base_dir / "data" / "relationships"
        if not rel_dir.exists():
            continue
        for path in rel_dir.rglob("*.md"):
            try:
                data = load_yaml_frontmatter(path)
            except Exception:
                continue
            rel_type = data.get("type", "")
            source_id = data.get("source", {}).get("id")
            target_id = data.get("target", {}).get("id")
            if not source_id or not target_id:
                continue
            source = lookup.get(source_id)
            target = lookup.get(target_id)
            if not source or not target:
                # Relationship to a missing entity; flag for review.
                msg = f"{path}: dangling relationship ({source_id} -> {target_id})"
                if warnings_only:
                    warns.append(msg)
                else:
                    errors.append(msg)
                continue

            source_depth = _depth_for_lookup(source)
            target_depth = _depth_for_lookup(target)

            # Same-depth relationships are allowed to use any non-knowledge relation
            # type, because they express domain semantics rather than abstraction jumps.
            if source_depth == target_depth:
                continue

            allowed = config.CROSS_LAYER_RELATIONSHIPS.get((source_depth, target_depth), [])
            # Generic relation types that are not layer-specific.
            generic = {
                "cites", "verified_by", "conflicts_with", "is_version_of",
                "is_alternative_to", "competes_with", "is_substitute_for",
                "proposes", "evaluates_on", "uses", "is_based_on", "mentions",
            }
            if rel_type not in allowed and rel_type not in generic:
                msg = (
                    f"{path}: '{rel_type}' is not allowed for "
                    f"{source_depth} -> {target_depth} "
                    f"({source_id} -> {target_id})"
                )
                if warnings_only:
                    warns.append(msg)
                else:
                    errors.append(msg)

    # Warn about entities missing theoretical_depth.
    missing_depth = [
        f"{info['path']}: missing theoretical_depth"
        for info in lookup.values()
        if not info.get("theoretical_depth")
    ]
    warns.extend(missing_depth)

    return errors, warns


def compile_validator(schema: dict) -> Draft202012Validator:
    """Compile a JSON schema validator once for reuse."""
    return Draft202012Validator(schema)


def validate_base(
    base_dir: Path,
    entry_validator: Draft202012Validator,
    relationship_validator: Draft202012Validator,
) -> list[str]:
    """Validate entity and relationship files under a base directory."""
    errors = []
    research_dir = base_dir / "research"
    relationships_dir = base_dir / "data" / "relationships"
    if research_dir.exists():
        print(f"Validating entity files under {research_dir}...")
        errors.extend(validate_directory(research_dir, entry_validator))
    if relationships_dir.exists():
        print(f"Validating relationship files under {relationships_dir}...")
        errors.extend(validate_directory(relationships_dir, relationship_validator))
    return errors


def main() -> int:
    args = parse_args()
    entry_schema = json.loads((SCHEMA_DIR / "entry_schema.json").read_text())
    relationship_schema = json.loads((SCHEMA_DIR / "relationship_schema.json").read_text())

    entry_validator = compile_validator(entry_schema)
    relationship_validator = compile_validator(relationship_schema)

    errors = []

    # Always validate production files.
    errors.extend(validate_base(ROOT, entry_validator, relationship_validator))

    # Validate a specific staging directory if requested.
    if args.staging_dir:
        errors.extend(validate_base(args.staging_dir, entry_validator, relationship_validator))

    # Validate all workstream staging directories if requested.
    if args.include_workstreams:
        workstreams_dir = STAGING_DIR / "workstreams"
        if workstreams_dir.exists():
            for ws_dir in sorted(workstreams_dir.iterdir()):
                if ws_dir.is_dir():
                    errors.extend(validate_base(ws_dir, entry_validator, relationship_validator))

    # Cross-layer validation across production + requested staging.
    base_dirs = [ROOT]
    if args.staging_dir:
        base_dirs.append(args.staging_dir)
    if args.include_workstreams:
        workstreams_dir = STAGING_DIR / "workstreams"
        if workstreams_dir.exists():
            for ws_dir in sorted(workstreams_dir.iterdir()):
                if ws_dir.is_dir():
                    base_dirs.append(ws_dir)
    cross_errors, cross_warnings = validate_cross_layer_relationships(base_dirs)
    errors.extend(cross_errors)

    if cross_warnings:
        print(f"\nFound {len(cross_warnings)} cross-layer warning(s):\n")
        for warning in cross_warnings[:50]:
            print(f"  - {warning}")
        if len(cross_warnings) > 50:
            print(f"  ... and {len(cross_warnings) - 50} more")

    if errors:
        print(f"\nFound {len(errors)} validation error(s):\n")
        for error in errors:
            print(f"  - {error}")
        return 1

    print("\nAll files validated successfully.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
