#!/usr/bin/env python3
"""
Fix warning-level quality issues in research entries:
- Fill/extend summaries from the body overview.
- Add a `## 参考` section when source URLs exist but the body lacks one.

Usage:
    python scripts/fix_warning_entries.py [--dry-run]
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from typing import Any

import yaml

ROOT = Path(__file__).parent.parent
RESEARCH_DIR = ROOT / "research"
MIN_SUMMARY_ZH = 80


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


def extract_overview(body: str) -> str:
    """Return the first substantial paragraph after the ## 概述 heading, falling
    back to the first substantial paragraph of the body."""
    def first_para(text: str) -> str:
        for para in re.split(r"\n\s*\n", text):
            para = re.sub(r"^#{1,6}\s+", "", para).strip()
            para = re.sub(r"\s+", " ", para)
            if len(para) >= 60 and not para.lower().startswith(("参考", "references", "참고")):
                return para
        return ""

    # Prefer the content inside the 概述 section.
    m = re.search(r"^#{1,6}\s*概述\s*\n(.*?)(?=^#{1,6}\s|\Z)", body, re.MULTILINE | re.DOTALL)
    if m:
        result = first_para(m.group(1))
        if result:
            return result
    return first_para(body)


def is_summary_bad(fm: dict[str, Any]) -> bool:
    summary = fm.get("summary", {}) or {}
    if not isinstance(summary, dict):
        return True
    zh = summary.get("zh", "")
    if not zh:
        return True
    if len(zh) < MIN_SUMMARY_ZH:
        return True
    title = (fm.get("names", {}) or {}).get("zh", "")
    if zh.strip() == title.strip():
        return True
    return False


def has_reference_section(body: str) -> bool:
    return bool(re.search(r"^#{1,6}\s*(参考|References|참고)\s*$", body, re.MULTILINE | re.IGNORECASE))


def add_reference_section(body: str, fm: dict[str, Any]) -> str:
    sources = fm.get("sources", []) or []
    urls = [s.get("url", "") for s in sources if s.get("url")]
    if not urls:
        return body
    ref = "\n## 参考\n"
    for u in urls:
        ref += f"- {u}\n"
    return body.rstrip() + "\n" + ref


def main() -> int:
    parser = argparse.ArgumentParser(description="Fix warning-level quality issues in research entries.")
    parser.add_argument("--dry-run", action="store_true", help="Do not write files")
    args = parser.parse_args()

    updated = 0
    skipped = 0

    for p in sorted(RESEARCH_DIR.rglob("*.md")):
        text = p.read_text(encoding="utf-8")
        fm, body = split_fm(text)
        if fm is None:
            skipped += 1
            continue

        changed = False

        # Fix summary
        if is_summary_bad(fm):
            overview = extract_overview(body)
            if overview:
                summary = fm.setdefault("summary", {})
                summary["zh"] = overview[:600]
                if not summary.get("en"):
                    summary["en"] = overview[:600]
                changed = True

        # Add reference section
        if not has_reference_section(body):
            new_body = add_reference_section(body, fm)
            if new_body != body:
                body = new_body
                changed = True

        if changed and not args.dry_run:
            new_yaml = yaml.safe_dump(fm, allow_unicode=True, sort_keys=False, width=120, default_flow_style=False)
            p.write_text(f"---\n{new_yaml}---\n{body}\n", encoding="utf-8")
            updated += 1
        elif changed:
            updated += 1
        else:
            skipped += 1

    print(f"Updated {updated}, skipped {skipped}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
