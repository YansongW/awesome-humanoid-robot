#!/usr/bin/env python3
"""Generate or update workstream YAMLs from a curated paper list.

Usage:
    source .venv/bin/activate
    python scripts/generate_workstream_from_curated.py \
        --papers data/curated/wechat_161_humanoid_papers.json \
        --resolution data/curated/wechat_161_arxiv_resolution.json \
        --out-dir scripts/ai4sci_workstreams/curated/wechat_161

The script:
1. Reads the curated paper list and the arXiv resolution table.
2. Groups papers by category.
3. For each category, creates a workstream YAML seeded with the resolved arXiv IDs.
4. Adds taxonomy-aligned seed queries so discovery can extend beyond the list.
"""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any

import yaml

from ai4sci_lib import config


CATEGORY_CONFIG: dict[str, dict[str, Any]] = {
    "运控基座与通用全身跟踪": {
        "name": "whole_body_control_curated",
        "path": "definition/algorithm_survey/control/whole_body_control_curated.yaml",
        "domains": ["07_ai_models_algorithms", "06_design_engineering", "11_applications_markets"],
        "seed_queries": [
            "humanoid whole-body control heterogeneous data",
            "humanoid motion tracking controller",
            "humanoid locomotion foundation model",
            "versatile humanoid control reinforcement learning",
            "humanoid balance and agility control",
        ],
    },
    "上半身中心控制与移动操作接口": {
        "name": "mobile_manipulation_interfaces_curated",
        "path": "definition/algorithm_survey/control/mobile_manipulation_interfaces_curated.yaml",
        "domains": ["07_ai_models_algorithms", "02_components", "11_applications_markets"],
        "seed_queries": [
            "humanoid mobile manipulation interface",
            "upper body control humanoid robot",
            "humanoid teleoperation interface manipulation",
            "bimanual mobile manipulation humanoid",
            "whole-body manipulation interface",
        ],
    },
    "视觉感知驱动的人形移动操作": {
        "name": "vision_driven_loco_manipulation_curated",
        "path": "definition/algorithm_survey/high_level_ai/vision_driven_loco_manipulation_curated.yaml",
        "domains": ["07_ai_models_algorithms", "08_software_middleware", "11_applications_markets"],
        "seed_queries": [
            "vision guided humanoid locomotion manipulation",
            "perception driven humanoid mobile manipulation",
            "humanoid robot visual servoing manipulation",
            "visual perception whole-body control humanoid",
            "humanoid navigation and manipulation vision",
        ],
    },
    "生成式运动、语言控制与轨迹规划": {
        "name": "generative_motion_language_planning_curated",
        "path": "definition/algorithm_survey/high_level_ai/generative_motion_language_planning_curated.yaml",
        "domains": ["07_ai_models_algorithms", "08_software_middleware"],
        "seed_queries": [
            "generative humanoid motion language control",
            "humanoid trajectory planning diffusion model",
            "language conditioned humanoid motion",
            "humanoid robot motion generation transformer",
            "generative model humanoid locomotion trajectory",
        ],
    },
    "动捕、人类视频与交互动作规划": {
        "name": "mocap_human_video_action_planning_curated",
        "path": "definition/algorithm_survey/learning/mocap_human_video_action_planning_curated.yaml",
        "domains": ["07_ai_models_algorithms", "09_data_datasets", "11_applications_markets"],
        "seed_queries": [
            "humanoid motion capture imitation learning",
            "human video to humanoid action",
            "humanoid interaction planning from video",
            "motion retargeting humanoid robot",
            "humanoid action planning human demonstration",
        ],
    },
    "特殊任务、接触规划与视觉闭环": {
        "name": "contact_planning_visual_feedback_curated",
        "path": "definition/algorithm_survey/learning/contact_planning_visual_feedback_curated.yaml",
        "domains": ["07_ai_models_algorithms", "06_design_engineering", "11_applications_markets"],
        "seed_queries": [
            "humanoid contact planning visual feedback",
            "humanoid robot special task planning",
            "visual closed loop humanoid manipulation",
            "humanoid contact rich manipulation",
            "humanoid task planning perception action loop",
        ],
    },
    "数据采集与遥操作系统": {
        "name": "teleoperation_data_collection_curated",
        "path": "definition/algorithm_survey/learning/teleoperation_data_collection_curated.yaml",
        "domains": ["07_ai_models_algorithms", "09_data_datasets", "08_software_middleware"],
        "seed_queries": [
            "humanoid teleoperation data collection system",
            "humanoid robot demonstration data",
            "whole body teleoperation humanoid",
            "humanoid imitation learning dataset",
            "remote teleoperation humanoid robot",
        ],
    },
    "硬件平台、感知配置与部署扩展": {
        "name": "hardware_perception_deployment_curated",
        "path": "definition/algorithm_survey/high_level_ai/hardware_perception_deployment_curated.yaml",
        "domains": ["02_components", "06_design_engineering", "08_software_middleware", "11_applications_markets"],
        "seed_queries": [
            "humanoid robot hardware platform perception",
            "humanoid sensor configuration deployment",
            "humanoid robot edge deployment",
            "humanoid platform design sensing",
            "humanoid robot field deployment scalability",
        ],
    },
    "人形 VLA、世界模型与通用操作": {
        "name": "vla_world_models_curated",
        "path": "definition/algorithm_survey/high_level_ai/vla_world_models_curated.yaml",
        "domains": ["07_ai_models_algorithms", "08_software_middleware", "09_data_datasets"],
        "seed_queries": [
            "humanoid vision language action model",
            "humanoid world model manipulation",
            "humanoid general manipulation policy",
            "VLA humanoid robot",
            "foundation model humanoid manipulation",
        ],
    },
    "从人类第一视角视频学习": {
        "name": "egocentric_video_learning_curated",
        "path": "definition/algorithm_survey/learning/egocentric_video_learning_curated.yaml",
        "domains": ["07_ai_models_algorithms", "09_data_datasets", "11_applications_markets"],
        "seed_queries": [
            "egocentric video learning humanoid robot",
            "first person video robot manipulation",
            "humanoid learning from egocentric video",
            "ego centric robot policy learning",
            "human demonstration video humanoid imitation",
        ],
    },
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Generate workstream YAMLs from a curated paper list."
    )
    parser.add_argument(
        "--papers",
        type=Path,
        default=config.ROOT / "data" / "curated" / "wechat_161_humanoid_papers.json",
        help="Path to curated papers JSON.",
    )
    parser.add_argument(
        "--resolution",
        type=Path,
        default=config.ROOT / "data" / "curated" / "wechat_161_arxiv_resolution.json",
        help="Path to arXiv resolution JSON.",
    )
    parser.add_argument(
        "--out-dir",
        type=Path,
        default=config.WORKSTREAMS_DIR / "curated" / "wechat_161",
        help="Output directory for generated workstream YAMLs.",
    )
    parser.add_argument(
        "--max-papers",
        type=int,
        default=None,
        help="Override max_papers per workstream (default: number of papers in category).",
    )
    return parser.parse_args()


