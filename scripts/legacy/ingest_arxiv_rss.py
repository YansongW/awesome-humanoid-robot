#!/usr/bin/env python3
"""Fetch arXiv cs.RO RSS and import humanoid-relevant papers into the graph.

Usage:
    python scripts/ingest_arxiv_rss.py --dry-run
    python scripts/ingest_arxiv_rss.py
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
RSS_URL = "http://export.arxiv.org/rss/cs.RO"
OUTPUT_PATH = ROOT / "data" / "curated" / "arxiv_ro_rss_latest.json"

KEYWORDS = [
    "humanoid",
    "locomotion",
    "loco-manipulation",
    "manipulation",
    "teleoperation",
    "whole-body",
    "whole body",
    "vision-language-action",
    "vla",
    "sim-to-real",
    "sim2real",
    "bipedal",
    "legged",
    "robot learning",
    "human motion",
    "character control",
    "motion tracking",
    "human-to-humanoid",
    "humanoid robot",
    "humanoid control",
    "humanoid locomotion",
    "humanoid manipulation",
]


def load_existing_titles_and_arxiv() -> tuple[set[str], set[str]]:
    titles: set[str] = set()
    arxiv_ids: set[str] = set()
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
            for src in data.get("sources", []):
                url = src.get("url", "")
                m = re.search(r"arxiv\.org/abs/(\d+\.\d+)", str(url))
                if m:
                    arxiv_ids.add(m.group(1))
        except Exception:
            continue
    return titles, arxiv_ids


def fetch_rss() -> list[dict[str, Any]]:
    resp = requests.get(RSS_URL, timeout=60)
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


def _extract_arxiv_id(url: str) -> str:
    m = re.search(r"arxiv\.org/abs/(\d+\.\d+)", url)
    return m.group(1) if m else ""


def _extract_year(title: str) -> str:
    m = re.search(r"20\d{2}", title)
    return m.group(0) if m else str(date.today().year)


def build_entry(
    item: dict[str, Any],
    existing_titles: set[str],
    existing_arxiv: set[str],
    existing_ids: set[str],
) -> dict[str, Any] | None:
    title = item["title"].strip()
    title_key = title.lower()
    arxiv_id = _extract_arxiv_id(item["link"])

    if title_key in existing_titles:
        print(f"[skip duplicate title] {title}")
        return None
    if arxiv_id and arxiv_id in existing_arxiv:
        print(f"[skip duplicate arxiv] {arxiv_id} - {title}")
        return None

    year = _extract_year(title)
    title_slug = entry_builder._slugify(title, max_len=30)
    ent_id = f"ent_paper_{title_slug}_{year}"
    candidate_id = ent_id
    counter = 1
    while candidate_id in existing_ids:
        candidate_id = f"{ent_id}_{counter}"
        counter += 1
    ent_id = candidate_id
    existing_ids.add(ent_id)
    existing_titles.add(title_key)
    if arxiv_id:
        existing_arxiv.add(arxiv_id)

    names = {"en": title, "zh": title, "ko": ""}
    summary_text = item.get("description", "") or f"{title} is a recent arXiv paper in robotics."
    summary = {"en": summary_text, "zh": summary_text, "ko": ""}

    tags = set(["humanoid", "robotics", entry_builder._slugify(title.split(":")[0], max_len=30)])
    tags = sorted(t for t in tags if t)

    today = str(date.today())
    sources = [
        {
            "id": "src_001",
            "type": "paper",
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
        "type": "paper",
        "names": names,
        "summary": summary,
        "domains": ["07_ai_models_algorithms", "08_software_middleware"],
        "layers": ["intelligence"],
        "functional_roles": ["knowledge", "intelligence"],
        "tags": tags,
        "theoretical_depth": ["system"],
        "verification": {
            "status": "partially_verified",
            "reviewed_by": "ai",
            "reviewed_at": today,
            "confidence": "medium",
            "notes": "Imported from arXiv cs.RO RSS feed.",
        },
        "sources": sources,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Ingest humanoid-relevant papers from arXiv cs.RO RSS.")
    parser.add_argument("--dry-run", action="store_true", help="Preview without writing files.")
    args = parser.parse_args()

    print(f"Fetching {RSS_URL} ...")
    items = fetch_rss()
    print(f"Total RSS items: {len(items)}")

    relevant = [it for it in items if is_relevant(it)]
    print(f"Humanoid-relevant items: {len(relevant)}")

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(json.dumps({
        "fetched_at": str(date.today()),
        "source": RSS_URL,
        "total": len(items),
        "relevant": len(relevant),
        "items": relevant,
    }, ensure_ascii=False, indent=2), encoding="utf-8")

    existing_titles, existing_arxiv = load_existing_titles_and_arxiv()
    existing_ids = entry_builder.load_existing_ids()

    added = 0
    skipped = 0
    for item in relevant:
        fm = build_entry(item, existing_titles, existing_arxiv, existing_ids)
        if fm is None:
            skipped += 1
            continue
        if args.dry_run:
            print(f"[dry-run] {fm['$id']}: {fm['names']['en'][:80]}")
        else:
            path = entry_builder.write_entry_file(fm, fm["summary"]["en"] or "", "papers", f"{fm['$id']}.md")
            print(f"[wrote] {path.name}")
        added += 1

    print(f"\nRelevant: {len(relevant)} | Added: {added} | Skipped duplicates: {skipped}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
