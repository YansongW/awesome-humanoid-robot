#!/usr/bin/env python3
"""
Automatically propose cross-layer and engineering relationships for production entities.

This script identifies system-level entities that lack outgoing cross-layer links,
selects candidate target entities at deeper theoretical depths, and uses an LLM to
propose semantically meaningful relationships. Proposals are written to the staging
area for human review.

Usage:
    source .venv/bin/activate
    python scripts/backfill_cross_layer_relationships.py --dry-run
    python scripts/backfill_cross_layer_relationships.py --max-per-entity 3 --max-total 50
"""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from datetime import datetime
from pathlib import Path
from typing import Any

import yaml

sys.path.insert(0, str(Path(__file__).parent))
from ai4sci_lib import config, llm_client


ROOT = Path(__file__).parent.parent
SCHEMA_DIR = ROOT / "data" / "schema" / "v1"
RELATIONSHIP_SCHEMA_PATH = SCHEMA_DIR / "relationship_schema.json"

# Allowed relationship types that are acceptable across any layer (generic).
GENERIC_REL_TYPES = {
    "cites",
    "verified_by",
    "conflicts_with",
    "is_version_of",
    "is_alternative_to",
    "competes_with",
    "is_substitute_for",
    "proposes",
    "evaluates_on",
    "uses",
    "is_based_on",
}

CROSS_LAYER_ALLOWED = config.CROSS_LAYER_RELATIONSHIPS


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Propose cross-layer relationships using an LLM and stage them for review."
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print proposals without writing files.",
    )
    parser.add_argument(
        "--max-per-entity",
        type=int,
        default=3,
        help="Maximum relationships to propose per source entity (default: 3).",
    )
    parser.add_argument(
        "--max-total",
        type=int,
        default=50,
        help="Maximum total relationships to propose (default: 50).",
    )
    parser.add_argument(
        "--min-confidence",
        choices=["high", "medium", "low"],
        default="medium",
        help="Minimum confidence to keep a proposal (default: medium).",
    )
    parser.add_argument(
        "--max-candidates",
        type=int,
        default=30,
        help="Maximum candidate targets to send to the LLM per source entity (default: 30).",
    )
    parser.add_argument(
        "--model",
        default=None,
        help="LLM model override.",
    )
    parser.add_argument(
        "--use-cache",
        action="store_true",
        default=True,
        help="Reuse cached LLM responses when available (default: True).",
    )
    parser.add_argument(
        "--clear-cache",
        action="store_true",
        help="Clear the proposal cache before running.",
    )
    return parser.parse_args()


def load_yaml_frontmatter(path: Path) -> dict[str, Any]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---"):
        raise ValueError(f"No frontmatter in {path}")
    _, rest = text.split("---", 1)
    yaml_text, _ = rest.split("---", 1)
    return yaml.safe_load(yaml_text)


def save_yaml_frontmatter(path: Path, data: dict[str, Any], body: str = "") -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    yaml_text = yaml.dump(data, sort_keys=False, allow_unicode=True, default_flow_style=False)
    path.write_text(f"---\n{yaml_text}---\n{body}", encoding="utf-8")


def build_entity_lookup() -> dict[str, dict[str, Any]]:
    lookup: dict[str, dict[str, Any]] = {}
    for path in config.RESEARCH_DIR.rglob("*.md"):
        try:
            data = load_yaml_frontmatter(path)
        except Exception:
            continue
        eid = data.get("$id")
        if not eid:
            continue
        lookup[eid] = {
            "path": path,
            "type": data.get("type", "paper"),
            "names": data.get("names", {}),
            "summary": data.get("summary", {}),
            "tags": set(data.get("tags", []) or []),
            "domains": data.get("domains", []),
            "layers": data.get("layers", []),
            "theoretical_depth": data.get("theoretical_depth", []),
            "sources": data.get("sources", []),
        }
    return lookup


def depth_for(entity: dict[str, Any]) -> str:
    depths = entity.get("theoretical_depth", [])
    for d in config.THEORETICAL_DEPTH_ORDER:
        if d in depths:
            return d
    # Fallback inference from type.
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


