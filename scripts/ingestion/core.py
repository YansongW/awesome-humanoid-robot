"""Core abstractions for the ingestion framework."""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any


@dataclass
class Source:
    """A configured external source."""

    id: str
    name: str
    type: str  # github_json, rss, api, wechat, curated_json, generic_rss
    url: str
    enabled: bool = True
    schedule: str = "on_demand"  # daily, weekly, on_demand
    keywords: list[str] = field(default_factory=list)
    fetch_url: str = ""
    extra: dict[str, Any] = field(default_factory=dict)
    # runtime stats (persisted in registry)
    last_run: str | None = None
    total_added: int = 0
    total_duplicates: int = 0
    status: str = "pending"


@dataclass
class ParsedItem:
    """A normalized item extracted from a source."""

    title: str
    type: str  # paper, report, dataset, benchmark, etc.
    year: str | int | None = None
    names: dict[str, str] = field(default_factory=dict)
    summary: dict[str, str] = field(default_factory=dict)
    domains: list[str] = field(default_factory=lambda: ["07_ai_models_algorithms"])
    layers: list[str] | None = None
    functional_roles: list[str] = field(default_factory=lambda: ["knowledge", "intelligence"])
    tags: list[str] = field(default_factory=list)
    theoretical_depth: list[str] = field(default_factory=lambda: ["system"])
    source_url: str = ""
    arxiv_id: str = ""
    source_type: str = "website"  # paper, website, report
    source_date: str = ""
    raw: dict[str, Any] = field(default_factory=dict)
    institution: str = ""

    def __post_init__(self) -> None:
        if not self.names:
            self.names = {"en": self.title, "zh": self.title, "ko": ""}
        if not self.summary:
            self.summary = {"en": self.title, "zh": self.title, "ko": ""}


@dataclass
class IngestionResult:
    """Result of attempting to ingest one ParsedItem."""

    source_id: str
    status: str  # added, duplicate, error, skipped
    item_title: str
    entry_id: str | None = None
    message: str = ""
