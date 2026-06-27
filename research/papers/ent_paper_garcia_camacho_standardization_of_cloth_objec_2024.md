---
$id: ent_paper_garcia_camacho_standardization_of_cloth_objec_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Standardization of Cloth Objects and its Relevance in Robotic Manipulation
  zh: 布料物体的标准化及其在机器人操作中的相关性
  ko: 천 객체의 표준화 및 로봇 조작과의 관련성
summary:
  en: This paper proposes a non-destructive, easy-to-use measurement framework grounded
    in textile-industry standards to characterize physical and mechanical cloth properties,
    and evaluates how stiffness, elasticity, and friction influence five robotic manipulation
    primitives performed with a Franka-Emika Panda robot.
  zh: 本文提出了一种基于纺织工业标准的无损、易用的测量框架，用于表征布料的物理和机械特性，并评估了刚度、弹性和摩擦力如何影响Franka-Emika Panda机器人执行的五种机器人操作基元。
  ko: 본 논문은 섬유 산업 표준에 기반한 비파괴적이고 사용하기 쉬운 측정 프레임워크를 제안하여 천의 물리적 및 기계적 특성을 특성화하고, Franka-Emika
    Panda 로봇으로 수행된 다섯 가지 로봇 조작 프리미티브에 강성, 탄성, 마찰이 미치는 영향을 평가한다.
domains:
- 10_evaluation_benchmarks
- 07_ai_models_algorithms
- 11_applications_markets
layers:
- intelligence
- validation_markets
functional_roles:
- knowledge
- intelligence
tags:
- cloth_manipulation
- deformable_objects
- fabric_characterization
- textile_measurement
- benchmarking
- reproducibility
- franka_emika_panda
- manipulation_primitives
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-06-27'
  confidence: medium
  notes: AI-extracted from supplied metadata and abstract; full paper verification
    recommended.
sources:
- id: src_001
  type: paper
  title: Standardization of Cloth Objects and its Relevance in Robotic Manipulation
  url: https://arxiv.org/abs/2403.04608
  date: '2024'
  accessed_at: '2026-06-27'
theoretical_depth:
- method
---

## Overview

Manipulating deformable objects such as cloth remains a persistent challenge in robotics, partly because physical and mechanical fabric properties—elasticity, stiffness, friction, and drape—are rarely reported in a standardized way. This paper introduces a non-destructive, easy-to-use measurement framework adapted from textile-industry standards so that roboticists can characterize cloth objects consistently and compare different cloth sets. The framework measures key properties and represents them on a radar chart to visualize variability across datasets. A set of manipulation primitives is then used to investigate how measured properties affect task outcomes.

The authors validate the framework on three cloth object sets and analyze the influence of cloth properties on five manipulation primitives performed with a Franka-Emika Panda robot and a custom finger-like gripper. The experiments cover basic interactions such as lift, drag, fold, pull, and push. The results show that different properties correlate differently with success or behavior for each primitive, supporting the argument that cloth characterization should accompany experimental reporting.

The paper concludes with a recommendation that cloth-manipulation results should be reported together with a description of the garments and their measured properties. This would improve reproducibility, enable fair comparisons across studies, and ultimately support generalization of manipulation policies to new cloth instances.

## Key Contributions

- A non-destructive, easy-to-use framework for characterizing cloth objects by physical and mechanical properties.
- Adaptation of textile-industry measurement methods (Cusick drape test, inclined-plane test, tensile test) for robotic applications.
- A radar-chart representation to benchmark and compare cloth sets based on property variability.
- Quantitative analysis of how stiffness, elasticity, and friction influence five manipulation primitives: lift, drag, fold, pull, and push.
- Recommendation to report cloth-property descriptions alongside manipulation results to improve reproducibility.

## Relevance to Humanoid Robotics

Humanoid robots operating in homes, hospitals, or factories will frequently encounter textiles and garments, whether folding laundry, dressing a person, or handling fabric covers. Reliable cloth manipulation therefore depends on understanding how material properties affect behavior. This paper provides a standardized way to measure and report those properties, which is essential for benchmarking and comparing manipulation algorithms across different humanoid platforms. By linking cloth characterization to manipulation outcomes, the work helps bridge the gap between material properties and policy design, supporting better generalization for assistive and service humanoid robots.
