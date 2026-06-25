"""PDF acquisition and text extraction."""

from __future__ import annotations

import re
from pathlib import Path
from typing import BinaryIO
from urllib.parse import urlparse

import requests


def _is_arxiv_url(url: str) -> bool:
    return "arxiv.org" in url.lower()


def _extract_arxiv_id(url_or_id: str) -> str | None:
    """Extract arXiv ID from URL or bare ID."""
    text = url_or_id.strip()
    # bare ID like 2604.23001 or arxiv:2604.23001
    m = re.match(r"(?:arxiv:)?(\d{4}\.\d{4,5})(v\d+)?", text, re.IGNORECASE)
    if m:
        return m.group(1)
    # URL like https://arxiv.org/abs/2604.23001
    m = re.search(r"arxiv\.org/(?:abs|pdf)/(\d{4}\.\d{4,5})(?:v\d+)?", text, re.IGNORECASE)
    if m:
        return m.group(1)
    return None


def resolve_arxiv_pdf_url(url_or_id: str) -> str | None:
    """Return the PDF URL for an arXiv ID or URL."""
    arxiv_id = _extract_arxiv_id(url_or_id)
    if not arxiv_id:
        return None
    return f"https://arxiv.org/pdf/{arxiv_id}.pdf"


def resolve_arxiv_abs_url(url_or_id: str) -> str | None:
    """Return the abstract URL for an arXiv ID or URL."""
    arxiv_id = _extract_arxiv_id(url_or_id)
    if not arxiv_id:
        return None
    return f"https://arxiv.org/abs/{arxiv_id}"


def download_pdf(url: str, dest: Path, timeout: int = 60) -> Path:
    """Download a PDF to the given destination."""
    dest.parent.mkdir(parents=True, exist_ok=True)
    response = requests.get(url, timeout=timeout, stream=True)
    response.raise_for_status()
    with open(dest, "wb") as f:
        for chunk in response.iter_content(chunk_size=8192):
            f.write(chunk)
    return dest


def extract_text_from_pdf(pdf_path: Path | BinaryIO) -> str:
    """Extract text from a PDF using PyMuPDF."""
    try:
        import fitz  # pymupdf
    except ImportError as exc:
        raise ImportError(
            "PyMuPDF is required for PDF extraction. Install it with: pip install pymupdf"
        ) from exc

    doc = fitz.open(str(pdf_path)) if isinstance(pdf_path, Path) else fitz.open(stream=pdf_path.read(), filetype="pdf")
    chunks = []
    for page in doc:
        text = page.get_text()
        if text.strip():
            chunks.append(text)
    doc.close()
    return "\n\n".join(chunks)


def get_paper_text(input_url_or_id: str, cache_dir: Path | None = None) -> tuple[str, dict[str, str]]:
    """Resolve, download, and extract text from a paper URL/ID.

    Returns:
        text: full extracted text
        meta: dict with keys 'source_url', 'pdf_url', 'title' (if available)
    """
    from . import config

    cache_dir = cache_dir or (config.STAGING_DIR / "pdfs")
    cache_dir.mkdir(parents=True, exist_ok=True)

    arxiv_id = _extract_arxiv_id(input_url_or_id)
    if arxiv_id:
        pdf_url = resolve_arxiv_pdf_url(input_url_or_id)
        abs_url = resolve_arxiv_abs_url(input_url_or_id)
        pdf_path = cache_dir / f"arxiv_{arxiv_id}.pdf"
        if not pdf_path.exists():
            download_pdf(pdf_url, pdf_path)
        text = extract_text_from_pdf(pdf_path)
        return text, {
            "source_url": abs_url or pdf_url,
            "pdf_url": pdf_url,
            "arxiv_id": arxiv_id,
        }

    # Generic URL path
    parsed = urlparse(input_url_or_id)
    if parsed.scheme in ("http", "https") and input_url_or_id.lower().endswith(".pdf"):
        filename = Path(parsed.path).name or "paper.pdf"
        pdf_path = cache_dir / filename
        if not pdf_path.exists():
            download_pdf(input_url_or_id, pdf_path)
        text = extract_text_from_pdf(pdf_path)
        return text, {"source_url": input_url_or_id, "pdf_url": input_url_or_id}

    raise ValueError(
        f"Unsupported paper input: {input_url_or_id}. "
        "Provide an arXiv ID/URL or a direct PDF URL."
    )
