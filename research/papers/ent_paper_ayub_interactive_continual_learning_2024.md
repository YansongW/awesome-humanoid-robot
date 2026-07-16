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

## Overview
For robots to perform assistive tasks in unstructured home environments, they must learn and reason on the semantic knowledge of the environments. Despite a resurgence in the development of semantic reasoning architectures, these methods assume that all the training data is available a priori. However, each user's environment is unique and can continue to change over time, which makes these methods unsuitable for personalized home service robots. Although research in continual learning develops methods that can learn and adapt over time, most of these methods are tested in the narrow context of object classification on static image datasets. In this paper, we combine ideas from continual learning, semantic reasoning, and interactive machine learning literature and develop a novel interactive continual learning architecture for continual learning of semantic knowledge in a home environment through human-robot interaction. The architecture builds on core cognitive principles of learning and memory for efficient and real-time learning of new knowledge from humans. We integrate our architecture with a physical mobile manipulator robot and perform extensive system evaluations in a laboratory environment over two months. Our results demonstrate the effectiveness of our architecture to allow a physical robot to continually adapt to the changes in the environment from limited data provided by the users (experimenters), and use the learned knowledge to perform object fetching tasks.

## Content
For robots to perform assistive tasks in unstructured home environments, they must learn and reason on the semantic knowledge of the environments. Despite a resurgence in the development of semantic reasoning architectures, these methods assume that all the training data is available a priori. However, each user's environment is unique and can continue to change over time, which makes these methods unsuitable for personalized home service robots. Although research in continual learning develops methods that can learn and adapt over time, most of these methods are tested in the narrow context of object classification on static image datasets. In this paper, we combine ideas from continual learning, semantic reasoning, and interactive machine learning literature and develop a novel interactive continual learning architecture for continual learning of semantic knowledge in a home environment through human-robot interaction. The architecture builds on core cognitive principles of learning and memory for efficient and real-time learning of new knowledge from humans. We integrate our architecture with a physical mobile manipulator robot and perform extensive system evaluations in a laboratory environment over two months. Our results demonstrate the effectiveness of our architecture to allow a physical robot to continually adapt to the changes in the environment from limited data provided by the users (experimenters), and use the learned knowledge to perform object fetching tasks.

## 개요
로봇이 비정형 가정 환경에서 보조 작업을 수행하려면 환경의 의미론적 지식을 학습하고 추론할 수 있어야 합니다. 의미론적 추론 아키텍처 개발이 다시 활기를 띠고 있지만, 이러한 방법들은 모든 훈련 데이터가 사전에 제공된다고 가정합니다. 그러나 각 사용자의 환경은 고유하며 시간이 지남에 따라 계속 변화할 수 있기 때문에, 이러한 방법들은 개인화된 가정용 서비스 로봇에는 적합하지 않습니다. 지속적 학습(continual learning) 연구는 시간이 지남에 따라 학습하고 적응할 수 있는 방법을 개발하지만, 대부분의 방법은 정적 이미지 데이터셋에서 객체 분류라는 좁은 맥락에서만 테스트됩니다. 본 논문에서는 지속적 학습, 의미론적 추론, 그리고 상호작용형 머신러닝 문헌의 아이디어를 결합하여, 인간-로봇 상호작용을 통해 가정 환경에서 의미론적 지식을 지속적으로 학습하는 새로운 상호작용형 지속적 학습 아키텍처를 개발합니다. 이 아키텍처는 학습과 기억의 핵심 인지 원리를 기반으로 하여 인간으로부터 새로운 지식을 효율적이고 실시간으로 학습합니다. 우리는 이 아키텍처를 실제 모바일 매니퓰레이터 로봇에 통합하고, 2개월 동안 실험실 환경에서 광범위한 시스템 평가를 수행했습니다. 그 결과, 우리의 아키텍처가 실제 로봇이 사용자(실험자)가 제공한 제한된 데이터로 환경 변화에 지속적으로 적응하고, 학습된 지식을 활용하여 객체 가져오기 작업을 수행할 수 있음을 입증했습니다.

## 핵심 내용
로봇이 비정형 가정 환경에서 보조 작업을 수행하려면 환경의 의미론적 지식을 학습하고 추론할 수 있어야 합니다. 의미론적 추론 아키텍처 개발이 다시 활기를 띠고 있지만, 이러한 방법들은 모든 훈련 데이터가 사전에 제공된다고 가정합니다. 그러나 각 사용자의 환경은 고유하며 시간이 지남에 따라 계속 변화할 수 있기 때문에, 이러한 방법들은 개인화된 가정용 서비스 로봇에는 적합하지 않습니다. 지속적 학습 연구는 시간이 지남에 따라 학습하고 적응할 수 있는 방법을 개발하지만, 대부분의 방법은 정적 이미지 데이터셋에서 객체 분류라는 좁은 맥락에서만 테스트됩니다. 본 논문에서는 지속적 학습, 의미론적 추론, 그리고 상호작용형 머신러닝 문헌의 아이디어를 결합하여, 인간-로봇 상호작용을 통해 가정 환경에서 의미론적 지식을 지속적으로 학습하는 새로운 상호작용형 지속적 학습 아키텍처를 개발합니다. 이 아키텍처는 학습과 기억의 핵심 인지 원리를 기반으로 하여 인간으로부터 새로운 지식을 효율적이고 실시간으로 학습합니다. 우리는 이 아키텍처를 실제 모바일 매니퓰레이터 로봇에 통합하고, 2개월 동안 실험실 환경에서 광범위한 시스템 평가를 수행했습니다. 그 결과, 우리의 아키텍처가 실제 로봇이 사용자(실험자)가 제공한 제한된 데이터로 환경 변화에 지속적으로 적응하고, 학습된 지식을 활용하여 객체 가져오기 작업을 수행할 수 있음을 입증했습니다.