def load_existing_relationships() -> set[tuple[str, str]]:
    pairs: set[tuple[str, str]] = set()
    dirs = [config.RELATIONSHIPS_DIR]
    if config.STAGING_RELATIONSHIPS_DIR.exists():
        dirs.append(config.STAGING_RELATIONSHIPS_DIR)
    for directory in dirs:
        if not directory.exists():
            continue
        for path in directory.rglob("*.md"):
            try:
                data = load_yaml_frontmatter(path)
            except Exception:
                continue
            src = data.get("source", {}).get("id")
            tgt = data.get("target", {}).get("id")
            if src and tgt:
                pairs.add((src, tgt))
    return pairs


def candidate_targets_for(
    source: dict[str, Any],
    lookup: dict[str, dict[str, Any]],
    existing: set[tuple[str, str]],
    max_candidates: int,
) -> list[dict[str, Any]]:
    """Return the most relevant candidate targets for a source entity."""
    source_depth = depth_for(source)
    source_tags = source.get("tags", set())
    candidates: list[tuple[int, dict[str, Any]]] = []
    for eid, entity in lookup.items():
        if eid == source.get("_id"):
            continue
        if (source.get("_id"), eid) in existing:
            continue
        target_depth = depth_for(entity)
        # We are looking for cross-layer (different depth) or engineering links to components/materials.
        if source_depth == target_depth:
            continue
        # Only propose links to deeper abstractions or well-defined engineering targets.
        if target_depth not in {"method", "formalism", "principle", "foundation"}:
            # Allow component/material targets from system-level sources as engineering links.
            if entity.get("type") not in {"component", "material", "algorithm"}:
                continue
        score = len(source_tags & entity.get("tags", set()))
        # Boost candidates when domains overlap.
        if set(source.get("domains", [])) & set(entity.get("domains", [])):
            score += 1
        candidates.append((score, entity))

    candidates.sort(key=lambda x: x[0], reverse=True)
    return [entity for _, entity in candidates[:max_candidates]]


def cache_path() -> Path:
    cache_dir = config.STAGING_DIR / "backfill"
    cache_dir.mkdir(parents=True, exist_ok=True)
    return cache_dir / "cache.jsonl"


def cache_key(source_id: str, candidate_ids: list[str]) -> str:
    payload = json.dumps({"source": source_id, "candidates": sorted(candidate_ids)}, sort_keys=True)
    return hashlib.sha256(payload.encode()).hexdigest()


def load_cache() -> dict[str, dict[str, Any]]:
    cache: dict[str, dict[str, Any]] = {}
    path = cache_path()
    if not path.exists():
        return cache
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            obj = json.loads(line)
            cache[obj["key"]] = obj
        except Exception:
            continue
    return cache


def save_cache(cache: dict[str, dict[str, Any]]) -> None:
    path = cache_path()
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as f:
        for obj in cache.values():
            f.write(json.dumps(obj, ensure_ascii=False) + "\n")


def build_llm_prompt(
    source: dict[str, Any],
    candidates: list[dict[str, Any]],
    max_per_entity: int,
) -> str:
    source_id = source.get("_id")
    source_depth = depth_for(source)
    source_name = source.get("names", {}).get("en", source_id)
    source_summary = source.get("summary", {}).get("en", "")
    source_tags = sorted(source.get("tags", set()))

    lines = [
        "You are a knowledge-graph curator for humanoid robotics.",
        "Given a source entity and a list of candidate target entities, propose meaningful cross-layer or engineering relationships.",
        "",
        "Source entity:",
        f"  id: {source_id}",
        f"  type: {source.get('type')}",
        f"  theoretical_depth: {source_depth}",
        f"  name (en): {source_name}",
        f"  summary (en): {source_summary}",
        f"  tags: {', '.join(source_tags)}",
        "",
        "Candidate target entities (each with id, type, depth, name, summary, tags):",
    ]
    for entity in candidates:
        eid = entity.get("_id")
        lines.append(f"- id: {eid}")
        lines.append(f"  type: {entity.get('type')}")
        lines.append(f"  theoretical_depth: {depth_for(entity)}")
        lines.append(f"  name (en): {entity.get('names', {}).get('en', eid)}")
        lines.append(f"  summary (en): {entity.get('summary', {}).get('en', '')}")
        lines.append(f"  tags: {', '.join(sorted(entity.get('tags', set())))}")
        lines.append("")

    lines.extend([
        "",
        f"Propose up to {max_per_entity} relationships from the source to candidate targets.",
        "Each relationship must be cross-layer or engineering-relevant (source depth != target depth).",
        "Choose relationship types only from the following schema enum: "
        "uses, is_based_on, formalizes, includes, derived_from, has_prerequisite, instantiates, "
        "integrates, requires, enables, produces, constrains, is_part_of, is_subsystem_of, consumes.",
        "",
        "Return strictly JSON in this format (no markdown, no commentary):",
        '{"relationships": [{"target_id": "...", "type": "...", "confidence": "high|medium|low", "description_en": "...", "description_zh": "...", "description_ko": "...", "justification": "..."}]}',
        "Only include relationships you are genuinely confident about. If none apply, return an empty list.",
    ])
    return "\n".join(lines)


