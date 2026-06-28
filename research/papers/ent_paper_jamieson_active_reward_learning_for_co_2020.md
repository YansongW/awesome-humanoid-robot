---
$id: ent_paper_jamieson_active_reward_learning_for_co_2020
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Active Reward Learning for Co-Robotic Vision Based Exploration in Bandwidth
    Limited Environments
  zh: 带宽受限环境下协同机器人视觉探索的主动奖励学习
  ko: 대역폭 제한 환경에서의 공동 로봇 비전 기반 탐사를 위한 능동 보상 학습
summary:
  en: A POMDP-based framework for autonomous visual exploration that uses regret-minimizing
    active reward learning to decide when a bandwidth-limited robot should query a
    human operator, evaluated on synthetic Voronoi topic maps and a coral-reef photomosaic.
  zh: 一种基于POMDP的自主视觉探索框架，利用后悔最小化的主动奖励学习来决定带宽受限机器人何时查询人类操作员，并在合成Voronoi主题图和珊瑚礁照片镶嵌图上进行了评估。
  ko: 대역폭이 제한된 로봇이 언제 인간 운영자에게 질의해야 하는지 결정하기 위해 후회 최소화 기반 능동 보상 학습을 사용하는 POMDP 기반
    자율 시각 탐사 프레임워크로, 합성 Voronoi 주제 맵과 산호초 사진 모자이크에서 평가되었다.
domains:
- 07_ai_models_algorithms
- 08_software_middleware
- 02_components
layers:
- intelligence
- upstream
functional_roles:
- intelligence
- knowledge
tags:
- active_learning
- reward_learning
- pomdp
- human_robot_teaming
- visual_exploration
- bandwidth_limited
- autonomous_navigation
- decision_making
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-06-28'
  confidence: medium
  notes: AI-extracted from metadata and abstract; full-text review required to confirm
    section citations and complete relationship set.; approved by autonomous review
    workflow.
sources:
- id: src_001
  type: paper
  title: Active Reward Learning for Co-Robotic Vision Based Exploration in Bandwidth
    Limited Environments
  url: https://arxiv.org/abs/2003.05016
  date: '2020'
  accessed_at: '2026-06-28'
theoretical_depth:
- method
---

## Overview

The paper addresses the problem of a robot that must autonomously decide where to navigate to collect new and scientifically relevant images while communicating sparingly with a human operator. The authors formulate this co-robotic visual exploration task as a partially observable Markov decision process (POMDP), deriving constraints and design principles for the observation model, reward model, and communication strategy. To handle the high-dimensional observation space and scarcity of relevant training data, they learn a low-dimensional semantic spatial observation model and an online reward model from topic representations.

The core methodological contribution is a regret-minimizing active reward learning criterion. Instead of merely maximizing information gain about the reward function, the robot selects queries that minimize expected path regret, thereby improving mission-level reward collection in bandwidth-limited settings. The approach is evaluated through simulations on synthetic Voronoi topic maps and a real-world coral-reef photomosaic from the 100 Islands Challenge.

## Key Contributions

- POMDP formulation for vision-based scientific exploration under bandwidth constraints.
- Design principles for observation models, reward models, and communication strategies in co-robotic systems.
- Novel regret-minimizing active reward learning criterion for online query selection.
- Simulation evaluation demonstrating up to 17% more reward per mission than the next-best criterion in some bandwidth-limited environments.

## Relevance to Humanoid Robotics

Although the paper focuses on underwater and aerial visual exploration platforms, its active reward learning and low-bandwidth human-robot teaming framework are directly transferable to humanoid robots deployed in remote or communication-constrained industrial environments. Humanoids operating in disaster zones, subsea facilities, or planetary surface missions can use similar POMDP-based decision-making to decide when to request operator input, maximizing scientific or operational value while conserving communication resources. The regret-based query-selection principle offers a practical way to balance autonomy with human oversight in safety-critical humanoid deployments.
