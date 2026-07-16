---
$id: ent_paper_worldscape_moe_a_unified_mixtu_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Worldscape-MoE: A Unified Mixture-of-Experts World Model for Scalable Heterogeneous Action Control'
  zh: 'Worldscape-MoE: A Unified Mixture-of-Experts World Model for Scalable Heterogeneous Action Control'
  ko: 'Worldscape-MoE: A Unified Mixture-of-Experts World Model for Scalable Heterogeneous Action Control'
summary:
  en: 'arXiv:2607.03964v1 Announce Type: new Abstract: World models are rapidly becoming a core infrastructure for embodied
    intelligence and interactive agents: they provide controllable simulators in which agents can perceive, act, forecast,
    and acquire scalable experience. Yet current video generation world models are still organized around isolated control
    interfaces, such as camera trajectories, robot actions, or hand-joint signals. This fragmentation is increasingly a scaling
    bottleneck. The central challenge is not the absence of controllable generators, but the lack of a unified and extensible
    learning framework that can absorb heterogeneous action supervision while preserving a shared model of world dynamics.
    In this work, we introduce Worldscape-MoE, a Mixture-of-Experts world model built on Diffusion Transformers for scalable
    heterogeneous action control. Our key observation is that different controls specify different interfaces to the same
    underlying world: although their representations differ, they constrain shared physical regularities, scene dynamics,
    and interaction semantics. Worldscape-MoE operationalizes this observation through modality-aware control injection, shared
    and control-specific experts, and a progressive MoE tuning strategy that supports continual extension to new action modalities.
    Experiments across locomotion, robotic manipulation, and egocentric hand control show that heterogeneous supervision improves
    rather than interferes with individual control capabilities. Worldscape-MoE achieves strong results on WorldArena, improves
    locomotion and hand-control metrics, exhibits robust out-of-distribution generalization, and demonstrates scaling behavior
    as additional control data and experts are integrated.'
  zh: 'arXiv:2607.03964v1 Announce Type: new Abstract: World models are rapidly becoming a core infrastructure for embodied
    intelligence and interactive agents: they provide controllable simulators in which agents can perceive, act, forecast,
    and acquire scalable experience. Yet current video generation world models are still organized around isolated control
    interfaces, such as camera trajectories, robot actions, or hand-joint signals. This fragmentation is increasingly a scaling
    bottleneck. The central challenge is not the absence of controllable generators, but the lack of a unified and extensible
    learning framework that can absorb heterogeneous action supervision while preserving a shared model of world dynamics.
    In this work, we introduce Worldscape-MoE, a Mixture-of-Experts world model built on Diffusion Transformers for scalable
    heterogeneous action control. Our key observation is that different controls specify different interfaces to the same
    underlying world: although their representations differ, they constrain shared physical regularities, scene dynamics,
    and interaction semantics. Worldscape-MoE operationalizes this observation through modality-aware control injection, shared
    and control-specific experts, and a progressive MoE tuning strategy that supports continual extension to new action modalities.
    Experiments across locomotion, robotic manipulation, and egocentric hand control show that heterogeneous supervision improves
    rather than interferes with individual control capabilities. Worldscape-MoE achieves strong results on WorldArena, improves
    locomotion and hand-control metrics, exhibits robust out-of-distribution generalization, and demonstrates scaling behavior
    as additional control data and experts are integrated.'
  ko: 'arXiv:2607.03964v1 Announce Type: new Abstract: World models are rapidly becoming a core infrastructure for embodied
    intelligence and interactive agents: they provide controllable simulators in which agents can perceive, act, forecast,
    and acquire scalable experience. Yet current video generation world models are still organized around isolated control
    interfaces, such as camera trajectories, robot actions, or hand-joint signals. This fragmentation is increasingly a scaling
    bottleneck. The central challenge is not the absence of controllable generators, but the lack of a unified and extensible
    learning framework that can absorb heterogeneous action supervision while preserving a shared model of world dynamics.
    In this work, we introduce Worldscape-MoE, a Mixture-of-Experts world model built on Diffusion Transformers for scalable
    heterogeneous action control. Our key observation is that different controls specify different interfaces to the same
    underlying world: although their representations differ, they constrain shared physical regularities, scene dynamics,
    and interaction semantics. Worldscape-MoE operationalizes this observation through modality-aware control injection, shared
    and control-specific experts, and a progressive MoE tuning strategy that supports continual extension to new action modalities.
    Experiments across locomotion, robotic manipulation, and egocentric hand control show that heterogeneous supervision improves
    rather than interferes with individual control capabilities. Worldscape-MoE achieves strong results on WorldArena, improves
    locomotion and hand-control metrics, exhibits robust out-of-distribution generalization, and demonstrates scaling behavior
    as additional control data and experts are integrated.'
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
- robotics
- worldscape_moe
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2607.03964v1.
sources:
- id: src_001
  type: paper
  title: 'Worldscape-MoE: A Unified Mixture-of-Experts World Model for Scalable Heterogeneous Action Control (arXiv)'
  url: https://arxiv.org/abs/2607.03964
  date: '2026'
  accessed_at: '2026-07-08'
