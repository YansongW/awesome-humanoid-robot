"""Adapter for Humanoid_Robot_Learning_Paper_Notebooks/progress.json."""

from __future__ import annotations

import base64
import json
import re
from pathlib import Path
from typing import Any

import requests

from ai4sci_lib import entry_builder

from ..core import ParsedItem, Source


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


def _extract_arxiv_id(url: str) -> str:
    if not url:
        return ""
    m = re.search(r"arxiv\.org/abs/(\d+\.\d+)", url)
    return m.group(1) if m else ""


class ProgressJsonAdapter:
    """Adapter for progress.json from Humanoid_Robot_Learning_Paper_Notebooks."""

    source_id = "humanoid_paper_notebooks_progress"

    def fetch(self, source: Source) -> list[ParsedItem]:
        data = self._load(source)
        items: list[ParsedItem] = []
        for paper in data.get("papers", []):
            title = paper.get("title", "").strip()
            if not title:
                continue
            title_cn = paper.get("title_cn", "").strip()
            arxiv_url = paper.get("arxiv", "")
            arxiv_id = _extract_arxiv_id(arxiv_url)
            folder = paper.get("folder", "")
            category_key = folder.split("/")[1] if "/" in folder else ""
            cat_info = CATEGORY_MAP.get(category_key, {})
            domains = cat_info.get("domains", ["07_ai_models_algorithms"])
            tags: set[str] = set(cat_info.get("tags", ["humanoid"]))
            tags.add(entry_builder._slugify(title.split(":")[0], max_len=30))
            route = paper.get("route", "")
            summary_text = f"{title} is a paper on {route or category_key} for humanoid robotics."
            if title_cn:
                summary_text += f" {title_cn}."
            items.append(ParsedItem(
                title=title,
                type="paper",
                year=self._extract_year(title),
                names={"en": title, "zh": title_cn or title, "ko": ""},
                summary={"en": summary_text, "zh": summary_text, "ko": ""},
                domains=domains,
                tags=sorted(t for t in tags if t),
                arxiv_id=arxiv_id,
                source_url=arxiv_url,
                source_type="paper" if arxiv_id else "website",
                institution=paper.get("route", ""),
                raw=paper,
            ))
        return items

    def _load(self, source: Source) -> dict[str, Any]:
        fetch_url = source.fetch_url
        if fetch_url.startswith("http"):
            resp = requests.get(fetch_url, timeout=30)
            resp.raise_for_status()
            content = base64.b64decode(resp.json()["content"]).decode("utf-8")
            return json.loads(content)
        path = Path(fetch_url)
        if path.exists():
            return json.loads(path.read_text(encoding="utf-8"))
        return {}

    @staticmethod
    def _extract_year(title: str) -> str:
        m = re.search(r"20\d{2}", title)
        return m.group(0) if m else "2026"
