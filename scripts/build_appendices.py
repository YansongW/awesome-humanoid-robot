#!/usr/bin/env python3
"""Generate wiki appendices A/B/C/E/G from KG source data (research/ + data/relationships/).

- 附录 A 实体与关系速查表：类型统计、关系类型统计、核心实体 Top 50
- 附录 B 关键数据集清单：dataset 类型实体
- 附录 C 软件与仿真平台清单：software_platform 与仿真相关 technology
- 附录 E 标准、法规与认证清单：standard 类型实体
- 附录 G 术语表：concept/principle/operator/algorithm 等实体的一句话定义

Generated content is derived from the KG, so re-run after KG updates.
"""
from __future__ import annotations

import re
import sys
from collections import Counter
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "website"))
from builder.loader import DOMAIN_LABELS, LAYER_LABELS, TYPE_LABELS  # noqa: E402

TYPE_ZH = TYPE_LABELS["zh"]
DOMAIN_ZH = DOMAIN_LABELS["zh"]
WIKI = ROOT / "wiki" / "docs" / "appendices"


def load_entries() -> list[dict]:
    entries = []
    for p in sorted(ROOT.glob("research/**/*.md")):
        text = p.read_text(encoding="utf-8")
        m = re.match(r"\A---\n(.*?)\n---\n", text, re.S)
        if not m:
            continue
        try:
            fm = yaml.safe_load(m.group(1))
        except yaml.YAMLError:
            continue
        if not isinstance(fm, dict) or "$id" not in fm:
            continue
        entries.append(fm)
    return entries


def load_relationships() -> list[dict]:
    rels = []
    for p in sorted((ROOT / "data" / "relationships").rglob("*.md")):
        text = p.read_text(encoding="utf-8")
        m = re.match(r"\A---\n(.*?)\n---\n", text, re.S)
        if not m:
            continue
        try:
            d = yaml.safe_load(m.group(1))
        except yaml.YAMLError:
            continue
        if isinstance(d, dict) and d.get("type"):
            src = (d.get("source") or {}).get("id", "")
            tgt = (d.get("target") or {}).get("id", "")
            rels.append({"type": d["type"], "source_id": src, "target_id": tgt})
    return rels


def zh_name(fm: dict) -> str:
    return (fm.get("names", {}) or {}).get("zh") or (fm.get("names", {}) or {}).get("en") or fm.get("$id", "")


def en_name(fm: dict) -> str:
    return (fm.get("names", {}) or {}).get("en") or ""


def zh_summary(fm: dict) -> str:
    s = (fm.get("summary", {}) or {}).get("zh") or (fm.get("summary", {}) or {}).get("en") or ""
    return re.sub(r"\s+", " ", s).strip()


def first_sentence(text: str, limit: int = 90) -> str:
    m = re.split(r"(?<=[。！？.!?])\s*", text, maxsplit=1)
    s = m[0] if m else text
    if len(s) > limit:
        s = s[:limit].rstrip() + "…"
    return s


def link(fm: dict) -> str:
    eid = fm.get("$id", "")
    return f"[{zh_name(fm)}](/entry/{eid}/)"


def header(title: str, intro: str) -> str:
    return f"# {title}\n\n> 本附录由 `scripts/build_appendices.py` 从知识图谱数据自动生成，随 KG 更新而更新。\n\n{intro}\n\n"


def gen_appendix_a(entries: list[dict], rels: list[dict]) -> str:
    out = [header("附录 A 实体与关系速查表", "知识图谱的实体类型、关系类型与核心实体一览。")]
    # entity type stats
    tc = Counter(fm.get("type", "unknown") for fm in entries)
    out.append("## A.1 实体类型分布\n")
    out.append("| 类型 | 中文 | 数量 |\n|---|---|---|")
    for t, c in tc.most_common():
        out.append(f"| `{t}` | {TYPE_ZH.get(t, t)} | {c} |")
    out.append(f"| **合计** | — | **{sum(tc.values())}** |\n")
    # relation type stats
    rc = Counter(r.get("type", "?") for r in rels)
    out.append("## A.2 关系类型分布\n")
    out.append("| 关系类型 | 数量 |\n|---|---|")
    for t, c in rc.most_common():
        out.append(f"| `{t}` | {c} |")
    out.append(f"| **合计** | **{sum(rc.values())}** |\n")
    # domain stats
    dc = Counter(d for fm in entries for d in (fm.get("domains") or []))
    out.append("## A.3 领域（Domain）分布\n")
    out.append("| 领域 | 实体数 |\n|---|---|")
    for d, c in sorted(dc.items()):
        out.append(f"| {DOMAIN_ZH.get(d, d)} | {c} |")
    # top entities by relation count
    deg = Counter()
    for r in rels:
        deg[r.get("source_id", "")] += 1
        deg[r.get("target_id", "")] += 1
    by_id = {fm.get("$id"): fm for fm in entries}
    out.append("\n## A.4 核心实体 Top 50（按关系数）\n")
    out.append("| 排名 | 实体 | 类型 | 关系数 |\n|---|---|---|---|")
    for i, (eid, c) in enumerate(deg.most_common(50), 1):
        fm = by_id.get(eid)
        if not fm:
            continue
        out.append(f"| {i} | {link(fm)} | {TYPE_ZH.get(fm.get('type', ''), fm.get('type', ''))} | {c} |")
    out.append("")
    return "\n".join(out)


