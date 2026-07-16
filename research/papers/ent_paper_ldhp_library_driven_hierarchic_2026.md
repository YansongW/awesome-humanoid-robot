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
  zh: 'arXiv:2603.13844v2 Announce Type: replace Abstract: Non-prehensile manipulation is essential for handling thin, large,
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2603.13844v2.
sources:
- id: src_001
  type: paper
  title: 'LDHP: Library-Driven Hierarchical Planning for Non-prehensile Dexterous Manipulation'
  url: https://arxiv.org/abs/2603.13844
  date: '2026'
  accessed_at: '2026-07-01'
---
## 概述
Non-prehensile manipulation is essential for handling thin, large, or otherwise ungraspable objects in unstructured settings. Prior planning and search-based methods often rely on ad-hoc manual designs or generate physically unrealizable motions by ignoring critical gripper properties, while training-based approaches are data-intensive and struggle to generalize to novel, out-of-distribution tasks. We propose a library-driven hierarchical planner (LDHP) that makes executability a first-class design goal: a top-tier contact-state planner proposes object-pose paths using MoveObject primitives, and a bottom-tier grasp planner synthesizes feasible grasp sequences with AdjustGrasp primitives; feasibility is certified by collision checks and quasi-static mechanics, and contact-sensitive segments are recovered via a bounded dichotomy refinement. This gripper-aware decomposition decouples object motion from grasp realizability, yields a task-agnostic pipeline that transfers across manipulation tasks and geometric variations without re-design, and exposes clean hooks for optional learned priors. Real-robot studies on zero-mobility lifting and slot insertion demonstrate consistent execution and robustness to shape and environment changes.

## 核心内容
Non-prehensile manipulation is essential for handling thin, large, or otherwise ungraspable objects in unstructured settings. Prior planning and search-based methods often rely on ad-hoc manual designs or generate physically unrealizable motions by ignoring critical gripper properties, while training-based approaches are data-intensive and struggle to generalize to novel, out-of-distribution tasks. We propose a library-driven hierarchical planner (LDHP) that makes executability a first-class design goal: a top-tier contact-state planner proposes object-pose paths using MoveObject primitives, and a bottom-tier grasp planner synthesizes feasible grasp sequences with AdjustGrasp primitives; feasibility is certified by collision checks and quasi-static mechanics, and contact-sensitive segments are recovered via a bounded dichotomy refinement. This gripper-aware decomposition decouples object motion from grasp realizability, yields a task-agnostic pipeline that transfers across manipulation tasks and geometric variations without re-design, and exposes clean hooks for optional learned priors. Real-robot studies on zero-mobility lifting and slot insertion demonstrate consistent execution and robustness to shape and environment changes.

## 参考
- http://arxiv.org/abs/2603.13844v2

## Overview
Non-prehensile manipulation is essential for handling thin, large, or otherwise ungraspable objects in unstructured settings. Prior planning and search-based methods often rely on ad-hoc manual designs or generate physically unrealizable motions by ignoring critical gripper properties, while training-based approaches are data-intensive and struggle to generalize to novel, out-of-distribution tasks. We propose a library-driven hierarchical planner (LDHP) that makes executability a first-class design goal: a top-tier contact-state planner proposes object-pose paths using MoveObject primitives, and a bottom-tier grasp planner synthesizes feasible grasp sequences with AdjustGrasp primitives; feasibility is certified by collision checks and quasi-static mechanics, and contact-sensitive segments are recovered via a bounded dichotomy refinement. This gripper-aware decomposition decouples object motion from grasp realizability, yields a task-agnostic pipeline that transfers across manipulation tasks and geometric variations without re-design, and exposes clean hooks for optional learned priors. Real-robot studies on zero-mobility lifting and slot insertion demonstrate consistent execution and robustness to shape and environment changes.