def load_json(path: Path) -> Any:
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def clean_arxiv_id(arxiv_id: str | None) -> str | None:
    if not arxiv_id:
        return None
    # Strip version suffix (e.g. 2511.17373v3 -> 2511.17373)
    m = re.match(r"(\d+\.\d+)(v\d+)?", arxiv_id.strip())
    if m:
        return m.group(1)
    return arxiv_id.strip()


def slugify(text: str) -> str:
    text = text.strip().lower()
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"[-\s]+", "_", text)
    return text[:80]


def build_workstream(
    category_name: str,
    papers: list[dict[str, Any]],
    max_papers: int | None,
) -> dict[str, Any]:
    cfg = CATEGORY_CONFIG.get(category_name)
    if cfg is None:
        # Fallback: use slugified category name and generic settings.
        slug = slugify(category_name)
        cfg = {
            "name": f"{slug}_curated",
            "path": f"curated/wechat_161/{slug}_curated.yaml",
            "domains": ["07_ai_models_algorithms"],
            "seed_queries": [f"{category_name} humanoid robot"],
        }

    arxiv_ids: list[str] = []
    seen: set[str] = set()
    for p in papers:
        aid = clean_arxiv_id(p.get("arxiv_id"))
        if aid and aid not in seen:
            arxiv_ids.append(aid)
            seen.add(aid)

    # Extend seed queries with title keywords to improve recall.
    extra_queries: list[str] = []
    for p in papers[:5]:
        title = p.get("title", "")
        if title:
            # Take first few meaningful words from title.
            words = [w for w in re.findall(r"[A-Za-z0-9]+", title) if len(w) > 3][:4]
            if words:
                extra_queries.append("humanoid " + " ".join(words).lower())

    seed_queries = cfg["seed_queries"] + extra_queries[:5]
    seed_queries = list(dict.fromkeys(seed_queries))  # preserve order, dedupe

    return {
        "name": cfg["name"],
        "description": f"Curated workstream for: {category_name}.\nSeeded with {len(arxiv_ids)} resolved arXiv papers from the WeChat 161-paper list.",
        "seed_queries": seed_queries,
        "paper_ids": arxiv_ids,
        "target_entity_types": ["paper", "method", "formalism", "technology", "component"],
        "target_domains": cfg["domains"],
        "relationship_patterns": [
            "cites",
            "is_based_on",
            "uses",
            "formalizes",
            "builds_on",
            "has_prerequisite",
            "instantiates",
            "derived_from",
        ],
        "relevance_threshold": "medium",
        "max_papers": max_papers if max_papers is not None else max(len(arxiv_ids), 10),
        "priority": 1,
        "sources": ["arxiv"],
        "metadata": {
            "curated_source": "wechat_161_humanoid_papers",
            "category": category_name,
            "resolved_count": len(arxiv_ids),
            "total_count": len(papers),
        },
    }


