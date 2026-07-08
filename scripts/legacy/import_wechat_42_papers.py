#!/usr/bin/env python3
"""Import the 42 WeChat humanoid-RL papers into the knowledge graph.

This script is intentionally exhaustive: every paper in the curated list becomes a
production entry, in line with the project rule that the knowledge graph must be
comprehensive rather than a Top-N selection.

Usage:
    python scripts/import_wechat_42_papers.py --dry-run
    python scripts/import_wechat_42_papers.py
"""

from __future__ import annotations

import argparse
import json
import re
import unicodedata
from datetime import date
from pathlib import Path
from typing import Any

import yaml

from ai4sci_lib import config, entry_builder


ROOT = config.ROOT
RESEARCH_DIR = config.RESEARCH_DIR
CURATED_PATH = ROOT / "data" / "curated" / "wechat_42_humanoid_rl_papers.json"
RESOLUTION_PATH = ROOT / "data" / "curated" / "wechat_42_humanoid_rl_arxiv_resolution.json"

CATEGORY_MAP: dict[str, dict[str, Any]] = {
    "动作数据、重定向、遥操作和交互保真": {
        "domains": ["07_ai_models_algorithms", "09_data_datasets"],
        "layers": ["intelligence"],
        "functional_roles": ["knowledge", "intelligence"],
        "tags": [
            "motion_retargeting",
            "teleoperation",
            "human_video",
            "interaction_fidelity",
            "data_collection",
            "human_demonstration",
        ],
    },
    "物理模仿、通用 motion tracker 和身体基础模型": {
        "domains": ["07_ai_models_algorithms"],
        "layers": ["intelligence"],
        "functional_roles": ["knowledge", "intelligence"],
        "tags": [
            "motion_tracking",
            "physics_based_control",
            "imitation_learning",
            "behavioral_foundation_model",
            "whole_body_control",
        ],
    },
    "感知式高动态运动": {
        "domains": ["07_ai_models_algorithms"],
        "layers": ["intelligence"],
        "functional_roles": ["knowledge", "intelligence"],
        "tags": [
            "perception",
            "high_dynamic_motion",
            "parkour",
            "locomotion",
            "vision_guided_control",
        ],
    },
    "视觉闭环、全身移动操作、任务接口和世界模型": {
        "domains": ["07_ai_models_algorithms", "08_software_middleware"],
        "layers": ["intelligence"],
        "functional_roles": ["knowledge", "intelligence"],
        "tags": [
            "visual_closed_loop",
            "mobile_manipulation",
            "whole_body_control",
            "vla",
            "world_model",
            "task_interface",
        ],
    },
    "接触、柔顺、负载和失败恢复": {
        "domains": ["07_ai_models_algorithms"],
        "layers": ["intelligence"],
        "functional_roles": ["knowledge", "intelligence"],
        "tags": [
            "contact_rich",
            "compliance",
            "load_carrying",
            "fall_recovery",
            "safety",
            "whole_body_control",
        ],
    },
}


def _slugify(text: str, max_len: int = 30) -> str:
    text = unicodedata.normalize("NFKD", text)
    text = text.encode("ascii", "ignore").decode("ascii")
    text = re.sub(r"[^\w\s-]", "", text).strip().lower()
    text = re.sub(r"[-\s]+", "_", text)
    return text[:max_len].strip("_")


def extract_year(date_str: str) -> str:
    m = re.search(r"(20\d{2})", date_str)
    return m.group(1) if m else str(date.today().year)


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


def load_arxiv_resolution() -> dict[str, str]:
    if not RESOLUTION_PATH.exists():
        return {}
    data = json.loads(RESOLUTION_PATH.read_text(encoding="utf-8"))
    return {
        item["num"]: item["arxiv_id"]
        for item in data
        if item.get("arxiv_id")
    }


