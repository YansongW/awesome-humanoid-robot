---
$id: ent_paper_bfm_zero_a_promptable_behavior_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'BFM-Zero: A Promptable Behavioral Foundation Model for Humanoid Control Using Unsupervised Reinforcement Learning'
  zh: BFM-Zero｜使用无监督强化学习的人形控制的即时行为基础模型
  ko: 'BFM-Zero: A Promptable Behavioral Foundation Model for Humanoid Control Using Unsupervised Reinforcement Learning'
summary:
  en: Building Behavioral Foundation Models (BFMs) for humanoid robots has the potential to unify diverse control tasks under
    a single, promptable generalist policy. However, existing approaches are either exclusively deployed on simulated humanoid
    characters, or specialized to specific tasks such as tracking. We propose BFM-Zero, a framework that learns an effective
    shared latent representation that embeds motions, goals, and rewards into a common space, enabling a single policy to
    be prompted for multiple downstream tasks without retraining. This well-structured latent space in BFM-Zero enables versatile
    and robust whole-body skills on a Unitree G1 humanoid in the real world, via diverse inference methods, including zero-shot
    motion tracking, goal reaching, and reward optimization, and few-sho
  zh: BFM-Zero 把本体状态与关节序列、仿真交互数据、接触力/触觉信号转成可跟踪的身体目标，并通过PPO/RL 策略训练、分层技能/专家策略、闭环纠错/人类干预训练或组合全身策略，最终输出全身轨迹/动作序列、低层控制器目标。关键点是把任务拆成可路由的技能或专家策略，再用高层模块在执行中选择和组合。
  ko: BFM-Zero 把本体状态与关节序列、仿真交互数据、接触力/触觉信号转成可跟踪的身体目标，并通过PPO/RL 策略训练、分层技能/专家策略、闭环纠错/人类干预训练或组合全身策略，最终输出全身轨迹/动作序列、低层控制器目标。关键点是把任务拆成可路由的技能或专家策略，再用高层模块在执行中选择和组合。
domains:
- 06_design_engineering
- 07_ai_models_algorithms
layers:
- midstream
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- balance
- behavioral_foundation_model
- bfm_zero
- locomotion
- motion_tracking
- whole_body_control
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: low
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from Semantic Scholar search: BFM-Zero: A Promptable
    Behavioral Foundation Model for Humanoid Control Using Unsupervised Reinforcement Learning.'
sources:
- id: src_001
  type: website
  title: BFM-Zero project page
  url: https://lecar-lab.github.io/BFM-Zero/
  date: '2025'
  accessed_at: '2026-06-26'
theoretical_depth:
- system
---
## 概述
Building Behavioral Foundation Models (BFMs) for humanoid robots has the potential to unify diverse control tasks under a single, promptable generalist policy. However, existing approaches are either exclusively deployed on simulated humanoid characters, or specialized to specific tasks such as tracking. We propose BFM-Zero, a framework that learns an effective shared latent representation that embeds motions, goals, and rewards into a common space, enabling a single policy to be prompted for multiple downstream tasks without retraining. This well-structured latent space in BFM-Zero enables versatile and robust whole-body skills on a Unitree G1 humanoid in the real world, via diverse inference methods, including zero-shot motion tracking, goal reaching, and reward optimization, and few-shot optimization-based adaptation. Unlike prior on-policy reinforcement learning (RL) frameworks, BFM-Zero builds upon recent advancements in unsupervised RL and Forward-Backward (FB) models, which offer an objective-centric, explainable, and smooth latent representation of whole-body motions. We further extend BFM-Zero with critical reward shaping, domain randomization, and history-dependent asymmetric learning to bridge the sim-to-real gap. Those key design choices are quantitatively ablated in simulation. A first-of-its-kind model, BFM-Zero establishes a step toward scalable, promptable behavioral foundation models for whole-body humanoid control.

## 核心内容
Building Behavioral Foundation Models (BFMs) for humanoid robots has the potential to unify diverse control tasks under a single, promptable generalist policy. However, existing approaches are either exclusively deployed on simulated humanoid characters, or specialized to specific tasks such as tracking. We propose BFM-Zero, a framework that learns an effective shared latent representation that embeds motions, goals, and rewards into a common space, enabling a single policy to be prompted for multiple downstream tasks without retraining. This well-structured latent space in BFM-Zero enables versatile and robust whole-body skills on a Unitree G1 humanoid in the real world, via diverse inference methods, including zero-shot motion tracking, goal reaching, and reward optimization, and few-shot optimization-based adaptation. Unlike prior on-policy reinforcement learning (RL) frameworks, BFM-Zero builds upon recent advancements in unsupervised RL and Forward-Backward (FB) models, which offer an objective-centric, explainable, and smooth latent representation of whole-body motions. We further extend BFM-Zero with critical reward shaping, domain randomization, and history-dependent asymmetric learning to bridge the sim-to-real gap. Those key design choices are quantitatively ablated in simulation. A first-of-its-kind model, BFM-Zero establishes a step toward scalable, promptable behavioral foundation models for whole-body humanoid control.

## 参考
- Semantic Scholar search: BFM-Zero: A Promptable Behavioral Foundation Model for Humanoid Control Using Unsupervised Reinforcement Learning

