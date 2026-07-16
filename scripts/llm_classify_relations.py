#!/usr/bin/env python3
"""Type queued entity-mention pairs with DeepSeek (Phase 1.2).

Reads .staging/llm_relation_queue.jsonl (produced by build_latent_relationships.py),
asks the LLM to pick a relation type per pair (or "none"), and writes typed
relationship files to data/relationships/.

Idempotent: progress is checkpointed to .staging/llm_relation_progress.jsonl;
re-running skips pairs already classified.

Usage:
    python scripts/llm_classify_relations.py            # dry-run report
    python scripts/llm_classify_relations.py --write
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys
from concurrent.futures import ThreadPoolExecutor
from datetime import date
from pathlib import Path

import requests
import yaml

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(Path(__file__).parent))
from build_latent_relationships import load_entities, load_existing_pairs, make_rel, dump_rel, VERB  # noqa: E402

TODAY = date.today().isoformat()
API_URL = "https://api.deepseek.com/chat/completions"
API_KEY = os.environ.get("DEEPSEEK_API_KEY") or (
    Path.home() / "Desktop" / ".ai_credentials.txt"
).read_text(encoding="utf-8").split("DEEPSEEK_API_KEY=")[1].split("\n")[0].strip()

QUEUE = ROOT / ".staging" / "llm_relation_queue.jsonl"
PROGRESS = ROOT / ".staging" / "llm_relation_progress.jsonl"

ALLOWED_TYPES = [
    "uses", "uses_hardware_from", "uses_software", "uses_simulator", "uses_dataset",
    "uses_benchmark", "is_based_on", "builds_on", "extends", "compares_with",
    "is_alternative_to", "has_prerequisite", "is_prerequisite_for", "evaluates_on",
    "evaluated_in", "demonstrates_on", "produces", "develops", "developed_by",
    "manufactured_by", "is_part_of", "is_subsystem_of", "enables", "requires",
    "integrates", "implements_on", "cites", "mentions", "none",
]

PROMPT = """You are classifying relationships in a humanoid-robot knowledge graph.
For each item, decide the relationship type FROM source TO target, based ONLY on the evidence sentence.
Allowed types:
{types}

Rules:
- Choose "none" if the evidence does not support any clear directed relationship (e.g. both are merely listed together).
- "mentions" only when the source clearly refers to the target but no stronger type fits.
- Direction matters: "uses" = source uses target; "developed_by" = source is developed by target.

Return a JSON array, one object per item, in order:
[{{"i": 0, "type": "uses", "reason_zh": "一句中文理由", "reason_en": "one English reason"}}, ...]
Return ONLY the JSON array.

Items:
{items}"""


def call_deepseek(prompt: str, retries: int = 2) -> str | None:
    headers = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}
    payload = {"model": "deepseek-chat", "temperature": 0.0,
               "messages": [{"role": "user", "content": prompt}]}
    for _ in range(retries + 1):
        try:
            resp = requests.post(API_URL, headers=headers, json=payload, timeout=120)
            if resp.status_code == 200:
                return resp.json()["choices"][0]["message"]["content"]
        except Exception:
            pass
    return None


def parse_json_array(text: str) -> list | None:
    m = re.search(r"\[.*\]", text or "", re.S)
    if not m:
        return None
    try:
        arr = json.loads(m.group(0))
        return arr if isinstance(arr, list) else None
    except json.JSONDecodeError:
        return None


def classify_batch(batch: list[dict]) -> list[dict]:
    items = "\n".join(
        f"{j}. source={b['source_name']} (type={b['source_type']}) | target={b['target_name']} "
        f"(type={b['target_type']}) | evidence: {b['evidence'][:250]}"
        for j, b in enumerate(batch)
    )
    out = call_deepseek(PROMPT.format(types=", ".join(ALLOWED_TYPES), items=items))
    arr = parse_json_array(out or "")
    results = []
    for j, b in enumerate(batch):
        verdict = None
        if arr:
            for obj in arr:
                if isinstance(obj, dict) and obj.get("i") == j:
                    verdict = obj
                    break
        rtype = (verdict or {}).get("type", "none")
        if rtype not in ALLOWED_TYPES:
            rtype = "none"
        results.append({
            **b,
            "rel_type": rtype,
            "reason_zh": (verdict or {}).get("reason_zh", ""),
            "reason_en": (verdict or {}).get("reason_en", ""),
        })
    return results


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--write", action="store_true")
    ap.add_argument("--workers", type=int, default=4)
    ap.add_argument("--batch", type=int, default=10)
    ap.add_argument("--limit", type=int, default=0, help="only process first N batches (smoke test)")
    args = ap.parse_args()

    queue = [json.loads(l) for l in QUEUE.read_text(encoding="utf-8").splitlines() if l.strip()]
    done = set()
    if PROGRESS.exists():
        for l in PROGRESS.read_text(encoding="utf-8").splitlines():
            if l.strip():
                r = json.loads(l)
                done.add((r["source_id"], r["target_id"]))
    todo = [q for q in queue if (q["source_id"], q["target_id"]) not in done]
    print(f"queue={len(queue)} done={len(done)} todo={len(todo)}")

    batches = [todo[i:i + args.batch] for i in range(0, len(todo), args.batch)]
    if args.limit:
        batches = batches[:args.limit]
    results: list[dict] = []
    with PROGRESS.open("a", encoding="utf-8") as pf:
        with ThreadPoolExecutor(max_workers=args.workers) as ex:
            for k, res in enumerate(ex.map(classify_batch, batches)):
                for r in res:
                    pf.write(json.dumps(r, ensure_ascii=False) + "\n")
                pf.flush()
                results.extend(res)
                if (k + 1) % 5 == 0:
                    print(f"  {k + 1}/{len(batches)} batches")

    typed = [r for r in results if r["rel_type"] != "none"]
    print(f"classified: typed={len(typed)} none={len(results) - len(typed)}")

    if not args.write:
        from collections import Counter
        print("type distribution:", dict(Counter(r["rel_type"] for r in typed)))
        for r in typed[:5]:
            print(" ", r["rel_type"], "|", r["source_name"][:40], "->", r["target_name"][:40],
                  "|", (r["reason_zh"] or r["reason_en"])[:80])
        print("dry-run; re-run with --write to apply")
        return

    ents = load_entities()
    existing = load_existing_pairs()
    rel_dir = ROOT / "data" / "relationships"
    written = skipped = 0
    for r in typed:
        sid, tid, rtype = r["source_id"], r["target_id"], r["rel_type"]
        if sid not in ents or tid not in ents or (sid, tid) in existing:
            skipped += 1
            continue
        reason = r["reason_zh"] or r["reason_en"] or r["evidence"][:200]
        rel = make_rel(ents[sid], ents[tid], rtype, "p3_llm_typed", "medium",
                       f"{reason} | 证据: {r['evidence'][:250]}",
                       f"https://kg.rounds-tech.com/entry/{sid}/", f"KG body of {sid}")
        (rel_dir / f"{rel['$id']}.md").write_text(dump_rel(rel), encoding="utf-8")
        existing.add((sid, tid))
        written += 1
    print(f"wrote {written} relationship files, skipped {skipped}")


if __name__ == "__main__":
    main()
