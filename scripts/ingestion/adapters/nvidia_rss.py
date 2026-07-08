"""Adapter for NVIDIA Blog robotics RSS feed."""

from __future__ import annotations

import re
from datetime import date
from typing import Any
from xml.etree import ElementTree as ET

import requests

from ai4sci_lib import entry_builder

from ..core import ParsedItem, Source


KEYWORDS = [
    "humanoid", "robot", "robotics", "GR00T", "Isaac", "Unitree", "Figure",
    "Tesla", "locomotion", "manipulation", "dexterous", "VLA", "vision-language-action",
    "sim-to-real", "sim2real", "embodied", "physical ai",
]

TECHNOLOGY_PATTERNS = {
    "GR00T": "technology",
    "Isaac": "software_platform",
    "Isaac Sim": "software_platform",
    "Isaac Lab": "software_platform",
    "Cosmos": "technology",
    "Omniverse": "software_platform",
    "Jetson": "component",
}


class NvidiaRssAdapter:
    """Adapter for https://blogs.nvidia.com/blog/category/robotics/feed/."""

    source_id = "nvidia_robotics_blog"

    def fetch(self, source: Source) -> list[ParsedItem]:
        resp = requests.get(source.url, timeout=60, headers={"User-Agent": "Mozilla/5.0"})
        resp.raise_for_status()
        resp.encoding = resp.apparent_encoding or "utf-8"
        root = ET.fromstring(resp.text.encode("utf-8"))
        channel = root.find("channel")
        if channel is None:
            return []

        items: list[ParsedItem] = []
        for item in channel.findall("item"):
            title_elem = item.find("title")
            link_elem = item.find("link")
            desc_elem = item.find("description")
            date_elem = item.find("pubDate")
            if title_elem is None or link_elem is None:
                continue
            title = (title_elem.text or "").strip()
            link = (link_elem.text or "").strip()
            desc = (desc_elem.text or "").strip() if desc_elem is not None else ""
            pub_date = (date_elem.text or "").strip() if date_elem is not None else ""
            if not title or not link:
                continue
            text = f"{title} {desc}".lower()
            if not any(kw.lower() in text for kw in (source.keywords or KEYWORDS)):
                continue
            year = self._extract_year(pub_date, title)
            summary_text = self._clean_html(desc) or title
            entity_type = self._classify_type(title)
            domains = self._infer_domains(title, entity_type)
            tags = {"nvidia", "robotics", "blog"}
            for kw in ["humanoid", "GR00T", "Isaac", "Unitree", "Figure", "Tesla", "VLA", "locomotion", "manipulation"]:
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
                source_url=link,
                source_type="website",
                source_date=year,
                raw={"description": desc},
            ))
        return items

    @staticmethod
    def _classify_type(title: str) -> str:
        for pattern, entity_type in TECHNOLOGY_PATTERNS.items():
            if pattern.lower() in title.lower():
                return entity_type
        return "report"

    @staticmethod
    def _infer_domains(title: str, entity_type: str) -> list[str]:
        text = title.lower()
        domains: set[str] = set()
        if entity_type in {"technology", "software_platform"}:
            domains.add("08_software_middleware")
            domains.add("07_ai_models_algorithms")
        if entity_type == "component":
            domains.add("02_components")
        domains.add("11_applications_markets")
        if any(kw in text for kw in ["humanoid", "locomotion", "manipulation", "vla"]):
            domains.add("07_ai_models_algorithms")
        return sorted(domains) or ["11_applications_markets"]

    @staticmethod
    def _clean_html(raw: str) -> str:
        text = re.sub(r"<[^>]+>", " ", raw)
        text = re.sub(r"\s+", " ", text)
        return text.strip()

    @staticmethod
    def _extract_year(pub_date: str, title: str) -> str:
        for text in (pub_date, title):
            m = re.search(r"20\d{2}", text)
            if m:
                return m.group(0)
        return str(date.today().year)
