#!/usr/bin/env python3
"""
Interactive review and approval workflow for staged AI-generated drafts.

Usage:
    source .venv/bin/activate
    python scripts/ai4sci_review.py

The script lists staged entries and relationships, then prompts for approve/edit/reject.
"""

from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import sys
from datetime import datetime
from pathlib import Path

import yaml

from ai4sci_lib import config, entry_builder, staging


def load_yaml_frontmatter(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---"):
        raise ValueError(f"No YAML frontmatter in {path}")
    _, rest = text.split("---", 1)
    yaml_text, _ = rest.split("---", 1)
    return yaml.safe_load(yaml_text)


def _entry_id_exists(entry_id: str) -> bool:
    """Check whether an entry with the given $id exists in production."""
    for path in config.RESEARCH_DIR.rglob("*.md"):
        try:
            data = load_yaml_frontmatter(path)
            if data.get("$id") == entry_id:
                return True
        except Exception:
            continue
    return False


def save_yaml_frontmatter(path: Path, frontmatter: dict) -> None:
    text = path.read_text(encoding="utf-8")
    _, rest = text.split("---", 1)
    _, body = rest.split("---", 1)
    new_yaml = yaml.dump(frontmatter, sort_keys=False, allow_unicode=True, default_flow_style=False)
    path.write_text(f"---\n{new_yaml}---\n{body}", encoding="utf-8")


def prompt_choice(question: str, choices: list[str]) -> str:
    while True:
        answer = input(f"{question} [{'/'.join(choices)}]: ").strip().lower()
        if answer in choices:
            return answer
        print("Invalid choice. Try again.")


def review_entry(entry_path: Path) -> tuple[str, str | None]:
    """Interactively review one entry. Returns (action, reason)."""
    print(f"\nReviewing entry: {entry_path}")
    try:
        data = load_yaml_frontmatter(entry_path)
    except Exception as exc:
        print(f"  Error reading frontmatter: {exc}")
        return "skip", None

    print(f"  ID: {data.get('$id')}")
    print(f"  Type: {data.get('type')}")
    print(f"  Names (en): {data.get('names', {}).get('en', 'N/A')}")
    print(f"  Domains: {data.get('domains')}")
    print(f"  Verification: {data.get('verification', {}).get('status')} "
          f"({data.get('verification', {}).get('reviewed_by')})")

    action = prompt_choice("Action", ["approve", "edit", "reject", "skip"])
    if action == "approve":
        return "approve", None
    if action == "edit":
        editor = shutil.which("vim") or shutil.which("nano") or shutil.which("code")
        if editor:
            subprocess.call([editor, str(entry_path)])
        else:
            print("No editor found; please edit the file manually and rerun.")
            return "skip", None
        # Re-read and ask again.
        return review_entry(entry_path)
    if action == "reject":
        reason = input("Reason for rejection: ").strip()
        return "reject", reason
    return "skip", None


def approve_entry(entry_path: Path) -> Path:
    data = load_yaml_frontmatter(entry_path)
    verification = data.get("verification", {})
    verification["status"] = "partially_verified"
    verification["reviewed_by"] = "human_and_ai"
    verification["reviewed_at"] = datetime.now().date().isoformat()
    verification["confidence"] = "medium"
    notes = verification.get("notes", "")
    if notes:
        verification["notes"] = notes + "; approved by human reviewer."
    else:
        verification["notes"] = "Approved by human reviewer after AI extraction."
    data["verification"] = verification
    save_yaml_frontmatter(entry_path, data)
    return staging.approve_entry(entry_path)


def reject_entry(entry_path: Path, reason: str) -> Path:
    return staging.reject_entry(entry_path, reason)


def review_relationship(rel_path: Path) -> tuple[str, str | None]:
    print(f"\nReviewing relationship: {rel_path.name}")
    try:
        data = load_yaml_frontmatter(rel_path)
    except Exception as exc:
        print(f"  Error reading frontmatter: {exc}")
        return "skip", None

    print(f"  ID: {data.get('$id')}")
    print(f"  Type: {data.get('type')}")
    src = data.get("source", {}).get("id", "N/A")
    tgt = data.get("target", {}).get("id", "N/A")
    print(f"  {src} --{data.get('type')}--> {tgt}")

    action = prompt_choice("Action", ["approve", "reject", "skip"])
    if action == "approve":
        return "approve", None
    if action == "reject":
        reason = input("Reason for rejection: ").strip()
        return "reject", reason
    return "skip", None


def approve_relationship(rel_path: Path) -> Path:
    data = load_yaml_frontmatter(rel_path)
    verification = data.get("verification", {})
    verification["status"] = "partially_verified"
    verification["reviewed_by"] = "human_and_ai"
    verification["reviewed_at"] = datetime.now().date().isoformat()
    verification["confidence"] = "medium"
    data["verification"] = verification
    save_yaml_frontmatter(rel_path, data)
    return staging.approve_relationship(rel_path)


def _review_at_base(base_dir: Path, auto_approve: bool) -> tuple[list[Path], list[Path], list[Path], list[Path]]:
    """Review all staged entries and relationships under a base directory."""
    entries = staging.list_staged_entries(base_dir)
    relationships = staging.list_staged_relationships(base_dir)

    if not entries and not relationships:
        print(f"No staged drafts to review in {base_dir}.")
        return [], [], [], []

    print(f"Found {len(entries)} staged entr{'y' if len(entries) == 1 else 'ies'} "
          f"and {len(relationships)} staged relationship{'s' if len(relationships) != 1 else ''} in {base_dir}.")

    approved_entries: list[Path] = []
    approved_rels: list[Path] = []
    rejected_entries: list[Path] = []
    rejected_rels: list[Path] = []

    for entry_path in entries:
        if auto_approve:
            action = "approve"
            reason = None
        else:
            action, reason = review_entry(entry_path)

        if action == "approve":
            approved_entries.append(staging.approve_entry(entry_path, base_dir=base_dir))
        elif action == "reject":
            rejected_entries.append(staging.reject_entry(entry_path, reason or "No reason provided.", base_dir=base_dir))

    for rel_path in relationships:
        # Only approve relationships whose source entry was approved or already exists.
        rel_data = load_yaml_frontmatter(rel_path)
        source_id = rel_data.get("source", {}).get("id", "")
        if not any(p.name == f"{source_id}.md" for p in approved_entries):
            if not _entry_id_exists(source_id):
                print(f"\nSkipping relationship {rel_path.name}: source entry {source_id} not approved.")
                continue

        if auto_approve:
            action = "approve"
            reason = None
        else:
            action, reason = review_relationship(rel_path)

        if action == "approve":
            approved_rels.append(staging.approve_relationship(rel_path))
        elif action == "reject":
            rejected_rels.append(staging.reject_entry(rel_path, reason or "No reason provided.", base_dir=base_dir))

    return approved_entries, approved_rels, rejected_entries, rejected_rels


def main() -> int:
    parser = argparse.ArgumentParser(description="Review staged AI-generated drafts.")
    parser.add_argument(
        "--auto-approve",
        action="store_true",
        help="Approve all staged drafts without prompting (use with caution).",
    )
    parser.add_argument(
        "--workstream",
        default=None,
        help="Review drafts from a specific workstream staging directory.",
    )
    parser.add_argument(
        "--workstreams-dir",
        type=Path,
        default=config.STAGING_DIR / "workstreams",
        help="Base directory containing workstream staging dirs.",
    )
    parser.add_argument(
        "--all-workstreams",
        action="store_true",
        help="Review drafts from all workstream staging directories plus the default staging area.",
    )
    args = parser.parse_args()

    staging.ensure_staging_dirs()

    base_dirs: list[Path] = []
    if args.workstream:
        base_dirs.append(args.workstreams_dir / args.workstream)
    elif args.all_workstreams:
        if args.workstreams_dir.exists():
            base_dirs.extend(sorted(d for d in args.workstreams_dir.iterdir() if d.is_dir()))
        base_dirs.append(config.STAGING_DIR)
    else:
        base_dirs.append(config.STAGING_DIR)

    all_approved_entries: list[Path] = []
    all_approved_rels: list[Path] = []
    all_rejected_entries: list[Path] = []
    all_rejected_rels: list[Path] = []

    for base_dir in base_dirs:
        ae, ar, re, rr = _review_at_base(base_dir, args.auto_approve)
        all_approved_entries.extend(ae)
        all_approved_rels.extend(ar)
        all_rejected_entries.extend(re)
        all_rejected_rels.extend(rr)

    print("\n--- Overall Summary ---")
    print(f"Approved entries: {len(all_approved_entries)}")
    for p in all_approved_entries:
        print(f"  + {p}")
    print(f"Approved relationships: {len(all_approved_rels)}")
    for p in all_approved_rels:
        print(f"  + {p}")
    print(f"Rejected entries: {len(all_rejected_entries)}")
    for p in all_rejected_entries:
        print(f"  - {p}")
    print(f"Rejected relationships: {len(all_rejected_rels)}")
    for p in all_rejected_rels:
        print(f"  - {p}")

    if all_approved_entries or all_approved_rels:
        print("\nRunning validation...")
        result = subprocess.run(
            [sys.executable, "scripts/validate_entries.py"],
            cwd=config.ROOT,
        )
        if result.returncode != 0:
            print("Validation failed. Please fix the approved drafts.", file=sys.stderr)
            return result.returncode

    return 0


if __name__ == "__main__":
    sys.exit(main())
