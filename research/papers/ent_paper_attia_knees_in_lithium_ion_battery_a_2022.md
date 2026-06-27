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
  en: A 2022 review that defines capacity-fade 'knees' in lithium-ion batteries, classifies
    six degradation pathways and three internal-state trajectory types, and examines
    sensitivities and prediction challenges.
  zh: 2022年综述，定义了锂离子电池容量衰减中的“拐点”，分类了六种退化路径和三种内部状态轨迹类型，并探讨了敏感性与预测挑战。
  ko: 2022년 리뷰로, 리튬 이온 배터리의 용량 감소 '무릎'을 정의하고 6가지 열화 경로와 3가지 내부 상태 궤적 유형을 분류하며 민감도와
    예측 과제를 검토한다.
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
  reviewed_at: '2026-06-27'
  confidence: medium
  notes: AI-extracted from metadata and abstract; full-text verification required
    before promotion.
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

## Overview

This paper reviews the phenomenon of "knees"—sudden, superlinear capacity fade events—in lithium-ion battery aging trajectories. It begins by defining knees and comparing offline and online knee-point identification algorithms. It then introduces three classes of internal-state trajectories that can produce a knee: snowball trajectories, in which an initial degradation accelerates; hidden trajectories, in which a slowly evolving internal change suddenly manifests as capacity loss; and threshold trajectories, in which a critical transition is crossed.

The authors organize knee causes into six pathways: lithium plating, electrode saturation, resistance growth, electrolyte and additive depletion, percolation-limited connectivity, and mechanical deformation. They note that some pathways involve internal states that are electrochemically undetectable, complicating both diagnosis and prediction. The paper also surveys design and usage sensitivities, such as electrode loading, temperature, state of charge, and cycling protocol, and reports a strong linear correlation between knee point and end-of-life across 17 datasets covering 303 cells.

Finally, the paper discusses modeling and prediction challenges. Because knees can arise from coupled mechanisms and cell-to-cell variability, and because key internal variables are difficult to measure nondestructively, predictive remaining-useful-life estimates remain an open problem.

## Key Contributions

- Defines capacity-fade knees and compares offline and online knee-point identification algorithms.
- Proposes six knee pathways: lithium plating, electrode saturation, resistance growth, electrolyte/additive depletion, percolation-limited connectivity, and mechanical deformation.
- Classifies internal-state trajectories as snowball, hidden, and threshold, linking them to detectability and predictability.
- Identifies cell-design and usage-condition sensitivities that accelerate or delay knees.
- Reports a strong linear correlation between knee point and end-of-life across 17 datasets (303 cells).

## Relevance to Humanoid Robotics

Humanoid robots require compact, high-cycle-life battery packs for untethered operation. Unexpected nonlinear aging knees can prematurely end service life and compromise mission reliability. The paper's framework for understanding, detecting, and predicting knees is therefore directly relevant to the design, health management, and safety certification of humanoid power systems.

Because humanoids may operate under variable loads and temperatures with limited maintenance access, remaining-useful-life estimation and early knee warning become critical for fleet management and deployment planning. The review's emphasis on mechanism-linked sensitivities and detectability can guide battery-selection and battery-management-system requirements for humanoid platforms.
