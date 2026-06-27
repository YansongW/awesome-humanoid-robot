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
  en: A 2017 survey that systematically reviews computational models of emotion in
    reinforcement learning agents and robots, organizing the literature around emotion
    elicitation, emotion types, and the functions emotions serve in learning and social
    signaling.
  zh: 2017年发表的综述，系统回顾了强化学习智能体与机器人中情绪的计算模型，围绕情绪诱发、情绪类型以及情绪在学习与社会信号传递中的功能对文献进行分类。
  ko: 2017년에 발표된 서베이로, 강화학습 에이전트와 로봇에서 감정의 계산 모델을 체계적으로 정리하며 감정 유발, 감정 유형, 학습 및 사회적
    신호 전달에서 감정의 기능을 중심으로 문헌을 분류한다.
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
  reviewed_at: '2026-06-26'
  confidence: medium
  notes: AI-extracted from the paper metadata and abstract; full-text verification
    and human review are required before promotion.
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

## Overview

This survey provides the first systematic review of computational models of emotion in reinforcement learning (RL) agents and robots. It begins with background on emotion theory and RL, then organizes the literature along three core dimensions: the underlying mechanisms from which emotions are elicited, the representational forms that emotions take, and the functional roles that emotions play within an agent's learning or interaction loop.

The authors categorize emotion elicitation into homeostasis/extrinsic motivation, appraisal/intrinsic motivation, value or reward-based derivation, and hard-wired mappings. They distinguish emotion types as categorical (e.g., discrete emotion labels) or dimensional (e.g., valence-arousal space). Emotion functions are classified as reward modification, state modification, meta-learning, action selection, or epiphenomenon. The survey also compares evaluation criteria and embodiment scenarios, and explicitly links emotion modeling to RL sub-fields such as intrinsic motivation and model-based RL.

Overall, the paper serves as both a practical overview for engineers who want to implement emotions in RL agents and a research agenda that identifies open challenges and future directions in emotion-RL integration.

## Key Contributions

- First comprehensive survey bridging emotion modelling and reinforcement learning
- Taxonomy of emotion elicitation, emotion types, and emotion functions in RL agents
- Systematic comparison of evaluation criteria and embodiment scenarios across emotion-RL research
- Practical guidelines for engineers implementing emotions in RL-based agents and robots
- Identification of open challenges and future directions for emotion-RL research

## Relevance to Humanoid Robotics

Although the survey is not specifically about humanoid hardware or mass production, its focus on social robotics and human-robot interaction is directly relevant to humanoid deployment. Humanoid robots are expected to operate in human-centric environments where transparent, legible behavior and social signaling improve user trust, safety, and engagement. The surveyed emotion models offer ways for a humanoid robot to communicate its internal state, signal uncertainty or goals, and elicit user empathy.

For the knowledge base, the paper provides a method-level taxonomy that can inform the design of affective and interactive control systems in humanoid robots. Its emphasis on evaluation criteria and embodiment scenarios also helps connect algorithmic advances to real-world application requirements.
