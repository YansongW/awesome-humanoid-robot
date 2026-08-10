---
$id: ent_paper_tomizawa_velocity_jump_in_the_crack_pro_2019
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Velocity jump in the crack propagation induced on a semi-crystalline polymer sheet by constant-speed stretching
  zh: 恒速拉伸下半结晶聚合物薄膜裂纹扩展速度跃变研究
  ko: 일정한 속도로 신장시킨 반결정성 고분자 시트에서의 균열 전파 속도 점프
summary:
  en: This paper reports the first experimental observation of a crack-propagation velocity jump in a non-elastomer, semi-crystalline
    polymer sheet under constant-speed stretching, and interprets the jump using glass-transition dynamics near the crack
    tip.
  zh: 本文首次实验观察到非弹性体半结晶聚合物薄片在恒速拉伸下裂纹扩展速度的跳跃现象，并利用裂纹尖端附近的玻璃化转变动力学解释了该现象。研究由作者团队完成，核心贡献在于将此前仅见于弹性体的裂纹速度跳跃扩展至非弹性体材料，并提供了基于最新理论的物理解释。
  ko: 본 논문은 일정한 속도로 신장시킨 비탄성체 반결정성 고분자 시트에서 균열 전파 속도 점프를 처음으로 실험적으로 관찰하고, 균열 선단 유리 전이 역학을 기반으로 이를 해석한다.
