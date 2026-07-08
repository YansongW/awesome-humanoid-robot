"""Central deduplication service for ingestion."""

from __future__ import annotations

import re
from pathlib import Path
from typing import Any

import yaml

from ai4sci_lib import config


class DedupService:
    """Normalize titles and detect duplicates across production and staging."""

    def __init__(self, search_dirs: list[Path] | None = None) -> None:
        self.search_dirs = search_dirs or [
            config.RESEARCH_DIR,
            config.RELATIONSHIPS_DIR,
            config.STAGING_DIR / "research",
            config.STAGING_DIR / "data" / "relationships",
        ]
        self.titles: set[str] = set()
        self.arxiv_ids: set[str] = set()
        self.urls: set[str] = set()
        self._load()

    @staticmethod
    def normalize_title(title: str) -> str:
        """Create a stable dedup key from a title."""
        t = title.lower()
        # remove URLs/markup artifacts
        t = re.sub(r"https?://\S+", "", t)
        # remove leading numbering and markdown heading markers
        t = re.sub(r"^(#{0,4}\s+|\d+[\.、]\s*)", "", t)
        # remove punctuation except alphanumeric and spaces
        t = re.sub(r"[^\w\s]", " ", t)
        # collapse whitespace
        t = re.sub(r"\s+", " ", t).strip()
        return t

    def _load(self) -> None:
        for base in self.search_dirs:
            if not base.exists():
                continue
            globber = base.rglob if base.is_dir() and not base.name.endswith(".md") else base.glob
            for path in globber("*.md"):
                try:
                    text = path.read_text(encoding="utf-8")
                    if not text.startswith("---"):
                        continue
                    _, rest = text.split("---", 1)
                    yaml_text, _ = rest.split("---", 1)
                    data = yaml.safe_load(yaml_text) or {}
                    names = data.get("names", {})
                    if isinstance(names, dict):
                        for v in names.values():
                            if v:
                                self.titles.add(self.normalize_title(v))
                    for src in data.get("sources", []):
                        url = str(src.get("url", "")).strip()
                        if url:
                            self.urls.add(url)
                        m = re.search(r"arxiv\.org/abs/(\d+\.\d+)", url)
                        if m:
                            self.arxiv_ids.add(m.group(1))
                except Exception:
                    continue

    def check(self, item_title: str, arxiv_id: str = "", source_url: str = "") -> tuple[bool, str]:
        """Return (is_duplicate, reason)."""
        norm = self.normalize_title(item_title)
        if norm and norm in self.titles:
            return True, "duplicate_title"
        if arxiv_id and arxiv_id in self.arxiv_ids:
            return True, "duplicate_arxiv"
        if source_url and source_url in self.urls:
            return True, "duplicate_url"
        return False, ""

    def add(self, item_title: str, arxiv_id: str = "", source_url: str = "") -> None:
        """Register a newly written item so later items in the same batch dedup."""
        norm = self.normalize_title(item_title)
        if norm:
            self.titles.add(norm)
        if arxiv_id:
            self.arxiv_ids.add(arxiv_id)
        if source_url:
            self.urls.add(source_url)
