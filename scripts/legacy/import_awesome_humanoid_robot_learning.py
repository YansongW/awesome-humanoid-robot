#!/usr/bin/env python3
"""Import the Awesome-Humanoid-Robot-Learning GitHub list into the knowledge graph.

Source: https://github.com/YanjieZe/awesome-humanoid-robot-learning
Usage:
    python scripts/import_awesome_humanoid_robot_learning.py --dry-run
    python scripts/import_awesome_humanoid_robot_learning.py
"""

from __future__ import annotations

import argparse
import json
import re
from datetime import date
from pathlib import Path
from typing import Any

import yaml

from ai4sci_lib import config, entry_builder


ROOT = config.ROOT
RESEARCH_DIR = config.RESEARCH_DIR
CURATED_PATH = ROOT / "data" / "curated" / "awesome_humanoid_robot_learning.json"

CATEGORY_MAP: dict[str, dict[str, Any]] = {
    "Loco-Manipulation and Whole-Body-Control": {
        "domains": ["07_ai_models_algorithms", "08_software_middleware"],
        "tags": ["humanoid", "loco_manipulation", "whole_body_control"],
    },
    "Manipulation": {
        "domains": ["07_ai_models_algorithms", "08_software_middleware"],
        "tags": ["humanoid", "manipulation"],
    },
    "Teleoperation": {
        "domains": ["07_ai_models_algorithms", "08_software_middleware"],
        "tags": ["humanoid", "teleoperation"],
    },
    "Locomotion": {
        "domains": ["07_ai_models_algorithms"],
        "tags": ["humanoid", "locomotion"],
    },
    "Navigation": {
        "domains": ["07_ai_models_algorithms", "08_software_middleware"],
        "tags": ["humanoid", "navigation"],
    },
    "State Estimation": {
        "domains": ["07_ai_models_algorithms", "08_software_middleware"],
        "tags": ["humanoid", "state_estimation", "slam"],
    },
    "Sim-to-Real": {
        "domains": ["07_ai_models_algorithms", "08_software_middleware"],
        "tags": ["humanoid", "sim_to_real"],
    },
    "Hardware Design": {
        "domains": ["06_design_engineering", "02_components"],
        "tags": ["humanoid", "hardware_design"],
    },
    "Simulation Benchmark": {
        "domains": ["07_ai_models_algorithms", "08_software_middleware", "10_evaluation_benchmarks"],
        "tags": ["humanoid", "simulation", "benchmark"],
    },
    "Physics-Based Character Animation": {
        "domains": ["07_ai_models_algorithms"],
        "tags": ["humanoid", "character_animation", "physics_based"],
    },
    "Human Motion Analysis and Synthesis": {
        "domains": ["07_ai_models_algorithms", "09_data_datasets"],
        "tags": ["humanoid", "motion_analysis", "motion_synthesis"],
    },
}


def load_existing_titles() -> set[str]:
    titles: set[str] = set()
    for path in RESEARCH_DIR.rglob("*.md"):
        try:
            text = path.read_text(encoding="utf-8")
            if not text.startswith("---"):
                continue
            _, rest = text.split("---", 1)
            yaml_text, _ = rest.split("---", 1)
            data = yaml.safe_load(yaml_text) or {}
            names = data.get("names", {})
            if isinstance(names, dict):
                titles.add(names.get("en", "").strip().lower())
                titles.add(names.get("zh", "").strip().lower())
        except Exception:
            continue
    return titles


def _extract_arxiv_id(url: str) -> str:
    if not url:
        return ""
    m = re.search(r"arxiv\.org/abs/(\d+\.\d+)", url)
    if m:
        return m.group(1)
    return ""


def _make_summary(paper: dict[str, Any]) -> str:
    title = paper.get("title", "").strip()
    year = paper.get("year", "")
    category = paper.get("category", "")
    parts = [f"{title} is a {year} work on {category.lower()} for humanoid robots"]
    if paper.get("code_url"):
        parts.append("with open-source code available")
    return ", ".join(parts) + "."