def _entity_table(title: str, intro: str, items: list[dict], limit: int = 0) -> str:
    out = [header(title, intro)]
    out.append("| 名称 | 英文名 | 简介 |\n|---|---|---|")
    items = sorted(items, key=lambda fm: zh_name(fm))
    if limit:
        items = items[:limit]
    for fm in items:
        s = first_sentence(zh_summary(fm)) or "—"
        out.append(f"| {link(fm)} | {en_name(fm)} | {s} |")
    out.append("")
    return "\n".join(out)


def gen_appendix_b(entries: list[dict]) -> str:
    ds = [fm for fm in entries if fm.get("type") == "dataset"]
    intro = f"知识图谱收录的 {len(ds)} 个关键数据集实体，涵盖遥操作演示、第一视角视频、动作捕捉与大规模跨具身数据。"
    return _entity_table("附录 B 关键数据集清单", intro, ds)


def gen_appendix_c(entries: list[dict]) -> str:
    sw = [fm for fm in entries if fm.get("type") == "software_platform"]
    sim_kw = ("mujoco", "isaac", "gazebo", "genesis", "drake", "pinocchio", "moveit", "ros", "mjcf", "urdf", "sapien", "pybullet", "lerobot")
    tech = [
        fm for fm in entries
        if fm.get("type") in ("technology", "benchmark")
        and any(k in (en_name(fm) + zh_name(fm)).lower() for k in sim_kw)
    ]
    seen, merged = set(), []
    for fm in sw + tech:
        if fm.get("$id") not in seen:
            seen.add(fm.get("$id"))
            merged.append(fm)
    intro = f"知识图谱收录的 {len(merged)} 个软件与仿真平台实体，覆盖中间件、运动规划、动力学库、物理引擎与大规模并行仿真。"
    return _entity_table("附录 C 软件与仿真平台清单", intro, merged)


def gen_appendix_e(entries: list[dict]) -> str:
    std = [fm for fm in entries if fm.get("type") == "standard"]
    intro = (
        f"知识图谱收录的 {len(std)} 个标准/法规/认证实体。"
        "机器人进入各区域市场前，应以此清单为索引核对适用标准与认证路径；各实体卡片内含适用范围与核心关注点。"
    )
    return _entity_table("附录 E 标准、法规与认证清单", intro, std)


def gen_appendix_g(entries: list[dict]) -> str:
    glossary_types = ["concept", "principle", "operator", "algorithm", "formalism", "theorem", "equation", "foundation"]
    out = [header("附录 G 术语表", "知识图谱中概念、原理、算子、算法等形式化实体的一句话定义，按类别分组。")]
    for t in glossary_types:
        items = [fm for fm in entries if fm.get("type") == t]
        if not items:
            continue
        out.append(f"## G.{glossary_types.index(t) + 1} {TYPE_ZH.get(t, t)}（{len(items)}）\n")
        out.append("| 术语 | 定义 |\n|---|---|")
        for fm in sorted(items, key=lambda x: zh_name(x)):
            s = first_sentence(zh_summary(fm), 120) or "—"
            out.append(f"| {link(fm)} | {s} |")
        out.append("")
    return "\n".join(out)


def main() -> None:
    entries = load_entries()
    rels = load_relationships()
    outputs = {
        "appendix-a.md": gen_appendix_a(entries, rels),
        "appendix-b.md": gen_appendix_b(entries),
        "appendix-c.md": gen_appendix_c(entries),
        "appendix-e.md": gen_appendix_e(entries),
        "appendix-g.md": gen_appendix_g(entries),
    }
    for name, content in outputs.items():
        (WIKI / name).write_text(content, encoding="utf-8")
        print(f"wrote {name}: {len(content)} bytes")


if __name__ == "__main__":
    main()
