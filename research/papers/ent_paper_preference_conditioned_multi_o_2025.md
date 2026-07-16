---
$id: ent_paper_preference_conditioned_multi_o_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Preference-Conditioned Multi-Objective RL for Integrated Command Tracking and Force Compliance in Humanoid Locomotion
  zh: Preference-Conditioned Multi-Objective RL for Integrated Command Tracking and Force Compliance in Humanoid Locomotion
  ko: Preference-Conditioned Multi-Objective RL for Integrated Command Tracking and Force Compliance in Humanoid Locomotion
summary:
  en: Preference-Conditioned Multi-Objective RL for Integrated Command Tracking and Force Compliance in Humanoid Locomotion
    is a 2025 work on locomotion for humanoid robots.
  zh: Preference-Conditioned Multi-Objective RL for Integrated Command Tracking and Force Compliance in Humanoid Locomotion
    is a 2025 work on locomotion for humanoid robots.
  ko: Preference-Conditioned Multi-Objective RL for Integrated Command Tracking and Force Compliance in Humanoid Locomotion
    is a 2025 work on locomotion for humanoid robots.
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- humanoid
- locomotion
- preference_conditioned_multi_o
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2510.10851v2.
sources:
- id: src_001
  type: paper
  title: Preference-Conditioned Multi-Objective RL for Integrated Command Tracking and Force Compliance in Humanoid Locomotion
    (arXiv)
  url: https://arxiv.org/abs/2510.10851
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Humanoid locomotion requires not only accurate command tracking for navigation but also compliant responses to external forces during human interaction. Despite significant progress, existing RL approaches mainly emphasize robustness, yielding policies that resist external forces but lack compliance particularly challenging for inherently unstable humanoids. In this work, we address this by formulating humanoid locomotion as a multi-objective optimization problem that balances command tracking and external force compliance. We introduce a preference-conditioned multi-objective RL (MORL) framework that enables a single omnidirectional locomotion policy to trade off between command following and force compliance via a user-specified preference input. External forces are modeled via velocity-resistance factor for consistent reward design, and training leverages an encoder-decoder structure that infers task-relevant privileged features from deployable observations. We validate our approach in both simulation and real-world experiments on a humanoid robot. Experimental results in simulation and on hardware show that the framework trains stably and enables deployable preference-conditioned humanoid locomotion.

## 核心内容
Humanoid locomotion requires not only accurate command tracking for navigation but also compliant responses to external forces during human interaction. Despite significant progress, existing RL approaches mainly emphasize robustness, yielding policies that resist external forces but lack compliance particularly challenging for inherently unstable humanoids. In this work, we address this by formulating humanoid locomotion as a multi-objective optimization problem that balances command tracking and external force compliance. We introduce a preference-conditioned multi-objective RL (MORL) framework that enables a single omnidirectional locomotion policy to trade off between command following and force compliance via a user-specified preference input. External forces are modeled via velocity-resistance factor for consistent reward design, and training leverages an encoder-decoder structure that infers task-relevant privileged features from deployable observations. We validate our approach in both simulation and real-world experiments on a humanoid robot. Experimental results in simulation and on hardware show that the framework trains stably and enables deployable preference-conditioned humanoid locomotion.

## 参考
- http://arxiv.org/abs/2510.10851v2

## Overview
Humanoid locomotion requires not only accurate command tracking for navigation but also compliant responses to external forces during human interaction. Despite significant progress, existing RL approaches mainly emphasize robustness, yielding policies that resist external forces but lack compliance, which is particularly challenging for inherently unstable humanoids. In this work, we address this by formulating humanoid locomotion as a multi-objective optimization problem that balances command tracking and external force compliance. We introduce a preference-conditioned multi-objective RL (MORL) framework that enables a single omnidirectional locomotion policy to trade off between command following and force compliance via a user-specified preference input. External forces are modeled via a velocity-resistance factor for consistent reward design, and training leverages an encoder-decoder structure that infers task-relevant privileged features from deployable observations. We validate our approach in both simulation and real-world experiments on a humanoid robot. Experimental results in simulation and on hardware show that the framework trains stably and enables deployable preference-conditioned humanoid locomotion.

