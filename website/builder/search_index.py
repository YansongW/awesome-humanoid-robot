"""Generate compact search index for client-side search."""

from __future__ import annotations

from typing import Any

from website.builder.loader import Entry, tokenize


def build_search_index(entries: dict[str, Entry]) -> dict[str, Any]:
    """Build a compact inverted index for Fuse.js or custom search.

    Returns:
        {
            "entries": [
                {"id": ..., "name": ..., "name_en": ..., "type": ..., "summary": ..., "domains": [...], "layers": [...], "url": ...},
                ...
            ],
            "index": {"token": [entry_index, ...], ...}
        }
    """
    entry_list = sorted(entries.values(), key=lambda e: e.name or e.id)
    compact = []
    for e in entry_list:
        compact.append(
            {
                "id": e.id,
                "name": e.name,
                "name_en": e.name_en,
                "type": e.type,
                "summary": e.summary,
                "domains": e.domains,
                "layers": e.layers,
                "url": e.url,
            }
        )

    inverted: dict[str, set[int]] = {}
    for idx, e in enumerate(entry_list):
        tokens = set()
        tokens.update(tokenize(e.id))
        tokens.update(tokenize(e.name))
        tokens.update(tokenize(e.name_en))
        tokens.update(tokenize(e.summary))
        tokens.update(tokenize(e.type))
        tokens.update(d.lower() for d in e.domains)
        tokens.update(t.lower() for t in e.tags)
        for tok in tokens:
            inverted.setdefault(tok, set()).add(idx)

    return {
        "entries": compact,
        "index": {k: sorted(v) for k, v in inverted.items()},
    }


def build_relations_data(entries: dict[str, Entry], relationships: list) -> dict:
    """Build graph data for Cytoscape.js."""
    nodes = []
    for e in entries.values():
        nodes.append(
            {
                "data": {
                    "id": e.id,
                    "name": e.name or e.id,
                    "type": e.type,
                    "domains": e.domains,
                }
            }
        )
    edges = []
    seen_edges = set()
    for rel in relationships:
        if rel.source_id not in entries or rel.target_id not in entries:
            continue
        edge_key = (rel.source_id, rel.target_id, rel.type)
        if edge_key in seen_edges:
            continue
        seen_edges.add(edge_key)
        edges.append(
            {
                "data": {
                    "id": rel.id,
                    "source": rel.source_id,
                    "target": rel.target_id,
                    "type": rel.type,
                    "description": rel.description,
                }
            }
        )
    return {"nodes": nodes, "edges": edges}
