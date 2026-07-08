#!/usr/bin/env python3
"""Fetch Unitree official news and ingest relevant items as report entries.

Usage:
    python scripts/ingest_unitree_news.py --dry-run
    python scripts/ingest_unitree_news.py
"""

from __future__ import annotations

import argparse
import json
import re
from datetime import date
from pathlib import Path
from typing import Any

import requests
import yaml

from ai4sci_lib import config, entry_builder


ROOT = config.ROOT
RESEARCH_DIR = config.RESEARCH_DIR
LIST_URL = "https://api.unitree.com/website/news/list"
INFO_URL = "https://api.unitree.com/website/news/info"
OUTPUT_PATH = ROOT / "data" / "curated" / "unitree_news_latest.json"

KEYWORDS = [
    "humanoid", "robot", "robotics", "GR00T", "Isaac", "G1", "H1", "H2", "G2",
    "dexterous", "manipulation", "locomotion", "embodied", "AI",
]


def load_existing_titles() -> set[str]:
    titles: set[str] = set()
    for path in RESEARCH_DIR.rglob("*.md"):
        try:
            text = path.read_text(encoding="utf-8")
            if not text.startswith("---"):
                continue
            _, rest = text.split("---", 1)
            yaml_text, _ = rest.split("---", 1)
            data = yaml.safe_load(yaml_text) or {}
            names = data.get("names", {})
            if isinstance(names, dict):
                titles.add(names.get("en", "").strip().lower())
                titles.add(names.get("zh", "").strip().lower())
        except Exception:
            continue
    return titles


def fetch_list() -> list[dict[str, Any]]:
    resp = requests.get(LIST_URL, timeout=30, headers={"User-Agent": "Mozilla/5.0"})
    resp.raise_for_status()
    data = resp.json()
    return data.get("data", {}).get("items", [])


def fetch_detail(news_id: str) -> dict[str, Any]:
    try:
        resp = requests.get(INFO_URL, params={"id": news_id}, timeout=20, headers={"User-Agent": "Mozilla/5.0"})
        resp.raise_for_status()
        data = resp.json()
        return data.get("data", {}) or {}
    except Exception:
        return {}


def clean_html(raw: str) -> str:
    text = re.sub(r"<[^>]+>", " ", raw)
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def is_relevant(item: dict[str, Any]) -> bool:
    text = f"{item.get('title','')} {item.get('description','')} {item.get('subTitle','')}".lower()
    return any(kw.lower() in text for kw in KEYWORDS)


def build_entry(
    item: dict[str, Any],
    detail: dict[str, Any],
    existing_titles: set[str],
    existing_ids: set[str],
) -> dict[str, Any] | None:
    title = item.get("title", "").strip()
    if not title:
        return None
    title_key = title.lower()
    if title_key in existing_titles:
        print(f"[skip duplicate title] {title}")
        return None

    year = str(date.today().year)
    m = re.search(r"20\d{2}", item.get("postTime", ""))
    if m:
        year = m.group(0)

    title_slug = entry_builder._slugify(title, max_len=30)
    ent_id = f"ent_report_unitree_{title_slug}_{year}"
    candidate_id = ent_id
    counter = 1
    while candidate_id in existing_ids:
        candidate_id = f"{ent_id}_{counter}"
        counter += 1
    ent_id = candidate_id
    existing_ids.add(ent_id)
    existing_titles.add(title_key)

    names = {"en": title, "zh": title, "ko": ""}

    summary_text = item.get("description", "") or title
    article = detail.get("article", {})
    content = article.get("content", "")
    if content:
        summary_text = clean_html(content)[:500]
    summary = {"en": summary_text, "zh": summary_text, "ko": ""}

    tags = set(["unitree", "robotics", "company_news"])
    for kw in ["humanoid", "G1", "H1", "H2", "GR00T", "dexterous", "manipulation", "locomotion"]:
        if kw.lower() in title.lower():
            tags.add(entry_builder._slugify(kw, max_len=20))
    tags = sorted(t for t in tags if t)

    today = str(date.today())
    news_id = item.get("id", "")
    detail_url = f"https://www.unitree.com/mobile/news"
    sources = [
        {
            "id": "src_001",
            "type": "website",
            "title": title,
            "url": detail_url,
            "date": item.get("postTime", "").split()[0] if item.get("postTime") else year,
            "accessed_at": today,
        }
    ]

    return {
        "$id": ent_id,
        "$schema": "../../data/schema/v1/entry_schema.json",
        "$version": 1,
        "type": "report",
        "names": names,
        "summary": summary,
        "domains": ["11_applications_markets", "06_design_engineering"],
        "layers": ["midstream", "validation_markets"],
        "functional_roles": ["knowledge", "market"],
        "tags": tags,
        "theoretical_depth": ["system"],
        "verification": {
            "status": "partially_verified",
            "reviewed_by": "ai",
            "reviewed_at": today,
            "confidence": "medium",
            "notes": f"Imported from Unitree official news API. News ID: {news_id}.",
        },
        "sources": sources,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Ingest Unitree official news as report entries.")
    parser.add_argument("--dry-run", action="store_true", help="Preview without writing files.")
    args = parser.parse_args()

    print(f"Fetching {LIST_URL} ...")
    items = fetch_list()
    print(f"Total news items: {len(items)}")

    # Keep English-language items only to avoid en/zh duplicates. Chinese-only items are dropped.
    relevant = [it for it in items if is_relevant(it) and it.get("lang") == ["2"]]
    print(f"Relevant English items: {len(relevant)}")

    existing_titles = load_existing_titles()
    existing_ids = entry_builder.load_existing_ids()

    results: list[dict[str, Any]] = []
    added = 0
    skipped = 0
    for item in relevant:
        detail = fetch_detail(item.get("id", ""))
        fm = build_entry(item, detail, existing_titles, existing_ids)
        if fm is None:
            skipped += 1
            continue
        results.append({"item": item, "detail": detail, "entry": fm})
        if args.dry_run:
            print(f"[dry-run] {fm['$id']}: {fm['names']['en'][:80]}")
        else:
            path = entry_builder.write_entry_file(fm, fm["summary"]["en"] or "", "reports", f"{fm['$id']}.md")
            print(f"[wrote] {path.name}")
        added += 1

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(json.dumps({
        "fetched_at": str(date.today()),
        "source": LIST_URL,
        "total": len(items),
        "relevant": len(relevant),
        "items": relevant,
    }, ensure_ascii=False, indent=2), encoding="utf-8")

    print(f"\nTotal: {len(items)} | Relevant: {len(relevant)} | Added: {added} | Skipped: {skipped}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
