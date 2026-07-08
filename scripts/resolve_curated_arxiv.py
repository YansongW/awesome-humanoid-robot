#!/usr/bin/env python3
"""Resolve curated paper titles to arXiv IDs with caching and polite rate limiting.

Usage:
    source .venv/bin/activate
    python scripts/resolve_curated_arxiv.py \
        --papers data/curated/wechat_161_humanoid_papers.json \
        --output data/curated/wechat_161_arxiv_resolution.json \
        --delay 3

The script reuses existing entries in the output file as a cache, so it can be
resumed safely if interrupted.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import time
import xml.etree.ElementTree as ET
from pathlib import Path
from typing import Any
from urllib.parse import quote_plus

import requests

from ai4sci_lib import config


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Resolve curated paper titles to arXiv IDs."
    )
    parser.add_argument(
        "--papers",
        type=Path,
        default=config.ROOT / "data" / "curated" / "wechat_161_humanoid_papers.json",
        help="Path to curated papers JSON.",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=config.ROOT / "data" / "curated" / "wechat_161_arxiv_resolution.json",
        help="Path to write/read resolution JSON (used as cache).",
    )
    parser.add_argument(
        "--delay",
        type=float,
        default=3.0,
        help="Seconds to sleep between arXiv API calls (default: 3).",
    )
    parser.add_argument(
        "--ss-delay",
        type=float,
        default=1.0,
        help="Seconds to sleep between Semantic Scholar calls (default: 1).",
    )
    parser.add_argument(
        "--max-results",
        type=int,
        default=5,
        help="Max search results per query.",
    )
    return parser.parse_args()


def load_json(path: Path) -> Any:
    if not path.exists():
        return []
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def save_json(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


def normalize_title(title: str) -> str:
    return re.sub(r"\s+", " ", title.strip().lower())


def clean_arxiv_id(arxiv_id: str) -> str | None:
    m = re.match(r"(\d+\.\d+)(v\d+)?", arxiv_id.strip())
    if m:
        return m.group(1)
    return arxiv_id.strip()


def search_arxiv_title(title: str, max_results: int = 5) -> str | None:
    """Search arXiv by exact title; return arXiv ID if a strong match is found."""
    q = quote_plus(f'ti:"{title}"')
    url = (
        "http://export.arxiv.org/api/query?"
        f"search_query={q}&start=0&max_results={max_results}&"
        "sortBy=relevance&sortOrder=descending"
    )
    try:
        response = requests.get(url, timeout=60)
        response.raise_for_status()
    except requests.RequestException as exc:
        raise RuntimeError(f"arXiv request failed: {exc}") from exc

    root = ET.fromstring(response.text)
    ns = {"atom": "http://www.w3.org/2005/Atom"}
    target = normalize_title(title)

    for entry in root.findall("atom:entry", ns):
        id_elem = entry.find("atom:id", ns)
        title_elem = entry.find("atom:title", ns)
        if id_elem is None or not id_elem.text:
            continue
        entry_title = normalize_title(title_elem.text or "")
        # Accept exact or near-exact match.
        if entry_title == target or target in entry_title or entry_title in target:
            arxiv_id = re.search(r"(\d+\.\d+)(v\d+)?", id_elem.text)
            if arxiv_id:
                return clean_arxiv_id(arxiv_id.group(0))
    return None


def search_semantic_scholar_title(title: str, max_results: int = 5) -> str | None:
    """Fallback: search Semantic Scholar for an arXiv-backed match."""
    url = "https://api.semanticscholar.org/graph/v1/paper/search"
    params = {
        "query": title,
        "fields": "title,externalIds",
        "limit": max_results,
    }
    try:
        response = requests.get(url, params=params, timeout=60)
        response.raise_for_status()
    except requests.RequestException as exc:
        raise RuntimeError(f"Semantic Scholar request failed: {exc}") from exc

    data = response.json()
    target = normalize_title(title)
    for paper in data.get("data", []):
        paper_title = normalize_title(paper.get("title", ""))
        if paper_title == target or target in paper_title or paper_title in target:
            external_ids = paper.get("externalIds") or {}
            arxiv_id = external_ids.get("ArXiv")
            if arxiv_id:
                return clean_arxiv_id(arxiv_id)
    return None


def resolve_one(paper: dict[str, Any], args: argparse.Namespace) -> dict[str, Any]:
    num = str(paper.get("num", "")).strip()
    title = paper.get("title", "").strip()
    result: dict[str, Any] = {
        "num": num,
        "title": title,
        "arxiv_id": None,
        "source": None,
        "error": None,
    }
    if not title:
        result["error"] = "Missing title"
        return result

    try:
        arxiv_id = search_arxiv_title(title, max_results=args.max_results)
        if arxiv_id:
            result["arxiv_id"] = arxiv_id
            result["source"] = "arxiv"
            return result
    except Exception as exc:
        result["error"] = f"arXiv: {exc}"
        return result
    finally:
        time.sleep(args.delay)

    try:
        arxiv_id = search_semantic_scholar_title(title, max_results=args.max_results)
        if arxiv_id:
            result["arxiv_id"] = arxiv_id
            result["source"] = "semanticscholar"
            return result
    except Exception as exc:
        result["error"] = f"Semantic Scholar: {exc}"
        return result
    finally:
        time.sleep(args.ss_delay)

    result["error"] = "No arXiv match found"
    return result


def main() -> int:
    args = parse_args()
    papers_data = load_json(args.papers)
    papers = papers_data.get("papers", [])

    # Load cache.
    cache = load_json(args.output)
    cache_by_num: dict[str, dict[str, Any]] = {}
    for item in cache:
        num = str(item.get("num", "")).strip()
        if num:
            cache_by_num[num] = item

    results: list[dict[str, Any]] = []
    resolved_count = 0
    for idx, paper in enumerate(papers, start=1):
        num = str(paper.get("num", "")).strip()
        cached = cache_by_num.get(num)
        if cached and cached.get("arxiv_id"):
            results.append(cached)
            resolved_count += 1
            print(f"[{idx}/{len(papers)}] {num} (cached) -> {cached['arxiv_id']}")
            continue

        print(f"[{idx}/{len(papers)}] {num} resolving: {paper.get('title', '')[:80]}...")
        result = resolve_one(paper, args)
        results.append(result)
        if result.get("arxiv_id"):
            resolved_count += 1
            print(f"  -> {result['arxiv_id']} ({result['source']})")
        else:
            print(f"  -> unresolved ({result.get('error')})")

        # Save incremental cache every 10 items.
        if idx % 10 == 0:
            save_json(args.output, results + [r for r in cache if str(r.get("num", "")).strip() not in cache_by_num])

    save_json(args.output, results)
    print(f"\n[resolve] Resolved {resolved_count}/{len(papers)} papers -> {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
