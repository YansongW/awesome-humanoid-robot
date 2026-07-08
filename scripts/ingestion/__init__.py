"""Unified ingestion framework for external sources into the knowledge graph."""

from .core import Source, ParsedItem, IngestionResult
from .registry import Registry
from .dedup import DedupService
from .writer import EntryWriter

__all__ = [
    "Source",
    "ParsedItem",
    "IngestionResult",
    "Registry",
    "DedupService",
    "EntryWriter",
]