## Content
Humanoid locomotion requires not only accurate command tracking for navigation but also compliant responses to external forces during human interaction. Despite significant progress, existing RL approaches mainly emphasize robustness, yielding policies that resist external forces but lack compliance, which is particularly challenging for inherently unstable humanoids. In this work, we address this by formulating humanoid locomotion as a multi-objective optimization problem that balances command tracking and external force compliance. We introduce a preference-conditioned multi-objective RL (MORL) framework that enables a single omnidirectional locomotion policy to trade off between command following and force compliance via a user-specified preference input. External forces are modeled via a velocity-resistance factor for consistent reward design, and training leverages an encoder-decoder structure that infers task-relevant privileged features from deployable observations. We validate our approach in both simulation and real-world experiments on a humanoid robot. Experimental results in simulation and on hardware show that the framework trains stably and enables deployable preference-conditioned humanoid locomotion.

## 개요
휴머노이드 보행은 내비게이션을 위한 정확한 명령 추적뿐만 아니라 인간과의 상호작용 중 외부 힘에 대한 순응적 반응도 필요로 합니다. 상당한 진전이 있었음에도 불구하고, 기존의 강화학습 접근법은 주로 강건성에 중점을 두어 외부 힘에 저항하는 정책을 생성하지만, 특히 본질적으로 불안정한 휴머노이드에게는 순응성이 부족하여 큰 도전 과제로 남아 있습니다. 본 연구에서는 휴머노이드 보행을 명령 추적과 외부 힘 순응 사이의 균형을 맞추는 다중 목표 최적화 문제로 정식화하여 이 문제를 해결합니다. 우리는 사용자가 지정한 선호도 입력을 통해 단일 전방향 보행 정책이 명령 추종과 힘 순응 사이에서 절충할 수 있도록 하는 선호도 조건부 다중 목표 강화학습(MORL) 프레임워크를 도입합니다. 외부 힘은 일관된 보상 설계를 위해 속도-저항 계수를 통해 모델링되며, 훈련은 배치 가능한 관측값에서 작업 관련 특권 특징을 추론하는 인코더-디코더 구조를 활용합니다. 우리는 휴머노이드 로봇을 대상으로 시뮬레이션과 실제 실험 모두에서 접근법을 검증합니다. 시뮬레이션 및 하드웨어 실험 결과는 프레임워크가 안정적으로 훈련되고 배치 가능한 선호도 조건부 휴머노이드 보행을 가능하게 함을 보여줍니다.

## 핵심 내용
휴머노이드 보행은 내비게이션을 위한 정확한 명령 추적뿐만 아니라 인간과의 상호작용 중 외부 힘에 대한 순응적 반응도 필요로 합니다. 상당한 진전이 있었음에도 불구하고, 기존의 강화학습 접근법은 주로 강건성에 중점을 두어 외부 힘에 저항하는 정책을 생성하지만, 특히 본질적으로 불안정한 휴머노이드에게는 순응성이 부족하여 큰 도전 과제로 남아 있습니다. 본 연구에서는 휴머노이드 보행을 명령 추적과 외부 힘 순응 사이의 균형을 맞추는 다중 목표 최적화 문제로 정식화하여 이 문제를 해결합니다. 우리는 사용자가 지정한 선호도 입력을 통해 단일 전방향 보행 정책이 명령 추종과 힘 순응 사이에서 절충할 수 있도록 하는 선호도 조건부 다중 목표 강화학습(MORL) 프레임워크를 도입합니다. 외부 힘은 일관된 보상 설계를 위해 속도-저항 계수를 통해 모델링되며, 훈련은 배치 가능한 관측값에서 작업 관련 특권 특징을 추론하는 인코더-디코더 구조를 활용합니다. 우리는 휴머노이드 로봇을 대상으로 시뮬레이션과 실제 실험 모두에서 접근법을 검증합니다. 시뮬레이션 및 하드웨어 실험 결과는 프레임워크가 안정적으로 훈련되고 배치 가능한 선호도 조건부 휴머노이드 보행을 가능하게 함을 보여줍니다.
