---
$id: ent_paper_reinforcement_learning_with_da_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Reinforcement Learning with Data Bootstrapping for Dynamic Subgoal Pursuit in Humanoid Robot Navigation
  zh: Reinforcement Learning with Data Bootstrapping for Dynamic Subgoal Pursuit in Humanoid Robot Navigation
  ko: Reinforcement Learning with Data Bootstrapping for Dynamic Subgoal Pursuit in Humanoid Robot Navigation
summary:
  en: Reinforcement Learning with Data Bootstrapping for Dynamic Subgoal Pursuit in Humanoid Robot Navigation is a paper on
    Navigation for humanoid robotics.
  zh: Reinforcement Learning with Data Bootstrapping for Dynamic Subgoal Pursuit in Humanoid Robot Navigation is a paper on
    Navigation for humanoid robotics.
  ko: Reinforcement Learning with Data Bootstrapping for Dynamic Subgoal Pursuit in Humanoid Robot Navigation is a paper on
    Navigation for humanoid robotics.
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
- navigation
- reinforcement_learning_with_da
theoretical_depth:
- system
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: low
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2506.02206v1.
sources:
- id: src_001
  type: website
  title: Reinforcement Learning with Data Bootstrapping for Dynamic Subgoal Pursuit in Humanoid Robot Navigation
  url: ''
  date: '2026'
  accessed_at: '2026-07-01'
---
## 概述
Safe and real-time navigation is fundamental for humanoid robot applications. However, existing bipedal robot navigation frameworks often struggle to balance computational efficiency with the precision required for stable locomotion. We propose a novel hierarchical framework that continuously generates dynamic subgoals to guide the robot through cluttered environments. Our method comprises a high-level reinforcement learning (RL) planner for subgoal selection in a robot-centric coordinate system and a low-level Model Predictive Control (MPC) based planner which produces robust walking gaits to reach these subgoals. To expedite and stabilize the training process, we incorporate a data bootstrapping technique that leverages a model-based navigation approach to generate a diverse, informative dataset. We validate our method in simulation using the Agility Robotics Digit humanoid across multiple scenarios with random obstacles. Results show that our framework significantly improves navigation success rates and adaptability compared to both the original model-based method and other learning-based methods.

## 核心内容
Safe and real-time navigation is fundamental for humanoid robot applications. However, existing bipedal robot navigation frameworks often struggle to balance computational efficiency with the precision required for stable locomotion. We propose a novel hierarchical framework that continuously generates dynamic subgoals to guide the robot through cluttered environments. Our method comprises a high-level reinforcement learning (RL) planner for subgoal selection in a robot-centric coordinate system and a low-level Model Predictive Control (MPC) based planner which produces robust walking gaits to reach these subgoals. To expedite and stabilize the training process, we incorporate a data bootstrapping technique that leverages a model-based navigation approach to generate a diverse, informative dataset. We validate our method in simulation using the Agility Robotics Digit humanoid across multiple scenarios with random obstacles. Results show that our framework significantly improves navigation success rates and adaptability compared to both the original model-based method and other learning-based methods.

## 参考
- http://arxiv.org/abs/2506.02206v1

## Overview
Safe and real-time navigation is fundamental for humanoid robot applications. However, existing bipedal robot navigation frameworks often struggle to balance computational efficiency with the precision required for stable locomotion. We propose a novel hierarchical framework that continuously generates dynamic subgoals to guide the robot through cluttered environments. Our method comprises a high-level reinforcement learning (RL) planner for subgoal selection in a robot-centric coordinate system and a low-level Model Predictive Control (MPC) based planner which produces robust walking gaits to reach these subgoals. To expedite and stabilize the training process, we incorporate a data bootstrapping technique that leverages a model-based navigation approach to generate a diverse, informative dataset. We validate our method in simulation using the Agility Robotics Digit humanoid across multiple scenarios with random obstacles. Results show that our framework significantly improves navigation success rates and adaptability compared to both the original model-based method and other learning-based methods.

