#!/usr/bin/env python3
"""Link zero-degree entities into the graph (Phase 1.3 gap-closer).

Deterministic rules (default):
  P5a  summary/body verb patterns ("introduced by X", "developed by X") matched
       against org-type entities -> developed_by
  P5b  acronym name index (3-8 chars, uppercase-heavy, word-boundary,
       case-sensitive, incl. parenthesized aliases) -> cites (in 参考) / mentions

LLM mode (--llm):
  P6   for entities still at degree 0, DeepSeek picks up to 3 relationships
       from a domain-filtered candidate list (validated IDs only).
       Checkpointed to .staging/llm_link_progress.jsonl; idempotent.

Usage:
    python scripts/link_zero_degree_entities.py            # deterministic dry-run
    python scripts/link_zero_degree_entities.py --write
    python scripts/link_zero_degree_entities.py --llm      # LLM dry-run
    python scripts/link_zero_degree_entities.py --llm --write
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys
from collections import Counter, defaultdict
from concurrent.futures import ThreadPoolExecutor
from datetime import date
from pathlib import Path

import requests

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(Path(__file__).parent))
from build_latent_relationships import (  # noqa: E402
    load_entities, load_existing_pairs, make_rel, dump_rel,
    build_name_index, find_mentions, in_reference_section,
)

TODAY = date.today().isoformat()
API_URL = "https://api.deepseek.com/chat/completions"
PROGRESS = ROOT / ".staging" / "llm_link_progress.jsonl"

ORG_TYPES = {"company", "oem", "component_manufacturer", "tier1_supplier"}
PAPER_LIKE = {"paper", "report"}

NEWS_TITLE_RE = re.compile(
    r"\b(Launches|Unveils|Selects|Secures|Closes|Enters|Announces|Raises|Partners|"
    r"Expands|Debuts|Introduces|Builds|Ships|Opens|Wins|Signs|Scales|Joins|Acquires)\b"
    r"|[\$':]")

ACRONYM_STOP = {
    "NOTE", "TODO", "IEEE", "ARXIV", "HTTP", "HTTPS", "PDF", "HTML", "URL", "DOI",
    "ETC", "FIG", "TABLE", "APP", "VOL", "ISBN", "ISSN", "INTRO", "ABSTRACT",
    "CONCLUSION", "RESULTS", "METHODS", "RELATED", "WORK", "TRUE", "FALSE",
    "NULL", "NONE", "TODO", "WIP", "TBD", "FAQ", "BOM", "CAD", "STEP", "STL",
    "USB", "LED", "PCB", "CNC", "DIY", "KIT", "MAX", "MIN", "AVG", "STD",
}

ORG_VERB_RE = re.compile(
    r"(?:introduced|developed|proposed|created|built|designed|released|led|published|presented)"
    r"\s+by\s+([A-Z][A-Za-z0-9 ,&'\-\.]{2,90}?)(?=[\.\,;]| (?:and|in|at|for|with|is|was)\b|$)",
)

PAPER_TYPES_WHITELIST = [
    "proposes", "introduces", "studies", "discusses", "uses", "evaluates_on",
    "benchmarks", "cites", "extends", "is_based_on", "developed_by",
    "demonstrates_on", "mentions", "produces", "develops", "supplies",
    "manufactured_by", "is_regulated_by", "compares_with", "is_alternative_to",
    "is_version_of", "serves", "targets", "none",
]

# ------------------------------------------------------------ acronym index

def acronym_ok(name: str) -> bool:
    if not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9+\-]{2,7}", name):
        return False
    if name.upper() in ACRONYM_STOP:
        return False
    uppers = sum(1 for c in name if c.isupper())
    has_digit = any(c.isdigit() for c in name)
    return uppers >= 2 or (uppers >= 1 and has_digit)


def build_acronym_index(ents: dict[str, dict]) -> list[tuple[str, str]]:
    pairs = []
    for eid, e in ents.items():
        candidates = set()
        for nm in {e["name_en"], e["name_zh"]}:
            nm = (nm or "").strip()
            if acronym_ok(nm):
                candidates.add(nm)
            m = re.search(r"\(([A-Za-z0-9][A-Za-z0-9+\-]{2,7})\)", nm)
            if m and acronym_ok(m.group(1)):
                candidates.add(m.group(1))
        for c in candidates:
            pairs.append((c, eid))
    pairs = list(dict.fromkeys(pairs))
    pairs.sort(key=lambda x: -len(x[0]))
    return pairs


WORD_RE_CACHE: dict[str, re.Pattern] = {}


def word_pattern(name: str) -> re.Pattern:
    if name not in WORD_RE_CACHE:
        WORD_RE_CACHE[name] = re.compile(r"(?<![A-Za-z0-9])" + re.escape(name) + r"(?![A-Za-z0-9])")
    return WORD_RE_CACHE[name]


def find_acronym_mentions(text: str, index: list[tuple[str, str]], own_id: str) -> dict[str, str]:
    hits: dict[str, str] = {}
    sentences = re.split(r"(?<=[。！？.!?\n])\s*", text)
    for sent in sentences:
        s = sent.strip()
        if len(s) < 10:
            continue
        for name, eid in index:
            if eid == own_id or eid in hits:
                continue
            if name in s and word_pattern(name).search(s):
                hits[eid] = s[:300]
    return hits

# --------------------------------------------------------------- rule P5a

def rule_org_verbs(ents, existing, out, stats):
    # Only clean org names: several company-type cards are news articles whose
    # names are full headlines — those must not become edge endpoints here.
    orgs = [(e["name_en"], eid) for eid, e in ents.items()
            if e["type"] in ORG_TYPES and e["name_en"]
            and len(e["name_en"]) <= 45 and not NEWS_TITLE_RE.search(e["name_en"])]
    for eid, e in ents.items():
        if e["type"] not in PAPER_LIKE:
            continue
        text = e.get("summary_en") or ""
        for m in ORG_VERB_RE.finditer(text):
            span = m.group(1)
            for oname, oid in orgs:
                if oid == eid or (eid, oid) in existing:
                    continue
                short = oname.split("(")[0].strip()
                if len(short) >= 4 and short in span:
                    rel = make_rel(e, ents[oid], "developed_by", "p5a_org_verb", "high",
                                   f"摘要载明 by {span.strip()[:120]}",
                                   f"https://kg.rounds-tech.com/entry/{eid}/", f"KG summary of {eid}")
                    out[rel["$id"]] = rel
                    existing.add((eid, oid))
                    stats["p5a"] += 1

# --------------------------------------------------------------- rule P5b

def rule_acronyms(ents, existing, out, stats):
    index = build_acronym_index(ents)
    for eid, e in ents.items():
        text = (e.get("summary_en") or "") + "\n" + e["body"]
        hits = find_acronym_mentions(text, index, eid)
        for tid, evidence in hits.items():
            if (eid, tid) in existing:
                continue
            if in_reference_section(e["body"], evidence):
                rtype, conf, rule = "cites", "medium", "p5b_acronym_ref"
            else:
                rtype, conf, rule = "mentions", "low", "p5b_acronym"
            rel = make_rel(e, ents[tid], rtype, rule, conf, evidence,
                           f"https://kg.rounds-tech.com/entry/{eid}/", f"KG body of {eid}")
            out[rel["$id"]] = rel
            existing.add((eid, tid))
            stats[rule] += 1

# ------------------------------------------------------------------ P6 LLM

def get_api_key() -> str:
    return os.environ.get("DEEPSEEK_API_KEY") or (
        Path.home() / "Desktop" / ".ai_credentials.txt"
    ).read_text(encoding="utf-8").split("DEEPSEEK_API_KEY=")[1].split("\n")[0].strip()


P6_PROMPT = """You are linking isolated entities in a humanoid-robot knowledge graph.
For each entity, choose up to 3 relationships FROM the entity TO a candidate entity.
Use ONLY candidate IDs from that entity's candidate list. Choose "none" if nothing fits.
Allowed types: {types}

