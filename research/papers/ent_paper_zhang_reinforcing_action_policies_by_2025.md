---
$id: ent_paper_zhang_reinforcing_action_policies_by_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Reinforcing Action Policies by Prophesying
  zh: Prophet
  ko: Reinforcing Action Policies by Prophesying
summary:
  en: Reinforcing Action Policies by Prophesying (Prophet), is a 2025 large vision-language-action model for robotic manipulation,
    introduced by Fudan University, Shanghai Innovation Institute, Logos Robotics.
  zh: Reinforcing Action Policies by Prophesying (Prophet), is a 2025 large vision-language-action model for robotic manipulation,
    introduced by Fudan University, Shanghai Innovation Institute, Logos Robotics.
  ko: Reinforcing Action Policies by Prophesying (Prophet), is a 2025 large vision-language-action model for robotic manipulation,
    introduced by Fudan University, Shanghai Innovation Institute, Logos Robotics.
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- large_vla_model
- prophet
- robotic_manipulation
- vision_language_action
- vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2511.20633v1.
sources:
- id: src_001
  type: paper
  title: Reinforcing Action Policies by Prophesying (arXiv)
  url: https://arxiv.org/abs/2511.20633
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: Prophet source
  url: https://doi.org/10.48550/arXiv.2511.20633
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Vision-Language-Action (VLA) policies excel in aligning language, perception, and robot control. However, most VLAs are trained purely by imitation, which overfits to demonstrations, and is brittle under distribution shift. Reinforcement learning (RL) directly optimizes task reward and thus addresses this misalignment, but real-robot interaction is expensive and conventional simulators are hard to engineer and transfer. We address both data efficiency and optimization stability in VLA post-training via a learned world model and an RL procedure tailored to flow-based action heads. Specifically, we introduce Prophet, a unified action-to-video robot actuation pretrained across large-scale, heterogeneous robot data to learn reusable action-outcome dynamics. It is able to few-shot adapt to new robots, objects, and environments, yielding a rollout-ready simulator. Upon Prophet, we reinforce action policies with Flow-action-GRPO (FA-GRPO), which adapts Flow-GRPO to operate on VLA actions, and with FlowScale, a stepwise reweighting that rescales per-step gradients in the flow head. Together, Prophet, FA-GRPO, and FlowScale constitute ProphRL, a practical, data- and compute-efficient path to VLA post-training. Experiments show 5-17% success gains on public benchmarks and 24-30% gains on real robots across different VLA variants.

## 核心内容
Vision-Language-Action (VLA) policies excel in aligning language, perception, and robot control. However, most VLAs are trained purely by imitation, which overfits to demonstrations, and is brittle under distribution shift. Reinforcement learning (RL) directly optimizes task reward and thus addresses this misalignment, but real-robot interaction is expensive and conventional simulators are hard to engineer and transfer. We address both data efficiency and optimization stability in VLA post-training via a learned world model and an RL procedure tailored to flow-based action heads. Specifically, we introduce Prophet, a unified action-to-video robot actuation pretrained across large-scale, heterogeneous robot data to learn reusable action-outcome dynamics. It is able to few-shot adapt to new robots, objects, and environments, yielding a rollout-ready simulator. Upon Prophet, we reinforce action policies with Flow-action-GRPO (FA-GRPO), which adapts Flow-GRPO to operate on VLA actions, and with FlowScale, a stepwise reweighting that rescales per-step gradients in the flow head. Together, Prophet, FA-GRPO, and FlowScale constitute ProphRL, a practical, data- and compute-efficient path to VLA post-training. Experiments show 5-17% success gains on public benchmarks and 24-30% gains on real robots across different VLA variants.

## 参考
- http://arxiv.org/abs/2511.20633v1

## Overview
Vision-Language-Action (VLA) policies excel in aligning language, perception, and robot control. However, most VLAs are trained purely by imitation, which overfits to demonstrations, and is brittle under distribution shift. Reinforcement learning (RL) directly optimizes task reward and thus addresses this misalignment, but real-robot interaction is expensive and conventional simulators are hard to engineer and transfer. We address both data efficiency and optimization stability in VLA post-training via a learned world model and an RL procedure tailored to flow-based action heads. Specifically, we introduce Prophet, a unified action-to-video robot actuation pretrained across large-scale, heterogeneous robot data to learn reusable action-outcome dynamics. It is able to few-shot adapt to new robots, objects, and environments, yielding a rollout-ready simulator. Upon Prophet, we reinforce action policies with Flow-action-GRPO (FA-GRPO), which adapts Flow-GRPO to operate on VLA actions, and with FlowScale, a stepwise reweighting that rescales per-step gradients in the flow head. Together, Prophet, FA-GRPO, and FlowScale constitute ProphRL, a practical, data- and compute-efficient path to VLA post-training. Experiments show 5-17% success gains on public benchmarks and 24-30% gains on real robots across different VLA variants.

