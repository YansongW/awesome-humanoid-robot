---
$id: ent_paper_jiang_irl_vla_training_an_vision_lan_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'IRL-VLA: Training an Vision-Language-Action Policy via Reward World Model'
  zh: IRL-VLA
  ko: 'IRL-VLA: Training an Vision-Language-Action Policy via Reward World Model'
summary:
  en: 'IRL-VLA: Training an Vision-Language-Action Policy via Reward World Model (IRL-VLA), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Bosch Corporate Research, School of Communication and Information Engineering,
    Shanghai University, School of Mechanical Engineering, Shanghai Jiao Tong University, Bosch Mobility Solutions, Robert
    Bosch GmbH, AIR, Tsinghua University.'
  zh: 'IRL-VLA: Training an Vision-Language-Action Policy via Reward World Model (IRL-VLA), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Bosch Corporate Research, School of Communication and Information Engineering,
    Shanghai University, School of Mechanical Engineering, Shanghai Jiao Tong University, Bosch Mobility Solutions, Robert
    Bosch GmbH, AIR, Tsinghua University.'
  ko: 'IRL-VLA: Training an Vision-Language-Action Policy via Reward World Model (IRL-VLA), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Bosch Corporate Research, School of Communication and Information Engineering,
    Shanghai University, School of Mechanical Engineering, Shanghai Jiao Tong University, Bosch Mobility Solutions, Robert
    Bosch GmbH, AIR, Tsinghua University.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- irl_vla
- large_vla_model
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2508.06571v3.
sources:
- id: src_001
  type: paper
  title: 'IRL-VLA: Training an Vision-Language-Action Policy via Reward World Model (arXiv)'
  url: https://arxiv.org/abs/2508.06571
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: IRL-VLA source
  url: https://doi.org/10.48550/arXiv.2508.06571
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Vision-Language-Action (VLA) models have demonstrated potential in autonomous driving. However, two critical challenges hinder their development: (1) Existing VLA architectures are typically based on imitation learning in open-loop setup which tends to capture the recorded behaviors in the dataset, leading to suboptimal and constrained performance, (2) Close-loop training relies heavily on high-fidelity sensor simulation, where domain gaps and computational inefficiencies pose significant barriers. In this paper, we introduce IRL-VLA, a novel close-loop Reinforcement Learning via \textbf{I}nverse \textbf{R}einforcement \textbf{L}earning reward world model with a self-built VLA approach. Our framework proceeds in a three-stage paradigm: In the first stage, we propose a VLA architecture and pretrain the VLA policy via imitation learning. In the second stage, we construct a lightweight reward world model via inverse reinforcement learning to enable efficient close-loop reward computation. To further enhance planning performance, finally, we design specialized reward world model guidence reinforcement learning via PPO(Proximal Policy Optimization) to effectively balance the safety incidents, comfortable driving, and traffic efficiency. Our approach achieves state-of-the-art performance in NAVSIM v2 end-to-end driving benchmark, 1st runner up in CVPR2025 Autonomous Grand Challenge. We hope that our framework will accelerate VLA research in close-loop autonomous driving.

## 核心内容
Vision-Language-Action (VLA) models have demonstrated potential in autonomous driving. However, two critical challenges hinder their development: (1) Existing VLA architectures are typically based on imitation learning in open-loop setup which tends to capture the recorded behaviors in the dataset, leading to suboptimal and constrained performance, (2) Close-loop training relies heavily on high-fidelity sensor simulation, where domain gaps and computational inefficiencies pose significant barriers. In this paper, we introduce IRL-VLA, a novel close-loop Reinforcement Learning via \textbf{I}nverse \textbf{R}einforcement \textbf{L}earning reward world model with a self-built VLA approach. Our framework proceeds in a three-stage paradigm: In the first stage, we propose a VLA architecture and pretrain the VLA policy via imitation learning. In the second stage, we construct a lightweight reward world model via inverse reinforcement learning to enable efficient close-loop reward computation. To further enhance planning performance, finally, we design specialized reward world model guidence reinforcement learning via PPO(Proximal Policy Optimization) to effectively balance the safety incidents, comfortable driving, and traffic efficiency. Our approach achieves state-of-the-art performance in NAVSIM v2 end-to-end driving benchmark, 1st runner up in CVPR2025 Autonomous Grand Challenge. We hope that our framework will accelerate VLA research in close-loop autonomous driving.

## 参考
- http://arxiv.org/abs/2508.06571v3

## Overview
Vision-Language-Action (VLA) models have demonstrated potential in autonomous driving. However, two critical challenges hinder their development: (1) Existing VLA architectures are typically based on imitation learning in open-loop setup which tends to capture the recorded behaviors in the dataset, leading to suboptimal and constrained performance, (2) Close-loop training relies heavily on high-fidelity sensor simulation, where domain gaps and computational inefficiencies pose significant barriers. In this paper, we introduce IRL-VLA, a novel close-loop Reinforcement Learning via **I**nverse **R**einforcement **L**earning reward world model with a self-built VLA approach. Our framework proceeds in a three-stage paradigm: In the first stage, we propose a VLA architecture and pretrain the VLA policy via imitation learning. In the second stage, we construct a lightweight reward world model via inverse reinforcement learning to enable efficient close-loop reward computation. To further enhance planning performance, finally, we design specialized reward world model guidance reinforcement learning via PPO (Proximal Policy Optimization) to effectively balance safety incidents, comfortable driving, and traffic efficiency. Our approach achieves state-of-the-art performance in the NAVSIM v2 end-to-end driving benchmark, 1st runner up in CVPR2025 Autonomous Grand Challenge. We hope that our framework will accelerate VLA research in close-loop autonomous driving.

