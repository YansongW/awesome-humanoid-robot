"""Load and render wiki pages from the wiki/ directory."""

from __future__ import annotations

import re
from pathlib import Path
from typing import Any

import markdown

ROOT = Path(__file__).resolve().parent.parent.parent
WIKI_DIR = ROOT / "wiki" / "docs"


def slugify_path(path: Path) -> str:
    """Convert a wiki file path to a URL path."""
    rel = path.relative_to(WIKI_DIR)
    parts = list(rel.with_suffix("").parts)
    return "wiki/" + "/".join(parts)


def strip_frontmatter(text: str) -> str:
    """Remove YAML frontmatter delimited by '---' at the start of the file."""
    return re.sub(r"^---\s*\n[\s\S]*?\n---\s*\n", "", text, count=1)


def extract_title(text: str) -> str:
    """Extract the first H1 from markdown text."""
    m = re.search(r"^#\s+(.+)$", text, re.MULTILINE)
    title = m.group(1).strip() if m else "Untitled"
    # Capitalize single-letter appendix identifiers (e.g. "附录 a" -> "附录 A").
    title = re.sub(r"(附录\s+)([a-z])", lambda m: m.group(1) + m.group(2).upper(), title)
    title = re.sub(r"(Appendix\s+)([a-z])", lambda m: m.group(1) + m.group(2).upper(), title, flags=re.IGNORECASE)
    return title


def build_wiki_pages() -> list[dict[str, Any]]:
    """Load all wiki Markdown files and convert them to HTML.

    Returns a list of page dicts with title, url, body_html, and metadata.
    """
    if not WIKI_DIR.exists():
        return []

    md = markdown.Markdown(
        extensions=[
            "extra",
            "toc",
            "tables",
            "admonition",
            "pymdownx.details",
            "pymdownx.superfences",
            "pymdownx.arithmatex",
            "pymdownx.mark",
            "pymdownx.tilde",
        ],
        extension_configs={
            "pymdownx.arithmatex": {"generic": True},
            "pymdownx.superfences": {},
        },
    )

    pages = []
    for path in sorted(WIKI_DIR.rglob("*.md")):
        # KG entity/relationship files are YAML metadata, not human-readable wiki pages.
        if "kg/relationships" in path.as_posix() or "kg/entities" in path.as_posix():
            continue
        text = path.read_text(encoding="utf-8")
        text = strip_frontmatter(text)
        # Skip files that only contain frontmatter (e.g. stub KG entities) so they
        # do not appear as empty "Untitled" pages in the wiki index.
        if not text.strip():
            continue
        title = extract_title(text)
        # TODO: when per-language wiki directories are introduced, filter here.
        # For now all languages share the same wiki source.
        url = slugify_path(path)
        body_html = md.convert(text)
        md.reset()
        pages.append(
            {
                "title": title,
                "url": url,
                "path": str(path),
                "body_html": body_html,
            }
        )
    return pages
