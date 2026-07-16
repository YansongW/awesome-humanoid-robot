"""Staging area management for AI-generated drafts."""

from __future__ import annotations

import shutil
from datetime import datetime
from pathlib import Path

from . import config


def ensure_staging_dirs_for(base_dir: Path | None = None) -> None:
    """Create all staging subdirectories under the given base directory."""
    base = base_dir or config.STAGING_DIR
    dirs = [
        base / "research",
        base / "data" / "relationships",
        base / "review",
        base / "rejected",
        base / "pdfs",
    ]
    for d in dirs:
        d.mkdir(parents=True, exist_ok=True)


def ensure_staging_dirs() -> None:
    """Create all staging subdirectories in the default staging area."""
    ensure_staging_dirs_for(config.STAGING_DIR)


def list_staged_entries(base_dir: Path | None = None) -> list[Path]:
    """Return all staged entity files under the given base directory."""
    base = base_dir or config.STAGING_DIR
    ensure_staging_dirs_for(base)
    return sorted((base / "research").rglob("*.md"))


def list_staged_relationships(base_dir: Path | None = None) -> list[Path]:
    """Return all staged relationship files under the given base directory."""
    base = base_dir or config.STAGING_DIR
    ensure_staging_dirs_for(base)
    return sorted((base / "data" / "relationships").glob("*.md"))


def approve_entry(staged_path: Path, base_dir: Path | None = None) -> Path:
    """Move a staged entity file to the production research directory."""
    base = base_dir or config.STAGING_DIR
    rel = staged_path.relative_to(base / "research")
    dest = config.RESEARCH_DIR / rel
    dest.parent.mkdir(parents=True, exist_ok=True)
    if dest.exists():
        raise FileExistsError(f"Production entry already exists: {dest}")
    shutil.move(str(staged_path), str(dest))
    # Clean up empty staging subdirectories.
    staged_path.parent.rmdir() if not any(staged_path.parent.iterdir()) else None
    return dest


def approve_relationship(staged_path: Path) -> Path:
    """Move a staged relationship file to the production relationships directory."""
    dest = config.RELATIONSHIPS_DIR / staged_path.name
    dest.parent.mkdir(parents=True, exist_ok=True)
    if dest.exists():
        raise FileExistsError(f"Production relationship already exists: {dest}")
    shutil.move(str(staged_path), str(dest))
    return dest


def reject_entry(staged_path: Path, reason: str, base_dir: Path | None = None) -> Path:
    """Move a staged file to the rejected directory with a reason note."""
    base = base_dir or config.STAGING_DIR
    ensure_staging_dirs_for(base)
    dest = base / "rejected" / f"{staged_path.stem}.md"
    counter = 1
    while dest.exists():
        dest = base / "rejected" / f"{staged_path.stem}_{counter}.md"
        counter += 1
    shutil.move(str(staged_path), str(dest))
    note = base / "rejected" / f"{dest.stem}.reason.txt"
    # 运行时生成 ISO 时间戳（此前此处残留未替换的 __TIMESTAMP__ 占位符）
    note.write_text(f"Rejected at: {datetime.now().isoformat()}\nReason: {reason}\n", encoding="utf-8")
    return dest
