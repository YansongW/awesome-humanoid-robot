---
$id: ent_paper_li_bfm_zero_a_promptable_behavior_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'BFM-Zero: A Promptable Behavioral Foundation Model for Humanoid Control Using Unsupervised Reinforcement Learning'
  zh: BFM-Zero：基于无监督强化学习的可提示人形机器人行为基础模型
  ko: 'BFM-Zero: 비지도 강화학습을 이용한 프롬프트 가능한 휴머노이드 제어 행동 기초 모델'
summary:
  en: BFM-Zero trains a single promptable foundation policy for whole-body humanoid control using off-policy unsupervised
    reinforcement learning and Forward-Backward representations, enabling zero-shot motion tracking, goal reaching, reward
    optimization, and few-shot latent-space adaptation on a real Unitree G1.
  zh: BFM-Zero基于离策略无监督强化学习与Forward-Backward表示，训练单一可提示的全身人形控制基础策略，可在真实Unitree G1上实现零样本运动跟踪、目标到达、奖励优化及少样本潜在空间自适应。
  ko: BFM-Zero는 오프폴리시 비지도 강화학습과 Forward-Backward 표현을 활용해 단일 프롬프트 가능한 전신 휴머노이드 제어 기초 정책을 학습하며, 실제 Unitree G1에서 제로샷 동작 추적, 목표
    도달, 보상 최적화 및 소수 샘플 잠재 공간 적응을 가능하게 한다.
domains:
- 07_ai_models_algorithms
- 08_software_middleware
- 05_mass_production
- 11_applications_markets
layers:
- intelligence
- validation_markets
functional_roles:
- knowledge
- intelligence
tags:
- behavioral_foundation_model
- promptable_policy
- unsupervised_reinforcement_learning
- forward_backward_representation
- sim_to_real
- whole_body_control
- unitree_g1
- booster_t1
- zero_shot_humanoid_control
- latent_space_control
- motion_tracking
- goal_reaching
- reward_optimization
- few_shot_adaptation
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2511.04131v1.
sources:
- id: src_001
  type: paper
  title: 'BFM-Zero: A Promptable Behavioral Foundation Model for Humanoid Control Using Unsupervised Reinforcement Learning'
  url: https://arxiv.org/abs/2511.04131
  date: '2025'
  accessed_at: '2026-06-26'
theoretical_depth:
- method
---
## 概述
Building Behavioral Foundation Models (BFMs) for humanoid robots has the potential to unify diverse control tasks under a single, promptable generalist policy. However, existing approaches are either exclusively deployed on simulated humanoid characters, or specialized to specific tasks such as tracking. We propose BFM-Zero, a framework that learns an effective shared latent representation that embeds motions, goals, and rewards into a common space, enabling a single policy to be prompted for multiple downstream tasks without retraining. This well-structured latent space in BFM-Zero enables versatile and robust whole-body skills on a Unitree G1 humanoid in the real world, via diverse inference methods, including zero-shot motion tracking, goal reaching, and reward optimization, and few-shot optimization-based adaptation. Unlike prior on-policy reinforcement learning (RL) frameworks, BFM-Zero builds upon recent advancements in unsupervised RL and Forward-Backward (FB) models, which offer an objective-centric, explainable, and smooth latent representation of whole-body motions. We further extend BFM-Zero with critical reward shaping, domain randomization, and history-dependent asymmetric learning to bridge the sim-to-real gap. Those key design choices are quantitatively ablated in simulation. A first-of-its-kind model, BFM-Zero establishes a step toward scalable, promptable behavioral foundation models for whole-body humanoid control.

## 核心内容
Building Behavioral Foundation Models (BFMs) for humanoid robots has the potential to unify diverse control tasks under a single, promptable generalist policy. However, existing approaches are either exclusively deployed on simulated humanoid characters, or specialized to specific tasks such as tracking. We propose BFM-Zero, a framework that learns an effective shared latent representation that embeds motions, goals, and rewards into a common space, enabling a single policy to be prompted for multiple downstream tasks without retraining. This well-structured latent space in BFM-Zero enables versatile and robust whole-body skills on a Unitree G1 humanoid in the real world, via diverse inference methods, including zero-shot motion tracking, goal reaching, and reward optimization, and few-shot optimization-based adaptation. Unlike prior on-policy reinforcement learning (RL) frameworks, BFM-Zero builds upon recent advancements in unsupervised RL and Forward-Backward (FB) models, which offer an objective-centric, explainable, and smooth latent representation of whole-body motions. We further extend BFM-Zero with critical reward shaping, domain randomization, and history-dependent asymmetric learning to bridge the sim-to-real gap. Those key design choices are quantitatively ablated in simulation. A first-of-its-kind model, BFM-Zero establishes a step toward scalable, promptable behavioral foundation models for whole-body humanoid control.

## 参考
- http://arxiv.org/abs/2511.04131v1

## Overview
Building Behavioral Foundation Models (BFMs) for humanoid robots has the potential to unify diverse control tasks under a single, promptable generalist policy. However, existing approaches are either exclusively deployed on simulated humanoid characters, or specialized to specific tasks such as tracking. We propose BFM-Zero, a framework that learns an effective shared latent representation that embeds motions, goals, and rewards into a common space, enabling a single policy to be prompted for multiple downstream tasks without retraining. This well-structured latent space in BFM-Zero enables versatile and robust whole-body skills on a Unitree G1 humanoid in the real world, via diverse inference methods, including zero-shot motion tracking, goal reaching, and reward optimization, and few-shot optimization-based adaptation. Unlike prior on-policy reinforcement learning (RL) frameworks, BFM-Zero builds upon recent advancements in unsupervised RL and Forward-Backward (FB) models, which offer an objective-centric, explainable, and smooth latent representation of whole-body motions. We further extend BFM-Zero with critical reward shaping, domain randomization, and history-dependent asymmetric learning to bridge the sim-to-real gap. Those key design choices are quantitatively ablated in simulation. A first-of-its-kind model, BFM-Zero establishes a step toward scalable, promptable behavioral foundation models for whole-body humanoid control.

