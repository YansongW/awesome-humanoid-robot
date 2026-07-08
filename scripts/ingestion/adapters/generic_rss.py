"""Generic RSS adapter for industry/news/standards sources."""

from __future__ import annotations

import re
from dataclasses import dataclass
from datetime import date
from typing import Any
from xml.etree import ElementTree as ET

import requests

from ai4sci_lib import entry_builder

from ..core import ParsedItem, Source


@dataclass
class RssSourceConfig:
    """Configuration for a generic RSS source."""

    source_id: str
    default_type: str = "report"
    domains: list[str] | None = None
    functional_roles: list[str] | None = None
    base_tags: set[str] | None = None
    company_keywords: dict[str, str] | None = None
    component_keywords: dict[str, str] | None = None
    technology_keywords: dict[str, str] | None = None


class GenericRssAdapter:
    """Generic RSS adapter that maps items to typed entities."""

    def __init__(self, config: RssSourceConfig) -> None:
        self.cfg = config

    def fetch(self, source: Source) -> list[ParsedItem]:
        resp = requests.get(source.url, timeout=60, headers={"User-Agent": "Mozilla/5.0"})
        resp.raise_for_status()
        resp.encoding = resp.apparent_encoding or "utf-8"
        root = ET.fromstring(resp.text.encode("utf-8"))
        channel = root.find("channel")
        if channel is None:
            return []

        keywords = source.keywords or []
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
            if not title or not link:
                continue
            desc = (desc_elem.text or "").strip() if desc_elem is not None else ""
            pub_date = (date_elem.text or "").strip() if date_elem is not None else ""

            text = f"{title} {desc}".lower()
            if keywords and not any(kw.lower() in text for kw in keywords):
                continue

            entity_type = self._classify_type(title, desc)
            domains = self._infer_domains(title, desc, entity_type)
            tags = self._infer_tags(title, desc, entity_type)
            year = self._extract_year(pub_date, title)
            summary_text = self._clean_html(desc) or title

            items.append(ParsedItem(
                title=title,
                type=entity_type,
                year=year,
                names={"en": title, "zh": title, "ko": ""},
                summary={"en": summary_text, "zh": summary_text, "ko": ""},
                domains=domains,
                functional_roles=self.cfg.functional_roles or ["knowledge", "market"],
                tags=sorted(tags),
                source_url=link,
                source_type="website",
                source_date=year,
                raw={"description": desc},
            ))
        return items

    def _classify_type(self, title: str, desc: str) -> str:
        text = f"{title} {desc}".lower()
        if self.cfg.company_keywords:
            for kw in self.cfg.company_keywords:
                if kw.lower() in text:
                    return "company"
        if self.cfg.component_keywords:
            for kw in self.cfg.component_keywords:
                if kw.lower() in text:
                    return "component"
        if self.cfg.technology_keywords:
            for kw in self.cfg.technology_keywords:
                if kw.lower() in text:
                    return "technology"
        return self.cfg.default_type

    def _infer_domains(self, title: str, desc: str, entity_type: str) -> list[str]:
        if self.cfg.domains:
            return self.cfg.domains
        text = f"{title} {desc}".lower()
        domains: set[str] = set()
        if entity_type in {"company", "market_segment", "application_scenario"}:
            domains.add("11_applications_markets")
        if entity_type in {"component", "robot_system"}:
            domains.add("02_components")
        if entity_type in {"technology", "software_platform", "tool_equipment"}:
            domains.add("08_software_middleware")
        if any(kw in text for kw in ["manufacturing", "machining", "assembly", "factory"]):
            domains.add("03_manufacturing_processes")
        if any(kw in text for kw in ["policy", "regulation", "standard", "safety", "certification", "liability"]):
            domains.add("12_policy_regulation_ethics")
        if any(kw in text for kw in ["actuator", "motor", "reducer", "gearbox", "sensor", "battery", "compute"]):
            domains.add("02_components")
        if any(kw in text for kw in ["humanoid", "locomotion", "manipulation", "vla", "vision-language-action", "ai"]):
            domains.add("07_ai_models_algorithms")
        return sorted(domains) or ["11_applications_markets"]

    def _infer_tags(self, title: str, desc: str, entity_type: str) -> set[str]:
        tags: set[str] = set(self.cfg.base_tags or [])
        text = f"{title} {desc}".lower()
        keyword_map = {
            "humanoid": "humanoid",
            "locomotion": "locomotion",
            "manipulation": "manipulation",
            "actuator": "actuator",
            "motor": "motor",
            "reducer": "reducer",
            "gearbox": "gearbox",
            "sensor": "sensor",
            "battery": "battery",
            "vla": "vla",
            "vision-language-action": "vision_language_action",
            "startup": "startup",
            "funding": "funding",
            "investment": "investment",
            "standard": "standard",
            "safety": "safety",
            "iso": "iso",
            "certification": "certification",
        }
        for kw, tag in keyword_map.items():
            if kw in text:
                tags.add(tag)
        tags.add(entry_builder._slugify(entity_type, max_len=20))
        return tags

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
