"""Adapters for curated JSON lists (Awesome-VLA, awesome-humanoid-robot-learning)."""

from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any

from ai4sci_lib import entry_builder

from ..core import ParsedItem, Source


VLA_DOMAIN = ["07_ai_models_algorithms", "08_software_middleware"]

HUMANOID_CATEGORY_MAP: dict[str, dict[str, Any]] = {
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


def _extract_arxiv_id(url: str) -> str:
    if not url:
        return ""
    m = re.search(r"arxiv\.org/abs/(\d+\.\d+)", url)
    return m.group(1) if m else ""


class AwesomeVLAAdapter:
    """Adapter for data/curated/awesome_vla_papers.json."""

    source_id = "awesome_vla_models"

    def fetch(self, source: Source) -> list[ParsedItem]:
        path = Path(source.fetch_url)
        if not path.exists():
            return []
        data = json.loads(path.read_text(encoding="utf-8"))
        items: list[ParsedItem] = []
        for paper in data.get("papers", []):
            title = paper.get("title", "").strip()
            if not title:
                continue
            year = paper.get("year")
            arxiv_id = (paper.get("arxiv_id") or "").strip()
            source_url = paper.get("source_url", "")
            model = paper.get("model", "").strip()
            summary_text = f"{title} is a {year} vision-language-action model for robotic manipulation"
            institution = paper.get("institution", "")
            if institution:
                summary_text += f" introduced by {institution}"
            venue = paper.get("venue", "")
            if venue:
                summary_text += f" and published at {venue}"
            summary_text += "."
            tags = {"vla", "vision_language_action", "robotic_manipulation"}
            if model:
                tags.add(entry_builder._slugify(model, max_len=30))
            items.append(ParsedItem(
                title=title,
                type="paper",
                year=year,
                names={"en": title, "zh": model or title, "ko": ""},
                summary={"en": summary_text, "zh": summary_text, "ko": ""},
                domains=VLA_DOMAIN,
                tags=sorted(tags),
                arxiv_id=arxiv_id,
                source_url=source_url if source_url else (f"https://arxiv.org/abs/{arxiv_id}" if arxiv_id else ""),
                source_type="paper" if arxiv_id else "website",
                institution=institution,
                raw=paper,
            ))
        return items


class AwesomeHumanoidAdapter:
    """Adapter for data/curated/awesome_humanoid_robot_learning.json."""

    source_id = "awesome_humanoid_robot_learning"

    def fetch(self, source: Source) -> list[ParsedItem]:
        path = Path(source.fetch_url)
        if not path.exists():
            return []
        data = json.loads(path.read_text(encoding="utf-8"))
        items: list[ParsedItem] = []
        for paper in data.get("papers", []):
            title = paper.get("title", "").strip()
            if not title:
                continue
            category = paper.get("category", "")
            cat_info = HUMANOID_CATEGORY_MAP.get(category, {})
            domains = cat_info.get("domains", ["07_ai_models_algorithms"])
            tags: set[str] = set(cat_info.get("tags", ["humanoid"]))
            tags.add(entry_builder._slugify(title.split(":")[0], max_len=30))
            arxiv_url = paper.get("arxiv_url", "")
            arxiv_id = _extract_arxiv_id(arxiv_url)
            website_url = paper.get("website_url", "")
            source_url = arxiv_url or website_url
            year = paper.get("year")
            summary_text = f"{title} is a {year} work on {category.lower()} for humanoid robots"
            if paper.get("code_url"):
                summary_text += ", with open-source code available"
            summary_text += "."
            items.append(ParsedItem(
                title=title,
                type="paper",
                year=year,
                names={"en": title, "zh": title, "ko": ""},
                summary={"en": summary_text, "zh": summary_text, "ko": ""},
                domains=domains,
                tags=sorted(t for t in tags if t),
                arxiv_id=arxiv_id,
                source_url=source_url,
                source_type="paper" if arxiv_id else "website",
                raw=paper,
            ))
        return items