## Content
Non-prehensile manipulation is essential for handling thin, large, or otherwise ungraspable objects in unstructured settings. Prior planning and search-based methods often rely on ad-hoc manual designs or generate physically unrealizable motions by ignoring critical gripper properties, while training-based approaches are data-intensive and struggle to generalize to novel, out-of-distribution tasks. We propose a library-driven hierarchical planner (LDHP) that makes executability a first-class design goal: a top-tier contact-state planner proposes object-pose paths using MoveObject primitives, and a bottom-tier grasp planner synthesizes feasible grasp sequences with AdjustGrasp primitives; feasibility is certified by collision checks and quasi-static mechanics, and contact-sensitive segments are recovered via a bounded dichotomy refinement. This gripper-aware decomposition decouples object motion from grasp realizability, yields a task-agnostic pipeline that transfers across manipulation tasks and geometric variations without re-design, and exposes clean hooks for optional learned priors. Real-robot studies on zero-mobility lifting and slot insertion demonstrate consistent execution and robustness to shape and environment changes.

## 개요
비파지 조작(Non-prehensile manipulation)은 비정형 환경에서 얇거나 크거나 잡기 어려운 물체를 다루는 데 필수적이다. 기존의 계획 및 탐색 기반 방법은 종종 임시방편적인 수동 설계에 의존하거나 중요한 그리퍼 특성을 무시하여 물리적으로 실현 불가능한 움직임을 생성하는 반면, 훈련 기반 접근법은 데이터 집약적이며 새로운 분포 외 작업으로 일반화하는 데 어려움을 겪는다. 우리는 실행 가능성을 최우선 설계 목표로 삼는 라이브러리 기반 계층적 계획기(LDHP)를 제안한다: 상위 계층의 접촉 상태 계획기는 MoveObject 프리미티브를 사용하여 물체 자세 경로를 제안하고, 하위 계층의 파지 계획기는 AdjustGrasp 프리미티브를 사용하여 실행 가능한 파지 시퀀스를 합성한다; 실행 가능성은 충돌 검사와 준정적 역학에 의해 인증되며, 접촉에 민감한 세그먼트는 유계 이분법 정제(bounded dichotomy refinement)를 통해 복구된다. 이러한 그리퍼 인식 분해는 물체 움직임과 파지 실현 가능성을 분리하고, 재설계 없이 조작 작업 및 기하학적 변형 전반에 걸쳐 전이되는 작업 무관 파이프라인을 제공하며, 선택적 학습 사전 지식을 위한 깔끔한 훅을 노출한다. 제로 이동성 리프팅 및 슬롯 삽입에 대한 실제 로봇 연구는 일관된 실행과 형상 및 환경 변화에 대한 강건성을 입증한다.

## 핵심 내용
비파지 조작(Non-prehensile manipulation)은 비정형 환경에서 얇거나 크거나 잡기 어려운 물체를 다루는 데 필수적이다. 기존의 계획 및 탐색 기반 방법은 종종 임시방편적인 수동 설계에 의존하거나 중요한 그리퍼 특성을 무시하여 물리적으로 실현 불가능한 움직임을 생성하는 반면, 훈련 기반 접근법은 데이터 집약적이며 새로운 분포 외 작업으로 일반화하는 데 어려움을 겪는다. 우리는 실행 가능성을 최우선 설계 목표로 삼는 라이브러리 기반 계층적 계획기(LDHP)를 제안한다: 상위 계층의 접촉 상태 계획기는 MoveObject 프리미티브를 사용하여 물체 자세 경로를 제안하고, 하위 계층의 파지 계획기는 AdjustGrasp 프리미티브를 사용하여 실행 가능한 파지 시퀀스를 합성한다; 실행 가능성은 충돌 검사와 준정적 역학에 의해 인증되며, 접촉에 민감한 세그먼트는 유계 이분법 정제(bounded dichotomy refinement)를 통해 복구된다. 이러한 그리퍼 인식 분해는 물체 움직임과 파지 실현 가능성을 분리하고, 재설계 없이 조작 작업 및 기하학적 변형 전반에 걸쳐 전이되는 작업 무관 파이프라인을 제공하며, 선택적 학습 사전 지식을 위한 깔끔한 훅을 노출한다. 제로 이동성 리프팅 및 슬롯 삽입에 대한 실제 로봇 연구는 일관된 실행과 형상 및 환경 변화에 대한 강건성을 입증한다.
