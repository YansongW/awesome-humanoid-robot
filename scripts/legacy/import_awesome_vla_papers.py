#!/usr/bin/env python3
"""Import the Awesome-VLA curated list into the knowledge graph.

This script imports every paper from data/curated/awesome_vla_papers.json,
skipping entries whose English title already exists in the graph.

Usage:
    python scripts/import_awesome_vla_papers.py --dry-run
    python scripts/import_awesome_vla_papers.py
"""

from __future__ import annotations

import argparse
import json
import re
from datetime import date
from pathlib import Path
from typing import Any

import yaml

from ai4sci_lib import config, entry_builder


ROOT = config.ROOT
RESEARCH_DIR = config.RESEARCH_DIR
CURATED_PATH = ROOT / "data" / "curated" / "awesome_vla_papers.json"


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


def _first_author_last(authors: list[Any]) -> str:
    if not authors:
        return "unknown"
    first = authors[0]
    if isinstance(first, dict):
        first = first.get("text", "")
    first = str(first).strip()
    # Extract last alphabetic token (e.g. "Li Chen 0008" -> "Chen").
    for token in reversed(first.split()):
        token = re.sub(r"[^A-Za-z]", "", token)
        if token:
            return token.lower()
    return "unknown"


def _make_summary(paper: dict[str, Any]) -> str:
    title = paper.get("title", "").strip()
    year = paper.get("year", "")
    ptype = paper.get("type", "VLA").lower()
    institution = paper.get("institution", "").strip()
    venue = paper.get("venue", "").strip()
    model = paper.get("model", "").strip()
    parts = [f"{title} ({model})" if model else title]
    parts.append(f"is a {year} {ptype} vision-language-action model for robotic manipulation")
    if institution:
        parts.append(f"introduced by {institution}")
    if venue:
        parts.append(f"and published at {venue}")
    return ", ".join(parts) + "."


def build_entry(
    paper: dict[str, Any],
    existing_titles: set[str],
    existing_ids: set[str],
) -> dict[str, Any] | None:
    title = paper.get("title", "").strip()
    if not title:
        return None
    if title.lower() in existing_titles:
        print(f"[skip duplicate] {title}")
        return None

    year = str(paper.get("year", date.today().year))
    first_author = _first_author_last(paper.get("authors", []))
    ent_id = entry_builder.make_entry_id("paper", first_author, title, year)

    candidate_id = ent_id
    counter = 1
    while candidate_id in existing_ids:
        candidate_id = f"{ent_id}_{counter}"
        counter += 1
    ent_id = candidate_id
    existing_ids.add(ent_id)

    model = paper.get("model", "").strip()
    names = {
        "en": title,
        "zh": model or title,
        "ko": "",
    }

    summary_text = _make_summary(paper)
    summary = {"en": summary_text, "zh": summary_text, "ko": ""}

    ptype = paper.get("type", "Large")
    base_tags: set[str] = {
        "vla",
        "vision_language_action",
        "robotic_manipulation",
        "generalist_policy" if ptype == "Generalized" else "large_vla_model",
        entry_builder._slugify(model, max_len=30) if model else "",
    }
    tags = sorted(t for t in base_tags if t)

    arxiv_id = (paper.get("arxiv_id") or "").strip()
    source_url = (paper.get("source_url") or "").strip()
    today = str(date.today())
    sources: list[dict[str, Any]] = []

    if arxiv_id:
        sources.append({
            "id": "src_001",
            "type": "paper",
            "title": f"{title} (arXiv)",
            "url": f"https://arxiv.org/abs/{arxiv_id}",
            "date": year,
            "accessed_at": today,
        })

    if source_url and (not arxiv_id or not source_url.startswith(f"https://arxiv.org/abs/{arxiv_id}")):
        src_id = "src_002" if arxiv_id else "src_001"
        src_type = "paper" if "proceedings.mlr.press" in source_url or "openreview.net" in source_url else "website"
        sources.append({
            "id": src_id,
            "type": src_type,
            "title": f"{model or title} source" if model else title,
            "url": source_url,
            "date": year,
            "accessed_at": today,
        })

    if not sources:
        sources.append({
            "id": "src_001",
            "type": "website",
            "title": title,
            "url": "",
            "date": year,
            "accessed_at": today,
        })

    institution = paper.get("institution", "").strip()
    venue = paper.get("venue", "").strip()
    notes_parts = [
        "Imported from Awesome-VLA curated list.",
    ]
    if model:
        notes_parts.append(f"Model: {model}.")
    if institution:
        notes_parts.append(f"Institution: {institution}.")
    if venue:
        notes_parts.append(f"Venue: {venue}.")
    if arxiv_id:
        notes_parts.append(f"arXiv: {arxiv_id}.")
    notes = " ".join(notes_parts)

    if arxiv_id or (source_url and source_url.startswith(("http://", "https://"))):
        status = "partially_verified"
        confidence = "medium"
    else:
        status = "unverified"
        confidence = "low"

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
            "status": status,
            "reviewed_by": "ai",
            "reviewed_at": today,
            "confidence": confidence,
            "notes": notes,
        },
        "sources": sources,
    }


def write_entry(frontmatter: dict[str, Any]) -> Path:
    subdir = "papers"
    filename = f"{frontmatter['$id']}.md"
    body = frontmatter["summary"]["en"] or ""
    return entry_builder.write_entry_file(frontmatter, body, subdir, filename)


def main() -> int:
    parser = argparse.ArgumentParser(description="Import Awesome-VLA papers into the graph.")
    parser.add_argument("--dry-run", action="store_true", help="Count and preview without writing files.")
    args = parser.parse_args()

    if not CURATED_PATH.exists():
        print(f"Curated data not found: {CURATED_PATH}")
        return 1

    data = json.loads(CURATED_PATH.read_text(encoding="utf-8"))
    papers = data.get("papers", [])
    existing_titles = load_existing_titles()
    existing_ids = entry_builder.load_existing_ids()
    print(f"Loaded {len(papers)} papers from Awesome-VLA list.")
    print(f"Existing titles in graph: {len(existing_titles)}")
    print(f"Existing IDs in graph: {len(existing_ids)}")

    added = 0
    skipped = 0
    for paper in papers:
        fm = build_entry(paper, existing_titles, existing_ids)
        if fm is None:
            skipped += 1
            continue
        if args.dry_run:
            print(f"[dry-run] {fm['$id']}: {fm['names']['en'][:80]}")
        else:
            path = write_entry(fm)
            print(f"[wrote] {path.name}")
        added += 1

    print(f"\nTotal: {len(papers)} | Added: {added} | Skipped duplicates: {skipped}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
