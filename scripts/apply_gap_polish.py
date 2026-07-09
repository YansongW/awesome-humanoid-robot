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
    names = curated["names"]
    summary = curated["summary"]

    title_parts = [names.get("en", "")]
    if names.get("zh"):
        title_parts.append(names["zh"])
    if names.get("ko"):
        title_parts.append(names["ko"])
    title = " / ".join(filter(None, title_parts))

    lines = [f"# {title}", ""]

    if summary.get("zh"):
        lines.extend(["## 摘要", "", summary["zh"], ""])
    if summary.get("en"):
        lines.extend(["## Abstract", "", summary["en"], ""])
    if summary.get("ko"):
        lines.extend(["## 요약", "", summary["ko"], ""])

    # Reference to Wiki chapter.
    chapter = curated.get("chapter")
    if chapter:
        lines.extend(
            ["", f"> 本词条对应 Wiki 第 {chapter} 章，详细论述见项目 Wiki。", ""]
        )

    return "\n".join(lines) + "\n"


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
