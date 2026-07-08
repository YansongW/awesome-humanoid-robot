#!/usr/bin/env python3
"""Render the expanded WBS JSON to markdown."""

from __future__ import annotations

import json
from pathlib import Path


def render_l4(actions: list[str]) -> str:
    if not actions:
        return ""
    lines = ["\n**四级关键动作：**\n"]
    for i, a in enumerate(actions, 1):
        lines.append(f"{i}. {a}")
    return "\n".join(lines) + "\n"


def render_subtask(sub: dict) -> str:
    return (
        f"- **{sub['id']} {sub['name']}**：{sub['detail']}"
        f"{render_l4(sub.get('level4', []))}"
    )


def render_task(task: dict) -> str:
    lines = [
        f"#### {task['id']} {task['name']}\n",
        f"- **方法 / 工具**：{task['method']}",
        f"- **设计思考逻辑**：{task['logic']}",
        f"- **关键约束**：{task['constraints']}",
        f"- **完成标准 / 输出物**：{task['criteria']}\n",
        "**三级子任务：**\n",
    ]
    for sub in task.get("subtasks", []):
        lines.append(render_subtask(sub))
    return "\n".join(lines) + "\n"


def render_package(pkg: dict) -> str:
    lines = [f"### {pkg['id']} {pkg['name']}\n"]
    for task in pkg["tasks"]:
        lines.append(render_task(task))
    return "".join(lines)


def render_phase(phase: dict) -> str:
    lines = [f"## {phase['id']} {phase['name']}\n"]
    for pkg in phase["packages"]:
        lines.append(render_package(pkg))
    return "".join(lines)


def main() -> None:
    data = json.loads(Path("data/humanoid_wbs_expanded.json").read_text(encoding="utf-8"))
    phases = len(data)
    packages = sum(len(p["packages"]) for p in data)
    tasks = sum(len(pkg["tasks"]) for p in data for pkg in p["packages"])
    subtasks = sum(
        len(t["subtasks"]) for p in data for pkg in p["packages"] for t in pkg["tasks"]
    )

    flowchart = """```mermaid
flowchart TD
    P0[0. 项目立项与商业基线] --> P1[1. 需求定义与系统方案]
    P1 --> P2[2. 工业设计与外观工程]
    P2 --> P3[3. 系统架构与机电总体设计]
    P3 --> P4[4. 关节模组与驱动系统]
    P3 --> P5[5. 本体结构工程与原型]
    P4 --> P5
    P5 --> P6[6. URDF建模与运动学校核]
    P5 --> P7[7. 仿真平台搭建与验证]
    P6 --> P7
    P5 --> P8[8. 结构强度仿真与迭代]
    P5 --> P9[9. 热管理仿真与迭代]
    P4 --> P9
    P7 --> P10[10. 运动控制算法开发与验证]
    P4 --> P10
    P3 --> P11[11. 灵巧手选型/设计与集成]
    P11 --> P10
    P7 --> P12[12. VLA/WAM/AI算法集成]
    P10 --> P12
    P3 --> P13[13. 电子电气与能源系统]
    P13 --> P9
    P10 --> P14[14. 软件中间件与系统集成]
    P12 --> P14
    P13 --> P14
    P8 --> P15[15. 整机集成与验证测试]
    P9 --> P15
    P10 --> P15
    P11 --> P15
    P14 --> P15
    P15 --> P16[16. 小批量试产与量产准备]
```
"""

    dependency_table = """| 阶段 | 关键前置依赖 | 说明 |
|---|---|---|
| P1 需求 | P0 立项 | 商业与法规基线决定需求边界 |
| P2 ID | P1 需求 | 外观服务于产品定位与指标 |
| P3 系统架构 | P1、P2 | 在ID与结构接口冻结后定义内部布局 |
| P4 关节 | P3 | DOF与动力学需求决定关节规格 |
| P5 结构 | P2、P3、P4 | 结构需包裹关节与外观 |
| P6 URDF | P5 | 结构CAD是URDF几何/惯量来源 |
| P7 仿真 | P6、P10 | 仿真需URDF与控制器共同驱动 |
| P8 结构FEA | P5、P3 | 结构几何与载荷决定仿真输入 |
| P9 热管理 | P4、P5、P13 | 热源来自关节、驱动器、电池、计算平台 |
| P10 控制 | P4、P6、P7 | 控制依赖硬件、模型与仿真验证 |
| P11 灵巧手 | P3、P10 | 手部DOF与手臂控制协同 |
| P12 AI/VLA | P7、P10、P11 | AI算法需仿真/实物平台与感知/控制基座 |
| P13 电子电气 | P3、P4 | 电气架构由系统与关节驱动方案决定 |
| P14 软件 | P10、P12、P13 | 中间件连接控制、AI、硬件 |
| P15 整机测试 | P8、P9、P10、P11、P14 | 所有子系统就绪后才能整机验证 |
| P16 试产 | P15 | 整机验证通过是试产前提 |
"""

    parts = [
        "# 全尺寸双足人形机器人产品开发全流程报告（V3 / 三四级任务展开版）\n\n"
        "> 本报告在 V2 工程级 WBS 基础上，将每个二级任务进一步展开为三级子任务与四级关键动作，可直接用于项目计划、排期与责任分配。\n\n"
        f"**统计**：{phases} 个阶段，{packages} 个工作包，{tasks} 个二级任务，{subtasks} 个三级子任务。\n\n",
        "## 0. 总体流程图\n\n" + flowchart + "\n",
        "## 0.1 阶段间关键依赖矩阵\n\n" + dependency_table + "\n",
    ]
    for phase in data:
        parts.append(render_phase(phase))

    output = Path("docs/humanoid_full_development_workflow_v3.md")
    output.write_text("".join(parts), encoding="utf-8")
    print(f"Wrote {output}")


if __name__ == "__main__":
    main()
