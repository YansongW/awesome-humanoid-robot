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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2404.17070v7. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
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

## 개요
이족 보행 로봇은 잠재적 응용 가능성과 인공지능, 특히 심층 강화 학습(DRL)의 발전으로 인해 전 세계적으로 주목받고 있습니다. DRL이 이족 보행 기술을 크게 발전시켰지만, 다양한 작업을 처리할 수 있는 통합 프레임워크의 개발은 여전히 진행 중인 과제입니다. 본 설문 조사는 이족 보행을 위한 기존 DRL 프레임워크를 체계적으로 분류, 비교 및 분석하여 종단 간 제어 방식과 계층적 제어 방식으로 구성합니다. 종단 간 프레임워크는 학습 접근 방식에 따라 평가되며, 계층적 프레임워크는 학습 기반 또는 전통적인 모델 기반 방법을 통합하는 계층 구조 측면에서 검토됩니다. 우리는 각 프레임워크의 구성, 장점, 한계 및 기능에 대한 상세한 평가를 제공합니다. 또한, 본 설문 조사는 주요 연구 격차를 식별하고 실제 환경에서 광범위하게 응용될 수 있는 보다 통합적이고 효율적인 이족 보행 프레임워크를 구축하기 위한 미래 방향을 제안합니다.

## 핵심 내용
이족 보행 로봇은 잠재적 응용 가능성과 인공지능, 특히 심층 강화 학습(DRL)의 발전으로 인해 전 세계적으로 주목받고 있습니다. DRL이 이족 보행 기술을 크게 발전시켰지만, 다양한 작업을 처리할 수 있는 통합 프레임워크의 개발은 여전히 진행 중인 과제입니다. 본 설문 조사는 이족 보행을 위한 기존 DRL 프레임워크를 체계적으로 분류, 비교 및 분석하여 종단 간 제어 방식과 계층적 제어 방식으로 구성합니다. 종단 간 프레임워크는 학습 접근 방식에 따라 평가되며, 계층적 프레임워크는 학습 기반 또는 전통적인 모델 기반 방법을 통합하는 계층 구조 측면에서 검토됩니다. 우리는 각 프레임워크의 구성, 장점, 한계 및 기능에 대한 상세한 평가를 제공합니다. 또한, 본 설문 조사는 주요 연구 격차를 식별하고 실제 환경에서 광범위하게 응용될 수 있는 보다 통합적이고 효율적인 이족 보행 프레임워크를 구축하기 위한 미래 방향을 제안합니다.

## 参考
- http://arxiv.org/abs/2404.17070v7
