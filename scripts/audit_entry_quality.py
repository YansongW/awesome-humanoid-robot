#!/usr/bin/env python3
"""
Audit knowledge-graph entry quality against the project content standard.

Outputs:
    .staging/quality_reports/quality_report_YYYYMMDD_HHMMSS.json
    .staging/quality_reports/quality_report_YYYYMMDD_HHMMSS.md

Usage:
    python scripts/audit_entry_quality.py
    python scripts/audit_entry_quality.py --min-chars-zh 400
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import yaml

sys.path.insert(0, str(Path(__file__).parent))
from ai4sci_lib import config

ROOT = Path(__file__).parent.parent
RESEARCH_DIR = ROOT / "research"
RELATIONSHIPS_DIR = ROOT / "data" / "relationships"
REPORT_DIR = ROOT / ".staging" / "quality_reports"

# Minimum meaningful Chinese body characters by entity type.
MIN_CHARS_ZH: dict[str, int] = {
    "method": 400,
    "principle": 400,
    "formalism": 400,
    "foundation": 400,
    "technology": 400,
    "component": 300,
    "material": 300,
    "software_platform": 300,
    "tool_equipment": 300,
    "company": 300,
    "oem": 300,
    "tier1_supplier": 300,
    "tier2_supplier": 300,
    "component_manufacturer": 300,
    "process": 500,
    "paper": 200,
    "report": 200,
    "dataset": 200,
    "benchmark": 200,
    "standard": 200,
}

DEFAULT_MIN_CHARS = 300

RELATIONSHIP_SCHEMA = {
    "required": {"type", "source", "target"},
    "source_required": {"id"},
    "target_required": {"id"},
}


def split_frontmatter(text: str) -> tuple[dict[str, Any] | None, str]:
    if not text.startswith("---"):
        return None, text
    parts = text.split("---", 2)
    if len(parts) < 3:
        return None, text
    try:
        fm = yaml.safe_load(parts[1]) or {}
    except Exception as exc:
        return None, text
    return fm, parts[2]


def meaningful_zh_chars(body: str, exclude: list[str]) -> int:
    """Count Chinese characters after removing headings and repeated summary/name text."""
    # Remove Markdown headings
    text = re.sub(r"^#{1,6}\s+", "", body, flags=re.MULTILINE)
    # Remove references section to avoid inflating with URLs
    text = re.split(r"\n## 参考|\n## References|\n## 참고", text, flags=re.IGNORECASE)[0]
    # Remove exact copies of excluded strings
    for s in exclude:
        if not s:
            continue
        text = text.replace(s, "")
    # Count CJK characters
    return len(re.findall(r"[\u4e00-\u9fff]", text))


def meaningful_en_words(body: str) -> int:
    """Count English words in the body, excluding headings."""
    text = re.sub(r"^#{1,6}\s+", "", body, flags=re.MULTILINE)
    text = re.split(r"\n## 参考|\n## References|\n## 참고", text, flags=re.IGNORECASE)[0]
    return len(re.findall(r"[A-Za-z]{2,}", text))


def has_section(body: str, *titles: str) -> bool:
    pattern = re.compile(r"^#{1,6}\s*(" + "|".join(re.escape(t) for t in titles) + r")\s*$", re.MULTILINE | re.IGNORECASE)
    return bool(pattern.search(body))


def load_entry(path: Path) -> dict[str, Any] | None:
    text = path.read_text(encoding="utf-8")
    fm, body = split_frontmatter(text)
    if fm is None:
        return None
    return {"path": path, "fm": fm, "body": body}


def audit_entry(entry: dict[str, Any]) -> dict[str, Any]:
    fm = entry["fm"]
    body = entry["body"]
    eid = fm.get("$id", "")
    etype = fm.get("type", "")

    names = fm.get("names", {}) or {}
    summary = fm.get("summary", {}) or {}
    verification = fm.get("verification", {}) or {}
    sources = fm.get("sources", []) or []
    related = fm.get("related_entities", []) or []

    exclude = []
    for lang in ("zh", "en", "ko"):
        n = names.get(lang, "") if isinstance(names, dict) else ""
        s = summary.get(lang, "") if isinstance(summary, dict) else ""
        if n:
            exclude.append(n)
        if s:
            exclude.append(s)

    zh_chars = meaningful_zh_chars(body, exclude)
    min_chars = MIN_CHARS_ZH.get(etype, DEFAULT_MIN_CHARS)

    issues: list[str] = []

    # Frontmatter checks
    if not names.get("en"):
        issues.append("missing_name_en")
    if not summary.get("en"):
        issues.append("missing_summary_en")
    if not summary.get("zh"):
        issues.append("missing_summary_zh")
    else:
        zh_summary = summary.get("zh", "").strip()
        if zh_summary in (names.get("zh", ""), names.get("en", "")):
            issues.append("summary_is_just_title")
        if len(zh_summary) < 20:
            issues.append("summary_too_short_zh")

    if not sources:
        issues.append("no_sources")

    if not verification.get("status"):
        issues.append("missing_verification_status")
    if not verification.get("reviewed_at"):
        issues.append("missing_reviewed_at")

    # Body checks
    en_words = meaningful_en_words(body)
    body_sufficient = zh_chars >= min_chars
    if etype in ("paper", "report") and not body_sufficient and en_words >= 80:
        body_sufficient = True
    if not body_sufficient:
        issues.append(f"body_too_short_zh ({zh_chars}/{min_chars})")
    if not has_section(body, "概述", "Overview", "개요"):
        issues.append("missing_overview_section")
    if not has_section(
        body,
        "核心内容", "核心原理", "核心方法", "关键子任务与技术内容", "关键活动", "技术内容",
        "方法", "原理", "结构", "实现步骤", "Abstract", "Methods", "Method", "Activities", "Tasks",
    ):
        issues.append("missing_core_section")
    if not has_section(body, "参考", "References", "참고"):
        issues.append("missing_reference_section")

    severity = "ok"
    if any(i.startswith("body_too_short") or i == "missing_overview_section" for i in issues):
        severity = "critical"
    elif issues:
        severity = "warning"

    return {
        "id": eid,
        "type": etype,
        "path": str(entry["path"].relative_to(ROOT)),
        "zh_chars": zh_chars,
        "min_chars": min_chars,
        "summary_zh": summary.get("zh", ""),
        "sources_count": len(sources),
        "related_count": len(related),
        "verification_status": verification.get("status", ""),
        "issues": issues,
        "severity": severity,
    }


def load_relationships() -> list[dict[str, Any]]:
    rels: list[dict[str, Any]] = []
    if not RELATIONSHIPS_DIR.exists():
        return rels
    for path in RELATIONSHIPS_DIR.rglob("*.md"):
        text = path.read_text(encoding="utf-8")
        fm, _ = split_frontmatter(text)
        if fm is None:
            continue
        rels.append({"path": path, "fm": fm})
    return rels


def audit_relationships(rels: list[dict[str, Any]], entity_ids: set[str]) -> dict[str, Any]:
    dangling: list[dict[str, str]] = []
    missing_desc: list[dict[str, str]] = []
    bad_type: list[dict[str, str]] = []
    duplicates: list[dict[str, str]] = []
    seen: set[tuple[str, str, str]] = set()

    for r in rels:
        fm = r["fm"]
        rel_type = fm.get("type", "")
        source_id = (fm.get("source") or {}).get("id", "")
        target_id = (fm.get("target") or {}).get("id", "")
        desc = fm.get("description", {}) or {}

        if source_id not in entity_ids or target_id not in entity_ids:
            dangling.append({"path": str(r["path"]), "source": source_id, "target": target_id})
        if not desc.get("zh") and not desc.get("en") and not desc.get("ko"):
            missing_desc.append({"path": str(r["path"]), "source": source_id, "target": target_id})
        if not rel_type:
            bad_type.append({"path": str(r["path"]), "source": source_id, "target": target_id})

        key = (source_id, rel_type, target_id)
        if key in seen:
            duplicates.append({"source": source_id, "target": target_id, "type": rel_type})
        seen.add(key)

    return {
        "total": len(rels),
        "dangling": dangling,
        "missing_description": missing_desc,
        "missing_type": bad_type,
        "duplicates": duplicates,
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Audit knowledge graph entry quality.")
    parser.add_argument("--min-chars-zh", type=int, default=None, help="Override default minimum Chinese body chars")
    parser.add_argument("--json-only", action="store_true", help="Only write JSON report")
    args = parser.parse_args(argv)

    if args.min_chars_zh is not None:
        global DEFAULT_MIN_CHARS
        DEFAULT_MIN_CHARS = args.min_chars_zh

    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")
    json_path = REPORT_DIR / f"quality_report_{timestamp}.json"
    md_path = REPORT_DIR / f"quality_report_{timestamp}.md"

    entries: list[dict[str, Any]] = []
    parse_errors: list[str] = []
    entity_ids: set[str] = set()

    for path in sorted(RESEARCH_DIR.rglob("*.md")):
        try:
            entry = load_entry(path)
        except Exception as exc:
            parse_errors.append(f"{path}: {exc}")
            continue
        if entry is None:
            parse_errors.append(f"{path}: no frontmatter")
            continue
        entity_ids.add(entry["fm"].get("$id", ""))
        entries.append(audit_entry(entry))

    rels = load_relationships()
    rel_audit = audit_relationships(rels, entity_ids)

    severity_counts = Counter(e["severity"] for e in entries)
    type_counts = Counter(e["type"] for e in entries)
    issue_counts = Counter()
    for e in entries:
        for issue in e["issues"]:
            issue_counts[issue.split("(")[0].strip()] += 1

    critical_entries = [e for e in entries if e["severity"] == "critical"]
    warning_entries = [e for e in entries if e["severity"] == "warning"]

    report = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "total_entries": len(entries),
        "severity_counts": dict(severity_counts),
        "type_counts": dict(type_counts),
        "issue_counts": dict(issue_counts),
        "critical_entries": sorted(critical_entries, key=lambda x: (x["type"], x["id"])),
        "warning_entries": sorted(warning_entries, key=lambda x: (x["type"], x["id"])),
        "relationships": rel_audit,
        "parse_errors": parse_errors,
    }

    json_path.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"JSON report: {json_path}")

    if not args.json_only:
        lines = [
            "# Knowledge Graph Quality Report\n",
            f"_Generated at {report['generated_at']}_\n",
            "## Summary\n",
            f"- Total entries: {report['total_entries']}",
            f"- Critical: {severity_counts.get('critical', 0)}",
            f"- Warning: {severity_counts.get('warning', 0)}",
            f"- OK: {severity_counts.get('ok', 0)}",
            f"- Parse errors: {len(parse_errors)}\n",
            "## Entries by Type\n",
            "| Type | Count |",
            "|------|-------|",
        ]
        for t, c in sorted(type_counts.items(), key=lambda x: -x[1]):
            lines.append(f"| {t} | {c} |")

        lines.extend(["", "## Issue Counts", ""])
        for issue, count in issue_counts.most_common():
            lines.append(f"- **{issue}**: {count}")

        lines.extend(["", "## Relationships", ""])
        lines.append(f"- Total: {rel_audit['total']}")
        lines.append(f"- Dangling: {len(rel_audit['dangling'])}")
        lines.append(f"- Missing description: {len(rel_audit['missing_description'])}")
        lines.append(f"- Missing type: {len(rel_audit['missing_type'])}")
        lines.append(f"- Duplicates: {len(rel_audit['duplicates'])}\n")

        lines.extend(["## Critical Entries (Sample)", ""])
        for e in critical_entries[:50]:
            lines.append(f"- `{e['id']}` ({e['type']}, {e['zh_chars']} zh chars): {', '.join(e['issues'])}")
        if len(critical_entries) > 50:
            lines.append(f"- ... and {len(critical_entries) - 50} more")

        md_path.write_text("\n".join(lines), encoding="utf-8")
        print(f"Markdown report: {md_path}")

    return 0 if severity_counts.get("critical", 0) == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