def is_allowed(rel_type: str, source_depth: str, target_depth: str) -> bool:
    if source_depth == target_depth:
        return rel_type in config.CROSS_LAYER_RELATIONSHIPS.get((source_depth, source_depth), [])
    allowed = config.CROSS_LAYER_RELATIONSHIPS.get((source_depth, target_depth), [])
    if rel_type in allowed or rel_type in GENERIC_REL_TYPES:
        return True
    return False


def propose_for_source(
    source: dict[str, Any],
    candidates: list[dict[str, Any]],
    args: argparse.Namespace,
    cache: dict[str, dict[str, Any]],
) -> list[dict[str, Any]]:
    candidate_ids = [e.get("_id") for e in candidates]
    key = cache_key(source.get("_id"), candidate_ids)
    source_depth = depth_for(source)

    cached = cache.get(key) if args.use_cache else None
    if cached and "result" in cached:
        result = cached["result"]
    else:
        prompt = build_llm_prompt(source, candidates, args.max_per_entity)
        messages = [
            {"role": "system", "content": "You are a precise knowledge-graph assistant. Return only JSON."},
            {"role": "user", "content": prompt},
        ]
        try:
            result = llm_client.chat_completion_json(
                messages,
                model=args.model,
                temperature=0.1,
                max_tokens=4096,
            )
        except Exception as exc:
            print(f"[warn] LLM call failed for {source.get('_id')}: {exc}", file=sys.stderr)
            return []
        cache[key] = {"key": key, "source": source.get("_id"), "result": result, "timestamp": datetime.utcnow().isoformat()}

    proposals = result.get("relationships", []) if isinstance(result, dict) else []
    accepted: list[dict[str, Any]] = []
    lookup = {e.get("_id"): e for e in candidates}
    for prop in proposals:
        target_id = prop.get("target_id")
        rel_type = prop.get("type")
        confidence = prop.get("confidence", "low")
        if target_id not in lookup:
            continue
        target = lookup[target_id]
        target_depth = depth_for(target)
        if not is_allowed(rel_type, source_depth, target_depth):
            print(
                f"[skip] {source.get('_id')} -> {rel_type} -> {target_id} "
                f"not allowed for {source_depth} -> {target_depth}",
                file=sys.stderr,
            )
            continue
        if confidence == "low" and args.min_confidence in ("high", "medium"):
            continue
        if confidence == "medium" and args.min_confidence == "high":
            continue
        accepted.append({
            "source": source,
            "target": target,
            "type": rel_type,
            "confidence": confidence,
            "description_en": prop.get("description_en", ""),
            "description_zh": prop.get("description_zh", ""),
            "description_ko": prop.get("description_ko", ""),
            "justification": prop.get("justification", ""),
        })
    return accepted


def relationship_exists(source_id: str, rel_type: str, target_id: str) -> bool:
    rel_id = f"rel_{source_id}_{rel_type}_{target_id}.md"
    return (config.RELATIONSHIPS_DIR / rel_id).exists() or (config.STAGING_RELATIONSHIPS_DIR / rel_id).exists()


