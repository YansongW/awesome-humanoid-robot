"""Build YAML frontmatter + Markdown entries and relationship files."""

from __future__ import annotations

import json
import re
import unicodedata
from pathlib import Path
from typing import Any

import yaml

from . import config


def _slugify(text: str, max_len: int = 40) -> str:
    """Create a filesystem-safe slug from text."""
    text = unicodedata.normalize("NFKD", text)
    text = text.encode("ascii", "ignore").decode("ascii")
    text = re.sub(r"[^\w\s-]", "", text).strip().lower()
    text = re.sub(r"[-\s]+", "_", text)
    return text[:max_len].strip("_")


def make_entry_id(entity_type: str, first_author: str, title: str, year: int | str) -> str:
    """Generate a deterministic entity ID."""
    author_slug = _slugify(first_author.split()[-1] if first_author else "unknown")
    title_slug = _slugify(title, max_len=30)
    return f"ent_{entity_type}_{author_slug}_{title_slug}_{year}"


def make_relationship_id(source_id: str, rel_type: str, target_id: str) -> str:
    """Generate a deterministic, schema-compliant lowercase relationship ID."""
    return f"rel_{source_id}_{rel_type}_{target_id}".lower()


def infer_subdir(entity_type: str) -> str:
    """Map entity type to research subdirectory."""
    return config.TYPE_TO_SUBDIR.get(entity_type, "papers")


def infer_layers(domains: list[str]) -> list[str]:
    """Infer value-chain layers from domains."""
    layers = sorted({config.LAYER_MAP[d] for d in domains if d in config.LAYER_MAP})
    return layers or ["intelligence"]


VALID_DOMAINS = set(config.DOMAIN_MAP.values())


def normalize_domains(domains: list[str]) -> tuple[list[str], list[str]]:
    """Split domain codes into valid and invalid lists against the canonical vocabulary."""
    valid = [d for d in domains if d in VALID_DOMAINS]
    invalid = [d for d in domains if d not in VALID_DOMAINS]
    return valid, invalid


# Map common LLM-generated relationship types to the project's controlled vocabulary.
RELATIONSHIP_TYPE_MAP = {
    # Supply / integration
    "component_used": "integrates",
    "uses_component": "integrates",
    "uses_hardware": "integrates",
    "uses_part": "integrates",
    "uses_metric": "uses",
    "uses_product_of": "uses",
    # Verification / evaluation
    "evaluates_with": "verified_by",
    "validated_by": "verified_by",
    "validates_with": "verified_by",
    "evaluated_on": "evaluates_on",
    # Derivation / extension
    "based_on": "is_based_on",
    "uses_method": "is_based_on",
    "builds_on": "builds_on",
    "improves": "builds_on",
    "extends_to": "extends",
    "applies": "uses",
    "implements": "instantiates",
    "describes": "proposes",
    "studies": "proposes",
    # Data / sourcing
    "uses_data_from": "sources_from",
    "data_from": "sources_from",
    # Comparison / citation
    "compares_to": "is_alternative_to",
    "compared_to": "is_alternative_to",
    "contrasts_with": "is_alternative_to",
    "utilizes": "requires",
    "employs": "requires",
    "mentions": "cites",
    "references": "cites",
    "discusses": "cites",
}


def normalize_relationship_type(rel_type: str) -> str:
    """Normalize an LLM relationship type to the allowed vocabulary."""
    return RELATIONSHIP_TYPE_MAP.get(rel_type, rel_type)


def build_entry_frontmatter(data: dict[str, Any]) -> dict[str, Any]:
    """Validate and normalize entry frontmatter data."""
    required = [
        "$id", "type", "names", "summary", "domains",
        "layers", "functional_roles", "verification", "sources",
    ]
    for key in required:
        if key not in data:
            raise ValueError(f"Missing required frontmatter key: {key}")
    frontmatter = {
        "$id": data["$id"],
        "$schema": "../../data/schema/v1/entry_schema.json",
        "$version": 1,
        "type": data["type"],
        "names": data["names"],
        "summary": data["summary"],
        "domains": data["domains"],
        "layers": data["layers"],
        "functional_roles": data["functional_roles"],
        "tags": data.get("tags", []),
        "verification": data["verification"],
        "sources": data["sources"],
    }
    if "related_entities" in data and data["related_entities"]:
        frontmatter["related_entities"] = data["related_entities"]
    return frontmatter


def build_relationship_frontmatter(data: dict[str, Any]) -> dict[str, Any]:
    """Validate and normalize relationship frontmatter data."""
    required = ["$id", "type", "source", "target", "description", "verification", "sources"]
    for key in required:
        if key not in data:
            raise ValueError(f"Missing required relationship key: {key}")
    return {
        "$id": data["$id"],
        "$schema": "../schema/v1/relationship_schema.json",
        "$version": 1,
        "type": data["type"],
        "source": data["source"],
        "target": data["target"],
        "domains": data.get("domains", {}),
        "description": data["description"],
        "verification": data["verification"],
        "sources": data["sources"],
    }


def dump_frontmatter(frontmatter: dict[str, Any]) -> str:
    """Dump frontmatter to YAML string."""
    return yaml.dump(frontmatter, sort_keys=False, allow_unicode=True, default_flow_style=False)


def write_entry_file(
    frontmatter: dict[str, Any],
    body: str,
    subdir: str,
    filename: str,
    base_dir: Path | None = None,
) -> Path:
    """Write an entry Markdown file."""
    base_dir = base_dir or config.RESEARCH_DIR
    out_dir = base_dir / subdir
    out_dir.mkdir(parents=True, exist_ok=True)
    path = out_dir / filename
    content = f"---\n{dump_frontmatter(frontmatter)}---\n\n{body.strip()}\n"
    path.write_text(content, encoding="utf-8")
    return path


def write_relationship_file(
    frontmatter: dict[str, Any],
    base_dir: Path | None = None,
) -> Path:
    """Write a standalone relationship Markdown file."""
    base_dir = base_dir or config.RELATIONSHIPS_DIR
    base_dir.mkdir(parents=True, exist_ok=True)
    filename = f"{frontmatter['$id']}.md"
    path = base_dir / filename
    content = f"---\n{dump_frontmatter(frontmatter)}---\n"
    path.write_text(content, encoding="utf-8")
    return path


def load_existing_ids() -> set[str]:
    """Load all existing entity and relationship IDs from the project."""
    ids: set[str] = set()
    for path in config.RESEARCH_DIR.rglob("*.md"):
        try:
            text = path.read_text(encoding="utf-8")
            if text.startswith("---"):
                _, rest = text.split("---", 1)
                yaml_text, _ = rest.split("---", 1)
                data = yaml.safe_load(yaml_text)
                if data and "$id" in data:
                    ids.add(data["$id"])
        except Exception:
            continue
    for path in config.RELATIONSHIPS_DIR.glob("*.md"):
        try:
            text = path.read_text(encoding="utf-8")
            if text.startswith("---"):
                _, rest = text.split("---", 1)
                yaml_text, _ = rest.split("---", 1)
                data = yaml.safe_load(yaml_text)
                if data and "$id" in data:
                    ids.add(data["$id"])
        except Exception:
            continue
    return ids
