#!/usr/bin/env python3
"""
Validate entity and relationship files against JSON schemas.

Usage:
    python scripts/validate_entries.py
"""

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


def main() -> int:
    entry_schema = json.loads((SCHEMA_DIR / "entry_schema.json").read_text())
    relationship_schema = json.loads((SCHEMA_DIR / "relationship_schema.json").read_text())

    errors = []

    print("Validating entity files...")
    errors.extend(validate_directory(RESEARCH_DIR, entry_schema))

    print("Validating relationship files...")
    errors.extend(validate_directory(RELATIONSHIPS_DIR, relationship_schema))

    if errors:
        print(f"\nFound {len(errors)} validation error(s):\n")
        for error in errors:
            print(f"  - {error}")
        return 1

    print("\nAll files validated successfully.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
