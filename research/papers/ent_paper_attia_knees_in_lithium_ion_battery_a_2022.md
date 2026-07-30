---
$id: ent_paper_attia_knees_in_lithium_ion_battery_a_2022
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: '"Knees" in lithium-ion battery aging trajectories'
  zh: 锂离子电池老化轨迹中的“拐点”
  ko: 리튬 이온 배터리 노화 궤적의 '무릎' 현상
summary:
  en: A 2022 review that defines capacity-fade 'knees' in lithium-ion batteries, classifies six degradation pathways and three
    internal-state trajectory types, and examines sensitivities and prediction challenges.
  zh: 这篇2022年的综述定义了锂离子电池老化轨迹中的容量衰减“拐点”（knees），由研究团队系统分类了六种退化路径和三种内部状态轨迹类型，并探讨了拐点的敏感性及预测挑战。
  ko: 2022년 리뷰로, 리튬 이온 배터리의 용량 감소 '무릎'을 정의하고 6가지 열화 경로와 3가지 내부 상태 궤적 유형을 분류하며 민감도와 예측 과제를 검토한다.
domains:
- 02_components
- 06_design_engineering
- 05_mass_production
layers:
- midstream
- upstream
functional_roles:
- knowledge
- intelligence
tags:
- battery_aging
- lithium_ion_battery
- knee_detection
- capacity_fade
- degradation_pathways
- remaining_useful_life
- power_systems
- energy_storage
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2201.02891v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: '"Knees" in lithium-ion battery aging trajectories'
  url: https://arxiv.org/abs/2201.02891
  date: '2022'
  accessed_at: '2026-06-27'
theoretical_depth:
- method
---
## 概述
该综述首先明确了拐点的定义，并归纳出三种可引发拐点的内部状态轨迹（雪球型、隐藏型和阈值型）。随后详细分析了六种拐点路径，包括锂沉积、电极饱和、电阻增长、电解液与添加剂消耗、逾渗限制的连通性以及机械变形，其中部分路径的内部状态信号在电化学上无法检测。研究还识别了影响拐点的关键设计与使用敏感性，并讨论了建模与预测的难点与机遇。

## 核心内容
### 核心定义与分类
- **拐点定义**：锂离子电池老化轨迹中出现的快速、非线性退化阶段，严重缩短电池寿命。
- **内部状态轨迹**：分为三类：
  - **雪球轨迹**：退化自加速，如锂沉积引发连锁反应。
  - **隐藏轨迹**：内部状态变化但外部电压/容量信号无预警。
  - **阈值轨迹**：达到临界点后突然退化（如电极饱和度）。

### 六种退化路径
1. **锂沉积**：负极表面金属锂析出，导致容量不可逆损失。
2. **电极饱和**：正极活性材料达到锂嵌入极限，引发结构应力。
3. **电阻增长**：SEI膜增厚或电解液分解导致内阻上升。
4. **电解液与添加剂消耗**：关键组分耗尽后副反应失控。
5. **逾渗限制的连通性**：导电网络断裂，活性材料失联。
6. **机械变形**：电极颗粒开裂或分层，加速退化。

### 关键发现
- **不可检测性**：部分路径（如隐藏轨迹）的早期信号无法通过常规电化学手段（如电压曲线）识别。
- **敏感性因素**：拐点出现时间受温度、充放电倍率（C-rate）、截止电压及电极设计（如N/P比）显著影响。
- **预测挑战**：现有模型难以捕捉非线性拐点，需结合多物理场仿真与数据驱动方法。

### 结论
该综述揭示了锂离子电池退化的复杂性与隐蔽性，为学术界和工业界延长电池寿命提供了系统性的路径分类与预测方向。

## Overview
Lithium-ion batteries can last many years but sometimes exhibit rapid, nonlinear degradation that severely limits battery lifetime. In this work, we review prior work on "knees" in lithium-ion battery aging trajectories. We first review definitions for knees and three classes of "internal state trajectories" (termed snowball, hidden, and threshold trajectories) that can cause a knee. We then discuss six knee "pathways", including lithium plating, electrode saturation, resistance growth, electrolyte and additive depletion, percolation-limited connectivity, and mechanical deformation -- some of which have internal state trajectories with signals that are electrochemically undetectable. We also identify key design and usage sensitivities for knees. Finally, we discuss challenges and opportunities for knee modeling and prediction. Our findings illustrate the complexity and subtlety of lithium-ion battery degradation and can aid both academic and industrial efforts to improve battery lifetime.

## 개요
리튬이온 배터리는 수년간 지속될 수 있지만, 때로는 배터리 수명을 심각하게 제한하는 급격하고 비선형적인 열화를 보입니다. 본 연구에서는 리튬이온 배터리 노화 궤적에서의 "니(knee)"에 대한 선행 연구를 검토합니다. 먼저 니의 정의와 니를 유발할 수 있는 세 가지 유형의 "내부 상태 궤적"(스노우볼, 히든, 임계값 궤적이라고 함)을 검토합니다. 그런 다음 리튬 도금, 전극 포화, 저항 증가, 전해질 및 첨가제 고갈, 퍼콜레이션 제한 연결성, 기계적 변형을 포함한 여섯 가지 니 "경로"를 논의합니다. 이 중 일부는 전기화학적으로 감지할 수 없는 신호를 가진 내부 상태 궤적을 포함합니다. 또한 니에 대한 주요 설계 및 사용 민감도를 식별합니다. 마지막으로 니 모델링 및 예측의 과제와 기회를 논의합니다. 본 연구 결과는 리튬이온 배터리 열화의 복잡성과 미묘함을 보여주며, 배터리 수명 개선을 위한 학계 및 산업계의 노력에 도움이 될 수 있습니다.

## 핵심 내용
리튬이온 배터리는 수년간 지속될 수 있지만, 때로는 배터리 수명을 심각하게 제한하는 급격하고 비선형적인 열화를 보입니다. 본 연구에서는 리튬이온 배터리 노화 궤적에서의 "니(knee)"에 대한 선행 연구를 검토합니다. 먼저 니의 정의와 니를 유발할 수 있는 세 가지 유형의 "내부 상태 궤적"(스노우볼, 히든, 임계값 궤적이라고 함)을 검토합니다. 그런 다음 리튬 도금, 전극 포화, 저항 증가, 전해질 및 첨가제 고갈, 퍼콜레이션 제한 연결성, 기계적 변형을 포함한 여섯 가지 니 "경로"를 논의합니다. 이 중 일부는 전기화학적으로 감지할 수 없는 신호를 가진 내부 상태 궤적을 포함합니다. 또한 니에 대한 주요 설계 및 사용 민감도를 식별합니다. 마지막으로 니 모델링 및 예측의 과제와 기회를 논의합니다. 본 연구 결과는 리튬이온 배터리 열화의 복잡성과 미묘함을 보여주며, 배터리 수명 개선을 위한 학계 및 산업계의 노력에 도움이 될 수 있습니다.

## 参考
- http://arxiv.org/abs/2201.02891v1