## Content
Vision-Language-Action (VLA) policies excel in aligning language, perception, and robot control. However, most VLAs are trained purely by imitation, which overfits to demonstrations, and is brittle under distribution shift. Reinforcement learning (RL) directly optimizes task reward and thus addresses this misalignment, but real-robot interaction is expensive and conventional simulators are hard to engineer and transfer. We address both data efficiency and optimization stability in VLA post-training via a learned world model and an RL procedure tailored to flow-based action heads. Specifically, we introduce Prophet, a unified action-to-video robot actuation pretrained across large-scale, heterogeneous robot data to learn reusable action-outcome dynamics. It is able to few-shot adapt to new robots, objects, and environments, yielding a rollout-ready simulator. Upon Prophet, we reinforce action policies with Flow-action-GRPO (FA-GRPO), which adapts Flow-GRPO to operate on VLA actions, and with FlowScale, a stepwise reweighting that rescales per-step gradients in the flow head. Together, Prophet, FA-GRPO, and FlowScale constitute ProphRL, a practical, data- and compute-efficient path to VLA post-training. Experiments show 5-17% success gains on public benchmarks and 24-30% gains on real robots across different VLA variants.

## 개요
Vision-Language-Action (VLA) 정책은 언어, 인식 및 로봇 제어를 정렬하는 데 탁월합니다. 그러나 대부분의 VLA는 순수한 모방 학습으로 훈련되어 시연에 과적합되고 분포 변화에 취약합니다. 강화 학습(RL)은 작업 보상을 직접 최적화하여 이러한 정렬 문제를 해결하지만, 실제 로봇 상호작용은 비용이 많이 들고 기존 시뮬레이터는 엔지니어링 및 전송이 어렵습니다. 우리는 학습된 세계 모델과 흐름 기반 행동 헤드에 맞춤화된 RL 절차를 통해 VLA 사후 훈련에서 데이터 효율성과 최적화 안정성을 모두 해결합니다. 구체적으로, 우리는 Prophet을 소개합니다. 이는 대규모 이기종 로봇 데이터에 걸쳐 사전 훈련된 통합된 행동-비디오 로봇 구동 모델로, 재사용 가능한 행동-결과 역학을 학습합니다. 이는 새로운 로봇, 객체 및 환경에 소수 샷 적응이 가능하여 롤아웃 준비가 된 시뮬레이터를 제공합니다. Prophet 위에서, 우리는 Flow-action-GRPO (FA-GRPO)를 사용하여 행동 정책을 강화합니다. 이는 Flow-GRPO를 VLA 행동에 적용하도록 조정하며, FlowScale은 흐름 헤드에서 단계별 그래디언트를 재조정하는 단계별 재가중치입니다. Prophet, FA-GRPO 및 FlowScale은 함께 ProphRL을 구성하며, 이는 VLA 사후 훈련을 위한 실용적이고 데이터 및 계산 효율적인 경로입니다. 실험 결과, 공개 벤치마크에서 5-17%의 성공률 향상과 다양한 VLA 변형에 걸쳐 실제 로봇에서 24-30%의 향상을 보여줍니다.

## 핵심 내용
Vision-Language-Action (VLA) 정책은 언어, 인식 및 로봇 제어를 정렬하는 데 탁월합니다. 그러나 대부분의 VLA는 순수한 모방 학습으로 훈련되어 시연에 과적합되고 분포 변화에 취약합니다. 강화 학습(RL)은 작업 보상을 직접 최적화하여 이러한 정렬 문제를 해결하지만, 실제 로봇 상호작용은 비용이 많이 들고 기존 시뮬레이터는 엔지니어링 및 전송이 어렵습니다. 우리는 학습된 세계 모델과 흐름 기반 행동 헤드에 맞춤화된 RL 절차를 통해 VLA 사후 훈련에서 데이터 효율성과 최적화 안정성을 모두 해결합니다. 구체적으로, 우리는 Prophet을 소개합니다. 이는 대규모 이기종 로봇 데이터에 걸쳐 사전 훈련된 통합된 행동-비디오 로봇 구동 모델로, 재사용 가능한 행동-결과 역학을 학습합니다. 이는 새로운 로봇, 객체 및 환경에 소수 샷 적응이 가능하여 롤아웃 준비가 된 시뮬레이터를 제공합니다. Prophet 위에서, 우리는 Flow-action-GRPO (FA-GRPO)를 사용하여 행동 정책을 강화합니다. 이는 Flow-GRPO를 VLA 행동에 적용하도록 조정하며, FlowScale은 흐름 헤드에서 단계별 그래디언트를 재조정하는 단계별 재가중치입니다. Prophet, FA-GRPO 및 FlowScale은 함께 ProphRL을 구성하며, 이는 VLA 사후 훈련을 위한 실용적이고 데이터 및 계산 효율적인 경로입니다. 실험 결과, 공개 벤치마크에서 5-17%의 성공률 향상과 다양한 VLA 변형에 걸쳐 실제 로봇에서 24-30%의 향상을 보여줍니다.
