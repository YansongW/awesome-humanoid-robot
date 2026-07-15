---
$id: ent_robot_boston_dynamics_atlas_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: robot_system
names:
  en: Boston Dynamics Atlas
  zh: 波士顿动力 Atlas
  ko: Boston Dynamics Atlas
summary:
  en: High-performance humanoid robot; latest generation uses all-electric actuation for dynamic athletic tasks.
  zh: '## 概述 波士顿动力 Atlas是人形机器人领域的重要robot_system。以下内容整理自项目 Wiki，供深入查阅。'
  ko: 고성능 휨로봇, 최신 세대는 동적 운 동 작업을 위한 전기식 액추에이션 사용.
domains:
- 06_design_engineering
- 02_components
layers:
- midstream
- upstream
functional_roles:
- knowledge
- intelligence
tags:
- athletic
- boston_dynamics
- electric_actuation
- humanoid
- robot_system
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Body backfilled from chapter-08.md#8.9.2 Boston Dynamics Atlas：液压驱动到电动驱动 by scripts/backfill_nonpaper_entries.py.
sources:
- id: src_001
  type: website
  title: Boston Dynamics Atlas
  url: https://bostondynamics.com/atlas
  date: '2024'
  accessed_at: '2026-07-01'
---

## 概述
波士顿动力 Atlas是人形机器人领域的重要robot_system。以下内容整理自项目 Wiki，供深入查阅。

## 核心内容
Boston Dynamics Atlas 以高动态运动著称。早期版本采用液压驱动，能够奔跑、跳跃、后空翻；2024 年发布的全新 Atlas 转向全电驱动，强调可维护性与商业化前景[35]。

!!! note "术语解释：液压驱动、电动驱动、高动态运动、后空翻、可维护性"
    - **液压驱动（hydraulic actuation）**：利用高压液体传递动力的驱动方式。
    - **电动驱动（electric actuation）**：利用电机与减速器传递动力的驱动方式。
    - **高动态运动（highly dynamic motion）**：快速、大加速度、高冲击的运动。
    - **后空翻（backflip）**：空中向后翻转的动作，展示高功率与控制能力。
    - **可维护性（maintainability）**：系统易于维修和保养的程度。

液压 Atlas 的优势在于高功率密度与抗冲击能力，但存在噪音、油液泄漏、维护复杂等问题。电动 Atlas 通过高扭矩密度电机与先进控制，试图在保持性能的同时降低运行与维护成本。

```mermaid
flowchart TD
    A["Atlas 液压版"] --> B["高功率密度"]
    A --> C["高动态运动"]
    A --> D["噪音/泄漏/维护复杂"]
    B --> E["奔跑/跳跃/后空翻"]
    C --> E
    D --> F["电动化动机"]
    G["Atlas 电动版"] --> H["安静/清洁/易维护"]
    G --> I["性能保留"]
    F --> G
```

## 参考
- [Boston Dynamics Atlas](https://bostondynamics.com/atlas)
- 项目 Wiki：chapter-08.md#8.9.2 Boston Dynamics Atlas：液压驱动到电动驱动


