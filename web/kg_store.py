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
ROADMAP_MAPPING_FILE = ROOT / "data" / "roadmap_mapping.yaml"
ROADMAP_SITE = "https://kg.rounds-tech.com"


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
    roadmap_stages: list[dict[str, Any]] = field(default_factory=list)
    roadmap_stage_index: dict[str, dict[str, Any]] = field(default_factory=dict)
    roadmap_roles: dict[str, str] = field(default_factory=dict)
    roadmap_map: dict[str, list[dict[str, str]]] = field(default_factory=dict)

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

        self._load_roadmap()

    def _load_roadmap(self) -> None:
        self.roadmap_stages.clear()
        self.roadmap_stage_index.clear()
        self.roadmap_roles.clear()
        self.roadmap_map.clear()
        if not ROADMAP_MAPPING_FILE.exists():
            return
        try:
            data = yaml.safe_load(ROADMAP_MAPPING_FILE.read_text(encoding="utf-8")) or {}
        except Exception:
            return
        stages = data.get("stages", {}) or {}
        ordered = sorted(stages.items(), key=lambda kv: kv[1].get("order", 0))
        for stage_id, info in ordered:
            title = info.get("title", {}) or {}
            stage = {
                "id": stage_id,
                "order": info.get("order", 0),
                "title": title.get("zh") or title.get("en") or stage_id,
                "url": ROADMAP_SITE + info.get("url", ""),
            }
            self.roadmap_stages.append(stage)
            self.roadmap_stage_index[stage_id] = stage
        for role_id, info in (data.get("roles", {}) or {}).items():
            if isinstance(info, dict):
                self.roadmap_roles[role_id] = info.get("zh") or info.get("en") or role_id
            else:
                self.roadmap_roles[role_id] = str(info)
        for eid, bindings in (data.get("entities", {}) or {}).items():
            if isinstance(bindings, list):
                self.roadmap_map[eid] = [
                    {"stage": b.get("stage", ""), "role": b.get("role", "")}
                    for b in bindings
                    if isinstance(b, dict)
                ]

    def roadmap_badges(self, eid: str) -> list[dict[str, str]]:
        badges: list[dict[str, str]] = []
        for b in self.roadmap_map.get(eid, []):
            stage = self.roadmap_stage_index.get(b["stage"])
            if not stage:
                continue
            badges.append(
                {
                    "stage_id": stage["id"],
                    "stage_title": stage["title"],
                    "stage_url": stage["url"],
                    "role": b["role"],
                    "role_label": self.roadmap_roles.get(b["role"], b["role"]),
                }
            )
        return badges

    def roadmap_tree(self) -> list[dict[str, Any]]:
        tree: list[dict[str, Any]] = []
        role_order = {r: i for i, r in enumerate(self.roadmap_roles)}
        for stage in self.roadmap_stages:
            by_role: dict[str, list[Entry]] = {}
            for eid, bindings in self.roadmap_map.items():
                for b in bindings:
                    if b["stage"] == stage["id"]:
                        entry = self.entries.get(eid)
                        if entry:
                            by_role.setdefault(b["role"], []).append(entry)
            groups = [
                {
                    "role": role,
                    "role_label": self.roadmap_roles.get(role, role),
                    "entries": sorted(entries, key=lambda e: e.name or e.id),
                }
                for role, entries in sorted(
                    by_role.items(), key=lambda kv: role_order.get(kv[0], 99)
                )
            ]
            tree.append({**stage, "groups": groups})
        return tree

    def stats(self) -> dict[str, Any]:
        connected = set(self.outgoing) | set(self.incoming)
        zero_degree = sum(1 for eid in self.entries if eid not in connected)
        total = len(self.entries)
        return {
            "entries": total,
            "relationships": len(self.relationships),
            "zero_degree": zero_degree,
            "zero_degree_ratio": (zero_degree / total) if total else 0.0,
        }

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
