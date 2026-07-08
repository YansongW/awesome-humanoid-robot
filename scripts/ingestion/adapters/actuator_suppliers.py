"""Adapter for curated actuator/joint/supplier data."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from ai4sci_lib import entry_builder

from ..core import ParsedItem, Source


class ActuatorSuppliersAdapter:
    """Adapter for data/curated/humanoid_actuators_suppliers.json."""

    source_id = "humanoid_actuators_suppliers"

    def fetch(self, source: Source) -> list[ParsedItem]:
        path = Path(source.fetch_url)
        if not path.exists():
            return []
        data = json.loads(path.read_text(encoding="utf-8"))
        items: list[ParsedItem] = []
        for entry in data.get("entries", []):
            title = entry.get("title", "").strip()
            if not title:
                continue
            entity_type = entry.get("type", "component")
            year = entry.get("year", 2024)
            names = entry.get("names", {"en": title, "zh": title, "ko": ""})
            summary = entry.get("summary", {"en": title, "zh": title, "ko": ""})
            domains = entry.get("domains", ["02_components"])
            tags: set[str] = set(entry.get("tags", []))
            tags.add(entry_builder._slugify(entity_type, max_len=20))
            source_url = entry.get("source_url", "")
            items.append(ParsedItem(
                title=title,
                type=entity_type,
                year=year,
                names=names,
                summary=summary,
                domains=domains,
                tags=sorted(t for t in tags if t),
                source_url=source_url,
                source_type="website",
                raw=entry,
            ))
        return items
