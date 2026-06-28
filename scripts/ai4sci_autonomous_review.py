#!/usr/bin/env python3
"""
Autonomous review and archival workflow for AI-generated staging drafts.

This script performs heuristic quality checks (schema validity, duplicates,
source quality, endpoint existence, cross-layer rules) and automatically
approves or rejects staged entries and relationships. Approved drafts are
moved to production; rejected drafts are moved to .staging/rejected with a
reason note.

Usage:
    source .venv/bin/activate
    python scripts/ai4sci_autonomous_review.py --dry-run
    python scripts/ai4sci_autonomous_review.py
    python scripts/ai4sci_autonomous_review.py --workstream battery_cells
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from typing import Any

import yaml

try:
    from jsonschema import Draft202012Validator, ValidationError
except ImportError as e:
    print(f"Missing dependency: {e}")
    sys.exit(1)

from ai4sci_lib import config, entry_builder, llm_client, staging


ROOT = config.ROOT
SCHEMA_DIR = config.SCHEMA_DIR
RESEARCH_DIR = config.RESEARCH_DIR
RELATIONSHIPS_DIR = config.RELATIONSHIPS_DIR
STAGING_DIR = config.STAGING_DIR

ENTRY_SCHEMA = json.loads((SCHEMA_DIR / "entry_schema.json").read_text())
RELATIONSHIP_SCHEMA = json.loads((SCHEMA_DIR / "relationship_schema.json").read_text())
ENTRY_VALIDATOR = Draft202012Validator(ENTRY_SCHEMA)
REL_VALIDATOR = Draft202012Validator(RELATIONSHIP_SCHEMA)


@dataclass
class ReviewResult:
    approved_entries: list[Path] = field(default_factory=list)
    approved_rels: list[Path] = field(default_factory=list)
    rejected_entries: list[tuple[Path, str]] = field(default_factory=list)
    rejected_rels: list[tuple[Path, str]] = field(default_factory=list)
    skipped_entries: list[tuple[Path, str]] = field(default_factory=list)
    skipped_rels: list[tuple[Path, str]] = field(default_factory=list)


def load_frontmatter(path: Path) -> tuple[dict[str, Any] | None, str]:
    """Load YAML frontmatter and body from a Markdown file."""
    try:
        text = path.read_text(encoding="utf-8")
        if not text.startswith("---"):
            return None, ""
        _, rest = text.split("---", 1)
        yaml_text, body = rest.split("---", 1)
        return yaml.safe_load(yaml_text), body
    except Exception:
        return None, ""


def save_yaml_frontmatter(path: Path, frontmatter: dict[str, Any], body: str) -> None:
    new_yaml = yaml.dump(frontmatter, sort_keys=False, allow_unicode=True, default_flow_style=False)
    path.write_text(f"---\n{new_yaml}---\n\n{body.strip()}\n", encoding="utf-8")


def validate_frontmatter(frontmatter: dict[str, Any], validator: Draft202012Validator) -> list[str]:
    errors: list[str] = []
    try:
        validator.validate(frontmatter)
    except ValidationError as e:
        errors.append(f"{e.message} at {'/'.join(map(str, e.path))}")
    return errors


def collect_entity_ids(base_dirs: list[Path]) -> set[str]:
    """Collect all entity $id values under the given base directories."""
    ids: set[str] = set()
    for base_dir in base_dirs:
        research_dir = base_dir / "research"
        if not research_dir.exists():
            continue
        for path in research_dir.rglob("*.md"):
            frontmatter, _ = load_frontmatter(path)
            if not frontmatter:
                continue
            eid = frontmatter.get("$id")
            if eid:
                ids.add(eid)
    return ids


def collect_production_entity_lookup() -> dict[str, dict[str, Any]]:
    """Build a lookup of production entity $id -> {type, theoretical_depth, path}."""
    lookup: dict[str, dict[str, Any]] = {}
    if not RESEARCH_DIR.exists():
        return lookup
    for path in RESEARCH_DIR.rglob("*.md"):
        frontmatter, _ = load_frontmatter(path)
        if not frontmatter:
            continue
        eid = frontmatter.get("$id")
        if not eid:
            continue
        lookup[eid] = {
            "type": frontmatter.get("type", "paper"),
            "theoretical_depth": frontmatter.get("theoretical_depth", []),
            "path": path,
        }
    return lookup


def collect_production_titles() -> set[str]:
    """Collect normalized titles already present in production."""
    titles: set[str] = set()
    if not RESEARCH_DIR.exists():
        return titles
    for path in RESEARCH_DIR.rglob("*.md"):
        frontmatter, _ = load_frontmatter(path)
        if not frontmatter:
            continue
        title = frontmatter.get("names", {}).get("en") or frontmatter.get("title", "")
        if title:
            titles.add(title.strip().lower())
    return titles


def _depth_for_lookup(entity: dict[str, Any]) -> str:
    depths = entity.get("theoretical_depth", [])
    if depths:
        for d in config.THEORETICAL_DEPTH_ORDER:
            if d in depths:
                return d
        return depths[0]
    type_to_depth = {
        "paper": "system",
        "robot_system": "system",
        "component": "system",
        "material": "system",
        "technology": "method",
        "method": "method",
        "algorithm": "method",
        "formalism": "formalism",
        "equation": "formalism",
        "operator": "formalism",
        "variable": "formalism",
        "constant": "formalism",
        "principle": "principle",
        "theorem": "principle",
        "foundation": "foundation",
        "benchmark": "system",
        "dataset": "system",
    }
    return type_to_depth.get(entity.get("type", "paper"), "system")


def is_cross_layer_allowed(rel_type: str, source: dict[str, Any], target: dict[str, Any]) -> bool:
    source_depth = _depth_for_lookup(source)
    target_depth = _depth_for_lookup(target)
    if source_depth == target_depth:
        return True
    allowed = config.CROSS_LAYER_RELATIONSHIPS.get((source_depth, target_depth), [])
    generic = {
        "cites", "verified_by", "conflicts_with", "is_version_of",
        "is_alternative_to", "competes_with", "is_substitute_for",
        "proposes", "evaluates_on", "uses", "is_based_on",
    }
    return rel_type in allowed or rel_type in generic


def heuristic_relevance(frontmatter: dict[str, Any]) -> bool:
    """Fast keyword-based relevance check."""
    text = " ".join([
        frontmatter.get("names", {}).get("en", ""),
        frontmatter.get("summary", {}).get("en", ""),
        " ".join(frontmatter.get("tags", [])),
    ]).lower()
    return any(kw.lower() in text for kw in config.HUMANOID_KEYWORDS)


def llm_review_entry(frontmatter: dict[str, Any]) -> tuple[bool, str, int]:
    """Use an LLM to judge whether an entry should be approved.

    Returns (approved, reason, quality_score).
    """
    system_prompt = (
        "You are a strict reviewer for a humanoid-robot knowledge graph. "
        "Decide whether the following entity draft should be approved. "
        "Consider: (1) relevance to humanoid robotics or its supply chain, "
        "components, AI, manufacturing, or evaluation; (2) factual plausibility; "
        "(3) completeness of metadata (names, summary, domains, sources). "
        "Return JSON only with keys: decision ('approve' or 'reject'), reason (string), quality_score (integer 1-10)."
    )
    user_prompt = yaml.dump(frontmatter, sort_keys=False, allow_unicode=True, default_flow_style=False)
    try:
        response = llm_client.chat_completion_json(
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ],
            temperature=0.2,
            max_tokens=512,
        )
        decision = str(response.get("decision", "")).lower()
        reason = response.get("reason", "No reason provided.")
        score = int(response.get("quality_score", 0))
        approved = decision == "approve" and score >= 6
        return approved, reason, score
    except Exception as exc:
        return False, f"LLM review failed: {exc}", 0


def check_sources(frontmatter: dict[str, Any]) -> list[str]:
    """Validate source quality. Returns list of issues."""
    issues: list[str] = []
    sources = frontmatter.get("sources", [])
    if not sources:
        issues.append("no sources")
        return issues
    for i, src in enumerate(sources):
        if not src.get("id"):
            issues.append(f"source {i} missing id")
        if not src.get("type"):
            issues.append(f"source {i} missing type")
        if not src.get("title") and not src.get("url"):
            issues.append(f"source {i} missing title and url")
    return issues


def review_entry(
    entry_path: Path,
    production_ids: set[str],
    production_titles: set[str],
    approved_titles: set[str],
    dry_run: bool,
    use_llm: bool,
) -> tuple[str, str | None]:
    """Review a single entry. Returns ('approve'|'reject'|'skip', reason)."""
    frontmatter, body = load_frontmatter(entry_path)
    if frontmatter is None:
        return "reject", "failed to parse YAML frontmatter"

    eid = frontmatter.get("$id")
    if not eid:
        return "reject", "missing $id"

    # Schema validation
    errors = validate_frontmatter(frontmatter, ENTRY_VALIDATOR)
    if errors:
        return "reject", f"schema validation failed: {'; '.join(errors[:3])}"

    # Duplicate check
    if eid in production_ids:
        return "skip", f"duplicate entity id: {eid}"

    title = (frontmatter.get("names", {}).get("en") or frontmatter.get("title", "")).strip()
    if not title:
        return "reject", "missing English name/title"
    norm_title = title.lower()
    if norm_title in production_titles:
        return "skip", f"duplicate title in production: {title}"
    if norm_title in approved_titles:
        return "skip", f"duplicate title already approved in this run: {title}"

    # Source quality
    source_issues = check_sources(frontmatter)
    if source_issues:
        return "reject", f"source issues: {'; '.join(source_issues)}"

    # Optional LLM quality / relevance review
    if use_llm:
        approved, reason, score = llm_review_entry(frontmatter)
        if not approved:
            return "reject", f"LLM review rejected (score {score}): {reason}"

    # Approve
    if not dry_run:
        verification = frontmatter.get("verification", {})
        verification["status"] = "partially_verified"
        verification["reviewed_by"] = "ai_autonomous"
        verification["reviewed_at"] = datetime.now().date().isoformat()
        verification["confidence"] = "medium"
        notes = verification.get("notes", "")
        verification["notes"] = (
            notes + "; approved by autonomous review workflow."
            if notes else "Approved by autonomous review workflow."
        )
        frontmatter["verification"] = verification
        save_yaml_frontmatter(entry_path, frontmatter, body)

    return "approve", None


def review_relationship(
    rel_path: Path,
    production_lookup: dict[str, dict[str, Any]],
    approved_entry_ids: set[str],
    dry_run: bool,
) -> tuple[str, str | None]:
    """Review a single relationship. Returns ('approve'|'reject'|'skip', reason)."""
    frontmatter, body = load_frontmatter(rel_path)
    if frontmatter is None:
        return "reject", "failed to parse YAML frontmatter"

    rel_type = frontmatter.get("type", "")
    source_id = frontmatter.get("source", {}).get("id")
    target_id = frontmatter.get("target", {}).get("id")
    if not source_id or not target_id:
        return "reject", "missing source or target id"

    # Schema validation
    errors = validate_frontmatter(frontmatter, REL_VALIDATOR)
    if errors:
        return "reject", f"schema validation failed: {'; '.join(errors[:3])}"

    # Normalize relationship type
    norm = entry_builder.normalize_relationship_type(rel_type)
    if norm and norm != rel_type:
        frontmatter["type"] = norm
        rel_type = norm
        frontmatter["$id"] = entry_builder.make_relationship_id(source_id, norm, target_id)
        if not dry_run:
            save_yaml_frontmatter(rel_path, frontmatter, body)

    # Endpoint existence
    if source_id not in approved_entry_ids and source_id not in production_lookup:
        return "reject", f"dangling source: {source_id}"
    if target_id not in approved_entry_ids and target_id not in production_lookup:
        return "reject", f"dangling target: {target_id}"

    # Cross-layer check
    source = production_lookup.get(source_id)
    if source is None:
        # Source is in approved staging entries; we don't have its full metadata yet,
        # so we skip cross-layer enforcement for newly approved entries.
        pass
    else:
        target = production_lookup.get(target_id)
        if target is None:
            # Target is newly approved; skip cross-layer enforcement.
            pass
        else:
            if not is_cross_layer_allowed(rel_type, source, target):
                return "reject", (
                    f"cross-layer rule violated: '{rel_type}' not allowed for "
                    f"{_depth_for_lookup(source)} -> {_depth_for_lookup(target)}"
                )

    if not dry_run:
        verification = frontmatter.get("verification", {})
        verification["status"] = "partially_verified"
        verification["reviewed_by"] = "ai_autonomous"
        verification["reviewed_at"] = datetime.now().date().isoformat()
        verification["confidence"] = "medium"
        frontmatter["verification"] = verification
        save_yaml_frontmatter(rel_path, frontmatter, body)

    return "approve", None


def review_at_base(base_dir: Path, dry_run: bool, use_llm: bool) -> ReviewResult:
    """Autonomously review all staged entries and relationships under base_dir."""
    result = ReviewResult()

    entries = staging.list_staged_entries(base_dir)
    relationships = staging.list_staged_relationships(base_dir)

    if not entries and not relationships:
        return result

    print(f"\nReviewing base: {base_dir}")
    print(f"  entries={len(entries)}, relationships={len(relationships)}")

    production_lookup = collect_production_entity_lookup()
    production_ids = set(production_lookup.keys())
    production_titles = collect_production_titles()
    approved_entry_ids: set[str] = set()
    approved_titles: set[str] = set()

    # First pass: review entries
    for entry_path in entries:
        action, reason = review_entry(entry_path, production_ids, production_titles, approved_titles, dry_run, use_llm)
        if action == "approve":
            title = ""
            if not dry_run:
                try:
                    dest = staging.approve_entry(entry_path, base_dir=base_dir)
                    result.approved_entries.append(dest)
                    frontmatter, _ = load_frontmatter(dest)
                    if frontmatter:
                        approved_entry_ids.add(frontmatter.get("$id", ""))
                        title = (frontmatter.get("names", {}).get("en") or frontmatter.get("title", "")).strip().lower()
                except FileExistsError as exc:
                    result.rejected_entries.append((entry_path, f"production collision: {exc}"))
            else:
                result.approved_entries.append(entry_path)
                frontmatter, _ = load_frontmatter(entry_path)
                if frontmatter:
                    approved_entry_ids.add(frontmatter.get("$id", ""))
                    title = (frontmatter.get("names", {}).get("en") or frontmatter.get("title", "")).strip().lower()
            if title:
                approved_titles.add(title)
        elif action == "reject":
            if not dry_run:
                dest = staging.reject_entry(entry_path, reason or "Autonomous review rejection.", base_dir=base_dir)
                result.rejected_entries.append((dest, reason or ""))
            else:
                result.rejected_entries.append((entry_path, reason or ""))
        else:
            result.skipped_entries.append((entry_path, reason or ""))

    # Second pass: review relationships using updated endpoint set
    all_endpoint_ids = production_ids | approved_entry_ids
    for rel_path in relationships:
        frontmatter, _ = load_frontmatter(rel_path)
        if not frontmatter:
            result.rejected_rels.append((rel_path, "failed to parse YAML frontmatter"))
            continue
        source_id = frontmatter.get("source", {}).get("id")
        target_id = frontmatter.get("target", {}).get("id")
        if source_id not in all_endpoint_ids or target_id not in all_endpoint_ids:
            reason = f"dangling relationship ({source_id} -> {target_id})"
            if not dry_run:
                dest = staging.reject_entry(rel_path, reason, base_dir=base_dir)
                result.rejected_rels.append((dest, reason))
            else:
                result.rejected_rels.append((rel_path, reason))
            continue

        action, reason = review_relationship(rel_path, production_lookup, approved_entry_ids, dry_run)
        if action == "approve":
            if not dry_run:
                try:
                    dest = staging.approve_relationship(rel_path)
                    result.approved_rels.append(dest)
                except FileExistsError as exc:
                    result.rejected_rels.append((rel_path, f"production collision: {exc}"))
            else:
                result.approved_rels.append(rel_path)
        elif action == "reject":
            if not dry_run:
                dest = staging.reject_entry(rel_path, reason or "Autonomous review rejection.", base_dir=base_dir)
                result.rejected_rels.append((dest, reason or ""))
            else:
                result.rejected_rels.append((rel_path, reason or ""))
        else:
            result.skipped_rels.append((rel_path, reason or ""))

    return result


def write_report(result: ReviewResult, report_path: Path) -> None:
    lines: list[str] = []
    lines.append("# Autonomous Review Report\n")
    lines.append(f"Generated: {datetime.now().isoformat()}\n")
    lines.append("\n## Summary\n")
    lines.append(f"- Approved entries: {len(result.approved_entries)}\n")
    lines.append(f"- Approved relationships: {len(result.approved_rels)}\n")
    lines.append(f"- Rejected entries: {len(result.rejected_entries)}\n")
    lines.append(f"- Rejected relationships: {len(result.rejected_rels)}\n")
    lines.append(f"- Skipped entries: {len(result.skipped_entries)}\n")
    lines.append(f"- Skipped relationships: {len(result.skipped_rels)}\n")

    def section(title: str, items: list[tuple[Path, str]]) -> None:
        if not items:
            return
        lines.append(f"\n## {title}\n")
        for path, reason in items:
            lines.append(f"- `{path}`: {reason}\n")

    section("Approved Entries", [(p, "approved") for p in result.approved_entries])
    section("Approved Relationships", [(p, "approved") for p in result.approved_rels])
    section("Rejected Entries", result.rejected_entries)
    section("Rejected Relationships", result.rejected_rels)
    section("Skipped Entries", result.skipped_entries)
    section("Skipped Relationships", result.skipped_rels)

    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text("".join(lines), encoding="utf-8")


def load_api_key_from_file(path: Path = Path.home() / "Desktop" / "ai4sci_api_key.txt") -> bool:
    """Load AI4SCI_API_KEY from a shell-style env file if present."""
    if not path.exists():
        return False
    try:
        for line in path.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            if "=" in line:
                key, value = line.split("=", 1)
                key = key.strip()
                value = value.strip().strip("'\"")
                if key and key not in os.environ:
                    os.environ[key] = value
        return bool(os.environ.get("AI4SCI_API_KEY") or os.environ.get("OPENAI_API_KEY"))
    except Exception:
        return False


def main() -> int:
    parser = argparse.ArgumentParser(description="Autonomous review and archival of staged drafts.")
    parser.add_argument("--dry-run", action="store_true", help="Preview decisions without moving files.")
    parser.add_argument("--workstream", default=None, help="Review a specific workstream staging directory.")
    parser.add_argument("--all-workstreams", action="store_true", help="Review all workstream staging directories.")
    parser.add_argument("--report", type=Path, default=None, help="Path for the review report.")
    parser.add_argument(
        "--llm-review",
        action="store_true",
        help="Use an LLM to judge entry relevance and quality (slower but more accurate).",
    )
    args = parser.parse_args()

    if args.llm_review:
        if not (os.environ.get("AI4SCI_API_KEY") or os.environ.get("OPENAI_API_KEY")):
            load_api_key_from_file()
        has_key = bool(os.environ.get("AI4SCI_API_KEY") or os.environ.get("OPENAI_API_KEY"))
        has_cli = os.environ.get("AI4SCI_USE_KIMI_CLI", "").lower() in ("1", "true", "yes")
        if not has_key and not has_cli:
            print("Warning: --llm-review requested but no LLM API key or CLI fallback found.", file=sys.stderr)

    staging.ensure_staging_dirs()

    base_dirs: list[Path] = []
    if args.workstream:
        base_dirs.append(STAGING_DIR / "workstreams" / args.workstream)
    elif args.all_workstreams:
        workstreams_dir = STAGING_DIR / "workstreams"
        if workstreams_dir.exists():
            base_dirs.extend(sorted(d for d in workstreams_dir.iterdir() if d.is_dir()))
        base_dirs.append(STAGING_DIR)
    else:
        base_dirs.append(STAGING_DIR)

    overall = ReviewResult()
    for base_dir in base_dirs:
        if not base_dir.exists():
            print(f"Skipping non-existent base: {base_dir}")
            continue
        res = review_at_base(base_dir, args.dry_run, args.llm_review)
        overall.approved_entries.extend(res.approved_entries)
        overall.approved_rels.extend(res.approved_rels)
        overall.rejected_entries.extend(res.rejected_entries)
        overall.rejected_rels.extend(res.rejected_rels)
        overall.skipped_entries.extend(res.skipped_entries)
        overall.skipped_rels.extend(res.skipped_rels)

    print("\n--- Autonomous Review Summary ---")
    print(f"Approved entries: {len(overall.approved_entries)}")
    print(f"Approved relationships: {len(overall.approved_rels)}")
    print(f"Rejected entries: {len(overall.rejected_entries)}")
    print(f"Rejected relationships: {len(overall.rejected_rels)}")
    print(f"Skipped entries: {len(overall.skipped_entries)}")
    print(f"Skipped relationships: {len(overall.skipped_rels)}")

    report_path = args.report or (
        STAGING_DIR / "review" / f"autonomous_review_{datetime.now().strftime('%Y%m%d_%H%M%S')}.md"
    )
    write_report(overall, report_path)
    print(f"\nReport written to: {report_path}")

    if overall.approved_entries or overall.approved_rels:
        print("\nRunning validation...")
        import subprocess
        result = subprocess.run([sys.executable, "scripts/validate_entries.py"], cwd=ROOT)
        if result.returncode != 0:
            print("Validation failed. Please inspect approved drafts.", file=sys.stderr)
            return result.returncode

    return 0


if __name__ == "__main__":
    sys.exit(main())
