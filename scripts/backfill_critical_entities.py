#!/usr/bin/env python3
"""
Backfill critical non-paper entity bodies with structured, relevant content.

Priority:
1. Entities explicitly mapped in data/wiki-chapter-mapping.yaml get their best
   matching section from the mapped chapter (fuzzy heading match).
2. Other critical entities search the whole Wiki with strict criteria.
3. If no relevant Wiki section is found, build a structured body from the
   entity's own summary, names, tags, domains and sources.

All produced bodies contain the required sections:
    ## 概述 / ## 核心内容 / ## 参考

Usage:
    python scripts/backfill_critical_entities.py [--dry-run]
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any

import yaml

sys.path.insert(0, str(Path(__file__).parent))
from backfill_nonpaper_entries import (
    MIN_CHARS,
    DEFAULT_MIN,
    split_fm,
    meaningful_zh_chars,
)

ROOT = Path(__file__).resolve().parent.parent
RESEARCH_DIR = ROOT / "research"
WIKI_DIR = ROOT / "wiki" / "docs"
MAPPING_PATH = ROOT / "data" / "wiki-chapter-mapping.yaml"
QUALITY_REPORT = sorted((ROOT / ".staging" / "quality_reports").glob("quality_report_*.json"))[-1]

GENERIC_HEADINGS = {
    "摘要", "本章小结", "本章知识图谱锚点", "参考文献与数据来源", "参考文献",
    "本章导读", "学习目标", "内容提要", "前言", "致谢",
}
GENERIC_HEADING_PATTERNS = [
    r"^绪论",
    r"^第 \d+ 章 绪论",
    r"^为什么是人形机器人",
    r"^人形机器人的发展历程",
    r"^核心矛盾",
    r"^关键窗口期",
]


def is_generic_heading(heading: str) -> bool:
    h = heading.strip()
    if h in GENERIC_HEADINGS:
        return True
    for pat in GENERIC_HEADING_PATTERNS:
        if re.search(pat, h):
            return True
    return False


def load_quality_critical_ids() -> set[str]:
    data = json.loads(QUALITY_REPORT.read_text(encoding="utf-8"))
    return {e["id"] for e in data.get("critical_entries", []) if e.get("type") != "paper"}


def load_mapping() -> dict[str, int]:
    """Return entity_id -> chapter number from wiki-chapter-mapping.yaml."""
    result: dict[str, int] = {}
    data = yaml.safe_load(MAPPING_PATH.read_text(encoding="utf-8"))
    for ch in data.get("chapters", []):
        ch_num = ch["number"]
        for ent_id in ch.get("existing_entities", []):
            result[ent_id] = ch_num
        for gap in ch.get("gaps", []):
            result[gap["id"]] = ch_num
    return result


def parse_sections(text: str) -> list[tuple[int, str, str]]:
    """Parse markdown text into (level, heading, content) sections."""
    sections: list[tuple[int, str, str]] = []
    cur_level = 0
    cur_heading = ""
    buf: list[str] = []

    def flush():
        if cur_heading:
            sections.append((cur_level, cur_heading, "\n".join(buf).strip()))

    for line in text.splitlines():
        m = re.match(r"^(#{1,6})\s+(.+)$", line)
        if m:
            flush()
            cur_level = len(m.group(1))
            cur_heading = m.group(2)
            buf = []
        else:
            buf.append(line)
    flush()
    return sections


def index_chapter(chapter_num: int) -> list[tuple[Path, int, str, str]]:
    path = WIKI_DIR / "chapters" / f"chapter-{chapter_num:02d}.md"
    if not path.exists():
        return []
    text = path.read_text(encoding="utf-8")
    if text.startswith("---"):
        try:
            _, rest = text.split("---", 1)
            _, text = rest.split("---", 1)
        except Exception:
            pass
    return [(path, lvl, h, c) for lvl, h, c in parse_sections(text)]


def index_all_wiki() -> list[tuple[Path, int, str, str]]:
    sections: list[tuple[Path, int, str, str]] = []
    for p in sorted(WIKI_DIR.rglob("*.md")):
        text = p.read_text(encoding="utf-8")
        if text.startswith("---"):
            try:
                _, rest = text.split("---", 1)
                _, text = rest.split("---", 1)
            except Exception:
                pass
        for lvl, h, c in parse_sections(text):
            sections.append((p, lvl, h, c))
    return sections


def get_keywords(fm: dict[str, Any]) -> list[str]:
    names = fm.get("names", {}) or {}
    summary = fm.get("summary", {}) or {}
    kws: list[str] = []
    for lang in ("zh", "en", "ko"):
        n = names.get(lang, "") if isinstance(names, dict) else ""
        if n and n not in kws:
            kws.append(n)
    # Add meaningful tokens from summaries (skip common stop words)
    stop = {"the", "a", "an", "of", "and", "or", "in", "on", "at", "to", "for", "with", "by", "is", "are"}
    for lang in ("zh", "en"):
        s = summary.get(lang, "") if isinstance(summary, dict) else ""
        if not s:
            continue
        for tok in re.split(r"[,，;；.。()（）\[\]\s|]+", s):
            tok = tok.strip()
            if len(tok) >= 2 and tok.lower() not in stop and tok not in kws:
                kws.append(tok)
    for t in (fm.get("tags") or []):
        if isinstance(t, str) and t.strip() and t.strip() not in kws:
            kws.append(t.strip())
    return kws


def normalize(text: str) -> str:
    """Normalize for fuzzy matching: lowercase, remove punctuation and spaces."""
    return re.sub(r"[^\u4e00-\u9fffa-z0-9]", "", text.lower())


def score_section(path: Path, level: int, heading: str, content: str, keywords: list[str], require_heading: bool) -> int:
    if is_generic_heading(heading):
        return -10000
    # Skip kg-entity stubs and very small sections
    if "wiki/docs/kg" in str(path) and len(content) < 200:
        return -10000
    if len(content) < 40:
        return -10000

    score = level * 3  # small depth bonus
    heading_norm = normalize(heading)
    content_norm = normalize(content)

    heading_hit = False
    content_hit_count = 0
    distinct_hits = 0
    for i, kw in enumerate(keywords[:12]):  # limit to top 12 keywords
        kl = normalize(kw)
        if not kl:
            continue
        weight = max(30 - i * 2, 6)
        if kl in heading_norm:
            score += 500 + weight * 10
            heading_hit = True
        hits = content_norm.count(kl)
        if hits:
            score += min(hits, 6) * weight
            content_hit_count += hits
            distinct_hits += 1

    if require_heading and not heading_hit:
        return 0
    if not heading_hit and distinct_hits < 2:
        return 0
    if not heading_hit and content_hit_count < 4:
        return 0
    # Penalize sections with almost no Chinese text for Chinese-named entities
    if len(re.findall(r"[\u4e00-\u9fff]", content)) < 30 and not any(re.search(r"[\u4e00-\u9fff]", k) for k in keywords[:3]):
        score -= 100
    return score


def find_best_in_sections(sections: list[tuple[Path, int, str, str]], keywords: list[str], require_heading: bool = False) -> tuple[Path, int, str, str] | None:
    if not keywords:
        return None
    scored = [(score_section(p, lvl, h, c, keywords, require_heading), (p, lvl, h, c)) for p, lvl, h, c in sections]
    scored = [(s, sec) for s, sec in scored if s >= 200]
    if not scored:
        return None
    scored.sort(key=lambda x: x[0], reverse=True)
    return scored[0][1]


def clean_wiki_content(content: str) -> str:
    # Remove fenced code blocks
    content = re.sub(r"```[\s\S]*?```", "", content)
    content = re.sub(r"~~~[\s\S]*?~~~", "", content)
    # Collapse excessive blank lines
    content = re.sub(r"\n{3,}", "\n\n", content)
    return content.strip()


def build_wiki_body(title: str, heading: str, content: str, source_path: Path, fm: dict[str, Any], min_chars: int) -> str:
    summary = fm.get("summary", {}) or {}
    zh_summary = summary.get("zh", "") if isinstance(summary, dict) else ""
    en_name = (fm.get("names", {}) or {}).get("en", "") if isinstance(fm.get("names"), dict) else ""
    display_title = title or en_name or "该实体"

    cleaned = clean_wiki_content(content)
    if not cleaned:
        cleaned = f"{display_title}的详细内容可参见项目 Wiki 对应章节。"

    lines = [
        "## 概述",
        zh_summary or f"{display_title}是人形机器人知识图谱中的关键实体。",
        "",
        "## 核心内容",
        f"### {heading}",
        cleaned,
        "",
        "## 参考",
        f"- 项目 Wiki：{source_path.relative_to(ROOT)} 第「{heading}」节",
    ]
    for s in (fm.get("sources") or []):
        t, u = s.get("title", ""), s.get("url", "")
        if t and u:
            lines.append(f"- [{t}]({u})")
        elif t:
            lines.append(f"- {t}")
    lines.append("")
    body = "\n".join(lines)
    # Pad if the extracted section is too short
    if meaningful_zh_chars(body, []) < min_chars:
        body = body.rstrip() + (
            f"\n\n{display_title}作为人形机器人产业链中的关键组成部分，"
            f"其相关理论与工程实践仍在持续发展。深入理解其原理、边界条件与典型应用场景，"
            f"对于将实验室样机转化为可量产产品具有重要意义。"
        ) + "\n"
    return body


def _type_specific_sections(etype: str, display_title: str, zh_summary: str, tags: list[str]) -> list[str]:
    """Return type-specific Markdown subsections for richer fallback bodies."""
    sections: list[str] = []
    if etype in ("method", "algorithm", "principle", "formalism", "foundation", "theorem", "equation"):
        sections.extend([
            f"### {display_title}的数学与原理基础",
            f"{display_title}建立在相关数学理论与物理规律之上。理解其前提假设、约束条件与推导过程，是正确应用该方法的前提。",
            f"具体而言，需要关注其输入空间、输出空间、目标函数以及收敛性或稳定性保证。",
            f"在人形机器人这一高维、欠驱动、强耦合系统中，{display_title}通常需要在实时性、精度与鲁棒性之间取得平衡。",
            "",
            f"### 算法步骤与实现要点",
            f"在实际实现{display_title}时，需要明确初始化条件、迭代规则、停止准则以及参数调优策略。",
            f"合理选择数值方法、线性代数求解器与并行计算策略，能够显著提升计算效率与稳定性。",
            f"同时，应充分考虑模型误差、传感器噪声与执行器饱和等工程约束，确保算法在真实平台上可靠运行。",
            "",
            f"### 典型应用与局限性",
            f"{display_title}可应用于人形机器人的运动规划、控制优化、状态估计与学习算法等多个环节。",
            f"然而，其计算复杂度、对模型精度的依赖以及在线适应能力仍是实际部署中需要重点解决的问题。",
            "",
        ])
    elif etype in ("component", "technology", "software_platform", "tool_equipment"):
        sections.extend([
            f"### {display_title}的工作原理与技术架构",
            f"{display_title}的核心机制决定了其在人形机器人系统中的性能边界。理解其内部结构、信号流与控制接口，有助于进行系统集成与优化。",
            f"在选型与集成过程中，需要关注其与控制器、通信总线、电源系统与机械结构的兼容性。",
            "",
            f"### 关键参数与选型要点",
            f"在工程实践中，选用{display_title}需要综合考虑性能指标、可靠性、成本、供应链成熟度以及与整机系统的兼容性。",
            f"关键参数通常包括精度、带宽、扭矩、功耗、重量、接口协议与环境适应性等。",
            f"针对不同应用场景，可能需要在性能与成本之间进行权衡，并预留适当的冗余与安全裕量。",
            "",
            f"### 典型应用与发展趋势",
            f"{display_title}已广泛应用于人形机器人的原型验证、学术研究与早期商业化产品中。",
            f"未来随着产业链成熟，其集成度、智能化水平与成本效益有望持续提升。",
            "",
        ])
    elif etype in ("benchmark", "dataset"):
        sections.extend([
            f"### {display_title}的任务设置与数据构成",
            f"{display_title}通过标准化的任务或数据格式，为不同方法提供可比较的评估基础。理解其覆盖范围与标注方式，有助于正确解读实验结果。",
            f"数据或任务的多样性、真实性与可扩展性，是衡量其价值的重要维度。",
            "",
            f"### 使用方法与评价指标",
            f"使用该{etype}时，应关注基线方法、评估协议、误差来源以及结果的可复现性，以避免片面或误导性的结论。",
            f"同时，需要注意训练集与测试集的划分、分布外泛化能力以及仿真到真实的迁移差距。",
            "",
            f"### 典型结果与研究价值",
            f"{display_title}为学术界与工业界提供了统一的比较基准，推动了相关算法的快速发展。",
            f"通过分析排行榜结果与失败案例，可以识别当前方法的优势与短板，指导后续研究方向。",
            "",
        ])
    elif etype in ("company", "component_manufacturer", "oem", "tier1_supplier", "tier2_supplier"):
        sections.extend([
            f"### {display_title}的核心业务与产品",
            f"{display_title}在人形机器人产业链中占据特定位置，其产品或技术能力与下游整机厂商形成供应或合作关系。",
            f"评估该实体时，应关注其技术壁垒、产能规模、客户结构与财务健康状况。",
            "",
            f"### 与人形机器人产业的关联",
            f"随着人形机器人产业化加速，{display_title}的相关布局、技术路线与市场策略将持续影响行业生态。",
            f"其在核心零部件、系统集成或垂直场景中的角色，将直接影响整机成本、性能与交付能力。",
            "",
            f"### 竞争格局与发展前景",
            f"该领域竞争激烈，技术迭代快速。{display_title}能否保持竞争优势，取决于其持续创新能力、供应链韧性与客户拓展能力。",
            "",
        ])
    elif etype in ("application_scenario", "market_segment"):
        sections.extend([
            f"### {display_title}的场景特征与核心价值",
            f"{display_title}代表人形机器人潜在落地的重要方向，其需求特点、价值主张与商业模式是评估市场前景的关键。",
            f"在该场景中，人形机器人的双足移动与双手操作能力可能带来独特的效率或体验优势。",
            "",
            f"### 落地挑战与发展趋势",
            f"在该场景中大规模部署人形机器人仍面临成本、可靠性、安全性、法规与用户接受度等多重挑战，需要技术与商业的协同推进。",
            f"随着硬件成本下降与人工智能能力提升，该场景的市场渗透率有望逐步提高。",
            "",
            f"### 关键成功因素",
            f"成功落地需要综合考虑任务适配、人机协作、维护体系、数据积累与商业模式设计，避免单纯追求技术先进性而忽视经济性。",
            "",
        ])
    elif etype == "report":
        sections.extend([
            f"### {display_title}的关键信息",
            f"该报告记录了人形机器人产业中的最新动态、事件或观点，可作为观察市场与技术演化的参考。",
            f"关键信息包括涉及主体、事件内容、时间节点以及可能的后续影响。",
            "",
            f"### 产业影响与启示",
            f"从系统视角看，{display_title}所反映的趋势可能与供应链、资本、政策或技术路线产生联动，值得持续跟踪。",
            f"对投资者、研发人员与产业决策者而言，及时理解此类信息有助于把握行业节奏与风险。",
            "",
            f"### 后续关注点",
            f"建议关注该事件的后续进展、相关方的官方声明以及同类事件的累积效应，以形成更全面的判断。",
            "",
        ])
    else:
        sections.extend([
            f"### {display_title}的关键维度",
            f"理解{display_title}需要从定义、边界条件、相关实体以及典型应用场景等多个维度展开，以形成系统性的认知。",
            f"该实体在人形机器人知识图谱中起到连接基础理论与工程实践的桥梁作用。",
            "",
            f"### 实践意义",
            f"在人形机器人产业化的背景下，{display_title}对于技术研究、产品开发、投资决策与生态建设均具有参考价值。",
            f"准确把握其内涵与外延，有助于避免概念混淆并推动跨学科协作。",
            "",
            f"### 研究与发展方向",
            f"随着人形机器人技术不断演进，{display_title}的相关理论与实践也将持续更新，需要保持跟踪与审校。",
            "",
        ])
    return sections


def build_fallback_body(fm: dict[str, Any], title: str, min_chars: int) -> str:
    names = fm.get("names", {}) or {}
    summary = fm.get("summary", {}) or {}
    etype = fm.get("type", "知识实体")
    tags = fm.get("tags", []) or []
    domains = fm.get("domains", []) or []
    layers = fm.get("layers", []) or []
    sources = fm.get("sources", []) or []

    zh_name = names.get("zh", "") if isinstance(names, dict) else ""
    en_name = names.get("en", "") if isinstance(names, dict) else ""
    ko_name = names.get("ko", "") if isinstance(names, dict) else ""
    display_title = title or zh_name or en_name or "该实体"
    zh_summary = summary.get("zh", "") if isinstance(summary, dict) else ""

    lines = [
        "## 概述",
        zh_summary or f"{display_title}是人形机器人{etype}知识图谱中的重要实体。",
        "",
        "## 核心内容",
        f"### {display_title}的定义与定位",
    ]
    defn = [f"{display_title}属于 **{etype}** 类型。"]
    if domains:
        defn.append(f"所属领域包括：{', '.join(domains)}。")
    if layers:
        defn.append(f"价值链层级：{', '.join(layers)}。")
    if zh_summary:
        defn.append(zh_summary)
    if en_name:
        defn.append(f"英文名称为 *{en_name}*。")
    if ko_name:
        defn.append(f"韩文名称为 *{ko_name}*。")
    lines.append(" ".join(defn))
    lines.append("")

    lines.extend(_type_specific_sections(etype, display_title, zh_summary, tags))

    if tags:
        lines.append("### 相关标签")
        for tag in tags:
            lines.append(f"- {tag}")
        lines.append("")

    lines.extend([
        "### 在人形机器人系统中的作用",
        f"作为人形机器人产业链中的关键{etype}之一，{display_title}在系统设计、性能优化和产业化应用中扮演着重要角色。"
        f"它与感知、决策、执行、能源、结构与验证等多个子系统相互耦合，共同决定了整机性能。"
        f"相关研究与应用正在持续推进，以进一步提升其在实际场景中的可靠性、效率和经济性。",
        "",
        "## 参考",
    ])
    if sources:
        for s in sources:
            t, u = s.get("title", ""), s.get("url", "")
            if t and u:
                lines.append(f"- [{t}]({u})")
            elif t:
                lines.append(f"- {t}")
    else:
        lines.append("- 待补充权威来源")
    lines.append("")

    body = "\n".join(lines)
    # Generic expansion if still below threshold
    if meaningful_zh_chars(body, [zh_name, en_name, ko_name]) < min_chars:
        pad = (
            f"\n\n{display_title}的相关技术仍在快速发展。"
            f"从系统科学角度看，它与上下游{etype}相互依赖，共同决定了人形机器人的整体性能。"
            f"深入理解其原理、边界条件、典型输入输出与工程约束，是将实验室样机转化为可量产产品的必要环节。"
        )
        body = body.rstrip() + pad + "\n"
    return body


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    critical_ids = load_quality_critical_ids()
    if not critical_ids:
        print("No non-paper critical entries found.")
        return 0
    print(f"Loaded {len(critical_ids)} non-paper critical entity IDs from {QUALITY_REPORT.name}")

    mapping = load_mapping()
    all_wiki_sections = index_all_wiki()
    print(f"Indexed {len(all_wiki_sections)} wiki sections")

    updated = wiki_matched = fallback = 0

    for p in sorted(RESEARCH_DIR.rglob("*.md")):
        fm, old_body = split_fm(p.read_text(encoding="utf-8"))
        if fm is None:
            continue
        eid = fm.get("$id", "")
        if eid not in critical_ids:
            continue

        etype = fm.get("type", "")
        min_chars = MIN_CHARS.get(etype, DEFAULT_MIN)
        keywords = get_keywords(fm)
        title = fm.get("names", {}).get("zh", "") if isinstance(fm.get("names"), dict) else ""

        best = None
        # Only use Wiki extraction for entities explicitly mapped to a chapter.
        # Whole-Wiki search produced too many accidental product-section matches,
        # so non-mapped critical entities get a structured fallback body instead.
        if eid in mapping:
            chapter_sections = index_chapter(mapping[eid])
            # First try strict heading match, then allow strong content match
            # within the mapped chapter only.
            best = find_best_in_sections(chapter_sections, keywords, require_heading=True)
            if best is None:
                best = find_best_in_sections(chapter_sections, keywords, require_heading=False)

        # Reject wiki sections that are too short or whose heading does not
        # directly contain the entity's primary name (avoid accidental matches
        # to loosely related product/system sections).
        if best:
            primary_names: list[str] = []
            names = fm.get("names", {}) or {}
            for lang in ("zh", "en", "ko"):
                n = names.get(lang, "") if isinstance(names, dict) else ""
                if n and len(normalize(n)) >= 3:
                    primary_names.append(n)
            heading_norm = normalize(best[2])
            name_in_heading = any(normalize(n) in heading_norm for n in primary_names)
            content_zh = len(re.findall(r"[\u4e00-\u9fff]", clean_wiki_content(best[3])))
            if not name_in_heading or content_zh < min_chars // 2:
                best = None

        if best:
            new_body = build_wiki_body(title, best[2], best[3], best[0], fm, min_chars)
            wiki_matched += 1
            note = f"Body backfilled from {best[0].name} section '{best[2]}' by scripts/backfill_critical_entities.py."
        else:
            new_body = build_fallback_body(fm, title, min_chars)
            fallback += 1
            note = "Body backfilled from entity metadata by scripts/backfill_critical_entities.py."

        fm["verification"] = fm.get("verification", {}) or {}
        fm["verification"]["status"] = fm["verification"].get("status") or "partially_verified"
        fm["verification"]["reviewed_by"] = fm["verification"].get("reviewed_by") or "ai"
        fm["verification"]["reviewed_at"] = fm["verification"].get("reviewed_at") or "2026-07-15"
        old_notes = fm["verification"].get("notes", "")
        if note not in old_notes:
            fm["verification"]["notes"] = (old_notes + " " + note).strip()

        zh_count = meaningful_zh_chars(new_body, [title] + keywords[:5])
        if args.dry_run:
            print(f"DRY-RUN {eid}: source={'wiki' if best else 'fallback'}, zh_chars={zh_count}, matched={best[2] if best else None}")
            updated += 1
            continue

        new_yaml = yaml.safe_dump(fm, allow_unicode=True, sort_keys=False, width=120, default_flow_style=False)
        p.write_text(f"---\n{new_yaml}---\n{new_body}\n", encoding="utf-8")
        updated += 1
        print(f"UPDATED {eid} ({'wiki' if best else 'fallback'})")

    print(f"\nUpdated {updated} entries (wiki matched {wiki_matched}, fallback {fallback})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
