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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2603.13844v2. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (668 chars, DeepSeek).'
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

## 参考
- http://arxiv.org/abs/2603.13844v2

## 개요
LDHP는 계층적 아키텍처를 통해 물체 운동과 파지 가능성을 분리하며, 최상위 계층은 MoveObject 프리미티브를 사용하여 물체 자세 경로를 계획하고, 하위 계층은 AdjustGrasp 프리미티브를 사용하여 실행 가능한 파지 시퀀스를 합성합니다. 이 방법은 충돌 감지와 준정적 역학 검증을 통해 실행 가능성을 확인하고, 유계 이분 정밀화(bounded dichotomy refinement)를 사용하여 접촉 민감 구간을 복구함으로써 물리적으로 실행 가능한 운동을 생성합니다. 이러한 설계는 전통적인 방법의 수동 설계나 데이터 집약적 훈련을 피하면서, 재설계 없이 작업 및 기하학적 변화에 걸쳐 전이할 수 있습니다.

## 핵심 내용
### 방법 아키텍처
LDHP는 이중 계층 계획 구조를 채택합니다:
- **최상위 접촉 상태 계획기**: MoveObject 프리미티브를 사용하여 물체 자세 경로를 제안하며, 접촉 상태에서 물체의 운동 궤적을 계획합니다.
- **하위 파지 계획기**: AdjustGrasp 프리미티브를 사용하여 실행 가능한 파지 시퀀스를 합성하며, 파지 동작의 물리적 실현 가능성을 보장합니다.

### 핵심 메커니즘
- **실행 가능성 검증**: 충돌 감지와 준정적 역학 모델을 통해 각 계획 단계의 실행 가능성을 인증합니다.
- **접촉 민감 구간 복구**: 유계 이분 정밀화(bounded dichotomy refinement) 방법을 사용하여 접촉에 민감한 운동 구간을 세밀하게 조정합니다.
- **작업 비의존 파이프라인**: 이러한 파지 인식 분해는 파이프라인이 재설계 없이 조작 작업 및 기하학적 변화에 걸쳐 전이할 수 있게 하며, 선택적 학습 사전(prior) 인터페이스를 제공합니다.

### 실험 설정 및 결과
- **실제 로봇 실험**: 제로 이동 리프팅(zero-mobility lifting) 및 슬롯 삽입(slot insertion) 두 작업에서 테스트되었습니다.
- **강건성 성능**: 실험은 LDHP가 형태 및 환경 변화에 대해 일관된 실행 능력과 강건성을 가지며, 얇거나, 크거나, 파지 불가능한 물체와 같은 비파지 조작 시나리오를 처리할 수 있음을 증명합니다.
