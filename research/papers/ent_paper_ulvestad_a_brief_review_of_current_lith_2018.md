---
$id: ent_paper_ulvestad_a_brief_review_of_current_lith_2018
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: A Brief Review of Current Lithium Ion Battery Technology and Potential Solid State Battery Technologies
  zh: 当前锂离子电池技术与潜在固态电池技术简要综述
  ko: 현재 리튬 이온 전지 기술 및 잠재적 고체 전해질 전지 기술에 대한 간단한 리뷰
summary:
  en: A 2018 review by Andrew Ulvestad that benchmarks state-of-the-art lithium-ion batteries against emerging solid-state
    batteries with lithium-metal anodes, comparing sulfide, polymer, and oxide solid electrolytes and surveying commercial
    SSB programs.
  zh: Andrew Ulvestad 于 2018 年发表的综述，对比了当前最先进的锂离子电池与采用锂金属负极的固态电池。核心贡献在于系统评估了硫化物、聚合物和氧化物三类固态电解质，并调查了丰田、宝马、戴森等公司的固态电池商业化项目，指出尚无固态电池能全面超越液态锂离子电池性能。
  ko: Andrew Ulvestad가 2018년에 발표한 개관 논문으로, 최첨단 리튬 이온 전지와 리튬 금속 음극을 사용하는 신흥 고체 전해질 전지를 비교하며, 황화물·고분자·산화물 고체 전해질 및 상용 SSB 프로그램을
    조사한다.
domains:
- 02_components
- 01_raw_materials
- 05_mass_production
layers:
- midstream
- upstream
functional_roles:
- knowledge
tags:
- lithium_ion_battery
- solid_state_battery
- solid_electrolyte
- lithium_metal_anode
- energy_density
- battery_safety
- power_source
- mobile_energy_storage
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/1803.04317v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: A Brief Review of Current Lithium Ion Battery Technology and Potential Solid State Battery Technologies
  url: https://arxiv.org/abs/1803.04317
  date: '2018'
  accessed_at: '2026-06-27'
theoretical_depth:
- system
---
## 概述
该综述首先回顾了液态锂离子电池的当前性能特征、成本趋势和未来潜力，随后聚焦固态电池研究，重点分析硫化物、聚合物和氧化物三类固态电解质的优缺点。文章还梳理了丰田、宝马、戴森等企业的固态电池商业化尝试，最终给出商业电池未来发展的时间线展望。核心结论是：固态电池虽能通过锂金属负极实现约20%能量密度提升，但至今未有产品在全部性能指标上超越现有液态锂离子电池，部分固态电解质技术甚至可能永远无法达到同等水平。

## 核心内容
### 研究背景与动机
- 固态电池（SSB）因丰田、宝马、戴森等公司投入而备受关注，核心驱动力是采用锂金属负极替代碳负极，可带来约20%能量密度提升。
- 但截至2018年，尚无SSB在所有性能指标上达到最先进液态锂离子电池（LIB）水平，部分固态电解质（SSE）技术可能永远无法与LIB匹敌。

### 液态锂离子电池现状
- 综述首先评估了当前LIB的性能特征、商业成本趋势及未来可能性，作为SSB的基准参照。

### 固态电解质三大类别
- **硫化物电解质**：离子电导率较高，但化学稳定性差，易与锂金属反应。
- **聚合物电解质**：加工性好、柔性高，但室温离子电导率低，需加热运行。
- **氧化物电解质**：热稳定性和电化学窗口宽，但界面阻抗大，制备成本高。

### 商业化尝试
- 调查了丰田、宝马、戴森等公司的SSB商业化项目，但未披露具体性能数据或量产时间表。

### 结论与展望
- 作者认为，SSB技术短期内无法全面替代LIB，未来商业电池的发展需平衡能量密度、安全性和成本，具体时间线取决于电解质材料突破与界面工程进展。

## Overview
Solid state battery technology has recently garnered considerable interest from companies including Toyota, BMW, Dyson, and others. The primary driver behind the commercialization of solid state batteries (SSBs) is to enable the use of lithium metal as the anode, as opposed to the currently used carbon anode, which would result in ~20% energy density improvement. However, no reported solid state battery to date meets all of the performance metrics of state of the art liquid electrolyte lithium ion batteries (LIBs) and indeed several solid state electrolyte (SSE) technologies may never reach parity with current LIBs. We begin with a review of state of the art LIBs, including their current performance characteristics, commercial trends in cost, and future possibilities. We then discuss current SSB research by focusing on three classes of solid state electrolytes: Sulfides, Polymers, and Oxides. We discuss recent and ongoing commercialization attempts in the SSB field. Finally, we conclude with our perspective and timeline for the future of commercial batteries.

## 개요
고체 전지 기술은 최근 Toyota, BMW, Dyson 등 여러 기업으로부터 상당한 관심을 받고 있습니다. 고체 전지(SSB) 상용화의 주요 동기는 현재 사용되는 탄소 음극 대신 리튬 금속을 음극으로 사용할 수 있게 하여 약 20%의 에너지 밀도 향상을 이루는 데 있습니다. 그러나 현재까지 보고된 고체 전지 중 어느 것도 최신 액체 전해질 리튬 이온 배터리(LIB)의 모든 성능 지표를 충족하지 못하며, 실제로 여러 고체 전해질(SSE) 기술은 현재 LIB와 동등한 수준에 도달하지 못할 수도 있습니다. 우리는 최신 LIB의 현재 성능 특성, 비용 측면의 상업적 추세, 그리고 미래 가능성에 대한 검토로 시작합니다. 그런 다음 황화물, 폴리머, 산화물의 세 가지 고체 전해질 종류에 초점을 맞춰 현재 SSB 연구를 논의합니다. SSB 분야의 최근 및 진행 중인 상용화 시도에 대해 논의한 후, 마지막으로 상용 배터리의 미래에 대한 우리의 관점과 타임라인을 제시하며 결론을 맺습니다.

## 핵심 내용
고체 전지 기술은 최근 Toyota, BMW, Dyson 등 여러 기업으로부터 상당한 관심을 받고 있습니다. 고체 전지(SSB) 상용화의 주요 동기는 현재 사용되는 탄소 음극 대신 리튬 금속을 음극으로 사용할 수 있게 하여 약 20%의 에너지 밀도 향상을 이루는 데 있습니다. 그러나 현재까지 보고된 고체 전지 중 어느 것도 최신 액체 전해질 리튬 이온 배터리(LIB)의 모든 성능 지표를 충족하지 못하며, 실제로 여러 고체 전해질(SSE) 기술은 현재 LIB와 동등한 수준에 도달하지 못할 수도 있습니다. 우리는 최신 LIB의 현재 성능 특성, 비용 측면의 상업적 추세, 그리고 미래 가능성에 대한 검토로 시작합니다. 그런 다음 황화물, 폴리머, 산화물의 세 가지 고체 전해질 종류에 초점을 맞춰 현재 SSB 연구를 논의합니다. SSB 분야의 최근 및 진행 중인 상용화 시도에 대해 논의한 후, 마지막으로 상용 배터리의 미래에 대한 우리의 관점과 타임라인을 제시하며 결론을 맺습니다.

## 参考
- http://arxiv.org/abs/1803.04317v1
