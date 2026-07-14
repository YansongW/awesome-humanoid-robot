---
$id: ent_paper_worldscape_moe_a_unified_mixtu_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Worldscape-MoE: A Unified Mixture-of-Experts World Model for Scalable Heterogeneous
    Action Control'
  zh: 'Worldscape-MoE: A Unified Mixture-of-Experts World Model for Scalable Heterogeneous
    Action Control'
  ko: 'Worldscape-MoE: A Unified Mixture-of-Experts World Model for Scalable Heterogeneous
    Action Control'
summary:
  en: "arXiv:2607.03964v1 Announce Type: new \nAbstract: World models are rapidly\
    \ becoming a core infrastructure for embodied intelligence and interactive agents:\
    \ they provide controllable simulators in which agents can perceive, act, forecast,\
    \ and acquire scalable experience. Yet current video generation world models are\
    \ still organized around isolated control interfaces, such as camera trajectories,\
    \ robot actions, or hand-joint signals. This fragmentation is increasingly a scaling\
    \ bottleneck. The central challenge is not the absence of controllable generators,\
    \ but the lack of a unified and extensible learning framework that can absorb\
    \ heterogeneous action supervision while preserving a shared model of world dynamics.\
    \ In this work, we introduce Worldscape-MoE, a Mixture-of-Experts world model\
    \ built on Diffusion Transformers for scalable heterogeneous action control. Our\
    \ key observation is that different controls specify different interfaces to the\
    \ same underlying world: although their representations differ, they constrain\
    \ shared physical regularities, scene dynamics, and interaction semantics. Worldscape-MoE\
    \ operationalizes this observation through modality-aware control injection, shared\
    \ and control-specific experts, and a progressive MoE tuning strategy that supports\
    \ continual extension to new action modalities. Experiments across locomotion,\
    \ robotic manipulation, and egocentric hand control show that heterogeneous supervision\
    \ improves rather than interferes with individual control capabilities. Worldscape-MoE\
    \ achieves strong results on WorldArena, improves locomotion and hand-control\
    \ metrics, exhibits robust out-of-distribution generalization, and demonstrates\
    \ scaling behavior as additional control data and experts are integrated."
  zh: "arXiv:2607.03964v1 Announce Type: new \nAbstract: World models are rapidly\
    \ becoming a core infrastructure for embodied intelligence and interactive agents:\
    \ they provide controllable simulators in which agents can perceive, act, forecast,\
    \ and acquire scalable experience. Yet current video generation world models are\
    \ still organized around isolated control interfaces, such as camera trajectories,\
    \ robot actions, or hand-joint signals. This fragmentation is increasingly a scaling\
    \ bottleneck. The central challenge is not the absence of controllable generators,\
    \ but the lack of a unified and extensible learning framework that can absorb\
    \ heterogeneous action supervision while preserving a shared model of world dynamics.\
    \ In this work, we introduce Worldscape-MoE, a Mixture-of-Experts world model\
    \ built on Diffusion Transformers for scalable heterogeneous action control. Our\
    \ key observation is that different controls specify different interfaces to the\
    \ same underlying world: although their representations differ, they constrain\
    \ shared physical regularities, scene dynamics, and interaction semantics. Worldscape-MoE\
    \ operationalizes this observation through modality-aware control injection, shared\
    \ and control-specific experts, and a progressive MoE tuning strategy that supports\
    \ continual extension to new action modalities. Experiments across locomotion,\
    \ robotic manipulation, and egocentric hand control show that heterogeneous supervision\
    \ improves rather than interferes with individual control capabilities. Worldscape-MoE\
    \ achieves strong results on WorldArena, improves locomotion and hand-control\
    \ metrics, exhibits robust out-of-distribution generalization, and demonstrates\
    \ scaling behavior as additional control data and experts are integrated."
  ko: "arXiv:2607.03964v1 Announce Type: new \nAbstract: World models are rapidly\
    \ becoming a core infrastructure for embodied intelligence and interactive agents:\
    \ they provide controllable simulators in which agents can perceive, act, forecast,\
    \ and acquire scalable experience. Yet current video generation world models are\
    \ still organized around isolated control interfaces, such as camera trajectories,\
    \ robot actions, or hand-joint signals. This fragmentation is increasingly a scaling\
    \ bottleneck. The central challenge is not the absence of controllable generators,\
    \ but the lack of a unified and extensible learning framework that can absorb\
    \ heterogeneous action supervision while preserving a shared model of world dynamics.\
    \ In this work, we introduce Worldscape-MoE, a Mixture-of-Experts world model\
    \ built on Diffusion Transformers for scalable heterogeneous action control. Our\
    \ key observation is that different controls specify different interfaces to the\
    \ same underlying world: although their representations differ, they constrain\
    \ shared physical regularities, scene dynamics, and interaction semantics. Worldscape-MoE\
    \ operationalizes this observation through modality-aware control injection, shared\
    \ and control-specific experts, and a progressive MoE tuning strategy that supports\
    \ continual extension to new action modalities. Experiments across locomotion,\
    \ robotic manipulation, and egocentric hand control show that heterogeneous supervision\
    \ improves rather than interferes with individual control capabilities. Worldscape-MoE\
    \ achieves strong results on WorldArena, improves locomotion and hand-control\
    \ metrics, exhibits robust out-of-distribution generalization, and demonstrates\
    \ scaling behavior as additional control data and experts are integrated."
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
  reviewed_at: '2026-07-08'
  confidence: medium
  notes: Imported via ingestion framework from source_type=paper.
