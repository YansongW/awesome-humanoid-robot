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
  zh: This article provides the first survey of computational models of emotion in reinforcement learning (RL) agents. The
    survey focuses on agent/robot emotions, and mostly ignores human user emotions. Emotions are recognized as functional
    in decision-making by influencing motivation and action selection. Therefore, computational emotion models are usually
    grounded in the agent's decision making architecture, of which RL is an important subclass. Studying emotions in RL-based
    agents is useful for three research fields. For machine learning (ML) researchers, emotion models may improve learning
    effic
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/1705.05172v1.
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
This article provides the first survey of computational models of emotion in reinforcement learning (RL) agents. The survey focuses on agent/robot emotions, and mostly ignores human user emotions. Emotions are recognized as functional in decision-making by influencing motivation and action selection. Therefore, computational emotion models are usually grounded in the agent's decision making architecture, of which RL is an important subclass. Studying emotions in RL-based agents is useful for three research fields. For machine learning (ML) researchers, emotion models may improve learning efficiency. For the interactive ML and human-robot interaction (HRI) community, emotions can communicate state and enhance user investment. Lastly, it allows affective modelling (AM) researchers to investigate their emotion theories in a successful AI agent class. This survey provides background on emotion theory and RL. It systematically addresses 1) from what underlying dimensions (e.g., homeostasis, appraisal) emotions can be derived and how these can be modelled in RL-agents, 2) what types of emotions have been derived from these dimensions, and 3) how these emotions may either influence the learning efficiency of the agent or be useful as social signals. We also systematically compare evaluation criteria, and draw connections to important RL sub-domains like (intrinsic) motivation and model-based RL. In short, this survey provides both a practical overview for engineers wanting to implement emotions in their RL agents, and identifies challenges and directions for future emotion-RL research.

## 核心内容
This article provides the first survey of computational models of emotion in reinforcement learning (RL) agents. The survey focuses on agent/robot emotions, and mostly ignores human user emotions. Emotions are recognized as functional in decision-making by influencing motivation and action selection. Therefore, computational emotion models are usually grounded in the agent's decision making architecture, of which RL is an important subclass. Studying emotions in RL-based agents is useful for three research fields. For machine learning (ML) researchers, emotion models may improve learning efficiency. For the interactive ML and human-robot interaction (HRI) community, emotions can communicate state and enhance user investment. Lastly, it allows affective modelling (AM) researchers to investigate their emotion theories in a successful AI agent class. This survey provides background on emotion theory and RL. It systematically addresses 1) from what underlying dimensions (e.g., homeostasis, appraisal) emotions can be derived and how these can be modelled in RL-agents, 2) what types of emotions have been derived from these dimensions, and 3) how these emotions may either influence the learning efficiency of the agent or be useful as social signals. We also systematically compare evaluation criteria, and draw connections to important RL sub-domains like (intrinsic) motivation and model-based RL. In short, this survey provides both a practical overview for engineers wanting to implement emotions in their RL agents, and identifies challenges and directions for future emotion-RL research.

## 参考
- http://arxiv.org/abs/1705.05172v1

## Overview
This article provides the first survey of computational models of emotion in reinforcement learning (RL) agents. The survey focuses on agent/robot emotions, and mostly ignores human user emotions. Emotions are recognized as functional in decision-making by influencing motivation and action selection. Therefore, computational emotion models are usually grounded in the agent's decision making architecture, of which RL is an important subclass. Studying emotions in RL-based agents is useful for three research fields. For machine learning (ML) researchers, emotion models may improve learning efficiency. For the interactive ML and human-robot interaction (HRI) community, emotions can communicate state and enhance user investment. Lastly, it allows affective modelling (AM) researchers to investigate their emotion theories in a successful AI agent class. This survey provides background on emotion theory and RL. It systematically addresses 1) from what underlying dimensions (e.g., homeostasis, appraisal) emotions can be derived and how these can be modelled in RL-agents, 2) what types of emotions have been derived from these dimensions, and 3) how these emotions may either influence the learning efficiency of the agent or be useful as social signals. We also systematically compare evaluation criteria, and draw connections to important RL sub-domains like (intrinsic) motivation and model-based RL. In short, this survey provides both a practical overview for engineers wanting to implement emotions in their RL agents, and identifies challenges and directions for future emotion-RL research.