domains:
- 01_raw_materials
- 06_design_engineering
layers:
- midstream
- upstream
functional_roles:
- knowledge
- material
tags:
- polymer_mechanics
- crack_propagation
- semi_crystalline_polymer
- fracture_dynamics
- material_characterization
- porous_polypropylene
- lightweight_materials
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/1904.03250v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    en/ko body retranslated from zh deep-read (656 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: Velocity jump in the crack propagation induced on a semi-crystalline polymer sheet by constant-speed stretching
  url: https://arxiv.org/abs/1904.03250
  date: '2019'
  accessed_at: '2026-06-27'
theoretical_depth:
- method
---
## 概述
长期以来，弹性体在应变作用下裂纹扩展速度的跳跃现象已被熟知，但此类跳跃从未在缺乏橡胶态平台（即储能模量图中无橡胶态平台）的聚合物中被报道。本研究通过恒速拉伸半结晶聚合物薄片，首次观察到无橡胶态平台的此类材料中裂纹扩展速度的跳跃。论文讨论了恒速拉伸裂纹扩展测试的优势，并基于近期提出的裂纹速度跳跃理论，为观察到的非弹性体薄片速度跳跃提供了物理诠释。

## 核心内容
### 实验发现
- 在恒速拉伸条件下，半结晶聚合物薄片（无橡胶态平台）的裂纹扩展速度出现跳跃，这是非弹性体材料中的首次实验观测。
- 此前，弹性体（如橡胶）的裂纹速度跳跃已被广泛研究，但非弹性体聚合物（如半结晶聚合物）中未见报道。

### 测试方法优势
- 恒速拉伸测试避免了传统恒定应变或恒定载荷测试中的复杂应力松弛效应，更易于控制实验条件。
- 该方法能直接关联裂纹尖端局部应变率与材料玻璃化转变动力学，为解释速度跳跃提供关键线索。

### 物理解释
- 裂纹尖端附近材料经历高应变率，导致局部玻璃化转变温度（Tg）升高，使原本处于橡胶态的区域转变为玻璃态。
- 这种玻璃化转变引发裂纹尖端附近材料刚度的突变，进而导致裂纹扩展速度的跳跃。
- 该解释基于近期提出的理论模型，该模型将裂纹速度跳跃归因于应变率诱导的玻璃化转变。

### 关键结论
- 非弹性体聚合物中裂纹速度跳跃的存在表明，该现象可能具有普适性，不限于弹性体。
- 恒速拉伸测试为研究聚合物断裂动力学提供了新工具，尤其适用于揭示玻璃化转变在裂纹扩展中的作用。

## 参考
- http://arxiv.org/abs/1904.03250v1

## Overview
For a long time, the phenomenon of abrupt jumps in crack propagation speed under strain has been well known in elastomers, but such jumps have never been reported in polymers lacking a rubbery plateau (i.e., no rubbery plateau in the storage modulus plot). In this study, by stretching semi-crystalline polymer sheets at a constant rate, crack propagation speed jumps were observed for the first time in such materials without a rubbery plateau. The paper discusses the advantages of constant-rate tensile crack propagation tests and, based on a recently proposed theory of crack speed jumps, provides a physical interpretation for the observed speed jumps in non-elastomeric sheets.

## Content
### Experimental Findings
- Under constant-rate tensile conditions, crack propagation speed jumps were observed in semi-crystalline polymer sheets (without a rubbery plateau), marking the first experimental observation of this phenomenon in non-elastomeric materials.
- Previously, crack speed jumps in elastomers (such as rubber) had been extensively studied, but no such reports existed for non-elastomeric polymers (e.g., semi-crystalline polymers).

### Advantages of the Testing Method
- Constant-rate tensile testing avoids the complex stress relaxation effects encountered in traditional constant-strain or constant-load tests, making experimental conditions easier to control.
- This method directly links the local strain rate at the crack tip to the glass transition dynamics of the material, providing key clues for explaining the speed jumps.

### Physical Interpretation
- The material near the crack tip experiences high strain rates, leading to an increase in the local glass transition temperature (Tg), causing regions originally in the rubbery state to transition to a glassy state.
- This glass transition induces a sudden change in the stiffness of the material near the crack tip, which in turn leads to the jump in crack propagation speed.
- This explanation is based on a recently proposed theoretical model that attributes crack speed jumps to strain-rate-induced glass transition.

### Key Conclusions
- The presence of crack speed jumps in non-elastomeric polymers suggests that this phenomenon may be universal and not limited to elastomers.
- Constant-rate tensile testing provides a new tool for studying polymer fracture dynamics, particularly useful for revealing the role of glass transition in crack propagation.

## 개요
오랫동안 탄성체에서 변형률 하의 균열 성장 속도 점프 현상은 잘 알려져 왔지만, 이러한 점프는 고무 상태 플랫폼(즉, 저장 탄성률 그래프에서 고무 상태 플랫폼이 없는)이 부재한 폴리머에서는 보고된 적이 없었습니다. 본 연구는 반결정성 폴리머 박막을 일정 속도로 인장하여, 고무 상태 플랫폼이 없는 이러한 재료에서 균열 성장 속도 점프를 최초로 관찰했습니다. 논문은 일정 속도 인장 균열 성장 테스트의 장점을 논의하고, 최근 제안된 균열 속도 점프 이론에 기반하여 관찰된 비탄성체 박막의 속도 점프에 대한 물리적 해석을 제공합니다.

## 핵심 내용
### 실험 발견
- 일정 속도 인장 조건에서 반결정성 폴리머 박막(고무 상태 플랫폼 없음)의 균열 성장 속도가 점프를 나타내며, 이는 비탄성체 재료에서의 최초 실험 관찰입니다.
- 이전에는 탄성체(예: 고무)의 균열 속도 점프가 널리 연구되었지만, 비탄성체 폴리머(예: 반결정성 폴리머)에서는 보고된 바 없습니다.

### 테스트 방법의 장점
- 일정 속도 인장 테스트는 기존의 일정 변형률 또는 일정 하중 테스트에서의 복잡한 응력 완화 효과를 피하여 실험 조건을 더 쉽게 제어할 수 있습니다.
- 이 방법은 균열 선단 근처의 국소 변형률 속도를 재료의 유리 전이 동역학과 직접 연결할 수 있어, 속도 점프를 설명하는 핵심 단서를 제공합니다.

### 물리적 해석
- 균열 선단 근처의 재료는 높은 변형률 속도를 경험하여 국소 유리 전이 온도(Tg)가 상승하고, 원래 고무 상태였던 영역이 유리 상태로 전환됩니다.
- 이러한 유리 전이는 균열 선단 근처 재료의 강성 급변을 유발하여 균열 성장 속도의 점프로 이어집니다.
- 이 해석은 최근 제안된 이론 모델에 기반하며, 해당 모델은 균열 속도 점프를 변형률 속도 유도 유리 전이에 기인합니다.

### 핵심 결론
- 비탄성체 폴리머에서 균열 속도 점프의 존재는 이 현상이 탄성체에 국한되지 않고 보편적일 수 있음을 시사합니다.
- 일정 속도 인장 테스트는 폴리머 파괴 동역학을 연구하는 새로운 도구를 제공하며, 특히 균열 성장에서 유리 전이의 역할을 밝히는 데 유용합니다.
