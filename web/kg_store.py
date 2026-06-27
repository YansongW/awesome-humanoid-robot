"""In-memory knowledge graph store built from production Markdown entries."""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

import yaml

ROOT = Path(__file__).resolve().parent.parent
RESEARCH_DIR = ROOT / "research"
RELATIONSHIPS_DIR = ROOT / "data" / "relationships"


def _split_frontmatter(text: str) -> tuple[dict[str, Any], str]:
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


def _extract_summary(entry: dict[str, Any]) -> str:
    summary = entry.get("summary", {})
    if isinstance(summary, dict):
        return summary.get("zh") or summary.get("en", "")
    return str(summary)


def _extract_name(entry: dict[str, Any]) -> str:
    names = entry.get("names", {})
    if isinstance(names, dict):
        return names.get("zh") or names.get("en", "")
    return str(names)


def _tokenize(text: str) -> list[str]:
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
    summary: str
    domains: list[str]
    layers: list[str]
    body: str
    body_html: str
    frontmatter: dict[str, Any]
    path: Path


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
    index_tokens: dict[str, set[str]] = field(default_factory=dict)

    def load(self) -> None:
        self.entries.clear()
        self.relationships.clear()
        self.outgoing.clear()
        self.incoming.clear()
        self.index_tokens.clear()

        for path in RESEARCH_DIR.rglob("*.md"):
            text = path.read_text(encoding="utf-8")
            front, body = _split_frontmatter(text)
            eid = front.get("$id")
            if not eid:
                continue
            name = _extract_name(front)
            summary = _extract_summary(front)
            import markdown
            body_html = markdown.markdown(body, extensions=["extra", "toc"])
            entry = Entry(
                id=eid,
                type=front.get("type", "unknown"),
                name=name,
                summary=summary,
                domains=front.get("domains", []) or [],
                layers=front.get("layers", []) or [],
                body=body,
                body_html=body_html,
                frontmatter=front,
                path=path,
            )
            self.entries[eid] = entry
            tokens: set[str] = set()
            tokens.update(_tokenize(eid))
            tokens.update(_tokenize(name))
            tokens.update(_tokenize(summary))
            tokens.update(_tokenize(body))
            tokens.update(d.lower() for d in entry.domains)
            self.index_tokens[eid] = tokens

        if RELATIONSHIPS_DIR.exists():
            for path in RELATIONSHIPS_DIR.rglob("*.md"):
                text = path.read_text(encoding="utf-8")
                front, _ = _split_frontmatter(text)
                rid = front.get("$id")
                if not rid:
                    continue
                source = front.get("source", {})
                target = front.get("target", {})
                source_id = source.get("id", "") if isinstance(source, dict) else ""
                target_id = target.get("id", "") if isinstance(target, dict) else ""
                desc = front.get("description", {})
                if isinstance(desc, dict):
                    description = desc.get("zh") or desc.get("en", "")
                else:
                    description = str(desc)
                rel = Relationship(
                    id=rid,
                    type=front.get("type", "unknown"),
                    source_id=source_id,
                    target_id=target_id,
                    source_name=self.entries.get(source_id, Entry(id=source_id, type="", name=source_id, summary="", domains=[], layers=[], body="", body_html="", frontmatter={}, path=Path())).name,
                    target_name=self.entries.get(target_id, Entry(id=target_id, type="", name=target_id, summary="", domains=[], layers=[], body="", body_html="", frontmatter={}, path=Path())).name,
                    description=description,
                )
                self.relationships.append(rel)
                self.outgoing.setdefault(source_id, []).append(rel)
                self.incoming.setdefault(target_id, []).append(rel)

    def search(self, query: str, top_k: int = 10) -> list[Entry]:
        q = query.strip().lower()
        q_tokens = _tokenize(query)
        if not q and not q_tokens:
            return sorted(self.entries.values(), key=lambda e: e.name or e.id)[:top_k]
        scores: list[tuple[float, str]] = []
        for eid, entry in self.entries.items():
            score = 0.0
            name = (entry.name or "").lower()
            summary = (entry.summary or "").lower()
            body = (entry.body or "").lower()
            if q and q in name:
                score += 100
            if q and q in eid.lower():
                score += 80
            if q and q in summary:
                score += 40
            for t in q_tokens:
                if t in name:
                    score += 10
                if t in summary:
                    score += 5
                if t in body:
                    score += 1
            if score > 0:
                scores.append((score, eid))
        scores.sort(key=lambda x: x[0], reverse=True)
        seen = set()
        results = []
        for _, eid in scores:
            if eid not in seen:
                seen.add(eid)
                results.append(self.entries[eid])
            if len(results) >= top_k:
                break
        return results

    def get_entry(self, eid: str) -> Entry | None:
        return self.entries.get(eid)

    def related_entries(self, eid: str) -> list[Entry]:
        ids = set()
        for rel in self.outgoing.get(eid, []) + self.incoming.get(eid, []):
            ids.add(rel.source_id if rel.source_id != eid else rel.target_id)
        return [self.entries[i] for i in ids if i in self.entries and i != eid]


_store: KGStore | None = None


def get_store() -> KGStore:
    global _store
    if _store is None:
        _store = KGStore()
        _store.load()
    return _store
