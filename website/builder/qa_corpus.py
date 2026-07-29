"""Build the client-side Q&A corpus for the BYOK ask page.

One JSON shard per primary domain (data/qa-corpus/<domain>.json) so the chat
panel only downloads the slices covering its retrieved entries instead of a
single multi-MB corpus. Domains whose shard would exceed MAX_SHARD_BYTES are
split further by entity type (<domain>--<type>.json); a tiny manifest.json
maps each domain to its shard files. Each record carries enough text for RAG
context (summary + truncated body + 1-hop relations).
"""

from __future__ import annotations

import json
from typing import Any

from website.builder.loader import KGStore

MAX_BODY_CHARS = 800
MAX_RELATIONS_PER_DIRECTION = 5
MAX_SHARD_BYTES = 900_000
UNKNOWN_DOMAIN = "unknown"


def _payload_bytes(records: dict) -> int:
    return len(json.dumps(records, ensure_ascii=False, separators=(",", ":")).encode("utf-8"))


def build_qa_corpus(store: KGStore) -> dict[str, Any]:
    """Return {"files": {filename: records}, "manifest": {domain: [filename]}}."""
    by_domain: dict[str, dict[str, Any]] = {}
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
        domain = e.domains[0] if e.domains else UNKNOWN_DOMAIN
        by_domain.setdefault(domain, {})[e.id] = {
            "id": e.id,
            "name": e.name,
            "name_en": e.name_en,
            "type": e.type,
            "summary": e.summary,
            "body": body,
            "relations": relations,
        }

    files: dict[str, dict] = {}
    manifest: dict[str, list[str]] = {}
    for domain, records in sorted(by_domain.items()):
        if _payload_bytes(records) <= MAX_SHARD_BYTES:
            fname = f"{domain}.json"
            files[fname] = records
            manifest[domain] = [fname]
            continue
        # Oversized domain: split by entity type; a type group that is still
        # oversized is split further into deterministic char-sum buckets (the
        # client recomputes the same bucket from the entry id).
        by_type: dict[str, dict] = {}
        for eid, rec in records.items():
            by_type.setdefault(rec["type"], {})[eid] = rec
        names = []
        for typ, recs in sorted(by_type.items()):
            typed = f"{domain}--{typ}"
            if _payload_bytes(recs) <= MAX_SHARD_BYTES:
                fname = f"{typed}.json"
                files[fname] = recs
                names.append(fname)
                continue
            n = -(-_payload_bytes(recs) // MAX_SHARD_BYTES)  # ceil
            buckets: list[dict] = [{} for _ in range(n)]
            for eid, rec in recs.items():
                buckets[sum(ord(c) for c in eid) % n][eid] = rec
            for i, bucket in enumerate(buckets):
                fname = f"{typed}--{i}.json"
                files[fname] = bucket
                names.append(fname)
        manifest[domain] = names
    return {"files": files, "manifest": manifest}

