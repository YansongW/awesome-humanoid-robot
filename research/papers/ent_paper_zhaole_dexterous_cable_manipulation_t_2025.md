---
$id: ent_paper_zhaole_dexterous_cable_manipulation_t_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Dexterous Cable Manipulation: Taxonomy, Multi-Fingered Hand Design, and Long-Horizon Manipulation'
  zh: 灵巧电缆操作：分类法、多指手机设计与长程操作
  ko: '민첩한 케이블 조작: 분류법, 다지수 손 설계 및 장기 조작'
summary:
  en: This paper proposes Cable Dexonomy, a taxonomy of dexterous one-handed cable manipulation primitives, and introduces
    a custom 25-DoF five-fingered hand with dual symmetric thumb-index configurations and rotatable fingertips, supported
    by a kinesthetic finger-dragging demonstration pipeline that replays primitives as finite-state-machine sequences for
    long-horizon tasks.
  zh: 本文提出了单手灵巧电缆操作原语分类法Cable Dexonomy，介绍了一种具有对称双拇指-食指构型和可旋转指尖的定制25自由度五指手，并开发了基于拖动示教的原语采集与有限状态机回放管道以完成长程任务。
  ko: 본 논문은 한 손 민첩한 케이블 조작 기본 동작 분류법인 Cable Dexonomy를 제안하고, 대칭형 이중 엄지-검지 구성과 회전 가능한 손끝 관절을 갖춘 사용자 정의 25자유도 5지 손을 소개하며, 장기
    과제를 위해 기본 동작을 유한 상태 머신 시퀀스로 재생하는 운동학적 손가락 끌기 시연 파이프라인을 개발한다.
domains:
- 02_components
- 07_ai_models_algorithms
- 06_design_engineering
- 03_manufacturing_processes
layers:
- intelligence
- midstream
- upstream
functional_roles:
- knowledge
- intelligence
- component
tags:
- dexterous_manipulation
- cable_manipulation
- multi_fingered_hand
- taxonomy
- demonstration_learning
- finite_state_machine
- flexible_object_manipulation
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2502.00396v2.
sources:
- id: src_001
  type: paper
  title: 'Dexterous Cable Manipulation: Taxonomy, Multi-Fingered Hand Design, and Long-Horizon Manipulation'
  url: https://arxiv.org/abs/2502.00396
  date: '2025'
  accessed_at: '2026-06-28'
theoretical_depth:
- method
related_entities:
- id: ent_component_leap_hand
  relationship: builds_on
  description:
    en: The custom hand uses Leap Hand fingers as the basis for its finger design.
    zh: 定制手的设计以Leap Hand的手指为基础。
    ko: 사용자 정의 손은 Leap Hand의 손가락을 손가락 설계의 기반으로 사용한다.
---
## 概述
Existing research that addressed cable manipulation relied on two-fingered grippers, which make it difficult to perform similar cable manipulation tasks that humans perform. However, unlike dexterous manipulation of rigid objects, the development of dexterous cable manipulation skills in robotics remains underexplored due to the unique challenges posed by a cable's deformability and inherent uncertainty. In addition, using a dexterous hand introduces specific difficulties in tasks, such as cable grasping, pulling, and in-hand bending, for which no dedicated task definitions, benchmarks, or evaluation metrics exist. Furthermore, we observed that most existing dexterous hands are designed with structures identical to humans', typically featuring only one thumb, which often limits their effectiveness during dexterous cable manipulation. Lastly, existing non-task-specific methods did not have enough generalization ability to solve these cable manipulation tasks or are unsuitable due to the designed hardware. We have three contributions in real-world dexterous cable manipulation in the following steps: (1) We first defined and organized a set of dexterous cable manipulation tasks into a comprehensive taxonomy, covering most short-horizon action primitives and long-horizon tasks for one-handed cable manipulation. This taxonomy revealed that coordination between the thumb and the index finger is critical for cable manipulation, which decomposes long-horizon tasks into simpler primitives. (2) We designed a novel five-fingered hand with 25 degrees of freedom (DoF), featuring two symmetric thumb-index configurations and a rotatable joint on each fingertip, which enables dexterous cable manipulation. (3) We developed a demonstration collection pipeline for this non-anthropomorphic hand, which is difficult to operate by previous motion capture methods.

## 核心内容
Existing research that addressed cable manipulation relied on two-fingered grippers, which make it difficult to perform similar cable manipulation tasks that humans perform. However, unlike dexterous manipulation of rigid objects, the development of dexterous cable manipulation skills in robotics remains underexplored due to the unique challenges posed by a cable's deformability and inherent uncertainty. In addition, using a dexterous hand introduces specific difficulties in tasks, such as cable grasping, pulling, and in-hand bending, for which no dedicated task definitions, benchmarks, or evaluation metrics exist. Furthermore, we observed that most existing dexterous hands are designed with structures identical to humans', typically featuring only one thumb, which often limits their effectiveness during dexterous cable manipulation. Lastly, existing non-task-specific methods did not have enough generalization ability to solve these cable manipulation tasks or are unsuitable due to the designed hardware. We have three contributions in real-world dexterous cable manipulation in the following steps: (1) We first defined and organized a set of dexterous cable manipulation tasks into a comprehensive taxonomy, covering most short-horizon action primitives and long-horizon tasks for one-handed cable manipulation. This taxonomy revealed that coordination between the thumb and the index finger is critical for cable manipulation, which decomposes long-horizon tasks into simpler primitives. (2) We designed a novel five-fingered hand with 25 degrees of freedom (DoF), featuring two symmetric thumb-index configurations and a rotatable joint on each fingertip, which enables dexterous cable manipulation. (3) We developed a demonstration collection pipeline for this non-anthropomorphic hand, which is difficult to operate by previous motion capture methods.

## 参考
- http://arxiv.org/abs/2502.00396v2

