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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/1904.03250v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
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

## Overview
It has long been known for elastomers that the velocity of crack propagation jumps as a function of strain. On the other hand, such a jump has not been reported in the literature for polymers which do not exhibit a rubbery plateau in the storage-modulus plot. Here, we report observation of jumps in crack propagation for semi-crystalline polymer sheets without the rubbery plateau, as a result of pulling the sheets at a constant speed. We discuss the advantages of this crack-propagation test under constant-speed stretching and provide physical interpretation of the velocity jump observed for non-elastomer sheets on the basis of a recently proposed theory for the velocity jump in crack propagation.

## 개요
탄성체의 경우 균열 전파 속도가 변형률의 함수로서 점프하는 현상은 오랫동안 알려져 왔습니다. 반면, 저장 탄성률 그래프에서 고무와 같은 평탄 영역을 나타내지 않는 고분자의 경우 이러한 점프가 문헌에서 보고된 바 없습니다. 본 연구에서는 고무 평탄 영역이 없는 반결정성 고분자 시트를 일정 속도로 당겼을 때 균열 전파에서 점프 현상이 관찰됨을 보고합니다. 우리는 일정 속도 인장 하에서의 이 균열 전파 시험의 장점을 논의하고, 최근 제안된 균열 전파 속도 점프 이론을 바탕으로 비탄성체 시트에서 관찰된 속도 점프에 대한 물리적 해석을 제공합니다.

## 핵심 내용
탄성체의 경우 균열 전파 속도가 변형률의 함수로서 점프하는 현상은 오랫동안 알려져 왔습니다. 반면, 저장 탄성률 그래프에서 고무와 같은 평탄 영역을 나타내지 않는 고분자의 경우 이러한 점프가 문헌에서 보고된 바 없습니다. 본 연구에서는 고무 평탄 영역이 없는 반결정성 고분자 시트를 일정 속도로 당겼을 때 균열 전파에서 점프 현상이 관찰됨을 보고합니다. 우리는 일정 속도 인장 하에서의 이 균열 전파 시험의 장점을 논의하고, 최근 제안된 균열 전파 속도 점프 이론을 바탕으로 비탄성체 시트에서 관찰된 속도 점프에 대한 물리적 해석을 제공합니다.

## 参考
- http://arxiv.org/abs/1904.03250v1
