#!/usr/bin/env python3
"""Promote the expanded humanoid WBS into the knowledge graph."""

from __future__ import annotations

import json
from datetime import date
from pathlib import Path

sys_path_inserted = False
if __name__ == "__main__":
    import sys
    sys.path.insert(0, str(Path(__file__).parent))
    sys_path_inserted = True

from ai4sci_lib import config, entry_builder


TODAY = date.today().isoformat()

PHASE_DOMAINS = {
    "P0": ["11_applications_markets", "12_policy_regulation_ethics"],
    "P1": ["06_design_engineering", "12_policy_regulation_ethics"],
    "P2": ["06_design_engineering"],
    "P3": ["06_design_engineering", "02_components"],
    "P4": ["02_components", "06_design_engineering"],
    "P5": ["06_design_engineering", "03_manufacturing_processes"],
    "P6": ["06_design_engineering", "08_software_middleware"],
    "P7": ["08_software_middleware", "10_evaluation_benchmarks"],
    "P8": ["06_design_engineering", "03_manufacturing_processes"],
    "P9": ["06_design_engineering"],
    "P10": ["07_ai_models_algorithms", "06_design_engineering"],
    "P11": ["02_components", "06_design_engineering"],
    "P12": ["07_ai_models_algorithms"],
    "P13": ["02_components", "08_software_middleware"],
    "P14": ["08_software_middleware"],
    "P15": ["04_assembly_integration_testing", "10_evaluation_benchmarks"],
    "P16": ["05_mass_production", "11_applications_markets"],
}

PHASE_DEPS = {
    "P1": ["P0"],
    "P2": ["P1"],
    "P3": ["P1", "P2"],
    "P4": ["P3"],
    "P5": ["P2", "P3", "P4"],
    "P6": ["P5"],
    "P7": ["P6", "P10"],
    "P8": ["P5", "P3"],
    "P9": ["P4", "P5", "P13"],
    "P10": ["P4", "P6", "P7"],
    "P11": ["P3", "P10"],
    "P12": ["P7", "P10", "P11"],
    "P13": ["P3", "P4"],
    "P14": ["P10", "P12", "P13"],
    "P15": ["P8", "P9", "P10", "P11", "P14"],
    "P16": ["P15"],
}

SOURCE = {
    "id": "wbs_v3_report",
    "type": "report",
    "title": "全尺寸双足人形机器人产品开发全流程报告（V3 / 三四级任务展开版）",
    "date": TODAY,
}


def layers_for(domains: list[str]) -> list[str]:
    return sorted({config.LAYER_MAP[d] for d in domains if d in config.LAYER_MAP}) or ["midstream"]


def make_body(entry_type: str, obj: dict, parent_name: str = "") -> str:
    lines = []
    if parent_name:
        lines.append(f"**所属阶段/工作包**：{parent_name}\n")
    if "method" in obj:
        lines.append(f"**方法 / 工具**：{obj['method']}\n")
    if "logic" in obj:
        lines.append(f"**设计思考逻辑**：{obj['logic']}\n")
    if "constraints" in obj:
        lines.append(f"**关键约束**：{obj['constraints']}\n")
    if "criteria" in obj:
        lines.append(f"**完成标准 / 输出物**：{obj['criteria']}\n")
    subs = obj.get("subtasks")
    if subs:
        lines.append("**三级子任务与四级关键动作：**\n")
        for sub in subs:
            lines.append(f"- {sub['id']} {sub['name']}")
            lines.append(f"  - {sub['detail']}")
            for a in sub.get("level4", []):
                lines.append(f"    - {a}")
            lines.append("")
    return "\n".join(lines).strip()


def create_entry(obj: dict, entity_id: str, entry_type: str, domains: list[str], depth: list[str], parent_name: str = "") -> str:
    name = obj["name"]
    summary = obj.get("criteria") or obj.get("detail", name)
    frontmatter = entry_builder.build_entry_frontmatter({
        "$id": entity_id,
        "type": entry_type,
        "names": {"en": f"{obj['id']} {name}", "zh": name, "ko": ""},
        "summary": {"en": summary, "zh": summary, "ko": ""},
        "domains": domains,
        "layers": layers_for(domains),
        "functional_roles": ["process", "knowledge"],
        "theoretical_depth": depth,
        "verification": {
            "status": "verified",
            "reviewed_by": "human_and_ai",
            "reviewed_at": TODAY,
            "confidence": "high",
            "notes": "Derived from docs/humanoid_full_development_workflow_v3.md",
        },
        "sources": [SOURCE],
    })
    body = make_body(entry_type, obj, parent_name)
    subdir = entry_builder.infer_subdir(entry_type)
    filename = f"{entity_id}.md"
    entry_builder.write_entry_file(frontmatter, body, subdir, filename)
    return entity_id


def _name(entity_id: str) -> dict:
    return {"en": entity_id, "zh": entity_id, "ko": ""}


def create_relationship(source_id: str, rel_type: str, target_id: str, description: str) -> None:
    rel_id = entry_builder.make_relationship_id(source_id, rel_type, target_id)
    frontmatter = entry_builder.build_relationship_frontmatter({
        "$id": rel_id,
        "type": rel_type,
        "source": {"id": source_id, "name": _name(source_id)},
        "target": {"id": target_id, "name": _name(target_id)},
        "description": {"en": description, "zh": description, "ko": ""},
        "verification": {
            "status": "verified",
            "reviewed_by": "human_and_ai",
            "reviewed_at": TODAY,
            "confidence": "high",
        },
        "sources": [SOURCE],
    })
    entry_builder.write_relationship_file(frontmatter)


def main() -> None:
    data = json.loads(Path("data/humanoid_wbs_expanded.json").read_text(encoding="utf-8"))
    existing = entry_builder.load_existing_ids()

    created_entries = []

    for phase in data:
        phase_id_short = phase["id"]
        phase_entity_id = f"ent_process_{phase_id_short.lower()}"
        domains = PHASE_DOMAINS.get(phase_id_short, ["06_design_engineering"])
        if phase_entity_id in existing:
            print(f"Skip existing {phase_entity_id}")
        else:
            create_entry(phase, phase_entity_id, "method", domains, ["system"])
            created_entries.append(phase_entity_id)

        for pkg in phase["packages"]:
            for task in pkg["tasks"]:
                task_entity_id = f"ent_process_{task['id'].replace('.', '_').lower()}"
                if task_entity_id in existing:
                    print(f"Skip existing {task_entity_id}")
                    continue
                create_entry(task, task_entity_id, "method", domains, ["method"], parent_name=phase["name"])
                created_entries.append(task_entity_id)

                # is_part_of relationship to phase
                create_relationship(
                    task_entity_id,
                    "is_part_of",
                    phase_entity_id,
                    f"任务 {task['id']} {task['name']} 是 {phase['name']} 的组成部分",
                )

    # Phase dependencies
    for target, sources in PHASE_DEPS.items():
        target_id = f"ent_process_{target.lower()}"
        for src in sources:
            source_id = f"ent_process_{src.lower()}"
            create_relationship(
                target_id,
                "requires",
                source_id,
                f"{target} 依赖 {src} 完成后才能启动",
            )

    print(f"Created {len(created_entries)} new entries")


if __name__ == "__main__":
    main()
