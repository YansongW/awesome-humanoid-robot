"""Adapter for IEEE Spectrum / Robotics RSS feed."""

from __future__ import annotations

from .generic_rss import GenericRssAdapter, RssSourceConfig


class IeeeSpectrumRoboticsAdapter(GenericRssAdapter):
    """Adapter for https://spectrum.ieee.org/feeds/topic/robotics.rss."""

    source_id = "ieee_spectrum_robotics_rss"

    def __init__(self) -> None:
        super().__init__(RssSourceConfig(
            source_id=self.source_id,
            default_type="report",
            domains=["11_applications_markets", "07_ai_models_algorithms"],
            functional_roles=["knowledge", "intelligence"],
            base_tags={"robotics", "ieee", "technology"},
            company_keywords={},
            component_keywords={},
            technology_keywords={},
        ))


