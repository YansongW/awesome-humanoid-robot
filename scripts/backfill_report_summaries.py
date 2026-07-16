#!/usr/bin/env python3
"""
Backfill empty report/blog entries with a short summary fetched from their
source URL's <meta name="description"> tag or first paragraph.

Usage:
    python scripts/backfill_report_summaries.py [--dry-run]
"""

from __future__ import annotations

import argparse
import html
import re
import sys
import time
from pathlib import Path
from typing import Any

import requests
import yaml

ROOT = Path(__file__).parent.parent
SEARCH_DIRS = [p for p in (ROOT / "research").iterdir() if p.is_dir()]


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


def is_empty(fm: dict[str, Any], body: str) -> bool:
    body_clean = re.sub(r"^#{1,6}\s+", "", body, flags=re.MULTILINE)
    body_clean = re.split(r"\n## 参考|\n## References|\n## 참고", body_clean, flags=re.IGNORECASE)[0]
    summary = fm.get("summary", {}) or {}
    if isinstance(summary, dict):
        for v in summary.values():
            if isinstance(v, str):
                body_clean = body_clean.replace(v, "")
    zh = len(re.findall(r"[\u4e00-\u9fff]", body_clean))
    en = len(re.findall(r"[A-Za-z]{2,}", body_clean))
    return zh < 50 and en < 80


def fetch_summary(url: str) -> str | None:
    if not url or not url.startswith(("http://", "https://")):
        return None
    try:
        r = requests.get(url, timeout=15, headers={"User-Agent": "Mozilla/5.0"})
        r.raise_for_status()
    except Exception:
        return None
    text = r.text

    # Meta description
    meta = ""
    m = re.search(
        r'<meta[^>]+(?:name|property)=["\'](?:description|og:description)["\'][^>]+content=["\']([^"\']+)',
        text,
        re.IGNORECASE,
    )
    if not m:
        m = re.search(
            r'<meta[^>]+content=["\']([^"\']+)["\'][^>]+(?:name|property)=["\'](?:description|og:description)["\']',
            text,
            re.IGNORECASE,
        )
    if m:
        meta = html.unescape(m.group(1)).strip()

    # If meta is already long enough, use it.
    if meta and len(meta) >= 250:
        return meta

    # Otherwise collect the first few substantial paragraphs.
    sys.path.insert(0, str(ROOT / "scripts"))
    from clean_entry_content import JUNK_MARKERS, SITE_BOILER, norm_boiler

    paragraphs: list[str] = []
    for p in re.findall(r"<p[^>]*>(.*?)</p>", text, re.IGNORECASE | re.DOTALL):
        p = re.sub(r"<[^>]+>", " ", p)
        p = html.unescape(p).strip()
        p = re.sub(r"\s+", " ", p)
        # Skip navigation/footer-ish fragments and scraped CSS/JS junk.
        if len(p) < 80:
            continue
        if any(marker in p for marker in JUNK_MARKERS):
            continue
        if any(b in norm_boiler(p) for b in SITE_BOILER):
            continue
        paragraphs.append(p)
        if len(paragraphs) >= 3:
            break

    combined = "\n\n".join([meta] + paragraphs) if meta else "\n\n".join(paragraphs)
    combined = re.sub(r"\s+", " ", combined).strip()
    return combined if len(combined) >= 120 else None


def build_body(summary: str, url: str) -> str:
    return (
        "## 概述\n"
        f"{summary}\n\n"
        "## 核心内容\n"
        f"{summary}\n\n"
        "## 参考\n"
        f"- {url}\n"
    )


def main() -> int:
    parser = argparse.ArgumentParser(description="Backfill empty report/blog entries from source pages.")
    parser.add_argument("--dry-run", action="store_true", help="Do not write files")
    parser.add_argument("--ids", nargs="*", help="Only process these entry IDs (stems)")
    parser.add_argument("--all-types", action="store_true", help="Process all entity types, not just report/paper")
    args = parser.parse_args()

    updated = 0
    failed = 0
    skipped = 0

    paths = sorted({p for d in SEARCH_DIRS for p in d.glob("*.md")})
    if args.ids:
        id_set = set(args.ids)
        paths = [p for p in paths if p.stem in id_set]

    for p in paths:
        text = p.read_text(encoding="utf-8")
        fm, body = split_fm(text)
        if fm is None:
            continue
        if not args.all_types and fm.get("type") not in ("report", "paper"):
            continue
        summary = fm.get("summary", {}) or {}
        names = fm.get("names", {}) or {}
        summary_is_title = (
            isinstance(summary, dict)
            and isinstance(names, dict)
            and summary.get("zh", "").strip() == names.get("zh", "").strip()
        )
        if not is_empty(fm, body) and not summary_is_title:
            skipped += 1
            continue

        sources = fm.get("sources", []) or []
        url = ""
        for s in sources:
            url = s.get("url", "")
            if url:
                break

        summary = fetch_summary(url) if url else None
        if not summary:
            failed += 1
            continue

        names = fm.get("names", {}) or {}
        summaries = fm.get("summary", {}) or {}
        if not summaries.get("en") or summary_is_title:
            summaries["en"] = summary[:800]
        if not summaries.get("zh") or summary_is_title:
            summaries["zh"] = summary[:800]
        fm["summary"] = summaries

        ver = fm.get("verification", {}) or {}
        ver["notes"] = f"Summary backfilled by scripts/backfill_report_summaries.py from {url}."
        ver["reviewed_at"] = "2026-07-15"
        fm["verification"] = ver

        new_body = build_body(summary, url)
        if not args.dry_run:
            new_yaml = yaml.safe_dump(fm, allow_unicode=True, sort_keys=False, width=120, default_flow_style=False)
            p.write_text(f"---\n{new_yaml}---\n{new_body}\n", encoding="utf-8")
        updated += 1
        time.sleep(0.5)

    print(f"Updated {updated}, skipped {skipped}, failed {failed}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
