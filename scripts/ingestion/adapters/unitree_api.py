"""Adapter for Unitree official news API."""

from __future__ import annotations

import re
from datetime import date
from typing import Any

import requests

from ai4sci_lib import entry_builder

from ..core import ParsedItem, Source


LIST_URL = "https://api.unitree.com/website/news/list"
INFO_URL = "https://api.unitree.com/website/news/info"

KEYWORDS = [
    "humanoid", "robot", "robotics", "GR00T", "Isaac", "G1", "H1", "H2", "G2",
    "dexterous", "manipulation", "locomotion", "embodied", "AI",
]

COMPONENT_PATTERNS = {
    "G1": "robot_system",
    "H1": "robot_system",
    "H2": "robot_system",
    "G2": "robot_system",
    "Go2": "robot_system",
    "B-W": "robot_system",
    "LiDAR": "component",
    "4D LiDAR": "component",
}


class UnitreeNewsAdapter:
    """Adapter for Unitree /website/news/list + /news/info."""

    source_id = "unitree_news"

    def fetch(self, source: Source) -> list[ParsedItem]:
        resp = requests.get(LIST_URL, timeout=30, headers={"User-Agent": "Mozilla/5.0"})
        resp.raise_for_status()
        data = resp.json()
        items: list[ParsedItem] = []
        seen_titles: set[str] = set()
        for news in data.get("data", {}).get("items", []):
            if news.get("lang") != ["2"]:
                continue
            title = news.get("title", "").strip()
            if not title or title.lower() in seen_titles:
                continue
            desc = news.get("description", "").strip()
            text = f"{title} {desc}".lower()
            if not any(kw.lower() in text for kw in KEYWORDS):
                continue
            detail = self._fetch_detail(news.get("id", ""))
            content_html = detail.get("article", {}).get("content", "")
            summary_text = self._clean_html(content_html) or desc
            year = self._extract_year(news.get("postTime", ""))
            entity_type = self._classify_type(title)
            domains = self._infer_domains(title, entity_type)
            tags = {"unitree", "robotics", "company_news"}
            for kw in ["humanoid", "G1", "H1", "H2", "GR00T", "dexterous", "manipulation", "locomotion"]:
                if kw.lower() in title.lower():
                    tags.add(entry_builder._slugify(kw, max_len=20))
            items.append(ParsedItem(
                title=title,
                type=entity_type,
                year=year,
                names={"en": title, "zh": title, "ko": ""},
                summary={"en": summary_text, "zh": summary_text, "ko": ""},
                domains=domains,
                functional_roles=["knowledge", "market"],
                tags=sorted(tags),
                source_url="https://www.unitree.com/mobile/news",
                source_type="website",
                source_date=news.get("postTime", "").split()[0] if news.get("postTime") else year,
                raw=news,
            ))
            seen_titles.add(title.lower())
        return items

    def _fetch_detail(self, news_id: str) -> dict[str, Any]:
        try:
            resp = requests.get(INFO_URL, params={"id": news_id}, timeout=20, headers={"User-Agent": "Mozilla/5.0"})
            resp.raise_for_status()
            return resp.json().get("data", {}) or {}
        except Exception:
            return {}

    @staticmethod
    def _classify_type(title: str) -> str:
        for pattern, entity_type in COMPONENT_PATTERNS.items():
            if pattern.lower() in title.lower():
                return entity_type
        return "report"

    @staticmethod
    def _infer_domains(title: str, entity_type: str) -> list[str]:
        text = title.lower()
        domains: set[str] = set()
        if entity_type in {"robot_system", "component"}:
            domains.add("06_design_engineering")
            domains.add("02_components")
        domains.add("11_applications_markets")
        if any(kw in text for kw in ["sensor", "lidar", "camera", "compute"]):
            domains.add("02_components")
        return sorted(domains) or ["11_applications_markets"]

    @staticmethod
    def _clean_html(raw: str) -> str:
        text = re.sub(r"<[^>]+>", " ", raw)
        text = re.sub(r"\s+", " ", text)
        return text.strip()

    @staticmethod
    def _extract_year(post_time: str) -> str:
        m = re.search(r"20\d{2}", post_time)
        return m.group(0) if m else str(date.today().year)
