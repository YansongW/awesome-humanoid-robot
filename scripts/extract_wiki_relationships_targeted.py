#!/usr/bin/env python3
"""
Targeted Wiki relationship extraction for chapters that already have content.

Only processes wiki/docs/chapters/chapter-01.md through chapter-08.md.
For each gap entity, finds sections that mention it and creates "mentions"
relationships to other entities that appear in the same section.

This is intentionally conservative: relationship semantics are weak, so all
edges are marked unverified/low-confidence.
"""

import re
import sys
from pathlib import Path
from typing import Optional

import yaml

ROOT = Path(__file__).parent.parent
MAPPING_FILE = ROOT / "data" / "wiki-chapter-mapping.yaml"
WIKI_DIR = ROOT / "wiki" / "docs" / "chapters"
RESEARCH_DIR = ROOT / "research"
RELATIONSHIPS_DIR = ROOT / "data" / "relationships" / "wiki"

VALID_REL_TYPES = {
    "acknowledges", "addresses", "affiliated", "affiliated_with", "affiliation",
    "analyzes", "applied_in", "applies_to", "approximates", "assumes", "authored_by",
    "authored_by_affiliation", "benchmarks", "builds_on", "built_upon", "case_study",
    "cites", "collaborates_with", "combines_with", "compares", "compares_with",
    "compensates_for", "competes_with", "conflicts_with", "constrains", "consumes",
    "demonstrates", "demonstrates_on", "derived_from", "developed_by", "develops",
    "discusses", "discusses_application_to", "distributes", "drives_demand_for",
    "enables", "establishes_hardness_on", "estimates", "evaluated_at", "evaluated_in",
    "evaluated_with", "evaluates", "evaluates_against", "evaluates_in", "evaluates_on",
    "extends", "formalizes", "funded_by", "generalizes_to", "has_prerequisite",
    "implemented_on", "implements_in", "implements_on", "implements_with", "includes",
    "instantiates", "instantiates_on", "institutional_affiliation", "integrates",
    "introduces", "is_alternative_to", "is_based_on", "is_instance_of", "is_part_of",
    "is_prerequisite_for", "is_regulated_by", "is_substitute_for", "is_subsystem_of",
    "is_version_of", "manufactured_by", "manufacturer_of", "mentions", "minimizes",
    "models", "part_of", "produces", "proposes", "releases", "requires", "reviews",
    "serves", "simulates_with", "solves", "sources_from", "studies_subclasses_of",
    "supplies", "surveys", "targets", "tested_with", "transfers_to", "uses",
    "uses_benchmark", "uses_data", "uses_dataset", "uses_hardware_from",
    "uses_implementation_from", "uses_material", "uses_notation_from", "uses_platform",
    "uses_product_of", "uses_simulator", "uses_software", "uses_technology",
    "uses_theorem", "validated_on", "validates_on", "verified_by",
}


def load_entities() -> dict[str, dict]:
    entities = {}
    for path in RESEARCH_DIR.rglob("*.md"):
        text = path.read_text(encoding="utf-8")
        if not text.startswith("---"):
            continue
        _, rest = text.split("---", 1)
        ym, _ = rest.split("---", 1)
        try:
            data = yaml.safe_load(ym)
        except Exception:
            continue
        eid = data.get("$id")
        if not eid:
            continue
        entities[eid] = {
            "type": data.get("type", ""),
            "domains": data.get("domains", []) or [],
            "names": data.get("names", {}) or {},
        }
    return entities


def build_name_index(entities: dict[str, dict]) -> dict[str, str]:
    index = {}
    for eid, info in entities.items():
        for lang, name in (info.get("names") or {}).items():
            if name and len(name) >= 2:
                index[name] = eid
    return index


def normalize_name(name: str) -> str:
    name = name.strip()
    name = re.sub(r"[（(][^）)]+[）)]", "", name)
    return name.replace(" ", "").replace("/", "")


def find_mentions(text: str, name_index: dict[str, str]) -> list[tuple[str, str]]:
    """Return list of (name, eid) mentions in text, preferring longest matches."""
    found = []
    for name, eid in sorted(name_index.items(), key=lambda x: -len(x[0])):
        for m in re.finditer(re.escape(name), text):
            found.append((m.start(), len(name), name, eid))
    found.sort()
    filtered = []
    last_end = -1
    for pos, length, name, eid in found:
        if pos >= last_end:
            filtered.append((name, eid))
            last_end = pos + length
    return filtered


def extract_sections(chapter_text: str) -> list[str]:
    """Split chapter into sections by Markdown headings."""
    sections = re.split(r"\n(?=#+\s)", chapter_text)
    return [s.strip() for s in sections if len(s.strip()) > 50]


