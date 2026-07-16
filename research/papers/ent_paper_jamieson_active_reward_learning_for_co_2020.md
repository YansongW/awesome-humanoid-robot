---
$id: ent_paper_jamieson_active_reward_learning_for_co_2020
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Active Reward Learning for Co-Robotic Vision Based Exploration in Bandwidth Limited Environments
  zh: 带宽受限环境下协同机器人视觉探索的主动奖励学习
  ko: 대역폭 제한 환경에서의 공동 로봇 비전 기반 탐사를 위한 능동 보상 학습
summary:
  en: A POMDP-based framework for autonomous visual exploration that uses regret-minimizing active reward learning to decide
    when a bandwidth-limited robot should query a human operator, evaluated on synthetic Voronoi topic maps and a coral-reef
    photomosaic.
  zh: 一种基于POMDP的自主视觉探索框架，利用后悔最小化的主动奖励学习来决定带宽受限机器人何时查询人类操作员，并在合成Voronoi主题图和珊瑚礁照片镶嵌图上进行了评估。
  ko: 대역폭이 제한된 로봇이 언제 인간 운영자에게 질의해야 하는지 결정하기 위해 후회 최소화 기반 능동 보상 학습을 사용하는 POMDP 기반 자율 시각 탐사 프레임워크로, 합성 Voronoi 주제 맵과 산호초 사진
    모자이크에서 평가되었다.
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
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2003.05016v1.
sources:
- id: src_001
  type: paper
  title: Active Reward Learning for Co-Robotic Vision Based Exploration in Bandwidth Limited Environments
  url: https://arxiv.org/abs/2003.05016
  date: '2020'
  accessed_at: '2026-06-28'
theoretical_depth:
- method
---
## 概述
We present a novel POMDP problem formulation for a robot that must autonomously decide where to go to collect new and scientifically relevant images given a limited ability to communicate with its human operator. From this formulation we derive constraints and design principles for the observation model, reward model, and communication strategy of such a robot, exploring techniques to deal with the very high-dimensional observation space and scarcity of relevant training data. We introduce a novel active reward learning strategy based on making queries to help the robot minimize path "regret" online, and evaluate it for suitability in autonomous visual exploration through simulations. We demonstrate that, in some bandwidth-limited environments, this novel regret-based criterion enables the robotic explorer to collect up to 17% more reward per mission than the next-best criterion.

## 核心内容
We present a novel POMDP problem formulation for a robot that must autonomously decide where to go to collect new and scientifically relevant images given a limited ability to communicate with its human operator. From this formulation we derive constraints and design principles for the observation model, reward model, and communication strategy of such a robot, exploring techniques to deal with the very high-dimensional observation space and scarcity of relevant training data. We introduce a novel active reward learning strategy based on making queries to help the robot minimize path "regret" online, and evaluate it for suitability in autonomous visual exploration through simulations. We demonstrate that, in some bandwidth-limited environments, this novel regret-based criterion enables the robotic explorer to collect up to 17% more reward per mission than the next-best criterion.

## 参考
- http://arxiv.org/abs/2003.05016v1

## Overview
We present a novel POMDP problem formulation for a robot that must autonomously decide where to go to collect new and scientifically relevant images given a limited ability to communicate with its human operator. From this formulation we derive constraints and design principles for the observation model, reward model, and communication strategy of such a robot, exploring techniques to deal with the very high-dimensional observation space and scarcity of relevant training data. We introduce a novel active reward learning strategy based on making queries to help the robot minimize path "regret" online, and evaluate it for suitability in autonomous visual exploration through simulations. We demonstrate that, in some bandwidth-limited environments, this novel regret-based criterion enables the robotic explorer to collect up to 17% more reward per mission than the next-best criterion.

## Content
We present a novel POMDP problem formulation for a robot that must autonomously decide where to go to collect new and scientifically relevant images given a limited ability to communicate with its human operator. From this formulation we derive constraints and design principles for the observation model, reward model, and communication strategy of such a robot, exploring techniques to deal with the very high-dimensional observation space and scarcity of relevant training data. We introduce a novel active reward learning strategy based on making queries to help the robot minimize path "regret" online, and evaluate it for suitability in autonomous visual exploration through simulations. We demonstrate that, in some bandwidth-limited environments, this novel regret-based criterion enables the robotic explorer to collect up to 17% more reward per mission than the next-best criterion.

## 개요
본 논문에서는 인간 운영자와의 제한된 통신 능력 하에서 새로운 과학적 관련 이미지를 수집하기 위해 자율적으로 이동 경로를 결정해야 하는 로봇을 위한 새로운 POMDP 문제 공식을 제시합니다. 이 공식을 바탕으로 관찰 모델, 보상 모델 및 통신 전략에 대한 제약 조건과 설계 원칙을 도출하고, 매우 고차원적인 관찰 공간과 관련 훈련 데이터의 부족 문제를 해결하기 위한 기법을 탐구합니다. 또한 로봇이 온라인에서 경로 "후회(regret)"를 최소화하도록 돕기 위해 질의를 활용하는 새로운 능동적 보상 학습 전략을 소개하고, 시뮬레이션을 통해 자율 시각적 탐사에의 적합성을 평가합니다. 일부 대역폭이 제한된 환경에서 이 새로운 후회 기반 기준이 차선의 기준보다 임무당 최대 17% 더 많은 보상을 수집할 수 있음을 입증합니다.

## 핵심 내용
본 논문에서는 인간 운영자와의 제한된 통신 능력 하에서 새로운 과학적 관련 이미지를 수집하기 위해 자율적으로 이동 경로를 결정해야 하는 로봇을 위한 새로운 POMDP 문제 공식을 제시합니다. 이 공식을 바탕으로 관찰 모델, 보상 모델 및 통신 전략에 대한 제약 조건과 설계 원칙을 도출하고, 매우 고차원적인 관찰 공간과 관련 훈련 데이터의 부족 문제를 해결하기 위한 기법을 탐구합니다. 또한 로봇이 온라인에서 경로 "후회(regret)"를 최소화하도록 돕기 위해 질의를 활용하는 새로운 능동적 보상 학습 전략을 소개하고, 시뮬레이션을 통해 자율 시각적 탐사에의 적합성을 평가합니다. 일부 대역폭이 제한된 환경에서 이 새로운 후회 기반 기준이 차선의 기준보다 임무당 최대 17% 더 많은 보상을 수집할 수 있음을 입증합니다.
