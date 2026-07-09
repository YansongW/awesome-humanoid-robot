#!/usr/bin/env python3
"""
Enrich the 86 Wiki-gap entity summaries from the source Wiki chapter text.

For each gap entity listed in data/wiki-chapter-mapping.yaml, this script:
- reads the corresponding wiki/docs/chapters/chapter-NN.md file,
- finds sentences that mention the entity's Chinese name,
- picks the longest informative sentence as summary.zh,
- leaves summary.en as a fallback generic English sentence.
"""

import re
import sys
from pathlib import Path
from typing import Optional

import yaml

ROOT = Path(__file__).parent.parent
MAPPING_FILE = ROOT / "data" / "wiki-chapter-mapping.yaml"
WIKI_DIR = ROOT / "wiki" / "docs" / "chapters"
RESEARCH_DIR = ROOT / "research"


def load_frontmatter(path: Path) -> tuple[dict, str, str]:
    text = path.read_text(encoding="utf-8")
    _, rest = text.split("---", 1)
    ym, body = rest.split("---", 1)
    return yaml.safe_load(ym), ym, body


def dump_frontmatter(data: dict, body: str) -> str:
    ym = yaml.safe_dump(data, allow_unicode=True, sort_keys=False, default_flow_style=False, width=120)
    body_stripped = body.lstrip("\n")
    return f"---\n{ym}---\n{body_stripped}"


def clean_sentence(sentence: str) -> str:
    # Remove Markdown links and formatting.
    sentence = re.sub(r"!?\[([^\]]*)\]\([^)]*\)", r"\1", sentence)
    sentence = re.sub(r"`([^`]+)`", r"\1", sentence)
    sentence = re.sub(r"\*\*", "", sentence)
    sentence = sentence.replace("\n", " ").strip()
    # Collapse whitespace.
    sentence = re.sub(r"\s+", " ", sentence)
    return sentence


def normalize_name(name: str) -> str:
    """Strip Markdown/MkDocs noise and normalize whitespace/punctuation."""
    name = name.strip()
    # Remove parenthetical abbreviations for matching, but keep the root term.
    name = re.sub(r"[（(][^）)]+[）)]", "", name)
    name = name.replace("/", " ")
    name = re.sub(r"\s+", "", name)
    return name


def name_variants(name: str) -> list[str]:
    """Generate possible Chinese name variants for matching."""
    variants = {name, normalize_name(name)}
    # Add space-separated version for terms like "PID控制" -> "PID 控制".
    spaced = re.sub(r"([a-zA-Z0-9]+)([\u4e00-\u9fff])", r"\1 \2", name)
    spaced = re.sub(r"([\u4e00-\u9fff])([a-zA-Z0-9]+)", r"\1 \2", spaced)
    variants.add(spaced)
    variants.add(normalize_name(spaced))
    # Drop empty.
    return [v for v in variants if len(v) >= 2]


def find_best_sentence(chapter_text: str, names: list[str], min_len: int = 20, max_len: int = 200) -> Optional[str]:
    """Find the best sentence mentioning any of `names` from the chapter text."""
    sentences = re.split(r"[。！？\n]", chapter_text)
    candidates = []
    for raw in sentences:
        raw = raw.strip()
        if not raw or len(raw) < min_len:
            continue
        cleaned = clean_sentence(raw)
        if len(cleaned) < min_len:
            continue
        matched = False
        for name in names:
            if name in cleaned:
                matched = True
                break
        if not matched:
            continue
        # Prefer sentences that define/explain (contain these verbs).
        score = 0
        if re.search(r"(是|指|为|表示|定义为|用于|通过|基于|利用|借助)", cleaned):
            score += 10
        # Penalize very long sentences.
        score -= max(0, len(cleaned) - max_len) * 0.05
        candidates.append((score, cleaned))

    if not candidates:
        return None
    candidates.sort(key=lambda x: -x[0])
    best = candidates[0][1]
    if len(best) > max_len:
        # Try to truncate at a comma or period-like boundary.
        truncate_at = best.rfind("，", 0, max_len)
        if truncate_at < min_len:
            truncate_at = max_len
        best = best[:truncate_at] + "…" if truncate_at < len(best) else best
    return best


def main() -> int:
    if not MAPPING_FILE.exists():
        print(f"Mapping file not found: {MAPPING_FILE}")
        return 1

    mapping = yaml.safe_load(MAPPING_FILE.read_text(encoding="utf-8"))
    enriched = 0
    skipped = 0

    for chapter in mapping.get("chapters", []):
        chapter_num = chapter.get("number")
        chapter_file = WIKI_DIR / f"chapter-{chapter_num:02d}.md"
        if not chapter_file.exists():
            continue
        chapter_text = chapter_file.read_text(encoding="utf-8")
        # Remove frontmatter.
        if chapter_text.startswith("---"):
            _, rest = chapter_text.split("---", 1)
            _, chapter_text = rest.split("---", 1)

        for gap in chapter.get("gaps", []):
            eid = gap.get("id")
            name = gap.get("name", "")
            if not eid or not name:
                continue
            entity_path = None
            for candidate in RESEARCH_DIR.rglob(f"{eid}.md"):
                entity_path = candidate
                break
            if not entity_path:
                skipped += 1
                continue

            try:
                data, _, body = load_frontmatter(entity_path)
            except Exception as e:
                print(f"WARN: failed to parse {entity_path}: {e}", file=sys.stderr)
                skipped += 1
                continue

            entity_zh = (data.get("names") or {}).get("zh", "")
            names_to_try = name_variants(name)
            if entity_zh and entity_zh != name:
                names_to_try.extend(name_variants(entity_zh))
            names_to_try = sorted(set(names_to_try), key=len, reverse=True)

            best_zh = find_best_sentence(chapter_text, names_to_try)
            if not best_zh:
                skipped += 1
                continue

            summary = data.setdefault("summary", {})
            old_zh = summary.get("zh", "")
            # Only overwrite if current summary is the generic placeholder.
            if "相关知识节点" in old_zh or not old_zh:
                summary["zh"] = best_zh
                enriched += 1
            else:
                skipped += 1
                continue

            # Keep English summary as a generic fallback if it's placeholder.
            en_name = data.get("names", {}).get("en") or ""
            old_en = summary.get("en", "")
            if "is a knowledge node" in old_en or not old_en:
                summary["en"] = f"{en_name}: {best_zh[:120]}..." if len(best_zh) > 120 else f"{en_name}: {best_zh}"

            entity_path.write_text(dump_frontmatter(data, body), encoding="utf-8")

    print(f"Enriched {enriched} entity summaries from Wiki; skipped {skipped}.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