---
## 概述
World models are rapidly becoming a core infrastructure for embodied intelligence and interactive agents: they provide controllable simulators in which agents can perceive, act, forecast, and acquire scalable experience. Yet current video generation world models are still organized around isolated control interfaces, such as camera trajectories, robot actions, or hand-joint signals. This fragmentation is increasingly a scaling bottleneck. The central challenge is not the absence of controllable generators, but the lack of a unified and extensible learning framework that can absorb heterogeneous action supervision while preserving a shared model of world dynamics. In this work, we introduce Worldscape-MoE, a Mixture-of-Experts world model built on Diffusion Transformers for scalable heterogeneous action control. Our key observation is that different controls specify different interfaces to the same underlying world: although their representations differ, they constrain shared physical regularities, scene dynamics, and interaction semantics. Worldscape-MoE operationalizes this observation through modality-aware control injection, shared and control-specific experts, and a progressive MoE tuning strategy that supports continual extension to new action modalities. Experiments across locomotion, robotic manipulation, and egocentric hand control show that heterogeneous supervision improves rather than interferes with individual control capabilities. Worldscape-MoE achieves strong results on WorldArena, improves locomotion and hand-control metrics, exhibits robust out-of-distribution generalization, and demonstrates scaling behavior as additional control data and experts are integrated.

## 核心内容
World models are rapidly becoming a core infrastructure for embodied intelligence and interactive agents: they provide controllable simulators in which agents can perceive, act, forecast, and acquire scalable experience. Yet current video generation world models are still organized around isolated control interfaces, such as camera trajectories, robot actions, or hand-joint signals. This fragmentation is increasingly a scaling bottleneck. The central challenge is not the absence of controllable generators, but the lack of a unified and extensible learning framework that can absorb heterogeneous action supervision while preserving a shared model of world dynamics. In this work, we introduce Worldscape-MoE, a Mixture-of-Experts world model built on Diffusion Transformers for scalable heterogeneous action control. Our key observation is that different controls specify different interfaces to the same underlying world: although their representations differ, they constrain shared physical regularities, scene dynamics, and interaction semantics. Worldscape-MoE operationalizes this observation through modality-aware control injection, shared and control-specific experts, and a progressive MoE tuning strategy that supports continual extension to new action modalities. Experiments across locomotion, robotic manipulation, and egocentric hand control show that heterogeneous supervision improves rather than interferes with individual control capabilities. Worldscape-MoE achieves strong results on WorldArena, improves locomotion and hand-control metrics, exhibits robust out-of-distribution generalization, and demonstrates scaling behavior as additional control data and experts are integrated.

## 参考
- http://arxiv.org/abs/2607.03964v1

## Overview
World models are rapidly becoming a core infrastructure for embodied intelligence and interactive agents: they provide controllable simulators in which agents can perceive, act, forecast, and acquire scalable experience. Yet current video generation world models are still organized around isolated control interfaces, such as camera trajectories, robot actions, or hand-joint signals. This fragmentation is increasingly a scaling bottleneck. The central challenge is not the absence of controllable generators, but the lack of a unified and extensible learning framework that can absorb heterogeneous action supervision while preserving a shared model of world dynamics. In this work, we introduce Worldscape-MoE, a Mixture-of-Experts world model built on Diffusion Transformers for scalable heterogeneous action control. Our key observation is that different controls specify different interfaces to the same underlying world: although their representations differ, they constrain shared physical regularities, scene dynamics, and interaction semantics. Worldscape-MoE operationalizes this observation through modality-aware control injection, shared and control-specific experts, and a progressive MoE tuning strategy that supports continual extension to new action modalities. Experiments across locomotion, robotic manipulation, and egocentric hand control show that heterogeneous supervision improves rather than interferes with individual control capabilities. Worldscape-MoE achieves strong results on WorldArena, improves locomotion and hand-control metrics, exhibits robust out-of-distribution generalization, and demonstrates scaling behavior as additional control data and experts are integrated.

