#!/usr/bin/env python3
"""
Extract additional relationship edges from Wiki chapter text.

Heuristic approach:
- Load all existing entities and their Chinese/English names.
- Read each Wiki chapter under wiki/docs/chapters/.
- Split text into sentences.
- For each sentence containing two or more entity mentions, look for a linking
  keyword between them and emit a relationship file.
- Skip duplicates and self-loops.
"""

import re
import sys
from pathlib import Path
from typing import Optional

import yaml

ROOT = Path(__file__).parent.parent
RESEARCH_DIR = ROOT / "research"
WIKI_CHAPTERS_DIR = ROOT / "wiki" / "docs" / "chapters"
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

# Chinese linking patterns → normalized relationship type.
LINK_PATTERNS = [
    (r"基于", "is_based_on"),
    (r"依赖", "requires"),
    (r"需要", "requires"),
    (r"包含", "includes"),
    (r"包括", "includes"),
    (r"组成", "is_part_of"),
    (r"应用于", "applies_to"),
    (r"用于", "applies_to"),
    (r"使用", "uses"),
    (r"采用", "uses"),
    (r"结合", "combines_with"),
    (r"融合", "combines_with"),
    (r"扩展", "extends"),
    (r"延伸", "extends"),
    (r"替代", "is_alternative_to"),
    (r"补充", "combines_with"),
    (r"支持", "enables"),
    (r"支撑", "enables"),
    (r"驱动", "enables"),
    (r"驱动.*需求", "drives_demand_for"),
    (r"产生", "produces"),
    (r"生成", "produces"),
    (r"验证", "validates_on"),
    (r"评估", "evaluates"),
    (r"测试", "tested_with"),
    (r"仿真", "simulates_with"),
    (r"模拟", "simulates_with"),
    (r"训练", "uses"),
    (r"学习", "uses"),
    (r"控制", "constrains"),
    (r"调节", "constrains"),
    (r"制造", "manufactured_by"),
    (r"生产", "produces"),
    (r"供应", "supplies"),
    (r"提供", "supplies"),
    (r"集成", "integrates"),
    (r"嵌入", "integrates"),
]


def load_entities() -> dict[str, dict]:
    """Return id -> {names, type, domains}."""
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
    """Map name variants (zh/en/ko) to entity ids. Longer names first."""
    index: dict[str, str] = {}
    for eid, info in entities.items():
        for lang, name in (info.get("names") or {}).items():
            if name:
                index[name] = eid
    return index


def find_entities_in_sentence(sentence: str, name_index: dict[str, str]) -> list[tuple[int, str, str]]:
    """Return sorted list of (position, name, eid) for entity mentions."""
    found = []
    # Longest names first to avoid partial matches.
    for name, eid in sorted(name_index.items(), key=lambda x: -len(x[0])):
        for m in re.finditer(re.escape(name), sentence):
            found.append((m.start(), name, eid))
    # Remove overlapping matches, keeping longest.
    found.sort()
    filtered = []
    last_end = -1
    for pos, name, eid in found:
        if pos >= last_end:
            filtered.append((pos, name, eid))
            last_end = pos + len(name)
    return filtered


def determine_rel_type(sentence: str, src_pos: int, src_len: int, tgt_pos: int) -> Optional[str]:
    """Look for a linking keyword between two entity mentions."""
    between = sentence[src_pos + src_len:tgt_pos]
    for pattern, rel_type in LINK_PATTERNS:
        if re.search(pattern, between):
            return rel_type
    return None


def sanitize_id_part(text: str) -> str:
    return re.sub(r"[^a-z0-9_]", "", text.lower().replace(" ", "_").replace("-", "_"))[:60]


def existing_relationships() -> set[tuple[str, str, str]]:
    existing: set[tuple[str, str, str]] = set()
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


