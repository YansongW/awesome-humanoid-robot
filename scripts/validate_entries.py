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

try:
    import yaml
    from jsonschema import validate, ValidationError
except ImportError as e:
    print(f"Missing dependency: {e}")
    print("Run: source .venv/bin/activate && pip install jsonschema pyyaml")
    sys.exit(1)


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


def validate_file(path: Path, schema: dict) -> list[str]:
    """Validate a single file. Returns list of error messages."""
    errors = []
    try:
        data = load_yaml_frontmatter(path)
    except Exception as e:
        return [f"{path}: failed to parse YAML frontmatter: {e}"]

    try:
        validate(instance=data, schema=schema)
    except ValidationError as e:
        errors.append(f"{path}: {e.message} at {'/'.join(map(str, e.path))}")

    return errors


def validate_directory(directory: Path, schema: dict) -> list[str]:
    """Validate all Markdown files in a directory recursively."""
    errors = []
    for path in directory.rglob("*.md"):
        errors.extend(validate_file(path, schema))
    return errors


def validate_base(base_dir: Path, entry_schema: dict, relationship_schema: dict) -> list[str]:
    """Validate entity and relationship files under a base directory."""
    errors = []
    research_dir = base_dir / "research"
    relationships_dir = base_dir / "data" / "relationships"
    if research_dir.exists():
        print(f"Validating entity files under {research_dir}...")
        errors.extend(validate_directory(research_dir, entry_schema))
    if relationships_dir.exists():
        print(f"Validating relationship files under {relationships_dir}...")
        errors.extend(validate_directory(relationships_dir, relationship_schema))
    return errors


def main() -> int:
    args = parse_args()
    entry_schema = json.loads((SCHEMA_DIR / "entry_schema.json").read_text())
    relationship_schema = json.loads((SCHEMA_DIR / "relationship_schema.json").read_text())

    errors = []

    # Always validate production files.
    errors.extend(validate_base(ROOT, entry_schema, relationship_schema))

    # Validate a specific staging directory if requested.
    if args.staging_dir:
        errors.extend(validate_base(args.staging_dir, entry_schema, relationship_schema))

    # Validate all workstream staging directories if requested.
    if args.include_workstreams:
        workstreams_dir = STAGING_DIR / "workstreams"
        if workstreams_dir.exists():
            for ws_dir in sorted(workstreams_dir.iterdir()):
                if ws_dir.is_dir():
                    errors.extend(validate_base(ws_dir, entry_schema, relationship_schema))

    if errors:
        print(f"\nFound {len(errors)} validation error(s):\n")
        for error in errors:
            print(f"  - {error}")
        return 1

    print("\nAll files validated successfully.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
