---
$id: ent_paper_colledanchise_act_perceive_and_plan_in_belie_2020
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Act, Perceive, and Plan in Belief Space for Robot Localization
  zh: 在信念空间中行动、感知与规划以实现机器人定位
  ko: 로봇 위치 추정을 위한 신념 공간에서의 행동, 인식 및 계획
summary:
  en: This paper proposes an interleaved acting-and-planning framework that reduces robot pose uncertainty by planning sequences
    of actuation and perception actions in belief space, using a best-first search guided by an entropy-based heuristic. The
    method was validated in simulation and on the IIT-R1 humanoid robot, showing that active semantic perception can complement
    feature-based localization in ambiguous environments.
  zh: 本文提出了一种交错执行与规划的框架，通过在信念空间中使用基于熵启发式的最佳优先搜索来规划驱动与感知动作序列，从而降低机器人位姿不确定性。该方法在仿真和IIT-R1人形机器人上进行了验证，表明主动语义感知可以在模糊环境中补充基于特征的定。
  ko: 본 논문은 엔트로피 기반 휴리스틱을 사용하는 최우선 탐색을 통해 신념 공간에서 구동 및 인식 동작 시퀀스를 계획함으로써 로봇 자세 불확실성을 줄이는 행동-계획 상호 교차 프레임워크를 제안한다. 이 방법은 시뮬레이션과
    IIT-R1 휴머노이드 로봇에서 검증되었으며, 모호한 환경에서 능동적 의미 인식이 특징 기반 위치 추정을 보완할 수 있음을 보여준다.
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- intelligence
- knowledge
tags:
- active_perception
- belief_space_planning
- robot_localization
- semantic_localization
- entropy_based_search
- iit_r1
- humanoid_localization
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2002.08124v3.
sources:
- id: src_001
  type: paper
  title: Act, Perceive, and Plan in Belief Space for Robot Localization
  url: https://arxiv.org/abs/2002.08124
  date: '2020'
  accessed_at: '2026-06-28'
theoretical_depth:
- method
---
## 概述
In this paper, we outline an interleaved acting and planning technique to rapidly reduce the uncertainty of the estimated robot's pose by perceiving relevant information from the environment, as recognizing an object or asking someone for a direction.   Generally, existing localization approaches rely on low-level geometric features such as points, lines, and planes, while these approaches provide the desired accuracy, they may require time to converge, especially with incorrect initial guesses. In our approach, a task planner computes a sequence of action and perception tasks to actively obtain relevant information from the robot's perception system. We validate our approach in large state spaces, to show how the approach scales, and in real environments, to show the applicability of our method on real robots.   We prove that our approach is sound, probabilistically complete, and tractable in practical cases.

## 核心内容
In this paper, we outline an interleaved acting and planning technique to rapidly reduce the uncertainty of the estimated robot's pose by perceiving relevant information from the environment, as recognizing an object or asking someone for a direction.   Generally, existing localization approaches rely on low-level geometric features such as points, lines, and planes, while these approaches provide the desired accuracy, they may require time to converge, especially with incorrect initial guesses. In our approach, a task planner computes a sequence of action and perception tasks to actively obtain relevant information from the robot's perception system. We validate our approach in large state spaces, to show how the approach scales, and in real environments, to show the applicability of our method on real robots.   We prove that our approach is sound, probabilistically complete, and tractable in practical cases.

## 参考
- http://arxiv.org/abs/2002.08124v3

## Overview
In this paper, we outline an interleaved acting and planning technique to rapidly reduce the uncertainty of the estimated robot's pose by perceiving relevant information from the environment, such as recognizing an object or asking someone for a direction. Generally, existing localization approaches rely on low-level geometric features such as points, lines, and planes. While these approaches provide the desired accuracy, they may require time to converge, especially with incorrect initial guesses. In our approach, a task planner computes a sequence of action and perception tasks to actively obtain relevant information from the robot's perception system. We validate our approach in large state spaces to demonstrate how it scales, and in real environments to show the applicability of our method on real robots. We prove that our approach is sound, probabilistically complete, and tractable in practical cases.

## Content
In this paper, we outline an interleaved acting and planning technique to rapidly reduce the uncertainty of the estimated robot's pose by perceiving relevant information from the environment, such as recognizing an object or asking someone for a direction. Generally, existing localization approaches rely on low-level geometric features such as points, lines, and planes. While these approaches provide the desired accuracy, they may require time to converge, especially with incorrect initial guesses. In our approach, a task planner computes a sequence of action and perception tasks to actively obtain relevant information from the robot's perception system. We validate our approach in large state spaces to demonstrate how it scales, and in real environments to show the applicability of our method on real robots. We prove that our approach is sound, probabilistically complete, and tractable in practical cases.

## 개요
본 논문에서는 환경으로부터 관련 정보를 인식(예: 객체 인식 또는 방향 문의)하여 추정된 로봇 포즈의 불확실성을 신속히 줄이기 위한 교차 실행 및 계획 기법을 개괄합니다. 일반적으로 기존 위치 추정 접근법은 점, 선, 평면과 같은 저수준 기하학적 특징에 의존합니다. 이러한 접근법은 원하는 정확도를 제공하지만, 특히 초기 추정이 부정확할 경우 수렴에 시간이 소요될 수 있습니다. 본 접근법에서는 작업 계획기가 일련의 행동 및 인식 작업을 계산하여 로봇의 인식 시스템으로부터 관련 정보를 능동적으로 획득합니다. 우리는 대규모 상태 공간에서 접근법의 확장성을 검증하고, 실제 환경에서 실제 로봇에 대한 방법의 적용 가능성을 입증합니다. 또한 본 접근법이 건전하고, 확률적으로 완전하며, 실제 사례에서 다루기 쉬움을 증명합니다.

## 핵심 내용
본 논문에서는 환경으로부터 관련 정보를 인식(예: 객체 인식 또는 방향 문의)하여 추정된 로봇 포즈의 불확실성을 신속히 줄이기 위한 교차 실행 및 계획 기법을 개괄합니다. 일반적으로 기존 위치 추정 접근법은 점, 선, 평면과 같은 저수준 기하학적 특징에 의존합니다. 이러한 접근법은 원하는 정확도를 제공하지만, 특히 초기 추정이 부정확할 경우 수렴에 시간이 소요될 수 있습니다. 본 접근법에서는 작업 계획기가 일련의 행동 및 인식 작업을 계산하여 로봇의 인식 시스템으로부터 관련 정보를 능동적으로 획득합니다. 우리는 대규모 상태 공간에서 접근법의 확장성을 검증하고, 실제 환경에서 실제 로봇에 대한 방법의 적용 가능성을 입증합니다. 또한 본 접근법이 건전하고, 확률적으로 완전하며, 실제 사례에서 다루기 쉬움을 증명합니다.
