#!/usr/bin/env python3
"""
Apply curated names/summaries to Wiki gap entities.

Reads data/gap-entity-polish.yaml and updates the corresponding
research/ entity Markdown files in place.

Rules:
  - Replace names and summary frontmatter with curated multilingual values.
  - Rewrite placeholder body text that matches "...是人形机器人产业链中的...相关知识节点。详见Wiki第N章...".
  - Bump verification to partially_verified / human_and_ai / high, reviewed_at today.
  - Preserve all other frontmatter fields and non-placeholder body content.
"""

import re
import sys
from datetime import date
from pathlib import Path
from typing import List, Optional
from typing import Optional

import yaml

ROOT = Path(__file__).parent.parent
POLISH_PATH = ROOT / "data" / "gap-entity-polish.yaml"
MAPPING_PATH = ROOT / "data" / "wiki-chapter-mapping.yaml"

PLACEHOLDER_ZH = re.compile(
    r"^(.+?)是人形机器人产业链中的\w+相关知识节点。详见Wiki第\d+章《[^》]+》。$"
)
PLACEHOLDER_EN = re.compile(
    r"^(.+?) is a knowledge node related to \w+ in the humanoid robot value chain\. See Wiki Chapter \d+\.$"
)
WIKI_REFERENCE_NOTE = re.compile(
    r"\n?> ?本词条对应 Wiki 第 \d+ 章，详细论述见项目 Wiki。\n?",
    re.MULTILINE,
)
SUMMARY_HEADINGS = re.compile(
    r"^#{1,6}\s+(摘要|Abstract|요약|概述|Overview|개요)\s*$",
    re.MULTILINE | re.IGNORECASE,
)


def load_polish():
    with POLISH_PATH.open("r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def load_mapping():
    with MAPPING_PATH.open("r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def find_entity_path(eid: str) -> Optional[Path]:
    matches = list((ROOT / "research").rglob(f"{eid}.md"))
    return matches[0] if matches else None


def split_frontmatter(text: str) -> tuple[str, str, str]:
    """Return (prefix, yaml_text, body)."""
    if not text.startswith("---"):
        raise ValueError("File must start with YAML frontmatter")
    _, rest = text.split("---", 1)
    yaml_text, body = rest.split("---", 1)
    return "---", yaml_text, body


def build_clean_body(fm: dict, curated: dict) -> str:
    """Return an empty body for previously-placeholder gap entities.

    The entry template already renders entry.summary in its own section, so the
    body should only contain additional content beyond the summary. Until we
    expand each gap entity with richer Wiki-derived content, leave the body blank
    rather than duplicating the summary or falling back to "see Wiki".
    """
    return ""


def body_is_placeholder(body: str) -> bool:
    stripped = body.strip()
    if not stripped:
        return True
    # Drop the title line and check remaining paragraphs.
    lines = [ln.strip() for ln in stripped.splitlines() if ln.strip()]
    if len(lines) <= 1:
        return True
    content = "\n".join(lines[1:])
    return bool(PLACEHOLDER_ZH.search(content) or PLACEHOLDER_EN.search(content))


def body_is_summary_only(body: str) -> bool:
    """Return True if the body only contains a title and summary sections.

    A summary-only body has only headings that match 摘要/Abstract/요약/etc.,
    plus their content and an optional initial level-1 title.
    """
    stripped = body.strip()
    if not stripped:
        return True
    lines = stripped.splitlines()

    # Parse sections by headings.
    sections: list[tuple[Optional[str], list[str]]] = []
    current_heading: Optional[str] = None
    current_lines: list[str] = []

    for line in lines:
        if re.match(r"^#{1,6}\s+", line):
            if current_heading is not None or current_lines:
                sections.append((current_heading, current_lines))
            current_heading = line.strip()
            current_lines = []
        else:
            current_lines.append(line)
    if current_heading is not None or current_lines:
        sections.append((current_heading, current_lines))

    if not sections:
        return True

    # Allow an initial level-1 title section.
    if sections[0][0] and sections[0][0].startswith("# "):
        sections = sections[1:]

    if not sections:
        return True

    for heading, _ in sections:
        if heading is None or not SUMMARY_HEADINGS.match(heading):
            return False
    return True


def update_frontmatter(fm: dict, curated: dict) -> dict:
    fm["names"] = {k: v for k, v in curated["names"].items() if v}
    fm["summary"] = {k: v for k, v in curated["summary"].items() if v}

    verification = fm.get("verification", {})
    verification["status"] = "partially_verified"
    verification["reviewed_by"] = "human_and_ai"
    verification["reviewed_at"] = date.today().isoformat()
    verification["confidence"] = "high"
    verification["notes"] = (
        "Curated names and summary from data/gap-entity-polish.yaml; "
        "placeholder body rewritten. Pending domain-expert final review."
    )
    fm["verification"] = verification

    # Ensure tags include gap_entity marker if not present.
    tags = fm.get("tags", [])
    if "wiki_gap" not in tags:
        tags.append("wiki_gap")
    fm["tags"] = tags

    return fm


def process_entity(eid: str, curated: dict) -> bool:
    path = find_entity_path(eid)
    if path is None:
        print(f"  SKIP: {eid} file not found", file=sys.stderr)
        return False

    text = path.read_text(encoding="utf-8")
    prefix, yaml_text, body = split_frontmatter(text)
    fm = yaml.safe_load(yaml_text)

    fm = update_frontmatter(fm, curated)

    if body_is_placeholder(body):
        new_body = build_clean_body(fm, curated)
    else:
        # Keep existing body but remove any remaining placeholder paragraph.
        new_body = re.sub(PLACEHOLDER_ZH, "", body)
        new_body = re.sub(PLACEHOLDER_EN, "", new_body)
        new_body = re.sub(WIKI_REFERENCE_NOTE, "", new_body)

    # If the body is now only a title + summary headings, clear it: the entry
    # template already renders entry.summary in its own section, so duplicating
    # it in the body produces two consecutive summary blocks.
    if body_is_summary_only(new_body):
        new_body = ""

    # Re-serialize frontmatter with nice formatting.
    new_yaml = yaml.safe_dump(
        fm,
        allow_unicode=True,
        sort_keys=False,
        width=120,
        default_flow_style=False,
    )
    new_text = f"{prefix}\n{new_yaml}{prefix}\n{new_body}"

    path.write_text(new_text, encoding="utf-8")
    return True


def main() -> int:
    polish = load_polish()
    mapping = load_mapping()

    # Build chapter lookup for polish metadata.
    chapter_lookup = {}
    for ch in mapping["chapters"]:
        for g in ch.get("gaps", []):
            chapter_lookup[g["id"]] = ch["number"]

    entities = polish["entities"]
    ok = 0
    skipped = 0
    for eid, curated in entities.items():
        curated["chapter"] = chapter_lookup.get(eid)
        if process_entity(eid, curated):
            ok += 1
            print(f"  OK: {eid}")
        else:
            skipped += 1

    print(f"\nUpdated {ok} entity files, skipped {skipped}.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
