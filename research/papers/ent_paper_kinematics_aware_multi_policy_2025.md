---
$id: ent_paper_kinematics_aware_multi_policy_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Kinematics-Aware Multi-Policy Reinforcement Learning for Force-Capable Humanoid Loco-Manipulation
  zh: Kinematics-Aware Multi-Policy Reinforcement Learning for Force-Capable Humanoid Loco-Manipulation
  ko: Kinematics-Aware Multi-Policy Reinforcement Learning for Force-Capable Humanoid Loco-Manipulation
summary:
  en: Kinematics-Aware Multi-Policy Reinforcement Learning for Force-Capable Humanoid Loco-Manipulation is a 2025 work on
    loco-manipulation and whole-body-control for humanoid robots.
  zh: Kinematics-Aware Multi-Policy Reinforcement Learning for Force-Capable Humanoid Loco-Manipulation is a 2025 work on
    loco-manipulation and whole-body-control for humanoid robots.
  ko: Kinematics-Aware Multi-Policy Reinforcement Learning for Force-Capable Humanoid Loco-Manipulation is a 2025 work on
    loco-manipulation and whole-body-control for humanoid robots.
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
- kinematics_aware_multi_policy
- loco_manipulation
- whole_body_control
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2511.21169v1.
sources:
- id: src_001
  type: paper
  title: Kinematics-Aware Multi-Policy Reinforcement Learning for Force-Capable Humanoid Loco-Manipulation (arXiv)
  url: https://arxiv.org/abs/2511.21169
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Humanoid robots, with their human-like morphology, hold great potential for industrial applications. However, existing loco-manipulation methods primarily focus on dexterous manipulation, falling short of the combined requirements for dexterity and proactive force interaction in high-load industrial scenarios. To bridge this gap, we propose a reinforcement learning-based framework with a decoupled three-stage training pipeline, consisting of an upper-body policy, a lower-body policy, and a delta-command policy. To accelerate upper-body training, a heuristic reward function is designed. By implicitly embedding forward kinematics priors, it enables the policy to converge faster and achieve superior performance. For the lower body, a force-based curriculum learning strategy is developed, enabling the robot to actively exert and regulate interaction forces with the environment.

## 核心内容
Humanoid robots, with their human-like morphology, hold great potential for industrial applications. However, existing loco-manipulation methods primarily focus on dexterous manipulation, falling short of the combined requirements for dexterity and proactive force interaction in high-load industrial scenarios. To bridge this gap, we propose a reinforcement learning-based framework with a decoupled three-stage training pipeline, consisting of an upper-body policy, a lower-body policy, and a delta-command policy. To accelerate upper-body training, a heuristic reward function is designed. By implicitly embedding forward kinematics priors, it enables the policy to converge faster and achieve superior performance. For the lower body, a force-based curriculum learning strategy is developed, enabling the robot to actively exert and regulate interaction forces with the environment.

## 参考
- http://arxiv.org/abs/2511.21169v1

## Overview
Humanoid robots, with their human-like morphology, hold great potential for industrial applications. However, existing loco-manipulation methods primarily focus on dexterous manipulation, falling short of the combined requirements for dexterity and proactive force interaction in high-load industrial scenarios. To bridge this gap, we propose a reinforcement learning-based framework with a decoupled three-stage training pipeline, consisting of an upper-body policy, a lower-body policy, and a delta-command policy. To accelerate upper-body training, a heuristic reward function is designed. By implicitly embedding forward kinematics priors, it enables the policy to converge faster and achieve superior performance. For the lower body, a force-based curriculum learning strategy is developed, enabling the robot to actively exert and regulate interaction forces with the environment.

## Content
Humanoid robots, with their human-like morphology, hold great potential for industrial applications. However, existing loco-manipulation methods primarily focus on dexterous manipulation, falling short of the combined requirements for dexterity and proactive force interaction in high-load industrial scenarios. To bridge this gap, we propose a reinforcement learning-based framework with a decoupled three-stage training pipeline, consisting of an upper-body policy, a lower-body policy, and a delta-command policy. To accelerate upper-body training, a heuristic reward function is designed. By implicitly embedding forward kinematics priors, it enables the policy to converge faster and achieve superior performance. For the lower body, a force-based curriculum learning strategy is developed, enabling the robot to actively exert and regulate interaction forces with the environment.

## 개요
휴머노이드 로봇은 인간과 유사한 형태를 지니고 있어 산업 응용 분야에서 큰 잠재력을 가지고 있습니다. 그러나 기존의 이동-조작 방법은 주로 정밀 조작에 초점을 맞추고 있어, 고부하 산업 시나리오에서 요구되는 정밀성과 능동적인 힘 상호작용의 결합된 요구를 충족시키지 못합니다. 이러한 격차를 해소하기 위해, 우리는 상체 정책, 하체 정책, 델타 명령 정책으로 구성된 분리된 3단계 훈련 파이프라인을 갖춘 강화 학습 기반 프레임워크를 제안합니다. 상체 훈련을 가속화하기 위해 휴리스틱 보상 함수가 설계되었습니다. 순방향 운동학 사전 지식을 암시적으로 내장함으로써, 정책이 더 빠르게 수렴하고 우수한 성능을 달성할 수 있게 합니다. 하체의 경우, 로봇이 환경과의 상호작용 힘을 능동적으로 발휘하고 조절할 수 있도록 하는 힘 기반 커리큘럼 학습 전략이 개발되었습니다.

## 핵심 내용
휴머노이드 로봇은 인간과 유사한 형태를 지니고 있어 산업 응용 분야에서 큰 잠재력을 가지고 있습니다. 그러나 기존의 이동-조작 방법은 주로 정밀 조작에 초점을 맞추고 있어, 고부하 산업 시나리오에서 요구되는 정밀성과 능동적인 힘 상호작용의 결합된 요구를 충족시키지 못합니다. 이러한 격차를 해소하기 위해, 우리는 상체 정책, 하체 정책, 델타 명령 정책으로 구성된 분리된 3단계 훈련 파이프라인을 갖춘 강화 학습 기반 프레임워크를 제안합니다. 상체 훈련을 가속화하기 위해 휴리스틱 보상 함수가 설계되었습니다. 순방향 운동학 사전 지식을 암시적으로 내장함으로써, 정책이 더 빠르게 수렴하고 우수한 성능을 달성할 수 있게 합니다. 하체의 경우, 로봇이 환경과의 상호작용 힘을 능동적으로 발휘하고 조절할 수 있도록 하는 힘 기반 커리큘럼 학습 전략이 개발되었습니다.