## Overview
Building Behavioral Foundation Models (BFMs) for humanoid robots has the potential to unify diverse control tasks under a single, promptable generalist policy. However, existing approaches are either exclusively deployed on simulated humanoid characters, or specialized to specific tasks such as tracking. We propose BFM-Zero, a framework that learns an effective shared latent representation that embeds motions, goals, and rewards into a common space, enabling a single policy to be prompted for multiple downstream tasks without retraining. This well-structured latent space in BFM-Zero enables versatile and robust whole-body skills on a Unitree G1 humanoid in the real world, via diverse inference methods, including zero-shot motion tracking, goal reaching, and reward optimization, and few-shot optimization-based adaptation. Unlike prior on-policy reinforcement learning (RL) frameworks, BFM-Zero builds upon recent advancements in unsupervised RL and Forward-Backward (FB) models, which offer an objective-centric, explainable, and smooth latent representation of whole-body motions. We further extend BFM-Zero with critical reward shaping, domain randomization, and history-dependent asymmetric learning to bridge the sim-to-real gap. Those key design choices are quantitatively ablated in simulation. A first-of-its-kind model, BFM-Zero establishes a step toward scalable, promptable behavioral foundation models for whole-body humanoid control.

## Content
Building Behavioral Foundation Models (BFMs) for humanoid robots has the potential to unify diverse control tasks under a single, promptable generalist policy. However, existing approaches are either exclusively deployed on simulated humanoid characters, or specialized to specific tasks such as tracking. We propose BFM-Zero, a framework that learns an effective shared latent representation that embeds motions, goals, and rewards into a common space, enabling a single policy to be prompted for multiple downstream tasks without retraining. This well-structured latent space in BFM-Zero enables versatile and robust whole-body skills on a Unitree G1 humanoid in the real world, via diverse inference methods, including zero-shot motion tracking, goal reaching, and reward optimization, and few-shot optimization-based adaptation. Unlike prior on-policy reinforcement learning (RL) frameworks, BFM-Zero builds upon recent advancements in unsupervised RL and Forward-Backward (FB) models, which offer an objective-centric, explainable, and smooth latent representation of whole-body motions. We further extend BFM-Zero with critical reward shaping, domain randomization, and history-dependent asymmetric learning to bridge the sim-to-real gap. Those key design choices are quantitatively ablated in simulation. A first-of-its-kind model, BFM-Zero establishes a step toward scalable, promptable behavioral foundation models for whole-body humanoid control.

## 개요
휴머노이드 로봇을 위한 행동 기반 모델(BFM)을 구축하면 다양한 제어 작업을 단일 프롬프트 가능한 범용 정책으로 통합할 수 있는 잠재력을 제공합니다. 그러나 기존 접근 방식은 시뮬레이션된 휴머노이드 캐릭터에만 배포되거나 추적과 같은 특정 작업에 특화되어 있습니다. 우리는 BFM-Zero를 제안합니다. 이 프레임워크는 동작, 목표 및 보상을 공통 공간에 임베딩하는 효과적인 공유 잠재 표현을 학습하여, 재학습 없이 단일 정책으로 여러 다운스트림 작업을 프롬프트할 수 있도록 합니다. BFM-Zero의 잘 구조화된 잠재 공간은 제로샷 동작 추적, 목표 도달, 보상 최적화 및 퓨샷 최적화 기반 적응을 포함한 다양한 추론 방법을 통해 실제 세계의 Unitree G1 휴머노이드에서 다재다능하고 강력한 전신 기술을 가능하게 합니다. 이전의 온-폴리시 강화 학습(RL) 프레임워크와 달리, BFM-Zero는 최근의 비지도 RL 및 Forward-Backward(FB) 모델의 발전을 기반으로 하며, 이는 목표 중심적이고 설명 가능하며 부드러운 전신 동작의 잠재 표현을 제공합니다. 우리는 BFM-Zero를 중요한 보상 형성, 도메인 무작위화 및 히스토리 종속 비대칭 학습으로 확장하여 시뮬레이션-현실 간극을 해소합니다. 이러한 주요 설계 선택은 시뮬레이션에서 정량적으로 절제됩니다. 최초의 모델인 BFM-Zero는 확장 가능하고 프롬프트 가능한 전신 휴머노이드 제어를 위한 행동 기반 모델로 나아가는 한 걸음을 확립합니다.

## 핵심 내용
휴머노이드 로봇을 위한 행동 기반 모델(BFM)을 구축하면 다양한 제어 작업을 단일 프롬프트 가능한 범용 정책으로 통합할 수 있는 잠재력을 제공합니다. 그러나 기존 접근 방식은 시뮬레이션된 휴머노이드 캐릭터에만 배포되거나 추적과 같은 특정 작업에 특화되어 있습니다. 우리는 BFM-Zero를 제안합니다. 이 프레임워크는 동작, 목표 및 보상을 공통 공간에 임베딩하는 효과적인 공유 잠재 표현을 학습하여, 재학습 없이 단일 정책으로 여러 다운스트림 작업을 프롬프트할 수 있도록 합니다. BFM-Zero의 잘 구조화된 잠재 공간은 제로샷 동작 추적, 목표 도달, 보상 최적화 및 퓨샷 최적화 기반 적응을 포함한 다양한 추론 방법을 통해 실제 세계의 Unitree G1 휴머노이드에서 다재다능하고 강력한 전신 기술을 가능하게 합니다. 이전의 온-폴리시 강화 학습(RL) 프레임워크와 달리, BFM-Zero는 최근의 비지도 RL 및 Forward-Backward(FB) 모델의 발전을 기반으로 하며, 이는 목표 중심적이고 설명 가능하며 부드러운 전신 동작의 잠재 표현을 제공합니다. 우리는 BFM-Zero를 중요한 보상 형성, 도메인 무작위화 및 히스토리 종속 비대칭 학습으로 확장하여 시뮬레이션-현실 간극을 해소합니다. 이러한 주요 설계 선택은 시뮬레이션에서 정량적으로 절제됩니다. 최초의 모델인 BFM-Zero는 확장 가능하고 프롬프트 가능한 전신 휴머노이드 제어를 위한 행동 기반 모델로 나아가는 한 걸음을 확립합니다.
