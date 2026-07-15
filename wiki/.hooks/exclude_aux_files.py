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


def on_files(files: Any, config: dict[str, Any], **kwargs: Any) -> Any:
    """Exclude auto-generated relationship pages and underscore-prefixed templates from the build."""
    to_remove = [
        f for f in files
        if f.src_path.startswith("kg/relationships/") or f.name.startswith("_")
    ]
    for f in to_remove:
        files.remove(f)
    return files
