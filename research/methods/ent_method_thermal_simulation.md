---
$id: ent_method_thermal_simulation
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: method
names:
  en: Thermal Simulation
  zh: 热仿真
  ko: 열 시뮬레이션
summary:
  en: A computational method that predicts temperature distribution, heat flux, and cooling requirements of electronic and
    mechanical systems under operating loads.
  zh: 1. 建立功耗模型：列出各组件的稳态功耗、峰值功耗和占空比。 2. 构建几何模型：用 CAD 模型或简化几何表示机器人外壳、散热器、风道。 3. 设置材料属性：导热系数、比热容、密度、发射率。 4. 划分网格：对关键区域加密，对远处区域粗化。
    5. 设定边界条件：环境温度、对流系数、风扇曲线、接触热阻。 6. 求解稳态/瞬态温度场：评估关键芯片结温和外壳温度。 7. 迭代优化：调整散热器、风道、TIM、功耗分配，直到满足热目标。
  ko: 전자·기계 시스템의 작동 하중에서 온도 분포·열 유량·냉각 요구량을 예측하는 계산 방법.
domains:
- 02_components
- 08_software_middleware
layers:
- midstream
functional_roles:
- knowledge
tags:
- method
- chapter_6
- wiki_gap
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: human_and_ai
  reviewed_at: '2026-07-14'
  confidence: high
  notes: Body backfilled from chapter-04.md#两节点热网络模型 by scripts/backfill_nonpaper_entries.py. Body backfilled from chapter-06.md
    section '6.7.3 整机功率与热仿真思路' by scripts/backfill_critical_entities.py.
sources:
- id: src_wiki_extraction
  type: other
  title: Wiki extraction
  date: '2026-07-09'
  accessed_at: '2026-07-09'
---

## 概述
预测电子与机械系统在运行载荷下的温度分布、热流密度与散热需求的计算方法。

## 核心内容
### 6.7.3 整机功率与热仿真思路
整机热仿真通常按以下步骤进行：

1. **建立功耗模型**：列出各组件的稳态功耗、峰值功耗和占空比。
2. **构建几何模型**：用 CAD 模型或简化几何表示机器人外壳、散热器、风道。
3. **设置材料属性**：导热系数、比热容、密度、发射率。
4. **划分网格**：对关键区域加密，对远处区域粗化。
5. **设定边界条件**：环境温度、对流系数、风扇曲线、接触热阻。
6. **求解稳态/瞬态温度场**：评估关键芯片结温和外壳温度。
7. **迭代优化**：调整散热器、风道、TIM、功耗分配，直到满足热目标。

!!! note "术语解释：占空比、CAD、边界条件、网格收敛、风扇曲线"
    - **占空比（duty cycle）**：某组件处于高功耗状态的时间比例。
    - **CAD（Computer-Aided Design）**：计算机辅助设计。
    - **边界条件（boundary condition）**：求解域边界上的物理约束，如温度、热流、对流。
    - **网格收敛（mesh convergence）**：加密网格后结果不再显著变化，说明数值解可信。
    - **风扇曲线（fan curve）**：风扇流量与压降的关系曲线。

### 热仿真在人形机器人中的工程意义
人形机器人集成了计算单元、电机驱动、电池和功率电子，热密度高且空间受限。热仿真用于预判关键芯片结温、电机绕组温升和外壳表面温度，指导散热器、风道、导热界面材料和功耗管理策略的设计，避免过热降频或寿命衰减。通过热-力-电联合仿真，还可以在整机设计早期识别热瓶颈并优化布局。

## 参考
- 项目 Wiki：wiki/docs/chapters/chapter-06.md 第「6.7.3 整机功率与热仿真思路」节
- Wiki extraction

热仿真作为人形机器人产业链中的关键组成部分，其相关理论与工程实践仍在持续发展。深入理解其原理、边界条件与典型应用场景，对于将实验室样机转化为可量产产品具有重要意义。


