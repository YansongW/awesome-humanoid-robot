#!/usr/bin/env python3
"""Fetch NVIDIA Blog robotics RSS and ingest relevant posts as report entries.

Usage:
    python scripts/ingest_nvidia_blog.py --dry-run
    python scripts/ingest_nvidia_blog.py
"""

from __future__ import annotations

import argparse
import json
import re
from datetime import date
from pathlib import Path
from typing import Any
from xml.etree import ElementTree as ET

import requests
import yaml

from ai4sci_lib import config, entry_builder


ROOT = config.ROOT
RESEARCH_DIR = config.RESEARCH_DIR
RSS_URL = "https://blogs.nvidia.com/blog/category/robotics/feed/"
OUTPUT_PATH = ROOT / "data" / "curated" / "nvidia_robotics_blog_latest.json"

KEYWORDS = [
    "humanoid", "robot", "robotics", "GR00T", "Isaac", "Unitree", "Figure",
    "Tesla", "locomotion", "manipulation", "dexterous", "VLA", "vision-language-action",
    "sim-to-real", "sim2real", "embodied", "physical ai",
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


def fetch_rss() -> list[dict[str, Any]]:
    resp = requests.get(RSS_URL, timeout=60, headers={"User-Agent": "Mozilla/5.0"})
    resp.raise_for_status()
    resp.encoding = resp.apparent_encoding or "utf-8"
    root = ET.fromstring(resp.text.encode("utf-8"))
    channel = root.find("channel")
    if channel is None:
        return []
    items: list[dict[str, Any]] = []
    for item in channel.findall("item"):
        title_elem = item.find("title")
        link_elem = item.find("link")
        desc_elem = item.find("description")
        date_elem = item.find("pubDate")
        title = (title_elem.text or "").strip() if title_elem is not None else ""
        link = (link_elem.text or "").strip() if link_elem is not None else ""
        desc = (desc_elem.text or "").strip() if desc_elem is not None else ""
        pub_date = (date_elem.text or "").strip() if date_elem is not None else ""
        if not title or not link:
            continue
        items.append({
            "title": title,
            "link": link,
            "description": desc,
            "pub_date": pub_date,
        })
    return items


def is_relevant(item: dict[str, Any]) -> bool:
    text = f"{item['title']} {item['description']}".lower()
    return any(kw.lower() in text for kw in KEYWORDS)


def _extract_year(text: str) -> str:
    m = re.search(r"20\d{2}", text)
    return m.group(0) if m else str(date.today().year)


def clean_html(raw: str) -> str:
    text = re.sub(r"<[^>]+>", " ", raw)
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def build_entry(
    item: dict[str, Any],
    existing_titles: set[str],
    existing_ids: set[str],
) -> dict[str, Any] | None:
    title = item["title"].strip()
    title_key = title.lower()
    if title_key in existing_titles:
        print(f"[skip duplicate title] {title}")
        return None

    year = _extract_year(item.get("pub_date", ""))
    title_slug = entry_builder._slugify(title, max_len=30)
    ent_id = f"ent_report_nvidia_{title_slug}_{year}"
    candidate_id = ent_id
    counter = 1
    while candidate_id in existing_ids:
        candidate_id = f"{ent_id}_{counter}"
        counter += 1
    ent_id = candidate_id
    existing_ids.add(ent_id)
    existing_titles.add(title_key)

    names = {"en": title, "zh": title, "ko": ""}
    summary_text = clean_html(item.get("description", "")) or title
    summary = {"en": summary_text, "zh": summary_text, "ko": ""}

    tags = set(["nvidia", "robotics", "blog"])
    for kw in ["humanoid", "GR00T", "Isaac", "Unitree", "Figure", "Tesla", "VLA", "locomotion", "manipulation"]:
        if kw.lower() in title.lower():
            tags.add(entry_builder._slugify(kw, max_len=20))
    tags = sorted(t for t in tags if t)

    today = str(date.today())
    sources = [
        {
            "id": "src_001",
            "type": "website",
            "title": title,
            "url": item["link"],
            "date": year,
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
        "domains": ["11_applications_markets", "07_ai_models_algorithms"],
        "layers": ["midstream", "validation_markets"],
        "functional_roles": ["knowledge", "market"],
        "tags": tags,
        "theoretical_depth": ["system"],
        "verification": {
            "status": "partially_verified",
            "reviewed_by": "ai",
            "reviewed_at": today,
            "confidence": "medium",
            "notes": "Imported from NVIDIA Blog robotics RSS feed.",
        },
        "sources": sources,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Ingest NVIDIA robotics blog posts as report entries.")
    parser.add_argument("--dry-run", action="store_true", help="Preview without writing files.")
    args = parser.parse_args()

    print(f"Fetching {RSS_URL} ...")
    items = fetch_rss()
    print(f"Total RSS items: {len(items)}")

    relevant = [it for it in items if is_relevant(it)]
    print(f"Relevant items: {len(relevant)}")

    existing_titles = load_existing_titles()
    existing_ids = entry_builder.load_existing_ids()

    added = 0
    skipped = 0
    for item in relevant:
        fm = build_entry(item, existing_titles, existing_ids)
        if fm is None:
            skipped += 1
            continue
        if args.dry_run:
            print(f"[dry-run] {fm['$id']}: {fm['names']['en'][:80]}")
        else:
            path = entry_builder.write_entry_file(fm, fm["summary"]["en"] or "", "reports", f"{fm['$id']}.md")
            print(f"[wrote] {path.name}")
        added += 1

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(json.dumps({
        "fetched_at": str(date.today()),
        "source": RSS_URL,
        "total": len(items),
        "relevant": len(relevant),
        "items": relevant,
    }, ensure_ascii=False, indent=2), encoding="utf-8")

    print(f"\nTotal: {len(items)} | Relevant: {len(relevant)} | Added: {added} | Skipped: {skipped}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
