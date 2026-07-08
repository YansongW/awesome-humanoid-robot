#!/usr/bin/env python3
"""Import WeChat article paper lists (with resolved arXiv IDs) into the graph.

Sources:
  data/curated/wechat_161_humanoid_papers.json
  data/curated/wechat_161_arxiv_resolution_complete.json
  data/curated/wechat_42_humanoid_rl_papers.json
  data/curated/wechat_42_humanoid_rl_arxiv_resolution.json
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
CURATED_DIR = ROOT / "data" / "curated"

CATEGORY_MAP: dict[str, dict[str, Any]] = {
    "运控基座与通用全身跟踪": {
        "domains": ["07_ai_models_algorithms", "08_software_middleware"],
        "tags": ["humanoid", "whole_body_control", "motion_tracking"],
    },
    "上半身中心控制与移动操作接口": {
        "domains": ["07_ai_models_algorithms", "08_software_middleware"],
        "tags": ["humanoid", "mobile_manipulation", "upper_body"],
    },
    "视觉感知驱动的人形移动操作": {
        "domains": ["07_ai_models_algorithms", "08_software_middleware"],
        "tags": ["humanoid", "visual_perception", "mobile_manipulation"],
    },
    "生成式运动、语言控制与轨迹规划": {
        "domains": ["07_ai_models_algorithms"],
        "tags": ["humanoid", "generative_motion", "language_control", "trajectory_planning"],
    },
    "动捕、人类视频与交互动作规划": {
        "domains": ["07_ai_models_algorithms", "09_data_datasets"],
        "tags": ["humanoid", "motion_capture", "human_video", "interaction_planning"],
    },
    "特殊任务、接触规划与视觉闭环": {
        "domains": ["07_ai_models_algorithms"],
        "tags": ["humanoid", "contact_planning", "visual_feedback", "special_tasks"],
    },
    "数据采集与遥操作系统": {
        "domains": ["07_ai_models_algorithms", "09_data_datasets"],
        "tags": ["humanoid", "data_collection", "teleoperation"],
    },
    "硬件平台、感知配置与部署扩展": {
        "domains": ["06_design_engineering", "02_components"],
        "tags": ["humanoid", "hardware_platform", "sensing", "deployment"],
    },
    "人形 VLA、世界模型与通用操作": {
        "domains": ["07_ai_models_algorithms", "08_software_middleware"],
        "tags": ["humanoid", "vla", "world_model", "general_manipulation"],
    },
    "从人类第一视角视频学习": {
        "domains": ["07_ai_models_algorithms", "09_data_datasets"],
        "tags": ["humanoid", "egocentric_video", "imitation_learning"],
    },
    "动作数据、重定向、遥操作和交互保真": {
        "domains": ["07_ai_models_algorithms", "09_data_datasets"],
        "tags": ["humanoid", "motion_data", "retargeting", "teleoperation", "interaction_fidelity"],
    },
    "强化学习奖励、课程学习与鲁棒策略": {
        "domains": ["07_ai_models_algorithms"],
        "tags": ["humanoid", "reinforcement_learning", "reward_design", "curriculum_learning", "robust_policy"],
    },
    "全身或足式运动策略与Sim-to-Real": {
        "domains": ["07_ai_models_algorithms", "08_software_middleware"],
        "tags": ["humanoid", "locomotion", "whole_body", "sim_to_real"],
    },
    "全身多接触任务与运动合成": {
        "domains": ["07_ai_models_algorithms"],
        "tags": ["humanoid", "multi_contact", "motion_synthesis"],
    },
}


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


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


def parse_year(date_str: str | None) -> str:
    if not date_str:
        return str(date.today().year)
    m = re.search(r"20\d{2}", str(date_str))
    return m.group(0) if m else str(date.today().year)


def _make_summary(paper: dict[str, Any]) -> str:
    title = paper.get("title", "").strip()
    category = paper.get("category", "")
    summary = paper.get("summary", "")
    if summary:
        return summary
    parts = [f"{title} 是一篇关于{category}的人形机器人研究工作"]
    if paper.get("institution"):
        parts.append(f"由 {paper['institution']} 完成")
    return "。".join(parts) + "。"


def build_entry(
    paper: dict[str, Any],
    arxiv_id: str | None,
    existing_titles: set[str],
    existing_arxiv: set[str],
    existing_ids: set[str],
) -> dict[str, Any] | None:
    title = paper.get("title", "").strip()
    if not title:
        return None

    title_key = title.lower()
    if title_key in existing_titles:
        print(f"[skip duplicate title] {title}")
        return None
    if arxiv_id and arxiv_id in existing_arxiv:
        print(f"[skip duplicate arxiv] {arxiv_id} - {title}")
        return None

    year = parse_year(paper.get("date"))
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

    short_name = paper.get("short_name", title.split(":")[0]).strip() or title
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
    base_tags.add(entry_builder._slugify(short_name, max_len=30))
    tags = sorted(t for t in base_tags if t)

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

    project_url = paper.get("project_url", "")
    if project_url and project_url != (f"https://arxiv.org/abs/{arxiv_id}" if arxiv_id else ""):
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

    notes = f"Imported from WeChat article curated list. Category: {category}."
    if arxiv_id:
        notes += f" arXiv: {arxiv_id}."

    status = "partially_verified" if arxiv_id else "unverified"
    confidence = "medium" if arxiv_id else "low"

    functional_roles = ["knowledge", "intelligence"]
    if "硬件" in category:
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


def load_resolution_map(path: Path) -> dict[str, str]:
    data = load_json(path)
    if not isinstance(data, list):
        return {}
    mapping: dict[str, str] = {}
    for item in data:
        title = item.get("title", "").strip()
        arxiv_id = item.get("arxiv_id", "")
        error = item.get("error")
        if title and arxiv_id and not error:
            mapping[title.lower()] = arxiv_id
    return mapping


def main() -> int:
    parser = argparse.ArgumentParser(description="Import WeChat article papers into the graph.")
    parser.add_argument("--dry-run", action="store_true", help="Count and preview without writing files.")
    args = parser.parse_args()

    humanoid = load_json(CURATED_DIR / "wechat_161_humanoid_papers.json")
    rl = load_json(CURATED_DIR / "wechat_42_humanoid_rl_papers.json")
    humanoid_arxiv = load_resolution_map(CURATED_DIR / "wechat_161_arxiv_resolution_complete.json")
    rl_arxiv = load_resolution_map(CURATED_DIR / "wechat_42_humanoid_rl_arxiv_resolution.json")

    all_papers: list[dict[str, Any]] = []
    seen_titles: set[str] = set()
    for paper in humanoid.get("papers", []):
        title_key = paper.get("title", "").strip().lower()
        if title_key and title_key not in seen_titles:
            seen_titles.add(title_key)
            paper["_arxiv_id"] = humanoid_arxiv.get(title_key)
            all_papers.append(paper)
    for paper in rl.get("papers", []):
        title_key = paper.get("title", "").strip().lower()
        if title_key and title_key not in seen_titles:
            seen_titles.add(title_key)
            paper["_arxiv_id"] = rl_arxiv.get(title_key)
            all_papers.append(paper)

    existing_titles, existing_arxiv = load_existing_titles_and_arxiv()
    existing_ids = entry_builder.load_existing_ids()
    print(f"Combined unique papers from WeChat sources: {len(all_papers)}")
    print(f"Existing titles: {len(existing_titles)} | Existing arXiv IDs: {len(existing_arxiv)}")

    added = 0
    skipped = 0
    for paper in all_papers:
        fm = build_entry(paper, paper.pop("_arxiv_id", None), existing_titles, existing_arxiv, existing_ids)
        if fm is None:
            skipped += 1
            continue
        if args.dry_run:
            print(f"[dry-run] {fm['$id']}: {fm['names']['en'][:80]}")
        else:
            path = entry_builder.write_entry_file(fm, fm["summary"]["en"] or "", "papers", f"{fm['$id']}.md")
            print(f"[wrote] {path.name}")
        added += 1

    print(f"\nTotal unique: {len(all_papers)} | Added: {added} | Skipped: {skipped}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
