---
$id: ent_paper_shield_safety_on_humanoids_via_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'SHIELD: Safety on Humanoids via CBFs In Expectation on Learned Dynamics'
  zh: 'SHIELD: Safety on Humanoids via CBFs In Expectation on Learned Dynamics'
  ko: 'SHIELD: Safety on Humanoids via CBFs In Expectation on Learned Dynamics'
summary:
  en: 'SHIELD: Safety on Humanoids via CBFs In Expectation on Learned Dynamics is a 2025 work on locomotion for humanoid robots.'
  zh: 'SHIELD: Safety on Humanoids via CBFs In Expectation on Learned Dynamics is a 2025 work on locomotion for humanoid robots.'
  ko: 'SHIELD: Safety on Humanoids via CBFs In Expectation on Learned Dynamics is a 2025 work on locomotion for humanoid robots.'
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
- shield
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2505.11494v3.
sources:
- id: src_001
  type: paper
  title: 'SHIELD: Safety on Humanoids via CBFs In Expectation on Learned Dynamics (arXiv)'
  url: https://arxiv.org/abs/2505.11494
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Robot learning has produced remarkably effective ``black-box'' controllers for complex tasks such as dynamic locomotion on humanoids. Yet ensuring dynamic safety, i.e., constraint satisfaction, remains challenging for such policies. Reinforcement learning (RL) embeds constraints heuristically through reward engineering, and adding or modifying constraints requires retraining. Model-based approaches, like control barrier functions (CBFs), enable runtime constraint specification with formal guarantees but require accurate dynamics models. This paper presents SHIELD, a layered safety framework that bridges this gap by: (1) training a generative, stochastic dynamics residual model using real-world data from hardware rollouts of the nominal controller, capturing system behavior and uncertainties; and (2) adding a safety layer on top of the nominal (learned locomotion) controller that leverages this model via a stochastic discrete-time CBF formulation enforcing safety constraints in probability. The result is a minimally-invasive safety layer that can be added to the existing autonomy stack to give probabilistic guarantees of safety that balance risk and performance. In hardware experiments on an Unitree G1 humanoid, SHIELD enables safe navigation (obstacle avoidance) through varied indoor and outdoor environments using a nominal (unknown) RL controller and onboard perception.

## 核心内容
Robot learning has produced remarkably effective ``black-box'' controllers for complex tasks such as dynamic locomotion on humanoids. Yet ensuring dynamic safety, i.e., constraint satisfaction, remains challenging for such policies. Reinforcement learning (RL) embeds constraints heuristically through reward engineering, and adding or modifying constraints requires retraining. Model-based approaches, like control barrier functions (CBFs), enable runtime constraint specification with formal guarantees but require accurate dynamics models. This paper presents SHIELD, a layered safety framework that bridges this gap by: (1) training a generative, stochastic dynamics residual model using real-world data from hardware rollouts of the nominal controller, capturing system behavior and uncertainties; and (2) adding a safety layer on top of the nominal (learned locomotion) controller that leverages this model via a stochastic discrete-time CBF formulation enforcing safety constraints in probability. The result is a minimally-invasive safety layer that can be added to the existing autonomy stack to give probabilistic guarantees of safety that balance risk and performance. In hardware experiments on an Unitree G1 humanoid, SHIELD enables safe navigation (obstacle avoidance) through varied indoor and outdoor environments using a nominal (unknown) RL controller and onboard perception.

## 参考
- http://arxiv.org/abs/2505.11494v3

## Overview
Robot learning has produced remarkably effective "black-box" controllers for complex tasks such as dynamic locomotion on humanoids. Yet ensuring dynamic safety, i.e., constraint satisfaction, remains challenging for such policies. Reinforcement learning (RL) embeds constraints heuristically through reward engineering, and adding or modifying constraints requires retraining. Model-based approaches, like control barrier functions (CBFs), enable runtime constraint specification with formal guarantees but require accurate dynamics models. This paper presents SHIELD, a layered safety framework that bridges this gap by: (1) training a generative, stochastic dynamics residual model using real-world data from hardware rollouts of the nominal controller, capturing system behavior and uncertainties; and (2) adding a safety layer on top of the nominal (learned locomotion) controller that leverages this model via a stochastic discrete-time CBF formulation enforcing safety constraints in probability. The result is a minimally-invasive safety layer that can be added to the existing autonomy stack to give probabilistic guarantees of safety that balance risk and performance. In hardware experiments on an Unitree G1 humanoid, SHIELD enables safe navigation (obstacle avoidance) through varied indoor and outdoor environments using a nominal (unknown) RL controller and onboard perception.

