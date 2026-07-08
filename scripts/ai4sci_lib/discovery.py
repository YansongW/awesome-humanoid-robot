"""Discovery sources for the AI4Sci pipeline.

Supports:
- arXiv API search
- Semantic Scholar search (optional, requires no API key for light usage)
- Manual URL/arXiv ID resolution
- Web search placeholder for future provider integration

All discovery functions return SourceCandidate objects and deduplicate against
existing project entries and already-staged drafts.
"""

from __future__ import annotations

import json
import re
import time
import xml.etree.ElementTree as ET
from pathlib import Path
from typing import Any
from urllib.parse import quote_plus

import requests

from . import config, entry_builder, pdf, pipeline


def _existing_ids() -> set[str]:
    """Load all existing and staged entity/relationship IDs."""
    return entry_builder.load_existing_ids()


def _tried_candidates_path() -> Path:
    """Path to the project-wide tried-candidates log."""
    return config.STAGING_DIR / "tried_candidates.jsonl"


def load_tried_candidates() -> set[str]:
    """Load the set of candidate keys already processed by any workstream."""
    path = _tried_candidates_path()
    tried: set[str] = set()
    if not path.exists():
        return tried
    try:
        with open(path, encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                try:
                    record = json.loads(line)
                except json.JSONDecodeError:
                    continue
                key = record.get("arxiv_id") or record.get("source_url")
                if key:
                    tried.add(key)
    except Exception:
        return tried
    return tried


def record_tried_candidate(candidate: pipeline.SourceCandidate) -> None:
    """Append a candidate to the project-wide tried log."""
    path = _tried_candidates_path()
    path.parent.mkdir(parents=True, exist_ok=True)
    record = {
        "arxiv_id": candidate.arxiv_id,
        "source_url": candidate.source_url,
        "discovered_by": candidate.discovered_by,
        "input": candidate.input,
    }
    with open(path, "a", encoding="utf-8") as f:
        f.write(json.dumps(record, ensure_ascii=False) + "\n")


def _arxiv_id_from_url_or_id(url_or_id: str) -> str | None:
    """Extract a clean arXiv ID if possible."""
    return pdf._extract_arxiv_id(url_or_id)


def resolve_candidate(input_str: str) -> pipeline.SourceCandidate | None:
    """Resolve a manual URL or arXiv ID into a SourceCandidate."""
    arxiv_id = _arxiv_id_from_url_or_id(input_str)
    if arxiv_id:
        return pipeline.SourceCandidate(
            input=input_str,
            source_url=pdf.resolve_arxiv_abs_url(input_str) or f"https://arxiv.org/abs/{arxiv_id}",
            pdf_url=pdf.resolve_arxiv_pdf_url(input_str),
            arxiv_id=arxiv_id,
            discovered_by="manual",
        )

    if input_str.lower().startswith(("http://", "https://")) and input_str.lower().endswith(".pdf"):
        return pipeline.SourceCandidate(
            input=input_str,
            source_url=input_str,
            pdf_url=input_str,
            arxiv_id=None,
            discovered_by="manual",
        )

    return None


def search_arxiv(
    query: str,
    max_results: int = 10,
    start: int = 0,
    sort_by: str = "relevance",
    sort_order: str = "descending",
) -> list[pipeline.SourceCandidate]:
    """Search arXiv and return SourceCandidate objects.

    Args:
        query: Search query string.
        max_results: Maximum number of results to return per page.
        start: Result offset for pagination.
        sort_by: arXiv sort field (relevance, lastUpdatedDate, submittedDate).
        sort_order: ascending or descending.

    Returns:
        List of SourceCandidate objects that are not already in the project.
    """
    url = (
        "http://export.arxiv.org/api/query?"
        f"search_query={quote_plus(query)}&"
        f"start={start}&max_results={max_results}&"
        f"sortBy={sort_by}&sortOrder={sort_order}"
    )
    response = requests.get(url, timeout=60)
    response.raise_for_status()

    root = ET.fromstring(response.text)
    ns = {"atom": "http://www.w3.org/2005/Atom"}

    existing = _existing_ids()
    candidates: list[pipeline.SourceCandidate] = []

    for entry in root.findall("atom:entry", ns):
        id_elem = entry.find("atom:id", ns)
        if id_elem is None or not id_elem.text:
            continue
        # arXiv ID URL looks like http://arxiv.org/abs/2604.12345
        arxiv_id = _arxiv_id_from_url_or_id(id_elem.text)
        if not arxiv_id:
            continue

        # Skip entries that are just search result metadata, not real papers.
        if arxiv_id in existing:
            continue

        title_elem = entry.find("atom:title", ns)
        title = title_elem.text.strip() if title_elem is not None and title_elem.text else ""

        summary_elem = entry.find("atom:summary", ns)
        summary = summary_elem.text.strip() if summary_elem is not None and summary_elem.text else ""

        # Skip arXiv category announcement pages.
        if not title:
            continue

        candidates.append(
            pipeline.SourceCandidate(
                input=arxiv_id,
                source_url=f"https://arxiv.org/abs/{arxiv_id}",
                pdf_url=f"https://arxiv.org/pdf/{arxiv_id}.pdf",
                arxiv_id=arxiv_id,
                discovered_by=f"arxiv:{query}",
                query=query,
                title=title,
                summary=summary,
            )
        )

    return candidates


def search_semantic_scholar(
    query: str,
    max_results: int = 10,
    start: int = 0,
    api_key: str | None = None,
) -> list[pipeline.SourceCandidate]:
    """Search Semantic Scholar and return arXiv-backed SourceCandidate objects.

    Only returns results that have an arXiv ID, because the rest of the pipeline
    is currently optimized for arXiv PDFs.
    """
    url = "https://api.semanticscholar.org/graph/v1/paper/search"
    headers: dict[str, str] = {}
    if api_key:
        headers["x-api-key"] = api_key
    params = {
        "query": query,
        "fields": "title,authors,year,externalIds,url",
        "limit": max_results,
        "offset": start,
    }
    response = requests.get(url, params=params, headers=headers, timeout=60)
    response.raise_for_status()
    data = response.json()

    existing = _existing_ids()
    candidates: list[pipeline.SourceCandidate] = []

    for paper in data.get("data", []):
        external_ids = paper.get("externalIds") or {}
        arxiv_id = external_ids.get("ArXiv")
        if not arxiv_id:
            continue
        if arxiv_id in existing:
            continue
        candidates.append(
            pipeline.SourceCandidate(
                input=arxiv_id,
                source_url=f"https://arxiv.org/abs/{arxiv_id}",
                pdf_url=f"https://arxiv.org/pdf/{arxiv_id}.pdf",
                arxiv_id=arxiv_id,
                discovered_by=f"semanticscholar:{query}",
                query=query,
            )
        )

    return candidates


def search_web(query: str, max_results: int = 5) -> list[pipeline.SourceCandidate]:
    """Placeholder for web search discovery.

    In the future this can call a configured search provider (e.g., SerpAPI,
    Bing API, or a local search tool). For now it returns an empty list and
    logs a note.
    """
    # TODO: integrate with a web search provider or Kimi Code CLI web search.
    return []


def discover_candidates(
    seed_queries: list[str],
    paper_ids: list[str] | None = None,
    max_results_per_query: int = 10,
    max_total: int | None = None,
    sources: list[str] | None = None,
    polite_delay: float = 0.5,
) -> list[pipeline.SourceCandidate]:
    """Run discovery across configured sources and return deduplicated candidates.

    Args:
        seed_queries: List of search query strings.
        paper_ids: Optional list of explicit arXiv IDs or URLs to include.
        max_results_per_query: Maximum results per query per page.
        max_total: Maximum total candidates to return across all queries.
            If None, defaults to max_results_per_query (backwards compatible).
        sources: List of source names to query (e.g., ["arxiv"]). Defaults to ["arxiv"].
        polite_delay: Seconds to sleep between paginated API calls.

    Returns:
        Deduplicated list of SourceCandidate objects, excluding project-wide
        tried candidates and existing entries.
    """
    sources = sources or ["arxiv"]
    if max_total is None:
        max_total = max_results_per_query

    tried = load_tried_candidates()
    existing = _existing_ids()
    candidates: list[pipeline.SourceCandidate] = []
    seen_ids: set[str] = set()

    def _add(candidate: pipeline.SourceCandidate | None) -> bool:
        if candidate is None:
            return False
        key = candidate.arxiv_id or candidate.source_url
        if not key:
            return False
        if key in existing or key in tried or key in seen_ids:
            return False
        candidates.append(candidate)
        seen_ids.add(key)
        return True

    # Explicitly requested papers/URLs first.
    for input_str in paper_ids or []:
        _add(resolve_candidate(input_str))
        if max_total and len(candidates) >= max_total:
            return candidates[:max_total]

    # Search-based discovery with pagination.
    for query in seed_queries:
        for source in sources:
            start = 0
            while True:
                if max_total and len(candidates) >= max_total:
                    return candidates[:max_total]

                remaining = max_total - len(candidates) if max_total else max_results_per_query
                page_size = min(max_results_per_query, remaining) if max_total else max_results_per_query

                try:
                    if source == "arxiv":
                        found = search_arxiv(query, max_results=page_size, start=start)
                    elif source == "semanticscholar":
                        found = search_semantic_scholar(query, max_results=page_size, start=start)
                    elif source == "web":
                        found = search_web(query, max_results=page_size)
                    else:
                        found = []
                except Exception:
                    found = []

                if not found:
                    break

                for candidate in found:
                    _add(candidate)

                start += len(found)

                # Stop paginating if the page was not full or we have enough.
                if len(found) < page_size:
                    break
                if max_total and len(candidates) >= max_total:
                    return candidates[:max_total]

                time.sleep(min(polite_delay, 0.1))

    return candidates
