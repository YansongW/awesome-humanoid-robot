---
$id: ent_tech_li_battery_humanoid
$schema: ../../../../../data/schema/v1/entry_schema.json
$version: 1
type: technology
names:
  en: Lithium-Ion Battery System for Humanoid Robots
  zh: 人形机器人锂离子电池系统
  ko: 휴로이드 로봇용 리튬 이온 배터리 시스템
summary:
  en: The incumbent onboard energy storage technology for humanoid robots, balancing energy density, power density, and cycle
    life, but currently limiting runtime to 2-4 hours for typical dynamic operation.
  zh: '## 概述 人形机器人锂离子电池系统是人形机器人领域的重要technology。以下内容整理自项目 Wiki，供深入查阅。'
  ko: 휴로이드 로봇의 기존 온보드 에너지 저장 기술로, 에너지 밀도, 출력 밀도, 사이클 수명 간의 균형을 맞추지만, 일반적인 동적 작업 시 2-4시간으로 운영 시간을 제한함.
domains:
- 01_raw_materials
- 02_components
- 03_manufacturing_processes
layers:
- upstream
- midstream
functional_roles:
- knowledge
- component
tags:
- lithium_ion_battery
- battery
- energy_density
- power_density
- solid_state_battery
- humanoid_robot
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Body backfilled from kg/entities/ent_component_lithium_battery.md by scripts/backfill_nonpaper_entries.py.
sources:
- id: src_deng_powering_humanoid_robots_2026
  type: paper
  title: 'Powering Humanoid Robots: The Central Role of Battery Technology'
  url: https://www.the-innovation.org/data/article/energy-use/preview/pdf/EU-2026-0002.pdf
  date: '2026-03-25'
  accessed_at: '2026-06-25'
- id: src_interact_analysis_li_batteries_2026
  type: report
  title: 'Humanoid robots and lithium-ion batteries: Long-term commitment or short-term convenience?'
  url: https://interactanalysis.com/insight/humanoid-robots-and-lithium-ion-batteries/
  date: '2026-01-30'
  accessed_at: '2026-06-25'
theoretical_depth:
- system
related_entities:
- id: ent_method_equivalent_circuit_battery_model
  relationship: uses
  description:
    en: The lithium-ion battery system uses equivalent-circuit models for state estimation and voltage prediction.
    zh: 锂离子电池系统使用等效电路模型进行状态估计和电压预测。
    ko: 리튬 이온 배터리 시스템은 상태 추정 및 전압 예측을 위해 등가 회로 모델을 사용한다.
- id: ent_component_battery_management_system
  relationship: integrates
  description:
    en: The battery system integrates a battery management system for monitoring, protection, and balancing.
    zh: 电池系统集成电池管理系统以实现监测、保护和均衡。
    ko: 배터리 시스템은 모니터링, 보호 및 균형을 위해 배터리 관리 시스템을 통합한다.
---

## 概述
人形机器人锂离子电池系统是人形机器人领域的重要technology。以下内容整理自项目 Wiki，供深入查阅。

## 核心内容
## 锂离子电池 / Lithium-ion Battery

### 概述

锂离子电池是一类以锂离子在正负极之间嵌入/脱嵌实现充放电的可充电电池，具有能量密度高、自放电低、无记忆效应等特点。本词条以 Panasonic NCR18650B 圆柱形 NCA 电芯为例，给出机器人电池组设计中常用的关键参数。

### 工作原理 / 技术架构

电池由正极（LiNiCoAlO₂）、石墨负极、隔膜与电解液组成。放电时锂离子从负极经电解液迁移至正极，电子经外电路做功；充电过程相反。电芯储存的能量与质量/体积能量密度为：
\[
E=C \cdot V_{\text{nom}},
\]
\[
\rho_e=\frac{E}{m}\quad\text{或}\quad\rho_v=\frac{E}{V},
\]
其中 \(C\) 为容量（Ah），\(V_{\text{nom}}\) 为标称电压，\(m\) 为质量，\(V\) 为体积。

### 关键参数表

| 规格项 | 数值（以 Panasonic NCR18650B 为例） | 备注/来源 |
|--------|-------------------------------------|-----------|
| 化学体系 | 锂离子（NCA） | DNK Power |
| 标称电压 | 3.6 V | DNK Power |
| 额定容量 | 3200 mAh；典型 3350 mAh | DNK Power |
| 充电电压 | 4.20 ± 0.03 V | DNK Power |
| 放电截止电压 | 2.5 V | DNK Power |
| 最大持续放电电流 | 4.875 A | DNK Power |
| 能量密度 | 676 Wh/L（体积）/ 243 Wh/kg | DNK Power |
| 内阻 | ≤100 mΩ | DNK Power |
| 尺寸 | Φ18.25 mm × 65.10 mm | DNK Power |
| 重量 | ≤47.5 g | DNK Power |
| 循环寿命 | 约 1000 次 | 行业资料 |
| 工作温度 | 充电 0–40 °C；放电 -20–60 °C | DNK Power |

### 应用场景

- 人形机器人躯干/背包电池组
- 移动机器人与无人车动力电源
- 电动工具与便携设备
- 储能系统

### 供应链关系

锂离子电池由松下、宁德时代、三星 SDI、LG 新能源等电芯厂生产，经电池模组/PACK 厂集成 BMS 后供应给机器人整机厂。在知识图谱中，`ent_component_lithium_battery` 作为能源子系统的基础部件，被多种移动机器人产品通过 `uses` 关系引用。

### 来源与验证

- [Panasonic NCR18650B Datasheet (DNK Power)](https://www.dnkpower.com/ncr18650b/)
- [Panasonic NCR18650B Specifications](https://makerselectronics.com/product/panasonic-ncr18650b-3-6v-15a-3350mah/)
- [Battery University - Lithium-ion Overview](https://batteryuniversity.com/article/bu-205-types-of-lithium-ion)

## 参考
- [Powering Humanoid Robots: The Central Role of Battery Technology](https://www.the-innovation.org/data/article/energy-use/preview/pdf/EU-2026-0002.pdf)
- [Humanoid robots and lithium-ion batteries: Long-term commitment or short-term convenience?](https://interactanalysis.com/insight/humanoid-robots-and-lithium-ion-batteries/)
- 项目 Wiki：kg/entities/ent_component_lithium_battery.md