def build_entry(
    paper: dict[str, Any],
    arxiv_map: dict[str, str],
    existing_titles: set[str],
) -> dict[str, Any] | None:
    title = paper.get("title", "").strip()
    if not title:
        return None
    if title.lower() in existing_titles:
        print(f"[skip duplicate] {title}")
        return None

    category = paper.get("category", "")
    cat_info = CATEGORY_MAP.get(category, {})
    year = extract_year(paper.get("date", ""))
    title_slug = _slugify(title, max_len=30)
    ent_id = f"ent_paper_{title_slug}_{year}"

    candidate_id = ent_id
    counter = 1
    existing_ids = entry_builder.load_existing_ids()
    while candidate_id in existing_ids:
        candidate_id = f"{ent_id}_{counter}"
        counter += 1
    ent_id = candidate_id

    short_name = paper.get("short_name", "")
    names = {
        "en": title,
        "zh": short_name or title,
        "ko": "",
    }

    summary_text = paper.get("summary", "").strip()
    summary = {
        "en": summary_text,
        "zh": summary_text,
        "ko": "",
    }

    domains = cat_info.get("domains", ["07_ai_models_algorithms"])
    layers = cat_info.get("layers", ["intelligence"])
    functional_roles = cat_info.get("functional_roles", ["knowledge"])
    base_tags = set(cat_info.get("tags", []))
    base_tags.add(_slugify(short_name, max_len=30))
    base_tags.add(_slugify(category, max_len=30))
    tags = sorted(t for t in base_tags if t)

    project_url = paper.get("project_url", "").strip()
    arxiv_id = arxiv_map.get(paper.get("num", ""))
    today = str(date.today())
    sources: list[dict[str, Any]] = []

    if arxiv_id:
        sources.append({
            "id": "src_001",
            "type": "paper",
            "title": f"{title} (arXiv)",
            "url": f"https://arxiv.org/abs/{arxiv_id}",
            "date": year,
            "accessed_at": today,
        })

    if project_url.startswith(("http://", "https://")):
        sources.append({
            "id": "src_002" if arxiv_id else "src_001",
            "type": "website",
            "title": f"{short_name} project page" if short_name else "Project page",
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

    if arxiv_id:
        status = "partially_verified"
        confidence = "medium"
        notes = (
            f"Imported from WeChat curated list ({paper.get('num', '')}). "
            f"Institution: {paper.get('institution', '')}. "
            f"arXiv: {arxiv_id}."
        )
    else:
        status = "unverified"
        confidence = "low"
        notes = (
            f"Imported from WeChat curated list ({paper.get('num', '')}). "
            f"Institution: {paper.get('institution', '')}. "
            "No canonical arXiv ID resolved yet."
        )

    return {
        "$id": ent_id,
        "$schema": "../../data/schema/v1/entry_schema.json",
        "$version": 1,
        "type": "paper",
        "names": names,
        "summary": summary,
        "domains": domains,
        "layers": layers,
        "functional_roles": functional_roles,
        "tags": tags,
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
    content = (
        f"---\n{yaml.dump(frontmatter, sort_keys=False, allow_unicode=True, default_flow_style=False)}---\n\n"
        f"{body.strip()}\n"
    )
    out_dir = RESEARCH_DIR / subdir
    out_dir.mkdir(parents=True, exist_ok=True)
    path = out_dir / filename
    path.write_text(content, encoding="utf-8")
    return path


def main() -> int:
    parser = argparse.ArgumentParser(description="Import the 42 WeChat humanoid-RL papers into the graph.")
    parser.add_argument("--dry-run", action="store_true", help="Count and preview without writing files.")
    args = parser.parse_args()

    if not CURATED_PATH.exists():
        print(f"Curated data not found: {CURATED_PATH}")
        return 1

    data = json.loads(CURATED_PATH.read_text(encoding="utf-8"))
    papers = data.get("papers", [])
    arxiv_map = load_arxiv_resolution()
    existing_titles = load_existing_titles()
    print(f"Loaded {len(papers)} papers from curated list.")
    print(f"Resolved {len(arxiv_map)} arXiv IDs.")
    print(f"Existing titles in graph: {len(existing_titles)}")

    added = 0
    skipped = 0
    for paper in papers:
        fm = build_entry(paper, arxiv_map, existing_titles)
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
