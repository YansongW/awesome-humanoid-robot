---
$id: ent_paper_ayub_interactive_continual_learning_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Interactive Continual Learning Architecture for Long-Term Personalization of Home Service Robots
  zh: 面向家庭服务机器人长期个性化的交互式持续学习架构
  ko: 가정 서비스 로봇의 장기 개인화를 위한 대화형 지속 학습 아키텍처
summary:
  en: This paper proposes an interactive continual learning architecture that enables a mobile manipulator to learn semantic
    knowledge of objects and contexts from real-time human-robot interaction, and validates it through two months of physical
    robot experiments.
  zh: For robots to perform assistive tasks in unstructured home environments, they must learn and reason on the semantic
    knowledge of the environments. Despite a resurgence in the development of semantic reasoning architectures, these methods
    assume that all the training data is available a priori. However, each user's environment is unique and can continue to
    change over time, which makes these methods unsuitable for personalized home service robots. Although research in continual
    learning develops methods that can learn and adapt over time, most of these methods are tested in the narrow context o
  ko: 본 논문은 실시간 인간-로봇 상호작용을 통해 물체와 맥락의 의미적 지식을 학습할 수 있는 대화형 지속 학습 아키텍처를 제안하고, 두 달간의 실제 로봇 실험을 통해 검증하였다.
domains:
- 07_ai_models_algorithms
- 08_software_middleware
- 11_applications_markets
layers:
- intelligence
- validation_markets
functional_roles:
- intelligence
- knowledge
tags:
- continual_learning
- interactive_machine_learning
- semantic_reasoning
- home_service_robot
- mobile_manipulator
- few_shot_learning
- human_robot_interaction
- cognitive_robotics
- long_term_memory
- personalization
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2403.03462v1.
sources:
- id: src_001
  type: paper
  title: Interactive Continual Learning Architecture for Long-Term Personalization of Home Service Robots
  url: https://arxiv.org/abs/2403.03462
  date: '2024'
  accessed_at: '2026-06-27'
theoretical_depth:
- method
---

## 概述
For robots to perform assistive tasks in unstructured home environments, they must learn and reason on the semantic knowledge of the environments. Despite a resurgence in the development of semantic reasoning architectures, these methods assume that all the training data is available a priori. However, each user's environment is unique and can continue to change over time, which makes these methods unsuitable for personalized home service robots. Although research in continual learning develops methods that can learn and adapt over time, most of these methods are tested in the narrow context of object classification on static image datasets. In this paper, we combine ideas from continual learning, semantic reasoning, and interactive machine learning literature and develop a novel interactive continual learning architecture for continual learning of semantic knowledge in a home environment through human-robot interaction. The architecture builds on core cognitive principles of learning and memory for efficient and real-time learning of new knowledge from humans. We integrate our architecture with a physical mobile manipulator robot and perform extensive system evaluations in a laboratory environment over two months. Our results demonstrate the effectiveness of our architecture to allow a physical robot to continually adapt to the changes in the environment from limited data provided by the users (experimenters), and use the learned knowledge to perform object fetching tasks.

## 核心内容
For robots to perform assistive tasks in unstructured home environments, they must learn and reason on the semantic knowledge of the environments. Despite a resurgence in the development of semantic reasoning architectures, these methods assume that all the training data is available a priori. However, each user's environment is unique and can continue to change over time, which makes these methods unsuitable for personalized home service robots. Although research in continual learning develops methods that can learn and adapt over time, most of these methods are tested in the narrow context of object classification on static image datasets. In this paper, we combine ideas from continual learning, semantic reasoning, and interactive machine learning literature and develop a novel interactive continual learning architecture for continual learning of semantic knowledge in a home environment through human-robot interaction. The architecture builds on core cognitive principles of learning and memory for efficient and real-time learning of new knowledge from humans. We integrate our architecture with a physical mobile manipulator robot and perform extensive system evaluations in a laboratory environment over two months. Our results demonstrate the effectiveness of our architecture to allow a physical robot to continually adapt to the changes in the environment from limited data provided by the users (experimenters), and use the learned knowledge to perform object fetching tasks.

## 参考
- http://arxiv.org/abs/2403.03462v1


