---
$id: ent_concept_digital_twin
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: concept
names:
  en: Digital Twin
  zh: 数字孪生
  ko: 디지털 트윈
summary:
  en: A virtual replica of a physical asset or process that is continuously synchronized with real-world data for monitoring,
    simulation, and optimization.
  zh: 数字孪生（digital twin）是物理实体在数字空间的实时映射，可用于设计验证、虚拟调试、健康监测与预测性维护。
  ko: 물리 자산이나 프로세스의 실시간 데이터와 지속적으로 동기화되는 가상 복제체로, 모니터링·시뮬레이션·최적화에 활용.
domains:
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
tags:
- concept
- chapter_23
- wiki_gap
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: human_and_ai
  reviewed_at: '2026-07-14'
  confidence: high
  notes: Body backfilled from chapter-08.md#8.8.3 数字孪生：从虚拟样机到在线映射 by scripts/backfill_nonpaper_entries.py.
sources:
- id: src_wiki_extraction
  type: other
  title: Wiki extraction
  date: '2026-07-09'
  accessed_at: '2026-07-09'
---

## 概述
数字孪生是人形机器人领域的重要概念。以下内容整理自项目 Wiki，供深入查阅。

## 核心内容
**数字孪生（digital twin）**是物理实体在数字空间的实时映射，可用于设计验证、虚拟调试、健康监测与预测性维护。

!!! note "术语解释：数字孪生、虚拟样机、虚拟调试、预测性维护、在线映射"
    - **数字孪生（digital twin）**：物理系统的高保真数字映射，可实时同步状态。
    - **虚拟样机（virtual prototype）**：在软件中构建的产品模型，用于仿真验证。
    - **虚拟调试（virtual commissioning）**：在虚拟环境中验证控制逻辑与软件。
    - **预测性维护（predictive maintenance）**：基于状态监测预测故障并提前维护。
    - **在线映射（online mapping）**：物理状态实时反馈到数字模型的过程。

人形机器人数字孪生工作流通常包括：

1. **高保真模型**：CAD/CAE 模型 + 多体动力学 + 传感器模型。
2. **仿真平台**：Isaac Sim、Gazebo、MuJoCo、Webots 等。
3. **数据接口**：ROS 2、DDS、EtherCAT 等实现虚实数据同步。
4. **在线标定**：通过真实传感器数据修正模型参数。
5. **闭环优化**：在数字空间中测试控制策略，再部署到实体。

!!! note "术语解释：高保真模型、仿真平台、数据接口、在线标定、闭环优化"
    - **高保真模型（high-fidelity model）**：接近真实物理行为的详细模型。
    - **仿真平台（simulation platform）**：提供物理引擎与可视化环境的软件。
    - **数据接口（data interface）**：不同系统之间交换数据的协议与 API。
    - **在线标定（online calibration）**：利用实际数据修正模型参数。
    - **闭环优化（closed-loop optimization）**：根据反馈持续改进设计或控制。

```mermaid
flowchart TD
    A["物理机器人"] -->|"传感器数据"| B["数据接口"]
    B --> C["数字孪生模型"]
    C --> D["仿真/分析/预测"]
    D --> E["优化策略"]
    E -->|"控制指令"| A
    C -.->|"可视化/监控"| F["运维平台"]
```

## 参考
- Wiki extraction
- 项目 Wiki：chapter-08.md#8.8.3 数字孪生：从虚拟样机到在线映射