sources:
- id: src_001
  type: paper
  title: 'Worldscape-MoE: A Unified Mixture-of-Experts World Model for Scalable Heterogeneous
    Action Control (arXiv)'
  url: https://arxiv.org/abs/2607.03964
  date: '2026'
  accessed_at: '2026-07-08'
---

## 概述
arXiv:2607.03964v1 Announce Type: new 
Abstract: World models are rapidly becoming a core infrastructure for embodied intelligence and interactive agents: they provide controllable simulators in which agents can perceive, act, forecast, and acquire scalable experience. Yet current video generation world models are still organized around isolated control interfaces, such as camera trajectories, robot actions, or hand-joint signals. This fragmentation is increasingly a scaling bottleneck. The central challenge is not the absence of controllable generators, but the lack of a unified and extensible learning framework that can absorb heterogeneous action supervision while preserving a shared model of world dynamics. In this work, we introduce Worldscape-MoE, a Mixture-of-Experts world model built on Diffusion Transformers for scalable heterogeneous action control. Our key observation is that different controls specify different interfaces to the same underlying world: although their representations differ, they constrain shared physical regularities, scene dynamics, and interaction semantics. Worldscape-MoE operationalizes this observation through modality-aware control injection, shared and control-specific experts, and a progressive MoE tuning strategy that supports continual extension to new action modalities. Experiments across locomotion, robotic manipulation, and egocentric hand control show that heterogeneous supervision improves rather than interferes with individual control capabilities. Worldscape-MoE achieves strong results on WorldArena, improves locomotion and hand-control metrics, exhibits robust out-of-distribution generalization, and demonstrates scaling behavior as additional control data and experts are integrated.

## Overview
arXiv:2607.03964v1 Announce Type: new 
Abstract: World models are rapidly becoming a core infrastructure for embodied intelligence and interactive agents: they provide controllable simulators in which agents can perceive, act, forecast, and acquire scalable experience. Yet current video generation world models are still organized around isolated control interfaces, such as camera trajectories, robot actions, or hand-joint signals. This fragmentation is increasingly a scaling bottleneck. The central challenge is not the absence of controllable generators, but the lack of a unified and extensible learning framework that can absorb heterogeneous action supervision while preserving a shared model of world dynamics. In this work, we introduce Worldscape-MoE, a Mixture-of-Experts world model built on Diffusion Transformers for scalable heterogeneous action control. Our key observation is that different controls specify different interfaces to the same underlying world: although their representations differ, they constrain shared physical regularities, scene dynamics, and interaction semantics. Worldscape-MoE operationalizes this observation through modality-aware control injection, shared and control-specific experts, and a progressive MoE tuning strategy that supports continual extension to new action modalities. Experiments across locomotion, robotic manipulation, and egocentric hand control show that heterogeneous supervision improves rather than interferes with individual control capabilities. Worldscape-MoE achieves strong results on WorldArena, improves locomotion and hand-control metrics, exhibits robust out-of-distribution generalization, and demonstrates scaling behavior as additional control data and experts are integrated.

## 개요
arXiv:2607.03964v1 Announce Type: new 
Abstract: World models are rapidly becoming a core infrastructure for embodied intelligence and interactive agents: they provide controllable simulators in which agents can perceive, act, forecast, and acquire scalable experience. Yet current video generation world models are still organized around isolated control interfaces, such as camera trajectories, robot actions, or hand-joint signals. This fragmentation is increasingly a scaling bottleneck. The central challenge is not the absence of controllable generators, but the lack of a unified and extensible learning framework that can absorb heterogeneous action supervision while preserving a shared model of world dynamics. In this work, we introduce Worldscape-MoE, a Mixture-of-Experts world model built on Diffusion Transformers for scalable heterogeneous action control. Our key observation is that different controls specify different interfaces to the same underlying world: although their representations differ, they constrain shared physical regularities, scene dynamics, and interaction semantics. Worldscape-MoE operationalizes this observation through modality-aware control injection, shared and control-specific experts, and a progressive MoE tuning strategy that supports continual extension to new action modalities. Experiments across locomotion, robotic manipulation, and egocentric hand control show that heterogeneous supervision improves rather than interferes with individual control capabilities. Worldscape-MoE achieves strong results on WorldArena, improves locomotion and hand-control metrics, exhibits robust out-of-distribution generalization, and demonstrates scaling behavior as additional control data and experts are integrated.