## Content
Vision-Language-Action (VLA) models have demonstrated potential in autonomous driving. However, two critical challenges hinder their development: (1) Existing VLA architectures are typically based on imitation learning in open-loop setup which tends to capture the recorded behaviors in the dataset, leading to suboptimal and constrained performance, (2) Close-loop training relies heavily on high-fidelity sensor simulation, where domain gaps and computational inefficiencies pose significant barriers. In this paper, we introduce IRL-VLA, a novel close-loop Reinforcement Learning via **I**nverse **R**einforcement **L**earning reward world model with a self-built VLA approach. Our framework proceeds in a three-stage paradigm: In the first stage, we propose a VLA architecture and pretrain the VLA policy via imitation learning. In the second stage, we construct a lightweight reward world model via inverse reinforcement learning to enable efficient close-loop reward computation. To further enhance planning performance, finally, we design specialized reward world model guidance reinforcement learning via PPO (Proximal Policy Optimization) to effectively balance safety incidents, comfortable driving, and traffic efficiency. Our approach achieves state-of-the-art performance in the NAVSIM v2 end-to-end driving benchmark, 1st runner up in CVPR2025 Autonomous Grand Challenge. We hope that our framework will accelerate VLA research in close-loop autonomous driving.

## 개요
Vision-Language-Action (VLA) 모델은 자율주행 분야에서 잠재력을 입증해 왔습니다. 그러나 두 가지 주요 과제가 그 발전을 저해하고 있습니다: (1) 기존 VLA 아키텍처는 일반적으로 개방 루프 설정에서의 모방 학습에 기반하여 데이터셋에 기록된 행동을 포착하는 경향이 있어, 최적이 아닌 제한된 성능을 초래합니다. (2) 폐쇄 루프 훈련은 고충실도 센서 시뮬레이션에 크게 의존하며, 여기서 도메인 격차와 계산 비효율성이 큰 장벽이 됩니다. 본 논문에서는 자체 구축 VLA 접근법을 통해 **역**강화 학습 보상 세계 모델을 이용한 새로운 폐쇄 루프 강화 학습인 IRL-VLA를 소개합니다. 우리의 프레임워크는 3단계 패러다임으로 진행됩니다: 첫 번째 단계에서는 VLA 아키텍처를 제안하고 모방 학습을 통해 VLA 정책을 사전 훈련합니다. 두 번째 단계에서는 역강화 학습을 통해 경량 보상 세계 모델을 구축하여 효율적인 폐쇄 루프 보상 계산을 가능하게 합니다. 마지막으로, 계획 성능을 더욱 향상시키기 위해 PPO(근접 정책 최적화)를 통한 특화된 보상 세계 모델 유도 강화 학습을 설계하여 안전 사고, 편안한 주행 및 교통 효율성을 효과적으로 균형을 맞춥니다. 우리의 접근법은 NAVSIM v2 종단간 주행 벤치마크에서 최첨단 성능을 달성했으며, CVPR2025 자율주행 그랜드 챌린지에서 1위 준우승을 차지했습니다. 우리의 프레임워크가 폐쇄 루프 자율주행에서 VLA 연구를 가속화하기를 기대합니다.

## 핵심 내용
Vision-Language-Action (VLA) 모델은 자율주행 분야에서 잠재력을 입증해 왔습니다. 그러나 두 가지 주요 과제가 그 발전을 저해하고 있습니다: (1) 기존 VLA 아키텍처는 일반적으로 개방 루프 설정에서의 모방 학습에 기반하여 데이터셋에 기록된 행동을 포착하는 경향이 있어, 최적이 아닌 제한된 성능을 초래합니다. (2) 폐쇄 루프 훈련은 고충실도 센서 시뮬레이션에 크게 의존하며, 여기서 도메인 격차와 계산 비효율성이 큰 장벽이 됩니다. 본 논문에서는 자체 구축 VLA 접근법을 통해 **역**강화 학습 보상 세계 모델을 이용한 새로운 폐쇄 루프 강화 학습인 IRL-VLA를 소개합니다. 우리의 프레임워크는 3단계 패러다임으로 진행됩니다: 첫 번째 단계에서는 VLA 아키텍처를 제안하고 모방 학습을 통해 VLA 정책을 사전 훈련합니다. 두 번째 단계에서는 역강화 학습을 통해 경량 보상 세계 모델을 구축하여 효율적인 폐쇄 루프 보상 계산을 가능하게 합니다. 마지막으로, 계획 성능을 더욱 향상시키기 위해 PPO(근접 정책 최적화)를 통한 특화된 보상 세계 모델 유도 강화 학습을 설계하여 안전 사고, 편안한 주행 및 교통 효율성을 효과적으로 균형을 맞춥니다. 우리의 접근법은 NAVSIM v2 종단간 주행 벤치마크에서 최첨단 성능을 달성했으며, CVPR2025 자율주행 그랜드 챌린지에서 1위 준우승을 차지했습니다. 우리의 프레임워크가 폐쇄 루프 자율주행에서 VLA 연구를 가속화하기를 기대합니다.
