---
$id: ent_paper_ldhp_library_driven_hierarchic_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'LDHP: Library-Driven Hierarchical Planning for Non-prehensile Dexterous Manipulation'
  zh: 'LDHP: Library-Driven Hierarchical Planning for Non-prehensile Dexterous Manipulation'
  ko: 'LDHP: Library-Driven Hierarchical Planning for Non-prehensile Dexterous Manipulation'
summary:
  en: 'arXiv:2603.13844v2 Announce Type: replace Abstract: Non-prehensile manipulation is essential for handling thin, large,
    or otherwise ungraspable objects in unstructured settings. Prior planning and search-based methods often rely on ad-hoc
    manual designs or generate physically unrealizable motions by ignoring critical gripper properties, while training-based
    approaches are data-intensive and struggle to generalize to novel, out-of-distribution tasks. We propose a library-driven
    hierarchical planner (LDHP) that makes executability a first-class design goal: a top-tier contact-state planner proposes
    object-pose paths using MoveObject primitives, and a bottom-tier grasp planner synthesizes feasible grasp sequences with
    AdjustGrasp primitives; feasibility is certified by collision checks and quasi-static mechanics, and contact-sensitive
    segments are recovered via a bounded dichotomy refinement. This gripper-aware decomposition decouples object motion from
    grasp realizability, yields a task-agnostic pipeline that transfers across manipulation tasks and geometric variations
    without re-design, and exposes clean hooks for optional learned priors. Real-robot studies on zero-mobility lifting and
    slot insertion demonstrate consistent execution and robustness to shape and environment changes.'
  zh: LDHP 是一种基于库驱动的分层规划器，由研究团队提出，用于解决非抓取式灵巧操作问题。其核心贡献在于将可执行性作为首要设计目标，通过顶层接触状态规划器和底层抓取规划器的协同工作，实现任务无关的操作管道，并在真实机器人实验中展示了鲁棒性。
  ko: 'arXiv:2603.13844v2 Announce Type: replace Abstract: Non-prehensile manipulation is essential for handling thin, large,
    or otherwise ungraspable objects in unstructured settings. Prior planning and search-based methods often rely on ad-hoc
    manual designs or generate physically unrealizable motions by ignoring critical gripper properties, while training-based
    approaches are data-intensive and struggle to generalize to novel, out-of-distribution tasks. We propose a library-driven
    hierarchical planner (LDHP) that makes executability a first-class design goal: a top-tier contact-state planner proposes
    object-pose paths using MoveObject primitives, and a bottom-tier grasp planner synthesizes feasible grasp sequences with
    AdjustGrasp primitives; feasibility is certified by collision checks and quasi-static mechanics, and contact-sensitive
    segments are recovered via a bounded dichotomy refinement. This gripper-aware decomposition decouples object motion from
    grasp realizability, yields a task-agnostic pipeline that transfers across manipulation tasks and geometric variations
    without re-design, and exposes clean hooks for optional learned priors. Real-robot studies on zero-mobility lifting and
    slot insertion demonstrate consistent execution and robustness to shape and environment changes.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- humanoid
- ldhp
- robotics
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2603.13844v2. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: 'LDHP: Library-Driven Hierarchical Planning for Non-prehensile Dexterous Manipulation'
  url: https://arxiv.org/abs/2603.13844
  date: '2026'
  accessed_at: '2026-07-01'
---
## 概述
LDHP 通过分层架构将物体运动与抓取可行性解耦，顶层使用 MoveObject 原语规划物体位姿路径，底层使用 AdjustGrasp 原语合成可行抓取序列。该方法通过碰撞检测和准静态力学验证可行性，并采用有界二分细化恢复接触敏感段，从而生成物理可执行的运动。这种设计避免了传统方法中的人工设计或数据密集训练，能够跨任务和几何变化迁移，无需重新设计。

## 核心内容
### 方法架构
LDHP 采用双层规划结构：
- **顶层接触状态规划器**：使用 MoveObject 原语提出物体位姿路径，负责规划物体在接触状态下的运动轨迹。
- **底层抓取规划器**：使用 AdjustGrasp 原语合成可行抓取序列，确保抓取动作的物理可实现性。

### 关键机制
- **可行性验证**：通过碰撞检测和准静态力学模型认证每一步规划的可行性。
- **接触敏感段恢复**：采用有界二分细化（bounded dichotomy refinement）方法，对接触敏感的运动段进行精细调整。
- **任务无关管道**：这种抓取感知分解使得管道能够跨操作任务和几何变化迁移，无需重新设计，并提供了可选学习先验的接口。

