---
$id: ent_paper_ayub_interactive_continual_learning_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Interactive Continual Learning Architecture for Long-Term Personalization of
    Home Service Robots
  zh: 面向家庭服务机器人长期个性化的交互式持续学习架构
  ko: 가정 서비스 로봇의 장기 개인화를 위한 대화형 지속 학습 아키텍처
summary:
  en: This paper proposes an interactive continual learning architecture that enables
    a mobile manipulator to learn semantic knowledge of objects and contexts from
    real-time human-robot interaction, and validates it through two months of physical
    robot experiments.
  zh: 本文提出了一种交互式持续学习架构，使移动操作机器人能够通过实时人机交互学习物体与环境的语义知识，并通过两个月的物理机器人实验进行了验证。
  ko: 본 논문은 실시간 인간-로봇 상호작용을 통해 물체와 맥락의 의미적 지식을 학습할 수 있는 대화형 지속 학습 아키텍처를 제안하고, 두 달간의
    실제 로봇 실험을 통해 검증하였다.
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
  reviewed_at: '2026-06-27'
  confidence: medium
  notes: AI-extracted from full text; requires human review before verification.
sources:
- id: src_001
  type: paper
  title: Interactive Continual Learning Architecture for Long-Term Personalization
    of Home Service Robots
  url: https://arxiv.org/abs/2403.03462
  date: '2024'
  accessed_at: '2026-06-27'
theoretical_depth:
- method
---

## Overview

This paper addresses the challenge of enabling home service robots to learn and reason about semantic knowledge in dynamic, unstructured environments where each user's home is unique and changes over time. The authors argue that existing semantic reasoning architectures assume all training data is available a priori, while continual learning methods are typically evaluated only on narrow object classification benchmarks. To bridge this gap, they propose an Interactive Continual Learning (ICL) architecture that unifies continual learning, interactive machine learning, and semantic reasoning.

The ICL architecture is built on cognitive principles of learning and memory. It uses a SUSTAIN-inspired clustering network to group similar experiences, dual long-term and short-term memory stores, and a predictive performance equation to model memory fading and consolidation. This design allows the robot to learn new objects and contexts from few examples provided through human-robot interaction, while mitigating catastrophic forgetting of previously learned knowledge.

The system is integrated with a physical Fetch mobile manipulator equipped with a 7-DOF arm, mobile base, LiDAR, and RGB-D camera. Visual processing is handled by a YOLO object detector and a ResNet18 feature extractor pretrained on ImageNet, running on an Nvidia RTX 2060 GPU workstation. The authors conduct extensive system evaluations over two months in a laboratory environment, demonstrating that the robot can continually adapt to environmental changes from limited user-provided data and use the learned semantic knowledge to perform object fetching tasks.

## Key Contributions

- A novel ICL architecture that unifies continual learning, interactive machine learning, and semantic reasoning for real-time, few-shot learning of objects and contexts via human-robot interaction without catastrophic forgetting.
- Cognitively inspired learning and memory mechanisms—including pattern-separation clustering, long-term memory fading, and short-term experience consolidation—that enable efficient adaptation to new knowledge.
- Extensive two-month physical-robot experiments in a large indoor lab demonstrating continual adaptation and successful object-fetching task execution.

## Relevance to Humanoid Robotics

The work is highly relevant to humanoid robotics because it tackles the personalization problem that any general-purpose home humanoid will face: different households have different objects, layouts, and user preferences, and these change over time. The ability to learn semantic knowledge incrementally from natural human-robot interaction, with limited data and without forgetting, is foundational for deploying humanoid robots in unstructured home environments. While the experiments use a Fetch mobile manipulator rather than a humanoid, the cognitive architecture and software mechanisms are transferable to humanoid platforms that must similarly perceive, remember, and act in dynamic domestic settings.