## Content
Safe and real-time navigation is fundamental for humanoid robot applications. However, existing bipedal robot navigation frameworks often struggle to balance computational efficiency with the precision required for stable locomotion. We propose a novel hierarchical framework that continuously generates dynamic subgoals to guide the robot through cluttered environments. Our method comprises a high-level reinforcement learning (RL) planner for subgoal selection in a robot-centric coordinate system and a low-level Model Predictive Control (MPC) based planner which produces robust walking gaits to reach these subgoals. To expedite and stabilize the training process, we incorporate a data bootstrapping technique that leverages a model-based navigation approach to generate a diverse, informative dataset. We validate our method in simulation using the Agility Robotics Digit humanoid across multiple scenarios with random obstacles. Results show that our framework significantly improves navigation success rates and adaptability compared to both the original model-based method and other learning-based methods.

## 개요
안전하고 실시간 내비게이션은 인간형 로봇 응용 분야의 기본 요소입니다. 그러나 기존의 이족 보행 로봇 내비게이션 프레임워크는 안정적인 보행에 필요한 정밀도와 계산 효율성 사이의 균형을 맞추는 데 어려움을 겪는 경우가 많습니다. 본 논문에서는 혼잡한 환경에서 로봇을 안내하기 위해 동적 하위 목표를 지속적으로 생성하는 새로운 계층적 프레임워크를 제안합니다. 제안하는 방법은 로봇 중심 좌표계에서 하위 목표를 선택하기 위한 고수준 강화 학습(RL) 플래너와 이러한 하위 목표에 도달하기 위한 강건한 보행 패턴을 생성하는 저수준 모델 예측 제어(MPC) 기반 플래너로 구성됩니다. 훈련 과정을 가속화하고 안정화하기 위해 모델 기반 내비게이션 접근 방식을 활용하여 다양하고 정보가 풍부한 데이터셋을 생성하는 데이터 부트스트래핑 기법을 통합합니다. 무작위 장애물이 있는 여러 시나리오에서 Agility Robotics Digit 휴머노이드를 사용하여 시뮬레이션을 통해 제안하는 방법을 검증합니다. 결과는 제안하는 프레임워크가 기존 모델 기반 방법 및 다른 학습 기반 방법과 비교하여 내비게이션 성공률과 적응성을 크게 향상시킴을 보여줍니다.

## 핵심 내용
안전하고 실시간 내비게이션은 인간형 로봇 응용 분야의 기본 요소입니다. 그러나 기존의 이족 보행 로봇 내비게이션 프레임워크는 안정적인 보행에 필요한 정밀도와 계산 효율성 사이의 균형을 맞추는 데 어려움을 겪는 경우가 많습니다. 본 논문에서는 혼잡한 환경에서 로봇을 안내하기 위해 동적 하위 목표를 지속적으로 생성하는 새로운 계층적 프레임워크를 제안합니다. 제안하는 방법은 로봇 중심 좌표계에서 하위 목표를 선택하기 위한 고수준 강화 학습(RL) 플래너와 이러한 하위 목표에 도달하기 위한 강건한 보행 패턴을 생성하는 저수준 모델 예측 제어(MPC) 기반 플래너로 구성됩니다. 훈련 과정을 가속화하고 안정화하기 위해 모델 기반 내비게이션 접근 방식을 활용하여 다양하고 정보가 풍부한 데이터셋을 생성하는 데이터 부트스트래핑 기법을 통합합니다. 무작위 장애물이 있는 여러 시나리오에서 Agility Robotics Digit 휴머노이드를 사용하여 시뮬레이션을 통해 제안하는 방법을 검증합니다. 결과는 제안하는 프레임워크가 기존 모델 기반 방법 및 다른 학습 기반 방법과 비교하여 내비게이션 성공률과 적응성을 크게 향상시킴을 보여줍니다.
