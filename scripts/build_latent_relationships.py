#!/usr/bin/env python3
"""Mine latent relationships from existing KG content (additive only).

Rules (notes field records the rule id so every batch is traceable/reversible):
  P0b  frontmatter related_entities without a standalone rel file
  P1   arXiv IDs in ## 参考 sections that resolve to existing entities -> cites
  P2   shared source URLs across entities -> typed edges (conservative)
  P3   entity-name mentions in bodies -> cites (in 参考) or LLM queue (elsewhere)
  P4   wiki chapters 9-30 same-section co-occurrence (core types) -> mentions

LLM-queued pairs are written to .staging/llm_relation_queue.jsonl for
scripts/llm_classify_relations.py — no untyped mention edges are created for them.

Usage:
    python scripts/build_latent_relationships.py            # dry-run report
    python scripts/build_latent_relationships.py --write
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from collections import defaultdict
from datetime import date
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
TODAY = date.today().isoformat()

CORE_TYPES = {"method", "technology", "concept", "benchmark", "dataset", "robot_system", "algorithm", "formalism", "principle", "operator"}
REF_TITLES = ("参考", "References", "참고")

# ---------------------------------------------------------------- loading

def split_file(text: str):
    m = re.match(r"\A---\n(.*?)\n---\n(.*)\Z", text, re.S)
    if not m:
        return None, None
    try:
        return yaml.safe_load(m.group(1)), m.group(2)
    except yaml.YAMLError:
        return None, None


def load_entities() -> dict[str, dict]:
    ents = {}
    for p in sorted(ROOT.glob("research/**/*.md")):
        fm, body = split_file(p.read_text(encoding="utf-8"))
        if not isinstance(fm, dict) or "$id" not in fm:
            continue
        names = fm.get("names", {}) or {}
        ents[fm["$id"]] = {
            "id": fm["$id"],
            "type": fm.get("type", "unknown"),
            "name_en": names.get("en", ""),
            "name_zh": names.get("zh", ""),
            "domains": fm.get("domains", []) or [],
            "body": body,
            "sources": fm.get("sources", []) or [],
            "related_entities": fm.get("related_entities", []) or [],
        }
    return ents


def load_existing_pairs() -> set[tuple[str, str]]:
    """All (source_id, target_id) ordered pairs with an existing relationship."""
    pairs = set()
    for p in (ROOT / "data" / "relationships").rglob("*.md"):
        fm, _ = split_file(p.read_text(encoding="utf-8"))
        if isinstance(fm, dict):
            s = (fm.get("source") or {}).get("id")
            t = (fm.get("target") or {}).get("id")
            if s and t:
                pairs.add((s, t))
    return pairs

# ------------------------------------------------------------- name index

STOP_NAMES = {
    "humanoid", "humanoid robot", "humanoid robots", "机器人", "人形机器人",
    "simulation", "control", "dynamics", "planning", "robotics", "强化学习",
}


def build_name_index(ents: dict[str, dict]) -> list[tuple[str, str]]:
    """(name, entity_id) pairs worth matching in text. Longest first."""
    pairs = []
    for eid, e in ents.items():
        for name in {e["name_en"], e["name_zh"]}:
            name = (name or "").strip()
            if len(name) < 8:
                continue
            if name.lower() in STOP_NAMES:
                continue
            pairs.append((name, eid))
    # dedupe identical names pointing at the same id; longest first for greedy match
    pairs = list(dict.fromkeys(pairs))
    pairs.sort(key=lambda x: -len(x[0]))
    return pairs


def find_mentions(body: str, name_index: list[tuple[str, str]], own_id: str) -> dict[str, list[str]]:
    """entity_id -> list of evidence sentences mentioning it in body."""
    hits: dict[str, list[str]] = defaultdict(list)
    sentences = re.split(r"(?<=[。！？.!?\n])\s*", body)
    for sent in sentences:
        s = sent.strip()
        if len(s) < 15:
            continue
        for name, eid in name_index:
            if eid == own_id or eid in hits:
                continue
            if name in s:
                hits[eid].append(s[:300])
    return hits


def in_reference_section(body: str, evidence: str) -> bool:
    parts = re.split(r"(?m)^(## .*)$", body)
    for i in range(1, len(parts) - 1, 2):
        title = re.sub(r"^##\s*", "", parts[i]).strip()
        if title in REF_TITLES:
            return evidence in parts[i + 1]
    return False

# ------------------------------------------------------------- rel writer

VERB = {
    "cites": ("cites", "引用"),
    "is_based_on": ("is based on", "基于"),
    "derived_from": ("is derived from", "衍生自"),
    "produces": ("produces", "生产"),
    "mentions": ("mentions", "提及"),
    "has_prerequisite": ("has prerequisite", "前置依赖"),
    "uses": ("uses", "使用"),
    "evaluates_on": ("is evaluated on", "评测于"),
    "proposes": ("proposes", "提出"),
    "serves": ("serves", "服务"),
}


def rel_id(src: str, rtype: str, tgt: str) -> str:
    rid = f"rel_{src}_{rtype}_{tgt}"
    return rid[:240]


def make_rel(src: dict, tgt: dict, rtype: str, rule: str, confidence: str,
             evidence: str, source_url: str, source_title: str) -> dict:
    en_verb, zh_verb = VERB.get(rtype, (rtype.replace("_", " "), rtype))
    return {
        "$id": rel_id(src["id"], rtype, tgt["id"]),
        "$schema": "../schema/v1/relationship_schema.json",
        "$version": 1,
        "type": rtype,
        "source": {"id": src["id"], "name": {"en": src["name_en"], "zh": src["name_zh"]}},
        "target": {"id": tgt["id"], "name": {"en": tgt["name_en"], "zh": tgt["name_zh"]}},
        "domains": {
            "source_domain": (src["domains"] or ["00_foundations"])[0],
            "target_domain": (tgt["domains"] or ["00_foundations"])[0],
        },
        "description": {
            "en": f"{src['name_en']} {en_verb} {tgt['name_en']}.",
            "zh": f"{src['name_zh']}{zh_verb}{tgt['name_zh']}。",
        },
        "verification": {
            "status": "partially_verified" if confidence != "low" else "unverified",
            "reviewed_by": "ai",
            "reviewed_at": TODAY,
            "confidence": confidence,
            "notes": f"Mined by build_latent_relationships.py rule {rule}. Evidence: {evidence[:400]}",
        },
        "sources": [{
            "id": "src_001",
            "type": "other",
            "title": source_title,
            "url": source_url,
            "accessed_at": TODAY,
        }],
    }


def dump_rel(rel: dict) -> str:
    return "---\n" + yaml.safe_dump(rel, allow_unicode=True, sort_keys=False, width=120) + "---\n"

# ------------------------------------------------------------------ rules

def rule_related_entities(ents, existing, out, stats):
    """P0b: frontmatter related_entities without a standalone rel file."""
    for eid, e in ents.items():
        for item in e["related_entities"]:
            if not isinstance(item, dict):
                continue
            tid = item.get("id")
            rtype = item.get("relationship") or "mentions"
            if not tid or tid not in ents or tid == eid or (eid, tid) in existing:
                continue
            desc = item.get("description", {}) or {}
            evidence = desc.get("zh") or desc.get("en") or "frontmatter related_entities"
            src_url = f"https://kg.rounds-tech.com/entry/{eid}/"
            rel = make_rel(e, ents[tid], rtype, "p0b_related_entities", "medium", evidence, src_url, f"KG frontmatter of {eid}")
            out[rel["$id"]] = rel
            existing.add((eid, tid))
            stats["p0b"] += 1


ARXIV_RE = re.compile(r"arxiv\.org/abs/(\d{4}\.\d{4,5})(v\d+)?")


def arxiv_index(ents) -> dict[str, str]:
    """arXiv id -> entity id. Prefer type=paper entities when several share the URL."""
    idx: dict[str, str] = {}
    paper_idx: dict[str, str] = {}
    for eid, e in ents.items():
        for s in e["sources"]:
            url = (s or {}).get("url", "") if isinstance(s, dict) else str(s)
            m = ARXIV_RE.search(url or "")
            if m:
                if e["type"] == "paper":
                    paper_idx.setdefault(m.group(1), eid)
                else:
                    idx.setdefault(m.group(1), eid)
    idx.update(paper_idx)
    return idx


def rule_arxiv_refs(ents, existing, out, stats):
    """P1: arXiv IDs in 参考 sections resolving to existing entities -> cites."""
    ax = arxiv_index(ents)
    for eid, e in ents.items():
        parts = re.split(r"(?m)^(## .*)$", e["body"])
        for i in range(1, len(parts) - 1, 2):
            title = re.sub(r"^##\s*", "", parts[i]).strip()
            if title not in REF_TITLES:
                continue
            for m in ARXIV_RE.finditer(parts[i + 1]):
                tid = ax.get(m.group(1))
                if not tid or tid == eid or (eid, tid) in existing:
                    continue
                line = parts[i + 1].strip().splitlines()[0][:200]
                rel = make_rel(e, ents[tid], "cites", "p1_arxiv_ref", "high",
                               f"参考文献列出 arXiv:{m.group(1)}", f"https://arxiv.org/abs/{m.group(1)}",
                               f"arXiv:{m.group(1)}")
                out[rel["$id"]] = rel
                existing.add((eid, tid))
                stats["p1"] += 1


def norm_source_url(url: str) -> str:
    m = ARXIV_RE.search(url or "")
    if m:
        return f"arxiv:{m.group(1)}"
    return (url or "").strip().rstrip("/").lower()


def rule_shared_sources(ents, existing, out, stats):
    """P2: entities sharing a source URL -> conservative typed edges."""
    by_url: dict[str, list[str]] = defaultdict(list)
    for eid, e in ents.items():
        for s in e["sources"]:
            url = (s or {}).get("url", "") if isinstance(s, dict) else str(s)
            nu = norm_source_url(url)
            if nu:
                by_url[nu].append(eid)
    for url, eids in by_url.items():
        eids = sorted(set(eids))
        if len(eids) < 2 or len(eids) > 20:
            continue
        papers = [i for i in eids if ents[i]["type"] == "paper"]
        others = [i for i in eids if ents[i]["type"] != "paper"]
        # paper as hub: component/method/robot_system derived_from / is_based_on paper
        if len(papers) == 1 and others:
            p = papers[0]
            for o in others:
                if (o, p) in existing or (p, o) in existing:
                    continue
                rtype = "derived_from" if ents[o]["type"] in ("component", "robot_system") else "is_based_on"
                rel = make_rel(ents[o], ents[p], rtype, "p2_shared_source", "medium",
                               f"与论文共享来源 {url}", f"https://kg.rounds-tech.com/entry/{p}/",
                               f"Shared source {url}")
                out[rel["$id"]] = rel
                existing.add((o, p))
                stats["p2"] += 1


def rule_body_mentions(ents, existing, out, queue, stats):
    """P3: name mentions in bodies. 参考-sec -> cites; else -> LLM queue."""
    name_index = build_name_index(ents)
    for eid, e in ents.items():
        hits = find_mentions(e["body"], name_index, eid)
        for tid, sentences in hits.items():
            if (eid, tid) in existing:
                continue
            evidence = sentences[0]
            if in_reference_section(e["body"], evidence):
                rel = make_rel(e, ents[tid], "cites", "p3_ref_mention", "medium", evidence,
                               f"https://kg.rounds-tech.com/entry/{eid}/", f"KG body of {eid}")
                out[rel["$id"]] = rel
                existing.add((eid, tid))
                stats["p3_cites"] += 1
            else:
                queue.append({
                    "source_id": eid, "target_id": tid,
                    "source_name": e["name_en"] or e["name_zh"],
                    "target_name": ents[tid]["name_en"] or ents[tid]["name_zh"],
                    "source_type": e["type"], "target_type": ents[tid]["type"],
                    "evidence": evidence,
                })
                stats["p3_queued"] += 1


def rule_wiki_cooccurrence(ents, existing, out, stats):
    """P4: same-section co-occurrence in wiki chapters 9-30, core types only."""
    name_index = [(n, i) for n, i in build_name_index(ents) if ents[i]["type"] in CORE_TYPES]
    wiki_dir = ROOT / "wiki" / "docs" / "chapters"
    for path in sorted(wiki_dir.glob("chapter-*.md")):
        m = re.match(r"chapter-(\d+)\.md", path.name)
        if not m or int(m.group(1)) < 9:
            continue
        text = path.read_text(encoding="utf-8")
        chapter = m.group(1)
        sections = re.split(r"(?m)^#{2,4} .*$", text)
        for sec in sections:
            found = set()
            for name, eid in name_index:
                if name in sec:
                    found.add(eid)
                if len(found) > 6:
                    break
            found = sorted(found)
            for a in range(len(found)):
                for b in range(a + 1, len(found)):
                    s, t = found[a], found[b]
                    if (s, t) in existing or (t, s) in existing:
                        continue
                    rel = make_rel(ents[s], ents[t], "mentions", f"p4_wiki_ch{chapter}", "low",
                                   f"在 Wiki 第 {chapter} 章同一小节共现",
                                   f"https://kg.rounds-tech.com/wiki/chapters/chapter-{chapter}/",
                                   f"Wiki 第 {chapter} 章")
                    out[rel["$id"]] = rel
                    existing.add((s, t))
                    stats["p4"] += 1


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--write", action="store_true")
    args = ap.parse_args()

    ents = load_entities()
    existing = load_existing_pairs()
    out: dict[str, dict] = {}
    queue: list[dict] = []
    stats = defaultdict(int)

    rule_related_entities(ents, existing, out, stats)
    rule_arxiv_refs(ents, existing, out, stats)
    rule_shared_sources(ents, existing, out, stats)
    rule_body_mentions(ents, existing, out, queue, stats)
    rule_wiki_cooccurrence(ents, existing, out, stats)

    print("new relationships by rule:", dict(stats))
    print("total new:", len(out), " llm_queue:", len(queue))

    manifest = {"date": TODAY, "stats": dict(stats), "total": len(out), "queued": len(queue)}
    (ROOT / ".staging").mkdir(exist_ok=True)
    (ROOT / ".staging" / "llm_relation_queue.jsonl").write_text(
        "\n".join(json.dumps(q, ensure_ascii=False) for q in queue) + "\n", encoding="utf-8")
    (ROOT / ".staging" / "latent_relationships_manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")

    if args.write:
        rel_dir = ROOT / "data" / "relationships"
        for rel in out.values():
            (rel_dir / f"{rel['$id']}.md").write_text(dump_rel(rel), encoding="utf-8")
        print(f"wrote {len(out)} files to data/relationships/")
    else:
        print("dry-run; re-run with --write to apply")


if __name__ == "__main__":
    main()