## Content
This article provides the first survey of computational models of emotion in reinforcement learning (RL) agents. The survey focuses on agent/robot emotions, and mostly ignores human user emotions. Emotions are recognized as functional in decision-making by influencing motivation and action selection. Therefore, computational emotion models are usually grounded in the agent's decision making architecture, of which RL is an important subclass. Studying emotions in RL-based agents is useful for three research fields. For machine learning (ML) researchers, emotion models may improve learning efficiency. For the interactive ML and human-robot interaction (HRI) community, emotions can communicate state and enhance user investment. Lastly, it allows affective modelling (AM) researchers to investigate their emotion theories in a successful AI agent class. This survey provides background on emotion theory and RL. It systematically addresses 1) from what underlying dimensions (e.g., homeostasis, appraisal) emotions can be derived and how these can be modelled in RL-agents, 2) what types of emotions have been derived from these dimensions, and 3) how these emotions may either influence the learning efficiency of the agent or be useful as social signals. We also systematically compare evaluation criteria, and draw connections to important RL sub-domains like (intrinsic) motivation and model-based RL. In short, this survey provides both a practical overview for engineers wanting to implement emotions in their RL agents, and identifies challenges and directions for future emotion-RL research.

## 개요
이 논문은 강화 학습(RL) 에이전트에서 감정의 계산 모델에 대한 최초의 조사를 제공합니다. 이 조사는 에이전트/로봇의 감정에 초점을 맞추며, 인간 사용자의 감정은 대부분 무시합니다. 감정은 동기 부여와 행동 선택에 영향을 미쳐 의사 결정에서 기능적인 역할을 하는 것으로 인식됩니다. 따라서 계산 감정 모델은 일반적으로 에이전트의 의사 결정 아키텍처에 기반하며, RL은 그 중요한 하위 클래스입니다. RL 기반 에이전트에서 감정을 연구하는 것은 세 가지 연구 분야에 유용합니다. 머신러닝(ML) 연구자에게 감정 모델은 학습 효율성을 향상시킬 수 있습니다. 대화형 ML 및 인간-로봇 상호작용(HRI) 커뮤니티에게 감정은 상태를 전달하고 사용자 투자를 증가시킬 수 있습니다. 마지막으로, 정서 모델링(AM) 연구자들이 성공적인 AI 에이전트 클래스에서 자신의 감정 이론을 조사할 수 있게 합니다. 이 조사는 감정 이론과 RL에 대한 배경 지식을 제공합니다. 체계적으로 다루는 내용은 1) 어떤 기반 차원(예: 항상성, 평가)에서 감정이 도출될 수 있으며 이를 RL 에이전트에서 어떻게 모델링할 수 있는지, 2) 이러한 차원에서 어떤 유형의 감정이 도출되었는지, 3) 이러한 감정이 에이전트의 학습 효율성에 영향을 미치거나 사회적 신호로 유용할 수 있는 방법입니다. 또한 평가 기준을 체계적으로 비교하고, (내재적) 동기 부여 및 모델 기반 RL과 같은 중요한 RL 하위 영역과의 연결을 도출합니다. 요약하면, 이 조사는 RL 에이전트에 감정을 구현하려는 엔지니어를 위한 실용적인 개요를 제공할 뿐만 아니라 미래의 감정-RL 연구를 위한 과제와 방향을 식별합니다.

## 핵심 내용
이 논문은 강화 학습(RL) 에이전트에서 감정의 계산 모델에 대한 최초의 조사를 제공합니다. 이 조사는 에이전트/로봇의 감정에 초점을 맞추며, 인간 사용자의 감정은 대부분 무시합니다. 감정은 동기 부여와 행동 선택에 영향을 미쳐 의사 결정에서 기능적인 역할을 하는 것으로 인식됩니다. 따라서 계산 감정 모델은 일반적으로 에이전트의 의사 결정 아키텍처에 기반하며, RL은 그 중요한 하위 클래스입니다. RL 기반 에이전트에서 감정을 연구하는 것은 세 가지 연구 분야에 유용합니다. 머신러닝(ML) 연구자에게 감정 모델은 학습 효율성을 향상시킬 수 있습니다. 대화형 ML 및 인간-로봇 상호작용(HRI) 커뮤니티에게 감정은 상태를 전달하고 사용자 투자를 증가시킬 수 있습니다. 마지막으로, 정서 모델링(AM) 연구자들이 성공적인 AI 에이전트 클래스에서 자신의 감정 이론을 조사할 수 있게 합니다. 이 조사는 감정 이론과 RL에 대한 배경 지식을 제공합니다. 체계적으로 다루는 내용은 1) 어떤 기반 차원(예: 항상성, 평가)에서 감정이 도출될 수 있으며 이를 RL 에이전트에서 어떻게 모델링할 수 있는지, 2) 이러한 차원에서 어떤 유형의 감정이 도출되었는지, 3) 이러한 감정이 에이전트의 학습 효율성에 영향을 미치거나 사회적 신호로 유용할 수 있는 방법입니다. 또한 평가 기준을 체계적으로 비교하고, (내재적) 동기 부여 및 모델 기반 RL과 같은 중요한 RL 하위 영역과의 연결을 도출합니다. 요약하면, 이 조사는 RL 에이전트에 감정을 구현하려는 엔지니어를 위한 실용적인 개요를 제공할 뿐만 아니라 미래의 감정-RL 연구를 위한 과제와 방향을 식별합니다.
