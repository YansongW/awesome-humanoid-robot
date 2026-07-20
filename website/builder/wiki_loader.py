"""Load and render wiki (wiki/) and roadmap (roadmap/) content pages."""

from __future__ import annotations

import re
from pathlib import Path
from typing import Any

import markdown

ROOT = Path(__file__).resolve().parent.parent.parent
WIKI_DIR = ROOT / "wiki" / "docs"
ROADMAP_DIR = ROOT / "roadmap" / "docs"


def slugify_path(path: Path, base_dir: Path = WIKI_DIR, prefix: str = "wiki") -> str:
    """Convert a content file path to a URL path."""
    rel = path.relative_to(base_dir)
    parts = list(rel.with_suffix("").parts)
    return prefix + "/" + "/".join(parts)


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
    """Order: chapters -> appendices -> everything else."""
    if name == "chapters":
        return (1, name)
    if name == "appendices":
        return (2, name)
    return (3, name)


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
            sort_rank = _sort_key(key)
            child = finalize(child)
            if child.get("is_dir"):
                child["_sort"] = sort_rank
                dirs.append(child)
            else:
                files.append(child)
        dirs.sort(key=lambda c: c.pop("_sort", (9, "")))
        files.sort(key=lambda c: c.get("path", ""))
        node["children"] = dirs + files
        return node

    return finalize(root)


def rewrite_md_links(text: str, prefix: str = "wiki") -> str:
    """Rewrite relative .md links (e.g. chapters/chapter-01.md#sec) to /<prefix>/ URLs."""

    def repl(m: re.Match) -> str:
        label, href = m.group(1), m.group(2)
        if href.startswith(("http://", "https://", "#", "/", "mailto:")):
            return m.group(0)
        mm = re.match(r"^(?:\.\./)*(.+?)\.md(#.*)?$", href)
        if not mm:
            return m.group(0)
        path, anchor = mm.group(1), mm.group(2) or ""
        return f"[{label}](/{prefix}/{path}/{anchor})"

    return re.sub(r"(?<!!)\[([^\]]*)\]\(([^)\s]+)\)", repl, text)


def is_stub_page(text: str) -> bool:
    """Detect placeholder chapters/appendices with no real content."""
    return len(text.strip()) < 500 or "正在撰写中" in text


def _render_pages(base_dir: Path, prefix: str) -> list[dict[str, Any]]:
    """Load Markdown files under ``base_dir`` and convert them to HTML.

    Relative .md links are rewritten to ``/<prefix>/`` URLs. Returns a list of
    page dicts with title, url, body_html, toc_html, stub flag, and metadata.
    Prev/next links are NOT set here — each product applies its own reading
    order.
    """
    if not base_dir.exists():
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
    for path in sorted(base_dir.rglob("*.md")):
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
        url = slugify_path(path, base_dir, prefix)
        text = rewrite_md_links(text, prefix)
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
    return pages


def _link_prev_next(pages: list[dict[str, Any]]) -> None:
    """Set prev_page/next_page on each page following the list order."""
    for i, page in enumerate(pages):
        page["prev_page"] = pages[i - 1] if i > 0 else None
        page["next_page"] = pages[i + 1] if i < len(pages) - 1 else None


def build_wiki_pages() -> list[dict[str, Any]]:
    """Load all wiki Markdown files and convert them to HTML."""
    pages = _render_pages(WIKI_DIR, "wiki")

    # Prev/next navigation across substantive pages in reading order:
    # chapters -> appendices -> everything else.
    def order_key(p: dict[str, Any]) -> tuple[int, str]:
        rel = Path(p["path"]).relative_to(WIKI_DIR).as_posix()
        if rel.startswith("chapters/"):
            return (1, rel)
        if rel.startswith("appendices/"):
            return (2, rel)
        return (3, rel)

    readable = [p for p in pages if not p["stub"]]
    readable.sort(key=order_key)
    _link_prev_next(readable)
    return pages


# Fixed reading order of the 0→1 roadmap: overview, four stages, then the
# four selection playbooks. Also drives prev/next links and the index page.
ROADMAP_ORDER = [
    "index",
    "stage-0-foundations",
    "stage-1-actuator",
    "stage-2-biped",
    "stage-3-humanoid",
    "playbooks/actuator-selection",
    "playbooks/compute-selection",
    "playbooks/sensor-selection",
    "playbooks/sim-setup",
]


def build_roadmap_pages() -> list[dict[str, Any]]:
    """Load the 0→1 roadmap pages (roadmap/docs/) and convert them to HTML.

    Roadmap is a separate product from the wiki: URLs live under /roadmap/
    and prev/next follows the fixed ROADMAP_ORDER chain. Pages are returned
    in that order.
    """
    pages = _render_pages(ROADMAP_DIR, "roadmap")

    def order_key(p: dict[str, Any]) -> tuple[int, str]:
        rel = Path(p["path"]).relative_to(ROADMAP_DIR).with_suffix("").as_posix()
        return (ROADMAP_ORDER.index(rel) if rel in ROADMAP_ORDER else len(ROADMAP_ORDER), rel)

    readable = [p for p in pages if not p["stub"]]
    readable.sort(key=order_key)
    _link_prev_next(readable)
    return sorted(pages, key=order_key)


def build_roadmap_tree(pages: list[dict[str, Any]]) -> dict[str, Any]:
    """Build the roadmap index tree: overview + stages flat, playbooks nested.

    Expects pages in ROADMAP_ORDER (as returned by ``build_roadmap_pages``).
    Node shape matches what the ``render_tree`` macro in the index templates
    consumes: ``title``, ``url`` (files only), ``children`` (dirs only),
    ``is_dir``, ``path``.
    """
    root: dict[str, Any] = {"title": "Roadmap", "is_dir": True, "children": [], "path": ""}
    playbooks: dict[str, Any] = {"title": "选型手册", "is_dir": True, "children": [], "path": "playbooks"}
    for page in pages:
        if page.get("stub"):
            continue
        node = {
            "title": page["title"],
            "url": page["url"],
            "is_dir": False,
            "path": page["url"][len("roadmap/"):],
        }
        if node["path"].startswith("playbooks/"):
            playbooks["children"].append(node)
        else:
            root["children"].append(node)
    if playbooks["children"]:
        root["children"].append(playbooks)
    return root
