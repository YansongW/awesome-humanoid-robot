#!/usr/bin/env python3
"""Build has_prerequisite learning-chain edges among roadmap-bound entities.

For each entity bound to a roadmap stage, DeepSeek picks its prerequisites
from entities bound to earlier-or-equal stages (natural curriculum order).
Edges: type=has_prerequisite, rule p7_learning_chain, confidence medium,
evidence = LLM reason. Idempotent via existing-pair skip + progress file.

Usage:
    python scripts/build_learning_chain.py            # dry-run
    python scripts/build_learning_chain.py --write
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(Path(__file__).parent))
from build_latent_relationships import load_entities, load_existing_pairs, make_rel, dump_rel  # noqa: E402
from link_zero_degree_entities import call_deepseek  # noqa: E402

PROGRESS = ROOT / ".staging" / "learning_chain_progress.jsonl"
STAGE_ORDER = ["stage-0-foundations", "stage-1-actuator", "stage-2-biped", "stage-3-humanoid"]

PROMPT = """You are building the prerequisite chain of a humanoid-robot learning roadmap.
For each entity below (the "learner's topic"), choose which OTHER entities from its candidate list
are direct prerequisites — things you must understand FIRST to learn this topic well.
Rules:
- Only pick from the candidate IDs listed for that entity.
- 0-3 prerequisites per entity; pick none if the topic is foundational.
- Do NOT pick prerequisites that are clearly more advanced than the topic itself.

Return ONLY a JSON array:
[{{"i": 0, "prereqs": [{{"id": "ent_...", "reason_zh": "一句中文理由", "reason_en": "one English reason"}}]}}, ...]

Entities (i. id | type | stage | summary):
{items}

Candidate pools (stage -> id=name):
{pools}"""


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--write", action="store_true")
    ap.add_argument("--workers", type=int, default=3)
    args = ap.parse_args()

    mapping = yaml.safe_load((ROOT / "data" / "roadmap_mapping.yaml").read_text(encoding="utf-8"))
    bindings = mapping["entities"]
    ents = load_entities()

    # summaries
    for p in sorted(ROOT.glob("research/**/*.md")):
        m = re.match(r"\A---\n(.*?)\n---\n", p.read_text(encoding="utf-8"), re.S)
        if not m:
            continue
        try:
            fm = yaml.safe_load(m.group(1))
        except yaml.YAMLError:
            continue
        if isinstance(fm, dict) and fm.get("$id") in ents:
            ents[fm["$id"]]["summary_en"] = (fm.get("summary") or {}).get("en", "")

    # stage -> entity list (bound entities only, existing in KG)
    stage_ents: dict[str, list[str]] = {s: [] for s in STAGE_ORDER}
    ent_stage: dict[str, int] = {}
    for eid, bl in bindings.items():
        if eid not in ents:
            continue
        best = min(STAGE_ORDER.index(b["stage"]) for b in bl if b["stage"] in STAGE_ORDER)
        ent_stage[eid] = best
        stage_ents[STAGE_ORDER[best]].append(eid)

    pools_text = "\n".join(
        f"{s}: " + "; ".join(f"{e}={ents[e]['name_en'][:36]}" for e in stage_ents[s][:60])
        for s in STAGE_ORDER
    )

    done = set()
    if PROGRESS.exists():
        for line in PROGRESS.read_text(encoding="utf-8").splitlines():
            if line.strip():
                done.add(json.loads(line)["entity_id"])
    todo = [e for e in ent_stage if e not in done]
    print(f"bound entities={len(ent_stage)} done={len(done)} todo={len(todo)}")

    batches = [todo[i:i + 10] for i in range(0, len(todo), 10)]

    def process(batch):
        items = []
        for j, eid in enumerate(batch):
            e = ents[eid]
            stage = STAGE_ORDER[ent_stage[eid]]
            items.append(f"{j}. {eid} | {e['type']} | {stage} | {(e.get('summary_en') or '')[:150]}")
        out = call_deepseek(PROMPT.format(items="\n".join(items), pools=pools_text))
        results = []
        m = re.search(r"\[.*\]", out or "", re.S)
        arr = None
        if m:
            try:
                arr = json.loads(m.group(0))
            except json.JSONDecodeError:
                arr = None
        for j, eid in enumerate(batch):
            prereqs = []
            if arr:
                for obj in arr:
                    if isinstance(obj, dict) and obj.get("i") == j:
                        prereqs = obj.get("prereqs") or []
                        break
            # validate: candidate must be a bound entity at earlier-or-equal stage
            valid = []
            for pr in prereqs:
                pid = pr.get("id") if isinstance(pr, dict) else None
                if pid in ent_stage and pid != eid and ent_stage[pid] <= ent_stage[eid]:
                    valid.append(pr)
            results.append({"entity_id": eid, "prereqs": valid[:3]})
        return results

    existing = load_existing_pairs()
    out_rels: dict[str, dict] = {}
    linked = 0
    PROGRESS.parent.mkdir(exist_ok=True)
    with PROGRESS.open("a", encoding="utf-8") as pf:
        with ThreadPoolExecutor(max_workers=args.workers) as ex:
            for k, res in enumerate(ex.map(process, batches)):
                for r in res:
                    pf.write(json.dumps(r, ensure_ascii=False) + "\n")
                pf.flush()
                if not args.write:
                    continue
                for r in res:
                    eid = r["entity_id"]
                    for pr in r["prereqs"]:
                        pid = pr["id"]
                        if (eid, pid) in existing:
                            continue
                        reason = pr.get("reason_zh") or pr.get("reason_en") or ""
                        rel = make_rel(ents[eid], ents[pid], "has_prerequisite", "p7_learning_chain",
                                       "medium", reason[:300],
                                       "https://kg.rounds-tech.com/roadmap/", "0→1 路线图学习链")
                        if rel["$id"] not in out_rels:
                            out_rels[rel["$id"]] = rel
                            existing.add((eid, pid))
                            linked += 1
                print(f"  batch {k + 1}/{len(batches)} linked={linked}")

    print(f"prerequisite edges: {linked if args.write else 'dry-run'}")
    if args.write:
        rel_dir = ROOT / "data" / "relationships"
        for rel in out_rels.values():
            (rel_dir / f"{rel['$id']}.md").write_text(dump_rel(rel), encoding="utf-8")
        print(f"wrote {len(out_rels)} files")
    else:
        shown = 0
        for line in PROGRESS.read_text(encoding="utf-8").splitlines()[-len(todo):]:
            r = json.loads(line)
            for pr in r["prereqs"]:
                print(" ", r["entity_id"][:45], "<-", pr["id"][:40], "|", (pr.get("reason_zh") or "")[:60])
                shown += 1
                if shown >= 10:
                    return


if __name__ == "__main__":
    main()