def existing_relationships() -> set[tuple[str, str, str]]:
    existing = set()
    if not RELATIONSHIPS_DIR.exists():
        return existing
    for path in RELATIONSHIPS_DIR.rglob("*.md"):
        text = path.read_text(encoding="utf-8")
        if not text.startswith("---"):
            continue
        _, rest = text.split("---", 1)
        ym, _ = rest.split("---", 1)
        try:
            data = yaml.safe_load(ym)
        except Exception:
            continue
        existing.add((
            data.get("source", {}).get("id", ""),
            data.get("type", ""),
            data.get("target", {}).get("id", ""),
        ))
    return existing


def sanitize_id_part(text: str) -> str:
    return re.sub(r"[^a-z0-9_]", "", text.lower().replace(" ", "_").replace("-", "_"))[:50]


def create_relationship(source_id: str, target_id: str, entities: dict, existing: set) -> Optional[str]:
    from typing import Optional
    if source_id == target_id:
        return None
    if (source_id, "mentions", target_id) in existing:
        return None

    RELATIONSHIPS_DIR.mkdir(parents=True, exist_ok=True)
    src_names = entities[source_id]["names"]
    tgt_names = entities[target_id]["names"]
    src_name = src_names.get("zh") or src_names.get("en") or source_id
    tgt_name = tgt_names.get("zh") or tgt_names.get("en") or target_id
    src_ko = src_names.get("ko") or ""
    tgt_ko = tgt_names.get("ko") or ""
    rid = f"rel_{sanitize_id_part(source_id)}_mentions_{sanitize_id_part(target_id)}"
    path = RELATIONSHIPS_DIR / f"{rid}.md"
    counter = 1
    while path.exists():
        rid = f"rel_{sanitize_id_part(source_id)}_mentions_{sanitize_id_part(target_id)}_{counter}"
        path = RELATIONSHIPS_DIR / f"{rid}.md"
        counter += 1

    src_domain = entities[source_id]["domains"][0] if entities[source_id]["domains"] else "00_foundations"
    tgt_domain = entities[target_id]["domains"][0] if entities[target_id]["domains"] else "00_foundations"

    content = f"""---
$id: {rid}
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: mentions
source:
  id: {source_id}
  name:
    zh: {src_name}
    en: {src_names.get("en") or src_name}
    ko: {src_ko}
target:
  id: {target_id}
  name:
    zh: {tgt_name}
    en: {tgt_names.get("en") or tgt_name}
    ko: {tgt_ko}
domains:
  source_domain: {src_domain}
  target_domain: {tgt_domain}
description:
  zh: 同一 Wiki 章节中共同出现的关系。
  en: Co-occurrence relationship extracted from the same Wiki chapter section.
  ko: ''
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-07-09'
  confidence: low
  notes: Targeted extraction from early Wiki chapters; semantic relation is weak.
sources:
- id: src_wiki_extraction
  type: other
  title: Wiki extraction
  date: '2026-07-09'
  accessed_at: '2026-07-09'
---

{src_name} **mentions** {tgt_name}。

该关系来自 Wiki 章节同一小节的共现提取。
"""
    path.write_text(content, encoding="utf-8")
    existing.add((source_id, "mentions", target_id))
    return rid


def main() -> int:
    if not MAPPING_FILE.exists():
        print(f"Mapping file not found: {MAPPING_FILE}")
        return 1

    mapping = yaml.safe_load(MAPPING_FILE.read_text(encoding="utf-8"))
    entities = load_entities()
    name_index = build_name_index(entities)
    existing = existing_relationships()
    created = 0

    for chapter in mapping.get("chapters", []):
        num = chapter.get("number")
        if num is None or num < 1 or num > 8:
            continue
        chapter_file = WIKI_DIR / f"chapter-{num:02d}.md"
        if not chapter_file.exists():
            continue
        text = chapter_file.read_text(encoding="utf-8")
        if text.startswith("---"):
            _, rest = text.split("---", 1)
            _, text = rest.split("---", 1)
        if len(text.strip()) < 200:
            continue

        sections = extract_sections(text)
        gap_ids = {g["id"] for g in chapter.get("gaps", [])}

        for section in sections:
            mentions = find_mentions(section, name_index)
            section_ids = {eid for _, eid in mentions}
            # Create co-occurrence edges between gap entities and other entities.
            for gap_id in gap_ids:
                if gap_id not in section_ids:
                    continue
                for _, eid in mentions:
                    if eid == gap_id:
                        continue
                    if create_relationship(gap_id, eid, entities, existing):
                        created += 1

    print(f"Created {created} targeted co-occurrence relationships from Wiki chapters 1-8.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
