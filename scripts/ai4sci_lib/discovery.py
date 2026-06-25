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

import re
import xml.etree.ElementTree as ET
from typing import Any
from urllib.parse import quote_plus

import requests

from . import config, entry_builder, pdf, pipeline


def _existing_ids() -> set[str]:
    """Load all existing and staged entity/relationship IDs."""
    return entry_builder.load_existing_ids()


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
    sort_by: str = "relevance",
    sort_order: str = "descending",
) -> list[pipeline.SourceCandidate]:
    """Search arXiv and return SourceCandidate objects.

    Args:
        query: Search query string.
        max_results: Maximum number of results to return.
        sort_by: arXiv sort field (relevance, lastUpdatedDate, submittedDate).
        sort_order: ascending or descending.

    Returns:
        List of SourceCandidate objects that are not already in the project.
    """
    url = (
        "http://export.arxiv.org/api/query?"
        f"search_query={quote_plus(query)}&"
        f"start=0&max_results={max_results}&"
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
            )
        )

    return candidates


def search_semantic_scholar(
    query: str,
    max_results: int = 10,
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
    sources: list[str] | None = None,
) -> list[pipeline.SourceCandidate]:
    """Run discovery across configured sources and return deduplicated candidates.

    Args:
        seed_queries: List of search query strings.
        paper_ids: Optional list of explicit arXiv IDs or URLs to include.
        max_results_per_query: Maximum arXiv results per query.
        sources: List of source names to query (e.g., ["arxiv"]). Defaults to ["arxiv"].

    Returns:
        Deduplicated list of SourceCandidate objects.
    """
    sources = sources or ["arxiv"]
    candidates: list[pipeline.SourceCandidate] = []
    seen_ids: set[str] = set()

    # Explicitly requested papers/URLs first.
    for input_str in paper_ids or []:
        candidate = resolve_candidate(input_str)
        if candidate and candidate.arxiv_id and candidate.arxiv_id not in seen_ids:
            if candidate.arxiv_id not in _existing_ids():
                candidates.append(candidate)
                seen_ids.add(candidate.arxiv_id)

    # Search-based discovery.
    for query in seed_queries:
        for source in sources:
            try:
                if source == "arxiv":
                    found = search_arxiv(query, max_results=max_results_per_query)
                elif source == "semanticscholar":
                    found = search_semantic_scholar(query, max_results=max_results_per_query)
                elif source == "web":
                    found = search_web(query, max_results=max_results_per_query)
                else:
                    found = []
            except Exception:
                found = []

            for candidate in found:
                key = candidate.arxiv_id or candidate.source_url
                if key and key not in seen_ids:
                    candidates.append(candidate)
                    seen_ids.add(key)

    return candidates
