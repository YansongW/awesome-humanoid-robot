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


