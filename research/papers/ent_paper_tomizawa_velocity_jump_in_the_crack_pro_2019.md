---
$id: ent_paper_tomizawa_velocity_jump_in_the_crack_pro_2019
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Velocity jump in the crack propagation induced on a semi-crystalline polymer
    sheet by constant-speed stretching
  zh: 恒速拉伸下半结晶聚合物薄膜裂纹扩展速度跃变研究
  ko: 일정한 속도로 신장시킨 반결정성 고분자 시트에서의 균열 전파 속도 점프
summary:
  en: This paper reports the first experimental observation of a crack-propagation
    velocity jump in a non-elastomer, semi-crystalline polymer sheet under constant-speed
    stretching, and interprets the jump using glass-transition dynamics near the crack
    tip.
  zh: 本文首次报道了在恒速拉伸条件下，非弹性体半结晶聚合物薄膜中裂纹扩展速度跃变的实验现象，并基于裂纹尖端附近的玻璃化转变动力学进行了解释。
  ko: 본 논문은 일정한 속도로 신장시킨 비탄성체 반결정성 고분자 시트에서 균열 전파 속도 점프를 처음으로 실험적으로 관찰하고, 균열 선단 유리
    전이 역학을 기반으로 이를 해석한다.
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
  reviewed_at: '2026-06-27'
  confidence: medium
  notes: AI-extracted from provided metadata and abstract; requires human review of
    full paper before verification.
sources:
- id: src_001
  type: paper
  title: Velocity jump in the crack propagation induced on a semi-crystalline polymer
    sheet by constant-speed stretching
  url: https://arxiv.org/abs/1904.03250
  date: '2019'
  accessed_at: '2026-06-27'
theoretical_depth:
- method
---

## Overview

This study investigates dynamic crack propagation in semi-crystalline polymer sheets that lack a rubbery plateau in their storage-modulus behavior. Previous literature had reported velocity jumps in crack propagation mainly for elastomers; it was therefore an open question whether analogous jumps occur in non-elastomer polymers. The authors perform constant-speed stretching experiments on porous polypropylene sheets and capture both slow pre-jump and fast post-jump crack motion using a conventional digital camera and a high-speed camera. They argue that the constant-speed boundary condition offers practical advantages over traditional fixed-grip tests, including greater sensitivity, shorter experimental time, and smaller sample consumption.

The observed velocity jump is interpreted through a recently proposed theory for elastomer fracture. The authors connect the jump to the glass-transition dynamics localized near the crack tip and invoke a time-temperature correspondence to explain the transition from slow to fast propagation. They also compare the amplitude and scaling of the jump with those reported for rubbers and elastomers, highlighting both similarities and system-specific differences.

## Key Contributions

- First experimental report of a crack-propagation velocity jump in a non-elastomer semi-crystalline polymer sheet.
- Demonstration that dynamic constant-speed stretching is more sensitive, timesaving, and sample-efficient than the traditional fixed-grip static test.
- Physical interpretation linking the observed velocity jump to glass-transition dynamics near the crack tip and to time-temperature correspondence.
- Comparison of jump amplitudes and scaling behavior with those of elastomers/rubbers.

## Relevance to Humanoid Robotics

Tough, lightweight polymer-based materials are critical for fabricating durable structural shells, joints, and protective coverings in humanoid robots intended for mass production and real-world deployment. Understanding fracture dynamics and velocity jumps in semi-crystalline polymers can inform material selection and safety margins for components that experience repeated or impact loading.