### 实验设置与结果
- **真实机器人实验**：在零移动提升（zero-mobility lifting）和槽插入（slot insertion）两个任务上进行测试。
- **鲁棒性表现**：实验证明 LDHP 对形状和环境变化具有一致的执行能力和鲁棒性，能够处理薄、大或不可抓取物体等非抓取操作场景。

## Overview
Non-prehensile manipulation is essential for handling thin, large, or otherwise ungraspable objects in unstructured settings. Prior planning and search-based methods often rely on ad-hoc manual designs or generate physically unrealizable motions by ignoring critical gripper properties, while training-based approaches are data-intensive and struggle to generalize to novel, out-of-distribution tasks. We propose a library-driven hierarchical planner (LDHP) that makes executability a first-class design goal: a top-tier contact-state planner proposes object-pose paths using MoveObject primitives, and a bottom-tier grasp planner synthesizes feasible grasp sequences with AdjustGrasp primitives; feasibility is certified by collision checks and quasi-static mechanics, and contact-sensitive segments are recovered via a bounded dichotomy refinement. This gripper-aware decomposition decouples object motion from grasp realizability, yields a task-agnostic pipeline that transfers across manipulation tasks and geometric variations without re-design, and exposes clean hooks for optional learned priors. Real-robot studies on zero-mobility lifting and slot insertion demonstrate consistent execution and robustness to shape and environment changes.

## 개요
비파지 조작(Non-prehensile manipulation)은 비정형 환경에서 얇거나 크거나 잡기 어려운 물체를 다루는 데 필수적이다. 기존의 계획 및 탐색 기반 방법은 종종 임시방편적인 수동 설계에 의존하거나 중요한 그리퍼 특성을 무시하여 물리적으로 실현 불가능한 움직임을 생성하는 반면, 훈련 기반 접근법은 데이터 집약적이며 새로운 분포 외 작업으로 일반화하는 데 어려움을 겪는다. 우리는 실행 가능성을 최우선 설계 목표로 삼는 라이브러리 기반 계층적 계획기(LDHP)를 제안한다: 상위 계층의 접촉 상태 계획기는 MoveObject 프리미티브를 사용하여 물체 자세 경로를 제안하고, 하위 계층의 파지 계획기는 AdjustGrasp 프리미티브를 사용하여 실행 가능한 파지 시퀀스를 합성한다; 실행 가능성은 충돌 검사와 준정적 역학에 의해 인증되며, 접촉에 민감한 세그먼트는 유계 이분법 정제(bounded dichotomy refinement)를 통해 복구된다. 이러한 그리퍼 인식 분해는 물체 움직임과 파지 실현 가능성을 분리하고, 재설계 없이 조작 작업 및 기하학적 변형 전반에 걸쳐 전이되는 작업 무관 파이프라인을 제공하며, 선택적 학습 사전 지식을 위한 깔끔한 훅을 노출한다. 제로 이동성 리프팅 및 슬롯 삽입에 대한 실제 로봇 연구는 일관된 실행과 형상 및 환경 변화에 대한 강건성을 입증한다.

## 핵심 내용
비파지 조작(Non-prehensile manipulation)은 비정형 환경에서 얇거나 크거나 잡기 어려운 물체를 다루는 데 필수적이다. 기존의 계획 및 탐색 기반 방법은 종종 임시방편적인 수동 설계에 의존하거나 중요한 그리퍼 특성을 무시하여 물리적으로 실현 불가능한 움직임을 생성하는 반면, 훈련 기반 접근법은 데이터 집약적이며 새로운 분포 외 작업으로 일반화하는 데 어려움을 겪는다. 우리는 실행 가능성을 최우선 설계 목표로 삼는 라이브러리 기반 계층적 계획기(LDHP)를 제안한다: 상위 계층의 접촉 상태 계획기는 MoveObject 프리미티브를 사용하여 물체 자세 경로를 제안하고, 하위 계층의 파지 계획기는 AdjustGrasp 프리미티브를 사용하여 실행 가능한 파지 시퀀스를 합성한다; 실행 가능성은 충돌 검사와 준정적 역학에 의해 인증되며, 접촉에 민감한 세그먼트는 유계 이분법 정제(bounded dichotomy refinement)를 통해 복구된다. 이러한 그리퍼 인식 분해는 물체 움직임과 파지 실현 가능성을 분리하고, 재설계 없이 조작 작업 및 기하학적 변형 전반에 걸쳐 전이되는 작업 무관 파이프라인을 제공하며, 선택적 학습 사전 지식을 위한 깔끔한 훅을 노출한다. 제로 이동성 리프팅 및 슬롯 삽입에 대한 실제 로봇 연구는 일관된 실행과 형상 및 환경 변화에 대한 강건성을 입증한다.

## 参考
- http://arxiv.org/abs/2603.13844v2