def create_relationship(source_id: str, target_id: str, rel_type: str, entities: dict) -> str:
    RELATIONSHIPS_DIR.mkdir(parents=True, exist_ok=True)
    src_name = entities[source_id]["names"].get("zh") or entities[source_id]["names"].get("en") or source_id
    tgt_name = entities[target_id]["names"].get("zh") or entities[target_id]["names"].get("en") or target_id
    rid = f"rel_{sanitize_id_part(source_id)}_{rel_type}_{sanitize_id_part(target_id)}"
    path = RELATIONSHIPS_DIR / f"{rid}.md"
    counter = 1
    while path.exists():
        rid = f"rel_{sanitize_id_part(source_id)}_{rel_type}_{sanitize_id_part(target_id)}_{counter}"
        path = RELATIONSHIPS_DIR / f"{rid}.md"
        counter += 1

    src_domain = entities[source_id]["domains"][0] if entities[source_id]["domains"] else "00_foundations"
    tgt_domain = entities[target_id]["domains"][0] if entities[target_id]["domains"] else "00_foundations"

    content = f"""---
$id: {rid}
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: {rel_type}
source:
  id: {source_id}
  name:
    zh: {src_name}
    en: {entities[source_id]["names"].get("en") or src_name}
    ko: {entities[source_id]["names"].get("ko") or ""}
target:
  id: {target_id}
  name:
    zh: {tgt_name}
    en: {entities[target_id]["names"].get("en") or tgt_name}
    ko: {entities[target_id]["names"].get("ko") or ""}
domains:
  source_domain: {src_domain}
  target_domain: {tgt_domain}
description:
  zh: Wiki 章节文本提取的跨层关系。
  en: Cross-layer link extracted from Wiki chapter text.
  ko: ''
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-07-09'
  confidence: low
  notes: Heuristic extraction from Wiki; pending human review.
sources:
- id: src_wiki_extraction
  type: other
  title: Wiki extraction
  date: '2026-07-09'
  accessed_at: '2026-07-09'
---

{src_name} **{rel_type}** {tgt_name}。

该关系来自 Wiki 章节的文本提取。
"""
    path.write_text(content, encoding="utf-8")
    return rid


def main() -> int:
    if not WIKI_CHAPTERS_DIR.exists():
        print(f"Wiki chapters directory not found: {WIKI_CHAPTERS_DIR}")
        return 1

    entities = load_entities()
    name_index = build_name_index(entities)
    existing = existing_relationships()
    created = 0
    skipped = 0

    for chapter_path in sorted(WIKI_CHAPTERS_DIR.glob("chapter-*.md")):
        text = chapter_path.read_text(encoding="utf-8")
        # Remove Markdown links/images and code blocks for cleaner text.
        text = re.sub(r"!?\[([^\]]*)\]\([^)]*\)", r"\1", text)
        text = re.sub(r"```[\s\S]*?```", "", text)
        text = re.sub(r"`([^`]+)`", r"\1", text)

        # Split into sentences (Chinese sentence delimiters).
        sentences = re.split(r"[。！？\n]", text)
        for sentence in sentences:
            sentence = sentence.strip()
            if len(sentence) < 10:
                continue
            mentions = find_entities_in_sentence(sentence, name_index)
            if len(mentions) < 2:
                continue
            # Try to link consecutive mentions.
            for i in range(len(mentions) - 1):
                src_pos, src_name, src_id = mentions[i]
                tgt_pos, tgt_name, tgt_id = mentions[i + 1]
                if src_id == tgt_id:
                    continue
                rel_type = determine_rel_type(sentence, src_pos, len(src_name), tgt_pos)
                if not rel_type:
                    continue
                if rel_type not in VALID_REL_TYPES:
                    continue
                if (src_id, rel_type, tgt_id) in existing:
                    skipped += 1
                    continue
                create_relationship(src_id, tgt_id, rel_type, entities)
                existing.add((src_id, rel_type, tgt_id))
                created += 1

    print(f"Created {created} new relationship files; skipped {skipped} duplicates.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