## Content
Building Behavioral Foundation Models (BFMs) for humanoid robots has the potential to unify diverse control tasks under a single, promptable generalist policy. However, existing approaches are either exclusively deployed on simulated humanoid characters, or specialized to specific tasks such as tracking. We propose BFM-Zero, a framework that learns an effective shared latent representation that embeds motions, goals, and rewards into a common space, enabling a single policy to be prompted for multiple downstream tasks without retraining. This well-structured latent space in BFM-Zero enables versatile and robust whole-body skills on a Unitree G1 humanoid in the real world, via diverse inference methods, including zero-shot motion tracking, goal reaching, and reward optimization, and few-shot optimization-based adaptation. Unlike prior on-policy reinforcement learning (RL) frameworks, BFM-Zero builds upon recent advancements in unsupervised RL and Forward-Backward (FB) models, which offer an objective-centric, explainable, and smooth latent representation of whole-body motions. We further extend BFM-Zero with critical reward shaping, domain randomization, and history-dependent asymmetric learning to bridge the sim-to-real gap. Those key design choices are quantitatively ablated in simulation. A first-of-its-kind model, BFM-Zero establishes a step toward scalable, promptable behavioral foundation models for whole-body humanoid control.

## 개요
휴머노이드 로봇을 위한 행동 기반 모델(BFM)을 구축하면 다양한 제어 작업을 단일 프롬프트 가능한 범용 정책으로 통합할 수 있는 잠재력이 있습니다. 그러나 기존 접근 방식은 시뮬레이션된 휴머노이드 캐릭터에만 배포되거나 추적과 같은 특정 작업에 특화되어 있습니다. 우리는 BFM-Zero를 제안합니다. 이 프레임워크는 동작, 목표 및 보상을 공통 공간에 임베딩하는 효과적인 공유 잠재 표현을 학습하여, 재학습 없이 단일 정책으로 여러 다운스트림 작업을 프롬프트할 수 있게 합니다. BFM-Zero의 잘 구조화된 잠재 공간은 제로샷 동작 추적, 목표 도달, 보상 최적화 및 퓨샷 최적화 기반 적응을 포함한 다양한 추론 방법을 통해 실제 환경의 Unitree G1 휴머노이드에서 다재다능하고 강력한 전신 기술을 가능하게 합니다. 기존의 온-폴리시 강화 학습(RL) 프레임워크와 달리, BFM-Zero는 최근의 비지도 RL 및 순방향-역방향(FB) 모델의 발전을 기반으로 하며, 이는 목표 중심적이고 설명 가능하며 부드러운 전신 동작의 잠재 표현을 제공합니다. 우리는 BFM-Zero를 중요한 보상 형성, 도메인 무작위화 및 이력 종속 비대칭 학습으로 확장하여 시뮬레이션-현실 간극을 해소합니다. 이러한 주요 설계 선택은 시뮬레이션에서 정량적으로 절제됩니다. 최초의 모델인 BFM-Zero는 확장 가능하고 프롬프트 가능한 전신 휴머노이드 제어를 위한 행동 기반 모델을 향한 한 걸음을 내딛습니다.

## 핵심 내용
휴머노이드 로봇을 위한 행동 기반 모델(BFM)을 구축하면 다양한 제어 작업을 단일 프롬프트 가능한 범용 정책으로 통합할 수 있는 잠재력이 있습니다. 그러나 기존 접근 방식은 시뮬레이션된 휴머노이드 캐릭터에만 배포되거나 추적과 같은 특정 작업에 특화되어 있습니다. 우리는 BFM-Zero를 제안합니다. 이 프레임워크는 동작, 목표 및 보상을 공통 공간에 임베딩하는 효과적인 공유 잠재 표현을 학습하여, 재학습 없이 단일 정책으로 여러 다운스트림 작업을 프롬프트할 수 있게 합니다. BFM-Zero의 잘 구조화된 잠재 공간은 제로샷 동작 추적, 목표 도달, 보상 최적화 및 퓨샷 최적화 기반 적응을 포함한 다양한 추론 방법을 통해 실제 환경의 Unitree G1 휴머노이드에서 다재다능하고 강력한 전신 기술을 가능하게 합니다. 기존의 온-폴리시 강화 학습(RL) 프레임워크와 달리, BFM-Zero는 최근의 비지도 RL 및 순방향-역방향(FB) 모델의 발전을 기반으로 하며, 이는 목표 중심적이고 설명 가능하며 부드러운 전신 동작의 잠재 표현을 제공합니다. 우리는 BFM-Zero를 중요한 보상 형성, 도메인 무작위화 및 이력 종속 비대칭 학습으로 확장하여 시뮬레이션-현실 간극을 해소합니다. 이러한 주요 설계 선택은 시뮬레이션에서 정량적으로 절제됩니다. 최초의 모델인 BFM-Zero는 확장 가능하고 프롬프트 가능한 전신 휴머노이드 제어를 위한 행동 기반 모델을 향한 한 걸음을 내딛습니다.
