#!/usr/bin/env python3
"""Expand the humanoid WBS to level-3 and level-4 tasks."""

from __future__ import annotations

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from generate_humanoid_wbs import WBS


def _l4_checklist(subtask_name: str) -> list[str]:
    """Generate generic level-4 key actions for a subtask."""
    name = subtask_name
    if "输入" in name or "梳理" in name or "目标" in name:
        return [
            "列出所有上游输入清单并确认版本",
            "将验收标准转化为可量化 KPI",
            "建立任务 Owner、时间节点与风险登记",
        ]
    if "方案" in name or "选型" in name or "设计" in name:
        return [
            "形成不少于 2 个候选方案",
            "建立评估矩阵并量化打分",
            "组织评审并冻结方案",
        ]
    if "建模" in name or "仿真" in name or "原型" in name or "实现" in name:
        return [
            "建立模型/样机并记录关键参数",
            "执行仿真或原型验证",
            "记录异常与偏差",
        ]
    if "测试" in name or "验证" in name or "评审" in name:
        return [
            "制定测试/评审计划与通过准则",
            "执行测试并记录原始数据",
            "输出问题清单与改进措施",
        ]
    if "文档" in name or "报告" in name or "交付" in name:
        return [
            "按模板编写文档并引用原始数据",
            "完成内部评审与版本控制",
            "发布并通知下游依赖方",
        ]
    if "优化" in name or "迭代" in name:
        return [
            "分析上一轮偏差根因",
            "实施设计/参数/工艺改进",
            "重新验证并对比改进前后指标",
        ]
    return [
        "明确本步骤的输入、方法与输出",
        "执行并记录关键数据",
        "与上游/下游确认接口一致性",
    ]


def expand_task(task: dict) -> dict:
    """Add level-3 subtasks and level-4 key actions to a task."""
    name = task["name"]
    method = task.get("method", "")
    expanded = dict(task)
    subtasks: list[dict] = []

    def add(suffix: str, sub_name: str, detail: str) -> None:
        sub_id = f"{task['id']}.{suffix}"
        subtasks.append({
            "id": sub_id,
            "name": sub_name,
            "detail": detail,
            "level4": _l4_checklist(sub_name),
        })

    # Use keywords to pick more specific subtask names.
    has_sim = any(k in method for k in ("仿真", "FEA", "CFD", "热网络", "建模"))
    has_select = any(k in name for k in ("选型", "选择"))
    has_design = any(k in name for k in ("设计", "Design"))
    has_test = any(k in name for k in ("测试", "验证", "试验", "评审"))
    has_algo = any(k in name for k in ("算法", "控制", "规划", "估计", "VLA", "WAM", "WBC", "MPC"))
    has_integrate = any(k in name for k in ("集成", "联调", "闭环"))
    has_doc = any(k in name for k in ("文档", "报告", "手册", "SOP"))

    # 1. Input / target
    add("1", "输入梳理与目标量化",
        f"整理「{name}」所需的上游输入、参考标准与资源，将完成标准转化为可量化的验收指标，并明确 Owner 与里程碑。")

    # 2. Scheme / selection / design / algorithm
    if has_algo:
        add("2", "算法/控制方案设计",
            f"基于「{method}」建立数学模型或算法框架，形成候选方案，评估稳定性、实时性与可扩展性，并冻结实现路径。")
    elif has_select:
        add("2", "候选方案建立与评估",
            f"针对「{name}」建立候选方案库，使用「{method}」进行量化评估，考虑成本、性能、供应链、可维护性后确定最终方案。")
    elif has_design:
        add("2", "概念与详细设计",
            f"完成「{name}」的概念设计、详细设计与接口定义，使用「{method}」验证可行性，输出图纸/算法/逻辑框架。")
    elif has_integrate:
        add("2", "接口与集成策略设计",
            f"梳理「{name}」涉及的子系统接口、数据流与时序，制定集成顺序、回退策略与异常处理机制。")
    else:
        add("2", "方案/方法设计",
            f"针对「{name}」制定实施方法或候选方案，使用「{method}」进行论证，明确技术路线与资源需求。")

    # 3. Model / simulation / prototype / implementation
    if has_sim:
        add("3", "建模/仿真与样机实现",
            f"建立「{name}」的仿真/数学模型或原型样机，使用「{method}」执行计算或实验，记录关键参数与边界条件。")
    elif has_algo:
        add("3", "算法实现与仿真验证",
            f"将「{name}」的算法在仿真环境或离线数据中实现，验证功能正确性、实时性与鲁棒性。")
    elif has_doc:
        add("3", "内容编写与内部评审",
            f"按模板完成「{name}」主体内容编写，引用原始数据与结论，组织评审并修订。")
    else:
        add("3", "实施/原型/样件制作",
            f"根据设计方案执行「{name}」的实施工作，制作原型、样件或完成关键步骤，记录过程数据。")

    # 4. Test / verification / optimization
    if has_test:
        add("4", "测试执行与结果分析",
            f"按照验收标准执行「{name}」测试，统计通过率/误差/偏差，进行根因分析并形成改进清单。")
    elif has_sim:
        add("4", "仿真结果校核与优化",
            f"校核「{name}」仿真结果与理论/试验数据的一致性，识别薄弱点并迭代优化。")
    elif has_algo:
        add("4", "算法调参与性能验证",
            f"对「{name}」算法进行参数调优与边界测试，验证在典型/极端工况下的性能是否满足指标。")
    else:
        add("4", "验证与问题闭环",
            f"对「{name}」输出进行验证，检查是否满足完成标准，记录问题并跟踪至关闭。")

    # 5. Documentation / handoff
    add("5", "文档输出与下游交付",
        f"输出「{name}」最终报告/图纸/规范，更新 ICD/BOM/SOP/需求追溯链，完成向下游环节的正式交付。")

    expanded["subtasks"] = subtasks
    return expanded


def expand_all(wbs: list[dict]) -> list[dict]:
    result = []
    for phase in wbs:
        p2 = dict(phase)
        p2["packages"] = []
        for pkg in phase["packages"]:
            p3 = dict(pkg)
            p3["tasks"] = [expand_task(t) for t in pkg["tasks"]]
            p2["packages"].append(p3)
        result.append(p2)
    return result


def main() -> None:
    expanded = expand_all(WBS)
    output = Path("data/humanoid_wbs_expanded.json")
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(expanded, ensure_ascii=False, indent=2), encoding="utf-8")

    # Print stats.
    phases = len(expanded)
    packages = sum(len(p["packages"]) for p in expanded)
    tasks = sum(len(pkg["tasks"]) for p in expanded for pkg in p["packages"])
    subtasks = sum(
        len(t["subtasks"]) for p in expanded for pkg in p["packages"] for t in pkg["tasks"]
    )
    print(f"Expanded WBS: {phases} phases, {packages} packages, {tasks} tasks, {subtasks} subtasks")
    print(f"Wrote {output}")


if __name__ == "__main__":
    main()
