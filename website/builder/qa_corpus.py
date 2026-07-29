"""Build the client-side Q&A corpus for the BYOK ask page.

One JSON record per entry: enough text for RAG context (summary + truncated
body + 1-hop relations) without shipping the full Markdown source.
"""

from __future__ import annotations

from typing import Any

from website.builder.loader import KGStore

MAX_BODY_CHARS = 1200
MAX_RELATIONS_PER_DIRECTION = 5


def build_qa_corpus(store: KGStore) -> dict[str, Any]:
    """Return {entry_id: {id, name, name_en, type, summary, body, relations}}."""
    corpus: dict[str, Any] = {}
    for e in store.entries.values():
        body = (e.body or "").strip()
        if len(body) > MAX_BODY_CHARS:
            body = body[:MAX_BODY_CHARS] + "…"
        relations = []
        for rel in store.outgoing.get(e.id, [])[:MAX_RELATIONS_PER_DIRECTION]:
            relations.append({
                "direction": "out",
                "type": rel.type,
                "other_id": rel.target_id,
                "other_name": rel.target_name,
            })
        for rel in store.incoming.get(e.id, [])[:MAX_RELATIONS_PER_DIRECTION]:
            relations.append({
                "direction": "in",
                "type": rel.type,
                "other_id": rel.source_id,
                "other_name": rel.source_name,
            })
        corpus[e.id] = {
            "id": e.id,
            "name": e.name,
            "name_en": e.name_en,
            "type": e.type,
            "summary": e.summary,
            "body": body,
            "relations": relations,
        }
    return corpus
