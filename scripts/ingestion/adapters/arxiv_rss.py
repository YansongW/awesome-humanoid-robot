"""Adapter for arXiv cs.RO RSS feed."""

from __future__ import annotations

import re
from datetime import date
from typing import Any
from xml.etree import ElementTree as ET

import requests

from ai4sci_lib import entry_builder

from ..core import ParsedItem, Source


DEFAULT_KEYWORDS = [
    "humanoid",
    "locomotion",
    "loco-manipulation",
    "manipulation",
    "teleoperation",
    "whole-body",
    "whole body",
    "vision-language-action",
    "vla",
    "sim-to-real",
    "sim2real",
    "bipedal",
    "legged",
    "robot learning",
    "human motion",
    "character control",
    "motion tracking",
    "human-to-humanoid",
    "humanoid robot",
    "humanoid control",
    "humanoid locomotion",
    "humanoid manipulation",
]


class ArxivRssAdapter:
    """Adapter for http://export.arxiv.org/rss/cs.RO."""

    source_id = "arxiv_ro_rss"

    def fetch(self, source: Source) -> list[ParsedItem]:
        url = source.url
        keywords = source.keywords or DEFAULT_KEYWORDS
        resp = requests.get(url, timeout=60)
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
            if title_elem is None or link_elem is None:
                continue
            title = (title_elem.text or "").strip()
            link = (link_elem.text or "").strip()
            desc = (desc_elem.text or "").strip() if desc_elem is not None else ""
            if not title or not link:
                continue
            text = f"{title} {desc}".lower()
            if not any(kw.lower() in text for kw in keywords):
                continue
            arxiv_id = self._extract_arxiv_id(link)
            year = self._extract_year(title, desc)
            summary_text = desc or f"{title} is a recent arXiv paper in robotics."
            items.append(ParsedItem(
                title=title,
                type="paper",
                year=year,
                names={"en": title, "zh": title, "ko": ""},
                summary={"en": summary_text, "zh": summary_text, "ko": ""},
                domains=["07_ai_models_algorithms", "08_software_middleware"],
                tags=["humanoid", "robotics", entry_builder._slugify(title.split(":")[0], max_len=30)],
                arxiv_id=arxiv_id,
                source_url=link,
                source_type="paper",
                source_date=year,
                raw={"description": desc},
            ))
        return items

    @staticmethod
    def _extract_arxiv_id(url: str) -> str:
        m = re.search(r"arxiv\.org/abs/(\d+\.\d+)", url)
        return m.group(1) if m else ""

    @staticmethod
    def _extract_year(title: str, desc: str) -> str:
        for text in (title, desc):
            m = re.search(r"20\d{2}", text)
            if m:
                return m.group(0)
        return str(date.today().year)
