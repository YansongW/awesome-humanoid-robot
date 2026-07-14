#!/usr/bin/env python3
"""
Backfill shallow non-paper research entries from wiki chapters / kg entities / appendix-d.

Usage:
    python scripts/backfill_nonpaper_entries.py
"""

from __future__ import annotations

import re
import sys
from pathlib import Path
from typing import Any

import yaml

sys.path.insert(0, str(Path(__file__).parent))
from fill_gap_bodies_from_wiki import EXTRA_KEYWORDS

ROOT = Path(__file__).parent.parent
RESEARCH_DIR = ROOT / "research"
WIKI_CHAPTERS = ROOT / "wiki" / "docs" / "chapters"
KG_ENTITIES = ROOT / "wiki" / "docs" / "kg" / "entities"
APPENDIX_D = ROOT / "wiki" / "docs" / "appendices" / "appendix-d"

MIN_CHARS = {
    "method": 400,
    "principle": 400,
    "formalism": 400,
    "foundation": 400,
    "technology": 400,
    "algorithm": 300,
    "component": 300,
    "material": 300,
    "software_platform": 300,
    "tool_equipment": 300,
    "company": 300,
    "oem": 300,
    "tier1_supplier": 300,
    "tier2_supplier": 300,
    "component_manufacturer": 300,
    "process": 500,
    "dataset": 200,
    "benchmark": 200,
    "standard": 200,
    "concept": 300,
    "robot_system": 300,
    "application_scenario": 300,
    "market_segment": 300,
    "operator": 300,
    "equation": 300,
    "theorem": 300,
}
DEFAULT_MIN = 300


def split_fm(text: str) -> tuple[dict[str, Any] | None, str]:
    if not text.startswith("---"):
        return None, text
    parts = text.split("---", 2)
    if len(parts) < 3:
        return None, text
    try:
        fm = yaml.safe_load(parts[1]) or {}
    except Exception:
        return None, text
    return fm, parts[2]


def meaningful_zh_chars(body: str, exclude: list[str]) -> int:
    text = re.sub(r"^#{1,6}\s+", "", body, flags=re.MULTILINE)
    for s in exclude:
        if s:
            text = text.replace(s, "")
    return len(re.findall(r"[\u4e00-\u9fff]", text))


def has_heading(body: str, pattern: str) -> bool:
    return bool(re.search(pattern, body, re.MULTILINE | re.IGNORECASE))


def index_chapter_sections() -> list[tuple[str, int, str, str]]:
    sections: list[tuple[str, int, str, str]] = []
    for ch_path in sorted(WIKI_CHAPTERS.glob("chapter-*.md")):
        text = ch_path.read_text(encoding="utf-8")
        cur_level = cur_heading = None
        buf: list[str] = []
        for line in text.splitlines():
            m = re.match(r"^(#{1,6})\s+(.+)$", line)
            if m:
                if cur_heading:
                    sections.append((ch_path.name, cur_level, cur_heading, "\n".join(buf)))
                cur_level = len(m.group(1))
                cur_heading = m.group(2)
                buf = []
            else:
                buf.append(line)
        if cur_heading:
            sections.append((ch_path.name, cur_level, cur_heading, "\n".join(buf)))
    return sections


def extract_names_from_appendix(text: str) -> list[str]:
    names: list[str] = []
    m = re.search(r"^#\s+(.+)$", text, re.MULTILINE)
    if m:
        names.extend([x.strip() for x in m.group(1).split("/") if x.strip()])
    for line in text.splitlines():
        if "中文名" in line or "英文名" in line:
            cells = [c.strip().strip("*") for c in line.split("|")]
            if len(cells) >= 3 and cells[2]:
                names.append(cells[2])
    return names


def index_kg_entities() -> dict[str, tuple[Path, str]]:
    idx: dict[str, tuple[Path, str]] = {}
    for p in KG_ENTITIES.rglob("*.md"):
        text = p.read_text(encoding="utf-8")
        names: list[str] = []
        body = text
        if text.startswith("---"):
            parts = text.split("---", 2)
            if len(parts) >= 3:
                try:
                    fm = yaml.safe_load(parts[1])
                    n = fm.get("names", {})
                    if isinstance(n, dict):
                        names = [v for v in n.values() if v]
                    body = parts[2]
                except Exception:
                    pass
        for n in names:
            idx[n.lower()] = (p, body)
    return idx


def index_appendix(dir_name: str) -> dict[str, tuple[Path, str]]:
    idx: dict[str, tuple[Path, str]] = {}
    d = APPENDIX_D / dir_name
    if not d.exists():
        return idx
    for p in d.glob("*.md"):
        text = p.read_text(encoding="utf-8")
        for n in extract_names_from_appendix(text):
            idx[n.lower()] = (p, text)
        # also index by filename stem (e.g. company_bonfiglioli -> bonfiglioli)
        stem = p.stem
        if "_" in stem:
            base = stem.split("_", 1)[1]
            if base:
                idx[base.lower()] = (p, text)
    return idx