def main() -> int:
    args = parse_args()
    papers_data = load_json(args.papers)
    resolution_data = load_json(args.resolution)

    # Build a num -> arxiv_id map.
    num_to_arxiv: dict[str, str] = {}
    for item in resolution_data:
        num = str(item.get("num", "")).strip()
        arxiv_id = item.get("arxiv_id") or item.get("arxiv")
        if num and arxiv_id:
            num_to_arxiv[num] = arxiv_id

    # Merge resolution into paper records.
    enriched: list[dict[str, Any]] = []
    for p in papers_data.get("papers", []):
        num = str(p.get("num", "")).strip()
        arxiv_id = num_to_arxiv.get(num)
        enriched.append({**p, "arxiv_id": arxiv_id})

    # Group by category.
    by_category: dict[str, list[dict[str, Any]]] = {}
    for p in enriched:
        cat = p.get("category", "Uncategorized")
        by_category.setdefault(cat, []).append(p)

    args.out_dir.mkdir(parents=True, exist_ok=True)

    generated: list[Path] = []
    for cat, papers in by_category.items():
        ws = build_workstream(cat, papers, args.max_papers)
        cfg = CATEGORY_CONFIG.get(cat)
        rel_path = Path(cfg["path"] if cfg else f"curated/wechat_161/{slugify(cat)}_curated.yaml")
        out_path = args.out_dir / rel_path.name
        with open(out_path, "w", encoding="utf-8") as f:
            yaml.safe_dump(ws, f, allow_unicode=True, sort_keys=False)
        generated.append(out_path)
        print(f"[generate] {cat}: {len(ws['paper_ids'])} paper IDs -> {out_path}")

    print(f"\n[generate] Created {len(generated)} workstream YAML(s) in {args.out_dir}")
    unresolved = [p for p in enriched if not p.get("arxiv_id")]
    if unresolved:
        print(f"[generate] Warning: {len(unresolved)} paper(s) without resolved arXiv ID")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
