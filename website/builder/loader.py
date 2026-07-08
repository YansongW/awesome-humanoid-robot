"""Load entries and relationships from the knowledge graph Markdown files."""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

import yaml

ROOT = Path(__file__).resolve().parent.parent.parent
RESEARCH_DIR = ROOT / "research"
RELATIONSHIPS_DIR = ROOT / "data" / "relationships"


def split_frontmatter(text: str) -> tuple[dict[str, Any], str]:
    """Split Markdown frontmatter from body."""
    if not text.startswith("---"):
        return {}, text
    parts = text.split("---", 2)
    if len(parts) < 3:
        return {}, text
    try:
        front = yaml.safe_load(parts[1]) or {}
    except Exception:
        front = {}
    return front, parts[2].strip()


def pick_lang(value: Any, lang: str = "zh") -> str:
    """Pick a language value from a dict or return string."""
    if isinstance(value, dict):
        return value.get(lang) or value.get("en") or value.get("ko") or ""
    return str(value or "")


def tokenize(text: str) -> list[str]:
    """Tokenize text for search; English words and Chinese characters."""
    text = text or ""
    tokens: list[str] = []
    for part in re.findall(r"[a-zA-Z0-9]+|[\u4e00-\u9fff]", text):
        if part[0].isascii():
            tokens.append(part.lower())
        else:
            tokens.extend(list(part.lower()))
    return tokens


@dataclass
class Entry:
    id: str
    type: str
    name: str
    name_en: str
    summary: str
    domains: list[str]
    layers: list[str]
    tags: list[str]
    body: str
    body_html: str
    frontmatter: dict[str, Any]
    path: Path

    @property
    def url(self) -> str:
        return f"entry/{self.id}/"


@dataclass
class Relationship:
    id: str
    type: str
    source_id: str
    target_id: str
    source_name: str
    target_name: str
    description: str


@dataclass
class KGStore:
    entries: dict[str, Entry] = field(default_factory=dict)
    relationships: list[Relationship] = field(default_factory=list)
    outgoing: dict[str, list[Relationship]] = field(default_factory=dict)
    incoming: dict[str, list[Relationship]] = field(default_factory=dict)

    def load(self) -> None:
        self.entries.clear()
        self.relationships.clear()
        self.outgoing.clear()
        self.incoming.clear()

        import markdown

        md = markdown.Markdown(extensions=["extra", "toc"])

        for path in RESEARCH_DIR.rglob("*.md"):
            text = path.read_text(encoding="utf-8")
            front, body = split_frontmatter(text)
            eid = front.get("$id")
            if not eid:
                continue

            names = front.get("names", {})
            summaries = front.get("summary", {})
            entry = Entry(
                id=str(eid),
                type=front.get("type", "unknown"),
                name=pick_lang(names, "zh"),
                name_en=pick_lang(names, "en"),
                summary=pick_lang(summaries, "zh"),
                domains=front.get("domains", []) or [],
                layers=front.get("layers", []) or [],
                tags=front.get("tags", []) or [],
                body=body,
                body_html=md.convert(body),
                frontmatter=front,
                path=path,
            )
            md.reset()
            self.entries[entry.id] = entry

        if RELATIONSHIPS_DIR.exists():
            for path in RELATIONSHIPS_DIR.rglob("*.md"):
                text = path.read_text(encoding="utf-8")
                front, _ = split_frontmatter(text)
                rid = front.get("$id")
                if not rid:
                    continue
                source = front.get("source", {}) or {}
                target = front.get("target", {}) or {}
                source_id = source.get("id", "") if isinstance(source, dict) else ""
                target_id = target.get("id", "") if isinstance(target, dict) else ""
                description = pick_lang(front.get("description", {}), "zh")

                rel = Relationship(
                    id=str(rid),
                    type=front.get("type", "unknown"),
                    source_id=source_id,
                    target_id=target_id,
                    source_name=self.entries.get(source_id, Entry(id=source_id, type="", name=source_id, name_en="", summary="", domains=[], layers=[], tags=[], body="", body_html="", frontmatter={}, path=Path())).name,
                    target_name=self.entries.get(target_id, Entry(id=target_id, type="", name=target_id, name_en="", summary="", domains=[], layers=[], tags=[], body="", body_html="", frontmatter={}, path=Path())).name,
                    description=description,
                )
                self.relationships.append(rel)
                self.outgoing.setdefault(source_id, []).append(rel)
                self.incoming.setdefault(target_id, []).append(rel)

    def related_entries(self, eid: str) -> list[Entry]:
        ids = set()
        for rel in self.outgoing.get(eid, []) + self.incoming.get(eid, []):
            ids.add(rel.source_id if rel.source_id != eid else rel.target_id)
        return [self.entries[i] for i in ids if i in self.entries and i != eid]
