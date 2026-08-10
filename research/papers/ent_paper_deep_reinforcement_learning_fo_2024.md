---
$id: ent_paper_deep_reinforcement_learning_fo_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Deep Reinforcement Learning for Bipedal Locomotion: A Brief Survey'
  zh: 'Deep Reinforcement Learning for Bipedal Locomotion: A Brief Survey'
  ko: 'Deep Reinforcement Learning for Bipedal Locomotion: A Brief Survey'
summary:
  en: 'Deep Reinforcement Learning for Bipedal Locomotion: A Brief Survey is a 2024 work on locomotion for humanoid robots.'
  zh: 本文是2024年关于双足机器人运动控制的深度强化学习（DRL）综述。系统分类并比较了端到端与分层控制两种框架，分析了各自的构成、优势与局限。研究指出了当前统一框架缺失的关键问题，并提出了未来发展方向。
  ko: 'Deep Reinforcement Learning for Bipedal Locomotion: A Brief Survey is a 2024 work on locomotion for humanoid robots.'
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- deep_reinforcement_learning_fo
- humanoid
- locomotion
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2404.17070v7. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (695 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: 'Deep Reinforcement Learning for Bipedal Locomotion: A Brief Survey (arXiv)'
  url: https://arxiv.org/abs/2404.17070
  date: '2024'
  accessed_at: '2026-07-01'
---
## 概述
双足机器人因人工智能进步而备受关注，深度强化学习（DRL）极大推动了其运动控制发展，但尚缺乏能处理多种任务的统一框架。本综述将现有DRL框架分为端到端与分层控制两类：端到端框架按学习方法评估，分层框架则考察其整合学习或传统模型方法的层级结构。文章详细评价了各框架的组成、能力与不足，并针对真实环境应用提出了构建更集成高效框架的研究方向。

## 核心内容
### 核心分类与框架分析
- **端到端框架**：直接通过DRL从传感器输入映射到关节动作，按学习方法（如PPO、SAC等）评估，优势在于简化流程，但面临样本效率低与泛化性差的问题。
- **分层控制框架**：采用多层结构，上层负责高层规划（如步态模式），下层执行底层控制（如关节力矩），可整合传统模型预测控制（MPC）或基于模型的强化学习，提升稳定性与任务适应性。

### 关键评估维度
- **组成与能力**：各框架在运动鲁棒性、地形适应性、能耗效率等方面表现不一。例如，端到端方法在复杂地形中易失败，而分层方法通过模块化设计更易处理扰动。
- **局限与挑战**：现有框架普遍缺乏对动态环境（如不平整地面、外力干扰）的泛化能力，且训练成本高（需数百万步仿真迭代）。

### 未来方向
- **统一框架构建**：需融合端到端学习的灵活性与分层控制的稳定性，例如通过元学习或迁移学习减少训练开销。
- **真实世界部署**：需解决仿真到现实（sim-to-real）的差距，包括传感器噪声、硬件延迟与能耗约束。
- **多任务协同**：探索将行走、奔跑、跳跃等运动模式整合至单一DRL策略，避免为每个任务单独训练。

## Overview
Bipedal robots are gaining global recognition due to their potential applications and advancements in artificial intelligence, particularly through Deep Reinforcement Learning (DRL). While DRL has significantly advanced bipedal locomotion, the development of a unified framework capable of handling a wide range of tasks remains an ongoing challenge. This survey systematically categorises, compares, and analyses existing DRL frameworks for bipedal locomotion, organising them into end-to-end and hierarchical control schemes. End-to-end frameworks are evaluated based on their learning approaches, while hierarchical frameworks are examined in terms of layered structures that integrate learning-based or traditional model-based methods. We provide a detailed evaluation of the composition, strengths, limitations, and capabilities of each framework. Additionally, this survey identifies key research gaps and proposes future directions aimed at creating a more integrated and efficient framework for bipedal locomotion, with wide-ranging applications in real-world environments.

## 参考
- http://arxiv.org/abs/2404.17070v7

## 개요
이족 보행 로봇은 인공지능의 발전으로 주목받고 있으며, 심층 강화 학습(DRL)이 그 운동 제어 발전을 크게 촉진했지만, 다양한 작업을 처리할 수 있는 통합 프레임워크는 아직 부족하다. 본综述은 기존 DRL 프레임워크를 종단 간(end-to-end) 및 계층적 제어(hierarchical control) 두 가지 유형으로 분류한다: 종단 간 프레임워크는 학습 방법에 따라 평가하고, 계층적 프레임워크는 학습 또는 전통적 모델 방법을 통합하는 계층 구조를考察한다. 본 논문은 각 프레임워크의 구성, 능력 및 한계를 상세히 평가하고, 실제 환경 적용을 위해 더 통합적이고 효율적인 프레임워크 구축을 위한 연구 방향을 제시한다.

## 핵심 내용
### 핵심 분류 및 프레임워크 분석
- **종단 간 프레임워크**: DRL을 통해 센서 입력에서 관절 토크로 직접 매핑하며, 학습 방법(예: PPO, SAC 등)에 따라 평가된다. 장점은 프로세스 단순화이지만, 샘플 효율성 저하와 일반화 성능 부족 문제에 직면한다.
- **계층적 제어 프레임워크**: 다층 구조를 채택하며, 상위 계층은 고수준 계획(예: 보행 패턴)을 담당하고 하위 계층은 저수준 제어(예: 관절 토크)를 실행한다. 전통적 모델 예측 제어(MPC) 또는 모델 기반 강화 학습을 통합하여 안정성과 작업 적응성을 향상시킬 수 있다.

### 핵심 평가 차원
- **구성 및 능력**: 각 프레임워크는 운동 견고성, 지형 적응성, 에너지 효율성 등에서 성능 차이를 보인다. 예를 들어, 종단 간 방법은 복잡한 지형에서 실패하기 쉬운 반면, 계층적 방법은 모듈식 설계를 통해 외란 처리에 더 유리하다.
- **한계 및 도전 과제**: 기존 프레임워크는 일반적으로 동적 환경(예: 고르지 않은 지면, 외부 힘 간섭)에 대한 일반화 능력이 부족하며, 훈련 비용이 높다(수백만 단계의 시뮬레이션 반복 필요).

### 미래 방향
- **통합 프레임워크 구축**: 종단 간 학습의 유연성과 계층적 제어의 안정성을 융합해야 하며, 예를 들어 메타 학습 또는 전이 학습을 통해 훈련 비용을 절감할 수 있다.
- **실제 세계 배포**: 시뮬레이션-실제(sim-to-real) 격차를 해결해야 하며, 센서 노이즈, 하드웨어 지연 및 에너지 제약을 포함한다.
- **다중 작업 협력**: 걷기, 달리기, 점프 등의 운동 모드를 단일 DRL 정책에 통합하여 작업별 개별 훈련을 피하는 방안을 탐구한다.
