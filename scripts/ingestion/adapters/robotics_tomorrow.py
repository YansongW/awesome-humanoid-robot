"""Adapter for RoboticsTomorrow News RSS feed."""

from __future__ import annotations

from .generic_rss import GenericRssAdapter, RssSourceConfig


class RoboticsTomorrowAdapter(GenericRssAdapter):
    """Adapter for https://www.roboticstomorrow.com/rss/news."""

    source_id = "robotics_tomorrow_rss"

    def __init__(self) -> None:
        super().__init__(RssSourceConfig(
            source_id=self.source_id,
            default_type="report",
            domains=["11_applications_markets"],
            functional_roles=["knowledge", "market"],
            base_tags={"robotics", "industry", "news"},
            company_keywords={
                "raises": "company",
                "funding": "company",
                "acquires": "company",
                "acquisition": "company",
                "partnership": "company",
                "launches": "company",
                "appoints": "company",
                "startup": "company",
                "unicorn": "company",
                "series": "company",
            },
            component_keywords={
                "actuator": "component",
                "motor": "component",
                "reducer": "component",
                "gearbox": "component",
                "sensor": "component",
                "battery": "component",
                "end effector": "component",
                "gripper": "component",
                "lidar": "component",
                "camera": "component",
                "compute": "component",
            },
            technology_keywords={
                "software": "technology",
                "platform": "technology",
                "simulation": "technology",
                "digital twin": "technology",
                "fleet management": "technology",
                "middleware": "technology",
                "sdk": "technology",
                "operating system": "technology",
            },
        ))
