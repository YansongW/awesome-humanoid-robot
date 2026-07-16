#!/usr/bin/env python3
"""Clean entry content in research/:

1. Rebuild bodies that contain scraped web junk (CSS/JS) -- keep clean sentences only.
2. Clean summaries that leaked markdown/boilerplate ("核心内容 ### ...", `**`, tables).
3. Replace raw domain/layer/type slugs in body boilerplate with readable zh labels.
4. De-duplicate identical 概述 / 核心内容 sections (truncate 概述 to the lead sentences).
5. Strip leading punctuation junk from names.

Usage:
    python scripts/clean_entry_content.py           # dry-run report
    python scripts/clean_entry_content.py --write   # apply changes
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "website"))
from builder.loader import DOMAIN_LABELS, LAYER_LABELS, TYPE_LABELS  # noqa: E402

DOMAIN_ZH = DOMAIN_LABELS["zh"]
LAYER_ZH = LAYER_LABELS["zh"]
TYPE_ZH = TYPE_LABELS["zh"]

STRONG_JUNK = [
    "!important", "data:image", "<style", ":before", ".fa-", "getElementById",
    "classList", "addEventListener", "querySelector", "no-repeat",
]
WEAK_JUNK = [
    "function ", "window.", "document.", "url(", "var(--", "@media",
    "console.", "setTimeout", "px;", "px}", "background:", "font-size:",
    "<div", "<span", "onclick",
]
JUNK_MARKERS = STRONG_JUNK + WEAK_JUNK


def is_junk_body(body: str) -> bool:
    if any(marker in body for marker in STRONG_JUNK):
        return True
    weak_hits = {m for m in WEAK_JUNK if m in body}
    return len(weak_hits) >= 2

BOILERPLATE_RES = [
    re.compile(r"^核心内容\s*"),
    re.compile(r"###\s*[^\n]{0,60}?的定义与定位\s*"),
    re.compile(r"[^\n]{0,60}?属于\s*\*\*[a-z_]+\*\*\s*类型[。，,]\s*"),
    re.compile(r"[^\n]{0,60}?属于\s*[a-z_]+\s*类型[。，,]\s*"),
    re.compile(r"所属领域包括：[^。]*。\s*"),
    re.compile(r"价值链层级：[^。]*。\s*"),
    re.compile(r"英文名称为\s*\*[^*]*\*。\s*"),
    re.compile(r"韩文名称为\s*\*[^*]*\*。\s*"),
]

BOILERPLATE_HINTS = ("###", "的定义与定位", "所属领域包括", "价值链层级", "核心内容")

DOMAIN_SLUG_RE = re.compile(r"\b(?:0\d|1[0-2])_[a-z_]+\b")


def split_file(text: str):
    m = re.match(r"\A---\n(.*?)\n---\n(.*)\Z", text, re.S)
    if not m:
        return None, None
    try:
        fm = yaml.safe_load(m.group(1))
    except yaml.YAMLError:
        return None, None
    if not isinstance(fm, dict):
        return None, None
    return fm, m.group(2)


def dump_file(fm: dict, body: str) -> str:
    return (
        "---\n"
        + yaml.safe_dump(fm, allow_unicode=True, sort_keys=False, width=120)
        + "---\n"
        + body
    )


SITE_BOILER = [
    "subscribe", "cookie", "privacy policy", "all rights reserved", "© copyright",
    "nondiscrimination", "more headlines", "newsletter", "document.write",
    "sign up", "follow us", "public charity", "enjoy more free content",
    "terms of", "ad privacy", "contact & support", "accessibility",
    "online robotics trade magazine", "read more", "advertisement",
    "inform our readers", "for more exclusive content", "join our",
    "join the world's largest", "spectrum's articles", "learn more about ieee",
    "pdf downloads", "become a member", "our articles, videos",
    "create an account", "sign in", "log in", "for full access",
]


def norm_boiler(s: str) -> str:
    return s.lower().replace("’", "'").replace("‘", "'")


def is_clean_sentence(s: str) -> bool:
    s = s.strip()
    if len(s) < 20:
        return False
    if any(b in norm_boiler(s) for b in SITE_BOILER):
        return False
    if any(marker in s for marker in JUNK_MARKERS):
        return False
    if "{" in s or "}" in s or "<" in s or ";" in s:
        return False
    alnum = sum(1 for c in s if c.isalnum() or "一" <= c <= "鿿")
    if alnum / max(len(s), 1) < 0.5:
        return False
    return True


def salvage_prefix(s: str) -> str:
    """Keep the clean leading fragment of a sentence glued to CSS/JS junk."""
    cut = len(s)
    for marker in JUNK_MARKERS + ["{", "}", "<", ";", "')", '")', "'}"]:
        i = s.find(marker)
        if 0 <= i < cut:
            cut = i
    normed = norm_boiler(s)
    for b in SITE_BOILER:
        i = normed.find(b)
        if 0 <= i < cut:
            cut = i
    prefix = re.sub(r"[\s'\")\]]+$", "", s[:cut]).strip()
    if len(prefix) >= 20 and is_clean_sentence(prefix):
        return prefix
    return ""


def extract_reference_section(body: str, fm: dict) -> str:
    m = re.search(r"^##\s*参考\s*\n(.*?)(?=^##\s|\Z)", body, re.M | re.S)
    if m and m.group(1).strip():
        return "## 参考\n" + m.group(1).strip()
    urls = [s.get("url") for s in fm.get("sources", []) or [] if isinstance(s, dict) and s.get("url")]
    if urls:
        return "## 参考\n" + "\n".join(f"- {u}" for u in urls)
    return ""


def rebuild_junk_body(body: str, fm: dict) -> str:
    # Collect clean sentences from the whole body (excluding the 参考 section).
    text = re.sub(r"^##\s*参考\s*\n.*", "", body, flags=re.M | re.S)
    text = re.sub(r"^#{1,6}\s*.*$", " ", text, flags=re.M)
    sentences = re.split(r"(?<=[.!?。！？])\s+|\n+", text)
    seen, kept = set(), []
    for s in sentences:
        s = re.sub(r"\s+", " ", s).strip()
        if not is_clean_sentence(s):
            s = salvage_prefix(s)
            if not s:
                continue
        key = s[:60]
        if key in seen:
            continue
        seen.add(key)
        kept.append(s)
    full = " ".join(kept)
    summary_text = (fm.get("summary", {}) or {}).get("en") or (fm.get("summary", {}) or {}).get("zh") or ""
    if len(full.split()) < 90 and summary_text:
        # Thin salvage (e.g. paywalled articles): pad with the clean summary.
        full = (summary_text + " " + full).strip()
    lead = " ".join(kept[:2]) if kept else full
    ref = extract_reference_section(body, fm)
    parts = ["## 概述", lead, "", "## 核心内容", full]
    if ref:
        parts += ["", ref]
    return "\n".join(parts) + "\n"


# ------------------------------------------------------------------ summaries
def has_boilerplate(s: str) -> bool:
    return any(h in s for h in BOILERPLATE_HINTS)


def clean_summary_text(s: str) -> str:
    if not s:
        return s
    out = s
    if has_boilerplate(out):
        for rx in BOILERPLATE_RES:
            out = rx.sub("", out)
    # strip leftover markdown emphasis / heading markers / table rows
    out = re.sub(r"\|[^\n]*\|", " ", out)  # table rows
    out = out.replace("**", "")
    out = re.sub(r"^#{1,6}\s*", "", out)
    out = re.sub(r"\s+", " ", out).strip()
    return out


def first_body_paragraph(body: str) -> str:
    m = re.search(r"^##\s*概述\s*\n(.+)", body, re.M)
    if m:
        return re.sub(r"\s+", " ", m.group(1)).strip()
    return ""


# --------------------------------------------------------------- slug cleanup
def replace_slugs(text: str) -> str:
    def dom_sub(m: re.Match) -> str:
        return DOMAIN_ZH.get(m.group(0), m.group(0))

    out = DOMAIN_SLUG_RE.sub(dom_sub, text)

    # 价值链层级：validation_markets / 智能层, validation_markets -> readable labels
    def layer_line_sub(m: re.Match) -> str:
        line = m.group(0)
        for slug, label in LAYER_ZH.items():
            line = re.sub(rf"\b{re.escape(slug)}\b", label, line)
        return line

    out = re.sub(r"价值链层级：[^\n。]*", layer_line_sub, out)

    # 属于 **application_scenario** 类型 -> 属于**应用场景**类型
    def type_bold_sub(m: re.Match) -> str:
        slug = m.group(1)
        return f"**{TYPE_ZH.get(slug, slug)}**"

    out = re.sub(r"\*\*([a-z_]+)\*\*", type_bold_sub, out)

    # 关键application_scenario之一 / 重要standard / 属于 company 类型
    for slug, label in TYPE_ZH.items():
        out = out.replace(f"关键{slug}之一", f"关键{label}之一")
        out = out.replace(f"重要{slug}", f"重要{label}")
        out = out.replace(f"属于 {slug} 类型", f"属于{label}类型")
    return out


# ---------------------------------------------------------------------- names
def clean_name(n: str) -> str:
    out = n.strip()
    out = re.sub(r"^[!！\s]+", "", out)
    out = out.strip()
    return out


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()

    stats = {"junk": 0, "summary": 0, "slug": 0, "name": 0, "yaml_err": 0}
    samples: list[str] = []

    for path in sorted(ROOT.glob("research/**/*.md")):
        text = path.read_text(encoding="utf-8")
        fm, body = split_file(text)
        if fm is None or body is None:
            stats["yaml_err"] += 1
            continue
        changed = False

        # 1. junk body rebuild
        if is_junk_body(body):
            new_body = rebuild_junk_body(body, fm)
            if new_body != body:
                body = new_body
                changed = True
                stats["junk"] += 1
                if len(samples) < 3:
                    samples.append(f"junk: {path.name}")

        # 2. summaries
        summary = fm.get("summary")
        if isinstance(summary, dict):
            for lang in ("zh", "en", "ko"):
                s = summary.get(lang)
                if not isinstance(s, str) or not s:
                    continue
                cleaned = clean_summary_text(s)
                if lang == "zh" and has_boilerplate(s) and len(cleaned) < 20:
                    names_zh = (fm.get("names", {}) or {}).get("zh", "")
                    fb = first_body_paragraph(body)
                    if len(fb) < 20 or fb == names_zh:
                        m2 = re.search(r"^##\s*核心内容\s*\n(?:#{1,6}\s*[^\n]*\n)?(.+)", body, re.M)
                        fb2 = re.sub(r"\s+", " ", m2.group(1)).strip() if m2 else ""
                        if len(fb2) > len(fb):
                            fb = fb2
                    cleaned = fb[:300] or cleaned
                if cleaned != s:
                    summary[lang] = cleaned
                    changed = True
                    stats["summary"] += 1
                    if lang == "zh" and len(samples) < 6:
                        samples.append(f"summary: {path.name} :: {cleaned[:60]}")

        # 3. slugs in body
        new_body = replace_slugs(body)
        if new_body != body:
            body = new_body
            changed = True
            stats["slug"] += 1

        # 4. names (render-level dedup of 概述/核心内容 happens in the builder)
        names = fm.get("names")
        if isinstance(names, dict):
            for lang in ("zh", "en", "ko"):
                n = names.get(lang)
                if isinstance(n, str) and n:
                    cleaned = clean_name(n)
                    if cleaned != n:
                        names[lang] = cleaned
                        changed = True
                        stats["name"] += 1

        if changed and args.write:
            # round-trip validation before writing
            out = dump_file(fm, body)
            check_fm, _ = split_file(out)
            if check_fm is None:
                print(f"SKIP (yaml round-trip failed): {path}")
                continue
            path.write_text(out, encoding="utf-8")

    print("stats:", stats)
    for s in samples:
        print(" ", s)
    if not args.write:
        print("dry-run; re-run with --write to apply")


if __name__ == "__main__":
    main()
