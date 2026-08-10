---
$id: ent_paper_moerland_emotion_in_reinforcement_learn_2017
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Emotion in Reinforcement Learning Agents and Robots: A Survey'
  zh: 强化学习智能体与机器人中的情绪：综述
  ko: '강화학습 에이전트와 로봇의 감정: 서베이'
summary:
  en: A 2017 survey that systematically reviews computational models of emotion in reinforcement learning agents and robots,
    organizing the literature around emotion elicitation, emotion types, and the functions emotions serve in learning and
    social signaling.
  zh: 这篇2017年的综述系统梳理了强化学习智能体与机器人中的情感计算模型，围绕情感诱发机制、情感类型及其在学习与社会信号传递中的功能展开。作者指出情感通过影响动机与动作选择来辅助决策，并首次将情感模型与RL架构进行系统性关联分析。
  ko: 2017년에 발표된 서베이로, 강화학습 에이전트와 로봇에서 감정의 계산 모델을 체계적으로 정리하며 감정 유발, 감정 유형, 학습 및 사회적 신호 전달에서 감정의 기능을 중심으로 문헌을 분류한다.
domains:
- 07_ai_models_algorithms
- 11_applications_markets
layers:
- intelligence
- validation_markets
functional_roles:
- knowledge
- intelligence
tags:
- emotion_modeling
- reinforcement_learning
- human_robot_interaction
- intrinsic_motivation
- affective_computing
- social_robotics
- survey
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/1705.05172v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (748 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: 'Emotion in Reinforcement Learning Agents and Robots: A Survey'
  url: https://arxiv.org/abs/1705.05172
  date: '2017'
  accessed_at: '2026-06-26'
theoretical_depth:
- method
---
## 概述
该综述聚焦于RL智能体/机器人的情感建模，而非人类用户情感。情感被视作决策功能组件，通过调节动机与动作选择发挥作用。研究覆盖三个交叉领域：机器学习研究者可借助情感模型提升学习效率；交互式ML与人机交互领域可通过情感传递状态信息并增强用户参与度；情感建模研究者则能在成功的AI智能体类别中验证其情感理论。文章系统梳理了情感从内稳态、评估等底层维度的衍生方式，RL智能体中已实现的情感类型，以及情感如何影响学习效率或作为社会信号。此外还比较了评估标准，并与内在动机、基于模型的RL等子领域建立联系。

## 核心内容
### 研究背景与动机
- 情感在RL智能体中的功能定位：通过影响动机与动作选择辅助决策，因此情感计算模型通常嵌入智能体的决策架构中，RL是该架构的重要子类。
- 三大研究领域价值：
  - **机器学习**：情感模型可能提升学习效率
  - **交互式ML与HRI**：情感可传递状态信息并增强用户参与度
  - **情感建模**：在成功AI智能体类别中验证情感理论

### 核心框架
- 情感理论背景：涵盖内稳态、评估等底层维度
- 情感类型：从上述维度衍生出的具体情感类别
- 功能分类：
  - **学习效率影响**：通过调节探索-利用平衡、奖励信号等机制
  - **社会信号功能**：通过表情、动作等传递智能体内部状态

### 实验设置与评估
- 系统比较不同情感模型的评估标准
- 与RL子领域关联：
  - **内在动机**：情感作为内在奖励信号的来源
  - **基于模型的RL**：情感预测辅助规划

### 结论与挑战
- 为工程师提供实现RL智能体情感功能的实用指南
- 识别未来研究方向：情感与RL的深度整合、跨领域验证、动态情感演化机制等

## Overview
This article provides the first survey of computational models of emotion in reinforcement learning (RL) agents. The survey focuses on agent/robot emotions, and mostly ignores human user emotions. Emotions are recognized as functional in decision-making by influencing motivation and action selection. Therefore, computational emotion models are usually grounded in the agent's decision making architecture, of which RL is an important subclass. Studying emotions in RL-based agents is useful for three research fields. For machine learning (ML) researchers, emotion models may improve learning efficiency. For the interactive ML and human-robot interaction (HRI) community, emotions can communicate state and enhance user investment. Lastly, it allows affective modelling (AM) researchers to investigate their emotion theories in a successful AI agent class. This survey provides background on emotion theory and RL. It systematically addresses 1) from what underlying dimensions (e.g., homeostasis, appraisal) emotions can be derived and how these can be modelled in RL-agents, 2) what types of emotions have been derived from these dimensions, and 3) how these emotions may either influence the learning efficiency of the agent or be useful as social signals. We also systematically compare evaluation criteria, and draw connections to important RL sub-domains like (intrinsic) motivation and model-based RL. In short, this survey provides both a practical overview for engineers wanting to implement emotions in their RL agents, and identifies challenges and directions for future emotion-RL research.

## 参考
- http://arxiv.org/abs/1705.05172v1

## 개요
본综述은 인간 사용자의 감정이 아닌 RL 에이전트/로봇의 감정 모델링에 초점을 맞춘다. 감정은 의사결정의 기능적 구성 요소로 간주되며, 동기와 행동 선택을 조절하는 역할을 한다. 연구는 세 가지 교차 영역을 다룬다: 머신러닝 연구자는 감정 모델을 통해 학습 효율성을 높일 수 있고, 인터랙티브 ML 및 인간-로봇 상호작용 분야는 감정을 통해 상태 정보를 전달하고 사용자 참여를 강화할 수 있으며, 감정 모델링 연구자는 성공적인 AI 에이전트 범주에서 자신의 감정 이론을 검증할 수 있다. 이 글은 항상성, 평가와 같은 하위 차원에서 감정이 파생되는 방식, RL 에이전트에서 구현된 감정 유형, 그리고 감정이 학습 효율성에 미치는 영향 또는 사회적 신호로서의 역할을 체계적으로 정리한다. 또한 평가 기준을 비교하고, 내재적 동기, 모델 기반 RL과 같은 하위 분야와의 연관성을 확립한다.

## 핵심 내용
### 연구 배경 및 동기
- RL 에이전트에서 감정의 기능적 위치: 동기와 행동 선택에 영향을 주어 의사결정을 보조하므로, 감정 계산 모델은 일반적으로 에이전트의 의사결정 아키텍처에 내장되며, RL은 해당 아키텍처의 중요한 하위 클래스이다.
- 세 가지 주요 연구 분야의 가치:
  - **머신러닝**: 감정 모델이 학습 효율성을 향상시킬 수 있음
  - **인터랙티브 ML 및 HRI**: 감정이 상태 정보를 전달하고 사용자 참여를 강화할 수 있음
  - **감정 모델링**: 성공적인 AI 에이전트 범주에서 감정 이론을 검증

### 핵심 프레임워크
- 감정 이론 배경: 항상성, 평가와 같은 하위 차원을 포함
- 감정 유형: 위 차원에서 파생된 구체적인 감정 범주
- 기능 분류:
  - **학습 효율성 영향**: 탐험-활용 균형, 보상 신호 등의 메커니즘 조절
  - **사회적 신호 기능**: 표정, 행동 등을 통해 에이전트 내부 상태 전달

### 실험 설정 및 평가
- 서로 다른 감정 모델의 평가 기준을 체계적으로 비교
- RL 하위 분야와의 연관성:
  - **내재적 동기**: 감정을 내재적 보상 신호의 원천으로 활용
  - **모델 기반 RL**: 감정 예측이 계획을 보조

### 결론 및 도전 과제
- 엔지니어에게 RL 에이전트 감정 기능 구현을 위한 실용적 가이드 제공
- 향후 연구 방향 식별: 감정과 RL의 심층 통합, 교차 영역 검증, 동적 감정 진화 메커니즘 등
