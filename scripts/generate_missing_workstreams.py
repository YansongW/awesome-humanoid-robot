#!/usr/bin/env python3
"""Generate stub workstream YAMLs for all unchecked leaves in WORKSTREAM_TREE.md.

Usage:
    source .venv/bin/activate
    python scripts/generate_missing_workstreams.py \
        --tree docs/ai4sci/WORKSTREAM_TREE.md \
        --out-dir scripts/ai4sci_workstreams \
        --priority-domains 03_manufacturing_processes 04_assembly_integration_testing \
                           05_mass_production 12_policy_regulation_ethics 01_raw_materials

The script:
1. Parses WORKSTREAM_TREE.md for `- [ ] path/to/workstream.yaml` entries.
2. Skips leaves that already have a YAML on disk.
3. Creates a stub YAML with taxonomy-derived name, domains, and seed queries.
4. Optionally prioritizes specific ontology domains by setting `priority: 1`.
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path
from typing import Any

import yaml

from ai4sci_lib import config


# Map a workstream file path to a sensible default domain list.
DOMAIN_HINTS: dict[str, list[str]] = {
    "01_raw_materials": ["01_raw_materials"],
    "02_components": ["02_components", "06_design_engineering"],
    "03_manufacturing_processes": ["03_manufacturing_processes", "05_mass_production"],
    "04_assembly_integration_testing": ["04_assembly_integration_testing", "06_design_engineering"],
    "05_mass_production": ["05_mass_production", "03_manufacturing_processes"],
    "06_design_engineering": ["06_design_engineering", "02_components"],
    "07_ai_models_algorithms": ["07_ai_models_algorithms", "08_software_middleware"],
    "08_software_middleware": ["08_software_middleware", "07_ai_models_algorithms"],
    "09_data_datasets": ["09_data_datasets", "07_ai_models_algorithms"],
    "10_evaluation_benchmarks": ["10_evaluation_benchmarks", "07_ai_models_algorithms"],
    "11_applications_markets": ["11_applications_markets", "07_ai_models_algorithms"],
    "12_policy_regulation_ethics": ["12_policy_regulation_ethics", "11_applications_markets"],
    "foundations": ["00_foundations", "07_ai_models_algorithms"],
    "cross_domain": ["07_ai_models_algorithms", "06_design_engineering", "05_mass_production"],
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Generate stub workstream YAMLs for unchecked WORKSTREAM_TREE leaves."
    )
    parser.add_argument(
        "--tree",
        type=Path,
        default=config.ROOT / "docs" / "ai4sci" / "WORKSTREAM_TREE.md",
        help="Path to WORKSTREAM_TREE.md.",
    )
    parser.add_argument(
        "--out-dir",
        type=Path,
        default=config.WORKSTREAMS_DIR,
        help="Root directory for workstream YAMLs.",
    )
    parser.add_argument(
        "--priority-domains",
        nargs="+",
        default=[],
        help="Domain codes that should receive priority: 1 instead of 2.",
    )
    parser.add_argument(
        "--yes",
        action="store_true",
        help="Write files without prompting.",
    )
    return parser.parse_args()


def parse_tree_leaves(path: Path) -> list[tuple[str, str]]:
    """Return list of (relative_path, display_name) for unchecked leaves."""
    leaves: list[tuple[str, str]] = []
    with open(path, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            m = re.match(r"-\s*\[\s*\]\s*`([^`]+\.yaml)`", line)
            if not m:
                continue
            rel_path = m.group(1)
            name = Path(rel_path).stem
            leaves.append((rel_path, name))
    return leaves


def infer_domains(rel_path: str) -> list[str]:
    rel_lower = rel_path.lower()
    for hint, domains in DOMAIN_HINTS.items():
        if hint in rel_lower:
            return domains
    return ["07_ai_models_algorithms"]


# Parent-directory tokens that produce awkward query topics.
_TOPIC_OVERRIDES: dict[str, str] = {
    "or ie": "operations research",
}


def build_seed_queries(name: str, rel_path: str) -> tuple[list[str], str]:
    """Generate a broad, domain-aware query set and a relevance context.

    Returns:
        (seed_queries, relevance_context).  The query set mixes general
        robotics/automation terms with one explicitly humanoid query so that
        foundational and sparse domains still surface relevant candidates.
    """
    raw_parts = [
        Path(p).stem
        for p in Path(rel_path).parts
        if p not in ("ai4sci_workstreams", ".")
    ]
    # Drop numeric domain codes like "03_manufacturing_processes".
    raw_parts = [p for p in raw_parts if not re.fullmatch(r"\d+_.*", p)]
    parts = [_TOPIC_OVERRIDES.get(p, p).replace("_", " ") for p in raw_parts]

    if len(parts) >= 2 and parts[0] == "foundations":
        topic = " ".join(parts[1:])
    else:
        topic = " ".join(parts[-2:]) if len(parts) >= 2 else name.replace("_", " ")

    queries = [
        f"{topic} robotics",
        f"humanoid robot {topic}",
        f"{topic} robots survey",
        f"{topic} automation manufacturing",
        f"{topic} applied to humanoid robots",
    ]
    context = (
        f"Relevant if it addresses {topic} in a robotics or automation context, "
        f"or develops foundational methods/principles applicable to humanoid "
        f"robots, even when examples are not explicitly humanoid."
    )
    return queries, context


def build_workstream(rel_path: str, name: str, priority_domains: set[str]) -> dict[str, Any]:
    domains = infer_domains(rel_path)
    priority = 1 if any(d in priority_domains for d in domains) else 2
    seed_queries, relevance_context = build_seed_queries(name, rel_path)
    return {
        "name": name,
        "description": f"Workstream for {name.replace('_', ' ')}. Generated from WORKSTREAM_TREE leaf: {rel_path}.",
        "seed_queries": seed_queries,
        "paper_ids": [],
        "target_entity_types": ["paper", "method", "technology", "component", "formalism"],
        "target_domains": domains,
        "relevance_context": relevance_context,
        "relationship_patterns": [
            "cites", "is_based_on", "uses", "requires", "enables",
            "formalizes", "builds_on", "has_prerequisite", "instantiates",
        ],
        "relevance_threshold": "medium",
        "max_papers": 5,
        "max_results_per_query": 50,
        "max_total": 100,
        "priority": priority,
        "sources": ["arxiv"],
        "metadata": {
            "generated_from": "WORKSTREAM_TREE.md",
            "leaf_path": rel_path,
        },
    }


def main() -> int:
    args = parse_args()
    priority_domains = set(args.priority_domains)
    leaves = parse_tree_leaves(args.tree)

    missing: list[tuple[str, str]] = []
    for rel_path, name in leaves:
        out_path = args.out_dir / rel_path
        if not out_path.exists():
            missing.append((rel_path, name))

    if not missing:
        print("[generate_missing] All WORKSTREAM_TREE leaves already have YAML files.")
        return 0

    print(f"[generate_missing] Found {len(missing)} missing workstream stub(s).")
    priority_count = sum(
        1 for rel_path, name in missing
        if any(d in priority_domains for d in infer_domains(rel_path))
    )
    if priority_count:
        print(f"[generate_missing] {priority_count} stub(s) marked as priority 1.")

    if not args.yes:
        response = input(f"Create {len(missing)} stub YAMLs in {args.out_dir}? [y/N] ")
        if response.lower() not in ("y", "yes"):
            print("Aborted.")
            return 0

    created = 0
    for rel_path, name in missing:
        out_path = args.out_dir / rel_path
        out_path.parent.mkdir(parents=True, exist_ok=True)
        ws = build_workstream(rel_path, name, priority_domains)
        with open(out_path, "w", encoding="utf-8") as f:
            yaml.safe_dump(ws, f, allow_unicode=True, sort_keys=False)
        created += 1
        print(f"[generate_missing] Created {out_path}")

    print(f"\n[generate_missing] Created {created} stub workstream(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
