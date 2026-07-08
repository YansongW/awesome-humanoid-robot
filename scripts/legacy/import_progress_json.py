#!/usr/bin/env python3
"""Import papers from Humanoid_Robot_Learning_Paper_Notebooks/progress.json.

Source: https://github.com/ImChong/Humanoid_Robot_Learning_Paper_Notebooks
Usage:
    python scripts/import_progress_json.py --dry-run
    python scripts/import_progress_json.py
"""

from __future__ import annotations

import argparse
import json
import re
from datetime import date
from pathlib import Path
from typing import Any

import yaml
import requests
import base64

from ai4sci_lib import config, entry_builder


ROOT = config.ROOT
RESEARCH_DIR = config.RESEARCH_DIR
PROGRESS_PATH = ROOT / "data" / "curated" / "humanoid_robot_learning_paper_notebooks_progress.json"

CATEGORY_MAP: dict[str, dict[str, Any]] = {
    "01_Foundational_RL": {
        "domains": ["07_ai_models_algorithms"],
        "tags": ["humanoid", "reinforcement_learning", "foundation"],
    },
    "02_Motion_Retargeting": {
        "domains": ["07_ai_models_algorithms", "09_data_datasets"],
        "tags": ["humanoid", "motion_retargeting"],
    },
    "03_High_Impact_Selection": {
        "domains": ["07_ai_models_algorithms"],
        "tags": ["humanoid", "high_impact"],
    },
    "04_Loco-Manipulation_and_WBC": {
        "domains": ["07_ai_models_algorithms", "08_software_middleware"],
        "tags": ["humanoid", "loco_manipulation", "whole_body_control"],
    },
    "05_Locomotion": {
        "domains": ["07_ai_models_algorithms"],
        "tags": ["humanoid", "locomotion"],
    },
    "06_Manipulation": {
        "domains": ["07_ai_models_algorithms", "08_software_middleware"],
        "tags": ["humanoid", "manipulation"],
    },
    "07_Teleoperation": {
        "domains": ["07_ai_models_algorithms", "08_software_middleware"],
        "tags": ["humanoid", "teleoperation"],
    },
    "08_Navigation": {
        "domains": ["07_ai_models_algorithms", "08_software_middleware"],
        "tags": ["humanoid", "navigation"],
    },
    "09_State_Estimation": {
        "domains": ["07_ai_models_algorithms", "08_software_middleware"],
        "tags": ["humanoid", "state_estimation"],
    },
    "10_Sim-to-Real": {
        "domains": ["07_ai_models_algorithms", "08_software_middleware"],
        "tags": ["humanoid", "sim_to_real"],
    },
    "11_Simulation_Benchmark": {
        "domains": ["07_ai_models_algorithms", "08_software_middleware", "10_evaluation_benchmarks"],
        "tags": ["humanoid", "simulation", "benchmark"],
    },
    "12_Hardware_Design": {
        "domains": ["06_design_engineering", "02_components"],
        "tags": ["humanoid", "hardware_design"],
    },
    "13_Physics-Based_Animation": {
        "domains": ["07_ai_models_algorithms"],
        "tags": ["humanoid", "physics_based", "character_animation"],
    },
    "14_Human_Motion": {
        "domains": ["07_ai_models_algorithms", "09_data_datasets"],
        "tags": ["humanoid", "human_motion", "motion_synthesis"],
    },
}


def load_existing_titles_and_arxiv() -> tuple[set[str], set[str]]:
    titles: set[str] = set()
    arxiv_ids: set[str] = set()
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
            for src in data.get("sources", []):
                url = src.get("url", "")
                m = re.search(r"arxiv\.org/abs/(\d+\.\d+)", str(url))
                if m:
                    arxiv_ids.add(m.group(1))
        except Exception:
            continue
    return titles, arxiv_ids


def _extract_arxiv_id(url: str) -> str:
    if not url:
        return ""
    m = re.search(r"arxiv\.org/abs/(\d+\.\d+)", url)
    return m.group(1) if m else ""


def _extract_year(title: str) -> str:
    m = re.search(r"20\d{2}", title)
    return m.group(0) if m else str(date.today().year)


