---
$id: ent_paper_real_world_humanoid_locomotion_2023
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Real-World Humanoid Locomotion with Reinforcement Learning
  zh: Real-World Humanoid Locomotion with Reinforcement Learning
  ko: Real-World Humanoid Locomotion with Reinforcement Learning
summary:
  en: Real-World Humanoid Locomotion with Reinforcement Learning is a 2023 work on locomotion for humanoid robots.
  zh: Real-World Humanoid Locomotion with Reinforcement Learning is a 2023 work on locomotion for humanoid robots.
  ko: Real-World Humanoid Locomotion with Reinforcement Learning is a 2023 work on locomotion for humanoid robots.
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
- real_world_humanoid_locomotion
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2303.03381v2.
sources:
- id: src_001
  type: paper
  title: Real-World Humanoid Locomotion with Reinforcement Learning (arXiv)
  url: https://arxiv.org/abs/2303.03381
  date: '2023'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: Real-World Humanoid Locomotion with Reinforcement Learning project page
  url: https://learning-humanoid-locomotion.github.io/
  date: '2023'
  accessed_at: '2026-07-01'
---
## 概述
Humanoid robots that can autonomously operate in diverse environments have the potential to help address labour shortages in factories, assist elderly at homes, and colonize new planets. While classical controllers for humanoid robots have shown impressive results in a number of settings, they are challenging to generalize and adapt to new environments. Here, we present a fully learning-based approach for real-world humanoid locomotion. Our controller is a causal transformer that takes the history of proprioceptive observations and actions as input and predicts the next action. We hypothesize that the observation-action history contains useful information about the world that a powerful transformer model can use to adapt its behavior in-context, without updating its weights. We train our model with large-scale model-free reinforcement learning on an ensemble of randomized environments in simulation and deploy it to the real world zero-shot. Our controller can walk over various outdoor terrains, is robust to external disturbances, and can adapt in context.

## 核心内容
Humanoid robots that can autonomously operate in diverse environments have the potential to help address labour shortages in factories, assist elderly at homes, and colonize new planets. While classical controllers for humanoid robots have shown impressive results in a number of settings, they are challenging to generalize and adapt to new environments. Here, we present a fully learning-based approach for real-world humanoid locomotion. Our controller is a causal transformer that takes the history of proprioceptive observations and actions as input and predicts the next action. We hypothesize that the observation-action history contains useful information about the world that a powerful transformer model can use to adapt its behavior in-context, without updating its weights. We train our model with large-scale model-free reinforcement learning on an ensemble of randomized environments in simulation and deploy it to the real world zero-shot. Our controller can walk over various outdoor terrains, is robust to external disturbances, and can adapt in context.

## 参考
- http://arxiv.org/abs/2303.03381v2

## Overview
Humanoid robots that can autonomously operate in diverse environments have the potential to help address labour shortages in factories, assist elderly at homes, and colonize new planets. While classical controllers for humanoid robots have shown impressive results in a number of settings, they are challenging to generalize and adapt to new environments. Here, we present a fully learning-based approach for real-world humanoid locomotion. Our controller is a causal transformer that takes the history of proprioceptive observations and actions as input and predicts the next action. We hypothesize that the observation-action history contains useful information about the world that a powerful transformer model can use to adapt its behavior in-context, without updating its weights. We train our model with large-scale model-free reinforcement learning on an ensemble of randomized environments in simulation and deploy it to the real world zero-shot. Our controller can walk over various outdoor terrains, is robust to external disturbances, and can adapt in context.

## Content
Humanoid robots that can autonomously operate in diverse environments have the potential to help address labour shortages in factories, assist elderly at homes, and colonize new planets. While classical controllers for humanoid robots have shown impressive results in a number of settings, they are challenging to generalize and adapt to new environments. Here, we present a fully learning-based approach for real-world humanoid locomotion. Our controller is a causal transformer that takes the history of proprioceptive observations and actions as input and predicts the next action. We hypothesize that the observation-action history contains useful information about the world that a powerful transformer model can use to adapt its behavior in-context, without updating its weights. We train our model with large-scale model-free reinforcement learning on an ensemble of randomized environments in simulation and deploy it to the real world zero-shot. Our controller can walk over various outdoor terrains, is robust to external disturbances, and can adapt in context.

## 개요
다양한 환경에서 자율적으로 작동할 수 있는 휴머노이드 로봇은 공장의 노동력 부족 해소, 가정에서의 노인 지원, 새로운 행성 개척에 기여할 잠재력을 가지고 있습니다. 휴머노이드 로봇을 위한 기존 제어기는 여러 환경에서 인상적인 결과를 보여주었지만, 새로운 환경에 일반화하고 적응하는 데 어려움이 있습니다. 본 연구에서는 실제 환경에서의 휴머노이드 보행을 위한 완전 학습 기반 접근법을 제시합니다. 우리의 제어기는 인과적 트랜스포머로, 고유수용성 관측과 행동의 이력을 입력으로 받아 다음 행동을 예측합니다. 우리는 관측-행동 이력에 세계에 대한 유용한 정보가 포함되어 있으며, 강력한 트랜스포머 모델이 가중치를 업데이트하지 않고도 맥락 내에서 행동을 적응시키는 데 사용할 수 있다고 가정합니다. 우리는 시뮬레이션에서 무작위화된 환경 집합에 대해 대규모 모델 프리 강화 학습으로 모델을 훈련하고, 제로샷으로 실제 환경에 배포합니다. 우리의 제어기는 다양한 야외 지형을 걸을 수 있고, 외부 교란에 강하며, 맥락 내에서 적응할 수 있습니다.

## 핵심 내용
다양한 환경에서 자율적으로 작동할 수 있는 휴머노이드 로봇은 공장의 노동력 부족 해소, 가정에서의 노인 지원, 새로운 행성 개척에 기여할 잠재력을 가지고 있습니다. 휴머노이드 로봇을 위한 기존 제어기는 여러 환경에서 인상적인 결과를 보여주었지만, 새로운 환경에 일반화하고 적응하는 데 어려움이 있습니다. 본 연구에서는 실제 환경에서의 휴머노이드 보행을 위한 완전 학습 기반 접근법을 제시합니다. 우리의 제어기는 인과적 트랜스포머로, 고유수용성 관측과 행동의 이력을 입력으로 받아 다음 행동을 예측합니다. 우리는 관측-행동 이력에 세계에 대한 유용한 정보가 포함되어 있으며, 강력한 트랜스포머 모델이 가중치를 업데이트하지 않고도 맥락 내에서 행동을 적응시키는 데 사용할 수 있다고 가정합니다. 우리는 시뮬레이션에서 무작위화된 환경 집합에 대해 대규모 모델 프리 강화 학습으로 모델을 훈련하고, 제로샷으로 실제 환경에 배포합니다. 우리의 제어기는 다양한 야외 지형을 걸을 수 있고, 외부 교란에 강하며, 맥락 내에서 적응할 수 있습니다.
