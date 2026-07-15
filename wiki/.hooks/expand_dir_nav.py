"""
MkDocs hook that expands directory references in the nav into explicit page lists
and excludes auto-generated relationship files from the build.

Loaded via `hooks:` in mkdocs.yml.
"""

from __future__ import annotations

import re
from pathlib import Path
from typing import Any

import yaml


def _title_from_file(path: Path) -> str:
    """Derive a nav title from frontmatter title/names.zh or the first H1 heading."""
    try:
        text = path.read_text(encoding="utf-8")
    except Exception:
        return path.stem

    # Frontmatter
    if text.startswith("---"):
        parts = text.split("---", 2)
        if len(parts) >= 3:
            try:
                fm = yaml.safe_load(parts[1]) or {}
            except Exception:
                fm = {}
            if isinstance(fm, dict):
                for key in ("title", "name"):
                    val = fm.get(key)
                    if isinstance(val, str) and val.strip():
                        return val.strip()
                names = fm.get("names")
                if isinstance(names, dict):
                    for lang in ("zh", "en", "ko"):
                        val = names.get(lang)
                        if isinstance(val, str) and val.strip():
                            return val.strip()
            text = parts[2]

    # First Markdown H1 heading
    for line in text.splitlines():
        m = re.match(r"^#\s+(.+)$", line)
        if m:
            return m.group(1).strip()

    return path.stem


def _expand_path(path: str, docs_dir: Path, default_title: str | None = None) -> Any:
    full = docs_dir / path
    if full.is_file() and full.suffix == ".md":
        if default_title:
            return {default_title: path}
        return path

    if full.is_dir():
        children: list[Any] = []
        for entry in sorted(full.iterdir()):
            name = entry.name
            if name.startswith("_") or name == ".pages":
                continue
            if entry.is_file() and entry.suffix == ".md":
                children.append({_title_from_file(entry): str(entry.relative_to(docs_dir))})
            elif entry.is_dir():
                children.append(_expand_path(str(entry.relative_to(docs_dir)), docs_dir))
        title = default_title or _title_from_dir(full)
        return {title: children}

    # Fallback: keep the original reference so MkDocs can report it.
    return {default_title or path: path}


def _title_from_dir(path: Path) -> str:
    # Use a .pages title if present
    pages_file = path / ".pages"
    if pages_file.exists():
        try:
            data = yaml.safe_load(pages_file.read_text(encoding="utf-8")) or {}
            if isinstance(data, dict) and data.get("title"):
                return str(data["title"])
        except Exception:
            pass
    return path.name


def _expand_item(item: Any, docs_dir: Path) -> Any:
    if isinstance(item, str):
        return _expand_path(item, docs_dir)
    if isinstance(item, dict):
        expanded = []
        for title, path in item.items():
            if isinstance(path, list):
                expanded.append({title: [_expand_item(child, docs_dir) for child in path]})
            else:
                expanded.append(_expand_path(path, docs_dir, default_title=title))
        # A dict entry always expands to a single node; keep it as dict
        return expanded[0] if len(expanded) == 1 else expanded
    if isinstance(item, list):
        return [_expand_item(i, docs_dir) for i in item]
    return item


def on_config(config: dict[str, Any], **kwargs: Any) -> dict[str, Any]:
    docs_dir = Path(config.get("docs_dir", "docs")).resolve()
    nav = config.get("nav", [])
    config["nav"] = [_expand_item(item, docs_dir) for item in nav]
    return config


def on_files(files: Any, config: dict[str, Any], **kwargs: Any) -> Any:
    """Exclude auto-generated relationship pages from the build to avoid nav bloat."""
    to_remove = [f for f in files if f.src_path.startswith("kg/relationships/")]
    for f in to_remove:
        files.remove(f)
    return files
