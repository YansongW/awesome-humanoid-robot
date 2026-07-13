"""Generate compact search index for client-side search."""

from __future__ import annotations

from collections import defaultdict
from typing import Any

from website.builder.loader import DOMAIN_LABELS, Entry, domain_label, tokenize, type_label


def _short_summary(summary: str, max_len: int = 90) -> str:
    """Return a short, single-line summary suitable for search result cards."""
    text = (summary or "").replace("\n", " ").replace("\r", " ")
    while "  " in text:
        text = text.replace("  ", " ")
    text = text.strip()
    if len(text) <= max_len:
        return text
    cut = text.rfind(" ", 0, max_len + 1)
    if cut <= 0:
        cut = max_len
    return text[:cut].rstrip() + "…"


def _field_tokens(text: str) -> list[str]:
    """Return unique, non-empty tokens for a text field."""
    tokens = tokenize(text or "")
    seen = set()
    out = []
    for t in tokens:
        if t and t not in seen:
            seen.add(t)
            out.append(t)
    return out


def build_search_index(entries: dict[str, Entry], lang: str = "zh") -> dict[str, Any]:
    """Build a compact client-side search index with an inverted token index.

    Returns:
        {
            "entries": [
                {"i": 0, "id": ..., "name": ..., "name_en": ..., "type": ..., "type_label": ..., "summary": ..., "domains": [...], "domain_labels": [...], "layers": [...], "url": ...},
                ...
            ],
            "index": {
                "pid": [0, 5, ...],   // token -> list of entry indices
                ...
            }
        }
    """
    entry_list = sorted(entries.values(), key=lambda e: e.name or e.id)
    compact: list[dict] = []
    inverted: dict[str, list[int]] = defaultdict(list)

    for idx, e in enumerate(entry_list):
        record = {
            "i": idx,
            "id": e.id,
            "name": e.name,
            "name_en": e.name_en,
            "type": e.type,
            "type_label": type_label(e.type, lang),
            "summary": _short_summary(e.summary),
            "domains": e.domains,
            "domain_labels": [domain_label(d, lang) for d in e.domains],
            "url": e.url,
        }
        compact.append(record)

        # Index tokens from high-signal fields only.  Summaries are kept in the
        # record for display and substring fallback scoring, but indexing every
        # summary token makes the inverted index too large.
        token_sources = [
            e.name,
            e.name_en,
            e.id,
            e.type,
            " ".join(e.domains),
        ]
        for src in token_sources:
            for t in _field_tokens(src):
                if idx not in inverted[t]:
                    inverted[t].append(idx)

    # Convert defaultdict to plain dict for JSON serialization.
    return {"entries": compact, "index": dict(inverted)}


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


def build_cluster_data(entries: dict[str, Entry], relationships: list) -> dict:
    """Build clustered graph data for performant overview visualization.

    Clusters by primary domain. Each cluster node contains the IDs of its
    members. Cluster-cluster edges aggregate cross-cluster relationships.
    """
    # Map each entity to its primary domain (first domain, fallback to type)
    entity_domain: dict[str, str] = {}
    for e in entries.values():
        entity_domain[e.id] = e.domains[0] if e.domains else f"type:{e.type}"

    # Collect clusters
    clusters: dict[str, dict] = {}
    for eid, domain in entity_domain.items():
        clusters.setdefault(
            domain,
            {"id": domain, "name": domain, "count": 0, "members": []},
        )
        clusters[domain]["count"] += 1
        clusters[domain]["members"].append(eid)

    # Aggregate edges between clusters
    cluster_edges: dict[tuple[str, str], int] = {}
    for rel in relationships:
        if rel.source_id not in entries or rel.target_id not in entries:
            continue
        src_domain = entity_domain.get(rel.source_id)
        tgt_domain = entity_domain.get(rel.target_id)
        if not src_domain or not tgt_domain or src_domain == tgt_domain:
            continue
        key = (src_domain, tgt_domain)
        cluster_edges[key] = cluster_edges.get(key, 0) + 1

    nodes = []
    for c in clusters.values():
        nodes.append(
            {
                "data": {
                    "id": c["id"],
                    "name": c["name"],
                    "count": c["count"],
                    "members": c["members"],
                    "isCluster": True,
                }
            }
        )

    edges = []
    for (src, tgt), weight in cluster_edges.items():
        edges.append(
            {
                "data": {
                    "id": f"{src}--{tgt}",
                    "source": src,
                    "target": tgt,
                    "weight": weight,
                    "isClusterEdge": True,
                }
            }
        )

    return {"nodes": nodes, "edges": edges}
