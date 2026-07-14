---
$id: ent_robot_system_tesla_optimus
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: robot_system
names:
  en: Tesla Optimus
  zh: Tesla Optimus
  ko: 테슬라 옵티머스
summary:
  en: Tesla's general-purpose humanoid robot program, with stated goals of factory deployment and high-volume manufacturing.
  zh: 特斯拉的通用人形机器人项目，目标是工厂部署和规模化制造。
  ko: 테슬라의 범용 휴인oid 로봇 프로그램으로, 공장 배치와 대량 생산을 목표로 합니다.
domains:
- 05_mass_production
- 06_design_engineering
- 11_applications_markets
layers:
- midstream
- validation_markets
functional_roles:
- system
- knowledge
tags:
- tesla
- optimus
- humanoid
- robot_system
- factory
- manufacturing
verification:
  status: partially_verified
  reviewed_by: human_and_ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Body backfilled from chapter-08.md#8.9.3 Tesla Optimus：面向制造的成本导向设计 by scripts/backfill_nonpaper_entries.py.
sources:
- id: src_001
  type: website
  title: Tesla Optimus Official Page
  url: https://www.tesla.com/optimus
  date: '2026'
  accessed_at: '2026-06-24'
- id: src_002
  type: report
  title: Interact Analysis — Humanoid Robots and Lithium-Ion Batteries
  url: https://interactanalysis.com/insight/humanoid-robots-and-lithium-ion-batteries/
  date: '2026'
  accessed_at: '2026-06-24'
theoretical_depth:
- system
---
## 概述
Tesla Optimus是人形机器人领域的重要robot_system。以下内容整理自项目 Wiki，供深入查阅。

## 核心内容
Tesla Optimus 的设计目标是在汽车制造等场景中替代或辅助人类劳动，因此强调成本、产量与可维护性[17][18]。

!!! note "术语解释：Optimus、成本导向设计、规模化、制造场景"
    - **Optimus**：Tesla 开发的人形机器人。
    - **成本导向设计（cost-driven design）**：以降低成本为核心目标的设计决策。
    - **规模化（scalability）**：设计支持从小批量到大批量的扩展。
    - **制造场景（manufacturing scenario）**：工厂、仓储等重复性劳动环境。

Optimus 公开设计特点（公开资料）：
- 身高约 173 cm，质量约 63 kg。
- 采用 Tesla 自研执行器与控制器。
- 强调零件数量少、制造工艺简单、易于自动化装配。
- 视觉感知基于 Tesla 自动驾驶技术迁移。
- 目标低成本大规模生产。

```mermaid
flowchart TD
    A["Tesla Optimus"] --> B["自研执行器"]
    A --> C["少零件/易装配"]
    A --> D["视觉感知复用"]
    A --> E["汽车供应链协同"]
    B --> F["降本"]
    C --> F
    D --> G["快速迭代"]
    E --> H["规模化"]
```

## 参考
- [Tesla Optimus Official Page](https://www.tesla.com/optimus)
- [Interact Analysis — Humanoid Robots and Lithium-Ion Batteries](https://interactanalysis.com/insight/humanoid-robots-and-lithium-ion-batteries/)
- 项目 Wiki：chapter-08.md#8.9.3 Tesla Optimus：面向制造的成本导向设计

