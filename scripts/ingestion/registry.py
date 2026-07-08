"""Source registry: load/save data/sources.yaml."""

from __future__ import annotations

from dataclasses import asdict
from pathlib import Path
from typing import Any

import yaml

from ai4sci_lib import config

from .core import Source


REGISTRY_PATH = config.ROOT / "data" / "sources.yaml"


class Registry:
    """Manage the source registry file."""

    def __init__(self, path: Path | None = None) -> None:
        self.path = path or REGISTRY_PATH
        self._data: dict[str, Any] = {"version": 1, "sources": []}
        self._load()

    def _load(self) -> None:
        if not self.path.exists():
            return
        try:
            self._data = yaml.safe_load(self.path.read_text(encoding="utf-8")) or {"version": 1, "sources": []}
        except Exception:
            self._data = {"version": 1, "sources": []}

    def save(self) -> None:
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self.path.write_text(yaml.dump(self._data, sort_keys=False, allow_unicode=True, default_flow_style=False), encoding="utf-8")

    def list_sources(self, enabled_only: bool = False) -> list[Source]:
        sources: list[Source] = []
        for raw in self._data.get("sources", []):
            if enabled_only and not raw.get("enabled", True):
                continue
            sources.append(self._to_source(raw))
        return sources

    def get(self, source_id: str) -> Source | None:
        for raw in self._data.get("sources", []):
            if raw.get("id") == source_id:
                return self._to_source(raw)
        return None

    def update_stats(
        self,
        source_id: str,
        added: int = 0,
        duplicates: int = 0,
        status: str | None = None,
    ) -> None:
        for raw in self._data.get("sources", []):
            if raw.get("id") != source_id:
                continue
            from datetime import datetime
            raw["last_run"] = datetime.utcnow().isoformat() + "Z"
            raw["total_added"] = raw.get("total_added", 0) + added
            raw["total_duplicates"] = raw.get("total_duplicates", 0) + duplicates
            if status:
                raw["status"] = status
            break
        self.save()

    def ensure_source(self, source: Source) -> None:
        """Add a source if it does not already exist."""
        if self.get(source.id) is not None:
            return
        raw = {k: v for k, v in asdict(source).items() if v is not None and v != ""}
        self._data.setdefault("sources", []).append(raw)
        self.save()

    @staticmethod
    def _to_source(raw: dict[str, Any]) -> Source:
        return Source(
            id=raw["id"],
            name=raw["name"],
            type=raw["type"],
            url=raw["url"],
            enabled=raw.get("enabled", True),
            schedule=raw.get("schedule", "on_demand"),
            keywords=raw.get("keywords", []),
            fetch_url=raw.get("fetch_url", ""),
            extra=raw.get("extra", {}),
            last_run=raw.get("last_run"),
            total_added=raw.get("total_added", 0),
            total_duplicates=raw.get("total_duplicates", 0),
            status=raw.get("status", "pending"),
        )
