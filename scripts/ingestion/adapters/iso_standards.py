"""Adapter for ISO standards/news RSS feed."""

from __future__ import annotations

from .generic_rss import GenericRssAdapter, RssSourceConfig


class IsoRoboticsAdapter(GenericRssAdapter):
    """Adapter for https://www.iso.org/news.xml filtered to robotics."""

    source_id = "iso_robotics_news"

    def __init__(self) -> None:
        super().__init__(RssSourceConfig(
            source_id=self.source_id,
            default_type="standard",
            domains=["12_policy_regulation_ethics"],
            functional_roles=["knowledge", "regulation"],
            base_tags={"iso", "standard", "robotics", "safety"},
            company_keywords={},
            component_keywords={},
            technology_keywords={
                "standard": "standard",
                "safety": "standard",
                "guideline": "standard",
                "regulation": "standard",
                "certification": "certification",
            },
        ))

    def _classify_type(self, title: str, desc: str) -> str:
        text = f"{title} {desc}".lower()
        if "certif" in text:
            return "certification"
        if any(kw in text for kw in ["standard", "iso", "iec", "safety", "regulation", "guideline"]):
            return "standard"
        return self.cfg.default_type
