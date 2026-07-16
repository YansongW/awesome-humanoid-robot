---
$id: ent_paper_reduced_order_model_guided_rl_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Reduced-Order Model-Guided RL for Demonstration-Free Humanoid Locomotion
  zh: Reduced-Order Model-Guided RL for Demonstration-Free Humanoid Locomotion
  ko: Reduced-Order Model-Guided RL for Demonstration-Free Humanoid Locomotion
summary:
  en: Reduced-Order Model-Guided RL for Demonstration-Free Humanoid Locomotion is a 2025 work on locomotion for humanoid robots.
  zh: Reduced-Order Model-Guided RL for Demonstration-Free Humanoid Locomotion is a 2025 work on locomotion for humanoid robots.
  ko: Reduced-Order Model-Guided RL for Demonstration-Free Humanoid Locomotion is a 2025 work on locomotion for humanoid robots.
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
- reduced_order_model_guided_rl
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2509.19023v1.
sources:
- id: src_001
  type: paper
  title: Reduced-Order Model-Guided RL for Demonstration-Free Humanoid Locomotion (arXiv)
  url: https://arxiv.org/abs/2509.19023
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
We introduce Reduced-Order Model-Guided Reinforcement Learning (ROM-GRL), a two-stage reinforcement learning framework for humanoid walking that requires no motion capture data or elaborate reward shaping. In the first stage, a compact 4-DOF (four-degree-of-freedom) reduced-order model (ROM) is trained via Proximal Policy Optimization. This generates energy-efficient gait templates. In the second stage, those dynamically consistent trajectories guide a full-body policy trained with Soft Actor--Critic augmented by an adversarial discriminator, ensuring the student's five-dimensional gait feature distribution matches the ROM's demonstrations. Experiments at 1 meter-per-second and 4 meter-per-second show that ROM-GRL produces stable, symmetric gaits with substantially lower tracking error than a pure-reward baseline. By distilling lightweight ROM guidance into high-dimensional policies, ROM-GRL bridges the gap between reward-only and imitation-based locomotion methods, enabling versatile, naturalistic humanoid behaviors without any human demonstrations.

## 核心内容
We introduce Reduced-Order Model-Guided Reinforcement Learning (ROM-GRL), a two-stage reinforcement learning framework for humanoid walking that requires no motion capture data or elaborate reward shaping. In the first stage, a compact 4-DOF (four-degree-of-freedom) reduced-order model (ROM) is trained via Proximal Policy Optimization. This generates energy-efficient gait templates. In the second stage, those dynamically consistent trajectories guide a full-body policy trained with Soft Actor--Critic augmented by an adversarial discriminator, ensuring the student's five-dimensional gait feature distribution matches the ROM's demonstrations. Experiments at 1 meter-per-second and 4 meter-per-second show that ROM-GRL produces stable, symmetric gaits with substantially lower tracking error than a pure-reward baseline. By distilling lightweight ROM guidance into high-dimensional policies, ROM-GRL bridges the gap between reward-only and imitation-based locomotion methods, enabling versatile, naturalistic humanoid behaviors without any human demonstrations.

## 参考
- http://arxiv.org/abs/2509.19023v1

## Overview
We introduce Reduced-Order Model-Guided Reinforcement Learning (ROM-GRL), a two-stage reinforcement learning framework for humanoid walking that requires no motion capture data or elaborate reward shaping. In the first stage, a compact 4-DOF (four-degree-of-freedom) reduced-order model (ROM) is trained via Proximal Policy Optimization. This generates energy-efficient gait templates. In the second stage, those dynamically consistent trajectories guide a full-body policy trained with Soft Actor--Critic augmented by an adversarial discriminator, ensuring the student's five-dimensional gait feature distribution matches the ROM's demonstrations. Experiments at 1 meter-per-second and 4 meter-per-second show that ROM-GRL produces stable, symmetric gaits with substantially lower tracking error than a pure-reward baseline. By distilling lightweight ROM guidance into high-dimensional policies, ROM-GRL bridges the gap between reward-only and imitation-based locomotion methods, enabling versatile, naturalistic humanoid behaviors without any human demonstrations.

