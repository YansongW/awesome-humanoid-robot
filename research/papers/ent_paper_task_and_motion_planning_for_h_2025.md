---
$id: ent_paper_task_and_motion_planning_for_h_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Task and Motion Planning for Humanoid Loco-manipulation
  zh: Task and Motion Planning for Humanoid Loco-manipulation
  ko: Task and Motion Planning for Humanoid Loco-manipulation
summary:
  en: Task and Motion Planning for Humanoid Loco-manipulation is a 2025 work on loco-manipulation and whole-body-control for
    humanoid robots.
  zh: 这是一项2025年关于人形机器人全身控制与移动操作的研究，提出了基于优化的任务与运动规划（TAMP）框架。其核心贡献在于通过共享接触模式表示，统一了移动与操作的规划过程，并首次在完全非循环规划中整合了全身动力学与驱动约束。
  ko: Task and Motion Planning for Humanoid Loco-manipulation is a 2025 work on loco-manipulation and whole-body-control for
    humanoid robots.
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
- loco_manipulation
- task_and_motion_planning_for_h
- whole_body_control
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2508.14099v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (516 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: Task and Motion Planning for Humanoid Loco-manipulation (arXiv)
  url: https://arxiv.org/abs/2508.14099
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
该工作将符号动作定义为接触模式的变化，从而将高层任务规划与低层运动规划联系起来。通过这种统一表示，框架能够同时处理任务、接触和运动规划，并纳入机器人、操作对象与环境之间的全部约束。在人形平台上的实验表明，该方法能够生成长序列、复杂推理下的多种物理一致移动操作行为。

## 核心内容
### 方法架构
- 提出基于优化的TAMP框架，通过**共享接触模式表示**统一移动与操作规划。
- 将**符号动作**定义为接触模式的变化，实现高层任务规划与低层运动规划的衔接。
- 采用**统一搜索**策略，同时覆盖任务、接触和运动规划三个层次。

### 关键特性
- 整合**全身动力学**模型，包含机器人、操作对象与环境之间的所有约束。
- 支持**完全非循环规划**，无需预设规划顺序。
- 考虑**驱动约束**，确保生成的运动在物理上可行。

### 实验设置与结果
- 在人形机器人平台上验证，能够生成**长动作序列**下的复杂移动操作行为。
- 行为在**物理一致性**上表现良好，涵盖多种操作场景。
- 据作者称，这是首个解决**人形机器人移动操作**中集成TAMP公式的工作，同时满足非循环规划与全身动力学约束。

## Overview
This work presents an optimization-based task and motion planning (TAMP) framework that unifies planning for locomotion and manipulation through a shared representation of contact modes. We define symbolic actions as contact mode changes, grounding high-level planning in low-level motion. This enables a unified search that spans task, contact, and motion planning while incorporating whole-body dynamics, as well as all constraints between the robot, the manipulated object, and the environment. Results on a humanoid platform show that our method can generate a broad range of physically consistent loco-manipulation behaviors over long action sequences requiring complex reasoning. To the best of our knowledge, this is the first work that enables the resolution of an integrated TAMP formulation with fully acyclic planning and whole body dynamics with actuation constraints for the humanoid loco-manipulation problem.

## 参考
- http://arxiv.org/abs/2508.14099v1

## 개요
이 연구는 기호적 행동을 접촉 패턴의 변화로 정의하여, 상위 수준의 작업 계획과 하위 수준의 운동 계획을 연결합니다. 이러한 통합 표현을 통해 프레임워크는 작업, 접촉 및 운동 계획을 동시에 처리할 수 있으며, 로봇, 조작 대상 및 환경 간의 모든 제약 조건을 포함합니다. 휴머노이드 플랫폼에서의 실험은 이 방법이 긴 시퀀스와 복잡한 추론 하에서 다양한 물리적으로 일관된 이동 조작 행동을 생성할 수 있음을 보여줍니다.

## 핵심 내용
### 방법 아키텍처
- 최적화 기반 TAMP 프레임워크를 제안하며, **공유 접촉 패턴 표현**을 통해 이동 및 조작 계획을 통합합니다.
- **기호적 행동**을 접촉 패턴의 변화로 정의하여, 상위 수준의 작업 계획과 하위 수준의 운동 계획을 연결합니다.
- **통합 검색** 전략을 채택하여 작업, 접촉 및 운동 계획의 세 가지 수준을 동시에 다룹니다.

### 주요 특징
- **전신 동역학** 모델을 통합하여 로봇, 조작 대상 및 환경 간의 모든 제약 조건을 포함합니다.
- **완전 비순환 계획**을 지원하며, 사전에 계획 순서를 설정할 필요가 없습니다.
- **구동 제약 조건**을 고려하여 생성된 운동이 물리적으로 실행 가능하도록 보장합니다.

### 실험 설정 및 결과
- 휴머노이드 로봇 플랫폼에서 검증되었으며, **긴 동작 시퀀스** 하에서 복잡한 이동 조작 행동을 생성할 수 있습니다.
- 행동은 **물리적 일관성** 측면에서 우수한 성능을 보이며, 다양한 조작 시나리오를 포함합니다.
- 저자에 따르면, 이는 **휴머노이드 로봇 이동 조작**에서 통합 TAMP 공식을 해결한 최초의 작업으로, 비순환 계획과 전신 동역학 제약 조건을 동시에 충족합니다.
