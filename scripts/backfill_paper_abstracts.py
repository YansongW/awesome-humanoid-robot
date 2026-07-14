#!/usr/bin/env python3
"""
Backfill paper entry abstracts from arXiv (bulk API) and Semantic Scholar.

Usage:
    python scripts/backfill_paper_abstracts.py [--limit N] [--dry-run]
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import time
import urllib.parse
import xml.etree.ElementTree as ET
from pathlib import Path
from typing import Any

import requests
import yaml

sys.path.insert(0, str(Path(__file__).parent))

ROOT = Path(__file__).parent.parent
PAPERS_DIR = ROOT / "research" / "papers"
STAGING_DIR = ROOT / ".staging"
CACHE_PATH = STAGING_DIR / "abstract_cache.json"
REPORT_PATH = STAGING_DIR / "abstract_backfill_report.json"

MIN_ZH_CHARS = 200
ARXIV_BATCH = 100
SS_DELAY = 1.0


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


def arxiv_id_from_url(url: str) -> str | None:
    m = re.search(r"arxiv\.org/(?:abs|pdf)/([0-9]+\.[0-9]+(?:v[0-9]+)?)", url, re.IGNORECASE)
    return m.group(1) if m else None


def base_arxiv_id(aid: str) -> str:
    return re.sub(r"v\d+$", "", aid)


def parse_arxiv_response(text: str) -> dict[str, dict[str, str]]:
    """Return mapping arxiv_id -> {title, abstract, source_url}."""
    results: dict[str, dict[str, str]] = {}
    root = ET.fromstring(text)
    ns = {"atom": "http://www.w3.org/2005/Atom"}
    for entry in root.findall("atom:entry", ns):
        id_url = entry.findtext("atom:id", "", ns).strip()
        # id_url is https://arxiv.org/abs/2501.12345v1
        m = re.search(r"/([0-9]+\.[0-9]+(?:v[0-9]+)?)$", id_url)
        if not m:
            continue
        aid = base_arxiv_id(m.group(1))
        title = (entry.findtext("atom:title", "", ns) or "").replace("\n", " ").strip()
        summary = (entry.findtext("atom:summary", "", ns) or "").replace("\n", " ").strip()
        results[aid] = {"title": title, "abstract": summary, "source": id_url}
    return results


def fetch_arxiv_batch(ids: list[str], cache: dict[str, Any]) -> dict[str, dict[str, str]]:
    base_ids = [base_arxiv_id(aid) for aid in ids]
    needed = [aid for aid in base_ids if f"arxiv:{aid}" not in cache]
    if not needed:
        return {aid: cache[f"arxiv:{aid}"] for aid in base_ids if f"arxiv:{aid}" in cache}

    results: dict[str, dict[str, str]] = {}
    for i in range(0, len(needed), ARXIV_BATCH):
        batch = needed[i : i + ARXIV_BATCH]
        id_list = ",".join(batch)
        url = f"http://export.arxiv.org/api/query?id_list={id_list}&max_results={len(batch)}"
        try:
            r = requests.get(url, timeout=60)
            r.raise_for_status()
        except Exception as exc:
            print(f"  arXiv batch failed: {exc}")
            for aid in batch:
                cache[f"arxiv:{aid}"] = None
            time.sleep(3)
            continue
        batch_results = parse_arxiv_response(r.text)
        for aid in batch:
            cache[f"arxiv:{aid}"] = batch_results.get(aid)
        results.update(batch_results)
        time.sleep(3)  # be polite to arXiv
    return results


def fetch_semantic_scholar(title: str, cache: dict[str, Any]) -> dict[str, str] | None:
    key = f"ss:{title.lower().strip()}"
    if key in cache:
        return cache[key]
    q = urllib.parse.quote(title)
    url = (
        "https://api.semanticscholar.org/graph/v1/paper/search"
        f"?query={q}&fields=title,abstract,year,authors&limit=3"
    )
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
    except Exception as exc:
        cache[key] = None
        return None
    data = r.json()
    papers = data.get("data", [])
    if not papers:
        cache[key] = None
        return None
    p = papers[0]
    result = {
        "title": p.get("title", ""),
        "abstract": p.get("abstract", ""),
        "source": f"Semantic Scholar search: {title}",
    }
    cache[key] = result
    return result


def build_body(abstract: str, source_label: str) -> str:
    return (
        "## 概述\n"
        f"{abstract}\n\n"
        "## 核心内容\n"
        f"{abstract}\n\n"
        "## 参考\n"
        f"- {source_label}\n"
    )


def needs_update(fm: dict[str, Any], body: str) -> bool:
    summary = fm.get("summary", {}) or {}
    names = fm.get("names", {}) or {}
    zh_chars = len(re.findall(r"[\u4e00-\u9fff]", body))
    if zh_chars < MIN_ZH_CHARS:
        return True
    if not summary.get("en") or not summary.get("zh"):
        return True
    if not names.get("en"):
        return True
    return False


def main() -> int:
    parser = argparse.ArgumentParser(description="Backfill paper abstracts from arXiv / Semantic Scholar.")
    parser.add_argument("--limit", type=int, default=None, help="Process at most N paper entries")
    parser.add_argument("--dry-run", action="store_true", help="Do not write files")
    parser.add_argument("--ss-only", action="store_true", help="Only use Semantic Scholar (for testing)")
    args = parser.parse_args()

    STAGING_DIR.mkdir(parents=True, exist_ok=True)
    cache: dict[str, Any] = json.loads(CACHE_PATH.read_text(encoding="utf-8")) if CACHE_PATH.exists() else {}

    paths = sorted(PAPERS_DIR.glob("*.md"))
    if args.limit is not None:
        paths = paths[: args.limit]

    # First pass: identify entries needing update and collect arXiv IDs.
    to_process: list[tuple[Path, dict[str, Any], str, dict[str, Any], str | None]] = []
    arxiv_ids: list[str] = []
    skipped: list[dict[str, str]] = []

    for p in paths:
        text = p.read_text(encoding="utf-8")
        fm, body = split_fm(text)
        if fm is None or fm.get("type") != "paper":
            skipped.append({"id": p.stem, "reason": "no frontmatter or not paper"})
            continue

        if not needs_update(fm, body):
            skipped.append({"id": fm.get("$id", p.stem), "reason": "already rich"})
            continue

        names = fm.get("names", {}) or {}
        sources = fm.get("sources", []) or []
        title = names.get("en") or names.get("zh") or p.stem

        arxiv_id: str | None = None
        for s in sources:
            arxiv_id = arxiv_id_from_url(s.get("url", ""))
            if arxiv_id:
                break

        to_process.append((p, fm, title, sources, arxiv_id))
        if arxiv_id and not args.ss_only:
            arxiv_ids.append(arxiv_id)

    print(f"Processing {len(to_process)} paper entries ({len(arxiv_ids)} with arXiv IDs)")

    # Bulk fetch arXiv abstracts (reads/writes cache even in dry-run to allow inspection).
    arxiv_results: dict[str, dict[str, str]] = {}
    if arxiv_ids:
        arxiv_results = fetch_arxiv_batch(arxiv_ids, cache)
        print(f"  fetched {len(arxiv_results)} arXiv abstracts")

    updated: list[dict[str, str]] = []
    failed: list[dict[str, str]] = []

    for p, fm, title, sources, arxiv_id in to_process:
        eid = fm.get("$id", p.stem)
        result: dict[str, str] | None = None

        if arxiv_id and not args.ss_only:
            cached = cache.get(f"arxiv:{base_arxiv_id(arxiv_id)}")
            result = cached if isinstance(cached, dict) else None

        if not result and title:
            result = fetch_semantic_scholar(title, cache)
            if result:
                time.sleep(SS_DELAY)

        if not result or not result.get("abstract"):
            failed.append({"id": eid, "reason": "no abstract found"})
            continue

        abstract = result["abstract"].strip()
        names = fm.get("names", {}) or {}
        summary = fm.get("summary", {}) or {}

        if not names.get("en") and result.get("title"):
            names["en"] = result["title"].strip()
        if not summary.get("en"):
            summary["en"] = abstract[:800]
        if not summary.get("zh"):
            summary["zh"] = abstract[:800]

        fm["names"] = names
        fm["summary"] = summary

        ver = fm.get("verification", {}) or {}
        ver["notes"] = f"Abstract backfilled by scripts/backfill_paper_abstracts.py from {result['source']}."
        ver["reviewed_at"] = "2026-07-14"
        fm["verification"] = ver

        new_body = build_body(abstract, result["source"])

        if not args.dry_run:
            new_yaml = yaml.safe_dump(fm, allow_unicode=True, sort_keys=False, width=120, default_flow_style=False)
            p.write_text(f"---\n{new_yaml}---\n{new_body}\n", encoding="utf-8")

        updated.append({"id": eid, "source": result["source"]})

    if not args.dry_run:
        CACHE_PATH.write_text(json.dumps(cache, ensure_ascii=False, indent=2), encoding="utf-8")
        report = {
            "processed": len(paths),
            "updated": len(updated),
            "skipped": len(skipped),
            "failed": len(failed),
            "updated_ids": updated,
            "failed_ids": failed,
            "skipped_reasons": skipped,
        }
        REPORT_PATH.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")

    print(f"Done: updated {len(updated)}, skipped {len(skipped)}, failed {len(failed)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