## Content
We introduce Reduced-Order Model-Guided Reinforcement Learning (ROM-GRL), a two-stage reinforcement learning framework for humanoid walking that requires no motion capture data or elaborate reward shaping. In the first stage, a compact 4-DOF (four-degree-of-freedom) reduced-order model (ROM) is trained via Proximal Policy Optimization. This generates energy-efficient gait templates. In the second stage, those dynamically consistent trajectories guide a full-body policy trained with Soft Actor--Critic augmented by an adversarial discriminator, ensuring the student's five-dimensional gait feature distribution matches the ROM's demonstrations. Experiments at 1 meter-per-second and 4 meter-per-second show that ROM-GRL produces stable, symmetric gaits with substantially lower tracking error than a pure-reward baseline. By distilling lightweight ROM guidance into high-dimensional policies, ROM-GRL bridges the gap between reward-only and imitation-based locomotion methods, enabling versatile, naturalistic humanoid behaviors without any human demonstrations.

## 개요
우리는 ROM-GRL(Reduced-Order Model-Guided Reinforcement Learning)을 소개합니다. 이는 모션 캡처 데이터나 복잡한 보상 설계 없이 인간형 보행을 구현하는 2단계 강화 학습 프레임워크입니다. 첫 번째 단계에서는 PPO(Proximal Policy Optimization)를 통해 간결한 4자유도(4-DOF) 축소 차수 모델(ROM)을 훈련합니다. 이를 통해 에너지 효율적인 보행 템플릿을 생성합니다. 두 번째 단계에서는 이러한 동적으로 일관된 궤적이 적대적 판별기로 보강된 SAC(Soft Actor-Critic)로 훈련된 전신 정책을 안내하여, 학생 모델의 5차원 보행 특징 분포가 ROM의 시연과 일치하도록 보장합니다. 1m/s 및 4m/s 속도에서의 실험 결과, ROM-GRL은 순수 보상 기반 기준선보다 현저히 낮은 추적 오차로 안정적이고 대칭적인 보행을 생성합니다. 가벼운 ROM 안내를 고차원 정책으로 증류함으로써, ROM-GRL은 보상 전용 방법과 모방 기반 보행 방법 간의 격차를 해소하여 인간 시연 없이도 다양하고 자연스러운 인간형 행동을 가능하게 합니다.

## 핵심 내용
우리는 ROM-GRL(Reduced-Order Model-Guided Reinforcement Learning)을 소개합니다. 이는 모션 캡처 데이터나 복잡한 보상 설계 없이 인간형 보행을 구현하는 2단계 강화 학습 프레임워크입니다. 첫 번째 단계에서는 PPO(Proximal Policy Optimization)를 통해 간결한 4자유도(4-DOF) 축소 차수 모델(ROM)을 훈련합니다. 이를 통해 에너지 효율적인 보행 템플릿을 생성합니다. 두 번째 단계에서는 이러한 동적으로 일관된 궤적이 적대적 판별기로 보강된 SAC(Soft Actor-Critic)로 훈련된 전신 정책을 안내하여, 학생 모델의 5차원 보행 특징 분포가 ROM의 시연과 일치하도록 보장합니다. 1m/s 및 4m/s 속도에서의 실험 결과, ROM-GRL은 순수 보상 기반 기준선보다 현저히 낮은 추적 오차로 안정적이고 대칭적인 보행을 생성합니다. 가벼운 ROM 안내를 고차원 정책으로 증류함으로써, ROM-GRL은 보상 전용 방법과 모방 기반 보행 방법 간의 격차를 해소하여 인간 시연 없이도 다양하고 자연스러운 인간형 행동을 가능하게 합니다.
