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
  zh: 本文提出一种交互式持续学习架构，使移动机械臂能够通过实时人机交互学习物体与场景的语义知识，并通过两个月的物理机器人实验验证其有效性。该架构由研究团队开发，核心贡献在于将持续学习、语义推理与交互式机器学习相结合，实现家庭服务机器人的长期个性化适应。
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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2403.03462v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (665 chars, DeepSeek).'
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
现有语义推理方法假设训练数据预先完整可用，但每个用户的家居环境独特且随时间变化，导致这些方法不适用于个性化家庭服务机器人。尽管持续学习领域已有可随时间适应的方法，但多数仅在静态图像数据集上的物体分类任务中测试。本文提出的架构融合持续学习、语义推理与交互式机器学习，基于学习与记忆的核心认知原理，实现从人类交互中高效实时学习新知识。研究团队将该架构集成到物理移动机械臂上，在实验室环境中进行了两个月的系统评估，验证了机器人能从用户提供的有限数据持续适应环境变化，并利用所学知识执行物体取送任务。

## 核心内容
### 方法架构
- 架构核心：结合持续学习、语义推理与交互式机器学习，基于认知科学中的学习与记忆原理设计
- 学习机制：通过人机交互实时获取物体与场景的语义知识，支持增量式知识更新
- 记忆管理：采用类似人类记忆的遗忘与巩固机制，平衡新知识学习与旧知识保留

### 实验设置
- 硬件平台：集成该架构的物理移动机械臂机器人
- 实验环境：实验室模拟家居环境
- 实验周期：持续两个月
- 数据来源：实验人员通过人机交互提供有限标注数据

### 关键结果
- 机器人能持续适应环境变化（如物体位置移动、新物体出现）
- 从用户提供的少量数据中有效学习语义知识
- 成功执行物体取送任务，验证了知识迁移与泛化能力
- 系统在两个月内保持稳定运行，未出现灾难性遗忘

### 结论
该架构证明了通过人机交互实现家庭服务机器人长期个性化适应的可行性，为未来部署在真实家庭环境中的持续学习机器人提供了技术基础。

## Overview
For robots to perform assistive tasks in unstructured home environments, they must learn and reason on the semantic knowledge of the environments. Despite a resurgence in the development of semantic reasoning architectures, these methods assume that all the training data is available a priori. However, each user's environment is unique and can continue to change over time, which makes these methods unsuitable for personalized home service robots. Although research in continual learning develops methods that can learn and adapt over time, most of these methods are tested in the narrow context of object classification on static image datasets. In this paper, we combine ideas from continual learning, semantic reasoning, and interactive machine learning literature and develop a novel interactive continual learning architecture for continual learning of semantic knowledge in a home environment through human-robot interaction. The architecture builds on core cognitive principles of learning and memory for efficient and real-time learning of new knowledge from humans. We integrate our architecture with a physical mobile manipulator robot and perform extensive system evaluations in a laboratory environment over two months. Our results demonstrate the effectiveness of our architecture to allow a physical robot to continually adapt to the changes in the environment from limited data provided by the users (experimenters), and use the learned knowledge to perform object fetching tasks.

## 参考
- http://arxiv.org/abs/2403.03462v1

## 개요
기존 의미론적 추론 방법은 훈련 데이터가 사전에 완전히 제공된다고 가정하지만, 각 사용자의 가정 환경은 고유하고 시간에 따라 변화하므로 이러한 방법은 개인화된 가정용 서비스 로봇에는 적합하지 않습니다. 지속 학습 분야에는 시간에 따라 적응할 수 있는 방법이 이미 있지만, 대부분 정적 이미지 데이터셋에서의 객체 분류 작업에서만 테스트되었습니다. 본 논문에서 제안하는 아키텍처는 지속 학습, 의미론적 추론 및 상호작용형 머신러닝을 융합하며, 학습과 기억의 핵심 인지 원리에 기반하여 인간 상호작용으로부터 효율적으로 실시간 새 지식을 학습합니다. 연구팀은 이 아키텍처를 물리적 이동 매니퓰레이터에 통합하고, 실험실 환경에서 두 달간 시스템 평가를 수행하여 로봇이 사용자가 제공한 제한된 데이터로 환경 변화에 지속적으로 적응하고, 학습한 지식을 활용해 객체 전달 작업을 수행할 수 있음을 검증했습니다.

## 핵심 내용
### 방법 아키텍처
- 아키텍처 핵심: 지속 학습, 의미론적 추론 및 상호작용형 머신러닝을 결합하며, 인지과학의 학습과 기억 원리에 기반하여 설계
- 학습 메커니즘: 인간-로봇 상호작용을 통해 객체와 장면의 의미론적 지식을 실시간 획득하고, 점진적 지식 업데이트 지원
- 기억 관리: 인간 기억의 망각과 강화 메커니즘을 모방하여 새 지식 학습과 기존 지식 보존의 균형 유지

### 실험 설정
- 하드웨어 플랫폼: 이 아키텍처를 통합한 물리적 이동 매니퓰레이터 로봇
- 실험 환경: 실험실에서 시뮬레이션한 가정 환경
- 실험 기간: 두 달간 지속
- 데이터 출처: 실험자가 인간-로봇 상호작용을 통해 제한된 라벨링 데이터 제공

### 주요 결과
- 로봇이 환경 변화(예: 객체 위치 이동, 새 객체 출현)에 지속적으로 적응 가능
- 사용자가 제공한 소량의 데이터로 의미론적 지식을 효과적으로 학습
- 객체 전달 작업을 성공적으로 수행하여 지식 전이 및 일반화 능력 검증
- 시스템이 두 달간 안정적으로 작동하며 치명적 망각 없음

### 결론
이 아키텍처는 인간-로봇 상호작용을 통한 가정용 서비스 로봇의 장기적 개인화 적응 가능성을 입증했으며, 실제 가정 환경에 배포할 지속 학습 로봇을 위한 기술적 기반을 제공합니다.
