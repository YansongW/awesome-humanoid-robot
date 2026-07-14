#!/usr/bin/env python3
"""
Backfill shallow process entries (ent_process_p*) from the WBS V3 report.

Usage:
    python scripts/backfill_process_bodies.py
"""

import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).parent.parent
REPORT = ROOT / "docs" / "humanoid_full_development_workflow_v3.md"
RESEARCH = ROOT / "research" / "methods"


def parse_p_sections(text: str) -> dict[str, tuple[str, str]]:
    sections: dict[str, tuple[str, str]] = {}
    current = title = None
    buffer: list[str] = []
    for line in text.splitlines():
        m = re.match(r"^## (P\d+)\s+(.+)$", line)
        if m:
            if current:
                sections[current] = (title, "\n".join(buffer))
            current, title = m.groups()
            buffer = []
        else:
            buffer.append(line)
    if current:
        sections[current] = (title, "\n".join(buffer))
    return sections


def build_body(p: str, title: str, text: str) -> str:
    lines: list[str] = []
    lines.append("## 概述")
    lines.append(
        f"{title}是人形机器人产品开发全流程中的第 {p[1:]} 个阶段，"
        "在 WBS V3 中展开为若干三级子任务。"
    )
    lines.append("")
    lines.append(
        "该阶段覆盖输入梳理、方案设计、实施/原型、验证闭环与文档交付等完整工程动作，"
        "是确保下游依赖方获得合格输入的关键节点。"
    )
    lines.append("")

    sub_sections: list[tuple[str, str, str]] = []
    cur_code = cur_title = None
    cur_lines: list[str] = []
    for line in text.splitlines():
        m = re.match(r"^(#{2,4}) (P\d+(?:\.\d+)*)\s+(.+)$", line)
        if m:
            if cur_code:
                sub_sections.append((cur_code, cur_title, "\n".join(cur_lines)))
            cur_code = m.group(2)
            cur_title = m.group(3)
            cur_lines = []
        else:
            cur_lines.append(line)
    if cur_code:
        sub_sections.append((cur_code, cur_title, "\n".join(cur_lines)))

    if sub_sections:
        lines.append("## 关键子任务与技术内容")
        for code, sub_title, sub_text in sub_sections:
            depth = code.count(".")
            heading_level = min(3 + depth, 5)
            lines.append(f"{'#' * heading_level} {sub_title}")
            for sl in sub_text.splitlines():
                if sl.strip():
                    lines.append(sl.rstrip())
            lines.append("")

    lines.append("## 完成标准")
    lines.append("本阶段所有三级子任务均通过验收评审，关键输出物版本受控并正式交付给下游依赖方。")
    lines.append("")
    lines.append("## 参考")
    lines.append("- 《全尺寸双足人形机器人产品开发全流程报告（V3 / 三四级任务展开版）》")
    lines.append("")
    return "\n".join(lines)


def meaningful_body_chars(text: str) -> int:
    clean = re.sub(r"#+\s+", "", text)
    clean = re.sub(r"\s+", "", clean)
    return len(clean)


def main() -> int:
    section_map = parse_p_sections(REPORT.read_text(encoding="utf-8"))
    updated: list[str] = []

    for p_id, (title, sec_text) in section_map.items():
        # P0 and P7 already have richer bodies in the repo.
        if p_id in ("P0", "P7"):
            continue
        path = RESEARCH / f"ent_process_{p_id.lower()}.md"
        if not path.exists():
            continue

        text = path.read_text(encoding="utf-8")
        if not text.startswith("---"):
            continue
        parts = text.split("---", 2)
        if len(parts) < 3:
            continue
        fm = yaml.safe_load(parts[1])
        body = parts[2].strip()

        if meaningful_body_chars(body) > 300:
            print(f"  SKIP {p_id}: body already rich", file=sys.stderr)
            continue

        new_body = build_body(p_id, title, sec_text)

        name_zh = fm.get("names", {}).get("zh", "") if isinstance(fm.get("names"), dict) else ""
        summary_zh = fm.get("summary", {}).get("zh", "") if isinstance(fm.get("summary"), dict) else ""
        if not summary_zh or summary_zh == name_zh:
            fm.setdefault("summary", {})
            fm["summary"]["zh"] = (
                f"{title}——人形机器人产品开发全流程第 {p_id[1:]} 阶段，"
                "涵盖方案设计、实施验证与文档交付。"
            )

        fm["verification"] = fm.get("verification", {})
        fm["verification"]["notes"] = (
            "Body populated from docs/humanoid_full_development_workflow_v3.md "
            "by scripts/backfill_process_bodies.py."
        )
        fm["verification"]["reviewed_at"] = "2026-07-14"

        new_yaml = yaml.safe_dump(
            fm, allow_unicode=True, sort_keys=False, width=120, default_flow_style=False
        )
        path.write_text(f"---\n{new_yaml}---\n{new_body}\n", encoding="utf-8")
        updated.append(p_id)
        print(f"  UPDATED {p_id}")

    print(f"\nUpdated {len(updated)} process entries: {updated}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