def build_entry(
    paper: dict[str, Any],
    existing_titles: set[str],
    existing_arxiv: set[str],
    existing_ids: set[str],
) -> dict[str, Any] | None:
    title = paper.get("title", "").strip()
    if not title:
        return None
    title_key = title.lower()
    arxiv_url = paper.get("arxiv", "")
    arxiv_id = _extract_arxiv_id(arxiv_url)

    if title_key in existing_titles:
        print(f"[skip duplicate title] {title}")
        return None
    if arxiv_id and arxiv_id in existing_arxiv:
        print(f"[skip duplicate arxiv] {arxiv_id} - {title}")
        return None

    year = _extract_year(title)
    title_slug = entry_builder._slugify(title, max_len=30)
    ent_id = f"ent_paper_{title_slug}_{year}"
    candidate_id = ent_id
    counter = 1
    while candidate_id in existing_ids:
        candidate_id = f"{ent_id}_{counter}"
        counter += 1
    ent_id = candidate_id
    existing_ids.add(ent_id)
    existing_titles.add(title_key)
    if arxiv_id:
        existing_arxiv.add(arxiv_id)

    title_cn = paper.get("title_cn", "").strip()
    names = {"en": title, "zh": title_cn or title, "ko": ""}

    folder = paper.get("folder", "")
    category_key = folder.split("/")[1] if "/" in folder else ""
    cat_info = CATEGORY_MAP.get(category_key, {})
    domains = cat_info.get("domains", ["07_ai_models_algorithms"])
    base_tags: set[str] = set(cat_info.get("tags", ["humanoid"]))
    base_tags.add(entry_builder._slugify(title.split(":")[0], max_len=30))
    tags = sorted(t for t in base_tags if t)

    route = paper.get("route", "")
    summary_text = f"{title} is a paper on {route or category_key} for humanoid robotics."
    if title_cn:
        summary_text += f" {title_cn}."
    summary = {"en": summary_text, "zh": summary_text, "ko": ""}

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
    if not sources:
        sources.append({
            "id": "src_001",
            "type": "website",
            "title": title,
            "url": "",
            "date": year,
            "accessed_at": today,
        })

    notes = f"Imported from Humanoid_Robot_Learning_Paper_Notebooks progress.json. Folder: {folder}."
    if route:
        notes += f" Route: {route}."

    status = "partially_verified" if arxiv_id else "unverified"
    confidence = "medium" if arxiv_id else "low"

    functional_roles = ["knowledge", "intelligence"]
    if "Hardware_Design" in category_key:
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


def main() -> int:
    parser = argparse.ArgumentParser(description="Import progress.json papers into the graph.")
    parser.add_argument("--dry-run", action="store_true", help="Preview without writing files.")
    parser.add_argument("--update", action="store_true", help="Fetch latest progress.json from GitHub before importing.")
    args = parser.parse_args()

    if args.update:
        fetch_progress_json()

    if not PROGRESS_PATH.exists():
        print(f"progress.json not found: {PROGRESS_PATH}")
        return 1

    data = json.loads(PROGRESS_PATH.read_text(encoding="utf-8"))
    papers = data.get("papers", [])
    print(f"Loaded {len(papers)} papers from progress.json.")

    existing_titles, existing_arxiv = load_existing_titles_and_arxiv()
    existing_ids = entry_builder.load_existing_ids()
    print(f"Existing titles: {len(existing_titles)} | Existing arXiv IDs: {len(existing_arxiv)}")

    added = 0
    skipped = 0
    for paper in papers:
        fm = build_entry(paper, existing_titles, existing_arxiv, existing_ids)
        if fm is None:
            skipped += 1
            continue
        if args.dry_run:
            print(f"[dry-run] {fm['$id']}: {fm['names']['en'][:80]}")
        else:
            path = entry_builder.write_entry_file(fm, fm["summary"]["en"] or "", "papers", f"{fm['$id']}.md")
            print(f"[wrote] {path.name}")
        added += 1

    print(f"\nTotal: {len(papers)} | Added: {added} | Skipped: {skipped}")
    return 0




def fetch_progress_json() -> None:
    api_url = "https://api.github.com/repos/ImChong/Humanoid_Robot_Learning_Paper_Notebooks/contents/progress.json"
    print(f"Fetching latest progress.json from GitHub API ...")
    resp = requests.get(api_url, timeout=30)
    resp.raise_for_status()
    data = resp.json()
    content = base64.b64decode(data["content"]).decode("utf-8")
    PROGRESS_PATH.parent.mkdir(parents=True, exist_ok=True)
    PROGRESS_PATH.write_text(content, encoding="utf-8")
    print(f"Updated {PROGRESS_PATH} ({len(content)} bytes)")


if __name__ == "__main__":
    raise SystemExit(main())
