#!/usr/bin/env python3
"""
Relationship backfill for the awesome-humanoid-robot knowledge graph.

This script proposes new relationships among existing production entities that the
automated pipeline missed, primarily because the LLM originally suggested targets
that did not yet exist. It runs in two phases:

1. Heuristic pass: type-pair + name/tag overlap to create high-confidence links.
2. LLM pass: ask an LLM to review candidate targets for entities still lacking
   enough relationships.

Usage:
    AI4SCI_USE_KIMI_CLI=1 python scripts/relationship_backfill.py
    AI4SCI_USE_KIMI_CLI=1 python scripts/relationship_backfill.py --llm-only
    AI4SCI_USE_KIMI_CLI=1 python scripts/relationship_backfill.py --dry-run --limit-sources 20
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

import yaml

sys.path.insert(0, str(Path(__file__).parent))
from ai4sci_lib import config, entry_builder, llm_client


ROOT = config.ROOT
RESEARCH_DIR = config.RESEARCH_DIR
RELATIONSHIPS_DIR = config.RELATIONSHIPS_DIR
SCHEMA_DIR = config.SCHEMA_DIR

# Allowed relationship types from the schema.
with (SCHEMA_DIR / "relationship_schema.json").open(encoding="utf-8") as _f:
    RELATIONSHIP_SCHEMA = json.load(_f)
ALLOWED_REL_TYPES: set[str] = set(RELATIONSHIP_SCHEMA["properties"]["type"]["enum"])


@dataclass
class Entity:
    id: str
    type: str
    names: dict[str, str]
    summary_en: str
    domains: set[str]
    layers: set[str]
    tags: set[str]
    path: Path

    @property
    def name_en(self) -> str:
        return self.names.get("en", self.id)


# Default relationship for a source type -> target type when there is a strong
# topical overlap. These are intentionally conservative; the heuristic pass only
# creates a link when names/tags overlap.
DEFAULT_REL_TYPE: dict[tuple[str, str], str] = {
    # Organisations / products
    ("oem", "robot_system"): "produces",
    ("component_manufacturer", "component"): "produces",
    ("component_manufacturer", "robot_system"): "produces",
    ("tier1_supplier", "component"): "supplies",
    ("tier1_supplier", "robot_system"): "supplies",
    ("tier2_supplier", "component"): "supplies",
    ("material_supplier", "material"): "supplies",
    ("software_vendor", "software_platform"): "produces",
    ("software_vendor", "component"): "produces",
    ("research_institution", "paper"): "produces",
    ("standards_body", "standard"): "produces",
    # Products / subsystems
    ("robot_system", "component"): "integrates",
    ("robot_system", "technology"): "uses",
    ("robot_system", "software_platform"): "uses",
    ("robot_system", "application_scenario"): "serves",
    ("robot_system", "market_segment"): "serves",
    ("component", "component"): "is_alternative_to",
    ("component", "material"): "requires",
    ("component", "technology"): "uses",
    ("technology", "component"): "enables",
    ("technology", "material"): "requires",
    ("material", "component"): "enables",
    ("material", "technology"): "enables",
    # Knowledge artifacts
    ("paper", "paper"): "cites",
    ("paper", "component"): "uses",
    ("paper", "robot_system"): "evaluates_on",
    ("paper", "dataset"): "sources_from",
    ("paper", "benchmark"): "evaluates_on",
    ("paper", "technology"): "uses",
    ("paper", "method"): "is_based_on",
    ("paper", "concept"): "is_based_on",
    ("paper", "algorithm"): "is_based_on",
    ("paper", "formalism"): "is_based_on",
    ("paper", "foundation"): "is_based_on",
    ("paper", "equation"): "uses",
    ("paper", "material"): "uses",
    ("benchmark", "paper"): "cites",
    ("benchmark", "dataset"): "evaluates_on",
    ("report", "paper"): "cites",
    ("report", "material"): "cites",
    ("standard", "component"): "is_regulated_by",
    ("standard", "robot_system"): "is_regulated_by",
    ("regulation", "robot_system"): "is_regulated_by",
    ("certification", "robot_system"): "is_regulated_by",
}

# Type pairs that are allowed to be symmetric / reversed.
TYPE_PAIR_HINTS: dict[tuple[str, str], list[str]] = {
    ("paper", "paper"): ["cites", "is_based_on", "builds_on", "extends", "is_alternative_to"],
    ("paper", "component"): ["integrates", "uses", "proposes"],
    ("paper", "robot_system"): ["integrates", "evaluates_on", "uses"],
    ("paper", "dataset"): ["sources_from", "uses"],
    ("paper", "benchmark"): ["evaluates_on", "cites"],
    ("paper", "technology"): ["uses", "proposes", "builds_on"],
    ("paper", "method"): ["is_based_on", "uses", "builds_on"],
    ("paper", "concept"): ["is_based_on", "uses"],
    ("paper", "algorithm"): ["is_based_on", "uses"],
    ("paper", "formalism"): ["is_based_on", "uses"],
    ("paper", "foundation"): ["is_based_on", "uses"],
    ("paper", "equation"): ["uses", "is_based_on"],
    ("paper", "material"): ["uses", "requires"],
    ("robot_system", "component"): ["integrates", "requires", "uses"],
    ("robot_system", "technology"): ["uses", "requires", "enables"],
    ("robot_system", "application_scenario"): ["serves", "drives_demand_for"],
    ("robot_system", "market_segment"): ["serves", "drives_demand_for"],
    ("component", "component"): ["integrates", "requires", "is_part_of"],
    ("component", "material"): ["requires", "uses"],
    ("component", "technology"): ["uses", "requires"],
    ("technology", "component"): ["enables", "requires"],
    ("technology", "material"): ["requires", "uses"],
    ("material", "component"): ["enables", "is_part_of"],
    ("material", "technology"): ["enables", "requires"],
    ("benchmark", "dataset"): ["evaluates_on", "uses"],
    ("benchmark", "paper"): ["cites", "is_based_on"],
    ("dataset", "benchmark"): ["evaluates_on", "serves"],
    ("company", "robot_system"): ["produces", "develops"],  # develops not schema; filtered later
    ("company", "component"): ["produces", "supplies"],
}


def load_entities() -> list[Entity]:
    """Load all production entities."""
    entities: list[Entity] = []
    for path in RESEARCH_DIR.rglob("*.md"):
        try:
            text = path.read_text(encoding="utf-8")
            if not text.startswith("---"):
                continue
            _, rest = text.split("---", 1)
            yaml_text, _ = rest.split("---", 1)
            data = yaml.safe_load(yaml_text) or {}
            ent_id = data.get("$id")
            if not ent_id:
                continue
            names = data.get("names", {})
            summary = data.get("summary", {})
            summary_en = summary.get("en", "") if isinstance(summary, dict) else str(summary)
            entities.append(
                Entity(
                    id=ent_id,
                    type=data.get("type", "paper"),
                    names=names if isinstance(names, dict) else {},
                    summary_en=summary_en,
                    domains=set(data.get("domains", [])),
                    layers=set(data.get("layers", [])),
                    tags=set(data.get("tags", [])),
                    path=path,
                )
            )
        except Exception:
            continue
    return entities


def load_existing_relationships() -> dict[tuple[str, str, str], dict[str, Any]]:
    """Load existing relationship files keyed by (source_id, type, target_id)."""
    existing: dict[tuple[str, str, str], dict[str, Any]] = {}
    for path in RELATIONSHIPS_DIR.glob("*.md"):
        try:
            text = path.read_text(encoding="utf-8")
            if not text.startswith("---"):
                continue
            _, rest = text.split("---", 1)
            data = yaml.safe_load(rest.split("---", 1)[0]) or {}
            src = data.get("source", {}).get("id")
            tgt = data.get("target", {}).get("id")
            rel_type = data.get("type")
            if src and tgt and rel_type:
                existing[(src, rel_type, tgt)] = data
        except Exception:
            continue
    return existing


# Tokens that are too generic to be used as mention evidence.
GENERIC_TOKENS = {
    "the", "and", "for", "with", "of", "on", "in", "to", "by", "a", "an", "is", "are",
    "humanoid", "humanoids", "robot", "robots", "robotics",
    "system", "systems", "component", "components", "technology", "technologies",
    "method", "methods", "algorithm", "algorithms", "model", "models", "data",
    "dataset", "datasets", "benchmark", "benchmarks", "paper", "report", "study",
    "analysis", "application", "applications", "market", "segment", "framework",
    "control", "planning", "learning", "simulation", "hardware", "software",
    "manufacturing", "production", "design", "engineering", "material", "materials",
    "equation", "equations", "foundation", "foundations", "concept", "concepts",
    "variable", "variables", "constant", "constants", "operator", "operators",
    "approximation", "approximations", "theorem", "theorems", "principle", "principles",
    "hand", "hands", "actuator", "actuators", "servo", "servos", "motor", "motors",
    "sensor", "sensors", "controller", "controllers", "reducer", "reducers", "gear", "gears",
    "battery", "batteries", "board", "boards", "chip", "chips", "processor", "processors",
    "compute", "computing", "joint", "joints", "inference", "device", "edge",
}


def _normalize(text: str) -> str:
    """Lower-case and collapse non-alphanumerics to spaces."""
    return re.sub(r"[^a-z0-9]+", " ", text.lower()).strip()


def _name_variants(entity: Entity, include_tags: bool = True) -> set[str]:
    """Return candidate strings that, if found in a summary, indicate a mention."""
    variants: set[str] = set()
    # English name.
    name_en = entity.name_en.strip()
    if name_en:
        variants.add(name_en.lower())
        # Normalized token sequence.
        variants.add(_normalize(name_en))
    # ID-derived tokens (drop the ent_ prefix and type token).
    id_parts = entity.id.lower().split("_")
    # Heuristic: drop leading 'ent' and the second token if it matches the entity type.
    if id_parts and id_parts[0] == "ent":
        id_parts = id_parts[1:]
    if id_parts and id_parts[0] == entity.type.lower().replace("_", ""):
        id_parts = id_parts[1:]
    for token in id_parts:
        if len(token) >= 3 and token not in GENERIC_TOKENS:
            variants.add(token)
    if include_tags:
        for tag in entity.tags:
            tag = tag.strip().lower()
            if len(tag) >= 3 and tag not in GENERIC_TOKENS:
                variants.add(tag)
    return variants


def _mentions(summary: str, entity: Entity, allow_tags: bool = True) -> bool:
    """Check whether the summary explicitly mentions the entity.

    Args:
        summary: Source summary text.
        entity: Target entity.
        allow_tags: If False, only the English name and ID-derived tokens are used;
            target tags are ignored. This avoids false matches caused by generic or
            shared component tags (e.g., "dynamixel").
    """
    summary_lower = summary.lower()
    variants = _name_variants(entity, include_tags=allow_tags)
    for variant in variants:
        if not variant:
            continue
        if len(variant.split()) > 1:
            if variant in summary_lower:
                return True
        else:
            if re.search(r"\b" + re.escape(variant) + r"\b", summary_lower):
                return True
    return False


def _name_mentions(summary: str, entity: Entity) -> bool:
    """Strict name-only mention check."""
    summary_lower = summary.lower()
    name_en = entity.name_en.strip().lower()
    if name_en and len(name_en) >= 3:
        if name_en in summary_lower:
            return True
        normalized = _normalize(entity.name_en)
        if normalized and normalized in summary_lower:
            return True
    return False


def _score_pair(src: Entity, tgt: Entity) -> int:
    """Score how likely a relationship between src and tgt is worth proposing."""
    score = 0
    shared_domains = src.domains & tgt.domains
    shared_layers = src.layers & tgt.layers
    shared_tags = src.tags & tgt.tags
    score += len(shared_domains) * 2
    score += len(shared_layers) * 1
    score += len(shared_tags) * 2
    if _mentions(src.summary_en, tgt):
        score += 15
    type_key = (src.type, tgt.type)
    if type_key in DEFAULT_REL_TYPE or type_key in TYPE_PAIR_HINTS:
        score += 3
    return score


def _candidate_targets(src: Entity, entities: list[Entity], existing: set[tuple[str, str, str]], top_k: int = 20) -> list[tuple[Entity, int]]:
    """Return the top-K candidate targets for a source, excluding existing relations."""
    scored: list[tuple[Entity, int]] = []
    for tgt in entities:
        if tgt.id == src.id:
            continue
        if (src.id, tgt.id) in {(s, t) for s, _, t in existing}:
            continue
        score = _score_pair(src, tgt)
        if score <= 0:
            continue
        scored.append((tgt, score))
    scored.sort(key=lambda x: (-x[1], x[0].id))
    return scored[:top_k]


def _normalize_rel_type(rel_type: str) -> str:
    """Normalize and validate a relationship type against the schema."""
    rel_type = entry_builder.normalize_relationship_type(rel_type)
    if rel_type not in ALLOWED_REL_TYPES:
        return ""
    return rel_type


def _build_relationship_frontmatter(
    src: Entity,
    tgt: Entity,
    rel_type: str,
    description: str,
    confidence: str,
    sources: list[dict[str, Any]],
) -> dict[str, Any]:
    """Create a relationship frontmatter dict."""
    rel_id = entry_builder.make_relationship_id(src.id, rel_type, tgt.id)
    today = str(__import__("datetime").date.today())
    return {
        "$id": rel_id,
        "$schema": "../schema/v1/relationship_schema.json",
        "$version": 1,
        "type": rel_type,
        "source": {
            "id": src.id,
            "name": src.names,
        },
        "target": {
            "id": tgt.id,
            "name": tgt.names,
        },
        "domains": {
            "source_domain": sorted(src.domains)[0] if src.domains else "",
            "target_domain": sorted(tgt.domains)[0] if tgt.domains else "",
        },
        "description": {
            "en": description,
            "zh": "",
            "ko": "",
        },
        "verification": {
            "status": "ai_proposed" if confidence == "low" else "partially_verified",
            "reviewed_by": "ai",
            "reviewed_at": today,
            "confidence": confidence,
            "notes": "Generated by relationship backfill heuristic." if confidence in {"low", "medium"} else "Generated by relationship backfill with LLM review.",
        },
        "sources": sources,
    }


def _sources_from_entity(entity: Entity) -> list[dict[str, Any]]:
    """Extract a usable source reference from an entity frontmatter."""
    try:
        text = entity.path.read_text(encoding="utf-8")
        _, rest = text.split("---", 1)
        data = yaml.safe_load(rest.split("---", 1)[0]) or {}
        sources = data.get("sources", [])
        if sources:
            first = sources[0]
            return [{
                "id": first.get("id", "src_backfill_001"),
                "type": first.get("type", "website"),
                "title": first.get("title", entity.name_en),
                "url": first.get("url", ""),
                "date": first.get("date", ""),
                "accessed_at": first.get("accessed_at", str(__import__("datetime").date.today())),
            }]
    except Exception:
        pass
    return [{
        "id": "src_backfill_001",
        "type": "website",
        "title": entity.name_en,
        "url": "",
        "date": "",
        "accessed_at": str(__import__("datetime").date.today()),
    }]


def _company_rel_type(src: Entity, tgt: Entity) -> str:
    """Pick the most appropriate company -> product relationship type."""
    if src.type in {"tier1_supplier", "tier2_supplier", "material_supplier"}:
        return "supplies"
    if src.type == "software_vendor" and tgt.type == "software_platform":
        return "produces"
    return "produces"


def _relation_type_for_pair(src: Entity, tgt: Entity) -> str:
    """Return a schema-allowed relationship type for a source/target type pair."""
    type_key = (src.type, tgt.type)
    if type_key in DEFAULT_REL_TYPE:
        rel_type = DEFAULT_REL_TYPE[type_key]
        # Refine company -> product.
        if src.type in {"oem", "component_manufacturer", "tier1_supplier", "tier2_supplier", "software_vendor", "material_supplier"} and tgt.type in {"component", "robot_system", "software_platform", "material", "dataset"}:
            rel_type = _company_rel_type(src, tgt)
        return rel_type

    # Fallbacks for common pairs.
    if src.type == "paper":
        if tgt.type == "paper":
            return "cites"
        if tgt.type in {"component", "robot_system", "technology", "material", "software_platform"}:
            return "uses"
        if tgt.type == "dataset":
            return "sources_from"
        if tgt.type == "benchmark":
            return "evaluates_on"
        if tgt.type in {"method", "concept", "algorithm", "formalism", "foundation", "equation"}:
            return "is_based_on"
    if src.type == "robot_system":
        if tgt.type in {"component", "technology", "software_platform", "material"}:
            return "integrates"
    if src.type == "component":
        if tgt.type == "component":
            # Two distinct components that mention each other are usually alternatives
            # or part of the same design space; avoid guessing "integrates".
            return "is_alternative_to"
        if tgt.type in {"technology", "software_platform"}:
            return "uses"
        if tgt.type == "material":
            return "requires"
    if src.type == "technology" and tgt.type in {"component", "material"}:
        return "enables"
    if src.type == "material" and tgt.type in {"component", "technology"}:
        return "enables"
    if src.type in {"benchmark", "report"} and tgt.type == "paper":
        return "cites"
    if src.type == "benchmark" and tgt.type == "dataset":
        return "evaluates_on"
    return ""


def heuristic_backfill(
    entities: list[Entity],
    existing: dict[tuple[str, str, str], dict[str, Any]],
    dry_run: bool,
) -> dict[tuple[str, str, str], dict[str, Any]]:
    """Create relationships when one entity's summary explicitly mentions another.

    Only links supported by a direct textual mention are kept, which keeps the
    heuristic precise enough to write to the repository without manual review.
    """
    added: dict[tuple[str, str, str], dict[str, Any]] = {}

    for src in entities:
        candidates = _candidate_targets(src, entities, set(existing.keys()) | set(added.keys()), top_k=50)
        created_for_source = 0
        for tgt, score in candidates:
            if created_for_source >= 4:
                break
            # Require an explicit mention in the source summary.
            # For organisations, require the target's actual name to appear; otherwise
            # generic shared tags (e.g. "dynamixel") create false product links.
            if src.type in {"oem", "component_manufacturer", "tier1_supplier", "tier2_supplier", "software_vendor", "material_supplier", "research_institution", "standards_body", "industry_consortium"}:
                mention_ok = _name_mentions(src.summary_en, tgt)
            elif src.type == "component" and tgt.type == "component":
                mention_ok = _name_mentions(src.summary_en, tgt)
            else:
                mention_ok = _mentions(src.summary_en, tgt)
            if not mention_ok:
                continue

            rel_type = _relation_type_for_pair(src, tgt)
            if not rel_type:
                continue
            rel_type = _normalize_rel_type(rel_type)
            if not rel_type:
                continue

            key = (src.id, rel_type, tgt.id)
            if key in existing or key in added:
                continue

            # Build a short, specific description.
            description = f"{src.name_en} is related to {tgt.name_en} through {rel_type}."
            if rel_type == "integrates":
                description = f"{src.name_en} integrates {tgt.name_en}."
            elif rel_type == "uses":
                description = f"{src.name_en} uses or builds on {tgt.name_en}."
            elif rel_type == "produces":
                description = f"{src.name_en} produces or develops {tgt.name_en}."
            elif rel_type == "supplies":
                description = f"{src.name_en} supplies {tgt.name_en}."
            elif rel_type == "requires":
                description = f"{src.name_en} requires {tgt.name_en}."
            elif rel_type == "enables":
                description = f"{tgt.name_en} enables or supports {src.name_en}."
            elif rel_type == "evaluates_on":
                description = f"{src.name_en} evaluates or benchmarks {tgt.name_en}."
            elif rel_type == "sources_from":
                description = f"{src.name_en} sources data from or uses {tgt.name_en}."
            elif rel_type == "cites":
                description = f"{src.name_en} cites or references {tgt.name_en}."
            elif rel_type == "is_based_on":
                description = f"{src.name_en} is based on or uses {tgt.name_en}."
            elif rel_type == "serves":
                description = f"{src.name_en} serves the {tgt.name_en} application or market."

            confidence = "medium" if score >= 18 else "low"
            fm = _build_relationship_frontmatter(
                src, tgt, rel_type, description, confidence, _sources_from_entity(src)
            )
            added[key] = fm
            created_for_source += 1
            if dry_run:
                print(f"[heuristic dry-run] {src.id} --{rel_type}--> {tgt.id} (score={score})")

    return added


def _llm_prompt(src: Entity, candidates: list[tuple[Entity, int]]) -> str:
    """Build a prompt asking the LLM to propose relationships for a source."""
    lines = [
        "You are a knowledge-graph curator for an encyclopedia of humanoid robots.",
        "Given the SOURCE entity below and a list of CANDIDATE target entities, decide which direct, meaningful relationships should exist.",
        "Base your answer only on the provided names, summaries, domains, and tags. Do not invent external facts.",
        "",
        "Allowed relationship types: " + ", ".join(sorted(ALLOWED_REL_TYPES)),
        "",
        "Return a JSON object exactly in this form:",
        '{"relationships": [{"target_id": "...", "type": "...", "description": "one concise sentence", "confidence": "high|medium|low"}]}',
        "If no relationship is clearly supported, return {\"relationships\": []}.",
        "",
        "=== SOURCE ===",
        f"id: {src.id}",
        f"type: {src.type}",
        f"name (en): {src.name_en}",
        f"domains: {sorted(src.domains)}",
        f"tags: {sorted(src.tags)}",
        f"summary (en): {src.summary_en[:800]}",
        "",
        "=== CANDIDATES ===",
    ]
    for idx, (tgt, score) in enumerate(candidates, 1):
        lines.append(
            f"{idx}. id={tgt.id} type={tgt.type} name={tgt.name_en} "
            f"domains={sorted(tgt.domains)} tags={sorted(tgt.tags)} "
            f"summary={tgt.summary_en[:400]}"
        )
    return "\n".join(lines)


def llm_backfill(
    entities: list[Entity],
    existing: dict[tuple[str, str, str], dict[str, Any]],
    added_heuristic: dict[tuple[str, str, str], dict[str, Any]],
    dry_run: bool,
    limit_sources: int | None,
    min_target_relationships: int = 2,
    model: str | None = None,
) -> dict[tuple[str, str, str], dict[str, Any]]:
    """Ask an LLM to propose relationships for entities still lacking enough links."""
    added: dict[tuple[str, str, str], dict[str, Any]] = {}
    existing_keys = set(existing.keys()) | set(added_heuristic.keys()) | set(added.keys())

    # Count current outgoing + incoming relationships per entity.
    rel_counts: dict[str, int] = {e.id: 0 for e in entities}
    for s, _, t in existing_keys:
        rel_counts[s] = rel_counts.get(s, 0) + 1
        rel_counts[t] = rel_counts.get(t, 0) + 1

    # Sort by ascending relationship count so under-connected entities go first.
    sources = sorted(entities, key=lambda e: (rel_counts.get(e.id, 0), e.id))
    if limit_sources:
        sources = sources[:limit_sources]

    total = len(sources)
    for i, src in enumerate(sources, 1):
        if rel_counts.get(src.id, 0) >= min_target_relationships:
            continue
        candidates = _candidate_targets(
            src, entities, existing_keys | set(added.keys()), top_k=15
        )
        if not candidates:
            continue

        prompt = _llm_prompt(src, candidates)
        if dry_run:
            print(f"[llm dry-run] ({i}/{total}) prompt for {src.id} ({len(candidates)} candidates)")
            continue

        try:
            result = llm_client.chat_completion_json(
                messages=[{"role": "user", "content": prompt}],
                model=model,
                temperature=0.2,
                max_tokens=2048,
            )
            proposals = result.get("relationships", []) if isinstance(result, dict) else []
        except Exception as exc:
            print(f"[llm_backfill] LLM failed for {src.id}: {exc}")
            continue

        accepted = 0
        for proposal in proposals:
            tgt_id = proposal.get("target_id") or proposal.get("target", {}).get("id")
            rel_type = _normalize_rel_type(proposal.get("type", ""))
            description = proposal.get("description", "")
            confidence = (proposal.get("confidence", "low") or "low").lower()
            if not tgt_id or not rel_type or not description:
                continue
            if confidence not in {"high", "medium", "low"}:
                confidence = "low"
            if confidence == "low":
                continue
            tgt = next((e for e in entities if e.id == tgt_id), None)
            if not tgt or tgt.id == src.id:
                continue
            key = (src.id, rel_type, tgt.id)
            if key in existing_keys or key in added:
                continue
            fm = _build_relationship_frontmatter(
                src, tgt, rel_type, description, confidence, _sources_from_entity(src)
            )
            added[key] = fm
            accepted += 1
            rel_counts[src.id] = rel_counts.get(src.id, 0) + 1
            rel_counts[tgt.id] = rel_counts.get(tgt.id, 0) + 1

        print(f"[llm_backfill] ({i}/{total}) {src.id}: accepted {accepted} proposals")

    return added


def write_relationships(relations: dict[tuple[str, str, str], dict[str, Any]]) -> list[Path]:
    """Write relationship frontmatter files to disk."""
    RELATIONSHIPS_DIR.mkdir(parents=True, exist_ok=True)
    paths: list[Path] = []
    for fm in relations.values():
        path = entry_builder.write_relationship_file(fm, base_dir=RELATIONSHIPS_DIR)
        paths.append(path)
    return paths


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Backfill relationships among existing entities.")
    parser.add_argument("--dry-run", action="store_true", help="Print proposed relationships without writing files.")
    parser.add_argument("--heuristic-only", action="store_true", help="Run only the heuristic pass.")
    parser.add_argument("--llm-only", action="store_true", help="Run only the LLM pass.")
    parser.add_argument("--limit-sources", type=int, default=None, help="Limit LLM pass to N most under-connected sources.")
    parser.add_argument("--model", type=str, default=None, help="LLM model override.")
    parser.add_argument("--min-target-relationships", type=int, default=2, help="Skip LLM review for entities already having this many relationships.")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    entities = load_entities()
    if not entities:
        print("No production entities found.")
        return 1

    existing = load_existing_relationships()
    print(f"Loaded {len(entities)} entities and {len(existing)} existing relationships.")

    added: dict[tuple[str, str, str], dict[str, Any]] = {}

    if not args.llm_only:
        heuristic_added = heuristic_backfill(entities, existing, args.dry_run)
        print(f"Heuristic pass proposed {len(heuristic_added)} relationships.")
        added.update(heuristic_added)

    if not args.heuristic_only:
        llm_added = llm_backfill(
            entities,
            existing,
            added if not args.dry_run else {},
            args.dry_run,
            args.limit_sources,
            args.min_target_relationships,
            args.model,
        )
        print(f"LLM pass proposed {len(llm_added)} relationships.")
        added.update(llm_added)

    if not args.dry_run:
        paths = write_relationships(added)
        print(f"Wrote {len(paths)} new relationship files to {RELATIONSHIPS_DIR}.")

    print(f"Total new relationships: {len(added)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
