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


# Directory titles used when rendering the wiki tree. The goal is to keep the
# sidebar/index readable: chapters first, then appendices, with appendix-d
# sub-pages nested under appendix-d rather than flattened.
DIR_TITLES: dict[str, str] = {
    "chapters": "正文",
    "appendices": "附录",
    "appendix-d": "附录 D 主要供应商与企业名录",
    "companies": "企业 Wiki",
    "products": "产品 Wiki",
    "technologies": "技术 Wiki",
}


def _sort_key(name: str) -> tuple[int, str]:
    """Order: chapters -> appendices -> everything else, then alphabetically."""
    if name == "chapters":
        return (0, name)
    if name == "appendices":
        return (1, name)
    return (2, name)


def build_wiki_tree(pages: list[dict[str, Any]]) -> dict[str, Any]:
    """Build a nested tree of wiki pages for hierarchical rendering.

    The tree mirrors the ``wiki/docs`` directory structure. Each node is a dict
    with ``title``, ``path``, ``url`` (files only), ``children`` (dirs only) and
    ``is_dir``. KG entity/relationship files are already filtered out by
    ``build_wiki_pages``.
    """
    root: dict[str, Any] = {"title": "Wiki", "is_dir": True, "children": {}, "path": ""}

    # Stub chapters (e.g. "本章正在撰写中") are rendered but hidden from the index.
    pages = [p for p in pages if not p.get("stub")]

    # Process deepest pages first so that directories are created before their
    # matching index file (e.g. appendices/appendix-d/ before appendix-d.md).
    sorted_pages = sorted(pages, key=lambda p: -len(Path(p["path"]).relative_to(WIKI_DIR).parts))

    for page in sorted_pages:
        rel = Path(page["path"]).relative_to(WIKI_DIR)
        current = root
        parts = list(rel.with_suffix("").parts)
        # Build/create intermediate directory nodes
        for i, part in enumerate(parts[:-1]):
            children = current.setdefault("children", {})
            sub_path = "/".join(parts[: i + 1])
            if part not in children:
                children[part] = {
                    "title": DIR_TITLES.get(part, part),
                    "is_dir": True,
                    "children": {},
                    "path": sub_path,
                }
            current = children[part]
        # Add the file node, or merge it with an existing directory index.
        leaf_name = parts[-1]
        children = current.setdefault("children", {})
        if leaf_name in children and children[leaf_name].get("is_dir"):
            # The matching directory already exists (created by deeper pages).
            children[leaf_name].update({
                "title": page["title"],
                "url": page["url"],
            })
        else:
            children[leaf_name] = {
                "title": page["title"],
                "url": page["url"],
                "is_dir": False,
                "path": str(rel.with_suffix("")),
            }

    def finalize(node: dict[str, Any]) -> dict[str, Any]:
        """Recursively convert children maps to sorted lists."""
        children = node.get("children", {})
        if not children:
            return {k: v for k, v in node.items() if k != "children"}
        dirs = []
        files = []
        for key, child in children.items():
            child = finalize(child)
            if child.get("is_dir"):
                dirs.append(child)
            else:
                files.append(child)
        dirs.sort(key=lambda c: _sort_key(c.get("title", "")))
        files.sort(key=lambda c: c.get("path", ""))
        node["children"] = dirs + files
        return node

    return finalize(root)


def rewrite_md_links(text: str) -> str:
    """Rewrite relative .md links (e.g. chapters/chapter-01.md#sec) to /wiki/ URLs."""

    def repl(m: re.Match) -> str:
        label, href = m.group(1), m.group(2)
        if href.startswith(("http://", "https://", "#", "/", "mailto:")):
            return m.group(0)
        mm = re.match(r"^(?:\.\./)*(.+?)\.md(#.*)?$", href)
        if not mm:
            return m.group(0)
        path, anchor = mm.group(1), mm.group(2) or ""
        return f"[{label}](/wiki/{path}/{anchor})"

    return re.sub(r"(?<!!)\[([^\]]*)\]\(([^)\s]+)\)", repl, text)


def is_stub_page(text: str) -> bool:
    """Detect placeholder chapters/appendices with no real content."""
    return len(text.strip()) < 500 or "正在撰写中" in text


def build_wiki_pages() -> list[dict[str, Any]]:
    """Load all wiki Markdown files and convert them to HTML.

    Returns a list of page dicts with title, url, body_html, toc_html, stub flag,
    and metadata.
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
        text = rewrite_md_links(text)
        body_html = md.convert(text)
        toc_html = md.toc if "<li>" in (md.toc or "") else ""
        md.reset()
        pages.append(
            {
                "title": title,
                "url": url,
                "path": str(path),
                "body_html": body_html,
                "toc_html": toc_html,
                "stub": is_stub_page(text),
            }
        )

    # Prev/next navigation across substantive pages in reading order:
    # chapters -> appendices -> everything else.
    def order_key(p: dict[str, Any]) -> tuple[int, str]:
        rel = Path(p["path"]).relative_to(WIKI_DIR).as_posix()
        if rel.startswith("chapters/"):
            return (0, rel)
        if rel.startswith("appendices/"):
            return (1, rel)
        return (2, rel)

    readable = [p for p in pages if not p["stub"]]
    readable.sort(key=order_key)
    for i, page in enumerate(readable):
        page["prev_page"] = readable[i - 1] if i > 0 else None
        page["next_page"] = readable[i + 1] if i < len(readable) - 1 else None
    return pages