## Content
World models are rapidly becoming a core infrastructure for embodied intelligence and interactive agents: they provide controllable simulators in which agents can perceive, act, forecast, and acquire scalable experience. Yet current video generation world models are still organized around isolated control interfaces, such as camera trajectories, robot actions, or hand-joint signals. This fragmentation is increasingly a scaling bottleneck. The central challenge is not the absence of controllable generators, but the lack of a unified and extensible learning framework that can absorb heterogeneous action supervision while preserving a shared model of world dynamics. In this work, we introduce Worldscape-MoE, a Mixture-of-Experts world model built on Diffusion Transformers for scalable heterogeneous action control. Our key observation is that different controls specify different interfaces to the same underlying world: although their representations differ, they constrain shared physical regularities, scene dynamics, and interaction semantics. Worldscape-MoE operationalizes this observation through modality-aware control injection, shared and control-specific experts, and a progressive MoE tuning strategy that supports continual extension to new action modalities. Experiments across locomotion, robotic manipulation, and egocentric hand control show that heterogeneous supervision improves rather than interferes with individual control capabilities. Worldscape-MoE achieves strong results on WorldArena, improves locomotion and hand-control metrics, exhibits robust out-of-distribution generalization, and demonstrates scaling behavior as additional control data and experts are integrated.

## 개요
World models는 체화된 지능과 상호작용 에이전트를 위한 핵심 인프라로 빠르게 자리 잡고 있습니다. 에이전트가 인지, 행동, 예측, 확장 가능한 경험을 습득할 수 있는 제어 가능한 시뮬레이터를 제공합니다. 그러나 현재의 비디오 생성 월드 모델은 여전히 카메라 궤적, 로봇 동작, 손 관절 신호와 같은 고립된 제어 인터페이스를 중심으로 구성되어 있습니다. 이러한 단편화는 점점 확장의 병목 현상이 되고 있습니다. 핵심 과제는 제어 가능한 생성기의 부재가 아니라, 공유된 세계 역학 모델을 유지하면서 이질적인 행동 감독을 흡수할 수 있는 통합적이고 확장 가능한 학습 프레임워크의 부재입니다. 본 연구에서는 확장 가능한 이질적 행동 제어를 위해 Diffusion Transformers 기반의 Mixture-of-Experts 월드 모델인 Worldscape-MoE를 소개합니다. 우리의 핵심 관찰은 서로 다른 제어가 동일한 기저 세계에 대해 서로 다른 인터페이스를 지정한다는 것입니다. 표현은 다르지만, 공유된 물리적 규칙성, 장면 역학, 상호작용 의미론을 제약합니다. Worldscape-MoE는 모달리티 인식 제어 주입, 공유 및 제어별 전문가, 새로운 행동 모달리티로의 지속적 확장을 지원하는 점진적 MoE 튜닝 전략을 통해 이 관찰을 구현합니다. 보행, 로봇 조작, 자기중심적 손 제어에 걸친 실험은 이질적 감독이 개별 제어 능력을 방해하기보다 향상시킨다는 것을 보여줍니다. Worldscape-MoE는 WorldArena에서 강력한 결과를 달성하고, 보행 및 손 제어 지표를 개선하며, 강력한 분포 외 일반화를 보여주고, 추가 제어 데이터와 전문가가 통합됨에 따라 확장 동작을 입증합니다.

## 핵심 내용
World models는 체화된 지능과 상호작용 에이전트를 위한 핵심 인프라로 빠르게 자리 잡고 있습니다. 에이전트가 인지, 행동, 예측, 확장 가능한 경험을 습득할 수 있는 제어 가능한 시뮬레이터를 제공합니다. 그러나 현재의 비디오 생성 월드 모델은 여전히 카메라 궤적, 로봇 동작, 손 관절 신호와 같은 고립된 제어 인터페이스를 중심으로 구성되어 있습니다. 이러한 단편화는 점점 확장의 병목 현상이 되고 있습니다. 핵심 과제는 제어 가능한 생성기의 부재가 아니라, 공유된 세계 역학 모델을 유지하면서 이질적인 행동 감독을 흡수할 수 있는 통합적이고 확장 가능한 학습 프레임워크의 부재입니다. 본 연구에서는 확장 가능한 이질적 행동 제어를 위해 Diffusion Transformers 기반의 Mixture-of-Experts 월드 모델인 Worldscape-MoE를 소개합니다. 우리의 핵심 관찰은 서로 다른 제어가 동일한 기저 세계에 대해 서로 다른 인터페이스를 지정한다는 것입니다. 표현은 다르지만, 공유된 물리적 규칙성, 장면 역학, 상호작용 의미론을 제약합니다. Worldscape-MoE는 모달리티 인식 제어 주입, 공유 및 제어별 전문가, 새로운 행동 모달리티로의 지속적 확장을 지원하는 점진적 MoE 튜닝 전략을 통해 이 관찰을 구현합니다. 보행, 로봇 조작, 자기중심적 손 제어에 걸친 실험은 이질적 감독이 개별 제어 능력을 방해하기보다 향상시킨다는 것을 보여줍니다. Worldscape-MoE는 WorldArena에서 강력한 결과를 달성하고, 보행 및 손 제어 지표를 개선하며, 강력한 분포 외 일반화를 보여주고, 추가 제어 데이터와 전문가가 통합됨에 따라 확장 동작을 입증합니다.
