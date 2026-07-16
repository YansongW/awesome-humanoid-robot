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

## Overview
Existing research that addressed cable manipulation relied on two-fingered grippers, which make it difficult to perform similar cable manipulation tasks that humans perform. However, unlike dexterous manipulation of rigid objects, the development of dexterous cable manipulation skills in robotics remains underexplored due to the unique challenges posed by a cable's deformability and inherent uncertainty. In addition, using a dexterous hand introduces specific difficulties in tasks, such as cable grasping, pulling, and in-hand bending, for which no dedicated task definitions, benchmarks, or evaluation metrics exist. Furthermore, we observed that most existing dexterous hands are designed with structures identical to humans', typically featuring only one thumb, which often limits their effectiveness during dexterous cable manipulation. Lastly, existing non-task-specific methods did not have enough generalization ability to solve these cable manipulation tasks or are unsuitable due to the designed hardware. We have three contributions in real-world dexterous cable manipulation in the following steps: (1) We first defined and organized a set of dexterous cable manipulation tasks into a comprehensive taxonomy, covering most short-horizon action primitives and long-horizon tasks for one-handed cable manipulation. This taxonomy revealed that coordination between the thumb and the index finger is critical for cable manipulation, which decomposes long-horizon tasks into simpler primitives. (2) We designed a novel five-fingered hand with 25 degrees of freedom (DoF), featuring two symmetric thumb-index configurations and a rotatable joint on each fingertip, which enables dexterous cable manipulation. (3) We developed a demonstration collection pipeline for this non-anthropomorphic hand, which is difficult to operate by previous motion capture methods.

## Content
Existing research that addressed cable manipulation relied on two-fingered grippers, which make it difficult to perform similar cable manipulation tasks that humans perform. However, unlike dexterous manipulation of rigid objects, the development of dexterous cable manipulation skills in robotics remains underexplored due to the unique challenges posed by a cable's deformability and inherent uncertainty. In addition, using a dexterous hand introduces specific difficulties in tasks, such as cable grasping, pulling, and in-hand bending, for which no dedicated task definitions, benchmarks, or evaluation metrics exist. Furthermore, we observed that most existing dexterous hands are designed with structures identical to humans', typically featuring only one thumb, which often limits their effectiveness during dexterous cable manipulation. Lastly, existing non-task-specific methods did not have enough generalization ability to solve these cable manipulation tasks or are unsuitable due to the designed hardware. We have three contributions in real-world dexterous cable manipulation in the following steps: (1) We first defined and organized a set of dexterous cable manipulation tasks into a comprehensive taxonomy, covering most short-horizon action primitives and long-horizon tasks for one-handed cable manipulation. This taxonomy revealed that coordination between the thumb and the index finger is critical for cable manipulation, which decomposes long-horizon tasks into simpler primitives. (2) We designed a novel five-fingered hand with 25 degrees of freedom (DoF), featuring two symmetric thumb-index configurations and a rotatable joint on each fingertip, which enables dexterous cable manipulation. (3) We developed a demonstration collection pipeline for this non-anthropomorphic hand, which is difficult to operate by previous motion capture methods.

## 개요
기존의 케이블 조작 연구는 두 손가락 그리퍼에 의존해 왔으며, 이는 인간이 수행하는 유사한 케이블 조작 작업을 수행하기 어렵게 만듭니다. 그러나 강체의 정교한 조작과 달리, 케이블의 변형 가능성과 내재된 불확실성으로 인해 로봇 공학에서 정교한 케이블 조작 기술의 개발은 아직 충분히 탐구되지 않았습니다. 또한, 정교한 손을 사용하면 케이블 잡기, 당기기, 손 안에서 구부리기와 같은 작업에서 특정 어려움이 발생하며, 이에 대한 전용 작업 정의, 벤치마크 또는 평가 지표가 존재하지 않습니다. 더 나아가, 기존의 대부분 정교한 손은 인간과 동일한 구조로 설계되어 일반적으로 엄지손가락이 하나만 있어 정교한 케이블 조작 시 효과성이 제한되는 경우가 많습니다. 마지막으로, 기존의 비작업 특화 방법은 이러한 케이블 조작 작업을 해결할 충분한 일반화 능력을 갖추지 못했거나 설계된 하드웨어로 인해 적합하지 않습니다. 우리는 실제 세계에서의 정교한 케이블 조작에 대해 다음 단계에서 세 가지 기여를 했습니다: (1) 먼저, 한 손 케이블 조작을 위한 대부분의 단기 행동 원시 요소와 장기 작업을 포괄하는 포괄적인 분류 체계로 정교한 케이블 조작 작업 세트를 정의하고 정리했습니다. 이 분류 체계는 엄지와 검지의 협력이 케이블 조작에 중요하며, 장기 작업을 더 간단한 원시 요소로 분해한다는 것을 밝혀냈습니다. (2) 우리는 25 자유도(DoF)를 가진 새로운 다섯 손가락 손을 설계했으며, 두 개의 대칭적인 엄지-검지 구성과 각 손가락 끝에 회전 가능한 관절을 특징으로 하여 정교한 케이블 조작을 가능하게 합니다. (3) 우리는 이전의 모션 캡처 방법으로는 작동하기 어려운 이 비인간형 손을 위한 시연 수집 파이프라인을 개발했습니다.

## 핵심 내용
기존의 케이블 조작 연구는 두 손가락 그리퍼에 의존해 왔으며, 이는 인간이 수행하는 유사한 케이블 조작 작업을 수행하기 어렵게 만듭니다. 그러나 강체의 정교한 조작과 달리, 케이블의 변형 가능성과 내재된 불확실성으로 인해 로봇 공학에서 정교한 케이블 조작 기술의 개발은 아직 충분히 탐구되지 않았습니다. 또한, 정교한 손을 사용하면 케이블 잡기, 당기기, 손 안에서 구부리기와 같은 작업에서 특정 어려움이 발생하며, 이에 대한 전용 작업 정의, 벤치마크 또는 평가 지표가 존재하지 않습니다. 더 나아가, 기존의 대부분 정교한 손은 인간과 동일한 구조로 설계되어 일반적으로 엄지손가락이 하나만 있어 정교한 케이블 조작 시 효과성이 제한되는 경우가 많습니다. 마지막으로, 기존의 비작업 특화 방법은 이러한 케이블 조작 작업을 해결할 충분한 일반화 능력을 갖추지 못했거나 설계된 하드웨어로 인해 적합하지 않습니다. 우리는 실제 세계에서의 정교한 케이블 조작에 대해 다음 단계에서 세 가지 기여를 했습니다: (1) 먼저, 한 손 케이블 조작을 위한 대부분의 단기 행동 원시 요소와 장기 작업을 포괄하는 포괄적인 분류 체계로 정교한 케이블 조작 작업 세트를 정의하고 정리했습니다. 이 분류 체계는 엄지와 검지의 협력이 케이블 조작에 중요하며, 장기 작업을 더 간단한 원시 요소로 분해한다는 것을 밝혀냈습니다. (2) 우리는 25 자유도(DoF)를 가진 새로운 다섯 손가락 손을 설계했으며, 두 개의 대칭적인 엄지-검지 구성과 각 손가락 끝에 회전 가능한 관절을 특징으로 하여 정교한 케이블 조작을 가능하게 합니다. (3) 우리는 이전의 모션 캡처 방법으로는 작동하기 어려운 이 비인간형 손을 위한 시연 수집 파이프라인을 개발했습니다.
