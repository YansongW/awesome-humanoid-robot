#!/usr/bin/env python3
"""Regenerate the entities section of data/roadmap_mapping.yaml.

Scans wiki/docs/roadmap/*.md for /entry/<id>/ links, verifies each id exists
in research/, and binds it to the page's stage:

- stage pages           -> role core
- platform entities     -> role recommended/optional per explicit table below
- playbook-only links   -> role optional on the related stage

Stages/roles metadata at the top of the yaml file is preserved verbatim;
only the `entities:` mapping is rewritten. Idempotent.

Usage: python scripts/build_roadmap_mapping.py
"""
from __future__ import annotations

import re
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
MAPPING = ROOT / "data" / "roadmap_mapping.yaml"
ROADMAP_DIR = ROOT / "wiki" / "docs" / "roadmap"

PAGE_STAGE = {
    "stage-0-foundations.md": "stage-0-foundations",
    "stage-1-actuator.md": "stage-1-actuator",
    "stage-2-biped.md": "stage-2-biped",
    "stage-3-humanoid.md": "stage-3-humanoid",
}

PLAYBOOK_STAGE = {
    "actuator-selection.md": "stage-1-actuator",
    "compute-selection.md": "stage-2-biped",
    "sim-setup.md": "stage-2-biped",
    "sensor-selection.md": "stage-3-humanoid",
}

# Explicit role overrides: entity_id -> {stage: role}
PLATFORM_ROLES = {
    "ent_robot_system_toddlerbot": {"stage-2-biped": "recommended"},
    "ent_robot_system_berkeley_humanoid_lite": {"stage-2-biped": "recommended"},
    "ent_robot_system_upkie": {"stage-2-biped": "recommended"},
    "ent_robot_system_bruce": {"stage-2-biped": "optional"},
    "ent_robot_system_openloong": {"stage-2-biped": "optional", "stage-3-humanoid": "recommended"},
    "ent_robot_system_inmoov": {"stage-3-humanoid": "optional"},
    "ent_robot_system_poppy_humanoid": {"stage-3-humanoid": "optional"},
    "ent_robot_system_robotis_op3": {"stage-3-humanoid": "optional"},
    "ent_robot_system_thormang3": {"stage-3-humanoid": "optional"},
    "ent_robot_system_odri_bolt": {"stage-1-actuator": "recommended"},
}

LINK_RE = re.compile(r"/entry/(ent_[A-Za-z0-9_]+)/")


def existing_entity_ids() -> set[str]:
    ids = set()
    for p in ROOT.glob("research/**/*.md"):
        m = re.search(r"\$id:\s*(\S+)", p.read_text(encoding="utf-8")[:4000])
        if m:
            ids.add(m.group(1))
    return ids


def page_links(path: Path) -> list[str]:
    text = path.read_text(encoding="utf-8")
    return list(dict.fromkeys(LINK_RE.findall(text)))


HEADER = """# 0→1 路线图 ↔ 知识图谱绑定表
#
# 新增卡片绑定时只需在 entities 下追加条目，builder 会在对应卡片页渲染
# 路线图徽章（阶段 + 角色），并链接到 wiki/docs/roadmap/ 下的阶段页面。
# 该文件只做"绑定"，不修改任何卡片本身的内容。
# entities 区块由 scripts/build_roadmap_mapping.py 自动再生成，请勿手改。
version: 1

stages:
  stage-0-foundations:
    order: 0
    title:
      zh: 阶段 0 · 基础筑基
      en: Stage 0 · Foundations
      ko: 0단계 · 기초 다지기
    url: /wiki/roadmap/stage-0-foundations/
  stage-1-actuator:
    order: 1
    title:
      zh: 阶段 1 · 造一个关节
      en: Stage 1 · Build One Joint
      ko: 1단계 · 관절 하나 만들기
    url: /wiki/roadmap/stage-1-actuator/
  stage-2-biped:
    order: 2
    title:
      zh: 阶段 2 · 双足平台
      en: Stage 2 · Biped Platform
      ko: 2단계 · 이족 플랫폼
    url: /wiki/roadmap/stage-2-biped/
  stage-3-humanoid:
    order: 3
    title:
      zh: 阶段 3 · 完整人形
      en: Stage 3 · Full Humanoid
      ko: 3단계 · 완전한 휴로봇
    url: /wiki/roadmap/stage-3-humanoid/

roles:
  core:
    zh: 核心
    en: Core
    ko: 핵심
  recommended:
    zh: 推荐
    en: Recommended
    ko: 추천
  optional:
    zh: 拓展
    en: Optional
    ko: 선택

"""


def main() -> None:
    valid = existing_entity_ids()
    bindings: dict[str, dict[str, str]] = {}  # eid -> {stage: role}
    missing: set[str] = set()

    def bind(eid: str, stage: str, role: str) -> None:
        if eid not in valid:
            missing.add(eid)
            return
        cur = bindings.setdefault(eid, {})
        # core beats recommended beats optional
        rank = {"core": 3, "recommended": 2, "optional": 1}
        if stage not in cur or rank[role] > rank[cur[stage]]:
            cur[stage] = role

    for page, stage in PAGE_STAGE.items():
        path = ROADMAP_DIR / page
        if not path.exists():
            continue
        for eid in page_links(path):
            bind(eid, stage, "core")

    for page, stage in PLAYBOOK_STAGE.items():
        path = ROADMAP_DIR / "playbooks" / page
        if not path.exists():
            continue
        for eid in page_links(path):
            bind(eid, stage, "optional")

    for eid, stage_roles in PLATFORM_ROLES.items():
        for stage, role in stage_roles.items():
            bind(eid, stage, role)

    if missing:
        print("WARNING: linked ids not found in research/:", sorted(missing))

    entities = {
        eid: [{"stage": s, "role": r} for s, r in sorted(stages.items())]
        for eid, stages in sorted(bindings.items())
    }

    body = yaml.safe_dump({"entities": entities}, allow_unicode=True, sort_keys=False, width=120)
    MAPPING.write_text(HEADER + body, encoding="utf-8")
    total_bindings = sum(len(v) for v in entities.values())
    print(f"bound {len(entities)} entities with {total_bindings} stage bindings")
    return 1 if missing else 0


if __name__ == "__main__":
    import sys
    sys.exit(main())