def write_relationship(proposal: dict[str, Any], dry_run: bool) -> Path | None:
    source = proposal["source"]
    target = proposal["target"]
    source_id = source.get("_id")
    target_id = target.get("_id")
    rel_type = proposal["type"]
    rel_id = f"rel_{source_id}_{rel_type}_{target_id}"

    if relationship_exists(source_id, rel_type, target_id):
        return None

    source_name_en = source.get("names", {}).get("en", source_id)
    target_name_en = target.get("names", {}).get("en", target_id)
    source_domain = source.get("domains", ["00_foundations"])[0]
    target_domain = target.get("domains", ["00_foundations"])[0]

    # Derive a source citation from the source entity's first source.
    src_sources = source.get("sources", [])
    rel_sources = []
    if src_sources:
        rel_sources.append({
            "id": f"src_backfill_{src_sources[0].get('id', 'unknown')}",
            "type": src_sources[0].get("type", "paper"),
            "title": src_sources[0].get("title", ""),
            "url": src_sources[0].get("url", ""),
            "date": src_sources[0].get("date", ""),
            "accessed_at": datetime.now().date().isoformat(),
        })
    else:
        rel_sources.append({
            "id": "src_backfill_generic",
            "type": "other",
            "title": "AI-proposed cross-layer backfill",
            "url": "",
            "date": datetime.now().date().isoformat(),
            "accessed_at": datetime.now().date().isoformat(),
        })

    data = {
        "$id": rel_id,
        "$schema": "../schema/v1/relationship_schema.json",
        "$version": 1,
        "type": rel_type,
        "source": {"id": source_id, "name": {"en": source_name_en}},
        "target": {"id": target_id, "name": {"en": target_name_en}},
        "domains": {"source_domain": source_domain, "target_domain": target_domain},
        "description": {
            "en": proposal["description_en"] or f"{source_id} {rel_type} {target_id}",
            "zh": proposal["description_zh"] or f"{source_id} {rel_type} {target_id}",
            "ko": proposal["description_ko"] or f"{source_id} {rel_type} {target_id}",
        },
        "verification": {
            "status": "speculative",
            "reviewed_by": "ai",
            "reviewed_at": datetime.now().date().isoformat(),
            "confidence": proposal["confidence"],
            "notes": f"AI-proposed backfill. Justification: {proposal.get('justification', '')}",
        },
        "sources": rel_sources,
    }

    dest = config.STAGING_RELATIONSHIPS_DIR / f"{rel_id}.md"
    if dry_run:
        print(f"[dry-run] would write {dest}")
        return dest
    dest.parent.mkdir(parents=True, exist_ok=True)
    save_yaml_frontmatter(dest, data)
    return dest


def main() -> int:
    args = parse_args()

    if args.clear_cache:
        cache_path().unlink(missing_ok=True)
        print("[info] Cleared backfill cache.")

    lookup = build_entity_lookup()
    for eid, entity in lookup.items():
        entity["_id"] = eid

    existing_pairs = load_existing_relationships()
    cache = load_cache()

    # Count existing cross-layer outgoing relationships per source entity.
    cross_layer_count: dict[str, int] = {}
    for src_id, tgt_id in existing_pairs:
        tgt = lookup.get(tgt_id)
        if not tgt:
            continue
        if depth_for(lookup.get(src_id, {})) != depth_for(tgt):
            cross_layer_count[src_id] = cross_layer_count.get(src_id, 0) + 1

    # Seed entities: all system-level entries, prioritized by fewest cross-layer outgoing links.
    seeds = [
        entity for entity in lookup.values()
        if depth_for(entity) == "system"
    ]
    seeds.sort(key=lambda e: cross_layer_count.get(e.get("_id"), 0))

    print(
        f"[info] Found {len(seeds)} system-level seed entities; "
        f"prioritizing those with the fewest cross-layer outgoing relationships."
    )

    total_written = 0
    total_skipped_existing = 0
    for source in seeds:
        if total_written >= args.max_total:
            break
        candidates = candidate_targets_for(source, lookup, existing_pairs, args.max_candidates)
        if not candidates:
            continue
        proposals = propose_for_source(source, candidates, args, cache)
        for proposal in proposals:
            if total_written >= args.max_total:
                break
            src_id = proposal["source"].get("_id")
            tgt_id = proposal["target"].get("_id")
            if (src_id, tgt_id) in existing_pairs:
                total_skipped_existing += 1
                continue
            dest = write_relationship(proposal, args.dry_run)
            if dest:
                total_written += 1
                existing_pairs.add((src_id, tgt_id))
                print(f"[proposed] {src_id} --{proposal['type']}--> {tgt_id} ({proposal['confidence']})")

    if args.use_cache:
        save_cache(cache)

    print(f"\nSummary:")
    print(f"  Seeds considered: {len(seeds)}")
    print(f"  Proposals written: {total_written}")
    print(f"  Skipped (already exists): {total_skipped_existing}")
    if args.dry_run:
        print("  This was a dry run; no files were written.")
    else:
        print(f"  Staged relationships are ready for review in {config.STAGING_RELATIONSHIPS_DIR}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
