---
$id: ent_paper_more_mixture_of_residual_exper_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'MoRE: Mixture of Residual Experts for Humanoid Lifelike Gaits Learning on Complex Terrains'
  zh: 'MoRE: Mixture of Residual Experts for Humanoid Lifelike Gaits Learning on Complex Terrains'
  ko: 'MoRE: Mixture of Residual Experts for Humanoid Lifelike Gaits Learning on Complex Terrains'
summary:
  en: 'MoRE: Mixture of Residual Experts for Humanoid Lifelike Gaits Learning on Complex Terrains is a 2025 work on locomotion
    for humanoid robots.'
  zh: 'MoRE: Mixture of Residual Experts for Humanoid Lifelike Gaits Learning on Complex Terrains is a 2025 work on locomotion
    for humanoid robots.'
  ko: 'MoRE: Mixture of Residual Experts for Humanoid Lifelike Gaits Learning on Complex Terrains is a 2025 work on locomotion
    for humanoid robots.'
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
- more
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2506.08840v2.
sources:
- id: src_001
  type: paper
  title: 'MoRE: Mixture of Residual Experts for Humanoid Lifelike Gaits Learning on Complex Terrains (arXiv)'
  url: https://arxiv.org/abs/2506.08840
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: 'MoRE: Mixture of Residual Experts for Humanoid Lifelike Gaits Learning on Complex Terrains project page'
  url: https://more-humanoid.github.io/
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Humanoid robots have demonstrated robust locomotion capabilities using Reinforcement Learning (RL)-based approaches. Further, to obtain human-like behaviors, existing methods integrate human motion-tracking or motion prior in the RL framework. However, these methods are limited in flat terrains with proprioception only, restricting their abilities to traverse challenging terrains with human-like gaits. In this work, we propose a novel framework using a mixture of latent residual experts with multi-discriminators to train an RL policy, which is capable of traversing complex terrains in controllable lifelike gaits with exteroception. Our two-stage training pipeline first teaches the policy to traverse complex terrains using a depth camera, and then enables gait-commanded switching between human-like gait patterns. We also design gait rewards to adjust human-like behaviors like robot base height. Simulation and real-world experiments demonstrate that our framework exhibits exceptional performance in traversing complex terrains, and achieves seamless transitions between multiple human-like gait patterns.

## 核心内容
Humanoid robots have demonstrated robust locomotion capabilities using Reinforcement Learning (RL)-based approaches. Further, to obtain human-like behaviors, existing methods integrate human motion-tracking or motion prior in the RL framework. However, these methods are limited in flat terrains with proprioception only, restricting their abilities to traverse challenging terrains with human-like gaits. In this work, we propose a novel framework using a mixture of latent residual experts with multi-discriminators to train an RL policy, which is capable of traversing complex terrains in controllable lifelike gaits with exteroception. Our two-stage training pipeline first teaches the policy to traverse complex terrains using a depth camera, and then enables gait-commanded switching between human-like gait patterns. We also design gait rewards to adjust human-like behaviors like robot base height. Simulation and real-world experiments demonstrate that our framework exhibits exceptional performance in traversing complex terrains, and achieves seamless transitions between multiple human-like gait patterns.

## 参考
- http://arxiv.org/abs/2506.08840v2

## Overview
Humanoid robots have demonstrated robust locomotion capabilities using Reinforcement Learning (RL)-based approaches. Further, to obtain human-like behaviors, existing methods integrate human motion-tracking or motion prior in the RL framework. However, these methods are limited in flat terrains with proprioception only, restricting their abilities to traverse challenging terrains with human-like gaits. In this work, we propose a novel framework using a mixture of latent residual experts with multi-discriminators to train an RL policy, which is capable of traversing complex terrains in controllable lifelike gaits with exteroception. Our two-stage training pipeline first teaches the policy to traverse complex terrains using a depth camera, and then enables gait-commanded switching between human-like gait patterns. We also design gait rewards to adjust human-like behaviors like robot base height. Simulation and real-world experiments demonstrate that our framework exhibits exceptional performance in traversing complex terrains, and achieves seamless transitions between multiple human-like gait patterns.

