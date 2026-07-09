#!/usr/bin/env python3
"""
Fix cross-layer relationship warnings by remapping relationship types to the
closest allowed type for the source/target theoretical-depth pair.
"""

import sys
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).parent))
from ai4sci_lib import config

ROOT = Path(__file__).parent.parent
RELATIONSHIPS_DIR = ROOT / "data" / "relationships"
RESEARCH_DIR = ROOT / "research"

GENERIC = {
    "cites", "verified_by", "conflicts_with", "is_version_of",
    "is_alternative_to", "competes_with", "is_substitute_for",
    "proposes", "evaluates_on", "uses", "is_based_on",
}


def load_frontmatter(path: Path) -> tuple[dict, str, str]:
    text = path.read_text(encoding="utf-8")
    _, rest = text.split("---", 1)
    ym, body = rest.split("---", 1)
    return yaml.safe_load(ym), ym, body


def dump_frontmatter(data: dict, body: str) -> str:
    ym = yaml.safe_dump(data, allow_unicode=True, sort_keys=False, default_flow_style=False, width=120)
    body_stripped = body.lstrip("\n")
    return f"---\n{ym}---\n{body_stripped}"


def depth_for_entity(eid: str, entities: dict) -> str:
    info = entities.get(eid, {})
    depths = info.get("theoretical_depth", [])
    for d in config.THEORETICAL_DEPTH_ORDER:
        if d in depths:
            return d
    type_to_depth = {
        "paper": "system", "robot_system": "system", "component": "system",
        "material": "system", "technology": "method", "method": "method",
        "algorithm": "method", "formalism": "formalism", "equation": "formalism",
        "operator": "formalism", "variable": "formalism", "constant": "formalism",
        "principle": "principle", "theorem": "principle", "foundation": "foundation",
    }
    return type_to_depth.get(info.get("type", "paper"), "system")


def load_entities() -> dict:
    entities = {}
    for path in RESEARCH_DIR.rglob("*.md"):
        try:
            data, _, _ = load_frontmatter(path)
        except Exception:
            continue
        eid = data.get("$id")
        if eid:
            entities[eid] = data
    return entities


def allowed_types(source_depth: str, target_depth: str) -> list[str]:
    return config.CROSS_LAYER_RELATIONSHIPS.get((source_depth, target_depth), [])


def fix_relationship(path: Path, entities: dict) -> bool:
    data, _, body = load_frontmatter(path)
    rel_type = data.get("type")
    source_id = data.get("source", {}).get("id")
    target_id = data.get("target", {}).get("id")
    if not source_id or not target_id:
        return False

    source_depth = depth_for_entity(source_id, entities)
    target_depth = depth_for_entity(target_id, entities)

    if source_depth == target_depth:
        return False

    if rel_type in GENERIC:
        return False

    allowed = allowed_types(source_depth, target_depth)

    if rel_type in allowed:
        return False

    # Map to the closest allowed or generic type.
    mapping = {
        "formalizes": "is_based_on",
        "requires": "has_prerequisite",
        "applies_to": "enables",
        "implemented_on": "instantiates",
        "leads_to": "builds_on",
        "feeds": "enables",
        "supports": "enables",
        "trains": "uses",
        "deployed_on": "implemented_on",
        "combined_with": "combines_with",
        "based_on": "is_based_on",
        "relies_on": "requires",
        "used_in": "applies_to",
        "followed_by": "builds_on",
    }
    new_type = mapping.get(rel_type)
    if new_type and (new_type in allowed or new_type in GENERIC):
        data["type"] = new_type
    elif allowed:
        data["type"] = allowed[0]
    elif rel_type in GENERIC:
        return False
    else:
        data["type"] = "mentions"

    path.write_text(dump_frontmatter(data, body), encoding="utf-8")
    return True


def main() -> int:
    entities = load_entities()
    fixed = 0
    if RELATIONSHIPS_DIR.exists():
        for path in RELATIONSHIPS_DIR.rglob("*.md"):
            try:
                if fix_relationship(path, entities):
                    fixed += 1
            except Exception as e:
                print(f"ERROR {path}: {e}", file=sys.stderr)
    print(f"Fixed {fixed} cross-layer relationship files.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
