#!/usr/bin/env python3
"""Import all 161 papers from the WeChat curated list into the knowledge graph.

This script is intentionally exhaustive: every paper in the curated list becomes a
production entry, in line with the project rule that the knowledge graph must be
comprehensive rather than a Top-N selection.

Usage:
    python scripts/import_wechat_161_papers.py --dry-run
    python scripts/import_wechat_161_papers.py
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
CURATED_PATH = ROOT / "data" / "curated" / "wechat_161_humanoid_papers.json"

CATEGORY_MAP: dict[str, dict[str, Any]] = {
    "运控基座与通用全身跟踪": {
        "domains": ["06_design_engineering", "07_ai_models_algorithms"],
        "layers": ["midstream", "intelligence"],
        "functional_roles": ["knowledge", "intelligence"],
        "tags": ["locomotion", "whole_body_control", "motion_tracking", "balance", "behavioral_foundation_model"],
    },
    "上半身中心控制与移动操作接口": {
        "domains": ["06_design_engineering", "07_ai_models_algorithms"],
        "layers": ["midstream", "intelligence"],
        "functional_roles": ["knowledge", "intelligence"],
        "tags": ["upper_body_control", "mobile_manipulation", "whole_body_control", "manipulation_interface"],
    },
    "视觉感知驱动的人形移动操作": {
        "domains": ["07_ai_models_algorithms", "06_design_engineering"],
        "layers": ["intelligence", "midstream"],
        "functional_roles": ["knowledge", "intelligence"],
        "tags": ["visual_perception", "mobile_manipulation", "vision_guided_control", "scene_understanding"],
    },
    "生成式运动、语言控制与轨迹规划": {
        "domains": ["07_ai_models_algorithms"],
        "layers": ["intelligence"],
        "functional_roles": ["knowledge", "intelligence"],
        "tags": ["generative_motion", "language_control", "trajectory_planning", "motion_generation"],
    },
    "动捕、人类视频与交互动作规划": {
        "domains": ["07_ai_models_algorithms", "09_data_datasets"],
        "layers": ["intelligence"],
        "functional_roles": ["knowledge", "intelligence"],
        "tags": ["motion_capture", "human_video", "interaction_planning", "motion_retargeting"],
    },
    "特殊任务、接触规划与视觉闭环": {
        "domains": ["07_ai_models_algorithms", "11_applications_markets"],
        "layers": ["intelligence", "validation_markets"],
        "functional_roles": ["knowledge", "intelligence"],
        "tags": ["contact_planning", "task_planning", "visual_closed_loop", "mobile_manipulation"],
    },
    "数据采集与遥操作系统": {
        "domains": ["09_data_datasets", "07_ai_models_algorithms"],
        "layers": ["intelligence"],
        "functional_roles": ["knowledge", "intelligence"],
        "tags": ["data_collection", "teleoperation", "human_demonstration", "dataset"],
    },
    "硬件平台、感知配置与部署扩展": {
        "domains": ["02_components", "06_design_engineering"],
        "layers": ["upstream", "midstream"],
        "functional_roles": ["knowledge", "component"],
        "tags": ["hardware_platform", "sensor_suite", "deployment", "real_world"],
    },
    "人形 VLA、世界模型与通用操作": {
        "domains": ["07_ai_models_algorithms", "08_software_middleware"],
        "layers": ["intelligence"],
        "functional_roles": ["knowledge", "intelligence"],
        "tags": ["vla", "vision_language_action", "world_model", "general_manipulation"],
    },
    "从人类第一视角视频学习": {
        "domains": ["07_ai_models_algorithms", "09_data_datasets"],
        "layers": ["intelligence"],
        "functional_roles": ["knowledge", "intelligence"],
        "tags": ["egocentric_video", "imitation_learning", "first_person_video", "vla"],
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


def build_entry(paper: dict[str, Any], existing_titles: set[str]) -> dict[str, Any] | None:
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
    # Ensure uniqueness
    candidate_id = ent_id
    counter = 1
    existing_ids = entry_builder.load_existing_ids()
    while candidate_id in existing_ids:
        candidate_id = f"{ent_id}_{counter}"
        counter += 1
    ent_id = candidate_id

    short_name = paper.get("short_name", "")
    desc = paper.get("desc", "")
    names = {
        "en": title,
        "zh": f"{short_name}｜{desc}" if short_name and desc else (short_name or title),
        "ko": "",
    }

    summary_text = paper.get("summary", "")
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

    project_url = paper.get("project_url", "")
    source_url = project_url if project_url.startswith(("http://", "https://")) else ""
    today = str(date.today())
    sources = []
    if source_url:
        sources.append({
            "id": "src_001",
            "type": "website",
            "title": f"{short_name} project page" if short_name else "Project page",
            "url": source_url,
            "date": year,
            "accessed_at": today,
        })
    else:
        sources.append({
            "id": "src_001",
            "type": "website",
            "title": title,
            "url": "",
            "date": year,
            "accessed_at": today,
        })

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
            "status": "ai_proposed",
            "reviewed_by": "ai",
            "reviewed_at": today,
            "confidence": "low",
            "notes": f"Imported from WeChat curated list ({paper.get('num', '')}). Institution: {paper.get('institution', '')}. Full title: {title}.",
        },
        "sources": sources,
    }


def write_entry(frontmatter: dict[str, Any]) -> Path:
    subdir = "papers"
    filename = f"{frontmatter['$id']}.md"
    body = frontmatter["summary"]["en"] or ""
    content = f"---\n{yaml.dump(frontmatter, sort_keys=False, allow_unicode=True, default_flow_style=False)}---\n\n{body.strip()}\n"
    out_dir = RESEARCH_DIR / subdir
    out_dir.mkdir(parents=True, exist_ok=True)
    path = out_dir / filename
    path.write_text(content, encoding="utf-8")
    return path


def main() -> int:
    parser = argparse.ArgumentParser(description="Import the 161 WeChat papers into the graph.")
    parser.add_argument("--dry-run", action="store_true", help="Count and preview without writing files.")
    args = parser.parse_args()

    if not CURATED_PATH.exists():
        print(f"Curated data not found: {CURATED_PATH}")
        return 1

    data = json.loads(CURATED_PATH.read_text(encoding="utf-8"))
    papers = data.get("papers", [])
    existing_titles = load_existing_titles()
    print(f"Loaded {len(papers)} papers from curated list.")
    print(f"Existing titles in graph: {len(existing_titles)}")

    added = 0
    skipped = 0
    for paper in papers:
        fm = build_entry(paper, existing_titles)
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