## Content
Humanoid robots have demonstrated robust locomotion capabilities using Reinforcement Learning (RL)-based approaches. Further, to obtain human-like behaviors, existing methods integrate human motion-tracking or motion prior in the RL framework. However, these methods are limited in flat terrains with proprioception only, restricting their abilities to traverse challenging terrains with human-like gaits. In this work, we propose a novel framework using a mixture of latent residual experts with multi-discriminators to train an RL policy, which is capable of traversing complex terrains in controllable lifelike gaits with exteroception. Our two-stage training pipeline first teaches the policy to traverse complex terrains using a depth camera, and then enables gait-commanded switching between human-like gait patterns. We also design gait rewards to adjust human-like behaviors like robot base height. Simulation and real-world experiments demonstrate that our framework exhibits exceptional performance in traversing complex terrains, and achieves seamless transitions between multiple human-like gait patterns.

## 개요
휴머노이드 로봇은 강화 학습(RL) 기반 접근법을 통해 강건한 보행 능력을 입증해 왔습니다. 또한, 인간과 유사한 행동을 얻기 위해 기존 방법들은 RL 프레임워크에 인간 동작 추적 또는 동작 사전 정보를 통합합니다. 그러나 이러한 방법들은 고유 감각만을 사용하는 평지 지형으로 제한되어, 인간과 유사한 보행으로 도전적인 지형을 횡단하는 능력을 제약합니다. 본 연구에서는 다중 판별기를 갖춘 잠재 잔차 전문가 혼합을 사용하여 외부 감각을 통해 제어 가능한 생생한 보행으로 복잡한 지형을 횡단할 수 있는 RL 정책을 훈련하는 새로운 프레임워크를 제안합니다. 우리의 2단계 훈련 파이프라인은 먼저 깊이 카메라를 사용하여 복잡한 지형을 횡단하도록 정책을 가르친 후, 보행 명령을 통해 인간과 유사한 보행 패턴 간 전환을 가능하게 합니다. 또한 로봇 베이스 높이와 같은 인간과 유사한 행동을 조정하기 위한 보행 보상을 설계합니다. 시뮬레이션 및 실제 실험을 통해 우리의 프레임워크가 복잡한 지형 횡단에서 뛰어난 성능을 보이며, 여러 인간과 유사한 보행 패턴 간 원활한 전환을 달성함을 입증합니다.

## 핵심 내용
휴머노이드 로봇은 강화 학습(RL) 기반 접근법을 통해 강건한 보행 능력을 입증해 왔습니다. 또한, 인간과 유사한 행동을 얻기 위해 기존 방법들은 RL 프레임워크에 인간 동작 추적 또는 동작 사전 정보를 통합합니다. 그러나 이러한 방법들은 고유 감각만을 사용하는 평지 지형으로 제한되어, 인간과 유사한 보행으로 도전적인 지형을 횡단하는 능력을 제약합니다. 본 연구에서는 다중 판별기를 갖춘 잠재 잔차 전문가 혼합을 사용하여 외부 감각을 통해 제어 가능한 생생한 보행으로 복잡한 지형을 횡단할 수 있는 RL 정책을 훈련하는 새로운 프레임워크를 제안합니다. 우리의 2단계 훈련 파이프라인은 먼저 깊이 카메라를 사용하여 복잡한 지형을 횡단하도록 정책을 가르친 후, 보행 명령을 통해 인간과 유사한 보행 패턴 간 전환을 가능하게 합니다. 또한 로봇 베이스 높이와 같은 인간과 유사한 행동을 조정하기 위한 보행 보상을 설계합니다. 시뮬레이션 및 실제 실험을 통해 우리의 프레임워크가 복잡한 지형 횡단에서 뛰어난 성능을 보이며, 여러 인간과 유사한 보행 패턴 간 원활한 전환을 달성함을 입증합니다.