def get_keywords(p: Path, fm: dict[str, Any]) -> list[str]:
    kws: list[str] = []
    names = fm.get("names", {}) or {}
    if isinstance(names, dict):
        for lang in ("zh", "en", "ko"):
            v = names.get(lang, "")
            if v and v not in kws:
                kws.append(v)
    for kw in EXTRA_KEYWORDS.get(p.stem, []):
        if kw not in kws:
            kws.append(kw)
    # Add base slug from entity id (e.g. ent_company_bonfiglioli_2024 -> bonfiglioli)
    stem = p.stem
    for prefix in ("ent_", "company_", "component_manufacturer_", "component_", "technology_", "software_platform_", "oem_", "tier1_supplier_"):
        if stem.startswith(prefix):
            base = stem[len(prefix):]
            base = re.sub(r"_\d{4}$", "", base)
            if base and base not in kws:
                kws.append(base.replace("_", " "))
            break
    # split parenthesized variants
    expanded: list[str] = []
    for k in kws:
        expanded.append(k)
        for part in re.split(r"[（(]", k):
            part = re.sub(r"[）)]", "", part).strip()
            if part and part not in expanded and len(part) > 1:
                expanded.append(part)
    # dedupe
    seen: set[str] = set()
    out: list[str] = []
    for k in expanded:
        kl = k.lower()
        if kl not in seen and len(kl) > 1:
            seen.add(kl)
            out.append(k)
    return out


def _contains_word(text: str, kw: str) -> bool:
    """Case-insensitive whole-word/phrase match. Chinese uses substring match."""
    kl = kw.lower()
    tl = text.lower()
    if re.search(r"[\u4e00-\u9fff]", kl):
        return kl in tl
    if len(kl) < 2:
        return False
    pattern = r"(?:^|\W)" + re.escape(kl) + r"(?:\W|$)"
    return bool(re.search(pattern, tl))


def _count_word(text: str, kw: str) -> int:
    kl = kw.lower()
    tl = text.lower()
    if re.search(r"[\u4e00-\u9fff]", kl):
        return tl.count(kl)
    if len(kl) < 2:
        return 0
    pattern = r"(?:^|\W)" + re.escape(kl) + r"(?:\W|$)"
    return len(re.findall(pattern, tl))


def score_text(keywords: list[str], title: str, content: str, require_heading: bool = True) -> tuple[int, bool]:
    score = 0
    heading_match = False
    content_hits = 0
    for kw in keywords:
        kl = kw.lower()
        if _contains_word(title, kw):
            score += 600 + len(kw) * 3
            heading_match = True
        hits = _count_word(content, kw)
        content_hits += hits
        score += hits * 8
    if require_heading and not heading_match:
        return 0, False
    # Boost if multiple distinct keywords appear in content even without heading match
    if not heading_match and content_hits >= 3:
        score += 100
    return score, heading_match


def find_best_source(
    keywords: list[str],
    chapter_sections: list[tuple[str, int, str, str]],
    kg_entities: dict[str, tuple[Path, str]],
    appendix_companies: dict[str, tuple[Path, str]],
    appendix_products: dict[str, tuple[Path, str]],
    etype: str,
) -> tuple[str, Path, str, int] | None:
    best: tuple[int, str, Path, str, int] | None = None

    # Chapter sections - heading match first
    for ch, level, heading, content in chapter_sections:
        if level <= 1:
            continue
        score, hmatch = score_text(keywords, heading, content, require_heading=True)
        if not hmatch:
            continue
        score += level * 5 + len(content) // 50
        if best is None or score > best[0]:
            best = (score, f"{ch}#{heading}", Path("wiki/docs/chapters") / ch, content, level)

    # Fallback: content-heavy sections without heading match (only for high-level topics,
    # not for methods/principles/technologies where off-topic sections would be harmful).
    if best is None and etype not in {
        "method", "principle", "formalism", "foundation", "algorithm",
        "technology", "component", "software_platform", "tool_equipment",
        "material", "equation", "theorem",
    }:
        for ch, level, heading, content in chapter_sections:
            if level <= 1:
                continue
            score, _ = score_text(keywords, heading, content, require_heading=False)
            if score < 120:
                continue
            score += level * 2 + len(content) // 100
            if best is None or score > best[0]:
                best = (score, f"{ch}#{heading}", Path("wiki/docs/chapters") / ch, content, level)

    # KG entities / appendix for component/company/technology/material/software
    if etype in {
        "component",
        "material",
        "software_platform",
        "tool_equipment",
        "company",
        "oem",
        "tier1_supplier",
        "tier2_supplier",
        "component_manufacturer",
        "technology",
        "robot_system",
    }:
        for idx, label in (
            (appendix_companies, "appendix-d/companies"),
            (appendix_products, "appendix-d/products"),
            (kg_entities, "kg/entities"),
        ):
            matched_key = None
            matched_score = 0
            for key in idx:
                for kw in keywords:
                    kl = kw.lower()
                    # Chinese/exact short match
                    is_chinese = bool(re.search(r"[\u4e00-\u9fff]", kl))
                    if is_chinese:
                        if kl in key or key in kl:
                            sc = 800 if label.startswith("appendix") else 700
                            sc += min(len(kl), len(key)) * 3
                            if sc > matched_score:
                                matched_score = sc
                                matched_key = key
                    else:
                        # English whole-word match only, skip very short tokens
                        if len(kl) < 4:
                            continue
                        pattern = r"(?:^|\W)" + re.escape(kl) + r"(?:\W|$)"
                        if re.search(pattern, key, re.IGNORECASE):
                            sc = 800 if label.startswith("appendix") else 700
                            sc += min(len(kl), len(key)) * 3
                            if sc > matched_score:
                                matched_score = sc
                                matched_key = key
            if matched_key:
                p, text = idx[matched_key]
                cleaned = clean_source_body(text)
                if len(re.findall(r"[\u4e00-\u9fff]", cleaned)) < 50:
                    continue
                score = matched_score + len(cleaned) // 50
                if best is None or score > best[0]:
                    best = (score, f"{label}/{p.name}", p, cleaned, 1)

    if best is None:
        return None
    return best[1], best[2], best[3], best[4]