Return ONLY a JSON array:
[{{"i": 0, "links": [{{"target_id": "ent_...", "type": "proposes", "reason_zh": "一句中文理由", "reason_en": "one English reason"}}]}}, ...]

Entities:
{items}"""


def call_deepseek(prompt: str, retries: int = 2) -> str | None:
    headers = {"Authorization": f"Bearer {get_api_key()}", "Content-Type": "application/json"}
    payload = {"model": "deepseek-chat", "temperature": 0.0,
               "messages": [{"role": "user", "content": prompt}]}
    for _ in range(retries + 1):
        try:
            resp = requests.post(API_URL, headers=headers, json=payload, timeout=180)
            if resp.status_code == 200:
                return resp.json()["choices"][0]["message"]["content"]
        except Exception:
            pass
    return None


def compute_degrees(existing_pairs):
    deg = Counter()
    for s, t in existing_pairs:
        deg[s] += 1
        deg[t] += 1
    return deg


def rule_llm_link(ents, existing, args, out, stats):
    degrees = compute_degrees(existing)
    include = set(args.include_types.split(",")) if args.include_types else None
    zero = [eid for eid in ents if degrees[eid] == 0 and (include is None or ents[eid]["type"] in include)]
    done = set()
    if PROGRESS.exists():
        for line in PROGRESS.read_text(encoding="utf-8").splitlines():
            if line.strip():
                done.add(json.loads(line)["entity_id"])
    todo = [eid for eid in zero if eid not in done]
    print(f"zero-degree={len(zero)} done={len(done)} todo={len(todo)}")
    if args.limit:
        todo = todo[: args.limit * args.batch]

    cand_types = {"method", "technology", "concept", "algorithm", "formalism", "principle",
                  "benchmark", "dataset", "robot_system", "software_platform", "component",
                  "company", "oem", "application_scenario", "standard"}
    cands_by_domain: dict[str, list[str]] = defaultdict(list)
    for eid, e in ents.items():
        if e["type"] in cand_types and degrees[eid] > 0:
            cands_by_domain[(e["domains"] or ["?"])[0]].append(eid)
    for d in cands_by_domain:
        cands_by_domain[d].sort(key=lambda i: -degrees[i])

    batches = [todo[i:i + args.batch] for i in range(0, len(todo), args.batch)]

    def process(batch):
        items, meta = [], []
        for j, eid in enumerate(batch):
            e = ents[eid]
            dom = (e["domains"] or ["?"])[0]
            cand_ids = cands_by_domain.get(dom, [])[:60]
            cand_str = "; ".join(f"{c}={ents[c]['name_en'][:40]}" for c in cand_ids)
            summary = (e.get("summary_en") or "")[:350]
            items.append(f"{j}. id={eid} | name={e['name_en'][:80]} | type={e['type']} | "
                         f"summary: {summary}\ncandidates: {cand_str}")
            meta.append((eid, set(cand_ids)))
        out_text = call_deepseek(P6_PROMPT.format(types=", ".join(PAPER_TYPES_WHITELIST),
                                                  items="\n\n".join(items)))
        results = []
        arr = None
        m = re.search(r"\[.*\]", out_text or "", re.S)
        if m:
            try:
                arr = json.loads(m.group(0))
            except json.JSONDecodeError:
                arr = None
        for j, (eid, cand_set) in enumerate(meta):
            links = []
            if arr:
                for obj in arr:
                    if isinstance(obj, dict) and obj.get("i") == j:
                        links = obj.get("links") or []
                        break
            valid = [l for l in links if isinstance(l, dict)
                     and l.get("target_id") in cand_set
                     and l.get("type") in PAPER_TYPES_WHITELIST
                     and l.get("type") != "none"][:3]
            results.append({"entity_id": eid, "links": valid})
        return results

    linked = 0
    PROGRESS.parent.mkdir(exist_ok=True)
    with PROGRESS.open("a", encoding="utf-8") as pf:
        with ThreadPoolExecutor(max_workers=args.workers) as ex:
            for k, res in enumerate(ex.map(process, batches)):
                for r in res:
                    pf.write(json.dumps(r, ensure_ascii=False) + "\n")
                    pf.flush()
                    eid = r["entity_id"]
                    for l in r["links"]:
                        tid = l["target_id"]
                        if (eid, tid) in existing:
                            continue
                        conf = "medium" if l["type"] != "mentions" else "low"
                        reason = l.get("reason_zh") or l.get("reason_en") or ""
                        rel = make_rel(ents[eid], ents[tid], l["type"], "p6_llm_link", conf,
                                       reason[:300],
                                       f"https://kg.rounds-tech.com/entry/{eid}/", f"KG body of {eid}")
                        key = rel["$id"]
                        if key not in out:
                            out[key] = rel
                            existing.add((eid, tid))
                            linked += 1
                if (k + 1) % 10 == 0:
                    print(f"  {k + 1}/{len(batches)} batches, linked={linked}")
    stats["p6_llm_link"] = linked

# -------------------------------------------------------------------- main

def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--write", action="store_true")
    ap.add_argument("--llm", action="store_true")
    ap.add_argument("--workers", type=int, default=4)
    ap.add_argument("--batch", type=int, default=8)
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--include-types", default="", help="comma-separated entity types to restrict LLM linking")
    args = ap.parse_args()

    ents = load_entities()
    # summaries are needed by P5a/P5b/P6; load_entities doesn't keep them — patch in
    for p in sorted(ROOT.glob("research/**/*.md")):
        text = p.read_text(encoding="utf-8")
        m = re.match(r"\A---\n(.*?)\n---\n", text, re.S)
        if not m:
            continue
        import yaml
        try:
            fm = yaml.safe_load(m.group(1))
        except yaml.YAMLError:
            continue
        if isinstance(fm, dict) and fm.get("$id") in ents:
            ents[fm["$id"]]["summary_en"] = (fm.get("summary") or {}).get("en", "")

    existing = load_existing_pairs()
    out: dict[str, dict] = {}
    stats: dict[str, int] = defaultdict(int)

    if args.llm:
        rule_llm_link(ents, existing, args, out, stats)
    else:
        rule_org_verbs(ents, existing, out, stats)
        rule_acronyms(ents, existing, out, stats)

    print("new relationships by rule:", dict(stats))
    print("total new:", len(out))

    if args.write:
        rel_dir = ROOT / "data" / "relationships"
        for rel in out.values():
            (rel_dir / f"{rel['$id']}.md").write_text(dump_rel(rel), encoding="utf-8")
        print(f"wrote {len(out)} files to data/relationships/")
    else:
        for rel in list(out.values())[:6]:
            print(" ", rel["type"], "|", rel["source"]["name"]["en"][:45], "->",
                  rel["target"]["name"]["en"][:45])
        print("dry-run; re-run with --write to apply")


if __name__ == "__main__":
    main()
