---
$id: ent_paper_zhaole_dexterous_cable_manipulation_t_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Dexterous Cable Manipulation: Taxonomy, Multi-Fingered Hand Design, and Long-Horizon
    Manipulation'
  zh: 灵巧电缆操作：分类法、多指手机设计与长程操作
  ko: '민첩한 케이블 조작: 분류법, 다지수 손 설계 및 장기 조작'
summary:
  en: This paper proposes Cable Dexonomy, a taxonomy of dexterous one-handed cable
    manipulation primitives, and introduces a custom 25-DoF five-fingered hand with
    dual symmetric thumb-index configurations and rotatable fingertips, supported
    by a kinesthetic finger-dragging demonstration pipeline that replays primitives
    as finite-state-machine sequences for long-horizon tasks.
  zh: 本文提出了单手灵巧电缆操作原语分类法Cable Dexonomy，介绍了一种具有对称双拇指-食指构型和可旋转指尖的定制25自由度五指手，并开发了基于拖动示教的原语采集与有限状态机回放管道以完成长程任务。
  ko: 본 논문은 한 손 민첩한 케이블 조작 기본 동작 분류법인 Cable Dexonomy를 제안하고, 대칭형 이중 엄지-검지 구성과 회전 가능한
    손끝 관절을 갖춘 사용자 정의 25자유도 5지 손을 소개하며, 장기 과제를 위해 기본 동작을 유한 상태 머신 시퀀스로 재생하는 운동학적 손가락
    끌기 시연 파이프라인을 개발한다.
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
  reviewed_at: '2026-06-28'
  confidence: medium
  notes: AI-extracted from abstract and metadata; full-text review needed to confirm
    section-level citations and exact hardware specifications.
sources:
- id: src_001
  type: paper
  title: 'Dexterous Cable Manipulation: Taxonomy, Multi-Fingered Hand Design, and
    Long-Horizon Manipulation'
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

## Overview

Existing robotic cable manipulation has largely relied on two-fingered grippers or task-specific hardware, which limits the kinds of in-hand and long-horizon operations that humans perform naturally. This paper argues that deformable cables introduce unique uncertainty and deformation challenges, and that most existing dexterous hands follow an anthropomorphic single-thumb design that is not ideal for cable tasks. To address these gaps, the authors present a unified research agenda: a task taxonomy, a non-anthropomorphic five-fingered hand, and a demonstration-based execution pipeline.

The proposed Cable Dexonomy organizes dexterous cable manipulation tasks into short-horizon action primitives and longer one-handed tasks. The taxonomy highlights that coordination between the thumb and index finger is critical for most cable primitives, and that long-horizon tasks can be decomposed into sequences of those primitives. Based on this insight, the authors design a 25-DoF five-fingered hand with two symmetric thumb-index pairs and rotatable fingertip joints, intended to improve cable grasping, pulling, and in-hand bending. Because the hand is non-anthropomorphic, traditional motion-capture-based teleoperation is difficult; the authors therefore develop a kinesthetic finger-dragging demonstration collection method and replay the recorded primitive trajectories through finite-state machines to execute multi-step cable tasks.

## Key Contributions

- Cable Dexonomy: a comprehensive taxonomy of dexterous cable manipulation tasks covering short-horizon primitives and one-handed long-horizon tasks.
- A 25-DoF five-fingered hand with two symmetric thumb-index configurations and rotatable fingertip joints for dexterous cable handling.
- A kinesthetic finger-dragging demonstration pipeline suitable for the non-anthropomorphic hand, enabling collection and replay of primitive trajectories.
- Finite-state-machine composition of primitives for long-horizon cable manipulation, with reported generalization across different cable types.

## Relevance to Humanoid Robotics

Dexterous manipulation of deformable objects such as cables is a key capability for future humanoid robots in industrial wiring, appliance assembly, household cable management, and other flexible-object handling scenarios. The paper's structured primitive taxonomy provides a reusable task vocabulary, while its high-DoF hand design and demonstration pipeline offer a concrete component-and-method reference that can inform end-effector choices and learning architectures for humanoid systems. Although the reported system is arm-static and not yet fully autonomous, it advances both the hardware and algorithmic foundations needed for humanoid cable manipulation.