def clean_source_body(text: str) -> str:
    """Strip frontmatter and navigation banners from wiki source."""
    if text.startswith("---"):
        parts = text.split("---", 2)
        if len(parts) >= 3:
            text = parts[2]
    # remove first navigation blockquote if present
    lines = text.splitlines()
    out: list[str] = []
    skip_banner = True
    for line in lines:
        if skip_banner and line.strip().startswith(">"):
            continue
        skip_banner = False
        out.append(line)
    return "\n".join(out).strip()


def build_body(title: str, source_text: str, source_label: str, fm: dict[str, Any]) -> str:
    source_text = clean_source_body(source_text)
    # Demote source headings so they sit under our core section
    demoted = re.sub(r"^(#{1,5})\s+", lambda m: "#" * (len(m.group(1)) + 1) + " ", source_text, flags=re.MULTILINE)

    lines: list[str] = []
    lines.append("## 概述")
    lines.append(f"{title}是人形机器人领域的重要{fm.get('type', '知识实体')}。以下内容整理自项目 Wiki，供深入查阅。")
    lines.append("")
    lines.append("## 核心内容")
    lines.append(demoted)
    lines.append("")
    lines.append("## 参考")
    sources = fm.get("sources", [])
    if sources:
        for s in sources:
            t = s.get("title", "")
            u = s.get("url", "")
            if t and u:
                lines.append(f"- [{t}]({u})")
            elif t:
                lines.append(f"- {t}")
    lines.append(f"- 项目 Wiki：{source_label}")
    lines.append("")
    return "\n".join(lines)


def main() -> int:
    chapter_sections = index_chapter_sections()
    kg_entities = index_kg_entities()
    appendix_companies = index_appendix("companies")
    appendix_products = index_appendix("products")

    updated = 0
    skipped: list[tuple[str, str]] = []

    for p in sorted(RESEARCH_DIR.rglob("*.md")):
        fm, body = split_fm(p.read_text(encoding="utf-8"))
        if fm is None:
            continue
        etype = fm.get("type", "")
        if etype in ("paper", "report"):
            continue
        min_chars = MIN_CHARS.get(etype, DEFAULT_MIN)

        names = fm.get("names", {}) or {}
        summary = fm.get("summary", {}) or {}
        exclude: list[str] = []
        for lang in ("zh", "en", "ko"):
            n = names.get(lang, "") if isinstance(names, dict) else ""
            s = summary.get(lang, "") if isinstance(summary, dict) else ""
            if n:
                exclude.append(n)
            if s:
                exclude.append(s)

        if meaningful_zh_chars(body, exclude) >= min_chars:
            continue

        keywords = get_keywords(p, fm)
        title = names.get("zh", "") or names.get("en", "") or p.stem
        result = find_best_source(
            keywords,
            chapter_sections,
            kg_entities,
            appendix_companies,
            appendix_products,
            etype,
        )
        if not result:
            skipped.append((p.stem, "no source match"))
            continue

        source_label, source_path, source_text, _level = result
        new_body = build_body(title, source_text, source_label, fm)

        # Fix summary
        zh_summary = summary.get("zh", "") if isinstance(summary, dict) else ""
        if not zh_summary or zh_summary == names.get("zh", ""):
            fm.setdefault("summary", {})
            fm["summary"]["zh"] = f"{title}——人形机器人{etype}知识实体，详见正文。"

        fm["verification"] = fm.get("verification", {})
        fm["verification"]["notes"] = f"Body backfilled from {source_label} by scripts/backfill_nonpaper_entries.py."
        fm["verification"]["reviewed_at"] = "2026-07-14"

        new_yaml = yaml.safe_dump(fm, allow_unicode=True, sort_keys=False, width=120, default_flow_style=False)
        p.write_text(f"---\n{new_yaml}---\n{new_body}\n", encoding="utf-8")
        updated += 1
        print(f"  UPDATED {p.stem} <- {source_label}")

    print(f"\nUpdated {updated} entries; skipped {len(skipped)}")
    for eid, reason in skipped[:30]:
        print(f"  SKIP {eid}: {reason}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