## Content
Robot learning has produced remarkably effective "black-box" controllers for complex tasks such as dynamic locomotion on humanoids. Yet ensuring dynamic safety, i.e., constraint satisfaction, remains challenging for such policies. Reinforcement learning (RL) embeds constraints heuristically through reward engineering, and adding or modifying constraints requires retraining. Model-based approaches, like control barrier functions (CBFs), enable runtime constraint specification with formal guarantees but require accurate dynamics models. This paper presents SHIELD, a layered safety framework that bridges this gap by: (1) training a generative, stochastic dynamics residual model using real-world data from hardware rollouts of the nominal controller, capturing system behavior and uncertainties; and (2) adding a safety layer on top of the nominal (learned locomotion) controller that leverages this model via a stochastic discrete-time CBF formulation enforcing safety constraints in probability. The result is a minimally-invasive safety layer that can be added to the existing autonomy stack to give probabilistic guarantees of safety that balance risk and performance. In hardware experiments on an Unitree G1 humanoid, SHIELD enables safe navigation (obstacle avoidance) through varied indoor and outdoor environments using a nominal (unknown) RL controller and onboard perception.

## 개요
로봇 학습은 휴머노이드의 동적 보행과 같은 복잡한 작업에 대해 매우 효과적인 '블랙박스' 제어기를 생성해 왔습니다. 그러나 동적 안전, 즉 제약 조건 충족을 보장하는 것은 이러한 정책에 있어 여전히 어려운 과제입니다. 강화 학습(RL)은 보상 엔지니어링을 통해 경험적으로 제약 조건을 포함시키며, 제약 조건을 추가하거나 수정하려면 재학습이 필요합니다. 제어 장벽 함수(CBF)와 같은 모델 기반 접근 방식은 런타임 제약 조건 명세를 공식적인 보장과 함께 가능하게 하지만 정확한 동역학 모델을 필요로 합니다. 본 논문은 SHIELD를 제시합니다. 이는 계층적 안전 프레임워크로, 다음을 통해 이러한 격차를 해소합니다: (1) 공칭 제어기의 하드웨어 롤아웃에서 얻은 실제 데이터를 사용하여 생성적이고 확률적인 동역학 잔차 모델을 훈련하여 시스템 동작과 불확실성을 포착하고; (2) 공칭(학습된 보행) 제어기 위에 안전 계층을 추가하여 확률적 이산 시간 CBF 공식을 통해 이 모델을 활용, 확률적으로 안전 제약 조건을 강제합니다. 그 결과는 기존 자율 주행 스택에 추가되어 위험과 성능의 균형을 맞추는 확률적 안전 보장을 제공하는 최소 침습적 안전 계층입니다. Unitree G1 휴머노이드의 하드웨어 실험에서 SHIELD는 공칭(알려지지 않은) RL 제어기와 온보드 인식을 사용하여 다양한 실내 및 실외 환경에서 안전한 탐색(장애물 회피)을 가능하게 합니다.

## 핵심 내용
로봇 학습은 휴머노이드의 동적 보행과 같은 복잡한 작업에 대해 매우 효과적인 '블랙박스' 제어기를 생성해 왔습니다. 그러나 동적 안전, 즉 제약 조건 충족을 보장하는 것은 이러한 정책에 있어 여전히 어려운 과제입니다. 강화 학습(RL)은 보상 엔지니어링을 통해 경험적으로 제약 조건을 포함시키며, 제약 조건을 추가하거나 수정하려면 재학습이 필요합니다. 제어 장벽 함수(CBF)와 같은 모델 기반 접근 방식은 런타임 제약 조건 명세를 공식적인 보장과 함께 가능하게 하지만 정확한 동역학 모델을 필요로 합니다. 본 논문은 SHIELD를 제시합니다. 이는 계층적 안전 프레임워크로, 다음을 통해 이러한 격차를 해소합니다: (1) 공칭 제어기의 하드웨어 롤아웃에서 얻은 실제 데이터를 사용하여 생성적이고 확률적인 동역학 잔차 모델을 훈련하여 시스템 동작과 불확실성을 포착하고; (2) 공칭(학습된 보행) 제어기 위에 안전 계층을 추가하여 확률적 이산 시간 CBF 공식을 통해 이 모델을 활용, 확률적으로 안전 제약 조건을 강제합니다. 그 결과는 기존 자율 주행 스택에 추가되어 위험과 성능의 균형을 맞추는 확률적 안전 보장을 제공하는 최소 침습적 안전 계층입니다. Unitree G1 휴머노이드의 하드웨어 실험에서 SHIELD는 공칭(알려지지 않은) RL 제어기와 온보드 인식을 사용하여 다양한 실내 및 실외 환경에서 안전한 탐색(장애물 회피)을 가능하게 합니다.