def build_entry(
    paper: dict[str, Any],
    existing_titles: set[str],
    existing_ids: set[str],
) -> dict[str, Any] | None:
    title = paper.get("title", "").strip()
    if not title:
        return None
    if title.lower() in existing_titles:
        print(f"[skip duplicate] {title}")
        return None

    year = str(paper.get("year", date.today().year))
    title_slug = entry_builder._slugify(title, max_len=30)
    ent_id = f"ent_paper_{title_slug}_{year}"
    candidate_id = ent_id
    counter = 1
    while candidate_id in existing_ids:
        candidate_id = f"{ent_id}_{counter}"
        counter += 1
    ent_id = candidate_id
    existing_ids.add(ent_id)

    names = {
        "en": title,
        "zh": title,
        "ko": "",
    }

    summary_text = _make_summary(paper)
    summary = {"en": summary_text, "zh": summary_text, "ko": ""}

    category = paper.get("category", "")
    cat_info = CATEGORY_MAP.get(category, {})
    domains = cat_info.get("domains", ["07_ai_models_algorithms"])
    base_tags: set[str] = set(cat_info.get("tags", ["humanoid"]))
    base_tags.add(entry_builder._slugify(title.split(":")[0], max_len=30))
    tags = sorted(t for t in base_tags if t)

    arxiv_url = paper.get("arxiv_url", "")
    arxiv_id = _extract_arxiv_id(arxiv_url)
    website_url = paper.get("website_url", "")
    source_url = paper.get("source_url", "")
    today = str(date.today())
    sources: list[dict[str, Any]] = []

    if arxiv_id:
        sources.append({
            "id": "src_001",
            "type": "paper",
            "title": f"{title} (arXiv)",
            "url": arxiv_url,
            "date": year,
            "accessed_at": today,
        })

    project_url = website_url or (source_url if not arxiv_id else "")
    if project_url and project_url != arxiv_url:
        src_id = "src_002" if arxiv_id else "src_001"
        sources.append({
            "id": src_id,
            "type": "website",
            "title": f"{title} project page",
            "url": project_url,
            "date": year,
            "accessed_at": today,
        })

    if not sources:
        sources.append({
            "id": "src_001",
            "type": "website",
            "title": title,
            "url": "",
            "date": year,
            "accessed_at": today,
        })

    notes_parts = [
        "Imported from Awesome-Humanoid-Robot-Learning curated list.",
    ]
    if category:
        notes_parts.append(f"Category: {category}.")
    if arxiv_id:
        notes_parts.append(f"arXiv: {arxiv_id}.")
    notes = " ".join(notes_parts)

    status = "partially_verified" if (arxiv_id or project_url) else "unverified"
    confidence = "medium" if (arxiv_id or project_url) else "low"

    functional_roles = ["knowledge", "intelligence"]
    if "Hardware Design" in category:
        functional_roles.append("system")

    return {
        "$id": ent_id,
        "$schema": "../../data/schema/v1/entry_schema.json",
        "$version": 1,
        "type": "paper",
        "names": names,
        "summary": summary,
        "domains": domains,
        "layers": ["intelligence"],
        "functional_roles": functional_roles,
        "tags": tags,
        "theoretical_depth": ["system"],
        "verification": {
            "status": status,
            "reviewed_by": "ai",
            "reviewed_at": today,
            "confidence": confidence,
            "notes": notes,
        },
        "sources": sources,
    }


def write_entry(frontmatter: dict[str, Any]) -> Path:
    subdir = "papers"
    filename = f"{frontmatter['$id']}.md"
    body = frontmatter["summary"]["en"] or ""
    return entry_builder.write_entry_file(frontmatter, body, subdir, filename)


def main() -> int:
    parser = argparse.ArgumentParser(description="Import Awesome-Humanoid-Robot-Learning papers into the graph.")
    parser.add_argument("--dry-run", action="store_true", help="Count and preview without writing files.")
    args = parser.parse_args()

    if not CURATED_PATH.exists():
        print(f"Curated data not found: {CURATED_PATH}")
        return 1

    data = json.loads(CURATED_PATH.read_text(encoding="utf-8"))
    papers = data.get("papers", [])
    existing_titles = load_existing_titles()
    existing_ids = entry_builder.load_existing_ids()
    print(f"Loaded {len(papers)} papers from Awesome-Humanoid-Robot-Learning list.")
    print(f"Existing titles in graph: {len(existing_titles)}")
    print(f"Existing IDs in graph: {len(existing_ids)}")

    added = 0
    skipped = 0
    for paper in papers:
        fm = build_entry(paper, existing_titles, existing_ids)
        if fm is None:
            skipped += 1
            continue
        if args.dry_run:
            print(f"[dry-run] {fm['$id']}: {fm['names']['en'][:80]}")
        else:
            path = write_entry(fm)
            print(f"[wrote] {path.name}")
        added += 1

    print(f"\nTotal: {len(papers)} | Added: {added} | Skipped duplicates: {skipped}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
